"""Is the full-dimension collision at t = 12 ISOLATED, or is it a FAMILY?

THE QUESTION. explore_descent26.py walked the (2,6) half of the first live
term count in the box {2..24} and found that delta = 2 OCCURS -- a collision
whose mechanism no proper face of its Newton polygon explains, exhibited by
one object in eight menu suits. One object cannot say whether full dimension
is a rarity or the generic behaviour past the classification: a lone witness
makes the incompleteness a curiosity, a family makes it the rule. That is
now the whole question, and it is answered by widening the box and re-walking
-- counting delta = 2 objects at the CORE and never at the menu, which is the
trap its predecessor's finding 2 caught in its own headline count.

WHOSE VOCABULARY. The suspicion is written in the FACES vocabulary -- delta,
initial forms, product Newton dimension -- which is the object's own. The
DESIGN VARIABLE it moves on is the element BOX, which is a bound on menu
elements and not on anything the mathematics names: a wider box is a bigger
sample of the same unbounded population, so every count here is about the box
and "family" means "more than one object in {2..32}", never "infinitely
many". The word ISOLATED is the one at risk of being read as a theorem about
the object; nothing below can supply that reading and no finding claims it.

THE TRANSPLANT, flagged. The per-menu census price used to choose the box is
3.08 ms, measured by explore_descent26.py on a stride-137 sample of the
size-6 menus of {2..32} -- the same population and the same operation this
file pays for, so it is a measured figure and not a quote from a neighbouring
size pair. But this file's census loop does MORE per menu than that sample
did (it scans the menu against every size-2 seed core as it goes), so the
figure is a floor and not the price. The price is re-measured on the pilot
box below and extrapolated by the menu-count ratio before the wide run is
launched.

THE HAND-ATTACK, on paper before any engine code, and it is what makes the
widening affordable at all.

THE SIGN SCAN IS NOT ABOUT ITS CORE. explore_descent26.py finding 7 proves
that at the size-2 seed core (1 + x0)(1 - x0 + x0^2), against a size-6
partner whose core is a single Z-irreducible q, the product is non-unique
exactly when (1 - x0 + x0^2) * q has no negative coefficient. That clause has
been carried downstream as a statement about THAT core. Re-reading the
derivation, it is not: write the seed's core as [n, p] with n the negative
factor and p the nonnegative one, and the partner's core as the factor q. The
partitions of {n, p, q} are five and count_from_core weighs them thus.
  {n},{p},{q} and {n},{p q}: rejected, n carries a negative coefficient.
  {n p},{q}: n p is the SEED's own menu core, hence 0/1 and nonnegative; it
     is atomic because its only bipartition is {n},{p} and n is negative. q
     is a single factor, so nonnegative and atomic. VALID, always.
  {n q},{p}: p is nonnegative and atomic; n q is atomic for the same reason
     n p is, its only bipartition being {n},{q}. VALID exactly when n q is
     NONNEGATIVE.
  {n p q}: not atomic -- {q},{n p} is a nonnegative bipartition of it.
So the count is 1 + [n q nonnegative], and the derivation used only four
facts: n negative, p nonnegative, q nonnegative and single, and n p
nonnegative. The last is automatic for any seed, its core being a 0/1 menu
polynomial with the monomial content divided out. Nothing is about
(1 - x0 + x0^2). THE CRITERION HOLDS AT EVERY SEED WHOSE CORE IS EXACTLY TWO
Z-FACTORS OF WHICH EXACTLY ONE IS NEGATIVE, against every single-factor
partner, in EITHER direction of the walk.

AND THE SIBLING CLAUSE FALLS OUT. If a two-factor seed core has BOTH factors
negative, the same five partitions leave only {n1 n2},{q} standing -- both
mixed blocks are rejected on the lone negative factor sitting alone -- so the
product is unique, always, with no scan run at all.

THE WITNESS IS THE CRITERION FIRING. The delta = 2 object's seed is
{3,4,8,9,18,24}, core (x0 + 1)(x0^2 x1 + x0^2 - x0 x1 + x1^2 + x1): two
factors, one negative. Its partner {2,3} has core x0 + x1, a single factor.
The criterion's product n q is
  (x0^2 x1 + x0^2 - x0 x1 + x1^2 + x1)(x0 + x1)
   = x0^3 x1 + x0^3 + x0^2 x1^2 + x0 x1 + x1^3 + x1^2,
which is exactly the second factorization's own 6-term factor, and it is
nonnegative. So the full-dimension mechanism this file is hunting for more of
is one instance of the scan, and the scan can therefore FIND the rest without
the counter -- which is what the widening is bought with.

WHERE THE HAND-ATTACK STOPS. It says nothing where the partner's core has two
or more factors, nor where the seed's core has three or more. Both go through
count_from_core unaided, as does every grading: the scan decides COLLISION or
NOT and never delta, which needs the factorization list and the faces.

THE PRICE AND THE BOX. The size-6 census is the whole cost and no criterion
shortcuts it (6 is composite; explore_seed_shape.py finding 7's
generate-don't-filter move is available at prime menu size only). {2..24} is
100,947 size-6 menus and {2..32} is 736,281, a factor of 7.29. The box is
{2..32} at both sizes, and the size-2 side of that box is where a second
structural thing happens rather than merely a bigger one: over {2..24} the
size-2 seeds are {2,16} and {3,24}, which carry ONE core between them, while
{2..32} adds {4,32} (the same core again) and {8,27}, whose core is
x0^3 + x1^3 = (x0 + x1)(x0^2 - x0 x1 + x1^2) -- a second seed core, in two
variables, of exactly the shape the generalized criterion runs on. So the
widened walk is not one population scaled; it is a second family opened.

MEMORY IS A DESIGN CONSTRAINT HERE AND WAS NOT BEFORE. explore_descent26.py
stored the core of every menu it factored and peaked at 204.6 MB over 100,947
of them. 7.29x that is over the 512MB ceiling, so the census here STREAMS:
each size-6 menu is factored, scanned against the size-2 seed cores, tested
for seedhood, and then DISCARDED unless it is a seed or a collision. sympy's
global expression cache grows with the distinct expressions built, so it is
cleared on a fixed menu stride as well. The run is under memwatch.py at the
512 default and the peak is reported.

DESIGN, five stages.
 S0 THE POSITIVE CONTROL, run before any sweep number is read. Three legs.
    (a) The delta pipeline must reproduce the two gradings
    explore_menu_faces.py publishes: the t = 6 cyclotomic identity and the
    t = 12 point {2,8,32} x {2,4,16,32}, both at dim = 1, delta = 1.
    (b) The exact face enumerator must find a separating EDGE on the escape
    specimen, the corpus's one published two-dimensional delta = 1 object --
    an enumerator returning only vertices would report delta = dim
    everywhere and manufacture a family out of nothing.
    (c) NEW, and it is the control the generalization needs: the criterion
    must fire at the KNOWN delta = 2 witness and must agree with
    count_from_core at every pair of the PILOT box {2..24}, whose answer
    (24 collisions, 9 objects, 55 size-6 seeds, one delta = 2) is published.
    The pilot is run in full before the wide box is walked.
 S1 THE SEED CENSUSES. The size-2 seeds by explore_seed_shape.py's
    arithmetic criterion, checked against the factorization filter, their
    distinct CORES, and the SHAPE TEST that each core is two factors with
    exactly one negative -- the criterion's hypothesis, checked and not
    assumed. Then the streaming size-6 census: every menu factored once, the
    seed list kept, the core-rank distribution of the seeds taken.
 S2 THE WALK, in two halves. The expensive half (size-2 seed core x every
    size-6 menu) rides on the census and is decided by the scan wherever its
    hypothesis holds, by count_from_core elsewhere, and by count_from_core
    ALSO on a fixed stride as a running control. The cheap half (size-6 seed
    x every size-2 menu) goes through count_from_core throughout, memoized
    on the core pair.
 S3 THE READING. The frame split first -- a 2-term and a 6-term 0/1 menu
    multiply to 12 terms exactly when no support collapses, so a product
    below 12 terms carries a coefficient above 1 and is outside the frame
    delta is minted for. Then, IN FRAME: collisions DEDUPED TO OBJECTS by
    core pair, the joint distribution of product dimension and delta over
    the objects, and for every delta >= 2 object its seed and that seed's
    core -- observables (1) and (2).
 S4 THE EXACT GRADING. Every collision of product dimension 2 has the proper
    faces of its Newton polygon enumerated exactly by hull, delta recomputed
    over that list, and the sampled reading checked against it. Every graded
    collision is re-multiplied and matched against the MENU product with
    every factor on both sides checked to be 0/1, independently of the
    counter that produced it.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): all three legs hold -- the two published gradings read
      dim = 1, delta = 1; the enumerator finds a separating edge on the
      escape specimen; and the pilot box reproduces its published answer
      with the criterion agreeing with the counter at every pair it reaches.
  PR1 (S1): the size-2 seeds of {2..32} are exactly {2,16}, {3,24}, {4,32}
      and {8,27}; they carry TWO distinct cores; and both cores are two
      factors with exactly one negative, so the criterion covers both.
  PR2 (S2): the criterion agrees with count_from_core at every pair where
      both are run, in the pilot box and on the wide box's stride alike.
  PR3 (S2): the wide walk's collision set CONTAINS the pilot box's -- the
      boxes are nested, so every {2..24} collision must reappear. A wide run
      that loses one has a bug the counts would not show.
  PR4 (S1): NOT PREDICTED. The size-6 seed count of the wide box and its
      core-rank distribution are observable (1) and predicting them is what
      would make the census unreadable.
  PR5 (S3): NOT PREDICTED. How many DISTINCT delta = 2 objects the wide box
      holds, and whether any has a seed other than {3,4,8,9,18,24}'s core,
      is observable (2) and is the one this file exists to decide.
  PR6 (S3): NOT PREDICTED. Whether product dimension 3 is still unreached is
      observable (3) -- the confinement was the claim that survived the
      narrow box and this is its first contact with a wider one.

KILLS (observables with live failure modes; what each MEANS is weighed after
the run and never before).
  K0: any S0 leg fails. The instrument is broken and nothing below is read.
  K1: the wide box holds a delta >= 2 object whose seed core is NOT
      {3,4,8,9,18,24}'s. The witness is not isolated and full dimension is a
      family -- the target this widening was aimed at.
  K2: some in-frame collision reaches product dimension >= 3. The
      confinement fails at the wider box, which is the claim that survived
      the narrow one.
  K3: the criterion disagrees with count_from_core at any pair where both
      are run. The generalization is wrong and the wide walk's collision
      set is under suspicion with it.
  K4: the wide walk's collision set does not contain the pilot box's. The
      streaming rewrite lost a collision the stored-core version found.
  K5: the wide walk prints ZERO in-frame collisions, or the box holds NO
      size-6 seed. Either decides on a population's emptiness rather than on
      the claim.

HONEST LIMITS carried into the reading, stated before the run. (i) The box
{2..32} is set by the measured price and by no argument that it is the right
box; every count here is about that box, and "isolated" can only ever mean
"alone in the box walked". (ii) The scan, not the counter, decides most of
the expensive half. It is PROVED and it is checked against the counter
across the whole pilot box and on a stride of the wide one -- but a wide-box
pair off that stride is decided by the proof and by no second computation.
(iii) delta is exact only where the exact enumerator applies, which is
product dimension 2: its hull routine is a polygon routine. If K2 fires, that
collision's delta is read off the sampled weight box and is an UPPER bound,
which is the unsafe direction for reporting 2 -- so a dimension-3 collision
would leave this file with a delta it cannot certify, and the finding would
say so rather than quote the number. (iv) Nothing here leaves the menu frame:
a 0/1 product with a factor carrying a coefficient above 1 is outside every
statement below. (v) The size-2 side is generated by an arithmetic criterion
and the size-6 side is filtered by factorization; at composite menu size no
criterion is available, which is why the census is the price.

FINDINGS (tiers per the standard naming scale; run record below).

0. TWO CORRECTIONS THE SLATE DOES NOT CARRY. It is left as frozen.
   (i) THE HAND-ATTACK WEIGHED A MULTISET AS A SET, and the control caught it
   before one minute of census was paid. The frozen derivation enumerates the
   partitions of {n, p, q} and reads five. Where q EQUALS p there are not
   five: {n,p},{q} and {n,q},{p} carry the SAME block multiset, and
   count_from_core -- which dedupes on the blocks and not on the index
   partition -- rightly counts them once. That leaf is UNIQUE whatever the
   sign scan says, so the criterion as frozen over-reports there. Measured on
   the {2..18} rehearsal box: 72 disagreements in 13,517, every one of them a
   size-6 seed whose core's nonnegative factor is x0 + 1 against a size-2
   partner whose core is x0 + 1. With the clause carried, the criterion
   agrees at 13,517 of 13,517 there, at 114,449 of 114,449 on the pilot box
   and at 96,072 of 96,072 on the wide one. The sibling case needs no clause:
   q cannot equal n, a single-factor partner core BEING its own 0/1 menu
   polynomial and hence nonnegative. The species is a derivation over a
   FACTOR MULTISET that counts index partitions rather than block multisets,
   and it is invisible at every population where the factors happen to be
   distinct -- which is why it survived to be found by a control and not by a
   reading.
   (ii) THE PUBLISHED CRITERION IS NOT REACHED BY THAT HOLE, and this run
   CERTIFIES that rather than arguing it. explore_descent26.py finding 7 runs
   at a seed core whose nonnegative factor has 2 terms against a partner core
   with 6, so q = p is impossible there by term count -- an argument, and one
   this file would rather not rest on. The certificate: the CORRECTED
   criterion agrees with the counter across the whole pilot box, and it
   differs from the frozen one ONLY at q = p, so no such pair exists in that
   population and the published 0 disagreements stand untouched, as does every
   restatement of them carried downstream.

1. THE WITNESS IS ISOLATED IN A BOX 7.3x THE ONE THAT FOUND IT (observation;
   the box {2..32}, 736,281 size-6 menus, every grading exact). K1 did not
   fire. The wide walk's 101 distinct pair-walks are 41 in frame, and those
   41 are 22 OBJECTS counted at the core: 21 at delta 1 and exactly ONE at delta 2 --
   the same object, {3,4,8,9,18,24} against {2c,3c}, wearing ten menu suits
   here rather than the narrow box's eight. Not one delta >= 2 object has a
   seed core other than the published one, and the wide box's seed population
   is nearly four times the narrow box's. So full dimension is a RARITY in
   the walked population and not the generic behaviour past the
   classification: the classification's incompleteness is real, and it is
   NARROW. What that is not: a theorem. The box is a bound on menu elements
   and nothing the mathematics names, so "isolated" means alone in {2..32}
   and can never mean alone.

2. THE CONFINEMENT SURVIVES ITS SECOND CONTACT, AND THE ROOM IT DECLINES HAS
   GROWN (observation, 41 in-frame collisions, every one at product dimension
   2). K2 did not fire: none reaches 3 or 4. The wide box holds 203 size-6
   seeds against 55, and 177 of them have core rank 3 against 46 -- so rank 3
   is now 87% of the seed population. A pair's reachable dimension is
   rank(dir A + dir B) and contains dir B, needing no factorization, so all
   177 x 465 = 82,305 pairs seeded by a rank-3 seed reach dimension >= 3, and
   not one of them carries an IN-FRAME collision. The room was there, seven
   times over, and went unused again.
   THE QUALIFIER IS LOAD-BEARING HERE AND WAS NOT AT {2..24}. The dimension
   reading covers the in-frame population, and this box -- unlike the narrow
   one, which had none -- carries 60 out-of-frame pair-walks whose dimension
   no check above reads. Whether the confinement extends to them is untested
   rather than established, and the predecessor could omit the qualifier only
   because its out-of-frame population was empty.

3. THE FRAME TRAP FIRES AT (2,6) ONCE THE BOX IS WIDE ENOUGH (measurement;
   which half or which seed supplies the out-of-frame products is NOT
   measured here and no mechanism is claimed). explore_descent26 finding 4
   reports every one of its collisions in frame and reads the size pair as
   the clean one whose count needs no frame correction. At {2..32} that
   reverses. Read per OBJECT, the one measure not resting on a counting
   convention: 4 of the box's 26 objects sit outside the frame, against 0 of
   the narrow box's 8. Per pair-walk it is 60 of 101. The reading that does
   not survive the widening is "this size pair is outside the trap"; the
   reading that does is that the trap is a fact about a POPULATION, and the
   narrow box's was too small to show it. Every count in findings 1 and 2 is
   taken after the split.
   THE COUNTS HERE ARE PER-OBJECT FOR A SECOND REASON, found by auditing this
   file's own first run. The walk's two halves OVERLAP -- a pair whose size-6
   half is itself a seed is walked by both -- and they count in different
   units, the expensive half walking one REPRESENTATIVE per size-2 seed core
   where the cheap half walks every menu. Four pairs of the wide box were
   walked twice and none of the pilot's were, so the raw totals were a mixed
   measure a narrow box could not expose. The pair lists are now deduped on
   the menu pair before anything is counted, and every comparison across
   boxes is taken at the object.

4. THE SIZE-2 SEED SIDE OF {2..32} IS FOUR MENUS AND TWO CORES (observation;
   PR1 held as written). {2,16}, {3,24} and {4,32} carry the one univariate
   core (1 + x0)(1 - x0 + x0^2); {8,27} carries x0^3 + x1^3 =
   (x0 + x1)(x0^2 - x0 x1 + x1^2), the first TWO-VARIABLE seed core any walk
   in this line of work has had. Both are two factors with exactly one
   negative, so the generalized criterion covers the entire seed side of the
   expensive half rather than a distinguished core of it.

5. WHAT THE WIDE BOX HOLDS AT SIZE 6 (measurement; observable (1)). All
   736,281 size-6 menus of {2..32} factored in 4,126.3 s: 203 seeds, core
   ranks 26 at rank 2 and 177 at rank 3. Core factor counts are 735,357
   single, 923 two and exactly ONE three -- so the criterion's single-factor
   hypothesis holds at 99.87% of the box, against 99.7% at {2..24}, and the
   scan's coverage does not decay as the box widens.

6. STREAMING IS WHAT MADE THE WIDENING FIT, AND IT COST NOTHING (measurement).
   Peak working set 171.4 MB over 736,281 menus, against the predecessor's
   204.6 MB over 100,947: 7.3x the population at 84% of the memory. The
   census discards every core that is neither a seed nor a collision and
   clears sympy's global cache on a fixed menu stride. The per-menu price
   rose to 5.71 ms against the 3.08 ms the slate quoted as a floor, and the
   slate was right to call it a floor -- that sample factored a core, and
   this census also scans it against every size-2 seed core.

7. THE PUBLISHED BOX HOLDS EIGHT OBJECTS AND NOT NINE, AND THE MISCOUNT IS
   THE VERY SPECIES ITS OWN FINDING NAMES (observation, exact; the pilot
   re-walk lists every object). explore_descent26.py finding 2 collapses the
   walk's 24 collisions to 9 objects by dividing out monomial content on the
   SIZE-2 side -- {2c,3c} reducing to x0 + x1 at every c -- and then counts
   the size-6 side by MENU. Two of its eight delta = 1 partners are the same
   object: {2,3,4,6,8,12} and {4,6,8,12,16,24}, the second being 2x the
   first, so a pure scaling of the exponent vectors that the content division
   undoes. Counted at the core throughout, the box is 16 pair-walks and 8
   objects -- 7 at delta 1 and 1 at delta 2 -- where that file reports 24 and
   9. The 24 is not wrong, it is the MENU count, and the two figures differ
   because {2,16} and {3,24} carry one core; the 9 is wrong. This file's own
   count is menu-clothes-free on both sides by construction, its object key
   being the unordered pair of core keys. The species is the one that file
   caught in its predecessor's hand enumeration and then committed on the
   half it was not looking at: a dedup applied to the side the reasoning is
   ABOUT and not to the side it merely ranges over.

HOW THE PREDICTIONS AND KILLS LANDED. PR0 held on all three legs. PR1 held
exactly as written. PR2 held only AFTER the correction of finding 0 (i): as
frozen it failed, and that failure is the finding. PR3 held -- 8 pilot
objects, 0 missing from the wide walk, so the streaming rewrite lost nothing
the stored-core version found. PR4, PR5 and PR6 were deliberately not
predicted and findings 5, 1 and 2 are what that bought. K1 did NOT fire, and
here that is the answer rather than a fault: the witness is alone in the box.
K2 did not fire, which is finding 2. K3 fired on the rehearsal box and is
finding 0 (i); it did not fire once the clause was carried. K4 and K5 did not
fire.

RUN RECORD (this file, under memwatch.py at the 512MB default). A rehearsal
box {2..18} was walked first, at ctrl_stride 1 so the counter ran at every
pair, and it is what fired K3. The reported run is pilot and wide in one
process: 68/68 checks, 4,922.9 s wall (82.0 min), peak working set 171.4 MB,
peak commit 164.1 MB. The pilot census 507.3 s at 5.03 ms/menu, its cheap
half 26.0 s; the wide census 4,201.3 s at 5.71 ms/menu, its cheap half
184.9 s over 60,479 distinct core pairs. The pilot is a full control and not
a warm-up: it reproduces the published 55 size-6 seeds and the published
delta = 2 witness before any wide number is read, and a failed check there
stops the file before the wide box is walked. A second run, `--pilot
--objects`, lists every object of the published box and is where finding 7's
two menus are read: 28/28 checks, 530.1 s, peak working set 72.1 MB.
"""

import os
import sys
import time
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import (X, check, CHECKS, menu_poly, used_vars,
                                has_negative, is_nonneg, count_from_core)
from explore_menu_faces import descent, report, exps, weight_box, \
    face_support, induced
from explore_descent_hunt import (rank_int, descent_sampled, core_of, RUNG12,
                                  factorizations)
from explore_seed_shape import criterion_seed2
from explore_descent26 import (core_key, poly_rank, exact_proper_faces,
                               exact_rank, derived_criterion)

PILOT = list(range(2, 25))        # the published box, re-walked as a control
WIDE = list(range(2, 33))         # the box this file is for
SEED_SIZE, PARTNER_SIZE = 2, 6
CTRL_STRIDE = 499                 # counter-vs-scan control on the wide box
CACHE_STRIDE = 20000              # sympy's global cache is cleared this often


# ------------------------------------------------------ the generalized scan
def scan_shape(core, gens):
    """(kind, negative factor, nonnegative factor) for a two-factor core.

    kind is "one" or "both" by the count of negative factors, and None where
    the core is not two factors -- the hypothesis of the hand-attack, tested
    and never assumed.
    """
    if len(core) != 2:
        return None, None, None
    negs = [f for f in core if has_negative(f, gens)]
    if len(negs) == 2:
        return "both", None, None
    if len(negs) == 1:
        pos = [f for f in core if f is not negs[0]][0]
        return "one", negs[0], pos
    return None, None, None


def scan_collides(shape, partner_core, gens):
    """The criterion. None where its hypothesis fails and it says nothing.

    The frozen hand-attack above weighs the partitions of {n, p, q} as a SET.
    They are a MULTISET: where q equals p, the partitions {n,p},{q} and
    {n,q},{p} carry the SAME block multiset and count_from_core -- which
    dedupes on the blocks and not on the index partition -- rightly counts
    them once. That leaf is UNIQUE whatever the sign scan says, and the
    control caught it (finding 0). q cannot equal n: a single-factor partner
    core IS its 0/1 menu polynomial, hence nonnegative, while n is not.
    """
    kind, neg, pos = shape
    if kind is None or len(partner_core) != 1:
        return None
    if kind == "both":
        return False
    q = partner_core[0]
    if sympy.expand(pos - q) == 0:
        return False
    return is_nonneg(sympy.expand(neg * q), gens)


def gens_of(*exprs):
    used = set()
    for e in exprs:
        used |= set(used_vars(e))
    return sorted(used, key=lambda v: X.index(v))


# ================================================== S0  the positive control
def stage0():
    print("\n=== S0  the positive control ===")
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
    dim, d = report("t = 12 graded point", facs[0], facs[1], g)
    check("S0a the graded t=12 point factors in exactly 2 ways", n == 2)
    check("S0a t=12 reproduces the published dim 1 and delta 1",
          dim == 1 and d == 1)

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
    print(f"  control: escape specimen has {len(efaces)} exact proper faces,"
          f" {len(efaces - set(eseen))} missed; separating dims {edims}")
    check("S0b the exact enumerator finds a separating EDGE on the published"
          " delta-1 specimen, so it can read below dim",
          1 in edims and not (efaces - set(eseen)))

    # (c) the criterion at the known witness, before any wide number is read.
    seed = (3, 4, 8, 9, 18, 24)
    part = (2, 3)
    gs, cs = core_of(seed)
    gp, cp = core_of(part)
    g = gens_of(menu_poly(seed), menu_poly(part))
    shape = scan_shape(cs, g)
    hit = scan_collides(shape, cp, g)
    print(f"  control: the published delta=2 witness {set(seed)} x {set(part)}"
          f" -- criterion kind={shape[0]}, fires={hit}")
    check("S0c the generalized criterion fires at the published delta=2"
          " witness, which is the mechanism it claims to cover",
          hit is True)


# ============================================== S1  the seed censuses (a box)
def seeds_size2(box):
    """The size-2 seeds of a box, by criterion and by filter, with cores."""
    menus = [tuple(c) for c in combinations(box, SEED_SIZE)]
    filt, cores, gens = [], {}, {}
    for A in menus:
        g, core = core_of(A)
        cores[A], gens[A] = core, g
        if any(has_negative(f, g) for f in core):
            filt.append(A)
    arith = [A for A in menus if criterion_seed2(*A)]
    return menus, filt, arith, cores, gens


def stage1_size2(box, label):
    menus, filt, arith, cores, gens = seeds_size2(box)
    print(f"  [{label}] size 2: {len(menus)} menus, {len(filt)} seeds by the"
          f" factorization filter, {len(arith)} by the arithmetic criterion")
    check(f"S1 [{label}] the size-2 arithmetic criterion agrees with the"
          " factorization filter", arith == filt)
    bycore = {}
    for A in filt:
        bycore.setdefault(core_key(cores[A]), []).append(A)
    for k, As in bycore.items():
        core = cores[As[0]]
        g = gens[As[0]]
        kind = scan_shape(core, g)[0]
        print(f"    core {core}  <- {', '.join(str(set(A)) for A in As)}"
              f"   criterion kind={kind}")
    print(f"  [{label}] distinct size-2 seed cores: {len(bycore)}")
    return menus, filt, cores, gens, bycore


def census6(box, seed2cores, ctrl_stride, label):
    """Stream every size-6 menu of the box: seeds out, collisions out, core gone.

    seed2cores is a list of (repr menu, core, gens, scan shape) -- the size-2
    seed side of the expensive half, one entry per distinct CORE.
    """
    menus = [tuple(c) for c in combinations(box, PARTNER_SIZE)]
    seeds, found, nfac = [], [], {}
    tested = agreed = 0
    t0 = time.time()
    for i, M in enumerate(menus):
        gM, cM = core_of(M)
        nfac[len(cM)] = nfac.get(len(cM), 0) + 1
        if any(has_negative(f, gM) for f in cM):
            seeds.append((M, cM, gM))
        for (S, cS, gS, shape) in seed2cores:
            g = sorted(set(gS) | set(gM), key=lambda v: X.index(v))
            pred = scan_collides(shape, cM, g)
            run_counter = pred is None or (i % ctrl_stride == 0)
            if run_counter:
                n, facs = count_from_core(cS + cM, g)
            else:
                n, facs = (2 if pred else 1), None
            if pred is not None and run_counter:
                tested += 1
                agreed += (pred == (n > 1))
            if n > 1:
                if facs is None:
                    n, facs = count_from_core(cS + cM, g)
                found.append(dict(A=S, B=M, n=n, facs=facs, gens=g))
        if (i + 1) % CACHE_STRIDE == 0:
            sympy.core.cache.clear_cache()
            print(f"    ... {i+1}/{len(menus)} factored, {len(seeds)} seeds,"
                  f" {len(found)} collisions   [{time.time()-t0:.1f}s]")
    dt = time.time() - t0
    print(f"  [{label}] size 6: {len(menus)} menus, {len(seeds)} seeds,"
          f" {len(found)} collisions on this half   [{dt:.1f}s,"
          f" {1000*dt/max(1,len(menus)):.2f} ms/menu]")
    print(f"    core factor-count distribution: {dict(sorted(nfac.items()))}")
    ranks = {}
    for (M, cM, gM) in seeds:
        ranks.setdefault(poly_rank(menu_poly(M)), []).append(M)
    print(f"  [{label}] OBSERVABLE (1) size-6 seed core-rank distribution: "
          f"{ {r: len(v) for r, v in sorted(ranks.items())} }")
    check(f"S1 [{label}] the box holds at least one size-6 seed (K5)",
          bool(seeds))
    return menus, seeds, found, tested, agreed


# ============================================ S2  the cheap half of the walk
def walk_seed6(seeds6, menus2, cores2, gens2, label):
    """size-6 seeds x every size-2 menu, memoized on the core pair."""
    print(f"  [{label}] cheap half: {len(seeds6)} size-6 seeds x"
          f" {len(menus2)} size-2 menus")
    memo, found = {}, []
    tested = agreed = 0
    t0 = time.time()
    for (S, cS, gS) in seeds6:
        shape = scan_shape(cS, gS)
        for M in menus2:
            cM, gM = cores2[M], gens2[M]
            g = sorted(set(gS) | set(gM), key=lambda v: X.index(v))
            pred = scan_collides(shape, cM, g)
            key = (core_key(cS), core_key(cM))
            if key in memo:
                n, facs = memo[key]
            else:
                n, facs = count_from_core(cS + cM, g)
                memo[key] = (n, facs) if n > 1 else (n, None)
            if pred is not None:
                tested += 1
                agreed += (pred == (n > 1))
            if n > 1:
                found.append(dict(A=M, B=S, n=n, facs=facs, gens=g))
    print(f"  [{label}] cheap half: {len(found)} collisions, {len(memo)}"
          f" distinct core pairs   [{time.time()-t0:.1f}s]")
    return found, tested, agreed


# ========================================================= S3  the reading
def grade(found):
    """dim, delta, terms, maxc for every collision, in place."""
    for r in found:
        prod = sympy.expand(menu_poly(r["A"]) * menu_poly(r["B"]))
        P = sympy.Poly(prod, *r["gens"])
        r["terms"] = len(P.monoms())
        r["maxc"] = max(abs(c) for c in P.coeffs())
        d, w, dim, b = 0, None, 0, 0
        for i1, i2 in combinations(range(len(r["facs"])), 2):
            dim, dd, ww, b = descent_sampled(r["facs"][i1], r["facs"][i2],
                                             r["gens"])
            if dd > d:
                d, w = dd, ww
        r["dim"], r["delta"], r["w"], r["radius"] = dim, d, w, b
    return found


def object_key(r):
    """The identity of a collision as an OBJECT: its unordered core pair.

    Menu suits share it -- finding 2 of the predecessor is the trap this
    exists to avoid, its 24 collisions being 8 objects (finding 7).
    """
    _, cA = core_of(r["A"])
    _, cB = core_of(r["B"])
    return tuple(sorted([core_key(cA), core_key(cB)]))


def stage3(found, label, pilot_objects=None):
    print(f"\n=== S3  the reading [{label}] ===")
    # THE TWO HALVES OVERLAP AND THEY COUNT DIFFERENTLY. A pair whose size-6
    # half is itself a seed is walked in BOTH halves, so the raw lists must
    # be deduped on the menu pair before anything is counted. And the
    # expensive half walks one REPRESENTATIVE per size-2 seed core while the
    # cheap half walks every menu, so a raw collision total mixes a core
    # count with a menu count -- which is why every figure reported as a
    # COMPARISON is taken per OBJECT, the one measure both halves share.
    byname = {}
    for r in found:
        byname.setdefault((r["A"], r["B"]), r)
    dupes = len(found) - len(byname)
    found = list(byname.values())
    print(f"  {len(found)} distinct pair-walks ({dupes} walked twice, once"
          f" by each half)")
    allobjs = {}
    for r in found:
        allobjs.setdefault(object_key(r), []).append(r)
    tc = {}
    for r in found:
        tc[r["terms"]] = tc.get(r["terms"], 0) + 1
    print(f"  product term counts over {len(found)} collisions:"
          f" {dict(sorted(tc.items()))}")
    check(f"S3 [{label}] a collision's product is 0/1 exactly when it has 12"
          " terms", all((r["maxc"] == 1) == (r["terms"] == 12) for r in found))
    inframe = [r for r in found if r["terms"] == 12]
    outobj = sum(1 for rs in allobjs.values() if rs[0]["terms"] != 12)
    print(f"  IN FRAME: {len(inframe)} pair-walks;  outside it:"
          f" {len(found)-len(inframe)}")
    print(f"  BY OBJECT, the frame split: {len(allobjs)-outobj} in frame,"
          f" {outobj} outside -- the convention-free reading")
    check(f"S3 [{label}] no object straddles the frame boundary",
          all(len({x["terms"] == 12 for x in rs}) == 1
              for rs in allobjs.values()))
    check(f"S3 [{label}] the walk found at least one IN-FRAME collision (K5)",
          bool(inframe))
    objs = {}
    for r in inframe:
        objs.setdefault(object_key(r), []).append(r)
    print(f"  OBSERVABLE (1)  {len(inframe)} in-frame collisions are"
          f" {len(objs)} OBJECTS, counted at the core")
    joint = {}
    for k, rs in objs.items():
        joint[(rs[0]["dim"], rs[0]["delta"])] = \
            joint.get((rs[0]["dim"], rs[0]["delta"]), 0) + 1
        check(f"S3 [{label}] every menu suit of one object grades alike",
              len({(r["dim"], r["delta"]) for r in rs}) == 1)
    if "--objects" in sys.argv:
        print("  every in-frame OBJECT, one line, with its menu suits:")
        for k, rs in sorted(objs.items(), key=lambda kv: -len(kv[1])):
            r = rs[0]
            print(f"    dim={r['dim']} delta={r['delta']}  {len(rs)} suits:"
                  f"  " + "; ".join(f"{set(x['A'])}x{set(x['B'])}"
                                    for x in rs[:6]))
    print("  in frame, by OBJECT, product dimension against delta:")
    for k in sorted(joint):
        print(f"    dim {k[0]}, delta {k[1]}: {joint[k]:4d} objects")
    full = [rs for rs in objs.values() if rs[0]["delta"] >= 2]
    print(f"  OBSERVABLE (2)  delta >= 2 OBJECTS: {len(full)}")
    known = core_key(core_of((3, 4, 8, 9, 18, 24))[1])
    fresh = []
    for rs in full:
        r = rs[0]
        seedside = [m for m in (r["A"], r["B"])
                    if any(has_negative(f, core_of(m)[0])
                           for f in core_of(m)[1])]
        ks = [core_key(core_of(m)[1]) for m in seedside]
        isnew = known not in ks
        fresh.append(isnew)
        print(f"    delta={r['delta']} dim={r['dim']}  {set(r['A'])} x"
              f" {set(r['B'])}  ({len(rs)} menu suits)  seed(s)"
              f" {[set(m) for m in seedside]}  new-seed-core={isnew}")
    check(f"S3 [{label}] every delta>=2 object's seed core is the published"
          " one (K1)", not any(fresh))
    check(f"S3 [{label}] exactly one delta>=2 OBJECT, as the narrow box found"
          " (K1)", len(full) == 1)
    check(f"S3 [{label}] no in-frame collision reaches product dimension >= 3"
          " (K2)", all(r["dim"] <= 2 for r in inframe))
    check(f"S3 [{label}] every reported delta is >= 1, as the proof requires",
          all(r["delta"] >= 1 for r in inframe))
    if pilot_objects is not None:
        missing = pilot_objects - set(objs)
        print(f"  containment: {len(pilot_objects)} pilot objects,"
              f" {len(missing)} missing from the wide walk")
        check(f"S3 [{label}] the wide walk's objects CONTAIN the pilot box's"
              " (K4)", not missing)
    return set(objs), inframe


# ==================================================== S4  the exact grading
def stage4(inframe, label):
    print(f"\n=== S4  the exact grading [{label}] ===")
    ident = allmenu = allbin = True
    for r in inframe:
        lhs = sympy.expand(sympy.prod(r["facs"][0]))
        menu = sympy.expand(menu_poly(r["A"]) * menu_poly(r["B"]))
        for f in r["facs"][1:]:
            ident &= sympy.expand(sympy.prod(f)) == lhs
        q = sympy.Poly(sympy.expand(sympy.cancel(menu / lhs)), *r["gens"])
        allmenu &= len(q.monoms()) == 1 and q.coeffs() == [1]
        for fac in r["facs"]:
            for f in fac:
                allbin &= all(abs(c) == 1
                              for c in sympy.Poly(f, *r["gens"]).coeffs())
    check(f"S4 [{label}] every graded collision's factorizations multiply to"
          " one polynomial, re-expanded independently of the counter", ident)
    check(f"S4 [{label}] every factor on both sides is 0/1, so both readings"
          " sit in the menu frame", allbin)
    check(f"S4 [{label}] every graded collision's product is the MENU product,"
          " up to the monomial content the cores divide out", allmenu)
    ok = checked = agree = 0
    for r in inframe:
        if r["dim"] != 2:
            continue
        pts = exps(sympy.expand(sympy.prod(r["facs"][0])), r["gens"])
        exact = exact_proper_faces(pts)
        seen = {}
        for w in weight_box(len(r["gens"]), r["radius"]):
            seen[frozenset(face_support(pts, w))] = w
        checked += 1
        ok += (not (exact - set(seen)))
        best = r["dim"]
        for f in exact:
            w = seen.get(f)
            if w is not None and induced(r["facs"][0], r["gens"], w) != \
                    induced(r["facs"][1], r["gens"], w):
                best = min(best, len(exact_rank(f)))
        agree += (best == r["delta"])
        r["exact_delta"] = best
    print(f"  collisions at dim 2: {checked}; sample complete at {ok};"
          f" exact delta agrees at {agree}")
    check(f"S4 [{label}] the weight sample produced EVERY proper face of the"
          " Newton polygon at every dimension-2 collision",
          checked > 0 and ok == checked)
    check(f"S4 [{label}] the delta recomputed over the exact face list agrees"
          " with the sampled one", checked > 0 and agree == checked)


# ==================================================================== driver
def run_box(box, label, ctrl_stride, pilot_objects=None):
    print(f"\n=== S1  the seed censuses [{label}]  box {{2..{max(box)}}} ===")
    menus2, seeds2, cores2, gens2, bycore = stage1_size2(box, label)
    seed2cores = []
    for k, As in bycore.items():
        A = As[0]
        seed2cores.append((A, cores2[A], gens2[A],
                           scan_shape(cores2[A], gens2[A])))
    check(f"S1 [{label}] every size-2 seed core is two factors with exactly"
          " one negative, the criterion's hypothesis",
          bool(seed2cores) and all(sh[0] == "one" for *_, sh in seed2cores))
    menus6, seeds6, found_a, ta, aa = census6(box, seed2cores, ctrl_stride,
                                              label)
    print(f"\n=== S2  the walk [{label}] ===")
    found_b, tb, ab = walk_seed6(seeds6, menus2, cores2, gens2, label)
    tested, agreed = ta + tb, aa + ab
    print(f"  [{label}] the criterion was applicable and cross-checked at"
          f" {tested} pairs, and agreed at {agreed}")
    check(f"S2 [{label}] the generalized criterion agrees with the counter"
          " wherever both are run (K3)", tested > 0 and agreed == tested)
    found = grade(found_a + found_b)
    objs, inframe = stage3(found, label, pilot_objects)
    stage4(inframe, label)
    return objs


def main():
    t0 = time.time()
    stage0()
    pilot = run_box(PILOT, "pilot {2..24}", 1)
    # FAIL FAST. The pilot is the whole control surface for the wide walk, and
    # the wide walk is an hour. A failed control there is not something to
    # discover an hour later, so nothing below runs on one.
    if any(not v for _, v in CHECKS):
        print("\nPILOT CONTROL FAILED -- the wide box is not walked.")
        for n, v in CHECKS:
            if not v:
                print(f"  FAIL {n}")
        return 1
    if "--pilot" not in sys.argv:
        run_box(WIDE, "wide {2..32}", CTRL_STRIDE, pilot_objects=pilot)
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time()-t0:.1f}s")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
