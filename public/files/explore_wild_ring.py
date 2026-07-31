r"""explore_wild_ring.py -- the doubly ramified cubic ring, and whether a
ring WALK can build a surplus the stop law has to fear.

THE QUESTION. The stop law -- a bounded tick gap stops a walk -- rests on
the populated-door ring readings, which survive because a ring walk's
surplus stays small: the walked v_p(L) reaches 3 and the walked door
excess 2, measured over three quadratic rings (explore_populated_door.py
F6/F7), while only PLANTED states run further. A measurement is not a
bound. This file carries the surplus as a COLUMN OVER THE WALK -- v_p(L)
and the door excess read at every step of every walk in a five-ring sweep
-- and adds the ring the corpus does not have: one where the cheap places
are totally ramified, so the walk's own vehicle is the place a surplus
would price out. K = Q[x]/(x^3 - 2), with 2 and 3 both totally ramified
and 3 the corpus's first wild place at an odd prime.

THE KILL-SHAPE THE ROADMAP FROZE, as an observable: the sweep prints a
walk that SEATS (by its own move rule, not by planting) a place Q with
v_p(N(Q) - 1) larger than every v_p(L) the three quadratic rings' walks
build in the same run. What that would MEAN -- the stop law scoped by ring
arithmetic rather than safe on dynamics -- is weighed after the run.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The engine's --
lam_P, door_r, seated, v_p(L) -- exactly explore_populated_door.py's
terms, because the claim under test (walked surplus stays small) is that
file's F6/F7 and a rig written in other words could not read it. The
schedule family's vocabulary (head, gap, price) enters only in S3, where
the ladders are read against the head criterion.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From quadratic and from the -23 cubic: NOTHING about column shapes is
    carried. Z[i]'s plateau is wild-at-2 with mu_4 present; here mu_4 is
    absent (Q_2(i) has e = 2, which does not divide 3) and no plateau is
    expected. Both ramified columns below are derived fresh from THIS
    ring's local unit groups and brute-checked.
 T2 The head criterion (explore_head_width.py F2: f = 1 AND mu_p in K_P
    AND e = (p-1)p^t) is used as a PREDICTION, never inside lam_P. Its
    own counterexample list already measures the LOCAL fields of both
    ramified places here -- Z[2^(1/3)] and Z[3^(1/3)], excess 0, each
    failing the e = (p-1)p^t clause -- so the expectation the roadmap
    carried (a head at the wild place) is refuted by a filed result
    before this engine runs, and the run is the global confirmation.
 T3 Maximality is NOT inherited from a squarefree discriminant -- disc
    x^3 - 2 is -108 = -2^2 * 3^3 and the squarefree argument the -23
    engine uses is unavailable. S2 COMPUTES Dedekind's criterion at 2 and
    3 (the only primes whose square divides -108) and closes the index by
    ind^2 | 108 with ind prime to 6. Only then does Dedekind's
    factorization rule apply at every p.
 T4 The surplus observables are explore_populated_door.py's own -- v_p(L)
    per seated place and door excess pop - lone -- reused verbatim, so
    the five-ring table extends its sweep rather than resembling it.

THE HAND-ATTACK, on paper before any engine code. Both ramified places
fail e/(p-1) < 1, so the tame logarithm column (q-1)*p^ceil((a-1)/e) is
licensed at NEITHER; each is derived from its own squaring/cubing depth
map, and the two deviate from the standard staircase in two DIFFERENT
ways, neither of them a head.

  X over 2 (e = 3, f = 1, q = 2; tame since 2 does not divide 3, yet
  e >= p - 1 so the logarithm does not converge). mu_{2^inf}(K_X) = {+-1}:
  any larger 2-power torsion needs Q_2(i), whose e = 2 does not divide a
  totally ramified cubic's 3. For u = 1 + x with v(x) = i, u^2 - 1 =
  x(x + 2) and v(2) = e = 3, so v(u^2 - 1) = 2i for i < 3 (the x^2 term
  wins), = i + 3 for i > 3, and >= 6 at the tie i = 3. The depth path
  from i = 1 is 1 -> 2 -> 4 -> 7 -> 10 -> ... : DOUBLING below the line
  e/(p-1) = 3, then step e. The exponent of U_1/U_a is set by that path
  (deeper starts need fewer squarings; the -1 coset starts at depth 3 and
  adds nothing), so the 2-part exponent at depth a is 0, 1 at a = 1, 2
  and ceil((a+2)/3) from a = 3 on. Column:

      lam(X^a) = 1, 2, 4, 4, 8, 8, 8, 16, 16, 16, 32, ...

  -- the standard staircase 2^ceil((a-1)/3) times an extra 2 from a = 3
  on, a permanent LEVEL SHIFT bought by the doubling zone, with runs of
  length 3 = e and excess 0. Consequence for the walk, derived from the
  column alone: the lone door at X cycles 1, 1, 2 over e = 1, 2, 3 and
  then 3, 2, 1 over each later run, so a walk standing on X pays 2, 2, 4,
  then 8, 8, 8, ... at e = 3, 5, 8, 11 (each move advances by its own
  door). The recurrent price is 8 = 2^3 = N(X)^e.

  Y over 3 (e = 3, f = 1, q = 3; WILD, 3 | e). mu_3 needs Q_3(zeta_3),
  e = 2, again not a divisor of 3: U_1 is torsion-free. For u = 1 + x,
  u^3 - 1 = 3x + 3x^2 + x^3 with v(3) = 3: at i = 1 the x^3 term wins
  alone (v = 3); at i >= 2 the 3x term wins alone (v = i + 3). Every
  depth is exact -- no generic/special split anywhere. Depth path from
  1: 1 -> 3 -> 6 -> 9 -> ...; 3-part exponent = ceil(a/3) for a >= 2.
  Column:

      lam(Y^a) = 2, 6, 6, 18, 18, 18, 54, ...

  -- against the standard 2*3^ceil((a-1)/3) this jumps one rung EARLY at
  every a = 1 mod 3 from a = 4 on, a permanent PHASE SHIFT: the first
  cubing lands at depth 3 rather than 1 + e = 4, so the first run is
  shortened to e - 1 and every later jump arrives a step sooner. Runs
  never exceed 3 = e: excess 0, no head here either.

  Unramified places (every p >= 5): e = 1 < p - 1, the logarithm
  converges, the column is standard (q-1)*p^(a-1).

  THE VOID WALK, derived from the doors above: X opens at 2 (cheapest in
  the whole ring), pays 2, 2, 4, then 8 recurrently, and nothing
  undercuts 8 -- Y's door is 2 against any L = 2^k (6 never divides a
  2-power), price 9; the place over 5 reads door 2 at price 25 once
  v_2(L) >= 2; the place over 11 reads door 1 at price 11. So the walk
  never leaves X: lock vehicle X, support ONE place, recurrent cost
  8 = N^e. Every prior engine locks on an e = 1 vehicle at cost N^1
  (Z[i] at 9, Z[sqrt-5] and Z[w] and the -23 cubic on their cheapest
  gap-1 places), so this is the corpus's first lock priced at N^gap with
  gap > 1 -- IF the derivation holds, which S4 reads off the imported
  walker rather than off this paragraph.
  [CORRECTED POST-RUN -- the engine refuted this paragraph's opening
  move, and F4 carries the finding. "X opens at 2" is wrong: the door
  condition consults lam(X^1) = q - 1 = 1, which DIVIDES the void
  invariant L = 1, so X's opening door is 2 and its price 4. Y opens at
  3 and wins the void; X is never seated by any walk in the sweep. The
  derivation above silently assumed an opening door of 1 at a place
  whose first column entry is trivial -- the vibes half the DISTRUST
  paragraph below names, distrusted for the right reason.]

  WHY THIS RING FOR THE SURPLUS QUESTION: its cheap door is a place whose
  own column absorbs v_2 slowly (one power per 3 depths), so an external
  v_2 supply prices X out fast -- the unseated door of X against an
  invariant with v_2(L) = k is the least r with ceil((r+2)/3) > k, which
  grows with slope 3 = e. The two-rate race the stop law leaves open
  (the recurrent price against the carrier floor p^k + 1) has its
  recurrent exponent multiplied by e here, which is the configuration no
  quadratic ring can present at a cheap place.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 The imported brute-forcer (explore_cubic_ring.py's, run there against
     three filed quadratic tables) reproduces Z[i]'s filed lambda table --
     the hand-derived wild plateau included -- at every place of norm <=
     30 within the residue cap, and the -23 engine's own closed form at
     norm <= 60, 0 off, BEFORE it is read against this ring.
  P2 S2 prints disc = -108; Dedekind's criterion COMPUTED at 2 and 3
     returns coprime (p-maximal at both); ind^2 | 108 with ind prime to 6
     closes ind = 1, so O = Z[theta] and the factorization of every p is
     the factorization of x^3 - 2 mod p. The Minkowski bound prints below
     3 and the one prime of norm 2 is (theta), principal with N = 2, so
     h = 1 and this is an ideal-world engine.
  P3 The engine factors 2 = X^3 and 3 = Y^3 (e = 3, f = 1 both), finds no
     other ramified prime in the whole sieved universe, and the
     splitting-type densities read near Chebotarev's 1/2, 1/3, 1/6 for
     S_3 (root-and-quadratic, inert, split).
  P4 The brute-forced columns at X (to depth 13) and Y (to depth 8) equal
     the hand columns above at every depth, and a sample of unramified
     places reads standard. A single disagreement kills the hand
     derivation and everything downstream of it.
  P5 The head census reads excess 0 at EVERY place of norm <= 30 plus
     both ramified places, depth 14: no head anywhere, the criterion's
     e = (p-1)p^t clause failing at both ramified places exactly as the
     filed local measurements say. The level shift and the phase shift
     both PRINT (the brute columns against the standard staircase) and
     neither exceeds run length e.
  P6 The void walk through the imported walker locks on X with support
     {X} alone and recurrent cost 8 = N(X)^3 -- the first lock in the
     corpus whose recurrent price is N^gap with gap > 1.
  P7 THE SURPLUS COLUMN, over the five-ring sweep (void plus planted
     ramified seeds, 60 moves each): the walked v_p(L) tops out at 3 --
     at Z[i], p = 2, reproducing the filed reading -- and neither cubic
     ring's walks beat it; no walk SEATS a place Q with v_p(N(Q) - 1)
     above 3 for any residue characteristic p of its state. FREE
     READ-OFF, the roadmap's: the count of steps at which the lone-door
     menu and the populated-door menu name different chosen places, per
     ring -- the first reading of whether the widening ever changes what
     a walk DOES rather than what a strand costs.

KILL-SHAPES, as observables.
  K1 the forcer disagrees with a filed table: instrument wrong, stop.
  K2 the forcer disagrees with a hand column at this ring: the derivation
     is wrong; the column must be found, not derived, and P5-P7 are read
     against the found one.
  K3 Dedekind's criterion returns non-coprime at 2 or 3: Z[theta] is not
     maximal, the engine's place enumeration is unsound, stop.
  K4 the sweep prints a walk-seated place whose v_p(N(Q) - 1) exceeds
     every v_p(L) the three quadratic walks print: the roadmap's kill --
     the stop law is scoped by ring arithmetic.
  K5 the void walk does not lock inside the walker's cap.

DISTRUST THE MARGIN. The derived halves are the two hand columns; each is
an exact depth-map computation with its ties located (the one tie, i = 3
over 2, is absorbed by the torsion coset and moves nothing). The vibes
half is the WALK derivation -- lock at 8, nothing undercuts -- which
leans on menu comparisons across the whole universe that only the engine
actually performs. S4 therefore asserts the lock facts off the walker's
own return, and P6 dies cleanly if the menu holds a rival the paragraph
missed.

POSITIVE CONTROL (S1, run before any verdict is read): the imported
forcer against Z[i]'s filed table (the hardest: a hand-derived wild
plateau) and the -23 engine's closed form, 0 off required, before it
touches this ring.

THE SECTIONS.
  S1  positive control: the forcer against two filed rings, then the
      hand columns of this one.
  S2  the ring: discriminant, Dedekind's criterion computed at 2 and 3,
      the index, h = 1, the factorization census and densities.
  S3  the ladders: both ramified columns against the standard staircase
      (the level shift and the phase shift), the head census, the door
      cycle at X.
  S4  the void walk through the imported walker.
  S5  the surplus column: five rings, void + planted seeds, v_p(L) and
      door excess per step; the kill-shape read; the menu read-off.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 BOTH HAND COLUMNS HOLD, AND THE COLUMN'S TAME/WILD LINE IS e < p - 1,
   NOT p | e (rule in range; 21 ramified readings to depth 13 at X and 8
   at Y against the hand columns, 39 unramified against standard, 0 off,
   after 43 + 47 filed readings at Z[i] and the -23 engine reproduced the
   instrument). lam(X^a) = 1, 2, then 2^ceil((a+2)/3) -- the standard
   staircase times a permanent extra 2 from a = 3 on, a LEVEL SHIFT
   bought by the doubling zone below e/(p-1) = 3, at a place that is TAME
   in the p | e sense. lam(Y^a) = 2, then 2*3^ceil(a/3) -- the staircase
   jumping one rung EARLY at every a = 1 mod 3, a PHASE SHIFT bought by
   wildness (the first cubing lands at depth v(3) = 3, not 1 + e), the
   corpus's first specimen of that shape. So the corpus's non-standard
   columns now sort into three geometries: heads (excess > 0, plateaus),
   level shifts (Z[w]'s split places over 2 run one 2-power BELOW
   standard, X here runs one ABOVE), and Y's phase shift -- and the line
   that predicts deviation is the logarithm's e < p - 1, which both
   ramified places fail while one is tame and one wild. [The geometries
   are features, not a partition: Z[w]'s pair also carries excess 1 --
   its completion is Q_2, whose column 1, 2, 2, 4, 8 plateaus once --
   so its below-standard tail is a headed column's displacement, and
   the HEADLESS level shift is X's alone.]

F2 THE MAXIMALITY ARGUMENT THE ROADMAP OWED, COMPUTED (property;
   Dedekind's criterion evaluated in-engine at 2 and 3, the census over
   all 2262 sieved primes). disc(x^3 - 2) = -108 = -2^2 * 3^3, not
   squarefree, so the -23 engine's licence does not transfer. Dedekind
   at 2: T = 1, coprime -- 2-maximal. At 3: T = x^2 + x + 1 with
   T(-1) = 1 != 0 mod 3, coprime to x + 1 -- 3-maximal. ind^2 | 108
   with ind prime to 6 forces ind = 1: O = Z[theta], and every p reads
   off x^3 - 2 mod p. 2 = X^3, 3 = Y^3, both (e, f) = (3, 1); x^3 - 2
   is squarefree mod all 2260 other primes; densities 0.503 / 0.335 /
   0.163 against Chebotarev's 1/2, 1/3, 1/6 for S_3. Minkowski bound
   2.940 < 3 and the one prime of norm <= 2 is (theta), principal:
   h = 1, an ideal-world engine.

F3 NO HEAD ANYWHERE, AND THE ROADMAP'S EXPECTATION DIED ON A FILED
   RESULT BEFORE THE ENGINE RAN (rule in range; all 8 places of norm <=
   30 -- both ramified places included -- at depth 14, excess 0 at every
   one). The head criterion's e = (p-1)p^t clause fails at both ramified
   places (3 is neither a power of 2 nor 2*3^t), exactly as
   explore_head_width.py F2's counterexample list already measured for
   the LOCAL fields Z[2^(1/3)] and Z[3^(1/3)] -- the roadmap's "a head
   is expected where the -23 field has none" was refuted by that filing
   at the freeze, recorded in T2, and the global run confirms it. What
   the ring supplies instead is F1's pair: columns that deviate from
   standard FOREVER while keeping excess 0.

F4 P6 REFUTED: THE CHEAPEST-NORM PLACE IN THE RING IS INVISIBLE TO EVERY
   WALK (rule in range; the imported walker from the void, locked at the
   first witnessed run). The slate derived a lock on X at N^e = 8; the
   engine locks on the rational place over 5 at N^1 = 5 after 12 steps,
   support 3^2 * 5^10, and X is never seated -- not at the void, where
   lam(X^1) = q - 1 = 1 divides L = 1 and prices X's opening at 4
   against Y's 3, and never after, because any invariant with v_2(L) = k
   prices X's opening door at the least r with ceil((r+2)/3) > k, slope
   3 = e. The walk seats the wild place twice, strands it at e = 2, and
   locks on the cheapest gap-1 place -- the same lock shape as every
   other engine. So the doubly ramified ring's distinctive places are
   both walk-invisible: X priced out by its own trivial first entry, Y
   stranded after two moves; and the two-rate race gains a sharper local
   reading than the f = 1 constant-decides case -- at X the recurrent
   exponent carries the factor e = 3, so the recurrent side loses the
   race outright, walk or no walk.

F5 THE WALKED SURPLUS IS ZERO AT FOUR OF FIVE RINGS AND 1 AT THE FIFTH,
   AND THE KILL-SHAPE DOES NOT FIRE (rule in range; five rings, 12
   walks, 720 steps, 1190 seated readings -- every seated place at every
   step). Max surplus v_p(L) - v_p(own lambda): Z[i] 1 (v_2(L) = 3
   against the ramified place's own 2 -- the filed state, door excess 2
   beside it, both reproducing explore_populated_door.py F6); Z[sqrt-5],
   Z[w], the -23 cubic and THIS ring all 0 at every step of every walk.
   Max seated cross-supply v_p(N(Q) - 1): 3 at Z[i] (the inert place
   over 3), 1 at Z[sqrt-5] planted, 0 at both cubic rings. K4 wanted a
   walk-seated supply beating the quadratics' walked surplus; nothing
   came near, and the ring BUILT for cheap supplies walks at surplus 0
   because greedy seating starves diversity -- its void walk seats two
   places total before locking. So the corpus's entire walked-surplus
   exposure remains ONE state shape in ONE ring, now confirmed against
   two cubic engines: the stop law's measured half gains a fifth and
   sixth ring at surplus 0, and what it still lacks is a THEOREM about
   greedy support growth, not more ladders.

F6 THE LONE AND POPULATED MENUS PART AT 409 OF 720 STEPS, IN THREE OF
   THE FIVE RINGS (rule in range; the roadmap's free read-off, every
   step of the sweep, first specimens printed per walk). The answer to
   "do the two menus ever name different places in an actual ring" is
   YES, massively: 7 of the 12 walks part from their lone-menu
   counterfactual at ~58 of 60 steps -- every planted walk of
   Z[sqrt-5], Z[i] and this ring, plus the voids of Z[i] and this ring;
   Z[sqrt-5]'s VOID walk never parts, and neither does any walk of
   Z[w] or the -23 cubic. Two mechanisms in
   the specimens: a STRAND is cheap under lone pricing and wide under
   populated (Z[sqrt-5] planted over 5: the lone menu names the strand
   itself at step 1), and a COVERED OPENING is cheap under lone pricing
   and priced out by the populated invariant (here: the lone menu names
   X at price 4 at step 2-3 of every walk while the true menu prices X
   at 32 and rising -- F4's invisibility, seen from the menu side; at
   Z[i] the lone menu names the split place over 5 while the true walk
   seats the inert place over 3). So the populated door is not a small
   correction to lone pricing but a different selection rule at most
   steps -- while the SURPLUS half of the widening (door excess at a
   seated place) fired only at Z[i]'s one state. The five walks where
   the menus never part are Z[w]'s two, the -23 cubic's two, and
   Z[sqrt-5]'s void; WHY those five agree is not settled by this sweep
   -- the -23 cubic's planted walk holds a gap-2 strand from step 0 and
   its menus still agree, so "all columns gap-1" is not the condition
   -- and the parting specimens share only that some place is priced
   across the argmin by one rule and not the other.

RUN RECORD. `python explore_wild_ring.py` (memwatch). One process,
CPython, no BLAS. 176 checks, 4.3 s wall, peak working set 23.1 MB under
the 512 MB ceiling. 2262 rational primes sieved (368 split / 1136
root-and-quadratic / 756 inert / 2 ramified). S1: 43 Z[i] + 47 -23-engine
filed readings reproduced, then 21 ramified + 39 unramified at this ring,
0 off. S5: 12 walks, 60 moves each, 720 steps, 1190 seated readings;
menu read-off 409 of 720. P1-P5 hit; P6 refuted by the engine (F4); P7's
surplus half hit with the kill silent, its menu half refuted in the
interesting direction (F6).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import gcd

CHECKS = 0

MAXP = 20000        # rational primes enumerated into the universe
BRUTE_CAP = 15000   # residues allowed in one brute-forced quotient
DEPTH_N = 14        # depths a ladder is tabulated to
ROOT_CAP = 600      # primes whose roots are extracted by trial
WALK_MOVES = 60     # moves per walk in the surplus sweep


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


# --------------------------------------------------------------- the ring
# K = Q(theta), theta^3 = 2. O = Z[theta] (PROVED in S2, not read off a
# squarefree discriminant -- disc = -108 is not squarefree). h = 1 (S2).
# The reduction rule, in the shape the generic brute-forcer reads:
WILD_REDUCE = (2, 0, 0)         # t^3 = 2
MINPOLY = (-2, 0, 0, 1)         # x^3 - 2, low coefficient first

# A place is a tag carrying numbers, the -23 engine's convention:
#   (p, e, f, i) -- rational prime, ramification index, residue degree,
#   ordinal separating places that agree in (p, e, f).

import explore_cubic_ring as C3     # the forcer + the -23 engine
import explore_lock_budget as LB    # the walker

PRIMES = C3.PRIMES                  # same sieve, same MAXP


def factor_shape(p):
    """[(e, f), ...] for the places over p, from x^3 - 2 mod p. Licensed
    by S2's computed maximality: Dedekind applies at EVERY p, including
    2 and 3 where the shape is read from the verified congruences
    x^3 - 2 = x^3 mod 2 and (x + 1)^3 mod 3."""
    if p in (2, 3):
        return [(3, 1)]
    # p >= 5: disc = -108 is a unit mod p, the factorization is squarefree;
    # the shape is the root count of x^3 - 2 -- 0, 1 or 3.
    f = MINPOLY
    sub = list(C3.ppowmod((0, 1), p, f, p))
    while len(sub) < 2:
        sub.append(0)
    sub[1] -= 1
    nr = len(C3.pgcd(tuple(sub), f, p)) - 1
    if nr <= 0:
        return [(1, 3)]                       # inert
    if nr == 1:
        return [(1, 1), (1, 2)]               # a rational place and an f=2
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
    return 0                       # h = 1 (S2): every ideal is principal


def place_key(pl):
    return (place_norm(pl), pl[1], pl[2], pl[3])


def conj_place(pl):
    """Non-Galois cubic: no conjugation acts on the places over Q."""
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

    THREE shapes, each derived in the docstring's hand-attack and
    brute-checked in S1: the level-shifted staircase at the tame totally
    ramified place over 2, the phase-shifted staircase at the wild place
    over 3, and the standard column everywhere else (e = 1 < p - 1, the
    logarithm's)."""
    if a == 0:
        return 1
    p, e, f = pl[0], pl[1], pl[2]
    if p == 2 and e == 3:
        if a == 1:
            return 1
        if a == 2:
            return 2
        return 2 ** ((a + 4) // 3)          # 2^ceil((a+2)/3), a >= 3
    if p == 3 and e == 3:
        if a == 1:
            return 2
        return 2 * 3 ** ((a + 2) // 3)      # 2*3^ceil(a/3), a >= 2
    return (p ** f - 1) * p ** (a - 1)


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


def gen_poly(pl):
    """h(t) with X = (p, h(theta)). Over 2 the place is (theta) = (2, t);
    over 3 the uniformizer is theta + 1; unramified f = 1 places take a
    root of x^3 = 2, f = 2 the cofactor x^2 + rx + r^2, f = 3 the whole
    of (p)."""
    p, e, f, i = pl
    if f == 3:
        return (0,)
    if p == 2:
        return (0, 1)
    if p == 3:
        return (1, 1)
    rs = sorted(r for r in range(p) if (r * r * r - 2) % p == 0)
    if f == 1:
        return (-rs[i] % p, 1)
    r = rs[0]
    return ((r * r) % p, r % p, 1)


UNIVERSE = build_universe()


# ------------------------------------------------- S1 the positive control
def s1_control():
    section("S1  POSITIVE CONTROL -- the imported forcer against two filed "
            "rings, then the hand columns of this one")
    print("  The instrument is explore_cubic_ring.py's generic brute-forcer")
    print("  (HNF residue enumeration, exponent of the unit group). It is")
    print("  re-run here against Z[i]'s filed table -- the hand-derived wild")
    print("  plateau included -- and the -23 engine's closed form, before it")
    print("  is allowed to read this ring.")
    print()
    quads = C3._load_quadratics()
    GI = next(M for name, M in quads if name == "Z[i]")
    T, N0 = C3.QUAD_RULE[GI.__name__]
    R = (N0, T)
    n_zi = 0
    for pl in GI.UNIVERSE:
        if GI.place_norm(pl) > 30:
            break
        gp, hpoly = C3.quadratic_ideal(GI, pl)
        q = GI.place_norm(pl)
        for a in range(1, 15):
            if q ** a > BRUTE_CAP:
                break
            got = C3.unit_exponent(gp, hpoly, R, a, q)
            want = GI.lam_P(pl, a)
            ok(got == want,
               "Z[i]: brute %d at %s^%d against filed %d"
               % (got, str(pl), a, want))
            n_zi += 1
    print("  Z[i]: %d filed readings reproduced, 0 off." % n_zi)

    n_c3 = 0
    for pl in C3.UNIVERSE:
        if pl[0] > C3.ROOT_CAP or C3.place_norm(pl) > 60:
            continue
        hpoly = C3.cubic_gen_poly(pl)
        q = C3.place_norm(pl)
        for a in range(1, DEPTH_N + 1):
            if q ** a > BRUTE_CAP:
                break
            got = C3.unit_exponent(pl[0], hpoly, C3.CUBIC_REDUCE, a, q)
            want = C3.lam_P(pl, a)
            ok(got == want,
               "-23 engine: brute %d at %s^%d against %d"
               % (got, C3.show(pl), a, want))
            n_c3 += 1
    print("  -23 engine: %d readings reproduced, 0 off. The instrument"
          % n_c3)
    print("  stands.")

    print()
    print("  And only now this ring. The hand columns under test:")
    print("  %-14s %-4s %-4s %-4s %-10s %-10s %s"
          % ("place", "e", "f", "a", "brute", "hand", ""))
    n_ram = 0
    for pl in UNIVERSE:
        if pl[1] != 3:
            continue
        hpoly = gen_poly(pl)
        q = place_norm(pl)
        for a in range(1, DEPTH_N + 1):
            if q ** a > BRUTE_CAP:
                break
            got = C3.unit_exponent(pl[0], hpoly, WILD_REDUCE, a, q)
            want = lam_P(pl, a)
            print("  %-14s %-4d %-4d %-4d %-10d %-10d %s"
                  % (show(pl), pl[1], pl[2], a, got, want,
                     "" if got == want else "  <-- DISAGREE"))
            ok(got == want,
               "hand column: brute %d at %s^%d against %d"
               % (got, show(pl), a, want))
            n_ram += 1
    n_unram = 0
    for pl in UNIVERSE:
        if pl[1] == 3 or pl[0] > ROOT_CAP or place_norm(pl) > 60:
            continue
        hpoly = gen_poly(pl)
        q = place_norm(pl)
        for a in range(1, DEPTH_N + 1):
            if q ** a > BRUTE_CAP:
                break
            got = C3.unit_exponent(pl[0], hpoly, WILD_REDUCE, a, q)
            want = lam_P(pl, a)
            ok(got == want,
               "unramified: brute %d at %s^%d against standard %d"
               % (got, show(pl), a, want))
            n_unram += 1
    print("  %d ramified readings against the hand columns and %d"
          % (n_ram, n_unram))
    print("  unramified against standard, 0 off.")
    return n_zi, n_c3, n_ram, n_unram


# ------------------------------------------------------------- S2 the ring
def poly_disc_cubic(a, b):
    """disc of x^3 + ax + b."""
    return -4 * a ** 3 - 27 * b ** 2


def dedekind_at(p, gbar_factors):
    """Dedekind's criterion at p for MINPOLY, with the factorization of
    f mod p supplied as [(factor, multiplicity), ...] over F_p and
    VERIFIED here by re-multiplying. Returns True iff Z[theta] is
    p-maximal: gcd(Tbar, gbar, hbar) = 1 where g = prod of distinct
    factors, h = f/g lifted, T = (g*h - f)/p."""
    f = MINPOLY
    prod = (1,)
    for fac, m in gbar_factors:
        for _ in range(m):
            prod = C3.pmul(prod, fac, p)
    ok(prod == C3.pnorm(f, p),
       "the supplied factorization does not multiply back to f mod %d" % p)
    g = (1,)
    h = (1,)
    for fac, m in gbar_factors:
        g = C3.pmul(g, fac, p)
        for _ in range(m - 1):
            h = C3.pmul(h, fac, p)
    # integer lift of g*h - f, then exact division by p
    gl = [x % p for x in g]
    hl = [x % p for x in h]
    ghl = [0] * (len(gl) + len(hl) - 1)
    for i, x in enumerate(gl):
        for j, y in enumerate(hl):
            ghl[i + j] += x * y
    fl = list(f) + [0] * (len(ghl) - len(f))
    diff = [ghl[k] - fl[k] for k in range(len(ghl))]
    assert all(d % p == 0 for d in diff), "g*h - f not divisible by %d" % p
    T = tuple(d // p for d in diff)
    d1 = C3.pgcd(T, g, p)
    d2 = C3.pgcd(d1, h, p)
    return len(d2) - 1 == 0, T


def s2_the_ring():
    section("S2  THE RING -- maximality COMPUTED, then the census")
    disc = poly_disc_cubic(0, -2)
    print("  disc(x^3 - 2) = %d = -2^2 * 3^3 -- NOT squarefree, so the -23"
          % disc)
    print("  engine's licence (squarefree disc => maximal) does not apply.")
    ok(disc == -108, "discriminant computes to %d, not -108" % disc)

    print()
    print("  Dedekind's criterion, computed at the two primes whose square")
    print("  divides the discriminant:")
    max2, T2 = dedekind_at(2, [((0, 1), 3)])            # x^3 mod 2
    print("    p = 2: f = x^3, T = %s, coprime: %s" % (str(T2), max2))
    ok(max2, "Dedekind fails at 2: Z[theta] not 2-maximal")
    max3, T3 = dedekind_at(3, [((1, 1), 3)])            # (x+1)^3 mod 3
    print("    p = 3: f = (x+1)^3, T = %s, coprime: %s" % (str(T3), max3))
    ok(max3, "Dedekind fails at 3: Z[theta] not 3-maximal")
    print("  ind^2 | 108 with ind prime to 6 forces ind = 1: O = Z[theta],")
    print("  and the factorization of every p reads off x^3 - 2 mod p.")

    mink = (4.0 / 3.141592653589793) * (6.0 / 27.0) * (108 ** 0.5)
    print()
    print("  Minkowski bound (4/pi)(3!/3^3)sqrt(108) = %.3f < 3: every class"
          % mink)
    print("  holds an ideal of norm <= 2; the one prime of norm 2 is")
    print("  (2, theta) = (theta), principal with N(theta) = 2. h = 1.")
    ok(mink < 3, "Minkowski bound %.3f is not below 3" % mink)

    print()
    rams = [pl for pl in UNIVERSE if pl[1] > 1]
    print("  ramified places: %s" % ", ".join(show(pl) for pl in rams))
    ok(sorted(pl[0] for pl in rams) == [2, 3],
       "the ramified primes are not exactly {2, 3}")
    ok(all(pl[1] == 3 and pl[2] == 1 for pl in rams),
       "a ramified place is not totally ramified")
    # verify squarefreeness at every other prime: gcd(f, f') = 1
    for p in PRIMES:
        if p in (2, 3):
            continue
        d = C3.pgcd(MINPOLY, C3.pderiv(MINPOLY, p), p)
        assert len(d) - 1 == 0, "x^3 - 2 not squarefree mod %d" % p
    ok(True, "x^3 - 2 squarefree at all %d unramified primes"
       % (len(PRIMES) - 2))

    shapes = {}
    for p in PRIMES:
        if p in (2, 3):
            continue
        key = tuple(sorted(factor_shape(p)))
        shapes[key] = shapes.get(key, 0) + 1
    tot = len(PRIMES) - 2
    print("  splitting densities over %d unramified primes:" % tot)
    for key, n in sorted(shapes.items()):
        print("    %-28s %6d  %.3f" % (str(key), n, n / tot))
    X = next(pl for pl in UNIVERSE if pl[0] == 2)
    Y = next(pl for pl in UNIVERSE if pl[0] == 3)
    return X, Y


# ---------------------------------------------------------- S3 the ladders
def runs_of(col):
    runs, cur, n = [], None, 0
    for v in col:
        if v == cur:
            n += 1
        else:
            if cur is not None:
                runs.append((cur, n))
            cur, n = v, 1
    runs.append((cur, n))
    return runs


def s3_ladders(X, Y):
    section("S3  THE LADDERS -- two shifted staircases, no head, and the "
            "door cycle at X")
    std2 = [2 ** (-(-(a - 1) // 3)) for a in range(1, DEPTH_N + 1)]
    std3 = [2 * 3 ** (-(-(a - 1) // 3)) for a in range(1, DEPTH_N + 1)]
    colX = [lam_P(X, a) for a in range(1, DEPTH_N + 1)]
    colY = [lam_P(Y, a) for a in range(1, DEPTH_N + 1)]
    print("  a           : %s" % " ".join("%6d" % a
                                          for a in range(1, DEPTH_N + 1)))
    print("  X (over 2)  : %s" % " ".join("%6d" % v for v in colX))
    print("  standard    : %s" % " ".join("%6d" % v for v in std2))
    print("  Y (over 3)  : %s" % " ".join("%6d" % v for v in colY))
    print("  standard    : %s" % " ".join("%6d" % v for v in std3))
    # the LEVEL shift: X = standard * 2 from a = 3 on, equal before
    ok(colX[0] == std2[0] and colX[1] == std2[1],
       "X does not agree with standard at a <= 2")
    ok(all(colX[a - 1] == 2 * std2[a - 1] for a in range(3, DEPTH_N + 1)),
       "X is not the standard staircase times 2 from a = 3 on")
    # the PHASE shift: Y jumps at a = 1 mod 3, standard at a = 2 mod 3
    diffs = [a for a in range(1, DEPTH_N + 1) if colY[a - 1] != std3[a - 1]]
    ok(all(a % 3 == 1 for a in diffs) and 4 in diffs,
       "Y's deviation from standard is not the a = 1 mod 3 phase shift")
    print()
    print("  X carries the standard staircase times TWO from a = 3 on (the")
    print("  level shift); Y jumps one rung early at every a = 1 mod 3 (the")
    print("  phase shift). Both deviate FOREVER; neither run exceeds e.")

    print()
    print("  head census, excess = longest run less e, depth %d:" % DEPTH_N)
    n_pl = 0
    for pl in UNIVERSE:
        if place_norm(pl) > 30:
            continue
        col = [lam_P(pl, a) for a in range(1, DEPTH_N + 1)]
        longest = max(n for _, n in runs_of(col))
        excess = longest - pl[1]
        print("    %-14s longest run %d, e = %d, excess %d"
              % (show(pl), longest, pl[1], excess))
        ok(excess <= 0, "a head at %s: excess %d" % (show(pl), excess))
        n_pl += 1
    print("  excess 0 at all %d places: NO head anywhere -- the criterion's"
          % n_pl)
    print("  e = (p-1)p^t clause fails at both ramified places, as the filed")
    print("  local measurements (Z[2^(1/3)], Z[3^(1/3)]) already said.")

    print()
    print("  the lone door cycle at X (L = its own lambda):")
    doors = [door_r(X, e, lam_P(X, e)) for e in range(1, 13)]
    print("    e = 1..12 : %s" % " ".join(str(d) for d in doors))
    ok(doors[:3] == [1, 1, 2], "the opening doors at X are not 1, 1, 2")
    ok(doors[4] == 3 and doors[7] == 3 and doors[10] == 3,
       "the recurrent door at e = 2 mod 3 is not 3")
    return colX, colY


# --------------------------------------------------------- S4 the void walk
def s4_void_walk():
    section("S4  THE VOID WALK -- this ring through the IMPORTED walker")
    M = sys.modules[__name__]
    print("  every place of norm <= 30 at the void, door and price:")
    print("  %-14s %-8s %-6s %s" % ("place", "norm", "door", "price"))
    scan = LB.scan_universe(M, {}, 1, ceiling=30)
    for nrm, r, cost, pl in sorted(scan):
        print("  %-14s %-8d %-6d %d" % (show(pl), nrm, r, cost))

    got = LB.walk_to_lock(M, {})
    ok(got is not None, "the void seed does not lock inside the walker's cap")
    st, L, pl, cost, steps = got
    print()
    print("  lock vehicle %s at recurrent cost %d, %d steps to the lock"
          % (show(pl), cost, steps))
    print("  locked support: %s" % show_st(st))
    # P6 predicted a lock on X at N^e = 8. The engine refutes it: at the
    # VOID the door condition consults lam(X^1) = q - 1 = 1, which divides
    # L = 1, so X's OPENING door is 2 (price 4) and Y's is 1 (price 3) --
    # the hand-attack's walk derivation missed the trivial first column
    # entry, exactly the vibes half the slate said to distrust. The
    # assertions below state what the engine prints.
    ok(pl == (5, 1, 1, 0),
       "the lock vehicle is not the rational place over 5: %s" % show(pl))
    ok(cost == place_norm(pl),
       "the recurrent cost %d is not the vehicle's norm %d"
       % (cost, place_norm(pl)))
    Y = next(q for q in st if q[0] == 3)
    ok(st[Y] == 2 and all(q[0] != 2 for q in st),
       "the stranded support is not Y^2 with X unseated: %s" % show_st(st))
    print()
    print("  P6 REFUTED: the norm-2 place is never seated at all. Its first")
    print("  column entry is q - 1 = 1, so from the void its door is 2 and")
    print("  its price 4, beaten by Y at 3; once anything supplies v_2, its")
    print("  door only widens. The walk seats the wild place twice, strands")
    print("  it at e = 2, and locks on the cheapest gap-1 place at N^1 = 5,")
    print("  the same lock shape as every other engine.")
    return st, L, pl, cost, steps


# ------------------------------------------ S5 the surplus over the walk
def lone_menu(mod, st):
    """The menu each place would face against its OWN invariant alone --
    the lone-door pricing, same tie-break. What the walk would do if no
    place could see the rest of the state."""
    best, ties = None, []
    for pl in mod.UNIVERSE:
        nrm = mod.place_norm(pl)
        if best is not None and nrm > best:
            break
        e = st.get(pl, 0)
        r = mod.door_r(pl, e, mod.lam_P(pl, e))
        cost = nrm ** r
        if best is None or cost < best:
            best, ties = cost, [(pl, r)]
        elif cost == best:
            ties.append((pl, r))
    ties.sort(key=lambda t: mod.place_key(t[0]))
    return best, ties


def walk_surplus(mod, seed, moves=WALK_MOVES):
    """Greedy walk from a seed, the surplus read at every step: for every
    seated place P over p, the SURPLUS v_p(L) - v_p(lam_P(P^e)) -- what
    the rest of the state pushes the invariant above P's own ladder (the
    raw v_p(L) is unbounded trivially along a lock vehicle's own column
    and measures nothing) -- and the door excess pop - lone. Also the
    cross-SUPPLY per step: for every seated pair (P over p, Q over
    another prime), v_p(N(Q) - 1), the residue-route term; and whether
    the lone menu names a different chosen place than the true menu."""
    st = dict(seed)
    L = mod.lam_state(st)
    max_sur = 0
    max_sur_spec = None
    max_exc = 0
    max_exc_spec = None
    max_supply = 0
    max_supply_spec = None
    menu_diff = 0
    menu_diff_spec = None
    nread = 0
    for step in range(1, moves + 1):
        cost, ties = mod.ideal_menu(st, L)
        pl, r = ties[0]
        lbest, lties = lone_menu(mod, st)
        if lties[0][0] != pl:
            menu_diff += 1
            if menu_diff_spec is None:
                menu_diff_spec = (step, pl, lties[0][0])
        st[pl] = st.get(pl, 0) + r
        L = mod.lam_state(st)
        seated = [(q, e) for q, e in st.items() if e >= 1]
        for q, e in seated:
            p = mod.place_char(q)
            sur = v_p(L, p) - v_p(mod.lam_P(q, e), p)
            lone = mod.door_r(q, e, mod.lam_P(q, e))
            pop = mod.door_r(q, e, L)
            nread += 1
            if sur > max_sur:
                max_sur = sur
                max_sur_spec = (step, q, p)
            if pop - lone > max_exc:
                max_exc = pop - lone
                max_exc_spec = (step, q, pop, lone)
            for q2, e2 in seated:
                if mod.place_char(q2) == p:
                    continue
                s = v_p(mod.place_norm(q2) - 1, p)
                if s > max_supply:
                    max_supply = s
                    max_supply_spec = (step, q2, p)
        assert cost <= mod.MAXP, "walk cost beyond the ring's universe"
    return dict(max_sur=max_sur, max_sur_spec=max_sur_spec,
                max_exc=max_exc, max_exc_spec=max_exc_spec,
                max_supply=max_supply, max_supply_spec=max_supply_spec,
                menu_diff=menu_diff, menu_diff_spec=menu_diff_spec,
                nread=nread)


def s5_surplus():
    section("S5  THE SURPLUS AS A COLUMN OVER THE WALK -- five rings, "
            "every step read")
    quads = C3._load_quadratics()
    ME = sys.modules[__name__]
    rams_of = {
        "Z[sqrt-5]": [('ram', 2), ('ram', 5)],
        "Z[w] (-23)": [('ram', 23)],
        "Z[i]": [('ram', 2)],
    }
    rings = []
    for name, M in quads:
        rings.append((name, M, rams_of[name]))
    c3ram = [pl for pl in C3.UNIVERSE if pl[1] > 1]
    rings.append(("-23 cubic", C3, c3ram))
    rings.append(("Z[2^(1/3)]", ME, [pl for pl in UNIVERSE if pl[1] > 1]))

    print("  void + one planted seed per ramified place, %d moves each."
          % WALK_MOVES)
    print("  %-12s %-20s %-8s %-6s %-8s %-9s %s"
          % ("ring", "seed", "surplus", "excess", "supply", "menudiff",
             "reads"))
    rows = []
    for name, M, rams in rings:
        seeds = [("void", {})]
        for pl in rams:
            seeds.append(("planted %s" % (show(pl) if M is ME
                                          else str(pl)), {pl: 1}))
        for sname, seed in seeds:
            got = walk_surplus(M, seed)
            rows.append((name, sname, got))
            print("  %-12s %-20s %-8d %-6d %-8d %-9d %d"
                  % (name, sname, got['max_sur'], got['max_exc'],
                     got['max_supply'], got['menu_diff'], got['nread']))

    quad_names = set(rams_of)
    quad_sur = max(g['max_sur'] for n, s, g in rows if n in quad_names)
    here = [g for n, s, g in rows if n == "Z[2^(1/3)]"]
    c3r = [g for n, s, g in rows if n == "-23 cubic"]
    print()
    print("  the three quadratic rings' walked surplus tops at %d" % quad_sur)
    print("  this ring's walks: max surplus %d, max seated cross-supply"
          % max(g['max_sur'] for g in here))
    print("  v_p(N(Q)-1) = %d; the -23 cubic: %d and %d"
          % (max(g['max_supply'] for g in here),
             max(g['max_sur'] for g in c3r),
             max(g['max_supply'] for g in c3r)))
    kill = any(g['max_supply'] > quad_sur for g in here + c3r)
    print("  KILL-SHAPE K4 (a walk-seated supply beating the quadratics'")
    print("  walked surplus): %s" % ("FIRED" if kill else "did not fire"))

    diffs = sum(g['menu_diff'] for _, _, g in rows)
    steps = WALK_MOVES * len(rows)
    print()
    print("  the free read-off: lone-door menu vs populated-door menu named")
    print("  different chosen places at %d of %d steps." % (diffs, steps))
    for n, s, g in rows:
        if g['menu_diff']:
            print("    first at %s / %s: step %d, %s against %s"
                  % (n, s, g['menu_diff_spec'][0],
                     str(g['menu_diff_spec'][1]), str(g['menu_diff_spec'][2])))
    return rows, quad_sur, kill, diffs, steps


def main():
    n_zi, n_c3, n_ram, n_unram = s1_control()
    X, Y = s2_the_ring()
    s3_ladders(X, Y)
    s4_void_walk()
    rows, quad_sur, kill, diffs, steps = s5_surplus()

    section("VERDICT -- the predictions read against what printed")
    print("  P1 %d + %d filed readings reproduced" % (n_zi, n_c3))
    print("  P2 maximality computed, h = 1: see S2")
    print("  P3 2 = X^3, 3 = Y^3, no other ramification: see S2")
    print("  P4 %d ramified + %d unramified brute readings: see S1"
          % (n_ram, n_unram))
    print("  P5 no head anywhere: see S3")
    print("  P6 the void walk: see S4")
    print("  P7 quadratic walked surplus max %d; kill fired: %s; menu"
          % (quad_sur, kill))
    print("     read-off %d of %d steps: see S5" % (diffs, steps))
    print("\n  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
