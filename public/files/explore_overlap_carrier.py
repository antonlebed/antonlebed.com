"""
explore_overlap_carrier.py -- the shared-channel-count carrier: does
deepest-overlap retrieval carry a class exactly, or does losing the
nested-ball structure lose the readout theorem?

THE QUESTION. explore_similarity_carrier.py split the embedding wall
along Ostrowski: agreement depth (ultrametric, balls = tower-ideal
cosets) hosts taxonomy-shaped classes at EXACT readout -- the ball-read:
a class constant on depth-d balls reads off any deepest-agreement
exemplar, no margin, no tie-break -- while similarity CHAINS (a near b,
b near c, a far from c) provably exceed that carrier (strong triangle,
exhaustive at Z/30). It left one residue OPEN: the ring holds another
native similarity grading, the unordered SHARED-CHANNEL COUNT
ov(x, y) = #{channels i : x == y mod p_i}, which is NOT ultrametric and
trivially REPRESENTS chains as subset overlap. The open question is
READOUT: does deepest-overlap retrieval carry a class EXACTLY -- an
overlap analogue of the ball-read -- or does losing the nested-ball
structure lose the theorem? Overlap neighbourhoods are not nested, and
two exemplars of equal deepest overlap can disagree; find a
tie-break-free exact read, or exhibit the configuration that forbids
one.

THE KEY OBJECTS.
  1. THE OVERLAP GRADING. ov(x, y) = the number of channels on which x
     and y agree (computed from CRT residues; on the probe's world ring
     the count runs over the WORKING channels, the pinned channels being
     shared by construction). Not ultrametric: the inclusion of
     agreement SETS -- the intersection of S(x,y) and S(y,z) sits
     inside S(x,z) -- gives only ov(x,z) >= ov(x,y) + ov(y,z) - k.
     Chains are representable: three subsets A, B, C with
     |A meet B| >= t, |B meet C| >= t, |A meet C| < t.
  2. THE THRESHOLD GRAPH. G_t on a world W: edge x ~ y iff
     ov(x, y) >= t. The neighbourhood N_t(x) = {y : ov(x,y) >= t}.
     Neighbourhoods at fixed t are NOT nested (two can intersect with
     neither containing the other) -- the structure the ball-read's
     proof consumed is genuinely absent.
  3. THE COMPONENT CRITERION (the dichotomy, one line each way).
     Deepest-overlap readout is exact and tie-break-free for every
     query q and every admissible pool (one containing at least one
     >=t neighbour of q) IFF the label is constant on the connected
     components of G_t.
       (<=) An exemplar achieving ov >= t is itself a G_t-neighbour of
       q, hence in q's component; constancy gives the true label, and
       every tied exemplar sits in the same component -- ties
       immaterial, exactly as in the ball-read.
       (=>) A label non-constant on a component is non-constant across
       some EDGE (walk the path); query one endpoint with the other as
       the whole pool: admissible, deepest, wrong. The minimal
       forbidding configuration is a threshold edge with distinct
       labels -- and a CHAIN a ~ b ~ c with label(a) != label(c) forces
       precisely that: the query b holds two >=t exemplars of
       disagreeing labels (equal-overlap when the chain is symmetric,
       an exact tie of disagreeing labels).
  4. THE READABLE HULL. G_{t+1} <= G_t, so component partitions REFINE
     as t rises: the components nest across thresholds even though the
     neighbourhoods do not nest at any fixed threshold. The nested
     family is a dendrogram, i.e. an ultrametric:
         u(x, y) = max { t : x, y in one component of G_t }
                 = max over paths x -> y of the minimum edge overlap
     (single linkage), and u is the pointwise-LEAST ultrametric
     similarity dominating ov: any ultrametric v >= ov satisfies, along
     a path realizing u, v(x,y) >= min v(edges) >= min ov(edges) =
     u(x,y). By the component criterion, the exactly-readable classes
     at threshold t are the classes constant on u-balls at t. So EXACT
     READOUT READS THE HULL, NOT THE GRADING: what deepest-overlap
     retrieval sees of ov is exactly its ultrametric hull u, and the
     chain gap -- pairs with ov(x,y) < t <= u(x,y) -- is invisible to
     it. The readable part of the non-ultrametric carrier is itself an
     ultrametric; chains live exactly in the part exact readout cannot
     see.
  5. FULL-RING TRIVIALITY. On the WHOLE ring Z/(p_1...p_k), G_t is
     connected for every t <= k-1: changing one channel's residue moves
     to a neighbour at ov = k-1 >= t, and any two elements differ in at
     most k channels, so a single-channel walk connects them. At t = k,
     ov = k means equality: singleton components. So on the full ring
     the count carrier's exactly-readable classes are TRIVIAL (constant
     labels below k, everything at k); readable structure exists only
     relative to a curated world whose threshold graph disconnects.
     Agreement depth needs no curation: its balls are ring cosets, and
     coset-constant classes read exactly on the whole ring.

THE RINGS AND THE WORLD. Tiny world: Z/30 = primorial_ring(3), channels
(2, 3, 5). Probe world ring: primorial_ring(10), channels
(2,3,5,7,11,13,17,19,23,29); channels 0..3 are PINNED to residue 1 for
every lexeme (excluded from the count), the six WORKING channels are
indices 4..9 (moduli 11,13,17,19,23,29), so the eight lexemes can carry
pairwise-distinct off-subset residues (values 2..9, all below the
smallest working modulus, all nonzero hence units). A lexeme is a
subset A of the six working channel slots w0..w5; its element phi(L)
takes residue 1 on the subset's channels and residue (index+2) off
them, so the realized agreement set of two lexemes is EXACTLY the
subset intersection, and every phi is a unit.

The world at threshold t = 3, seen lexemes five:
    component I  : A1 = {w0,w1,w2,w3}, A2 = {w1,w2,w3,w4},
                   A3 = {w2,w3,w4,w5}
                   -- ov(A1,A2) = 3, ov(A2,A3) = 3, ov(A1,A3) = 2:
                   a CHAIN inside the component.
    component II : B1 = {w0,w1,w4,w5}, B2 = {w0,w4,w5}
                   -- ov(B1,B2) = 3; every cross overlap <= 2.
Held-out: QA = {w1,w2,w3} (ties A1, A2 at overlap 3, both component I);
QB = {w0,w4,w5} (ties B1, B2 at 3, both component II).
Classes, coarse (component-constant): ALPHA on component I, BETA on
component II. Paradigm: form(L, cell) = phi(L) * K(class(L), cell),
K units chosen as primes above the largest channel (ALPHA: 31, 37, 41;
BETA: 43, 47, 53; citation K = 1). Completion of a held-out lexeme from
its placement phi(q) and citation form, by transform extraction from a
deepest-overlap exemplar, every tied exemplar required to yield the
true form -- the machinery of the filed ball-read probe, retrieval
swapped from deepest agreement to deepest overlap.
Classes, fine (chain-separating): label A1 and A3 differently. The
forbidding configuration: query QF = {w1,w2,w3,w4} (A2's subset) with
pool {A1, A3, B1, B2} -- ov(QF,A1) = 3 = ov(QF,A3), an exact tie of
disagreeing labels, two extractions, two different predictions.

THE HAND-DERIVATION (frozen pre-engine; index convention re-derived
from crt.py: encode(n, ring) = n mod each channel modulus in
TOWER_PRIMES order, channels indexed 0-based in that order; decode =
CRT reconstruction). Tiny world in Z/30, residue vectors written
(mod 2, mod 3, mod 5): a = (0,0,0) -> 0; b = (0,0,1) -> 6 (6 mod 2 = 0,
mod 3 = 0, mod 5 = 1); c = (0,1,1) -> 16 (16 mod 2 = 0, mod 3 = 1,
mod 5 = 1). ov(a,b): agree mod 2 and mod 3, differ mod 5 -> 2.
ov(b,c): agree mod 2 and mod 5, differ mod 3 -> 2. ov(a,c): agree
mod 2 only -> 1. So (2, 2, 1) is a chain at t = 2 -- the exact shape
agreement depth refuses under ANY assignment (filed: 27000 triples,
zero realizations). Hull: u(a,c) = min(2, 2) = 2 > ov(a,c) = 1 -- the
hull merges the chain's endpoints, which is the readout's blindness
made explicit. Criterion at this world, t = 2: G_2 is the path
a - b - c, one component; a labeling with label(a) != label(c) has the
edge-walk break at some edge; query b with pool {a, c} is an exact tie
(2 = 2) of disagreeing labels. The probe world's completion algebra:
pred = K(class(L*), cell) * phi(q); true = K(class(q), cell) * phi(q);
exact iff class(L*) = class(q), which the component criterion delivers
for coarse classes and denies for fine.

PREDICTIONS (fixed before the run; adjudicated post-run in the RUN
RECORD).
  PR1 (representation; rule). The chain (ov >= 2, ov >= 2, ov < 2) is
      realized at Z/30 by (0, 6, 16) with counts (2, 2, 1), and the
      probe world realizes a chain at t = 3 inside a readable
      component (A1, A2, A3 at 3, 3, 2) -- the count carrier
      represents chains where agreement depth provably cannot.
  PR2 (the component criterion; criterion, proof + exhaustive). Over
      ALL labelings of the five-lexeme world with up to three labels
      (3^5 = 243) and ALL admissible pools for every query, exact
      tie-break-free deepest-overlap readout holds IFF the labeling is
      constant on G_3's components -- zero exceptions in either
      direction; same exhaustive verdict at the tiny world (27
      labelings, t = 2).
  PR3 (the readable hull; rule + verified). u computed from components
      across thresholds equals u computed as max-min path overlap, on
      the probe world and on 20 seeded random 6-element worlds in
      Z/30; u satisfies the strong triangle everywhere; component
      partitions nest across thresholds while fixed-t neighbourhoods
      exhibit a non-nested pair (N_3(A1) and N_3(A3) intersect,
      neither containing the other); and the readable labelings at
      every threshold are exactly the u-ball-constant ones.
  PR4 (completion; rule via the criterion + verified). Coarse classes:
      both held-out lexemes complete every non-citation cell exactly
      (6/6 at 1.000) with every deepest-overlap tie yielding the true
      form (ties present at both queries by design); seen-lexeme
      completion 15/15. Fine classes: the QF configuration prints an
      exact tie of disagreeing labels whose two extractions disagree
      on the predicted form -- the tie-break-free exact read does not
      exist, as the criterion's (=>) direction demands.
  PR5 (full-ring triviality; rule, proof + exhaustive). On all of
      Z/30, G_1 and G_2 are connected (single components of size 30)
      and G_3 is 30 singletons -- so below t = k the full ring's
      readable classes are the constants; the single-channel-walk
      proof gives the same for every k at every t <= k-1.

THE KILL-SHAPE (printed observables). The criterion dies if the
exhaustive sweep prints a component-constant labeling with a wrong or
tie-variant readout (the <= direction fails: no exact read after all),
or a non-component-constant labeling that reads exactly on every
admissible pool (the => direction fails: a finer exact read exists and
the hull is NOT the readable part). The hull claim dies if the two
computations of u disagree on any pair, or u violates the strong
triangle. The completion claim dies if a coarse-class held-out cell
prints below 1.000 or any tie is variant. The triviality claim dies if
BFS finds G_1 or G_2 disconnected on Z/30.

POSITIVE CONTROLS (run before any verdict is read). (a) CRT roundtrip
decode(encode(n)) == n on samples of both rings. (b) The tiny-world
hand numbers: the engine reproduces phi = (0, 6, 16), overlaps
(2, 2, 1), u(a,c) = 2. (c) Unit check: every phi and every K
invertible. (d) Seen-lexeme completion at 15/15 (the rig is live; the
fine-class failure is then a finding, not a broken engine).

FINDINGS (tiers inline; run record below; sections keyed to the
predictions).

1. CHAINS RIDE THE COUNT CARRIER (rule). The chain the ultrametric
   provably refuses (filed: zero realizations in 27000 Z/30 triples)
   is realized by the count at the first opportunity: (0, 6, 16) in
   Z/30 with overlaps (2, 2, 1), and the probe world carries the chain
   A1 - A2 - A3 (3, 3, 2) INSIDE a readable component -- representation
   is cheap here (PR1).

2. THE COMPONENT CRITERION (criterion -- necessary and sufficient,
   proved, one line each way; exhaustively confirmed). Deepest-overlap
   readout is exact and tie-break-free for every query and every
   admissible pool IFF the label is constant on the components of the
   threshold graph G_t. Exhaustive: 243/243 labelings at the
   five-lexeme world, 27/27 at the tiny world, zero exceptions either
   direction (PR2). The positive half is the overlap ball-read: any
   exemplar at ov >= t is a neighbour, hence in-component, and every
   tied exemplar likewise -- ties immaterial for the ball-read's own
   reason. The negative half: label non-constancy on a component
   breaks across an edge, and that edge is the forbidding
   configuration.

3. EXACT READOUT READS THE HULL, NOT THE GRADING (rule, proved +
   verified). Components nest across thresholds (a dendrogram) even
   though fixed-t neighbourhoods do not (N_3(A1) = {A1, A2} and
   N_3(A3) = {A2, A3} intersect, neither containing the other), so
   u(x, y) = max-t-same-component = max-min path overlap (single
   linkage; the two computations agree on the probe world and 20
   seeded random Z/30 worlds) is an ultrametric -- the pointwise-LEAST
   ultrametric dominating ov -- and the exactly-readable labelings at
   every threshold are exactly the u-ball-constant ones (verified at
   all seven thresholds x 243 labelings). THE READABLE HULL: what
   deepest-overlap retrieval can read of a non-ultrametric grading is
   precisely its ultrametric hull; the chain gap ov < t <= u is
   invisible to exact readout by theorem (PR3).

4. THE READ THAT EXISTS AND THE ONE THAT CANNOT (rule via the
   criterion + verified). Coarse (component-constant) classes: both
   held-out lexemes complete every cell exactly, 6/6, with 2-wide
   deepest-overlap ties at both queries all yielding the true form --
   the overlap analogue of the ball-read completion, live (PR4;
   seen-lexeme control 15/15). Fine (chain-separating) classes: the
   forbidding configuration prints -- query QF ties A1 (ALPHA) and A3
   (BETA) at overlap 3 exactly, their two extractions predict
   1074902041 vs 3995390533 -- no tie-break-free read exists, as the
   criterion's necessity direction demands; and u(A1, A3) = 3 > 2 =
   ov(A1, A3) names why: the hull merges what the fine labels split.

5. THE FULL RING READS NOTHING (rule, proof + exhaustive). On all of
   Z/30, G_1 and G_2 are single 30-element components and G_3 is 30
   singletons; the single-channel walk gives the same at every k --
   G_t connected for all t <= k-1, singletons at t = k. So on the FULL
   ring the count carrier's readable classes are the constants: its
   readable structure exists only relative to a curated world whose
   threshold graph disconnects. Agreement depth needs no curation --
   its balls are ring cosets, readable on the whole ring (PR5).

THE VERDICT. Both halves of the open question land at once, because
they are the same theorem. YES, deepest-overlap retrieval carries a
class exactly -- the overlap ball-read is real, tie-break-free, and
completion-grade -- but ONLY for classes constant on threshold
components; and the configuration forbidding anything finer is
exhibited and forced: any chain-separating label puts an exact tie of
disagreeing labels behind some query. The two are one statement, the
component criterion, and its structural content is the READABLE HULL:
the exactly-readable part of ANY similarity grading is its least
dominating ultrametric, so losing the nested balls does not lose the
theorem -- the theorem retreats to the nested structure that survives
inside every grading (components nest even when neighbourhoods do
not), and that structure is again an ultrametric. The count carrier
REPRESENTS chains and cannot exactly READ them apart -- chains live
exactly in the grading-hull gap, invisible to exact readout by
theorem, not by this carrier's poverty. So the filed split sharpens:
trees are native to agreement depth; chains ride the count; but
EXACT READOUT is ultrametric-shaped no matter the carrier, and the
non-ultrametric residue needs the deleted metric not for
representation but for any reading finer than the hull. And the two
kept carriers differ in one more way the probe measured: agreement
depth reads coset classes on the whole ring, while the count reads
nothing on the full ring at any threshold below k -- its classes are
properties of a curated world, not of the ring.

RUN RECORD. Single run, all 22 checks green on the first execution of
the full engine; two post-run hygiene edits (a docstring escape
sequence that tripped a SyntaxWarning, and a dead assignment removed
from the enumeration loop), rerun identical at 22/22. Final prints:
controls (a)-(d) PASS with seen-lexeme completion 15/15; PR1 chains
(2,2,1) at Z/30 and (3,3,2) in-world; PR2 243/243 and 27/27 labelings,
zero criterion violations; PR3 hull two-ways equal on probe + 20
random worlds, strong triangle everywhere, dendrogram nesting PASS,
the non-nested neighbourhood pair printed, hull-readability
equivalence at all thresholds; PR4 coarse 6/6 with tie widths [2, 2]
all-true, fine configuration printed (tie at 3, predictions
1074902041 vs 3995390533); PR5 component size profiles [30], [30],
[1]*30. All five predictions fired as frozen; the kill-shape did not.
Runtime ~1 s, memory trivial.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import random
from itertools import product, combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import primorial_ring, encode, decode, is_unit, mod_inverse

R3 = primorial_ring(3)      # Z/30, channels (2, 3, 5)
R10 = primorial_ring(10)    # channels (2,...,29)

WORKING = tuple(range(4, 10))       # working channel indices in R10
N_WORK = len(WORKING)               # 6
PINNED = tuple(range(0, 4))         # pinned to residue 1

CHECKS = []


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond)))
    status = "PASS" if cond else "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f" -- {detail}"
    print(line)


# ----------------------------------------------------------------------
# The grading
# ----------------------------------------------------------------------

def ov_full(x, y, ring):
    """Shared-channel count over ALL channels of the ring."""
    rx, ry = encode(x, ring), encode(y, ring)
    return sum(1 for a, b in zip(rx, ry) if a == b)


def ov_work(x, y):
    """Shared-channel count over the WORKING channels of R10."""
    rx, ry = encode(x, R10), encode(y, R10)
    return sum(1 for i in WORKING if rx[i] == ry[i])


# ----------------------------------------------------------------------
# The probe world: lexemes as working-channel subsets
# ----------------------------------------------------------------------

SUBSETS = {
    # seen
    "A1": {0, 1, 2, 3}, "A2": {1, 2, 3, 4}, "A3": {2, 3, 4, 5},
    "B1": {0, 1, 4, 5}, "B2": {0, 4, 5},
    # held-out
    "QA": {1, 2, 3}, "QB": {0, 4, 5},
    # the forbidding-configuration query (A2's subset, fresh identity)
    "QF": {1, 2, 3, 4},
}
SEEN = ("A1", "A2", "A3", "B1", "B2")
T = 3

COARSE = {"A1": "ALPHA", "A2": "ALPHA", "A3": "ALPHA",
          "B1": "BETA", "B2": "BETA",
          "QA": "ALPHA", "QB": "BETA"}

CELLS = ("cite", "X", "Y", "Z")
K = {("ALPHA", "cite"): 1, ("ALPHA", "X"): 31, ("ALPHA", "Y"): 37,
     ("ALPHA", "Z"): 41,
     ("BETA", "cite"): 1, ("BETA", "X"): 43, ("BETA", "Y"): 47,
     ("BETA", "Z"): 53}


def build_phi():
    """Each lexeme: residue 1 on its subset's working channels, residue
    (index+2) elsewhere on working channels, residue 1 on pinned
    channels -- realized agreement sets are exactly subset
    intersections, and every phi is a unit."""
    phi = {}
    for idx, (name, sub) in enumerate(SUBSETS.items()):
        residues = []
        for ch in range(R10.k):
            if ch in PINNED:
                residues.append(1)
            else:
                w = ch - 4
                residues.append(1 if w in sub else (idx + 2))
        phi[name] = decode(tuple(residues), R10)
    return phi


PHI = build_phi()


def form(name, cell, classes=COARSE):
    return (PHI[name] * K[(classes[name], cell)]) % R10.N


def deepest(qname, pool):
    """All pool members at maximal overlap with q, plus the max."""
    scored = [(ov_work(PHI[qname], PHI[p]), p) for p in pool]
    best = max(s for s, _ in scored)
    return best, [p for s, p in scored if s == best]


def complete(qname, cell, exemplar, classes=COARSE):
    """pred = form(L*, cell) * form(L*, cite)^-1 * form(q, cite)."""
    f_cell = form(exemplar, cell, classes)
    f_cite = form(exemplar, "cite", classes)
    inv = mod_inverse(f_cite, R10.N)
    return (f_cell * inv * (PHI[qname] * K[(classes[qname], "cite")])) % R10.N


# ----------------------------------------------------------------------
# Graph machinery (worlds are dicts name -> element; overlap fn passed)
# ----------------------------------------------------------------------

def components(names, ovfn, t):
    """Connected components of G_t as a frozenset of frozensets."""
    names = list(names)
    seen_set, comps = set(), []
    for start in names:
        if start in seen_set:
            continue
        stack, comp = [start], set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            for y in names:
                if y not in comp and ovfn(x, y) >= t:
                    stack.append(y)
        seen_set |= comp
        comps.append(frozenset(comp))
    return comps


def hull_by_components(names, ovfn, kmax):
    """u(x,y) = max t such that x,y share a component of G_t."""
    names = list(names)
    u = {}
    for t in range(0, kmax + 1):
        for comp in components(names, ovfn, t):
            for x in comp:
                for y in comp:
                    u[(x, y)] = t
    return u


def hull_by_paths(names, ovfn):
    """u(x,y) = max over paths of min edge overlap (Floyd max-min);
    the diagonal comes out as ov(x,x), the full channel count."""
    names = list(names)
    u = {(x, y): ovfn(x, y) for x in names for y in names}
    for z in names:
        for x in names:
            for y in names:
                via = min(u[(x, z)], u[(z, y)])
                if via > u[(x, y)]:
                    u[(x, y)] = via
    return u


def is_component_constant(labeling, comps):
    return all(len({labeling[x] for x in comp}) == 1 for comp in comps)


def exact_readout_everywhere(names, ovfn, labeling, t):
    """For every query and every admissible pool: does every deepest
    exemplar carry the query's label?"""
    names = list(names)
    for q in names:
        others = [x for x in names if x != q]
        for r in range(1, len(others) + 1):
            for pool in combinations(others, r):
                scored = [(ovfn(q, p), p) for p in pool]
                best = max(s for s, _ in scored)
                if best < t:
                    continue  # inadmissible pool
                tied = [p for s, p in scored if s == best]
                if any(labeling[p] != labeling[q] for p in tied):
                    return False
    return True


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    print("=" * 70)
    print("THE SHARED-CHANNEL-COUNT CARRIER -- exact overlap readout?")
    print("=" * 70)

    # ------------------------------------------------------------------
    print("\n-- POSITIVE CONTROLS --")
    ok = all(decode(encode(n, R3), R3) == n for n in range(30))
    ok10 = all(decode(encode(n, R10), R10) == n
               for n in (0, 1, 12345, 510510, R10.N - 1))
    check("control (a): CRT roundtrip both rings", ok and ok10)

    a, b, c = 0, 6, 16
    ovs = (ov_full(a, b, R3), ov_full(b, c, R3), ov_full(a, c, R3))
    check("control (b): tiny-world hand numbers", ovs == (2, 2, 1),
          f"phi = (0, 6, 16), overlaps {ovs}")
    tiny = {"a": a, "b": b, "c": c}
    tiny_ov = lambda x, y: ov_full(tiny[x], tiny[y], R3)
    u_tiny = hull_by_paths(tiny.keys(), tiny_ov)
    check("control (b'): hull merges the chain endpoints",
          u_tiny[("a", "c")] == 2, f"u(a,c) = {u_tiny[('a','c')]} > ov = 1")

    units_ok = (all(is_unit(PHI[n], R10) for n in SUBSETS)
                and all(is_unit(v, R10) for v in K.values()))
    check("control (c): every phi and every K a unit", units_ok)

    # realized overlaps match the designed subset intersections
    design_ok = True
    for x, y in combinations(SUBSETS, 2):
        want = len(SUBSETS[x] & SUBSETS[y])
        got = ov_work(PHI[x], PHI[y])
        if want != got:
            design_ok = False
    check("world realization: overlap == subset intersection, all pairs",
          design_ok)

    seen_hits = 0
    for q in SEEN:
        pool = [x for x in SEEN if x != q]
        best, tied = deepest(q, pool)
        for cell in CELLS[1:]:
            true = form(q, cell)
            if best >= T and all(complete(q, cell, e) == true
                                 for e in tied):
                seen_hits += 1
    check("control (d): seen-lexeme completion 15/15",
          seen_hits == 15, f"{seen_hits}/15")

    # ------------------------------------------------------------------
    print("\n-- PR1: CHAINS ARE REPRESENTABLE --")
    check("PR1: Z/30 chain (2,2,1) at t=2",
          ovs[0] >= 2 and ovs[1] >= 2 and ovs[2] < 2)
    w_ov = lambda x, y: ov_work(PHI[x], PHI[y])
    chain_probe = (w_ov("A1", "A2"), w_ov("A2", "A3"), w_ov("A1", "A3"))
    check("PR1: probe-world chain A1-A2-A3 at t=3",
          chain_probe == (3, 3, 2), f"overlaps {chain_probe}")

    # ------------------------------------------------------------------
    print("\n-- PR2: THE COMPONENT CRITERION (exhaustive) --")
    comps_probe = components(SEEN, w_ov, T)
    comp_repr = sorted(sorted(c) for c in comps_probe)
    check("G_3 components are {A1,A2,A3} | {B1,B2}",
          comp_repr == [["A1", "A2", "A3"], ["B1", "B2"]],
          f"{comp_repr}")

    agree = 0
    counterexample = None
    for labels in product(range(3), repeat=len(SEEN)):
        lab = dict(zip(SEEN, labels))
        cc = is_component_constant(lab, comps_probe)
        ex = exact_readout_everywhere(SEEN, w_ov, lab, T)
        if cc == ex:
            agree += 1
        elif counterexample is None:
            counterexample = (lab, cc, ex)
    check("PR2: exact readout <=> component-constant, 243/243 labelings",
          agree == 243, f"{agree}/243, first violation: {counterexample}")

    agree_t = 0
    for labels in product(range(3), repeat=3):
        lab = dict(zip(tiny.keys(), labels))
        cc = is_component_constant(lab, components(tiny.keys(), tiny_ov, 2))
        ex = exact_readout_everywhere(tiny.keys(), tiny_ov, lab, 2)
        if cc == ex:
            agree_t += 1
    check("PR2: same at the tiny world, 27/27 labelings", agree_t == 27)

    # ------------------------------------------------------------------
    print("\n-- PR3: THE READABLE HULL --")
    names5 = list(SEEN)
    u1 = hull_by_components(names5, w_ov, N_WORK)
    u2 = hull_by_paths(names5, w_ov)
    check("hull two ways agrees on the probe world",
          all(u1[(x, y)] == u2[(x, y)] for x in names5 for y in names5))

    rng = random.Random(631)
    rand_ok, strong_ok = True, True
    for trial in range(20):
        elems = rng.sample(range(30), 6)
        wnames = [f"e{i}" for i in range(6)]
        wmap = dict(zip(wnames, elems))
        wov = lambda x, y: ov_full(wmap[x], wmap[y], R3)
        ua = hull_by_components(wnames, wov, 3)
        ub = hull_by_paths(wnames, wov)
        if any(ua[(x, y)] != ub[(x, y)] for x in wnames for y in wnames):
            rand_ok = False
        for x in wnames:
            for y in wnames:
                for z in wnames:
                    if ub[(x, z)] < min(ub[(x, y)], ub[(y, z)]):
                        strong_ok = False
    check("hull two ways agrees on 20 seeded random Z/30 worlds", rand_ok)
    check("hull satisfies the strong triangle everywhere", strong_ok)

    nested_ok = True
    prev = None
    for t in range(0, N_WORK + 1):
        cs = components(names5, w_ov, t)
        if prev is not None:
            for comp in cs:
                if not any(comp <= p for p in prev):
                    nested_ok = False
        prev = cs
    check("component partitions nest across thresholds (dendrogram)",
          nested_ok)

    n_a1 = {x for x in names5 if w_ov("A1", x) >= T}
    n_a3 = {x for x in names5 if w_ov("A3", x) >= T}
    non_nested = (n_a1 & n_a3) and not (n_a1 <= n_a3) and not (n_a3 <= n_a1)
    check("fixed-t neighbourhoods do NOT nest: N_3(A1) vs N_3(A3)",
          bool(non_nested), f"N_3(A1) = {sorted(n_a1)}, "
          f"N_3(A3) = {sorted(n_a3)}")

    hull_read_ok = True
    for t in range(0, N_WORK + 1):
        comps_t = components(names5, w_ov, t)
        for labels in product(range(3), repeat=len(SEEN)):
            lab = dict(zip(SEEN, labels))
            cc = is_component_constant(lab, comps_t)
            ub_const = all(lab[x] == lab[y] for x in names5 for y in names5
                           if u1[(x, y)] >= t)
            if cc != ub_const:
                hull_read_ok = False
    check("readable labelings == u-ball-constant labelings, every t",
          hull_read_ok)

    # ------------------------------------------------------------------
    print("\n-- PR4: COMPLETION -- the read that exists, the one that "
          "cannot --")
    held_hits, tie_widths = 0, []
    for q in ("QA", "QB"):
        best, tied = deepest(q, SEEN)
        tie_widths.append(len(tied))
        for cell in CELLS[1:]:
            true = form(q, cell)
            if best >= T and all(complete(q, cell, e) == true
                                 for e in tied):
                held_hits += 1
    check("coarse classes: held-out completion 6/6, every tie true",
          held_hits == 6, f"{held_hits}/6, tie widths {tie_widths} "
          "(ties present, immaterial)")

    fine = dict(COARSE)
    fine.update({"A1": "ALPHA", "A3": "BETA", "QF": "ALPHA"})
    pool_f = ["A1", "A3", "B1", "B2"]
    best_f, tied_f = deepest("QF", pool_f)
    preds = {e: complete("QF", "X", e, fine) for e in tied_f}
    labels_f = {e: fine[e] for e in tied_f}
    disagree = (best_f >= T and len(set(labels_f.values())) > 1
                and len(set(preds.values())) > 1)
    check("fine classes: THE FORBIDDING CONFIGURATION", disagree,
          f"query QF, tie at overlap {best_f}: "
          + ", ".join(f"{e} (label {labels_f[e]}, pred {preds[e]})"
                      for e in sorted(tied_f)))
    print(f"    u(A1, A3) = {u1[('A1','A3')]} >= t = {T} > "
          f"ov(A1, A3) = {w_ov('A1','A3')}: the hull merges what the "
          "fine labels split -- the chain gap is exactly what exact "
          "readout cannot see.")

    # ------------------------------------------------------------------
    print("\n-- PR5: FULL-RING TRIVIALITY --")
    full = {str(n): n for n in range(30)}
    fov = lambda x, y: ov_full(full[x], full[y], R3)
    sizes = {t: sorted(len(c) for c in components(full.keys(), fov, t))
             for t in (1, 2, 3)}
    check("Z/30 whole ring: G_1 connected", sizes[1] == [30])
    check("Z/30 whole ring: G_2 connected", sizes[2] == [30])
    check("Z/30 whole ring: G_3 = 30 singletons", sizes[3] == [1] * 30)

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print(f"CHECKS: {n_pass}/{len(CHECKS)} PASS")
    if n_pass != len(CHECKS):
        print("FAILURES:")
        for name, ok in CHECKS:
            if not ok:
                print(f"  - {name}")
        sys.exit(1)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
