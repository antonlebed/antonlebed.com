r"""explore_cubic_carrier.py -- can one ring carry both a HEAD and a
SEATED residue-degree-3 CARRIER? Shop the cubic fields for a ring with 2
INERT and a head somewhere, then walk it and read whether the f = 3
place's own supply is what a deep place's door reads.

THE QUESTION. A place of residue degree 3 over the rational prime q has
N - 1 = q^3 - 1 = (q-1)(q^2+q+1), so it supplies the primes l = 1 mod 3
dividing q^2+q+1 from a rational prime far below anything residue degree
<= 2 reaches, and it ATTAINS the floor any supplier of v_l = k has
(norm >= l^k + 1) where degree <= 2 is slack. That is a PRICE fact and
the corpus has it (explore_cubic_undercut.py; the carrier clause of the
clock corpus). What it has never had is the same fact PAID: every f = 3
place either lives in a ring whose walk seats nothing -- the headless
cubic, which clocks one place forever -- or lives at a norm no menu will
ever charge. The two engines that own f = 3 places have only ever priced
them.

The tension is real and it is arithmetic, not accident. A supply is cheap
at degree 3 only when q is SMALL: q = 2 supplies 7 at norm 8, where
degree <= 2 needs 29; q = 3 supplies 13 at norm 27 against 53. So the
cheap carrier wants 2 INERT. But the corpus's one headed cubic ring has
2 SPLIT (that is where its head lives, an unramified f = 1 place over 2),
and its cheapest f = 3 place is the inert 7 at norm 343 -- an order of
magnitude past anything its walks charge. This file asks whether one ring
can hold both, and the head criterion says exactly where to look.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The shopping
half is written in the FIELD's words -- inert, residue degree, place norm
-- and the reading half in the WALKER's -- door, menu, seated, supply.
The welding term is CARRIER, and it belongs to the walker: a place is a
carrier for a seated place P over l when v_l(L) is set by that place's
own residue cardinality rather than by P's own ladder. Nothing in the
shopping half may be read as a walk result and nothing in the walking
half as a fact about the field.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From explore_headed_cubic_walk.py: the head-holds-the-walk reading
    (a head at the cheapest place absorbs the trajectory at 2/move) is
    a HEAD-AT-2 fact. Here the head is forced to sit over 3 with e = 2,
    a TAME ramified place, and its recurrent price is 3/move against a
    universe whose cheapest f = 3 place charges 8. Nothing about which
    place wins a menu is carried; every menu below is computed.
 T2 The class group is NOT carried and NOT computed. The carrier
    question is about residue degree and door arithmetic; h enters
    neither. Dropping it is a deliberate narrowing of the shop, and it
    means no element-world reading appears in this file at all.
 T3 The head criterion arrives at its surviving form (rule in range,
    explore_head_width.py F2): headed iff f = 1, e = (p-1)p^t, and mu_p
    lies in the completion. It is a PREDICTION here; the brute ladder's
    excess -- longest run of one lambda value, less e -- is the verdict,
    exactly as the shop that first used it did.
 T4 The deep-depth licence for a non-standard column is the LOGARITHM,
    imported as a derivation and re-checked per column: the p-th power
    map carries U_a isomorphically onto U_(a+e) once a > e/(p-1), so from
    there the column satisfies lambda(a+e) = p*lambda(a) EXACTLY. The
    threshold this file uses, a0 = floor(e*p/(p-1)) + 1, is deliberately
    LOOSER than that bound rather than equal to it -- it costs a rung or
    two of brute and removes the need to argue the boundary case. The
    brute checks the recurrence on its own tail; the closed form is
    licensed past the brute by the inequality and never by extrapolation.

THE HAND-ATTACK, on paper before any engine code.

  WHERE A HEAD CAN SIT WHEN 2 IS INERT. The criterion needs f = 1 and
  e = (p-1)p^t. In a cubic field e <= 3, so (p-1)p^t <= 3 leaves exactly
  three shapes: p = 2 with e = 1 or e = 2, and p = 3 with e = 2 (t = 0;
  e = 6 does not fit in degree 3). If 2 is INERT its one place has
  f = 3, killing both p = 2 shapes outright. So in a cubic field with 2
  inert a head can sit ONLY at a place over 3 with e = 2 and f = 1 --
  the partially ramified shape, 3O = P^2 * Q with both places of norm 3
  -- and only when the completion holds mu_3, i.e. is Q_3(zeta_3) =
  Q_3(sqrt -3) rather than the other ramified quadratic Q_3(sqrt 3).
  That is a two-line consequence of the criterion and it is the whole
  shopping spec: the field must be partially ramified at 3, with the
  right one of the two ramified quadratic completions, and irreducible
  mod 2. S2 states it and S3 checks it at every field it enumerates --
  no headed place anywhere with p >= 5 or with f >= 2.

  THE COLUMN AT THAT HEAD. K_v = Q_3(zeta_3), e = 2, f = 1, so
  |(O/P^a)^*| = 2 * 3^(a-1) and lambda = 2 * 3^c(a). pi = zeta_3 - 1 has
  pi^2 = -3*zeta_3, so 3 is a unit times pi^2. For x of valuation j,
  (1+x)^3 = 1 + 3x + 3x^2 + x^3 with the three terms at valuations
  j+2, 2j+2, 3j: at j >= 2 the minimum is j+2 alone, so U_j^3 lies in
  U_(j+2) and no deeper -- the standard step. At j = 1 the first and
  third terms TIE at valuation 3 and the tie is never broken by the
  residue field: writing x = u*pi, 3x + x^3 = pi^3 * (u*(-zeta_3) + u^3)
  and over F_3 every unit residue satisfies u^3 = u, so the bracket
  vanishes mod pi and the cube lands at depth >= 4. That extra rung is
  the head: one flat step at the bottom, excess 1 against e = 2. The
  brute is the check, not the licence.

  THE CARRIER, and what it must be read against. With 2 inert the ring's
  one place over 2 is Q2, norm 8, N - 1 = 7 -- and 7 is the WHOLE of
  q^2+q+1 at q = 2, since q - 1 = 1. So nothing has to be disentangled:
  every bit of what Q2 supplies is the degree-3 factor, and a degree-1 or
  degree-2 place over 2 would supply nothing at all. The consumer is a
  place P over 7 with e = f = 1: lambda(P^b) = 6 * 7^(b-1), so
  v_7(lambda(P^b)) = b - 1 and P's door at depth a is the least r with
  a + r - 1 > v_7(L). Seat P at depth 1 with no other 7-supply and
  v_7(L) = 0: door 1, cost 7. Seat Q2 beside it and v_7(L) = 1: door 2,
  cost 49. So the carrier's whole visible effect is one door step, and
  the ABLATION -- the same state with Q2 removed -- is the control that
  says the step is Q2's and not the state's.

  THE PRICE PAID, in the same ring. The cheapest place of residue degree
  <= 2 that supplies v_7 >= 1 needs norm p = 1 mod 7 (the smallest is 29)
  or norm p^2 with p = +-1 mod 7 (the smallest is 169), whichever the
  ring actually holds. Against norm 8 that is the undercut, charged on a
  menu rather than read off a table.

  WHAT A GREEDY WALK WILL DO, and why the census is the honest half.
  From the void every door is 1 and the menu is the norm order, so the
  cheapest place wins: norm 3 -- the head itself. A head at 3/move
  undercuts a norm-8 place forever, so the void walk should lock on the
  head and seat nothing else, and no seed of the small belt should ever
  charge 8 while a norm-3 door stands at 1. The census measures that
  rather than assuming it; the carrier state is then PLANTED, which is
  what the width construction of the headed-cubic walk already does and
  what the clock corpus's own excess readings do.

  DISTRUST THE MARGIN. The derived half is the door arithmetic at P and
  the e <= 3 head census; both are brute-checked (S1, S2). The vibes
  half: "a field with 2 inert and a head over 3 exists in the box" is
  asserted by the enumeration or reported as its own finding (K2), and
  "the belt never seats Q2" is a SCOPE, not a claim.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 The controls reproduce: the headed cubic's norm-2 column
     1,2,2,4,8,16,32 with excess 1 and its norm-4 and norm-3 columns
     standard; the headless cubic's 2 read INERT with f = 3 and excess 0
     at every place of norm <= 27. 0 disagreements.
  P2 Over every field the box enumerates, every place with brute excess
     >= 1 has f = 1 and (p, e) in {(2,1), (2,2), (3,2)} -- 0 headed
     places at p >= 5, 0 at f >= 2.
  P3 The shop prints a first field with 2 INERT and a headed place inside
     |d| <= 2000, its head sits over 3 with e = 2 and f = 1, and its
     brute column shows excess 1 with the recurrence lambda(a+2) =
     3*lambda(a) holding from a = 4 on.
  P4 At the winner: the f = 3 place over 2 has norm 8 and N - 1 = 7,
     and the cheapest place of residue degree <= 2 in the SAME ring
     supplying v_7 >= 1 has norm >= 29. The undercut ratio printed is
     >= 3.6.
  P5 The void walk locks on the head at 3/move, and across the norm <= 40
     seed belt NO walk seats the norm-8 place: the seated-place census
     over every walked state contains no f = 3 place.
  P6 At the planted carrier state -- Q2 seated at depth 1 beside P7
     seated at depth 1 -- the door at P7 reads 2 with Q2 present and 1
     with Q2 ablated, and the menu's chosen move differs between the two
     states: the f = 3 place's supply re-prices the walk.

KILL-SHAPES, as observables.
  K1 a control column disagrees with a filed one: the instrument is
     wrong and nothing below is readable; the run stops loudly.
  K2 no field with 2 inert and a headed place inside the cap: the cap is
     raised once and the run repeated; still none is printed as the
     finding, and the structural law of S2 is then the whole result.
  K3 the winner's head fails its brute (excess 0 at every place): the
     criterion's mu_3 clause was misread at this completion; printed
     with the column.
  K4 the ablation shows NO door change at P7: the f = 3 supply is not
     load-bearing in that state; printed with the state and the two
     doors -- a finding about the construction, not a silent skip.
  K5 the recurrence lambda(a+e) = p*lambda(a) fails inside the brute
     range at or above a0 = floor(e*p/(p-1)) + 1: the deep-depth licence
     does not hold for this column and no walk that reaches past the
     brute may be read; the run stops loudly.

THE POSITIVE CONTROL (S1, run before any verdict is read). The column
instrument and the place reader are run against the two cubic rings the
corpus has already filed -- the headed d = -283 ring and the headless
d = -23 ring -- and only then is any new field read.

THE SECTIONS.
  S1  positive control: the two filed cubic rings, columns and shapes.
  S2  the structural law: where a head can sit in a cubic field, derived
      and then checked over the whole enumeration.
  S3  the shop: fields in |d| order, 2's shape, the cheapest f = 3 place,
      the head census; the first field with 2 inert AND a head.
  S4  the price in-ring: what the f = 3 place supplies and what degree
      <= 2 would charge for the same supply in the same ring.
  S5  the walk: the void, the seed belt census, and the planted carrier
      state with its ablation control.

FINDINGS (tiers inline; run record at the bottom; every section asserts).

F1 A HEAD AND A CHEAP f = 3 PLACE ARE COMPATIBLE, AND THE HEAD HAS EXACTLY
   ONE PLACE LEFT TO SIT AT (rule, conditional on the head criterion's
   own rule-in-range tier; the derivation is the two-line one above and
   the census checks it at 331 fields -- 1529 places brute-read to depth
   3, 0 excess off the three shapes, plus 623 whose residue cap stopped
   the brute short of a verdict, every one of them f >= 2 or p >= 5 and
   so headless by the criterion without a brute). Since e <= 3 in a
   cubic field, e = (p-1)p^t admits only (p, e) = (2,1), (2,2), (3,2),
   so 2 INERT -- which is what makes the carrier cost 8 rather than 343
   -- kills both p = 2 shapes and leaves the partially ramified place
   over 3 as the ONLY seat a head can take. That is not an obstruction:
   88 of the 331 fields enumerated to |d| <= 2000 have 2 inert, 9 of
   those carry a head, and every one of the 9 carries it at exactly the
   predicted place, p = 3 with e = 2, f = 1, excess 1. So the
   configuration the clock corpus records as unmeasured was never
   blocked -- it was unshopped.

F2 THE RING: d = 321, K = Q[x]/(x^3 - x^2 - 6x - 3), totally real (rule in
   range; the Hunter box at |d| <= 2000, 3906 polynomials, 331 fields,
   identification per the shop's fingerprint assumption). It is the
   first field by |d| passing all three gates -- 2 inert (one place,
   norm 8, N - 1 = 7), a head (over 3, e = 2, f = 1), and a degree-1
   place over 7 for the supply to be read BY. The first two gates alone
   are met earlier, at d = -255, whose 7 is itself inert: 5 of the 9
   two-gate fields hold a degree-1 consumer and 4 do not, so the third
   gate is a real filter and not bookkeeping. The head column reads
   2,6,6,6,18,18,54,54 -- the flat run 3 against e = 2, excess 1, the
   hand-derived tie at valuation 1 confirmed -- and satisfies
   lambda(a+2) = 3*lambda(a) at every depth from a0 = 4, checked at 3
   depths inside the brute range and licensed past it by the logarithm.

F3 THE UNDERCUT, CHARGED IN ONE RING RATHER THAN READ OFF A TABLE (property
   of this ring's universe). The f = 3 place over 2 supplies 7 -- the
   whole of q^2+q+1 at q = 2, since q - 1 = 1, so there is no degree-<=
   2 component of its supply to disentangle -- at norm 8. The cheapest
   place of residue degree <= 2 in the SAME ring supplying v_7 >= 1 is
   the degree-1 place over 29, at norm 29: a menu factor of 3.62. The
   two prices are the same table entry the cubic-undercut rig printed,
   now standing in one universe where a walk can pay either.

F4 THE f = 3 PLACE SERVES AS A CARRIER ON A WALK -- the reading the clock
   corpus filed as "not measured" (observation; 3 of 35 seeds over the
   norm <= 64 belt, the ablation run at all 397 walked states). The
   first: from seed 7[e1,f2] the walk seats the norm-8 place, and at
   that state the f = 2 place over 7 has v_7(L) = 1 supplied by the
   norm-8 place's own N - 1 and by nothing else -- its door reads 2
   where the ablated state reads 1, and since that consumer's NORM is 49
   rather than 7 the menu price it moves is 2401 against 49. Removing
   the carrier is the whole test: a supply that changes no door is not a
   carrier, and F5 says why every state that seats the pair passes it.
   The walks also lock ON an f = 3 place once (the norm-8 place at
   8/move, 1 of 35 seeds), which no walk in this corpus had done either.
   AND THE HAND-ATTACK WAS WRONG ABOUT THIS, which is the correction P5
   bought: it expected the head at 3/move to undercut a norm-8 place
   forever, so that no belt seed would ever charge 8. The FROZEN belt
   refutes it on its own -- 6 of 21 walks move on the norm-8 place, and
   all 6 moves are on that place rather than a deeper f = 3 one. The
   error was reading 3/move, which is the head's LOCKED recurrent price,
   as the price it charges from any state: seated at depth 2 the head's
   own door is 3 and it charges 27, and a seed of norm 31 lifts that
   door to 5 and 243. A head undercuts the universe only from states
   that leave its door at 1.

F5 THE SUPPLY BITES ONLY WHILE THE CONSUMER IS SHALLOW, AND THE CARRIER
   HOLDS IT THERE (rule in range for the arithmetic, observation for the
   census: 33 coincidence states, all 33 load-bearing, consumer depth 1
   at every one). A seated place P over l supplies v_l = ceil((a-1)/e_P)
   at depth a from its OWN standard ladder, so a carrier supplying v_l =
   k is load-bearing at P only while ceil((a-1)/e_P) < k, which is a <=
   e_P*(k-1) + 1. The consumer's RESIDUE DEGREE never enters -- the
   census's own first carrier state has an f = 2 consumer -- and its
   RAMIFICATION cancels out of the window at k = 1, where the bound
   reads a <= 1 for every e_P. So at k = 1 -- which is all a norm-8
   place can give, since 7 || 7 -- the window is the single depth a = 1
   whatever the consumer is, and only a carrier supplying k >= 2 could
   buy a ramified consumer any more room.
   THE STANDARD LADDER IS THE SCOPE OF THAT, and it is narrower than the
   sentence reads: the window above is the HEADLESS one (narrower still,
   SETTLED SINCE: the TAME one, e <= p - 1 -- a wild headless column is
   not the staircase, explore_wild_ring.py), exact at a
   consumer whose column holds no extra flat step and departing from
   k = 2 on at one that does -- wider at some, NARROWER at others, with
   no single correction, since a head's transient makes a column climb
   fast at the bottom before it flattens (explore_carrier_window.py,
   which also prices k >= 2: cheap at l = 2 and at no l this file's
   degree-3 route can reach). The k = 1 reading is untouched -- the
   window is the single depth 1 at every consumer measured, headed or
   not -- and this file's own consumers over 7 are headless anyway, so
   every reading below stands as stated.
   The window does not merely
   happen to hold: the raised door prices the consumer OUT of the menu
   -- a door of 2 costs its norm SQUARED -- so the walk stops moving it
   and it stays at depth 1. The carrier keeps ITSELF load-bearing, which
   is why the census finds no coincidence state outside the window
   rather than a few inside it. That is also why the frozen norm <= 40
   belt read 0: the configuration needs both places in one state and 7 *
   8 = 56 exceeds 40, so the frozen belt could not hold one at any
   depth. The belt was extended to 64 for that arithmetic reason and the
   frozen reading stands as printed.

F6 THE CARRIER CHANGES THE LIMIT, NOT ONLY A DOOR (observation at one
   planted pair). At the minimal state {norm-8 place, degree-1 place
   over 7}, both at depth 1, the menu's chosen move differs from the
   ablated state's -- 11 against 7 -- and the two walks lock at
   DIFFERENT places: 11/move with the carrier, 7/move without it. So the
   f = 3 place's supply is not decoration on a door; one seated place of
   residue degree 3 moves where the trajectory ends. This is the sharp
   half of F4's reading and it is planted, not seeded: the seeded
   carriers of F4 are read at their doors.

RUN RECORD. `python explore_cubic_carrier.py`, under memwatch.py. One
process, CPython, no BLAS. 35 checks, 142 s wall (the cost is S3: a brute
lambda column at every place over 2, 3, 5, 7 of all 331 fields), peak
working set 27.7 MB under the 512 MB ceiling. S1: the two filed cubic
rings, columns reproduced, 0 off. S2: the three shapes. S3: 3906
polynomials -> 356 reducible + 2329 over-cap + 1221 kept, 331 fields; 1529
places brute-read and 623 left to the criterion; 88 with 2 inert, 197
headed, 9 passing both, 5 passing all three. S5: void
locks the norm-3 head place at 3/move; frozen belt 21 seeds / 241 states,
0 coincidences, 0 carriers; extended belt 35 seeds / 397 states, 5
seed-contained f = 3 places, 8 walk-seated, 33 coincidence states all
33 load-bearing at consumer depth 1, over 3 seeds; the first carrier
state's consumer is the norm-49 place over 7, door 1 -> 2, cost
49 -> 2401; the consumer is moved 0 further times at all 33, and both
planted menus are 1-way ties, so F6's move difference is not the
tie-break's. Two instrument corrections between the first run and this
one, both caught by reading the prints rather than by an assert: the head
place was located by an index read off ONE generator's maximal order and
then dereferenced against ANOTHER generator of the same field, which is
only safe when the two orders enumerate their places in the same order
(it fired K5 at the winner, since the index landed on a standard column);
the head census dropped a place whose residue cap stopped its brute short
of depth 3 without counting it, which is a silent skip and made the
three-shapes coverage read as complete when 29% of the places carried no
brute verdict at all; and the belt census first counted f = 3 places
seated in the FINAL state,
which cannot tell a place the walk seated from one the seed contained --
the split into seed-contained, walk-seated and load-bearing is the fix,
and it is what makes F4 a walk result. A fourth, and the only one that
put a wrong number in a doc: the census printed a move's cost as
l ** door, the RATIONAL PRIME raised to the door, where a move costs the
PLACE NORM raised to it. The two agree at every f = 1 consumer, which is
what the planted state has, and part at the census's own first carrier
state, whose consumer has f = 2 -- so the printed pair read 49 against 7
where the walk charges 2401 against 49. A third, caught by the audit: the
load-bearing count was reported per SEED beside a coincidence count per
STATE, two scales read as one ratio. Counting both per state is what
turned F5 from "most coincidences fail the ablation" into its opposite.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

sys.setrecursionlimit(20000)

import explore_cubic_ring as CR
import explore_cubic_field_shop as SHOP
import explore_lock_budget as LB

CHECKS = 0

DISC_CAP = 2000       # |d_K| ceiling for the shop
BRUTE_CAP = 15000     # residues allowed in one brute-forced quotient
LADDER_DEPTH = 13     # depths a column is brute-read to
MAXP = 20000          # rational primes enumerated into a walker universe
BELT = 40             # seed belt: generator products of norm <= this
BELT_EXT = 64         # the extension named in S5: 7 * 8 = 56 needs it
PRICE_SCAN = 4000     # rational primes scanned for a degree <= 2 supplier


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def lcm(a, b):
    from math import gcd
    return a // gcd(a, b) * b


def v_p(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def factor(n):
    out, d = [], 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


# ------------------------------------------------- columns and the head read
def brute_column(O, P, q, depth=LADDER_DEPTH):
    """lambda(P^a) for a = 1.. by brute residue walk, while q^a fits the
    residue cap. The instrument is the shop's own."""
    col, a = [], 1
    while q ** a <= BRUTE_CAP and a <= depth:
        col.append(SHOP.unit_exponent_order(O, P, a, q))
        a += 1
    return col


def excess_of(col, e):
    """Longest run of one lambda value above 1, less e -- the brute head
    verdict the shop family uses."""
    if not col or all(x <= 1 for x in col):
        return 0
    best = 0
    run, cur = 0, None
    for x in col:
        if x <= 1:
            run, cur = 0, None
            continue
        if x == cur:
            run += 1
        else:
            cur, run = x, 1
        best = max(best, run)
    return best - e


def log_floor(e, p):
    """a0 = floor(e*p/(p-1)) + 1: the depth past which U_a is additive and
    lambda(a+e) = p*lambda(a) holds exactly (T4)."""
    return (e * p) // (p - 1) + 1


class Column(object):
    """One place's lambda column: brute where the residues fit, extended by
    the logarithm's recurrence past that, never by extrapolation."""

    def __init__(self, p, e, f, brute):
        self.p, self.e, self.f = p, e, f
        self.q = p ** f
        self.brute = list(brute)
        self.a0 = log_floor(e, p)
        self.cache = {0: 1}
        for i, x in enumerate(brute):
            self.cache[i + 1] = x
        self.recurrence_checked = 0
        for a in range(max(self.a0, 1) + e, len(brute) + 1):
            if a - e >= 1:
                ok(brute[a - 1] == p * brute[a - e - 1],
                   "K5: recurrence fails at a = %d for p=%d e=%d f=%d"
                   % (a, p, e, f))
                self.recurrence_checked += 1

    def lam(self, a):
        if a in self.cache:
            return self.cache[a]
        assert a > len(self.brute), "column cache hole at %d" % a
        assert len(self.brute) > self.a0, \
            "no licensed tail: brute depth %d, a0 %d" % (len(self.brute),
                                                         self.a0)
        v = self.p * self.lam(a - self.e)
        self.cache[a] = v
        return v

    def standard(self, a):
        if a == 0:
            return 1
        return (self.q - 1) * self.p ** -(-(a - 1) // self.e)


# ------------------------------------------------------------- the ring model
def factor_shape_poly(mono, p):
    """[(e, f), ...] for the places over p read off the minimal polynomial
    mod p. Dedekind, valid at every p because the caller supplies a
    polynomial of index 1 (disc(poly) = d_K)."""
    f = mono
    g = CR.pgcd(f, CR.pderiv(f, p), p)
    dg = len(g) - 1
    if dg == 3:
        return [(3, 1)]                       # f' = 0 and f a cube
    if dg == 2:
        return [(3, 1)]
    if dg == 1:
        return [(2, 1), (1, 1)]
    assert dg == 0, "unreadable factor shape at %d" % p
    sub = list(CR.ppowmod((0, 1), p, f, p))
    while len(sub) < 2:
        sub.append(0)
    sub[1] -= 1
    nr = len(CR.pgcd(tuple(sub), f, p)) - 1
    if nr <= 0:
        return [(1, 3)]
    if nr == 1:
        return [(1, 1), (1, 2)]
    assert nr == 3, "a squarefree cubic with %d roots mod %d" % (nr, p)
    return [(1, 1), (1, 1), (1, 1)]


class Model(object):
    """A walker model over one cubic field: places (p, e, f, i), the lambda
    columns, doors and the ideal menu. Shaped for the imported walker."""

    def __init__(self, abc, d, O, maxp=MAXP):
        self.abc, self.d, self.O = abc, d, O
        a, b, c = abc
        self.mono = (c, b, a, 1)
        ok(SHOP.poly_disc3(a, b, c) == d,
           "model polynomial has index > 1: disc %d against d_K %d"
           % (SHOP.poly_disc3(a, b, c), d))
        self.UNIVERSE = []
        for p in CR.PRIMES:
            if p > maxp:
                break
            seen = {}
            for (e, f) in factor_shape_poly(self.mono, p):
                i = seen.get((e, f), 0)
                seen[(e, f)] = i + 1
                self.UNIVERSE.append((p, e, f, i))
        self.UNIVERSE.sort(key=self.place_key)
        self.columns = {}

    # ---- place accessors
    def place_norm(self, pl):
        return pl[0] ** pl[2]

    def place_key(self, pl):
        return (pl[0] ** pl[2], pl[1], pl[2], pl[3])

    def show(self, pl):
        return "%d[e%d,f%d]%s" % (pl[0], pl[1], pl[2],
                                  ".%d" % pl[3] if pl[3] else "")

    def show_st(self, st):
        parts = ["%s^%d" % (self.show(pl), e)
                 for pl, e in sorted(st.items(), key=lambda kv:
                                     self.place_key(kv[0])) if e]
        return "*".join(parts) if parts else "(1)"

    # ---- the lambda column
    def set_column(self, pl, col):
        self.columns[pl] = col

    def lam_P(self, pl, a):
        if a == 0:
            return 1
        col = self.columns.get(pl)
        if col is not None:
            return col.lam(a)
        p, e = pl[0], pl[1]
        return (self.place_norm(pl) - 1) * p ** -(-(a - 1) // e)

    def lam_state(self, st):
        L = 1
        for pl, e in st.items():
            L = lcm(L, self.lam_P(pl, e))
        return L

    def door_r(self, pl, e, L):
        r = 1
        while L % self.lam_P(pl, e + r) == 0:
            r += 1
            assert r < 500, "door search runaway"
        return r

    def ideal_menu(self, st, L):
        best, ties = None, []
        for pl in self.UNIVERSE:
            nrm = self.place_norm(pl)
            if best is not None and nrm > best:
                break
            r = self.door_r(pl, st.get(pl, 0), L)
            cost = nrm ** r
            if best is None or cost < best:
                best, ties = cost, [(pl, r)]
            elif cost == best:
                ties.append((pl, r))
        assert best <= MAXP, "universe guard: door beyond MAXP"
        ties.sort(key=lambda t: self.place_key(t[0]))
        return best, ties

    def gen_products(self, maxnorm):
        pls = [pl for pl in self.UNIVERSE
               if self.place_norm(pl) <= maxnorm]
        out = []

        def rec(i, cur, nrm):
            if cur:
                out.append((nrm, dict(cur)))
            for j in range(i, len(pls)):
                pl = pls[j]
                n2 = nrm * self.place_norm(pl)
                if n2 > maxnorm:
                    break
                e = 1
                while n2 <= maxnorm:
                    cur[pl] = e
                    rec(j + 1, cur, n2)
                    e += 1
                    n2 *= self.place_norm(pl)
                del cur[pl]

        rec(0, {}, 1)
        out.sort(key=lambda x: x[0])
        return out


SKIPPED = []   # places the brute could not read to depth 3: reported,
               # never dropped in silence (the head verdict needs a run)


def head_census(O, primes=(2, 3, 5, 7, 11)):
    """Every place over the given primes with its brute column, excess and
    the criterion's prediction. A place whose residue cap stops the brute
    short of depth 3 carries NO excess verdict -- a run of one value needs
    three rungs to be told from a standard column -- so it is appended to
    SKIPPED and counted there. The criterion, not the brute, is what
    covers those: f >= 2 is headless outright and e <= 3 < (p-1) at every
    p >= 5, so no skipped place could have been headed."""
    rows = []
    for p in primes:
        for i, (P, e, f) in enumerate(SHOP.maximal_places(O, p)):
            q = p ** f
            col = brute_column(O, P, q)
            if len(col) < 3:
                SKIPPED.append((p, e, f))
                continue
            exc = excess_of(col, e)
            pred = False
            if f == 1:
                t = p - 1
                while t <= e:
                    if t == e:
                        pred = True
                    t *= p
            rows.append((p, i, e, f, col, exc, pred, P))
    return rows


# ------------------------------------------------------ S1 positive control
FILED_283 = (0, 4, 1)     # x^3 + 4x + 1, d = -283, the headed cubic
FILED_23 = (0, -1, -1)    # x^3 - x - 1, d = -23, the headless cubic


def s1_control():
    section("S1  POSITIVE CONTROL -- the two filed cubic rings")
    O283, d283 = SHOP.maximal_order(*FILED_283)
    ok(d283 == -283, "control field 1 has d = %d, not -283" % d283)
    rows = head_census(O283, primes=(2, 3, 5))
    print("  d = -283 (the headed cubic):")
    seen2 = {}
    for (p, i, e, f, col, exc, pred, P) in rows:
        print("    p=%d.%d e=%d f=%d norm %-4d col %-28s excess %d"
              % (p, i, e, f, p ** f,
                 ",".join(str(x) for x in col[:7]), exc))
        if p == 2:
            seen2[f] = (col, exc)
    ok(1 in seen2 and 2 in seen2, "d=-283 does not show 2 as split 1+2")
    col2, exc2 = seen2[1]
    ok(col2[:7] == [1, 2, 2, 4, 8, 16, 32],
       "K1: the filed head column 1,2,2,4,8,16,32 is not reproduced: %s"
       % col2[:7])
    ok(exc2 == 1, "K1: the filed head excess 1 is not reproduced: %d" % exc2)
    col4, exc4 = seen2[2]
    ok(all(col4[a] == 3 * 2 ** a for a in range(len(col4))),
       "K1: the filed norm-4 column 3*2^(a-1) is not reproduced: %s" % col4)
    ok(exc4 == 0, "K1: the norm-4 place reads a head: excess %d" % exc4)
    print("    filed head column and the standard norm-4 column reproduced.")

    O23, d23 = SHOP.maximal_order(*FILED_23)
    ok(d23 == -23, "control field 2 has d = %d, not -23" % d23)
    rows23 = head_census(O23, primes=(2, 3))
    print("  d = -23 (the headless cubic):")
    shape2 = [(e, f) for (p, i, e, f, col, exc, pred, P) in rows23 if p == 2]
    for (p, i, e, f, col, exc, pred, P) in rows23:
        print("    p=%d.%d e=%d f=%d norm %-4d col %-28s excess %d"
              % (p, i, e, f, p ** f,
                 ",".join(str(x) for x in col[:7]), exc))
    ok(shape2 == [(1, 3)], "K1: 2 is not inert in the d=-23 field: %s"
       % shape2)
    ok(all(exc <= 0 for (p, i, e, f, col, exc, pred, P) in rows23),
       "K1: the headless cubic reads a head")
    print("    2 INERT, norm 8, N-1 = 7 -- the cheap carrier, in the ring")
    print("    that has no head. Every place read excess 0.")
    return O283, O23


# ------------------------------------------------- S2 where a head can sit
def s2_structural():
    section("S2  THE STRUCTURAL LAW -- where a head can sit in a cubic "
            "field")
    shapes = []
    for p in (2, 3, 5, 7, 11, 13):
        for e in (1, 2, 3):
            t, good = p - 1, False
            while t <= e:
                if t == e:
                    good = True
                t *= p
            if good:
                shapes.append((p, e))
    print("  criterion shapes with e <= 3 (f = 1 required): %s"
          % ", ".join("p=%d e=%d" % s for s in shapes))
    ok(shapes == [(2, 1), (2, 2), (3, 2)],
       "the e <= 3 head shapes are %s, not the three derived" % shapes)
    print("  so: 2 inert (f = 3) kills both p = 2 shapes, and the only")
    print("  survivor is a place over 3 with e = 2, f = 1 -- the partially")
    print("  ramified shape, with the completion holding mu_3.")
    return shapes


# ------------------------------------------------------------- S3 the shop
def s3_shop(cap):
    section("S3  THE SHOP -- cubic fields to |d| <= %d: 2's shape, the "
            "cheapest f = 3 place, the head census" % cap)
    fields, counts = SHOP.enumerate_fields(cap)
    n_poly, n_red, n_over, n_kept = counts
    print("  %d polynomials: %d reducible, %d over cap, %d kept -> %d fields"
          % (n_poly, n_red, n_over, n_kept, len(fields)))
    ok(n_red + n_over + n_kept == n_poly, "bucket counts do not sum")
    n_inert2 = 0
    n_headed = 0
    n_read = 0
    del SKIPPED[:]     # S1's controls are counted on their own
    off_shape = []
    two_gate = []
    winner = None
    print("  the three gates: 2 INERT (the carrier at norm 8), a HEAD")
    print("  somewhere, and a degree-1 place over 7 (the consumer -- the")
    print("  only prime a norm-8 place supplies, since N - 1 = 7).")
    print("  %-7s %-9s %-22s %-14s %s"
          % ("d", "2-shape", "head", "7-shape", "gates"))
    for (ad, d, cx, polys) in fields:
        a, b, c, O = polys[0]
        pl2 = SHOP.maximal_places(O, 2)
        shape2 = sorted((e, f) for (P, e, f) in pl2)
        inert2 = shape2 == [(1, 3)]
        if inert2:
            n_inert2 += 1
        rows = head_census(O, primes=(2, 3, 5, 7))
        n_read += len(rows)
        heads = [(p, i, e, f, col, exc) for (p, i, e, f, col, exc, pred, P)
                 in rows if exc >= 1]
        for (p, i, e, f, col, exc) in heads:
            if f != 1 or (p, e) not in ((2, 1), (2, 2), (3, 2)):
                off_shape.append((d, p, e, f, exc))
        if heads:
            n_headed += 1
        if not (inert2 and heads):
            continue
        shape7 = sorted((e, f) for (P, e, f) in SHOP.maximal_places(O, 7))
        consumer = any(f == 1 for (e, f) in shape7)
        two_gate.append((d, shape7, consumer))
        hd = ", ".join("p=%d e=%d f=%d exc %d" % (p, e, f, exc)
                       for (p, i, e, f, col, exc) in heads)
        print("  %-7d %-9s %-22s %-14s %s"
              % (d, "inert", hd,
                 "+".join("e%df%d" % s for s in shape7),
                 "3/3" if consumer else "2/3 (no f=1 over 7)"))
        if consumer and winner is None:
            winner = (d, cx, polys)
    print("  places the brute read to depth 3: %d;  places its residue cap"
          " stopped short, verdict left to the criterion: %d"
          % (n_read, len(SKIPPED)))
    ok(all(f >= 2 or p >= 5 for (p, e, f) in SKIPPED),
       "a skipped place the criterion does not cover: %s"
       % [t for t in SKIPPED if t[2] < 2 and t[0] < 5][:5])
    print("  every skipped place has f >= 2 or p >= 5 -- headless by the")
    print("  criterion without a brute, which is what makes the census's")
    print("  coverage of the three shapes complete rather than sampled.")
    print("  fields with 2 inert: %d;  fields with a headed place: %d;"
          % (n_inert2, n_headed))
    print("  fields passing both of the first two gates: %d, of which %d "
          "also hold a degree-1 place over 7"
          % (len(two_gate), sum(1 for t in two_gate if t[2])))
    ok(not off_shape,
       "P2 broken: headed places off the three shapes: %s" % off_shape[:5])
    print("  0 headed places off the three derived shapes (P2).")
    return fields, two_gate, winner


# ----------------------------------------------------- S4 the price in-ring
def cheapest_low_degree_supplier(M, ell, kmin=1):
    """Cheapest place of residue degree <= 2 in M's own universe whose
    N - 1 carries v_ell >= kmin."""
    best = None
    for pl in M.UNIVERSE:
        if pl[2] >= 3:
            continue
        n = M.place_norm(pl)
        if n > PRICE_SCAN:
            break
        if v_p(n - 1, ell) >= kmin:
            if best is None or n < best[0]:
                best = (n, pl)
    return best


def s4_price(M, Q2):
    section("S4  THE PRICE IN-RING -- what the f = 3 place supplies and "
            "what degree <= 2 would charge for it")
    n8 = M.place_norm(Q2)
    supply = n8 - 1
    print("  the f = 3 place over 2: norm %d, N - 1 = %d = (q-1)(q^2+q+1) "
          "= %d * %d" % (n8, supply, 1, 7))
    ok(n8 == 8 and supply == 7, "the f=3 place over 2 is not norm 8")
    ells = sorted(set(factor(supply)))
    print("  primes it supplies: %s (all of them from q^2+q+1, since "
          "q - 1 = 1)" % ells)
    rows = []
    for ell in ells:
        best = cheapest_low_degree_supplier(M, ell)
        ok(best is not None,
           "no degree <= 2 supplier of %d below norm %d" % (ell, PRICE_SCAN))
        rows.append((ell, best[0], best[1]))
        print("    l = %d: degree <= 2 needs norm %d (%s) against norm %d "
              "-- undercut %.2fx"
              % (ell, best[0], M.show(best[1]), n8, best[0] / float(n8)))
    ok(all(r[1] >= 29 for r in rows),
       "P4 broken: a degree <= 2 supplier under norm 29: %s" % rows)
    return rows


# ------------------------------------------------------------- S5 the walk
def seated_places(st):
    return [pl for pl, e in st.items() if e]


def carrier_scan(M, st):
    """Every load-bearing carrier configuration at one state: a seated
    place Q whose OWN residue cardinality N(Q) - 1 sets v_l(L) for a
    prime l, beside a seated place P over that same l whose door is
    strictly larger with Q than without it. The ablation is the whole
    test -- a supply that changes no door is not a carrier."""
    out = []
    L = M.lam_state(st)
    for Q in seated_places(st):
        nq = M.place_norm(Q)
        st_ab = dict(st)
        del st_ab[Q]
        L_ab = M.lam_state(st_ab)
        for ell in sorted(set(factor(nq - 1))):
            for P in seated_places(st):
                if P == Q or P[0] != ell:
                    continue
                a = st[P]
                d1 = M.door_r(P, a, L)
                d0 = M.door_r(P, a, L_ab)
                if d1 > d0:
                    out.append((Q, P, ell, d1, d0,
                                v_p(L, ell), v_p(L_ab, ell)))
    return out


def walk_trace(M, seed, cap=None):
    """The greedy walk as a list of (state, L, move) triples, one per move,
    stopping at the same lock witness the imported walker uses."""
    st = dict(seed)
    L = M.lam_state(st)
    run_pl, run = None, 0
    trace = []
    for i in range(cap or LB.WALK_CAP):
        cost, ties = M.ideal_menu(st, L)
        pl, r = ties[0]
        trace.append((dict(st), L, (pl, r, cost)))
        run = run + 1 if pl == run_pl else 1
        run_pl = pl
        st = dict(st)
        st[pl] = st.get(pl, 0) + r
        L = M.lam_state(st)
        if run >= LB.LOCK_R:
            break
    trace.append((dict(st), L, None))
    return trace


def census(M, belt, tag):
    """The seed belt walked with the carrier scan run at EVERY state, not
    only at the lock: seed-contained f = 3 places, walk-seated ones, and
    the load-bearing configurations, kept apart."""
    seeds = M.gen_products(belt)
    lock_places = {}
    seed_f3 = 0        # the f = 3 place was in the SEED
    walk_f3 = 0        # the WALK made a move on an f = 3 place
    carrier_seeds = 0  # some state along the walk carries a load-bearing
    walked = 0         # f = 3 supply another seated place's door reads
    n_states = 0
    after = {}         # moves ON the consumer at/after a load-bearing
    cdepth = {}        # state; consumer DEPTH at each coincidence
    carrier_states = 0  # STATES, not seeds: the comparable count to the
    coincidences = 0   # both an f = 3 place and a place over one of the
    first_carrier = None                     # primes it supplies, seated
    for (nrm, seed) in seeds:
        if LB.walk_to_lock(M, seed) is None:
            continue
        walked += 1
        trace = walk_trace(M, seed)
        if any(p[2] >= 3 for p in seated_places(seed)):
            seed_f3 += 1
        if any(mv is not None and mv[0][2] >= 3 for (_, _, mv) in trace):
            walk_f3 += 1
        st, L, pl, cost, steps = LB.walk_to_lock(M, seed)
        lock_places[(M.show(pl), cost)] = lock_places.get(
            (M.show(pl), cost), 0) + 1
        hit = False
        for i, (stt, LL, mv) in enumerate(trace):
            n_states += 1
            f3s = [p for p in seated_places(stt) if p[2] >= 3]
            for Q in f3s:
                ells = set(factor(M.place_norm(Q) - 1))
                cons = [P for P in seated_places(stt)
                        if P != Q and P[0] in ells]
                if cons:
                    coincidences += 1
                    for cpl in cons:
                        cdepth[stt[cpl]] = cdepth.get(stt[cpl], 0) + 1
                    break
            rows = [r for r in carrier_scan(M, stt) if r[0][2] >= 3]
            if rows:
                hit = True
                carrier_states += 1
                # the mechanism, as an observable: once the door is up,
                # is the consumer ever moved again on this walk?
                Pc = rows[0][1]
                later = sum(1 for (_, _, m) in trace[i:]
                            if m is not None and m[0] == Pc)
                after[later] = after.get(later, 0) + 1
                if first_carrier is None:
                    first_carrier = (seed, stt, rows)
        if hit:
            carrier_seeds += 1
    print("\n  %s: %d seeds of norm <= %d, %d locked over %d walked states"
          % (tag, len(seeds), belt, walked, n_states))
    print("    lock places %s" % sorted(lock_places.items()))
    print("    seeds that already CONTAIN an f = 3 place:      %d" % seed_f3)
    print("    seeds whose WALK moves on an f = 3 place:       %d" % walk_f3)
    print("    states seating an f = 3 place BESIDE a consumer: %d"
          % coincidences)
    print("    of those, states where the supply is LOAD-BEARING: %d"
          % carrier_states)
    print("    consumer DEPTH at those states: %s"
          % (sorted(cdepth.items()) or "-"))
    print("    further moves ON that consumer, at or after: %s"
          % (sorted(after.items()) or "-"))
    print("    seeds carrying a LOAD-BEARING f = 3 supply:     %d"
          % carrier_seeds)
    ok(carrier_states <= coincidences,
       "a load-bearing state that seats no consumer: %d > %d"
       % (carrier_states, coincidences))
    if first_carrier is not None:
        seed, stt, rows = first_carrier
        Q, P, ell, d1, d0, v1, v0 = rows[0]
        print("    first such state, from seed %s:" % M.show_st(seed))
        nP = M.place_norm(P)
        print("      state %s: carrier %s (norm %d) supplies l = %d, "
              "v_l(L) %d -> %d, door at %s (norm %d) %d -> %d "
              "(cost %d -> %d)"
              % (M.show_st(stt), M.show(Q), M.place_norm(Q), ell, v0, v1,
                 M.show(P), nP, d0, d1, nP ** d0, nP ** d1))
    return (len(seeds), walked, n_states, seed_f3, walk_f3, coincidences,
            carrier_states, carrier_seeds, cdepth, after, first_carrier)


def s5_walk(M, Q2, head_pl):
    section("S5  THE WALK -- the void, the belt census, and the planted "
            "carrier state")
    got = LB.walk_to_lock(M, {})
    ok(got is not None, "the void walk does not lock inside the cap")
    st, L, pl, cost, steps = got
    print("  void walk: locks %s at %d/move after %d moves, state %s"
          % (M.show(pl), cost, steps, M.show_st(st)))
    void_lock = (pl, cost)

    census(M, BELT, "the frozen belt")
    print("\n  THE BELT IS EXTENDED, and the reason is arithmetic rather")
    print("  than a second try: the carrier configuration needs BOTH the")
    print("  norm-8 place and a place over 7 in one state, and 7 * 8 = 56")
    print("  exceeds 40 -- the frozen belt cannot hold one, whatever the")
    print("  walks do. The frozen reading above stands; this is a new one.")
    ext = census(M, BELT_EXT, "the extended belt")

    # ---- the planted carrier state
    P7 = None
    for pl in M.UNIVERSE:
        if pl[0] == 7 and pl[1] == 1 and pl[2] == 1:
            P7 = pl
            break
    ok(P7 is not None, "the winner ring holds no degree-1 place over 7")
    st_with = {Q2: 1, P7: 1}
    st_without = {P7: 1}
    L_with = M.lam_state(st_with)
    L_without = M.lam_state(st_without)
    d_with = M.door_r(P7, 1, L_with)
    d_without = M.door_r(P7, 1, L_without)
    print("\n  the carrier state, planted:")
    nP7 = M.place_norm(P7)
    print("    with    Q2: state %s, L = %d, v_7(L) = %d, door at P7 = %d, "
          "cost %d" % (M.show_st(st_with), L_with, v_p(L_with, 7),
                       d_with, nP7 ** d_with))
    print("    without Q2: state %s, L = %d, v_7(L) = %d, door at P7 = %d, "
          "cost %d" % (M.show_st(st_without), L_without,
                       v_p(L_without, 7), d_without, nP7 ** d_without))
    ok(d_with > d_without,
       "K4: the ablation shows no door change at P7 (%d vs %d)"
       % (d_with, d_without))
    ok(v_p(L_with, 7) == 1 and v_p(L_without, 7) == 0,
       "the 7-supply is not Q2's alone: v_7 %d / %d"
       % (v_p(L_with, 7), v_p(L_without, 7)))
    print("    -> the f = 3 place over 2 IS the carrier: its own N - 1 = 7")
    print("       sets v_7(L), and P7's door reads it.")

    c_with, ties_with = M.ideal_menu(st_with, L_with)
    c_without, ties_without = M.ideal_menu(st_without, L_without)
    print("    menu with    Q2: cost %d, move %s^%d (%d-way tie)"
          % (c_with, M.show(ties_with[0][0]), ties_with[0][1],
             len(ties_with)))
    print("    menu without Q2: cost %d, move %s^%d (%d-way tie)"
          % (c_without, M.show(ties_without[0][0]), ties_without[0][1],
             len(ties_without)))
    ok(len(ties_with) == 1 and len(ties_without) == 1,
       "the planted menus tie, so the move difference is the tie-break's: "
       "%d and %d ways" % (len(ties_with), len(ties_without)))
    moved = (ties_with[0] != ties_without[0]) or (c_with != c_without)
    print("    the chosen move %s"
          % ("DIFFERS -- the supply re-prices the walk" if moved
             else "is the same -- the supply is priced in but not decisive"))

    g_with = LB.walk_to_lock(M, st_with)
    g_without = LB.walk_to_lock(M, st_without)
    for tag, g in (("with Q2   ", g_with), ("without Q2", g_without)):
        ok(g is not None, "K5: the carrier walk (%s) does not lock" % tag)
        st, L, pl, cost, steps = g
        print("    walk %s: locks %s at %d/move after %d moves, state %s"
              % (tag, M.show(pl), cost, steps, M.show_st(st)))
    return void_lock, ext, (d_with, d_without, moved)


def main():
    O283, O23 = s1_control()
    s2_structural()
    fields, two_gate, winner = s3_shop(DISC_CAP)
    if winner is None:
        print("\n  K2: no field passing all three gates inside |d| <= %d."
              % DISC_CAP)
        return
    d, cx, polys = winner
    section("THE WINNER -- d = %d" % d)
    idx1 = [(a, b, c, O) for (a, b, c, O) in polys
            if SHOP.poly_disc3(a, b, c) == d]
    ok(idx1, "no index-1 generator for the winner field d = %d" % d)
    a, b, c, O = idx1[0]
    print("  x^3 %+d x^2 %+d x %+d, %s cubic, d = %d"
          % (a, b, c, "complex" if cx else "totally real", d))
    M = Model((a, b, c), d, O)
    print("  universe: %d places over %d rational primes"
          % (len(M.UNIVERSE), sum(1 for p in CR.PRIMES if p <= MAXP)))
    # the head is re-read on THIS order: the shop's census ran on another
    # generator of the same field and its place indices are that order's.
    heads = [(p, i, e, f, cl, exc)
             for (p, i, e, f, cl, exc, pred, P) in head_census(O, (2, 3, 5))
             if exc >= 1]
    ok(heads, "K3: the winner reads no head on its index-1 order")
    hp, hi, he, hf, hcol, hexc = heads[0]
    P = SHOP.maximal_places(O, hp)[hi][0]
    col = Column(hp, he, hf, brute_column(O, P, hp ** hf))
    print("  head at p=%d e=%d f=%d: column %s, excess %d, a0 = %d, "
          "recurrence checked at %d depths"
          % (hp, he, hf, ",".join(str(x) for x in col.brute), hexc,
             col.a0, col.recurrence_checked))
    ok(hexc >= 1, "K3: the winner's head reads excess %d" % hexc)
    ok(col.recurrence_checked >= 1,
       "the head column has no licensed tail inside the brute range")
    head_pl = None
    Q2 = None
    for pl in M.UNIVERSE:
        if pl[0] == hp and pl[1] == he and pl[2] == hf and head_pl is None:
            head_pl = pl
        if pl[0] == 2 and pl[2] == 3:
            Q2 = pl
    ok(head_pl is not None, "the head place is not in the model universe")
    ok(Q2 is not None, "the model universe holds no f = 3 place over 2")
    M.set_column(head_pl, col)
    print("  head place in the model: %s;  the f = 3 place: %s (norm %d)"
          % (M.show(head_pl), M.show(Q2), M.place_norm(Q2)))
    s4_price(M, Q2)
    s5_walk(M, Q2, head_pl)
    print("\nchecks: %d" % CHECKS)


if __name__ == "__main__":
    main()
