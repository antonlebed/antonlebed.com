"""The on-line delay in a base that is not an integer: is the delay of a
non-affine map still the margin law's L* when the streams and the
output are written in base beta over {-1, 0, 1}, beta the golden mean
or the Narayana root, where the prefixes form no lattice at all?

THE QUESTION. The many-stream theorem (explore_manystream_delay.py) and
its gap-set clause (explore_gap_lattice.py) read the delay of a map at
an integer radix b: the prefixes at a depth are integers, the output
cells are translates of one hull by integers, and either the reader has
no strategy (the contiguous case, the delay exactly the margin law's)
or a strategy that buys nothing at every pair reached (the gap sets).
Take instead a base beta > 1, the real root of x^2 = x + 1 (the golden
mean, 1.618...) or of x^3 = x^2 + 1 (the Narayana root, 1.4656...),
with the digits {-1, 0, 1} on every stream and on the output. A prefix
at depth n is the element sum d_i beta^(n - i) of Z[beta], the cells
at a depth are the hull's translates by those prefixes, and two
prefixes of one depth differ by an element of Z[beta] whose real value
is generically not an integer, so the zones of two legal parents need
not agree -- the gap sets' state-dependence, aperiodic now. Does the
margin law, written in the base, still give the delay?

THE DERIVATION, written before the engine. Let M = 1/(beta - 1); the
tail set of a prefix is T = (D + T)/beta with hull [-M, M] of width
w = 2M, and T is the whole hull iff the digit images d + [-M, M] cover
beta [-M, M] = [-M - 1, M + 1], iff the gap 1 between consecutive
digits is at most w, iff beta - 1 <= 2: interval tails at both bases.
A parent q's children at depth t + 1 are beta q + d + [-M, M] in the
child's units, their union the parent exactly, and consecutive children
overlap in a ZONE [beta q + d + 1 - M, beta q + d + M] of length w - 1.
THE STATE LEMMA transfers verbatim: the image inside the parent fits no
child iff it strictly contains a zone of that parent, since the
children are consecutive overlapping intervals covering the parent.
SUFFICIENCY transfers with the base in the exponent: at output depth
t + 1 the reader has read t + 1 + c input digits, the image is at most
Lam w beta^-(t + 1 + c) wide (Lam the box width rate, the sup over the
window of the gradient's L1 norm), a zone is (w - 1) beta^(o - t - 1)
long, so

    beta^L (w - 1) >= Lam w,   L = c + o,

suffices, with L* its least L. NECESSITY does not transfer: the
theorem's first step, any legal digit as good as any other, is the
image-only lemma, false where the parents' zones misalign, and its
second, the phases along a lattice line, has no lattice to run on. By
hand at the golden mean: M = beta, w = 2 beta, w - 1 = 2 beta - 1;
x y has Lam = 2M = 2 beta, the law beta^L (2 beta - 1) >= 4 beta^2,
4 beta^2 / (2 beta - 1) = 4.683 against beta^3 = 4.236 and beta^4 =
6.854, so L* = 4; its range [-beta^2, beta^2] fits beta^o [-beta, beta]
first at o = 1, the lookahead 3. The divider x / (s + y) at P = 1 has
s = M + 1 = beta^2, Lam = (P + M)/P^2 = beta^2, the law
beta^L (2 beta - 1) >= 2 beta^3, 3.789 against beta^2 = 2.618 and
beta^3 = 4.236, so L* = 3 at o = 0. At the Narayana root
beta^2 (beta - 1) = 1, so M = beta^2 = 2.148, w = 4.296, w - 1 = 3.296;
x y: Lam w / (w - 1) = 5.599 against beta^4 = 4.614 and beta^5 = 6.762,
L* = 5, o = 2 (M^2 <= beta^2 M with equality); the divider:
(1 + M) w / (w - 1) = 4.103 against beta^3 = 3.148 and beta^4 = 4.614,
L* = 4, o = 0. The engine decides every one of these EXACTLY, an
element of Q(beta) as an integer vector in the power basis, a sign by
a float evaluation with an error bound and, where that is silent, by
refining beta's rational isolation interval until the interval
evaluation is one-signed; equality is the zero vector.

THE SLATE, frozen before the engine. Bases: the golden mean and the
Narayana root, digits {-1, 0, 1}. Maps: x y and the divider x/(s + y)
at P = 1. The instrument is the exhaustive game tree at lookahead c and
lead o, the reader choosing among legal digits and the adversary among
all input digit pairs, a death at round r exact and a survival to the
tree's depth a bounded certificate. The control is the same engine at
the integer base 2 over {-1, 0, 1} (the minimal polynomial x = 2, the
elements integers), read against the many-stream engine's own law and
tree at the cell (2, 1, 1), the divider there at P = 1 = 1/(b - 1),
the record's pole distance.

P-A THE TAILS. Interval at both bases (beta - 1 <= 2), w = 2/(beta - 1).
P-B THE LAW. As derived by hand above: golden x y L* = 4 at o = 1, the
    divider L* = 3 at o = 0; Narayana x y L* = 5 at o = 2, the divider
    L* = 4 at o = 0.
P-C THE STRATEGY WITNESS. Images at input depth 3 with two legal
    parents at output depth 3 of different verdicts: TRANSPLANT from
    the gap sets (a witness at 17 of the 23 state-dependent sets): a
    positive count at both bases for x y. The derivation's own
    reading agrees: two parents differ by an element of Z[beta] whose
    real value is not an integer, so a zone of one that contains no
    zone of the other is generic.
P-D THE GAME. TRANSPLANT from the contiguous theorem and the gap sets:
    dead at L* - 1 within rounds 1 to 4, alive at L* to the tree's
    depth. The derivation's own reading, the line's kill below: the
    parents form no lattice, so the reader's strategy may buy a digit,
    the tree alive at L* - 1 past round 4.
P-E THE LEAD RAISED AT A TOUCHING SET. At radix 3 over {-2, 0, 1, 2}
    (touching, z_min = 0, every pair dead at every L <= 3 at the
    record's lead, the first digit killing where the root's touching
    point lies inside the range) the tree at the lead raised by one:
    the root gains siblings, the first-digit kill moves to a later
    round or the pair survives some L to the tree's depth.

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROL. At the integer base 2 over {-1, 0, 1} the engine's L*
   and lead differing from explore_manystream_delay.py's law_L and
   least_lead for x y or the divider, or its tree's verdict at L* - 1
   or L* differing from that engine's certificate at the same budget
   (dead against alive, or a different death round) -> nothing below
   is read.
K2 THE STATE LEMMA. At any node, "no legal child" disagreeing with
   "the image strictly contains a zone of the parent".
K3 THE SUFFICIENCY HALF. The tree dead at L* at either base and map.
K4 THE CONFINEMENT. The confined tree (the adversary's moves outside
   the excess region skipped) dying at a different round from the full
   tree at any pair the full tree killed.
K5 THE CONFINED GAP READER. At radix 3 over {-3, -1, 0, 1, 2}, x y at
   L = 2, where explore_gap_lattice.py's full tree died at round 4 after
   surviving 3: the confined gap reader dying at any other round.
THE TWO UNREACHED PAIRS of the gap-set record: the divider at radix 3
over {-3, -2, -1, 0, 2} and {-2, 0, 1, 2, 3}, alive at L* - 1 = 3 to
three rounds at 10.6 million nodes of the full tree, run under the
confined gap reader to whatever round its budget reaches; dead at any
round closes the gap-set clause's "26 of 28" to 28 of 28, alive to
round 5 or deeper is the line's kill.
THE LINE'S KILL: a non-affine map alive at L* - 1 to a depth past the
contiguous kill rounds (round 5 or deeper), or K3; either prints "the
delay is not one margin law across numerations".

POSITIVE CONTROL: K1, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. At (2, 1, 1) the engine's L* = 2 and o = 0 for
   x y and the divider equal the many-stream engine's, and both trees
   kill at L = 1 at round 2 and survive L = 2 to three rounds. K1 never
   fired; K2 never fired at any node of any tree.

F2 THE TAILS AND THE LAW [property]. Interval at both bases. Golden:
   M = 1.618, w = 3.236, w - 1 = 2.236; x y L* = 4 at o = 1, the
   divider L* = 3 at o = 0. Narayana: M = 2.148, w = 4.296,
   w - 1 = 3.296; x y L* = 5 at o = 2, the divider L* = 4 at o = 0.
   Every value the hand derivation named, decided exactly.

F3 THE READER HAS A STRATEGY [observation at depth 3]. Of the 45
   images with two legal parents, 16 disagree at the golden mean (19
   prefixes per stream) and 1 at the Narayana root (27 prefixes): death
   is not image-only at either base.

F4 THE GAME [rule at the four pairs]. Dead at L* - 1 at every pair and
   alive at L* to the full tree's depth (2, or 1 at the Narayana
   divider), where the excess region is EMPTY, so the confined tree is
   the law's sufficiency verbatim. The kill rounds: the golden divider
   at 4 (74,366 nodes of the full tree), the Narayana product at 4
   (74,364), and the golden product and the Narayana divider at ROUND
   5 (626 and 785 nodes of the confined tree, where the full tree
   survived three rounds at 150,000 nodes and, at the rehearsal, the
   Narayana divider three rounds at three million): one round past the
   contiguous and gap-set kills, the strategy delaying the kill and
   never escaping it. The transplant held; the line's kill did not
   fire, by one round.

F5 THE CONFINEMENT [property, checked]. The confined tree reproduces
   the full tree's kill round at every pair the full tree killed (K4:
   the golden divider and the Narayana product at round 4; K5: x y at
   radix 3 over {-3, -1, 0, 1, 2}, L = 2, at round 4 with 36,539 nodes
   against the full tree's ten million) and reaches the deep kills at
   under 800 nodes.

F6 THE TWO UNREACHED PAIRS ARE DEAD. At radix 3 the divider at L = 3
   (the generalized law's L* = 4) over {-3, -2, -1, 0, 2} dies at
   round 4 with 36,708 nodes and over {-2, 0, 1, 2, 3} at round 4 with
   286,169: the gap-set clause's "26 of 28" is 28 of 28.

F7 THE LEAD RAISED AT A TOUCHING SET [observation at L <= 3]. At radix
   3 over {-2, 0, 1, 2} the first-digit kill moves from round 1 to
   round 2 at every L in 0..3 for x y and the divider alike: the
   root's siblings buy exactly one round and no L.

VERDICT. In base beta over {-1, 0, 1} at the golden mean and the
Narayana root the delay of x y and the divider is the margin law's L*
in the base, beta^L (w - 1) >= Lam w, although the reader has a
strategy at both bases and the prefixes form no lattice; the kills
sit at rounds 4 and 5, one round deeper than at any integer radix. The
margin law holds as a law across three numerations and its necessity
proof is the contiguous case's alone.

RUN RECORD: pure Python, integer vectors for every verdict; under
memwatch, peak commit 42 MB against the 512 MB default, wall 101 s at
the tree budget 150,000 and the confined budget three million. Prints
reproduced by:
python prime/code/explore_beta_delay.py [NODE_BUDGET]
"""

import itertools
import math
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_manystream_delay as ms                      # noqa: E402
import explore_gap_lattice as gl                           # noqa: E402

FAILURES = []
TREE_BUDGET = 150_000
DEEP_BUDGET = 3_000_000
WITNESS_DEPTH = 3
WALL_CAP = 240.0


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print("  KILL:", msg)


def isign(x):
    return (x > 0) - (x < 0)


# ------------------------------------------------------------ the base

class Base:
    """Z[beta], beta the real root above 1 of x^D = c_0 + c_1 x + ... +
    c_(D-1) x^(D-1); an element is a tuple of D integers in the power
    basis. D = 1 is the integer radix c_0."""

    def __init__(self, name, coeffs):
        self.name, self.c, self.D = name, tuple(coeffs), len(coeffs)
        D = self.D
        self.zero = (0,) * D
        self.one = (1,) + (0,) * (D - 1)
        self.beta = (0, 1) + (0,) * (D - 2) if D > 1 else (coeffs[0],)
        self.bm1 = self.sub(self.beta, self.one)
        # the isolating interval: minpoly < 0 at lo, > 0 at hi, one root above 1
        if D == 1:
            self.lo = self.hi = Fr(coeffs[0])
            self.fl = float(coeffs[0])
        else:
            lo, hi = Fr(1), Fr(2)
            while self.minpoly_at(hi) <= 0:
                hi *= 2
            for _ in range(256):
                mid = (lo + hi) / 2
                if self.minpoly_at(mid) < 0:
                    lo = mid
                else:
                    hi = mid
            self.lo, self.hi = lo, hi
            self.fl = float((lo + hi) / 2)
        self.flpow = [self.fl ** i for i in range(D)]
        self._pw = {0: self.one, 1: self.beta}

    def minpoly_at(self, x):
        return x ** self.D - sum(ci * x ** i for i, ci in enumerate(self.c))

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def scale(self, k, a):
        return tuple(k * x for x in a)

    def mul(self, a, b):
        D = self.D
        if D == 1:
            return (a[0] * b[0],)
        r = [0] * (2 * D - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    r[i + j] += x * y
        for k in range(2 * D - 2, D - 1, -1):
            coef = r[k]
            if coef:
                r[k] = 0
                for i, ci in enumerate(self.c):
                    r[k - D + i] += coef * ci
        return tuple(r[:D])

    def power(self, k):
        if k not in self._pw:
            self._pw[k] = self.mul(self.power(k - 1), self.beta)
        return self._pw[k]

    def sign(self, a):
        if not any(a):
            return 0
        if self.D == 1:
            return isign(a[0])
        val = 0.0
        bound = 0.0
        for x, p in zip(a, self.flpow):
            val += x * p
            bound += abs(x) * p
        bound *= 1e-13
        if val > bound:
            return 1
        if val < -bound:
            return -1
        return self._sign_exact(a)

    def _sign_exact(self, a):
        lo, hi = self.lo, self.hi
        while True:
            vlo, vhi = self._horner_iv(a, lo, hi)
            if vlo > 0:
                return 1
            if vhi < 0:
                return -1
            mid = (lo + hi) / 2
            if self.minpoly_at(mid) < 0:
                lo = mid
            else:
                hi = mid

    def _horner_iv(self, a, lo, hi):
        """Interval evaluation of sum a_i x^i over x in [lo, hi] > 0."""
        vlo, vhi = Fr(0), Fr(0)
        for x in reversed(a):
            cands = (vlo * lo, vlo * hi, vhi * lo, vhi * hi)
            vlo, vhi = min(cands) + x, max(cands) + x
        return vlo, vhi

    # fractions of elements: (num, den) with den > 0
    def le(self, fa, fb):
        return self.sign(self.sub(self.mul(fa[0], fb[1]), self.mul(fb[0], fa[1]))) <= 0

    def lt(self, fa, fb):
        return self.sign(self.sub(self.mul(fa[0], fb[1]), self.mul(fb[0], fa[1]))) < 0

    def fpow(self, k):
        """beta^k as a fraction, k of either sign."""
        return (self.power(k), self.one) if k >= 0 else (self.one, self.power(-k))

    def fmul(self, fa, fb):
        return self.mul(fa[0], fb[0]), self.mul(fa[1], fb[1])

    def ffloat(self, fa):
        return self.tofloat(fa[0]) / self.tofloat(fa[1])

    def tofloat(self, a):
        return sum(x * p for x, p in zip(a, self.flpow))

    def prefixes(self, n, a=1):
        """The representable prefix elements at depth n, one coordinate,
        over the digits {-a, ..., a}."""
        cur = {self.zero}
        for _ in range(n):
            nxt = set()
            for u in cur:
                bu = self.mul(self.beta, u)
                for d in range(-a, a + 1):
                    nxt.add(self.add(bu, self.scale(d, self.one)))
            cur = nxt
        return sorted(cur, key=self.tofloat)


# ------------------------------------------------------------- the maps

class BProduct:
    name, d = "x y", 2

    def __init__(self, B):
        self.B = B

    def image(self, xs, ys, den, betan):
        """Corners as elements over the common den; returns (lo, hi) fractions."""
        B = self.B
        c = [B.mul(x, y) for x in xs for y in ys]
        lo = hi = c[0]
        for e in c[1:]:
            if B.sign(B.sub(e, lo)) < 0:
                lo = e
            if B.sign(B.sub(e, hi)) > 0:
                hi = e
        d2 = B.mul(den, den)
        return (lo, d2), (hi, d2)

    def window_range(self, M):
        B = self.B
        M2 = B.fmul(M, M)
        return (B.neg(M2[0]), M2[1]), M2

    def lam(self, M):
        return self.B.scale(2, M[0]), M[1]

    def grad_sup(self, box):
        """sup over the box of |d_x f| + |d_y f| (floats): max|y| + max|x|."""
        return max(abs(box[1][0]), abs(box[1][1])) + max(abs(box[0][0]), abs(box[0][1]))


class BDivision:
    """x / (s + y), s = M + P, P = p/q > 0."""
    d = 2

    def __init__(self, B, p, q, a=1):
        self.B, self.p, self.q = B, p, q
        self.name = f"x/(M + {p}/{q} + y)" if q != 1 else f"x/(M + {p} + y)"
        # s = M + p/q = (q a + p (beta - 1)) / (q (beta - 1)), M = a/(beta - 1)
        self.s_num = B.add(B.scale(q * a, B.one), B.scale(p, B.bm1))
        self.sf = B.ffloat((self.s_num, B.scale(q, B.bm1)))

    def image(self, xs, ys, den, betan):
        """den = (beta - 1) beta^n; xs, ys the corner numerators."""
        B, q = self.B, self.q
        sb = B.mul(self.s_num, betan)                 # s_num beta^n
        D1 = B.add(sb, B.scale(q, ys[0]))
        D2 = B.add(sb, B.scale(q, ys[1]))
        N1, N2 = B.scale(q, xs[0]), B.scale(q, xs[1])
        dh = D1 if B.sign(N2) > 0 else D2
        dl = D1 if B.sign(N1) < 0 else D2
        return (N1, dl), (N2, dh)

    def window_range(self, M):
        B = self.B
        r = B.fmul(M, (B.scale(self.q, B.one), B.scale(self.p, B.one)))
        return (B.neg(r[0]), r[1]), r

    def grad_sup(self, box):
        """sup of 1/D + |x|/D^2 over the box, D = s + y at its least."""
        s = self.sf
        D = s + box[1][0]
        return 1 / D + max(abs(box[0][0]), abs(box[0][1])) / (D * D)

    def lam(self, M):
        """(P + M) / P^2 = (p/q + M) q^2 / p^2."""
        B = self.B
        pq = (B.scale(self.p, B.one), B.scale(self.q, B.one))
        s = (B.add(B.mul(pq[0], M[1]), B.mul(M[0], pq[1])), B.mul(pq[1], M[1]))
        return B.mul(s[0], B.scale(self.q * self.q, B.one)), B.mul(s[1], B.scale(self.p * self.p, B.one))


# ------------------------------------------------------------- the law

def least_lead(B, fmap, a=1):
    M = (B.scale(a, B.one), B.bm1)
    lo, hi = fmap.window_range(M)

    def fits(o):
        Mo = B.fmul(M, B.fpow(o))
        return B.le((B.neg(Mo[0]), Mo[1]), lo) and B.le(hi, Mo)
    o = 0
    if fits(0):
        while o > -60 and fits(o - 1):
            o -= 1
    else:
        while not fits(o):
            o += 1
    return o


def law_L(B, fmap, a=1):
    """Least L with beta^L (w - 1) >= Lam w, w = 2M, M = a/(beta - 1)."""
    M = (B.scale(a, B.one), B.bm1)
    w = (B.scale(2, M[0]), M[1])
    z = (B.sub(w[0], w[1]), w[1])
    rhs = B.fmul(fmap.lam(M), w)

    def holds(L):
        return B.le(rhs, B.fmul(B.fpow(L), z))
    if B.sign(z[0]) <= 0:
        raise ValueError(f"{B.name}: the zone has no length, the law admits no L")
    L = 0
    while not holds(L):
        L += 1
    while L > -60 and holds(L - 1):
        L -= 1
    return L, z, w


# ------------------------------------------------------------ the game

class Budget(Exception):
    pass


class BetaReader:
    """The reading game in base beta over {-1, 0, 1} at lookahead c and
    lead o, the state lemma checked at every node."""

    def __init__(self, B, fmap, c, o, a=1):
        self.B, self.f, self.c, self.o, self.a = B, fmap, c, o, a
        self.d = fmap.d
        self.digits = tuple(range(-a, a + 1))
        self.aone = B.scale(a, B.one)
        self.delem = {d: B.scale(d, B.one) for d in self.digits}
        self.moves = list(itertools.product(self.digits, repeat=self.d))
        self.nodes = 0
        self.lemma_checked = 0
        self.budget = None
        self.t_end = None
        self.confined = False
        # the law's threshold at this L: (w - 1) beta^(c + o) / w, floats
        M = B.ffloat((self.aone, B.bm1))
        w = 2 * M
        self.Mf, self.wf = M, w
        self.lam_law = (w - 1) * B.fl ** (c + o) / w

    def in_region(self, us, n):
        """Does the box's width rate exceed the law's threshold? A box
        below it (with a margin, so the float errs toward keeping the
        box) can never straddle, nor can any descendant."""
        s = self.B.fl ** n
        box = [((self.B.tofloat(u) - self.Mf) / s, (self.B.tofloat(u) + self.Mf) / s) for u in us]
        return self.f.grad_sup(box) > self.lam_law * (1 - 1e-9)

    def image(self, us, n):
        B = self.B
        betan = B.power(n)
        den = B.mul(B.bm1, betan)
        corners = [(B.sub(B.mul(u, B.bm1), self.aone), B.add(B.mul(u, B.bm1), self.aone)) for u in us]
        return self.f.image(corners[0], corners[1], den, betan)

    def cell(self, q, t):
        """The output cell of prefix q at depth t: beta^(o - t) (q +- M)."""
        B, o = self.B, self.o
        qm = B.mul(q, B.bm1)
        lo, hi = B.sub(qm, self.aone), B.add(qm, self.aone)
        if o >= 0:
            p = B.power(o)
            den = B.mul(B.bm1, B.power(t))
            return (B.mul(lo, p), den), (B.mul(hi, p), den)
        den = B.mul(B.bm1, B.power(t - o))
        return (lo, den), (hi, den)

    def legal(self, us, n, q, t):
        c1, c2 = self.cell(q, t)
        lo, hi = self.image(us, n)
        return self.B.le(c1, lo) and self.B.le(hi, c2)

    def child(self, q, d):
        return self.B.add(self.B.mul(self.B.beta, q), self.delem[d])

    def dead_by_zone(self, us, n, q, t):
        lo, hi = self.image(us, n)
        for d in self.digits[:-1]:
            bot = self.cell(self.child(q, d + 1), t + 1)[0]
            top = self.cell(self.child(q, d), t + 1)[1]
            if self.B.lt(top, hi) and self.B.lt(lo, bot):
                return True
        return False

    def extend(self, us, n, n1):
        """The adversary's prefixes at depth n1 below us at depth n, one
        digit tuple at a time; confined, a partial prefix outside the
        excess region is pruned with every completion (a completion's
        box lies inside it)."""
        if n == n1:
            yield us
            return
        B = self.B
        for mv in self.moves:
            us1 = tuple(B.add(B.mul(B.beta, u), self.delem[x]) for u, x in zip(us, mv))
            if self.confined and not self.in_region(us1, n + 1):
                continue
            yield from self.extend(us1, n + 1, n1)

    def survives(self, us, n, q, t, rounds):
        if rounds == 0:
            return True
        n1 = max(0, t + 1 + self.c)
        B = self.B
        for us1 in self.extend(us, n, n1):
            self.nodes += 1
            if self.nodes > self.budget or time.time() > self.t_end:
                raise Budget()
            legal = [p for p in self.digits if self.legal(us1, n1, self.child(q, p), t + 1)]
            if self.lemma_checked < 100_000:
                self.lemma_checked += 1
                ok((not legal) == self.dead_by_zone(us1, n1, q, t),
                   f"K2 state lemma at {B.name} {self.f.name} c={self.c} o={self.o}: "
                   f"us={us1} n={n1} q={q} t={t}")
            alive = False
            for p in legal:
                if self.survives(us1, n1, self.child(q, p), t + 1, rounds - 1):
                    alive = True
                    break
            if not alive:
                return False
        return True

    def certificate(self, budget, wall=WALL_CAP, max_rounds=8, confined=False):
        """Iterative deepening until the budget or the wall: (death
        round or None, the deepest round completed). Confined: the
        adversary's moves outside the excess region are skipped, which
        loses no kill and no survival (a box below the threshold has
        an image no wider than any zone, as does every descendant)."""
        self.budget, self.t_end = budget, time.time() + wall
        self.confined = confined
        root = (self.B.zero,) * self.d
        ok(self.legal(root, 0, self.B.zero, 0),
           f"ROOT ILLEGAL at {self.B.name} {self.f.name} a={self.a} o={self.o}: the lead is wrong")
        if not self.legal(root, 0, self.B.zero, 0):
            return 0, 0
        done = 0
        for r in range(1, max_rounds + 1):
            try:
                if not self.survives(root, 0, self.B.zero, 0, r):
                    return r, done
            except Budget:
                return None, done
            done = r
        return None, done

    def witness_count(self, n, t):
        reps = self.B.prefixes(n, self.a)
        parents = self.B.prefixes(t, self.a)
        images = disagree = 0
        for us in itertools.product(reps, repeat=self.d):
            legal_q = [q for q in parents if self.legal(us, n, q, t)]
            if len(legal_q) < 2:
                continue
            images += 1
            if len({self.dead_by_zone(us, n, q, t) for q in legal_q}) == 2:
                disagree += 1
        return images, disagree, len(reps), len(parents)


def game(B, fmap, Ls, budget, label):
    o = least_lead(B, fmap)
    out = {}
    for L in Ls:
        rd = BetaReader(B, fmap, L - o, o)
        t1 = time.time()
        r, depth = rd.certificate(budget)
        out[L] = (r, depth, rd.nodes, time.time() - t1)
    words = ", ".join(f"L={L}: {'dead r=' + str(r) if r is not None else 'alive'} [{d}] "
                      f"{nd} nodes {s:.1f}s" for L, (r, d, nd, s) in out.items())
    print(f"  {label} o={o}: {words}")
    return o, out


# ---------------------------------------------------------------- runs

def control(budget):
    print("\n=== K1 THE CONTROL: the integer base 2 over {-1, 0, 1} against the many-stream engine")
    B = Base("base 2", (2,))
    b, am, ap = 2, 1, 1
    for fmap, mmap in ((BProduct(B), ms.Product(b, am, ap)),
                       (BDivision(B, 1, 1), ms.Division(b, am, ap, Fr(1, 1)))):
        L, z, w = law_L(B, fmap)
        o = least_lead(B, fmap)
        Le, oe = ms.law_L(b, am, ap, mmap), ms.least_lead(b, am, ap, mmap)
        ok(L == Le, f"K1 {fmap.name}: L*={L} against law_L={Le}")
        ok(o == oe, f"K1 {fmap.name}: o={o} against least_lead={oe}")
        _, res = game(B, fmap, (L - 1, L), budget, f"(2,1,1) {fmap.name} L*={L}")
        for LL in (L - 1, L):
            rd = ms.ReaderD(b, am, ap, LL - oe, mmap, oe)
            r, depth = rd.certificate_depth(budget)
            print(f"    many-stream engine at L={LL}: {'dead r=' + str(r) if r is not None else 'alive'} [{depth}]")
            ok(res[LL][0] == r, f"K1 {fmap.name} L={LL}: engine {res[LL][0]} against many-stream {r}")


def bases():
    return [Base("golden (x^2 = x + 1)", (1, 1)), Base("Narayana (x^3 = x^2 + 1)", (1, 0, 1))]


def tails_and_law(B):
    print(f"\n=== {B.name}: beta = {B.fl:.6f}")
    M = (B.one, B.bm1)
    w = B.ffloat(M) * 2
    interval = B.fl - 1 <= 2
    print(f"  P-A tails: {'interval' if interval else 'Cantor'} (beta - 1 = {B.fl - 1:.4f} <= 2), "
          f"M = {B.ffloat(M):.4f}, w = {w:.4f}, w - 1 = {w - 1:.4f}")
    ok(interval, f"{B.name}: Cantor tails")
    rows = []
    for fmap in (BProduct(B), BDivision(B, 1, 1)):
        L, z, wf = law_L(B, fmap)
        o = least_lead(B, fmap)
        lam = B.ffloat(fmap.lam(M))
        print(f"  P-B law {fmap.name}: Lam = {lam:.4f}, Lam w / (w - 1) = {lam * w / (w - 1):.4f}, "
              f"beta^{L - 1} = {B.fl ** (L - 1):.4f}, beta^{L} = {B.fl ** L:.4f}: L* = {L}, o = {o}, c* = {L - o}")
        rows.append((fmap, L, o))
    return rows


def witness(B):
    rd = BetaReader(B, BProduct(B), 0, 0)
    images, dis, nr, npar = rd.witness_count(WITNESS_DEPTH, WITNESS_DEPTH)
    print(f"  P-C witness x y at depth {WITNESS_DEPTH}: {nr} prefixes per stream, {npar} parents; "
          f"{images} images with two legal parents, {dis} disagreeing")
    return dis


def games(B, rows, budget):
    out = []
    for fmap, L, o in rows:
        _, res = game(B, fmap, (L - 1, L), budget, f"  P-D {fmap.name} L*={L}")
        ok(res[L][0] is None, f"K3 {B.name} {fmap.name}: tree dead at L* = {L} (round {res[L][0]})")
        out.append((fmap, L, o, res))
    return out


def deepen(B, rows, budget):
    for fmap, L, o, res in rows:
        if res[L - 1][0] is not None:
            rd = BetaReader(B, fmap, L - 1 - o, o)
            r, depth = rd.certificate(budget, confined=True)
            print(f"  K4 confined control {B.name} {fmap.name} L={L - 1}: "
                  f"{'dead r=' + str(r) if r is not None else 'alive'} [{depth}] {rd.nodes} nodes "
                  f"against the full tree's r={res[L - 1][0]}")
            ok(r == res[L - 1][0], f"K4 {B.name} {fmap.name} L={L - 1}: confined round {r} against full {res[L - 1][0]}")
            continue
        rd = BetaReader(B, fmap, L - 1 - o, o)
        t1 = time.time()
        r, depth = rd.certificate(budget, confined=True)
        print(f"  DEEPENING (confined) {B.name} {fmap.name} L={L - 1} (L*={L}): "
              f"{'dead r=' + str(r) if r is not None else 'alive'} [{depth}] {rd.nodes} nodes {time.time() - t1:.1f}s")
        res[L - 1] = (r, depth, rd.nodes, time.time() - t1)
    for fmap, L, o, res in rows:
        rd = BetaReader(B, fmap, L - o, o)
        t1 = time.time()
        r, depth = rd.certificate(budget, confined=True)
        verdict = ("the excess region is EMPTY, the law's sufficiency verbatim"
                   if rd.nodes == 0 else
                   f"{'dead r=' + str(r) if r is not None else 'alive'} [{depth}] {rd.nodes} nodes")
        print(f"  AT L* (confined) {B.name} {fmap.name} L={L}: {verdict} {time.time() - t1:.1f}s")
        ok(r is None, f"K3 {B.name} {fmap.name}: confined tree dead at L* = {L} (round {r})")


class ConfinedGap(gl.GapReader):
    """The gap-set reader with the adversary confined to the excess
    region of the generalized law: a box whose width rate is at most
    z_min b^L / w has an image no wider than any zone, so it and its
    descendants never kill."""

    def __init__(self, b, D, c, fmap, o):
        super().__init__(b, D, c, fmap, o)
        _, w, _, zmin = gl.tail_verdict(b, D)
        self.lam_law = float(zmin) * float(b) ** (c + o) / float(w) * (1 - 1e-9)
        self.budget = None
        self.t_end = None

    def extend(self, us, n, n1):
        if n == n1:
            yield us
            return
        for mv in self.moves:
            us1 = tuple(self.b * u + x for u, x in zip(us, mv))
            if not self.in_region(self.box_float(us1, n + 1)):
                continue
            yield from self.extend(us1, n + 1, n1)

    def survives(self, us, n, q, t, rounds, confined=False):
        if rounds == 0:
            return True
        n1 = max(0, t + 1 + self.c)
        for us1 in self.extend(us, n, n1):
            self.nodes += 1
            if self.nodes > self.budget or time.time() > self.t_end:
                raise Budget()
            legal = [p for p in self.digits if self.legal(us1, n1, self.b * q + p, t + 1)]
            if self.lemma_checked < 100_000:
                self.lemma_checked += 1
                ok((not legal) == self.dead_by_zone(us1, n1, q, t),
                   f"K2 state lemma at ({self.b},{self.digits}) {self.f.name} c={self.c}")
            alive = False
            for p in legal:
                if self.survives(us1, n1, self.b * q + p, t + 1, rounds - 1):
                    alive = True
                    break
            if not alive:
                return False
        return True

    def certificate(self, budget, wall=WALL_CAP, max_rounds=8):
        self.budget, self.t_end = budget, time.time() + wall
        root = (0,) * self.d
        if not self.legal(root, 0, 0, 0):
            return 0, 0
        done = 0
        for r in range(1, max_rounds + 1):
            try:
                if not self.survives(root, 0, 0, 0, r):
                    return r, done
            except Budget:
                return None, done
            done = r
        return None, done


def unreached_pairs(budget):
    print("\n=== THE TWO UNREACHED DIVIDER PAIRS at radix 3 (explore_gap_lattice.py F4), the confined tree")
    b = 3
    runs = [((-3, -1, 0, 1, 2), "x y", 2, 4, "K5 control: the full tree's kill at round 4"),
            ((-3, -2, -1, 0, 2), "div", 3, None, "unreached at 3 rounds, 10.6 million nodes"),
            ((-2, 0, 1, 2, 3), "div", 3, None, "unreached at 3 rounds, 10.6 million nodes")]
    for D, nm, L, expect, note in runs:
        am, ap = -min(D), max(D)
        fmap = ms.Product(b, am, ap) if nm == "x y" else ms.Division(b, am, ap, Fr(1, b - 1))
        Lg = gl.law_gen(b, D, fmap)
        o = ms.least_lead(b, am, ap, fmap)
        rd = ConfinedGap(b, D, L - o, fmap, o)
        t1 = time.time()
        r, depth = rd.certificate(budget)
        print(f"  radix 3 {list(D)} {fmap.name} L={L} (law L*={Lg}, o={o}; {note}): "
              f"{'dead r=' + str(r) if r is not None else 'alive'} [{depth}] {rd.nodes} nodes {time.time() - t1:.1f}s")
        if expect is not None:
            ok(r == expect, f"K5 radix 3 {list(D)} {fmap.name} L={L}: confined round {r} against the full tree's {expect}")


def touching_lead():
    print("\n=== P-E THE LEAD RAISED BY ONE at radix 3 over {-2, 0, 1, 2}, x y and the divider")
    b, D = 3, (-2, 0, 1, 2)
    am, ap = 2, 2
    for fmap in (ms.Product(b, am, ap), ms.Division(b, am, ap, Fr(1, 2))):
        o0 = ms.least_lead(b, am, ap, fmap)
        for o in (o0, o0 + 1):
            res = {}
            for L in range(0, 4):
                rd = gl.GapReader(b, D, L - o, fmap, o)
                r, depth = rd.certificate(gl.TREE_BUDGET)
                res[L] = (r, depth)
            words = ", ".join(f"L={L}: {'dead r=' + str(r) if r is not None else 'alive'} [{d}]"
                              for L, (r, d) in res.items())
            print(f"  {fmap.name} o={o}{' (the record)' if o == o0 else ' (raised)'}: {words}")


def main():
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else TREE_BUDGET
    t0 = time.time()
    control(budget)
    summary = []
    for B in bases():
        rows = tails_and_law(B)
        dis = witness(B)
        res = games(B, rows, budget)
        deepen(B, res, DEEP_BUDGET)
        summary.append((B, dis, res))
    touching_lead()
    unreached_pairs(DEEP_BUDGET)
    print("\n=== SUMMARY: the two bases side by side")
    for B, dis, res in summary:
        for fmap, L, o, r in res:
            below = r[L - 1]
            at = r[L]
            print(f"  {B.name} {fmap.name}: L*={L} o={o} c*={L - o}; at L*-1 "
                  f"{'dead r=' + str(below[0]) if below[0] is not None else 'ALIVE'} [{below[1]}]; "
                  f"at L* {'DEAD r=' + str(at[0]) if at[0] is not None else 'alive'} [{at[1]}]; "
                  f"witness {dis}")
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
