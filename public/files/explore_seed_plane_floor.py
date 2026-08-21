"""explore_seed_plane_floor.py -- the plane's own floor for a free seed: the
43 non-collinear size-4 seeds of {2..32} through the torsion test. (Imports
the torsion instrument of explore_seed_torsion.py and the size-4 census of
explore_seed_shape.py; reads both vocabularies.)

THE QUESTION. A MENU is a finite set of integers >= 2 read as a
0/1-coefficient polynomial in the primes; its CORE is that polynomial with
the monomial content divided out; a menu is a SEED when its core carries a
Z-irreducible factor with a negative coefficient. A negative factor is
TORSION-ROOTED when it vanishes at a tuple of roots of unity and
TORSION-FREE when it vanishes at none; a seed is rooted or free by its
negative factor. Along a line the least size of a free seed is 3 (the
trinomial {2,32,64}, 1 + x^4 + x^5 = (1 + x + x^2)(x^3 - x + 1)); in the
plane the swept boxes hold two free seeds, both of size 6, and the torsion
cells ran sizes 5 to 9 and never asked size 4. A size-3 seed is collinear
by the three-member criterion, so off every line the least free size is 4
or more. The size-4 census of {2..32} holds 44 seeds among 31,465 menus,
exactly one collinear ({2,4,16,32}). This file puts the other 43 through
the complete torsion test. The kill is a print: the number of torsion-free
negative factors among them, with their seeds.

THE HAND-ATTACK, on paper before any engine code.

  (1) WHAT A SIZE-4 SEED IS. The term-count law: in a nonnegative
      factorization of a 0/1 polynomial the term counts multiply and both
      factors are 0/1. At size 4 the non-seed reducible cores are
      therefore products of two 0/1 binomials and nothing else; a size-4
      seed's core is Z-reducible with a negative factor by definition, and
      since P(1) = 4 = f(1) g(1), a two-factor core has (f(1), g(1)) in
      {(1,4), (2,2), (4,1)} -- a negative factor can evaluate to 1 at the
      all-ones point (x^3 - x + 1 does) or to 2 (x^2 - xy + y^2 + 1 does).
  (2) THE PAIRING LEMMA. A four-term 0/1 polynomial P vanishes at a torsion
      point chi iff its four monomials split into two pairs with
      chi(m_i) = -chi(m_j) on each. Proof: P(chi) is a vanishing sum of
      four roots of unity, counted with repetition. Merge equal terms and
      split into minimal vanishing sums (Mann: in a minimal one of r
      distinct terms normalized to contain 1, every order divides the
      product of the primes up to r, so at r <= 4 every term is a sixth
      root of unity). A minimal sum of 2 terms is antipodal; of 3 is a
      rotate of 1 + w + w^2; of 4 DISTINCT sixth roots of unity does not
      exist, since the six sixth roots sum to zero, so four of them vanish
      iff the complementary two do, which makes the four two antipodal
      pairs and the sum not minimal. With repetition the merged sums are
      2a + b + c = 0, forcing b = c = -a, and 2a + 2b = 0 -- pairings
      again; 3a + b and 4a never vanish. A 3 + 1 split leaves a lone root,
      which does not vanish. So the only shape is 2 + 2: a pairing.
  (3) WHAT THE LEMMA BUYS. For a pairing pi with difference vectors
      d_1 = E_1 - E_2 and d_2 = E_3 - E_4, the coset C_pi = {chi : chi(d_1)
      = chi(d_2) = -1} is nonempty iff the assignment d_1, d_2 -> -1
      respects every relation a d_1 + b d_2 = 0, i.e. iff d_1, d_2 are
      linearly independent, or parallel, d_1 = s v and d_2 = t v with v
      primitive, with s and t of the SAME 2-adic valuation (chi(v) a
      primitive 2s-th root gives chi(v)^t = -1 iff t/s is a ratio of odd
      integers). So THE CORE HAS A TORSION ZERO iff one of its three
      pairings passes that test -- decidable from the exponent vectors
      without factoring anything, and the engine checks it against the
      complete tier on every core. The negative factor is rooted only if
      it vanishes somewhere on some C_pi; free means the cofactor takes
      every component of every nonempty C_pi.
  (4) THE BINOMIAL-COFACTOR SHAPE, by hand. If the cofactor is a binomial
      m_1 + m_3 = m_1(1 + u), it divides m_2 + m_4 = m_2(1 + w) only when
      w = u^{2j+1}, and then the core is (1 + u)(m_1 + m_2 q(u)) with
      q(u) = 1 - u + ... + u^{2j}: the negative factor is A + vB with A a
      MONOMIAL, v = m_2/m_1. Off every line v is independent of u (a
      dependence between them is a rank-1 lattice), so the character with
      u -> 1, v -> -1 is a torsion zero: q(1) = 1 and m_1 + m_2 = 0. The
      size-6 witnesses are free because their A and B have moduli that
      never agree at a torsion point; a monomial A has modulus 1
      everywhere and agrees with q(1) at once. So every non-collinear
      size-4 seed with a binomial cofactor is ROOTED, by hand. What the
      hand does not reach: cores with (f(1), g(1)) = (1, 4) or (4, 1),
      where the cofactor has four terms or the negative factor does, and
      the three cores with more than two factors.
  (5) THE HUNCH, fixed before the run and marked as such: ZERO free. The
      reason is (4) -- the shape that freed the plane at size 6 needs two
      competing non-monomial coefficients, and four terms leave no room
      for two of them beside a cofactor. A transplant from the line is
      NOT available: along a line four terms reach a free seed at degree 5
      (explore_seed_line_floor.py F4), but every such witness is
      collinear by construction and is excluded here.

THE RIG.
  P0 CONTROLS, read before any census number: x^3 - x + 1 prints free and
     1 - x + x^2 prints rooted at the univariate instrument; the size-6
     witness {2,3,4,8,16,24} prints free (complete tier, 0 zeros) and the
     rooted size-6 seed {3,4,8,9,18,24} prints rooted (cheap tier, zeros
     > 0), both through this file's own factor extraction.
  P1 THE CENSUS, by the parent's machinery: size 4 over {2..32}, the seed
     count and the collinear count, checked against 44 and 1.
  P2 THE PAIRING LEMMA, checked: for each of the 44 cores the complete
     tier's verdict on the whole four-term core against the pairing
     predicate of (3), menu by menu.
  P3 THE KILL: every negative factor of the 43 non-collinear seeds through
     the complete tier. Printed per seed: the menu, its prime count and
     affine rank, the factor count of its core, the negative factor, and
     the verdict with its tier, lattice rank rho, term count k and order
     N. Then the count of free factors -- the kill -- and a tally of the
     rooted by cofactor shape (binomial or not), which is what (4) claims
     to predict. The collinear one is printed beside them for the record.
  P4 THE LINE'S CONTRAST, added after the first run for the reading: the
     same shape along a line, 1 + x^3 + x^4 + x^5 = (1 + x)(1 - x + x^2 +
     x^4), the binomial-cofactor quadrinomial at the line's least free
     degree, through the instrument -- where v = u^4 is a power of u the
     character of (4) is not available, u -> 1 forcing v -> 1.

THE PREDICTIONS, FIXED BEFORE THE RUN -- every kill is a printed count.
  K0  CONTROLS: the four verdicts as named in P0.
  K1  CENSUS: 44 seeds, 1 collinear.
  K2  PAIRING: the lemma's predicate agrees with the complete tier on all
      44 cores (a proved lemma; a miss is the instrument's).
  K3  HAND SHAPE: every rooted seed with a binomial cofactor is rooted --
      vacuous if (4) is right, a printed contradiction if not.
  K4  THE KILL: the hunch is 0 free. ZERO -> the plane's least free size
      stays 6 in the swept boxes, size 4 closed and size 5 empty there.
      ONE OR MORE -> the plane's floor is 4, the witness named and its
      freedom re-derived by hand where the moduli argument reaches it.

  K5  THE CONTRAST (P4, fixed before its own run): 1 - x + x^2 + x^4 prints
      free -- the line's shape (4) does not reach, and the plane's does.

RESOURCE ENVELOPE. The census factors 31,465 menus with sympy (~1-2 min);
44 core tests and 43 factor tests at milliseconds each. Memory under
200 MB. Run: python explore_seed_plane_floor.py

FINDINGS (the recorded run, 11 of 11 checks, 46.5 s, the census 46 s of it;
every figure below is that run's print. The first run, without P4, printed
the same figures at 9 of 9 checks in 46.5 s.)

  F1  THE KILL DID NOT FIRE (rule, exhaustive over {2..32}): 0 torsion-free
      negative factors among the 43 non-collinear size-4 seeds, all 43
      rooted at the cheap tier. 41 carry a four-term negative factor of
      lattice rank 2 with EXACTLY ONE zero of order dividing 6; the other
      two, {2,3,16,24} and {3,4,24,32}, are three-factor cores (a binomial
      times 1 + x^3) whose negative factor is 1 - x + x^2. So the plane's
      least free size stays 6 in the swept boxes: size 4 closed here, size
      5 empty in {2..24}, size 6 attained by the two torsion witnesses.
  F2  EVERY ONE OF THE 43 HAS A BINOMIAL COFACTOR (observation, this box),
      so the hand argument (4) reaches the whole census and every verdict
      is a PROPERTY as well as a print: the 41 two-factor cores are
      (1 + u)(m_1 + m_2 q(u)) with q = 1 - u + u^2 -- the j = 1 member,
      four terms, the only one the box admits since u^5 beside u would need
      2^6 -- and the negative factor IS the second bracket, rooted at the
      character u -> 1, v = m_2/m_1 -> -1, which is the one zero mod 6 the
      print counts. Along a line that character is gone, v being a power of
      u, and the same binomial-cofactor shape is FREE at the line's least
      degree: 1 + x^3 + x^4 + x^5 = (1 + x)(1 - x + x^2 + x^4), complete
      tier, 0 zeros (P4). The plane's floor and the line's therefore part
      at size 4 for a reason the exponent lattice states: a free
      four-term seed needs its two non-binomial monomials dependent on the
      binomial's ratio, which is collinearity.
  F3  THE PAIRING LEMMA held on 44 of 44 cores (property, proved in (2));
      every core in the census has a torsion zero, and the pairing
      predicate read it off the exponent vectors without factoring.
"""

import os
import sys
import time
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import Poly

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_seed_rank_law import CHECKS, check
from explore_seed_torsion import test_factor, factor_data
from explore_seed_shape import (census, menu_poly, used_vars, core_of,
                                negative, vectors, affine_rank, collinear,
                                exponents)


def verdict(expr, gens):
    """The torsion verdict of one polynomial: the instrument's dict plus
    'free' (True/False/None for undecided)."""
    d = test_factor(*factor_data(expr, gens))
    d['free'] = None if d['tier'] == 'undecided' else d['zeros'] == 0
    return d


def fmt(d):
    return (f"{'FREE' if d['free'] else 'rooted' if d['free'] is False else 'UNDECIDED'}"
            f" [{d['tier']}, rho={d['rho']}, k={d['k']}, N={d['N']}, zeros={d['zeros']}]")


def seed_data(A):
    """(core factors, negative factors, gens) of a menu."""
    P = menu_poly(A)
    g = used_vars(P)
    core = core_of(P)
    negs = [f for f in core if negative(f, g)]
    return core, negs, g


def v2(n):
    n = abs(n)
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def pairing_predicate(pts):
    """Hand-attack (3): does some pairing of the four exponent vectors have
    a realizable coset chi(d1) = chi(d2) = -1?"""
    p = pts
    pairings = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    for (a, b), (c, d) in pairings:
        d1 = [x - y for x, y in zip(p[a], p[b])]
        d2 = [x - y for x, y in zip(p[c], p[d])]
        if sympy.Matrix([d1, d2]).rank() == 2:
            return True
        g1 = 0
        for x in d1:
            g1 = gcd(g1, x)
        g2 = 0
        for x in d2:
            g2 = gcd(g2, x)
        # parallel: d1 = s v, d2 = t v with v primitive; |s| = g1, |t| = g2
        if v2(g1) == v2(g2):
            return True
    return False


def stage_p0():
    print("P0 CONTROLS")
    x, y = sympy.symbols('x y')
    d = verdict(x**3 - x + 1, [x])
    print(f"  x^3 - x + 1: {fmt(d)}")
    check("K0 x^3 - x + 1 free", d['free'] is True)
    d = verdict(1 - x + x**2, [x])
    print(f"  1 - x + x^2: {fmt(d)}")
    check("K0 1 - x + x^2 rooted", d['free'] is False)
    for A, want in (((2, 3, 4, 8, 16, 24), True), ((3, 4, 8, 9, 18, 24), False)):
        core, negs, g = seed_data(A)
        assert len(negs) == 1, (A, negs)
        d = verdict(negs[0], g)
        print(f"  {A}: negative factor {negs[0]}: {fmt(d)}")
        check(f"K0 {A} {'free' if want else 'rooted'}", d['free'] is want)


def stage_p1():
    print("P1 CENSUS size 4 over {2..32}")
    t0 = time.time()
    menus, seeds, cores, gensof = census(list(range(2, 33)), 4)
    coll = [A for A in seeds if affine_rank(vectors(A)) == 1]
    print(f"  {len(menus)} menus, {len(seeds)} seeds, {len(coll)} collinear "
          f"{coll} ({time.time() - t0:.0f} s)")
    check("K1 44 seeds", len(seeds) == 44)
    check("K1 1 collinear", len(coll) == 1)
    return seeds, cores, gensof, coll


def stage_p2(seeds, gensof):
    print("P2 PAIRING LEMMA on the whole cores")
    agree = 0
    for A in seeds:
        g = gensof[A]
        # the core as one polynomial: the product of its Z-factors
        core_poly = sympy.expand(sympy.Mul(*seed_data(A)[0]))
        d = verdict(core_poly, g)
        pred = pairing_predicate(vectors(A))
        ok = (d['free'] is False) == pred and d['free'] is not None
        agree += ok
        if not ok:
            print(f"  MISS {A}: tier {fmt(d)} vs pairing {pred}")
    print(f"  agreement on {agree}/{len(seeds)} cores")
    check("K2 pairing lemma agrees on every core", agree == len(seeds))


def stage_p3(seeds, coll):
    print("P3 THE KILL: every negative factor of the non-collinear seeds")
    free, rooted = [], []
    binomial_rooted = binomial_total = 0
    undecided = 0
    for A in seeds:
        core, negs, g = seed_data(A)
        pts = vectors(A)
        r = affine_rank(pts)
        nprimes = len({p for m in A for p in exponents(m)})
        tag = "COLLINEAR" if A in coll else f"rank {r}"
        cof = [f for f in core if not negative(f, g)]
        binom = any(len(Poly(f, *g).monoms()) == 2 for f in cof)
        for f in negs:
            d = verdict(f, g)
            print(f"  {A} [{nprimes} primes, {tag}, {len(core)} factors"
                  f"{', binomial cofactor' if binom else ''}] {f}: {fmt(d)}")
            if A in coll:
                continue
            if d['free'] is None:
                undecided += 1
            elif d['free']:
                free.append((A, f, d))
            else:
                rooted.append((A, f, d))
            if binom:
                binomial_total += 1
                binomial_rooted += d['free'] is False
    print(f"  non-collinear seeds: {len(seeds) - len(coll)}; negative factors:"
          f" {len(free) + len(rooted) + undecided}; FREE {len(free)}, rooted"
          f" {len(rooted)}, undecided {undecided}")
    print(f"  binomial-cofactor factors: {binomial_total}, rooted {binomial_rooted}")
    for A, f, d in free:
        print(f"  FREE WITNESS {A}: {f}")
    check("K3 every binomial-cofactor factor rooted", binomial_rooted == binomial_total)
    check("no factor undecided", undecided == 0)
    print(f"  K4 THE KILL COUNT: {len(free)} torsion-free negative factors among"
          f" the {len(seeds) - len(coll)} non-collinear size-4 seeds of {{2..32}}")
    return free


def stage_p4():
    print("P4 THE LINE'S CONTRAST")
    x = sympy.symbols('x')
    P = 1 + x**3 + x**4 + x**5
    fl = sympy.factor_list(P)[1]
    print(f"  1 + x^3 + x^4 + x^5 = {sympy.factor(P)}")
    negs = [f for f, m in fl if any(c < 0 for c in Poly(f, x).coeffs())]
    check("K5 one negative factor, 1 - x + x^2 + x^4",
          len(negs) == 1 and sympy.expand(negs[0] - (1 - x + x**2 + x**4)) == 0)
    d = verdict(negs[0], [x])
    print(f"  {negs[0]}: {fmt(d)}")
    check("K5 the line's quadrinomial factor free", d['free'] is True)


def main():
    t0 = time.time()
    stage_p0()
    seeds, cores, gensof, coll = stage_p1()
    stage_p2(seeds, gensof)
    stage_p3(seeds, coll)
    stage_p4()
    passed = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{passed}/{len(CHECKS)} checks passed, {time.time() - t0:.1f} s")
    for name, ok in CHECKS:
        if not ok:
            print(f"  FAILED: {name}")


if __name__ == '__main__':
    main()
