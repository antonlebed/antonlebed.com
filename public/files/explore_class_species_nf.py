"""explore_class_species_nf.py -- the CLASS SPECIES over a number ring: is a
same-cost tie in two ideal classes a reordering or a choice, in the world
with no genus?

THE QUESTION. The greedy image is a product, over a trajectory's surviving
openings, of the tie multiplicity at each, and "multiplicity" means the
WITHIN-TYPE multiplicity: a tie set splits into the types the engine can
read, and a choice between two TYPES was held to be a REORDERING. Over a
function field that reading has been split into species and one of them
overturned: two cores of one degree in DIFFERENT CLASSES starve each other,
so the choice is permanent and the within-type product is a lower bound
rather than the count (explore_reordering.py). That correction cannot move
a cardinality where the openings are endless -- a larger factor at
endlessly many openings is still the continuum. It bites where the image is
FINITE, and the finite images are the NUMBER RINGS.

WHY THE NUMBER RINGS MAY ALREADY DECIDE IT. Their ties are conjugate pairs
P, P' of one norm, and conjugate ideals carry INVERSE classes, since P*P'
is the rational prime and hence principal. Wherever the class group has an
element of order above 2, a non-principal conjugate tie is therefore
CROSS-CLASS: the within-class reading scores it multiplicity 1 -- no choice
at all -- while explore_greedy_image_nf.py's own breadth-first search, which
counts distinct LIMITS and not paths, measured 2 and met its 2^(t-e) bound
at every element seed. Either that measurement contradicts the within-class
reading, which tests the correction in a world where nothing of its proof
applies, or every tie there is principal-cored and the question is empty.
The two rings this corpus runs are Z[sqrt(-5)] at h = 2 and Z[w],
w^2 = w - 6, the maximal order of Q(sqrt(-23)), at h = 3.

WHAT DOES NOT TRANSFER, and it is the whole proof. The function-field
certificate has two halves. The CORE route is shut by the starved place's
door staying dearer -- an argument in DEGREES, where the number ring prices
in NORMS and multiplies where the function field adds. The PASSENGER route
is shut by minimal class representatives having degree at most the GENUS,
and a number ring has no genus at all. Both halves are re-derived below
from the number ring's own arithmetic, and the second one moves: the line
the genus drew is drawn here by MINKOWSKI.

THE SETTING. Both rings, both worlds, through the engines already built:
the ring arithmetic, the door menus and the element vehicle scan from
explore_number_field_lock.py and explore_module_law.py, and the two searches
(path enumeration over tie-choice vectors, and breadth-first with a visited
state set) from explore_greedy_image_nf.py, whose per-state audit hook is
what this file subclasses. IDEAL world: states are integral ideals, a move
is the least-norm ideal raising lambda. ELEMENT world: states and moves
principal, so a move seats a BUNDLE -- a core and whatever rides with it.
The seed belts are that file's: the void plus every place-power product of
norm at most 40 in the ideal world, and every element of norm at most 40 in
the element world, so every comparison below is against a measurement
already taken on the same states.

TRANSPLANT FLAGS, fixed at the freeze. Every intuition here is imported
from a neighbouring value of the ring parameter and is marked rather than
trusted.
 1. From the function field: "a cross-class decline is a choice." Its proof
    is degree arithmetic against the genus and carries NOTHING. Re-derived
    below in norms against Minkowski, and asserted at every visited state.
 2. From the IDEAL world to the ELEMENT world: "once P is seated its
    unseated conjugate is strictly dearer." That is a bare-door argument
    (explore_greedy_image_nf.py lemma C). An element vehicle carries a
    RIDER, so the comparison acquires a rider ratio on both sides and the
    inequality is not the same inequality.
 3. From the function field: "the rider is a minimal class representative."
    True wherever cost minimality picks the rider, which is a property of
    the menu and not of the ring -- but WHICH places are minimal
    representatives is entirely the ring's, and is what lemma C below
    computes rather than transplants.
 4. From explore_greedy_image_nf.py: "e, the ties the lock erased, is a
    measured residual." It was frozen there as an open observable and
    printed at two seeds. Nothing is assumed about its mechanism; PR8 is
    where this file asks whether it has one.

THE HAND-ATTACK, on paper before any engine code, in five lemmas. The rig
asserts each of them at every state it visits rather than assuming any.

 A. A TIE IS CROSS-CLASS EXACTLY WHEN ITS CORE IS NON-PRINCIPAL. P*P' =
    (p) is principal, so [P'] = -[P]. A tie set is a conjugate pair (proved
    in the ideal world, censused in the element one), so its two cores lie
    in inverse classes: the same class exactly when 2[P] = 0. At h = 2 that
    is every class and the species is EMPTY by group theory; at h = 3 it is
    only the trivial one, so every non-principal tie is cross-class.
 B. THE CORE ROUTE, with the rider ratio it acquires. Once P over the split
    rational prime p is seated at depth e >= 1, (p-1) divides lambda, so
    the least exponent A outside the absorbed set is at least 2: the
    unseated conjugate's bare door costs p^A while P's own deepening door
    costs p^max(1, A-e) <= p^(A-1). In the ELEMENT world both are
    multiplied by their riders' norms, so the gap p^e must beat the ratio
    of two rider norms, which lemma C bounds by the largest minimal
    representative norm. At both rings that bound is 2, so the argument
    survives at p >= 3 and can FAIL at p = 2 -- which is why the rig checks
    the engine's own menu at every successor and not the inequality alone,
    and reports the MARGIN rather than asserting the sign.
 C. THE PASSENGER ROUTE, and where the line sits with no genus. A vehicle
    is a core power times the minimal-norm representative of the class the
    core must cancel -- the number-ring form of the bare-door lemma, which
    the rig asserts at every menu it reads. A rider is therefore a minimal
    representative, and Minkowski bounds every class's minimal norm by
    (4/pi)^s (n!/n^n) sqrt|d|: 2.85 at Z[sqrt(-5)] and 3.05 at Z[w]. So the
    RIDER SET is finite and explicit, and a place outside it can only ever
    arrive as a CORE. The genus drew that line at degree g; here Minkowski
    draws it at NORM 2.
 D. AND THE TWO RINGS DIFFER IN WHAT SITS ON THE LINE. Z[sqrt(-5)]'s
    nontrivial class is represented at norm 2 by the RAMIFIED place over 2,
    which is Galois-fixed and so can never be a tie member at all;
    Z[w]'s two nontrivial classes are represented by the SPLIT pair over 2,
    which can. So the passenger route is shut at every tie of the first
    ring by geography, and open at exactly one pair of the second.
 E. THE LEVEL BELOW BOTH BUDGETS. The function-field capacity bound was
    derived from Riemann-Roch -- each class's minimal-degree effective
    representatives form a linear system, hence a finite set. Minkowski is
    not needed here either. What both arguments use is only that the class
    group is FINITE and that each cost level holds finitely many ideals, so
    each class has a least cost attained by finitely many ideals. The rider
    set is finite in any ring with those two properties; Riemann-Roch and
    Minkowski supply the VALUE of the bound and neither supplies the
    finiteness.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE CLASS SPECIES OCCURS AT h = 3, AND EVERY TIE'S CORES ARE INVERSE
    (lemma A). What the rig PRINTS: per ring per world, the tie census by
    species, and for the CLASS species the core norms and classes.
    KILL: zero CLASS pairs at Z[w]'s element world, in which case the
    question is empty; or one tie whose two cores are not inverse.
PR2 AND IT IS EMPTY AT h = 2, by group theory and not by census: every
    class is its own inverse there.
    KILL: one cross-class pair at Z[sqrt(-5)] in either world.
PR3 THE IDEAL WORLD HAS NO CLASS SPECIES AT EITHER RING, the class not
    being read there.
    KILL: one.
PR4 THE WITHIN-CLASS WIDTH IS 1 AT EVERY CLASS TIE, so the product the
    formula takes scores NO CHOICE at an opening where the breadth-first
    search counted two limits.
    KILL: one class tie whose within-class width is 2.
PR5 THE CERTIFICATE FIRES OUTSIDE THE RIDER SET (lemmas B, C). At every
    cross-class tie whose declined core is not a minimal representative,
    both routes are shut: its cheapest vehicle is strictly dearer than the
    successor's menu, and no vehicle can carry it as a passenger.
    KILL: one such declined core minimal at the successor, or seated along
    the canonical continuation.
PR6 AND IT REFUSES INSIDE IT. The split pair over 2 at Z[w] IS the rider
    set, so the certificate must decline to certify a tie there. What the
    rig PRINTS and what is read after the run: whether the declined core
    actually comes back, and by which route.
    No kill -- an open observable, frozen as such.
PR7 THE MINIMAL REPRESENTATIVES ARE UNIQUE AND SIT UNDER MINKOWSKI
    (lemmas C, D): the unit ideal and the ramified place over 2 at
    Z[sqrt(-5)]; the unit ideal and the split pair over 2 at Z[w].
    KILL: a class with two minimal representatives, or a minimal
    representative above the ring's Minkowski bound.
PR8 SO THE ERASED COUNT IS NOT A RESIDUAL. explore_greedy_image_nf.py
    measured e, the ties the lock swallowed, at two seeds and left its
    mechanism open. Predict e counts exactly the ties whose core lies in
    the RIDER SET, the recurrent vehicle at Z[w] being the product of the
    two minimal representatives.
    KILL: a seed where the two counts differ.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 EVERY ELEMENT-WORLD TIE AT h = 3 IS CROSS-CLASS, AND THE MEASUREMENT
   REFUTES THE WITHIN-CLASS READING (rule in range; 5 tie states on the
   norm-40 element belt and 35 on the norm-250 one, with 0 principal cores
   over 164 seeds). Conjugate cores carry inverse classes, so a tie is
   cross-class exactly when its core is non-principal -- and no tie on
   either belt has a principal core. The within-class width is therefore 1
   at every one of them: the product the formula takes scores NO CHOICE at
   any opening of that ring. The breadth-first search, which counts
   distinct LIMITS with a visited state set rather than paths, measures 2
   at 4 of the 27 element seeds. So at h = 3 the within-class reading is not
   a correction term carrying a small residual -- it is the WHOLE count,
   and it is wrong at every seed whose image exceeds a point. The
   function-field correction is confirmed in a world where nothing of its
   proof applies.

F2 AND h = 2 IS EMPTY BY GROUP THEORY, NOT BY CENSUS (proved; 0
   cross-class pairs over 25 and then 50 tie states). Every class is its own
   inverse at h = 2, so conjugate cores share a class and the species cannot
   exist there whatever the ring's geography does. The two rings therefore
   report the same number 2 with different objects behind it: a within-class
   WIDTH at h = 2, a SUM over two class branches at h = 3. Reading "the
   multiplicity over a quadratic number ring is 2" as one fact merges them,
   and the merge is invisible until h has an element of order above 2.

F3 THE PASSENGER ROUTE'S LINE IS MINKOWSKI'S, AND IT SITS AT NORM 2
   (two tiers, and they differ: the minimal representatives are PROVED --
   the enumeration to norm 60 is exhaustive and clears the Minkowski bound,
   so each class's minimum and its uniqueness are exact -- while the
   bare-door form the rider reading rests on is a RULE IN RANGE, read at
   every vehicle the searches met and never assumed). A rider is the minimal-norm representative of the class its core
   must cancel, so the RIDER SET -- the places a vehicle can ever carry as a
   passenger -- is the union of those representatives' supports, and
   Minkowski bounds each class's minimal norm at 2.85 and 3.05. It comes
   out {R2} at h = 2 and {P2.0, P2.1} at h = 3. What stands on the line
   differs and decides the ring: K5's representative is a RAMIFIED place,
   which is Galois-fixed and can never be a tie member at all, so its
   passenger route is shut at every tie by geography; K23's is a SPLIT PAIR,
   which ties. At norm 2 the picture the function field draws also
   degenerates -- the minimal representative of the cancelling class is the
   CORE'S OWN PLACE, so the rider lands on the core and their exponents add:
   the bare door of P2 at door exponent 2 is the vehicle P2^3, and reading
   "the core's exponent is its door" off the vehicle is then false while the
   bare-door DIVISOR is still exact. Read as divisors, every tie member the
   rig reads is its core's bare door at offset 0, on both belts, which is
   what makes "the core", and with it the species, well defined here.

F4 THE ERASED COUNT IS NOT A RESIDUAL: IT COUNTS THE RIDER-SET TIES (rule
   in range; 27/27 element seeds at h = 3 and 26/26 at h = 2). e -- the ties
   the lock swallows, so that two permanently distinct states reach ONE
   limit -- equals the number of openings on the trajectory whose core lies
   in the rider set, at every element seed of both rings. The mechanism is
   F3's, and it is a BASIN's and not the ring's: h = 3 has two element
   basins, one locking on (2) = P2.0*P2.1 and one on the inert place over
   5, and only the first can erase anything -- (2) is the PRODUCT OF THE
   TWO MINIMAL REPRESENTATIVES, so the places it swallows are exactly the
   rider-eligible ones, while the inert basin's vehicle carries a place no
   rider can. The measured equality is therefore a rule in range and not a
   theorem: it would fail at a seed holding a rider-set tie that locked in
   the inert basin, and no seed of these belts does. Erasure and readmission are then ONE
   route and not two independent failures of survival: a declined core comes
   back as a PASSENGER, and whether that kills PERMANENCE or only VISIBILITY
   turns on whether the vehicle carrying it recurs. The forward check reads
   the split directly -- all 6 declined cores the certificate refused are
   seated again within 12 moves, against 0 of the 4 it certified.
   (PR8 was frozen UNSCOPED and is FALSE in the ideal world, where a vehicle
   is a single place and e is 0 whatever the rider set holds -- a fact the
   source file already filed. It is an element-world claim; the 77 of 79
   ideal seeds that agree with it agree by accident.)

F5 AND THE SEATED-CORE REGIME HAS A CERTIFICATE OF ITS OWN -- THE LOCK,
   NOT STARVATION (rule in range; 17/17 and 14/14 ideal seeds separating at
   infinity, 10/10 and 4/4 element seeds separating at a frozen place; the
   freeze inherits the LOCK's own scope, its permanence beyond the witness
   window being the recurrence argument these rings were filed with).
   Starvation separates two limits by leaving a declined core's exponent at
   0, so it needs that core UNSEATED, and it covers only 2 of the 5 class
   ties: at the other three both cores are already seated and the choice is
   which of them to DEEPEN. What settles those is the LOCK. Its recurrent
   vehicle carries a fixed set of places to infinity and touches nothing
   else, so every exponent OUTSIDE that support is frozen from the lock
   onwards, and two branches differing there differ at the limit whether or
   not anything was starved. The two worlds then split cleanly on which
   mechanism runs: every IDEAL-world pair separates AT INFINITY, the two
   branches locking on different vehicles, which is starvation; every
   ELEMENT-world pair separates at a FROZEN FINITE place, both branches
   locking on the SAME vehicle. So the world the class species lives in is
   exactly the world starvation does NOT separate, and the freeze is what
   carries it. The freeze is also the number ring's alone -- it needs a
   lock, and a world with endless openings freezes nothing, which is why
   the same regime stays open over a function field. The two worlds are
   COMPLEMENTARY rather than parallel, and not because one of them can
   count: they have different certificates.

F6 THE LEVEL BELOW BOTH BUDGETS: NEITHER RIEMANN-ROCH NOR MINKOWSKI IS
   NEEDED (a derivation, with no run behind it). The capacity bound that
   defends the countable gap was derived over function fields from the
   minimal-degree effective representatives of a class forming a linear
   system, hence a finite set; here Minkowski gives the same finiteness by
   a different route. Both are stronger than the argument uses. What it
   needs is only that the class group is FINITE and that each cost level
   holds finitely many ideals -- whereupon each class has a least cost
   attained by finitely many of them, and the rider set is finite. Any
   Dedekind ring with those two properties has a bounded rider set, so the
   permanence half of the gap's defence covers a CLASS of rings rather than
   the two examples it was proved over. Riemann-Roch and Minkowski supply
   the VALUE of the line; neither supplies the finiteness.

F7 A DEPTH SPECIES EXISTS AT h = 3, AND THE NARROW BELT HAS NONE (unfrozen;
   2 of the 35 tie states on the widened element belt). Two cores of one
   norm tie at DIFFERENT depths and different door exponents -- the norm-2
   pair at depths 1 and 2 with doors 3 and 2, both vehicles of norm 8. Both
   its cores are rider-eligible, so it lies INSIDE the line F3 draws, where
   the passenger route is open and the class certificate is not run. It is
   the same open species the function field left open, arriving at the one
   ring family where it can be enumerated rather than argued.

F8 AND THE SEVENTH RING'S COARSE TYPE HOLDS TOO (rule in range; 169
   measured-type parts of a tie set over both rings and both belts, 0
   collisions). The images were MEASURED with the type (norm, class,
   exponent); the count was proved to factor over a type that carries the
   state DEPTH as well, and the two come apart exactly when one tie set
   holds two members of one measured type at different depths. None does,
   at either ring. The function-field proof of this used minimal
   representatives unique and no two places of degree <= g sharing a
   class; here the first holds at every class of both rings and the second
   is replaced by the rider set's smallness. Cheap, and it closes the one
   ring family the function-field result never covered.

THE DESIGN, in seven sections after the control.

 S1 THE POSITIVE CONTROL, run before any census is read. (a) The class
    labelling validated with no appeal to a table: every element of norm at
    most 200 in each ring has factorization class-sum zero, and every place
    is inverse to its conjugate. (b) At Z[sqrt(-5)] the labelling is
    checked against that ring's own independently filed class bit. (c) The
    filed engine facts reproduced through the imports -- the element
    overtures of both rings and the void tie of Z[w]. (d) The species
    classifier on planted pairs, one within-class and one cross-class, each
    of which must come back with its own name. (e) The domination detector
    on a starved core, on a core at a state where nothing is seated, and on
    a rider-eligible core -- the last being the control that must REFUSE,
    so that neither the detector's hits nor its zeros are automatic.
 S2 THE CLASS DATA: per ring, the class group order, the Minkowski bound,
    each class's minimal norm and every ideal attaining it, and the RIDER
    SET their supports give (PR7).
 S3 THE TIE CENSUS BY SPECIES: both searches over both seed belts, both
    worlds, both rings, with every tie set classified from its cores'
    norms, exponents and classes (PR1, PR2, PR3). The bare-door reading is
    asserted at every menu the searches read, since a vehicle with two
    lambda-raising places would make "the core" ambiguous and the species
    unreadable. Free at the same states, and the one ring family the
    function-field coarse-type result never covered: whether the type the
    images were MEASURED with ever holds two members of one tie set at
    different DEPTHS, which is where it would come apart from the type the
    count was proved to factor over.
 S4 THE CERTIFICATES at every cross-class tie: the core route against the
    successor's own menu, and the passenger route against the rider set
    (PR5, PR6). A pair is reported certified only when BOTH are shut.
 S5 THE FORWARD CHECK: each declined core followed along the canonical
    continuation, split by whether the certificate covers it -- the split
    being the point, since a certificate that covered everything would be
    untested.
 S5b THE FREEZE CERTIFICATE, added after the freeze and predicted by
    nothing: how each seed's limits actually separate -- by their INFINITY
    sets differing, which is starvation, or by a FINITE coordinate the
    lock's recurrent vehicle does not touch and therefore froze. The
    second needs nothing starved and is what covers the seated-core
    regime S4 leaves uncertified.
 S6 THE WIDTHS AND THE COUNT: per seed, the within-class product against
    the breadth-first search's own measured image size (PR4). This is the
    comparison the file exists to make.
 S7 THE ERASED COUNT against the rider-set tie count, per seed (PR8).

Run: `python explore_class_species_nf.py`. RUN RECORD (1222 checks here plus
the imported engines' own, ~0.6 s). S1 control: 139 and 129 elements to norm
200 of class 0 in the two rings, 40 places per ring inverse to their
conjugates, the computed class agreeing with Z[sqrt(-5)]'s own filed class
bit at all 40; the two element overtures, the two-basin tails and the
norm-6 void tie all reproduced; the classifier naming each planted species;
the domination detector certifying a starved norm-3 core and REFUSING both
a core at an unseated norm and a rider-eligible one. S2: h = 2 and 3 with
Minkowski 2.85 and 3.05, every class's minimal representative UNIQUE and
under the bound, rider sets {R2} (ramified) and {P2.0, P2.1} (a split
pair). S3 narrow belts: 18/7 and 14/5 tie states over the ideal/element
worlds, every one of multiplicity 2; all within-class except the h = 3
element world's 5, which are all CLASS, each of within-class width 1; 62 and
40 tie-set encounters, every tie member a bare door at offset 0, and 25 + 24
measured-type parts of a tie set with 0 holding two depths. S3b the
widened element belt at norm <= 250: 178 and 164 seeds, 50 tie states all
within-class at h = 2 with 18 principal cores, and 35 at h = 3 with 33 CLASS,
2 DEPTH and ZERO principal cores; offsets 0 throughout and 50 + 70 further
measured-type parts with 0 collisions. S4: 5 class ties, 4 of the 10 ordered
directions certified and 6 refused, every refusal for an already-seated
declined core; the core route reached its cost comparison 9 times and the
declined core's own vehicle ran 3.00 to 4.50 times the menu, never at or
below it. S5 forward check: 4/4 certified cores never seated again,
6/6 refused ones seated again within 12 moves. S5b: every ideal-world seed
with more than one limit separates AT INFINITY (17/17 and 14/14) and every
element-world one at a FROZEN finite place (10/10 and 4/4), the two
branches there locking on the same vehicle. S6: the within-class product
and the measurement agree at all 52/26/79 seeds of the other three columns
and disagree at 4 of the 27 h = 3 element seeds, where the product is 1 and
the measurement 2; the raw product exceeds the measurement at 6, by the 2
erased ties. S7: e equals the rider-set tie count at 27/27 and 26/26
element seeds. Slate PR1-PR8: PR1-PR7 hit; PR8 hit in the element world and
MISSED as frozen, having been written unscoped over a world where an ideal
vehicle makes e zero by construction. Unfrozen finds: the rider landing ON
its core at norm 2 (F3), the erasure/readmission identification (F4), the
certificate's silence at seated cores (F5), and the DEPTH species the wide
belt turned up (F7). The coarse-type census (F8) and the FREEZE
certificate (F5) were both added AFTER the freeze and no prediction covers
either; they are printed and asserted, not weighed against a slate. The
freeze is the one that changed a reading: the seated-core regime was
written up as settled by enumeration, and it is not -- it has its own
certificate, which the run then had to be asked for.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import pi, sqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_number_field_lock as K5      # the h = 2 ring (lineage)
import explore_module_law as K23            # the h = 3 ring (lineage)
import explore_greedy_image_nf as NF        # the two searches and the belts

CHECKS = 0

GEN_CAP = 60         # norm cap for the ideal enumeration behind the minreps
ELEM_CAP = 200       # norm cap for the class-sum control
FORWARD_T = 12       # moves the forward check follows a declined core for
WIDE_CAP = 250       # norm cap for the widened element belt

# (name, module, h, discriminant, the class-group generator place)
RINGS = [("K5", K5, 2, -20, ('ram', 2)),
         ("K23", K23, 3, -23, ('split', 2, 0))]


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def show(pl):
    return NF.show_place(pl)


def show_st(st):
    return NF.show_state(st)


# ------------------------------------------------------------- the classes
def is_principal(M, A):
    """An integral ideal is principal iff some element of its norm generates
    it. Both rings are imaginary quadratic, so the norm form is positive
    definite and the candidate list at a given norm is finite."""
    n = M.ideal_norm(A)
    if n == 1:
        return True
    for (y, x) in M.elem_candidates(n):
        if M.ideal_from_gens([(x, y)]) == A:
            return True
    return False


class Ring(object):
    """One ring with its class layer: the class of every place, each class's
    minimal-norm representatives, and the rider set those supports give."""

    def __init__(self, name, M, h, disc, gen):
        self.name, self.M, self.h, self.disc, self.gen = name, M, h, disc, gen
        self.g_hnf = M.place_hnf(gen)
        self.cls = {}
        # Minkowski: (4/pi)^s (n!/n^n) sqrt|d| at n = 2, s = 1.
        self.mink = (4.0 / pi) * 0.5 * sqrt(abs(disc))
        self._minreps()

    def cls_of_place(self, pl):
        if pl not in self.cls:
            A = self.M.place_hnf(pl)
            found = None
            for a in range(self.h):
                B = self.M.ideal_mul(A, self.M.ideal_pow(self.g_hnf,
                                                         (self.h - a) % self.h))
                if is_principal(self.M, B):
                    found = a
                    break
            ok(found is not None,
               "%s: place %s lies in no class of order %d"
               % (self.name, show(pl), self.h))
            self.cls[pl] = found
        return self.cls[pl]

    def cls_of(self, fac):
        """The class of a product of places, as a residue mod h."""
        c = 0
        for pl, e in fac.items():
            c += e * self.cls_of_place(pl)
        return c % self.h

    def _minreps(self):
        """Each class's least norm and every integral ideal attaining it, by
        enumerating products of places to GEN_CAP. The unit ideal supplies
        the trivial class at norm 1."""
        best = {0: (1, [{}])}
        for nrm, fac in self.M.gen_products(GEN_CAP):
            c = self.cls_of(fac)
            if c not in best or nrm < best[c][0]:
                best[c] = (nrm, [dict(fac)])
            elif nrm == best[c][0]:
                best[c][1].append(dict(fac))
        self.minnorm = dict((c, best[c][0]) for c in best)
        self.minreps = dict((c, best[c][1]) for c in best)
        self.rider = set()
        for c, reps in self.minreps.items():
            for rep in reps:
                for pl in rep:
                    self.rider.add(pl)


# ------------------------------------------------------------ the vehicles
def raisers(R, st, L, veh):
    """The places of a vehicle whose new exponent actually raises lambda."""
    return [pl for pl, e in veh.items()
            if L % R.M.lam_P(pl, st.get(pl, 0) + e)]


MAX_OFFSET = 4
MARGINS = []         # (ring, world, declined core's cost, the menu's) pairs


def vkey(veh):
    return tuple(sorted((repr(pl), e) for pl, e in veh.items() if e))


def bare_door(R, world, st, L, core, j=0):
    """The vehicle that opens a core's door at offset j: the core at its door
    exponent plus j, times the minimal-norm representative of the class that
    power must cancel. In the ideal world nothing is cancelled. The rider can
    land ON the core -- at norm 2 the minimal representative IS a place of the
    tied pair -- so the two exponents are ADDED rather than kept apart."""
    r = R.M.door_r(core, st.get(core, 0), L) + j
    veh = {core: r}
    if world == "element":
        c = (-r * R.cls_of_place(core)) % R.h
        for pl, e in R.minreps[c][0].items():
            veh[pl] = veh.get(pl, 0) + e
    nrm = 1
    for pl, e in veh.items():
        nrm *= R.M.place_norm(pl) ** e
    return r, veh, nrm


def read_core(R, world, st, L, veh):
    """(core, depth, door exponent, offset). Exactly ONE place of a vehicle
    raises lambda -- a second would make the core, and with it the species,
    ambiguous -- and the vehicle is that core's bare door at some offset.
    The offset is READ and reported rather than asserted zero: the function
    field's proof that it is always zero is degree arithmetic and is not
    carried here."""
    rs = raisers(R, st, L, veh)
    ok(len(rs) == 1,
       "%s/%s: a vehicle at %s with %d lambda-raising places, so no core"
       % (R.name, world, show_st(st), len(rs)))
    core = rs[0]
    for j in range(MAX_OFFSET):
        r, expect, _ = bare_door(R, world, st, L, core, j)
        if vkey(expect) == vkey(veh):
            return core, st.get(core, 0), r, j
    ok(False,
       "%s/%s: a vehicle at %s is no bare door of its core %s at any offset "
       "below %d" % (R.name, world, show_st(st), show(core), MAX_OFFSET))


def species(R, world, a, b):
    """The name of a cross-type pair, from its two core readings."""
    (p, _, rp, _), (q, _, rq, _) = a, b
    ok(p != q, "%s/%s: two distinct tie members with one core"
       % (R.name, world))
    if R.M.place_norm(p) != R.M.place_norm(q):
        return "cross-norm"
    if rp != rq:
        return "depth"
    if world == "ideal" or R.cls_of_place(p) == R.cls_of_place(q):
        return "within"
    return "class"


# ------------------------------------------------------------- the audit
class SpeciesAudit(NF.Audit):
    """The greedy-image searches' own per-state hook, extended to read every
    tie set's species. The searches are unchanged; what they visit is."""

    def __init__(self, R):
        NF.Audit.__init__(self)
        self.R = R
        self.reset()

    def reset(self):
        self.seen = {}      # (world, state key) -> record, deduped
        self.encounters = 0
        self.offsets = {}   # bare-door offset -> tie members read at it
        self.cur = set()    # the tie states of the seed being searched
        self.coarse_parts = 0   # measured-type parts of a tie set, examined
        self.coarse_bad = []    # parts holding two depths: a type collision

    def start_seed(self):
        """Per-seed attribution is kept apart from the global dedup: two
        seeds can pass through ONE tie state, and a diff against what was
        already seen would credit it to the first seed only."""
        self.cur = set()

    def tie(self, M, world, st, cost, vehs):
        NF.Audit.tie(self, M, world, st, cost, vehs)
        R = self.R
        self.encounters += 1
        key = (world, NF.frz(st), cost)
        self.cur.add(key)
        if key in self.seen:
            return
        L = M.lam_state(st)
        cores = [read_core(R, world, st, L, v) for v in vehs]
        names = {}
        for i in range(len(cores)):
            for j in range(i + 1, len(cores)):
                s = species(R, world, cores[i], cores[j])
                names[s] = names.get(s, 0) + 1
        fine, coarse, depths = {}, {}, {}
        for (_, _, _, j) in cores:
            self.offsets[j] = self.offsets.get(j, 0) + 1
        # THE COARSE TYPE against the REFINED one. The type the images were
        # MEASURED with reads (norm, class, exponent); the type the count
        # was PROVED to factor over carries the state depth as well. They
        # differ exactly when one tie set holds two members of one measured
        # type at different depths, which is checked here at every tie set
        # rather than inherited from the function-field ladder.
        for (core, e, r, _) in cores:
            k = (R.M.place_norm(core), r,
                 R.cls_of_place(core) if world == "element" else -1)
            depths.setdefault(k, set()).add(e)
        for k, es in depths.items():
            if len(es) > 1:
                self.coarse_bad.append((world, show_st(st), k, sorted(es)))
            self.coarse_parts += 1
        for (core, _, r, _) in cores:
            c = R.cls_of_place(core) if world == "element" else -1
            k = (R.M.place_norm(core), r)
            fine[k + (c,)] = fine.get(k + (c,), 0) + 1
            coarse[k] = coarse.get(k, 0) + 1
        self.seen[key] = {
            "world": world, "st": dict(st), "cost": cost,
            "vehs": [dict(v) for v in vehs], "cores": cores,
            "species": names, "width": max(fine.values()),
            "raw": len(vehs), "norm_width": max(coarse.values()),
        }


# ------------------------------------------------------- the certificates
def cheapest_vehicle(R, world, st, L, core):
    """The declined core's own cheapest vehicle at a state, over the offsets
    -- at norm 2 an offset vehicle can cost the same as the bare door, so
    the minimum is taken rather than the offset-zero form assumed."""
    best = None
    for j in range(MAX_OFFSET):
        r, _, nrm = bare_door(R, world, st, L, core, j)
        if best is None or nrm < best[0]:
            best = (nrm, r)
    return best


def dominated(R, world, st, chosen, decl_core):
    """Both routes to a declined core, at the successor of `chosen`. As a
    CORE: its cheapest vehicle strictly dearer than the successor's menu,
    with a seated same-norm neighbour to keep it so. As a PASSENGER: the
    core outside the rider set, which is what stops a vehicle carrying it
    back. Returns (verdict, detail)."""
    M = R.M
    s2 = NF.apply_vehicle(st, chosen)
    if st.get(decl_core, 0):
        return False, "already seated, so lemma A has no hypothesis"
    if s2.get(decl_core, 0):
        return False, "seated by the move itself"
    if decl_core in R.rider:
        return False, "in the rider set, so a vehicle can carry it back"
    cj = M.conj_place(decl_core)
    e_nb = s2.get(cj, 0)
    if not e_nb:
        return False, "no seated conjugate at the norm"
    L2 = M.lam_state(s2)
    cost2, _ = NF.MENUS[world](M, s2, L2)
    own, r = cheapest_vehicle(R, world, s2, L2, decl_core)
    # The cost comparison is a VERDICT and not an assertion. Written as an
    # assert it could only ever kill the run, so a certification would turn
    # on the structural pre-checks alone and the margin would go
    # unmeasured -- and the margin is the content, lemma B predicting the
    # gap to be a power of the rational prime against a rider ratio of at
    # most the largest minimal representative norm.
    MARGINS.append((R.name, world, own, cost2))
    if own <= cost2:
        return False, "still a minimal move, %d against menu %d" % (own,
                                                                    cost2)
    return True, "conjugate seated at depth %d, own vehicle %d vs menu %d" \
                 % (e_nb, own, cost2)


def forward_unseated(R, world, st, chosen, decl_core, T):
    """Follow the canonical continuation and report whether the declined
    core is ever seated again -- by any route, core or passenger."""
    M = R.M
    s = NF.apply_vehicle(st, chosen)
    for _ in range(T):
        if s.get(decl_core, 0):
            return False
        L = M.lam_state(s)
        _, vehs = NF.MENUS[world](M, s, L)
        s = NF.apply_vehicle(s, vehs[0])
    return not s.get(decl_core, 0)


# --------------------------------------------------------------- S1 control
def s1_control(rings):
    section("S1  THE POSITIVE CONTROL -- the class layer and the detectors")

    # (a) the labelling, with no appeal to a table: a principal ideal has
    # class zero, so every element's factorization must sum to zero.
    for R in rings:
        n_el = 0
        for n in range(2, ELEM_CAP + 1):
            for (y, x) in R.M.elem_candidates(n):
                fac = R.M.factor_elem(x, y)
                ok(R.cls_of(fac) == 0,
                   "%s: an element of norm %d has class %d"
                   % (R.name, n, R.cls_of(fac)))
                n_el += 1
        n_pl = 0
        for pl in R.M.UNIVERSE[:40]:
            ok((R.cls_of_place(pl) + R.cls_of_place(R.M.conj_place(pl)))
               % R.h == 0,
               "%s: %s and its conjugate are not inverse"
               % (R.name, show(pl)))
            n_pl += 1
        print("  %-4s class labelling: %d elements to norm %d all of class 0,"
              " %d places inverse to their conjugates"
              % (R.name, n_el, ELEM_CAP, n_pl))

    # (b) a second, independent source at the ring that files one.
    n_bit = 0
    for pl in K5.UNIVERSE[:40]:
        ok(rings[0].cls_of_place(pl) == K5.place_bit(pl),
           "K5: the computed class of %s disagrees with the filed bit"
           % show(pl))
        n_bit += 1
    print("  K5   the computed class agrees with that ring's own filed class"
          " bit at %d places" % n_bit)

    # (c) the filed engine facts, through the imports.
    log, _, _ = K5.run_elem({}, 8)
    ok([mv[2] for mv in log] == [4, 4, 9, 6, 4, 4, 4, 4],
       "control: the K5 element overture is %s" % [mv[2] for mv in log])
    tails = set()
    for seed in ({}, {('inert', 5): 1}):
        log, _, _ = K23.run_elem(seed, 20)
        tails.add(log[-1][2])
    ok(tails == {4, 25}, "control: the K23 element basins are %s" % tails)
    n0, hits0 = K23.elem_menu({}, 1)
    ok(n0 == 6 and len(hits0) == 2,
       "control: the K23 element void opens %d ways at norm %d"
       % (len(hits0), n0))
    print("  engines: the K5 element overture, the K23 two-basin tails, and")
    print("           the K23 element void's norm-6 tie all reproduce")

    # (d) the classifier on planted pairs, one of each name.
    R23 = rings[1]
    p3, p3c = ('split', 3, 0), K23.conj_place(('split', 3, 0))
    planted = [
        (("within", "element"), ((p3, 0, 1, {}), (p3, 0, 1, {}))),
        (("class", "element"), ((p3, 0, 1, {}), (p3c, 0, 1, {}))),
        (("within", "ideal"), ((p3, 0, 1, {}), (p3c, 0, 1, {}))),
        (("depth", "element"), ((p3, 0, 1, {}), (p3c, 0, 2, {}))),
        (("cross-norm", "element"), ((p3, 0, 1, {}), (('ram', 23), 0, 1, {}))),
    ]
    for (want, world), (a, b) in planted:
        if want == "within" and a[0] == b[0]:
            continue    # the identical-core case is what species() forbids
        got = species(R23, world, a, b)
        ok(got == want,
           "control: a planted %s pair in the %s world came back %s"
           % (want, world, got))
    print("  classifier: the planted class, depth, cross-norm and")
    print("              ideal-world-within pairs each came back named")

    # (e) the domination detector: a hit, and two refusals it must make.
    veh = {('split', 3, 0): 1, ('split', 2, 0): 1}
    L = K23.lam_state({})
    ok(read_core(R23, "element", {}, L, veh)[0] == ('split', 3, 0),
       "control: the bare-door reader misnames the norm-6 vehicle's core")
    hit, _ = dominated(R23, "element", {}, veh, p3c)
    ok(hit, "control: the detector will not certify a starved norm-3 core")
    miss1, why1 = dominated(R23, "element", {},
                            {('split', 3, 0): 1, ('split', 2, 0): 1},
                            ('split', 13, 5))
    ok(not miss1, "control: the detector certified a core at an unseated norm")
    p2, p2c = ('split', 2, 0), ('split', 2, 1)
    miss2, why2 = dominated(R23, "element", {p2: 1}, {p2: 3}, p2c)
    ok(not miss2 and "rider set" in why2,
       "control: the detector certified a RIDER-ELIGIBLE core: %s" % why2)
    print("  detector:   certifies a starved norm-3 core, refuses a core at")
    print("              an unseated norm (%s)," % why1)
    print("              and refuses a rider-eligible one (%s)" % why2)
    print("\n  Control green.")


# ------------------------------------------------------------ S2 the classes
def s2_class_data(rings):
    section("S2  THE CLASS DATA -- where Minkowski draws the line")
    print("  A rider is the minimal-norm representative of the class its")
    print("  core must cancel, so the places a vehicle can carry as a")
    print("  PASSENGER are exactly the supports of those representatives.")
    print("  Minkowski bounds each class's minimal norm, which is what the")
    print("  genus does in a function field.\n")
    print("  %-5s %-3s %-9s %-8s %-7s %-26s %s"
          % ("ring", "h", "Minkowski", "class", "minnorm", "representatives",
             "unique"))
    for R in rings:
        ok(len(R.minnorm) == R.h,
           "%s: %d classes found at h = %d" % (R.name, len(R.minnorm), R.h))
        for c in sorted(R.minnorm):
            reps = R.minreps[c]
            ok(R.minnorm[c] <= R.mink,
               "%s: class %d's minimal norm %d exceeds Minkowski %.2f"
               % (R.name, c, R.minnorm[c], R.mink))
            ok(len(reps) == 1,
               "%s: class %d has %d minimal representatives"
               % (R.name, c, len(reps)))
            print("  %-5s %-3d %-9.2f %-8d %-7d %-26s %s"
                  % (R.name, R.h, R.mink, c, R.minnorm[c],
                     ", ".join(show_st(r) for r in reps), "yes"))
        kinds = sorted(set(pl[0] for pl in R.rider))
        print("        rider set: %s -- %s"
              % (", ".join(show(pl) for pl in sorted(R.rider,
                                                     key=R.M.place_key))
                 or "(empty)", "/".join(kinds) or "nothing"))
    print("\n  A RAMIFIED place is Galois-fixed and can never be a tie")
    print("  member; a SPLIT pair can. Which of the two carries a ring's")
    print("  minimal representatives is what decides whether the passenger")
    print("  route is open at any tie of that ring at all.")


# ------------------------------------------------------- S3 the tie census
def canonical_walk(R, world, seed, audit):
    """The trajectory the formula's product runs over: the canonical branch,
    first tie member at every opening, to the lock. The product is over ONE
    trajectory's openings, so the tie states of the OTHER branches -- which
    the searches also visit -- must not enter it."""
    M = R.M
    st, L, used = dict(seed), M.lam_state(seed), 0
    ties = []
    while used < NF.T_CAP:
        if NF.lock_probe(M, world, st, L, NF.T_CAP - used) is not None:
            return ties
        cost, vehs = NF.MENUS[world](M, st, L)
        if len(vehs) > 1:
            key = (world, NF.frz(st), cost)
            ok(key in audit.seen,
               "%s/%s: the canonical walk met a tie state at %s the searches "
               "never recorded" % (R.name, world, show_st(st)))
            ties.append(audit.seen[key])
        st = NF.apply_vehicle(st, vehs[0])
        L = M.lam_state(st)
        used += 1
    ok(False, "%s/%s: the canonical walk from %s did not lock"
       % (R.name, world, show_st(seed)))


def census(rings):
    """Both searches over both belts, both worlds, both rings. Returns the
    per-ring audit and the per-seed image records."""
    out = {}
    for R in rings:
        audit = SpeciesAudit(R)
        recs = {}
        for world, seeds in (("ideal", NF.ideal_seeds(R.M)),
                             ("element", NF.element_seeds(R.M))):
            rows = []
            for seed in seeds:
                audit.start_seed()
                rec = NF.image_of(R.M, world, seed, audit)
                rec["world"] = world
                rec["ties"] = [audit.seen[k] for k in audit.cur]
                rec["walk"] = canonical_walk(R, world, seed, audit)
                ok(len(rec["walk"]) == rec["t"],
                   "%s/%s: the canonical walk from %s meets %d openings "
                   "against the searches' t = %d"
                   % (R.name, world, show_st(seed), len(rec["walk"]),
                      rec["t"]))
                rows.append(rec)
            recs[world] = rows
        out[R.name] = (audit, recs)
    return out


def s3_species(rings, data):
    section("S3  THE TIE CENSUS BY SPECIES")
    print("  Every tie set the two searches meet, on and off the filed")
    print("  trajectories, named from its cores' norms, exponents and")
    print("  classes. A tie set is deduped by (world, state, cost).\n")
    print("  %-5s %-8s %-8s %-8s %-8s %-8s %-8s %s"
          % ("ring", "world", "ties", "within", "class", "depth",
             "cross-nrm", "raw mult"))
    tot = {}
    for R in rings:
        audit, _ = data[R.name]
        for world in ("ideal", "element"):
            rows = [r for r in audit.seen.values() if r["world"] == world]
            names = {}
            for r in rows:
                for s, n in r["species"].items():
                    names[s] = names.get(s, 0) + n
            mult = {}
            for r in rows:
                mult[r["raw"]] = mult.get(r["raw"], 0) + 1
            tot[(R.name, world)] = (rows, names)
            print("  %-5s %-8s %-8d %-8d %-8d %-8d %-8d %s"
                  % (R.name, world, len(rows), names.get("within", 0),
                     names.get("class", 0), names.get("depth", 0),
                     names.get("cross-norm", 0), dict(sorted(mult.items()))))
    for R in rings:
        for world in ("ideal", "element"):
            rows, names = tot[(R.name, world)]
            if world == "ideal":
                ok(names.get("class", 0) == 0,
                   "PR3: %s's ideal world has %d CLASS pairs"
                   % (R.name, names.get("class", 0)))
            if R.h == 2:
                ok(names.get("class", 0) == 0,
                   "PR2: %s/%s has %d CLASS pairs at h = 2"
                   % (R.name, world, names.get("class", 0)))
    R23 = [R for R in rings if R.h == 3][0]
    rows, names = tot[(R23.name, "element")]
    ok(names.get("class", 0) > 0,
       "PR1: the h = 3 element world has no CLASS pair, so the question is "
       "empty")
    for r in rows:
        for i in range(len(r["cores"])):
            for j in range(i + 1, len(r["cores"])):
                a, b = r["cores"][i][0], r["cores"][j][0]
                if R23.M.place_norm(a) != R23.M.place_norm(b):
                    continue
                ok((R23.cls_of_place(a) + R23.cls_of_place(b)) % R23.h == 0,
                   "PR1: a tie at %s pairs classes %d and %d, not inverses"
                   % (show_st(r["st"]), R23.cls_of_place(a),
                      R23.cls_of_place(b)))
    widths = {}
    for R in rings:
        audit, _ = data[R.name]
        for r in audit.seen.values():
            if r["species"].get("class", 0):
                widths[r["width"]] = widths.get(r["width"], 0) + 1
                ok(r["width"] == 1,
                   "PR4: a CLASS tie at %s has within-class width %d"
                   % (show_st(r["st"]), r["width"]))
    print("\n  The within-class width at every CLASS tie: %s"
          % dict(sorted(widths.items())))
    for R in rings:
        audit, _ = data[R.name]
        ok(not audit.coarse_bad,
           "%s: the measured type collides with the factoring one at %s"
           % (R.name, audit.coarse_bad[:1]))
        print("  %-5s %d tie-set encounters over the two searches, %d "
              "distinct; bare-door offsets read: %s"
              % (R.name, audit.encounters, len(audit.seen),
                 dict(sorted(audit.offsets.items()))))
        print("        %d measured-type parts of a tie set, %d holding two "
              "depths -- so the type the image was MEASURED with is the type"
              % (audit.coarse_parts, len(audit.coarse_bad)))
        print("        the count was PROVED to factor over, here as well")
    print("  An offset above 0 would be a tie member that is NOT its core's")
    print("  bare door, which the function field forbids by an argument in")
    print("  degrees. Here it is read at every member rather than assumed.")


def s3b_wider(rings):
    """A tie is cross-class exactly when its core is NON-PRINCIPAL, so a
    within-class tie at h = 3 needs a principal SPLIT core. Whether one is
    reachable is geography, and the narrow belt cannot tell an accident of
    its own width from a fact about the ring."""
    section("S3b  THE WIDENED ELEMENT BELT -- is the census the belt's?")
    print("  Element seeds to norm %d, both rings, the same two searches.\n"
          % WIDE_CAP)
    print("  %-5s %-8s %-8s %-8s %-8s %-22s %s"
          % ("ring", "seeds", "ties", "within", "class", "every species",
             "principal cores"))
    for R in rings:
        audit = SpeciesAudit(R)
        seeds = NF.element_seeds(R.M, WIDE_CAP)
        for seed in seeds:
            audit.start_seed()
            NF.image_of(R.M, "element", seed, audit)
        names, prin = {}, 0
        for r in audit.seen.values():
            for s, n in r["species"].items():
                names[s] = names.get(s, 0) + n
            prin += sum(1 for c in r["cores"]
                        if R.cls_of_place(c[0]) == 0)
        mult = {}
        for r in audit.seen.values():
            mult[r["raw"]] = mult.get(r["raw"], 0) + 1
        print("  %-5s %-8d %-8d %-8d %-8d %-22s %d"
              % (R.name, len(seeds), len(audit.seen), names.get("within", 0),
                 names.get("class", 0), dict(sorted(names.items())), prin))
        ok(not audit.coarse_bad,
           "%s: the measured type collides with the factoring one at %s"
           % (R.name, audit.coarse_bad[:1]))
        print("        tie multiplicities: %s; offsets: %s; measured-type "
              "parts %d, collisions with the factoring type %d"
              % (dict(sorted(mult.items())),
                 dict(sorted(audit.offsets.items())),
                 audit.coarse_parts, len(audit.coarse_bad)))
        for r in sorted(audit.seen.values(),
                        key=lambda z: (z["cost"], show_st(z["st"]))):
            if set(r["species"]) - {"within", "class"}:
                print("        %-9s %s at norm %d: %s"
                      % ("/".join(sorted(set(r["species"]) -
                                         {"within", "class"})),
                         show_st(r["st"]), r["cost"],
                         " | ".join("%s door %d depth %d"
                                    % (show(c[0]), c[2], c[1])
                                    for c in r["cores"])))


# ------------------------------------------------------ S4/S5 certificates
def s4_certificates(rings, data):
    section("S4  THE CERTIFICATES -- both routes, at every cross-class tie")
    print("  A pair is CERTIFIED only when both routes are shut: the core")
    print("  route by the declined core's cheapest vehicle staying dearer")
    print("  than the successor's own menu, and the passenger route by the")
    print("  core lying outside the rider set.\n")
    print("  %-5s %-8s %-9s %-10s %-10s %s"
          % ("ring", "world", "class ties", "dirs cert", "dirs refused",
             "why refused"))
    certs, refusals = [], []
    for R in rings:
        audit, _ = data[R.name]
        for world in ("ideal", "element"):
            rows = [r for r in audit.seen.values()
                    if r["world"] == world and r["species"].get("class", 0)]
            nc, nr, whys = 0, 0, {}
            for r in rows:
                for i in range(len(r["cores"])):
                    for j in range(len(r["cores"])):
                        if i == j:
                            continue
                        a, b = r["cores"][i], r["cores"][j]
                        if species(R, world, a, b) != "class":
                            continue
                        verdict, why = dominated(R, world, r["st"],
                                                 r["vehs"][i], b[0])
                        r["certified"] = r.get("certified", False) or verdict
                        if verdict:
                            nc += 1
                            certs.append((R, world, r, r["vehs"][i], b[0]))
                        else:
                            nr += 1
                            key = why.split(",")[0]
                            whys[key] = whys.get(key, 0) + 1
                            refusals.append((R, world, r, r["vehs"][i], b[0]))
            if rows:
                print("  %-5s %-8s %-9d %-10d %-10d %s"
                      % (R.name, world, len(rows), nc, nr,
                         "; ".join("%s x%d" % (k, v)
                                   for k, v in sorted(whys.items())) or "-"))
    print("\n  EVERY CLASS TIE, one row each -- the census is small enough to")
    print("  print whole, so no specimen is chosen for the reader.\n")
    print("  %-5s %-24s %-5s %-14s %-8s %-6s %s"
          % ("ring", "state", "cost", "the two cores", "classes", "rider",
             "verdict"))
    for R in rings:
        audit, _ = data[R.name]
        for r in sorted(audit.seen.values(),
                        key=lambda z: (z["world"], z["cost"],
                                       show_st(z["st"]))):
            if not r["species"].get("class", 0):
                continue
            cs = [c[0] for c in r["cores"]]
            verdicts = []
            for i in range(len(r["cores"])):
                for j in range(len(r["cores"])):
                    if i != j:
                        v, why = dominated(R, r["world"], r["st"],
                                           r["vehs"][i], r["cores"][j][0])
                        verdicts.append("choice" if v else why.split(",")[0])
            print("  %-5s %-24s %-5d %-14s %-8s %-6s %s"
                  % (R.name, show_st(r["st"]), r["cost"],
                     " | ".join(show(c) for c in cs),
                     ",".join(str(R.cls_of_place(c)) for c in cs),
                     "yes" if any(c in R.rider for c in cs) else "no",
                     " / ".join(sorted(set(verdicts)))))
    tight = [m for m in MARGINS if m[2] <= m[3]]
    if MARGINS:
        ratios = sorted(m[2] / float(m[3]) for m in MARGINS)
        print("\n  The core route reached its COST comparison %d times, and"
              % len(MARGINS))
        print("  the declined core's own vehicle ran %.2f to %.2f times the"
              % (ratios[0], ratios[-1]))
        print("  menu, never at or below it (%d at or below). Lemma B says"
              % len(tight))
        print("  the gap is a power of the rational prime against a rider")
        print("  ratio of at most 2, so it is 3/2 or better at every norm")
        print("  above 2 and could close only at norm 2 -- which the rider")
        print("  set removes before the comparison is ever reached.")
    ok(not tight,
       "a declined core outside the rider set is still a minimal move: %s"
       % tight[:1])
    print("\n  The starvation certificate needs an UNSEATED declined core, so")
    print("  it is silent wherever both cores are already seated and the")
    print("  choice is which of two seated places to DEEPEN. Those are not")
    print("  left to the count: S5b gives them a second certificate.")
    return certs, refusals


def s5_forward(certs, refusals):
    section("S5  THE FORWARD CHECK -- the declined core along the walk")
    print("  A certificate that covered every case would be untested, so")
    print("  the split is the point: the covered cores and the refused ones")
    print("  are followed by the SAME walk for %d moves.\n" % FORWARD_T)
    rows = []
    for label, batch in (("certified", certs), ("refused", refusals)):
        stayed, came = 0, 0
        for (R, world, r, chosen, core) in batch:
            if forward_unseated(R, world, r["st"], chosen, core, FORWARD_T):
                stayed += 1
            else:
                came += 1
        rows.append((label, len(batch), stayed, came))
        print("  %-10s %4d cores: %4d never seated again, %4d seated again"
              % (label, len(batch), stayed, came))
    for label, n, stayed, came in rows:
        if label == "certified":
            ok(came == 0,
               "PR5: %d certified cores were seated again along the walk"
               % came)
    return rows


# --------------------------------------------------------- S6 the widths
def s5b_freeze(rings, data):
    """THE SECOND CERTIFICATE. Starvation separates two limits by leaving a
    place unseated, so it needs an unseated victim. The LOCK separates them
    another way: its recurrent vehicle carries a fixed set of places to
    infinity and touches nothing else, so every exponent OUTSIDE that
    support is frozen from the lock onwards. Two branches differing there
    at the moment of locking differ at the limit, whether or not anything
    was starved -- which is exactly the seated-core regime the starvation
    certificate is silent at."""
    section("S5b  THE FREEZE CERTIFICATE -- what the lock separates")
    print("  Two limits separate one of two ways. Their INFINITY sets can")
    print("  differ -- what a starved place gives, the branches locking on")
    print("  different vehicles. Or the infinity sets AGREE and the limits")
    print("  differ at a FINITE place, which the lock froze: its recurrent")
    print("  vehicle touches nothing else, so no later move reaches that")
    print("  coordinate. The second needs nothing starved.\n")
    print("  %-5s %-8s %-8s %-12s %-12s %s"
          % ("ring", "world", "seeds>1", "at infinity", "frozen",
             "example"))
    for R in rings:
        _, recs = data[R.name]
        for world in ("ideal", "element"):
            n, at_inf, frozen, ex = 0, 0, 0, ""
            for rec in recs[world]:
                lims = sorted(rec["bfs_limits"])
                if len(lims) < 2:
                    continue
                n += 1
                kinds = set()
                for i in range(len(lims)):
                    for j in range(i + 1, len(lims)):
                        a, b = dict(lims[i]), dict(lims[j])
                        ooa = set(pl for pl, e in a.items() if e == 'oo')
                        oob = set(pl for pl, e in b.items() if e == 'oo')
                        if ooa != oob:
                            kinds.add("infinity")
                            continue
                        diff = [pl for pl in set(a) | set(b)
                                if a.get(pl, '0') != b.get(pl, '0')]
                        # The infinity sets agree, so every differing place
                        # is FINITE in both and outside the recurrent
                        # vehicle -- frozen from the lock onwards.
                        ok(diff and not (set(diff) & ooa),
                           "%s/%s: two limits agree at infinity and differ "
                           "nowhere finite, from %s"
                           % (R.name, world, show_st(rec["seed"])))
                        kinds.add("frozen")
                        if not ex:
                            ex = "%s at %s" % (show_st(rec["seed"]), diff[0])
                at_inf += ("infinity" in kinds)
                frozen += ("frozen" in kinds)
            if n:
                print("  %-5s %-8s %-8d %-12d %-12d %s"
                      % (R.name, world, n, at_inf, frozen, ex))
    print("\n  So the seated-core regime is not settled by ENUMERATION after")
    print("  all -- it has its own certificate, and a different one: the")
    print("  lock freezes every place its vehicle does not carry. That is")
    print("  the certificate a world with ENDLESS openings cannot have,")
    print("  nothing ever being frozen there, which is why the same regime")
    print("  stays open over a function field.")


def s6_widths(rings, data):
    section("S6  THE WIDTHS AND THE COUNT -- what the product scores")
    print("  Per seed: the product of the WITHIN-CLASS widths over the")
    print("  seed's tie states, against the breadth-first search's own")
    print("  measured image size. The two are the reading and the")
    print("  measurement, on the same states.\n")
    print("  %-5s %-8s %-7s %-10s %-10s %-10s %s"
          % ("ring", "world", "seeds", "within", "raw", "measured",
             "seeds where within-class misses"))
    out = {}
    for R in rings:
        _, recs = data[R.name]
        for world in ("ideal", "element"):
            npr, nraw, nms, diff, examples = 0, 0, 0, 0, []
            for rec in recs[world]:
                prod, raw = 1, 1
                for r in rec["walk"]:
                    prod *= r["width"]
                    raw *= r["raw"]
                got = len(rec["bfs_limits"])
                npr += (prod > 1)
                nraw += (raw > 1)
                nms += (got > 1)
                if prod != got:
                    diff += 1
                    if len(examples) < 3:
                        examples.append("%s: %d vs %d"
                                        % (show_st(rec["seed"]), prod, got))
            out[(R.name, world)] = (npr, nraw, nms, diff)
            print("  %-5s %-8s %-7d %-10d %-10d %-10d %d  %s"
                  % (R.name, world, len(recs[world]), npr, nraw, nms, diff,
                     "; ".join(examples)))
    print("\n  'within' is the product of the within-class widths over the")
    print("  canonical trajectory's openings -- the factor the formula")
    print("  takes; 'raw' the product of the full tie multiplicities;")
    print("  'measured' the breadth-first search's own distinct-limit count.")
    only_uncert, with_class = 0, 0
    for R in rings:
        _, recs = data[R.name]
        for rec in recs["element"]:
            cls_ties = [r for r in rec["walk"] if r["species"].get("class", 0)]
            if len(rec["bfs_limits"]) <= 1 or not cls_ties:
                continue
            with_class += 1
            if not any(r.get("certified") for r in cls_ties):
                only_uncert += 1
    print("\n  Seeds whose measured image exceeds one point and whose")
    print("  trajectory carries a CLASS tie: %d, of which %d carry NO tie the"
          % (with_class, only_uncert))
    print("  starvation certificate covers -- and the FREEZE certificate of")
    print("  S5b is what proves those, so none of them rests on the count.")
    return out


# --------------------------------------------------------- S7 the erasure
def s7_erasure(rings, data):
    section("S7  THE ERASED COUNT AGAINST THE RIDER SET")
    print("  The greedy-image file measured e, the ties the lock swallowed,")
    print("  and left its mechanism open. Predict e counts exactly the ties")
    print("  whose core lies in the RIDER SET.\n")
    print("  %-5s %-8s %-7s %-10s %-12s %s"
          % ("ring", "world", "seeds", "sum e", "sum rider", "seeds agreeing"))
    for R in rings:
        _, recs = data[R.name]
        for world in ("ideal", "element"):
            se, sr, agree = 0, 0, 0
            for rec in recs[world]:
                rid = 0
                for r in rec["walk"]:
                    if any(c[0] in R.rider for c in r["cores"]):
                        rid += 1
                se += rec["erased"]
                sr += rid
                agree += (rec["erased"] == rid)
                # PR8 was frozen UNSCOPED and is false in the ideal world for
                # a reason already filed: an ideal vehicle is a single place,
                # so it can swallow no pair and e is 0 there whatever the
                # rider set holds. The prediction is an ELEMENT-world claim
                # and is asserted where it has content.
                if world == "element":
                    ok(rec["erased"] == rid,
                       "PR8: %s seed %s erased %d ties with %d rider-set ties"
                       % (R.name, show_st(rec["seed"]), rec["erased"], rid))
            print("  %-5s %-8s %-7d %-10d %-12d %d/%d"
                  % (R.name, world, len(recs[world]), se, sr, agree,
                     len(recs[world])))
    print("\n  The ideal-world rows are PR8's own scope error and not a")
    print("  finding: an ideal vehicle is a single place, so it swallows no")
    print("  pair and e is 0 there whatever sits in the rider set.")


def main():
    print("EXPLORE: THE CLASS SPECIES OVER A NUMBER RING")
    print("Is a same-cost tie in two ideal classes a reordering or a choice,")
    print("where the image is FINITE and there is no genus?")
    rings = [Ring(n, M, h, d, g) for (n, M, h, d, g) in RINGS]
    s1_control(rings)
    s2_class_data(rings)
    data = census(rings)
    s3_species(rings, data)
    s3b_wider(rings)
    certs, refusals = s4_certificates(rings, data)
    s5_forward(certs, refusals)
    s5b_freeze(rings, data)
    s6_widths(rings, data)
    s7_erasure(rings, data)
    section("CHECKS")
    print("  %d assertions in this file, plus the imported engines' own."
          % CHECKS)


if __name__ == "__main__":
    main()
