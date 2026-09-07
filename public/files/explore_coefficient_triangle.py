"""explore_coefficient_triangle.py — THE COEFFICIENT TRIANGLE: is the
digit string of w a unitriangular function of the Eisenstein
coefficients' digits in level order, deriving the mass law?

THE QUESTION. A totally ramified f = 1 window K/Q_p is given by an
Eisenstein polynomial F = x^e + sum_{i=1}^{e-1} p b_i x^i - p d, d a
unit, with pi its root, and w = -p/pi^e (2/pi^e at p = 2) is the
window's unit. The jump set of K is a function of the first M e digits
of w, M = v_p(i*), i* = e/(p - 1) (explore_jump_digits.py), the hit
vector of the greedy dlog of zeta_p is a unitriangular function of
those digits and the jump set its record reading, so Pagano's mass law
is the pushforward of the uniform measure on digit strings
(explore_hit_triangle.py). Not derived was why HAAR-random Eisenstein
windows give uniform digits: the digit census matched the law's counts
cell by cell and the audit refused "the digit cells are Haar cells".
The window word w_1..w_{3e/2-1} at p = 2 is a unitriangular function of
the sub-leading coefficient bits (explore_readout_triangle.py), and
every deeper bit of b_i feeds level i + ke and no lower level
(explore_reduction_law.py). This rig asks whether that pricing is the
whole story at EVERY level: is the map from the coefficients' digits,
ordered by the level each first enters, to the digits of w
unitriangular, at every p?

THE OBJECTS. THE COEFFICIENT DIGITS: b_i = sum_k beta_{i,k} p^k and
d = d_0 + sum_{k>=1} delta_k p^k in base p, digits in {0, ..., p-1};
d_0 = p - 1 at the open gate (w_0 = 1 iff d = -1 mod p, since
w = -1/d mod pi), d_0 = 1 at p = 2 always. THE LEVEL of beta_{i,k} is
i + ke (1 <= i <= e-1, k >= 0) and of delta_k is ke (k >= 1): every
level r >= 1 carries EXACTLY ONE coefficient digit, the one at
(i, k) = (r mod e, r div e), and the first M e levels carry
M(e - 1) + M = M e digits, as many as the jump set reads. THE DIGITS
OF w: the canonical expansion w = sum w_r pi^r, w_r in {0, ..., p-1},
computed in O_K = Z_p[pi] by valuation and subtraction, the same
reading as explore_jump_digits.py's engine digits. THE DIGIT RING
(explore_jump_digits.py): digit strings under p = -w pi^e
(2 = w pi^e at p = 2), a carry at level s landing at s + e with w's
digits.

THE HAND DERIVATION (on paper, before the engine).

H1  THE FIXED-POINT EQUATION. F(pi) = 0 reads pi^e = p (d - sum b_i
    pi^i) = p D, so w = -p/pi^e = -1/D, and inside the digit ring,
    where p = -w pi^e, D = d_0 + sum_{k>=1} delta_k (-w)^k pi^{ke}
    - sum_{i,k} beta_{i,k} (-w)^k pi^{i+ke}: each coefficient digit
    enters as a monomial at ITS level times a power of w, whose
    digit-0 is 1. So D = d_0 (1 + E) with E a sum of terms each of
    level >= 1, one term per coefficient digit, the level-r term
    being (a unit) x (the level-r digit) x pi^r x (1 + higher digits
    of w), and w = -(1/d_0)(1 - E + E^2 - ...).
H2  THE TRIANGLE. The level-r digit of w reads: the level-r digit of
    -E, which is (a unit) x (the level-r coefficient digit) plus,
    from every other term of E, its level-s digit with s < r times a
    digit w_j of w with j = r - s >= 1, j <= r - 1; the level-r digit
    of E^n, n >= 2, a sum of products of n factors each of level
    >= 1 and so each <= r - 1; and the carries, born at levels
    s <= r - e and landing w_j at s + e + j = r, j <= r - e - 1. By
    induction on r every w_j with j < r is a function of the
    coefficient digits at levels < r, so w_r = u_r c_r + g_r(c_1,
    ..., c_{r-1}) with c_r the level-r coefficient digit and u_r a
    unit mod p (u_r = +-1: (-1)^{k} from (-w)^k, the sign of the
    beta terms, and 1/d_0^2 = 1). The map from the coefficient
    digits at levels 1..N to w_1..w_N is unitriangular over F_p at
    EVERY N, hence a bijection F_p^N -> F_p^N, and in the limit a
    bijection from Eisenstein polynomials with the open gate onto
    digit strings with w_0 = 1: the digit string is a complete
    invariant of the Eisenstein polynomial. Nothing here uses the
    parity of e or the value of p; at p = 2 the parity of e enters
    only through 3e/2, the word's length.
H3  THE TWO TRUNCATIONS. explore_readout_triangle.py's grid map is
    this map at levels 1..3e/2-1, its parameter order (beta_i at
    levels i < e, delta at e, gamma_i = beta_{i,1} at e + i) being the
    level order; the reduction law is the statement that the map is
    triangular, a digit at level >= 3e/2 moving no digit of the word;
    the odd-p word's "b_i mod p; d mod p^2" is the same at levels
    1..e. And the jump set's M e digits are the truncation at M e:
    the M e coefficient digits at levels 1..Me fix the jump set, and
    no fewer do (the digit precision's anchor split, read through the
    bijection).
H4  THE MASS LAW FROM THE COEFFICIENTS. The Haar measure on Eisenstein
    polynomials makes the coefficient digits independent and uniform
    on {0, ..., p-1} (b_i uniform in Z_p, d uniform in the units;
    conditioned on the open gate, d_0 = p - 1 and every other digit
    stays uniform). A unitriangular bijection pushes independent
    uniform digits forward to independent uniform digits, so the digit
    string of w is uniform (H2), the hit vector is uniform
    (explore_hit_triangle.py H1) and the jump set's law is the record
    reading's pushforward (H3 there), which is Pagano's law. So at
    every p, given Theorem 1.4 for the module, the mass law is derived
    from the coefficients through three unitriangular maps composed:
    coefficient digits -> digits of w -> hit vector -> jump set, the
    last a record reading. Pagano's Theorem 10.1 excludes p = 2 with
    e even; the composed triangle does not.
H5  THE FIRST ROWS BY HAND at p = 2, e = 4, with beta_i = beta_{i,0}:
    w_1 = beta_1; w_2 = beta_2 + beta_1 (T^2's beta_1^2 = beta_1);
    w_3 = beta_3 + beta_1 (T^3's beta_1^3; T^2's cross term
    2 beta_1 beta_2 pi^3 = beta_1 beta_2 w pi^7 lands at 7). At
    e = 2: w_1 = beta_1, w_2 = delta_1 + beta_1 (x^2 + 2x - 6 prints
    (1, 0), explore_reduction_law.py RD5). x^e - 2 prints the all-zero
    string at every e (w = 1 exactly), and x^e + p at odd p; x^e - 3
    has d = 1 and the closed gate.

PREDICTIONS, fixed before the engine ran.
  PR1 (bijection, exhaustive at (p, e) = (2, 4)). The 256 Eisenstein
      cells (b_1, b_2, b_3 mod 4; d mod 8, odd) print 256 distinct
      strings w_1..w_8, each cell's string the same at two random
      lifts of the cell. KILL: two cells sharing a string, or a cell
      whose lifts differ below level 9.
  PR2 (the diagonal at p = 2, flips). At e = 2, 4, 6, 8, 12 (c_0 = 3),
      16, over sampled Eisenstein polynomials and every level
      r <= Me + e: flipping the level-r bit flips w_r and moves no
      w_j, j < r. KILL: one (polynomial, r) off.
  PR3 (the diagonal at odd p). At (3, 6), (3, 12) with c_0 = 2,
      (3, 18), (5, 20), open gate, over sampled polynomials and every
      r <= Me: adding t p^k to the level-r coefficient, t = 0..p-1,
      leaves w_1..w_{r-1} fixed and runs w_r through all of F_p.
      Control: d not -1 mod p gives w_0 != 1. KILL: one (polynomial,
      r) off.
  PR4 (the reader, read first). This rig's digits of w equal
      explore_jump_digits.py's engine digits at x^2 - 2, Phi_8(x + 1),
      x^12 - 2, x^6 + 3x + 3, x^6 + 3x^3 + 3, x^6 + 6x^3 + 3 and eight
      Haar-random octics, to CAP + 2; and the composed reading
      (digits -> hit vector -> records, explore_hit_triangle.py)
      equals the module engine's frontier at each. KILL: one off.
  PR5 (the mass law from the coefficients, exhaustive). Over the 4
      cells at (2, 2), the 256 at (2, 4) and the 729 open-gate cells
      at (3, 6) (b_i mod 3, d mod 9 with d = 2 mod 3) the composed
      triangle's jump sets fall in the counts of
      explore_jump_haar.py's law times the cell count: 2, 1, 1 and
      128, 32, 32, 16, 16, 16, 8, 4, 2, 2. KILL: one count off.
  PR6 (controls, read first). x^e - 2 at p = 2 and x^e + p at odd p
      (d = -1 exactly, so w = -1/D = 1) print all zeros to level
      Me + e at e = 2, 4, 8, 16 and at (3, 6), (5, 20); the skeleton
      design x^e + 2x^{e/2} + 4x^{e/4} - 6 prints nonzero exactly at
      {e/2, 5e/4} below 3e/2 at e = 8, 16; the hand rows H5 at e = 2
      and e = 4 (w_1..w_3) hold at every cell.
  PR7 (the rows). The algebraic normal forms of w_1..w_8 over the 8
      bits at e = 4 and of w_1..w_12 over the 12 bits at e = 8 each
      carry the diagonal bit with coefficient 1 and no bit of higher
      level. KILL: a diagonal coefficient 0 or a higher bit present.

THE DESIGN. engine: O_K = Z_p[x]/(F) modulo p^N as coefficient vectors,
N = M + 4 (enough for Me + e + 1 digits), w = -1/D by Newton's
iteration, the canonical digits by valuation and subtraction, a digit
tried over F_p at odd p; the coefficient digit at level r is
(i, k) = (r mod e, r div e), changed by adding t p^k to b_i (i >= 1) or
to d (i = 0). The composed reading imports explore_hit_triangle.py's
hit_vector and records over explore_jump_digits.py's digit ring; the
law is explore_jump_haar.py's; the module engine is
explore_jump_digits.py's engine_read. Samples from seed 1181. verdict:
PR1-PR7 as counts.
Run: python prime/code/explore_coefficient_triangle.py

FINDINGS (entered post-run, copied from printed output).

1. THE COEFFICIENT TRIANGLE (PR1, PR2, PR3 hit). The 256 Eisenstein
   cells at (2, 4) print 256 distinct strings w_1..w_8, each the same at
   two random lifts, and the 4 at (2, 2) and 729 open-gate cells at
   (3, 6) likewise. At 1136 (polynomial, level) pairs over (2, 2), (2, 4),
   (2, 6) with c_0 = 3, (2, 8), (2, 12) with c_0 = 3, (2, 16) to level 80,
   (3, 6), (3, 12) with c_0 = 2, (3, 18) and (5, 20), changing the
   level-r coefficient digit through F_p leaves w_1..w_{r-1} fixed and
   runs w_r through all of F_p: every level a unit, at p = 2 to e past
   the jump set's precision. d = -1 mod p is the open gate and d - 1 the
   closed one at every odd-p cell.

2. THE READER (PR4, PR6 hit). This rig's digits are
   explore_jump_digits.py's engine digits to CAP + 2 at 14 fields
   (x^2 - 2, Phi_8(x + 1), x^12 - 2, three sextics at p = 3, eight
   Haar-random octics), and the composed reading digits -> hit vector
   -> records is the module engine's frontier at each; x^e - 2 and
   x^e + p print w = 1 at six cells; the skeleton design prints
   {e/2, 5e/4} at e = 8, 16.

3. THE MASS LAW FROM THE COEFFICIENTS (PR5 hit). The composed
   triangle's jump sets over the Eisenstein cells: 2, 1, 1 at (2, 2);
   128, 32, 32, 16, 16, 16, 8, 4, 2, 2 at (2, 4); 486, 162, 54, 18, 6,
   3 at (3, 6) — the law's masses times the cell count at every class.

4. THE ROWS (PR7 hit; the hand rows H5 verbatim). e = 4, bits named
   b_i.k and d_k: w_1 = b1.0; w_2 = b1.0 + b2.0; w_3 = b1.0 + b3.0;
   w_4 = b1.0 + b2.0 + d1 + b1.0 b2.0; w_5 = b1.0 + b1.1 + b1.0 b2.0 +
   b1.0 b3.0 + b1.0 d1; w_6, w_7 of degree 2; w_8 = b1.0 + b2.0 + d1 +
   d2 + b1.0 b2.0 + b2.0 b3.0 + b2.0 d1 + b3.0 b1.1 + b2.0 b2.1 +
   b1.0 b3.1 + b1.0 b2.0 d1, degree 3. e = 8: w_1..w_3 as at e = 4,
   w_4 = b1.0 + b2.0 + b4.0 + b1.0 b2.0, degrees 2 to w_10 and 3 at
   w_11, w_12; every row carries its diagonal bit and no bit above its
   level.

TIER. THE COEFFICIENT TRIANGLE — the map from the coefficient digits
of an Eisenstein polynomial, ordered by level i + ke, to the digits of
w is unitriangular over F_p at every level and every p, so a bijection
from open-gate Eisenstein polynomials onto digit strings with w_0 = 1
— is a THEOREM (H1-H2, the pricing of every reading of w at or above
its entry level); its instances rules at the cells read. THE MASS LAW
FROM THE COEFFICIENTS — Pagano's law is the pushforward of the Haar
measure on Eisenstein polynomials through three unitriangular maps
composed — is a THEOREM at every p given Theorem 1.4 (H4 with
explore_hit_triangle.py H1-H3), its instances rules at (2, 2), (2, 4),
(3, 6). The rows are records of the computation.

RUN RECORD. python prime/code/memwatch.py prime/code/explore_coefficient_triangle.py:
16.3 s wall, peak working set 16.9 MB, 175,850 checks. PRE-GREEN
FAILURES, two, both in the controls' own statements and neither in a
prediction about the triangle: the odd-p w = 1 control was written as
d = p - 1 (x^6 - 6, whose w has digit 2 at level 6) where w = 1 needs
d = -1 exactly (x^e + p); the closed-gate control added 1 to
d = -1 mod p, which is no unit, and subtracts 1 now.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_jump_digits as jd  # noqa: E402
import explore_hit_triangle as ht  # noqa: E402
import explore_jump_haar as jh  # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ------------------------------------------------------------ the ring O_K / p^N

class Window:
    """K = Q_p[x]/(F), F = x^e + sum p b_i x^i - p d, elements as
    coefficient vectors of length e over Z/p^N."""

    def __init__(self, p, e, b, d, N):
        self.p, self.e, self.N = p, e, N
        self.pN = p ** N
        self.b = [x % self.pN for x in b]     # b[i], i = 0..e-1, b[0] unused
        self.d = d % self.pN
        # pi^e = p (d - sum b_i pi^i)
        self.top = [(p * self.d) % self.pN] + [(-p * self.b[i]) % self.pN for i in range(1, e)]

    def mul(self, x, y):
        e, pN = self.e, self.pN
        prod = [0] * (2 * e - 1)
        for i, xi in enumerate(x):
            if xi:
                for j, yj in enumerate(y):
                    prod[i + j] = (prod[i + j] + xi * yj) % pN
        for k in range(2 * e - 2, e - 1, -1):
            c = prod[k]
            if c:
                prod[k] = 0
                for j, t in enumerate(self.top):
                    prod[k - e + j] = (prod[k - e + j] + c * t) % pN
        return prod[:e]

    def sub(self, x, y):
        return [(a - c) % self.pN for a, c in zip(x, y)]

    def const(self, c):
        return [c % self.pN] + [0] * (self.e - 1)

    def pi_pow(self, r):
        el = self.const(1)
        pi = [0, 1] + [0] * (self.e - 2)
        for _ in range(r):
            el = self.mul(el, pi)
        return el

    def val(self, x):
        """v_pi(x) as min over j of e v_p(c_j) + j; None at zero."""
        best = None
        for j, c in enumerate(x):
            if c == 0:
                continue
            k = 0
            while c % self.p == 0:
                c //= self.p
                k += 1
            v = self.e * k + j
            if best is None or v < best:
                best = v
        return best

    def inverse(self, D):
        """1/D for a unit D by Newton's iteration x <- x(2 - Dx)."""
        d0 = D[0] % self.p
        x = self.const(pow(d0, -1, self.p))
        two = self.const(2)
        for _ in range(12):
            x = self.mul(x, self.sub(two, self.mul(D, x)))
        ok(self.val(self.sub(self.mul(D, x), self.const(1))) is None
           or self.val(self.sub(self.mul(D, x), self.const(1))) >= self.e * (self.N - 1),
           "inverse not exact")
        return x

    def w(self):
        """w = -p/pi^e = -1/D, D = d - sum b_i pi^i."""
        D = [self.d] + [(-self.b[i]) % self.pN for i in range(1, self.e)]
        inv = self.inverse(D)
        if self.p == 2:
            return inv
        return [(-c) % self.pN for c in inv]

    def digits(self, x, n):
        """The canonical digits x_0..x_{n-1}, n <= e (N - 1)."""
        ok(n <= self.e * (self.N - 1), "digits past precision")
        out = []
        pows = [self.pi_pow(r) for r in range(n)]
        for r in range(n):
            v = self.val(x)
            if v is None or v > r:
                out.append(0)
                continue
            ok(v == r, "valuation below the level")
            for a in range(1, self.p):
                y = self.sub(x, [(a * c) % self.pN for c in pows[r]])
                vy = self.val(y)
                if vy is None or vy > r:
                    out.append(a)
                    x = y
                    break
            else:
                ok(False, "no digit clears level %d" % r)
        return out


def geometry(p, e):
    return ht.geometry(p, e)


def w_digits(p, e, b, d, n):
    istar, c0, M, estar, cap = geometry(p, e)
    N = M + 4
    while e * (N - 1) < n:
        N += 1
    W = Window(p, e, b, d, N)
    return W.digits(W.w(), n)


def level_param(e, r):
    """(i, k) of the coefficient digit at level r."""
    return r % e, r // e


def bump(p, e, b, d, r, t):
    """Add t p^k to the level-r coefficient."""
    i, k = level_param(e, r)
    b2, d2 = list(b), d
    if i == 0:
        d2 = d + t * p ** k
    else:
        b2[i] = b[i] + t * p ** k
    return b2, d2


def random_eis(p, e, rng, N):
    b = [0] + [rng.randrange(p ** N) for _ in range(e - 1)]
    d = rng.randrange(p ** N)
    d = d - d % p + (p - 1)           # d = -1 mod p: the open gate
    return b, d


def eis_list(p, e, b, d):
    """Coefficients low to high for the module engine."""
    return [(-p * d)] + [p * b[i] for i in range(1, e)] + [1]


def composed(p, e, dig):
    """(frontier, hit vector) from the digit string via the hit triangle."""
    istar, c0, M, estar, cap = geometry(p, e)
    padded = list(dig) + [0] * (cap + 3 - len(dig))
    hits = ht.hit_vector(p, e, padded)
    return ht.records(p, e, hits), hits


# ------------------------------------------------------------ the stages

def stage_controls():
    print("[PR6, PR4] controls: the reader against the engine and the known prints")
    for p, e in ((2, 2), (2, 4), (2, 8), (2, 16), (3, 6), (5, 20)):
        istar, c0, M, estar, cap = geometry(p, e)
        n = M * e + e + 1
        dig = w_digits(p, e, [0] * e, -1 if p > 2 else 1, n)
        ok(dig[0] == 1 and not any(dig[1:]), "(%d, %d) x^e - p d, d = -1: digits %s" % (p, e, dig))
    print("  x^e - 2 and x^e + p print w = 1 at six cells")
    for e in (8, 16):
        b = [0] * e
        b[e // 2] = 1
        b[e // 4] = 2
        dig = w_digits(2, e, b, 3, 3 * e // 2)
        nz = [r for r in range(1, 3 * e // 2) if dig[r]]
        ok(nz == [e // 2, 5 * e // 4], "skeleton design at e = %d: nonzero at %s" % (e, nz))
    print("  the skeleton design prints {e/2, 5e/4} at e = 8, 16")
    fields = [("x^2-2", 2, [-2, 0, 1]), ("zeta8", 2, [2, 4, 6, 4, 1]),
              ("x^12-2", 2, [-2] + [0] * 11 + [1]),
              ("x^6+3x+3", 3, [3, 3, 0, 0, 0, 0, 1]),
              ("x^6+3x^3+3", 3, [3, 0, 0, 3, 0, 0, 1]),
              ("x^6+6x^3+3", 3, [3, 0, 0, 6, 0, 0, 1])]
    rng = random.Random(1181)
    for j in range(8):
        eis = [2 * rng.randrange(-8, 8) for _ in range(8)] + [1]
        eis[0] = 2 * (2 * rng.randrange(-8, 8) + 1)
        fields.append(("octic%d" % j, 2, eis))
    n_read = 0
    for name, p, eis in fields:
        e = len(eis) - 1
        front, dig, cap, F = jd.engine_read(name, p, eis)
        ok(front is not None, "%s: gate closed" % name)
        d = (-eis[0] // p)
        b = [0] + [eis[i] // p for i in range(1, e)]
        mine = w_digits(p, e, b, d, cap + 2)
        ok(mine == list(dig[:cap + 2]), "%s: digits %s, engine %s" % (name, mine, dig[:cap + 2]))
        fr, hits = composed(p, e, mine)
        ok(fr == front, "%s: composed %s, engine %s" % (name, fr, front))
        n_read += 1
    print("  %d fields: this reader's digits are the engine's to CAP + 2, and the\n"
          "  composed reading is the engine's frontier at each" % n_read)


def stage_bijection():
    print("\n[PR1, PR5, PR6] the exhaustive cells")
    rng = random.Random(1181)
    # (2, 2): 4 cells; (2, 4): 256 cells; (3, 6): 729 open-gate cells
    for p, e in ((2, 2), (2, 4), (3, 6)):
        istar, c0, M, estar, cap = geometry(p, e)
        Me = M * e
        seen = {}
        counts = {}
        for code in range(p ** Me):
            # the level-r digit of the code is the level-r coefficient digit
            b = [0] * e
            d = p - 1 if p > 2 else 1
            for r in range(1, Me + 1):
                t = (code // p ** (r - 1)) % p
                b, d = bump(p, e, b, d, r, t)
            dig = w_digits(p, e, b, d, Me + 1)
            key = tuple(dig[1:])
            ok(key not in seen, "(%d, %d): cells %s and %s share the string %s"
               % (p, e, seen.get(key), (b, d), key))
            seen[key] = (list(b), d)
            # two random lifts of the cell agree below Me + 1
            for _ in range(2):
                b2 = [0] + [b[i] + p ** (M + 1) * rng.randrange(p ** 3) for i in range(1, e)]
                d2 = d + p ** (M + 1) * rng.randrange(p ** 3)
                ok(w_digits(p, e, b2, d2, Me + 1) == dig,
                   "(%d, %d): a lift of the cell %s moved a digit below %d" % (p, e, (b, d), Me + 1))
            if p == 2 and e == 4:
                beta = [0] + [b[i] % 2 for i in range(1, 4)]
                ok(dig[1] == beta[1] and dig[2] == (beta[2] + beta[1]) % 2
                   and dig[3] == (beta[3] + beta[1]) % 2,
                   "e = 4 hand rows off at %s: %s" % ((b, d), dig))
            if p == 2 and e == 2:
                ok(dig[1] == b[1] % 2 and dig[2] == ((d // 2) + b[1]) % 2,
                   "e = 2 hand rows off at %s: %s" % ((b, d), dig))
            fr, hits = composed(p, e, dig)
            counts[fr] = counts.get(fr, 0) + 1
        law = jh.law(p, e)
        ok(set(counts) == set(law), "(%d, %d): classes %s vs law %s" % (p, e, set(counts), set(law)))
        off = [fr for fr in law if counts[fr] != law[fr] * p ** Me]
        ok(not off, "(%d, %d): counts off at %s" % (p, e, off))
        print("  (p, e) = (%d, %d): %d cells, %d strings, the hand rows hold, jump-set counts %s"
              % (p, e, p ** Me, len(seen),
                 sorted(counts.values(), reverse=True)))


def stage_flips():
    print("\n[PR2, PR3] the diagonal by flips")
    rng = random.Random(1181)
    cells = [(2, 2, 12), (2, 4, 12), (2, 6, 8), (2, 8, 8), (2, 12, 4), (2, 16, 3),
             (3, 6, 8), (3, 12, 4), (3, 18, 2), (5, 20, 2)]
    total = 0
    for p, e, n in cells:
        istar, c0, M, estar, cap = geometry(p, e)
        Me = M * e
        R = Me + e if p == 2 else Me
        N = M + 4
        while e * (N - 1) < R + 1:
            N += 1
        for _ in range(n):
            b, d = random_eis(p, e, rng, N)
            base = w_digits(p, e, b, d, R + 1)
            ok(base[0] == 1, "(%d, %d): gate closed at an open-gate draw" % (p, e))
            for r in range(1, R + 1):
                seen = set()
                for t in range(p):
                    b2, d2 = bump(p, e, b, d, r, t)
                    dig = w_digits(p, e, b2, d2, R + 1)
                    ok(dig[:r] == base[:r],
                       "(%d, %d) r = %d: a change at level %d moved a digit below it" % (p, e, r, r))
                    seen.add(dig[r])
                ok(len(seen) == p, "(%d, %d) r = %d: digits %s, not F_%d" % (p, e, r, sorted(seen), p))
                total += 1
        if p > 2:
            b, d = random_eis(p, e, rng, N)
            dig = w_digits(p, e, b, d - 1, 1)
            ok(dig[0] != 1, "(%d, %d): d != -1 mod p left the gate open" % (p, e))
        print("  (p, e) = (%d, %d) c_0 = %d M = %d Me = %-2d: %d polynomials, levels 1..%d, every level a unit"
              % (p, e, c0, M, Me, n, R))
    print("  %d (polynomial, level) pairs, each a permutation of F_p at its level" % total)


def stage_rows():
    print("\n[PR7] the algebraic normal forms at p = 2")
    for e, R in ((4, 8), (8, 12)):
        table = {}
        for code in range(1 << R):
            b = [0] * e
            d = 1
            for r in range(1, R + 1):
                t = (code >> (r - 1)) & 1
                b, d = bump(2, e, b, d, r, t)
            table[code] = w_digits(2, e, b, d, R + 1)
        print("  e = %d:" % e)
        for r in range(1, R + 1):
            f = [table[code][r] for code in range(1 << r)]   # codes with higher bits 0
            monos = ht.anf(f, r)
            ok((1 << (r - 1)) in monos, "e = %d: w_%d lacks its diagonal" % (e, r))
            # no dependence on higher bits: compare codes differing only above r
            for code in range(1 << R):
                ok(table[code][r] == table[code & ((1 << r) - 1)][r],
                   "e = %d: w_%d reads a bit above level %d" % (e, r, r))
            deg = max(bin(m).count("1") for m in monos)
            names = {}
            for j in range(1, r + 1):
                i, k = level_param(e, j)
                names[j] = ("d%d" % k) if i == 0 else ("b%d.%d" % (i, k))
            terms = []
            for m in sorted(monos, key=lambda m: (bin(m).count("1"), m)):
                terms.append("1" if m == 0 else "".join(
                    names[j + 1] + " " for j in range(m.bit_length()) if m >> j & 1).strip().replace(" ", "*"))
            print("    w_%-2d = %s   (degree %d)" % (r, " + ".join(terms), deg))


def run():
    t0 = time.time()
    print("THE COEFFICIENT TRIANGLE")
    print("=" * 64)
    stage_controls()
    stage_bijection()
    stage_flips()
    stage_rows()
    print("\nVERDICT: PR1-PR7 hit; %d checks, %.1f s" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    run()
