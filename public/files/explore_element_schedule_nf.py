"""explore_element_schedule_nf.py -- THE ELEMENT WORLD OVER A NUMBER RING:
does the schedule reading survive once degrees stop adding and norms start
multiplying, and is the element lock's recurrent price flat?

THE QUESTION, in two halves that share one machinery.

Over the ring of a curve the element world is a SCHEDULE statement: the ring
enters as a SUPPLY MATRIX n(degree, class) over a finite abelian group and
nothing else, a move seating a core X^n together with MINREP(-n*c) -- the
minimal effective divisor of the class that power must cancel, so the vehicle
is principal -- at cost d*n + m(-n*c), where m(x) is the least total degree of
an effective multiset of items whose classes sum to x. With m and MINREP
recomputed from that matrix alone, the abstract walker's element menu is the
ring engine's, vehicle for vehicle, over six function fields
(explore_class_schedule.py). Its own transplant flag carries NOTHING to the
number rings and says why: their element engine enumerates by NORM, has no
genus, and its degrees are logarithms rather than integers.

 (a) IS THE RECURRENT PRICE FLAT? A number ring's IDEAL walk locks with a
     recurrent vehicle costing N(P) per move forever, because deepening P
     from e to e + r takes v_p of the state's invariant to e + r - 1, so the
     next door at P is 1 (explore_lock_budget.py F1). An ELEMENT move seats a
     BUNDLE, so its recurrent vehicle is a product over several places, and
     the ideal argument is per-place. Does the element tail stay flat?

 (b) DOES THE SUPPLY MATRIX SURVIVE? m is a MINIMUM OVER SUMS and the
     shortest path deriving it is weighted by each class's least degree. Over
     a number ring the cost of a vehicle is a PRODUCT of norms, so m becomes
     a minimum over products and its weights stop being integers. Does the
     derivation survive that, and is the ring's element menu still a minimum
     over its own supply?

THE SETTING. The two quadratic rings the corpus walks: Z[sqrt(-5)], h = 2,
and Z[w] with w^2 = w - 6, the maximal order of Q(sqrt(-23)), h = 3. Both
element engines are IMPORTED rather than re-implemented, together with the
class layer that reads each place's ideal class and each class's minimal
representatives by ideal arithmetic (explore_number_field_lock.py,
explore_module_law.py, explore_class_species_nf.py). What this file adds is
an ABSTRACT walker that is handed the supply and the group table and nothing
else, and the tail census neither engine has run.

A COLOURED SUPPLY here is the class group C, given by its addition table,
together with the items' colours: an item is a place, its colour is
(NORM, class), and m(x) is the least NORM PRODUCT of an effective multiset of
items whose classes sum to x, with m(0) = 1. A move takes a core X of colour
(N, c) at door r and seats X^r + MINREP(-r*c), of cost N^r * m(-r*c).

THE WORDS THIS FILE USES THROUGHOUT, since it is read by whoever reads the
pages that cite it. The state's INVARIANT is lambda, the exponent of the unit
group of the quotient by the current state. A VEHICLE is what a move
multiplies the state by, and a move is admissible only if it raises the
invariant. A place's DOOR at its current depth is the least r by which
deepening it does so -- what a move at that place has to buy. A place's
LADDER is the set of depths at which its own lambda moves, and its GAP is
the spacing of that set; the TICK is the function field's version of the
same thing, one global clock rather than one ladder per place. The VOID is
the empty state. A trajectory LOCKS when it stops opening new places and
re-deepens one recurrent vehicle forever, and a BASIN is the set of seeds
whose trajectories lock on the same one. A BELT is a set of seeds: every
state of norm at most some bound, walked one trajectory each. A state's MENU
is the set of admissible vehicles at the least cost any of them has -- one
member where the greedy move is unique, several where it ties, and it is the
object every comparison below is between. A class's WIDTH is how many
minimal representatives it has.

THE HAND-ATTACK, on paper before any engine code.

 L1 THE COST MONOID PORTS, AND IT IS NOT WHERE THE PORT IS HARD. The
    function field's monoid is (Z>=0, +) and this one is (Z>=1, *); both are
    ordered monoids whose operation is monotone (a <= a' implies a*b <=
    a'*b) and whose generators sit strictly above the identity (degrees
    >= 1, norms >= 2), and the logarithm embeds the second in the first. So
    every argument that uses only "m is a minimum over a monotone monoid"
    ports verbatim, and exactly two do.
     (i) THE BARE DOOR IS NEVER BEATEN. MINREP(-(n+j)c) together with j
         copies of the core is an effective multiset of class -n*c, so
         m(-nc) <= N^j * m(-(n+j)c), which IS cost(n) <= cost(n+j). The
         only hypothesis is that m is a minimum.
     (ii) m IS A SHORTEST PATH over the Cayley graph of C whose edge for
         class c carries the least norm of an item of class c, taken in the
         (min, *) semiring -- which is (min, +) after logs. Replacing any
         item of a multiset by the least-norm item of its own class changes
         no class sum and never raises the product, so the path bound is
         attained and the minimum is over paths.
    Both are derivations, so the cost monoid is settled on paper. What stays
    empirical is whether the RING's element menu is that object.

 L2 WHERE THE PORT IS ACTUALLY NON-TRIVIAL, named at the freeze so that no
    section below is credited with finding it.
     (i) THE DOOR. Every item of a function field's walker shares ONE
         ladder, the global tick doubling. A number ring gives its
         unramified places gap 1 and its ramified ones gap e in the same
         walk, and the door reads the state's own invariant. A supply matrix
         alone therefore cannot give the door: the ring must supply a SECOND
         COLUMN, a per-item ladder. This is the amendment the port is
         expected to need, and it is not the monoid.
     (ii) THE IDENTITY. m(0) = 0 there and 1 here: a rider of the trivial
         class is free on both sides, so this is a change of notation.
     (iii) THE LANDING. The rider can land ON the core and merge exponents,
         at norm 2 in particular. Same on both sides.
     (iv) UNIQUENESS of the minimal representative is what decides whether
         the orbit count needs a width reading at all. Both rings are
         expected to have unique minimal representatives, as every ring the
         corpus walks does, so the question would again live only in the
         abstract world.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

 PR1 (positive control, run before anything is read) The imported engines
     reproduce their filed facts -- the K5 element overture 4, 4, 9, 6 then
     4 forever, the K23 element tails at 4 and 25 in two basins -- and the
     shortest-path m of L1(ii) equals a BRUTE minimum over the ring's own
     place-power products, at every class of both rings.
     KILL: the control fails, in which case nothing below is read.
 PR2 THE MENU IS A MINIMUM OVER THE SUPPLY -- the headline. With m and
     MINREP recomputed from the supply matrix alone, the abstract walker's
     element menu equals the ring engine's element menu VEHICLE FOR VEHICLE
     at every state of every element trajectory of both belts.
     KILL: one state where a vehicle sits in one menu and not the other,
     which is the queued kill-shape verbatim -- an element menu whose
     cheapest completion is not any minimum over the supply.
 PR3 NO OFFSET WINS. The rig offers a core at its door exponent plus j for
     j >= 1 at every menu and none is strictly cheaper (L1(i)). Ties at an
     offset are RECORDED rather than predicted: the proof bounds the offset
     from below and says nothing about equality.
     KILL: one offset strictly cheaper than its own bare door.
 PR4 THE RECURRENT PRICE IS FLAT. Every element lock's tail cost is
     constant. The mechanism predicted: the core's own door settles at its
     constant gap by the ideal argument, and the rider's price is a TABLE
     LOOKUP on the core's colour and its door, so both factors of
     N^r * m(-r*c) are fixed once the door is.
     KILL: an element lock whose tail cost grows.
 PR5 AND SO IS THE BUNDLE'S COMPOSITION. The recurrent vehicle's place count
     and total exponent are constant along the tail. What would break
     flatness is a bundle whose composition grows, which is the rider's
     doing and not the gap's, so the composition is the observable that
     would say which mechanism failed.
     KILL: a tail whose vehicle composition changes while its cost does not
     -- which would leave PR4 true for a reason other than the predicted
     one.
 PR6 THE RING SUPPLIES A LADDER COLUMN AND THE COLOUR DOES NOT DETERMINE
     IT. The model lam(N, gap, a) = (N - 1) * rad(N)^ceil((a-1)/gap), with
     gap the ramification index and rad the prime under the place,
     reproduces the ring's own lambda at every place of both universes with
     p - 1 > e, and parts from it at exactly the places with p - 1 <= e --
     the three places over 2 the two rings have, the ramified one at
     Z[sqrt(-5)] and the split pair at Z[w] -- where the principal units are
     still squaring rather than stepping and a leading stretch of larger
     gaps precedes the constant one. (The index convention was re-derived
     from the engines' own lambda tables at the freeze rather than carried:
     the first draft of this prediction named the wildly ramified place
     alone, which is the ramification reading of a criterion that is not
     about ramification.)
     KILL: the model parts at a place with p - 1 > e, which would mean norm
     and gap together are not enough anywhere.
 PR7 THE MINIMAL REPRESENTATIVE IS UNIQUE at every class of both rings, so
     the failed-gate width question does not arise over a number ring either.
     A REPRODUCTION and not a question: uniqueness is proved at both rings by
     an exhaustive enumeration clearing the Minkowski bound
     (explore_class_species_nf.py F3), and it is re-read here because the
     abstract MINREP is single-valued and would be silently wrong if it were
     not.
     KILL: a class with two minimal representatives.

TRANSPLANT FLAGS, fixed at the freeze. Every intuition below is imported
from a neighbouring value of the ring parameter and is marked rather than
trusted.
 1. From the function fields, EVERYTHING, and this file is that flag being
    discharged rather than carried: degrees ADD where norms MULTIPLY, the
    tick DOUBLES where a ring's landing is exact, there is a genus there and
    none here. No statement of the six-ring result is assumed; each is
    re-derived over the multiplicative monoid or re-measured.
 2. From the IDEAL world to the ELEMENT world. The flat-price mechanism of
    explore_lock_budget.py is an argument about ONE place's valuation and an
    element move deepens several. It is not carried; PR4 is its test.
 3. From h = 2 to h = 3. One rider class against two, and a ramified
    minimal representative against a conjugate pair of split ones. Every
    count is reported per ring.
 4. "The ring enters as a supply matrix and NOTHING else" is UNDER TEST and
    not a premise -- L2(i) already predicts a second column, and PR6 is
    where it is read.

THE DESIGN, in four sections after the control.

 S1 THE SUPPLY AND ITS TWO COLUMNS. Per ring: the class of every place, the
    supply matrix over a norm window, each class's least norm and every item
    attaining it (PR7), the shortest-path m against the brute minimum over
    place-power products (PR1), and the ladder column -- the model lambda
    against the engine's over a norm window of its own, at depths 1..14,
    read as a BICONDITIONAL against the p - 1 <= e criterion so that an
    agreement at a wild place counts against it too (PR6).
 S2 THE ABSTRACT MENU AGAINST THE RING'S. Every element seed of both belts,
    twelve moves each. At every state the abstract menu is built from the
    matrix -- every place at its door exponent plus offsets, priced
    N^r * m(-r*c) with MINREP realised from the matrix -- and compared as a
    SET of vehicles against the ring engine's own element menu (PR2, PR3).
    The DOOR is read off the ring's lambda here, exactly as the six-ring rig
    reads the tick off the ring, so what this section tests is the bundle
    and the cost monoid; the ladder column's own status is S1's question and
    not this one's.
 S3 THE RECURRENT PRICE. Every element seed walked past its lock, with the
    lock witnessed as the census witnesses it (the same vehicle repeated for
    LOCK_R consecutive moves) and forty tail moves recorded past it: the
    tail costs, the largest last/first ratio, the distinct settled costs,
    and the vehicle's composition along the tail (PR4, PR5).
 S4 THE SYNTHESIS: what the two worlds and the two characteristics read in
    one table, with the columns this file measured filled from its own runs
    and the function-field ones cited.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE COST MONOID SURVIVES, AND A NUMBER RING'S ELEMENT MENU IS STILL A
   MINIMUM OVER ITS OWN SUPPLY (rule in range; two rings, 675 states -- every
   element seed of both norm-40 belts walked 12 moves on its canonical line
   plus the whole branch tree out to 4 moves, menus compared vehicle for
   vehicle, 0 differing). With m and MINREP recomputed from the supply matrix
   alone -- a shortest path over the class group in the (min, *) semiring,
   weighted by each class's least NORM -- the abstract walker's element menu
   is the ring engine's at every state: 344 menu entries over 334 states at
   Z[sqrt(-5)] and 347 over 341 at Z[w], of which 103 and 307 are BUNDLES
   rather than single places. Two halves of that are NOT new and are cited:
   the bare-door FORM over a number ring -- a rider being the minimal-norm
   representative of the class its core must cancel -- is a rule in range at
   every vehicle the class-species searches met, and each class's minimal
   representative and its UNIQUENESS are PROVED there, by an enumeration to
   norm 60 that clears the Minkowski bound (explore_class_species_nf.py F3),
   which is what PR7 reproduces rather than establishes. What is new is that
   m and MINREP are DERIVED by that shortest path, from the matrix and not
   from any enumeration of the ring's ideals, and that the whole MENU is
   compared -- the minimum over items and its entire tie set -- where the
   filed rig checks the form of the vehicles it meets. So "the ring enters as a supply matrix over a
   finite abelian group" reaches past the function fields, and the monoid
   change costs NOTHING: degrees adding and norms multiplying are one
   statement, the second being the first after logs, and the two arguments
   that use m -- the shortest path and the bare-door bound -- need only that
   m is a minimum over a monotone monoid. What the abstract side is HANDED
   is the door, read off the ring's lambda exactly as the six-ring rig is
   handed the tick (explore_class_schedule.py); F2 is where that hand-over
   is priced, and it is the port's one real cost.

F2 AND THAT COST IS A SECOND COLUMN -- THE LADDER, WHICH THE COLOUR DOES NOT
   DETERMINE (the SCHEDULE-side reading is this file's; the ring-side facts
   under it are cited, not remeasured). Every item of a function field's
   walker shares ONE ladder, the doubling tick. A number ring gives each item
   its own, and both arithmetic facts behind that are already filed over all
   90 places of the two universes: the gap IS the ramification index, and
   exactly three places carry a HEAD -- a leading stretch of wider gaps --
   namely the three with p - 1 <= e, which are Z[sqrt(-5)]'s ramified place
   over 2 and Z[w]'s SPLIT pair over 2, because below e/(p-1) the principal
   units are still squaring rather than stepping (explore_tick_pump.py).
   Neither is rediscovered here, and the second is not a statement about
   ramification, two of the three being unramified.
   WHAT IS THIS FILE'S is the consequence for the SUPPLY. A colour is
   (norm, class), a colour does not determine a ladder, so the matrix cannot
   give the door and the ring must hand a further column over. The model
   lam(N, gap, a) = (N - 1)*rad(N)^ceil((a-1)/gap) is what a colour plus a
   gap CAN give, and it is read against the engines at the 35 places of norm
   <= 60 over depths 1..14 as a BICONDITIONAL against the filed criterion, so
   that an agreement at a p - 1 <= e place would count against it too: 32
   agree, 3 part from depth 3 on, 35 of 35 on the criterion. So the column is
   a formula in the colour except where p <= e + 1 -- these two rings' places
   over 2, though a ring in which 3 ramified would carry a head there too.
   (PR6 as first drafted named the wildly ramified place alone. It was
   corrected at the FREEZE against that filed criterion, before any run: the
   ramification reading of a criterion that is not about ramification would
   have made a hit look like a miss.)

F3 WHY THE ELEMENT LOCK'S RECURRENT PRICE IS FLAT -- THE OBSERVATION IS
   FILED AND THE MECHANISM IS WHAT WAS MISSING. That the tails are flat is
   NOT this file's: both element censuses already assert it seed by seed at
   their own belts, K5's over its last 25 moves with the vehicle pinned to
   {ram 2: 2} at norm 4 (explore_number_field_lock.py) and K23's over 41
   seeds and 40 moves with its two basins at norms 4 and 25
   (explore_module_law.py). That first assertion is also the COMPOSITION this
   rig re-derived -- at Z[sqrt(-5)] the recurrent vehicle is one place at
   exponent 2 and not a bundle at all, which is what "{ram 2: 2}" says.
   Re-measured here over both belts under one witness (53
   seeds, 40 tail moves past each lock, 0 non-flat, 0 shifting composition, 0
   alternating vehicles at a flat cost, largest last/first ratio 1.00), which
   is a regression check and is reported as one.
   WHAT IS NEW IS THE ROUTE, and it is exactly what explore_lock_budget.py's
   own transplant flag said its argument did not cover: that argument is
   about ONE place's valuation and an element move seats several. The
   answer is that it does not need to reach several. F1 pins the recurrent
   vehicle's FORM -- core^r * MINREP(-r*c) -- so the price factors, the first
   factor flat by the ideal world's valuation argument verbatim (deepening
   takes the state's valuation to the new depth minus one, leaving the next
   door at the constant gap) and the second a table lookup on a finite group,
   fixed once the door is. So the element world's flat price is the ideal
   mechanism COMPOSED with the rider being a PRICE, and needs no argument of
   its own. The frozen prediction -- a product of bounded gaps is bounded, so
   the price should be flat -- hit, but not by its own reasoning: what makes
   the second factor constant is that it is a lookup, not that its factors
   are bounded.

F4 THE BARE DOOR'S BOUND IS ATTAINED, AND ITS TIGHTNESS LOCUS IS THE RIDER
   SET -- ONE HALF A FILED THEOREM AND THE OTHER A MEASUREMENT (UNFROZEN;
   PR3 froze the ties as recorded rather than predicted; 8019 offsets offered
   over the 675 states, 0 winning, 177 tying). The inequality
   cost(n) <= cost(n+j) is proved over any monotone monoid and says nothing
   about equality -- but its equality case is ALREADY A THEOREM, and this
   file's first reading of the ties re-minted it as a fresh find: where
   minimal representatives are unique, equality forces the two vehicles to be
   the SAME DIVISOR (lemma S, explore_coarse_type.py F1, proved and certified
   over six function fields). Reproduced here in the other characteristic at
   177 of 177 ties, on rings that lemma had never been run against. And the
   rider-set locus is that theorem's own two-line consequence rather than a
   coincidence: one divisor means minrep(-rc) = P^j * minrep(-(r+j)c), so the
   core P appears in the support of a minimal representative, which IS the
   rider set. So the containment needs no ring and no run.
   What the run adds beyond the instance is the CONVERSE, which no lemma here
   gives: every place of both rider sets attains the bound somewhere (R2 at
   Z[sqrt(-5)]; P2.0 and P2.1 at Z[w]), so the tightness locus EQUALS the
   rider set at these two rings rather than merely sitting inside it -- and
   that direction is contingent, since it needs the walk to reach a door at
   which the core's own class is what the rider must cancel. The tie
   arithmetic prints as one signature at both rings: m falling from 2 to 1
   against a core of norm 2 at j = 1, the extra core power costing exactly
   what it saves on the rider.

Run: `python explore_element_schedule_nf.py`. RUN RECORD (9267 checks,
~0.1 s, peak working set 19 MB; the abstract menu stops scanning at the first
item whose norm exceeds the running best, which is what makes an exhaustive
comparison cheap).
S0 control: the K5 element overture 4, 4, 9, 6 then 4s; the K23 element
basins at tail norms 4 and 25; the shortest-path m equal to a brute minimum
over the ring's own place-power products at every class of both rings (1, 2
at h = 2; 1, 2, 2 at h = 3), the two KEY SETS compared against the group order
first so that a class the path never reached could not go missing from both
sides of the comparison. S1: the supply matrices over the norm-30 window,
every class's minimal representative of WIDTH 1 at both rings (so the failed
gate does not arise over a number ring either), the path MINREP equal to the
ring's at every class, and the ladder column parting at 3 places of 35, the
biconditional against p - 1 <= e holding at all 35.
S2: 334 and 341 states, 0 menu mismatches, 0 offsets winning, 177 tying, 0
ties that are two divisors, 0 with a core outside the rider set, and every
rider-set place among the attaining cores. S3: 26 and 27 locks, 0 non-flat -- a
REGRESSION check, the flatness being the two element censuses' own.
Slate PR1-PR7: all hit, PR6 hit as corrected at the freeze. Unfrozen find:
F4, and the audit rewrote it twice -- first because a biconditional had been
stated off a containment the tie census gives for free, then because the
containment itself is a filed THEOREM this file had re-minted as its own
observation, having read explore_class_schedule.py's citation of lemma S
without reading the lemma. What survives as this file's is the instance in
the other characteristic and the converse direction.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import heapq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_number_field_lock as K5      # the h = 2 ring (lineage)
import explore_module_law as K23            # the h = 3 ring (lineage)
import explore_greedy_image_nf as NF        # the belts and the lock witness
import explore_class_species_nf as CS       # the class layer (lineage)

CHECKS = 0

SUPPLY_CAP = 300     # norm window the abstract supply is built over
MENU_T = 12          # moves of each element trajectory the menus are read on
OFFSETS = 3          # core exponents above the bare door that are offered
BRANCH_D = 4         # moves of the branch tree the menus are also read on
LEAD = 20            # moves allowed before the tail is read
TAIL = 40            # tail moves recorded past the lock
DEPTH_CAP = 14       # depths the ladder model is read at
LADDER_CAP = 60      # norm window the ladder column is read over


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def record(cond, bucket, item):
    """A check that BANKS its failure instead of aborting, so a kill prints
    its own shape before the section asserts."""
    global CHECKS
    if cond:
        CHECKS += 1
    else:
        bucket.append(item)
    return cond


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def vkey(veh):
    """A vehicle as a comparable key: its place-exponent multiset."""
    return tuple(sorted((repr(pl), e) for pl, e in veh.items() if e))


def rad(n):
    """The prime under a prime-power norm."""
    p = 2
    while p * p <= n:
        if n % p == 0:
            return p
        p += 1
    return n


# ------------------------------------------------------- the abstract supply
class Supply(object):
    """What the ring hands over as a SUPPLY: for every item a COLOUR
    (norm, class) and a LADDER (its gap), plus the group's addition table.
    m and MINREP are recomputed here as a shortest path over the group and
    are never read off the ring. Not everything the abstract walker uses --
    the DOOR comes from the ring's own lambda, which is what S1 prices."""

    def __init__(self, R):
        self.h = R.h
        self.items = []                      # (place, norm, class, gap)
        for pl in R.M.UNIVERSE:
            if R.M.place_norm(pl) > SUPPLY_CAP:
                continue
            self.items.append((pl, R.M.place_norm(pl), R.cls_of_place(pl),
                               2 if pl[0] == 'ram' else 1))
        self.least = {}                      # class -> least norm
        self.least_items = {}                # class -> items attaining it
        for (pl, n, c, g) in self.items:
            if c not in self.least or n < self.least[c]:
                self.least[c], self.least_items[c] = n, [pl]
            elif n == self.least[c]:
                self.least_items[c].append(pl)
        self._paths()

    def _paths(self):
        """m and MINREP by Dijkstra in the (min, *) semiring: dist[x] is the
        least norm product of a multiset of classes summing to x."""
        self.m = {0: 1}
        self.path = {0: ()}
        pq = [(1, 0, ())]
        while pq:
            d, x, pth = heapq.heappop(pq)
            if d > self.m.get(x, d):
                continue
            for c in sorted(self.least):
                if c == 0:
                    continue
                y, nd = (x + c) % self.h, d * self.least[c]
                if y not in self.m or nd < self.m[y]:
                    self.m[y], self.path[y] = nd, pth + (c,)
                    heapq.heappush(pq, (nd, y, pth + (c,)))

    def minrep(self, x):
        """The rider as a place multiset, realised from the matrix by taking
        each path class's least-norm item."""
        veh = {}
        for c in self.path[x % self.h]:
            pl = self.least_items[c][0]
            veh[pl] = veh.get(pl, 0) + 1
        return veh

    def lam_model(self, pl, n, g, a):
        """The ladder column's own lambda: the residue field's order minus
        one, times the prime under the place raised to the principal-unit
        level the gap allows."""
        if a == 0:
            return 1
        lev = -(-(a - 1) // g)               # ceil((a-1)/g)
        return (n - 1) * rad(n) ** lev


# --------------------------------------------------------- the abstract menu
def abstract_menu(R, S, st, L, offsets=OFFSETS):
    """The element menu built from the supply alone: every item at its door
    exponent plus j, carrying MINREP of the class that power must cancel,
    priced as a norm product. Returns (best cost, vehicles at it, the offset
    record)."""
    best, veh_at, off_rec = None, {}, []
    for (pl, n, c, g) in S.items:
        if best is not None and n > best:
            break                            # cost >= norm at every offset
        e = st.get(pl, 0)
        r0 = R.M.door_r(pl, e, L)
        for j in range(offsets + 1):
            r = r0 + j
            rider = S.minrep((-r * c) % S.h)
            veh = dict(rider)
            veh[pl] = veh.get(pl, 0) + r
            cost = 1
            for q, ex in veh.items():
                cost *= R.M.place_norm(q) ** ex
            mm = S.m[(-r * c) % S.h]
            if j == 0:
                bare, m_bare, bare_key = cost, mm, vkey(veh)
            else:
                off_rec.append((j, bare, cost, (m_bare, mm, n, j), pl,
                                bare_key == vkey(veh)))
            if best is None or cost < best:
                best, veh_at = cost, {vkey(veh): veh}
            elif cost == best:
                veh_at.setdefault(vkey(veh), veh)
    assert best is not None and best <= SUPPLY_CAP, \
        "the abstract menu's cost left the supply window"
    return best, veh_at, off_rec


# ---------------------------------------------------------------- S0 control
def s0_control(rings):
    section("S0  THE POSITIVE CONTROL -- filed facts through the imported "
            "engines")
    log, st, L = K5.run_elem({}, 8)
    norms = [mv[2] for mv in log]
    ok(norms == [4, 4, 9, 6, 4, 4, 4, 4],
       "control: the K5 element overture is %s" % norms)
    print("  K5 element void:    norms %s -- the filed opening, where the"
          % norms[:6])
    print("                      early moves pay for a rider and the tail")
    print("                      does not")
    tails = set()
    for seed in ({}, {('inert', 5): 1}):
        log, st, L = K23.run_elem(seed, 20)
        tails.add(log[-1][2])
    ok(tails == {4, 25}, "control: the K23 element basins are %s" % tails)
    print("  K23 element basins: tail norms %s -- two basins, not one"
          % sorted(tails))

    # PR1's second half: the shortest path against a brute minimum over the
    # ring's own place-power products.
    print("\n  %-5s %-7s %-24s %s"
          % ("ring", "class", "m by shortest path", "m by brute product"))
    for R, S in rings:
        brute = {0: 1}
        for nrm, fac in R.M.gen_products(CS.GEN_CAP):
            c = R.cls_of(fac)
            if c not in brute or nrm < brute[c]:
                brute[c] = nrm
        # The key sets are compared FIRST: looping over one side's classes
        # would make a class the path never reached invisible.
        ok(set(S.m) == set(range(R.h)) == set(brute),
           "%s: classes by path %s, by brute %s, group order %d"
           % (R.name, sorted(S.m), sorted(brute), R.h))
        for c in sorted(S.m):
            ok(S.m[c] == brute[c],
               "%s: m(%d) = %s by path and %s by brute"
               % (R.name, c, S.m[c], brute[c]))
            print("  %-5s %-7d %-24d %d" % (R.name, c, S.m[c], brute[c]))
    print("\n  Control green: the engines reproduce the filed facts and the")
    print("  path minimum is the ring's own minimum at every class.")


# ------------------------------------------------- S1 the supply and columns
def s1_supply(rings):
    section("S1  THE SUPPLY AND ITS TWO COLUMNS -- what the ring hands over")
    print("  A colour is (norm, class); the supply matrix counts items at")
    print("  each. The LADDER column is the second thing the ring supplies,")
    print("  and the question is whether the colour already determines it.\n")
    for R, S in rings:
        print("  %s (h = %d), supply matrix over the norm window <= 30:"
              % (R.name, R.h))
        rows = {}
        for (pl, n, c, g) in S.items:
            if n <= 30:
                rows.setdefault(n, {}).setdefault(c, 0)
                rows[n][c] += 1
        print("    %-8s %s" % ("norm", "  ".join("c=%d" % c
                                                 for c in range(R.h))))
        for n in sorted(rows):
            print("    %-8d %s"
                  % (n, "  ".join("%3d" % rows[n].get(c, 0)
                                  for c in range(R.h))))
        # PR7: the width of every class's minimal representative.
        widths = []
        for c in sorted(S.m):
            reps = R.minreps[c]
            widths.append((c, S.m[c], len(reps)))
            ok(len(reps) == 1,
               "%s: class %d has %d minimal representatives"
               % (R.name, c, len(reps)))
            if c:
                ok(vkey(S.minrep(c)) == vkey(reps[0]),
                   "%s: the path MINREP(%d) is %s, the ring's is %s"
                   % (R.name, c, S.minrep(c), reps[0]))
        print("    minreps: %s -- (class, m, width)"
              % ", ".join("(%d, %d, %d)" % w for w in widths))
        print("    rider set: %s"
              % " ".join(NF.show_place(pl) for pl in sorted(R.rider,
                                                            key=R.M.place_key)))
    # PR6: the ladder column against the engine's lambda.
    print("\n  the LADDER COLUMN: the model (N-1)*rad(N)^ceil((a-1)/gap)")
    print("  against the engine's own lambda, every place at norm <= %d,"
          % LADDER_CAP)
    print("  depths 1..%d.\n" % DEPTH_CAP)
    print("  %-5s %-14s %-5s %-5s %-7s %s"
          % ("ring", "place", "p", "e", "p-1<=e", "model vs engine lambda"))
    heads, parted, agree = [], [], 0
    for R, S in rings:
        for (pl, n, c, g) in S.items:
            if n > LADDER_CAP:
                continue
            off = [a for a in range(1, DEPTH_CAP + 1)
                   if S.lam_model(pl, n, g, a) != R.M.lam_P(pl, a)]
            p = rad(n)
            # The filed criterion is read as a BICONDITIONAL, which is
            # stronger than PR6 asked: a place parts from the model exactly
            # when p - 1 <= e. A part at a TAME place is PR6's kill; an
            # AGREEMENT at a wild one would say the criterion over-predicts.
            record(bool(off) == (p - 1 <= g), parted,
                   (R.name, NF.show_place(pl), p, g, off[:4]))
            if off:
                heads.append((R.name, pl, p, g, off))
                print("  %-5s %-14s %-5d %-5d %-7s parts from depth %d on"
                      % (R.name, NF.show_place(pl), p, g, "yes", off[0]))
            else:
                agree += 1
    print("  %d further places of the two universes: the model IS the"
          % agree)
    print("  engine's lambda at every depth read.")
    print("  places where parting and p - 1 <= e disagree: %d." % len(parted))
    for row in parted[:5]:
        print("    %s %s p=%d e=%d depths %s" % row)
    ok(not parted, "PR6: the criterion misses at %d places, first %s"
       % (len(parted), parted[:1]))
    return heads


# --------------------------------------------- S2 the abstract menu vs ring
def s2_menus(rings):
    section("S2  THE ABSTRACT MENU AGAINST THE RING'S -- vehicle for vehicle")
    print("  The abstract side reads the supply matrix and the group table,")
    print("  and takes the DOOR from the ring's own lambda. It never sees an")
    print("  element of the ring, and whether the ladder column could have")
    print("  supplied that door instead is S1's question, not this one's.\n")
    print("  Two state sets: each seed's canonical trajectory, and the whole")
    print("  BRANCH TREE out to %d moves, so that a tie's other side is read"
          % BRANCH_D)
    print("  too. A tie's branches are isomorphic worlds and the menus are")
    print("  compared at both.\n")
    print("  %-5s %-7s %-8s %-9s %-9s %-8s %s"
          % ("ring", "seeds", "states", "vehicles", "bundles", "offsets",
             "offset ties"))
    out, misses, beaten, sigs = [], [], [], {}
    offcore, tiecore, notone = [], {}, []
    for R, S in rings:
        seeds = NF.element_seeds(R.M)
        nstate, nveh, nbundle, noff, ntie = 0, 0, 0, 0, 0
        for seed in seeds:
            # (state, moves left on the canonical line, moves left branching)
            stack, seen = [(dict(seed), MENU_T, BRANCH_D)], set()
            while stack:
                st, tleft, bleft = stack.pop()
                if tleft <= 0 and bleft <= 0:
                    continue
                key = vkey(st)
                if key in seen:
                    continue
                seen.add(key)
                L = R.M.lam_state(st)
                n, hits = R.M.elem_menu(st, L)
                best, veh_at, off_rec = abstract_menu(R, S, st, L)
                ring_set = dict((vkey(fac), fac) for (yx, fac) in hits)
                record(best == n and set(veh_at) == set(ring_set), misses,
                       (R.name, NF.show_state(st), n, best,
                        sorted(set(veh_at) - set(ring_set)),
                        sorted(set(ring_set) - set(veh_at))))
                for j, bare, cost, sig, core, same in off_rec:
                    record(cost >= bare, beaten,
                           (R.name, NF.show_state(st), bare, cost))
                    noff += 1
                    if cost == bare:
                        ntie += 1
                        sigs[(R.name,) + sig] = sigs.get((R.name,) + sig,
                                                         0) + 1
                        # lemma S: where minimal representatives are unique
                        # the equality case forces ONE divisor, whence the
                        # core lies in a minimal representative's support.
                        record(same, notone,
                               (R.name, NF.show_place(core),
                                NF.show_state(st)))
                        record(core in R.rider, offcore,
                               (R.name, NF.show_place(core),
                                NF.show_state(st)))
                        tiecore.setdefault(R.name, set()).add(core)
                nstate += 1
                nveh += len(veh_at)
                nbundle += sum(1 for v in veh_at.values() if len(v) > 1)
                for idx, (yx, fac) in enumerate(hits):
                    if idx and bleft <= 0:
                        break          # off the branch tree, one line only
                    st2 = dict(st)
                    for pl, e in fac.items():
                        st2[pl] = st2.get(pl, 0) + e
                    stack.append((st2, tleft - 1 if idx == 0 else 0,
                                  bleft - 1))
        print("  %-5s %-7d %-8d %-9d %-9d %-8d %d"
              % (R.name, len(seeds), nstate, nveh, nbundle, noff, ntie))
        out.append((R.name, len(seeds), nstate, nveh, nbundle, noff, ntie))
    print("\n  the bare door's bound is ATTAINED and not strict: %d of the"
          % sum(sigs.values()))
    print("  offered offsets tie their own bare door. A tie is the RIDER")
    print("  falling by exactly what the extra core power costs:\n")
    print("    %-5s %-8s %-8s %-6s %-4s %s"
          % ("ring", "m(bare)", "m(off)", "norm", "j", "ties"))
    for k in sorted(sigs):
        print("    %-5s %-8d %-8d %-6d %-4d %d"
              % (k[0], k[1], k[2], k[3], k[4], sigs[k]))
    print("  ties where the offset is a DIFFERENT divisor from its own bare")
    print("  door, which the filed lemma S says cannot happen where minimal")
    print("  representatives are unique: %d." % len(notone))
    print("  ties whose core is OUTSIDE the rider set, which follows from")
    print("  that: %d." % len(offcore))
    print("  and the CONVERSE, which no lemma here gives: the cores")
    print("  that actually attain the bound, against each ring's rider set:")
    for R, S in rings:
        got = tiecore.get(R.name, set())
        print("    %-5s attained at %-14s rider set %s"
              % (R.name,
                 " ".join(NF.show_place(p)
                          for p in sorted(got, key=R.M.place_key)) or "none",
                 " ".join(NF.show_place(p)
                          for p in sorted(R.rider, key=R.M.place_key))))
    print("\n  menu mismatches: %d; offsets beating their own bare door: %d"
          % (len(misses), len(beaten)))
    for row in misses[:5]:
        print("    %s at %s: ring %d, abstract %d; only-abstract %s; "
              "only-ring %s" % row)
    for row in beaten[:5]:
        print("    %s at %s: bare %d, offset %d" % row)
    ok(not misses, "PR2: %d menu mismatches, first %s"
       % (len(misses), misses[:1]))
    ok(not beaten, "PR3: %d offsets beat their bare door, first %s"
       % (len(beaten), beaten[:1]))
    ok(not notone, "lemma S: %d ties are two divisors, first %s"
       % (len(notone), notone[:1]))
    ok(not offcore, "%d ties have a core outside the rider set, first %s"
       % (len(offcore), offcore[:1]))
    return out


# ------------------------------------------------- S3 the recurrent price
def s3_tails(rings):
    section("S3  THE RECURRENT PRICE -- what an element lock costs per move")
    print("  Each element seed walked %d moves and its last %d read as the"
          % (LEAD + TAIL, TAIL))
    print("  tail, with the lock witnessed as the census witnesses it: the")
    print("  same vehicle repeated for %d consecutive moves.\n" % NF.LOCK_R)
    print("  %-5s %-7s %-9s %-22s %-10s %s"
          % ("ring", "seeds", "locked", "settled costs", "max ratio",
             "composition"))
    out, nonflat, unwitnessed, shifting = [], [], [], []
    for R, S in rings:
        seeds = NF.element_seeds(R.M)
        costs, nlock, ratio, compo, alt = set(), 0, 1.0, set(), 0
        for seed in seeds:
            log, st, L = R.M.run_elem(seed, LEAD + TAIL)
            tail = log[-TAIL:]
            wit = set(vkey(mv[1]) for mv in tail[-NF.LOCK_R:])
            if not record(len(wit) == 1, unwitnessed,
                          (R.name, NF.show_state(seed), len(wit))):
                continue
            nlock += 1
            tc = [mv[2] for mv in tail]
            record(len(set(tc)) == 1, nonflat,
                   (R.name, NF.show_state(seed), tc[:8]))
            costs.add(tc[0])
            ratio = max(ratio, float(tc[-1]) / tc[0])
            alt += (len(set(vkey(mv[1]) for mv in tail)) > 1)
            comps = set((len(mv[1]), sum(mv[1].values())) for mv in tail)
            compo |= comps
            record(len(comps) == 1, shifting,
                   (R.name, NF.show_state(seed), sorted(comps)))
        print("  %-5s %-7d %-9d %-22s %-10.2f %s"
              % (R.name, len(seeds), nlock,
                 " ".join(str(c) for c in sorted(costs)), ratio,
                 " ".join("%d places/%d exp" % c for c in sorted(compo))))
        out.append((R.name, len(seeds), nlock, sorted(costs), ratio,
                    sorted(compo), alt))
    print("\n  tails without a lock witness: %d; tails whose cost is not"
          % len(unwitnessed))
    print("  flat: %d; tails whose bundle composition shifts: %d;"
          % (len(nonflat), len(shifting)))
    print("  tails whose vehicle ALTERNATES at a flat cost: %d."
          % sum(r[6] for r in out))
    for row in (unwitnessed + nonflat + shifting)[:6]:
        print("    %s %s %s" % row)
    ok(not unwitnessed, "S3: %d tails carry no lock witness" % len(unwitnessed))
    ok(not nonflat, "PR4: %d tails are not flat, first %s"
       % (len(nonflat), nonflat[:1]))
    ok(not shifting, "PR5: %d tails shift composition, first %s"
       % (len(shifting), shifting[:1]))
    return out


# ------------------------------------------------------------- S4 synthesis
def s4_synthesis(menus, tails, heads):
    section("S4  THE SYNTHESIS -- what the ring supplies, in one table")
    print("  %-22s %-24s %s" % ("", "function fields", "number rings"))
    print("  %-22s %-24s %s"
          % ("cost monoid", "(degrees, +), m = 0", "(norms, *), m = 1"))
    print("  %-22s %-24s %s"
          % ("m", "least total degree", "least norm product"))
    print("  %-22s %-24s %s"
          % ("derivation", "shortest path", "shortest path (min, *)"))
    print("  %-22s %-24s %s"
          % ("ladder", "one, the doubling tick", "one per item, its gap"))
    print("  %-22s %-24s %s"
          % ("rider cost bound", "= the genus, measured",
             "= max m, no second object"))
    print("\n  measured here: %s"
          % "; ".join("%s %d seeds, %d states, %d vehicles"
                      % (r[0], r[1], r[2], r[3]) for r in menus))
    print("  tails: %s"
          % "; ".join("%s %d locks, costs %s, max ratio %.2f"
                      % (r[0], r[2], r[3], r[4]) for r in tails))
    print("  ladder column parts from the colour at %d place(s): %s"
          % (len(heads),
             ", ".join("%s %s" % (h[0], NF.show_place(h[1])) for h in heads)))


def main():
    rings = []
    for (name, M, h, disc, gen) in CS.RINGS:
        R = CS.Ring(name, M, h, disc, gen)
        rings.append((R, Supply(R)))
    s0_control(rings)
    heads = s1_supply(rings)
    menus = s2_menus(rings)
    tails = s3_tails(rings)
    s4_synthesis(menus, tails, heads)
    print("\nALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
