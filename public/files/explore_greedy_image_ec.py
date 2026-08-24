"""explore_greedy_image_ec.py -- THE FOURTH RING: equal characteristic WITH a
nontrivial class group, and what it does to the greedy image.

THE QUESTION. |Im_greedy| = the product, over a trajectory's SURVIVING
openings, of the tie multiplicity at each -- one formula fitting three rings,
with a GAP in it: a surviving opening is a tie, so its multiplicity is at
least 2, and countably many surviving openings give the continuum while
finitely many give a finite number. No greedy image is countably infinite
(explore_greedy_image_nf.py F6, F7). That is a fact about the FORMULA, and
the formula is a rule in range over three rings: Z, two quadratic number
rings, and F_2[x]. The three sit at the corners of a (characteristic, class
group) square with ONE cell untouched -- equal characteristic with h > 1.
F_2[x] cannot fill it: h = 1 makes its ideal and element worlds one world,
so it has no BUNDLE, and a bundle is the only known way for a declined
choice to be readmitted. What does the fourth cell do?

THE RING. R = the affine coordinate ring of an elliptic curve E over F_q --
the functions regular away from the point at infinity O. It is Dedekind, of
equal characteristic p, with finite residue fields and finitely many places
per norm bound, and Pic(R) = Pic^0(E) = E(F_q), nontrivial as soon as
#E(F_q) >= 2. Its PLACES are the closed points of E other than O: Galois
orbits of geometric points, of degree d = orbit size, norm q^d, residue
field F_{q^d}. Taking q = 2 makes this the MINIMAL change against F_2[x],
which is the coordinate ring of the affine line -- the same characteristic,
the same residue-field ladder, the same lambda law. Only the class group
moves, and over F_2 it moves through its whole range: #E(F_2) in {1..5} by
Hasse, so the four nontrivial values 2, 3, 4, 5 are the complete ladder, and
F_2[x] itself is the h = 1 control this engine must reproduce.

THE TWO WORLDS. IDEAL: a state is an effective affine divisor, a move is the
least-degree effective divisor raising lambda. ELEMENT: states and moves are
PRINCIPAL. An effective affine divisor D = sum n_i P_i is principal in R
exactly when sigma(D) := sum n_i * (the sum of P_i's geometric points) = O
in E(F_q) -- the summation map IS the class map, and it is one application of
the group law. That is why an elliptic curve is the least machinery for this
cell: the bundle constraint costs a group addition per divisor.

THE LAMBDA PUMP (Theorem A, equal characteristic, explore_module_law.py):
lam_P(a) = lcm(q^d - 1, p^ceil(log_p a)) for a >= 1, and 1 at a = 0. It
reads (degree, depth) and nothing else -- no place-individual content -- so
same-degree places are cost-identical and ties are generic, as over F_2[x].
The residue fields this ring actually has are F_4, F_8, F_16, ... which the
source file never ran (it ran F_2, F_3, F_9), so the law is re-brute-verified
here at the fields in play.

TRANSPLANT FLAGS, fixed at the freeze. Every intuition below is imported from
a neighbouring value of the ring parameter and is marked rather than trusted.
 1. From F_2[x]: "the sibling starvation makes each choice permanent." That
    is an argument about degree classes in a ring where every divisor is
    principal. It is re-derived here for the IDEAL world only (lemma C) and
    asserted at every visited state; it is NOT carried into the element
    world, which is where a bundle can readmit.
 2. From the number rings: "a tie is a Galois orbit / a conjugate pair."
    False here. A tie is a COST class -- equal d*r -- and can straddle
    degrees. None of that file's tie audits transfer.
 3. From explore_module_law.py Theorem B(ii): "equal-characteristic move
    costs diverge." Derived there for SINGLE-PLACE moves. The bundle
    extension is lemma D below and is MEASURED here, not assumed.
 4. From explore_greedy_image_nf.py: its searches close a branch at a LOCK.
    Equal characteristic never locks, so there is no finite limit to
    enumerate and the observable itself must change (see THE OBSERVABLE).

THE HAND-ATTACK, on paper before any engine code, in four lemmas. The rig
asserts each of them at the states it visits rather than assuming any.

 A. THE DOOR LAW IS F_2[x]'s VERBATIM. With d = deg P, e = the depth of P,
    c = v2(lambda), lambda_odd = lambda >> c:
      DEEPEN  (e >= 1):                             r = 2^c + 1 - e, cost d*r
      FRESH   (e = 0, (2^d - 1) does not divide lambda_odd): r = 1, cost d
      CLOCKED (e = 0, (2^d - 1) divides lambda_odd):   r = 2^c + 1, cost
                                                       d*(2^c + 1)
    Cost is measured as the DEGREE of the vehicle, the canonical transfer of
    "least m" (norm q^deg, so degree order is norm order). No ghosts: state
    and clock live in different monoids, the same type separation as F_2[x].
    So the only two things this ring changes against F_2[x] are the
    POPULATION per degree (genus-1 geometry) and the PRINCIPALITY constraint
    (the class group). One dial each.
 B. THE MINIMAL IDEAL MOVE IS A SINGLE-PLACE POWER. lambda(state + D) is an
    lcm over places, so D raises it exactly when some P^{n_P} in D does; then
    n_P >= door_r(P) and deg D >= d_P * n_P >= min over P of d_P*door_r(P).
    The minimisers are therefore exactly the single-place powers, which is
    Theorem B's bundle argument at this ring.
 C. IDEAL-WORLD PERMANENCE. A seated place's own deepening door costs
    d*(2^c + 1 - e) <= d*2^c, while an unseated place of the same degree is
    CLOCKED (its 2^d - 1 already divides lambda) at d*(2^c + 1) -- strictly
    more, at every state. A declined tie member is never readmitted in the
    ideal world, so ideal openings are permanent.
 D. THE FREE RIDER IS ALWAYS A RATIONAL POINT, and the bundle is minimal.
    For a class c != O the point c itself is an affine place of degree 1 with
    sigma = c, so every nonzero class contains a degree-1 place and the
    minimal completion of a core P^r has degree exactly [r*sigma(P) != O],
    i.e. 0 or 1. Hence every element move is a core plus at most ONE rational
    point, of degree at most the ideal minimum plus one, and the rider is
    DETERMINED by the core's class: it is the rational point -r*sigma(P). By
    the same minimality every minimal element vehicle is generated as
    core-plus-rider, so that construction is complete and not a heuristic.
 E. THE SPRAWL COVERS BUNDLES. Suppose every move past t0 has degree <= B.
    Norm-finiteness makes the vehicles past t0 a finite set, so the support
    stops growing and the multiplicities per move are bounded by some m.
    After M further moves no depth exceeds C + M*m, the (q^d - 1) factors are
    frozen, and every tick must come from some depth crossing a p-power
    frontier -- at most |S|*(log_p(C + M*m) + 1) of those, against the M ticks
    M moves require. That fails for large M, so costs diverge in EITHER
    world. Flag 3's extension, derived here and measured below.

THE OBSERVABLE, and why it is not the number-ring one. With no lock there is
no finite limit to enumerate, so "count the limits" is not a finite question.
What IS finite and decidable at a horizon is the two halves of SURVIVING:
 (i) PERMANENCE -- at an opening the greedy declines a member; does a later
     move of the SAME branch seat a place that member carried? Lemma C says
     no in the ideal world. A bundle can say yes in the element world, and
     that is the live question this cell was built to ask.
 (ii) LOCKSTEP -- do two branches differing only in which tie member they
     take carry the identical (cost, kind, degree, exponent) sequence? This
     is what makes the count FACTOR over openings, and the source file
     names it as the formula's one contingent assumption. (Its findings are
     numbered F1.. as well; every bare F-number below is THIS file's, and a
     reference to the source file's says so.)
Readmission alone cannot falsify the gap: if every opening fails to survive
the product is empty and the image is a POINT, which is finite and leaves the
gap standing. The gap falls only if the count fails to FACTOR. So lockstep is
the load-bearing measurement here and readmission is its candidate mechanism.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE DOOR LAW AND THE IDEAL MINIMUM are lemmas A and B exactly: at every
    scanned state, no effective divisor of degree below the engine's cost
    raises lambda, and the min-degree raisers are exactly the engine's tie
    set -- single-place powers in the ideal world.
    KILL: one scanned state where a cheaper raiser exists, or where the
    min-degree raisers differ from the menu's ties.
PR2 THE IDEAL WORLD SPRAWLS AT EVERY h: no trajectory's tail is one repeated
    vehicle, and the cost sequence is unbounded.
    KILL: a trajectory whose last LOCK_R moves are the same vehicle.
PR3 EVERY ELEMENT MOVE IS A CORE PLUS AT MOST ONE DEGREE-1 PLACE, of degree
    at most the ideal minimum at that state plus one (lemma D).
    KILL: one element move carrying a passenger of degree >= 2, or exceeding
    the ideal minimum by 2 or more.
PR4 IDEAL PERMANENCE HOLDS AT EVERY VISITED STATE (lemma C): an unseated
    place's door cost strictly exceeds the door cost of every seated place of
    the same degree.
    KILL: one visited state where it does not.
PR5 THE ELEMENT WORLD READMITS -- frozen as an OBSERVABLE, not an inference.
    What the rig PRINTS: per opening, whether a place carried only by a
    DECLINED member is seated later in the same branch within the horizon.
    The prediction is that readmission occurs at h >= 3, where two or more
    rational points share a degree and therefore tie, and the rider is one of
    them; and not at h = 2, which has a single rational point, hence no
    degree-1 tie and one possible rider forever.
    KILL: readmission printed at h = 2, or none printed at h = 5.
PR6a IDEAL LOCKSTEP HOLDS. lambda reads (degree, depth) only and the
    degree-multiset of the state is branch-independent, so all branches from
    a seed carry one signature sequence.
    KILL: two ideal branches from one seed with differing signatures.
PR6b ELEMENT LOCKSTEP is an OPEN OBSERVABLE, no kill, and it is the
    load-bearing measurement here. The mechanism to watch, named at the
    freeze: the rider is fixed by CLASS, same-degree places carry DIFFERENT
    classes, so a rider can land on a place that is seated in one branch and
    unseated in another -- different (degree, depth) multisets, different
    lambda, divergent doors from there on. The rig prints how many seeds'
    element branches disagree and at which move index the first disagreement
    falls.
PR7 THE IMAGE, printed and not predicted: distinct states at the horizon per
    seed per world, and the count of openings whose declined members are
    never readmitted within the horizon. A horizon count of survivors is an
    UPPER bound on survival and is reported as such.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE FOURTH CELL IS CHEAP, AND ITS LADDER IS COMPLETE (rule in range; five
   rings x two worlds x 14 moves, seeds the void plus every effective divisor
   to degree 3). Over F_2 the Hasse interval is #E(F_2) in {1..5}, so one
   curve per value gives the WHOLE class-group ladder in equal
   characteristic, with F_2[x] -- the coordinate ring of the affine line --
   sitting at h = 1 as the control. The door law is F_2[x]'s verbatim (lemma
   A, whose closed form is matched against the SEARCHED door at 48188 place-
   states and whose menu is brute-scanned at every state within the cap):
   this engine, told only
   that polynomials are the places of a genus-0 ring, reproduces the filed
   F_2[x] void trajectory move for move, encodings 4, 2, 4, 7, 11, 16, 19,
   37, 67, 131, 256 at degrees 2, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8
   (explore_function_field_lock.py finding 5). So exactly two dials move
   across the ladder: the POPULATION per degree, which genus-1 geometry
   makes lumpy -- the h = 5 curve has FOUR rational points and no place at
   all of degree 2 or 3, the h = 2 curve has one rational point and a dense
   ladder -- and the PRINCIPALITY constraint, which is the class group.

F2 THE EQUAL-CHARACTERISTIC 1-UNIT LAW AT F_4, F_8 AND F_16 (theorem A
   instantiated; 18 (residue field, depth) pairs, exact). lam_P(a) =
   lcm(q^d - 1, 2^ceil(log2 a)) by direct exponent computation in
   F_{2^d}[t]/(t^a). The source file ran F_2, F_3 and F_9; these are the
   residue fields an elliptic curve over F_2 actually has, and the law is
   f-independent across them as stated.

F3 THE SPRAWL SURVIVES BUNDLES (rule in range; 226 trajectories x 14 moves
   -- 113 seeds over five rings, in both worlds -- plus lemma E). No
   trajectory locks in
   either world: the last 6 moves are 6 DISTINCT vehicles at every seed of
   every ring, and costs climb to degree 12-14 within 14 moves. Theorem
   B(ii)'s cost divergence was derived for single-place moves; the extension
   is lemma E, and its load-bearing step is that a bounded-cost tail freezes
   the SUPPORT, after which the only tick source is a depth crossing a
   p-power frontier -- logarithmically many, against the one tick per move a
   trajectory needs. A bundled world sprawls exactly as a single-place one
   does.

F4 THE FREE RIDER IS ALWAYS A RATIONAL POINT (rule, proved as lemma D;
   asserted at 1762 element moves). Every nonzero ideal class of an elliptic
   curve's coordinate ring contains a place of degree 1 -- the point itself
   -- so the minimal completion of a core P^r has degree exactly
   [r*sigma(P) != O], 0 or 1. The element move is therefore the ideal core
   plus AT MOST ONE rational point, never more, and the rider is not chosen
   but SUMMONED: it is the rational point -r*sigma(P). On an elliptic curve
   the bundle is minimal, which is what makes the next two findings possible
   to state exactly.

F5 READMISSION IS REAL, AND IT NEEDS h >= 3 (rule in range; the headline
   mechanism). A declined place is STARVED when the move leaves its degree
   seated, which is the only kind of decline lemma C dominates and so the
   only kind that could have been permanent. In the IDEAL world 0 starved
   declines came back at any ring (0 of 5930, 5459, 15240, 19851, 42919) --
   lemma C holds at the level of the IMAGE and not only of the door. In the
   ELEMENT world: 0 at h = 1 and h = 2, then 3 of 5895 at h = 3, 6 of 5445
   at h = 4, 5 of 8459 at h = 5. The mechanism is the one the freeze named:
   two or more rational points share a degree and therefore TIE, the greedy
   declines one, and a later core's class summons it back as the rider.
   Specimen: the h = 5 void declines a rational point at move 1 and takes it
   back at move 2, inside the vehicle P1.2*P1.3, a rational core with a
   rational rider. h = 2 has a single rational point, so no degree-1 tie
   exists and the one possible rider is already seated; F6 turns that
   reading into a proof.
   HOW THIS WAS SCORED, since it decides the verdict. PR5's observable as
   FROZEN counts any declined place that returns, and under that wording
   h = 2 returns 48 times and the prediction is KILLED. What splits starved
   from free is F8, and the split was forced by the h = 1 CONTROL rather
   than by the ring whose verdict it changes: F_2[x] has no bundle at all
   and its ideal world still showed 45 returns, which is impossible in the
   sense the formula means, so the observable was measuring two different
   things before any ring was judged by it. PR5 is scored against the
   refined reading, and it is worth less than a prediction that never
   needed rescuing.

F6 BUT THE MECHANISM IS CAPACITY-BOUNDED, AND THAT IS THE GAP'S ANSWER
   (rule, proved, with 14 of 14 readmissions confirming and no trajectory
   losing more distinct places than it has rational points). Two steps, and
   the first alone would not do it.
   READMISSION IS CONFINED TO DEGREE 1. A starved place P of degree d sits
   under every seated same-degree neighbour's door: its own costs
   d*(2^c + 1) against the seated one's d*(2^c + 1 - e), and pricing both
   completions moves that by at most 1, so P can be a minimal CORE only
   when d*e <= 1 -- only at d = e = 1. For d >= 2 it is never a core, and
   never a passenger either, lemma D making every non-core passenger a
   place of degree 1. So the only places a readmission can ever seat are
   the h - 1 rational points, whatever the ring and whatever the horizon --
   which also forces F5's zero at h = 2, one rational point having no
   second degree-1 place to starve it.
   AND A FINITE SET OF VICTIMS IS NOT A FINITE NUMBER OF FAILED OPENINGS,
   since one place declined at endlessly many openings and seated once
   would break the bound while touching nothing else. What closes it is
   that DEPTHS NEVER FALL: a readmission IS a seating, each of the h - 1
   points is lost once, and the openings that fail are the ones preceding a
   finite seating time. The worst trajectory measured loses 2. And the
   bound does not need the seatings to FINISH -- every void with more than
   one point to seat leaves some unseated at the horizon (1 of 2, 2 of 3
   and 3 of 4 at h = 3, 4, 5), and a point never seated is never readmitted
   either, which is the same bound from the other side.
   So permanence fails at finitely many openings, infinitely many survive,
   and the fourth world sits AT THE CONTINUUM. The cell built to break the
   gap answers it instead: the source file's "no greedy image is countably
   infinite" survives its sharpest test, and survives it with a REASON
   rather than an absence of counterexample. The live route -- permanence
   broken by a bundle readmitting a declined choice, on independence's
   template -- is real here and has a BUDGET. Erasure was already excluded
   by construction, needing a recurrent vehicle where a recurrent vehicle
   is a lock and a lock stops the openings. Both halves of "surviving" now
   have a named reason they cannot fail endlessly, which is a stronger
   statement than the gap itself.

F7 AND THE COUNT STILL FACTORS (rule in range, and the range is the modest
   half of this file: 0 disagreeing seeds of 7, 6, 9, 12 and 15 with content,
   both worlds and every ring, but branching only at the first 2 within-type
   openings and running 9 moves from seeds of degree <= 2). Lockstep -- the
   multiplicity at a later opening must not depend on the choice made at an
   earlier one -- was the formula's one contingent assumption when this file
   ran, and PR6b named a concrete way for it to die here: the rider is fixed
   by CLASS, same-degree places carry different classes, so a rider could
   land on a place seated in one branch and unseated in another, splitting
   lambda. It did not fire in range. It cannot fire at all: lockstep is since
   PROVED, by the observation that everything the engine reads is a function
   of a place's (degree, class), so a permutation preserving that colouring
   is an automorphism of the dynamics and carries one tie member of a type to
   another while fixing the state (explore_greedy_image_g2.py). This file's
   census is therefore a control on a theorem rather than evidence for an
   assumption, and the fourth world still enters the table as a fourth
   CONFIRMATION rather than a fourth value. ONE READING HERE IS NARROWER
   THAN IT LOOKS, and the proof is
   what exposes it: the type that factors carries the STATE DEPTH, and the
   type used here does not. The two coincide for a bare door exponent, and
   the only way they can part is a core exponent ABOVE it -- which this
   file's menu offers as r0 + 1 and which this file never measured. At genus
   2 no such vehicle entered a tie set at all, so the question is open here
   too rather than answered. (CLOSED SINCE: an offset vehicle is never a NEW
   divisor -- minrep(-(r+j)c) + j*P represents the class the bare door must
   cancel, so the bare door is never dearer, explore_coarse_type.py -- and
   at genus 2 none entered a tie set, explore_greedy_image_g2.py.)
   AND WHAT A FAILURE WOULD HAVE TO LOOK LIKE, named at the freeze so the
   next ring can be aimed rather than watched: a countably infinite image
   needs the count NOT to factor, and the only shape that yields exactly
   aleph0 is endless openings where a deviation is readmitted so that all
   branches agree from some move on, while the limit still records WHICH
   opening the branch first deviated at -- one limit per index of first
   deviation, plus the canonical branch. That needs readmission to re-merge
   the branches AND a permanent finite record to keep the index visible,
   which is why readmission alone gives a point rather than aleph0 and why
   lockstep is the thing to instrument.

F8 A CORRECTION TO WHAT AN "OPENING" IS, and the corpus could not have seen
   it in the three rings already run (rule in range; 691 of 2810 tie states
   straddle two vehicle degrees). A tie set is not one kind of thing. It
   splits into engine TYPES -- lambda reads (degree, depth), and the element
   world reads one further datum, the class -- and a choice BETWEEN types is
   a different move, not a choice of member. Those declines are not starved,
   and they come back: in the IDEAL world, where lemma C forbids a STARVED
   decline's return and 0 of 89399 came back, free declines returned 45, 41,
   36, 77 and 70 times at h = 1..5, and 45, 48, 31, 62 and 70 times in the
   element world. So the formula's MULTIPLICITY must be
   read as the WITHIN-TYPE multiplicity; the raw tie count overcounts, and
   the surplus is the source file's independence corner case -- a
   reordering, not a
   choice -- appearing inside DYNAMICS rather than under a second law.
   SUPERSEDED IN PART: only the cross-DEGREE surplus is a reordering. Two
   cores of one degree in different CLASSES starve each other, so that part
   of the surplus is a CHOICE above the genus and the within-type
   multiplicity is a lower bound (explore_reordering.py). Z has
   no ties to split and the number rings tie only in Galois pairs of one
   norm, so the distinction was invisible until a ring tied across degrees.
   AND THE CLASS GROUP DIVIDES THE MULTIPLICITY, the second thing the raw
   count hides (observation, five rings). A principal world's within-type
   opening is only the same-degree places OF ONE CLASS, so it is about 1/h
   as wide as the ideal world's: the largest widths measured run 335, 340,
   630, 616, 1160 in the ideal world against 335, 168, 210, 154, 232 in the
   element world at h = 1..5. The division is NEAR-exact and not exact, and
   the difference matters. The class map's fibres over a degree are equal at
   every degree measured at h = 5 and at 10 of 13 at h = 3, but only 7 of 15
   at h = 2, where they spread by as much as 18. So 630/3, 616/4 and 1160/5
   landing exactly is that near-uniformity plus which degree the maximum
   happened to fall on, not an identity -- and h = 2's 168 against a naive
   340/2 = 170 is the same fact showing its working. What survives as the
   claim is the FACTOR: the class group is the one thing here that reaches
   the COUNT directly, where everything else it does reaches it through the
   rider.

F9 AND THE BUDGET IS NOT GENUS 1's -- IT IS RIEMANN-ROCH'S (a derivation
   from F4 and F6, no run behind it, and inheriting their design scope: cold
   D-DYN, the minimal-move policy class, the element world of a function
   field's affine coordinate ring). The obvious objection to F6 is that
   "every nonzero class contains a place of degree 1" is a genus-1 accident,
   so at higher genus the rider could have unbounded degree and the budget
   would be infinite. It cannot. For a smooth projective curve over a finite
   field with a rational point at infinity, the class group of the affine
   ring is FINITE, and for each class the minimal-degree effective affine
   representatives form a complete linear system minus a hyperplane
   condition -- a projective space over F_q, hence a FINITE set. The rider
   is always a minimal representative of the class the core needs cancelled,
   so the places a rider can ever carry lie in a fixed finite set: the union,
   over the finitely many classes, of the finitely many minimal
   representatives. Genus moves the SIZE of that set, from h - 1 places at
   genus 1 to something bounded by the class number times the size of a
   linear system, and never its finiteness. So the seated-once argument of
   F6 runs unchanged at every genus: permanence fails at finitely many
   openings, infinitely many survive, and the image is the continuum. THE
   PERMANENCE HALF OF THE GAP IS THEREFORE CLOSED FOR EVERY FUNCTION FIELD
   OVER A FINITE FIELD, not only for the curves run here -- which, with
   erasure already excluded by construction, left LOCKSTEP as the only
   contingent thing the formula rested on. The derivation is since paid at
   genus 2, where the rider does grow to degree 2 and the bound survives it
   unchanged, and lockstep is since proved (F7).

THE DESIGN, in six sections after the control.

 S1 THE POSITIVE CONTROL, run before any image is read.
    (a) The equal-characteristic 1-unit law brute-verified at the residue
        fields this ring actually has -- F_2, F_4, F_8, F_16 -- by direct
        exponent computation in F_{2^d}[t]/(t^a), closing a gap the source
        file left (it ran F_2, F_3, F_9).
    (b) The curve arithmetic: point counts over F_{2^d} from direct
        enumeration against the zeta-function prediction, and the
        closed-point counts against the Moebius formula.
    (c) The class map: sigma(P) lands in E(F_2) at every place, and the
        affine degree-1 places carry exactly the nonzero classes, bijectively.
    (d) THE h = 1 CONTROL, in two halves: the same engine run on F_2[x] --
        places the monic irreducibles, class group trivial, tie-break by the
        encoding order -- must reproduce explore_function_field_lock.py's
        void trajectory move for move; and at S6, since h = 1 makes every
        divisor principal, the ELEMENT engine must degenerate to the ideal
        one row for row, or the h > 1 differences are partly the code path.
    (e) The door brute: at every state whose cost is within the scan cap, a
        full enumeration of effective divisors, both worlds (PR1).
    If the control fails nothing below is read.
 S2 THE GEOGRAPHY of the five rings: places by degree, places by class, and
    where the degree-1 population sits -- the mechanism variable is the
    number of affine rational points, which is h - 1.
 S3 THE IDEAL WORLD: cold D-DYN from a seed battery, per ring. The sprawl
    (PR2), the door law and permanence at every state (PR1, PR4), and the tie
    census -- multiplicity, and which degrees a tie straddles.
 S4 THE ELEMENT WORLD: the same battery. The free-rider structure asserted
    at every move (PR3), the sprawl again, and the READMISSION census (PR5).
 S5 LOCKSTEP: branching at the first SPLITS openings and running
    canonically thereafter, both worlds, comparing signature sequences
    (PR6a, PR6b). The branching is WITHIN A TYPE only -- choosing between
    two types is a different move, not a choice of member, so its sequences
    differ by construction and that is S3/S4's reordering rather than a
    lockstep failure. The coverage is bounded BY DESIGN and not by a cap the
    run might hit, so there is nothing to truncate; what the bound costs is
    stated as the finding's scope instead, since a narrow enumeration that
    finds nothing is weak evidence and must read as such.
 S6 THE FOUR-WORLD TABLE: what the fourth cell does to the formula and to
    the gap.

Run: `python explore_greedy_image_ec.py`. RUN RECORD (132825 checks, ~58 s).
S1 control: the 1-unit law exact at 18 (residue field, depth) pairs over F_2,
F_4, F_8 and F_16, and lam_pp met the exponent of 9 FULL unit groups computed
element by element, which is the check that does not restate the law's own
shape; 128 point and closed-point counts exact against the zeta function and
Moebius, degrees 1..16 over four curves; the class map lands in E(F_2) at
every place of every ring, with h - 1 rational affine places, one per nonzero
class; the F_2[x] void reproduced move for move, and its element and ideal
rows identical at S6, so the element code path degenerates as h = 1 requires;
360 states brute-scanned against a full divisor enumeration, 0 above the
degree-9 cap. S2 geography: places of degree 1..8 read [2,1,2,3,6,9,18,30] at
h = 1, [1,3,4,2,4,6,20,34] at h = 2, [2,3,2,0,6,11,18,27] at h = 3,
[3,2,0,2,8,8,16,34] at h = 4 and [4,0,0,5,4,10,20,25] at h = 5; the class
fibres over a degree are equal at 16/16, 7/15, 10/13, 7/12 and 12/12 of the
live degrees, with spreads 0, 18, 2, 9 and 0. S3 ideal world, 14 moves from
15/14/21/28/35 seeds: no lock anywhere (the last 6 moves are 6 distinct
vehicles at every seed), cost max 12/12/13/13/14, 178/173/237/350/420 tie
states, and 0 starved declines readmitted out of 5930/5459/15240/19851/42919.
S4 element world, same battery: 1762 moves rider-checked with no violation,
and starved readmissions 0, 0, 3, 6, 5 at h = 1..5 -- all 14 of them places
of degree 1, every one of them that place's own seating, and no trajectory
losing more than 2 openings; the element voids seat 1 of 1, 1 of 2, 2 of 3
and 3 of 4 rational points by the horizon at h = 2..5. S5 lockstep: 0
disagreeing seeds of 7/6/9/12/15 with content, both worlds and every ring,
branching at the first 2 within-type openings over 9 moves. Audit: 3524
states visited, 2861 brute-scanned, 2810 tie states with multiplicities from
2 to 1160, 691 of them straddling two degrees, largest within-type widths
335/340/630/616/1160 in the ideal world against 335/168/210/154/232 in the
element world, 48188 door exponents found by SEARCH and matched against
lemma A's closed form, 13705 permanence checks. Slate PR1-PR7: all hit, no
misses -- with PR5 scored against the starved/free split of F8 and not
against its own frozen wording, which the h = 1 control refuted before any
ring's verdict was read; PR6b was frozen as an open observable and printed
lockstep HOLDING, which is what leaves the formula intact. Unfrozen finds:
the type/reordering split inside a tie set and the class group's division of
the multiplicity (F8), the degree-1 confinement of readmission and the
seated-once step that turns it into a bound (F6), and the Riemann-Roch
generalisation that carries the bound to every genus (F9).
"""

import sys

CHECKS = 0

DMAX = 16          # greatest place degree the universes carry
T_RUN = 14         # moves per deterministic trajectory
T_LS = 9           # moves per branch in the lockstep enumeration
SPLITS = 2         # openings the lockstep enumeration branches at
LOCK_R = 6         # repeated vehicles that would witness a lock
SCAN_DEG = 9       # greatest vehicle degree the brute scan enumerates
SEED_DEG = 3       # seeds are the void + every effective divisor to this degree


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


def ceil_log2(a):
    return (a - 1).bit_length()          # a >= 1


def v2(n):
    return (n & -n).bit_length() - 1


def mobius(n):
    r, p, m = 1, 2, n
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            r = -r
        p += 1
    if m > 1:
        r = -r
    return r


# --------------------------------------------------------------- GF(2^d)
def pdeg(a):
    return a.bit_length() - 1


def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pmod(a, b):
    db = pdeg(b)
    while a and pdeg(a) >= db:
        a ^= b << (pdeg(a) - db)
    return a


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


def is_irr(f):
    """Rabin irreducibility on the int encoding of a polynomial over F_2."""
    d = pdeg(f)
    if d < 1:
        return False
    if d == 1:
        return True
    if f & 1 == 0 or bin(f).count("1") % 2 == 0:
        return False
    t = 2
    for _ in range(d):
        t = pmod(pmul(t, t), f)
    if t != 2:
        return False
    m, ps = d, []
    p = 2
    while p * p <= m:
        if m % p == 0:
            ps.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        ps.append(m)
    for q in ps:
        t = 2
        for _ in range(d // q):
            t = pmod(pmul(t, t), f)
        if pgcd(t ^ 2, f) != 1:
            return False
    return True


def irr_of_degree(d):
    return [f for f in range(1 << d, 2 << d) if is_irr(f)]


class GF(object):
    """F_{2^d} on int encodings, with the additive solver for z^2 + z = w."""

    def __init__(self, d):
        self.d = d
        self.n = 1 << d
        # F_2 is F_2[x]/(x); above degree 1 the least irreducible will do
        self.m = 2 if d == 1 else irr_of_degree(d)[0]
        self.piv = {}
        for i in range(d):
            v, comb = self.sq(1 << i) ^ (1 << i), 1 << i
            while v:
                b = v.bit_length() - 1
                if b in self.piv:
                    pv, pc = self.piv[b]
                    v ^= pv
                    comb ^= pc
                else:
                    self.piv[b] = (v, comb)
                    break

    def mul(self, a, b):
        if a <= 1 or b <= 1:
            return a * b
        return pmod(pmul(a, b), self.m)

    def sq(self, a):
        return self.mul(a, a)

    def inv(self, a):
        r, b, e = 1, a, self.n - 2
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def sqrt(self, a):
        for _ in range(self.d - 1):
            a = self.mul(a, a)
        return a

    def solve_quad(self, w):
        """z with z^2 + z = w, or None. The other root is z ^ 1."""
        v, comb = w, 0
        while v:
            b = v.bit_length() - 1
            if b not in self.piv:
                return None
            pv, pc = self.piv[b]
            v ^= pv
            comb ^= pc
        return comb


# ------------------------------------------------- the curve and its points
class Curve(object):
    """y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6 over F_2."""

    def __init__(self, a1, a2, a3, a4, a6):
        self.a = (a1, a2, a3, a4, a6)

    def rhs(self, F, x):
        a1, a2, a3, a4, a6 = self.a
        x2 = F.sq(x)
        return F.mul(x2, x) ^ (x2 if a2 else 0) ^ (x if a4 else 0) ^ a6

    def on(self, F, x, y):
        a1, a2, a3, a4, a6 = self.a
        return (F.sq(y) ^ (F.mul(x, y) if a1 else 0) ^ (y if a3 else 0)
                == self.rhs(F, x))

    def add(self, F, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        a1, a2, a3, a4, a6 = self.a
        x1, y1 = P
        x2, y2 = Q
        negy1 = y1 ^ (F.mul(a1, x1) if a1 else 0) ^ a3
        if x1 == x2 and y2 == negy1:
            return None
        if x1 != x2:
            lam = F.mul(y1 ^ y2, F.inv(x1 ^ x2))
        else:
            num = F.sq(x1) ^ (a4 if a4 else 0) ^ ((y1) if a1 else 0)
            den = (x1 if a1 else 0) ^ a3
            lam = F.mul(num, F.inv(den))
        x3 = F.sq(lam) ^ (lam if a1 else 0) ^ a2 ^ x1 ^ x2
        y3 = F.mul(lam, x1 ^ x3) ^ y1 ^ (x3 if a1 else 0) ^ a3
        return (x3, y3)

    def points(self, F):
        """Affine points over F, by solving the quadratic in y at each x."""
        a1, a2, a3, a4, a6 = self.a
        out = []
        for x in range(F.n):
            f = self.rhs(F, x)
            u = (x if a1 else 0) ^ a3
            if u == 0:
                out.append((x, F.sqrt(f)))
                continue
            u2 = F.sq(u)
            z = F.solve_quad(F.mul(f, F.inv(u2)))
            if z is None:
                continue
            out.append((x, F.mul(u, z)))
            out.append((x, F.mul(u, z ^ 1)))
        return out


# ------------------------------------------------------------------ rings
class Ring(object):
    """One ring, reduced to the interface the searches use.

    A PLACE is a hashable key; deg[pl] is its degree and cls[pl] its ideal
    class as an index into the class list, 0 being the identity. A VEHICLE is
    a dict {place: exponent}; a STATE is the same. Costs are DEGREES.
    """

    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.deg = {}
        self.cls = {}
        self.by_deg = {}
        self.rider = {}      # class -> the degree-1 place carrying it
        self.addc = None     # class addition table
        self.negc = None     # class negation table
        self.enc = None      # genus-0 only: the encoding, for the tie-break

    def add_class(self, c1, c2):
        return self.addc[c1][c2]

    def neg_class(self, c):
        return self.negc[c]

    def veh_class(self, veh):
        c = 0
        for pl, e in veh.items():
            for _ in range(e % self.h if self.h > 1 else 0):
                c = self.add_class(c, self.cls[pl])
        return c

    def veh_deg(self, veh):
        return sum(self.deg[pl] * e for pl, e in veh.items())

    def veh_key(self, veh):
        """The canonical tie-break order. Genus 0 uses the polynomial
        encoding, the canonical transfer of F_2[x]'s 'least monic m'; the
        curves have no encoding and use (degree, place key)."""
        if self.enc is not None:
            m = 1
            for pl, e in veh.items():
                for _ in range(e):
                    m = pmul(m, self.enc[pl])
            return (self.veh_deg(veh), m)
        return (self.veh_deg(veh),
                tuple(sorted((self.deg[pl], pl, e) for pl, e in veh.items())))

    # ------------------------------------------------------- the pump
    def lam_pp(self, d, a):
        if a == 0:
            return 1
        return lcm((1 << d) - 1, 1 << ceil_log2(a))

    def lam_state(self, st):
        L = 1
        for pl, e in st.items():
            if e:
                L = lcm(L, self.lam_pp(self.deg[pl], e))
        return L

    def door_r(self, pl, e, L):
        d = self.deg[pl]
        r = 1
        while L % self.lam_pp(d, e + r) == 0:
            r += 1
            assert r < 4096, "door search runaway"
        return r

    def kind(self, e, r):
        if e >= 1:
            return "deepen"
        return "fresh" if r == 1 else "clocked"


def build_curve_ring(name, curve, h, dmax):
    R = Ring(name, h)
    F1 = GF(1)
    rat = [None] + curve.points(F1)
    ok(len(rat) == h, "%s: #E(F_2) = %d, expected %d" % (name, len(rat), h))
    idx = dict((P, i) for i, P in enumerate(rat))
    R.classes = rat
    R.addc = [[idx[curve.add(F1, rat[i], rat[j])] for j in range(h)]
              for i in range(h)]
    ok(R.addc[0] == list(range(h)), "%s: class 0 is not the identity" % name)
    R.negc = [next(j for j in range(h) if R.addc[i][j] == 0) for i in range(h)]
    for d in range(1, dmax + 1):
        F = GF(d)
        pts = curve.points(F)
        seen, out = set(), []
        for P in pts:
            if P in seen:
                continue
            orb, Q = [P], (F.sq(P[0]), F.sq(P[1]))
            while Q != P:
                orb.append(Q)
                Q = (F.sq(Q[0]), F.sq(Q[1]))
            for Rp in orb:
                seen.add(Rp)
            if len(orb) != d:
                continue
            s = None
            for Rp in orb:
                s = curve.add(F, s, Rp)
            ok(s is None or (s[0] <= 1 and s[1] <= 1),
               "%s: an orbit sum left the prime field at degree %d" % (name, d))
            pl = (d, min(orb))
            R.deg[pl] = d
            R.cls[pl] = idx[s]
            out.append(pl)
        out.sort()
        R.by_deg[d] = out
    for pl in R.by_deg[1]:
        R.rider[R.cls[pl]] = pl
    return R


def build_poly_ring(dmax):
    """F_2[x]: the h = 1 control. Places are the monic irreducibles."""
    R = Ring("F_2[x]", 1)
    R.classes = [None]
    R.addc = [[0]]
    R.negc = [0]
    R.enc = {}
    for d in range(1, dmax + 1):
        out = []
        for f in irr_of_degree(d):
            pl = (d, f)
            R.deg[pl] = d
            R.cls[pl] = 0
            R.enc[pl] = f
            out.append(pl)
        R.by_deg[d] = out
    return R


# ------------------------------------------------------------- the menus
def doors_at(R, st, L, d):
    """(r for an unseated place of degree d, [(place, r)] for the seated
    ones). lam reads (degree, depth) only, so every unseated place of a
    degree shares one door and it is computed once."""
    r0 = R.door_r(R.by_deg[d][0], 0, L) if R.by_deg[d] else None
    seated = [(pl, R.door_r(pl, st[pl], L)) for pl in st
              if st[pl] and R.deg[pl] == d]
    return r0, seated


def ideal_menu(R, st, L):
    """(degree, [vehicle]) -- the minimal-degree ticking effective divisors,
    which lemma B says are single-place powers."""
    best, ties = None, []
    nseat = {}
    for pl, e in st.items():
        if e:
            nseat[R.deg[pl]] = nseat.get(R.deg[pl], 0) + 1
    for d in range(1, DMAX + 1):
        if best is not None and d > best:
            break
        pls = R.by_deg[d]
        if not pls:
            continue
        cands = []
        if len(pls) > nseat.get(d, 0):
            r0 = R.door_r(pls[0], 0, L)
            cands.append((d * r0, r0, None))
        for pl in st:
            if st[pl] and R.deg[pl] == d:
                r = R.door_r(pl, st[pl], L)
                cands.append((d * r, r, pl))
        for cost, r, only in cands:
            if best is not None and cost > best:
                continue
            group = [{pl: r} for pl in pls if st.get(pl, 0) == 0] \
                if only is None else [{only: r}]
            if best is None or cost < best:
                best, ties = cost, list(group)
            else:
                ties.extend(group)
    ok(best is not None and best <= DMAX,
       "%s: the ideal door reached degree %s, past the universe" % (R.name, best))
    ties.sort(key=R.veh_key)
    return best, ties


def elem_menu(R, st, L):
    """(degree, [vehicle]) in the PRINCIPAL world. Lemma D: every minimal
    vehicle is a core P^r plus the single rational point its class needs, so
    the construction below is complete."""
    best, ties, seen = None, [], set()

    def offer(veh):
        nonlocal best, ties, seen
        cost = R.veh_deg(veh)
        if best is not None and cost > best:
            return
        key = tuple(sorted(veh.items()))
        if best is None or cost < best:
            best, ties, seen = cost, [veh], {key}
        elif key not in seen:
            seen.add(key)
            ties.append(veh)

    def complete(pl, r):
        veh = {pl: r}
        c = R.veh_class(veh)
        if c:
            # the rider must CANCEL the core's class, so it is the rational
            # point -r*sigma(P) (lemma D)
            q = R.rider[R.neg_class(c)]
            veh = dict(veh)
            veh[q] = veh.get(q, 0) + 1
        return veh

    for d in range(1, DMAX + 1):
        if best is not None and d > best:
            break
        pls = R.by_deg[d]
        if not pls:
            continue
        groups = {}
        for pl in pls:
            if st.get(pl, 0) == 0:
                groups.setdefault(R.cls[pl], []).append(pl)
        entries = []
        if groups:
            r0 = R.door_r(pls[0], 0, L)
            for c in groups:
                entries.append((groups[c], r0))
                entries.append((groups[c], r0 + 1))
        for pl in st:
            if st[pl] and R.deg[pl] == d:
                r0 = R.door_r(pl, st[pl], L)
                entries.append(([pl], r0))
                entries.append(([pl], r0 + 1))
        for group, r in entries:
            # cost is uniform inside a (degree, class) group, so it is priced
            # once and the group materialised only while it is competitive
            if best is not None and R.veh_deg(complete(group[0], r)) > best:
                continue
            for pl in group:
                offer(complete(pl, r))
    # DMAX and not DMAX + 1: at cost DMAX + 1 a place of degree DMAX + 1
    # could tie and the universe would not carry it, so that is a failure
    # rather than a bound to lean on.
    ok(best is not None and best <= DMAX,
       "%s: the element door reached degree %s, past the universe"
       % (R.name, best))
    for veh in ties:
        ok(R.veh_class(veh) == 0, "%s: a non-principal element vehicle" % R.name)
    ties.sort(key=R.veh_key)
    return best, ties


MENUS = {"ideal": ideal_menu, "element": elem_menu}
R_OF = {}                      # ring name -> ring, for the specimen prints


def fmt_state(R, st):
    parts = ["P%d.%d^%d" % (R.deg[pl], R.by_deg[R.deg[pl]].index(pl), e)
             for pl, e in sorted(st.items(), key=lambda kv: R.deg[kv[0]]) if e]
    return "*".join(parts) if parts else "(1)"


# ------------------------------------------------------- the brute scan
_DIVS = {}


def all_divisors(R, maxdeg):
    """Every effective divisor of degree 1..maxdeg, as a list of dicts."""
    key = (R.name, maxdeg)
    if key in _DIVS:
        return _DIVS[key]
    pls = [pl for d in range(1, maxdeg + 1) for pl in R.by_deg[d]]
    out = []

    def rec(i, cur, dg):
        if cur:
            out.append(dict(cur))
        for j in range(i, len(pls)):
            pl = pls[j]
            dd = R.deg[pl]
            if dg + dd > maxdeg:
                continue
            e, g = 1, dg + dd
            while g <= maxdeg:
                cur[pl] = e
                rec(j + 1, cur, g)
                e += 1
                g += dd
            del cur[pl]

    rec(0, {}, 0)
    out.sort(key=lambda v: R.veh_deg(v))
    _DIVS[key] = out
    return out


def scan_check(R, world, st, L, cost, ties):
    """PR1 at one state: nothing cheaper ticks, and the min-degree tickers are
    exactly the menu's ties."""
    at_cost = []
    for veh in all_divisors(R, cost):
        dg = R.veh_deg(veh)
        if world == "element" and R.veh_class(veh) != 0:
            continue
        L2 = L
        for pl, e in veh.items():
            L2 = lcm(L2, R.lam_pp(R.deg[pl], st.get(pl, 0) + e))
        if L2 <= L:
            continue
        ok(dg >= cost, "%s/%s: a degree-%d divisor ticks below the door %d"
           % (R.name, world, dg, cost))
        if dg == cost:
            at_cost.append(veh)
    got = sorted(tuple(sorted(v.items())) for v in at_cost)
    want = sorted(tuple(sorted(v.items())) for v in ties)
    ok(got == want, "%s/%s: scan ties != menu ties at cost %d (%d vs %d)"
       % (R.name, world, cost, len(got), len(want)))
    if world == "ideal":
        for veh in at_cost:
            ok(len(veh) == 1,
               "%s: a minimal ideal move is not a single-place power" % R.name)


# ----------------------------------------------------------- trajectories
def apply_veh(st, veh):
    out = dict(st)
    for pl, e in veh.items():
        out[pl] = out.get(pl, 0) + e
    return out


def vkey(veh):
    return tuple(sorted(veh.items()))


def sig_of(R, st, veh, cost):
    """The move's signature: what lockstep says is branch-independent --
    cost, kind, and the (degree, exponent) multiset of the vehicle."""
    core = max(veh, key=lambda pl: R.deg[pl] * veh[pl])
    k = R.kind(st.get(core, 0), veh[core])
    return (cost, k, tuple(sorted((R.deg[pl], e) for pl, e in veh.items())))


class Audit(object):
    def __init__(self):
        self.states = 0
        self.scanned = 0
        self.scan_skipped = 0
        self.tie_states = 0
        self.tie_sizes = {}
        self.tie_multideg = 0     # tie sets straddling two vehicle degrees
        self.starve = 0
        self.starve_bad = []
        self.doors = 0
        self.door_bad = []
        self.riders = 0
        self.rider_bad = []

    def at_state(self, R, world, st, L, cost, ties):
        self.states += 1
        if cost <= SCAN_DEG:
            scan_check(R, world, st, L, cost, ties)
            self.scanned += 1
        else:
            self.scan_skipped += 1
        if len(ties) > 1:
            self.tie_states += 1
            self.tie_sizes[len(ties)] = self.tie_sizes.get(len(ties), 0) + 1
            degs = set()
            for veh in ties:
                for pl in veh:
                    degs.add(R.deg[pl])
            if len(degs) > 1:
                self.tie_multideg += 1
        # PR1, lemma A: the door exponent found by SEARCH must equal the
        # closed form. The searching door_r is what the menus use, so the
        # closed form is otherwise prose with no verifier behind it.
        c = v2(L)
        for d in range(1, min(DMAX, 8) + 1):
            for pl in R.by_deg[d][:2]:
                e = st.get(pl, 0)
                got = R.door_r(pl, e, L)
                if e >= 1:
                    want = 2 ** c + 1 - e
                elif (L >> c) % ((1 << d) - 1) != 0:
                    want = 1
                else:
                    want = 2 ** c + 1
                self.doors += 1
                if got != want:
                    self.door_bad.append((R.name, d, e, c, got, want))
        # PR4, lemma C: an unseated place's door strictly exceeds every
        # seated same-degree place's door.
        for d in range(1, DMAX + 1):
            seated = [pl for pl in R.by_deg[d] if st.get(pl, 0) > 0]
            if not seated:
                continue
            unse = [pl for pl in R.by_deg[d] if st.get(pl, 0) == 0]
            if not unse:
                continue
            worst = max(R.door_r(pl, st[pl], L) for pl in seated)
            fresh = R.door_r(unse[0], 0, L)
            self.starve += 1
            if not fresh > worst:
                self.starve_bad.append((R.name, world, d, worst, fresh))

    def rider_check(self, R, st, veh, ideal_cost):
        """PR3 / lemma D: a core plus at most one degree-1 passenger."""
        self.riders += 1
        cost = R.veh_deg(veh)
        if cost > ideal_cost + 1:
            self.rider_bad.append((R.name, "cost", cost, ideal_cost))
            return
        core = max(veh, key=lambda pl: R.deg[pl] * veh[pl])
        for pl, e in veh.items():
            if pl is core:
                continue
            if R.deg[pl] != 1 or e != 1:
                self.rider_bad.append((R.name, "passenger", R.deg[pl], e))


def run(R, world, seed, T, audit=None):
    """One trajectory under the canonical tie-break. Returns the move log."""
    menu = MENUS[world]
    st, L = dict(seed), R.lam_state(seed)
    log = []
    for _ in range(T):
        cost, ties = menu(R, st, L)
        if audit is not None:
            audit.at_state(R, world, st, L, cost, ties)
        veh = ties[0]
        if audit is not None and world == "element":
            icost, _ = ideal_menu(R, st, L)
            audit.rider_check(R, st, veh, icost)
        st2 = apply_veh(st, veh)
        # A DECLINED place is one an unchosen tie member would have seated.
        # It is STARVED when the move leaves some place of its own degree
        # seated -- lemma C then dominates it forever in the ideal world.
        # Otherwise it is FREE, and the tie was a REORDERING, not a choice.
        seated_degs = set(R.deg[pl] for pl, e in st2.items() if e)
        declined = {}
        for other in ties:
            if vkey(other) == vkey(veh):
                continue
            for pl in other:
                if pl not in veh and st.get(pl, 0) == 0:
                    declined[pl] = ("starved" if R.deg[pl] in seated_degs
                                    else "free")
        # The RAW multiplicity and the largest WITHIN-TYPE one. Only the
        # second can survive an opening; the gap between them is the
        # reordering the raw count mistakes for a choice.
        bytype = {}
        for other in ties:
            bytype.setdefault(veh_type(R, world, other), []).append(other)
        log.append({"cost": cost, "veh": veh, "nties": len(ties),
                    "ntypes": len(bytype),
                    "maxtype": max(len(g) for g in bytype.values()),
                    "sig": sig_of(R, st, veh, cost), "declined": declined,
                    "state": st})
        st = st2
        L2 = R.lam_state(st)
        ok(L2 > L, "%s/%s: the chosen move does not raise lambda" % (R.name, world))
        L = L2
    return log


def readmission(R, log):
    """Per DECLINED PLACE, split by whether the move starved it: is it seated
    later in the same branch? Returns counts (starved, starved_back, free,
    free_back, first_starved_readmission)."""
    ns, nsb, nf, nfb, first, degs, when = 0, 0, 0, 0, None, {}, []
    for i, mv in enumerate(log):
        for pl, tag in mv["declined"].items():
            back = next((j for j, later in enumerate(log[i + 1:])
                         if pl in later["veh"]), None)
            if tag == "starved":
                ns += 1
                if back is not None:
                    nsb += 1
                    d = R.deg[pl]
                    degs[d] = degs.get(d, 0) + 1
                    when.append((i, i + back + 1, pl))
                    if first is None:
                        first = (i, d, i + back + 1, dict(log[i + back + 1]
                                                          ["veh"]))
            else:
                nf += 1
                nfb += (back is not None)
    return ns, nsb, nf, nfb, first, degs, when


def seating_moves(R, log, places):
    """For each named place, the move that first seats it, or None. Depths
    never fall, so a place is seated at most ONCE -- this is the step that
    turns a finite set of possible victims into a finite number of failed
    openings. It is NOT that the seatings finish: a rational point can stay
    unseated forever (the h = 5 void leaves one of its four), and such a
    point is never readmitted either, because readmission IS the seating."""
    out = {}
    for pl in places:
        for i, mv in enumerate(log):
            if mv["state"].get(pl, 0) == 0 and pl in mv["veh"]:
                out[pl] = i
                break
        else:
            out[pl] = None
    return out


def seeds_of(R, maxdeg):
    return [{}] + [dict(v) for v in all_divisors(R, maxdeg)]


# ------------------------------------------------------------- S1 control
def s1a_unit_law():
    print("  (a) the equal-characteristic 1-unit law at the residue fields")
    print("      THIS ring has -- F_2, F_4, F_8, F_16 (the source file ran")
    print("      F_2, F_3, F_9), by direct exponent in F_{2^d}[t]/(t^a):")
    caps = {1: 6, 2: 5, 3: 4, 4: 3}
    n = 0
    for d, amax in sorted(caps.items()):
        F = GF(d)
        for a in range(1, amax + 1):
            # U_1 = 1 + t*F_q[t]/(t^a); brute its exponent.
            expo = 1
            for code in range(F.n ** (a - 1)):
                c, u = code, [0] * a
                u[0] = 1
                for j in range(1, a):
                    u[j] = c % F.n
                    c //= F.n
                # order of u by repeated squaring: char 2, so it is a 2-power
                k, w = 0, u
                while w != [1] + [0] * (a - 1):
                    w = polysq(F, w, a)
                    k += 1
                    assert k < 32, "1-unit order runaway"
                expo = lcm(expo, 1 << k)
            want = 1 << ceil_log2(a)
            ok(expo == want, "1-unit exponent at q=%d a=%d: %d != %d"
               % (F.n, a, expo, want))
            n += 1
    # lcm(q - 1, exp U_1) is the law's SHAPE, so checking lam_pp against it
    # would restate the line above. The contact check is the exponent of the
    # WHOLE unit group of F_q[t]/(t^a), computed without the law.
    m = 0
    for d, amax in ((1, 4), (2, 3), (3, 2)):
        F = GF(d)
        for a in range(1, amax + 1):
            expo = 1
            for code in range(F.n ** a):
                c, u = code, []
                for _ in range(a):
                    u.append(c % F.n)
                    c //= F.n
                if u[0] == 0:
                    continue                     # not a unit
                k, w = 1, list(u)
                one = [1] + [0] * (a - 1)
                while w != one:
                    w = polymul(F, w, u, a)
                    k += 1
                    assert k <= F.n ** a, "unit order runaway"
                expo = lcm(expo, k)
            ok(expo == Ring("x", 1).lam_pp(d, a),
               "the unit-group exponent of F_%d[t]/(t^%d) is %d, the law says"
               " %d" % (F.n, a, expo, Ring("x", 1).lam_pp(d, a)))
            m += 1
    print("      %d (residue field, depth) pairs for the 1-unit exponent and"
          % n)
    print("      %d full unit groups computed element by element: lam_pp is"
          % m)
    print("      the ring's own lambda, not a restatement of its shape.")


def polysq(F, u, a):
    out = [0] * a
    for i in range(a):
        if 2 * i < a:
            out[2 * i] ^= F.sq(u[i])
    return out


def polymul(F, u, v, a):
    out = [0] * a
    for i in range(a):
        if not u[i]:
            continue
        for j in range(a - i):
            out[i + j] ^= F.mul(u[i], v[j])
    return out


def s1b_curves(rings, curves):
    print("\n  (b) the curve arithmetic: direct point counts over F_{2^d}")
    print("      against the zeta function, and closed points against Moebius")
    n = 0
    for name, curve, h in curves:
        t = 2 + 1 - h
        s = [2, t]
        for i in range(2, DMAX + 1):
            s.append(t * s[i - 1] - 2 * s[i - 2])
        N = [None] + [(1 << e) + 1 - s[e] for e in range(1, DMAX + 1)]
        for d in range(1, DMAX + 1):
            F = GF(d)
            ok(len(curve.points(F)) + 1 == N[d],
               "%s: #E(F_2^%d) = %d, zeta says %d"
               % (name, d, len(curve.points(F)) + 1, N[d]))
            want = sum(mobius(d // e) * N[e] for e in range(1, d + 1)
                       if d % e == 0) // d
            got = len(rings[name].by_deg[d]) + (1 if d == 1 else 0)
            ok(got == want, "%s: %d closed points of degree %d, Moebius says %d"
               % (name, got, d, want))
            n += 2
    print("      %d counts, all exact, degrees 1..%d over %d curves."
          % (n, DMAX, len(curves)))


def s1c_class_map(rings):
    print("\n  (c) the class map: sigma lands in E(F_2) at every place, and")
    print("      the affine degree-1 places carry the nonzero classes exactly")
    for name, R in sorted(rings.items()):
        if R.h == 1:
            continue
        d1 = set(R.cls[pl] for pl in R.by_deg[1])
        ok(d1 == set(range(1, R.h)),
           "%s: degree-1 classes are %s, not the nonzero classes" % (name, d1))
        ok(len(R.by_deg[1]) == R.h - 1,
           "%s: %d rational affine places at h = %d"
           % (name, len(R.by_deg[1]), R.h))
        ok(len(R.rider) == R.h - 1, "%s: the rider table is short" % name)
    print("      exact at every ring: h - 1 rational affine places, one per")
    print("      nonzero class, so every class has a degree-1 representative")
    print("      and lemma D's completion is always available.")


VOID_DEGREES = [2, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8]
VOID_KINDS = ["clocked", "deepen", "deepen", "fresh", "fresh", "deepen",
              "fresh", "fresh", "fresh", "fresh", "deepen"]


def s1d_poly_control(R):
    print("\n  (d) the h = 1 control: this engine on F_2[x], tie-broken by the")
    print("      encoding order, against the filed void trajectory")
    log = run(R, "ideal", {}, len(VOID_DEGREES))
    degs = [mv["cost"] for mv in log]
    ok(degs == VOID_DEGREES, "the F_2[x] void degrees are %s, filed %s"
       % (degs, VOID_DEGREES))
    encs = []
    for mv in log:
        m = 1
        for pl, e in mv["veh"].items():
            for _ in range(e):
                m = pmul(m, R.enc[pl])
        encs.append(m)
    ok(encs[:9] == [4, 2, 4, 7, 11, 16, 19, 37, 67],
       "the F_2[x] void encodings are %s" % encs[:9])
    ok(pdeg(encs[9]) == 7 and is_irr(encs[9]), "move 10 is not a degree-7 irr")
    ok(encs[10] == 256, "move 11 is not x^8")
    kinds = []
    st = {}
    for mv in log:
        core = max(mv["veh"], key=lambda pl: R.deg[pl] * mv["veh"][pl])
        kinds.append(R.kind(mv["state"].get(core, 0), mv["veh"][core]))
    ok(kinds == VOID_KINDS, "the F_2[x] void kinds are %s" % kinds)
    ok((1, 3) not in log[-1]["state"], "x+1 opened in the F_2[x] void")
    print("      moves 1-11 = %s" % encs)
    print("      degrees    = %s" % degs)
    print("      -- the filed trajectory, move for move, through an engine")
    print("      that knows nothing about polynomials except that they are")
    print("      the places of a genus-0 ring.")


def s1e_scan(rings, audit):
    print("\n  (e) the door brute: every state below the scan cap, both")
    print("      worlds, checked against a full enumeration of divisors")
    for name, R in sorted(rings.items()):
        for world in ("ideal", "element"):
            for seed in seeds_of(R, 2)[:6]:
                run(R, world, seed, 6, audit=audit)
    print("      %d states scanned, %d above the degree-%d cap."
          % (audit.scanned, audit.scan_skipped, SCAN_DEG))
    ok(audit.scanned > 0, "the menu was never brute-scanned")
    ok(not audit.starve_bad, "PR4 failed at %s" % audit.starve_bad[:3])
    ok(not audit.rider_bad, "PR3 failed at %s" % audit.rider_bad[:3])


# ---------------------------------------------------------- S2 geography
def s2_geography(rings, order):
    section("S2  THE GEOGRAPHY -- the complete class-group ladder at q = 2")
    print("  Places by degree, and where the degree-1 population sits. The")
    print("  mechanism variable is the number of AFFINE RATIONAL POINTS,")
    print("  which is h - 1: those are the only places a free rider can be,")
    print("  and two of them at one degree is the only way a rider can also")
    print("  be a tie member.\n")
    print("  %-8s %-4s %-30s %-14s %s"
          % ("ring", "h", "places of degree 1..8", "deg-1 classes",
             "class fibres"))
    for name in order:
        R = rings[name]
        row = [len(R.by_deg[d]) for d in range(1, 9)]
        cl = sorted(R.cls[pl] for pl in R.by_deg[1])
        # HOW EVENLY the class map splits a degree. This is what decides how
        # much narrower a PRINCIPAL world's openings are than an ideal
        # world's, and it is near-uniform rather than uniform -- so an exact
        # division by h at any one degree is that near-uniformity and not an
        # identity.
        even, spread, live = 0, 0, 0
        for d in range(1, DMAX + 1):
            pls = R.by_deg[d]
            if len(pls) < R.h:
                continue
            live += 1
            fib = [0] * R.h
            for pl in pls:
                fib[R.cls[pl]] += 1
            even += (len(set(fib)) == 1)
            spread = max(spread, max(fib) - min(fib))
        print("  %-8s %-4d %-30s %-14s %s"
              % (name, R.h, row, cl or "none",
                 "equal at %d/%d degrees, spread <= %d" % (even, live, spread)))


# -------------------------------------------------------- S3/S4 the worlds
def run_world(rings, order, world, audit):
    section("S%s  THE %s WORLD -- cold D-DYN, %d moves, seeds to degree %d"
            % ("3" if world == "ideal" else "4", world.upper(), T_RUN, SEED_DEG))
    if world == "element":
        print("  Moves are PRINCIPAL. Lemma D says every one of them is an")
        print("  ideal core plus at most one rational point, and the rider is")
        print("  fixed by the core's class -- asserted at every move (PR3).\n")
    else:
        print("  Lemma C says a declined member can never come back: an")
        print("  unseated place is CLOCKED where a seated one deepens, and")
        print("  the clocked door is strictly dearer -- asserted at every")
        print("  visited state (PR4).\n")
    print("  A DECLINED place is STARVED when the move leaves its degree")
    print("  seated (lemma C dominates it in the ideal world) and FREE")
    print("  otherwise -- a free decline means the tie was a REORDERING and")
    print("  the place is expected back. Only a STARVED decline that comes")
    print("  back is a readmission in the sense the formula means.\n")
    print("  %-8s %-6s %-6s %-6s %-11s %-11s %s"
          % ("ring", "seeds", "cost", "tie", "starved", "free", "tail"))
    print("  %-8s %-6s %-6s %-6s %-11s %-11s %s"
          % ("", "", "max", "states", "declines/back", "declines/back",
             "vehicles"))
    out = {}
    for name in order:
        R = rings[name]
        seeds = seeds_of(R, SEED_DEG)
        cmax, ties, tails = 0, 0, set()
        xtype, wmax = 0, 0
        ns = nsb = nf = nfb = 0
        first_readm, rdegs = None, {}
        lastback, prefix = -1, -1
        for seed in seeds:
            log = run(R, world, seed, T_RUN, audit=audit)
            cmax = max(cmax, max(mv["cost"] for mv in log))
            ties += sum(1 for mv in log if mv["nties"] > 1)
            xtype += sum(1 for mv in log if mv["ntypes"] > 1)
            wmax = max([wmax] + [mv["maxtype"] for mv in log])
            a, b, c, d, fi, dg, when = readmission(R, log)
            ns, nsb, nf, nfb = ns + a, nsb + b, nf + c, nfb + d
            for k, v in dg.items():
                rdegs[k] = rdegs.get(k, 0) + v
            # THE SEATED-ONCE CHECK, the step that makes the capacity bound
            # bite. Every readmitted place is a rational point (asserted
            # below), and its readmission IS its seating, so all of that
            # place's failed openings share ONE back-move and a trajectory
            # can lose at most h - 1 distinct places.
            if when:
                seats = seating_moves(R, log, set(pl for _, _, pl in when))
                for _, backmv, pl in when:
                    ok(seats[pl] == backmv,
                       "%s/%s: a readmission at move %d is not that place's "
                       "own seating (seated at %s) -- the seated-once step "
                       "does not hold" % (name, world, backmv + 1, seats[pl]))
                    lastback = max(lastback, backmv)
                ok(len(set(pl for _, _, pl in when)) <= R.h - 1,
                   "%s/%s: %d distinct places readmitted, above the h - 1 = %d "
                   "rational points" % (name, world,
                                        len(set(pl for _, _, pl in when)),
                                        R.h - 1))
                prefix = max(prefix, len(when))
            if b and first_readm is None:
                first_readm = (R.veh_deg(seed) if seed else 0, fi, dict(seed))
            tv = set(vkey(mv["veh"]) for mv in log[-LOCK_R:])
            tails.add(len(tv))
            ok(len(tv) > 1,
               "PR2: %s/%s locked -- the last %d moves are one vehicle"
               % (name, world, LOCK_R))
        out[name] = (len(seeds), cmax, ties, ns, nsb, nf, nfb, first_readm,
                     rdegs, lastback, prefix, xtype, wmax)
        print("  %-8s %-6d %-6d %-6d %-11s %-11s %s"
              % (name, len(seeds), cmax, ties, "%d/%d" % (ns, nsb),
                 "%d/%d" % (nf, nfb), "%d..%d" % (min(tails), max(tails))))
    if world == "ideal":
        for name in order:
            ok(out[name][4] == 0,
               "PR4/lemma C: %s readmitted a STARVED decline in the ideal "
               "world" % name)
        print("\n  0 starved declines came back anywhere: lemma C holds at")
        print("  the level of the IMAGE and not only of the door.")
    else:
        print("\n  READMISSION, by the DEGREE of the place that came back --")
        print("  the number that decides whether the mechanism can scale:")
        for name in order:
            _, _, _, ns, nsb, _, _, fr, rd, lb, px, _, _ = out[name]
            print("    %-8s %4d of %6d starved declines back, degrees %s"
                  % (name, nsb, ns, dict(sorted(rd.items())) or "none"))
            if nsb:
                mv, d, back, veh = fr[1]
                print("      first: seed %s, declined at move %d, back at move"
                      " %d in the vehicle %s"
                      % (fmt_state(R_OF[name], fr[2]), mv + 1, back + 1,
                         fmt_state(R_OF[name], veh)))
                print("      last readmission at move %d; worst trajectory"
                      " lost %d openings" % (lb + 1, px))
        allrd = {}
        for name in order:
            for k, v in out[name][8].items():
                allrd[k] = allrd.get(k, 0) + v
        ok(set(allrd) <= {1},
           "a readmitted place had degree > 1: %s -- the rider bound is not "
           "what confines readmission" % sorted(allrd))
        print("  Every readmitted place has DEGREE 1, and no trajectory has")
        print("  more distinct readmission moves than it has rational points")
        print("  to seat (asserted per seed). A finite set of VICTIMS is not")
        print("  yet a finite number of failed openings -- one place declined")
        print("  endlessly would break the bound. What closes it is that")
        print("  depths never fall, so a readmission IS a seating and each of")
        print("  the h - 1 rational points can be seated once. It is NOT")
        print("  that the seatings finish -- measured from the void at the")
        print("  horizon, rational points seated:")
        unfinished = 0
        for name in order:
            R = R_OF[name]
            if R.h == 1:
                continue
            log = run(R, "element", {}, T_RUN)
            st = apply_veh(log[-1]["state"], log[-1]["veh"])
            got = sum(1 for pl in R.by_deg[1] if st.get(pl, 0) > 0)
            unfinished += (got < R.h - 1)
            print("    %-8s %d of %d" % (name, got, R.h - 1))
        ok(unfinished > 0,
           "every ring seats all its rational points, so the claim that the "
           "bound does not need the seatings to finish is untested here")
        print("  -- so a point can stay unseated forever, and a point never")
        print("  seated is never readmitted either: the same bound from the")
        print("  other side.")
    return out


# ------------------------------------------------------------- S5 lockstep
def veh_type(R, world, veh):
    """What the ENGINE can read about a vehicle. lam reads (degree, depth)
    only; the element world reads one more thing, the CLASS, through the
    principality test and the rider. Nothing else is legible."""
    if world == "ideal":
        return tuple(sorted((R.deg[pl], e) for pl, e in veh.items()))
    return tuple(sorted((R.deg[pl], R.cls[pl], e) for pl, e in veh.items()))


def tie_reps(R, world, ties, width):
    """The members lockstep is ABOUT. A tie set splits into engine TYPES --
    lambda reads (degree, depth), and the element world reads one further
    datum, the CLASS, through the principality test and the rider. Choosing
    between two TYPES is a different move and the sequences are expected to
    differ (that is the reordering S3/S4 measures). Lockstep is the claim
    about choosing between two MEMBERS OF ONE TYPE, so the enumeration
    branches inside the largest such type and nowhere else."""
    by = {}
    for v in ties:
        by.setdefault(veh_type(R, world, v), []).append(v)
    big = max(by.values(), key=len)
    if len(big) < 2:
        return ties[:1], False
    return big[:width], True


def branches(R, world, seed, T, splits, width=4):
    """Branch at the first `splits` within-type openings, then run
    canonically to T. Returns (signature sequences, splits actually taken)."""
    menu = MENUS[world]
    out, taken = [], 0
    stack = [(dict(seed), R.lam_state(seed), [], 0, 0)]
    while stack:
        st, L, log, used, spent = stack.pop()
        if used == T:
            out.append(tuple(log))
            continue
        cost, ties = menu(R, st, L)
        pick, real = ties[:1], False
        if len(ties) > 1 and spent < splits:
            pick, real = tie_reps(R, world, ties, width)
        if real:
            taken = max(taken, spent + 1)
        for veh in pick:
            child = apply_veh(st, veh)
            stack.append((child, R.lam_state(child),
                          log + [sig_of(R, st, veh, cost)], used + 1,
                          spent + (1 if real else 0)))
    return out, taken


def s5_lockstep(rings, order):
    section("S5  LOCKSTEP -- does the count FACTOR over openings?")
    print("  Lockstep -- the multiplicity at a later opening must not depend")
    print("  on the choice made at an earlier one -- was the formula's one")
    print("  contingent assumption when this file was written, and is since")
    print("  PROVED (explore_greedy_image_g2.py). What follows is a control")
    print("  on a theorem. Branching runs over the first %d"
          % SPLITS)
    print("  openings and canonically thereafter, to %d moves, comparing the"
          % T_LS)
    print("  (cost, kind, degree-exponent) sequences. Branching is WITHIN A")
    print("  TYPE only: choosing between two TYPES is a different move, and")
    print("  its sequences differ by construction -- that is the reordering")
    print("  S3 and S4 measure, not a lockstep failure. A seed with no")
    print("  within-type opening has ONE branch and carries no evidence, so")
    print("  the seeds where the test has CONTENT are counted separately.\n")
    print("  %-8s %-8s %-7s %-9s %-9s %s"
          % ("ring", "world", "seeds", "branches", "disagree", "first split"))
    print("  %-8s %-8s %-7s %-9s %-9s %s"
          % ("", "", "w/ content", "", "", ""))
    out = {}
    for name in order:
        R = rings[name]
        for world in ("ideal", "element"):
            seeds = seeds_of(R, 2)
            nb, bad, live, first = 0, 0, 0, None
            for seed in seeds:
                logs, taken = branches(R, world, seed, T_LS, SPLITS)
                nb += len(logs)
                live += (taken > 0)
                sigs = set(logs)
                if len(sigs) > 1:
                    bad += 1
                    if first is None:
                        a, b = sorted(sigs)[:2]
                        k = next(i for i in range(len(a)) if a[i] != b[i])
                        first = (R.veh_deg(seed) if seed else 0, k, a[k], b[k])
            out[(name, world)] = (live, nb, bad, first)
            print("  %-8s %-8s %-7s %-9d %-9d %s"
                  % (name, world, "%d/%d" % (live, len(seeds)), nb, bad,
                     "move %d: %s vs %s" % (first[1] + 1, first[2], first[3])
                     if first else "-"))
    for name in order:
        ok(out[(name, "ideal")][2] == 0,
           "PR6a: ideal lockstep failed at %s" % name)
    print("\n  Ideal lockstep holds at every ring (PR6a): lambda reads")
    print("  (degree, depth), the degree-multiset is branch-independent, and")
    print("  nothing else can reach a door.")
    return out


# ------------------------------------------------------------- S6 the table
def s6_table(ideal_out, elem_out, ls_out, order):
    section("S6  THE FOUR-WORLD TABLE -- what the untouched cell does")
    # THE DEGENERACY CONTROL, free and never taken until now: at h = 1 every
    # divisor is principal, so the two worlds are ONE world and the element
    # machinery -- the class arithmetic, the rider lookup, the principality
    # filter in the brute scan -- must reproduce the ideal engine exactly. If
    # it does not, every h > 1 difference below is partly the element code
    # path rather than the class group.
    ok(ideal_out["F_2[x]"] == elem_out["F_2[x]"],
       "the element engine does not degenerate to the ideal one at h = 1: "
       "%s vs %s" % (ideal_out["F_2[x]"], elem_out["F_2[x]"]))
    ok(ls_out[("F_2[x]", "ideal")] == ls_out[("F_2[x]", "element")],
       "the h = 1 lockstep rows differ between the two worlds")
    print("  DEGENERACY CONTROL: at h = 1 every divisor is principal, so the")
    print("  two worlds are one world -- and the element engine reproduces")
    print("  the ideal one row for row at F_2[x], asserted. Every difference")
    print("  below is therefore the class group and not the code path.\n")
    print("  MULTIPLICITY is the largest WITHIN-TYPE tie width, which is the")
    print("  only one an opening can survive, followed by how many tie states")
    print("  were CROSS-type -- those are reorderings, and a raw tie count")
    print("  that includes them overcounts the formula's multiplicity.")
    print("  PERMANENCE is starved declines that came BACK; a starved decline")
    print("  is the only kind that could have survived, a free one being a")
    print("  reordering. LOCKSTEP is seeds whose branches disagree.\n")
    print("  %-16s %-16s %-15s %-15s %s"
          % ("ring, world", "multiplicity", "openings", "permanence",
             "lockstep"))
    print("  %-16s %-16s %-15s %-15s %s"
          % ("Z", "1 (order)", "stop (lock)", "n/a", "n/a"))
    print("  %-16s %-16s %-15s %-15s %s"
          % ("K, ideal", "2 (Galois)", "stop (lock)", "holds", "holds"))
    print("  %-16s %-16s %-15s %-15s %s"
          % ("K, element", "2 (Galois)", "stop (lock)", "holds", "holds"))
    for name in order:
        for world in ("ideal", "element"):
            n, nb, bad, first = ls_out[(name, world)]
            src = ideal_out if world == "ideal" else elem_out
            _, cmax, ties, ns, nsb, nf, nfb, _, _, _, _, xt, wm = src[name]
            print("  %-16s %-16s %-15s %-15s %s"
                  % ("%s, %s" % (name, world),
                     "<= %d, %d/%d cross" % (wm, xt, ties),
                     "never (sprawl)", "%d/%d back" % (nsb, ns),
                     "%d/%d seeds split" % (bad, n)))


def main():
    curves = [("h2", Curve(1, 1, 0, 0, 1), 2),
              ("h3", Curve(0, 0, 1, 0, 0), 3),
              ("h4", Curve(1, 0, 0, 0, 1), 4),
              ("h5", Curve(0, 0, 1, 1, 0), 5)]
    section("S1  THE POSITIVE CONTROL -- run before any image is read")
    s1a_unit_law()
    rings = {}
    for name, curve, h in curves:
        rings[name] = build_curve_ring(name, curve, h, DMAX)
    rings["F_2[x]"] = build_poly_ring(DMAX)
    R_OF.update(rings)
    order = ["F_2[x]", "h2", "h3", "h4", "h5"]
    s1b_curves(rings, curves)
    s1c_class_map(rings)
    s1d_poly_control(rings["F_2[x]"])
    audit = Audit()
    s1e_scan(rings, audit)
    print("\n  Control green.")
    s2_geography(rings, order)
    ideal_out = run_world(rings, order, "ideal", audit)
    elem_out = run_world(rings, order, "element", audit)
    section("THE AUDIT -- every state the trajectories visited")
    print("  states visited:                 %d" % audit.states)
    print("  brute-scanned:                  %d (%d above the degree-%d cap)"
          % (audit.scanned, audit.scan_skipped, SCAN_DEG))
    print("  tie states:                     %d" % audit.tie_states)
    print("  tie multiplicities:             %s"
          % dict(sorted(audit.tie_sizes.items())))
    print("  tie sets straddling two degrees: %d" % audit.tie_multideg)
    print("  door exponents checked against the closed form (lemma A,")
    print("  searched vs 2^c+1-e / 1 / 2^c+1): %d" % audit.doors)
    print("  permanence checks (lemma C):    %d" % audit.starve)
    print("  element moves rider-checked:    %d" % audit.riders)
    ok(not audit.starve_bad, "PR4 failed at %s" % audit.starve_bad[:3])
    ok(not audit.rider_bad, "PR3 failed at %s" % audit.rider_bad[:3])
    ok(not audit.door_bad, "PR1/lemma A: the searched door and the closed "
       "form disagree at %s" % audit.door_bad[:3])
    ls_out = s5_lockstep(rings, order)
    s6_table(ideal_out, elem_out, ls_out, order)
    print("\nALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
