"""The mixing shape at (3,4): a census the record never took, and a
theorem that says what a mixing collision there must be.

THE QUESTION. A COLLISION is one 0/1 product with two distinct
N-irreducible factorizations -- multisets of ATOMIC 0/1 blocks, a block
being atomic when no bipartition of its Z-irreducible atoms gives two
nonnegative sub-products (explore_menu_reach.py's counter). Two
factorizations are SHARED when, after the blocks they have in common are
set aside as spectators, some block of one divides some block of the
other; they are MIXING when no block of either divides a block of the
other and none is common. The parallel-edge criterion
(explore_face_accident.py) is stated at the shared shape {p.n, q} against
{p, n.q}; the (2,6) census of {2..32} holds four objects at the mixing
shape {p1 n1, p2 n2} against {p1 n2, p2 n1}, one family, {2,16} against
{2,8,32} + m.{1,2,4}. The record's sentence for the (3,4) half -- 71
in-frame collisions at size 3 over {2..32} against size 4 over {2..24}
(explore_descent_hunt.py, explore_seed_confine.py) -- was that every one
of them is shared and that the absence of a mixing case there is not
derived. That sentence was written without a rig. This file takes the
census it describes, and derives what a mixing (3,4) collision can be.

WHOSE VOCABULARY. Shared and mixing are read on ATOMIC factorizations, the
level the criterion and the (2,6) census both use, and not on the menu
pair the sweep walked: a 4-menu that is two 0/1 binomials is not a block
of any atomic factorization, and a pair {A, B} with B = B1 B2 reads at
the atomic level as {A, B1, B2}. The distinction is load-bearing for the
census below (the t = 6 identity with a spectator binomial is a (3,4)
menu pair and a shared atomic pair) and it is marked as a transplant from
the (2,6) file's vocabulary, where it was minted.

THE HAND-ATTACK, on paper before any engine code (the theorem is
restated in the finding once the run has printed). Its two inputs and
one lemma:
  - the trinomial lemma (explore_seed_rank_law.py): a reducible 0/1
    trinomial is collinear, 1 + v^a + v^b along one primitive monomial v;
  - unique factorization in the Laurent ring, units being +-monomials;
  - THE CYCLE LEMMA, one variable: {0,a,b} + {0,s} = {0,i,j} + {0,k} with
    both sums direct and s != k. The s-pairs and the k-pairs are two
    perfect matchings on the six points; their union is a union of even
    cycles, a 2-cycle forcing s = k, so it is one alternating 6-cycle,
    and closing it forces k = 3s (or s = 3k); walking it from the minimum
    leaves one shape, m + s.{0,...,5}. So a 6-term (3,2)-against-(3,2)
    collision with distinct binomials IS the t = 6 identity in v^s:
    1 + v^{2e} + v^{4e} beside 1 + v^e, and 1 + v^e + v^{2e} beside
    1 + v^{3e} -- the second irreducible only at e = 1, so a reducible
    3-block can take EITHER role, and the case split below runs both:
    in the second role the 3-block divides the other side's 6-block
    (Phi3(v^e) + z Phi3(v^{2e}) = Phi3(v^e)(1 + z Phi6(v^e))), which is
    the shared shape, and the 4-block beside it is (1 + v^e)(m1 + m2) or
    (1 + v^{3e})(m1 + m2), not atomic, whenever the two slices agree.
What the attack derives, case by case over the block-value shapes a
12-term product admits ({2,6}, {3,4}, {2,2,3}) once spectators are shown
impossible (a spectator leaves a 6-term residue, whose only collision is
the t = 6 identity and that is shared, or a 4-term one, which factors
uniquely): a mixing pair with a 3-term block on either side has that block
REDUCIBLE, hence collinear along a line v, and then either
  (I) every block is a polynomial in v -- product Newton dimension 1 --
  or
  (II) THE FAMILY, in coordinates with v primitive and z off the line:
        A = 1 + v^{2e} + v^{4e},   B = (1 + v^{3e}) + z (1 + v^e),
        C = 1 + v^{3e},            D = (1 + v^{2e} + v^{4e}) + z (1 + v^e + v^{2e}),
      {A, B} against {C, D}, e >= 1. Every member is in frame at every e
      and every z off the line; B and D are atomic (a proper sub-product
      of the cyclotomics of 1 + v^e or of 1 + v^e + v^{2e} that leaves a
      nonnegative block beside Phi6(v^e) + z would have to be a 0/1
      binomial or trinomial divisible by Phi6(v^e), and the only such are
      1 + v^{3e} and Phi3(v^{2e}) themselves); no block divides a block
      across, Phi2(v^e) and Phi3(v^e) sharing no cyclotomic index.
The (2,6) census's family is (II) at e = 1, v = the monomial of 2,
z = m/2 -- and its (3,4) side {2,8,32} x {2,16,m,2m} lies INSIDE the
(3,4) sweep's box for m in {3,5,6,7,9,10,11,12}. So the hand-attack's
first claim is about the record: the 71 contain mixing objects.

DISTRUST THE MARGIN, not the kill. The kill -- a mixing (3,4) object
outside (I) and (II) -- is derived from the theorem and is what the
one-variable search and the census can print. The MARGIN is the count 8:
it rests on the box's element bound applied to a family read off the
(2,6) side, and a box can hold a family member the (2,6) box did not (m
up to 12 here against 8 there), which is why S1 prints every mixing
object rather than asserting a count. The second margin is (I): the
theorem says one-variable mixing is not excluded, the family itself has
line members (z = v^j, in frame when j is off e.[-5, 7]), and whether
anything ELSE is one-variable and mixing is searched, never derived.

DESIGN, five stages.
 S0 THE POSITIVE CONTROL, read before any census number. (a) The pair
    {2,8,32} x {2,6,12,16} -- the (2,6) census's m = 6 object read from
    its (3,4) side -- must count 2 atomic factorizations and classify
    MIXING, matching the family at e = 1. (b) The graded t = 12 point
    {2,8,32} x {2,4,16,32} must classify SHARED. (c) The cycle lemma
    exhaustively: every direct {0,a,b} + {0,s} with a second (3,2)
    decomposition at a different binomial, exponents to 30, is the t = 6
    identity in v^s.
 S1 THE CENSUS. The (3,4) box rebuilt from explore_descent_hunt.py's own
    build (imported), the same 85,253 pairs re-walked, every in-frame
    collision's atomic factorizations classified pairwise: spectators,
    the block-value shape, SHARED or MIXING, and for each mixing pair
    whether it matches the family template and at what e.
 S2 THE LEMMAS ON THE BOX. Asserted over S1's output: no mixing pair
    carries a spectator; every mixing pair's 3-block is a reducible
    trinomial; every mixing pair is the family or one-variable.
 S3 THE FAMILY OFF THE BOX. Members built directly at e = 1..4 with a
    symbolic off-line z, and in menu clothes at q = 3 and at e = 2 --
    elements to 512 -- each counted (2 atomic factorizations) and
    classified mixing.
 S4 THE ONE-VARIABLE SEARCH. Every direct one-variable (3,4) product
    with exponents to a stated bound (M34_N, default 24) that admits a
    second tiling by a binomial or a trinomial; the atomic factorizations
    of each, classified; every mixing one matched against the family's
    line members. Reported whatever it finds.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): the three controls read as stated.
  PR1 (S1): 71 in-frame collisions, the published count.
  PR2 (S1): the mixing pairs among them are exactly {2,8,32} x
      {2,16,m,2m} for m in {3,5,6,7,9,10,11,12} -- 8 -- every one at
      e = 1; every other pair is shared, and every pair carrying a
      spectator is shared.
  PR3 (S2): the three lemmas hold at every row.
  PR4 (S3): every constructed member counts exactly 2 and reads mixing.
  PR5 (S4): every one-variable mixing object found is a line member of
      the family; the COUNT of one-variable collisions and their shapes
      is NOT PREDICTED, being the measurement.

KILLS (observables; what each MEANS is weighed after the run).
  K0: any S0 control misreads -- the instrument is broken, nothing below
      is read.
  K1: S1 prints a mixing pair that matches neither the family nor
      dimension 1, or a mixing pair with a spectator, or one whose
      3-block is irreducible -- the hand-attack has a hole, and its
      location is the printed row.
  K2: S1 prints 0 mixing pairs -- the record's sentence stood, and the
      hand-attack's reading of the box is what was wrong.
  K3: S4 prints a one-variable mixing object that is not a line member
      of the family -- a new object, and (I) is inhabited beyond the
      family.
  K4: S3 prints a member counting other than 2 or reading shared -- the
      converse half of the theorem is wrong at that e.

HONEST LIMITS, named before the run. (i) The theorem's case (I) is a
residual class, not a classification: one-variable mixing is searched to
an exponent bound and nothing here bounds it. (ii) The census is the
box's; the theorem is what makes the box's reading transferable. (iii)
Atomicity and the counter are explore_menu_reach.py's, imported and
controlled in S0, not re-proved. (iv) The trinomial lemma is cited from
explore_seed_rank_law.py; the Ljunggren-free step in the atomicity of D
uses only that a product of cyclotomics has no non-cyclotomic factor.

RUN RECORD. Wall-clock estimate: the S1 re-walk is the predecessor's
244 s; S4 at N = 24 is ~560,000 masks and a few hundred factorizations,
a minute or two. Under 512 MB throughout by the predecessor's peak.
Runs: stages 0-3 together, 12/12 checks, 240.3 s, peak working set
74.5 MB; stage 4 alone, 2/2 checks, 213.8 s, 70.1 MB. Finding 1's
220.3 s is the first full run's walk, whose 71 rows are identical. The
whole file, after the audit's residual-multiset fix: 14/14 checks,
481.6 s, peak working set 74.7 MB, every figure above unchanged.

FINDINGS (post-run; every figure below is the run's own print).

0. THE CONTROLS PASS (K0 did not fire). The m = 6 object counts 2 atomic
   factorizations, reads MIXING (3,4)v(2,6) with no spectator and matches
   the family at e = 1; the graded t = 12 point reads SHARED, the t = 6
   identity beside a spectator. The cycle lemma holds exhaustively: 11,760
   direct {0,a,b} + {0,s} to exponent 30, 17 with a second (3,2)
   decomposition at a different binomial, all 17 the t = 6 identity.

1. THE RECORD'S SENTENCE WAS FALSE: THE 71 HOLD 16 MIXING OBJECTS, AND
   THEY ARE THE FAMILY (measurement; K2 did not fire). The re-walk of the
   85,253 pairs (220.3 s) finds the published 71 in-frame collisions, each
   with exactly two atomic factorizations, and the pairwise reading is
   55 SHARED, every one the t = 6 identity with one spectator binomial
   ((2,3)v(2,3), spectator = 1), and 16 MIXING, every one (3,4)v(2,6)
   with no spectator, every one the family at e = 1: {2,8,32} against
   c'.{1, 8} + m.{1, 2} with c' in {2, 3} and m/c' not a power of 2 --
   the eight at c' = 2 the slate predicted, and eight more at c' = 3
   ({3,24} + m.{1,2}, m in {2,4,5,7,8,9,10,11}) the slate's count missed.
   The older record had counted them without naming them: the box's 17
   size-4 seeds are these 16 partners and {2,3,16,24}, whose collision is
   shared, so explore_seed_confine.py's "16 where both halves are seeds"
   IS the mixing population -- the two readings agree object for object.
   PR2 as frozen (eight) FAILED on the count; the check now compares
   against the family's members the box admits, computed, and passes at
   16 = 16. The miss is the named margin: a family read off the (2,6)
   side's c = c' = 2 and carried to a box where c' ranges.

2. THE THREE LEMMAS HOLD ON THE BOX (K1 did not fire): no mixing pair
   carries a spectator, every mixing pair's 3-block is the reducible
   trinomial {2,8,32}, every mixing pair matches the family template.

3. THE FAMILY IS MIXING AT EVERY e BUILT, AND OFF THE BOX (construction,
   verified exactly; K4 did not fire): at e = 1, 2, 3, 4 with a symbolic
   off-line z the product has 12 terms, exactly 2 atomic factorizations
   and reads MIXING at its own e; in menu clothes {2,18,162} x
   {2,54,10,30} (q = 3), {2,32,512} x {2,128,3,12} (e = 2) and
   {3,12,48} x {5,40,7,14} (c != c') each count 2 and read MIXING.

4. ONE VARIABLE, TO EXPONENT 24, IS THE FAMILY AGAIN (observation, exact
   in that box; K3 did NOT fire, though the first run's reading of it
   was mistaken -- see the redesign note). 221,832 direct one-variable
   (3,4) products, 19,927 distinct supports with a second tiling, 19,433
   primitive; 201 of those carry >= 2 atomic factorizations; the pairwise
   reading is 79 SHARED (78 the t = 6 identity with a spectator, 1 of
   shape (2,2,3)v(2,2,3)) and 124 MIXING, and EVERY mixing pair carries
   the family's (3,4) side {1 + v^{2e} + v^{4e}, (1 + v^{3e}) +
   v^j (1 + v^e)}, e = 1..6 (32, 20, 24, 16, 24, 8). At 122 the other
   side is {1 + v^{3e}, Phi3(v^e) q} as off the line; at 2 (both e = 2,
   supports {0,1,3,...,11,14} and its reflection) the cofactor
   q = Phi6(v^2) + v splits as (1 + v)(1 - v^2 + v^3), the 6-block
   refines, and the other side reads (2,2,3): {1 + v^3, 1 + v^6,
   1 + v + v^5}. So on the line the family's D can fail to be atomic and
   the pair is still mixing, with three blocks against two. No
   one-variable mixing object outside the family's (3,4) side exists to
   exponent 24; nothing here says so beyond it. Peak 70.1 MB, 213.8 s.

REDESIGN NOTE, kept because the charter asks for it. The first S4 ran
the sympy-expression counter over all 19,927 supports and was killed at
twice its estimate with no end in sight (the sympy expansion per block,
times Bell-number partitions per support); the stage was rewritten on
integer coefficient lists with primitive supports only, and runs in
214 s. The first run's partial print had already shown the two (2,2,3)
rows above, which the first matcher (written for a (2,6) other side)
reported as not the family; the family is read on its (3,4) side now,
and that is the reading the finding states.
"""

import os
import sys
import time
from collections import Counter
from itertools import combinations
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import Poly

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import (X, check, CHECKS, menu_poly, used_vars,
                                zfactors, is_nonneg, block_product,
                                set_partitions, is_atomic)
from explore_descent_hunt import build_box, build_pairs, core_of

N_ONEVAR = int(os.environ.get("M34_N", "24"))


# ------------------------------------------------ atomic factorizations, indexed
def atomic_factorizations(core, gens):
    """The N-irreducible factorizations as index partitions of the core.

    explore_menu_reach.count_from_core returns the blocks as polynomials;
    the dichotomy below needs divisibility ACROSS blocks, which on index
    sets is multiset inclusion of the atoms, so the partition is kept.
    """
    cache, found = {}, {}
    for part in set_partitions(list(range(len(core)))):
        blocks = []
        for idxs in part:
            b = block_product(core, idxs)
            if not is_nonneg(b, gens):
                break
            if not is_atomic(core, idxs, gens, cache):
                break
            blocks.append((tuple(sorted(idxs)), b))
        else:
            key = tuple(sorted(sympy.srepr(b) for _, b in blocks))
            found[key] = blocks
    return list(found.values())


def atom_multiset(core, idxs):
    return Counter(sympy.srepr(core[i]) for i in idxs)


def divides(core, x, y):
    """Block x divides block y: x's atom multiset sits inside y's."""
    mx, my = atom_multiset(core, x), atom_multiset(core, y)
    return all(my[k] >= v for k, v in mx.items())


def classify(core, P, Q, gens):
    """(verdict, shape, spectators) for two atomic factorizations.

    Common blocks are set aside as spectators; on what remains, SHARED
    when some block of one side divides some block of the other, MIXING
    otherwise. Shape = the block values (term counts) of each residual
    side.
    """
    keyP = Counter(sympy.srepr(b) for _, b in P)
    keyQ = Counter(sympy.srepr(b) for _, b in Q)
    common = keyP & keyQ
    nspec = sum(common.values())
    residP, residQ = [], []
    for side, resid in ((P, residP), (Q, residQ)):
        left = Counter(common)
        for i, b in side:
            k = sympy.srepr(b)
            if left[k] > 0:
                left[k] -= 1
            else:
                resid.append((i, b))
    valsP = tuple(sorted(int(b.subs({g: 1 for g in gens})) for _, b in residP))
    valsQ = tuple(sorted(int(b.subs({g: 1 for g in gens})) for _, b in residQ))
    shape = f"{valsP}v{valsQ}"
    shared = any(divides(core, x, y) or divides(core, y, x)
                 for x, _ in residP for y, _ in residQ)
    return ("SHARED" if shared else "MIXING"), shape, nspec, residP, residQ


# ---------------------------------------------------------- the family template
def support(expr, gens):
    return [tuple(m) for m in Poly(expr, *gens).monoms()]


def vsub(p, q):
    return tuple(a - b for a, b in zip(p, q))


def vadd(p, q):
    return tuple(a + b for a, b in zip(p, q))


def vscale(k, p):
    return tuple(k * a for a in p)


def vgcd(p):
    g = 0
    for a in p:
        g = gcd(g, abs(a))
    return g


def match_family(blocksP, blocksQ, gens):
    """e if {P} against {Q} is the family template (either order), else None.

    Reads the 3-block's support as {p0, p0 + 2e v, p0 + 4e v}, then checks
    the 2-block is {c0, c0 + 3e v}, the 4-block {b0, b0 + 3e v, b1,
    b1 + e v} with b1 - b0 off the line, and the 6-block {d0, d0 + 2e v,
    d0 + 4e v, d1, d1 + e v, d1 + 2e v}.
    """
    sides = [(blocksP, blocksQ), (blocksQ, blocksP)]
    for S1, S2 in sides:
        v1 = sorted(S1, key=lambda b: len(support(b, gens)))
        v2 = sorted(S2, key=lambda b: len(support(b, gens)))
        if len(v1) != 2 or len(v2) != 2:
            continue
        A, B = v1
        C, D = v2
        if [len(support(b, gens)) for b in (A, B, C, D)] != [3, 4, 2, 6]:
            continue
        pts = sorted(support(A, gens))
        for p0 in pts:
            others = [p for p in pts if p != p0]
            for p1 in others:
                p2 = [p for p in others if p != p1][0]
                d1, d2 = vsub(p1, p0), vsub(p2, p0)
                if d2 != vscale(2, d1):
                    continue
                g = vgcd(d1)
                if g == 0 or g % 2:
                    continue
                e = g // 2
                v = tuple(a // g for a in d1)
                # the 2-block
                cs = sorted(support(C, gens))
                if vsub(cs[1], cs[0]) not in (vscale(3 * e, v), vscale(-3 * e, v)):
                    continue
                # the 4-block: one slice {b0, b0+3ev}, one {b1, b1+ev}
                bs = set(support(B, gens))
                ok4 = False
                for b0 in bs:
                    if vadd(b0, vscale(3 * e, v)) in bs:
                        rest = bs - {b0, vadd(b0, vscale(3 * e, v))}
                        for b1 in rest:
                            if vadd(b1, vscale(e, v)) in rest:
                                off = vsub(b1, b0)
                                # off the line: not an integer multiple of v
                                onl = (vgcd(off) == 0) or all(
                                    off[i] * v[j] == off[j] * v[i]
                                    for i in range(len(v)) for j in range(i + 1, len(v)))
                                if not onl:
                                    ok4 = True
                if not ok4:
                    continue
                ds = set(support(D, gens))
                ok6 = False
                for d0 in ds:
                    if all(vadd(d0, vscale(k * e, v)) in ds for k in (2, 4)):
                        rest = ds - {vadd(d0, vscale(k * e, v)) for k in (0, 2, 4)}
                        for dd1 in rest:
                            if all(vadd(dd1, vscale(k * e, v)) in rest for k in (1, 2)):
                                ok6 = True
                if ok6:
                    return e
    return None


def trinomial_reducible(expr, gens):
    _, core = zfactors(expr)
    return len(core) > 1


# ========================================================= S0  the controls
def pair_report(A, B, label):
    gA, cA = core_of(A)
    gB, cB = core_of(B)
    g = sorted(set(gA) | set(gB), key=lambda v: X.index(v))
    core = cA + cB
    facs = atomic_factorizations(core, g)
    rows = []
    for i1, i2 in combinations(range(len(facs)), 2):
        verdict, shape, nspec, rP, rQ = classify(core, facs[i1], facs[i2], g)
        e = match_family([b for _, b in rP], [b for _, b in rQ], g)
        rows.append((verdict, shape, nspec, e))
    print(f"  {label}: {set(A)} x {set(B)} -> {len(facs)} atomic factorizations; "
          + "; ".join(f"{v} {s} spect={n} family_e={e}" for v, s, n, e in rows))
    return facs, rows


def tilings_3_2(S):
    """All (T, U) with S = T + U direct, |T| = 3 (T contains min S) and
    all (K, W) with |K| = 2, as frozensets. Bitmask arithmetic."""
    out2, out3 = [], []
    bits = [i for i in range(S.bit_length()) if S >> i & 1]
    m0 = bits[0]
    for k in bits[1:]:
        k -= m0
        rem, W = S, []
        ok = True
        while rem:
            x = (rem & -rem).bit_length() - 1
            if not (rem >> (x + k)) & 1:
                ok = False
                break
            rem &= ~(1 << x)
            rem &= ~(1 << (x + k))
            W.append(x)
        if ok:
            out2.append((k, tuple(W)))
    for i, j in combinations(bits[1:], 2):
        i, j = i - m0, j - m0
        rem, U = S, []
        ok = True
        while rem:
            x = (rem & -rem).bit_length() - 1
            if not ((rem >> (x + i)) & 1 and (rem >> (x + j)) & 1):
                ok = False
                break
            rem &= ~((1 << x) | (1 << (x + i)) | (1 << (x + j)))
            U.append(x)
        if ok:
            out3.append(((0, i, j), tuple(U)))
    return out2, out3


def stage0():
    print("\n=== S0  the positive controls ===")
    facs, rows = pair_report((2, 8, 32), (2, 6, 12, 16), "control (a), the m = 6 object")
    check("S0a: the m = 6 object counts 2 atomic factorizations", len(facs) == 2)
    check("S0a: and reads MIXING", rows and rows[0][0] == "MIXING")
    check("S0a: and matches the family at e = 1", rows and rows[0][3] == 1)
    facs, rows = pair_report((2, 8, 32), (2, 4, 16, 32), "control (b), the graded t = 12 point")
    check("S0b: the graded point reads SHARED at every pair",
          rows and all(r[0] == "SHARED" for r in rows))
    # (c) the cycle lemma, exhaustively to exponent 30
    print("  control (c): the cycle lemma over {0,a,b} + {0,s}, exponents to 30")
    n_dir, n_coll, n_ident = 0, 0, 0
    bad = []
    for a in range(1, 31):
        for b in range(a + 1, 31):
            for s in range(1, 31):
                S = 0
                pts = [0, a, b, s, a + s, b + s]
                if len(set(pts)) < 6:
                    continue
                for p in pts:
                    S |= 1 << p
                n_dir += 1
                out2, out3 = tilings_3_2(S)
                alt = [(k, W) for k, W in out2 if k != s]
                if alt:
                    n_coll += 1
                    # the identity: {0,a,b} in {e{0,1,2}, e{0,2,4}} and the two
                    # binomials {s, k} = {e, 3e} in the matching order
                    ok = False
                    for k, W in alt:
                        e = min(s, k)
                        if {s, k} == {e, 3 * e} and (
                            ((a, b) == (2 * e, 4 * e) and s == e)
                            or ((a, b) == (e, 2 * e) and s == 3 * e)):
                            ok = True
                    if ok:
                        n_ident += 1
                    else:
                        bad.append((a, b, s, alt))
    print(f"    {n_dir} direct sums, {n_coll} with a second (3,2) decomposition, "
          f"{n_ident} of them the t = 6 identity; exceptions: {bad[:5]}")
    check("S0c: every 6-term (3,2)-against-(3,2) collision to exponent 30 is the t = 6 identity",
          n_coll > 0 and n_coll == n_ident)


# ============================================================ S1  the census
def stage1():
    print("\n=== S1  the census: the 71, classified at the atomic level ===")
    t0 = time.time()
    menus, seeds, cores, gensof = build_box()
    pairs = build_pairs(menus, seeds)
    rows = []
    n_inframe = 0
    for i, (A, B) in enumerate(pairs):
        g = sorted(set(gensof[A]) | set(gensof[B]), key=lambda v: X.index(v))
        core = cores[A] + cores[B]
        facs = atomic_factorizations(core, g)
        if len(facs) < 2:
            continue
        prod = sympy.expand(menu_poly(A) * menu_poly(B))
        nterms = len(Poly(prod, *g).monoms())
        if nterms != 12:
            continue
        n_inframe += 1
        for i1, i2 in combinations(range(len(facs)), 2):
            verdict, shape, nspec, rP, rQ = classify(core, facs[i1], facs[i2], g)
            e = match_family([b for _, b in rP], [b for _, b in rQ], g)
            dim3 = trinomial_reducible(menu_poly(A), g)
            rows.append((A, B, len(facs), verdict, shape, nspec, e, dim3))
            print(f"    {set(A)} x {set(B)}: {len(facs)} fac, {verdict} {shape} "
                  f"spect={nspec} family_e={e} A_reducible={dim3}")
        if (i + 1) % 20000 == 0:
            print(f"    ... {i+1}/{len(pairs)} walked   [{time.time()-t0:.1f}s]")
    print(f"  walked {len(pairs)} pairs in {time.time()-t0:.1f}s: "
          f"{n_inframe} in-frame collisions, {len(rows)} factorization pairs")
    tally = Counter((r[3], r[4], r[5] > 0) for r in rows)
    for (v, s, sp), n in sorted(tally.items()):
        print(f"    {n:3d}  {v} {s} spectator={sp}")
    return rows, n_inframe


def stage2(rows, n_inframe):
    print("\n=== S2  the lemmas on the box ===")
    mixing = [r for r in rows if r[3] == "MIXING"]
    print(f"  mixing pairs: {len(mixing)}")
    for r in mixing:
        print(f"    {set(r[0])} x {set(r[1])}  {r[4]} family_e={r[6]}")
    check("S1: 71 in-frame collisions, the published count", n_inframe == 71)
    # the family at e = 1, v = the monomial of 2, in the size-4 box {2..24}:
    # B = c'.{1, 8} + m.{1, 2}, four distinct elements, m/c' not a power of 2
    expected = set()
    for cp in range(2, 25):
        for m in range(2, 25):
            B = {cp, 8 * cp, m, 2 * m}
            if max(B) > 24 or len(B) < 4:
                continue
            r = sympy.Rational(m, cp)
            if r.q == 1 and (r.p & (r.p - 1)) == 0:
                continue
            if r.p == 1 and (r.q & (r.q - 1)) == 0:
                continue
            expected.add(((2, 8, 32), tuple(sorted(B))))
    got = {(r[0], tuple(sorted(r[1]))) for r in mixing}
    print(f"  family members the box admits (computed): {len(expected)}; "
          f"mixing pairs printed: {len(got)}")
    check("S1/PR2: the mixing pairs are exactly the family's members the box admits "
          "(the slate said eight; the run prints the count)", got == expected)
    check("S2: no mixing pair carries a spectator", all(r[5] == 0 for r in mixing))
    check("S2: every mixing pair's 3-block is a reducible trinomial", all(r[7] for r in mixing))
    check("S2: every mixing pair matches the family template (all are 2-variable here)",
          all(r[6] is not None for r in mixing))
    check("S2: every pair with a spectator is shared",
          all(r[3] == "SHARED" for r in rows if r[5] > 0))


# =================================================== S3  the family off the box
def family_polys(e, z, v=None):
    v = v if v is not None else X[0]
    A = 1 + v**(2 * e) + v**(4 * e)
    B = (1 + v**(3 * e)) + z * (1 + v**e)
    C = 1 + v**(3 * e)
    D = (1 + v**(2 * e) + v**(4 * e)) + z * (1 + v**e + v**(2 * e))
    return [sympy.expand(p) for p in (A, B, C, D)]


def stage3():
    print("\n=== S3  the family off the box ===")
    allok = True
    for e in (1, 2, 3, 4):
        A, B, C, D = family_polys(e, X[1])
        g = [X[0], X[1]]
        prod = sympy.expand(A * B)
        check_eq = sympy.expand(C * D) == prod
        nterms = len(Poly(prod, *g).monoms())
        _, core = zfactors(prod)
        facs = atomic_factorizations(core, g)
        rows = []
        for i1, i2 in combinations(range(len(facs)), 2):
            verdict, shape, nspec, rP, rQ = classify(core, facs[i1], facs[i2], g)
            fe = match_family([b for _, b in rP], [b for _, b in rQ], g)
            rows.append((verdict, shape, nspec, fe))
        ok = (check_eq and nterms == 12 and len(facs) == 2
              and rows and rows[0][0] == "MIXING" and rows[0][3] == e)
        allok &= ok
        print(f"  e = {e}: A*B == C*D {check_eq}, {nterms} terms, {len(facs)} atomic "
              f"factorizations, {rows}")
    # menu clothes: q = 3 at e = 1, and q = 2 at e = 2
    for A, B, label in (((2, 18, 162), (2, 54, 10, 30), "q = 3, e = 1, c = c' = 2, z = 5"),
                        ((2, 32, 512), (2, 128, 3, 12), "q = 2, e = 2, c = c' = 2, z = 3/2"),
                        ((3, 12, 48), (5, 40, 7, 14), "q = 2, e = 1, c = 3, c' = 5, z = 7/5")):
        facs, rows = pair_report(A, B, label)
        allok &= (len(facs) == 2 and rows[0][0] == "MIXING")
    check("S3/PR4: every constructed member counts 2 and reads MIXING at its e", allok)


# =================================================== S4  the one-variable search
def conv(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def atoms_of_support(S, x):
    """The Z-irreducible atoms of the 0/1 polynomial with support S, as
    integer coefficient lists (monomial factors dropped)."""
    F = sum(x**i for i in S)
    _, fl = sympy.factor_list(sympy.expand(F))
    atoms = []
    for f, mult in fl:
        if f == x:
            continue
        cs = [int(c) for c in reversed(Poly(f, x).all_coeffs())]
        atoms.extend([cs] * mult)
    return atoms


def atomic_factorizations_1var(atoms):
    """Index partitions into nonnegative atomic blocks, one-variable, fast."""
    prods, nonneg, atomic = {}, {}, {}

    def prod(idxs):
        key = tuple(sorted(idxs))
        if key not in prods:
            p = [1]
            for i in key:
                p = conv(p, atoms[i])
            prods[key] = p
            nonneg[key] = all(c >= 0 for c in p)
        return key

    def is_atomic_1(key):
        if key in atomic:
            return atomic[key]
        v = True
        if len(key) > 1:
            for r in range(1, len(key) // 2 + 1):
                for sub in combinations(key, r):
                    rest = tuple(i for i in key if i not in set(sub))
                    if nonneg[prod(sub)] and nonneg[prod(rest)]:
                        v = False
                        break
                if not v:
                    break
        atomic[key] = v
        return v

    found = {}
    for part in set_partitions(list(range(len(atoms)))):
        blocks = []
        for idxs in part:
            key = prod(idxs)
            if not nonneg[key] or not is_atomic_1(key):
                break
            blocks.append(key)
        else:
            sig = tuple(sorted(tuple(prods[k]) for k in blocks))
            found[sig] = blocks
    return list(found.values()), prods


def classify_1var(atoms, P, Q, prods):
    keyP = Counter(tuple(prods[k]) for k in P)
    keyQ = Counter(tuple(prods[k]) for k in Q)
    common = keyP & keyQ
    nspec = sum(common.values())
    rP, rQ = [], []
    for side, resid in ((P, rP), (Q, rQ)):
        left = Counter(common)
        for k in side:
            t = tuple(prods[k])
            if left[t] > 0:
                left[t] -= 1
            else:
                resid.append(k)

    def vals(ks):
        return tuple(sorted(sum(prods[k]) for k in ks))

    shape = f"{vals(rP)}v{vals(rQ)}"

    def div(a, b):
        ca = Counter(tuple(atoms[i]) for i in a)
        cb = Counter(tuple(atoms[i]) for i in b)
        return all(cb[t] >= n for t, n in ca.items())

    shared = any(div(a, b) or div(b, a) for a in rP for b in rQ)
    return ("SHARED" if shared else "MIXING"), shape, nspec, rP, rQ


def supp(coeffs):
    return [i for i, c in enumerate(coeffs) if c]


def family_side_1var(rP, rQ, prods):
    """Read the family's (3,4) side on either residual side: A = {0,2e,4e},
    B = {b0, b0+3e, b1, b1+e}. Returns (e, other-side shape) or None."""
    for S1, S2 in ((rP, rQ), (rQ, rP)):
        if len(S1) != 2:
            continue
        b = sorted(S1, key=lambda k: sum(prods[k]))
        A, B = supp(prods[b[0]]), supp(prods[b[1]])
        if len(A) != 3 or len(B) != 4:
            continue
        if A[1] - A[0] != A[2] - A[1] or (A[1] - A[0]) % 2:
            continue
        e = (A[1] - A[0]) // 2
        eb = set(B)
        ok = any(b0 + 3 * e in eb and any(b1 + e in eb - {b0, b0 + 3 * e}
                                          for b1 in eb - {b0, b0 + 3 * e})
                 for b0 in eb)
        if ok:
            other = tuple(sorted(sum(prods[k]) for k in S2))
            return e, other
    return None


def stage4():
    print(f"\n=== S4  one-variable (3,4) products, exponents to {N_ONEVAR} ===")
    t0 = time.time()
    N = N_ONEVAR
    found = {}
    n_direct = 0
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            T = (1 << 0) | (1 << a) | (1 << b)
            for u1, u2, u3 in combinations(range(1, N + 1), 3):
                S = T | (T << u1) | (T << u2) | (T << u3)
                if bin(S).count("1") != 12:
                    continue
                n_direct += 1
                out2, out3 = tilings_3_2(S)
                alt3 = [t for t in out3 if t[0] != (0, a, b)]
                if out2 or alt3:
                    found.setdefault(S, []).append(((0, a, b), (0, u1, u2, u3)))
    # a support whose exponents share a factor d is the image of one at
    # exponents/d, already walked: primitive supports only
    prim = {}
    for S in found:
        pts = [i for i in range(S.bit_length()) if S >> i & 1]
        g = 0
        for p in pts:
            g = gcd(g, p)
        if g == 1:
            prim[S] = pts
    print(f"  {n_direct} direct products, {len(found)} distinct supports with a second "
          f"tiling, {len(prim)} primitive   [{time.time()-t0:.1f}s]")
    x = X[0]
    n_coll, n_mix = 0, 0
    tally, mixkinds, offenders, mix_rows = Counter(), Counter(), [], []
    for n_done, (S, pts) in enumerate(sorted(prim.items())):
        atoms = atoms_of_support(pts, x)
        facs, prods = atomic_factorizations_1var(atoms)
        if len(facs) < 2:
            continue
        n_coll += 1
        for i1, i2 in combinations(range(len(facs)), 2):
            verdict, shape, nspec, rP, rQ = classify_1var(atoms, facs[i1], facs[i2], prods)
            tally[(verdict, shape, nspec > 0)] += 1
            if verdict == "MIXING":
                n_mix += 1
                fs = family_side_1var(rP, rQ, prods)
                if fs is None:
                    kind = "NOT-FAMILY"
                    offenders.append((pts, shape,
                                      [supp(prods[k]) for k in rP],
                                      [supp(prods[k]) for k in rQ]))
                else:
                    kind = f"family (3,4) side at e={fs[0]}, other side {fs[1]}"
                mixkinds[kind] += 1
                mix_rows.append((pts, shape, kind))
        if (n_done + 1) % 2000 == 0:
            print(f"    ... {n_done+1}/{len(prim)} factored, {n_coll} collisions, "
                  f"{n_mix} mixing   [{time.time()-t0:.1f}s]")
    print(f"  {n_coll} primitive one-variable collisions (>= 2 atomic factorizations), "
          f"{n_mix} mixing pairs   [{time.time()-t0:.1f}s]")
    for (v, s, sp), n in sorted(tally.items()):
        print(f"    {n:4d}  {v} {s} spectator={sp}")
    print("  mixing pairs by kind:")
    for k, n in sorted(mixkinds.items()):
        print(f"    {n:4d}  {k}")
    for pts, shape, kind in mix_rows[:40]:
        print(f"    MIXING {shape} support {pts}  -> {kind}")
    if len(mix_rows) > 40:
        print(f"    ... {len(mix_rows) - 40} more mixing rows not printed")
    if offenders:
        print("  OFFENDERS (mixing with no family (3,4) side):")
        for o in offenders[:20]:
            print("   ", o)
    check("S4: one-variable mixing exists (the family's line members)", n_mix > 0)
    check("S4/PR5: every one-variable mixing pair carries the family's (3,4) side",
          n_mix > 0 and not offenders)
    return n_coll, n_mix, offenders


def main():
    t0 = time.time()
    stages = os.environ.get("M34_STAGES", "01234")
    if "0" in stages:
        stage0()
        if not all(ok for _, ok in CHECKS):
            print("\nK0: a control failed; nothing below is read.")
    if "1" in stages:
        rows, n_inframe = stage1()
        stage2(rows, n_inframe)
    if "3" in stages:
        stage3()
    if "4" in stages:
        stage4()
    print(f"\n=== {sum(ok for _, ok in CHECKS)}/{len(CHECKS)} checks passed, "
          f"{time.time()-t0:.1f}s ===")
    if not all(ok for _, ok in CHECKS):
        sys.exit(1)


if __name__ == "__main__":
    main()
