"""
THE DELETED BUDGET -- what does an imported hypothesis's failure buy?

Two specimens sit on adjacent blocks of the walls chart and neither
reads as an instance of the other. Designed ramification
(explore_designed_ramification.py): Hilbert reciprocity forces an even
ramification set across ALL places, the tower keeps only the finite
ones, and the visible set can be odd -- deleting a place turned a
global parity law into a design knob. The division ladder
(explore_division_ladder.py): Chevalley-Warning needs a degree-2 form
in >= 3 variables, so the ladder is uniform from the quaternion floor
up and channel-sensitive at exactly the entry floor -- an unmet
numeric hypothesis left a channel-sensitive corner the theorem never
governed. This sweep asks whether each shape recurs, keeping the two
routes sorted, because they do different things:

  PLACE ROUTE: a deleted place removes a TERM from a constraint that
  still binds what remains -- the freedom bought is a design knob.
  THRESHOLD ROUTE: an unmet hypothesis leaves the theorem SILENT --
  what survives below is whatever it never governed.

THE CANDIDATES, SORTED BEFORE PRICING (the sort is part of the slate):
  PLACE: Hilbert reciprocity (the anchor, already verified); the
  Brauer sum-of-invariants law sum_v inv_v = 0 (TRANSPLANT FLAG: the
  quaternion result is its 2-torsion instance, and the suspicion that
  every cyclic algebra hands a designable channel pattern is imported
  from n = 2 to n >= 3); the product formula prod_v |x|_v = 1 (the
  case the two pricing windows' conservation law reduces to); the
  function-field degree relation on F_2(t) (the CONTROL: its deleted
  place is NOT archimedean, so it separates "deletion buys" from
  "archimedean-ness buys").
  THRESHOLD: Chevalley-Warning (the anchor, already charted); the
  square-counting ladder -- Lagrange's four squares, with the three-
  and two-square theorems as its sub-threshold floors; Wedderburn and
  Artin-Zorn (hypothesis = finiteness, which every channel MEETS, so
  no tower object sits below the threshold: sorted degenerate, not
  computed); the Hurwitz dimensions (the ladder's end is uniform over
  R and over every channel alike -- already charted, no per-channel
  corner: sorted charted, not computed).

THE HAND-ATTACK (before any engine code).
  (i) Product formula: x = prod p^(a_p) realizes ANY finitely
  supported valuation vector, so with the archimedean term deleted
  the finite constraint is VOID -- the freedom bought is the deleted
  place's entire value group. The full formula prod_v |x|_v = 1
  (finite places times the archimedean absolute value) must print
  exactly 1 as a Fraction.
  (ii) Brauer: Br(R) = {0, 1/2} (Frobenius: the real division
  algebras are R, C, H), so the deleted place can absorb exactly one
  bit, and only 2-torsion. For a quaternion class the visible
  (finite) invariant sum is 0 or 1/2 -- both realizable, the odd
  visible parity exactly when (a,b)_inf = -1. For an odd-degree
  cyclic algebra the invariants live in (1/n)Z/Z, which contains no
  1/2, so the finite sum must be 0 EXACTLY: the transplant DIES BY
  HAND -- the quaternion knob is the whole knob, one bit, and odd
  torsion buys nothing. (Property + classical: Albert-Brauer-Hasse-
  Noether exact sequence; not computed here.)
  (iii) The emerging law the sweep tests: THE FREEDOM A DELETED PLACE
  BUYS IS EXACTLY ITS OWN LOCAL TERM'S GROUP -- {+-1} for
  reciprocity (one bit), Br(R) = Z/2 for the Brauer sum (one bit,
  2-torsion only), the full value group for the product formula
  (total freedom). The function-field control tests that the law is
  about DELETION, not about the deleted place being archimedean.
  (iv) Squares: mod any odd p the squares-with-zero number (p+1)/2,
  and two translates of a (p+1)/2-set cover F_p, so EVERY residue is
  a sum of two squares at EVERY channel -- the sub-threshold
  conditions are invisible at precision 1. The two-square condition
  over Z is a VALUATION-PARITY fact (v_p(n) even at p = 3 mod 4);
  the three-square condition is a 2-ADIC fact at channel 2
  (n != 4^a(8b+7): strip the 4s -- depth -- then read mod 8 --
  precision -- while the channel reads mod 2:
  squares mod 8 are {0,1,4} and three of them never sum to 7).
  Hand-derived invisible pair for three squares: 7 and 510517 =
  7 + 510510 agree at every channel of Z/510510; 510517 = 5 mod 8
  and is odd, so it IS a sum of three squares while 7 is not.
  (v) Index convention re-derived before the freeze: RAD channels
  are p in {2,3,5,7,11,13,17}; a residue window at channel p reads
  n mod p, precision 1.

THE PREDICTIONS (frozen before the engine; kills are what the rig
PRINTS, weighed after).
  F1 (place / product formula): 200 random valuation vectors each
  realized by a constructed rational whose valuations reprint the
  vector, and prod_v |x|_v over ALL places = 1 exactly, every trial.
  KILL OBSERVABLE: any vector whose constructed rational's
  valuations differ, or any product printing != 1.
  F2 (place / function-field control, q = 2): for random nonzero
  f in F_2(t), sum over all places (monic irreducibles + the degree
  place) of deg(v) * v(f) prints 0; and CONSTRUCTIVELY (the mirror
  of F1's realization) f = t^k realizes visible sum k for every k in
  [-8, 8]. KILL OBSERVABLE: a nonzero full sum, or a k the
  construction misses. (The slate's first draft asked a random
  sample to cover [-6, 6] -- a sampling margin, not a freedom test;
  replaced by the construction before any verdict was read, the
  freedom claim being constructive in every route case.)
  F3 (place / Brauer 2-torsion): POSITIVE CONTROL first -- the four
  recorded algebras (5,3), (77,-1), (-1,-1), (-3,-1) reprint visible
  sets {3,5}, {7,11}, {2}, {3} with infinity flags F, F, T, T. Then
  the sweep over squarefree a, b with |a|, |b| <= 30: reciprocity
  holds at every pair, the visible set's parity is odd EXACTLY when
  a < 0 and b < 0 ((a,b)_inf = -1), and both parities occur.
  KILL OBSERVABLE: any parity mismatch, or all visible parities
  even (nothing bought).
  F4 (place / Brauer odd torsion): no computation -- the verdict is
  the hand derivation in (ii), tier property + classical. Printed as
  a statement only.
  F5 (threshold / per-channel totality): at every RAD channel every
  residue is a sum of two squares (exhaustive); mod 8 the sums of
  three squares miss exactly {7} while mod 2 they miss nothing.
  KILL OBSERVABLE: a channel with an unreachable residue (would
  make the sub-threshold condition residue-visible, hence charted).
  F6 (threshold / the ladder over Z, exhaustive to N = 20000, all
  verdicts by direct search): two squares iff v_p(n) even for every
  p = 3 mod 4; three squares iff n != 4^a(8b+7); four squares total.
  KILL OBSERVABLE: any n breaking any of the three equivalences.
  F7 (threshold / the invisibility observable): an explicit pair
  n = n' mod 510510 with opposite two-square verdicts (valuation
  invisibility), and the hand-derived pair (7, 510517) with opposite
  three-square verdicts (precision invisibility) -- BOTH verdicts by
  direct search, the characterization used only to aim. No pair
  exists for four squares (nothing survives at the threshold).
  KILL OBSERVABLE (the threshold route's kill): no invisible pair
  found -- every sub-threshold survivor residue-visible.

Survey anchors (classical, named so nothing poses as new): Hilbert
symbols and reciprocity (Serre, A Course in Arithmetic III); the
Albert-Brauer-Hasse-Noether exact sequence 0 -> Br(Q) ->
sum_v Br(Q_v) -> Q/Z -> 0 with Br(R) = (1/2)Z/Z (Frobenius);
the product formula over Q and over F_q(t); Fermat/Euler two squares,
Legendre/Gauss three squares, Lagrange four squares; Chevalley-
Warning; Wedderburn; Artin-Zorn; Hurwitz. Our content is the
composition: the deleted-budget law across the place route, and the
sub-threshold survivors read against the tower's residue windows.

FINDINGS (entered post-run; all printed output, 0.18 s, trivial
memory; every assert green, neither route's kill fired).

  F1 HOLDS (rule): 200/200 constructed rationals reprint their
  valuation vectors and print full product exactly 1. With the
  archimedean term deleted the finite product formula constrains
  NOTHING -- the freedom bought is the deleted place's entire value
  group.
  F2 HOLDS (rule): 200/200 full degree sums print 0 over F_2(t);
  t^k realizes every visible sum k in [-8, 8]. The deleted place is
  the DEGREE place -- non-archimedean, degree 1 -- and deleting it
  buys the same total freedom: THE BUDGET LAW IS ABOUT DELETION,
  NOT ARCHIMEDEAN-NESS.
  F3 HOLDS (rule): positive control 4/4; 1444 squarefree pairs,
  0 parity mismatches, odd visible sets 361 = 19^2 -- EXACTLY the
  a < 0, b < 0 quadrant, so the visible parity is the deleted
  place's symbol and nothing else. Both parities realized.
  F4 (property + classical): Br(R) = {0, 1/2}, so the Brauer budget
  is one bit and 2-torsion's alone -- the quaternion design knob is
  the WHOLE knob; odd-degree cyclic algebras' visible invariants
  still sum to 0 exactly. The n = 2 -> n >= 3 transplant dies.
  F5 HOLDS (rule): every residue at every channel is a sum of two
  squares (7/7 channels exhaustive); three-square sums mod 8 miss
  exactly {7} while mod 2 they miss nothing.
  F6 HOLDS (rule, exhaustive to 20000, all verdicts direct): two
  squares iff v_p(n) even at every p = 3 mod 4; three squares iff
  n != 4^a(8b+7); four squares total. 0/0/0 mismatches.
  F7 HOLDS (rule): invisible pairs printed with both verdicts by
  direct search -- two squares (3, 2552553), congruent mod 510510,
  False/True (valuation-depth invisibility); three squares
  (7, 510517), False/True (precision invisibility: 510517 = 5 mod
  8). Four squares: no condition survives, no pair exists.

  THE SYNTHESIS. The two routes price in the same currency. PLACE:
  what deleting a place buys at a global constraint is exactly the
  deleted term's own local group -- {+-1} for reciprocity (one
  parity bit), Br(R) = (1/2)Z/Z for the Brauer sum (one bit,
  2-torsion only), the full value group for the product formula
  (the visible constraint void) -- and the function-field control
  shows the law is deletion's, not the archimedean place's.
  THRESHOLD: below an unmet uniformity hypothesis what survives is
  local data DEEPER than the residue window -- valuation parity
  (depth) for two squares, the 2-adic n != 4^a(8b+7) for three
  (strip the 4s, then read mod 8: depth, then precision; the pair's
  odd witness isolates the precision half), nothing at the
  threshold itself -- so the survivors are exactly
  channel-invisible, witnessed by congruent pairs with opposite
  verdicts. Wedderburn and Artin-Zorn are degenerate for the sweep
  (finiteness is met by every channel; nothing sits below), and the
  Hurwitz boundary is uniform and already charted, so the square
  ladder is the route's one specimen beyond the entry floor.
"""

import random
from fractions import Fraction

random.seed(2)

RAD = [2, 3, 5, 7, 11, 13, 17]
M_RAD = 510510


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# ---------------------------------------------------------------------------
# Shared small number theory (Hilbert symbols as in
# explore_designed_ramification.py, restated here so the rig is standalone).
# ---------------------------------------------------------------------------

def prime_factors(n):
    n = abs(n)
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def vp(n, p):
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a, n


def legendre(u, p):
    u %= p
    if u == 0:
        return 0
    return 1 if pow(u, (p - 1) // 2, p) == 1 else -1


def hilbert_odd(a, b, p):
    al, u = vp(a, p)
    be, v = vp(b, p)
    s = 1
    if (al * be * ((p - 1) // 2)) % 2:
        s = -s
    if be % 2:
        s *= legendre(u, p)
    if al % 2:
        s *= legendre(v, p)
    return s


def hilbert_2(a, b):
    al, u = vp(a, 2)
    be, v = vp(b, 2)
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = eps(u) * eps(v) + al * om(v) + be * om(u)
    return -1 if e % 2 else 1


def hilbert_inf(a, b):
    return -1 if (a < 0 and b < 0) else 1


def ramification_set(a, b):
    """Finite ramified places + infinity flag; asserts reciprocity."""
    odd_places = sorted(set(p for p in prime_factors(a * b) if p != 2))
    fin = []
    prodall = hilbert_inf(a, b) * hilbert_2(a, b)
    if hilbert_2(a, b) == -1:
        fin.append(2)
    for p in odd_places:
        s = hilbert_odd(a, b, p)
        prodall *= s
        if s == -1:
            fin.append(p)
    assert prodall == 1, "Hilbert reciprocity violated -- formula bug"
    return sorted(fin), hilbert_inf(a, b) == -1


def is_squarefree(n):
    n = abs(n)
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return False
        d += 1
    return True


# ---------------------------------------------------------------------------
# F1: the product formula over Q, and the void visible constraint.
# ---------------------------------------------------------------------------

def run_f1():
    section("F1: PRODUCT FORMULA OVER Q -- the visible constraint is void")
    trials = 200
    primes_pool = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    bad = 0
    for _ in range(trials):
        support = random.sample(primes_pool, random.randint(1, 5))
        vec = {p: random.choice([-3, -2, -1, 1, 2, 3]) for p in support}
        x = Fraction(1)
        for p, a in vec.items():
            x *= Fraction(p) ** a
        # reprint the valuations of the constructed rational
        num, den = x.numerator, x.denominator
        for p in primes_pool:
            want = vec.get(p, 0)
            got = vp(num, p)[0] - vp(den, p)[0]
            if got != want:
                bad += 1
        # full product formula: finite |x|_p times archimedean |x|
        prod = Fraction(1)
        for p in prime_factors(num) + prime_factors(den):
            prod *= Fraction(p) ** (-(vp(num, p)[0] - vp(den, p)[0]))
        prod *= abs(x)
        if prod != 1:
            bad += 1
    print(f"trials: {trials}  valuation-reprint or product failures: {bad}")
    assert bad == 0


# ---------------------------------------------------------------------------
# F2: the function-field control -- F_2(t), deleted place NOT archimedean.
# Polynomials over F_2 as bitmasks (bit i = coefficient of t^i).
# ---------------------------------------------------------------------------

def pdeg(f):
    return f.bit_length() - 1


def pmul(f, g):
    r = 0
    while g:
        if g & 1:
            r ^= f
        f <<= 1
        g >>= 1
    return r


def pdivmod(f, g):
    q = 0
    dg = pdeg(g)
    while pdeg(f) >= dg and f:
        sh = pdeg(f) - dg
        q ^= 1 << sh
        f ^= g << sh
    return q, f


def irreducibles_f2(maxdeg):
    """All irreducible polynomials over F_2 of degree 1..maxdeg."""
    irr = []
    for f in range(2, 1 << (maxdeg + 1)):
        if pdeg(f) < 1:
            continue
        ok = True
        for g in irr:
            if 2 * pdeg(g) > pdeg(f):
                break
            if pdivmod(f, g)[1] == 0:
                ok = False
                break
        if ok:
            irr.append(f)
    return irr


def poly_valuation(f, g):
    """v_g(f) for polynomials, f nonzero."""
    a = 0
    while True:
        q, r = pdivmod(f, g)
        if r != 0:
            return a, f
        f = q
        a += 1


def run_f2():
    section("F2: F_2(t) CONTROL -- the deleted place is not archimedean")
    irr = irreducibles_f2(8)
    trials = 200
    visible_sums = set()
    bad = 0
    for _ in range(trials):
        num = random.randint(1, (1 << 7) - 1)
        den = random.randint(1, (1 << 7) - 1)
        # full sum over finite places
        s = 0
        for g in [h for h in irr if pdeg(h) <= max(pdeg(num), pdeg(den))]:
            s += pdeg(g) * (poly_valuation(num, g)[0] - poly_valuation(den, g)[0])
        v_inf = pdeg(den) - pdeg(num)  # the degree place, deg 1
        if s + v_inf != 0:
            bad += 1
        visible_sums.add(s)
    # constructive leg (mirror of F1): f = t^k realizes visible sum k
    constructed = []
    for k in range(-8, 9):
        num = 1 << max(k, 0)
        den = 1 << max(-k, 0)
        s = 0
        for g in [h for h in irr if pdeg(h) <= max(pdeg(num), pdeg(den))]:
            s += pdeg(g) * (poly_valuation(num, g)[0] - poly_valuation(den, g)[0])
        constructed.append(s == k)
    print(f"trials: {trials}  full-sum failures: {bad}")
    print(f"visible sums sampled: {sorted(visible_sums)}")
    print(f"constructed t^k realizes k for k in [-8,8]: {all(constructed)}")
    assert bad == 0 and all(constructed)


# ---------------------------------------------------------------------------
# F3: the Brauer 2-torsion budget -- one bit, and it is the infinite place's.
# ---------------------------------------------------------------------------

def run_f3():
    section("F3: QUATERNION SWEEP -- the visible parity is the deleted bit")
    # positive control: the four recorded specimens reprint
    control = [
        ((5, 3), [3, 5], False),
        ((77, -1), [7, 11], False),
        ((-1, -1), [2], True),
        ((-3, -1), [3], True),
    ]
    for (a, b), want_fin, want_inf in control:
        fin, at_inf = ramification_set(a, b)
        print(f"control ({a},{b}): visible {fin} inf {at_inf}")
        assert fin == want_fin and at_inf == want_inf, "positive control failed"
    print("positive control: 4/4 reprint")

    vals = [n for n in range(-30, 31) if n != 0 and is_squarefree(n)]
    pairs = 0
    odd_visible = 0
    mismatches = 0
    for a in vals:
        for b in vals:
            fin, at_inf = ramification_set(a, b)  # asserts reciprocity
            pairs += 1
            odd = len(fin) % 2 == 1
            if odd:
                odd_visible += 1
            if odd != at_inf:
                mismatches += 1
    print(f"pairs swept: {pairs}  parity mismatches: {mismatches}")
    print(f"odd visible sets: {odd_visible}  even: {pairs - odd_visible}")
    assert mismatches == 0 and 0 < odd_visible < pairs


def run_f4():
    section("F4: BRAUER ODD TORSION -- the transplant dies by hand")
    print("Br(R) = {0, 1/2} (Frobenius). An odd-degree cyclic algebra's")
    print("invariants live in (1/n)Z/Z, which contains no 1/2, so the")
    print("finite invariants must sum to 0 EXACTLY: deletion buys odd")
    print("torsion nothing. The quaternion knob is the whole knob.")
    print("(Property + classical -- Albert-Brauer-Hasse-Noether; stated,")
    print("not computed.)")


# ---------------------------------------------------------------------------
# F5-F7: the threshold route -- the square ladder against residue windows.
# ---------------------------------------------------------------------------

def two_square_direct(n):
    a = 0
    while a * a <= n:
        r = n - a * a
        s = int(r ** 0.5)
        if any((s + d) ** 2 == r for d in (-1, 0, 1) if s + d >= 0):
            return True
        a += 1
    return False


def three_square_direct(n):
    a = 0
    while a * a <= n:
        if two_square_direct(n - a * a):
            return True
        a += 1
    return False


def run_f5():
    section("F5: PER-CHANNEL TOTALITY -- the survivors are invisible at precision 1")
    for p in RAD:
        sq = set((x * x) % p for x in range(p))
        reach2 = set((s + t) % p for s in sq for t in sq)
        print(f"channel {p}: two-square residues {len(reach2)}/{p}")
        assert len(reach2) == p
    sq8 = set((x * x) % 8 for x in range(8))
    reach3_mod8 = set((a + b + c) % 8 for a in sq8 for b in sq8 for c in sq8)
    missing = sorted(set(range(8)) - reach3_mod8)
    print(f"squares mod 8: {sorted(sq8)}  three-square sums miss: {missing}")
    assert missing == [7]


def run_f6():
    section("F6: THE LADDER OVER Z -- exhaustive to N = 20000, direct search")
    N = 20000
    squares = set(x * x for x in range(int(N ** 0.5) + 2) if x * x <= N)
    s2 = [False] * (N + 1)
    for n in range(N + 1):
        s2[n] = any((n - q) in squares for q in squares if q <= n)
    s3 = [False] * (N + 1)
    for n in range(N + 1):
        s3[n] = any(s2[n - q] for q in squares if q <= n)
    s4 = [False] * (N + 1)
    for n in range(N + 1):
        s4[n] = any(s3[n - q] for q in squares if q <= n)

    def two_square_char(n):
        if n == 0:
            return True
        for p in prime_factors(n):
            if p % 4 == 3 and vp(n, p)[0] % 2 == 1:
                return False
        return True

    def three_square_char(n):
        while n % 4 == 0 and n > 0:
            n //= 4
        return n % 8 != 7

    bad2 = sum(1 for n in range(N + 1) if s2[n] != two_square_char(n))
    bad3 = sum(1 for n in range(N + 1) if s3[n] != three_square_char(n))
    bad4 = sum(1 for n in range(N + 1) if not s4[n])
    print(f"N = {N}")
    print(f"two-square char mismatches:   {bad2}")
    print(f"three-square char mismatches: {bad3}")
    print(f"four-square failures:         {bad4}")
    assert bad2 == 0 and bad3 == 0 and bad4 == 0


def run_f7():
    section("F7: THE INVISIBLE PAIRS -- same residue at every channel, opposite verdict")
    # two squares: aim with the characterization, verify by direct search
    n0 = 3
    pair2 = None
    for k in range(1, 60):
        n1 = n0 + k * M_RAD
        ok = True
        for p in prime_factors(n1):
            if p % 4 == 3 and vp(n1, p)[0] % 2 == 1:
                ok = False
                break
        if ok:
            pair2 = (n0, n1)
            break
    assert pair2 is not None, "no two-square pair in range -- threshold kill fires"
    a, b = pair2
    va, vb = two_square_direct(a), two_square_direct(b)
    print(f"two squares:   n = {a} (direct: {va})  n' = {b} (direct: {vb})")
    print(f"               n' - n = {b - a} = {(b - a) // M_RAD} * 510510")
    assert va is False and vb is True and (b - a) % M_RAD == 0

    # three squares: the hand-derived pair
    a, b = 7, 7 + M_RAD
    va, vb = three_square_direct(a), three_square_direct(b)
    print(f"three squares: n = {a} (direct: {va})  n' = {b} (direct: {vb})")
    print(f"               {b} mod 8 = {b % 8} (7 mod 8 = 7)")
    assert va is False and vb is True

    print("four squares:  total -- no condition survives at the threshold,")
    print("               so no pair exists (F6's zero failures).")


if __name__ == "__main__":
    run_f1()
    run_f2()
    run_f3()
    run_f4()
    run_f5()
    run_f6()
    run_f7()
    print()
    print("ALL CHECKS PASSED")
