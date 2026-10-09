"""rank2.py -- the rank-2 flattening lattice: its least height, its
second minimum, and the gap between them.

QUESTION. At width M = J + 2 the integer polynomials of degree < M that
vanish to order J at 1 are exactly (a + b x)(x - 1)^J, a lattice of
rank 2. What is its least height (sup norm of the coefficients), what
attains it, how far above it does the next independent vector sit, and
is the least height the height of a product of factors x^d - 1?

THE OBJECTS. c_k = C(J, k), zero outside 0 <= k <= J. The coefficient
of x^k in (a + b x)(x - 1)^J is (-1)^(J-k) (a c_k - b c_{k-1}), so the
height is H(a, b) = max_k |a c_k - b c_{k-1}|, k = 0..J+1. N = c_m with
m = floor(J/2) is the row's largest entry, attained first at m, and
D = max_k |c_k - c_{k-1}| is the largest adjacent difference.

THE PROOF, written before the engine (theorem, every J >= 2).
  (i) Symmetries. H(a, b) = H(-a, -b), and the row's palindrome
      c_k = c_{J-k} sends index k to J + 1 - k and gives
      H(a, b) = H(b, a).
  (ii) D <= N - 1. For 1 <= k <= J the difference c_k - c_{k-1} is
      below max(c_k, c_{k-1}) <= N in absolute value because both are
      at least 1, and the end terms are c_0 = 1 and c_J = 1; N >= 2 at
      J >= 2 finishes it. (At J = 1, N = 1 and (1, 0) ties (1, 1).)
  (iii) Opposite signs or a zero coordinate. At k = m,
      |a c_m - b c_{m-1}| = |a| N + |b| c_{m-1} >= N when a != 0, and
      when a = 0 the index k = m + 1 gives |b| N >= N.
  (iv) Same sign, a != b. By (i) take a > b >= 1. At k = m the row is
      still strictly rising, c_{m-1} < c_m, so
      a c_m - b c_{m-1} = (a - b) N + b (c_m - c_{m-1}) >= N + 1.
  (v) a = b = t. H = |t| D.
  So H >= N > D off the line a = b, H = |t| D on it, and the least
  height is D, attained only at +-(1, 1): h(J + 2, J) = D with the
  unique minimiser +-(1 + x)(x - 1)^J. Among vectors independent of
  (1, 1), (iv) gives at least N + 1 and (iii) gives exactly N only
  when |a| N + |b| c_{m-1} = N, i.e. (a, b) = +-(1, 0), or when a = 0
  and |b| = 1; so the second minimum is lambda_2 = N, attained there
  and nowhere else among independent vectors (a multiple t(1, 1) of
  the minimiser reaches N too whenever tD = N).
  (vi) The pure products at rank 2 with at least J parts and degree at
      most J + 1 are (x - 1)^J, (x - 1)^(J+1) and (x - 1)^(J-1)(x^2 - 1),
      cofactors 1, x - 1 and 1 + x, of heights N, C(J+1, floor((J+1)/2))
      and D; so ph = D = h and no rank-2 cell fails.

THE SLATE (predictions, fixed before the run).
  P1 A complete search of every (a, b) with H(a, b) <= N, at J = 2..16,
     finds the minimum D at +-(1, 1) only, and the independent vectors
     at height N exactly +-(1, 0), +-(0, 1).
  P2 The general lattice route (flatten.py) prints h(J + 2, J) = D at
     J = 2..30.
  P3 (TRANSPLANT from an older record) The ratio
     lambda_2 / lambda_1 = (sqrt(e)/2) sqrt(J + 1) (1 + eps_J) with
     -1/(J + 1) < eps_J <= 5/(2(J + 1)) at every J = 2..4000, eps at
     J = 10 near 0.0241 and at J = 2000 near 0.000075.
KILLS. K1: a pair other than +-(1, 1) at height <= D, or an
independent pair at height N other than the four. K2: an eps_J outside
its band. K3: the lattice route off D.

THE SEARCH (why it is complete). |a| = |a c_0| <= H, so |a| <= N; and
at k = m, |a N - b c_{m-1}| <= H confines b to an interval of length
2N / c_{m-1} around a N / c_{m-1}. Every pair in the box so cut is
scored.

CONTROL. The search at J = 2..16 must also find every multiple t(1, 1)
with tD <= N (a positive control on the search's reach).

FINDINGS (copied from the printed output).
  F1 THE SEARCH (P1 holds, K1 never fired). At every J = 2..16 the
     least height is D at +-(1, 1) alone and the independent vectors at
     height N are exactly +-(1, 0), +-(0, 1): D, N = 1, 2 at J = 2;
     90, 252 at J = 10; 3640, 12870 at J = 16. The control found every
     multiple t(1, 1) with tD <= N; with the four independent vectors
     they make the 6, 8 or 10 pairs at height <= N each depth prints.
  F2 THE ROUTE (P2 holds, K3 never fired). The general lattice route
     prints h(J + 2, J) = D at every J = 2..30.
  F3 THE RATIO (P3 holds, K2 never fired). Over J = 2..4000,
     (J + 1) eps_J lies in [-0.4166, 1.2022], inside (-1, 5/2]; eps is
     +0.400723 at J = 2, +0.024105 at J = 10, -0.004146 at J = 99,
     +0.008928 at J = 100 (the parity swing), +0.000075 at J = 2000
     and +0.000038 at J = 4000, where (J + 1) eps reads 0.1504.
  F4 THE HILL CLIMB equals the full row scan at every J = 2..300.

RUN RECORD. A first run walked the whole row at every depth and cost
389.5 s (peak working set 14.9 MB); the unimodal hill climb replaced it
with every figure unchanged, 2.2 s, peak 11.9 MB, under a memory guard.
"""
import sys
import time
from math import comb
from decimal import Decimal, getcontext

import flatten

getcontext().prec = 50


def row(J):
    return [comb(J, k) for k in range(J + 1)]


def H(a, b, c):
    J = len(c) - 1
    best = 0
    for k in range(J + 2):
        ck = c[k] if k <= J else 0
        ck1 = c[k - 1] if k >= 1 else 0
        best = max(best, abs(a * ck - b * ck1))
    return best


def step(n, k):
    """c_k - c_{k-1} for the row of J = n - 1, as C(n, k)(n - 2k)/n."""
    return comb(n, k) * (n - 2 * k) // n


def minima(J):
    """(D, N). The step g(k) = C(n, k)(n - 2k)/n, n = J + 1, has
    g(k+1)/g(k) = ((n - k)/(k + 1)) ((n - 2k - 2)/(n - 2k)) on
    0 <= k < n/2 - 1, a product of two factors decreasing in k, so it is
    unimodal on the rising half and a hill climb from any start finds
    its maximum; the falling half mirrors it."""
    n = J + 1
    top = (n - 1) // 2 if n % 2 else n // 2 - 1
    k = min(top, max(0, int(n / 2 - n ** 0.5 / 2)))
    g = step(n, k)
    while k < top and step(n, k + 1) > g:
        k += 1
        g = step(n, k)
    while k > 0 and step(n, k - 1) > g:
        k -= 1
        g = step(n, k)
    return max(g, 1), comb(J, J // 2)


def search(J):
    """Every (a, b) != (0, 0) with H(a, b) <= N, by the strip."""
    c = row(J)
    m = J // 2
    N, cm1 = c[m], c[m - 1]
    out = []
    for a in range(-N, N + 1):
        lo = (a * N - N) // cm1 - 1
        hi = (a * N + N) // cm1 + 1
        for b in range(lo, hi + 1):
            if (a, b) != (0, 0):
                v = H(a, b, c)
                if v <= N:
                    out.append((v, a, b))
    return out


def main():
    t0 = time.time()
    k1 = ctrl = 0
    for J in range(2, 17):
        D, N = minima(J)
        found = search(J)
        mins = [(a, b) for (v, a, b) in found if v == D]
        low = [(a, b) for (v, a, b) in found if v < D]
        indep = sorted((a, b) for (v, a, b) in found if a != b and v == N)
        below = [(a, b) for (v, a, b) in found if a != b and v < N]
        mult = sorted(a for (v, a, b) in found if a == b)
        want = sorted(t for t in range(-N, N + 1) if t and abs(t) * D <= N)
        if (low or sorted(mins) != [(-1, -1), (1, 1)] or below
                or indep != [(-1, 0), (0, -1), (0, 1), (1, 0)]):
            k1 += 1
        if mult != want:
            ctrl += 1
        print("J=%2d  D=%5d  N=%5d  pairs at height <= N: %3d  minimisers %s"
              "  independent at N %s" % (J, D, N, len(found), sorted(mins),
                                         indep))
    print("P1: K1 fired %d times; control (multiples t(1,1), tD <= N) off %d"
          % (k1, ctrl))

    off = 0
    for J in range(2, 301):
        c = row(J)
        full = max(abs(c[k] - (c[k - 1] if k else 0)) for k in range(J + 1))
        if (full, c[J // 2]) != minima(J):
            off += 1
    print("control: the hill climb equals the full row scan at J = 2..300,"
          " %d off" % off)

    k3 = 0
    for J in range(2, 31):
        h, v, _ = flatten.least_height(J + 2, J)
        if h != minima(J)[0]:
            k3 += 1
            print("K3 at J=%d: %d against %d" % (J, h, minima(J)[0]))
    print("P2: the lattice route at J = 2..30, K3 fired %d times" % k3)

    k2 = 0
    lo_w = hi_w = None
    c0 = Decimal(1).exp().sqrt() / 2
    for J in range(2, 4001):
        D, N = minima(J)
        n = J + 1
        eps = (Decimal(N) / Decimal(D)) / (c0 * Decimal(n).sqrt()) - 1
        ne = float(eps * n)
        if not (-1 < ne <= 2.5):
            k2 += 1
            print("K2 at J=%d: n eps = %.4f" % (J, ne))
        lo_w = ne if lo_w is None else min(lo_w, ne)
        hi_w = ne if hi_w is None else max(hi_w, ne)
        if J in (2, 10, 99, 100, 2000, 4000):
            print("  J=%4d  eps=%+.6f  (J+1) eps=%+.4f" % (J, eps, ne))
    print("P3: J = 2..4000, K2 fired %d times; (J+1) eps in [%.4f, %.4f]"
          % (k2, lo_w, hi_w))
    print("wall %.1f s" % (time.time() - t0))
    return k1 + ctrl + off + k3 + k2


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
