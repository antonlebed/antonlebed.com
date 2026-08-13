"""Menu factorization, third aim: read the collision on the FACES.

THE QUESTION. A MENU is a finite set of integers >= 2; writing each
element in the primes p_1..p_r turns it into a set S of exponent VECTORS
in Z^r_{>=0}, and the menu becomes the 0/1-coefficient polynomial
supported on S. Two menu pairs that are indistinguishable at every
temperature satisfy 1_{S_A} * 1_{S_B} = 1_{S_C} * 1_{S_D} as functions
on Z^r -- an equality of CONVOLUTIONS of indicator functions. The prior
files established that this is a factorization question and that both
observables minted to grade it read ONE factor at a time, while the
mechanism is a RELATION between factors (explore_menu_factorization.py,
explore_menu_reach.py). This file asks what the convolution equality
says about the SUPPORTS, and turns the answer into an observable that
reads the relation.

THE INCUMBENT, READ FULL-TEXT BEFORE THIS SLATE WAS WRITTEN, and it
decides the shape of the file. The support-only content of the equality
is classical in full, in two pieces:
 (O) OSTROWSKI'S THEOREM. The Newton polytope of a product is the
     Minkowski sum of the factors' Newton polytopes. So the equality
     forces conv S_A + conv S_B = conv S_C + conv S_D, and nothing about
     the supports beyond it. Turning that into a factorization
     instrument -- enumerate the Minkowski decompositions of the Newton
     polytope, each is a candidate factorization -- is Gao and Lauder,
     "Decomposition of polytopes and polynomials" (2001).
 (I) INITIAL-FORM MULTIPLICATIVITY. For a weight w, the w-initial form
     of a product is the product of the w-initial forms. Standard, and
     over a semiring with no cancellation it needs no domain argument:
     the coefficient of the product at a point of the w-maximal face can
     only be reached by w-maximal terms of the factors.
So the aim named for this file -- "what does the convolution equality
say about the supports alone" -- is answered by prior work outright.
What is NOT prior is (I) applied to non-uniqueness in this semiring:
the incumbent for that, C. van de Woestijne, "Factors of disconnected
graphs and polynomials with nonnegative integer coefficients" (Ars Math.
Contemp. 5, 2012), classifies by NUMBER OF TERMS t = P(1) via
topological sorting over term bijections and never restricts to a face.
His Theorem 3.20, read here in full, is what makes this file's t <= 10
statement a theorem rather than a sweep.

WHAT (I) BUYS, hand-derived before any engine code. Applying (I) to the
collision gives, for every weight w,
    1_{face_w A} * 1_{face_w B} = 1_{face_w C} * 1_{face_w D},
a collision on every FACE of the product's Newton polytope, in lower
dimension. That is the instrument, and it reads the pair.

THE OBSERVABLE MINTED HERE: THE DESCENT DIMENSION. Let F1 and F2 be two
distinct N-irreducible factorizations of one product P. For a weight w
write ind_w(F) for the multiset obtained by taking in_w(f) for each
f in F, dividing each by its own monomial content, and dropping the
entries that become 1. Then
    delta = min { dim face_w(Newt P) : ind_w(F1) != ind_w(F2) }.
The monomial content is divided out because a monomial is an atom of
the semiring that can sit beside either factor, and a difference of
monomial PLACEMENT is not a difference of mechanism. At w = 0 the face
is the whole polytope and the multisets are F1 and F2 themselves, so
delta is defined and delta <= dim Newt P always. delta < dim says the
two factorizations already differ on a PROPER face: the mechanism is
INHERITED from lower dimension. delta = dim says it is not.

WHY THIS IS THE RIGHT LADDER. Level 0 -- a difference visible at a
VERTEX -- is exactly what the classical polytope instrument (O) can
see, since a vertex reads the factors' Newton polytopes and nothing
finer. Every level above 0 is invisible to it. So the descent dimension
grades a collision by how much more than the supports must be read to
see it, and the corpus's own escape specimen is the test of where that
starts.

WHAT IS ASKED HERE, in four parts. (1) Grade the (2,5) escape specimen
of explore_menu_reach.py: it is not the image of a one-variable
polynomial, so is its mechanism nonetheless one-variable ON A FACE?
(2) Grade the incumbent's COMPLETE t = 10 classification -- the three
sporadic identities and BOTH two-parameter families -- read
multivariately, which is where a non-collinear support can first live.
(3) Grade the objects the corpus already holds at t = 6 and t = 12.
(4) Ask whether anything here reaches delta >= 2.

THE INCUMBENT'S t = 10 CLASSIFICATION, quoted (Theorem 3.20). Up to a
monomial factor and up to replacing X by a power, a 10-term polynomial
with non-unique factorization is one of
  S1  (1+X)(1+X^2+X^4+X^6+X^8)   = (1+X^5)(1+X+X^2+X^3+X^4)
  S2  (1+X)(1+X^4+X^6+X^8+X^12)  = (1+X^5)(1+X+X^4+X^7+X^8)
  S3  (1+X^3)(1+X^2+X^4+X^6+X^8) = (1+X^5)(1+X^2+X^3+X^4+X^6)
or of one of the two families, for integers a >= 0 and b >= 1,
  F1  (1+X^3b)(1+X^a+X^b+X^{a+b}+X^{a+2b})
        = (1+X^b)(1+X^a+X^{a+2b}+X^3b+X^{a+4b})
  F2  (1+X^3b)(1+X^a+X^b+X^{a+b}+X^{2b})
        = (1+X^b)(1+X^a+X^2b+X^{a+3b}+X^4b).
The multivariate reading is his own Lemma 3.10, which makes a
factorization in several variables a compatible tuple of coordinate
projections: a and b become independent VECTORS, and only the two
FAMILIES have two free exponents to spend on that. The three sporadics
carry ONE parameter, so every multivariate lift of them is a monomial
substitution of a one-variable polynomial and its support is collinear.

THE HAND-DERIVATION THIS FILE EXISTS TO CHECK. Take w with <w,b> = 0
and <w,a> != 0, which exists exactly when a and b are independent.
Every power of X^b ties at 0, so the face is decided by the a-part.
  F1, at <w,a> > 0: the left factors are unmoved (1+X^3b has no a) and
  the right ones keep their a-terms, giving
      (1+v^3) * u(1+v+v^2)  =  (1+v) * u(1+v^2+v^4),
  writing u = X^a, v = X^b. Dividing out the monomial content the two
  multisets are {1+v^3, 1+v+v^2} and {1+v, 1+v^2+v^4}: DIFFERENT, on a
  face that spans only b, hence of dimension 1.
  F2, at <w,a> > 0: the same computation gives {1+v^3, 1+v} against
  {1+v, 1+v^3} -- the SAME multiset, so that face is trivial and F2 is
  not graded there. At <w,a> < 0 the a-terms drop instead and F2 gives
      (1+v^3)(1+v+v^2)  =  (1+v)(1+v^2+v^4),
  the same cyclotomic identity, again on a face of dimension 1.
So both families are predicted to descend to ONE identity, the t = 6
cyclotomic collision, and F2 is the case that shows the monomial-content
division is load-bearing rather than cosmetic: without it F2 would be
graded on a face where nothing but a monomial has moved.

DESIGN, five stages.
 S0 THE FACE MACHINERY, controlled in both directions. The weight box
    must recover the exact face count of a known polygon, and a
    deliberately trivial pair must read trivial.
 S1 THE COUNTER, as in the companion files: the cyclotomic core prints
    2 semiring-irreducible factorizations and a monomial specimen 1.
 S2 THE ESCAPE SPECIMEN, as menus: {2,54}x{2,6,10,30,90} against
    {2,6}x{2,10,54,90,810}. Product Newton dimension, delta, and the
    face identity printed at the minimizing weight.
 S3 THE COMPLETE t = 10 CLASSIFICATION. The two families instantiated
    with a and b as INDEPENDENT vectors -- (a,b) = ((1,0),(0,1)) and
    ((1,1),(0,1)), the second to check the grading does not depend on
    the vectors being a coordinate frame -- and the three sporadics
    lifted by the only lift they admit. Each graded.
 S4 THE CORPUS'S OWN RUNGS. The t = 6 identity and the t = 12 instance
    {2,8,32}x{2,4,16,32}, graded. Nusken's t = 12 example (3.2) is NOT
    included: it carries a coefficient 2 and is therefore not a menu.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): the weight box finds exactly 8 proper faces of the escape
      specimen's polygon (4 vertices, 4 edges), and the trivial pair
      reads trivial.
  PR1 (S1): 2 and 1.
  PR2 (S2): product Newton dimension 2, delta = 1, and the face at the
      minimizing weight is the cyclotomic identity
      (1+v^3)(1+v+v^2) = (1+v)(1+v^2+v^4) up to monomial content.
  PR3 (S3, families): both F1 and F2, at both vector choices, have
      product dimension 2 and delta = 1, with the same cyclotomic face.
  PR4 (S3, sporadics): every lift has product Newton dimension <= 1, so
      delta <= 1 with no face argument needed.
  PR5 (S4): the t = 6 identity has dimension 1 and delta = 1; the t = 12
      instance has dimension 1 and delta = 1.
  PR6 (all stages): nothing here reaches delta >= 2.

KILLS (observables with live failure modes; the meaning is weighed after
the run, never before).
  K0: the weight box misses a face of the control polygon, or the
      trivial pair reads non-trivial -- the instrument is broken and no
      delta below is read.
  K1: either S1 number is wrong -- the counter is broken.
  K2: the escape specimen reads delta = 2 -- the hand-derivation above
      is wrong, since it exhibits a differing face of dimension 1.
  K3: any object here reads delta >= 2. This is the outcome worth
      hunting: it would say the mechanism is NOT face-inherited and the
      ladder bottoms out above one variable.
  K4: a family reads a differing face that is not the cyclotomic
      identity -- the descent is to something else, and the "one
      mechanism at t <= 10" reading falls.

FINDINGS (tiers per the standard naming scale; run record below).

0. TWO CORRECTIONS TO THE SLATE ABOVE, found by the audit that followed
   the run. The slate is left as frozen and both are stated here.
   (i) "WHY THIS IS THE RIGHT LADDER" IS WRONG, IN THE DIRECTION THAT
   FLATTERS THIS FILE. It claims level 0 is what the classical polytope
   instrument sees and that everything above 0 is invisible to it.
   Neither half holds. Level 0 is UNREACHABLE by construction: at a
   vertex every initial form is a single monomial -- a point is a
   Minkowski sum only of points -- with COEFFICIENT 1, since a vertex of
   the sum decomposes uniquely and the two menus are 0/1, so the
   product's vertex coefficients are 1 and each factor's therefore
   divides 1. Dividing out the monomial content leaves 1 on every entry
   and empties BOTH multisets, so no vertex can ever grade a collision:
   delta >= 1 always, and the run confirms it at the escape polygon's
   four vertices. The coefficient step is what makes "empties" true
   rather than "leaves a constant", and it is where the 0/1 hypothesis
   enters. And the classical
   instrument is not blind above 0: the escape's two factorizations have
   DIFFERENT factor Newton polytopes -- the segments [0,3] and [0,1]
   along the second variable -- so their Minkowski decompositions differ
   and Gao-Lauder would separate them. The descent dimension is
   therefore NOT a refinement of the polytope instrument; it is a
   different reading, and what it buys is not invisibility to the
   classical one but the LOCATION of the mechanism -- which face, and
   which identity sits on it. Findings 3, 4 and 5 rest on that and are
   untouched.
   (ii) "ONE PARAMETER" IS THE WRONG COUNT for the t = 6 form and the
   three sporadics. Each carries TWO free exponents, since "up to
   multiplication by a power of X" is a parameter as much as "up to
   replacing X by a power". What makes their lifts collinear is that one
   of the two enters as a TRANSLATION: the exponent vectors are
   alpha + t_i*beta with the t_i fixed by the identity, an arithmetic
   progression along beta whatever alpha is. That is the same
   two-dimensional solution space explore_menu_reach.py's correction
   (ii) had to restore for its own t = 6 derivation, and this file
   walked past it a second time. The conclusion stands; its stated
   reason did not.

1. THE AIM AS POSED RETIRES AGAINST PRIOR WORK (prior result, applied).
   "What does the convolution equality say about the SUPPORTS alone" is
   answered in full by Ostrowski's theorem: the equality forces
   conv S_A + conv S_B = conv S_C + conv S_D and nothing else, and the
   instrument built on that -- read the Minkowski decompositions of the
   Newton polytope as candidate factorizations -- is Gao and Lauder.
   The support statement is also STRICTLY weaker than the factor one,
   with a hand witness needing no engine: {0,1}+{0,1,3} and
   {0,1,2}+{0,2} have the same sumset {0,1,2,3,4} and the same mass 6,
   and their convolutions differ (1+2x+x^2+x^3+x^4 against
   1+x+2x^2+x^3+x^4). So the supports cannot be the mechanism, and this
   is the THIRD time this line of work has aimed at work the literature had
   already done.

2. THE PRODUCTIVE RESIDUE IS THE OTHER HALF OF THE SUPPORT READING, AND
   IT READS THE PAIR (property). Initial-form multiplicativity turns the
   collision into a collision on EVERY face of the product's Newton
   polytope. The DESCENT DIMENSION defined above grades a collision by
   the smallest face that already sees the difference, and unlike the
   product's variable count and the negative factor's Newton dimension
   -- this line of work's two spectators, both reading one factor at a time
   -- it is a function of the two factorizations jointly. Its levels run
   from 1 to dim (finding 0 (i)), and what a level buys is the LOCATION
   of the mechanism: the smallest face already carrying it, and the
   identity sitting there.

3. THE ESCAPE IS NOT A ONE-VARIABLE IMAGE AND IS A ONE-VARIABLE DESCENT
   (rule, proved and verified exactly). The (2,5) specimen
   {2,54}x{2,6,10,30,90} against {2,6}x{2,10,54,90,810} has a
   two-dimensional product polygon and delta = 1: at the weight
   maximizing the u-part its two factorizations induce
   (1+v^3)(1+v+v^2) against (1+v)(1+v^2+v^4) on an edge -- the t = 6
   cyclotomic identity itself. So explore_menu_reach.py's headline
   stands as written and was incomplete as a reading: the mechanism is
   not an IMAGE of one variable, and it is inherited from one variable
   on a FACE. The second variable rides the co-factors exactly as that
   file's finding 3 says, and the face is where the ride becomes
   visible.

4. AT t <= 10 EVERY MECHANISM IS ONE-VARIABLE (rule, proved from the
   incumbent's classification; four instances verified). Every
   non-uniqueness with t <= 10 terms has delta <= 1: it is carried by a
   face of dimension at most 1, so no collision there is more than a
   one-variable identity plus the co-factors riding it. NOT "one
   mechanism" -- the three sporadic t = 10 identities are regroupings of
   Phi_2 Phi_5 Phi_10, a different identity from the t = 6 one, and
   being collinear they are their own faces. What the two FAMILIES
   descend to is the t = 6 cyclotomic identity, and that is the claim
   is_cyclotomic_face tests, on the families and the escape and nowhere
   else. Proof: t = 4, 8, 9 are unique and
   t = 1, 2, 3, 5, 7 are trivial or prime, so only t = 6 and t = 10
   carry non-uniqueness. Theorem 3.17's t = 6 form spends one of its two
   free exponents on a TRANSLATION, so its exponent vectors are
   alpha + t_i*beta and every multivariate lift is collinear --
   dimension <= 1, delta <= 1 with no face argument needed, and the same
   holds for Theorem 3.20's three sporadic identities, confirmed here by
   lifting each into two variables along independent alpha and beta.
   The two 2-parameter families are the only place a
   non-collinear support can live -- the lift step being Lemma 3.10
   applied coordinate by coordinate, exactly as explore_menu_reach.py's
   (b) does at t = 6, so a free exponent becomes a free VECTOR and the
   translation is the all-ones direction -- and for both, a weight w with
   <w,b> = 0 and <w,a> != 0 -- which exists exactly when a and b are
   independent, in any number of variables -- cuts a face spanning b
   alone, of dimension 1, carrying the cyclotomic identity. The engine
   confirms this at both families and at two independent vector choices
   each, ((1,0),(0,1)) and ((1,1),(0,1)). COROLLARY: delta >= 2 requires
   t >= 12. Not t >= 11: a prime t factors uniquely by Lemma 3.4, so the
   first live count past the classification is the first COMPOSITE one,
   and the size pairs there are (2,6) and (3,4). Only ONE of those is a
   pair the reach file priced out of its boxes -- (3,4), at 18 minutes,
   beside (4,4) at 90; (2,6) is past every menu size any sweep in this
   corpus has reached, size 5 already being outside them. Between the
   two there is exactly one graded point, S4's t = 12 instance.
   (SETTLING POINTER, added later: the 18-minute price is wrong by about
   4.4x -- the walk is bounded by the seed count, not the menu count --
   and (3,4) has since been swept, with the descent dimension graded on
   every collision it holds. The corollary above is untouched; what
   changes is only that its cheap half is no longer unswept. What the
   sweep found is that file's to state: explore_descent_hunt.py.)

5. THE MONOMIAL-CONTENT DIVISION IS LOAD-BEARING (observation, and F2 is
   the witness). At <w,a> > 0 the second family induces {1+v^3, 1+v}
   against {1+v, 1+v^3}: the same multiset, differing only in which
   factor the monomial X^a sits beside. Read without dividing out the
   monomial content that face would grade as a difference, and the
   family would appear to descend at a face where nothing but an atom
   has moved. Its real descent is at <w,a> < 0, where the a-terms drop
   instead and the cyclotomic identity appears -- which the run
   confirms, minimizing at w = (-1, 0) for F2 against w = (8, 0) for F1.

6. NOTHING HERE REACHES delta >= 2 (observation, over every object in
   this file; the scope clause is load-bearing and the corollary's own
   target has since been hit -- explore_descent26.py exhibits a delta = 2
   collision at t = 12, past every object this file grades, so what stands
   below is a statement about these ten and never about the question).
   All TEN graded objects -- the escape specimen, the two
   families at two vector choices each, the three lifted sporadics, the
   t = 6 identity and the t = 12 instance -- read delta = 1, which for
   the five one-dimensional ones is forced and for the five
   two-dimensional ones is the finding. The split is the printed dim
   column and not a recount: dim = 2 at the escape and at all four
   family lifts, dim = 1 at the three sporadics, the t = 6 identity and
   the t = 12 instance. Level 0 is not merely
   unoccupied but unreachable, for the reason finding 0 (i) gives; the
   delta = 0 the run printed once came from an object carrying a
   coefficient 2, a transcription error caught by that object's own
   products-agree check and by nothing else.

THE HEADLINE. The support reading is classical and strictly weaker, but
its second half -- the faces -- is the instrument this line of work was
missing, because it is the first observable that reads the two
factorizations jointly. Read through it, every collision the corpus and
the literature hold below t = 12 is a ONE-VARIABLE identity plus the
co-factors riding it -- several distinct identities, all of them
cyclotomic regroupings, each on a face of dimension at most 1 -- and the
corpus's own escape, announced as the falsification of the one-variable
reading, is the t = 6 identity seen on an edge.

HONEST LIMITS carried into the reading, stated before the run. (i) The
weight box is a SAMPLE of the normal fan, complete for the objects here
only because S0 checks the face count against the polygon; a higher-
dimensional object would need the fan computed. (ii) t <= 10 is where
the incumbent classifies, so a statement about all collisions there is a
theorem and a statement about t >= 12 is about the named objects only.
(iii) Nothing here is a realization claim.
RUN RECORD (this file, under memwatch.py at the 512MB default, 0.8 s
wall, peak working set 53.8 MB). Run 1: 37/38, the single failure a
transcription error in the first sporadic's left factor -- (1,1) for
(0,1), i.e. 2X where 1+X was meant -- caught by that object's own
products-agree check and by nothing else. Run 2 after the fix: 38/38,
every prediction PR0-PR6 held as written and no kill fired. Run 3, after
the audit added the vertex check of finding 0 (i) and lifted the
sporadics as S3's design had said and the code had not: 39/39, both new
checks green. Run 4, after the audit found finding 1's support witness
cited to this file and tested nowhere in it: 41/41.
"""

import os
import sys
import time
from itertools import combinations, product as iproduct

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import Poly

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import (X, check, CHECKS, menu_poly, newton_dim,
                                n_factorizations, used_vars)

WBOX = 8


# ------------------------------------------------------------------ face tools
def exps(expr, gens):
    return [tuple(m) for m in Poly(expr, *gens).monoms()]


def face_support(pts, w):
    best = max(sum(c * wi for c, wi in zip(p, w)) for p in pts)
    return [p for p in pts if sum(c * wi for c, wi in zip(p, w)) == best]


def initial_form(expr, gens, w):
    P = Poly(expr, *gens)
    keep = set(face_support([tuple(m) for m in P.monoms()], w))
    out = 0
    for mon, coeff in zip(P.monoms(), P.coeffs()):
        if tuple(mon) in keep:
            term = coeff
            for g, e in zip(gens, mon):
                term *= g ** e
            out += term
    return sympy.expand(out)


def primitive(expr, gens):
    """Divide out the monomial content."""
    P = Poly(expr, *gens)
    mons = [tuple(m) for m in P.monoms()]
    shift = [min(m[i] for m in mons) for i in range(len(gens))]
    div = 1
    for g, e in zip(gens, shift):
        div *= g ** e
    return sympy.expand(sympy.cancel(expr / div))


def induced(fac, gens, w):
    out = []
    for f in fac:
        p = primitive(initial_form(f, gens, w), gens)
        if p != 1:
            out.append(sympy.srepr(p))
    return tuple(sorted(out))


def affine_rank(pts):
    if len(pts) < 2:
        return 0
    base = pts[0]
    rows = [[a - b for a, b in zip(p, base)] for p in pts[1:]]
    return sympy.Matrix(rows).rank()


def weight_box(r, b=WBOX):
    for w in iproduct(range(-b, b + 1), repeat=r):
        if any(w):
            yield w


def faces_seen(pts, r):
    seen = {}
    for w in weight_box(r):
        seen[tuple(sorted(face_support(pts, w)))] = w
    return seen


def descent(fac1, fac2, gens):
    """(product Newton dimension, delta, minimizing weight)."""
    prod = sympy.expand(sympy.prod(fac1))
    pts = exps(prod, gens)
    dim = affine_rank(pts)
    best_d, best_w = dim, None
    for face, w in faces_seen(pts, len(gens)).items():
        if induced(fac1, gens, w) != induced(fac2, gens, w):
            d = affine_rank(list(face))
            if d < best_d:
                best_d, best_w = d, w
    return dim, best_d, best_w


def report(label, fac1, fac2, gens):
    dim, d, w = descent(fac1, fac2, gens)
    print(f"  {label:<34} dim={dim}  delta={d}  w={w}")
    if w is not None:
        f1 = [primitive(initial_form(f, gens, w), gens) for f in fac1]
        f2 = [primitive(initial_form(f, gens, w), gens) for f in fac2]
        f1 = [f for f in f1 if f != 1]
        f2 = [f for f in f2 if f != 1]
        print(f"      face: {'  *  '.join(map(str, f1))}"
              f"   ==   {'  *  '.join(map(str, f2))}")
    return dim, d


# ------------------------------------------------------- the cyclotomic marker
def is_cyclotomic_face(fac1, fac2, gens, w):
    """Both sides equal the t=6 identity in ONE variable, up to monomials."""
    if w is None:
        return False
    sides = []
    for fac in (fac1, fac2):
        ps = [primitive(initial_form(f, gens, w), gens) for f in fac]
        ps = [p for p in ps if p != 1]
        sides.append(sorted(sympy.srepr(p) for p in ps))
    got = set()
    for side in sides:
        for s in side:
            e = sympy.sympify(s)
            vs = used_vars(e)
            if len(vs) != 1:
                return False
            v = vs[0]
            got.add(sympy.srepr(sympy.expand(e.subs(v, X[0]))))
    want = {sympy.srepr(sympy.expand(p)) for p in
            (1 + X[0]**3, 1 + X[0] + X[0]**2, 1 + X[0], 1 + X[0]**2 + X[0]**4)}
    return got == want


# ============================================================ S0  the machinery
ESC_A, ESC_B = (2, 54), (2, 6, 10, 30, 90)
ESC_C, ESC_D = (2, 6), (2, 10, 54, 90, 810)


def stage0():
    print("\n=== S0  the face machinery, both directions ===")
    u, v = X[0], X[1]
    prod = sympy.expand(menu_poly(ESC_A) * menu_poly(ESC_B))
    gens = [X[1], X[2]]          # 54 = 2*27, 90 = 2*3^2*5 -> vars x0,x1,x2
    gens = used_vars(prod)
    pts = exps(prod, gens)
    seen = faces_seen(pts, len(gens))
    proper = [f for f in seen if len(f) < len(pts)]
    print(f"  escape polygon: {len(pts)} points, "
          f"{len(seen)} faces seen, {len(proper)} proper")
    check("S0 the weight box finds 8 proper faces", len(proper) == 8)

    # The supports are strictly weaker than the convolutions: same
    # sumset, same mass, different multiplicity function.
    w1 = [sympy.expand(1 + u), sympy.expand(1 + u + u**3)]
    w2 = [sympy.expand(1 + u + u**2), sympy.expand(1 + u**2)]
    p1, p2 = sympy.expand(w1[0] * w1[1]), sympy.expand(w2[0] * w2[1])
    s1 = {m[0] for m in Poly(p1, u).monoms()}
    s2 = {m[0] for m in Poly(p2, u).monoms()}
    print(f"  support witness: sumsets {sorted(s1)} / {sorted(s2)}, "
          f"masses {p1.subs(u, 1)} / {p2.subs(u, 1)}")
    print(f"    convolutions {p1}   vs   {p2}")
    check("S0 the support witness shares its sumset and its mass",
          s1 == s2 and p1.subs(u, 1) == p2.subs(u, 1))
    check("S0 the support witness has DIFFERENT convolutions",
          sympy.expand(p1 - p2) != 0)

    g = [u, v]
    triv1 = [sympy.expand(1 + u**3), sympy.expand(1 + v)]
    triv2 = [sympy.expand(1 + v), sympy.expand(1 + u**3)]
    same = all(induced(triv1, g, w) == induced(triv2, g, w)
               for w in weight_box(2, 3))
    check("S0 an identical pair reads trivial at every weight", same)


# ============================================================ S1  the counter
def stage1():
    print("\n=== S1  the counter ===")
    x, y = X[0], X[1]
    n, _ = n_factorizations(sympy.expand((1 + x + x**2) * (1 + x**3)))
    m, _ = n_factorizations(sympy.expand(x * y * (1 + x)))
    print(f"  cyclotomic core -> {n}   monomial specimen -> {m}")
    check("S1 cyclotomic core prints 2", n == 2)
    check("S1 monomial specimen prints 1", m == 1)


# ============================================================ S2  the specimen
def stage2():
    print("\n=== S2  the (2,5) escape specimen, as menus ===")
    p1 = [menu_poly(ESC_A), menu_poly(ESC_B)]
    p2 = [menu_poly(ESC_C), menu_poly(ESC_D)]
    lhs, rhs = sympy.expand(p1[0] * p1[1]), sympy.expand(p2[0] * p2[1])
    check("S2 the two products agree", sympy.expand(lhs - rhs) == 0)
    gens = used_vars(lhs)
    dim, d = report("escape specimen", p1, p2, gens)
    check("S2 the product polygon is 2-dimensional", dim == 2)
    check("S2 the escape descends: delta = 1", d == 1)
    _, _, w = descent(p1, p2, gens)
    check("S2 the differing face is the cyclotomic identity",
          is_cyclotomic_face(p1, p2, gens, w))

    # Is level 0 reachable at all? At a VERTEX every initial form of a
    # 0/1 product is a single monomial, so the monomial-content division
    # empties both multisets and no vertex can ever grade a collision.
    pts = exps(sympy.expand(p1[0] * p1[1]), gens)
    verts = [(f, w) for f, w in faces_seen(pts, len(gens)).items()
             if affine_rank(list(f)) == 0]
    print(f"  vertices of the escape polygon: {len(verts)}")
    empty = all(induced(p1, gens, w) == () == induced(p2, gens, w)
                for _, w in verts)
    check("S2 every vertex induces the EMPTY multiset on both sides",
          empty and len(verts) == 4)


# ============================================================ S3  t = 10, all
def fam(kind, a, b, gens):
    """The incumbent's two families with a, b as exponent VECTORS."""
    def m(vec):
        t = 1
        for g, e in zip(gens, vec):
            t *= g ** e
        return t
    A, B = m(a), m(b)
    if kind == "F1":
        return ([sympy.expand(1 + B**3),
                 sympy.expand(1 + A + B + A * B + A * B**2)],
                [sympy.expand(1 + B),
                 sympy.expand(1 + A + A * B**2 + B**3 + A * B**4)])
    return ([sympy.expand(1 + B**3),
             sympy.expand(1 + A + B + A * B + B**2)],
            [sympy.expand(1 + B),
             sympy.expand(1 + A + B**2 + A * B**3 + B**4)])


SPORADIC = [
    ("S1 sporadic", (0, 1), (0, 2, 4, 6, 8), (0, 5), (0, 1, 2, 3, 4)),
    ("S2 sporadic", (0, 1), (0, 4, 6, 8, 12), (0, 5), (0, 1, 4, 7, 8)),
    ("S3 sporadic", (0, 3), (0, 2, 4, 6, 8), (0, 5), (0, 2, 3, 4, 6)),
]


def stage3():
    print("\n=== S3  the complete t = 10 classification ===")
    gens = [X[0], X[1]]
    for kind in ("F1", "F2"):
        for a, b in (((1, 0), (0, 1)), ((1, 1), (0, 1))):
            f1, f2 = fam(kind, a, b, gens)
            check(f"S3 {kind} a={a} b={b}: products agree",
                  sympy.expand(f1[0] * f1[1] - f2[0] * f2[1]) == 0)
            dim, d = report(f"{kind}  a={a} b={b}", f1, f2, gens)
            check(f"S3 {kind} a={a} b={b}: dim 2", dim == 2)
            check(f"S3 {kind} a={a} b={b}: delta = 1", d == 1)
            _, _, w = descent(f1, f2, gens)
            check(f"S3 {kind} a={a} b={b}: cyclotomic face",
                  is_cyclotomic_face(f1, f2, gens, w))

    print("  the sporadics, lifted by the only lift they admit")
    alpha, beta = (1, 0), (1, 2)          # translation, direction: independent
    for name, e1, e2, e3, e4 in SPORADIC:
        def lift(es):
            out = 0
            for e in es:
                term = 1
                for g, c in zip(gens, alpha):
                    term *= g ** c
                for g, c in zip(gens, beta):
                    term *= g ** (c * e)
                out += term
            return sympy.expand(out)
        f1, f2 = [lift(e1), lift(e2)], [lift(e3), lift(e4)]
        check(f"S3 {name}: products agree",
              sympy.expand(f1[0] * f1[1] - f2[0] * f2[1]) == 0)
        dim, d = report(name, f1, f2, gens)
        check(f"S3 {name}: dimension <= 1 under a two-variable lift", dim <= 1)
        check(f"S3 {name}: delta <= 1", d <= 1)


# ============================================================ S4  corpus rungs
def stage4():
    print("\n=== S4  the corpus's own rungs ===")
    x = X[0]
    f1 = [sympy.expand(1 + x + x**2), sympy.expand(1 + x**3)]
    f2 = [sympy.expand(1 + x), sympy.expand(1 + x**2 + x**4)]
    dim, d = report("t = 6 cyclotomic", f1, f2, [x])
    check("S4 t=6 dimension 1", dim == 1)
    check("S4 t=6 delta = 1", d == 1)

    prod = sympy.expand(menu_poly((2, 8, 32)) * menu_poly((2, 4, 16, 32)))
    gens = used_vars(prod)
    n, facs = n_factorizations(prod)
    print(f"  t = 12 instance {{2,8,32}}x{{2,4,16,32}} -> {n} factorizations")
    check("S4 the t=12 instance factors in exactly 2 ways", n == 2)
    dim, d = report("t = 12 instance", facs[0], facs[1], gens)
    check("S4 t=12 dimension 1", dim == 1)
    check("S4 t=12 delta = 1", d == 1)


def main():
    t0 = time.time()
    stage0()
    stage1()
    stage2()
    stage3()
    stage4()
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok}/{len(CHECKS)} checks passed in {time.time() - t0:.1f}s")
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
