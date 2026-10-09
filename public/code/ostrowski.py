"""
ostrowski.py -- the trailing Ostrowski numeration read as a numeration
of the circle, and what that decides for every affine integer map and
every floor division, at every irrational alpha.

QUESTION. Fix an irrational alpha in (0, 1) with continued fraction
[0; a_1, a_2, ...], denominators q_(-1) = 0, q_0 = 1, q_(k+1) =
a_(k+1) q_k + q_(k-1), numerators p_k likewise, and remainders
theta_k = q_k alpha - p_k (theta_(-1) = -1), which alternate in sign
and shrink. Every n >= 0 has one greedy OSTROWSKI string n = sum d_k
q_k with 0 <= d_0 <= a_1 - 1, 0 <= d_k <= a_(k+1), and d_(k-1) = 0
whenever d_k = a_(k+1). Its depth-t TILE is the set of integers
sharing d_0 .. d_(t-1). A reader of f at lookahead c sees the input's
depth-(t + c) tile and commits the output's depth-t tile. Which maps
read, at what lookahead, and does anything depend on alpha beyond its
first quotients? In particular: does a non-periodic alpha put floor
division in the MIDDLE class (finite lookahead at every depth,
unbounded), as a sparse divisor chain does?

THE ARGUMENT (written before this script).
  (1) THE CIRCLE NUMERATION. Write r for the value of a depth-t
      prefix, 0 <= r < q_t (there are q_t legal prefixes). The legal
      tails from position t have real stars sum_(k>=t) d_k theta_k
      filling the open interval between -theta_t and -theta_(t-1)
      when d_(t-1) = 0 (the extreme tails being (0, a_(t+2), 0,
      a_(t+4), ...) and (a_(t+1), 0, a_(t+3), 0, ...), by the
      telescoping a_(k+1) theta_k = theta_(k+1) - theta_(k-1)), and
      between -theta_t and -theta_(t-1) - theta_t when d_(t-1) != 0
      (the cap at position t then barred); position 0 behaves as if
      d_(-1) != 0, its cap being a_1 - 1. So the prefix-r tile is the
      arc r alpha + (that interval) of the circle R/Z, of length
      |theta_(t-1)| + |theta_t| (d_(t-1) = 0, which is r < q_(t-1))
      or |theta_(t-1)|, and n lies in it iff n alpha mod 1 does. Its
      endpoints are r alpha - theta_t = -(q_t - r) alpha mod 1 and
      -(q_(t-1) - r) alpha or -(q_(t-1) + q_t - r) alpha mod 1: every
      endpoint is -j alpha with 1 <= j <= q_t. The lengths sum to
      q_t |theta_(t-1)| + q_(t-1) |theta_t| = |q_t p_(t-1) - q_(t-1)
      p_t| = 1, the n alpha are dense, so the q_t arcs tile the circle
      and their q_t endpoints are exactly the CUTS -alpha, ...,
      -q_t alpha. The completion, the odometer, maps onto the circle,
      two-to-one exactly over the cuts -j alpha (j >= 1), whose two
      codings part at the digit below the first depth with q_t >=
      max(j, 2).
  (2) THE TWO CODINGS OF -alpha. q_K - 1 = a_K q_(K-1) + (q_(K-2) -
      1) is greedy and legal, so q_K - 1 is the cap-filling on one
      parity: (0, a_2, 0, a_4, ...) at even K, (a_1 - 1, 0, a_3, 0,
      ...) at odd K. Their stars are -alpha and 1 - alpha, one circle
      point, and they part at the lowest position a nonzero digit may
      take: position 0 when a_1 >= 2, position 1 when a_1 = 1. So
      n -> n - 1 at the inputs q_K, which converge to 0 in the
      odometer, has images alternating between the two codings.
  (3) THE CONTAINMENT CRITERION. Let f(n) = m n + omega (m >= 1) on the
      integers where it is >= 0, so that f(n) alpha = g(n alpha) mod
      1 with g(x) = m x + omega alpha, continuous and locally injective.
      Let t be a depth with q_t >= 2. Then f reads at lookahead c at
      depth t iff every g-preimage of every cut -j alpha, j <= q_t,
      is a cut -i alpha with 1 <= i <= q_(t+c). If no preimage lies
      inside an input arc I, g(I minus its endpoints) is connected and
      misses every cut, so it lies in one output arc; if a preimage y
      lies inside I, g carries the integers on the two sides of y
      (dense) to the two sides of a cut, which are different arcs
      when q_t >= 2. This is the wall criterion f^-1(B) minus B with
      B the cut set, on a connected circle.
  (4) THE AFFINE MAPS. The preimages of -j alpha under g are (h - (j
      + omega) alpha)/m, h = 0..m-1, and such a point equals -i alpha mod
      1 only if (m i - j - omega) alpha is an integer congruent to -h mod
      m, which for irrational alpha needs m i = j + omega and h = 0. So:
      n + omega (m = 1, omega >= 0) reads, with c_min(t) = min{c :
      q_(t+c) >= q_t + omega} wherever q_t >= 2, and 0 while q_t = 1;
      n + omega (omega <= -1) has the preimage -(omega + 1) alpha of
      -alpha, never a cut; m n + omega (m >= 2) has the preimages
      h = 1..m-1, never cuts. Both read
      at no lookahead from the first depth t_0 with q_t >= 2, which
      is t_0 = 1 when a_1 >= 2 and 2 when a_1 = 1.
  (5) RESIDUE FREEDOM AND THE FLOORS. The rotation by (1, alpha) on
      Z/m x R/mZ is minimal: its orbit closure is a closed subgroup
      holding m (1, alpha) = (0, m alpha), which generates a dense
      subgroup of R/mZ since alpha is irrational, and then (1, alpha)
      gives the rest. So the integers of any tile (an arc) realize
      every pair (n mod m, floor(n alpha) mod m): a tile fixes n alpha
      mod 1 and nothing of n mod m. For u = floor(n/m), n = m u + s,
      u alpha = (n alpha - s alpha)/m, so the images of one input
      arc near a non-cut x accumulate at m points (x - s alpha + P)/m,
      P = 0..m-1, spaced 1/m. Rotating x, one of them crosses a cut
      while the others (cut differences being irrational) sit
      strictly inside arcs, so at some non-cut x two of the m points
      lie in different depth-t_0 arcs, and every input tile about x
      holds integers of both. floor(n/m) is DISCONTINUOUS from t_0 at
      every irrational alpha: never MIDDLE. On a divisor chain the
      tiles are residue classes and fix n mod m once m divides the
      modulus; here they never do.

PREDICTIONS (frozen before the engine ran).
  P1 THE CUTS. At every alpha below and every depth t with q_t <=
     20000, the q_t prefix arcs have endpoints -j alpha, 1 <= j <=
     q_t, each j exactly twice (once per side), total length exactly
     1 as a rational identity, and when sorted around the circle each
     arc's end is the next arc's start; every n < N lies strictly
     inside the arc of its own prefix. No exception anywhere.
  P2 THE CODINGS. The greedy string of q_K - 1 equals the parity's
     cap-filling at every K = 1..60 at every alpha; the two parities'
     strings first differ at position t_0 - 1; their stars (exact
     rationals over a certified approximation) sum to -alpha and
     1 - alpha to within 10^-20.
  P3 THE SUCCESSORS. For n + omega, omega = 0..5, the brute lookahead
     over n < N equals min{c : q_(t+c) >= q_t + omega} (0 while q_t = 1) at
     every depth t with q_(t+c+1) <= N, every alpha. Kill: one
     mismatch.
  P4 THE TEARS. For n + omega (omega = -1, -2), m n + omega (m = 2..4,
     omega = 0, 1) and floor(n/m) (m = 2..4), the brute lookahead at
     t_0 over n < N is at least c_N - 2 at N = 10^4 and 10^5, c_N being the largest
     c with q_(t_0+c) <= N (a deeper input tile holds one integer
     below N and reads vacuously). Kill: a map reading at t_0 with c
     <= c_N - 3 at either N. At depths t < t_0 every map reads at 0.
  P5 RESIDUE FREEDOM. Every depth-s tile holding at least 40 m^2
     integers below N = 10^5 realizes all m^2 pairs (n mod m,
     floor(n alpha) mod m), m = 2..5. Kill: one missing pair.
  P6 CONTROLS, run before any verdict: the identity reads at 0
     everywhere; at the golden alpha the successor reads at 1 from
     depth 2 (the Zeckendorf control); a planted non-map (f
     = n XOR 1 on the binary digits, no continuous circle map) is flagged torn
     by the brute at some depth; the certified quotients of cbrt(2)
     - 1 agree between the lower and upper bounds for 40 terms.
  [SETTLED ON A LATER READ, the slate above left as frozen. P4's
  reading below t_0 and P6's identity control hold by construction (one
  tile; the input and output keys one array at c = 0) and are not
  checks. P5 reads the tiles at each depth whose mean tile holds 40 m^2
  integers. Each control reads before its own detector's verdicts, not
  before every verdict, and a planted floor, n in place of
  floor(n alpha), now controls P5's census.]

THE ALPHAS. golden [1], silver [2], bronze [3] and sqrt(3) - 1 [1, 2]
(periodic); e - 2 = [0; 1, 2, 1, 1, 4, 1, 1, 6, ...] and cbrt(2) - 1
(non-periodic, the second certified from integer bounds); and a
seeded random alpha with quotients in 1..4. Exact rationals
throughout: alpha is replaced by a convergent p_M/q_M with q_M above
10^60; the least arc is asserted to clear the approximation error by
10^20, and every other comparison clears it by more, unasserted.

FINDINGS (entered after the run, from its prints; `--full`).
  F1 THE CUTS (theorem, argument (1); P1 lands). 185,523 tiles over
     the seven alphas (golden depths 0..21, 46,367 tiles; cbrt(2) - 1
     depths 0..10, 10,238): structure faults 0, every n < 20000
     strictly inside its own prefix's arc, the least arc 4.09e-05.
  F2 THE CODINGS (theorem, argument (2)). The closed form is off at 0
     of 60 K at every alpha, and the parities part at position
     t_0 - 1 at every one (1 at golden, sqrt(3) - 1 and e - 2; 0 at
     the rest). The star is EXACTLY -alpha + theta_K at even K and
     1 - alpha + theta_K at odd K, at all 60 K of all seven alphas.
     P2's frozen tolerance MISSED at golden and sqrt(3) - 1: the
     truncation is |theta_K|, about 1/q_(K+1), near 10^-13 at golden
     K = 60, and the slate's 10^-20 was a wrong estimate of it; the
     exact identity replaced the tolerance, which it implies.
  F3 THE SUCCESSORS (theorem, argument (4); P3 lands). Off the
     formula at 0 depths at every alpha. n + 1 reads 0, 0, then 1 at
     every depth at golden; n + 5 reads 0, 0, 3, 2, 2, then 1 at
     golden and 0, 0, 3, 2, then 1 at e - 2, the early bumps where
     q_(t+1) - q_t < 5.
  F4 THE TEARS (P4 lands, the kill missing everywhere). At both N,
     every tear map's least lookahead at t_0 is c_N - 1, c_N or c_N
     + 1: at golden 17 or 18 at c_N 17 and 22 or 23 at c_N 22, the
     one c_N - 1 being 4n at cbrt(2) - 1, N = 10^4 (8 at c_N 9); the
     floors n // 2, n // 3 and n // 4 read exactly at c_N + 1 at both N
     and all seven alphas (asserted). A
     tear map reads only near c_N, where its input tiles hold a few
     integers below N.
  F5 RESIDUE FREEDOM (P5 lands). 11,169 (tile, m) tests over
     m = 2..5 and the seven alphas, none missing a pair.
  F6 CONTROLS (all green). 300 quotients of cbrt(2) - 1 certified;
     n XOR 1 flagged torn at golden depths 2..6; the planted floor
     misses a pair in all 3 golden depth-3 tiles; the golden successor
     at 1 from depth 2, ahead of P3's verdicts.

RUN RECORD. After the slate froze, P4 gained the assert that the
floors read exactly at c_N + 1; its section rerun `--full` held at all
seven alphas. Later the identity control and the reading below t_0,
which held by construction, were cut, the residue census gained its
planted control, and the in-arc check of P1 reached every depth to
t_max. `--full`: 39/39, 20.0 s, peak 73 MB under a 512 MB watch; the
default (P1 to 5000, P4 at N = 10^4 only, P5 to 3 * 10^4): 39/39,
5.0 s, 33 MB. The first full run held all seven alphas' prefix tables at
once (peak 430 MB) and failed P2's tolerance at two alphas; the
tables are now built per alpha and the tolerance is the exact
identity of F2.
"""

import random
import sys
import time
from array import array
from fractions import Fraction

CHECKS = []
FULL = "--full" in sys.argv    # the record run; the default runs small


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tag = "ok  " if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f" -- {detail}" if detail else ""))


# ------------------------------------------------------------- alphas

def cf_of_fraction(x, limit):
    out = []
    while len(out) < limit and x.denominator != 1:
        a = x.numerator // x.denominator
        out.append(a)
        x = 1 / (x - a)
    return out


def icbrt(n):
    x = 1 << ((n.bit_length() + 2) // 3 + 1)
    while True:
        y = (2 * x + n // (x * x)) // 3
        if y >= x:
            return x
        x = y


def cbrt2_quotients(digits=320):
    """The quotients of cbrt(2) - 1 shared by a lower and an upper
    bound 10^-digits apart, the last shared one dropped."""
    s = 10 ** digits
    r = icbrt(2 * s ** 3)
    assert r ** 3 <= 2 * s ** 3 < (r + 1) ** 3
    lo = cf_of_fraction(Fraction(r, s) - 1, 400)
    hi = cf_of_fraction(Fraction(r + 1, s) - 1, 400)
    common = []
    for a, b in zip(lo, hi):
        if a != b:
            break
        common.append(a)
    return common[1:-1]


def e_minus_2(n):
    out, k = [1, 2], 1
    while len(out) < n:
        out += [1, 1, 2 * (k + 1)]
        k += 1
    return out[:n]


def alphas():
    rnd = random.Random(7)
    return [
        ("golden [1]", [1] * 320),
        ("silver [2]", [2] * 200),
        ("bronze [3]", [3] * 160),
        ("sqrt(3) - 1 [1, 2]", [1, 2] * 120),
        ("e - 2", e_minus_2(200)),
        ("cbrt(2) - 1", cbrt2_quotients()),
        ("random 1..4 (seed 7)", [rnd.randint(1, 4) for _ in range(200)]),
    ]


class Numeration:
    """alpha = [0; a_1, a_2, ...], replaced for arithmetic by its last
    convergent P/Q; a real is a pair (A, B) meaning A + B alpha."""

    def __init__(self, name, quots):
        self.name, self.a = name, [None] + list(quots)
        q, p = [0, 1], [1, 0]
        for a in quots:
            q.append(a * q[-1] + q[-2])
            p.append(a * p[-1] + p[-2])
        self.qq, self.pp = q[1:], p[1:]
        self.Q, self.P = q[-1], p[-1]
        assert self.Q > 10 ** 60, name
        self.t0 = 1 if quots[0] >= 2 else 2

    def q(self, k):
        return 0 if k == -1 else self.qq[k]

    def p(self, k):
        return 1 if k == -1 else self.pp[k]

    def theta(self, k):
        return (-self.p(k), self.q(k))

    def value(self, x):
        return Fraction(x[0] * self.Q + x[1] * self.P, self.Q)

    def sign(self, x):
        v = x[0] * self.Q + x[1] * self.P
        return (v > 0) - (v < 0)

    def digits(self, n):
        k = 0
        while self.q(k + 1) <= n:
            k += 1
        d = [0] * (k + 1)
        while n:
            while self.q(k) > n:
                k -= 1
            d[k], n = divmod(n, self.q(k))
        return d

    def legal(self, d):
        if d and d[0] > self.a[1] - 1:
            return False
        for k in range(1, len(d)):
            if d[k] > self.a[k + 1]:
                return False
            if d[k] == self.a[k + 1] and d[k - 1] != 0:
                return False
        return True

    def star(self, d):
        return (sum(-dk * self.p(k) for k, dk in enumerate(d)),
                sum(dk * self.q(k) for k, dk in enumerate(d)))

    def depth_of(self, N):
        """The largest t with q_t <= N."""
        t = 0
        while self.q(t + 1) <= N:
            t += 1
        return t

    def keys(self, M):
        """key[s][n], the value of n's depth-s prefix for n < M: the
        greedy remainder chain n mod q_T mod q_(T-1) ... mod q_s."""
        top = self.depth_of(M) + 1
        cur = array("i", range(M))
        out = [None] * (top + 1)
        for s in range(top, -1, -1):
            qs = self.q(s)
            cur = array("i", (v % qs for v in cur))
            out[s] = cur
        return out


# ------------------------------------------------------------- P1

def tile_ends(w, t, r, sr):
    """The endpoints (A, B) of the depth-t tile of prefix r (star sr),
    with the cut indices j they sit at."""
    tt, tu = w.theta(t), w.theta(t - 1)
    e1 = (sr[0] - tt[0], sr[1] - tt[1])
    j1 = w.q(t) - r
    if t >= 1 and r < w.q(t - 1):
        e2 = (sr[0] - tu[0], sr[1] - tu[1])
        j2 = w.q(t - 1) - r
    else:
        e2 = (sr[0] - tu[0] - tt[0], sr[1] - tu[1] - tt[1])
        j2 = w.q(t - 1) + w.q(t) - r
    return e1, e2, j1, j2


def section_cuts(ws, qmax=20000, nmax=20000):
    print("\nP1 THE CUTS: the depth-t tiles are the arcs cut at -j alpha")
    for w in ws:
        tmax = w.depth_of(qmax)
        bad, least, tiles = 0, Fraction(1), 0
        for t in range(tmax + 1):
            qt, arcs, js = w.q(t), [], {}
            for r in range(qt):
                d = w.digits(r) if r else []
                e1, e2, j1, j2 = tile_ends(w, t, r, w.star(d))
                for e, j in ((e1, j1), (e2, j2)):
                    if not 1 <= j <= qt or \
                            (w.value(e) + j * Fraction(w.P, w.Q)) % 1:
                        bad += 1
                    js[j] = js.get(j, 0) + 1
                lo, hi = (e1, e2) if w.sign((e2[0] - e1[0],
                                             e2[1] - e1[1])) > 0 else (e2, e1)
                ln = w.value(hi) - w.value(lo)
                arcs.append((w.value(lo) % 1, ln))
            tiles += qt
            if sorted(js) != list(range(1, qt + 1)) or \
                    any(v != 2 for v in js.values()):
                bad += 1
            if sum(ln for _, ln in arcs) != 1:
                bad += 1
            arcs.sort()
            for i, (st, ln) in enumerate(arcs):
                if (st + ln) % 1 != arcs[(i + 1) % len(arcs)][0]:
                    bad += 1
                least = min(least, ln)
        outside = 0
        for n in range(nmax):
            d = w.digits(n)
            sn = w.star(d)
            d += [0] * (tmax - len(d))
            r, sr = 0, (0, 0)
            for t in range(tmax + 1):
                if t:
                    k = t - 1
                    r += d[k] * w.q(k)
                    sr = (sr[0] - d[k] * w.p(k), sr[1] + d[k] * w.q(k))
                e1, e2, _, _ = tile_ends(w, t, r, sr)
                s1 = w.sign((sn[0] - e1[0], sn[1] - e1[1]))
                s2 = w.sign((sn[0] - e2[0], sn[1] - e2[1]))
                if s1 * s2 != -1:
                    outside += 1
        clear = least > Fraction(10 ** 20 * qmax, w.Q ** 2)
        print(f"  {w.name:21s} depths 0..{tmax:2d}, {tiles:5d} tiles: "
              f"structure faults {bad}, n outside its tile {outside}, "
              f"least arc {float(least):.3g}")
        check(f"{w.name}: the tiles are the arcs cut at -alpha .. "
              f"-q_t alpha", bad == 0 and outside == 0 and clear)


# ------------------------------------------------------------- P2

def section_codings(ws):
    print("\nP2 THE TWO CODINGS OF -alpha: q_K - 1 by the parity of K")
    for w in ws:
        bad = 0
        for K in range(1, 61):
            d = w.digits(w.q(K) - 1)
            d += [0] * (K - len(d))
            want = [0] * K
            for pos in range(K - 1, -1, -2):
                want[pos] = w.a[pos + 1] if pos else w.a[1] - 1
            if d != want or not w.legal(d):
                bad += 1
        stars_off = 0
        for K in range(1, 61):
            base = (1, -1) if K % 2 else (0, -1)
            th = w.theta(K)
            if w.star(w.digits(w.q(K) - 1)) != (base[0] + th[0],
                                                 base[1] + th[1]):
                stars_off += 1
        de, do = w.digits(w.q(60) - 1), w.digits(w.q(59) - 1)
        L = max(len(de), len(do))
        de, do = de + [0] * (L - len(de)), do + [0] * (L - len(do))
        part = next(i for i in range(L) if de[i] != do[i])
        ok = stars_off == 0
        print(f"  {w.name:21s} closed form off at {bad} of 60 K; parts "
              f"at position {part} (t_0 - 1 = {w.t0 - 1}); star off "
              f"-alpha + theta_K (K even), 1 - alpha + theta_K (K odd) "
              f"at {stars_off} of 60 K")
        check(f"{w.name}: q_K - 1 is the cap-filling, parting at t_0 - 1",
              bad == 0 and part == w.t0 - 1 and ok)


# ------------------------------------------------------------- brute

def reads(key, out, lo, N, t, c):
    """True iff every n in [lo, N) sharing a depth-(t + c) prefix has
    one depth-t prefix of out[n]."""
    kin, kout, seen = key[t + c], key[t], {}
    for n in range(lo, N):
        b = kout[out[n]]
        if seen.setdefault(kin[n], b) != b:
            return False
    return True


def least_c(key, out, lo, N, t, cmax):
    for c in range(cmax + 1):
        if reads(key, out, lo, N, t, c):
            return c
    return None


def succ_formula(w, t, om):
    if w.q(t) == 1:
        return 0
    c = 0
    while w.q(t + c) < w.q(t) + om:
        c += 1
    return c


def section_successors(ws, key_of, N=20000, head=True):
    if head:
        print("\nP3 THE SUCCESSORS n + omega: brute c_min against min{c : "
              "q_(t+c) >= q_t + omega}")
    for w in ws:
        key, off, cols = key_of[w.name], 0, []
        for om in range(6):
            out = [n + om for n in range(N)]
            col, t = [], 0
            while True:
                f = succ_formula(w, t, om)
                if w.q(t + f + 1) > N:
                    break
                b = least_c(key, out, 0, N, t, f + 2)
                col.append(b)
                off += b != f
                t += 1
            cols.append(col)
        print(f"  {w.name:21s} omega = 1: {cols[1]}; omega = 5: {cols[5]}; "
              f"off the formula {off}")
        if w.name.startswith("golden"):
            check("control: the golden successor reads at 1 from depth 2",
                  cols[1][0:2] == [0, 0] and set(cols[1][2:]) == {1})
        check(f"{w.name}: n + omega reads exactly at the formula", off == 0)


def tear_maps():
    return ([("n - %d" % om, om, lambda n, om=om: n - om) for om in (1, 2)]
            + [("%dn + %d" % (m, om), 0, lambda n, m=m, om=om: m * n + om)
               for m in (2, 3, 4) for om in (0, 1)]
            + [("n // %d" % m, 0, lambda n, m=m: n // m) for m in (2, 3, 4)])


def section_tears(ws, key_of, head=True):
    if head:
        print("\nP4 THE TEARS: brute reading at t_0 against c_N")
    for w in ws:
        key, t0, worst = key_of[w.name], w.t0, None
        for N in ((10 ** 4, 10 ** 5) if FULL else (10 ** 4,)):
            cap = w.depth_of(N) - t0
            rows = []
            for name, lo, f in tear_maps():
                out = [0] * lo + [f(n) for n in range(lo, N)]
                early = reads(key, out, lo, N, t0, cap - 3)
                c = least_c(key, out, lo, N, t0, cap + 1) if not early \
                    else None
                rows.append((name, c, early))
            bad = [r for r in rows if r[2]]
            bad += [r for r in rows if r[0].startswith("n //")
                    and r[1] != cap + 1]
            got = [r[1] for r in rows]
            print(f"  {w.name:21s} N = {N:6d} c_N {cap:2d}: least c at t_0 "
                  f"{got} (None: read at c <= c_N - 3)")
            worst = (worst or 0) + len(bad)
        check(f"{w.name}: every tear map reads at no c <= c_N - 3; "
              f"the floors n // 2, 3, 4 at c_N + 1",
              worst == 0)


def pair_census(ks, fl, m, N):
    """(tested, missing): the tiles of key ks holding at least 40 m^2
    integers below N, and how many miss a pair (n mod m, fl[n] mod m)."""
    pairs, count = {}, {}
    for n in range(N):
        k = ks[n]
        count[k] = count.get(k, 0) + 1
        pairs.setdefault(k, set()).add((n % m, fl[n] % m))
    full = [k for k, cnt in count.items() if cnt >= 40 * m * m]
    return len(full), sum(len(pairs[k]) != m * m for k in full)


def section_residues(ws, key_of, head=True):
    N = 10 ** 5 if FULL else 3 * 10 ** 4
    if head:
        print("\nP5 RESIDUE FREEDOM: every pair (n mod m, floor(n alpha) "
              "mod m) in every populous tile")
    for w in ws:
        key = key_of[w.name]
        fl = [n * w.P // w.Q for n in range(N)]
        tested, missing = 0, 0
        for m in (2, 3, 4, 5):
            for s in range(w.depth_of(N) + 1):
                if N // w.q(s) < 40 * m * m:
                    break
                ts, ms = pair_census(key[s], fl, m, N)
                tested, missing = tested + ts, missing + ms
        print(f"  {w.name:21s} tiles tested {tested}, missing a pair "
              f"{missing}")
        check(f"{w.name}: every populous tile realizes every residue pair",
              tested > 0 and missing == 0)


def section_controls(ws, key_of, N=20000):
    print("\nP6 CONTROLS")
    cb = [w for w in ws if w.name.startswith("cbrt")][0]
    check("cbrt(2) - 1 quotients certified for 40 terms",
          len(cb.a) - 1 >= 40, f"{len(cb.a) - 1} certified")
    gold = [w for w in ws if w.name.startswith("golden")][0]
    key = key_of[gold.name]
    out = [n ^ 1 for n in range(N)]
    torn = [t for t in range(1, 7)
            if not reads(key, out, 0, N, t, gold.depth_of(N) - t - 3)]
    check("planted non-map n XOR 1 is flagged torn by the brute",
          bool(torn), f"torn at depths {torn}")
    ts, ms = pair_census(key[3], list(range(N)), 2, N)
    check("planted floor n in place of floor(n alpha) misses pairs in the "
          "residue census", ts > 0 and ms == ts, f"{ms} of {ts} tiles")


def main():
    t_start = time.time()
    ws = [Numeration(n, qs) for n, qs in alphas()]
    M = 4 * (10 ** 5 if FULL else 3 * 10 ** 4) + 2
    gold = ws[0]
    section_controls(ws, {gold.name: gold.keys(M)})
    section_cuts(ws, *((20000, 20000) if FULL else (5000, 5000)))
    section_codings(ws)
    for section in (section_successors, section_tears, section_residues):
        for w in ws:
            section([w], {w.name: w.keys(M)}, head=(w is gold))
    print(f"\n{sum(CHECKS)}/{len(CHECKS)} checks passed, "
          f"{time.time() - t_start:.1f} s")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
