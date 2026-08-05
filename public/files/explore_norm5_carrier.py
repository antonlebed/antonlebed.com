r"""explore_norm5_carrier.py -- does a WALK seat a norm-5 carrier beside a
consumer over 2? The k >= 2 supply is priced and has never been paid;
this shops a quadratic field holding both, plants the pair, and reads the
door, the ablation and the limit against the window read off the column.

THE QUESTION. A place carrying v_l = k needs norm >= l^k + 1, so the
floor is set by how SMALL l is, and at l = 2 it is ATTAINED: norms 3, 5,
9, 17 carry k = 1, 2, 3, 4. Norm 5 is therefore the cheapest supply of
k = 2 that exists anywhere. That is a PRICE fact and the corpus has it
(explore_carrier_window.py). What it has never had is the same fact
PAID -- every k >= 2 supply in the corpus is a table entry, never a
place a menu charged beside a consumer that reads it. The one carrier
ever paid is the residue-degree-3 undercut, and that is a k = 1
phenomenon at l = 7 (explore_cubic_carrier.py); the two do not meet,
since l = 2 cannot divide q^2 + q + 1.

The consumer is a place over 2, and the corpus says its window departs
from the filed closed form in BOTH directions depending on its shape --
which makes the payment a two-sided test rather than a confirmation.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The shopping
half is the FIELD's -- split, inert, ramified, residue degree, place
norm. The reading half is the WALKER's -- door, menu, seated, supply,
load-bearing. The welding term is CARRIER and it belongs to the walker:
a place Q is a carrier for a seated P over l when v_l(L) is set by
N(Q) - 1 rather than by P's own ladder, and the ABLATION is what
decides it. The WINDOW belongs to the column and is defined there --
the deepest a whose self-supply is still under k -- and everything the
menu says is scored against that reading, never the reverse.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From explore_cubic_carrier.py: the shop-then-plant-then-ablate
    shape, and the census-over-a-seed-belt as the honest half of "does a
    walk seat it". Carried as METHOD only. Nothing about WHICH place
    wins a menu is carried -- that file's universe has a norm-3 head
    undercutting a norm-8 carrier, and here the carrier is norm 5 in a
    universe whose cheapest place is norm 2 or 3. Every menu is computed.
 T2 From explore_carrier_window.py: the three consumer columns over 2
    (Z's split shape, the inert shape, Q(i)'s ramified shape) are
    corpus readings, and the windows below are RE-BRUTED here rather
    than quoted. The transplanted part is the DEFINITION of the window
    and of the depth shift, not any measured number.
 T3 The class group is NOT carried and NOT computed. The door and the
    supply are residue arithmetic; h enters neither. This is a
    deliberate narrowing -- no element-world reading appears here, and
    the walk below is the IDEAL walk throughout.
 T4 The deep-depth licence for a column past its brute is the
    logarithm's recurrence lambda(a) = p*lambda(a - e). The cubic shop
    licensed it from a DERIVED threshold floor(e*p/(p-1)) + 1. That
    threshold is NOT carried: it is a statement about U_a alone, and
    lambda is the whole unit group's, whose bottom rungs a head holds
    flat for longer. Here the recurrence's start depth is MEASURED --
    the least a1 from which it holds on the WHOLE remaining brute, with
    at least MIN_CONFIRM confirmed rungs -- and the derived threshold is
    printed beside it as an observable, never as the licence.

THE HAND-ATTACK, on paper before any engine code.

  WHAT A NORM-5 CARRIER IS. A place Q over 5 with f = 1 has N(Q) = 5 and
  N(Q) - 1 = 4, so v_2(N(Q) - 1) = 2 exactly: seated at any depth it puts
  v_2(L) >= 2. f = 1 over 5 means 5 SPLIT or 5 RAMIFIED -- and the
  ramified case matters, since it puts d = -5 in the shop, which is the
  ring the corpus walks most. A norm-25 inert place over 5 supplies
  v_2(24) = 3 and is a different carrier at a different norm; the shop
  keeps it apart rather than counting it.

  THE THREE CONSUMER SHAPES, and why the test is two-sided. In a
  quadratic field a place over 2 is one of exactly three shapes, and the
  head criterion (f = 1, e = (p-1)p^t, mu_p in the completion) reads
  each of them without a choice: mu_2 = {+-1} lies in every field, and
  (2-1)*2^t = 1, 2 are both <= 2 = the degree, so
    A  2 SPLIT      e = 1, f = 1, norm 2  -- HEADED
    B  2 INERT      e = 1, f = 2, norm 4  -- headless (f = 2)
    C  2 RAMIFIED   e = 2, f = 1, norm 2  -- HEADED
  and the corpus's window readings say A runs WIDER than the filed form
  and C runs NARROWER, at k = 2. So the same carrier must be
  load-bearing one depth PAST where the formula closes the window at A,
  and must go dead one depth BEFORE it at C.

  THE COLUMNS, hand-derived. At A the completion is Q_2 and the column
  is Z's: 1, 2, 2, 4, 8, ... so v_2 = 0, 1, 1, 2, 3 -- one flat step at
  the bottom, which is the head. Window at k = 2 is the deepest a with
  v_2 < 2, i.e. a = 3, against a filed e(k-1) + 1 = 2. At B the group is
  k^* x U_1/U_a with k^* of order 3 and the unramified step at every
  rung, so lambda = 3 * 2^(a-1), v_2 = a - 1, window 2 = filed 2. At C
  the filed form gives v_2 = ceil((a-1)/2) and the corpus reads the
  measured column climbing FASTER at the bottom, so the window closes at
  2 against a filed 3.

  THE DOOR THE CARRIER MOVES, at A, hand-computed. Plant P over 2 at
  depth 1 alone: L = lambda(P) = 1, and the door is the least r with
  lambda(P^(1+r)) not dividing L, so r = 1 and the move costs 2. Seat Q
  beside it: L = lcm(1, 4) = 4, and lambda(P^2) = 2, lambda(P^3) = 2,
  lambda(P^4) = 4 all divide 4 while lambda(P^5) = 8 does not -- door 4,
  cost 16. That is a FOUR-fold door step where the degree-3 carrier's
  whole visible effect was one, and the reason is that k = 2 and the
  head's flat step compound. At depth 4 the ablated and the carried
  state both read v_2(L) = 2 and the door is 1 either way: dead, which
  is the window closing at 3.

  WHAT MAKES THIS A PAYMENT AND NOT A TABLE. The door is charged on a
  MENU against every other place in the universe, and the ablation is
  the control that says the step is Q's. A supply that changes no door
  is not a carrier however cheap its norm.

  DISTRUST THE MARGIN. The derived half is the door arithmetic and the
  three-shapes census, both brute-checked (S1, S3). The vibes half:
  "some field in the box holds a norm-5 place beside each shape over 2"
  is asserted by the enumeration and reported as its own finding, and
  "a void walk will not seat norm 5" is a SCOPE the census measures,
  never a claim -- the cheapest place in a 2-inert field is norm 3 or 4,
  and norm 5 is not obviously out of reach there.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 S1 reproduces: this file's ring model agrees with the corpus's
     Z[sqrt(-5)] walker at every place over p <= 50 -- same (e, f)
     multiset, same lambda at depths 1..6, same door on a common state,
     same first six moves of the void walk. Any disagreement is this
     file's until shown otherwise.
  P2 S2 finds all three arms non-empty inside |d| <= DISC_CAP, and every
     shopped field prints a place over 5 of residue degree 1.
  P3 S3 prints v_2(N(Q) - 1) = 2 at every norm-5 carrier -- no arm gets
     a different k -- and the consumer windows at k = 2 read
     A: 3 (filed 2), B: 2 (filed 2), C: 2 (filed 3).
  P4 S4's planted pair moves the door at consumer depth 1 from 1 to 4 at
     arm A (cost 2 -> 16), and the load-bearing depth range ends exactly
     at the TRUE window at all three arms -- 3, 2, 2 -- and not at the
     filed one.
  P5 S5's census finds at least one walked state seating a norm-5 place
     beside a seated place over 2 at some arm. If it finds none anywhere,
     the finding is what forbids the pairing, and the door reading of S4
     stands as a planted result exactly as the cubic carrier's did.
  P6 S5's limit reading: the planted pair with and without the carrier
     locks at DIFFERENT recurrent prices at arm A. A carrier that moves a
     door but not the limit is a weaker result and is reported as such.

RESOURCE ENVELOPE. Brute quotients capped at INDEX_CAP residues, which
is depth 14 at norm 2 and depth 7 at norm 4; one process, no arrays, well
under the 512MB analysis default. Estimated wall clock under 3 minutes.

FINDINGS (tiers stated per line; run record at the end).

  F1 THE PAIRING IS COMMON, NOT SHOPPED FOR -- rule in range. Inside
     |d| <= 200 a norm-5 place sits beside a place over 2 in 141 fields:
     21 with 2 split, 24 with 2 inert, 96 with 2 ramified. Nothing has to
     be engineered, because the carrier spec is only "a place over 5 of
     residue degree 1", which 5 SPLIT and 5 RAMIFIED both meet. That is
     the whole difference from the degree-3 undercut, where the cheap
     carrier forced 2 inert and left the head exactly one seat: at l = 2
     the cheapest supply of k = 2 is a norm the generic ring already has.
     The arm representatives the shop returns are d = -15 (5 ramified),
     d = 5 (5 ramified) and d = -1 -- so Q(i), the corpus's own narrow-
     window specimen, is an arm-C field with 5 SPLIT, and the ring the
     shop hands the widest arm is one whose norm-5 place is ramified.

  F2 EVERY NORM-5 CARRIER SUPPLIES EXACTLY k = 2, INDEPENDENT OF ITS OWN
     RAMIFICATION -- property, checked at all three arms. N - 1 = 4 at
     norm 5 whether the place is split or ramified, so v_2 = 2 flat. The
     carrier's own column (4, 20, 20, 100, 100 at a ramified 5; 4, 20,
     100, 500, 2500 at a split one) differs between the arms and the
     supply does not: what a carrier hands over is its RESIDUE
     CARDINALITY, and its own depth structure is not consulted.

  F3 THE WINDOW IS A MENU FACT AND NOT ONLY A COLUMN FACT -- rule in
     range, three arms x six depths, ablation-controlled. The deepest
     depth at which seating the carrier changes the consumer's door is
     the TRUE window read off the brute column at every arm -- 3, 2, 2 --
     and it is the filed form e(k-1)+1 at only one of them:

       arm            consumer        TRUE  filed   deepest LOAD-BEARING
       A  2 split     e=1 f=1 headed     3      2     3
       B  2 inert     e=1 f=2 headless   2      2     2
       C  2 ramified  e=2 f=1 headed     2      3     2

     So the headed departure, which the corpus had only as a reading off
     a unit-exponent column, is what a greedy engine actually charges --
     in BOTH directions, one depth past the formula at A and one short of
     it at C.

  F4 THE HEAD'S TRANSIENT COSTS DEPTH AND BUYS SIZE, AND THAT IS ONE
     MECHANISM READ TWICE -- observation, the sharpest number here. At the
     ramified consumer of Q(i) the column's v_2 is 0, 1, 2, 2, 2, 2, 2,
     3, 3: it climbs FAST at the bottom, which closes the window at 2
     instead of 3, and then sits FLAT for five rungs. Inside the window
     that flat stretch is what the door has to cross: seating the carrier
     at consumer depth 1 moves the door from 1 to 7, a move costing 2
     against 128. At the split consumer the same carrier moves the door
     from 1 to 4 (cost 2 -> 16), and at the headless inert consumer from
     1 to 3 (cost 4 -> 64). The degree-3 carrier's whole visible effect
     was ONE door step (7 -> 49, explore_cubic_carrier.py). So the two
     halves of a head are the same fact seen from two sides -- fewer
     depths where a carrier is load-bearing, and a far larger door at
     each of them -- and the k = 2 supply is what makes the second half
     visible, since a k = 1 carrier can never reach past the first rung
     of a flat stretch.

  F5 TWO ARMS PAY IT WITH A WALK AND THE THIRD NEVER DOES, AND THE THIRD
     IS THE ONE WITH THE BIGGEST DOOR -- observation over the walked belt
     (norm <= 64, LOCK_R = 10). Every seed of every belt locks. States
     seating a norm-5 place beside a place over 2 / of those the
     ablation-confirmed load-bearing ones / of THOSE the ones the WALK
     seated rather than the seed: 429 / 269 / 156 of 1259 states at arm A,
     148 / 15 / 13 of 358 at arm B, and 99 / 66 / ZERO of 541 at arm C.
     So the split and inert consumers get the supply charged on a menu
     against every other place in the universe, which is what the priced
     fact had never had. The ramified consumer does not: all 66 of its
     load-bearing states come from seeds that already held both places,
     and no walk in the belt ever moves either one in. That third column
     is the whole reason the census is kept -- the first two columns alone
     read as "walks seat it", and they are the columns the seed can fake.

     Where the belts LOCK is the measurement beside it, and it does not
     say what a one-line mechanism would. Arm C's 48 walks lock at seven
     different places: 13 on the norm-9 inert place over 3, 17 on the two
     norm-5 places -- the CARRIER itself, at 5/move -- 12 on norm-13, 4 on
     17, and 2 on the ramified place over 2 at cost 4, so the consumer is
     not uniformly priced out either. Arm A's 106 locks sit mostly on its
     norm-3 place (41) and its two norm-2 places (56); arm B's 28 sit on
     norm-19 (14), norm-11 (11) and its own norm-4 consumer (3). What is
     measured is therefore the walk-seated count and not a story about
     why: at arm C no walk in the belt ever moves either member of the
     pair into a state where the other is already seated, while at arms A
     and B walks do it 156 and 13 times. Arm C reproduces the degree-3
     carrier's shape -- rare pairing, planted state -- and the arm with
     the largest door is the arm whose walks never build the pairing,
     which is a coincidence of two measurements until something connects
     them.

  F6 THE CARRIER MOVES THE LIMIT AT EVERY ARM, AND AT TWO OF THEM IT IS
     NOT THE THING THE WALK LOCKS ON -- observation, planted pair with and
     without. Walked to lock from {consumer at depth 1, carrier at depth
     1} against the same seed ablated: 3[e2,f1] at 9/move against
     2[e1,f1] at 2/move (A); 19[e1,f1] at 19/move against 2[e1,f2] at
     4/move (B); 5[e1,f1] at 5/move against 3[e1,f2] at 9/move (C).

     THE CONFOUND, which is named rather than removed because it cannot be
     designed away here: ablating the carrier removes its SUPPLY and its
     availability as a cheap VEHICLE in one move, and there is no
     same-norm place that supplies nothing -- every odd norm q has q - 1
     even, so any odd-norm place carries some v_2. What separates the two
     is WHICH place the carried walk locks on. At A and B it is a third
     place, norm 9 and norm 19, so the carrier changed the limit without
     being it and those two readings are clean. At C the walk locks ON the
     carrier, at 5/move against the ablated 9/move -- so the one case
     where the recurrent price goes DOWN is also the one case where supply
     and vehicle cannot be told apart, and "a raised door is not a raised
     limit" is a reading of that confounded row and not of the other two.

  F7 THE WINDOW IS THE SHAPE'S, THE DOOR IS THE COMPLETION'S -- rule in
     range over the swept box, and the correction that S6 exists for. S3
     and S4 read ONE field per arm, and a place over 2 does NOT determine
     its completion: Q_2 has six ramified quadratic extensions and Q(i) is
     one of them, so "arm C's window is 2" was one completion's reading
     wearing a shape's name. Swept over every shopped field with |d| <= 60
     -- 5 fields at arm A, 8 at arm B, 28 at arm C -- the k = 2 window
     takes exactly ONE value per arm (3, 2, 2), so the shape does fix it --
     and the DEEPEST LOAD-BEARING DEPTH equals it at all 41, which is what
     lifts F3's headline off its three fields. The DOOR does not: arm A's depth-1 door is 4 at all five and arm B's
     is 3 at all eight, but arm C's takes 5, 6 and 7, because what sets it
     is how long the column's flat stretch runs and that is completion
     data -- v_2 breaks at depth 6 in Q(sqrt(-6)) and at depth 8 in Q(i).
     So the two halves of F4 separate cleanly: the depth a head COSTS is a
     shape invariant, and the size it BUYS is not. Q(i) is the extreme of
     its arm rather than its representative, and the 1 -> 7 door is
     Q(i)'s, not the ramified shape's. What the door IS a function of is
     below, and it is not the completion either.

     AND THE DOOR IS A FUNCTION OF d mod 8 AND OF NOTHING ELSE, WHICH IS
     NOT THE SAME AS BEING COMPLETION DATA -- it is COARSER. Over the 28
     ramified fields the residue sorts the door with no exceptions:
     d = 2 and 6 mod 8 give door 5 (7 fields each), d = 3 gives 6 (8
     fields), d = 7 gives 7 (6 fields). But d mod 8 does not pin the
     completion. Q_2(sqrt d) is the class of d in Q_2^* / (Q_2^*)^2,
     whose invariant is (v_2(d) mod 2, odd part mod 8), and the 28 fields
     realize SIX such classes against those FOUR residues: d = 2 mod 8
     carries odd parts 1 and 5, d = 6 mod 8 carries 3 and 7, and each
     even residue therefore spans two DISTINCT ramified extensions of
     Q_2 -- 6 being the whole count of them. So the door is constant
     across completions the residue merges, and Q_2(sqrt 2) and
     Q_2(sqrt 10) print the identical column [0,1,2,2,2,3,3,4,4] here.
     The size a head buys is a rule in range on one residue, sitting
     strictly between the shape and the completion, and the extreme case
     Q(i) sits in the d = 7 class rather than being special. What is
     still open is WHY that class runs longest.

  WHAT THIS DOES NOT SHOW. The sweep runs only to |d| <= 60 and only at
  k = 2; the k >= 3 rows of S3 are still one field per arm. The belt
  census and the limit readings are ONE field per arm throughout -- S6
  sweeps columns and doors, not walks. The walks
  are the IDEAL walks (T3) -- no class group, no element world. The
  census ablation deletes ONE norm-5 place, so in a ring where 5 SPLITS
  the conjugate place stays seated and supplies the same v_2 = 2; that
  makes the walk-seated counts a LOWER bound on carriers and never an
  upper one. And the
  arm-C door values 5, 6, 7 are three values over 28 fields sorted by a
  residue coarser than the completion, not a law about which extension
  gives which: what would settle that is the flat stretch's length as a
  function of the completion, which is not computed here. That the
  residue suffices over this box is a rule in range and not a proof that
  the two merged pairs of completions agree at every depth.

S6 CARRIES NO PREDICTION, and says so rather than pretending otherwise.
It was written after the rest had run, when the scope line for the window
readings was found to claim a SHAPE where the evidence reached one field.
A section added to answer an overclaim cannot predict what it is checking;
what it prints either widens the claim's range or narrows its wording, and
here it did both.

RUN RECORD. python prime/code/memwatch.py prime/code/explore_norm5_carrier.py
-- 4087 asserted checks passed, peak working set 29.6MB, wall 61.6s.
Three instrument corrections, in the order they were caught. The census
first counted a load-bearing state
without asking whether the SEED already held both places, which cannot
tell a pairing a walk built from one it was handed -- the exact defect
the cubic carrier's census had to learn, reintroduced here and caught by
reading its own headline back. The split into seed-held and walk-seated
is what turns arm C's 66 into a 0 and makes this file's walk claim two
arms wide rather than three. The second was caught by the run rather than
by reading: the licensed tail was being demanded at
every brute column, and a norm-9 inert place reaches only depth 4, which
is three rungs -- not enough to license anything. The fix is the split
the corpus's own law already justifies: a column is brute-read as the
WALK's column only where a head can sit (f = 1, e = (p-1)p^t), and
everywhere else the brute is spent as a CONTROL that the closed form
passes at every rung. That control is what makes arm B's row above a
measurement rather than the formula restated. The third was found by
writing F7 out for a reader who cannot already know it: S6 asserted the
door constant on d mod 8 and then CALLED that residue the completion,
which is false in the one direction that matters -- the residue is
coarser. The six square classes the box realizes are now computed and
asserted beside the four residues, so the sweep says which of the two
the door is a function of instead of assuming they are one thing.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from math import gcd

import explore_carrier_window as CW
import explore_lock_budget as LB

K5 = LB.K5                # the corpus's Z[sqrt(-5)] walker, S1's control

CHECKS = 0

DISC_CAP = 200        # |d| ceiling for the shop
INDEX_CAP = 20000     # residues allowed in one brute-forced quotient
MAXP = 20000          # rational primes enumerated into a walker universe
MIN_CONFIRM = 4       # brute rungs a measured recurrence must confirm on
TAIL_CAP = 40         # depths a column may be extended past its brute
BELT = 64             # seed belt: generator products of norm <= this
SWEEP_CAP = 60        # |d| ceiling for the across-completions sweep (S6)
K_SHOWN = 4           # supply levels the window table prices


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def lcm(a, b):
    return a // gcd(a, b) * b


def v_p(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def sieve(n):
    flag = [True] * (n + 1)
    flag[0] = flag[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if flag[i]:
            for j in range(i * i, n + 1, i):
                flag[j] = False
    return [i for i in range(n + 1) if flag[i]]


PRIMES = sieve(MAXP)


def squarefree(d):
    m = abs(d)
    i = 2
    while i * i <= m:
        if m % (i * i) == 0:
            return False
        i += 1
    return True


# ------------------------------------------------------- columns and heads
class Column(object):
    """One place's lambda column: brute where the residues fit, extended
    past it by the recurrence lambda(a) = p*lambda(a - e) -- whose start
    depth is MEASURED on the brute's own tail (T4) and never assumed."""

    def __init__(self, p, e, f, brute):
        self.p, self.e, self.f = p, e, f
        self.q = p ** f
        self.brute = list(brute)
        self.derived_a0 = (e * p) // (p - 1) + 1     # printed, not used
        self.a1 = self._measure_start()
        self.cache = {0: 1}
        for i, x in enumerate(brute):
            self.cache[i + 1] = x

    def _measure_start(self):
        """Least a1 >= e + 1 from which lambda(a) = p*lambda(a-e) holds on
        the WHOLE remaining brute, with at least MIN_CONFIRM confirmed
        rungs. None where the brute is too short to license anything."""
        n = len(self.brute)
        for a1 in range(self.e + 1, n + 1):
            if n - a1 + 1 < MIN_CONFIRM:
                return None
            if all(self.brute[a - 1] == self.p * self.brute[a - self.e - 1]
                   for a in range(a1, n + 1)):
                return a1
        return None

    def confirmed(self):
        return 0 if self.a1 is None else len(self.brute) - self.a1 + 1

    def lam(self, a):
        if a in self.cache:
            return self.cache[a]
        assert a > len(self.brute), "column cache hole at %d" % a
        assert self.a1 is not None, \
            "no licensed tail for p=%d e=%d f=%d (brute depth %d)" \
            % (self.p, self.e, self.f, len(self.brute))
        assert a <= len(self.brute) + TAIL_CAP, \
            "column extended past TAIL_CAP at p=%d e=%d f=%d" \
            % (self.p, self.e, self.f)
        v = self.p * self.lam(a - self.e)
        self.cache[a] = v
        return v

    def standard(self, a):
        if a == 0:
            return 1
        return (self.q - 1) * self.p ** -(-(a - 1) // self.e)


def depth_shift(col, ell, e):
    """The column's asymptotic DEPTH shift x: the least x >= 0 for which
    v_ell(lambda(P^a)) = ceil((a-1-x)/e) on a whole suffix, with the depth
    that suffix starts at. This is explore_carrier_window's own instrument,
    CALLED rather than re-implemented: it is a DEFINITION and not a
    measurement, and two copies of a definition are two places for it to
    drift. What this file re-brutes is every COLUMN it reads."""
    return CW.excess_of(col, ell, e)


def true_window(col, ell, k):
    """The load-bearing window read STRAIGHT off the measured column: the
    deepest a whose self-supply v_ell(lambda(P^a)) is still under k. This
    is the definition; every closed form is scored against it."""
    good = [a for a in range(1, len(col) + 1) if v_p(col[a - 1], ell) < k]
    return max(good) if good else 0


def filed_window(e, k):
    return e * (k - 1) + 1


def head_shape(ell, e, f):
    """The head criterion's SHAPE clause (f = 1, e = (l-1)l^t). The third
    clause -- mu_l in the completion -- is not decidable from (e, f); over
    l = 2 it is free, since mu_2 = {+-1} lies in every field, so over 2
    this test IS the criterion."""
    if f != 1:
        return False
    m = e
    if m % (ell - 1) != 0:
        return False
    m //= (ell - 1)
    while m % ell == 0:
        m //= ell
    return m == 1


# --------------------------------------------------------- the ring model
class QModel(object):
    """A walker model over one quadratic field: places (p, e, f, i), the
    lambda columns, doors and the ideal menu. Duck-typed for the corpus's
    imported walker (explore_lock_budget.walk_to_lock)."""

    def __init__(self, d, brute_primes=(2, 3, 5), maxp=MAXP):
        ok(squarefree(d) and d not in (0, 1), "d = %d is not a field" % d)
        self.d = d
        self.O = CW.QuadOrder(d)
        self.UNIVERSE = []
        self.lattice = {}
        for p in PRIMES:
            if p > maxp:
                break
            seen = {}
            for (e, f, lat) in self.O.places(p):
                i = seen.get((e, f), 0)
                seen[(e, f)] = i + 1
                pl = (p, e, f, i)
                self.UNIVERSE.append(pl)
                self.lattice[pl] = lat
        self.UNIVERSE.sort(key=self.place_key)
        # A column is BRUTE-READ wherever a head can sit -- f = 1 with
        # e = (p-1)p^t -- and CHECKED against the closed form everywhere
        # else. The split is not a shortcut: a headless place's column is
        # the closed form by the corpus's law, and reading a measured
        # recurrence off a norm-9 brute that reaches depth 4 would license
        # a tail on three rungs. So the headless brute is spent as a
        # CONTROL on the formula the walk then uses.
        self.columns = {}
        self.checked = 0
        for pl in self.UNIVERSE:
            if pl[0] not in brute_primes:
                continue
            col = self.brute(pl)
            if len(col) < 3:
                continue
            if head_shape(pl[0], pl[1], pl[2]):
                self.columns[pl] = Column(pl[0], pl[1], pl[2], col)
            else:
                std = Column(pl[0], pl[1], pl[2], col)
                for a in range(1, len(col) + 1):
                    ok(col[a - 1] == std.standard(a),
                       "headless place %s departs from the closed form at"
                       " depth %d: %d against %d"
                       % ((pl,), a, col[a - 1], std.standard(a)))
                    self.checked += 1
                self.headless_brute = getattr(self, "headless_brute", {})
                self.headless_brute[pl] = col

    # ---- brute column at one place, by its own lattice
    def brute(self, pl, cap=INDEX_CAP):
        P = self.lattice[pl]
        O = self.O
        col, a, Pa = [], 1, P
        while CW.QuadOrder.index(Pa) <= cap:
            h11, h12, h22 = Pa
            reps = [(x, y) for x in range(h11) for y in range(h22)]
            units = [u for u in reps
                     if not CW.QuadOrder.in_lattice(u, P)]
            one = CW.QuadOrder.reduce((1, 0), Pa)
            lam = CW.lam_of_group(
                units,
                lambda u, v, L=Pa: CW.QuadOrder.reduce(O.mul(u, v), L),
                one)
            npl = CW.QuadOrder.index(P)
            ok(CW.QuadOrder.index(Pa) == npl ** a,
               "P^%d has index %d, not %d" % (a, CW.QuadOrder.index(Pa),
                                              npl ** a))
            ok(len(units) == npl ** a - npl ** (a - 1),
               "unit count at depth %d is %d, not %d"
               % (a, len(units), npl ** a - npl ** (a - 1)))
            ok((npl ** a - npl ** (a - 1)) % lam == 0,
               "exponent %d does not divide the order at depth %d"
               % (lam, a))
            col.append(lam)
            a += 1
            Pa = CW.QuadOrder.lat_mul(Pa, P, O)
        return col

    # ---- place accessors
    def place_norm(self, pl):
        return pl[0] ** pl[2]

    def place_key(self, pl):
        return (pl[0] ** pl[2], pl[1], pl[2], pl[3])

    def show(self, pl):
        return "%d[e%d,f%d]%s" % (pl[0], pl[1], pl[2],
                                  ".%d" % pl[3] if pl[3] else "")

    def show_st(self, st):
        parts = ["%s^%d" % (self.show(pl), a)
                 for pl, a in sorted(st.items(),
                                     key=lambda kv: self.place_key(kv[0]))
                 if a]
        return "*".join(parts) if parts else "(1)"

    def places_over(self, p):
        return [pl for pl in self.UNIVERSE if pl[0] == p]

    def column_of(self, pl):
        """The measured column at pl, whether it is the one the walk uses
        (headed) or the control the closed form passed (headless)."""
        if pl in self.columns:
            return self.columns[pl].brute
        return getattr(self, "headless_brute", {}).get(pl)

    # ---- the lambda column, doors and the menu
    def lam_P(self, pl, a):
        if a == 0:
            return 1
        col = self.columns.get(pl)
        if col is not None:
            return col.lam(a)
        p, e = pl[0], pl[1]
        return (self.place_norm(pl) - 1) * p ** -(-(a - 1) // e)

    def lam_state(self, st):
        L = 1
        for pl, a in st.items():
            L = lcm(L, self.lam_P(pl, a))
        return L

    def door_r(self, pl, a, L):
        r = 1
        while L % self.lam_P(pl, a + r) == 0:
            r += 1
            assert r < 500, "door search runaway"
        return r

    def ideal_menu(self, st, L):
        best, ties = None, []
        for pl in self.UNIVERSE:
            nrm = self.place_norm(pl)
            if best is not None and nrm > best:
                break
            r = self.door_r(pl, st.get(pl, 0), L)
            cost = nrm ** r
            if best is None or cost < best:
                best, ties = cost, [(pl, r)]
            elif cost == best:
                ties.append((pl, r))
        assert best <= MAXP, "universe guard: door beyond MAXP"
        ties.sort(key=lambda t: self.place_key(t[0]))
        return best, ties

    def gen_products(self, maxnorm):
        pls = [pl for pl in self.UNIVERSE
               if self.place_norm(pl) <= maxnorm]
        out = []

        def rec(i, cur, nrm):
            if cur:
                out.append((nrm, dict(cur)))
            for j in range(i, len(pls)):
                pl = pls[j]
                n2 = nrm * self.place_norm(pl)
                if n2 > maxnorm:
                    break
                a = 1
                while n2 <= maxnorm:
                    cur[pl] = a
                    rec(j + 1, cur, n2)
                    a += 1
                    n2 *= self.place_norm(pl)
                del cur[pl]

        rec(0, {}, 1)
        out.sort(key=lambda x: x[0])
        return out


def walk_trace(M, seed, cap=None):
    """The greedy walk as (state, L, move) triples, one per move, stopping
    at the same lock witness the imported walker uses."""
    st = dict(seed)
    L = M.lam_state(st)
    run_pl, run = None, 0
    trace = []
    for _ in range(cap or LB.WALK_CAP):
        cost, ties = M.ideal_menu(st, L)
        pl, r = ties[0]
        trace.append((dict(st), L, (pl, r, cost)))
        run = run + 1 if pl == run_pl else 1
        run_pl = pl
        st = dict(st)
        st[pl] = st.get(pl, 0) + r
        L = M.lam_state(st)
        if run >= LB.LOCK_R:
            break
    trace.append((dict(st), L, None))
    return trace


# ------------------------------------------------------ S1 positive control
def s1_control():
    section("S1  POSITIVE CONTROL -- this ring model against the corpus's")
    print("  The corpus's Z[sqrt(-5)] walker (explore_number_field_lock.py)")
    print("  is an INDEPENDENT model of the same ring: its places are named")
    print("  by shape and its columns are closed forms. If this file's")
    print("  lattice model disagrees with it, this file is wrong until")
    print("  shown otherwise -- the verdicts below all ride on this.")
    M = QModel(-5)
    kmap = {}
    for pl in K5.UNIVERSE:
        if K5.place_char(pl) > 50:
            continue
        p = K5.place_char(pl)
        f = 2 if pl[0] == 'inert' else 1
        e = 2 if pl[0] == 'ram' else 1
        kmap.setdefault((p, e, f), []).append(pl)
    mine = {}
    for pl in M.UNIVERSE:
        if pl[0] > 50:
            continue
        mine.setdefault((pl[0], pl[1], pl[2]), []).append(pl)
    ok(set(kmap) == set(mine),
       "place shapes over p <= 50 differ: %s vs %s"
       % (sorted(set(kmap) - set(mine)), sorted(set(mine) - set(kmap))))
    ok(all(len(kmap[s]) == len(mine[s]) for s in kmap),
       "place COUNTS differ at some shape")
    print("  place shapes over p <= 50 agree: %d shapes, %d places"
          % (len(kmap), sum(len(v) for v in mine.values())))
    bad = []
    for s in sorted(kmap):
        for a in range(1, 7):
            x, y = K5.lam_P(kmap[s][0], a), M.lam_P(mine[s][0], a)
            if x != y:
                bad.append((s, a, x, y))
    print("  lambda at depths 1..6, every shape over p <= 50:")
    if bad:
        for (s, a, x, y) in bad:
            print("    DISAGREE (p,e,f)=%s a=%d: corpus %d, this file %d"
                  % (s, a, x, y))
    else:
        print("    every value agrees")
    ok(not bad, "lambda disagrees with the corpus model at %d places"
       % len(bad))
    # a door on a common state, and the void walk's first moves
    st_k = {kmap[(3, 1, 1)][0]: 2, kmap[(2, 2, 1)][0]: 1}
    st_m = {mine[(3, 1, 1)][0]: 2, mine[(2, 2, 1)][0]: 1}
    Lk, Lm = K5.lam_state(st_k), M.lam_state(st_m)
    ok(Lk == Lm, "state invariant differs: %d vs %d" % (Lk, Lm))
    for s in sorted(kmap):
        ok(K5.door_r(kmap[s][0], 1, Lk) == M.door_r(mine[s][0], 1, Lm),
           "door differs at shape %s" % (s,))
    print("  state invariant and every door on it agree (L = %d)" % Lm)
    stk, stm = {}, {}
    moves_k, moves_m = [], []
    for _ in range(6):
        ck, tk = K5.ideal_menu(stk, K5.lam_state(stk))
        cm, tm = M.ideal_menu(stm, M.lam_state(stm))
        plk, rk = tk[0]
        plm, rm = tm[0]
        moves_k.append((K5.place_norm(plk), rk, ck))
        moves_m.append((M.place_norm(plm), rm, cm))
        stk[plk] = stk.get(plk, 0) + rk
        stm[plm] = stm.get(plm, 0) + rm
    print("  void walk, first six moves (norm, door, cost):")
    print("    corpus:    %s" % moves_k)
    print("    this file: %s" % moves_m)
    ok(moves_k == moves_m, "the void walks diverge")
    # the depth-shift instrument against explore_carrier_window's
    col = M.columns[mine[(2, 2, 1)][0]].brute
    print("  Z[sqrt(-5)] ramified column over 2, brute: %s" % col)
    print("  its measured recurrence starts at a1 = %s (derived threshold"
          " %d), %d rungs confirmed"
          % (M.columns[mine[(2, 2, 1)][0]].a1,
             M.columns[mine[(2, 2, 1)][0]].derived_a0,
             M.columns[mine[(2, 2, 1)][0]].confirmed()))
    return M


# --------------------------------------------------------------- S2 the shop
def s2_shop(cap=DISC_CAP):
    section("S2  THE SHOP -- quadratic fields holding a norm-5 place beside"
            " each shape over 2")
    print("  carrier spec: a place over 5 with f = 1, i.e. 5 SPLIT or 5")
    print("  RAMIFIED -- norm 5, N - 1 = 4, so v_2 = 2 exactly.")
    print("  consumer spec: a place over 2, whose three shapes are the")
    print("  three arms. Headedness over 2 needs no third clause: mu_2")
    print("  lies in every field, so the shape test IS the criterion.")
    arms = {"A split": [], "B inert": [], "C ramified": []}
    for d in range(-cap, cap + 1):
        if d in (0, 1) or not squarefree(d):
            continue
        O = CW.QuadOrder(d)
        five = [(e, f) for (e, f, lat) in O.places(5) if f == 1]
        if not five:
            continue
        two = O.places(2)
        e2, f2 = two[0][0], two[0][1]
        if (e2, f2) == (1, 1):
            arms["A split"].append(d)
        elif (e2, f2) == (1, 2):
            arms["B inert"].append(d)
        else:
            arms["C ramified"].append(d)
    for name in sorted(arms):
        ds = arms[name]
        print("  arm %-12s %3d fields with |d| <= %d; first five: %s"
              % (name, len(ds), cap,
                 sorted(ds, key=lambda x: (abs(x), x))[:5]))
        ok(ds, "arm %s is empty inside the shop box" % name)
    return arms


# -------------------------------------------- S3 the columns and the windows
def s3_columns(arms):
    section("S3  THE COLUMNS -- the carrier's supply and the consumer's"
            " window, both brute")
    picks = []
    for name in sorted(arms):
        d = sorted(arms[name], key=lambda x: (abs(x), x))[0]
        picks.append((name, d))
    rows = []
    for (name, d) in picks:
        M = QModel(d)
        Q = [pl for pl in M.places_over(5) if pl[2] == 1][0]
        P = M.places_over(2)[0]
        colQ = M.column_of(Q)
        colP = M.column_of(P)
        kQ = v_p(M.place_norm(Q) - 1, 2)
        x, start = depth_shift(colP, 2, P[1])
        print("\n  arm %s: d = %d" % (name, d))
        print("    carrier %s norm %d, N-1 = %d, v_2 = %d, column %s"
              % (M.show(Q), M.place_norm(Q), M.place_norm(Q) - 1, kQ,
                 colQ[:5]))
        ok(kQ == 2, "the norm-5 carrier at d=%d supplies v_2 = %d, not 2"
           % (d, kQ))
        print("    consumer %s norm %d, head shape %s, column %s"
              % (M.show(P), M.place_norm(P),
                 "YES" if head_shape(2, P[1], P[2]) else "no", colP[:9]))
        print("    v_2 of that column: %s"
              % [v_p(x2, 2) for x2 in colP[:9]])
        print("    depth shift x = %s from a = %s; recurrence from a1 = %s"
              % (x, start,
                 M.columns[P].a1 if P in M.columns else "closed form"))
        print("    %-3s %6s %6s %s" % ("k", "TRUE", "filed", "verdict"))
        wins = {}
        for k in range(1, K_SHOWN + 1):
            tw = true_window(colP, 2, k)
            fw = filed_window(P[1], k)
            if tw == len(colP):
                print("    %-3d >=%4d %6d  CENSORED (off the end of the"
                      " brute)" % (k, tw, fw))
                continue
            verd = ("same" if tw == fw else
                    "WIDER +%d" % (tw - fw) if tw > fw else
                    "NARROWER %d" % (tw - fw))
            wins[k] = (tw, fw)
            print("    %-3d %6d %6d  %s" % (k, tw, fw, verd))
        rows.append((name, d, M, Q, P, wins))
    print("")
    print("  the k = 2 row is the one the carrier pays at, and it is the")
    print("  two-sided test: A must run WIDER and C NARROWER than filed.")
    got = dict((r[0], r[5].get(2)) for r in rows)
    print("  k = 2 windows (TRUE, filed): %s" % sorted(got.items()))
    ok(got["A split"][0] > got["A split"][1],
       "arm A's k=2 window is not wider than filed")
    ok(got["B inert"][0] == got["B inert"][1],
       "arm B's k=2 window departs from filed at a HEADLESS consumer")
    ok(got["C ramified"][0] < got["C ramified"][1],
       "arm C's k=2 window is not narrower than filed")
    return rows


# ------------------------------------------- S4 the planted pair and the door
def s4_planted(rows):
    section("S4  THE PLANTED PAIR -- the door on a MENU, and the ablation")
    print("  For each arm: plant the consumer at depth a and the norm-5")
    print("  carrier at depth 1, and read the consumer's door with the")
    print("  carrier and with it ABLATED. A supply that moves no door is")
    print("  not a carrier, and the depth where the step dies is the")
    print("  window read off the menu rather than off the column.")
    out = []
    for (name, d, M, Q, P, wins) in rows:
        nP = M.place_norm(P)
        print("\n  arm %s (d = %d): consumer %s norm %d, carrier %s norm %d"
              % (name, d, M.show(P), nP, M.show(Q), M.place_norm(Q)))
        print("    %-3s %8s %8s %10s %10s  %s"
              % ("a", "door-ab", "door+Q", "cost-ab", "cost+Q", "carrier?"))
        last = 0
        for a in range(1, 7):
            st = {P: a, Q: 1}
            st_ab = {P: a}
            L, L_ab = M.lam_state(st), M.lam_state(st_ab)
            d1 = M.door_r(P, a, L)
            d0 = M.door_r(P, a, L_ab)
            bearing = d1 > d0
            if bearing:
                last = a
            print("    %-3d %8d %8d %10d %10d  %s   (v_2(L) %d -> %d)"
                  % (a, d0, d1, nP ** d0, nP ** d1,
                     "LOAD-BEARING" if bearing else "dead",
                     v_p(L_ab, 2), v_p(L, 2)))
        tw, fw = wins[2]
        print("    deepest load-bearing depth: %d   TRUE window %d, filed %d"
              % (last, tw, fw))
        ok(last == tw,
           "arm %s: the menu's last load-bearing depth %d is not the"
           " column's window %d" % (name, last, tw))
        out.append((name, d, M, Q, P, last, tw, fw))
    print("")
    print("  -> the window is a MENU fact and not only a column fact at")
    print("     every arm, including the two where the filed form is wrong")
    print("     and in the two opposite directions.")
    return out


# ------------------------------------------------ S5 the walk and the limit
def s5_walk(planted):
    section("S5  THE WALK -- does a greedy walk SEAT the pair, and does the"
            " carrier move the LIMIT")
    print("  The census is the honest half: a planted state proves the")
    print("  arithmetic, a walked one proves a menu ever charges it.")
    for (name, d, M, Q, P, last, tw, fw) in planted:
        got = LB.walk_to_lock(M, {})
        if got is None:
            print("\n  arm %s (d = %d): the void walk does not lock inside"
                  " the cap" % (name, d))
        else:
            st, L, pl, cost, steps = got
            print("\n  arm %s (d = %d): void walk locks on %s at cost %d"
                  " after %d moves" % (name, d, M.show(pl), cost, steps))
        seeds = M.gen_products(BELT)
        n_states = coincid = bearing = 0
        walk_bearing = 0    # the WALK put the carrier or the consumer there
        first = None        # first load-bearing state of any kind
        first_walked = None  # first the walk MADE -- the only walk result
        walked = 0
        lock_places = {}
        for (nrm, seed) in seeds:
            got = LB.walk_to_lock(M, seed)
            if got is None:
                continue
            walked += 1
            key = (M.show(got[2]), got[3])
            lock_places[key] = lock_places.get(key, 0) + 1
            for (stt, LL, mv) in walk_trace(M, seed):
                n_states += 1
                seated = [pp for pp, a in stt.items() if a]
                Qs = [pp for pp in seated if pp[0] == 5 and pp[2] == 1]
                Ps = [pp for pp in seated if pp[0] == 2]
                if not Qs or not Ps:
                    continue
                coincid += 1
                hit = None
                for Qq in Qs:
                    st_ab = dict(stt)
                    del st_ab[Qq]
                    L_ab = M.lam_state(st_ab)
                    for Pp in Ps:
                        a = stt[Pp]
                        r1, r0 = (M.door_r(Pp, a, LL),
                                  M.door_r(Pp, a, L_ab))
                        if r1 > r0 and hit is None:
                            hit = (seed, stt, Qq, Pp, a, r0, r1)
                if hit is None:
                    continue
                bearing += 1
                if first is None:
                    first = hit
                # THE SPLIT the cubic carrier's census had to learn: a
                # state holding both places proves nothing about a WALK
                # if the SEED already held them. The test is SEATING and
                # not deepening -- a walk that only drives a seeded
                # carrier deeper did not put the pairing there, so the
                # bar is that one of the two was absent from the seed
                # entirely and the walk moved it in.
                Qq, Pp = hit[2], hit[3]
                if not seed.get(Qq, 0) or not seed.get(Pp, 0):
                    walk_bearing += 1
                    if first_walked is None:
                        first_walked = hit
        print("    belt of norm <= %d: %d seeds, %d locked, %d states"
              % (BELT, len(seeds), walked, n_states))
        print("    lock places over the belt (place, cost): %s"
              % sorted(lock_places.items(), key=lambda kv: -kv[1]))
        print("    states seating a norm-5 place BESIDE a place over 2: %d"
              % coincid)
        print("    of those, LOAD-BEARING under ablation:               %d"
              % bearing)
        print("    of those, ones the WALK made rather than the seed:   %d"
              % walk_bearing)
        ok(bearing <= coincid, "more load-bearing states than coincidences")
        ok(walk_bearing <= bearing, "more walk-made than load-bearing")
        for (tag, rec) in (("first load-bearing state", first),
                           ("first the WALK made", first_walked)):
            if rec is None:
                print("    %s: NONE" % tag)
                continue
            seed, stt, Qq, Pp, a, d0, d1 = rec
            nP = M.place_norm(Pp)
            print("    %s, from seed %s:" % (tag, M.show_st(seed)))
            print("      %s: carrier %s moves %s's door %d -> %d at depth"
                  " %d (cost %d -> %d)"
                  % (M.show_st(stt), M.show(Qq), M.show(Pp), d0, d1, a,
                     nP ** d0, nP ** d1))
    # the limit: the planted pair walked to lock, with and without
    print("\n  THE LIMIT -- the planted pair walked to lock, ablated and not.")
    print("  THE CONFOUND, named because it cannot be designed away: removing")
    print("  the carrier removes its SUPPLY and its availability as a cheap")
    print("  VEHICLE at once, and no same-norm place supplies nothing -- every")
    print("  odd norm q has q - 1 even. What separates them is WHICH place the")
    print("  carried walk locks on: if the lock vehicle is the carrier itself,")
    print("  the moved limit is at least partly the vehicle's and the reading")
    print("  is confounded; if it is some third place, the carrier changed the")
    print("  limit without being it.")
    print("  %-14s %-24s %-24s %s"
          % ("consumer", "with carrier", "ablated", "verdict"))
    moved = clean = 0
    for (name, d, M, Q, P, last, tw, fw) in planted:
        res, vehicles = [], []
        for seed in ({P: 1, Q: 1}, {P: 1}):
            got = LB.walk_to_lock(M, seed)
            vehicles.append(None if got is None else got[2])
            res.append("-" if got is None else
                       "%s at %d/move" % (M.show(got[2]), got[3]))
        verd = ""
        if res[0] != res[1]:
            moved += 1
            if vehicles[0] == Q:
                verd = "MOVED (confounded: locks ON the carrier)"
            else:
                verd = "MOVED, carrier is not the vehicle"
                clean += 1
        print("  %-14s %-24s %-24s %s" % (name, res[0], res[1], verd))
    print("  the carrier moves the limit at %d of %d consumers, and at %d of"
          " those" % (moved, len(planted), clean))
    print("  the lock vehicle is a THIRD place, which is the unconfounded"
          " reading.")
    ok(clean > 0, "every limit move is confounded by the carrier being the"
       " lock vehicle -- the limit claim has no clean instance left")
    return moved


# ---------------------------------------- S6 the sweep across completions
def s6_sweep(arms, cap=SWEEP_CAP):
    section("S6  THE SWEEP -- is the window one field's, or the shape's?")
    print("  S3 and S4 read ONE field per arm, and a place over 2 does not")
    print("  determine its completion: Q_2 has six ramified quadratic")
    print("  extensions and Q(i) is one of them. So the arm-C reading is")
    print("  one completion's until this says otherwise. Swept here: the")
    print("  k = 2 window and the depth-1 door the carrier moves, at every")
    print("  shopped field with |d| <= %d." % cap)
    print("  The DEEPEST LOAD-BEARING DEPTH is swept too, since it is what")
    print("  the headline claim is about and S4 read it at one field each.")
    print("\n  %-12s %5s  %-30s %5s %5s %6s  %s"
          % ("arm", "d", "v_2 of the column", "win", "filed", "l-b", "1 ->"))
    per_arm = {}
    for name in sorted(arms):
        for d in sorted(arms[name], key=lambda x: (abs(x), x)):
            if abs(d) > cap:
                continue
            M = QModel(d, brute_primes=(2, 5))
            P = M.places_over(2)[0]
            Q = [pl for pl in M.places_over(5) if pl[2] == 1][0]
            col = M.column_of(P)
            tw, fw = true_window(col, 2, 2), filed_window(P[1], 2)
            last, d0, d1 = 0, None, None
            for a in range(1, tw + 4):
                r1 = M.door_r(P, a, M.lam_state({P: a, Q: 1}))
                r0 = M.door_r(P, a, M.lam_state({P: a}))
                if a == 1:
                    d0, d1 = r0, r1
                if r1 > r0:
                    last = a
            per_arm.setdefault(name, []).append((d, tw, fw, d0, d1, last))
            print("  %-12s %5d  %-30s %5d %5d %6d  %d -> %d"
                  % (name, d, [v_p(x, 2) for x in col[:9]], tw, fw, last,
                     d0, d1))
    print("")
    for name in sorted(per_arm):
        rows = per_arm[name]
        wins = sorted(set(r[1] for r in rows))
        doors = sorted(set(r[4] for r in rows))
        print("  arm %-12s %2d fields: window(s) %s, depth-1 door(s) %s"
              % (name, len(rows), wins, doors))
        ok(len(wins) == 1,
           "arm %s: the k=2 window is not constant across the arm: %s"
           % (name, wins))
        for (d, tw, fw, d0, d1, last) in rows:
            ok(last == tw,
               "d=%d: deepest load-bearing depth %d is not the window %d"
               % (d, last, tw))
    cwins = set(r[1] for r in per_arm["C ramified"])
    cdoors = set(r[4] for r in per_arm["C ramified"])
    # WHICH completion, made explicit -- and the residue is NOT the
    # completion. Q_2(sqrt d) is determined by the class of d in
    # Q_2^* / (Q_2^*)^2, whose invariant is (v_2(d) mod 2, odd part mod 8):
    # squares have even valuation and a unit square is 1 mod 8. So the
    # class is FINER than d mod 8 -- d = 2 mod 8 carries odd parts 1 and 5
    # alike -- and both readings are printed rather than conflated.
    def sq_class(d):
        a, u = 0, d
        while u % 2 == 0:
            u //= 2
            a += 1
        return (a % 2, u % 8)

    by_res, by_cls = {}, {}
    for (d, tw, fw, d0, d1, last) in per_arm["C ramified"]:
        by_res.setdefault(d % 8, set()).add(d1)
        by_cls.setdefault(sq_class(d), set()).add(d1)
    print("")
    print("  the ramified door against d mod 8, and against the 2-adic")
    print("  square class (v_2 mod 2, odd part mod 8) that pins the")
    print("  completion itself:")
    for m in sorted(by_res):
        cls = sorted({sq_class(r[0]) for r in per_arm["C ramified"]
                      if r[0] % 8 == m})
        n = sum(1 for r in per_arm["C ramified"] if r[0] % 8 == m)
        print("    d = %d mod 8:  door(s) %s   (%d fields, %d completion(s)"
              " %s)" % (m, sorted(by_res[m]), n, len(cls), cls))
        ok(len(by_res[m]) == 1,
           "d = %d mod 8 gives more than one door: %s" % (m, by_res[m]))
    for c in sorted(by_cls):
        ok(len(by_cls[c]) == 1,
           "square class %s gives more than one door: %s" % (c, by_cls[c]))
    n_cls, n_res = len(by_cls), len(by_res)
    print("")
    print("    %d square classes swept against %d residues -- the residue is"
          % (n_cls, n_res))
    print("    COARSER, so the door is constant across DISTINCT completions.")
    ok(n_cls > n_res,
       "the sweep no longer separates the square class from d mod 8: "
       "%d classes, %d residues" % (n_cls, n_res))
    print("")
    print("  -> the WINDOW is the shape's and not the completion's, at")
    print("     every arm swept. The DOOR is not: arm C's window takes one")
    print("     value across %d fields and its depth-1 door takes %d --"
          % (len(per_arm["C ramified"]), len(cdoors)))
    print("     %s, set by how long the column's flat stretch runs. But it"
          % sorted(cdoors))
    print("     is fixed by d mod 8, which is coarser than the completion,")
    print("     so the door is NOT completion data either -- it is constant")
    print("     across completions the residue merges.")
    ok(len(cwins) == 1 and len(cdoors) > 1,
       "arm C no longer separates a constant window from a varying door")
    return per_arm


def main():
    print("explore_norm5_carrier.py -- paying the k = 2 supply: a norm-5"
          " carrier beside a consumer over 2")
    s1_control()               # the control runs BEFORE any verdict
    arms = s2_shop()
    rows = s3_columns(arms)
    planted = s4_planted(rows)
    s5_walk(planted)
    s6_sweep(arms)
    section("CHECKS")
    print("  %d asserted checks passed" % CHECKS)


if __name__ == "__main__":
    main()
