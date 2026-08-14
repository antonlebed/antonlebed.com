"""The generator's last four: putting the parallel-edge criterion to every object.

THE QUESTION. explore_descent26_why.py derived a criterion that DERIVES the
descent dimension delta rather than correlating with it -- a face separates
only if in_w(n) is non-monomial and at least one of in_w(p), in_w(q) is -- and
checked it at 231 faces over 18 distinct objects with 0 disagreements. But its
generator reaches 18 of the wide box's 22 published in-frame objects and none
of the 4 out-of-frame ones, so four in-frame objects have never had the
criterion put to them, and that is the whole distance between finding 2 and the
word "every". This file closes the generator and grades what it reaches.

WHOSE VOCABULARY. The gap is written in the vocabulary of the GENERATOR -- 0/1
divisors, quotients, Minkowski summands -- and not in the criterion's. That is
the right register for it: the criterion is a statement about faces and no
missing object can weaken it, while the shortfall is a statement about a SEARCH
and is repaired inside the search. Every count below is about the box walked;
the menu boxes are the sampling frame and nothing the mathematics names.

THE HAND-ATTACK, on paper before any engine code, in three parts. It settles
what the widening covers and, more usefully, what it does NOT.

PART ONE -- WHY A BLOCK OF SIZE 2 OR 3 ALWAYS EXISTS, AND WHY THAT IS THE
WHOLE SEARCH. A factorization here is a partition of the product's Z-irreducible
multiset into blocks that are nonnegative and semiring-atomic (the counter's own
definition). Take a walked pair (A, B) of menu sizes 2 and 6 whose product is
non-unique, and look at the SECOND factorization's block sizes. For nonnegative
0/1 factors term counts multiply, so those sizes are a factorization of 12 into
parts >= 2: {2,6}, {3,4}, {2,2,3}, or the single part {12}. The last says the
product is atomic, which contradicts the first factorization having two blocks.
So EVERY second factorization carries a block u of size 2 or 3.

Assume that block does not mix nonconstant factors drawn from both cores -- the
same assumption part one of the predecessor made, and it is discharged the same
way for size 3 as for size 2, since a product of two nonnegative 0/1 factors
carries at least 4 terms. Then u divides ONE core. Write that core as u*n and
call the other core c. The remaining blocks partition the rest, whose product is
exactly n*c, so the second factorization exists precisely when n*c is
nonnegative -- and that is true whether the rest is one block ({2,6}, {3,4}) or
two ({2,2,3}), since a product of nonnegative blocks is nonnegative. So the test
"n * (the other core) is nonnegative" is EXACT for this shape, and the 4-term
block of a {3,4} split is never searched for: it is c*n, derived.

The predecessor searched u only at size 2, on both sides, plus finding 0's patch
for a negative factor sitting strictly inside a nonnegative trinomial QUOTIENT.
The one shape that leaves uncovered is u of size 3 with a NEGATIVE quotient --
a core factoring as two 3-term pieces with no binomial divisor at all. That is
the widening, and by the paragraph above it completes the search under the
mixing assumption. Note the quotient must be negative or nothing is new: a
0/1 trinomial divisor with a nonnegative quotient forces that quotient to be a
0/1 binomial by the term-count law, which the binomial search already finds.

PART TWO -- THE CANDIDATE RESTRICTION, so the widening is a search and not a
census. Newt(f*g) = Newt(f) + Newt(g) for any polynomials over a domain
(Ostrowski) -- nonnegativity is not needed -- so Newt(u) is a Minkowski summand
of Newt(C), and every edge direction of a summand is an edge direction of the
sum. A 0/1 trinomial's polytope is a triangle or a segment; in both cases all
of its edge directions are parallel to differences of two support vectors of C.
A summand also FITS inside the sum, so u's extent along each coordinate is
bounded by C's.

That gives the enumeration. Fix the weight w with strictly positive weights
(1, 64, 64^2, ...), which is injective on this box's exponent vectors, so the
w-minimal support vector of C is a unique vertex, and translate u so its own
w-minimal exponent is 0. Then u = {0, a, b} with a and b both w-POSITIVE, and
a, b and b-a are each parallel to one of the 15 support differences and each
within C's coordinate extent. Because that weight is injective, packing an
exponent vector into a single integer is exactly evaluating it, so the whole
test is integer subtraction against a precomputed set -- no gcd inside the pair
loop. The collinear case rides along: for u = {0, a, 2a} the segment's only
edge is [0,2a] and a is a multiple of the same primitive direction.

PART THREE -- WHAT THE WIDENING STILL DOES NOT REACH, named before the run so a
clean result cannot be read as completeness. (i) The MIXING assumption above: a
size-2 or size-3 block that is a product of a negative factor of one core with a
negative factor of the other is invisible to a search that divides one core at a
time. (ii) A core whose every nontrivial 0/1 divisor is trivial -- both Z-factors
negative -- has no nonnegative 0/1 divisor of any size, so no divisor search of
any width flags it; the predecessor's corpus already knows that shape (a
two-factor seed core with both factors negative) and knows it is unique against a
single-factor partner, which is a statement about the PARTNER and not about this
search. Neither is repaired here, and if the wide box still falls short of 22
these are where to look.

WHAT THE CRITERION NEEDS GENERALIZED, and it is only the reading. The FACE form
-- a face separates exactly when in_w(n) is non-monomial and at least one of
in_w(p), in_w(q) is -- is stated over arbitrary p and q and is untouched. The
EDGE form is what assumed binomials: in_w(p) non-monomial was read as "w is
perpendicular to dir(p)", one direction. Where the recovered p or q is a
TRINOMIAL its polytope has up to three edge directions, so the reading becomes
DELTA = 1 EXACTLY WHEN Newt(n) HAS AN EDGE PARALLEL TO AN EDGE OF Newt(p) OR OF
Newt(q), which is the same statement with "dir" replaced by "edge directions"
and reduces to the published one when both are binomials. The run reads the
face form directly off a weight scan, so the generalization changes what is
PRINTED and not what is tested.

THE TWO CONTROL SPECIMENS, hand-verified before the engine and frozen here.
Each is a 6-term 0/1 core with a 0/1 trinomial divisor of negative quotient and
NO 0/1 binomial divisor whatever -- so the predecessor's split search and its
finding-0 patch both see nothing at all, and a control built on them MOVES under
the very defect it guards.
  COLLINEAR:  C = 1 + x + x^2 + x^3 + x^4 + x^8
              = (1 + x + x^2) * (1 + x^3 - x^5 + x^6).
  TRIANGLE:   C = 1 + y + x^2 y + x y^3 + x^2 y^3 + x^3 y^2
              = (1 + y + x y) * (1 - x y + x^2 y + x y^2),
  the second checked by hand: the three cross terms x y, x y^2 and x^2 y^2 each
  cancel exactly once. The triangle one is the load-bearing half. A collinear
  specimen alone would leave the two-free-directions branch of the enumeration
  unguarded, which is the branch the widening exists to add.
Neither is a menu of either box -- scaled to integer elements they leave {2..32}
-- which costs nothing, since the search operates on cores and not on menus.

DESIGN, four stages.
 S0 THE POSITIVE CONTROL, run before any generated number is read.
    (a) THE MOVING CONTROL. On both frozen specimens: the binomial divisor
        search returns nothing, the negative-split search returns nothing and
        the finding-0 patch returns nothing, while the trinomial split search
        returns exactly the published (u, n). Fails outright if the new layer
        is absent or wrong.
    (b) THE RESTRICTION LOSES NOTHING. Over every size-6 menu of {2..12}, the
        restricted candidate enumeration plus exact division finds exactly the
        set of 0/1 trinomial divisors that sympy's factorization finds by
        multiplying out sub-multisets of the Z-factors. An implementation that
        drops candidates the proof allows dies here rather than in the box.
    (c) THE NONNEGATIVE-QUOTIENT CLAUSE. Every 0/1 trinomial divisor with a
        nonnegative quotient found in (b) has a 0/1 BINOMIAL quotient, and its
        core is already flagged by the predecessor's search -- so restricting
        the new layer to negative quotients discards nothing.
    (d) THE PILOT BOX IS REPRODUCED ENTIRELY: {2..24} yields 8 in-frame objects,
        7 at delta 1 and 1 at delta 2, and the delta = 2 object is the published
        witness {3,4,8,9,18,24} x {2,3}. Nothing below is read on a failure.
 S1 THE GENERATION, per box, the predecessor's with the layer added on BOTH
    sides: every size-2 and every size-6 core is scanned for 0/1 binomial
    divisors with a negative quotient, for negative factors hidden inside a
    nonnegative trinomial quotient, and now for 0/1 TRINOMIAL divisors with a
    negative quotient. Each negative factor n is paired against every menu of
    the other size and kept when n * (that core) is nonnegative. Every candidate
    is CONFIRMED with count_from_core, so no collision rests on the generator.
    Deduped on the menu pair, collapsed to OBJECTS by core pair, and the flagged
    core count is reported per LAYER so the widening's own contribution is
    visible rather than inferred from the total.
 S2 THE FRAME AND THE GRADING, unchanged: the 12-term frame split, then dim and
    delta per in-frame object, with the sampled face reading checked against the
    exact hull enumeration at every dimension-2 object.
 S3 THE CRITERION, at both levels, over every object the widened generator
    reaches. Face by face: does "this face separates" agree with the face form?
    Object by object: does the generalized edge reading predict delta? Then the
    table, with the four columns the generalization needs -- the term counts of
    the recovered p and q, and the edge-direction sets of both -- so a row whose
    q is a trinomial is legible as such rather than hidden behind a "dir".
    The objects the predecessor did NOT reach are printed apart and named.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): all four legs hold.
  PR1 (S1): the widened generator closes the gap on the wide box -- 22 in-frame
      objects and 4 out of frame, against the predecessor's 18 and 0 -- and
      flags all 203 published size-6 seeds against its 199.
  PR2 (S3, face form): 0 disagreements at every face of every object of both
      boxes, as at the predecessor's 231 readings.
  PR3 (S3, object form): the generalized edge reading predicts delta at every
      in-frame object of both boxes. The four newly reached objects read delta
      = 1 -- which the published census already says, so what is predicted is
      that the CRITERION derives it, not that the number comes out that way.
  PR4: NOT PREDICTED. What the widened scan costs against the predecessor's
      213.3 s and against the 4,126.3 s census. A measurement, and the point of
      taking it is that it prices every later run of this question.
  PR5: NOT PREDICTED. Whether the recovered p or q at a newly reached object is
      a trinomial at all. The {3,4} shape is what the widening was built for,
      but a core reached by a trinomial divisor can still present a binomial
      block in its second factorization, and predicting which would be a guess
      dressed as a design.

KILLS (observables with live failure modes; what each MEANS is weighed after the
run and never before).
  K0: any S0 leg fails. The instrument is broken and nothing below is read.
  K1: the wide box still falls short of 22 in-frame or 4 out-of-frame objects.
      The residual is part three's, and which of its two shapes it is becomes
      the next question rather than this one's answer.
  K2: some face separates where the criterion forbids it -- the PROVED half is
      wrong and the criterion dies outright.
  K3: some face fails to separate where the criterion allows it. The sufficient
      half is wrong; the criterion survives as a lower bound on delta and stops
      being a criterion. This kill has more room than it did: q may now be a
      trinomial, whose initial form is non-monomial on strictly more weights.
  K4: the generalized edge reading misgrades any in-frame object.
  K5: the pilot box is not reproduced. The widening broke something that worked.
  K6: the two-differing-block recovery fails at some object -- the {p*n, q}
      against {p, n*q} shape does not cover what the widening reached, and the
      criterion has no p, n, q to be tested on there.

HONEST LIMITS carried into the reading, stated before the run. (i) The boxes
bound menu ELEMENTS and nothing the mathematics names. (ii) Completeness of the
generator rests on part three's two named assumptions and its warrant is
agreement with published populations, not a proof. (iii) The criterion's
sufficient half remains an observation over the faces read, and widening the
population is exactly what could break it. (iv) Nothing here leaves the menu
frame: a 0/1 product with a factor carrying a coefficient above 1 is outside
every statement below, and the out-of-frame objects are counted and not graded.

FINDINGS (tiers per the standard naming scale; run record below).

0. ONE CORRECTION THE SLATE DOES NOT CARRY. It is left as frozen. S0c was
   written to check that a core with a trinomial divisor of NONNEGATIVE
   quotient "is already flagged by the predecessor's search", and that is
   false and ought to be: such a core is a product of two nonnegative 0/1
   pieces and is typically no seed at all, so there is nothing to flag. The
   load-bearing statement, which is what the leg now checks, is that the split
   contributes no negative factor OF ITS OWN -- and where the trinomial itself
   carries one, finding 0's patch already flags the core. 8 such splits over
   {2..12}, all 8 with a 0/1 binomial quotient, all 8 accounted for.

1. THE SEED GAP IS CLOSED, AND EXACTLY (observation, exact). The trinomial
   layer takes the wide box from the predecessor's 199 flagged size-6 cores to
   203 -- the published seed count of {2..32}, reached in full -- and the four
   it adds are reached by that layer ALONE, neither the binomial split search
   nor finding 0's patch seeing them. The pilot box moves by nothing at all:
   55 flagged cores and 0 reached by the new layer, so the shape the widening
   exists for is absent from {2..24} entirely.

2. AND WHAT THE FOUR SEEDS CARRY IS THE OUT-OF-FRAME HALF, WHICH REFUTES THE
   SUSPICION THAT NAMED THEM (observation, exact). The predecessor recorded
   that "the two 4s are the same 4 seeds if each carries one object of each
   kind, which is a suspicion and not a measurement". Measured: the four seeds
   carry the four OUT-OF-FRAME objects and not one of the four missing
   in-frame ones. The walk goes from 18 in-frame + 0 out to 18 in-frame + 4
   out. So the two 4s were never the same 4, and the in-frame shortfall was
   never a seed-side gap -- it survives a search that now reaches every seed
   the box has.

3. AND IT IS NOT A WRONG-FACTOR ARTIFACT EITHER (observation, exact; S4, which
   is NOT on the design above and was added after finding 2 was read). Flagging
   a core asks whether it HAS a negative factor; pairing needs the RIGHT one,
   and the two come apart wherever a core carries more than one. So all 203
   flagged cores were factored outright and EVERY negative factor paired
   against every one of the 465 size-2 partners: 204 negative factors in all,
   2,955 candidate pairs, and 0 new collisions. Every S1 collision seeded by a
   flagged core is reached again, so the exhaustive enumeration contains the
   quotient one and adds nothing. The size-2 side needs no such stage: the box
   has 4 size-2 seeds carrying 2 cores between them, (1+x0)(1-x0+x0^2) and
   (x0+x1)(x0^2-x0x1+x1^2), and each core has exactly ONE negative Z-factor,
   which the binomial split search finds.

4. SO THE RESIDUAL IS A PAIRING HYPOTHESIS AND NOT A SEED GAP, WITH MIXING
   THE LEADING BRANCH OF TWO (observation; the argument is part one of the
   hand-attack run backwards). Part one proves every second factorization carries a block of
   size 2 or 3, and that IF that block divides one core the test "n * (the
   other core) is nonnegative" is EXACT -- exact, not sufficient, since the
   remaining blocks' product is that quantity whether they are one block or
   two. Findings 1 and 3 exhaust both sides of the hypothesis: every core that
   carries a negative factor is flagged, and every negative factor of every
   flagged core is paired. What is left is the hypothesis itself -- and one
   branch of the block argument that neither stage covers, named here rather
   than swept into the leading answer. LEADING: the block MIXES, drawing a
   factor from each core with at least one negative, the one case the
   term-count law does not forbid, which is part three's residual (i). SECOND,
   and it survives because both stages filter to NEGATIVE quotients: where
   u divides cB with a NONNEGATIVE complement while cB still carries a negative
   atom deeper in, the differing block can sit wholly inside one core, and
   neither the quotient test nor S4's nf * (the whole other core) is shaped to
   find it. What makes mixing the leading half is the suit counts and not an
   argument: a core factoring non-uniquely on its own would collide against
   EVERY one of the 465 partners, and the widest object here wears 10. That is
   evidence, not a proof, and it is why the second branch is written down
   instead of eliminated.
   The cheap next cut follows from the same sentence and needs no census: the
   size-2 side supplies only two cores and their nonnegative factors are
   1 + x0 and x0 + x1, so for each flagged core's negative factor b, test
   whether (1+x0)*b or (x0+x1)*b is a nonnegative 0/1 polynomial of 2 or 3
   terms, and then whether the complementary product is nonnegative. 406
   tests. The second branch is cheaper still and rides along: count the
   factorizations of each of the 203 flagged cores ALONE, which decides whether
   any core is internally non-unique -- the cheap probe of that branch and not
   a settlement of it, since a differing block inside one core can still draw
   on the partner's atoms.
   SETTLED, and not by either probe named here (explore_descent26_mix.py): the
   residual is the MIXING branch at all four objects, reached by walking the
   seed-against-seed class with no sign filter at all. The cut named just
   above reads the mixing in the mirror direction -- these four pair the
   size-2 core's NEGATIVE factor with the size-6 core's nonnegative one across
   a {3,4} split -- so it would have returned a null at the objects it was
   aimed at.

5. THE CRITERION HOLDS WHEREVER IT IS PUT -- WHEREVER IT CAN BE STATED, the
   scope this headline did not know it had (explore_descent26_mix.py: the four
   objects it adds share no factor across their two factorizations, so the
   recovery finds no p, n, q and the criterion is UNSTATED there rather than
   false; the readings below are untouched) -- AND ITS EDGE FORM NEEDED
   GENERALIZING TO SAY SO (rule, proved in its necessary half; 157 face
   readings over the wide box's 18 objects, 39 of them separating, 0
   disagreements in either direction, K2 K3 K4 all shut). The face form is
   reproduced to the digit. What changed is the READING: at 17 of the 18
   in-frame objects the recovered q is a TRINOMIAL and not a binomial -- at 15
   of them x0^2 + x0 + 1 and at the two seeded by {8,27} its HOMOGENIZATION
   x0^2 + x0 x1 + x1^2, which is the same distinction the falsified
   collinearity claim turned on -- so "w perpendicular to dir(q)" names one
   direction where the object has three. The generalized form -- DELTA = 1 EXACTLY WHEN Newt(n)
   HAS AN EDGE PARALLEL TO AN EDGE OF Newt(p) OR OF Newt(q) -- predicts delta
   at every one, and reduces to the published binomial form at the witness,
   which is the single row where p and q are both binomials and the only one
   with no spectator. The predecessor computed a single dir(q) from the first
   of three support differences at exactly those 17 rows; it never printed the
   value and nothing downstream read it, so the published criterion is
   untouched and only its statement was narrower than its own population.

6. THE PRICE (measurement; PR4, observable). The widened scan of the wide box
   costs 550.6 s against the predecessor's 213.3 s -- 2.6x for the layer --
   and remains 7.5x under the 4,126.3 s census it replaces. S4 adds 1.4 s of
   pairing and 16.5 s of confirmation on top, so exhausting the negative
   factors of every seed in the box is free beside the scan that finds them.
   Peak working set 131.4 MB.

HOW THE PREDICTIONS AND KILLS LANDED. PR0 held on all four legs, after finding
0's correction to what leg (c) asserts. PR1 held on its seed half -- 203 of 203
-- and FAILED on its object half: 18 in-frame against the predicted 22, with
the 4 out-of-frame reached. PR2 and PR3 held. PR4 and PR5 were deliberately not
predicted, and PR5 is worth the abstention: the recovered q is a trinomial at 17
of 18 objects, so the shape the widening was built for is not the shape the
widening's own objects wear. K1 FIRED, on the in-frame half of the wide box
only, and findings 2, 3 and 4 are what the firing bought -- a diagnosis by
elimination where the predecessor had a suspicion. K0, K2, K3, K4, K5 and K6
did not fire. The file ends 60/61 and exits nonzero, which is the honest record
of a kill that fired rather than a fault to be tidied.

A UNITS WARNING, for anyone comparing this file's pair counts with the census's.
They are NOT the same unit and the difference is not this file's to fix: the
census walks one REPRESENTATIVE per size-2 seed core in its expensive half
(explore_descent26_wide.py finding 3), where this file walks every size-2 menu.
So its 41 in-frame pair-walks and this file's 63 measure different things and
neither is wrong. Only the OBJECT count is comparable across the two, which is
the convention both files already state, and it is the one the shortfall is
read in.

RUN RECORD (this file, under memwatch.py at the 512MB default). Pilot and wide
in one process: 60/61 checks, 677.3 s wall, peak working set 131.4 MB, peak
commit 123.7 MB. The pilot leg is a full control and not a warm-up -- it
reproduces the published 8 objects and the published witness, and the layer
diff inside the same scan reproduces the predecessor's own 18 in-frame objects
on the wide box, so the shortfall this file reports is measured against the
predecessor rather than quoted from it. An earlier run of this file, before S4
existed, returned the same 22 objects and the same 18 in frame.
"""

import os
import sys
import time
from itertools import combinations
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import (X, check, CHECKS, menu_poly, used_vars,
                                has_negative)
from explore_menu_faces import exps, face_support, induced, weight_box
from explore_descent_hunt import rank_int, core_of, factorizations
from explore_descent26 import poly_rank
from explore_descent26_why import (NP, PILOT, WIDE, menu_core, pmul, pnonneg,
                                   div_exact, binomial_divisors, to_expr,
                                   splits_of, hidden_negatives, as_dict,
                                   grade, nonmono, object_key)

PB = 64                        # exponents here are at most 5; 64 leaves room


# ================================ the trinomial layer (part two of the attack)
def pack(v):
    """The injective positive weight of part two, as a single integer.

    Linear in v, so pack(a) - pack(b) = pack(a - b) and the pair loop needs no
    vector arithmetic at all. Injective for entries of absolute value < PB/2.
    """
    s = 0
    for c in reversed(v):
        s = s * PB + c
    return s


def tri_candidates(C):
    """Every 0/1 trinomial whose polytope could be a Minkowski summand of Newt(C).

    All three edge directions parallel to a support difference, every coordinate
    inside C's own extent, and the w-minimal exponent translated to 0 -- so each
    triangle is enumerated once, from its w-minimal vertex.
    """
    supp = list(C)
    mxc = [max(v[i] for v in supp) for i in range(NP)]
    prims = set()
    for a, b in combinations(supp, 2):
        d = tuple(i - j for i, j in zip(a, b))
        g = 0
        for e in d:
            g = gcd(g, abs(e))
        if not g:
            continue
        prims.add(tuple(e // g for e in d))
        prims.add(tuple(-e // g for e in d))
    mult = []
    for p in prims:
        t = 1
        while True:
            v = tuple(t * e for e in p)
            if any(abs(e) > mxc[i] for i, e in enumerate(v)):
                break
            mult.append(v)
            t += 1
    par = {pack(v) for v in mult}
    pos = sorted(((pack(v), v) for v in mult), key=lambda z: z[0])
    pos = [z for z in pos if z[0] > 0]
    out, seen = [], set()
    for (pa, va), (pb, vb) in combinations(pos, 2):
        if (pb - pa) not in par:
            continue
        lo = tuple(min(0, va[i], vb[i]) for i in range(NP))
        pts = [tuple(-l for l in lo),
               tuple(a - l for a, l in zip(va, lo)),
               tuple(b - l for b, l in zip(vb, lo))]
        key = tuple(sorted(pts))
        if len(set(pts)) != 3 or key in seen:
            continue
        seen.add(key)
        out.append({p: 1 for p in pts})
    return out


def tri_splits(core):
    """(u, n) for every 0/1 TRINOMIAL divisor u of core with a negative quotient.

    A nonnegative quotient is not new: the term-count law makes it a 0/1
    binomial, which the binomial divisor search already finds (S0c).
    """
    out = []
    for u in tri_candidates(core):
        n = div_exact(core, u)
        if n is not None and not pnonneg(n):
            out.append((u, n))
    return out


def brute_trinomial_divisors(C):
    """Every 0/1 trinomial divisor of C, by factoring and multiplying out.

    The control's reference implementation: correct by construction, far too
    slow for a box, and it is what S0b holds the restricted search against.
    """
    e = to_expr(C)
    g = used_vars(e) or [X[0]]
    facs = []
    for f, m in sympy.factor_list(e)[1]:
        if f in X:
            continue
        for _ in range(m):
            facs.append(sympy.expand(f))
    out = []
    for r in range(1, len(facs) + 1):
        for idx in combinations(range(len(facs)), r):
            u = sympy.expand(sympy.prod([facs[i] for i in idx]))
            P = sympy.Poly(u, *g)
            if len(P.monoms()) != 3 or any(c != 1 for c in P.coeffs()):
                continue
            v = sympy.expand(sympy.prod([facs[i] for i in range(len(facs))
                                         if i not in idx]))
            out.append((as_dict(u), as_dict(v)))
    return out


# ================================================== S0  the positive control
COLLINEAR = (1 + X[0] + X[0] ** 2 + X[0] ** 3 + X[0] ** 4 + X[0] ** 8,
             1 + X[0] + X[0] ** 2,
             1 + X[0] ** 3 - X[0] ** 5 + X[0] ** 6)
TRIANGLE = (1 + X[1] + X[0] ** 2 * X[1] + X[0] * X[1] ** 3
            + X[0] ** 2 * X[1] ** 3 + X[0] ** 3 * X[1] ** 2,
            1 + X[1] + X[0] * X[1],
            1 - X[0] * X[1] + X[0] ** 2 * X[1] + X[0] * X[1] ** 2)


def stage0():
    print("\n=== S0  the positive control ===")
    # (a) THE MOVING CONTROL: the layer's own specimens, invisible to the old search
    for name, (Ce, ue, ne) in (("collinear", COLLINEAR), ("triangle", TRIANGLE)):
        assert sympy.expand(ue * ne - Ce) == 0, name
        C = as_dict(sympy.expand(Ce))
        old = binomial_divisors(C)
        oldneg = splits_of(C)
        oldhid = hidden_negatives(C)
        new = tri_splits(C)
        print(f"  control [{name}]: binomial divisors {len(old)},"
              f" negative splits {len(oldneg)}, finding-0 patch {len(oldhid)},"
              f" trinomial splits {len(new)}")
        check(f"S0a [{name}] the predecessor's search sees nothing at all --"
              " no binomial divisor, no negative split, no hidden negative",
              not old and not oldneg and not oldhid)
        check(f"S0a [{name}] the trinomial layer recovers exactly the frozen"
              " (u, n)",
              len(new) == 1
              and sympy.expand(to_expr(new[0][0]) - ue) == 0
              and sympy.expand(to_expr(new[0][1]) - ne) == 0)
    # (b) the restriction loses nothing, against a factoring reference
    lost = extra = ncore = ntri = 0
    nonneg_q, nonneg_bin, nonneg_flagged = 0, 0, 0
    for A in combinations(range(2, 13), 6):
        C = menu_core(A)
        ncore += 1
        ref = brute_trinomial_divisors(C)
        mine = []
        for u in tri_candidates(C):
            n = div_exact(C, u)
            if n is not None:
                mine.append((u, n))
        rk = {tuple(sorted(u)) for u, _ in ref}
        mk = {tuple(sorted(u)) for u, _ in mine}
        lost += len(rk - mk)
        extra += len(mk - rk)
        ntri += len(rk)
        for u, n in ref:
            if not pnonneg(n):
                continue
            nonneg_q += 1
            nonneg_bin += (len(n) == 2 and all(c == 1 for c in n.values()))
            ue = to_expr(u)
            ug = used_vars(ue) or [X[0]]
            if any(has_negative(sympy.expand(f), ug)
                   for f, _ in sympy.factor_list(ue)[1] if f not in X):
                nonneg_flagged += bool(hidden_negatives(C))
            else:
                nonneg_flagged += 1
    print(f"  control: {ncore} size-6 menus of {{2..12}}, {ntri} trinomial"
          f" divisors by factoring; restricted search missed {lost}, invented"
          f" {extra}")
    check("S0b the restricted candidate enumeration finds every 0/1 trinomial"
          " divisor the factoring reference finds", lost == 0)
    check("S0b and invents none -- every candidate that divides is a genuine"
          " 0/1 trinomial divisor", extra == 0)
    # (c) the nonnegative-quotient clause discards nothing
    print(f"  control: {nonneg_q} of those have a NONNEGATIVE quotient;"
          f" {nonneg_bin} of the quotients are 0/1 binomials, and"
          f" {nonneg_flagged} of the cores were already flagged")
    check("S0c a trinomial divisor with a nonnegative quotient has a 0/1"
          " BINOMIAL quotient -- the term-count law, so the negative-quotient"
          " restriction discards nothing",
          nonneg_q == nonneg_bin)
    check("S0c and such a split contributes no negative factor of its own:"
          " where the trinomial carries one, the finding-0 patch already"
          " flags the core", nonneg_q == nonneg_flagged)


# ==================================================== S1  the generation
def movers_of(core):
    """Every negative factor of a core the three layers reach, tagged by layer."""
    out = [(n, "bin") for _, n in splits_of(core)]
    out += [(as_dict(h), "hid") for h in hidden_negatives(core)]
    out += [(n, "tri") for _, n in tri_splits(core)]
    return out


def generate(box, label):
    """Every (2,6) collision candidate of a box, confirmed by the counter."""
    t0 = time.time()
    menus2 = [tuple(c) for c in combinations(box, 2)]
    menus6 = [tuple(c) for c in combinations(box, 6)]
    cores2 = {A: menu_core(A) for A in menus2}
    mov2 = {A: movers_of(cores2[A]) for A in menus2}
    hot2 = [A for A in menus2 if mov2[A]]
    lay2 = {t: sum(1 for A in menus2 if any(k == t for _, k in mov2[A]))
            for t in ("bin", "hid", "tri")}
    print(f"  [{label}] {len(menus2)} size-2 menus, {len(hot2)} carrying a"
          f" negative factor (by layer: {lay2}); {len(menus6)} size-6 menus")
    # Two candidate sets in ONE scan: what the three layers reach, and what the
    # predecessor's two reach on their own. The difference is the widening's
    # contribution, measured rather than inferred from the boxes being nested.
    cand, old, flagged = set(), set(), []
    lay6 = {"bin": 0, "hid": 0, "tri": 0}
    nsplit6 = tri_only = 0
    for i, B in enumerate(menus6):
        cB = menu_core(B)
        for A in hot2:
            for n, k in mov2[A]:
                if pnonneg(pmul(n, cB)):
                    cand.add((A, B))
                    if k != "tri":
                        old.add((A, B))
        movers = movers_of(cB)
        if movers:
            kinds = {k for _, k in movers}
            nsplit6 += 1
            flagged.append(B)
            for t in kinds:
                lay6[t] += 1
            tri_only += kinds == {"tri"}
            for A in menus2:
                cA = cores2[A]
                for n, k in movers:
                    if pnonneg(pmul(n, cA)):
                        cand.add((A, B))
                        if k != "tri":
                            old.add((A, B))
        if (i + 1) % 100000 == 0:
            print(f"    ... {i+1}/{len(menus6)} scanned, {nsplit6} flagged,"
                  f" {len(cand)} candidates   [{time.time()-t0:.1f}s]")
    tscan = time.time() - t0
    assert len(flagged) == nsplit6
    print(f"  [{label}] scan done: {nsplit6} size-6 cores carry a negative"
          f" factor (by layer: {lay6}; {tri_only} reached by the trinomial"
          f" layer ALONE), {len(cand)} candidate pairs   [{tscan:.1f}s]")
    found = []
    for A, B in sorted(cand):
        gA, cA = core_of(A)
        gB, cB = core_of(B)
        n, facs, g = factorizations(cA, cB, gA, gB)
        if n > 1:
            found.append(dict(A=A, B=B, n=n, facs=facs, gens=g,
                              old=(A, B) in old))
    print(f"  [{label}] confirmed by the counter: {len(found)} of"
          f" {len(cand)} candidates, {sum(r['old'] for r in found)} of them"
          f" reachable without the trinomial layer"
          f"   [{time.time()-t0:.1f}s total]")
    check(f"S1 [{label}] the generator produced at least one collision",
          bool(found))
    return found, tscan, flagged, tri_only


# ======================== S4  the exhaustive pairing (NOT on the design)
def all_negative_factors(core):
    """Every sub-multiset product of a core's Z-factors that carries a negative
    coefficient. Exhaustive, and it costs one factorization -- affordable only
    because it is asked of the flagged cores and never of the box."""
    e = to_expr(core)
    g = used_vars(e) or [X[0]]
    facs = []
    for f, m in sympy.factor_list(e)[1]:
        if f in X:
            continue
        for _ in range(m):
            facs.append(sympy.expand(f))
    out = []
    for r in range(1, len(facs) + 1):
        for idx in combinations(range(len(facs)), r):
            v = sympy.expand(sympy.prod([facs[i] for i in idx]))
            if has_negative(v, g):
                out.append(as_dict(v))
    return out


def stage4(box, label, flagged, seen):
    """Pair every flagged core's EVERY negative factor against every partner.

    S1 asks whether a core HAS a negative factor and pairs the one its divisor
    search happened to surface. Those are different questions: a core enters the
    flagged count on one negative factor while the collision needs another, and
    the count then reads complete while the pairing is not. Here the flagged
    cores are factored outright -- 203 of them against a box of 736,281 -- and
    every negative factor is paired, so no pairing rests on which factor a
    quotient exposed. The size-2 side is NOT made exhaustive; that is the one
    hole this stage leaves, and it is named in the reading.
    """
    print(f"\n=== S4  the exhaustive pairing [{label}] ===")
    t0 = time.time()
    menus2 = [tuple(c) for c in combinations(box, 2)]
    cores2 = {A: menu_core(A) for A in menus2}
    cand, nfac = set(), 0
    for B in flagged:
        negs = all_negative_factors(menu_core(B))
        nfac += len(negs)
        for A in menus2:
            for n in negs:
                if pnonneg(pmul(n, cores2[A])):
                    cand.add((A, B))
                    break
    fresh = sorted(cand - seen)
    print(f"  [{label}] {len(flagged)} flagged cores carry {nfac} negative"
          f" factors in all; {len(cand)} candidate pairs, {len(fresh)} of them"
          f" not already CONFIRMED by S1 (S1's own candidate set is wider and"
          f" includes the size-2 route this stage does not walk)"
          f"   [{time.time()-t0:.1f}s]")
    found = []
    for A, B in fresh:
        gA, cA = core_of(A)
        gB, cB = core_of(B)
        n, facs, g = factorizations(cA, cB, gA, gB)
        if n > 1:
            found.append(dict(A=A, B=B, n=n, facs=facs, gens=g, old=False))
    print(f"  [{label}] confirmed by the counter: {len(found)} new collisions"
          f"   [{time.time()-t0:.1f}s]")
    fl = set(flagged)
    check(f"S4 [{label}] every S1 collision seeded by a flagged core is reached"
          " again -- the exhaustive enumeration contains the quotient one",
          not {(A, B) for A, B in seen if B in fl} - cand)
    return found


# ==================================================== S3  the criterion
def split_of_collision(r):
    """(p, n, q, spectators) for a collision, read off the counter's blocks.

    The predecessor's recovery, unchanged in what it does and no longer
    assuming the two differing blocks are binomial and six-term: p and q are
    whatever the counter's blocks are, and the criterion is symmetric in them.
    """
    f1 = list(r["facs"][0])
    f2 = list(r["facs"][1])
    spect, rest2, d1 = [], list(f2), []
    for t in f1:
        hit = next((u for u in rest2 if sympy.expand(t - u) == 0), None)
        if hit is None:
            d1.append(t)
        else:
            rest2.remove(hit)
            spect.append(t)
    if len(d1) != 2 or len(rest2) != 2:
        return None, None, None, None
    for p in d1:
        other1 = d1[1] if p is d1[0] else d1[0]
        for pn in rest2:
            q = rest2[1] if pn is rest2[0] else rest2[0]
            n = sympy.cancel(pn / p)
            if not n.is_polynomial():
                continue
            n = sympy.expand(n)
            if sympy.expand(n * q - other1) == 0:
                return p, n, q, spect
    return None, None, None, None


def edge_dirs(e, g):
    """The primitive edge directions of Newt(e), as a sorted set of tuples.

    A superset for a polytope of more than two vertices -- differences of
    support vectors rather than of adjacent vertices -- which is what the
    printed column is for: the criterion itself is read off the weight scan.
    """
    out = set()
    for u, v in combinations(exps(e, g), 2):
        d = tuple(a - b for a, b in zip(u, v))
        h = 0
        for c in d:
            h = gcd(h, abs(c))
        if not h:
            continue
        d = tuple(c // h for c in d)
        out.add(min(d, tuple(-c for c in d)))
    return sorted(out)


def stage3(objs, label, prior):
    print(f"\n=== S3  the criterion [{label}] ===")
    rows, faces, agree, sep_tot = [], 0, 0, 0
    bad_nec, bad_suf = [], []
    for key, rs in objs.items():
        r = rs[0]
        p, n, q, spect = split_of_collision(r)
        if p is None:
            rows.append(dict(r=r, p=None, key=key))
            continue
        g = r["gens"]
        pts = exps(sympy.expand(sympy.prod(r["facs"][0])), g)
        seen = {}
        for w in weight_box(len(g), r["radius"]):
            seen.setdefault(frozenset(face_support(pts, w)), w)
        edge = False
        for f, w in seen.items():
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
        rows.append(dict(r=r, p=p, n=n, q=q, key=key, suits=len(rs),
                         spect=len(spect), pt=len(exps(p, g)),
                         qt=len(exps(q, g)), nt=len(exps(n, g)),
                         pd=edge_dirs(p, g), qd=edge_dirs(q, g),
                         nrank=rank_int([tuple(a - b for a, b in zip(u, v))
                                         for u, v in combinations(exps(n, g), 2)]),
                         pred=1 if edge else r["dim"],
                         seedrank=max(poly_rank(menu_poly(r["A"])),
                                      poly_rank(menu_poly(r["B"]))),
                         fresh=key not in prior))
    print(f"  faces examined: {faces} over {len(objs)} objects,"
          f" {sep_tot} of them separating; criterion agreed at {agree}")
    check(f"S3 [{label}] the two-differing-block recovery found p, n and q at"
          " every object (K6)", all(row["p"] is not None for row in rows))
    check(f"S3 [{label}] no face separates where the criterion forbids it --"
          " the PROVED half (K2)", not bad_nec)
    check(f"S3 [{label}] no face fails to separate where the criterion allows"
          " it -- the sufficient half (K3)", not bad_suf)
    graded = [row for row in rows if row["p"] is not None]
    check(f"S3 [{label}] the generalized edge reading predicts delta at every"
          " in-frame object (K4)",
          all(row["pred"] == row["r"]["delta"] for row in graded))
    print("\n  THE TABLE -- every in-frame object, one line  (new | suits |"
          " dim delta | criterion | spectators | p,q,n term counts)")
    for row in sorted(graded, key=lambda z: (-z["fresh"], -z["r"]["delta"],
                                             -z["suits"])):
        r = row["r"]
        print(f"    {'NEW' if row['fresh'] else '   '} {row['suits']:2d}x "
              f" dim {r['dim']} delta {r['delta']}  crit {row['pred']}"
              f"  spect {row['spect']}  seedrank {row['seedrank']}"
              f"  p[{row['pt']}t] q[{row['qt']}t] n[{row['nt']}t"
              f" rank {row['nrank']}]   {set(r['A'])} x {set(r['B'])}")
    fresh = [row for row in graded if row["fresh"]]
    print(f"\n  objects the predecessor did NOT reach: {len(fresh)}")
    for row in fresh:
        print(f"    {set(row['r']['A'])} x {set(row['r']['B'])}"
              f"   delta {row['r']['delta']}  criterion {row['pred']}")
        print(f"      p = {row['p']}   [edges {row['pd']}]")
        print(f"      q = {row['q']}   [edges {row['qd']}]")
        print(f"      n = {row['n']}   [edges {edge_dirs(row['n'], row['r']['gens'])}]")
    return rows


# ==================================================================== driver
def run_box(box, label):
    print(f"\n=== S1  the generation [{label}]  box {{2..{max(box)}}} ===")
    found, tscan, flagged, trionly = generate(box, label)
    s1obj = {object_key(r) for r in found}
    s1in = {object_key(r) for r in found
            if len(sympy.Poly(sympy.expand(menu_poly(r["A"]) * menu_poly(r["B"])),
                              *r["gens"]).monoms()) == 12}
    found += stage4(box, label, flagged, {(r["A"], r["B"]) for r in found})
    print(f"  [{label}] S1 reached {len(s1obj)} objects ({len(s1in)} in frame);"
          f" with S4 the walk stands at {len({object_key(r) for r in found})}")
    objs, outobj = grade(found, label)
    # An object is the widening's iff NO menu suit of it was reachable without
    # the trinomial layer -- read at the CORE, which is the convention-free
    # unit, and never at the menu, where one suit reached is the whole object.
    prior = {k for k, rs in objs.items() if any(r["old"] for r in rs)}
    rows = stage3(objs, label, prior)
    return objs, outobj, rows, tscan, len(flagged), trionly, len(prior)


def main():
    t0 = time.time()
    stage0()
    objs, outobj, _, _, _, _, pprior = run_box(PILOT, "pilot {2..24}")
    d2 = [rs[0] for rs in objs.values() if rs[0]["delta"] >= 2]
    check("S0d the widened generator still reproduces the published pilot box:"
          " 8 in-frame objects, 7 at delta 1 and 1 at delta 2 (K5)",
          len(objs) == 8 and len(d2) == 1)
    check("S0d the pilot delta=2 object is the published witness (K5)",
          len(d2) == 1 and
          {tuple(sorted(d2[0]["A"])), tuple(sorted(d2[0]["B"]))} ==
          {(2, 3), (3, 4, 8, 9, 18, 24)})
    check("S0d the predecessor reproduced the pilot box ENTIRELY, so the"
          " widening adds nothing there and the layer diff says so",
          pprior == len(objs) == 8)
    if any(not v for _, v in CHECKS):
        print("\nPILOT CONTROL FAILED -- the wide box is not walked.")
        for n, v in CHECKS:
            if not v:
                print(f"  FAIL {n}")
        return 1
    if "--pilot" not in sys.argv:
        wobjs, woutobj, _, tscan, nflag, trionly, wprior = run_box(
            WIDE, "wide {2..32}")
        wd2 = [rs[0] for rs in wobjs.values() if rs[0]["delta"] >= 2]
        check("S1 the wide box reaches the published 22 in-frame objects,"
              " 21 at delta 1 and 1 at delta 2 (K1)",
              len(wobjs) == 22 and len(wd2) == 1)
        check("S1 the wide box reaches the published 4 out-of-frame objects"
              " (K1)", woutobj == 4)
        check("S1 the wide box flags all 203 published size-6 seeds (K1)",
              nflag == 203)
        check("S1 the layer diff reproduces the predecessor's published"
              " shortfall: 18 in-frame objects reachable without the"
              " trinomial layer (K1)", wprior == 18)
        print(f"\n  PR4 the widened scan of the wide box: {tscan:.1f} s,"
              f" against the predecessor's 213.3 s and the 4,126.3 s census;"
              f" {trionly} cores reached by the trinomial layer alone")
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time()-t0:.1f}s")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
