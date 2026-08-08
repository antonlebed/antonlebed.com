"""explore_schedule_image.py -- how MANY limits a pricing schedule has, and
whether counting them needs the ring.

THE QUESTION. A greedy trajectory over the ring of a curve converges to a
divisor whose shape -- one deep coordinate over a support that stays flat --
turns out to be a statement about a PRICING SCHEDULE and not about arithmetic
(explore_price_schedule.py). The companion object is how many such limits
there are: the greedy IMAGE, sized until now by a product, over the
trajectory's surviving openings, of the tie multiplicity at each -- a census,
with the ring supplying every factor. So the same question is owed to it. Is
the image a schedule statement with the ring entering only as a SUPPLY of how
many items each degree has, or is there a point where the ring is genuinely
load-bearing? Either answer is worth having: one collapses a large block of
the corpus one level down, the other NAMES the ring's contribution instead of
assuming it.

THE OBJECT THE ABSTRACT WALKER DOES NOT CARRY. The schedule walker holds no
item identities at all -- its state is, per degree, a list of exponents --
which is exactly why it reproduces the ring engine so cheaply. The image
question is about identities: WHICH item of a degree got seated. So this rig
adds them back. A CONFIGURATION is a function from items (d, i), i indexing
the n_d items of degree d, to exponents >= 0, with 0 meaning unseated; its
SHAPE is the multiset of positive exponents per degree, which is precisely
what the identity-free walker carries. The abstract image at N moves is the
set of configurations reachable in N moves, and the identity-free walker's
own branch tree is the set of reachable SHAPES.

THE HAND-ATTACK, on paper before any engine code, three lemmas.

 L1 THE SYMMETRY. Let G = prod_d S(n_d) permute the items within each degree.
    Everything the walker reads about an item is its degree and its exponent,
    and the supply enters as a COUNT. So G acts by automorphisms of the
    dynamics: applying a permutation to every move of a trajectory gives a
    legal trajectory with the same cost sequence, ending at the permuted
    configuration. Hence the reachable set is G-STABLE. (This is the ring's
    lockstep theorem with the class layer deleted -- there the colouring is
    (degree, class), here it is the degree alone.)
 L2 AN ORBIT IS A SHAPE CLASS. G is transitive on the configurations of a
    fixed shape: at each degree, two such configurations assign one exponent
    multiset to k_d distinct items out of n_d, and some permutation of those
    n_d items carries one assignment to the other. With L1 this says a
    reachable shape's reachable configurations are the WHOLE shape class.
 L3 THE COUNT, by orbit-stabiliser. The stabiliser of a configuration inside
    S(n_d) is the product of the symmetric groups on the fibres of its
    exponent function -- (n_d - k_d)! on the unseated items and mult_d(e)! on
    each repeated exponent e. So

      |shape class| = prod_d  n_d! / [ (n_d - k_d)! * prod_e mult_d(e)! ]

    a MULTINOMIAL coefficient read off the supply and the shape ALONE, and
    the image at N moves is the SUM of that over the reachable shapes. No
    census and no ring: the branch tree of the identity-free walker supplies
    the shapes, the supply vector supplies everything else.

WHAT THE LEMMAS ALREADY DECIDE, fixed here so the run cannot be read as
having discovered them.
 (a) With m fresh discounts and a degree left flat, the factor is C(n_d, m),
     a BINOMIAL and not a falling factorial: the m! ORDERS in which one
     degree's m items are seated reach ONE configuration, and a limit, being
     a divisor, cannot record the order.
 (b) A degree carrying the deep coordinate beside j flat items contributes
     n_d * C(n_d - 1, j) -- the deep item's identity is a free coordinate.
 (c) At b >= 3 the clock hands off and STRANDS an item above exponent 1
     forever. A strand sits at an exponent of its own, hence in a fibre of
     its own, so L1 makes every (strand, deep) pair reachable and the strand
     MULTIPLIES the image rather than being fixed by the choice already made.

WHERE A KILL CAN ACTUALLY LIVE, since L1 to L3 are airtight in a world built
to satisfy L1. Three places, and the sections are aimed at them.
 (i) THE SHAPE-TO-LIMIT MAP. A limit forgets the deep item's finite exponent,
     so two shapes differing only there reach one limit and the sum over
     shapes OVERCOUNTS. What the sum must run over is shapes with the deep
     coordinate's exponent quotiented away, and that is a correction to the
     formula, not a gloss on it.
 (ii) THE RING'S OWN SUPPLIES. The lemmas are about an abstract supply; the
     six ring supplies are where they meet real place counts. What that does
     NOT do is run a ring engine: the transfer to the ring's own ideal-world
     image rides the identity-free walker's certification against the exact
     divisibility walker (explore_price_schedule.py), which equates the two
     menus as (degree, door, kind) multisets and so equates the number of
     choices at every opening -- which is the only thing an orbit size reads.
     A ring engine carrying places would test that transfer directly, and
     nothing here is a substitute for it.
 (iii) WHAT THE PRICE READS. The degree is not privileged in L1 -- what is
     privileged is the colouring the price can see. If the formula is really
     about that, then giving items a COLOUR the price reads must refine the
     group to prod over (degree, colour) and the formula must survive
     verbatim, while the colour-blind formula must then FAIL. That is the
     abstract form of the ring's class layer, and it is testable here.

THE ONE INGREDIENT THAT DOES NOT TRANSLATE, named at the freeze so no section
is later credited with finding it. (The belief below is left as it was
frozen; F7 carries what a later rig corrected in it, and the correction is
about WHICH class the rider cancels.) In the ring's element world a move seats a
BUNDLE whose composition is the minimal representative of the state's
accumulated class -- a price reading the whole seated set rather than
(item, staleness). No dial of the schedule family has that shape. So the
prediction carried in is that the class layer refines the SUPPLY, from a
vector n_d to a matrix n_(d,c), and the rider is what the schedule world
cannot express at all. This rig tests the first half and does not enter the
second.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the identity-free walker to this one: the move model is IMPORTED
    verbatim (doors, ticks, discounts, born-covered degrees), and the control
    below advances both walkers together over the same moves rather than
    trusting the import.
 2. From the shape count to the configuration count: NOTHING is carried. The
    identity-free walker's branch tree counts shapes and says nothing about
    identities; every configuration count here is enumerated with identities
    in, and the formula is checked against that enumeration and never used to
    produce it.
 3. The toy supplies are ABSTRACT. A supply with two items at every degree is
    a legal state of the abstract dynamics and is not certified to be any
    curve's place count.
 4. From the ideal world to the element world: nothing. A rider raises an
    exponent with no clock move; this rig stays in the ideal world, where the
    identity-free walker is certified against the exact engine.

ONE DESIGN CHOICE, inherited rather than made. The fresh discount is given to
OPENINGS only, as in explore_price_schedule.py, where the alternative reading
is argued to be degenerate. It matters here only at m >= 2, which is exactly
where the binomial claim lives, so the claim is a claim about THAT discount.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE IDENTIFIED WALKER IS THE IDENTITY-FREE ONE. What the rig PRINTS: over
    a canonical walk on each supply, the identified menu collapsed to a
    (degree, door, kind) multiset against the identity-free walker's own menu,
    the two minimal costs, the two tick sequences, and the count of states
    compared -- the identity-free walker advanced by the identified walker's
    own move, so no tie convention can make them agree by construction. Both
    walkers stop their menu scan at the first degree that cannot win, so on
    the supplies small enough to scan whole the identified menu is ALSO read
    with the stop rule off, and the rig prints how far.
    KILL: one disagreement, in cost, in any type's multiplicity, or in a tick;
    or a menu the stop rule truncated.
PR2 A REACHABLE SHAPE'S CONFIGURATIONS ARE ITS WHOLE ORBIT. What the rig
    PRINTS: per supply, at a fixed move budget, how many shapes are
    reachable, how many distinct configurations carry them, the SUM of L3's
    multinomial over those shapes, and the widest single shape with its own
    orbit size. Every shape is ASSERTED against its own multinomial; the
    print is the aggregate, the assert is the test.
    KILL: one shape whose enumerated count differs from its multinomial in
    either direction.
PR3 THE DISCOUNT'S FACTOR IS A BINOMIAL. What the rig PRINTS: at m = 1, 2, 3,
    for the first two degrees that reach their full width on a supply, the
    number of distinct seated SETS reachable there and the number of distinct
    seating ORDERS, against C(n_d, m) and the falling factorial.
    KILL: a set count matching neither.
PR4 THE STRAND IS A FREE COORDINATE. What the rig PRINTS: at b = 3 and b = 4,
    over every branch, the degrees the stranded and the deep item sit at, how
    many distinct (strand, deep) pairs occur, and the supply product summed
    over the degree-pairs seen -- the pair count being ASSERTED per
    degree-pair, never against the pooled total; and at b = 2, a pair count
    of zero.
    KILL: a pair set smaller than the product, which is the strand being a
    function of the choice already made; or a strand at b = 2.
PR5 THE SUM OVER SHAPES OVERCOUNTS LIMITS. What the rig PRINTS: over a pooled
    range of move budgets, the number of distinct configurations, the number
    of distinct LIMIT READINGS (the deep item's own exponent forgotten), and
    the shapes that merged.
    KILL: the two counts equal, which would mean nothing merges and the
    correction is empty.
PR6 THE FORMULA TRACKS WHAT THE PRICE READS. What the rig PRINTS: over a
    coloured supply run twice -- equal weights, so the price cannot see the
    colour, and unequal ones, so it can -- the shapes, the configurations,
    the summed colour-refined and colour-blind multinomials, and whether each
    formula holds at EVERY shape.
    KILL: the refined formula failing where the colour is read, or the blind
    one failing where it is not.

The last section is a READOUT and not a test: the formula, once checked,
applied to the six ring supplies over their first ten openings.

FINDINGS (tiers below; run record at the bottom). Every section asserts,
the last one only that its ladder is increasing -- it is a readout and the
numbers in F6 are read, not tested.

F1 THE IMAGE IS A SUM OF ORBIT SIZES, AND EVERY ORBIT IS READ OFF THE SUPPLY
   (proved -- L1 to L3 -- and a rule in range: 8 supplies, 16 reachable
   shapes, 35752 configurations enumerated with identities in at a move
   budget of 8 for the ring supplies and 10 for the toys, 0 shapes off their
   multinomial). Every reachable shape carries exactly its whole orbit:
   F_2[x] 396 configurations over 2 shapes, h2 672 over 2, h3 7920 over 2,
   h4 4864 over 2, h5 16000 over ONE, g2 4608 over 2, and the toys 320 over 3
   and 972 over 2. So the count needs no census. The identity-free walker's
   branch tree supplies the SHAPES -- a small number of them, and it is the
   only thing the dynamics has to be run for -- and the supply vector
   supplies everything else through a multinomial. The corpus's product over
   openings of the tie multiplicity is the special case where every opened
   degree carries one item at exponent 1, and it is a product INSIDE a shape
   where the honest object is a sum over them.

F2 THE DISCOUNT'S FACTOR IS A BINOMIAL, AND THE m! IT DROPS IS THE SEATING
   ORDER (proved as a corollary of L3; rule in range over 4 supplies and 18
   (supply, m, degree) rows, 0 off). At m = 2 over a degree with 3 items:
   3 distinct seated SETS against C(3,2) = 3, and 6 distinct seating ORDERS
   against the falling factorial 3*2 = 6. At m = 3 over the same degree: ONE
   set against C(3,3), still 6 orders. The two counts part by exactly m! at
   every row, which is the ORDER the state records and the limit, being a
   divisor, cannot. A count of trajectories is therefore not a count of
   limits wherever a degree is seated more than once.

F3 THE STRAND IS A FREE COORDINATE AND MULTIPLIES (rule in range; two
   supplies at b = 2, 3 and 4, every branch of each). At b = 2 there is no
   strand at all, 0 pairs at both supplies. At b >= 3 the clock hands off,
   the strand sits at degree 2 and the surviving deep item at degree 1, and
   the (strand, deep) pair set is the FULL product of the two degrees'
   supplies -- 4 = 2*2 at the two-item supply and 9 = 3*3 at the three-item
   one, at b = 3 and again at b = 4, checked per degree-pair and not pooled.
   So which item is stranded is NOT fixed by the choice that fixes the deep
   coordinate: the b >= 3 image carries a factor the b = 2 image does not,
   and one infinite coordinate parting from a flat support costs the count a
   whole coordinate rather than a footnote.

F4 THE SUM OVER SHAPES OVERCOUNTS LIMITS, AND WHAT MERGES IS A CLOCK MOVE
   (rule in range, four supplies over move budgets 3 to 8). A clock move on
   the deep item raises the one exponent a limit forgets and touches nothing
   else, so it takes two shapes to one reading: F_2[x] 487 configurations
   against 461 readings with 26 merged, h2 922 against 847 with 75, and the
   toys 164 against 124 with 40 and 879 against 726 with 153. **And the
   window this was first read over missed it entirely**, which the section
   now prints rather than recounts: budgets 7 and 8 give 444 configurations
   against 444 readings at F_2[x] and nothing merged at any of the four
   supplies, because those two moves contain NO clock move -- the column
   that would say so reads "none". The observable was under-powered and the
   claim was not, and the only reason that is decidable is the clock-step
   column standing beside the merge count; a merge count alone says nothing
   either way, in either direction.

F5 THE FORMULA TRACKS WHAT THE PRICE READS, AND THE DEGREE IS ONE INSTANCE OF
   THAT (rule in range; one coloured supply of 4 items at each of 5 degrees,
   run twice). Where the two colours carry equal weight the price cannot see
   them: 512 configurations, and the colour-blind and colour-refined
   multinomials BOTH give 512. Where they carry weights 1 and 3 the price
   sees them: 32 configurations, the refined formula gives 32 and the blind
   one still says 512. So L1's group is the symmetry group of the READABLE
   COLOURING and not of the degree, and the degree is one instance of it.
   That the ring's own (degree, class) colouring is the same lemma at a finer
   supply -- a supply MATRIX where the ideal world has a vector -- is then a
   DERIVATION from the lockstep theorem and not a measurement, and it covers
   the COLOURING alone: what a class does to the supply, never what a rider
   does to a move (F7).

F6 THE RING SUPPLIES' OWN NUMBERS, from the formula once checked. Over the
   first ten openings: F_2[x] 1.8e11, h2 3.71e11, h3 6.82e13, h4 4.68e13,
   h5 2.31e16, g2 3.23e13. The two the corpus already carried are
   reproduced, and the ladder each is read off shows why they differ -- h5
   opens at degree 4 and never at 1, 2 or 3, so its factors start large.

F7 WHAT DOES NOT TRANSLATE -- two things, and only the first was fixed at
   the freeze. The element world's RIDER seats a bundle whose composition is
   the minimal representative of the state's accumulated class, a price
   reading the whole seated set rather than (item, staleness); no dial of
   this family has that shape and this rig does not enter that world. So what
   F5 shows is that the class layer's contribution to the IMAGE is a supply
   refinement, and what stays open is everything the rider decides.
   (CORRECTED SINCE, explore_class_schedule.py: the description above is
   wrong about WHICH class the rider cancels, and the error mattered. A
   state is an ELEMENT, so every vehicle is principal and the state's
   accumulated class is identically trivial -- the minimal representative of
   it is the empty divisor. What the rider cancels is the class of the CORE
   POWER, so its cost is d*n + m(-n*c), a table on the moving vehicle's own
   colour and its door that reads no seated item at all. What SURVIVES is the
   sentence's conclusion and not its reason: the rider still has no dial in
   this family, because a move here raises ONE item's exponent and a bundle
   raises several -- a shape rather than a price. And "what stays open is
   everything the rider decides" is now closed for the IMAGE, the element
   count being this same multinomial at the (degree, class) colouring.) The
   second is larger and is the run's own residue rather than the freeze's:
   everything here sizes ONE opening, while a count over a trajectory also
   needs HOW MANY openings there are and how many SURVIVE -- and in this
   family a degree is covered only by being opened, so against an infinite
   supply the ladder never exhausts and no schedule run here can stop
   opening. The ring's LOCK therefore has no analogue in the dials as they
   stand, which leaves the cardinality gap exactly where it was.
   (SETTLED SINCE, explore_ladder_stop.py: the covering rule -- "covered only
   by being opened" -- turned out to BE a dial, and one that reads the clock
   stops the ladder outright. What survives verbatim is the scope written
   here: no schedule run IN THIS RIG can stop opening, every one of them
   carrying that rule. What does not is the sentence's reach past this rig --
   the family does have a stop, and the finite image it gives is
   n^(D-1)*(n+1) at supply width n, which is not the ring's 2^t.)

RUN RECORD. One process, CPython, no BLAS. Wall 2.3s, peak working set 49 MB
against the 512 MB ceiling. 212189 checks here and 2092 in the imported
identity-free walker. What the enumeration costs is set by the state count at
S2, which IS the orbit size being verified and so grows with the supplies --
16000 states at the widest, which is why the budgets are 8 and 10 and not
more.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
from math import factorial

import explore_greedy_limit as GL
import explore_coarse_type as CT
import explore_price_schedule as PS

CHECKS = 0

DCAP = 20            # the identified walker's degree bound, asserted against
STATE_CAP = 60000    # distinct identified states carried, asserted against
CONTROL_N = 40       # states of the canonical walk the control compares
BUDGET = 8           # moves enumerated with identities in, the ring supplies
TOY_BUDGET = 10      # moves enumerated with identities in, the toy supplies
EXPAND_CAP = 64      # items a degree may hold before identities cost too much


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def multinomial(n, exps):
    """L3's per-block factor: how many ways the exponent multiset `exps` can
    be assigned to distinct items out of n."""
    k = len(exps)
    if k > n:
        return 0
    out = factorial(n) // factorial(n - k)
    mult = {}
    for e in exps:
        mult[e] = mult.get(e, 0) + 1
    for c in mult.values():
        out //= factorial(c)
    return out


def orbit_size(supply, shape):
    """L3 over all blocks. `supply` maps a block to its item count and `shape`
    maps a block to the sorted tuple of exponents seated in it."""
    out = 1
    for blk, exps in shape.items():
        out *= multinomial(supply[blk], exps)
    return out


# ------------------------------------------------------- the identified walker
class IWalk(object):
    """A state of the abstract dynamics WITH item identities. seat maps an
    item (degree, index) to its exponent; the move model is that of
    explore_price_schedule.py, and the control certifies the import."""

    def __init__(self, npl, sch, tag, dcap=DCAP, colour=None, weight=None,
                 track=False):
        self.track = track          # carry the seating ORDERS, which only the
        self.npl = npl              # discount section needs and every other
                                    # section would pay for
        self.sch = sch
        self.tag = tag
        self.dcap = dcap
        self.colour = colour        # (d, i) -> colour, or None
        self.weight = weight        # colour -> integer multiplier
        self.seat = {}
        self.opens = {}
        self.opened = []
        self.T = 1
        self.step = 0
        self.clocks = []            # (step, item) of every tick-raising move
        # every ORDER of first seatings that reaches this state. Distinct
        # orders can reach one state, which is the whole of the binomial
        # claim, so they are carried on the state and unioned when the
        # enumeration merges two paths -- a count read off the deduplicated
        # states alone would be the configuration count wearing another name.
        self.orders = set([()])
        # is there anything at all past the degree cap? Where there is not,
        # a scan that runs the whole range is COMPLETE rather than truncated,
        # which is the toy supplies' case and not the rings'
        self.beyond = any(npl[d] for d in range(dcap + 1, len(npl)))

    def copy(self):
        s = IWalk(self.npl, self.sch, self.tag, self.dcap, self.colour,
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

    def covered(self, d):
        return d in self.sch.born or self.opens.get(d, 0) >= self.sch.m

    def cost(self, d, i, door):
        c = self.sch.price(d, door)
        if self.colour is not None:
            c *= self.weight[self.colour[(d, i)]]
        return c

    def wmin(self):
        return min(self.weight.values()) if self.colour is not None else 1

    def menu(self, full=False):
        """(cost, [items at that cost]). Two economies, both forced by the
        supplies: the scan stops at the first degree whose cheapest
        conceivable move -- door 1, at the cheapest colour -- already costs
        more than the best found (sound because price(d, 1) is non-decreasing
        in d, which each schedule is checked for once); and a degree's
        UNSEATED items enter as a GROUP, since they are interchangeable and
        share a door, expanded to identities only at the winning cost. Without
        the second, a scan that runs to degree 30 enumerates the 2^30/30 items
        that live there. `full` turns the stop off, and the control runs both
        at every state of a supply small enough to scan whole."""
        byd = {}
        for (d, i), e in self.seat.items():
            byd.setdefault(d, {})[i] = e
        best, cands = None, []
        w = self.wmin()
        stopped = False
        for d in range(1, self.dcap + 1):
            if best is not None and self.sch.price(d, 1) * w > best:
                stopped = True
                if not full:
                    break
            if self.npl[d] == 0:
                continue
            row = byd.get(d, {})
            start = len(cands)
            for i, e in sorted(row.items()):
                c = self.cost(d, i, max(1, self.T + 1 - e))
                cands.append((c, d, i, max(1, self.T + 1 - e), "move"))
            if len(row) < self.npl[d]:
                door = 1 if not self.covered(d) else self.T + 1
                if self.colour is None:
                    cands.append((self.sch.price(d, door), d, None, door,
                                  "open"))
                else:
                    ok(self.npl[d] <= EXPAND_CAP,
                       "%s: degree %d holds %d coloured items"
                       % (self.tag, d, self.npl[d]))
                    for i in range(self.npl[d]):
                        if i not in row:
                            cands.append((self.cost(d, i, door), d, i, door,
                                          "open"))
            for c in cands[start:]:
                if best is None or c[0] < best:
                    best = c[0]
        ok(best is not None, "%s: an empty menu" % self.tag)
        # the scan reaching the degree cap without the stop rule firing is a
        # SILENT truncation -- the one failure this economy can produce, and
        # nothing else in the rig would notice it
        ok(stopped or not self.beyond,
           "%s: the menu scan ran to the degree cap %d without the stop rule "
           "firing, and the supply has items past it, so the menu is a "
           "truncation" % (self.tag, self.dcap))
        out = []
        for c, d, i, door, kind in cands:
            if c != best:
                continue
            mult = 1 if i is not None else self.npl[d] - len(byd.get(d, {}))
            out.append((d, i, door, kind, mult))
        return best, sorted(out, key=lambda x: (x[0], -1 if x[1] is None
                                                else x[1], x[2], x[3]))

    def collapse(self, entries):
        """The menu as the identity-free walker reads it: a multiset over
        (degree, door, kind)."""
        out = {}
        for d, i, door, kind, mult in entries:
            out[(d, door, kind)] = out.get((d, door, kind), 0) + mult
        return out

    def first_move(self, entries):
        """One identified move from the least menu entry -- the canonical
        continuation, and the only thing a single walk needs. It gives a group
        its least unseated item, so it costs nothing at a degree with a
        million items."""
        d, i, door, kind, _ = entries[0]
        if i is None:
            # `next`, never `min`: a degree deep in the ladder holds millions
            # of items and min would walk every one of them
            i = next(j for j in range(self.npl[d])
                     if (d, j) not in self.seat)
        return (d, i, door, kind)

    def choices(self, entries):
        """The menu with identities in: a group of unseated items becomes one
        move per item. Only affordable where the winning degree is small,
        which is asserted rather than hoped for."""
        byd = {}
        for (d, i), e in self.seat.items():
            byd.setdefault(d, {})[i] = e
        out = []
        for d, i, door, kind, mult in entries:
            if i is not None:
                out.append((d, i, door, kind))
                continue
            ok(self.npl[d] <= EXPAND_CAP,
               "%s: the winning move is at degree %d, which holds %d items -- "
               "too many to give identities to" % (self.tag, d, self.npl[d]))
            for j in range(self.npl[d]):
                if j not in byd.get(d, {}):
                    out.append((d, j, door, kind))
        return sorted(out)

    def apply(self, mv):
        d, i, door, kind = mv
        e0 = self.seat.get((d, i), 0)
        ok(e0 == 0 if kind == "open" else e0 > 0,
           "%s: a %s move at a %s item" % (self.tag, kind,
                                           "seated" if e0 else "bare"))
        if kind == "open":
            if not self.covered(d):
                if self.opens.get(d, 0) == 0:
                    self.opened.append(d)
                self.opens[d] = self.opens.get(d, 0) + 1
            if self.track:
                self.orders = set(o + ((d, i),) for o in self.orders)
        self.seat[(d, i)] = e0 + door
        Tb = self.T
        while self.T < self.seat[(d, i)]:
            self.T = self.sch.tick_up(self.T)
        if self.T > Tb:
            ok(self.seat[(d, i)] == Tb + 1,
               "%s: a tick-raising move landed at %d, not %d"
               % (self.tag, self.seat[(d, i)], Tb + 1))
            self.clocks.append((self.step, (d, i)))
        ok(max(self.opened or [0]) <= self.dcap - 4,
           "%s: the ladder reached degree %d against a cap of %d, so the menu "
           "is a truncation" % (self.tag, max(self.opened or [0]), self.dcap))
        self.step += 1
        return Tb, self.T

    def key(self):
        return (tuple(sorted((d, i, e) for (d, i), e in self.seat.items())),
                self.T)

    def config(self):
        return tuple(sorted((d, i, e) for (d, i), e in self.seat.items()))

    def block(self, it, refined):
        """The colouring the price can read: the degree, or (degree, colour).
        Read PER ITEM and only for the seated ones -- a map over the whole
        universe would materialise every item of every degree in range, which
        at these supplies is a hundred thousand entries per state."""
        if refined and self.colour is not None:
            return (it[0], self.colour[it])
        return it[0]

    def shape(self, refined=True):
        out = {}
        for it, e in self.seat.items():
            out.setdefault(self.block(it, refined), []).append(e)
        return dict((b, tuple(sorted(v))) for b, v in out.items())

    def deep(self):
        """The item the LAST clock move went to -- the coordinate that runs
        away. None before any clock move.

        SOUND BECAUSE THIS WALKER HAS ONE CLOCK (self.T is a scalar), which is
        the premise this identification carried unstated until
        explore_headed_image.py F1 measured it: a clock rises only where the
        landing exponent exceeds the tick, so a clock mover sits above
        exponent 1, and with a single clock the limit theorem makes exactly
        one coordinate recurrent. Under a PER-ITEM clock the last clock mover
        is the recurrent item at 4.6% of states, so nothing here transfers to
        a walker whose clock is per-item -- and explore_tick_pump.py's
        `reading` inherited this identification from here."""
        return self.clocks[-1][1] if self.clocks else None

    def strands(self):
        """Items above exponent 1 that are not the deep one."""
        dp = self.deep()
        return sorted(it for it, e in self.seat.items() if e > 1 and it != dp)

    def reading(self):
        """The LIMIT as this state determines it: which item runs away, and
        the exponent of every other seated item. The deep item's own exponent
        is forgotten, being infinite in the limit."""
        dp = self.deep()
        return (dp, tuple(sorted((it, e) for it, e in self.seat.items()
                                 if it != dp)))


def supply_of(npl, dcap=DCAP):
    return dict((d, npl[d]) for d in range(1, dcap + 1))


def supply_blocks(npl, colour, dcap=DCAP):
    out = {}
    for d in range(1, dcap + 1):
        for i in range(npl[d]):
            b = (d, colour[(d, i)])
            out[b] = out.get(b, 0) + 1
    return out


def reach(npl, sch, tag, n, colour=None, weight=None, dcap=DCAP, track=False):
    """Every distinct identified state reachable in n moves by any tie
    choice. The cap is asserted against, so a truncation cannot pass as a
    count."""
    root = IWalk(npl, sch, tag, dcap, colour, weight, track)
    live = {root.key(): root}
    for _ in range(n):
        nxt = {}
        for s in live.values():
            _, entries = s.menu()
            for mv in s.choices(entries):
                s2 = s.copy()
                s2.apply(mv)
                have = nxt.get(s2.key())
                if have is None:
                    nxt[s2.key()] = s2
                elif track:
                    have.orders |= s2.orders
        ok(len(nxt) <= STATE_CAP,
           "%s: %d states at one depth, over the cap" % (tag, len(nxt)))
        live = nxt
    return list(live.values())


def by_shape(states, refined=True):
    out = {}
    for s in states:
        out.setdefault(tuple(sorted(s.shape(refined).items())), set()).add(
            s.config())
    return out


# ------------------------------------------------------ S0 forced failures
def s0_forced(supplies):
    """Every check the run leans on, made to fail once."""
    npl = supplies["F_2[x]"]
    sch = PS.Sched("corner")
    fired = []

    # (a) the control, given a walker whose clock triples -- menus must part
    try:
        control(npl, PS.Sched("b=3", b=3), "forced", 6, cross=sch)
        fired.append(("control", False))
    except AssertionError:
        fired.append(("control", True))

    # (b) the orbit count, read with a supply one item short at a degree the
    # short walk actually seats -- a degree it never reaches cannot break it
    bad = list(npl)
    bad[1] -= 1
    try:
        states = reach(npl, sch, "forced", 6)
        check_orbits(states, supply_of(bad), "forced")
        fired.append(("orbit", False))
    except AssertionError:
        fired.append(("orbit", True))

    # (c) the degree cap, forced low enough that the ladder reaches it
    try:
        reach(npl, sch, "forced", 8, dcap=6)
        fired.append(("degree cap", False))
    except AssertionError:
        fired.append(("degree cap", True))

    # (d) the menu truncation, the failure path the scan economy can produce.
    # It needs every degree in range already COVERED -- with a fresh discount
    # anywhere the menu's best is that degree's own price and the scan stops
    # at once, which is why no ordinary state here can truncate
    try:
        w = IWalk(npl, PS.Sched("forced", born=tuple(range(1, 7))), "forced", 6)
        w.T = 100
        w.menu()
        fired.append(("truncation", False))
    except AssertionError:
        fired.append(("truncation", True))

    # (e) the state cap, forced to one state
    global STATE_CAP
    keep, STATE_CAP = STATE_CAP, 1
    try:
        reach(npl, sch, "forced", 4)
        fired.append(("state cap", False))
    except AssertionError:
        fired.append(("state cap", True))
    finally:
        STATE_CAP = keep

    for name, hit in fired:
        print("  %-12s forced to fail: %s" % (name, "yes" if hit else "NO"))
        ok(hit, "the %s check did not fail when broken" % name)


# ------------------------------------------------------------- S1 the control
def control(npl, sch, tag, n, cross=None, dcap=60, brute=0):
    """PR1: advance the identity-free walker by the identified walker's own
    move and compare the two menus at every state. The identified walker gets
    a generous degree cap here, the walk being one branch rather than a tree,
    so a menu disagreement cannot be its truncation. `brute` scans every
    degree up to it with no stop rule, which certifies the stop rule itself --
    only affordable where every degree in range holds few items."""
    a = IWalk(npl, sch, tag, dcap)
    b = PS.Walk(npl, cross if cross is not None else sch, tag)
    seen = 0
    for _ in range(n):
        ca, entries = a.menu()
        cb, ties = b.menu()
        coll = a.collapse(entries)
        ok(ca == cb, "%s: costs %d and %d part at state %d"
           % (tag, ca, cb, seen))
        ok(coll == ties, "%s: menus %s and %s part at state %d"
           % (tag, sorted(coll.items()), sorted(ties.items()), seen))
        if brute:
            b0 = IWalk(npl, sch, tag, brute)
            b0.seat, b0.opens, b0.T = dict(a.seat), dict(a.opens), a.T
            cf, mf = b0.menu(full=True)
            ok((cf, b0.collapse(mf)) == (ca, coll),
               "%s: the stop rule truncated the menu at state %d -- %s "
               "against %s" % (tag, seen, sorted(coll.items()),
                               sorted(b0.collapse(mf).items())))
        mv = a.first_move(entries)
        Tb, Ta = a.apply(mv)
        _, _, Tb2, Ta2 = b.apply((mv[0], mv[2], mv[3]))
        ok((Tb, Ta) == (Tb2, Ta2),
           "%s: ticks %s and %s part at state %d"
           % (tag, (Tb, Ta), (Tb2, Ta2), seen))
        seen += 1
    return seen


def s1_control(supplies, names, brute_names=()):
    print("  supply     states  final tick  opened  brute-scanned"
          "  cost of the last move")
    for name in names:
        br = 24 if name in brute_names else 0
        seen = control(supplies[name], PS.Sched("corner"), name, CONTROL_N,
                       brute=br)
        a = IWalk(supplies[name], PS.Sched("corner"), name, dcap=60)
        for _ in range(CONTROL_N):
            c, entries = a.menu()
            a.apply(a.first_move(entries))
        print("  %-10s %-7d %-11d %-7d %-14s %d"
              % (name, seen, a.T, len(a.opened),
                 "to degree %d" % br if br else "-", c))


# ----------------------------------------------------------- S2 the orbits
def check_orbits(states, supply, tag, refined=True, want=True):
    """PR2: every reachable shape's configurations against L3's multinomial.
    Returns (shapes, configs, the per-shape rows)."""
    rows = []
    groups = by_shape(states, refined)
    for shp, cfgs in sorted(groups.items()):
        pred = orbit_size(supply, dict(shp))
        rows.append((shp, len(cfgs), pred))
        if want:
            ok(len(cfgs) == pred,
               "%s: shape %s carries %d configurations against an orbit of %d"
               % (tag, shp, len(cfgs), pred))
    return len(groups), sum(len(c) for c in groups.values()), rows


def s2_orbits(supplies, names, budget):
    print("  supply     states  shapes  configurations  orbit sum  widest shape")
    for name in names:
        npl = supplies[name]
        states = reach(npl, PS.Sched("corner"), name, budget)
        nsh, ncf, rows = check_orbits(states, supply_of(npl), name)
        tot = sum(p for _, _, p in rows)
        widest = max(rows, key=lambda r: r[2])
        ok(ncf == tot, "%s: %d configurations against an orbit sum of %d"
           % (name, ncf, tot))
        print("  %-10s %-7d %-7d %-15d %-10d %s"
              % (name, len(states), nsh, ncf, tot,
                 ",".join("d%d:%s" % (b, "".join(str(e) for e in ex))
                          for b, ex in widest[0]) + " = %d" % widest[2]))


# -------------------------------------------------------- S3 the discount
def s3_discount(supplies, budgets):
    print("  supply     m  degree  n_d  width  distinct sets  C(n,m)"
          "  distinct orders  falling")
    for name, budget in budgets:
        npl = supplies[name]
        for m in (1, 2, 3):
            sch = PS.Sched("m=%d" % m, m=m)
            states = reach(npl, sch, "%s/m=%d" % (name, m), budget, track=True)
            # a degree at its full width with every item flat: the case (a)
            # of the freeze, read off the seated sets and the seating orders
            shown = 0
            for d in sorted(set(dd for s in states for dd in s.opened)):
                flat = [s for s in states
                        if len([1 for (dd, i), e in s.seat.items()
                                if dd == d and e == 1]) == m
                        and not [1 for (dd, i), e in s.seat.items()
                                 if dd == d and e != 1]]
                if not flat or npl[d] < m:
                    continue
                sets = set(frozenset(i for (dd, i), e in s.seat.items()
                                     if dd == d) for s in flat)
                orders = set(tuple(i for (dd, i) in o if dd == d)
                             for s in flat for o in s.orders)
                binom = factorial(npl[d]) // (factorial(m)
                                              * factorial(npl[d] - m))
                fall = factorial(npl[d]) // factorial(npl[d] - m)
                print("  %-10s %-2d %-7d %-4d %-6d %-14d %-7d %-16d %d"
                      % (name, m, d, npl[d], m, len(sets), binom,
                         len(orders), fall))
                ok(len(sets) == binom,
                   "%s/m=%d: degree %d reaches %d seated sets, against a "
                   "binomial of %d and a falling factorial of %d"
                   % (name, m, d, len(sets), binom, fall))
                ok(len(orders) == fall,
                   "%s/m=%d: degree %d reaches %d seating orders, against %d"
                   % (name, m, d, len(orders), fall))
                shown += 1
                if shown == 2:
                    break


# --------------------------------------------------------- S4 the strand
def s4_strand(supplies, names, budget):
    print("  supply     b    branches  strand degrees  deep degrees"
          "  pairs  supply product")
    for name in names:
        for b in (2, 3, 4):
            sch = PS.Sched("b=%d" % b, b=b)
            states = reach(supplies[name], sch, "%s/b=%d" % (name, b), budget)
            pairs = set()
            for s in states:
                for st in s.strands():
                    pairs.add((st, s.deep()))
            if b == 2:
                print("  %-10s %-4d %-9d %-15s %-13s %-6d %s"
                      % (name, b, len(states), "-", "-", len(pairs), "-"))
                ok(not pairs, "%s/b=2: %d strands where none is expected"
                   % (name, len(pairs)))
                continue
            # PER DEGREE-PAIR, never pooled: a total over degree-pairs can
            # match a supply product while some pair is short, and it is the
            # pair that says whether the strand is free
            npl = supplies[name]
            deg = {}
            for st, dp in pairs:
                deg.setdefault((st[0], dp[0]), set()).add((st, dp))
            prod = 0
            for (x, y), got in sorted(deg.items()):
                want = npl[x] * npl[y] - (npl[x] if x == y else 0)
                prod += want
                ok(len(got) == want,
                   "%s/b=%d: strand degree %d against deep degree %d reaches "
                   "%d pairs, against a supply product of %d, so the strand "
                   "is not a free coordinate" % (name, b, x, y, len(got), want))
            print("  %-10s %-4d %-9d %-15s %-13s %-6d %d"
                  % (name, b, len(states),
                     ",".join(str(x) for x, _ in sorted(deg)) or "-",
                     ",".join(str(y) for _, y in sorted(deg)) or "-",
                     len(pairs), prod))
            ok(pairs, "%s/b=%d: no strand at all" % (name, b))
            ok(len(pairs) == prod,
               "%s/b=%d: %d (strand, deep) pairs against a supply product of "
               "%d" % (name, b, len(pairs), prod))


# ---------------------------------------------------------- S5 the merge
def s5_merge(supplies, names, budgets, want=True):
    """PR5. What merges two configurations into one limit is a CLOCK MOVE on
    the deep item, which raises the one exponent the limit forgets and touches
    nothing else. So the observable is only alive over a window of move
    budgets that CONTAINS a clock move, and the clock's steps are printed
    beside the counts rather than assumed to fall inside."""
    print("  supply     budgets  states  clock steps in window"
          "  configurations  limit readings  merged")
    for name in names:
        states = []
        for n in budgets:
            states += reach(supplies[name], PS.Sched("corner"), name, n)
        cfg = set(s.config() for s in states)
        rd = {}
        for s in states:
            rd.setdefault(s.reading(), set()).add(s.config())
        merged = sum(1 for v in rd.values() if len(v) > 1)
        steps = sorted(set(st for s in states for st, _ in s.clocks
                           if min(budgets) <= st + 1 <= max(budgets)))
        print("  %-10s %-8s %-7d %-22s %-15d %-15d %d"
              % (name, "%d-%d" % (min(budgets), max(budgets)), len(states),
                 ",".join(str(x) for x in steps) or "none",
                 len(cfg), len(rd), merged))
        if want:
            ok(len(rd) < len(cfg),
               "%s: %d readings against %d configurations, so nothing merged"
               % (name, len(rd), len(cfg)))
            ok(merged, "%s: no shape merged" % name)
        else:
            # BOTH halves, since the finding is the implication and not
            # either fact: this window holds no clock move, and nothing in
            # it merges. Asserting only the second would let a window that
            # did hold one pass as evidence for a window that does not.
            ok(not steps,
               "%s: the narrow window holds clock moves at %s, so a zero "
               "merge count there is not the under-powering it is read as"
               % (name, steps))
            ok(not merged,
               "%s: the window with no clock move in it merged %d shapes, so "
               "it was not under-powered after all" % (name, merged))


# --------------------------------------------------------- S6 the colour
def s6_colour(budget):
    """PR6: the same supply with a colour the price reads and a colour it
    cannot, against both the blind and the refined multinomial."""
    npl = [0] * (PS.DEG_CAP + 2)
    for d in range(1, 6):
        npl[d] = 4
    colour = dict(((d, i), i % 2) for d in range(1, 6) for i in range(4))
    print("  weights     shapes  configurations  refined sum  blind sum"
          "  refined  blind")
    for tag, wt in (("1,1 blind", {0: 1, 1: 1}), ("1,3 read", {0: 1, 1: 3})):
        sch = PS.Sched("corner")
        states = reach(npl, sch, tag, budget, colour=colour, weight=wt)
        sup_r = supply_blocks(npl, colour)
        sup_b = supply_of(npl)
        _, ncf, rows_r = check_orbits(states, sup_r, tag, refined=True,
                                      want=False)
        nsh, _, rows_b = check_orbits(states, sup_b, tag, refined=False,
                                      want=False)
        okr = all(c == p for _, c, p in rows_r)
        okb = all(c == p for _, c, p in rows_b)
        print("  %-11s %-7d %-15d %-12d %-10d %-8s %s"
              % (tag, nsh, ncf, sum(p for _, _, p in rows_r),
                 sum(p for _, _, p in rows_b),
                 "yes" if okr else "NO", "yes" if okb else "NO"))
        ok(okr, "%s: the colour-refined formula fails" % tag)
        if wt[0] != wt[1]:
            ok(not okb,
               "%s: the colour-BLIND formula still holds where the price "
               "reads the colour" % tag)
        else:
            ok(okb, "%s: the colour-blind formula fails where the price "
               "cannot read the colour" % tag)


# ------------------------------------------------------- S7 the ring supplies
def s7_rings(supplies, names, k=10):
    """A READOUT, not a test: the formula applied over the first k openings of
    each ring supply, the ladder being the degrees the fresh discount opens in
    order. The deep coordinate's own factor is printed beside it."""
    print("  supply     first %d opened degrees                 image over "
          "them" % k)
    for name in names:
        npl = supplies[name]
        s = IWalk(npl, PS.Sched("corner"), name, dcap=60)
        while len(s.opened) < k:
            _, entries = s.menu()
            s.apply(s.first_move(entries))
        degs = s.opened[:k]
        # the one thing a readout can still be wrong about: the fresh ladder
        # opens degrees in strictly increasing order, which is what makes
        # "the first k openings" a well-defined set of degrees at all
        ok(all(b > a for a, b in zip(degs, degs[1:])),
           "%s: the ladder opened %s, which is not increasing" % (name, degs))
        tot = 1
        for d in degs:
            tot *= npl[d]
        print("  %-10s %-38s %.3g"
              % (name, ",".join("%d(%d)" % (d, npl[d]) for d in degs), tot))


# ------------------------------------------------------------------- main
def main():
    supplies, ring_names = {}, []
    for L in CT.build_ladder():
        _, npl, _, _ = GL.universe(L)
        supplies[L.name] = npl
        ring_names.append(L.name)
    for tag, n, hi in (("toy2", 2, 8), ("toy3", 3, 6)):
        npl = [0] * (PS.DEG_CAP + 2)
        for d in range(1, hi + 1):
            npl[d] = n
        supplies[tag] = npl
    toy_names = ["toy2", "toy3"]

    section("S0  THE HARNESS FORCED TO FAIL")
    for sch in (PS.Sched("corner"), PS.Sched("b=3", b=3), PS.Sched("b=4", b=4),
                PS.Sched("m=2", m=2), PS.Sched("m=3", m=3)):
        sch.check_monotone(120)
    s0_forced(supplies)

    section("S1  THE POSITIVE CONTROL -- IDENTITIES CHANGE NO MENU")
    s1_control(supplies, ring_names + toy_names, brute_names=toy_names)

    section("S2  A REACHABLE SHAPE'S CONFIGURATIONS ARE ITS WHOLE ORBIT")
    print("  Every tie choice followed with identities in, grouped by the")
    print("  shape the identity-free walker carries, against L3.")
    s2_orbits(supplies, ring_names, BUDGET)
    s2_orbits(supplies, toy_names, TOY_BUDGET)

    section("S3  THE DISCOUNT'S FACTOR")
    s3_discount(supplies, [(n, TOY_BUDGET) for n in toy_names]
                + [("F_2[x]", BUDGET - 1), ("g2", BUDGET - 1)])

    section("S4  THE STRAND")
    s4_strand(supplies, toy_names, BUDGET)

    section("S5  THE SHAPES THAT MERGE")
    print("  First the window this was read over BEFORE the clock's steps")
    print("  were printed beside it -- two adjacent budgets, which contain no")
    print("  clock move on these supplies and so cannot merge anything. The")
    print("  kill it fires is the observable's, not the claim's.")
    s5_merge(supplies, ring_names[:2] + toy_names, [BUDGET - 1, BUDGET],
             want=False)
    print("\n  And the same reading over a window that does contain one:")
    s5_merge(supplies, ring_names[:2] + toy_names,
             list(range(BUDGET - 5, BUDGET + 1)))

    section("S6  WHAT THE PRICE READS")
    s6_colour(BUDGET - 1)

    section("S7  THE RING SUPPLIES' OWN NUMBERS")
    s7_rings(supplies, ring_names)

    section("SUMMARY")
    print("  %d checks passed here, %d in the imported walker."
          % (CHECKS, PS.CHECKS))


if __name__ == "__main__":
    main()
