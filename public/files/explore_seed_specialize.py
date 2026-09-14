"""explore_seed_specialize.py -- is the plane's size-5 question a
different question from the line's? Whether a free size-5 seed in two
variables specializes, along y -> x^K, to a 0/1 pentanomial in one
variable whose non-cyclotomic part is reducible. (Imports the
seed enumeration and factoring of explore_seed_pentanomial.py and the
torsion instrument of explore_seed_torsion.py; reads their vocabulary.)

THE QUESTION. explore_seed_pentanomial.py left one front: whether a
size-5 seed -- a non-collinear 0/1 pentanomial core with two or more
non-monomial Z-irreducible factors, one negative -- is ever FREE
OUTRIGHT, every negative factor vanishing at no tuple of roots of
unity. The box [0,8]^2 holds none among its 130 seeds, and the row
lemma proved there says such a core has no factor containing a
one-dimensional torsion coset (a cyclotomic polynomial in a monomial),
since at size 5 any such factor is a product of Phi_{6m}'s, negative and
rooted. On the line the same question is Filaseta and Solan's (Math.
Scand. 84, 1999): is the non-cyclotomic part of every 0/1 pentanomial 1
or irreducible? This file asks whether the plane's question is a
DIFFERENT question, and the answer is no.

THE THEOREM, proved before the engine (the cofactor theorem's own
route, explore_seed_cofactor.py, run once more at size 5).

  Let F be a free size-5 seed in Z[x, y], F = F_1 ... F_m the
  factorization into non-monomial Z-irreducible factors, m >= 2. At
  (1, 1) the values multiply to 5, so exactly one factor has value
  +-5 and the rest +-1; a factor with no negative coefficient has
  value at least 2 unless it is a monomial, so at most ONE factor is
  positive, and then it has value 5. For K larger than the spread of
  F's x-exponents the substitution y -> x^K sends distinct exponent
  vectors to distinct exponents, so F(x, x^K) is a 0/1 pentanomial,
  each F_i(x, x^K) is non-constant and non-monomial, and the
  factorization survives.
  (i) A NEGATIVE factor is torsion-free (the seed is free), so
      F_i(x, x^K) has no cyclotomic factor at ANY K: a root of unity
      zeta with F_i(zeta, zeta^K) = 0 is a torsion zero of F_i.
  (ii) If two or more factors are negative, F(x, x^K) has two
      non-constant factors with no cyclotomic factor between them, so
      its non-cyclotomic part is reducible at every K past the spread.
  (iii) Otherwise m = 2, F = G H with G positive of value 5 and H
      negative. G(x, x^K) is a product of cyclotomic polynomials at
      only finitely many K. Suppose not. G has positive y-degree (a G
      in x alone with a cyclotomic factor Phi_n(x) contains the
      torsion line x = zeta_n, which the row lemma forbids in a free
      seed), so G(x, x^K) has degree at least K and, past the spread,
      exactly G's own t monomials as terms, t fixed by G and not by K
      (a factor can carry more monomials than the pentanomial it
      divides), and by Hajos's lemma (a polynomial with t terms has no
      nonzero root of multiplicity t or more) at least K/(t - 1)
      DISTINCT roots of unity zeta, each a torsion point (zeta, zeta^K)
      on the irreducible curve G = 0. Over the infinite set of such K
      the curve carries infinitely many torsion points, so it contains
      a torsion coset of positive dimension (Ihara-Serre-Tate; Laurent
      1984), so G is a cyclotomic polynomial in a monomial, and the row
      lemma makes that factor negative: a contradiction. Hence past
      finitely many K the non-cyclotomic part of F(x, x^K) is the
      non-cyclotomic part of G(x, x^K), non-constant, times
      H(x, x^K), non-constant and cyclotomic-free: reducible.
  So a free size-5 seed in the plane hands the line, at every large K,
  a 0/1 pentanomial whose non-cyclotomic part is reducible -- a NO to
  the Filaseta-Solan question -- and if that question's answer is YES
  the plane's least free size is 6, the two size-6 witnesses of
  explore_seed_torsion.py being the floor. A line witness whose
  cyclotomic part has no negative coefficient is itself a free
  collinear seed, so the plane adds no witness the line does not
  already need. Filaseta and Solan's
  THEOREM (the reciprocal reading) adds the shape: the reducible part
  at each such K carries a non-cyclotomic RECIPROCAL factor.

  Marked as transplant: none. The cofactor theorem's specialization
  argument is the same move at size 4, where Mills's theorem stood
  where Filaseta-Solan's question stands here; the size-5 route needs
  the row lemma at both ends (no torsion line in a free seed, a
  torsion-coset factor forced negative) and Hajos's bound at t = 5.

THE RIG. Every step of the proof that is a printable instance is
printed at the box's own seeds, so the argument is exercised where a
mis-step would show. Specializations are factored over Z by sympy and
a factor is cyclotomic iff Poly.is_cyclotomic.

  S0 CONTROLS, read before any census figure. (a) A factor that IS a
     torsion coset, 1 + xy, specializes to 1 + x^(K+1), all-cyclotomic
     at every K = 1..60 (the coset step's positive control). (b) The
     size-6 free bracket x(1 + x^2) + y(1 - x + x^2), torsion-free by
     explore_seed_torsion.py's proof, specializes cyclotomic-free at
     every K = 1..60 (step (i)). (c) The line's own witness
     1 + x + x^3 + x^4 + x^7 = Phi_5(x)(x^3 - x^2 + 1) prints its
     non-cyclotomic part irreducible (the Filaseta-Solan shape, YES).
     (d) Hajos: the largest multiplicity of a nonzero root over every
     specialization the run factors, at most t - 1 at a t-term
     polynomial, so at most 4 at the pentanomials of S4 and at most
     one less than the term count at the factors of S2 and S3, every
     one of which has five terms or fewer in the box.
  S1 THE BOX: explore_seed_pentanomial.py's enumeration and factoring
     over [0,B]^2 (B = 8; --rehearse runs B = 5), the seeds collected
     with their factors and each factor's sign.
  S2 STEP (i) AT EVERY TORSION-FREE FACTOR: every negative factor that
     the instrument reads torsion-free (the 33 mixed brackets at B = 8)
     specialized at K = 1..60; the count of (factor, K) with a
     cyclotomic factor.
  S3 STEP (iii) AT EVERY POSITIVE FACTOR: every positive factor (the
     97 rooted seeds' brackets at B = 8) specialized at K = 1..60; the
     count of (factor, K) that are all-cyclotomic, and the largest such
     K -- the theorem says finitely many, and the print says how many.
  S4 THE REDUCTION ON THE BOX: every seed specialized at K = B+1..B+4,
     the term count checked at 5 with every coefficient 1, and the
     non-cyclotomic part's irreducible-factor count printed; the number
     of (seed, K) with a reducible non-cyclotomic part, which would be
     a Filaseta-Solan NO witness at degree at most B + (B+4)B.

THE PREDICTIONS, fixed before the run, every kill a printed count.
  K0  CONTROLS as named in S0: (a) 60 of 60 all-cyclotomic, (b) 0 of 60
      with a cyclotomic factor, (c) one non-cyclotomic factor, (d) at
      most 4.
  K1  S2 prints 0: a cyclotomic factor at a torsion-free factor's
      specialization is a torsion zero the instrument missed -- the
      instrument or step (i) is wrong, and nothing below is read.
  K2  S3 prints a finite count with a largest K well below 60; the
      hunch is 0 at every K past the spread, and a count that GROWS
      with the K range is the coset step wrong.
  K3  S4 prints 0 reducible non-cyclotomic parts (a transplant from the
      line's census, which is exhaustive to degree 70 while these reach
      degree 104): a nonzero count is a Filaseta-Solan witness, named
      and its factorization printed, a finding and not a bug.

RESOURCE ENVELOPE. The enumeration and factoring are the parent rig's
(about 5 minutes, under 300 MB); the specializations are about 10^4
univariate factorizations at degree at most 500, milliseconds each.
Run: python explore_seed_specialize.py [--rehearse]

FINDINGS (the recorded run, 9 of 9 checks, 324.2 s -- the parent's
enumeration 129.7 s and factoring 155.3 s; every figure below is that
run's print. The rehearsal at [0,5]^2: 14 seeds, 9 of 9, 7.9 s.)

  F1  THE CONTROLS HOLD (K0): 1 + xy all-cyclotomic at 60 of 60 K; the
      size-6 free bracket with a cyclotomic factor at 0 of 60 K; the
      line's witness Phi_5 times one non-cyclotomic factor; (d) every
      specialization's multiplicity below its own term count, the
      largest multiplicity 1 and the largest term count 7 -- the mixed
      bracket (1 + w) + m Phi_3(w) Phi_12(w), which is why the bound is
      read at a factor's own count and never at the pentanomial's five.
  F2  THE BOX AGAIN (S1): 130 seeds, 97 with a positive factor, 33 with
      two or more negative factors (the mixed shape, Phi_6 beside its
      free bracket), no seed with two positive factors.
  F3  STEP (i) AT 33 OF 33 (K1): the 33 torsion-free brackets specialize
      cyclotomic-free at every K = 1..60, 0 of 1980 pairs.
  F4  STEP (iii) AT 97 OF 97 (K2): the positive brackets are
      all-cyclotomic at 47 of 5820 pairs, the largest such K = 16 and
      none past it -- finitely many, as the coset step says, and NOT
      zero: x^2 + xy + x + y + 1 at K = 3 is Phi_5(x), and the rooted
      bracket (1 + w) + m Phi_3(w) folds onto a cyclotomic at small K
      whenever the offset's exponent lines the two rows up.
  F5  THE REDUCTION ON THE BOX (K3): at 520 (seed, K) pairs, K = 9..12,
      every specialization is a 0/1 pentanomial, its non-cyclotomic
      part is 1 at 2 pairs and irreducible at the other 518, reducible
      at none -- the Filaseta-Solan YES at degrees the line's census
      (to 70) does not reach, 520 pentanomials from 130 seeds, of
      degree at most 104.

  TIER. The specialization theorem is PROVED in the docstring and its
  three printable steps checked at 33, 97 and 130 instances; the
  Filaseta-Solan reading at K = 9..12 is an observation. The front
  moves: the plane holds a free size-5 seed only if the line hands
  Filaseta and Solan a NO.
"""
import os
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy
from sympy import Poly, symbols, factor_list

from explore_seed_rank_law import CHECKS, check
from explore_seed_pentanomial import stage_s1 as enumerate_box
from explore_seed_pentanomial import factors_of, poly_of, negative, x, y, GENS
from explore_seed_torsion import test_factor, factor_data

KMAX = 60


def specialize(f, K):
    """f(x, x^K) as a univariate Poly over Z."""
    return Poly(f.as_expr().subs(y, x ** K), x)


HAJOS = dict(mult=0, terms=0, ok=True)  # the (d) control, fed by split


def split(p):
    """(cyclotomic factors, non-cyclotomic factors, max nonzero-root
    multiplicity) of a univariate Poly, monomial content dropped; the
    multiplicity is read against the polynomial's own term count."""
    _, fl = factor_list(p)
    cyc, non, mult = [], [], 0
    for f, e in fl:
        q = Poly(f, x)
        if q.degree() == 0 or q.as_expr() == x:
            continue
        mult = max(mult, e)
        (cyc if q.is_cyclotomic else non).append((q, e))
    nt = len(p.terms())
    HAJOS['mult'] = max(HAJOS['mult'], mult)
    HAJOS['terms'] = max(HAJOS['terms'], nt)
    if mult >= nt:
        HAJOS['ok'] = False
    return cyc, non, mult


def is_torsion_free(f):
    v = test_factor(*factor_data(f.as_expr(), GENS))
    return v['tier'] == 'complete' and v['zeros'] == 0


def stage_s0():
    print("S0 controls")
    a = Poly(1 + x * y, x, y)
    n_a = sum(1 for K in range(1, KMAX + 1) if not split(specialize(a, K))[1])
    print(f"  (a) 1 + xy all-cyclotomic at {n_a} of {KMAX} K")
    check("K0a the torsion coset specializes all-cyclotomic at every K", n_a == KMAX)
    b = Poly(x * (1 + x ** 2) + y * (1 - x + x ** 2), x, y)
    n_b = sum(1 for K in range(1, KMAX + 1) if split(specialize(b, K))[0])
    print(f"  (b) the size-6 free bracket carries a cyclotomic factor at {n_b} of {KMAX} K")
    check("K0b the torsion-free bracket specializes cyclotomic-free at every K", n_b == 0)
    c = Poly(1 + x + x ** 3 + x ** 4 + x ** 7, x)
    cyc, non, _ = split(c)
    print(f"  (c) 1 + x + x^3 + x^4 + x^7: cyclotomic {[str(q.as_expr()) for q, _ in cyc]}, "
          f"non-cyclotomic factors {len(non)}")
    check("K0c the line's witness has one non-cyclotomic factor", len(non) == 1)
    return 0


def stage_s1(B):
    reps = enumerate_box(B)
    print(f"S1 factoring {len(reps)} representatives")
    t0 = time.time()
    seeds = []
    for pts in reps:
        fs = factors_of(poly_of(pts))
        if len(fs) >= 2:
            seeds.append((pts, fs))
    n_pos = sum(1 for _, fs in seeds for f in fs if not negative(f))
    print(f"  seeds {len(seeds)}, positive factors {n_pos}, "
          f"seeds with two or more negative factors "
          f"{sum(1 for _, fs in seeds if sum(negative(f) for f in fs) >= 2)} "
          f"({time.time() - t0:.1f} s)")
    check("S1 no seed has two positive factors",
          all(sum(not negative(f) for f in fs) <= 1 for _, fs in seeds))
    return seeds


def stage_s2(seeds):
    print("S2 step (i): every torsion-free negative factor specialized")
    free = [f for _, fs in seeds for f in fs if negative(f) and is_torsion_free(f)]
    bad = 0
    mult = 0
    for f in free:
        for K in range(1, KMAX + 1):
            cyc, _, m = split(specialize(f, K))
            mult = max(mult, m)
            bad += bool(cyc)
    print(f"  torsion-free negative factors {len(free)}, (factor, K) pairs with a "
          f"cyclotomic factor {bad} of {len(free) * KMAX}")
    check("K1 a torsion-free factor never specializes onto a cyclotomic factor", bad == 0)
    return mult


def stage_s3(seeds):
    print("S3 step (iii): every positive factor specialized")
    pos = [f for _, fs in seeds for f in fs if not negative(f)]
    allcyc = []
    mult = 0
    for f in pos:
        for K in range(1, KMAX + 1):
            _, non, m = split(specialize(f, K))
            mult = max(mult, m)
            if not non:
                allcyc.append((f.as_expr(), K))
    kmax = max((K for _, K in allcyc), default=0)
    print(f"  positive factors {len(pos)}, all-cyclotomic (factor, K) pairs "
          f"{len(allcyc)} of {len(pos) * KMAX}, largest such K {kmax}")
    for expr, K in allcyc[:10]:
        print(f"    {expr} at K = {K}")
    check("K2 a positive factor is all-cyclotomic at finitely many K, none past 20",
          kmax <= 20)
    return mult


def stage_s4(seeds, B):
    print(f"S4 the reduction: every seed at K = {B + 1}..{B + 4}")
    n_pairs = n_red = n_one = 0
    mult = 0
    shape_ok = True
    for pts, fs in seeds:
        F = Poly(poly_of(pts), x, y)
        for K in range(B + 1, B + 5):
            p = specialize(F, K)
            if len(p.terms()) != 5 or any(c != 1 for c in p.coeffs()):
                shape_ok = False
            cyc, non, m = split(p)
            mult = max(mult, m)
            n_pairs += 1
            if len(non) == 0:
                n_one += 1
            if len(non) >= 2:
                n_red += 1
                print(f"    WITNESS {pts} at K = {K}: {[str(q.as_expr()) for q, _ in non]}")
    print(f"  (seed, K) pairs {n_pairs}, non-cyclotomic part 1 at {n_one}, "
          f"reducible at {n_red}; every specialization a 0/1 pentanomial: {shape_ok}")
    check("S4 every specialization is a 0/1 pentanomial", shape_ok)
    check("K3 no seed of the box specializes to a Filaseta-Solan witness", n_red == 0)
    return mult


def main():
    rehearse = '--rehearse' in sys.argv
    B = 5 if rehearse else 8
    t0 = time.time()
    stage_s0()
    seeds = stage_s1(B)
    m2 = stage_s2(seeds)
    m3 = stage_s3(seeds)
    m4 = stage_s4(seeds, B)
    print(f"S0(d) largest nonzero-root multiplicity over every specialization "
          f"{HAJOS['mult']}, largest term count {HAJOS['terms']}, every "
          f"multiplicity below its own term count: {HAJOS['ok']}")
    check("K0d Hajos: every specialization's multiplicity is below its term count",
          HAJOS['ok'] and max(m2, m3, m4) == HAJOS['mult'])
    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_ok} of {len(CHECKS)} checks passed, {time.time() - t0:.1f} s")


if __name__ == '__main__':
    main()
