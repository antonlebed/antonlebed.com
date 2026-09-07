"""explore_jump_digits.py — THE WHOLE JUMP SET FROM THE DIGITS: how many
digits of w fix the jump set of a window, and is the reading the greedy
dlog of zeta_p in the ring the digits define?

THE QUESTION. Here w = -p/pi^e (2/pi^e at p = 2), the window's unit. The jump set (I, beta) of a totally ramified f = 1 window
K/Q_p with integral seat i* = c_0 p^M is the Pareto frontier of the
relation vector p dlog(zeta_p) under (order, weight after powering)
(Pagano, arXiv:1810.09975, Theorem 1.4; explore_jump_set.py). Its first
point is (c_0, M + 1) at weight e* = p i* (explore_rung_odd.py), its
second is read off the digits of w by the module and the equation at
the seat (explore_second_point.py): the second frontier weight is
e* + min(delta_w, p^M) up to the truncation, and the readout theorem's
rung reads 3e/2 - 1 digits of w. This rig asks for the WHOLE frontier:
is the jump set a function of finitely many digits of w, how many, and
is the reading the greedy discrete log of zeta_p carried out in the
ring the digits alone define?

THE OBJECTS. The digits of w are its canonical expansion w = sum w_r
pi^r with w_r in {0, ..., p - 1}, w_0 = 1 at the open gate. THE DIGIT
RING: the digit strings of length N with the carry rule p = sigma w
pi^e, sigma = -1 at odd p and +1 at p = 2 (the sign of w's definition),
so a coefficient q p at level r becomes sigma q w at level r + e; it is
O_K / pi^N for the window whose Eisenstein polynomial is the
distinguished factor of p - sigma pi^e w(pi), and it reads only the
digits w_j with j < N - e. The greedy dlog, the pullback along
rho(i) = min(p i, i + e), the basis 1 + pi^a for a in T* = {a < e* :
p not dividing a} u {e*} and the frontier are explore_rung_odd.py's,
run in the digit ring. A HIT is a level at which the greedy dlog of
zeta_p divides out a basis monomial; the hit at level L with pullback
(a, b) is the point (a, b + 1) at weight rho(L).

THE HAND DERIVATION (on paper, before the engine).

H1  THE DOMINANCE BOUND. A hit L > i* gives a point at weight rho(L)
    > e*, dominated by the first point iff its order b(L) + 1 >= M + 1.
    L in [e* + ke, e* + (k+1)e) pulls back with b >= k + 1 except
    L = e* + ke itself, where b = k. So every hit at or above
    CAP := e* + (M - 1)e + 1 is dominated, and the frontier is a
    function of the hits below CAP.
H2  THE UPWARD LEMMA. A carry at level r lands at r + e carrying w's
    digits; a binomial coefficient enters as a power of p, upward; a
    product's level-X digit reads its factors' levels <= X; zeta_p's
    level-X digit reads w_r for r <= X - i* (zeta_2 = 1 - w pi^e
    exactly; at odd p the equation (1 + t)^(p-1) = w(1 + ...) reads
    t at level s off w_s). So every hit below CAP reads w_r with
    r <= CAP - 1 - i* = e + (M - 1)e = M e.
H3  THE PRECISION THEOREM (candidate). The jump set is a function of
    the digits w_1, ..., w_(Me), M = v_p(i*), at every p. At M = 0 no
    digit is read and the frontier is {(i*, 1)} alone.
H4  SHARPNESS. The anchor K = Q_p(zeta_(p^(M+1))) (e = p^M (p - 1),
    c_0 = 1) has zeta_p = (1 + pi)^(p^M) exactly, hit set {i*} and
    I = {c_0}; at c_0 > 1 the tame twist pi^(c_0) = zeta_(p^(M+1)) - 1
    is the anchor (p = 2, c_0 = 3, M = 2: x^12 + 4x^9 + 6x^6 + 4x^3 + 2,
    the octic Phi_8(x^3 + 1)). A digit string agreeing with an anchor's
    to M e - 1 and differing at M e hits e* + (M - 1)e exactly (the
    lower digits agree, so the lower carries agree, and the level
    CAP - 1 digit flips), the point (e*, M) at weight e* + M e,
    undominated: I gains e*. So M e - 1 digits do not suffice.
H5  e = 2 BY HAND. -1 = 1 - w pi^2, B = (1 + pi)^2 = 1 + pi^2 + w pi^3;
    -1 - B at level 3 reads -w_1 - 1, a hit iff w_1 = 0 (the point
    (3, 1), tau = 1); at level 4 it reads -w_2 - 2, a hit iff w_2 = 1
    (the point (4, 1), tau = 2); otherwise I = {1}. Masses 1/2, 1/4,
    1/4 on the four digit cells, Pagano's.
H6  THE TWO PRECISIONS. The rung reads 3e/2 - 1 digits, the whole
    frontier M e = e log_2 e at p = 2: 5 against 8 at e = 4, 11
    against 24 at e = 8. The gap is the frontier's points past the
    second, which no minimum reads.

PREDICTIONS, fixed before the engine ran.
  PR1 (the ring is the field). At every field read — the tame
      readout's twenty at p = 3, 5, x^12 - 2, the six ramified
      quadratics, 512 Haar-random octics (seed 1179) and the anchors —
      the digit ring, fed the engine's digits of w, returns the
      engine's frontier. KILL: one field off.
  PR2 (M e digits suffice). At every field, replacing every digit of
      w past position M e by random digits (three tails) leaves the
      frontier unchanged. KILL: one field or tail off.
  PR3 (M e is sharp). At each anchor — zeta_4, zeta_8, zeta_16 at
      p = 2; zeta_9 at p = 3; zeta_25 at p = 5; the c_0 = 3 octic — the
      engine frontier is {(c_0, M + 1)}, and the digit string agreeing
      with the anchor's to M e - 1 with digit M e changed reads
      {(c_0, M + 1), (e*, M)} with the second weight e* + M e. KILL:
      one anchor off.
  PR4 (the digit censuses). Over all 2^(Me) digit strings the frontier
      counts are 2, 1, 1 at e = 2 and 128, 32, 32, 16, 16, 16, 8, 4, 2,
      2 at e = 4 — the Haar masses times the cell count, the digit
      cells carrying the mass law. KILL: one count off; a miss is a
      finding about the two measures, not about H3.
  PR5 (the two precisions at e = 4). Over the 256 cells the rung
      (second weight capped at 7e/2 = 14) is a function of w_1..w_5,
      and at least one pair of cells differing only in w_8 has
      different frontiers. KILL: a pair agreeing on w_1..w_5 with
      different rungs, or no pair split at w_8.
  PR6 (the e = 8 digit population). 2048 uniform digit strings at
      precision 24 with random tails sit within the mass law's band:
      worst |z| < 3.5 over the classes with expected count >= 8, no
      frontier outside the admissible set. KILL: a frontier off the
      law or |z| >= 3.5.
  PR7 (controls, read first). x^2 - 2: digits w = (1, 0, ...), hits
      {2, 3, 4} (the level-4 hit dominated), frontier ((1, 2), (3, 1)). x^6 + 3x + 3: frontier
      ((1, 2), (4, 1)), hit at level 4. zeta_8: hit set {4}, frontier
      ((1, 3),). The digit ring's -1 at p = 2 squares to 1.

THE DESIGN. engine: explore_rung_odd.py's field, window, zeta_p, dlog
and frontier for the engine side; a digit reader for w with the
digits 0..p-1 (the Teichmueller digits of explore_tame_readout.py
differ at p = 5 and the ring is the same); the digit ring with add,
mul, inverse by digit correction, pow, and the H6 root-of-unity loop
of explore_rung_odd.py for zeta_p at odd p (-1 = 1 - w pi^e at p = 2);
its precision CAP + e + 2, so zeta_p is exact below CAP. The mass law
is explore_jump_haar.py's. verdict: PR1-PR7 as counts.
Run: python prime/code/explore_jump_digits.py

FINDINGS (entered post-run, copied from printed output).

1. THE RING IS THE FIELD, AND M e DIGITS SUFFICE (PR1, PR2 hit, 0 off
   at 534 open-gate fields: fifteen of the tame readout's twenty,
   x^12 - 2, the six ramified quadratics, 512 Haar octics carrying 19
   jump sets, and the six anchors; three random tails past M e at
   each). Hit sets below CAP: x^6+3x+3 [3, 4, 7, 8] I=[1, 4]
   beta=[2, 1]; x^18+3 [9, 18, 21, 25, 30, 32, 33, 36, 37, 39, 42]
   I=[1, 7, 25] beta=[3, 2, 1]; x^12-2 (c_0 = 3, M e = 24, CAP 37)
   [12, 18, 21, 24, 27, 36] I=[3, 9, 21] beta=[3, 2, 1]; x^2-2
   [2, 3, 4], the level-4 hit dominated; x^2+2x+2, zeta9 and zeta25
   hit their seat alone.

2. M e IS SHARP (PR3 hit at the six anchors): zeta4 (M e = 2) reads
   I=[1, 4] at weight 6 once digit 2 is changed; zeta8 (8) I=[1, 8] at
   16; zeta16 (24) I=[1, 16] at 40; Phi8(x^3+1) (c_0 = 3, M e = 24)
   I=[3, 24] at 48; zeta9 (6) I=[1, 9] at 15; zeta25 (20) I=[1, 25]
   at 45 — each beta(e*) = M, each hit set [i*, e* + (M - 1)e].

3. THE DIGIT CELLS CARRY THE MASS LAW (PR4 hit; PR6 hit): the 4
   digit strings at e = 2 fall 2, 1, 1 on [1, 3], [1], [1, 4]; the
   256 at e = 4 fall 128, 32, 32, 16, 16, 16, 8, 4, 2, 2 on the ten
   jump sets, every count the law's ([1, 5] beta (3, 1) at 128 down
   to [1, 8] beta (3, 2) and [1] at 2). At e = 8, 2048 uniform strings
   at precision 24 carry 31 jump sets, worst |z| 1.51 over the classes
   with expected count >= 8, chi-square 24.6 on 19 df, deviate +0.93:
   [1, 9] 1041 (law 1024), [1, 5, 11] 243 (256), [1, 11] 243 (256),
   [1, 5, 13] 142 (128), [1, 5, 15] 71 (64), [1, 3, 13] 61 (64).

4. THE TWO PRECISIONS (PR5 hit): over the 256 cells at e = 4 the rung
   is a function of w_1..w_5 (six rung values) while the frontier is
   not a function of w_1..w_7: 2 of the 128 precision-7 cells split at
   w_8 — 0100101, where w_8 = 1 adds the hit at 12 and I=[1, 8]
   beta=[3, 2] to hits [4, 10]; and 0100110, where w_8 = 1 is the
   anchor zeta8 with hit set [4] and w_8 = 0 hits [4, 12] — and 2 of
   the 64 precision-6 cells split below.

TIER. THE DIGIT PRECISION OF THE JUMP SET — the jump set a function of
w_1, ..., w_(Me), M = v_p(i*), and of no fewer, read by the greedy dlog
of zeta_p in the ring the digits define — is a THEOREM for every
totally ramified f = 1 window with integral seat at every p, given
Pagano's Theorem 1.4 (H1-H4); its instances are rules at the 534
fields read. The digit cells at precision M e carrying the mass law's
frequencies is a RULE,
exhaustive at e = 2 and e = 4, and an observation at e = 8 over 2048
draws.

RUN RECORD. python prime/code/memwatch.py prime/code/explore_jump_digits.py:
36.3 s wall, peak working set 18.5 MB, 140,690 checks. PR7's x^2 - 2
control was written {2, 3} by hand and the rig printed [2, 3, 4], the
level-4 hit real and dominated by the level-3 point, so the frontier
read as predicted; the expected list was corrected before the anchors
ran, no other prediction touched. Two pre-green faults: a missing
import, and the census print's cell total written 2^M e for M e (the
census itself counted 4 and 256).
"""
import os
import random
import sys
import time
from math import comb

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, ".")
sys.path.insert(0, "prime/code")
import explore_arrival_defect as ad       # noqa: E402
import explore_jump_set as js             # noqa: E402
import explore_jump_haar as jh            # noqa: E402
import explore_rung_odd as ro             # noqa: E402
import explore_rung_theorem as rt         # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ------------------------------------------------------------ the digit ring

class DigitRing:
    """Digit strings of length N under p = sigma w pi^e."""

    def __init__(self, p, e, wdig, N):
        self.p, self.e, self.N = p, e, N
        self.sigma = 1 if p == 2 else -1
        need = N - e
        ok(len(wdig) >= need, "digit ring at N=%d needs %d digits of w, %d given"
           % (N, need, len(wdig)))
        ok(wdig[0] == 1, "w_0 != 1")
        self.w = list(wdig[:need])
        self.one = self.norm([1] + [0] * (N - 1))

    def norm(self, c):
        c = list(c) + [0] * (self.N - len(c))
        p, e, N, w, s = self.p, self.e, self.N, self.w, self.sigma
        for r in range(N):
            q, d = divmod(c[r], p)
            c[r] = d
            if q:
                base = r + e
                if base < N:
                    sq = s * q
                    for j in range(N - base):
                        if w[j]:
                            c[base + j] += sq * w[j]
        return c[:N]

    def add(self, a, b):
        return self.norm([x + y for x, y in zip(a, b)])

    def sub(self, a, b):
        return self.norm([x - y for x, y in zip(a, b)])

    def mul(self, a, b):
        N = self.N
        c = [0] * N
        for i, x in enumerate(a):
            if x:
                for j in range(N - i):
                    y = b[j]
                    if y:
                        c[i + j] += x * y
        return self.norm(c)

    def val(self, a):
        for i, x in enumerate(a):
            if x:
                return i
        return self.N

    def mono(self, d, j):
        c = [0] * self.N
        c[0] = 1
        if j < self.N:
            c[j] += d
        return self.norm(c)

    def inv(self, u):
        """Inverse of a 1-unit by digit correction."""
        ok(u[0] == 1, "inverse of a non-unit")
        x = list(self.one)
        while True:
            r = self.sub(self.mul(u, x), self.one)
            L = self.val(r)
            if L >= self.N:
                return x
            d = (-r[L]) % self.p
            c = list(x)
            c[L] += d
            x = self.norm(c)

    def pow(self, u, n):
        r, b = self.one, u
        while n:
            if n & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            n >>= 1
        return r

    def zeta_p(self, istar):
        """zeta_p: -1 at p = 2; the H6 loop at odd p; None at the closed
        gate. Exact below N - e."""
        p, e, N = self.p, self.e, self.N
        if p == 2:
            return self.norm([-1] + [0] * (N - 1))
        estar = p * istar
        z = self.mono(1, istar)
        for _ in range(N + 2):
            g = self.sub(self.pow(z, p), self.one)
            L = self.val(g)
            if L >= N:
                return z
            if L <= estar:
                ok(L == estar, "z^p - 1 below e*")
                return None
            j = L - e
            for s in range(1, p):
                z2 = self.mul(z, self.mono(s, j))
                if self.val(self.sub(self.pow(z2, p), self.one)) > L:
                    z = z2
                    break
            else:
                ok(False, "no digit raises v(z^p - 1) at %d" % L)
        ok(False, "zeta_p loop did not converge")

    def dlog(self, u, istar, cap):
        """(orders {a: b_a + 1}, hit levels) of the greedy dlog of u,
        hits read below cap."""
        p, e = self.p, self.e
        estar = p * istar
        T = [a for a in range(1, estar) if a % p] + [estar]
        c = {a: 0 for a in T}
        hits = []
        cache = {}
        while True:
            i = self.val(self.sub(u, self.one))
            if i >= cap:
                break
            a, b = i, 0
            while not (a == estar or (a < estar and a % p)):
                a = a // p if a < estar else a - e
                b += 1
            ok(a in T, "pullback off T*")
            if (a, b) not in cache:
                inv = self.inv(self.pow(self.mono(1, a), p ** b))
                pw = [self.one]
                for _ in range(p - 1):
                    pw.append(self.mul(pw[-1], inv))
                cache[(a, b)] = pw
            for d in range(1, p):
                u2 = self.mul(u, cache[(a, b)][d])
                if self.val(self.sub(u2, self.one)) > i:
                    u = u2
                    c[a] += d * p ** b
                    hits.append(i)
                    break
            else:
                ok(False, "no digit raises weight %d" % i)
        ords = {a: ordp(p, v) + 1 for a, v in c.items() if v}
        return ords, hits


def ordp(p, n):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def frontier(p, e, ords):
    pts = list(ords.items())
    front = []
    for (a, b) in pts:
        wt = jh.rho_k(p, e, a, b)
        dom = any((b2 <= b and jh.rho_k(p, e, a2, b2) <= wt)
                  for (a2, b2) in pts if (a2, b2) != (a, b))
        if not dom:
            front.append((a, b))
    front.sort()
    return tuple(front)


def seat_split(p, istar):
    c0, M = istar, 0
    while c0 % p == 0:
        c0 //= p
        M += 1
    return c0, M


def digit_frontier(p, e, wdig):
    """(frontier, hits, CAP) from the digits of w alone; wdig must
    reach CAP + 2."""
    istar = e // (p - 1)
    c0, M = seat_split(p, istar)
    estar = p * istar
    cap = estar + (M - 1) * e + 1 if M >= 1 else estar
    N = cap + e + 2
    R = DigitRing(p, e, wdig, N)
    z = R.zeta_p(istar)
    if z is None:
        return None, [], cap
    ords, hits = R.dlog(z, istar, cap)
    return frontier(p, e, ords), hits, cap


# ------------------------------------------------------------ the engine side

def engine_digits(F, w, pi, n):
    """The digits 0..p-1 of the unit w, by division by pi:
    (A - d) pi^(e-1) w / (sigma p)."""
    p = F.p
    sigma = 1 if p == 2 else -1
    pik = F.one
    for _ in range(F.e - 1):
        pik = F.emul(pik, pi)
    A, out = w, []
    for _ in range(n):
        d = A[0][0] % p
        out.append(d)
        B = [list(c) for c in A]
        B[0][0] = (B[0][0] - d) % F.pM
        C = F.emul(F.emul(tuple(tuple(c) for c in B), pik), w)
        ok(all(c[0] % p == 0 for c in C), "%s: inexact digit division" % F.name)
        A = tuple((((sigma * (c[0] // p)) % F.pM),) for c in C)
    return out


def engine_read(name, p, eis):
    """(frontier, digits of w to CAP + 2, hits) from the module engine."""
    F = ro.field(name, p, eis)
    c0, M = ro.seat_split(F)
    istar, estar = F.seat, F.p * F.seat
    cap = estar + (M - 1) * F.e + 1 if M >= 1 else estar
    w, pi, delta, w0 = ro.window(F)
    z = ro.zeta_p(F)
    if z is None:
        return None, None, None, F
    ords = ro.orders(F, z, pi)
    front = ro.frontier(F, ords)
    dig = engine_digits(F, w, pi, cap + 3)
    return front, dig, cap, F


def fmt(front):
    return "I=%s beta=%s" % ([a for a, _ in front], [b for _, b in front])


def read(name, p, eis, rng, verbose=True):
    """PR1 and PR2 at one field; returns the engine frontier or None."""
    front, dig, cap, F = engine_read(name, p, eis)
    if front is None:
        if verbose:
            print("%-16s p=%d e=%d gate closed" % (name, p, F.e))
        return None
    e, istar = F.e, F.seat
    c0, M = seat_split(p, istar)
    Me = M * e
    df, hits, cap2 = digit_frontier(p, e, dig)
    ok(cap2 == cap, "%s: CAP mismatch" % name)
    ok(df == front, "%s: digit frontier %s, engine %s" % (name, df, front))
    for _ in range(3):
        tail = [dig[j] if j <= Me else rng.randrange(p) for j in range(len(dig))]
        df2, _h, _c = digit_frontier(p, e, tail)
        ok(df2 == front, "%s: a tail past %d digits moved the frontier to %s"
           % (name, Me, df2))
    if verbose:
        print("%-16s p=%d e=%d i*=%d M=%d  Me=%-3d CAP=%-3d hits<CAP %s  %s"
              % (name, p, e, istar, M, Me, cap, hits, fmt(front)))
    return front


# ------------------------------------------------------------ the anchors

def anchors():
    phi25 = [sum(comb(5 * j, k) for j in range(5)) for k in range(21)]
    return [
        ("zeta4", 2, [2, 2, 1]),
        ("zeta8", 2, [2, 4, 6, 4, 1]),
        ("zeta16", 2, [2, 8, 28, 56, 70, 56, 28, 8, 1]),
        ("Phi8(x^3+1)", 2, [2, 0, 0, 4, 0, 0, 6, 0, 0, 4, 0, 0, 1]),
        ("zeta9", 3, [3, 9, 18, 21, 15, 6, 1]),
        ("zeta25", 5, phi25),
    ]


def sharpness(rng):
    print("[PR3] the anchors: M e - 1 digits do not suffice")
    for name, p, eis in anchors():
        front, dig, cap, F = engine_read(name, p, eis)
        e, istar = F.e, F.seat
        c0, M = seat_split(p, istar)
        estar, Me = p * istar, M * e
        ok(front == ((c0, M + 1),), "%s: engine frontier %s" % (name, front))
        flipped = list(dig)
        flipped[Me] = (flipped[Me] + rng.randrange(1, p)) % p
        df, hits, _c = digit_frontier(p, e, flipped)
        want = tuple(sorted([(c0, M + 1), (estar, M)]))
        ok(df == want, "%s: flipped digit %d reads %s, expected %s"
           % (name, Me, df, want))
        ok(hits == [istar, estar + (M - 1) * e],
           "%s: hits %s" % (name, hits))
        print("  %-12s e=%-3d M=%d Me=%-3d anchor %s; digit %d changed -> %s "
              "at weight %d" % (name, e, M, Me, fmt(front), Me, fmt(df),
                                estar + Me))


# ------------------------------------------------------------ the censuses

def census(p, e, rng, verbose):
    """Every digit string of length M e: {frontier: count}, the rung
    table and the w_8 split count."""
    istar = e // (p - 1)
    c0, M = seat_split(p, istar)
    Me = M * e
    cap = p * istar + (M - 1) * e + 1
    counts, by_string = {}, {}
    for k in range(p ** Me):
        digs = [1]
        kk = k
        for _ in range(Me):
            digs.append(kk % p)
            kk //= p
        pad = digs + [0] * (cap + 3 - len(digs))
        fr, hits, _c = digit_frontier(p, e, pad)
        counts[fr] = counts.get(fr, 0) + 1
        by_string[tuple(digs[1:])] = (fr, hits)
    return counts, by_string


def run():
    t0 = time.time()
    rng = random.Random(1179)
    print("THE WHOLE JUMP SET FROM THE DIGITS")
    print("=" * 64)

    print("[PR7] controls")
    R = DigitRing(2, 2, [1, 0, 0, 0, 0, 0, 0, 0], 8)
    m1 = R.zeta_p(2)
    ok(R.mul(m1, m1) == R.one, "(-1)^2 != 1 in the digit ring")
    fr, hits, cap = digit_frontier(2, 2, [1, 0] + [0] * 8)
    ok(fr == ((1, 2), (3, 1)) and hits == [2, 3, 4],
       "x^2-2 control: %s hits %s" % (fr, hits))
    front, dig, cap, F = engine_read("x^2-2", 2, [-2, 0, 1])
    ok(dig[:2] == [1, 0], "x^2-2 digits %s" % dig[:4])
    fr = read("x^6+3x+3", 3, [3, 3, 0, 0, 0, 0, 1], rng)
    ok(fr == ((1, 2), (4, 1)), "x^6+3x+3 control")
    fr = read("zeta8", 2, [2, 4, 6, 4, 1], rng)
    ok(fr == ((1, 3),), "zeta8 control")
    print("  controls hit\n")

    print("[PR1, PR2] the tame readout's twenty, x^12 - 2, the quadratics")
    n_open = n_closed = 0
    for name, p, eis in ro.tame_fields():
        fr = read(name, p, eis, rng)
        n_open += fr is not None
        n_closed += fr is None
    read("x^12-2", 2, [-2] + [0] * 11 + [1], rng)
    n_open += 1
    quads = [("x^2-2", [-2, 0, 1]), ("x^2+2", [2, 0, 1]),
             ("x^2-10", [-10, 0, 1]), ("x^2+10", [10, 0, 1]),
             ("x^2+2x-2", [-2, 2, 1]), ("x^2+2x+2", [2, 2, 1])]
    for name, eis in quads:
        read(name, 2, eis, rng)
        n_open += 1

    print("\n[PR1, PR2] 512 Haar-random octics, seed 1179")
    hrng = random.Random(1179)
    octs = {}
    for _ in range(512):
        eis = rt.haar_octic(hrng, 8, 6)
        fr = read("e=8", 2, eis, rng, verbose=False)
        octs[fr] = octs.get(fr, 0) + 1
        n_open += 1
    print("  %d jump sets over 512 octics, digit ring = engine at every one"
          % len(octs))

    print()
    sharpness(rng)

    print("\n[PR4, PR5] the digit censuses at e = 2 and e = 4")
    for e in (2, 4):
        counts, by_string = census(2, e, rng, True)
        law = jh.law(2, e)
        n = (e.bit_length() - 1) * e
        total = 2 ** n
        print("  e=%d: %d digit strings of length %d, %d jump sets"
              % (e, total, n, len(counts)))
        off = 0
        for fr in sorted(counts, key=lambda f: -counts[f]):
            want = law.get(fr, 0) * total
            mark = "" if want == counts[fr] else "   <-- law %s" % want
            off += want != counts[fr]
            print("    %-28s %4d  (law %s)%s"
                  % (fmt(fr), counts[fr], want, mark))
        ok(off == 0 and set(law) == set(counts),
           "e=%d: the digit census is not the Haar law" % e)
        if e == 4:
            # PR5: the rung is a function of w_1..w_5; the frontier splits at w_8
            rung_by = {}
            for digs, (fr, hits) in by_string.items():
                w2 = jh.rho_k(2, 4, *fr[1]) if len(fr) > 1 else None
                rung = 14 if w2 is None else min(w2, 14)
                rung_by.setdefault(digs[:5], set()).add(rung)
            ok(all(len(v) == 1 for v in rung_by.values()),
               "the rung is not a function of w_1..w_5")
            split8 = sum(1 for digs, (fr, _h) in by_string.items()
                         if digs[7] == 0
                         and by_string[digs[:7] + (1,)][0] != fr)
            split7 = sum(1 for digs, (fr, _h) in by_string.items()
                         if digs[6] == 0 and digs[7] == 0
                         and len({by_string[digs[:6] + (a, b)][0]
                                  for a in (0, 1) for b in (0, 1)}) > 1)
            ok(split8 >= 1, "no cell splits at w_8")
            print("    the rung is a function of w_1..w_5 (%d rung values); "
                  "%d of 128 precision-7 cells split at w_8; %d of 64 "
                  "precision-6 cells split below" % (
                      len({next(iter(v)) for v in rung_by.values()}),
                      split8, split7))
            for digs, (fr, hits) in sorted(by_string.items()):
                if digs[7] == 0 and by_string[digs[:7] + (1,)][0] != fr:
                    print("    split cell w_1..w_7 = %s: w_8=0 %s hits %s | "
                          "w_8=1 %s hits %s" % (
                              "".join(map(str, digs[:7])), fmt(fr), hits,
                              fmt(by_string[digs[:7] + (1,)][0]),
                              by_string[digs[:7] + (1,)][1]))

    print("\n[PR6] 2048 uniform digit strings at e = 8, precision 24")
    law8 = jh.law(2, 8)
    counts = {}
    for _ in range(2048):
        digs = [1] + [rng.randrange(2) for _ in range(24 + 8 + 4)]
        fr, hits, _c = digit_frontier(2, 8, digs)
        counts[fr] = counts.get(fr, 0) + 1
    off_law = [fr for fr in counts if fr not in law8]
    ok(not off_law, "a frontier outside the admissible set at e = 8")
    worst, chi, df, z = rt.band(counts, law8, 2048)
    ok(worst < 3.5, "worst |z| %.2f" % worst)
    print("  %d jump sets; worst |z| %.2f over classes with expected >= 8; "
          "chi-square %.1f on %d df, deviate %+.2f" % (len(counts), worst,
                                                        chi, df, z))
    top = sorted(counts.items(), key=lambda kv: -kv[1])[:6]
    for fr, n in top:
        print("    %-28s %4d  (law %.1f)" % (fmt(fr), n, float(law8[fr]) * 2048))

    print("\nVERDICT: PR1-PR7 hit at %d open-gate and %d closed-gate fields; "
          "%d checks, %.1f s" % (n_open, n_closed, CHECKS, time.time() - t0))


if __name__ == "__main__":
    run()
