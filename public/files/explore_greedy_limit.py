"""explore_greedy_limit.py -- what a greedy trajectory over a function field
CONVERGES TO, coordinate by coordinate.

THE QUESTION. A minimal-move policy over the ring of a curve walks forever,
raising exponents at places; the walks never lock and never repeat, and the
set of limits they reach is known to be a continuum. What is not known is
what those limits ARE. A separation certificate (explore_undercut.py) freezes
a place's exponent whenever a cheaper door of no greater degree exists, and
its census is stark -- at a walked state almost every place the certificate
can speak about is already frozen, and nearly all the survivors have degree
1. That census is a measurement at the states the walks REACH; a limit is a
statement about infinity, and the gap between them is what this rig closes.
The suspicion it inherits is that the limit divisor has infinite exponent
only at places of DEGREE 1. That suspicion is written in the census's
vocabulary -- which places survive freezing -- and the object here is a
different one: which place the policy RETURNS TO forever. The slate below is
written in the second vocabulary, and its answer is not the suspicion's.

THE DOOR ARITHMETIC, re-derived from the engine and not remembered
(lam_pp(d, a) = lcm(2^d - 1, 2^ceil_log2(a)) with ceil_log2(1) = 0, lam_state
the lcm over seated places). Write lambda_odd = lcm(2^d - 1) over seated
degrees, kappa = max ceil_log2(e), and T = 2^kappa, the TICK. The engine's
door at a place of degree d and exponent e is

  1                       if 2^d - 1 does not divide lambda_odd   (FRESH)
  max(1, T + 1 - e)       otherwise                              (CLOCK)

and the cost is d times the door. DEGREE 1 IS NEVER FRESH -- 2^1 - 1 = 1
divides everything -- so a rational place can only ever be seated by a clock
move, which is the asymmetry the whole argument turns on.

THE HAND-ATTACK, on paper before any engine code.

 L0 THE EXPONENT CEILING. A clock move lands its core at e = T + 1 and
    ceil_log2(T + 1) = kappa + 1, so the tick DOUBLES exactly; a fresh move
    lands at e = 1 and leaves it alone. Ticks never fall, so every exponent
    ever written is 0, 1, or (the tick at its own clock) + 1, hence
    e <= T/2 + 1 at every later state. Therefore sigma = T + 1 - e >= T/2
    and EVERY place's price is at least d * T/2.
 L1 A CLOCKED RATIONAL PLACE IS PERMANENT. After a clock at P the tick is
    T' = 2T and sigma_P = T' + 1 - (T + 1) = T, so price_P = d_P * T, while
    every other place's sigma rises by T and its price by d_Q * T. If
    d_P = 1 then price_Q - price_P = price_Q(before) + (d_Q - 1) * T > 0 for
    every Q, so a rational place that is the strict minimum when clocked is
    the strict minimum at every later state. Fresh moves move no sigma and
    seat their place at e = 1 for a price of d * T >= 2T (degree 1 never
    being fresh), which is above T.
 L2 THE CLOCK'S DEGREE IS AT MOST 2. Let X be clocked at a state whose tick
    is at least 3 while some rational place is unseated. That place's price
    is T + 1 and X's is at most that, while L0 puts X's price at or above
    d_X * T/2. So d_X <= 2 + 2/T, i.e. d_X <= 2. Against a witness of degree
    d rather than 1 the same line gives d_X <= 2d, so on a ring whose least
    place degree is d_min the clock's degree is at most 2 * d_min.
 L3 THE STEADY STATE. Once a place C of degree c in {1, 2} is the permanent
    clock, its price between clocks is c * T/2, while every other place is
    unseated (price at least T + 1) or seated fresh at e = 1 (price
    d * T >= 2T). Both exceed c * T/2. So NO OTHER EXPONENT EVER MOVES
    AGAIN, and the only other move that can be minimal is a fresh open at
    the least uncovered degree D, at price D, taken while D < c * T/2.
 L4 THE LADDER IS EVERY DEGREE. 2^d - 1 carries a prime factor no smaller
    2^e - 1 carries for every d other than 1 and 6 -- BANG's theorem, the
    base-2 case of Zsigmondy, whose two exceptions are exactly those -- and
    at the one that bites, 2^6 - 1 = 3^2 * 7, a square of 3 is needed that
    no smaller 2^e - 1 supplies. So no degree is covered before it is
    opened; degree 1 is covered from the start. The
    fresh ladder is therefore 2, 3, 4, ... skipping only degrees with no
    place, one place seated per degree at exponent 1, and since the tick
    grows without bound every degree is eventually opened.

 SO THE LIMIT IS  infinity * C  +  sum over opened degrees d of  Q_d,
 with C of degree 1 or 2 and Q_d any one place of degree d. The limit set is
 then in bijection with the choice of C times one free choice per degree, so
 the continuum is a PRODUCT OVER DEGREES of place counts -- a description of
 the limit object rather than a count of it. (This line as frozen carries an
 off-by-one the run found: where C has degree 2 it was itself opened fresh,
 so it is one of the Q_d and the sum must not count it twice. F1 and F7 carry
 the corrected statement; the slate is left as it was written.)

 THE INHERITED SUSPICION IS TOO STRONG, and L2 says where it breaks: a
 degree-2 place clocked forever prices at T against an unseated rational
 place's T + 1, cheaper by exactly 1 at every state, so that branch's limit
 would carry its infinite exponent at a place of degree 2 and NO rational
 place in its support at all. Whether such a branch is reachable is for the
 run to say.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the ideal world to the element world: NOTHING. A rider raises a
    place's exponent with no clock move, which breaks L0's ceiling and with
    it every lemma above. The element world is walked and PRINTED, not
    predicted, and its slate asks a question rather than fixing an answer.
 2. From the trajectory region to anywhere else: nothing. This rig has only
    trajectories; every count it reports is over the branches it walks and
    says nothing about branches it does not.
 3. The symbolic universe against the engine's: the light walker below reads
    only (degree, exponent) and a place COUNT per degree, never a place's
    identity. That is a claim about the ideal menu, and it is CONTROLLED --
    the two menus are compared type by type at every state the engine can
    reach -- rather than assumed.

THE BLOCKER, and why it dissolves. The engine's walks stop early because the
cheapest move's degree passes a trimmed place universe, and its door search
caps the tick. Both are limits of carrying PLACES. The ideal dynamics carries
none: it needs only how many places each degree has, and those come from the
curve's own zeta numerator, fitted from the engine's counts at the degrees it
does carry and verified at the degrees the fit did not use. So the ideal
world is walked hundreds of moves deep with no place universe at all, and the
engine is kept for the control and for the element world.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE DOOR ARITHMETIC AND THE TICK. What the rig PRINTS: the number of
    moves read, over every walk of every branch -- a clock move exactly
    doubling the tick and landing its core at T + 1, a fresh move leaving
    the tick alone and landing at exponent 1.
    KILL: one move that does neither. The whole argument is arithmetic on
    these two identities.
PR2 THE LIGHT WALKER IS THE ENGINE. What the rig PRINTS: at every state of
    every engine-reachable prefix, the two menus as (degree, door, kind)
    multisets with their multiplicities, and the count of states compared.
    KILL: one disagreement, in cost or in any type's multiplicity.
PR3 THE PLACE COUNTS ARE THE ZETA'S. What the rig PRINTS: the fitted
    L-polynomial per ring, checked against the functional equation, and its
    place count against the engine's at every degree of the built universe.
    KILL: one degree where the count is wrong.
PR4 EVERY CLOCKED PLACE HAS DEGREE AT MOST 2. What the rig PRINTS: the
    census of clock moves by the degree of the place clocked, over every
    edge of the exhaustively branched stretch and over every continuation,
    per ring -- and separately the ring with no place of degree 2 or 3,
    where the census must read degree 1 alone.
    KILL: one clock move at a place of degree 3 or more.
PR5 ONE PLACE TAKES EVERY CLOCK IN THE END. What the rig PRINTS: per branch,
    the last step at which a clock move went to a place other than the final
    one, and that final place's degree.
    KILL: a branch whose clock moves never settle on a single place.
PR6 EVERY OTHER EXPONENT IS 0 OR 1. What the rig PRINTS: per branch, at the
    end of the long walk, how many places sit at each exponent and how many
    degrees have been opened -- which must be the number of places at
    exponent 1.
    KILL: one place other than the eternal clock above exponent 1.
PR7 THE ELEMENT WORLD, printed and not predicted: how many distinct places
    rise above exponent 1, and for each unit of exponent whether a move's
    own core or a RIDER put it there.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE IDEAL WORLD'S LIMIT IS NAMED (proved for the ideal world -- L0 to L4 above, an
   induction over the move model that calls on no computation; and a rule in
   range, 11 branches at six rings walked 300 moves each with every move's
   tick and exponent read). The limit divisor of a greedy trajectory is

     infinity * C  +  one place at exponent 1 at each opened degree,

   ONE place C carrying an unbounded exponent while EVERY OTHER SEATED PLACE
   STANDS AT EXPONENT 1 FOREVER. C is itself one of the opened degrees'
   places exactly when its degree is 2; a rational C is seated by a clock and
   never appears among them, which is the whole of the off-by-one in F7. Every branch ends at a profile of one place
   above exponent 1 and 290 at exponent 1, the degrees having opened in
   order, one place each, with no exponent between. That answers the
   question one level down: a sprawling world's limit is not merely
   determined almost everywhere, it is WRITTEN DOWN -- a single deep
   coordinate over a flat support that grows forever.

F2 THE CLOCK'S DEGREE IS 1 OR 2, AND THE DEGREE-2 BRANCH IS REACHABLE
   (proved for the ideal world -- L2; rule in range, 0 of 140 censused clock
   moves at degree 3 or more over six rings, counted per EDGE of the
   exhaustively branched stretch so that state merging cannot hide one). The
   suspicion this rig inherited -- infinite exponent only at places of
   degree 1 -- is REFUTED, and by a margin of exactly 1 (0 of the 140 clock
   moves the census covers went to a place of degree 3 or more; the control's
   own 30 are driven by the engine and counted apart): a degree-2 place
   clocked forever prices at T against an unseated rational place's T + 1 at
   every state, so it wins by one unit and never yields. Five of the six
   rings reach that branch (all but h5), and its limit carries its infinite
   coordinate at a place of DEGREE 2 with NO rational place in its support
   at all. The true race is not degree against staleness but 2 * d_min: the
   clock's degree is at most twice the least degree the ring has a place at.
   (Since generalised: 2 * d_min is the corner b = 2, alpha = 1 of a formula
   over the pricing schedule, d_min * (b/(b-1))^(1/alpha), and the bound is
   ATTAINED by a trajectory exactly where the void menu ties -- which at
   these six rings needs the least fresh-eligible degree to be precisely
   twice the least born-covered one -- explore_price_schedule.py)

F3 THE ONE-BRANCH RING IS THE ONE WITH NO PLACE OF DEGREE 2 (rule in range,
   six rings, IDEAL world -- the branching is the light walker's and the
   element world is not walked far enough to have a branch count). h5 has four rational places and no place of degree 2 or 3,
   and it is the only ring whose walk has a single branch and whose clock
   census reads degree 1 alone. The alternative attractor is missing for
   GEOGRAPHY, not arithmetic -- the degree that could hold it is empty. And
   the price comparison that refuses a deeper clock is measured rather than
   argued: planting a stale place of degree 3 or 4 with a rational witness
   present, the menu refuses it at every ring; removing degrees 1 and 2 from
   the universe, the SAME state makes it minimal at cost 96 or 128. So the
   refusal is the WITNESS's doing, and a ring with no low-degree place would
   host a deeper clock.
   (Since sharpened, and "GEOGRAPHY, not arithmetic" is the wrong contrast:
   the empty degree is what makes h5's least fresh-eligible degree 4, and the
   single branch is then the plain inequality 4 * 1 > 1 * 2 between the two
   VOID-menu bids. The same one line gives the branch count at every ring,
   so h5 obeys the rule rather than escaping it -- explore_price_schedule.py)

F4 THE IDEAL CONTINUUM IS A PRODUCT OVER DEGREES (a derivation on F1, with
   the factors computed and every opening's WIDTH asserted to be the
   degree's whole unseated population, which is what the product multiplies; the element world reads a class at every
   opening as well, so this is not its description). The choice at each opening is which place of that degree to
   seat, and it is FREE and PERMANENT -- nothing later in the dynamics reads
   a place's identity, which is why the light walker can carry no places at
   all and still be the engine (S1b). So the limit set is (the choice of C)
   times a product over degrees of place counts, and the first ten openings
   alone already offer 1.8e11 ways at F_2[x], 3.7e11 at h2, 4.7e13 at h4,
   3.2e13 at g2, 6.8e13 at h3 and 2.3e16 at h5. The cardinality result said
   the greedy image is a continuum; this says its points are CHOICE
   FUNCTIONS ON DEGREES, one place picked per degree with the deep
   coordinate chosen at the first clock.

F5 THE CLOCK SETTLES AT ITS FIRST MOVE, with no transient (rule in range,
   11 branches, IDEAL world -- L1 is what binds, and the rider voids it). In every branch the last clock move that went anywhere but
   the final place IS the first clock move. So which place carries the
   infinite exponent is decided by the trajectory's FIRST clock and never
   revisited -- L1 binds from the beginning rather than after a settling
   period, which is why the limit has no memory of the walk beyond that one
   choice.

F6 THE ELEMENT WORLD BREAKS THE CEILING, AND THE RIDER IS WHY -- printed,
   not predicted (observation, five rings, walks of 18 to 21 moves cut by
   the trimmed universe). Within twenty moves h4 and h5 carry TWO places
   above exponent 1 and g2 carries THREE, and the extra ones are built
   ENTIRELY by riders -- g2's two shallow rational places stand at exponents
   2 and 6 with not one unit from a move's own core. So L0's exponent
   ceiling fails exactly where transplant flag 1 said it would, and with it
   every lemma above. THE IDEAL WORLD'S SINGLE DEEP COORDINATE IS A PROPERTY
   OF A WORLD WITH NO CLASSES. Two of the five rings still show a single
   deep place at the depth reached (h2, h3), and h3's is of degree 2.
   (Since closed, and the capitalised sentence is too strong: a world WITH
   classes has a single deep coordinate whenever the eternal clock's class
   generates no rider, which is h3 exactly -- what a class buys is at most
   the clock's own class orbit, and h2's and h4's second deep place is a
   transient the clock strands rather than a coordinate it feeds
   -- explore_element_limit.py)

F7 WHAT IS STILL OPEN, and it is one question. Do the element world's
   rider-built places grow WITHOUT BOUND, or stall? The mechanism is a race
   of rates: a clock doubles one exponent per clock move while riders add
   one unit per fresh open to whichever rational place the opened core's
   class summons, and there are of order T/2 fresh opens between doublings.
   Linear against exponential says the riders lose in the end; the same
   count against a fixed number of rational places says each of them
   receives a positive fraction, and a rider-fed place gets CHEAPER while
   the clock's price doubles. The walks here are cut at twenty moves and
   cannot separate the two. (Since answered, and the premise in this
   paragraph is what was wrong: riders do NOT add one unit per fresh open,
   because greedy takes a PRINCIPAL core wherever the degree has one and
   pays no rider at all. The surviving flow is one clock move's rider per
   era against an era that doubles, so the rate is constant and not linear;
   whether the fed places are nonetheless unbounded is still open
   -- explore_element_limit.py; SETTLED SINCE by explore_rider_recursion.py:
   they are unbounded, and how many is decided by the increment recursion
   on (T mod h, r mod h) -- a cell inside its cycle is fed forever, one
   only in the pre-period stops at a computable exponent) The refinement PR6's arithmetic needed is filed
   here too: "the places at exponent 1 are the opened degrees" holds where
   the clock is rational and is one short where the clock was itself opened
   fresh, the seated places being the opened degrees plus one exactly when
   the clock has degree 1.

THE DESIGN, in five sections after the control.

 S1 THE POSITIVE CONTROL, run before any census is read.
    (a) THE PLACE COUNTS (PR3): the zeta numerator fitted from the first 2g
        power sums by Newton's identities, checked against the functional
        equation, and its place counts read against the engine's at every
        degree of the built universe.
    (b) THE LIGHT WALKER AGAINST THE ENGINE (PR2): menus compared type by
        type at every state of the engine's own canonical walk in the ideal
        world, at every ring. The walker is advanced by the ENGINE's move,
        so no tie-break convention can make the two paths agree by
        construction.
    (c) THE PRICE COMPARISON ON PLANTED STATES: a state where a place of
        degree 3 or more is stale and a rational place is fresh from its own
        clock -- the walker's menu must REFUSE the deep clock. Then the same
        state with the low degrees removed from the universe, where it must
        FIRE, or the control tests the state rather than the witness.
 S2 THE LONG WALK, ideal world, carrying the COVERAGE RULE (L4) and the
    canonical rule's own obligation with it:
    at every state of every continuation the exact big-integer divisibility
    test, over every degree the menu prices, is read against the rule that
    the covered degrees are the opened ones and 1 -- a degree covered without
    being opened would refute L4 and is not assumed away. every distinct state reachable by any tie
    choice over the first stretch, then each continued canonically to the
    full length, with the tick, the opened degrees, the settling step and
    the exponent profile printed per branch (PR1, PR5, PR6).
 S3 THE CLOCK CENSUS (PR4): every clock move by the degree of the place
    clocked -- over every EDGE of the branched stretch, so that a branch
    merged away by state deduplication cannot hide one, and over every
    continuation.
 S4 THE LIMIT'S SHAPE (PR6) and its MULTIPLICITY: at the end of each branch,
    the support by exponent, and the free choices the trajectory has made --
    one per opened degree, as many ways as that degree has places.
 S5 THE ELEMENT WORLD (PR7): the engine walked from the void at a raised
    universe, every exponent increment attributed to the core of its move or
    to the rider its class summoned.

Run: `python explore_greedy_limit.py`. RUN RECORD (513489 checks, ~34 s, peak
43.7 MB, of which about 33 s is the element section's place universe). S1
control: the zeta numerator fitted from the first 2g power sums at each ring
-- 1 at the rational function field, 1 - t + 2t^2, 1 + 2t^2, 1 + t + 2t^2 and
1 + 2t + 2t^2 at the four elliptic rings, 1 + 2t + 4t^2 + 4t^3 + 4t^4 at the
genus-2 one -- each satisfying its functional equation and reproducing the
engine's place count at all 12 built degrees, 8 to 12 of which the fit never
used; the light menu equal to the engine's in cost, type and multiplicity at
91 states over six rings, every walk advanced by the ENGINE's move and every
one of the six ended by the trimmed universe rather than by the walk length;
and a stale place of degree 3 or 4 refused at all six rings with a rational
witness present and MINIMAL at the same state with degrees 1 and 2 taken out
of the universe. S2: 11 branches, 3360 moves read in the walk phase -- 140 clock
moves each doubling the tick exactly and landing at T + 1, 3220 fresh moves
each leaving the tick alone and landing at exponent 1, the control's own 91
moves counted apart in the tally the run prints -- reaching ticks of 512 and 1024
with 290 or 291 degrees opened, every branch settling on its clock at that
clock's first move -- a place's identity being (degree, slot), and every move
checked against a snapshot taken at its own entry, so that no existing slot is
displaced or lowered and exactly the intended one changes, since the settling
claim reads identity off exactly that -- and two rules asserted at every state of every
continuation -- no degree covered before it is opened, and every tie type
NOT taken still minimal at the successor, so the canonical convention is
verified to pick an ORDER and never an outcome, which is what entitles the
shapes below to be read off one continuation. S3: the clock census
reads degree 1 and degree 2 only, at every ring and in both regions, 0 of the
140 censused at degree 3 or above; h5 reads degree 1 alone. S4: exactly one place above
exponent 1 in every branch of every ring. S5: the element world at a universe
of degree 16, walks of 18 to 21 moves -- one place above exponent 1 at h2 and
h3, two at h4 and h5, three at g2, with 1 to 14 rider units placed and g2's
two shallow rational places built from riders alone. Slate PR1-PR7: PR1, PR2,
PR3, PR4, PR5 and PR7 hit; PR6's kill missed and its arithmetic clause is
refined by one in the branch whose clock was opened fresh (F7). REFUTED at
the run: the inherited suspicion that the infinite exponent sits only at
places of degree 1 (F2).

THE HARNESS, forced to fail rather than trusted. A door off by one makes the
light menu disagree with the engine's at the first state; a place count off
by one is caught at degree 1 of the first ring; a planted degree-3 clock
trips the census bound; a move that inserts into its row instead of editing
in place trips the slot check; an opened degree left out of the opened list
trips the coverage rule; an opening width off by one trips the width check; a
tie member the convention cannot preserve trips the reordering check; and a
second place above exponent 1 trips the limit shape. All seven fired. The slot check's FIRST
form did not, and that is worth recording: it asserted an open lands at the
row's last index, which is trivially true here because every open lands on an
empty row -- a condition that cannot fail is not a check, and only forcing it
showed the difference. Its scope is corruption within a move, which is the
only kind this rig can produce, `apply` being the sole writer of the state.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_greedy_image_ec as EC        # the genus 0 and 1 rings
import explore_greedy_image_g2 as G2        # the genus 2 ring
import explore_coarse_type as CT            # the ladder, the states
import explore_reordering as RO             # the menus in both worlds

CHECKS = 0

DEG_CAP = 600        # the light walker's own universe bound, asserted against
WALK_N = 300         # moves per light walk, the branched stretch included
BRANCH_N = 12        # moves over which every tie choice is followed
BRANCH_CAP = 32      # distinct states carried through the branched stretch
ENGINE_N = 60        # moves of the engine walk the control compares against
ELEM_DMAX = 16       # the place universe the element section builds
ELEM_N = 60          # moves attempted in the element world
TRUNC = {"branch-cap": 0, "engine-short": 0, "element-short": 0}
# moves are counted PER PHASE, because only the walk phase's clock moves are
# the ones S3 censuses and asserts a degree bound on -- the control's walks
# are driven by the engine and are not part of that claim
MOVES = {"control-clock": 0, "control-fresh": 0, "walk-clock": 0,
         "walk-fresh": 0}
PHASE = ["control"]
UNIV = {}


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ----------------------------------------------------- the symbolic universe
def power_sums(R, dmax):
    """a_n = 2^n - N_n for n = 1..dmax, where N_n counts the points of the
    affine curve over the field of 2^n elements -- read off the engine's own
    places, N_n being the sum of d * (places of degree d) over d dividing n."""
    a = [0] * (dmax + 1)
    for n in range(1, dmax + 1):
        N = 0
        for d in range(1, n + 1):
            if n % d == 0:
                N += d * len(R.by_deg.get(d, []))
        a[n] = (1 << n) - N
    return a


def fit_L(a, g):
    """The L-polynomial coefficients of L(t) = prod(1 - alpha_i t) from the
    first 2g power sums, by Newton's identities: for n <= 2g,
    a_n = -sum_{i<n} c_i a_{n-i} - n c_n. Exact integer division, or the fit
    is not a curve's."""
    c = [1] + [0] * (2 * g)
    for n in range(1, 2 * g + 1):
        s = a[n] + sum(c[i] * a[n - i] for i in range(1, n))
        ok(s % n == 0, "the Newton fit left a fraction at n = %d" % n)
        c[n] = -s // n
    return c


def extend_sums(a, c, g, dmax):
    """a_n = -sum_{i=1..2g} c_i a_{n-i} for n > 2g."""
    out = list(a[:2 * g + 1]) + [0] * (dmax - 2 * g)
    for n in range(2 * g + 1, dmax + 1):
        out[n] = -sum(c[i] * out[n - i] for i in range(1, 2 * g + 1))
    return out


def counts_from_sums(a, dmax):
    """The place count per degree, by Moebius inversion of N_n = 2^n - a_n."""
    N = [0] + [(1 << n) - a[n] for n in range(1, dmax + 1)]
    npl = [0] * (dmax + 2)
    for d in range(1, dmax + 1):
        s = 0
        for e in range(1, d + 1):
            if d % e == 0:
                s += EC.mobius(e) * N[d // e]
        ok(s % d == 0, "the Moebius inversion left a fraction at degree %d" % d)
        npl[d] = s // d
        ok(npl[d] >= 0, "a negative place count at degree %d" % d)
    return npl


def universe(L, dmax=DEG_CAP):
    """(L-polynomial, place count per degree, power sums, degrees built) --
    the ring's place universe from its own zeta numerator."""
    if L.name not in UNIV:
        built = max(d for d in L.R.by_deg if L.R.by_deg[d])
        a = power_sums(L.R, built)
        c = fit_L(a, L.g)
        UNIV[L.name] = (c, counts_from_sums(extend_sums(a, c, L.g, dmax),
                                            dmax), a, built)
    return UNIV[L.name]


# ------------------------------------------------------- the light walker
class Light(object):
    """A state of the ideal dynamics carrying no places: seat[d] is the list
    of exponents of the seated places of degree d, and npl[d] how many places
    that degree has. The menu is a function of these alone, which S1(b)
    certifies against the engine rather than assuming. A place's identity is
    (degree, slot) -- its index in seat[d], which never moves."""

    def __init__(self, npl, tag):
        self.npl = npl
        self.tag = tag
        self.seat = {}          # degree -> exponents, all >= 1
        self.opened = []        # degrees opened by a fresh move, in order
        self.lam_odd = 1
        self.cov = set([1])     # degrees whose factor lambda_odd carries
        self.T = 1
        self.step = 0
        self.clocks = []        # (step, degree, slot) of every clock move

    def copy(self):
        s = Light(self.npl, self.tag)
        s.seat = dict((d, list(v)) for d, v in self.seat.items())
        s.opened = list(self.opened)
        s.lam_odd = self.lam_odd
        s.cov = set(self.cov)
        s.T = self.T
        s.step = self.step
        s.clocks = list(self.clocks)
        return s

    def covered(self, d):
        """Exact, and memoised only in the direction that cannot go stale:
        lambda_odd never falls, so a covered degree stays covered."""
        if d in self.cov:
            return True
        if self.lam_odd % ((1 << d) - 1) == 0:
            self.cov.add(d)
            return True
        return False

    def door(self, d, e):
        if not self.covered(d):
            return 1
        return max(1, self.T + 1 - e)

    def menu(self):
        """(cost, {(degree, door, kind): multiplicity}) -- the ideal menu,
        grouped by what a move DOES. KIND is 'open' for a place seated from
        exponent 0 and 'move' for one already seated."""
        best, ties = None, {}
        d = 0
        while best is None or d < best:
            d += 1
            ok(d <= DEG_CAP,
               "%s: the light menu reached degree %d, past its universe"
               % (self.tag, d))
            if self.npl[d] == 0:
                continue
            row = self.seat.get(d, ())
            cands = []
            if self.npl[d] > len(row):
                r = self.door(d, 0)
                cands.append((d * r, r, "open", self.npl[d] - len(row)))
            for e in row:
                r = self.door(d, e)
                cands.append((d * r, r, "move", 1))
            for cost, r, kind, n in cands:
                if best is not None and cost > best:
                    continue
                if best is None or cost < best:
                    best, ties = cost, {}
                key = (d, r, kind)
                ties[key] = ties.get(key, 0) + n
        return best, ties

    def apply(self, key):
        """Seat the move of type (degree, door, kind). PR1 is checked here,
        so that every move of every branch is read and not only the walks a
        section chooses to follow."""
        d, r, kind = key
        Tb = self.T
        # F5 identifies a place as (degree, slot), so a slot must never move.
        # Checking that inside the append would be tautological -- every open
        # here lands on an empty row, so any insert position is also the last
        # one. The check that can FAIL is across the move: every slot that
        # existed must still exist with an exponent no lower, and exactly one
        # entry may change. Snapshot first.
        was = len(self.seat.get(d, ()))
        before = dict(((dd, i), e)
                      for dd, v in self.seat.items() for i, e in enumerate(v))
        if kind == "open":
            row = self.seat.setdefault(d, [])
            row.append(r)
            slot = len(row) - 1
            if not self.covered(d):
                self.opened.append(d)
                self.lam_odd = EC.lcm(self.lam_odd, (1 << d) - 1)
                self.cov.add(d)
        else:
            row = self.seat[d]
            slot = next(i for i, e in enumerate(row) if self.door(d, e) == r)
            row[slot] += r
            ok(len(row) == was,
               "%s: a move at degree %d changed the population"
               % (self.tag, d))
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
        self.T = 1 << max(EC.ceil_log2(e) for v in self.seat.values()
                          for e in v)
        if self.T > Tb:
            ok(self.T == 2 * Tb, "%s: a clock move took the tick %d to %d"
               % (self.tag, Tb, self.T))
            ok(e2 == Tb + 1, "%s: a clock move landed at %d, not %d"
               % (self.tag, e2, Tb + 1))
            self.clocks.append((self.step, d, slot))
            MOVES[PHASE[0] + "-clock"] += 1
        else:
            ok(e2 == r == 1, "%s: a tickless move at door %d landed at %d"
               % (self.tag, r, e2))
            MOVES[PHASE[0] + "-fresh"] += 1
        self.step += 1
        return d, kind, Tb, self.T


def profile(s):
    """How many places sit at each exponent."""
    out = {}
    for row in s.seat.values():
        for e in row:
            out[e] = out.get(e, 0) + 1
    return out


def coverage_rule(s):
    """L4: the covered degrees are the opened ones together with 1. Read
    against the walker's own exact divisibility test, which is what `cov`
    holds after a menu has priced every degree up to the cost."""
    return s.cov == set([1]) | set(s.opened)


# ------------------------------------------------------------- S1 control
def s1a_counts(ladder):
    """PR3: the fitted zeta numerator and its place counts against the
    engine's own, over the whole built universe."""
    print("  ring     g   L-polynomial coefficients   degrees built  "
          "beyond the fit")
    for L in ladder:
        c, npl, a, built = universe(L)
        for i in range(L.g + 1):
            ok(c[2 * L.g - i] == (1 << (L.g - i)) * c[i],
               "%s: the functional equation fails at coefficient %d"
               % (L.name, i))
        for d in range(1, built + 1):
            ok(npl[d] == len(L.R.by_deg.get(d, [])),
               "%s: degree %d has %d places, the zeta numerator says %d"
               % (L.name, d, len(L.R.by_deg.get(d, [])), npl[d]))
        ok(built > 2 * L.g,
           "%s: the fit used every degree it was checked on" % L.name)
        print("  %-8s %-3d %-27s %-14d %d"
              % (L.name, L.g, c[1:] if L.g else "1 (the rational function "
                 "field)", built, built - 2 * L.g))


def eng_menu_types(R, st, ties):
    """The engine's tie set as the same (degree, door, kind) multiset the
    light menu reports."""
    out = {}
    for veh in ties:
        ok(len(veh) == 1,
           "%s: an ideal vehicle carrying %d places" % (R.name, len(veh)))
        pl, r = list(veh.items())[0]
        key = (R.deg[pl], r, "open" if st.get(pl, 0) == 0 else "move")
        out[key] = out.get(key, 0) + 1
    return out


def s1b_walker(ladder):
    """PR2: the light menu against the engine's, state by state, with the
    light state advanced by the ENGINE's own move."""
    print("  ring     states compared  menu entries  engine walk ended by")
    tot = 0
    for L in ladder:
        _, npl, _, _ = universe(L)
        s, st, n, nt = Light(npl, L.name), {}, 0, 0
        why = "the walk length"
        for _ in range(ENGINE_N):
            try:
                lam, cost, ties = RO.menu_of(L, "ideal", st)
            except AssertionError:
                why = "the trimmed universe"
                TRUNC["engine-short"] += 1
                break
            lcost, lties = s.menu()
            ok(lcost == cost, "%s: light cost %d against engine cost %d"
               % (L.name, lcost, cost))
            ets = eng_menu_types(L.R, st, ties)
            ok(lties == ets, "%s: light menu %s against engine menu %s"
               % (L.name, sorted(lties.items()), sorted(ets.items())))
            ok(1 << EC.v2(lam) == s.T, "%s: light tick %d against engine %d"
               % (L.name, s.T, 1 << EC.v2(lam)))
            n += 1
            nt += len(lties)
            pl, r = list(ties[0].items())[0]
            s.apply((L.R.deg[pl], r,
                     "open" if st.get(pl, 0) == 0 else "move"))
            st = EC.apply_veh(st, ties[0])
        ok(n >= 6, "%s: only %d states compared" % (L.name, n))
        tot += n
        print("  %-8s %-16d %-13d %s" % (L.name, n, nt, why))
    print("  TOTAL    %d states, every cost, type and multiplicity equal"
          % tot)


def plant(npl, T, deep_d, cap):
    """A state at tick T with every degree up to `cap` that has a place
    seated at exponent 1, and the place of degree `deep_d` clocked to the top
    of the range -- the one place whose door is T/2 rather than T."""
    s = Light(npl, "planted")
    for d in range(1, cap + 1):
        if npl[d]:
            s.seat[d] = [T // 2 + 1 if d == deep_d else 1]
            s.opened.append(d)
            s.lam_odd = EC.lcm(s.lam_odd, (1 << d) - 1)
            s.cov.add(d)
    s.T = 1 << max(EC.ceil_log2(e) for v in s.seat.values() for e in v)
    ok(s.T == T, "the planted state's tick is %d, not %d" % (s.T, T))
    return s


def s1c_detector(ladder):
    """The refusal of a deep clock must be the RATIONAL WITNESS's doing and
    not the state's, so the same state is run with the low degrees taken out
    of the universe, where the deep clock must become minimal."""
    T, cap = 64, 200
    print("  ring     deep degree  with the low degrees  without them")
    for L in ladder:
        _, npl, _, _ = universe(L)
        cut = list(npl)
        for d in (1, 2):
            cut[d] = 0
        deep = min(d for d in range(3, DEG_CAP) if cut[d])
        _, ties = plant(npl, T, deep, cap).menu()
        held = [k for k in ties if k[0] == deep and k[2] == "move"]
        ok(not held, "%s: the deep clock at degree %d was minimal with a "
           "witness present" % (L.name, deep))
        cost2, ties2 = plant(cut, T, deep, cap).menu()
        fired = [k for k in ties2 if k[0] == deep and k[2] == "move"]
        ok(fired, "%s: the deep clock at degree %d was not minimal even with "
           "the witness removed, so the control tests the state" % (L.name,
                                                                    deep))
        print("  %-8s %-12d %-21s %s"
              % (L.name, deep, "refused", "minimal at cost %d" % cost2))


# ---------------------------------------------------------- the long walk
def key_of(s):
    return (tuple(sorted((d, tuple(v)) for d, v in s.seat.items())), s.T)


def branches(L, npl, census):
    """Every distinct state reachable by any tie choice over the first
    stretch. Every EDGE's clock degree enters the census before the states
    are deduplicated, so a branch merged away cannot hide one."""
    root = Light(npl, L.name)
    live = {key_of(root): root}
    for _ in range(BRANCH_N):
        nxt = {}
        for s in live.values():
            _, ties = s.menu()
            for key in sorted(ties):
                s2 = s.copy()
                d, kind, Tb, Ta = s2.apply(key)
                if Ta > Tb:
                    census[(L.name, "branched", d)] = \
                        census.get((L.name, "branched", d), 0) + 1
                nxt.setdefault(key_of(s2), s2)
        if len(nxt) > BRANCH_CAP:
            TRUNC["branch-cap"] += 1
            nxt = dict(sorted(nxt.items())[:BRANCH_CAP])
        live = nxt
    return [live[k] for k in sorted(live)]


def continue_walk(L, s, n, census):
    """The canonical continuation: the least (degree, door, kind) among the
    minimal moves. Ties between a fresh open and a clock are REORDERINGS --
    both moves are taken, in one order or the other -- so the convention
    picks an order and not an outcome, which is CHECKED at every such step
    below rather than left as a claim about the dynamics."""
    for _ in range(n):
        _, ties = s.menu()
        # F4's product is over the tie WIDTH at each opening, so the width
        # must be the degree's whole unseated population and not merely some
        # of it -- asserted here rather than read off the menu's construction
        for (dd, r, kind), mult in ties.items():
            if kind == "open" and r == 1:
                ok(mult == s.npl[dd] - len(s.seat.get(dd, ())),
                   "%s: a fresh opening at degree %d offers %d places, the "
                   "degree has %d unseated"
                   % (L.name, dd, mult, s.npl[dd] - len(s.seat.get(dd, ()))))
        # the convention takes the least (degree, door, kind); it may only
        # pick an ORDER, so where the tie holds more than one type the others
        # must still be minimal at the successor -- checked, not asserted in
        # prose, since every shape below is read off this one continuation
        taken = sorted(ties)[0]
        rest = [k for k in ties if k != taken]
        d, kind, Tb, Ta = s.apply(taken)
        if rest:
            _, nxt = s.menu()
            for k in rest:
                dd, rr, kk = k
                want = (dd, s.door(dd, 0) if kk == "open" else rr, kk)
                ok(want in nxt,
                   "%s: the tie member %s was dropped by taking %s, so the "
                   "canonical rule picked an outcome and not an order"
                   % (L.name, k, taken))
        ok(coverage_rule(s), "%s: a degree is covered without being opened"
           % L.name)
        if Ta > Tb:
            census[(L.name, "tail", d)] = census.get((L.name, "tail", d), 0) + 1
    return s


def settling(s):
    """(the last step at which a clock went elsewhere, the final clock's
    place). PR5 reads both."""
    ok(bool(s.clocks), "a walk with no clock move at all")
    last = (s.clocks[-1][1], s.clocks[-1][2])
    step = None
    for st, d, slot in s.clocks:
        if (d, slot) != last:
            step = st
    return step, last


# ------------------------------------------------------- the element world
def s5_element(ladder):
    """PR7: the element world walked with the engine, every exponent
    increment attributed to its move's core or to the rider."""
    print("  ring     moves  rider units  places above e=1  "
          "what raised them")
    for L in ladder:
        if L.R.h == 1:
            continue
        st, n, riders, src = {}, 0, 0, {}
        for _ in range(ELEM_N):
            try:
                lam, cost, ties = RO.menu_of(L, "element", st)
            except AssertionError:
                TRUNC["element-short"] += 1
                break
            veh = ties[0]
            _, core = CT.offset_of(L, "element", st, veh, lam)
            ok(core is not None,
               "%s: a minimal vehicle with no readable core" % L.name)
            for pl, e in veh.items():
                row = src.setdefault(pl, [0, 0])
                row[0 if pl == core else 1] += e
                if pl != core:
                    riders += e
            st = EC.apply_veh(st, veh)
            n += 1
        deep = sorted((L.R.deg[pl], st[pl], src[pl]) for pl in st
                      if st[pl] > 1)
        print("  %-8s %-6d %-12d %-17d %s"
              % (L.name, n, riders, len(deep),
                 "; ".join("degree %d at e=%d (core %d, rider %d)"
                           % (d, e, v[0], v[1]) for d, e, v in deep) or "--"))


def main():
    ladder = CT.build_ladder()

    section("S1  THE POSITIVE CONTROL")
    print("(a) THE PLACE COUNTS FROM THE ZETA NUMERATOR")
    s1a_counts(ladder)
    print("\n(b) THE LIGHT WALKER AGAINST THE ENGINE")
    s1b_walker(ladder)
    print("\n(c) THE DEEP CLOCK REFUSED, AND THE SAME STATE WITHOUT ITS")
    print("    WITNESS, WHERE IT MUST FIRE")
    s1c_detector(ladder)

    section("S2  THE LONG WALK")
    print("  Every tie choice followed for %d moves, each distinct state"
          % BRANCH_N)
    print("  then continued canonically to %d moves in all." % WALK_N)
    print("\n  ring     branches  tick     opened  clock degree  settles at"
          "  exponent profile")
    census, shapes = {}, {}
    PHASE[0] = "walk"
    for L in ladder:
        _, npl, _, _ = universe(L)
        rows = []
        for s in branches(L, npl, census):
            s = continue_walk(L, s, WALK_N - BRANCH_N, census)
            step, last = settling(s)
            rows.append((s, step, last))
        shapes[L.name] = rows
        for s, step, last in rows:
            print("  %-8s %-9d %-8d %-7d %-13d %-11s %s"
                  % (L.name, len(rows), s.T, len(s.opened), last[0],
                     "step %d" % step if step is not None
                     else "its first clock",
                     dict(sorted(profile(s).items()))))

    PHASE[0] = "control"

    section("S3  THE CLOCK CENSUS")
    print("  Every clock move by the degree of the place clocked -- the race")
    print("  between the tick and the staleness a cheaper place can hold.")
    print("  BRANCHED counts every edge of the exhaustive stretch, before")
    print("  states are merged; TAIL counts the canonical continuations.")
    print("\n  ring     region     clock moves by place degree")
    censused = 0
    for L in ladder:
        for region in ("branched", "tail"):
            row = [(d, n) for (nm, rg, d), n in sorted(census.items())
                   if nm == L.name and rg == region]
            print("  %-8s %-10s %s"
                  % (L.name, region,
                     ", ".join("degree %d: %d" % r for r in row) or "none"))
            for d, n in row:
                censused += n
                ok(d <= 2, "%s: a clock move at a place of degree %d"
                   % (L.name, d))

    print("\n  %d clock moves censused, every one at degree 1 or 2. The"
          % censused)
    print("  control's own walks (S1b) are driven by the ENGINE and are")
    print("  counted apart, in the move tally below -- they are not part")
    print("  of this claim.")

    section("S4  THE LIMIT'S SHAPE")
    print("  At the end of each branch: the support by exponent, and the")
    print("  free choices made -- one per opened degree, as many ways as")
    print("  that degree has places.")
    print("  ABOVE E=1 is over every branch; the columns after it are the")
    print("  FIRST branch's, the others being printed per branch in S2.")
    print("\n  ring     branches  above e=1  at e=1  opened  "
          "ways over the first 10 openings")
    for L in ladder:
        _, npl, _, _ = universe(L)
        rows, above = shapes[L.name], set()
        for s, step, last in rows:
            pr = profile(s)
            deep = sum(n for e, n in pr.items() if e > 1)
            above.add(deep)
            ok(deep == 1, "%s: %d places above exponent 1" % (L.name, deep))
            # every seated place was either opened FRESH or seated by a clock
            # move from exponent 0, and only degree 1 can be the second
            seated = sum(len(v) for v in s.seat.values())
            ok(seated == len(s.opened) + (1 if last[0] == 1 else 0),
               "%s: %d places seated against %d degrees opened and a clock of "
               "degree %d" % (L.name, seated, len(s.opened), last[0]))
            ok(pr.get(1, 0) == seated - 1,
               "%s: %d places at exponent 1 with %d seated"
               % (L.name, pr.get(1, 0), seated))
        s = rows[0][0]
        ways = 1
        for d in s.opened[:10]:
            ways *= npl[d]
        print("  %-8s %-9d %-10s %-6d %-7d %d"
              % (L.name, len(rows), sorted(above), profile(s).get(1, 0),
                 len(s.opened), ways))

    section("S5  THE ELEMENT WORLD")
    print("  The engine at a place universe of degree %d, walked from the"
          % ELEM_DMAX)
    print("  void. A rider raises an exponent with NO clock move, which is")
    print("  what the ideal argument has no room for.")
    EC.DMAX = G2.DMAX = ELEM_DMAX
    s5_element(CT.build_ladder())

    section("SUMMARY")
    print("  %d checks passed." % CHECKS)
    print("  moves read: %s" % MOVES)
    print("  truncation: %s" % TRUNC)


if __name__ == "__main__":
    main()
