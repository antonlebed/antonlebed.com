"""explore_greedy_image_nf.py -- THE GREEDY IMAGE OVER A NUMBER RING: how
many limits the minimal-move policy class reaches when "least" ties, in the
third of the three worlds the corpus can run.

THE QUESTION. A demand law's FATE IMAGE is the set of limits its whole FREE
policy class reaches from a seed. Its restriction to the MINIMAL-MOVE policy
class is the GREEDY IMAGE, Im_greedy(L, s) -- an object that only exists
where "least" fails to name a move. Over Q it is a single point at every
law, by definition and not by measurement: the least admissible m is unique
because Z totally orders the candidates (explore_fate_image.py). Over
F_2[x] it is a CONTINUUM under D-DYN: "least" orders by degree, every fresh
opening is a free choice among all N_2(d) irreducibles of the frontier
degree, and the sibling starvation makes each choice permanent
(explore_fate_image_ff.py). The third world is the quadratic number rings,
where the tie census already files that every tie is a GALOIS ORBIT
(explore_number_field_lock.py finding 3). What is the greedy image over
Z[sqrt(-5)] (h = 2) and over Z[w], w^2 = w - 6, the maximal order of
Q(sqrt(-23)) (h = 3)?

WHY IT IS NOT A COROLLARY OF THE TIE CENSUS. The census counted TIES along
two filed tie-break rules. A tie is a CHOICE POINT, and the image is a set
of LIMITS; the two agree only if the choices are independent and permanent.
Two ways they need not be. (i) BRANCHES MERGE -- over F_2[x] the void's
third tie member rejoins the lex branch within a few moves and ends at the
same support, so a count of ties is an upper bound and nothing more. (ii)
THE CONJUGATE CHOICE MAY NOT SURVIVE: the two branches of a Galois tie are
isomorphic worlds and may reach limits that are literally conjugate rather
than distinct, which would make the number-field image an ORBIT -- the
natural guess, already dead over F_2[x] (Aut has order 2 and the image is
uncountable) but never tested in the one world where every tie IS a
symmetry.

THE SETTING. Cold D-DYN, both worlds of each ring, exactly as
explore_number_field_lock.py and explore_module_law.py run them and with
their engines imported rather than re-implemented (the door menu, the
lambda pumps, the element vehicle scan). IDEAL world: states are integral
ideals, a move is the least-norm ideal m != (1) with lambda(I*m) >
lambda(I). ELEMENT world: states and moves principal. A LIMIT is a
supernatural ideal -- an exponent function on the places with values in
{0, 1, ...} u {oo}. Since every censused trajectory LOCKS, a limit is a
finite exponent vector together with the lock vehicle's places at infinity.

TRANSPLANT FLAGS, fixed at the freeze. Every intuition below is imported
from a neighbouring value of the ring parameter and is marked rather than
trusted.
 1. From F_2[x]: "each opening is a FREE choice, made permanent by the
    sibling starvation." F_2[x]'s starvation is a proof about degree
    classes and clocked doors. Nothing of it transfers as stated; the
    number-ring analogue is re-derived below and re-checked at every state
    the search visits.
 2. From F_2[x]: "the image is a continuum because the run never halts."
    Here runs LOCK, so the number of choice points is finite and the
    cardinality question is a COUNTING question rather than a cardinality
    one. The interesting content moves accordingly.
 3. From the census: "max wander 2" and "every tie is a conjugate pair"
    are facts about the two filed tie-break rules. This search visits
    states no filed trajectory reached, where neither is guaranteed.
 4. From the IDEAL world to the ELEMENT world: an ideal move seats ONE
    place, an element move seats a bundle (the free-rider door, norm 6 =
    P2*P3'). Every argument below that says "the sibling never enters"
    is an ideal-world argument and is not carried across -- the element
    world is where a merge can happen and is run as the test, not as a
    second confirmation.

THE HAND-ATTACK, on paper before any engine code, in four lemmas and one
prediction. Lemmas A, C and D are derivations; the rig asserts each of
them at every state it visits rather than assuming any.

 A. WHERE A TIE CAN LIVE. A door's cost is N(place)^r -- p^r at a split or
    ramified place, q^(2r) at an inert one. Every cost is therefore a power
    of the place's RATIONAL prime, so two doors of equal cost lie over one
    rational prime, and a rational prime carries two places only when it
    SPLITS. Ties are conjugate pairs and nothing else. (The filed
    "every tie is a Galois orbit" is the same statement as a census; this
    is the reason.)
 B. THE DOOR EXPONENT. lam_P(pl, a) divides lam_P(pl, a+1) at all four
    pump shapes, so { a : lam_P(pl, a) | L } is downward closed. With
    A(pl, L) = the least a >= 1 outside it, the door exponent is
    r = max(1, A - e) at current depth e. Everything below rests on this.
 C. SIBLING STARVATION OVER K. Once P (split p) is seated at depth e >= 1,
    (p-1) | L, hence A >= 2, hence the unseated conjugate P' costs p^A >=
    p^2 while P's own deepening door costs p^max(1, A-e) <= p^(A-1). The
    sibling is STRICTLY dominated at every state and can never re-enter
    the minimal set. Ideal-world choices are permanent, and the two
    branches of a tie differ in their support forever.
 D. LOCKSTEP. lam_P depends only on (kind, p, a) and is identical at P and
    P'. Two policies differing only in which member of a tie they take are
    therefore identical in (cost, kind, char, r) at every move -- the same
    lemma as F_2[x]'s, by the same argument, with the degree class
    replaced by the conjugate pair.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE IDEAL IMAGE IS FINITE OF SIZE EXACTLY 2^t, where t is the number of
    tie moves on a trajectory -- branch-independent by lemma D. The lock
    ends the openings, so t is finite; the starvation (lemma C) makes the
    2^t branches pairwise distinct, so no merge occurs and the search's
    distinct-limit count MEETS its own upper bound.
    KILL: a seed whose distinct-limit count differs from 2^t, in either
    direction.
PR2 SO THE IMAGE IS A GALOIS ORBIT ONLY WHERE t <= 1. |Gal| = 2, so an
    orbit has at most 2 members; a seed with two tie moves has four limits
    and its image strictly contains the orbit of any member. Predict both
    cases occur in the K5 ideal census: the void locks P3 at move 1 (t = 1,
    an orbit of 2), while seed P29 ghosts through the split 7-pair and
    locks the fresh 23-pair (t = 2, four limits). Predict t = 0 also
    occurs, at seeds
    locking a ramified place with no split opening -- a Z-like single
    point inside a ring that ties.
    KILL: every censused seed has the same t, or no seed exceeds t = 1.
PR3 THE TIE SHAPE IS EXACTLY LEMMA A at every state the search visits, on
    and off the filed trajectories: every tie set has 2 members, they lie
    over one rational prime, they are conjugate, and their door exponents
    are equal.
    KILL: one tie set with a member count != 2, or with two members over
    different rational primes, or a tie set that is not a conjugate pair.
PR4 STARVATION HOLDS AT EVERY VISITED STATE: wherever one member of a
    split pair is seated and the other is not, the unseated one's door
    cost strictly exceeds the seated one's.
    KILL: one state where the two costs are equal or the unseated one is
    cheaper.
PR5 LOCKSTEP HOLDS ACROSS THE WHOLE POLICY CLASS: all 2^t branches from a
    seed carry the identical sequence of (cost, kind, char, r), differing
    only in WHICH member of each tied pair they seat.
    KILL: two branches from one seed whose sequences differ.
PR6 THE ELEMENT WORLD IS WHERE THE PREDICTIONS STOP. Its ties are bundles
    and flag 4 withdraws lemma C, so no count is predicted. What the rig
    PRINTS and what is read after the run: the tie multiplicities (are
    they all 2?), whether any two branches reach a common state (the merge
    observable: a state with in-degree > 1 in the search), and the
    distinct-limit count against 2^t.
    No kill -- an open observable, frozen as such.
PR7 THE THREE-WORLD FORMULA. |Im_greedy| = the product, over the
    trajectory's openings, of the tie multiplicity at each. Over Z every
    multiplicity is 1 (the total order) and the product is 1; over K the
    multiplicity is 2 at a split opening and 1 otherwise, and the openings
    stop at the lock, so the product is 2^t; over F_q[x] the multiplicity
    is N_q(d) and the openings never stop, so the product is a continuum.
    Predict the K columns of that table are what PR1 measures, so that one
    formula covers all three worlds with two ring facts feeding it -- the
    tie multiplicity and lock-versus-sprawl -- and nothing else.
    KILL: PR1 fails, or the K5 and K23 ideal columns disagree with each
    other in shape.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE GREEDY IMAGE OVER A NUMBER RING IS FINITE, OF SIZE EXACTLY 2^t
   (rule in range; two rings x two belts -- 52 and 79 seeds at norm <= 40,
   then 351 and 495 at norm <= 250, the wider belt containing the narrower
   and re-running it -- every seed measured by both searches, and every
   ideal state either search visited product-scanned for a cheaper
   COMPOSITE move, which the source files verify at their own census
   states only). t is the number of tie moves, and it is branch-independent
   because LOCKSTEP holds across the whole policy class: all 2^t branches
   from a seed carry the identical sequence of (cost, kind, char, r) and
   differ only in WHICH member of each tied pair they seat -- checked at
   every seed, and carrying CONTENT at the 31 seeds of the norm-40 belts
   that have a second branch at all, a t = 0 seed having nothing to
   disagree with itself. The BFS with a
   visited state set MEETS its own upper bound at every seed -- 0 branch
   merges -- because the SIBLING STARVATION over K makes each choice
   permanent: once P is seated at depth e >= 1, (p-1) | lambda, so the
   unseated conjugate's door costs p^A >= p^2 while P's own deepening door
   costs p^max(1, A-e) <= p^(A-1), strictly cheaper at every state (2308
   instances checked). So the three worlds read 1, 2^t, and the continuum,
   and the middle one is the only one where the count is a MEASUREMENT.

F2 AND THE IMAGE IS A GALOIS ORBIT ONLY WHERE t <= 1 -- the orbit reading
   dies in the one world where it looked alive (rule in range; the
   specimen exhaustive over its own tie sets). |Gal| = 2, so an orbit holds
   at most 2 limits, and the K5 norm-40 belt realises t = 0, 1 and 2: of
   its 52 seeds, 35 reach a single POINT and are Z-like inside a ring that
   ties, 15 reach a 2-member orbit, and the TWO seeds above 29 reach FOUR
   each. Writing P7, P7' and P23, P23' for the two split pairs the run
   prints, the image of the seed P29 is P29*P7*P23^oo, P29*P7'*P23^oo,
   P29*P7*P23'^oo and P29*P7'*P23'^oo, of
   which any one's conjugate carries the seed P29' and is not in the image
   at all. Two independent Galois ties compose into a group of choices
   larger than the group, so "every tie is a Galois orbit" is a statement
   about SINGLE ties that does not survive composition. The natural guess
   was already dead over F_2[x] on cardinality grounds; here it dies on the
   arithmetic of the number field itself.

F3 WHAT DECIDES IT IS GEOGRAPHY, NOT THE CLASS GROUP (rule in range at
   K5, and a NULL at K23 -- no t >= 2 seed was found there out to norm
   250, which is not a proof that none exists). t >= 2 needs two split
   openings, so it needs the pre-lock WANDER to open a split pair; a
   ramified or inert place is Galois-FIXED and cannot tie, so a wander
   through one spends no choice. K23 wanders through ramified places only
   (50 of 50 wander moves), while K5's wander opens the split 7-pair
   (10 of 192). Neither h nor the class group enters: what decides whether
   a ring's greedy image can EXCEED an orbit is which places the ring makes
   cheap enough to wander through.

F4 THE TIE'S SHAPE IS A THEOREM IN THE IDEAL WORLD AND A MEASUREMENT IN
   THE ELEMENT WORLD (618 tie-set encounters on and off the filed
   trajectories, every one of multiplicity 2 and every one a conjugate
   pair). A door's cost is N(place)^r, always a power of the place's
   RATIONAL prime, so equal costs lie over one rational prime and a
   rational prime carries two places only when it splits: in the ideal
   world ties ARE conjugate pairs, by a proof rather than by a census.
   That argument reads the norm of a SINGLE place and so does not bind
   where a move is a bundle -- and 12 of the element ties do straddle two
   rational primes, while still coming in conjugate pairs. The filed
   "every tie is a Galois orbit" therefore rests on two different
   footings in the two worlds, and only one of them is derived.

F5 THE LOCK ERASES A CHOICE IT SWALLOWS -- permanence in the STATE is not
   visibility at the LIMIT (rule in range; 53 element seeds over two
   rings, 27/27 and 26/26; unfrozen, the slate having frozen the element
   count as an open observable). The anticipated failure was that branches
   REJOIN; they never did, in any run, in either world. What happened
   instead is that two permanently distinct states reach ONE limit: at K23
   the element world's recurrent vehicle is (2) = P2*P2', which carries
   BOTH members of a conjugate pair, so a tie at that pair sends both
   choices to the same supernatural ideal and the branch that seated P2
   first becomes indistinguishable from the branch that seated P2'. Two
   seeds show it, where 2^t predicts 2 limits and the search finds 1. The
   corrected count is |Im| = 2^(t - e), e = the ties the lock swallowed,
   which holds at every element seed measured, and e = 0 in the ideal
   world necessarily, an ideal vehicle being a single place. This splits a
   concept the corpus treated as atomic: a free choice has a permanence
   its state can hold and a visibility only its limit can grant.
   (SINCE DERIVED, so e is no longer a residual: it counts the ties whose
   core lies in the RIDER SET -- the places a vehicle can carry as a
   passenger, which are the supports of the minimal class representatives.
   The vehicle of the basin that erases, (2) = P2*P2', is the product of
   the two, so what it swallows is exactly what a rider can carry, and
   erasure is the same route as readmission rather than a second way of
   failing to survive. The ring's OTHER element basin locks on the inert
   place over 5 and can erase nothing, so the equality is a rule in range
   over these belts.
   Holds at 27/27 and 26/26 element seeds; explore_class_species_nf.py F4.)

F6 SO ONE FORMULA COVERS THE THREE WORLDS (synthesis over three rings):
   |Im_greedy| = the product, over the trajectory's SURVIVING openings, of
   the tie multiplicity at each -- an opening surviving when its choice is
   permanent in the state AND visible at the limit. Three ring facts feed
   it: the MULTIPLICITY at an opening (1 over Z by the total order, 2 over
   K by Galois, N_q(d) over F_q[x] by cost collapse); HOW MANY openings
   there are, where the lock/sprawl dichotomy decides finite against
   endless and the ring's GEOGRAPHY decides the finite count (F3); and
   WHAT THE RECURRENT VEHICLE CARRIES, one place or a bundle that can
   swallow a pair, which decides how many of them survive (F5). The
   image is a point, a finite number (a power of 2 at these two rings,
   both quadratic -- F7) and a continuum, because the SURVIVING openings
   are none, finitely many, and endless. Surviving is the word doing the
   work: Z's trajectory opens constantly and none of its openings is a
   tie. And not because the three rings differ in arithmetic depth.
   That reading was assembled from
   two facts already filed apart, the tie census and the lock/sprawl
   characteristic dichotomy, plus the third this file had to find.
   WHAT WOULD FALSIFY IT, since a product over openings that survive can
   be read as true by construction: the content is not the survival
   criterion but the FACTORISATION -- that the count factors over
   openings at all, which needs the multiplicity at a later opening to be
   independent of the choice made at an earlier one. That is LOCKSTEP,
   and it is contingent, not definitional. A ring whose tie at one place
   changed the tie structure downstream would have an image no product
   over openings could give, and lockstep is asserted here rather than
   assumed for exactly that reason.
   (SINCE PROVED, and so no longer the contingent thing: everything these
   engines read is a function of a place's (norm, class) -- lambda reads
   (norm, depth), principality reads the class sum -- so any permutation
   preserving that colouring is an automorphism of the dynamics and carries
   one tie member of a type to another while fixing the state, which makes
   the two subtrees isomorphic. What the factorisation still rests on is
   the separate reading of a CROSS-type decline as a reordering rather than
   a choice. See explore_greedy_image_g2.py F5, F6.)
   SETTLED IN PART, and against that reading: a cross-DEGREE decline is a
   reordering, but two cores of one degree in different CLASSES are a
   CHOICE, each starving the other, so the within-type multiplicity is a
   lower bound and the count is a sum over class-branches of products
   (explore_reordering.py; SINCE WIDENED to a sum over TYPES, two clock
   moves at different degrees being a choice too -- explore_undercut.py). A conjugate pair carries INVERSE classes, so
   this ring's own ties are cross-class wherever the class has order above
   2 -- which is where the transfer to the number rings starts.
   (SINCE RUN, and the transfer lands: at h = 3 EVERY element tie is
   cross-class, no tie of either belt having a principal core, so the
   within-class product scores 1 where the breadth-first count above
   measures 2. The count here is the SUM and not the product, and the two
   rings' element worlds report one multiplicity 2 with two objects behind
   it -- a width at h = 2, a sum at h = 3. explore_class_species_nf.py
   F1, F2.)
   AND THE FORMULA COVERS THE (LAW, RING) PAIR, not only the ring -- the
   corner case is a law this file never ran. Greedy INDEPENDENCE over
   F_2[x] ties at its openings exactly as dynamics does, and still reaches
   the polynomial primorial under every tie-break
   (explore_fate_image_ff.py). A multiplicity-counting formula would give
   a continuum there and is simply wrong; this one gives ONE, because
   independence never STARVES the sibling it declines -- coprimality
   readmits it and it is seated a move later, so the tie is a REORDERING
   and the opening does not survive. Both halves of "surviving" are
   therefore load-bearing and neither is decoration: dynamics over a
   number ring loses openings to the second half (the lock swallows them),
   independence over F_2[x] loses every opening to the first.

F7 AND THE FORMULA HAS A GAP IN IT: no greedy image is COUNTABLY INFINITE
   (a derivation from F6, with no run behind it, and inheriting F6's scope
   exactly -- it is a fact about the formula, and the formula is a rule in
   range over three rings). A surviving opening is a TIE, so its
   multiplicity is at least 2, and the openings of a trajectory are a
   countable set. If finitely many survive, the product is finite. If
   infinitely many do, the choice functions number at least 2^aleph0 and
   at most aleph0^aleph0, which is the same cardinal -- so the image is
   exactly the continuum. Nothing lands between. The three measured worlds
   sit at 1, at 2^t and at the continuum, and the gap says the space
   between the finite ones and the continuum is EMPTY -- not that the
   finite ones are powers of 2, which is an accident of the sample rather
   than of the formula. Both rings run here are QUADRATIC, so |Gal| = 2
   caps every multiplicity at 2; a cubic field whose rational prime splits
   into three places ties three ways, and its finite images run over
   products of 3s as readily as of 2s. What a fourth ring can move is the
   finite VALUE; what it cannot do is land between finite and continuum.
   WHERE IT WOULD BREAK, which is the interesting half, and NOT by the
   route F5 makes obvious. The gap needs infinitely many openings to
   yield infinitely many SURVIVING ones, so falsifying it needs a ring
   with endless openings whose choices endlessly fail to survive. F5's
   mechanism cannot do it: erasure destroys VISIBILITY and needs a
   recurrent vehicle to swallow the tied pair, a recurrent vehicle is a
   lock, and a lock stops the openings -- so the two are mutually
   exclusive by construction, not merely unobserved. Equal characteristic
   cannot supply one either, its move costs DIVERGING generally (the
   crystal/absorption result, explore_module_law.py, over any
   equal-characteristic Dedekind ring with finite residue fields), which
   is the sprawl and is exactly the absence of a bounded-cost recurrent
   tail.
   The live candidate is the OTHER half, PERMANENCE, and F6's corner case
   is the template: independence loses every opening because coprimality
   READMITS the sibling it declined. A bundle can readmit too -- the
   free-rider door seats a place the branch did not choose. So the ring to
   run is equal characteristic WITH a nontrivial class group, the one cell
   of the (characteristic, class group) square this corpus has never
   touched, and the question there is whether its bundles readmit declined
   conjugates in a sprawl that never locks. F_2[x] cannot answer it: h = 1
   makes its ideal and element worlds the same world, so it has no bundle
   at all, which is why nothing was readmitted or erased there. Two
   outcomes and both are worth the run: readmission gives a finite image
   with endless openings and kills the gap, no readmission measures a
   fourth world at the continuum and leaves it standing.
   (SINCE SETTLED by explore_greedy_image_ec.py, which ran the cell over
   the complete class-group ladder at q = 2: the outcome was NEITHER of
   those two. Readmission is REAL there and the image is at the continuum
   anyway, because the rider is confined to a finite set of places and a
   readmission IS a seating -- so permanence fails at finitely many of
   endlessly many openings. The dichotomy above is the error: it read
   "bundles readmit" as an all-or-nothing property of the ring, where it
   is a BUDGET. What survives of this paragraph is the question and the
   reason F_2[x] cannot answer it.)

THE DESIGN, in six sections after the control.

 S1 THE POSITIVE CONTROL, run before any image is read. Four filed facts
    reproduced through the imported engines (the K5 ideal void's 3-lock,
    the ghost-fresh-lock wander from the K5 seed P29, the K5 element
    overture 4, 4, 9, 6 then 4 forever, and the K23 element two-basin
    tails), plus lemma B
    brute-verified as a divisibility chain over every pump shape in both
    rings. If the control fails nothing below is read.
 S2 THE IDEAL IMAGE AT K5, by two independent searches whose agreement is
    the finding. (a) PATH ENUMERATION over all tie-choice vectors, giving
    the branch logs, the lockstep check and the upper bound 2^t. (b)
    BREADTH-FIRST over the tie sets with a VISITED SET OF STATES, which
    merges any two branches that rejoin and so counts distinct limits
    rather than distinct paths. PR1 is the claim that (b) meets (a), and
    the two are compared as SETS, since a count can agree while the sets
    differ.
 S3 THE IDEAL IMAGE AT K23, the same two searches over the h = 3 ring.
 S3b THE WIDENED BELT, both rings out to norm 250, asking whether the tie
    counts the norm-40 belts show are the belt's accident or the ring's
    geography, and censusing which KIND of place each ring's pre-lock
    wander opens -- only a split place can tie.
 S4 THE ELEMENT IMAGE, both rings, the same two searches with lemma C
    withdrawn and the merge observable printed.
 S5 THE AUDIT: the per-state tie-shape and starvation records the searches
    accumulated, over every visited state and not only the filed
    trajectories.
 S6 THE THREE-WORLD TABLE, PR7's formula with the K columns filled from
    the runs and the Z and F_2[x] columns cited.

A limit is recorded only from a LOCKED branch. The lock witness is the
census's own: the same vehicle repeated for LOCK_R consecutive moves at
the price-law cost, with no tie in that window; permanence beyond the
window is the recurrence argument of explore_number_field_lock.py finding
1, not a claim of this file, so every count below is a rule IN RANGE.

Run: `python explore_greedy_image_nf.py`. RUN RECORD (3730 checks here plus
the two imported engines' own, ~0.9 s). The two searches are compared as
SETS and not merely in count at every seed of every section: they share the
door menu and nothing else, so a dedup fault in the breadth-first walk or a
lost branch in the path enumeration lands here and nowhere else.
S1 control: the pump is a divisibility chain at 252 place-depth pairs over
both rings; the K5 ideal void's 3/move column with a 2-tie at move one; the
K5 seed P29 wander (ghost at char 7, fresh P23 pair, then 23/move); the K5
element overture 4, 4, 9, 6 then 4 forever; the K23 element tails at 4 and
25, two basins. S2 K5 ideal, 52 seeds: t = 0 at 35 seeds (1 limit), t = 1
at 15 (2), t = 2 at 2 (4); 0 branch merges; wander moves {ram 34, split 2}.
S3 K23 ideal, 79 seeds: t = 0 at 65, t = 1 at 14; 0 merges; wander {ram 2}.
S3b the widened belt at norm <= 250: K5 351 seeds {0: 222, 1: 121, 2: 8},
wander {ram 182, split 10}; K23 495 seeds {0: 382, 1: 113}, wander {ram
50}. S4 element, 26 seeds at K5 (36 paths, 36 distinct) and 27 at K23 (33
paths, 31 distinct): 0 state merges in both, 2^t met at 26/26 and 25/27,
2^(t-e) met at 26/26 and 27/27; the two K23 misses are the seeds (2) and
(2)^2, each with one tie erased by the (2) = P2*P2' vehicle. S5 audit: 618
tie-set encounters, all of multiplicity 2 and all conjugate pairs, 606 over
one rational prime and 12 straddling two (element only), 586 with equal
door exponents (ideal only); 2308 starvation checks; 1484 ideal states
product-scanned for a cheaper composite move, 0 above the scan cap.
Lockstep carries content at 17 of 52 K5 seeds and 14 of 79 K23 seeds --
the rest have a single branch. Slate PR1-PR7: all
hit, no misses; PR6 was frozen as an open observable and printed the
erasure, which amended PR7's formula with its third ring fact. Unfrozen
finds: the erasure itself, the wander-kind mechanism behind F3, and the
element ties that straddle two rational primes.
"""

import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_number_field_lock as K5      # the h = 2 ring (lineage)
import explore_module_law as K23            # the h = 3 ring (lineage)

CHECKS = 0

T_CAP = 40          # moves per branch, the census horizon
LOCK_R = 10         # consecutive identical vehicles that witness a lock
PATH_CAP = 4096     # tie-choice vectors enumerated before giving up
NODE_CAP = 20000    # search nodes before giving up

RINGS = [("K5", K5, "Z[sqrt(-5)], h = 2"),
         ("K23", K23, "Z[w], w^2 = w - 6, h = 3")]


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 68)
    print(t)
    print("=" * 68)


def frz(st):
    """Hashable state key: the nonzero exponents, place-sorted."""
    return tuple(sorted(((repr(pl), e) for pl, e in st.items() if e)))


def show_place(pl):
    if pl[0] == 'split':
        return "P%d.%d" % (pl[1], pl[2])
    if pl[0] == 'inert':
        return "Q%d" % pl[1]
    return "R%d" % pl[1]


def show_state(st):
    parts = ["%s^%s" % (show_place(pl), e)
             for pl, e in sorted(st.items(), key=lambda kv: (kv[1] == 'oo',
                                                             repr(kv[0])))
             if e]
    return "*".join(parts) if parts else "(1)"


# ------------------------------------------------------------- the two menus
# Both worlds are reduced to one interface: a MENU is (cost, [vehicle]),
# a vehicle is a dict {place: exponent} the move multiplies into the state.

def menu_ideal(M, st, L):
    cost, ties = M.ideal_menu(st, L)
    return cost, [{pl: r} for (pl, r) in ties]


def menu_elem(M, st, L):
    n, hits = M.elem_menu(st, L)
    return n, [fac for (yx, fac) in hits]


MENUS = {"ideal": menu_ideal, "element": menu_elem}


def apply_vehicle(st, veh):
    out = dict(st)
    for pl, e in veh.items():
        out[pl] = out.get(pl, 0) + e
    return out


def vkey(veh):
    return tuple(sorted((repr(pl), e) for pl, e in veh.items()))


# ------------------------------------------------------------- the audits
class Audit(object):
    """Per-state records the searches accumulate, over every visited state."""

    def __init__(self):
        self.tie_sizes = {}       # multiplicity -> count of tie states
        self.tie_states = 0
        self.conj_pairs = 0       # tie sets that are a conjugate pair
        self.one_char = 0         # tie sets over a single rational prime
        self.equal_r = 0          # tie sets whose door exponents agree
        self.starve = 0           # starvation instances checked
        self.elem_multichar = 0   # element tie sets spanning two rat. primes
        self.scanned = 0          # states whose menu was product-scanned
        self.scan_skipped = 0     # states whose door exceeded the scan cap
        self.lockstep_seeds = 0   # seeds where lockstep has content (t >= 1)
        self.starve_bad = []
        self.tie_bad = []

    def tie(self, M, world, st, cost, vehs):
        self.tie_states += 1
        self.tie_sizes[len(vehs)] = self.tie_sizes.get(len(vehs), 0) + 1
        chars = set()
        for veh in vehs:
            for pl in veh:
                chars.add(M.place_char(pl))
        if len(chars) == 1:
            self.one_char += 1
        elif world == "ideal":
            self.tie_bad.append(("multi-char", show_state(st), cost))
        else:
            self.elem_multichar += 1
        if len(vehs) == 2:
            a, b = vehs
            ca = dict((M.conj_place(pl), e) for pl, e in a.items())
            if vkey(ca) == vkey(b):
                self.conj_pairs += 1
            elif world == "ideal":
                self.tie_bad.append(("not conjugate", show_state(st), cost))
            if world == "ideal":
                ra, = a.values()
                rb, = b.values()
                if ra == rb:
                    self.equal_r += 1
                else:
                    self.tie_bad.append(("unequal r", show_state(st), cost))

    def minimal(self, M, st, L, cost, vehs):
        """THE MENU ITSELF, at a state no filed trajectory reached. The door
        menu offers PRIME-POWER moves; that the true minimum is never a
        COMPOSITE ideal is verified by a full product scan in the two source
        files, but only at their own census states. The searches here visit
        states off every filed trajectory, so the scan is re-run at each of
        them -- otherwise 'the minimal-move policy class' is an assumption
        exactly where the measurement is new."""
        if cost > M.SCAN_CAP:
            self.scan_skipped += 1
            return
        M.scan_check(st, L, cost, [next(iter(v.items())) for v in vehs])
        self.scanned += 1

    def starvation(self, M, st, L):
        """PR4 at one state: a seated split place strictly dominates its
        unseated conjugate."""
        for pl, e in st.items():
            if e == 0 or pl[0] != 'split':
                continue
            cj = M.conj_place(pl)
            if st.get(cj, 0) > 0:
                continue
            own = M.place_norm(pl) ** M.door_r(pl, e, L)
            sib = M.place_norm(cj) ** M.door_r(cj, 0, L)
            self.starve += 1
            if not sib > own:
                self.starve_bad.append((show_state(st), show_place(pl),
                                        own, sib))


# ------------------------------------------------------- the two searches
def lock_probe(M, world, st, L, budget):
    """Forward-simulate deterministically to the END of the horizon. Returns
    the lock vehicle if every remaining move is that one vehicle with no tie
    anywhere, else None -- so a tie appearing late cannot be missed."""
    if budget < LOCK_R:
        return None
    menu = MENUS[world]
    s, l, first = dict(st), L, None
    for i in range(budget):
        cost, vehs = menu(M, s, l)
        if len(vehs) != 1:
            return None
        if first is None:
            first = vehs[0]
        elif vkey(vehs[0]) != vkey(first):
            return None
        s = apply_vehicle(s, vehs[0])
        l = M.lam_state(s)
    return first


def limit_of(st, veh):
    """The supernatural ideal: the frozen exponents, the vehicle at oo."""
    lim = dict((pl, e) for pl, e in st.items() if e)
    for pl in veh:
        lim[pl] = 'oo'
    return lim


def enumerate_paths(M, world, seed, audit):
    """PATH search: every tie-choice vector, run to the lock. A log entry is
    (cost, kind, char, r, tie multiplicity, the tie's place set). Returns
    (paths, sigs, limits, ties_per_path, erased_per_path, note)."""
    menu = MENUS[world]
    paths, sigs, limits, ties_seen, erased = [], [], [], [], []
    stack = [(dict(seed), M.lam_state(seed), [], 0)]
    note = ""

    def close(log, st, veh):
        paths.append(log)
        sigs.append(tuple((c, k, ch, r) for (c, k, ch, r, _, _) in log))
        limits.append(None if veh is None else limit_of(st, veh))
        ties_seen.append(sum(1 for mv in log if mv[4] > 1))
        # A TIE IS ERASED when the lock vehicle swallows BOTH tied places:
        # the limit sends them to infinity together and forgets which branch
        # seated which. Permanence in the STATE is not visibility at the LIMIT.
        swallowed = set() if veh is None else set(repr(pl) for pl in veh)
        erased.append(sum(1 for mv in log
                          if mv[4] > 1 and mv[5] <= swallowed))

    while stack:
        st, L, log, used = stack.pop()
        if len(paths) >= PATH_CAP:
            note = "path cap %d hit" % PATH_CAP
            break
        veh = lock_probe(M, world, st, L, T_CAP - used)
        if veh is not None:
            close(log, st, veh)
            continue
        if used >= T_CAP:
            note = "a branch reached the move cap without locking"
            close(log, st, None)
            continue
        cost, vehs = menu(M, st, L)
        audit.starvation(M, st, L)
        if world == "ideal":
            audit.minimal(M, st, L, cost, vehs)
        tieset = frozenset(repr(pl) for v in vehs for pl in v)
        if len(vehs) > 1:
            audit.tie(M, world, st, cost, vehs)
        for veh in vehs:
            pl = sorted(veh, key=M.place_key)[0]
            kind = (M.classify(st, L, pl, veh[pl]) if len(veh) == 1
                    else 'bundle')
            entry = (cost, kind, M.place_char(pl), veh[pl], len(vehs), tieset)
            child = apply_vehicle(st, veh)
            stack.append((child, M.lam_state(child), log + [entry], used + 1))
    return paths, sigs, limits, ties_seen, erased, note


def bfs_limits(M, world, seed, audit):
    """BFS over the tie sets with a VISITED SET OF STATES: states reached by
    two branches are expanded once, so what is counted is distinct LIMITS.
    Returns (limits, nodes, merges, note)."""
    menu = MENUS[world]
    start = dict(seed)
    seen = {frz(start): 0}
    frontier = [(start, M.lam_state(start), 0)]
    limits, nodes, merges, note = [], 0, 0, ""
    while frontier:
        nxt = []
        for st, L, used in frontier:
            nodes += 1
            if nodes > NODE_CAP:
                note = "node cap %d hit" % NODE_CAP
                return limits, nodes, merges, note
            veh = lock_probe(M, world, st, L, T_CAP - used)
            if veh is not None:
                limits.append(limit_of(st, veh))
                continue
            if used >= T_CAP:
                note = "a branch reached the move cap without locking"
                continue
            cost, vehs = menu(M, st, L)
            audit.starvation(M, st, L)
            if world == "ideal":
                audit.minimal(M, st, L, cost, vehs)
            if len(vehs) > 1:
                audit.tie(M, world, st, cost, vehs)
            for v in vehs:
                child = apply_vehicle(st, v)
                key = frz(child)
                if key in seen:
                    merges += 1
                    continue
                seen[key] = used + 1
                nxt.append((child, M.lam_state(child), used + 1))
        frontier = nxt
    return limits, nodes, merges, note


def limkey(lim):
    return tuple(sorted((repr(pl), str(e)) for pl, e in lim.items() if e))


def image_of(M, world, seed, audit):
    """The greedy image from one seed, by both searches. Returns a record."""
    paths, sigs, plims, ties, erased, pnote = enumerate_paths(
        M, world, seed, audit)
    blims, nodes, merges, bnote = bfs_limits(M, world, seed, audit)
    pset = set(limkey(l) for l in plims if l is not None)
    bset = set(limkey(l) for l in blims)
    # THE TWO SEARCHES MUST AGREE AS SETS, not merely in count. They share
    # the menu and nothing else: one enumerates tie-choice vectors depth
    # first with no dedup, the other walks levels with a visited state set.
    # A dedup bug in the second or a lost branch in the first shows up here
    # and nowhere else, since a count can coincide while the sets differ.
    ok(pset == bset,
       "the two searches disagree from %s: paths %d, bfs %d, symmetric "
       "difference %s" % (show_state(seed), len(pset), len(bset),
                          sorted(pset ^ bset)[:2]))
    # NO SILENT CAPS: either search can give up on a big enough seed, and a
    # truncated search reports a SMALLER image, which is the one direction
    # that reads as a clean measurement. The note is asserted empty rather
    # than recorded and forgotten.
    note = (pnote + " " + bnote).strip()
    ok(not note, "a search truncated from %s: %s" % (show_state(seed), note))
    return {
        "seed": seed, "paths": len(paths), "sigs": set(sigs),
        "t": ties[0] if ties else 0, "t_all": set(ties),
        "erased": erased[0] if erased else 0, "erased_all": set(erased),
        "bfs_limits": bset, "blims": blims,
        "nodes": nodes, "merges": merges,
        "unlocked": sum(1 for l in plims if l is None),
    }


# ------------------------------------------------------------------ seeds
def ideal_seeds(M, cap=40):
    out = [{}]
    for nrm, m in M.gen_products(cap):
        out.append(dict(m))
    return out


def element_seeds(M, cap=40):
    out = [{}]
    for n in range(2, cap + 1):
        for (y, x) in M.elem_candidates(n):
            out.append(M.factor_elem(x, y))
    return out


# --------------------------------------------------------------- S1 control
def s1_control():
    section("S1  THE POSITIVE CONTROL -- filed facts through the imported "
            "engines")

    # (a) lemma B: the pump is a divisibility CHAIN at every shape.
    chain = 0
    for name, M, _ in RINGS:
        for pl in M.UNIVERSE[:14]:
            for a in range(0, 9):
                ok(M.lam_P(pl, a + 1) % M.lam_P(pl, a) == 0,
                   "lemma B: %s %s a=%d not a divisibility chain"
                   % (name, pl, a))
                chain += 1
    print("  lemma B (the pump is a divisibility chain, so the door exponent")
    print("  is max(1, A - e)): %d place-depth pairs, both rings, exact."
          % chain)

    # (b) the K5 ideal void: Z's 3-lock verbatim, up to the Galois tie.
    log, st, L = K5.run_ideal({}, 12)
    ok(all(c == 3 for (pl, r, c, kind, nt) in log),
       "control: the K5 ideal void is not a 3/move column")
    ok(log[0][4] == 2, "control: the K5 void's first move is not a tie")
    print("  K5 ideal void:      %s -- cost 3/move, first move a 2-tie"
          % " ".join(show_place(mv[0]) for mv in log[:4]))

    # (c) the K29 wander: ghost -> fresh -> lock.
    r29 = K5.SPLIT_ROOT[29]
    log, st, L = K5.run_ideal({('split', 29, r29): 1}, 12)
    kinds = [mv[3] for mv in log[:3]]
    ok(kinds[0] == 'ghost' and K5.place_char(log[0][0]) == 7,
       "control: K5 seed P29 does not ghost at char 7")
    ok(K5.place_char(log[1][0]) == 23 and log[1][3] == 'fresh',
       "control: K5 seed P29 does not reach the fresh P23 pair")
    ok(all(mv[2] == 23 for mv in log[2:]),
       "control: K5 seed P29 does not lock at 23")
    print("  K5 ideal seed P29:  %s -- ghost 7, fresh 23, then 23/move"
          % " ".join("%s(%s)" % (show_place(mv[0]), mv[3]) for mv in log[:3]))

    # (d) the K5 element overture and the K23 element basins.
    log, st, L = K5.run_elem({}, 8)
    norms = [mv[2] for mv in log]
    ok(norms == [4, 4, 9, 6, 4, 4, 4, 4],
       "control: the K5 element overture is %s" % norms)
    print("  K5 element void:    norms %s -- the free-rider overture"
          % norms[:6])
    tails = set()
    for seed in ({}, {('inert', 5): 1}):
        log, st, L = K23.run_elem(seed, 20)
        tails.add(log[-1][2])
    ok(tails == {4, 25}, "control: the K23 element basins are %s" % tails)
    print("  K23 element basins: tail norms %s -- two basins, not one"
          % sorted(tails))
    print("\n  Control green: the imported engines reproduce the filed facts.")


# ------------------------------------------------------------- S2/S3 ideals
def run_ideal_world(name, M, blurb, audit):
    section("S%s  THE IDEAL IMAGE AT %s (%s)"
            % ("2" if name == "K5" else "3", name, blurb))
    seeds = ideal_seeds(M)
    print("  %d seeds: the void + every place-power product of norm <= 40.\n"
          % len(seeds))
    by_t, mismatches, unlocked, merges = {}, [], 0, 0
    specimens = []
    for seed in seeds:
        rec = image_of(M, "ideal", seed, audit)
        unlocked += rec["unlocked"]
        merges += rec["merges"]
        ok(len(rec["t_all"]) == 1,
           "PR5/PR1: branches from %s disagree on the tie count: %s"
           % (show_state(seed), rec["t_all"]))
        ok(len(rec["sigs"]) == 1,
           "PR5 lockstep: %d distinct (cost, kind, char, r) sequences from %s"
           % (len(rec["sigs"]), show_state(seed)))
        # a seed with t = 0 has ONE branch, so the lockstep check passes
        # there for want of a second sequence to disagree with: count the
        # seeds where it has content, and report that rather than the total
        if rec["t"] >= 1:
            audit.lockstep_seeds += 1
        # An ideal vehicle is ONE place, so it can never swallow a conjugate
        # pair whole: no tie is erased here, and 2^t is the honest count.
        ok(rec["erased_all"] == {0},
           "an ideal lock vehicle swallowed a tie at %s" % show_state(seed))
        t = rec["t"]
        got = len(rec["bfs_limits"])
        if got != 2 ** t:
            mismatches.append((show_state(seed), t, got))
        by_t.setdefault(t, []).append((seed, rec))
        if t >= 1 and seed:
            specimens.append((seed, rec))
    # the richest images first: the headline is a seed whose image EXCEEDS
    # the Galois orbit, where one exists in the belt
    specimens.sort(key=lambda sr: -sr[1]["t"])
    specimens = specimens[:2]
    ok(unlocked == 0, "%d branches reached the move cap without locking"
       % unlocked)
    ok(not mismatches, "PR1: distinct limits != 2^t at %s" % mismatches[:3])

    print("  %-6s %-8s %-10s %-12s %s"
          % ("t", "seeds", "2^t", "distinct", "reading"))
    for t in sorted(by_t):
        seeds_t = by_t[t]
        got = set(len(r["bfs_limits"]) for _, r in seeds_t)
        reading = ("a POINT (Z-like)" if t == 0 else
                   "a Galois ORBIT" if t == 1 else
                   "STRICTLY BIGGER than an orbit")
        print("  %-6d %-8d %-10d %-12s %s"
              % (t, len(seeds_t), 2 ** t,
                 ",".join(str(g) for g in sorted(got)), reading))
    print("\n  branch merges seen by the visited set: %d "
          "(a merge would drop the count below 2^t)" % merges)
    live = sum(len(v) for t, v in by_t.items() if t >= 1)
    print("  seeds where LOCKSTEP has content: %d of %d -- a t = 0 seed has"
          % (live, len(seeds)))
    print("  ONE branch, so its lockstep check passes for want of a rival")
    print("  sequence and is not evidence for the lemma.")

    # WHERE A SECOND CHOICE COMES FROM: t >= 2 needs the pre-lock WANDER to
    # open a split pair, since a ramified or inert place is Galois-fixed and
    # cannot tie. Counted through the module's own deterministic runner.
    wk = {}
    for seed in seeds:
        log, _, _ = M.run_ideal(seed, 25)
        lockpl = log[-1][0]
        w = next(i for i, mv in enumerate(log) if mv[0] == lockpl)
        for mv in log[:w]:
            wk[mv[0][0]] = wk.get(mv[0][0], 0) + 1
    print("  pre-lock WANDER moves by place kind: %s" % (dict(sorted(wk.items()))
                                                        or "none"))
    print("  -- a ramified or inert place is Galois-FIXED and never ties, so")
    print("  only a split wander can raise t above the lock's own opening.")

    print("\n  Specimens -- the tie-choice vectors and where they land:")
    for seed, rec in specimens:
        print("    seed %-12s t = %d, %d limits:"
              % (show_state(seed), rec["t"], len(rec["bfs_limits"])))
        for lim in sorted(rec["blims"], key=lambda l: show_state(l))[:4]:
            print("      %s" % show_state(lim))
    return by_t


# --------------------------------------------------- S3b the widened belt
WIDE = 250


def s3b_wide(audit):
    section("S3b THE WANDER IS THE SOURCE -- a wider belt, both rings")
    print("  t >= 2 needs TWO split openings, so it needs the pre-lock wander")
    print("  to pass through a split pair. The norm-40 belts above show t = 2")
    print("  at K5 and not at K23; this widens both to norm <= %d to ask"
          % WIDE)
    print("  whether that is the belt's accident or the ring's geography.\n")
    print("  %-6s %-8s %-26s %s" % ("ring", "seeds", "t histogram",
                                    "wander moves by kind"))
    out = {}
    for name, M, _ in RINGS:
        hist, wk = {}, {}
        for nrm, m in M.gen_products(WIDE):
            seed = dict(m)
            rec = image_of(M, "ideal", seed, audit)
            ok(len(rec["bfs_limits"]) == 2 ** rec["t"],
               "PR1 outside the norm-40 belt at %s" % show_state(seed))
            hist[rec["t"]] = hist.get(rec["t"], 0) + 1
            log, _, _ = M.run_ideal(seed, 25)
            lockpl = log[-1][0]
            w = next(i for i, mv in enumerate(log) if mv[0] == lockpl)
            for mv in log[:w]:
                wk[mv[0][0]] = wk.get(mv[0][0], 0) + 1
        out[name] = (hist, wk)
        print("  %-6s %-8d %-26s %s"
              % (name, sum(hist.values()), dict(sorted(hist.items())),
                 dict(sorted(wk.items()))))
    ok(max(out["K5"][0]) >= 2, "K5 lost its t = 2 seeds on the wider belt")
    ok(max(out["K23"][0]) <= 1,
       "K23 has a t >= 2 seed on the wider belt -- the reading below changes")
    # the printed sentence below says ONLY ramified, so that is what is
    # asserted -- "no split" would be a weaker check than the claim it guards
    ok(set(out["K23"][1]) == {"ram"},
       "K23's wander is not ramified-only: %s" % out["K23"][1])
    print("\n  K23 wanders ONLY through ramified places, which are")
    print("  Galois-fixed and cannot tie, so its wander spends no choice;")
    print("  K5's wander opens the split 7-pair and spends one. Whether the")
    print("  image can EXCEED a Galois orbit is therefore decided by which")
    print("  places the ring makes cheap -- geography, and not h or the")
    print("  class group. Rule IN RANGE, and a null result at K23: no t >= 2")
    print("  seed was FOUND there, which is not a proof that none exists.")


# ------------------------------------------------------------- S4 elements
def s4_element(audit):
    section("S4  THE ELEMENT IMAGE -- where flag 4 withdraws the starvation")
    print("  An element move seats a BUNDLE, so an unchosen conjugate can be")
    print("  seated later by a rider and two branches can rejoin. No count")
    print("  is predicted here (PR6); the merge is the observable.\n")
    print("  %-5s %-7s %-9s %-8s %-9s %-8s %-9s %s"
          % ("ring", "seeds", "t range", "paths", "distinct", "state",
             "2^t met", "2^(t-e) met"))
    print("  %-5s %-7s %-9s %-8s %-9s %-8s %-9s %s"
          % ("", "", "", "", "", "merges", "", ""))
    out, short = {}, {}
    for name, M, _ in RINGS:
        seeds = element_seeds(M)
        tmax, tmin, npaths, ndist, nmerge = 0, 99, 0, 0, 0
        met, met_e, rows = 0, 0, []
        for seed in seeds:
            rec = image_of(M, "element", seed, audit)
            ok(rec["unlocked"] == 0,
               "an element branch from %s hit the move cap unlocked"
               % show_state(seed))
            ok(len(rec["t_all"]) == 1,
               "element branches from %s disagree on the tie count: %s"
               % (show_state(seed), rec["t_all"]))
            ok(len(rec["erased_all"]) == 1,
               "element branches from %s disagree on the erased count: %s"
               % (show_state(seed), rec["erased_all"]))
            t, e = rec["t"], rec["erased"]
            tmax, tmin = max(tmax, t), min(tmin, t)
            npaths += rec["paths"]
            got = len(rec["bfs_limits"])
            ndist += got
            nmerge += rec["merges"]
            met += (got == 2 ** t)
            met_e += (got == 2 ** (t - e))
            if got != 2 ** t:
                rows.append((show_state(seed), t, e, got))
        out[name] = (len(seeds), tmin, tmax, npaths, ndist, nmerge)
        short[name] = rows
        print("  %-5s %-7d %-9s %-8d %-9d %-8d %-9s %s"
              % (name, len(seeds), "%d..%d" % (tmin, tmax), npaths, ndist,
                 nmerge, "%d/%d" % (met, len(seeds)),
                 "%d/%d" % (met_e, len(seeds))))
        ok(met_e == len(seeds),
           "the surviving-tie count missed at %s" % rows[:3])
    for name in short:
        if short[name]:
            print("\n  %s seeds where 2^t OVERCOUNTS -- and what the lock did"
                  " (seed, t, erased, distinct):" % name)
            for row in short[name][:6]:
                print("    %-24s t = %d, erased %d -> %d limits" % row)
    print("\n  THE ERASURE, unfrozen (PR6 froze the element count as an open")
    print("  observable and this is what it printed). A tie choice is")
    print("  permanent in the STATE by the starvation, and the state merges")
    print("  are %d in every run above -- yet a choice is invisible at the"
          % sum(v[5] for v in out.values()))
    print("  LIMIT when the lock vehicle swallows BOTH tied places, which an")
    print("  element vehicle can do and an ideal vehicle cannot. Distinct")
    print("  limits = 2^(t - e), e = the ties the lock swallowed.")


# ------------------------------------------------------------------ S5/S6
def s5_audit(audit):
    section("S5  THE AUDIT -- every state the two searches visited")
    print("  tie-set encounters (both searches, every seed, both worlds and")
    print("  both rings -- instances checked, not distinct states): %d"
          % audit.tie_states)
    print("  tie-set multiplicities:        %s"
          % dict(sorted(audit.tie_sizes.items())))
    print("  tie sets over ONE rational prime: %d" % audit.one_char)
    print("  tie sets spanning TWO rational primes: %d (element world only --"
          % audit.elem_multichar)
    print("    a BUNDLE carries several places, so lemma A's cost argument,")
    print("    which reads the norm of a single place, does not bind there)")
    print("  tie sets that are a conjugate pair: %d" % audit.conj_pairs)
    print("  tie sets with equal door exponents: %d (ideal world only)"
          % audit.equal_r)
    ok(not audit.tie_bad, "PR3: ideal-world tie shape violated: %s"
       % audit.tie_bad[:3])
    ok(audit.conj_pairs == audit.tie_states,
       "a tie set was not a conjugate pair: %d of %d"
       % (audit.conj_pairs, audit.tie_states))
    print("  starvation checks (a seated split place vs its unseated")
    print("  conjugate):                    %d" % audit.starve)
    print("  ideal states whose MENU was product-scanned (no cheaper")
    print("  COMPOSITE ideal ticks, and the min-cost tickers are exactly")
    print("  the menu's ties):              %d, %d above the scan cap"
          % (audit.scanned, audit.scan_skipped))
    ok(audit.scanned > 0, "the menu was never product-scanned")
    print("  -- the source files run this scan at their own census states")
    print("  only; these are the states off every filed trajectory, where")
    print("  'the minimal move' would otherwise be an assumption.")
    ok(not audit.starve_bad, "PR4: starvation failed at %s"
       % audit.starve_bad[:3])
    print("\n  PR3 and PR4 hold at every visited state, on and off the filed")
    print("  trajectories -- lemma A and lemma C are what the census saw.")
    print("  Every tie in BOTH worlds is a conjugate pair; in the element")
    print("  world that is a measurement and not lemma A, since the tie can")
    print("  straddle two rational primes there.")


def s6_three_worlds(k5_by_t, k23_by_t):
    section("S6  THE THREE-WORLD TABLE -- one formula, three ring facts")
    print("  |Im_greedy| = the product, over the trajectory's SURVIVING")
    print("  openings, of the tie multiplicity at each. An opening survives")
    print("  when its choice is permanent in the state (the starvation) AND")
    print("  visible at the limit (the lock does not swallow the tied places")
    print("  whole). Three ring facts feed it: the MULTIPLICITY at an")
    print("  opening; HOW MANY openings there are -- the lock/sprawl")
    print("  dichotomy deciding finite against endless, and the ring's")
    print("  geography deciding the finite count, since a second choice")
    print("  needs the wander itself to open a split pair; and WHAT THE")
    print("  RECURRENT VEHICLE CARRIES, which decides how many survive.\n")
    print("  %-13s %-15s %-14s %-11s %s"
          % ("ring, world", "multiplicity", "openings", "vehicle",
             "|Im_greedy|"))
    print("  %-13s %-15s %-14s %-11s %s"
          % ("Z", "1 (order)", "stop (lock)", "one prime", "1, a point"))
    ks = sorted(set(k5_by_t) | set(k23_by_t))
    print("  %-13s %-15s %-14s %-11s %s"
          % ("K, ideal", "2 (Galois)", "stop (lock)", "one place",
             "2^t, t in %s" % ks))
    print("  %-13s %-15s %-14s %-11s %s"
          % ("K, element", "2 (Galois)", "stop (lock)", "a BUNDLE",
             "2^(t-e), e = swallowed"))
    print("  %-13s %-15s %-14s %-11s %s"
          % ("F_q[x]", "N_q(d)", "never (sprawl)", "one place",
             "the continuum"))
    print("\n  The Z row is explore_fate_image.py's and the F_q[x] row is")
    print("  explore_fate_image_ff.py's; the two K rows are this file's. The")
    print("  cardinality is a point, a finite number and a continuum because")
    print("  the SURVIVING openings are none, finitely many and endless --")
    print("  Z's trajectory opens constantly and none of its openings ties --")
    print("  and NOT because the three rings differ in arithmetic depth.")


def main():
    audit = Audit()
    s1_control()
    k5 = run_ideal_world("K5", K5, "Z[sqrt(-5)], h = 2", audit)
    k23 = run_ideal_world("K23", K23, "Z[w], w^2 = w - 6, h = 3", audit)
    s3b_wide(audit)
    s4_element(audit)
    s5_audit(audit)
    s6_three_worlds(k5, k23)
    print("\nALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
