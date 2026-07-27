"""
COUPLING ORDER AS GEOMETRY -- two orders, two completions.

THE TARGET. Two orders live on a rung and the probe
separates them. (1) The TIME-ORDER: the ring cycle 0,1,2,... read along
the torus diagonal flow -- the canonical translation-invariant cyclic
order, described in explore_organizing_relations.py as "exactly what no channel sees" (Z/n carries phi(n)
invariant cyclic orders; unit multiplication permutes them
transitively). (2) The COUPLING ORDER: the empirical convergence order
of CRT-LM channels -- mod 2 first, then 3, 5, ... (pattern, never
violated across 5 architectures, in an engineering line no longer
pursued). The probe question:
what is each order made of, and what geometry does "distance from
convergence order" actually generate?

Survey anchors (standard material, named so nothing here poses as new):
cyclically ordered groups (Rieger 1946-48; Swierczkowski 1959 embedding
theorem: cyclic orders come from circle embeddings), Poincare rotation
numbers / rotation vectors (rational rotation = periodic orbit; the
diagonal flow is rotation by (1/p_1, ..., 1/p_k) on T^k), Bertrand's
postulate (p_{i+1} < 2 p_i -- powers the uniqueness in II), the adelic
fractional-part identity (x - sum_p {x}_p in Z for x in Q; the
partial-fraction escape is its restriction to denominator N), cutting sequences / Christoffel words
(crossing patterns of rational slopes are balanced two-letter words),
the profinite metric / product topology on Pi_p F_p (the native limit
topology). Ours is the tower-side composition: which
completion each order belongs to, what each costs per channel, and
what the convergence order's geometry is.

PREDICTIONS (stated before computing, per protocol):
  P1 (angle decomposition): the angle of n in the canonical cycle is
     n/N = sum_p (n_p w_p mod p)/p  (mod 1), w_p = (N/p)^{-1} mod p --
     channel-local summands, exact at every element (the adelic
     identity at the rung). Under generator t the same holds with
     t^{-1}-twisted weights, and t |-> (w_p * (t^{-1} mod p))_p is a
     bijection onto all nonzero weight tuples: the phi(N) invariant
     cyclic orders ARE the phi(N) weight systems of the partial-fraction
     escape.
  P2 (rotation vectors): cycle t advances channel p by (t mod p)/p per
     step; t = 1 is the UNIQUE generator whose speeds decrease in
     modulus order (= the coupling order) -- forced by the 2-channel
     anchor plus Bertrand's postulate -- and uniqueness FAILS on a
     designed tower with a doubled prime gap (expect witness {3,7}).
  P3 (hiding, relation-side): knowing the channels in S (modulus M =
     prod S) pins the cycle position to a uniform N/M-point ladder;
     the fraction of distinct triples whose cyclic orientation is
     determined is < 1 for every proper S and shrinks as M shrinks;
     a single channel determines (almost) nothing.
  P4 (the skeleton): channel p's zero crossings sit at multiples of p
     in EVERY cycle t (the sieve word is the t-invariant skeleton);
     the phase braid between crossings separates all phi(N) orders;
     two-channel crossing words are balanced (Christoffel).
  P5 (time = the deleted place): elapsed time between x and y along
     the canonical cycle, symmetrized, IS circular size |x-y|; the
     thresholded time-distance relation fails the conjunctive test
     maximally (it inherits the whole size wall).
  P6 (the coupling metric): ordering channels by the coupling order
     and reading agreement depth (d = 1/p_m# after m agreeing
     channels) is an ultrametric whose balls are exactly the cosets
     of the tower ideals (p_m#) -- the finite-rung profinite metric.
     The geometry the convergence order generates is the KEPT
     topology, not the torus dress: the two orders are the
     two completions.

Findings preview (full statements at the bottom):
  1. THE ANGLE IS A SUM OF CHANNEL PHASES (rule): adelic identity at
     the rung; cyclic orders = weight systems, bijectively.
  2. THE COUPLING ORDER PICKS THE CANONICAL CYCLE (criterion,
     proved): t = 1 is the unique speed-monotone generator iff 2 is in
     the set and no gap doubles (p_{i+1} < 2 p_i); primorial rungs
     pass both legs (anchor by construction, gaps by Bertrand);
     {3,7} violates both.
  3. THE HIDING IS TOTAL (rule, proved for every cyclic group
     Z/N and every proper divisor M): no proper subset determines
     the orientation of ANY distinct triple.
  4. THE SIEVE WORD IS THE INVARIANT SKELETON (rule + classical):
     zeros are t-invariant; the braid separates; pairs are balanced.
  5. TIME IS THE DELETED PLACE (rule): elapsed time = circular size;
     thresholded, it walks BOTH failure modes (explore_organizing_relations.py)
     as the radius grows (finer than P5 predicted).
  6. CONVERGENCE-ORDER DISTANCE = THE PROFINITE METRIC (rule): balls
     are the tower ideals; the filtration IS the tower.

THE PROOF (added in a later run, closing the total-hiding hook and
the doubled-gap knob it sat next to).
  FINDING 2 -> CRITERION (proved, all finite prime sets S): t = 1 is
  the unique speed-monotone generator iff 2 in S and p_{i+1} < 2 p_i
  throughout. (<=) a unit t has t = 1 mod 2, anchoring speed 1/2;
  inductively t = 1 mod p_i forces t mod p_{i+1} < p_{i+1}/p_i < 2,
  so t = 1 mod p_{i+1}; hence t = 1. (=>) two witness families: with
  no 2-anchor, t = (2,1,...,1) has speeds 2/p_1 > 1/p_2 > ... (first
  step needs only 2 p_2 > p_1); at a doubled gap after p_j,
  t = (1,..,1,2,1,..,1) has 1/p_j > 2/p_{j+1} (the gap) and
  2/p_{j+1} > 1/p_{j+2}. Equal speeds are impossible between
  distinct prime channels (a/p = b/q cross-multiplies to aq = bp,
  so q | b with 1 <= b < q), so monotone = strict for free. The
  primorial rungs pass both legs: the 2-anchor by construction,
  the gap leg by Bertrand's postulate. Mechanical sweep below
  (section II): ALL prime subsets of the first 10 primes with
  N <= 40000 (439 sets, 431 failing; the 8 passing include the
  non-prefixes {2,3,5,7,13} and {2,3,5,7,11,17} -- the criterion is
  gap-shaped, not prefix-shaped), exhaustive count == 1 iff
  criterion, plus the witness re-verified on every failing set.
  FINDING 3 -> RULE, PROVED for every cyclic group Z/N and EVERY
  proper divisor M | N (primality, squarefree-ness, the tower: all
  unused). Reduction: orientation is translation-invariant, and
  translating a completion (x0+iM, y0+jM, z0+lM) by its base point
  maps the class onto {(0, beta+jM, gamma+lM)} with every (j,l) hit
  equally; btw(0,y,z) is then y < z as integers in (0,N). Extremes:
  the ladder of beta contains min Y <= M and max Y >= (c-1)M
  (c = N/M >= 2), likewise gamma; so (min Y, max Z) gives y < z and
  (max Y, min Z) gives y > z, both strict and distinct -- UNLESS
  min Y = max Z = M, which forces beta = gamma = 0 and c = 2: the
  antipodal-diagonal class, whose ladders are both {M} and which
  contains no distinct triple at all. Every nonempty class shows
  both orientations: determined fraction exactly 0. Mechanical sweep
  below (section III): ground-truth orientation enumeration over all
  N <= 72 x every proper divisor including 1 (252 pairs,
  non-squarefree N included), empty class iff antipodal diagonal,
  extreme-pair witnesses valid everywhere.

Run: python prime/code/explore_coupling_order.py   (~2-3 s, tiny memory)
"""

import time
from fractions import Fraction
from itertools import combinations
from math import gcd

T0 = time.perf_counter()

# ---------------------------------------------------------------- helpers

def primorial(primes):
    N = 1
    for p in primes:
        N *= p
    return N

def units(N):
    return [t for t in range(1, N) if gcd(t, N) == 1]

def crt_weights(primes, N):
    """w_p = (N/p)^{-1} mod p for each p."""
    return {p: pow(N // p, -1, p) for p in primes}

def section(title):
    print()
    print("=" * 68)
    print(title)
    print("=" * 68)

PASS = []
def report(label, ok, detail=""):
    PASS.append((label, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f" -- {detail}" if detail else ""))

# ---------------------------------------------------------------- I

section("I. THE ANGLE DECOMPOSITION (adelic identity at the rung)")

# P1a: n/N = sum_p (n_p w_p mod p)/p (mod 1), exhaustive at Z/210.
primes4 = [2, 3, 5, 7]
N4 = primorial(primes4)            # 210
w4 = crt_weights(primes4, N4)
ok = all(
    (sum(Fraction((n % p) * w4[p] % p, p) for p in primes4)
     - Fraction(n, N4)).denominator == 1
    for n in range(N4)
)
report(f"angle = sum of channel phases, exhaustive Z/{N4}", ok,
       "n/N == sum (n_p w_p mod p)/p  (mod 1)")

# Same at RAD, sampled (every 101st element, exact fractions).
primes7 = [2, 3, 5, 7, 11, 13, 17]
N7 = primorial(primes7)            # 510510
w7 = crt_weights(primes7, N7)
ok = all(
    (sum(Fraction((n % p) * w7[p] % p, p) for p in primes7)
     - Fraction(n, N7)).denominator == 1
    for n in range(0, N7, 101)
)
report(f"same at RAD Z/{N7}, sampled stride 101", ok)

# P1b: t-twisted weights at Z/30, exhaustive over all units;
# the map t -> weight system is a bijection onto nonzero tuples.
primes3 = [2, 3, 5]
N3 = primorial(primes3)            # 30
w3 = crt_weights(primes3, N3)
U3 = units(N3)
ok_twist = True
weight_systems = set()
for t in U3:
    tinv = pow(t, -1, N3)
    wt = {p: w3[p] * (tinv % p) % p for p in primes3}
    weight_systems.add(tuple(wt[p] for p in primes3))
    for n in range(N3):
        s = n * tinv % N3          # position of n in cycle (0, t, 2t, ...)
        lhs = sum(Fraction((n % p) * wt[p] % p, p) for p in primes3)
        if (lhs - Fraction(s, N3)).denominator != 1:
            ok_twist = False
report(f"t-twisted decomposition, exhaustive Z/{N3} x {len(U3)} units",
       ok_twist, "position s_t(n)/N = sum (n_p w_p^t mod p)/p")
all_nonzero = {(a, b, c) for a in range(1, 2) for b in range(1, 3)
               for c in range(1, 5)}
report("cyclic orders <-> weight systems bijection",
       weight_systems == all_nonzero,
       f"{len(weight_systems)} weight systems = phi({N3}) = {len(U3)}")

# ---------------------------------------------------------------- II

section("II. ROTATION VECTORS: THE COUPLING ORDER PICKS t = 1")

# Cycle t advances channel p by (t mod p)/p per step. Speed-monotone:
# (t mod p_1)/p_1 > (t mod p_2)/p_2 > ... (strict, coupling order).
def speed_monotone(t, primes):
    return all((t % q) * p < (t % p) * q          # (t%q)/q < (t%p)/p
               for p, q in zip(primes, primes[1:]))

for primes in ([2, 3, 5], [2, 3, 5, 7], [2, 3, 5, 7, 11],
               [2, 3, 5, 7, 11, 13], primes7):
    N = primorial(primes)
    mono = [t for t in range(1, N) if gcd(t, N) == 1
            and speed_monotone(t, primes)]
    report(f"k={len(primes)} (N={N}): speed-monotone generators = {{1}}",
           mono == [1], f"checked all phi(N)={len(units(N)) if N <= 30030 else 'phi'} units"
           if N <= 30030 else "checked all units")

# Designed-tower contrast: {3,7} has a doubled gap (7 > 2*3).
dprimes = [3, 7]
dN = primorial(dprimes)
dmono = [t for t in range(1, dN) if gcd(t, dN) == 1
         and speed_monotone(t, dprimes)]
report("designed tower {3,7}: uniqueness FAILS", dmono != [1],
       f"speed-monotone generators: {dmono}")

# THE CRITERION (proved -- docstring carries the proof). t = 1 is
# the unique speed-monotone generator iff 2 in S and no doubled gap
# (p_{i+1} < 2 p_i throughout). Mechanical re-verification: exhaustive
# count over all units vs the criterion, every prime subset of the
# first 10 primes with N <= 40000; on every failing set, the proof's
# necessity witness is rebuilt by CRT and re-checked.
def crt_build(primes, residues):
    N = primorial(primes)
    return sum(r * (N // p) * pow(N // p, -1, p)
               for p, r in zip(primes, residues)) % N

pool = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
checked = mismatches = failing = 0
passing_sets = []
wit_ok = True
for r in range(1, len(pool) + 1):
    for S in combinations(pool, r):
        S = list(S)
        N = primorial(S)
        if N > 40000:
            continue
        count = sum(1 for t in range(1, N)
                    if gcd(t, N) == 1 and speed_monotone(t, S))
        crit = (S[0] == 2) and all(q < 2 * p for p, q in zip(S, S[1:]))
        if (count == 1) != crit:
            mismatches += 1
        if crit:
            passing_sets.append(tuple(S))
        if not crit:
            failing += 1
            if S[0] != 2:                  # no anchor: (2, 1, ..., 1)
                res = [2] + [1] * (len(S) - 1)
            else:                          # 2 at the first doubled gap
                j = next(i for i in range(len(S) - 1)
                         if S[i + 1] > 2 * S[i])
                res = [1] * len(S)
                res[j + 1] = 2
            t = crt_build(S, res)
            if t == 1 or gcd(t, N) != 1 or not speed_monotone(t, S):
                wit_ok = False
        checked += 1
report(f"criterion: unique iff 2 in S and no doubled gap ({checked} sets)",
       mismatches == 0,
       "ALL prime subsets of the first 10 primes with N <= 40000")
report(f"necessity witnesses speed-monotone on all {failing} failing sets",
       wit_ok, "(2,1,...,1) without the anchor; 2 at the first doubled gap")
print(f"    passing sets ({len(passing_sets)}): "
      + ", ".join("{" + ",".join(map(str, S)) + "}" for S in passing_sets))

# ---------------------------------------------------------------- III

section("III. THE LADDER HIDES ORIENTATION (quantitative, relation-side)")

# Knowing channels S (modulus M) pins position to the ladder n_S + j*M.
# Orientation btw(a,b,c) = ((b-a) mod N) < ((c-a) mod N). A triple's
# orientation is DETERMINED by S iff all distinct completions agree.
# Translation invariance: class (m_a,m_b,m_c) == class (0, beta, gamma).

def determined_fraction(primes, S):
    N = primorial(primes)
    M = primorial(S)
    c = N // M                     # ladder length
    total_distinct = N * (N - 1) * (N - 2)
    det_weight = 0
    sanity = 0
    for beta in range(M):
        for gamma in range(M):
            # distinct-completion count for class (0, beta, gamma)
            D = c ** 3
            D -= (beta == 0) * c * c
            D -= (gamma == 0) * c * c
            D -= (beta == gamma) * c * c
            D += 2 * (beta == 0 and gamma == 0) * c
            sanity += M * D
            if D == 0:
                continue
            seen = set()
            for i in range(c):
                x = i * M
                for j in range(c):
                    y = beta + j * M
                    if y == x:
                        continue
                    dyx = (y - x) % N
                    for l in range(c):
                        z = gamma + l * M
                        if z == x or z == y:
                            continue
                        seen.add(dyx < (z - x) % N)
                        if len(seen) == 2:
                            break
                    if len(seen) == 2:
                        break
                if len(seen) == 2:
                    break
            if len(seen) == 1:
                det_weight += M * D
    assert sanity == total_distinct, "class accounting broken"
    return det_weight / total_distinct

print(f"\n  Z/30, all proper nonempty channel subsets:")
fr30 = {}
for r in (1, 2):
    for S in combinations(primes3, r):
        fr30[S] = determined_fraction(primes3, list(S))
        print(f"    known {str(S):10s} (M={primorial(S):3d}): "
              f"determined fraction = {fr30[S]:.4f}")

print(f"\n  Z/210, all proper nonempty channel subsets:")
fr210 = {}
for r in (1, 2, 3):
    for S in combinations(primes4, r):
        fr210[S] = determined_fraction(primes4, list(S))
        print(f"    known {str(S):12s} (M={primorial(S):3d}): "
              f"determined fraction = {fr210[S]:.4f}")

# Control: the machinery returns 1.0 when ALL channels are known.
ctl30 = determined_fraction(primes3, primes3)
ctl210 = determined_fraction(primes4, primes4)
report("control: full channel set determines every triple",
       ctl30 == 1.0 and ctl210 == 1.0,
       f"Z/30 {ctl30}, Z/210 {ctl210}")

total = all(f == 0.0 for f in list(fr30.values()) + list(fr210.values()))
report("TOTAL hiding: every proper subset determines NOTHING", total,
       "stronger than predicted (P3 said < 1, shrinking)")

# Range extension: the largest proper subset at Z/2310 (dark channel 2).
primes5 = [2, 3, 5, 7, 11]
fr2310 = determined_fraction(primes5, [3, 5, 7, 11])
report("extends to Z/2310, known (3,5,7,11), M=1155", fr2310 == 0.0,
       f"determined fraction = {fr2310:.4f}")

# THE PROOF (docstring carries it), re-verified mechanically.
# Reduced class (beta, gamma) mod M: triples (0, y, z) with y, z in
# (0, N), y = beta and z = gamma mod M, y != z. Ground truth: every
# nonempty class shows BOTH orientations (y < z and y > z), and the
# only empty class is the antipodal diagonal (beta = gamma = 0 at
# c = 2). Scope: ALL N and ALL proper divisors M -- non-squarefree N
# included, since the proof never uses the tower.
def hiding_ground_truth(N, M):
    c = N // M
    for beta in range(M):
        for gamma in range(M):
            seen = set()
            for j in range(c):
                y = beta + j * M
                if y == 0:
                    continue
                for l in range(c):
                    z = gamma + l * M
                    if z == 0 or z == y:
                        continue
                    seen.add(y < z)
            antipodal = (beta == 0 and gamma == 0 and c == 2)
            if antipodal != (len(seen) == 0):
                return False
            if not antipodal and len(seen) != 2:
                return False
    return True

# The proof's extreme-pair witnesses: min Y <= M and max Y >= (c-1)M
# in every ladder, so (min Y, max Z) and (max Y, min Z) realize the
# two orientations in every nonempty class.
def witness_pairs_valid(N, M):
    c = N // M
    for beta in range(M):
        for gamma in range(M):
            if beta == 0 and gamma == 0 and c == 2:
                continue
            min_y = beta if beta else M
            max_y = beta + (c - 1) * M if beta else (c - 1) * M
            min_z = gamma if gamma else M
            max_z = gamma + (c - 1) * M if gamma else (c - 1) * M
            if not (0 < min_y < max_z < N and 0 < min_z < max_y < N):
                return False
    return True

pairs_swept = 0
gt_ok = wit_ok2 = True
for N in range(4, 73):
    for M in range(1, N):          # 1 is a proper divisor too (empty set)
        if N % M:
            continue
        pairs_swept += 1
        gt_ok = gt_ok and hiding_ground_truth(N, M)
        wit_ok2 = wit_ok2 and witness_pairs_valid(N, M)
report(f"PROOF ground truth: all N <= 72 x every proper divisor "
       f"({pairs_swept} pairs)", gt_ok,
       "both orientations in every nonempty class; empty iff "
       "antipodal diagonal")
report("proof witnesses (extreme pairs) valid everywhere", wit_ok2,
       "min Y <= M <= (c-1)M <= max Y in every ladder")

# ---------------------------------------------------------------- IV

section("IV. THE SKELETON: SIEVE WORD INVARIANT, BRAID SEPARATES")

# Zeros of channel p along cycle t: position s has element t*s; its
# channel-p residue is 0 iff p | t*s iff p | s (t a unit). t-invariant.
ok = True
for t in U3:
    for p in primes3:
        zeros = {s for s in range(N3) if (t * s) % p == 0}
        if zeros != set(range(0, N3, p)):
            ok = False
report("zero crossings = multiples of p in EVERY cycle t (Z/30)", ok,
       "the sieve word is the t-invariant skeleton")

# The phase braid -- the RANKING of channels by phase at each step,
# ties grouped, NO residue values (residues would carry the whole
# orbit and make separation trivial) -- separates all phi(N) orders.
def braid_word(t, primes, N):
    word = []
    for s in range(N):
        n = t * s % N
        groups = {}
        for p in primes:
            groups.setdefault(Fraction(n % p, p), []).append(p)
        word.append(tuple(tuple(groups[ph]) for ph in sorted(groups)))
    return tuple(word)

words = {braid_word(t, primes3, N3) for t in U3}
report("phase braid separates all phi(30) = 8 cyclic orders",
       len(words) == len(U3), f"{len(words)} distinct braid words")

# Two-channel crossing words are balanced (Christoffel): word over one
# period, 'a' at multiples of p, 'b' at multiples of q, corner 'ab'.
def crossing_word(p, q):
    events = []
    for s in range(1, p * q + 1):
        if s % p == 0:
            events.append((s, 'a'))
        if s % q == 0:
            events.append((s, 'b'))
    return ''.join(letter for s, letter in sorted(events))

def is_balanced(word):
    n = len(word)
    doubled = word + word
    for length in range(1, n):
        counts = {doubled[i:i + length].count('a') for i in range(n)}
        if max(counts) - min(counts) > 1:
            return False
    return True

pairs = [(2, 3), (3, 5), (5, 7), (2, 17), (7, 11), (13, 17)]
ok = all(is_balanced(crossing_word(p, q)) for p, q in pairs)
report("two-channel crossing words balanced (Christoffel)", ok,
       f"pairs {pairs}")

# ---------------------------------------------------------------- V

section("V. TIME IS THE DELETED PLACE")

# Elapsed time x -> y along the canonical cycle is (y-x) mod N (one
# step = +1); symmetrized it is circular size |x-y|_circ exactly.
ok = all(min((y - x) % N3, (x - y) % N3)
         == min(abs(x - y), N3 - abs(x - y))
         for x in range(N3) for y in range(N3))
report("symmetrized elapsed time = circular size |x-y| (Z/30)", ok)

# Thresholded time-distance R_d = {(x,y): |x-y|_circ <= d} fails the
# conjunctive test at every 1 <= d < N/2, but the failure MODE depends
# on the threshold radius: once 2d+1 >= p_k the difference set covers
# every channel (projections saturate -- maximal failure, the order
# relation's own failure mode per explore_organizing_relations.py);
# below that the largest channels keep proper projections (that
# script's grading failure mode). At d = 0 the relation is equality:
# conjunctive.
def threshold_modes(primes, N, d_values):
    pk = primes[-1]
    modes = {}
    for d in d_values:
        R = {(x, y) for x in range(N) for y in range(N)
             if min((y - x) % N, (x - y) % N) <= d}
        projs = {p: {(x % p, y % p) for x, y in R} for p in primes}
        conj = {(x, y) for x in range(N) for y in range(N)
                if all((x % p, y % p) in projs[p] for p in primes)}
        saturated = all(len(projs[p]) == p * p for p in primes)
        if conj == R:
            mode = "conjunctive"
        elif saturated:
            mode = "maximal"
        else:
            mode = "proper"
        expected = ("conjunctive" if d == 0
                    else "maximal" if 2 * d + 1 >= pk else "proper")
        modes[d] = (mode, expected)
    return modes

modes30 = threshold_modes(primes3, N3, range(N3 // 2))
print("  Z/30 threshold modes (d: found / expected by 2d+1 vs p_k):")
for d, (mode, expected) in modes30.items():
    print(f"    d={d:2d}: {mode:12s} (expected {expected})")
ok30 = all(mode == expected for mode, expected in modes30.values())
report("failure mode = radius vs largest channel, exhaustive d (Z/30)",
       ok30, "d=0 conjunctive (equality); 2d+1 >= p_k maximal; below proper")

# Boundary at a second rung: Z/210 (p_k = 7 -> proper at d = 1, 2;
# maximal from d = 3); spot value d = 104 at the far end.
modes210 = threshold_modes(primes4, N4, list(range(11)) + [104])
ok210 = all(mode == expected for mode, expected in modes210.values())
report("same mode boundary at Z/210, d = 0..10 + 104", ok210,
       "proper at d = 1, 2; maximal from d = 3 (2d+1 >= 7)")

# ---------------------------------------------------------------- VI

section("VI. CONVERGENCE-ORDER DISTANCE = THE PROFINITE METRIC")

# Coupling metric at Z/210: depth(x,y) = # leading channels (coupling
# order) agreeing; d(x,y) = 1/p_depth#. Ultrametric, exhaustive via
# translation invariance: depth is a function of the difference.
prims = [1, 2, 6, 30, 210]         # p_m# for m = 0..4
def depth_of(diff):
    m = 0
    while m < 4 and diff % prims[m + 1] == 0:
        m += 1
    return m

depth = [depth_of(dd) for dd in range(N4)]
ok = all(depth[(d1 + d2) % N4] >= min(depth[d1], depth[d2])
         for d1 in range(N4) for d2 in range(N4))
report("ultrametric inequality, exhaustive differences Z/210", ok,
       "depth(x,z) >= min(depth(x,y), depth(y,z))")

# Balls = cosets of the tower ideals (p_m#).
ok = True
for m in range(5):
    ball0 = {y for y in range(N4) if depth_of(y) >= m}
    coset = set(range(0, N4, prims[m]))
    if ball0 != coset:
        ok = False
report("balls around 0 = the tower ideals (p_m#), m = 0..4", ok,
       "ball tree = the tower filtration; translation gives all balls")

# The metric needs the channel ORDER; a different order is a different
# metric (witness), but every order's ball tree is a filtration by
# ideals -- the coupling order's filtration is the primorial tower.
x, y = 0, 105                      # 105 = 3*5*7: agree mod 3,5,7, differ mod 2
d_coupling = Fraction(1, prims[depth_of(105)])
rev = [7, 5, 3, 2]
m_rev = 0
rprims = [1, 7, 35, 105, 210]
while m_rev < 4 and 105 % rprims[m_rev + 1] == 0:
    m_rev += 1
d_reversed = Fraction(1, rprims[m_rev])
report("channel order changes the metric (witness x=0, y=105)",
       d_coupling != d_reversed,
       f"coupling d = {d_coupling}, reversed d = {d_reversed}")

# ---------------------------------------------------------------- findings

section("FINDINGS (tier-labeled)")

print("""
1. THE ANGLE IS A SUM OF CHANNEL PHASES (rule). The canonical cycle
   embeds Z/N in the circle at angle n/N (Swierczkowski: cyclic order
   = circle embedding), and that angle decomposes as the mod-1 sum of
   k CHANNEL-LOCAL phases (n_p w_p mod p)/p -- the adelic identity
   x - sum_p {x}_p in Z restricted to denominator N, i.e. the
   partial-fraction escape read order-side (exhaustive Z/210, sampled
   RAD; twisted form exhaustive Z/30 x all units). The phi(N)
   invariant cyclic orders are EXACTLY the phi(N) weight systems of
   the escape (bijection verified): choosing a cyclic order IS
   choosing a unit weight per channel. The time-order is made of
   per-channel phases combined by mod-1 ADDITION -- the one
   cross-channel shape the conjunctive test (explore_organizing_relations.py) cannot express.

2. THE COUPLING ORDER PICKS THE CANONICAL CYCLE (criterion, proved).
   Cycle t rotates channel p at speed (t mod p)/p. t = 1 is
   the UNIQUE speed-monotone generator iff 2 is in the set and no
   gap doubles (p_{i+1} < 2 p_i throughout): the 2-channel anchors
   at 1/2 and the chain inequality forces t = 1 mod every p; absent
   the anchor t = (2,1,...,1) is speed-monotone, and at a doubled
   gap so is the 2-at-the-gap tuple (proof in the docstring;
   mechanical sweep over ALL prime subsets of the first 10 primes
   with N <= 40000, witnesses re-verified on every failing set).
   Primorial rungs pass both legs -- the 2-anchor by construction,
   the gap leg by Bertrand's postulate -- so at every rung the
   empirical convergence order singles out the sieve's own cycle
   among all phi(N) invariant cyclic orders, while {3,7} (no anchor
   AND a doubled gap) has six speed-monotone generators.

3. THE HIDING IS TOTAL (rule, proved for every cyclic group Z/N
   and EVERY proper divisor M -- primality, squarefree-ness, the
   tower all unused; STRONGER than predicted P3, which said "< 1 and
   shrinking"). Knowing the channels in S pins a position to a
   uniform N/M-point ladder (M = prod S), and for EVERY class of
   distinct triples both orientations occur among the ladder
   completions: the determined fraction is exactly 0. Proof: reduce
   the base point to 0 (orientation = integer comparison on (0,N));
   every ladder contains an element <= M and one >= (c-1)M, and the
   extreme pairs realize both orientations -- the single empty class
   is the antipodal diagonal (beta = gamma = 0 at c = 2). Ground
   truth re-swept: all N <= 72 x every proper divisor; rung-scale
   record exhaustive Z/30, Z/210, Z/2310 at M = 1155. Control: the
   full channel set determines every triple (fraction 1). One bit of
   cyclic orientation costs the entire complement -- the hiding
   lemma, relation-side, in its sharpest form, now for all rungs and
   all designed towers at once.

4. THE SIEVE WORD IS THE INVARIANT SKELETON (rule + classical).
   Channel p crosses zero at multiples of p in EVERY cycle t (t a
   unit: p | ts iff p | s) -- the crossing pattern of the diagonal
   flow is the Eratosthenes pattern, and it is the t-INVARIANT
   skeleton shared by all phi(N) cyclic orders. What separates them
   is only the phase braid between crossings -- the RANKING of
   channels by phase, ties grouped, residue values withheld so the
   test cannot pass on orbit data alone (8/8 distinct at Z/30).
   Two-channel crossing words are balanced -- Christoffel words of
   slope p/q, the classical cutting sequence (verified 6 pairs); the
   full k-channel word is the cutting sequence of the torus diagonal.

5. TIME IS THE DELETED PLACE (rule). Elapsed time along the canonical
   cycle, symmetrized, IS circular size |x-y| -- the diagonal flow's
   clock is the archimedean metric reborn (the dynamical dress on
   the tower's own geometric reading of that metric). Thresholded
   time-distance R_d
   fails the conjunctive test at every 1 <= d < N/2, and the failure
   MODE is set by the radius against the largest channel (exhaustive
   in d at Z/30): once 2d+1 >= p_k every projection saturates (the
   order relation's own failure mode, explore_organizing_relations.py,
   maximal); below that the largest channels keep
   proper projections (that script's grading failure mode); at d = 0 the relation
   is equality, conjunctive. The wall is the same wall, and the
   threshold radius walks it through both failure modes --
   finer structure than prediction P5, which said maximal across
   the board.

6. CONVERGENCE-ORDER DISTANCE = THE PROFINITE METRIC (rule). Reading
   agreement depth along the coupling order gives an ultrametric
   (exhaustive Z/210) whose balls are exactly the cosets of the tower
   ideals (p_m#): the ball tree IS the tower filtration, and its
   limit topology is the native profinite topology. The channel
   order changes the METRIC (witness) but every order filters by
   ideals; the coupling order's filtration is the primorial
   trajectory itself.

CAPSTONE -- TWO ORDERS, TWO COMPLETIONS. The probe's two orders are
the two sides of Ostrowski: the TIME-ORDER is the deleted place's
order structure (a circle embedding, channel-additive mod 1,
ladder-hidden from every proper window set, sieve-skeletoned), and
the COUPLING ORDER is not an order on the ring at all -- it is an
order on the CHANNELS, and the geometry it generates is the kept
profinite side: the tower read as a metric. "Distance from
convergence order" is made of agreement depth in the tower
filtration. The empirical training link was later resolved as a
mundane effect (class count plus an alphabet accident,
explore_coupling_mechanism.py, from an engineering line no longer
pursued); everything derived here is exact
and stands on its own.
""")

failed = [label for label, ok in PASS if not ok]
print(f"  {len(PASS) - len(failed)}/{len(PASS)} checks pass"
      + (f"; FAILED: {failed}" if failed else " -- ALL GREEN")
      + f"  ({time.perf_counter() - T0:.1f} s)")
