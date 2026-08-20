"""explore_seed_torsion.py -- where a seed's negative factor first stops being
torsion-rooted. Is every negative factor of an in-box seed rooted at a
torsion point of the torus, and if not, at what size and in what box does
the first torsion-free one appear? (Reads the vocabulary and the machinery
of explore_seed_rank_law.py, which it imports.)

THE QUESTION. A MENU is a finite set of integers >= 2 read as a
0/1-coefficient polynomial in the primes; its CORE is that polynomial with
the monomial content divided out; a menu is a SEED when its core has two or
more non-monomial Z-irreducible factors and one of them carries a negative
coefficient. Every negative factor the corpus had met before this file is
CYCLOTOMIC-ROOTED: it vanishes at a TORSION POINT, a tuple of roots of
unity -- 1 - x + x^2 at a primitive sixth root, x^2 - xy + y^2 on a torsion
line, and the rank-4 seeds of size 8 over {2..20}, of shape
x(x^2 - x + 1) + L with L a 0/1 sum in the other variables, at a sixth root
beside a vanishing sum 1 + w + w^2 of L's monomials. Call a factor
TORSION-ROOTED when it has a torsion zero and TORSION-FREE when it has
none. Univariately the two notions are cyclotomic factor / none, and the
theory of lacunary polynomials (Schinzel; Bombieri and Zannier) splits the
cyclotomic part off and treats the rest as the general case; which part a
seed's negative factor lives in is what this file reads.

THE LITERATURE, read before the engine. Ljunggren (Math. Scand. 8, 1960)
and independently Tverberg: a reducible 0/1 trinomial has a cyclotomic
factor, and the trinomial removed of its cyclotomic factors is irreducible
or 1 (quoted in Filaseta, Finch and Nicol, J. Theor. Nombres Bordeaux 18
(2006), Lemma 3.1, and in Filaseta and Kalogirou, arXiv 2508.12242, Section
4). Ljunggren's quadrinomial theorem was amended by Mills (Math. Scand. 57,
1985): as read, for -1 + x + x^n + x^m the non-cyclotomic part is
irreducible EXCEPT for -1 + x^r + x^{7r} + x^{8r} = (x^{2r} + 1)(x^{3r} +
x^{2r} - 1)(x^{3r} - x^r + 1) -- the plastic number's polynomial again, on
a quadrinomial with one minus sign (quoted in Dutykh and Verger-Gaugry,
arXiv 1902.09814, Theorem 8; the all-plus quadrinomial case was not read
and is checked on the box below). Filaseta, Finch and Nicol: the recursive sequence
f_j = x^{k_j} + f_{j-1}, k_j least making f_j reducible, runs 1, 1 + x^3,
1 + x^3 + x^15, ... and is FINITE, ending at f_7 = 1 + x^3 + x^15 + x^16 +
x^32 + x^33 + x^34 + x^35. Schinzel (1986), as re-proved for 0/1 polynomials
by Filaseta and Kalogirou: for fixed k, almost all 1 + x^{n_1} + ... +
x^{n_k} removed of their cyclotomic factors are irreducible. Aliev and
Smyth, Solving algebraic equations in roots of unity (Forum Math. 24, 2012;
arXiv 0704.1747): every torsion zero set of a polynomial is a finite union
of maximal torsion cosets (Laurent's theorem), with an algorithm built on
Beukers and Smyth's conjugation lemma rather than Mann's; the instrument
below uses Mann directly, the polynomials here being small.

THE HAND-ATTACK, on paper before any engine code.

  (1) THE INVARIANT. f(chi) for a character chi: Z^m -> roots of unity
      depends only on chi restricted to the lattice L_f = <E_j - E_1> of the
      factor's exponent differences (rank rho), and every character of L_f
      extends to Z^m, so the factor is REDUCED to its own lattice: a Z-basis
      of L_f (Hermite normal form), the exponents rewritten in it, and f
      has a torsion zero iff the reduced polynomial in rho variables does.
      rho <= dim Newt(core) <= floor(n/2) <= 4 at n <= 9 (the half-size law,
      Minkowski sum), so every in-box factor lives on a torus of dimension
      <= 4 whatever its variable count. The CORE is never reduced this way
      before factoring -- 1 + x^3 reduces to 1 + y, irreducible, while
      1 + x^3 factors -- so the core is factored in the prime variables as
      the parent rig does and only the FACTOR is reduced. A torsion zero of
      the factor, not a cyclotomic factor of a coordinate restriction, is
      the invariant: restrictions miss the torsion points off the axes, and
      the cheap tier counts how many factors are rooted only there.
  (2) WHY ONE BRUTE FORCE IS COMPLETE. Let chi be a torsion zero. f(chi) =
      sum c_j chi(E_j) = 0 is a vanishing sum of roots of unity with
      integer coefficients; merge equal values, split into MINIMAL
      vanishing sums, pull back to a partition pi of the k monomials into
      blocks of size >= 2, each block vanishing at chi. Mann (Mathematika
      12, 1965): in a minimal vanishing sum of r distinct roots of unity
      with rational coefficients, normalized to contain 1, every term has
      order dividing M_r = product of the primes <= r. So within a block
      the ratios chi(E_j - E_j') lie in the M_|B|-th roots of unity, i.e.
      chi restricted to L_pi = <within-block differences> takes values of
      order dividing M_pi = M_{largest block}; and each block's vanishing
      depends only on chi|L_pi. Extend chi|L_pi to Z^rho: trivially on a
      complement of the saturation of L_pi, and on the saturation with
      orders dividing M_pi * e_pi, e_pi the exponent of the torsion of
      Z^rho / L_pi. The extension is again a torsion zero, of order
      dividing N_pi = M_pi * e_pi. Hence f has a torsion zero iff it has
      one of order dividing N* = lcm over all partitions pi of N_pi -- a
      finite search over (Z/N*)^rho, COMPLETE. 1 + x^3 (k = 2, M = 2,
      L_pi = 3Z, e_pi = 3, the zero at order 6) is the smallest case and
      the classical g(x^d) subtlety of the sparse-polynomial cyclotomic
      bound. e_pi is the largest invariant factor of the difference
      matrix, from gcds of minors.
  (3) THE TIERS AND THEIR COST. CHEAP: the search at N = 6 over (Z/6)^rho,
      at most 1296 points, where every corpus witness lives. COMPLETE: N*
      as above; M_k is 6 for k <= 4, 30 for k = 5, 6 and 210 for
      k = 7..10, so the complete grid is 30^rho * e^rho at k <= 6 and
      210^4 at seven terms in four dimensions -- out of budget there. The
      complete tier is only needed on the factors the cheap tier leaves,
      and a factor left undecided prints as such; the rule in range needs
      that count at zero. Evaluation is chunked numpy over the grid;
      candidates with |f| < 1e-6 are verified EXACTLY in Z[T]/Phi_N(T),
      and a true zero is always a candidate, so there is no false negative.
  (4) THE CONTROLS. Negative, univariate: x^3 - x + 1 (irreducible, not
      cyclotomic; the plastic number's polynomial). Negative, multivariate:
      x^3 - x + 1 + 3y -- |3 eta| = 3 while |zeta^3 - zeta + 1| <= 3 with
      equality only if zeta^3 = -zeta = 1, impossible; so no torsion zero,
      by hand, and the complete tier must print none at rho = 2. Positive:
      1 - x + x^2, x^2 - xy + y^2 (rho = 1 after reduction), and
      x^3 - x^2 + x + y + z + w, the first size-8 seed's factor -- each
      found at N = 6. The lift: 1 + x^3 has its zero found through e = 3.
  (5) WHAT ELSE TO PRINT. The cheap tier sees EVERY zero of order dividing
      6, so it can say whether one sits on an axis (one coordinate off 1,
      the absorbed-cyclotomic mechanism) or only off the axes; and it can
      test, through each zero and along each direction in {-1, 0, 1}^rho,
      whether f vanishes identically on the torsion LINE through it -- a
      lower bound on the dimension of the torsion locus, which for rho >= 2
      can never reach rho - 1 (a factor containing a codimension-1 torsion
      coset is a cyclotomic polynomial in one monomial, of lattice rank 1).

THE RIG. C0 the controls. C1 the UNIVARIATE CENSUS: every 0/1 polynomial
with constant term 1 and degree <= 16 (2^15 per degree), tested for a
cyclotomic factor exactly (Phi_d for phi(d) <= 16) and, failing that,
factored; per degree, the reducible ones with no cyclotomic factor are
counted by term count, with how many carry a negative factor, and the least
degree per term count is printed; sizes <= 4 are swept separately to degree
30 as the trinomial theorem's check and the quadrinomial case's box. C2 the MULTIVARIATE CELL: menus of sizes
5 and 6 over {2..24}, 7 and 8 over {2..20} and 9 over {2..24} -- the boxes
the parent rigs ran -- enumerated by the parent's code, classes at ranks
<= floor(n/2) (every higher rank is empty by the half-size law) factored
whole, and every negative factor of every seed put through both tiers. A
rehearsal flag (--rehearse) runs every stage small: boxes {2..16}, census
to degree 12.

THE PREDICTIONS, FIXED BEFORE THE RUN -- every kill is a printed count.

  C0  CONTROLS: the two negatives print no torsion zero, the univariate
      one at both tiers and the multivariate one at the complete tier;
      the three positives and the lift print zeros at the cheap tier.
  C1  CENSUS: no reducible 0/1 polynomial of degree <= 11 lacks a
      cyclotomic factor; degree 12 holds 24 that do, 8 with seven terms
      and 16 with nine, twelve of them carrying a negative factor (the
      preliminary run this file re-derives); sizes <= 4 print 0 to degree
      30 (trinomials by Ljunggren and Tverberg, as read; quadrinomials
      unread in the all-plus case, Mills's exception carrying a minus
      sign, so that cell is a box fact). The least degree at sizes 5 and 6, if any <= 16, is printed.
  C2  THE CELL: the aim's hunch was that it prints EMPTY -- every in-box
      negative factor torsion-rooted, with the univariate degree-12 floor
      as the reason a small box cannot hold one. The checks are the
      instrument's: no factor undecided; every control decided by the
      named tier. The KILL is a print: the number of negative factors with
      no torsion zero under the complete tier, with their seeds, sizes and
      ranks. The largest k among the factors and its M_k print.
  C3  THE PRINTS: per factor the tier that decided it, the number of zeros
      mod 6, how many sit on an axis, and whether a torsion line through a
      zero lies in the factor.

RESOURCE ENVELOPE. Enumeration of about 1.08 million menus at the parent
rig's rate (~80 s) plus sympy factoring of ~28,000 classes (~50 s); the
census factors only what passes the cyclotomic sieve (~2 minutes); the
torsion tests are milliseconds each. Estimated five minutes, memory under
200 MB. Run: python explore_seed_torsion.py [--rehearse]

FINDINGS (the recorded run, 11 of 11 checks, 267.8 s; every figure below is
that run's print).

  F1  THE KILL FIRED, AT THE SMALLEST SIZE THE BOXES HOLD. The five cells
      hold 37 seeds (sizes 5, 7 and 9 hold none in their boxes: 238, 1,513
      and 18,711 classes at rank <= floor(n/2), 0, 0 and 19 reducible, none
      a seed; size 6 over {2..24} holds 28 among 2,735 classes, size 8 over
      {2..20} 9 among 5,256), one negative factor each. TWO are
      TORSION-FREE under the complete tier (rho = 2, k = 5, N* = 60, 0
      zeros): {2,3,4,8,16,24}, core (1 + x)(x^3 + x^2 y - xy + x + y) =
      (1 + x)[x(1 + x^2) + y(1 - x + x^2)], and {2,3,6,12,16,24}, core
      (1 + x)[x(1 - x + x^2) + y(1 + x^2)], both at rank 2. The other 35
      are rooted at the cheap tier. So "every negative factor is torsion-
      rooted" is FALSE in the corpus's own boxes, at size 6. (The
      univariate census F4 below counts a DIFFERENT statistic -- reducible
      with no cyclotomic factor at all -- which excludes exactly the shape
      these two witnesses have, a cyclotomic cofactor beside a torsion-
      free negative factor; the line's own least degree for that shape is
      5, at three terms, 1 + x^4 + x^5 = (x^2 + x + 1)(x^3 - x + 1), read
      with this cell's criterion in explore_seed_line_floor.py.)
  F2  THE WITNESS BY HAND, stronger than the print (property, proved). On
      |x| = 1, x = e^{i theta}: |x(1 + x^2)| = |x^-1 + x| = |2 cos theta|
      and |1 - x + x^2| = |x^-1 - 1 + x| = |2 cos theta - 1|; a zero with
      |y| = 1 needs them equal, i.e. cos theta = 1/4, and 2 cos theta =
      x + x^-1 is an algebraic integer at every root of unity while 1/2 is
      not. So the factor has no TORSION zero. It does meet the unit torus:
      at cos theta = 1/4 both moduli are 1/2 and y = -x(1 + x^2)/(1 - x +
      x^2) is unimodular, a zero of the factor with |x| = |y| = 1 -- the
      computation above finds that point and then shows it is not a
      torsion point. The second witness is the same computation with the
      moduli swapped.
      Irreducible because linear in y with coprime coefficients x(1 + x^2)
      and 1 - x + x^2. THE SHAPE is the size-8 family's: (1 + x)(A + L)
      with (1 + x)A and (1 + x)L both 0/1 -- there A = x(x^2 - x + 1)
      vanishes at a sixth root and L can vanish beside it; here A =
      x(1 + x^2) does not vanish where B = 1 - x + x^2 does, and one y
      cannot make |A| = |B| at any root of unity.
  F3  THE ROOTED 35 (observation, these boxes): 32 have k = 5 or 6 and 3
      have k = 7 (the largest; Mann's M_7 = 210, never needed since all
      three are rooted at N = 6). 14 of the 35 have a zero on an axis (one
      coordinate off 1 in the reduced lattice) and 21 are rooted only off
      the axes -- so a coordinate restriction is the wrong invariant more
      often than not; 20 contain a torsion LINE through a found zero (15
      of the 17 of size 6 at rho 3 with k = 5, and all 5 of size 8 at
      rho 4), and every rooted factor at rho = 2, every k = 7 factor and
      every size-8 factor at rho 3 is rooted at isolated points only, in
      this search. A print and not a check: every
      one of the 37 cores has cofactor 1 + x_2, the prime 2's variable --
      each seed in these boxes is (1 + x)(negative factor).
  F4  THE UNIVARIATE CENSUS (rule, exhaustive to degree 16; sizes <= 4 to
      degree 30). No reducible 0/1 polynomial with constant term 1 and
      degree <= 11 lacks a cyclotomic factor; degree 12 holds 24 (8 at
      seven terms, all with a negative factor; 16 at nine, 4 with), the
      preliminary figures re-derived. The least degree by term count: 6
      terms at 13, x^13 + x^10 + x^6 + x^2 + x + 1 = (x^5 + x^2 + 1)(x^8 -
      x^3 + x + 1); 7 at 12 ((x^5 - x^3 + 1)(x^7 + x^5 + x^4 + x^3 + x^2
      + x + 1)); 8 at 13; 9 at 12 ((x^4 + x + 1)(x^8 + x^2 + 1), both factors
      nonnegative); 10, 11 and 12 terms at 15. Five terms has no witness
      to degree 16 UNDER THIS STATISTIC, and sizes <= 4 none to degree 30
      (three terms as Ljunggren and Tverberg require; four terms a box
      fact here). Twelve-term witnesses carry no negative factor at 15 or
      16 (both factors 0/1). This statistic is not the seed question: a
      0/1 polynomial with a cyclotomic factor whose cofactor is a torsion-
      free negative factor is a seed with a torsion-free negative factor
      and is not counted here -- 1 + x + x^2 + x^3 + x^9 = Phi_5(x) (x^5 -
      x^4 + 1) at five terms, 1 + x^4 + x^5 = Phi_3(x) (x^3 - x + 1) at
      three. The seed question along the line is explore_seed_line_floor.py's.

  TIERS. F1: rule in range for the 35 (these five boxes) and a FACT for
  the two (a complete search, then F2's proof). F2: property, proved. F3:
  observation, these boxes. F4: rule, exhaustive in its degree range.

  RUN RECORD. The instrument was developed against a preliminary survey of
  the same five cells (the 37 seeds and the two torsion-free factors first
  printed there, which is what moved F2 onto paper before this file ran);
  every figure above is this file's own print. Rehearsal over {2..16} with
  the census to degree 12: 9.5 s, 11 checks, four seeds all rooted. Full
  run 267.8 s, the census 141 s of it; peak memory not measured, the
  largest array a 50-million-point budget never reached (N*^rho = 3,600 at
  the two complete-tier factors). Python 3.12, sympy, numpy.
"""

import itertools
import math
import os
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np
import sympy
from sympy import Matrix, Poly, ZZ, symbols
from sympy.matrices.normalforms import hermite_normal_form

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_seed_rank_law import (CHECKS, check, reduced_matrix,
                                   affine_rank, canonical, poly_of, describe)

T = symbols('T')
CELLS = [(5, 24), (6, 24), (7, 20), (8, 20), (9, 24)]


# ---------------------------------------------------------- the instrument
def primorial_upto(r):
    m = 1
    for p in sympy.primerange(2, r + 1):
        m *= p
    return m


def reduce_to_lattice(monoms):
    """The exponents rewritten in a Z-basis of L = <E_j - E_1>, shifted to
    minimum 0 per coordinate: (list of tuples in Z^rho, rho)."""
    E = [tuple(m) for m in monoms]
    D = Matrix([[a - b for a, b in zip(e, E[0])] for e in E[1:]])
    if D.rows == 0 or D.is_zero_matrix:
        return [tuple()] * len(E), 0
    H = hermite_normal_form(D.T).T
    B = Matrix([list(H.row(i)) for i in range(H.rows)
                if not H.row(i).is_zero_matrix])
    rho = B.rows
    inv = (B * B.T).inv()
    coords = []
    for e in E:
        d = Matrix([[a - b for a, b in zip(e, E[0])]])
        c = d * B.T * inv
        assert c * B == d and all(x.is_integer for x in c)
        coords.append(tuple(int(x) for x in c))
    mins = [min(c[i] for c in coords) for i in range(rho)]
    return [tuple(c[i] - mins[i] for i in range(rho)) for c in coords], rho


def torsion_exponent(rows):
    """Exponent of the torsion of Z^rho / (row lattice): the largest
    invariant factor d_r / d_{r-1}, from gcds of minors."""
    M = Matrix(rows)
    if M.is_zero_matrix:
        return 1
    r = M.rank()

    def gcd_minors(k):
        g = 0
        for ri in itertools.combinations(range(M.rows), k):
            for ci in itertools.combinations(range(M.cols), k):
                g = math.gcd(g, int(M.extract(list(ri), list(ci)).det()))
        return g
    return gcd_minors(r) // (gcd_minors(r - 1) if r > 1 else 1)


def partitions_min2(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for k in range(1, len(rest) + 1):
        for mates in itertools.combinations(rest, k):
            remaining = [x for x in rest if x not in mates]
            for p in partitions_min2(remaining):
                yield [(first,) + mates] + p


def complete_order(coords):
    """N* = lcm over partitions pi of M_{largest block} * e_pi."""
    N = 1
    for p in partitions_min2(range(len(coords))):
        rows = []
        for block in p:
            b0 = coords[block[0]]
            for j in block[1:]:
                rows.append([a - b for a, b in zip(coords[j], b0)])
        n_pi = primorial_upto(max(len(b) for b in p)) * torsion_exponent(rows)
        N = N * n_pi // math.gcd(N, n_pi)
    return N


def exact_zero(coords, coeffs, a, N):
    g = sum(c * T ** (sum(x * y for x, y in zip(e, a)) % N)
            for c, e in zip(coeffs, coords))
    return Poly(g, T).rem(Poly(sympy.cyclotomic_poly(N, T), T)).is_zero


def zeros_mod(coords, coeffs, rho, N, chunk=1 << 18, budget=50_000_000):
    """Every a in (Z/N)^rho with f(omega^a) = 0, exactly verified; None
    when the grid is over budget."""
    total = N ** rho
    if total > budget:
        return None
    E = np.array(coords, dtype=np.int64).reshape(len(coords), rho)
    C = np.array(coeffs, dtype=np.float64)
    found = []
    for start in range(0, total, chunk):
        idx = np.arange(start, min(total, start + chunk), dtype=np.int64)
        A = np.empty((len(idx), rho), dtype=np.int64)
        q = idx.copy()
        for i in range(rho - 1, -1, -1):
            A[:, i] = q % N
            q //= N
        ph = (A @ E.T) % N
        val = (C * np.exp(2j * np.pi * ph / N)).sum(axis=1)
        for j in np.nonzero(np.abs(val) < 1e-6)[0]:
            a = tuple(int(x) for x in A[j])
            if exact_zero(coords, coeffs, a, N):
                found.append(a)
    return found


def on_torsion_line(coords, coeffs, a, v, N):
    """Does f vanish identically on {omega^a * t^v}? Group the monomials
    by their t-exponent and test each group's sum in Z[T]/Phi_N."""
    groups = {}
    for c, e in zip(coeffs, coords):
        te = sum(x * y for x, y in zip(e, v))
        groups[te] = groups.get(te, 0) + c * T ** (sum(x * y for x, y in zip(e, a)) % N)
    phi = Poly(sympy.cyclotomic_poly(N, T), T)
    return all(Poly(g, T).rem(phi).is_zero for g in groups.values())


def torsion_line_dim(coords, coeffs, zeros, rho, N):
    """1 if some torsion line through a found zero lies in f = 0 (searched
    along directions in {-1, 0, 1}^rho), else 0."""
    if rho < 2:
        return 0
    dirs = [v for v in itertools.product((-1, 0, 1), repeat=rho)
            if any(v) and next(x for x in v if x) > 0]
    for a in zeros:
        for v in dirs:
            if on_torsion_line(coords, coeffs, a, v, N):
                return 1
    return 0


def test_factor(monoms, coeffs, cheap_N=6):
    coords, rho = reduce_to_lattice(monoms)
    k = len(coords)
    z = zeros_mod(coords, coeffs, rho, cheap_N)
    if z:
        axis = sum(1 for a in z if sum(1 for x in a if x) <= 1)
        line = torsion_line_dim(coords, coeffs, z, rho, cheap_N)
        return dict(rho=rho, k=k, tier='cheap', N=cheap_N, zeros=len(z),
                    axis=axis, line=line)
    Nstar = complete_order(coords)
    z = zeros_mod(coords, coeffs, rho, Nstar)
    if z is None:
        return dict(rho=rho, k=k, tier='undecided', N=Nstar, zeros=None,
                    axis=None, line=None)
    return dict(rho=rho, k=k, tier='complete', N=Nstar, zeros=len(z),
                axis=None, line=None)


def factor_data(expr, gens):
    p = Poly(expr, *gens)
    return p.monoms(), [int(c) for c in p.coeffs()]


# ------------------------------------------------------------- the stages
def stage_c0():
    print("\nC0  CONTROLS")
    x, y, z, w = symbols('x y z w')
    cases = [
        ("x^3 - x + 1 (negative, univariate)", x**3 - x + 1, (x,), 'complete', 0),
        ("x^3 - x + 1 + 3y (negative, two variables)", x**3 - x + 1 + 3*y, (x, y), 'complete', 0),
        ("1 - x + x^2", 1 - x + x**2, (x,), 'cheap', 1),
        ("x^2 - xy + y^2", x**2 - x*y + y**2, (x, y), 'cheap', 1),
        ("x^3 - x^2 + x + y + z + w", x**3 - x**2 + x + y + z + w, (x, y, z, w), 'cheap', 1),
        ("1 + x^3 (the lift through e = 3)", 1 + x**3, (x,), 'cheap', 1),
    ]
    for name, e, g, tier, want in cases:
        r = test_factor(*factor_data(e, g))
        print(f"  {name}: rho {r['rho']}, k {r['k']}, {r['tier']} tier at "
              f"N = {r['N']}, {r['zeros']} zeros"
              + (f", {r['axis']} on an axis, torsion line {'yes' if r['line'] else 'no'}"
                 if r['tier'] == 'cheap' else ""))
        check(f"C0 {name}: {tier} tier, {'a zero' if want else 'no zero'}",
              r['tier'] == tier and bool(r['zeros']) == bool(want))
    # the univariate negative at the cheap tier too
    r = zeros_mod(*reduce_to_lattice(factor_data(x**3 - x + 1, (x,))[0])[:1],
                  [1, -1, 1], 1, 6)
    check("C0 x^3 - x + 1 has no zero at the cheap tier either", r == [])


def univariate_census(dmax, sizes_small_dmax):
    x = symbols('x')
    cyc = {d: Poly(sympy.cyclotomic_poly(d, x), x, domain=ZZ)
           for d in range(1, 6 * max(dmax, sizes_small_dmax) + 2)
           if sympy.totient(d) <= max(dmax, sizes_small_dmax)}

    def no_cyclotomic(p):
        D = p.degree()
        return not any(c.degree() <= D and p.rem(c).is_zero
                       for c in cyc.values())

    least = {}
    per_degree = {}
    for D in range(1, max(dmax, sizes_small_dmax) + 1):
        cnt = {}
        for inner in range(0, D):
            if D > dmax and inner + 2 > 4:
                break
            for S in itertools.combinations(range(1, D), inner):
                exps = (0,) + S + (D,)
                n = len(exps)
                p = Poly.from_dict({(e,): 1 for e in exps}, x, domain=ZZ)
                if not no_cyclotomic(p):
                    continue
                fl = p.factor_list()[1]
                if sum(m for f, m in fl) >= 2:
                    neg = any(any(c < 0 for c in f.coeffs()) for f, m in fl)
                    cnt.setdefault(n, [0, 0])
                    cnt[n][0] += 1
                    cnt[n][1] += neg
                    if n not in least:
                        least[n] = (D, p.as_expr(), [f.as_expr() for f, m in fl])
        per_degree[D] = cnt
    return per_degree, least


def stage_c1(dmax, small_dmax):
    print(f"\nC1  THE UNIVARIATE CENSUS -- 0/1 polynomials with constant term 1, "
          f"degree <= {dmax} (sizes <= 4 to {small_dmax})")
    t0 = time.time()
    per_degree, least = univariate_census(dmax, small_dmax)
    for D in sorted(per_degree):
        cnt = per_degree[D]
        if cnt:
            print(f"  degree {D}: " + ", ".join(
                f"{n} terms: {c[0]} ({c[1]} with a negative factor)"
                for n, c in sorted(cnt.items())))
    print("  least degree by term count: " + "; ".join(
        f"{n} terms at degree {least[n][0]}, {least[n][1]} = {least[n][2]}"
        for n in sorted(least)))
    print(f"  ({time.time() - t0:.0f} s)")
    below = sum(c[0] for D in range(1, min(12, dmax + 1)) for c in per_degree[D].values())
    check(f"C1 degree <= 11: {below} reducible with no cyclotomic factor", below == 0)
    if dmax >= 12:
        d12 = per_degree[12]
        tot = sum(c[0] for c in d12.values())
        neg = sum(c[1] for c in d12.values())
        check(f"C1 degree 12: {tot} = {d12.get(7, [0])[0]} at seven terms + "
              f"{d12.get(9, [0])[0]} at nine, {neg} with a negative factor",
              tot == 24 and d12.get(7, [0])[0] == 8 and d12.get(9, [0])[0] == 16
              and neg == 12)
    small = sum(c[0] for D in per_degree for n, c in per_degree[D].items() if n <= 4)
    check(f"C1 sizes <= 4 to degree {small_dmax}: {small} reducible with no "
          f"cyclotomic factor", small == 0)
    return per_degree, least


def collect_seeds(size, box):
    t0 = time.time()
    classes = {}
    nmenus = 0
    for menu in itertools.combinations(range(2, box + 1), size):
        nmenus += 1
        rows = reduced_matrix(menu)
        r = affine_rank(rows)
        if r > size // 2:
            continue
        classes.setdefault(canonical(rows), (menu, r))
    t1 = time.time()
    seeds = []
    nred = 0
    for key, (menu, r) in classes.items():
        expr, gens = poly_of(list(key))
        content, fl = sympy.factor_list(expr)
        core = [f for f, m in fl for _ in range(m) if f not in gens]
        if len(core) < 2:
            continue
        nred += 1
        negs = [Poly(f, *gens) for f in core
                if any(c < 0 for c in Poly(f, *gens).coeffs())]
        if negs:
            seeds.append((menu, r, negs))
    print(f"  size {size} over {{2..{box}}}: {nmenus} menus, {len(classes)} "
          f"classes at rank <= {size // 2}, {nred} reducible, {len(seeds)} "
          f"seeds (enumeration {t1 - t0:.0f} s, factoring {time.time() - t1:.0f} s)")
    return seeds


def stage_c2(cells):
    print("\nC2  THE MULTIVARIATE CELL -- every seed's negative factors through both tiers")
    rows = []
    for size, box in cells:
        for menu, r, negs in collect_seeds(size, box):
            core, _ = describe(menu)
            for p in negs:
                res = test_factor(p.monoms(), [int(c) for c in p.coeffs()])
                rows.append((size, box, menu, r, core, res))
    print("\nC3  THE PRINTS -- per negative factor")
    free = [row for row in rows if row[5]['tier'] == 'complete' and row[5]['zeros'] == 0]
    undecided = [row for row in rows if row[5]['tier'] == 'undecided']
    for size, box, menu, r, core, res in rows:
        tag = ("TORSION-FREE" if res['tier'] == 'complete' and res['zeros'] == 0
               else "undecided" if res['tier'] == 'undecided' else "rooted")
        extra = (f", {res['axis']} on an axis, torsion line "
                 f"{'yes' if res['line'] else 'no'}" if res['tier'] == 'cheap' else "")
        print(f"  size {size} {menu} rank {r}: k {res['k']}, rho {res['rho']}, "
              f"{res['tier']} tier at N = {res['N']}, {res['zeros']} zeros{extra} "
              f"-- {tag}; core {core}")
    kmax = max((row[5]['k'] for row in rows), default=0)
    print(f"\n  {len(rows)} negative factors over {len({row[2] for row in rows})} seeds; "
          f"largest k = {kmax}, Mann's M_k = {primorial_upto(kmax)}")
    tally = {}
    for row in rows:
        res = row[5]
        key = (row[0], res['rho'], res['k'], res['tier'])
        tally[key] = tally.get(key, 0) + 1
    for key in sorted(tally):
        print(f"  size {key[0]}, rho {key[1]}, k {key[2]}, {key[3]}: {tally[key]}")
    cheap = [row for row in rows if row[5]['tier'] == 'cheap']
    print(f"  rooted at the cheap tier: {len(cheap)}, of which "
          f"{sum(1 for row in cheap if row[5]['axis'])} have a zero on an axis and "
          f"{sum(1 for row in cheap if row[5]['line'])} contain a torsion line")
    print(f"  THE KILL AS A PRINT: {len(free)} torsion-free negative factors"
          + (": " + "; ".join(f"size {s} {m} rank {r}" for s, b, m, r, c, res in free)
             if free else ""))
    check(f"C2 no factor undecided ({len(undecided)} undecided)", not undecided)
    return rows


def main():
    rehearse = '--rehearse' in sys.argv
    t0 = time.time()
    if rehearse:
        print("REHEARSAL: boxes {2..16}, census to degree 12")
        cells = [(s, 16) for s, b in CELLS]
        dmax, small = 12, 14
    else:
        cells, dmax, small = CELLS, 16, 30
    stage_c0()
    stage_c1(dmax, small)
    stage_c2(cells)
    failed = [n for n, ok in CHECKS if not ok]
    print(f"\n{len(CHECKS) - len(failed)}/{len(CHECKS)} checks pass, "
          f"{time.time() - t0:.1f} s total")
    if failed:
        print("FAILED: " + "; ".join(failed))
        sys.exit(1)


if __name__ == '__main__':
    main()
