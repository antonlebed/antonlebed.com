"""explore_coarse_type.py -- is the type the greedy image is COUNTED with the
type the factoring theorem is PROVED for?

THE QUESTION. The greedy image over a function field is a product, over a
trajectory's surviving openings, of the tie multiplicity at each. That the
product FACTORS -- that the multiplicity at a later opening does not depend
on the choice made at an earlier one -- is a theorem, and the theorem is
about a REFINED type: colour a place by (degree, class) and refine the
colour by the state depth, and two tie members of one refined type generate
isomorphic subtrees (explore_greedy_image_g2.py lemma G). But every
multiplicity the corpus has MEASURED was taken with a COARSE type, (degree,
class, exponent), which does not carry the depth. If a tie set can ever hold
two members of one coarse type at two different depths -- a COLLISION -- the
measured multiplicity is taken across branches the theorem does not cover,
and the correction has lineage into every ring already run.

The collision is known to need a core exponent ABOVE the bare door, because
at a bare door the exponent determines the depth. Whether such an OFFSET
vehicle can enter a tie set at all was left open: at genus 2 all 1550
element tie members reconstructed at offset 0, which makes that census
evidence about the offsets and not about the collision.

THIS RIG ATTACKS THE COLLISION DIRECTLY, and the offset question comes back
as a separate observable rather than as the proxy. The two are not
equivalent: a collision needs two DISTINCT places wearing one colour where
an offset needs only one place and a cooperative class, so the offset is the
weaker condition and a zero in it would prove more than it was asked to.
(Lemma S below settled the offset outright, in the direction the freeze
thought least likely -- so the separation was worth making, and not for the
reason it was made.)

THE SETTING. The function-field ladder the greedy image was measured over,
six rings, with their engines imported rather than re-implemented: F_2[x]
(genus 0) and the q = 2 elliptic ladder h = 1..5 from
explore_greedy_image_ec.py, and the genus-2 ring y^2 + y = x^5 + x from
explore_greedy_image_g2.py. Both worlds of each. Where those two scripts
census the states their TRAJECTORIES visit, this one enumerates states
EXHAUSTIVELY -- every effective divisor up to a degree cap -- which is what
turns "did not occur" into "cannot occur in this region".

TRANSPLANT FLAGS, fixed at the freeze. Every intuition below is imported
from a neighbouring parameter value and is marked rather than trusted.
 1. From the trajectory censuses: "no offset vehicle enters a tie set."
    That is a statement about the states the greedy walks through. It is
    NOT carried; the exhaustive scan is run precisely because the greedy
    visits a thin set.
 2. From genus 2: "the rider has degree at most 2." Re-derived below as
    "at most g" and CHECKED per ring rather than carried, since the
    elliptic rings and F_2[x] have their own g.
 3. From the ideal world: "the door determines the depth, so no two depths
    share an exponent." True there because the ideal menu has no offsets at
    all; the element world offers r+1..r+g and the argument is redone.
 4. From the function fields to the number rings: NOTHING is carried. The
    number-ring element engine enumerates elements by norm and has no genus;
    its analogue of lemma R below would bound the offset by the largest
    minimal class-representative NORM, and that transfer is left open and
    named rather than assumed here.

THE HAND-ATTACK, on paper before any engine code. Write d = deg P, e = the
depth of P at the state, kappa = v2(lambda), c = cls P, and m(x) for the
degree of the minimal effective AFFINE representative of the class x, so
m(0) = 0. A vehicle in the element world is complete(P, n) = P^n plus the
minimal representative of the class it must cancel, of cost d*n + m(-n*c).
Its OFFSET is j = n - door(P, e).

 L1 THE DOOR IS 2^kappa + 1 - e AT EVERY PLACE OF A SEATED DEGREE. For
    e >= 1 the door search gives r = 2^kappa + 1 - e, and e <= 2^kappa
    always, since lambda already carries 2^ceil(log2 e). For e = 0 at a
    degree that already carries a seated place, (2^d - 1) divides lambda,
    so the fresh place is CLOCKED at 2^kappa + 1 -- which is the same
    formula at e = 0. Hence two places of one degree at depths e and
    e + delta have doors differing by exactly delta, the deeper one
    CHEAPER, and a common exponent forces the deeper one to sit delta
    higher above its own door.
 L2 OFFSET ADMISSIBILITY. complete(P, r+j) is in the minimal tie set only
    if it is no dearer than complete(P, r), which is also in the menu:
       d*j <= m(-r*c) - m(-(r+j)*c) <= g.
    So d*j <= g. At genus 0 every m is 0 and j = 0 is forced; at genus 1
    only (d, j) = (1, 1) survives the cost test; at genus 2 only (1,1),
    (1,2) and (2,1) do. Surviving the cost test is not occurring: lemma S
    below shows what the equality case of this inequality actually is.
    The same inequality shows the menu is COMPLETE at offsets 0..g: an
    exponent j above the door costs at least j and can save at most g.
 L3 A COLLISION NEEDS TWO DISTINCT PLACES OF ONE DEGREE AND ONE CLASS.
    Equal coarse multisets with unequal refined multisets means some coarse
    triple (d, c, n) whose depth refinements differ, hence places P in one
    member and P' in the other with the same degree, the same class and the
    same exponent but different depths -- so P != P'.
 L4 AND THAT PAIR CANNOT EXIST ABOVE THE GENUS. Every rider place lies in
    the support of a minimal representative, hence has degree at most g.
    If either of P, P' is a rider then d <= g. If both are cores then L1
    puts the deeper at offset j + delta with delta >= 1, and L2 gives
    d*(j + delta) <= m(-r'*c) - m(-n*c), so d <= m(-r'*c) <= g and c != 0,
    since m vanishes on the trivial class. Every case therefore needs
    d <= g.
 R  THE GATE. Let D be the least degree at which two DISTINCT places share
    a class. If D > g, no tie set in either world holds two members
    of one coarse type at two different depths: the coarse type IS the
    factoring type and the measured multiplicity is the proved one. (This
    lemma was frozen as "D+ > g" for D+ the least degree at two distinct
    places of one NONZERO class, which is weaker than its own case
    analysis supports: only case A above forces c != 0, and cases B and C
    admit the trivial class. The rig asserts the stronger D > g, and the
    printed D+ survives as the quantity governing case A alone -- which
    lemma S closes without any gate.) In the
    IDEAL world the menu is bare doors only, so delta = 0 is forced by L1
    and the conclusion holds with no hypothesis at all.
    Two distinct places of one degree in one class means P ~ P', i.e. the
    curve carries a pencil of degree d <= g with two IRREDUCIBLE rational
    fibres -- in ANY class, the trivial one included, which is how F_2[x]
    sits one degree above its own genus. That is what a ring would have to
    supply to break the coarse type, and it is a statement about
    low-degree pencils rather than about the dynamics.
    AND IT ALSO BREAKS LEMMA S, which is why the two hypotheses are one
    design target rather than two: l(D) >= 2 at degree d <= g is exactly
    a class with two minimal representatives. Neither is easy to supply.
    An IMAGINARY hyperelliptic model blocks d = 2 outright: every fibre of
    x is linearly equivalent to 2O, so the degree-2 pencil sits in the
    TRIVIAL class, whose minimal affine representative is the empty
    divisor and which summons no rider. Genus 3 blocks d = 3: at degree 3
    on a genus-3 curve l(D) = 1 + l(K - D), so l(D) >= 2 forces
    D ~ K - P for a rational point P, and hyperelliptically
    K - P ~ g^1_2 + iota(P) -- a pencil with iota(P) as a BASE point, so
    every member contains a rational point and none is irreducible. A
    break therefore wants a pencil of degree at most g that is neither the
    hyperelliptic one nor forced to carry a base point, which puts the
    first honest candidate at genus 4 or above.

 S  THE OFFSET NEVER PAYS -- derived AFTER the run, as the diagnosis of the
    zero PR5 called a kill, and certified rather than assumed by the
    section the run then grew. minrep(-(r+j)c) + j*P is effective, affine,
    and of class -(r+j)c + j*c = -r*c, so it is a representative of the
    class the BARE door must cancel and
       m(-r*c) <= m(-(r+j)*c) + d*j,
    which is L2's inequality with the sign it actually has: the bare door
    is never dearer than any offset, at any genus, on any ring where every
    class HAS a minimal effective affine representative -- which is the
    only hypothesis, and S1 enumerates it. If
    minimal representatives are UNIQUE, equality forces
    minrep(-r*c) = minrep(-(r+j)*c) + j*P and hence
    complete(P, r+j) = complete(P, r) AS DIVISORS. So an offset vehicle is
    never a NEW member of a tie set: the tie set is exactly the bare-door
    vehicles, and L1 then gives the core-core half of R outright, with no
    gate. What R's gate is still needed for is the RIDER half.

THE OBSERVABLE. Per ring, per world, over an exhaustive enumeration of
states: the tie sets, their partition by coarse type against their partition
by refined type, and the offset of every tie member. A collision is a coarse
class holding two refined classes. Because the enumeration covers states no
trajectory need reach, a ZERO here is stronger than a trajectory zero and a
HIT is weaker -- so every hit is reported with the DEGREE of the state it
occurs at, the region reaching well past the degree-3 seeds the filed
censuses start from.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE DOOR CLOSED FORM (L1). What the rig PRINTS: doors searched against
    2^kappa + 1 - e at every place of a degree that already carries a seated
    place, including the fresh ones, and the disagreement count.
    KILL: one disagreement.
PR2 THE RIDER BOUND. What the rig PRINTS: per ring, the number of minimal
    representatives per class, their degrees, and the greatest degree of a
    place in any minimal representative's support, against g.
    KILL: a class with no minimal representative in range, a minimal
    representative of degree above g, or a rider place of degree above g.
PR3 THE GATE (R). What the rig PRINTS: per ring, g, the least degree D at
    which two distinct places share ANY class, and the least degree D+ at
    which they share a NONZERO class, both by exhaustive enumeration over
    the whole place universe rather than only up to g -- so the margin is
    printed and not assumed.
    KILL: a ring with D <= g. (Frozen as "D+ <= g"; corrected to the
    stronger D at audit, with lemma R, and the rig asserts D throughout.)
PR4 NO COLLISION, EXHAUSTIVELY. Over every state of degree <= the cap, both
    worlds, all six rings: zero tie sets whose coarse-type partition is
    coarser than their refined-type partition.
    KILL: one collision.
PR5 OFFSET TIE MEMBERS EXIST OFF GENUS 0 AND CANNOT EXIST AT GENUS 0. L2
    forces j = 0 when every m is 0, so F_2[x] must print zero; off genus 0
    the inequality is satisfiable and the prediction is that the exhaustive
    scan FINDS at least one offset tie member somewhere on the ladder --
    which no trajectory census ever did. What the rig PRINTS: per ring per
    world, the offset histogram over tie members, and a specimen state for
    the least offset found.
    KILL: an offset tie member in F_2[x], which kills L2; or zero offset tie
    members anywhere, which would leave the trajectory zero unexplained and
    send the question back to the desk.
PR6 THE CENSUS, printed and not predicted: states enumerated, tie states,
    multiplicity histogram, how many tie sets straddle two degrees, and how
    many hold two coarse types at all -- the cross-type count, which is the
    OTHER open residual of the product formula and is measured here only
    because the same scan produces it.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE OFFSET IS NEVER A NEW VEHICLE, AND THAT IS A PROOF (proved, lemma S;
   certified 124754 times, 13512 of them at equal cost). The element menu
   offers core exponents r..r+g because a cheaper completion could in
   principle repay the extra degree. It never can: minrep(-(r+j)c) + j*P is
   an effective affine representative of the class the bare door must
   cancel, so m(-rc) <= m(-(r+j)c) + d*j and the bare door is no dearer
   than any offset -- at every genus, and on any ring where every class
   HAS a minimal effective affine representative, which is the only
   hypothesis and which S1 enumerates at all six. Where
   minimal representatives are unique, which they are at every ring here,
   the equality case forces the two vehicles to be the SAME DIVISOR. So a
   tie set is exactly the set of bare-door vehicles, and the r+1 / r+2
   entries of explore_greedy_image_ec.py and explore_greedy_image_g2.py are
   provably redundant: correct, complete, and never once the source of a
   member. The certificate exhibits the witness divisor and re-derives its
   class and degree rather than trusting the identity.

F2 SO THE COARSE TYPE IS THE FACTORING TYPE, AT EVERY RING ON THE LADDER
   (proved, lemma R with lemma S; 44484 state-menus, 0 collisions). The
   factoring theorem is about a colouring that carries the state depth; the
   corpus's measured multiplicities were taken with one that does not, and
   the gap could only open through a core above the bare door. Lemma S
   closes that route outright. What is left is the RIDER route -- a
   colliding pair needs two DISTINCT places of one degree and one class,
   and a rider place lies in a minimal representative, hence has degree at
   most g -- and the gate closes that: the least degree at which two
   distinct places share a class is 1, 2, 5, 5, 6 and 6 against genus 0, 1,
   1, 1, 1 and 2 -- margins of 1, 1, 4, 4, 5 and 4. The gate is thin at the
   TWO ENDS of the ladder and nowhere between: at F_2[x], where every place
   carries the trivial class and the two degree-1 places share it, and at
   the h = 2 ring, where two degree-2 places share a nonzero class. Each
   clears its genus by exactly one degree.
   The genus-2 census that first asked this question printed a zero from a
   mechanism that never fired; the zero is now a theorem, and it covers all
   six rings at once rather than the one it was measured on.

F3 AND THE PREDICTION THAT CARRIED THE RISK LOST, WHICH IS HOW THE PROOF
   ARRIVED. PR5 predicted that offset tie members EXIST off genus 0,
   reasoning from L2's inequality being satisfiable; the exhaustive scan
   printed zero at all six rings, which is PR5's own named kill. The
   diagnosis is that L2 was read with the wrong sign: its equality case is
   not a coincidence to be hunted but the merge itself. The first form of
   the offset-detector control died with the prediction -- it hand-built
   complete(P, door + 1) and asked the reader to return 1, which on a ring
   with unique minimal representatives is unaskable -- and was rebuilt on a
   DOCTORED ring, one class given a deliberately non-minimal representative,
   where the reader must and does return j. A control that a theorem makes
   unsatisfiable is not a control, and the replacement is the one the
   headline zero needs.

F4 THE WITHIN-TYPE MULTIPLICITY IS BOUGHT BY DEPTH, NOT BY GEOGRAPHY
   (observation, exhaustive in range; an unfrozen find). Over every state
   of degree at most 9 to 11, and across the five rings that HAVE classes,
   the element world's within-type width is at most 2 and is exactly 1 at
   6038 of their 6195 tie states -- at h = 5, at all 1299 of them.
   (Class-blind F_2[x] is excluded on both counts and reaches 3, its coarse
   type being one datum poorer.) The same rings'
   TRAJECTORY censuses reach within-type widths up to 335 in the element
   world and 1160 in the ideal one across the elliptic ladder, and 8 and
   180 at genus 2 -- two to three orders of magnitude above anything the
   exhaustive shallow region contains. The exhaustive region is shallow by
   construction and the trajectories are deep, and that is the whole of the
   difference: a wide within-type tie needs many places of one degree
   already clocked to one door, which only depth supplies. So the factor
   the product formula multiplies is not read off the place geography.

F5 AND THE ONE RISK LEFT IS NOT A CORRECTION TERM, IT IS THE MAIN TERM
   (observation, exhaustive in range). In the element world, and again at
   the five rings that HAVE classes, essentially every tie in the region
   is CROSS-type: 1299 of 1299 at h = 5, 1122 of 1122 at genus 2, 1610 of
   1610 at h = 4, 1305 of 1305 at h = 3, and 784 of 859 at h = 2.
   Class-blind F_2[x] again sits apart at 882 of 1654, and for the same
   reason as in F4: with one datum fewer, its coarse type merges what the
   others separate, so more of its raw width survives as within-type. The
   two findings are one fact seen twice -- what the CLASS buys the engine
   is the ability to call a tie two moves rather than one.
   The reading that a cross-type decline is a REORDERING
   rather than a choice therefore discards almost the
   entire raw tie width at almost every opening in this region. Whatever
   the product formula counts, it is not counting most of what the menu
   offers, and the step that throws the rest away has never been tested
   against the object it is about.
   SINCE TESTED, AND IT IS HALF WRONG: a cross-type pair splits by whether
   its two cores share a DEGREE. Cross-degree is a reordering; the same
   degree in two CLASSES is a CHOICE above the genus, each core starving
   the other. So the width discarded here is discarded correctly only in
   part, and the count is a sum over class-branches of products
   (explore_reordering.py). (SINCE WIDENED: cross-degree is a reordering
   only where one member is FRESH; two clock moves at different degrees are
   a choice as well, so the sum runs over TYPES rather than classes and the
   correction reaches the ideal world -- explore_undercut.py.)

THE DESIGN, in five sections after the control.

 S1 THE POSITIVE CONTROL, run before any census is read.
    (a) The imported rings are built and their own class-group and
        Riemann-Roch checks re-run through this rig's entry points: every
        class has exactly one minimal affine representative and every
        representative degree is at most g (PR2).
    (b) THE DETECTOR CONTROL, the one this rig cannot do without: the
        headline is a ZERO, so the detector is handed a SYNTHETIC tie set
        holding two members of one coarse type at two different depths and
        must report a collision, and a second holding two members of one
        coarse type at one depth and must report none.
    (c) THE OFFSET-DETECTOR CONTROL, for the same reason -- a census that
        cannot see an offset cannot report their absence -- and in the form
        lemma S left it. On these rings complete(P, door + j) IS
        complete(P, door), so no offset can be hand-built to read back; the
        reader is exercised on a DOCTORED ring instead, one class given a
        deliberately non-minimal representative, where the offset vehicle
        really is a different divisor and the reader must return j. On the
        true ring the bare door must read as 0.
    (d) This rig's own completion against the imported one, so that the
        offsets are read with the engine's vehicle and not a paraphrase.
        DIRECTLY only for the genus-2 engine, whose completion is a module
        function; the other five keep theirs as a closure inside the menu
        and cannot be called. Those are covered end to end instead, in the
        scan: every tie member the engine builds is asserted rebuildable
        here as complete(core, door + j), so a completion that drifted
        would fail the scan rather than quietly read every member as
        unrecognised.
    (e) The brute door scan: at states within the cost cap, a full
        enumeration of effective divisors confirms the menu's tie set is
        exactly the set of minimal ticking divisors (PR1 and menu
        completeness at offsets 0..g).
 S2 THE GATE: the place geography of every ring -- places per degree,
    classes per degree, D, D+ and g (PR3).
 S3 THE EXHAUSTIVE SCAN, ideal world: every effective divisor to the cap,
    the tie census, the coarse/refined comparison (PR4) and the offsets
    (PR5).
 S4 THE EXHAUSTIVE SCAN, element world: the same, where the riders and the
    offsets live.
 S5 THE TABLE: per ring, g against D+, the scan's reach, the offsets found
    and the collisions found.
 S6 THE OFFSET CERTIFICATE, grown after the run to carry lemma S rather
    than to observe its consequence: at every scanned state, every core of
    degree up to the state's own menu cost, and every offset j >= 1, the
    witness divisor is re-derived, the bare door is asserted no dearer, and
    equal cost is asserted to mean the same divisor. A core dearer than the
    cost cannot tie, so that range is the whole competitive one, and the
    cap is set at the greatest cost the menus reach rather than below it --
    nothing is left uncertified. It runs inside S4 because it is a
    statement about the element menu at a state.

Run: `python explore_coarse_type.py`. RUN RECORD (1187454 checks, ~3.2 s).
S1 control: minimal representative degrees 1/4/10 at degrees 0/1/2 for genus
2 and one per nonzero class for the elliptic ladder, every one within the
genus and every rider place of degree at most g (widest 0, 1, 1, 1, 1, 2);
all 30 classes of the six rings enumerated to degree g, each with exactly
ONE minimal representative and each matching the one the ladder carries,
which is lemma S's merge hypothesis checked rather than inherited; a
planted collision found and an equal-depth pair and a singleton left clean; 6
doctored offsets read back at their own j with the bare door reading 0; 160
completions agreeing with the engine's own; 692 menus confirmed against a
full effective-divisor enumeration; and all 43149 tie members across both
scans rebuilt from their own core and door, which is what covers the five
engines whose completion cannot be called directly. S2 gate: D = 1, 2, 5, 5, 6, 6 and D+ =
none, 2, 5, 5, 6, 7 against g = 0, 1, 1, 1, 1, 2. S3 ideal world, 22242
state-menus: raw tie widths 2..7 over 8852 tie states, within-type widths
1..5, 872 tie states with no within-type choice at all. S4 element world,
same states: raw tie widths 2..6 over 7849 tie states, within-type widths
1..3, 6294 with no within-type choice, and 124754 lemma-S certificates of
which 13512 at equal cost and every one the same divisor, at every core the
menus can reach and with nothing left above the cap. 418203 doors read
against the closed form per world, no disagreement; greatest menu cost 4 in
the ideal world and 6 in the element one, against a place universe trimmed
to degree 12, so no place outside it could have tied and 0 states were
skipped for passing it. Slate PR1-PR6: PR1,
PR2, PR4 and PR6 hit; PR3 hit in a STRONGER form than it was frozen in, the
gate being asserted on D rather than the D+ the freeze wrote, since lemma
R's own case analysis needs the trivial class admitted; PR5's kill FIRED --
zero offset tie members anywhere -- and F1 is the diagnosis. Unfrozen
finds: lemma S itself, that
the within-type width is a depth phenomenon and not a geographic one (F4),
and that the cross-type reading carries nearly the whole raw tie width in
this region rather than a correction to it (F5).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_greedy_image_ec as EC       # the genus 0 and 1 rings
import explore_greedy_image_g2 as G2       # the genus 2 ring

# The imported engines size their place universe for the trajectory censuses
# they run; this rig's states are capped well below that, so the universe is
# trimmed to keep the build cheap. It still reaches far past every cost the
# menus quote and past every degree the gate below reports.
EC.DMAX = 12
G2.DMAX = 12

CHECKS = 0

SCAN_DEG = {"F_2[x]": 11, "h2": 10, "h3": 10, "h4": 10, "h5": 10, "g2": 9}
BRUTE_DEG = 4       # states at or below this degree get the full divisor scan
BRUTE_COST = 7      # and only when the menu's cost is at or below this
CERT_DEG = 6        # greatest core degree the offset certificate reaches


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------- the six rings
class Ladder(object):
    """One ring plus the two things this rig needs beyond the engines: the
    genus, and the minimal representative of a class as a divisor."""

    def __init__(self, name, R, mod, g, minrep):
        self.name = name
        self.R = R
        self.mod = mod
        self.g = g
        self.minrep = minrep          # class -> dict(place -> exponent)

    def cancel(self, c):
        """The minimal divisor whose class is -c: what a core of class c
        must carry to become principal."""
        return self.minrep[self.R.neg_class(c)]

    def complete(self, pl, n):
        veh = {pl: n}
        c = self.R.veh_class(veh)
        for q, e in self.cancel(c).items():
            veh[q] = veh.get(q, 0) + e
        return veh

    def m(self, c):
        return self.R.veh_deg(self.minrep[c])


def build_ladder():
    out = []
    curves = [("h2", EC.Curve(1, 1, 0, 0, 1), 2),
              ("h3", EC.Curve(0, 0, 1, 0, 0), 3),
              ("h4", EC.Curve(1, 0, 0, 0, 1), 4),
              ("h5", EC.Curve(0, 0, 1, 1, 0), 5)]
    P = EC.build_poly_ring(EC.DMAX)
    out.append(Ladder("F_2[x]", P, EC, 0, {0: {}}))
    for name, curve, h in curves:
        R = EC.build_curve_ring(name, curve, h, EC.DMAX)
        reps = {0: {}}
        for c in range(1, h):
            reps[c] = {R.rider[c]: 1}
        out.append(Ladder(name, R, EC, 1, reps))
    R = G2.build_ring(G2.DMAX)
    full = G2.minimal_reps(R)
    reps = {}
    for c in range(R.h):
        ok(c in full, "g2: class %d has no minimal representative in range" % c)
        ok(len(full[c][1]) == 1,
           "g2: class %d has %d minimal representatives" % (c, len(full[c][1])))
        reps[c] = full[c][1][0]
        R.minrep[c] = reps[c]
    out.append(Ladder("g2", R, G2, 2, reps))
    return out


# --------------------------------------------------------------- the types
def coarse_type(L, world, veh):
    """What the ENGINE reads about a vehicle: lambda reads the degree, and
    the element world reads the class through the principality test."""
    R = L.R
    return tuple(sorted((R.deg[pl], R.cls[pl] if world == "element" else -1, e)
                        for pl, e in veh.items()))


def refined_type(L, world, st, veh):
    """The factoring theorem's colouring: the coarse type plus the state
    depth at every place of the vehicle."""
    R = L.R
    return tuple(sorted((R.deg[pl], R.cls[pl] if world == "element" else -1, e,
                         st.get(pl, 0)) for pl, e in veh.items()))


def collisions(L, world, st, ties):
    """The coarse classes that hold two refined classes. A tie set is clean
    when the two partitions agree."""
    byc = {}
    for veh in ties:
        byc.setdefault(coarse_type(L, world, veh), set()).add(
            refined_type(L, world, st, veh))
    return [(k, v) for k, v in byc.items() if len(v) > 1]


def vkey(veh):
    return tuple(sorted(veh.items()))


def offset_of(L, world, st, veh, lam):
    """(j, core) for the least j with veh = complete(core, door + j), or
    (None, None). In the ideal world a vehicle is a bare single-place power
    and carries no completion, so the same reading applies with an empty
    rider. The core is returned rather than guessed from the weights: with a
    rider of degree g the heaviest term need not be the core."""
    R = L.R
    for j in range(L.g + 1):
        for pl in veh:
            r0 = R.door_r(pl, st.get(pl, 0), lam)
            cand = {pl: r0 + j} if world == "ideal" else L.complete(pl, r0 + j)
            if vkey(cand) == vkey(veh):
                return j, pl
    return None, None


# ------------------------------------------------------- state enumeration
def eff_divisors(L, cap):
    """Every effective divisor of degree 0..cap, the void included."""
    R = L.R
    pls = [pl for d in range(1, cap + 1) for pl in R.by_deg.get(d, [])]
    out = []

    def rec(i, cur, dg):
        out.append((dict(cur), dg))
        for j in range(i, len(pls)):
            pl = pls[j]
            dd = R.deg[pl]
            if dg + dd > cap:
                continue
            e, tot = 1, dg + dd
            while tot <= cap:
                cur[pl] = e
                rec(j + 1, cur, tot)
                e += 1
                tot += dd
            del cur[pl]

    rec(0, {}, 0)
    return out


# --------------------------------------------------------------- S1 control
def s1a_reps(ladder):
    """Every class has exactly one minimal affine representative, of degree
    at most g, supported on places of degree at most g (PR2). UNIQUENESS is
    the hypothesis lemma S's merge step rests on, so it is enumerated here
    at every ring rather than inherited from the source scripts' proofs:
    all effective divisors to degree g, grouped by class, must give one
    minimal per class and it must be the one the ladder carries."""
    print("  ring     h   g   minrep degrees        widest rider place")
    for L in ladder:
        R = L.R
        best = {}
        for div, dg in eff_divisors(L, L.g):
            c = R.veh_class(div)
            if c not in best or dg < best[c][0]:
                best[c] = (dg, [div])
            elif dg == best[c][0]:
                best[c][1].append(div)
        for c in range(R.h):
            ok(c in best, "%s: class %d has no effective representative of "
               "degree at most the genus" % (L.name, c))
            ok(len(best[c][1]) == 1, "%s: class %d has %d minimal "
               "representatives, so lemma S's merge step has no hypothesis"
               % (L.name, c, len(best[c][1])))
            ok(vkey(best[c][1][0]) == vkey(L.minrep[c]),
               "%s: the enumerated minimal representative of class %d is not "
               "the one the ladder carries" % (L.name, c))
        degs, wide = {}, 0
        for c in range(R.h):
            dg = L.m(c)
            ok(dg <= L.g, "%s: class %d has a minimal representative of "
               "degree %d above the genus" % (L.name, c, dg))
            degs[dg] = degs.get(dg, 0) + 1
            for pl in L.minrep[c]:
                wide = max(wide, R.deg[pl])
                ok(R.deg[pl] <= L.g, "%s: a rider place of degree %d"
                   % (L.name, R.deg[pl]))
        ok(degs.get(0, 0) == 1, "%s: the trivial class is not the only one "
           "of degree 0" % L.name)
        print("  %-8s %-3d %-3d %-21s %d"
              % (L.name, R.h, L.g, dict(sorted(degs.items())), wide))


def s1b_detector(ladder):
    """THE DETECTOR CONTROL. The headline is a zero, so the detector is fed
    a collision it must find and a near-miss it must not."""
    L = ladder[-1]
    R = L.R
    d = next(dd for dd in sorted(R.by_deg) if len(R.by_deg[dd]) >= 2)
    P, Q = R.by_deg[d][0], R.by_deg[d][1]
    hit = collisions(L, "ideal", {P: 2}, [{P: 3}, {Q: 3}])
    ok(len(hit) == 1, "the detector missed a planted collision")
    ok(len(hit[0][1]) == 2, "the planted collision reported %d refined types"
       % len(hit[0][1]))
    ok(not collisions(L, "ideal", {P: 2, Q: 2}, [{P: 3}, {Q: 3}]),
       "the detector fired on two members at one depth")
    ok(not collisions(L, "ideal", {P: 2}, [{P: 3}]),
       "the detector fired on a singleton")
    print("  planted collision found, equal-depth pair and singleton clean;")
    print("  the specimen was two degree-%d places at depths 2 and 0." % d)


def s1c_offset_detector(ladder):
    """THE OFFSET-DETECTOR CONTROL, in the form lemma S left it. A census
    that cannot see an offset cannot report their absence -- but on these
    rings complete(P, door + j) IS complete(P, door), so a hand-built offset
    is not available to read back. The reader is therefore exercised on a
    DOCTORED ring, one class given a deliberately non-minimal representative
    so that the offset vehicle really is a different divisor; the reader must
    return j there, and 0 on the true ring."""
    seen = 0
    for L in ladder:
        if L.g == 0:
            continue
        R = L.R
        P = R.by_deg[1][0]
        st = {P: 1}
        lam = R.lam_state(st)
        r0 = R.door_r(P, 1, lam)
        ok(offset_of(L, "element", st, L.complete(P, r0), lam) == (0, P),
           "%s: the reader missed the bare door" % L.name)
        for j in range(1, L.g + 1):
            reps = dict(L.minrep)
            c0 = R.neg_class(R.veh_class({P: r0 + j}))
            padded = dict(reps[c0])
            padded[P] = padded.get(P, 0) + R.h     # class h*c = 0: still a
            reps[c0] = padded                      # representative, not minimal
            D = Ladder(L.name + "*", R, L.mod, L.g, reps)
            veh = D.complete(P, r0 + j)
            ok(vkey(veh) != vkey(D.complete(P, r0)),
               "%s: the doctored ring did not separate offset %d"
               % (L.name, j))
            ok(offset_of(D, "element", st, veh, lam) == (j, P),
               "%s: the offset reader missed a doctored offset %d"
               % (L.name, j))
            seen += 1
    print("  %d doctored offsets read back at their own j, and the bare door"
          % seen)
    print("  read as 0, over the five rings of genus >= 1.")


def s1d_completion(ladder):
    """This rig's completion against the engine's, so that offsets are read
    with the engine's vehicle."""
    n = 0
    for L in ladder:
        if L.mod is not G2:
            continue
        R = L.R
        for d in sorted(R.by_deg):
            for pl in R.by_deg[d][:4]:
                for r in range(1, 5):
                    ok(vkey(L.complete(pl, r)) == vkey(G2.complete(R, pl, r)),
                       "%s: the completion disagrees with the engine's" % L.name)
                    n += 1
    print("  %d completions agree with the engine's own." % n)


def s1e_brute(ladder):
    """The full divisor enumeration behind the menu, which is also the check
    that offsets 0..g exhaust the minimal vehicles."""
    done = 0
    for L in ladder:
        for st, dg in eff_divisors(L, BRUTE_DEG):
            lam = L.R.lam_state(st)
            for world in ("ideal", "element"):
                cost, ties = L.mod.MENUS[world](L.R, st, lam)
                if cost > BRUTE_COST:
                    continue
                L.mod.scan_check(L.R, world, st, lam, cost, ties)
                done += 1
    print("  %d menus confirmed against a full effective-divisor "
          "enumeration." % done)


# ------------------------------------------------------------- S2 the gate
def s2_gate(ladder):
    print("  ring     g   places by degree 1..8            D    D+")
    gate = {}
    for L in ladder:
        R = L.R
        counts = [len(R.by_deg.get(d, [])) for d in range(1, 9)]
        D, Dp = None, None
        for d in sorted(R.by_deg):
            byc = {}
            for pl in R.by_deg[d]:
                byc.setdefault(R.cls[pl], []).append(pl)
            for c, group in byc.items():
                if len(group) >= 2:
                    if D is None:
                        D = d
                    if c != 0 and Dp is None:
                        Dp = d
        if D is not None:
            ok(D > L.g, "%s: two distinct places of degree %d share a class, "
               "at genus %d -- the rider route is open" % (L.name, D, L.g))
        gate[L.name] = (D, Dp)
        print("  %-8s %-3d %-32s %-4s %s"
              % (L.name, L.g, counts, D, "none" if Dp is None else Dp))
    return gate


# ----------------------------------------------------------- S3/S4 the scan
class Census(object):
    def __init__(self):
        self.states = 0
        self.skipped = []
        self.ties = 0
        self.sizes = {}
        self.crosstype = 0
        self.within = {}
        self.no_choice = 0
        self.members = 0
        self.offsets = {}
        self.off_spec = None
        self.coll = []
        self.doors = 0
        self.maxcost = 0
        self.certs = 0
        self.cert_eq = 0
        self.cert_skipped = 0


def certify_s(L, st, lam, cost, cen):
    """THE OFFSET CERTIFICATE, added after the run to carry lemma S rather
    than to observe its consequence. At every competitive place and every
    offset j >= 1: the bare door is no dearer, and where the costs are equal
    the two vehicles are the SAME divisor. The exhibited witness is
    minrep(-(r+j)c) + j*P, which the assert re-derives rather than trusts."""
    R = L.R
    if L.g == 0:
        return
    for d in range(1, min(cost, CERT_DEG) + 1):
        for pl in R.by_deg.get(d, []):
            r = R.door_r(pl, st.get(pl, 0), lam)
            base = L.complete(pl, r)
            for j in range(1, L.g + 1):
                up = L.complete(pl, r + j)
                witness = dict(L.cancel(R.veh_class({pl: r + j})))
                witness[pl] = witness.get(pl, 0) + j
                ok(R.veh_class(witness) ==
                   R.neg_class(R.veh_class({pl: r})) and
                   R.veh_deg(witness) == R.veh_deg(up) - d * r,
                   "%s: the witness divisor is not an effective "
                   "representative of the class the bare door must cancel"
                   % L.name)
                ok(R.veh_deg(base) <= R.veh_deg(up),
                   "%s: an offset-%d vehicle undercuts its own bare door"
                   % (L.name, j))
                if R.veh_deg(base) == R.veh_deg(up):
                    cen.cert_eq += 1
                    ok(vkey(base) == vkey(up),
                       "%s: an offset-%d vehicle ties its bare door as a "
                       "DIFFERENT divisor" % (L.name, j))
                cen.certs += 1
    if cost > CERT_DEG:
        cen.cert_skipped += 1


def scan(L, world, cap, cen):
    R = L.R
    menu = L.mod.MENUS[world]
    for st, dg in eff_divisors(L, cap):
        lam = R.lam_state(st)
        try:
            cost, ties = menu(R, st, lam)
        except AssertionError:
            cen.skipped.append(dg)
            continue
        cen.states += 1
        # The trimmed universe is only harmless while every menu cost stays
        # within it: a core of degree d costs at least d, so a place beyond
        # the cap can tie only at a cost beyond the cap.
        cen.maxcost = max(cen.maxcost, cost)
        ok(cost <= EC.DMAX if L.mod is EC else cost <= G2.DMAX,
           "%s/%s: a menu cost of %d passed the trimmed universe"
           % (L.name, world, cost))
        # PR1: the door closed form at every place of a seated degree
        kappa = EC.v2(lam)
        seatdeg = set(R.deg[pl] for pl, e in st.items() if e)
        for d in sorted(seatdeg):
            for pl in R.by_deg[d]:
                e = st.get(pl, 0)
                ok(R.door_r(pl, e, lam) == (1 << kappa) + 1 - e,
                   "%s/%s: the door at a degree-%d place of depth %d is not "
                   "2^%d + 1 - %d" % (L.name, world, d, e, kappa, e))
                cen.doors += 1
        if world == "element":
            certify_s(L, st, lam, cost, cen)
        if len(ties) < 2:
            continue
        cen.ties += 1
        cen.sizes[len(ties)] = cen.sizes.get(len(ties), 0) + 1
        cen.members += len(ties)
        kinds = {}
        for veh in ties:
            k = coarse_type(L, world, veh)
            kinds[k] = kinds.get(k, 0) + 1
            j, core = offset_of(L, world, st, veh, lam)
            # An unreadable member would land in the histogram as None and
            # the headline zero would then be a reader failure wearing a
            # result. It is also the cross-check of this rig's completion
            # against the FIVE engines whose own completion is a closure
            # and cannot be called directly: every tie member the engine
            # built must be rebuilt here from its core and its door.
            ok(j is not None, "%s/%s: a tie member this rig cannot rebuild "
               "as complete(core, door + j)" % (L.name, world))
            cen.offsets[j] = cen.offsets.get(j, 0) + 1
            if j:
                # L2 must hold at every offset the scan actually finds; the
                # ideal world has no rider to pay for one at all
                ok(world == "element", "%s: an offset-%d tie member in the "
                   "ideal world, where a vehicle carries no rider"
                   % (L.name, j))
                r0 = R.door_r(core, st.get(core, 0), lam)
                lo = L.m(R.neg_class(R.veh_class({core: r0})))
                hi = L.m(R.neg_class(R.veh_class({core: r0 + j})))
                ok(R.deg[core] * j <= lo - hi,
                   "%s/%s: an offset-%d tie member breaks the offset bound"
                   % (L.name, world, j))
                if cen.off_spec is None or j < cen.off_spec[0]:
                    cen.off_spec = (j, dg, L.mod.fmt_state(R, st), cost)
        if len(kinds) > 1:
            cen.crosstype += 1
        # what the product formula actually multiplies: the WITHIN-type
        # width, and how often the raw tie carries no within-type choice
        w = max(kinds.values())
        cen.within[w] = cen.within.get(w, 0) + 1
        if w == 1:
            cen.no_choice += 1
        bad = collisions(L, world, st, ties)
        if bad:
            cen.coll.append((dg, L.mod.fmt_state(R, st), bad[0]))
    return cen


def run_scan(ladder, world):
    print("  ring     cap  states  ties  raw   cross  within  no-choice  "
          "offsets")
    out = {}
    for L in ladder:
        cap = SCAN_DEG[L.name]
        cen = scan(L, world, cap, Census())
        out[L.name] = cen
        ok(cen.ties > 0, "%s/%s: the scan found no tie at all, so a zero "
           "below would be vacuous" % (L.name, world))
        offs = dict(sorted(cen.offsets.items(),
                           key=lambda kv: (kv[0] is None, kv[0])))
        print("  %-8s %-4d %-7d %-5d %-5s %-6d %-7s %-10d %s"
              % (L.name, cap, cen.states, cen.ties,
                 "%d..%d" % (min(cen.sizes), max(cen.sizes)), cen.crosstype,
                 "%d..%d" % (min(cen.within), max(cen.within)),
                 cen.no_choice, offs))
        if cen.skipped:
            print("           %d states skipped, the menu passing the "
                  "universe" % len(cen.skipped))
        if cen.certs:
            print("           lemma S: %d offset certificates, %d at equal "
                  "cost and every one" % (cen.certs, cen.cert_eq))
            print("           the same divisor (%d states above the "
                  "degree-%d core cap)" % (cen.cert_skipped, CERT_DEG))
        ok(not cen.coll, "%s/%s: a coarse-type collision at %s"
           % (L.name, world, cen.coll[:1]))
    return out


# ------------------------------------------------------------- S5 the table
def s5_table(ladder, gate, ideal, elem):
    print("  ring     g   D+     ideal states  elem states  offset members  "
          "collisions")
    toff, tcoll, tstates = 0, 0, 0
    for L in ladder:
        i, e = ideal[L.name], elem[L.name]
        off = sum(v for k, v in e.offsets.items() if k) + \
            sum(v for k, v in i.offsets.items() if k)
        coll = len(i.coll) + len(e.coll)
        toff += off
        tcoll += coll
        tstates += i.states + e.states
        print("  %-8s %-3d %-6s %-13d %-12d %-15d %d"
              % (L.name, L.g, "none" if gate[L.name][1] is None
                 else gate[L.name][1], i.states, e.states, off, coll))
    for world, cens in (("ideal", ideal), ("element", elem)):
        hist, ndoor = {}, 0
        for c in cens.values():
            ndoor += c.doors
            for w, n in c.sizes.items():
                hist[w] = hist.get(w, 0) + n
        print("  raw tie widths, %-8s %s" % (world, dict(sorted(hist.items()))))
        print("  doors read against the closed form: %d; greatest menu cost "
              "%d, against a" % (ndoor, max(c.maxcost for c in cens.values())))
        print("  trimmed universe of degree %d, so no place outside it could "
              "have tied" % EC.DMAX)
    print("\n  %d state-menus over six rings and two worlds; %d offset tie"
          % (tstates, toff))
    print("  members; %d collisions." % tcoll)
    spec = [e.off_spec for e in elem.values() if e.off_spec]
    if spec:
        j, dg, txt, cost = min(spec)
        print("  least offset found: j = %d at a degree-%d state %s, cost %d."
              % (j, dg, txt, cost))
    else:
        print("  no offset tie member anywhere in the scan.")


def main():
    section("S1  THE POSITIVE CONTROL -- run before any census is read")
    ladder = build_ladder()
    s1a_reps(ladder)
    s1b_detector(ladder)
    s1c_offset_detector(ladder)
    s1d_completion(ladder)
    s1e_brute(ladder)
    print("\n  Control green.")
    section("S2  THE GATE -- D+ against the genus, over the whole universe")
    gate = s2_gate(ladder)
    section("S3  THE EXHAUSTIVE SCAN -- ideal world")
    ideal = run_scan(ladder, "ideal")
    section("S4  THE EXHAUSTIVE SCAN -- element world")
    elem = run_scan(ladder, "element")
    section("S5  THE TABLE")
    s5_table(ladder, gate, ideal, elem)
    print("\nALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
