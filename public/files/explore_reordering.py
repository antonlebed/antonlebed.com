"""explore_reordering.py -- is a CROSS-TYPE decline a reordering or a choice?

THE QUESTION. The greedy image over a function field is a product, over a
trajectory's surviving openings, of the tie multiplicity at each, and
"multiplicity" means the WITHIN-TYPE multiplicity: a tie set splits into the
types the engine can read -- lambda reads (degree, depth), and the element
world reads one further datum, the ideal class -- and a choice between two
TYPES is held to be a REORDERING, the same moves in a different order
reaching one limit, rather than a choice. Every count the corpus reports
rests on that reading and it has never been proved or tested. It also
carries almost the whole formula: exhaustively over the shallow region
essentially every element-world tie is cross-type (explore_coarse_type.py
F5), so the reading discards nearly the entire raw tie width at almost every
opening.

WHAT THE DESK FOUND FIRST, and it is why this rig exists in this shape: the
question is not one question. Two tie members are cross-type in two
different ways, and the ways have different fates.

THE SPECIES, fixed at the freeze. Write d for a core's degree, e for its
depth in the state, kappa = v2(lambda), g for the genus, and m(c) for the
degree of the minimal effective affine representative of class c, so m <= g
by Riemann-Roch. Every tie member is a bare door -- core plus the minimal
representative of the class the core must cancel, at exponent exactly the
door (explore_coarse_type.py lemma S) -- so a pair of members is named by
its two CORES:

  WITHIN    same degree, same class, same exponent. What the formula counts.
  CLASS     same degree and exponent, different class. Exists in the element
            world only: the ideal world does not read the class, so a
            same-degree tie there is within-type by definition.
  DEPTH     same degree, different exponent, hence different depth. Needs
            d*e <= g, since a clocked member costs d*(2^kappa + 1) against a
            deepening one's d*(2^kappa + 1 - e) and only the rider can pay
            the difference.
  ODD-EVEN  different degrees, one member FRESH and the other DEEPEN or
            CLOCKED. A fresh move multiplies lambda by the odd 2^d - 1; a
            deepen or clocked move raises v2(lambda) and nothing else.
  EVEN-EVEN different degrees, both clock moves.
  ODD-ODD   different degrees, both fresh. Possible only in the element
            world, where a fresh move costs d + m(-cls) and two degrees can
            be levelled by their riders.

THE HAND-ATTACK, on paper before any engine code.

 A. THE CLASS SPECIES IS A CHOICE ABOVE THE GENUS, and no horizon is
    needed. Let the two cores P and Q be UNSEATED (fresh or clocked), of one
    degree d > g, and let Q be chosen. Then some place of degree d is seated
    at depth e >= 1 in the successor, so P is CLOCKED there and forever
    after: its cheapest vehicle costs at least d*(2^kappa + 1), while the
    seated neighbour's own deepening costs at most
    d*(2^kappa + 1 - e) + g. The gap is at least d*e - g >= d - g > 0, so P
    is STRICTLY dominated at every later state and is never a minimal move.
    Nor can P arrive as a passenger: a vehicle is a core plus a minimal
    representative, and a minimal representative has degree at most g < d.
    So P has limit exponent 0 in the chosen branch and at least 1 in its
    own: THE TWO BRANCHES REACH DIFFERENT LIMITS. The formula's within-type
    multiplicity discards a choice.
    The same argument fails at d <= g by exactly one step -- the rider can
    pay a gap of g -- which is the readmission regime the capacity bound
    already covers, and this rig reports the two regimes apart.
 B. AND WHAT THAT DOES TO THE PRODUCT. Distinct choices at such an opening
    have disjoint images, so |Im(s)| >= sum over the tied classes of
    |Im(s + v)|, and lockstep equates the terms only INSIDE a class -- two
    cores of different classes wear different colours and generate no
    isomorphism. The count is therefore a SUM over class-branches of
    products, where the formula follows ONE branch and multiplies its
    width: a lower bound rather than the count.
 C. THE ODD-EVEN SPECIES IS A REORDERING, in the ideal world, and the
    branches REJOIN IN TWO MOVES. A fresh move at degree d' leaves
    v2(lambda) untouched, so the clock member's door 2^kappa + 1 - e is
    unchanged and it is still minimal after it. A clock move leaves
    lambda_odd untouched, so the fresh member's cost d' is unchanged, every
    other fresh cost is unchanged, and every clock cost only rises with
    kappa -- including the moved place's own next door, which costs d*2^kappa
    against its old d*(2^kappa + 1 - e) and e <= 2^kappa. So the minimum is
    unmoved and the fresh member is still minimal after it. The two vehicles
    are supported at different places, so both orders reach the SAME
    DIVISOR. In the ELEMENT world the argument has a hole and the rig is
    what closes it: a fresh core's RIDER lands on a seated place and can
    itself cross a 2-power frontier, so an element fresh move can raise the
    clock after all.
 D. A SAME-DEGREE PAIR SHARES ITS KIND. If a place of degree d is seated
    then (2^d - 1) divides lambda_odd, so no place of that degree is fresh.
    Hence "fresh at degree d" and "deepen at degree d" cannot both occur,
    and the DEPTH species is a clocked member against a deepening one.

THE OBSERVABLE, and what is decidable at a horizon. Two branches reach the
same limit iff they agree at every place -- the same places at infinite
exponent and the same finite exponents elsewhere -- and a finite head start
at a place the future sends to infinity is forgotten, so measuring the STATE
does not settle the LIMIT. Two things do settle it:

  REJOIN      each member is still MINIMAL after the other, so both branches
              reach one state and every later move agrees. Proves ONE limit.
  DOMINATION  a declined core is unseated at a degree that carries a seated
              place, with d*e > g, AND lies outside every minimal
              representative, which needs its degree above g. Lemma A then
              proves it is never seated again by either route, so the two
              limits differ at that place. Proves TWO limits, and only the
              first of its two conditions is about cost -- the second is
              what stops a rider carrying the place back.

Everything else is UNDECIDED at a horizon and is printed as such rather than
scored. A rejoin is checked at the level the image cares about -- membership
of the MINIMAL set, not availability at some cost -- because a policy in the
minimal-move class may only take minimal moves.

THE SETTING. The six-ring function-field ladder the greedy image was
measured over, with the engines imported rather than re-implemented:
F_2[x] (genus 0) and the q = 2 elliptic ladder h = 1..5 from
explore_greedy_image_ec.py, the genus-2 ring y^2 + y = x^5 + x from
explore_greedy_image_g2.py, and the ring interface, the class data and the
exhaustive state enumeration from explore_coarse_type.py. Both worlds of
each. Two regions: the EXHAUSTIVE shallow one, every effective divisor to a
degree cap, which turns "did not occur" into "cannot occur in this region";
and the TRAJECTORY region, where the widths run an order of magnitude
wider -- 60 against the exhaustive region's 5 -- though still short of the
depth the source censuses reach, so a zero there is weaker than a zero
here and is read as one.

TRANSPLANT FLAGS, fixed at the freeze. Every intuition below is imported
from a neighbouring parameter value and is marked rather than trusted.
 1. From the within-type branch enumerations: "branches never rejoin in any
    measured run." Those rigs branch WITHIN a type by design
    (explore_greedy_image_ec.py S5), so the statement is about the species
    where starvation applies and carries NOTHING to the cross-type ones. It
    is not assumed here in either direction.
 2. From the ideal world to the element world: "a fresh move leaves the
    clock alone." True where a vehicle is a bare place power, and lemma C
    names the hole the rider opens. The rig tests both worlds separately.
 3. From the trajectory censuses: "free declines come back." A return is a
    seating in the STATE, and the question is about the LIMIT. Nothing is
    carried; the two certificates above are what is read.
 4. To the number rings: NOTHING is carried. Their ties are conjugate pairs
    of one norm, whose classes are inverse and so differ wherever the class
    group has an element of order above 2 -- the CLASS species in another
    world, with no genus to bound the rider. That transfer is named here and
    left to the ring that owns it. (SINCE RUN by
    explore_class_species_nf.py: the species is there and is every element
    tie at h = 3, the rider bound is MINKOWSKI's and sits at norm 2, and
    the certificate carries across -- with the same silence at seated
    cores, which the number rings settle by the LOCK instead, freezing every
    place its recurrent vehicle does not carry. SINCE SUBSUMED: both that
    freeze and the starvation here are one lemma about two door prices,
    which needs no lock and closes the seated-core regime in a sprawling
    world too -- explore_undercut.py.)

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE CLASS SPECIES OCCURS ABOVE THE GENUS. What the rig PRINTS: per ring
    per world per region, the cross-type pair census by species, and for the
    CLASS species the split by whether both cores are unseated and by
    core degree against g.
    KILL: zero CLASS pairs with unseated cores of degree above g anywhere,
    in which case lemma A is vacuous and the reading survives untouched
    here.
PR2 AND EVERY ONE OF THEM IS A CHOICE (lemma A). What the rig PRINTS: at
    every such pair, the domination certificate -- the declined core's
    cheapest vehicle against the successor's menu cost, the seated
    neighbour's door, and d*e against g -- plus a forward check that the
    declined core is never seated along the canonical continuation.
    KILL: one such pair where the declined core is a minimal move at the
    successor, or is seated along the continuation.
PR3 THE ODD-EVEN SPECIES REJOINS IN THE IDEAL WORLD (lemma C), at every
    occurrence: each member is minimal after the other and the two orders
    give one divisor.
    KILL: one ideal-world odd-even pair that does not rejoin.
PR4 THE IDEAL WORLD HAS NO CLASS SPECIES, by definition of the type it
    reads, and no ODD-ODD species, since two fresh moves there cost exactly
    their degrees.
    KILL: one of either.
PR5 THE ELEMENT WORLD'S FRESH MOVES CAN MOVE THE CLOCK (lemma C's hole).
    What the rig PRINTS: how many element fresh vehicles raise v2(lambda)
    through their rider, and whether any odd-even pair fails to rejoin
    because of it.
    KILL: none -- this is an open observable. A zero would say the ideal
    proof happens to cover the element world too.
PR6 THE OPEN SPECIES, printed and not predicted: EVEN-EVEN, ODD-ODD and
    DEPTH pairs classified REJOINED / DOMINATED / UNDECIDED.
PR7 THE CENSUS, printed and not predicted: per ring per world, the tie
    states, the within-type width the formula multiplies, and the
    LAMBDA-width -- the largest group of members sharing a core degree and
    exponent, which is what lemma A says survives an opening. The element
    world's lambda-width against the ideal world's width is the test of
    whether the class group divides the IMAGE or only the tie WIDTH.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE CROSS-TYPE QUESTION IS NOT ONE QUESTION, and the corpus asked only one
   of the questions inside it (the taxonomy above, exhaustive in range). The
   species do not merely differ in fate, they live in different worlds: the
   IDEAL world's cross-type pairs are ODD-EVEN and EVEN-EVEN and nothing else,
   at all six rings, because a same-degree tie there is within-type by
   definition and two fresh moves cost exactly their degrees. The CLASS, DEPTH
   and ODD-ODD species exist in the element world alone, and for two reasons
   that both need it: the class is READ there, and the rider can level two
   costs the ideal world prices apart. So "a cross-type decline is a
   reordering" is a statement about two different objects in the two worlds,
   and it was read as one.

F2 THE CLASS SPECIES IS A CHOICE, NOT A REORDERING (proved, lemma A; 473
   certificates over four rings, and 344 forward checks with no return). Two
   cores of one degree and exponent in different classes tie; whichever is
   chosen, the other is unseated at a degree that now carries a seated
   place, so its own vehicle is dearer by d*e - g at every later state and
   it can never be a core again; and above the genus it cannot arrive as a
   passenger either, minimal representatives having degree at most g. Its
   limit exponent is 0 in the one branch and at least 1 in the other, so the
   two branches reach DIFFERENT LIMITS -- with no horizon, no census and no
   appeal to a lock. Certified at 30, 95 and 4 pairs in the exhaustive
   region at h = 3, 4 and genus 2, and at 9, 24, 90 and 221 pairs in the
   trajectory region at h = 3, 4, 5 and genus 2, where the degrees run
   higher. Every one of the 473 is TWO-SIDED -- each core starves the
   other -- which is not required for the verdict, one direction being
   enough to separate the limits, and says the species is symmetric where
   it fires.

F3 SO THE PRODUCT FORMULA'S FACTOR IS TOO SMALL, AND THE COUNT IS A SUM OF
   PRODUCTS (a derivation from F2, lemma B). Distinct choices at a certified
   opening have disjoint images, so |Im(s)| >= sum over the tied classes of
   |Im(s + v)|; lockstep equates those terms only INSIDE a class, two cores
   of different classes wearing different colours and generating no
   isomorphism between their subtrees. The within-type product therefore
   follows ONE class-branch of that sum where the count adds the others, so
   it is a lower bound. (SINCE WIDENED: the colours differ by DEGREE as
   readily as by class, and the cross-degree EVEN-EVEN pairs this rig left
   open are certified choices too, so the sum runs over TYPES and the bound
   holds in the ideal world, which reads no class at all --
   explore_undercut.py.) The bound is not tight
   where the species occurs: the within-type width is 1 -- the formula
   scoring no choice at all -- at 38 openings ON measured trajectories,
   which is where the product is taken, and at 121 further tie states in
   the exhaustive region, which are states a trajectory could stand at
   rather than ones any run visited. A certified pair proves at least two
   limits survive each of them. What this does NOT touch is the cardinality
   verdict at these six rings: the openings there are endless, and a larger
   factor at endlessly many openings is still the continuum. It bites where
   the image is FINITE, which is the number rings and the one ring family
   the coarse-type result never covered.

F4 THE ODD-EVEN SPECIES IS A REORDERING, AND ITS FIRST PROOF WAS WRONG IN A
   WAY THE RIG CORRECTED (rule in range; 4419 ideal-world occurrences over six
   rings and both regions, every one rejoining, 0 undecided). Lemma C's
   two-move argument holds as stated only for a DEEPEN member: a CLOCKED
   member sits at e = 0 with door 2^kappa + 1, and after it is taken the same
   place stands at depth 2^kappa + 1 under clock kappa + 1, where its next
   door costs d*2^kappa -- strictly LESS than the d*(2^kappa + 1) it just
   paid. The minimum drops, the fresh member is temporarily out-competed, and
   the two orders are separated by the moves that cheaper door invites. They
   still meet, in the IDEAL world: the fresh member cannot be starved in the
   meantime, since clocking a degree d' needs a seated degree DIVISIBLE by d'
   -- a primitive prime divisor of 2^(d') - 1 divides 2^m - 1 only when d' | m
   -- and a move cheaper than d' has degree below d'. So it returns to the
   minimal set when the costs climb back and both branches reach one divisor.
   That step is exactly what the element world does not have, a rider being
   free to seat a place of any degree up to g. Measured as a REJOIN at 3439
   pairs directly and as a DELAYED rejoin, found by reachability inside a
   degree budget, at 980 more.

F5 AND THE GENUS IS EXACTLY WHERE THE CERTIFICATE STOPS, which the rig
   caught by refusing its own first version (rule in range; 344 covered
   cores never seated again, against 5 of 6 rider-eligible ones coming
   back). The first certificate shut only the CORE route, d*e > g, and the
   forward check along the canonical continuation immediately found a
   degree-1 core seated again -- as a RIDER, which is the readmission the
   capacity bound already files. With both routes shut the same check finds
   no return anywhere; with only the core route shut, 5 of 6 come back. The
   two regimes are the same line the rider bound draws, seen from the
   opposite side: below the genus a declined core is a loan, above it a
   loss.

F6 WHAT WAS STILL OPEN, and it is now three named species rather than one
   claim. EVEN-EVEN -- two clock moves at different degrees -- never once
   rejoins inside the budget the search spends, in either region or either
   world (0 of 1626), and no certificate available HERE fires on it: taking
   either member raises the clock and makes the other dearer, so neither the
   commutation argument nor the starvation argument runs. (SINCE CLOSED: a
   third certificate does run on it, comparing two DOOR PRICES rather than
   asking what recurs, and it proves the species a CHOICE at every
   occurrence -- explore_undercut.py.) DEPTH and ODD-ODD are mixed: ODD-ODD
   rejoins at every trajectory-region occurrence (396) and at none of the 32
   in the exhaustive one. The element world's ODD-EVEN residual is 74 pairs,
   and it is NOT the rider-clock hole lemma C named -- 0 of 1065 element fresh
   vehicles move the clock through their rider at any ring. (SINCE EXPLAINED:
   the rider's hole is that it DISCOUNTS A DOOR rather than moving the clock,
   which drops the menu minimum below the tie cost and out-competes the other
   member; it accounts for that residual and for the 32.)

THE DESIGN, in seven sections after the control.

 S1 THE POSITIVE CONTROL, run before any census is read.
    (a) The ladder's own invariants through this rig's entry points: one
        minimal affine representative per class, of degree at most g.
    (b) THE SPECIES CLASSIFIER, on synthetic pairs built to order: two
        cores of one degree and class, of one degree and two classes, of one
        degree and two exponents, and of two degrees in each kind pairing.
        Each must come back with its own name.
    (c) THE REJOIN DETECTOR, on a planted commuting pair and a planted
        non-commuting one -- a detector that cannot see a rejoin cannot
        report their absence, and a detector that sees one everywhere
        cannot either.
    (d) THE DOMINATION DETECTOR, on a state where a place is starved, one
        where it is not, and one where the core route is shut but a rider
        can carry the place back -- the last being the version the forward
        check refuted, kept as a control so it cannot return.
 S2 THE EXHAUSTIVE REGION: every effective divisor to the cap, both worlds,
    six rings. The species census (PR1, PR4).
 S3 THE CERTIFICATES: domination at every CLASS pair above the genus (PR2),
    rejoin at every ODD-EVEN pair (PR3), and the fresh-rider clock count
    (PR5). A pair that rejoins may not also starve a core, and the two
    certificates are asserted against each other rather than merely counted.
 S4 THE WIDTHS: what the formula multiplies against what survives (PR7).
 S5 THE TRAJECTORY REGION: canonical walks from a seed battery, the same
    census and the same certificates where the widths are large.
 S6 THE FORWARD CHECK: a starved core followed along the canonical
    continuation, split by whether the certificate covers it.
 S7 WHERE THE FORMULA IS BLIND: openings carrying a certified choice, and
    how many of those the within-type width scores as no choice at all.

Run: `python explore_reordering.py`. RUN RECORD (253121 checks, ~4 s). S1
control: the six rings with one minimal representative per class and every
representative inside its genus; the classifier naming all six species on
synthetic pairs and reading the class split as within-type in the ideal world;
the rejoin detector finding 48 rejoins and refusing 134 within-type pairs, so
neither its hits nor its zeros are automatic; the domination detector
certifying a starved degree-4 core, refusing a core at an unseated degree, and
refusing a starved RATIONAL point because a rider can carry it back. S2
exhaustive region, states to degree 8 (9 at F_2[x]): 416/225/352/428/431/843
ideal tie states and 416/239/344/408/331/590 element ones over F_2[x], h =
2..5 and genus 2. The ideal world's cross-type pairs are ODD-EVEN and
EVEN-EVEN only at every ring (PR4 hit); the element world adds CLASS at
171/117/691/428 pairs for h = 3, 4, 5 and genus 2, DEPTH at 290 (h = 4 only)
and ODD-ODD at 16 and 16 (h = 4, genus 2). S3: CLASS pairs split above/below
the genus and on seated cores 30/102/39, 95/6/16, 0/480/211 and 4/115/309;
every pair above the genus certified a CHOICE and no pair below one did. Ideal
ODD-EVEN: 1564 rejoins and 955 delayed rejoins, 0 undecided at all six rings
(PR3 hit, with lemma C repaired -- F4). Element ODD-EVEN: 72 undecided, and 0
of 1065 element fresh vehicles move the clock through their rider, so PR5's
observable is a zero. S4 widths, element world: the within-type width is 1 at
344 of 344 tie states at h = 3 and at 331 of 331 at h = 5, where the
lambda-width reaches 2 and 4. S5 trajectory region, 10 moves from the void and
from every effective divisor to degree 2: 344 CLASS choices certified at h =
3, 4, 5 and genus 2, and 1875 further ideal ODD-EVEN rejoins with 25 delayed
and again 0 undecided. No tie state in either region passed the pair cap, so
no width is thinned. All 473 certificates are two-sided. S6 forward check: 344
covered cores followed 8 moves each with 0 seated again, against 5 of 6
rider-eligible ones seated again -- the readmission the genus bound predicts,
on the other side of the same line. S7: the within-type width is 1 where a
certified pair proves at least two limits, at 38 openings on the walked
trajectories and at 121 further tie states in the exhaustive region. No
search stopped short anywhere: the delayed-rejoin reachability met neither
the node cap nor the trimmed universe, and no walk ended early, so the only
limit on an UNDECIDED verdict is the degree budget the search spends. Slate
PR1-PR7: PR1, PR2, PR3, PR4, PR6 and PR7 hit; PR5's observable printed a zero,
so the hole lemma C named in the element world is not where the element
residual comes from. Unfrozen finds: the delayed rejoin and the clocked-door
drop that makes it necessary (F4), and the passenger route, which the forward
check found open in the first
certificate (F5).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_greedy_image_ec as EC        # the genus 0 and 1 rings
import explore_greedy_image_g2 as G2        # the genus 2 ring
import explore_coarse_type as CT            # the ladder, the types, the states

CHECKS = 0

# The exhaustive caps sit at or below the source scan's, since this rig runs
# two menu calls per cross-type PAIR on top of the scan itself.
SCAN_DEG = {"F_2[x]": 9, "h2": 8, "h3": 8, "h4": 8, "h5": 8, "g2": 8}
WALK_T = 10          # moves per canonical walk in the trajectory region
SEED_DEG = 2         # walk seeds are the void + every effective divisor here
FORWARD_T = 8        # moves the forward check follows a dominated core for
PAIR_CAP = 2000      # pairs examined per tie state; excess is REPORTED
BFS_BUDGET = 8       # added degree the delayed-rejoin search may spend
BFS_CAP = 300        # states the delayed-rejoin search may hold per branch


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def vkey(veh):
    return tuple(sorted(veh.items()))


# ------------------------------------------------------------ the species
def core_of(L, world, st, veh, lam):
    """(core place, depth, exponent, kind). Every tie member is a bare door
    (explore_coarse_type.py lemma S), which is asserted here rather than
    assumed: an offset would make the core reading ambiguous."""
    j, core = CT.offset_of(L, world, st, veh, lam)
    ok(core is not None,
       "%s/%s: a tie member that is no complete(core, door + j)"
       % (L.name, world))
    ok(j == 0, "%s/%s: a tie member at offset %s, which lemma S forbids"
       % (L.name, world, j))
    e = st.get(core, 0)
    return core, e, veh[core], L.R.kind(e, veh[core])


def species(L, world, a, b):
    """The name of a cross-type pair, from its two core readings."""
    R = L.R
    (p, ep, rp, kp), (q, eq, rq, kq) = a, b
    ok(p != q,
       "%s/%s: two distinct tie members with one core" % (L.name, world))
    if R.deg[p] == R.deg[q]:
        if rp != rq:
            return "depth"
        if world == "ideal" or R.cls[p] == R.cls[q]:
            return "within"
        return "class"
    fp, fq = kp == "fresh", kq == "fresh"
    if fp and fq:
        return "odd-odd"
    if fp != fq:
        return "odd-even"
    return "even-even"


def widths(L, world, st, ties, lam):
    """(within-type width, lambda-width): the largest group of members
    sharing (degree, class, exponent) -- what the formula multiplies -- and
    the largest sharing (degree, exponent) alone, which merges the classes
    lemma A says are choices."""
    R, fine, coarse, theirs = L.R, {}, {}, {}
    for veh in ties:
        core, _, r, _ = core_of(L, world, st, veh, lam)
        c = R.cls[core] if world == "element" else -1
        k = (R.deg[core], r)
        fine[k + (c,)] = fine.get(k + (c,), 0) + 1
        coarse[k] = coarse.get(k, 0) + 1
        # The comparison this rig exists to make is against the width the
        # FORMULA multiplies, so the fine partition is checked against the
        # source rig's own type function rather than assumed equal to it: a
        # width computed here that is not theirs would compare nothing.
        t = CT.coarse_type(L, world, veh)
        theirs[t] = theirs.get(t, 0) + 1
    ok(sorted(fine.values()) == sorted(theirs.values()),
       "%s/%s: this rig's within-type partition is not the source rig's"
       % (L.name, world))
    return max(fine.values()), max(coarse.values())


# ------------------------------------------------------- the certificates
def menu_of(L, world, st):
    lam = L.R.lam_state(st)
    cost, ties = L.mod.MENUS[world](L.R, st, lam)
    return lam, cost, ties


def rejoins(L, world, st, v1, v2):
    """Is each member still MINIMAL after the other? Then both branches can
    reach st + v1 + v2 and every later move agrees: ONE limit. Returns
    "rejoin", "not-minimal", or "unreadable" -- the last when the successor's
    menu passes the trimmed place universe, which is a READER failure and
    must never be scored as a refusal."""
    for x, y in ((v1, v2), (v2, v1)):
        s2 = EC.apply_veh(st, x)
        try:
            _, _, ties = menu_of(L, world, s2)
        except AssertionError:
            return "unreadable"
        if vkey(y) not in [vkey(v) for v in ties]:
            return "not-minimal"
    ok(vkey(EC.apply_veh(EC.apply_veh(st, v1), v2))
       == vkey(EC.apply_veh(EC.apply_veh(st, v2), v1)),
       "%s: two orders of one pair give different divisors" % L.name)
    return "rejoin"


def ridable(L):
    """The places a vehicle can carry as a PASSENGER: the supports of the
    minimal representatives, all of degree at most g. A place outside this
    set can only ever arrive as a CORE."""
    if not hasattr(L, "_ridable"):
        L._ridable = set(pl for c in range(L.R.h) for pl in L.minrep[c])
        for pl in L._ridable:
            ok(L.R.deg[pl] <= L.g,
               "%s: a minimal representative carries a place above the genus"
               % L.name)
    return L._ridable


def dominated(L, world, st, chosen, decl_core, passenger=True):
    """Lemma A at the successor of `chosen`. BOTH routes to the declined core
    must be shut: as a CORE, by d*e > g against the seated neighbour's door,
    with the engine agreeing that its cheapest vehicle is dearer than the
    menu; and as a PASSENGER, by the core lying outside the minimal
    representatives, which needs d > g. The passenger route is not
    decoration -- the forward check below catches a degree-1 core coming back
    as a rider when it is left open. Returns (verdict, detail)."""
    R = L.R
    s2 = EC.apply_veh(st, chosen)
    d = R.deg[decl_core]
    if s2.get(decl_core, 0):
        return False, "seated by the move itself"
    seated = [(pl, e) for pl, e in s2.items() if e and R.deg[pl] == d]
    if not seated:
        return False, "no seated place of the degree"
    best_e = max(e for _, e in seated)
    if d * best_e <= L.g:
        return False, "d*e = %d, inside the genus %d" % (d * best_e, L.g)
    if passenger and decl_core in ridable(L):
        return False, "degree %d <= g = %d, so a rider can carry it back" % (
            d, L.g)
    lam2, cost2, _ = menu_of(L, world, s2)
    r = R.door_r(decl_core, 0, lam2)
    veh = {decl_core: r} if world == "ideal" else L.complete(decl_core, r)
    own = R.veh_deg(veh)
    ok(own > cost2,
       "%s/%s: a core with d*e = %d > g is still a minimal move (%d vs %d)"
       % (L.name, world, d * best_e, own, cost2))
    return True, "d*e = %d > g = %d, off the rider set, own vehicle %d vs " \
                 "menu %d" % (d * best_e, L.g, own, cost2)


_REACH = {}
TRUNC = {"reach-universe": 0, "reach-cap": 0, "walk-short": 0}


def reach(L, world, st, budget, cap):
    """Every state a MINIMAL-move policy can reach from st while the added
    degree stays inside `budget`. The image is a set of limits over the whole
    minimal-move class, so the branches meet if ANY two policies do -- not
    only if the canonical pair does."""
    key = (L.name, world, vkey(st))
    if key in _REACH:
        return _REACH[key]
    base = L.R.veh_deg(st)
    seen, frontier = {vkey(st)}, [st]
    while frontier and len(seen) < cap:
        nxt = []
        for s in frontier:
            try:
                _, cost, ties = menu_of(L, world, s)
            except AssertionError:
                # the successor's menu passes the trimmed place universe, so
                # this arm is unexplored rather than absent: the search can
                # only MISS a rejoin here, never invent one, and the count
                # is printed so the conservatism is visible
                TRUNC["reach-universe"] += 1
                continue
            for veh in ties:
                s2 = EC.apply_veh(s, veh)
                if L.R.veh_deg(s2) - base > budget:
                    continue
                k = vkey(s2)
                if k in seen:
                    continue
                seen.add(k)
                nxt.append(s2)
                if len(seen) >= cap:
                    break
            if len(seen) >= cap:
                break
        frontier = nxt
    if len(seen) >= cap:
        TRUNC["reach-cap"] += 1
    _REACH[key] = seen
    return seen


def meets(L, world, st, v1, v2, budget, cap):
    """Do the two branches reach one state inside the budget? A DELAYED
    rejoin: the clocked case opens a cheaper door at the moved place, so the
    two orders are separated by the moves that door invites, and the meeting
    divisor is st + v1 + v2 plus those."""
    a = reach(L, world, EC.apply_veh(st, v1), budget, cap)
    b = reach(L, world, EC.apply_veh(st, v2), budget, cap)
    return not a.isdisjoint(b)


def forward_unseated(L, world, st, chosen, decl_core, T):
    """Lemma A says never; the canonical continuation is what a run can
    check. Returns (moves walked, seated at move or None)."""
    s = EC.apply_veh(st, chosen)
    for i in range(T):
        try:
            _, _, ties = menu_of(L, world, s)
        except AssertionError:
            return i, None
        s = EC.apply_veh(s, ties[0])
        if s.get(decl_core, 0):
            return i + 1, i
    return T, None


# ------------------------------------------------------------- the census
class Census(object):
    def __init__(self):
        self.states = 0
        self.ties = 0
        self.cross = 0
        self.pairs = {}          # species -> count
        self.verdict = {}        # (species, verdict) -> count
        self.class_above = 0     # CLASS pairs, unseated cores, degree > g
        self.class_below = 0
        self.class_seated = 0
        self.fine = {}           # within-type width histogram
        self.coarse = {}         # lambda-width histogram
        self.riderclock = 0      # element fresh vehicles that move the clock
        self.fresh = 0
        self.pair_skipped = 0
        self.dom = {}            # one-sided / two-sided domination
        self.certified_ties = 0  # tie states carrying a certified choice
        self.blind = 0           # of those, the ones the formula scores 1
        self.spec = {}           # species -> one specimen line

    def bump(self, d, k):
        d[k] = d.get(k, 0) + 1


def classify_state(L, world, st, lam, cost, ties, cen, certify=True):
    """Every cross-type pair at one tie state: its species, and which
    certificate fires."""
    R = L.R
    reads = [core_of(L, world, st, veh, lam) for veh in ties]
    for veh, (core, e, r, k) in zip(ties, reads):
        if world == "element" and k == "fresh":
            cen.fresh += 1
            if EC.v2(R.lam_state(EC.apply_veh(st, veh))) > EC.v2(lam):
                cen.riderclock += 1
    f, c = widths(L, world, st, ties, lam)
    cen.bump(cen.fine, f)
    cen.bump(cen.coarse, c)
    n = len(ties)
    npair = n * (n - 1) // 2
    if npair > PAIR_CAP:
        cen.pair_skipped += 1
        return
    seen, certified = False, False
    for i in range(n):
        for j in range(i + 1, n):
            sp = species(L, world, reads[i], reads[j])
            if sp == "within":
                continue
            seen = True
            cen.bump(cen.pairs, sp)
            if sp == "class":
                p, q = reads[i][0], reads[j][0]
                if reads[i][1] or reads[j][1]:
                    cen.class_seated += 1
                elif R.deg[p] > L.g:
                    cen.class_above += 1
                else:
                    cen.class_below += 1
            if not certify:
                continue
            v1, v2 = ties[i], ties[j]
            # DOMINATION first: one side is enough. If choosing v1 leaves
            # v2's core dominated, that core is unseated forever in the one
            # branch and seated in the other, so the limits differ -- what
            # the other branch does to v1's core is a second reason, never a
            # requirement.
            d1, _ = dominated(L, world, st, v1, reads[j][0])
            d2, _ = dominated(L, world, st, v2, reads[i][0])
            verdict = rejoins(L, world, st, v1, v2)
            if d1 or d2:
                ok(verdict != "rejoin",
                   "%s/%s: a pair both rejoins and starves a core" % (L.name,
                                                                      world))
                cen.bump(cen.dom, "two-sided" if d1 and d2 else "one-sided")
                verdict = "choice"
                certified = True
            elif verdict == "not-minimal":
                verdict = ("rejoin-delayed"
                           if meets(L, world, st, v1, v2, BFS_BUDGET, BFS_CAP)
                           else "undecided")
            cen.bump(cen.verdict, (sp, verdict))
            if sp not in cen.spec:
                cen.spec[sp] = "%s/%s at %s: %s vs %s -> %s" % (
                    L.name, world, L.mod.fmt_state(R, st),
                    L.mod.fmt_state(R, v1), L.mod.fmt_state(R, v2), verdict)
    if seen:
        cen.cross += 1
    if certified:
        # The formula's factor at this opening against what is PROVED to
        # survive it. A certified pair gives two limits, so an opening the
        # formula scores 1 is an opening it is blind at.
        cen.certified_ties += 1
        if f == 1:
            cen.blind += 1


# --------------------------------------------------------------- S1 control
def s1a_ladder(ladder):
    print("  (a) the ladder through this rig's entry points")
    print("      ring       h   g   minrep degrees")
    for L in ladder:
        degs = sorted(set(L.m(c) for c in range(L.R.h)))
        for c in range(L.R.h):
            ok(L.m(c) <= L.g,
               "%s: class %d has a minimal representative above the genus"
               % (L.name, c))
        print("      %-10s %-3d %-3d %s" % (L.name, L.R.h, L.g, degs))


def s1b_classifier(ladder):
    """Synthetic pairs built to order, one per species."""
    print("  (b) the species classifier on synthetic pairs")
    L = ladder[-1]                                  # the genus-2 ring
    R = L.R
    mk = lambda pl, e, r, k: (pl, e, r, k)
    d1 = R.by_deg[1]
    ok(len(d1) >= 2, "g2: too few degree-1 places to build the pairs")
    same_cls, diff_cls = None, None
    for d in range(2, 9):
        pls = R.by_deg.get(d, [])
        for i in range(len(pls)):
            for j in range(i + 1, len(pls)):
                if R.cls[pls[i]] == R.cls[pls[j]] and same_cls is None:
                    same_cls = (pls[i], pls[j])
                if R.cls[pls[i]] != R.cls[pls[j]] and diff_cls is None:
                    diff_cls = (pls[i], pls[j])
    ok(same_cls is not None and diff_cls is not None,
       "g2: no degree carries both a repeated and a split class")
    d3 = list(diff_cls)
    cases = [
        ("within", mk(same_cls[0], 0, 1, "fresh"), mk(same_cls[1], 0, 1, "fresh")),
        ("class", mk(diff_cls[0], 0, 1, "fresh"), mk(diff_cls[1], 0, 1, "fresh")),
        ("depth", mk(d3[0], 0, 5, "clocked"), mk(d3[1], 2, 3, "deepen")),
        ("odd-even", mk(d3[0], 0, 1, "fresh"), mk(d1[0], 1, 3, "deepen")),
        ("even-even", mk(d3[0], 0, 3, "clocked"), mk(d1[0], 1, 9, "deepen")),
        ("odd-odd", mk(d3[0], 0, 1, "fresh"), mk(d1[0], 0, 1, "fresh")),
    ]
    for want, a, b in cases:
        got = species(L, "element", a, b)
        ok(got == want, "the classifier called a %s pair %s" % (want, got))
        print("      %-10s ok" % want)
    ok(species(L, "ideal", *cases[1][1:]) == "within",
       "the ideal world read a class split")
    print("      the ideal world reads the class split as within-type: ok")


def s1c_rejoin(ladder):
    """A planted commuting pair and a planted non-commuting one."""
    print("  (c) the rejoin detector")
    hits, miss = 0, 0
    for L in ladder:
        for world in ("ideal", "element"):
            for st, dg in CT.eff_divisors(L, 3):
                try:
                    lam, cost, ties = menu_of(L, world, st)
                except AssertionError:
                    continue
                if len(ties) < 2:
                    continue
                reads = [core_of(L, world, st, v, lam) for v in ties]
                for i in range(len(ties)):
                    for j in range(i + 1, len(ties)):
                        got = rejoins(L, world, st, ties[i], ties[j])
                        if species(L, world, reads[i], reads[j]) == "within":
                            miss += got == "not-minimal"
                            continue
                        hits += got == "rejoin"
    ok(hits > 0, "the detector reports no rejoin anywhere, so its zeros are "
       "not evidence")
    ok(miss > 0, "the detector reports a rejoin at every pair it sees, so "
       "its hits are not evidence")
    print("      %d rejoins found and %d within-type pairs refused: both "
          "directions live" % (hits, miss))


def s1d_domination(ladder):
    """A starved core must be reported dominated; a fresh one must not."""
    print("  (d) the domination detector")
    L = next(x for x in ladder if x.name == "h5")
    R = L.R
    d4 = R.by_deg[4]
    ok(len(d4) >= 2, "h5: degree 4 does not carry two places")
    st = {d4[0]: 3}
    good, why = dominated(L, "ideal", st, {d4[0]: 2}, d4[1])
    ok(good, "the detector missed a starved core: %s" % why)
    st2 = {R.by_deg[1][0]: 2}
    bad, why2 = dominated(L, "ideal", st2, {R.by_deg[1][0]: 1}, d4[0])
    ok(not bad, "the detector called an unstarved core dominated")
    print("      starved core: dominated (%s)" % why)
    print("      unstarved core: not dominated (%s)" % why2)
    # the passenger route, which the forward check caught being left open
    p1 = R.by_deg[1]
    rid, why3 = dominated(L, "element", {p1[0]: 3}, {p1[0]: 2}, p1[1])
    ok(not rid, "the detector certified a core a rider can carry back")
    half, _ = dominated(L, "element", {p1[0]: 3}, {p1[0]: 2}, p1[1],
                        passenger=False)
    ok(half, "the core route is not shut at a starved rational point, so "
       "the passenger test is not what the refusal is testing")
    print("      ridable core: not dominated (%s)" % why3)


# ----------------------------------------------------------- S2/S3/S4 scan
def scan(L, world, cap):
    cen = Census()
    for st, dg in CT.eff_divisors(L, cap):
        try:
            lam, cost, ties = menu_of(L, world, st)
        except AssertionError:
            continue
        cen.states += 1
        if len(ties) < 2:
            continue
        cen.ties += 1
        classify_state(L, world, st, lam, cost, ties, cen)
    return cen


def report(name, cen):
    order = ["class", "depth", "odd-even", "even-even", "odd-odd"]
    pairs = " ".join("%s=%d" % (k, cen.pairs[k]) for k in order
                     if k in cen.pairs)
    # A skipped tie state is a WIDE one, which is the opposite of a
    # harmless sample, so the count is printed beside the census it thins.
    skip = ("" if not cen.pair_skipped
            else "  [%d states past the pair cap]" % cen.pair_skipped)
    print("  %-8s %-7d %-6d %-6d %s%s" % (name, cen.states, cen.ties,
                                          cen.cross, pairs or "(none)", skip))


def totals(table, ladder, world):
    """The per-species verdict totals over the whole ladder. Printed rather
    than left to be added up by hand off the per-ring rows."""
    agg = {}
    for L in ladder:
        for (s, v), n in table[(L.name, world)].verdict.items():
            agg[(s, v)] = agg.get((s, v), 0) + n
    order = ["class", "depth", "odd-even", "even-even", "odd-odd"]
    out = []
    for sp in order:
        row = [(v, n) for (s, v), n in sorted(agg.items()) if s == sp]
        if row:
            out.append("%s: %s (%d)" % (sp, ", ".join("%s %d" % r for r in row),
                                        sum(n for _, n in row)))
    return out


def verdict_table(cen):
    order = ["class", "depth", "odd-even", "even-even", "odd-odd"]
    out = []
    for sp in order:
        row = [(v, n) for (s, v), n in sorted(cen.verdict.items()) if s == sp]
        if row:
            out.append("%s: %s" % (sp, ", ".join("%s %d" % r for r in row)))
    return out


# ------------------------------------------------------------ S5 walks
def walk(L, world, seed, T):
    """One canonical trajectory; returns the states, menus and moves."""
    st, out = dict(seed), []
    for _ in range(T):
        try:
            lam, cost, ties = menu_of(L, world, st)
        except AssertionError:
            TRUNC["walk-short"] += 1
            break
        out.append((dict(st), lam, cost, ties))
        st = EC.apply_veh(st, ties[0])
    return out


def main():
    ladder = CT.build_ladder()

    section("S1  THE POSITIVE CONTROL")
    s1a_ladder(ladder)
    s1b_classifier(ladder)
    s1c_rejoin(ladder)
    s1d_domination(ladder)

    cens = {}
    for world in ("ideal", "element"):
        section("S2  THE EXHAUSTIVE REGION, %s world" % world.upper())
        print("  ring     states  ties   cross  cross-type pairs by species")
        for L in ladder:
            cen = scan(L, world, SCAN_DEG[L.name])
            cens[(L.name, world)] = cen
            report(L.name, cen)
            if world == "ideal":
                ok("class" not in cen.pairs,
                   "%s: a CLASS pair in the ideal world" % L.name)
                ok("odd-odd" not in cen.pairs,
                   "%s: an ODD-ODD pair in the ideal world" % L.name)
                ok("depth" not in cen.pairs,
                   "%s: a DEPTH pair in the ideal world, where two exponents "
                   "at one degree cannot cost the same" % L.name)

    section("S3  THE CERTIFICATES")
    print("  ring     world    CLASS pairs: above g / below g / seated cores")
    for L in ladder:
        for world in ("ideal", "element"):
            cen = cens[(L.name, world)]
            if not (cen.class_above or cen.class_below or cen.class_seated):
                continue
            print("  %-8s %-8s %d / %d / %d"
                  % (L.name, world, cen.class_above, cen.class_below,
                     cen.class_seated))
    print()
    print("  ring     world    verdicts by species")
    for L in ladder:
        for world in ("ideal", "element"):
            cen = cens[(L.name, world)]
            for line in verdict_table(cen):
                print("  %-8s %-8s %s" % (L.name, world, line))
    print()
    for world in ("ideal", "element"):
        for line in totals(cens, ladder, world):
            print("  TOTAL    %-8s %s" % (world, line))
    print()
    for L in ladder:
        for world in ("ideal", "element"):
            d = cens[(L.name, world)].dom
            if d:
                print("  %-8s %-8s domination: %s" % (L.name, world,
                      ", ".join("%s %d" % kv for kv in sorted(d.items()))))
    print()
    for L in ladder:
        cen = cens[(L.name, "element")]
        if cen.fresh:
            print("  %-8s element fresh vehicles: %d, of which %d move the "
                  "clock through the rider" % (L.name, cen.fresh,
                                               cen.riderclock))

    section("S4  THE WIDTHS -- what the formula multiplies against what "
            "survives")
    print("  ring     world    within-type width   lambda-width")
    for L in ladder:
        for world in ("ideal", "element"):
            cen = cens[(L.name, world)]
            if not cen.ties:
                continue
            print("  %-8s %-8s %-19s %s"
                  % (L.name, world,
                     dict(sorted(cen.fine.items())),
                     dict(sorted(cen.coarse.items()))))

    section("S5  THE TRAJECTORY REGION")
    print("  ring     world    states  ties  cross  pairs by species")
    walked = {}
    for L in ladder:
        for world in ("ideal", "element"):
            cen = Census()
            seeds = [{}] + [dict(v) for v, _ in CT.eff_divisors(L, SEED_DEG)
                            if v]
            for seed in seeds:
                for st, lam, cost, ties in walk(L, world, seed, WALK_T):
                    cen.states += 1
                    if len(ties) < 2:
                        continue
                    cen.ties += 1
                    classify_state(L, world, st, lam, cost, ties, cen)
            walked[(L.name, world)] = cen
            report("%s/%s" % (L.name, world[0]), cen)
    print()
    print("  ring     world    verdicts by species (trajectory region)")
    for L in ladder:
        for world in ("ideal", "element"):
            for line in verdict_table(walked[(L.name, world)]):
                print("  %-8s %-8s %s" % (L.name, world, line))
    for world in ("ideal", "element"):
        for line in totals(walked, ladder, world):
            print("  TOTAL    %-8s %s" % (world, line))
    for L in ladder:
        for world in ("ideal", "element"):
            d = walked[(L.name, world)].dom
            if d:
                print("  %-8s %-8s domination: %s" % (L.name, world,
                      ", ".join("%s %d" % kv for kv in sorted(d.items()))))
    print()
    print("  ring     world    within-type width   lambda-width")
    for L in ladder:
        for world in ("ideal", "element"):
            cen = walked[(L.name, world)]
            if not cen.ties:
                continue
            print("  %-8s %-8s %-19s %s"
                  % (L.name, world, dict(sorted(cen.fine.items())),
                     dict(sorted(cen.coarse.items()))))

    section("S6  THE FORWARD CHECK -- a starved core along the walk")
    print("  The certificate shuts TWO routes. Following the canonical")
    print("  continuation separates them: a core off the rider set must")
    print("  never come back, and one on it is where the returns live.")
    print("  ring     world    certified / back    core-route only / back")
    for L in ladder:
        for world in ("ideal", "element"):
            full, full_back, half, half_back, skipped = 0, 0, 0, 0, 0
            seeds = [{}] + [dict(v) for v, _ in CT.eff_divisors(L, SEED_DEG)
                            if v]
            for seed in seeds:
                for st, lam, cost, ties in walk(L, world, seed, WALK_T):
                    if len(ties) < 2:
                        continue
                    reads = [core_of(L, world, st, v, lam) for v in ties]
                    n = len(ties)
                    if n * (n - 1) // 2 > PAIR_CAP:
                        skipped += 1
                        continue
                    for i in range(n):
                        for j in range(i + 1, n):
                            if species(L, world, reads[i], reads[j]) != "class":
                                continue
                            core = reads[j][0]
                            half_ok, _ = dominated(L, world, st, ties[i], core,
                                                   passenger=False)
                            if not half_ok:
                                continue
                            full_ok, _ = dominated(L, world, st, ties[i], core)
                            _, when = forward_unseated(L, world, st, ties[i],
                                                       core, FORWARD_T)
                            if full_ok:
                                full += 1
                                full_back += when is not None
                            else:
                                half += 1
                                half_back += when is not None
            if full or half:
                print("  %-8s %-8s %-4d / %-11d %-4d / %-4d %s"
                      % (L.name, world, full, full_back, half, half_back,
                         "" if not skipped
                         else "(%d states past the pair cap)" % skipped))
                ok(full_back == 0, "%s/%s: a core the certificate covers was "
                   "seated later" % (L.name, world))

    section("S7  WHERE THE FORMULA IS BLIND")
    print("  Openings carrying a CERTIFIED choice, and how many of those the")
    print("  within-type width scores 1 -- a factor of 1 where two limits")
    print("  are proved.")
    print("  ring     world    region       certified openings  scored 1")
    for tag, table in (("exhaustive", cens), ("trajectory", walked)):
        for L in ladder:
            for world in ("ideal", "element"):
                cen = table[(L.name, world)]
                if not cen.certified_ties:
                    continue
                print("  %-8s %-8s %-12s %-19d %d"
                      % (L.name, world, tag, cen.certified_ties, cen.blind))

    section("SPECIMENS")
    for (name, world), cen in sorted(cens.items()):
        for sp in sorted(cen.spec):
            print("  %-10s %s" % (sp, cen.spec[sp]))

    print()
    print("  where the search stopped short: %s" % TRUNC)
    print("  (a reach truncation can only HIDE a rejoin and a short walk")
    print("  only shortens the trajectory region; neither can "
          "manufacture a verdict, so both are reported)")
    print("\n%d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
