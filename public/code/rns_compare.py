"""rns_compare.py -- a published residue comparison method, implemented
from its pseudocode and priced against the size wall.

QUESTION. A residue number system holds x in [0, M) as its residues at
pairwise coprime moduli m_1 .. m_n, and no channel-local read compares
two such numbers (the size wall). Every exact comparator pays a
reconstruction: some key that rises with x, and a strict one takes at
least M values, log2 M bits. Didier, El Mrabet, Glandus and Robert,
"Residue Number System Comparison revisited, a software perspective"
(arXiv:2605.18415v1), propose a method for arbitrary moduli with one
redundant modulus m_a coprime to M. What does it compute, what does it
cost, and where does it sit on that scale?

THE METHOD, read from the paper's Algorithms 1 to 3.
  Algorithm 1. Given the residues of N1 and N2 in the base and at m_a:
    delta1 = (N1 - N2) mod m_a, from the redundant channel;
    z_i = (N1 - N2) mod m_i in every channel, the residues of
    (N1 - N2) mod M;
    the mixed-radix digits of that value by Algorithm 2, and its
    residue mod m_a by Algorithm 3, delta;
    N1 >= N2 iff delta = delta1.
  Why it is exact: if N1 >= N2 the value is N1 - N2 and delta = delta1;
  if N1 < N2 it is N1 - N2 + M and delta = delta1 + M mod m_a, which
  differs from delta1 because m_a is coprime to M. The redundant channel
  is a TEST of which branch the wrap took, never a computation of it.
  Algorithm 2 (Szabo and Tanaka's mixed-radix conversion): for i = 2..n,
  for j = 1..i-1, a_i <- (a_i - a_j) m_j^-1 mod m_i: n(n-1)/2 modular
  multiplications. Algorithm 3: x <- a_1 mod m_a, then for i = 2..n,
  x <- x + a_i mu_i mod m_a, mu_i the product of m_1 .. m_(i-1) mod
  m_a. Its loop multiplies n - 1 times; the paper's text says n, and
  its Table 1 counts n(n-1)/2 + n.

PREDICTIONS, fixed before this run from the pseudocode and the wall.
  P1 exact at every pair: all ordered pairs at {3, 5, 7} (m_a = 11) and
     at the composite moduli {4, 9, 5} (m_a = 7); 50,000 random pairs
     plus a corner list at the primorial base 2 .. 17 (m_a = 19); 20,000
     plus corners at {15, 77, 221} (m_a = 4, itself composite); 5,000
     plus corners at eight primes above 2^16 (m_a = 65167). The corners:
     equal values, differences of m_a and 2 m_a, 0 and M - 1 and their
     neighbours, adjacent pairs at M/2.
  P2 the multiplications per comparison, counted at the two sites, are
     n(n-1)/2 + (n - 1): 5, 27 and 35 at n = 3, 7 and 8, one under the
     paper's Table 1.
  P3 the computed object is the whole mixed-radix digit vector, log2 M
     bits, and the digit map is injective on [0, M) (exhaustive at the
     two small bases): the method is strict, so the floor binds it.
  P4 in the presented conversion digit i's j-th step waits on digit j,
     so the last digit is final after n - 1 rounds even with the digits
     (the outer loop) computed in parallel, each digit's steps in turn
     and each step as soon as the digit it reads is final. The O(log n)
     parallel time in the paper's Table 1 rests on a different
     conversion it cites (Huang) and does not present; P4 prices the
     presented one.
  P5 POSITIVE CONTROLS, run before any verdict. (a) A comparator that
     always answers N1 >= N2 fails at exactly the N1 < N2 pairs of
     {3, 5, 7}. (b) With m_a = 15 dividing M = 105, Algorithm 1 mislabels
     every N1 < N2 pair and no other: coprimality is load-bearing.
     [Read later: the method needs only that m_a not divide M, the wrap
     shifting delta by M mod m_a; P5b shows a divisor breaks it, not
     that coprimality is needed.]

FINDINGS, entered after the run from its print. Every prediction held,
10/10 checks.
  P5 both controls fire: 5460 of the 5460 N1 < N2 pairs at {3, 5, 7}.
  P1 exact at all 118,485 pairs: 11,025 and 32,400 exhaustive, then
     50,020, 20,020 and 5,020 with the corners.
  P2 5, 5, 27, 5 and 35 multiplications at n = 3, 3, 7, 3, 8, one
     under Table 1 at every base. The paper was read at source for
     this count: Table 1 prints (n(n-1)/2 + n) M and the text of
     Algorithm 3 says n multiplications, while its loop runs i = 2..n.
  P3 105 and 180 distinct digit vectors: the width is log2 M, 128.0
     bits at the eight primes above 2^16.
  P4 n - 1 rounds at every base. [Read later: the dependency model
     gives digit i ready at round i for every n, so P4 is the argument
     itself; it is now printed as a record, not checked.]
  Tiers: exactness is the paper's theorem, verified here; the count,
  the width and the depth are rules, proved from the pseudocode and
  counted at every base.

RUN RECORD. `python rns_compare.py` under a memory guard: 10/10 PASS, 16.5 MB
peak commit, 0.5 s, seed 20260731. After a code read, 9/9: the controls
stop the run if either fails, P3 prints its 105 and 180, and P4, which
held by its own model, is printed as a record (rounds 2, 2, 6, 2, 7 at
n = 3, 3, 7, 3, 8). 16.2 MB, 0.3 s.

Standard library only.

    python rns_compare.py
"""

import math
import random

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}"
                                                      if detail else ""))


class Counter:
    def __init__(self):
        self.n = 0

    def mulmod(self, a, b, m):
        self.n += 1
        return a * b % m


def precompute(base, ma):
    n = len(base)
    inv = [[pow(base[j], -1, base[i]) if j < i else 0 for i in range(n)]
           for j in range(n)]
    mu, acc = [1] * n, 1
    for i in range(1, n):
        acc = acc * base[i - 1] % ma
        mu[i] = acc
    return inv, mu


def mixed_radix(z, base, inv, cnt):
    """Algorithm 2."""
    a = list(z)
    for i in range(1, len(base)):
        for j in range(i):
            a[i] = cnt.mulmod((a[i] - a[j]) % base[i], inv[j][i], base[i])
    return a


def to_ma(a, ma, mu, cnt):
    """Algorithm 3."""
    x = a[0] % ma
    for i in range(1, len(a)):
        x = (x + cnt.mulmod(a[i], mu[i], ma)) % ma
    return x


def compare(x, y, base, ma, inv, mu, cnt):
    """Algorithm 1 on the residues of x and y: True iff x >= y."""
    delta1 = (x % ma - y % ma) % ma
    z = [(x % m - y % m) % m for m in base]
    return to_ma(mixed_radix(z, base, inv, cnt), ma, mu, cnt) == delta1


def corners(M, ma):
    h = M // 2
    pts = [(0, 0), (M - 1, M - 1), (h, h), (0, 1), (1, 0), (M - 1, 0),
           (0, M - 1), (M - 1, M - 2), (M - 2, M - 1), (1, M - 1),
           (h, h + 1), (h + 1, h), (2 * ma, ma), (ma, 2 * ma),
           (h + ma, h), (h, h + ma), (h + 2 * ma, h), (h, h + 2 * ma),
           (ma, 0), (0, ma)]
    return [(x % M, y % M) for x, y in pts]


def failures(pairs, base, ma, comparator=None):
    inv, mu = precompute(base, ma)
    cnt = Counter()
    ge = lt = 0
    for x, y in pairs:
        got = comparator(x, y) if comparator else \
            compare(x, y, base, ma, inv, mu, cnt)
        if got != (x >= y):
            ge += x >= y
            lt += x < y
    return ge, lt


SUITES = [([3, 5, 7], 11, None), ([4, 9, 5], 7, None),
          ([2, 3, 5, 7, 11, 13, 17], 19, 50000),
          ([15, 77, 221], 4, 20000),
          ([65537, 65539, 65543, 65551, 65557, 65563, 65579, 65581],
           65167, 5000)]


def section_controls():
    print("P5 -- positive controls")
    base = [3, 5, 7]
    pairs = [(x, y) for x in range(105) for y in range(105)]
    n_lt = sum(x < y for x, y in pairs)
    ge, lt = failures(pairs, base, 11, comparator=lambda x, y: True)
    check("P5a always >= fails at exactly the N1 < N2 pairs",
          (ge, lt) == (0, n_lt), f"{lt} of {n_lt}")
    ge, lt = failures(pairs, base, 15)
    check("P5b m_a = 15 dividing 105 mislabels every N1 < N2 pair, no "
          "other", (ge, lt) == (0, n_lt), f"{lt} of {n_lt}")


def section_exact():
    print("P1 -- exactness")
    rng = random.Random(20260731)
    total = 0
    for base, ma, draws in SUITES:
        M = math.prod(base)
        assert math.gcd(M, ma) == 1
        if draws is None:
            pairs = [(x, y) for x in range(M) for y in range(M)]
        else:
            pairs = [(rng.randrange(M), rng.randrange(M))
                     for _ in range(draws)] + corners(M, ma)
        ge, lt = failures(pairs, base, ma)
        total += len(pairs)
        check(f"P1 n = {len(base)}, m_a = {ma}: exact", ge + lt == 0,
              f"{len(pairs)} pairs")
    print(f"  {total} pairs in all")


def section_price():
    print("P2, P3, P4 -- price, width, depth")
    ok = True
    for base, ma, _ in SUITES:
        n, M = len(base), math.prod(base)
        inv, mu = precompute(base, ma)
        cnt = Counter()
        compare(M // 3, M // 5, base, ma, inv, mu, cnt)
        want = n * (n - 1) // 2 + (n - 1)
        print(f"  n = {n}: {cnt.n} multiplications, Table 1 says "
              f"{want + 1}; digit width log2 M = {math.log2(M):.1f} bits")
        ok &= cnt.n == want
    check("P2 multiplications = n(n-1)/2 + (n-1) at every base", ok)
    ok, sizes = True, []
    for base, ma in (([3, 5, 7], 11), ([4, 9, 5], 7)):
        M = math.prod(base)
        inv, mu = precompute(base, ma)
        seen = {tuple(mixed_radix([x % m for m in base], base, inv,
                                  Counter())) for x in range(M)}
        ok &= len(seen) == M
        sizes.append(len(seen))
    check("P3 the digit map is injective on [0, M) at both small bases",
          ok, f"{sizes[0]} and {sizes[1]} distinct digit vectors")
    rounds = []
    for base, _, _ in SUITES:
        n = len(base)
        ready = [0] * n
        for i in range(1, n):
            t = 0
            for j in range(i):
                t = max(t, ready[j]) + 1
            ready[i] = t
        rounds.append(ready[-1])
    print(f"  P4 the presented conversion's last digit is final at round "
          f"{rounds}, n - 1 at n = {[len(b) for b, _, _ in SUITES]}")


def main():
    section_controls()
    if not all(CHECKS):
        print("\nCONTROL FAILED: nothing below is read.")
        raise SystemExit(1)
    section_exact()
    section_price()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
