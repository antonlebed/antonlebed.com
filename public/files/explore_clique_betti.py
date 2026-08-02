"""What the clique complex of a Hamming graph counts.

THE OBJECT.  The CRT neighbour graph on Z/N, N = p_1...p_k, is the Cartesian
product K_{p_1} [] ... [] K_{p_k}: two residues are adjacent iff they differ in
exactly ONE channel.  Its CLIQUE COMPLEX fills in every complete subgraph as a
simplex.  One number about that complex was on record and unexplained: the
first Betti number is (p-1)(q-1) for two channels, exact at every computed
pair, and the formula collapses at three -- {2,3,5} -> 30, {2,3,7} -> 44,
{2,5,7} -> 82, {3,5,7} -> 140, {2,3,5,7} -> 384, no product form fitting.

THE QUESTION.  What does b1 count at k >= 3?  A closed form is the answer only
if it comes with the object it counts; a curve fitted through five points is
not an answer, and the corpus already carries one such coincidence here
(b1(Z/30) = 30 = N).

THE SLATE (frozen before any engine code).

S0 -- THE STRUCTURAL CLAIM, derived on paper before this file existed.
  In a Cartesian product two vertices are adjacent iff they differ in exactly
  one coordinate.  If u,v differ in coordinate i and v,w in coordinate j != i,
  then u,w differ in BOTH and are non-adjacent.  So every clique has all its
  pairwise differences in a single coordinate: it lies in a LINE (all
  coordinates but one held fixed).  Maximal cliques are therefore exactly the
  lines, of which there are L = sum_i N/p_i, and two distinct lines share at
  most one vertex.  The complex is thus a union of simplices glued at isolated
  points.  Adding the lines one at a time, a simplex attached along c
  already-present vertices is up to homotopy a wedge of c-1 circles (c >= 1);
  summing c over all lines counts incidences minus vertices, kN - N.  Hence the
  complex is homotopy equivalent to a wedge of circles with

        b1 = kN - N - L + 1,     L = sum_i N/p_i,

  equivalently b1 = 1 + N*(k - 1 - sum_i 1/p_i), and b_j = 0 for all j >= 2.
  Nothing in the argument uses primality: the p_i are complete-graph sizes.
  At k=2 it collapses to 2pq - pq - p - q + 1 = (p-1)(q-1), the recorded form.

P1 -- THE CLOSED FORM.  PREDICTION: an INDEPENDENT homology computation (ranks
  of the GF(2) boundary maps of the actual clique complex, cliques enumerated
  by common neighbours and never by the line structure S0 asserts) reproduces
  kN - N - L + 1 on every case below, including k=3 triples outside the five
  on record, k=4, k=5, repeated sizes, and non-prime sizes.
  KILL (observable): any case where the computed b1 differs from the form.

P2 -- THE VANISHING ABOVE 1.  PREDICTION: computed b2 = 0 and b3 = 0 on every
  case where the complex has simplices of that dimension at all.  This is the
  half of S0 that a fitted formula could never supply, and it is what makes the
  wedge-of-circles reading the object rather than a coincidence.
  KILL (observable): any case with b2 > 0 or b3 > 0.

P3 -- THE MAXIMAL CLIQUES.  PREDICTION: the enumerated maximal cliques number
  exactly L = sum_i N/p_i, with N/p_i of size p_i for each i, and every pair of
  distinct maximal cliques meets in 0 or 1 vertices.  This is S0's premise
  tested directly rather than assumed, so that P1 passing cannot be a numerical
  accident over a complex shaped some other way.
  KILL (observable): a maximal-clique count other than L, a size multiset other
  than the predicted one, or any two maximal cliques sharing >= 2 vertices.

POSITIVE CONTROL (run before any verdict is read).  The homology engine is run
on three complexes whose Betti numbers are known independently of anything
here: a hollow 6-cycle (b0,b1,b2) = (1,1,0), two disjoint triangles filled in
(2,0,0), and the boundary of a tetrahedron -- a 2-sphere -- (1,0,1).  The
b2 = 1 case matters most: it is the only run in this file that proves the b2
column can report a NON-zero, without which P2 passing would say nothing.

METHOD.  Betti numbers over GF(2) from boundary ranks:
b0 = V - rk(d1), b1 = E - rk(d1) - rk(d2), b2 = T - rk(d2) - rk(d3).  Ranks by
bitmask Gaussian elimination.  GF(2) Betti numbers bound the rational ones from
above and coincide with them absent 2-torsion; a wedge of circles is
torsion-free, so agreement with the predicted values is the check.  Cliques are
found by intersecting neighbour sets, which uses only the adjacency relation.

RESOURCE.  All cases below have < 1000 edges except (2,3,5,7) at 1365 and
(2,2,3,3,5) at 900; the largest boundary matrix holds ~1500 bitmask rows of
~1400 bits.  Well under the 512MB ceiling, seconds of wall clock.

FINDINGS (post-run edit; run record at the end).

F1 -- THE CLOSED FORM HOLDS, and it is a THEOREM rather than a fit.  Computed
  b1 equals kN - N - L + 1 on all 20 cases: the three recorded pairs, all five
  k >= 3 points on record, four fresh triples, a fresh k=4, two k=5 cases with
  repeated sizes, and four non-prime cases including the archived fat pair
  (8,9) -> 56.  The form is not fitted -- S0 derives it, and what the runs test
  is the derivation.  P1 survives.
  ONE STEP S0 LEFT IMPLICIT, completed here rather than by editing S0, which is
  written before the run and left as written.  S0 sums c over all L lines to
  kN - N and then writes b1 = kN - N - L + 1 without saying where the -(L-1)
  comes from, and it fixes no order. Both are one omission: order the lines so
  each after the first meets the union of its predecessors -- connectivity of
  the graph allows it, and it is what puts the c attaching points in ONE
  component, which the wedge step needs. Then the first line contributes c = 0
  and each of the other L - 1 contributes c - 1, so the wedge count is (kN -
  N) - (L - 1). Worth stating alongside it is why the attaching set is
  discrete at all: two vertices of a line span an edge no other line contains,
  so a line meets the union of the others in isolated points and never along a
  simplex. The formula and every prediction are unchanged; what was missing
  was the bookkeeping, and the doc entry carries the completed form.

F2 -- NOTHING ABOVE DIMENSION 1.  b2 = 0 on every case and b3 = 0 on every case
  that has 4-cliques at all (the two exceptions, [2,2,2,2,2] and [3,3,3], have
  no 4-cliques, since a line of size m carries simplices only up to dimension
  m-1).  The complex is a wedge of b1 circles.  P2 survives, and the positive
  control is what gives that its weight: the same engine reports b2 = 1 on the
  2-sphere, so a zero here is a measurement and not a dead column.

F3 -- THE PREMISE IS THE ANSWER.  Maximal cliques, enumerated by Bron-Kerbosch
  with no use of the product structure, number exactly L = sum_i N/p_i, split
  by size as N/p_i cliques of size p_i for each i, and no two share more than
  one vertex -- on all five cases checked, including repeated and non-prime
  sizes.  P3 survives.  So the cliques ARE the lines, which is what turns the
  count into an object rather than a formula.

WHAT b1 COUNTS.  The independent cycles of the vertex-line incidence graph:
nodes are the N residues and the L lines, edges are the kN incidences, and
b1 = kN - (N + L) + 1 is that graph's cycle rank.  The bookkeeping form is
sharper still -- a line of size p_i is a simplex contributing p_i - 1
independent edges, so the lines jointly offer sum_i (N/p_i)(p_i - 1) = kN - L,
while a spanning tree on the residues can absorb only N - 1 of them.  b1 is the
EXCESS: the independent edges the lines supply beyond what the residues can
hold.  The k=2 collapse to (p-1)(q-1) is the same statement on a grid.

WHY THE OLD READING MISSED IT.  The product form (p-1)(q-1) factors at k=2 and
at no higher k, so a search for a product formula was a search in a family that
contains the answer only at the one rung where it was already known.  The true
form is a DIFFERENCE of three terms, and the middle one, L = sum_i N/p_i, is
not symmetric under anything the product family can express.  b1(Z/30) = 30 = N
stays a coincidence: b1 = N asks for k - 1 - sum_i 1/p_i = 1 - 1/N exactly, and
{2,3,5} meets it because 2 - 31/30 = 29/30 = 1 - 1/30.  No other set tested
does.

WHAT IS NOT CLAIMED.  Betti numbers here are computed over GF(2), which bounds
the rational ones from above; agreement with a wedge of circles (torsion-free)
is what makes them the rational values.  The theorem itself is proved over any
coefficients by S0 and does not rest on these runs.

RUN RECORD.  Windows, python 3, single process under memwatch: peak working set
44.6 MB, peak commit 39.5 MB, ceiling 512 MB, wall 0.5s.  All 20 cases and all
three positive controls in one run.

AND THE RESOURCE ESTIMATE ABOVE WAS WRONG, recorded here rather than by editing
a pre-run section.  It names two cases as the exceptions to "< 1000 edges", one
of which -- (2,2,3,3,5) at 900 -- is not an exception at all, and it puts the
largest boundary matrix at ~1500 rows of ~1400 bits.  FIVE cases exceed 1000
edges, and the largest is (5,7,11): 3850 edges and 8470 triangles, so the
biggest matrix is 8470 rows of 3850 bits, over five times the estimate.  The
run was never near the ceiling and the estimate's error changed nothing about
its safety -- what it cost was the estimate's usefulness as a check, since a
number this far off would not have caught a runaway either.
"""

from itertools import combinations
from math import prod


# ── homology over GF(2) ────────────────────────────────────────────────

def gf2_rank(rows):
    """Rank of a GF(2) matrix given as integer bitmasks."""
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


def simplices(adj, nv):
    """All cliques of size 2, 3, 4 as sorted tuples, via neighbour sets."""
    edges = [(a, b) for a in range(nv) for b in adj[a] if b > a]
    tris = []
    for a, b in edges:
        for c in sorted(adj[a] & adj[b]):
            if c > b:
                tris.append((a, b, c))
    tets = []
    for a, b, c in tris:
        for d in sorted(adj[a] & adj[b] & adj[c]):
            if d > c:
                tets.append((a, b, c, d))
    return edges, tris, tets


def boundary(faces, lower_index, dim):
    """Bitmask rows of the boundary map from `faces` (dim-simplices)."""
    rows = []
    for f in faces:
        m = 0
        for skip in range(dim + 1):
            m |= 1 << lower_index[f[:skip] + f[skip + 1:]]
        rows.append(m)
    return rows


def betti(adj, nv):
    """(b0, b1, b2) over GF(2), plus the simplex counts."""
    edges, tris, tets = simplices(adj, nv)
    ei = {e: i for i, e in enumerate(edges)}
    ti = {t: i for i, t in enumerate(tris)}
    r1 = gf2_rank([(1 << a) | (1 << b) for a, b in edges])
    r2 = gf2_rank(boundary(tris, ei, 2))
    r3 = gf2_rank(boundary(tets, ti, 3))
    return (nv - r1, len(edges) - r1 - r2, len(tris) - r2 - r3), \
           (nv, len(edges), len(tris), len(tets))


def betti3(adj, nv):
    """b3 over GF(2): needs the 5-cliques.  Returns None if there are none."""
    edges, tris, tets = simplices(adj, nv)
    fives = []
    for a, b, c, d in tets:
        for e in sorted(adj[a] & adj[b] & adj[c] & adj[d]):
            if e > d:
                fives.append((a, b, c, d, e))
    if not tets:
        return None
    ti = {t: i for i, t in enumerate(tris)}
    qi = {q: i for i, q in enumerate(tets)}
    r3 = gf2_rank(boundary(tets, ti, 3))
    r4 = gf2_rank(boundary(fives, qi, 4))
    return len(tets) - r3 - r4


# ── the Hamming graph ──────────────────────────────────────────────────

def hamming_adj(mods):
    """Adjacency sets of K_{m_1} [] ... [] K_{m_k} on 0..prod(mods)-1."""
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
            if sum(1 for i in range(len(mods))
                   if coords[a][i] != coords[b][i]) == 1:
                adj[a].add(b)
                adj[b].add(a)
    return adj, nv


def maximal_cliques(adj, nv):
    """Bron-Kerbosch with pivoting -- no use of the product structure."""
    out = []

    def bk(r, p, x):
        if not p and not x:
            out.append(tuple(sorted(r)))
            return
        pivot = max(p | x, key=lambda u: len(adj[u] & p))
        for v in sorted(p - adj[pivot]):
            bk(r | {v}, p & adj[v], x & adj[v])
            p = p - {v}
            x = x | {v}

    bk(set(), set(range(nv)), set())
    return out


def predicted(mods):
    nv = prod(mods)
    return len(mods) * nv - nv - sum(nv // m for m in mods) + 1


# ── the runs ───────────────────────────────────────────────────────────

def positive_control():
    print("POSITIVE CONTROL")
    # hollow 6-cycle
    cyc = [set() for _ in range(6)]
    for i in range(6):
        cyc[i].add((i + 1) % 6)
        cyc[(i + 1) % 6].add(i)
    print("  6-cycle           (b0,b1,b2) =", betti(cyc, 6)[0], " expect (1, 1, 0)")
    # two disjoint filled triangles
    two = [set() for _ in range(6)]
    for base in (0, 3):
        for a, b in combinations(range(base, base + 3), 2):
            two[a].add(b)
            two[b].add(a)
    print("  2 triangles       (b0,b1,b2) =", betti(two, 6)[0], " expect (2, 0, 0)")
    # boundary of a tetrahedron = S^2 (drop the 3-cell by hand)
    sph = [set() for _ in range(4)]
    for a, b in combinations(range(4), 2):
        sph[a].add(b)
        sph[b].add(a)
    edges, tris, _ = simplices(sph, 4)
    ei = {e: i for i, e in enumerate(edges)}
    r1 = gf2_rank([(1 << a) | (1 << b) for a, b in edges])
    r2 = gf2_rank(boundary(tris, ei, 2))
    print("  S^2 (no 3-cell)   (b0,b1,b2) =",
          (4 - r1, len(edges) - r1 - r2, len(tris) - r2), " expect (1, 0, 1)")


CASES = [
    # (mods, label) -- the recorded pairs, the five k>=3 points on record,
    # fresh triples, k=4, k=5, repeated and non-prime sizes.
    ([3, 5], "recorded pair"),
    ([3, 7], "recorded pair"),
    ([5, 7], "recorded pair"),
    ([2, 3, 5], "on record"),
    ([2, 3, 7], "on record"),
    ([2, 5, 7], "on record"),
    ([3, 5, 7], "on record"),
    ([2, 3, 5, 7], "on record"),
    ([2, 3, 11], "fresh triple"),
    ([3, 5, 11], "fresh triple"),
    ([5, 7, 11], "fresh triple"),
    ([2, 7, 13], "fresh triple"),
    ([2, 3, 5, 11], "fresh k=4"),
    ([2, 2, 2, 2, 2], "k=5, repeated"),
    ([2, 2, 3, 3, 5], "k=5, repeated"),
    ([3, 3, 3], "repeated"),
    ([4, 6], "non-prime pair"),
    ([4, 5, 6], "non-prime triple"),
    ([2, 9], "non-prime pair"),
    ([8, 9], "archived fat pair"),
]


def main():
    positive_control()

    print("\nP3 -- MAXIMAL CLIQUES ARE THE LINES")
    for mods in ([2, 3, 5], [3, 5, 7], [2, 3, 5, 7], [4, 5, 6], [2, 2, 3, 3, 5]):
        adj, nv = hamming_adj(mods)
        mc = maximal_cliques(adj, nv)
        want_n = sum(nv // m for m in mods)
        sizes = sorted((len(c), sum(1 for d in mc if len(d) == len(c)))
                       for c in {len(c): c for c in mc}.values())
        worst = max((len(set(a) & set(b)) for a, b in combinations(mc, 2)),
                    default=0)
        print(f"  {str(mods):18s} count {len(mc):5d} (L = {want_n:5d})"
              f"  sizes {sizes}  max pairwise overlap {worst}")

    print("\nP1/P2 -- b1 AGAINST kN - N - L + 1, AND THE VANISHING ABOVE 1")
    print(f"  {'mods':18s} {'N':>6s} {'b1':>7s} {'pred':>7s} {'ok':>3s}"
          f" {'b2':>4s} {'b3':>4s}  note")
    for mods, note in CASES:
        adj, nv = hamming_adj(mods)
        (b0, b1, b2), counts = betti(adj, nv)
        b3 = betti3(adj, nv)
        p = predicted(mods)
        assert b0 == 1, (mods, b0)
        print(f"  {str(mods):18s} {nv:6d} {b1:7d} {p:7d} {str(b1 == p):>3s}"
              f" {b2:4d} {str(b3 if b3 is not None else '-'):>4s}  {note}")


if __name__ == "__main__":
    main()
