"""The descent dimension at the first live term count: does any collision
reach delta >= 2?

THE QUESTION. explore_menu_faces.py minted the DESCENT DIMENSION delta of
two distinct N-irreducible factorizations of one 0/1-coefficient product:
the smallest dimension of a face of the product's Newton polytope on which
the two factorizations already induce different factor multisets, each
initial form divided by its own monomial content. delta >= 1 always -- a
vertex can never grade a collision -- and delta = dim says the mechanism is
of FULL dimension, inherited from no proper face: a collision that is not a
lower-variable identity with the co-factors riding it.

Every object that file and the literature reach reads delta = 1. Its
COROLLARY located the first place a delta >= 2 could live: the incumbent's
classification (van de Woestijne, Thm 3.20) is complete through term count
t = 10, t = 11 is prime and so factors uniquely, and therefore the first
live count is t = 12 -- the first COMPOSITE past the classification. At
t = 12 the menu size pairs are (2,6) and (3,4). (2,6) needs a menu of six
and is past every size any sweep in this corpus has run. (3,4) is the half
the reach file priced at ~18 minutes and deliberately left outside its
boxes. This file asks the (3,4) half.

WHOSE VOCABULARY. The suspicion is written in the FACES vocabulary --
delta, initial forms, monomial content -- which is the object's own, minted
where the observable was. But the PRICE it inherits is written in the reach
file's vocabulary, whose dial is the MENU SIZE PAIR and whose boxes were
set by measured cost and by nothing else (explore_menu_reach.py S3: "THE
BOXES ARE SET BY MEASURED COST, not by an argument that they are the right
ones"). A price quoted in one vocabulary for a question asked in another is
a TRANSPLANT and is flagged here as one: that the (3,4) sweep costs 18
minutes is a fact about the reach file's boxes, and whether those boxes can
host a delta >= 2 collision at all is a separate question this file asks
FIRST, cheaply, before spending the 18 minutes.

THE HAND-ATTACK, on paper before any engine code, and it already bites.
The reach file's boxes are sizes 2 and 3 over {2..32} and size 4 over
{2..24}. The corpus's ONE graded t = 12 point is {2,8,32} x {2,4,16,32}
(explore_menu_faces.py S4). Its size-4 menu contains 32, and 32 > 24. So
the only t = 12 collision the corpus has already graded lies OUTSIDE the
box whose cost quoted the 18 minutes -- which is why that file had to check
it separately, as a named construction in S3b, rather than finding it in a
sweep. A sweep that cannot contain the one point it is extending is not
obviously the right sweep, and the observable that settles it is what the
sweep PRINTS about the collisions it does find, not what that would mean.

DISTRUST THE MARGIN, not the kill. The kill here -- "some pair reads
delta >= 2" -- is derived: it is the corollary's own target. The MARGIN is
the expectation that delta = 1 will hold throughout, and that expectation
is a vibe carried from objects every one of which was hand-built or
classified. So the margin is where this file looks: the frozen kills below
include the two ways the run can print delta = 1 everywhere while measuring
NOTHING -- an empty sweep, and a sweep whose collisions are all collinear,
where delta = 1 is forced by dim = 1 and is not a finding at all.

DESIGN, four stages.
 S0 THE POSITIVE CONTROL, run before any sweep result is read. The delta
    pipeline imported here must reproduce explore_menu_faces.py's own
    published gradings on the two objects that file states in S4: the t = 6
    cyclotomic identity, and the t = 12 instance {2,8,32} x {2,4,16,32}.
    Both are published as dim = 1, delta = 1. If either misreads, the
    instrument is broken and no sweep number below is read.
 S1 THE BOX AUDIT. Print each element of the graded t = 12 point against
    the box it would have to sit in, and print whether an in-box (3,4) pair
    can reach product Newton dimension >= 2 at all -- the necessary
    condition for delta >= 2, since delta <= dim. Reported over the seed
    population the sweep actually walks, not over an argument.
 S2 THE SWEEP. The (3,4) pair at the reach file's own boxes and its own
    seed filter -- a menu is a SEED when its Z-irreducible core carries a
    factor with a negative coefficient, and a pair is walked when either
    side is one. Every non-unique product found is graded: factorization
    count, product Newton dimension, and delta with its minimizing weight.
    Timed, and reported whatever it finds.
 S3 THE READING. The joint distribution of dim and delta over everything
    S2 found, which is the measurement this file exists to take.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): both controls read dim = 1 and delta = 1, matching the values
      explore_menu_faces.py publishes.
  PR1 (S1): the graded t = 12 point is OUTSIDE the size-4 box, on the
      element 32 against the box's ceiling of 24.
  PR2 (S1): the box is NOT disqualified by dimension alone -- some in-box
      (3,4) pair reaches product Newton dimension >= 2.
  PR3 (S2): the sweep finds at least one non-unique (3,4) pair.
  PR4 (S2): every non-unique pair it finds reads delta = 1.
  PR5 (S3): NOT PREDICTED. The dim distribution of the collisions found is
      the measurement; predicting it is what would make S3 unreadable.

KILLS (observables with live failure modes; what each MEANS is weighed
after the run and never before).
  K0: either S0 control reads a dim or a delta other than the published 1
      -- the instrument is broken and nothing below it is read.
  K1: the sweep prints a pair with delta >= 2. This is the outcome the
      corollary hunts: a mechanism of full dimension at the first live
      count.
  K2: the sweep prints ZERO non-unique pairs. The box hosts no (3,4)
      collision at all.
  K3: the sweep prints non-unique pairs and EVERY one has product Newton
      dim = 1. Then delta = 1 is forced by delta <= dim at every one of
      them, and no pair in the box was ever able to read otherwise.

HONEST LIMITS carried into the reading, stated before the run. (i) Any
statement here is about the reach file's boxes, which are a measured-cost
sample and not an argument. (ii) The seed filter is that file's and is
inherited, not re-derived here. (iii) The weight box that computes delta is
a SAMPLE of the normal fan (explore_menu_faces.py's limit (i)), complete
only where a face count is checked against the polytope; S0 is where that
is checked here. (iv) t = 12 is past where the incumbent classifies, so
nothing here is a statement about all collisions at t = 12 -- only about
the ones in this box.

FINDINGS (tiers per the standard naming scale; run record below).

0. TWO CORRECTIONS TO THE SLATE ABOVE, found by the audit that followed
   the run. The slate is left as frozen and both are stated here.
   (i) S0 CARRIES A THIRD CONTROL THE DESIGN DOES NOT NAME, and the file
   carries a mechanism the design does not mention either. delta is read
   off a weight box of (2b+1)^r weights, which is unaffordable past a few
   variables, so the radius is shrunk with the variable count
   (sample_radius) and reported with every grading. The third control
   checks that shrink: the escape specimen graded at the sampled radius
   against the full one, both reading dim = 2, delta = 1.
   (ii) AND HONEST LIMIT (iii) OVERSTATES THE CONTROL IT POINTS AT, in
   the direction that flatters this file. It says the fan sample is
   "complete only where a face count is checked against the polytope; S0
   is where that is checked here". S0 checks no such thing. A face count
   against a polygon is what explore_menu_faces.py's own S0 runs, and
   this file has no equivalent: what its S0 runs is the radius control in
   (i), which asks whether the SHRUNK sample loses a face the full sample
   sees, on the one two-dimensional object at hand. That is the right
   control for the shrink and it is not a completeness claim about the
   fan. So every delta below is read off a SAMPLED fan whose completeness
   is controlled at one specimen and nowhere else -- weaker than the
   frozen sentence claims, and weaker in exactly the direction that
   matters, since an unsampled weight can only LOWER a delta by
   exhibiting a differing face the sample missed. The finding-1 reading
   is therefore an upper bound on each delta, which is the safe side for
   a hunt whose kill is delta >= 2: a missed face could not have hidden
   one.

1. EVERY COLLISION THE (3,4) SWEEP FINDS DESCENDS TO AN EDGE, AND AT
   ALMOST ALL OF THEM THAT WAS MEASURED RATHER THAN FORCED (observation,
   336 instances in one box; the (2,6) half of t = 12 is unswept and
   outside this claim). The (3,4) sweep found 336 non-unique products
   over 85,253 pairs. Every one reads
   delta = 1: the descent dimensions present are exactly [1]. What makes
   that a measurement and not an artifact is the dim column beside it --
   334 of the 336 have product Newton dimension 2, so delta was free to
   read 2 at all but two of them and read 1 instead. Only 2 of 336 are
   one-dimensional, where delta <= dim forces the answer. Every one of the
   336 factors in exactly TWO ways, which the run prints rather than
   assumes -- delta is defined for a PAIR of factorizations, so a product
   factoring three ways would carry one delta per pair and a single
   reported figure would be covering for the others. Here there is one
   pair per product and nothing to cover for. So the reading
   the incumbent's classification supports through t = 10 -- every
   collision is a lower-variable identity with the co-factors riding it --
   survives its first test past where that classification reaches.
   SCOPE, corrected by explore_seed_confine.py finding 1 and not by this
   file's own audit: this file called all 336 collisions "at t = 12" and
   only 71 are. A 3-term and a 4-term 0/1 menu multiply to 12 terms
   exactly when no support collapses, and 265 of these products have 10
   or 8 -- a coefficient above 1, outside the 0/1 frame
   explore_menu_faces.py mints delta for. The delta reading above is
   unaffected, 336 covering the 71; every COUNT here is over a population
   4.7x the object, and the two dimension-1 collisions -- the only ones
   where delta was forced -- are both outside the frame, so IN frame all
   71 sit at dimension 2 and the descent was measured at every one.

2. THE FRONT WAS PRICED 4.4x HIGH, AND THE OVERPRICING IS THE SEED COUNT
   (measurement). The (3,4) half was carried as "~18 minutes", a figure
   quoted from the reach file's own cost model and repeated as the reason
   the pair sat outside its boxes. This whole file -- box build, sweep and
   grading -- runs in 244.4 s, just over four minutes, inside the
   wall-clock line rather than far over it. The gap is not the per-pair
   cost but the PAIR COUNT: the seed filter leaves 1 seed among the 4495
   size-3 menus and 17 among the 8855 size-4 menus, so the walk is 85,253
   pairs -- 1x8855 + 17x4495, less the 17 that both halves name -- and not
   the half-million an 18-minute quote at 2.1 ms implies. Those seed
   counts are not new here: explore_menu_reach.py prints both, and the
   seed lists, in the same stage that quotes the price. So the figure that
   kept this pair unswept had its own refutation in its own output, and
   what was missing was never a measurement -- only the step of pricing
   the walk off the numbers already on the screen.

3. THE BOX THAT PRICED THE SWEEP CANNOT CONTAIN THE POINT THE SWEEP
   EXTENDS (property, from the box constants). The corpus's one graded
   t = 12 point is {2,8,32} x {2,4,16,32}; the size-4 box stops at 24 and
   the menu carries 32. That is why the faces file had to check it as a
   named construction rather than find it in a sweep, and it means the 336
   collisions here and that point are disjoint evidence rather than one
   body with a witness inside it.

4. THE UNIQUE SIZE-3 SEED IN {2..32} IS THAT SAME POINT'S SIZE-3 HALF
   (observation; both seed lists printed in full by the run). Exactly one
   size-3 menu in the box is a seed -- a menu whose Z-irreducible core
   carries a negative coefficient -- and it is {2,8,32}. So one half of
   the corpus's graded point is distinguished in the box while the other
   half is outside it, and the 8855 pairs that half contributes to this
   sweep are every in-box partner it has.

5. IN THIS BOX NON-UNIQUENESS IS CONFINED TO PRODUCT DIMENSION <= 2, AND
   VANISHES ENTIRELY ABOVE IT (observation, over every pair the sweep
   walks; the seed filter is inherited, so this is a statement about the
   walked population and not about menus the filter excludes). A REACHABLE
   dimension is the rank of the joint direction space -- the Newton
   polytope of a product being the Minkowski sum of the factors' -- so it
   needs no factorization and was computed over the same 85,253 pairs the
   sweep walks. It distributes as 2 pairs at dimension 1, 3002 at 2,
   30,127 at 3 and 52,122 at 4: 96.5% of the box reaches dimension 3 or
   more. The collisions do not follow it anywhere. Both dimension-1 pairs
   collide; 334 of the 3002 dimension-2 pairs do, at 11.13%; and NOT ONE
   of the 82,249 pairs at dimension 3 or 4 does. So non-uniqueness here is not
   merely failing to be full-dimensional -- it is absent from the
   dimensions the box overwhelmingly supplies, and nothing in this file
   explains why. AND IT IS NOT ONLY THIS BOX: every collision
   explore_menu_faces.py grades sits at dimension <= 2 as well -- dim = 2
   at the escape specimen and the four family lifts, dim = 1 at the three
   sporadics, the t = 6 identity and the t = 12 instance, ten objects
   that are hand-built or classified rather than swept and that include
   the one this box cannot reach. Two populations with nothing in common
   but the question, and neither has produced a collision above dimension
   2.

6. THAT CLOSES MOST OF THE ROOM A delta >= 2 HAD, AND SAYS WHERE THE REST
   OF IT IS (observation, read off finding 5). delta >= 2 requires
   dim >= 2, so it was natural to look where dimension is plentiful --
   and dimension is plentiful exactly where collisions are absent. If the
   confinement in finding 5 is a law rather than a fact about this box,
   the only surviving corridor for a delta >= 2 collision is dim = 2 with
   delta = 2 -- full-dimensional, on a polytope of dimension 2, where
   finding 1 has already read 334 instances and found delta = 1 at every
   one. That does not settle the front: it relocates it. The question
   worth asking before any wider sweep is whether the confinement holds
   outside this box at all, because a delta >= 2 hunt over dimension 3
   and 4 pairs is a hunt in a region with no collisions in it.
   ANSWERED by explore_seed_confine.py, and the answer moves the spend:
   the confinement is not the seed capping the dimension by construction
   -- both seed populations reach dimension 3 or 4 at over 95% of their
   walked pairs -- but a size-4 core of rank 3 is Z-irreducible and so
   never a seed, which caps the SEED side of this half at rank 2 at every
   bound rather than in this box. A rank-3 seed IS available at size 6
   (size 5 is undecided there), so the room is the (2,6) half and not a
   wider (3,4) walk.

HOW THE PREDICTIONS AND KILLS LANDED. PR0, PR1, PR2, PR3 and PR4 all held
as written; PR5 was deliberately not predicted and findings 5 and 6 are
what that bought. No kill fired: K0 did not (both controls reproduced the
published dim 1, delta 1, and the shrunk weight box reproduced the
full-radius reading on the escape specimen), K1 did not (no delta >= 2),
and K2 and K3 -- the two ways a run prints delta = 1 while measuring
nothing -- did not, which is finding 1's whole content. Freezing K2 and K3
as observables is what makes the negative result readable: without the dim
column a sweep finding 336 collisions at delta = 1 would look identical
whether the descent was measured or forced, and here it was forced at 2 of
them.

RUN RECORD (this file, under memwatch.py at the 512MB default, 244.8 s
wall, peak working set 84.3 MB). The diagnostic half (S0 and S1, under
--diagnose) was run FIRST and separately, at 21.5 s and 71.2 MB peak, to
decide whether the sweep was worth its quoted price before spending it --
which is where findings 2, 3 and 4 come from and why finding 2 was known
before the sweep ran rather than after. Run 1: 10/10, no kill fired, but
the audit that followed found S1's reachable-dimension search exiting
early at the first pair meeting its threshold, so the number it called a
MAXIMUM was a first-hit and read 3 where the true maximum is 4. The search
was made exhaustive -- which is affordable only because the rank needs no
factorization, and needed rank_int, sympy's Matrix.rank() being dominated
by its own overhead at this call count -- and the corrected histogram is
what findings 5 and 6 rest on; neither existed in the form above before
that fix, finding 5 having claimed only a gap between 2 and 3. The same
audit added S3's cross-tabulation, which is where the confinement became
visible, and the printing of the seed lists finding 4 had asserted from
the witness line alone. Run 2, after all three: 11/11. Round 2 of the same
audit found S1's histogram walking the two halves UNDEDUPED while the
sweep walked a set, so the cross-tab was dividing 336 deduped collisions
by 85,270 undeduped pairs; the two now share one pair list, which moved
the dimension-2 denominator from 3019 to 3002 -- every one of the 17
double-named pairs sitting at that dimension -- and the rate from 11.06%
to 11.13%. Run 3, on the shared population: 11/11, and the histogram now
sums to the swept count exactly, which is the check that the two stages
read one population. Round 5 found the grading reading only the FIRST TWO
factorizations of each product while delta is defined per pair, so a
product factoring three ways would have had the other pairs silently
uncovered; every pair is now graded and the largest delta reported. Run
4: 11/11, and the factorization counts print as [2] throughout -- the
earlier reading was right and is now established rather than assumed.
Run 5 adds the delta >= 1 self-test, the proved floor used as a check on
the grading itself: a pair loop that never ran would return the initial 0
and the "no delta >= 2" check would pass on it, for the wrong reason.
12/12. Run 6 adds the check that a collision's PRODUCT dimension equals
its pair's REACHABLE dimension -- the identity the cross-tab silently
rests on, since one table's buckets are counted by the second quantity
and filled by the first. It holds at every collision, as the sumset
argument says it must, and it is now asserted rather than assumed:
13/13, and every figure above is that run's.
"""

import os
import sys
import time
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import (X, check, CHECKS, menu_poly, newton_dim,
                                used_vars, zfactors, has_negative,
                                count_from_core, block_product)
from explore_menu_faces import (descent, report, exps, affine_rank,
                                induced, face_support, weight_box)

BOX_SMALL = list(range(2, 33))    # the reach file's sizes 2,3 box
BOX_BIG = list(range(2, 25))      # the reach file's size-4 box
RUNG12 = ((2, 8, 32), (2, 4, 16, 32))


def core_of(A):
    P = menu_poly(A)
    return used_vars(P), zfactors(P)[1]


def rank_int(rows):
    """Rank of an integer matrix, by fraction-free elimination.

    Used where sympy's Matrix.rank() would be called tens of thousands of
    times on tiny matrices and its overhead, not the arithmetic, dominates.
    """
    m = [list(r) for r in rows]
    rank, col, ncols = 0, 0, len(m[0]) if m else 0
    while rank < len(m) and col < ncols:
        piv = next((i for i in range(rank, len(m)) if m[i][col]), None)
        if piv is None:
            col += 1
            continue
        m[rank], m[piv] = m[piv], m[rank]
        for i in range(rank + 1, len(m)):
            if m[i][col]:
                a, b = m[rank][col], m[i][col]
                m[i] = [b * x - a * y for x, y in zip(m[rank], m[i])]
        rank += 1
        col += 1
    return rank


def sample_radius(r):
    """The weight-box radius, shrunk so the fan sample stays walkable.

    The box is (2b+1)^r weights, so a fixed radius is unaffordable past a
    few variables. The radius used is REPORTED with every grading below,
    because it is the sample the delta was read off (honest limit (iii)).
    """
    return {1: 8, 2: 8, 3: 4}.get(r, 2)


def descent_sampled(fac1, fac2, gens):
    """(product Newton dim, delta, minimizing weight, radius used).

    explore_menu_faces.descent at a radius that depends on the variable
    count, so a collision over many primes terminates.
    """
    prod = sympy.expand(sympy.prod(fac1))
    pts = exps(prod, gens)
    dim = affine_rank(pts)
    r = len(gens)
    b = sample_radius(r)
    seen = {}
    for w in weight_box(r, b):
        seen[tuple(sorted(face_support(pts, w)))] = w
    best_d, best_w = dim, None
    for face, w in seen.items():
        if induced(fac1, gens, w) != induced(fac2, gens, w):
            d = affine_rank(list(face))
            if d < best_d:
                best_d, best_w = d, w
    return dim, best_d, best_w, b


def factorizations(coreA, coreB, gensA, gensB):
    """(count, the N-irreducible factorizations) for the product A*B."""
    g = sorted(set(gensA) | set(gensB), key=lambda v: X.index(v))
    core = coreA + coreB
    n, facs = count_from_core(core, g)
    return n, facs, g


# ==================================================== S0  the positive control
def stage0():
    print("\n=== S0  the positive control: the two published gradings ===")
    x = X[0]
    f1 = [sympy.expand(1 + x + x**2), sympy.expand(1 + x**3)]
    f2 = [sympy.expand(1 + x), sympy.expand(1 + x**2 + x**4)]
    dim, d = report("t = 6 cyclotomic", f1, f2, [x])
    check("S0 control: t=6 reproduces the published dim 1", dim == 1)
    check("S0 control: t=6 reproduces the published delta 1", d == 1)

    A, B = RUNG12
    gA, cA = core_of(A)
    gB, cB = core_of(B)
    n, facs, g = factorizations(cA, cB, gA, gB)
    print(f"  {set(A)} x {set(B)}  ->  {n} factorizations")
    check("S0 control: the graded t=12 point factors in exactly 2 ways",
          n == 2)
    dim, d = report("t = 12 graded point", facs[0], facs[1], g)
    check("S0 control: t=12 reproduces the published dim 1", dim == 1)
    check("S0 control: t=12 reproduces the published delta 1", d == 1)

    # The sweep grades at a SHRUNK weight box (sample_radius), so the shrink
    # is controlled against the full-radius reading on the one object here
    # that is two-dimensional -- the escape specimen the faces file grades
    # at delta = 1 on an edge.
    esc1 = [menu_poly((2, 54)), menu_poly((2, 6, 10, 30, 90))]
    esc2 = [menu_poly((2, 6)), menu_poly((2, 10, 54, 90, 810))]
    ge = used_vars(sympy.expand(esc1[0] * esc1[1]))
    full = descent(esc1, esc2, ge)
    samp = descent_sampled(esc1, esc2, ge)
    print(f"  escape specimen: full radius -> dim={full[0]} delta={full[1]};"
          f"  sampled radius {samp[3]} -> dim={samp[0]} delta={samp[1]}")
    check("S0 control: the shrunk sample reproduces the published delta 1",
          samp[0] == full[0] == 2 and samp[1] == full[1] == 1)


# ========================================================= S1  the box audit
def build_pairs(menus, seeds):
    """The deduped (size-3, size-4) pairs the sweep walks.

    A pair is walked when either side is a seed, so the two halves both
    name the pairs whose BOTH sides are seeds; the set is what removes
    them. S1 and S2 must read the same population or the cross-tab in S3
    divides a deduped numerator by an undeduped denominator.
    """
    pairs = set()
    for S in seeds[3]:
        for M in menus[4]:
            pairs.add((S, M))
    for S in seeds[4]:
        for M in menus[3]:
            pairs.add((M, S))
    both = sum(1 for A, B in pairs if A in set(seeds[3]) and B in set(seeds[4]))
    print(f"  pairs to walk: {len(pairs)}  "
          f"({len(seeds[3])}x{len(menus[4])} + {len(seeds[4])}x{len(menus[3])}"
          f" less the {both} both halves name)")
    return sorted(pairs)


def stage1(pairs):
    print("\n=== S1  the box audit ===")
    A, B = RUNG12
    print(f"  the graded t=12 point: {set(A)} (size 3) x {set(B)} (size 4)")
    print(f"  size-3 box {{2..{max(BOX_SMALL)}}}: "
          f"{set(A)} in box -> {all(a in BOX_SMALL for a in A)}")
    print(f"  size-4 box {{2..{max(BOX_BIG)}}}: "
          f"{set(B)} in box -> {all(b in BOX_BIG for b in B)}")
    outside = [b for b in B if b not in BOX_BIG]
    print(f"    elements outside the size-4 box: {outside}")
    check("S1 the graded t=12 point is OUTSIDE the sweep's size-4 box",
          bool(outside))

    # Can an in-box (3,4) pair reach product Newton dimension >= 2 at all?
    # The Newton polytope of a product is the Minkowski sum of the factors',
    # whose direction space is dir(A) + dir(B) -- so this needs no
    # factorization and no expansion, only the two difference spaces. (The
    # affine rank of A union B is NOT this number: it also picks up the
    # offset between the two menus, which the sum translates away.)
    # EXHAUSTIVE over the pairs the sweep walks -- no early exit. An early
    # exit here would report the first dimension found at or above the
    # threshold and not the largest, which is a different number and the one
    # finding 5 leans on.
    dirs = {}

    def directions(M):
        if M not in dirs:
            pts = exps(menu_poly(M), X)
            dirs[M] = [[c - b for c, b in zip(p, pts[0])] for p in pts[1:]]
        return dirs[M]

    hist, best, witness, byp = {}, 0, None, {}
    for A2, B2 in pairs:
        rows = directions(A2) + directions(B2)
        r = rank_int(rows) if rows else 0
        hist[r] = hist.get(r, 0) + 1
        byp[(A2, B2)] = r
        if r > best:
            best, witness = r, (A2, B2)
    print(f"  product Newton dimensions REACHABLE in box (pair counts): "
          f"{dict(sorted(hist.items()))}")
    if witness:
        print(f"  max reachable: {best}"
              f"   witness {set(witness[0])} x {set(witness[1])}")
    check("S1 the box is not disqualified by dimension alone", best >= 2)
    return best, hist, byp


# ============================================================ S2  the sweep
def build_box():
    """The menus, the seed filter, and the cores -- the sweep's input."""
    print("\n=== the box: menus, cores and the seed filter ===")
    print(f"  boxes: size 3 over {{2..{max(BOX_SMALL)}}}, "
          f"size 4 over {{2..{max(BOX_BIG)}}}")
    t0 = time.time()
    menus, seeds, cores, gensof = {}, {}, {}, {}
    for s, box in ((3, BOX_SMALL), (4, BOX_BIG)):
        menus[s] = [tuple(c) for c in combinations(box, s)]
        seeds[s] = []
        for A in menus[s]:
            g, core = core_of(A)
            cores[A], gensof[A] = core, g
            if any(has_negative(f, g) for f in core):
                seeds[s].append(A)
        print(f"  size {s}: {len(menus[s]):6d} menus, "
              f"{len(seeds[s]):4d} seeds   [{time.time()-t0:.1f}s]")
        print(f"    seeds: " + ", ".join(str(set(A)) for A in seeds[s]))
    return menus, seeds, cores, gensof


def stage2(pairs, cores, gensof):
    print("\n=== S2  the (3,4) sweep at the reach file's own boxes ===")
    t0 = time.time()
    found = []
    for i, (A, B) in enumerate(pairs):
        n, facs, g = factorizations(cores[A], cores[B], gensof[A], gensof[B])
        if n > 1:
            # delta is defined for a PAIR of factorizations, so a product
            # factoring more than two ways carries one delta per pair. The
            # hunt asks whether ANY pair reaches 2, so take the largest.
            dim, d, w, b = 0, 0, None, 0
            for i1, i2 in combinations(range(len(facs)), 2):
                dim, dd, ww, b = descent_sampled(facs[i1], facs[i2], g)
                if dd > d:
                    d, w = dd, ww
            found.append((A, B, n, dim, d, w, len(g), b))
            print(f"    COLLISION {set(A)} x {set(B)}  ->  {n} factorizations,"
                  f" vars={len(g)} dim={dim} delta={d} w={w} radius={b}"
                  f"   [{time.time()-t0:.1f}s]")
        if (i + 1) % 50000 == 0:
            print(f"    ... {i+1}/{len(pairs)} walked, {len(found)} found"
                  f"   [{time.time()-t0:.1f}s]")
    print(f"  swept {len(pairs)} pairs in {time.time()-t0:.1f}s, "
          f"{len(found)} non-unique")
    return found, len(pairs)


# =========================================================== S3  the reading
def stage3(found, npairs, hist, byp):
    print("\n=== S3  the reading ===")
    if not found:
        print("  the box hosts NO (3,4) collision: nothing to grade.")
        check("S3 the sweep found at least one non-unique pair", False)
        return
    check("S3 the sweep found at least one non-unique pair", True)
    ncounts = sorted({f[2] for f in found})
    print(f"  factorization counts present: {ncounts}"
          f"   (delta is per PAIR of factorizations, and the largest over"
          f" all pairs is what each collision reports)")
    dims = sorted({f[3] for f in found})
    deltas = sorted({f[4] for f in found})
    print(f"  {len(found)} collisions over {npairs} pairs")
    print(f"  product Newton dimensions present: {dims}")
    print(f"  descent dimensions present:        {deltas}")
    forced = [f for f in found if f[3] == 1]
    print(f"  collisions where dim = 1, so delta = 1 is FORCED: "
          f"{len(forced)}/{len(found)}")
    free = [f for f in found if f[3] >= 2]
    print(f"  collisions where dim >= 2, so delta could have read 2: "
          f"{len(free)}/{len(found)}")
    for A, B, n, dim, d, w, nv, b in free[:10]:
        print(f"    {set(A)} x {set(B)}  vars={nv} dim={dim} delta={d}"
              f" w={w} radius={b}")
    # delta >= 1 is PROVED (no vertex can grade a collision), so a reported
    # 0 means the grading returned its initial value -- a pair loop that
    # never ran. Without this the "no delta >= 2" check passes on it.
    check("S3 every reported delta is >= 1, as the proof requires",
          all(f[4] >= 1 for f in found))
    check("S3 no collision in this box reaches delta >= 2",
          all(f[4] <= 1 for f in found))

    # Where the collisions sit against where the pairs sit. A pair's
    # REACHABLE dimension (S1's histogram) and a collision's product
    # dimension are the same quantity, so the two tables cross-tabulate.
    # The cross-tab below puts a collision's PRODUCT dimension (S2, the
    # affine rank of the product's support) into a bucket counted by the
    # pair's REACHABLE dimension (S1, the rank of the joint direction
    # space). Those are the same number -- the support of a convolution of
    # nonnegative things is the sumset, and a Minkowski sum's dimension is
    # the sum of the direction spaces -- but the table is only readable if
    # they agree at every collision, so check rather than assume.
    check("S3 product dimension equals the pair's reachable dimension",
          all(byp[(f[0], f[1])] == f[3] for f in found))
    print("  collisions against pairs, by product Newton dimension:")
    bydim = {}
    for f in found:
        bydim[f[3]] = bydim.get(f[3], 0) + 1
    for d in sorted(hist):
        n, tot = bydim.get(d, 0), hist[d]
        print(f"    dim {d}: {n:4d} collisions among {tot:6d} pairs"
              f"   ({100.0*n/tot:.2f}%)")
    high = sum(hist[d] for d in hist if d >= 3)
    check("S3 no collision at product dimension >= 3, over every such pair",
          all(f[3] <= 2 for f in found) and high > 0)


def main():
    t0 = time.time()
    stage0()
    menus, seeds, cores, gensof = build_box()
    pairs = build_pairs(menus, seeds)
    _, hist, byp = stage1(pairs)
    if "--diagnose" in sys.argv:
        print("\n(--diagnose: S0 and S1 only, the sweep not run)")
        ok = sum(1 for _, v in CHECKS if v)
        print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time() - t0:.1f}s")
        return 0 if ok == len(CHECKS) else 1
    found, npairs = stage2(pairs, cores, gensof)
    stage3(found, npairs, hist, byp)
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time() - t0:.1f}s")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
