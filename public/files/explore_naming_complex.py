"""What the naming criterion says about the clique complex.

THE OBJECT.  The neighbour graph on Z/N, N = p_1...p_m, is the Cartesian
product K_{p_1} [] ... [] K_{p_m}; its clique complex is a wedge of b1 circles
with b1 = 1 - chi, chi = N(1 - m + sum 1/p_i) (explore_clique_betti.py).  The
reciprocal naming criterion says an absent prime s divides -chi(S) iff
sum_i 1/p_i = m - 1 (mod s) (explore_tower_naming.py).  The criterion was
written when -chi was a formula with no object; now -chi = b1 - 1, so the
criterion is a divisibility statement about the FIRST HOMOLOGY of a complex,
and it has never been read as one.

THE QUESTION.  Does the homology say anything the factorization does not?
Two halves.  (a) A sub-ring is a sub-product, so its complex embeds -- does
b1 - 1 track that embedding, and does the criterion travel along it?  (b) The
one classical theorem connecting a prime to an Euler characteristic runs
through a FREE ACTION: if Z/s acts freely on a finite complex X, then
chi(X) = s * chi(X/G), so s | chi(X).  Naming is exactly s | chi.  Is the
divisibility carried by a symmetry?

THE SLATE (frozen before any engine code).

S0 -- THE ADDITIVE REWRITE, derived on paper before this file existed.
  Put g(S) = sum_{p in S} (1 - 1/p), read in Z/s (every p is invertible mod s
  since s is absent and all entries are prime).  Then
      -chi(S) = N * (g(S) - 1),
  so with gcd(N, s) = 1 the criterion reads g(S) = 1 (mod s), with the SET SIZE
  m gone.  g is additive over disjoint unions, so the criterion is a level set
  of a Z/s-valued linear functional on the subset lattice: w_s(p) = 1 - p^{-1}
  is a weight per prime, and s names S iff the weights of S sum to 1.
  Two consequences, both derived here and tested below.  Naming is closed under
  adjoining an s-NEUTRAL block (g(U) = 0): the criterion travels along the
  embedding of complexes exactly when the complement is neutral.  And the class
  counts over subsets of the first k primes are the coefficients of
  prod_p (1 + x^{w_s(p)}) in Z[x]/(x^s - 1) -- which is what a 1/s naming
  baseline would have to come from.

S1 -- THE EMBEDDING FORMULA, derived on paper before this file existed.
  For T a subset of S with U = S minus T: holding the U-coordinates at any fixed
  value gives an induced subgraph isomorphic to the T-product, and there are
  c = N_S / N_T such slices, pairwise disjoint and covering the vertex set.
  Additivity of g gives
      b1(S) - 1 = c * (b1(T) - 1) + N_S * g(U),
  the copy count appearing as the multiplier on the subcomplex's own homology.

P1 -- THE ADDITIVE FORM IS THE CRITERION.  PREDICTION: over every non-empty
  S contained in the first 9 primes and every prime s <= 200 absent from S,
  the truth of s | -chi(S) agrees with g(S) = 1 (mod s) on every pair; and the
  distribution of g over subsets of the first k primes matches the coefficients
  of prod_p (1 + x^{w_s(p)}) mod x^s - 1 exactly, for a spread of s and k.
  KILL (observable): any pair where divisibility and the congruence disagree,
  or any class-count vector differing from the polynomial's coefficients.

P2 -- THE EMBEDDING FORMULA.  PREDICTION: for every T strictly inside every S
  over the first 7 primes, the two sides of S1 agree as integers, and the
  slices are checked rather than assumed -- exactly N_S/N_T of them, pairwise
  disjoint, each an INDUCED subgraph of the big graph isomorphic to the
  T-product (checked by edge count and by degree profile, never by fiat).
  KILL (observable): any T, S with the sides unequal, or a slice that is not
  induced-isomorphic to the T-product, or a count other than N_S/N_T.

P3 -- THE SUBCOMPLEX IS HOMOLOGICALLY INDEPENDENT.  The formula above is
  arithmetic until the inclusion is shown to be seen by homology.  PREDICTION:
  for every T inside every S with N_S <= 210, the map H_1(X(T); F_2) ->
  H_1(X(S); F_2) induced by one slice is INJECTIVE (image rank = b1(T)), and
  the c slices are JOINTLY independent (joint image rank = c * b1(T)).  H_1 is
  free here (b_j = 0 above 1), so injectivity over F_2 gives it over Z.
  KILL (observable): a single-slice image rank below b1(T), or a joint rank
  below c * b1(T).

P4 -- NO SYMMETRY CARRIES THE DIVISIBILITY.  Derived on paper: the factors
  K_{p_i} are Cartesian-prime and pairwise non-isomorphic, so by Sabidussi's
  theorem Aut of the graph -- hence of the clique complex, which has the graph
  as its 1-skeleton -- is Sym(p_1) x ... x Sym(p_m) acting coordinatewise.  An
  element of prime order s has each sigma_j of order 1 or s; a permutation of
  order s on p_j points has p_j - s*(number of s-cycles) fixed points, and
  s does not divide p_j because s is absent, so sigma_j fixes a point.  The
  tuple of those points is a FIXED VERTEX.  So no Z/s acts freely on X(S) for
  any absent s -- while the criterion says s | chi(X(S)) on a positive fraction
  of sub-rings.  PREDICTION: brute-force Aut on the one product small enough to
  enumerate has order |Sym(2)| * |Sym(3)| = 12 (Sabidussi tested, not cited),
  and every randomly built order-s automorphism, over a spread of S and absent
  s, has a fixed vertex.
  KILL (observable): a brute-force Aut order other than 12, or any sampled
  order-s automorphism with no fixed vertex.
  AND THE SAMPLE ALONE CANNOT FAIL, which is why it does not stand alone:
  with s absent, no fixed-point-free coordinate is CONSTRUCTIBLE, so the
  0 it returns is the arithmetic restated and not a test.  C4 below splits
  the instrument from the signal by running the same detector where the
  hypothesis fails.

P5 -- THE WEIGHT LAW AND WHAT IT SUBSUMES.  S0's weight w_s(p) = 1 - p^{-1}
  reads only p mod s, so the criterion is a function of the RESIDUE CENSUS of
  S mod s and nothing else -- no tower structure, no set size.  Four
  consequences, derived on paper here and tested below.
  (a) CENSUS DEPENDENCE: two sub-rings with the same residue census mod s
      agree on whether s names them.
  (b) s-INVISIBILITY: w_s(p) = 0 exactly when p = 1 (mod s), so such a prime
      may be adjoined or deleted without changing naming.  The recorded
      2-invisibility is the degenerate case: mod 2 every odd prime is 1, so
      every weight vanishes and g = 0 can never reach 1.
  (c) 3-DOMINANCE AT EVERY SIZE: mod 3 the weights are 0 (p = 1) and 2
      (p = 2), so s = 3 names S iff #{p in S : p = 2 mod 3} = 2 (mod 3) --
      the recorded C(r_2,2)C(r_1,1) count is this at m = 3.
  (d) THE BASELINE IS AN EXPONENTIAL SUM, not an empirical ratio.  Counting by
      characters of Z/s, #{S : g(S) = 1} = (1/s) sum_j zeta^{-j} prod_p
      (1 + zeta^{j w_p}), so
          |count - 2^n/s|  <=  ((s-1)/s) * 2^n * max_{j != 0} prod_p
                               |cos(pi * j * w_p / s)|,
      and every factor with w_p != 0 is at most cos(pi/s) < 1.  So the naming
      fraction goes to 1/s exponentially in the number of pool primes that are
      not 1 mod s -- the recorded 1/s baseline as a bound rather than a fit,
      and transparency-independent because the weight reads only p mod s.
  PREDICTION: (a), (b), (c) hold with no counterexample over subsets of the
  first 12 primes for a spread of s; the measured |count - 2^n/s| sits under
  the (d) bound in every case.
  KILL (observable): any counterexample to (a), (b) or (c); any measured
  deviation above the printed bound.

POSITIVE CONTROLS (run and read BEFORE any verdict below them).
  C1  The homology engine on this file's own slice indexing reproduces the
      closed form for b1 on every complex used in P3, computed from GF(2)
      boundary ranks over the big-graph edge index.
  C2  A NEGATIVE control on P1: the off-by-one congruence sum 1/p_i = m
      (mod s) must FAIL somewhere, else the agreement in P1 is vacuous.
  C3  A NEGATIVE control on P3: a cycle basis of a RANDOM induced subgraph of
      the same vertex count as a slice must not be forced to full rank -- the
      rank routine is shown able to report a deficiency at all.
  C4  A NEGATIVE control on P4: the fixed-vertex detector run on complexes
      whose factor SIZES are divisible by s -- legitimate complexes, primality
      being unused in the b1 form -- where an order-s element covering such a
      coordinate by s-cycles genuinely has no fixed vertex.  The detector must
      report free there, or its 0 above measures nothing.

FINDINGS (entered after the run; every prediction survived).

F1  THE CRITERION IS A WEIGHT SUM, and the set size is not part of it.
  21,202 (S, s) pairs over the first 9 primes and every absent prime s <= 200:
  s | -chi(S) and g(S) = 1 (mod s) agree on all 21,202, with 473 namings among
  them.  The off-by-one congruence sum 1/p_i = m disagrees with divisibility on
  777 of the pairs it was run over, so the agreement is not vacuous.  Class
  counts match the coefficients of prod_p (1 + x^{w_s(p)}) mod x^s - 1 exactly
  at (s,k) = (5,8), (7,9), (11,9), (13,7), (29,9).  Tier: RULE (proved from
  -chi = N(g - 1) with gcd(N,s) = 1; exhaustive over the stated range).

F2  THE WEIGHT READS ONLY p mod s, so naming reads only the RESIDUE CENSUS.
  Exhaustively over all 2,047 non-empty sub-rings of the pool at each of
  s = 3, 5, 7, 11, 13: 0 census violations (41 to 1,151 distinct censuses
  each); 3,392 adjunctions of a prime p = 1 (mod s) changed naming 0 times.
  Recorded 2-invisibility is the
  degenerate case (mod 2 every odd prime has weight 0, so g = 0 never reaches
  1) and needs no parity argument of its own.  Recorded 3-dominance holds at
  EVERY size in the form "named iff #{p = 2 mod 3} = 2 (mod 3)": 0 violations
  over all 2,047 sub-rings of the pool, and it returns the recorded 18/35 at
  m = 3, k = 8.  Tier: RULE (one-line proof from the weight law; exhaustive
  over the stated pool).

F3  THE 1/s BASELINE IS A BOUND, NOT A FIT.  |count - 2^n/s| sits under the
  character-sum bound in all 10 (s, n) cells run, s in {3,5,7,11,13} and
  n in {6,9}; the bound decays like cos(pi/s)^t in the number t of pool primes
  not 1 mod s, so the naming fraction converges to 1/s exponentially.  This
  upgrades the recorded naming baseline from a k=25 pattern to a proved rule,
  and it supplies the reason the baseline was measured to be
  transparency-independent: the weight is a function of p mod s alone, and no
  tower quantity enters.  Tier: RULE (proved; the run is the numerical check).

F4  THE EMBEDDING FORMULA, with the copy count as the multiplier.
  b1(S) - 1 = c*(b1(T) - 1) + N_S * g(S minus T), c = N_S/N_T, holds on all
  1,932 (S, T) pairs over the first 7 primes; the slices were checked rather
  than assumed (count, disjointness, cover, induced edge count and degree
  profile) with 0 failures.  So the criterion travels along the embedding
  exactly when the complement block is s-neutral, and the copy count is where
  the sub-ring's own homology enters.  Tier: RULE.

F5  THE COPIES ARE HOMOLOGICALLY INDEPENDENT.  Over 28 complexes with
  N <= 210, the map H_1(X(T); F_2) -> H_1(X(S); F_2) from one slice has image
  rank exactly b1(T) in every case, and the c slices jointly have rank exactly
  c*b1(T): 0 single-slice failures, 0 joint failures.  H_1 is free here, so
  injectivity over F_2 gives it over Z.  The positive control (b1 from GF(2)
  boundary ranks against the closed form) is ok on all 28 before any of this is
  read, and the negative control shows the rank routine reporting a deficiency
  where one exists -- a random induced subgraph on 10 vertices of X({2,3,5})
  carries 3 independent cycles and image rank 0, all three being boundaries of
  lines.  Tier: RULE over the stated range.

F6  THE DIVISIBILITY IS NOT SYMMETRY-BORNE -- and this is the one thing the
  homology says that the factorization cannot.  s names S iff s | b1(S) - 1
  iff X(S) is homotopy equivalent to a connected s-fold cover of a graph with
  b1 = (b1(S) - 1)/s + 1, which the run prints for the named sub-rings.  But
  no Z/s acts freely on X(S) for any absent s: every automorphism of prime
  order s fixes a vertex, because Aut is the coordinatewise Sym(p_1) x ... x
  Sym(p_m) and s divides no p_i.  Brute-force Aut(K_2 [] K_3) = 12 = |Sym(2)| *
  |Sym(3)| confirms the structure theorem on the one case small enough to
  enumerate; 94 sampled non-identity order-s automorphisms across five S and
  five absent s gave 0 without a fixed vertex -- and that 0 is only worth
  reading because C4 makes the same detector say FREE on all three complexes
  whose sizes s divides, which is where the absence hypothesis is doing the
  work.  C4 also caught its own first version: a control putting ONE s-cycle
  on a coordinate of size 4 leaves two points fixed, and the detector said so.  So the covering exists only up
  to homotopy, and X(S) is no REGULAR s-fold cover: the quotient graph is
  X(S) modulo no symmetry it has, which is as far as a free-action argument
  reaches -- a non-regular covering map out of X(S) is untouched by it.  The
  classical route from a prime to an Euler characteristic is unavailable.
  Tier: RULE (proved; the run is the check).

WHAT THIS SETTLES.  The homology supplies the OBJECT and the embedding law,
and it supplies one negative that arithmetic could not state.  The arithmetic
content of the criterion is carried entirely by the weight law: naming is a
level set of a linear functional whose weights read p mod s, which subsumes
2-invisibility, generalizes 3-dominance to every size, and turns the 1/s
baseline into a bound.  No new statement about H_1 beyond the embedding law
was found; the criterion is not a statement about the complex's symmetry, and
the run says why it cannot be.

RUN RECORD.  One process, 0.7 s wall clock, pure-python bitsets (no numpy, no
BLAS), peak footprint far under the 512MB analysis default; the largest
complex handled is X({2,3,5,7}) at 210 vertices, 1,365 edges, 1,540 triangles.

Run: python prime/code/explore_naming_complex.py
"""

import sys
sys.path.insert(0, '.')
from itertools import combinations
from math import prod
from random import Random

from prime.code.crt import is_prime

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def section(title):
    print(f"\n{'=' * 76}")
    print(f"  {title}")
    print(f"{'=' * 76}")


def neg_chi(ps):
    N = prod(ps)
    return N * (len(ps) - 1) - sum(N // p for p in ps)


def b1_form(ps):
    return neg_chi(ps) + 1


def g_mod(ps, s):
    """sum_{p in S} (1 - p^{-1})  in  Z/s."""
    return sum(1 - pow(p, -1, s) for p in ps) % s


# ── the product graph, with coordinates kept ───────────────────────────

def build(mods):
    """Vertices 0..N-1 in mixed radix over `mods`; adjacency sets."""
    nv = prod(mods)
    coords = []
    for v in range(nv):
        c, x = [], v
        for m in mods:
            c.append(x % m)
            x //= m
        coords.append(tuple(c))
    adj = [set() for _ in range(nv)]
    for a in range(nv):
        for b in range(a + 1, nv):
            if sum(1 for i in range(len(mods)) if coords[a][i] != coords[b][i]) == 1:
                adj[a].add(b)
                adj[b].add(a)
    return coords, adj, nv


def slices(mods, keep):
    """Vertex lists of the N/N_T parallel copies of the `keep`-subproduct."""
    coords, _, nv = build(mods)
    drop = [i for i in range(len(mods)) if i not in keep]
    buckets = {}
    for v in range(nv):
        key = tuple(coords[v][i] for i in drop)
        buckets.setdefault(key, []).append(v)
    return list(buckets.values())


# ── GF(2) linear algebra and homology ──────────────────────────────────

def gf2_rank(rows):
    pivots = {}
    rank = 0
    for r in rows:
        while r:
            top = r.bit_length() - 1
            if top not in pivots:
                pivots[top] = r
                rank += 1
                break
            r ^= pivots[top]
    return rank


def edges_of(adj, nv):
    return [(a, b) for a in range(nv) for b in sorted(adj[a]) if b > a]


def triangles_of(adj, edges):
    tris = []
    for a, b in edges:
        for c in sorted(adj[a] & adj[b]):
            if c > b:
                tris.append((a, b, c))
    return tris


def cycle_basis(verts, adj, eidx):
    """Fundamental cycles of the induced subgraph on `verts`, as bitmasks
    over the AMBIENT edge index -- one per non-tree edge."""
    vset = set(verts)
    seen, parent, order = set(), {}, []
    for root in verts:
        if root in seen:
            continue
        seen.add(root)
        parent[root] = None
        stack = [root]
        while stack:
            u = stack.pop()
            order.append(u)
            for w in sorted(adj[u] & vset):
                if w not in seen:
                    seen.add(w)
                    parent[w] = u
                    stack.append(w)
    tree = set()
    for v in verts:
        if parent.get(v) is not None:
            tree.add((min(v, parent[v]), max(v, parent[v])))
    depth = {}
    for v in order:
        depth[v] = 0 if parent[v] is None else depth[parent[v]] + 1
    cycles = []
    for a in verts:
        for b in sorted(adj[a] & vset):
            if b <= a or (a, b) in tree:
                continue
            mask = 1 << eidx[(a, b)]
            u, w = a, b
            while u != w:
                if depth[u] >= depth[w]:
                    mask ^= 1 << eidx[(min(u, parent[u]), max(u, parent[u]))]
                    u = parent[u]
                else:
                    mask ^= 1 << eidx[(min(w, parent[w]), max(w, parent[w]))]
                    w = parent[w]
            cycles.append(mask)
    return cycles


def boundary_rows(tris, eidx):
    rows = []
    for a, b, c in tris:
        rows.append((1 << eidx[(a, b)]) | (1 << eidx[(a, c)]) | (1 << eidx[(b, c)]))
    return rows


# ── P1: the additive form ──────────────────────────────────────────────

def run_additive():
    section("P1  THE ADDITIVE FORM IS THE CRITERION")
    small_primes = [p for p in range(2, 201) if is_prime(p)]
    pairs = agree = named = 0
    bad = []
    for m in range(1, len(PRIMES) + 1):
        for S in combinations(PRIMES, m):
            nc = neg_chi(list(S))
            for s in small_primes:
                if s in S:
                    continue
                pairs += 1
                divides = (nc % s == 0)
                congruent = (g_mod(S, s) == 1)
                if divides == congruent:
                    agree += 1
                else:
                    bad.append((S, s, divides, congruent))
                named += divides
    print(f"  (S, s) pairs tested: {pairs}   agreements: {agree}   "
          f"disagreements: {len(bad)}")
    print(f"  pairs where s names S: {named}")
    for row in bad[:5]:
        print(f"    MISMATCH {row}")

    print("\n  C2  NEGATIVE CONTROL -- the off-by-one congruence sum 1/p = m")
    wrong = 0
    for m in range(1, 6):
        for S in combinations(PRIMES, m):
            nc = neg_chi(list(S))
            for s in small_primes[:15]:
                if s in S:
                    continue
                off = (sum(pow(p, -1, s) for p in S) % s) == (len(S) % s)
                if off != (nc % s == 0):
                    wrong += 1
    print(f"  disagreements of the WRONG congruence with divisibility: {wrong}")

    print("\n  the class counts against prod_p (1 + x^w) mod x^s - 1")
    for s, k in [(5, 8), (7, 9), (11, 9), (13, 7), (29, 9)]:
        pool = [p for p in PRIMES[:k] if p != s]
        poly = [0] * s
        poly[0] = 1
        for p in pool:
            w = (1 - pow(p, -1, s)) % s
            new = [0] * s
            for i, v in enumerate(poly):
                new[i] += v
                new[(i + w) % s] += v
            poly = new
        counts = [0] * s
        for m in range(len(pool) + 1):
            for S in combinations(pool, m):
                counts[g_mod(S, s) if S else 0] += 1
        ok = counts == poly
        print(f"  s={s:<3} k={k}  classes match polynomial: {ok}   "
              f"named class {counts[1]}/{2 ** len(pool)}  "
              f"(1/s share = {2 ** len(pool) / s:.1f})")


# ── P2: the embedding formula ──────────────────────────────────────────

def run_embedding():
    section("P2  THE EMBEDDING FORMULA")
    checked = mismatch = slicebad = 0
    shown = 0
    for m in range(2, 8):
        for S in combinations(PRIMES[:7], m):
            NS = prod(S)
            for t in range(1, m):
                for T in combinations(S, t):
                    NT = prod(T)
                    U = [p for p in S if p not in T]
                    c = NS // NT
                    lhs = b1_form(list(S)) - 1
                    rhs = c * (b1_form(list(T)) - 1) + sum(NS - NS // p for p in U)
                    checked += 1
                    if lhs != rhs:
                        mismatch += 1
                        print(f"    MISMATCH S={S} T={T}  {lhs} != {rhs}")
                    if shown < 4 and NS <= 210:
                        print(f"  S={str(S):<18} T={str(T):<14} c={c:<4} "
                              f"b1(S)-1={lhs:<6} = {c}*{b1_form(list(T)) - 1} + "
                              f"{sum(NS - NS // p for p in U)}")
                        shown += 1
    print(f"  (S, T) pairs tested: {checked}   mismatches: {mismatch}")

    print("\n  the slices checked rather than assumed (N_S <= 210)")
    for m in range(2, 5):
        for S in combinations(PRIMES[:5], m):
            if prod(S) > 210:
                continue
            mods = list(S)
            _, adj, nv = build(mods)
            for t in range(1, m):
                for keep in combinations(range(m), t):
                    T = [mods[i] for i in keep]
                    parts = slices(mods, set(keep))
                    ok = len(parts) == prod(S) // prod(T)
                    ok &= len({v for pt in parts for v in pt}) == nv
                    _, tadj, tnv = build(T)
                    tedges = sum(len(tadj[v]) for v in range(tnv)) // 2
                    tdeg = sorted(len(tadj[v]) for v in range(tnv))
                    for pt in parts:
                        ps = set(pt)
                        deg = sorted(len(adj[v] & ps) for v in pt)
                        e = sum(deg) // 2
                        if len(pt) != tnv or e != tedges or deg != tdeg:
                            ok = False
                    if not ok:
                        slicebad += 1
                        print(f"    SLICE FAIL S={S} T={T}")
    print(f"  slice failures: {slicebad}")


# ── P3: homological independence of the copies ─────────────────────────

def run_homology():
    section("C1 / P3  THE SLICES IN H_1 OF THE BIG COMPLEX")
    cases = []
    for m in range(2, 5):
        for S in combinations(PRIMES[:6], m):
            if prod(S) <= 210:
                cases.append(list(S))
    print(f"  complexes: {[tuple(c) for c in cases]}")

    print("\n  C1  POSITIVE CONTROL -- b1 from GF(2) boundary ranks vs the form")
    engines = {}
    for mods in cases:
        _, adj, nv = build(mods)
        edges = edges_of(adj, nv)
        eidx = {e: i for i, e in enumerate(edges)}
        tris = triangles_of(adj, edges)
        brows = boundary_rows(tris, eidx)
        r2 = gf2_rank(brows)
        r1 = gf2_rank([(1 << a) | (1 << b) for a, b in edges])
        b1 = len(edges) - r1 - r2
        engines[tuple(mods)] = (adj, nv, eidx, brows, r2)
        flag = "ok" if b1 == b1_form(mods) else "FAIL"
        print(f"  {str(tuple(mods)):<18} N={nv:<5} E={len(edges):<6} "
              f"tri={len(tris):<6} b1={b1:<7} form={b1_form(mods):<7} {flag}")

    print("\n  P3  single-slice and joint image ranks in H_1(X(S); F_2)")
    single_bad = joint_bad = 0
    for mods in cases:
        adj, nv, eidx, brows, r2 = engines[tuple(mods)]
        m = len(mods)
        for t in range(1, m):
            for keep in combinations(range(m), t):
                T = [mods[i] for i in keep]
                parts = slices(mods, set(keep))
                c = len(parts)
                one = cycle_basis(parts[0], adj, eidx)
                r_one = gf2_rank(brows + one) - r2
                allc = []
                for pt in parts:
                    allc.extend(cycle_basis(pt, adj, eidx))
                r_all = gf2_rank(brows + allc) - r2
                exp1, expc = b1_form(T) , c * b1_form(T)
                s1 = "ok" if r_one == exp1 else "FAIL"
                sc = "ok" if r_all == expc else "FAIL"
                single_bad += r_one != exp1
                joint_bad += r_all != expc
                print(f"  S={str(tuple(mods)):<16} T={str(tuple(T)):<14} c={c:<4} "
                      f"one={r_one}/{exp1} {s1:<4} joint={r_all}/{expc} {sc:<4} "
                      f"b1(S)={b1_form(mods)}")
    print(f"  single-slice failures: {single_bad}   joint failures: {joint_bad}")

    print("\n  C3  NEGATIVE CONTROL -- the rank routine can report a deficiency")
    mods = [2, 3, 5]
    adj, nv, eidx, brows, r2 = engines[(2, 3, 5)]
    rng = Random(20250609)
    for size in (6, 10):
        vs = sorted(rng.sample(range(nv), size))
        cyc = cycle_basis(vs, adj, eidx)
        r = gf2_rank(brows + cyc) - r2
        print(f"  random induced subgraph on {size} vertices: "
              f"{len(cyc)} independent cycles, image rank {r}")


# ── P4: the symmetry obstruction ───────────────────────────────────────

def run_symmetry():
    section("P4  NO FREE ACTION -- THE DIVISIBILITY IS NOT SYMMETRY-BORNE")
    from itertools import permutations
    _, adj, nv = build([2, 3])
    count = 0
    for perm in permutations(range(nv)):
        if all((perm[b] in adj[perm[a]]) for a in range(nv) for b in adj[a]):
            count += 1
    print(f"  C-control  brute-force |Aut(K_2 [] K_3)| = {count}   "
          f"|Sym(2) x Sym(3)| = 12   "
          f"{'ok' if count == 12 else 'FAIL'}")

    rng = Random(59)
    free_found = 0
    trials = 0
    print("\n  order-s automorphisms built at random, over absent s")
    for S in [(2, 3, 5), (3, 5, 7), (2, 5, 11), (3, 7, 11), (2, 3, 5, 7)]:
        for s in (3, 5, 7, 11, 13):
            if s in S:
                continue
            for _ in range(40):
                sigmas = []
                for p in S:
                    pts = list(range(p))
                    rng.shuffle(pts)
                    sigma = list(range(p))
                    ncyc = rng.randrange(0, p // s + 1)
                    for j in range(ncyc):
                        cyc = pts[j * s:(j + 1) * s]
                        for i in range(s):
                            sigma[cyc[i]] = cyc[(i + 1) % s]
                    sigmas.append(sigma)
                if all(sg == list(range(len(sg))) for sg in sigmas):
                    continue
                trials += 1
                fixpts = [[x for x in range(len(sg)) if sg[x] == x] for sg in sigmas]
                if any(not f for f in fixpts):
                    free_found += 1
    print(f"  non-identity order-s automorphisms sampled: {trials}   "
          f"with NO fixed vertex: {free_found}")

    print("\n  NEGATIVE CONTROL -- the detector must report a free element "
          "where")
    print("  the hypothesis fails, i.e. where s DOES divide a factor size.")
    for mods, s in [([2, 3, 5], 5), ([2, 3, 5], 3), ([4, 9], 2)]:
        sigmas = []
        for q in mods:
            sigma = list(range(q))
            if q % s == 0:
                for c in range(q // s):
                    base = c * s
                    for i in range(s):
                        sigma[base + i] = base + (i + 1) % s
            sigmas.append(sigma)
        fixpts = [[x for x in range(len(sg)) if sg[x] == x] for sg in sigmas]
        free = any(not f for f in fixpts)
        print(f"  sizes {str(tuple(mods)):<12} s={s}  divides a size: "
              f"{any(q % s == 0 for q in mods)}   detector says fixed-point-free: "
              f"{free}")
    print("\n  the covering reading, on the named sub-rings of the first 7 primes")
    shown = 0
    for m in range(2, 5):
        for S in combinations(PRIMES[:7], m):
            nc = neg_chi(list(S))
            for s in [p for p in range(2, 60) if is_prime(p) and p not in S]:
                if nc % s == 0 and shown < 8:
                    print(f"  s={s:<4} names {str(S):<18} b1-1={nc:<8} "
                          f"quotient graph b1 = {nc // s + 1}")
                    shown += 1


def run_weight_law():
    section("P5  THE WEIGHT LAW AND WHAT IT SUBSUMES")
    pool12 = [p for p in range(2, 40) if is_prime(p)][:12]
    print(f"  pool: {pool12}")

    print("\n  (a) naming depends only on the residue census mod s")
    census_bad = 0
    for s in (3, 5, 7, 11, 13):
        table = {}
        pool = [p for p in pool12 if p != s]
        for m in range(1, len(pool) + 1):
            for S in combinations(pool, m):
                key = tuple(sorted(p % s for p in S))
                named = neg_chi(list(S)) % s == 0
                if key in table and table[key] != named:
                    census_bad += 1
                table[key] = named
        print(f"  s={s:<3} sub-rings {2 ** len(pool) - 1:<5} "
              f"distinct censuses {len(table):<5} "
              f"censuses disagreeing on naming: {census_bad}")
    print(f"  total census violations: {census_bad}")

    print("\n  (b) s-invisibility: p = 1 (mod s) can be adjoined or deleted freely")
    inv_bad = inv_tested = 0
    for s in (3, 5, 7, 11, 13, 17):
        invisible = [p for p in pool12 if p % s == 1 and p != s]
        others = [p for p in pool12 if p != s and p % s != 1]
        for q in invisible:
            for m in range(0, len(others) + 1):
                for S in combinations(others, m):
                    inv_tested += 1
                    a = neg_chi(list(S)) % s == 0
                    b = neg_chi(sorted(S + (q,))) % s == 0
                    inv_bad += a != b
        print(f"  s={s:<3} invisible primes in pool: {invisible}")
    print(f"  adjunctions tested: {inv_tested}   naming changed: {inv_bad}")

    print("\n  (c) 3-dominance at every size: named iff #{p = 2 mod 3} = 2 (mod 3)")
    dom_bad = 0
    dom_pool = [p for p in pool12 if p != 3]
    for m in range(1, len(dom_pool) + 1):
        for S in combinations(dom_pool, m):
            named = neg_chi(list(S)) % 3 == 0
            rule = sum(1 for p in S if p % 3 == 2) % 3 == 2
            dom_bad += named != rule
    print(f"  violations over all {2 ** len(dom_pool) - 1} sub-rings of the "
          f"pool: {dom_bad}")
    k8 = [2, 3, 5, 7, 11, 13, 17, 19]
    others = [p for p in k8 if p != 3]
    hit = sum(1 for S in combinations(others, 3)
              if sum(1 for p in S if p % 3 == 2) % 3 == 2)
    print(f"  the recorded m=3 count at k=8: {hit}/{len(list(combinations(others, 3)))}")

    print("\n  (d) the baseline as an exponential-sum bound, not a fit")
    import cmath
    for s in (3, 5, 7, 11, 13):
        for n in (6, 9, 12):
            pool = [p for p in pool12 if p != s][:n]
            if len(pool) < n:
                continue
            w = [(1 - pow(p, -1, s)) % s for p in pool]
            exact = sum(1 for m in range(len(pool) + 1)
                        for S in combinations(pool, m)
                        if sum((1 - pow(p, -1, s)) for p in S) % s == 1)
            total = 2 ** len(pool)
            bound = (s - 1) / s * total * max(
                abs(prod(cmath.cos(cmath.pi * j * wp / s) for wp in w))
                for j in range(1, s))
            dev = abs(exact - total / s)
            flag = "ok" if dev <= bound + 1e-9 else "FAIL"
            print(f"  s={s:<3} n={n:<3} named {exact}/{total} = "
                  f"{exact / total:.4f}  (1/s = {1 / s:.4f})  "
                  f"|dev|={dev:.2f} <= bound {bound:.2f}  {flag}")


def main():
    print("=" * 76)
    print("  THE NAMING CRITERION AS A STATEMENT ABOUT THE CLIQUE COMPLEX")
    print("=" * 76)
    run_additive()
    run_embedding()
    run_homology()
    run_symmetry()
    run_weight_law()


if __name__ == "__main__":
    main()
