"""explore_greedy_image_g2.py -- THE FIFTH RING: genus 2, where the rider
stops being a rational point, and what that does to the product formula.

THE QUESTION. |Im_greedy| = the product, over a trajectory's SURVIVING
openings, of the tie multiplicity at each. Survival has two halves and one
of them is closed: PERMANENCE fails at only finitely many openings over any
function field of a finite field, because the rider is always a
minimal-degree representative of the class the core needs cancelled, there
are finitely many classes, each class's minimal representatives form a
finite linear system, and a readmission IS a seating
(explore_greedy_image_ec.py F9). ERASURE was excluded by construction: it
needs a recurrent vehicle, a recurrent vehicle is a lock, and a lock stops
the openings. What is LEFT is LOCKSTEP -- the multiplicity at a later
opening must not depend on the choice made at an earlier one, which is what
makes the count FACTOR rather than merely bound. It is asserted in every
ring run so far and proved in none, and genus 1 is the wrong place to test
it: there each nonzero ideal class has exactly ONE degree-1 representative,
so the rider is the same PLACE in both branches and nothing can diverge.

THE RING. R = the affine coordinate ring of a genus-2 curve over F_2 with a
rational point at infinity: C: y^2 + y = x^5 + x, the functions regular away
from O. Deg f = 5 makes the model IMAGINARY -- one point at infinity, and it
is rational and a Weierstrass point -- so R is Dedekind of equal
characteristic 2 with Pic(R) = Pic^0(C) = Jac(C)(F_2), of order 15 here. Its
PLACES are the closed points of the affine curve. Against the elliptic ring
of the fourth cell, exactly one dial moves: THE GENUS. Everything else --
characteristic, base field, residue-field ladder, the lambda law -- is held
fixed, so any difference is genus and nothing else.

WHAT THE GENUS BUYS, and it is not what the handover expected. On a genus-2
curve Riemann-Roch gives l(D) = 1 + l(K - D) at deg D = 2, and K has degree
2, so a degree-2 class carries TWO independent functions exactly when it is
canonical and one otherwise -- the canonical class is the one place a class
can have SEVERAL minimal representatives, and q + 1 = 3 of them. But in the
imaginary model K ~ 2O, so that class is the TRIVIAL one, whose minimal
affine representative is the EMPTY divisor and which summons no rider at
all; its three members are 2O, which is not affine, and the two affine
fibres of x and x + 1, which are principal. The multiplicity Riemann-Roch
grants therefore lands exactly on the class that never rides, and EVERY
NONZERO CLASS HAS EXACTLY ONE MINIMAL AFFINE REPRESENTATIVE. The rider is
still SUMMONED, not chosen. That is settled at the desk before the engine
runs, and S1 checks it by enumeration.

What genus 2 DOES change is the rider's SIZE: 10 of the 15 classes need a
degree-2 completion, which is either a PAIR of rational points or an
irreducible degree-2 PLACE. Genus 1's lemma D -- "the free rider is always a
rational point, and the vehicle is a core plus at most one of them" -- is
FALSE here, and it was load-bearing for both the menu's completeness and the
capacity bound. Both are re-derived below at the genus the ring has.

TRANSPLANT FLAGS, fixed at the freeze. Every intuition below is imported
from a neighbouring value of the ring parameter and is marked rather than
trusted.
 1. From the elliptic ring: "the rider is a rational point, so a vehicle is
    a core plus at most one passenger, of degree at most the ideal minimum
    plus one." FALSE at genus 2 and replaced by lemma D below; the exponent
    offsets the menu must try change with it.
 2. From the elliptic ring: "readmission is confined to degree 1." That
    argument prices the two completions and finds they move the comparison
    by at most 1. At genus 2 they move it by at most 2, so the confinement
    is re-derived (lemma F) and MEASURED, not carried.
 3. From every previous ring: "lockstep is an open observable to be
    measured." Replaced by lemma G, a proof; the run becomes its control
    rather than its evidence. The prediction that carries risk is no longer
    lockstep but the COARSE-TYPE GAP the proof exposes (PR7).
 4. From the elliptic ring: "a tie is a cost class and can straddle
    degrees." Kept -- it is a statement about the door law, which is
    unchanged here -- but re-measured rather than assumed.

THE HAND-ATTACK, on paper before any engine code, in seven lemmas. The rig
asserts each of them at the states it visits rather than assuming any.

 A. THE DOOR LAW IS UNCHANGED. With d = deg P, e = the depth of P,
    c = v2(lambda), lambda_odd = lambda >> c:
      DEEPEN  (e >= 1):                             r = 2^c + 1 - e, cost d*r
      FRESH   (e = 0, (2^d - 1) does not divide lambda_odd): r = 1, cost d
      CLOCKED (e = 0, (2^d - 1) divides lambda_odd):   r = 2^c + 1, cost
                                                       d*(2^c + 1)
    lam_P(a) = lcm(q^d - 1, p^ceil(log_p a)) reads (degree, depth) and
    nothing else (explore_module_law.py Theorem A, equal characteristic), and
    genus touches neither. Cost is the DEGREE of the vehicle, the canonical
    transfer of "least m".
 B. THE MINIMAL IDEAL MOVE IS A SINGLE-PLACE POWER. lambda(state + D) is an
    lcm over places, so D raises it exactly when some P^{n_P} in D does;
    then n_P >= door_r(P) and deg D >= d_P * n_P >= min over P of
    d_P*door_r(P). The minimisers are exactly the single-place powers.
 C. IDEAL-WORLD PERMANENCE. A seated place's own deepening door costs
    d*(2^c + 1 - e) <= d*2^c, while an unseated place of the same degree is
    CLOCKED at d*(2^c + 1) -- strictly more, at every state. A declined tie
    member is never readmitted in the ideal world.
 D. THE COMPLETION IS THE UNIQUE MINIMAL REPRESENTATIVE, of degree 0, 1 or
    2. Write minrep(c) for a minimal-degree effective affine divisor of
    class c. Riemann-Roch: at degree 2 every class of Pic^0 has l = 1 unless
    it is canonical, and canonical means trivial here, so for c != 0 there
    is exactly one effective divisor of degree 2 in the class, and it avoids
    O unless c already has a degree-1 representative. Hence minrep(c) is
    UNIQUE for every c, of degree 1 for the h_1 = #C(F_2) - 1 classes of a
    rational point and 2 for the rest. A principal ticking divisor D
    decomposes as P^n + rest with n >= door_r(P) and cls(rest) = -n*cls(P),
    so deg D >= d*n + deg minrep(-n*cls(P)) and the minimisers are exactly
    the core-plus-minrep vehicles. Since deg minrep <= 2, an exponent
    n >= r + 3 costs at least 3 more than n = r and can save at most 2: THE
    MENU MUST TRY r, r+1 AND r+2, and no more.
 E. THE SPRAWL COVERS BUNDLES. Suppose every move past t0 has degree <= B.
    Norm-finiteness makes the vehicles past t0 a finite set, so the support
    stops growing and the multiplicities per move are bounded by some m.
    After M further moves no depth exceeds C + M*m, the (q^d - 1) factors
    are frozen, and every tick must come from some depth crossing a p-power
    frontier -- at most |S|*(log_p(C + M*m) + 1) of those, against the M
    ticks M moves require. That fails for large M, so costs diverge in
    EITHER world, at any genus.
 F. THE CAPACITY BOUND AT GENUS 2. A starved place P of degree d sits under
    every seated same-degree neighbour's door: its own costs d*(2^c + 1)
    against the seated one's d*(2^c + 1 - e), a gap of d*e, and pricing both
    completions moves that by at most 2. So P can be a minimal CORE only
    when d*e <= 2, i.e. (d, e) in {(1,1), (1,2), (2,1)}; and P can be a
    PASSENGER only if it lies in the support of some minrep. Both sets are
    finite and confined to degree <= 2, so the places a readmission can ever
    seat are a fixed finite set. Depths never fall, so a readmission IS a
    seating and each such place is lost at most once: permanence fails at
    finitely many openings, exactly as at genus 1, with the victim set
    widened from the rational points to the minrep support.
 G. LOCKSTEP IS A THEOREM. Colour a place by chi(P) = (deg P, cls P).
    Everything the engine reads is chi-determined: lambda reads (degree,
    depth), principality reads the class sum, and the minimal
    representatives of a class are the effective divisors of a given degree
    and class. So any permutation tau of places with chi o tau = chi is an
    automorphism of the whole dynamics: tau(menu(s)) = menu(tau s), and a
    move's signature at s equals its image's at tau s. Now refine the colour
    by the state, kappa_s(P) = (deg P, cls P, s(P)), and define the REFINED
    TYPE of a vehicle v at s as the multiset {(deg P, cls P, v(P), s(P))}.
    If two menu members have the same refined type, then for each kappa
    colour their exponent multisets agree, so a kappa-preserving permutation
    carries one to the other -- and a kappa-preserving permutation fixes s.
    Hence the future TREE under one is isomorphic to the tree under the
    other: EVERY LATER OPENING HAS THE SAME MULTIPLICITY, and the count
    factors. This holds at every ring the corpus has run, not only here.
 H. AND WHERE THE CONTINGENCY MOVES TO. Lemma G is about the REFINED type;
    the corpus's type is (degree, class, exponent) with no state depth. For
    a bare door exponent the two agree -- r = 2^c + 1 - e determines e, and
    a fresh place of a degree that already has a seated neighbour is clocked
    at 2^c + 1 and so strictly dearer, hence never in the same tie -- but
    the element world also offers r+1 and r+2, and a place at depth e using
    exponent r then shares a coarse type with a place at depth e+1 using the
    same exponent. Their successors carry the same lambda and DIFFERENT
    depths, so their futures can diverge. Whether such a pair ever occurs is
    an observable, not a derivation, and it is what PR7 measures.
    SUPERSEDED: it is a derivation. The r+1 and r+2 offers never produce a
    divisor the bare door does not, so the pair cannot occur here or at any
    ring with unique minimal representatives (explore_coarse_type.py lemma
    S); PR7's observable was sound and its mechanism was empty by proof.

THE OBSERVABLE. With no lock there is no finite limit to enumerate, so
"count the limits" is not a finite question; what is finite and decidable at
a horizon is the two halves of SURVIVING (permanence, lockstep) plus the
structure lemma D and lemma F rest on. Readmission alone cannot falsify the
gap -- if every opening fails to survive the product is empty and the image
is a POINT. The gap falls only if the count fails to FACTOR.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE DOOR LAW AND THE IDEAL MINIMUM are lemmas A and B exactly: at every
    scanned state no effective divisor of degree below the engine's cost
    raises lambda, and the min-degree raisers are exactly the engine's tie
    set -- single-place powers in the ideal world.
    KILL: one scanned state where a cheaper raiser exists, or where the
    min-degree raisers differ from the menu's ties.
PR2 THE IDEAL WORLD SPRAWLS: no trajectory's tail is one repeated vehicle,
    and the cost sequence is unbounded.
    KILL: a trajectory whose last LOCK_R moves are the same vehicle.
PR3 THE RIDER IS UNIQUE AND NO LONGER RATIONAL (lemma D). What the rig
    PRINTS: per class, the number and degree of minimal affine
    representatives; and per element move, whether the vehicle is a core
    plus exactly minrep of the cancelling class. The prediction is that
    every nonzero class has exactly ONE, that both degree-1 and degree-2
    completions occur, and that a degree-2 completion appears in BOTH
    shapes -- a pair of rational points, and an irreducible degree-2 place.
    KILL: a class with two minimal representatives, or an element move whose
    completion is not minrep of its class, or a vehicle exceeding the ideal
    minimum at that state by 3 or more.
PR4 IDEAL PERMANENCE HOLDS AT EVERY VISITED STATE (lemma C).
    KILL: one visited state where an unseated place's door does not strictly
    exceed every seated same-degree place's door.
PR5 READMISSION IS REAL AND CONFINED TO THE MINREP SUPPORT (lemma F). What
    the rig PRINTS: per opening, whether a place carried only by a DECLINED
    member is seated later in the same branch within the horizon, split by
    whether the move STARVED it, and the degree of every place that came
    back. The prediction is that starved readmissions occur in the element
    world and none in the ideal world, that every readmitted place has
    degree <= 2, and that no trajectory readmits more distinct places than
    the minrep support holds.
    KILL: a starved readmission in the ideal world, a readmitted place of
    degree >= 3, or a trajectory exceeding the support bound.
PR6 LOCKSTEP HOLDS, in both worlds, and the rig CERTIFIES lemma G rather
    than merely observing its conclusion: at every within-type tie it
    constructs the permutation tau, and asserts that tau preserves degree
    and class at every place, fixes the current state, carries one tie
    member to the other, and FIXES EVERY MINIMAL REPRESENTATIVE -- the last
    being the step genus could have broken. Branch signature sequences are
    then compared to the horizon as the end-to-end check.
    KILL: a within-type tie with no such tau, or two branches from one seed
    with differing signature sequences.
PR7 THE COARSE-TYPE GAP -- frozen as an OPEN OBSERVABLE with no prediction,
    and the one place risk is left after lemma G. What the rig PRINTS: how
    many tie states hold two members of the same COARSE type (degree, class,
    exponent) at different core DEPTHS, which lemma H says can only come
    from the r+1 / r+2 offsets. A nonzero count means the multiplicity the
    corpus reports is taken across branches lemma G does not cover, and the
    reading has lineage into every ring already run.
PR8 THE IMAGE, printed and not predicted: distinct states at the horizon per
    seed per world, tie multiplicities raw and within-type, and the count of
    openings whose declined members are never readmitted within the horizon.
    A horizon count of survivors is an UPPER bound and is reported as such.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE FIFTH RING IS CHEAP, AND GENUS IS THE ONLY DIAL THAT MOVED (rule in
   range; 90 trajectories x 12 moves over two worlds, seeds the void plus
   every effective divisor to degree 3). #Jac(F_2) = 15 twice over, from the
   zeta function built out of N_1 = 5 and N_2 = 9 and from the reduced-
   Mumford enumeration, which are independent computations; 28 point and
   closed-point counts exact at degrees 1..14; places of degree 1..8 read
   [4, 2, 0, 2, 4, 12, 20, 22]. Everything upstream of the rider is the
   elliptic ring's verbatim -- 16464 door exponents found by SEARCH match
   lemma A's closed form, no trajectory locks in either world (the last 6
   moves are 6 distinct vehicles at every seed), and 0 of 9040 starved ideal
   declines return, so lemma C holds at the level of the image. Genus
   reaches the dynamics through the completion and nowhere else.

F2 THE CANONICAL MULTIPLICITY LANDS ON THE CLASS THAT NEVER RIDES (rule,
   proved, and enumerated at 15 of 15 classes). Riemann-Roch gives
   l(D) = 1 + l(K - D) at degree 2, so a degree-2 class carries two
   independent functions exactly when it is canonical -- the one place a
   class could have SEVERAL minimal representatives, and q + 1 = 3 of them.
   In the imaginary model K ~ 2O, so that class is the TRIVIAL one: its
   minimal affine representative is the empty divisor, it summons no rider
   at all, and its three members of |K| are 2O, which is not affine, plus
   the two affine fibres of x and x + 1, which are principal. Hence EVERY
   NONZERO CLASS HAS EXACTLY ONE MINIMAL AFFINE REPRESENTATIVE -- 4 of
   degree 1, 10 of degree 2 -- and the rider is still SUMMONED, not chosen.
   The mechanism this ring was built to expose, a branch's earlier choice
   deciding which representative a later move summons, cannot fire at genus
   2. That is settled at the desk before any trajectory runs, and it is the
   reason the ring's interest turned out to lie elsewhere.

F3 BUT THE RIDER STOPS BEING A RATIONAL POINT (rule, proved as lemma D;
   reconstructed at 588 chosen element moves and at all 1550 element tie
   members). The completion is the unique minimal representative of the
   class the core must cancel, of degree 0, 1 or 2 -- 169, 176 and 243
   moves respectively -- and a degree-2 completion appears in ALL THREE
   shapes it can have: a DOUBLED rational point, a pair of DISTINCT rational
   points, and an irreducible degree-2 PLACE (4, 4 and 2 of the ten degree-2
   classes respectively). The support size is part of the shape, and a census
   keyed on the degree multiset alone hides the first two inside one entry.
   Genus 1's lemma D, "a core plus at most one rational point", is false
   here, and it was load-bearing twice: the menu must try core exponents
   r, r+1 and r+2 rather than r and r+1, and the set of places a readmission
   can ever seat widens from the h - 1 rational points to the support of the
   minimal representatives -- 6 places here, of degrees 1 and 2.

F4 THE CAPACITY BOUND SURVIVES THE WIDENING (rule in range, with lemma F;
   16 readmissions, none exceeding the bound). In the element world 16 of
   786 starved declines return against 0 of 9040 in the ideal world, every
   returning place is that place's own first seating, and no trajectory
   loses more distinct places than the support holds -- the worst loses 3
   openings. Every returning place has degree 1: the widening lemma F
   PERMITS, from degree 1 to degree <= 2, did not materialise, so the bound
   grew and the phenomenon did not. From the void all 6 ridable places are
   seated by the horizon, which is the bound from the other side -- a place
   never seated is never readmitted either.

F5 LOCKSTEP IS A THEOREM (proved, lemma G; certified 2533 times at visited
   ties and end-to-end at 120 branches). Everything the engine reads is a
   function of a place's (degree, class): lambda reads (degree, depth),
   principality reads the class sum, and a class's minimal representatives
   are the effective divisors of a given degree and class. So any
   permutation of places preserving that colouring is an automorphism of the
   whole dynamics, and two tie members of one REFINED type -- the colouring
   plus the state depth -- are carried one to the other by such a
   permutation that also FIXES the state. The subtrees are then isomorphic,
   every later opening has the same multiplicity, and THE COUNT FACTORS.
   The rig certifies the permutation rather than observing its consequence:
   at every within-type tie it exhibits the transposition list and asserts
   that it preserves degree, preserves class, fixes the state, carries one
   member to the other, and FIXES EVERY MINIMAL REPRESENTATIVE -- the last
   being the obligation genus could have broken, since a rider inside a
   repeated (degree, class) group would be moved by it. No rider is: the
   least degree at which two places share a class is 6, and every rider has
   degree 1 or 2. This closes the assumption the product formula has rested
   on in every ring the corpus has run, and it closes it for all of them at
   once, not only for this one.
   AND THE END-TO-END CHECK IS STRICTER THAN THE THEOREM, which is worth
   saying because PR6's kill condition is not sound as frozen. Branch
   signature sequences agree at 17 of 17 seeds with content in both worlds,
   over branching capped at the first 2 within-type openings, 4 members per
   opening and 8 moves. But lemma G gives an isomorphism of the two
   SUBTREES, not equality of the CANONICAL PATH through them: the tie-break
   orders vehicles by place key, which is the one thing the colouring does
   not preserve, so the two branches can descend to corresponding-but-
   different vehicles. Agreement therefore over-delivers, and a
   disagreement would have needed diagnosis rather than being the automatic
   kill PR6 called it. The evidence for lemma G is the 2533 certificates,
   which check the permutation itself; the signature comparison is a
   bonus observation that the tie-break happens to be compatible too.

F6 AND THE CONTINGENCY MOVES TWICE, WHICH IS THE POINT (rule in range, and
   the scope statement that decides what F5 is worth). Lemma G is about the
   REFINED type; the corpus's type is (degree, class, exponent) with no
   state depth. For a BARE door exponent the two coincide, by two lines:
   r = 2^c + 1 - e determines e, and a fresh place of a degree that already
   has a seated neighbour is clocked at 2^c + 1 and so strictly dearer,
   hence never in the same tie. The ONLY route to a coarse type holding two
   depths is a core exponent above the bare door -- which lemma D's own
   derivation permits, and which the menu therefore has to offer. In range
   no such vehicle exists anywhere: all 1550 element tie members reconstruct
   at offset 0, and 0 of 919 tie states hold a coarse-type collision. So
   PR7's zero is VACUOUS -- it is evidence about the offsets, not about the
   collision, and a zero from an observable whose mechanism never fired is
   worth saying out loud rather than banking. What survives is sharper than
   what was asked: in range the corpus's coarse type IS the factoring type,
   for the proved bare-door reason, and the formula's remaining risk is two
   named things and no longer lockstep -- whether an offset vehicle can
   enter a tie set at all, and the still-unproved claim that a CROSS-type
   decline is a reordering rather than a choice.
   SUPERSEDED IN PART: the first of those is closed. An offset vehicle is
   never a NEW divisor -- minrep(-(r+j)c) + j*P represents the class the
   bare door must cancel, so the bare door is never dearer, and unique
   minimal representatives make the equality case the same divisor
   (explore_coarse_type.py). The offer of r+1 and r+2 in the menu below is
   correct and complete and never the source of a tie member, the zero
   above is a theorem rather than a vacuity, and the CROSS-type reading is
   the formula's whole remaining risk.
   SINCE SETTLED, AND IT SPLIT: a cross-degree decline is a reordering, a
   same-degree decline in another CLASS is a choice above the genus, and
   two clock moves at different degrees are open. The within-type
   multiplicity is therefore a lower bound (explore_reordering.py).

THE DESIGN, in six sections after the control.

 S1 THE POSITIVE CONTROL, run before any image is read.
    (a) The equal-characteristic 1-unit law: lam_pp against the exponent of
        FULL unit groups of F_{2^d}[t]/(t^a) computed element by element,
        which is the check that does not restate the law's own shape.
    (b) The curve arithmetic: point counts over F_{2^d} from direct
        enumeration against the zeta function built from N_1 and N_2, and
        the closed-point counts against the Moebius formula.
    (c) The class group: the reduced-Mumford enumeration counts P(1)
        exactly; Cantor composition makes it an abelian group with the
        empty divisor as identity; the class map is additive; and the
        fibre of every irreducible u(x) -- a principal divisor, being
        div(u) + (deg) O -- has class 0.
    (d) The Riemann-Roch census: minimal affine representatives per class,
        against the desk prediction that exactly #C(F_2) - 1 classes have a
        degree-1 representative, every other nonzero class has exactly one
        of degree 2, and the trivial class's degree-2 affine members are
        exactly the fibres of x and x + 1.
    (e) THE CLASS-BLIND DEGENERACY CONTROL: the same engine run on a copy of
        the ring with every class set to 0 must reproduce the IDEAL engine
        row for row, or the class group's effects below are partly the
        element code path.
    (f) The door brute: at every state whose cost is within the scan cap, a
        full enumeration of effective divisors, both worlds (PR1).
    If the control fails nothing below is read.
 S2 THE GEOGRAPHY: places by degree and by class, the minimal
    representatives, and the least degree at which two places share a class
    -- the only degree at which an element-world within-type tie can live.
 S3 THE IDEAL WORLD: cold D-DYN from a seed battery. The sprawl (PR2), the
    door law and permanence at every state (PR1, PR4), and the tie census.
 S4 THE ELEMENT WORLD: the same battery. The completion structure asserted
    at every move (PR3), the sprawl again, and the readmission census (PR5).
 S5 LOCKSTEP: the tau certificate at every within-type tie (PR6), the
    coarse-type gap census (PR7), and branch signature sequences compared to
    the horizon. The branch enumeration is bounded BY DESIGN and not by a
    cap the run might hit -- the first SPLITS within-type openings, the
    first `width` members of each, T_LS moves -- so there is nothing to
    truncate; what the bound costs is stated as the finding's scope, since a
    narrow enumeration that finds nothing is weak evidence and must read as
    such. The certificate has no such bound and is the load-bearing half.
 S6 THE FIVE-RING TABLE: what genus does to the formula and to the gap.

Run: `python explore_greedy_image_g2.py`. RUN RECORD (54190 checks, ~1.4 s).
S1 control: lam_pp met the exponent of 9 FULL unit groups computed element by
element; 28 point and closed-point counts exact against the zeta function and
Moebius at degrees 1..14, with #Jac = 15 agreeing between the zeta function
and the reduced-Mumford enumeration; 3615 class-group checks (bijective
action, commutativity, associativity) and 8 fibres of irreducible u(x) all of
class 0 and degree 2*deg(u), which is the principality control; the
Riemann-Roch census exact -- 15 classes, 1 trivial at degree 0, 4 at degree 1,
10 at degree 2, every one of them UNIQUE, and the trivial class's two affine
members of |K| the fibres of x and x + 1; the class-blind degeneracy control
identical move for move at 8 seeds over 8 moves, so every difference below is
the class group and not the element code path; 990 states brute-scanned
against a full divisor enumeration, 186 above the degree-8 cap. S2 geography:
places of degree 1..8 = [4, 2, 0, 2, 4, 12, 20, 22], 4 affine rational points,
minimal representatives 1/4/10 at degrees 0/1/2, 6 places able to ever ride at
degrees 1 and 2, least degree with two places of one class 6, and 0 riders
inside a repeated (degree, class) group. S3 ideal world, 45 seeds x 12 moves:
no lock, cost max 11, 477 tie states of which 128 cross-type, largest
within-type width 180, 0 of 9040 starved declines readmitted. S4 element
world, same battery: 588 moves completion-checked with no violation, cost max
11, 385 tie states of which 216 cross-type, largest within-type width 8, and
16 of 786 starved declines readmitted -- all of degree 1, each its own
seating, worst trajectory losing 3 openings, and all 6 ridable places seated
from the void by the horizon. S5 lockstep: 2533 lemma-G certificates at
visited ties (8211 further members left uncertified by the per-type cap of 6),
0 disagreeing seeds of 17 with content in both worlds over 120 branches
(branching capped by design at the first 2 within-type openings, 4 members
each, 8 moves), and
the coarse-type gap 0 of 919 tie states -- with all 1550 element tie members
at offset 0, so that zero is vacuous and is reported as such. Audit: 1176
states visited, 919 tie states with multiplicities from 2 to 180, 363 of them
straddling two degrees, 16464 door exponents searched and matched against
lemma A, 3673 permanence checks. Slate PR1-PR8: PR1-PR6 hit, no misses; PR7
was frozen as an open observable and printed a zero its own mechanism never
reached, which is a miss of the OBSERVATION and not of the prediction, and F6
scores it that way. Unfrozen finds: that the canonical multiplicity lands on
the trivial class and so cannot reach the rider (F2), a THIRD shape for a
degree-2 completion where PR3 named two -- a doubled rational point beside a
pair of distinct ones (F3) -- and that the bare-door case of lemma H is
provable rather than merely observed, which is what makes the vacuous zero
still worth something (F6).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

CHECKS = 0

DMAX = 14          # greatest place degree the universe carries
T_RUN = 12         # moves per deterministic trajectory
T_LS = 8           # moves per branch in the lockstep enumeration
SPLITS = 2         # openings the lockstep enumeration branches at
LOCK_R = 6         # repeated vehicles that would witness a lock
SCAN_DEG = 8       # greatest vehicle degree the brute scan enumerates
CERT_PAIRS = 6     # tie members certified against the first, per type, per state
OFF_CAP = 60       # tie members the offset census reads, per state
SEED_DEG = 3       # seeds are the void + every effective divisor to this degree

CURVE_F = 0b100010     # f = x^5 + x
CURVE_H = 0b1          # h = 1


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


# --------------------------------------------------- F_2[x] on int encodings
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


def pdivmod(a, b):
    q, db = 0, pdeg(b)
    while a and pdeg(a) >= db:
        sh = pdeg(a) - db
        q ^= 1 << sh
        a ^= b << sh
    return q, a


def pmod(a, b):
    return pdivmod(a, b)[1]


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


def pxgcd(a, b):
    """(g, s, t) with s*a + t*b = g."""
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1:
        q, r = pdivmod(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, s0 ^ pmul(q, s1)
        t0, t1 = t1, t0 ^ pmul(q, t1)
    return r0, s0, t0


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
    m, ps, p = d, [], 2
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


_IRR = {}


def irr_of_degree(d):
    if d not in _IRR:
        _IRR[d] = [f for f in range(1 << d, 2 << d) if is_irr(f)]
    return _IRR[d]


class Field(object):
    """F_2[X]/(u) for irreducible u, with the Artin-Schreier solver."""

    def __init__(self, u):
        self.u = u
        self.d = pdeg(u)
        self.n = 1 << self.d
        self.piv = {}
        for i in range(self.d):
            v = self.mul(1 << i, 1 << i) ^ (1 << i)
            comb = 1 << i
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
        return pmod(pmul(a, b), self.u)

    def inv(self, a):
        g, s, _ = pxgcd(a, self.u)
        assert g == 1, "inverse of a non-unit"
        return pmod(s, self.u)

    def sqrt(self, a):
        for _ in range(self.d - 1):
            a = self.mul(a, a)
        return a

    def evalp(self, p, x):
        r = 0
        for i in range(pdeg(p), -1, -1):
            r = self.mul(r, x)
            if (p >> i) & 1:
                r ^= 1
        return r

    def solve_as(self, w):
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


# ------------------------------------------------ the curve and its Jacobian
def fibre_ys(F, x):
    """The y's over x in F: two (split), one (ramified) or none (inert)."""
    b = F.evalp(CURVE_H, x)
    c = F.evalp(CURVE_F, x)
    if b == 0:
        return [F.sqrt(c)]
    z = F.solve_as(F.mul(c, F.inv(F.mul(b, b))))
    if z is None:
        return []
    return [F.mul(b, z), F.mul(b, z ^ 1)]


def npoints(m):
    """#C(F_{2^m}), the point at infinity included."""
    F = Field(irr_of_degree(m)[0])
    return 1 + sum(len(fibre_ys(F, x)) for x in range(F.n))


def reduce_div(D, g=2):
    """Cantor reduction to deg u <= g. Over F_2 every polynomial is monic."""
    u, v = D
    while pdeg(u) > g:
        un = pdivmod(CURVE_F ^ pmul(v, CURVE_H) ^ pmul(v, v), u)[0]
        vn = pmod(CURVE_H ^ v, un)
        u, v = un, vn
    return (u, v)


def cantor(D1, D2, g=2):
    """Composition then reduction: the group law on Pic^0."""
    u1, v1 = D1
    u2, v2 = D2
    d0, e1, e2 = pxgcd(u1, u2)
    d, c1, c2 = pxgcd(d0, v1 ^ v2 ^ CURVE_H)
    s1, s2, s3 = pmul(c1, e1), pmul(c1, e2), c2
    u = pdivmod(pmul(u1, u2), pmul(d, d))[0]
    num = (pmul(s1, pmul(u1, v2)) ^ pmul(s2, pmul(u2, v1))
           ^ pmul(s3, pmul(v1, v2) ^ CURVE_F))
    v = pmod(pdivmod(num, d)[0], u)
    return reduce_div((u, v), g)


def reduced_classes():
    """The unique reduced Mumford representative of every class of Pic^0."""
    out = []
    for u in range(1, 8):
        du = pdeg(u)
        for v in range(1 << du if du else 1):
            if pmod(pmul(v, v) ^ pmul(v, CURVE_H) ^ CURVE_F, u) == 0:
                out.append((u, v))
    return out


# ------------------------------------------------------------------ the ring
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
        self.minrep = {}      # class -> the unique minimal effective divisor
        self.addc = None
        self.negc = None

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
        """The canonical tie-break: least degree, then least place keys."""
        return (self.veh_deg(veh),
                tuple(sorted((self.deg[pl], pl, e) for pl, e in veh.items())))

    # --------------------------------------------------------- the pump
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


def build_ring(dmax):
    """Places = closed affine points; classes = Jac(F_2) by Cantor."""
    cl = reduced_classes()
    hh = len(cl)
    R = Ring("g2", hh)
    R.classes = cl
    idx = dict((c, i) for i, c in enumerate(cl))
    R.addc = [[idx[cantor(cl[i], cl[j])] for j in range(hh)]
              for i in range(hh)]
    ok(R.addc[idx[(1, 0)]] == list(range(hh)),
       "the empty divisor is not the class identity")
    ok(idx[(1, 0)] == 0, "the identity is not class 0")
    R.negc = [next(j for j in range(hh) if R.addc[i][j] == 0) for i in range(hh)]
    for d in range(1, dmax + 1):
        R.by_deg[d] = []
    for m in range(1, dmax + 1):
        for u in irr_of_degree(m):
            F = Field(u)
            x0 = pmod(2, u)               # the image of X, uniform in m
            ys = fibre_ys(F, x0)
            if ys:
                for y in ys:
                    pl = (m, u, y)
                    R.deg[pl] = m
                    R.cls[pl] = idx[reduce_div((u, y))]
                    R.by_deg[m].append(pl)
            elif 2 * m <= dmax:
                # the fibre is one closed point of degree 2m, and it is the
                # divisor of u(x): principal, hence of trivial class
                pl = (2 * m, u, None)
                R.deg[pl] = 2 * m
                R.cls[pl] = 0
                R.by_deg[2 * m].append(pl)
    for d in range(1, dmax + 1):
        R.by_deg[d].sort()
    return R


def minimal_reps(R, maxdeg=3):
    """Every minimal-degree effective affine divisor of each class."""
    reps = {0: (0, [{}])}
    pls = [pl for d in range(1, maxdeg + 1) for pl in R.by_deg[d]]

    def rec(i, cur, dg):
        if cur:
            c = R.veh_class(cur)
            best = reps.get(c)
            if best is None or dg < best[0]:
                reps[c] = (dg, [dict(cur)])
            elif dg == best[0]:
                best[1].append(dict(cur))
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
    return reps


def trivialised(R):
    """A copy of the ring with every class 0: the degeneracy control."""
    T = Ring("class-blind", 1)
    T.classes = [(1, 0)]
    T.addc = [[0]]
    T.negc = [0]
    T.deg = dict(R.deg)
    T.cls = dict((pl, 0) for pl in R.cls)
    T.by_deg = dict((d, list(v)) for d, v in R.by_deg.items())
    T.minrep = {0: {}}
    return T


# --------------------------------------------------------------- the menus
def complete(R, pl, r):
    """The core P^r plus the unique minimal representative of the class it
    must cancel (lemma D). The representative may share the core's place, in
    which case the exponents merge."""
    veh = {pl: r}
    c = R.veh_class(veh)
    if c:
        for q, e in R.minrep[R.neg_class(c)].items():
            veh[q] = veh.get(q, 0) + e
    return veh


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
       "the ideal door reached degree %s, past the universe" % best)
    ties.sort(key=R.veh_key)
    return best, ties


def elem_menu(R, st, L):
    """(degree, [vehicle]) in the PRINCIPAL world. Lemma D: every minimal
    vehicle is a core P^n plus minrep of the class it must cancel, with
    n in {r, r+1, r+2} -- a completion saves at most 2 and an extra
    exponent costs at least 1 per unit of degree."""
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
                for j in (0, 1, 2):
                    entries.append((groups[c], r0 + j))
        for pl in st:
            if st[pl] and R.deg[pl] == d:
                r0 = R.door_r(pl, st[pl], L)
                for j in (0, 1, 2):
                    entries.append(([pl], r0 + j))
        for group, r in entries:
            # cost is uniform inside a (degree, class) group, so it is priced
            # once and the group materialised only while it is competitive
            if best is not None and R.veh_deg(complete(R, group[0], r)) > best:
                continue
            for pl in group:
                offer(complete(R, pl, r))
    ok(best is not None and best <= DMAX,
       "the element door reached degree %s, past the universe" % best)
    for veh in ties:
        ok(R.veh_class(veh) == 0, "a non-principal element vehicle")
    ties.sort(key=R.veh_key)
    return best, ties


MENUS = {"ideal": ideal_menu, "element": elem_menu}


def fmt_state(R, st):
    parts = ["P%d.%d^%d" % (R.deg[pl], R.by_deg[R.deg[pl]].index(pl), e)
             for pl, e in sorted(st.items(), key=lambda kv: R.deg[kv[0]]) if e]
    return "*".join(parts) if parts else "(1)"


# ----------------------------------------------------------- the brute scan
_DIVS = {}


def all_divisors(R, maxdeg):
    """Every effective divisor of degree 1..maxdeg, as (divisor, degree,
    class). Degree and class are cached here because the brute scan reads
    the whole list once per scanned state."""
    key = (R.name, maxdeg)
    if key in _DIVS:
        return _DIVS[key]
    pls = [pl for d in range(1, maxdeg + 1) for pl in R.by_deg[d]]
    out = []

    def rec(i, cur, dg):
        if cur:
            out.append((dict(cur), dg, R.veh_class(cur)))
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
    out.sort(key=lambda t: t[1])
    _DIVS[key] = out
    return out


def scan_check(R, world, st, L, cost, ties):
    """PR1 at one state: nothing cheaper ticks, and the min-degree tickers are
    exactly the menu's ties."""
    at_cost = []
    for veh, dg, vc in all_divisors(R, cost):
        if world == "element" and vc != 0:
            continue
        L2 = L
        for pl, e in veh.items():
            L2 = lcm(L2, R.lam_pp(R.deg[pl], st.get(pl, 0) + e))
        if L2 <= L:
            continue
        ok(dg >= cost, "%s: a degree-%d divisor ticks below the door %d"
           % (world, dg, cost))
        if dg == cost:
            at_cost.append(veh)
    got = sorted(tuple(sorted(v.items())) for v in at_cost)
    want = sorted(tuple(sorted(v.items())) for v in ties)
    ok(got == want, "%s: scan ties != menu ties at cost %d (%d vs %d)"
       % (world, cost, len(got), len(want)))
    if world == "ideal":
        for veh in at_cost:
            ok(len(veh) == 1,
               "a minimal ideal move is not a single-place power")


# ------------------------------------------------------------ trajectories
def apply_veh(st, veh):
    out = dict(st)
    for pl, e in veh.items():
        out[pl] = out.get(pl, 0) + e
    return out


def vkey(veh):
    return tuple(sorted(veh.items()))


def core_of(R, st, veh, L):
    """The place whose power actually raises lambda. With a degree-2 rider
    the heaviest term is no longer always the core, so it is found by the
    tick and not by the weight. The tie-break reads only (degree, exponent,
    depth) -- never the place key -- so that it commutes with lemma G's
    colour-preserving permutations; two places attaining the maximum share
    all three and so share a kind."""
    cands = [pl for pl, e in veh.items()
             if L % R.lam_pp(R.deg[pl], st.get(pl, 0) + e) != 0]
    ok(bool(cands), "no place in the vehicle raises lambda")
    return max(cands, key=lambda pl: (R.deg[pl] * veh[pl], R.deg[pl],
                                      veh[pl], st.get(pl, 0)))


def offset_of(R, st, veh, L):
    """The least j such that the vehicle is complete(core, door + j) for some
    place in it, or None. j > 0 is the ONLY route to lemma H's coarse-type
    collision, so how often it appears among tie MEMBERS -- not merely among
    chosen moves -- is what decides whether PR7's observable was exercised."""
    for j in (0, 1, 2):
        for pl in veh:
            r0 = R.door_r(pl, st.get(pl, 0), L)
            if vkey(complete(R, pl, r0 + j)) == vkey(veh):
                return j
    return None


def sig_of(R, st, veh, cost, L):
    """The move's signature: what lockstep says is branch-independent --
    cost, kind, and the (degree, exponent) multiset of the vehicle."""
    core = core_of(R, st, veh, L)
    k = R.kind(st.get(core, 0), veh[core])
    return (cost, k, tuple(sorted((R.deg[pl], e) for pl, e in veh.items())))


def veh_type(R, world, st, veh, refined):
    """What the ENGINE can read about a vehicle. lambda reads (degree,
    depth); the element world reads one further datum, the CLASS, through
    the principality test and the completion. The REFINED type carries the
    state depth as well -- lemma G's colouring -- and the coarse one does
    not, which is the gap PR7 measures."""
    out = []
    for pl, e in veh.items():
        c = R.cls[pl] if world == "element" else -1
        out.append((R.deg[pl], c, e) + ((st.get(pl, 0),) if refined else ()))
    return tuple(sorted(out))


class Audit(object):
    def __init__(self):
        self.states = 0
        self.scanned = 0
        self.scan_skipped = 0
        self.tie_states = 0
        self.tie_sizes = {}
        self.tie_multideg = 0
        self.coarse_gap = 0
        self.coarse_gap_at = []
        self.starve = 0
        self.starve_bad = []
        self.doors = 0
        self.door_bad = []
        self.riders = 0
        self.rider_bad = []
        self.rider_degs = {}
        self.rider_shapes = set()
        self.offsets = {}
        self.mem_offsets = {}
        self.off_skipped = 0
        self.certs = 0
        self.cert_skipped = 0

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
            # PR7, lemma H: a coarse type holding two different refined ones
            # is a branching lemma G does not cover.
            byc = {}
            for veh in ties:
                byc.setdefault(veh_type(R, world, st, veh, False),
                               set()).add(veh_type(R, world, st, veh, True))
            if world == "element":
                for veh in ties[:OFF_CAP]:
                    j = offset_of(R, st, veh, L)
                    self.mem_offsets[j] = self.mem_offsets.get(j, 0) + 1
                self.off_skipped += max(0, len(ties) - OFF_CAP)
            if any(len(s) > 1 for s in byc.values()):
                self.coarse_gap += 1
                if len(self.coarse_gap_at) < 3:
                    self.coarse_gap_at.append((world, fmt_state(R, st), cost))
            # PR6, lemma G certified at EVERY within-type tie the engine
            # meets, not only at the ones the branch enumeration reaches.
            # The per-group cap is stated rather than silent.
            byr = {}
            for veh in ties:
                byr.setdefault(veh_type(R, world, st, veh, True),
                               []).append(veh)
            for grp in byr.values():
                if len(grp) < 2:
                    continue
                for other in grp[1:CERT_PAIRS + 1]:
                    pairs = tau_certificate(R, world, st, grp[0], other)
                    ok(pairs is not None,
                       "a within-type tie with no colour-preserving tau")
                    check_tau(R, world, st, pairs, grp[0], other)
                    self.certs += 1
                self.cert_skipped += max(0, len(grp) - 1 - CERT_PAIRS)
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
                    self.door_bad.append((d, e, c, got, want))
        # PR4, lemma C: an unseated place's door strictly exceeds every
        # seated same-degree place's door.
        for d in range(1, DMAX + 1):
            seated = [pl for pl in R.by_deg[d] if st.get(pl, 0) > 0]
            unse = [pl for pl in R.by_deg[d] if st.get(pl, 0) == 0]
            if not seated or not unse:
                continue
            worst = max(R.door_r(pl, st[pl], L) for pl in seated)
            fresh = R.door_r(unse[0], 0, L)
            self.starve += 1
            if not fresh > worst:
                self.starve_bad.append((world, d, worst, fresh))

    def rider_check(self, R, st, veh, ideal_cost, L):
        """PR3 / lemma D: the vehicle IS some core P^n, n in {r, r+1, r+2},
        plus the unique minimal representative of the class it cancels. The
        check reconstructs the vehicle rather than inspecting it, so a
        vehicle of any other shape fails outright."""
        self.riders += 1
        cost = R.veh_deg(veh)
        if cost > ideal_cost + 2:
            self.rider_bad.append(("cost", cost, ideal_cost))
            return
        hit = None
        for j in (0, 1, 2):
            for pl in veh:
                r0 = R.door_r(pl, st.get(pl, 0), L)
                if vkey(complete(R, pl, r0 + j)) == vkey(veh):
                    hit = (pl, r0 + j, j)
                    break
            if hit:
                break
        if hit is None:
            self.rider_bad.append(("completion", vkey(veh)))
            return
        pl, n, j = hit
        # THE OFFSET CENSUS. PR7's observable can only be reached through a
        # core exponent above the bare door, so how often an offset WINS is
        # what decides whether a zero there is informative or vacuous.
        self.offsets[j] = self.offsets.get(j, 0) + 1
        rest = dict(veh)
        rest[pl] -= n
        if not rest[pl]:
            del rest[pl]
        dg = R.veh_deg(rest)
        self.rider_degs[dg] = self.rider_degs.get(dg, 0) + 1
        if dg:
            # the SUPPORT SIZE is part of the shape: a doubled rational point
            # and a pair of distinct ones are both degree 2 over degree-1
            # places, and they are different divisors
            self.rider_shapes.add(
                (tuple(sorted(R.deg[q] for q, e in rest.items()
                              for _ in range(e))), len(rest)))


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
            audit.rider_check(R, st, veh, icost, L)
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
        bytype = {}
        for other in ties:
            bytype.setdefault(veh_type(R, world, st, other, True),
                              []).append(other)
        log.append({"cost": cost, "veh": veh, "nties": len(ties),
                    "ntypes": len(bytype),
                    "maxtype": max(len(g) for g in bytype.values()),
                    "sig": sig_of(R, st, veh, cost, L), "declined": declined,
                    "state": st})
        st = st2
        L2 = R.lam_state(st)
        ok(L2 > L, "%s: the chosen move does not raise lambda" % world)
        L = L2
    return log


def readmission(R, log):
    """Per DECLINED PLACE, split by whether the move starved it: is it seated
    later in the same branch?"""
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
                        first = (i, d, i + back + 1,
                                 dict(log[i + back + 1]["veh"]))
            else:
                nf += 1
                nfb += (back is not None)
    return ns, nsb, nf, nfb, first, degs, when


def seating_moves(R, log, places):
    """For each named place, the move that first seats it, or None. Depths
    never fall, so a place is seated at most ONCE -- the step that turns a
    finite set of possible victims into a finite number of failed openings."""
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
    return [{}] + [dict(v) for v, _, _ in all_divisors(R, maxdeg)]


# -------------------------------------------------------------- S1 control
def polysq(F, u, a):
    out = [0] * a
    for i in range(a):
        if 2 * i < a:
            out[2 * i] ^= F.mul(u[i], u[i])
    return out


def polymul(F, u, v, a):
    out = [0] * a
    for i in range(a):
        if not u[i]:
            continue
        for j in range(a - i):
            out[i + j] ^= F.mul(u[i], v[j])
    return out


def s1a_unit_law(R):
    print("  (a) the equal-characteristic 1-unit law: lam_pp against the")
    print("      exponent of FULL unit groups of F_{2^d}[t]/(t^a), computed")
    print("      element by element -- the check that does not restate the")
    print("      law's own shape")
    m = 0
    for d, amax in ((1, 4), (2, 3), (3, 2)):
        F = Field(irr_of_degree(d)[0])
        for a in range(1, amax + 1):
            expo = 1
            for code in range(F.n ** a):
                c, u = code, []
                for _ in range(a):
                    u.append(c % F.n)
                    c //= F.n
                if u[0] == 0:
                    continue
                k, w = 1, list(u)
                one = [1] + [0] * (a - 1)
                while w != one:
                    w = polymul(F, w, u, a)
                    k += 1
                    assert k <= F.n ** a, "unit order runaway"
                expo = lcm(expo, k)
            ok(expo == R.lam_pp(d, a),
               "the unit-group exponent of F_%d[t]/(t^%d) is %d, the law says"
               " %d" % (F.n, a, expo, R.lam_pp(d, a)))
            m += 1
    print("      %d full unit groups: lam_pp is the ring's own lambda." % m)


def s1b_curve(R):
    print("\n  (b) the curve arithmetic: direct point counts over F_{2^d}")
    print("      against the zeta function, and closed points against Moebius")
    n1, n2 = npoints(1), npoints(2)
    # the Frobenius eigenvalues' elementary symmetric functions, from N_1 and
    # N_2 alone; the functional equation fixes e_3 = q*e_1 and e_4 = q^2
    e1 = 3 - n1
    e2 = (e1 * e1 - (5 - n2)) // 2
    e3, e4 = 2 * e1, 4
    # Newton's identities: the first four carry the extra k*e_k term, and
    # from k = 5 the plain recurrence holds
    s = [4, e1]
    s.append(e1 * s[1] - 2 * e2)
    s.append(e1 * s[2] - e2 * s[1] + 3 * e3)
    s.append(e1 * s[3] - e2 * s[2] + e3 * s[1] - 4 * e4)
    for i in range(5, DMAX + 1):
        s.append(e1 * s[i - 1] - e2 * s[i - 2] + e3 * s[i - 3] - e4 * s[i - 4])
    N = [None] + [(1 << d) + 1 - s[d] for d in range(1, DMAX + 1)]
    cnt = 0
    for d in range(1, DMAX + 1):
        ok(npoints(d) == N[d],
           "#C(F_2^%d) = %d, the zeta function says %d" % (d, npoints(d), N[d]))
        want = sum(mobius(d // e) * N[e] for e in range(1, d + 1)
                   if d % e == 0) // d
        got = len(R.by_deg[d]) + (1 if d == 1 else 0)
        ok(got == want, "%d closed points of degree %d, Moebius says %d"
           % (got, d, want))
        cnt += 2
    print("      %d counts, all exact, degrees 1..%d. N_1 = %d, N_2 = %d,"
          % (cnt, DMAX, n1, n2))
    print("      #Jac(F_2) = P(1) = %d." % (5 - 3 * e1 + e2))
    ok(5 - 3 * e1 + e2 == R.h,
       "the zeta function says #Jac = %d, the Mumford enumeration says %d"
       % (5 - 3 * e1 + e2, R.h))
    return n1


def s1c_class_group(R):
    print("\n  (c) the class group: the reduced-Mumford enumeration counts")
    print("      P(1) exactly (asserted above), Cantor makes it an abelian")
    print("      group, and every principal fibre has class 0")
    ng = 0
    for i in range(R.h):
        ok(sorted(R.addc[i]) == list(range(R.h)), "class %d does not act "
           "bijectively" % i)
        ng += 1
        for j in range(R.h):
            ok(R.addc[i][j] == R.addc[j][i], "the class group is not abelian")
            ng += 1
            for k in range(R.h):
                ok(R.addc[R.addc[i][j]][k] == R.addc[i][R.addc[j][k]],
                   "the class group is not associative")
                ng += 1
    # the fibre of an irreducible u(x) is div(u) + 2*deg(u)*O: principal, so
    # its places sum to the trivial class and to degree 2*deg(u)
    nf = 0
    for m in range(1, 5):
        for u in irr_of_degree(m):
            tot, dg = 0, 0
            for pl in [p for d in range(1, DMAX + 1) for p in R.by_deg[d]
                       if p[1] == u]:
                mult = 2 if _ramified(pl) else 1
                for _ in range(mult):
                    tot = R.add_class(tot, R.cls[pl])
                dg += R.deg[pl] * mult
            ok(tot == 0, "the fibre over %s has class %d, not 0" % (bin(u), tot))
            ok(dg == 2 * m, "the fibre over %s has degree %d, not %d"
               % (bin(u), dg, 2 * m))
            nf += 1
    print("      %d group checks, and %d fibres of irreducible u(x) all of"
          % (ng, nf))
    print("      class 0 and degree 2*deg(u), as div(u) requires.")


def _ramified(pl):
    """A place whose fibre is 2P: the only y over its x. An inert place is
    the whole fibre already and so counts once."""
    if pl[2] is None:
        return False
    return len(fibre_ys(Field(pl[1]), pmod(2, pl[1]))) == 1


def s1d_riemann_roch(R, n1, reps):
    print("\n  (d) the Riemann-Roch census: minimal affine representatives")
    print("      per class, against the desk prediction")
    ok(set(reps) == set(range(R.h)), "some class has no representative in "
       "range")
    for c in range(R.h):
        dg, rs = reps[c]
        ok(len(rs) == 1,
           "class %d has %d minimal representatives, Riemann-Roch says 1"
           % (c, len(rs)))
        ok(dg <= 2, "class %d needs degree %d" % (c, dg))
    d1 = sum(1 for c in range(R.h) if reps[c][0] == 1)
    d2 = sum(1 for c in range(R.h) if reps[c][0] == 2)
    ok(d1 == n1 - 1, "%d classes have a degree-1 representative, the %d "
       "affine rational points say %d" % (d1, n1 - 1, n1 - 1))
    ok(d1 + d2 + 1 == R.h, "the census does not cover the class group")
    # the trivial class's degree-2 affine members: |K| minus 2O
    triv = [D for D, dg, vc in all_divisors(R, 2) if dg == 2 and vc == 0]
    ok(len(triv) == 2, "the trivial class has %d affine divisors of degree 2, "
       "|K| minus 2O says 2" % len(triv))
    for D in triv:
        us = set(pl[1] for pl in D)
        ok(len(us) == 1 and pdeg(list(us)[0]) == 1,
           "a trivial-class degree-2 divisor is not a fibre of x - a")
    print("      %d classes: 1 trivial (degree 0), %d of degree 1, %d of"
          % (R.h, d1, d2))
    print("      degree 2 -- every one of them UNIQUE, as Riemann-Roch")
    print("      requires, the canonical multiplicity landing on the trivial")
    print("      class where it summons nothing. The trivial class's two")
    print("      affine members of |K| are the fibres of x and x + 1.")


def s1e_degeneracy(R):
    print("\n  (e) the class-blind degeneracy control: with every class set")
    print("      to 0 the element engine must reproduce the ideal one")
    T = trivialised(R)
    n = 0
    for seed in seeds_of(R, 2)[:8]:
        a = run(R, "ideal", seed, 8)
        b = run(T, "element", seed, 8)
        ok([vkey(m["veh"]) for m in a] == [vkey(m["veh"]) for m in b],
           "the element engine does not degenerate to the ideal one when the "
           "class group is trivial")
        n += 1
    print("      %d seeds, %d moves each, identical move for move." % (n, 8))


def s1f_scan(R, audit):
    print("\n  (f) the door brute: every state below the scan cap, both")
    print("      worlds, checked against a full enumeration of divisors")
    for world in ("ideal", "element"):
        for seed in seeds_of(R, 2)[:8]:
            run(R, world, seed, 6, audit=audit)
    print("      %d states scanned, %d above the degree-%d cap."
          % (audit.scanned, audit.scan_skipped, SCAN_DEG))
    ok(audit.scanned > 0, "the menu was never brute-scanned")
    ok(not audit.starve_bad, "PR4 failed at %s" % audit.starve_bad[:3])
    ok(not audit.rider_bad, "PR3 failed at %s" % audit.rider_bad[:3])


# ---------------------------------------------------------- S2 geography
def s2_geography(R, reps):
    section("S2  THE GEOGRAPHY -- genus 2 over F_2, one dial from the fourth "
            "cell")
    print("  Places by degree, the class map's fibres, and the minimal")
    print("  representatives -- the only divisors a completion can ever be.")
    print("  The number that decides whether lockstep has room is the least")
    print("  degree at which TWO places share a class: below it, no")
    print("  element-world within-type tie exists at all.\n")
    row = [len(R.by_deg[d]) for d in range(1, 9)]
    print("  places of degree 1..8:      %s" % row)
    print("  affine rational points:     %d" % len(R.by_deg[1]))
    print("  class number:               %d" % R.h)
    byd = {}
    for c in range(R.h):
        byd[reps[c][0]] = byd.get(reps[c][0], 0) + 1
    print("  minimal reps by degree:     %s" % dict(sorted(byd.items())))
    sup = set()
    for c in range(R.h):
        sup.update(reps[c][1][0])
    print("  places that can ever ride:  %d, of degrees %s"
          % (len(sup), sorted(set(R.deg[pl] for pl in sup))))
    grp = {}
    for d in range(1, DMAX + 1):
        for pl in R.by_deg[d]:
            grp.setdefault((d, R.cls[pl]), []).append(pl)
    rep_deg = sorted(d for (d, c), v in grp.items() if len(v) > 1)
    print("  least degree with two places of one class: %s"
          % (rep_deg[0] if rep_deg else "none"))
    clash = [pl for pl in sup if len(grp[(R.deg[pl], R.cls[pl])]) > 1]
    print("  riders inside a repeated (degree, class) group: %d" % len(clash))
    ok(not clash,
       "a rider shares its (degree, class) with another place: %s" % clash[:2])
    return sup


# -------------------------------------------------------- S3/S4 the worlds
def run_world(R, world, audit, sup):
    section("S%s  THE %s WORLD -- cold D-DYN, %d moves, seeds to degree %d"
            % ("3" if world == "ideal" else "4", world.upper(), T_RUN,
               SEED_DEG))
    if world == "element":
        print("  Moves are PRINCIPAL. Lemma D says every one of them is an")
        print("  ideal core plus the UNIQUE minimal representative of the")
        print("  class it must cancel -- of degree 0, 1 or 2, which is what")
        print("  genus 2 changes. Asserted at every move (PR3).\n")
    else:
        print("  Lemma C says a declined member can never come back: an")
        print("  unseated place is CLOCKED where a seated one deepens, and")
        print("  the clocked door is strictly dearer -- asserted at every")
        print("  visited state (PR4).\n")
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
        if when:
            seats = seating_moves(R, log, set(pl for _, _, pl in when))
            for _, backmv, pl in when:
                ok(seats[pl] == backmv,
                   "%s: a readmission at move %d is not that place's own "
                   "seating (seated at %s) -- the seated-once step does not "
                   "hold" % (world, backmv + 1, seats[pl]))
                lastback = max(lastback, backmv)
            ok(len(set(pl for _, _, pl in when)) <= len(sup),
               "%s: %d distinct places readmitted, above the %d in the "
               "minimal-representative support"
               % (world, len(set(pl for _, _, pl in when)), len(sup)))
            prefix = max(prefix, len(when))
        if b and first_readm is None:
            first_readm = (R.veh_deg(seed) if seed else 0, fi, dict(seed))
        tv = set(vkey(mv["veh"]) for mv in log[-LOCK_R:])
        tails.add(len(tv))
        ok(len(tv) > 1, "PR2: %s locked -- the last %d moves are one vehicle"
           % (world, LOCK_R))
    print("  seeds %d, cost max %d, tie states %d, tail vehicles %d..%d"
          % (len(seeds), cmax, ties, min(tails), max(tails)))
    print("  starved declines %d, of which back %d; free declines %d, back %d"
          % (ns, nsb, nf, nfb))
    print("  tie states that are CROSS-type: %d; largest within-type width: %d"
          % (xtype, wmax))
    if world == "ideal":
        ok(nsb == 0, "PR4/lemma C: a STARVED decline came back in the ideal "
           "world")
        print("\n  0 starved declines came back: lemma C holds at the level")
        print("  of the IMAGE and not only of the door.")
    else:
        print("\n  READMISSION by the DEGREE of the place that came back --")
        print("  the number that decides whether the mechanism can scale:")
        print("    degrees %s" % (dict(sorted(rdegs.items())) or "none"))
        if nsb:
            mv, dd, back, veh = first_readm[1]
            print("    first: seed %s, declined at move %d, back at move %d"
                  % (fmt_state(R, first_readm[2]), mv + 1, back + 1))
            print("           in the vehicle %s" % fmt_state(R, veh))
            print("    last readmission at move %d; worst trajectory lost %d"
                  " openings" % (lastback + 1, prefix))
        ok(set(rdegs) <= {1, 2},
           "a readmitted place had degree > 2: %s -- lemma F's pricing is not "
           "what confines readmission" % sorted(rdegs))
        seated = 0
        log = run(R, "element", {}, T_RUN)
        st = apply_veh(log[-1]["state"], log[-1]["veh"])
        seated = sum(1 for pl in sup if st.get(pl, 0) > 0)
        print("    from the void, %d of the %d places that can ever ride are"
              % (seated, len(sup)))
        print("    seated by the horizon -- a place never seated is never")
        print("    readmitted either, the same bound from the other side.")
    return (len(seeds), cmax, ties, ns, nsb, nf, nfb, rdegs, lastback, prefix,
            xtype, wmax)


# ------------------------------------------------------------- S5 lockstep
def tau_certificate(R, world, st, v1, v2):
    """Lemma G, made explicit: a permutation of places preserving the world's
    colouring, fixing the state, and carrying v1 to v2. Returns the
    transposition list, or None if no colour-preserving matching exists. The
    ideal world does not read the class, so its colour is (degree, depth)
    alone and the matching is correspondingly freer."""
    if veh_type(R, world, st, v1, True) != veh_type(R, world, st, v2, True):
        return None
    left = dict(v1)
    right = dict(v2)
    for pl in list(left):
        if right.get(pl) == left[pl]:
            del left[pl]
            del right[pl]
    pairs = []
    for pl, e in sorted(left.items()):
        match = None
        for q, e2 in sorted(right.items()):
            if e2 == e and R.deg[q] == R.deg[pl] \
                    and (world == "ideal" or R.cls[q] == R.cls[pl]) \
                    and st.get(q, 0) == st.get(pl, 0):
                match = q
                break
        if match is None:
            return None
        del right[match]
        pairs.append((pl, match))
    return pairs if not right else None


def check_tau(R, world, st, pairs, v1, v2):
    """The certificate's obligations, all four: the map is a BIJECTION, it
    CARRIES v1 to v2, it preserves the world's colouring and fixes the state,
    and -- in the element world -- it fixes EVERY minimal representative
    setwise, which is the step genus could have broken. The carrying is the
    headline and so is checked rather than trusted to the matching that
    built the pairs; without it the other three can all hold of a map that
    does not do the one thing lemma G needs."""
    perm = {}
    for a, b in pairs:
        # a matching that sent two places to one would satisfy every
        # colour test below and still not be a permutation
        ok(perm.get(a, b) == b and perm.get(b, a) == a,
           "the tau matching is not a bijection")
        perm[a] = b
        perm[b] = a
    ok(len(set(perm.values())) == len(perm), "tau is not injective")
    img = {}
    for pl, e in v1.items():
        img[perm.get(pl, pl)] = img.get(perm.get(pl, pl), 0) + e
    ok(vkey(img) == vkey(v2),
       "tau does not carry the tie member to the other: %s -> %s, wanted %s"
       % (vkey(v1), vkey(img), vkey(v2)))
    for a, b in perm.items():
        ok(R.deg[a] == R.deg[b], "tau does not preserve degree")
        ok(st.get(a, 0) == st.get(b, 0), "tau does not fix the state")
        if world == "element":
            ok(R.cls[a] == R.cls[b], "tau does not preserve class")
    if world == "ideal":
        return
    for c in range(R.h):
        D = R.minrep[c]
        img = dict((perm.get(pl, pl), e) for pl, e in D.items())
        ok(vkey(img) == vkey(D),
           "tau moves the minimal representative of class %d -- the rider is "
           "not colour-blind and lockstep has room to fail" % c)


def tie_reps(R, world, st, ties, width):
    """The members lockstep is ABOUT: the largest group of one REFINED type
    (degree, class, exponent, state depth). Choosing between two types is a
    different move and the sequences are expected to differ -- that is the
    reordering S3/S4 measures, not a lockstep failure."""
    by = {}
    for v in ties:
        by.setdefault(veh_type(R, world, st, v, True), []).append(v)
    big = max(by.values(), key=len)
    if len(big) < 2:
        return ties[:1], False
    return big[:width], True


def branches(R, world, seed, T, splits, width=4, cert=None):
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
            pick, real = tie_reps(R, world, st, ties, width)
        if real:
            taken = max(taken, spent + 1)
            if cert is not None:
                for other in pick[1:]:
                    pairs = tau_certificate(R, world, st, pick[0], other)
                    ok(pairs is not None,
                       "a within-type tie with no colour-preserving tau")
                    check_tau(R, world, st, pairs, pick[0], other)
                    cert[0] += 1
        for veh in pick:
            child = apply_veh(st, veh)
            stack.append((child, R.lam_state(child),
                          log + [sig_of(R, st, veh, cost, L)], used + 1,
                          spent + (1 if real else 0)))
    return out, taken


def s5_lockstep(R, reps, audit):
    section("S5  LOCKSTEP -- a theorem now, and the rig is its control")
    print("  Lemma G: everything the engine reads is a function of a place's")
    print("  (degree, class), so any permutation preserving those is an")
    print("  automorphism of the dynamics; two tie members of one REFINED")
    print("  type -- (degree, class, exponent, state depth) -- are carried")
    print("  one to the other by such a permutation that also fixes the")
    print("  state. The subtrees are then isomorphic and every later opening")
    print("  has the same multiplicity, so the count FACTORS.")
    print("  The rig certifies the permutation at every within-type tie and")
    print("  compares branch signature sequences to the horizon.\n")
    out = {}
    cert = [0]
    for world in ("ideal", "element"):
        seeds = seeds_of(R, 2)
        nb, bad, live, first = 0, 0, 0, None
        for seed in seeds:
            logs, taken = branches(R, world, seed, T_LS, SPLITS,
                                   cert=cert if world == "element" else None)
            nb += len(logs)
            live += (taken > 0)
            sigs = set(logs)
            if len(sigs) > 1:
                bad += 1
                if first is None:
                    a, b = sorted(sigs)[:2]
                    k = next(i for i in range(len(a)) if a[i] != b[i])
                    first = (k, a[k], b[k])
        out[world] = (live, nb, bad, first)
        print("  %-8s seeds with content %d/%d, branches %d, disagreeing %d %s"
              % (world, live, len(seeds), nb, bad,
                 "(first at move %d: %s vs %s)" % (first[0] + 1, first[1],
                                                   first[2]) if first else ""))
    for world in ("ideal", "element"):
        ok(out[world][2] == 0, "PR6: %s lockstep failed" % world)
    print("\n  %d within-type ties certified: at each one a permutation of" % cert[0])
    print("  places preserving degree and class, fixing the state, carrying")
    print("  one member to the other, and FIXING EVERY MINIMAL")
    print("  REPRESENTATIVE -- the last being the obligation genus 2 could")
    print("  have broken and does not.")
    print("\n  PR7, THE COARSE-TYPE GAP: tie states holding two members of")
    print("  one COARSE type (degree, class, exponent) at different core")
    print("  DEPTHS -- branchings lemma G does NOT cover, reachable only")
    print("  through the r+1 / r+2 offsets: %d of %d tie states."
          % (audit.coarse_gap, audit.tie_states))
    if audit.coarse_gap:
        print("  first at: %s" % (audit.coarse_gap_at,))
    return out


# ------------------------------------------------------------- S6 the table
def s6_table(R, ideal_out, elem_out, ls_out, sup, audit):
    section("S6  THE FIVE-RING TABLE -- what genus does to the formula")
    print("  MULTIPLICITY is the largest WITHIN-TYPE tie width, the only one")
    print("  an opening can survive, followed by how many tie states were")
    print("  CROSS-type -- those are reorderings. PERMANENCE is starved")
    print("  declines that came BACK. LOCKSTEP is seeds whose branches")
    print("  disagree.\n")
    print("  %-18s %-16s %-15s %-14s %s"
          % ("ring, world", "multiplicity", "openings", "permanence",
             "lockstep"))
    print("  %-18s %-16s %-15s %-14s %s"
          % ("Z", "1 (order)", "stop (lock)", "n/a", "n/a"))
    print("  %-18s %-16s %-15s %-14s %s"
          % ("number ring", "2 (Galois)", "stop (lock)", "holds", "holds"))
    print("  %-18s %-16s %-15s %-14s %s"
          % ("F_2[x]", "<= 335", "never (sprawl)", "0 back", "holds"))
    print("  %-18s %-16s %-15s %-14s %s"
          % ("elliptic (g=1)", "<= 1160", "never (sprawl)", "14 back",
             "holds"))
    for world, src in (("ideal", ideal_out), ("element", elem_out)):
        _, cmax, ties, ns, nsb, nf, nfb, rd, lb, px, xt, wm = src
        live, nb, bad, _ = ls_out[world]
        print("  %-18s %-16s %-15s %-14s %s"
              % ("genus 2, %s" % world, "<= %d, %d/%d cross" % (wm, xt, ties),
                 "never (sprawl)", "%d/%d back" % (nsb, ns),
                 "%d/%d seeds split" % (bad, live)))
    print("\n  The completion at genus 2, by degree: %s"
          % dict(sorted(audit.rider_degs.items())))
    print("  The shapes a degree-2 completion took: %s"
          % sorted(audit.rider_shapes))
    print("  Places that can ever ride: %d (genus 1 has h - 1, all rational)."
          % len(sup))


def main():
    section("S1  THE POSITIVE CONTROL -- run before any image is read")
    R = build_ring(DMAX)
    s1a_unit_law(R)
    n1 = s1b_curve(R)
    s1c_class_group(R)
    reps = minimal_reps(R)
    s1d_riemann_roch(R, n1, reps)
    for c in range(R.h):
        R.minrep[c] = reps[c][1][0]
    s1e_degeneracy(R)
    audit = Audit()
    s1f_scan(R, audit)
    print("\n  Control green.")
    sup = s2_geography(R, reps)
    ideal_out = run_world(R, "ideal", audit, sup)
    elem_out = run_world(R, "element", audit, sup)
    section("THE AUDIT -- every state the trajectories visited")
    print("  states visited:                  %d" % audit.states)
    print("  brute-scanned:                   %d (%d above the degree-%d cap)"
          % (audit.scanned, audit.scan_skipped, SCAN_DEG))
    print("  tie states:                      %d" % audit.tie_states)
    print("  tie multiplicities:              %s"
          % dict(sorted(audit.tie_sizes.items())))
    print("  tie sets straddling two degrees: %d" % audit.tie_multideg)
    print("  door exponents searched vs the closed form: %d" % audit.doors)
    print("  permanence checks (lemma C):     %d" % audit.starve)
    print("  element moves completion-checked: %d" % audit.riders)
    print("  core exponent offsets, CHOSEN moves (offset -> count): %s"
          % dict(sorted(audit.offsets.items())))
    print("  core exponent offsets, all element tie MEMBERS: %s (%d beyond"
          % (dict(sorted(audit.mem_offsets.items(), key=lambda kv: (kv[0] is
                                                                    None, kv[0]))),
             audit.off_skipped))
    print("  the per-state cap of %d)" % OFF_CAP)
    print("  lemma G certificates at visited ties: %d (%d further members"
          % (audit.certs, audit.cert_skipped))
    print("  left uncertified by the per-type cap of %d)" % CERT_PAIRS)
    ok(not audit.starve_bad, "PR4 failed at %s" % audit.starve_bad[:3])
    ok(not audit.rider_bad, "PR3 failed at %s" % audit.rider_bad[:3])
    ok(not audit.door_bad, "PR1/lemma A: the searched door and the closed "
       "form disagree at %s" % audit.door_bad[:3])
    ls_out = s5_lockstep(R, reps, audit)
    s6_table(R, ideal_out, elem_out, ls_out, sup, audit)
    print("\nALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
