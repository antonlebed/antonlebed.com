"""explore_class_schedule.py -- is the RIDER a price, and does the abstract
pricing schedule reach the element world?

THE QUESTION. The greedy dynamics over the ring of a curve is reproduced
move for move by an abstract walker carrying no arithmetic at all: items with
an integer DEGREE, a global CLOCK, a price of degree times staleness, a
one-per-degree fresh discount, and a SUPPLY VECTOR of how many items each
degree has (explore_price_schedule.py). Its image is then a sum, over the
reachable shapes, of a multinomial read off that vector
(explore_schedule_image.py). Both results are about the IDEAL world. The
element world has one ingredient no dial of that family expresses: a move
does not seat a single item, it seats a BUNDLE -- a core P^n together with
the minimal effective divisor of the class P^n must cancel, so that the
vehicle is principal and the state stays an element rather than an ideal.
That bundle is the RIDER. This rig asks whether the rider is a price, and
what the element world's image is if it is.

THE SETTING, abstracted. A COLOURED SUPPLY is a finite abelian group C, given
by its addition table, together with a count n(d, c) of items at each
(degree, class). An item is (d, c, i). For a class x write m(x) for the least
total degree of an effective multiset of items whose classes sum to x, with
m(0) = 0, and MINREP(x) for a multiset attaining it. A move takes a core item
X of colour (d, c) at door n and seats

    X^n  +  MINREP(-n*c),      of cost  d*n + m(-n*c),

exponents merging where the rider lands on the core's own item. The door rule
is the ideal world's verbatim -- 1 for opening an item of an uncovered
degree, T + 1 - e otherwise -- while COVERING is taken in the RING's form
rather than that walker's: a degree is covered once some seated item's degree
is divisible by it, degree 1 born covered since 2^1 - 1 divides every tick
(flag 1 below, and S0 measures where the two forms part).
Everything the ring supplies to that is the group C and the matrix n(d, c) --
m and MINREP are DERIVED from the matrix here and never handed in, which is
the whole of what is being tested.

THE HAND-ATTACK, on paper before any engine code.

 D1 THE RIDER SPLITS INTO A SURCHARGE AND A BUNDLE, and only one half is a
    price. Its COST, d*n + m(-n*c), is a function of the core's colour and
    its door alone -- it reads no other seated item, and the state enters
    only through the door, exactly as in the ideal world. So the cost half is
    a price in a family whose prices read a COLOUR instead of a degree, which
    explore_schedule_image.py already showed is the right widening. Its
    EFFECT is not: the move raises the exponents of items other than the
    core, and no member of a family in which a move raises ONE item's
    exponent can express that, whatever its price. So "is the rider a price"
    has two answers and they differ, and this is fixed here so that no
    section below is credited with finding it.
 D2 THE BARE DOOR IS NEVER BEATEN, with no genus and no ring. The menu must
    offer a core exponent above its door, since a longer core can summon a
    cheaper rider. It never wins: MINREP(-(n+j)c) together with j copies of
    the core is an effective multiset of class -n*c, so
    m(-n*c) <= j*d + m(-(n+j)c), which is exactly cost(n) <= cost(n+j). The
    only hypothesis is that m is a minimum, so the six-ring statement of
    explore_coarse_type.py is a schedule fact rather than an arithmetic one.
    The rig OFFERS the offsets anyway and asserts none wins.
 D3 THE SYMMETRY. Let G = prod over colours of S(n(d, c)), permuting items
    within a colour. The dynamics reads degree, class, the group law and the
    minrep map. G preserves the first three by construction; whether it
    preserves the fourth is the whole question, and it is exactly the
    UNIQUENESS of minimal representatives. If MINREP(x) is unique for every
    x then no item in its support shares a colour with another item -- a
    second item of that colour would give a second representative of the same
    degree and class -- so G fixes every rider pointwise, G acts by
    automorphisms of the dynamics, and the orbit-count argument of
    explore_schedule_image.py runs verbatim at the REFINED colouring:

      |shape class| = prod over colours  n! / [ (n - k)! * prod_e mult(e)! ]

    with the shape now a multiset of positive exponents PER COLOUR. Where
    uniqueness fails the map is set-valued and the reading matters, which is
    D4.
 D4 WHERE THE GATE FAILS there are two readings and they cannot both be
    right. Under SUMMON-ALL the menu offers every minimal representative;
    G permutes them, the dynamics is equivariant again and the formula
    survives at a larger shape set. Under CANONICAL-CHOICE the move takes one
    representative fixed in advance; G no longer preserves the minrep map,
    and the formula must fail. Every ring the corpus walks has unique
    minimal representatives, so which reading a curve realizes is not a
    question a ring can be asked -- the abstract world is where a failed gate
    exists at all.
 D5 TWO THINGS THE BUNDLE CAN DO THAT THE IDEAL WORLD CANNOT, both consequences
    of the rider landing on items of its own choosing rather than the core's.
    A rider can seat an item of a degree no opening has reached, COVERING that
    degree for free and shortening the ladder; and a rider can raise an item
    above the tick, which is a CLOCK MOVE bought without a clock move being
    chosen. Both are observables below, neither is assumed.

PREDICTIONS, frozen here before the engine runs.
 PR1 (positive control) At the trivial group the walker is the ideal-world
     walker: same menus as (degree, door, kind) multisets and same states at
     every step against explore_price_schedule.py's, over every schedule and
     supply run, and no move a bundle.
 PR2 (positive control) Over the six rings, with the supply matrix read off
     the ring and m and MINREP derived from that matrix alone, the abstract
     menu equals the ring engine's element menu VEHICLE FOR VEHICLE under the
     item-to-place bijection, at every state of the ring's own greedy walk.
 PR3 D2's offsets never win, at every ring and every supply.
 PR4 Every reachable shape carries its whole refined orbit, 0 shapes off the
     multinomial; and the DEGREE-blind multinomial, which is the ideal
     world's formula, is wrong somewhere -- it must be, or the class layer
     would be invisible to the count.
 PR5 At a failed gate, SUMMON-ALL holds the formula and CANONICAL-CHOICE
     breaks it. If CANONICAL-CHOICE also holds, D3's necessity direction is
     wrong and the minrep map is not what the group has to preserve.
 PR6 No rider raises an item above the tick, over the six rings' own walks.
     This is a re-derivation of a measured zero, and the abstract reason is
     that a rider's exponent is at most its multiplicity in a minimal
     representative, which is small where the tick is large.
 PR7 A rider covers a degree before any opening reaches it. UNKNOWN at the
     freeze: the observable is the count and there is no prediction. The
     competing consideration is that the cheapest core summons the cheapest
     rider, so a rider of degree 2 is offered only where every degree-1 one
     is already seated -- which the ladder may reach first.

KILL-SHAPE, named as an observable. A reachable shape, at a supply with
unique minimal representatives, whose configuration set is a PROPER SUBSET of
its refined orbit. That would mean the class layer is not a colouring, the
supply matrix is not what the ring contributes, and the four questions this
rig collapses into one are four again.

TRANSPLANT FLAGS, fixed at the freeze. Every intuition below is carried from
a neighbouring parameter value and is marked rather than trusted.
 1. From the ideal world's walker to this one: the door rule and the tick
    rule are IMPORTED verbatim, and S0 advances both walkers over the same
    moves rather than trusting the import. The COVERING rule is NOT imported
    -- explore_price_schedule.py covers a degree once its fresh discounts are
    spent THERE, and this rig uses the ring's own divisibility form, a degree
    covered once some seated item's degree is divisible by it. The two are
    theorems of each other along a ring's ladder and need not agree off it,
    and a rider seats items no opening chose, which is exactly what a
    discount count cannot book. S0 therefore COMPARES the two covered sets at
    every step and prints where they part, rather than either rule being
    assumed to be the other.
 2. From the ideal world's orbit count: NOTHING is carried. Every
    configuration count here is enumerated with identities in, and the
    multinomial is checked against that enumeration and never used to
    produce it.
 3. From the ring to the abstract supply: the matrix and the group table are
    READ OFF the ring; m and MINREP are recomputed from the matrix and
    asserted against the ring's own, rather than imported.
 4. From the function fields to the number rings: NOTHING. The number-ring
    element engine enumerates by norm, has no genus, and its degrees are
    logarithms rather than integers; whether the walker here reaches it is
    left open and named.
    (SINCE RUN, and it reaches: the walker's menu is the number-ring
    engines' at 675 states over the two quadratic rings. The cost monoid
    was the wrong thing to fear -- m becomes a minimum over PRODUCTS and
    the two arguments that touch it need only a monotone monoid, which the
    logarithm supplies. What the port does need is a second column, a
    LADDER per colour, because a ring's items do not share one tick; the
    column is a formula in the colour except above residue characteristic
    2. explore_element_schedule_nf.py F1, F2.)
 5. The fresh-discount dial m of explore_price_schedule.py is NOT carried:
    covering here is the ring's own divisibility rule, one discount per
    degree, since a rider seats items outside any opening and the discount
    bookkeeping is exactly what that breaks.
 6. The toy supplies are ABSTRACT. A coloured supply is a legal state of the
    abstract dynamics and is not certified to be any curve's place count.

FINDINGS (tiers below; run record at the bottom).

F1 THE ELEMENT WORLD IS A SCHEDULE STATEMENT TOO, AND THE RING ENTERS AS A
   SUPPLY MATRIX OVER A FINITE ABELIAN GROUP (rule in range; six rings, the
   whole BRANCH TREE out to four moves -- five levels, 82 states -- plus
   nine moves of the canonical trajectory each, menus compared vehicle for
   vehicle under the item-to-place bijection). The tree is the audit's doing
   and PR2 as frozen asked only for the trajectory: S3 counts orbits over the
   abstract tree, so
   a control that visits one path certifies the walker exactly where those
   counts do not live, and the tick is READ OFF the ring's own lambda at each
   state so the door rule is under test rather than handed the answer. With m
   and the minimal representatives RECOMPUTED from the
   matrix -- a shortest path over the class group, weighted by the least
   degree at which each class has an item -- the abstract walker's element
   menu is the ring engine's at every state of the ring's own greedy walk:
   31 vehicles over 9 menus at F_2[x], 19 at h2, 28 at h3, 18 at h4, 26 at
   h5, 20 at g2, none differing. The colourings are 9, 16, 22, 27, 33 and 65
   wide. So what the ideal world reads as a supply VECTOR the element world
   reads as a supply MATRIX n(d, c) together with the group's addition
   table, and NOTHING else about the ring is read. The gate falls out as a
   property OF THAT MATRIX rather than as an independent confirmation, which
   is worth saying because it looks like one: the least degree at which two
   items share a colour is 1, 2, 5, 5, 6 and 6, agreeing with
   explore_coarse_type.py -- but both read the same place classes, so what
   this shows is that the gate needs no curve to STATE, not that it has been
   checked twice.

F2 THE COST IS A PRICE AND THE BUNDLE IS NOT, so the question has two
   answers (D1, measured). Every tie member at every visited state is priced
   TWICE and by different arithmetic -- the RING sums its vehicle divisor's
   degrees, the table looks up d*n + m(-n*c) from the core's colour and its
   door -- and 142 of 142 agree over the six rings. The two-way form is the
   point and the rig's first version did not have it: it compared the table
   against the same table, which passes by construction and says nothing
   about whether a price can express the cost. The other half is a SHAPE and
   not a number -- 0, 1, 1, 2, 5 and 8 of the first nine moves are bundles,
   touching 9, 10, 10, 11, 14 and 19 items where an ideal move touches nine.
   A family whose move raises ONE item's exponent has no member that raises
   several, at any price at all, so the rider's effect is outside the family
   by construction rather than by a dial being missing.

F3 THE RIDER'S DEGREE BOUND IS THE GENUS, READ OFF THE MATRIX (rule in
   range, asserted at six rings). The widest surcharge, max over classes of
   m, is 0, 1, 1, 1, 1 and 2 against genera 0, 1, 1, 1, 1 and 2. Over a
   curve that bound is Riemann-Roch's; here it is the greatest shortest-path
   weight from the identity in the class group's Cayley graph, computed from
   place counts with no geometry in the room.

F4 THE BARE DOOR IS NEVER BEATEN, WITH NO GENUS AND NO RING (proved, D2;
   PR3 discharged, the offsets offered and none winning at every menu of
   every ring AND of every abstract supply enumerated -- the second half was
   frozen and unchecked until the audit added it). The
   proof needs only that m is a minimum: minrep(-(n+j)c) together with j
   copies of the core is effective of class -n*c, so
   m(-n*c) <= j*d + m(-(n+j)c), which is cost(n) <= cost(n+j). So
   explore_coarse_type.py's lemma R is a schedule fact whose six-ring
   verification is one instance, and the hypothesis it has to name there --
   that every class HAS a minimal effective affine representative -- is
   automatic here.

F5 THE ORBIT COUNT SURVIVES THE CLASS LAYER, AND THE IDEAL WORLD'S FORMULA
   DOES NOT (rule in range: 8 supplies at a move budget of 5 over a DEGREE-4
   window, which is what enumerating with identities in costs; 0 shapes off
   the refined multinomial and 76 off the blind one). Shapes and
   configurations per supply: 14/30, 13/16, 9/9, 8/8, 21/21, 32/32 over the
   six rings' truncated matrices
   and 7/13, 7/25 over two designed ones; the degree-blind formula is off at
   0, 9, 8, 7, 20, 28, 2 and 2 of those. Its one zero is F_2[x], where the
   group is trivial and the two formulas are the same formula. So the
   element world's image is the ideal world's sum of multinomials with the
   colouring refined from the degree to (degree, class), and the class layer
   is visible to the count -- which is the orbit-count half of the question,
   answered.

F6 AT A FAILED GATE THE FORMULA SURVIVES ONE READING, AND THE WIDTH DECIDES
   THE OTHER -- PR5 lost as frozen and won one width up. Under SUMMON-ALL
   the formula holds everywhere, 0 off at every supply and budget. Under
   CANONICAL-CHOICE it holds at the width-2 failed gate, where the two
   readings reach the SAME configurations (10 against 10 at budget 3, 22
   against 22 at budget 4), and it BREAKS at width 3: 2 shapes off at budget
   3 and 4 at budget 4, the canonical set a proper subset both times, 16 of
   20 and 37 of 50. The witness is the shape seating two of the rider
   colour's three items at exponent 1 beside a doubled item of the other
   colour -- orbit 3, reached 2, the missing member being the pair that
   omits the canonical item. Width 2 cannot be short for the reason the
   witness gives: seating both items leaves no pair to omit. So D3's
   uniqueness is SUFFICIENT for the orbit count and NOT NECESSARY. What
   replaces it is not named here, and the obvious candidate is refuted by
   this section's own width-2 row: "the rider's mass can reach every item of
   its colour" fails there -- canonical mass sits on one item of two -- while
   the count survives. Whatever the condition is, it is about which shapes
   are REACHABLE and not about where the mass can land.
   AND THIS SECTION'S FIRST DESIGN RETURNED A ZERO FROM A MECHANISM THAT
   NEVER FIRED, which is why the summons column exists. That supply carried
   a class-0 item at its least degree; a free-riding item at the bottom runs
   away and is never asked to summon anything, and the enumeration contained
   0 ambiguous summons. The rows read as evidence about the gate and were
   evidence about the walk. With the class-0 item removed the mechanism
   fires 72 times and the section says something.

F7 THE BUNDLE COVERS A DEGREE FOR FREE ONCE, AND NEVER CLOCKS (observation;
   six rings, nine moves each, so 54 moves in all -- thin, and reported as
   thin). PR6 holds AND ITS MECHANISM FIRED, which is the part worth saying:
   11 riders landed on an item that was ALREADY SEATED -- the whole
   precondition for a rider-clock -- and 0 of them pushed it above the tick.
   Without that second count the zero would have been the same shape as S4's
   first design, a number about which items riders reach rather than about
   what a rider does to the tick. PR7 fires
   once, at g2 and nowhere else: at step 3 a rider seats a degree-2 item
   before any opening reaches degree 2. What it does NOT do is explain the
   gaps in the ladders -- h4 and h5 skip degrees with no free cover at all
   (seated 1,2,4,5,6,7 and 1,4,5,6,7 against F_2[x]'s 1,2,3,4,5,6), so the
   skipping is the price's doing and the free cover is a separate, rarer
   thing that has not yet been shown to cost anything.

WHAT THIS RIG CANNOT DO, so it is not claimed. An abstract walker says what
happens when the gate fails; it never says whether a Dedekind ring realizes
the failure, and every ring walked here has a gate that holds. The number
rings are untouched -- their engine enumerates by norm and their degrees are
logarithms, so F1's matrix is not known to be the right object there. And
the whole rig is the IDEAL-to-element step at ONE opening: how many openings
a trajectory has, and how many survive, is where explore_ladder_stop.py
works and is not decided here.

RUN RECORD. One process, CPython, no BLAS. Wall 0.3s, peak working set
16.5 MB against the 512 MB ceiling. 1921 checks here, over six ring engines
imported rather than re-implemented. The enumeration's cost is set by the
identified state count at S3, which is why the degree range there is 4 and
the budget 5 while S1 walks the rings at degree 9.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import factorial

import explore_coarse_type as CT
import explore_price_schedule as PS
from explore_greedy_image_ec import v2

CHECKS = 0
PRICED = [0]         # tie members priced against the ring's own arithmetic
BFSTATES = [0]       # ring states whose menus the abstract walker reproduced
RIDDEN = [0]         # riders landing on an item that is already seated

DMAX = 9             # greatest item degree the universes carry
WALK_N = 9           # moves of the ring's own greedy walk, S1 and S2
BFS_D = 5            # LEVELS of the ring's own branch tree the control
                     # sweeps: level 0 is the void, so it reaches states
                     # at most BFS_D - 1 moves out
BUDGET = 5           # moves enumerated with identities in, S3
STATE_CAP = 40000    # identified states carried at one level, asserted against


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------ the supply
class Supply(object):
    """A coloured supply: a finite abelian group by its addition table, and a
    count of items at each (degree, class). m and the minimal representatives
    are DERIVED here from the matrix -- nothing about them is handed in."""

    def __init__(self, tag, h, addc, cnt, dmax=DMAX, born=(1,)):
        self.tag = tag
        self.h = h
        self.addc = addc
        self.negc = [next(j for j in range(h) if addc[i][j] == 0)
                     for i in range(h)]
        self.cnt = dict((k, v) for k, v in cnt.items() if v)
        self.dmax = dmax
        self.born = frozenset(born)
        self.colours = sorted(self.cnt)
        self.items = [(d, c, i) for (d, c) in self.colours
                      for i in range(self.cnt[(d, c)])]
        self.m, self.reps = self._minreps()

    def add(self, a, b):
        return self.addc[a][b]

    def neg(self, c):
        return self.negc[c]

    def mul(self, n, c):
        """n copies of the class c, by repeated addition."""
        out = 0
        for _ in range(n % self.h if self.h > 1 else 0):
            out = self.add(out, c)
        return out

    def _minreps(self):
        """m(x) by shortest path over the class group, then every minimal
        COLOUR multiset attaining it, then every ITEM multiset refining one.
        A minimal representative may repeat an item -- a doubled item is a
        legal effective divisor -- so the enumeration is over multisets with
        repetition and not over subsets."""
        best = dict((c, None) for c in range(self.h))
        best[0] = 0
        least = {}
        for (d, c) in self.colours:
            if c not in least or d < least[c]:
                least[c] = d
        seen = set()
        while True:
            live = [c for c in range(self.h)
                    if best[c] is not None and c not in seen]
            if not live:
                break
            u = min(live, key=lambda c: best[c])
            seen.add(u)
            for c, d in least.items():
                v = self.add(u, c)
                if best[v] is None or best[u] + d < best[v]:
                    best[v] = best[u] + d
        reps = {}
        for x in range(self.h):
            if best[x] is None:
                continue
            out = []
            self._enum(0, {}, 0, 0, best[x], x, out)
            ok(out or x == 0, "%s: class %d has degree %s and no witness"
               % (self.tag, x, best[x]))
            reps[x] = out if x else [{}]
        return best, reps

    def _enum(self, i, cur, dg, cl, cap, target, out):
        """Colour multisets of total degree exactly cap and class target,
        taken in non-decreasing colour order so each multiset is built once,
        then expanded to item multisets."""
        if dg == cap:
            if cl == target:
                out.extend(self._expand(sorted(cur.items()), 0, {}))
            return
        for j in range(i, len(self.colours)):
            d, c = self.colours[j]
            if dg + d > cap:
                continue
            cur[(d, c)] = cur.get((d, c), 0) + 1
            self._enum(j, cur, dg + d, self.add(cl, c), cap, target, out)
            cur[(d, c)] -= 1
            if not cur[(d, c)]:
                del cur[(d, c)]

    def _expand(self, rows, i, cur):
        """Every way of splitting each colour's multiplicity over its items."""
        if i == len(rows):
            return [dict(cur)]
        (d, c), k = rows[i]
        n = self.cnt[(d, c)]
        out = []

        def parts(j, left, acc):
            if j == n - 1:
                acc.append(left)
                nxt = dict(cur)
                for s, e in enumerate(acc):
                    if e:
                        nxt[(d, c, s)] = e
                out.extend(self._expand(rows, i + 1, nxt))
                acc.pop()
                return
            for e in range(left + 1):
                acc.append(e)
                parts(j + 1, left - e, acc)
                acc.pop()

        parts(0, k, [])
        return out

    def unique(self):
        return all(len(v) == 1 for v in self.reps.values())

    def gate(self):
        """The least degree at which two distinct items share a colour, or
        None. Where that is above every minimal representative's degree the
        gate HOLDS and the minreps are unique."""
        share = [d for (d, c), n in self.cnt.items() if n > 1]
        return min(share) if share else None


def cost(sup, d, c, n):
    """The vehicle's whole price: the core's degree times its exponent, plus
    the rider's degree. A function of the colour and the door alone."""
    return d * n + sup.m[sup.neg(sup.mul(n, c))]


def vehicle(sup, item, n, rep):
    """The core at exponent n merged with one minimal representative."""
    veh = {item: n}
    for q, e in rep.items():
        veh[q] = veh.get(q, 0) + e
    return veh


# -------------------------------------------------------------- the walker
class CWalk(object):
    """A state of the coloured dynamics with identities in: st maps an item to
    its exponent, T is the tick. Covering is the ring's divisibility rule --
    a degree is covered once some seated item's degree is divisible by it."""

    def __init__(self, sup, summon="all", b=2):
        self.sup = sup
        self.summon = summon
        self.b = b
        self.st = {}
        self.T = 1
        self.step = 0
        self.free_cover = []     # (step, degree) first seated by a rider
        self.rider_clock = 0     # riders that pushed an item above the tick
        self.ridden = 0          # riders landing on an already-seated item
        self.bundle = 0          # moves touching more than one item

    def copy(self):
        s = CWalk(self.sup, self.summon, self.b)
        s.st = dict(self.st)
        s.T = self.T
        s.step = self.step
        s.free_cover = list(self.free_cover)
        s.rider_clock = self.rider_clock
        s.ridden = self.ridden
        s.bundle = self.bundle
        return s

    def key(self):
        return (tuple(sorted(self.st.items())), self.T)

    def covered(self, d):
        if d in self.sup.born:
            return True
        for (dd, _, _), e in self.st.items():
            if e and dd % d == 0:
                return True
        return False

    def door(self, d, e):
        if e == 0 and not self.covered(d):
            return 1
        return max(1, self.T + 1 - e)

    def reps_of(self, x):
        r = self.sup.reps[x]
        return r if self.summon == "all" else r[:1]

    def menu(self, offsets=(0, 1, 2)):
        """(cost, [(vehicle, core, door)]). Every core item is priced at its
        bare door and at the offsets above it; D2 says the bare door wins and
        the caller asserts it rather than the menu assuming it. The core is
        RETURNED rather than recovered from the vehicle, since a rider can
        land on the core's own item and the two exponents then merge."""
        best, ties, seen = None, [], set()

        def offer(veh, core, n, c):
            nonlocal best, ties, seen
            k = tuple(sorted(veh.items()))
            if best is not None and c > best:
                return
            if best is None or c < best:
                best, ties, seen = c, [(veh, core, n)], {k}
            elif k not in seen:
                seen.add(k)
                ties.append((veh, core, n))

        for d in range(1, self.sup.dmax + 1):
            if best is not None and d > best:
                break
            for (dd, cc) in self.sup.colours:
                if dd != d:
                    continue
                fresh = [(d, cc, i) for i in range(self.sup.cnt[(d, cc)])
                         if not self.st.get((d, cc, i))]
                cores = [(fresh, 0)] if fresh else []
                for i in range(self.sup.cnt[(d, cc)]):
                    e = self.st.get((d, cc, i), 0)
                    if e:
                        cores.append(([(d, cc, i)], e))
                for group, e in cores:
                    r0 = self.door(d, e)
                    for j in offsets:
                        n = r0 + j
                        c = cost(self.sup, d, cc, n)
                        if best is not None and c > best:
                            continue
                        want = self.sup.neg(self.sup.mul(n, cc))
                        for x in self.reps_of(want):
                            for it in group:
                                offer(vehicle(self.sup, it, n, x), it, n, c)
        ok(best is not None, "%s: an empty menu" % self.sup.tag)
        ties.sort(key=lambda t: (sorted(t[0].items()), t[1], t[2]))
        return best, ties

    def apply(self, veh, core):
        """Seat a vehicle. The core is named so that the rider's own effects
        -- a free cover, a clock bought without a clock move -- are read off
        the items the core is not."""
        Tb = self.T
        if len(veh) > 1:
            self.bundle += 1
        pre = set(d for d in range(1, self.sup.dmax + 1) if self.covered(d))
        for q, e in veh.items():
            was = self.st.get(q, 0)
            if not was and q != core and q[0] not in pre:
                self.free_cover.append((self.step, q[0]))
            if was and q != core:
                # a rider landing on an ALREADY-SEATED item is the whole
                # precondition for a rider-clock; without this count the
                # rider-clock zero cannot be told from a mechanism that
                # never fired
                RIDDEN[0] += 1
                self.ridden += 1
            self.st[q] = was + e
        top = max(self.st[q] for q in veh)
        by_core = self.st[core]
        while self.T < top:
            self.T = self.b * self.T
        if self.T > Tb and by_core <= Tb:
            self.rider_clock += 1
        self.step += 1
        return Tb, self.T

    def shape(self):
        """The multiset of positive exponents per COLOUR -- what an
        identity-free coloured walker would carry."""
        out = {}
        for (d, c, _), e in self.st.items():
            if e:
                out.setdefault((d, c), []).append(e)
        return tuple(sorted((k, tuple(sorted(v))) for k, v in out.items()))

    def config(self):
        return tuple(sorted((q, e) for q, e in self.st.items() if e))


def orbit_size(sup, shape, blind=False):
    """The refined multinomial of D3: at each colour, choose which items are
    seated and divide by the orders inside a repeated exponent. With
    blind=True the colours are merged by degree, which is the ideal world's
    formula and the thing that must fail."""
    rows = {}
    for (d, c), exps in shape:
        k = (d,) if blind else (d, c)
        rows.setdefault(k, []).extend(exps)
    tot = 1
    for k, exps in rows.items():
        if blind:
            n = sum(v for (d, c), v in sup.cnt.items() if d == k[0])
        else:
            n = sup.cnt[k]
        kk = len(exps)
        if kk > n:
            return 0
        num = factorial(n) // factorial(n - kk)
        mult = {}
        for e in exps:
            mult[e] = mult.get(e, 0) + 1
        for v in mult.values():
            num //= factorial(v)
        tot *= num
    return tot


def levels(sup, budget, summon="all", cap=STATE_CAP):
    """The identified reachable sets, one per move count, and a census of the
    moves that built them. `summons` counts the moves whose rider class has
    MORE THAN ONE minimal representative -- the mechanism S4 is about, so
    that a zero there can be told apart from a zero whose mechanism never
    fired."""
    start = CWalk(sup, summon)
    cur = {start.key(): start}
    out = [cur]
    census = {"moves": 0, "summons": 0, "riders": 0}
    for _ in range(budget):
        nxt = {}
        for s in cur.values():
            best, ties = s.menu()
            # PR3 was frozen over every ring AND every supply, and only the
            # rings were being checked: the abstract supplies run their menus
            # through here, so the bare door is asserted here too
            bare, _ = s.menu(offsets=(0,))
            ok(bare == best, "%s: an offset beat the bare door, %d against %d"
               % (sup.tag, best, bare))
            for veh, core, n in ties:
                x = sup.neg(sup.mul(n, core[1]))
                census["moves"] += 1
                if len(sup.reps[x]) > 1:
                    census["summons"] += 1
                if sup.m[x]:
                    census["riders"] += 1
                t = s.copy()
                t.apply(veh, core)
                nxt.setdefault(t.key(), t)
        ok(len(nxt) <= cap, "%s: %d states at one level, past the cap"
           % (sup.tag, len(nxt)))
        if not nxt:
            break
        cur = nxt
        out.append(cur)
    return out, census


# --------------------------------------------------- the rings as supplies
def ring_supply(L, dmax=DMAX):
    """The supply matrix, the group table and the item-to-place bijection,
    read off a ring. Nothing about m or the minimal representatives is read:
    those are recomputed from the matrix by Supply and asserted against the
    ring's own in S1."""
    R = L.R
    h = R.h if R.h else 1
    addc = R.addc if R.addc else [[0]]
    cnt, places = {}, {}
    for d in range(1, dmax + 1):
        by_c = {}
        for pl in R.by_deg.get(d, ()):
            by_c.setdefault(R.cls[pl], []).append(pl)
        for c, pls in by_c.items():
            pls.sort()
            cnt[(d, c)] = len(pls)
            for i, pl in enumerate(pls):
                places[(d, c, i)] = pl
    sup = Supply(L.name, h, addc, cnt, dmax=dmax)
    return sup, places


def to_place(veh, places):
    out = {}
    for q, e in veh.items():
        out[places[q]] = out.get(places[q], 0) + e
    return out


# ------------------------------------------------- S0 the degeneracy control
def s0_control(supplies):
    section("S0  THE DEGENERACY CONTROL -- the trivial group is the ideal "
            "world")
    print("the coloured walker against explore_price_schedule.py's, over the")
    print("same moves; PR1 says the menus and the states agree at every step")
    print()
    print("%-14s %6s %8s %8s %8s %8s" % ("supply", "steps", "menus", "states",
                                         "bundles", "cov-part"))
    sch = PS.Sched("corner")
    for tag, npl in supplies:
        cnt = dict(((d, 0), n) for d, n in enumerate(npl) if n)
        sup = Supply(tag, 1, [[0]], cnt)
        ok(sup.m[0] == 0 and sup.reps[0] == [{}],
           "%s: the trivial group has a nonempty minimal representative" % tag)
        a = CWalk(sup)
        # the ideal walker indexes its supply to its own degree cap, so the
        # dict is filled out to that cap rather than to this rig's
        b = PS.Walk(dict((d, npl[d] if d < len(npl) else 0)
                         for d in range(PS.DEG_CAP + 1)), sch, tag)
        menus = states = covpart = 0
        for _ in range(WALK_N):
            ca, ties = a.menu()
            cb, tb = b.menu()
            ok(ca == cb, "%s: cost %d against %d" % (tag, ca, cb))
            ma = {}
            for veh, core, n in ties:
                ok(len(veh) == 1, "%s: a bundle at the trivial group" % tag)
                kind = "move" if a.st.get(core, 0) else "open"
                key = (core[0], n, kind)
                ma[key] = ma.get(key, 0) + 1
            ok(ma == tb, "%s: menus part -- %s against %s" % (tag, ma, tb))
            menus += 1
            veh, core, _n = ties[0]
            a.apply(veh, core)
            key = min(tb)
            b.apply(key)
            pa = {}
            for (d, _, _), e in a.st.items():
                if e:
                    pa.setdefault(d, []).append(e)
            pb = dict((d, sorted(v)) for d, v in b.seat.items() if v)
            ok(dict((d, sorted(v)) for d, v in pa.items()) == pb,
               "%s: states part at step %d -- %s against %s"
               % (tag, a.step, pa, pb))
            ok(a.T == b.T, "%s: ticks part, %d against %d" % (tag, a.T, b.T))
            mine = set(d for d in range(1, a.sup.dmax + 1)
                       if npl[d] and a.covered(d))
            if mine != b.cov_set():
                covpart += 1
            states += 1
        print("%-14s %6d %8d %8d %8d %8d" % (tag, WALK_N, menus, states,
                                             a.bundle, covpart))
        ok(a.bundle == 0, "%s: a bundle at the trivial group" % tag)
    print()
    print("PR1 holds: at one colour the walker IS the ideal-world walker.")
    print("cov-part counts states where the divisibility covering rule and")
    print("the discount-count one differ -- a zero there says the control")
    print("did not separate them, not that they are the same rule.")


# ---------------------------------------------------- S1 the transfer control
def s1_transfer(ladders):
    section("S1  THE TRANSFER CONTROL -- the supply matrix is all the ring "
            "gives")
    print("m and the minimal representatives are recomputed from the matrix")
    print("alone, then the abstract menu is compared to the ring engine's")
    print("element menu vehicle for vehicle over the ring's own BRANCH TREE")
    print("and along its canonical trajectory (PR2, widened at audit)")
    print()
    print("%-8s %3s %5s %7s %6s %7s %7s %7s %7s" %
          ("ring", "h", "gate", "colours", "uniq", "m-rows", "menus", "vehs",
           "tree"))
    out = []
    for L in ladders:
        sup, places = ring_supply(L)
        R = L.R
        mrows = 0
        for c in range(sup.h):
            ok(sup.m.get(c) is not None,
               "%s: class %d unreachable from the matrix" % (L.name, c))
            ok(sup.m[c] == L.m(c),
               "%s: derived m(%d) = %d against the ring's %d"
               % (L.name, c, sup.m[c], L.m(c)))
            rep = dict((R.deg[pl], 0) for pl in L.minrep[c])
            for pl, e in L.minrep[c].items():
                rep[R.deg[pl]] += e
            got = {}
            for x in sup.reps[c]:
                for (d, _, _), e in x.items():
                    got[d] = got.get(d, 0) + e
                break
            ok(got == dict((k, v) for k, v in rep.items() if v)
               or (not rep and not got),
               "%s: class %d rides %s where the ring rides %s"
               % (L.name, c, got, rep))
            mrows += 1
        uniq = sup.unique()
        ok(uniq, "%s: the ring's minimal representatives are not unique here"
           % L.name)
        # THE CONTROL IS OVER THE RING'S BRANCH TREE AND NOT ONE PATH: S3
        # enumerates the abstract tree, so a control that only ever visits
        # the canonical trajectory certifies the walker exactly where the
        # orbit counts do not live. Every ring state at most BFS_D - 1 moves
        # out is compared -- level 0 is the void -- with the tick READ OFF the
        # ring's own lambda so the door rule is under test too rather than
        # being handed the answer.
        item_of = dict((pl, q) for q, pl in places.items())
        seen, frontier, states = set(), [{}], 0
        for _ in range(BFS_D):
            nxt = []
            for st0 in frontier:
                key = tuple(sorted(st0.items()))
                if key in seen:
                    continue
                seen.add(key)
                states += 1
                lam0 = R.lam_state(st0)
                c0, t0 = L.mod.MENUS["element"](R, st0, lam0)
                probe = CWalk(sup)
                probe.st = dict((item_of[pl], e)
                                for pl, e in st0.items() if e)
                probe.T = 1 << v2(lam0)
                ca0, ta0 = probe.menu()
                ok(ca0 == c0, "%s: BFS cost %d against the ring's %d at %s"
                   % (L.name, ca0, c0, key))
                ok(sorted(tuple(sorted(to_place(v, places).items()))
                          for v, _c, _n in ta0)
                   == sorted(tuple(sorted(v.items())) for v in t0),
                   "%s: BFS menus part at %s" % (L.name, key))
                for veh in t0:
                    st1 = dict(st0)
                    for pl, e in veh.items():
                        st1[pl] = st1.get(pl, 0) + e
                    nxt.append(st1)
            ok(len(nxt) <= STATE_CAP, "%s: %d ring states at one BFS level"
               % (L.name, len(nxt)))
            frontier = nxt
        BFSTATES[0] += states
        st, w, menus, vehs = {}, CWalk(sup), 0, 0
        for _ in range(WALK_N):
            lam = R.lam_state(st)
            cb, tb = L.mod.MENUS["element"](R, st, lam)
            ca, ta = w.menu()
            ok(ca == cb, "%s: cost %d against the ring's %d"
               % (L.name, ca, cb))
            mine = sorted(tuple(sorted(to_place(v, places).items()))
                          for v, _c, _n in ta)
            theirs = sorted(tuple(sorted(v.items())) for v in tb)
            ok(mine == theirs,
               "%s: menus part at step %d\n  mine   %s\n  theirs %s"
               % (L.name, w.step, mine, theirs))
            menus += 1
            vehs += len(ta)
            # the cost table against the RING's own arithmetic, which is the
            # only non-circular way to check that the surcharge is a price:
            # the ring SUMS the vehicle divisor's degrees, the table LOOKS UP
            # m. Comparing the table to itself, which this rig did first,
            # passes by construction and says nothing.
            for v, c0, n0 in ta:
                PRICED[0] += 1
                ok(cost(sup, c0[0], c0[1], n0)
                   == R.veh_deg(to_place(v, places)),
                   "%s: the table prices %s at %d, the ring at %d"
                   % (L.name, (c0, n0), cost(sup, c0[0], c0[1], n0),
                      R.veh_deg(to_place(v, places))))
            bare, _ = w.menu(offsets=(0,))
            ok(bare == ca, "%s: an offset beat the bare door, %d against %d"
               % (L.name, ca, bare))
            # both walks are driven by the RING's canonical winner, so that a
            # tie-break the colouring cannot see never parts them
            want = tuple(sorted(tb[0].items()))
            pick = [(v, c, n) for v, c, n in ta
                    if tuple(sorted(to_place(v, places).items())) == want]
            ok(len(pick) == 1, "%s: the ring's winner has %d preimages"
               % (L.name, len(pick)))
            veh, core, _n = pick[0]
            w.apply(veh, core)
            for pl, e in tb[0].items():
                st[pl] = st.get(pl, 0) + e
        print("%-8s %3d %5s %7d %6s %7d %7d %7d %7d" %
              (L.name, sup.h, sup.gate(), len(sup.colours), uniq, mrows,
               menus, vehs, states))
        out.append((L, sup, places, w))
    print()
    print()
    print("tree = ring states of the branch tree at most %d moves out whose"
          % (BFS_D - 1))
    print("menus the abstract walker reproduced, %d in all -- the control"
          % BFSTATES[0])
    print("S3's orbit counts need, a single trajectory not being one.")
    print("PR2 holds: the abstract walker reads nothing the ring engine does")
    print("not, and nothing the matrix and the group table cannot supply.")
    return out


# ------------------------------------------- S2 the surcharge and the bundle
def s2_split(walked):
    section("S2  THE COST IS A PRICE AND THE BUNDLE IS NOT")
    print("D1's two halves, measured: the surcharge m(-n*c) reads the core's")
    print("colour and its door and nothing else, while the move touches items")
    print("the core is not")
    print()
    print("%-8s %7s %7s %8s %8s" %
          ("ring", "m-max", "riders", "bundles", "touched"))
    for L, sup, places, w in walked:
        mmax = max(v for v in sup.m.values() if v is not None)
        # the rider's degree bound is Riemann-Roch's over a curve; here it is
        # a shortest path over the class group, so the agreement is a
        # statement and not a restatement
        ok(mmax == L.g, "%s: the widest surcharge is %d against genus %d"
           % (L.name, mmax, L.g))
        dep, riders, touched = 0, 0, 0
        v2 = CWalk(sup)
        for _ in range(WALK_N):
            c, ties = v2.menu()
            for veh, core, n in ties:
                # every tie member repriced from the colour table alone, with
                # the state entering only through the door already taken
                if cost(sup, core[0], core[1], n) != c:
                    dep += 1
            veh, core, _n = ties[0]
            if len(veh) > 1:
                riders += 1
            touched += len(veh)
            v2.apply(veh, core)
        ok(dep == 0, "%s: %d menu costs the colour table does not give"
           % (L.name, dep))
        print("%-8s %7d %7d %8d %8d" %
              (L.name, mmax, riders, v2.bundle, touched))
    print()
    print("The surcharge is a price, and the check is the RING's: %d tie"
          % PRICED[0])
    print("members priced by summing a divisor's degrees against the same")
    print("members priced by looking up the colour table, 0 differing (S1).")
    print("The bundle is not: a move that raises several items has no")
    print("expression in a family whose moves raise one, at any price.")


# ------------------------------------------------------- S3 the orbit count
def s3_orbits(sups, budget=BUDGET):
    section("S3  THE ORBIT COUNT -- configurations against the refined "
            "multinomial")
    print("the six ring rows are their matrices TRUNCATED to degree 4, which")
    print("is what enumerating with identities in costs -- not the full")
    print("supplies S1 walks. Every configuration enumerated; PR4 says each")
    print("reachable shape carries its whole refined orbit, and that the")
    print("degree-blind formula -- the ideal world's -- is wrong somewhere")
    print()
    print("%-10s %7s %7s %8s %7s %7s" %
          ("supply", "shapes", "configs", "formula", "off", "blind-off"))
    tot_off = tot_blind = 0
    for sup in sups:
        lv, _cen = levels(sup, budget)
        shapes, configs, off, blindoff = set(), 0, 0, 0
        for level in lv:
            byshape = {}
            for s in level.values():
                byshape.setdefault(s.shape(), set()).add(s.config())
            for sh, cfgs in byshape.items():
                shapes.add(sh)
                configs += len(cfgs)
                if len(cfgs) != orbit_size(sup, sh):
                    off += 1
                if len(cfgs) != orbit_size(sup, sh, blind=True):
                    blindoff += 1
        print("%-10s %7d %7d %8s %7d %7d" %
              (sup.tag, len(shapes), configs, "checked", off, blindoff))
        tot_off += off
        tot_blind += blindoff
    print()
    print("shapes off the refined formula: %d; off the blind one: %d"
          % (tot_off, tot_blind))
    # asserted after every row has printed, so a kill is READ and not only
    # raised
    ok(tot_off == 0, "%d shapes off the refined multinomial" % tot_off)


# -------------------------------------------------------- S4 the failed gate
def s4_gate(budget=4):
    section("S4  THE FAILED GATE -- two items of one colour, and the rider "
            "lands inside")
    print("D4: with minimal representatives no longer unique, SUMMON-ALL")
    print("should hold the formula (PR5) and CANONICAL-CHOICE should break it")
    print()
    # the two supplies differ in ONE item, and the item is the one that
    # doubles the rider's own colour. Neither carries a class-0 item at the
    # least degree, which is what the rig's first design got wrong: a
    # free-riding item at the bottom runs away and no ambiguous rider is ever
    # summoned, so the whole section returned a zero from a mechanism that
    # never fired. The summons column below is what says which happened.
    h = 3
    addc = [[(i + j) % h for j in range(h)] for i in range(h)]
    held = Supply("gate-holds", h, addc,
                  {(2, 1): 1, (2, 2): 1, (3, 1): 1, (5, 0): 2})
    broke = Supply("gate-fails", h, addc,
                   {(2, 1): 2, (2, 2): 1, (3, 1): 1, (5, 0): 2})
    wide = Supply("gate-fails-3", h, addc,
                  {(2, 1): 3, (2, 2): 1, (3, 1): 1, (5, 0): 2})
    print("%-14s %4s %6s %6s %10s %6s %5s %7s %7s" %
          ("supply", "bud", "gate", "uniq", "reading", "shapes", "off",
           "riders", "summon"))
    fired = 0
    for sup in (held, broke, wide):
        for bud in range(3, budget + 1):
            reach, witness = {}, {}
            for reading in ("all", "one"):
                s2 = Supply(sup.tag, sup.h, sup.addc, sup.cnt)
                lv, cen = levels(s2, bud, summon=reading)
                shapes, off, cfgset = set(), 0, set()
                for level in lv:
                    byshape = {}
                    for s in level.values():
                        byshape.setdefault(s.shape(), set()).add(s.config())
                    for sh, cfgs in byshape.items():
                        shapes.add(sh)
                        cfgset |= cfgs
                        if len(cfgs) != orbit_size(s2, sh):
                            off += 1
                            if off == 1:
                                witness[reading] = (sh, len(cfgs),
                                                    orbit_size(s2, sh))
                reach[reading] = cfgset
                if not sup.unique():
                    fired += cen["summons"]
                print("%-14s %4d %6s %6s %10s %6d %5d %7d %7d" %
                      (sup.tag, bud, sup.gate(), sup.unique(),
                       "summon-all" if reading == "all" else "canonical",
                       len(shapes), off, cen["riders"], cen["summons"]))
            # the sharper observable: a broken symmetry that leaves the
            # formula standing must still be VISIBLE somewhere, and the place
            # to look is the reachable set itself
            a, b = reach["all"], reach["one"]
            rel = ("equal" if a == b else
                   "canonical is a proper subset" if b < a else
                   "the two sets are incomparable")
            print("%-14s %4d   reachable configurations: %d against %d, %s"
                  % ("", bud, len(a), len(b), rel))
            if "one" in witness:
                sh, got, want = witness["one"]
                print("%-14s %4d   canonical's first short shape %s: %d of %d"
                      % ("", bud, sh, got, want))
    print()
    print("moves summoning a class with several representatives: %d" % fired)
    if not fired:
        print("-- so every zero above is VACUOUS: the mechanism never fired,")
        print("   and the rows are evidence about the walk and not the gate.")
    print()
    print("reps of each class, the two supplies:")
    for sup in (held, broke):
        print("  %-12s %s" % (sup.tag,
                              " ".join("%d:%d" % (c, len(v))
                                       for c, v in sorted(sup.reps.items()))))


# ------------------------------------- S5 what the bundle does to the ladder
def s5_free(walked):
    section("S5  THE RIDER'S FREE COVER, AND WHETHER A RIDER CLOCKS")
    print("D5's two observables over the six rings' own walks: PR6 predicts")
    print("no rider-clock, PR7 is unknown at the freeze")
    print()
    print("%-8s %10s %8s %11s %12s %9s" %
          ("ring", "free-cover", "ridden", "rider-clock", "at (step,deg)",
           "seated"))
    fc = rc = rd = 0
    for L, sup, places, w in walked:
        opened = sorted(set(d for (d, _, _), e in w.st.items() if e))
        print("%-8s %10d %8d %11d %12s %9s" %
              (L.name, len(w.free_cover), w.ridden, w.rider_clock,
               ";".join("%d,%d" % t for t in w.free_cover) or "-",
               ",".join(str(d) for d in opened)))
        fc += len(w.free_cover)
        rc += w.rider_clock
        rd += w.ridden
    print()
    print("free covers %d, rider-clocks %d over %d rings" % (fc, rc,
                                                             len(walked)))
    print("riders landing on an already-seated item: %d -- the whole" % rd)
    if not rd:
        print("precondition for a rider-clock, so the zero above is VACUOUS")
        print("and is evidence about which items riders reach, not about")
        print("what a rider does to the tick.")
    else:
        print("precondition for a rider-clock, so the zero above is a")
        print("statement about the tick and not about the mechanism.")


# ------------------------------------------------------------------- main
def main():
    CT.EC.DMAX = DMAX
    CT.G2.DMAX = DMAX
    supplies = [("one-each", [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
                ("two-each", [0, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
                ("sparse", [0, 1, 0, 2, 1, 1, 0, 2, 1, 1])]
    s0_control(supplies)
    ladders = CT.build_ladder()
    walked = s1_transfer(ladders)
    s2_split(walked)
    # S3 enumerates with identities in, so the universes are narrowed: the
    # same six supplies over a shorter degree range, plus two designed ones
    h3 = 3
    a3 = [[(i + j) % h3 for j in range(h3)] for i in range(h3)]
    small = [Supply(sup.tag, sup.h, sup.addc,
                    dict((k, v) for k, v in sup.cnt.items() if k[0] <= 4),
                    dmax=4)
             for _, sup, _, _ in walked]
    small.append(Supply("flat-3", h3, a3,
                        {(1, 1): 1, (1, 2): 1, (2, 0): 2, (3, 1): 1},
                        dmax=4))
    # wide-3 repeats only colours that no minimal representative uses, so its
    # gate HOLDS at width 3 -- a failed gate is S4's subject, not S3's
    small.append(Supply("wide-3", h3, a3,
                        {(1, 1): 1, (1, 2): 1, (2, 0): 3, (3, 1): 2},
                        dmax=4))
    s3_orbits(small)
    s4_gate()
    s5_free(walked)
    print("\n%d checks." % CHECKS)


if __name__ == "__main__":
    main()
