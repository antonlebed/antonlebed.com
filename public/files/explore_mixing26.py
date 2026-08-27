"""The mixing pair with no three-term block: (2,6) against (2,6), and the
binomial-pair criterion that decides it.

THE QUESTION. The mixing theorem (explore_mixing34.py) classifies every
mixing collision at twelve terms that carries a three-term block on
either side: one-variable, or the family. The one shape it does not
reach is a twelve-term 0/1 product with two atomic factorizations of
block sizes {2,6} on BOTH sides -- P = (1+u) H = (1+u') H' with u != u'
monomials and H, H' six-term 0/1 blocks -- mixing, that is, with neither
binomial dividing the other side's block or binomial. No census has
shown one. This file asks whether one exists, in one variable by census
and in any number of variables by derivation, and what decides it.

WHOSE VOCABULARY. Shared and mixing are the mixing theorem's: read on
ATOMIC factorizations, common blocks set aside as spectators, SHARED
when some block of one side divides (on the Z-atom multiset) some block
of the other, MIXING otherwise. A (2,6)-against-(2,6) pair can carry no
spectator (u != u' and H = H' would force u = u') and no six-block can
divide the other side's six-block or binomial, so its verdict is the
one question: does 1+u divide H' or 1+u', or 1+u' divide H or 1+u. The
suspicion is written in this file's own vocabulary -- the two binomials
as two perfect matchings on the twelve points -- and the cycle lemma is
marked as a TRANSPLANT from the (3,4) file: there it closed a six-cycle
with the ratio k = 3s; here the same walk is run at every even length
with the ratio free.

THE HAND-ATTACK, on paper before any engine code (the theorem is
restated in the finding once the run has printed). Four
passes and one specimen.
  1. OFF THE LINE, SHARED FOR FREE. Write u = w^s, u' = w'^k with w, w'
     primitive monomials. If w and w' are independent, every
     irreducible factor of 1+u is a cyclotomic in w alone and none is
     associate to a factor of 1+u', so in the Laurent ring (a UFD, units
     the +-monomials) every atom of the squarefree 1+u divides H'.
     Specimen: the plus-pentomino outline, twelve lattice points tiled
     by horizontal and by vertical dominoes, (1+x) H = (1+y) H' with
     H' = (1+x)(x + y - xy + x^2 y + x y^2).
  2. ON THE LINE, THE CLASS REDUCTION. u = v^s, u' = v^k, v primitive,
     g = gcd(s,k), s = g s', k = g k', w = v^g. Split the support along
     the cosets of <w>: P = sum_c m_c P_c(w), the coset monomials m_c a
     free basis over Z[w, 1/w]. Each slice is a one-variable set tiled
     by s'-pairs and by k'-pairs, and 1+w^{s'} divides H' iff it divides
     every slice H'_c. H itself need not be one-variable.
  3. THE PARITY SPLIT. gcd(s',k') = 1. Different parity: the two
     binomials are coprime and pass 1 applies -- shared. Both odd:
     1+w^{s'} = prod_{d | s'} Phi_{2d}(w), and every Phi_{2d} with d > 1
     is coprime to 1+w^{k'} and divides every H'_c; the one atom in
     question is 1+w, which divides 1+w^{k'} exactly once. So 1+u
     divides H' iff (1+w)^2 divides every P_c, iff P_c'(-1) = 0 for
     every class -- and since P_c = (1+w^{s'}) H_c gives P_c'(-1) =
     s' H_c(-1), iff every slice of H has as many even as odd exponents.
     The multiplicity of 1+w in P_c is 1 + mult(H_c) = 1 + mult(H'_c),
     so the condition read from the other side (1+u' | H) is the SAME
     condition. s' = 1 is 1+u dividing 1+u' outright.
     THE CRITERION (binomial pairs, any size, any number of variables):
     (1+u)H against (1+u')H' mixes iff u and u' lie on one line, s/g
     and k/g are coprime odd integers >= 3, and some class has
     P_c'(-1) != 0.
  4. THE CYCLES DECIDE P_c'(-1). In a class the steps s', k' are both
     odd, so parity alternates round every cycle of the two matchings'
     union. A 2m-cycle whose signed s'-steps sum to a s' and signed
     k'-steps to b k' closes iff a s' + b k' = 0, with a = b = m (mod 2)
     and |a|, |b| <= m; H_c's points on it (the lower endpoints of its
     s'-pairs) are (m+a)/2 of one parity and (m-a)/2 of the other, so
     H_c(-1) is a signed sum of the cycles' a's. A cycle with a != 0
     needs k' | a and s' | b, hence m >= max(s',k') >= 5: the 4-cycle
     (a rectangle {0,s'}+{0,k'}+x), the 8-cycle and the 12-cycle all
     have a = 0 (the 12-cycle: a even and >= 5 gives |a| = 6 = 2k', so
     k' = 3 and b = 2s' <= 6 forces s' = 3 = k'); the 6-cycle needs
     m = 3 < 5 and does not exist at all with coprime odd s', k' >= 3
     (the cycle lemma's k = 3s is the non-coprime case); the 10-cycle is
     inhabited at (s',k') = (3,5): 0, 3, -2, 1, -4, -1, -6, -3, -8, -5.
     A twelve-point support has no 2-slice and no 6-cycle, so it is a
     union of 4-, 8- and 12-cycles, every one with a = 0, and 1+u
     divides H'.
  THE THEOREM the attack derives: a (2,6)-against-(2,6) pair at twelve
  terms is SHARED, always, in any number of variables. With the mixing
  theorem: every mixing pair at twelve terms has a three-term block and
  is one-variable or the family.
  THE SPECIMEN, ten terms: S = {0,2,3,4,5,6,7,8,9,11} = {0,3}+{0,2,4,6,8}
  = {0,5}+{0,2,3,4,6}. H = Phi5(v^2) = Phi5 Phi10 (atomic, Phi10 having
  a negative coefficient), H' = Phi5 Phi6 (atomic), P = Phi2 Phi5 Phi6
  Phi10, and among the sub-products of the four atoms the nonnegative
  ones give exactly the two factorizations: (2,5) against (2,5), no
  spectator, no block dividing across. MIXING at ten terms with no
  three-term block. At fourteen, 10 + 4 is a shape the criterion
  permits; whether its 7-blocks stay atomic is a measurement.

DISTRUST THE MARGIN, not the kill. The kill -- a twelve-term (2,6)v(2,6)
row reading MIXING -- is what the census prints. The margins: (i) the
census is one-variable and to an exponent bound, and the theorem is
what makes it transferable; the rig checks the theorem's own steps at
every row (every cycle zero-sum, both binomials dividing across) rather
than only the verdict. (ii) The ten-term specimen was found by hand
from the 10-cycle; its atomicity is asserted by the counter, not
assumed. (iii) The criterion's sufficiency is checked where it has
content -- ten and fourteen terms -- by comparing its verdict with the
atomic classification at every (2,n)v(2,n) pair.

DESIGN, three stages.
 S0 THE CONTROLS, read before any census number. (a) The ten-term
    specimen must count exactly 2 atomic factorizations and classify
    MIXING (2,5)v(2,5), no spectator. (b) The plus outline, in two
    variables, must count 2 and classify SHARED (2,6)v(2,6), no
    spectator. (c) The criterion function must say MIXING of (a) and,
    on the line, SHARED of the cycle lemma's own object {0,1}+{0,...,5}
    (s' = 1) and of a rectangle-times-trinomial (every cycle a
    rectangle).
 S1 THE TWELVE-TERM CENSUS, one variable. Every support {0,s}+H with
    H a six-set containing 0, exponents to M26_NC (default 36), that
    admits a second binomial tiling k != s; for every pair of binomial
    tilings the cycle decomposition (lengths and closing sums), the
    criterion's verdict and its reason. Then, to M26_N (default 24),
    the atomic factorizations of every such primitive support and the
    pairwise classification: every (2,6)v(2,6) pair's verdict against
    the criterion's, the divisibility both ways, every other shape
    tallied beside it ((2,2,3)v(2,6) among them).
 S2 TEN AND FOURTEEN TERMS, the same census at block size 5 (to M26_N)
    and 7 (to M26_N7, default 20): the mixing (2,n)v(2,n) rows printed
    with their cycle types, the criterion compared at every pair.

PREDICTIONS (fixed before the engine, and before any run).
  PR0 (S0): the three controls read as stated.
  PR1 (S1): ZERO mixing (2,6)v(2,6) rows; every (2,6)v(2,6) pair is
      SHARED with EACH binomial dividing the other side's six-block;
      every cycle of every binomial pair has closing sums a = b = 0;
      the criterion agrees with the classification at every
      (2,6)v(2,6) pair. The counts of supports and of the other
      shapes are the measurement.
  PR2 (S2): at ten terms mixing (2,5)v(2,5) pairs exist, the specimen
      among them, every one at s/g, k/g coprime odd >= 3 with a
      10-cycle in some class; the criterion agrees at every pair. The
      count is not predicted. At fourteen terms the criterion agrees
      at every pair; whether any mixing row exists is not predicted.

KILLS (observables; what each means is weighed after the run).
  K0: a control misreads -- the instrument is broken, nothing below is
      read.
  K1: S1 prints a MIXING (2,6)v(2,6) row, or a cycle with a != 0, or a
      (2,6)v(2,6) pair where the criterion and the classification
      disagree -- the derivation has a hole, and its location is the
      printed row.
  K2: S2 prints zero mixing rows at ten terms -- the specimen is wrong
      or the rig cannot see a mixing binomial pair, and PR1's zero is
      not read.
  K3: S2 prints a pair at ten or fourteen terms where the criterion
      and the classification disagree -- the criterion is wrong at
      that row.

HONEST LIMITS, named before the run. (i) The census is one-variable
and bounded; the multi-variable claim rests on passes 1-2, checked at
one specimen. (ii) Atomicity and the counter are explore_menu_reach.py's
and the one-variable fast path is explore_mixing34.py's, imported and
controlled in S0, not re-proved. (iii) The criterion decides
binomial-against-binomial pairs only; nothing here is said of a pair
whose sides differ in block sizes beyond what the mixing theorem says.

RUN RECORD. Wall-clock estimate: S1's support walk is C(37,6) ~ 2.3M
bitmask tests, under a minute; the atomic classification to exponent
24 is a fraction of explore_mixing34.py's stage 4 (fewer supports),
minutes at most; S2 is smaller. Under 512 MB by the predecessor's peak.
Runs: the first full run passed ten minutes with no print and was
killed -- not the census but an infinite walk in the cycle finder,
which stepped to p + s whenever that point was present instead of along
the tiling's own pair (redesigned to walk the tilings' pair maps). The
closing-sum assertion was then corrected from a s = b k to a s + b k = 0
(a sign convention; nothing in the derivation moves). Two checks then
failed on their own letter, not on the derivation: the both-binomials-
divide clause was asserted at every shared pair where the derivation
states it only off the divisible branch, and a branch slip in narrowing
it counted divisible-branch shared rows as mixing for one run; both
narrowed to what the derivation claims. The audit then reordered the
criterion's branches so s' = 1 against an even k' reads as coprime, not
as dividing (verdicts unchanged, the tallies below re-read from the
rerun). Final: 9/9 checks, 45.5 s,
peak working set 65.4 MB (memwatch), atomic bound 30 at twelve and ten
terms, 24 at fourteen, cycle census to 36.

FINDINGS (post-run; every figure below is the run's own print).

0. THE CONTROLS PASS (K0 did not fire). The ten-term specimen has four
   Z-atoms and exactly two atomic factorizations, {0,3} x {0,2,4,6,8}
   and {0,5} x {0,2,3,4,6}, MIXING (2,5)v(2,5) with no spectator. The
   plus outline's core is {1+x, 1+y, x + y - xy + x^2 y + x y^2} and
   its two atomic factorizations read SHARED (2,6)v(2,6). The criterion
   reads MIXING at the specimen (P'(-1) = 15), SHARED at the cycle
   lemma's object (one binomial divides the other) and at the
   rectangle product (every class with (1+w)^2).

1. TWELVE TERMS: THE SHAPE IS SHARED, AND THE CYCLES SAY WHY (theorem,
   proved in the hand-attack; the census exact in its box; K1 did not
   fire). 879,133 direct binomial x 6-set products to exponent 36 give
   15,276 supports with a second binomial tiling and 15,459 tiling
   pairs. Cycle types: (4,4,4) at 15,332 pairs, (12) at 37, (6,6) at
   90 -- and NO (8,4): a zero-sum 8-cycle does not occur on the line at
   all. The only nonzero closing sums are the 90 (6,6) pairs, every one
   on the divisible branch (k = 3s, the cycle lemma's object); off that
   branch every cycle closes with a = b = 0. The criterion reads SHARED
   at all 15,459 pairs: 10,334 coprime of different parity, 2,800 with
   one binomial dividing the other (s' = 1 or k' = 1 with the other
   ODD -- the audit found the even case labelled here too, where the
   binomials are coprime and nothing divides), 2,325 by (1+w)^2 in
   every class.
   Of the 5,960 primitive supports to exponent 30, 69 carry >= 2 atomic
   factorizations: 49 pairs the t = 6 identity beside a spectator
   ((2,3)v(2,3)), 1 pair (2,2,3)v(2,2,3) shared, 2 pairs MIXING
   (2,2,3)v(3,4) -- the family's two line members whose six-block
   splits, explore_mixing34.py's finding 4 -- and 19 pairs (2,6)v(2,6),
   EVERY ONE SHARED, the criterion agreeing at each and EACH binomial
   dividing the other side's six-block. Zero mixing (2,6)v(2,6) rows.
   PR1's letter -- "every cycle of every binomial pair" zero-sum --
   overreached the derivation, which excludes nonzero sums only off the
   divisible branch; the (6,6) pairs at k = 3s are exactly the cycle
   lemma's, and the check was narrowed to the derivation's claim.

2. THE EMPTINESS IS TWELVE'S (observation, exact in the boxes; K2 and
   K3 did not fire). Ten terms, block size 5, exponents to 30: 142
   supports, 114 primitive, all 114 collisions (2,5)v(2,5), and exactly
   ONE mixing -- the specimen {0,2,3,4,5,6,7,8,9,11} at (s,k) = (3,5),
   the single 10-cycle with closing sums (5,-3), P'(-1) = 15. Its
   dilate at (6,10) is the only other mixing tiling pair in the census.
   Fourteen terms, block size 7, exponents to 24: 385 supports, all
   primitive, all 385 collisions (2,7)v(2,7), 24 MIXING: a 14-cycle at
   (3,7) (closing sums (7,-3)), at (5,7) ((7,-5)) and at (3,5)
   ((5,-3)), or a 10-cycle at (3,5) beside a rectangle, one of them in
   class 1 of (6,10). The criterion agrees with the atomic
   classification at every one of the 114 + 385 pairs, and off the
   divisible branch each shared pair has both binomials dividing
   across. So a mixing collision with no three-term block exists at
   ten terms and at fourteen, and not at twelve: what twelve lacks is
   a cycle with a nonzero closing sum, the shortest being the
   10-cycle, which twelve cannot seat beside a 2-slice.

WHAT THE THEOREM NOW SAYS, with explore_mixing34.py's: every mixing
collision at twelve terms in frame carries a three-term block, hence is
one-variable or the family; the residual class the mixing theorem left
is empty in every number of variables. The criterion is the general
statement for binomial-against-binomial pairs at any size.
"""

import os
import sys
import time
from collections import Counter
from itertools import combinations
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_menu_reach import X, check, CHECKS, zfactors
from explore_mixing34 import (atomic_factorizations, classify,
                              atoms_of_support, atomic_factorizations_1var,
                              classify_1var, supp)

N_ATOMIC = int(os.environ.get("M26_N", "30"))
N_CYCLES = int(os.environ.get("M26_NC", "36"))
N_SEVEN = int(os.environ.get("M26_N7", "24"))


# ------------------------------------------------------------- binomial tilings
def binomial_tilings(S):
    """Every k with S = {0,k} + W direct, as (k, W); S a bitmask."""
    out = []
    bits = [i for i in range(S.bit_length()) if S >> i & 1]
    for k in bits[1:]:
        k -= bits[0]
        rem, W, ok = S, [], True
        while rem:
            x = (rem & -rem).bit_length() - 1
            if not (rem >> (x + k)) & 1:
                ok = False
                break
            rem &= ~((1 << x) | (1 << (x + k)))
            W.append(x)
        if ok:
            out.append((k, tuple(W)))
    return out


def cycles_of(pts, s, k, Ws=None, Wk=None):
    """The alternating cycles of the s-tiling and the k-tiling on pts: a
    list of (length, a, b) with a s + b k = 0 the closing sums. The tilings'
    own pairs (lower endpoints Ws, Wk) define the matchings; when not
    given they are recomputed by the greedy walk from the minimum."""
    P = set(pts)

    def pairs(step, W):
        if W is None:
            rem, W = set(pts), []
            while rem:
                x = min(rem)
                assert x + step in rem, (pts, step)
                rem -= {x, x + step}
                W.append(x)
        m = {}
        for x in W:
            m[x], m[x + step] = (x + step, 1), (x, -1)
        return m

    ms, mk = pairs(s, Ws), pairs(k, Wk)
    seen, out = set(), []
    for p0 in pts:
        if p0 in seen:
            continue
        p, length, a, b = p0, 0, 0, 0
        while True:
            q, da = ms[p]
            seen.add(p)
            seen.add(q)
            r, db = mk[q]
            length += 2
            a += da
            b += db
            p = r
            if p == p0:
                break
        assert a * s + b * k == 0, (pts, s, k, a, b)
        out.append((length, a, b))
    return out


def criterion(pts, s, k):
    """The binomial-pair criterion's verdict for {0,s}+H = {0,k}+H' on
    the support pts, with its reason."""
    g = gcd(s, k)
    s1, k1 = s // g, k // g
    if (s1 - k1) % 2:
        return "SHARED", "coprime binomials, different parity"
    if s1 == 1 or k1 == 1:
        return "SHARED", "one binomial divides the other"
    for c in range(g):
        cls = [(x - c) // g for x in pts if (x - c) % g == 0]
        dP = sum(x if x % 2 else -x for x in cls)   # P_c'(-1)
        if dP != 0:
            return "MIXING", f"class {c}: P_c'(-1) = {dP}"
    return "SHARED", "every class has (1+w)^2 | P_c"


# ------------------------------------------------------------------ the census
def census(n, N_cyc, N_atom, label):
    """Every 2n-term support {0,s}+H (0 in H, exponents to N_cyc) with
    a second binomial tiling; cycles and the criterion at every pair of
    tilings; atomic classification for the primitive ones to N_atom."""
    print(f"\n=== {label}: block size {n}, cycles to {N_cyc}, atomic to {N_atom} ===")
    t0 = time.time()
    found = {}
    n_walked = 0
    for s in range(1, N_cyc + 1):
        for rest in combinations(range(1, N_cyc - s + 1), n - 1):
            H = 1
            for r in rest:
                H |= 1 << r
            S = H | (H << s)
            if bin(S).count("1") != 2 * n:
                continue
            n_walked += 1
            if S in found:
                continue
            tl = binomial_tilings(S)
            if len(tl) >= 2:
                found[S] = tl
    print(f"  {n_walked} direct binomial x {n}-set products, {len(found)} distinct "
          f"supports with >= 2 binomial tilings   [{time.time()-t0:.1f}s]")
    # cycles and the criterion at every pair of tilings
    cyc_tally, crit_tally, nonzero = Counter(), Counter(), []
    n_pairs = 0
    for S, tl in found.items():
        pts = [i for i in range(S.bit_length()) if S >> i & 1]
        for (s, Ws), (k, Wk) in combinations(tl, 2):
            n_pairs += 1
            cyc = cycles_of(pts, s, k, Ws, Wk)
            v, why = criterion(pts, s, k)
            why = why.split(":")[0]
            cyc_tally[(why, tuple(sorted(L for L, _, _ in cyc)))] += 1
            if any(a for _, a, _ in cyc):
                nonzero.append((pts, s, k, cyc, why))
            crit_tally[(v, why)] += 1
    print(f"  {n_pairs} binomial tiling pairs; cycle types by the criterion's branch:")
    for (why, t), c in sorted(cyc_tally.items()):
        print(f"    {c:6d}  {t}  [{why}]")
    # a nonzero closing sum is derived impossible off the divisible branch
    bad = [r for r in nonzero if r[4] != "one binomial divides the other"]
    print(f"  pairs with a nonzero closing sum: {len(nonzero)}, off the divisible "
          f"branch: {len(bad)}")
    for pts, s, k, cyc, why in (bad or nonzero)[:8]:
        print(f"    s={s} k={k} cycles={cyc} [{why}] support {pts}")
    print("  the criterion's verdicts:")
    for (v, why), c in sorted(crit_tally.items()):
        print(f"    {c:6d}  {v}  ({why})")
    # atomic classification of the primitive supports to N_atom
    x = X[0]
    shapes, mix_rows, disagree, oneway = Counter(), [], [], []
    n_coll, n_binpairs = 0, 0
    prim = {S: tl for S, tl in found.items() if S.bit_length() - 1 <= N_atom}
    kept = {}
    for S, tl in prim.items():
        pts = [i for i in range(S.bit_length()) if S >> i & 1]
        g = 0
        for p in pts:
            g = gcd(g, p)
        if g == 1:
            kept[S] = (tl, pts)
    for S, (tl, pts) in sorted(kept.items()):
        atoms = atoms_of_support(pts, x)
        facs, prods = atomic_factorizations_1var(atoms)
        if len(facs) < 2:
            continue
        n_coll += 1
        for i1, i2 in combinations(range(len(facs)), 2):
            verdict, shape, nspec, rP, rQ = classify_1var(atoms, facs[i1], facs[i2], prods)
            shapes[(verdict, shape, nspec > 0)] += 1
            binom = f"(2, {n})v(2, {n})"
            if shape == binom and nspec == 0:
                n_binpairs += 1
                # the two binomials from the residual sides
                sb = [supp(prods[k]) for k in rP if sum(prods[k]) == 2][0]
                kb = [supp(prods[k]) for k in rQ if sum(prods[k]) == 2][0]
                s, k = sb[1] - sb[0], kb[1] - kb[0]
                cv, why = criterion(pts, s, k)
                if cv != verdict:
                    disagree.append((pts, s, k, verdict, cv, why))
                if verdict == "MIXING":
                    mix_rows.append((pts, s, k, cycles_of(pts, s, k), why))
                elif not why.startswith("one binomial"):
                    # off the divisible branch both binomials divide across
                    Hp = [prods[k2] for k2 in rQ if sum(prods[k2]) != 2][0]
                    Hq = [prods[k2] for k2 in rP if sum(prods[k2]) != 2][0]
                    dP = sympy.Poly(sum(c * x**i for i, c in enumerate(Hp)), x)
                    dQ = sympy.Poly(sum(c * x**i for i, c in enumerate(Hq)), x)
                    bs = sympy.Poly(1 + x**s, x)
                    bk = sympy.Poly(1 + x**k, x)
                    if not (dP.rem(bs).is_zero and dQ.rem(bk).is_zero):
                        oneway.append((pts, s, k))
    print(f"  {len(kept)} primitive supports to exponent {N_atom}, {n_coll} with >= 2 "
          f"atomic factorizations   [{time.time()-t0:.1f}s]")
    for (v, sh, sp), c in sorted(shapes.items()):
        print(f"    {c:6d}  {v} {sh} spectator={sp}")
    print(f"  (2,{n})v(2,{n}) pairs: {n_binpairs}, MIXING among them: {len(mix_rows)}, "
          f"criterion disagreements: {len(disagree)}, shared off the divisible branch "
          f"with a binomial NOT dividing the other block: {len(oneway)}")
    for pts, s, k, cyc, why in mix_rows[:20]:
        print(f"    MIXING s={s} k={k} cycles={cyc} {why} support {pts}")
    if len(mix_rows) > 20:
        print(f"    ... {len(mix_rows) - 20} more mixing rows not printed")
    for row in disagree[:10]:
        print("    DISAGREE", row)
    for row in oneway[:10]:
        print("    ONE-WAY", row)
    return dict(found=len(found), pairs=n_pairs, nonzero=bad, coll=n_coll,
                binpairs=n_binpairs, mix=mix_rows, disagree=disagree, oneway=oneway,
                shapes=shapes)


# ================================================================ S0 controls
def stage0():
    print("\n=== S0  the controls ===")
    x, y = X[0], X[1]
    # (a) the ten-term specimen
    pts = [0, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    atoms = atoms_of_support(pts, x)
    facs, prods = atomic_factorizations_1var(atoms)
    print(f"  (a) specimen {pts}: {len(atoms)} atoms, {len(facs)} atomic factorizations")
    for f in facs:
        print("      ", [supp(prods[k]) for k in f])
    ok_a = len(facs) == 2
    if ok_a:
        verdict, shape, nspec, _, _ = classify_1var(atoms, facs[0], facs[1], prods)
        print(f"      {verdict} {shape} spectators={nspec}")
        ok_a = verdict == "MIXING" and shape == "(2, 5)v(2, 5)" and nspec == 0
    check("S0a: the ten-term specimen counts 2 and reads MIXING (2,5)v(2,5)", ok_a)
    # (b) the plus outline, two variables
    plus = [(1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3),
            (1, 2), (0, 2), (0, 1), (1, 1)]
    P = sympy.expand(sum(x**i * y**j for i, j in plus))
    mons, core = zfactors(P)
    gens = [x, y]
    facs2 = atomic_factorizations(core, gens)
    print(f"  (b) plus outline: core {core}, {len(facs2)} atomic factorizations")
    ok_b = len(facs2) == 2
    if ok_b:
        verdict, shape, nspec, _, _ = classify(core, facs2[0], facs2[1], gens)
        print(f"      {verdict} {shape} spectators={nspec}")
        ok_b = verdict == "SHARED" and shape == "(2, 6)v(2, 6)" and nspec == 0
    check("S0b: the plus outline counts 2 and reads SHARED (2,6)v(2,6)", ok_b)
    # (c) the criterion function
    c1 = criterion(pts, 3, 5)
    hexa = list(range(6)) + list(range(13, 19))   # {0,1}+{0,2,4}+{0,13} = {0,3}+{0,1,2}+{0,13}
    c2 = criterion(hexa, 1, 3)
    rect = sorted({0, 3, 5, 8} | {1, 4, 6, 9} | {13, 16, 18, 21})  # {0,3}+{0,5}+{0,1,13}
    c3 = criterion(rect, 3, 5)
    print(f"  (c) criterion: specimen {c1}; cycle-lemma object {c2}; rectangles {c3}")
    check("S0c: the criterion reads MIXING at the specimen and SHARED at both line controls",
          c1[0] == "MIXING" and c2[0] == "SHARED" and c3[0] == "SHARED")


def main():
    t0 = time.time()
    stages = os.environ.get("M26_STAGES", "012")
    if "0" in stages:
        stage0()
        if not all(ok for _, ok in CHECKS):
            print("\nK0: a control failed; nothing below is read.")
    if "1" in stages:
        r = census(6, N_CYCLES, N_ATOMIC, "S1 twelve terms")
        check("S1/PR1: off the divisible branch every twelve-term cycle has closing sums zero",
              not r["nonzero"])
        check("S1/PR1: (2,6)v(2,6) pairs exist and every one reads SHARED",
              r["binpairs"] > 0 and not r["mix"])
        check("S1/PR1: the criterion agrees at every (2,6)v(2,6) pair, both binomials dividing across",
              not r["disagree"] and not r["oneway"])
    if "2" in stages:
        r5 = census(5, N_ATOMIC, N_ATOMIC, "S2 ten terms")
        check("S2/PR2: mixing (2,5)v(2,5) pairs exist at ten terms", len(r5["mix"]) > 0)
        check("S2/PR2: the criterion agrees at every (2,5)v(2,5) pair",
              not r5["disagree"] and not r5["oneway"])
        r7 = census(7, N_SEVEN, N_SEVEN, "S2 fourteen terms")
        check("S2/PR2: the criterion agrees at every (2,7)v(2,7) pair",
              not r7["disagree"] and not r7["oneway"])
    print(f"\n=== {sum(ok for _, ok in CHECKS)}/{len(CHECKS)} checks passed, "
          f"{time.time()-t0:.1f}s ===")
    if not all(ok for _, ok in CHECKS):
        sys.exit(1)


if __name__ == "__main__":
    main()
