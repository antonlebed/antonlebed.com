"""explore_dual_affine_class.py -- THE AFFINE CLASS AT THE LEADING END:
which monotone maps within a bounded distance of a line are exactly
window-local at the archimedean pole, and the sums of free divisions
that leave the numerator family.

THE OBJECT. The size window W_{b,t}(n) = (sign, exponent, t leading
base-b digits) reads an integer through its top; its fibers at
precision t' are the grid intervals [m b^j, (m+1) b^j) with m a
t'-digit number, deep when j >= 1. A map f is EXACTLY WINDOW-LOCAL at
lookahead c if at every precision t every fiber at precision t + c
maps into one window at precision t. For monotone f the image of a
fiber is an interval, so it straddles the output boundary B iff the
CROSSING n*(B) = min{n : f(n) >= B} sits strictly inside the fiber;
the output boundaries at precision t are the numbers M b^J with M a
t-digit number; so f is exactly local at lookahead c iff every
crossing of a boundary M b^J that lies in a deep fiber at precision
t + c is that fiber's left end, b^j | n*(M b^J) with j its depth
(explore_dual_locality.py, the boundary-preimage method).

WHAT IS KNOWN. explore_dual_locality.py read the arithmetic members:
floor((u/v) n) exactly local iff rad(u) | rad(b) (the numerator
criterion, at bases 2, 6, 10), floor((n+s)/v) exactly local iff s = 0
(the phase law), n + a graded for every a != 0 (the shift wall), and
the structural split -- fiber-permuting maps local and non-monotone --
with the arithmetic members conjectured to be exactly the numerator
family beyond the swept families (scalings, phases, shifts, powers).

THE QUESTION. (Q1) Is g(n) = floor(n/3) + floor(n/7) exactly local at
base 10, a monotone arithmetic map that is no floor((u n + s)/v)? (Q2)
Among monotone f with f(n) = lambda n + O(1), which are exactly local,
at any lookahead?

THE HAND ATTACK. Let f be nondecreasing with |f(n) - lambda n| <= C,
lambda > 0. For a boundary B the crossing obeys |n*(B) - B/lambda| <=
W := ceil(C/lambda) + 1, since f(n) >= B once lambda n >= B + C and
f(n) < B while lambda n < B - C.
  THE SLOPE THEOREM. If f is exactly local at lookahead c then lambda
= b^r / a for integers r >= 0, a >= 1: the reduced numerator of
lambda divides a power of b. Proof: take the exponent boundaries
B = b^J. n*(b^J) has at least J - L digits for a constant L (n* >=
b^J / lambda - W), so its fiber at precision 1 + c has depth at least
J - L - c, and alignment gives b^{J-L-c} | n*(b^J) once that depth is
positive. Then q_J := n*(b^J) / b^{J-L-c} is an integer and
q_J = b^{L+c} / lambda + theta b^{L+c-J} with |theta| <= W, so the
fixed real b^{L+c} / lambda is within W b^{L+c-J} of an integer at
every large J, hence is one: a := b^{L+c} / lambda.
  THE ALIGNMENT CONDITION. Write lambda = b^r / a. f is exactly local
at SOME lookahead iff there is K >= 0 such that for every positive
multiple N of a b^K: f(N) >= lambda N and f(N - 1) < lambda N, i.e.
the crossing of the boundary lambda N is exactly N. Only if: for
B = M b^J with J >= r the point N_0 = B/lambda = a M b^{J-r} is an
integer divisible by b^{J-r}; the crossing is within W of it and has
at least t + J - r - 1 digits for J large (constants independent of
M and t), so alignment at lookahead c gives b^{J-r-1-c} | n*; both
n* and N_0 are multiples of b^{J-r-1-c}, their difference is at most
W, so once b^{J-r-1-c} > W they are equal: n*(lambda N) = N for
every N = a M b^{J-r}, J >= J_0, which is every multiple of
a b^{J_0 - r}. If: with K given, for J >= r + K the crossing of
M b^J is a M b^{J-r}, a multiple of b^{J-r}, with at most
t + J - r + digits(a) digits, so its depth at precision t + c is at
most J - r once c >= digits(a) and it is aligned; the boundaries with
J < r + K have crossings within W of a number below b^{t+K+digits(a)-1},
hence of fewer than t + K + digits(a) + digits(W) digits, shallow at
precision t + c once c >= K + digits(a) + digits(W) - 1; so f is
exact at that lookahead, the crossing's own wobble W paying its
digits.
  THE COROLLARIES. floor((u/v) n) with rad(u) | rad(b): N a multiple
of a = v b^r / u gives f(N) = lambda N and f(N-1) = floor(lambda N -
lambda) < lambda N, so K = 0 -- the numerator criterion at every
base, both halves. floor((n+s)/v), 0 < s < v: f(N-1) = floor((N - 1 +
s)/v) = N/v = lambda N at every multiple of v, so the condition fails
at every K -- the phase law at every base. n + a: f(N-1) < N iff
a <= 0 and f(N) >= N iff a >= 0 -- the shift wall at every base.
  THE SUM CRITERION. f(n) = sum_i c_i floor(n/v_i) with c_i >= 1,
V = lcm(v_i), U = sum_i c_i V/v_i, lambda = U/V: f(n) <= lambda n
with equality iff V | n, and f(N-1) = lambda N - sum c_i < lambda N
at every such N; so the alignment condition holds at K iff V | a b^K
iff U | b^{r+K}; f is exactly local iff rad(U) | rad(b), U the
numerator OVER THE LCM, unreduced. At (3, 7), base 10: V = 21,
U = 10, exact; the crossing of M 10^J is 21 M 10^{J-1}, of
t + J or t + J + 1 digits, aligned at lookahead 2 and not at 1 when
21 M has t + 2 digits and 10 does not divide M. At (3, 6): U = 3,
lambda = 1/2, the reduced numerator 1 -- the slope condition holds
and the alignment condition fails, as it does for floor((n+1)/3): the
converse of the slope theorem is false and the sweep below counts
its failures. g is outside every phase floor((10 n + s)/21): those
maps stay within an interval of length under 1 of 10 n / 21, while
g(20) - 200/21 = -32/21 and g(21) - 10 = 0.

PREDICTIONS, FIXED BEFORE THE RUN (what the engine prints).
  C1 CONTROL: the locality rig's verdicts reproduce under this rig's
     crossing reader -- floor(2 n) exact and floor(3 n) graded at
     base 2, floor(n/3) exact and floor((n+1)/3) graded at base 10 --
     and every graded witness passes the definition-level pair test.
     KILL: any disagreement.
  E1 THE KILL PROBE: g at base 10 -- the brute sweep at t = 1, 2, 3
     over depths 1, 2 prints exceptions > 0 at lookahead 0 and 1 and
     0 at lookahead 2; the crossing scan at lookahead 2 over t = 1, 2
     and J <= 10 finds every deep crossing aligned, and n*(M 10^J) =
     21 M 10^{J-1} at every scanned M, J >= 1. KILL (of the probe, not
     of the theorem): a nonzero count at lookahead 2, or a misaligned
     deep crossing at lookahead 2.
  E2 THE SLOPE THEOREM'S STEP: the b-adic depth of n*(b^J) for J =
     1..14: at g, base 10, v_10 = J - 1 exactly; at g, base 2 (U =
     10, rough), v_2(n*(2^J)) stays at most 3 across the range; and
     at base 2 a deep misaligned crossing is constructed at every
     lookahead c <= 8. KILL: the base-2 depth climbing with J, or a
     lookahead with no witness.
  E3 THE SUM CRITERION SWEEP: over the 55 pairs 2 <= v1 < v2 <= 12 at
     bases 2, 6, 10 and six weighted sums at base 10, the crossing
     reader (least lookahead <= 10 at which every scanned deep
     crossing is aligned at t = 1, 2 and J <= c + 8, else a witness
     at every lookahead) agrees with rad(U) | rad(b) at every cell. The
     converse-failure count -- rad(u) | rad(b) for the reduced u but
     rad(U) does not divide rad(b) -- is at least 1 at bases 2 and 10
     ((3, 6) and (6, 12) at both). KILL: a cell where the reader
     disagrees with the criterion; a converse-failure count of 0 at
     both bases empties the E3 statement without killing it.
  E4 THE ALIGNMENT CONDITION READ DIRECTLY: at every cell of E3 and
     at the phases floor((n+s)/v), v = 3, 5, 7, s < v, and the shifts
     n + a, |a| <= 3, at bases 2 and 10, the condition (some K <= 8
     with f(N) >= lambda N and f(N-1) < lambda N at the first 400
     multiples N of a b^K) holds iff the crossing reader says exact,
     and at every exact cell the least lookahead is at most
     K + digits(a) + digits(W) - 1. KILL: a cell where the two
     disagree, or a least lookahead over the bound.
  E5 THE COROLLARIES: phases exact iff s = 0 and shifts exact iff
     a = 0, at both bases, by both readers. KILL: any other pattern.

Estimate: under a minute, exact integers throughout, trivial memory.
Stages (argv): none; the whole run is one pass.

FINDINGS (each at its own tier; the prints copied, the asserts read)

F1  THE CONTROLS HOLD. floor(2n) exact at c = 0 and floor(3n) graded
    with a witness at every c <= 10 at base 2; floor(n/3) exact at
    c = 1 and floor((n+1)/3) graded at every c <= 10 at base 10; every
    witness passed the pair test.
F2  THE KILL PROBE FIRES (rule, exact by the boundary-preimage method
    at the scanned scope; the theorem below carries it to every
    lookahead): g = floor(n/3) + floor(n/7), slope 10/21, is exactly
    local at base 10 at lookahead 2 -- the brute sweep at t = 1..3
    over depths 1, 2 prints 998, 1046 and 0 exceptions at lookahead
    0, 1, 2; the crossing scan at lookahead 2 finds every deep
    crossing aligned at 77 + 772 deep crossings (t = 1, 2, J <= 10);
    n*(M 10^J) = 21 M 10^{J-1} at all 792 scanned cells. g's
    deviation from 10n/21 spans [-32/21, 0], width 32/21 > 1, so it
    is no floor((10 n + s)/21): a monotone arithmetic map outside the
    numerator family and its phases is exactly local, and the
    conjecture that the arithmetic exact-local members are the
    numerator family is dead as stated.
F3  THE SLOPE THEOREM'S STEP READS AS DERIVED. v_10(n*(10^J)) = J - 1
    at every J = 1..14 for g at base 10; at base 2, where U = 10 is
    rough, v_2(n*(2^J)) over J = 1..14 is 1, 0, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 0, never above 1, and a deep misaligned crossing is
    constructed at every lookahead c <= 8 (n* = 6, 9, 9, 35, 35, 69,
    135, 539, 539 at the boundaries 2^J, J = 1, 2, 2, 4, 4, 5, 6, 8,
    8): the depth alignment demands climbs with J and the crossing's
    depth does not.
F4  THE SUM CRITERION HOLDS AT EVERY CELL (theorem by the hand attack;
    read at 171 cells): rad(U) | rad(b) with U the numerator over the
    lcm agrees with the crossing reader at all 171 (55 pairs at bases
    2, 6, 10 and six weighted sums at base 10), and the alignment
    condition read directly (some K <= 8) agrees with the reader at
    all 171. The converse of the slope theorem fails at 2 cells at
    base 2 and 3 at base 10 -- floor(n/3) + floor(n/6) and
    floor(n/6) + floor(n/12) at both, 3 floor(n/3) + floor(n/7) at
    base 10 (U = 24, reduced numerator 8) -- and at none at base 6.
    The exact cells' least lookahead (read at t = 1, 2, a lower bound
    on the true c*: explore_dual_least_lookahead.py reads c* = 4 at
    floor(n/3) + floor(n/9), base 2, where this scan reads 3, the deep
    witness first at t = 4) runs 1 to 6 and sits at or under
    K + digits(a) + digits(W) - 1 at every one of the 42 exact cells,
    meeting it at 15 ((3, 5) at base 10: a = 1875, W = 5,
    K = 0, c = 4 at the bound; (3, 7): a = 21, W = 6, c = 2 at the
    bound; (2, 6): a = 15, W = 4, K = 1, c = 2 under the bound 3).
F5  THE COROLLARIES REPRODUCE AS INSTANCES: floor((n+s)/v) exact iff
    s = 0 at v = 3, 5, 7 and n + a exact iff a = 0 at |a| <= 3, at
    bases 2 and 10, by the crossing reader and the alignment condition
    alike.

RUN RECORD (the estimate first, then what it cost)
Estimated under a minute; 11.8 s wall, peak working set 13 MB under
the 512 MB ceiling. The first run's reader scanned J <= 8 at every
lookahead and returned 15 false exact verdicts at base 2 plus three
in E5, every one a graded map whose few deep crossings at a high
lookahead happened to align -- the same shape as the locality rig's
pre-engine sweeps; the scan's J now runs to c + 8 with a floor on the
deep crossings seen, and the second run printed no kill. The
predictions were not touched. An audit round then added the
lookahead bound's check to E4, the bound corrected from
K + digits(a) to carry the crossing's wobble W; the rerun printed no
kill, 11.9 s.
"""
import os
import sys
import time
from fractions import Fraction
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_dual_locality import (ndigits, fiber_of, pair_witness,   # noqa: E402
                                   brute_exact, rad_divides)

KILLS = []


def kill(msg):
    KILLS.append(msg)
    print("  KILL:", msg)


def lcm(a, b):
    return a * b // gcd(a, b)


def vb(n, b):
    """The largest e with b^e | n (n > 0)."""
    e = 0
    while n % b == 0:
        n //= b
        e += 1
    return e


def digits(n, b):
    return ndigits(n, b) + 1


# ------------------------------------------------------------- the maps
class Affine:
    """A monotone map with f(n) = lam n + O(1): the map, its slope as a
    Fraction, a bound C on |f(n) - lam n|, and a name."""

    def __init__(self, name, f, lam, C):
        self.name, self.f, self.lam, self.C = name, f, Fraction(lam), C
        for n in range(1, 3000):
            assert abs(f(n) - self.lam * n) <= C, (name, n)
            assert f(n + 1) >= f(n), (name, n)


def sum_map(terms):
    """terms: list of (c_i, v_i) -> sum c_i floor(n / v_i)."""
    V = 1
    for _, v in terms:
        V = lcm(V, v)
    U = sum(c * V // v for c, v in terms)
    name = " + ".join(("%d*" % c if c > 1 else "") + "floor(n/%d)" % v
                      for c, v in terms)
    return Affine(name, lambda n: sum(c * (n // v) for c, v in terms),
                  Fraction(U, V), sum(c for c, _ in terms)), U, V


def scaling(u, v, s=0):
    return Affine("floor((%d n + %d)/%d)" % (u, s, v),
                  lambda n: (u * n + s) // v, Fraction(u, v), 1)


def shift(a):
    return Affine("n + %d" % a, lambda n: n + a, 1, abs(a))


# -------------------------------------------------------- the crossing
def crossing(m, B):
    """n*(B) = min{n >= 1 : f(n) >= B} by bisection on the monotone
    map, bracketed by the deviation bound."""
    f, lam, C = m.f, m.lam, m.C
    lo = max(1, int((B - C) / lam) - 1)
    while lo > 1 and f(lo) >= B:
        lo = max(1, lo // 2)
    hi = int((B + C) / lam) + 2
    while f(hi) < B:
        hi *= 2
    if f(lo) >= B:
        return lo
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if f(mid) >= B:
            hi = mid
        else:
            lo = mid
    return hi


def scan(m, b, t, c, Jmax):
    """Every boundary M b^J, M t-digit, 1 <= J <= Jmax: returns
    (all_aligned, witness, deep_count); a witness is a deep misaligned
    crossing, verified by the definition-level pair test."""
    deep = 0
    for J in range(1, Jmax + 1):
        for M in range(b ** (t - 1), b ** t):
            n = crossing(m, M * b ** J)
            lo, hi, j = fiber_of(n, b, t + c)
            if j >= 1:
                deep += 1
                if n != lo:
                    assert pair_witness(m.f, n, b, t, t + c), (m.name, n)
                    return False, (J, M, n), deep
    return True, None, deep


def least_lookahead(m, b, cmax=10, span=8):
    """The least c <= cmax at which every scanned deep crossing is
    aligned at t = 1 and 2 over J <= c + span, else None with a witness
    at every c. The scan's J runs with c so that the deep crossings
    seen never thin out as the lookahead grows: a scan at fixed J meets
    only a few deep crossings at a high lookahead and reads a graded
    map as exact when those few happen to align."""
    wits = []
    for c in range(cmax + 1):
        ok1, w1, d1 = scan(m, b, 1, c, c + span)
        ok2, w2, d2 = scan(m, b, 2, c, c + span)
        if ok1 and ok2:
            assert d1 >= (b - 1) * (span // 2), (m.name, b, c, d1)
            assert d2 >= b * (b - 1) * (span // 2), (m.name, b, c, d2)
            return c, wits
        wits.append(w1 or w2)
    return None, wits


# ------------------------------------------- the alignment condition
def slope_ok(m, b):
    return rad_divides(m.lam.numerator, b)


def split_slope(lam, b):
    """lam = b^r / a with r least: returns (r, a)."""
    u, v = lam.numerator, lam.denominator
    r = 0
    while (b ** r) % u:
        r += 1
    return r, v * b ** r // u


def alignment_K(m, b, Kmax=8, count=400):
    """The least K <= Kmax at which f(N) >= lam N and f(N-1) < lam N
    at the first `count` positive multiples N of a b^K; None if the
    slope condition fails or no K passes."""
    if not slope_ok(m, b):
        return None
    r, a = split_slope(m.lam, b)
    for K in range(Kmax + 1):
        step = a * b ** K
        good = True
        for q in range(1, count + 1):
            N = step * q
            if not (m.f(N) >= m.lam * N and m.f(N - 1) < m.lam * N):
                good = False
                break
        if good:
            return K
    return None


# -------------------------------------------------------------- the run
def main():
    t0 = time.time()
    print("=== C1 the controls: the locality rig's verdicts under the "
          "crossing reader")
    for (mp, b, want) in [(scaling(2, 1), 2, True), (scaling(3, 1), 2, False),
                          (scaling(1, 3), 10, True),
                          (scaling(1, 3, 1), 10, False)]:
        c, wits = least_lookahead(mp, b)
        verdict = c is not None
        print("  %-24s base %2d: %s" % (mp.name, b,
              "exact at c=%d" % c if verdict else
              "graded, witnesses at c=0..%d" % (len(wits) - 1)))
        if verdict != want:
            kill("C1 %s base %d" % (mp.name, b))

    print("=== E1 the kill probe: g = floor(n/3) + floor(n/7) at base 10")
    g, U, V = sum_map([(1, 3), (1, 7)])
    print("  slope %s, U = %d over V = %d" % (g.lam, U, V))
    for c in (0, 1, 2):
        exc = sum(brute_exact(g.f, 10, t, c, depths=(1, 2)) for t in (1, 2, 3))
        print("  brute sweep t=1..3 depths 1,2 lookahead %d: %d exceptions"
              % (c, exc))
        if (exc == 0) != (c == 2):
            kill("E1 brute count at c=%d is %d" % (c, exc))
    for t in (1, 2):
        ok_, w, deep = scan(g, 10, t, 2, 10)
        print("  crossing scan t=%d c=2 J<=10: aligned=%s deep=%d" % (t, ok_, deep))
        if not ok_:
            kill("E1 misaligned deep crossing at c=2: %s" % (w,))
    bad = [(M, J) for t in (1, 2) for J in range(1, 9)
           for M in range(10 ** (t - 1), 10 ** t)
           if crossing(g, M * 10 ** J) != 21 * M * 10 ** (J - 1)]
    print("  n*(M 10^J) = 21 M 10^(J-1) fails at %d of %d cells" % (len(bad), 8 * 99))
    if bad:
        kill("E1 crossing formula: %s" % bad[:5])
    dev = [g.f(n) - g.lam * n for n in range(0, 22)]
    print("  g - 10n/21 over one period: min %s max %s, width %s"
          % (min(dev), max(dev), max(dev) - min(dev)))
    c_g, _ = least_lookahead(g, 10)
    print("  least lookahead by the crossing reader: %s" % c_g)

    print("=== E2 the slope theorem's step: b-adic depth of n*(b^J)")
    for b in (10, 2):
        row = [vb(crossing(g, b ** J), b) for J in range(1, 15)]
        print("  base %2d  v_b(n*(b^J)), J=1..14: %s" % (b, row))
        if b == 10 and row != [J - 1 for J in range(1, 15)]:
            kill("E2 base 10 depth is not J-1")
        if b == 2 and max(row) > 3:
            kill("E2 base 2 depth exceeds 3: %d" % max(row))
    c2, wits = least_lookahead(g, 2, cmax=8)
    print("  g at base 2: %s" % ("exact at c=%d" % c2 if c2 is not None
                                 else "graded, witnesses (J, M, n*) at c=0..8: %s"
                                 % wits))
    if c2 is not None:
        kill("E2 g exact at base 2")

    print("=== E3 the sum criterion sweep, and E4 the alignment condition")
    cells = []
    for b in (2, 6, 10):
        for v1 in range(2, 13):
            for v2 in range(v1 + 1, 13):
                cells.append((b, [(1, v1), (1, v2)]))
    for terms in ([(2, 3), (1, 7)], [(3, 3), (1, 7)], [(2, 3), (2, 7)],
                  [(1, 2), (1, 5), (1, 10)], [(1, 2), (1, 3), (1, 7)],
                  [(1, 3), (1, 7), (1, 21)]):
        cells.append((10, terms))
    agree = 0
    e4_agree = 0
    n_exact = at_bound = 0
    conv = {2: [], 6: [], 10: []}
    rows = []
    for b, terms in cells:
        m, U, V = sum_map(terms)
        pred = rad_divides(U, b)
        c, wits = least_lookahead(m, b)
        K = alignment_K(m, b)
        read = c is not None
        if read == pred:
            agree += 1
        else:
            kill("E3 base %d %s: criterion %s, reader %s" % (b, m.name, pred, read))
        if (K is not None) == read:
            e4_agree += 1
        else:
            kill("E4 base %d %s: condition K=%s, reader %s" % (b, m.name, K, read))
        if read:
            r_, a_ = split_slope(m.lam, b)
            W = -((-m.C) // m.lam) + 1
            bound = K + digits(a_, b) + digits(W, b) - 1
            n_exact += 1
            if c == bound:
                at_bound += 1
            if c > bound:
                kill("E4 base %d %s: c=%d over the bound %d" % (b, m.name, c, bound))
        if slope_ok(m, b) and not pred:
            conv[b].append(m.name)
        rows.append((b, m.name, U, V, pred, c, K))
    print("  %d cells; criterion and crossing reader agree at %d; alignment "
          "condition and reader agree at %d" % (len(cells), agree, e4_agree))
    print("  exact cells %d, least lookahead at the bound K + digits(a) + "
          "digits(W) - 1 at %d, never over it" % (n_exact, at_bound))
    for b in (2, 6, 10):
        print("  base %2d converse failures (slope holds, U rough): %d %s"
              % (b, len(conv[b]), conv[b]))
    if not conv[2] or not conv[10]:
        kill("E3 converse failures absent at base 2 or 10")
    print("  the exact cells (base, map, U/V, least c, K):")
    for b, name, U, V, pred, c, K in rows:
        if pred:
            print("    %2d  %-40s %3d/%-3d c=%s K=%s" % (b, name, U, V, c, K))

    print("=== E5 the corollaries: phases and shifts by both readers")
    for b in (2, 10):
        for v in (3, 5, 7):
            pat = []
            for s in range(v):
                m = scaling(1, v, s)
                c, _ = least_lookahead(m, b)
                K = alignment_K(m, b)
                pat.append((c is not None, K is not None))
            print("  base %2d floor((n+s)/%d), s=0..%d: (reader, condition) %s"
                  % (b, v, v - 1, pat))
            if pat != [(True, True)] + [(False, False)] * (v - 1):
                kill("E5 phases at base %d v=%d" % (b, v))
        pat = []
        for a in range(-3, 4):
            m = shift(a)
            c, _ = least_lookahead(m, b)
            K = alignment_K(m, b)
            pat.append((a, c is not None, K is not None))
        print("  base %2d n + a, a=-3..3: %s" % (b, pat))
        if [(x, y) for _, x, y in pat] != [(False, False)] * 3 + [(True, True)] + [(False, False)] * 3:
            kill("E5 shifts at base %d" % b)

    print("=== KILLS: %s" % (KILLS if KILLS else "none"))
    print("wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
