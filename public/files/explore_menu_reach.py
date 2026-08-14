"""Menu factorization, second aim: does the mechanism escape one variable?

THE QUESTION. A MENU is a finite set of integers >= 2; it becomes the
Dirichlet polynomial Z_A(beta) = sum over m in A of m^-beta, and
substituting x_i = p_i^-beta makes it a polynomial in N[x_1..x_r] whose
coefficients are all 0 or 1. Two menus with equal products are
indistinguishable at every temperature, and that is a FACTORIZATION
question exactly where factorization in this semiring is non-unique.
The companion file explore_menu_factorization.py established the SEED
CRITERION: non-uniqueness requires a menu whose polynomial carries a
Z-irreducible factor with a negative coefficient, and every such factor
found there -- over menus of size <= 3 with elements <= 81 -- had a
Newton polygon of DIMENSION 1, the signature of a monomial substitution
or a weighted homogenization applied to a one-variable polynomial. The
open question it left: is every non-uniqueness in this semiring an
image of the one-variable one?

THE INCUMBENT, READ FULL-TEXT BEFORE THIS SLATE WAS WRITTEN, and it is
why this file exists in the shape it does. Factorization of polynomials
with nonnegative integer coefficients is a studied subject. The
governing reference is C. van de Woestijne, "Factors of disconnected
graphs and polynomials with nonnegative integer coefficients" (2011),
which parametrises factorizations in this semiring and classifies them
by the NUMBER OF TERMS t = P(1) rather than by degree; the multiplicative
monoid's ideal theory is Campanini and Facchini, "Factorizations of
polynomials with integral non-negative coefficients" (Semigroup Forum
99, 2019), which is not used here. Four of that first paper's results
bear directly, and together they REPLACE the sweep this file was
originally going to run:

 (L3.3) If P has t terms and factors as S*T with s and t' terms, then
        t = s*t'. If P's monomials are distinct, so are each factor's.
        (Independently derived in the companion file; noted as prior.)
 (L3.4) t prime => P factors uniquely.
 (L3.10) THE REDUCTION. Writing each polynomial by its exponent VECTORS,
        a factorization of P in N[x_1..x_m] is exactly a compatible
        tuple of factorizations of its m coordinate projections sharing
        one term-bijection sigma. Multivariate factorization is
        univariate factorization done coordinate by coordinate.
 (T3.16-3.20) t = 4, 8 and 9 factor UNIQUELY. t = 6 is non-unique only
        for X^a(1 + X^b + ... + X^5b). t = 10 is non-unique only for
        three sporadic polynomials and TWO 2-PARAMETER FAMILIES, of
        which the first is
           (1 + X^3b)(1 + X^a + X^b + X^{a+b} + X^{a+2b})
         = (1 + X^b)(1 + X^a + X^{a+2b} + X^3b + X^{a+4b}).

WHAT THAT BUYS, hand-derived here before any engine code.
 (a) MENU SIZES ARE THE GRADING. Two menus of sizes s1 and s2 have a
     product with t = s1*s2 terms, so the literature's t-classification
     is a classification by SIZE PAIR. Sizes (2,2), (2,4) and (3,3) give
     t = 4, 8, 9: UNIQUE, at any element bound, by theorem rather than
     by sweep. So the size-4 sweep this file was planned as -- size-4
     menus against size-2, at the cost of a million factorizations --
     was aimed at a t-value already settled in the negative.
 (b) t = 6 FORCES COLLINEARITY, which is the corpus's conjecture proved
     at that size pair. If a product of a size-2 and a size-3 menu
     factors non-uniquely, then by (L3.10) some coordinate projection is
     the 6-term non-unique polynomial of (T3.17), and the two term-
     bijections are thereby pinned; every OTHER coordinate must solve
     the same linear system, whose general solution makes its exponents
     an arithmetic progression too. So the exponent VECTORS are an
     arithmetic progression along a single direction v in Z^m: the
     support is collinear, the Newton polygon is a segment, and every
     factor's polygon is a sub-segment of it. Sign of v is unconstrained,
     which is exactly the difference between a monomial substitution
     (v nonnegative) and a weighted homogenization (v mixed) -- the two
     rungs the corpus had already seen, and there is no third at t = 6.
 (c) t = 10 DOES NOT. The two-parameter family above has TWO free
     exponents a and b, and (L3.10) lets them be independent VECTORS.
     Setting u = X^a and v = X^b as separate variables the identity
     reads (1 + v^3)(1 + u + v + uv + uv^2)
          = (1 + v)(1 + u + uv^2 + v^3 + uv^4),
     both sides expanding to the same 10 distinct monomials, every
     factor having 0/1 coefficients and a prime number of terms (2 and
     5), hence irreducible in the semiring by (L3.4). Its support is NOT
     collinear. So a non-uniqueness that is not an image of a
     one-variable polynomial exists, and the cheapest place it lives is
     the size pair (2,5) -- not (2,4), and not any element bound on
     sizes <= 4.
 (d) THE NEGATIVE FACTOR IS STILL ONE-VARIABLE. Dividing, the identity
     is driven by 1 + v^3 = (1 + v)(1 - v + v^2) and
     (1 + v + v^2)(1 - v + v^2) = 1 + v^2 + v^4: the same cyclotomic
     mechanism, run over the coefficient semiring N[u] instead of N.
     The negative Z-irreducible is 1 - v + v^2, Newton dimension 1. So
     the observable the companion file minted -- the Newton dimension of
     the NEGATIVE FACTOR -- does not fire on (c) either. The second
     variable enters through the CO-FACTOR, and a dimension-1 negative
     factor is compatible with a mechanism that is not a one-variable
     image. This is the second spectator in this line of work: the first was
     the product's variable count, raised for free by a monomial factor.

THE SPECIMEN, hand-built from (c) at the freeze. Read u = 5, v = 3 and
shift by 2 so every element is >= 2:
    A = {2, 54}                  C = {2, 6}
    B = {2, 6, 10, 30, 90}       D = {2, 10, 54, 90, 810}
Hand-multiplied, both products are the 10-element set
    {4, 12, 20, 60, 108, 180, 324, 540, 1620, 4860}.
Its top element 4860 and B's and D's size 5 are jointly why no sweep
run in this corpus could have met it: every census so far stopped at
size 3 and element 81.

WHAT IS ASKED HERE, in three parts. (1) Verify the specimen as an
object of this corpus -- equal products, two factorizations, and the
Newton dimensions of the product, of each factor, and of each negative
factor. (2) TEST THE TRANSFER, because (L3.16-3.20) are stated for ONE
variable and every use above routes them through (L3.10): sweep menu
size pairs exhaustively at a stated element bound and check that t = 4,
8 and 9 are unique for MENUS in several variables, with t = 6 as the
positive control that the rig can see non-uniqueness at all. (3) Ask the
corrected question of everything found: does any NEGATIVE Z-irreducible
factor anywhere have a Newton polygon of dimension >= 2?

DESIGN, four stages.
 S1 CONTROL, the counter read in both directions. The cyclotomic core
    (1+x+x^2)(1+x^3) must print exactly 2 semiring-irreducible
    factorizations and x*y*(1+x) must print exactly 1. A counter that
    cannot print 2, or cannot print 1, decides nothing downstream.
 S2 THE SPECIMEN. A*B and C*D compared as integer multisets; the common
    product's semiring-irreducible factorizations enumerated in full;
    the Newton dimension of the product, of every factor in every
    factorization, and of every negative Z-irreducible factor.
 S3 THE TRANSFER SWEEP, over the size pairs where a THEOREM is being
    tested and nowhere else. Every menu of size 2 and 3 with elements in
    {2..32}, and of size 4 with elements in {2..24}, is factored over Z
    once and cached. Because the Z-factors of a product are the union of
    the factors' -- the seed criterion -- no product is ever factored: a
    pair's factor multiset is the concatenation of two cached ones, and
    only pairs where at least one menu is a SEED can be non-unique, so
    only those are counted. For each size pair, printed: the number of
    products that factor non-uniquely, and for each such product its
    Newton dimension. The pairs swept are (2,2), (2,4) and (3,3) -- the
    three the literature calls UNIQUE, t = 4, 8, 9 -- and (2,3), t = 6,
    the positive control. THE BOXES ARE SET BY MEASURED COST, not by an
    argument that they are the right ones: at 2.1 ms per pair the two
    remaining pairs (3,4) and (4,4) are 18 and 90 minutes, far over the
    wall-clock line, and they are the two the literature leaves open, so
    sweeping them would buy a box-sized answer to an unbounded question.
    (SETTLING POINTER, added later: the (3,4) figure is wrong by about
    4.4x. The per-pair rate stands -- 2.6 ms measured against the 2.1 ms
    quoted -- but the PAIR COUNT does not: the walk is bounded by the SEED
    count, not the menu count, so (3,4) is 85,253 pairs and runs in just
    over four minutes. It has since been swept, with the descent dimension
    graded on every collision it holds; see explore_descent_hunt.py. The
    (4,4) figure rests on the same derivation and remains unmeasured.)
 S3b THE OPEN RUNGS, as named constructions rather than a sweep. The
    hand-derived t = 12 instance below is checked directly, and so is
    the t = 16 doubling that the same reasoning predicts stays unique.
 S4 THE CORRECTED OBSERVABLE. Over every non-unique product found in S2
    and S3, the maximum Newton dimension of a negative Z-irreducible
    factor.

PREDICTIONS (fixed before the engine, and before any run).
  PR1 (S1): 2 for the cyclotomic core, 1 for the monomial specimen.
  PR2 (S2): A*B and C*D are the same 10-element set; it carries exactly
      2 semiring-irreducible factorizations; the product's Newton
      dimension is 2; the four factors' dimensions are 1, 2, 1, 2; the
      only negative Z-irreducible factor is 1 - v + v^2, dimension 1.
  PR3 (S3, positive control): the (2,3) pair, t = 6, yields at least one
      non-unique product, and EVERY one it yields has product Newton
      dimension 1. The second half is (b) above, and it is the one that
      can fail while the first holds.
  PR4 (S3, the transferred theorems): ZERO non-unique products at size
      pairs (2,2), (2,4) and (3,3), i.e. at t = 4, 8 and 9.
  PR5 (S3b, the open rungs): the hand-derived t = 12 instance factors
      NON-uniquely. {2,8,32} has core (1+x+x^2)(1-x+x^2) and {2,4,16,32}
      has core (1+x)^2(1-x+x^2), so the product's factor multiset admits
      both {(1+x^2+x^4), (1+x^3), (1+x)} and {(1+x^3), (1+x^3),
      (1+x+x^2)} -- two, and it uses one variable. The t = 16 doubling
      {2,4,16,32} against itself has core (1+x)^4(1-x+x^2)^2, whose only
      atomic nonnegative blocks are 1+x and 1+x^3, so it factors
      UNIQUELY as (1+x^3)^2(1+x)^2. Both are predictions about named
      objects, not about a box.
  PR6 (S4, the decision observable): the maximum is 1. No negative
      Z-irreducible factor anywhere here has a two-dimensional Newton
      polygon, so the conjecture SURVIVES in the corrected form -- a
      negative irreducible factor of a 0/1-coefficient product has
      collinear exponents -- even though the surrounding claim it was
      part of, that every non-uniqueness is a one-variable image, does
      not survive S2.

FINDINGS (tiers per the standard naming scale; run record below).

0. TWO CORRECTIONS TO THE SLATE ABOVE, found by the audit that followed
   the run. The slate is left as frozen and both are stated here.
   (i) THE INCUMBENT IS UNDER-CREDITED, in the direction that flatters
   this file. The slate says the uniqueness results are stated for ONE
   variable and that S3 therefore tests their transfer. They are so
   stated, but the SEVERAL-variable statement is the same paper's own
   Theorem 1.1, proved there by exactly the reduction the slate cites:
   a polynomial in countably many variables corresponds to a graph, and
   uniqueness at 4, 8 and 9 components is that theorem. So S3 is an
   independent CONFIRMATION at this corpus's own objects, not the
   closing of a gap the literature left open, and finding 5 should be
   read at that weight.
   (ii) THE t = 6 DERIVATION IN (b) OMITS THE STEP THAT MAKES ITS OWN
   CONCLUSION POSSIBLE. As written it takes the combined linear system's
   solution space to be the one-dimensional progression the source
   normalises to, which would force the direction NONNEGATIVE and
   contradict the same paragraph's claim that its sign is free. The
   system is translation-invariant -- adding a constant to every
   exponent multiplies by a monomial -- so the space is TWO-dimensional,
   spanned by the all-ones vector and one progression vector v
   (computed: rank 4 in 6 unknowns). Each coordinate j is therefore
   alpha_j * 1 + beta_j * v, so term i has exponent vector
   alpha + v_i * beta: collinear along beta, with beta's sign free per
   coordinate. That is what separates substitution from homogenization,
   and the conclusion of (b) stands on it rather than on what (b) says.

   (iii) THE ELEMENT BOUND IS NOT A BINDING DIAL, and finding 2 below
   says it is. The first specimen tops out at menu element 810 because
   it reads the family at u = 5, v = 3; read at the cheapest primes the
   SAME family gives {2,16} x {2,4,6,12,24} against {2,4} x
   {2,6,16,24,96}, largest menu element 96, two factorizations and the
   same two-dimensional polygon (S2b). So what hid this from every
   census here is menu SIZE 5, which no sweep in this corpus has ever
   reached, and NOT the joint movement of two dials: 96 is barely past
   the size-3 map's element bound of 81. Finding 2's "both dials had to
   move at once" is wrong, and it was wrong in the direction that makes
   the miss look less avoidable than it was.

1. THE INCUMBENT RETIRES THE PLANNED SWEEP (prior result, applied).
   Factorization here is classified by the NUMBER OF TERMS, and two
   menus of sizes s1 and s2 make a product with s1*s2 terms, so the
   literature's t-classification is a classification by SIZE PAIR. Size
   pairs (2,2), (2,4) and (3,3) carry t = 4, 8, 9, all three UNIQUE by
   theorem at ANY element bound. The sweep this file was planned as --
   size-4 menus against size-2, priced at roughly 22 minutes of
   factorization -- was therefore aimed at a value already settled in
   the negative, and no element bound could have changed its answer.

2. THE ONE-VARIABLE CONJECTURE IS FALSE (construction, verified
   exactly). The menus {2,54} x {2,6,10,30,90} and {2,6} x
   {2,10,54,90,810} have the same product, the 10-element set
   {4,12,20,60,108,180,324,540,1620,4860}, which carries exactly two
   semiring-irreducible factorizations. Its Newton polygon is
   TWO-DIMENSIONAL, and so are two of its four factors, so this
   non-uniqueness is not the image of any one-variable polynomial under
   substitution or homogenization. It comes from the incumbent's
   two-parameter family at t = 10, whose two free exponents may be
   independent VECTORS; read as menus that is the size pair (2,5), with
   a top element of 4860. Both dials -- size and element bound -- had to
   move at once, which is why no census in this corpus could have met
   it: every one stopped at size 3 and element 81.

3. THE MINTED OBSERVABLE IS THE SECOND SPECTATOR (observation, and it
   is the finding worth carrying). The negative Z-irreducible factor of
   finding 2 is x^2 - x + 1: ONE variable, Newton dimension 1, the same
   cyclotomic factor the corpus has had all along. The second variable
   enters through the CO-FACTORS, which are the two-dimensional ones.
   So the Newton dimension of the negative factor does not grade
   whether a mechanism is a one-variable image -- it is dimension 1 on
   a mechanism that is not. The companion file minted that observable
   to replace the product's VARIABLE COUNT, which failed because a
   monomial factor raises it for free; the replacement fails for the
   opposite reason, reading only the part of the product where the new
   structure is absent. Two observables, two spectators, and what
   separates them from the real question is the same thing both times:
   the mechanism lives in the RELATION between the factors, and neither
   observable reads more than one factor at a time.

4. AT t = 6 COLLINEARITY IS FORCED (rule, proved at that size pair;
   exhaustively confirmed at scope). If a size-2 and a size-3 menu have
   a non-uniquely factoring product, the reduction pins both term-
   bijections, every coordinate must solve one linear system, and the
   exponent vectors are an arithmetic progression along a single
   direction. So the polygon is a segment and the mechanism IS a
   one-variable image -- substitution where the direction is
   nonnegative, weighted homogenization where it is mixed, and there is
   no third rung there. All 39 non-unique products the sweep found at
   t = 6 have product Newton dimension 1, 39 of 39.

5. THE UNIVARIATE THEOREMS TRANSFER TO MENUS IN SEVERAL VARIABLES
   (observation, exhaustive at the stated boxes). Zero non-unique
   products among 1,854 pairs at t = 4, 43,257 at t = 8 and 4,495 at
   t = 9. This is the step every use of the literature here routes
   through, and it is measured rather than assumed.

6. THE CORRECTED CONJECTURE SURVIVES (observation, over everything
   found here). No negative Z-irreducible factor anywhere in this file
   -- the t = 10 specimen, the 39 products at t = 6, the t = 12
   instance -- has a Newton polygon of dimension >= 2. What remains
   open, and is now the sharp statement because it outlived the frame
   it was born in, is whether a negative irreducible factor of a
   0/1-coefficient POLYNOMIAL must have collinear exponents at all.
   (SETTLED SINCE, and the answer is NO: the full-dimension collision's
   seed core is (x0 + 1)(x0^2 x1 + x0^2 - x0 x1 + x1^2 + x1), whose
   second factor is Z-irreducible, negative and of Newton dimension 2 --
   explore_descent26.py and explore_descent26_why.py. What survives here
   is the scope this file actually walked, where the maximum is 1.) The
   object is the polynomial and not the product: a product of two menus
   need not have 0/1 coefficients, while its Z-factors are exactly the
   two menus' own, so the menus are where the property lives.

7. THE TWO OPEN RUNGS, one point each. At t = 12 the pair {2,8,32} x
   {2,4,16,32} factors in exactly 2 ways and is collinear; at t = 16
   the doubling {2,4,16,32} x {2,4,16,32} factors uniquely, its only
   atomic nonnegative blocks being 1 + x and 1 + x^3. The literature
   classifies t <= 10, so these two are observations about two objects
   and say nothing about their size pairs.

THE HEADLINE (settled further by explore_menu_faces.py, which supplies
the instrument finding 3 says is missing: a collision restricts to every
FACE of its Newton polytope, and the DESCENT DIMENSION built on that
reads the two factorizations jointly. Under it this file's escape is the
cyclotomic identity seen on an edge, so "escapes the images of one
variable" survives exactly as written and "escapes one variable" does
not -- the mechanism is inherited from one variable on a face, at every
object this corpus or the literature reaches below t = 12). The
mechanism DOES escape the images of one variable, and
the corpus was looking in the wrong place with the wrong instrument. The
escape needs menu sizes 2 and 5, not 4; the size pairs reachable by
sizes <= 4 are either settled unique by theorem (t = 4, 8, 9) or forced
collinear (t = 6). And the escape is invisible to the observable minted
to detect it, because the negative factor stays one-variable while the
co-factors carry the second -- so what survives as the open question is
the narrower claim about negative factors, not the wide one about
mechanisms, which is now false.

KILLS (observables with live failure modes; the meaning is weighed
after the run, never before).
  K1: either S1 number is wrong -- the counter is broken and nothing
      downstream is read.
  K2: S2's two products differ, or the factorization count is not 2 --
      the specimen is wrong, the incumbent identity was misapplied, and
      the whole reading of (c) falls.
  K3: any non-unique product at t = 4, 8 or 9 -- the univariate
      uniqueness theorems do NOT transfer to menus in several variables,
      which would mean the reduction is being misused here, and (a)'s
      retirement of the size-4 sweep would be void.
  K4: a t = 6 non-unique product of Newton dimension >= 2 -- the
      collinearity derivation (b) is wrong.
  K5: a negative Z-irreducible factor of Newton dimension >= 2 anywhere
      -- the corrected conjecture dies too. This is the outcome worth
      hunting and the one this line of work has never had.

HONEST LIMITS carried into the reading. (i) S3 is exhaustive only over
the four size pairs and the two boxes named there; the size-5 menus the
specimen needs are outside every box by cost (measured: ~1.9 ms to
factor one menu, and C(31,5) is 169,911 of them, before any pairing),
so S2's specimen is a CONSTRUCTION checked exactly, never a sweep
result -- and the same is true of both S3b instances. (ii) t = 12 and
16 are therefore touched at two points and not swept at all; the
literature classifies t <= 10 only, so what this file says about them
is what those two objects do and nothing wider. (iii) The
counts rest on the unique-factorization argument in the companion file
and on sympy's multivariate integer factorization, whose only guard here
is S1. (iv) Nothing here is a realization claim: whether these menus
assemble into an actual dated fiber is a separate question, settled by
explore_rogue_world.py only inside its own smaller scope.
RUN RECORD (this file, under memwatch.py at the 512MB default, 172.6 s
wall, peak working set 68.0 MB). Run 1: 16/16 at 179.4 s, all four
stages green, every prediction PR1-PR6 held as written and no kill
fired. The sweep found 4 size-2 seeds, 1 size-3 seed and 17 size-4
seeds in its boxes, and 39 non-unique products, all at t = 6.
The boxes and the four swept size pairs were set by MEASURED cost
before the slate was frozen -- 0.7/1.0/1.6/1.9 ms to factor one menu at
sizes 2/3/4/5 and 2.1 ms to grade one pair -- which is what put the
(3,4) and (4,4) sweeps, at 18 and 90 minutes, outside this file and
left them as the two named constructions of S3b.
Run 2 (this record): the audit round added S2b, the same family read at
its cheapest primes, after finding 2's claim that the element bound was
a binding dial turned out to be false -- and renamed one S2b check whose
name and assertion described different facts. 19/19, wall unmoved within
noise. The five predictions the slate names are untouched by both runs;
S2b answers a question the audit asked, not one the slate froze, and it
is labelled so.
Post-run edits: correction 0, this findings block, this run record and
the S2b stage; the slate, the predictions, the kills and the rest of the
engine untouched.
"""

import os
import sys
import time
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import Poly, symbols

CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))
    print(("PASS  " if ok else "FAIL  ") + name)


# ------------------------------------------------------------ menu -> polynomial
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
X = symbols(' '.join(f'x{i}' for i in range(len(PRIMES))))


def monomial(m):
    t, rest = 1, m
    for i, p in enumerate(PRIMES):
        while rest % p == 0:
            rest //= p
            t *= X[i]
    assert rest == 1, f"element {m} outside the prime list"
    return t


def menu_poly(A):
    return sympy.expand(sum(monomial(m) for m in A))


def used_vars(expr):
    return [x for x in X if expr.has(x)]


def newton_dim(expr, gens):
    """Affine dimension of the exponent-vector set."""
    pts = [list(mon) for mon in Poly(expr, *gens).monoms()]
    if len(pts) < 2:
        return 0
    base = pts[0]
    rows = [[a - b for a, b in zip(p, base)] for p in pts[1:]]
    return sympy.Matrix(rows).rank()


# -------------------------------------------------------- Z-factors of one menu
def zfactors(expr):
    """(monomial variables, core Z-irreducibles), each positive-leading."""
    content, fl = sympy.factor_list(expr)
    assert content == 1, f"non-unit content {content}"
    mons, core = [], []
    for f, mult in fl:
        for _ in range(mult):
            (mons if f in X else core).append(sympy.expand(f))
    return mons, core


def is_nonneg(expr, gens):
    return all(c >= 0 for c in Poly(expr, *gens).coeffs())


def has_negative(expr, gens):
    return not is_nonneg(expr, gens)


# ------------------------------------ semiring-irreducible factorization counter
def block_product(core, idxs):
    out = 1
    for i in idxs:
        out *= core[i]
    return sympy.expand(out)


def set_partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i] + [[first] + part[i]] + part[i + 1:]
        yield [[first]] + part


def is_atomic(core, idxs, gens, cache):
    """No bipartition of this block into two nonnegative sub-products."""
    key = tuple(sorted(idxs))
    if key in cache:
        return cache[key]
    n = len(idxs)
    verdict = True
    if n > 1:
        for r in range(1, n // 2 + 1):
            for sub in combinations(idxs, r):
                rest = [i for i in idxs if i not in set(sub)]
                if (is_nonneg(block_product(core, sub), gens)
                        and is_nonneg(block_product(core, rest), gens)):
                    verdict = False
                    break
            if not verdict:
                break
    cache[key] = verdict
    return verdict


def count_from_core(core, gens):
    """Distinct semiring-irreducible factorizations, given the core factors.

    Monomial factors are dropped by the caller: a monomial always splits
    off alone, so it multiplies the count by one.
    """
    cache, found = {}, {}
    for part in set_partitions(list(range(len(core)))):
        blocks = []
        for idxs in part:
            b = block_product(core, idxs)
            if not is_nonneg(b, gens):
                break
            if not is_atomic(core, idxs, gens, cache):
                break
            blocks.append(b)
        else:
            found[tuple(sorted(sympy.srepr(b) for b in blocks))] = blocks
    return len(found), list(found.values())


def n_factorizations(expr):
    gens = used_vars(expr) or [X[0]]
    _, core = zfactors(expr)
    return count_from_core(core, gens)


# ============================================================ S1  the controls
def stage1():
    print("\n=== S1  the counter, read in both directions ===")
    x, y = X[0], X[1]
    cyclo = sympy.expand((1 + x + x**2) * (1 + x**3))
    n, facs = n_factorizations(cyclo)
    print(f"  (1+x+x^2)(1+x^3) -> {n} semiring-irreducible factorizations")
    for f in facs:
        print("      " + "  *  ".join(str(b) for b in f))
    check("S1 cyclotomic core prints 2", n == 2)

    mono = sympy.expand(x * y * (1 + x))
    m, _ = n_factorizations(mono)
    print(f"  x*y*(1+x)        -> {m} (monomial factors dropped)")
    check("S1 monomial specimen prints 1", m == 1)


# ============================================================ S2  the specimen
SPEC_A = (2, 54)
SPEC_B = (2, 6, 10, 30, 90)
SPEC_C = (2, 6)
SPEC_D = (2, 10, 54, 90, 810)


def product_multiset(A, B):
    out = {}
    for a in A:
        for b in B:
            out[a * b] = out.get(a * b, 0) + 1
    return out


def stage2():
    print("\n=== S2  the specimen the incumbent's t=10 family supplies ===")
    print(f"  A = {set(SPEC_A)}   B = {set(SPEC_B)}")
    print(f"  C = {set(SPEC_C)}   D = {set(SPEC_D)}")
    ab = product_multiset(SPEC_A, SPEC_B)
    cd = product_multiset(SPEC_C, SPEC_D)
    print(f"  A*B = {sorted(ab)}")
    print(f"  C*D = {sorted(cd)}")
    check("S2 the two products agree as multisets", ab == cd)
    check("S2 the product is a 10-element SET (no repeats)",
          len(ab) == 10 and set(ab.values()) == {1})

    P = sympy.expand(menu_poly(SPEC_A) * menu_poly(SPEC_B))
    gens = used_vars(P)
    mons, core = zfactors(P)
    n, facs = count_from_core(core, gens)
    print(f"  variables used: {len(gens)};  monomial factors: {len(mons)}")
    print(f"  semiring-irreducible factorizations: {n}")
    dims = []
    for f in facs:
        row = []
        for b in f:
            d = newton_dim(b, gens)
            row.append(d)
            print(f"      {b}    [Newton dim {d}]")
        dims.append(row)
        print("      ---")
    check("S2 the product factors in exactly 2 ways", n == 2)
    pdim = newton_dim(sympy.expand(block_product(core, range(len(core)))), gens)
    print(f"  product core Newton dimension: {pdim}")
    check("S2 the product's Newton polygon is 2-dimensional", pdim == 2)
    flat = sorted(d for row in dims for d in row)
    print(f"  factor Newton dimensions (sorted): {flat}")
    check("S2 the factor dimensions are 1,1,2,2", flat == [1, 1, 2, 2])

    negs = [f for f in core if has_negative(f, gens)]
    print(f"  negative Z-irreducible factors: {[str(f) for f in negs]}")
    ndims = [newton_dim(f, gens) for f in negs]
    print(f"  their Newton dimensions: {ndims}")
    check("S2 exactly one negative Z-irreducible, of dimension 1",
          len(negs) == 1 and ndims == [1])
    return max(ndims) if ndims else 0


# ================================== S2b  the same family at its cheapest reading
SPEC2_A = (2, 16)
SPEC2_B = (2, 4, 6, 12, 24)
SPEC2_C = (2, 4)
SPEC2_D = (2, 6, 16, 24, 96)


def stage2b():
    """The audit's question: is the element bound really a binding dial?"""
    print("\n=== S2b  the same family read at its cheapest primes ===")
    print(f"  A = {sorted(SPEC2_A)}   B = {sorted(SPEC2_B)}")
    print(f"  C = {sorted(SPEC2_C)}   D = {sorted(SPEC2_D)}")
    ab = product_multiset(SPEC2_A, SPEC2_B)
    cd = product_multiset(SPEC2_C, SPEC2_D)
    print(f"  common product: {sorted(ab)}")
    check("S2b the two products agree as multisets", ab == cd)
    P = sympy.expand(menu_poly(SPEC2_A) * menu_poly(SPEC2_B))
    gens = used_vars(P)
    _, core = zfactors(P)
    n, _ = count_from_core(core, gens)
    d = newton_dim(block_product(core, range(len(core))), gens)
    negs = [f for f in core if has_negative(f, gens)]
    nd = [newton_dim(f, gens) for f in negs]
    print(f"  factorizations {n}, product Newton dimension {d}")
    print(f"  negative Z-irreducible factors {[str(f) for f in negs]},"
          f" dimensions {nd}")
    print(f"  largest menu element {max(max(SPEC2_B), max(SPEC2_D))},"
          f" against {max(max(SPEC_B), max(SPEC_D))} for the first reading")
    check("S2b it is the same phenomenon: 2 factorizations, dimension 2",
          n == 2 and d == 2)
    check("S2b even the cheapest reading needs an element past 81, but only"
          " just -- so SIZE is the dial that hid this, not the bound",
          max(max(SPEC2_B), max(SPEC2_D)) == 96)
    return max(nd) if nd else 0


# ==================================================== S3  the transfer sweep
BOX_SMALL = list(range(2, 33))    # sizes 2 and 3
BOX_BIG = list(range(2, 25))      # size 4, where the menu count grows fastest
PAIRS_SWEPT = ((2, 2), (2, 3), (2, 4), (3, 3))


def stage3():
    print("\n=== S3  the transfer sweep over the four size pairs a theorem"
          " reaches ===")
    print("  boxes: sizes 2,3 over {2..32};  size 4 over {2..24}")
    t0 = time.time()
    menus, cores, gensof, seeds = {}, {}, {}, {}
    for s in (2, 3, 4):
        box = BOX_BIG if s == 4 else BOX_SMALL
        menus[s] = [tuple(c) for c in combinations(box, s)]
        seeds[s] = []
        for A in menus[s]:
            P = menu_poly(A)
            g = used_vars(P)
            _, core = zfactors(P)
            cores[A] = core
            gensof[A] = g
            if any(has_negative(f, g) for f in core):
                seeds[s].append(A)
        print(f"  size {s}: {len(menus[s]):6d} menus, {len(seeds[s]):4d} seeds"
              f"   [{time.time()-t0:.1f}s]")
    for s in (2, 3, 4):
        shown = ", ".join(str(set(A)) for A in seeds[s][:8])
        print(f"    size-{s} seeds: "
              + ((shown + (" ..." if len(seeds[s]) > 8 else ""))
                 if seeds[s] else "(none)"))

    results, maxneg = {}, 0
    for s1, s2 in PAIRS_SWEPT:
        pairs = set()
        for S in seeds[s1]:
            for M in menus[s2]:
                pairs.add(tuple(sorted((S, M))))
        for S in seeds[s2]:
            for M in menus[s1]:
                pairs.add(tuple(sorted((S, M))))
        nonuniq = []
        for A, B in pairs:
            n, d, nd = grade_pair(cores, gensof, A, B)
            if n > 1:
                maxneg = max(maxneg, nd)
                nonuniq.append((A, B, n, d, nd))
        results[(s1, s2)] = nonuniq
        dims = sorted({d for _, _, _, d, _ in nonuniq})
        print(f"  sizes ({s1},{s2})  t={s1*s2:2d}  pairs {len(pairs):7d}"
              f"   NON-UNIQUE {len(nonuniq):5d}"
              f"   product Newton dims {dims if dims else '-'}"
              f"   [{time.time()-t0:.1f}s]")
        for A, B, n, d, nd in nonuniq[:3]:
            print(f"        {set(A)} x {set(B)}  ->  {n} factorizations,"
                  f" product dim {d}, negative-factor dim {nd}")

    check("S3 t=4 has no non-unique product", not results[(2, 2)])
    check("S3 t=8 has no non-unique product", not results[(2, 4)])
    check("S3 t=9 has no non-unique product", not results[(3, 3)])
    check("S3 t=6 has some (positive control)", bool(results[(2, 3)]))
    check("S3 every t=6 non-unique product is collinear",
          bool(results[(2, 3)])
          and all(d == 1 for _, _, _, d, _ in results[(2, 3)]))
    return maxneg


def grade_pair(cores, gensof, A, B):
    """(factorization count, product Newton dim, max negative-factor dim)."""
    g = sorted(set(gensof[A]) | set(gensof[B]), key=lambda v: X.index(v))
    core = cores[A] + cores[B]
    n, _ = count_from_core(core, g)
    if n <= 1:
        return n, 0, 0
    d = newton_dim(block_product(core, range(len(core))), g)
    negs = [f for f in core if has_negative(f, g)]
    return n, d, max(newton_dim(f, g) for f in negs)


# ============================================ S3b  the two open rungs, by name
RUNG12 = ((2, 8, 32), (2, 4, 16, 32))
RUNG16 = ((2, 4, 16, 32), (2, 4, 16, 32))


def stage3b():
    print("\n=== S3b  the open rungs t=12 and t=16, as named constructions ===")
    cores, gensof, maxneg = {}, {}, 0
    for A in set(RUNG12) | set(RUNG16):
        P = menu_poly(A)
        gensof[A] = used_vars(P)
        _, cores[A] = zfactors(P)
        print(f"  {set(A)} core factors: "
              + " * ".join(str(f) for f in cores[A]))
    for label, (A, B), want in (("t=12", RUNG12, 2), ("t=16", RUNG16, 1)):
        n, d, nd = grade_pair(cores, gensof, A, B)
        maxneg = max(maxneg, nd)
        print(f"  {label}: {set(A)} x {set(B)}  ->  {n} factorizations,"
              f" product dim {d}, negative-factor dim {nd}")
        check(f"S3b {label} factors in exactly {want} way(s)", n == want)
    return maxneg


# =============================================== S4  the corrected observable
def stage4(*maxima):
    print("\n=== S4  the corrected observable ===")
    m = max(maxima)
    print(f"  max Newton dimension of a NEGATIVE Z-irreducible factor"
          f" over every non-unique product found here: {m}")
    check("S4 no negative Z-irreducible factor has dimension >= 2", m == 1)


def main():
    t0 = time.time()
    stage1()
    m2 = stage2()
    m2b = stage2b()
    m3 = stage3()
    m3b = stage3b()
    stage4(m2, m2b, m3, m3b)
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks pass   [{time.time()-t0:.1f}s]")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
