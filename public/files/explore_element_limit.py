"""explore_element_limit.py -- what a greedy trajectory converges to when the
ring HAS CLASSES, where the ideal argument has no room for the rider.

THE QUESTION. Over a ring whose class group is trivial the limit of a greedy
trajectory is known: one place carrying an unbounded exponent, every other
seated place standing at exponent 1 forever, and the support growing without
end (explore_greedy_limit.py). Every step of that argument rests on an
EXPONENT CEILING -- no exponent is ever written except 0, 1, or the tick at
its own clock plus 1 -- and the ceiling holds because the only way to raise
an exponent is to pay for it. Where the class group is non-trivial that
fails. A minimal vehicle is a core P^r times the minimal representative of
the class it must cancel, so a move at one place RAISES THE EXPONENT AT
ANOTHER for free: the RIDER. The ceiling has no defence against it, and with
the ceiling every clause of the limit goes. This rig asks what the limit is
in the world that actually has classes.

THE DOOR ARITHMETIC, re-derived from the engine and not remembered.
`door_r(pl, e, lam)` is the least r with `lam_pp(d, e+r)` not dividing the
state's lambda, and `lam_pp(d, a) = lcm(2^d - 1, 2^ceil_log2(a))`. Writing
lambda_odd for the lcm of 2^d - 1 over seated degrees and T = 2^kappa for the
tick, that unfolds to

  1                       if 2^d - 1 does not divide lambda_odd   (FRESH)
  max(1, T + 1 - e)       otherwise                              (CLOCK)

-- the SAME door as the ideal world. The element world changes the VEHICLE,
never the door: the cost of a move at a place of degree d and class c with
increment r is

  d * r  +  deg minrep(-(r*c))

and the engine offers r0 + j for j = 0 .. g, a longer core sometimes buying a
cheaper completion. DEGREE 1 IS STILL NEVER FRESH, 2^1 - 1 dividing
everything.

THE HAND-ATTACK, on paper before any engine code.

 E0 GREEDY PREFERS A PRINCIPAL CORE. A fresh open at an uncovered degree d
    takes r = 1, so its vehicle is P * minrep(-c) at cost d + deg minrep(-c).
    A place of class 0 costs d and every other place of that degree costs
    strictly more. So the minimal fresh open at a degree takes a PRINCIPAL
    core whenever the degree has an unseated one, and summons NO RIDER.
    This is where the handover's arithmetic breaks: it assumed the opened
    cores' classes equidistribute, and greedy is what makes them not.
 E1 SO THE FRESH RIDER FLOW DRIES UP. A degree's places spread over the h
    classes and their number grows like 2^d/d, so past a small degree every
    class is populated, principal cores are always available, and no fresh
    open ever pays a rider again. Whether the small degrees are small is a
    COUNT, and the count is what S1(a) computes.
 E2 WHAT SURVIVES IS THE CLOCK'S OWN RIDER. A clock move at C with increment
    r carries class r * cls(C) and needs a rider unless that vanishes. There
    is about one clock move per doubling, so the surviving rider rate is O(1)
    per era -- LOGARITHMIC in the tick, not linear. If the eternal clock's
    place is itself principal, no rider is ever summoned again at all.
 E3 THE TWO RACES, with the ideal steady state as the ONLY thing borrowed and
    borrowed as a HYPOTHESIS (the era length is measured at S3, not imported).
    A clock of degree c prices at c*T/2 between clocks; opens run while the
    degree is below that price, so the cumulative opened degree is about
    c*T/2 and era k's own opens number about c*T_k/4. A rational place at
    exponent e prices at T + 1 - e, so it undercuts the clock when
    e > T*(1 - c/2).
      c = 2 needs only e >= 2. ANY rational place at exponent 2 or more takes
      a degree-2 clock, and the rider is what puts one there.
      c = 1 needs e > T/2. Under the handover's linear intake a rational place
      reaches about c*T/(2h), short by the factor h; under E1's dried-up flow
      it reaches only about log T. Either way the degree-1 clock holds.
    So the prediction is that the element clock ENDS AT DEGREE 1 at every
    ring, the degree-2 branch the ideal world proves permanent being a
    TRANSIENT here -- and the two worlds then differ on the limit's headline
    and not merely on its depth.
 E4 AND THE LIMIT GAINS COORDINATES. Riders never stop entirely while the
    eternal clock's class is non-zero, so the places its riders feed grow
    without bound too, at a logarithmic rate. The ideal world's ONE deep
    place would become one deep place plus up to h - 1 slowly deepening
    rational ones. Which is the printed question at S4.

THE CLASS-REFINED PLACE COUNTS, exactly and with no curve. The walker below
needs how many places each (degree, class) cell has, to degrees in the
hundreds, and the engine cannot supply them -- its place universe costs 2^d.
They come instead from the ring's own zeta data in the GROUP RING Z[G],
G = Pic^0(F_2). Over the PROJECTIVE curve, with cls(P) = [P - deg(P)*infinity]
which is exactly what the engine's own class map is,

  B(t) = prod_P (1 - [cls P] t^deg P)^-1 = sum_n b_n t^n,

b_n being the class-refined count of effective divisors of degree n. Riemann-
Roch makes every class of degree n >= 2g - 1 hold exactly 2^(n+1-g) - 1 of
them, so b_n = (2^(n+1-g) - 1) * N there, with N the norm element sum_c [c];
the finitely many b_n below that come from enumerating effective divisors over
places of degree at most 2g - 2. Hence B is a RATIONAL function known exactly,

  B(t) * (1 - t)(1 - 2t) = Q(t),  deg Q <= 2g + 1,

with no fit and no free parameter, and t B'/B = t Q'/Q + t/(1-t) + 2t/(1-2t)
gives

  c_n = u_n + (1 + 2^n)*[0],   n q_n = sum_{i<=n} q_i u_{n-i},
  c_n = sum_{d | n} d * a_d^(n/d),   a_d = sum_{deg P = d} [cls P],

a_d^(m) being a_d pushed forward by multiplication-by-m on G. So

  n * a_n = c_n - sum_{d | n, d < n} d * a_d^(n/d),

an exact integer recursion whose division by n must come out whole. The affine
counts are the projective ones less the single rational place at infinity,
which every ring here has exactly one of and which carries class 0. For genus
1 the construction has NO low-degree input at all, so all six rings' counts
are PREDICTIONS checked against the engine rather than fits.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the ideal world (explore_greedy_limit.py L0-L4): the DOOR only, and
    re-derived above rather than adapted. L0's exponent ceiling is exactly
    what the rider breaks, so L1 to L4 are void here and none is used. Where
    the ideal steady state is needed for a RATE (E3) it enters as a named
    hypothesis and the rate it predicts is measured against S3's own count.
 2. From the handover's slate: its equidistribution assumption is REJECTED by
    E0 before any code, and its era length is measured, never imported.
 3. The light walker's cell abstraction -- that the element menu is a function
    of (degree, class, exponent) and a place count per cell -- is a CLAIM
    about the menu, controlled at S1(b) against the engine, not assumed.
 4. From ring to ring: nothing. h = 1 is walked as the degenerate control
    where the element world IS the ideal world.
 5. From the branches walked to all branches: NOTHING. Every tie choice is
    followed only over the first stretch and only up to a cap, and past that
    stretch every walk is canonical -- so a column read "over all branches"
    means over the branches CARRIED, and the rig prints which rings hit the
    cap. No count here is a statement about all trajectories.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PE1 THE CLASS-REFINED COUNTS ARE THE GROUP RING'S. What the rig PRINTS: per
    ring, Q's coefficients, and the count per (degree, class) against the
    engine's own census at every built degree, with how many of those degrees
    the construction's inputs did not use.
    KILL: one degree and class where the count is wrong.
PE2 THE LIGHT WALKER IS THE ENGINE. What the rig PRINTS: at every state of
    the engine's own element walk, the two menus as (degree, class, kind,
    exponent, increment) multisets with multiplicities, the cost, and the
    number of states compared.
    KILL: one disagreement, in cost or in any type's multiplicity.
PE3 A FRESH OPEN TAKES A PRINCIPAL CORE (E0). What the rig PRINTS: per ring,
    the class of every opened core over the whole walk, and the last step at
    which a fresh open summoned a rider.
    KILL: a fresh open paying a rider while an unseated principal place of
    its degree exists.
PE4 EVERY DEGREE PAST A SMALL ONE HAS A PRINCIPAL PLACE (E1). What the rig
    PRINTS: per ring, every degree in range with no place of class 0, and the
    least class-0 count over the degrees above the last of them.
    KILL: a degree above the stated bound with no principal place.
PE5 THE RIDER RATE IS LOGARITHMIC, NOT LINEAR (E2). What the rig PRINTS: per
    ring and per era, the fresh opens, the rider units placed, and which kind
    of move placed them.
    KILL: rider units per era growing with the era's length.
PE6 A DEGREE-2 CLOCK DOES NOT HOLD AGAINST A RATIONAL PLACE AT EXPONENT 2
    (E3). What the rig PRINTS: per ring, every tick doubling with the place
    that crossed, its degree and class, whether a core or a rider carried it
    across, and the deepest rational exponent standing at the time.
    KILL: a doubling taken by a degree-2 place while some rational place
    stands at exponent 2 or more.
PE7 A DEGREE-1 CLOCK IS PERMANENT HERE TOO. What the rig PRINTS: per ring and
    branch, the last doubling that went anywhere but the final place, and the
    final place's degree and class.
    KILL: a place of degree 1 taking a doubling and later losing one.
PE8 THE ERA LENGTH, printed and not predicted: opens between doublings
    against the clock's price at the era, which is what E3 borrowed as a
    hypothesis.
PE9 THE LIMIT'S SHAPE, printed and not predicted: at the end of each walk,
    how many places stand above exponent 1, their degree and class, and every
    unit attributed to a core or to a rider.

FINDINGS (tiers below; run record at the bottom; every section asserts).

FE1 THE CLASS-REFINED PLACE COUNTS COME OUT OF THE GROUP RING, WITH NO CURVE
    AND NO FIT (rule in range -- six rings, every (degree, class) cell at
    every built degree, 10 to 12 of them beyond any input the construction
    used). The count of places of degree d in ideal class c is a Riemann-Roch
    identity in Z[Pic^0], not a search: B(t)(1-t)(1-2t) is a polynomial of
    degree 0 at the rational function field, 2 at each elliptic ring and 4 at
    the genus-2 one, and the four elliptic rings and F_2[x] need NO
    low-degree input at all -- their cell counts are predictions the engine
    then confirms. This is what makes an element-world walker light: the
    engine's place universe costs 2^d and stops at degree 16, and the cells
    are exact to degree 1200.

FE2 GREEDY WILL NOT PAY A RIDER IT CAN AVOID, SO THE FRESH RIDER FLOW DRIES
    UP (proved -- E0, the vehicle at an uncovered degree costing d for a
    principal core and d + deg minrep otherwise; and a rule in range, 286 to
    291 of each walk's ~291 opens taking a principal core, every exception
    lying at one of the finitely many degrees with no principal place). Those
    degrees are read off the cell counts and there are at most six of them
    per ring -- [1, 4] at h2, [1, 3, 4] at h3, [1, 2, 3, 4] at h4,
    [1, 2, 3, 5] at h5, [1, 2, 3, 4, 5, 7] at g2, none at F_2[x] -- and above
    the last of them every degree to 1200 has at least two principal places.
    So a fresh open summons a rider only in a bounded initial stretch, ending
    by step 9 of 300 at every ring. THE HANDOVER'S ARITHMETIC RESTED ON THE
    OPPOSITE, that the opened cores' classes equidistribute; they do not, and
    greedy is what makes them not.

FE3 THE RIDER RATE IS CONSTANT PER ERA WHILE THE ERA LENGTH DOUBLES (rule in
    range, six rings, 10 or 11 eras each). The opens per era double away --
    1, 0, 0, 2, 4, 8, 16, 32, 64, 128 at F_2[x] and h2, and the same shape at
    every other ring -- while the rider units placed in an era never exceed
    SIX anywhere and never grow with the era. The peak is g2's fifth era, and
    it is a peak because four of its six units come from OPENS, which is the
    dying transient; from the sixth era on every ring places 0, 1 or 2 units
    per era and every one of them comes from a DEEPENING move. After the initial stretch the ONLY rider source is the clock's own
    move, one per era by construction, so the total rider intake after k
    doublings is O(k) -- LOGARITHMIC in the tick against a clock that
    doubles. The race the handover set up as linear against exponential is
    not linear; it is constant against exponential, and the loser loses by
    more than was thought.

FE4 THE ERA LENGTH IS THE IDEAL WORLD'S, MEASURED AND NOT IMPORTED (rule in
    range). A clock of degree c at tick T opens about c*T/4 degrees before
    the next doubling: h2 reads 128 opens at tick 512 with a degree-1 clock
    and h3 reads 128 at tick 256 with a degree-2 one, both exactly c*T/4.
    Transplant flag 1 said nothing carries from the ideal world; this one
    does, and it is the one clause the hand-attack needed.

FE5 THE DEGREE-2 CLOCK SURVIVES THE ELEMENT WORLD -- and the prediction that
    it would not is REFUTED by its own sibling clause (rule in range: h3's
    clock is a place of degree 2 and class 0 in both branches, holding all
    nine doublings over 300 moves on both branches its sweep enumerated, with
    no rational place ever above exponent 1). The undercut mechanism is real and is PLANTED to prove it: at a tick
    of 32 a degree-2 clock prices at 32 at the four rings whose minimal
    representatives are single points and 34 at g2, while a rational place at
    exponent 3 prices at 30 everywhere and takes the menu alone -- and the
    same place at exponent 1 prices at the clock's own figure or above,
    leaving the clock on the menu. What never arrives is the
    antecedent. A rational place reaches exponent 2 only by rider, and at h3
    the clock is PRINCIPAL, so its own moves summon no rider and the flow
    that would feed one has already dried up. The two worlds therefore
    AGREE on the limit's headline at h3 -- a degree-2 deep place with no
    rational place in its support at all -- and the ideal world's
    proof of it, though void as an argument here, was not wrong as a verdict.

FE6 THE DEEP COORDINATES ARE THE CLOCK AND ITS CLASS ORBIT (proved for the
    steady state -- after the last non-principal open the only move that is
    not an open is the clock's, so the only cells a rider can reach are those
    of the minimal representatives the clock's class summons; and a rule in
    range, asserted at every branch carried, together with the clock's having
    changed hands INSIDE the transient or not at all -- the premise that no
    move but the clock's deepens anything is not assumed either, it is what
    the same assertion reads off `grew`, whose every entry is a RIDER unit).
    Write gamma for the
    clock's class. Every place other than the clock that deepens after the
    window lies in the orbit {minrep(-m*gamma)}, and gains its units as a
    RIDER, never as a core. So the element limit is

      infinity * C  +  at most the orbit's places, each gaining about one
                       unit an era
                    +  one place at exponent 1 at each opened degree,

    and its STEADY STATE collapses to the ideal world's shape exactly when
    the orbit is empty or is the clock itself. Both happen: gamma = 0 at h3
    and F_2[x] kills the rider outright, and an orbit of order 2 sends every
    rider back to the clock at h2 and h4, whose clocks take 4 and 9 rider
    units on their own coordinate and give none away after the window. The
    COUNT of deep places is a different statement and is read over branches,
    because the transient can strand one before the clock settles: h2 and h4
    read ONE deep place on some branches and TWO on others while their steady
    state is single-coordinate on all of them. Where gamma has larger order
    the limit gains coordinates on every branch carried -- h5 ends with three
    places above exponent 1 on all twelve (a clock at 513 and two rational
    places at 6 and 3, both built from riders alone) and g2 with three to
    five. h5 and g2 are the two rings whose sweep hit the cap, so those two
    are the ones whose branch sets are incomplete (flag 5). E4's
    further clause -- that those coordinates grow WITHOUT BOUND -- is NOT
    settled here and should not be read out of the shape: the rate is about
    one unit an era at the depth walked, and h2 is the standing warning that
    a rider income can simply stop, its clock's own having ceased the moment
    the parity of its increment locked.

FE7 A DEGREE-1 CLOCK IS NOT PERMANENT, AND THE COUNTEREXAMPLE IS A RIDER
    TAKING THE CLOCK (PE7's kill fired; observation, one ring). At g2 the
    rational place of class 2 carries the first THREE doublings and carries
    them as a RIDER, not as a core -- the literal thing the handover asked
    about -- and then loses the clock to the rational place of class 1 at
    step 4, which holds the remaining seven. So the ideal world's permanence
    lemma fails here as stated. What survives is the windowed form, asserted
    at every branch: the clock changes hands inside the TRANSIENT -- at or
    before the last open that summoned a rider, which is measured and not
    read off the settling step -- or not at all.

FE8 THE CANONICAL CONTINUATION PICKS AN OUTCOME HERE, NOT ONLY AN ORDER
    (observation, six rings, the first 40 steps of each branch, the declined
    move compared by its VEHICLE -- which cells it raises and by how much --
    and not by its delta, since a delta carries the from-exponent and would
    score a move as lost merely because the state moved under it; measuring
    it the robust way leaves every figure below unchanged, so the losses are
    real and not relabelling). A declined minimal type re-priced at the
    successor of the taken one is still minimal at 6 of 6, 7 of 8, 6 of 6,
    12 of 12 and 32 of 32 types over the first five rings -- and at only 46
    of 85 at g2. The ideal world's reordering lemma, which is what entitles a
    shape to be read off one continuation, does not hold in the element
    world, which is why every column of S2 is reported over ALL branches.

THE DESIGN, in four sections after the control.

 S1 THE POSITIVE CONTROL, run before any census is read.
    (a) THE CELL COUNTS (PE1): the group-ring construction above, its counts
        read against the engine's own class census at every built degree.
    (b) THE LIGHT WALKER AGAINST THE ENGINE (PE2): menus compared type by
        type at every state of the engine's element walk, at every ring, the
        walker advanced by the ENGINE's move so that no tie-break convention
        can make the two agree by construction.
    (c) THE UNDERCUT, PLANTED (E3's mechanism as a detector): a state with a
        degree-2 place clocked and a rational place at exponent 2, where the
        menu must prefer the rational place; and the same state with that
        rational place at exponent 1, where it must NOT.
 S2 THE LONG WALK, every tie choice followed over a first stretch and each
    distinct state continued canonically, with the tick, the opened degrees,
    the doublings and the rider ledger printed per branch.
 S3 THE ERA LEDGER (PE5, PE8): per era, its length in opens, the clock's
    price, and the rider units placed with the kind of move that placed them.
 S4 THE LIMIT'S SHAPE (PE6, PE7, PE9): the doublings by degree and class, the
    settling step, and the support above exponent 1 with every unit
    attributed.

Run: `python explore_element_limit.py`. RUN RECORD (1534551 checks, ~16 s,
peak 28.9 MB). S1 control: the group-ring construction reproducing the
engine's own class census at all 12 built degrees of all six rings, with Q of
degree 0, 2, 2, 2, 2 and 4 and no low-degree input at all below genus 2; the
light menu equal to the engine's in cost and in every type's multiplicity at
90 states over six rings, 127 types and 1864 vehicles read, every walk ended
by the trimmed universe rather than by the walk length; and the planted
undercut firing at exponent 3 and refusing to fire at exponent 1 at the five
rings with a place of degree 2. S2: 300 moves per branch, 2 to 12 branches
per ring with 39 states dropped at the two rings that hit the cap (h5, g2),
10308 moves read -- ticks of 512 and 1024 with 291 to 295 places
seated and 9 or 10 doublings, the final clock reading (1, 0) or (2, 0) at
F_2[x], (1, 1) at h2 and h4, (2, 0) at h3, one of three rational places at h5
and one of two at g2. S3: the era ledger, opens doubling to 128 per era against rider units
peaking at 6 in g2's fifth era and running 0, 1 or 2 from the sixth on. S4: the orbit law and the
windowed permanence asserted at every branch of every ring, the window
opening by step 9 of 300. Slate PE1-PE9: PE1 to PE5 hit; PE8 and PE9 carry no
kill and simply printed; PE6's kill missed for want of its antecedent (FE5);
PE7's kill FIRED (FE7). REFUTED at the run: the hand-attack's headline that the element clock
ends at degree 1 at every ring (E3), and the handover's premise that the
opened cores' classes equidistribute (FE2). LEFT UNSETTLED: E4's clause that
the rider-fed coordinates grow without bound (FE6).

THE HARNESS, forced to fail rather than trusted -- each of the following was
MADE to fail in a scratch run, not argued. A cell count off by one is caught
at degree 3 of the first ring; a door off by one makes the light menu
disagree with the engine's at the first state; a rider cell holding two
places trips the singleton check; two cells aliasing one exponent list -- the
corruption-within-a-move this rig can actually produce, `apply` being the
sole writer -- trips the containment check; an exponent lifted past twice the
tick trips the tick check; a deep place attributed to the wrong clock trips
the orbit law; a non-principal open with a principal place unseated trips E0;
and a clock changing hands after the transient trips the permanence check.
All eight fired.

Three near-misses are worth the record, because each is a check that looked
like one and was not. Reading the menu by (core, increment) rather than by
what the move DOES makes the light menu offer two types where the engine
offers one vehicle -- that is how the type came to be the DIVISOR, a delta
having two readings the divisor cannot tell apart. The orbit law's first two
forms could not fail: stated over the whole history it is refuted at h2,
where the transient strands a degree-2 place before the clock settles, and
stated over every unit it is refuted everywhere, because seating a place is
a unit too; only the third form -- units that DEEPEN an already-seated place,
inside a window that waits for the last non-principal open -- is the law that
is true. And the permanence check's first form was a TAUTOLOGY: it asked
whether any doubling after the settling step went elsewhere, when settling()
is defined as the last step at which one did. It is replaced by the claim
that has content, namely that the settling step lies inside the transient,
whose end is measured independently as the last open that summoned a rider.
The orbit containment stays vacuous at four of the six rings, where nothing
outside the clock deepens at all; the rig PRINTS how many pairs it ranged
over so that is visible, and the emptiness those rings turn on is asserted
in its own right.
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

DEG_CAP = 1200       # the light walker's own universe bound, asserted against
WALK_N = 300         # moves per light walk, the branched stretch included
BRANCH_N = 8         # moves over which every tie choice is followed
BRANCH_CAP = 12      # distinct states carried through the branched stretch
ENGINE_DMAX = 12     # the place universe the engine control builds
ENGINE_N = 40        # moves of the engine walk the control compares against
REJOIN_N = 40        # steps over which the declined tie types are re-priced
TRUNC = {"branch-cap": 0, "engine-short": 0}
MOVES = {"control": 0, "walk": 0}
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


# ------------------------------------------------------------- the group ring
class GRing(object):
    """Z[G] for the ring's class group, as integer vectors of length h."""

    def __init__(self, addc, negc):
        self.addc, self.negc = addc, negc
        self.h = len(negc)
        self._scale = {}

    def zero(self):
        return [0] * self.h

    def one(self):
        v = [0] * self.h
        v[0] = 1
        return v

    def norm(self):
        return [1] * self.h

    def add(self, x, y):
        return [a + b for a, b in zip(x, y)]

    def smul(self, k, x):
        return [k * a for a in x]

    def mul(self, x, y):
        out = [0] * self.h
        for i, a in enumerate(x):
            if not a:
                continue
            row = self.addc[i]
            for j, b in enumerate(y):
                if b:
                    out[row[j]] += a * b
        return out

    def scale(self, c, m):
        """m * c in G, written additively."""
        key = (c, m % self.h)
        if key not in self._scale:
            acc, k = 0, m % self.h
            for _ in range(k):
                acc = self.addc[acc][c]
            self._scale[key] = acc
        return self._scale[key]

    def push(self, x, m):
        """x pushed forward by multiplication-by-m on G."""
        out = [0] * self.h
        for c, a in enumerate(x):
            if a:
                out[self.scale(c, m)] += a
        return out


def poly_mul(GR, A, B):
    out = [GR.zero() for _ in range(len(A) + len(B) - 1)]
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            out[i + j] = GR.add(out[i + j], GR.mul(a, b))
    return out


def eff_by_class(GR, places, n):
    """The class-refined count of effective divisors of degree exactly n over
    the given (degree, class) places -- the low-degree input to B."""
    out = GR.zero()

    def rec(i, dg, cl):
        if dg == n:
            out[cl] += 1
            return
        for j in range(i, len(places)):
            d, c = places[j]
            e, tot, acc = 1, dg + d, GR.addc[cl][c]
            while tot <= n:
                rec(j + 1, tot, acc)
                e += 1
                tot += d
                acc = GR.addc[acc][c]

    rec(0, 0, 0)
    return out


def cell_universe(L, dmax=DEG_CAP):
    """(Q, npl) -- the class-refined AFFINE place count per degree, exact,
    from the ring's zeta data in the group ring. npl[d][c] is how many places
    of degree d lie in class c."""
    if L.name in UNIV:
        return UNIV[L.name]
    R, g = L.R, L.g
    GR = GRing(R.addc, R.negc)
    n0 = max(0, 2 * g - 1)
    # the projective places of low degree: the affine ones plus the single
    # rational place at infinity, which carries class 0 at every ring here
    low = [(1, 0)]
    for d in range(1, max(1, 2 * g - 2) + 1):
        if d <= 2 * g - 2:
            for pl in R.by_deg.get(d, []):
                low.append((d, R.cls[pl]))
    P = [eff_by_class(GR, low, n) for n in range(n0)]
    if not P:
        P = [GR.zero()]                      # the zero polynomial, for g = 0
    den = [GR.one(), GR.smul(-3, GR.one()), GR.smul(2, GR.one())]
    Q = poly_mul(GR, P, den)
    # t^n0 * (2^(n0+1-g) * (1 - t) - (1 - 2t)) * N
    tail = [GR.zero() for _ in range(n0 + 2)]
    k = 1 << (n0 + 1 - g)
    tail[n0] = GR.smul(k - 1, GR.norm())
    tail[n0 + 1] = GR.smul(2 - k, GR.norm())
    while len(Q) < len(tail):
        Q.append(GR.zero())
    for i, v in enumerate(tail):
        Q[i] = GR.add(Q[i], v)
    while len(Q) > 1 and Q[-1] == GR.zero():
        Q.pop()
    ok(Q[0] == GR.one(), "%s: Q has constant term %s, not the identity"
       % (L.name, Q[0]))
    ok(len(Q) - 1 <= 2 * g + 1, "%s: Q has degree %d, past 2g + 1"
       % (L.name, len(Q) - 1))
    # u_n from n q_n = sum_{i <= n} q_i u_{n-i}
    u = [GR.zero()]
    for n in range(1, dmax + 1):
        acc = GR.smul(n, Q[n]) if n < len(Q) else GR.zero()
        for i in range(1, min(n, len(Q) - 1) + 1):
            acc = GR.add(acc, GR.smul(-1, GR.mul(Q[i], u[n - i])))
        u.append(acc)
    # c_n = u_n + (1 + 2^n)[0], then the divisor recursion for a_n
    a = [GR.zero()]
    for n in range(1, dmax + 1):
        c = list(u[n])
        c[0] += 1 + (1 << n)
        for d in range(1, n):
            if n % d == 0:
                c = GR.add(c, GR.smul(-d, GR.push(a[d], n // d)))
        ok(all(x % n == 0 for x in c),
           "%s: the class recursion left a fraction at degree %d" % (L.name, n))
        a.append([x // n for x in c])
    npl = {}
    for d in range(1, dmax + 1):
        v = list(a[d])
        if d == 1:
            v[0] -= 1                        # the place at infinity is not affine
        ok(all(x >= 0 for x in v),
           "%s: a negative place count at degree %d: %s" % (L.name, d, v))
        npl[d] = v
    UNIV[L.name] = (Q, npl)
    return UNIV[L.name]


def engine_cells(R, d):
    """The engine's own class census at a degree."""
    v = [0] * R.h
    for pl in R.by_deg.get(d, []):
        v[R.cls[pl]] += 1
    return v


# --------------------------------------------------------- the light walker
class ELight(object):
    """A state of the ELEMENT dynamics carrying no places, only CELLS: a cell
    is a (degree, class) pair, seat[cell] is the list of exponents of the
    seated places in it, and npl[d][c] is how many places the cell has. A
    place's identity is (cell, slot), its index in seat[cell], which never
    moves. Every place supporting a minimal representative is the unique
    place of its cell, which is asserted at build time, so a rider's target
    is a cell and the walker can name it."""

    def __init__(self, npl, GR, rep, repdeg, g, tag):
        self.npl, self.GR, self.rep, self.repdeg = npl, GR, rep, repdeg
        self.g, self.tag, self.h = g, tag, GR.h
        self.seat = {}          # (degree, class) -> exponents, all >= 1
        self.opened = []        # (step, degree, class, kind) per first seating
        self.lam_odd = 1
        self.cov = set([1])
        self.T = 1
        self.step = 0
        self.src = {}           # (cell, slot) -> [core units, rider units]
        self.doubles = []       # (step, cell, slot, carrier, deepest rational)
        # per era: opens, rider units from an open, rider units from a
        # deepening move, moves
        self.eras = [[0, 0, 0, 0]]
        self.core = {}          # delta -> its canonical (degree, class, e, r)
        self.ambig = 0          # deltas with more than one reading
        self.units = []         # (step, cell, slot, "core"/"rider", n, before)
        self.open_riders = []   # steps at which an OPEN summoned a rider
        self.impure = []        # (step, degree, class) per non-principal open

    def copy(self):
        s = ELight(self.npl, self.GR, self.rep, self.repdeg, self.g, self.tag)
        s.seat = dict((k, list(v)) for k, v in self.seat.items())
        s.opened = list(self.opened)
        s.lam_odd, s.cov, s.T, s.step = self.lam_odd, set(self.cov), self.T, self.step
        s.src = dict((k, list(v)) for k, v in self.src.items())
        s.doubles = list(self.doubles)
        s.eras = [list(e) for e in self.eras]
        s.core, s.ambig, s.units = dict(self.core), self.ambig, list(self.units)
        s.open_riders = list(self.open_riders)
        s.impure = list(self.impure)
        return s

    def covered(self, d):
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

    def cost(self, d, c, r):
        return d * r + self.repdeg[self.GR.negc[self.GR.scale(c, r)]]

    def free(self, d, c):
        return self.npl[d][c] - len(self.seat.get((d, c), ()))

    def delta_of(self, d, c, e, r):
        """What the move DOES: the exponent of every cell it touches, before
        and after. The core cell takes r units and every cell of the summoned
        minimal representative takes its own, MERGING with the core when the
        representative lands on the core's own cell. This -- and not the
        (core, increment) reading -- is the type, because two readings can
        produce one divisor and the engine offers it once."""
        cell = (d, c)
        seen = {cell: [e, e + r]}
        for cell2, ex in self.rep[self.GR.negc[self.GR.scale(c, r)]].items():
            if cell2 in seen:
                seen[cell2][1] += ex
            else:
                e2 = self.seat.get(cell2, (0,))[0] if self.seat.get(cell2) \
                    else 0
                seen[cell2] = [e2, e2 + ex]
        return tuple(sorted((k, v[0], v[1]) for k, v in seen.items()))

    def ways(self, delta):
        """How many vehicles wear this type: a free choice of place at every
        component, the components lying in distinct cells."""
        n = 1
        for cell, e0, _e1 in delta:
            if e0 == 0:
                n *= self.free(cell[0], cell[1])
            else:
                n *= self.seat.get(cell, []).count(e0)
        return n

    def menu(self):
        """(cost, {delta: multiplicity}) -- the element menu as what each
        minimal move does. A vehicle's cost is at least its core's degree, so
        the degree loop may stop at the best cost found."""
        best, ties, core = None, {}, {}
        d = 0
        while best is None or d < best:
            d += 1
            ok(d <= DEG_CAP, "%s: the light menu reached degree %d, past its "
               "universe" % (self.tag, d))
            if d > len(self.npl) or sum(self.npl[d]) == 0:
                continue
            cands = []
            r0 = self.door(d, 0)
            for c in range(self.h):
                if self.free(d, c) > 0:
                    for j in range(self.g + 1):
                        cands.append((c, 0, r0 + j))
            for (dd, c), row in self.seat.items():
                if dd != d:
                    continue
                for e in sorted(set(row)):
                    re = self.door(d, e)
                    for j in range(self.g + 1):
                        cands.append((c, e, re + j))
            # SORTED, because `apply` reads a delta's core off the FIRST
            # reading that produces it and a delta can have two. Unsorted the
            # opens all precede the moves and the row iterates a set, so the
            # attribution would depend on insertion order rather than on the
            # rule the docstring states.
            cands.sort()
            for c, e, r in cands:
                cost = self.cost(d, c, r)
                if best is not None and cost > best:
                    continue
                if best is None or cost < best:
                    best, ties, core = cost, {}, {}
                key = self.delta_of(d, c, e, r)
                if key not in ties:
                    ties[key] = self.ways(key)
                    core[key] = (d, c, e, r)
                else:
                    self.ambig += 1
        self.core = core
        return best, ties

    def apply(self, key):
        """Seat the move of type `key`, the delta above. Attribution reads the
        core off the CANONICAL reading -- the least (degree, class, exponent,
        increment) producing this delta -- because a delta can have two
        readings and the divisor cannot tell them apart."""
        Tb = self.T
        before = dict(((k, i), x)
                      for k, v in self.seat.items() for i, x in enumerate(v))
        d, c, e, r = self.core[key]
        # E0 as an assertion and not a story: a principal core at this degree
        # would cost d against this vehicle's d + deg minrep, so a
        # non-principal open can only be minimal where no principal place of
        # the degree is left unseated. FE2 reads the exceptions off this.
        if e == 0 and c != 0:
            ok(self.free(d, 0) == 0,
               "%s: a non-principal open at degree %d with %d principal "
               "places unseated" % (self.tag, d, self.free(d, 0)))
            self.impure.append((self.step, d, c))
        cell, core_slot = (d, c), None
        touched, rid_units = set(), 0
        rat_before = max([x for (dd, _c), v in self.seat.items() if dd == 1
                          for x in v] or [0])
        for cell2, e0, e1 in key:
            row = self.seat.setdefault(cell2, [])
            if e0 == 0:
                ok(self.free(cell2[0], cell2[1]) > 0,
                   "%s: a component at cell %s with no unseated place"
                   % (self.tag, cell2))
                row.append(0)
                slot = len(row) - 1
            else:
                slot = next(i for i, x in enumerate(row) if x == e0)
            row[slot] += e1 - e0
            src = self.src.setdefault((cell2, slot), [0, 0])
            if cell2 == cell:
                core_slot = slot
                src[0] += r
                src[1] += e1 - e0 - r
                rid_units += e1 - e0 - r
                self.units.append((self.step, cell2, slot, "core", r, e0))
                if e1 - e0 - r:
                    self.units.append((self.step, cell2, slot, "rider",
                                       e1 - e0 - r, e0 + r))
            else:
                src[1] += e1 - e0
                rid_units += e1 - e0
                self.units.append((self.step, cell2, slot, "rider", e1 - e0,
                                   e0))
            touched.add((cell2, slot))
        after = dict(((k, i), x)
                     for k, v in self.seat.items() for i, x in enumerate(v))
        ok(all(k in after and after[k] >= x for k, x in before.items()),
           "%s: a move at cell %s displaced or lowered an existing slot"
           % (self.tag, cell))
        ok(set(k for k, x in before.items() if after.get(k) != x) <= touched,
           "%s: a move at cell %s changed a slot outside its vehicle"
           % (self.tag, cell))
        newly = [k for k in after if k not in before]
        for (cl2, _s) in newly:
            self.lam_odd = EC.lcm(self.lam_odd, (1 << cl2[0]) - 1)
            self.opened.append((self.step, cl2[0], cl2[1],
                                "open" if cl2 == cell else "rider"))
        kind = "open" if e == 0 else "move"
        self.T = 1 << max(EC.ceil_log2(x) for v in self.seat.values() for x in v)
        ok(self.T in (Tb, 2 * Tb), "%s: the tick went from %d to %d"
           % (self.tag, Tb, self.T))
        era = self.eras[-1]
        era[3] += 1
        if kind == "open":
            era[0] += 1
            era[1] += rid_units
            if rid_units:
                self.open_riders.append(self.step)
        else:
            era[2] += rid_units
        if self.T > Tb:
            crossed = sorted(((after[k], k) for k in after
                              if after[k] > Tb and before.get(k, 0) <= Tb),
                             reverse=True)
            ok(crossed, "%s: the tick doubled with no slot crossing it"
               % self.tag)
            _x, (ccell, cslot) = crossed[0]
            carrier = "core" if (ccell, cslot) == (cell, core_slot) else "rider"
            self.doubles.append((self.step, ccell, cslot, carrier, rat_before,
                                 len(crossed)))
            self.eras.append([0, 0, 0, 0])
        MOVES[PHASE[0]] += 1
        self.step += 1
        return kind, rid_units


def deep_places(s):
    """(degree, class, exponent, core units, rider units) above exponent 1."""
    out = []
    for cell, row in s.seat.items():
        for i, e in enumerate(row):
            if e > 1:
                sr = s.src.get((cell, i), [0, 0])
                out.append((cell[0], cell[1], e, sr[0], sr[1]))
    return sorted(out)


def settling(s):
    """(the last doubling that went anywhere but the final place, the final
    place) -- the element world's reading of where the clock lands."""
    if not s.doubles:
        return None, None
    last = (s.doubles[-1][1], s.doubles[-1][2])
    step = None
    for rec in s.doubles:
        if (rec[1], rec[2]) != last:
            step = rec[0]
    return step, last


# ---------------------------------------------------------------- the rings
def light_of(L, tag):
    """A walker for the ring, with the minimal representatives read off the
    engine as CELLS and every one of their places asserted to be alone in
    its cell -- which is what lets a walker with no places name a rider."""
    R = L.R
    _Q, npl = cell_universe(L)
    GR = GRing(R.addc, R.negc)
    rep, repdeg = {}, {}
    for c in range(R.h):
        cells, dg = {}, 0
        for pl, e in L.minrep[c].items():
            d, cl = R.deg[pl], R.cls[pl]
            same = [q for q in R.by_deg[d] if R.cls[q] == cl]
            ok(len(same) == 1, "%s: the representative cell (%d, %d) holds %d "
               "places" % (L.name, d, cl, len(same)))
            ok(npl[d][cl] == 1, "%s: the count says cell (%d, %d) holds %d "
               "places" % (L.name, d, cl, npl[d][cl]))
            cells[(d, cl)] = cells.get((d, cl), 0) + e
            dg += d * e
        rep[c], repdeg[c] = cells, dg
    return ELight(npl, GR, rep, repdeg, L.g, tag)


# ------------------------------------------------------------- S1 control
def s1a_counts(ladder):
    """PE1: the group-ring construction against the engine's class census."""
    print("  ring     h    deg Q  Q under the trivial character  degrees "
          "checked  beyond the input")
    for L in ladder:
        Q, npl = cell_universe(L)
        built = max(L.R.by_deg)
        used = max(0, 2 * L.g - 2)
        for d in range(1, built + 1):
            ok(npl[d] == engine_cells(L.R, d),
               "%s: degree %d reads %s, the group ring says %s"
               % (L.name, d, engine_cells(L.R, d), npl[d]))
        ok(built > used, "%s: the input used every degree it was checked on"
           % L.name)
        print("  %-8s %-4d %-6d %-30s %-17d %d"
              % (L.name, L.R.h, len(Q) - 1, [sum(v) for v in Q], built,
                 built - used))


def eng_delta(L, st, veh):
    """What an engine vehicle DOES, in the light walker's own cell language:
    the exponent of every cell it touches, before and after. No reading of a
    core is needed, which is the point -- a divisor does not carry one."""
    R = L.R
    out = []
    for pl, e in veh.items():
        e0 = st.get(pl, 0)
        out.append(((R.deg[pl], R.cls[pl]), e0, e0 + e))
    return tuple(sorted(out))


def eng_types(L, st, ties):
    out = {}
    for veh in ties:
        key = eng_delta(L, st, veh)
        out[key] = out.get(key, 0) + 1
    return out


def s1b_walker(ladder):
    """PE2: the light menu against the engine's, at every state of the
    engine's element walk, the walker advanced by the ENGINE's move."""
    print("  ring     states  types compared  vehicles  ended by")
    for L in ladder:
        s, st, n, ntypes, nveh = light_of(L, L.name + "/control"), {}, 0, 0, 0
        why = "the walk length"
        for _ in range(ENGINE_N):
            try:
                _lam, cost, ties = RO.menu_of(L, "element", st)
            except AssertionError:
                TRUNC["engine-short"] += 1
                why = "the trimmed universe"
                break
            want = eng_types(L, st, ties)
            got_cost, got = s.menu()
            ok(got_cost == cost, "%s: the light cost %s against the engine's %s"
               % (L.name, got_cost, cost))
            ok(got == want, "%s: the light menu %s against the engine's %s"
               % (L.name, sorted(got.items()), sorted(want.items())))
            ntypes += len(want)
            nveh += len(ties)
            key = sorted(want)[0]
            veh = next(v for v in ties if eng_delta(L, st, v) == key)
            s.apply(key)
            st = EC.apply_veh(st, veh)
            n += 1
        print("  %-8s %-7d %-15d %-9d %s" % (L.name, n, ntypes, nveh, why))


PLANT_T = 32          # the tick the undercut is planted at
PLANT_COV = 80        # degrees seeded as covered, so no fresh open is cheaper


def cheapest(s, d, c, e):
    """The cheapest offer at a cell over the offsets the engine allows."""
    r0 = s.door(d, e)
    return min(s.cost(d, c, r0 + j) for j in range(s.g + 1))


def s1c_undercut(ladder):
    """E3's mechanism as a detector, planted rather than argued: a degree-2
    place freshly clocked at a tick of %d against a rational place at
    exponent 3, where the rational place must be STRICTLY cheaper and the
    menu must pick it -- and the SAME state with that place at exponent 1,
    where it must not be cheaper at all. A detector that fires in both states
    is testing the state, not the depth.""" % PLANT_T
    print("  ring     deg-2 clock  rational at e=3  at e=1  menu picks the")
    print("                                                 rational place")
    for L in ladder:
        _Q, npl = cell_universe(L)
        if npl[2] == [0] * L.R.h:
            print("  %-8s %s" % (L.name, "no place of degree 2 -- skipped"))
            continue
        c2 = next(c for c in range(L.R.h) if npl[2][c] > 0)
        c1 = next(c for c in range(L.R.h) if npl[1][c] > 0)
        prices, picked = [], []
        for e1 in (3, 1):
            s = light_of(L, L.name + "/plant")
            # the degree-2 place just clocked: it sits at the previous tick
            # plus one, which is where a clock move lands it
            s.seat[(2, c2)] = [PLANT_T // 2 + 1]
            s.seat[(1, c1)] = [e1]
            s.lam_odd = 1
            for d in range(1, PLANT_COV + 1):
                s.lam_odd = EC.lcm(s.lam_odd, (1 << d) - 1)
            s.cov = set(range(1, PLANT_COV + 1))
            s.T = PLANT_T
            clock = cheapest(s, 2, c2, PLANT_T // 2 + 1)
            rival = cheapest(s, 1, c1, e1)
            prices.append((clock, rival))
            _cost, ties = s.menu()
            cells = set(cell for key in ties for cell, _a, _b in key)
            picked.append(((1, c1) in cells, (2, c2) in cells))
        ok(prices[0][1] < prices[0][0],
           "%s: the rational place at exponent 3 prices at %d against the "
           "degree-2 clock's %d" % (L.name, prices[0][1], prices[0][0]))
        ok(picked[0] == (True, False),
           "%s: at exponent 3 the menu reads %s, not the rational place alone"
           % (L.name, picked[0]))
        ok(prices[1][1] >= prices[1][0],
           "%s: the rational place at exponent 1 already prices at %d under "
           "the clock's %d, so the detector reads the state, not the depth"
           % (L.name, prices[1][1], prices[1][0]))
        ok(picked[1][1], "%s: at exponent 1 the degree-2 clock is already off "
           "the menu, so the detector reads the state, not the depth"
           % L.name)
        print("  %-8s %-12d %-16d %-7d %s"
              % (L.name, prices[0][0], prices[0][1], prices[1][1],
                 "alone at e=3; the clock survives at e=1"))


# ------------------------------------------------------------- the long walk
def key_of(s):
    return (tuple(sorted((k, tuple(sorted(v))) for k, v in s.seat.items())),
            s.T)


def canon(ties):
    """The canonical tie-break: the least type key. It picks an ORDER among
    the minimal moves; whether it also picks an OUTCOME is measured at S2 by
    re-pricing every declined type at the successor."""
    return sorted(ties)[0]


def branches(L):
    """Every distinct state reachable by any tie choice over the first
    stretch, CAPPED -- the number of states dropped is returned with them,
    because a ring that hits the cap has a branch set this rig has NOT
    enumerated, and every column read over its branches is scoped to the
    ones carried."""
    dropped = [0]
    cur = [light_of(L, L.name)]
    for _ in range(BRANCH_N):
        nxt, seen = [], set()
        for s in cur:
            _cost, ties = s.menu()
            for key in sorted(ties):
                s2 = s.copy()
                s2.apply(key)
                k = key_of(s2)
                if k in seen:
                    continue
                seen.add(k)
                nxt.append(s2)
        if len(nxt) > BRANCH_CAP:
            TRUNC["branch-cap"] += len(nxt) - BRANCH_CAP
            dropped[0] += len(nxt) - BRANCH_CAP
            nxt = nxt[:BRANCH_CAP]
        cur = nxt
    return cur, dropped[0]


def vehicle(delta):
    """A move stripped of the state it was priced in: which cells it raises
    and by how much. The DELTA carries the from-exponent, so comparing deltas
    across a move would score a declined type as lost merely because the
    state moved under it -- only cells the taken move also touched can
    genuinely change a declined move's standing, and those show up as a
    changed door rather than a changed name."""
    return tuple(sorted((cell, e1 - e0) for cell, e0, e1 in delta))


def continue_walk(s, n, rejoin):
    """The canonical continuation, with the declined tie types re-priced at
    the successor over the first REJOIN_N steps -- recorded, not asserted:
    the ideal world's reordering lemma is void here."""
    for i in range(n):
        _cost, ties = s.menu()
        key = canon(ties)
        if i < REJOIN_N and len(ties) > 1:
            s2 = s.copy()
            s2.apply(key)
            _c2, t2 = s2.menu()
            still = set(vehicle(k) for k in t2)
            for other in ties:
                if other == key:
                    continue
                rejoin[0] += 1
                if vehicle(other) in still:
                    rejoin[1] += 1
        s.apply(key)
    return s


def main():
    EC.DMAX = G2.DMAX = ENGINE_DMAX
    ladder = CT.build_ladder()

    section("S1  THE POSITIVE CONTROL")
    print("(a) THE CELL COUNTS FROM THE GROUP RING")
    s1a_counts(ladder)
    print("\n(b) THE LIGHT WALKER AGAINST THE ENGINE")
    s1b_walker(ladder)
    print("\n(c) THE UNDERCUT, PLANTED")
    s1c_undercut(ladder)

    section("S1(d)  WHERE THE PRINCIPAL PLACES ARE")
    print("  PE4: the degrees with no place of class 0, and the least")
    print("  class-0 population above the last of them.")
    print("\n  ring     degrees with no principal place   least above  at "
          "degree")
    for L in ladder:
        _Q, npl = cell_universe(L)
        bad = [d for d in range(1, DEG_CAP + 1) if npl[d][0] == 0]
        top = max(bad) if bad else 0
        rest = [(npl[d][0], d) for d in range(top + 1, DEG_CAP + 1)]
        lo = min(rest) if rest else (0, 0)
        ok(lo[0] >= 1, "%s: degree %d has no principal place above the bound"
           % (L.name, lo[1]))
        print("  %-8s %-33s %-12d %d"
              % (L.name, str(bad) if bad else "none", lo[0], lo[1]))

    section("S2  THE LONG WALK")
    print("  Every tie choice followed for %d moves, each distinct state then"
          % BRANCH_N)
    print("  continued canonically to %d moves in all." % WALK_N)
    print("  Every column below is over ALL branches, not one continuation.")
    print("\n  ring     branches  tick   seated  doublings  final clock "
          "(degree, class)  settles at  above e=1  declined types still")
    print("                                                              "
          "                                        minimal at the successor")
    PHASE[0] = "walk"
    shapes = {}
    for L in ladder:
        rows, rejoin = [], [0, 0]
        got, dropped = branches(L)
        for s in got:
            rows.append(continue_walk(s, WALK_N - BRANCH_N, rejoin))
        shapes[L.name] = rows
        clocks = set(settling(s)[1][0] for s in rows)
        steps = set(settling(s)[0] for s in rows)
        deep = set(len(deep_places(s)) for s in rows)
        print("  %-8s %-9s %-6d %-7s %-10s %-30s %-11s %-10s %d of %d"
              % (L.name, "%d%s" % (len(rows), " *" if dropped else ""),
                 rows[0].T,
                 sorted(set(sum(len(v) for v in s.seat.values())
                            for s in rows)),
                 sorted(set(len(s.doubles) for s in rows)), sorted(clocks),
                 sorted(x if x is not None else -1 for x in steps),
                 sorted(deep), rejoin[1], rejoin[0]))
    PHASE[0] = "control"
    print("\n  A STAR marks a ring whose branch sweep hit the cap, %d states"
          % TRUNC["branch-cap"])
    print("  being dropped in all, so at those rings every column above is")
    print("  over the branches CARRIED and not over all of them. And past the")
    print("  branched stretch every ring is canonical, so no column here is a")
    print("  statement about all trajectories at any ring.")
    print("\n  A settling step of -1 means the clock never changed hands. The")
    print("  last column is the ideal world's reordering lemma put to the")
    print("  question here, where nothing proves it: a declined minimal type")
    print("  re-priced at the successor of the taken one.")

    section("S3  THE ERA LEDGER")
    print("  PE5 and PE8: per era -- the moves between two tick doublings --")
    print("  its opens, its rider units, and the clock's price at its start.")
    print("  The opens are what E3 borrowed from the ideal steady state as a")
    print("  hypothesis; the rider columns are what the handover predicted")
    print("  would track them.")
    print("\n  ring     era  tick   moves  opens  rider units from an open  "
          "from a deepening move")
    for L in ladder:
        s = shapes[L.name][0]
        for i, (opens, ro, rd, mv) in enumerate(s.eras):
            print("  %-8s %-4d %-6d %-6d %-6d %-25d %d"
                  % (L.name, i, 1 << i, mv, opens, ro, rd))

    section("S4  THE LIMIT'S SHAPE")
    print("  PE3, PE6, PE7, PE9: every doubling with the place that crossed")
    print("  and what carried it, and the support above exponent 1. The")
    print("  ORBIT LAW is E2's clause made checkable: after the clock settles")
    print("  the only move that is not an open is the clock's own, so the")
    print("  only cells a rider can ever reach again are those of the minimal")
    print("  representatives its class summons -- and if the clock's class is")
    print("  0 there are none, and the clock is the only deep place.")
    for L in ladder:
        s = shapes[L.name][0]
        print("\n  %s" % L.name)
        after, wins, ranged = [], [], []
        for br in shapes[L.name]:
            st0, last = settling(br)
            # the window the law speaks over: the clock established (its own
            # first doubling if it never changed hands) AND the low-degree
            # transient over, the last open that summoned a rider being what
            # ends it
            trans = max(br.doubles[0][0],
                        max(br.open_riders) if br.open_riders else -1)
            st0 = max(br.doubles[0][0] if st0 is None else st0, trans)
            wins.append(st0)
            gam = last[0][1]
            orbit = set()
            for m in range(br.h):
                orbit |= set(br.rep[br.GR.negc[br.GR.scale(gam, m)]])
            # a unit is DEEPENING when the slot already stood at 1 or more; a
            # unit that merely seats a place is the flat support, not a
            # coordinate going deep
            grew = {}
            for step, cell, slot, kind, n, pre in br.units:
                if step > st0 and (cell, slot) != last and pre >= 1:
                    grew.setdefault((cell, kind), 0)
                    grew[(cell, kind)] += n
            ok(all(cell in orbit and kind == "rider" for cell, kind in grew),
               "%s: after the clock settled at step %d, %s grew outside its "
               "orbit %s" % (L.name, st0, sorted(grew), sorted(orbit)))
            # the containment above ranges over `grew` and is VACUOUS where
            # nothing grew, which is four of the six rings. Where the orbit
            # reaches nothing but the clock, the law's whole content IS the
            # emptiness, so assert that directly rather than let an empty
            # `all` stand in for it
            ok(gam != 0 or not grew,
               "%s: a principal clock and %s still grew" % (L.name, sorted(grew)))
            ok(orbit - set([last[0]]) or not grew,
               "%s: the orbit reaches nothing but the clock and %s still grew"
               % (L.name, sorted(grew)))
            ranged.append(len(grew))
            # PE7 in the only form the run leaves standing: the clock changes
            # hands inside the TRANSIENT or not at all. Reading that off st0
            # would be a tautology -- st0 is at least the settling step, and
            # settling() is DEFINED as the last hand-change, so "no doubling
            # after st0 went elsewhere" cannot fail. The falsifiable claim is
            # that the settling step lies inside the transient, whose end is
            # the last open that summoned a rider, measured independently.
            hand, _l = settling(br)
            ok(hand is None or hand <= trans,
               "%s: the clock changed hands at step %s, after the transient "
               "ended at %d" % (L.name, hand, trans))
            after.append(len(grew))
        print("    the orbit-containment check ranged over %d (cell, kind) "
              "pairs across the branches -- it is VACUOUS at a ring where "
              "that is 0, and what carries the law there is the emptiness, "
              "asserted separately" % sum(ranged))
        print("    the law's window opens at step %s of %d; places OTHER than"
              % (sorted(set(wins)), WALK_N))
        print("    the clock still deepening inside it, per branch: %s"
              % sorted(set(after)))
        by_rider = [st for st, _d, _c, k in s.opened if k == "rider"]
        cores = {}
        for _st, _d, cc, k in s.opened:
            if k == "open":
                cores[cc] = cores.get(cc, 0) + 1
        print("    places first seated by an OPEN, by class: %s"
              % dict(sorted(cores.items())))
        print("    places first seated by a RIDER: %d, last at step %s"
              % (len(by_rider), max(by_rider) if by_rider else "--"))
        bare = set(d for d in range(1, DEG_CAP + 1)
                   if cell_universe(L)[1][d][0] == 0)
        for b in shapes[L.name]:
            for _s, dd, _c in b.impure:
                ok(dd in bare, "%s: a non-principal open at degree %d, which "
                   "has a principal place of its own" % (L.name, dd))
        print("    non-principal opens, over all branches: %s, the last at "
              "step %s, at degrees %s -- every one of them a degree S1(d) "
              "lists as having no principal place at all"
              % (sorted(set(len(b.impure) for b in shapes[L.name])),
                 sorted(set(max([x[0] for x in b.impure] or [-1])
                            for b in shapes[L.name])),
                 sorted(set(x[1] for b in shapes[L.name] for x in b.impure))))
        print("    the last OPEN that summoned a rider, per branch: %s"
              % sorted(set(max(b.open_riders) if b.open_riders else -1
                           for b in shapes[L.name])))
        print("    doublings (step, degree, class, carrier, deepest rational")
        print("    standing BEFORE the move, slots crossing at once):")
        shown = s.doubles[:6] + ([None] if len(s.doubles) > 8 else []) \
            + (s.doubles[-2:] if len(s.doubles) > 8 else s.doubles[6:])
        for rec in shown:
            if rec is None:
                print("      ...")
                continue
            st, cell, _slot, carrier, deep, nx = rec
            print("      %-5d %-3d %-3d %-7s %-4d %d"
                  % (st, cell[0], cell[1], carrier, deep, nx))
        print("    above exponent 1 (degree, class, e, core, rider): %s"
              % deep_places(s))

    section("SUMMARY")
    print("  %d checks passed." % CHECKS)
    print("  moves read: %s" % MOVES)
    print("  truncation: %s" % TRUNC)


if __name__ == "__main__":
    main()
