r"""explore_headed_cubic_walk.py -- the walk on the first classed, headed
cubic ring: K = Q[x]/(x^3 + 4x + 1), d = -283, h = 2, cheapest place
headed.

THE QUESTION. explore_cubic_field_shop.py found and certified the ring:
the first cubic field by |discriminant| with h > 1, whose cheapest place
(norm 2, e = 1, f = 1, completion Q_2) carries a head -- the one
configuration every walked ring so far lacks, a nontrivial class group
UNDER a headed cheapest place at degree 3. The shop stopped at the
ladders; this file walks. Three readings, each a deliverable on its own:
the SEED CENSUS through the imported walker (does the head hold any
lock, or do the walks degenerate the way the headless cubic's did --
explore_cubic_ring.py F5), the ELEMENT world at h = 2 (the element
price and the class tax at a ring where both places over 2 are
non-principal), and the WIDTH the image carries (whether a menu of this
ring ever presents a tie of multiplicity 3, the base the exhausted-image
law prices openings by, never yet seen in a number ring).

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The question
is written in the WALKER's terms -- lam_P, door, lock, tie, rider --
because what is under test is dynamics. The class layer enters only as
place bits certified by the class-field instruments (generator search,
exhausted unit-reduced box, relation kernel), the shop's vocabulary,
and the two are welded by cross-checks rather than shared assumptions.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From Z[sqrt(-5)]'s element world (explore_number_field_lock.py):
    the resonance, the free-rider/Charon mechanism, and the monobasin
    are STOREY-UP imports -- there the cheap bundle (2) = P2^2 is a
    RAMIFIED square and the tax refund is the resonance ord[P2] = e;
    here the candidate bundle P2^2 squares an UNRAMIFIED headed place
    and any refund is the head column's own step. The shapes are
    re-derived by hand below and the engine decides.
 T2 The head column beyond depth 7 is EXTRAPOLATED: the shop's brute
    read 1,2,2,4,8,16,32 and the closed form 2^max(1,a-2) is frozen
    from it. This file re-brutes the column to depth 13 before anything
    downstream reads it.
 T3 The void-lock expectation (norm-3 place at 3/move) is the shop's F4
    hand-read, imported as a prediction.
 T4 The quadratic image corpus's tie facts (every ideal tie a conjugate
    pair; lockstep via the Galois colouring) lean on conjugacy, which
    this S_3 field does not put on its places. Nothing of them is
    assumed; multiplicities and lockstep are measured.

THE RING. theta^3 = -4 theta - 1; disc(x^3 + 4x + 1) = -4*64 - 27 =
-283, squarefree, so Z[theta] is the maximal order and Dedekind reads
every factorization off the polynomial mod p; 283 is the only ramified
prime. Class group C2 (the shop's sandwich: relation order H = 2, the
norm-4 place over 2 non-principal by exhausted box, the norm-2 place
its C2 inverse).

THE HAND-ATTACK, on paper before any engine code.

  THE COLUMNS. lam at the head place P2 (norm 2): 1, 2, 2, 4, 8, ...,
  i.e. 2^max(1, a-2) for a >= 2 -- a flat step at depths 2..3, then
  doubling. Everywhere else the standard closed form
  (N-1) * p^ceil((a-1)/e) is licensed by the logarithm (e < p-1 at
  every other place: the tame ramified pair over 283 included) EXCEPT
  the norm-4 place Q4 over 2 (e = 1, f = 2, e/(p-1) = 1), exactly the
  f = 2-over-2 cell explore_cubic_ring.py F1 names as predicted-standard
  and never measured: for u = 1 + 2x with x a generator of F_4,
  u^2 = 1 + 4(x + x^2) and x + x^2 = 1 there, so the column should be
  standard 3 * 2^(a-1). This ring is the corpus's first test of that
  cell, and S1 brutes it.

  DOORS OVER 2, the arithmetic everything downstream runs on. Fresh P2
  at L = 1: lam(1) = 1 divides 1, lam(2) = 2 does not -- door 2, cost
  4. Seated P2 at depth 2 (L contains 2): lam(3) = 2 divides, lam(4)
  = 4 does not -- door 2, cost 4, landing at depth 4. Seated at depth
  a >= 3: lam(a+1) = 2^(a-1) exceeds the column's own 2-part 2^(a-2),
  so unless another place supplies the missing power of 2 the door is
  1 at cost 2, RECURRENT, and nothing can undercut norm 2: the head
  holds any walk that reaches it at depth 3 or deeper. So the seed
  P2^2 should print the menu {P2 at door 2, Q4 at door 1}, both cost
  4 -- a SAME-PRIME CROSS-NORM tie, a species no quadratic ring can
  present (at degree 2 equal door costs over one rational prime force
  equal norms: split places share the norm, a ramified or inert prime
  carries one place) -- and, taking the tie's first member, jump to
  P2^4 and lock the head at 2/move.

  THE ELEMENT VOID. Norm 2, 3, 5 carry only the places P2, P3, P5,
  all non-principal (bits below), so no element move exists there --
  the box search must come back empty, and that emptiness is the
  certificate. Norm 4: Q4 is non-principal but P2^2 is principal by
  group theory (its class squares to the identity), so the element
  void's FIRST move is the head's own square at cost 4, the ideal
  void's price for the head -- and lam(P2^(2k)) = 2^(2k-2) strictly
  increases from k = 1, so P2^2 ticks forever: the element void walk
  should be P2^2 from move 1, no overture at all, lock at 4/move ON
  THE HEAD, while the ideal void locks the norm-3 place at 3/move.
  The tax refund here is not Z[sqrt(-5)]'s ramification resonance:
  P2 is unramified; what refunds the C2 tax is the head column's own
  flat step (two rungs for one doubling at the bottom).

  BITS BY HAND. N(theta - 1) = -f(1) = -6, and theta - 1 sits in P2
  (1 is the root of f mod 2) and in P3 (1 is the root mod 3), so
  (theta - 1) = P2 * P3 and bit(P3) = bit(P2) = 1. N(theta - 3) =
  -f(3) = -40 = -(2^3 * 5); mod Q4 = (2, theta^2 + theta + 1) the
  element theta - 3 = theta + 1 = theta^2 is a unit, so the 2-part is
  all at P2: (theta - 3) = P2^3 * P5 and bit(P5) = 3 * bit(P2) + 0
  = 1 mod 2. So P2, Q4, P3, P5 are ALL non-principal -- consistent
  with Minkowski (bound 4.76: classes generated by places of norm
  <= 4, all three of which have bit 1).

  THE RIDER. Seed P3^2 (principal, norm 9, L = 6): P2^2 does not tick
  (lam(P2^2) = 2 divides 6), P3 alone is not principal; the cheapest
  ticking principal ideal is (theta - 1) = P2 * P3 at norm 6 -- P3
  ticking, P2 riding flat: Charon's bundle with the head as passenger.
  Two rides feed P2 to depth 2, then P2^2 ticks at cost 4 < 6 and the
  head absorbs the trajectory. The monobasin question -- does EVERY
  principal seed end at the head lock -- is geography, left to the
  census.

  THE WIDTH. A tie of multiplicity 3 needs three places of one norm:
  a split-completely prime p0 (three roots of f mod p0; none below
  30 by hand -- 2, 3, 5 have one root, 7, 11, 13 none, 17, 19 one --
  so p0 >= 31 and Chebotarev puts density 1/6 on the class). For the
  3-tie to be the MENU MINIMUM every place of norm < p0 must have its
  door pushed to cost >= p0. The obstruction: a place seated deep on a
  standard column has door 1 at its own norm forever, and the pair
  over 2 cannot cover each other (P2^j supplies 2^(j-2) while Q4
  needs 3 * 2^a with a >= j to be covered, and Q4^a supplies 2^(a-1)
  while P2 needs 2^(j-1) with j >= a + 2: contradiction). What
  dissolves it: the N-1 parts of OTHER places are STATIC suppliers --
  a split place of norm q contributes the whole of q - 1 to L at
  depth 1 while its own door cost stays q -- so a state seating the
  three norm-p0 places at depth 1 beside suppliers chosen so that
  every rung under p0 divides L (and p0 itself does not divide L,
  keeping the targets' doors at 1) puts the three-way tie at the
  bottom of the menu. The construction is a covering computation, not
  a hand result: S5 runs the loop and asserts what it reaches. From
  the tie, each forced branch deepens its own place (the branch move
  puts (p0-1) * p0 into L, lifting the other two targets' doors to
  cost p0^3), so the three branches should lock three DISTINCT
  places at p0/move: three limits from one opening, the width-3
  base realized.

  DISTRUST THE MARGIN. The derived half is the door arithmetic and
  the bits; both are brute-checked before use (S1, S2). The vibes
  half: "seeds to norm 40 map the basins" is a SCOPE, not a claim;
  "suppliers exist below the universe cap" is asserted by the loop or
  reported as its own finding (K5).

PREDICTIONS, fixed before the engine ran, each naming what the rig
PRINTS.
  P1 The generic brute-forcer reproduces the headless cubic's filed
     inert-2 and tame-23 columns (its own ring, its own tags), and the
     two brute instruments (polynomial-order and maximal-order) agree
     at every shared cell of THIS ring. 0 disagreements.
  P2 The full brute sweep matches lam_P at every (place, depth) within
     the residue cap -- the head column 1,2,2,4,...,2^11 to depth 13
     and the norm-4 column 3*2^(a-1) to depth 6 included -- and the
     standard e=1 form disagrees exactly at the head place from
     depth 3 on.
  P3 2 = P2*Q4, 3 = P3*Q9, 5 = P5*Q25, 7 inert; 283 the only ramified
     prime in a full scan of the universe, shape P*Q^2; a
     split-completely prime exists below 300 (p0 printed); the three
     splitting densities land near 1/2, 1/3, 1/6.
  P4 The relation kernel mod 2 is 1-dimensional; kernel bits equal
     certificate bits at every generator place; bits(P2, Q4, P3, P5)
     = 1; (theta - 1) factors as P2 * P3; the element box finds NO
     principal ideal of norm 2, 3 or 5, and every principal ideal it
     does find has even bit sum.
  P5 The ideal void locks the norm-3 place at 3/move through the
     imported walker; seed P2^2 prints the cross-norm tie {P2 door 2,
     Q4 door 1} at cost 4 and locks the head at 2/move; every
     generator-product seed locks within the walker's cap.
  P6 The element void's first move is P2^2 at cost 4 and the walk
     locks vehicle P2^2 at 4/move -- the element lock sits ON the
     head; the void's element/ideal split prints 4 against 3. Seed
     P3^2 opens with the norm-6 rider (theta - 1), P3 ticking, P2
     flat, and is absorbed by the head lock.
  P7 The covering loop reaches a state whose menu minimum is p0 with
     the tie EXACTLY the three norm-p0 places, and the three forced
     branches each lock their own branch place at p0/move -- three
     distinct limits from one opening.

KILL-SHAPES, as observables.
  K1 a brute cell disagrees with lam_P: the column model is wrong and
     nothing below is readable; the run stops loudly.
  K2 the relation kernel is not 1-dimensional, or kernel bits differ
     from certificate bits anywhere: the class instrument is wrong;
     no class-flavored reading below is admissible.
  K3 the element box finds a principal ideal of norm 2 or 3: the h = 2
     certificate or the unit is wrong; the run stops loudly.
  K4 the ideal void does not lock the norm-3 place at 3/move: the
     transplanted hand-read was wrong; printed as the finding.
  K5 the covering loop exhausts its supplier budget before reaching a
     3-way minimum: printed with the offending place and rung -- a
     finding about the cover, not a silent skip.

THE POSITIVE CONTROL (S1, run before any verdict is read). The brute
instruments are run against the headless cubic's independently filed
columns first, then against each other on this ring's shared cells,
and only then is the sweep read.

THE SECTIONS.
  S1  positive control + the ladder sweep: both brute instruments, the
      head column deep, the f = 2-over-2 cell.
  S2  the ring: factorizations, the ramification scan, p0, the class
      bits by kernel and by certificate box, the hand relations.
  S3  the ideal seed census through the imported walker: the void, the
      P2^2 seed, basin geography, tie multiplicities.
  S4  the element world: the void walk, the rider, the census over
      principal seeds, the element price.
  S5  the width: the covering construction, the three-way tie, the
      three branches.

FINDINGS (tiers inline; run record at the bottom; every section
asserts).

F1 THE COLUMN MODEL HOLDS AND THE UNMEASURED CELL FILLS (rule in
   range; 44 cells brute-forced at every place of norm <= 30 to the
   residue cap, 0 off; the two instruments welded on 18 shared cells;
   6 filed control cells of the headless cubic reproduced first). The
   head column is 1,2,2,4,...,2^11 = 2^max(1, a-2) to depth 13 -- the
   excess persists far past the shop's depth-7 read (T2 discharged) --
   and the standard e = 1 form misses EXACTLY the head's 11 cells from
   depth 3, nothing else. The norm-4 place over 2 (e = 1, f = 2) is
   STANDARD, 3 * 2^(a-1) to depth 6: the f = 2-over-2 cell
   explore_cubic_ring.py F1 names as predicted-standard-and-unmeasured
   is now measured, and the x + x^2 mechanism's prediction was right.
   THE DEEP SCOPE IS PROPERTY, NOT EXTRAPOLATION -- the walks below
   reach depths past the brute caps (the element census's deepest lock
   state sits at P2^25 * Q4^27), and the columns there are licensed by
   derivation, not by the sweep: the head column is the exponent of
   (Z/2^a)^* (e = f = 1: the residue ring IS Z/2^a), and the norm-4
   column's hand argument bounds the exponent from both sides (see
   lam_P's docstring). The brute is the check; the closed forms are
   exact at every depth this file consumes.

F2 THE HEADED CUBIC WALKS -- heads decide walks beyond the quadratic
   family (rule in range; 44 ideal seeds, the norm <= 40 belt plus the
   void, through the imported walker: all lock). The void locks the
   norm-3 place at 3/move (the shop's F4 hand-read, exact). Basin
   geography is rich where the headless cubic's was a point: FIVE lock
   places -- head 2/move (11 seeds), norm-3 3/move (12), norm-4 4/move
   (2), norm-5 5/move (11), norm-17 17/move (8). The head holds at
   EVERY seeded depth in the census, bare P2^1 included (at the
   void's L = 1 its next rung is uncovered: door 1 at cost 2 from the
   seed's first menu), and seed P2^2's door-2 jump clears the flat
   window in one move, landing at depth 4 where the column doubles
   every rung and cost 2 undercuts the universe forever -- where
   Z[sqrt(-5)]'s wild seat loses its shallow grab (the (2) seed) and
   holds only what it is given deep (P2^5). So the heads-decide-walks
   reading survives residue degree 3 and h > 1 together: the
   quadratic walks were not a quadratic accident.

F3 THE CROSS-NORM TIE, a species no quadratic ring can present
   (observation at this ring; 3 of 453 census menu readings, plus the
   constructed P2^2 menu, all the same pair). {P2 at door 2, Q4 at
   door 1}: one rational prime, two norms, equal cost 4. At degree 2
   equal door costs over one prime force equal norms (split places
   are conjugate, ramified and inert primes carry one place); the
   f = 1-beside-f = 2 configuration that breaks this is degree >= 3's
   own. Every other census menu is tie-free: multiplicity census
   {1: 450, 2: 3}.

F4 THE ELEMENT WORLD LOCKS ON THE HEAD, AND THE CLASS TAX IS
   GRANULARITY, NOT RUNG PRICE (rule in range; 21 principal seeds to
   norm 40, all lock; the void overture asserted move by move). C2
   shuts the three cheapest seats: no principal ideal of norm 2, 3 or
   5 exists (unit-reduced boxes exhausted -- proofs, not searches), so
   the element void's FIRST move is the head's own square P2^2 at
   cost 4, with no overture at all, and the walk locks vehicle P2^2
   at 4/move. The void's split: element 4 against ideal 3. The tax
   read exactly: the recurrent price is 4 = 2^2 = N^ord[P2], but per
   LADDER RUNG the element world pays 2 -- lambda quadruples per
   element move where the ideal lock doubles -- which is the ideal
   world's own head price. So at an unramified head the C2 tax buys
   move granularity (two rungs per move) and not rung price:
   Z[sqrt(-5)]'s resonance refund (ord = e) has an unramified
   analogue with the column's flat step in e's role. T1's transplant
   re-derived, not assumed.

F5 THREE ELEMENT BASINS -- the monobasin is quadratic geography, not
   an h > 1 law (observation; 21 seeds: 17 lock P2^2, 3 lock the
   norm-17 place -- the belt's one PRINCIPAL small place, clockable
   alone in the element world -- and 1 locks the bundle (2) = P2*Q4
   at 8/move: the Q4^2 seed, whose deep f = 2 column supplies the
   2-power that lambda-covers the head column at the lock -- P2^2
   never ticks there, so the degree-bound vehicle is the cheapest
   LEFT, the dowry editing the vehicle menu). 49 rider moves:
   (theta - 1) = P2 * P3 is Charon's
   bundle with the head as ferry -- seed P3^2 rides it twice, each
   ride feeding P2, and the head absorbs the walk at move 3.

F6 WIDTH 3 IS REAL -- the first multiplicity-3 opening in a number
   ring (observation at a constructed state; the covering loop, five
   suppliers). p0 = 71 is the first split-completely prime (the
   splitting densities 0.507, 0.334, 0.159 sit on Chebotarev's 1/2,
   1/3, 1/6). Seating the three norm-71 places at depth 1 beside five
   static suppliers -- split places over 73, 113, 139, 313, 331, each
   seated so its N - 1 covers a named rung of a cheaper place --
   pushes every door under 71 past it: the menu bottoms at the
   three-way tie, and the three forced branches each lock their own
   place at 71/move. Three distinct limits from one opening: the
   width-3 base of the exhausted-image law realized in a number ring.
   The state is PLANTED -- no census seed reached one, the belt's
   ties are all the width-2 species of F3 -- so the claim is that the
   ring PRESENTS width 3; seeded reachability is geography left open.
   The hand-attack's mutual-covering obstruction over 2 is dissolved
   exactly by the N - 1 statics, the ghost supply's mechanism.

RUN RECORD. `python explore_headed_cubic_walk.py`. One process,
CPython, no BLAS. 718 checks, 6.5 s wall, peak working set 24.0 MB
under memwatch.py's 512 MB ceiling. S1: 6 control cells, 18 weld
cells, 44 sweep cells, 0 off; the weld runs shallow (residue count
<= 100) because the polynomial-order forcer's unreduced iterated HNF
swells at deep powers -- its home ring never exercises them -- and
the recursion limit is raised for its xgcd. S2: 2262-prime
ramification scan (283 only), p0 = 71, kernel dim 1 with kernel bits
equal to certificate bits at all 8 generator places, 21 principal
ideals to norm 40 all of even bit sum. S3: 44 seeds, 5 lock places,
tie census {1: 450, 2: 3}. S4: 21 principal seeds, 3 vehicles, 49
rider moves. S5: 5 suppliers, the 3-tie, 3 branches locking
themselves at 71/move. One instrument correction between the first
green run and this one, caught by reading the prints (a "2 hits"
line where one ideal has one factorization): the shop's hnf_red is
swell-control, not a canonical form -- its descending-column pass
can leave an unreduced entry -- so ideal identity here goes through
hnf_canon's ascending-column reduction; the first run's dynamics
were unaffected (same ideal, two keys), only its hit and ideal
counts.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from math import gcd, sqrt

sys.setrecursionlimit(20000)   # the imported forcer's xgcd recurses

import explore_cubic_ring as CR
import explore_cubic_field_shop as SHOP
import explore_lock_budget as LB

CHECKS = 0

MAXP = 20000        # rational primes enumerated into the universe
BRUTE_CAP = 15000   # residues allowed in one brute-forced quotient
BIT_NORM_CAP = 30   # generator places for the relation kernel
ELEM_SCAN_CAP = 120  # norms the element menu may scan to
ELEM_T = 25         # element census moves per seed
SUPPLIER_CAP = 40   # covering-loop iterations before K5 fires

MINPOLY = (1, 4, 0, 1)      # x^3 + 4x + 1, low coefficient first
REDUCE = (-1, -4, 0)        # t^3 = -1 - 4t
POLY_ABC = (0, 4, 1)        # x^3 + a x^2 + b x + c


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
    n = abs(n)
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def prime_divisors(n):
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


PRIMES = CR.PRIMES  # sieve to 20000, shared with the headless engine


# --------------------------------------------------------------- the ring
def factor_shape(p):
    """[(e, f), ...] for the places over p, off the minimal polynomial mod
    p. Dedekind applies because disc = -283 is squarefree, so Z[theta] is
    the maximal order."""
    f = MINPOLY
    d = CR.pgcd(f, CR.pderiv(f, p), p)
    if len(d) - 1 == 1:
        return [(1, 1), (2, 1)]               # g * h^2, both linear
    if len(d) - 1 == 2:
        return [(3, 1)]                       # h^3
    assert len(d) - 1 == 0, "unreadable factor shape at %d" % p
    sub = list(CR.ppowmod((0, 1), p, f, p))
    while len(sub) < 2:
        sub.append(0)
    sub[1] -= 1
    nr = len(CR.pgcd(tuple(sub), f, p)) - 1
    if nr <= 0:
        return [(1, 3)]                       # inert
    if nr == 1:
        return [(1, 1), (1, 2)]               # a rational place and f = 2
    assert nr == 3, "a squarefree cubic with %d roots mod %d" % (nr, p)
    return [(1, 1), (1, 1), (1, 1)]


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


def place_key(pl):
    return (place_norm(pl), pl[1], pl[2], pl[3])


def conj_place(pl):
    """S_3 cubic: no conjugation acts on the places over Q."""
    return pl


def show(pl):
    return "%d[e%d,f%d]%s" % (pl[0], pl[1], pl[2],
                              ".%d" % pl[3] if pl[3] else "")


def show_st(st):
    parts = ["%s^%d" % (show(pl), e)
             for pl, e in sorted(st.items(), key=lambda kv: place_key(kv[0]))
             if e]
    return "*".join(parts) if parts else "(1)"


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


UNIVERSE = build_universe()
HEAD = (2, 1, 1, 0)   # the norm-2 place: the certified head
Q4 = (2, 1, 2, 0)     # the norm-4 place over 2
P3 = (3, 1, 1, 0)
P5 = (5, 1, 1, 0)


def lam_P(pl, a):
    """lambda of the prime-power column X^a -- the exponent of (O/X^a)^*.

    The standard closed form (N - 1) * p^ceil((a-1)/e) everywhere EXCEPT
    the head place, whose column is 1, 2, 2, 4, 8, ... = 2^max(1, a-2)
    from depth 2. Depth is NOT capped by the brute range: at the head,
    e = f = 1 makes O/P2^a = Z/2^a and the column is the exponent of
    (Z/2^a)^* -- a property of Q_2, exact at every depth; at the norm-4
    place the hand argument is two-sided (a generator's square lands one
    level deep since x + x^2 is a unit on F_4's generators, and the
    2-power map U_b -> U_(b+1) bounds the exponent above), so
    3 * 2^(a-1) holds at every depth. S1's brute (depths 13 and 6) is
    the CHECK on both, not the license."""
    if a == 0:
        return 1
    if pl == HEAD:
        return 1 if a == 1 else 2 ** max(1, a - 2)
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


_gp_cache = {}


def gen_products(maxnorm):
    """All nontrivial place-power products of norm <= maxnorm."""
    if maxnorm in _gp_cache:
        return _gp_cache[maxnorm]
    pls = [pl for pl in UNIVERSE if place_norm(pl) <= maxnorm]
    out = []

    def rec(i, cur, nrm):
        if cur:
            out.append((nrm, dict(cur)))
        for j in range(i, len(pls)):
            pl = pls[j]
            n2 = nrm * place_norm(pl)
            if n2 > maxnorm:
                break
            e = 1
            while n2 <= maxnorm:
                cur[pl] = e
                rec(j + 1, cur, n2)
                e += 1
                n2 *= place_norm(pl)
            del cur[pl]

    rec(0, {}, 1)
    out.sort(key=lambda x: x[0])
    _gp_cache[maxnorm] = out
    return out


# ------------------------------------------- the maximal order and its HNFs
_O, _ = SHOP.maximal_order(*POLY_ABC)
assert _O.trace_form_disc() == -283, "wrong field"
assert all(_O.basis[i] == tuple(1 if j == i else 0 for j in range(3))
           for i in range(3)), "Z[theta] not maximal: identity basis lost"

_hnf_cache = {}


def hnf_places(p):
    """[(tag, P_hnf)] for the places over p, tag ordinals following the
    maximal-order enumeration within each (e, f) class. This bijection
    DEFINES which tag names which same-(e,f) place; factor_shape fixes
    only the multiset, asserted equal."""
    if p in _hnf_cache:
        return _hnf_cache[p]
    got = SHOP.maximal_places(_O, p)
    seen = {}
    out = []
    for (P, e, f) in got:
        i = seen.get((e, f), 0)
        seen[(e, f)] = i + 1
        out.append(((p, e, f, i), P))
    assert sorted((e, f) for (_, e, f) in got) == \
        sorted(factor_shape(p)), "place shapes disagree at %d" % p
    _hnf_cache[p] = out
    return out


def tag_hnf(pl):
    for (tag, P) in hnf_places(pl[0]):
        if tag == pl:
            return P
    raise AssertionError("no HNF for %s" % (pl,))


# ------------------------------------------------------------ class bits
_BITS = {}


def place_bit(pl):
    """The place's class in C2: 0 = principal (a generator FOUND), 1 =
    non-principal (the unit-reduced box EXHAUSTED -- a proof, the shop's
    certificate). Cached; cross-checked against the relation kernel in
    S2."""
    if pl in _BITS:
        return _BITS[pl]
    P = tag_hnf(pl)
    n = place_norm(pl)
    g = SHOP.find_generator(_O, P, n)
    if g is not None:
        _BITS[pl] = 0
        return 0
    certified, detail = SHOP.non_principality_certificate(
        _O, P, n, POLY_ABC)
    _BITS[pl] = 1 if certified else 0
    return _BITS[pl]


def bit_sum(st):
    return sum(place_bit(pl) * e for pl, e in st.items()) % 2


# ------------------------------------------------- elements by norm, complete
def _embedding_rows():
    a, b, c = POLY_ABC
    r = SHOP.real_root_cubic(a, b, c)
    q1 = a + r
    q0 = b + r * q1
    zr = -q1 / 2
    im2 = q0 - q1 * q1 / 4
    assert im2 > 0, "complex pair expected"
    zi = sqrt(im2)
    emb = []
    for bvec in _O.basis:
        t = [float(bvec[k]) for k in range(3)]
        sR = t[0] + t[1] * r + t[2] * r * r
        zRe = t[0] + t[1] * zr + t[2] * (zr * zr - zi * zi)
        zIm = t[1] * zi + t[2] * (2 * zr * zi)
        emb.append((sR, zRe, zIm))
    return [[e[0] for e in emb], [e[1] for e in emb], [e[2] for e in emb]]


_EMB = _embedding_rows()
_ETA = SHOP.find_unit(_O)
assert _ETA is not None, "no unit found"
_UREAL = abs(sum(float(_ETA[j]) * _EMB[0][j] for j in range(3)))
if _UREAL < 1:
    _UREAL = 1 / _UREAL
assert _UREAL > 1 + 1e-9, "unit with unit-modulus real embedding"

def hnf_canon(gens):
    """CANONICAL HNF key. The shop's hnf_red controls coefficient swell
    but is not canonical: its descending-column pass lets a column-1
    reduction reintroduce unreduced column-2 entries, so one ideal can
    wear two keys. Reducing in ASCENDING column order is canonical --
    column i lands in [0, diag) and later columns are cleaned after."""
    H = [list(r) for r in SHOP.hnf_red(gens, 3)]
    for i in range(3):
        for j in range(i):
            q = H[j][i] // H[i][i]
            if q:
                H[j] = [a - q * b for a, b in zip(H[j], H[i])]
    return tuple(tuple(row) for row in H)


_pion_cache = {}


def principal_ideals_of_norm(n):
    """Every principal ideal of norm n, as (hnf_key, generator, factor
    dict). COMPLETE: any generator can be unit-reduced until its real
    embedding lies in [n^(1/3)/sqrt(u), n^(1/3)*sqrt(u)], which bounds
    all three embeddings and hence the theta-coordinates -- the same box
    the shop's non-principality certificate exhausts."""
    if n in _pion_cache:
        return _pion_cache[n]
    BR = n ** (1.0 / 3) * sqrt(_UREAL) * (1 + 1e-9)
    BC = n ** (1.0 / 3) * _UREAL ** 0.25 * (1 + 1e-9)
    inv = SHOP.mat_inv_float(_EMB)
    bounds = (BR, BC, BC)
    lim = []
    for i in range(3):
        s = sum(abs(inv[i][j]) * bounds[j] for j in range(3))
        lim.append(int(s * (1 + 1e-9)) + 2)
    found = {}
    for x in range(-lim[0], lim[0] + 1):
        for y in range(-lim[1], lim[1] + 1):
            for z in range(-lim[2], lim[2] + 1):
                v = (x, y, z)
                if v == (0, 0, 0):
                    continue
                if abs(_O.norm(v)) != n:
                    continue
                gens = [_O.mul(v, tuple(1 if k == j else 0
                                        for k in range(3)))
                        for j in range(3)]
                key = hnf_canon(gens)
                if key not in found:
                    found[key] = v
    out = []
    for key in sorted(found):
        v = found[key]
        fac = factor_principal(v, abs(_O.norm(v)))
        out.append((key, v, fac))
    _pion_cache[n] = out
    return out


def factor_principal(v, N):
    """Place factorization of the principal ideal (v), by valuations."""
    fac = {}
    for p in prime_divisors(N):
        for (tag, P) in hnf_places(p):
            val = SHOP.place_valuation(_O, v, P, v_p(N, p) + 1)
            if val:
                fac[tag] = val
    nn = 1
    for pl, e in fac.items():
        nn *= place_norm(pl) ** e
    assert nn == N, "factor_principal norm mismatch"
    return fac


def elem_menu(st, L):
    """(norm, hits): every principal ideal at the least ticking norm."""
    for n in range(2, ELEM_SCAN_CAP + 1):
        hits = []
        for (key, v, fac) in principal_ideals_of_norm(n):
            L2 = L
            for pl, e in fac.items():
                L2 = lcm(L2, lam_P(pl, st.get(pl, 0) + e))
            if L2 > L:
                hits.append((key, v, fac))
        if hits:
            return n, hits
    raise AssertionError("element scan exhausted")


def run_elem(seed, T):
    st, L = dict(seed), lam_state(seed)
    ok(bit_sum(st) == 0, "element seed not principal")
    log = []
    for _ in range(T):
        n, hits = elem_menu(st, L)
        key, v, fac = hits[0]
        flat = tuple(pl for pl, e in fac.items()
                     if L % lam_P(pl, st.get(pl, 0) + e) == 0)
        for pl, e in fac.items():
            st[pl] = st.get(pl, 0) + e
        L2 = lam_state(st)
        ok(L2 > L, "element move grows lambda")
        assert bit_sum(st) == 0, "element state left the principal class"
        log.append((key, v, fac, n, flat, len(hits)))
        L = L2
    return log, st, L


def elem_lock(log):
    """The recurrent vehicle, if the last LOCK_R moves repeat one ideal."""
    R = LB.LOCK_R
    if len(log) < R:
        return None
    tail = [mv[0] for mv in log[-R:]]
    if len(set(tail)) == 1:
        return log[-1]
    return None


# ------------------------------------------- S1 control + the ladder sweep
def roots_mod(p):
    return [r for r in range(p)
            if (r * r * r + 4 * r + 1) % p == 0]


def s1_ladders():
    section("S1  POSITIVE CONTROL + THE LADDER SWEEP -- both brute "
            "instruments, the head deep")

    # (a) the polynomial-order forcer against the headless cubic's own
    #     filed columns: inert 2 (f = 3) and the tame pair member over 23.
    n_ctl = 0
    for a in range(1, 5):
        got = CR.unit_exponent(2, (0,), CR.CUBIC_REDUCE, a, 8)
        want = CR.lam_P((2, 1, 3, 0), a)
        ok(got == want, "control inert-2 depth %d: %d != %d"
           % (a, got, want))
        n_ctl += 1
    for a in range(1, 3):
        got = CR.unit_exponent(23, (13, 1), CR.CUBIC_REDUCE, a, 23)
        want = CR.lam_P((23, 2, 1, 0), a)
        ok(got == want, "control tame-23 depth %d: %d != %d"
           % (a, got, want))
        n_ctl += 1
    print("  control: %d filed cells of the headless cubic reproduced"
          % n_ctl)

    # (b) cross-instrument weld on THIS ring: the polynomial forcer and
    #     the maximal-order forcer agree at every small shared cell.
    n_weld = 0
    for pl in UNIVERSE:
        q = place_norm(pl)
        if q > 25 or pl[0] > 5:
            continue
        rts = roots_mod(pl[0])
        if pl[2] == 1 and pl[1] == 1 and rts:
            hpoly = (-rts[0] % pl[0], 1)
        elif pl[2] == 3:
            hpoly = (0,)
        elif pl[2] == 2:
            rem = MINPOLY
            for r in rts:
                rem = SHOP.poly_divmod_q(rem, (-r % pl[0], 1), pl[0])
            hpoly = rem
        else:
            continue
        a = 1
        while q ** a <= 100:
            # shallow cells only: the polynomial-order forcer's UNREDUCED
            # iterated HNF swells at deep powers (its home ring never
            # exercises them); agreement of the two code paths is what
            # the weld certifies, and depth does not change either path.
            g1 = CR.unit_exponent(pl[0], hpoly, REDUCE, a, q)
            g2 = SHOP.unit_exponent_order(_O, tag_hnf(pl), a, q)
            ok(g1 == g2, "instruments disagree at %s^%d: %d != %d"
               % (show(pl), a, g1, g2))
            n_weld += 1
            a += 1
    print("  weld: %d shared cells, both instruments agree" % n_weld)

    # (c) the sweep: every place of norm <= 30, every depth in cap,
    #     against lam_P; the standard form's misses counted beside it.
    n_cells, std_miss = 0, []
    for pl in UNIVERSE:
        q = place_norm(pl)
        if q > 30:
            break
        a = 1
        while q ** a <= BRUTE_CAP:
            got = SHOP.unit_exponent_order(_O, tag_hnf(pl), a, q)
            want = lam_P(pl, a)
            ok(got == want, "lam_P wrong at %s^%d: brute %d, formula %d"
               % (show(pl), a, got, want))
            std = (q - 1) * pl[0] ** -(-(a - 1) // pl[1])
            if std != got:
                std_miss.append((pl, a))
            n_cells += 1
            a += 1
    print("  sweep: %d cells brute-forced, 0 off lam_P" % n_cells)
    head_col = [lam_P(HEAD, a) for a in range(1, 14)]
    print("  head column to depth 13: %s" % head_col)
    print("  norm-4 column to depth 6: %s (the f = 2-over-2 cell: %s)"
          % ([lam_P(Q4, a) for a in range(1, 7)],
             "STANDARD" if all(m[0] != Q4 for m in std_miss)
             else "NON-STANDARD"))
    ok(all(m[0] == HEAD and m[1] >= 3 for m in std_miss),
       "standard form missed somewhere besides the deep head: %s"
       % std_miss)
    ok(len(std_miss) == len([a for a in range(3, 14)
                             if 2 ** a <= BRUTE_CAP]),
       "standard-form misses not exactly the head depths >= 3")
    print("  standard e=1 form misses exactly the head at depths >= 3 "
          "(%d cells)" % len(std_miss))


# ------------------------------------------------------------ S2 the ring
def s2_ring():
    section("S2  THE RING -- factorizations, ramification, p0, the class "
            "bits")

    for p in (2, 3, 5, 7):
        print("  %d: %s" % (p, ", ".join(
            show(pl) for pl in UNIVERSE if pl[0] == p)))
    ok([pl for pl in UNIVERSE if pl[0] == 2] == [HEAD, Q4],
       "2 does not factor as P2 * Q4")
    ok(factor_shape(3) == [(1, 1), (1, 2)], "3 is not P3 * Q9")
    ok(factor_shape(5) == [(1, 1), (1, 2)], "5 is not P5 * Q25")
    ok(factor_shape(7) == [(1, 3)], "7 is not inert")
    ok(factor_shape(283) == [(1, 1), (2, 1)], "283 is not P * Q^2")

    ram = [p for p in PRIMES if any(e > 1 for (e, f) in factor_shape(p))]
    ok(ram == [283], "ramified primes %s, expected [283]" % ram)
    print("  ramification scan over %d primes: only 283 (tame, P*Q^2)"
          % len(PRIMES))

    counts = {"PQ2": 0, "P+Q9": 0, "inert": 0, "split": 0}
    p0 = None
    for p in PRIMES:
        sh = factor_shape(p)
        if len(sh) == 2 and sh[1][0] == 2:
            counts["PQ2"] += 1
        elif len(sh) == 3:
            counts["split"] += 1
            if p0 is None:
                p0 = p
        elif len(sh) == 2:
            counts["P+Q9"] += 1
        else:
            counts["inert"] += 1
    tot = len(PRIMES)
    print("  densities: P+Q(f=2) %.3f (1/2), inert %.3f (1/3), "
          "split-completely %.3f (1/6)"
          % (counts["P+Q9"] / tot, counts["inert"] / tot,
             counts["split"] / tot))
    ok(p0 is not None and p0 < 300,
       "no split-completely prime below 300")
    print("  first split-completely prime p0 = %d: %s"
          % (p0, ", ".join(show(pl) for pl in UNIVERSE if pl[0] == p0)))

    # the class bits: relation kernel mod 2 over the generator places
    gen_places = []
    for pl in UNIVERSE:
        if place_norm(pl) > BIT_NORM_CAP:
            break
        gen_places.append((pl[0], pl[1], pl[2],
                           "%d.%d" % (pl[0], pl[3]), tag_hnf(pl)))
    rows = SHOP.harvest_relations(_O, gen_places)
    ok(len(rows) >= 50, "relation harvest too thin: %d rows" % len(rows))
    k = len(gen_places)
    cols = [[rows[i][j] for i in range(len(rows))] for j in range(k)]
    kern = SHOP.kernel_mod_p(cols, 2)
    ok(len(kern) == 1, "relation kernel mod 2 has dim %d, not 1"
       % len(kern))
    bits_k = [x % 2 for x in kern[0]]
    tags = [pl for pl in UNIVERSE if place_norm(pl) <= BIT_NORM_CAP]
    n_agree = 0
    for i, pl in enumerate(tags):
        ok(bits_k[i] == place_bit(pl),
           "kernel bit %d != certificate bit %d at %s"
           % (bits_k[i], place_bit(pl), show(pl)))
        n_agree += 1
    print("  kernel dim 1; kernel bits == certificate bits at all %d "
          "generator places" % n_agree)
    print("  bits: %s" % ", ".join(
        "%s:%d" % (show(pl), place_bit(pl)) for pl in tags))
    for pl in (HEAD, Q4, P3, P5):
        ok(place_bit(pl) == 1, "%s expected non-principal" % show(pl))
    print("  P2, Q4, P3, P5 all non-principal (the hand relations)")

    fac = factor_principal((-1, 1, 0), 6)      # theta - 1
    ok(fac == {HEAD: 1, P3: 1}, "(theta-1) != P2 * P3: %s" % fac)
    fac = factor_principal((-3, 1, 0), 40)     # theta - 3
    ok(fac == {HEAD: 3, P5: 1}, "(theta-3) != P2^3 * P5: %s" % fac)
    print("  (theta-1) = P2 * P3, (theta-3) = P2^3 * P5, as derived")

    for n in (2, 3, 5):
        got = principal_ideals_of_norm(n)
        ok(got == [], "principal ideal of norm %d found: K3" % n)
    print("  no principal ideal of norm 2, 3 or 5 (boxes exhausted)")
    n_even = 0
    for n in range(2, 41):
        for (key, v, fac) in principal_ideals_of_norm(n):
            ok(bit_sum(fac) == 0,
               "principal ideal with odd bit sum at norm %d" % n)
            n_even += 1
    print("  every principal ideal to norm 40 has even bit sum "
          "(%d ideals)" % n_even)
    return p0


# --------------------------------------- S3 the ideal census (the walker)
def s3_ideal_census():
    section("S3  THE IDEAL CENSUS -- this ring through the IMPORTED "
            "walker")
    M = sys.modules[__name__]

    print("  void menu, every place of norm <= 30:")
    scan = LB.scan_universe(M, {}, 1, ceiling=30)
    for nrm, r, cost, pl in sorted(scan):
        print("    %-14s norm %-6d door %-3d price %d"
              % (show(pl), nrm, r, cost))

    got = LB.walk_to_lock(M, {})
    ok(got is not None, "the void does not lock in the walker's cap")
    st, L, pl, cost, steps = got
    print("  void locks %s at %d/move (%d steps); support %s"
          % (show(pl), cost, steps, show_st(st)))
    ok(pl == P3 and cost == 3,
       "K4: the void lock is %s at %d, not the norm-3 place at 3"
       % (show(pl), cost))

    # the P2^2 seed: the cross-norm tie, then the head lock
    seed = {HEAD: 2}
    L0 = lam_state(seed)
    cost0, ties0 = ideal_menu(seed, L0)
    print("  seed P2^2 first menu: cost %d, ties %s"
          % (cost0, [(show(p_), r_) for p_, r_ in ties0]))
    ok(cost0 == 4 and ties0 == [(HEAD, 2), (Q4, 1)],
       "the cross-norm tie {P2 r2, Q4 r1} did not print: %s" % ties0)
    ok(place_norm(ties0[0][0]) != place_norm(ties0[1][0]),
       "tie members share a norm")
    got = LB.walk_to_lock(M, seed)
    ok(got is not None, "seed P2^2 does not lock")
    st, L, pl, cost, steps = got
    print("  seed P2^2 locks %s at %d/move; support %s"
          % (show(pl), cost, show_st(st)))
    ok(pl == HEAD and cost == 2, "the head does not hold the P2^2 seed")

    # the belt census: locks and tie multiplicities
    seeds = LB.locking_seeds(M)
    ok(len(seeds) > 0, "no locking seeds")
    lock_hist = {}
    head_locks = []
    for seed, (st, L, pl, cost, steps) in seeds:
        lock_hist[pl] = lock_hist.get(pl, 0) + 1
        if pl == HEAD:
            head_locks.append(seed)
    print("  %d seeds (norm <= %d belt + void) all lock; lock places:"
          % (len(seeds), LB.SEED_CAP))
    for pl in sorted(lock_hist, key=place_key):
        print("    %-14s %3d seeds at %d/move"
              % (show(pl), lock_hist[pl], place_norm(pl)))
    print("  seeds locking on the HEAD: %d" % len(head_locks))
    for seed in head_locks[:6]:
        print("    %s" % show_st(seed))

    # tie multiplicities along every census trajectory
    mult_hist = {}
    for seed, (st_l, L_l, pl_l, cost_l, steps_l) in seeds:
        st, L = dict(seed), lam_state(seed)
        for _ in range(steps_l):
            cost, ties = ideal_menu(st, L)
            mult_hist[len(ties)] = mult_hist.get(len(ties), 0) + 1
            p_, r_ = ties[0]
            st[p_] = st.get(p_, 0) + r_
            L = lam_state(st)
    print("  tie multiplicity over all census moves: %s"
          % dict(sorted(mult_hist.items())))
    return seeds, mult_hist


# ------------------------------------------------- S4 the element world
def s4_element_world():
    section("S4  THE ELEMENT WORLD -- the void, the rider, the census")

    log, st, L = run_elem({}, 15)
    print("  element void, first 6 moves:")
    for (key, v, fac, n, flat, nh) in log[:6]:
        print("    norm %-4d %-22s flat %-14s (%d hits)"
              % (n, show_st(fac),
                 ",".join(show(p_) for p_ in flat) or "-", nh))
    lk = elem_lock(log)
    ok(lk is not None, "the element void does not lock")
    ok(log[0][3] == 4 and log[0][2] == {HEAD: 2},
       "the element void's first move is not P2^2 at 4: %s"
       % show_st(log[0][2]))
    ok(lk[2] == {HEAD: 2} and lk[3] == 4,
       "the element void lock is not P2^2 at 4/move")
    print("  element void locks vehicle P2^2 at 4/move -- ON the head")
    print("  the void's split: element 4 against ideal 3")

    # the rider seed P3^2
    log3, st3, L3 = run_elem({P3: 2}, 12)
    print("  seed P3^2, first 4 moves:")
    for (key, v, fac, n, flat, nh) in log3[:4]:
        print("    norm %-4d %-22s flat %s"
              % (n, show_st(fac),
                 ",".join(show(p_) for p_ in flat) or "-"))
    ok(log3[0][3] == 6 and log3[0][2] == {HEAD: 1, P3: 1}
       and log3[0][4] == (HEAD,),
       "seed P3^2's first move is not the norm-6 rider")
    lk3 = elem_lock(log3)
    ok(lk3 is not None and lk3[2] == {HEAD: 2},
       "the rider seed is not absorbed by the head lock")
    print("  the norm-6 rider (theta-1) fires, P2 riding; the head "
          "absorbs the walk")

    # the census over principal generator-product seeds
    seeds = [(nrm, m) for nrm, m in gen_products(40) if bit_sum(m) == 0]
    lock_hist, rider_moves, n_locked = {}, 0, 0
    for nrm, m in seeds:
        lg, st_c, L_c = run_elem(m, ELEM_T)
        lk = elem_lock(lg)
        if lk is not None:
            n_locked += 1
            key = show_st(lk[2])
            lock_hist[key] = lock_hist.get(key, 0) + 1
        rider_moves += sum(1 for mv in lg if mv[4])
    print("  %d principal seeds (norm <= 40): %d lock inside %d moves"
          % (len(seeds), n_locked, ELEM_T))
    for key in sorted(lock_hist):
        print("    vehicle %-22s %3d seeds" % (key, lock_hist[key]))
    print("  rider moves (a flat component bundled): %d" % rider_moves)
    return seeds, lock_hist


# ----------------------------------------------------------- S5 the width
def s5_width(p0):
    section("S5  THE WIDTH -- covering the menu down to a three-way tie "
            "at p0 = %d" % p0)
    targets = [pl for pl in UNIVERSE if pl[0] == p0]
    ok(len(targets) == 3, "p0 does not carry three places")
    W = {pl: 1 for pl in targets}
    suppliers = []
    for it in range(SUPPLIER_CAP):
        L = lam_state(W)
        cost, ties = ideal_menu(W, L)
        if cost == p0:
            break
        offender, r_off = ties[0]
        m = lam_P(offender, W.get(offender, 0)
                  + door_r(offender, W.get(offender, 0), L))
        sup = None
        for pl in UNIVERSE:
            if pl[2] != 1 or pl[1] != 1 or pl[0] <= p0 or pl in W:
                continue
            if (pl[0] - 1) % m == 0 and (pl[0] - 1) % p0 != 0:
                sup = pl
                break
        ok(sup is not None,
           "K5: no supplier for rung %d of %s (iteration %d)"
           % (m, show(offender), it))
        W[sup] = 1
        suppliers.append((sup, m))
    L = lam_state(W)
    cost, ties = ideal_menu(W, L)
    print("  suppliers seated: %d" % len(suppliers))
    for sup, m in suppliers:
        print("    %-16s covers rung %d" % (show(sup), m))
    print("  menu at the covering state: cost %d, ties %s"
          % (cost, [(show(p_), r_) for p_, r_ in ties]))
    ok(cost == p0, "K5: menu minimum %d, not p0 = %d" % (cost, p0))
    ok(sorted(pl for pl, r in ties) == sorted(targets)
       and all(r == 1 for _, r in ties),
       "the tie is not exactly the three norm-p0 places at door 1")
    print("  WIDTH 3: the menu's minimum is a three-way tie, the first "
          "in a number ring")

    # the three branches: each forced first move, then greedy
    for tgt in targets:
        st = dict(W)
        st[tgt] = st.get(tgt, 0) + 1
        L2 = lam_state(st)
        locked, run_pl, run = None, None, 0
        for i in range(LB.WALK_CAP):
            c2, t2 = ideal_menu(st, L2)
            p_, r_ = t2[0]
            if p_ == run_pl:
                run += 1
            else:
                run_pl, run = p_, 1
            st[p_] = st.get(p_, 0) + r_
            L2 = lam_state(st)
            if run >= LB.LOCK_R:
                locked = (p_, c2)
                break
        ok(locked is not None, "branch %s does not lock" % show(tgt))
        ok(locked[0] == tgt and locked[1] == p0,
           "branch %s locks %s at %d, not itself at p0"
           % (show(tgt), show(locked[0]), locked[1]))
        print("  branch %s locks itself at %d/move" % (show(tgt), p0))
    print("  three distinct limits from one opening: the width-3 base "
          "realized")


def main():
    s1_ladders()
    p0 = s2_ring()
    s3_ideal_census()
    s4_element_world()
    s5_width(p0)

    section("VERDICT -- the predictions read against what printed")
    print("  P1/P2 the controls, the weld and the sweep: see S1")
    print("  P3 the ring and p0: see S2")
    print("  P4 the bits: see S2")
    print("  P5 the ideal census and the cross-norm tie: see S3")
    print("  P6 the element world: see S4")
    print("  P7 the width: see S5")
    print("\n  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
