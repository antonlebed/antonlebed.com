"""
size.py -- what a residue window cannot read about size, and what the
cheapest exact read of size costs.

USE. In Python, from the folder holding size.py. The
least key reads floor(x/m_k) and x mod m_k off a residue word alone,
and compare orders two words by it:

    >>> from size import least_key, compare
    >>> ms = (2, 3, 5, 7, 11, 13, 17)          # Z/510510
    >>> a = tuple(1000 % m for m in ms)
    >>> b = tuple(999 % m for m in ms)
    >>> least_key(a, ms)                       # 1000 = 17 * 58 + 14
    (58, 14)
    >>> compare(a, b, ms)
    1

QUESTION. A residue window reads an integer x in [0, M) through its
residues x mod p at the places p of M. Which maps can such a window
compute channel by channel, why is size (sign, comparison, overflow)
not among them, how completely is size hidden from a proper window,
and what is the least a reader must add to compare two residue words
exactly? Which of these answers are about windows, and which are about
the archimedean place the integers happen to have?

THE ARGUMENT (written before this script).
  (1) THE LOCALITY CRITERION. Call F : R -> R on a finite ring
      R = K_1 x ... x K_k (a product of finite fields: a squarefree
      Z/M, or F_2[x]/f with f squarefree) CHANNEL-LOCAL when the i-th
      component of F(x) depends only on the i-th component of x. Then
      F is channel-local iff it is a polynomial function. A polynomial
      is evaluated componentwise; conversely each component map
      K_i -> K_i is a Lagrange polynomial of degree < |K_i|, and the
      coefficients glue degree by degree by the CRT. The same proof
      runs in several variables. The equivalence needs the fields:
      over Z/8 the channel-local maps (value mod 2 fixed by argument mod 2)
      number 2^2 * 4^8 = 262,144, and the polynomial maps are Kempner's
      8 * 8 * 4 * 4 = 1,024.
  (2) THE SIZE WALL. Read x as its least residue. For every prime
      p | M with p < M, sign(x) = [x >= M/2] is not channel-local at p:
      0 and b = p * ceil(M/(2p)) agree mod p, and M/2 <= b <= M - 1
      because p <= M/2. The same pair walls comparison [x < y] (at
      (0, 0) against (0, b)) and overflow [x + y >= M] (at (0, 0)
      against (b, b)). A channel-local bijection T has a channel-local
      inverse, so sign o T is channel-local at no prime p | M below M
      either: no channel-local change of coordinates, linear or not,
      exposes size.
  (3) THE HIDING LEMMA. In any cyclic Z/M, knowing x mod W for a proper
      divisor W of M leaves x on the ladder r + jW, j < c = M/W.
      Exactly c/2 of the ladder sits at or above M/2 when c is even; when
      c is odd it is (c - 1)/2 or (c + 1)/2 as r < W/2 or not. So the
      sign bit's bias in every fiber is exactly 0 or exactly half an
      element, 0 iff c is even. Cyclic orientation is hidden totally:
      translate a triple's base point to 0, where orientation is integer
      comparison on (0, M); each ladder holds an element <= W and one
      >= (c - 1)W, so the extreme completions give both orientations,
      unless both ladders are {W} at c = 2 (no distinct triple).
  (4) THE HALF-COVERAGE LAW. Read x in [1, X] through x mod Q, for any
      Q <= X. The fiber of x has one lift iff x - Q < 1 and x + Q > X,
      so exactly max(0, 2Q - X) elements are determined. Every fiber's
      least lift is <= Q and its greatest is > X - Q, so two fibers can
      be ordered with certainty only if X - Q + 1 <= a < b <= Q for
      some lifts, which needs 2Q - X >= 2; conversely at 2Q - X >= 2
      the elements X - Q + 1 and X - Q + 2 are both determined. At a
      divisor Q | X, Q < X, the best guess of [a < b] from the residues
      (order the residues) is right on exactly X(X + Q - 2)/2 of the
      X(X - 1) ordered pairs of distinct elements, half of them at
      Q = 1: order leaks at every Q >= 2 while certainty waits for
      half.
  (5) THE RELATIONAL FORM. A relation R on Z/M is CONJUNCTIVE when it
      equals the conjunction of its projections to the channels.
      Equality is; divisibility is (x | y iff y_p = 0 wherever x_p = 0,
      channel by channel); the order x <= y is not, and fails
      maximally: every projection is all of F_p x F_p (take
      x < p <= y <= 2p - 1, in range when M >= 2p), so the conjunction is
      everything. Conjunctive iff R is a rectangle (rank 1) at every
      split of one channel against the rest: a set equal to the
      product of its projection and its co-projection for every
      coordinate is the product of all its projections (replace one
      coordinate at a time).
  (6) THE EXACT COMPARATOR. Pairwise coprime moduli m_1 < ... < m_k,
      M their product, S = sum M/m_i, D(x) = sum floor(x/m_i) on
      [0, M). (i) gcd(M, S) = 1: modulo a prime of m_i every term but
      M/m_i carries m_i. (ii) M * D(x) = S * x - sum (M/m_i) x_i, so
      D(x) = -M^(-1) sum (M/m_i) x_i mod S, and 0 <= D <= S - k: one dot
      product of the residues mod S reads D exactly. (iii)
      D(x + 1) - D(x) counts the moduli dividing x + 1. So inside a run
      where D is constant no modulus divides a later element, every
      residue x mod m_j climbs by one without wrapping, and the run has
      at most m_1 elements. Hence key_j(x) = (D(x), x mod m_j) is strictly
      increasing on [0, M) for EVERY j: an exact comparator, with sign
      one compare against key_j(ceil(M/2)) and the overflow of x + y the
      compare key_j(z) < key_j(x), z = x + y mod M. D alone ties exactly
      the pairs inside one run; the adjacent ties are the x with no
      modulus dividing x + 1, M prod (1 - 1/m_i) of them, phi(M) when
      every modulus is prime.
  (7) THE COST LAW. The comparator's dot product is reduced mod S and
      reconstruction's mod M, and S / M = sum 1/m_i. So it is narrower
      iff sum 1/m_i < 1, and S = M never happens, by (i). The primorial
      rungs fail from k = 3 on (1/2 + 1/3 + 1/5 = 31/30), k = 2 passes
      (5/6). The Fermat numbers are pairwise coprime with
      sum 1/F_n < 0.5961, so every set of them passes. A strictly
      monotone characteristic on [0, M) takes M values, so a
      characteristic comparator computing below log2 M bits must be a
      non-injective form plus a tie-break (pigeonhole).
  (8) THE F_2[x] CONTROL. Over the ring F_2[x]/f, f squarefree with
      two or more factors, read a as its representative of degree
      < deg f. The criterion (1) holds verbatim. The top degree bit
      [deg a = deg f - 1] is channel-local at no channel f_i (0 against
      f_i * x^(deg f - 1 - deg f_i)), so the information core of the
      wall is unchanged. What goes is three things the Z side has: (a)
      every fiber of a proper window g | f is a coset r + g * P, P the
      polynomials of degree < deg f - deg g, and exactly half of it has top
      bit 1, so the bias is 0 at EVERY proper window (over Z it is half
      an element whenever M/W is odd); (b) the degree of a product is
      the sum of the degrees, no carry; (c) the partial-fraction read is exact or flags itself.
      With a/f = sum b_i / f_i (b_i = a * (f/f_i)^(-1) mod f_i), sum of
      proper fractions being proper, the t leading Laurent coefficients
      add without carries: sum_i (b_i x^t div f_i) = (a x^t) div f. That
      quotient is either nonzero, and its degree gives deg a exactly, or
      zero, which says deg a < deg f - t. Over Z the t-bit truncation of
      y/M = frac(sum y_i w_i / m_i), y_i = y mod m_i, w_i = (M/m_i)^(-1)
      mod m_i, can wrap below 0 and read a small y as a large one, with
      no flag. (Settled
      later, on an audit: this control does not say which difference
      between Z and F_2[x] owns (a) to (c). The two differ in the
      archimedean place and in the characteristic. Carries belong to
      characteristic 0, the 2-adic integers carrying too. (a) was first
      read as the fiber size 2^e being even; the F_3[x] arm below,
      added later, reads it again. Measured against the ring's
      own share, a fiber's degree profile above deg g is the same for
      every r at every q, since deg(r + g*P) = deg g + deg P for P != 0:
      the ultrametric inequality of the place degree reads. PREDICTION,
      fixed before that arm ran: at f = x(x + 1)(x^2 + 1)(x^2 + x + 2)
      over F_3, every fiber of all 15 proper windows has one profile.)
  (9) THE LEAST COMPARATOR (added after the first run, on reading
      Babenko, Piestrak, Chervyakov and Deryabin, Electronics 10 (2021)
      1041, in full). A key (G(x), x mod m_j) injective on [0, M) needs
      G to take at least M/m_j values, since the M/m_j elements of one
      residue class mod m_j must get distinct G: the pigeonhole floor,
      for ANY G. G = floor(x/m_j) attains it, and it is one dot product
      of the residues mod M/m_j: floor(x/m_j) = (B - x_j) * m_j^(-1) mod
      M/m_j, B the CRT value of the other residues mod M/m_j. The key
      is then x itself in mixed radix, strictly increasing, and the
      largest modulus m_k gives the least range. The paper works with
      core functions, weighted sums of the quotients
      floor(x/m_i); it calls this one the minimum-range
      monotonic core function and shows the diagonal D is the core
      function with every weight equal to 1. Since
      S = sum M/m_i > M/m_1 >= M/m_k, the diagonal is never the least:
      the cost law (7) compares D with the wrong rival. The least key's
      first coordinate is a reconstruction of x modulo every modulus
      but the largest.
      PREDICTION (fixed before the second run): at the four sets of D,
      floor(x/m_k) by the dot product equals the direct quotient at
      every x in [0, M), and M/m_k < S at each.
      THE KEY AS A TOOL. least_key(residues, ms) takes one residue
      word, pairwise coprime moduli in any order, and returns
      (floor(x/m_k), x mod m_k) from the residues alone;
      compare(a, b, ms) returns -1, 0 or 1 as the integers the two
      words name compare. Nothing else is read: the quotient is the dot
      product above, the CRT coefficients rebuilt per call (the calls
      are shown under USE at the head of this docstring).
      PREDICTION (fixed before the third run): at each of the four sets
      of D, on 2000 seeded pairs and every pair of the corners 0, 1,
      m_k - 1, m_k, M - 2, M - 1, compare agrees with integer
      comparison and least_key's two coordinates rebuild x as
      m_k * q + r; the words also pass in reversed modulus order.
  (10) THE ADDITIVE LABELLING (added later, on the question of a small
      size labelling). A LABELLING is a map mu : [0, N) -> L,
      |L| = s < N; it is ADD-UPDATABLE when some A : L x L -> L has
      mu(x + y) = A(mu(x), mu(y)) whenever x + y < N. Then mu(x + 1) =
      g(mu(x)) with g = A(., mu(1)), so mu is the orbit of mu(0) under
      one self-map of an s-set: injective on a prefix [0, x0) and
      periodic with period d from x0 on, x0 + d <= s. Conversely each
      such pair is the congruence of (N, +) with index x0 and period d,
      a monoid congruence, so it is add-updatable; for N > s the pairs
      give distinct labellings, and up to relabelling there are exactly
      s(s + 1)/2 of them, one for each x0 >= 0, d >= 1 with x0 + d <= s.
      The congruence respects multiplication too (x = y mod d, both
      >= x0, gives xz = yz mod d with both >= x0, or both 0), so every
      add-updatable labelling is mul-updatable for free. Labels (a, b)
      are ORDER-INFORMATIVE when every value labelled a lies below
      every value labelled b. Every label first appears below x0 + d,
      so an informative b has least value at most s - 1; and for
      values u < v both at or above s, v's label already labels a value
      below x0 + d <= s <= u, so no such pair is ordered by its labels,
      at every N > s.
      PREDICTION (fixed before section A ran): a depth-first search over
      every labelling, labels in first-occurrence order and A filled in
      as the search goes, no shape assumed, finds exactly s(s + 1)/2
      add-updatable labellings at every N in {8, 10, 12, 14} and s in
      {2, 3, 4, 5}; each is a rho with x0 + d <= s and is
      mul-updatable; the largest least value of an informative b is
      s - 1; and where N >= 2s no pair of values at or above s has an
      informative pair of labels.

PREDICTIONS (fixed before the run). Every check prints PASS. Counts:
Z/6 has 108 channel-local maps, all polynomial; Z/4 64 of 64; Z/8
1,024 polynomial of 262,144 channel-local; F_2[x]/(x(x+1)) 16 = 16;
F_2[x]/(x(x^2+x+1)) 1,024 = 1,024; F_2[x]/x^2 64 of 64; F_2[x]/x^3
1,024 of 262,144. The run over {97, 101, 103} reaches 97 elements.
At Z/510510 the D-only ties number phi = 92,160. A Z witness of the
silent wrap exists at t = 16 bits among x <= 1000 at Z/510510.

DESIGN. Sections of checks printing PASS or FAIL, a control first
where a check could pass vacuously.
  L  the locality criterion: exhaustive at Z/6; span counts at Z/4,
     Z/8 and four F_2[x] quotients, against channel-local totals that
     are the channels' map counts multiplied by hand; the Lagrange +
     CRT lift in one and two variables at Z/30 on seeded random maps.
  W  the size wall: the witness b, 0 mod p, in [M/2, M) by its own
     arithmetic (argued, the pairs to M <= 300 counted); sign o T for
     seeded channel-local bijections T of Z/30.
  H  the hiding lemma: every fiber of every proper window of every
     Z/M, M <= 240 (the high count c/2 at even c, (c - 1)/2 plus
     [r >= W/2] at odd c); orientation at every M <= 60 and every
     proper W, both orientations in every class but the antipodal one.
  C  the half-coverage law: singles at X <= 240, counted from each
     residue class's lifts, pairs at X <= 120, the accuracy count at
     every divisor budget X <= 120.
  R  the relational form at Z/210 (equality, divisibility, order) and
     the rectangle criterion at Z/30 on the same three relations;
     after the audit, betweenness as a
     ternary relation at Z/6 and Z/30 in place of its base-0
     identity.
  D  the comparator: gcd(M, S) = 1 on seeded random coprime sets; the
     dot-product formula for D at 2000 seeded x at Z/510510,
     {3, 5, 17, 257}, {97, 101, 103} and the composite set
     {15, 77, 221}, the longest run of constant D printed (the
     strictness of every key_j and the run's length m_1 are (6)(iii)'s
     argument, holding by D's definition, and are not checked); the
     D-only ties; sign and overflow at Z/210 exhaustively.
  K  the cost law: the rung sums (S/M is the same sum, printed at
     k = 2, 3, 7), the Fermat sum, two designed sets.
  Q  the least comparator (added after the first run): the dot
     product for floor(x/m_k) at every x of the four sets of D, and
     M/m_k < S; the tool (added later): least_key and
     compare on residue words at seeded pairs and corners. Its two
     controls run first, with A's, and stop the run if one fails:
     words read against the wrong modulus order must mis-compare, and
     one modulus keys a word by its residue.
  A  the additive labelling (added with (10)): the search over every
     labelling at the sixteen cells, the rho, the free multiplication,
     the height and the blind tail.
  F  the F_2[x] control at f = x(x+1)(x^2+x+1)(x^3+x+1)(x^3+x^2+1),
     degree 10: the factors' irreducibility (the degree wall is (8)'s
     argument), the zero bias at all 31 proper
     windows, deg(ab), the exact-or-flagged read at every a and every
     t from 1 to 10; and the Z wrap witness at Z/510510.

RUN RECORD. First run: 46 of 46 PASS, every prediction met. Z/6 108
channel-local, 108 polynomial of 46,656; Z/8 1,024 of 262,144;
F_2[x]/x^3 1,024 of 262,144; the two squarefree F_2[x] quotients 16 = 16
and 1,024 = 1,024. The runs of D reach 2, 3, 97 and 15 at the four sets,
each its m_1. Z/510510's D-only ties are 92,160 = phi. The orientation sweep
met 15,475 base-0 classes, and the 29 without a distinct triple are the
antipodal ones, one per even M <= 60. The Z wrap's first witness is
x = 1: its 16-bit truncated sum lands past one half. Second run, after
the source read that added (9): 50 of 50 PASS. The least range M/m_k
against the diagonal's S: 30,030 against 716,167 at Z/510510, 255 against
39,062 at {3, 5, 17, 257}, 9,797 against 30,191 at {97, 101, 103}, and
1,155 against 21,487 at {15, 77, 221}. Wall 2.8 s, peak 79 MB. After
the audit, 51 of 51: betweenness as a ternary relation, 60 triples
with a closure of 192 at Z/6 and 12,180 with 27,000 at Z/30. Then 52
of 52: the F_3[x] arm finds one degree profile per window at
all 15 proper windows, as predicted. With (10), 54 of 54: the search
finds x mod 3 and rejects [x >= 3] at N = 8, and returns 136 labellings
over the sixteen cells, s(s + 1)/2 at each, every one a rho with
x0 + d <= s, mul-updatable and blind at and above s where N >= 2s, the
largest least value of an informative label s - 1 at every cell. Wall
2.8 s, peak 81 MB. (A later proof read found N >= 2s idle: the
blindness holds at every N > s, and the check now covers the one
cell it skipped, (8, 5); still 54 of 54.) With the tool, 59 of 59:
the one-modulus control, and compare and least_key right at 2,036
pairs per set, each in both modulus orders, as predicted; the usage
lines, run by hand, give (58, 14) and 1. Wall 2.9 s. After a code
read, 51 of 51: checks that held by construction were cut (every key_j's
strictness and the longest run of D, now argued and printed; S < M iff
the rung sum < 1, now printed; the size wall's witness b and the degree
wall's), the controls run first and stop the run on a failure, the
wrong-order words mis-comparing at 404 of 900 pairs of Z/30; the bias is
now read with its sign, the singles from the residue classes' lifts,
betweenness's closure holding all 60 and 12,180 triples of the other
orientation, and the five factors irreducible. Wall 2.6 s, peak 75 MB.
With a check of the tie count at composite moduli, 52 of 52: at
{15, 77, 221} D ties 234,080 adjacent pairs, M prod (1 - 1/m_i),
against phi(M) = 92,160, where (6) had said the ties were the x with
x + 1 prime to M. Wall 2.5 s, peak 75 MB.

Run: python size.py   (a few seconds, under 100 MB)
"""

import random
from fractions import Fraction
from itertools import product
from math import gcd, prod

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tail = f"  ({detail})" if detail else ""
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{tail}")


def primes_of(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def phi(n):
    r = n
    for p in primes_of(n):
        r = r // p * (p - 1)
    return r


# ---------------------------------------------------------------- rings
# A finite commutative ring as elements 0..q-1 with add and mul tables
# built from a rule; F_2[x] elements are ints read as bit polynomials.

def clmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pdeg(a):
    return a.bit_length() - 1


def pmod(a, f):
    df = pdeg(f)
    while a and pdeg(a) >= df:
        a ^= f << (pdeg(a) - df)
    return a


def pdivmod(a, f):
    q, df = 0, pdeg(f)
    while a and pdeg(a) >= df:
        s = pdeg(a) - df
        q ^= 1 << s
        a ^= f << s
    return q, a


def pinv(a, f):
    """Inverse of a modulo f in F_2[x] (a prime to f)."""
    r0, r1, s0, s1 = f, pmod(a, f), 0, 1
    while r1:
        q, r = pdivmod(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, s0 ^ clmul(q, s1)
    assert r0 == 1
    return pmod(s0, f)


class Ring:
    def __init__(self, name, q, add, mul):
        self.name, self.q = name, q
        self.els = range(q)
        self.add = [[add(a, b) for b in self.els] for a in self.els]
        self.mul = [[mul(a, b) for b in self.els] for a in self.els]


def zmod(n):
    return Ring(f"Z/{n}", n, lambda a, b: (a + b) % n,
                lambda a, b: a * b % n)


def f2quot(f, label):
    return Ring(label, 1 << pdeg(f), lambda a, b: a ^ b,
                lambda a, b: pmod(clmul(a, b), f))


def poly_function_span(R):
    """All polynomial functions R -> R, as tuples: the R-span of the
    power functions x^j, taken until the powers repeat."""
    powers, seen = [], set()
    cur = tuple(1 for _ in R.els)
    while cur not in seen:
        seen.add(cur)
        powers.append(cur)
        cur = tuple(R.mul[cur[a]][a] for a in R.els)
    span = {tuple(0 for _ in R.els)}
    for g in powers:
        mults = {tuple(R.mul[c][v] for v in g) for c in R.els}
        span = {tuple(R.add[s[a]][m[a]] for a in R.els)
                for s in span for m in mults}
    return span


# ------------------------------------------------------------ section L

CHANNEL_MAPS = {
    "Z/4": [lambda a: a % 2],
    "Z/8": [lambda a: a % 2],
    "F2[x]/(x(x+1))": [lambda a: pmod(a, 0b10), lambda a: pmod(a, 0b11)],
    "F2[x]/(x(x^2+x+1))": [lambda a: pmod(a, 0b10),
                           lambda a: pmod(a, 0b111)],
    "F2[x]/x^2": [lambda a: pmod(a, 0b10)],
    "F2[x]/x^3": [lambda a: pmod(a, 0b10)],
}

def lagrange_crt_lift(M, table):
    """Given a channel-local map on squarefree Z/M (as a table of
    values), build one polynomial with coefficients mod M by Lagrange
    on each channel and CRT glue per degree; return its coefficients."""
    ps = primes_of(M)
    deg = max(ps)
    coeffs_by_p = {}
    for p in ps:
        g = [table[x] % p for x in range(p)]      # the channel map
        c = [0] * p
        for a in range(p):
            if g[a] == 0:
                continue
            # basis polynomial prod_{b != a} (x - b)/(a - b) over F_p
            basis = [1]
            den = 1
            for b in range(p):
                if b == a:
                    continue
                basis = [((basis[i - 1] if i > 0 else 0)
                          - b * (basis[i] if i < len(basis) else 0)) % p
                         for i in range(len(basis) + 1)]
                den = den * (a - b) % p
            s = g[a] * pow(den, -1, p) % p
            for i, v in enumerate(basis):
                c[i] = (c[i] + s * v) % p
        coeffs_by_p[p] = c
    out = []
    for j in range(deg):
        # CRT: the coefficient mod M agreeing with each channel's
        val = 0
        for p in ps:
            cj = coeffs_by_p[p][j] if j < p else 0
            e = (M // p) * pow(M // p, -1, p)
            val = (val + cj * e) % M
        out.append(val)
    return out


def lift2(M, table2):
    """Two-variable version: the channel map of (x, y) is a Lagrange
    polynomial in x and y over F_p; glue per bidegree by the CRT."""
    ps = primes_of(M)
    deg = max(ps)
    coef = {}
    for p in ps:
        c = [[0] * p for _ in range(p)]
        inv = {}
        for a in range(p):
            basis, den = [1], 1
            for b in range(p):
                if b == a:
                    continue
                basis = [((basis[i - 1] if i > 0 else 0)
                          - b * (basis[i] if i < len(basis) else 0)) % p
                         for i in range(len(basis) + 1)]
                den = den * (a - b) % p
            inv[a] = [v * pow(den, -1, p) % p for v in basis]
        for a in range(p):
            for b in range(p):
                g = table2[(a, b)] % p
                if g == 0:
                    continue
                for i, u in enumerate(inv[a]):
                    for j, v in enumerate(inv[b]):
                        c[i][j] = (c[i][j] + g * u * v) % p
        coef[p] = c
    out = [[0] * deg for _ in range(deg)]
    for i in range(deg):
        for j in range(deg):
            val = 0
            for p in ps:
                cij = coef[p][i][j] if i < p and j < p else 0
                e = (M // p) * pow(M // p, -1, p)
                val = (val + cij * e) % M
            out[i][j] = val
    return out


def section_l():
    print("L  the locality criterion")
    # exhaustive at Z/6: all 6^6 maps
    local = poly = 0
    inside = True
    span = poly_function_span(zmod(6))
    for F in product(range(6), repeat=6):
        is_local = all(F[a] % p == F[a % p] % p
                       for p in (2, 3) for a in range(6))
        local += is_local
        poly += F in span
        inside &= is_local or F not in span
    check("Z/6: channel-local maps = polynomial maps, exhaustive",
          inside and local == poly == 108,
          f"{local} channel-local, {poly} polynomial of 46656")
    # counts elsewhere: channel-local by construction, polynomial by span
    cases = [
        (zmod(4), 2 ** 2 * 2 ** 4, 64),
        (zmod(8), 2 ** 2 * 4 ** 8, 1024),
        (f2quot(0b110, "F2[x]/(x(x+1))"), 2 ** 2 * 2 ** 2, 16),
        (f2quot(clmul(0b10, 0b111), "F2[x]/(x(x^2+x+1))"),
         2 ** 2 * 4 ** 4, 1024),
        (f2quot(0b100, "F2[x]/x^2"), 2 ** 2 * 2 ** 4, 64),
        (f2quot(0b1000, "F2[x]/x^3"), 2 ** 2 * 4 ** 8, 1024),
    ]
    for R, n_local, n_poly in cases:
        span = poly_function_span(R)
        # the channel of the value: the residue mod the one prime (Z/4,
        # Z/8, F_2[x]/x^k) or mod each factor; checked on the span
        chans = CHANNEL_MAPS[R.name]
        inside = all(all(ch(F[a]) == ch(F[b]) for ch in chans
                         for a in R.els for b in R.els if ch(a) == ch(b))
                     for F in span)
        check(f"{R.name}: {len(span)} polynomial of {n_local} channel-local"
              f" (counted by hand), each channel-local",
              len(span) == n_poly and inside)
    # constructive lift at Z/30, one and two variables
    rng = random.Random(30)
    ok = True
    for _ in range(100):
        chan = {p: [rng.randrange(p) for _ in range(p)] for p in (2, 3, 5)}
        table = []
        for x in range(30):
            v = sum(chan[p][x % p] * (30 // p) * pow(30 // p, -1, p)
                    for p in (2, 3, 5)) % 30
            table.append(v)
        c = lagrange_crt_lift(30, table)
        ok &= all(sum(cj * pow(x, j, 30) for j, cj in enumerate(c)) % 30
                  == table[x] for x in range(30))
    check("Z/30: 100 seeded channel-local maps lift to one polynomial", ok)
    ok = True
    for _ in range(20):
        chan = {p: {(a, b): rng.randrange(p) for a in range(p)
                    for b in range(p)} for p in (2, 3, 5)}
        table2 = {}
        for x in range(30):
            for y in range(30):
                table2[(x, y)] = sum(
                    chan[p][(x % p, y % p)] * (30 // p)
                    * pow(30 // p, -1, p) for p in (2, 3, 5)) % 30
        c = lift2(30, table2)
        ok &= all(sum(c[i][j] * pow(x, i, 30) * pow(y, j, 30)
                      for i in range(5) for j in range(5)) % 30
                  == table2[(x, y)] for x in range(30) for y in range(30))
    check("Z/30: 20 seeded two-variable channel-local maps lift", ok)


# ------------------------------------------------------------ section W

def section_w():
    print("W  the size wall")
    count = 0
    for M in range(4, 301):
        for p in primes_of(M):
            if p == M:
                continue
            count += 1
    # the witness b = p ceil(M/(2p)) lies in [M/2, M) for every p < M by
    # its own arithmetic (the proof's step), so it is not checked
    print(f"  the witness b at {count} (M, p) pairs, M <= 300: argued")
    rng = random.Random(7)
    ok = True
    for _ in range(30):
        perms = {p: rng.sample(range(p), p) for p in (2, 3, 5)}
        T = [sum(perms[p][x % p] * (30 // p) * pow(30 // p, -1, p)
                 for p in (2, 3, 5)) % 30 for x in range(30)]
        assert sorted(T) == list(range(30))
        sT = [int(2 * T[x] >= 30) for x in range(30)]
        ok &= all(any(sT[a] != sT[b] for a in range(30) for b in range(30)
                      if a % p == b % p) for p in (2, 3, 5))
    check("sign o T channel-local at no channel, 30 seeded bijections T", ok)


# ------------------------------------------------------------ section H

def section_h():
    print("H  the hiding lemma")
    ok, windows = True, 0
    for M in range(2, 241):
        for W in range(1, M):
            if M % W:
                continue
            c = M // W
            for r in range(W):
                high = sum(1 for j in range(c) if 2 * (r + j * W) >= M)
                want = c // 2 if c % 2 == 0 else (c - 1) // 2 + (2 * r >= W)
                ok &= high == want
            windows += 1
    check("sign bias exactly 0 (M/W even) or 1/2 (M/W odd, + iff "
          "r >= W/2), every fiber", ok, f"{windows} windows, M <= 240")
    ok, classes, empty = True, 0, 0
    for M in range(3, 61):
        for W in range(1, M):
            if M % W:
                continue
            c = M // W
            for bb in range(W):
                for gg in range(W):
                    Y = [bb + j * W for j in range(c)]
                    Z = [gg + j * W for j in range(c)]
                    seen = set()
                    for y in Y:
                        for z in Z:
                            if y != 0 and z != 0 and y != z:
                                seen.add(y < z)
                    classes += 1
                    if not seen:
                        empty += 1
                        ok &= c == 2 and bb == 0 and gg == 0
                    else:
                        ok &= seen == {True, False}
    check("orientation: both in every class with a distinct triple", ok,
          f"{classes} base-0 classes, M <= 60, {empty} without one")


# ------------------------------------------------------------ section C

def section_c():
    print("C  the half-coverage law")
    ok, n = True, 0
    for X in range(1, 241):
        for Q in range(1, X + 1):
            # a residue class with one lift in [1, X] determines it
            det = sum(1 for r in range(Q) if len(range(r or Q, X + 1, Q)) == 1)
            ok &= det == max(0, 2 * Q - X)
            n += 1
    check("determined singles = max(0, 2Q - X)", ok, f"{n} budgets")
    ok, n = True, 0
    for X in range(1, 121):
        for Q in range(1, X + 1):
            spans = {}
            for m in range(1, X + 1):
                lo, hi = spans.get(m % Q, (m, m))
                spans[m % Q] = (min(lo, m), max(hi, m))
            sp = list(spans.values())
            has = any(a[1] < b[0] or b[1] < a[0]
                      for i, a in enumerate(sp) for b in sp[i + 1:])
            ok &= has == (2 * Q - X >= 2)
            n += 1
    check("some pair is ordered with certainty iff 2Q - X >= 2", ok,
          f"{n} budgets")
    ok, n = True, 0
    for X in range(2, 121):
        for Q in range(1, X):
            if X % Q:
                continue
            fib = [[m for m in range(1, X + 1) if m % Q == r]
                   for r in range(Q)]
            right = 0
            for fa in fib:
                for fb in fib:
                    lt = sum(1 for a in fa for b in fb if a < b)
                    gt = sum(1 for a in fa for b in fb if a > b)
                    right += max(lt, gt)    # the better order of the
                    # two classes: residues ordered, 0 read as Q
            ok &= 2 * right == X * (X + Q - 2)
            n += 1
    check("best residue guess right on X(X + Q - 2)/2 pairs", ok,
          f"{n} divisor budgets, X <= 120")


# ------------------------------------------------------------ section R

def conj_closure(M, rel):
    ps = primes_of(M)
    proj = {p: {(x % p, y % p) for (x, y) in rel} for p in ps}
    return {(x, y) for x in range(M) for y in range(M)
            if all((x % p, y % p) in proj[p] for p in ps)}, proj


def rectangle_everywhere(M, rel):
    ps = primes_of(M)
    for p in ps:
        rows = {(x % p, y % p) for (x, y) in rel}
        cols = {(x % (M // p), y % (M // p)) for (x, y) in rel}
        rebuilt = {(x, y) for x in range(M) for y in range(M)
                   if (x % p, y % p) in rows
                   and (x % (M // p), y % (M // p)) in cols}
        if rebuilt != rel:
            return False
    return True


def section_r():
    print("R  the relational form")
    M = 210
    eq = {(x, x) for x in range(M)}
    div = {(x, x * z % M) for x in range(M) for z in range(M)}
    le = {(x, y) for x in range(M) for y in range(M) if x <= y}
    for name, rel, want in (("equality", eq, True),
                            ("divisibility", div, True),
                            ("order", le, False)):
        closure, proj = conj_closure(M, rel)
        check(f"Z/210 {name} conjunctive: {closure == rel}",
              (closure == rel) == want)
    closure, proj = conj_closure(M, le)
    check("order fails maximally: every projection is all of F_p x F_p",
          all(len(proj[p]) == p * p for p in primes_of(M))
          and len(closure) == M * M)
    for M in (6, 30):
        btw = {(a, b, c) for a in range(M) for b in range(M)
               for c in range(M)
               if len({a, b, c}) == 3 and (b - a) % M < (c - a) % M}
        proj = {p: {(a % p, b % p, c % p) for (a, b, c) in btw}
                for p in primes_of(M)}
        closure = {(a, b, c) for a in range(M) for b in range(M)
                   for c in range(M)
                   if all((a % p, b % p, c % p) in proj[p] for p in proj)}
        apart = [t for t in closure - btw if len(set(t)) == 3]
        check(f"Z/{M}: cyclic betweenness, ternary, is not conjunctive",
              (0, 1, 1) in closure and len(apart) == len(btw),
              f"{len(btw)} triples, closure {len(closure)}, (0, 1, 1) in "
              f"it, and {len(apart)} distinct triples of the other "
              f"orientation")
    M = 30
    rels = {"equality": {(x, x) for x in range(M)},
            "divisibility": {(x, x * z % M) for x in range(M)
                             for z in range(M)},
            "order": {(x, y) for x in range(M) for y in range(M) if x <= y}}
    ok = all(rectangle_everywhere(M, r) == (conj_closure(M, r)[0] == r)
             for r in rels.values())
    check("Z/30: conjunctive iff a rectangle at every one-channel split",
          ok)


# ------------------------------------------------------------ section D

def comparator(ms):
    M = prod(ms)
    S = sum(M // m for m in ms)
    return M, S


def D_direct(x, ms):
    return sum(x // m for m in ms)


def D_dot(x, ms, M, S):
    Minv = pow(M, -1, S)
    return (-Minv * sum((M // m) * (x % m) for m in ms)) % S


def D_table(ms, M):
    return [sum(x // m for m in ms) for x in range(M)]


def runs(Dv):
    """The runs of constant D, as (start, length)."""
    out, start = [], 0
    for x in range(1, len(Dv) + 1):
        if x == len(Dv) or Dv[x] != Dv[x - 1]:
            out.append((start, x - start))
            start = x
    return out


def section_d():
    print("D  the exact comparator")
    rng = random.Random(510510)
    ok = True
    for _ in range(300):
        ms, size = [], rng.randrange(2, 7)
        while len(ms) < size:
            m = rng.randrange(2, 400)
            if all(gcd(m, o) == 1 for o in ms):
                ms.append(m)
        M, S = comparator(ms)
        ok &= gcd(M, S) == 1
    check("gcd(M, S) = 1 on 300 seeded pairwise coprime sets", ok)
    sets = [(2, 3, 5, 7, 11, 13, 17), (3, 5, 17, 257), (97, 101, 103),
            (15, 77, 221)]
    for ms in sets:
        M, S = comparator(ms)
        rng2 = random.Random(M)
        xs = [rng2.randrange(M) for _ in range(2000)]
        ok_dot = all(D_dot(x, ms, M, S) == D_direct(x, ms) for x in xs)
        longest = max(length for _, length in runs(D_table(ms, M)))
        check(f"{set(ms)}: D by one dot product mod S (2000 seeded x)",
              ok_dot, f"M = {M}, longest run of constant D {longest} "
              f"(m_1 by D's definition)")
    M = 510510
    ms = sets[0]
    Dv = D_table(ms, M)
    ties = sum(1 for x in range(1, M) if Dv[x] == Dv[x - 1])
    check("Z/510510: D alone ties exactly phi(M) adjacent pairs",
          ties == phi(M), f"{ties} ties, phi = {phi(M)}")
    ms = sets[3]
    M = 15 * 77 * 221
    Dv = D_table(ms, M)
    ties = sum(1 for x in range(1, M) if Dv[x] == Dv[x - 1])
    want = M
    for m in ms:
        want = want // m * (m - 1)
    check("{15, 77, 221}: D ties exactly M prod (1 - 1/m_i) adjacent "
          "pairs", ties == want, f"{ties} ties, phi = {phi(M)}")
    ms, M = (2, 3, 5, 7), 210
    Dv = [D_direct(x, ms) for x in range(M)]
    K = [(Dv[x], x % 2) for x in range(M)]
    half = -(-M // 2)
    ok = all((K[x] >= K[half]) == (2 * x >= M) for x in range(M))
    ok &= all((K[(x + y) % M] < K[x]) == (x + y >= M)
              for x in range(M) for y in range(M))
    check("Z/210: sign and overflow each one key compare, exhaustive", ok)


# ------------------------------------------------------------ section K

def rung_primes(k):
    out, n = [], 2
    while len(out) < k:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def section_k():
    print("K  the cost law")
    sums = [sum(Fraction(1, p) for p in rung_primes(k)) for k in range(1, 11)]
    check("rungs: sum 1/p < 1 exactly at k = 1, 2",
          [s < 1 for s in sums] == [True, True] + [False] * 8,
          f"k = 3 gives {sums[2]}")
    for k in (2, 3, 7):
        M, S = comparator(rung_primes(k))
        print(f"  rung k = {k}: S/M = sum 1/p = {float(S / M):.4f}")
    fermat = [2 ** (2 ** n) + 1 for n in range(8)]
    ok = all(gcd(a, b) == 1 for i, a in enumerate(fermat)
             for b in fermat[i + 1:])
    total = sum(Fraction(1, F) for F in fermat)
    tail = Fraction(2, 2 ** (2 ** 8))    # sum over n >= 8 of 1/F_n
    check("Fermat numbers pairwise coprime, sum 1/F_n < 0.5961",
          ok and total + tail < Fraction(5961, 10000),
          f"sum to F_7 = {float(total):.7f}")
    for bits in (16, 32):
        ps, n = [], 2 ** bits - 1
        while len(ps) < 8:
            n -= 2
            if is_probable_prime(n):
                ps.append(n)
        M, S = comparator(ps)
        check(f"8 primes below 2^{bits}: S narrower than M",
              S < M, f"log2 M = {M.bit_length()}, log2 S = "
              f"{S.bit_length()}")


def is_probable_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


# ------------------------------------------------------------ section Q

def quotient_dot(ms, j):
    """floor(x/m_j) for every x in [0, M), each read off the residues
    by one dot product modulo M/m_j."""
    M = prod(ms)
    mj, R = ms[j], M // ms[j]
    others = [m for i, m in enumerate(ms) if i != j]
    crt = [(R // m) * pow(R // m, -1, m) for m in others]
    inv = pow(mj, -1, R) if R > 1 else 0
    out = []
    for x in range(M):
        y = sum((x % m) * c for m, c in zip(others, crt))
        out.append((y - x % mj) * inv % R)
    return out


def least_key(residues, ms):
    """(floor(x/m_k), x mod m_k) for the x in [0, M) with the given
    residues mod the pairwise coprime ms, m_k the largest modulus: the
    least exact key, read off the residues alone."""
    if len(residues) != len(ms):
        raise ValueError("one residue per modulus")
    k = max(range(len(ms)), key=lambda i: ms[i])
    mk, R = ms[k], prod(ms) // ms[k]
    rk = residues[k] % mk
    if R == 1:
        return 0, rk
    y = sum((r % m) * (R // m) * pow(R // m, -1, m)
            for i, (r, m) in enumerate(zip(residues, ms)) if i != k)
    return (y - rk) * pow(mk, -1, R) % R, rk


def compare(a, b, ms):
    """-1, 0 or 1 as the integers named by residue words a and b
    compare, each read through its least key."""
    ka, kb = least_key(a, ms), least_key(b, ms)
    return (ka > kb) - (ka < kb)


def section_q():
    print("Q  the least comparator")
    for ms in ((2, 3, 5, 7, 11, 13, 17), (3, 5, 17, 257), (97, 101, 103),
               (15, 77, 221)):
        M, S = comparator(ms)
        k = len(ms) - 1
        q = quotient_dot(ms, k)
        ok = all(q[x] == x // ms[k] for x in range(M))
        check(f"{set(ms)}: floor(x/m_k) by one dot product mod M/m_k",
              ok and M // ms[k] < S,
              f"range M/m_k = {M // ms[k]} against S = {S}")
    for ms in ((2, 3, 5, 7, 11, 13, 17), (3, 5, 17, 257), (97, 101, 103),
               (15, 77, 221)):
        M, mk = prod(ms), max(ms)
        rng = random.Random(M + 1)
        corners = [0, 1, mk - 1, mk, M - 2, M - 1]
        pairs = [(rng.randrange(M), rng.randrange(M)) for _ in range(2000)]
        pairs += [(x, y) for x in corners for y in corners]
        rev = ms[::-1]
        ok, n = True, 0
        for x, y in pairs:
            for order in (ms, rev):
                a = tuple(x % m for m in order)
                b = tuple(y % m for m in order)
                q, r = least_key(a, order)
                ok &= compare(a, b, order) == (x > y) - (x < y)
                ok &= mk * q + r == x
                n += 1
        check(f"{set(ms)}: compare and least_key on residue words",
              ok, f"{n // 2} pairs, each in both modulus orders")


# ------------------------------------------------------------ section F

def section_f():
    print("F  the F_2[x] control")
    factors = [0b10, 0b11, 0b111, 0b1011, 0b1101]  # x, x+1, x^2+x+1, ...
    f = 1
    for g in factors:
        f = clmul(f, g)
    n = pdeg(f)
    # degree at most 3: irreducible iff no root, at 0 or at 1
    irred = all(pdeg(g) == 1 or (g & 1 and bin(g).count("1") % 2)
                for g in factors)
    check("f has degree 10 and five distinct irreducible factors",
          n == 10 and len(set(factors)) == 5 and irred)
    ok, windows = True, 0
    for mask in range(31):                       # proper divisors g | f
        g = 1
        for i, h in enumerate(factors):
            if mask >> i & 1:
                g = clmul(g, h)
        free = n - pdeg(g)
        for r in range(1 << pdeg(g)):
            top = sum(1 for P in range(1 << free)
                      if pdeg(r ^ clmul(g, P)) == n - 1)
            ok &= 2 * top == 1 << free
        windows += 1
    check("top bit exactly balanced in every fiber of every proper window",
          ok, f"{windows} windows; over Z the bias is 1/2 at odd M/W")
    ok = all(pdeg(clmul(a, b)) == pdeg(a) + pdeg(b)
             for a in range(1, 256) for b in range(1, 256))
    check("deg(ab) = deg a + deg b for every nonzero a, b < 256", ok)
    us = [pinv(pmod(pdivmod(f, g)[0], g), g) for g in factors]
    ok, flagged = True, {}
    for a in range(1 << n):
        bs = [pmod(clmul(a, u), g) for u, g in zip(us, factors)]
        whole = 0
        for b, g, in zip(bs, factors):
            whole ^= clmul(b, pdivmod(f, g)[0])
        ok &= pmod(whole, f) == a
        for t in range(1, n + 1):
            lead = 0
            for b, g in zip(bs, factors):
                lead ^= pdivmod(b << t, g)[0]
            ok &= lead == pdivmod(a << t, f)[0]
            if lead:
                ok &= pdeg(lead) - t + n == pdeg(a)
            else:
                ok &= a == 0 or pdeg(a) < n - t
                flagged[t] = flagged.get(t, 0) + 1
    check("partial fractions: t leading coefficients exact or zero",
          ok and all(flagged[t] == 2 ** (n - t) for t in range(1, n + 1)),
          f"flagged {[flagged[t] for t in range(1, n + 1)]}")
    ms = (2, 3, 5, 7, 11, 13, 17)
    M = prod(ms)
    t = 16
    w = {m: pow(M // m, -1, m) for m in ms}
    witness = None
    for x in range(1, 1001):
        est = sum(((x % m) * w[m] % m) * (1 << t) // m for m in ms)
        est %= 1 << t
        if 2 * est >= 1 << t:                   # read as x >= M/2
            witness = x
            break
    check("Z at Z/510510: a 16-bit truncation reads a small x as large",
          witness is not None, f"first witness x = {witness}")
    # F_3[x]: polynomials as coefficient tuples, low degree first
    def trim3(a):
        a = [c % 3 for c in a]
        while a and a[-1] == 0:
            a.pop()
        return tuple(a)

    def add3(a, b):
        n = max(len(a), len(b))
        return trim3([(a[i] if i < len(a) else 0)
                      + (b[i] if i < len(b) else 0) for i in range(n)])

    def mul3(a, b):
        if not a or not b:
            return ()
        r = [0] * (len(a) + len(b) - 1)
        for i, u in enumerate(a):
            for j, v in enumerate(b):
                r[i + j] += u * v
        return trim3(r)

    def below3(d):
        return [trim3(c) for c in product(range(3), repeat=d)]

    facs3 = [(0, 1), (1, 1), (1, 0, 1), (2, 1, 1)]
    f3 = (1,)
    for h in facs3:
        f3 = mul3(f3, h)
    n3 = len(f3) - 1
    ok, windows = True, 0
    for mask in range(2 ** len(facs3) - 1):
        g = (1,)
        for i, h in enumerate(facs3):
            if mask >> i & 1:
                g = mul3(g, h)
        dg = len(g) - 1
        profiles = set()
        for r in below3(dg):
            prof = [0] * (n3 + 1)
            for P in below3(n3 - dg):
                d = len(add3(r, mul3(g, P))) - 1
                if d >= dg:
                    prof[d] += 1
            profiles.add(tuple(prof))
        ok &= len(profiles) == 1
        windows += 1
    check("F_3[x]: every fiber of a proper window has one degree profile",
          ok, f"{windows} windows at degree {n3}")


def labellings(N, s):
    """Every add-updatable labelling on [0, N) with at most s labels,
    labels in first-occurrence order; A is filled in as the search
    goes, keyed by the unordered pair of labels."""
    out, mu, A = [], [0], {(0, 0): 0}

    def rec(n, used):
        if n == N:
            out.append(tuple(mu))
            return
        for c in range(min(used + 1, s)):
            new, ok = {}, True
            for x in range(n // 2 + 1):
                y = n - x
                a, b = mu[x], (c if y == n else mu[y])
                key = (min(a, b), max(a, b))
                have = A.get(key, new.get(key))
                if have is None:
                    new[key] = c
                elif have != c:
                    ok = False
                    break
            if ok:
                A.update(new)
                mu.append(c)
                rec(n + 1, max(used, c + 1))
                mu.pop()
                for key in new:
                    del A[key]

    rec(1, 1)
    return out


def rho(mu):
    first = {}
    for x, a in enumerate(mu):
        if a in first:
            return first[a], x - first[a]
        first[a] = x
    return len(mu), None


def section_controls():
    print("controls")
    fam = set(labellings(8, 3))
    check("control: the search finds x mod 3 and rejects [x >= 3]",
          tuple(x % 3 for x in range(8)) in fam and
          tuple(int(x >= 3) for x in range(8)) not in fam)
    ms = (2, 3, 5)
    wrong = sum(compare(tuple(x % m for m in ms[::-1]),
                        tuple(y % m for m in ms[::-1]), ms)
                != (x > y) - (x < y) for x in range(30) for y in range(30))
    check("control: words read against the wrong modulus order "
          "mis-compare", wrong > 0, f"{wrong} of 900 pairs at Z/30")
    check("control: one modulus keys every word by its residue",
          compare((0,), (0,), (7,)) == 0 and least_key((3,), (7,)) == (0, 3))


def section_a():
    print("A  the additive labelling")
    bad = total = 0
    worst = {}
    for N in (8, 10, 12, 14):
        for s in (2, 3, 4, 5):
            fam = labellings(N, s)
            total += len(fam)
            bad += len(fam) != s * (s + 1) // 2
            for mu in fam:
                x0, d = rho(mu)
                shape = d is not None and x0 + d <= s and all(
                    mu[x] == mu[x + d] for x in range(x0, N - d))
                B, mul = {}, True
                for x in range(N):
                    for y in range(x, N):
                        if x * y < N:
                            key = (min(mu[x], mu[y]), max(mu[x], mu[y]))
                            if B.setdefault(key, mu[x * y]) != mu[x * y]:
                                mul = False
                vals = {}
                for x, a in enumerate(mu):
                    vals.setdefault(a, []).append(x)
                inf = [(a, b) for a in vals for b in vals
                       if max(vals[a]) < min(vals[b])]
                h = max((min(vals[b]) for a, b in inf), default=0)
                worst[(N, s)] = max(worst.get((N, s), 0), h)
                blind = all(
                    not (max(vals[mu[u]]) < min(vals[mu[v]]))
                    for u in range(s, N) for v in range(u + 1, N))
                bad += not (shape and mul and blind)
            bad += worst[(N, s)] != s - 1
    check("every add-updatable labelling is a rho, mul-updatable, and "
          "blind at and above s; s(s+1)/2 of them per cell", bad == 0,
          f"{total} labellings over 16 cells, largest least value of an "
          f"informative label s - 1 at every cell, {bad} faults")


def main():
    section_controls()
    if not all(CHECKS):
        print("\nCONTROL FAILED: nothing below is read.")
        raise SystemExit(1)
    section_a()
    section_l()
    section_w()
    section_h()
    section_c()
    section_r()
    section_d()
    section_k()
    section_q()
    section_f()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
