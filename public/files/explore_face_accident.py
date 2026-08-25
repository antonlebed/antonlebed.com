"""THE EXACT FACE LAW: the parallel-edge criterion's converse, proved, and the
accident it turns out to name.

THE QUESTION. explore_descent26_why.py derived the parallel-edge criterion --
on a collision {p*n, q} against {p, n*q} a face w separates only if in_w(n)
is non-monomial and at least one of in_w(p), in_w(q) is -- and proved the
necessary half. The sufficient half was left as an observation over 231
face readings at 18 objects: "two non-monomial initial forms could in
principle induce equal multisets by accident, and that they never do is an
observation". This file asks what the accident IS, whether it can happen at
all, and what the criterion reads once it is named.

WHOSE VOCABULARY. The faces vocabulary of the predecessor, unchanged: initial
forms in_w, the primitive part prim (the monomial content divided out), the
induced multiset of primitive initial forms per factorization. The menu
boxes are the predecessor's sampling frame and nothing more; the specimens
below are stated as polynomials first and wear menu clothes only to show
they are objects the counter's own definition admits.

THE HAND-ATTACK, on paper before any engine code, in four parts.

PART ONE -- THE LAW. Write P, N, Q for the primitive initial forms of p, n, q
at a weight w. Initial forms multiply, and so does the primitive part: the
least exponent of each variable in a product is the sum of the least
exponents, since the lowest-x_i parts multiply to something nonzero over a
domain. Spectators contribute the same primitive initial form to both sides
and cancel. So the two sides read

    {P*N, Q}   against   {P, N*Q}

as two-element multisets over Z[x]. They are EQUAL exactly when N = 1 or
P = Q: if equal, either P*N = P (so N = 1, cancelling P in a domain) or
P*N = N*Q (so P = Q); and conversely either condition gives equality on
sight. Hence

    A FACE SEPARATES IF AND ONLY IF in_w(n) IS NON-MONOMIAL AND
    prim in_w(p) != prim in_w(q).

Both directions are proved. The predecessor's clause "at least one of
in_w(p), in_w(q) is non-monomial" is implied (two monomials share the
primitive part 1) and is not sufficient: the ACCIDENT is exactly P = Q with
N non-monomial -- p and q sharing a primitive initial form at a face where n
does not collapse. One sign remark makes the law exact rather than
up-to-units: a vertex of Newt(n) carries coefficient +1 in this frame,
because in_w(p) is a nonzero face of a 0/1 polynomial and in_w(p)*in_w(n)
is a face of the 0/1 polynomial p*n, so a monomial in_w(n) = c*x^a forces
c = 1. So "N = 1" and "in_w(n) is a monomial" are the same condition here.

PART TWO -- WHY THE ACCIDENT NEVER FIRED AT THE 18. At 17 of the 18 objects
q is a collinear trinomial (x0^2 + x0 + 1, or at the two seeded by {8,27}
its homogenization x0^2 + x0 x1 + x1^2), whose Newton polytope is a SEGMENT:
every proper face is a vertex, so a non-monomial in_w(q) is all of q, three
terms, and never the primitive part of a two-term p (the term count is
invariant under dividing out a monomial). At the witness p = x0 + 1 and
q = x0 + x1 are distinct primitive binomials, so any face where both are
non-monomial reads P = p != q = Q. So at every one of the 18 the sufficient
half is a THEOREM and the 231 readings confirmed rather than established it.

PART THREE -- THE ACCIDENT IS REAL, IN A GENUINE COLLISION. In one variable
every polytope is a segment, so P = Q non-monomial forces p and q to be
associates and the two factorizations to coincide: an accident needs two
variables and a q whose polygon carries an edge equal to p up to a monomial.
Take p = 1 + t, n = 1 - t + t^2 (so p*n = 1 + t^3), and q = (1 + t) +
y*(1 + t + t^2). Then n*q = (1 + t^3) + y*(1 + t^2 + t^4) is nonnegative
0/1, and the product F = (1 + t^3)*q carries 10 distinct terms, all
coefficients 1. Its Z-irreducible factors are 1 + t, 1 - t + t^2 and q (q is
linear in y with coprime coefficients), and the nonnegative atomic
factorizations are exactly {1 + t^3, q} and {1 + t, n*q}: two, a collision
by the counter's definition, of the shared-factor shape the criterion is
stated over. At the bottom face w = (0,-1): in_w(p) = 1 + t = in_w(q), and
in_w(n) = n is non-monomial. The old clause fires; the two sides read
{1 + t^3, 1 + t} against {1 + t, 1 + t^3} and do not separate. The top face
w = (0,1) reads in_w(q) = 1 + t + t^2 != 1 + t and separates, so delta = 1
and the misread costs nothing here. In menu clothes the collision is
{2,16}.{2,4,6,12,24} = {2,4}.{2,6,16,24,96}: a size pair (2,5) at term
count 10, elements reaching 96 -- outside every box the corpus walked.

PART FOUR -- AND THE ACCIDENT CAN SWALLOW EVERY PARALLEL FACE, WHICH IS A
SECOND FULL-DIMENSION MECHANISM. Keep p and n and set

    q = (1 + t) + y*(1 + t + t^2) + y^2*(1 + t).

q is irreducible (degree 2 in y: any split (a + b y)(c + d y) with ac = bd =
1 + t forces ad + bc into {2 + 2t + t^2, 2 + 2t} up to sign, neither 1 + t + t^2) and
not divisible by 1 + t (q at t = -1 is y). n*q = (1 + t^3) + y*(1 + t^2 +
t^4) + y^2*(1 + t^3) is nonnegative 0/1, and F = (1 + t^3)*q carries 4 + 6
+ 4 = 14 distinct terms, all coefficients 1. Two atomic factorizations,
{1 + t^3, q} and {1 + t, n*q}, as before. Its Newton polygon has vertices
(0,0), (4,0), (5,1), (4,2), (0,2). Bottom and top edges: in_w(q) = 1 + t =
in_w(p) with in_w(n) = n non-monomial -- both ACCIDENTS. The two right edges
(w = (1,-1) and (1,1)) and the left edge (w = (-1,0)) read in_w(n) a
monomial. Every vertex is a monomial. So NO proper face separates and delta
= 2 -- while the old edge criterion reads delta = 1, n's segment being
parallel to p's direction (1,0) and to two edges of q. The witness of the
wide box was a negative cofactor whose polygon has NO edge parallel to
either block; this is a negative cofactor whose every parallel edge is an
accident. Two ways an edge of Newt(n) can fail to separate -- an object
may mix them -- and the criterion as published sees one. In menu clothes: {2,16}.{2,4,6,12,18,24,36} =
{2,4}.{2,6,16,18,24,96,144}, size pair (2,7), term count 14.

Both specimens are FROZEN here, derived by hand; the run confirms each with
the corpus's own counter and face reader and reads nothing else off them.

THE DESIGN, four stages.
 S0 THE CONTROLS, run before any generated number is read.
    (a) The imported counter reproduces the published t = 6 cyclotomic
        identity as exactly two factorizations.
    (b) The predecessor's generator reproduces its published pilot box:
        8 in-frame objects, 7 at delta 1 and 1 at delta 2, the delta = 2
        object being {3,4,8,9,18,24} x {2,3}. Nothing below is read on a
        failure.
 S1 THE LAW AT THE PUBLISHED POPULATION. The wide box {2..32} regenerated
    by the predecessor's generator (its 18 in-frame shared-factor objects),
    and at every face of every object the exact law -- separates iff
    in_w(n) non-monomial and prim in_w(p) != prim in_w(q) -- is checked
    against the induced multisets, and the accident faces (old clause fires,
    face does not separate) are COUNTED, with the part-two reason printed
    per object: q's polytope a segment, or p and q distinct binomials.
 S2 THE TWO FROZEN SPECIMENS. For each: the counter's factorization count
    and blocks, the frame (all coefficients 1), the exact proper faces of
    the product polygon with the weight sample checked to produce every one
    of them, the face-by-face reading, delta, the old edge criterion's
    verdict and the exact law's verdict.
 S3 THE SEARCH, in the accident's own shape and in a stated box. p = 1 + t;
    n = B/(1 + t) for every 0/1 univariate B of degree at most D with a
    negative quotient; q = q_0 + y q_1 + y^2 q_2 with each layer a 0/1
    univariate of degree at most D, q_0 = t^a (1 + t) (the accident
    placed at the bottom face), every layer's product with n and with
    B nonnegative 0/1 (so F = B*q is 0/1), q primitive in t and not
    divisible by 1 + t. Every candidate is confirmed by the counter, read
    face by face at its exact proper faces, and graded; objects are
    deduplicated on the product's support up to translation. D = 5 in
    this slate; the box bounds degrees and nothing the mathematics names,
    so the run prints D = 4, 5 and 6 and the record quotes the largest.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): both controls hold.
  PR1 (S1): the exact law agrees with separation at every face of every
      one of the 18 objects, in both directions. This is a theorem; a
      disagreement is an engine fault and not a finding.
  PR2 (S1): the accident count over the 18 objects is ZERO, and the printed
      reason is part two's at every object: q collinear at 17, p != q at
      the witness.
  PR3 (S2): both specimens are collisions with exactly two factorizations;
      the 10-term one reads delta 1 with one accident face; the 14-term one
      reads delta 2 with two accident faces, and the old edge criterion
      reads 1 there -- a misgrade -- while the exact law reads 2.
  PR4 (S3): the search finds at least two delta = 2 objects, the frozen
      14-term specimen among them.
  PR5: NOT PREDICTED. The counts: how many genuine collisions the box
      holds, how many carry an accident face, how the old criterion's
      misgrades split between delta 1 and delta 2.

KILLS (observables; what each MEANS is weighed after the run).
  K0: a control fails. Nothing below is read.
  K1: any face at any object disagrees with the exact law. The algebra of
      part one is wrong, or the reader is.
  K2: the accident count at the 18 is positive. Part two's reason is wrong
      at that object, and the published 231-reading record was misread.
  K3: a specimen is not a collision (the counter returns one factorization),
      or the 14-term specimen has a separating proper face. Part three or
      four is wrong on paper.
  K4: the search returns only the frozen specimen at delta 2, or none.

RESOURCE ENVELOPE (named before the run). The wide-box regeneration is the
predecessor's, 236 s and 132 MB at its last record; the search is bounded
by (number of admissible n) x (admissible layers)^2 dictionary products
plus one counter call per surviving candidate. Estimate under 10 minutes
and under 200 MB; run under memwatch at the default ceiling.

FINDINGS (tiers per the standard naming scale; run record below).

1. THE EXACT FACE LAW (criterion, proved both ways in part one; checked at
   157 faces over the wide box's 18 shared-factor objects, 39 of them
   separating, 0 disagreements in either direction, and at every face of
   every specimen and search object below). A face separates the two
   factorizations if and only if in_w(n) is non-monomial and prim in_w(p)
   != prim in_w(q). The predecessor's sufficient half is the special case
   where the two primitive initial forms cannot coincide.

2. WHY IT NEVER FIRED BEFORE (property, part two; PR2 held, K2 shut). The
   accident count over the 18 objects is 0, and the reason printed at
   every one is part two's: q collinear at 17 (three terms against p's
   two) and p, q distinct binomials at the witness. The 231 published
   readings confirmed a theorem about these objects; they did not have
   to be read as evidence.

3. THE ACCIDENT IS REAL AND CARRIES A SECOND FULL-DIMENSION MECHANISM
   (property, the two frozen specimens confirmed by the counter and the
   face reader; PR3 held, K3 shut). The 10-term specimen is a 0/1
   collision with exactly two factorizations, one accident face, delta 1.
   The 14-term specimen is a 0/1 collision with exactly two
   factorizations, 10 faces, 0 separating, 2 accident faces, every exact
   proper face sampled: delta 2, where the old edge criterion reads 1
   and the exact law reads 2. So the parallel-edge reading at product
   dimension 2 is: delta = 1 exactly when Newt(n) has an edge parallel to
   an edge of Newt(p) or Newt(q) ALONG WHICH p and q read different
   primitive initial forms -- and without the clause it misgrades.

4. THE SHAPE IS NOT RARE IN ITS OWN BOX (observation, exact in the box;
   PR4 held, K4 shut). Over p = 1 + t, degrees at most 6, three layers:
   7 admissible n, 628 candidates, 628 distinct products, 628 genuine
   collisions each with exactly two factorizations and the shared-factor
   shape, every one carrying an accident face; 138 at delta 2 -- 287 and
   42 up to the box's two reflections -- and the old edge criterion
   misgrades exactly those 138, all at delta 2, the exact law none. The
   delta = 2 objects sit at term counts 14 (80 of them) and 18 (58), none
   at 12, so the wide box's lone full-dimension object stays alone at its
   own term count. At degrees at most 4 and 5 the same box prints 96/30 and 336/86 (one and
   five admissible n). Every count is about the box walked.

5. WITH n AND p ON ONE LINE THE MECHANISM HAS A CLOSED READING (property, derived
   after the first pilot print and then checked rather than predicted --
   the one reading this file did not carry in its slate). With n and p
   both univariate in t, n has non-monomial initial forms at w = (0, +1)
   and (0, -1) only and p reads itself there, so delta = 2 exactly when
   BOTH outermost y-layers of q are p up to a monomial; true at all 628
   objects. The slate froze D = 5 and the run
   was taken at 4, 5 and 6, the box being a price and not a hypothesis.

HOW THE PREDICTIONS AND KILLS LANDED. PR0 through PR4 held; PR5 was not
predicted and finding 4 is what that bought. K0 through K4 stayed shut.

RUN RECORD (this file, under memwatch.py at the 512MB default). 54/54
checks, 292.2 s wall (235.9 s of it the predecessor's wide-box
regeneration, 22.9 s the search), peak working set 131.5 MB, peak commit
124.4 MB. The --pilot flag skips the wide box and runs in about 55 s.
"""

import os
import sys
import time
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_menu_reach import (X, check, CHECKS, zfactors, count_from_core,
                                used_vars)
from explore_menu_faces import (exps, face_support, initial_form, primitive,
                                induced, weight_box, affine_rank)
from explore_descent_hunt import descent_sampled
from explore_descent26 import exact_proper_faces
from explore_descent26_why import (PILOT, WIDE, generate, grade,
                                   split_of_collision, nonmono, pmul,
                                   pnonneg, div_exact)

T, Y = X[0], X[1]
D = int(os.environ.get('FACE_D', '6'))


# ============================================================ the exact law
def prim_in(expr, gens, w):
    return primitive(initial_form(expr, gens, w), gens)


def exact_law(p, n, q, gens, w):
    return nonmono(n, gens, w) and prim_in(p, gens, w) != prim_in(q, gens, w)


def old_clause(p, n, q, gens, w):
    return nonmono(n, gens, w) and (nonmono(p, gens, w) or nonmono(q, gens, w))


def faces_of(facs, gens, radius):
    """{face support: one weight selecting it} over the weight sample."""
    pts = exps(sympy.expand(sympy.prod(facs)), gens)
    seen = {}
    for w in weight_box(len(gens), radius):
        seen.setdefault(frozenset(face_support(pts, w)), w)
    return pts, seen


def read_object(facs, gens, radius, p, n, q):
    """Face-by-face reading: (faces, separating, accident, disagreements,
    old-edge verdict, exact-law verdict)."""
    pts, seen = faces_of(facs[0], gens, radius)
    nfaces = sep = acc = bad = 0
    old_any = exact_any = False
    for f, w in seen.items():
        s = induced(facs[0], gens, w) != induced(facs[1], gens, w)
        law = exact_law(p, n, q, gens, w)
        old = old_clause(p, n, q, gens, w)
        nfaces += 1
        sep += s
        bad += (s != law)
        acc += (old and not s)
        old_any |= old
        exact_any |= law
    return nfaces, sep, acc, bad, old_any, exact_any


def q_reason(p, q, gens):
    """Part two's reason the accident cannot fire: q collinear, or p and q
    distinct primitive binomials."""
    eq = exps(q, gens)
    ep = exps(p, gens)
    if affine_rank(eq) <= 1 and len(eq) > len(ep):
        return "q collinear, %d terms against p's %d" % (len(eq), len(ep))
    if len(eq) == 2 and len(ep) == 2 and primitive(p, gens) != primitive(q, gens):
        return "p and q distinct binomials"
    return "NO REASON"


# ================================================= S0  the positive control
def stage0():
    print("\n=== S0  the controls ===")
    t = T
    F = sympy.expand((1 + t) * (1 + t**2 + t**4))
    cnt, facs = count_from_core(zfactors(F)[1], [t])
    print("  t = 6 cyclotomic identity: %d factorizations" % cnt)
    check("S0a the counter reproduces the t = 6 identity as two"
          " factorizations", cnt == 2)
    found, _ = generate(PILOT, "pilot {2..24}")
    objs, outobj = grade(found, "pilot {2..24}")
    d2 = [rs[0] for rs in objs.values() if rs[0]["delta"] >= 2]
    check("S0b the generator reproduces the published pilot box: 8 in-frame"
          " objects, 7 at delta 1 and 1 at delta 2", len(objs) == 8
          and len(d2) == 1)
    check("S0b the pilot delta = 2 object is the published witness",
          len(d2) == 1 and
          {tuple(sorted(d2[0]["A"])), tuple(sorted(d2[0]["B"]))} ==
          {(2, 3), (3, 4, 8, 9, 18, 24)})
    return objs


# ================================================= S1  the law at the 18
def stage1(objs, label):
    print("\n=== S1  the exact law at the published population [%s] ===" % label)
    tot = dict(faces=0, sep=0, acc=0, bad=0, objs=0, reasons=0)
    for key, rs in objs.items():
        r = rs[0]
        p, n, q, spect = split_of_collision(r)
        if p is None:
            print("  object %s x %s: no shared factor, unstated"
                  % (set(r["A"]), set(r["B"])))
            continue
        g = r["gens"]
        nf, sep, acc, bad, old_any, law_any = read_object(
            r["facs"], g, r["radius"], p, n, q)
        reason = q_reason(p, q, g)
        tot["faces"] += nf
        tot["sep"] += sep
        tot["acc"] += acc
        tot["bad"] += bad
        tot["objs"] += 1
        tot["reasons"] += (reason != "NO REASON")
        print("  %s x %s: faces %d, separating %d, accidents %d,"
              " disagreements %d, delta %d, old-edge %d, exact %d -- %s"
              % (set(r["A"]), set(r["B"]), nf, sep, acc, bad, r["delta"],
                 1 if old_any else r["dim"], 1 if law_any else r["dim"],
                 reason))
    print("  TOTAL: %d objects, %d faces, %d separating, %d accidents,"
          " %d disagreements, reason printed at %d"
          % (tot["objs"], tot["faces"], tot["sep"], tot["acc"], tot["bad"],
             tot["reasons"]))
    check("S1 [%s] the exact law agrees with separation at every face of"
          " every shared-factor object (K1)" % label, tot["bad"] == 0
          and tot["faces"] > 0)
    check("S1 [%s] the accident count over the population is zero (K2)"
          % label, tot["acc"] == 0)
    check("S1 [%s] part two's reason is printed at every object (K2)"
          % label, tot["reasons"] == tot["objs"])
    return tot


# ================================================= S2  the frozen specimens
def grade_poly(F, gens, label, verbose=True, core=None):
    """Counter, frame, exact faces, delta, both verdicts for a product F.

    core: the Z-irreducible factors of F where the caller already knows
    them (the search builds F as a product of factored pieces); otherwise
    F is factored here."""
    P = sympy.Poly(F, *gens)
    terms, maxc = len(P.monoms()), max(abs(c) for c in P.coeffs())
    if core is None:
        core = zfactors(F)[1]
    cnt, facs = count_from_core(core, gens)
    out = dict(terms=terms, maxc=maxc, cnt=cnt, facs=facs)
    if cnt < 2:
        return out
    dim, delta, w, radius = descent_sampled(facs[0], facs[1], gens)
    out.update(dim=dim, delta=delta, radius=radius)
    pts, seen = faces_of(facs[0], gens, radius)
    complete = True
    if dim == 2:
        exact = exact_proper_faces(pts)
        complete = not (exact - set(seen))
    out["complete"] = complete
    r = dict(facs=facs, gens=gens)
    p, n, q, spect = split_of_collision(r)
    out["shape"] = p is not None
    if p is None:
        return out
    nf, sep, acc, bad, old_any, law_any = read_object(facs, gens, radius,
                                                      p, n, q)
    out.update(faces=nf, sep=sep, acc=acc, bad=bad,
               old=1 if old_any else dim, exact=1 if law_any else dim,
               p=p, n=n, q=q)
    if verbose:
        print("  [%s] %d terms, max coefficient %d, %d factorizations"
              % (label, terms, maxc, cnt))
        for f in facs:
            print("     blocks: %s" % " | ".join(str(b) for b in f))
        print("     p = %s   n = %s   q = %s" % (p, n, q))
        print("     dim %d, delta %d (radius %d, exact faces all sampled: %s)"
              % (dim, delta, radius, complete))
        print("     faces %d, separating %d, accident faces %d,"
              " disagreements with the exact law %d" % (nf, sep, acc, bad))
        print("     old edge criterion reads delta %d; exact law reads %d"
              % (out["old"], out["exact"]))
    return out


SPEC10 = sympy.expand((1 + T**3) * ((1 + T) + Y * (1 + T + T**2)))
SPEC14 = sympy.expand((1 + T**3) * ((1 + T) + Y * (1 + T + T**2)
                                    + Y**2 * (1 + T)))


def stage2():
    print("\n=== S2  the two frozen specimens ===")
    g = [T, Y]
    a = grade_poly(SPEC10, g, "10-term")
    check("S2 the 10-term specimen is a 0/1 collision with exactly two"
          " factorizations (K3)", a["maxc"] == 1 and a["terms"] == 10
          and a["cnt"] == 2)
    check("S2 the 10-term specimen has the shared-factor shape and one"
          " accident face, and reads delta 1 (K3)",
          a.get("shape") and a.get("acc") == 1 and a.get("delta") == 1)
    check("S2 the 10-term specimen: exact law agrees at every face (K1)",
          a.get("bad") == 0 and a.get("complete"))
    b = grade_poly(SPEC14, g, "14-term")
    check("S2 the 14-term specimen is a 0/1 collision with exactly two"
          " factorizations (K3)", b["maxc"] == 1 and b["terms"] == 14
          and b["cnt"] == 2)
    check("S2 the 14-term specimen has two accident faces and NO separating"
          " proper face: delta 2 (K3)", b.get("shape") and b.get("acc") == 2
          and b.get("sep") == 0 and b.get("delta") == 2 and b.get("dim") == 2)
    check("S2 the 14-term specimen: the old edge criterion reads 1 and the"
          " exact law reads 2 (K3)", b.get("old") == 1 and b.get("exact") == 2)
    check("S2 the 14-term specimen: exact law agrees at every face, every"
          " exact proper face sampled (K1)", b.get("bad") == 0
          and b.get("complete"))
    return a, b


# ================================================= S3  the search
def upoly(mask):
    return {(i, 0): 1 for i in range(D + 1) if mask >> i & 1}


def is01(d):
    return all(c == 1 for c in d.values())


def to_expr2(d):
    e = 0
    for (i, j), c in d.items():
        e += c * T**i * Y**j
    return sympy.expand(e)


def canon(pts):
    pts = list(pts)
    lo = [min(p[i] for p in pts) for i in range(len(pts[0]))]
    return frozenset(tuple(a - b for a, b in zip(p, lo)) for p in pts)


def outer_layers_p(qd):
    """Both the lowest and the highest y-layer of q are t^a (1 + t)."""
    ys = sorted({j for _, j in qd})
    for j in (ys[0], ys[-1]):
        row = sorted(i for i, jj in qd if jj == j)
        if len(row) != 2 or row[1] - row[0] != 1:
            return False
    return True


def sym_key(pts):
    """The support up to translation and the two reflections t -> -t,
    y -> -y (the box's own symmetries)."""
    best = None
    for st in (1, -1):
        for sy in (1, -1):
            k = tuple(sorted(canon((st * a, sy * b) for a, b in pts)))
            if best is None or k < best:
                best = k
    return best


def stage3():
    print("\n=== S3  the search: p = 1 + t, degrees at most %d, layers 3 ===" % D)
    t0 = time.time()
    p = {(0, 0): 1, (1, 0): 1}
    ns = []
    for mask in range(1, 1 << (D + 1)):
        if not mask & 1:
            continue
        B = upoly(mask)
        n = div_exact(B, p)
        if n is None or pnonneg(n):
            continue
        ns.append((B, n))
    print("  admissible n: %d (0/1 B of degree <= %d with a negative"
          " quotient by 1 + t)" % (len(ns), D))
    layers_all = [upoly(m) for m in range(1, 1 << (D + 1))]
    cands = 0
    seen = {}
    results = []
    for B, n in ns:
        core_n = zfactors(to_expr2(n))[1]
        adm = [r for r in layers_all
               if is01(pmul(n, r)) and is01(pmul(B, r))]
        bottoms = [r for r in adm if len(r) == 2
                   and sorted(i for i, _ in r)[1] - sorted(i for i, _ in r)[0] == 1]
        adm0 = [None] + adm
        for q0 in bottoms:
            for q1 in adm0:
                for q2 in adm0:
                    if q1 is None and q2 is None:
                        continue
                    q = dict(q0)
                    for j, qj in ((1, q1), (2, q2)):
                        if qj is not None:
                            for (i, _), c in qj.items():
                                q[(i, j)] = c
                    if min(i for i, _ in q) != 0:
                        continue
                    # not divisible by 1 + t: some layer nonzero at t = -1
                    if all(sum((-1) ** i for (i, jj) in q if jj == j) == 0
                           for j in range(3)):
                        continue
                    cands += 1
                    Fd = pmul(B, q)
                    key = canon(Fd)
                    if key in seen:
                        continue
                    seen[key] = True
                    qe = to_expr2(q)
                    core = [1 + T] + core_n + zfactors(qe)[1]
                    res = grade_poly(to_expr2(Fd), [T, Y], "search",
                                     verbose=False, core=core)
                    if res["cnt"] >= 2:
                        res["B"], res["q"] = to_expr2(B), to_expr2(q)
                        res["outer"] = outer_layers_p(q)
                        res["sym"] = sym_key(Fd)
                        results.append(res)
    print("  candidates %d, distinct products %d, collisions %d   [%.1fs]"
          % (cands, len(seen), len(results), time.time() - t0))
    shaped = [r for r in results if r.get("shape")]
    unsh = len(results) - len(shaped)
    two = sum(1 for r in results if r["cnt"] == 2)
    withacc = [r for r in shaped if r["acc"] > 0]
    d2 = [r for r in shaped if r["delta"] == 2]
    mis = [r for r in shaped if r["old"] != r["delta"]]
    bad = sum(r["bad"] for r in shaped)
    inc = sum(1 for r in shaped if not r["complete"])
    print("  collisions with exactly two factorizations: %d; shared-factor"
          " shape %d, unstated %d" % (two, len(shaped), unsh))
    print("  shaped objects with an accident face: %d; at delta 2: %d;"
          " old edge criterion misgrades: %d (all at delta 2: %s)"
          % (len(withacc), len(d2), len(mis),
             all(r["delta"] == 2 for r in mis)))
    print("  exact-law disagreements: %d; objects with an unsampled exact"
          " face: %d" % (bad, inc))
    print("  up to the box's reflections: %d objects, %d at delta 2"
          % (len({r["sym"] for r in shaped}),
             len({r["sym"] for r in d2})))
    outer_ok = all((r["delta"] == 2) == r["outer"] for r in shaped)
    print("  delta = 2 exactly when both outer layers of q are t^a (1 + t):"
          " %s" % outer_ok)
    print("  the delta = 2 objects:")
    for r in d2:
        print("     B = %s   q = %s   terms %d   accidents %d   cnt %d"
              % (r["B"], r["q"], r["terms"], r["acc"], r["cnt"]))
    key14 = canon(exps(SPEC14, [T, Y]))
    hit = any(canon(exps(sympy.expand(r["B"] * r["q"]), [T, Y])) == key14
              for r in d2)
    check("S3 the search reaches the frozen 14-term specimen at delta 2",
          hit)
    check("S3 the search finds at least two delta = 2 objects (K4)",
          len(d2) >= 2)
    check("S3 the exact law agrees at every face of every shaped object"
          " found (K1)", bad == 0 and inc == 0)
    check("S3 every misgrade of the old edge criterion sits at delta 2,"
          " where every parallel face is an accident",
          all(r["delta"] == 2 and r["exact"] == 2 for r in mis))
    check("S3 with n and p both univariate, delta = 2 exactly when both outer layers"
          " of q are p up to a monomial (the property read off the first"
          " pilot print, checked rather than predicted)", outer_ok)
    return results


# ==================================================================== driver
def main():
    t0 = time.time()
    stage0()
    if any(not v for _, v in CHECKS):
        print("\nCONTROL FAILED -- nothing below is read.")
        return 1
    stage1_objs = None
    if "--pilot" not in sys.argv:
        found, _ = generate(WIDE, "wide {2..32}")
        stage1_objs, _ = grade(found, "wide {2..32}")
        stage1(stage1_objs, "wide {2..32}")
    stage2()
    stage3()
    ok = sum(1 for _, v in CHECKS if v)
    print("\n%d/%d checks passed in %.1fs" % (ok, len(CHECKS), time.time() - t0))
    return 0 if ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
