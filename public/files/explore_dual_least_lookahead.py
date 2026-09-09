"""explore_dual_least_lookahead.py -- THE LEAST LOOKAHEAD OF AN EXACT
AFFINE MAP AT THE LEADING END: the digit count the deep boundaries
force, and whether anything else is ever needed.

THE OBJECT. The size window at base b and precision t reads a positive
integer through its t leading digits; a map f is EXACTLY WINDOW-LOCAL
at lookahead c if the t leading digits of f(n) are a function of the
t + c leading digits of n, at every t. For monotone f the test is the
crossings: with n*(B) = min{n : f(n) >= B}, f is exactly local at
lookahead c iff every crossing of an output boundary M b^J (M a
t-digit number) that lies in a deep fiber at precision t + c -- a
fiber [m b^j, (m+1) b^j) with j >= 1 -- is that fiber's left end
(explore_dual_locality.py). The least such c is c*(f, b).

WHAT IS KNOWN (explore_dual_affine_class.py). For monotone f with
|f(n) - lambda n| <= C, exactness at some lookahead holds iff lambda =
b^r / a (r >= 0 least, a >= 1) and, for some K, every positive
multiple N of a b^K has f(N) >= lambda N > f(N - 1): the crossing of
lambda N is N itself. The least such K is written K below. That rig
read c* at 42 exact cells and found it at most K + digits(a) +
digits(W) - 1, W = ceil(C / lambda) + 1 the crossing's distance bound,
met at 15 cells; c* itself was not derived.

THE HAND ATTACK. Write d = digits_b(a), m = v_b(a) and a' = a / b^m,
the part of a prime to b.
  THE DEEP LAYER. For J >= r + K the crossing of M b^J is exactly
N = a M b^{J-r}. Its fiber at precision t + c has depth j = digits(aM)
+ J - r - t - c, positive for J large, and N is aligned iff b^j | N
iff j <= v_b(aM) + J - r. So a deep misaligned crossing exists at
lookahead c iff c < D(M) := digits_b(aM) - t - v_b(aM) for some t and
t-digit M, at EVERY large J, and
    c* >= c_deep := max over t, M of D(M).
digits_b(aM) - t is d - 1 plus one when the product overflows into a
fresh digit, and v_b(aM) = m + v_b(M); so c_deep = d - m = digits_b(a')
when some M prime to b overflows, which happens for t large exactly
when a' >= 2 (the overflow interval [b^{d+t-1}/a, b^t) has length at
least b^t/(b^{d-1} + 1) - 1 and contains a unit mod b once that
exceeds b); when a' = 1 the product never overflows and c_deep = 0.
    c_deep = digits_b(a') - [a' = 1].
  THE SHALLOW LAYER. For J < r + K the crossing sits within W of
a M b^{J-r} < a b^{t+K-1}, so n* < b^{d+t+K-1} + W, which is below
b^{d+t+K} whenever W <= (b - 1) b^{d+t+K-1}, i.e. for every t >= t_1
with t_1 the least t making that true. There digits(n*) <= d + t + K -
1 and the fiber depth at precision t + c is at most d + K - 1 - c: no
shallow-layer crossing is deep at c >= d + K - 1, hence
    c* <= max(c_deep, d + K - 1)   once the t < t_1 cells are checked,
sharper than the old bound by digits(W). At K = 0 with b not dividing
a (m = 0, a' = a >= 2): c_deep = d and the shallow layer is shallow at
every c >= d - 1 < d for t >= t_1, so
    THE LEAST-LOOKAHEAD LAW: c* = digits_b(a) when K = 0 and b does
    not divide a, given the finitely many boundaries at t < t_1 hold
    no deep misaligned crossing at c = d (a finite check per cell).
Where K >= 1 or b | a the shallow layer can exceed c_deep and c* sits
in [c_deep, max(c_deep, d + K - 1)], decided by the shallow crossings
at J < r + K alone.
  WHAT THE OLD RIG CANNOT SEE. It scans t = 1 and 2 only; the deep
witness at c_deep - 1 needs an M prime to b in the overflow interval,
which may first exist at a t past 2 for some a (a = 9 at base 2 needs
t = 4: 9M >= 2^(t+3) with M odd first at M = 15). So the old reading
can sit BELOW c* by the rig's own reach, and this rig scans t up to
max(3, t_ov), t_ov computed from a and b, with the formula in hand.

THE READERS. c_deep by the formula. c_scan: the least c <= 10 at
which every deep crossing of every boundary M b^J, J = 0..r + K + 6,
M a t-digit number, t = 1..max(3, t_ov), is aligned; a scan whose J runs with
c is not needed here since the deep layer's verdict is the formula's
and the scan only certifies it. The deciding crossing at c_scan - 1
is printed with its layer (deep: J >= r + K; shallow: J < r + K). A
crossing with f(n* - 1) = 0 is no witness, zero having no window,
the convention of every reader in this family.
The finite check for the law: at every K = 0, b-coprime cell, every
boundary with t < t_1 and J < r scanned at c = d.

PREDICTIONS, FIXED BEFORE THE RUN (what the engine prints).
  C1 CONTROL: the old rig's least_lookahead reproduces its record --
     42 exact cells among the 171, the bound K + digits(a) + digits(W)
     - 1 met at 15 -- and at the four control maps floor(2n) reads 0
     and floor(3n) graded at base 2, floor(n/3) reads 1 and
     floor((n+1)/3) graded at base 10. KILL: any other count.
  E1 THE LOWER BOUND: c_scan >= c_deep at every exact cell, and at
     every exact cell with c_deep >= 1 a deep-layer misaligned
     crossing is exhibited at c = c_deep - 1 at some t <= max(3, t_ov),
     t_ov the least t whose overflow interval holds a unit. KILL: a
     cell with c_scan < c_deep, or one with no deep witness at c_deep
     - 1 (which would mean the overflow argument needs t > 3 there;
     a KILL of the rig's reach, named as such, not of the bound).
  E2 THE LAW: at every exact cell with K = 0 and b not dividing a,
     c_scan = digits_b(a) and the t < t_1 finite check passes. KILL:
     one such cell off the formula.
  E3 THE UPPER BOUND: c_scan <= max(c_deep, d + K - 1) at every exact
     cell, and the count of cells where c_scan > c_deep is printed with
     the deciding shallow crossing's J < r + K at each. KILL: a cell
     over the bound.
  E4 THE OLD RIG'S REACH: the cells where the t = 1, 2 reading sits
     below c_scan are listed; predicted few or none, every one a cell
     whose overflow unit first appears past t = 2. KILL: a listed cell
     whose gap is not explained by a deep witness at t > 2.

Estimate: two to four minutes, exact integers, trivial memory.
Stages (argv): none.

FINDINGS (each at its own tier; the prints copied, the asserts read)

F1  THE CONTROL HOLDS: 42 exact cells, the old bound met at 15, the
    four maps reading 0, graded, 1, graded.
F2  THE DEEP LOWER BOUND HOLDS AT EVERY CELL (theorem by the hand
    attack; E1, 0 kills): c_scan >= c_deep at all 42, and a deep-layer
    misaligned crossing at c_deep - 1 was exhibited at every cell at
    some t <= max(3, t_ov); t_ov is at most 2 everywhere but at
    floor(n/3) + floor(n/9), base 2, where it is 4 and the deciding
    crossing prints at t = 4 (the first odd M with 9M past 2^{t+3} is
    15).
F3  THE LEAST-LOOKAHEAD LAW HOLDS AT ALL 30 LAW CELLS (theorem for
    maps with W <= (b - 1) b^d, which every law cell satisfies, so the
    t < t_1 check is empty at every one; E2, 0 kills): c* = digits_b(a)
    at K = 0 and b coprime to a, the deciding crossing deep at every
    one.
F4  THE UPPER BOUND HOLDS (E3, 0 kills): c_scan <= max(c_deep, d + K -
    1) at all 42; c_scan exceeds c_deep at exactly 2 cells, floor(n/4)
    + floor(n/12) at bases 6 and 10 (a = 3, K = 2, c_deep = 1, c* = 2),
    the shallow layer deciding, as it does at 5 further cells where it
    ties the deep layer's reading.
F5  THE OLD READING SITS BELOW c* AT ONE CELL (E4, 0 kills): floor(n/3)
    + floor(n/9) at base 2 read 3 at t <= 2 and c* is 4, the deep
    witness needing t = 4; the other 41 agree. That cell's old bound
    K + digits(a) + digits(W) - 1 = 6 still holds it.

RUN RECORD (the estimate first, then what it cost)
Estimated two to four minutes; 2.0 s wall, peak working set 12.8 MB.
The rig was designed in the morning and run in the afternoon, its
predictions untouched between.
"""
import os
import sys
import time
from fractions import Fraction
from math import ceil, gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_dual_locality import fiber_of, pair_witness           # noqa: E402
from explore_dual_affine_class import (sum_map, scaling, crossing,  # noqa: E402
                                       least_lookahead, slope_ok,
                                       split_slope, alignment_K,
                                       digits, vb)

KILLS = []


def kill(msg):
    KILLS.append(msg)
    print("  KILL:", msg)


def t_overflow(a, b):
    """The least t at which some t-digit M prime to b has aM carrying
    one digit more than a b^(t-1) does; None when a is a power of b."""
    d = digits(a, b)
    if a == b ** (d - 1):
        return None
    t = 1
    while True:
        lo = -(-b ** (d + t - 1) // a)
        if any(gcd(M, b) == 1 for M in range(lo, b ** t)):
            return t
        t += 1


def deciding(m, b, c, Jmax, tmax=3, Jmin=0):
    """The first deep misaligned crossing at lookahead c over t <= tmax,
    J = Jmin..Jmax, as (t, J, M, n*), or None."""
    for t in range(1, tmax + 1):
        for J in range(Jmin, Jmax + 1):
            for M in range(b ** (t - 1), b ** t):
                n = crossing(m, M * b ** J)
                lo, hi, j = fiber_of(n, b, t + c)
                if j >= 1 and n != lo and m.f(n - 1) != 0:
                    assert pair_witness(m.f, n, b, t, t + c), (m.name, n)
                    return (t, J, M, n)
    return None


def c_scan(m, b, Jmax, tmax, cmax=10):
    """The least c <= cmax with no deep misaligned crossing at t <= tmax,
    J <= Jmax, with the deciding crossing at c - 1."""
    last = None
    for c in range(cmax + 1):
        w = deciding(m, b, c, Jmax, tmax)
        if w is None:
            return c, last
        last = w
    return None, last


def cells():
    out = []
    for b in (2, 6, 10):
        for v1 in range(2, 13):
            for v2 in range(v1 + 1, 13):
                out.append((b, sum_map([(1, v1), (1, v2)])[0]))
    for terms in ([(2, 3), (1, 7)], [(3, 3), (1, 7)], [(2, 3), (2, 7)],
                  [(1, 2), (1, 5), (1, 10)], [(1, 2), (1, 3), (1, 7)],
                  [(1, 3), (1, 7), (1, 21)]):
        out.append((10, sum_map(terms)[0]))
    return out


def main():
    t0 = time.time()
    print("=== C1 the control: the old rig's record and the four maps")
    for (mp, b, want) in [(scaling(2, 1), 2, 0), (scaling(3, 1), 2, None),
                          (scaling(1, 3), 10, 1), (scaling(1, 3, 1), 10, None)]:
        c, _ = least_lookahead(mp, b)
        print("  %-24s base %2d: %s" % (mp.name, b, c))
        if c != want:
            kill("C1 %s base %d reads %s" % (mp.name, b, c))
    rows = []
    n_exact = n_bound = 0
    for b, m in cells():
        if not slope_ok(m, b):
            continue
        K = alignment_K(m, b)
        if K is None:
            continue
        c_old, _ = least_lookahead(m, b)
        if c_old is None:
            kill("C1 alignment holds but the old reader says graded: %s base %d"
                 % (m.name, b))
            continue
        r, a = split_slope(m.lam, b)
        W = ceil(Fraction(m.C) / m.lam) + 1
        n_exact += 1
        if c_old == K + digits(a, b) + digits(W, b) - 1:
            n_bound += 1
        rows.append((b, m, r, a, K, W, c_old))
    print("  exact cells %d (record 42), old bound met at %d (record 15)"
          % (n_exact, n_bound))
    if (n_exact, n_bound) != (42, 15):
        kill("C1 record not reproduced")

    print("=== E1-E4 the least lookahead against the deep formula")
    print("  %-34s b  r     a  K  d  m  cdeep cscan cold  W tov layer  witness"
          % "map")
    e1_bad = e2_bad = e3_bad = e4_bad = 0
    n_law = n_shallow = n_gap = 0
    for b, m, r, a, K, W, c_old in rows:
        mm = vb(a, b)
        ap = a // b ** mm
        d = digits(a, b)
        c_deep = digits(ap, b) - (1 if ap == 1 else 0)
        Jmax = r + K + 6
        t_ov = t_overflow(a, b)
        tmax = max(3, t_ov or 0)
        cs, wit = c_scan(m, b, Jmax, tmax)
        layer = "-"
        if wit is not None:
            layer = "deep" if wit[1] >= r + K else "shallow"
        print("  %-34s %d %2d %5d %2d %2d %2d  %2d    %2d   %2d  %3d %2s %-7s %s"
              % (m.name, b, r, a, K, d, mm, c_deep, cs, c_old, W, t_ov, layer, wit))
        if cs is None:
            kill("scan found no lookahead <= 10 at %s base %d" % (m.name, b))
            continue
        # E1: the lower bound and its witness
        if cs < c_deep:
            e1_bad += 1
            kill("E1 c_scan %d < c_deep %d at %s base %d" % (cs, c_deep, m.name, b))
        if c_deep >= 1:
            w = deciding(m, b, c_deep - 1, Jmax, tmax, Jmin=r + K)
            if w is None:
                e1_bad += 1
                kill("E1 no deep-layer witness at c = %d: %s base %d, got %s"
                     % (c_deep - 1, m.name, b, w))
        # E2: the law at K = 0, b coprime to a
        if K == 0 and a % b:
            n_law += 1
            t1 = 1
            while W > (b - 1) * b ** (d + t1 + K - 1):
                t1 += 1
            fin = None
            for t in range(1, t1):
                for J in range(0, r):
                    for M in range(b ** (t - 1), b ** t):
                        n = crossing(m, M * b ** J)
                        lo, hi, j = fiber_of(n, b, t + d)
                        if j >= 1 and n != lo and m.f(n - 1) != 0:
                            fin = (t, J, M, n)
            if cs != d or fin is not None:
                e2_bad += 1
                kill("E2 law fails: %s base %d c_scan %d digits %d finite %s"
                     % (m.name, b, cs, d, fin))
        # E3: the upper bound
        if cs > max(c_deep, d + K - 1):
            e3_bad += 1
            kill("E3 over the bound at %s base %d: %d > %d"
                 % (m.name, b, cs, max(c_deep, d + K - 1)))
        if cs > c_deep:
            n_shallow += 1
            if layer != "shallow":
                kill("E3 c_scan above c_deep but the deciding crossing is deep: %s"
                     % m.name)
        # E4: the old rig's reach
        if c_old != cs:
            n_gap += 1
            if c_old > cs or wit is None or wit[0] <= 2:
                e4_bad += 1
                kill("E4 old reading %d vs scan %d at %s base %d, witness %s"
                     % (c_old, cs, m.name, b, wit))
    print("  cells: %d exact; law cells (K = 0, b coprime to a): %d; "
          "c_scan > c_deep at %d; old reading differs at %d"
          % (len(rows), n_law, n_shallow, n_gap))
    print("  kills: E1 %d, E2 %d, E3 %d, E4 %d" % (e1_bad, e2_bad, e3_bad, e4_bad))
    print("KILLS: %d" % len(KILLS))
    for k in KILLS:
        print("  -", k)
    print("wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
