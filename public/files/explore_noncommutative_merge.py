"""Does a NON-commutative / two-operation binding algebra natively read the
branching of MERGE — binary-branching hierarchy with matching, general
linguistics' basic composition operation, and here just bracket nesting —
while the flat-role independence survives? The single-commutative-ring
assumption dropped — the wall-dissolution hunt, cast three.

THE QUESTION (the third cast of the wall-dissolution hunt). Casts one and two
converged on a NO-FREE-LUNCH across the tower's two extreme poles: flat-role CRT
independence OR native positional recursion, never both, because "no single
COMMUTATIVE ring holds both — CRT independence REQUIRES coprime non-coupling
channels while a positional magnitude IS the carry-coupling of its digits". That
verdict rests on ONE load-bearing assumption: a SINGLE COMMUTATIVE ring with one
multiplication, where a channel either COUPLES (positional → buys recursion,
loses independence) or does NOT (CRT → keeps independence, loses recursion). Cast
three drops it: give the substrate a SECOND, NON-commutative structural op. Does
branching read natively while the flat-role independence (explore_structure_
dependence.py, the tower reads it NATIVELY) SURVIVES — on ONE integrated algebra?
The trap to avoid: two substrates STAPLED is the priced door in
disguise (explore_dual_merge.py THE PRICED DOOR); the honest read is whether ONE
algebra carries both natively or the cross-op read is the borrow.

THE NEW AXIS IS BRANCHING, NOT MATCHING. Casts one/two already gave the matching
PREDICATE (balance-checking a given digit sequence, the Minsky fold on recovered
digits) natively — distinct from the POP the depth-face ratchet forbade (II.1 A2),
which the invertible non-commutative ops recover here (the honest partial, P4). The
wall a commutative ring hits
on STRUCTURE is BRANCHING: ring x is commutative, so a leaf's left/right path LR
equals RL (the multiset collapse of explore_structure_dependence.py; the branching
kill of explore_recursion_growth.py A3). The one thing a non-commutative op can add
is exactly this: distinguish LR from RL. So cast three tests the BRANCHING readback.

WHOSE VOCABULARY (fixed before any engine code was written). Three suspicions, all
TRANSPLANTS, all flagged and put at risk:
  [T1] "a finite structural op (permutation group / matrix monoid over a fixed
       ring) caps branching depth = a RATCHET" is transplanted from the depth-face
       ratchet (explore_recursion_growth.py II.1) and the precision ratchet
       (explore_dual_merge.py). MARKED; the wrap point is MEASURED (distinct-path
       count vs |image|), not inferred from the analogy.
  [T2] "a non-commutative MIXING op couples the channels = the carry analog" is
       transplanted from cast two's carry-coupling (explore_dual_merge.py TEST 2).
       MARKED and put at RISK: the DISSOLUTION fires if some non-commutative bind
       decodes per role. Measured (per-role decode mismatch count), not assumed.
  [T3] "unbounded native branching requires GROWING the resource = the borrow" is
       transplanted from cast one's escape ("an INFINITE modulus = the full deleted
       place", explore_merge_dissolution.py). MARKED; the growth (matrix entry
       magnitude vs depth) is MEASURED, not asserted.

THE SUBSTRATE (one integrated algebra, three binding ops — a TRICHOTOMY). Roles
and fillers live in k channels (the tower windows). A leaf's structural position
is its L/R path; encode a path by an op OTHER than commutative x:
  - Op C  (commutative ring x, the CONTROL / the tower): path w -> product of
      position-atoms p_{w_i}. Commutative, so LR = RL: the branch structure
      COLLAPSES (explore_structure_dependence.py verbatim).
  - Op P  (permutation rho, non-commutative but independence-PRESERVING): path w
      -> rho_{w_1} o rho_{w_2} o ... in the symmetric group S_k, with rho_L, rho_R
      NON-commuting permutations. Distinguishes LR != RL. rho is an automorphism of
      the direct product that PERMUTES the factors, so it preserves per-channel
      independence (a consistent relabel, not a mix). BUT S_k is FINITE (order <=
      k!): distinct paths WRAP by pigeonhole = bounded (a structural-position
      ratchet [T1]).
  - Op M  (matrix, non-commutative MIXING): path w -> product of position-matrices
      M_{w_i}. The free SL_2(Z) generators M_L = [[1,1],[0,1]], M_R = [[1,0],[1,1]]
      distinguish ALL paths UNBOUNDEDLY (a free monoid) — but the ENTRIES GROW
      (Fibonacci) = magnitude re-imported [T3], and the matrix product MIXES
      coordinates so per-role decode FAILS [T2]. Over a FIXED ring Z/N the matrix
      monoid is FINITE -> it wraps too.
Matching/pop: the non-commutative ops are INVERTIBLE (rho^-1 is native; the free
generators have det 1, so integer inverses) -> a native POP. Dropping commutativity
RECOVERS the pop the depth ratchet forbade (no DEC) — an honest partial win, but
the target is the TRIPLE {branching-unbounded, fixed-resource, independence}, not
the pop alone.

THE PROBE. Two tests, both on the one integrated substrate; the verdict is how
each op fails a DIFFERENT leg of the impossible triple.

  TEST 1  THE BRANCHING READBACK (does a non-commutative op distinguish branch
      structure, and how far?). Encode every L/R path up to depth n under each op
      C / P / M. Observables: the LR vs RL witness (does the op separate them?);
      the number of distinct paths sharing one image (collisions) at each op —
      Op C collapses (LR=RL, anagram paths merge), Op P wraps at |S_k| (a ratchet),
      Op M over Z is injective at all depths (free) but its max entry GROWS with
      depth (magnitude re-import), Op M over Z/N wraps (finite monoid).

  TEST 2  THE FLAT-ROLE INDEPENDENCE CONTROL (does the structural op DECOMPOSE per
      role?). The property (explore_dual_merge.py TEST 2-algebra): the native binding
      must distribute per channel. Cast each op's structural action as a linear map S
      on the k content channels and test the distributes-over-product HOMOMORPHISM
      S(a (.) b) == S(a) (.) S(b) [ (.) = per-channel product ] — the exact statement
      of "the structure does not disturb the per-channel factorization". ONE variable
      differs — each op is cast as its OWN TEST-1 operator:
        - TOWER / Op C (positive control, MUST pass): bind by crt_mul / crt_add; read
          per window. PREDICT 0 mismatches (the CRT iso — the detector fires TRUE on a
          genuinely independent substrate).
        - Op P: S is the PERMUTATION matrix of rho_L (a channel bijection, one nonzero
          per row — the factor-permuting structural action). PREDICT 0 mismatches — a
          one-nonzero-per-row map commutes with the per-channel product (independence
          PRESERVED, the dissolution candidate for the independence leg). NOT vacuous:
          it holds BECAUSE S is a bijection, and fails for the mixing generator below.
        - Op M: S is the LITERAL branching generator M_L (the same op TEST 1 used) —
          its mixing row [1,1] combines two channels. PREDICT > 0 mismatches in that
          row — the cross terms make (sum_j S_rj a_j)(sum_l S_rl b_l) != sum_j S_rj a_j
          b_j; mixing couples the coordinates (the carry analog [T2], general to any
          mixing, not just carry). So the SAME operator that buys unbounded branching
          (Op M / Z, TEST 1) is the one that couples the roles.

PREDICTIONS (frozen before the run).
  P1 (TEST 1, branching): Op C collapses (LR == RL; > 0 census collisions at every
     depth — the tower's structure wall reproduced). Op P separates LR != RL but
     WRAPS (injective only while distinct-path count <= |S_k|; > 0 collisions past
     it — the ratchet [T1]). Op M / Z injective at ALL depths (free monoid) with
     max entry GROWING in depth [T3]; Op M / (Z/N) wraps (finite).
  P2 (TEST 2, independence): the native binding decomposes per role for Op C
     (0 mismatches, CRT iso — positive control) and for Op P (0 mismatches, rho
     relabels channels — independence PRESERVED); for Op M it does NOT (> 0
     mismatches — matrix mixing, the carry analog [T2]).
  P3 (the impossible triple, the no-free-lunch): NO op achieves {branching
     UNBOUNDED, resource FIXED, independence KEPT} at once. The independence-
     keeping ops (C, P) are BOUNDED (collapse or wrap); the unbounded op (M/Z)
     loses independence AND grows magnitude; the fixed-resource M (M / (Z/N))
     wraps. Dropping commutativity trades the COLLAPSE for a WRAP or for
     COUPLING+GROWTH — the no-free-lunch is RESOURCE-forced, DEEPER than
     commutativity-forced. §IV.3 generalizes: "single commutative ring" ->
     "any fixed-resource binding algebra".
  P4 (the honest partial): the non-commutative ops RECOVER native matching/pop
     (invertibility) — a real partial dissolution — but not the triple.

POSITIVE CONTROLS (run and asserted before any verdict is read).
  - rho_L, rho_R are genuine bijections of the k channels (permutations), and they
    do NOT commute (so Op P can separate LR from RL at all — the branching detector
    is not dead);
  - the free generators M_L, M_R round-trip: path -> matrix -> path via the inverse
    generators (injective over Z), so TEST 1's Op-M injectivity is a real read;
  - the TOWER CRT-independence detector fires TRUE (crt_mul and crt_add decompose
    per window) — so a FALSE on Op M is meaningful;
  - Op C genuinely COLLAPSES LR == RL (the collapse detector fires on a collapsing
    substrate — TEST 1's Op-C result is a wall, not a harness miss).

KILL (observable). DISSOLUTION fires iff SOME integrated op, on ONE FIXED-resource
substrate, reads branching UNBOUNDEDLY (injective as paths grow, no wrap, entries
and channels NOT growing) AND decodes per role (0 mismatches) — then one algebra
reads Merge branching natively AND keeps flat-role independence: the deletion was
NOT forced (outcome a, the wanted result). Its ABSENCE — C collapses, P wraps
while keeping independence, M is unbounded only by coupling AND growing magnitude —
is the FORCED-DEEPER no-free-lunch (outcome b): the §IV.3 verdict generalizes from
"single commutative ring" to "any fixed-resource binding algebra". Both first-class.

FINDINGS (all four predictions met; no dissolution kill fired; every number below
is printed output; exhaustive at the stated toy scope; observation tier). Census =
30 L/R paths to depth 4; k = 3 channels; C / M(Z/N) small moduli.

  POSITIVE CONTROLS PASS. rho_L, rho_R are genuine permutations and do NOT commute
  (so Op P can separate branches at all); the free generators M_L, M_R round-trip
  path<->matrix over Z (Op M's injectivity is a real read, not a loss); the tower
  CRT-independence detector fires TRUE (0/150, native *,+ decompose per window — so
  a FALSE on Op M is meaningful); Op C genuinely collapses LR == RL (its TEST 1
  result is a wall, not a harness miss).

  P1 CONFIRMED — TEST 1, THE BRANCHING READBACK (collapse / wrap / grow). The LR vs
  RL witness separates the ops cleanly: Op C gives 15 == 15 (COLLAPSE — commutative,
  branch lost), while Op P gives (2,1,0) != (0,2,1) and Op M gives [[2,1],[1,1]] !=
  [[1,1],[1,2]] (both SEPARATE the branch). Over the 30-path census: Op C leaves 7
  distinct images (23 paths lost — anagram collapse); Op P leaves 6 distinct images
  (24 lost) = exactly |S_3| — a WRAP at the group order (the structural-position
  ratchet [T1]); Op M / Z is INJECTIVE (30/30 distinct) — but its max matrix entry
  GROWS 1, 2, 3, 5, 8, 13 with depth (Fibonacci — the magnitude re-import [T3], the
  unboundedness IS the growth a fixed ring cannot hold); Op M over the FIXED ring
  Z/2 SATURATES at 6 distinct images by depth 3 and wraps forever after — and
  6 = |SL_2(F_2)| = |S_3|, the SAME bound Op P hits (SL_2(F_2) is S_3), the finite
  monoid's ratchet [T1]. So branching is distinguished by both non-commutative ops
  but stays BOUNDED on any fixed resource; unbounded branching (Op M / Z) is bought
  only by growing the entry magnitude.

  P2 CONFIRMED — TEST 2, FLAT-ROLE INDEPENDENCE (does the structural op distribute
  over the per-role binding, S(a.b) == S(a).S(b)?). Each op is cast as its OWN TEST-1
  operator. Op C / the tower: 0/150 per-role reads wrong (the CRT iso — roles
  independent, the positive control). Op P: 0/27 wrong — the PERMUTATION matrix of
  rho_L (one nonzero per row) distributes over the per-channel product, so independence
  is PRESERVED (the dissolution candidate for the independence leg holds it — and
  non-vacuously: it holds BECAUSE S is a bijection). Op M: 9/18 wrong — S = the LITERAL
  branching generator M_L, whose mixing row [1,1] couples its two channels (that row
  fails, its identity row [0,1] preserves), so the cross terms of the same operator
  that buys unbounded branching (TEST 1) break the per-role read (the carry analog
  [T2], confirmed on a structural op that is NOT positional-magnitude — the coupling is
  intrinsic to MIXING, wider than cast two's carry).

  P3 CONFIRMED — THE IMPOSSIBLE TRIPLE (the resource-forced no-free-lunch). No op
  holds {branching UNBOUNDED, resource FIXED, independence KEPT} at once:
    Op C  : independence KEPT, branching COLLAPSED  (commutative).
    Op P  : independence KEPT, branching BOUNDED    (wraps at |S_k|).
    Op M/Z: branching UNBOUNDED, independence LOST  AND magnitude GROWS.
    Op M/(Z/N): fixed resource -> branching WRAPS    (finite monoid), still no
                independence.
  The independence-keeping ops are bounded; the unbounded op loses independence and
  grows magnitude. Dropping commutativity trades the COLLAPSE for a WRAP or for
  COUPLING+GROWTH — it does NOT buy the triple.

  P4 CONFIRMED (structurally) — THE HONEST PARTIAL. The non-commutative ops are
  invertible (rho^-1 native; the free generators have det 1 so integer inverses, in
  MAT_INV, drive the round-trip control) — so they RECOVER a native POP/matching
  that the depth-face ratchet (no DEC) forbade. A real partial dissolution of the
  matching wall — but not of the branching-with-independence triple.

THE VERDICT (observation tier, exhaustive at scope): FORCED-DEEPER CONFIRMED (outcome
b). Dropping the single-COMMUTATIVE-ring assumption does NOT dissolve the no-free-
lunch — it RELOCATES it and shows it was never about commutativity. A binding op that
distinguishes branches at all must be non-commutative (else LR = RL); and on a FIXED
resource ANY op has a FINITE image (a permutation group of order <= k!, a matrix monoid
over a finite ring), so an unbounded family of distinct paths cannot inject — branching
injectivity WRAPS = a bounded ratchet (Op P, Op M/(Z/N)).
Unbounded branching needs an INFINITE image = growing magnitude (Op M/Z's Fibonacci
entries) = the archimedean magnitude the tower deleted, re-imported. And the ops split
on independence exactly as the mixing predicts: the factor-PERMUTING op (Op P) keeps
per-role independence but is the most bounded, while the coordinate-MIXING op (Op M)
buys the unbounded separation only by coupling the roles (the carry analog, now shown
to be MIXING in general, not positional carry specifically). So §IV.3 GENERALIZES:
from "no single COMMUTATIVE-ring substrate holds both" to "no FIXED-RESOURCE binding
algebra holds both" — the deletion is resource-forced. The impossible triple is
{branching-unbounded, fixed-resource, flat-role-independence}: keep independence and
you collapse (commutative) or wrap (permutation); go unbounded and you couple AND grow
the magnitude. The one honest partial: non-commutativity RECOVERS native matching/pop
(invertibility), the wall casts one/two paid for — but never the triple.

THE PRICED DOOR, DEEPENED (recorded, not the destination). Cast two's product door
(Z/p_k# x dual register) stapled two substrates; cast three shows why NO integrated
single algebra escapes either — the growth that a genuine (Op M/Z-style) native
unbounded branching requires IS the base extension. Unbounded native Merge with
flat-role independence requires an UNBOUNDED resource (image size / matrix magnitude /
dimension / precision / channel count), and provisioning it as you recurse is exactly
the borrow made integral (the keystone lemma). The dissolution hunt's first arc is
robustly closed at its deepest named design level; the verdict hands to PROGRAM 2
(learning redesign) and PROGRAM 3 (emergence scale).

HONEST LIMITS. Toy scope (paths/trees to small depth, k = 3 channels, 2x2 matrices,
small moduli). The claim is a NATIVENESS / inductive-bias statement — which structural
readouts are native (fixed-resource ops + invertible generators) vs paid — not a
learned-generalization claim, not a scale claim, no learning rule (codes/readers hand-
designed, as in casts one/two). The TRICHOTOMY is three principled representatives of
the design axis (commutative / factor-permuting / coordinate-mixing), NOT a proof over
all non-commutative binding algebras — "any fixed-resource binding algebra wraps" rests
on the finite-image argument (a finite structure has a finite image, so an injective
map from an unbounded domain cannot exist), exhibited here on S_3 and SL_2(F_2), not
exhausted over all finite algebras. The ratchet/carry-analog readings are transplants
[T1]/[T2]/[T3] from casts one/two, VALIDATED by the measured wrap and mismatch curves,
not assumed. "Forced across three principled corners" remains NOT "globally impossible":
the space is infinite; a genuinely different integrated algebra is a reopen.

RUN RECORD (python prime/code/explore_noncommutative_merge.py, well under a second,
trivial memory, pure Python + crt.py, no external libraries). Census 30 L/R paths to
depth 4; k = 3; C / M(Z/N) moduli N = 30, Nm = 2. Positive controls PASS (rho
non-commuting bijections; free-generator round-trip; tower CRT iso 0/150; Op C collapse
LR==RL). TEST 1: Op C 7 distinct / 23 lost (collapse); Op P 6 distinct / 24 lost (wrap
at |S_3|); Op M/Z 30/30 injective, max entry 1/2/3/5/8/13 by depth (growth); Op M/(Z/2)
saturates at 6 = |SL_2(F_2)| by depth 3 (wrap). TEST 2 (the homomorphism S(a.b) ==
S(a).S(b), each op its own TEST-1 operator): tower 0/150, Op P 0/27 (rho_L's
permutation matrix distributes — indep preserved), Op M 9/18 (S = M_L, its mixing row
[1,1] couples — indep lost on the same op that buys branching). No dissolution kill
fired. All asserts green.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import Ring, encode  # noqa: E402


def banner(s):
    print("\n" + "=" * 68)
    print(s)
    print("=" * 68)


# ------------------------------------------------------------------ #
# binary L/R paths (the branching atoms) and small trees              #
# ------------------------------------------------------------------ #

def all_paths(max_len):
    """All nonempty L/R paths up to length max_len (2 + 4 + ... branches)."""
    out = []

    def rec(s):
        if len(s) >= 1:
            out.append(s)
        if len(s) < max_len:
            rec(s + "L")
            rec(s + "R")

    rec("")
    return out


# ------------------------------------------------------------------ #
# Op C — commutative ring product (the tower / the control)           #
# ------------------------------------------------------------------ #

# position atoms: two coprime units, one per branch direction
ATOM = {"L": 3, "R": 5}


def encode_C(path, N):
    """Commutative product of position-atoms, mod N. LR == RL (order lost)."""
    v = 1
    for ch in path:
        v = (v * ATOM[ch]) % N
    return v


# ------------------------------------------------------------------ #
# Op P — permutation composition (non-commutative, factor-permuting)  #
# ------------------------------------------------------------------ #

def compose(f, g):
    """(f o g)[i] = f[g[i]] — apply g then f."""
    return tuple(f[g[i]] for i in range(len(g)))


def is_bijection(p):
    return sorted(p) == list(range(len(p)))


RHO = {
    "L": (1, 2, 0),   # the 3-cycle 0->1->2->0
    "R": (1, 0, 2),   # the transposition 0<->1, 2 fixed
}


def encode_P(path):
    """Fold rho_{w_1} o rho_{w_2} o ... — path -> permutation of the k channels."""
    k = len(next(iter(RHO.values())))
    perm = tuple(range(k))          # identity
    for ch in path:
        perm = compose(perm, RHO[ch])
    return perm


# ------------------------------------------------------------------ #
# Op M — matrix product (non-commutative, coordinate-mixing)          #
# ------------------------------------------------------------------ #

MAT = {
    "L": ((1, 1), (0, 1)),          # the free SL_2(Z) generators
    "R": ((1, 0), (1, 1)),
}
MAT_INV = {
    "L": ((1, -1), (0, 1)),         # det 1 -> integer inverses (native pop)
    "R": ((1, 0), (-1, 1)),
}


def matmul(A, B, N=None):
    """2x2 product, optionally mod N (a fixed finite ring)."""
    C = tuple(
        tuple(sum(A[i][t] * B[t][j] for t in range(2)) for j in range(2))
        for i in range(2)
    )
    if N is not None:
        C = tuple(tuple(x % N for x in row) for row in C)
    return C


def encode_M(path, N=None):
    """Fold M_{w_1} . M_{w_2} . ... — path -> matrix (over Z, or mod N)."""
    A = ((1, 0), (0, 1))
    for ch in path:
        A = matmul(A, MAT[ch], N)
    return A


def maxabs(A):
    return max(abs(A[i][j]) for i in range(2) for j in range(2))


def main():
    N = 30                          # a small squarefree modulus for Op C / M(Z/N)
    max_len = 4
    paths = all_paths(max_len)
    print("DOES A NON-COMMUTATIVE BINDING ALGEBRA READ BRANCHING MERGE NATIVELY,")
    print("AND DOES THE FLAT-ROLE INDEPENDENCE SURVIVE? (cast three)")
    print(f"census: {len(paths)} L/R paths up to depth {max_len}; "
          f"k=3 channels; C/M(Z/N) modulus N={N}")

    # ---- POSITIVE CONTROLS -------------------------------------------
    banner("POSITIVE CONTROLS")
    assert is_bijection(RHO["L"]) and is_bijection(RHO["R"])
    noncomm = compose(RHO["L"], RHO["R"]) != compose(RHO["R"], RHO["L"])
    assert noncomm
    print("rho_L, rho_R are genuine permutations and do NOT commute .... PASS")

    # free generators round-trip: path -> matrix -> path via inverse gens
    for path in paths:
        A = encode_M(path)
        # strip generators from the right using inverse gens, recover the path
        rec, cur = [], A
        while cur != ((1, 0), (0, 1)):
            # the last generator is recoverable from the sign pattern of a column;
            # simpler: try both, keep the one that keeps entries nonnegative-Fib
            for ch in ("L", "R"):
                trial = matmul(cur, MAT_INV[ch])
                if maxabs(trial) <= maxabs(cur) and all(
                    trial[i][j] >= 0 for i in range(2) for j in range(2)
                ):
                    rec.append(ch)
                    cur = trial
                    break
            else:
                break
        assert "".join(reversed(rec)) == path
    print("free generators M_L, M_R round-trip (path<->matrix over Z) . PASS")

    # tower CRT-independence detector fires TRUE
    tower = Ring("roles", (7, 11, 13), (1, 1, 1))
    tower_mism = 0
    for x in (5, 40, 137, 900, tower.N - 3):
        for y in (6, 51, 208, 700, tower.N - 9):
            zmul, zadd = (x * y) % tower.N, (x + y) % tower.N
            ex, ey, em, ea = (encode(x, tower), encode(y, tower),
                              encode(zmul, tower), encode(zadd, tower))
            for r in range(3):
                if em[r] != (ex[r] * ey[r]) % tower.moduli[r]:
                    tower_mism += 1
                if ea[r] != (ex[r] + ey[r]) % tower.moduli[r]:
                    tower_mism += 1
    assert tower_mism == 0
    print("tower CRT-independence detector fires TRUE ................. PASS  "
          "(native *,+ decompose per window)")

    # Op C genuinely collapses LR == RL
    assert encode_C("LR", N) == encode_C("RL", N)
    print("Op C genuinely collapses LR == RL (a real wall) ........... PASS")

    # ---- TEST 1: THE BRANCHING READBACK ------------------------------
    banner("TEST 1  the branching readback -- collapse / wrap / grow")
    print(f"LR vs RL witness:  C: {encode_C('LR', N)} vs {encode_C('RL', N)}"
          f"  |  P: {encode_P('LR')} vs {encode_P('RL')}"
          f"  |  M/Z: {encode_M('LR')} vs {encode_M('RL')}")

    def collisions(enc):
        seen = {}
        for p in paths:
            seen.setdefault(enc(p), []).append(p)
        return sum(len(g) - 1 for g in seen.values() if len(g) > 1), len(seen)

    cC, dC = collisions(lambda p: encode_C(p, N))
    cP, dP = collisions(encode_P)
    cMz, dMz = collisions(lambda p: encode_M(p))
    print(f"Op C (commutative x, mod {N}): {cC:>3} paths lost, "
          f"{dC} distinct images  -> COLLAPSE (branch structure lost)")
    print(f"Op P (perm S_3, |S_3|=6):      {cP:>3} paths lost, "
          f"{dP} distinct images  -> WRAP at the group order (a ratchet)")
    print(f"Op M (matrix / Z, free):       {cMz:>3} paths lost, "
          f"{dMz} distinct images  -> INJECTIVE (unbounded, entries grow)")
    print("Op M / Z max matrix entry vs depth (the magnitude re-import -- the")
    print("Fibonacci growth is the unboundedness; a FIXED ring cannot hold it):")
    for d in range(1, max_len + 3):
        worst = max(maxabs(encode_M(p)) for p in all_paths(d) if len(p) == d)
        print(f"    depth {d}: max |entry| = {worst}")

    # Op M over a FIXED small ring Z/Nm: the monoid is finite -> it WRAPS. Scan
    # depth until the distinct-image count saturates (genuinely exhibited, not
    # a shallow census that never reached the entry magnitude of the modulus).
    Nm = 2                              # SL_2(Z/2) has order 6
    print(f"Op M / Z/{Nm} (a FIXED ring): distinct images saturate at the finite")
    print(f"    monoid order (the wrap -- the ratchet a fixed resource forces;")
    print(f"    note SL_2(F_2) = S_3, so it wraps at 6 = |S_3|, exactly like Op P):")
    prev = -1
    for d in range(1, 9):
        imgs = {encode_M(p, Nm) for p in all_paths(d)}
        flag = "  <- SATURATED (wrapped)" if len(imgs) == prev else ""
        print(f"    depth <= {d}: {len(imgs)} distinct images{flag}")
        prev = len(imgs)

    # ---- TEST 2: FLAT-ROLE INDEPENDENCE ------------------------------
    banner("TEST 2  flat-role independence -- does the structural op distribute "
           "over per-role binding?")
    # The independence property (explore_dual_merge.py TEST 2-algebra): the native
    # binding must DECOMPOSE per role. Cast each op's OWN structural action (the
    # SAME operator TEST 1 used) as a linear map S on the content channels and test
    # the distributes-over-product HOMOMORPHISM S(a (.) b) == S(a) (.) S(b)
    # [ (.) = per-channel product ] -- the exact statement of "the structure does
    # not disturb the per-channel factorization". Op P's S is a PERMUTATION matrix
    # (its rho as a channel bijection -- one nonzero per row); Op M's S is the LITERAL
    # branching generator M_L (its mixing row [1,1] couples two channels). A
    # permutation PASSES because a one-nonzero-per-row map commutes with the
    # per-channel product; a mixing generator FAILS in its combining row because
    # (sum_j S_rj a_j)(sum_l S_rl b_l) != sum_j S_rj a_j b_j -- so the SAME operator
    # that buys unbounded branching (Op M / Z, TEST 1) is the one that couples the
    # roles. Neither test is vacuous: each COULD fail; the asserts guard the harness.
    def matvec(S, v, dim):
        return tuple(sum(S[r][j] * v[j] for j in range(dim)) % N for r in range(dim))

    def hadamard(u, w, dim):
        return tuple((u[r] * w[r]) % N for r in range(dim))

    def indep_mismatch(S, dim, vecs_a, vecs_b):
        mism, trials = 0, 0
        for a in vecs_a:
            for b in vecs_b:
                lhs = matvec(S, hadamard(a, b, dim), dim)          # S(a (.) b)
                rhs = hadamard(matvec(S, a, dim), matvec(S, b, dim), dim)  # S(a).S(b)
                for r in range(dim):
                    trials += 1
                    if lhs[r] != rhs[r]:
                        mism += 1
        return mism, trials

    sigma = RHO["L"]                                   # the channel bijection (Op P)
    S_perm = tuple(tuple(1 if j == sigma[r] else 0 for j in range(3))
                   for r in range(3))
    S_M = MAT["L"]                                      # the LITERAL Op M generator
    # harness guards: S_perm a genuine bijection (one nonzero/row + columns a perm);
    # S_M genuinely mixes (its row [1,1] combines two channels) -- so each CAN fail.
    assert sorted(sigma) == [0, 1, 2]
    assert all(sum(S_perm[r]) == 1 for r in range(3))
    assert any(sum(1 for x in S_M[r] if x) >= 2 for r in range(2))

    p_mism, p_trials = indep_mismatch(
        S_perm, 3, ((2, 3, 5), (7, 1, 4), (6, 8, 2)),
        ((1, 4, 3), (9, 2, 5), (3, 7, 6)))
    m_mism, m_trials = indep_mismatch(
        S_M, 2, ((2, 3), (5, 1), (4, 6)), ((1, 4), (3, 2), (6, 5)))
    print(f"Op C / TOWER (native *,+):      {tower_mism}/{5 * 5 * 3 * 2} per-role "
          "reads wrong  -> CRT iso, roles independent")
    print(f"Op P (permutation, S=rho_L):    {p_mism}/{p_trials} per-role reads "
          "wrong  -> a bijection distributes over the product, independence PRESERVED")
    print(f"Op M (S = M_L, TEST 1's gen):   {m_mism}/{m_trials} per-role reads "
          "wrong  -> its mixing row [1,1] couples; the same op that buys branching")

    banner("DONE")
    print("TEST 1: Op C collapses (LR=RL), Op P wraps at |S_k| (a ratchet), Op M")
    print("is unbounded only over Z with GROWING entries (mod N it wraps).")
    print("TEST 2: independence survives Op C and Op P (relabel, no mix) but dies")
    print("under Op M (mixing = the carry analog). No fixed-resource op reads")
    print("branching UNBOUNDED and keeps independence -- the no-free-lunch is")
    print("resource-forced. See the module docstring for the verdict.")


if __name__ == "__main__":
    main()
