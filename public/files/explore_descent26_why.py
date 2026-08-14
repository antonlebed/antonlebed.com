"""WHAT the full-dimension collision IS: why that seed and no other.

THE QUESTION. explore_descent26_wide.py settled both headline questions at
term count 12: a collision of descent dimension delta = 2 EXISTS, and it is
alone in a box 7.3x the one that found it. What neither run touched is the
MECHANISM. Nothing yet says why {3,4,8,9,18,24} x {2,3} and no other menu
pair, and the two structural handles the (3,4) half offered both miss here:
the witness's seed core has rank 2 where this size pair makes rank 3
available, so the rank does not select it, and the seed is not collinear, so
the absorption sentence that explains 48 of the 71 collisions there has no
line to run on. This file asks what DOES select it, and the answer wanted is
a criterion that DERIVES delta rather than a column that correlates with it.

WHOSE VOCABULARY. The suspicion is written in the FACES vocabulary -- initial
forms, Newton polygons, Minkowski summands -- which is the object's own and
not the menu vocabulary the boxes are drawn in. The menu box survives only as
the sampling frame, and every count below is about the box walked.

THE TRAP THIS FILE IS BUILT AROUND, named before the design. The comparison
on offer is 21 rows at delta = 1 against ONE at delta = 2. With
a single positive row ANY column that isolates it "agrees with delta at every
row", and the witness is isolated in a great many ways -- its menu, its core,
its partner. Separation is therefore worth nothing on its own here. The bar
this file sets instead: a candidate must be DERIVED from the algebra, must
predict delta face by face rather than object by object, and must be checked
at every face of every object, which is a population of hundreds rather than
of 22.

THE HAND-ATTACK, on paper before any engine code, in two parts. It changes
both what this file can afford and what it is looking for.

PART ONE -- THE SHAPE OF A (2,6) COLLISION, AND WHY NO CENSUS IS NEEDED.
A collision is a pair of factorizations of one product into blocks that are
nonnegative and atomic. Take a walked pair (A, B) of menu sizes 2 and 6 whose
product is non-unique, and look at the second factorization's 2-TERM block.
That block is a nonnegative 0/1 binomial. It cannot mix nonconstant factors
drawn from both cores: for nonnegative 0/1 factors term counts MULTIPLY
(explore_seed_shape.py's term-count law), so such a product carries at least
4 terms. So the 2-term block is a polynomial divisor of ONE core. Call it p,
write that core as p*n, and call the other core q. The two factorizations are

    {p*n, q}   and   {p, n*q},

and the second is available exactly when n*q is nonnegative. Neither test
factors anything. And p is findable from the core's own support: Newt(p) is a
Minkowski summand of Newt(p*n), so its direction is parallel to an EDGE of
that polytope, hence parallel to a difference of two support vectors -- 15
differences at size 6, each contributing its own integer sub-multiples. So
the collisions of a box are GENERATED directly, and the size-6 seed census
that priced the last two runs at over an hour is not on the path at all.

WHERE PART ONE STOPS. It assumes the 2-term block is a divisor of one core,
which the term-count law gives unless the block mixes two NEGATIVE factors
into a nonnegative binomial (NARROWER THAN THE EXCEPTION IS --
explore_descent26_mix.py: the law forbids only a product of two NONNEGATIVE
0/1 factors, so ONE negative factor suffices to mix, and the four objects it
adds mix a nonnegative factor of one core with a negative factor of the
other); and it requires n to carry a negative
coefficient, which is the standing fact that only seeds collide. Both are
assumptions about a population and neither is proved here, so the generator
is CONTROLLED against the published object counts of two nested boxes rather
than trusted.

PART TWO -- WHAT A FACE CAN SEE. Initial forms are multiplicative, so on a
weight w the two factorizations induce

    {in(p)*in(n), in(q)}   against   {in(p), in(n)*in(q)},

each factor divided by its own monomial content (that division is the whole
point: it is what makes a vertex grade nothing). Two collapses follow.
  If in_w(n) is a MONOMIAL, both sides reduce to {prim in(p), prim in(q)}.
  If in_w(p) and in_w(q) are BOTH monomials, both reduce to {prim in(n), 1}.
Either way the face fails to separate. So

    A FACE SEPARATES ONLY IF in_w(n) is non-monomial AND at least one of
    in_w(p), in_w(q) is non-monomial.

Read geometrically: in_w(n) non-monomial says w is normal to a positive-
dimensional face of Newt(n); in_w(p) non-monomial says w is perpendicular to
dir(p), the direction of the binomial p. At product dimension 2 -- which is
every in-frame collision either box has ever produced -- the second condition
pins w to one line, so the whole test is four weights, and the criterion
reads: DELTA = 1 EXACTLY WHEN Newt(n) HAS AN EDGE PARALLEL TO dir(p) OR TO
dir(q). Name it THE PARALLEL-EDGE CRITERION.

The necessary half is proved above and is the load-bearing half: it gives an
upper bound on the separating faces, hence a LOWER bound on delta, which is
the direction a sampled face reading cannot supply. The sufficient half is
not proved -- two non-monomial initial forms could still induce equal
multisets by accident -- so it is a prediction and the run checks it.

HAND-CHECKED ON THE WITNESS before any code. n = x0^2 x1 + x0^2 - x0 x1 +
x1^2 + x1, p = x0 + 1 with dir (1,0), q = x0 + x1 with dir (1,-1). The four
weights: w = (0,1) maximizes at (0,2) alone and w = (0,-1) at (2,0) alone, so
p contributes nothing; w = (1,1) maximizes x0+x1 at (2,1) alone and w =
(-1,-1) at (0,1) alone, so q contributes nothing. Every in_w(n) is a
monomial, no proper face separates, and delta = 2 follows from the algebra
rather than from an enumeration. If the criterion is right, THAT is what the
witness IS.

DESIGN, four stages.
 S0 THE POSITIVE CONTROL, run before any generated number is read.
    (a) The delta pipeline reproduces the two published gradings, the t = 6
        cyclotomic identity and the t = 12 graded point, both dim 1 delta 1.
    (b) The exact face enumerator finds a separating EDGE on the published
        two-dimensional delta = 1 escape specimen -- an enumerator returning
        only vertices would read delta = dim everywhere.
    (c) The pure-integer polynomial layer this file builds for speed (vectors,
        dict polynomials, exact division by a binomial) agrees with sympy on
        every core it computes in the pilot box, and its binomial-divisor
        search finds the divisor 1 + x0 of the published size-2 seed core
        1 + x0^3 -- the search that replaces the census.
    (d) THE GENERATOR REPRODUCES THE PUBLISHED PILOT BOX: {2..24} must yield
        8 in-frame OBJECTS, 7 at delta 1 and 1 at delta 2, and the delta = 2
        object must be {3,4,8,9,18,24} x {2,3}. A generator that misses a
        collision fails here, and nothing below is read on a failure.
 S1 THE GENERATION, per box. Every size-6 menu's core is scanned for 0/1
    binomial divisors with a negative-coefficient quotient; every size-2
    menu's core likewise (which is where the size-2 seeds enter, 1 + x0
    dividing 1 + x0^3). Each split (p, n) is paired against every menu of
    the other size and kept when n * (that core) is nonnegative. Every
    candidate is then CONFIRMED with count_from_core, the same counter both
    predecessors used, so no collision below rests on the generator's
    algebra. Deduped on the menu pair, then collapsed to OBJECTS by core
    pair -- the convention-free unit both halves share.
 S2 THE FRAME AND THE GRADING. The frame split first: a 2-term and a 6-term
    0/1 menu multiply to 12 terms exactly when no support collapses, so a
    product below 12 terms carries a coefficient above 1 and is outside the
    frame delta is minted for. Then dim and delta for every in-frame object,
    and for the dimension-2 ones the exact face enumeration by hull with the
    sampled reading checked against it.
 S3 THE CRITERION, checked at two levels.
    (a) FACE BY FACE, the population that makes this more than a 22-row
        coincidence: over every object and every weight of the sample box,
        does "this face separates" agree with "in_w(n) non-monomial AND
        (in_w(p) or in_w(q) non-monomial)"? The necessary half is proved, so
        a disagreement can only be a separating-looking face where the
        criterion fires and the multisets coincide anyway -- which would
        falsify the sufficient half and is the interesting failure.
    (b) OBJECT BY OBJECT, the parallel-edge reading: does Newt(n) have an
        edge parallel to dir(p) or dir(q), and does that predict delta at
        every one of the box's in-frame objects?
    Then THE TABLE itself: every in-frame object with the
    columns a mechanism could live in -- which side is the seed, the seed
    core's rank, dir(p), dir(q), the rank and edge directions of Newt(n),
    the criterion's verdict, and delta -- printed in full so the comparison
    is on the record rather than asserted.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): all four legs hold. (d) is the one that can fail on a real
      mistake: it is the generator's only contact with a published count
      before the wide box is walked.
  PR1 (S1): the wide box {2..32} yields 26 objects, 22 of them in frame, and
      the in-frame 22 split 21 at delta 1 and 1 at delta 2 -- the published
      reading, reproduced by a route that factors no menu.
  PR2 (S3a): the criterion agrees with separation at every face of every
      object in both boxes. The necessary half is proved; this predicts the
      sufficient half too.
  PR3 (S3b): the parallel-edge criterion predicts delta at every in-frame
      object of both boxes, and in particular reads 2 at the witness and 1
      at all 21 others.
  PR4: NOT PREDICTED. Which OTHER columns of the table also separate the
      witness. The trap named at the top says several will, and predicting
      them is what would make the table unreadable.
  PR5: NOT PREDICTED. What the generator costs against the 4,126 s census
      it replaces. It is a measurement and the point of taking it is that
      what any later run of this question costs depends on it.

KILLS (observables with live failure modes; what each MEANS is weighed after
the run and never before).
  K0: any S0 leg fails. The instrument is broken and nothing below is read.
  K1: the generator's object counts differ from the published ones on either
      box. Part one of the hand-attack is wrong about the shape of a
      collision, and the census IS the price after all.
  K2: some face separates where the criterion says it cannot. The PROVED
      half is wrong, which would mean the initial-form algebra above is
      wrong, and the criterion dies outright.
  K3: some face fails to separate where the criterion says it should. The
      sufficient half is wrong: the criterion survives as a necessary
      condition and a lower bound on delta, and stops being a criterion.
  K4: the parallel-edge reading misgrades any object. Whatever survives K2
      and K3, it does not reduce to the edge test at the object level.
  K5: the wide box yields no delta = 2 object, or no collisions at all. The
      run is deciding on a population's emptiness rather than on the claim.

HONEST LIMITS carried into the reading, stated before the run. (i) The boxes
bound menu ELEMENTS and nothing the mathematics names; every count is about
the box walked and "the witness" can only ever mean the witness of {2..32}.
(ii) The criterion is derived at product dimension 2 in its edge form; the
face form is dimension-free but the edge reading uses that every in-frame
collision here is 2-dimensional, which is an observation of these boxes and
not a theorem. (iii) The generator's completeness rests on the two
assumptions part one names, and its warrant is S0(d) and PR1 -- agreement
with two published populations -- not a proof. (iv) Nothing here leaves the
menu frame: a 0/1 product with a factor carrying a coefficient above 1 is
outside every statement below.

FINDINGS (tiers per the standard naming scale; run record below).

0. ONE CORRECTION THE SLATE DOES NOT CARRY. It is left as frozen. Part one
   assumed the moving negative factor n is core/p for a 0/1 binomial divisor
   p. It need not be. Where a core reads p*t with t a 0/1 TRINOMIAL, the
   negative factor can sit strictly INSIDE t, and then core/p = t is
   nonnegative and the split search sees nothing at all. The engine now
   factors those trinomial quotients -- cached per distinct trinomial, which
   is the only factorization this file pays for -- and the wide box's flagged
   size-6 cores stand at 199 against its 203 seeds with the patch in. The
   PILOT box flags 55 either way, and 873 candidate pairs either way: the
   patch changed nothing there, which is why the control that reproduces
   that box entirely could not have exposed this. The species is an enumeration
   keyed on a QUOTIENT where the object it means to enumerate is a FACTOR,
   and it is invisible wherever the factor happens to be the whole quotient,
   which is every case the hand-attack checked.

1. THE PARALLEL-EDGE CRITERION HOLDS AT EVERY FACE OF EVERY OBJECT REACHED
   (rule, proved in its necessary half; 231 face readings, 55 of them
   separating, 0 disagreements in either direction -- 74 readings over the
   pilot box's 8 objects and 157 over the wide box's 18, and the 8 are 8 of
   the 18 by comparison of the two printed tables, so the distinct
   population is 18 and not 26). A face
   separates exactly when in_w(n) is non-monomial AND at least one of in_w(p),
   in_w(q) is. The necessary half is the proof in part two of the hand-attack
   and it is what the run cannot supply: it bounds the separating faces from
   above and so bounds delta from BELOW, the direction a sampled face reading
   never reaches. The sufficient half was a prediction and PR2 held: no face
   the criterion allows failed to separate. K2 and K3 both stayed shut.

2. AND IT IS WHAT THE WITNESS IS (observation, exact; PR3 held, K4 did not
   fire). in_w(p) is non-monomial exactly when w is perpendicular to dir(p),
   so at product dimension 2 the criterion reads: DELTA = 1 EXACTLY WHEN
   Newt(n) HAS AN EDGE PARALLEL TO dir(p) OR TO dir(q). It predicts delta at
   every in-frame object either box reaches -- 18 distinct, the pilot's 8
   being 8 of those 18, read off the two printed tables rather than argued
   from the boxes being nested, which is the containment a rewritten walk
   is exactly the thing that can break. Every delta = 1 object is the same
   thing wearing different clothes: the t = 6 cyclotomic identity -- or, at
   the two objects seeded by {8,27}, its HOMOGENIZATION x0^2 - x0 x1 + x1^2,
   which is two variables wearing a one-variable image and is exactly the
   distinction the falsified collinearity claim turned on -- n the 3-term
   collinear factor, p and q on n's own line, with ONE spectator block
   -- a binomial riding along that contributes the same primitive initial
   form to both sides and cancels. The witness is the only object with no
   spectator, and its n is 5 terms of RANK 2 whose polygon's edges miss BOTH
   binomial directions, (1,0) and (1,-1) -- which of the two wears the name
   p is the recovery's choice and not the object's, the criterion being
   symmetric in p and q and the hand-attack above naming them the other way
   round. So the mechanism is not the rank the
   size pair adds and not the seed's collinearity: it is that the negative
   cofactor's polygon has grown an edge structure NEITHER binomial is
   parallel to, which is what "inherited from no face" means concretely.

3. THE TRAP THE SLATE NAMED FIRED, AND THE TABLE IS WHERE IT SHOWS
   (observation). The rank of Newt(n) also agrees with delta at every one of
   the 18 rows -- 1 at each delta = 1 object, 2 at the witness -- and it is
   NOT the mechanism. It agrees only because in the reached population every
   collinear n happens to lie on p's own line; a collinear n on a line
   neither binomial shares would read rank 1 and delta 2, and the criterion
   says so while the rank column cannot. This is the difference between a
   column that separates one row from seventeen and a criterion that
   derives the answer, and the table prints both so the difference is on the
   record. PR4 was deliberately not predicted and this is what that bought.

4. THE CENSUS IS NOT THE PRICE (measurement; PR5, observable). The wide box's
   collisions are generated in 213.3 s of scanning plus 22.8 s of confirmation
   -- 236.1 s in all, against the 4,126.3 s census the last two runs paid to
   reach the same population, and 4,922.9 s for the full predecessor run. The
   whole box is walked without factoring a menu: cores come from exponent
   arithmetic, binomial divisors from the support's own differences (Newt(p)
   is a Minkowski summand, so dir(p) is parallel to an edge and hence to a
   difference of two support vectors), and sympy is called only on the
   distinct trinomial quotients of finding 0 and on the 4,146 confirmations.
   Peak working set 132.1 MB against the predecessor's 171.4 MB.

5. AND IT IS NOT YET COMPLETE: K1 FIRED (measurement, and the open gap). The
   generator reaches 199 of the published 203 size-6 seeds, and its wide box
   is 18 in-frame objects against the published 22, with NONE of the 4
   published out-of-frame objects. The pilot box {2..24} is reproduced
   ENTIRELY -- 8 objects, 7 at delta 1, 1 at delta 2, the published witness
   -- so the shortfall is a wide-box shape the narrow box does not contain,
   and the two 4s are the same 4 seeds if each carries one object of each
   kind, which is a suspicion and not a measurement. What the shortfall does
   NOT touch: every claim above is stated over the objects reached and is
   exact there, and the criterion's proved half is a theorem about faces that
   no missing object can weaken. What it DOES touch is finding 2's word
   "every": the four unreached objects have never had the criterion put to
   them. The next cut at them is the divisor search widened from binomials to
   0/1 TRINOMIAL divisors, whose supports are constrained the same way -- a
   trinomial's polygon is a Minkowski summand too -- and which is where a
   core factoring as two 3-term pieces with no binomial divisor would be
   caught, the one shape both the split search and finding 0's patch miss.

HOW THE PREDICTIONS AND KILLS LANDED. PR0 held on all four legs, and (d) is
what makes the rest readable: the pilot box is reproduced entirely before any
wide number is taken. PR1 FAILED and that failure is finding 5 -- 18 in-frame
objects against the predicted 22. PR2 and PR3 held. PR4 and PR5 were
deliberately not predicted and findings 3 and 4 are what that bought. K1
FIRED, on the wide box only, and it is the one open thing here; K2, K3, K4
and K5 did not fire. The file therefore ends 51/53 and exits nonzero, which
is the honest record of a kill that fired rather than a fault to be tidied.

RUN RECORD (this file, under memwatch.py at the 512MB default). Pilot and
wide in one process: 51/53 checks, 270.7 s wall, peak working set 131.7 MB,
peak commit 124.2 MB. Two of those checks were added after the reading, by
the audit rather than the design: delta is the MAX over factorization pairs
while the criterion is tested on the pair (facs[0], facs[1]), and those are
one pair only where the collision has exactly two factorizations. They do,
in both boxes, so the flaw was latent and never fired -- but it is now
checked rather than argued, and every other figure reproduced to the digit
on the re-run. The pilot box is a full control and not a warm-up -- it
reproduces the published 8 objects and the published witness before the wide
box is walked, and a failed check there stops the file. An earlier run of the
same file, before finding 0's patch, returned the same 18 in-frame objects
that the patched one does: the patch bought coverage of the seed side and no
collision, which is worth knowing because it says the four missing objects
are not of that shape either. What that earlier run's own flagged-core count
was on the wide box is NOT recorded here, because the line was not read
before the run was replaced.
"""

import os
import sys
import time
from itertools import combinations
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import (X, PRIMES, check, CHECKS, menu_poly,
                                used_vars, has_negative, is_nonneg,
                                count_from_core)
from explore_menu_faces import (exps, face_support, initial_form, induced,
                                affine_rank, weight_box, report)
from explore_descent_hunt import (rank_int, descent_sampled, core_of, RUNG12,
                                  factorizations)
from explore_descent26 import core_key, poly_rank, exact_proper_faces

PILOT = list(range(2, 25))
WIDE = list(range(2, 33))
NP = 11                                   # primes up to 31; 32 = 2^5 is in box
PRIMS = PRIMES[:NP]


# ============================================== the pure-integer polynomial layer
def vec(m):
    """Exponent vector of an integer, as a tuple over the first NP primes."""
    out, rest = [0] * NP, m
    for i, p in enumerate(PRIMS):
        while rest % p == 0:
            rest //= p
            out[i] += 1
    assert rest == 1, f"element {m} outside the prime list"
    return tuple(out)


def menu_core(A):
    """The core of a menu as a dict {exponent vector: 1}, content divided out."""
    vs = [vec(m) for m in A]
    lo = tuple(min(v[i] for v in vs) for i in range(NP))
    return {tuple(a - b for a, b in zip(v, lo)): 1 for v in vs}


def pmul(a, b):
    out = {}
    for u, cu in a.items():
        for v, cv in b.items():
            w = tuple(i + j for i, j in zip(u, v))
            c = out.get(w, 0) + cu * cv
            if c:
                out[w] = c
            elif w in out:
                del out[w]
    return out


def pnonneg(a):
    return all(c >= 0 for c in a.values())


def order(v):
    return (sum(v), v)


def div_exact(C, D):
    """C / D as integer polynomials, or None where the division is not exact."""
    ld = max(D, key=order)
    cd = D[ld]
    rem, q = dict(C), {}
    while rem:
        v = max(rem, key=order)
        u = tuple(a - b for a, b in zip(v, ld))
        if min(u) < 0:
            return None
        c, r = divmod(rem[v], cd)
        if r:
            return None
        q[u] = c
        for w, cw in D.items():
            t = tuple(a + b for a, b in zip(u, w))
            nc = rem.get(t, 0) - c * cw
            if nc:
                rem[t] = nc
            elif t in rem:
                del rem[t]
    return q


def binomial_divisors(C):
    """Every 0/1 binomial divisor of C, with its quotient.

    Newt(p) is a Minkowski summand of Newt(C), so dir(p) is parallel to an
    edge of Newt(C) and hence to a difference of two support vectors; its
    integer sub-multiples are the rest of the candidates.
    """
    supp = list(C)
    cands = set()
    for a, b in combinations(supp, 2):
        d = tuple(i - j for i, j in zip(a, b))
        g = 0
        for e in d:
            g = gcd(g, abs(e))
        if not g:
            continue
        prim = tuple(e // g for e in d)
        for t in range(1, g + 1):
            e = tuple(t * c for c in prim)
            lo = tuple(min(0, c) for c in e)
            cands.add((tuple(-c for c in lo),
                       tuple(c - l for c, l in zip(e, lo))))
    out = []
    for u, v in cands:
        p = {u: 1, v: 1}
        n = div_exact(C, p)
        if n is not None:
            out.append((p, n))
    return out


def to_expr(d, gens=None):
    e = 0
    for v, c in d.items():
        t = c
        for i, k in enumerate(v):
            if k:
                t *= X[i] ** k
        e += t
    return sympy.expand(e)


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
    check("S0a t=12 reproduces the published dim 1 and delta 1",
          n == 2 and dim == 1 and d == 1)

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
    edims = sorted({affine_rank(list(f)) for f in esep})
    print(f"  control: escape specimen, {len(efaces)} exact proper faces,"
          f" {len(efaces - set(eseen))} missed; separating dims {edims}")
    check("S0b the exact enumerator finds a separating EDGE on the published"
          " delta-1 specimen, so it can read below dim", 1 in edims)

    # (c) the integer layer against sympy, and the divisor search.
    bad = 0
    for A6 in combinations(range(2, 13), 6):
        mine = to_expr(menu_core(A6))
        g, core = core_of(A6)
        theirs = sympy.expand(sympy.prod(core))
        bad += (sympy.expand(mine - theirs) != 0)
    seed2 = menu_core((2, 16))
    divs = binomial_divisors(seed2)
    negq = [(p, n) for p, n in divs if not pnonneg(n)]
    print(f"  control: integer core layer disagreed with sympy at {bad} menus;"
          f" 1+x0^3 has {len(divs)} binomial divisors, {len(negq)} with a"
          f" negative quotient")
    check("S0c the integer polynomial layer reproduces sympy's core at every"
          " size-6 menu of {2..12}", bad == 0)
    check("S0c the divisor search finds the split of the published size-2 seed"
          " core 1 + x0^3 into a binomial and a negative quotient",
          len(negq) == 1 and to_expr(negq[0][1]) ==
          sympy.expand(1 - X[0] + X[0]**2))


# ==================================================== S1  the generation
def splits_of(core):
    return [(p, n) for p, n in binomial_divisors(core) if not pnonneg(n)]


TRIFAC = {}


def hidden_negatives(core):
    """Negative factors of a core that are NOT a quotient by a binomial.

    The slate's part one assumed the moving negative factor n is core/p for
    a 0/1 binomial divisor p. It need not be: where the core is p*t with t a
    0/1 TRINOMIAL, the negative factor can sit strictly inside t, and then
    core/p = t is nonnegative and the split search sees nothing. The
    quotients are trinomials and there are few distinct ones, so each is
    factored once with sympy and cached -- the only factorization this file
    pays for, and it is paid per distinct trinomial rather than per menu.
    """
    out = []
    for p, t in binomial_divisors(core):
        if not pnonneg(t) or len(t) != 3:
            continue
        key = tuple(sorted(t))
        if key not in TRIFAC:
            e = to_expr(t)
            g = used_vars(e) or [X[0]]
            fl = sympy.factor_list(e)[1]
            TRIFAC[key] = [sympy.expand(f) for f, m in fl for _ in range(m)
                           if f not in X and has_negative(sympy.expand(f), g)]
        out.extend(TRIFAC[key])
    return out


def as_dict(expr):
    P = sympy.Poly(expr, *X)
    out = {}
    for m, c in zip(P.monoms(), P.coeffs()):
        # NP is the prime count the box needs, not the symbol count. Truncating
        # a monomial that reaches past it would silently alias two exponent
        # vectors, so it is refused rather than trimmed.
        assert not any(m[NP:]), f"exponent vector past prime {PRIMS[-1]}: {m}"
        out[tuple(m[:NP])] = int(c)
    return out


def generate(box, label):
    """Every (2,6) collision candidate of a box, confirmed by the counter."""
    t0 = time.time()
    menus2 = [tuple(c) for c in combinations(box, 2)]
    menus6 = [tuple(c) for c in combinations(box, 6)]
    cores2 = {A: menu_core(A) for A in menus2}
    splits2 = {A: splits_of(cores2[A]) for A in menus2}
    hot2 = [A for A in menus2 if splits2[A]]
    print(f"  [{label}] {len(menus2)} size-2 menus, {len(hot2)} carrying a"
          f" negative split; {len(menus6)} size-6 menus to scan")
    cand = set()
    nsplit6 = 0
    for i, B in enumerate(menus6):
        cB = menu_core(B)
        for A in hot2:
            for p, n in splits2[A]:
                if pnonneg(pmul(n, cB)):
                    cand.add((A, B))
        movers = [n for _, n in splits_of(cB)]
        hidden = hidden_negatives(cB)
        if hidden:
            movers = movers + [as_dict(h) for h in hidden]
        if movers:
            nsplit6 += 1
            for A in menus2:
                cA = cores2[A]
                for n in movers:
                    if pnonneg(pmul(n, cA)):
                        cand.add((A, B))
                        break
        if (i + 1) % 100000 == 0:
            print(f"    ... {i+1}/{len(menus6)} scanned, {nsplit6} with a"
                  f" negative split, {len(cand)} candidates"
                  f"   [{time.time()-t0:.1f}s]")
    tscan = time.time() - t0
    print(f"  [{label}] scan done: {nsplit6} size-6 cores carry a negative"
          f" split, {len(cand)} candidate pairs   [{tscan:.1f}s]")
    found = []
    for A, B in sorted(cand):
        gA, cA = core_of(A)
        gB, cB = core_of(B)
        n, facs, g = factorizations(cA, cB, gA, gB)
        if n > 1:
            found.append(dict(A=A, B=B, n=n, facs=facs, gens=g))
    print(f"  [{label}] confirmed by the counter: {len(found)} of"
          f" {len(cand)} candidates   [{time.time()-t0:.1f}s total]")
    check(f"S1 [{label}] the generator produced at least one collision (K5)",
          bool(found))
    return found, tscan


# ============================================ S2  the frame and the grading
def object_key(r):
    return tuple(sorted([core_key(core_of(r["A"])[1]),
                         core_key(core_of(r["B"])[1])]))


def grade(found, label):
    print(f"\n=== S2  the frame and the grading [{label}] ===")
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
        r["dim"], r["delta"], r["radius"] = dim, d, b
    check(f"S2 [{label}] a collision's product is 0/1 exactly when it carries"
          " 12 terms", all((r["maxc"] == 1) == (r["terms"] == 12)
                           for r in found))
    # delta is the MAX over factorization pairs while S3 tests the criterion
    # on the pair (facs[0], facs[1]). Those are the same pair only where the
    # collision has exactly two factorizations, so that is checked and not
    # assumed -- a third would put the grading and the test on different
    # objects without either one looking wrong.
    check(f"S2 [{label}] every collision has exactly two factorizations, so"
          " the pair delta is read from is the pair the criterion is tested"
          " on", all(r["n"] == 2 for r in found))
    allobj = {}
    for r in found:
        allobj.setdefault(object_key(r), []).append(r)
    inframe = [r for r in found if r["terms"] == 12]
    objs = {}
    for r in inframe:
        objs.setdefault(object_key(r), []).append(r)
    outobj = len(allobj) - len(objs)
    print(f"  {len(found)} pair-walks -> {len(allobj)} objects;"
          f" IN FRAME {len(inframe)} pair-walks -> {len(objs)} objects,"
          f" {outobj} objects outside")
    check(f"S2 [{label}] no object straddles the frame boundary",
          all(len({x["terms"] == 12 for x in rs}) == 1
              for rs in allobj.values()))
    joint = {}
    for rs in objs.values():
        k = (rs[0]["dim"], rs[0]["delta"])
        joint[k] = joint.get(k, 0) + 1
        check(f"S2 [{label}] every menu suit of one object grades alike",
              len({(r["dim"], r["delta"]) for r in rs}) == 1)
    print("  in frame, by OBJECT, product dimension against delta:")
    for k in sorted(joint):
        print(f"    dim {k[0]}, delta {k[1]}: {joint[k]:4d} objects")
    # the exact face check, where the enumerator applies
    ok = checked = 0
    for rs in objs.values():
        r = rs[0]
        if r["dim"] != 2:
            continue
        pts = exps(sympy.expand(sympy.prod(r["facs"][0])), r["gens"])
        exact = exact_proper_faces(pts)
        seen = set()
        for w in weight_box(len(r["gens"]), r["radius"]):
            seen.add(frozenset(face_support(pts, w)))
        checked += 1
        ok += not (exact - seen)
    print(f"  objects at dim 2: {checked}; weight sample complete at {ok}")
    check(f"S2 [{label}] the weight sample produced EVERY proper face of the"
          " Newton polygon at every dimension-2 object",
          checked > 0 and ok == checked)
    return objs, len(allobj) - len(objs)


# ==================================================== S3  the criterion
def split_of_collision(r):
    """(p, n, q, spectators) for a collision, read off the counter's blocks.

    The two factorizations agree on some blocks and differ on the rest. Every
    collision either box produces differs on exactly two: {p, n*q} against
    {p*n, q}, with the agreeing blocks -- SPECTATORS -- riding along. They
    contribute the same primitive initial form to both sides at every weight,
    so they cancel from the comparison and the algebra of the hand-attack is
    untouched by their presence. Recovered from the counter's own output
    rather than from the generator, so the criterion is tested against the
    reading that produced delta.
    """
    f1 = list(r["facs"][0])
    f2 = list(r["facs"][1])
    spect, rest2 = [], list(f2)
    d1 = []
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


def nonmono(expr, gens, w):
    return len(sympy.Poly(initial_form(expr, gens, w), *gens).monoms()) > 1


def stage3(objs, label):
    print(f"\n=== S3  the criterion [{label}] ===")
    rows, faces, agree, sep_tot = [], 0, 0, 0
    bad_nec, bad_suf = [], []
    for key, rs in objs.items():
        r = rs[0]
        p, n, q, spect = split_of_collision(r)
        if p is None:
            rows.append(dict(r=r, p=None))
            continue
        g = r["gens"]
        seen = {}
        pts = exps(sympy.expand(sympy.prod(r["facs"][0])), g)
        for w in weight_box(len(g), r["radius"]):
            seen.setdefault(frozenset(face_support(pts, w)), w)
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
        # the parallel-edge reading
        dn = [tuple(a - b for a, b in zip(u, v))
              for u, v in combinations(exps(n, g), 2)]
        dp = [tuple(a - b for a, b in zip(u, v))
              for u, v in combinations(exps(p, g), 2)][0]
        dq = [tuple(a - b for a, b in zip(u, v))
              for u, v in combinations(exps(q, g), 2)][0]
        edge = False
        for w in weight_box(len(g), r["radius"]):
            if not nonmono(n, g, w):
                continue
            if nonmono(p, g, w) or nonmono(q, g, w):
                edge = True
                break
        rows.append(dict(r=r, p=p, n=n, q=q, suits=len(rs), spect=len(spect),
                         dp=dp, dq=dq, ndirs=rank_int(dn) if dn else 0,
                         nterms=len(exps(n, g)), pred=1 if edge else r["dim"],
                         seedrank=max(poly_rank(menu_poly(r["A"])),
                                      poly_rank(menu_poly(r["B"]))),
                         nvars=len(g)))
    print(f"  faces examined: {faces} over {len(objs)} objects,"
          f" {sep_tot} of them separating; criterion agreed at {agree}")
    check(f"S3 [{label}] the criterion recovered p, n and q at every object",
          all(row["p"] is not None for row in rows))
    check(f"S3 [{label}] no face separates where the criterion forbids it"
          " -- the PROVED half (K2)", not bad_nec)
    check(f"S3 [{label}] no face fails to separate where the criterion allows"
          " it -- the sufficient half (K3)", not bad_suf)
    graded = [row for row in rows if row["p"] is not None]
    check(f"S3 [{label}] the parallel-edge reading predicts delta at every"
          " in-frame object (K4)",
          all(row["pred"] == row["r"]["delta"] for row in graded))
    print("\n  THE TABLE -- every in-frame object, one line"
          "  (suits | dim delta | criterion | spectators | seed rank"
          " | n: terms, rank)")
    for row in sorted(graded, key=lambda z: (-z["r"]["delta"], -z["suits"])):
        r = row["r"]
        print(f"    {row['suits']:2d}x  dim {r['dim']} delta {r['delta']}"
              f"  crit {row['pred']}  spect {row['spect']}"
              f"  seedrank {row['seedrank']}  nvars {row['nvars']}"
              f"  n[{row['nterms']}t rank {row['ndirs']}]"
              f"   {set(r['A'])} x {set(r['B'])}")
    full = [row for row in graded if row["r"]["delta"] >= 2]
    print(f"  delta >= 2 objects: {len(full)}")
    for row in full:
        print(f"    n = {row['n']}   p = {row['p']}   q = {row['q']}")
    return rows


# ==================================================================== driver
def run_box(box, label):
    print(f"\n=== S1  the generation [{label}]  box {{2..{max(box)}}} ===")
    found, tscan = generate(box, label)
    objs, outobj = grade(found, label)
    rows = stage3(objs, label)
    return objs, outobj, rows, tscan


def main():
    t0 = time.time()
    stage0()
    objs, outobj, _, _ = run_box(PILOT, "pilot {2..24}")
    d2 = [rs[0] for rs in objs.values() if rs[0]["delta"] >= 2]
    check("S0d the generator reproduces the published pilot box: 8 in-frame"
          " objects, 7 at delta 1 and 1 at delta 2 (K1)",
          len(objs) == 8 and len(d2) == 1)
    check("S0d the pilot delta=2 object is the published witness (K1)",
          len(d2) == 1 and
          {tuple(sorted(d2[0]["A"])), tuple(sorted(d2[0]["B"]))} ==
          {(2, 3), (3, 4, 8, 9, 18, 24)})
    if any(not v for _, v in CHECKS):
        print("\nPILOT CONTROL FAILED -- the wide box is not walked.")
        for n, v in CHECKS:
            if not v:
                print(f"  FAIL {n}")
        return 1
    if "--pilot" not in sys.argv:
        objs, outobj, _, tscan = run_box(WIDE, "wide {2..32}")
        d2 = [rs[0] for rs in objs.values() if rs[0]["delta"] >= 2]
        check("S1 the wide box reproduces the published 22 in-frame objects,"
              " 21 at delta 1 and 1 at delta 2 (K1)",
              len(objs) == 22 and len(d2) == 1)
        check("S1 the wide box reproduces the published 4 out-of-frame"
              " objects (K1)", outobj == 4)
        print(f"\n  PR5 the generator's scan of the wide box: {tscan:.1f} s,"
              f" against the 4,126.3 s census it replaces")
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time()-t0:.1f}s")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
