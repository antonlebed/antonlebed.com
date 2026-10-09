"""halfsize.py -- how many dimensions a polynomial with n terms can span
and still factor.

QUESTION. A seed's core is a 0/1 polynomial that factors over Z into
two non-monomial factors. Its NEWTON DIMENSION d is the dimension of
the convex hull of its exponent vectors. How large can d be against
the number of terms n? A nonnegative split multiplies term counts, so
factors of r and s terms give n = r s terms at dimension at most
r + s - 2 <= r s / 2. Does cancellation, the thing a seed has and a
nonnegative split lacks, ever buy more dimensions than that? And does
the answer need 0/1 coefficients?

THE ARGUMENT (written before the engine). Let f be a Laurent
polynomial over C with n terms and Newton polytope P of dimension d,
and suppose f = g h with neither factor a monomial. Claim: n >= 2d.
Suppose instead n < 2d, so d >= 2.
  (1) THE TRINOMIAL LEMMA, ANY COEFFICIENTS. alpha + beta u + gamma v
      with alpha beta gamma != 0 and u, v monomials whose exponent
      vectors are linearly independent is irreducible up to monomial
      units. A basis of the saturated lattice of their plane, extended
      to a basis of Z^N, is a unimodular change of monomial variables,
      an automorphism of the Laurent ring, and with the two vectors in
      Hermite form over it, it carries the trinomial to (alpha + beta X^rho) +
      gamma X^sigma Y^eta with rho, eta >= 1. Over the principal ideal
      domain R = C[X, 1/X] this is a polynomial in Y of degree eta with
      constant term alpha + beta X^rho, squarefree in characteristic 0,
      and a unit leading coefficient: Eisenstein at X - zeta for any
      root zeta of the constant term, so irreducible in R[Y] and, not
      being divisible by Y, in R[Y, 1/Y] up to units, which are
      monomials. A factorization in more variables has both Newton
      polytopes in translates of the trinomial's plane, so it is one in
      two variables up to monomials.
  (2) THE POLYTOPE HALF, the literature's: a d-polytope with fewer
      than 2d vertices is Minkowski indecomposable (Yost, Irreducible
      convex sets, Mathematika 38 (1991), Proposition 6, as restated in
      Przeslawski and Yost, More indecomposable polyhedra, Extracta
      Math. 31 (2016), arXiv:1607.00643), and a decomposable one with
      exactly 2d is combinatorially a prism over a (d - 1)-simplex
      (Przeslawski and Yost, Theorem 9 of the arXiv text; first in
      Kallay's 1979 thesis, unpublished). P has at most n < 2d
      vertices. Newt(g) + Newt(h) = P (Ostrowski), so both are
      homothets lambda P + t and mu P + t' with lambda + mu = 1, and
      neither factor is a monomial, so lambda, mu > 0.
  (3) THE CLEAN-TRIANGLE LEMMA. Mark the support points; the vertices
      are among them. A d-polytope, d >= 2, with fewer than 2d marked
      points has a triangular 2-face whose only marked points are its
      vertices (CLEAN). If P is a simplex, it has at most d - 2 extra
      points; each lies in the relative interior of one face and spoils
      only the triangles containing that face, at most d - 1 (those
      through an edge), while P has (d + 1) d (d - 1) / 6 triangles
      and (d + 1) d (d - 1) / 6 > (d - 2)(d - 1), since
      d^2 - 5d + 12 > 0.
      If P is not a simplex, some facet misses two vertices: were every
      facet to miss exactly one, conv(V - {v}) would be a facet for
      every vertex v, so no vertex lies in the affine hull of the
      others and V is affinely independent. That facet is a
      (d - 1)-polytope with at most n - 2 < 2(d - 1) marked points,
      its vertices among them, and induction ends at a polygon with at
      most three marked points, a clean triangle. A 2-face of a face is
      a 2-face of P.
  (4) CLOSE. Let T be a clean triangle of P and w a weight whose face
      is T. Initial forms multiply: f_T = g_(lambda T) h_(mu T). The
      left side is a trinomial with non-collinear exponents, the
      right a product of two polynomials with triangular Newton
      polygons, neither a monomial, against (1). So n >= 2d.
THE HALF-SIZE LAW: a polynomial over C with n terms that factors into
two non-monomial factors has Newton dimension at most floor(n/2). No
step reads a coefficient beyond its being nonzero. For a seed of size
n (a 0/1 core, whose negative Z-irreducible factor is proper) the
dimension is at most floor(n/2).
TIGHTNESS, by construction. With T3 = 1 - x + x^2, the product
T3 (A(x) + sum_(i<=k) y_i B_i(x)), each T3 A and T3 B_i one of 1 + x^3
and 1 + x^2 + x^4, is 0/1 with n = sum of the parts' term counts at
dimension k + 1: all binomials give n = 2k + 2 at n/2, one trinomial
n = 2k + 3 at floor(n/2), for every n >= 2. At size 5 that is the
menu {2, 16, 6, 24, 96}, core 1 + x^3 + y (1 + x^2 + x^4).

DESIGN. collide.py supplies the menus' exponent vectors and Z-factors.
Exponents here are tuples, polynomials sparse dictionaries; the
dimension is exact rational elimination.
  CONTROL: the clean-triangle detector, a linear program asking for a
     weight exact on three marked points and strictly lower on every
     other, run where the answer is known: the unit cube (no triangle),
     a tetrahedron with one edge's midpoint marked (2 of 4 clean), the
     square pyramid (4 triangles, all clean). And the trinomial lemma's
     edges: 1 + x^4 + x^5, collinear, reducible; 1 + x^2 + y^2, whose
     triangle is twice a lattice triangle, irreducible.
  TRINOMIAL: seeded random trinomials in three variables, exponents in
     0..4, coefficients in +-1..+-3, non-collinear, factored over Q,
     which probes (1) through its factors over Q only.
  TRIANGLE: seeded random marked sets in {0..3}^d for d = 3, 4, 5, of
     n points with d + 1 <= n <= 2d - 1 spanning d dimensions; the
     detector must find a clean triangle in each.
  PRODUCTS: seeded random products g h, both non-monomial, from two
     shapes: g one-variable of at least two terms, coefficients drawn
     from {-1, 0, 1} at degree 1..3, against h = B_0(x) + sum y_i
     B_i(x), k = 1..4, each B_i of at least two terms, drawn to degree
     <= 4 with coefficients in -2..2 -- the shape where
     cancellation builds the tight family -- and g, h generic sparse
     in four variables. Each product's term count n and dimension d.
  TIGHT: the construction at n = 4..11: terms, dimension, and a
     negative Z-irreducible factor.
  CENSUS: every menu of sizes 5, 6 and 7 from {2..16}; the core's
     dimension, and every core with 2d > n factored.

PREDICTIONS (fixed before the engine).
  P1 CONTROL: cube 0 clean triangles, tetrahedron with midpoint 2,
     square pyramid 4; 1 + x^4 + x^5 reducible, 1 + x^2 + y^2
     irreducible.
  P2 TRINOMIAL: 0 reducible.
  P3 TRIANGLE: a clean triangle in every configuration.
  P4 PRODUCTS: no product with 2d > n. How many reach 2d = n WITH
     cancellation (n below the product of the factors' term counts)
     is the measurement. [Ruled on audit: the parenthesis counts merged
     terms, cancelling or not; the findings say merged.]
  P5 TIGHT: at every n, n terms, all 1, dimension floor(n/2), and a
     negative Z-irreducible factor.
  P6 CENSUS: 0 reducible cores with 2d > n.

KILLS. P1 is the positive control: if it misses, nothing after it is
read. A reducible non-collinear trinomial kills (1); a configuration
with no clean triangle kills (3); a product or a menu core with
2d > n kills the law, and names (2) if its face polynomials are
clean trinomials. A tight member off its dimension or without a
negative factor kills the tightness claim.

FINDINGS. Every prediction held and no kill fired.
  P1 the detector reads the cube 0, the tetrahedron with a midpoint 2,
     the square pyramid 4; 1 + x^4 + x^5 has 2 factors and 1 + x^2 +
     y^2 one.
  P2 300 non-collinear trinomials, 0 reducible.
  P3 150 configurations at each of d = 3, 4, 5, every one with a
     clean triangle.
  P4 60,000 products, 0 with 2d > n; 15,694 at 2d = n, 96 of them
     with merged terms, the highest at n = 8, d = 4. Merging reaches
     the bound and never passes it.
  P5 n = 4..11 each at n terms and dimension floor(n/2) with a
     negative factor; the menu {2, 16, 6, 24, 96} at dimension 2, a
     seed.
  P6 sizes 5, 6, 7 from {2..16}: 3,003, 5,005 and 6,435 menus, of
     which 2,929, 4,174 and 5,923 sit above floor(n/2); each was
     factored and none is reducible.
Tier: the half-size law is a theorem, proved above with the polytope
half cited; this file is its falsification attempt, toy-scale.

RUN RECORD. 7 of 7 checks, 28 s, peak commit 94 MB. The census first
ran over {2..20} (11,628, 27,132 and 50,388 menus, 0 reducible above
the law, 193 s) and was cut to {2..16} for the gate.
"""

import os
import random
import sys
import time
from fractions import Fraction
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from sympy import Poly, symbols  # noqa: E402
from scipy.optimize import linprog  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from collide import vec, zfactors, negative, menu_poly  # noqa: E402

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tag = "ok  " if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))


def control(name, ok, detail=""):
    check(name, ok, detail)
    if not ok:
        print("  control failed: run stopped")
        raise SystemExit(1)


def section(title):
    print()
    print(title)


# ------------------------------------------------------------ geometry

def dim(points):
    """Affine dimension of integer points, exact."""
    pts = list(points)
    if len(pts) < 2:
        return 0
    base = pts[0]
    rows = [[Fraction(a - b) for a, b in zip(p, base)] for p in pts[1:]]
    r, cols = 0, len(rows[0])
    for c in range(cols):
        piv = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                q = rows[i][c] / rows[r][c]
                rows[i] = [a - q * b for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def clean_triangles(points, stop=False):
    """Triples of marked points forming a 2-face that holds no other
    marked point: some weight w is equal on the three and at least one
    lower on every other point (feasibility, HiGHS)."""
    pts = list(points)
    d = len(pts[0])
    found = []
    for tri in combinations(range(len(pts)), 3):
        if dim([pts[i] for i in tri]) != 2:
            continue
        a0 = pts[tri[0]]
        a_eq = [[p - q for p, q in zip(pts[i], a0)] for i in tri[1:]]
        b_eq = [0, 0]
        a_ub = [[p - q for p, q in zip(pts[j], a0)]
                for j in range(len(pts)) if j not in tri]
        b_ub = [-1] * len(a_ub)
        res = linprog([0] * d, A_ub=a_ub or None, b_ub=b_ub or None,
                      A_eq=a_eq, b_eq=b_eq, bounds=[(None, None)] * d,
                      method="highs")
        if res.status == 0:
            found.append(tri)
            if stop:
                break
    return found


# ------------------------------------------------------------ polynomials

def pmul(f, g):
    out = {}
    for e, c in f.items():
        for e2, c2 in g.items():
            k = tuple(a + b for a, b in zip(e, e2))
            out[k] = out.get(k, 0) + c * c2
    return {k: c for k, c in out.items() if c}


def factors_q(f, gens):
    """Non-monomial Q-irreducible factors of a sparse dict polynomial."""
    _, fl = Poly.from_dict(f, *gens).factor_list()
    return [(q, e) for q, e in fl if len(q.terms()) > 1]


# ------------------------------------------------------------ sections

def section_control():
    section("CONTROL -- the detector and the lemma's edges")
    cube = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    tet = [(0, 0, 0), (2, 0, 0), (0, 2, 0), (0, 0, 2), (1, 0, 0)]
    pyr = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1)]
    c1, c2, c3 = (len(clean_triangles(p)) for p in (cube, tet, pyr))
    print(f"    clean triangles: cube {c1}, tetrahedron with midpoint "
          f"{c2}, square pyramid {c3}")
    control("P1 cube 0, tetrahedron 2, pyramid 4",
            (c1, c2, c3) == (0, 2, 4))
    x, y = symbols("x y")
    red = factors_q({(0,): 1, (4,): 1, (5,): 1}, [x])
    irr = factors_q({(0, 0): 1, (2, 0): 1, (0, 2): 1}, [x, y])
    print(f"    1 + x^4 + x^5: {len(red)} factors; 1 + x^2 + y^2: "
          f"{len(irr)} factor")
    control("P1 collinear reducible, doubled triangle irreducible",
          len(red) == 2 and len(irr) == 1)


def section_trinomial(samples=300, seed=1):
    section("TRINOMIAL -- non-collinear trinomials, any coefficients")
    rng = random.Random(seed)
    gens = symbols("x0:3")
    done = red = 0
    while done < samples:
        u = tuple(rng.randint(0, 4) for _ in range(3))
        v = tuple(rng.randint(0, 4) for _ in range(3))
        z = (0, 0, 0)
        if dim([z, u, v]) != 2:
            continue
        cs = [rng.choice([-3, -2, -1, 1, 2, 3]) for _ in range(3)]
        f = {z: cs[0], u: cs[1], v: cs[2]}
        done += 1
        fl = factors_q(f, gens)
        if sum(e for _, e in fl) > 1:
            red += 1
            print(f"    REDUCIBLE: {f}")
    print(f"    {done} trinomials, {red} reducible")
    check("P2 no non-collinear trinomial factors", red == 0)


def section_triangle(per_d=150, seed=2):
    section("TRIANGLE -- a clean triangle below 2d marked points")
    rng = random.Random(seed)
    total = miss = 0
    for d in (3, 4, 5):
        got = 0
        while got < per_d:
            n = rng.randint(d + 1, 2 * d - 1)
            pts = set()
            while len(pts) < n:
                pts.add(tuple(rng.randint(0, 3) for _ in range(d)))
            pts = sorted(pts)
            if dim(pts) != d:
                continue
            got += 1
            if not clean_triangles(pts, stop=True):
                miss += 1
                print(f"    NO CLEAN TRIANGLE: {pts}")
        total += got
        print(f"    d = {d}: {got} configurations")
    print(f"    {total} configurations, {miss} without a clean triangle")
    check("P3 every configuration has a clean triangle", miss == 0)


def rand_uni(rng, deg_lo, deg_hi, coeffs):
    while True:
        deg = rng.randint(deg_lo, deg_hi)
        f = {i: rng.choice(coeffs) for i in range(deg + 1)}
        f = {i: c for i, c in f.items() if c}
        if len(f) >= 2:
            return f


def section_products(samples=60000, seed=3):
    section("PRODUCTS -- terms against dimension, with merged terms")
    rng = random.Random(seed)
    over = tight = tight_cancel = 0
    best = None
    for s in range(samples):
        if s % 2 == 0:
            k = rng.randint(1, 4)
            r = k + 1
            g1 = rand_uni(rng, 1, 3, [-1, 0, 1])
            g = {(i,) + (0,) * k: c for i, c in g1.items()}
            h = {}
            for j in range(k + 1):
                b = rand_uni(rng, 0, 4, [-2, -1, 0, 1, 2]) \
                    if j else rand_uni(rng, 1, 4, [-2, -1, 0, 1, 2])
                for i, c in b.items():
                    e = [0] * r
                    e[0] = i
                    if j:
                        e[j] = 1
                    h[tuple(e)] = c
        else:
            r = 4

            def sparse():
                while True:
                    t = rng.randint(2, 4)
                    f = {tuple(rng.randint(0, 2) for _ in range(r)):
                         rng.choice([-2, -1, 1, 2]) for _ in range(t)}
                    if len(f) >= 2:
                        return f
            g, h = sparse(), sparse()
        f = pmul(g, h)
        n, d = len(f), dim(f.keys())
        if 2 * d > n:
            over += 1
            print(f"    OVER: n = {n}, d = {d}, g = {g}, h = {h}")
        if 2 * d == n:
            tight += 1
            if n < len(g) * len(h):
                tight_cancel += 1
                if best is None or d > best[1]:
                    best = (n, d, g, h)
    print(f"    {samples} products, {over} with 2d > n, {tight} at 2d = n,"
          f" {tight_cancel} of them with merged terms")
    if best:
        print(f"    highest merging tight product: n = {best[0]}, "
              f"d = {best[1]}")
    check("P4 no product with 2d > n", over == 0)


def tight_member(n):
    """T3 (A + sum y_i B_i) with T3 A, T3 B_i in {1 + x^3, 1 + x^2 + x^4}:
    returns the product as a dict over (x, y_1..y_k)."""
    k = n // 2 - 1
    parts = [{0: 1, 3: 1}] * (k + 1)
    if n % 2:
        parts = [{0: 1, 2: 1, 4: 1}] + parts[1:]
    r = k + 1
    f = {}
    for j, p in enumerate(parts):
        for i, c in p.items():
            e = [0] * r
            e[0] = i
            if j:
                e[j] = 1
            f[tuple(e)] = c
    return f


def section_tight():
    section("TIGHT -- the bound attained at every n")
    ok = True
    for n in range(4, 12):
        f = tight_member(n)
        gens = symbols(f"t0:{len(next(iter(f)))}")
        fl = factors_q(f, gens)
        neg = any(any(c < 0 for c in q.coeffs()) for q, _ in fl)
        d = dim(f.keys())
        good = (len(f) == n and set(f.values()) == {1}
                and d == n // 2 and neg)
        ok &= good
        print(f"    n = {n}: terms {len(f)}, dimension {d}, "
              f"{sum(e for _, e in fl)} factors, negative factor {neg}")
    menu = (2, 16, 6, 24, 96)
    vs = [vec(m) for m in menu]
    d5 = dim(vs)
    neg5 = any(negative(q) for q in zfactors(menu_poly(menu)))
    print(f"    menu {menu}: dimension {d5}, seed {neg5}")
    check("P5 every member tight, a seed at every n", ok and d5 == 2
          and neg5)


def section_census(box=16, sizes=(5, 6, 7)):
    section(f"CENSUS -- every menu of sizes {sizes} from {{2..{box}}}")
    vecs = {m: vec(m) for m in range(2, box + 1)}
    bad = 0
    for n in sizes:
        menus = over = 0
        by_d = {}
        for menu in combinations(range(2, box + 1), n):
            menus += 1
            d = dim([vecs[m] for m in menu])
            by_d[d] = by_d.get(d, 0) + 1
            if 2 * d > n:
                over += 1
                if len(zfactors(menu_poly(menu))) > 1:
                    bad += 1
                    print(f"    REDUCIBLE above the law: {menu}")
        print(f"    size {n}: {menus} menus, dimensions "
              f"{dict(sorted(by_d.items()))}, {over} above floor(n/2) "
              f"factored")
    check("P6 no reducible core above floor(n/2)", bad == 0)


def main():
    t0 = time.time()
    section_control()
    section_trinomial()
    section_triangle()
    section_products()
    section_tight()
    section_census()
    print()
    n, ok = len(CHECKS), sum(CHECKS)
    print(f"{ok} of {n} checks pass  [{time.time() - t0:.1f} s]")
    return 0 if ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
