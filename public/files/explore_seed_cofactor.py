"""explore_seed_cofactor.py -- can a four-term 0/1 polynomial be reducible
over Z without a binomial factor? The box census behind the size-4 law.
(Reads the seed vocabulary of explore_seed_shape.py; imports nothing from
it, every configuration here being a set of exponent vectors rather than
a menu.)

THE QUESTION. A MENU is a finite set of integers >= 2 read as a
0/1-coefficient polynomial in the primes; its CORE is that polynomial with
the monomial content divided out; a menu is a SEED when its core carries a
Z-irreducible factor with a negative coefficient. The plane's size-4 closure
(explore_seed_plane_floor.py) rests on one hypothesis the census supplied
and no argument did: every non-collinear four-term seed has a BINOMIAL
cofactor 1 + u. With it, the negative factor is m_1 + m_2 q(u) with a
monomial m_1 and the character u -> 1, m_2/m_1 -> -1 is a torsion zero;
without it nothing is known. A menu's exponent vectors are a thin subset of
the lattice -- the vectors of {2..32} -- so the census says little about the
hypothesis as a statement about four-term polynomials. This file asks it of
EVERY four-point configuration in a box: is a four-term 0/1 Laurent
polynomial that factors over Z always divisible by a binomial? Reducibility
here is Z-reducibility of the core (the monomial content divided out); a
BINOMIAL FACTOR is a Z-irreducible factor with exactly two terms. The kill
is a print: the number of reducible non-collinear configurations with no
binomial factor, with the witnesses.

THE HAND-ATTACK, on paper before any engine code. P = m_1 + m_2 + m_3 + m_4
with exponent vectors E_1..E_4; suppose P = g h with both factors
non-monomial. Write N(.) for the Newton polytope, N(P) = N(g) + N(h).

  (1) VERTEX COEFFICIENTS ARE +1. P is positive on the positive orthant, so
      g and h are nonvanishing there and of constant sign; take both
      positive. A polynomial positive on the orthant has positive
      coefficients at every vertex of its Newton polytope (the vertex
      dominates in its own outward direction), and at a vertex of N(P)
      the coefficient 1 is a product of one vertex coefficient of g and
      one of h, so both are +1.
  (2) AFFINE RANK 3 IS IRREDUCIBLE. N(P) is a simplex, whose Minkowski
      summands are homothetic copies, so N(g) and N(h) are both
      three-dimensional; a facet F of N(P) carries the face polynomial
      P_F = g_F h_F with both face polynomials two-dimensional, and P_F is
      a trinomial with independent exponents, irreducible outright (the
      trinomial lemma the three-member seed criterion rests on). So a
      reducible four-term polynomial has affine rank <= 2, and off a line
      it is exactly 2: PLANAR.
  (3) PLANE, BOTH FACTORS ON A LINE. g = G(u), h = H(w) with u, w
      independent monomials: the monomials u^a w^b are distinct, nothing
      cancels, and the term counts multiply, 4 = 2 x 2; every coefficient
      is a product of two and equals 1, so P = (1 + u^a)(1 + w^b) up to a
      monomial -- two binomials, and the negative factor, when there is
      one, is a cyclotomic piece of one of them.
  (4) PLANE, ONE FACTOR ON A LINE. h = H(w), and after a unimodular change
      w = y^e. Group P by x-exponent: P = sum_a x^a P_a(y) with each P_a a
      0/1 polynomial divisible by H(y^e), which has >= 2 terms; four terms
      leave exactly two values of a, each P_a a binomial y^b (1 + y^k_a).
      H(y^e) divides gcd(1 + y^k_1, 1 + y^k_2), which is 1 unless k_1 and
      k_2 share their 2-adic valuation, and then equals 1 + y^d with d =
      2^s gcd(odd parts): both k_a are odd multiples of d, and
      P = (1 + y^d)(m_1 q_1(y^d) + m_2 q_2(y^d)), q_i alternating sums --
      the binomial-cofactor shape of the census, derived rather than read.
  (5) PLANE, BOTH FACTORS TWO-DIMENSIONAL. N(g) and N(h) are polygons whose
      outward normals are among N(P)'s three or four, each owning at least
      three, so they SHARE an edge direction; choose coordinates with that
      edge at the bottom, P = (1 + x^l) + (two terms above), g = sum y^c
      g_c, h = sum y^d h_d, g_0 h_0 = 1 + x^l with both of >= 2 terms
      (coprime, each a product of cyclotomic polynomials). If the top row
      of P is a binomial, every middle row vanishes and P = A(x) + B(x)
      y^N with A, B binomials; Capelli over Q(x) (A and B squarefree) makes
      this reducible only when A = B up to a monomial and then P = (1 +
      x^l)(1 + x^m y^N) -- two binomials again. If the top row is a
      monomial, P has one middle term x^c y^j, and the Newton polygon of
      the cofactor polynomials over Q(x) at a cyclotomic divisor of g_0
      forces s, r >= j and g_0 | g_c, h_0 | h_d for 0 < c, d < j. The
      author's paper attack stops there; the s + r = 2 case closes by
      hand (row 1 a monomial forces g_0 and h_0 to differ by a monomial,
      and 1 + x^l = h_0 (h_0 +- x^m) has no solution with h_0 of two or
      more terms), and the general case is what the box is asked about.
      The census's (2,2) split is (3)-(5) with a binomial; the (1,4) split
      -- a four-term factor beside a one-term evaluation -- is the shape no
      step above produces, and the box is where it would show.
  (6) THE HUNCH, fixed before the run and marked as such: ZERO witnesses in
      the plane box and zero on the line to degree 60 -- the hand reaches
      every shape but the tail of (5), and that tail has the form of a
      trinomial over Q(x) whose coefficients are a monomial and a monomial
      over a binomial, which is the rigid shape the s + r = 2 case killed.

THE RIG.
  P0 CONTROLS, read before any census number: (1 + x)(1 + y) prints
     reducible with a binomial factor; 1 + x + y prints irreducible; the
     line's 1 + x^3 + x^4 + x^5 prints reducible with the binomial 1 + x
     and the negative factor 1 - x + x^2 + x^4; the trinomial 1 + x^4 +
     x^5 prints reducible (collinear, the control that collinearity is
     what the filter removes). The Kronecker prefilter (y -> x^(B+1), an
     irreducible image proving the source irreducible) is checked against
     direct factoring on a sample.
  P1 THE PLANE BOX: every 4-subset of [0, B]^2 with min x = min y = 0 (one
     representative per translation class), B = 6, non-collinear. Each is
     factored over Z (the prefilter first, then sympy on the survivors).
     Printed: the configuration count, the collinear count removed, the
     reducible count, how many of those carry a negative factor (the
     seeds), how many reducible have a binomial Z-factor, and THE KILL --
     the reducible with none, each printed with its factorization. Also
     tallied: the term-count split of the factors of every reducible one
     (2 x 2 or 1 x 4 by evaluation at the all-ones point), and the hull
     shape (triangle or quadrilateral).
  P2 THE RANK-3 BOX: every 4-subset of [0, 2]^3 with min coordinates 0 and
     affine rank 3. Printed: the count and the reducible count, which (2)
     says is zero.
  P3 THE LINE to degree 60: every quadrinomial 1 + x^a + x^b + x^c, c <= 60.
     Printed: the count, the seed count (a negative Z-factor), and the
     seeds with no binomial Z-factor -- the (1,4) split on the line,
     which the parent swept to degree 30.

THE PREDICTIONS, FIXED BEFORE THE RUN -- every kill is a printed count.
  K0  CONTROLS: the five verdicts as named in P0; prefilter agreement on
      the sample.
  K1  THE KILL: 0 reducible non-collinear configurations without a
      binomial factor in the plane box. ONE OR MORE -> the hypothesis
      fails as a statement about polynomials, the witness is printed with
      its factors, and the size-4 law keeps its box qualifier; the
      witness is then put through the torsion test by hand.
  K2  RANK 3: 0 reducible.
  K3  THE LINE: 0 seeds without a binomial factor to degree 60.
  K4  THE SPLIT: no Z-factor of a reducible configuration in the plane
      box evaluates to 4 at the all-ones point -- the (1,4) split never
      occurs -- which K1 implies and is printed separately because it is
      the shape the hand cannot produce. (Its multiset print lists EVERY
      Z-factor, so a binomial splitting into cyclotomic pieces shows as
      (1, 2, 2) or (1, 1, 2, 2), still a 2 x 2 split.)

RESOURCE ENVELOPE. About 47,000 plane configurations; the prefilter factors
a univariate quadrinomial of degree <= 48 in about a millisecond and the
survivors a bivariate polynomial in a few; estimate 3-8 minutes, memory
under 200 MB. Run: python explore_seed_cofactor.py

THE PROOF, completed after the first run was launched and before its
print was read, and banked on disk then. It bypasses the tail of (5)
entirely, by way of a classical theorem on the LINE and a classical
theorem on torsion points, both read full-text.

  Imports. MILLS (Math. Scand. 57, 1985, Theorem 2): for F = x^n + e_1
  x^m + e_2 x^p + e_3 with e_i = +-1, write F = A B with A the product of
  the cyclotomic factors; B is irreducible except when F is one of four
  listed forms, every one of which has constant term -1 -- so for an
  all-plus quadrinomial B is irreducible. CAPELLI: over a field K, x^n -
  c is reducible iff c is a p-th power in K for some prime p | n, or
  4 | n and c = -4 d^4. HAJOS: a nonzero root of a t-term polynomial has
  multiplicity at most t - 1. IHARA-SERRE-TATE (Lang's conjecture for
  curves in the two-dimensional torus): an irreducible curve containing
  infinitely many torsion points is a torsion coset, w = zeta for a
  primitive monomial w and a root of unity zeta. MANN, as the pairing
  lemma of (2) above.

  Step 0 (rank 3 irreducible, the trinomial lemma proved). (2) above,
  with the trinomial lemma itself proved by Capelli: 1 + u + v with u, v
  independent is, in coordinates with v = y^e and u = x^a y^b, a != 0,
  the binomial y^b (x^a + (1 + y^e) / y^b) in x over Q(y); (1 + y^e)/y^b
  is squarefree and nonconstant, so neither a p-th power nor -4 d^4, and
  Gauss's lemma (the content in x is 1) makes it irreducible over Z.

  Step 1 (the line). P = 1 + x^a + x^b + x^c reducible. By Mills a proper
  factorization carries a cyclotomic factor, so P vanishes at a root of
  unity zeta; the pairing lemma writes P = x^i (1 + x^s) + x^k (1 + x^t)
  with zeta^s = zeta^t = -1, so s and t share their 2-adic valuation v,
  and with d = 2^v gcd(odd parts) both s/d and t/d are odd: 1 + x^d
  divides both halves.

  Step 2 (the plane). P = g h, both non-monomial, affine rank 2 in
  coordinates x, y. For K beyond the x-width of N(P) the substitution
  y -> x^K is injective on the lattice points of N(P), hence on the
  supports of g and h, so F_K = g_K h_K is a reducible 0/1 quadrinomial
  and by Mills one of g_K, h_K divides the cyclotomic part. Infinitely
  many K, so one factor, say g, has g_K cyclotomic for infinitely many
  K. If g involves no y it is cyclotomic in x and vanishes on a torsion
  coset outright. Otherwise deg g_K grows without bound and Hajos gives
  at least deg g_K / (t_g - 1) distinct roots zeta, each a torsion point
  (zeta, zeta^K) of g = 0: infinitely many, so some component of g = 0
  is a torsion coset C = {chi : chi(w) = zeta}, and P vanishes on C. The
  pairing lemma holds at every TORSION point of C -- in coordinates with
  w = x', C is x' = zeta with y' free, and its torsion points are those
  with y' a root of unity, infinitely many -- so one pairing holds at
  infinitely many of them, and chi(m_1/m_2) = -1 for infinitely many
  roots of unity chi(y') forces the difference vector to have no
  y'-component. Both differences are
  multiples of x': P = m_2 (1 + x'^s) + m_4 (1 + x'^t) with zeta^s =
  zeta^t = -1, and Step 1's gcd gives the binomial 1 + x'^d dividing
  both halves: P = (1 + w)(m_2 q_s(w) + m_4 q_t(w)) with w = x'^d and q_n
  the alternating sum 1 - w + ... + w^(n - 1), n = s/d and t/d odd.

  So: THE COFACTOR THEOREM. A four-term 0/1 polynomial, in any number of
  variables, that is reducible over Z is divisible by 1 + u for some
  monomial u. (Theorem; rank >= 3 is irreducible, the line is Step 1,
  the plane Step 2.)

  Step 3 (the size-4 closure). P non-collinear, so v = m_4/m_2 is
  independent of w. The negative Z-irreducible factors of P are among
  the cyclotomic pieces of 1 + w -- rooted -- and the factors of R =
  q_s(w) + v q_t(w). Let c = gcd(q_s, q_t), cyclotomic in w, and R = c
  R' with R' = a(w) + v b(w), a and b coprime squarefree products of
  cyclotomics. If s = t then R = q_s (1 + v) and P is a product of two
  binomials, every factor cyclotomic and rooted. If s != t, write v =
  x'^i y'^j with j >= 1: over Q(x'), R' = b x'^i (y'^j - C) with C =
  -a / (b x'^i), and a/b in lowest terms is not a p-th power (both
  squarefree, not both constant) and not -4 d^4, so R' is irreducible
  over Q(x'), primitive over Z[x'^+-] since gcd(a, b) = 1, and
  Z-irreducible by Gauss. At the character chi(w) = 1, chi(v) = -1 it
  vanishes: a(1) - b(1) = (q_s(1) - q_t(1)) / c(1) = (1 - 1) / c(1), and
  c(1) != 0 because no cyclotomic factor of 1 + w^n vanishes at 1. So
  the one non-cyclotomic factor is rooted, and EVERY NON-COLLINEAR
  FOUR-TERM SEED IS ROOTED (theorem). Along a line v is a power of w,
  the character is unavailable, and 1 + x^3 + x^4 + x^5 is free.

FINDINGS (the recorded run: 9 of 9 checks, 1006.3 s -- the plane box
364.5 s, the rank-3 box 178.3 s, the line 463.5 s -- against a 3-8 minute
estimate, twice the top of it, memory under 100 MB. The first run printed
the same figures at 8 of 9 in 1011.1 s; its one miss was the K4 predicate,
which compared the printed multiset of ALL Z-factor evaluations against
(2, 2) where a binomial splitting into cyclotomic pieces prints (1, 2, 2):
no factor evaluates to 4, which is what K4 asserts, and the predicate was
corrected to say so before the recorded run.)

  F1  THE KILL DID NOT FIRE IN THE PLANE (rule, exhaustive over [0,6]^2;
      theorem by the proof above): 46,921 translation classes of four
      points, 84 collinear removed, 26,448 proved irreducible by the
      prefilter, 20,389 factored, 1,921 reducible, and every one of the
      1,921 carries a binomial Z-factor. 1,274 of them are seeds (a
      negative factor). Every reducible hull is a QUADRILATERAL -- the
      theorem's shape m_2 (1 + w^s) + m_4 (1 + w^t) has two parallel
      edges -- and no Z-factor evaluates to 4 at the all-ones point: the
      splits are (2, 2) at 1,747, (1, 2, 2) at 156, (1, 1, 2, 2) at 18.
  F2  RANK 3 IS IRREDUCIBLE (theorem, Step 0; checked over [0,2]^3): 0
      reducible among 8,424 rank-3 configurations.
  F3  THE LINE (theorem, Step 1; checked to degree 60): 34,220
      quadrinomials, 14,825 seeds, 0 without a binomial Z-factor -- the
      parent's 1,780 to degree 30 extended by a factor of eight and then
      closed by Mills.
  F4  THE RESIDUAL FRONT is size 5 off a line: five is prime, so a size-5
      seed is a reducible 0/1 pentanomial with non-collinear exponents,
      and no Mills exists for pentanomials; the swept menu boxes hold
      none, the plane's free witnesses sit at six, and the gap between
      the closure at four and the witnesses at six is that one size.
"""

import os
import sys
import time
from itertools import combinations
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import Poly, symbols, factor_list

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_seed_rank_law import CHECKS, check

x, y, z = symbols('x y z')


def poly_of(pts, gens):
    return sum(sympy.Mul(*[g ** e for g, e in zip(gens, p)]) for p in pts)


def affine_rank(pts):
    base = pts[0]
    vecs = [[a - b for a, b in zip(p, base)] for p in pts[1:]]
    return sympy.Matrix(vecs).rank() if vecs else 0


def z_factors(expr, gens):
    """Non-monomial Z-irreducible factors of expr, with multiplicity."""
    _, fl = factor_list(sympy.expand(expr), *gens)
    out = []
    for f, m in fl:
        p = Poly(f, *gens)
        if len(p.terms()) >= 2:
            out.extend([p] * m)
    return out


def is_negative(p):
    return any(c < 0 for c in p.coeffs())


def analyse(pts, gens):
    """dict: reducible, binomial (a two-term Z-factor), negative (a
    negative Z-factor), split (sorted tuple of factor evaluations at 1),
    factors (strings)."""
    fs = z_factors(poly_of(pts, gens), gens)
    return {
        'reducible': len(fs) >= 2,
        'binomial': any(len(f.terms()) == 2 for f in fs),
        'negative': any(is_negative(f) for f in fs),
        'split': tuple(sorted(int(f.as_expr().subs({g: 1 for g in gens}))
                              for f in fs)),
        'factors': [str(f.as_expr()) for f in fs],
    }


def kronecker_irreducible(pts, K):
    """True when the Kronecker image y -> x^K is irreducible over Z, which
    proves the source irreducible (the image is injective on every
    monomial inside the box, hence on the factors' supports)."""
    expo = sorted(a + K * b for a, b in pts)
    e0 = expo[0]
    f = sum(x ** (e - e0) for e in expo)
    _, fl = factor_list(f, x)
    return sum(m for g, m in fl if Poly(g, x).degree() > 0) == 1


def hull_shape(pts):
    """'triangle' if one point lies in the hull of the other three (or on
    an edge), else 'quadrilateral'."""
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    for i in range(4):
        others = [pts[j] for j in range(4) if j != i]
        p = pts[i]
        s = [cross(others[k], others[(k + 1) % 3], p) for k in range(3)]
        if all(v >= 0 for v in s) or all(v <= 0 for v in s):
            return 'triangle'
    return 'quadrilateral'


def stage_p0():
    print("P0 CONTROLS")
    g2 = (x, y)
    a = analyse([(0, 0), (1, 0), (0, 1), (1, 1)], g2)
    print(f"  (1+x)(1+y): reducible={a['reducible']} binomial={a['binomial']} {a['factors']}")
    check("P0 (1+x)(1+y) reducible with a binomial", a['reducible'] and a['binomial'])
    b = analyse([(0, 0), (1, 0), (0, 1)], g2)
    print(f"  1+x+y: reducible={b['reducible']}")
    check("P0 1+x+y irreducible", not b['reducible'])
    c = analyse([(0,), (3,), (4,), (5,)], (x,))
    print(f"  1+x^3+x^4+x^5: reducible={c['reducible']} binomial={c['binomial']} negative={c['negative']} {c['factors']}")
    check("P0 1+x^3+x^4+x^5 = (1+x)(1-x+x^2+x^4)",
          c['reducible'] and c['binomial'] and c['negative'] and len(c['factors']) == 2)
    d = analyse([(0,), (4,), (5,)], (x,))
    print(f"  1+x^4+x^5: reducible={d['reducible']} {d['factors']}")
    check("P0 1+x^4+x^5 reducible (collinear trinomial)", d['reducible'])
    # prefilter agreement on a sample
    B, K = 6, 7
    sample = [((0, 0), (2, 0), (1, 1), (0, 3)), ((0, 0), (3, 0), (1, 1), (2, 2)),
              ((0, 0), (1, 0), (0, 1), (1, 1)), ((0, 0), (2, 0), (0, 2), (2, 2)),
              ((0, 0), (1, 0), (0, 2), (3, 1)), ((0, 0), (3, 0), (0, 3), (1, 1))]
    ok = True
    for pts in sample:
        ki = kronecker_irreducible(pts, K)
        red = analyse(list(pts), g2)['reducible']
        print(f"  prefilter {pts}: kronecker_irreducible={ki} reducible={red}")
        if ki and red:
            ok = False
    check("P0 prefilter never calls a reducible configuration irreducible (sample)", ok)


def stage_p1(B=6):
    print(f"\nP1 THE PLANE BOX [0,{B}]^2, one representative per translation class")
    t0 = time.time()
    K = B + 1
    g2 = (x, y)
    grid = [(a, b) for a in range(B + 1) for b in range(B + 1)]
    total = collinear = reducible = seeds = binom = 0
    kills, splits, hulls = [], {}, {}
    prefiltered = 0
    for pts in combinations(grid, 4):
        if min(p[0] for p in pts) or min(p[1] for p in pts):
            continue
        total += 1
        if affine_rank(list(pts)) < 2:
            collinear += 1
            continue
        if kronecker_irreducible(pts, K):
            prefiltered += 1
            continue
        a = analyse(list(pts), g2)
        if not a['reducible']:
            continue
        reducible += 1
        seeds += a['negative']
        binom += a['binomial']
        splits[a['split']] = splits.get(a['split'], 0) + 1
        hs = hull_shape(list(pts))
        hulls[hs] = hulls.get(hs, 0) + 1
        if not a['binomial']:
            kills.append((pts, a['factors']))
    print(f"  configurations {total}, collinear removed {collinear}, "
          f"prefilter proved irreducible {prefiltered}, factored {total - collinear - prefiltered}")
    print(f"  reducible {reducible}; with a negative factor (seeds) {seeds}; "
          f"with a binomial Z-factor {binom}")
    print(f"  evaluation splits of the reducible: {splits}")
    print(f"  hull shapes of the reducible: {hulls}")
    print(f"  THE KILL: reducible non-collinear configurations with NO binomial factor: {len(kills)}")
    for pts, fs in kills[:20]:
        print(f"    {pts}: {fs}")
    print(f"  ({time.time() - t0:.1f} s)")
    check("K1 plane box: no reducible configuration lacks a binomial factor", len(kills) == 0)
    check("K4 plane box: no Z-factor evaluates to 4 at the all-ones point",
          all(4 not in s for s in splits))
    return kills


def stage_p2(B=2):
    print(f"\nP2 THE RANK-3 BOX [0,{B}]^3")
    t0 = time.time()
    g3 = (x, y, z)
    grid = [(a, b, c) for a in range(B + 1) for b in range(B + 1) for c in range(B + 1)]
    total = reducible = 0
    wit = []
    for pts in combinations(grid, 4):
        if min(p[0] for p in pts) or min(p[1] for p in pts) or min(p[2] for p in pts):
            continue
        if affine_rank(list(pts)) < 3:
            continue
        total += 1
        # Kronecker in two steps: z -> y^(B+1), then y -> x^((B+1)^2)
        K1, K2 = B + 1, (B + 1) ** 2
        expo = sorted(a + K2 * b + K2 * K1 * c for a, b, c in pts)
        f = sum(x ** (e - expo[0]) for e in expo)
        _, fl = factor_list(f, x)
        if sum(m for g, m in fl if Poly(g, x).degree() > 0) == 1:
            continue
        a = analyse(list(pts), g3)
        if a['reducible']:
            reducible += 1
            wit.append((pts, a['factors']))
    print(f"  rank-3 configurations {total}, reducible {reducible} ({time.time() - t0:.1f} s)")
    for w in wit[:10]:
        print(f"    {w}")
    check("K2 rank-3 box: no reducible configuration", reducible == 0)


def stage_p3(dmax=60):
    print(f"\nP3 THE LINE: 1 + x^a + x^b + x^c, c <= {dmax}")
    t0 = time.time()
    total = seeds = 0
    kills = []
    for c in range(3, dmax + 1):
        for a, b in combinations(range(1, c), 2):
            total += 1
            _, fl = factor_list(1 + x ** a + x ** b + x ** c, x)
            fs = [Poly(g, x) for g, m in fl for _ in range(m) if Poly(g, x).degree() > 0]
            if any(is_negative(f) for f in fs):
                seeds += 1
                if not any(len(f.terms()) == 2 for f in fs):
                    kills.append(((a, b, c), [str(f.as_expr()) for f in fs]))
    print(f"  quadrinomials {total}, seeds {seeds}, seeds with no binomial factor {len(kills)} "
          f"({time.time() - t0:.1f} s)")
    for k in kills[:20]:
        print(f"    {k}")
    check("K3 line to degree 60: every seed has a binomial factor", len(kills) == 0)


def main():
    t0 = time.time()
    stage_p0()
    stage_p1()
    stage_p2()
    stage_p3()
    n = len(CHECKS)
    ok = sum(1 for _, v in CHECKS if v)
    print(f"\n{ok} of {n} checks, {time.time() - t0:.1f} s")
    for name, v in CHECKS:
        print(f"  [{'ok' if v else 'FAIL'}] {name}")


if __name__ == '__main__':
    main()
