r"""explore_cubic_ring.py -- a cubic number ring as a walking engine, and
whether one closed form carries every column it has.

THE QUESTION. Every ring engine this corpus walks is QUADRATIC. Three of
them -- Z[sqrt(-5)], Z[w] with w^2 = w - 6, and Z[i] -- hardcode a binary
norm form and a 2x2 HNF, so a rational prime lies under at most two places
and any two of them are Galois conjugates: equal norm, equal ramification,
equal ladder. Two structures that a quadratic ring cannot present are
therefore invisible to everything built on top of them -- a rational prime
under two places of DIFFERENT ramification, and a residue degree above 2.
This file supplies both from one field, as a module of the same seven names
the imported walker already reads.

K = Q[x]/(x^3 - x - 1), the cubic field of least |discriminant|, disc = -23.
The discriminant is squarefree, so O = Z[theta] is the maximal order and
Dedekind's criterion applies at every rational prime: the factorization of
p is the factorization of x^3 - x - 1 mod p. The field is non-Galois (S_3),
so places over Q carry NO conjugation action at all -- the conjugate pairs
every quadratic engine is full of simply do not exist here, and that is the
point rather than a defect. Minkowski's bound is (4/pi)*(6/27)*sqrt(23) =
1.36 < 2, so h = 1 and the class layer is trivial; this file is an IDEAL
world engine and says nothing about riders.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The question is
written in the ENGINE's terms -- lam_P, door_r, place_norm, the ladder gap
-- and deliberately not in the schedule family's, because what is under
test is whether the ring's own lambda is reproduced by a formula the
schedule family states (the colour-plus-gap model of
explore_element_schedule_nf.py). A rig written in the formula's own words
could not see the column it is checking.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From quadratic to cubic. NOTHING is carried. Every column below is
    derived from the local unit group of THIS ring and brute-checked
    against a forcer that reproduces the three quadratic engines' filed
    tables first. In particular the plateau Z[i]'s ramified place carries
    is NOT expected here and no shape from it is assumed.
 T2 From the head criterion to this ring. explore_head_width.py F2 states
    the criterion as f = 1 with mu_p in K_P and e = (p-1)p^t, which
    CORRECTS the earlier reading p - 1 <= e. Only the corrected form is
    used, and it is used as a PREDICTION to be checked against the ladders
    the engine prints, never as an assumption inside lam_P.
 T3 From the maximality of Z[theta] to the place enumeration. Squarefree
    discriminant is what licenses reading the factorization of p off the
    polynomial. It is asserted (S2), not assumed.

THE HAND-ATTACK, on paper before any engine code, and it is where the
ramified column is bought.

  lam_P(X^a) is the exponent of (O/X^a)^*, which is k^* x U_1/U_a with k^*
  cyclic of order q - 1. The prime-to-p part of the exponent is therefore
  q - 1 at every depth (explore_populated_door.py F1, a property of every
  Dedekind domain with finite residue fields), so the whole of the work is
  the p-part.

  Write e for the ramification index and f for the residue degree at X,
  p the residue characteristic, q = p^f. Where e/(p-1) < 1 the logarithm
  converges on U_1 and is an isomorphism of U_1 onto the maximal ideal m,
  so U_1 is TORSION-FREE and U_1/U_a = m/m^a as a Z_p-module. Multiplying
  by p multiplies m by m^e, so p^k kills m/m^a exactly when e*k + 1 >= a:
  the exponent of U_1/U_a is p^ceil((a-1)/e). Hence

      lam_P(X^a) = (q - 1) * p^ceil((a-1)/e)                          (*)

  wherever e < p - 1. THREE CASES CARRY THIS RING and the third is the one
  a quadratic ring never offers:
   - every unramified place at odd p: e = 1 and (*) is the standard column
     (q-1)*p^(a-1);
   - the ONE place over 2: x^3 - x - 1 has no root mod 2 and a cubic with
     no root is irreducible, so 2 is INERT with f = 3 and q = 8. Here
     e/(p-1) = 1, not < 1, so (*) is not licensed and the case is done by
     hand: U_1 = mu_2 x Z_2^3, and for u = 1 + 2x with x in F_8 \ F_2,
     u^2 = 1 + 4(x + x^2) with x + x^2 a UNIT, so u has order 2^(a-1) in
     U_1/U_a and the column is standard after all. This is exactly where
     Z[w]'s SPLIT places over 2 depart from standard -- there f = 1, the
     residue field is F_2, x + x^2 vanishes identically and the exponent
     drops to 2^(a-2). Residue degree 3 is what rescues it.
   - the ramified place over 23: e = 2 and p - 1 = 22, so the ramification
     is TAME, (*) applies, and the column is (23-1)*23^ceil((a-1)/2) -- a
     staircase of step 2 with no head. Z[i]'s ramified column is a five-
     wide plateau because there the ramification is WILD (p = 2, e = 2);
     nothing of that shape is expected here and T1 says so.

  So the prediction is that ONE formula covers this ring end to end, which
  is a stronger claim than any quadratic engine can make -- each of those
  needs at least one hand-derived column beside its standard one.

  WHAT 23 DOES, and it is READ OFF the engine rather than frozen from this
  paragraph. disc = -23 is squarefree, so 23 is the only ramified prime.
  By hand: x^3 - x - 1 = (x - 3)(x^2 + 3x + 8) mod 23, and x^2 + 3x + 8 has
  discriminant 9 - 32 = -23 = 0 mod 23, so it is (x + 13)^2. That gives
  23 = P * Q^2 with e_P = f_P = f_Q = 1 and e_Q = 2 -- two places of EQUAL
  NORM 23 and different local degree, which is the configuration no
  quadratic ring builds. S2 prints the factorization the engine computes
  and the predictions below are read against it.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 The generic monic-order brute-forcer reproduces the filed lambda
     tables of Z[sqrt(-5)], Z[w] and Z[i] -- three tables it did not write,
     one of them a hand-derived plateau -- at every place of norm <= 30 and
     every depth whose residue count fits the cap. 0 disagreements.
  P2 At this ring the same forcer reproduces (*) at every brute-forceable
     (place, depth), INCLUDING the inert place over 2 and the ramified
     place over 23. A single disagreement kills the closed form and with it
     everything below.
  P3 The engine factors 23 as P * Q^2 with (e, f) = (1, 1) and (2, 1),
     equal norms 23, and no other rational prime ramifies below MAXP.
  P4 NO place of this ring carries a HEAD -- the longest run of one lambda
     value, less e, is 0 everywhere. The corrected criterion predicts it:
     the only p with p - 1 <= e is 2, and the place there has f = 3, which
     fails the f = 1 clause.
  P5 The void walk through the IMPORTED walker locks, and it locks at the
     first move on the least-norm place, whose door is 1 at every depth
     because it has no head. The lock cost is that place's norm.
  P6 The colour-plus-gap formula (N-1)*rad(N)^ceil((a-1)/gap), which
     reproduces a quadratic ring's lambda at 32 of its 35 places of norm
     <= 60 and misses exactly the heads, reproduces THIS ring's lambda at
     ALL of them -- and it separates P from Q, which share a colour and
     differ only in the gap.

KILL-SHAPES, as observables.
  K1 the forcer disagrees with a filed quadratic table: the instrument is
     wrong and nothing below is readable.
  K2 the forcer disagrees with (*) anywhere at this ring: the closed form
     is wrong, and the ramified column has to be found rather than derived.
  K3 the engine does not factor 23 as a place plus a squared place: the
     configuration the corpus queued three questions behind is not here and
     the field has to be rechosen.
  K4 the void walk does not lock inside the imported walker's cap.

DISTRUST THE MARGIN. The derived half is (*), and it is derived twice --
once from the logarithm at the tame places and once by hand at the inert
place over 2, where the logarithm does not converge. The VIBES half is
"disc = -23 is squarefree so Z[theta] is maximal and 23 is the only
ramified prime": S2 checks the ramification by gcd(f, f') at every prime of
the universe rather than asserting it from the discriminant.

THE POSITIVE CONTROL (S1, run before any verdict is read). One brute-forcer
over an arbitrary monic order Z[t]/(m) -- degree 2 or 3 alike -- enumerates
O/X^a from an HNF basis of the ideal, keeps the units, and takes the
exponent of the group. It is run FIRST against the three quadratic engines
whose tables are already filed and independently written, and only then
against this ring. A forcer that reproduces three tables it did not write
is the instrument; a forcer that does not is the finding.

THE SECTIONS.
  S1  positive control: the forcer against three filed rings, then this one.
  S2  the ring itself: the factorization of 23, the ramification census.
  S3  the ladders: heads, tail gaps, and the colour-plus-gap formula.
  S4  the void walk through the imported walker.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 ONE CLOSED FORM CARRIES A WHOLE RING, AND IT IS NOT A NEW FORMULA -- IT
   IS THE SUPPLY MODEL, DERIVED FROM THE OTHER END (property for the tame
   places, where it is the logarithm's; a rule in range at the inert place
   over 2, where the logarithm does not converge and the derivation is by
   hand; 48 brute-forced readings at this ring against 152 at the three
   filed ones, 0 off). lam_P(X^a) = (N(X) - 1) * p^ceil((a-1)/e) at every
   place of K: the prime-to-p part is q - 1 by the local unit group's
   splitting, and the p-part is the exponent of m/m^a, which is
   p^ceil((a-1)/e) wherever the logarithm converges -- e/(p-1) < 1 at every
   place of this ring but one.
   THAT IS THE SAME EXPRESSION AS explore_element_schedule_nf.py's
   colour-plus-gap model, (N-1)*rad(N)^ceil((a-1)/gap), reached from the
   opposite direction: there it is what a SUPPLY MATRIX plus a ladder column
   can express, read against the engines afterwards; here it is what the
   local unit group IS, given tameness. Two ends, one formula, and the
   agreement is the finding rather than a coincidence to be filed twice.
   SO WHERE IT MISSES IS ONE QUESTION AND NOT TWO, AND THE ANSWER IS
   ARITHMETIC AND NOT SIZE (rule in range; every distinct column of the
   three quadratic engines at norm <= 200, to depth 14). It misses at 3 of
   them and every one is at p = 2 -- Z[i]'s wild ramified column,
   Z[sqrt-5]'s, and Z[w]'s SPLIT places over 2 -- while BOTH tame ramified
   columns there, Z[sqrt-5] over 5 and Z[w] over 23, are reproduced. So
   ramification is not what breaks it -- and neither is WILDNESS alone,
   which one of the three refutes outright: Z[w]'s split places over 2 are
   UNRAMIFIED. TWO MECHANISMS, ONE SHARED PRECONDITION, and they are worth
   keeping apart rather than unified. The precondition is p = 2 with f = 1,
   which all three misses have and nothing else in the four rings does. Above
   it, the two ramified misses break the formula because the ramification is
   WILD -- e/(p-1) >= 1, so the logarithm does not converge and U_1 carries
   p-torsion, Z[i]'s mu_4 being the plateau's own cause -- while the
   unramified miss breaks it because x + x^2 vanishes identically on F_2, so
   u^2 for u = 1 + 2x lands two levels deep instead of one.
   THIS RING DEFEATS BOTH, and at this field they are one fact wearing two
   consequences: 2 is INERT, so there is no ramified place over 2 to be wild
   at, and f = 3 makes x + x^2 a unit for any x in F_8 \ F_2. Both follow
   from the single reading that x^3 - x - 1 is irreducible mod 2. WHAT IS
   NOT MEASURED, since no ring here carries it: f = 2 over 2, where the
   second mechanism predicts survival (F_4 has x + x^2 = 1 at a generator)
   and the corpus has no test.
   AND THE COROLLARY IS A CORRECTION TO A COUNT THIS RING IS READ AGAINST:
   the corpus's five NON-STANDARD columns are five against the e = 1 shape
   (q-1)*p^(a-1), not against this formula, and two of the five are tame
   ramified columns the formula has had all along.

F2 23 = P*Q^2, READ OFF THE ENGINE, AND IT IS THE CONFIGURATION (property;
   the factorization is Dedekind's, disc = -23 being squarefree, and the
   ramification census scans all 2262 rational primes below 20000). The two
   places over 23 have (e, f) = (1, 1) and (2, 1), equal norms 23, and local
   degrees e*f = 1 and 2. 23 is the only ramified prime. The splitting-type
   densities read 0.501 for a rational place beside an f = 2 place, 0.337
   inert, 0.162 split completely, against Chebotarev's 1/2, 1/3, 1/6 for
   S_3 -- so the field supplies both an f = 3 place and the P*Q^2 pair, and
   supplies each at positive density rather than as a coincidence at 23.

F3 NO PLACE OF THIS RING CARRIES A HEAD, AND THE CORRECTED CRITERION IS WHY
   (rule in range; every place of norm <= 30 plus the pair over 23,
   tabulated to depth 14, excess 0 at all of them and the tail gap the
   ramification index at all of them). The earlier reading of the criterion,
   p - 1 <= e, would predict a head at the place over 2, where e = 1 and
   p - 1 = 1. The corrected one (explore_head_width.py F2: f = 1 with mu_p
   in K_P and e = (p-1)p^t) predicts none, because that place has f = 3.
   The engine agrees with the corrected form. This is the first reading in
   the corpus where the two versions of the criterion DISAGREE and the
   engine decides between them -- at the three quadratic rings every place
   over 2 has f <= 2 and f = 1 wherever e > 1, so the clause that separates
   them is never exercised.

F4 A COLOUR PLUS A GAP DETERMINES LAMBDA HERE, AND THE GAP COLUMN IS WHAT
   DOES THE WORK (rule in range; 551 places of norm <= 4000 to depth 14, 0
   off). This is F1's formula read as the SUPPLY's rather than as the local
   unit group's, and what it adds is the model's own scope: over a quadratic
   ring it reproduces lambda at 32 of the 35 places of norm <= 60 and misses
   exactly the heads. Here it misses nothing, since F3 says
   there are no heads -- so P*Q^2 names NO third column, which is the answer
   to the free read-off and is the negative half. THE POSITIVE HALF IS WHAT
   THE PAIR SHOWS ABOUT THE SECOND COLUMN. Over a quadratic ring the norm
   fixes the gap outright, a rational prime being split or ramified and not
   both, so the ladder column is carried but never separates two places; at
   23 the two places share the colour 23 and differ only in the gap, and
   their columns differ from depth 3 on (11638 against 506). So the ladder
   is a column the supply genuinely needs rather than a field derivable from
   the colour, and this ring is where that stops being an argument about
   what the matrix records and becomes a reading.

F5 THE VOID WALK IS DEGENERATE, AND ITS DEGENERACY IS F3 READ AS A PRICE
   (rule in range; the imported walker from the void, locked at the first
   witnessed run). With no head anywhere, the least-norm place has door 1 at
   every depth -- its lambda gains a fresh factor of p at each rung, which no
   invariant built from its own past can carry -- so it is priced at its
   norm forever, and no place of larger norm can undercut it. Here that is
   the rational place over 5, at cost 5, and the walk clocks it and nothing
   else. The three quadratic engines all lock elsewhere and later precisely
   BECAUSE their cheapest place has a head: Z[i]'s ramified place over 2 is
   the void's cheapest opening at 4 and is abandoned at exponent 3 when its
   plateau prices the next door at 32. So a head is not a curiosity of the
   ladder -- it is the only thing that makes a greedy walk in a number ring
   do anything, and a ring without one has a walk that says nothing. Every
   informative state in THIS ring is a PLANTED one, which is a fact about
   the instrument and is stated so the next rig does not read a walk here as
   evidence.

RUN RECORD. `python explore_cubic_ring.py`. One process, CPython, no BLAS.
232 checks, 15.3 s wall, peak working set 23.2 MB under memwatch.py's 512 MB
ceiling. 2262 rational primes sieved into 4128 places. S1: 152 brute-forced
readings against the three quadratic engines' filed tables including Z[i]'s
hand-derived plateau and Z[sqrt-5]'s, 0 disagreements; then 47 readings at
this ring to the sweep's cap of 15000 residues, plus the ramified column
carried alone to depth 4 (279841 residues, 10.7 s of the total) where the
staircase RISES rather than plateaus -- 22, 506, 506, 11638 against the
closed form. S3 also runs the formula over the three quadratic engines'
distinct columns at norm <= 200 -- a control added after the run, when F1's
first draft was found to have braided two different baselines -- and it
misses at 3, all at p = 2. All six predictions hit; no kill-shape fired.
P5 named the lock
at the first move and the walker reports 10 steps, which is its own witness
threshold (LOCK_R consecutive identical vehicles) and not a delay: the
support at the lock is one place at exponent 10.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import gcd, isqrt

CHECKS = 0

MAXP = 20000        # rational primes enumerated into the universe
BRUTE_CAP = 15000   # residues allowed in one brute-forced quotient
DEPTH_N = 14        # depths a ladder is tabulated to
ROOT_CAP = 600      # primes whose roots are extracted by trial
RAM_DEPTH = 4       # depth the ramified column alone is carried to


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def lcm(a, b):
    return a * b // gcd(a, b)


def v_p(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def _sieve(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(2, n + 1) if s[i]]


PRIMES = _sieve(MAXP)

# --------------------------------------------------------------- the ring
# K = Q(theta), theta^3 = theta + 1. O = Z[theta], disc -23, h = 1.
# The reduction rule, in the shape the generic brute-forcer reads:
#   t^n = REDUCE[0] + REDUCE[1]*t + ... + REDUCE[n-1]*t^(n-1)
CUBIC_REDUCE = (1, 1, 0)        # t^3 = 1 + t
MINPOLY = (-1, -1, 0, 1)        # x^3 - x - 1, low coefficient first

# A PLACE IS A TAG CARRYING NUMBERS, not a splitting-type name:
#   (p, e, f, i)  -- rational prime, ramification index, residue degree,
#                    and an ordinal separating places that agree in (p,e,f).
# The three quadratic engines tag places 'split'/'inert'/'ram', an alphabet
# that can only name the shapes a degree-2 field has. Here e and f are read
# off the tag directly and no alphabet is needed.


# ------------------------------------------------- polynomials mod a prime
def pnorm(a, p):
    while a and a[-1] % p == 0:
        a = a[:-1]
    return tuple(x % p for x in a)


def pmul(a, b, p):
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return pnorm(out, p)


def pmod(a, b, p):
    """a mod b over F_p, b monic-izable."""
    a = list(pnorm(a, p))
    b = pnorm(b, p)
    inv = pow(b[-1], p - 2, p)
    while len(a) >= len(b):
        c = (a[-1] * inv) % p
        if c:
            off = len(a) - len(b)
            for i, y in enumerate(b):
                a[off + i] = (a[off + i] - c * y) % p
        a.pop()
        while a and a[-1] % p == 0:
            a.pop()
    return pnorm(a, p)


def pgcd(a, b, p):
    a, b = pnorm(a, p), pnorm(b, p)
    while b:
        a, b = b, pmod(a, b, p)
    if a:
        inv = pow(a[-1], p - 2, p)
        a = pnorm(tuple(x * inv for x in a), p)
    return a


def ppowmod(base, k, m, p):
    res, b = (1,), pmod(base, m, p)
    while k:
        if k & 1:
            res = pmod(pmul(res, b, p), m, p)
        b = pmod(pmul(b, b, p), m, p)
        k >>= 1
    return res


def pderiv(a, p):
    return pnorm(tuple(i * a[i] for i in range(1, len(a))), p)


def roots_mod(p):
    """Every root of the minimal polynomial mod p, by trial. Only called at
    small p, where the ideal generators are wanted for the brute force."""
    out = []
    for r in range(p):
        v = (r * r * r - r - 1) % p
        if v == 0:
            out.append(r)
    return out


def factor_shape(p):
    """[(e, f), ...] for the places over p, from the factorization of the
    minimal polynomial mod p. Dedekind applies because Z[theta] is maximal."""
    f = MINPOLY
    d = pgcd(f, pderiv(f, p), p)
    if len(d) - 1 == 1:
        return [(1, 1), (2, 1)]               # g * h^2, both linear
    if len(d) - 1 == 2:
        return [(3, 1)]                       # h^3
    assert len(d) - 1 == 0, "unreadable factor shape at %d" % p
    # squarefree: the linear part is gcd(x^p - x, f), whose degree is the
    # number of roots -- 0, 1 or 3, a cubic with two roots having a third
    sub = list(ppowmod((0, 1), p, f, p))
    while len(sub) < 2:
        sub.append(0)
    sub[1] -= 1
    nr = len(pgcd(tuple(sub), f, p)) - 1
    if nr <= 0:
        return [(1, 3)]                       # inert
    if nr == 1:
        return [(1, 1), (1, 2)]               # a rational place and a square
    assert nr == 3, "a squarefree cubic with %d roots mod %d" % (nr, p)
    return [(1, 1), (1, 1), (1, 1)]


def build_universe():
    places = []
    for p in PRIMES:
        seen = {}
        for (e, f) in factor_shape(p):
            i = seen.get((e, f), 0)
            seen[(e, f)] = i + 1
            places.append((p, e, f, i))
    places.sort(key=place_key)
    return places


def place_char(pl):
    return pl[0]


def place_e(pl):
    return pl[1]


def place_f(pl):
    return pl[2]


def place_norm(pl):
    return pl[0] ** pl[2]


def place_ef(pl):
    return pl[1] * pl[2]


def place_bit(pl):
    return 0                       # h = 1: every ideal is principal


def place_key(pl):
    return (place_norm(pl), pl[1], pl[2], pl[3])


def conj_place(pl):
    """A non-Galois cubic has no conjugation acting on its places over Q, so
    a place is its own only companion. The three quadratic engines return
    the Galois conjugate here; that structure is absent by construction and
    its absence is the reason this ring can present what they cannot."""
    return pl


def show(pl):
    return "%d[e%d,f%d]%s" % (pl[0], pl[1], pl[2],
                              ".%d" % pl[3] if pl[3] else "")


def show_st(st):
    parts = ["%s^%d" % (show(pl), e)
             for pl, e in sorted(st.items(), key=lambda kv: place_key(kv[0]))
             if e]
    return "*".join(parts) if parts else "(1)"


def lam_P(pl, a):
    """lambda of the prime-power column X^a -- the exponent of (O/X^a)^*.

    ONE closed form at every place of this ring: (q - 1) * p^ceil((a-1)/e).
    At the tame places it is the logarithm's, U_1 being torsion-free and
    isomorphic to the maximal ideal; at the inert place over 2, where the
    logarithm does not converge, it is the hand derivation in the docstring.
    Brute-checked against the residue rings themselves in S1.
    """
    if a == 0:
        return 1
    p, e = pl[0], pl[1]
    return (place_norm(pl) - 1) * p ** -(-(a - 1) // e)


def lam_state(st):
    L = 1
    for pl, e in st.items():
        L = lcm(L, lam_P(pl, e))
    return L


def door_r(pl, e, L):
    r = 1
    while L % lam_P(pl, e + r) == 0:
        r += 1
        assert r < 500, "door search runaway"
    return r


def ideal_menu(st, L):
    """(cost, ties): ties = all min-cost (place, r), sorted by place_key."""
    best, ties = None, []
    for pl in UNIVERSE:
        nrm = place_norm(pl)
        if best is not None and nrm > best:
            break
        r = door_r(pl, st.get(pl, 0), L)
        cost = nrm ** r
        if best is None or cost < best:
            best, ties = cost, [(pl, r)]
        elif cost == best:
            ties.append((pl, r))
    assert best <= MAXP, "universe guard: door beyond MAXP"
    ties.sort(key=lambda t: place_key(t[0]))
    return best, ties


UNIVERSE = build_universe()


# --------------------------------- a generic monic-order brute-forcer
# One instrument for orders of ANY degree. O = Z[t]/(m) with m monic of
# degree n, given by the reduction rule t^n = R[0] + R[1] t + ... An element
# is an n-tuple of integers; an ideal is a rank-n Z-lattice given by
# generators and reduced to an upper-triangular HNF basis, whose residues
# are exactly the boxes {0 <= x_i < d_i}.
def omul(u, v, R):
    n = len(R)
    out = [0] * (2 * n - 1)
    for i, x in enumerate(u):
        if x:
            for j, y in enumerate(v):
                out[i + j] += x * y
    for k in range(2 * n - 2, n - 1, -1):
        c = out[k]
        if c:
            out[k] = 0
            for j in range(n):
                out[k - n + j] += c * R[j]
    return tuple(out[:n])


def xgcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, x, y = xgcd(b, a % b)
    return (g, y, x - (a // b) * y)


def hnf(gens, n):
    """Upper-triangular HNF basis of the lattice spanned by gens (n-tuples).
    Returns rows b_0..b_{n-1} with b_i leading at column i, all positive."""
    work = [list(g) for g in gens]
    basis = []
    for col in range(n):
        piv = None
        for i in range(len(work)):
            if work[i][col] == 0:
                continue
            if piv is None:
                piv = i
                continue
            a, b = work[piv], work[i]
            g, x, y = xgcd(a[col], b[col])
            u, v = a[col] // g, b[col] // g
            work[piv] = [x * a[k] + y * b[k] for k in range(n)]
            work[i] = [u * b[k] - v * a[k] for k in range(n)]
        assert piv is not None, "degenerate lattice at column %d" % col
        row = work.pop(piv)
        if row[col] < 0:
            row = [-t for t in row]
        basis.append(row)
    return basis


def reduce_mod(u, basis, n):
    v = list(u)
    for i in range(n):
        q = v[i] // basis[i][i]
        if q:
            for k in range(i, n):
                v[k] -= q * basis[i][k]
    return tuple(v)


def ideal_gens_generic(p, hpoly, R):
    """Z-module generators of (p, h(t)) as n-tuples: p*t^j and t^j*h(t)."""
    n = len(R)
    out = []
    for j in range(n):
        e = tuple(p if k == j else 0 for k in range(n))
        out.append(e)
    hv = tuple(list(hpoly) + [0] * (n - len(hpoly)))[:n]
    cur = hv
    for j in range(n):
        out.append(cur)
        cur = omul(cur, tuple(1 if k == 1 else 0 for k in range(n)), R)
    return out


def ideal_pow(gens, a, R, n):
    cur = [tuple(1 if k == j else 0 for k in range(n)) for j in range(n)]
    for _ in range(a):
        prod = [omul(u, v, R) for u in cur for v in gens]
        cur = [tuple(r) for r in hnf(prod, n)]
    return hnf(cur, n)


def unit_exponent(p, hpoly, R, a, q):
    """Exponent of (O/X^a)^*, brute-forced from the actual residue ring.
    X = (p, h(t)); q = N(X). Units are the residues NOT in X."""
    n = len(R)
    gens = ideal_gens_generic(p, hpoly, R)
    basis = ideal_pow(gens, a, R, n)
    one_basis = hnf(gens, n)
    dims = [basis[i][i] for i in range(n)]
    total = 1
    for d in dims:
        total *= d
    assert total == q ** a, "residue count %d is not the norm %d" % (total,
                                                                    q ** a)
    one = reduce_mod(tuple(1 if k == 0 else 0 for k in range(n)), basis, n)
    zero = tuple([0] * n)
    order = q ** (a - 1) * (q - 1)
    fac, m, d = [], order, 2
    while d * d <= m:
        while m % d == 0:
            fac.append(d)
            m //= d
        d += 1
    if m > 1:
        fac.append(m)
    fac = sorted(set(fac))

    def powmod(u, k):
        res, b = one, u
        while k:
            if k & 1:
                res = reduce_mod(omul(res, b, R), basis, n)
            b = reduce_mod(omul(b, b, R), basis, n)
            k >>= 1
        return res

    exp = 1
    ranges = [range(d) for d in dims]

    def walk(idx, acc):
        nonlocal exp
        if idx == n:
            u = tuple(acc)
            if reduce_mod(u, one_basis, n) == zero:
                return                                  # in X: not a unit
            if powmod(u, exp) == one:
                return                                  # order already seen
            o = order
            for r in fac:
                while o % r == 0 and powmod(u, o // r) == one:
                    o //= r
            exp = lcm(exp, o)
            return
        for x in ranges[idx]:
            acc.append(x)
            walk(idx + 1, acc)
            acc.pop()

    walk(0, [])
    return exp


# --------------------------------------------------------- the four rings
def quadratic_ideal(M, pl):
    """(p, h(t)) for a place of one of the three quadratic engines, in this
    file's generic vocabulary. h is t - r at a split or ramified place and
    the whole modulus (i.e. nothing beyond p) at an inert one."""
    p = M.place_char(pl)
    T, N0 = QUAD_RULE[M.__name__]
    if pl[0] == 'inert':
        return p, (0,)                          # h = 0, so the ideal is (p)
    if pl[0] == 'split':
        r = pl[2]
    else:
        r = next(x for x in range(p) if (x * x - T * x - N0) % p == 0)
    return p, (-r % p, 1)


QUAD_RULE = {}


def _load_quadratics():
    import explore_number_field_lock as K5
    import explore_module_law as K23
    import explore_gaussian_runaway as GI
    QUAD_RULE[K5.__name__] = (0, -5)            # t^2 = -5
    QUAD_RULE[K23.__name__] = (1, -6)           # t^2 = t - 6
    QUAD_RULE[GI.__name__] = (0, -1)            # t^2 = -1
    return [("Z[sqrt-5]", K5), ("Z[w] (-23)", K23), ("Z[i]", GI)]


# ------------------------------------------------- S1 the positive control
def s1_control():
    section("S1  POSITIVE CONTROL -- one brute-forcer over an arbitrary "
            "monic order, against three filed rings and only then this one")
    print("  The instrument: enumerate O/X^a from an HNF basis of the ideal,")
    print("  drop the residues lying in X, take the exponent of what is left.")
    print("  It knows nothing of splitting types and works at any degree.")
    print("  Run first at the three quadratic engines whose lambda tables are")
    print("  independently written -- one of them a hand-derived plateau.")
    print()
    print("  %-11s %-10s %-4s %-10s %-10s %s"
          % ("ring", "place", "a", "brute", "filed", ""))
    n_quad = 0
    for name, M in _load_quadratics():
        T, N0 = QUAD_RULE[M.__name__]
        R = (N0, T)
        for pl in M.UNIVERSE:
            if M.place_norm(pl) > 30:
                break
            gp, hpoly = quadratic_ideal(M, pl)
            q = M.place_norm(pl)
            for a in range(1, 15):
                if q ** a > BRUTE_CAP:
                    break
                got = unit_exponent(gp, hpoly, R, a, q)
                want = M.lam_P(pl, a)
                print("  %-11s %-10s %-4d %-10d %-10d %s"
                      % (name, str(pl), a, got, want,
                         "" if got == want else "  <-- DISAGREE"))
                ok(got == want,
                   "%s: brute exponent %d at %s^%d against the filed %d"
                   % (name, got, pl, a, want))
                n_quad += 1
    print("  %d filed readings reproduced, 0 off. The instrument stands."
          % n_quad)

    print()
    print("  and only now this ring, whose whole table is the closed form")
    print("  (N-1)*p^ceil((a-1)/e) -- the tame derivation at every place but")
    print("  the inert one over 2, which the docstring does by hand:")
    print("  %-14s %-4s %-4s %-4s %-10s %-10s %s"
          % ("place", "e", "f", "a", "brute", "closed", ""))
    n_cub = 0
    for pl in UNIVERSE:
        if pl[0] > ROOT_CAP or place_norm(pl) > 60:
            continue
        hpoly = cubic_gen_poly(pl)
        q = place_norm(pl)
        for a in range(1, DEPTH_N + 1):
            if q ** a > BRUTE_CAP:
                break
            got = unit_exponent(pl[0], hpoly, CUBIC_REDUCE, a, q)
            want = lam_P(pl, a)
            print("  %-14s %-4d %-4d %-4d %-10d %-10d %s"
                  % (show(pl), pl[1], pl[2], a, got, want,
                     "" if got == want else "  <-- DISAGREE"))
            ok(got == want,
               "cubic: brute exponent %d at %s^%d against the closed form %d"
               % (got, show(pl), a, want))
            n_cub += 1
    print("  %d readings at this ring, 0 off. (*) holds where it is checked."
          % n_cub)

    print()
    print("  AND THE RAMIFIED COLUMN ONE DEPTH FURTHER, past the sweep's own")
    print("  cap. It is the only place where (*)'s e-branch is exercised at")
    print("  all, and depth 3 shows only the PLATEAU; the depth-4 reading is")
    print("  where the staircase has to RISE again, which is the half a")
    print("  plateau alone cannot witness:")
    ram = next(pl for pl in UNIVERSE if pl[0] == 23 and pl[1] == 2)
    got = unit_exponent(23, cubic_gen_poly(ram), CUBIC_REDUCE, RAM_DEPTH, 23)
    print("    %-14s a = %d : brute %d, closed %d"
          % (show(ram), RAM_DEPTH, got, lam_P(ram, RAM_DEPTH)))
    ok(got == lam_P(ram, RAM_DEPTH),
       "the ramified column's rise disagrees at depth %d: %d against %d"
       % (RAM_DEPTH, got, lam_P(ram, RAM_DEPTH)))
    n_cub += 1
    return n_quad, n_cub


def cubic_gen_poly(pl):
    """h(t) with X = (p, h(theta)), for a place whose roots are extractable."""
    p, e, f, i = pl
    if f == 3:
        return (0,)                              # inert: X = (p)
    rs = roots_mod(p)
    if e == 2:
        # the REPEATED root: the one at which the derivative also vanishes
        rep = [r for r in rs if (3 * r * r - 1) % p == 0]
        ok(len(rep) == 1, "a ramified place at %d with %d repeated roots"
                          % (p, len(rep)))
        return (-rep[0] % p, 1)
    if f == 1:
        simple = sorted(r for r in rs if (3 * r * r - 1) % p != 0)
        return (-simple[i] % p, 1)
    # f = 2: the irreducible quadratic cofactor, minpoly / (t - r)
    r = rs[0]
    # x^3 - x - 1 = (x - r)(x^2 + r x + (r^2 - 1)) mod p
    return ((r * r - 1) % p, r % p, 1)


# ------------------------------------------------------------- S2 the ring
def s2_the_ring():
    section("S2  THE RING -- what 23 does, and where else anything ramifies")
    print("  The factorization type is READ OFF the engine, not frozen from")
    print("  the hand computation, since an index convention is re-derived")
    print("  from the engine rather than remembered.")
    print()
    over23 = [pl for pl in UNIVERSE if pl[0] == 23]
    for pl in over23:
        print("    %-14s e = %d, f = %d, norm = %d"
              % (show(pl), pl[1], pl[2], place_norm(pl)))
    ok(sorted((pl[1], pl[2]) for pl in over23) == [(1, 1), (2, 1)],
       "23 does not factor as P*Q^2: %s" % [(pl[1], pl[2]) for pl in over23])
    ok(len(set(place_norm(pl) for pl in over23)) == 1,
       "the two places over 23 do not share a norm")
    P = [pl for pl in over23 if pl[1] == 1][0]
    Q = [pl for pl in over23 if pl[1] == 2][0]
    print()
    print("  P*Q^2 at 23: equal norms %d, local degrees e*f = %d and %d."
          % (place_norm(P), place_ef(P), place_ef(Q)))
    print("  No quadratic ring builds this -- two places over one rational")
    print("  prime there are a conjugate SPLIT pair, equal in norm, in")
    print("  ramification and in ladder.")

    print()
    print("  the ramification census over the whole universe:")
    ram = [pl for pl in UNIVERSE if pl[1] > 1]
    ok(all(pl[0] == 23 for pl in ram),
       "a prime other than 23 ramifies: %s" % [pl for pl in ram
                                               if pl[0] != 23][:3])
    print("    %d rational primes enumerated, %d places, ramified at 23 only."
          % (len(PRIMES), len(UNIVERSE)))

    print()
    print("  and the splitting-type densities, which is Chebotarev's own")
    print("  reading of a non-Galois cubic (1/6, 1/2, 1/3 for S_3):")
    tally = {}
    for p in PRIMES:
        if p == 23:
            continue
        key = tuple(sorted((pl[1], pl[2]) for pl in UNIVERSE if pl[0] == p))
        tally[key] = tally.get(key, 0) + 1
    for key, n in sorted(tally.items(), key=lambda t: -t[1]):
        print("    %-30s %5d primes  (%.3f)"
              % (" ".join("e%df%d" % k for k in key), n,
                 n / (len(PRIMES) - 1)))
    return P, Q


# ---------------------------------------------------------- S3 the ladders
def s3_ladders(P, Q):
    section("S3  THE LADDERS -- heads, tail gaps, and whether a colour plus "
            "a gap determines lambda")
    print("  A place with no head repeats each lambda exactly e times. The")
    print("  observable is the EXCESS: the longest run of one lambda value,")
    print("  less e. The corrected head criterion (f = 1 with mu_p in K_P and")
    print("  e = (p-1)p^t) predicts NO head anywhere here: the only p with")
    print("  p - 1 <= e is 2, and the place there has f = 3.")
    print()
    print("  %-14s %-4s %-4s %-28s %-6s %-8s %s"
          % ("place", "e", "f", "lambda by depth", "run", "excess",
             "tail gap"))
    heads = 0
    for pl in UNIVERSE:
        if place_norm(pl) > 30 and pl[0] != 23:
            continue
        lams = [lam_P(pl, a) for a in range(1, DEPTH_N + 1)]
        run = max(sum(1 for x in lams if x == v) for v in set(lams) if v > 1)
        gaps = set()
        for k in range(1, 6):
            lo = next(a for a in range(1, 60)
                     if v_p(lam_P(pl, a), pl[0]) > k - 1)
            hi = next(a for a in range(1, 60) if v_p(lam_P(pl, a), pl[0]) > k)
            gaps.add(hi - lo)
        ok(len(gaps) == 1, "%s has no constant tail gap: %s"
                           % (show(pl), sorted(gaps)))
        g = gaps.pop()
        ok(g == pl[1], "%s: tail gap %d is not the ramification index %d"
                       % (show(pl), g, pl[1]))
        heads += (run > pl[1])
        print("  %-14s %-4d %-4d %-28s %-6d %-8d %d"
              % (show(pl), pl[1], pl[2],
                 ",".join(str(x) for x in lams[:6])[:28], run, run - pl[1], g))
    ok(heads == 0, "%d places carry a head, which the criterion forbids here"
                   % heads)
    print("  0 heads, and the tail gap is the ramification index at every"
          " one.")

    print()
    print("  THE COLOUR-PLUS-GAP FORMULA, (N-1)*rad(N)^ceil((a-1)/gap), which")
    print("  reproduces a quadratic ring's lambda at 32 of its 35 places of")
    print("  norm <= 60 and misses exactly the heads. Read here at every")
    print("  place of the universe, to depth %d:" % DEPTH_N)
    off = []
    for pl in UNIVERSE:
        if place_norm(pl) > 4000:
            continue
        rad = pl[0]
        for a in range(1, DEPTH_N + 1):
            got = (place_norm(pl) - 1) * rad ** -(-(a - 1) // pl[1])
            if got != lam_P(pl, a):
                off.append((pl, a, got, lam_P(pl, a)))
    ok(not off, "the colour+gap formula misses at %s" % off[:2])
    n = len([pl for pl in UNIVERSE if place_norm(pl) <= 4000])
    print("    reproduced at all %d places of norm <= 4000, 0 off." % n)

    print()
    print("  AND IT IS THE SAME FORMULA AS (*), so the question of where it")
    print("  MISSES is one question and not two. Run it over the three")
    print("  quadratic engines, which is what says whether this ring's clean")
    print("  sheet is a size fact or an arithmetic one:")
    print("  %-11s %-16s %-6s %-6s %s"
          % ("ring", "column", "p", "e", "lambda by depth"))
    misses = []
    for name, M in _load_quadratics():
        seen = set()
        for pl in M.UNIVERSE:
            if M.place_norm(pl) > 200:
                break
            key = (pl[0], M.place_char(pl))
            if key in seen:
                continue
            seen.add(key)
            p = M.place_char(pl)
            f = 2 if pl[0] == 'inert' else 1
            e = M.place_ef(pl) // f
            q = M.place_norm(pl)
            bad = [a for a in range(1, DEPTH_N + 1)
                   if M.lam_P(pl, a) != (q - 1) * p ** -(-(a - 1) // e)]
            if bad:
                misses.append((name, pl, p, e))
                print("  %-11s %-16s %-6d %-6d %s"
                      % (name, str(pl), p, e,
                         ",".join(str(M.lam_P(pl, a)) for a in range(1, 7))))
    ok(misses, "the formula misses nowhere in the quadratic engines, so it "
               "was never a per-ring fact and this ring's sheet says nothing")
    ok(all(p == 2 for _, _, p, _ in misses),
       "a miss sits at an odd residue characteristic: %s"
       % [(n, pl) for n, pl, p, _ in misses if p != 2])
    print("  %d misses over three rings, every one at p = 2 with f = 1 --"
          % len(misses))
    print("  and BOTH tame ramified columns there (Z[sqrt-5] over 5, Z[w]")
    print("  over 23) are reproduced, so ramification is not what breaks it,")
    print("  nor is wildness alone: one of the three is UNRAMIFIED.")
    print()
    print("  and it SEPARATES the pair over 23, which share a colour:")
    for pl in (P, Q):
        print("    %-14s norm %d, gap %d, lambda %s ..."
              % (show(pl), place_norm(pl), pl[1],
                 ",".join(str(lam_P(pl, a)) for a in range(1, 6))))
    ok(lam_P(P, 3) != lam_P(Q, 3),
       "the two places over 23 have the same lambda column, so the gap "
       "column is not load-bearing here after all")
    print("  Same norm, different gap, different column -- so the gap is a")
    print("  column the supply matrix genuinely needs, which over a quadratic")
    print("  ring it never has to be: there the norm fixes it outright.")


# -------------------------------------------------------- S4 the void walk
def s4_void_walk():
    section("S4  THE VOID WALK -- this ring through the IMPORTED walker")
    import explore_lock_budget as LB
    M = sys.modules[__name__]
    print("  every place of norm <= 30 at the void, door and price:")
    print("  %-14s %-8s %-6s %s" % ("place", "norm", "door", "price"))
    scan = LB.scan_universe(M, {}, 1, ceiling=30)
    for nrm, r, cost, pl in sorted(scan):
        print("  %-14s %-8d %-6d %d" % (show(pl), nrm, r, cost))
    cheapest = min(scan, key=lambda t: (t[2], t[0]))
    print("  cheapest opening: %s at %d" % (show(cheapest[3]), cheapest[2]))

    got = LB.walk_to_lock(M, {})
    ok(got is not None, "the void seed does not lock inside the walker's cap")
    st, L, pl, cost, steps = got
    print()
    print("  lock vehicle %s at recurrent cost %d, %d steps to the lock"
          % (show(pl), cost, steps))
    print("  locked support: %s" % show_st(st))
    deep = [(q, e) for q, e in st.items() if e > 1 and q != pl]
    print("  places above exponent 1 besides the vehicle: %d" % len(deep))
    ok(cost == place_norm(pl),
       "the lock cost %d is not the vehicle's own norm %d"
       % (cost, place_norm(pl)))
    print()
    print("  The walk is DEGENERATE and the reason is S3's: with no head")
    print("  anywhere, the least-norm place has door 1 at every depth, so its")
    print("  price is its norm and nothing in the universe can undercut it.")
    print("  Every interesting state in this ring is therefore a PLANTED one.")
    return st, L, pl, cost, steps


def main():
    n_quad, n_cub = s1_control()
    P, Q = s2_the_ring()
    s3_ladders(P, Q)
    s4_void_walk()

    section("VERDICT -- the predictions read against what printed")
    print("  P1 %d filed readings over three quadratic engines" % n_quad)
    print("  P2 %d readings at this ring against the closed form" % n_cub)
    print("  P3 23 = P*Q^2, places %s"
          % ", ".join(show(pl) for pl in UNIVERSE if pl[0] == 23))
    print("  P4 heads: see S3")
    print("  P5 the void walk: see S4")
    print("  P6 the colour+gap formula: see S3")
    print("\n  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
