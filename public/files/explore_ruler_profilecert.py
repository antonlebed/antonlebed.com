"""explore_ruler_profilecert.py -- IS THE CERTIFICATE'S SIZE PROFILE
EVENTUALLY CONSTANT IN n, AND FROM WHERE? The exact-fill certificate at
walk cell W-n (fifteen atoms, three labels, theta = (n - 1)/n) carries
a size profile s(n) that explore_ruler_gaplaw.py read constant at
111112222233333 from n = 2000 to n = 100000 and left unproved past it.
This rig turns that observation into a theorem with a certified
threshold: the certificate is a finite computation tree whose every
branch is the sign of a polynomial in theta with integer coefficients,
so its output is a step function of theta with finitely many steps,
and the last step is found by isolating the roots of the tests the
tree takes.

(The cell, the certificate's size vector and the anchored-gap
machinery are IMPORTED from explore_ruler_setvalued.py,
explore_ruler_boundedgap.py and explore_ruler_gaplaw.py. New here is
the polynomial transcription of the certificate, the root isolation,
and the threshold.)

THE OBJECT, in its own vocabulary. The walk cell reads the ring
Z/105 through the residue window mod 15 (fifteen ATOMS r) into three
magnitude LABELS y = floor(x/35), under the geometric law P(x) ~
theta^x. Every atom's fiber is seven residues r + 15j, j < 7, and its
posterior over labels is a block read of the fiber: with q = theta^15
the mass of label y at atom r is (q^lo - q^hi)/(1 - q^7) over the
fiber block [lo, hi) the label owns. The blocks are fixed by the
window and never move with theta: atoms 0..4 carry (3, 2, 2) residues
per label, atoms 5..9 carry (2, 3, 2) and atoms 10..14 carry (2, 2, 3),
so the 45 posteriors take SEVEN distinct values, each a polynomial in
q over the common denominator 1 - q^7:

    three-residue blocks   1 - q^3,  q^2 - q^5,  q^4 - q^7
    two-residue blocks     1 - q^2,  q^2 - q^4,  q^3 - q^5,  q^5 - q^7

(1 - q^2 is shared by atoms 5..9 and 10..14). The atom masses are
theta^r (1 - q^7)/((1 - q) D) with D = (1 - theta^105)/(1 - theta).

THE CERTIFICATE'S TREE, read from cert_sizes. (i) The OPERATIVE LEVEL
is the largest posterior value t whose above-or-equal set covers
1 - alpha = 7/10 of the mass. (ii) Every pair strictly above t is in
the certificate; s_r counts them. (iii) The pairs whose value IS t
form the TIED BLOCK, and a min-cost subset sum picks the cheapest
sub-block whose mass closes the coverage shortfall; its members raise
s_r by one. The integerize scale (one common denominator of every
Fraction in the cell) multiplies every cost, coverage and target alike
and cancels from every comparison, so the profile is a function of
theta alone.

THE HAND ATTACK, worked on paper before any engine code.

FIRST, EVERY BRANCH IS A POLYNOMIAL SIGN. A posterior-against-posterior
test is the sign of a difference of two of the seven numerators. A
coverage test cov(t) >= 7/10 is, after clearing the positive
denominator D (1 - q^7), the sign of 10 sum_{(r,y) >= t} theta^r S_7
(q^lo - q^hi) - 7 D (1 - q^7), S_7 = 1 + q + ... + q^6. A fill test
sum_S cost >= need is, after the same clearing, the sign of
t_num sum_S theta^r S_7 - [7/10 D (1 - q^7) - sum_above theta^r S_7
(q^lo - q^hi)] times 10. Subset-against-subset is S_7 times a
difference of theta-monomial sums. Every denominator cleared is
positive on (0, 1). So the tree's path on any interval where every
test polynomial keeps its sign is constant, and the profile with it:
that is the abstract half, and it is a page.

SECOND, WHAT THE FAR PROFILE SAYS THE TREE DID. As theta -> 1 with
eps = 1 - q the three-residue values are 3 eps and the two-residue
values 2 eps to first order, and within each family the order is
fixed on all of (0, 1) by a monomial factor: 1 - q^3 > q^2 - q^5 >
q^4 - q^7 and 1 - q^2 > q^2 - q^4 > q^3 - q^5 > q^5 - q^7. The far
profile 111112222233333 reads: atoms 0..4 keep one pair, atoms 5..9
two, atoms 10..14 three, so the pairs in are exactly the values
{1 - q^3, q^2 - q^5, q^4 - q^7, 1 - q^2, q^2 - q^4}, the level is the
least of them, q^2 - q^4 = q^2 (1 - q^2), and the tied block is the
five class-1 pairs of atoms 10..14, all five taken by the fill. The
coverage check at the limit: without the tied block 13/21 < 7/10,
with it 15/21 >= 7/10; each tied item is worth about 2/105, the
shortfall about 0.081, so 4.25 items are needed and all five go in.
The record says the 3s "invade the tail" as n grows, which in this
vocabulary is the fill taking a fifth item from atom 10, the dearest
of the tied five, once four no longer close the shortfall: the
deciding root is a FILL test, not a level crossing.

THIRD, THE CROSS-FAMILY CROSSINGS. 1 - q^2 against q^2 - q^5 differs
by 1 - 2 q^2 + q^5 = (1 - q)(1 + q - q^2 - q^3 - q^4), one root near
q = 0.75, theta near 0.981, n near 52: the walk's small rungs cross
posterior orderings, the far rungs do not.

FOURTH, THE GAP ON THE FIXED BOX. Once s is constant the anchored box
c_r in [s_r - 3, s_r] is fixed, so the flattening spectrum A_J of
explore_ruler_gaplaw.py is n-free: A_4 = 18 attained by the vector of
(x - 1)(x^2 - 1)(x^3 - 1)^2 and no admissible flattening 5, 6 or 7.
With the moment identity P(theta) = sum_j m_j (-1/n)^j and
|m_j| <= B_j = sum_r C(r, j) max(|s_r - 3|, |s_r|), a flattening-4
vector has |P| >= n^-4 (18 - T_4(n)), T_4 = sum_{j >= 5} B_j n^(4-j),
and a flattening-J vector with J <= 3 has |P| >= n^-J (1 - T_J(n)).
Past the least n_0 where every J <= 3 floor clears the J = 4 ceiling
18 + T_4, the gap in value units is 18 n^-4 (1 + eps) with
|eps| <= T_4(n)/18: a theorem on [max(N, n_0), infinity). B_5 is
about 3 C(15, 6) = 15015, so n_0 is of order 10^4 by this crude
tail, and the rungs between N and n_0 are prints.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. THE TRANSCRIPTION. Every test the far path takes clears to a
      polynomial in theta with integer coefficients (the code raises
      on anything else); the far level is q^2 - q^4 and the tied block
      is the five class-1 pairs of atoms 10..14, all taken.
  P2. THE THRESHOLD LANDS IN (1000, 2000]: the largest root in (0, 1)
      over every test polynomial sits at theta between the 1000 and
      2000 rungs, so N is certified below 2000 and the observed
      constancy from 2000 was the theorem's own edge.
  P3. THE DECIDING TEST IS A FILL TEST: the polynomial carrying the
      largest root is a four-item-against-need test of the tied
      block, not a posterior ordering or a coverage test.
  P4. THE ROOTS READ THE LADDER: some test polynomial has a root with
      n = 1/(1 - theta) in (150, 175], where the record's profile
      reaches ...333, and the fill tests' roots enumerate the record's
      "sliding" rungs.
  P5. THE FIXED-BOX GAP. On the box of s(N): A_4 = 18, A_5 = A_6 =
      None, no flattening 7; n_0 is of order 10^4; the ladder rungs
      at n >= max(N, n_0) print g_A n^4 in value units inside
      18 (1 +- T_4/18).

KILLS, as observables rather than inferences.
  K-A. The transcription raises: a branch of cert_sizes whose test
       is not a polynomial sign (then the abstract half is wrong as
       stated).
  K-B. A test polynomial with a root at theta >= theta_100000 (then
       N exceeds the observed range and the four decades were an
       accident of the ladder; the theorem stands with that N).
  K-C. Parity: the transcribed profile differs from cert_sizes at any
       rung of the ladder.
  K-D. The root counter fails its control: reports 0 on a polynomial
       with a planted root in the interval, or a root on a
       root-free one.

CONTROLS, run and read BEFORE any verdict.
  C1 (REPRODUCTION). At every rung of explore_ruler_gaplaw.py's
     ladder, the transcribed tree evaluated at theta_n prints the
     same size profile as the imported cert_sizes.
  C2 (ROOT COUNTER, POSITIVE). A polynomial with a planted root at
     the midpoint of [theta_N, 1) counts one root there and the
     bisection brackets it; 1 + theta^2 counts zero; and a planted
     pair of roots inside the interval counts two.
  C3 (DEFLATION). Every test polynomial's multiplicity at theta = 1
     is printed and the deflated polynomial is nonzero at 1.

THE ARMS.
  1. The transcription at theta_100000: the path taken, every test as
     (label, degree, multiplicity at 1, largest root in (0, 1) read
     as n), the resulting profile, and the least certified N: the
     least integer n with theta_n above every root, checked exactly
     at n and at n - 1.
  2. The ladder reproduction (C1) and the profiles at N - 1 and N.
  3. The fixed-box gap: the spectrum on the box of s(N), the tail
     constants B_j, n_0, and the value-unit g_A n^4 at every ladder
     rung with its band.

RESOURCE NOTE. Exact integer and Fraction arithmetic, no numpy. The
polynomials have degree at most about 210; Descartes' rule on the
Moebius-transformed polynomial bounds the root count on an interval
and bisection makes it exact, all in Fractions. The spectrum's
meet-in-the-middle on the anchored box is the gap-law rig's arm 4,
seconds. Estimate: under a minute, well under 512 MB.

RUN RECORD (final run: wall 52.0 s, peak working set 56.4 MB under
memwatch at the 512 MB default). The first draft's Descartes bound ran
in Fractions at 0.7 s a call and the bisection made the rig a
runaway, killed at ten times its estimate; the bound was rewritten in
integers (fifty times faster) and a list-concatenation bug in S_7's
construction, found by the same timing pass, was fixed before any
verdict was read. C2: the planted root counts one and its bracket
holds it, 1 + x^2 counts zero, the planted pair counts two. C1: the
transcribed tree and cert_sizes print the same profile at all 19
rungs (the ladder plus n = 1450 and 1451). C3: every deflated test is
nonzero at 1. K-A, K-B, K-C, K-D fired nowhere.

P1 HOLDS. The far path takes 49 tests, every one an integer
polynomial of degree 45 to 209 with multiplicity 1 or 2 at theta = 1:
5 coverage tests (the four values above the level and the level),
6 value-against-level tests, 6 orderings among the four values above
the level, and 32 fill tests -- the five-item block feasible, every
one of its 31 proper sub-blocks infeasible.
The level is q^2 - q^4, the tied block the five class-1 pairs of atoms
10..14, and the fill takes all five.

P2 HOLDS AND THE THRESHOLD IS SHARP. The largest root over every test
sits at theta in (0.999310491, 0.999310492], n in (1450.3067,
1450.3087]; every test is root-free on [theta_1451, 1), so s(n) =
111112222233333 for all n >= 1451, and cert_sizes at n = 1450 prints
111112222233332: the threshold is exact, not merely certified.

P3 HOLDS, AND THE HAND ATTACK NAMED THE WRONG ATOM. The deciding
polynomial is the fill test "the four-item block {10, 11, 12, 13} <
need", degree 209; the five four-item sub-blocks carry the five
largest roots, n = 1434.30 to 1450.31, and the block of atoms 10..13
-- the HEAVIEST four, since cost and mass are the same number w_r
here -- is the last to lose feasibility as n rises. So at n = 1450
the fill is that block and the atom left out is 14, the lightest
(cert_sizes prints ...33332), not atom 10 as the hand attack's SECOND
paragraph guessed: the fill drops the cheapest item, and the cheapest
is the lightest.

P4 HOLDS AND THE ROOTS ARE THE LADDER'S JUMPS. The fill tests' roots
come in five bands, one per sub-block size: the one-item blocks at
n = 111.8 to 113.0, two-item at 159.9 to 162.5, three-item at 286.5 to
291.3, four-item at 1434.3 to 1450.3, and the empty block at 86.8 --
the rungs where the record's profile gains its next 3 (n = 100..110
carry one, 125..150 two, 175..200 three, 400..1000 four, 1451 on
five). Two posterior orderings cross inside the walk: q^4 - q^7
against 1 - q^2 at n = 166.28, and q^4 - q^7 against the level
(the same polynomial as q^2 - q^5 against 1 - q^2, both q^2 times
2 q^2 - q^5 - 1) at n = 91.72; the coverage tests at the three
three-residue values have their roots at n = 4.95, and the empty
fill's polynomial is the coverage test at 1 - q^2. Every within-family
ordering and the coverage test at the level itself are root-free on
(0, 1).

P5 HOLDS, AND THE EXACT TAIL CLOSES THE GAP LAW DOWN TO N. On the
fixed box A_4 = 18, A_5 = A_6 = None, no flattening 7; the box-only
tail constants (B_5 = 14805) give n_0 = 8779. An arm added after the
first run replaced them by exact per-flattening extremes from the
same meet-in-the-middle join (the box is 4^15, so seconds): the least
|m_J| over vectors of flattening exactly J is 1, 1, 1, 2, 18 for
J = 0..4, and m_{J+1} over them ranges in [-55, 260], [-100, 875],
[-130, 600], [-96, 279], [63, 72]. With these n_0 = 880 < 1451, so
the value-unit anchored gap is 18 n^-4 (1 + eps) with |eps| <=
(72/n + sum_{j >= 6} B_j n^(4-j))/18 for every n >= 1451, a theorem
on the profile's own range; the four rungs from 2000 print inside
the band (17.96852 in [17.95920, 18.04080] at n = 2000; 17.99937 in
[17.99928, 18.00072] at n = 100000). The argmin at n = 100000 is the
coefficient vector of (x - 1)(x^2 - 1)(x^3 - 1)^2 placed on atoms
1..10, m_4 = 18, m_5 = 63, the least m_5 a flattening-4 vector of the
box carries.

WHAT THIS SETTLES AND WHAT IT LEAVES. The open sentence -- the size
profile is constant "observed across four decades, not proved" --
closes as a theorem with a sharp threshold: constant on all of
n >= 1451, changing at 1450, by a certificate whose every step is
exact, and the gap law 18 n^-4 (1 + eps) with an explicit eps holds
on the same range. The method is general: any instrument whose output
is the path of a finite computation tree branching on signs of
polynomials in a parameter is eventually constant in that parameter,
and the threshold is a root isolation over the tests the far path
takes. Left open: the Diophantine regime n <= 50, where the profile
changes at every rung read, is still priced only by the box scan.
"""

import os
import sys
import time
from fractions import Fraction
from itertools import combinations, product as iproduct
from math import comb

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_exchange import ALPHA  # noqa: E402
from explore_ruler_optimum import integerize  # noqa: E402
from explore_ruler_boundedgap import anchored_gap_mim, cert_sizes  # noqa: E402
from explore_ruler_gaplaw import (  # noqa: E402
    anchored_argmin, deepest_flattening_15, flattening, moments, walk_cell,
)

F = Fraction

M = 15
K = 3
NPRIMES = 105
FAR = 100000
LADDER = (3, 5, 10, 25, 50, 100, 110, 125, 150, 175, 200, 400, 1000,
          2000, 5000, 20000, 100000)


# ------------------------------------------------------- polynomials
# A polynomial in theta is a list of Fraction coefficients, low first.

def p_add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(n)]


def p_sub(a, b):
    return p_add(a, [-x for x in b])


def p_scale(a, s):
    return [x * s for x in a]


def p_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def p_mono(e, c=1):
    out = [F(0)] * (e + 1)
    out[e] = F(c)
    return out


def p_trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def p_eval(a, x):
    acc = F(0)
    for c in reversed(a):
        acc = acc * x + c
    return acc


def p_int(a):
    """Clear denominators: the same sign everywhere, integer
    coefficients, content removed."""
    a = p_trim(a)
    if not a:
        return []
    den = 1
    for c in a:
        den = den * c.denominator // _gcd(den, c.denominator)
    ints = [int(c * den) for c in a]
    g = 0
    for c in ints:
        g = _gcd(g, abs(c))
    return [c // g for c in ints]


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def p_divide_x_minus_1(a):
    """Exact quotient of a by (x - 1); the caller checks a(1) = 0."""
    n = len(a) - 1
    q = [0] * n
    carry = 0
    for i in range(n, 0, -1):
        carry = a[i] + carry
        q[i - 1] = carry
    assert a[0] + carry == 0
    return q


def p_deflate_at_1(a):
    """(quotient with the root 1 removed, its multiplicity)."""
    a = p_trim(a)
    m = 0
    while a and p_eval(a, 1) == 0:
        a = p_trim(p_divide_x_minus_1(a))
        m += 1
    return a, m


# ------------------------------------------------ root counting
# Descartes' rule on the Moebius image of [a, b]: the number of sign
# variations bounds the count of roots in (a, b) from above and has
# its parity; bisection to brackets of 0 or 1 variations makes the
# count exact (Vincent / Collins-Akritas).

def _variations(coeffs):
    v = 0
    last = 0
    for c in coeffs:
        if c == 0:
            continue
        s = 1 if c > 0 else -1
        if last and s != last:
            v += 1
        last = s
    return v


def descartes_bound(p, a, b):
    """Sign variations of (1 + x)^d p((a + b x)/(1 + x)) -- an upper
    bound, with the right parity, on the roots of p in (a, b)."""
    p = p_int(p)
    d = len(p) - 1
    # integers throughout: a = A/Q, b = B/Q, and Q^d p((A + (B - A) t)/Q)
    # = sum_i c_i Q^(d-i) (A + W t)^i, W = B - A -- the same signs
    Q = a.denominator * b.denominator // _gcd(a.denominator, b.denominator)
    A = a.numerator * (Q // a.denominator)
    B = b.numerator * (Q // b.denominator)
    W = B - A
    apow = [1]
    wpow = [1]
    for _ in range(d):
        apow.append(apow[-1] * A)
        wpow.append(wpow[-1] * W)
    r = [0] * (d + 1)
    for i, c in enumerate(p):
        if c == 0:
            continue
        cq = c * Q ** (d - i)
        for j in range(i + 1):
            r[j] += cq * comb(i, j) * apow[i - j] * wpow[j]
    # (1 + x)^d r(1/(1 + x)) = sum_i r_i (1 + x)^(d - i)
    out = [0] * (d + 1)
    for i, c in enumerate(r):
        if c == 0:
            continue
        e = d - i
        for j in range(e + 1):
            out[j] += c * comb(e, j)
    return _variations(out)


def count_roots(p, a, b, depth=0):
    """Exact number of distinct roots of p in the OPEN interval (a, b),
    p nonzero at both ends."""
    assert p_eval(p, a) != 0 and p_eval(p, b) != 0
    v = descartes_bound(p, a, b)
    if v <= 1:
        return v
    mid = (a + b) / 2
    if p_eval(p, mid) == 0:
        # a root at the midpoint: split around it
        return 1 + count_roots(p, a, mid, depth + 1) \
            + count_roots(p, mid, b, depth + 1)
    return count_roots(p, a, mid, depth + 1) + count_roots(p, mid, b, depth + 1)


def largest_root_below(p, lo, hi, width):
    """A bracket (l, h] with h - l <= width around the largest root of p
    in (lo, hi), or None if p has none there. p nonzero at lo, hi."""
    if count_roots(p, lo, hi) == 0:
        return None
    while hi - lo > width:
        mid = (lo + hi) / 2
        if p_eval(p, mid) == 0:
            mid = mid + (hi - mid) / 3  # step off an exact root
        if count_roots(p, mid, hi) > 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


# ------------------------------------------- the cell as polynomials

def theta_of(n):
    return F(n - 1, n)


class CellPolys(object):
    """The walk cell's masses and posteriors as polynomials in theta,
    every denominator cleared by a factor positive on (0, 1)."""

    def __init__(self):
        cell = walk_cell(FAR)
        self.blocks = [cell.blocks(r) for r in range(M)]
        q = 15
        # S_7 = 1 + q + ... + q^6 in theta
        self.S7 = [F(1) if i % q == 0 else F(0) for i in range(q * 6 + 1)]
        self.one_minus_q7 = p_sub([F(1)], p_mono(q * 7))
        # D = 1 + theta + ... + theta^104
        self.D = [F(1)] * NPRIMES
        # value numerators per (r, y): q^lo - q^hi
        self.val = {}
        for r in range(M):
            for y in range(K):
                lo, hi = self.blocks[r][y]
                self.val[(r, y)] = p_trim(p_sub(p_mono(q * lo), p_mono(q * hi)))
        # cost numerator per atom: theta^r S_7; the common denominator
        # of costs and covers is D (1 - q^7), positive on (0, 1)
        self.cost = [p_mul(p_mono(r), self.S7) for r in range(M)]
        # cover numerator per (r, y): theta^r S_7 (q^lo - q^hi)
        self.cover = {k: p_mul(self.cost[k[0]], v) for k, v in self.val.items()}
        # target numerator: (1 - alpha) D (1 - q^7)
        self.target = p_scale(p_mul(self.D, self.one_minus_q7), F(1) - ALPHA)
        # the distinct values, keyed by their polynomial
        keys = {}
        for k, v in self.val.items():
            keys.setdefault(tuple(v), []).append(k)
        self.distinct = list(keys.items())  # [(poly tuple, [(r, y), ...])]


class Recorder(object):
    """Every sign the tree consults, as (label, integer polynomial,
    sign at theta_0)."""

    def __init__(self, theta):
        self.theta = theta
        self.tests = []

    def sign(self, label, poly):
        poly = p_int(poly)
        if not poly:
            return 0
        v = p_eval(poly, self.theta)
        s = 0 if v == 0 else (1 if v > 0 else -1)
        self.tests.append((label, poly, s))
        return s


def profile_at(cp, theta, record=False):
    """The certificate's size profile at theta by the transcribed
    tree; with record=True also the recorder holding every test."""
    rec = Recorder(theta)
    vals = [(F(p_eval(list(poly), theta)), poly, pairs)
            for poly, pairs in cp.distinct]
    # the operative level: the largest distinct value whose >= set
    # covers the target
    order = sorted(vals, key=lambda t: t[0], reverse=True)

    def cov_poly(t_poly):
        acc = []
        for poly, pairs in cp.distinct:
            if p_eval(list(poly), theta) >= p_eval(list(t_poly), theta):
                for k in pairs:
                    acc = p_add(acc, cp.cover[k])
        return p_sub(acc, cp.target)

    level = None
    for i, (_v, poly, pairs) in enumerate(order):
        s = rec.sign("cov>=target at value %s" % _vname(poly), cov_poly(poly))
        if s >= 0:
            level = i
            break
    assert level is not None
    t_poly = order[level][1]
    # every distinct value against the level; among the values above,
    # every pair (their order fixes each cov set)
    above = []
    for i, (_v, poly, _pairs) in enumerate(order):
        if i == level:
            continue
        s = rec.sign("value %s vs level %s" % (_vname(poly), _vname(t_poly)),
                     p_sub(list(poly), list(t_poly)))
        assert s != 0, "a value coinciding with the level at this theta"
        if s > 0:
            above.append(poly)
    for pa, pb in combinations(above, 2):
        rec.sign("value %s vs value %s" % (_vname(pa), _vname(pb)),
                 p_sub(list(pa), list(pb)))
    sizes = [0] * M
    above_cov = []
    for poly in above:
        for (r, _y) in dict(cp.distinct)[poly]:
            sizes[r] += 1
            above_cov = p_add(above_cov, cp.cover[(r, _y)])
    # the tied block and its cheapest fill: sum_S cost >= need, i.e.
    # t_num sum_S theta^r S_7 >= target - above_cov (both over the
    # common positive denominator)
    tied = dict(cp.distinct)[t_poly]
    shortfall = p_sub(cp.target, above_cov)
    subsets = []
    for size in range(len(tied) + 1):
        for S in combinations(range(len(tied)), size):
            csum = []
            for i in S:
                csum = p_add(csum, cp.cost[tied[i][0]])
            subsets.append((S, csum, p_eval(csum, theta)))
    lhs = lambda csum: p_mul(list(t_poly), csum)  # noqa: E731
    feasible = [(v, S, csum) for S, csum, v in subsets
                if p_eval(lhs(csum), theta) - p_eval(shortfall, theta) >= 0]
    assert feasible, "the tied block cannot close the shortfall"
    best = min(feasible, key=lambda t: t[0])
    _bv, S_star, c_star = best
    rec.sign("fill: %d-item block %s >= need" % (len(S_star), _sname(S_star, tied)),
             p_sub(lhs(c_star), shortfall))
    for S, csum, v in subsets:
        if S == S_star:
            continue
        if v < best[0]:
            s = rec.sign("fill: cheaper %d-item block %s < need"
                         % (len(S), _sname(S, tied)), p_sub(lhs(csum), shortfall))
            assert s < 0
        else:
            s = rec.sign("fill: block %s costlier than %s"
                         % (_sname(S, tied), _sname(S_star, tied)),
                         p_sub(csum, c_star))
            assert s > 0, "an equal-cost fill tie at this theta"
    for i in S_star:
        sizes[tied[i][0]] += 1
    return (sizes, rec, t_poly, tied, S_star) if record else sizes


def _vname(poly):
    """A value's numerator as q^lo - q^hi."""
    nz = [i for i, c in enumerate(poly) if c]
    return "q^%d-q^%d" % (nz[0] // 15, nz[1] // 15)


def _sname(S, tied):
    return "{" + ",".join(str(tied[i][0]) for i in S) + "}"


def profile_str(sizes):
    return "".join(str(s) for s in sizes)


# -------------------------------------------------------------- arms

def arm_transcription(cp):
    print("ARM 1 -- the transcription at theta_%d" % FAR)
    theta0 = theta_of(FAR)
    sizes, rec, t_poly, tied, S_star = profile_at(cp, theta0, record=True)
    print("  profile %s   level %s   tied block atoms %s   fill takes %s"
          % (profile_str(sizes), _vname(t_poly),
             [r for r, _y in tied], _sname(S_star, tied)))
    print("  %d tests recorded; each: degree, multiplicity at 1, largest"
          " root in (0, 1) as n = 1/(1 - theta)" % len(rec.tests))
    rows = []
    for label, poly, s in rec.tests:
        defl, mult = p_deflate_at_1(poly)
        assert p_eval(defl, 1) != 0
        br = None
        if p_eval(defl, F(0)) == 0:
            lo = F(1, 10 ** 6)
        else:
            lo = F(0)
        br = largest_root_below(defl, lo, F(1), F(1, 10 ** 9))
        rows.append((label, len(poly) - 1, mult, br, s))
    rows.sort(key=lambda t: (-(1 / (1 - t[3][1])) if t[3] else 0))
    nmax = None
    for label, deg, mult, br, s in rows:
        if br is None:
            root = "none"
        else:
            nlo = float(1 / (1 - br[0]))
            nhi = float(1 / (1 - br[1]))
            root = "theta in (%.9f, %.9f]  n in (%.4f, %.4f]" % (
                float(br[0]), float(br[1]), nlo, nhi)
            if nmax is None or nhi > nmax:
                nmax = nhi
        print("  %-48s deg %3d  mult@1 %d  sign %+d  root %s"
              % (label, deg, mult, s, root))
    return sizes, rec, rows, nmax


def certify(rec, n):
    """True iff every recorded test polynomial, deflated at 1, is
    nonzero at theta_n and root-free on (theta_n, 1)."""
    th = theta_of(n)
    for _label, poly, _s in rec.tests:
        defl, _m = p_deflate_at_1(poly)
        if p_eval(defl, th) == 0 or count_roots(defl, th, F(1)) > 0:
            return False
    return True


def arm_threshold(rec, nmax):
    print("\nARM 1b -- the certified threshold")
    n = int(nmax) + 1
    while not certify(rec, n):
        n += 1
    while n > 2 and certify(rec, n - 1):
        n -= 1
    print("  every test root-free on [theta_n, 1) for n = %d;"
          " some test has a root on [theta_%d, theta_%d)" % (n, n - 1, n))
    return n


def arm_ladder(cp, N):
    print("\nARM 2 -- C1 reproduction: transcribed tree vs cert_sizes")
    rungs = sorted(set(LADDER) | {N - 1, N})
    agree = 0
    for n in rungs:
        cell = walk_cell(n)
        got = cert_sizes(cell, ALPHA)
        assert got is not None, n
        mine = profile_at(cp, theta_of(n))
        ok = mine == got[0]
        agree += ok
        print("  W-%-6d cert_sizes %s   transcribed %s   %s"
              % (n, profile_str(got[0]), profile_str(mine),
                 "agree" if ok else "DIFFER (K-C)"))
    print("  %d of %d rungs agree" % (agree, len(rungs)))
    return agree == len(rungs)


def control_roots(N):
    print("\nC2 -- the root counter on planted roots")
    a = theta_of(N)
    mid = (a + 1) / 2
    planted = p_mul(p_sub(p_mono(1), [mid]), [F(3), F(0), F(1)])  # (x - mid)(x^2 + 3)
    c1 = count_roots(planted, a, F(1))
    br = largest_root_below(planted, a, F(1), F(1, 10 ** 9))
    ok1 = c1 == 1 and br is not None and br[0] < mid <= br[1]
    print("  (x - mid)(x^2 + 3): count %d, bracket holds mid: %s" % (c1, ok1))
    c2 = count_roots([F(1), F(0), F(1)], a, F(1))
    print("  1 + x^2: count %d" % c2)
    r1 = a + (1 - a) / 3
    r2 = a + 2 * (1 - a) / 3
    pair = p_mul(p_sub(p_mono(1), [r1]), p_sub(p_mono(1), [r2]))
    c3 = count_roots(pair, a, F(1))
    print("  two planted roots at thirds: count %d" % c3)
    ok = ok1 and c2 == 0 and c3 == 2
    print("  C2 %s" % ("PASSED" if ok else "FAILED (K-D)"))
    return ok


def _half_extremes(rlo, rhi, ranges, d):
    """Over vectors on atoms rlo..rhi-1: prefix (m_0..m_{d-2}) ->
    {m_{d-1}: (min m_d, max m_d)}, moments on the global atom
    indices."""
    rows = [[comb(r, j) for j in range(d + 1)] for r in range(rlo, rhi)]
    out = {}
    for vec in iproduct(*[range(lo, hi + 1) for lo, hi in ranges[rlo:rhi]]):
        ms = [0] * (d + 1)
        for i, c in enumerate(vec):
            if c:
                row = rows[i]
                for j in range(d + 1):
                    ms[j] += c * row[j]
        inner = out.setdefault(tuple(ms[:d - 1]), {})
        got = inner.get(ms[d - 1])
        if got is None:
            inner[ms[d - 1]] = (ms[d], ms[d])
        else:
            inner[ms[d - 1]] = (min(got[0], ms[d]), max(got[1], ms[d]))
    return out


def extreme_next_moment(ranges, d):
    """(min, max) of m_d over box vectors of flattening exactly d - 1
    (m_0..m_{d-2} = 0, m_{d-1} != 0), by a meet-in-the-middle join on
    the moment prefixes; None if no such vector."""
    a = _half_extremes(0, 7, ranges, d)
    b = _half_extremes(7, 15, ranges, d)
    lo = hi = None
    for pre, inner_a in a.items():
        inner_b = b.get(tuple(-x for x in pre))
        if inner_b is None:
            continue
        # per side: the two best maxima and the two best minima with
        # their m_{d-1} keys, so a forbidden key can be skipped
        bmax = sorted(((v[1], k) for k, v in inner_b.items()), reverse=True)[:2]
        bmin = sorted(((v[0], k) for k, v in inner_b.items()))[:2]
        for ka, (amin, amax) in inner_a.items():
            for v, kb in bmax:
                if kb != -ka:
                    if hi is None or amax + v > hi:
                        hi = amax + v
                    break
            for v, kb in bmin:
                if kb != -ka:
                    if lo is None or amin + v < lo:
                        lo = amin + v
                    break
    return None if lo is None else (lo, hi)


def arm_gap(cp, N, sizes):
    print("\nARM 3 -- the gap on the fixed box of s(N) = %s" % profile_str(sizes))
    ranges = [(sizes[r] - K, sizes[r]) for r in range(M)]
    spec = {}
    for depth in (4, 5, 6):
        _best, pos, deeper = deepest_flattening_15(ranges, depth)
        spec[depth] = pos
        if depth == 6:
            spec["deeper"] = deeper
    print("  A_4 %s  A_5 %s  A_6 %s  flattening-7 admissible: %s"
          % (spec[4], spec[5], spec[6], bool(spec["deeper"])))
    bound = [max(abs(sizes[r] - K), abs(sizes[r])) for r in range(M)]
    B = [sum(comb(r, j) * bound[r] for r in range(M)) for j in range(M)]
    print("  tail constants B_j = sum_r C(r,j) max|c_r|: %s" % B)

    def tail(J, n, start):
        return sum(F(B[j], n ** (j - J)) for j in range(start, M))

    A4 = spec[4]
    # exact per-flattening constants: least |m_J| and the extreme
    # m_{J+1} over vectors of flattening exactly J, J = 0..4
    A = {}
    E = {}
    for J in range(5):
        t0 = time.time()
        A[J] = deepest_flattening_15(ranges, J)[0]
        ext = extreme_next_moment(ranges, J + 1)
        E[J + 1] = max(abs(ext[0]), abs(ext[1]))
        print("  flattening %d: least |m_%d| %d, m_%d in [%d, %d]  (%.0f s)"
              % (J, J, A[J], J + 1, ext[0], ext[1], time.time() - t0))
    assert A[4] == A4

    def n0_of(crude):
        n = 2
        while True:
            if crude:
                ceiling = F(A4) + tail(4, n, 5)
            else:
                ceiling = F(A4) + F(E[5], n) + tail(4, n, 6)
            ok = True
            for J in range(4):
                if crude:
                    floor = (1 - tail(J, n, J + 1)) * n ** (4 - J)
                else:
                    floor = (A[J] - F(E[J + 1], n) - tail(J, n, J + 2))                         * n ** (4 - J)
                if floor <= ceiling:
                    ok = False
                    break
            if ok:
                return n
            n += 1
    n0_crude = n0_of(True)
    n0 = n0_of(False)
    print("  n_0 (every J <= 3 floor clears the J = 4 ceiling): %d by the"
          " box-only tail B_j, %d with the exact |m_J| and m_{J+1}"
          % (n0_crude, n0))
    print("  so for n >= %d the value-unit gap is %d n^-4 (1 + eps),"
          " |eps| <= (%d/n + sum_{j>=6} B_j n^(4-j))/%d"
          % (max(N, n0), A4, E[5], A4))
    print("  %-8s %14s %14s %14s" % ("rung", "g_A n^4 (value)", "band low", "band high"))
    for n in LADDER:
        if n < N:
            continue
        cell = walk_cell(n)
        cost, _cover, _target, den = integerize(cell, ALPHA)
        got = cert_sizes(cell, ALPHA)
        s = got[0]
        assert s == sizes, (n, s)
        best = anchored_gap_mim(cost, s, K, M)
        th = theta_of(n)
        value = F(best, den) * (1 - th ** M) / (1 - th) * n ** 4
        eps = (F(E[5], n) + tail(4, n, 6)) / A4
        inside = A4 * (1 - eps) <= value <= A4 * (1 + eps)
        print("  W-%-6d %14.9f %14.9f %14.9f  %s"
              % (n, float(value), float(A4 * (1 - eps)), float(A4 * (1 + eps)),
                 "inside" if inside else ("outside" if n >= n0 else "below n_0")))
    _best, vec = anchored_argmin(
        *(integerize(walk_cell(FAR), ALPHA)[0], sizes, K, M))
    J, mJ = flattening(vec)
    print("  argmin at W-%d: %s  flattening %d  m_J %d  moments %s"
          % (FAR, vec, J, mJ, moments(vec)[4:]))


def main():
    t0 = time.time()
    cp = CellPolys()
    print("the seven distinct posterior values: %s\n"
          % ", ".join(_vname(list(p)) for p, _ in cp.distinct))
    sizes, rec, rows, nmax = arm_transcription(cp)
    N = arm_threshold(rec, nmax)
    ok_c2 = control_roots(N)
    ok_c1 = arm_ladder(cp, N)
    arm_gap(cp, N, sizes)
    print("\nVERDICT: C1 %s, C2 %s; the profile %s is constant for all"
          " n >= %d (every test polynomial root-free on [theta_%d, 1))."
          % ("passed" if ok_c1 else "FAILED", "passed" if ok_c2 else "FAILED",
             profile_str(sizes), N, N))
    print("wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
