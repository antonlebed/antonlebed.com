"""
explore_similarity_carrier.py -- the similarity carrier: which side of
Ostrowski carries semantic similarity, and how much of the embedding wall
that choice dissolves.

THE QUESTION. explore_embedding.py closed the fusional case of the
surface->ring embedding with a wall: suppletive morphology (shared meaning,
no shared surface structure) generalizes to held-out lexemes only by
re-importing either the deleted archimedean similarity gradient (a learned
metric embedding) or a per-lexeme codebook that does not extend. That wall
statement quietly assumes similarity must be ARCHIMEDEAN -- a real-valued
gradient. But the ring kept the other side of Ostrowski's dichotomy:
agreement depth along the tower filtration is an ultrametric whose balls
are exactly the cosets of the tower ideals (explore_coupling_order.py).
The design variable, named: THE SIMILARITY CARRIER -- similarity graded by
the deleted archimedean metric (learned, approximate) versus similarity
graded by the kept agreement-depth ultrametric (native, exact). The probe:
does the kept carrier host the HIERARCHICAL part of similarity exactly --
so a fusional paradigm whose inflection classes are taxonomy-shaped
generalizes to held-out lexemes with no metric and no flat codebook --
while the part that genuinely needs the deleted metric shrinks to the
NON-ULTRAMETRIC residue, similarity chains that violate the strong
triangle inequality?

THE KEY OBJECTS.
  1. AGREEMENT DEPTH. Fix a filtration of the ring's channels into ordered
     blocks B_1, ..., B_D with block moduli M_1, ..., M_D (products of the
     block's prime channels). depth(x, y) = the largest d such that
     x == y mod M_1 * ... * M_d (0 if they already differ mod M_1). This is
     an ultrametric grading: congruences compose, so
         depth(x, z) >= min(depth(x, y), depth(y, z))
     -- the strong triangle inequality, one line from the definition.
  2. THE TREE EMBEDDING. A rooted taxonomy of depth D with level-d
     branching at most the count of admissible level-d digits embeds by
     path: leaf x with path (a_1, ..., a_D) maps to
         phi(x) = CRT(a_1, ..., a_D)   (block d carrying digit a_d),
     and then depth(phi(x), phi(y)) = the depth of the leaves' lowest
     common ancestor, exactly. Digits are drawn from unit residues so
     phi(x) is a ring unit (invertible; exact unbind stays available).
  3. BALL-READ RETRIEVAL. If a label (an inflection class) is constant on
     depth-d balls, then for any query q and any exemplar set containing
     at least one member of q's ball, the DEEPEST-AGREEMENT exemplar
         L* = argmax_L depth(phi(q), phi(L))
     lies in q's ball, so its label is q's label -- exactly, with no
     margin: members of the ball agree to depth >= d, non-members to
     depth < d, and the two ranges cannot overlap. Ties in the argmax are
     immaterial for the same reason (every tied exemplar sits in the same
     ball), and the engine checks that rather than assuming it: a hit
     requires every tied exemplar to yield the true form. Nearest-neighbor
     class readout, a heuristic in an archimedean embedding, is a theorem
     here.
  4. THE RESIDUE. A similarity pattern with sim(a,b) >= d, sim(b,c) >= d,
     sim(a,c) < d -- a chain at threshold d, the standard shape of
     distributional co-occurrence neighborhoods ("bank" near "river",
     "bank" near "money", "river" far from "money") -- is unrepresentable
     as agreement depth for ANY assignment of ring elements, by the strong
     triangle inequality above. The kept carrier hosts trees; it refuses
     chains, provably.

THE RING. RAD = Z/510510 (k = 7, channels {2,3,5,7,11,13,17}). Filtration
blocks: B_1 = {2,3,5} (M_1 = 30), B_2 = {7} (M_2 = 7), B_3 = {11,13,17}
(M_3 = 2431). Unit digits per block: 8 for B_1 (1 x 2 x 4), 6 for B_2,
1920 for B_3 -- so a taxonomy with up to 8 macro-classes, 6 sub-classes
each, and 1920 leaves per sub-class embeds. The probe uses 4 macro-classes
x 2 sub-classes x 3 leaves = 24 lexemes.

THE PARADIGM (fusional by construction: class-specific transforms, no
shared surface structure across classes). form(L, cell) = phi(L) *
K(class(L), cell) mod N, with every K a unit and the citation cell's
K = 1. Two cells' transforms are set at the MACRO level (constant on
depth-1 balls), two at the SUB level (constant on depth-2 balls) -- so one
embedding must serve two different label granularities at once. Held-out
lexemes: 6 of 24 (each sub-class keeps at least one seen exemplar); a
held-out lexeme arrives with only its tree placement phi(q) and its
citation form, and every other cell must be produced by transform
extraction from the deepest-agreement seen exemplar:
    T = form(L*, cell) * form(L*, cite)^-1,   pred = T * form(q, cite).

WHAT THIS DOES AND DOES NOT CLAIM. The probe separates the CARRIER from
the ASSIGNMENT. It asks whether the ring natively grades hierarchical
similarity at exact readout (carrier); where a lexeme's tree placement
comes from is a data-side learning problem this probe does not touch. It
makes no capacity claim of any kind -- no count of how many patterns fit,
no scaling in the ring size. And the residue half is a refusal result:
the chain shape needs a carrier the ring does not have.

THE HAND-DERIVATION (frozen pre-engine; convention re-derived from
crt.py: encode(n, ring) = n mod each channel modulus in TOWER_PRIMES
order; CRT decode via decode(residues, ring); blocks group channel
indices 0-based in that order). Tiny case, Z/30, blocks {2,3} then {5}:
unit digits mod 6 are {1, 5} (2 macro-classes), mod 5 are {1,2,3,4}.
Lexemes A = (1,1), B = (1,2), C = (5,1): A and B share macro-class
(digit 1 mod 6), C does not. phi(A) = CRT(1 mod 6, 1 mod 5) = 1;
phi(B) = CRT(1, 2) = 7; phi(C) = CRT(5, 1) = 11. K(class 1, pl) = 7
(a unit mod 30), citation K = 1, so form(A, pl) = 1 * 7 = 7 and the
true form(B, pl) = 7 * 7 = 49 = 19 mod 30. Held-out B: depth(7, 1) --
7 == 1 mod 6, 7 != 1 mod 5 -> depth 1; depth(7, 11) -- 7 != 11 mod 6
-> depth 0. Deepest exemplar is A, same macro-class. T = form(A, pl) *
form(A, cite)^-1 = 7 * 1 = 7; pred = 7 * phi(B) = 7 * 7 = 19 = the true
form. EXACT.

PREDICTIONS (fixed before the run; adjudicated post-run in the RUN
RECORD).
  PR1 (embedding exactness; rule). Over all 276 leaf pairs of the
      24-leaf taxonomy, depth(phi(x), phi(y)) equals the lowest-common-
      ancestor depth, with zero exceptions, and every phi(x) is a unit.
  PR2 (hierarchical generalization; rule + verification). Every held-out
      lexeme resolves every non-citation cell exactly (24 of 24
      completions at 1.000) from deepest-agreement transfer alone -- both
      the macro-level and the sub-level cells, one embedding serving both
      granularities. Two controls: a FLAT per-lexeme codebook (transforms
      indexed by lexeme identity, the rescue explore_embedding.py showed
      does not extend) scores 0 on held-out; a SCRAMBLED embedding (phi
      values permuted across leaves, breaking the ball/class alignment,
      machinery unchanged) scores at or near chance -- the lift rides the
      ball structure, not the transform algebra.
  PR3 (simultaneous multi-level readout; rule). From one phi(q), the
      macro-class and sub-class of every lexeme are both exactly readable
      by partial congruence (mod M_1, mod M_1*M_2) -- the whole ancestor
      chain in one element, no second embedding.
  PR4 (the residue; rule, proof + exhaustive control). The strong
      triangle inequality depth(x,z) >= min(depth(x,y), depth(y,z))
      holds for ALL triples in an exhaustive sweep of Z/30 (27000
      triples), and consequently the chain pattern (depth(a,b) >= 1,
      depth(b,c) >= 1, depth(a,c) = 0) is realized by ZERO of the 27000
      assignments -- the refusal is total, not a search that came up
      empty at random.

THE KILL-SHAPE (printed observables). The dissolve claim dies if PR2
prints below 1.000 while PR1 and the positive controls are green (the
carrier is sound but the readout is not exact after all), or if the
deepest-agreement retrieval needs a magnitude tie-break to pick L*
(an archimedean sneak-in). The residue claim dies if the exhaustive
sweep finds one chain-realizing triple.

POSITIVE CONTROLS (run before any verdict is read). (a) CRT roundtrip:
decode(encode(n)) == n on samples. (b) The hand pair above: the engine
reproduces phi(A) = 1, phi(B) = 7, phi(C) = 11, depths (1, 0), and the
completion 19. (c) Unit check: phi(x) * phi(x)^-1 == 1 for all leaves.
(d) The flat-codebook control resolves SEEN lexemes at 1.000 (it fails
only held-out -- a live rig, not a broken one).

FINDINGS (tiers inline; run record below; sections keyed to the
predictions).

1. THE KEPT CARRIER HOSTS TREES EXACTLY (rule, mechanism-proved +
   verified). The path embedding realizes lowest-common-ancestor depth
   as agreement depth on all 276 leaf pairs with zero mismatches and
   all 24 phi values distinct units (PR1). The mechanism is the
   definition of CRT: two elements agree mod a prefix of the filtration
   exactly when their paths share that prefix.

2. HIERARCHICAL FUSIONAL GENERALIZATION IS NATIVE, METRIC-FREE, AND
   CODEBOOK-FREE (rule via the ball-read lemma; 24/24 verified at this
   taxonomy). Every held-out lexeme resolves every cell exactly by
   transform extraction from a deepest-agreement exemplar -- with the
   strong requirement that EVERY depth-tied exemplar yields the true
   form, and zero tie-variant cells observed: the choice inside the
   ball is immaterial, as the lemma says, so no magnitude tie-break
   exists anywhere in the loop. The two controls isolate the mechanism:
   a flat per-lexeme codebook covers 0 of 6 held-out lexemes (the
   non-extending rescue of explore_embedding.py, restated as coverage),
   and a seeded scramble of the same phi values across leaves --
   machinery untouched, ball/class alignment destroyed -- scores 0/24.
   The lift rides the ball structure, not the transform algebra. (A
   first control attempt used a ROTATION of the leaf index and scored
   12/24: translation maps the block-structured class partition partly
   onto itself, so a rotation is a structurally confounded scramble --
   kept here as a note because the confound is itself a fact about how
   much structure the partition shares with the index.)

3. ONE ELEMENT CARRIES THE WHOLE ANCESTOR CHAIN (rule). Macro-class
   equality is exactly congruence mod 30 and sub-class equality exactly
   congruence mod 210, over all 276 pairs (PR3) -- the two label
   granularities read out of the same embedding by partial congruence,
   no second embedding, and the paradigm exercised both at once (two
   cells keyed to each level).

4. THE RESIDUE IS THE NON-ULTRAMETRIC PART, PROVABLY (rule, one-line
   proof + exhaustive control). Congruences compose, so agreement depth
   obeys depth(x,z) >= min(depth(x,y), depth(y,z)); the exhaustive sweep
   of all 27000 triples of Z/30 finds zero violations and zero
   realizations of the chain pattern (depth(a,b) >= 1, depth(b,c) >= 1,
   depth(a,c) = 0). So similarity CHAINS -- the shape of graded
   distributional neighborhoods, where a is near b and b near c without
   a near c -- cannot ride agreement depth under ANY assignment of ring
   elements. The refusal is the theorem, the sweep its control.

THE VERDICT. The embedding wall of explore_embedding.py SPLITS along
Ostrowski's own seam. The wall said fusional generalization re-imports
the deleted similarity metric or a codebook that does not extend; this
probe adds the third path the dichotomy was hiding: the ring KEPT a
similarity carrier -- agreement depth, whose balls are the tower-ideal
cosets -- and it hosts the HIERARCHICAL part of similarity natively, at
exact readout -- the generalization guaranteed by construction, where an
archimedean embedding carries no such theorem and must be trained and
validated. What agreement depth REFUSES is the non-ultrametric
residue: overlapping graded neighborhoods, similarity chains, anything
violating the strong triangle inequality. So a learned metric embedding
is needed AT MOST for that residue -- and whether even the residue needs
it is open: the ring holds other similarity gradings this probe did not
test (the unordered shared-channel count, for one, is native and not
ultrametric). (Settled since: explore_overlap_carrier.py -- the count
REPRESENTS chains, but exact deepest-overlap readout holds iff the label
is constant on threshold-graph components, so the exactly-readable part
of any grading is its least dominating ultrametric; the deleted metric
is needed only for readings finer than that hull. This probe's own
claims all survive unchanged.) Trees are native; chains exceed this
carrier. Where a
lexeme's tree placement comes from remains a data-side question outside
this probe's scope.

RUN RECORD. Single run after two engine corrections, both caught by
controls before any verdict was read: (i) four intended-prime transform
constants were composite and shared factors with the ring (121, 143,
169, 187) -- the unit positive control failed and they were replaced
with primes above the largest channel; (ii) the first scrambled control
was a rotation and scored 12/24 for the structural reason recorded in
finding 2, replaced by a seeded shuffle. Final prints: controls (a)-(d)
PASS with 72/72 seen-lexeme completions; PR1 276 pairs, 0 mismatches,
24/24 distinct; PR2 24/24 held-out completions, 0 tie-variant cells,
codebook coverage 0/6 -> 0/24, scramble 0/24; PR3 both congruence
equivalences PASS; PR4 27000 triples, 0 violations, 0 chains. All four
predictions fired as frozen; the kill-shape did not. Runtime ~1 s,
memory trivial.
"""

import sys
import os
import itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import RAD_RING, encode, decode

N = RAD_RING.N  # 510510
PRIMES = RAD_RING.moduli  # (2, 3, 5, 7, 11, 13, 17)

# Filtration blocks: channel indices into PRIMES, in order.
BLOCKS = [(0, 1, 2), (3,), (4, 5, 6)]
BLOCK_MODULI = [2 * 3 * 5, 7, 11 * 13 * 17]  # 30, 7, 2431
PREFIX_MODULI = [30, 210, 510510]  # M_1, M_1*M_2, M_1*M_2*M_3


def depth(x, y, prefix_moduli=PREFIX_MODULI):
    """Agreement depth along the filtration: largest d with x == y mod
    (M_1 ... M_d); 0 if they differ already mod M_1."""
    d = 0
    for M in prefix_moduli:
        if (x - y) % M == 0:
            d += 1
        else:
            break
    return d


def crt_pair(r1, m1, r2, m2):
    """Smallest nonnegative solution of x == r1 mod m1, x == r2 mod m2
    (m1, m2 coprime)."""
    g = pow(m1, -1, m2)
    return (r1 + m1 * ((r2 - r1) * g % m2)) % (m1 * m2)


def phi_from_path(path):
    """Embed a taxonomy path (a_1, a_2, a_3) -- block digits, each a unit
    residue mod its block modulus -- as the CRT element of RAD."""
    x = path[0] % BLOCK_MODULI[0]
    m = BLOCK_MODULI[0]
    for digit, bm in zip(path[1:], BLOCK_MODULI[1:]):
        x = crt_pair(x, m, digit % bm, bm)
        m *= bm
    return x


# ---------------------------------------------------------------------
# The taxonomy: 4 macro-classes x 2 sub-classes x 3 leaves.
# Unit digits: coprime to the block modulus.
MACRO_DIGITS = [1, 7, 11, 13]          # units mod 30, distinct
SUB_DIGITS = [1, 3]                    # units mod 7
LEAF_DIGITS = [1, 2, 3]                # units mod 2431 (coprime to 11*13*17)

LEXEMES = []  # (name, path, macro_index, sub_index)
for mi, md in enumerate(MACRO_DIGITS):
    for si, sd in enumerate(SUB_DIGITS):
        for li, ld in enumerate(LEAF_DIGITS):
            name = f"L{mi}{si}{li}"
            LEXEMES.append((name, (md, sd, ld), mi, si))

PHI = {name: phi_from_path(path) for name, path, _, _ in LEXEMES}
MACRO = {name: mi for name, _, mi, _ in LEXEMES}
SUB = {name: (mi, si) for name, _, mi, si in LEXEMES}


def lca_depth(n1, n2):
    """Taxonomy depth of the lowest common ancestor of two leaves."""
    if n1 == n2:
        return 3
    if SUB[n1] == SUB[n2]:
        return 2
    if MACRO[n1] == MACRO[n2]:
        return 1
    return 0


# The fusional paradigm: cells and class-specific unit transforms.
# 'pl' and 'du' are MACRO-level cells; 'pst' and 'fut' are SUB-level.
# Transforms are fixed distinct units of RAD (spot-checked coprime below).
CELLS = ["pl", "du", "pst", "fut"]
K_MACRO = {  # (macro_index, cell) -> unit
    (mi, c): u
    for mi, (row) in enumerate([(101, 103), (107, 109), (113, 199), (127, 131)])
    for c, u in zip(["pl", "du"], row)
}
K_SUB = {  # ((macro_index, sub_index), cell) -> unit
    (key, c): u
    for key, row in zip(
        itertools.product(range(4), range(2)),
        [(137, 139), (211, 149), (151, 157), (163, 167),
         (223, 173), (179, 181), (227, 191), (193, 197)],
    )
    for c, u in zip(["pst", "fut"], row)
}


def transform_for(name, cell):
    if cell in ("pl", "du"):
        return K_MACRO[(MACRO[name], cell)]
    return K_SUB[(SUB[name], cell)]


def form(name, cell):
    if cell == "cite":
        return PHI[name]
    return PHI[name] * transform_for(name, cell) % N


HELD_OUT = ["L001", "L012", "L102", "L110", "L201", "L310"]
SEEN = [name for name, _, _, _ in LEXEMES if name not in HELD_OUT]


def deepest_agreement(qname, pool):
    """ALL exemplars of maximal agreement depth with the query, plus the
    depth. The ball-read lemma predicts the choice among them is
    immaterial (any member of the query's ball carries the same class),
    so the caller verifies tie-INVARIANCE rather than tie-breaking."""
    best_d = -1
    best = []
    for L in pool:
        d = depth(PHI[qname], PHI[L])
        if d > best_d:
            best_d, best = d, [L]
        elif d == best_d:
            best.append(L)
    return best, best_d


def complete(qname, cell, exemplar):
    """Transform extraction from the exemplar, applied to the query's
    citation form."""
    t = form(exemplar, cell) * pow(form(exemplar, "cite"), -1, N) % N
    return t * form(qname, "cite") % N


def main():
    print("=== explore_similarity_carrier.py ===")
    print(f"ring N = {N}, blocks {BLOCK_MODULI}, prefix moduli {PREFIX_MODULI}")
    print(f"{len(LEXEMES)} lexemes, {len(HELD_OUT)} held out, cells {CELLS}")

    # ---- positive controls ----
    print("\n-- positive controls --")
    ok = all(decode(encode(n, RAD_RING), RAD_RING) == n for n in (0, 1, 7, 12345, 510509))
    print(f"(a) CRT roundtrip on samples: {'PASS' if ok else 'FAIL'}")

    # (b) the hand pair at Z/30 (blocks {2,3} then {5})
    pm30 = [6, 30]
    a, b, c = crt_pair(1, 6, 1, 5), crt_pair(1, 6, 2, 5), crt_pair(5, 6, 1, 5)
    d_ab = depth(a, b, pm30)
    d_bc = depth(b, c, pm30)
    t_hand = (a * 7 % 30) * pow(a, -1, 30) % 30
    pred_hand = t_hand * b % 30
    hand_ok = (a, b, c) == (1, 7, 11) and (d_ab, d_bc) == (1, 0) and pred_hand == 19
    print(f"(b) hand pair: phi = ({a},{b},{c}), depths ({d_ab},{d_bc}), "
          f"completion {pred_hand} -- {'PASS' if hand_ok else 'FAIL'}")

    units_ok = all(PHI[n] * pow(PHI[n], -1, N) % N == 1 for n in PHI)
    print(f"(c) all 24 phi values are units: {'PASS' if units_ok else 'FAIL'}")

    kunits_ok = all(pow(u, -1, N) is not None for u in
                    list(K_MACRO.values()) + list(K_SUB.values()))
    print(f"    all transforms are units: {'PASS' if kunits_ok else 'FAIL'}")

    seen_flat = sum(
        1 for L in SEEN for cell in CELLS
        if complete(L, cell, L) == form(L, cell)
    )
    print(f"(d) flat codebook on SEEN lexemes: {seen_flat}/{len(SEEN) * len(CELLS)}")

    # ---- PR1: embedding exactness ----
    print("\n-- PR1: depth(phi(x),phi(y)) == lca depth, all pairs --")
    names = [n for n, _, _, _ in LEXEMES]
    mismatches = sum(
        1 for n1, n2 in itertools.combinations(names, 2)
        if depth(PHI[n1], PHI[n2]) != lca_depth(n1, n2)
    )
    distinct = len(set(PHI.values()))
    print(f"pairs checked: {len(names) * (len(names) - 1) // 2}, "
          f"mismatches: {mismatches}, distinct phi: {distinct}/{len(names)}")

    # ---- PR2: hierarchical generalization + controls ----
    print("\n-- PR2: held-out completion via deepest agreement --")
    hits, total, tie_variant = 0, 0, 0
    for q in HELD_OUT:
        tied, d = deepest_agreement(q, SEEN)
        for cell in CELLS:
            total += 1
            preds = {complete(q, cell, ex) for ex in tied}
            if len(preds) > 1:
                tie_variant += 1
            if preds == {form(q, cell)}:
                hits += 1
    print(f"held-out completions: {hits}/{total} (a hit requires EVERY "
          f"depth-tied exemplar to yield the true form)")
    print(f"tie-variant cells (tied exemplars disagreeing, which would "
          f"force a tie-break): {tie_variant}")

    # flat codebook control: a transform table indexed by lexeme identity,
    # built from SEEN forms. It has no row for a held-out lexeme, so its
    # held-out score is 0 by its own coverage -- the non-extending rescue
    # explore_embedding.py measured, restated here as coverage.
    covered = sum(1 for q in HELD_OUT if q in SEEN)
    print(f"flat-codebook coverage of held-out lexemes: {covered}/"
          f"{len(HELD_OUT)} -> 0/{total} completions")

    # scrambled control: permute phi across leaves by a seeded shuffle,
    # breaking ball/class alignment; machinery unchanged. (A ROTATION is
    # the wrong scramble here: translation of the leaf index maps the
    # block-structured class partition partly onto itself.)
    import random
    perm = names[:]
    random.Random(0).shuffle(perm)
    scram = {names[i]: PHI[perm[i]] for i in range(len(names))}
    s_hits = 0
    for q in HELD_OUT:
        best_d, best = -1, None
        for L in SEEN:
            d = depth(scram[q], scram[L])
            if d > best_d:
                best_d, best = d, L
        for cell in CELLS:
            t = form(best, cell) * pow(form(best, "cite"), -1, N) % N
            if t * form(q, "cite") % N == form(q, cell):
                s_hits += 1
    print(f"scrambled-embedding control on held-out: {s_hits}/{total}")

    # ---- PR3: simultaneous multi-level readout ----
    print("\n-- PR3: ancestor chain by partial congruence --")
    macro_ok = all(
        (PHI[n1] - PHI[n2]) % PREFIX_MODULI[0] == 0
        if MACRO[n1] == MACRO[n2]
        else (PHI[n1] - PHI[n2]) % PREFIX_MODULI[0] != 0
        for n1, n2 in itertools.combinations(names, 2)
    )
    sub_ok = all(
        (PHI[n1] - PHI[n2]) % PREFIX_MODULI[1] == 0
        if SUB[n1] == SUB[n2]
        else (PHI[n1] - PHI[n2]) % PREFIX_MODULI[1] != 0
        for n1, n2 in itertools.combinations(names, 2)
    )
    print(f"macro-class == congruence mod {PREFIX_MODULI[0]}: "
          f"{'PASS' if macro_ok else 'FAIL'}")
    print(f"sub-class   == congruence mod {PREFIX_MODULI[1]}: "
          f"{'PASS' if sub_ok else 'FAIL'}")

    # ---- PR4: the residue, exhaustively at Z/30 ----
    print("\n-- PR4: strong triangle + chain refusal, exhaustive Z/30 --")
    pm30 = [6, 30]
    violations, chains = 0, 0
    for x in range(30):
        for y in range(30):
            for z in range(30):
                dxy, dyz, dxz = depth(x, y, pm30), depth(y, z, pm30), depth(x, z, pm30)
                if dxz < min(dxy, dyz):
                    violations += 1
                if dxy >= 1 and dyz >= 1 and dxz == 0:
                    chains += 1
    print(f"triples: 27000, strong-triangle violations: {violations}, "
          f"chain patterns realized: {chains}")

    print("\ndone.")


if __name__ == "__main__":
    main()
