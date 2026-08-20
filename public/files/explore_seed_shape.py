"""What IS a seed? The filter that bounds every menu sweep, characterized.

THE QUESTION. A MENU is a finite set of integers >= 2, read as a
0/1-coefficient polynomial in the primes (m = prod p_i^e_i becomes the
monomial x_1^e_1 ...). A menu is a SEED when its Z-irreducible core -- the
polynomial with its monomial content divided out -- carries a factor with a
negative coefficient. Seedhood is the filter that bounds every menu sweep
in this corpus: because the Z-factors of a product are the union of the
factors', and a factorization over N is a partition of the Z-irreducible
multiset into blocks with nonnegative products, a product with no negative
Z-irreducible factor anywhere factors UNIQUELY. So only pairs where one
side is a seed can collide, and the seed count -- not the menu count -- is
what prices every walk (explore_menu_reach.py S3, explore_descent_hunt.py
finding 2).

Nobody has ever asked what that set IS. Its counts are printed and its
members listed -- over {2..32} exactly one size-3 menu is a seed and it is
{2,8,32}; over {2..24} exactly 17 of 8855 size-4 menus are -- and that is
where the reading stopped. The set is small and structured and it is the
reason the sweeps are boxed at all: the box exists to bound the SEED side
and nothing else. This file asks whether a sentence states it.

WHOSE VOCABULARY. The suspicion is written in the MENU vocabulary, whose
dial is the element bound, and that is the wrong vocabulary for it: a menu
polynomial depends on its elements only through their exponent VECTORS, so
seedhood is invariant under any relabelling of primes and under the
translation that divides out the content. {2,8,32} is {2^1, 2^3, 2^5} --
one prime and an exponent pattern -- and the element bound that box carries
is a bound on the vectors' entries wearing element clothes. Every claim
below is therefore written about exponent vectors, and the element boxes
survive only as the sampling frame.

THE HAND-ATTACK, on paper before any engine code, and it settles more than
it was expected to.

THE TERM-COUNT LAW. Let P be a 0/1-coefficient polynomial and P = f*g with
f, g nonnegative integer polynomials. Then P(1) = f(1)g(1); P(1) is the
term count T of P since P is 0/1; f(1) >= #f with equality exactly when f
is 0/1, and likewise g; and the support of P is contained in the sumset of
the supports, so T <= #f * #g <= f(1)g(1) = T. Every inequality is an
equality: TERM COUNTS MULTIPLY and both factors are themselves 0/1. So a
nonnegative factorization of a menu polynomial's core induces a
factorization of its term count.

COROLLARY, THE PRIME-SIZE IDENTITY. At a menu size t that is PRIME, the
only factorizations of t are trivial, and the content is already divided
out, so no nontrivial nonnegative factorization of the core exists. Hence
  at prime menu size, SEED == the core is REDUCIBLE OVER Z.
Sizes 2 and 3 are prime. Size 4 is not, and there the non-seeds split: a
size-4 non-seed core is either Z-irreducible or a product of two 0/1
BINOMIALS, and nothing else is available.

THE SIZE-2 CRITERION, in closed form. A two-element menu's core is
x^alpha + x^beta with disjoint supports (the content is the componentwise
minimum). Let d be the gcd of all entries of alpha and beta together, and
write the core as U^d + V^d with U, V coprime monomials. A^d + B^d is
reducible over Z exactly when d has an odd prime factor (the odd part
supplies A^(d/p) + B^(d/p) as a factor; when d is a power of 2 the form is
irreducible). With the prime-size identity above this is a CRITERION:
  {m, n} is a seed  <=>  d has an odd prime factor,
where d is read off the reduced pair. In element terms: divide out
g = gcd(m, n), and d is the largest integer such that both m/g and n/g are
perfect d-th powers. It is decidable without factoring a polynomial at all.

DISTRUST THE MARGIN, not the kill. The kill here -- "the criterion
misclassifies some menu" -- is derived from the argument above and is what
the run can refute cheaply. The MARGIN is the expectation that sizes 3 and
4 will submit to the same treatment, and that expectation is a vibe carried
from the one size where the algebra closed. So the file predicts a
STRUCTURE at size 3 rather than a criterion, and predicts nothing at all at
size 4.

DESIGN, four stages.
 S0 THE POSITIVE CONTROL, run before any census number is read. This file
    builds its own instrument -- its own prime list, its own monomial map,
    its own core extraction -- rather than importing the reach file's,
    because the control is only worth running if the two are independent.
    It must reproduce explore_menu_reach.py's own published seed counts on
    that file's own boxes: 4 seeds among the 465 size-2 menus over {2..32},
    1 among the 4495 size-3 menus over the same box, and 17 among the 8855
    size-4 menus over {2..24}; and the size-3 seed must be {2,8,32}. If any
    of those misses, the instrument is broken and nothing below is read.
 S1 THE TERM-COUNT LAW, checked where it is used rather than assumed. Over
    every menu the census walks: a menu is a seed exactly when some
    Z-irreducible factor of its core is negative (the definition, restated
    as a check that the two readings never part); at sizes 2 and 3 a menu
    is a seed exactly when its core has more than one Z-irreducible factor
    (the prime-size identity); and at size 4 every reducible non-seed has
    exactly two Z-irreducible factors, each with exactly two terms (what
    the law leaves available at a composite size).
 S2 THE WIDENED CENSUS. Sizes 2 and 3 over {2..64}, size 4 over {2..32} --
    which is the widening this line of work priced as its fallback, and it
    captures {2,4,16,32}, the size-4 half of the corpus's one graded t = 12
    point, which every box here has so far excluded. Printed: the seed
    count at each size, the seeds themselves in full at sizes 2 and 3, and
    at size 4 the count with the seeds listed.
 S3 THE READING. The size-2 criterion evaluated on every size-2 menu in the
    widened box WITHOUT factoring anything, and compared against the
    factorization instrument menu by menu. Then the size-3 seeds read for
    the structure predicted below. Then the size-4 seeds sorted by how many
    primes they use and how many Z-irreducible factors they carry, which is
    the measurement this stage exists to take.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): 4, 1 and 17 seeds on the three published boxes, and the size-3
      seed is {2,8,32}.
  PR1 (S1): every check holds at every menu. The term-count law is proved
      above, so a failure here is a failure of the instrument or of the
      argument, and either one voids the rest.
  PR2 (S3): the size-2 criterion agrees with the factorization instrument
      at every one of the 1953 size-2 menus over {2..64}. No exceptions.
  PR3 (S2/S3): exactly 11 size-2 seeds over {2..64}, and they are {2,16},
      {3,24}, {4,32}, {5,40}, {6,48}, {7,56}, {8,64} (ratio 8), {2,54}
      (ratio 27), {2,64} (ratio 32), {8,27} and {16,54} (the coprime cube
      pairs). Derived by hand from the criterion before the run.
  PR4 (S3): every size-3 seed's core is divisible by 1 + w + w^2 for some
      monomial w -- the trinomial route running through a cyclotomic factor
      and nothing else reaching. Among the 2-power triples in {2..64}
      exactly three are seeds: {2,4,64}, {2,8,32} and {2,32,64}, the three
      whose reduced exponents are distinct modulo 3 and are not {0,1,2}.
  PR5: NOT PREDICTED -- the size-3 seed TOTAL over the widened box, and the
      whole of the size-4 population. Those are the measurement, and
      predicting them is what would make S3 unreadable.

KILLS (observables with live failure modes; what each MEANS is weighed
after the run and never before).
  K0: any S0 count or the S0 witness misses. The instrument is broken.
  K1: any S1 check fails. The term-count law or its use here is wrong, and
      with it the prime-size identity every claim below leans on.
  K2: the size-2 criterion misclassifies any menu in the widened box. The
      closed form is wrong as stated and size 2 is not characterized.
  K3: some size-3 seed's core carries no 1 + w + w^2 factor. Then the
      cyclotomic route is not the only one into size 3 and PR4's sentence
      does not state the set.

HONEST LIMITS carried into the reading, stated before the run. (i) The
size-2 criterion is PROVED above and CHECKED on a box; the check is a
control on the instrument and adds nothing to the proof's scope. (ii)
Nothing at sizes 3 and 4 is proved here -- the prime-size identity is
proved and reduces size 3 to a reducibility question, but which trinomials
are reducible is CLASSICAL and is neither settled nor read here, and PR4
is a structural observation on a box. (iii) The census is boxed at both
sizes and the size-4 box is widened, not removed. (iv) Every claim is
about menus, so a polynomial with a
coefficient above 1 anywhere is outside the frame, as it is everywhere in
this corpus.

FINDINGS (tiers per the standard naming scale; run record below).

0. FOUR ADDITIONS THE DESIGN DOES NOT NAME, all from the audit that
   followed run 1; the slate is left as frozen.
   (i) S3 CARRIES A SECOND CLOSED CRITERION, at size 3 (criterion_seed3),
   which the design does not promise: the design says size 3 is READ for a
   structure and predicts one, and what the reading found was a decision
   procedure. It is checked the same way the size-2 one is -- evaluated on
   every menu in the box without factoring anything, and compared menu by
   menu against the factorization instrument. Finding 3 is that check.
   (ii) S3's size-4 block reports two shape columns the design does not
   list -- collinearity of the exponent vectors, and whether a cyclotomic
   trinomial factor is present. Both were added because sizes 2 and 3 had
   just made them the discriminating questions, and both are reported as
   measurements with nothing predicted about them.
   (iii) S1'S FIRST CHECK COULD NOT FAIL. As first written it asked
   whether a menu is a seed exactly when some Z-irreducible factor of its
   core is negative -- which is the expression census() evaluates to BUILD
   the seed list, so the check recomputed its own input and would have
   passed on any instrument whatever. It is replaced by the invariance the
   design ASSERTS and never tested: seedhood is a condition on exponent
   vectors up to translation and relabelling, so multiplying a menu
   through by 3 and replacing every prime by the next one must both leave
   the verdict alone. Checked at every seed plus a strided sample of each
   box, and both hold everywhere -- which is a statement about the
   instrument, since a core extraction that forgot the content division
   would fail the first and a factorization sensitive to variable order
   would fail the second.
   (iv) THE FIRST WORDING OF THE COLLINEARITY CHECK READ THE WRONG
   OBJECT and failed on a true statement. It counted the variables of the
   MENU polynomial, where the claim is about the CORE: {3,12,48} uses two
   primes and its core 1 + x^2 + x^4 uses one, the prime 3 being the
   content. Collinearity of the reduced exponent vectors is the
   content-free way to say it and is what the check now tests.

1. AT PRIME MENU SIZE, SEEDHOOD IS EXACTLY REDUCIBILITY OVER Z (property,
   proved in the hand-attack above; every one of the 73,129 menus of the
   widened census carries a check the law licenses -- the identity itself
   at the 41,664 of sizes 2 and 3, the non-seed shape it forces at the
   31,465 of size 4). NO NOVELTY IS CLAIMED FOR THE LAW ITSELF: the
   classification of factorization in this semiring BY NUMBER OF TERMS is
   classical, this corpus already credits it, and a statement this
   elementary is far likelier a lemma of that body than a new one -- what
   is this file's is the USE, reading it as a criterion on a single menu.
   The term-count law is the whole of it: a
   nonnegative factorization of a 0/1 polynomial multiplies term counts
   and both factors are themselves 0/1, so at a prime term count no
   nonnegative factorization survives the content division, and the
   Z-factorization must carry a negative factor the moment it is
   nontrivial. This is what makes sizes 2 and 3 answerable at all -- the
   question stops being "which factorizations are nonnegative" and becomes
   "which menu polynomials factor", which is classical. At size 4 the law
   instead says what the non-seeds look like, and the run confirms it:
   every reducible non-seed in the size-4 box is a product of exactly two
   0/1 BINOMIALS, which is the only term-count factorization 4 admits.

2. SIZE 2 IS CHARACTERIZED IN CLOSED FORM (rule, proved above and verified
   against factorization at all 1953 menus of {2..64}, 0 disagreements).
   {m, n} is a seed exactly when d has an odd prime factor, where g =
   gcd(m, n) and d is the largest integer such that m/g and n/g are both
   perfect d-th powers. No polynomial is factored to decide it. The twelve
   seeds over {2..64} are {2,16}, {2,54}, {2,64}, {3,24}, {4,32}, {5,40},
   {6,48}, {7,56}, {8,27}, {8,64}, {16,54}, {27,64} -- eleven at d = 3 and
   one at d = 5, and the whole of the d = 5 population in this box is
   {2,64}. The element bound is doing nothing structural here: it caps the
   ratio, and every seed is a ratio-8, ratio-27, ratio-32 or
   coprime-cube-pair menu.

3. SIZE 3 IS CHARACTERIZED TOO, AND THE SET IS TINY (rule, verified
   exhaustively against factorization at all 39,711 menus of {2..64}, 0
   disagreements). A three-element menu is a seed exactly when its reduced
   exponent vectors are COLLINEAR -- so the core is 1 + x^a + x^b in a
   single monomial direction -- and {0, a, b} meets all three residues
   modulo 3, and {a, b} is not {1, 2}. The three clauses are three
   different facts, and only one of them is this file's. ATTRIBUTION: the
   univariate half -- that a 0/1 trinomial is reducible exactly when a
   cyclotomic factor divides it, so that Phi_3 divisibility is the only
   route in -- is the CLASSICAL classification of trinomial
   factorization, not a result of this file; what is checked here is that
   it holds at every menu in the box, and what is this file's is the
   reduction TO it: that affine rank 2 leaves nothing to check, so the
   criterion never has to leave one variable. THE WARRANT FOR THAT HALF
   IS SUPERSEDED by explore_seed_confine.py finding 5, the conclusion
   unchanged: this file said the rank-2 core is "a monomial image of
   1 + u + v" and irreducible, which ASSERTS the irreducibility rather
   than deriving it, a monomial substitution carrying no factorization
   back on its own. The derivation is the SIMPLEX LAW at n = 3 -- three
   points of affine rank 2 make the core a 0/1 trinomial with
   independent exponents, which is irreducible outright (the trinomial
   lemma of explore_seed_rank_law.py; the triangle's indecomposability,
   which this line first leaned on, is not enough by itself, a simplex
   being the sum of two of its own homothets). That reduction was
   the mechanism this file read off the census rather than a proof it
   supplied (honest limit (ii)), and it now has one;
   and the classical half is credited here without its source having
   been read. The
   residue condition itself is elementary -- divisibility by 1 + x + x^2
   is exactly {0, a, b} meeting all three residues -- and the last clause
   removes 1 + x + x^2 itself, which is divisible by itself and
   irreducible. Five menus in the whole box pass:
   {2,4,64}, {2,8,32}, {2,32,64}, {3,12,48} and {4,16,64}. Three distinct
   cores between them -- 1 + x^2 + x^4 carried by three of the five,
   1 + x + x^5 and 1 + x^4 + x^5 by one each, the last two being each
   other's reversal -- so the size-3 seed set over an element bound is
   three trinomials wearing menu clothes.

4. THE CRITERIA HELD AND THE HAND ENUMERATIONS DID NOT, both times
   (measurement, against the frozen predictions). PR3 named eleven size-2
   seeds and the box holds twelve: the hand walk of coprime d = 3 pairs
   stopped at {8,27} and never asked which other pairs of coprime cubes
   fit under 64, which {27,64} does. PR4's second half named three 2-power
   size-3 seeds and the box holds four: the hand walk enumerated reduced
   exponent CLASSES rather than menus, and {2,8,32} and {4,16,64} are two
   menus sharing the class {0,2,4}. Neither miss touched the criteria --
   PR2 and finding 3's check both read 0 disagreements over 41,664 menus.
   What failed both times was the step AFTER the criterion, counting its
   solutions inside a box by hand, and that is worth keeping because the
   criterion is the part that looked hard.

5. SIZE 4 IS A DIFFERENT ANIMAL, AND THE ONE EXCEPTION IS THE POINT THIS
   LINE OF WORK ALREADY CARES ABOUT (observation, 44 seeds among the 31,465
   size-4 menus of {2..32}). Neither size-3 mechanism survives: exactly 1
   of the 44 has collinear exponent vectors, and 0 of the 44 carry a
   1 + w + w^2 factor. So the one-variable shape that IS the seed set at
   size 3 is essentially absent at size 4, where 31 seeds use two primes
   and 12 use three, and 41 of 44 carry exactly two Z-irreducible factors.
   The single collinear one is {2,4,16,32} -- the size-4 half of the
   corpus's one graded t = 12 point, whose size-3 half {2,8,32} is
   likewise the unique size-3 seed of the reach file's box. That point is
   therefore not a specimen that happened to be reachable by hand: it is
   the only place in either box where a collinear seed meets a collinear
   seed, which is why it reads dimension 1 while all 71 IN-FRAME swept
   collisions read 2 -- the 336 the sweep prints include 265 outside the
   0/1 frame (explore_seed_confine.py finding 1).

6. THE WIDENING THIS LINE OF WORK PRICED AS ITS FALLBACK IS DONE, AND IT
   CAPTURES THE POINT THE SWEEP COULD NOT REACH (measurement). The size-4
   box here is {2..32} against the reach file's {2..24}, and {2,4,16,32}
   is inside it and is a seed. explore_descent_hunt.py finding 3 records
   that the swept box could not contain the point the sweep extends; the
   seed side of that box no longer has that hole. What this file does NOT
   do is walk the resulting pairs -- the seed census is one side of the
   walk and the partner menus are the other, and the (3,4) walk over these
   wider boxes is 5 x 31,465 + 44 x 39,711 LESS the 5 x 44 that both
   halves name -- 1,904,389 pairs against the 85,253 already swept, which
   is a sweep to be priced rather than a corollary of this census.

7. WHAT THE CHARACTERIZATION BUYS: THE SEED SIDE CAN BE GENERATED RATHER
   THAN FILTERED (property, from findings 2 and 3). Every sweep in this
   corpus builds its seed list by factoring every menu in a box and
   keeping the ones that come out negative, which is why the box exists on
   the seed side at all. At sizes 2 and 3 that is now unnecessary: both
   criteria decide seedhood from the exponent vectors by arithmetic, so
   the seeds can be ENUMERATED directly at any bound, or generated with no
   bound at all -- one parametric family per size, each read straight off
   its criterion. Size 2 is {c*u, c*v} with u, v coprime d-th powers and d
   carrying an odd prime factor. Size 3 is {c, c*Q^a, c*Q^b} with Q >= 2,
   c >= 2 and {0, a, b} meeting all three residues mod 3 without being
   {0, 1, 2} -- the collinearity clause IS that form, the primitive
   direction wearing integer clothes as Q, and the five seeds of the box
   are 2*{1,2,32}, 2*{1,4,16}, 2*{1,16,32}, 3*{1,4,16} and 4*{1,4,16}.
   The box survives on the
   PARTNER side, where nothing here touches it. That is the design
   variable this line of work named, moved: a (3,4) walk no longer needs a
   size-3 box, only a size-4 one.

RUN RECORD (this file, under memwatch.py at the 512MB default, 126.7 s
wall, peak working set 95.6 MB). Run 1: 15/16, and the one failure was the
frozen PR4 second half, which named three 2-power size-3 seeds where the
box holds four (finding 4). Runs 2 and 3 added the size-3 criterion and
the collinearity check; run 2 failed the latter on a true statement,
having counted the menu's variables rather than the core's (finding 0
(iii)). Run 3: 19/19, with the checks now locking the measured seed lists
at sizes 2 and 3 rather than the hand-derived ones. Run 4 added the size-4
shape columns, which is where finding 5 comes from: 19/19. Round 2 of the
audit found S1's first check recomputing its own input and replaced it
with the two invariance checks (finding 0 (iii)); run 5 passed both but
counted a sample that listed the seeds twice at stride 1, and run 6 is on
the deduplicated sample: 22/22, and every figure above is that run's.
"""

import os
import sys
import time
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import symbols, Poly

# ---------------------------------------------- the instrument, built here
# Independent of explore_menu_reach.py's, which is what makes S0 a control:
# its prime list stops at 37 and the widened box below reaches 64.
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
X = symbols(' '.join(f'y{i}' for i in range(len(PRIMES))))

CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))
    print(("PASS  " if ok else "FAIL  ") + name)


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
    return [v for v in X if expr.has(v)]


def core_of(expr):
    """The Z-irreducible factors left after the monomial content."""
    content, fl = sympy.factor_list(expr)
    assert content == 1, f"non-unit content {content}"
    core = []
    for f, mult in fl:
        for _ in range(mult):
            if f not in X:
                core.append(sympy.expand(f))
    return core


def negative(expr, gens):
    return any(c < 0 for c in Poly(expr, *gens).coeffs())


def nterms(expr, gens):
    return len(Poly(expr, *gens).monoms())


# ------------------------------------------------ the size-2 criterion, closed
def exponents(m):
    """The prime exponent vector of m, as a dict."""
    e, rest = {}, m
    for p in PRIMES:
        while rest % p == 0:
            rest //= p
            e[p] = e.get(p, 0) + 1
    assert rest == 1
    return e


def power_index(m):
    """The largest d with m a perfect d-th power (0 for m == 1)."""
    e = exponents(m)
    if not e:
        return 0
    d = 0
    for v in e.values():
        d = sympy.gcd(d, v)
    return int(d)


def odd_part(n):
    while n and n % 2 == 0:
        n //= 2
    return n


def vectors(A):
    """The menu's exponent vectors with the content divided out."""
    es = [exponents(m) for m in A]
    ps = sorted({p for e in es for p in e})
    rows = [[e.get(p, 0) for p in ps] for e in es]
    low = [min(r[i] for r in rows) for i in range(len(ps))]
    return [[c - b for c, b in zip(r, low)] for r in rows]


def affine_rank(pts):
    """Dimension of the affine span of a set of exponent vectors."""
    base = pts[0]
    rows = [[a - b for a, b in zip(p, base)] for p in pts[1:]]
    return sympy.Matrix(rows).rank() if rows else 0


def collinear(pts):
    """Do three exponent vectors have affine rank 1?"""
    p0, p1, p2 = pts
    d1 = [b - a for a, b in zip(p0, p1)]
    d2 = [b - a for a, b in zip(p0, p2)]
    n = len(d1)
    return not any(d1[i] * d2[j] != d1[j] * d2[i]
                   for i in range(n) for j in range(i + 1, n))


def criterion_seed3(A):
    """Is a three-element menu a seed? Decided without factoring.

    Added by the audit that followed run 1 and not named in the frozen
    design; the reading it locks is finding 3. The reduced vectors are
    {0, a*v, b*v} or they are not collinear at all; a non-collinear 0/1
    trinomial is a monomial image of 1 + u + v and irreducible, so only
    the collinear ones can be seeds, and there the core is 1 + x^a + x^b,
    divisible by 1 + x + x^2 exactly when {0, a, b} meets all three
    residues mod 3, and reducible exactly when that quotient is not
    trivial -- which excludes {a, b} = {1, 2}, the polynomial 1 + x + x^2
    itself.
    """
    pts = vectors(A)
    if not collinear(pts):
        return False                      # affine rank 2: irreducible
    p0, p1, p2 = pts
    d1 = [b - a for a, b in zip(p0, p1)]
    d2 = [b - a for a, b in zip(p0, p2)]
    n = len(d1)
    g1 = 0
    for c in d1:
        g1 = sympy.igcd(g1, c)
    w = [c // g1 for c in d1]
    i = next(i for i in range(n) if w[i])
    ts = [0, int(g1), int(d2[i] // w[i])]
    lo = min(ts)
    a, b = sorted(t - lo for t in ts)[1:]
    if len({0, a % 3, b % 3}) != 3:
        return False
    return {a, b} != {1, 2}


def criterion_seed2(m, n):
    """Is {m, n} a seed? Decided without factoring any polynomial.

    d is the gcd of the exponents of the reduced pair; the menu is a seed
    exactly when d has an odd prime factor (the hand-attack above).
    """
    g = sympy.igcd(m, n)
    d = sympy.gcd(power_index(m // g), power_index(n // g))
    return odd_part(int(d)) > 1


# ------------------------------------------------------------ census machinery
def census(box, size):
    """(menus, seeds, cores, gens) over every size-`size` menu in `box`."""
    menus = [tuple(c) for c in combinations(box, size)]
    seeds, cores, gensof = [], {}, {}
    for A in menus:
        P = menu_poly(A)
        g = used_vars(P)
        core = core_of(P)
        cores[A], gensof[A] = core, g
        if any(negative(f, g) for f in core):
            seeds.append(A)
    return menus, seeds, cores, gensof


def is_seed(A):
    P = menu_poly(A)
    g = used_vars(P)
    return any(negative(f, g) for f in core_of(P))


def scaled(A, c):
    """The menu with every element multiplied by c: a pure TRANSLATION of
    the exponent vectors, which the content division must undo."""
    return tuple(sorted(c * m for m in A))


def shift_primes(A):
    """The menu with every prime replaced by the next one: a RELABELLING
    of the variables, which no factorization can see. None if the menu
    already reaches the top of the prime list."""
    out = []
    for m in A:
        v = 1
        for p, k in exponents(m).items():
            i = PRIMES.index(p)
            if i + 1 >= len(PRIMES):
                return None
            v *= PRIMES[i + 1] ** k
        out.append(v)
    return tuple(sorted(out))


def show(label, seeds, cap=40):
    shown = ", ".join("{" + ",".join(str(m) for m in A) + "}"
                      for A in seeds[:cap])
    print(f"    {label}: " + (shown + (" ..." if len(seeds) > cap else "")
                              if seeds else "(none)"))


REACH_SMALL = list(range(2, 33))   # the reach file's sizes 2,3 box
REACH_BIG = list(range(2, 25))     # the reach file's size-4 box
WIDE_SMALL = list(range(2, 65))    # this file's sizes 2,3 box
WIDE_BIG = list(range(2, 33))      # this file's size-4 box


# ==================================================== S0  the positive control
def stage0():
    print("\n=== S0  the positive control: the reach file's published counts"
          " on its own boxes ===")
    t0 = time.time()
    published = {(2, 'small'): 4, (3, 'small'): 1, (4, 'big'): 17}
    sizes = {(2, 'small'): (REACH_SMALL, 465),
             (3, 'small'): (REACH_SMALL, 4495),
             (4, 'big'): (REACH_BIG, 8855)}
    seed3 = None
    for key, want in published.items():
        size = key[0]
        box, nmenus = sizes[key]
        menus, seeds, _, _ = census(box, size)
        print(f"  size {size}: {len(menus):6d} menus, {len(seeds):4d} seeds"
              f"   [{time.time() - t0:.1f}s]")
        show(f"size-{size} seeds", seeds, cap=20)
        check(f"S0 the box holds {nmenus} size-{size} menus",
              len(menus) == nmenus)
        check(f"S0 size-{size} reproduces the published {want} seeds",
              len(seeds) == want)
        if size == 3:
            seed3 = seeds
    check("S0 the unique size-3 seed is {2,8,32}", seed3 == [(2, 8, 32)])


# ================================================= S1  the term-count law used
def stage1(size, menus, seeds, cores, gensof):
    """Every check the term-count law licenses at this size."""
    seedset = set(seeds)
    bad_prime, bad_four = [], []
    for A in menus:
        core, g = cores[A], gensof[A]
        seed = A in seedset
        if size in (2, 3):
            if seed != (len(core) > 1):
                bad_prime.append(A)
        elif size == 4 and not seed and len(core) > 1:
            if len(core) != 2 or any(nterms(f, g) != 2 for f in core):
                bad_four.append(A)

    # The invariance the WHOSE VOCABULARY paragraph asserts, checked rather
    # than asserted: seedhood reads the exponent vectors up to translation
    # and relabelling, so scaling a menu and shifting its primes must both
    # leave the verdict alone. Every seed plus a strided sample of the box.
    stride = 1 if size == 2 else 25
    sample = sorted(set(seeds) | set(menus[::stride]))
    bad_scale = [A for A in sample if is_seed(scaled(A, 3)) != (A in seedset)]
    bad_relab = [A for A in sample
                 if shift_primes(A) is not None
                 and is_seed(shift_primes(A)) != (A in seedset)]
    check(f"S1 size-{size}: seedhood survives scaling, over {len(sample)}"
          " menus", not bad_scale)
    check(f"S1 size-{size}: seedhood survives prime relabelling, over"
          f" {len(sample)} menus", not bad_relab)
    if size in (2, 3):
        check(f"S1 size-{size}: seed == Z-reducible (the prime-size identity)",
              not bad_prime)
    else:
        check(f"S1 size-{size}: every reducible non-seed is two 0/1 binomials",
              not bad_four)


# ===================================================== S2  the widened census
def stage2():
    print("\n=== S2  the widened census: sizes 2,3 over {2..64},"
          " size 4 over {2..32} ===")
    t0 = time.time()
    out = {}
    for size, box in ((2, WIDE_SMALL), (3, WIDE_SMALL), (4, WIDE_BIG)):
        menus, seeds, cores, gensof = census(box, size)
        print(f"  size {size}: {len(menus):6d} menus, {len(seeds):4d} seeds"
              f"   [{time.time() - t0:.1f}s]")
        show(f"size-{size} seeds", seeds)
        stage1(size, menus, seeds, cores, gensof)
        out[size] = (menus, seeds, cores, gensof)
    return out


# ========================================================= S3  the reading
def phi3_divisor(core, gens, A):
    """A monomial w with 1 + w + w^2 dividing the core, or None."""
    P = sympy.expand(sympy.prod(core)) if core else sympy.Integer(1)
    top = {}
    for mon in Poly(P, *gens).monoms():
        for v, e in zip(gens, mon):
            top[v] = max(top.get(v, 0), e)
    cands = [sympy.Integer(1)]
    for v, e in top.items():
        cands = [c * v**i for c in cands for i in range(e + 1)]
    for w in cands:
        if w == 1:
            continue
        q, r = sympy.div(P, sympy.expand(1 + w + w**2), *gens)
        if r == 0:
            return w
    return None


def stage3(out):
    print("\n=== S3  the reading ===")

    # --- size 2: the closed criterion against the factorization instrument
    menus2, seeds2, _, _ = out[2]
    seedset = set(seeds2)
    wrong = [A for A in menus2 if criterion_seed2(*A) != (A in seedset)]
    print(f"  size 2: criterion evaluated on {len(menus2)} menus,"
          f" {len(wrong)} disagreements with the factorization instrument")
    check("S3 the size-2 criterion agrees with factorization at every menu",
          not wrong)
    check("S3 the size-2 seeds are the measured twelve",
          sorted(seeds2) == [(2, 16), (2, 54), (2, 64), (3, 24), (4, 32),
                             (5, 40), (6, 48), (7, 56), (8, 27), (8, 64),
                             (16, 54), (27, 64)])
    print(f"  size-2 seeds ({len(seeds2)}), with the reduced power index d:")
    for A in seeds2:
        m, n = A
        g = sympy.igcd(m, n)
        d = sympy.gcd(power_index(m // g), power_index(n // g))
        print(f"    {{{m},{n}}}  gcd {g}  reduced {m//g}/{n//g}  d = {d}")

    # --- size 3: the structure
    menus3, seeds3, cores3, gens3 = out[3]
    print(f"  size-3 seeds ({len(seeds3)}), with the cyclotomic witness:")
    nophi = []
    for A in seeds3:
        w = phi3_divisor(cores3[A], gens3[A], A)
        nfac = len(cores3[A])
        print(f"    {set(A)}  primes {len(gens3[A])}  Z-factors {nfac}"
              f"  1+w+w^2 witness: {w}")
        if w is None:
            nophi.append(A)
    check("S3 every size-3 seed core is divisible by 1 + w + w^2", not nophi)
    check("S3 every size-3 seed's exponent vectors are COLLINEAR",
          all(collinear(vectors(A)) for A in seeds3))
    wrong3 = [A for A in menus3 if criterion_seed3(A) != (A in set(seeds3))]
    print(f"  size 3: criterion evaluated on {len(menus3)} menus,"
          f" {len(wrong3)} disagreements with the factorization instrument")
    check("S3 the size-3 criterion agrees with factorization at every menu",
          not wrong3)
    check("S3 the size-3 seeds are the measured five",
          sorted(seeds3) == [(2, 4, 64), (2, 8, 32), (2, 32, 64),
                             (3, 12, 48), (4, 16, 64)])

    # --- size 4: the measurement, unpredicted
    menus4, seeds4, cores4, gens4 = out[4]
    byprimes, byfactors = {}, {}
    for A in seeds4:
        byprimes[len(gens4[A])] = byprimes.get(len(gens4[A]), 0) + 1
        byfactors[len(cores4[A])] = byfactors.get(len(cores4[A]), 0) + 1
    print(f"  size-4 seeds ({len(seeds4)} of {len(menus4)} menus)")
    show("the full list", seeds4, cap=len(seeds4))
    print(f"    by prime count:  {dict(sorted(byprimes.items()))}")
    print(f"    by Z-factor count: {dict(sorted(byfactors.items()))}")
    flat = [A for A in seeds4 if affine_rank(vectors(A)) == 1]
    phi = [A for A in seeds4
           if phi3_divisor(cores4[A], gens4[A], A) is not None]
    print(f"    with COLLINEAR exponent vectors: {len(flat)} of {len(seeds4)}"
          f"   {[set(A) for A in flat]}")
    print(f"    with a 1 + w + w^2 factor: {len(phi)} of {len(seeds4)}")
    graded = (2, 4, 16, 32)
    print(f"    the graded point's size-4 half {set(graded)} is in the box:"
          f" {graded in set(menus4)}; a seed: {graded in set(seeds4)}")


def main():
    t0 = time.time()
    stage0()
    out = stage2()
    stage3(out)
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time() - t0:.1f}s")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
