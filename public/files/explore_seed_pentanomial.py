"""explore_seed_pentanomial.py -- the plane's least free seed size, 5 or 6:
every non-collinear 0/1 pentanomial of the box [0,8]^2 through the
complete torsion test. (Imports the torsion instrument of
explore_seed_torsion.py and the rank machinery it rests on; reads that
file's vocabulary.)

THE QUESTION. A MENU is a finite set of integers >= 2 read as a
0/1-coefficient polynomial in the primes; its CORE is that polynomial with
the monomial content divided out; a menu is a SEED when its core has two or
more non-monomial Z-irreducible factors and one of them carries a negative
coefficient. A negative factor is TORSION-ROOTED when it vanishes at a
tuple of roots of unity and TORSION-FREE when it vanishes at none. In the
plane -- two primes, the exponents in Z^2 -- the swept boxes hold two free
seeds, both of size 6 ((1 + x)[x(1 + x^2) + y(1 - x + x^2)] and its
mirror); size 3 is collinear by the three-member criterion; size 4 is
closed off every line by the cofactor theorem (explore_seed_cofactor.py,
explore_seed_plane_floor.py); and size 5 is EMPTY in {2..24} for a reason
that says nothing in general -- every seed of those boxes has the cofactor
1 + x, which forces an even term count. So the plane's least free size is
5 or 6, and this file asks which, over a box the menu boxes never reached:
every 0/1 pentanomial in two variables with exponents in [0,8]^2, read up
to translation (the core) and the box's eight symmetries.

THE HAND-ATTACK, on paper before any engine code.

  (1) FIVE IS PRIME. P(1,1) = 5 = f(1,1) g(1,1), so any factorization has
      values (+-1, +-5) at the all-ones point, and a nonnegative split
      would need a monomial factor, which the core has not. Hence a
      reducible non-collinear pentanomial core IS a seed, with no further
      condition: the question is whether some reducible non-collinear 0/1
      pentanomial has a negative factor with no torsion zero. The value
      +-1 factor can be a positive cyclotomic (G below) or the negative
      factor (as on the line, Phi_5(x)(x^3 - x^2 + 1) = 1 + x + x^3 + x^4
      + x^7); the value-5 factor is a cyclotomic Phi_{5^a} in a monomial
      or a non-cyclotomic polynomial with that value.
  (2) THE ROW LEMMA. Suppose the core has a CYCLOTOMIC-IN-A-MONOMIAL
      factor Phi_n(w), w a monomial -- equivalently a factor containing a
      one-dimensional torsion coset. Change coordinates by GL_2(Z) so that
      w = x^d; then Phi_n(x^d) divides P iff it divides every y-row P_j(x)
      of P, and each nonzero row is a 0/1 polynomial in x with t_j terms,
      sum t_j = 5, vanishing at a primitive n-th root of unity zeta -- a
      vanishing sum of t_j roots of unity. By Mann a row of size 2 is an
      antipodal pair (n even), of size 3 a rotated 1 + w + w^2 (3 | n),
      of size 4 two pairs, of size 5 R_5 or R_2 + R_3; a row of size 1
      never vanishes. Non-collinear means two nonzero rows, so the rows
      are {2, 3}: a binomial x^a(1 + x^s) and a trinomial x^b(1 + x^t +
      x^{t'}), and every common root has order divisible by 6 (zeta^s =
      -1 and {zeta^t, zeta^{t'}} = {omega, omega^2}). So G = gcd of the
      rows is a product of Phi_{6m}'s, G(1) = 1, and the core is
      G(x) (A' + y^k B') with A' = (1 + x^s)/G, B' = (trinomial)/G,
      coprime -- the bracket irreducible at k = 1 outright and at k > 1
      by Capelli unless -A'/B' is a p-th power in Q(x) for a prime p | k
      or -4 times a fourth power, which would make B' = b^p or b^4 and
      A' = -+a^p or 4a^4 (coprime, lowest terms), impossible at the
      values A'(1) = 2 and B'(1) = 3. Consequences: (a) every seed with
      a cyclotomic-in-a-monomial factor has that factor ROOTED and
      NEGATIVE (Phi_{6m} has a negative coefficient for every m), so a
      size-5 seed all of whose negative factors are torsion-free has NO
      cyclotomic factor at all -- the shape the line's census counts
      separately, whose univariate floor is degree 12 at seven terms;
      (b) the (+-1, +-5) split is inverted against the line: G has value
      1 and the bracket has value 5, so a MIXED seed -- rooted G beside a
      torsion-free negative bracket -- is possible in principle, and
      the hand has a candidate in the box: rows 1 + x^3 and 1 + x^4 +
      x^8, G = Phi_6, bracket (1 + x) + y Phi_3(x) Phi_12(x) = 1 + x +
      y(1 + x - x^3 + x^5 + x^6), negative, coprime rows, irreducible;
      its torsion question is the instrument's.
  (3) THE NEGATIVE FACTOR OF A FREE SEED HAS RANK 2. If it were
      univariate in a monomial, f(x^d) in adapted coordinates, every
      y-row would be divisible by it; a 0/1 binomial row has only
      cyclotomic factors, a 0/1 trinomial row's non-cyclotomic part is
      irreducible or 1 (Ljunggren, Tverberg), so a torsion-free f(x^d)
      could sit in the trinomial row but never in the binomial one,
      and rows {2, 3} are the only non-collinear split. A rank-2
      +-1-coefficient factor with 3 terms always has a torsion zero (an
      R_3 with independent differences), and value +-1 forces an odd
      term count, so such a factor has 5 terms or more; the box decides
      whether a product of two such things is ever a 0/1 pentanomial.
  (4) THE FILTER, exact. A factorization's Newton polygons Minkowski-sum
      to the core's (Ostrowski), and neither summand is a point (a
      monomial factor is content; a constant one is +-1). A lattice
      polygon with primitive edge directions v_i of lattice lengths l_i
      is a sum of two lattice polygons, neither a point, iff some choice
      0 <= l'_i <= l_i, not all 0 and not all l_i, has sum l'_i v_i = 0
      (Gao and Lauder): a segment summand is the case of two antiparallel
      edges. The filter is necessary and cheap; the factorization itself
      is sympy's. Its own check: the hand candidate of (2) and the known
      rooted size-5 seed {2,16,6,24,96}, core 1 + x^3 + y(1 + x^2 + x^4)
      = Phi_6(x)[(1 + x) + y(1 + x + x^2)], both pass it.
  (5) THE HUNCH, fixed before the run and marked as such. PURE free
      (every negative factor torsion-free): ZERO in the box, the shape
      needing a product with no cyclotomic factor at all, which the
      line first reaches at seven terms. MIXED (a rooted cyclotomic
      factor beside a torsion-free negative bracket): UNKNOWN -- the
      candidate of (2) is where to look, and the count is the print.
      The size-6 witnesses are not a transplant here: their cofactor
      1 + x is exactly what an odd size forbids.

THE RIG.
  S0 CONTROLS, read before any census number: the two known size-5 seeds
     of the box -- the rooted {2,16,6,24,96} and the hand candidate --
     pass the polygon filter, factor as (2) says, and print their
     verdicts; the size-6 free witness prints free and the line's
     1 + x + x^3 + x^4 + x^7 prints its negative factor free through this
     file's own pipeline (both outside the box's enumeration, run
     directly); 1 + x + x^2 + y (irreducible) is filtered or irreducible.
  S1 THE ENUMERATION: every 5-subset of [0,8]^2 with min x = 0 and min
     y = 0 (the cores), affine rank 2, through the polygon filter;
     survivors reduced to one representative per orbit of the box's
     dihedral group (x <-> y, x -> 8 - x, y -> 8 - y, re-normalized).
     Printed: the subset count, the non-collinear count, the survivors,
     the orbit representatives.
  S2 THE FACTORIZATION: every representative factored over Z (sympy);
     the reducible ones are the seeds. Printed: the seed count, that
     every seed has a negative factor (the check of (1)), the split of
     the seeds by whether some factor is cyclotomic in a monomial (a
     rank-1 factor with a torsion zero) -- the row-lemma shape -- and
     for those the check that the rows in the factor's direction are of
     sizes 2 and 3.
  S3 THE KILL: every negative factor of every seed through the complete
     torsion tier. Printed per seed: the exponent set, the factors, the
     verdict per negative factor with its tier, rho, k, N and zero count;
     then the three counts -- PURE FREE (every negative factor free),
     MIXED (a rooted and a free negative factor), ROOTED (every negative
     factor rooted) -- and the witnesses of the first two by name.

THE PREDICTIONS, FIXED BEFORE THE RUN -- every kill is a printed count.
  K0  CONTROLS: as named in S0; the rooted size-5 seed prints rooted, the
      size-6 witness free, the line's witness free.
  K1  THE FILTER passes both size-5 controls and every seed found at S2
      (a seed failing the filter is a bug in the filter, printed).
  K2  EVERY reducible non-collinear core is a seed (the count of
      reducible cores with no negative factor is 0).
  K3  EVERY seed with a cyclotomic-in-a-monomial factor has rows {2, 3}
      in that factor's direction and that factor rooted (the row lemma,
      vacuous if none, a printed contradiction if it fails).
  K4  THE KILL: PURE FREE = 0 (the hunch). One or more -> the plane's
      least free size is 5 outright, the witness named and its freedom
      re-derived by hand where the moduli argument reaches it. MIXED is
      a count with no hunch: nonzero names the least size at which the
      plane holds a torsion-free negative factor at all, beside a rooted
      one; zero says the mixed shape's brackets are all rooted in this
      box.

RESOURCE ENVELOPE. C(81, 5) = 25.6 million subsets iterated, about a
fifth normalized, the polygon filter at tens of microseconds each; sympy
bivariate factoring at ~1 ms per survivor. Estimated 10 to 20 minutes,
memory under 300 MB (the survivor set held as tuples). A rehearsal flag
(--rehearse) runs the box [0,5]^2 first. Run:
python explore_seed_pentanomial.py [--rehearse]

FINDINGS (the recorded run, 12 of 12 checks, 323.0 s -- the enumeration
137.6 s, the factoring 145.3 s; every figure below is that run's print.
The rehearsal at [0,5]^2 held 14 seeds, all rooted, in 7.5 s.)

  F1  THE PLANE FIRST HOLDS A TORSION-FREE NEGATIVE FACTOR AT SIZE 5
      (theorem by exhibit). The hand candidate of (2) factors as
      (x^2 - x + 1)(x^6 y + x^5 y - x^3 y + x y + x + y + 1) and its
      bracket prints FREE at the complete tier (rho = 2, k = 7, N = 1260,
      0 zeros) beside Phi_6 rooted (cheap tier, 2 zeros mod 6): a MIXED
      seed. By hand, stronger than the print: on |x| = 1 write t = 2 +
      2 cos theta; |1 + x|^2 = t, |Phi_3(x)|^2 = (t - 1)^2, |Phi_12(x)|^2
      = (t^2 - 4t + 1)^2, so the two coefficients of the bracket have
      equal moduli iff t^6 - 10t^5 + 35t^4 - 52t^3 + 35t^2 - 11t + 1 = 0,
      a Z-irreducible sextic with two non-real roots (0.495 +- 0.323 i)
      and four real ones (0.144, 1.446, 3.501, 3.918), none of which is
      totally real, hence none of the form 2 + 2 cos(2 pi k / n). So no
      root of unity x makes the moduli agree and the bracket has no
      torsion zero; it does meet the unit torus, at the four real roots,
      at non-torsion points -- the size-6 witnesses' picture.
  F2  THE BOX (observation, [0,8]^2): 25,621,596 subsets, 5,263,020
      cores, 5,262,736 non-collinear, 1,228,232 through the polygon
      filter, 154,643 orbit representatives, 130 seeds -- every one
      with a negative factor (K2), every one passing the filter (K1),
      and EVERY ONE with a cyclotomic-in-a-monomial factor, rows {2, 3}
      in its direction and that factor negative (K3, the row lemma at
      130 of 130). THE KILL: PURE FREE 0, the hunch; MIXED 33; rooted 97.
  F3  THREE IDENTITIES AND NOTHING ELSE, in lattice coordinates along the
      cyclotomic direction: rows (1 + w^3; 1 + w^2 + w^4) -> rooted, 79
      (Phi_6(w) times (1 + w) + m Phi_3(w), the bracket positive); rows
      (1 + w^6; 1 + w^4 + w^8) -> rooted, 18 (Phi_12(w) times (1 + w^2)
      + m Phi_3(w) Phi_6(w), positive); rows (1 + w^3; 1 + w^4 + w^8) ->
      MIXED, 33 (Phi_6(w) times (1 + w) + m Phi_3(w) Phi_12(w), the
      bracket negative and free). So the box holds ONE torsion-free
      negative factor up to lattice equivalence, w running over x, y
      and xy and m over the offsets the box allows; the binomial row's
      exponent is 3 or 6 because a common root of the rows has order
      6m dividing 2s, and s <= 8 in the box. The first S4 print used
      v . p for the row coordinate and read 11 distinct brackets off
      the reduction's basis orientation; the lattice coordinate and the
      row-shape argument replaced it.

  TIER. The size-5 free factor is a THEOREM BY EXHIBIT (the hand proof of
  F1, the instrument agreeing); the row lemma is PROVED in the docstring
  and checked at 130 of 130; the box counts are OBSERVATION. What stays
  open: whether a size-5 seed is ever free OUTRIGHT -- by the row lemma
  such a core has no cyclotomic factor at all, which the line first
  reaches at seven terms and this box never reaches at five.
"""
import os
import sys
import time
from itertools import combinations
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy
from sympy import Poly, symbols

from explore_seed_rank_law import CHECKS, check
from explore_seed_torsion import test_factor, factor_data

x, y = symbols('x y')
GENS = (x, y)


# ------------------------------------------------------------ the filter
def hull(pts):
    """Convex hull, counter-clockwise, of a list of lattice points."""
    pts = sorted(set(pts))
    if len(pts) <= 2:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def edges_of(h):
    """(primitive direction, lattice length) per edge of a hull."""
    out = []
    n = len(h)
    for i in range(n):
        dx = h[(i + 1) % n][0] - h[i][0]
        dy = h[(i + 1) % n][1] - h[i][1]
        g = gcd(abs(dx), abs(dy))
        out.append(((dx // g, dy // g), g))
    return out


Z, F, ZF, M = 0, 1, 2, 3  # all-zero so far, all-full, both (vacuous), mixed


def decomposable(pts):
    """Gao-Lauder: the hull is a Minkowski sum of two lattice polygons,
    neither a point, iff a sub-choice of edge lengths closes up."""
    h = hull(pts)
    if len(h) <= 2:
        # a segment: decomposable iff its lattice length is >= 2
        return len(h) == 2 and edges_of(h)[0][1] >= 2
    states = {(0, 0, ZF)}
    for (vx, vy), l in edges_of(h):
        nxt = set()
        for sx, sy, st in states:
            for lp in range(l + 1):
                if lp == 0:
                    ns = {ZF: Z, Z: Z, F: M, M: M}[st]
                elif lp == l:
                    ns = {ZF: F, F: F, Z: M, M: M}[st]
                else:
                    ns = M
                nxt.add((sx + lp * vx, sy + lp * vy, ns))
        states = nxt
    return (0, 0, M) in states


def affine_rank2(pts):
    p0 = pts[0]
    for a in pts[1:]:
        for b in pts[1:]:
            if (a[0] - p0[0]) * (b[1] - p0[1]) - (a[1] - p0[1]) * (b[0] - p0[0]):
                return True
    return False


# ---------------------------------------------------------- the symmetry
def normalize(pts):
    mx = min(p[0] for p in pts)
    my = min(p[1] for p in pts)
    return tuple(sorted((p[0] - mx, p[1] - my) for p in pts))


def canonical(pts):
    best = None
    for sx in (1, -1):
        for sy in (1, -1):
            for swap in (False, True):
                q = [(sx * p[0], sy * p[1]) for p in pts]
                if swap:
                    q = [(b, a) for a, b in q]
                c = normalize(q)
                if best is None or c < best:
                    best = c
    return best


# -------------------------------------------------------- the factoring
def poly_of(pts):
    return sum(x ** i * y ** j for i, j in pts)


def factors_of(P):
    _, fl = sympy.factor_list(Poly(P, x, y))
    out = []
    for f, e in fl:
        out.extend([f] * e)
    return out


def negative(f):
    return any(c < 0 for c in f.coeffs())


def direction_of(f):
    """The primitive direction of a rank-1 factor's exponents."""
    ms = f.monoms()
    dx = ms[1][0] - ms[0][0]
    dy = ms[1][1] - ms[0][1]
    g = gcd(abs(dx), abs(dy))
    return (dx // g, dy // g)


def row_sizes(pts, v):
    """Sizes of the rows of pts transverse to direction v: points grouped
    by the value of the linear form vanishing on v."""
    rows = {}
    for i, j in pts:
        key = v[1] * i - v[0] * j
        rows[key] = rows.get(key, 0) + 1
    return sorted(rows.values())


def fmt(d):
    tag = 'UNDECIDED' if d['zeros'] is None else ('FREE' if d['zeros'] == 0 else 'rooted')
    return f"{tag} [{d['tier']}, rho={d['rho']}, k={d['k']}, N={d['N']}, zeros={d['zeros']}]"


def verdicts(P):
    """(factors, [(factor, verdict dict)] for the negative ones)."""
    fs = factors_of(P)
    negs = [(f, test_factor(*factor_data(f.as_expr(), GENS))) for f in fs if negative(f)]
    return fs, negs


def classify(negs):
    frees = [d['zeros'] == 0 for _, d in negs]
    if not frees:
        return 'no negative factor'
    if all(frees):
        return 'PURE FREE'
    if any(frees):
        return 'MIXED'
    return 'rooted'


# ------------------------------------------------------------ the stages
def stage_s0():
    print("S0 controls")
    rooted5 = [(0, 0), (3, 0), (0, 1), (2, 1), (4, 1)]
    cand5 = [(0, 0), (3, 0), (0, 1), (4, 1), (8, 1)]
    for name, pts in (("rooted size-5 {2,16,6,24,96}", rooted5),
                      ("hand candidate 1+x^3+y(1+x^4+x^8)", cand5)):
        ok = decomposable(pts)
        fs, negs = verdicts(poly_of(pts))
        print(f"  {name}: filter={'pass' if ok else 'FAIL'}; factors {fs}")
        for f, d in negs:
            print(f"    negative {f.as_expr()}: {fmt(d)}")
        check(f"S0 filter passes {name}", ok)
        check(f"S0 {name} reducible", len(fs) >= 2)
        if name.startswith("rooted"):
            check("S0 rooted control prints rooted", classify(negs) == 'rooted')
    six = (1 + x) * (x * (1 + x ** 2) + y * (1 - x + x ** 2))
    fs, negs = verdicts(sympy.expand(six))
    print(f"  size-6 witness: factors {fs}")
    for f, d in negs:
        print(f"    negative {f.as_expr()}: {fmt(d)}")
    check("S0 size-6 witness prints free", classify(negs) == 'PURE FREE')
    line = 1 + x + x ** 3 + x ** 4 + x ** 7
    fs, negs = verdicts(line)
    print(f"  line witness 1+x+x^3+x^4+x^7: factors {fs}")
    for f, d in negs:
        print(f"    negative {f.as_expr()}: {fmt(d)}")
    check("S0 line witness prints free", classify(negs) == 'PURE FREE')
    tri = [(0, 0), (1, 0), (2, 0), (0, 1)]
    fs = factors_of(poly_of(tri))
    print(f"  1+x+x^2+y: filter={'pass' if decomposable(tri) else 'fail'}, factors {len(fs)}")
    check("S0 1+x+x^2+y irreducible", len(fs) == 1)


def stage_s1(B):
    print(f"S1 enumeration over [0,{B}]^2")
    t0 = time.time()
    grid = [(i, j) for i in range(B + 1) for j in range(B + 1)]
    n_sub = n_norm = n_rank2 = n_pass = 0
    reps = set()
    for c in combinations(range(len(grid)), 5):
        n_sub += 1
        pts = [grid[k] for k in c]
        if min(p[0] for p in pts) or min(p[1] for p in pts):
            continue
        n_norm += 1
        if not affine_rank2(pts):
            continue
        n_rank2 += 1
        if not decomposable(pts):
            continue
        n_pass += 1
        reps.add(canonical(pts))
    print(f"  subsets {n_sub}, cores {n_norm}, non-collinear {n_rank2}, "
          f"filter survivors {n_pass}, orbit representatives {len(reps)} "
          f"({time.time() - t0:.1f} s)")
    return sorted(reps)


def stage_s2_s3(reps):
    print(f"S2 factorization of {len(reps)} representatives")
    t0 = time.time()
    seeds = []
    no_negative = 0
    for pts in reps:
        fs = factors_of(poly_of(pts))
        if len(fs) >= 2:
            seeds.append((pts, fs))
            if not any(negative(f) for f in fs):
                no_negative += 1
    print(f"  seeds {len(seeds)}, reducible cores with no negative factor "
          f"{no_negative} ({time.time() - t0:.1f} s)")
    check("K2 every reducible non-collinear core is a seed", no_negative == 0)

    print("S3 the torsion verdicts")
    counts = {'PURE FREE': 0, 'MIXED': 0, 'rooted': 0}
    witnesses = {'PURE FREE': [], 'MIXED': []}
    row_lemma_ok = True
    n_cyc = 0
    filter_ok = True
    for pts, fs in seeds:
        if not decomposable(list(pts)):
            filter_ok = False
        negs = []
        cyc_dirs = []
        for f in fs:
            d = test_factor(*factor_data(f.as_expr(), GENS))
            if d['rho'] == 1 and d['zeros'] not in (0, None):
                cyc_dirs.append((f, direction_of(f)))
                if not negative(f):
                    row_lemma_ok = False
            if negative(f):
                negs.append((f, d))
        if cyc_dirs:
            n_cyc += 1
            for f, v in cyc_dirs:
                if row_sizes(pts, v) != [2, 3]:
                    row_lemma_ok = False
                    print(f"  ROW LEMMA FAILS at {pts}: factor {f.as_expr()}, "
                          f"rows {row_sizes(pts, v)}")
        cls = classify(negs)
        counts[cls] += 1
        if cls != 'rooted':
            witnesses[cls].append((pts, fs, negs))
        print(f"  {list(pts)} = {' * '.join(str(f.as_expr()) for f in fs)}  -> {cls}")
        for f, d in negs:
            print(f"      negative {f.as_expr()}: {fmt(d)}")
    print(f"  seeds with a cyclotomic-in-a-monomial factor: {n_cyc} of {len(seeds)}")
    check("K1 the filter passes every seed", filter_ok)
    check("K3 the row lemma: rows {2,3} and the cyclotomic factor negative",
          row_lemma_ok)
    print(f"  THE KILL: PURE FREE {counts['PURE FREE']}, MIXED {counts['MIXED']}, "
          f"rooted {counts['rooted']}")
    for cls in ('PURE FREE', 'MIXED'):
        for pts, fs, negs in witnesses[cls]:
            print(f"    {cls}: {list(pts)} = "
                  f"{' * '.join(str(f.as_expr()) for f in fs)}")
    check("K4 pure free count printed", True)
    stage_s4(seeds)
    return counts


def stage_s4(seeds):
    """THE ROW SHAPES, added after the first run for the reading: every
    seed's rows in the direction of its cyclotomic factor -- the binomial
    row 1 + w^s and the trinomial row 1 + w^t + w^t' -- tallied with the
    verdict. The row exponents are LATTICE coordinates along the
    direction, (v . (p - p0)) / (v . v), so the same identity in the
    direction xy reads as it does in x. Up to GL_2(Z) and translation the
    bracket is determined by the row shape (s; t, t') alone -- the rows'
    offset monomial is the second basis vector -- so the number of
    distinct mixed row shapes is the number of distinct free factors the
    box holds up to lattice equivalence."""
    print("S4 the row shapes (lattice coordinates along the cyclotomic direction)")
    tally = {}
    for pts, fs in seeds:
        cyc = [f for f in fs if test_factor(*factor_data(f.as_expr(), GENS))['rho'] == 1]
        f = cyc[0]
        v = direction_of(f)
        vv = v[0] * v[0] + v[1] * v[1]
        rows = {}
        for i, j in pts:
            rows.setdefault(v[1] * i - v[0] * j, []).append(v[0] * i + v[1] * j)
        shape = []
        for key in rows:
            e = sorted(rows[key])
            assert all((a - e[0]) % vv == 0 for a in e)
            shape.append(tuple((a - e[0]) // vv for a in e))
        shape = tuple(sorted(shape, key=len))
        negs = [(g, test_factor(*factor_data(g.as_expr(), GENS))) for g in fs if negative(g)]
        cls = classify(negs)
        tally[(shape, cls)] = tally.get((shape, cls), 0) + 1
    for (shape, cls), n in sorted(tally.items(), key=lambda kv: (-kv[1], str(kv[0]))):
        print(f"  rows {shape} -> {cls}: {n}")
    mixed_shapes = {shape for (shape, cls) in tally if cls == 'MIXED'}
    print(f"  distinct free brackets up to lattice equivalence: {len(mixed_shapes)} "
          f"{sorted(mixed_shapes)}")


def main():
    rehearse = '--rehearse' in sys.argv
    B = 5 if rehearse else 8
    t0 = time.time()
    stage_s0()
    reps = stage_s1(B)
    stage_s2_s3(reps)
    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_ok} of {len(CHECKS)} checks passed, {time.time() - t0:.1f} s")


if __name__ == '__main__':
    main()
