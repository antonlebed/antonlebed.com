"""
The comparator ruler: grading a live RNS comparison method on the wall's scale

An earlier line of work (explore_rns_comparator.py,
explore_size_transform.py) classified every known exact escape from
non-positional comparison into three priced routes: (a) the circle sum
(partial fractions, full log2 N bits in R/Z), (b) mixed-radix
conversion (exact but triangular: n digits in sequence, n-1 gated
rounds), (c) a monotone characteristic -- where a NON-STRICT
one (the diagonal) buys a ring-sized extra positional channel plus a
tie-break, and a STRICT one pays the injectivity floor (a strict
characteristic on [0, N) takes >= N values, so its computed width never
drops below log2 N). A 2026 general-moduli
comparison method (Didier, El Mrabet, Glandus, Robert, "Residue Number
System Comparison revisited, a software perspective", arXiv:2605.18415v1,
full text) was graded ON PAPER as paying route (b) whole. This script is
the ruler made real: the specimen implemented from the paper's own
Algorithms 1-3, verified against ground truth, its price MEASURED, and
the placement leg -- the cost-law boundary sum 1/m = 1 straddled by
constructed modulus sets, with the diagonal comparator's width verdict
required to flip exactly there.

THE SPECIMEN (from the full text). Algorithm 1, RNSComp(N1, N2): given
both operands' residues in base B = {m_1..m_n} plus their residues at a
redundant modulus ma coprime to M = prod m_i:
  1. delta1 = (n1a - n2a) mod ma                     [the direct route]
  2. z_i = (n1_i - n2_i) mod m_i for every channel   [(N1-N2) mod M]
  3. {a_1..a_n} = MRConversion(z)                    [Algorithm 2]
  4. delta = toma(a_1..a_n)                          [Algorithm 3]
     = ((N1 - N2) mod M) mod ma
  5. return N1 >= N2 iff delta == delta1
Theorem 1: correct for ALL 0 <= N1, N2 < M, because N1 < N2 shifts
delta by M mod ma != 0 (ma coprime to M). The redundant channel is used
as a consistency TEST (delta == delta1?), never to compute the CRT
correction k -- the paper cites Shenoy-Kumaresan for redundant-modulus
base extension and rejects that route for comparison (their k needs
x_r = X mod m_r guaranteed, which the difference of two residue vectors
does not provide when N1 < N2).

THE QUESTION. Does the specimen, implemented and measured, pay exactly
the prices the escape classification assigns it -- and does the
diagonal-comparator cost-law verdict flip exactly at sum 1/m = 1?

THE SLATE (frozen before the engine; hand-derived from the paper's
pseudocode and the wall chart):

  P1 (correctness). The implemented Algorithm 1 agrees with ground
     truth (integer comparison, equality counted as >=) on every pair
     tested: exhaustive all ordered pairs at two toy bases (one with
     composite moduli), random pairs plus a corner battery (equal
     values, differences that are multiples of ma, values at and next
     to 0 and M-1, adjacent pairs) at the k=7 primorial base, at the
     all-composite set {15, 77, 221}, and at 8 primes near 2^16.
  P2 (price). The measured word-multiplication count per comparison is
     n(n-1)/2 + (n-1): Algorithm 2's triangular n(n-1)/2 plus
     Algorithm 3's loop from digit 2, which executes n-1 multiplies --
     ONE UNDER the paper's own Table 1 figure of n(n-1)/2 + n (its
     Algorithm 3 text says n multiplications; the loop as printed does
     n-1). The discrepancy is a reading of the paper, not a defect of
     the method.
  P3 (width = the injectivity floor, paid). The computed object is the
     full mixed-radix digit vector: sum_i log2 m_i = log2 M bits,
     exactly the floor, and the digit map is injective on [0, M)
     (exhaustive at the toy bases). The specimen never computes under
     log2 N -- it is strict, so the floor binds it; route (c)'s dodge
     (a non-strict characteristic like D alone) is what computes
     narrower.
  P4 (triangular depth, paid). Digit a_i is finalized only after
     a_1..a_{i-1}: the dependency chain has length n-1 rounds (the
     paper's parallel inner loop; sequentially n(n-1)/2 steps). The
     specimen pays route (b)'s gate structure in full.
  P5 (placement). For constructed modulus sets with sum 1/m straddling
     1 -- including the razor pair {2,3,7,43} (sum = 1805/1806) and
     {2,3,7,41} (sum = 1723/1722) -- the diagonal channel's width
     verdict SQ < M holds iff sum 1/m < 1, EXACTLY (SQ = sum_i M/m_i =
     M * sum 1/m_i as exact integers), with gcd(M, SQ) = 1 at every
     set (the forced coprimality, re-confirmed in passing). The
     specimen's own width column reads log2 M at every set,
     independent of sum 1/m: the ruler shows the strict method pinned
     to the floor while the non-strict diagonal dips below it exactly
     where sum 1/m < 1.
  P6 (positive controls, run before any verdict is read).
     (a) An always->= comparator fed to the harness fails on exactly
         the pairs with N1 < N2 (harness detects failure).
     (b) Algorithm 1 run OUTSIDE its hypothesis, ma | M (base {3,5,7},
         ma = 15): every N1 < N2 pair is mislabeled >= (delta =
         delta1 + M = delta1 mod ma), every N1 >= N2 pair correct --
         the coprimality hypothesis is load-bearing, and the harness
         sees the breakage.

KILL-SHAPE (observables, frozen; meaning weighed after the run): the
kill fires iff the rig prints, for the specimen, a total computed digit
width strictly under log2 M AND a dependency depth strictly under n-1
-- the specimen paying neither the injectivity floor nor the
triangular depth (it contains no circle-sum step by construction).
Then the escape classification is incomplete and the chart gains a
fourth row instead of a ruler.

DESIGN NOTES. Index convention re-derived from the paper before the
freeze: the paper's Algorithm 2 is 1-based, digits a_1..a_n, constants
inv(m_j, m_i) = m_j^{-1} mod m_i for j < i; this implementation is
0-based with inv[j][i] for j < i, digit a[i] reduced mod base[i].
Ground truth is plain integer comparison of the decoded values.
Multiplications are counted by instrumented arithmetic at the two
sites the paper counts (Algorithm 2 line 6, Algorithm 3 line 3).
Depth is measured by simulating the paper's parallel schedule: in
round r every unfinalized digit subtracts the just-finalized a_r; the
printed depth is the number of rounds until a_n finalizes.
Resource estimate: pure Python integers, largest base 8 x 16-bit
primes, ~10^5 comparisons total, well under 10 s and a few MB.

FINDINGS (tiers per the naming discipline; every number below is from
the printed run):

1. CORRECTNESS: EXACT EVERYWHERE TESTED (rule, verified exhaustive at
   two toy bases + sampled at three working bases). All ordered pairs
   at {3,5,7} (11,025) and at the composite-moduli {4,9,5} (32,400);
   50,000 random pairs + the corner battery at the k=7 primorial base
   (ma = 19), 20,000 + corners at the all-composite {15,77,221}
   (ma = 4), 5,000 + corners at 8 primes near 2^16 (ma = 65167):
   0 mismatches, 118,485 pairs total. The corner battery hits equal
   values, differences of +-ma and +-2ma (the paper's Remark 1), 0 and
   M-1 and their neighbours, and adjacent pairs at M/2. The paper's
   generality claims hold as stated: composite moduli, composite
   redundant modulus (ma = 4), full range.

2. PRICE: n(n-1)/2 + (n-1) WORD MULTIPLICATIONS, MEASURED (rule,
   verified at every base). n=3: 5, n=7: 27, n=8: 35 -- exactly the
   frozen prediction, ONE UNDER the paper's Table 1 (n(n-1)/2 + n):
   its Algorithm 3 as printed multiplies n-1 times, not the n its
   text states. A reading of the paper's own count, not a defect of
   the method; the triangular term matches exactly.

3. WIDTH: THE INJECTIVITY FLOOR, PAID WHOLE (rule, verified; the floor
   itself = property, pigeonhole). The computed object is the full
   mixed-radix digit vector, sum log2 m_i = log2 M bits (n=8 base:
   128.0), and the digit map is injective on [0, M): 105/105 distinct
   digit vectors at {3,5,7}, 180/180 at {4,9,5}. The specimen is
   strict, so the floor binds it: it never computes under log2 M.

4. DEPTH: n-1 GATED ROUNDS, MEASURED (rule, verified at every base).
   The parallel-schedule simulation finalizes the last digit at round
   n-1 at every base (n=3: 2, n=7: 6, n=8: 7): route (b)'s triangular
   gate paid in full; the sequential step count is the same n(n-1)/2
   the price counts.

5. PLACEMENT: THE VERDICT FLIPS EXACTLY AT SUM 1/m = 1 (rule, verified
   at 8 sets, exact integer arithmetic: SQ = M * sum 1/m and
   gcd(M, SQ) = 1 asserted at every set). SQ < M iff sum 1/m < 1 at
   every set, razor pair included: {2,3,7,43} at sum = 0.999446
   (D width 10.8178 vs floor 10.8186) against {2,3,7,41} at
   sum = 1.000581 (10.7507 vs 10.7499) -- the flip bracketed within
   6e-4 on both sides, and {2,3,7,43,1807} tightens the below side to
   1 - 1/3263442. The specimen's width column reads log2 M at every
   row while the diagonal's reads log2 M + log2(sum 1/m): the strict
   method pinned to the floor, the non-strict diagonal dipping under
   it exactly where sum 1/m < 1.

6. CONTROLS: BOTH FIRED AS PREDICTED (verified, run before any
   verdict). (a) The always->= comparator fails on exactly the 5,460
   N1 < N2 pairs at {3,5,7}. (b) With ma = 15 dividing M = 105, every
   N1 < N2 pair is mislabeled (5460/5460) and every N1 >= N2 pair is
   correct: the coprimality hypothesis is load-bearing, and the
   harness sees breakage when it is there.

THE KILL DOES NOT FIRE: the specimen pays the injectivity floor
(finding 3) AND the triangular depth (finding 4). The paper-grade
verdict -- escape (b), priced by the chart, not crossing it -- is now
measured, not read.

RUN RECORD: python explore_comparator_ruler.py -> ALL CHECKS PASS:
118,485 correctness pairs, 2 controls, 8 placement sets; 0.31 s, pure
Python integers. Deterministic seed 20260731.
"""

import math
import random
from fractions import Fraction


# ---------------------------------------------------------------- machinery

class MulCounter:
    """Counts word-size modular multiplications at the paper's two sites."""
    def __init__(self):
        self.n = 0

    def mulmod(self, a, b, m):
        self.n += 1
        return (a * b) % m


def precompute(base, ma):
    """Inverse table inv[j][i] = base[j]^{-1} mod base[i] (j < i), and
    mu[i] = prod(base[:i]) mod ma (Algorithm 3's constants)."""
    n = len(base)
    inv = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(i):
            inv[j][i] = pow(base[j], -1, base[i])
    mu = [1] * n
    acc = 1
    for i in range(1, n):
        acc = (acc * base[i - 1]) % ma
        mu[i] = acc
    return inv, mu


def mr_conversion(z, base, inv, cnt):
    """Algorithm 2: mixed-radix digits of the value with residues z."""
    n = len(base)
    a = list(z)
    for i in range(1, n):
        for j in range(i):
            a[i] = cnt.mulmod((a[i] - a[j]) % base[i], inv[j][i], base[i])
    return a


def to_ma(a, ma, mu, cnt):
    """Algorithm 3: the mixed-radix value reduced mod ma."""
    x = a[0] % ma
    for i in range(1, len(a)):
        x = (x + cnt.mulmod(a[i], mu[i], ma)) % ma
    return x


def rns_comp(r1, r2, n1a, n2a, base, ma, inv, mu, cnt):
    """Algorithm 1: True iff N1 >= N2."""
    delta1 = (n1a - n2a) % ma
    z = [(x - y) % m for x, y, m in zip(r1, r2, base)]
    digits = mr_conversion(z, base, inv, cnt)
    delta = to_ma(digits, ma, mu, cnt)
    return delta == delta1


def encode(x, base):
    return [x % m for m in base]


def check_pairs(pairs, base, ma, comparator=None):
    """Ground-truth harness: returns (fail_ge, fail_lt) counts, where
    fail_ge = wrong verdicts on N1 >= N2 pairs, fail_lt on N1 < N2."""
    inv, mu = precompute(base, ma)
    cnt = MulCounter()
    fail_ge = fail_lt = 0
    for x, y in pairs:
        if comparator is None:
            got = rns_comp(encode(x, base), encode(y, base),
                           x % ma, y % ma, base, ma, inv, mu, cnt)
        else:
            got = comparator(x, y)
        want = x >= y
        if got != want:
            if want:
                fail_ge += 1
            else:
                fail_lt += 1
    return fail_ge, fail_lt


def corner_battery(M, ma):
    """The frozen corner list: equal, +-ma and +-2ma differences,
    the ends and their neighbours, adjacent pairs at M/2."""
    h = M // 2
    pts = [(0, 0), (M - 1, M - 1), (h, h),
           (0, 1), (1, 0), (M - 1, 0), (0, M - 1),
           (M - 1, M - 2), (M - 2, M - 1), (1, M - 1),
           (h, h + 1), (h + 1, h),
           (2 * ma % M, ma % M), (ma % M, 2 * ma % M),
           ((h + ma) % M, h), (h, (h + ma) % M),
           ((h + 2 * ma) % M, h), (h, (h + 2 * ma) % M),
           (ma % M, 0), (0, ma % M)]
    return [(x % M, y % M) for x, y in pts]


# ---------------------------------------------------------------- the run

def main():
    rng = random.Random(20260731)
    total_pairs = 0

    # ---- P6 controls FIRST (a verdict needs a positive control).
    base, ma = [3, 5, 7], 11
    M = math.prod(base)
    allpairs = [(x, y) for x in range(M) for y in range(M)]
    n_lt = sum(1 for x, y in allpairs if x < y)

    fg, fl = check_pairs(allpairs, base, ma, comparator=lambda x, y: True)
    print("control (a) always->= at {3,5,7}: fails on N1<N2 = %d "
          "(expect %d), on N1>=N2 = %d (expect 0)" % (fl, n_lt, fg))
    assert fl == n_lt and fg == 0

    fg, fl = check_pairs(allpairs, base, 15)   # ma = 15 divides M = 105
    print("control (b) ma=15 | M=105: N1<N2 mislabeled = %d/%d, "
          "N1>=N2 wrong = %d (expect all / 0)" % (fl, n_lt, fg))
    assert fl == n_lt and fg == 0

    # ---- P1 correctness.
    print()
    suites = [
        ([3, 5, 7],        11,    "exhaustive"),
        ([4, 9, 5],        7,     "exhaustive"),
        ([2, 3, 5, 7, 11, 13, 17], 19, 50000),
        ([15, 77, 221],    4,     20000),
        ([65537, 65539, 65543, 65551, 65557, 65563, 65579, 65581],
                           65167, 5000),
    ]
    for base, ma, mode in suites:
        M = math.prod(base)
        assert math.gcd(M, ma) == 1
        for i in range(len(base)):
            for j in range(i):
                assert math.gcd(base[i], base[j]) == 1
        if mode == "exhaustive":
            pairs = [(x, y) for x in range(M) for y in range(M)]
        else:
            pairs = [(rng.randrange(M), rng.randrange(M))
                     for _ in range(mode)]
            pairs += corner_battery(M, ma)
        fg, fl = check_pairs(pairs, base, ma)
        total_pairs += len(pairs)
        print("P1 base %-11s n=%d ma=%-5d pairs=%-6d mismatches=%d"
              % ("{%s}" % ",".join(map(str, base[:3]))
                 + ("..." if len(base) > 3 else ""),
                 len(base), ma, len(pairs), fg + fl))
        assert fg == 0 and fl == 0

    # ---- P2 price: mults per single comparison.
    print()
    for base, ma, _ in suites:
        n = len(base)
        M = math.prod(base)
        inv, mu = precompute(base, ma)
        cnt = MulCounter()
        rns_comp(encode(M // 3, base), encode(M // 5, base),
                 (M // 3) % ma, (M // 5) % ma, base, ma, inv, mu, cnt)
        pred = n * (n - 1) // 2 + (n - 1)
        print("P2 n=%d: mults=%d predict n(n-1)/2+(n-1)=%d "
              "(paper Table 1: %d)" % (n, cnt.n, pred, pred + 1))
        assert cnt.n == pred

    # ---- P3 width: digits carry log2 M exactly; injective at toys.
    print()
    for base, ma, mode in suites:
        M = math.prod(base)
        print("P3 n=%d: digit width = sum log2 m_i = log2 M = %.1f bits"
              % (len(base), math.log2(M)))
    for base, ma in [([3, 5, 7], 11), ([4, 9, 5], 7)]:
        M = math.prod(base)
        inv, mu = precompute(base, ma)
        cnt = MulCounter()
        seen = set()
        for x in range(M):
            seen.add(tuple(mr_conversion(encode(x, base), base, inv, cnt)))
        print("P3 injectivity at M=%d: %d distinct digit vectors"
              % (M, len(seen)))
        assert len(seen) == M

    # ---- P4 depth: rounds until the last digit, derived from the
    # dependency structure of Algorithm 2 itself: digit i's j-th step
    # subtracts a_j, so it can run no earlier than one round after BOTH
    # digit j is final and digit i's previous step ran.
    print()
    for base, ma, _ in suites:
        n = len(base)
        ready = [0] * n                # round at which digit i is final
        for i in range(1, n):
            t = 0
            for j in range(i):
                t = max(t, ready[j]) + 1
            ready[i] = t
        depth = ready[n - 1]
        print("P4 n=%d: dependency depth = %d rounds (predict n-1 = %d)"
              % (n, depth, n - 1))
        assert depth == n - 1

    # ---- P5 placement: the cost-law boundary straddled.
    print()
    place_sets = [
        [3, 5, 7],
        [97, 101, 103],
        [65537, 65539, 65543, 65551, 65557, 65563, 65579, 65581],
        [2, 3, 7, 43],            # razor, below
        [2, 3, 7, 43, 1807],      # sharper below
        [2, 3, 7, 41],            # razor, above
        [2, 3, 5],
        [2, 3, 5, 7, 11, 13, 17],
    ]
    for base in place_sets:
        M = math.prod(base)
        SQ = sum(M // m for m in base)
        s = sum(Fraction(1, m) for m in base)
        assert SQ == M * s            # SQ = M * sum 1/m exactly
        assert math.gcd(M, SQ) == 1   # forced coprimality, in passing
        verdict = SQ < M
        assert verdict == (s < 1)     # the flip, exact
        print("P5 %-28s sum1/m=%-12s SQ%sM  width: D=%.4f floor=%.4f"
              % ("{%s}" % ",".join(map(str, base)),
                 "%.6f" % float(s), "<" if verdict else ">=",
                 math.log2(SQ), math.log2(M)))

    print()
    print("ALL CHECKS PASS: %d correctness pairs, 2 controls, %d "
          "placement sets" % (total_pairs, len(place_sets)))


if __name__ == "__main__":
    main()
