"""The seed-flower as an operator: -chi iterated on designed towers.

THE OPERATOR. Any squarefree prime set S is a tower ring (a designed
tower). Its CRT Euler characteristic chi = N(1 - k + sum 1/p) is an
integer; the seed-flower principle says -chi names primes
OUTSIDE S. Read that as a map:

    F(S) = the prime support of |-chi(S)|

F sends designed towers to designed towers -- iterate it. The dynamics
live on the designed-tower lattice, not inside any one rung. This script
charts them: fixed points, cycles, transients, escape.

TWO LAWS FIRST (property -- one-line proofs, verified exhaustively over
every step this script computes):
  L1 (fixed-point-free). For p in S: N = 0 and N/q = 0 (mod p) for q != p,
      so -chi = -N/p (mod p), nonzero. F(S) is DISJOINT from S -- no fixed
      points exist, and any cycle has period >= 2. This is the
      member-coprimality pre-sieve (explore_chi_primality.py) read
      dynamically.
  L2 (2 is never named). If 2 in S, -chi = -N/2 = 1 (mod 2) (N/2 odd,
      squarefree). If 2 not in S, N and every N/p are odd, so
      -chi = (k-1) - k = 1 (mod 2). Either way -chi is ODD: 2 never
      divides it, and after one step every orbit lives on odd-prime sets.
      (= the member-coprimality + 2-invisibility entries of
      explore_chi_primality.py, read dynamically.)
  Sign (property): -chi = -1 for |S| = 1; -chi = 1 for S = {2,3};
      -chi > 1 for every other |S| >= 2 (k >= 3: -chi >= N(k/2-1) >= N/2).

CONVENTIONS. |-chi| <= 1 ends the orbit: fate DEAD (the support is empty;
every singleton has -chi = -1, so reaching a prime -chi means death two
steps later at most). Values past BOUND = 10^18 are not factored: fate
ESCAPE, support honestly UNKNOWN past the bound (the factorization-cost
cap -- a standing limit worth revisiting with faster factoring).
MAX_ITERS = 120 without a fate: UNDECIDED.

PREDICTIONS (stated before the run):
  P1: the two laws hold over every computed step (proof above; the
      exhaustive check is wiring, not discovery).
  P2: NO cycles of any period anywhere in the sweeps (RAD's 127
      sub-rings, the 2047 subsets of the first 11 primes, the random
      large seeds).
  P3: death dominates RAD: >= 100/127 orbits reach the empty set; escape
      past 10^18 is a minority fate (possibly empty).
  P4: transients are short: median RAD death step <= 8, max <= 25.
  P5: escape fraction RISES with seed size k (extended sweep, k = 1..11:
      small-k seeds die, large-k seeds increasingly escape).
  P6: the smooth skeleton is a small forest: <= 15 of the 127 RAD
      sub-rings have an axiom-smooth image (support inside {2..17}),
      there are NO smooth cycles, and every fully-smooth orbit dies
      within <= 6 steps. (Hand specimen found while predicting:
      {2,3,13} -> {5,17} -> {3,7} -> {11} -> dead, all-smooth.)

Tier: L1/L2/sign = property (proved). Everything empirical below =
observation (single sweep, stated ranges). Numerology watch: 137 is
named as a value of one orbit, nothing more.

Run: python prime/code/explore_seed_flower_operator.py   (~1 s)
"""

import os
import random
import sys
import time
from collections import Counter
from itertools import combinations
from math import prod

from sympy import factorint, primerange

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import Ring, euler_characteristic  # noqa: E402 (library cross-check)

BOUND = 10 ** 18
MAX_ITERS = 120
AXIOM = frozenset([2, 3, 5, 7, 11, 13, 17])
EXT_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, ok))
    print(f"  CHECK {len(CHECKS):>2}: {'PASS' if ok else 'FAIL'}  {name}"
          + (f"  [{detail}]" if detail else ""))


def neg_chi(S):
    k = len(S)
    N = prod(S)
    return N * (k - 1) - sum(N // p for p in S)


_cache = {}  # frozenset -> (value, next) where next is frozenset | 'DEAD' | 'ESCAPE'


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
    """Iterate F from seed. Returns fate dict."""
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


def fct_str(v):
    if v == 1:
        return "1"
    if v > BOUND:
        return ">BOUND"
    f = factorint(v)
    return "*".join(f"{p}^{e}" if e > 1 else str(p) for p in sorted(f) for e in [f[p]])


def section(title):
    print(f"\n{'=' * 72}\n  {title}\n{'=' * 72}")


t0 = time.time()

# ----------------------------------------------------------------------
section("I. THE OPERATOR AND ITS LAWS")
# ----------------------------------------------------------------------

print("""
F(S) = prime support of |-chi(S)|, chi = N(1 - k + sum 1/p).
L1: -chi = -N/p (mod p) for p in S  => F(S) disjoint from S (no fixed
    points; cycles need period >= 2). The explore_chi_primality.py
    pre-sieve, read dynamically.
L2: -chi is odd for every nonempty squarefree S => 2 is never named.
Sign: -chi = -1 at singletons, +1 at {2,3}, > 1 everywhere else.
(Exhaustive verification over every computed step: checks section.)
""")

print("Specimens (the known flowers, now as orbit openings):")
for seed in [(2, 3, 5), (2, 3, 5, 13, 17)]:
    v = neg_chi(frozenset(seed))  # neg_chi already returns -chi
    print(f"  -chi({set_str(seed)}) = {v} = {fct_str(v)}")

# ----------------------------------------------------------------------
section("II. SPECIMEN ORBITS")
# ----------------------------------------------------------------------

for seed in [(2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11), (2, 3, 5, 13, 17),
             (2, 3, 13), AXIOM]:
    ob = orbit(seed)
    print(f"\n  seed {set_str(seed)}  ->  {ob['fate']} at step {ob['steps']}")
    for i, S in enumerate(ob['path']):
        v = ob['values'][i] if i < len(ob['values']) else None
        arrow = f"  --{v}={fct_str(v)}-->" if v is not None else ""
        print(f"    {set_str(S)}{arrow}")
    if ob['fate'] == 'DEAD':
        print("    {} (empty: dead)")

# ----------------------------------------------------------------------
section("III. EXHAUSTIVE RAD SWEEP: ALL 127 SUB-RINGS")
# ----------------------------------------------------------------------

rad_orbits = {}
for size in range(1, 8):
    for c in combinations(sorted(AXIOM), size):
        rad_orbits[frozenset(c)] = orbit(c)

fates = Counter(ob['fate'] for ob in rad_orbits.values())
print(f"\n  Fate census over 127 seeds: {dict(fates)}")

dead_steps = sorted(ob['steps'] for ob in rad_orbits.values() if ob['fate'] == 'DEAD')
if dead_steps:
    med = dead_steps[len(dead_steps) // 2]
    print(f"  Death steps: min {dead_steps[0]}, median {med}, max {dead_steps[-1]}")

print("\n  Fate by seed size:")
print(f"  {'k':>3} {'seeds':>6} {'DEAD':>5} {'ESCAPE':>7} {'CYCLE':>6} {'UNDEC':>6}")
for size in range(1, 8):
    obs = [ob for S, ob in rad_orbits.items() if len(S) == size]
    f = Counter(ob['fate'] for ob in obs)
    print(f"  {size:>3} {len(obs):>6} {f['DEAD']:>5} {f['ESCAPE']:>7} "
          f"{f['CYCLE']:>6} {f['UNDECIDED']:>6}")

# longest transient + biggest excursion
longest = max(rad_orbits.items(), key=lambda kv: kv[1]['steps'])
print(f"\n  Longest RAD orbit: seed {set_str(longest[0])}, "
      f"{longest[1]['fate']} at step {longest[1]['steps']}")
for i, S in enumerate(longest[1]['path']):
    v = longest[1]['values'][i] if i < len(longest[1]['values']) else None
    print(f"    {set_str(S)}" + (f"  --{v}-->" if v is not None else ""))

peaked = max(rad_orbits.items(),
             key=lambda kv: max(kv[1]['values']) / kv[1]['values'][0])
seed_v = peaked[1]['values'][0]
peak_v = max(peaked[1]['values'])
print(f"\n  Biggest excursion (peak/first ratio): seed {set_str(peaked[0])}, "
      f"first value {seed_v}, peak {peak_v}  (x{peak_v / seed_v:.1f})")

escapes_rad = [(S, ob) for S, ob in rad_orbits.items() if ob['fate'] == 'ESCAPE']
if escapes_rad:
    print(f"\n  RAD escapes ({len(escapes_rad)}):")
    for S, ob in escapes_rad:
        print(f"    seed {set_str(S)}: passed {ob['values'][-1]:.2e} at step {ob['steps']}")
undec_rad = [(S, ob) for S, ob in rad_orbits.items() if ob['fate'] == 'UNDECIDED']
if undec_rad:
    print(f"\n  RAD undecided ({len(undec_rad)}):")
    for S, ob in undec_rad:
        print(f"    seed {set_str(S)}: at step {ob['steps']}, last value {ob['values'][-1]:.2e}")

# ----------------------------------------------------------------------
section("IV. EXTENDED SWEEP: ALL 2047 SUBSETS OF THE FIRST 11 PRIMES")
# ----------------------------------------------------------------------

ext_orbits = {}
for size in range(1, 12):
    for c in combinations(EXT_PRIMES, size):
        ext_orbits[frozenset(c)] = orbit(c)

ext_fates = Counter(ob['fate'] for ob in ext_orbits.values())
print(f"\n  Fate census over 2047 seeds: {dict(ext_fates)}")

print("\n  Fate by seed size (escape fraction is the P5 subject):")
print(f"  {'k':>3} {'seeds':>6} {'DEAD':>5} {'ESCAPE':>7} {'CYCLE':>6} "
      f"{'UNDEC':>6} {'esc%':>6}")
esc_frac_by_k = {}
for size in range(1, 12):
    obs = [ob for S, ob in ext_orbits.items() if len(S) == size]
    f = Counter(ob['fate'] for ob in obs)
    frac = f['ESCAPE'] / len(obs)
    esc_frac_by_k[size] = frac
    print(f"  {size:>3} {len(obs):>6} {f['DEAD']:>5} {f['ESCAPE']:>7} "
          f"{f['CYCLE']:>6} {f['UNDECIDED']:>6} {frac:>6.1%}")

# ----------------------------------------------------------------------
section("V. RANDOM LARGE SEEDS")
# ----------------------------------------------------------------------

rng = random.Random(58)
mid_primes = list(primerange(100, 10 ** 4))
big_primes = list(primerange(10 ** 3, 10 ** 6))
rand_seeds = ([tuple(rng.sample(big_primes, 2)) for _ in range(40)]
              + [tuple(rng.sample(mid_primes, 3)) for _ in range(40)])
rand_orbits = {frozenset(s): orbit(s) for s in rand_seeds}
rand_fates = Counter(ob['fate'] for ob in rand_orbits.values())
print(f"\n  40 random pairs (primes in [10^3, 10^6]) + 40 random triples "
      f"(primes in [10^2, 10^4]):")
print(f"  Fate census: {dict(rand_fates)}")
rd = sorted(ob['steps'] for ob in rand_orbits.values() if ob['fate'] == 'DEAD')
if rd:
    print(f"  Death steps: min {rd[0]}, median {rd[len(rd) // 2]}, max {rd[-1]}")

# ----------------------------------------------------------------------
section("VI. THE MECHANISM OF MORTALITY")
# ----------------------------------------------------------------------

print("""
L3 (shrink lemma, property): -chi(S) < N(k-1), so a step OUT of a
support of size k' lands below (k'-1) x the radical of the current
value. For k' = 2 that is STRICT SHRINK (-chi({p,q}) = (p-1)(q-1)-1
< pq); k' = 1 dies. Growth requires support >= 3 -- and supports of
typical values are small (omega ~ ln ln v), while square parts shave
the radical further. Death gate: |-chi| <= 1 happens only at
singletons and {2,3}, and {2,3} is UNREACHABLE (L2: 2 is never
named) -- so every death (past trivial seeds) passes through a
PRIME-POWER -chi value.
""")

# growth-step census by the support size that produced the value
grow, tot = Counter(), Counter()
for d in (rad_orbits, ext_orbits, rand_orbits):
    for ob in d.values():
        vs, ph = ob['values'], ob['path']
        for i in range(1, len(vs)):
            ksz = len(ph[i])  # support that produced vs[i]
            tot[ksz] += 1
            if vs[i] > vs[i - 1]:
                grow[ksz] += 1
print("  Per-step growth census (over all orbit transitions; shared tails")
print("  counted once per orbit):")
print(f"  {'support k':>10} {'steps':>7} {'grew':>6} {'frac':>7}")
for ksz in sorted(tot):
    print(f"  {ksz:>10} {tot[ksz]:>7} {grow[ksz]:>6} {grow[ksz] / tot[ksz]:>7.1%}")

# death-gate census: the value that produced each terminal singleton
gates = Counter()
for d in (rad_orbits, ext_orbits, rand_orbits):
    for ob in d.values():
        if ob['fate'] == 'DEAD' and ob['steps'] >= 2:
            pen = ob['path'][-1]
            v_in = ob['values'][-2]
            p = next(iter(pen))
            gates['prime' if v_in == p else 'prime power (e >= 2)'] += 1
print(f"\n  Death gates (terminal singleton's producing value): {dict(gates)}")

# the escapes, in full
print("\n  The escapes (support sizes along the path, then values):")
for label, d in [("EXT", ext_orbits), ("RAND", rand_orbits)]:
    for S, ob in sorted(d.items(), key=lambda kv: len(kv[0])):
        if ob['fate'] == 'ESCAPE':
            sizes = ",".join(str(len(P)) for P in ob['path'])
            vals = " ".join(f"{v:.1e}" for v in ob['values'])
            print(f"    [{label}] seed {set_str(S)}: escaped at step {ob['steps']}")
            print(f"          supports {sizes}")
            print(f"          values {vals}")

# ----------------------------------------------------------------------
section("VII. THE SMOOTH SKELETON (F restricted to the axiom set)")
# ----------------------------------------------------------------------

print("""
Which of the 127 RAD sub-rings have an axiom-smooth image (F(S) inside
{2..17})? F restricted to those nodes is the smooth skeleton -- the part
of the dynamics that never leaves RAD.
""")

smooth_edge = {}   # S -> F(S), only when F(S) is a nonempty smooth set
smooth_dead = []   # S with |-chi| <= 1
for S in rad_orbits:
    v, nxt = step(S)
    if nxt == 'DEAD':
        smooth_dead.append(S)
    elif isinstance(nxt, frozenset) and nxt <= AXIOM:
        smooth_edge[S] = nxt

print(f"  Nodes with smooth image: {len(smooth_edge)} of 127 "
      f"(+ {len(smooth_dead)} that die immediately)")
for S, T in sorted(smooth_edge.items(), key=lambda kv: (len(kv[0]), prod(kv[0]))):
    v, _ = step(S)
    print(f"    {set_str(S):<18} --{v}--> {set_str(T)}")

# smooth cycles? walk the functional graph restricted to smooth_edge
smooth_cycles = []
for start in smooth_edge:
    seen = {start}
    cur = start
    while cur in smooth_edge:
        cur = smooth_edge[cur]
        if cur in seen:
            smooth_cycles.append((start, cur))
            break
        seen.add(cur)
print(f"\n  Smooth cycles found: {len(smooth_cycles)}")

# fully-smooth orbits: every set in the path inside AXIOM
fully_smooth = []
for S, ob in rad_orbits.items():
    if all(P <= AXIOM for P in ob['path']):
        fully_smooth.append((S, ob))
print(f"\n  Fully smooth-lived orbits (every set in path inside the axiom set):"
      f" {len(fully_smooth)}")
for S, ob in sorted(fully_smooth, key=lambda kv: -kv[1]['steps']):
    chain = " -> ".join(set_str(P) for P in ob['path'])
    print(f"    {chain}  [{ob['fate']} at {ob['steps']}]")
max_smooth_steps = max((ob['steps'] for _, ob in fully_smooth), default=0)

# ----------------------------------------------------------------------
section("VIII. CHECKS")
# ----------------------------------------------------------------------

all_orbits = {}
all_orbits.update(rad_orbits)
all_orbits.update(ext_orbits)
all_orbits.update(rand_orbits)

# 1. specimens
check("specimens: -chi({2,3,5}) = 29, -chi({2,3,5,13,17}) = 137^2, "
      "-chi({2,3}) = 1, -chi({p}) = -1",
      neg_chi(frozenset([2, 3, 5])) == 29
      and neg_chi(frozenset([2, 3, 5, 13, 17])) == 137 ** 2
      and neg_chi(frozenset([2, 3])) == 1
      and all(neg_chi(frozenset([p])) == -1 for p in AXIOM))

# 2. L1 over every computed step (works even past BOUND: v mod p is cheap)
l1_ok = all(all(v % p != 0 for p in S) for S, (v, _) in _cache.items() if v > 1)
check("L1 fixed-point-free: no member of S divides -chi(S), every step",
      l1_ok, f"{len(_cache)} cached steps")

# 3. L2 oddness
check("L2: -chi odd at every computed step",
      all(v % 2 == 1 for v, _ in _cache.values()))

# 4. sign facts
sign_ok = all(v >= 1 and (v > 1 or len(S) == 1 or S == frozenset([2, 3]))
              for S, (v, _) in _cache.items())
check("sign: |-chi| >= 1 always; = 1 only at singletons and {2,3}", sign_ok)

# 5. partitions
check("fate partitions: RAD 127, EXT 2047, RAND 80",
      sum(Counter(ob['fate'] for ob in rad_orbits.values()).values()) == 127
      and sum(ext_fates.values()) == 2047
      and sum(rand_fates.values()) == len(rand_orbits))

# 6. fate consistency
cons = True
for ob in all_orbits.values():
    if ob['fate'] == 'DEAD':
        cons &= ob['values'][-1] <= 1
    elif ob['fate'] == 'ESCAPE':
        cons &= ob['values'][-1] > BOUND
    elif ob['fate'] == 'CYCLE':
        cons &= ob['period'] >= 2
check("fate consistency: DEAD ends <= 1, ESCAPE ends > BOUND, "
      "CYCLE period >= 2", cons)

# 7. hand-traced orbit (computed by hand while writing predictions)
hand = orbit((2, 3, 5, 7, 11))
hand_path = [frozenset(s) for s in
             [(2, 3, 5, 7, 11), (59, 107), (3, 683), (29, 47), (3, 11, 13), (643,)]]
check("hand-traced orbit {2,3,5,7,11}: values 6313,6147,1363,1287,643,1; "
      "dead at 6",
      hand['fate'] == 'DEAD' and hand['steps'] == 6
      and hand['values'] == [6313, 6147, 1363, 1287, 643, 1]
      and hand['path'] == hand_path)

# 8. factorization wiring: every cached support re-multiplies into v
fac_ok = True
for S, (v, nxt) in _cache.items():
    if isinstance(nxt, frozenset):
        f = factorint(v)
        fac_ok &= prod(p ** e for p, e in f.items()) == v
        fac_ok &= frozenset(f) == nxt
check("factorization wiring: support * exponents re-multiplies to |-chi|",
      fac_ok)

# 9. smooth skeleton independently consistent with orbit paths
sk_ok = (len(smooth_cycles) == 0)
for S, ob in fully_smooth:
    # every consecutive pair in a fully smooth path must be a smooth edge
    for a, b in zip(ob['path'], ob['path'][1:]):
        sk_ok &= smooth_edge.get(a) == b
check("smooth skeleton: no cycles; fully-smooth paths walk smooth edges",
      sk_ok)

# 10. cache-independence: fresh recompute of 5 orbits matches
saved = dict(_cache)
_cache.clear()
fresh_ok = True
probe = list(rad_orbits)[7::25][:5]
for S in probe:
    fresh_ok &= orbit(S)['fate'] == rad_orbits[S]['fate']
_cache.update(saved)
check("cache-independence: 5 fresh orbits reproduce their fates", fresh_ok)

# 11. library cross-check: the in-script formula against crt.py's
#     euler_characteristic, exhaustive over all 127 thin RAD sub-rings
lib_ok = all(
    neg_chi(frozenset(c)) == -euler_characteristic(Ring("t", list(c), [1] * len(c)))
    for size in range(1, 8) for c in combinations(sorted(AXIOM), size))
check("library cross-check: neg_chi == -euler_characteristic(crt.Ring), "
      "all 127 thin sub-rings", lib_ok)

# 12. L3 shrink-lemma bounds, exhaustive over the cache
l3_ok = all(v < (len(S) - 1) * prod(S) for S, (v, _) in _cache.items()
            if len(S) >= 2)
l3_ok &= all(v < prod(S) for S, (v, _) in _cache.items() if len(S) == 2)
check("L3 bounds: -chi(S) < N(k-1) for k >= 2; strict shrink at k = 2",
      l3_ok)

# 13. death gates: {2,3} never reached; every non-trivial death passes a
#     prime-power -chi (terminal singleton)
gate_ok = all(nxt != frozenset([2, 3]) for _, nxt in _cache.values()
              if isinstance(nxt, frozenset))
for d in (rad_orbits, ext_orbits, rand_orbits):
    for ob in d.values():
        if ob['fate'] == 'DEAD' and ob['steps'] >= 2:
            gate_ok &= len(ob['path'][-1]) == 1
check("death gates: {2,3} unreachable; every non-trivial death ends in a "
      "singleton (prime-power -chi)", gate_ok)

# ----------------------------------------------------------------------
section("IX. PREDICTIONS vs OUTCOMES")
# ----------------------------------------------------------------------

n_cycles = sum(1 for ob in all_orbits.values() if ob['fate'] == 'CYCLE')
rad_dead = fates['DEAD']
med_dead = dead_steps[len(dead_steps) // 2] if dead_steps else None
max_dead = dead_steps[-1] if dead_steps else None
esc_small = esc_frac_by_k.get(2, 0)
esc_big = esc_frac_by_k.get(11, 0)

print(f"""
  P1 (laws):     L1 + L2 hold over all {len(_cache)} computed steps
                 -> {'CONFIRMED' if l1_ok else 'REFUTED'}
  P2 (cycles):   predicted none; found {n_cycles}
                 -> {'CONFIRMED' if n_cycles == 0 else 'MISSED'}
  P3 (death):    predicted >= 100/127 RAD deaths; got {rad_dead}/127
                 (escape {fates['ESCAPE']}, undecided {fates['UNDECIDED']})
                 -> {'CONFIRMED' if rad_dead >= 100 else 'MISSED'}
  P4 (speed):    predicted median <= 8, max <= 25; got median {med_dead}, max {max_dead}
                 -> {'CONFIRMED' if med_dead is not None and med_dead <= 8 and max_dead <= 25 else 'MISSED'}
  P5 (escape-k): predicted escape fraction rises with k;
                 k=2: {esc_small:.1%} ... k=11: {esc_big:.1%}
                 -> {'CONFIRMED' if esc_big > esc_small else 'MISSED'}
  P6 (smooth):   predicted <= 15 smooth-image nodes, 0 smooth cycles,
                 fully-smooth orbits die within <= 6 steps;
                 got {len(smooth_edge)} nodes, {len(smooth_cycles)} cycles,
                 max fully-smooth life {max_smooth_steps}
                 -> {'CONFIRMED' if len(smooth_edge) <= 15 and not smooth_cycles and max_smooth_steps <= 6 else 'MISSED'}
""")

n_pass = sum(1 for _, ok in CHECKS if ok)
print(f"{'=' * 72}")
print(f"  {n_pass}/{len(CHECKS)} checks pass "
      f"{'-- ALL GREEN' if n_pass == len(CHECKS) else '-- FAILURES ABOVE'}"
      f"   ({time.time() - t0:.1f} s)")
print(f"{'=' * 72}")
