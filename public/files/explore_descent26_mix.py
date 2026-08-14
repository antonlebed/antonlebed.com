"""The four the generator misses: identified, not diagnosed by elimination.

THE QUESTION. explore_descent26_close.py closed the SEED side of the (2,6)
generator exactly -- all 203 size-6 seeds of {2..32} flagged, every negative
factor of every one of them paired -- and the in-frame object count stayed at
18 against the census's published 22. Its finding 4 named the residual a
PAIRING HYPOTHESIS in two branches and left both live: a differing block that
MIXES factors drawn from both cores, or one sitting wholly inside one core.
This file does not weigh the branches. It IDENTIFIES the four objects, by
walking the one class of pairs a sign-filtered generator can provably miss --
a class small enough to walk with no filter at all.

WHOSE VOCABULARY. The gap is written in the vocabulary of the generator's
FILTER -- the sign tests "n * (the other core) is nonnegative" that both S1
and S4 accept candidates on -- and not in the vocabulary of the divisor
SEARCH that finds n. That is the register the shortfall actually lives in:
the search now reaches every seed the box has, and what is left is a test
applied to what it reaches. Every count below is about the box walked; the
menu boxes are the sampling frame and nothing the mathematics names.

THE HAND-ATTACK, on paper before any engine code, in three parts.

PART ONE -- THE COVERAGE THEOREM. A sign-filtered generator can only miss a
pair with a SEED ON BOTH SIDES. Let cA and cB be the 0/1 cores of a size-2
and a size-6 menu, P = cA * cB, and suppose cB carries NO negative
Z-irreducible factor -- a non-seed, by explore_seed_shape.py's own definition
of the word. Two cases.
  (i) cA carries no negative factor either. Then every Z-irreducible factor of
  P is nonnegative, so every block built from two or more of them bipartitions
  into two nonnegative blocks and is NOT atomic. The only factorization is the
  full atom multiset, and the pair is unique. No collision to miss.
  (ii) cA carries a negative factor n, and its core is EXACTLY TWO Z-factors,
  so cA = p * n. That second hypothesis is load-bearing and it is the box's:
  the size-2 seeds of {2..32} are four menus carrying two cores, each two
  factors with exactly one negative (explore_descent26_wide.py finding 4). A
  size-2 core with more atoms admits a block whose cA-part is a proper
  sub-product T of them, and what the argument below then forces is
  pnonneg((prod T) * cB) for THAT sub-product -- still a sign test, but not
  necessarily one the divisor layers surface. Nothing in this box has that
  shape and nothing here proves it cannot elsewhere. Take any
  factorization of P into nonnegative atomic blocks and look at the block
  containing n. If that block also contains p it is cA * S for a sub-product S
  of cB's atoms, and it bipartitions as {cA}, {S} -- both nonnegative -- so it
  is non-atomic unless S is empty; and where S is empty the block is cA and
  the remaining blocks are forced to be the atoms of cB, which is the one
  factorization every such product already has. Otherwise the block is n * S
  with S a nonempty NONNEGATIVE sub-product of cB's atoms, and then
      n * cB = (n * S) * (cB / S)
  is a product of two nonnegative polynomials and is itself NONNEGATIVE.
So a second factorization at a non-seed cB forces pnonneg(n * cB), which is
exactly the predecessor's S1 test on the size-2 side. Every collision that
test misses has a seed on both sides. The size-2 seed side of {2..32} is four
menus carrying two cores (explore_descent26_wide.py finding 4), so the whole
missable class is 4 x 203 menu pairs -- and it is walked here with the counter
and no filter whatever, which is what makes the closure a measurement rather
than another sufficient condition.

PART TWO -- THE SPECIMEN, hand-derived and hand-checked before the engine, and
it does two jobs: it shows the missable class is INHABITED, and it shows the
cheap cut named for the residual was aimed at the wrong block. Take the atoms
    p1 = 1 + x0            n1 = 1 - x0 + x0^2
    p2 = 1 + x0 + x0^2     n2 = 1 - x0 + x0^2 + x1
n2 is linear in x1 with unit content, hence Z-irreducible. All four cross
products are nonnegative and 0/1:
    p1 n1 = 1 + x0^3                                        2 terms
    p2 n2 = 1 + x0^2 + x0^4 + x1 + x0 x1 + x0^2 x1          6 terms
    p1 n2 = 1 + x0^3 + x1 + x0 x1                           4 terms
    p2 n1 = 1 + x0^2 + x0^4                                 3 terms
so {p1 n1, p2 n2} and {p1 n2, p2 n1} are two factorizations of one 12-term 0/1
product, and each of the four blocks is atomic because its only bipartition
stands a negative atom alone. Both sign tests FAIL on it: n1 * (p2 n2) carries
-x0 and n2 * (p1 n1) carries -x0, so neither S1 nor S4 ever proposes the pair.
And the two cores are menus of the box: {2,16} and {2,6,8,12,24,32}.
  What that costs the cheap cut. The cut named at parking tests u = p1 * b for
b a negative factor of the size-6 core, at 2 or 3 terms. Here the small block
is n1 * p2 -- the size-2 core's NEGATIVE factor against the size-6 core's
NONNEGATIVE one, the mirror direction -- and p1 * n2 carries 4 terms, so that
cut returns nothing at the one object it was aimed at. Part one of the
predecessor's attack is untouched by this: its block of size 2 or 3 is the
3-term p2 n1, and it does mix.

PART THREE -- WHAT THIS DOES NOT REACH, named before the run so a closure
cannot be read as more than it is. (i) The theorem's hypothesis is that the
FLAGGED cores are exactly the seeds, which rests on close.py finding 1 (203
flagged) against the census's published 203 and is inherited, not reproved
here. (ii) The walk is the box's, and the box bounds menu elements and nothing
the mathematics names. (iii) Nothing leaves the menu frame; out-of-frame
objects are counted and not graded. (iv) The theorem is about the size-6 side
being a non-seed. It does NOT say the missable class is small in general --
only that it is small in a box whose size-2 seed side is four menus.

DESIGN, four stages.
 S0 THE POSITIVE CONTROL, run before any generated number is read.
    (a) THE MOVING LEG, on the frozen specimen of part two: the counter returns
        exactly 2 factorizations and they are the frozen blocks, while the
        predecessor's two sign tests -- n * cB over the size-2 core's negative
        factors, and nf * cA over every negative factor of the size-6 core --
        BOTH return nothing. A walk that keeps any sign filter fails here, and
        so does one whose counter cannot see a mixing block.
    (b) THE PILOT BOX IS REPRODUCED: over {2..24}, the generator's collisions
        together with this file's unfiltered walk give the published 8 in-frame
        objects, 7 at delta 1 and 1 at delta 2, the delta = 2 one being the
        published witness. Nothing below is read on a failure.
 S1 THE GENERATION, close.py's unchanged, per box: the three divisor layers on
    both sides, every candidate confirmed by the counter, and the flagged
    size-6 cores kept. Its in-frame object count is the baseline the closure is
    measured against, reproduced in this process and not quoted.
 S2 THE UNFILTERED WALK. Every flagged size-6 core against every size-2 menu of
    the box, straight through count_from_core with NO sign test, memoized on
    the core pair. By part one this contains every collision S1 can miss.
 S3 THE READING. Frame split and grading by the shared pipeline, then for each
    object S1 did not reach: its two factorizations, which core each block's
    atoms are drawn from -- the MIXING read, printed per block and not
    asserted -- and the parallel-edge criterion at every face, face form and
    generalized edge form both.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): both legs hold.
  PR1 (S2): the union reaches the census's published 22 in-frame objects and 4
      out of frame. The shortfall closes exactly, and the four new ones all
      carry a size-6 seed against a size-2 seed.
  PR2 (S3): every newly reached in-frame object is a MIXING one -- each of the
      two differing blocks draws at least one atom from each core.
  PR3 (S3): the face form of the criterion has 0 disagreements at the new
      objects and the generalized edge reading predicts delta at each, as at
      close.py's 157 readings.
  PR4 (S3): all four new objects read delta = 1. This is DERIVED and not
      guessed: the census publishes 21 at delta 1 and exactly one at delta 2
      over 22 objects, and the 18 S1 reaches already contain the delta = 2
      witness, so anything else contradicts the census.
  PR5: NOT PREDICTED. What the unfiltered walk costs against the 550.6 s scan
      that feeds it and the 4,126.3 s census it is a substitute for.

KILLS (observables with live failure modes; what each MEANS is weighed after
the run and never before).
  K0: any S0 leg fails. The instrument is broken and nothing below is read.
  K1: the union still falls short of 22 in-frame objects. Part one's theorem is
      false, or the flagged cores are not the seeds, and the residual survives
      a walk built to have no filter left to be wrong.
  K2: the union EXCEEDS 22 in frame. Then the census's own walk missed
      collisions and every count downstream of it is under suspicion.
  K3: some newly reached object is NOT mixing -- both differing blocks sit
      inside one core. The second branch of the predecessor's finding 4 is live
      and the leading branch was not the whole residual.
  K4: the criterion disagrees at any new object, in either half. The
      predecessor's K2 or K3 reopens on a population it was never read at.
  K5: any new object reads delta >= 2. It contradicts the census's isolation
      finding, and the two runs cannot both be right.
  K6: the two-differing-block recovery fails at a new object -- the {p n, q}
      shape does not cover what mixing produces, and the criterion has no p, n,
      q to be tested on there.

HONEST LIMITS carried into the reading, stated before the run. (i) The box
bounds menu ELEMENTS and nothing the mathematics names. (ii) The closure's
completeness is part one's theorem plus the inherited flagged = seeds
identification, not an exhaustive walk of the box. (iii) delta is exact only at
product dimension 2, where the hull enumerator applies. (iv) The criterion's
sufficient half remains an observation over the faces read, and a new
population is exactly what could break it.

FINDINGS (tiers per the standard naming scale; run record below).

0. ONE CORRECTION THE SLATE DOES NOT CARRY. It is left as frozen. S3 as
   designed registered its criterion legs unconditionally, so where the
   recovery finds no p, n, q there are no faces to read and three legs report
   PASS over an empty population -- and the same held of every S3 leg on the
   pilot box, whose fresh set is empty by construction. Both are checks that
   cannot move under the defect they guard, which is the species this file's
   own S0 is built around, committed in the reading rather than in the
   control. The legs are now registered only over a population that exists,
   and the pilot's real statement -- that the box has nothing in the missable
   class -- is S0b's, where it is checked against a published count.

1. THE SHORTFALL CLOSES EXACTLY, AND WITH NO FILTER LEFT TO BE WRONG
   (observation, exact). The generator's 18 in-frame objects plus the
   unfiltered walk over the missable class reach 22 in frame and 4 out --
   the census's published split, no fewer (K1 shut) and no more (K2 shut).
   The walk is 94,395 pairs over 60,479 distinct core pairs and returns 12
   collisions the generator did not have, which are 4 objects. What closed
   the gap is not a wider search: the scan feeding this run flags the same
   203 seeds and reaches the same 18 objects as its predecessor, in this
   process and not by quotation.

2. AND THE RESIDUAL IS MIXING, MEASURED RATHER THAN ELIMINATED
   (observation, exact; K3 shut). At every one of the four, both blocks of
   the second factorization draw an atom from EACH core -- read per block by
   matching atoms against the two cores' own factor lists, not inferred from
   the failure of anything else. The predecessor's finding 4 named this the
   leading branch on suit counts and wrote the second branch down rather
   than eliminating it; the second branch is not what these four are.

3. THE CHEAP CUT NAMED AT PARKING WAS AIMED AT THE MIRROR BLOCK, AND WOULD
   HAVE READ NULL (observation, exact). That cut tests u = p*b for p a
   nonnegative factor of a size-2 core and b a negative factor of a flagged
   core, at 2 or 3 terms. At every one of the four the small block is the
   OTHER pairing -- the size-2 core's NEGATIVE factor against the size-6
   core's NONNEGATIVE one -- and the companion block carries 4 terms, so the
   {3,4} split is what these wear and the cut sees neither half. The
   predecessor's part one is untouched: a 3-term block does exist at every
   one, and it does mix. What was wrong was the direction the cut read the
   mixing in, and a null there would have been read as evidence against the
   branch that is in fact the answer.

4. THE FOUR ARE ONE FAMILY AND THE BOX TRUNCATES IT (observation, exact;
   S4, which is NOT on the design above and was added after finding 2 was
   read). Every one pairs {2,16} against {2,8,32} u m*{1,2,4}, and the
   members inside {2..32} are exactly m = 3, 5, 6, 7 -- swept over every m
   from 2 to 16 rather than read off a hand-picked list, so the word EXACTLY
   is the sweep's and not the list's. Two conditions cut it and both bite:
   4m must land at or below 32, and the m-part must leave six DISTINCT
   elements, which m = 2, 4, 8 and 16 fail by folding into the base {2,8,32}.
   Carried past the bound, every m the sweep reaches collides in frame by the
   same mixing shape: 11 of the 15 swept leave six distinct elements and all
   11 collide, EVENS INCLUDED -- m = 6, 10, 12 and 14 -- so membership is no
   parity or squarefree condition, and 4 of the 11 sit inside the box. So the generator's
   shortfall is not four accidents at the edge of a box; it is one family
   the element bound cuts off, and it GROWS as the box widens. What that is
   not: a proof that the family is infinite, nor that it is the only one --
   four members past the bound is a spot check and the box is still the
   sampling frame.

5. THE CRITERION CANNOT BE STATED AT ANY OF THEM (observation; K6 FIRED at
   all four, and the file ends 62/63 and exits nonzero, which is the honest
   record of a kill rather than a fault to be tidied). The parallel-edge
   criterion is read off a recovery that writes a collision as {p*n, q}
   against {p, n*q} -- one block of each factorization sharing the factor p.
   The mixing shape has no such p: the four blocks are p1*n1, p2*n2, p1*n2,
   p2*n1 over two nonnegative and two negative atoms, and no block of one
   factorization divides a block of the other. So these four have no p, n, q
   for the criterion to be put to, and the corpus's "the criterion holds
   wherever it is put" acquires a boundary it did not have: there are
   in-frame objects at this size pair where it is not false but UNSTATED.
   Nothing here disturbs its readings at the 18 -- no face of a fresh object
   was read at all, and the legs that would have reported agreement are not
   registered.

6. THE COVERAGE THEOREM IS WHAT MADE THE WALK SMALL (property, proved; part
   one of the hand-attack, and its practical content is finding 1). A pair
   whose size-6 core carries no negative factor cannot collide unseen: the
   block holding the size-2 core's negative factor forces n * cB to be a
   product of nonnegatives, which is the predecessor's own S1 test. So the
   missable class is seed-against-seed, four menus by 203, and it is walked
   here with the counter and no sign test. The generator's completeness
   stops being a hypothesis controlled against published counts and becomes
   a theorem plus one walked exception.

7. THE PRICE (measurement; PR5, observable). The unfiltered walk costs
   171.0 s on top of the 545.6 s scan that supplies the flagged cores, and
   the two together run under a SIXTH of the 4,126.3 s census whose published
   COUNTS they now reproduce -- 22 in frame, 4 out, 21 at delta 1 and one at
   delta 2. Not object for object: the census's object LIST was never
   recorded, so set identity is not a thing either run can be checked against,
   and the agreement claimed here is of counts and of the delta split. The ratio is quoted to one figure on
   purpose: it moved between 5.72 and 5.76 across this file's runs on
   wall-clock jitter alone, so a second figure would be reporting the machine.
   Peak working set 133.0 MB.

HOW THE PREDICTIONS AND KILLS LANDED. PR0 held on both legs, the moving one
included: neither sign filter proposes the frozen specimen while its size-6
core IS flagged. PR1, PR2 and PR4 held as written. PR3 FAILED, and not in the
direction it was written for -- the criterion did not disagree, it could not
be reached, which finding 5 records and which PR3 had no way to express. PR5
was deliberately not predicted. K6 FIRED at all four objects; K0, K1, K2, K3,
K4 and K5 did not.

A NOTE ON WHAT THE FOUR ARE NOT. They are in frame, at product dimension 2,
and every one reads delta = 1, so nothing here touches the isolation of the
delta = 2 witness or the confinement -- the census's split of 21 and 1 over 22
is reproduced exactly. The closure is a statement about a GENERATOR and its
filter, not about the mathematics the generator was built to survey.

RUN RECORD (this file, under memwatch.py at the 512MB default). Pilot and wide
in one process: 62/63 checks, 844.4 s wall, peak working set 133.0 MB, peak
commit 125.8 MB. The pilot leg is a full control and not a warm-up: it
reproduces the published 8 in-frame objects and the published witness, and its
unfiltered walk returns nothing fresh, which is the box having nothing in the
missable class rather than the walk being idle. Four earlier runs of this file
returned the same 22 objects, the same four fresh ones and the same K6 firing;
what changed across them was finding 0's correction, the addition of S4, and
S4's own sweep replacing a hand-picked list of m.
"""

import os
import sys
import time
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import X, check, CHECKS
from explore_descent_hunt import core_of, factorizations
from explore_descent26_why import (PILOT, WIDE, menu_core, pmul, pnonneg,
                                   splits_of, hidden_negatives, as_dict,
                                   grade, nonmono, object_key)
from explore_menu_faces import exps, face_support, induced, weight_box
from explore_descent26_close import (generate, movers_of, tri_splits,
                                     all_negative_factors, split_of_collision,
                                     edge_dirs)

# ============================================ the frozen specimen (part two)
SPEC_A = (2, 16)
SPEC_B = (2, 6, 8, 12, 24, 32)
SPEC_BLOCKS = (
    # {p1 n1, p2 n2} -- the menu pair's own factorization
    (1 + X[0] ** 3,
     1 + X[0] ** 2 + X[0] ** 4 + X[1] + X[0] * X[1] + X[0] ** 2 * X[1]),
    # {p1 n2, p2 n1} -- the mixing one, which no sign test proposes
    (1 + X[0] ** 3 + X[1] + X[0] * X[1],
     1 + X[0] ** 2 + X[0] ** 4),
)


def blockset(facs):
    """A factorization as a comparable set of expanded blocks."""
    return frozenset(sympy.srepr(sympy.expand(b)) for b in facs)


def stage0():
    print("\n=== S0  the positive control ===")
    gA, cA = core_of(SPEC_A)
    gB, cB = core_of(SPEC_B)
    n, facs, g = factorizations(cA, cB, gA, gB)
    print(f"  specimen {set(SPEC_A)} x {set(SPEC_B)} -> {n} factorizations")
    for f in facs:
        print("      " + "  *  ".join(str(sympy.factor(b)) for b in f))
    check("S0a the specimen factors in exactly two ways", n == 2)
    check("S0a and they are the two frozen block sets",
          {blockset(f) for f in facs} == {blockset(b) for b in SPEC_BLOCKS})
    P = sympy.Poly(sympy.expand(sympy.prod(facs[0])), *g)
    print(f"  specimen product: {len(P.monoms())} terms,"
          f" max coefficient {max(abs(c) for c in P.coeffs())}")
    check("S0a the specimen is IN FRAME -- 12 terms, all coefficients 1",
          len(P.monoms()) == 12 and max(abs(c) for c in P.coeffs()) == 1)
    # the moving half: both sign filters must return nothing at all
    coreA, coreB = menu_core(SPEC_A), menu_core(SPEC_B)
    s1 = [n for n, _ in movers_of(coreA) if pnonneg(pmul(n, coreB))]
    s4 = [n for n in all_negative_factors(coreB) if pnonneg(pmul(n, coreA))]
    print(f"  the predecessor's filters on it: S1 proposes {len(s1)},"
          f" S4 proposes {len(s4)}")
    check("S0a THE MOVING LEG -- the S1 sign test proposes the pair on NO"
          " negative factor of the size-2 core", not s1)
    check("S0a THE MOVING LEG -- the S4 sign test proposes it on NO negative"
          " factor of the size-6 core", not s4)
    check("S0a and the size-6 core IS flagged, so the shortfall is the filter"
          " and not the search", bool(movers_of(coreB)))


# ================================================= S2  the unfiltered walk
def unfiltered_walk(box, label, flagged, seen):
    """Every flagged size-6 core against every size-2 menu, no sign test.

    By part one this contains every collision a sign-filtered generator can
    miss. The counter is the only filter; memoization is on the CORE pair,
    which is the convention-free unit and the one the census counts in.
    """
    print(f"\n=== S2  the unfiltered walk [{label}] ===")
    t0 = time.time()
    menus2 = [tuple(c) for c in combinations(box, 2)]
    cores2 = {A: core_of(A) for A in menus2}
    memo, found, npair = {}, [], 0
    for i, B in enumerate(flagged):
        gB, cB = core_of(B)
        kB = tuple(sorted(sympy.srepr(f) for f in cB))
        for A in menus2:
            gA, cA = cores2[A]
            npair += 1
            key = (tuple(sorted(sympy.srepr(f) for f in cA)), kB)
            if key not in memo:
                memo[key] = factorizations(cA, cB, gA, gB)[0]
            if memo[key] > 1 and (A, B) not in seen:
                n, facs, g = factorizations(cA, cB, gA, gB)
                found.append(dict(A=A, B=B, n=n, facs=facs, gens=g, old=False))
        if (i + 1) % 50 == 0:
            print(f"    ... {i+1}/{len(flagged)} flagged cores,"
                  f" {len(found)} fresh   [{time.time()-t0:.1f}s]")
    tw = time.time() - t0
    print(f"  [{label}] {npair} pairs over {len(memo)} distinct core pairs;"
          f" {len(found)} collisions S1 did not already have   [{tw:.1f}s]")
    return found, tw


# ======================================================= S3  the reading
def which_core(block, cA, cB):
    """(from A, from B) -- how many of a block's atoms each core supplies.

    A block is a product of Z-irreducibles; each is matched against the two
    cores' own factor lists, consumed once so a repeated factor cannot be
    counted twice on the same side.
    """
    _, atoms = sympy.factor_list(block)
    flat = []
    for f, m in atoms:
        if f in X:
            continue
        for _ in range(m):
            flat.append(sympy.expand(f))
    left, right = list(cA), list(cB)
    na = nb = 0
    for f in flat:
        hit = next((u for u in left if sympy.expand(f - u) == 0), None)
        if hit is not None:
            left.remove(hit)
            na += 1
            continue
        hit = next((u for u in right if sympy.expand(f - u) == 0), None)
        if hit is not None:
            right.remove(hit)
            nb += 1
    return na, nb, len(flat)


def read_new(objs, prior, label):
    """Grade and read every object the generator did not reach."""
    print(f"\n=== S3  the objects the generator misses [{label}] ===")
    fresh = {k: rs for k, rs in objs.items() if k not in prior}
    print(f"  {len(objs)} in-frame objects, {len(prior)} of them reached by"
          f" the generator, {len(fresh)} fresh")
    if not fresh:
        # No leg below is registered over an empty population. That the box
        # has nothing in the missable class is a real statement and it is
        # S0b's, checked there against the published object count; restating
        # it here as four passes over no objects would put four checks in the
        # file that no defect can move.
        print("  nothing fresh: no S3 leg is registered, the box having"
              " nothing in the missable class (S0b owns that statement)")
        return fresh
    faces = agree = sep_tot = 0
    bad_nec, bad_suf, nomix, badpred, recov = [], [], [], [], []
    for key, rs in sorted(fresh.items()):
        r = rs[0]
        g = r["gens"]
        _, cA = core_of(r["A"])
        _, cB = core_of(r["B"])
        print(f"\n  OBJECT {set(r['A'])} x {set(r['B'])}   {len(rs)} suit(s)"
              f"   dim {r['dim']}  delta {r['delta']}")
        mixed = []
        for j, f in enumerate(r["facs"]):
            parts = []
            for b in f:
                na, nb, tot = which_core(b, cA, cB)
                parts.append(f"[{len(exps(b, g))}t A:{na} B:{nb}]")
                if j == 1:
                    mixed.append(na > 0 and nb > 0)
            print(f"      factorization {j}: " + "  ".join(parts))
            print("        " + "  *  ".join(str(sympy.factor(b)) for b in f))
        if not all(mixed):
            nomix.append(key)
        p, n, q, spect = split_of_collision(r)
        if p is None:
            recov.append(key)
            continue
        pts = exps(sympy.expand(sympy.prod(r["facs"][0])), g)
        seen, edge = {}, False
        for w in weight_box(len(g), r["radius"]):
            seen.setdefault(frozenset(face_support(pts, w)), w)
        for _, w in seen.items():
            sep = induced(r["facs"][0], g, w) != induced(r["facs"][1], g, w)
            pred = nonmono(n, g, w) and (nonmono(p, g, w) or nonmono(q, g, w))
            faces += 1
            sep_tot += sep
            agree += (sep == pred)
            if sep and not pred:
                bad_nec.append((key, w))
            if pred and not sep:
                bad_suf.append((key, w))
            edge = edge or pred
        if (1 if edge else r["dim"]) != r["delta"]:
            badpred.append(key)
        print(f"      recovered  p[{len(exps(p, g))}t edges {edge_dirs(p, g)}]"
              f"  q[{len(exps(q, g))}t edges {edge_dirs(q, g)}]"
              f"  n[{len(exps(n, g))}t]  spectators {len(spect)}"
              f"  criterion {1 if edge else r['dim']}")
    print(f"\n  faces examined at the fresh objects: {faces},"
          f" {sep_tot} separating; criterion agreed at {agree}")
    check(f"S3 [{label}] the two-differing-block recovery found p, n and q at"
          " every fresh object (K6)", not recov)
    check(f"S3 [{label}] every fresh object MIXES -- each block of the second"
          " factorization draws an atom from each core (K3)", not nomix)
    # The criterion legs are registered ONLY where a face was actually read.
    # Where the recovery fails there is no p, n, q, hence no reading at all,
    # and a leg that passes over an empty population is a check that cannot
    # move under the defect it guards -- the species this file's own S0 is
    # built to avoid, and it would be the loudest place to commit it.
    if faces:
        check(f"S3 [{label}] no face separates where the criterion forbids it"
              " (K4)", not bad_nec)
        check(f"S3 [{label}] no face fails to separate where the criterion"
              " allows it (K4)", not bad_suf)
        check(f"S3 [{label}] the generalized edge reading predicts delta at"
              " every fresh object (K4)", not badpred)
    else:
        print("  the criterion is UNREACHABLE at every fresh object: with no"
              " p, n, q recovered there is no face reading to agree or"
              " disagree, so no K4 leg is registered here.")
        check(f"S3 [{label}] the criterion is unreachable at EVERY fresh"
              " object and not at some -- one mechanism, not two",
              len(recov) == len(fresh))
    check(f"S3 [{label}] no fresh object reads delta >= 2 (K5)",
          all(rs[0]["delta"] == 1 for rs in fresh.values()))
    return fresh


# ============= S4  the family (NOT on the design; added after S3 was read)
FAMILY_M = tuple(range(2, 17))   # swept, never hand-picked: see S4
FAMILY_BASE = (2, 8, 32)


def stage4():
    """Are the four fresh objects one family, truncated by the element bound?

    Every one of them pairs {2,16} against a size-6 menu that reads
    {2,8,32} u m*{1,2,4} -- m = 3, 5, 6 and 7, which are exactly the m whose
    largest element 4m lands at or below 32. If the shape collides at m past
    the bound too, the generator's shortfall is one family the box truncates
    and not four accidents, and it grows with the box rather than closing.
    Predicted before the stage was run: every listed m collides in frame with
    the same mixing shape, and exactly m = 3, 5, 6, 7 sit inside {2..32}.
    """
    print("\n=== S4  the family {2,8,32} u m*{1,2,4} ===")
    A = (2, 16)
    gA, cA = core_of(A)
    inbox, coll, mix, eligible = [], [], [], []
    for m in FAMILY_M:
        B = tuple(sorted(set(FAMILY_BASE) | {m, 2 * m, 4 * m}))
        if len(B) != 6:
            print(f"  m = {m:2d}: {set(B)} is not six distinct elements")
            continue
        eligible.append(m)
        gB, cB = core_of(B)
        n, facs, g = factorizations(cA, cB, gA, gB)
        P = sympy.Poly(sympy.expand(sympy.prod(facs[0])), *g)
        frame = len(P.monoms()) == 12 and max(abs(c) for c in P.coeffs()) == 1
        mixed = False
        if n == 2:
            second = facs[1] if blockset(facs[1]) != blockset([
                sympy.expand(sympy.prod(cA)), sympy.expand(sympy.prod(cB))
            ]) else facs[0]
            mixed = all(which_core(b, cA, cB)[0] > 0
                        and which_core(b, cA, cB)[1] > 0 for b in second)
        print(f"  m = {m:2d}: max element {max(B):3d}"
              f"  {'IN BOX ' if max(B) <= 32 else 'outside'}"
              f"  factorizations {n}  in frame {frame}  mixing {mixed}")
        if max(B) <= 32:
            inbox.append(m)
        if n == 2 and frame:
            coll.append(m)
        if mixed:
            mix.append(m)
    # Against the ELIGIBLE m and not against FAMILY_M: the swept range holds m
    # that fold into the base and never form a menu at all, and comparing to
    # the raw range would fail on bookkeeping while comparing to `coll` itself
    # would be unfalsifiable. Eligibility is the six-distinct-elements test and
    # nothing about collisions.
    print(f"  swept m = {FAMILY_M[0]}..{FAMILY_M[-1]}: {len(eligible)} leave"
          f" six distinct elements, {len(coll)} of those collide in frame,"
          f" {len(inbox)} sit inside the box")
    check("S4 every member of the family that forms a menu at all collides in"
          " frame, inside the box and past it", set(coll) == set(eligible))
    check("S4 and every one of them collides by MIXING", set(mix) == set(coll))
    check("S4 the members inside {2..32} are exactly m = 3, 5, 6, 7 -- the"
          " four fresh objects, so the shortfall is the family truncated",
          inbox == [3, 5, 6, 7])


# ==================================================================== driver
def run_box(box, label):
    print(f"\n=== S1  the generation [{label}]  box {{2..{max(box)}}} ===")
    found, _, flagged, _ = generate(box, label)
    seen = {(r["A"], r["B"]) for r in found}
    s1in = {object_key(r) for r in found
            if len(sympy.Poly(sympy.expand(sympy.prod(r["facs"][0])),
                              *r["gens"]).monoms()) == 12}
    fresh, tw = unfiltered_walk(box, label, flagged, seen)
    found += fresh
    objs, outobj = grade(found, label)
    prior = s1in & set(objs)
    print(f"  [{label}] S1 reached {len(prior)} in-frame objects; with the"
          f" unfiltered walk the union stands at {len(objs)}")
    newobj = read_new(objs, prior, label)
    return objs, outobj, prior, newobj, len(flagged), tw


def main():
    t0 = time.time()
    stage0()
    objs, _, prior, _, _, _ = run_box(PILOT, "pilot {2..24}")
    d2 = [rs[0] for rs in objs.values() if rs[0]["delta"] >= 2]
    check("S0b the pilot box is reproduced entirely: 8 in-frame objects,"
          " 7 at delta 1 and 1 at delta 2", len(objs) == 8 and len(d2) == 1)
    check("S0b the pilot delta=2 object is the published witness",
          len(d2) == 1 and
          {tuple(sorted(d2[0]["A"])), tuple(sorted(d2[0]["B"]))} ==
          {(2, 3), (3, 4, 8, 9, 18, 24)})
    check("S0b and the generator already reached all 8, so the pilot box has"
          " nothing in the missable class", len(prior) == 8)
    if any(not v for _, v in CHECKS):
        print("\nPILOT CONTROL FAILED -- the wide box is not walked.")
        for n, v in CHECKS:
            if not v:
                print(f"  FAIL {n}")
        return 1
    if "--pilot" not in sys.argv:
        wobjs, woutobj, wprior, wnew, nflag, tw = run_box(WIDE, "wide {2..32}")
        wd2 = [rs[0] for rs in wobjs.values() if rs[0]["delta"] >= 2]
        check("S1 the wide box flags all 203 published size-6 seeds",
              nflag == 203)
        check("S1 the generator's in-frame baseline is the published 18",
              len(wprior) == 18)
        check("S2 the union reaches the census's 22 in-frame objects -- no"
              " fewer (K1)", len(wobjs) >= 22)
        check("S2 and no more (K2)", len(wobjs) <= 22)
        check("S2 the union reaches the census's 4 out-of-frame objects",
              woutobj == 4)
        check("S2 exactly four objects are fresh", len(wnew) == 4)
        check("S3 the delta split is the census's: 21 at delta 1, one at 2",
              len(wd2) == 1)
        stage4()
        print(f"\n  PR5 the unfiltered walk of the wide box: {tw:.1f} s,"
              f" against the 550.6 s scan that feeds it and the 4,126.3 s"
              f" census it substitutes for")
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time()-t0:.1f}s")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
