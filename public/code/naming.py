"""naming.py -- which primes divide the Euler characteristic of a set.

QUESTION. Take a finite set S of primes, N = the product of S, m = |S|,
and the ring Z/N read through its m channels. Its HAMMING GRAPH joins
two residues that differ in exactly one channel: the Cartesian product
of the complete graphs K_p, p in S. Fill in every clique and call the
result X(S), the CLIQUE COMPLEX. What is its homotopy type, what is
its Euler characteristic chi, and which primes s outside S divide -chi
(s NAMES S)?

THE ARGUMENT (written before this script).
  (1) THE COMPLEX. Sizes n_1..n_m >= 2, not necessarily prime. If u, v
      differ in coordinate i and v, w in coordinate j != i, then u, w
      differ in both and are not adjacent; so a clique lies in a LINE
      (all coordinates but one fixed). The maximal cliques are the
      L = sum_i N/n_i lines, two lines meet in at most one vertex, and
      every vertex lies on m lines. Replace each line (a simplex) by
      the cone on its vertices: both are contractible and glued along
      the same vertex set, so X is homotopy equivalent to the
      bipartite VERTEX-LINE GRAPH B, which has N + L vertices and mN
      edges and is connected. So X is a wedge of circles with
          b1 = mN - N - L + 1 = 1 + N (m - 1 - sum_i 1/n_i),
      b_j = 0 for j >= 2, and -chi = b1 - 1.
      b1 = N exactly when sum 1/n_i = m - 2 + 1/N. Sizes >= 2 give
      sum 1/n_i <= m/2, so m <= 3; m = 1 and m = 2 are impossible
      (m = 2 would need n_1 + n_2 = 1); at m = 3 the sum exceeds 1, so
      the least size is 2, and then (n_2 - 2)(n_3 - 2) = 3: the sizes
      are {2, 3, 5} and nothing else.
  (2) THE INTEGER. For primes, -chi(S) = N (g - 1) with
      g = sum over S of (1 - 1/p). Modulo a member p every term of
      N (m - 1) - sum over r in S of N/r vanishes but -N/p, which is
      prime to p: no member divides -chi. Modulo 2 with every member
      odd, -chi is (m - 1) - m = -1: -chi is odd, so 2 never names.
      g is the mean Hamming distance from any point of Z/N, since a
      uniform residue differs from a fixed one at p with chance
      1 - 1/p; so -chi = sum over x of (d(0, x) - 1), d the
      Hamming distance, the number of channels where two residues
      differ. Both sides count mN - N - L: the reading is a recount,
      not a second fact.
  (3) THE WEIGHT LAW. For a prime s not in S, N is invertible mod s,
      so s | -chi iff g = 1 in Z/s, that is iff the WEIGHTS
      w_s(p) = 1 - p^(-1) mod s over S sum to 1. Naming therefore
      depends only on S's residues mod s; a prime p = 1 mod s has
      weight 0 and is invisible; mod 3 the weights are 0 (p = 1) and 2
      (p = 2), so 3 names S iff #{p in S : p = 2 mod 3} = 2 mod 3.
      A pool of primes has a set that s names iff 1 is a subset sum of the
      weights; the empty sum is 0 and a singleton's -chi is -1, so
      nothing smaller cheats. By Cauchy-Davenport, adding a nonzero
      weight to a subset-sum set A of Z/s gives at least
      min(s, |A| + 1) sums; so s - 1 primes of nonzero weight reach
      every residue, and every prime s >= 3 names a set once the rung
      holds s - 1 primes other than s that are not 1 mod s.
  (4) THE BASELINE. Over a pool P of primes not containing s,
      #{S in P : s names S} = (1/s) sum_j e(-j/s) prod_p (1 + e(j w_p / s)),
      and |1 + e(t)| = 2|cos(pi t)|, so the count differs from 2^|P|/s
      by at most ((s - 1)/s) 2^|P| max_{j != 0} prod_p |cos(pi j w_p / s)|,
      each factor with w_p != 0 at most cos(pi / s) < 1.
  (5) THE SLICES. For T inside S, fixing the coordinates of S \\ T cuts
      X(S)'s vertices into c = N_S / N_T SLICES, each an induced copy of
      X(T). In B each slice is a subgraph (its vertices and its
      T-lines), the slices are disjoint, and a subgraph's cycle space
      is a subspace of the graph's; so the slices' first homology
      injects jointly, rank c b1(T). The count identity
      b1(S) - 1 = c (b1(T) - 1) + N_S sum over S \\ T of (1 - 1/p)
      is (2)'s algebra, not a finding.
  (6) NO SYMMETRY. For distinct prime sizes, Aut(X(S)) is the product
      of the Sym(p) acting coordinatewise (the Hamming graph's
      automorphisms, its factors being Cartesian-prime and pairwise
      non-isomorphic). An automorphism of prime order s not in S has
      each component of order 1 or s, with p - s k fixed points, k its
      number of s-cycles, never 0 since s does not divide p; so it fixes a
      vertex. s | b1 - 1 says X is homotopy equivalent to an s-fold
      cover of a graph, and no simplicial Z/s action on X supplies it.

DESIGN. Sections of checks printing PASS or FAIL.
  X  the complex. For twenty size tuples (primes, repeats, non-primes,
     m = 1..4): the Hamming graph's cliques are enumerated from the
     adjacency alone (common neighbours), never from lines; the GF(2)
     Betti numbers b0..b3 come from boundary ranks. Bron-Kerbosch lists
     the maximal cliques to check they are the lines. Then an exhaustive
     search for b1 = N over size multisets: m = 1, 2, 3 with sizes to
     60, m = 4 to 30, m = 5 to 12. POSITIVE CONTROL first: the engine on a
     hollow hexagon (1, 1, 0), two filled triangles (2, 0, 0) and a
     tetrahedron's boundary (1, 0, 1), the last proving the b2 column
     can print a nonzero.
  I  the integer, over every nonempty S in the first nine primes:
     -chi odd, prime to every member; and, by brute force over Z/N for
     every S in the first five primes, -chi = sum (d(0, x) - 1),
     d the Hamming distance, the number of channels where two
     residues differ.
  W  the weight law over every (S, s), S nonempty in the first nine
     primes, s prime <= 200 outside S; the mod-3 count over every S in
     the first twelve primes without 3. POSITIVE CONTROL: the law with
     weight p^(-1) in place of 1 - p^(-1) must fail. Then, for every
     prime s < 200, the first rung at which s names a set, read two ways
     -- by -chi over every S in the first twelve primes, and by a
     subset-sum walk of the weights to rung 60 -- against the
     Cauchy-Davenport rung.
  B  the baseline: s in {3, 5, 7, 11, 13}, P the first 6 and the first 9
     primes other than s; the count, 2^|P|/s and the bound. An
     all-invisible pool (the primes 1 mod 3 below 50, s = 3) must
     count exactly 0.
  S  the slices: every pair T inside S, both nonempty and T != S, S
     inside {2, 3, 5, 7} of two or more primes. The rank of the slices'
     cycles in H1(X(S)) over GF(2) is rank(D + Z1(slices)) - rank(D), D
     the triangle boundaries. POSITIVE CONTROL first: the cycles of
     one line's edge graph (a boundary, since the line is a simplex)
     must map to rank 0.
  A  automorphisms: |Aut| of the Hamming graph by brute force over all
     vertex permutations at sizes (2, 3), after a POSITIVE CONTROL at
     (2, 2), where equal sizes let the factors swap. Then, for three
     (S, s) with s outside S, every element of order s in the product
     of the Sym(p) fixes a vertex, after a CONTROL s = 5 inside
     S = {2, 5, 7}, where a free one exists.

PREDICTIONS, fixed before the run.
  X0 the three control complexes read (1, 1, 0), (2, 0, 0), (1, 0, 1).
  X1 b1 = 1 + N (m - 1 - sum 1/n) on all twenty tuples: 2, 4, 8, 24 at
     (2,3), (2,5), (3,5), (5,7); 1, 4, 0, 3, 15 at (2,2), (3,3), (4),
     (2,4), (4,6); 5, 23 at (2,2,2), (2,3,4); 30, 44, 82, 140, 74 at
     (2,3,5), (2,3,7), (2,5,7), (3,5,7), (3,4,5); 49, 17, 384, 89 at
     (2,2,3,3), (2,2,2,2), (2,3,5,7), (2,2,3,5). b0 = 1, b2 = b3 = 0
     everywhere.
  X2 the maximal cliques are L lines, N/n_i of size n_i, meeting
     pairwise in at most one vertex.
  X3 the only size multiset with b1 = N is {2, 3, 5}.
  I1 0 exceptions over 511 sets; I2 0 exceptions over 31 sets.
  W1 0 violations over 21,202 pairs; W2 0 violations; W0 the control
     shows violations.
  W3 the two first-naming rungs agree wherever both are defined; 2 names
     no set; 41 first names one at rung 8 ({17, 19}, whose -chi
     is 287 = 7 * 41); every odd prime below 200 names one by rung 11;
     every first rung sits at or below the Cauchy-Davenport rung.
  B1 each count within its bound, in all ten cells; B2 exactly 0.
  S1 image rank = c b1(T) at all 50 pairs; S0 the control reads 0.
  A1 |Aut| = 12 = 2! 3!; A0 |Aut| = 8 at (2, 2), not 2! 2! = 4.
  A2 no free element of order s; A3 the control finds free ones.

FINDINGS. Every prediction landed: 21/21 checks PASS, the controls
first.
  X0 the controls read (1, 1, 0), (2, 0, 0) and (1, 0, 1).
  X1 X2 all twenty tuples print b = (1, b1, 0, 0) with b1 the formula's,
     from 2 at (2, 3) to 384 at (2, 3, 5, 7); the maximal cliques are
     the lines and meet in at most one vertex. X3 the search finds
     (2, 3, 5) alone. (X2 was widened
     after the first run to test that each maximal clique varies in
     exactly one coordinate; it passes.)
  I1 511 sets, 0 exceptions; I2 31 sets, 0 exceptions.
  W0 the wrong weight shows 962 violations; W1 21,202 pairs, 0
     violations; W2 2,047 sets, 0 violations.
  W3 the scan and the walk agree at every prime below 200; 2 names no
     set; 41 first at rung 8, through {17, 19}, whose -chi is
     287 = 7 * 41; the first rungs run 3 to 9, the
     largest prime first naming a set at rung 9 being 167, every one at or
     below its Cauchy-Davenport rung and meeting it only at s = 3 (the
     meeting asserted after the slate froze).
  B1 all ten cells inside the bound (at s = 13, |P| = 6 the bound, 9.80,
     exceeds 2^6/13 itself: six primes do not yet force the count);
     B2 0.
  S1 50 pairs, image rank c b1(T) at every one, 22 of them with T of two
     or more primes and so a nonzero rank; S0 six cycles, image 0.
  A1 12; A0 8. A2 7,370, 24,127 and 504 elements of order s, none free;
     A3 12,120 of 12,624 elements of order 5 are free.
  Tiers: the complex is a theorem, proved in (1), b1 = N at {2, 3, 5}
  alone with it; (2) is a property; the weight law a criterion, and
  every odd prime eventually naming a set a theorem; the baseline, the
  slices and the fixed vertex are theorems. Every check is a
  witness in range, never the proof.

Run record: 21/21 PASS, 0.2 s, peak commit 10.7 MB under a memory guard.

Standard library only.

    python naming.py
"""

from itertools import combinations, combinations_with_replacement, \
    permutations, product
from math import cos, pi, prod

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" -- {detail}" if detail else ""))


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


PRIMES = [p for p in range(2, 2000) if is_prime(p)]


def neg_chi(S):
    N = prod(S)
    return N * (len(S) - 1) - sum(N // p for p in S)


# ---- homology over GF(2) ----------------------------------------------

def rank(rows):
    pivots, r = {}, 0
    for v in rows:
        while v:
            h = v.bit_length() - 1
            if h in pivots:
                v ^= pivots[h]
            else:
                pivots[h] = v
                r += 1
                break
    return r


def boundary_rows(upper, lower):
    index = {s: i for i, s in enumerate(lower)}
    rows = []
    for s in upper:
        v = 0
        for face in combinations(s, len(s) - 1):
            v |= 1 << index[face]
        rows.append(v)
    return rows


def betti(simplices, top=3):
    """simplices[d] = sorted tuples of dimension d; b_0..b_top."""
    ranks = [0]
    for d in range(1, top + 2):
        upper = simplices[d] if d < len(simplices) else []
        ranks.append(rank(boundary_rows(upper, simplices[d - 1]))
                     if upper else 0)
    counts = [len(simplices[d]) if d < len(simplices) else 0
              for d in range(top + 1)]
    return [counts[d] - ranks[d] - ranks[d + 1] for d in range(top + 1)]


def closure(maximal):
    faces = set()
    for s in maximal:
        for r in range(1, len(s) + 1):
            faces.update(combinations(sorted(s), r))
    top = max(len(f) for f in faces)
    return [sorted(f for f in faces if len(f) == d + 1) for d in range(top)]


# ---- the Hamming graph and its cliques --------------------------------

def hamming(sizes):
    verts = list(product(*[range(n) for n in sizes]))
    adj = [set() for _ in verts]
    for i, u in enumerate(verts):
        for j in range(i + 1, len(verts)):
            if sum(a != b for a, b in zip(u, verts[j])) == 1:
                adj[i].add(j)
                adj[j].add(i)
    return verts, adj


def cliques(adj, top):
    """All cliques with up to top + 1 vertices, from adjacency alone."""
    levels = [[(v,) for v in range(len(adj))]]
    while len(levels) <= top:
        nxt = []
        for c in levels[-1]:
            common = set.intersection(*(adj[v] for v in c))
            nxt.extend(c + (w,) for w in sorted(common) if w > c[-1])
        if not nxt:
            break
        levels.append(nxt)
    return levels


def maximal_cliques(adj):
    out = []

    def bk(r, p, x):
        if not p and not x:
            out.append(frozenset(r))
            return
        for v in list(p):
            bk(r | {v}, p & adj[v], x & adj[v])
            p = p - {v}
            x = x | {v}
    bk(set(), set(range(len(adj))), set())
    return out


def b1_formula(sizes):
    N = prod(sizes)
    return 1 + N * (len(sizes) - 1) - sum(N // n for n in sizes)


def section_x():
    print("X  the complex is a wedge of circles")
    controls = {
        "hexagon": ([(i, (i + 1) % 6) for i in range(6)], [1, 1, 0]),
        "two triangles": ([(0, 1, 2), (3, 4, 5)], [2, 0, 0]),
        "sphere": (list(combinations(range(4), 3)), [1, 0, 1]),
    }
    got = {k: betti(closure(v), top=2) for k, (v, _) in controls.items()}
    check("X0 control complexes", all(got[k] == v for k, (_, v)
                                       in controls.items()), str(got))
    cases = [(2, 3), (2, 5), (3, 5), (5, 7), (2, 2), (3, 3), (4,), (2, 4),
             (4, 6), (2, 2, 2), (2, 3, 4), (2, 3, 5), (2, 3, 7), (2, 5, 7),
             (3, 5, 7), (3, 4, 5), (2, 2, 3, 3), (2, 2, 2, 2), (2, 3, 5, 7),
             (2, 2, 3, 5)]
    bad_b, bad_l = [], []
    for sizes in cases:
        verts, adj = hamming(sizes)
        levels = cliques(adj, 4)
        b = betti(levels, top=3)
        want = [1, b1_formula(sizes), 0, 0]
        print(f"     {str(sizes):14s} N={len(verts):4d}  b={b}")
        if b != want:
            bad_b.append(sizes)
        mc = maximal_cliques(adj)
        N = prod(sizes)
        want_sizes = sorted(n for n in sizes for _ in range(N // n))
        meets = max((len(c1 & c2) for c1, c2 in combinations(mc, 2)),
                    default=0)
        lines = all(sum(len({verts[v][i] for v in c}) > 1
                        for i in range(len(sizes))) == 1 for c in mc)
        if (sorted(len(c) for c in mc) != want_sizes or meets > 1
                or not lines):
            bad_l.append(sizes)
    check("X1 b1 = 1 + N(m - 1 - sum 1/n), b0 = 1, b2 = b3 = 0",
          not bad_b, f"{len(cases)} tuples, failures {bad_b}")
    check("X2 maximal cliques are the lines, meeting in <= 1 vertex",
          not bad_l, f"failures {bad_l}")
    hits = []
    for m, top in ((1, 60), (2, 60), (3, 60), (4, 30), (5, 12)):
        for sizes in combinations_with_replacement(range(2, top + 1), m):
            if b1_formula(sizes) == prod(sizes):
                hits.append(sizes)
    check("X3 b1 = N in the search only at sizes {2, 3, 5}",
          hits == [(2, 3, 5)],
          f"hits {hits}")


def section_i():
    print("I  the integer -chi = N(g - 1)")
    bad = 0
    sets = [S for r in range(1, 10) for S in combinations(PRIMES[:9], r)]
    for S in sets:
        c = neg_chi(S)
        if c % 2 == 0 or any(c % p == 0 for p in S):
            bad += 1
    check("I1 -chi odd and prime to every member", bad == 0,
          f"{len(sets)} sets, {bad} exceptions")
    bad = 0
    sets = [S for r in range(1, 6) for S in combinations(PRIMES[:5], r)]
    for S in sets:
        total = sum(sum(x % p != 0 for p in S) - 1 for x in range(prod(S)))
        bad += total != neg_chi(S)
    check("I2 -chi = sum over Z/N of (d(0, x) - 1)", bad == 0,
          f"{len(sets)} sets, {bad} exceptions")


# ---- the weight law ---------------------------------------------------

def weight(p, s):
    return (1 - pow(p, -1, s)) % s


def first_rung_walk(s, kmax=60):
    """Least k with 1 a subset sum of the weights of p_1..p_k, p != s."""
    reach = {0}
    for k, p in enumerate(PRIMES[:kmax], start=1):
        if p != s:
            w = weight(p, s)
            reach |= {(a + w) % s for a in reach}
        if 1 in reach:
            return k
    return None


def cauchy_davenport_rung(s):
    count = 0
    for k, p in enumerate(PRIMES, start=1):
        if p != s and p % s != 1:
            count += 1
            if count == s - 1:
                return k


def section_w():
    print("W  the weight law")
    pool = PRIMES[:9]
    small = [s for s in PRIMES if s <= 200]
    pairs = viol = ctrl = 0
    for r in range(1, 10):
        for S in combinations(pool, r):
            c = neg_chi(S)
            for s in small:
                if s in S:
                    continue
                pairs += 1
                named = c % s == 0
                viol += named != (sum(weight(p, s) for p in S) % s == 1)
                ctrl += named != (sum(pow(p, -1, s) for p in S) % s == 1)
    check("W0 control: weight 1/p in place of 1 - 1/p fails", ctrl > 0,
          f"{ctrl} violations")
    check("W1 s names S iff the weights sum to 1 mod s", viol == 0,
          f"{pairs} pairs, {viol} violations")
    pool3 = [p for p in PRIMES[:12] if p != 3]
    sets3 = [S for r in range(1, len(pool3) + 1)
             for S in combinations(pool3, r)]
    bad = sum((neg_chi(S) % 3 == 0)
              != (sum(p % 3 == 2 for p in S) % 3 == 2) for S in sets3)
    check("W2 3 names S iff #{p = 2 mod 3} = 2 mod 3", bad == 0,
          f"{len(sets3)} sets, {bad} violations")
    chis = {}
    for r in range(1, 13):
        for S in combinations(range(12), r):
            chis[S] = neg_chi([PRIMES[i] for i in S])
    first, agree, cd_ok, meet = {}, True, True, []
    for s in small:
        direct = min((max(S) + 1 for S, c in chis.items()
                      if c % s == 0 and s not in [PRIMES[i] for i in S]),
                     default=None)
        walk = first_rung_walk(s)
        first[s] = walk
        if direct != (walk if walk is not None and walk <= 12 else None):
            agree = False
        if walk is None and s != 2:
            agree = False
        if s > 2 and (walk is None or walk > cauchy_davenport_rung(s)):
            cd_ok = False
        if s > 2 and walk == cauchy_davenport_rung(s):
            meet.append(s)
    latest = max((k, s) for s, k in first.items() if k is not None)
    check("W3 first naming rung: -chi scan = subset-sum walk", agree,
          f"latest odd s < 200: {latest[1]} at rung {latest[0]}")
    c = neg_chi((17, 19))
    check("W3 2 names no set; 41 first names one at rung 8, {17, 19}",
          first[2] is None and first[41] == 8 and c == 287 == 7 * 41,
          f"41 -> {first[41]}, -chi(17, 19) = {c}")
    check("W3 every odd prime < 200 names a set by rung 11",
          all(first[s] <= 11 for s in small if s > 2),
          f"rungs {sorted(set(first[s] for s in small if s > 2))}")
    check("W3 at or below the Cauchy-Davenport rung, meeting it only at "
          "s = 3", cd_ok and meet == [3], f"meets at {meet}")


def section_b():
    print("B  the baseline")
    ok, cells = True, 0
    for s in (3, 5, 7, 11, 13):
        for size in (6, 9):
            cells += 1
            P = [p for p in PRIMES if p != s][:size]
            w = [weight(p, s) for p in P]
            count = sum(sum(w[i] for i in S) % s == 1
                        for r in range(size + 1)
                        for S in combinations(range(size), r))
            base = 2 ** size / s
            bound = (s - 1) / s * 2 ** size * max(
                prod(abs(cos(pi * j * x / s)) for x in w)
                for j in range(1, s))
            ok &= abs(count - base) <= bound + 1e-9
            print(f"     s={s:2d} |P|={size}  count {count:4d}  "
                  f"2^|P|/s {base:7.2f}  bound {bound:7.2f}")
    check("B1 |count - 2^|P|/s| within the character bound", ok,
          f"{cells} cells")
    P = [p for p in PRIMES if p < 50 and p % 3 == 1]
    zero = sum(neg_chi(S) % 3 == 0 for r in range(1, len(P) + 1)
               for S in combinations(P, r))
    check("B2 an all-invisible pool names nothing", zero == 0,
          f"s = 3 over {P}")


# ---- the slices -------------------------------------------------------

def complex_edges(sizes):
    verts, adj = hamming(sizes)
    levels = cliques(adj, 2)
    return verts, levels[1], levels[2]


def cycle_basis(edges, nverts, eindex):
    """Fundamental cycles of a graph, as bitmasks over eindex."""
    nbr = [[] for _ in range(nverts)]
    for (u, v) in edges:
        nbr[u].append(v)
        nbr[v].append(u)
    to_root, seen, tree = {}, set(), set()
    for root in range(nverts):
        if root in seen or not nbr[root]:
            continue
        seen.add(root)
        to_root[root] = 0
        stack = [root]
        while stack:
            u = stack.pop()
            for v in nbr[u]:
                if v not in seen:
                    seen.add(v)
                    e = (min(u, v), max(u, v))
                    tree.add(e)
                    to_root[v] = to_root[u] ^ (1 << eindex[e])
                    stack.append(v)
    return [(1 << eindex[e]) ^ to_root[e[0]] ^ to_root[e[1]]
            for e in edges if e not in tree]


def section_s():
    print("S  the slices inject jointly")
    verts, edges, tris = complex_edges((2, 5))
    eindex = {e: i for i, e in enumerate(edges)}
    line = [e for e in edges if verts[e[0]][0] == verts[e[1]][0] == 0]
    z = cycle_basis(line, len(verts), eindex)
    bd = boundary_rows(tris, edges)
    image = rank(bd + z) - rank(bd)
    check("S0 control: one line's cycles map to rank 0",
          image == 0 and len(z) == 6, f"{len(z)} cycles, image {image}")
    base = (2, 3, 5, 7)
    ok, npairs, nonzero = True, 0, 0
    for r in range(2, 5):
        for S in combinations(base, r):
            verts, edges, tris = complex_edges(S)
            eindex = {e: i for i, e in enumerate(edges)}
            bd = boundary_rows(tris, edges)
            rb = rank(bd)
            for t in range(1, r):
                for T in combinations(S, t):
                    keep = [i for i, p in enumerate(S) if p not in T]
                    inside = [e for e in edges if all(
                        verts[e[0]][i] == verts[e[1]][i] for i in keep)]
                    z = cycle_basis(inside, len(verts), eindex)
                    image = rank(bd + z) - rb
                    want = prod(S) // prod(T) * b1_formula(T)
                    ok &= image == want
                    npairs += 1
                    nonzero += want > 0
    check("S1 slice cycles have rank c * b1(T) in H1(X(S))", ok,
          f"{npairs} pairs, {nonzero} with nonzero rank")


# ---- automorphisms ----------------------------------------------------

def automorphisms(sizes):
    verts, adj = hamming(sizes)
    edges = [(u, v) for u in range(len(verts)) for v in adj[u] if u < v]
    return sum(all(g[v] in adj[g[u]] for u, v in edges)
               for g in permutations(range(len(verts))))


def order_s_elements(p, s):
    ident = tuple(range(p))
    out = []
    for g in permutations(range(p)):
        h = ident
        for _ in range(s):
            h = tuple(g[i] for i in h)
        if h == ident:
            out.append(sum(g[i] == i for i in range(p)))
    return out


def free_elements(S, s):
    """Elements of order s in prod Sym(p) fixing no vertex."""
    fixes = [order_s_elements(p, s) for p in S]
    total = free = 0
    for combo in product(*fixes):
        if all(f == p for f, p in zip(combo, S)):
            continue
        total += 1
        free += any(f == 0 for f in combo)
    return total, free


def section_a():
    print("A  no free symmetry")
    a = automorphisms((2, 2))
    check("A0 control: |Aut| at (2, 2) = 8, factors swap", a == 8, f"{a}")
    a = automorphisms((2, 3))
    check("A1 |Aut| at (2, 3) = 2! 3!", a == 12, f"{a}")
    total, free = free_elements((2, 5, 7), 5)
    check("A3 control: s = 5 inside S = {2, 5, 7} has free elements",
          free > 0, f"{free} of {total}")
    ok = True
    for S, s in (((2, 5, 7), 3), ((3, 5, 7), 2), ((2, 3, 7), 5)):
        total, free = free_elements(S, s)
        print(f"     S={S} s={s}: {total} elements of order s, {free} free")
        ok &= total > 0 and free == 0
    check("A2 every element of order s outside S fixes a vertex", ok)


def main():
    section_x()
    section_i()
    section_w()
    section_b()
    section_s()
    section_a()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
