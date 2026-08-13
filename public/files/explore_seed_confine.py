"""Does the SEED explain the confinement? The 336 collisions read at the
factor level.

THE QUESTION. explore_descent_hunt.py finding 5 records a confinement with
nothing explaining it: over the 85,253 walked (3,4) pairs, product Newton
dimension runs 2 / 3002 / 30,127 / 52,122 at dimensions 1 / 2 / 3 / 4 --
96.5% of the box reaches dimension 3 or more -- and NOT ONE of the 82,249
pairs at dimension 3 or 4 collides. All 336 collisions sit at dimension
<= 2. Finding 6 reads the consequence for the delta >= 2 front: if the
confinement is a law, the only surviving corridor is dim = 2 with
delta = 2, and a hunt at higher dimension is a hunt where there is nothing
to find. So what the confinement IS decides where this line of work spends
next, and it is asked before any wider sweep.

The cheap deflation on offer: every walked pair carries a SEED, so a
collision plausibly forces the partner to share the seed's structure,
which would cap the product's dimension BY CONSTRUCTION and make the
confinement a restatement of what a seed is.

WHOSE VOCABULARY, and the aim's own hole. The deflation was written in the
DIMENSION vocabulary -- "does the product span the seed's direction plus
at most one more?" -- and at a COLLINEAR seed that question cannot fail.
A collinear seed has core direction rank 1; the hunt file already
publishes dim <= 2 at every one of the 336; so "seed rank + 1" is
satisfied by arithmetic on two published numbers and no instrument is
consulted. That is a check recomputing its own input, the species
explore_seed_shape.py found in its own S1. The question therefore moves
one level DOWN, into the vocabulary where the mechanism would live: the
Z-IRREDUCIBLE FACTORS of the product's core, which is where a
factorization is decided and where the seed's negativity actually acts.

THE HAND-ATTACK, on paper before any engine code, and it supplies the
sentence the run is here to test.

THE DISJOINT-SUPPORT LEMMA. Let g, h be integer polynomials in disjoint
variable sets, with g carrying a negative coefficient. The monomials of
g*h are the products m_g * m_h, all distinct, with coefficients c_g * c_h.
So g*h carries a negative coefficient too. CONTRAPOSITIVE, which is the
form used below: in any NONNEGATIVE block of a factorization, a factor
carrying a negative coefficient must sit with at least one other factor
sharing a variable with it. Negativity cannot be cancelled across
disjoint variables.

THE ABSORPTION SENTENCE, the candidate mechanism. Take a walked pair whose
seed A is a size-3 menu. explore_seed_shape.py finding 3: a size-3 seed's
reduced exponent vectors are COLLINEAR, so its core is 1 + x^a + x^b along
a single monomial direction L, and every Z-factor of that core is
supported on L -- including the negative one, g. In the pair's own
factorization g sits with the rest of core(A). A SECOND factorization must
also place g in a nonnegative block, and by the lemma that block carries a
factor sharing g's variables. If neither menu's core is non-unique on its
own, that partner factor comes from core(B). Now the term-count law
(explore_seed_shape.py finding 1): a nonnegative factorization of a 0/1
polynomial multiplies term counts and both factors are 0/1, so core(B) at
size 4 is irreducible over N or splits as two 0/1 BINOMIALS and nothing
else. If one of those binomials is spent absorbing g, at most one binomial
is left to contribute a direction off L -- and the product's dimension is
capped at 2 BY THE TERM-COUNT LAW, not by the sweep's box. That is the
deflation, stated so that it can fail.

WHERE IT CANNOT RUN, and this is half the walked box. The same file's
finding 5: at size 4 the collinear shape is essentially absent -- 1 of 44
seeds over {2..32}. Most walked pairs here are seeded by their SIZE-4
half, where the seed's core need not be collinear and the sentence above
has no line L to run on. Which population the 336 sit in is unmeasured,
and it is the measurement this file exists to take.

DISTRUST THE MARGIN, not the kill. The kills below are derived from the
lemma and the term-count law. The MARGIN is the expectation that the
confinement is trivial -- that the seed caps the dimension by
construction -- and that expectation dies on a number already published:
if the seed capped the dimension, the walked pairs would sit at low
dimension too, and 96.5% of them do not. So the cap, if it is real, is
bought by the COLLISION and not by the walk, and S1 re-measures that
split per population rather than inheriting the aggregate.

DESIGN, four stages.
 S0 THE POSITIVE CONTROL, run before any population number is read. Two
    parts, and only the second is independent. (a) The box, the seed
    filter and the pair count must reproduce explore_descent_hunt.py's
    published figures: 1 size-3 seed and it is {2,8,32}, 17 size-4 seeds,
    85,253 deduped pairs. That machinery is IMPORTED from
    explore_menu_reach.py, so this is a regression check on a shared
    instrument and is called one. (b) The genuinely independent control:
    explore_seed_shape.py's criterion_seed3 decides size-3 seedhood by
    ARITHMETIC on exponent vectors with no polynomial factored at all,
    and must return the same size-3 seed set over the same box.
 S1 THE POPULATIONS. Split the walked pairs by which half carries the
    seed -- the size-3 seed's 8855, the size-4 seeds' pairs, and the
    overlap both halves name -- and print the reachable-dimension
    histogram PER POPULATION. Also the core direction rank of every one
    of the 18 seeds, which is what says how many of them the absorption
    sentence can even address.
 S2 THE SWEEP AND THE FACTOR-LEVEL READING. Re-walk the pairs, keep the
    non-unique products, and per collision print: which half carries the
    seed, that seed's core direction rank, the partner's, the product's
    Newton dimension, the product's term count, the factorization count,
    each side's OWN factorization count, whether the seed's negative
    factor has a partner factor sharing its variables, and -- where the
    seed is collinear on a line L -- whether some factor of the partner's
    core is supported on L, and the rank spanned by every product-core
    factor NOT supported on L.
 S3 THE READING. The cross-tabulations: collisions by seed population, by
    seed rank against product dimension, and the absorption columns
    aggregated. This is the measurement.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): 1 size-3 seed, {2,8,32}; 17 size-4 seeds; 85,253 pairs; and
      the arithmetic criterion returns exactly the same size-3 seed set.
  PR1 (S1): BOTH populations supply pairs at dimension >= 3 in the large
      majority. The aggregate 96.5% is published; the claim here is that
      neither population is the low-dimensional one, so the cap is not
      bought by the walk in either.
  PR2 (S2): the sweep re-finds exactly 336 collisions, and every one of
      their products has exactly 12 terms -- t = 12 is what the hunt
      file's finding 1 calls them, and a product whose support collapsed
      would carry a coefficient above 1 and be outside the frame.
  PR3 (S2): at every collision, each side's core factors UNIQUELY on its
      own. Then the product's second factorization must move a factor
      across the seam, by counting alone, and the lemma applies to it.
  PR4 (S2): at every collision whose seed's core is COLLINEAR on a line
      L, some factor of the partner's core is supported on L, and the
      product-core factors not supported on L span rank <= 1.
  PR5: NOT PREDICTED -- which population the 336 sit in, and the seed
      rank against product dimension cross-tab. Those are the
      measurement, and predicting them is what would make S3 unreadable.

KILLS (observables with live failure modes; what each MEANS is weighed
after the run and never before).
  K0: any S0 figure misses, or the arithmetic criterion disagrees with the
      factorization filter. The instrument is broken and nothing below is
      read.
  K1: the sweep re-finds a collision count other than 336, or some
      collision's product does not have 12 terms.
  K2: some collision has a side whose core already factors two ways. Then
      that collision rides on one menu's own non-uniqueness, the seam is
      not crossed by counting alone, and the lemma does not reach it.
  K3: some collinear-seed collision's partner core carries NO factor
      supported on the seed's line. The absorption sentence is not the
      mechanism there.
  K4: some collision's off-line factors span rank >= 2. The term-count
      cap is not what holds the dimension down at that collision, and the
      confinement survives the deflation there.

HONEST LIMITS carried into the reading, stated before the run. (i) The
factorization machinery is explore_menu_reach.py's, imported; S0(a) is
therefore a regression check and not an independent control, and the one
independent control here is S0(b)'s arithmetic criterion, which covers the
SEED FILTER and not the factorization counter. (ii) The boxes are
explore_descent_hunt.py's, which are explore_menu_reach.py's, which are
set by measured cost and not by an argument -- every statement here is
about that box. (iii) The disjoint-support lemma and the term-count law
are proved; the ABSORPTION SENTENCE assembled from them is not, and what
this file does is check whether it describes the 336 collisions. A
sentence true at every collision in one box is an observation about that
box. (iv) Nothing here computes delta; the descent dimensions are
explore_descent_hunt.py's and are not recomputed. (v) Only the (3,4) half
of t = 12 is in scope, as it is for the hunt file; the (2,6) half is
unswept.

FINDINGS (tiers per the standard naming scale; run record below).

0. FIVE ADDITIONS AND CORRECTIONS THE DESIGN DOES NOT NAME, all from reading run 1's
   prints; the slate is left as frozen.
   (i) S2 AND S3 SPLIT THE COLLISIONS BY FRAME. K1 fired -- most products
   do not have 12 terms -- and a single figure quoted over the union of
   the two classes is a figure about neither, so every reading below runs
   over each separately and only the in-frame block carries checks.
   (ii) S4 IS NEW. S3's reading turned out to rest on a bound on the
   SEED's core rank, and whether that bound is a fact about the box
   decides this line of work's next spend, so the stage that tests it was
   added with its own hand argument.
   (iii) TWO CHOICES S2 MAKES THAT THE DESIGN DOES NOT STATE. Where BOTH
   halves are seeds the file reads the SIZE-3 half as the seed and the
   size-4 half as the partner, so those 16 collisions land in the
   collinear bucket; reading them the other way would put them in the
   non-collinear one, and finding 3 handles them explicitly as the
   partner-is-a-seed column rather than letting the tie-break hide them.
   And the "shares a variable" column is STRONGER than the
   disjoint-support lemma: the lemma allows the factor that absorbs the
   negativity to come from the seed's own core, and this asks for one from
   the PARTNER's. It holds at all 336 either way, so what it reports is
   the stronger statement.
   (iv) AND HONEST LIMIT (ii) IS NOW FALSE OF ONE FINDING, in the
   direction that undersells it. The limit says the boxes are
   explore_descent_hunt.py's and that "every statement here is about that
   box". That was true of the design as frozen, which had no S4. Finding
   5 is a PROOF and holds at every bound; its boxes are controls on the
   argument and not its scope, and they are this file's own ({2..32} at
   n = 4, {2..16} at n = 5) rather than the hunt file's. So the limit as
   written would have a reader discount the one result here that needs no
   box. Findings 1 through 4 and 6 remain box-limited exactly as it says.
   (v) S4'S FIRST BOUNDARY CONTROL MEASURED NOTHING. It looked for a
   rank-3 seed at size 5 over {2..16} and that box holds NO size-5 seed at
   all, so the control was deciding on the population's emptiness rather
   than on the claim -- the failure mode explore_descent_hunt.py froze K2
   and K3 against, arriving here in a control instead of a kill. The box
   scan is kept as a measurement and the boundary is tested by
   CONSTRUCTION instead.

1. MOST OF THE 336 ARE NOT AT t = 12 AND ARE NOT 0/1 (measurement; K1
   fired). The 336 products' term counts are 71 at 12, 263 at 10 and 2 at
   8, and a product is 0/1 exactly when it has 12 terms -- the two
   readings are one test, since 3 x 4 = 12 is what the term-count law
   gives when no support collapses. So 265 of the 336 carry a coefficient
   above 1 and sit OUTSIDE the frame this line of work's question is asked in:
   explore_menu_faces.py mints delta for two factorizations of a
   0/1-COEFFICIENT product, and explore_descent_hunt.py finding 1 reports
   the 336 as "collisions at t = 12". The in-frame population is 71.
   Nothing in the hunt file's headline dies of this -- delta = 1 at all
   336 covers the 71 -- but every COUNT it quotes is a count over a
   population that is 4.7x the object.

2. IN FRAME, EVERY COLLISION SITS AT PRODUCT DIMENSION 2, AND THE TWO
   WHERE THE DESCENT WAS FORCED ARE NOT IN IT (observation, 71
   instances). The hunt file's finding 1 records 2 of 336 at dimension 1,
   where delta <= dim forces delta = 1 and nothing is measured. Both are
   8-term products, outside the frame. So in frame the dim column reads 2
   at every one of the 71, delta was free to read 2 at every one, and the
   hunt file's grading read 1 at every one. The negative result is
   CLEANER on the correct population than on the one it was reported
   over.

3. THE ABSORPTION SENTENCE HOLDS WHEREVER IT HAS A LINE, AND THE
   TERM-COUNT CAP HOLDS EXACTLY WHERE ITS HYPOTHESIS DOES (observation,
   64 and 48 instances). 64 of the 71 in-frame collisions have a
   COLLINEAR seed. At every one of the 64 the partner's core carries a
   factor supported on the seed's line -- the absorption the
   disjoint-support lemma demands, 64/64. The off-line rank then splits
   the 64 exactly in two, and the split is the hand-attack's own
   hypothesis showing up as a measurement: at the 48 whose partner is NOT
   itself a seed it reads 1, which is the term-count cap, the partner's
   core being two 0/1 binomials with one spent on the absorption; at the
   16 whose partner IS itself a seed it reads 2, and a seed's core is
   precisely not two 0/1 binomials, so the cap was never priced for them.
   The hand-attack stated that hypothesis and the design as
   frozen dropped it; the run put it back.

4. WHICH POPULATION THE 336 SIT IN, WHICH WAS THE MEASUREMENT
   (measurement). In frame: 48 seeded by the size-3 seed {2,8,32} alone,
   16 where both halves are seeds, 7 by a size-4 seed alone. So the
   collinear seed carries 64 of the 71 while sitting in 8,855 of the
   85,253 walked pairs -- its own 8,838 plus the 17 it shares -- and those
   17 collide 16 times. Every rate here is quoted IN FRAME, since that is
   the whole of finding 1: 94% at the shared 17, against 0.083% over the
   box. Outside the frame the balance inverts: 263 of the 265 are seeded
   by a size-4 seed alone.

5. THE DIMENSION CEILING HAS A PROVED HALF, AND IT IS ONE LAW RATHER
   THAN A FACT PER SIZE: A SEED OF SIZE n HAS CORE RANK AT MOST n - 2,
   FOR n >= 3 (property, proved; verified at n = 3 by
   explore_seed_shape.py's 39,711-menu census, at n = 4 at all 30,077
   rank-3 size-4 menus of {2..32}, and at n = 5 at all 1,962 rank-4
   size-5 menus of {2..16} -- 0 reducible at every size). THE SIMPLEX
   LAW: n exponent vectors of affine rank n - 1 are affinely independent,
   so all n are vertices and the Newton polytope is an (n-1)-SIMPLEX; a
   simplex of dimension >= 2 is Minkowski-indecomposable; a product's
   Newton polytope is the Minkowski sum of its factors'; and the core has
   its content divided out, so no factor is a monomial. Hence such a core
   is Z-IRREDUCIBLE and cannot be a seed, which is the bound.
   THE HYPOTHESIS n >= 3 IS LOAD-BEARING and the audit that generalized
   this is what found it: indecomposability fails for a SEGMENT, which
   splits as two shorter segments, so at n = 2 the law is false and
   1 + x^3 = (1 + x)(1 - x + x^2) is the standing witness against it --
   the very factor the absorption sentence above runs on. What the bound
   gives this line of work: rank 2 at size 4, so the (3,4) seed side is capped
   at 2 at every bound, with the widened size-4 box reading 1 seed at
   rank 1 and 43 at rank 2 and none above; and rank 3 requiring size 5 or
   more, which is where finding 7 picks it up.

6. BUT THE SEED RANK IS NOT WHAT HOLDS THE PRODUCTS DOWN, AND THE
   PER-POPULATION HISTOGRAM IS WHY (observation, over all 85,253 walked
   pairs). The deflation on offer was that the seed caps the product's
   dimension by construction. It does not: the walked pairs reach
   dimension 3 or 4 at 95.6% of the size-3 seed's 8,838 and 96.6% of the
   size-4 seeds' 76,398 -- neither population is the low-dimensional one,
   because the PARTNER is unbounded in rank and 30,077 size-4 menus of
   rank 3 are walked as partners. What collapses the dimension is the
   COLLISION, not the walk, and finding 3 is the mechanism at 48 of the
   71: the absorption spends one of the partner's two binomials on the
   seed's line and leaves one direction. So the confinement is deflated
   where the term-count law reaches and MEASURED-ONLY at the other 23 --
   the 16 with a seed partner and the 7 with a rank-2 seed, where no
   argument here prices the partner's contribution.

7. WHERE THE ROOM ACTUALLY IS: RANK 3 IS REACHED AT SIZE 6, WHICH IS THE
   (2,6) HALF, AND THE BOUND PERMITS SIZE 5 (property, by construction,
   verified by the instrument). The
   simplex law of finding 5 puts rank 3 at size 5 or more (a seed of
   size n has core rank <= n - 2), and the term-count law says where it
   is actually reached: six terms factor as 2 x 3, a 0/1 binomial has
   rank 1 and a 0/1 trinomial rank at most 2, so 3 is reachable at size
   6 and by this route not below. The witness is
   (1 + x^3)(1 + y + z), whose factor 1 + x^3 = (1 + x)(1 - x + x^2)
   supplies the negative Z-factor: in menu clothes over the primes 2, 3, 5
   and doubled, {2, 6, 10, 16, 48, 80} -- size 6, core rank 3, a seed.
   explore_descent_hunt.py finding 6 reads the confinement as relocating
   the front to dim = 2 with delta = 2 and asks whether the confinement
   holds outside its box; this says the (3,4) half cannot host a
   higher-dimensional collision on the seed side AT ANY BOUND, the rank
   bound being proved rather than sampled, and that a rank-3 seed IS
   available at size 6 -- the (2,6) half this line of work carries as an
   instrument design. SIZE 5 IS NOT SETTLED HERE and the sentence stops
   short of it: 5 is a prime term count, so a size-5 seed is exactly a
   Z-reducible core, and whether a 5-point support of rank 3 can have a
   Minkowski-decomposable Newton polytope is not decided by the simplex
   argument, which needs the points to be exactly four. The box scan
   found no size-5 seed at all under 16, which is consistent with either
   answer and settles neither. The wider (3,4) walk is the cheaper move
   and this is the reason it is not the informative one.

HOW THE PREDICTIONS AND KILLS LANDED. PR0, PR1 and PR3 held as written.
PR2 SPLIT: the sweep re-found 336, and its second clause -- that every
product has 12 terms -- failed at 265 of them, which fired K1 and is
finding 1. PR4 SPLIT the same way: its first clause held at 64 of 64,
the partner's core carrying a factor on the collinear seed's line at
every one, and its second failed at 16, which fired K4. Reading the 16
is finding 3 and they are not a scatter -- they are exactly the
collisions whose partner is ITSELF a seed, where the term-count cap the
clause was priced on has no hypothesis, so what K4 killed was a clause
stated more widely than its own hand-attack supported. PR5 was
deliberately not predicted and findings 4, 5 and 6 are what that bought.
K0 did not fire (both S0 legs reproduced, including the independent
arithmetic criterion), K2 did not (each side of every collision factors
uniquely on its own, so every second factorization crosses the seam by
counting alone), and K3 did not. Two kills fired, both on clauses rather
than on the file's question, and the file's question -- does the seed
explain the confinement -- is answered by findings 5 and 6 and not by
either kill.

RUN RECORD (this file, under memwatch.py at the 512MB default, 277.6 s
wall, peak working set 89.7 MB; the sweep itself is ~204 s of it). The
diagnostic half (S0 and S1, under --diagnose) was run first and separately
at 20.8 s and 90.0 MB, which is where finding 6's per-population
histograms come from and why they were known before the sweep was spent.
Run 1: 16/19, with three checks failing -- the two frame checks, which are
finding 1 and the fired K1, and the off-line cap, which read rank 2 at 16
collisions. Reading the split behind that third failure is finding 3: the
16 are exactly the collisions whose partner is itself a seed, where the
cap's hypothesis does not hold, so the check was re-stated against the
hypothesis the hand-attack had named and the design had dropped. Run
2 added the frame split and S4: 23/25, the two failures being K1 and S4's
size-5 boundary control, which found no size-5 seed at all in its box and
so decided nothing (finding 0 (v)). Run 3 replaced that control with the
constructed size-6 witness: 24/25, the one failure being K1 itself, which
is finding 1 and is left standing rather than restated as a pass. Run 4 is
run 3 with two check LABELS corrected -- the shares column is stronger
than the lemma and said so -- and reproduces run 3's verdict sequence
exactly, check for check. Run 5 adds the n = 5 leg of the simplex law,
the control the argument's general form owes at a size neither this file
nor explore_seed_shape.py had tested: 25/26, the one failure still K1.
Every figure above is run 5's.
"""

import os
import sys
import time
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import (X, check, CHECKS, menu_poly, used_vars,
                                zfactors, has_negative, count_from_core)
from explore_menu_faces import exps
from explore_descent_hunt import rank_int, BOX_SMALL, BOX_BIG
from explore_seed_shape import criterion_seed3


# ------------------------------------------------------ direction-space tools
def directions(pts):
    """Exponent differences from the first point -- the direction space."""
    return [[c - b for c, b in zip(p, pts[0])] for p in pts[1:]]


def rank_of(pts):
    rows = directions(pts)
    return rank_int(rows) if rows else 0


def poly_rank(expr):
    return rank_of(exps(expr, X))


def primitive_direction(pts):
    """The primitive spanning vector of a rank-1 direction space, or None.

    Sign-normalized on its first nonzero entry so that two supports on the
    same line report the same vector.
    """
    rows = directions(pts)
    if not rows or rank_int(rows) != 1:
        return None
    row = next(r for r in rows if any(r))
    g = 0
    for c in row:
        g = sympy.igcd(g, c)
    v = [c // int(g) for c in row]
    if next(c for c in v if c) < 0:
        v = [-c for c in v]
    return tuple(v)


def on_line(expr, v):
    """Is this polynomial's support contained in a translate of span(v)?"""
    rows = directions(exps(expr, X))
    if not rows:
        return True
    return rank_int(rows + [list(v)]) == 1


def core_of(A):
    P = menu_poly(A)
    return used_vars(P), zfactors(P)[1]


# ================================================== S0  the positive control
def build_box():
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
    print("  size-3 seeds: " + ", ".join(str(set(A)) for A in seeds[3]))
    print("  size-4 seeds: " + ", ".join(str(set(A)) for A in seeds[4]))
    return menus, seeds, cores, gensof


def build_pairs(menus, seeds):
    """The deduped (size-3, size-4) pairs, as explore_descent_hunt.py walks."""
    pairs = set()
    for S in seeds[3]:
        for M in menus[4]:
            pairs.add((S, M))
    for S in seeds[4]:
        for M in menus[3]:
            pairs.add((M, S))
    return sorted(pairs)


def stage0(menus, seeds, pairs):
    print("\n=== S0  the positive control ===")
    print("  (a) regression against explore_descent_hunt.py's published box")
    check("S0a exactly 1 size-3 seed in the box", len(seeds[3]) == 1)
    check("S0a the size-3 seed is {2,8,32}", seeds[3] == [(2, 8, 32)])
    check("S0a exactly 17 size-4 seeds in the box", len(seeds[4]) == 17)
    print(f"  pairs to walk: {len(pairs)}  "
          f"({len(seeds[3])}x{len(menus[4])} + {len(seeds[4])}x{len(menus[3])}"
          f" less the overlap)")
    check("S0a the deduped pair count reproduces 85253", len(pairs) == 85253)

    print("  (b) the independent control: seedhood by arithmetic, nothing"
          " factored")
    byarith = [A for A in menus[3] if criterion_seed3(A)]
    print(f"    criterion_seed3 over the {len(menus[3])} size-3 menus:"
          f" {len(byarith)} seeds -> "
          + ", ".join(str(set(A)) for A in byarith))
    check("S0b the arithmetic criterion agrees with the factorization filter",
          byarith == seeds[3])


# ====================================================== S1  the populations
def stage1(menus, seeds, pairs):
    print("\n=== S1  the populations, split by which half carries the seed ===")
    s3, s4 = set(seeds[3]), set(seeds[4])

    print("  core direction rank of every seed in the box:")
    for s in (3, 4):
        ranks = {}
        for A in seeds[s]:
            r = poly_rank(menu_poly(A))
            ranks.setdefault(r, []).append(A)
        for r in sorted(ranks):
            print(f"    size {s}, rank {r}: {len(ranks[r]):3d}   "
                  + ", ".join(str(set(A)) for A in ranks[r][:6])
                  + (" ..." if len(ranks[r]) > 6 else ""))
    collinear3 = [A for A in seeds[3] if poly_rank(menu_poly(A)) == 1]
    collinear4 = [A for A in seeds[4] if poly_rank(menu_poly(A)) == 1]
    check("S1 the size-3 seed's core is collinear (rank 1)",
          len(collinear3) == len(seeds[3]))
    print(f"  collinear seeds: {len(collinear3)}/{len(seeds[3])} at size 3,"
          f" {len(collinear4)}/{len(seeds[4])} at size 4")

    # Reachable dimension, per population. The Newton polytope of a product
    # is the Minkowski sum, so this is the rank of the joint direction space
    # and needs no factorization.
    dirs, byp, hist = {}, {}, {}

    def dof(M):
        if M not in dirs:
            dirs[M] = directions(exps(menu_poly(M), X))
        return dirs[M]

    for A, B in pairs:
        pop = ("both" if (A in s3 and B in s4)
               else "seed3" if A in s3 else "seed4")
        r = rank_int(dof(A) + dof(B))
        byp[(A, B)] = (r, pop)
        hist.setdefault(pop, {})
        hist[pop][r] = hist[pop].get(r, 0) + 1

    print("  reachable product Newton dimension, pairs per population:")
    tot = {}
    for pop in ("seed3", "seed4", "both"):
        h = hist.get(pop, {})
        n = sum(h.values())
        hi = sum(v for d, v in h.items() if d >= 3)
        print(f"    {pop:6s}: {n:6d} pairs  {dict(sorted(h.items()))}"
              f"   dim>=3: {hi} ({100.0*hi/n:.1f}%)" if n else
              f"    {pop:6s}: 0 pairs")
        for d, v in h.items():
            tot[d] = tot.get(d, 0) + v
    print(f"    all   : {sum(tot.values()):6d} pairs"
          f"  {dict(sorted(tot.items()))}")
    check("S1 the per-population histograms sum to the swept population",
          sum(tot.values()) == len(pairs))
    check("S1 the aggregate histogram reproduces the published 2/3002/"
          "30127/52122",
          [tot.get(d, 0) for d in (1, 2, 3, 4)] == [2, 3002, 30127, 52122])
    for pop in ("seed3", "seed4"):
        h = hist.get(pop, {})
        n = sum(h.values())
        hi = sum(v for d, v in h.items() if d >= 3)
        check(f"S1 population {pop} is majority dimension >= 3", hi > n / 2)
    return byp


# ============================== S2  the sweep and the factor-level reading
def stage2(pairs, cores, gensof, seeds, byp):
    print("\n=== S2  the sweep, and the 336 read at the factor level ===")
    s3, s4 = set(seeds[3]), set(seeds[4])
    t0 = time.time()
    found = []
    for i, (A, B) in enumerate(pairs):
        g = sorted(set(gensof[A]) | set(gensof[B]), key=lambda v: X.index(v))
        core = cores[A] + cores[B]
        n, _ = count_from_core(core, g)
        if n > 1:
            found.append((A, B, n, g))
            print(f"    COLLISION {set(A)} x {set(B)}  ->  {n} factorizations"
                  f"   [{time.time()-t0:.1f}s]")
        if (i + 1) % 20000 == 0:
            print(f"    ... {i+1}/{len(pairs)} walked, {len(found)} found"
                  f"   [{time.time()-t0:.1f}s]")
    print(f"  swept {len(pairs)} pairs in {time.time()-t0:.1f}s, "
          f"{len(found)} non-unique")

    rows = []
    for A, B, n, g in found:
        which = ("both" if (A in s3 and B in s4)
                 else "seed3" if A in s3 else "seed4")
        seed = A if A in s3 else B
        partner = B if A in s3 else A
        prod = sympy.expand(menu_poly(A) * menu_poly(B))
        dim = poly_rank(prod)
        terms = len(sympy.Poly(prod, *g).monoms())
        maxcoeff = max(abs(c) for c in sympy.Poly(prod, *g).coeffs())
        # each side's OWN factorization count: if both are 1, the product's
        # second factorization must move a factor across the seam.
        nA, _ = count_from_core(cores[A], gensof[A])
        nB, _ = count_from_core(cores[B], gensof[B])
        srank = poly_rank(menu_poly(seed))
        prank = poly_rank(menu_poly(partner))
        L = primitive_direction(exps(menu_poly(seed), X))
        # the negative factors of the seed's core, and whether the partner's
        # core carries a factor sharing variables with them (the lemma) and
        # a factor on the seed's line (the absorption sentence).
        negs = [f for f in cores[seed] if has_negative(f, X)]
        negvars = set()
        for f in negs:
            negvars |= set(used_vars(f))
        shares = any(negvars & set(used_vars(f)) for f in cores[partner])
        online = (None if L is None
                  else any(on_line(f, L) for f in cores[partner]))
        # The rank spanned by the product-core factors NOT on L. The product's
        # direction space is the SUM of the factors' (Minkowski), so this is
        # the concatenation of their direction rows and not the span of their
        # points from a common origin.
        offrank = None
        if L is not None:
            off = []
            for f in cores[A] + cores[B]:
                if not on_line(f, L):
                    off += directions(exps(f, X))
            offrank = rank_int(off) if off else 0
        pseed = partner in (s3 | s4)
        rows.append(dict(A=A, B=B, n=n, pop=which, dim=dim, terms=terms,
                         maxc=maxcoeff, nA=nA, nB=nB, srank=srank,
                         prank=prank, online=online, offrank=offrank,
                         shares=shares, nneg=len(negs), pseed=pseed))
        print(f"    {set(A)} x {set(B)}  pop={which} n={n} terms={terms}"
              f" maxc={maxcoeff} dim={dim} seedrank={srank}"
              f" partnerrank={prank} partnerseed={pseed}"
              f" sideN=({nA},{nB}) shares={shares} online={online}"
              f" offrank={offrank}")
    check("S2 the sweep re-finds the published 336 collisions",
          len(found) == 336)
    # THE FRAME. This line of work's object is a 0/1-COEFFICIENT product
    # (explore_menu_faces.py mints delta for one), and the term-count law
    # says a 3-term and a 4-term 0/1 menu multiply to 12 terms exactly when
    # nothing collapses. So the two readings are the same test, and a
    # product below 12 terms carries a coefficient above 1 and is outside
    # the frame the question is asked in. K1 is frozen on both.
    inframe = [r for r in rows if r["terms"] == 12]
    outframe = [r for r in rows if r["terms"] != 12]
    tc = {}
    for r in rows:
        tc[r["terms"]] = tc.get(r["terms"], 0) + 1
    print(f"  product term counts over the {len(rows)} collisions: "
          f"{dict(sorted(tc.items()))}")
    print(f"  IN FRAME (t=12, 0/1): {len(inframe)};  "
          f"outside it: {len(outframe)}")
    check("S2 a collision's product is 0/1 exactly when it has 12 terms",
          all((r["maxc"] == 1) == (r["terms"] == 12) for r in rows))
    check("S2 every collision's product has exactly 12 terms",
          all(r["terms"] == 12 for r in rows))
    check("S2 each side of a collision factors uniquely on its own",
          all(r["nA"] == 1 and r["nB"] == 1 for r in rows))
    check("S2 product dimension agrees with the pair's reachable dimension",
          all(byp[(r["A"], r["B"])][0] == r["dim"] for r in rows))
    return rows


# ========================================================= S3  the reading
def read_block(label, rows, checked):
    """The factor-level reading over one population.

    Run over the in-frame collisions and again over the ones outside the
    frame, because the two are different objects and a figure quoted over
    their union is a figure about neither. Only the IN-FRAME block carries
    checks -- the frame is where this line of work's question lives.
    """
    print(f"\n  --- {label}: {len(rows)} collisions ---")
    if not rows:
        return
    pops, tab = {}, {}
    for r in rows:
        pops[r["pop"]] = pops.get(r["pop"], 0) + 1
        tab[(r["srank"], r["dim"])] = tab.get((r["srank"], r["dim"]), 0) + 1
    print(f"    by seed population: {dict(sorted(pops.items()))}")
    print("    seed core rank against product Newton dimension:")
    for (sr, d) in sorted(tab):
        print(f"      seed rank {sr}, product dim {d}: {tab[(sr, d)]:4d}")

    coll = [r for r in rows if r["srank"] == 1]
    print(f"    collinear-seed: {len(coll)};  "
          f"non-collinear-seed: {len(rows)-len(coll)}")
    shares = sum(1 for r in rows if r["shares"])
    print(f"    the lemma sharpened to the PARTNER side (the seed's negative"
          f" factor shares a variable with a partner-core factor, which the"
          f" lemma does not require): {shares}/{len(rows)}")
    if coll:
        on = sum(1 for r in coll if r["online"])
        print(f"    the absorption sentence (a partner-core factor sits ON"
              f" the seed's line): {on}/{len(coll)}")
        offs, split = {}, {}
        for r in coll:
            offs[r["offrank"]] = offs.get(r["offrank"], 0) + 1
            split[(r["pseed"], r["offrank"])] = \
                split.get((r["pseed"], r["offrank"]), 0) + 1
        print(f"    off-line rank: {dict(sorted(offs.items()))}")
        print("    off-line rank against whether the PARTNER is itself a"
              " seed:")
        for k in sorted(split):
            print(f"      partner-is-seed={k[0]}, off-line rank {k[1]}:"
                  f" {split[k]:4d}")
    if not checked:
        return
    check("S3 in frame: the seed's negative factor shares a variable with a"
          " PARTNER-core factor -- stronger than the lemma, which allows the"
          " sharing factor to come from the seed's own core",
          all(r["shares"] for r in rows))
    check("S3 in frame: every collision sits at product dimension 2",
          all(r["dim"] == 2 for r in rows))
    check("S3 in frame: no seed of a collision has core rank above 2",
          all(r["srank"] <= 2 for r in rows))
    if coll:
        check("S3 in frame: at every collinear-seed collision the partner"
              " core carries a factor on the seed's line",
              all(r["online"] for r in coll))
        # The term-count cap has a HYPOTHESIS the hand-attack stated and the
        # slate then dropped: it prices the partner's core as two 0/1
        # binomials, which is what a size-4 NON-seed's reducible core is.
        # Where the partner is itself a seed that pricing does not apply, so
        # the cap is asserted exactly where its hypothesis holds.
        check("S3 in frame: where the partner is NOT itself a seed, the"
              " off-line factors span rank <= 1 -- the term-count cap",
              all(r["offrank"] <= 1 for r in coll if not r["pseed"]))
        check("S3 in frame: the off-line rank exceeds 1 only where the"
              " partner is itself a seed",
              all(r["pseed"] for r in coll if r["offrank"] > 1))


def stage3(rows):
    print("\n=== S3  the reading ===")
    if not rows:
        check("S3 there is something to read", False)
        return
    read_block("IN FRAME (t = 12, 0/1 product)",
               [r for r in rows if r["terms"] == 12], True)
    read_block("OUTSIDE THE FRAME (a coefficient above 1)",
               [r for r in rows if r["terms"] != 12], False)


# ============================ S4  how far up the seed rank can go, and why
def stage4():
    """Not named in the design: the bound S3 turns out to rest on.

    S3's in-frame reading caps the product dimension at the SEED's own core
    rank, and every seed in the sweep's box has rank <= 2. Whether that is
    a fact about the box decides whether a wider sweep can host a
    higher-dimensional collision at all -- which is this line of work's next
    spend. The hand argument, on paper before this stage was written:
    four exponent vectors of affine rank 3 are four affinely independent
    points, so all four are vertices and the Newton polytope is a
    3-SIMPLEX; a simplex is Minkowski-indecomposable; the Newton polytope
    of a product is the Minkowski sum of the factors'; and the content is
    already divided out, so no factor is a monomial. Hence a size-4 core of
    rank 3 is Z-IRREDUCIBLE and can never be a seed, and with the size-3
    seeds collinear (explore_seed_shape.py finding 3) every seed of size
    <= 4 has core rank <= 2. Five points of rank 3 are NOT forced to be a
    simplex, so the argument stops at size 4 -- and the boundary control
    below is that a rank-3 seed does appear at size 5.
    """
    print("\n=== S4  the seed-rank bound, and where it stops ===")
    t0 = time.time()
    wide = list(range(2, 33))
    seeds4, r3, r3red = [], 0, []
    for A in combinations(wide, 4):
        rk = poly_rank(menu_poly(A))
        g, core = core_of(A)
        isseed = any(has_negative(f, g) for f in core)
        if isseed:
            seeds4.append((A, rk))
        if rk == 3:
            r3 += 1
            if len(core) > 1:
                r3red.append(A)
    print(f"  size-4 census over {{2..32}}: {len(seeds4)} seeds "
          f"[{time.time()-t0:.1f}s]")
    ranks = {}
    for A, rk in seeds4:
        ranks[rk] = ranks.get(rk, 0) + 1
    print(f"  seed core rank distribution: {dict(sorted(ranks.items()))}")
    print(f"  size-4 menus of rank 3 in the box: {r3}; "
          f"of those, Z-REDUCIBLE: {len(r3red)}")
    check("S4 the widened box's size-4 seed count reproduces the published"
          " 44", len(seeds4) == 44)
    check("S4 no size-4 seed in the widened box has core rank above 2",
          all(rk <= 2 for _, rk in seeds4))
    check("S4 every size-4 menu of rank 3 is Z-irreducible, as the simplex"
          " argument requires", not r3red)

    # A box scan for the boundary, reported and NOT checked. Run 2 put the
    # control here at size 5 over {2..16} and it found no seed AT ALL, so it
    # decided nothing: a control over an empty population passes or fails on
    # the population's emptiness and not on the claim. It stays as a
    # measurement -- size-5 seeds are absent under this bound -- and the
    # boundary is tested constructively instead.
    # THE SIMPLEX LAW AT SIZE 5, which is the control the argument's
    # GENERAL form owes. n points of affine rank n-1 are affinely
    # independent, so the Newton polytope is an (n-1)-simplex -- the
    # argument never used n = 4. Its hypothesis is n >= 3 and that is
    # load-bearing rather than tidy: indecomposability holds for simplices
    # of dimension >= 2 and FAILS for a segment, which splits as two
    # shorter segments, so at n = 2 the law is false and 1 + x^3 =
    # (1 + x)(1 - x + x^2) is the standing witness against it. For n >= 3
    # the law is: a size-n menu whose core has rank n-1 is Z-irreducible
    # and never a seed, so every seed of size n has core rank <= n-2. It
    # is verified here at n = 4 above, at n = 3 by explore_seed_shape.py's
    # own census, and at n = 5 by this scan, a size neither file tested.
    s5, r4, r4red = [], 0, []
    for A in combinations(range(2, 17), 5):
        g, core = core_of(A)
        rk = poly_rank(menu_poly(A))
        if any(has_negative(f, g) for f in core):
            s5.append((A, rk))
        if rk == 4:
            r4 += 1
            if len(core) > 1:
                r4red.append(A)
    print(f"  size-5 seeds over {{2..16}}: {len(s5)}   "
          f"(reported, not a control: an empty population decides nothing)"
          f"   [{time.time()-t0:.1f}s]")
    print(f"  size-5 menus of rank 4 in that box: {r4}; "
          f"of those, Z-REDUCIBLE: {len(r4red)}")
    check("S4 the simplex law at n = 5: every rank-4 size-5 menu is"
          " Z-irreducible, the argument never having used n = 4",
          r4 > 0 and not r4red)

    # THE BOUNDARY CONTROL, constructed rather than sampled. The simplex
    # argument uses that four points of rank 3 are all vertices; more points
    # need not be, so the bound should break above size 4 -- and the
    # term-count law says exactly where. Six terms factor as 2 x 3, a 0/1
    # binomial has rank 1 and a 0/1 trinomial rank at most 2, so 3 is
    # reachable at size 6 and not below by this route. The witness:
    # (1 + x^3)(1 + y + z), whose factor 1 + x^3 = (1 + x)(1 - x + x^2)
    # supplies the negative Z-factor. In menu clothes over the primes
    # 2, 3, 5, doubled so every element is at least 2.
    W = (2, 6, 10, 16, 48, 80)
    gW, coreW = core_of(W)
    rkW = poly_rank(menu_poly(W))
    isW = any(has_negative(f, gW) for f in coreW)
    print(f"  the constructed witness {set(W)}: size {len(W)}, "
          f"core rank {rkW}, seed {isW}")
    print(f"    core: {coreW}")
    check("S4 boundary control: a seed of core rank 3 exists at size 6,"
          " so the rank bound is the simplex and stops at size 4",
          isW and rkW == 3 and len(W) == 6)


def main():
    t0 = time.time()
    menus, seeds, cores, gensof = build_box()
    pairs = build_pairs(menus, seeds)
    stage0(menus, seeds, pairs)
    byp = stage1(menus, seeds, pairs)
    if "--diagnose" in sys.argv:
        print("\n(--diagnose: S0 and S1 only, the sweep not run)")
        ok = sum(1 for _, v in CHECKS if v)
        print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time() - t0:.1f}s")
        return 0 if ok == len(CHECKS) else 1
    rows = stage2(pairs, cores, gensof, seeds, byp)
    stage3(rows)
    stage4()
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time() - t0:.1f}s")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
