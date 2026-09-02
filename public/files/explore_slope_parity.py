"""Why the census's numerator carries every factor of 2 its modulus
does: the parity of n is the deep-saturation filter's, and it is
decided one multiple of g at a time.

THE QUESTION. explore_slope_arc.py moved the step's oddness off the
carry and onto the modulus: step = n (mod 2) at every even-radix pair,
n = N/g is odd at all 3516 below-cut pairs, and n is odd exactly when
2^v2(N) divides u -- the joint (v2(N), v2(u)) over that population
never once puts v2(u) below v2(N). Its N7 left the reason open as a
question about which CELLS the census admits, not about the carry.
This file asks that question of the census's own filters: the
interval-mismatch condition, the pre-period floor, the below-count and
the measure cut. Which of them forbids an even n, and is the parity a
fact about the below-cut population or about every cell the census
forms at all?

Notation is the family's, at phase 0: N = v.b^c, u = q, g = gcd(u, N),
n = N/g, I = [lo, hi] the winning interval with E = floor(a(N-u)/(b-1)),
wtop = (a r_c + 1)v - 1, wbot = -a r_c v, hi = min(E, wtop),
lo = max(-E, wbot), span = hi - lo + 1, A the saturated classes mod g
(those whose n residues all have a representative in I), f(t) = b.t
(mod g) the class map, J the least j with 2a r_j + 1 >= n, and a class
DEEP-SATURATED when its orbit is unsaturated only inside its
pre-period and below J.

THE DERIVATION, hand-attacked on paper before this engine existed.

(A) THE MODULUS DIVIDES b^c. The census's u are those with gcd(u, v) = 1
    and gcd(u, N) = g, so gcd(g, v) = 1, and g | N = v.b^c gives
    g | b^c. Hence b^c = 0 (mod g), the class map t -> b.t (mod g)
    sends every class to the fixed point 0 within c steps, and the
    orbit's cycle is the single class 0. A class is deep-saturated
    only if 0 is SATURATED: an unsaturated class on the cycle recurs
    at every large j.

(B) THE UNSATURATED BLOCK IS THE COMPLEMENT OF I IN ONE PERIOD. The
    unsaturated classes are the residues mod g of the integers
    strictly between hi and N + lo -- the N - span integers of the
    period [lo, N + lo) that I does not cover -- fewer than g of them
    at any cell that carries a mismatch at all, so the block holds at
    most one multiple of g. Class 0 is unsaturated iff a multiple of g
    lies strictly between hi and N + lo.

(C) THE BLOCK CONTAINS N/2 AT EVERY EVEN-RADIX CELL. An even radix has
    2a >= b (2a + 1 >= b with b even), and then a r_c >= b^c / 2, so
    wtop >= N/2 + v - 1 >= N/2 and -wbot >= N/2. The interval's three
    branches: where E <= wtop and E <= -wbot, I = [-E, E] with 2E + 1 =
    span < N, so hi = E < N/2 and lo = -E > -N/2; where wtop <= E,
    span >= 2 wtop + 1 > N, and where -wbot <= E, span >= 2(-wbot) + 1
    > N -- neither branch has a cell. So every cell is symmetric,
    hi < N/2 < N + lo, and N/2 lies in the block.

(D) SO n IS ODD AT EVERY EVEN-RADIX CELL, BY PROPERTY. N/2 = g.(n/2)
    is a multiple of g exactly when n is even; then by (C) it lies in
    the block, by (B) class 0 is unsaturated, and by (A) no class is
    deep-saturated -- the cell carries nothing and the census never
    forms it. The below-count and the measure cut enter nowhere: the
    parity is decided before either is read, at every below-count
    threshold, and the whole census -- not the below-cut population --
    has n odd. In the parent's terms: n odd means g carries every
    factor of 2 in N, so 2^v2(N) | u; and since gcd(g, v) = 1 makes
    v odd and v2(g) = v2(b^c), the census's v2(N) is c.v2(b) -- which
    is why the parent's joint sat at v2(N) = 8 for b = 4 (c = 4) and
    at 4, 5, 6 for b = 6 (c = 4, 5, 6).

(E) THE ODD PRIMES OF b ARE NOT FORCED. For an odd prime p | b, p | n
    puts the multiples kN/p in gZ, and the block holds one of them
    only when E < N(p-1)/(2p); the block's length N - span is below g
    <= N/p, so this needs the deficit N - span - 1 to sit within one
    of N/p - 1 -- a razor rather than a law. So the census can and
    should carry cells with 3 | n at b = 6 and 5 | n at b = 10: the
    factor 2 is special because N/2 is the ONE multiple of N/p the
    symmetric block is guaranteed to contain.

(F) THE ODD RADIX HAS A HOLE. At b = 2a + 1 the bound a r_c >= b^c/2
    fails (a r_c = (b^c - 1)/2), the third branch of (C) opens with E
    up to N/2 + v/2 - 2, and N/2 can then sit inside I. n even at an
    odd radix needs v even, and this file counts rather than argues
    those cells: the claim (D) makes is for even radices, which is
    where every below-cut pair lives, and the odd-radix parity at this
    cap is a measurement.

THE DESIGN, frozen before the engine.

E-A THE CANDIDATE STREAM reproduces the census. The census's own loop
    is walked to the point where a cell has passed the interval
    mismatch and the pre-period floor but not yet the deep-saturation
    read, yielding every such cell; the ones a deep-saturated class of
    below-count >= 3 survives in must be exactly solved_cells' keys.
    Control: the two key sets are equal.
E-B (A) checked: gcd(g, v) = 1 and b^c = 0 (mod g) at every candidate
    cell. Kill: a candidate cell printing either false.
E-C (B) checked against the direct count: at every candidate cell,
    0 is in A iff no multiple of g lies strictly between hi and N + lo.
    Kill: one disagreement.
E-D (C) checked: at every even-radix candidate cell, hi < N/2 < N + lo.
    Kill: one even-radix candidate cell with N/2 outside the block.
    And at odd radix the count of candidate cells with N/2 outside the
    block is printed beside the count with v even, unasserted.
E-E (D) as the observable: over candidate cells with n even, the count
    with below_counts empty, out of the count of such cells -- the
    prediction is all of them, at both radix parities for even radix
    and as a reading for odd; then over the census (deep-saturated
    cells, below-count >= 3), the count with n odd out of all. Kill: a
    census cell with n even at any radix, or an even-radix candidate
    cell with n even carrying a deep-saturated class. Positive
    control: the census is non-empty at every radix the parent
    reports, so the filter passes cells and is not vacuous.
E-F THE SAME AT BELOW-COUNT 1: solved_cells at min_below = 1 and the
    same cap, n odd at every cell. Kill: one even n. This is what says
    the below-count threshold is not the actor.
E-G (E) read: over the census, per radix, the count of cells with
    v_p(g) < c.v_p(b) for each prime p | b -- for p = 2 the prediction is 0
    at every even radix (forced), for odd p a positive count is the
    prediction where the radix carries cells at all.
E-H THE PARENT'S JOINT REPRODUCED: over the below-cut non-contained
    pairs the joint of (b, c) and of (v2(N), v2(u) capped at v2(N)+1),
    the latter to equal the parent's {(4,4): 344, (4,5+): 296, (5,5):
    36, (5,6+): 44, (6,6): 4, (6,7+): 8, (8,8): 1344, (8,9+): 1440}.
    Control: the below-cut population is 3516.

FINDINGS (entered post-run; every number below sits in this file's
own prints).

N1 THE PARITY IS THE DEEP-SATURATION READ'S, AND IT IS THE WHOLE
   CENSUS'S. The candidate stream reproduces solved_cells exactly:
   11,220 cells pass the interval mismatch and the pre-period floor,
   11,095 of them carry a deep-saturated class of below-count >= 3,
   and those are solved_cells' keys to the cell. n is odd at all
   11,095 -- b = 2 (9567 cells), 3 (1281), 4 (131), 6 (113) and 10 (3)
   -- and at all 85,611 cells of the census at below-count 1, over
   eleven radices. The 107 candidate cells with n even (11,521 at
   below-count 1) carry no deep-saturated class, every one.
N2 THE MECHANISM CHECKS STEP BY STEP. gcd(g, v) = 1 and b^c = 0
   (mod g) at every candidate cell (A); class 0 is in A exactly when
   no multiple of g lies strictly between hi and N + lo, 11,220 of
   11,220 and 97,226 of 97,226 (B); N/2 lies in that block at every
   even-radix candidate cell, 0 misses at either threshold (C). And
   the block never holds a multiple of g OTHER than N/2 at this cap:
   among candidate cells with n odd, class 0 is unsaturated at 0.
N3 THE FACTOR 2 IS THE ONLY FORCED ONE. v2(g) = c.v2(b) at every
   even-radix census cell, so v is odd, v2(N) = c.v2(b), and the below-cut joint
   of (b, c) is {(4,4): 2784, (6,4): 628, (6,5): 80, (6,6): 12,
   (10,4): 12} -- the parent's v2(N) values 8, 4, 5, 6 read off it.
   The odd primes are not forced: at below-count 1 the cells with
   v_p(g) < c.v_p(b) are 5656 of 8127 at b = 6 (p = 3), 1606 of 2296 at
   b = 10 (p = 5), 588 of 919 at b = 12 (p = 3), and at the odd
   radices 3602 of 13,978 at b = 3, 907 of 4871 at b = 5. At
   below-count 3 the same count reads 113 of 113 at b = 6 and 3 of 3
   at b = 10, and that is the depth floor's doing and not the
   parity's: a below-count of 3 needs J >= 4, so n >= 2a r_3 + 2,
   which is 260 at b = 6 (a >= 3) and 1112 at b = 10, while the cap
   leaves v <= 46 and v <= 6 -- so n = v.(b^c/g) draws its size from
   the odd prime, g < b^c there, and it is the cap and the floor that
   select it. At b = 4 the floor is 86 against v <= 234, and g = 4^c
   at every cell.
N4 THE ODD-RADIX HOLE IS EMPTY AT THIS CAP. No odd-radix candidate
   cell has n even at all -- none has v even -- at either threshold,
   so (F)'s hole has zero population here and the odd-radix parity is
   a measurement with nothing to test it against.
N5 THE PARENT'S JOINT REPRODUCED: 3516 below-cut pairs, and the
   (v2(N), v2(u)) joint equal to the parent's at every entry.

VERDICT, by piece.
  - n ODD AT EVERY EVEN-RADIX CELL (D) is a PROPERTY: four steps of
    arithmetic from the census's own definitions, checked at 11,220
    and 97,226 candidate cells with 0 misses at each step. It closes
    the question the parent left open -- the numerator carries every
    factor of 2 the modulus does because an even n would put N/2,
    a multiple of g, inside the unsaturated block, and the class map's
    terminal class would then be unsaturated.
  - THE FILTERS THAT DO NOT ACT: the below-count and the measure cut
    enter the argument nowhere, and the census at below-count 1 reads
    n odd at all 85,611 cells (RULE at this scope, N <= 60,000).
  - THE ODD PRIME IS NOT FORCED (N3): a PROPERTY that it is not (the
    block need not hold kN/p), with the mixed counts at below-count 1
    as the instances; the 113 of 113 at below-count 3 is the depth
    floor against the cap, derived above.
  - THE ODD RADIX (N4): untested, zero population.

RUN RECORD: pure Python, integers only, standard library;
explore_slope_tree.py's cell, params, interval and depth_J,
explore_slope_twolevel.py's below_counts and preperiod_ceiling,
explore_slope_width.py's solved_cells, divisors and u_candidates,
explore_slope_window.py's walk and explore_slope_empty.py's pair_report
imported rather than copied, so the census walked is the one those
files measured. 123.7 s wall, peak working set 209.0 MB against the
512 MB analysis ceiling (memwatch.py); the below-count-1 census is
the heavier half at 68 s. Prints reproduced by:
python prime/code/explore_slope_parity.py
"""

import os
import sys
import time
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_slope_tree import cell, params, interval, depth_J  # noqa: E402
from explore_slope_twolevel import (  # noqa: E402
    below_counts, preperiod_ceiling,
)
from explore_slope_width import (  # noqa: E402
    solved_cells, divisors, u_candidates,
)
from explore_slope_window import walk, MU_CUT  # noqa: E402
from explore_slope_empty import pair_report  # noqa: E402

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print("  FAIL:", msg)


def v_p(x, p):
    k = 0
    while x % p == 0:
        x //= p
        k += 1
    return k


def prime_factors(b):
    out, p = [], 2
    while p * p <= b:
        if b % p == 0:
            out.append(p)
            while b % p == 0:
                b //= p
        p += 1
    if b > 1:
        out.append(b)
    return out


def candidate_cells(n_cap, min_below, b_cap=12, a_cap=8, c_cap=8):
    """solved_cells' loop up to the deep-saturation read: every
    phase-0 cell with N <= n_cap that has passed the interval mismatch
    and the pre-period floor. Yields (N, key, ce, two) with two the
    below-count levels solved_cells would keep."""
    tau_need = min_below + 1
    for b in range(2, b_cap + 1):
        for a in range(1, a_cap + 1):
            if 2 * a + 1 < b:
                continue
            for c in range(1, c_cap + 1):
                if b ** c > n_cap:
                    break
                for v in range(1, n_cap // b ** c + 1):
                    N = v * b ** c
                    for g in divisors(N):
                        if preperiod_ceiling(b, g) < tau_need:
                            continue
                        n = N // g
                        if depth_J(b, a, n) < tau_need:
                            continue
                        for u in u_candidates(b, a, c, v, g, N):
                            L, phi, N2, q, g2 = params(b, a, c, u, v, 0, 1)
                            if N2 != N or g2 != g:
                                continue
                            lo, hi, span, _ = interval(b, a, c, u, v, 0, 1)
                            if lo > hi or span > N or not (0 < N - span < g):
                                continue
                            ce = cell(b, a, c, u, v, 0, 1)
                            if ce is None:
                                continue
                            cnt, _ = below_counts(ce)
                            two = sorted(t for t, k in cnt.items()
                                         if k >= min_below)
                            yield (N, (b, a, c, u, v), ce, two)


def multiple_in_block(g, lo, hi, N):
    """Is some multiple of g strictly between hi and N + lo?"""
    k = hi // g + 1
    return k * g < N + lo


def run(cap, min_below=3):
    print(f"THE CENSUS, N <= {cap}, below-count >= {min_below}, phase 0")
    t0 = time.time()
    census_keys = {key for _, key, _, _ in solved_cells(cap, min_below)}
    print(f"solved_cells: {len(census_keys)} cells, "
          f"{time.time() - t0:.1f} s")
    seen = 0
    kept = set()
    bad_a = bad_c = bad_half_even = 0
    odd_half_out = odd_half_out_veven = 0
    even_n = even_n_empty = even_n_even_radix = even_n_even_radix_deep = 0
    zero_unsat_odd_n = 0
    per_radix = {}
    for N, key, ce, two in candidate_cells(cap, min_below):
        b, a, c, u, v = key
        g, n, lo, hi, A = ce["g"], ce["n"], ce["lo"], ce["hi"], ce["A"]
        seen += 1
        # E-B
        if gcd(g, v) != 1 or pow(b, c, g) != 0:
            bad_a += 1
        # E-C: 0 in A iff no multiple of g in the block
        if (0 in A) == multiple_in_block(g, lo, hi, N):
            bad_c += 1
        # E-D
        half_in = hi < N / 2 < N + lo
        if b % 2 == 0:
            if not half_in:
                bad_half_even += 1
        elif not half_in:
            odd_half_out += 1
            if v % 2 == 0:
                odd_half_out_veven += 1
        # E-E
        if n % 2 == 0:
            even_n += 1
            if not two:
                even_n_empty += 1
            if b % 2 == 0:
                even_n_even_radix += 1
                if two:
                    even_n_even_radix_deep += 1
        elif 0 not in A:
            zero_unsat_odd_n += 1
        if two:
            kept.add(key)
            r = per_radix.setdefault(b, {"cells": 0, "n_even": 0,
                                         "v_even": 0})
            r["cells"] += 1
            r["n_even"] += n % 2 == 0
            r["v_even"] += v % 2 == 0
            for p in prime_factors(b):
                r[p] = r.get(p, 0) + (v_p(g, p) < c * v_p(b, p))
    print(f"\nE-A  candidate cells {seen}; with a deep-saturated class of "
          f"below-count >= {min_below}: {len(kept)}")
    ok(kept == census_keys, "E-A: the candidate stream reproduces "
       "solved_cells' key set")
    print(f"E-B  gcd(g, v) = 1 and b^c = 0 (mod g): {seen - bad_a} of "
          f"{seen}")
    ok(bad_a == 0, "E-B: g | b^c at every candidate cell")
    print(f"E-C  0 in A iff no multiple of g strictly between hi and "
          f"N + lo: {seen - bad_c} of {seen}")
    ok(bad_c == 0, "E-C: class 0's saturation is the block test")
    print(f"E-D  even radix: N/2 strictly between hi and N + lo at every "
          f"candidate cell -- misses {bad_half_even}")
    ok(bad_half_even == 0, "E-D: the block contains N/2 at even radix")
    print(f"     odd radix: candidate cells with N/2 outside the block "
          f"{odd_half_out}, of which v even {odd_half_out_veven}")
    print(f"E-E  candidate cells with n even {even_n}; of these, with no "
          f"deep-saturated class {even_n_empty}; even-radix ones "
          f"{even_n_even_radix}, carrying a deep-saturated class "
          f"{even_n_even_radix_deep}")
    ok(even_n_even_radix_deep == 0, "E-E: an even n at even radix "
       "carries no deep-saturated class")
    tot = sum(r["cells"] for r in per_radix.values())
    n_even_census = sum(r["n_even"] for r in per_radix.values())
    print(f"     census cells {tot}, n even at {n_even_census}; n odd "
          f"with class 0 unsaturated among candidates: "
          f"{zero_unsat_odd_n} (excluded by another multiple of g)")
    ok(n_even_census == 0, "E-E: n is odd at every census cell")
    ok(len(per_radix) >= 5, "E-E control: the census is non-empty at "
       "several radices")
    print("E-G  per radix: cells, n even, v even, and per prime p | b "
          "the cells with v_p(g) < c.v_p(b)")
    for b in sorted(per_radix):
        r = per_radix[b]
        ps = ", ".join(f"p={p}: {r[p]}" for p in prime_factors(b))
        print(f"     b = {b:2d}: cells {r['cells']:5d}, n even "
              f"{r['n_even']}, v even {r['v_even']}, {ps}")
        if b % 2 == 0:
            ok(r[2] == 0, f"E-G: v2(g) = c.v2(b) at every b = {b} cell")
    print(f"     wall {time.time() - t0:.1f} s")


def run_pairs(cap, min_below=3):
    """E-H: the parent's joint, over the below-cut population."""
    t0 = time.time()
    below = bad_v2 = 0
    bc, twos = {}, {}
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        r = pair_report(b, a, n, A, C)
        if r["contained"] or r["mu"] >= MU_CUT:
            continue
        below += 1
        u, c = key[3], key[2]
        bc[(b, c)] = bc.get((b, c), 0) + 1
        v2N, v2u = v_p(N, 2), v_p(u, 2)
        k = (v2N, min(v2u, v2N + 1))
        twos[k] = twos.get(k, 0) + 1
        if v2N != c * v_p(b, 2):
            bad_v2 += 1
    print(f"\nE-H  below-cut population {below} (parent: 3516)")
    ok(below == 3516, "E-H control: the below-cut population is 3516")
    print(f"     joint (b, c): {dict(sorted(bc.items()))}")
    print(f"     joint (v2(N), v2(u) capped at v2(N)+1): "
          f"{dict(sorted(twos.items()))}")
    parent = {(4, 4): 344, (4, 5): 296, (5, 5): 36, (5, 6): 44,
              (6, 6): 4, (6, 7): 8, (8, 8): 1344, (8, 9): 1440}
    ok(twos == parent, "E-H: the parent's joint reproduced")
    ok(bad_v2 == 0, "E-H: v2(N) = c.v2(b) at every below-cut pair")
    print(f"     wall {time.time() - t0:.1f} s")


def main():
    run(60000, 3)
    run_pairs(60000, 3)
    print("\nE-F  the same at below-count 1")
    run(60000, 1)
    if FAILURES:
        print(f"\nFAILURES: {len(FAILURES)}")
        return
    print("\nall checks passed")


if __name__ == "__main__":
    main()
