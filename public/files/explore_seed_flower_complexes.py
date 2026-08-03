"""Is the seed-flower map a map of complexes?

QUESTION. The seed-flower operator F(S) = prime support of |-chi(S)|
iterates on squarefree prime sets (explore_seed_flower_operator.py).
Each set S also carries a topological object: the clique complex X(S)
of K_{p_1} [] ... [] K_{p_k}, homotopy equivalent to a wedge of b1
circles with b1 = 1 - chi (explore_clique_betti.py,
explore_naming_complex.py). F's target shares no coordinate with its
source (L1: F(S) disjoint from S), so the honest first question is
whether ANY map of complexes exists to find. The cheap probe: what F
does to b1 over the orbits already swept.

THE HAND-ATTACK (on paper, before engine code). b1 = 1 - chi means
-chi(S) = b1(S) - 1: the integer the operator factors IS the circle
count minus one. Consequences, each a one-line derivation the rig
checks exhaustively:

  D1 (descent). F(S) = supp(|b1(S) - 1|) depends on X(S) only through
      its homotopy type. Since b1 classifies these complexes up to
      homotopy (wedges of circles), F descends to a well-defined map
      on homotopy types: the coordinates never mattered. Death reads
      as CONTRACTIBILITY: every non-trivial death passes a singleton,
      whose complex is a simplex (b1 = 0).
  D2 (consecutive coprimality). supp(v_t) = P_{t+1} and L1 makes
      v_{t+1} = -chi(P_{t+1}) coprime to every prime of P_{t+1}, so
      gcd(v_t, v_{t+1}) = 1: consecutive orbit values share no factor.
  D3 (no covering realization). A connected d-fold cover has
      chi(source) = d * chi(target), i.e. v_t = d * v_{t+1} up to the
      sign convention; D2 forces |v_{t+1}| = 1, so no covering map in
      either direction between consecutive live complexes -- the only
      covers sit at the contractible ends. No ring map either:
      gcd(N(S), N(F(S))) = 1 and Z/N -> Z/N' needs N' | N. So the map
      of complexes exists ONLY at the homotopy-invariant level, never
      as a continuous realization.

PREDICTIONS (stated before the run):
  P1: positive control FIRST -- independent GF(2) simplicial homology
      (boundary-matrix ranks, no wedge theorem) gives b1 = 0, 2, 30
      at {2}, {2,3}, {2,3,5}; then b1(S) - 1 == -chi(S) holds at every
      set the sweeps compute (D1 wiring).
  P2: gcd(v_t, v_{t+1}) = 1 at every computed consecutive pair (D2);
      hence divisibility steps (a cover's arithmetic shadow) number 0.
  P3: collisions -- distinct sets sharing one -chi, which D1 makes
      distinct complexes with one homotopy type and one image -- exist:
      the 11 singletons collide at -chi = -1. Among the 2036
      non-singleton subsets of the first 11 primes: predict ZERO
      collisions (falsifiable; the census prints every class).
  P4: distance-2 prime returns occur -- L1 blocks only immediate
      return. Hand witness: seed {2,3,5,7,11} has v_1 = 6147 = 3^2*683
      and v_3 = 1287 = 3^2*11*13, sharing 3. Predict >= 5% of paths
      with >= 4 sets show one, and 3 is the modal returning prime
      (2 never available, L2).
  P5: the b1 multiplier v_{t+1}/v_t at a squarefree v_t with
      omega factors equals (omega - 1) - sum 1/q exactly; the census
      by omega shows the mass just below omega - 1, square parts
      shaving the radical further (the mechanism census of
      explore_seed_flower_operator.py, now read on circle counts:
      support-2 steps always SHRINK b1, L3).

CONVENTIONS (= explore_seed_flower_operator.py): |-chi| <= 1 ends the
orbit (DEAD); values past BOUND = 10^18 are not factored (ESCAPE);
MAX_ITERS = 120 (UNDECIDED). Sweeps: all 127 subsets of {2..17} (RAD)
and all 2047 subsets of the first 11 primes; shared tails counted once
per orbit.

FINDINGS (11/11 checks green).
  1. THE ANSWER, both directions. YES at the invariant level: D1-D3
     confirmed over 11,342 cached steps and 10,039 consecutive value
     pairs -- F descends to a well-defined map on homotopy types, and
     death is contractibility (every non-trivial death ends at a
     singleton's simplex, b1 = 0). NO as a realization: zero
     divisibility steps among 10,039 pairs -- no covering map, no ring
     map, between any two consecutive live complexes. The positive
     control (independent GF(2) boundary-rank homology) printed
     b1 = 0, 2, 30 at {2}, {2,3}, {2,3,5} before any sweep verdict.
  2. COLLISIONS ARE COMMON -- P3 MISSED, richly. 2047 subsets of the
     first 11 primes take only 2020 distinct -chi values: 17 collision
     classes, 16 of them non-singleton (rule -- exhaustive at that
     range). The famous flower is not even alone in its homotopy type:
     {2,3,5} and {2,31} share -chi = 29 (one wedge of 30 circles, one
     image {29}); the largest class is -chi = 71 = {2,3,11}, {5,19},
     {7,13}. The classes split evenly by shape: 8 mix sizes and 8 are
     same-size pairs or triples ({2,13} and {3,7} at -chi = 11;
     {2,13,17} and {5,7,11} at 603).
  3. DISTANCE-2 RETURNS ARE THE NORM, not the exception: 838/1175 =
     71.3% of paths with >= 4 sets bring some prime back two steps
     after it left (predicted >= 5% -- underconfident by 14x). Modal
     returner 3 (441 orbits), then 5 (280), 7 (222): L1's exclusion
     is exactly one step deep, and the small odd primes shuttle in
     and out of the support for the whole life of an orbit.
  4. THE MULTIPLIER LAW, corrected by its own run: at squarefree v_t
     the ratio v_{t+1}/v_t equals (omega-1) - sum 1/q INTEGER-EXACTLY
     for omega >= 2 -- but the frozen P5 claimed it at EVERY squarefree
     step and broke 2023 times at omega = 1, where the orbit stores
     |-chi| = 1 while the formula wants -chi = -1: the slate forgot
     the absolute value it had itself declared in the conventions.
     Support-2 steps shrink b1 at every occurrence (L3). The whole
     mortality mechanism is thereby a statement about circle counts:
     the hazard race runs on b1, shifted by one.

Tier: D1-D3 = property (proved; exhaustive check is wiring). Finding 2
= rule (exhaustive, subsets of the first 11 primes). Findings 3-4
census lines = observation (the two sweeps' ranges).

Run: python prime/code/explore_seed_flower_complexes.py
     (0.3 s, 62.2 MB peak under memwatch)
"""

import time
from collections import Counter
from itertools import combinations, product
from math import gcd, prod

from sympy import factorint

AXIOM = frozenset([2, 3, 5, 7, 11, 13, 17])
EXT_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
BOUND = 10 ** 18
MAX_ITERS = 120

CHECKS = []


def check(name, ok, note=""):
    CHECKS.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({note})" if note else ""))


def neg_chi(S):
    """-chi(S) = N(k-1) - sum N/p, N = prod(S)."""
    N = prod(S)
    return N * (len(S) - 1) - sum(N // p for p in S)


def b1(S):
    """First Betti number of the clique complex X(S) = 1 - chi."""
    return 1 + neg_chi(S)


_cache = {}


def step(S):
    if S in _cache:
        return _cache[S]
    v = abs(neg_chi(S))
    if v <= 1:
        out = (v, 'DEAD')
    elif v > BOUND:
        out = (v, 'ESCAPE')
    else:
        out = (v, frozenset(factorint(v)))
    _cache[S] = out
    return out


def orbit(seed):
    S = frozenset(seed)
    path = [S]
    values = []
    visited = {S: 0}
    for t in range(MAX_ITERS):
        v, nxt = step(S)
        values.append(v)
        if nxt == 'DEAD':
            return dict(fate='DEAD', steps=t + 1, path=path, values=values)
        if nxt == 'ESCAPE':
            return dict(fate='ESCAPE', steps=t + 1, path=path, values=values)
        if nxt in visited:
            return dict(fate='CYCLE', steps=t + 1, path=path + [nxt],
                        values=values, period=(t + 1) - visited[nxt])
        visited[nxt] = t + 1
        path.append(nxt)
        S = nxt
    return dict(fate='UNDECIDED', steps=MAX_ITERS, path=path, values=values)


def set_str(S):
    return "{" + ",".join(str(p) for p in sorted(S)) + "}"


def gf2_rank(rows):
    """Rank over GF(2) of bitmask rows (Gaussian elimination)."""
    rank = 0
    basis = []
    for r in rows:
        for b in basis:
            r = min(r, r ^ b)
        if r:
            basis.append(r)
            basis.sort(reverse=True)
            rank += 1
    return rank


def homology_b1(sizes):
    """b1 of the clique complex of prod K_{sizes}, by GF(2) boundary
    ranks over explicit simplices. Independent of the wedge theorem:
    cliques found from the one-coordinate adjacency directly."""
    verts = list(product(*[range(p) for p in sizes]))
    vidx = {v: i for i, v in enumerate(verts)}
    k = len(sizes)
    # edges: differ in exactly one coordinate
    edges = []
    for a, b in combinations(verts, 2):
        if sum(x != y for x, y in zip(a, b)) == 1:
            edges.append((a, b))
    eidx = {e: i for i, e in enumerate(edges)}
    # triangles: triples pairwise adjacent = triples inside one line
    tris = []
    for a, b, c in combinations(verts, 3):
        if (sum(x != y for x, y in zip(a, b)) == 1
                and sum(x != y for x, y in zip(a, c)) == 1
                and sum(x != y for x, y in zip(b, c)) == 1):
            tris.append((a, b, c))
    d1 = [(1 << vidx[a]) | (1 << vidx[b]) for a, b in edges]
    d2 = []
    for a, b, c in tris:
        m = 0
        for e in [(a, b), (a, c), (b, c)]:
            m |= 1 << eidx[e]
        d2.append(m)
    r1, r2 = gf2_rank(d1), gf2_rank(d2)
    betti0 = len(verts) - r1
    betti1 = (len(edges) - r1) - r2
    return betti0, betti1


def section(title):
    print(f"\n{'=' * 72}\n  {title}\n{'=' * 72}")


t0 = time.time()

# ----------------------------------------------------------------------
section("I. POSITIVE CONTROL: INDEPENDENT GF(2) HOMOLOGY (runs first)")
# ----------------------------------------------------------------------

control_ok = True
for sizes, want in [((2,), 0), ((2, 3), 2), ((2, 3, 5), 30)]:
    c0, c1 = homology_b1(sizes)
    formula = b1(frozenset(sizes)) if len(set(sizes)) == len(sizes) else None
    print(f"  sizes {sizes}: GF(2) homology b0 = {c0}, b1 = {c1}; "
          f"formula b1 = {formula}; expected {want}")
    control_ok &= (c0 == 1 and c1 == want and formula == want)
check("positive control: GF(2) boundary ranks give b1 = 0, 2, 30 at "
      "{2}, {2,3}, {2,3,5}, matching 1 - chi", control_ok)

# ----------------------------------------------------------------------
section("II. THE SWEEPS (RAD 127 + EXT 2047), b1 ALONGSIDE")
# ----------------------------------------------------------------------

rad_orbits = {}
for size in range(1, 8):
    for c in combinations(sorted(AXIOM), size):
        rad_orbits[frozenset(c)] = orbit(c)
ext_orbits = {}
for size in range(1, 12):
    for c in combinations(EXT_PRIMES, size):
        ext_orbits[frozenset(c)] = orbit(c)

all_orbits = dict(rad_orbits)
all_orbits.update(ext_orbits)

fates = Counter(ob['fate'] for ob in ext_orbits.values())
print(f"\n  EXT fate census (2047 seeds): {dict(fates)}")
print(f"  RAD fate census (127 seeds): "
      f"{dict(Counter(ob['fate'] for ob in rad_orbits.values()))}")

print("\n  Specimen orbit as complexes (b1 = v + 1 along the path):")
ob = orbit((2, 3, 5, 7, 11))
for i, S in enumerate(ob['path']):
    v = ob['values'][i] if i < len(ob['values']) else None
    tail = f"  b1(X) = {b1(S)}" + (f",  -chi = {v}" if v is not None else "")
    print(f"    {set_str(S)}{tail}")

# ----------------------------------------------------------------------
section("III. COLLISIONS: DISTINCT SETS, ONE HOMOTOPY TYPE, ONE IMAGE")
# ----------------------------------------------------------------------

by_v = {}
for size in range(1, 12):
    for c in combinations(EXT_PRIMES, size):
        by_v.setdefault(neg_chi(c), []).append(frozenset(c))
collisions = {v: ss for v, ss in by_v.items() if len(ss) > 1}
print(f"\n  Distinct -chi values over 2047 subsets: {len(by_v)}")
print(f"  Collision classes (>= 2 sets sharing one -chi): {len(collisions)}")
for v, ss in sorted(collisions.items()):
    names = " ".join(set_str(S) for S in sorted(ss, key=sorted)[:12])
    more = "" if len(ss) <= 12 else f" ... ({len(ss)} total)"
    print(f"    -chi = {v}: {names}{more}")
nonsing = {v: ss for v, ss in collisions.items()
           if any(len(S) > 1 for S in ss)}
print(f"  Classes containing a non-singleton: {len(nonsing)}")

# ----------------------------------------------------------------------
section("IV. CONSECUTIVE COPRIMALITY AND THE COVERING CENSUS")
# ----------------------------------------------------------------------

pairs = 0
coprime_ok = True
div_steps = 0
for ob in all_orbits.values():
    vs = ob['values']
    for a, b in zip(vs, vs[1:]):
        pairs += 1
        if gcd(a, b) != 1:
            coprime_ok = False
        if (b > 1 and a % b == 0) or (a > 1 and b % a == 0):
            div_steps += 1
print(f"\n  Consecutive value pairs over both sweeps: {pairs}")
print(f"  All coprime: {coprime_ok}")
print(f"  Divisibility steps (a cover's arithmetic shadow): {div_steps}")

# distance-2 returns: path sets two apart sharing a prime
ret_orbits = 0
eligible = 0
returners = Counter()
witness = None
for S, ob in all_orbits.items():
    path = ob['path']
    if len(path) < 4:
        continue
    eligible += 1
    hit = set()
    for t in range(len(path) - 2):
        hit |= path[t] & path[t + 2]
    if hit:
        ret_orbits += 1
        for p in hit:
            returners[p] += 1
        if witness is None:
            witness = (S, sorted(hit))
print(f"\n  Distance-2 prime returns (paths with >= 4 sets): "
      f"{ret_orbits}/{eligible} orbits")
print(f"  Returning primes (per orbit): {dict(returners.most_common(10))}")
if witness:
    print(f"  First witness: seed {set_str(witness[0])}, returns {witness[1]}")

# ----------------------------------------------------------------------
section("V. WHAT F DOES TO b1: THE MULTIPLIER CENSUS")
# ----------------------------------------------------------------------

# ratio v_{t+1}/v_t bucketed by omega(v_t) = |P_{t+1}|, squarefree split
buckets = {}
sf_exact_ok = True       # the omega >= 2 law, integer-exact
sf_om1_breaks = 0        # where the frozen P5 forgot the absolute value
shrink2_ok = True
for ob in all_orbits.values():
    vs, path = ob['values'], ob['path']
    for t in range(len(vs) - 1):
        T = path[t + 1]          # supp(v_t)
        om = len(T)
        ratio = vs[t + 1] / vs[t]
        sf = (prod(T) == vs[t])
        buckets.setdefault((om, sf), []).append(ratio)
        if sf:
            # integer-exact: v_{t+1} = v_t(om-1) - sum v_t/q needs
            # -chi(T) > 0, i.e. om >= 2 -- at om = 1 the orbit stores
            # |-chi| = 1, not -chi = -1
            expect = vs[t] * (om - 1) - sum(vs[t] // q for q in T)
            if om >= 2:
                if vs[t + 1] != expect:
                    sf_exact_ok = False
            elif vs[t + 1] != expect:
                sf_om1_breaks += 1
        if om == 2 and vs[t + 1] >= vs[t]:
            shrink2_ok = False
print(f"\n  {'omega':>6} {'sqfree':>7} {'steps':>6} {'min':>8} "
      f"{'median':>8} {'max':>8}")
for (om, sf), rs in sorted(buckets.items()):
    rs.sort()
    print(f"  {om:>6} {str(sf):>7} {len(rs):>6} {rs[0]:>8.3f} "
          f"{rs[len(rs) // 2]:>8.3f} {rs[-1]:>8.3f}")
print(f"\n  Squarefree ratio == (omega-1) - sum 1/q, omega >= 2, "
      f"integer-exact: {sf_exact_ok}")
print(f"  omega = 1 breaks of that formula (the absolute value at the "
      f"terminal step): {sf_om1_breaks}")
print(f"  Support-2 steps all shrink b1: {shrink2_ok}")

# ----------------------------------------------------------------------
section("VI. CHECKS")
# ----------------------------------------------------------------------

# b1 formula wiring over every set the sweeps touched
wired = all(b1(S) - 1 == neg_chi(S) for S in all_orbits)
wired &= all(b1(P) - 1 == neg_chi(P)
             for ob in all_orbits.values() for P in ob['path'])
check("D1 wiring: b1(S) - 1 == -chi(S) at every swept set and path set",
      wired)

check("known values: b1(RAD) = 2,346,894; b1({2,3}) = 2; b1({2,3,5}) = 30",
      b1(AXIOM) == 2346894 and b1(frozenset([2, 3])) == 2
      and b1(frozenset([2, 3, 5])) == 30)

l1_ok = all(all(v % p != 0 for p in S) for S, (v, _) in _cache.items()
            if v > 1)
l2_ok = all(v % 2 == 1 for v, _ in _cache.values())
check("inherited laws: L1 (no member divides -chi) and L2 (-chi odd), "
      "every cached step", l1_ok and l2_ok, f"{len(_cache)} steps")

check("D2: consecutive orbit values coprime, every pair", coprime_ok,
      f"{pairs} pairs")
check("D3 shadow: divisibility steps = 0", div_steps == 0)

hand = orbit((2, 3, 5, 7, 11))
check("hand witness: seed {2,3,5,7,11} has supp(v_1) & supp(v_3) = {3}",
      hand['values'][:4] == [6313, 6147, 1363, 1287]
      and hand['path'][2] & hand['path'][4] == frozenset([3]))

check("fate census matches the operator sweep: RAD all 127 DEAD; "
      "EXT 2044 DEAD",
      Counter(ob['fate'] for ob in rad_orbits.values())['DEAD'] == 127
      and fates['DEAD'] == 2044)

sing_class = by_v.get(-1, [])
check("collision control: the 11 singletons share -chi = -1",
      len(sing_class) == 11 and all(len(S) == 1 for S in sing_class))

well_def = all(len({step(S)[1] if isinstance(step(S)[1], str)
                    else frozenset(step(S)[1]) for S in ss}) == 1
               for ss in collisions.values())
check("descent wiring: every collision class has ONE image F(S)", well_def)

check("multiplier law: squarefree omega >= 2 integer-exact; "
      "support-2 always shrinks", sf_exact_ok and shrink2_ok)

# ----------------------------------------------------------------------
section("VII. PREDICTIONS vs OUTCOMES")
# ----------------------------------------------------------------------

frac = ret_orbits / eligible if eligible else 0
modal = returners.most_common(1)[0][0] if returners else None
print(f"""
  P1 (control + descent): control {'PASS' if control_ok else 'FAIL'}, wiring
      {'holds' if wired else 'BROKEN'} -> {'CONFIRMED' if control_ok and wired else 'REFUTED'}
  P2 (coprimality): {pairs} pairs, all coprime = {coprime_ok},
      divisibility steps = {div_steps} -> {'CONFIRMED' if coprime_ok and div_steps == 0 else 'REFUTED'}
  P3 (collisions): singleton class of 11; non-singleton classes = {len(nonsing)}
      -> {'CONFIRMED' if len(nonsing) == 0 else 'MISSED (classes above)'}
  P4 (distance-2): {ret_orbits}/{eligible} = {frac:.1%} of eligible paths
      (predicted >= 5%); modal returner {modal} (predicted 3)
      -> {'CONFIRMED' if frac >= 0.05 and modal == 3 else 'MISSED'}
  P5 (multiplier): as frozen -- exact at EVERY squarefree v_t -- the law
      breaks at omega = 1 ({sf_om1_breaks} terminal steps: the slate forgot
      the ABSOLUTE VALUE, |-chi| = 1 vs -chi = -1)
      -> MISSED as stated; holds integer-exactly at omega >= 2
      ({'True' if sf_exact_ok else 'False'}), support-2 shrink {shrink2_ok}
""")

n_pass = sum(1 for _, ok in CHECKS if ok)
print(f"{'=' * 72}")
print(f"  {n_pass}/{len(CHECKS)} checks pass "
      f"{'-- ALL GREEN' if n_pass == len(CHECKS) else '-- FAILURES ABOVE'}"
      f"   ({time.time() - t0:.1f} s)")
print(f"{'=' * 72}")
