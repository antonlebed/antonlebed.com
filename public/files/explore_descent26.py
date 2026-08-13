"""The (2,6) half of t = 12: is any collision's mechanism of FULL dimension?

THE QUESTION. explore_descent_hunt.py swept the (3,4) half of the first live
term count and found every collision descending to an edge (delta = 1), with
every in-frame one sitting at product Newton dimension 2 --
explore_seed_confine.py finding 1 corrects the population to 71. Finding 5 of
that file then proved the SIMPLEX LAW -- a seed of size n has core rank at
most n - 2 for n >= 3 -- which closes the (3,4) seed side at every bound
rather than in a box: a size-4 seed caps at rank 2, so no wider (3,4) walk
can raise the seed side's contribution to the product's dimension. t = 12
admits exactly two menu size pairs, and the other one is (2,6). There the
simplex law permits a seed of core rank 4, and the term-count law reaches
rank 3 by construction. So this is the first size pair where the confinement
-- non-uniqueness absent above product dimension 2 -- is under contact
rather than being restated.

WHOSE VOCABULARY. The suspicion is written in the FACES vocabulary -- delta,
initial forms, product Newton dimension -- which is the object's own. But the
DESIGN VARIABLE it moves on is the MENU SIZE PAIR, which is
explore_menu_reach.py's, and the ROOM it claims to move into was located in
the SIMPLEX vocabulary of explore_seed_confine.py finding 5, a statement
about a SEED's core rank and not about a PRODUCT's dimension. Those are two
different quantities and the step between them is a hypothesis, not an
identity: a product's Newton polytope is the Minkowski sum of its factors',
so a rank-3 seed makes dimension 3 REACHABLE and nothing more. The
transplant is flagged here as one -- the room named at (2,6) is room on the
SEED side, and whether a collision uses it is exactly this file's question.

TRANSPLANT, second and cheaper. The per-pair cost carried by this line of
work is 2.1 ms, a figure measured on the (3,4) walk, where one side is a
3-term menu. Six-term menus are a different animal and the corpus holds no
per-menu figure at size 6 at all. So the price is re-derived here before
being spent, which is the move explore_descent_hunt.py finding 2 rewards:
that file found its own 18-minute quote overpriced 4.4x by a pair count
already printed in its own predecessor's output.

THE PRICE, measured on a strided sample before the box was chosen (stride
137 over the size-6 menus of each candidate box, run under memwatch.py).
Over {2..24}: 100,947 size-6 menus, 2.21 ms per menu to build and factor a
core, projecting 224 s for the census. Over {2..32}: 736,281 menus at
3.08 ms, projecting 2,268 s for the census alone, before any pair is walked.
The pair cost sampled at 2.78 ms. THE BOX IS {2..24} AT BOTH SIZES and it is
set by that measurement and by nothing else.

THE HAND-ATTACK, on paper before any engine code, and it pays for itself
twice -- once by halving the walk and once by supplying a control.

THE SEED SIDE IS ONE CORE. explore_seed_shape.py finding 2 characterizes the
size-2 seeds in closed form: {m, n} is a seed exactly when d has an odd prime
factor, where g = gcd(m, n) and d is the largest integer with m/g and n/g
both perfect d-th powers. Over {2..24} the d = 3 family {c, 8c} supplies
{2,16} and {3,24}, and 27c exceeds 24 for every c >= 2. But a menu's CORE has
its monomial content divided out, and both menus reduce to the same
polynomial: {2,16} is x0 * (1 + x0^3) and {3,24} is x1 * (1 + x0^3). So the
two seeds carry ONE core, (1 + x0)(1 - x0 + x0^2), and the pairs they
contribute are the same computation twice. The walk memoizes on the core and
reports both counts.

THE COLLISION CRITERION AT THAT CORE, derived. Write the seed's core as
[n, p] with n = 1 - x + x^2 and p = 1 + x, and let the size-6 partner's core
be a single Z-irreducible factor q -- which the priced sample says is the
case at 736 of 737 menus. count_from_core partitions {n, p, q} into blocks
that are nonnegative and atomic:
  {n,p,q} and {n, pq}: rejected, n carries a negative coefficient.
  {npq}: rejected, since {np} and {q} is a nonnegative bipartition of it, so
     it is not atomic.
  {np, q}: np = 1 + x^3 is nonnegative, and it is atomic because its only
     bipartition is {n},{p} and n is negative; q is a single factor, hence
     nonnegative and atomic. VALID, always.
  {nq, p}: p is nonnegative and atomic; nq is atomic for the same reason np
     is, its only bipartition being {n},{q}. So this block is valid exactly
     when nq is NONNEGATIVE.
Hence at a single-core partner the product is non-unique exactly when
(1 - x + x^2) * q has no negative coefficient -- one polynomial multiply and
a sign scan, no partitioning at all. This is a CONTROL here and not the
instrument: the sweep runs count_from_core, which is the instrument the
(3,4) half ran, and the criterion is checked against it at every menu whose
core is a single factor. A criterion agreeing with the counter over ~100,000
menus is the independent control explore_seed_confine.py's S0(b) is, and
this file's is over a population 22x larger -- that file's criterion is
checked at the 4,495 size-3 menus of its box.

WHERE THE HAND-ATTACK STOPS. It says nothing about the menus whose core has
two or more factors, nor about the size-6 SEED half of the walk, where the
partner is a 2-term menu and the seed is the six. Both go through
count_from_core unaided.

DISTRUST THE MARGIN, not the kill. The kill -- some collision reads
dimension 3 or delta 2 -- is derived: it is this line of work's own target.
The MARGIN is the expectation that the confinement holds here too, and that
expectation is carried from a size pair whose seed side is capped at rank 2
by a proof. It has no warrant at a pair whose seed side is capped at 4. So
the margin is where this file looks, and the frozen kills below include the
two ways this run can print "confinement holds" while measuring nothing: a
walk that finds no in-frame collision at all, and a box that holds no
size-6 seed, either of which decides on a population's emptiness rather
than on the claim -- the species explore_seed_confine.py finding 0 (v)
names, arriving there in a control and frozen here as a kill.

DESIGN, four stages.
 S0 THE POSITIVE CONTROL, run before any sweep number is read. Two legs.
    (a) The delta pipeline imported here must reproduce the two gradings
    explore_menu_faces.py publishes and explore_descent_hunt.py's S0
    re-reads: the t = 6 cyclotomic identity and the t = 12 point
    {2,8,32} x {2,4,16,32}, both at dim = 1, delta = 1. (b) The shrunk
    weight box must reproduce the full-radius reading on the escape
    specimen, the two-dimensional object the sample could lose a face on.
 S1 THE BOXES AND THE CENSUS. The size-2 seeds by explore_seed_shape.py's
    arithmetic criterion over the box, checked against the factorization
    filter; their distinct CORE count. Then the exhaustive size-6 census:
    every menu factored once, the seed list, and the CORE DIRECTION RANK
    distribution of the seeds -- 6 is composite, so no criterion shortcuts
    this and it is the census that must be paid.
 S2 THE WALK. The deduped pairs -- size-2 seeds x size-6 menus, plus
    size-2 menus x size-6 seeds -- each graded by count_from_core, and
    every non-unique product graded further: factorization count, product
    term count, maximum coefficient, product Newton dimension, and delta
    with its minimizing weight and the radius it was read at. The derived
    criterion is evaluated alongside at every single-core partner and
    checked against the counter.
 S3 THE READING. The frame split first -- a 2-term and a 6-term 0/1 menu
    multiply to 12 terms exactly when no support collapses, so a product
    below 12 terms carries a coefficient above 1 and is outside the frame
    delta is minted for. Then, IN FRAME: the joint distribution of product
    dimension and delta, which is the measurement this file exists to take.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): both gradings read dim = 1, delta = 1, and the sampled radius
      reproduces the full-radius reading on the escape specimen.
  PR1 (S1): the size-2 seeds of the box are exactly {2,16} and {3,24}, the
      arithmetic criterion and the factorization filter agree at all 253
      size-2 menus, and the two seeds carry ONE distinct core.
  PR2 (S2): the derived criterion agrees with count_from_core at every
      size-6 menu whose core is a single factor.
  PR3 (S1): NOT PREDICTED. The size-6 seed count and its core-rank
      distribution are observable (1) and predicting them is what would
      make the census unreadable.
  PR4 (S2): NOT PREDICTED. The collision count and the term-count split
      against 12 are observable (2).
  PR5 (S3): NOT PREDICTED. Whether any in-frame collision reaches product
      dimension >= 3, and what delta reads there, is observable (3) and is
      the one that decides this line of work.

KILLS (observables with live failure modes; what each MEANS is weighed
after the run and never before).
  K0: either S0 leg reads a dim or a delta other than the published 1. The
      instrument is broken and nothing below it is read.
  K1: some in-frame collision reads delta >= 2. This is the target this
      line of work was aimed at: a mechanism of full dimension at the
      first live term count.
  K2: some in-frame collision reads product dimension >= 3. Weaker than K1
      and the one the (3,4) half could not fire, its seed side capping at
      rank 2 -- non-uniqueness would then not be confined to dimension 2.
  K3: the walk prints ZERO in-frame collisions. The box hosts no (2,6)
      collision in frame at all, and every dimension figure below it is a
      figure about an empty set.
  K4: the box holds NO size-6 seed. Then the second half of the walk is
      empty and the census answers on the population's emptiness rather
      than on the claim.
  K5: the derived criterion disagrees with count_from_core at any
      single-core partner. The hand-attack is wrong and the walk's own
      arithmetic is under suspicion with it.

HONEST LIMITS carried into the reading, stated before the run. (i) The box
{2..24} is set by the measured price quoted above and by no argument that it
is the right box; every count here is about that box. (ii) delta is read off
a SAMPLED weight box whose radius shrinks with the variable count
(explore_descent_hunt.py finding 0 (ii)): an unsampled weight can only LOWER
a delta by exhibiting a differing face the sample missed, so every delta here
is an UPPER bound, which is the safe side for a hunt whose kill is
delta >= 2. (iii) The size-2 side is generated by a criterion and the size-6
side is filtered by factorization; at composite menu size no criterion is
available, which is why the census is the price. (iv) Nothing here leaves the
menu frame: a 0/1 product with a factor carrying a coefficient above 1 is
outside every statement below, and the literature's own twelve-term example
is one. (v) "Does a size-6 seed of core rank 3 exist" is NOT an observable
here -- explore_seed_confine.py's S4 answers it yes by the construction
{2,6,10,16,48,80}, whose largest element is outside this box. What is open
is what a box holds, which is a different question and is observable (1).

FINDINGS (tiers per the standard naming scale; run record below).

0. TWO ADDITIONS THE DESIGN DOES NOT NAME. The slate is left as frozen.
   (i) S4 IS NEW, AND K1 FIRING IS WHY. Honest limit (ii) says an unsampled
   weight can only LOWER a delta, and calls that the safe side. It is the
   safe side for a run REPORTING delta = 1, which is what the (3,4) half
   reported and what the limit was written for. This run reports delta = 2,
   and a proper face the weight box missed would deflate exactly that
   reading. So the limit as frozen is backwards for this file's own result,
   and the sample had to be removed from the argument rather than
   disclaimed: S4 enumerates the faces of the Newton POLYGON exactly -- at
   product dimension 2 the proper faces are the vertices and the edges of a
   polygon, so a hull in exact integer arithmetic settles the list -- and
   checks that the weight box produced every one of them. It did, at all 24,
   so no delta reported here is an upper bound and the limit reaches none of
   them.
   (ii) S4 CARRIES THE CONTROL THAT MAKES ITS ANSWER READABLE, and the
   control is not the enumeration's own output. An enumerator that returned
   only VERTICES would find no separating proper face anywhere and report
   delta = dim at every collision, manufacturing this file's result. So it is
   run first on the escape specimen, the corpus's one published
   two-dimensional delta = 1 object, where it must find a separating EDGE.
   It does. The graded collisions are also re-multiplied and matched against
   the MENU product independently of the counter that produced them, with
   every factor on both sides checked to be 0/1.

1. A COLLISION OF FULL DIMENSION EXISTS AT t = 12 (observation, exact --
   every face of the witness's Newton polygon enumerated, so the reading is
   not sample-dependent; the existence half needs one witness and has one).
   The question was whether any 0/1-coefficient collision has a
   mechanism that no face explains -- descent dimension delta >= 2. It does:
     (x0 + x1)(x0^3x1 + x0^3 + x0^2 + x0x1^2 + x1^2 + x1)
       = (x0 + 1)(x0^3x1 + x0^3 + x0^2x1^2 + x0x1 + x1^3 + x1^2),
   a 12-term 0/1 product, four 0/1 factors, product Newton dimension 2 and
   delta 2. In menu clothes it is {2,3} x {3,4,8,9,18,24}. Every proper face
   of that polygon -- 0-dimensional and 1-dimensional alike -- induces the
   SAME factor multiset on both sides; only the whole polygon separates them.
   So the reading that survived the (3,4) half and every object the
   literature classifies -- every collision is a lower-variable identity with
   the co-factors riding it -- is FALSE at the first term count where it
   could fail. The classification of these collisions is structurally
   incomplete, not merely unfinished.

2. THERE IS EXACTLY ONE SUCH MECHANISM IN THE BOX, AND IT WEARS EIGHT MENU
   SUITS (observation, 8 instances of 1 object). The walk prints delta = 2 at
   eight pairs, all sharing the size-6 seed {3,4,8,9,18,24} against the
   size-2 menus {2c, 3c} for c = 1..8. Those are one object, not eight
   witnesses: a menu's core has its monomial content divided out and
   {2c, 3c} reduces to x0 + x1 at every c, so all eight carry an identical
   core pair and an identical identity. The same collapse runs on the other
   side of the ledger -- the 16 collisions at delta = 1 are the box's two
   size-2 seeds, which finding 4 shows carry one core between them, against
   eight distinct size-6 partners. So the walk's 24 collisions are 9 objects:
   one at delta 2 and eight at delta 1. Quoting 24 would be quoting menu
   clothes, the species explore_seed_shape.py finding 4 caught in a hand
   enumeration and this file catches in its own headline count.

3. NON-UNIQUENESS IS STILL CONFINED TO PRODUCT DIMENSION 2, AT THE SIZE
   PAIR WHERE THE SEED SIDE WAS FREE OF IT (observation, 24 instances, all
   in frame). K2 did not fire: every collision sits at dimension 2, none at
   3 or 4. That is the measurement the (3,4) half could not take -- its seed
   side is capped at core rank 2 by the simplex law at every bound, so
   dimension 3 was never reachable there from the seed. Here it is reachable,
   and the count is exact rather than inferred from the seed census. A
   product's Newton polytope is the Minkowski sum of its factors', so a
   pair's reachable dimension is rank(dir A + dir B) and that contains
   dir B: any pair whose size-6 half is one of the 46 rank-3 seeds
   (finding 5) reaches dimension 3 or more, with no factorization consulted.
   Those pairs are 46 x 253 = 11,638 of the walk, every one of them walked,
   and NOT ONE collides. So the room was there and went unused, and the
   confinement survives its first real contact -- it is now the surviving
   structure rather than the suspected one, while the delta = 1 reading it
   was paired with is not. The two were always separate claims and this run
   separates them.
   AND THE FULL-DIMENSION WITNESS COMES FROM A RANK-2 SEED, which is the
   sharp form: {3,4,8,9,18,24} has core rank 2, so the mechanism finding 1
   exhibits is not bought by the extra seed rank this size pair supplies.
   The 46 rank-3 seeds bought dimension and no collisions; a rank-2 seed
   bought the collision that no face explains. Whatever selects the
   witness, it is not the rank.

4. THE FRAME TRAP DID NOT FIRE HERE (measurement, 24 instances; the
   mechanism below is a SUGGESTION and nothing here tests it). At (3,4)
   the frame trap was the
   story: 265 of 336 products carried a coefficient above 1
   (explore_seed_confine.py finding 1). Here ALL 24 products have 12 terms
   and maximum coefficient 1 -- not one collision falls outside the frame.
   The suggestion, untested here and stated as one: a support collapse needs
   a ratio between two menu elements to be matched by a ratio in the
   partner, and a 2-element menu offers ONE such ratio against a 3-element
   menu's three. Whether that is the mechanism is a question for a run that
   measures collapse rates by size pair, which this file does not do -- what
   it reports is the 24. The size pair that looked like the
   expensive half is the clean one, and the count this file reports needs no
   frame correction of the kind its predecessor's did.

5. WHAT THE BOX HOLDS AT SIZE 6, WHICH NO CRITERION COULD HAVE TOLD IT
   (measurement; observable (1)). 6 is composite, so
   explore_seed_shape.py finding 7's generate-don't-filter move is
   unavailable and the census is the price: all 100,947 size-6 menus of
   {2..24} factored, 243.5 s, 55 seeds. Their core direction ranks split 9
   at rank 2 and 46 at rank 3 -- so rank 3, which explore_seed_confine.py
   finding 7 reached by a single construction outside every box, is the
   MAJORITY of the seed population inside this one. The room the simplex law
   permits at size 6 is not a corner of the parameter space; it is where the
   seeds mostly live. 100,644 of the menus have a single Z-irreducible core
   factor and 303 have two.

6. THE SEED SIDE OF THIS SIZE PAIR IS ONE CORE, AND THAT HALVED THE WALK
   (property, proved in the hand-attack; verified at both seeds). The box's
   size-2 seeds are {2,16} and {3,24} by
   explore_seed_shape.py's arithmetic criterion, which agrees with the
   factorization filter at all 253 menus. Both reduce to the same core,
   (1 + x0)(1 - x0 + x0^2), because a core has its monomial content divided
   out -- so the 201,894 pairs their two halves contribute are 100,947
   computations, and memoizing on the core is exact rather than approximate.
   The walk computed 109,587 distinct cores over 215,699 pairs.

7. AND THE COLLISION CONDITION AT THAT CORE IS ONE SIGN SCAN (rule, proved
   in the hand-attack and verified against the counter at 201,288 pairs, 0
   disagreements). Where the size-6 partner's core is a single Z-irreducible
   factor q -- 100,644 of the box's 100,947 menus -- the product is
   non-unique exactly when (1 - x0 + x0^2) * q has no negative coefficient.
   The derivation is four rejected partitions and one surviving one, and it
   needs no partitioning machinery at all. It is used here as a CONTROL and
   not as the instrument: the sweep runs count_from_core, which is what the
   (3,4) half ran, and the criterion is the independent check on it --
   over 22x the population explore_seed_confine.py's S0(b) covers, that
   file's criterion being checked at 4,495 menus against these 100,644.
   What it buys beyond the control is a price: a (2,6) walk that only needs
   the collision COUNT can skip the counter at 99.7% of its pairs.

HOW THE PREDICTIONS AND KILLS LANDED. PR0, PR1 and PR2 held as written.
PR3, PR4 and PR5 were deliberately not predicted and findings 5, 4 and 1
are what that bought. K1 FIRED -- the target it was aimed at, and the only kill
here that is a find rather than a fault. K2 did not fire, which is finding
3 and is the half of the (3,4) reading that survives. K3 and K4, the two
ways this run could have printed a confinement while measuring nothing, did
not fire: 24 in-frame collisions and 55 size-6 seeds, so neither the frame
population nor the seed population decided on its own emptiness. K5 did not
fire at any of the 201,288 pairs where the derived criterion applies.

RUN RECORD (this file, under memwatch.py at the 512MB default). The census
and the pair walk were PRICED FIRST on a strided sample, at 2.21 ms per
size-6 menu over {2..24} against 3.08 ms over {2..32}, which is what chose
the box; the census then came in at 243.5 s against a 224 s projection.
Run 1: 13/14, the one failure being K1 itself, which is finding 1 and is
left standing as a failed check rather than restated as a pass -- 702.6 s
wall, peak working set 204.0 MB, the walk 454.2 s of it. The audit that
followed found honest limit (ii) pointing the wrong way for this file's own
result (finding 0 (i)) and added S4, whose face enumeration was exercised on
the eight delta = 2 collisions alone -- and on the escape-specimen control
-- before the file was re-run, so that a bug in it would not cost a second
walk. Run 2, with S4 in place: 19/20, the one failure still K1. Its S4 runs
over all 24 dimension-2 collisions and not only the eight: the weight box
produced every proper face of the polygon at every one of them, and the
delta recomputed over the exact face list agrees at all 24. So every delta
this file reports is EXACT rather than an upper bound -- the delta = 1
readings as much as the delta = 2 ones -- and honest limit (ii) does not
reach any figure above. 685.9 s wall, peak working set 204.6 MB. Every
figure above is run 2's.
"""

import os
import sys
import time
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import (X, check, CHECKS, menu_poly, used_vars,
                                zfactors, has_negative, is_nonneg,
                                count_from_core)
from explore_menu_faces import descent, report, exps
from explore_descent_hunt import (rank_int, descent_sampled, core_of, RUNG12,
                                  factorizations)
from explore_seed_shape import criterion_seed2

BOX = list(range(2, 25))          # both sizes, set by the measured price
SEED_SIZE, PARTNER_SIZE = 2, 6


def directions(pts):
    return [[c - b for c, b in zip(p, pts[0])] for p in pts[1:]]


def poly_rank(expr):
    rows = directions(exps(expr, X))
    return rank_int(rows) if rows else 0


def core_key(core):
    """A hashable identity for a core, so equal cores are computed once."""
    return tuple(sorted(sympy.srepr(f) for f in core))


# ================================================== S0  the positive control
def stage0():
    print("\n=== S0  the positive control: the published gradings ===")
    x = X[0]
    f1 = [sympy.expand(1 + x + x**2), sympy.expand(1 + x**3)]
    f2 = [sympy.expand(1 + x), sympy.expand(1 + x**2 + x**4)]
    dim, d = report("t = 6 cyclotomic", f1, f2, [x])
    check("S0a t=6 reproduces the published dim 1 and delta 1",
          dim == 1 and d == 1)

    A, B = RUNG12
    gA, cA = core_of(A)
    gB, cB = core_of(B)
    n, facs, g = factorizations(cA, cB, gA, gB)
    print(f"  {set(A)} x {set(B)}  ->  {n} factorizations")
    dim, d = report("t = 12 graded point", facs[0], facs[1], g)
    check("S0a the graded t=12 point factors in exactly 2 ways", n == 2)
    check("S0a t=12 reproduces the published dim 1 and delta 1",
          dim == 1 and d == 1)

    esc1 = [menu_poly((2, 54)), menu_poly((2, 6, 10, 30, 90))]
    esc2 = [menu_poly((2, 6)), menu_poly((2, 10, 54, 90, 810))]
    ge = used_vars(sympy.expand(esc1[0] * esc1[1]))
    full = descent(esc1, esc2, ge)
    samp = descent_sampled(esc1, esc2, ge)
    print(f"  escape specimen: full radius -> dim={full[0]} delta={full[1]};"
          f"  sampled radius {samp[3]} -> dim={samp[0]} delta={samp[1]}")
    check("S0b the shrunk weight sample reproduces the full-radius reading",
          samp[0] == full[0] == 2 and samp[1] == full[1] == 1)


# ============================================= S1  the boxes and the census
def stage1():
    print(f"\n=== S1  the boxes and the census: both sizes over "
          f"{{2..{max(BOX)}}} ===")
    menus2 = [tuple(c) for c in combinations(BOX, SEED_SIZE)]
    cores2, gens2 = {}, {}
    filtered2 = []
    for A in menus2:
        g, core = core_of(A)
        cores2[A], gens2[A] = core, g
        if any(has_negative(f, g) for f in core):
            filtered2.append(A)
    byarith = [A for A in menus2 if criterion_seed2(*A)]
    print(f"  size 2: {len(menus2)} menus, {len(filtered2)} seeds by the"
          f" factorization filter, {len(byarith)} by the arithmetic criterion")
    print("    seeds: " + ", ".join(str(set(A)) for A in filtered2))
    check("S1 the size-2 arithmetic criterion agrees with the filter",
          byarith == filtered2)
    check("S1 the size-2 seeds of the box are {2,16} and {3,24}",
          filtered2 == [(2, 16), (3, 24)])
    keys2 = {core_key(cores2[A]) for A in filtered2}
    for A in filtered2:
        print(f"    {set(A)}: core {cores2[A]}")
    check("S1 the size-2 seeds of the box carry ONE distinct core",
          len(keys2) == 1)

    print(f"  size 6: factoring every menu of {{2..{max(BOX)}}} "
          f"(the census the composite size has to pay)")
    t0 = time.time()
    menus6 = [tuple(c) for c in combinations(BOX, PARTNER_SIZE)]
    cores6, gens6, seeds6, nfac = {}, {}, [], {}
    for i, A in enumerate(menus6):
        g, core = core_of(A)
        cores6[A], gens6[A] = core, g
        nfac[len(core)] = nfac.get(len(core), 0) + 1
        if any(has_negative(f, g) for f in core):
            seeds6.append(A)
        if (i + 1) % 25000 == 0:
            print(f"    ... {i+1}/{len(menus6)} factored, {len(seeds6)} seeds"
                  f"   [{time.time()-t0:.1f}s]")
    print(f"  size 6: {len(menus6)} menus, {len(seeds6)} seeds"
          f"   [{time.time()-t0:.1f}s]")
    print(f"    core factor-count distribution: {dict(sorted(nfac.items()))}")
    ranks = {}
    for A in seeds6:
        r = poly_rank(menu_poly(A))
        ranks.setdefault(r, []).append(A)
    print(f"  OBSERVABLE (1)  size-6 seed core-rank distribution: "
          f"{ {r: len(v) for r, v in sorted(ranks.items())} }")
    for r in sorted(ranks):
        print(f"    rank {r}: " + ", ".join(str(set(A)) for A in ranks[r][:8])
              + (" ..." if len(ranks[r]) > 8 else ""))
    # K4 is frozen on emptiness: a census over an empty population decides
    # on the population and not on the claim.
    check("S1 the box holds at least one size-6 seed (K4)", bool(seeds6))
    return menus2, menus6, cores2, gens2, cores6, gens6, filtered2, seeds6


# ============================================================ S2  the walk
def build_pairs(menus2, menus6, seeds2, seeds6):
    pairs = set()
    for S in seeds2:
        for M in menus6:
            pairs.add((S, M))
    for S in seeds6:
        for M in menus2:
            pairs.add((M, S))
    both = sum(1 for A, B in pairs if A in set(seeds2) and B in set(seeds6))
    print(f"  pairs to walk: {len(pairs)}  "
          f"({len(seeds2)}x{len(menus6)} + {len(seeds6)}x{len(menus2)}"
          f" less the {both} both halves name)")
    return sorted(pairs)


def derived_criterion(seedcore, partnercore, gens):
    """The hand-attack's criterion, valid only at a single-factor partner.

    The seed's core is [n, p] with n negative; the partner's is one factor q.
    Then the product is non-unique exactly when n*q is nonnegative. Returns
    None where the hypothesis does not hold and the criterion says nothing.
    """
    if len(partnercore) != 1 or len(seedcore) != 2:
        return None
    negs = [f for f in seedcore if has_negative(f, gens)]
    if len(negs) != 1:
        return None
    return is_nonneg(sympy.expand(negs[0] * partnercore[0]), gens)


def stage2(pairs, cores, gensof, seeds2):
    print("\n=== S2  the walk ===")
    t0 = time.time()
    s2 = set(seeds2)
    memo, found, tested, agreed = {}, [], 0, 0
    for i, (A, B) in enumerate(pairs):
        g = sorted(set(gensof[A]) | set(gensof[B]), key=lambda v: X.index(v))
        core = cores[A] + cores[B]
        key = core_key(core)
        if key in memo:
            n, facs = memo[key]
        else:
            n, facs = count_from_core(core, g)
            # The factorization LISTS are kept only where they are needed --
            # a collision. Keeping them at every unique core would hold one
            # list per menu in the box, which the 512MB ceiling does not buy.
            memo[key] = (n, facs) if n > 1 else (n, None)
        # the derived criterion, where its hypothesis holds
        if A in s2:
            pred = derived_criterion(cores[A], cores[B], g)
            if pred is not None:
                tested += 1
                agreed += (pred == (n > 1))
        if n > 1:
            prod = sympy.expand(menu_poly(A) * menu_poly(B))
            P = sympy.Poly(prod, *g)
            terms, maxc = len(P.monoms()), max(abs(c) for c in P.coeffs())
            dim, d, w, b = 0, 0, None, 0
            for i1, i2 in combinations(range(len(facs)), 2):
                dim, dd, ww, b = descent_sampled(facs[i1], facs[i2], g)
                if dd > d:
                    d, w = dd, ww
            found.append(dict(A=A, B=B, n=n, terms=terms, maxc=maxc, dim=dim,
                              delta=d, w=w, radius=b, nvars=len(g),
                              facs=facs, gens=g))
            print(f"    COLLISION {set(A)} x {set(B)}  n={n} terms={terms}"
                  f" maxc={maxc} dim={dim} delta={d} vars={len(g)}"
                  f" radius={b} w={w}   [{time.time()-t0:.1f}s]")
        if (i + 1) % 20000 == 0:
            print(f"    ... {i+1}/{len(pairs)} walked, {len(found)} found,"
                  f" {len(memo)} distinct cores   [{time.time()-t0:.1f}s]")
    print(f"  swept {len(pairs)} pairs in {time.time()-t0:.1f}s, "
          f"{len(found)} non-unique; {len(memo)} distinct cores computed")
    print(f"  the derived criterion was applicable at {tested} pairs and"
          f" agreed at {agreed}")
    check("S2 the derived criterion agrees with the counter wherever its"
          " hypothesis holds (K5)", tested > 0 and agreed == tested)
    return found


# ========================================================= S3  the reading
def stage3(found):
    print("\n=== S3  the reading ===")
    if not found:
        print("  the box hosts NO (2,6) collision at all.")
        check("S3 the walk found at least one non-unique pair", False)
        return
    tc = {}
    for r in found:
        tc[r["terms"]] = tc.get(r["terms"], 0) + 1
    print(f"  OBSERVABLE (2)  product term counts over the {len(found)}"
          f" collisions: {dict(sorted(tc.items()))}")
    check("S3 a collision's product is 0/1 exactly when it has 12 terms",
          all((r["maxc"] == 1) == (r["terms"] == 12) for r in found))
    inframe = [r for r in found if r["terms"] == 12]
    print(f"  IN FRAME (t = 12, 0/1): {len(inframe)};  "
          f"outside it: {len(found) - len(inframe)}")
    # K3: every dimension figure below is a figure about this population.
    check("S3 the walk found at least one IN-FRAME collision (K3)",
          bool(inframe))
    if not inframe:
        return
    dims, deltas = {}, {}
    for r in inframe:
        dims[r["dim"]] = dims.get(r["dim"], 0) + 1
        deltas[r["delta"]] = deltas.get(r["delta"], 0) + 1
    print(f"  OBSERVABLE (3)  in frame, product Newton dimension: "
          f"{dict(sorted(dims.items()))}")
    print(f"                  in frame, descent dimension delta: "
          f"{dict(sorted(deltas.items()))}")
    print("  in frame, dimension against delta:")
    joint = {}
    for r in inframe:
        k = (r["dim"], r["delta"])
        joint[k] = joint.get(k, 0) + 1
    for k in sorted(joint):
        forced = " (delta forced by delta <= dim)" if k[0] == 1 else ""
        print(f"    dim {k[0]}, delta {k[1]}: {joint[k]:4d}{forced}")
    free = [r for r in inframe if r["dim"] >= 2]
    print(f"  collisions where dim >= 2, so delta was FREE to read 2: "
          f"{len(free)}/{len(inframe)}")
    # delta >= 1 is proved (no vertex grades a collision), so a reported 0
    # means the pair loop never ran and the delta checks would pass on it.
    check("S3 every reported delta is >= 1, as the proof requires",
          all(r["delta"] >= 1 for r in inframe))
    check("S3 no in-frame collision reaches delta >= 2 (K1)",
          all(r["delta"] <= 1 for r in inframe))
    check("S3 no in-frame collision reaches product dimension >= 3 (K2)",
          all(r["dim"] <= 2 for r in inframe))


# ============== S4  is the sampled fan COMPLETE at the collisions it graded?
def project2(pts):
    """Exact 2-D coordinates for a point set of affine rank 2.

    The affine hull is a plane, so SOME pair of coordinates restricts to an
    affine isomorphism on it -- the pair whose 2x2 minor in a basis of the
    direction space is nonzero. An affine isomorphism carries faces to faces,
    so the hull may be taken in the projection with nothing lost.
    """
    base = pts[0]
    rows = [[a - b for a, b in zip(p, base)] for p in pts[1:]]
    basis = []
    for r in rows:
        if rank_int(basis + [r]) > len(basis):
            basis.append(r)
        if len(basis) == 2:
            break
    b1, b2 = basis
    for i in range(len(base)):
        for j in range(i + 1, len(base)):
            if b1[i] * b2[j] - b1[j] * b2[i]:
                return [(p[i], p[j]) for p in pts], (i, j)
    return None, None


def hull2(q):
    """Monotone-chain hull in exact integer arithmetic; returns the cycle."""
    pts = sorted(set(q))
    if len(pts) <= 2:
        return pts

    def cross(o, a, b):
        return ((a[0]-o[0])*(b[1]-o[1])) - ((a[1]-o[1])*(b[0]-o[0]))

    lo = []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def exact_proper_faces(pts):
    """Every PROPER face of a rank-2 point set's convex hull, exactly.

    A polygon's proper faces are its vertices and its edges, and an edge
    carries every input point lying on its segment -- which is what a weight
    selects, so the comparison against the sample is like for like.
    """
    q, _ = project2(pts)
    idx = {}
    for p, qq in zip(pts, q):
        idx.setdefault(qq, []).append(p)
    cyc = hull2(q)
    faces = set()
    for v in cyc:
        faces.add(frozenset(idx[v]))
    n = len(cyc)
    for k in range(n):
        a, b = cyc[k], cyc[(k + 1) % n]
        on = []
        for qq, ps in idx.items():
            cr = ((b[0]-a[0])*(qq[1]-a[1])) - ((b[1]-a[1])*(qq[0]-a[0]))
            within = (min(a[0], b[0]) <= qq[0] <= max(a[0], b[0])
                      and min(a[1], b[1]) <= qq[1] <= max(a[1], b[1]))
            if cr == 0 and within:
                on += ps
        faces.add(frozenset(on))
    return faces


def stage4(found):
    """Not named in the design: whether the SAMPLE the deltas were read off
    is complete at the objects it graded.

    Honest limit (ii) says an unsampled weight can only LOWER a delta. That
    is the safe direction for a run reporting delta = 1 and the UNSAFE one
    for a run reporting delta = 2: a proper face the weight box missed would
    deflate a 2 to a 1, so a fired K1 is exactly the reading the sample
    cannot be trusted on. This stage removes the sample from the argument at
    every collision of product dimension 2, by enumerating the faces of the
    Newton POLYGON exactly and asking whether the weight box produced all of
    them. Where it did, the delta is exact rather than an upper bound.
    """
    print("\n=== S4  was the sampled fan complete where it graded? ===")
    if not found:
        check("S4 there is something to verify", False)
        return
    from explore_menu_faces import weight_box, face_support, induced
    # THE CONTROL, run before any collision here is read: the enumeration
    # must find the separating EDGE on the one two-dimensional object the
    # corpus publishes at delta = 1. A face enumerator that returned only
    # vertices would report delta = dim everywhere and manufacture the very
    # reading this stage exists to test.
    esc1 = [menu_poly((2, 54)), menu_poly((2, 6, 10, 30, 90))]
    esc2 = [menu_poly((2, 6)), menu_poly((2, 10, 54, 90, 810))]
    ge = used_vars(sympy.expand(esc1[0] * esc1[1]))
    epts = exps(sympy.expand(sympy.prod(esc1)), ge)
    efaces = exact_proper_faces(epts)
    eseen = {}
    for w in weight_box(len(ge), 8):
        eseen[frozenset(face_support(epts, w))] = w
    esep = [f for f in efaces if f in eseen
            and induced(esc1, ge, eseen[f]) != induced(esc2, ge, eseen[f])]
    edims = sorted({len(exact_rank(f)) for f in esep})
    print(f"  control, the escape specimen: {len(efaces)} exact proper faces,"
          f" {len(efaces - set(eseen))} missed by the sample;"
          f" separating face dimensions {edims}")
    check("S4 control: the exact enumeration finds a separating EDGE on the"
          " published delta-1 specimen, so it can read below dim",
          1 in edims and not (efaces - set(eseen)))
    # THE IDENTITY, verified independently of the counter that produced it.
    # count_from_core builds both factorizations from one core, so their
    # equality is true by construction -- and a construction is what a
    # positive control is for. Every graded collision is re-multiplied here
    # and matched against the MENU product, with both factorizations' factors
    # checked to be 0/1: a full-dimensional mechanism whose two sides were
    # not both in the menu frame would not be one.
    ident = allmenu = allbin = True
    for r in found:
        lhs = sympy.expand(sympy.prod(r["facs"][0]))
        menu = sympy.expand(menu_poly(r["A"]) * menu_poly(r["B"]))
        for f in r["facs"][1:]:
            ident &= sympy.expand(sympy.prod(f)) == lhs
        # The menu product is the core product times the monomial content the
        # cores divide out, so their ratio must be a single monomial of
        # coefficient 1 -- which ties the graded object to the MENUS the walk
        # names, and not merely to a polynomial the counter handed back.
        q = sympy.expand(sympy.cancel(menu / lhs))
        qp = sympy.Poly(q, *r["gens"])
        allmenu &= len(qp.monoms()) == 1 and qp.coeffs() == [1]
        for fac in r["facs"]:
            for f in fac:
                allbin &= all(abs(c) == 1 for c in
                              sympy.Poly(f, *r["gens"]).coeffs())
    check("S4 every graded collision's factorizations multiply to one and the"
          " same polynomial, re-expanded independently of the counter", ident)
    check("S4 every factor on both sides of every graded collision is 0/1,"
          " so both readings sit in the menu frame", allbin)
    check("S4 every graded collision's product is the MENU product, up to the"
          " monomial content the cores divide out", allmenu)
    ok, checked, exactdelta = 0, 0, {}
    for r in found:
        if r["dim"] != 2:
            continue
        prod = sympy.expand(sympy.prod(r["facs"][0]))
        pts = exps(prod, r["gens"])
        exact = exact_proper_faces(pts)
        seen = {}
        for w in weight_box(len(r["gens"]), r["radius"]):
            seen[frozenset(face_support(pts, w))] = w
        missing = exact - set(seen)
        checked += 1
        ok += (not missing)
        # delta, recomputed over the EXACT face list: the smallest dimension
        # of a proper face on which the two factorizations already differ,
        # and dim itself when no proper face does.
        best = r["dim"]
        for f in exact:
            w = seen.get(f)
            if w is None:
                continue
            if induced(r["facs"][0], r["gens"], w) != \
                    induced(r["facs"][1], r["gens"], w):
                best = min(best, len(exact_rank(f)))
        exactdelta[(r["A"], r["B"])] = best
        if missing or best != r["delta"]:
            print(f"    {set(r['A'])} x {set(r['B'])}: "
                  f"{len(exact)} exact proper faces, {len(missing)} missed by"
                  f" the sample; sampled delta={r['delta']} exact={best}")
    print(f"  collisions at dim 2: {checked}; sample complete at {ok}")
    agree = sum(1 for r in found if r["dim"] == 2
                and exactdelta.get((r["A"], r["B"])) == r["delta"])
    print(f"  exact delta agrees with the sampled delta at {agree}/{checked}")
    check("S4 the weight sample produced EVERY proper face of the Newton"
          " polygon at every dimension-2 collision",
          checked > 0 and ok == checked)
    check("S4 the delta recomputed over the exact face list agrees with the"
          " sampled one", checked > 0 and agree == checked)


def exact_rank(face):
    """The affine rank of a face, as a list the caller can take len() of."""
    pts = list(face)
    if len(pts) < 2:
        return []
    rows = [[a - b for a, b in zip(p, pts[0])] for p in pts[1:]]
    return [0] * rank_int(rows)


def main():
    t0 = time.time()
    stage0()
    menus2, menus6, cores2, gens2, cores6, gens6, seeds2, seeds6 = stage1()
    cores = dict(cores2)
    cores.update(cores6)
    gensof = dict(gens2)
    gensof.update(gens6)
    pairs = build_pairs(menus2, menus6, seeds2, seeds6)
    if "--diagnose" in sys.argv:
        print("\n(--diagnose: S0 and S1 only, the walk not run)")
        ok = sum(1 for _, v in CHECKS if v)
        print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time()-t0:.1f}s")
        return 0 if ok == len(CHECKS) else 1
    found = stage2(pairs, cores, gensof, seeds2)
    stage3(found)
    stage4(found)
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time()-t0:.1f}s")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
