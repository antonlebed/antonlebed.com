"""
Linnik-ordering injectivity at scale.

A prime q enters lambda at the rung of L(q) = the least prime p with
p = 1 (mod q)  (Linnik's function): the first rung whose p_k - 1 it
divides. The Linnik ordering is INJECTIVE iff no two primes enter at
the same rung, i.e. no prime p exists whose p-1 has two prime factors
q1, q2 such that p = L(q1) = L(q2) simultaneously.

Reformulation that scales: walk primes p in increasing order, factor
p-1 (smallest-prime-factor sieve), count the never-before-seen prime
factors. Injectivity <=> that count is <= 1 at every rung. This
replaces the per-q search of explore_lambda_tower.py (k<=50) with one
sieve pass: k up to pi(N).

Sections:
  I.   Injectivity scan k = 1 .. pi(N)        (rule)
  II.  Entry statistics + nearest misses      (observation)
  III. Why no collision should ever occur     (heuristic, Cramer-style)

FINDINGS (run at N = 5*10^7, k_max = pi(N) = 3,001,134):
  1. (rule) The Linnik ordering is injective through k = 3,001,134
     (all primes p <= 5*10^7): no rung introduces two new lambda
     primes. Extends the k<=50 check by ~5 orders of magnitude.
     414,894 introductions (13.8% of rungs; rate falls 0.50 -> 0.13
     by decade of k).
  2. (property) A collision at rung p requires p = 1 (mod 2*q1*q2),
     so p >= 2*q1*q2 + 1, and BOTH q's must have survived unhit
     through all earlier rungs. q = 2 can never collide: it enters at
     rung 2 (p = 3, p-1 = 2) alone, by inspection.
  3. (observation) Near misses DIE OUT: call an introduction
     non-trivial when some other factor q2 of the same p-1 entered
     past rung 0.1*k, i.e. outside the first 10% of the tower below
     it (gap < 0.9k; gap 0 = collision). Only 9 such events exist
     in the whole scan, ALL at k <= 43 (last: p = 191, new q = 19,
     with q = 5 entered at rung 5). Past k = 43 every new prime
     enters alongside co-factors settled in the first decades of the
     tower -- the two-simultaneous-late-entries event a collision
     requires never comes close again. Structurally: the new prime
     is the largest factor of p-1 in ALL 414,894 introductions
     (an exception = ONE anomalously late prime; a collision needs
     two at once, a squared rarity).
  4. (heuristic) Cramer/Dirichlet model: primes = 1 (mod q) have
     density 1/(q-1); a pair (q1, q2) collides only if the first
     prime = 1 (mod q1*q2) precedes every single hit. Size floor
     (a hit = 1 mod m needs p > m) gives
        P(q1, q2 collide) ~ exp(-(q1+q2-2)/ln(q1*q2)) / (q1+q2-1).
     A priori expected collisions, summed over odd pairs q <= 229,
     is 0.0439 (converged: the tail beyond adds ~1.5*10^-14), dominated
     by the tiniest pairs ((3,5): 0.016) -- and those pairs are
     settled collision-free by computation.
     Conditioned on the horizon (every q with L(q) <= N is settled;
     smallest unseen q = 470,941), expected FUTURE collisions
     ~ exp(-q_b/ln(q_a*q_b)) for the two smallest unseen q's
     ~ 10^-8031: effectively zero. (The sum over ALL unseen pairs is
     dominated by its smallest term -- the pair count multiplies by
     fewer than ~15 orders of magnitude, irrelevant at this scale.)
  5. (observation) Entry rung grows near-linearly: windowed fits give
     E(q) ~ q^0.96..0.98 for q from 10 to 10^6; the top window
     (q > 10^6) is censored -- its late entrants exceed the horizon.
     Supersedes the censored global ~0.7 of explore_prime_gaps.py.

Tier: rule (verified exhaustively k <= 3,001,134); "always injective"
stays a conjecture with heuristic support. Not a proof: a collision
remains logically possible; the model says it requires two large
primes to dodge ~q_other/ln(q1*q2) independent hits each, jointly.

Resource: peak commit 355 MB at N = 5*10^7 (memwatch-verified),
wall ~4 s. N is a CLI arg: `python explore_linnik_injectivity.py
[N]` (default 50000000). OPENBLAS_NUM_THREADS=1 is set before the
numpy import -- otherwise OpenBLAS reserves ~730 MB of thread-arena
commit that memwatch (rightly) counts.
"""

import os
import sys
from math import isqrt, log, exp

# No BLAS used here -- without this, OpenBLAS reserves ~730 MB of
# per-thread arena COMMIT on import and trips the memwatch ceiling.
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np


def spf_sieve(n):
    """Smallest-prime-factor sieve, int32. spf[m]==0 <=> m prime (m>=2)."""
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, isqrt(n) + 1):
        if spf[i] == 0:
            sl = spf[i * i :: i]
            sl[sl == 0] = i
    return spf


def factor_distinct(m, spf):
    """Distinct prime factors of m via SPF division."""
    out = []
    while m > 1:
        q = int(spf[m])
        if q == 0:
            q = m
        out.append(q)
        while m % q == 0:
            m //= q
    return out


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 50_000_000

    print(f"LINNIK-ORDERING INJECTIVITY (primes p <= {N:,})")
    print("=" * 72)
    print()

    spf = spf_sieve(N)
    primes = (np.flatnonzero(spf[2:] == 0) + 2).astype(np.int64)
    k_max = len(primes)
    print(f"pi({N:,}) = {k_max:,} rungs")
    print()

    # entry_rung[q] = rung index (1-based) at which prime q entered
    # lambda; 0 = not yet entered. q <= (N-1)//2 possible at most.
    entry_rung = np.zeros(N // 2 + 2, dtype=np.int32)

    # --- I. The scan ---
    print("I. INJECTIVITY SCAN")
    print("-" * 72)

    collisions = []          # (k, p, [new qs])  -- expected empty
    intro_count = 0
    new_is_largest = 0       # intros where the new prime tops p-1
    nontrivial = []          # gaps < 0.9k: (gap, k, p, q_new, q_prev)
    decade_stats = {}        # decade -> [rungs, intros]
    small_entry = {}         # q -> (k, p) for q < 100 (doc-facing facts)

    CHUNK = 200_000
    for base in range(0, k_max, CHUNK):
        chunk = primes[base : base + CHUNK].tolist()
        for j, p in enumerate(chunk):
            k = base + j + 1
            if p == 2:
                continue
            qs = factor_distinct(p - 1, spf)
            new_qs = [q for q in qs if entry_rung[q] == 0]
            if len(new_qs) >= 2:
                collisions.append((k, p, new_qs))
                print(f"  *** COLLISION at k={k:,}, p={p:,}: {new_qs} ***")
            d = len(str(k)) - 1
            st = decade_stats.setdefault(d, [0, 0])
            st[0] += 1
            st[1] += len(new_qs)
            if new_qs:
                intro_count += len(new_qs)
                if new_qs[0] == max(qs):
                    new_is_largest += 1
                for q in new_qs:
                    entry_rung[q] = k
                    if q < 100:
                        small_entry[q] = (k, p)
                # nearest-miss bookkeeping: how recently did the other
                # factors of p-1 enter?  gap 0 would be a collision.
                for q2 in qs:
                    if q2 in new_qs:
                        continue
                    gap = k - int(entry_rung[q2])
                    if gap < 0.9 * k:
                        nontrivial.append((gap, k, p, new_qs[0], q2))

    if collisions:
        print(f"  RESULT: {len(collisions)} collision(s) found -- "
              "injectivity FAILS (a finding!)")
    else:
        print(f"  RESULT: injective through k = {k_max:,} "
              f"(no rung introduces two new lambda primes)")
    print(f"  primes introduced: {intro_count:,} "
          f"({100*intro_count/k_max:.1f}% of rungs introduce one)")
    print()

    # sanity anchors (must match explore_lambda_tower.py k<=50 facts)
    assert small_entry[11][1] == 23 and small_entry[7][1] == 29, \
        "Linnik inversion 11<7 lost"
    assert small_entry[23][1] == 47 and small_entry[13][1] == 53, \
        "Linnik inversion 23<13 lost"
    assert small_entry[17][1] == 103, "q=17 must enter via p=103"
    assert all(k > 50 for k, _, _ in collisions), \
        "collision at k<=50 contradicts explore_lambda_tower.py"

    # --- II. Entry statistics + nearest misses ---
    print("II. ENTRY STATISTICS")
    print("-" * 72)
    print(f"  {'rungs k in':>20} {'intro rate':>11}")
    for d in sorted(decade_stats):
        rungs, intros = decade_stats[d]
        lo = 10 ** d
        print(f"  {lo:>9,}..{min(10**(d+1)-1, k_max):>9,} "
              f"{intros/rungs:>10.3f}")
    print(f"  new prime = largest factor of p-1 in {new_is_largest:,} "
          f"of {intro_count:,} introductions")
    print("  (an exception = ONE anomalously late prime; a collision "
          "needs two at once)")
    print()

    nontrivial.sort(key=lambda t: t[1])
    print(f"  NON-TRIVIAL NEAR MISSES (co-factor entered past rung "
          f"0.1k; gap 0 = collision): {len(nontrivial)} total")
    for gap, k, p, q1, q2 in nontrivial[:20]:
        print(f"    k={k:>6,} p={p:>9,}: q={q1:,} enters; "
              f"q={q2:,} entered rung {k-gap:,} (gap {gap:,})")
    if len(nontrivial) > 20:
        print(f"    ... ({len(nontrivial)-20} more)")
    last_nt_k = nontrivial[-1][1] if nontrivial else None
    min_gap = min(nontrivial)[0] if nontrivial else None
    print(f"  last near miss at k = {last_nt_k:,} -- past it, every "
          f"co-factor of an")
    print(f"  introduction settled in the first 10% of the tower below it")
    print()

    # smallest primes still unseen at the horizon
    qs_all = primes[primes <= N // 2]
    unseen = qs_all[entry_rung[qs_all] == 0]
    print(f"  unseen primes q <= N/2 at horizon: {len(unseen):,}; "
          f"smallest: {[int(q) for q in unseen[:5]]}")
    q_a, q_b = (int(unseen[0]), int(unseen[1])) if len(unseen) >= 2 \
        else (None, None)
    print()

    # entry-rung growth: windowed power-law fit E(q) ~ q^a.  Windows
    # avoid the censoring bias that a single global fit suffers (late
    # entrants beyond the horizon are missing from the sample -- the
    # bias that put explore_prime_gaps.py's old global fit at ~0.7).
    ent_mask = entry_rung[qs_all] > 0
    ent_q = qs_all[ent_mask].astype(np.float64)
    ent_k = entry_rung[qs_all][ent_mask].astype(np.float64)
    print("  ENTRY-RUNG GROWTH, windowed fit E(q) ~ q^a:")
    for lo, hi, note in [(10.0, 1e3, ""), (1e3, 1e5, ""), (1e5, 1e6, ""),
                         (1e6, N / 2, "  (censored: late entrants "
                                      "exceed the horizon)")]:
        m = (ent_q >= lo) & (ent_q < hi)
        if int(m.sum()) < 10:
            continue
        a = np.polyfit(np.log(ent_q[m]), np.log(ent_k[m]), 1)[0]
        print(f"    q in [{lo:>9,.0f}, {hi:>12,.0f}): a = {a:.3f}  "
              f"(n={int(m.sum()):,}){note}")
    print()

    # --- III. Heuristic: why no collision should ever occur ---
    print("III. CRAMER-STYLE HEURISTIC")
    print("-" * 72)
    print("  P(pair q1,q2 collide) ~ exp(-(q1+q2-2)/ln(q1*q2)) / (q1+q2-1)")
    print("  (no single hit below the first joint hit; joint hits need")
    print("   p > q1*q2, by which point each q faces ~q_other/ln(q1*q2)")
    print("   independent 1/(q-1) trials)")
    print()

    small_qs = [int(q) for q in primes[1:50]]   # odd primes; 2 excluded
    expected = 0.0
    top_pairs = []
    for i, q1 in enumerate(small_qs):
        for q2 in small_qs[i + 1:]:
            pp = exp(-(q1 + q2 - 2) / log(q1 * q2)) / (q1 + q2 - 1)
            expected += pp
            top_pairs.append((pp, q1, q2))
    top_pairs.sort(reverse=True)
    print(f"  a priori expected collisions, all odd pairs q <= "
          f"{small_qs[-1]}: {expected:.4f}")
    print("  (converged: the tail beyond q = 229 adds ~1.5*10^-14)")
    print("  dominated by the smallest pairs (all settled clean by I):")
    for pp, q1, q2 in top_pairs[:4]:
        print(f"    ({q1},{q2}): {pp:.5f}")
    print()

    if q_a is not None:
        log10_tail = -(q_b - 1) / log(q_a * q_b) / log(10)
        print(f"  beyond the horizon every candidate pair has both "
              f"q >= {q_a:,}:")
        print(f"  expected future collisions ~ 10^{log10_tail:,.0f}")
        print("  (sum over all unseen pairs ~ its smallest term; the "
              "pair count adds")
        print("   fewer than ~15 orders -- irrelevant at this scale)")
    print()

    print("=" * 72)
    print("FINDINGS")
    print(f"  1. (rule)     injective through k = {k_max:,} "
          f"({'0 collisions' if not collisions else 'FAILED'})")
    print(f"  2. (property) collision at p needs p >= 2*q1*q2 + 1; "
          f"q=2 enters rung 2 solo")
    print(f"  3. (observation) near misses die out: {len(nontrivial)} "
          f"total, last at k = {last_nt_k:,}; min gap {min_gap}")
    print(f"  4. (heuristic) future-collision expectation "
          f"~ 10^{log10_tail:,.0f} -- effectively impossible, but not "
          f"a proof")
    print(f"  5. (observation) entry rung near-linear: E(q) ~ "
          f"q^0.96..0.98 in uncensored windows")


if __name__ == "__main__":
    main()
