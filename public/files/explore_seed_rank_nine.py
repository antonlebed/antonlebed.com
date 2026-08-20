"""explore_seed_rank_nine.py -- the half-size ceiling's first untested cells.
Does any reducible 0/1 polynomial with 9 terms have Newton-polytope
dimension 5 or 6, or one with 10 terms dimension 6 or 7? (Reads the
vocabulary and the machinery of explore_seed_rank_law.py, which it imports;
the cells here are the ones that script's record names as the conjecture's
first untested ones.)

THE QUESTION. A MENU is a finite set of integers >= 2 read as a
0/1-coefficient polynomial in the primes; its CORE is that polynomial with
the monomial content divided out; its CORE RANK is the affine rank of the
reduced exponent vectors, the dimension of the Newton polytope. A menu is
REDUCIBLE when its core has two or more non-monomial Z-irreducible factors,
and a SEED when one of those carries a negative coefficient. The seed rank
law (property, proved): a reducible core of n >= 5 terms has rank <= n - 3.
The half-size ceiling (rule in range through n = 8): a reducible core of n
terms has rank <= floor(n/2). Its first cells past the range are n = 9 at
ranks 5 and 6 and n = 10 at ranks 6 and 7, and this file prints them.

THE HAND-ATTACK, on paper before any engine code.

  (1) WHY THE CELLS ARE THE PROOF'S BLIND SPOT. The law's proof needs two
      things of the support's hull P of dimension d: that P is Minkowski-
      indecomposable, so the factors' polytopes are homothets of P; and
      that P has a triangular 2-face carrying no support point but its
      vertices, whose face polynomial is then a reducible non-collinear
      0/1 trinomial, against the trinomial lemma. At n = d + 2 the hull
      has d + 1 or d + 2 vertices and both shapes are classified; at
      n = 9, d = 5 the hull may have 6, 7, 8 or 9 vertices, and a
      5-polytope with 8 or 9 vertices is beyond the classification. If
      the ceiling is TRUE the reason is that every d-polytope with fewer
      than 2d vertices is indecomposable (the polytope half, a literature
      question) and that fewer than 2d support points cannot spoil every
      triangular 2-face (the clean-triangle half); if it is FALSE the
      witness is a decomposable hull with fewer than 2d vertices or a
      homothetic factorization that hides every triangle, and the
      cheapest place to see either is these cells.

  (2) WHAT A BOX CAN AND CANNOT SAY. Over an element box {2..b} the primes
      present cap the affine rank at their COUNT (not one below it: ten
      points in eight coordinates can have affine rank 8), so {2..24}
      with nine primes reaches rank 8 at n = 9 and {2..20} with eight
      reaches rank 8 at n = 10, the theorem's forbidden cell there. A
      zero in a conjecture cell is a RULE IN RANGE and never a proof; a
      reducible class there is a counterexample outright, because a
      class's core rank is computed exactly and its factorization is
      sympy's over Z.

  (3) THE CORES. Every negative factor the corpus had met before
      explore_seed_rank_law.py was 1 - x + x^2 or x^2 - xy + y^2, each the
      cyclotomic factor of a binomial 1 + x^3 or x^3 + y^3; that script
      found negative factors in three and four variables. Whether a
      seed's negative factor is always a univariate cyclotomic polynomial
      (a factor of some 1 + x^k, absorbed into a 0/1 product) or can be
      genuinely multivariate is read here off the rank-4 seeds of size 8
      over {2..20}, the cell where that script's four-variable negative
      factor lives: the first 25 seeds' negative factors are printed and
      tallied as univariate-cyclotomic against the rest. A print, not a
      check.

THE RIG. Menus of size 9 are enumerated over {2..24} and of size 10 over
{2..20}; each is reduced, its affine rank computed exactly, and its
matrix canonicalized up to a permutation of the prime columns so each
class is factored once (all of it explore_seed_rank_law.py's code). A
rehearsal flag (--rehearse) runs every stage over {2..12}.

THE PREDICTIONS, FIXED BEFORE THE RUN -- every kill is a printed count.

  C0  CONTROL, the attaining family: {2,16,6,24,96,10,80,14,112}, nine
      terms, (1+x^3) + y(1+x^2+x^4) + z(1+x^3) + w(1+x^3), prints SEED at
      rank 4; {2,16,6,48,10,80,14,112,22,176}, ten terms,
      (1+x^3)(1+y+z+w+v), prints SEED at rank 5.
  C1  n = 9 over {2..24}: the rank-8 and rank-7 cells (the old law) and
      the rank-6 cell (the theorem) print 0 reducible; the rank-5 cell --
      the ceiling's -- prints 0 reducible.
  C2  n = 10 over {2..20}: the rank-8 cell (the theorem) and the rank-7
      and rank-6 cells (the ceiling's) print 0 reducible.
  C3  THE CORES, a print: the first 25 rank-4 seeds of size 8 over
      {2..20}, each with its negative factor, and the tally
      univariate-cyclotomic versus other.
  What would kill what: a reducible class at rank 6 of size 9 or rank 8
  of size 10 kills the THEOREM (its proof has an error); one at rank 5
  of size 9 or rank 6 or 7 of size 10 kills the CEILING and leaves the
  theorem standing; the family failing C0 means the rig's object is not
  the proof's.

RESOURCE ENVELOPE. Pure-Python enumeration (C(23,9) = 817,190 menus at
size 9, C(19,10) = 92,378 at size 10; the parent rig enumerated about
8,000 menus per second) plus sympy factoring of the deduplicated classes;
estimated under ten minutes, memory under 200 MB (the class dictionaries
at the four ranks of interest). Run: python explore_seed_rank_nine.py
[--rehearse]

FINDINGS (the recorded run, 9 of 9 checks, 457.8 s, peak 127 MB; every
figure below is that run's print).

  F1  EVERY CELL IS EMPTY. Size 9 over {2..24}: 817,190 menus -- rank 8
      (30,178 menus, 3,232 classes), rank 7 (174,776 menus, 9,297
      classes), rank 6 (326,528 menus, 19,654 classes) and rank 5
      (228,080 menus, 31,521 classes): 0 reducible at each. Size 10 over
      {2..20}: 92,378 menus -- rank 8 (2,785 menus, 1,866 classes), rank 7
      (19,647 menus, 3,298 classes), rank 6 (38,057 menus, 4,067
      classes): 0 reducible at each. The theorem holds at every class in
      range (its proof is paper); the half-size ceiling is a rule in
      range through n = 10 by this run, and the docs that cite this file
      carry its proof -- the polytope half from the literature (a
      d-polytope with fewer than 2d vertices is indecomposable) and a
      clean-triangle lemma -- which the hand-attack's (1) named as the
      shape the reason would have to take.
  F2  THE CONTROL. Both family members print SEED at the ceiling: n = 9
      at rank 4 with core [x2^2 - x2 + 1, x2^2 x3 + x2 x3 + x2 x5 + x2 x7
      + x2 + x3 + x5 + x7 + 1], n = 10 at rank 5 with core [x11 + x3 + x5
      + x7 + 1, x2 + 1, x2^2 - x2 + 1].
  F3  THE CORES (observation). {2..20} holds exactly 5 rank-4 seeds of
      size 8 among 4,059 classes, and every negative factor is
      MULTIVARIATE and of one shape: x2^3 - x2^2 + x2 + L, L a sum of
      monomials in the other primes' variables ({2,3,5,6,7,10,14,16}:
      L = x3 + x5 + x7; {2,3,6,7,10,14,16,20}: x2 x5 + x3 + x7;
      {2,5,7,9,10,14,16,18}: x3^2 + x5 + x7; {2,6,7,10,12,14,16,20}:
      x2 x3 + x2 x5 + x7; {2,7,9,10,14,16,18,20}: x2 x5 + x3^2 + x7) --
      0 univariate-cyclotomic, 5 other. The cyclotomic 1 - x + x^2 is
      the one-variable part, x2 (x2^2 - x2 + 1), the cofactor is 1 + x2
      every time, and (1 + x2) x2 (x2^2 - x2 + 1) = x2 + x2^4 is the
      absorption; L rides along multiplied by 1 + x2. So "every negative
      factor is an absorbed cyclotomic" is FALSE as stated and true of
      the univariate restriction in this cell; whether a seed's negative
      factor can carry no cyclotomic restriction at all is not asked
      here.

  TIERS. F1: rule in range (n = 9 over {2..24}, n = 10 over {2..20}) for
  the ceiling; the theorem's in-range check. F2: property, by
  construction. F3: observation, one cell of one box.

  RUN RECORD. Rehearsal at {2..12}, 0.1 s, every stage exercised. A first
  full run (537 s, 8 checks) factored ranks 7 and 6 at n = 10 and read
  the cores at size 9; its prints caught two slate errors: hand-attack
  (2) had said eight primes cap the rank at 7, where affine rank reaches
  the prime count and the box held 2,785 rank-8 menus of size 10
  unfactored (added as the theorem cell), and the size-9 cores stage
  found no rank-4 seed in {2..24} at all (16,734 classes), a box fact
  like the parent rig's, so the read moved to size 8 over {2..20} where
  the parent's four-variable witness lives. Rehearsed again (0.2 s, 9
  checks) and rerun whole: the recorded run above, whose n = 9 figures
  are the first run's to the digit. Python 3.12, sympy.
"""

import os
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import Poly

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_seed_rank_law import (CHECKS, check, reduced_matrix,
                                   affine_rank, factor_class, describe,
                                   sweep)

FAMILY = [
    (9, 4, (2, 16, 6, 24, 96, 10, 80, 14, 112)),
    (10, 5, (2, 16, 6, 48, 10, 80, 14, 112, 22, 176)),
]


def stage_c0():
    print("\nC0  CONTROL -- the attaining family at n = 9 and n = 10")
    for n, want, menu in FAMILY:
        rows = reduced_matrix(menu)
        r = affine_rank(rows)
        reducible, seed, neg = factor_class(rows)
        core, negs = describe(menu)
        print(f"  n={n} {menu}: rank {r}, {'SEED' if seed else 'not a seed'}"
              f", core {core}")
        check(f"C0 n={n} family member is a seed at rank {want}",
              seed and r == want)


def is_univariate_cyclotomic(f):
    gens = [g for g in f.free_symbols]
    if len(gens) != 1:
        return False
    x = gens[0]
    p = Poly(f, x)
    deg = p.degree()
    for m in range(1, 200):
        if sympy.totient(m) == deg and Poly(sympy.cyclotomic_poly(m, x), x) == p:
            return True
    return False


def stage_cores(box, size=8, rank=4, limit=25):
    print(f"\nC3  THE CORES -- the first {limit} rank-{rank} seeds of size "
          f"{size} over {{2..{box}}}")
    from itertools import combinations
    from explore_seed_rank_law import canonical
    seen = set()
    found = 0
    uni = other = 0
    for menu in combinations(range(2, box + 1), size):
        rows = reduced_matrix(menu)
        if affine_rank(rows) != rank:
            continue
        key = canonical(rows)
        if key in seen:
            continue
        seen.add(key)
        reducible, seed, neg = factor_class(list(key))
        if not seed:
            continue
        core, negs = describe(menu)
        kinds = []
        for g in negs:
            if is_univariate_cyclotomic(g):
                uni += 1
                kinds.append("cyclotomic")
            else:
                other += 1
                kinds.append("other")
        print(f"  {menu}: negative {negs} [{', '.join(kinds)}]")
        found += 1
        if found >= limit:
            break
    print(f"  tally over {found} seeds ({len(seen)} rank-{rank} classes looked "
          f"at): {uni} univariate-cyclotomic negative factors, {other} other")


def main():
    rehearse = '--rehearse' in sys.argv
    t0 = time.time()
    if rehearse:
        print("REHEARSAL over {2..12} at every stage")
        b9 = b10 = 12
    else:
        b9, b10 = 24, 20
    stage_c0()
    print("\nC1  THE CELLS at n = 9")
    res = sweep(9, b9, {8, 7, 6, 5}, set(), "C1")
    for r, what in ((8, "old law"), (7, "old law"), (6, "theorem"),
                    (5, "ceiling")):
        ncl, red = res[r][0], res[r][1]
        check(f"C1 rank {r} ({what}) cell: {red} reducible of {ncl}",
              red == 0)
    print("\nC2  THE CELLS at n = 10")
    res = sweep(10, b10, {8, 7, 6}, set(), "C2")
    for r, what in ((8, "theorem"), (7, "ceiling"), (6, "ceiling")):
        ncl, red = res[r][0], res[r][1]
        check(f"C2 rank {r} ({what}) cell: {red} reducible of {ncl}",
              red == 0)
    stage_cores(b10)
    failed = [n for n, ok in CHECKS if not ok]
    print(f"\n{len(CHECKS) - len(failed)}/{len(CHECKS)} checks pass, "
          f"{time.time() - t0:.1f} s total")
    if failed:
        print("FAILED: " + "; ".join(failed))
        sys.exit(1)


if __name__ == '__main__':
    main()
