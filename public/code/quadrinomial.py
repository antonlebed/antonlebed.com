"""quadrinomial.py -- a four-term 0/1 polynomial that factors into two
non-monomial factors carries a binomial factor, and off a line every
factor vanishes on roots of unity.

QUESTION. The torsion split asks whether a seed's negative factor can avoid
every point of roots of unity. At size 3 the answer is decided on a line by
Ljunggren's theorem (Math. Scand. 8 (1960) 65-70). What does a four-term 0/1
polynomial P look like when it factors over Z, in any number of variables, and
can a non-collinear four-member seed be free?

THE ARGUMENT (written before the engine). Let P = m_1 + m_2 + m_3 + m_4,
monomials with exponent vectors e_1..e_4, and P = g h over Z with
neither factor a monomial.
  (0) AFFINE DIMENSION. At dimension 3 the half-size law (halfsize.py)
      forbids a factorization, 4 < 2 * 3. So P lies on a line or in a
      plane, and the frame's unimodular map puts it in one or two
      variables.
  (1) THE PAIRING LEMMA. Four complex numbers of modulus 1 summing to 0
      are two antipodal pairs. If z_1 + z_2 = 0 then z_3 + z_4 = 0.
      Otherwise s = z_1 + z_2 != 0, and the unordered pair of unit
      numbers with sum s is unique (the circle meets the perpendicular
      to s through s/2 in two points), so {z_3, z_4} = {-z_1, -z_2}. So
      at any root of P on the unit torus some pairing {i, j}, {k, l} has
      m_i / m_j = -1 = m_k / m_l there.
  (2) HAJOS'S BOUND. A nonzero root z of a T-term polynomial sum c_a
      x^(n_a) has multiplicity at most T - 1: at multiplicity T the
      operators (x d/dx)^r, r = 0..T - 1, all kill it, a Vandermonde
      system in the distinct n_a with the nonzero unknowns c_a z^(n_a).
  (3) MILLS'S THEOREM (Math. Scand. 57 (1985) 44-50, Theorem 2, read at
      source): for F = x^n + e_1 x^m + e_2 x^p + e_3, n > m > p > 0,
      e_i = +-1, the part B of F whose roots are no roots of unity is
      irreducible except for four forms, each with e_3 = -1. So an
      all-plus quadrinomial's non-cyclotomic part is 1 or irreducible.
  (4) THE LINE. P = 1 + x^a + x^b + x^c reducible has two non-unit
      factors, so by (3) a cyclotomic one, and a root of unity zeta
      with P(zeta) = 0. By (1) P = x^i (1 + x^s) + x^k (1 + x^t), s, t >
      0, with zeta^s = zeta^t = -1, so s and t have one 2-adic
      valuation, and with d = gcd(s, t) both s/d and t/d are odd: 1 +
      x^d divides both halves.
  (5) THE PLANE. Choose coordinates in which neither g's nor h's
      support lies on a horizontal line. For K beyond the x-width of
      P's support, y -> x^K is injective on it and on g's and h's, so
      P_K = g_K h_K is an all-plus quadrinomial with two non-monomial
      factors, and by (3) one of them has only roots of unity for roots.
      One factor, say g, does so for infinitely many K. The degree of
      g_K past its lowest term grows with K, so by (2) g_K has
      unboundedly many distinct roots zeta, each a zero of P at the
      unit-torus point (zeta, zeta^K). For a pairing whose differences
      u = e_i - e_j and u' = e_k - e_l are not parallel, zeta^A = -1 =
      zeta^C with A = u . (1, K), C = u' . (1, K) makes zeta^(2 gcd(A,
      C)) = 1, and gcd(A, C) divides det(u, u') != 0: such a pairing
      holds at no more than 2 |det| roots, whatever K. So for large K
      some root sits on a pairing with parallel differences, u = s w
      and u' = t w along one primitive w, and omega = zeta^(w . (1, K))
      has omega^s = omega^t = -1. As in (4): P = m_j (1 + w^s) + m_l (1
      + w^t) with s/d and t/d odd, d = gcd(s, t).
THE COFACTOR THEOREM: a four-term 0/1 polynomial that factors over Z
into two non-monomial factors is divisible by 1 + u for a monomial u; in
fact P = m (1 + W)(q_s'(W) + v q_t'(W)) with W = w^d, s' = s/d and
t' = t/d odd, v = m_l / m_j and q_n(W) = 1 - W + ... + W^(n - 1).
  (6) THE SIZE-4 CLOSURE. Off a line v is independent of W. The factors
      of 1 + W and of c = gcd(q_s', q_t') are cyclotomic in W and vanish
      at roots of unity. If s' = t' the rest is 1 + v, likewise. If
      s' != t', R = a(W) + v b(W) with a = q_s'/c and b = q_t'/c
      coprime, squarefree, not both constant. Write v = x^i y^j, j >= 1,
      in coordinates with W = x^d. If a is not constant, R is Eisenstein
      in y at any prime of Q[x, 1/x] dividing a once (a has constant term
      1, so x does not divide it); if a = 1, then y^-j R is Eisenstein in
      1/y at a prime factor of b. R is primitive, so Z-irreducible, and
      at the torus point x = 1, y^j = -1, where W = 1 and v = -1, R =
      a(1) - b(1) = (1 - 1)/c(1) = 0, c(1) dividing q_s'(1) = 1. So
      EVERY Z-FACTOR OF A REDUCIBLE NON-COLLINEAR FOUR-TERM 0/1
      POLYNOMIAL IS TORSION-ROOTED, and a four-member seed off a line is
      rooted. On a line v can be a power of W and the character is gone:
      1 + x^3 + x^4 + x^5 = (1 + x)(1 - x + x^2 + x^4) is free.
  (7) TWO FREE SEEDS AT SIZE 6. {2, 3, 4, 8, 16, 24} has core
      (1 + x)[x (1 + x^2) + y (1 - x + x^2)], the bracket linear in y
      with coprime coefficients, so irreducible, and negative. At a
      torus point |y| = 1 forces |1 + x^2| = |1 - x + x^2| with |x| = 1,
      i.e. |2 cos theta| = |2 cos theta - 1|, so cos theta = 1/4 and x is
      a root of 2x^2 - x + 2, no algebraic integer, no root of unity. So
      the bracket meets no torsion point and the seed is free, mixed
      beside the rooted 1 + x, at size 6; its mirror {2, 3, 6, 12, 16,
      24} likewise.

DESIGN. Configurations are sets of exponent vectors, factored with
sympy after collide.py's frame is applied by hand (min subtracted).
  CONTROL: (1 + x)(1 + y) reducible with a binomial factor; 1 + x + y
     irreducible; Mills's four forms at r = 1 each with two
     non-cyclotomic factors.
  PAIRING: every 4-tuple of 24th roots of unity summing to 0, each read
     for an antipodal pairing.
  PLANE: every 4-subset of [0, 4]^2 with least coordinates 0,
     non-collinear: reducible count; every reducible one read for the
     theorem's shape (a pairing along one primitive w with s/d, t/d
     odd) and a binomial Z-factor; every Z-factor searched for a zero
     at a pair of N-th roots of unity, N <= 24.
  RANK3: every 4-subset of [0, 2]^3 with least coordinates 0 at affine
     dimension 3: reducible count.
  LINE: every 1 + x^a + x^b + x^c, c <= 40: reducible count, shape and
     binomial factor, non-cyclotomic factors at most one, seeds by
     torsion class; 1 + x^3 + x^4 + x^5 among the free.
  FREE6: the two menus' cores factored; the bracket negative and
     irreducible; no zero at a pair of N-th roots, N <= 60.

PREDICTIONS (fixed before the engine).
  P1 CONTROL: as named.
  P2 PAIRING: every vanishing tuple pairs antipodally.
  P3 PLANE: every reducible configuration has the shape and a binomial
     factor, and every Z-factor a torsion zero at N <= 24.
  P4 RANK3: 0 reducible.
  P5 LINE: every reducible quadrinomial has the shape and a binomial
     factor; at most one non-cyclotomic factor each; free seeds exist,
     1 + x^3 + x^4 + x^5 among them.
  P6 FREE6: both cores (1 + x) times a negative irreducible bracket
     with no torsion zero at N <= 60.

KILLS. P1 is the positive control: if it misses, nothing after it is
read. A vanishing tuple without an antipodal pairing kills (1). A
reducible configuration without the shape kills (4) or (5); a factor
with no torsion zero off a line is read before it kills (6), since the
search is bounded, and names the order it needs. A reducible rank-3
configuration kills (0). Two non-cyclotomic factors in a line
quadrinomial contradicts the cited theorem.

FINDINGS. Every prediction held and no kill fired.
  P1 (1 + x)(1 + y) has 2 factors, both binomials; 1 + x + y has 1;
     Mills's four forms at r = 1 have 2 non-cyclotomic factors each.
  P2 69 vanishing sums of four 24th roots of unity, the first root 1
     and the other three an ordered triple, every one two antipodal
     pairs.
  P3 4,764 non-collinear configurations in [0, 4]^2, 296 reducible, 149
     of them seeds; every reducible one has the shape and a binomial
     factor, and every factor a torsion zero, the largest order needed
     8.
  P4 8,424 configurations of [0, 2]^3 at dimension 3, 0 reducible.
  P5 9,880 quadrinomials to degree 40, 4,306 reducible, every one with
     the shape and a binomial factor, at most one non-cyclotomic
     factor in any; seeds 366 rooted, 3,926 mixed, 0 free outright, 1 +
     x^3 + x^4 + x^5 among the free. None can be free outright: Mills
     gives every reducible one a cyclotomic factor.
  P6 {2, 3, 4, 8, 16, 24} factors as x0 + 1 times x0^3 + x0^2 x1 - x0
     x1 + x0 + x1, and {2, 3, 6, 12, 16, 24} as x0 + 1 times x0^3 +
     x0^2 x1 - x0^2 + x0 + x1; each has one negative factor and no
     torsion zero at N <= 60: free, and mixed beside the rooted
     x0 + 1.
Tiers: the cofactor theorem and the size-4 closure are theorems,
proved above with Mills's theorem cited; the two free seeds at size
6 are a theorem by exhibit, proved by hand; the boxes are their falsification
attempt, toy-scale.

RUN RECORD. 9 of 9 checks, 11.4 s, peak commit 51 MB. The first run
missed P1 at 8 of 9 on a transcription error in the control, Mills's
second form typed with x^2 for x; corrected against the paper, every
other print unchanged. An audit then restored MIXED to mean a free seed
with any torsion-rooted factor; the line's split moved from 1,136
mixed and 2,790 free outright to 3,926 and 0.
"""

import cmath
import os
import sys
import time
from itertools import combinations, product
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from sympy import Poly, symbols  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from collide import menu_poly, vec, zfactors, negative  # noqa: E402

CHECKS = []
X, Y, Z = symbols("x y z")


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


def poly(points, gens):
    return Poly.from_dict({p: 1 for p in points}, *gens)


def factors(p):
    """Non-monomial Z-irreducible factors with multiplicity, normed."""
    _, fl = p.factor_list()
    out = []
    for q, e in fl:
        if len(q.terms()) < 2:
            continue
        if q.LC() < 0:
            q = -q
        out += [q] * e
    return out


def dim(points):
    base = points[0]
    rows = [[a - b for a, b in zip(p, base)] for p in points[1:]]
    from sympy import Matrix
    return Matrix(rows).rank()


def content(u):
    g = 0
    for a in u:
        g = gcd(g, abs(a))
    return g


def shape(points):
    """The theorem's shape: a pairing {i, j}, {k, l} whose differences are
    s w and t w along one primitive w with s/d and t/d odd."""
    for (i, j), (k, l) in (((0, 1), (2, 3)), ((0, 2), (1, 3)),
                           ((0, 3), (1, 2))):
        u = [a - b for a, b in zip(points[i], points[j])]
        v = [a - b for a, b in zip(points[k], points[l])]
        s, t = content(u), content(v)
        wu = tuple(a // s for a in u)
        wv = tuple(a // t for a in v)
        if wu != wv and wu != tuple(-a for a in wv):
            continue
        d = gcd(s, t)
        if (s // d) % 2 and (t // d) % 2:
            return True
    return False


def torsion_zero(q, top):
    """Least N <= top with q vanishing at a point of N-th roots of unity,
    else None (numerical, |q| < 1e-9)."""
    terms = q.terms()
    nv = len(terms[0][0])
    for n in range(1, top + 1):
        roots = [cmath.exp(2j * cmath.pi * k / n) for k in range(n)]
        for pt in product(range(n), repeat=nv):
            val = 0
            for e, c in terms:
                z = 1
                for k, ex in zip(pt, e):
                    z *= roots[(k * ex) % n]
                val += int(c) * z
            if abs(val) < 1e-9:
                return n
    return None


def section_control():
    section("CONTROL")
    a = factors(poly([(0, 0), (1, 0), (0, 1), (1, 1)], (X, Y)))
    b = factors(poly([(0, 0), (1, 0), (0, 1)], (X, Y)))
    print(f"    (1 + x)(1 + y): {len(a)} factors; 1 + x + y: {len(b)}")
    mills = [Poly(X ** 8 + X ** 7 + X - 1, X), Poly(X ** 8 - X ** 7 -
             X - 1, X), Poly(X ** 8 + X ** 4 + X ** 2 - 1, X),
             Poly(X ** 8 - X ** 6 - X ** 4 - 1, X)]
    noncyc = [sum(1 for q in factors(m) if not q.is_cyclotomic)
              for m in mills]
    print(f"    Mills's four forms at r = 1: non-cyclotomic factors "
          f"{noncyc}")
    control("P1 controls", len(a) == 2 and len(b) == 1
          and all(len(q.terms()) == 2 for q in a) and noncyc == [2] * 4)


def section_pairing(n=24):
    section(f"PAIRING -- vanishing sums of four {n}th roots of unity")
    roots = [cmath.exp(2j * cmath.pi * k / n) for k in range(n)]
    zero = bad = 0
    for t in product(range(n), repeat=3):
        z = 1 + sum(roots[k] for k in t)
        if abs(z) > 1e-9:
            continue
        zero += 1
        ks = (0,) + t
        if not any((ks[i] - ks[j]) % n == n // 2 and
                   (ks[k] - ks[l]) % n == n // 2
                   for (i, j), (k, l) in (((0, 1), (2, 3)), ((0, 2), (1, 3)),
                                          ((0, 3), (1, 2)))):
            bad += 1
    print(f"    {zero} vanishing tuples with first root 1, {bad} unpaired")
    check("P2 every vanishing tuple pairs antipodally", zero and bad == 0)


def section_plane(box=4, top=24):
    section(f"PLANE -- every 4-subset of [0, {box}]^2, least coordinates 0")
    grid = [(a, b) for a in range(box + 1) for b in range(box + 1)]
    configs = red = seeds = noshape = nobin = unrooted = 0
    need = 0
    for pts in combinations(grid, 4):
        if min(p[0] for p in pts) or min(p[1] for p in pts):
            continue
        if dim(list(pts)) != 2:
            continue
        configs += 1
        fs = factors(poly(pts, (X, Y)))
        if len(fs) < 2:
            continue
        red += 1
        seeds += any(any(c < 0 for c in q.coeffs()) for q in fs)
        if not shape(list(pts)):
            noshape += 1
            print(f"    NO SHAPE: {pts}")
        if not any(len(q.terms()) == 2 for q in fs):
            nobin += 1
        for q in fs:
            n = torsion_zero(q, top)
            if n is None:
                unrooted += 1
                print(f"    NO TORSION ZERO <= {top}: {q.as_expr()} in {pts}")
            else:
                need = max(need, n)
    print(f"    {configs} configurations, {red} reducible, {seeds} seeds; "
          f"without the shape {noshape}, without a binomial factor {nobin},"
          f" factors without a torsion zero {unrooted}; largest N needed "
          f"{need}")
    check("P3 every reducible one has the shape and a binomial factor",
          red and noshape == 0 and nobin == 0)
    check("P3 every factor has a torsion zero", unrooted == 0)


def section_rank3(box=2):
    section(f"RANK3 -- every 4-subset of [0, {box}]^3 at dimension 3")
    grid = list(product(range(box + 1), repeat=3))
    configs = red = 0
    for pts in combinations(grid, 4):
        if any(min(p[i] for p in pts) for i in range(3)):
            continue
        if dim(list(pts)) != 3:
            continue
        configs += 1
        red += len(factors(poly(pts, (X, Y, Z)))) > 1
    print(f"    {configs} configurations, {red} reducible")
    check("P4 dimension 3 is irreducible", configs and red == 0)


def section_line(top=40):
    section(f"LINE -- 1 + x^a + x^b + x^c, c <= {top}")
    total = red = noshape = nobin = worst = 0
    tally = {"rooted": 0, "mixed": 0, "outright": 0}
    free_names = set()
    for c in range(3, top + 1):
        for a, b in combinations(range(1, c), 2):
            total += 1
            fs = factors(poly([(0,), (a,), (b,), (c,)], (X,)))
            if len(fs) < 2:
                continue
            red += 1
            if not shape([(0,), (a,), (b,), (c,)]):
                noshape += 1
            if not any(len(q.terms()) == 2 for q in fs):
                nobin += 1
            worst = max(worst, sum(1 for q in fs if not q.is_cyclotomic))
            neg = [q.is_cyclotomic for q in fs
                   if any(k < 0 for k in q.coeffs())]
            if neg:
                if all(neg):
                    tally["rooted"] += 1
                else:
                    rooted = any(q.is_cyclotomic for q in fs)
                    tally["mixed" if rooted else "outright"] += 1
                    free_names.add((a, b, c))
    print(f"    {total} quadrinomials, {red} reducible; without the shape "
          f"{noshape}, without a binomial factor {nobin}; most "
          f"non-cyclotomic factors {worst}; seeds rooted {tally['rooted']},"
          f" mixed {tally['mixed']}, free outright {tally['outright']}")
    check("P5 every reducible one has the shape and a binomial factor",
          red and noshape == 0 and nobin == 0)
    check("P5 Mills: at most one non-cyclotomic factor", worst <= 1)
    check("P5 1 + x^3 + x^4 + x^5 is free", (3, 4, 5) in free_names)


def section_free6(top=60):
    section("FREE6 -- two free seeds at size 6")
    ok = True
    for menu in ((2, 3, 4, 8, 16, 24), (2, 3, 6, 12, 16, 24)):
        fs = zfactors(menu_poly(menu))
        neg = [f for f in fs if negative(f)]
        idx = [i for i, e in enumerate(zip(*[vec(m) for m in menu]))
               if any(e)]
        qs = []
        for f in neg:
            d = {tuple(e[i] for i in idx): c for e, c in f.d.items()}
            lo = [min(e[k] for e in d) for k in range(len(idx))]
            qs.append(Poly.from_dict({tuple(a - b for a, b in zip(e, lo)): c
                                      for e, c in d.items()}, X, Y))
        zero = [torsion_zero(q, top) for q in qs]
        print(f"    {menu}: factors {[f.as_expr() for f in fs]}; negative "
              f"{len(neg)}, torsion zero at N <= {top}: {zero}")
        pos = [str(f.as_expr()) for f in fs if not negative(f)]
        ok &= (len(fs) == 2 and len(neg) == 1 and zero == [None]
               and pos == ["x0 + 1"])
    check("P6 both free, no torsion zero found", ok)


def main():
    t0 = time.time()
    section_control()
    section_pairing()
    section_plane()
    section_rank3()
    section_line()
    section_free6()
    print()
    n, ok = len(CHECKS), sum(CHECKS)
    print(f"{ok} of {n} checks pass  [{time.time() - t0:.1f} s]")
    return 0 if ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
