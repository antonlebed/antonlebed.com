"""A priori plateau collision RATE -- the residual open question left by
explore_plateau_collisions.py.

The mechanism (explore_plateau_collisions.py): at a plateau
the spectral gain is the uncovered window, and a window value dies iff a
multiplicative relation  prod_A(q-1) = (p_k - 1) * prod_B(q-1)  holds
over disjoint sets of old tower primes within the lambda budget. Open
residual: predict the collision RATE from the divisor structure of
p_k - 1 alone, without running the spectrum census.

What this script settles:

1. APPLICABILITY (criterion, proved). A window pattern S collides via
   relation (A, B) iff B subset S, A disjoint from S, and
   prod(S) <= lambda * prod(B) / prod(A). The collision set is EXACTLY
   the union of these explicit sets over all relations (both directions
   are an earlier derivation run forwards/backwards). The prime 2 is a
   PARITY MEMBER of A or B -- factor (2-1) = 1 in the product, cost 2
   in the prime budget. It is NOT a free toggle: the budget can block
   it (first caught at k=11: A = (3,7,11), B = (5) needs 2 in U to fix
   parity, and 2 * 51051 > lambda = 55440).

2. TRUNCATION COMPLETENESS (observation, k <= 22). Completeness at
   zero floor is the criterion itself (every collided value yields its
   own relation); the OBSERVATION is that the truncation loses
   nothing: |B| <= 3 with applicability bound >= 0.002 (power-of-two
   rounded) covers all 16,586 collided values across the 10 validation
   rungs, zero false hits. The deepest needed relations are |B| = 3,
   prod(B) ~ 10^5, killing one window value each (k=21).

3. CELL-SUM FORMULA (rule, pattern measure; proved + verified k <= 22).
   Within a fixed ON/OFF assignment (cell) of the ACTIVE primes (those
   appearing in any relation), every applicable relation's residual
   condition is a pure budget threshold -- thresholds are NESTED, so
   the within-cell union is one threshold, and

     patrate = (1/N(b)) * sum_cells count(inactive, t_c / prod(ON(c)))

   with N(x) = #patterns of prime-product <= x, b = lambda/p_k,
   t_c = max over applicable relations of min(b, lam*prod(B)/prod(A)).
   The pattern-collision rate is a CLOSED COUNTING COMPUTATION -- no
   spectrum enumeration. Matches the measured pattern rate exactly at
   every k <= 22.

4. VALUE BIAS (observation). The census rate counts distinct VALUES;
   the formula counts PATTERNS. Collided values carry more representing
   patterns, so cellsum >= value rate, gap 0.00-0.24 over the census.
   OUT-OF-SAMPLE HIT at k=37: predicted 0.74..0.98 from cell-sum
   0.98 BEFORE any k=37 spectrum existed; measured value rate 0.916
   (bias 0.06).

5. DIRECT FACTORABILITY REFUTED AT SCALE (observation). k=31, 34, 36
   have ZERO direct representations of p_k - 1 over {q-1} yet collide
   64-84% -- the small-k story "factorability marks the extremes" was
   window poverty, not law. In rich windows the B != empty relations
   (window patterns that already contain B) carry the rate.

Census: 18 plateau rungs k = 6..37 (was 10 through k <= 22). Spectra
are enumerated as signed denominators s*e (machine-word ints, not
(sign, ~10^56-bigint) tuples) -- the k=37 census holds 4.7M values and
stays under the 512MB line; big-rung spectra are never retained.

Run: python prime/code/explore_plateau_rate.py        (~13 min: the
k=36/37 value censuses and their cell-sum rows dominate)
"""

from math import prod, lcm
from time import perf_counter
from crt import is_prime


def section(title):
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}")


def first_n_primes(n):
    primes, c = [], 2
    while len(primes) < n:
        if is_prime(c):
            primes.append(c)
        c += 1
    return primes


def tower_lambda(primes):
    r = 1
    for p in primes:
        r = lcm(r, p - 1)
    return r


def count_patterns(qs, budget):
    """#subsets S of qs with prod(S) <= budget (full-subtree shortcut)."""
    if budget < 1:
        return 0
    qs = sorted(qs)
    n = len(qs)
    # suffix products, capped RELATIVE to the budget: any value above
    # budget compares identically for every recursive sub-budget, so
    # budget + 1 is exact at any scale (a fixed cap like 2^62 would be
    # silently outgrown -- k=40's window budget is already 0.26 * 2^62)
    CAP = budget + 1
    suffix = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = min(CAP, suffix[i + 1] * qs[i])

    def rec(i, b):
        if i == n:
            return 1
        if suffix[i] <= b:
            return 1 << (n - i)
        total = rec(i + 1, b)
        if qs[i] <= b:
            total += rec(i + 1, b // qs[i])
        return total

    return rec(0, budget)


def spectrum(primes, budget, collect_patterns=False):
    """Distinct F values (s, D) by pruned subset DFS (pattern criterion).

    With collect_patterns: also every admissible pattern as
    (ON-set, prod, value)."""
    k = len(primes)
    phi = prod(p - 1 for p in primes)
    values = {}
    pats = [] if collect_patterns else None

    def rec(i, pr, e, sel):
        if i == k:
            d = phi // e
            s = -1 if (k - len(sel)) % 2 else 1
            v = (s, d)
            if v not in values:
                values[v] = tuple(sel)
            if collect_patterns:
                pats.append((tuple(sel), pr, v))
            return
        p = primes[i]
        rec(i + 1, pr, e, sel)
        if pr * p <= budget:
            sel.append(p)
            rec(i + 1, pr * p, e * (p - 1), sel)
            sel.pop()

    rec(0, 1, 1, [])
    return values, pats


def spectrum_set(primes, budget):
    """Distinct F values as SIGNED DENOMINATORS: value (s, D) with
    D = phi/e, e = prod(p-1 over the ON primes), is stored as s*e.
    e <= budget <= lambda (< 2^62 through K_CENSUS=37; a bump past a
    lambda jump only costs int width), so the set holds machine-word ints
    instead of (sign, ~10^56-bigint) tuples -- the big censuses stay
    under the 512MB line -- and the DFS leaf skips the phi//e division
    (~300M leaves at k=37)."""
    k = len(primes)
    out = set()

    def rec(i, pr, e, m):
        if i == k:
            out.add(e if (k - m) % 2 == 0 else -e)
            return
        p = primes[i]
        rec(i + 1, pr, e, m)
        if pr * p <= budget:
            rec(i + 1, pr * p, e * (p - 1), m + 1)

    rec(0, 1, 1, 0)
    return out


def find_A(target, qs, prime_budget, forbid):
    """Subsets A of qs (not in forbid) with prod(q-1 for q in A) == target
    and prod(A) <= prime_budget. q = 2 may join A: factor (2-1) = 1 in
    the product, cost 2 in the budget -- the parity member, never free."""
    cand = [q for q in qs if q not in forbid]
    out = []

    def rec(i, rem, pb, sel):
        if rem == 1 and sel:
            out.append(tuple(sel))
            # no return: q=2 (factor 1) may still extend a complete A
        for j in range(i, len(cand)):
            q = cand[j]
            qm1 = q - 1
            if qm1 > rem:
                break
            if rem % qm1 == 0 and q <= pb:
                sel.append(q)
                rec(j + 1, rem // qm1, pb // q, sel)
                sel.pop()

    rec(0, target, prime_budget, [])
    return out


def relations(old_primes, p_new, lam, ub_floor=0.002, bmax=3):
    """All relations (A, B): disjoint subsets of old primes (2 allowed in
    either, as parity member), |A| + |B| odd, prod_A(q-1) =
    (p_new - 1) * prod_B(q-1), kept when the applicability upper bound
    N(b_r / prod(B)) / N(b) >= ub_floor. Returns [(A, B, ub)],
    ub-descending.

    Budgets for the bound are rounded UP to the next power of two:
    N is monotone, so the bound stays an upper bound, and the counting
    collapses to ~50 cached calls per rung (a raw N(x) costs ~1 s at
    k=30's budgets; thousands of distinct budgets would hang)."""
    b = lam // p_new
    n_total = count_patterns(old_primes, b)
    pm1 = p_new - 1
    cache = {}

    def n_all(budget):
        if budget >= b:
            return n_total
        budget = 1 << max(0, budget).bit_length()   # round up to 2^e
        if budget not in cache:
            cache[budget] = count_patterns(old_primes, min(b, budget))
        return cache[budget]

    rels = []

    def b_sets(i, pr, sel):
        if n_all(b // pr) / n_total < ub_floor:
            return
        yield list(sel), pr
        if len(sel) >= bmax:
            return
        for j in range(i, len(old_primes)):
            q = old_primes[j]
            if pr * q > b:
                break
            sel.append(q)
            yield from b_sets(j + 1, pr * q, sel)
            sel.pop()

    for B, prB in b_sets(0, 1, []):
        target = pm1 * prod(q - 1 for q in B)
        for A in find_A(target, old_primes, lam, set(B)):
            if (len(A) + len(B)) % 2 == 0:
                continue
            b_r = min(b, lam * prod(B) // prod(A))
            ub = n_all(b_r // prB) / n_total
            if ub >= ub_floor:
                rels.append((tuple(A), tuple(B), ub))
    rels.sort(key=lambda r: -r[2])
    return rels


def cell_sum(old_primes, p_new, lam, rels):
    """Exact pattern-measure of the relation union, by cell DFS over the
    active primes. Within a cell the applicable relations reduce to one
    budget threshold (nested), so each leaf is one counting call."""
    b = lam // p_new
    active = sorted({q for A, B, _ in rels for q in A + B})
    act_set = set(active)
    inactive = [q for q in old_primes if q not in act_set]
    n_total = count_patterns(old_primes, b)
    rbud = [(set(A), set(B), min(b, lam * prod(B) // prod(A)))
            for A, B, _ in rels]
    leaf_cache = {}

    def count_inactive(budget):
        if budget not in leaf_cache:
            leaf_cache[budget] = count_patterns(inactive, budget)
        return leaf_cache[budget]

    total = 0

    def rec(i, prc, live):
        nonlocal total
        if not live:
            return
        if i == len(active):
            t = max(br for _, _, br in live)
            total += count_inactive(t // prc)
            return
        q = active[i]
        rec(i + 1, prc, [r for r in live if q not in r[1]])   # q OFF
        if prc * q <= b:
            rec(i + 1, prc * q, [r for r in live if q not in r[0]])  # ON
    rec(0, 1, rbud)
    return total / n_total


K_CENSUS = 37     # value-census ceiling (k=36/37 spectra ~2-3 min each)
K_VALIDATE = 22   # pattern-level exact validation ceiling
T_CAP = 300       # cell-sum relation cap for the big rungs
ALL = first_n_primes(40)
PLATEAUS = [k for k in range(4, 41)
            if tower_lambda(ALL[:k]) == tower_lambda(ALL[:k - 1])]


# ========================================================================
# I. CENSUS -- collision rate + the two gates, all plateau rungs k <= 37
# ========================================================================

section("I. CENSUS k <= 37: rate + gates (was k <= 22 in an earlier run)")

print("""
  Gate A (divisibility): (p_k - 1) | D for window value (s, D).
  Gate B (realization):  (-s, D/(p_k - 1)) is an old value.
  rate = P[A and B]. Neither gate alone is the rate.
""")

# measured anchors (regression check, like the sibling script's own
# frozen gain table): an earlier census covered k <= 36; k=37 was
# measured in a later out-of-sample test, first computed via the
# (s, D)-tuple census
RATE_ANCHORS = {6: 1.00, 11: 0.55, 12: 0.85, 13: 0.70, 14: 0.50,
                18: 0.91, 19: 0.60, 20: 0.57, 21: 0.92, 22: 0.55,
                24: 0.75, 30: 0.80, 31: 0.83, 32: 0.70, 33: 0.55,
                34: 0.64, 36: 0.84, 37: 0.916}

print(f"  {'k':>3} {'p-1':>5} {'|W|':>9} {'collide':>9} {'rate':>6} "
      f"{'P[A]':>6} {'P[B|A]':>7} {'sec':>6}")
print(f"  {'-' * 58}")

census = {}      # k -> collided (s, D) set at k <= K_VALIDATE, else None
for k in PLATEAUS:
    if k > K_CENSUS:
        break
    ps = ALL[:k]
    p_new = ps[-1]
    old = ps[:-1]
    lam = tower_lambda(ps)
    pm1 = p_new - 1
    phi = prod(p - 1 for p in old)
    t0 = perf_counter()
    old_vals = spectrum_set(old, lam)
    window = spectrum_set(old, lam // p_new)
    n_a = n_ab = 0
    collided = set() if k <= K_VALIDATE else None
    for se in window:
        e = abs(se)
        # gate A: (p_k - 1) | D for D = phi/e  <=>  e*(p_k - 1) | phi
        if phi % (e * pm1) == 0:
            n_a += 1
            # gate B: (-s, D/(p_k - 1)) is an old value <=> denominator
            # e*(p_k - 1) with flipped sign is in the old spectrum
            if -se * pm1 in old_vals:
                n_ab += 1
                if collided is not None:
                    collided.add((1 if se > 0 else -1, phi // e))
    el = perf_counter() - t0
    nw = len(window)
    rate = n_ab / nw
    census[k] = collided
    del old_vals, window      # big-rung spectra are never retained
    print(f"  {k:>3} {pm1:>5} {nw:>9,} {n_ab:>9,} {rate:>6.2f} "
          f"{n_a / nw:>6.2f} {n_ab / n_a:>7.2f} {el:>6.1f}", flush=True)
    assert abs(rate - RATE_ANCHORS[k]) < 0.005, \
        f"k={k}: rate {rate:.3f} drifted from anchor {RATE_ANCHORS[k]}"

print("\n  18 plateau rungs. Rates span 0.50-1.00; both gates vary")
print("  (P[A] 0.68-1.00, P[B|A] 0.60-1.00) -- neither is the rate.")


# ========================================================================
# II. DIRECT FACTORABILITY DOES NOT SCALE
# ========================================================================

section("II. DIRECT REPS OF p_k - 1 OVER {q-1}: refuted as the driver")

print(f"\n  {'k':>3} {'p-1':>5} {'rate':>6} {'#reps':>6}  representations")
print(f"  {'-' * 64}")
for k in census:
    ps = ALL[:k]
    p_new = ps[-1]
    odd = [q for q in ps[:-1] if q > 2]
    reps = find_A(p_new - 1, odd, 1 << 62, set())
    rep_strs = ["*".join(f"({q}-1)" for q in a) for a in reps]
    print(f"  {k:>3} {p_new - 1:>5} {RATE_ANCHORS[k]:>6.2f} {len(reps):>6}  "
          f"{'; '.join(rep_strs) if rep_strs else '-'}")

print("""
  k <= 22 suggested "factorable p-1 collides 85-92%, unfactorable
  50-60%". The extension kills it: k=31 (126), k=34 (138), k=36 (150)
  have ZERO direct reps yet collide 83% / 64% / 84%. Rich windows have
  many patterns already containing B, so B != empty relations do the
  work that direct (B = empty) relations do in poor windows.
""")


# ========================================================================
# III. THE RELATION UNION IS THE COLLISION SET, VALUE-EXACTLY
# ========================================================================

section("III. RELATION UNION vs CENSUS (value-exact at k <= 22)")

print("""
  Relation (A, B) applies to window pattern S iff B subset S, A disjoint
  S, prod(S) <= lambda*prod(B)/prod(A); |A|+|B| odd with 2 as a BUDGETED
  parity member. Union over the truncated enumeration (|B| <= 3,
  bound >= 0.002) vs the true collided set:
""")

print(f"  {'k':>3} {'p-1':>5} {'#rel':>5} {'union':>7} {'census':>7} "
      f"{'missed':>6} {'false':>6} {'patrate':>8} {'mu1':>5}")
print(f"  {'-' * 58}")

patrates = {}
rels_at = {}
for k in census:
    if k > K_VALIDATE:
        continue
    ps = ALL[:k]
    p_new = ps[-1]
    old = ps[:-1]
    lam = tower_lambda(ps)
    rels = relations(old, p_new, lam)
    rels_at[k] = rels
    _, pats = spectrum(old, lam // p_new, collect_patterns=True)
    truly = census[k]

    hit = set()
    pat_hits = 0
    for S, prS, v in pats:
        sS = set(S)
        for A, B, _ in rels:
            if set(B) <= sS and not sS & set(A) \
                    and prS * prod(A) <= lam * prod(B):
                pat_hits += 1
                hit.add(v)
                break
    false_hits = len(hit - truly)
    missed = len(truly - hit)
    patrates[k] = pat_hits / len(pats)

    # exact top applicability: mu_r = count(old - A - B, b_r/prodB)/N(b)
    # over the 50 best bound-candidates (the bounds in rels are rounded
    # upper bounds, not measures)
    b = lam // p_new
    n_total = count_patterns(old, b)
    mu1 = max(count_patterns([q for q in old if q not in A + B],
                             min(b, lam * prod(B) // prod(A)) // prod(B))
              / n_total
              for A, B, _ in rels[:50])
    print(f"  {k:>3} {p_new - 1:>5} {len(rels):>5} {len(hit):>7} "
          f"{len(truly):>7} {missed:>6} {false_hits:>6} "
          f"{patrates[k]:>8.2f} {mu1:>5.2f}")
    assert false_hits == 0, f"k={k}: relation hit a non-collided value"
    assert missed == 0, f"k={k}: truncation missed {missed} collisions"

total_collided = sum(len(c) for c in census.values() if c is not None)
print(f"""
  missed = 0 and false = 0 at every rung: the truncated a priori
  enumeration IS the collision set, value for value ({total_collided:,}
  collided values across the 10 rungs). (patrate = fraction of window
  PATTERNS hit -- the formula's native measure, used in IV.)
""")


# ========================================================================
# IV. THE CELL-SUM FORMULA
# ========================================================================

section("IV. CELL-SUM: pattern rate exactly, value rate to a known bias")

print("""
  patrate = (1/N(b)) * sum over cells c of the active primes of
            count(inactive, t_c / prod(ON(c)))
  -- counting only, no spectrum. Exactness check (vs III), then the full
  table with the value bias. Big rungs use the top-%d relations by
  applicability bound (cap checked against the full union at k <= 24:
  asserted to lose < 0.02).
""" % T_CAP)

print(f"  {'k':>3} {'p-1':>5} {'#rel':>6} {'used':>5} {'cellsum':>8} "
      f"{'patrate':>8} {'rate':>6} {'bias':>6} {'sec':>6}")
print(f"  {'-' * 60}")

for k in census:
    ps = ALL[:k]
    p_new = ps[-1]
    old = ps[:-1]
    lam = tower_lambda(ps)
    t0 = perf_counter()
    # big rungs: floor 0.01 -- the top-T_CAP bounds sit far above it,
    # and the fine tail only slows the enumeration
    rels = rels_at.get(k) or relations(old, p_new, lam,
                                       ub_floor=0.01 if k >= 30 else 0.002)
    used = rels[:T_CAP]
    cs = cell_sum(old, p_new, lam, used)
    full = cs
    if k <= 24 and len(rels) > T_CAP:
        full = cell_sum(old, p_new, lam, rels)
        assert full - cs < 0.02, \
            f"k={k}: T_CAP={T_CAP} loses {full - cs:.3f} of the union"
    el = perf_counter() - t0
    pr = patrates.get(k)
    pr_s = f"{pr:>8.2f}" if pr is not None else f"{'-':>8}"
    rate = RATE_ANCHORS[k]
    print(f"  {k:>3} {p_new - 1:>5} {len(rels):>6} {len(used):>5} "
          f"{cs:>8.2f} {pr_s} {rate:>6.2f} {cs - rate:>6.2f} {el:>6.1f}",
          flush=True)
    if pr is not None:
        # THE exactness claim: the full cell-sum equals the measured
        # pattern-union rate to float precision (same integers, same
        # denominator) -- not merely within a tolerance
        assert abs(full - pr) < 1e-9, \
            f"k={k}: full cell-sum {full!r} != measured patrate {pr!r}"
    assert cs >= rate - 0.005, \
        f"k={k}: cell-sum below the value rate (bias sign violated)"

print("""
  k=37 OUT-OF-SAMPLE TEST (predicted at floor 0.002, before any
  k=37 spectrum existed: cell-sum 0.98 -> value rate 0.74..0.98;
  measured in a later run): rate 0.916 -- HIT. Bias 0.06 against the predicted
  cell-sum (the capped row above subtracts unrounded and prints 0.07);
  inside the observed 0.00-0.24 band either way.""")


# ========================================================================
# V. KEY FINDINGS
# ========================================================================

section("V. KEY FINDINGS")

print("""
1. APPLICABILITY CRITERION (criterion, proved). Window pattern S
   collides via relation (A, B) iff B subset S, A disjoint S, and
   prod(S) <= lambda*prod(B)/prod(A). The collision set is exactly the
   union of these sets over the relations of p_k - 1. The prime 2 is a
   BUDGETED parity member (factor 1, cost 2) -- not a free toggle.

2. TRUNCATION COMPLETENESS (observation, k <= 22). Complete at zero
   floor by the criterion; at floor 0.002 (power-of-two rounded) with
   |B| <= 3 the union covers all 16,586 collided values over the 10
   validation rungs, zero false hits.

3. CELL-SUM FORMULA (rule, verified k <= 22). The pattern-collision
   rate is exactly a nested-threshold sum of counting functions over
   active-prime cells -- a closed a priori computation from the
   relation census of p_k - 1; no spectrum enumeration. Matches the
   measured pattern rate at every validation rung.

4. VALUE BIAS (observation, all 18 rungs). cellsum >= value rate
   always; gap 0.00-0.24, largest when the rate is low (collided
   values carry more representing patterns than survivors).
   As a value-rate predictor the formula is PATTERN-tier: it tracks
   (high cellsum -> high rate) with a known one-sided bias.
   OUT-OF-SAMPLE HIT at k=37: predicted 0.74..0.98 before any
   k=37 spectrum existed; measured 0.916, bias 0.06.

5. DIRECT FACTORABILITY REFUTED AT SCALE (observation). Zero direct
   reps at k=31/34/36 yet rates 0.83/0.64/0.84. What sets the rate is
   the budget-weighted relation census -- in rich windows dominated by
   B != empty relations -- not the factorability of p_k - 1 over {q-1}
   per se. The k <= 22 factorability story was window poverty.

6. UNIVERSALITY OF THE TOP APPLICABILITY (observation, k <= 22). The
   largest single-relation applicability (mu1 in III, exact) is
   0.20-0.23 at every validation rung past k=6 (0.33 at k=6's 3-value
   window) -- essentially the membership probability of the cheapest
   B prime in the pattern ensemble, a property of the budget, not of
   p_k. (Big rungs report only rounded upper bounds; exact mu
   unmeasured there.)
""")

print("=" * 72)
print("  Done. Collision rate: exact in pattern measure, pattern-tier")
print("  (one-sided bias 0.00-0.24) in value measure.")
print("=" * 72)
