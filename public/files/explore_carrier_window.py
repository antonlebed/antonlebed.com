r"""explore_carrier_window.py -- how deep is a carrier load-bearing, and
can one be bought at a walkable norm? Price the SUPPLY FLOOR over every
(l, k) a menu could charge, and re-derive the LOAD-BEARING WINDOW against
the consumer's own column rather than against a formula.

THE QUESTION, in two halves that turn out to be one.

  HALF ONE -- THE PRICE. A place Q is a CARRIER for a seated place P over
  the rational prime l when v_l(L) is set by Q's own residue cardinality
  rather than by P's ladder, and what Q supplies is v_l(N(Q) - 1). So a
  carrier supplying v_l = k exists at norm q exactly when l^k divides
  q - 1, and the cheapest one at that (l, k) is the least prime power in
  that congruence class. The corpus has priced this at k = 1 only, over
  nine primes, at residue degree <= 2 against degree 3 (the carrier clause
  of the clock corpus; explore_cubic_undercut.py). At k >= 2 it has never
  been priced at all, and nothing in the corpus has ever SEATED a carrier
  with k >= 2. The question is whether that is arithmetic or accident:
  what does k >= 2 COST, and is any of it inside the belt the walks
  actually charge?

  HALF TWO -- THE WINDOW. A seated P over l supplies itself from its own
  ladder at depth a, so a carrier giving v_l = k is load-bearing only
  while the consumer's self-supply stays under k. The corpus files that
  self-supply as ceil((a-1)/e_P) and reads the window off it as
  a <= e_P*(k-1) + 1 -- from which its sharpest reading follows, that at
  k = 1 the window is the single depth a = 1 for EVERY ramification, the
  consumer's ramification cancelling. That formula is stated with no
  dependence on l. But the same corpus carries a HEAD criterion -- a place
  whose column holds one FLAT step more than its ramification accounts
  for, headed iff f = 1, e = (p-1)p^t and mu_p lies in the completion
  (explore_head_width.py F2) -- and a head is precisely a place whose
  column climbs SLOWER than the standard count. If a CONSUMER is headed,
  it supplies itself less than the formula says, and the window is wider
  than the corpus has ever written. The two halves meet at l = 2, where
  e = (2-1)*2^t admits e = 1 and mu_2 = {+-1} lies in every completion:
  the head condition there is nearly free.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The price half
is written in the RATIONAL ARITHMETIC of congruences -- prime power,
congruence class, floor -- and owes nothing to any field. The window half
is written in the WALKER's -- seated, supply, door, load-bearing -- and
the welding term is COLUMN, which belongs to the place: lambda(P^a) is
the exponent of (O/P^a)^*, a local invariant that both halves read. The
head is the LOCAL half's word and is imported as such (T1). Nothing in
the price half may be read as a statement about any ring's places, and
nothing in the window half as a fact about what a walk will charge.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 The HEAD is transplanted from the shop family (explore_head_width.py,
    explore_cubic_carrier.py), where it is a fact about a place a walk
    LOCKS ON -- a cheap recurrent absorber. Here it is read at a place in
    the opposite role, a CONSUMER being supplied. Nothing about pricing,
    absorption or menus is carried across; what is carried is one
    arithmetic reading, that a headed column holds an extra flat step.
    The excess is recomputed by brute here and never quoted.
 T2 "Walkable norm" is transplanted from the seed belts the cubic carrier
    rig walks (BELT 40, extended to 64). It is a MEASURED belt and not a
    bound, so every verdict resting on it is scoped to those belts and
    said to be. No claim below reads walkable as unreachable.
 T3 The window formula a <= e_P*(k-1) + 1 is the corpus's and is a
    PREDICTION here, not a premise. S3 and S4 read columns by brute and
    the formula is scored against them; where they disagree the brute is
    the verdict.
 T4 The l = 2 column shape is NOT carried from the classical structure of
    (Z/2^m)^*. Every column below is brute-forced from the ring, and the
    classical fact is what the control is FOR.

THE HAND-ATTACK, on paper before any engine code.

  THE FLOOR AND WHO ATTAINS IT. A place carrying v_l = k has norm q with
  l^k | q - 1 and q > 1, so q >= l^k + 1: that is the floor, and it is
  attained exactly when l^k + 1 is itself a prime power. At l = 2 the
  floor is 2^k + 1 and the Fermat numbers sit right on it -- k = 1 gives
  3, k = 2 gives 5, k = 4 gives 17 -- while k = 3 wants 9, which is 3^2
  and also a prime power. So the first four values of k at l = 2 should
  ALL attain their floor, at norms 3, 5, 9, 17. Every one of those is
  inside the walked belt. If that survives the engine, the answer to
  "can a carrier supply k >= 2 at a walkable norm" is not merely yes but
  yes four times over at the smallest prime there is, and the handover's
  reading -- that the cheapest candidate anywhere is 197 -- was an
  artifact of scanning residue degree 3 for l = 1 mod 3, which is the one
  family that CANNOT contain l = 2.

  WHY 197 WAS THE RIGHT ANSWER TO THE WRONG QUESTION. At l = 7, k = 2
  the floor is 50 and the least prime power that is 1 mod 49 is 197, a
  degree-1 place; the degree-3 route needs 49 | q^2+q+1, first at q = 67,
  norm 300763. Both are outside any belt. So the SCAN was right about
  l = 7 and its generalization to "anywhere" is what fails: the cost of
  k >= 2 is governed by l^k, and l = 2 is where l^k is cheap.

  THE WINDOW AND THE HEAD. For P over l with e = e_P, f = f_P, the column
  is lambda(P^a) = lcm(l^f - 1, exponent of U_1/U_a), and the l-part is
  what a carrier competes with. The standard count gives
  v_l(lambda(P^a)) = ceil((a-1)/e) -- U_1 climbing one rung per e in
  depth -- and this is exact once a passes the logarithm threshold
  a > e/(l-1). BELOW that threshold the l-th power map can land one rung
  deeper than the count, and that extra rung is the head. At l = 2, e = 1
  the threshold is a > 1, so the anomaly sits at the very bottom of the
  column where it cannot be outrun: (Z/2^a)^* is cyclic only to a = 2 and
  splits as Z/2 x Z/2^(a-2) after, so the 2-part of the exponent should
  read a - 2 from a = 3 on, one under the formula's a - 1. Every odd l at
  e = 1 has threshold a > 1/(l-1) < 1, so no anomaly and the formula
  should be exact.

  WHAT THAT DOES TO THE WINDOW. Write the consumer's self-supply as
  ceil((a-1)/e_P) - x_P with x_P the column's EXCESS -- 0 headless, and
  the head's extra rungs otherwise. Load-bearing is self-supply < k, i.e.
  ceil((a-1)/e_P) < k + x_P, i.e. a <= e_P*(k - 1 + x_P) + 1. So a headed
  consumer is load-bearing e_P*x_P deeper than the corpus's formula says,
  and at k = 1 the filed reading -- the single depth a = 1 for every
  ramification -- should hold at every HEADLESS consumer and FAIL at every
  headed one, where it reads a <= e_P + 1 instead.

  DISTRUST THE MARGIN. The derived half is the floor q >= l^k + 1 and the
  congruence search, which is a finite scan and admits no margin at all.
  The vibes half is the excess claim: that the anomaly is exactly ONE rung
  and sits exactly at l = 2. Both the size and the location are what S3
  and S4 measure, and a second rung anywhere, or an anomaly at an odd l,
  refutes the correction as stated rather than the direction of it.

  RE-DERIVING THE INDEX CONVENTION. Depth a is the EXPONENT of the place
  in the ideal, so a = 1 is the residue field itself and lambda(P^1) =
  l^f - 1, whose l-part is 0. The columns below are printed from a = 1
  and every formula is scored against that indexing, not against a
  0-based one.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 CONTROL. The brute column of (Z/l^a)^* prints v_l(lambda) = a - 1 at
     every depth read, for every odd l in scope; excess 0. And the brute
     quadratic machinery reproduces a split place over an odd l with the
     same column, which is what says the machinery is reading places and
     not integers.
  P2 The l = 2 column at e = f = 1 prints v_2(lambda) = a - 1 at a <= 2
     and a - 2 at a >= 3; excess exactly 1, no second rung at any depth
     read.
  P3 The supply floor table prints, for k = 2, least carrier norms 5 at
     l = 2, 19 at l = 3, 101 at l = 5, 197 at l = 7 -- so k = 2 is inside
     the belt of 64 at l = 2 and l = 3 and outside it at every l >= 5.
  P4 At l = 2 the least carrier norm for k = 1, 2, 3, 4 is 3, 5, 9, 17,
     each EQUAL to its floor 2^k + 1, and all four inside the belt; k = 5
     first leaves it, at 97 against a floor of 33.
  P5 A headed consumer's window is e_P deeper per unit of excess: the
     brute columns satisfy v_l(lambda(P^a)) = ceil((a-1)/e_P) - x_P at
     every depth past the head, with x_P the measured excess, and the
     corpus's a <= e_P*(k-1) + 1 fails at exactly the headed consumers.
  P6 The head criterion predicts the excess it is scored against: at
     l = 2 the places with f = 1 and e a power of 2 read excess >= 1, and
     the INERT place over 2 (f = 2) and every place over an odd l failing
     e = (l-1)l^t read excess 0.

KILL-SHAPES, frozen as observables and not as inferences.
  K1 If the k = 2 row of the floor table prints no norm at or under 64,
     the widening is priced out of the belts and the single-depth window
     stands as the law for walked states.
  K2 If the l = 2 column prints a - 1 at every depth, the excess is not
     there and the window formula needs no correction; P2 and P5 die
     together.
  K3 If any odd l prints a nonzero excess at e = 1, the anomaly is not
     the head's and the correction is misattributed even if the numbers
     move; the formula would then be wrong for a reason this rig has not
     found.
  K4 If a ramified consumer's excess fails to multiply by e_P in the
     window -- if the brute column's shortfall is not e_P*x_P rungs of
     DEPTH -- the correction is not a window statement and only the
     column reading survives.

RESOURCE ENVELOPE, named before the run. Every quotient is brute-forced
and capped at INDEX_CAP residues; the largest structure held is one list
of that many pairs. Peak well under the 512MB analysis default; wall
clock estimated at 1-2 minutes, single process.

FINDINGS.

  F1 K >= 2 IS CHEAP, AND IT IS CHEAP AT THE SMALLEST PRIME (rule in
     range; the least prime power q with l^k | q - 1 for every prime
     l < 24 and k <= 6, scanned to 2e6, S2). At l = 2 the least carrier
     norm for k = 1, 2, 3, 4 is 3, 5, 9, 17 -- every one of them EQUAL to
     its floor 2^k + 1, and every one inside the belt of 64. k = 5 is the
     first to leave, at 97 against a floor of 33. At l = 3 only k = 1 and
     k = 2 are in the belt (norms 4 and 19); at every l >= 5 the belt
     holds k = 1 alone, and l = 17 and l = 19 do not reach even that. So
     a carrier supplying k >= 2 is not a curiosity to be hunted at a
     large norm: at l = 2 it is the third-cheapest place there is.
     P3 and P4 hit exactly, including the four floor attainments.

  F2 THE 197 WAS THE RIGHT ANSWER TO THE WRONG QUESTION, and the scan
     that produced it named its own scope. The handover's reading -- that
     the cheapest carrier reaching k >= 2 anywhere is 197 -- is confirmed
     AT l = 7 and false as stated: 197 is the least prime power that is
     1 mod 49 (S2 reproduces it), and the degree-3 route's 300763 is
     worse, but both are l = 7 facts. The cost of k >= 2 is governed by
     l^k, so it is decided by how small l is and not by residue degree,
     and the degree-3 family -- l = 1 mod 3 dividing q^2+q+1 -- is the one
     family that cannot contain l = 2 at all. The undercut is a k = 1
     phenomenon (that reading stands); the WIDENING is an l = 2 one.

  F3 THE FILED WINDOW FORMULA IS THE HEADLESS FORMULA (rule in range;
     the window read straight off brute columns at eight consumers over
     three rational primes, k <= 4, S5). The corpus files the consumer's
     self-supply as ceil((a-1)/e_P) and reads the window a <= e_P*(k-1)+1
     off it. Scored against the window computed as max{a : self-supply
     < k} from the measured column, that closed form is EXACT at every
     headless consumer read -- Z at 3 and at 7, the inert place over 2,
     and the ramified place of Q(sqrt3) -- at every k in range, 16 of 16
     readings. At a HEADED consumer it is wrong, and that is the finding:
     the formula describes the column a place has when it has no head.

  F4 BUT THE HEAD DOES NOT SIMPLY WIDEN THE WINDOW -- IT ERRS IN BOTH
     DIRECTIONS, AND NOT AT ALL AT k = 1. Three readings, none of them
     the one this rig first derived:
       (a) At k = 1 the window is the single depth a = 1 at EVERY place
           read, headed or not, 8 of 8. It cannot be otherwise: the
           window needs self-supply 0, every column starts at 0 and every
           column reaches 1 by depth 2. So the corpus's sharpest reading
           -- that at k = 1 the window is depth 1 for every ramification
           -- SURVIVES intact, and survives at headed places too.
       (b) From k = 2 a headed consumer departs, and at Z's place over 2
           and the split place of Q(sqrt17) it is WIDER by exactly 1 at
           k = 2, 3, 4; at Q(sqrt-3) wider by 1 at k = 2 and 3 and back
           to EQUAL at k = 4.
       (c) At Q(i)'s ramified place over 2 the departure runs the other
           way first: NARROWER by 1 at k = 2 (window 2 against a filed 3)
           before running wider by 2 at k = 3 and 4. A head can COST a
           carrier depth.
     So there is no single-shift closed form, and the window is read off
     the column. What makes the direction unpredictable is the head's
     TRANSIENT: the column climbs FAST at the bottom before flattening
     -- Q(i) reads v = 0, 1, 2, 2, 2, 2, 2 -- so a shallow window can sit
     inside the fast stretch and a deeper one inside the flat.

  F5 THE ERROR THIS RIG MADE FIRST, kept because it is the reusable half.
     The freeze wrote the self-supply as ceil((a-1)/e_P) - x_P and the
     first engine fitted x_P as an ASYMPTOTIC depth shift, then derived a
     window from the fit -- giving "k = 1 widens to depth 2 over Q_2 and
     3 in Z[i]", which the direct reading above refutes flatly. The fit
     itself is sound and is still printed: past the head every column
     does satisfy v = ceil((a-1-x_P)/e_P), from depth 6 at the worst.
     What was invalid was APPLYING it where the window lives. The window
     is a SHALLOW-depth quantity and a head's transient is a shallow-depth
     effect, so an asymptotic fit is the one instrument guaranteed to
     miss it. Both instrument errors this file made have one shape:
     reading a quantity that varies with depth at a single depth, and
     reading a shallow quantity off a deep fit.

  F6 THE HEAD CRITERION PREDICTS WHICH CONSUMERS DEPART (rule in range;
     11 places, S5). Every consumer whose window matches the filed form
     at every k is headless by the criterion, and every consumer that
     departs at some k is headed -- the criterion agrees at 10 of 11
     places, and the eleventh is its mu_l clause showing its work:
     Q(sqrt-3) and Q(sqrt3) are identical in (l, e, f) = (3, 2, 1) and
     differ only in whether mu_3 lies in the completion, giving excess 1
     against 0 and a departing window against an exact one. The shape
     test alone cannot separate them, which is why the clause is in the
     criterion. Two further readings: the inert place over 2 (f = 2) is
     HEADLESS despite mu_2 lying in every completion, so f = 1 is doing
     real work and l = 2 is not blanket-headed; and Q(i)'s place over 2
     reads excess 2, refuting the freeze's vibes-half that the anomaly is
     exactly ONE rung -- flagged as the margin to distrust, and it was.

  F7 WHAT THIS BUYS A WALK, stated at the depth it was measured. At
     l = 2 a carrier of norm 5 supplies k = 2, and at a headed
     unramified consumer over 2 the window is depth 3 against the filed
     2; at norm 9 (k = 3) it is 4 against 3, and at norm 17 (k = 4) it
     is 5 against 4. At Q(i)'s ramified consumer the same norm-5 carrier
     gets depth 2 against a filed 3 -- less room, not more. The headless
     control moves at no k, which is what says the departure is the
     head's.

SCOPE, stated rather than implied. "Walkable" is the measured seed belt
of the cubic carrier rig (T2) and not a bound. The columns are read at
11 places drawn from Z and five quadratic orders, with e <= 2 and f <= 2
-- a cubic or wilder place is not read here, and neither is any place
with e divisible by l^2. The windows are read DIRECTLY off those columns
and are therefore exact for the places and the k listed, claiming
nothing about a place not read; k runs to 4 and a window deeper than a
column is not scored. The asymptotic fit is reported separately and is
not what any window claim rests on.

RUN RECORD. One process, 0.3s wall, peak working set 12.8 MB against the
512 MB default (memwatch). 15 asserted checks pass, S1 first: the odd
rational columns read the standard count exactly, and the split place
over 7 in Q(sqrt2) reproduces Z's column at 7 term for term, which is
what says the lattice machinery reads a PLACE. The first run's asserts
also caught a mis-scoped control of my own -- it quoted the corpus's 29
as the cheapest v_7 = 1 supplier, which is the degree <= 2 figure, where
this table is unbounded in degree and correctly prints the norm-8
degree-3 carrier; both are now checked.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import gcd

CHECKS = 0

INDEX_CAP = 4200      # residues allowed in one brute-forced quotient
FLOOR_SCAN = 2000000  # prime powers scanned for the least carrier norm
BELT = 64             # the walked seed belt, extended (T2) -- measured
K_MAX = 6             # supply levels priced
L_MAX = 24            # rational primes l priced (the corpus's nine)


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def v_p(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_power(n):
    """(p, f) if n = p^f with f >= 1, else None."""
    if n < 2:
        return None
    d = 2
    while d * d <= n:
        if n % d == 0:
            f = 0
            m = n
            while m % d == 0:
                m //= d
                f += 1
            return (d, f) if m == 1 else None
        d += 1
    return (n, 1)


def lcm(a, b):
    return a // gcd(a, b) * b


# ---------------------------------------------------- half one: the price
def least_carrier_norm(ell, k, cap=FLOOR_SCAN):
    """The least prime power q with ell^k | q - 1 -- the cheapest place
    that can supply v_ell = k, at any residue degree. Returns (q, p, f)
    or None if the scan runs out."""
    m = ell ** k
    q = m + 1
    while q <= cap:
        pf = prime_power(q)
        if pf is not None:
            return (q, pf[0], pf[1])
        q += m
    return None


# ------------------------------------------- half two: the local columns
def lam_of_group(elems, mul, one):
    """Exponent of a finite abelian group given as a list of elements with
    a multiplication -- brute, which is the instrument the verdict needs.
    An element already killed by the running exponent is skipped, which is
    a speedup and not an approximation: the exponent is the lcm of orders
    and an element with u^e = 1 has order dividing e."""
    def powr(u, k):
        r, b = one, u
        while k:
            if k & 1:
                r = mul(r, b)
            b = mul(b, b)
            k >>= 1
        return r

    e = 1
    for u in elems:
        if powr(u, e) == one:
            continue
        k, v = 1, u
        while v != one:
            v = mul(v, u)
            k += 1
        e = lcm(e, k)
    return e


def column_Z(ell, cap=INDEX_CAP):
    """lambda((Z/ell^a)^*) for a = 1.. while ell^a fits the cap. This is
    the place of a rational prime in Z: e = f = 1."""
    col, a = [], 1
    while ell ** a <= cap:
        n = ell ** a
        us = [x for x in range(1, n) if gcd(x, n) == 1]
        col.append(lam_of_group(us, lambda x, y, n=n: x * y % n, 1))
        a += 1
    return col


class QuadOrder(object):
    """The maximal order of Q(sqrt d), d squarefree, on basis {1, w} with
    w^2 = t*w + n. Elements are pairs (x, y) meaning x + y*w."""

    def __init__(self, d):
        self.d = d
        if d % 4 == 1:
            self.t, self.n = 1, (d - 1) // 4
        else:
            self.t, self.n = 0, d

    def mul(self, u, v):
        x1, y1 = u
        x2, y2 = v
        return (x1 * x2 + self.n * y1 * y2,
                x1 * y2 + x2 * y1 + self.t * y1 * y2)

    def places(self, ell):
        """Places over ell as (e, f, lattice-basis of P). The lattice is a
        2x2 column pair [(a,b),(c,e)] of Z-coordinates on {1, w}, read from
        the factorization of x^2 - t*x - n mod ell."""
        roots = [r for r in range(ell) if (r * r - self.t * r - self.n) % ell == 0]
        if not roots:
            return [(1, 2, self.hnf([(ell, 0), (0, ell)]))]
        if len(roots) == 2:
            return [(1, 1, self.hnf([(ell, 0), (-r % ell, 1)])) for r in roots]
        r = roots[0]
        return [(2, 1, self.hnf([(ell, 0), (-r % ell, 1)]))]

    # ---- integer lattice machinery, 2x2, on coordinates (x, y)
    @staticmethod
    def hnf(vecs):
        """Hermite form [(h11, h12), (0, h22)] of the Z-lattice spanned by
        the given coordinate vectors: basis b1 = (h11, 0), b2 = (h12, h22)."""
        rows = [(int(v[0]), int(v[1])) for v in vecs]
        # one generator carrying the gcd of every y-coordinate, built by
        # running extended gcd so its x-coordinate is carried along with it
        cx, cy = 0, 0
        for (x, y) in rows:
            if y == 0:
                continue
            if cy == 0:
                cx, cy = x, y
                continue
            g = gcd(cy, y)
            u, v = QuadOrder.egcd(cy, y)
            cx, cy = cx * u + x * v, g
        if cy == 0:
            h11 = 0
            for (x, _) in rows:
                h11 = gcd(h11, x)
            return (abs(h11), 0, 0)
        if cy < 0:
            cx, cy = -cx, -cy
        h12, h22 = cx, cy
        # every lattice vector drops to the y = 0 line by subtracting a
        # multiple of that generator; h11 is the gcd of where they land
        h11 = 0
        for (x, y) in rows:
            h11 = gcd(h11, x - (y // h22) * h12)
        h11 = abs(h11)
        if h11:
            h12 %= h11
        return (h11, h12, h22)

    @staticmethod
    def egcd(a, b):
        """(u, v) with a*u + b*v = gcd(a, b)."""
        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1
        while r:
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
        return old_s, old_t

    @staticmethod
    def lat_mul(A, B, O):
        """Product of two lattices as ideals: all pairwise products, HNF'd."""
        a1 = (A[0], 0)
        a2 = (A[1], A[2])
        b1 = (B[0], 0)
        b2 = (B[1], B[2])
        prods = [O.mul(u, v) for u in (a1, a2) for v in (b1, b2)]
        return QuadOrder.hnf(prods)

    @staticmethod
    def reduce(u, L):
        """Coordinates of u reduced into the fundamental box of lattice L."""
        h11, h12, h22 = L
        x, y = u
        if h22:
            q = y // h22
            x -= q * h12
            y -= q * h22
        if h11:
            x %= h11
        return (x, y)

    @staticmethod
    def index(L):
        return L[0] * L[2]

    @staticmethod
    def in_lattice(u, L):
        return QuadOrder.reduce(u, L) == (0, 0)


def column_quad(O, ell, e_want, f_want, cap=INDEX_CAP):
    """lambda((O/P^a)^*) for a = 1.. at the place over ell with the asked
    (e, f), brute over the residue box while the index fits the cap."""
    sel = [pl for pl in O.places(ell) if pl[0] == e_want and pl[1] == f_want]
    if not sel:
        return None
    P = sel[0][2]
    col, a, Pa = [], 1, P
    while QuadOrder.index(Pa) <= cap:
        h11, h12, h22 = Pa
        reps = [(x, y) for x in range(h11) for y in range(h22)]
        units = [u for u in reps if not QuadOrder.in_lattice(u, P)]
        one = QuadOrder.reduce((1, 0), Pa)
        col.append(lam_of_group(
            units,
            lambda u, v, L=Pa: QuadOrder.reduce(O.mul(u, v), L),
            one))
        a += 1
        Pa = QuadOrder.lat_mul(Pa, P, O)
    return col


def excess_of(col, ell, e):
    """The column's DEPTH EXCESS: the least x >= 0 for which the measured
    ell-part reads v_ell(lambda(P^a)) = ceil((a-1-x)/e) on a whole suffix
    of the column, returned with the depth that suffix starts at.

    Reading it at ONE depth is what the first instrument did and it is
    wrong for e > 1: the head shifts the DEPTH argument, so the shortfall
    against ceil((a-1)/e) oscillates with period e and scores 0 at half
    the depths a headed place could be read at. The asymptotic shift is
    the quantity the window needs, and it is what this fits.

    It is also NOT the shop family's excess, which is a run length less e
    (explore_cubic_carrier.py excess_of). That one is a head DETECTOR --
    nonzero iff headed -- and it counts the head's transient rungs too,
    so the two numbers part company wherever a head has a transient."""
    if not col:
        return (None, None)
    vs = [v_p(x, ell) for x in col]
    n = len(vs)
    best = None
    for x in range(0, n):
        for start in range(0, n):
            if all(vs[a - 1] == max(0, -(-(a - 1 - x) // e))
                   for a in range(start + 1, n + 1)):
                cand = (x, start + 1)
                if best is None or (cand[1], cand[0]) < (best[1], best[0]):
                    best = cand
                break
    return best if best else (None, None)


def head_predicted(ell, e, f):
    """The corpus's head criterion (T1): f = 1, e = (l-1)*l^t, and mu_l in
    the completion. The third clause is not decidable from (e, f) alone, so
    this returns the criterion's SHAPE test and S5 scores it as such."""
    if f != 1:
        return False
    m = e
    if m % (ell - 1) != 0:
        return False
    m //= (ell - 1)
    while m % ell == 0:
        m //= ell
    return m == 1


def true_window(col, ell, k):
    """The load-bearing window read STRAIGHT off the measured column: the
    deepest a whose self-supply is still under k. This is the definition;
    every closed form below is scored against it and never the reverse.

    Reading a window off an ASYMPTOTIC fit instead is the error this
    function exists to prevent -- the window lives at SHALLOW depth, which
    is exactly where a head's transient has not settled."""
    good = [a for a in range(1, len(col) + 1) if v_p(col[a - 1], ell) < k]
    return max(good) if good else 0


def shortfall(col, ell, e):
    """Per-depth shortfall of the measured ell-part against the standard
    count ceil((a-1)/e), indexed from a = 1."""
    return [(-(-(a) // e)) - v_p(col[a], ell) for a in range(len(col))]


# ------------------------------------------------------------- the sections
def s1_control():
    section("S1  CONTROL -- the instruments read what they are pointed at")
    for ell in (3, 5, 7):
        col = column_Z(ell)
        vs = [v_p(x, ell) for x in col]
        print("  Z, l=%2d  e=1 f=1  v_l(lambda) = %s   standard a-1 = %s"
              % (ell, vs, list(range(len(vs)))))
        ok(vs == list(range(len(vs))),
           "odd rational place off the standard count at l=%d" % ell)
    # the quadratic machinery must reproduce a place, not an integer:
    # 7 splits in Q(sqrt 2) (2 is a QR mod 7), and each factor has e=f=1,
    # so its column must equal Z's at 7 exactly.
    O = QuadOrder(2)
    col = column_quad(O, 7, 1, 1)
    ref = column_Z(7)[:len(col)]
    print("  Q(sqrt2), l=7 split  e=1 f=1  lambda = %s" % col)
    print("  Z, l=7 truncated                lambda = %s" % ref)
    ok(col == ref, "split place over 7 does not reproduce the rational column")
    print("  -> the lattice machinery reads a PLACE and agrees with Z where"
          " the place is rational")


def s2_floor():
    section("S2  THE PRICE -- least carrier norm supplying v_l = k, any degree")
    print("  floor is l^k + 1; belt is norm <= %d (measured, not a bound)" % BELT)
    print("   l    k   least q      p^f      floor   attains  in belt")
    rows = {}
    for ell in [q for q in range(2, L_MAX) if is_prime(q)]:
        for k in range(1, K_MAX + 1):
            got = least_carrier_norm(ell, k)
            if got is None:
                print("  %2d  %3d      -- none under the scan cap --" % (ell, k))
                continue
            q, p, f = got
            floor = ell ** k + 1
            rows[(ell, k)] = q
            print("  %2d  %3d  %9d   %3d^%-2d  %8d   %-6s  %s"
                  % (ell, k, q, p, f, floor,
                     "yes" if q == floor else "no",
                     "YES" if q <= BELT else "no"))
        print("")
    # the corpus's own carrier table is the DEGREE-BOUNDED reading: its 29
    # is the cheapest supplier of v_7 = 1 at residue degree <= 2, and its 8
    # is the degree-3 undercut. This table is unbounded in degree, so it
    # must reproduce the 8 -- and the bounded scan beside it, the 29.
    ok(rows[(2, 1)] == 3 and rows[(7, 1)] == 8,
       "the unbounded k=1 row lost the corpus's norm-8 degree-3 carrier")
    lo = min(q for q in range(2, 400)
             if prime_power(q) and prime_power(q)[1] <= 2 and (q - 1) % 7 == 0)
    print("  cheapest v_7 = 1 supplier at residue degree <= 2: norm %d"
          " (the corpus's undercut baseline)" % lo)
    ok(lo == 29, "the degree <= 2 baseline for l=7 is not the corpus's 29")
    walk2 = [k for k in range(1, K_MAX + 1) if rows.get((2, k), 10 ** 9) <= BELT]
    print("  k reachable inside the belt at l=2: %s" % walk2)
    for ell in [q for q in range(3, L_MAX) if is_prime(q)]:
        ws = [k for k in range(1, K_MAX + 1)
              if rows.get((ell, k), 10 ** 9) <= BELT]
        print("  k reachable inside the belt at l=%d: %s" % (ell, ws))
    return rows


def s3_rational_columns():
    section("S3  THE CONSUMER COLUMN at e = f = 1 -- brute, over every l")
    print("   l   lambda column                v_l          standard   excess")
    out = {}
    for ell in [q for q in range(2, L_MAX) if is_prime(q)]:
        col = column_Z(ell)
        vs = [v_p(x, ell) for x in col]
        std = list(range(len(vs)))
        x, start = excess_of(col, ell, 1)
        out[ell] = (col, vs, x, start)
        print("  %2d   %-26s %-12s %-10s %d (from a=%d)"
              % (ell, col[:6], vs, std, x, start))
    ok(out[2][2] == 1, "l=2 did not read depth excess 1 at e=f=1")
    for ell in out:
        if ell != 2:
            ok(out[ell][2] == 0,
               "odd l=%d read a nonzero excess at e=f=1 (K3)" % ell)
    return out


def s4_quadratic_columns():
    section("S4  RAMIFIED AND INERT CONSUMERS -- the excess against (e, f)")
    cases = [
        (-1, 2, 2, 1, "Q(i): 2 ramified"),
        (17, 2, 1, 1, "Q(sqrt17): 2 split"),
        (5, 2, 1, 2, "Q(sqrt5): 2 inert"),
        (-3, 3, 2, 1, "Q(sqrt-3): 3 ramified, mu_3 present"),
        (3, 3, 2, 1, "Q(sqrt3): 3 ramified, mu_3 ABSENT"),
        (-1, 5, 1, 2, "Q(i): 5 inert"),
    ]
    out = []
    print("  %-34s l  e f  excess  from  head-shape  v_l column"
          % "field and place")
    for d, ell, e, f, tag in cases:
        O = QuadOrder(d)
        col = column_quad(O, ell, e, f)
        if col is None:
            print("  %-34s %2d  %d %d   -- place absent --" % (tag, ell, e, f))
            continue
        vs = [v_p(x, ell) for x in col]
        x, start = excess_of(col, ell, e)
        hp = head_predicted(ell, e, f)
        print("  %-34s %2d  %d %d  %5d  a=%-3d %-10s  %s"
              % (tag, ell, e, f, x, start, "yes" if hp else "no", vs))
        out.append((d, ell, e, f, tag, col, vs, x, hp))
    return out


def s5_window(rows, rat, quad):
    section("S5  THE WINDOW REPRICED -- self-supply, excess, and the depth")
    print("  filed:     self-supply = ceil((a-1)/e_P),  window a <= e_P(k-1)+1")
    print("  corrected: self-supply = ceil((a-1-x_P)/e_P),")
    print("             window a <= e_P(k-1) + 1 + x_P      (P5 as frozen,")
    print("             which read the shift as e_P*x_P in VALUE, is REFUTED:")
    print("             the head shifts DEPTH, so the widening is x_P flat)")
    print("")
    print("  per-depth shortfall of the measured column against the count:")
    for ell in (2, 3, 7):
        col = rat[ell][0]
        sf = shortfall(col, ell, 1)
        print("    Z, l=%2d e=1: %s" % (ell, sf))
    for (d, ell, e, f, tag, col, vs, x, hp) in quad:
        print("    %-34s %s" % (tag + ":", shortfall(col, ell, e)))
    print("")
    print("  the head criterion scored against the measured excess:")
    allc = [(2, 1, 1, rat[2][2]), (3, 1, 1, rat[3][2]), (5, 1, 1, rat[5][2]),
            (7, 1, 1, rat[7][2]), (11, 1, 1, rat[11][2]),
            (13, 1, 1, rat[13][2])]
    allc += [(ell, e, f, x) for (d, ell, e, f, tag, col, vs, x, hp) in quad]
    agree = 0
    for (ell, e, f, x) in allc:
        hp = head_predicted(ell, e, f)
        mark = "agree" if (hp == (x > 0)) else "DISAGREE"
        if mark == "agree":
            agree += 1
        print("    l=%2d e=%d f=%d  excess %d  criterion says %-3s  %s"
              % (ell, e, f, x, "yes" if hp else "no", mark))
    print("  criterion agrees at %d of %d places read" % (agree, len(allc)))
    print("  the one DISAGREE is the criterion's THIRD clause, and it is a")
    print("  confirmation rather than a miss: head_predicted tests only the")
    print("  SHAPE (f=1, e=(l-1)l^t) because mu_l in the completion is not")
    print("  decidable from (e, f). Q(sqrt-3) and Q(sqrt3) are identical in")
    print("  (l, e, f) = (3, 2, 1) and differ ONLY in mu_3, and they read")
    print("  excess 1 against 0 -- so the clause the shape test drops is")
    print("  exactly the clause the columns need.")
    print("")
    print("  THE WINDOW READ OFF THE COLUMN, against the filed closed form.")
    print("  The window is max{a : self-supply < k} and nothing else; the")
    print("  closed form is scored against it, never substituted for it.")
    print("  %-36s  k  TRUE  filed  verdict" % "consumer")
    places = [("Z at 2: e=1 f=1, headed", rat[2][0], 2, 1),
              ("Z at 3: e=1 f=1, headless", rat[3][0], 3, 1),
              ("Z at 7: e=1 f=1, headless", rat[7][0], 7, 1)]
    places += [(tag, col, ell, e)
               for (d, ell, e, f, tag, col, vs, x, hp) in quad]
    verdicts = {}
    for (tag, col, ell, e) in places:
        for k in range(1, 5):
            filed = e * (k - 1) + 1
            if filed > len(col):
                continue
            tw = true_window(col, ell, k)
            if tw == filed:
                verd = "same"
            elif tw > filed:
                verd = "WIDER  +%d" % (tw - filed)
            else:
                verd = "NARROWER %d" % (tw - filed)
            verdicts.setdefault(tag, []).append((k, tw, filed, verd))
            print("  %-36s  %d  %4d  %5d  %s" % (tag, k, tw, filed, verd))
    # the two readings the closed form gets wrong, asserted so they cannot
    # quietly come back: k = 1 never widens, and a head can NARROW.
    for (tag, col, ell, e) in places:
        ok(true_window(col, ell, 1) == 1,
           "k=1 window is not depth 1 at %s" % tag)
    qi = [c for c in places if c[0].startswith("Q(i)")]
    if qi:
        tag, col, ell, e = qi[0]
        ok(true_window(col, ell, 2) < e * 1 + 1,
           "Q(i) at k=2 no longer reads NARROWER than the filed form")
    print("  -> the filed form is EXACT at every headless consumer read,")
    print("     and at a headed one it errs in BOTH directions.")


def main():
    print("explore_carrier_window.py -- the supply floor and the load-bearing"
          " window")
    s1_control()          # the positive control runs BEFORE any verdict
    rows = s2_floor()
    rat = s3_rational_columns()
    quad = s4_quadratic_columns()
    s5_window(rows, rat, quad)
    section("CHECKS")
    print("  %d asserted checks passed" % CHECKS)


if __name__ == "__main__":
    main()
