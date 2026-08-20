"""explore_seed_rank_law.py -- how high can a seed's core rank go at a given
menu size? The simplex law's undecided cell (size 5, rank 3) closed by a
proof that also repairs the law's argument, and the sharper bound the
proof suggests tested in range. (Reads the vocabulary of
explore_seed_shape.py and the size-6 record of explore_seed_confine.py;
shares no code with either, which is what makes its controls controls.)

THE QUESTION. A MENU is a finite set of integers >= 2, read as a
0/1-coefficient polynomial in the primes (m = prod p_i^e_i becomes the
monomial x_1^e_1 ...). Its CORE is that polynomial with the monomial
content divided out; a menu is a SEED when its core carries a Z-irreducible
factor with a negative coefficient, which is the one route to a non-unique
factorization over N (the seed criterion). A seed's CORE RANK is the
affine rank of its reduced exponent vectors -- the dimension of its
Newton polytope. The simplex law says a seed of size n has core rank at
most n - 2 for n >= 3, and the record under it reads: rank 2 is reached
at size 4, rank 3 at size 6 (first witness (1 + x^3)(1 + y + z), the menu
{2, 6, 10, 16, 48, 80}), and size 5 is undecided -- the bound permits
rank 3 there and no witness reaches it. This file asks what the true
maximum is.

WHOSE VOCABULARY. The vectors', as explore_seed_shape.py settled: seedhood
depends on a menu only through its reduced exponent vectors, so two menus
with the same matrix up to a relabelling of primes are one object. The
element boxes below are the SAMPLING FRAME and nothing else; every class
is factored once.

THE HAND-ATTACK, on paper before any engine code.

  (0) THE LAW'S PROOF HAS A GAP, AND ITS CONCLUSION SURVIVES IT. The
      stated argument runs: n vectors of affine rank n - 1 span a
      simplex; a simplex is Minkowski-indecomposable; a product's Newton
      polytope is the Minkowski sum of the factors'; hence the core is
      irreducible. But "indecomposable" in the polytope sense means that
      every summand is a HOMOTHET of the polytope, and a simplex is the
      sum of two smaller homothets of itself, lambda*D + mu*D = D. So
      indecomposability alone never forbids a factorization: (1 + x + y)^2
      has the triangle as its Newton polygon and factors. The law's own
      n = 2 remark is the tell -- a segment is indecomposable in exactly
      that sense, and 1 + x^3 = (1 + x)(1 - x + x^2) factors. What saves
      the conclusion is the 0/1 hypothesis, through the lemma in (1).

  (1) THE TRINOMIAL LEMMA. A 0/1 trinomial 1 + x^a + x^b whose exponent
      vectors a, b are linearly independent is irreducible over C (hence
      over Z, up to monomials). Proof: a, b span a rank-2 sublattice; a
      unimodular change of monomial variables -- an automorphism of the
      Laurent ring -- carries the trinomial to 1 + X^alpha + X^beta Y^gamma
      with alpha, gamma nonzero, and replacing X or Y by its inverse and
      multiplying through by a monomial gives X^m (1 + X^alpha) +
      X^m' Y^gamma with alpha, gamma >= 1 and one of m, m' zero. As a
      polynomial in Y over C[X] this is Eisenstein at the prime X - zeta
      for any root zeta of 1 + X^alpha: the leading coefficient X^m' is
      prime to it, the constant term X^m (1 + X^alpha) is divisible by it
      exactly once since 1 + X^alpha is squarefree. Eisenstein gives
      irreducibility over C(X); primitivity in Y (the two coefficients
      share no factor, one of m, m' being 0) lifts it to C[X, Y]; a
      factorization in the Laurent ring is one in the polynomial ring up
      to monomial units. (When a and b are collinear the trinomial is
      univariate and CAN factor -- the collinear criterion of size 3.)

  (2) THE REPAIRED SIMPLEX LAW. Let f be a 0/1 polynomial with n >= 3
      terms of affine rank n - 1, so its Newton polytope D is a simplex
      with every support point a vertex. If f = g h with neither factor a
      monomial, the Newton polytopes of g and h are non-points summing to
      D, hence homothets lambda*D + t and mu*D + t' with lambda, mu > 0
      (a simplex is indecomposable: its 2-faces are triangles, a
      triangle's only summands are homothets -- a summand's edge normals
      are among the triangle's three, so it is a homothetic triangle, a
      segment or a point, and segment + segment or segment + triangle is
      never a triangle -- and the triangles of a simplex form a chain
      sharing edges and touching every vertex, so the ratio lambda is one
      number and the summand is lambda*D up to translation). Take any
      triangular 2-face F of D (D itself at n = 3). The face polynomial
      of f at F is the product of the face polynomials of g and h there,
      whose Newton polygons lambda*F and mu*F are non-points, so the face
      polynomial of f -- a 0/1 trinomial whose exponents are the vertices
      of a non-degenerate triangle, not collinear -- is reducible,
      against (1). So f is irreducible: the law's statement stands on a
      different proof.

  (3) THE CELL CLOSES, AND ONE RANK MORE WITH IT. Let f be 0/1 with
      n >= 5 terms of affine rank d = n - 2. The hull P of the support has
      d + 1 or d + 2 vertices.
        -- d + 1 vertices: P is a simplex and one support point s is not a
           vertex; s lies in the relative interior of one face G of P. A
           triangular 2-face of P is CLEAN (carries no support point but
           its three vertices) unless it contains G, and at most d - 1 of
           the C(d+1, 3) triangles do (the triangles through an edge);
           C(d+1, 3) > d - 1 for d >= 3, so a clean triangle exists. P is
           indecomposable as in (2), so the factors' polytopes are
           homothets, and the clean triangle's face polynomial is a
           reducible non-collinear 0/1 trinomial, against (1).
        -- d + 2 vertices, every support point a vertex: if some facet
           holds d + 1 of them, the remaining vertex is an apex and P is a
           PYRAMID, whose triangles through the apex form a chain touching
           every vertex; otherwise every facet is a (d-1)-simplex and P is
           SIMPLICIAL, all of whose 2-faces are triangles. Either way P is
           indecomposable, every triangle is clean, and (1) applies.
      Hence a 0/1 polynomial with n >= 5 terms of affine rank n - 2 is
      irreducible up to content and monomials, and a seed of size n >= 5
      has core rank <= n - 3. At n = 5 that is rank <= 2: the undecided
      cell is EMPTY. At n = 6 it is rank <= 3, which the size-6 record
      already shows in its box (177 seeds at rank 3, 26 at rank 2, none at
      4).

  (4) THE CONJECTURE BEYOND, AND ITS TIGHTNESS. A nonnegative
      factorization multiplies term counts (the term-count law), so
      f = g h with a and b terms has n = a b and rank <= (a-1) + (b-1)
      <= ab/2, with equality only when a or b is 2: for nonnegative
      factors the bound is floor(n/2) and it is a prism over a simplex.
      The suspicion is that cancellation buys nothing here either:
      EVERY reducible 0/1 polynomial with n terms has affine rank at most
      floor(n/2). The bound is attained by seeds at every n >= 4:
      (1 - x + x^2)(A(x) + sum_i y_i B_i(x)) where each of
      (1 - x + x^2) A and (1 - x + x^2) B_i is 1 + x^3 (two terms) or
      1 + x^2 + x^4 (three) -- blocks of two terms give n = 2 + 2k at rank
      k + 1 = n/2, one block of three gives n = 3 + 2k at rank
      k + 1 = (n - 1)/2. What the paper proof does NOT reach is n = 7 at
      rank 4 and n = 8 at rank 5: 4-polytopes with 7 vertices and
      5-polytopes with 8 are beyond the two shapes (3) classifies. Those
      two cells are the conjecture's in-range test.

THE RIG. Menus of size n are enumerated from an element box {2..b}; each
is reduced to its exponent matrix with the content divided out, its
affine rank is computed by exact elimination, and the matrix is
canonicalized up to a permutation of the prime columns (columns grouped
by their sorted-entry signature, permutations tried within a group), so
each class is factored once with sympy. A class is REDUCIBLE when its
core has two or more non-monomial Z-irreducible factors counted with
multiplicity, and a SEED when one of them carries a negative coefficient.
Sizes 3, 5 and 6 run over {2..24}; sizes 7 and 8 over {2..20}. A
rehearsal flag (--rehearse) runs every stage over {2..12}, exercising each
before the full run.

THE PREDICTIONS, FIXED BEFORE THE RUN -- every kill is a printed count.

  C0  CONTROL, the trinomial lemma: among the size-3 classes of
      non-collinear vectors (rank 2), the reducible count prints 0. The
      collinear seed {2, 8, 32} prints SEED and the segment {2, 16} prints
      SEED at rank 1 (the n = 2 exception, 1 + x^3).
  C1  THE THEOREM at n = 5: the rank-3 classes' reducible count prints 0
      and so their seed count; the rank-4 (old-law) cell prints 0.
  C2  THE THEOREM at n = 6: the rank-4 classes' reducible count prints 0;
      rank 5 prints 0.
  C3  THE CONJECTURE at n = 7: rank 6 and rank 5 (old law, theorem) print
      0; rank 4 -- the conjecture's cell -- prints 0 reducible.
  C4  THE CONJECTURE at n = 8: rank 7 and rank 6 print 0; rank 5 prints 0
      reducible.
      (C1-C4 also print the box's first seed at the rank just below the
      cell, or "none in this box"; that line is information and not a
      check -- the REHEARSAL at {2..12} showed it failing for box reasons
      alone, the smallest rank-2 seed of size 5 needing an element like
      48, so tightness is carried by C5 and by nothing in a sweep.)
  C5  TIGHTNESS, the family: the five menus
        n=4 {2,16,6,48}             (1+x^3)(1+y)
        n=5 {2,16,6,24,96}          (1+x^3) + y(1+x^2+x^4)
        n=6 {2,16,6,48,10,80}       (1+x^3)(1+y+z)
        n=7 {2,16,6,24,96,10,80}    (1+x^3) + y(1+x^2+x^4) + z(1+x^3)
        n=8 {2,16,6,48,10,80,14,112}(1+x^3)(1+y+z+w)
      each print SEED with core rank 2, 2, 3, 3, 4 = floor(n/2) and a
      negative factor 1 - x + x^2 in the core.
  What would kill what: a reducible class in C1's rank-3 cell or C2's
  rank-4 cell kills the THEOREM (and the proof above has an error); one
  in C3's rank-4 or C4's rank-5 cell kills the CONJECTURE and leaves the
  theorem standing; a reducible class in C0 kills the lemma and with it
  everything.

RESOURCE ENVELOPE. Pure-Python enumeration plus sympy factoring of the
deduplicated classes; estimated under 10 minutes, memory well under
100 MB. Run: python explore_seed_rank_law.py [--rehearse]

FINDINGS (one full run, 18 of 18 checks, 76.7 s; every figure below is
that run's print).

  F1  THE CELL IS EMPTY, AND THE THEOREM HOLDS AT EVERY CLASS IN RANGE.
      Size 5 over {2..24}: 33,649 menus, of which 6,140 have rank 3 and
      make 1,546 classes -- 0 reducible; the 27,169 rank-4 menus make
      2,114 classes -- 0 reducible. Size 6 over {2..24}: 100,947 menus;
      the 35,493 rank-4 menus make 5,139 classes -- 0 reducible; rank 5,
      58,371 menus in 3,247 classes -- 0 reducible. A seed of size 5 has
      core rank at most 2 and one of size 6 at most 3 (property, proved;
      the rig's agreement at every class is the check that the proof's
      object is the engine's).
  F2  THE CONJECTURE SURVIVES BOTH CELLS THE PROOF DOES NOT REACH. Size 7
      over {2..20}: 50,388 menus; rank 4 holds 13,894 of them in 3,271
      classes -- 0 reducible; rank 5 (22,432 menus, 1,963 classes) and
      rank 6 (11,635 menus, 878 classes) -- 0 reducible. Size 8 over
      {2..20}: 75,582 menus; rank 5 holds 30,951 in 3,298 classes -- 0
      reducible; rank 6 (23,813 menus, 1,963 classes) and rank 7 (5,605
      menus, 854 classes) -- 0 reducible. So over these boxes every
      reducible 0/1 polynomial of 7 terms has rank <= 3 and of 8 terms
      rank <= 4 (rule in range; the floor(n/2) law beyond n = 8 is a
      pattern, its first untested cells n = 9 at ranks 5 and 6).
  F3  TIGHTNESS, AND TWO NEGATIVE FACTORS OF A NEW SHAPE. The family's
      five menus are seeds at rank 2, 2, 3, 3, 4 = floor(n/2), each core
      carrying x2^2 - x2 + 1 (the prime 2's variable). The boxes' own
      first seeds just below the cells: size 6, {2, 3, 4, 5, 10, 24} =
      (1 + x2)(x2^2 x3 - x2 x3 + x2 + x3 + x5) at rank 3; size 8,
      {2, 3, 5, 6, 7, 10, 14, 16} = (1 + x2)(x2^3 - x2^2 + x2 + x3 + x5
      + x7) at rank 4 -- negative Z-irreducible factors in three and four
      variables, where the corpus had met 1 - x + x^2 and x^2 - xy + y^2
      (observation). Sizes 5 and 7 hold no seed at the cell's rank inside
      their boxes (238 and 1,477 classes factored to exhaustion), which
      is a box fact: the family supplies {2, 16, 6, 24, 96} and
      {2, 16, 6, 24, 96, 10, 80} outside them.
  F4  THE CONTROL. 1,758 non-collinear size-3 menus of {2..24} in 199
      classes -- 0 reducible (the trinomial lemma, in range); {2, 8, 32}
      and {2, 16} are seeds at rank 1 with cores [x2^2 - x2 + 1,
      x2^2 + x2 + 1] and [x2 + 1, x2^2 - x2 + 1].

  TIERS. The repaired simplex law and rank <= n - 3 at n >= 5: property,
  proved (hand-attack (1)-(3)), with F1 as its in-range check. The
  floor(n/2) ceiling: rule in range through n = 8, pattern beyond (as
  recorded; since settled -- explore_seed_rank_nine.py carries the n = 9
  and n = 10 cells, and the ceiling's proof, the polytope half from the
  literature and a clean-triangle lemma, stands in the docs that cite
  both files). Its attainment at every n >= 4: property, by construction
  (F3). The
  many-variable negative factors: observation.

  RUN RECORD. Rehearsal at {2..12}, 1.1 s, every stage exercised: its
  four in-box witness lines failed for box reasons (the smallest rank-2
  seed of size 5 needs an element like 48) and were demoted to prints
  before the full run; nothing else in the slate moved. One correction
  between the first full run and the recorded one: the witness prints
  named the negative factor in canonical column order beside a menu in
  prime order, and now factor the menu in its own prime coordinates;
  no check changed. Full run 76.7 s -- enumeration 33 s, factoring 44 s
  -- memory trivial; Python 3.12, sympy.
"""

import os
import sys
import time
from fractions import Fraction
from itertools import combinations, permutations, product

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import symbols, Poly

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]
VARS = symbols(' '.join(f'y{i}' for i in range(len(PRIMES))))

CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))
    print(("PASS  " if ok else "FAIL  ") + name)


# ------------------------------------------------------------ the vectors
def exponent_vector(m):
    v = [0] * len(PRIMES)
    rest = m
    for i, p in enumerate(PRIMES):
        while rest % p == 0:
            rest //= p
            v[i] += 1
    assert rest == 1, f"element {m} outside the prime list"
    return v


VEC = {}


def vec(m):
    if m not in VEC:
        VEC[m] = exponent_vector(m)
    return VEC[m]


def reduced_matrix(menu):
    """Rows = menu elements, columns = the primes present, content divided
    out (each column shifted to minimum 0); all-zero columns dropped."""
    rows = [vec(m) for m in menu]
    cols = [j for j in range(len(PRIMES)) if any(r[j] for r in rows)]
    mins = [min(r[j] for r in rows) for j in cols]
    return [tuple(r[j] - mn for j, mn in zip(cols, mins)) for r in rows]


def affine_rank(rows):
    """Exact rank of the differences from the first row."""
    base = rows[0]
    mat = [[Fraction(a - b) for a, b in zip(r, base)] for r in rows[1:]]
    rank = 0
    ncols = len(base)
    for c in range(ncols):
        piv = None
        for i in range(rank, len(mat)):
            if mat[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        pr = mat[rank]
        for i in range(len(mat)):
            if i != rank and mat[i][c] != 0:
                f = mat[i][c] / pr[c]
                mat[i] = [x - f * y for x, y in zip(mat[i], pr)]
        rank += 1
        if rank == len(mat):
            break
    return rank


def canonical(rows):
    """The reduced matrix up to a permutation of its columns: columns are
    grouped by signature (sorted entries) and the lexicographically least
    sorted row tuple over the within-group permutations is the key."""
    ncols = len(rows[0])
    sig = [tuple(sorted(r[j] for r in rows)) for j in range(ncols)]
    groups = {}
    for j in range(ncols):
        groups.setdefault(sig[j], []).append(j)
    keys = sorted(groups)
    perms_per_group = [list(permutations(groups[k])) for k in keys]
    best = None
    for choice in product(*perms_per_group):
        order = [j for perm in choice for j in perm]
        cand = tuple(sorted(tuple(r[j] for j in order) for r in rows))
        if best is None or cand < best:
            best = cand
    return best


# ---------------------------------------------------------- the factoring
def poly_of(rows):
    ncols = len(rows[0])
    gens = VARS[:ncols]
    expr = 0
    for r in rows:
        t = 1
        for g, e in zip(gens, r):
            t *= g ** e
        expr += t
    return sympy.expand(expr), gens


def factor_class(rows):
    """(reducible, seed, negative factor or None) for a canonical class."""
    expr, gens = poly_of(rows)
    content, fl = sympy.factor_list(expr)
    assert content == 1, f"non-unit content {content}"
    core = []
    for f, mult in fl:
        if f in gens:
            continue
        core.extend([f] * mult)
    reducible = len(core) >= 2
    neg = None
    for f in core:
        if any(c < 0 for c in Poly(f, *gens).coeffs()):
            neg = f
            break
    return reducible, neg is not None, neg


def describe(menu):
    """The menu's core factored in its OWN prime coordinates (x2 for the
    prime 2, and so on), for the prints; the classes are factored in
    canonical column order, which is a relabelling of these."""
    rows = [vec(m) for m in menu]
    cols = [j for j in range(len(PRIMES)) if any(r[j] for r in rows)]
    mins = [min(r[j] for r in rows) for j in cols]
    gens = symbols(' '.join(f'x{PRIMES[j]}' for j in cols))
    if not isinstance(gens, tuple):
        gens = (gens,)
    expr = 0
    for r in rows:
        t = 1
        for g, j, mn in zip(gens, cols, mins):
            t *= g ** (r[j] - mn)
        expr += t
    content, fl = sympy.factor_list(sympy.expand(expr))
    core = [f for f, mult in fl for _ in range(mult) if f not in gens]
    neg = [f for f in core if any(c < 0 for c in Poly(f, *gens).coeffs())]
    return core, neg


# ------------------------------------------------------------- the stages
def sweep(size, box, kill_ranks, witness_ranks, label):
    """Enumerate menus of a size over a box, bucket by rank, factor every
    class at the kill ranks, factor the witness ranks' classes until the
    first seed, print the cell table."""
    t0 = time.time()
    elems = list(range(2, box + 1))
    of_interest = set(kill_ranks) | set(witness_ranks)
    classes = {}   # rank -> {canonical: representative menu}
    counts = {}    # rank -> menu count
    for menu in combinations(elems, size):
        rows = reduced_matrix(menu)
        r = affine_rank(rows)
        counts[r] = counts.get(r, 0) + 1
        if r in of_interest:
            key = canonical(rows)
            classes.setdefault(r, {}).setdefault(key, menu)
    t1 = time.time()
    print(f"\n{label}: size {size} over {{2..{box}}}, "
          f"{sum(counts.values())} menus, enumeration {t1 - t0:.1f} s")
    print("  menus by rank: " +
          ", ".join(f"rank {r}: {counts[r]}" for r in sorted(counts)))
    result = {}
    for r in sorted(of_interest, reverse=True):
        cl = classes.get(r, {})
        red = seeds = tried = 0
        witness = None
        for key, menu in cl.items():
            reducible, seed, neg = factor_class(list(key))
            tried += 1
            red += reducible
            seeds += seed
            if seed and witness is None:
                core, negs = describe(menu)
                witness = (menu, negs[0], core)
                if r in witness_ranks and r not in kill_ranks:
                    break
        result[r] = (len(cl), red, seeds, witness, tried)
        if r in kill_ranks:
            print(f"  rank {r}: {len(cl)} classes, all factored: "
                  f"{red} reducible, {seeds} seeds" +
                  (f"; witness {witness[0]} = {witness[2]}"
                   if witness else ""))
        else:
            print(f"  rank {r}: {len(cl)} classes, {tried} factored to the "
                  f"first seed: " +
                  (f"{witness[0]} = {witness[2]}"
                   if witness else "none found"))
    print(f"  factoring {time.time() - t1:.1f} s")
    return result


def stage_c0(box):
    print("\nC0  CONTROL -- the trinomial lemma and the two known seeds")
    res = sweep(3, box, {2}, {1}, "C0")
    ncl, red, seeds, _, _ = res[2]
    check("C0 every non-collinear size-3 class is irreducible "
          f"({red} reducible of {ncl})", red == 0)
    for menu, want_rank in (((2, 8, 32), 1), ((2, 16), 1)):
        rows = reduced_matrix(menu)
        reducible, seed, neg = factor_class(rows)
        r = affine_rank(rows)
        core, negs = describe(menu)
        print(f"  {menu}: rank {r}, {'SEED' if seed else 'not a seed'}, "
              f"core {core}")
        check(f"C0 {menu} is a seed at rank {want_rank}",
              seed and r == want_rank)


def stage_theorem(size, box, tag):
    old, thm, wit = size - 1, size - 2, size - 3
    res = sweep(size, box, {old, thm}, {wit}, tag)
    check(f"{tag} rank {old} (old law) cell: {res[old][1]} reducible "
          f"of {res[old][0]}", res[old][1] == 0)
    check(f"{tag} rank {thm} (theorem) cell: {res[thm][1]} reducible "
          f"of {res[thm][0]}", res[thm][1] == 0)
    print(f"  ({tag} the box's first seed at rank {wit}: "
          f"{res[wit][3][0] if res[wit][3] else 'none in this box'})")
    return res


def stage_conjecture(size, box, tag):
    old, thm, conj = size - 1, size - 2, size // 2
    res = sweep(size, box, {old, thm, conj + 1}, {conj}, tag)
    check(f"{tag} rank {old} (old law) cell: {res[old][1]} reducible "
          f"of {res[old][0]}", res[old][1] == 0)
    check(f"{tag} rank {thm} (theorem) cell: {res[thm][1]} reducible "
          f"of {res[thm][0]}", res[thm][1] == 0)
    check(f"{tag} rank {conj + 1} (conjecture) cell: "
          f"{res[conj + 1][1]} reducible of {res[conj + 1][0]}",
          res[conj + 1][1] == 0)
    print(f"  ({tag} the box's first seed at rank {conj}: "
          f"{res[conj][3][0] if res[conj][3] else 'none in this box'})")
    return res


FAMILY = [
    (4, (2, 16, 6, 48)),
    (5, (2, 16, 6, 24, 96)),
    (6, (2, 16, 6, 48, 10, 80)),
    (7, (2, 16, 6, 24, 96, 10, 80)),
    (8, (2, 16, 6, 48, 10, 80, 14, 112)),
]


def stage_c5():
    print("\nC5  TIGHTNESS -- the family (1 - x + x^2)(A + sum y_i B_i)")
    for n, menu in FAMILY:
        rows = reduced_matrix(menu)
        r = affine_rank(rows)
        reducible, seed, neg = factor_class(rows)
        core, negs = describe(menu)
        print(f"  n={n} {menu}: rank {r}, {'SEED' if seed else 'not a seed'}"
              f", core {core}")
        check(f"C5 n={n} seed at rank {n // 2} with a negative factor",
              seed and r == n // 2 and neg is not None)


def main():
    rehearse = '--rehearse' in sys.argv
    t0 = time.time()
    if rehearse:
        print("REHEARSAL over {2..12} at every stage")
        b_small = b_large = 12
    else:
        b_small, b_large = 24, 20
    stage_c0(b_small)
    print("\nC1  THE THEOREM at n = 5")
    stage_theorem(5, b_small, "C1")
    print("\nC2  THE THEOREM at n = 6")
    stage_theorem(6, b_small, "C2")
    print("\nC3  THE CONJECTURE at n = 7")
    stage_conjecture(7, b_large, "C3")
    print("\nC4  THE CONJECTURE at n = 8")
    stage_conjecture(8, b_large, "C4")
    stage_c5()
    failed = [n for n, ok in CHECKS if not ok]
    print(f"\n{len(CHECKS) - len(failed)}/{len(CHECKS)} checks pass, "
          f"{time.time() - t0:.1f} s total")
    if failed:
        print("FAILED: " + "; ".join(failed))
        sys.exit(1)


if __name__ == '__main__':
    main()
