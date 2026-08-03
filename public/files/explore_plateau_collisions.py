"""Plateau collision mechanism -- what controls the spectral gain at plateaus.

An earlier run measured: plateau rungs k=11..14 gain FEW distinct F values
(60/20/41/70; gain ratios 0.05-0.18, against 0.64-1.50 at the jumps below
k=15), and k=6 gained exactly zero. Open question: what controls the gain?

This script settles the mechanism. Three pieces, all algebraic:

1. PATTERN CRITERION (proved). The gate pattern of n is the set S of
   tower primes dividing n. S occurs among n=1..lambda iff
   prod(S) <= lambda: n = prod(S) realizes exactly S, and any n with
   pattern S is a multiple of prod(S). This replaces the O(lambda*k)
   sweep with a pruned subset enumeration -- rungs far past k=14 open up.

2. PLATEAU DECOMPOSITION (proved). At a plateau rung k (lambda fixed),
   every n=1..lambda either is divisible by p_k (gate 1: F_k = F_{k-1})
   or is not (gate c = -1/(p_k - 1): F_k = c * F_{k-1}). The admissible
   old patterns are unchanged (same lambda), so the distinct-value sets
   obey, exactly:
       V_k = W  union  c*V_{k-1}
   where W = { F_{k-1}(S) : prod(S) <= lambda/p_k } is the WINDOW -- the
   old spectrum as seen through multiples of p_k. Rescaling by c is
   injective, so |c*V_{k-1}| = |V_{k-1}| and
       gain = |V_k| - |V_{k-1}| = |W \\ c*V_{k-1}|.
   The gain at a plateau is the part of the window that the rescaled
   spectrum fails to cover.

3. COLLISION CRITERION (proved). F values are canonical fractions
   s/D with s = (-1)^(#OFF), D = prod_{q OFF}(q-1). A window value s/D
   dies (collides) iff (p_k - 1) | D and (-s, D/(p_k-1)) is an old
   value. Writing both patterns by their ON-sets and cancelling common
   primes, that is: there exist disjoint sets A, B of old primes with
       prod_{q in A}(q-1)  =  (p_k - 1) * prod_{q in B}(q-1),
   |A| + |B| odd, and both witness patterns lambda-admissible. The
   prime 2 contributes factor (2-1)=1 and acts as a parity toggle --
   BUDGETED, not free: the lambda budget can block it
   (explore_plateau_rate.py, caught at k=11). Collisions ARE
   multiplicative relations of p_k - 1 over the older shifted primes
   {q - 1}. The RATE residual is settled in explore_plateau_rate.py:
   collision set = union of relation-applicability sets,
   pattern-rate = closed cell-sum formula, direct factorability
   refuted as the driver at scale.

So the gain is controlled by two quantities:
  - WINDOW SIZE |W|: set by the budget lambda/p_k (richer when lambda
    is large relative to p_k).
  - RELATION RICHNESS of p_k - 1 over {q-1}: each budget-admissible
    relation kills window values. At k=11..14 the windows are nearly
    equal (133/135/135/139), so the gain variation 60/20/41/70 is
    almost entirely collision rate (55/85/70/50%): 36 = 2*18 factors
    DIRECTLY over the shifted primes and 85% of the k=12 window dies;
    42 has no direct factorization and only half the k=14 window dies.
    Direct factorability marks the extremes, not a law: 40 = 4*10 also
    factors directly yet only 70% of the k=13 window dies -- the rate
    is the budget-weighted census of ALL relations.

Run: python prime/code/explore_plateau_collisions.py
"""

from math import prod, lcm
from fractions import Fraction
from time import perf_counter
from collections import Counter
from crt import is_prime


def section(title):
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}")


def first_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def tower_lambda(primes):
    result = 1
    for p in primes:
        result = lcm(result, p - 1)
    return result


def spectrum(primes, budget):
    """Distinct F values over admissible gate patterns, by subset DFS.

    A pattern is its ON-set S (primes dividing n); admissible iff
    prod(S) <= budget (pattern criterion). F = s/D with
    s = (-1)^(#OFF), D = prod_{q OFF}(q-1) -- canonical (numerator +-1).

    Returns (values, leaves): values maps (s, D) -> one representative
    ON-set (first found); leaves = number of admissible patterns.
    """
    k = len(primes)
    phi = prod(p - 1 for p in primes)
    values = {}
    leaves = 0

    def rec(i, pr, e, sel):
        nonlocal leaves
        if i == k:
            leaves += 1
            d = phi // e
            s = -1 if (k - len(sel)) % 2 else 1
            v = (s, d)
            if v not in values:
                values[v] = tuple(sel)
            return
        p = primes[i]
        rec(i + 1, pr, e, sel)              # p OFF
        if pr * p <= budget:                # p ON
            sel.append(p)
            rec(i + 1, pr * p, e * (p - 1), sel)
            sel.pop()

    rec(0, 1, 1, [])
    return values, leaves


K_DIRECT = 10      # direct n-sweep verification ceiling
K_TABLE = 14       # the previously measured range
K_EXTENDED = 22    # extension ceiling (end of the k=18..22 plateau run)
ALL_PRIMES = first_n_primes(K_EXTENDED)


# ========================================================================
# I. PATTERN CRITERION -- VERIFIED AGAINST THE DIRECT SWEEP
# ========================================================================

section("I. PATTERN CRITERION: S occurs in 1..lambda  iff  prod(S) <= lambda")

print("""
  Proof: n = prod(S) is divisible by exactly the primes of S among the
  tower primes, so prod(S) <= lambda realizes the pattern. Conversely
  any n with pattern S is a multiple of prod(S), so prod(S) <= n <= lambda.

  Verification: direct sweep pattern sets vs subset enumeration, k=3..10.
""")

print(f"  {'k':>3} {'lambda':>8} {'sweep pats':>11} {'subset pats':>12} {'match':>6}")
print(f"  {'-' * 46}")

for k in range(3, K_DIRECT + 1):
    ps = ALL_PRIMES[:k]
    lam = tower_lambda(ps)
    swept = set()
    for n in range(1, lam + 1):
        swept.add(tuple(p for p in ps if n % p == 0))
    vals, leaves = spectrum(ps, lam)
    enumerated = set()
    # re-enumerate patterns (cheap at these k) for the set comparison
    def collect(i, pr, sel, out, ps=ps, lam=lam):
        if i == len(ps):
            out.add(tuple(sel))
            return
        collect(i + 1, pr, sel, out)
        if pr * ps[i] <= lam:
            sel.append(ps[i])
            collect(i + 1, pr * ps[i], sel, out)
            sel.pop()
    collect(0, 1, [], enumerated)
    ok = swept == enumerated
    print(f"  {k:>3} {lam:>8,} {len(swept):>11} {len(enumerated):>12} "
          f"{'OK' if ok else 'FAIL':>6}")
    assert ok, f"pattern criterion failed at k={k}"


# ========================================================================
# II. DISTINCT-F BY SUBSET METHOD -- THE EARLIER TABLE, REPRODUCED AND PASSED
# ========================================================================

section("II. DISTINCT F VALUES k=3..14 (subset method vs direct sweep)")

print(f"\n  {'k':>3} {'p_k':>4} {'type':>8} {'lambda':>8} {'patterns':>9} "
      f"{'distinct F':>11} {'gain':>6} {'sweep':>7}")
print(f"  {'-' * 64}")

distinct_at = {}
prev = 0
PRIOR_GAINS = {6: 0, 11: 60, 12: 20, 13: 41, 14: 70}
for k in range(3, K_TABLE + 1):
    ps = ALL_PRIMES[:k]
    lam = tower_lambda(ps)
    lam_prev = tower_lambda(ps[:-1]) if k > 3 else 1
    step = "plateau" if (k > 3 and lam == lam_prev) else "JUMP"
    vals, leaves = spectrum(ps, lam)
    distinct = len(vals)
    distinct_at[k] = vals
    gain = distinct - prev

    sweep_note = ""
    if k <= K_DIRECT:
        swept_f = set()
        for n in range(1, lam + 1):
            f = Fraction(1)
            for p in ps:
                if n % p:
                    f *= Fraction(-1, p - 1)
            swept_f.add(f)
        subset_f = {Fraction(s, d) for (s, d) in vals}
        assert swept_f == subset_f, f"subset method disagrees at k={k}"
        sweep_note = "OK"

    if k in PRIOR_GAINS:
        assert gain == PRIOR_GAINS[k], (
            f"k={k}: gain {gain} != predicted {PRIOR_GAINS[k]}")

    print(f"  {k:>3} {ps[-1]:>4} {step:>8} {lam:>8,} {leaves:>9,} "
          f"{distinct:>11} {gain:>6} {sweep_note:>7}")
    prev = distinct

print("\n  Subset method == direct sweep for k=3..10 (value sets equal).")
print("  Plateau gains match the earlier measurement: k=6 -> 0, k=11..14 -> 60/20/41/70.")


# ========================================================================
# III. PLATEAU DECOMPOSITION -- gain = |W \ c*V_{k-1}|, EXACTLY
# ========================================================================

section("III. PLATEAU DECOMPOSITION: V_k = W union c*V_{k-1}")

print("""
  W = old spectrum through the p_k window (old patterns with budget
  lambda/p_k -- the n divisible by p_k). c = -1/(p_k - 1). Rescaling is
  injective, so gain = |W| - |W intersect c*V_{k-1}|. Verified exactly:
""")

print(f"  {'k':>3} {'p_k':>4} {'budget':>9} {'|W|':>5} {'collide':>8} "
      f"{'gain':>5} {'gain (II)':>10} {'match':>6}")
print(f"  {'-' * 58}")

plateau_data = {}
for k in sorted(PRIOR_GAINS):
    ps = ALL_PRIMES[:k]
    p_new = ps[-1]
    lam = tower_lambda(ps)
    assert lam == tower_lambda(ps[:-1]), f"k={k} is not a plateau"

    old_vals, _ = spectrum(ps[:-1], lam)
    window, _ = spectrum(ps[:-1], lam // p_new)
    rescaled = {(-s, d * (p_new - 1)) for (s, d) in old_vals}

    collided = {v for v in window if v in rescaled}
    gain = len(window) - len(collided)
    gain_ii = len(distinct_at[k]) - len(distinct_at[k - 1])
    ok = gain == gain_ii
    plateau_data[k] = (old_vals, window, collided)

    print(f"  {k:>3} {p_new:>4} {lam // p_new:>9,} {len(window):>5} "
          f"{len(collided):>8} {gain:>5} {gain_ii:>10} "
          f"{'OK' if ok else 'FAIL':>6}")
    assert ok, f"decomposition disagrees at k={k}"

print("""
  The gain IS the uncovered window. Why 20 at k=12 but 70 at k=14 splits
  into two questions: how big is the window (budget lambda/p_k), and how
  much of it does the rescaled spectrum cover (collisions)?
""")


# ========================================================================
# IV. COLLISION CENSUS -- THE MULTIPLICATIVE RELATIONS
# ========================================================================

section("IV. COLLISIONS = MULTIPLICATIVE RELATIONS OF p_k - 1 OVER {q-1}")

print("""
  Each collided window value yields a relation: with S_T = window
  pattern, S_U = old pattern hitting the same value after rescaling,
  cancel common primes (A = S_U - S_T, B = S_T - S_U):

      prod_{q in A}(q-1)  =  (p_k - 1) * prod_{q in B}(q-1),  |A|+|B| odd.

  (One witness per collided value; 2 contributes factor 1 -- a parity
  toggle, budgeted: see explore_plateau_rate.py.) Distinct reduced
  relations per plateau rung:
""")

for k in sorted(plateau_data):
    ps = ALL_PRIMES[:k]
    p_new = ps[-1]
    old_vals, window, collided = plateau_data[k]

    relations = Counter()
    for (s, d) in collided:
        d_u, rem = divmod(d, p_new - 1)
        assert rem == 0, "collision without (p_k - 1) | D"
        s_t = window[(s, d)]
        s_u = old_vals[(-s, d_u)]
        a = tuple(sorted(set(s_u) - set(s_t)))
        b = tuple(sorted(set(s_t) - set(s_u)))
        lhs = prod(q - 1 for q in a)
        rhs = (p_new - 1) * prod(q - 1 for q in b)
        assert lhs == rhs and (len(a) + len(b)) % 2 == 1, \
            f"relation check failed at k={k}: A={a} B={b}"
        relations[(a, b)] += 1

    print(f"\n  k={k} (p_k={p_new}, p_k-1={p_new - 1}): "
          f"|W|={len(window)}, collided={len(collided)}, "
          f"gain={len(window) - len(collided)}")
    for (a, b), count in relations.most_common():
        lhs = " * ".join(f"({q}-1)" for q in a) or "1"
        rhs = " * ".join(f"({q}-1)" for q in b)
        rhs = f"{p_new - 1}" + (f" * {rhs}" if rhs else "")
        print(f"    {lhs} = {rhs}   [kills {count} window value"
              f"{'s' if count > 1 else ''}]")


# ========================================================================
# V. EXTENSION -- THE k=18..22 PLATEAU RUN
# ========================================================================

section("V. EXTENSION PAST k=14: rungs k=15..22 by subset method")

print("""
  The pattern criterion frees the computation from the O(lambda*k)
  sweep, so the next plateau run -- k=18..22, lambda = 480,720,240 --
  is reachable. Full table with plateau decomposition at each plateau:
""")

print(f"  {'k':>3} {'p_k':>4} {'type':>8} {'lambda':>12} {'patterns':>9} "
      f"{'distinct F':>11} {'gain':>6} {'|W|':>6} {'collide':>8} {'sec':>6}")
print(f"  {'-' * 84}")

prev = len(distinct_at[K_TABLE])
for k in range(K_TABLE + 1, K_EXTENDED + 1):
    ps = ALL_PRIMES[:k]
    p_new = ps[-1]
    lam = tower_lambda(ps)
    lam_prev = tower_lambda(ps[:-1])
    plateau = lam == lam_prev
    step = "plateau" if plateau else "JUMP"

    t0 = perf_counter()
    vals, leaves = spectrum(ps, lam)
    distinct = len(vals)
    gain = distinct - prev

    w_note = c_note = ""
    if plateau:
        old_vals, _ = spectrum(ps[:-1], lam)
        window, _ = spectrum(ps[:-1], lam // p_new)
        rescaled = {(-s, d * (p_new - 1)) for (s, d) in old_vals}
        collided = {v for v in window if v in rescaled}
        assert len(window) - len(collided) == gain, \
            f"decomposition disagrees at k={k}"
        plateau_data[k] = (old_vals, window, collided)
        w_note, c_note = str(len(window)), str(len(collided))
    elapsed = perf_counter() - t0

    print(f"  {k:>3} {p_new:>4} {step:>8} {lam:>12,} {leaves:>9,} "
          f"{distinct:>11} {gain:>6} {w_note:>6} {c_note:>8} "
          f"{elapsed:>6.1f}")
    prev = distinct

print("\n  Relations at the new plateaus:")
for k in range(K_TABLE + 1, K_EXTENDED + 1):
    if k not in plateau_data:
        continue
    ps = ALL_PRIMES[:k]
    p_new = ps[-1]
    old_vals, window, collided = plateau_data[k]
    relations = Counter()
    for (s, d) in collided:
        d_u, rem = divmod(d, p_new - 1)
        assert rem == 0, "collision without (p_k - 1) | D"
        s_t = window[(s, d)]
        s_u = old_vals[(-s, d_u)]
        a = tuple(sorted(set(s_u) - set(s_t)))
        b = tuple(sorted(set(s_t) - set(s_u)))
        assert prod(q - 1 for q in a) == (p_new - 1) * prod(q - 1 for q in b) \
            and (len(a) + len(b)) % 2 == 1, \
            f"relation check failed at k={k}: A={a} B={b}"
        relations[(a, b)] += 1
    print(f"\n  k={k} (p_k={p_new}, p_k-1={p_new - 1}): "
          f"|W|={len(window)}, collided={len(collided)}, "
          f"gain={len(window) - len(collided)}, "
          f"{len(relations)} distinct relations")
    for (a, b), count in relations.most_common(6):
        lhs = " * ".join(f"({q}-1)" for q in a) or "1"
        rhs = " * ".join(f"({q}-1)" for q in b)
        rhs = f"{p_new - 1}" + (f" * {rhs}" if rhs else "")
        print(f"    {lhs} = {rhs}   [kills {count}]")
    if len(relations) > 6:
        print(f"    ... and {len(relations) - 6} more")


# ========================================================================
# VI. KEY FINDINGS
# ========================================================================

section("VI. KEY FINDINGS")

print("""
1. PATTERN CRITERION (criterion, proved). A gate pattern S occurs among
   n=1..lambda iff prod(S) <= lambda. Frees the dynamical spectrum from
   the O(lambda*k) sweep: pruned subset enumeration reaches any rung
   whose admissible-pattern count is tractable -- the k=22 rung costs
   0.1 s, timed in section V's own sec column.

2. PLATEAU DECOMPOSITION (rule, proved algebraically; verified k=6,
   11..14, 18..22). Not a criterion: it is an IDENTITY between value
   sets, not a necessary-and-sufficient condition on anything.
   At a plateau, V_k = W union c*V_{k-1}, with W the old
   spectrum through the p_k window (budget lambda/p_k) and
   c = -1/(p_k-1) injective. The gain is EXACTLY the uncovered window:
   gain = |W| - |W intersect c*V_{k-1}|.

3. COLLISION CRITERION (criterion, proved). A window value s/D dies iff
   (p_k-1) | D and (-s, D/(p_k-1)) is an old value -- equivalently iff
   a multiplicative relation prod_A(q-1) = (p_k-1)*prod_B(q-1) holds
   over disjoint sets of old primes, |A|+|B| odd, within the lambda
   budget. Collisions are number theory: the multiplicative structure
   of the shifted primes q-1, the same objects that drive transparency.

4. WHAT CONTROLS THE GAIN (the opening question, answered). Two factors:
   the window size |W| (set by the budget lambda/p_k) and the collision
   rate, set by the relation richness of p_k - 1 over {q-1}. At k=11..14
   the windows are nearly equal (133/135/135/139), so the variation
   60/20/41/70 is almost entirely collision rate (55/85/70/50%). The
   extremes track direct factorability: 85% at k=12 (36 = 2*18 over the
   shifted primes) vs 50% at k=14 (42 = 2*3*7 has no direct
   representation -- every relation needs a nontrivial denominator
   side). But factorability alone is not the rate: 40 = 4*10 factors
   directly yet collides only 70% (k=13) -- the rate is the
   budget-weighted census of ALL relations. k=6 was total coverage of a
   3-value window. The SAME predicate sorts k=18..22, and is no more
   than a marker there either: 60 and 72 are directly representable
   over the shifted primes -- (7-1)*(11-1) and (2-1)*(7-1)*(13-1), both
   printed in section V -- and collide 91% and 92% (gains 350, 382);
   66, 70 and 78 have no direct representation and collide 55-60%
   (gains 1663-2257).

5. TRANSPARENT PRIMES ARE DOUBLY REDUNDANT (observation). A plateau
   means (p_k-1) | lambda -- p_k's dynamics embed in the existing orbit.
   The collision criterion shows the SPECTRAL side: when p_k - 1 also
   factors multiplicatively over {q-1}, PART of what the new gate
   contributes embeds in the rescaled old spectrum too. Part, never
   all: every plateau measured here past k=6 has a POSITIVE gain -- 92%
   of the window dies at k=21 against 50% at k=14, and only k=6's
   3-value window went entirely. Dynamical redundancy and spectral
   redundancy are separate layers, both driven by p-1.
""")

print("=" * 72)
print("  Done. Plateau collision mechanism settled.")
print("=" * 72)
