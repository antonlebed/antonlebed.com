"""
explore_collision_growth.py — learning as collision-driven substrate GROWTH.

THE QUESTION. The reader-descent corpus proves DESTINATION UNIVERSALITY over a
FIXED substrate: a reader adapts to its resource metabolism, never its training
data. This script breaks the fixed-substrate root. Learning is redefined as
GROWTH: when supervised data presents a distinction the current rung cannot
resolve (two inputs the ring maps to the same cell that supervision says
differ — a COLLISION), grow a window. The substrate is no longer chosen once
and held; it grows on the data. Does that make the learned destination
DATA-dependent (the wall dissolves), or does growth re-derive a
stream-independent counter (the wall survives one level up)?

THE ARENA.
  - Inputs: integers, universe U = {0..M-1}.
  - A STREAM is a supervised partition (labeling) of U. A MUST-SEPARATE pair is
    two inputs in different classes.
  - A SUBSTRATE is an ordered set S of distinct primes (the grown window set).
  - S RESOLVES a pair (x, y) iff some p in S has p not dividing (x - y). Because
    the primes are distinct, x == y mod prod(S) iff prod(S) | (x - y); so a pair
    is UNRESOLVED by S iff prod(S) | (x - y).
  - A COLLISION at S is a must-separate pair S does not resolve.

THE DIFFERENCE-SET REDUCTION (method + PR5). Whether S resolves a pair depends
ONLY on the difference (x - y). So a stream's entire separation demand is
carried by its SET OF DIFFERENCES D = { |x - y| : must-separate pair (x, y) }.
The engine reduces every stream to D and grows against it — this is both the
efficient representation and the content of PR5: collision-driven growth is a
greedy hitting-set over D, prime p "hitting" difference d iff p does not divide
d.

THE GROWTH RULE (least-new). On a collision, add the SMALLEST prime not in S
(drawn from the pool = the first P primes) that resolves at least one currently
unresolved difference; iterate to zero collisions or pool exhaustion. This is
the constrained-least-new mechanism of explore_growth_capability.py — the rule
whose "emergent designed tower" grows a demand-shaped window set. Here the
demand is supplied by DATA (which differences supervision requires resolved)
instead of by an algebraic capability.

  The sibling rule greedy-cover ("add the prime resolving the MOST differences")
  picks the LARGEST pool prime first — a large prime rarely divides a random
  difference, so it separates a ~(1 - 1/p) fraction in one move — growing a
  primorial SUFFIX. Both rules are stream-independent on generic streams; this
  script uses least-new because it makes the primorial-prefix vs designed-tower
  contrast the clean content axis and reuses the corpus's proved lemma.

THE AXIS (count vs content). A prime p resolves a generic difference with
probability 1 - 1/p, so on random labelings every prime resolves some difference
and least-new grows the primorial PREFIX 2, 3, 5, 7, ... identically across
streams (the substrate is a stream-independent counter — its DEPTH varies with
the required resolution, its CONTENT does not: COUNT-selection, the wall
survives). When a stream lives on a sublattice U_q = {x == r mod q}, every
difference is divisible by q, so q resolves nothing and least-new SKIPS it — the
designed-tower knob, now driven by data (CONTENT-selection at the SET level).
Whether that set-level content amounts to the DATA picking the destination is
the transfer question.

PREDICTIONS (fixed before the run; adjudicated post-run in the RUN RECORD).
  PR1  (generic COUNT) random labelings over fixed M grow the IDENTICAL set (the
       ensemble's distinct-set count is 1) = the primorial prefix; depth grows
       with M while the set stays a prefix. The KILL-shape fires on the generic
       ensemble.
  PR2  (set content) U_q sublattice streams SKIP q; different-q ensembles grow
       provably different sets.
  PR3  (transfer, the sharp claim) sublattice set-difference does NOT by itself
       force worse cross-transfer (redundant small primes still cover — predict
       cross-residual near 0 for PR2 streams); a real transfer-gap requires an
       engineered UNIQUE-NEED difference (divisible by every pool prime but one).
       So set-difference != destination-dependence; the transfer-gap is the true
       wall-dissolution observable.
  PR4  (myopia, secondary) least-new's grown set is >= the optimal (minimum)
       cover; measure the gap against a brute-force minimum cover on small
       instances (the set-cover myopia, mirroring the growth-capability myopia
       gap). Meaningful only where selection is content-shaped.
  PR5  (descent / subsumption) collision-driven growth IS greedy hitting-set over
       the difference set, prime p hitting difference d iff p does not divide d;
       the count vs content axis is the generic vs structured cover instance;
       this subsumes the growth learner into set-cover and re-derives destination
       universality (generic stream => prefix => depth is a counter).

THE KILL-SHAPE (printed observable). Across the diverse generic ensemble the
grown window set is IDENTICAL (distinct-set count 1, a primorial prefix) =>
destination universality re-derived as a counter; growth does NOT dissolve the
wall. THE SURVIVE-SHAPE: two ensembles grow provably DIFFERENT sets AND
cross-transfer residual > 0 while self-residual = 0 => the data picked the
destination.

POSITIVE CONTROL (run before any verdict is read). (a) resolves() computed as
prod(S) not dividing (x - y) must equal the direct CRT-tuple test (some p in S
with x mod p != y mod p) on every sampled (S, pair). (b) On U = {0..29} with an
all-distinct labeling, least-new must grow EXACTLY {2, 3, 5} (2 kills odd
differences, 3 kills the rest not divisible by 3, 5 kills the difference-6
pairs, and no nonzero difference below 30 is divisible by 30) — any other output
is a harness bug.

FINDINGS (tiers inline; run record below; all sections assert).

1. THE DIFFERENCE-SET REDUCTION (property + rule, proved; S0, S5). Resolution
   depends only on the difference: S resolves (x, y) iff prod(S) does not divide
   (x - y) (property — the CRT-tuple test and the product form agree on 4000
   samples). So collision-driven growth IS greedy hitting-set over the
   difference set D, prime p hitting difference d iff p does not divide d — a
   from-scratch hitting-set greedy reproduces grow_least_new exactly (S5, set
   [2, 3, 5, 7]). The learning-as-growth winner is set-cover. [PR5]

2. THE GENERIC COUNT REGIME -- the wall SURVIVES (observation at scope + the
   all-distinct rule; S1). 24 random labelings over U = 0..209 grow ONE
   identical set, the primorial prefix [2, 3, 5, 7] (distinct-set count 1). For
   all-distinct U = {0..M-1} the prefix is forced (rule): least-new grows
   2, 3, 5, ... and halts once prod(S) exceeds M-1, so depth is 3, 4, 5, 6 at
   M = 30, 210, 2310, 30030, a pure prefix throughout. THE KILL-SHAPE FIRES: the
   grown substrate is stream-INDEPENDENT, its CONTENT a primorial prefix, only
   its DEPTH varying with the required resolution -- destination universality
   re-derived one level up: the substrate is a primorial prefix fixed by
   resolution alone, blind to content (the data sets how FINE, never WHAT).
   Growth does not dissolve the wall on generic data. [PR1]

3. SET-LEVEL CONTENT -- sublattice data skips primes (rule, proved; S2). A
   stream on U_q = {x == 0 mod q} has every difference divisible by q, so q
   resolves nothing and least-new NEVER picks it (rule). The ensembles
   q = 3, 5, 7 grow three different sets ([2, 5, 7, 11], [2, 3, 7, 11],
   [2, 3, 5, 11]) -- the designed-tower knob (skip a prime) is an OUTPUT of data
   structure, the data-driven mirror of explore_growth_capability.py's
   capability-driven emergent designed tower. [PR2]

4. THE FLIP CONDITION -- set-difference is NOT destination-dependence (the sharp
   result, observation at scope; S3). Fully different grown sets transfer
   NEAR-INTACT: S_A (U_3, skips 3) leaves 0 of 125 of stream B's differences
   unresolved; S_B leaves 1 of 209 of A's -- the lone residual is the boundary
   difference d = prod(S_B) = 462, the single value the other cover exactly
   divides. Redundant small primes still cover, so sublattice structure alone
   does not make the destination data-dependent. The TRUE wall-dissolution
   observable is a UNIQUE-NEED difference -- one divisible by every pool prime
   but one (d = 770 = 2*5*7*11, resolvable only by 3): stream B needing it grows
   [3], while stream A on U_3 (which never demands 3) grows [2, 5, 7, 11] and
   leaves B's distinction 1 of 1 UNRESOLVED. THE SURVIVE-SHAPE. The wall
   dissolves only when the data demands a prime no other stream demands -- not
   merely when the data is structured (the lone boundary residual aside). [PR3]

5. THE MYOPIA IS GENERIC (observation at scope; S4). least-new's grown set is
   never below the minimum cover (40/40) and STRICTLY overpays in 40 of 40
   random small instances -- the set-cover myopia is pervasive here, not
   occasional, because smallest-first least-new grabs 2 (odd differences are
   always present) even when a single larger prime covers the whole demand (hand
   instance D = {1, 770}: least-new [2, 3] vs minimum cover [3]). Reaching the
   optimal data-shaped substrate costs lookahead, echoing the growth-capability
   myopia gap. [PR4]

THE VERDICT. The substrate door (this script) and the data door
(explore_prediction_door.py) are both real but open destination-dependence
differently: the data door relaxes
the LOSS to read the future; growth relaxes the SUBSTRATE. At toy scope growth's
verdict is CONTINGENT, and the toy pins the flip condition -- the wall SURVIVES
on generic and merely-sublattice data (the grown substrate is a stream-
independent primorial prefix, depth a counter) and DISSOLVES only when the data
carries UNIQUE-NEED distinctions (a demand no other stream makes). Since the
learner is set-cover (finding 1), the whole dichotomy is the generic-vs-
structured cover-instance distinction. Honest limit: hand-designed, toy scope,
this 12-prime pool and these stream families; the tier is observation for the
regime verdicts and rule for the reduction, the all-distinct prefix, and the
skip-a-sublattice-prime law.

RUN RECORD (python explore_collision_growth.py, ~1 s, trivial memory):
  S0 controls: 4000 samples resolve == product == CRT-tuple; U30 -> [2, 3, 5]
  S1 generic: 24 random labelings -> 1 distinct set [2, 3, 5, 7]; depth 3/4/5/6
     at M = 30/210/2310/30030, all prefixes
  S2 content: U_3/U_5/U_7 -> [2,5,7,11]/[2,3,7,11]/[2,3,5,11], three different
  S3 transfer: sublattice cross 0 of 125 and 1 of 209; unique-need 1 of 1
  S4 myopia: 40/40 least-new >= min cover, 40/40 strict overpay; hand [2,3] vs [3]
  S5 descent: hitting-set greedy == grow_least_new [2, 3, 5, 7]
  TOTAL 8059 checks, exit 0.

ADJUDICATION vs the predictions fixed before the run (git history). PR1, PR2,
PR5 landed exactly -- the sublattice sets matched the hand derivation prime for
prime. PR3 landed with the predicted nuance sharpened:
sublattice cross-transfer is 0 one way but 1 the other (the boundary difference
d = prod(S) = 462, foreseen in the slate as the exact-multiple artifact) --
near-intact, not exactly zero -- and the qualitative claim (set-difference !=
destination-dependence) holds, the unique-need transfer-gap total as predicted.
PR4 landed STRONGER than "occasional": strict overpay in 40 of 40 -- the
smallest-first bias makes myopia generic at this scope, not an exception.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
from math import prod
from itertools import combinations

CHECKS = 0


def check(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ------------------------------------------------------------------ primes

def first_primes(n):
    ps, c = [], 2
    while len(ps) < n:
        if all(c % p for p in ps):
            ps.append(c)
        c += 1
    return ps


POOL = first_primes(12)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


# ------------------------------------------------------- the arena (diffs)

def resolves(S, x, y):
    """S separates (x, y): some prime in S does not divide their difference."""
    d = x - y
    return any(d % p != 0 for p in S)


def unresolved_diffs(S, D):
    """Differences a substrate S fails to separate: prod(S) | d."""
    P = prod(S) if S else 1
    return [d for d in D if d % P == 0]


def grow_least_new(D, pool=POOL):
    """least-new collision-driven growth against a difference set. Ordered."""
    S = []
    D = list(D)
    while True:
        u = unresolved_diffs(S, D)
        if not u:
            return S
        for p in pool:                        # smallest first
            if p in S:
                continue
            if any(d % p != 0 for d in u):    # resolves >= 1 unresolved diff
                S.append(p)
                break
        else:
            return S                           # pool exhausted


def diffs_of(labeling):
    """The set of must-separate differences of a labeling {input: class}."""
    xs = sorted(labeling)
    D = set()
    for a, b in combinations(xs, 2):
        if labeling[a] != labeling[b]:
            D.add(b - a)
    return D


def diffs_all_distinct_range(M):
    """All-distinct labeling of {0..M-1}: every difference 1..M-1 occurs."""
    return set(range(1, M))


def sublattice_diffs(M, q, r=0):
    """All-distinct labeling on {x in 0..M-1 : x == r mod q}: diffs = q*Z."""
    U = [x for x in range(M) if x % q == r]
    return {b - a for a, b in combinations(U, 2)}


def random_labeling(M, classes, rng):
    return {x: rng.randrange(classes) for x in range(M)}


# --------------------------------------------------------- S0: controls

def s0_controls():
    print("S0: positive controls")
    rng = random.Random(20250311)
    for _ in range(4000):
        k = rng.randrange(1, 6)
        S = rng.sample(POOL, k)
        x, y = rng.randrange(2000), rng.randrange(2000)
        prod_form = (x - y) % prod(S) != 0
        tuple_form = any(x % p != y % p for p in S)
        check(resolves(S, x, y) == prod_form, "resolve != product form")
        check(resolves(S, x, y) == tuple_form, "resolve != CRT-tuple test")
    print("  resolve() == product form == CRT-tuple test (4000 samples)")
    D = diffs_all_distinct_range(30)
    S = grow_least_new(D)
    check(S == [2, 3, 5], f"U30 all-distinct grew {S}, expected [2,3,5]")
    check(not unresolved_diffs(S, D), "S=[2,3,5] leaves a collision")
    print(f"  U=0..29 all-distinct -> grew {S} (prod {prod(S)}), zero residual")


# -------------------------------------------------- S1: the generic COUNT

def s1_generic(K=24, M=210, classes=8):
    print("S1: generic ensemble -- the COUNT regime (PR1)")
    rng = random.Random(11)
    grown = [tuple(grow_least_new(diffs_of(random_labeling(M, classes, rng))))
             for _ in range(K)]
    distinct = set(grown)
    print(f"  {K} random labelings over U=0..{M-1}, {classes} classes")
    print(f"  distinct grown sets: {len(distinct)}  ->  {sorted(distinct)}")
    check(len(distinct) == 1, "generic ensemble did not grow one identical set")
    the_set = list(distinct.pop())
    check(the_set == POOL[:len(the_set)], "grown set is not a primorial prefix")
    print(f"  KILL-SHAPE: identical set {the_set}, the primorial prefix"
          f" (prod {prod(the_set)})")
    print("  depth vs M (all-distinct labeling):")
    for M2 in (30, 210, 2310, 30030):
        S = grow_least_new(diffs_all_distinct_range(M2))
        check(S == POOL[:len(S)], f"M={M2} not a prefix")
        print(f"    M={M2:>6}: depth {len(S)}  set {S}")
    return the_set


# --------------------------------------------------- S2: the set content

def s2_content(M=630):
    print("S2: sublattice streams -- CONTENT at the SET level (PR2)")
    sets = {}
    for q in (3, 5, 7):
        S = grow_least_new(sublattice_diffs(M, q))
        sets[q] = S
        check(q not in S, f"U_{q} stream did not skip {q}")
        print(f"  U_{q} = {{x == 0 mod {q}}} -> grew {S}  (skips {q})")
    check(len({tuple(v) for v in sets.values()}) == 3,
          "sublattice streams did not grow three different sets")
    print("  three sublattice ensembles grow three DIFFERENT sets")
    return sets


# ----------------------------------------------------- S3: the transfer

def s3_transfer(M=630):
    print("S3: transfer -- set-difference vs destination-dependence (PR3)")
    DA, DB = sublattice_diffs(M, 3), sublattice_diffs(M, 5)
    SA, SB = grow_least_new(DA), grow_least_new(DB)
    check(not unresolved_diffs(SA, DA) and not unresolved_diffs(SB, DB),
          "self-residual nonzero")
    ab = len(unresolved_diffs(SA, DB))
    ba = len(unresolved_diffs(SB, DA))
    print(f"  sublattice: S_A={SA} (U_3), S_B={SB} (U_5)")
    print(f"    self-residual 0/0;  cross A->B {ab} of {len(DB)},  "
          f"B->A {ba} of {len(DA)} diffs")
    print("    fully different SETS, transfer near-intact -> set-diff != dest-dep")
    # unique-need: a difference only q=3 can resolve
    pool = POOL[:5]                                   # [2,3,5,7,11]
    need = prod([p for p in pool if p != 3])          # 2*5*7*11 = 770
    check(need % 3 != 0, "unique-need difference divisible by 3")
    SB2 = grow_least_new({need}, pool)
    check(SB2 == [3], f"unique-need stream grew {SB2}, expected [3]")
    SA2 = grow_least_new(sublattice_diffs(300, 3), pool)
    check(3 not in SA2, "A demanded 3")
    resid = len(unresolved_diffs(SA2, {need}))
    print(f"  unique-need: B needs only 3 (diff {need}); S_A={SA2} skips 3")
    print(f"    cross A->B residual {resid} of 1  -> SURVIVE-SHAPE (transfer-gap)")
    check(resid == 1, "unique-need transfer-gap did not fire")


# ------------------------------------------------------- S4: the myopia

def min_cover(D, pool=POOL):
    """Brute-force minimum hitting set of primes (size-ascending)."""
    D = list(D)
    for size in range(len(pool) + 1):
        for combo in combinations(pool, size):
            if not unresolved_diffs(list(combo), D):
                return list(combo)
    return list(pool)


def s4_myopia():
    print("S4: myopia -- least-new vs the minimum cover (PR4, secondary)")
    rng = random.Random(7)
    gaps, trials = 0, 40
    for _ in range(trials):
        M = rng.randrange(12, 40)
        D = diffs_of(random_labeling(M, rng.randrange(2, 5), rng))
        if not D:
            continue
        g = grow_least_new(D, POOL[:6])
        m = min_cover(D, POOL[:6])
        check(len(g) >= len(m), "least-new below the minimum cover")
        if len(g) > len(m):
            gaps += 1
    print(f"  {trials} random small instances: least-new >= min cover always; "
          f"strict overpay in {gaps}")
    pool = POOL[:5]
    D = {770, 1}                        # 770 = 2*5*7*11 (only 3 resolves); 1 (any)
    g, m = grow_least_new(D, pool), min_cover(D, pool)
    check(len(g) >= len(m), "hand myopia check")
    print(f"    hand instance D={sorted(D)}: least-new {g}, min cover {m}")


# ------------------------------------------------- S5: the subsumption

def s5_descent():
    print("S5: descent -- growth IS greedy hitting-set (PR5)")
    D = sorted(diffs_of(random_labeling(120, 6, random.Random(3))))
    S = grow_least_new(D)
    covered = [False] * len(D)
    hs = []
    while not all(covered):
        for p in POOL:
            if p in hs:
                continue
            hits = [i for i, d in enumerate(D) if not covered[i] and d % p != 0]
            if hits:
                hs.append(p)
                for i in hits:
                    covered[i] = True
                break
        else:
            break
    check(hs == S, f"hitting-set greedy {hs} != grow_least_new {S}")
    print(f"  hit(p, d) = [p does not divide d]; greedy hitting-set reproduces")
    print(f"  grow_least_new exactly: {S}")
    print("  => the collision learner is set-cover; generic instance = prefix")


if __name__ == "__main__":
    s0_controls()
    s1_generic()
    s2_content()
    s3_transfer()
    s4_myopia()
    s5_descent()
    print(f"\nALL SECTIONS PASS -- {CHECKS} checks, exit 0")
