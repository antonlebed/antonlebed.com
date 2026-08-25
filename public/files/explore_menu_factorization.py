"""Menu factorization: is permanent indistinguishability just factoring?

THE QUESTION. Two routes of a dated fiber -- common seed, common
length, common endpoint -- are indistinguishable at EVERY temperature
precisely when their interior menus have equal products. A MENU is a
finite set of integers >= 2; it becomes the Dirichlet polynomial
Z_A(beta) = sum over m in A of m^-beta, and substituting x_i =
p_i^-beta makes it a polynomial in N[x_1..x_r] whose coefficients are
all 0 or 1 -- the menu being a SET is exactly that restriction. Menus
are NOT closed under multiplication ({2,3}*{2,3} = x^2 + 2xy + y^2),
so the ambient semiring is N[x_1..x_r] plain and 0/1-support is a
condition on the FACTORS one is allowed to look for, never on the
products. So every all-temperature amnesia question is an
EQUAL-PRODUCTS question there -- which becomes a FACTORIZATION
question only where factorization is non-unique. Conflating the two is
the error this file was written out of: an earlier collision census
(explore_rogue_world.py) sorted 4849 colliding pairs into a scaling
family, a one-prime family, and "474 involving >= 2 primes" called
TRANSFER, which is not a mechanism but the complement of the other two
wearing a name.

WHAT IS ASKED HERE, in two parts. (1) Retire the residual bucket: for
every colliding product at the earlier census's own scope, print how
many distinct N-irreducible factorizations it has and how many
variables it uses. (2) Ask how far non-uniqueness reaches past ONE
variable -- every non-uniqueness the corpus has ever witnessed is the
one-variable cyclotomic one.

HAND-DERIVED BEFORE ANY ENGINE CODE (property; four steps, each a line).
 (a) Z[x_1..x_r] is a UFD and a menu polynomial is primitive (its
     coefficients are 0/1), so by Gauss a product of two menu
     polynomials is primitive and every factor of it with integer
     coefficients is, up to sign, a product of a sub-multiset of its
     Z-irreducible factors. Normalizing each Z-irreducible to positive
     leading coefficient in a fixed monomial order removes the sign
     choice: a sub-product then has positive leading coefficient, so it
     is never the negative of a nonnegative polynomial.
 (b) Hence the N-factorizations of P are exactly the partitions of P's
     Z-irreducible multiset into blocks whose products are all
     nonnegative, and the N-IRREDUCIBLE ones are exactly those whose
     every block admits no bipartition into two nonnegative
     sub-products.
 (c) Monomials split off alone: x^a is reducible for a >= 2, and a
     block holding a variable together with anything else is reducible
     by that variable. So the count is carried by the CORE, the
     polynomial left after dividing out the monomial gcd.
 (d) THE CRITERION, and it is what reframes the whole question: if
     every Z-irreducible factor of P is nonnegative, then all-singletons
     is the only N-irreducible factorization and P factors UNIQUELY. So
     non-uniqueness REQUIRES a Z-irreducible factor carrying a negative
     coefficient. The Z-irreducible factors of Z_A * Z_B are those of
     Z_A together with those of Z_B -- so carrying a negative factor is
     a property of a SINGLE MENU, never of the pairing. Call such a menu
     a SEED. A census of collisions cannot see this; an enumeration of
     menus can, and that is why part (2) below enumerates menus and not
     pairs.

 The trivial half of the regrouping frame follows from (d) and is why
 that frame is worth nothing by itself: where the product factors
 uniquely, factors(A) + factors(B) IS that factorization and so is
 factors(C) + factors(D), so both pairs partition one multiset and the
 collision is a REGROUPING. The complement can exist only where the
 product's own N-factorization is non-unique.

 THE HAND SPECIMEN, derived at the freeze from step (d). The known
 one-variable non-uniqueness is the cyclotomic regrouping
 (1+x)(1+x+x^2)(1-x+x^2), whose factor 1-x+x^2 is negative and mates
 with either of the other two. Substituting a MONOMIAL for x keeps the
 mechanism one-variable in disguise. HOMOGENIZING it does not: with
 x^2 - xy + y^2 as the negative factor, (x+y)(x^2-xy+y^2) = x^3 + y^3
 and (x^2+xy+y^2)(x^2-xy+y^2) = x^4 + x^2y^2 + y^4 are both
 nonnegative, so the product of all three carries two N-irreducible
 factorizations in TWO variables. Read back as menus with x = 2, y = 3:
 {8,27} x {4,6,9} against {2,3} x {16,36,81}, both spanning the product
 set {32,48,72,108,162,243}.

 THE LADDER THIS SETS UP, and the observable that reads it: a negative
 Z-irreducible factor can use ONE variable (monomial substitution -- the
 only kind the corpus has seen), or >= 2 variables with a Newton polygon
 of dimension 1 (homogenization -- the specimen above), or a Newton
 polygon of dimension >= 2, which would be a mechanism no image of a
 one-variable polynomial supplies. The engine prints the variable count
 and the Newton dimension of every negative factor it finds.

DESIGN, five stages.
 S1 CONTROL, the counter read in both directions. The core
    (1+x+x^2)(1+x^3) must print exactly 2 N-irreducible factorizations
    and the transfer specimen x*y*(1+x) must print exactly 1. A counter
    that cannot print 2, or cannot print 1, decides nothing.
 S2 CONTROL, census reproduction. The earlier record's scope rebuilt
    exactly: menus = subsets of {2..16} u {32} of size 1..3, all
    unordered pairs, exact integer polynomial arithmetic, grouped by
    product polynomial; a collision class is a product carrying >= 2
    menu pairs. Its printed totals must match the frozen record, or the
    scope is a different one and no verdict transfers to it.
 S3 THE SWEEP. For every colliding product at that scope, the number of
    distinct N-irreducible factorizations and the number of variables
    used. No regrouping verdict is printed: step (d) makes it a function
    of the first number, and a rig that recomputes a derivation reports
    its own agreement with itself.
 S4 THE MECHANISM MAP. Every menu of size 1..3 with elements in
    {2..81} is factored over Z and kept if it carries a negative
    Z-irreducible factor. Printed: how many such seeds, the distinct
    negative factors, and for each its variable count and Newton
    dimension.
 S5 THE SPECIMEN. The hand-derived pair of pairs checked for equal
    products, and its common product's N-irreducible factorizations
    enumerated and printed in full.

PREDICTIONS (fixed before the engine, and before any run).
  PR1 (S1): 2 for the cyclotomic core, 1 for the transfer specimen.
  PR2 (S2): 696 menus, 242,556 pairs, 4849 colliding pair-of-pairs,
      4487 collision classes; scaling 4369 of which 111 one-prime;
      non-scaling 480 = 6 one-prime + 474 multi-prime.
  PR3 (S3, the positive control on the verdict path): the contract
      collision's product Z_{2,4,8} * Z_{2,16} appears among the
      colliding products and prints NON-unique. That collision is the
      rogue world's whole mechanism; a run printing it unique has a
      broken factorizer and no verdict at all.
  PR4 (S3, the decision observable): ZERO colliding products at census
      scope have >= 2 N-irreducible factorizations AND use more than one
      variable. By step (d) with PR5 below.
  PR5 (S4 restricted to census scope, the REASON for PR4): every seed
      whose elements lie in {2..16} u {32} carries a negative factor in
      ONE variable. Derivation: a negative factor needs a Z-reducible
      core, the cheapest being 1 + t^n with n carrying an odd factor
      > 1, hence n >= 3; a multi-variable monomial ratio t has t >= 6,
      so the top element would be >= 216 > 32. {2,16}, {4,32} and
      {2,8,32} are predicted among the seeds.
  PR6 (S5): the two pairs have equal product multisets and their common
      product has exactly 2 N-irreducible factorizations using 2
      variables -- (x^3+y^3)(x^2+xy+y^2) and (x+y)(x^4+x^2y^2+y^4).
  PR7 (S4, how far the mechanism reaches): over elements {2..81} every
      negative factor found has a Newton polygon of dimension <= 1, and
      at least one uses >= 2 variables. Every non-uniqueness reachable
      there is then a substitution or homogenization image of the
      one-variable mechanism.

KILLS (observables with live failure modes; the meaning is weighed
after the run, never before).
  K1: either S1 number is wrong -- the counter is broken and nothing
      downstream is read.
  K2: any PR2 number differs -- this is a different census from the
      frozen record and the guard it was written to discharge is not
      discharged by it.
  K3: the contract product is absent, or prints unique -- broken
      factorizer, no verdict.
  K4: PR6 fails -- the homogenization route is wrong, the multivariate
      specimen dies, and the corpus's one-variable reading stands.
  K5: S4 prints a negative factor of Newton dimension >= 2 -- a
      mechanism beyond any image of a one-variable polynomial. This
      kills PR7 and is the outcome worth hunting.

HONEST LIMITS carried into the reading. (i) S3 is exhaustive only at
the earlier record's scope, which S2 exists to pin. (ii) S4 sweeps
menus of size <= 3 with elements <= 81; a dimension-2 negative factor
outside that box is unmeasured, so PR7 surviving is a statement about
the box and not about the semiring. (iii) The N-irreducible count rests
on the UFD argument in step (a), so it is exact rather than sampled --
but it inherits sympy's integer factorization as its one external
dependency, which S1 exists to keep honest.

FINDINGS (tiers per the standard naming scale; run record below).

1. NON-UNIQUENESS IS A PROPERTY OF A SINGLE MENU (property, derived by
   hand before the engine, step (d) above; the engine only exercises
   it). If every Z-irreducible factor of a product is nonnegative the
   N-irreducible factorization is unique, so non-uniqueness requires a
   negative-coefficient Z-irreducible; and the Z-factors of Z_A * Z_B
   are those of Z_A together with those of Z_B. So the property belongs
   to one MENU -- a SEED -- and never to the pairing. This is why a
   census of colliding PAIRS is the wrong instrument for the question
   it was read as answering: pairs are quadratically many and carry the
   property linearly.

2. THE RESIDUAL BUCKET IS RETIRED AND THE EXHAUSTION HOLDS AT SCOPE
   WITH TWO MECHANISMS (observation, exhaustive at the earlier census's
   scope). Of 4849 colliding pair-of-pairs, 4839 sit in a product that
   factors UNIQUELY over N and are therefore REGROUPINGS by the trivial
   half of the frame -- both pairs partition one factor multiset. The
   other 10 sit in the only 6 products (of 4487) that factor
   non-uniquely, every one of them with exactly 2 factorizations. The
   "474 involving >= 2 primes" bucket splits 472 regroupings + 2, and
   the 2 are not a third mechanism (finding 3). The whole non-unique
   part of the census scope is generated by exactly THREE seed menus:
   {2,16}, {4,32}, {2,8,32}, and no others exist inside {2..16} u {32}.
   The old three-way sort -- scaling, one-prime, transfer -- is replaced
   by a two-way one that is a theorem on one side: REGROUPING, or
   NON-UNIQUE PRODUCT.

3. THE DECIDING OBSERVABLE WAS COUNTING A SPECTATOR (observation, and
   it is a correction to the question rather than an answer to it). Two
   census-scope products factor non-uniquely AND use more than one
   variable -- {2,16} x {3,6,12} and {4,32} x {3,6,12} -- so the
   question "does any non-uniquely factoring product use more than one
   variable" fires YES at scope. It fires for nothing: both are
   x*y*(1+x)(1-x+x^2)(1+x+x^2), where the second variable enters as a
   MONOMIAL factor standing beside a mechanism that is entirely
   one-variable. A product's variable count cannot grade a mechanism,
   because a monomial factor raises it for free. The observable that
   does is the variable count and the Newton dimension of the NEGATIVE
   FACTOR, which finding 1 locates and which S4 prints.

4. THE MULTIVARIATE SPECIMEN, AND IT IS HOMOGENIZATION RATHER THAN
   SUBSTITUTION (construction, hand-derived at the freeze and
   engine-verified). {8,27} x {4,6,9} and {2,3} x {16,36,81} both span
   the product set {32,48,72,108,162,243}; the common polynomial
   x^5 + x^4y + x^3y^2 + x^2y^3 + xy^4 + y^5 carries exactly two
   N-irreducible factorizations, (x+y)(x^4+x^2y^2+y^4) and
   (x^3+y^3)(x^2+xy+y^2), whose shared negative factor x^2 - xy + y^2
   genuinely uses TWO variables. Substituting a monomial into the
   one-variable identity keeps the mechanism one-variable; HOMOGENIZING
   it does not, and that is the operation the corpus had not used. The
   two pairs ARE the two factorizations rather than two partitions of
   one factor multiset, so this collision is not a regrouping. It is a
   collision and nothing further: whether these menus assemble into an
   actual dated fiber is REALIZATION, a separate question that
   explore_rogue_world.py settles only inside its own scope (elements
   <= 32, seeds t <= 8), which this specimen sits outside. Until that
   is run it is a fact about polynomials and not yet an amnesia
   witness.

5. EVERY REACHABLE MECHANISM IS STILL AN IMAGE OF THE ONE-VARIABLE ONE
   (observation, exhaustive over menus of size <= 3 with elements <=
   81). 23 seeds, carrying 7 distinct negative Z-irreducible factors.
   Two of the seven use two variables -- x^2 - xy + y^2 (from {8,27},
   {16,54}, {24,81}) and x^4 - x^2y + y^2 (from {27,64}) -- so finding
   4's specimen is not isolated. But ALL SEVEN have a Newton polygon of
   dimension 1: their exponent vectors are collinear, which is exactly
   the signature of a monomial substitution or a weighted
   homogenization applied to a one-variable polynomial. So the ladder
   has three rungs and the box reaches two of them: one variable
   (substitution), several variables with a segment Newton polygon
   (homogenization), and a Newton polygon of dimension >= 2, which is
   ABSENT here. A dimension-2 negative factor would be a mechanism no
   image of a one-variable polynomial supplies, and hunting one is the
   frontier this leaves.

THE HEADLINE. Permanent indistinguishability of pasts is NOT
factorization: at census scope 4839 of 4849 collisions are regroupings,
compatible with unique factorization exactly as 2*6 = 3*4 is in Z. It
becomes factorization only at the seeds, and a seed is a single menu
whose polynomial carries a negative irreducible factor -- three of them
at census scope, 23 up to element 81. The mechanism reaches past one
variable, by homogenization rather than by substitution, and it has not
yet been seen to reach past a one-dimensional Newton polygon at all.

LATER CONTACT, and it moves two of the statements above. The incumbent
read this file called for is PAID (explore_menu_reach.py): factorization
in this semiring is classified in the literature by NUMBER OF TERMS,
which read through menu sizes settles size pairs (2,2), (2,4) and (3,3)
as unique at any element bound and forces (2,3) collinear. Finding 5's
frontier is therefore reached, at menu size pair (2,5). Limit (d) below
named size and element bound as the two dials and declined to say which
hid it; the answer is SIZE, and the element bound was barely binding.
Note WHAT is two-dimensional there: the PRODUCT's Newton polygon, while
the negative factor's stays one-dimensional -- so finding 5's literal
claim about the seven negative factors is untouched, and it is the
one-variable READING built on it, here and in the headline below, that
is false rather than merely unwitnessed. The observable this file minted
would not have fired at the escape. The record here stands as what THIS run measured; the
current statement is the one explore_menu_reach.py carries.

NO NOVELTY IS CLAIMED HERE. Factorization in the semiring N_0[x] is a
studied subject and this file has not read it. What is stated above is
stated as a measurement of THIS corpus's objects; whether the several-
variable case or the 0/1 constraint on the factors sought is anyone's
new ground is unpaid, and that reading is the gate before any of this
reaches a public surface.

HONEST LIMITS. (a) S3 is exhaustive only at the earlier record's scope,
which S2 pins by reproducing all nine of its published counts. (b) S4
sweeps menus of size <= 3 with elements <= 81; finding 5's absence is a
statement about that box, not about the semiring, and the box was set
by runtime and not by any argument that it is the right one. (c) The
counts rest on the UFD argument of step (a) and on sympy's multivariate
integer factorization, whose only guard here is S1. (d) Menus of size
> 3 are untouched, and so are elements > 81; those are the two dials,
and nothing here argues which one hides a dimension-2 factor. What can
be said is that finding 5's absence is NOT for want of two-dimensional
menus: 82,044 of the 82,160 size-3 menus swept have a two-dimensional
Newton polygon themselves, and none of them yielded a two-dimensional
negative FACTOR. The polytope of a product is the Minkowski sum of the
factors' (Ostrowski), so a two-dimensional factor forces a
two-dimensional menu polygon but not conversely, which is why the two
counts come apart this far.

RUN RECORD (this file, under memwatch.py at the 512MB default,
~143 s wall, peak working set 249 MB). Run 1: 20/20, all five stages
green -- but PR4 was REFUTED, two multivariate non-unique products
appearing at census scope; reading them produced finding 3 (the
spectator monomial), which PR4's observable could not
distinguish from a real multivariate mechanism. PR1, PR2, PR3, PR5,
PR6, PR7 all held as written. Run 2 (this record): added the S3
classification print -- where the earlier census's three-way sort lands
once products are graded by factorization -- giving finding 2's
472 + 2 split and the 10 collisions inside non-unique products;
20/20 unchanged. Run 3 (the audit round): added S4's count of size-3
menus whose OWN Newton polygon is two-dimensional -- 82,044 of 82,160 --
after the audit found the honest limit citing a FALSE reason for
expecting a dimension-2 factor at size 4 (a three-term polynomial can
carry a triangle; 1 + x + y does). The measured count replaces that
reason and strengthens the absence it was written to weaken. 20/20;
wall 128 s -> 143 s, the added Newton-dimension test on every size-3
menu.
Post-run edits: this findings block, the S3 classification print and
the S4 dimension count; the slate, the predictions, the kills and the
rest of the engine untouched.
"""

import os
import sys
import time
from itertools import combinations, combinations_with_replacement

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import Poly, symbols

CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))
    print(("PASS  " if ok else "FAIL  ") + name)


# ------------------------------------------------------------ menu -> polynomial
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79]
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


# ------------------------------------------------- N-irreducible factorizations
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


def n_factorizations(expr, want_list=False):
    """Distinct N-irreducible factorizations of a nonnegative polynomial.

    Returns (count, monomial_factors, core_factor_count, n_variables) and,
    when want_list, the factorizations themselves as sorted tuples.
    """
    gens = used_vars(expr) or [X[0]]
    mons, core = zfactors(expr)
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
            key = tuple(sorted(sympy.srepr(b) for b in blocks))
            found[key] = blocks
    out = (len(found), mons, len(core), len(gens))
    return (out, list(found.values())) if want_list else out


def newton_dim(expr, gens):
    """Affine dimension of the exponent-vector set."""
    pts = [list(mon) for mon in Poly(expr, *gens).monoms()]
    if len(pts) < 2:
        return 0
    base = pts[0]
    rows = [[a - b for a, b in zip(p, base)] for p in pts[1:]]
    return sympy.Matrix(rows).rank()


# ------------------------------------------------------------ the menu census
def zdict(menu):
    return {m: 1 for m in menu}


def dmul(P, Q):
    R = {}
    for a, ca in P.items():
        for b, cb in Q.items():
            R[a * b] = R.get(a * b, 0) + ca * cb
    return R


def dkey(P):
    return tuple(sorted(P.items()))


def prime_set(n):
    fs, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    return fs


def scale_of(A, C):
    if len(A) != len(C) or C[0] % A[0]:
        return None
    c = C[0] // A[0]
    if c < 2:
        return None
    return c if all(c * a == cc for a, cc in zip(A, C)) else None


def is_scaling(pp1, pp2):
    (A, B), (C, D) = pp1, pp2
    for X1, Y1 in ((A, B), (B, A)):
        for X2, Y2 in ((C, D), (D, C)):
            c = scale_of(X1, X2)
            if c is not None and scale_of(Y2, Y1) == c:
                return True
    return False


def one_prime(pp1, pp2):
    ps = set()
    for menu in pp1 + pp2:
        for m in menu:
            ps |= prime_set(m)
    return len(ps) == 1


T0 = time.perf_counter()

# ============================================================ S1 the control
print("== S1 control: the counter read in both directions ==")
x, y = X[0], X[1]
CYCLO = sympy.expand((1 + x + x ** 2) * (1 + x ** 3))
TRANSFER = sympy.expand(x * y * (1 + x))
(nc, _, _, vc), cyc_list = n_factorizations(CYCLO, want_list=True)
(nt, mt, _, vt) = n_factorizations(TRANSFER)
print(f"  (1+x+x^2)(1+x^3) = {CYCLO}")
for f in cyc_list:
    print(f"     factorization: {[str(b) for b in f]}")
print(f"  x*y*(1+x): monomial factors {[str(m) for m in mt]}, "
      f"N-irreducible factorizations {nt}")
check("S1 cyclotomic core has exactly 2 N-irreducible factorizations",
      nc == 2)
check("S1 transfer specimen has exactly 1", nt == 1)

# ============================================================ S2 the census
print("\n== S2 control: the census rebuilt at the frozen scope ==")
UNIVERSE = tuple(range(2, 17)) + (32,)
menus_all = []
for size in (1, 2, 3):
    menus_all += list(combinations(UNIVERSE, size))

products = {}
npairs = 0
for A, B in combinations_with_replacement(menus_all, 2):
    products.setdefault(dkey(dmul(zdict(A), zdict(B))), []).append((A, B))
    npairs += 1
classes = {k: v for k, v in products.items() if len(v) >= 2}

colliding = [(k, a, b) for k, v in classes.items()
             for a, b in combinations(v, 2)]
n_scaling = sum(1 for _, a, b in colliding if is_scaling(a, b))
n_oneprime = sum(1 for _, a, b in colliding if one_prime(a, b))
n_s_op = sum(1 for _, a, b in colliding
             if is_scaling(a, b) and one_prime(a, b))
n_multi = sum(1 for _, a, b in colliding
              if not is_scaling(a, b) and not one_prime(a, b))
print(f"  menus {len(menus_all)}, pairs {npairs}, "
      f"colliding pair-of-pairs {len(colliding)}, "
      f"collision classes {len(classes)}")
print(f"  partition: scaling {n_scaling} (one-prime {n_s_op}); "
      f"non-scaling {len(colliding) - n_scaling} = "
      f"one-prime {n_oneprime - n_s_op} + multi-prime {n_multi}")
check("S2 menus 696", len(menus_all) == 696)
check("S2 pairs 242556", npairs == 242556)
check("S2 colliding pair-of-pairs 4849", len(colliding) == 4849)
check("S2 collision classes 4487", len(classes) == 4487)
check("S2 scaling 4369", n_scaling == 4369)
check("S2 scaling-and-one-prime 111", n_s_op == 111)
check("S2 non-scaling 480", len(colliding) - n_scaling == 480)
check("S2 non-scaling one-prime 6", n_oneprime - n_s_op == 6)
check("S2 multi-prime 474", n_multi == 474)
print(f"  [{time.perf_counter() - T0:.1f}s]")

# ============================================================ S3 the sweep
print("\n== S3 the sweep: N-irreducible factorizations per colliding"
      " product ==")
CONTRACT_A, CONTRACT_B = (2, 4, 8), (2, 16)
contract_key = dkey(dmul(zdict(CONTRACT_A), zdict(CONTRACT_B)))
check("S3 contract product is a census collision class",
      contract_key in classes)

nonunique = []
by_vars = {}
contract_n = None
for key, pairs in classes.items():
    A, B = pairs[0]
    P = sympy.expand(menu_poly(A) * menu_poly(B))
    n, mons, ncore, nv = n_factorizations(P)
    by_vars.setdefault((n >= 2, nv), 0)
    by_vars[(n >= 2, nv)] += 1
    if n >= 2:
        nonunique.append((key, n, nv, pairs[0]))
    if key == contract_key:
        contract_n = n
        print(f"  contract product {[m for m, _ in key]}: "
              f"N-irreducible factorizations {contract_n}, variables {nv}")
check("S3 contract product factors NON-uniquely", contract_n is not None
      and contract_n >= 2)

# Where the earlier census's three-way sort lands once the products are
# graded by factorization rather than by the primes they mention.
unique_keys = {k for k in classes} - {t[0] for t in nonunique}
n_multi_unique = sum(1 for k, a, b in colliding
                     if k in unique_keys
                     and not is_scaling(a, b) and not one_prime(a, b))
n_scaling_unique = sum(1 for k, a, b in colliding
                       if k in unique_keys and is_scaling(a, b))
n_coll_nonunique = sum(1 for k, _, _ in colliding if k not in unique_keys)
print(f"  of the 474 multi-prime collisions, sitting in a UNIQUELY "
      f"factoring product: {n_multi_unique}")
print(f"  of the {n_scaling} scaling collisions, uniquely factoring: "
      f"{n_scaling_unique}")
print(f"  colliding pair-of-pairs inside a non-unique product: "
      f"{n_coll_nonunique}")

multivar_nonunique = [t for t in nonunique if t[2] >= 2]
print(f"  colliding products {len(classes)}; "
      f"non-uniquely factoring {len(nonunique)}; "
      f"of those with >= 2 variables {len(multivar_nonunique)}")
counts = sorted({n for _, n, _, _ in nonunique})
print(f"  factorization counts seen among the non-unique: {counts}")
vars_seen = sorted({nv for _, _, nv, _ in nonunique})
print(f"  variable counts among the non-unique: {vars_seen}")
for key, n, nv, pair in sorted(nonunique, key=lambda t: t[0])[:6]:
    print(f"    {pair[0]} x {pair[1]} -> product {[m for m, _ in key]}"
          f"  count {n}, vars {nv}")
if multivar_nonunique:
    print("  MULTIVARIATE NON-UNIQUE AT CENSUS SCOPE:")
    for key, n, nv, pair in multivar_nonunique[:10]:
        print(f"    {pair[0]} x {pair[1]} count {n} vars {nv}")
print(f"  [{time.perf_counter() - T0:.1f}s]")

# ============================================================ S4 the mechanism
print("\n== S4 the mechanism map: menus carrying a negative Z-factor ==")
SEED_MAX = 81
seeds = []
n_menus = n_menus_2d = 0
for size in (1, 2, 3):
    for A in combinations(range(2, SEED_MAX + 1), size):
        P = menu_poly(A)
        gens = used_vars(P)
        n_menus += 1
        if size == 3 and newton_dim(P, gens) >= 2:
            n_menus_2d += 1
        _, core = zfactors(P)
        neg = [f for f in core if not is_nonneg(f, gens)]
        if neg:
            seeds.append((A, gens, neg))
n_size3 = len(list(combinations(range(2, SEED_MAX + 1), 3)))
print(f"  menus swept: elements 2..{SEED_MAX}, size <= 3, total "
      f"{n_menus}; seeds found {len(seeds)}")
print(f"  size-3 menus whose OWN Newton polygon is 2-dimensional: "
      f"{n_menus_2d} of {n_size3}")

negcat = {}
for A, gens, neg in seeds:
    for f in neg:
        fg = used_vars(f)
        d = newton_dim(f, fg)
        negcat.setdefault(sympy.srepr(f), (f, len(fg), d, []))[3].append(A)
print(f"  distinct negative Z-irreducible factors: {len(negcat)}")
rows = sorted(negcat.values(), key=lambda r: (r[2], r[1], len(str(r[0]))))
for f, nv, d, owners in rows:
    print(f"    {f}   variables {nv}, Newton dim {d}, "
          f"first menus {owners[:3]}")
maxdim = max((r[2] for r in rows), default=-1)
maxvars = max((r[1] for r in rows), default=0)
print(f"  max Newton dimension over all negative factors: {maxdim}")
print(f"  max variable count over all negative factors: {maxvars}")

census_seeds = [(A, gens, neg) for A, gens, neg in seeds
                if all(m in UNIVERSE for m in A)]
census_bad = [A for A, gens, neg in census_seeds
              if any(len(used_vars(f)) > 1 for f in neg)]
print(f"  seeds inside the census universe: {len(census_seeds)} -> "
      f"{[A for A, _, _ in census_seeds]}")
check("S4 every census-scope seed has a one-variable negative factor",
      not census_bad)
check("S4 {2,16}, {4,32}, {2,8,32} are census-scope seeds",
      all(t in [A for A, _, _ in census_seeds]
          for t in ((2, 16), (4, 32), (2, 8, 32))))
check("S4 some negative factor uses >= 2 variables", maxvars >= 2)
print(f"  [{time.perf_counter() - T0:.1f}s]")

# ============================================================ S5 the specimen
print("\n== S5 the hand specimen: the homogenized mechanism ==")
SPEC1, SPEC2 = ((8, 27), (4, 6, 9)), ((2, 3), (16, 36, 81))
s1 = sorted(a * b for a in SPEC1[0] for b in SPEC1[1])
s2 = sorted(a * b for a in SPEC2[0] for b in SPEC2[1])
print(f"  {SPEC1[0]} x {SPEC1[1]} -> {s1}")
print(f"  {SPEC2[0]} x {SPEC2[1]} -> {s2}")
check("S5 the two pairs have equal product multisets", s1 == s2)
PS = sympy.expand(menu_poly(SPEC1[0]) * menu_poly(SPEC1[1]))
check("S5 the two products are the same polynomial",
      sympy.expand(PS - menu_poly(SPEC2[0]) * menu_poly(SPEC2[1])) == 0)
(ns, mons_s, ncore_s, nvs), spec_list = n_factorizations(PS, want_list=True)
print(f"  common product: {PS}")
print(f"  Z-irreducible factors: {sympy.factor_list(PS)[1]}")
for f in spec_list:
    print(f"     N-irreducible factorization: {[str(b) for b in f]}")
print(f"  N-irreducible factorizations {ns}, variables {nvs}")
check("S5 the specimen factors NON-uniquely", ns == 2)
check("S5 the specimen uses 2 variables", nvs == 2)

# ============================================================ verdict
print(f"\n[total {time.perf_counter() - T0:.1f}s]")
npass = sum(1 for _, ok in CHECKS if ok)
print(f"\n{npass}/{len(CHECKS)} checks pass")
for name, ok in CHECKS:
    if not ok:
        print("  FAILED: " + name)
sys.exit(0 if npass == len(CHECKS) else 1)
