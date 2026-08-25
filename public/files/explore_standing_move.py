"""
explore_standing_move.py -- THE STANDING-MOVE DICHOTOMY (a descent probe;
sibling of explore_lock_prime.py, explore_hot_limit.py,
explore_selection_frame.py, explore_module_law.py).

THE QUESTION. One argument in the cascade corpus turns out to say
nothing about characteristics, about number rings, or about primes. It
says: if a greedy walk faces a FAMILY of moves each of which is
available whatever the state has done, and each of which is priced by
ONE coordinate of the state, then each of those moves independently
CAPS what the walk can be paying, so either some coordinate stays
bounded -- and then a bounded-cost move recurs forever and absorbs the
tail, a LOCK -- or every one of those coordinates runs away AT ONCE.
That is a statement about greedy walks. This corpus is full of greedy
walks, and the first place to run it is the SELECTION LADDER
(explore_selection_frame.py): floor 0 pure order, floor 1 cancellative
commutative monoid with a summable character, floor 2 unique
factorization. Does a floor of that ladder SUPPLY the argument its
hypothesis?

The hypothesis doing all the work is availability. The pricing half is
easy: a cost formula either reads one coordinate or it does not, and
that is checked by reading it. Availability is the half that will fail
where it fails, so the design is built around it, and around the
sharpening the statement needs before it can be tested at all -- the
cascade's door is not a fixed move but a RECIPE, a different element at
every state, and what is required of it is only that its output be
ADMISSIBLE everywhere. "State-independent in availability" is therefore
a property of a recipe and never of a move.

Design + predictions PR1-PR6 fixed before the engine.

THE SCHEMA, stated so it can be checked. A world is (states, A(.),
cost, step): A(s) the admissible moves at s, cost a positive number per
move, greedy stepping by an argmin of cost over A(s). A STANDING FAMILY
is an index set I with recipes M_i : states -> moves such that
  (S1) STANDING AVAILABILITY: M_i(s) in A(s) at every reachable s;
  (S2) COORDINATE PRICING: cost(M_i(s)) = f_i(x_i(s)) for a single
       integer coordinate x_i of the state and a nondecreasing f_i.
Given (S1), greedy pays at most min_i f_i(x_i(s)) at every step -- THE
CAP. Add
  (S3) NORM-FINITENESS: finitely many moves under any cost ceiling, and
       a move recurring infinitely often absorbs the tail,
and the dichotomy follows: either some x_i is bounded along the walk
and the walk LOCKS, or every x_i diverges simultaneously. Corollary A:
a family member whose f_i is CONSTANT locks the walk outright.
Corollary B: escape is a CONJUNCTION over the whole family, never a
disjunction the walk gets to satisfy at one index of its choosing.

THE CELLS. Three demands over Z, each a growth law
(explore_growth_laws.py): D-DYN (lambda must grow -- depth), D-IND (the
extension must split -- breadth), D-TRA (capacity with lambda frozen --
mortality). Two worlds off Z: NUM23, the numerical monoid {x^n : n = 0
or n >= 2}, cancellative and NOT free (floor 1 without floor 2); and a
finite divisor region as a bare poset (floor 0). The grid is
demand x floor, which is the selection frame's own pair of axes.

PREDICTIONS (fixed before the engine).

PR1 (floor 0). No standing family, for a structural reason rather than
a contingent one: a poset's moves are DESTINATIONS, so a move object
cannot even be shared between two states, and a recipe M(s) in A(s)
exists exactly where A(s) is nonempty -- which fails precisely at the
tombstones. The schema is vacuous at floor 0, and what it wants from
floor 1 is the monoid ACTION (moves as increments), not the weight.

PR2 (floor 1). Up-closure -- the hot-limit theorem's hypothesis, and
the only availability guarantee that ladder floor states -- does NOT
supply a standing family. Up-closure says a*A(s) is contained in A(s),
so the cheapest admissible a-multiple costs at most w(a) * (the greedy
cost) and at least the greedy cost: a cap ABOVE what the walk is
already paying caps nothing. Floor 1's guarantee is a MASS floor
(explore_hot_limit.py's uniform opening bound, which is what the
thermal theorem consumes) and the greedy schema needs a COST bound.
Predicted numerically: over Z's D-DYN the cheapest admissible
a-multiple never falls below the greedy cost at any visited state, for
every a in a scanned range.

PR3 (D-IND, floor 2). Standing availability fails by CONSUMPTION:
support-avoidance makes an atom inadmissible forever once used, so
every move under a fixed cost ceiling is permanently dead after a
finite stage and no recipe of bounded cost survives. Hence no cap, the
costs diverge, and the walk does not lock -- breadth realizes the
escape branch VACUOUSLY, having no coordinates to run away.

PR4 (D-DYN, over Z). A standing family exists and is the DOOR MENU, one
recipe per prime, and its existence comes from the door identity
(lambda(q^d) has unbounded q-part) rather than from any floor of the
ladder. Its pricing coordinate is predicted to be the EXCESS
x_q(N) = v_q(lambda(N)) - v_q(N), with door cost q^(x_q + 2) on the
deepening branch, and the recurrence invariant of the lock-prime law
(v_q(lambda) = e_q - 1) is predicted to be exactly x_q = -1 -- a
CONSTANT cap, so Corollary A relocks the trajectory without
enumerating a single ghost. What the schema is predicted NOT to
recover is WHICH prime: the basin map is the wander bound's and lies
outside it.

PR5 (the verdict). Whether a standing family exists will turn out to be
a property of the DEMAND -- does it consume its moves? -- and not of
the structural floor. Freeness enters one step later, deciding whether
a consuming demand survives at all (in NUM23 independence is mortal).
So the answer to "which floor supplies the hypothesis" is predicted to
be NONE, with the supplying property named instead.

PR6 (kill-shapes, as observables). The rig prints per cell: a boolean
for standing availability over every visited state; the greedy cost
against the family cap step by step; the excess coordinate's trace; and
lock / no-lock. KILL-A: a printed greedy cost STRICTLY ABOVE the
printed cap at any state falsifies (S2) as stated or the door
computation. KILL-B: a printed standing recipe of bounded cost in the
D-IND cell would predict a lock there, and breadth does not lock --
that falsifies the schema itself rather than the cell. KILL-C: the
excess coordinate failing to be constant along a locked tail
falsifies PR4's identification of the invariant with the coordinate.

POSITIVE CONTROL (run before any verdict is read). The door menu is
recomputed from the definition of lambda by brute scan and must agree
with the closed form at every state visited; greedy D-DYN must
reproduce the recorded basin behaviour (seed 71 ghosts through 5 and 7
and locks 17); greedy D-IND from seed 1 must reproduce the primes in
increasing order. A harness that misses any of these has no standing to
report a verdict.

FINDINGS (tiers per the standard naming scale; run record below; all
sections assert).

1. THE STANDING-MOVE DICHOTOMY (rule, proved -- the schema, and it is
   about greedy walks rather than about rings). Under (S1), (S2) and
   (S3) above: the walk pays at most min_i f_i(x_i(s)) at every step,
   so either some coordinate stays bounded along a subsequence -- and
   then a move of bounded cost recurs infinitely often and absorbs the
   tail, a LOCK -- or every coordinate diverges at once. Corollary A: a
   family
   member priced CONSTANT in the state locks the walk outright.
   Corollary B: escape is a conjunction over the whole family. Two
   recorded results of this corpus turn out to be the two branches at
   one dial setting apart. Over Z the depth walk's cheapest standing
   price goes CONSTANT and the trajectory locks (the lock-prime law,
   explore_lock_prime.py); in a characteristic-zero ring the door's
   price GROWS with the state and an escape has to outrun every
   index simultaneously (the escape's conjunction,
   explore_module_law.py). The dial is whether the standing move's
   price is constant in the state or a growing function of one of its
   coordinates, and nothing else separates the two arguments.

2. THE PRICING COORDINATE IS THE EXCESS, AND IT HAS A FLOOR (rule,
   proved; verified S2). Write x_q(N) = v_q(lambda(N)) - v_q(N). The
   deepening door is exactly q^(x_q + 2) (22/22 deepening states), and
   q^(x_q + 2) BOUNDS the door at q in every branch -- 402 exact and
   1326 strict over 1728 odd-prime/state pairs, the strict ones being
   the openings, where a ghost pays only q. At ODD q the coordinate is
   bounded BELOW at -1, and that is PROVED rather than censused: q^e
   divides N, so lambda(q^e) divides lambda(N), and lambda(q^e) carries
   q^(e-1), giving v_q(lambda) >= e_q - 1. The census agrees
   (1728/1728, floor reached at 113 pairs). The
   recurrence invariant of the lock-prime law -- v_q(lambda) = e_q - 1
   at odd q, e_q - 2 at q = 2 -- IS x_q = -1: the coordinate sitting on
   its own floor. THE QUALIFIER IS THE PRIME. At q = 2 the invariant
   shifts by one, so the floor sits at -2 and the bound reads
   2^(x + 3), which holds at 71 of the 72 states censused -- the
   exception the virgin state, where 2's door is 4. Every odd-q figure
   here excludes q = 2 for that reason. So the lock is
   not a second mechanism beside the cap -- it is the cap pinned at the
   bottom of the coordinate that prices it. Along seed 71's locked tail
   x_17 = -1 and door_17 = 17 hold constant for six steps, out to
   N = 59,981,858,965. THE WELD: the cascade's budget inequality prices
   the EXCESS of V over a carrier's own exponent and proves it
   unbuyable UPWARD; the recurrence invariant pins the same coordinate
   at its floor from BELOW. One coordinate, two directions, two worlds.

3. THE DEPTH CELL HAS A STANDING FAMILY, AND NO FLOOR SUPPLIED IT
   (rule, proved; verified S1-S2). The door at q exists from every
   state for one reason -- lambda(q^d) has unbounded q-part, so some
   power of q always grows lambda -- and 1800/1800 state-prime pairs
   over twelve seeded walks have their door admissible. What the cap
   trace carries is its VALUES, not the inequality -- greedy under the
   family minimum is forced once the door is admissible (finding 7's
   caveat): seed 71 pays 5, 7, 17, 17, 17, 17 against caps of exactly
   those figures, seed 210 sits at 5 throughout, and it is the caps
   GOING CONSTANT that says anything. That existence is the door
   identity's, a fact about lambda in this world, and not a gift of any
   structural floor.

4. FLOOR 1 SUPPLIES THE HYPOTHESIS IN THE WRONG CURRENCY (rule,
   proved; verified S5). Up-closure -- the hot-limit theorem's one
   availability hypothesis (explore_hot_limit.py) -- gives a*A(s)
   contained in A(s) (141 pairs at N = 210), hence a standing SET
   whose cheapest member costs at most w(a) times the greedy cost and
   never less: 0/16 cheapest admissible a-multiples fell below the
   greedy cost, ratios 1.00 to 3.57. A cap sitting above what the walk
   already pays caps nothing. Floor 1's guarantee is a MASS floor,
   which is exactly what the thermal theorem consumes and exactly what
   the greedy schema cannot use. The two theorems share a hypothesis
   and spend it in different currencies -- which is why the cofinal hot
   limit and the locking greedy walk coexist in one world.

5. BREADTH IS INSIDE THE SCHEMA, ON THE ESCAPE BRANCH, AND CONSUMPTION
   IS WHAT PUTS IT THERE (rule, proved; verified S3; the reading this
   record first printed -- "no standing family at all" -- corrected by
   explore_standing_recipe.py). Support-avoidance kills a MOVE
   permanently on use: every move of cost <= 30 is permanently
   inadmissible by step 10 and none resurrects, the deaths arriving in
   the order 2, 4, 6, 8, 10, 12 at step 1, then 3 and 9, then 5, then
   7. But availability is a RECIPE's, by this record's own correction
   above, and the recipe "the least prime not dividing N" is admissible
   at every state, its cost the greedy cost, its coordinate omega(N).
   So D-IND has a standing family; what it has none of is a standing
   recipe of BOUNDED price -- no move recurs -- which is exactly the
   escape branch. Its costs are the primes and diverge, and reading
   that as the schema's escape is now the RIGHT reading, with the
   mechanism named: consumption selects the branch. The one-recipe
   family is BLIND (its coordinate never repeats) and the sibling
   record's per-class family is the non-blind one.

6. NO FLOOR SUPPLIES IT, AND THE THREE FAIL IN THREE DIFFERENT PLACES
   (synthesis -- this record's headline; verified S4, S6). The three
   failures are NOT one failure repeated, and the design's expectation
   that availability would be the whole story is wrong at the bottom
   floor. FLOOR 0 fails on PRICING, not on availability: on the region
   {1, 2, 3, 6} under the interval demand the maximum 6 lies in A(1),
   A(2) and A(3) -- a constant standing move over every state that
   still moves -- so (S1) is satisfied and it is (S2) that has nothing
   to read, a bare order carrying no cost. Two weightings of that same
   order send greedy to 2 and to 3 from the same state: price is data
   the order does not carry. Add a price to that same order and the
   cell becomes finding 7's. FLOOR 1 fails on the CURRENCY of availability: it
   has increments and prices them in mass (finding 4). FLOOR 2 supplies
   availability in the RECIPE sense and destroys it in the fixed-move
   sense: freeness is what lets the independence demand be
   support-avoiding, i.e. CONSUMING, which is the escape branch's
   selector and not the schema's edge (finding 5, corrected). So the answer
   to "which floor of the selection ladder supplies the standing
   hypothesis" is NONE, and what the DEMAND supplies -- whether it
   consumes what it offers -- is the BRANCH, a third axis beside the
   selection frame's two (structure floor x selection need). Freeness enters one step later, deciding not whether a
   consuming demand has a cap but whether it survives at all: in NUM23,
   cancellative and non-free, every maximal independence path from the
   identity has length at most 2 (the twelve maximal paths enumerated),
   because every x^n with n >= 5 carries both atoms.

7. THE CLOSURE'S OWN MOVE, AND WHERE THE THIRD FATE SITS (rule, proved;
   verified S4). Priced, floor 0's cell is the transparency walk, whose
   wall map is a closure operator, and a closure hands the schema a
   standing move outright: from any state the jump m = V = W(lambda(N))/N
   lands on the closure N*, and lambda(N*) = lambda(N) because
   lambda(W(lambda(N))) divides lambda(N) by construction while lambda
   is monotone. So the move is admissible from every live state and
   priced by ONE
   coordinate -- the HEADROOM V itself, which is the percept the sighted
   probe reads. Measured at 13 states off seeds 3, 5, 7: admissible
   throughout, V falling 48, 24, 12, 6, 3, 1 off seed 5. The coordinate
   is BOUNDED and
   descends to 1, which is the dichotomy's absorbing branch, so
   MORTALITY is not outside the schema at all -- it is the lock branch
   with the coordinate collapsing rather than merely staying bounded.
   Two of the three fates therefore sit inside: depth locks with the
   coordinate pinned at its floor, mortality absorbs with the
   coordinate driven to its bottom, and BREADTH is the one fate the
   schema does not reach, for the reason finding 5 gives. (That V sits
   at or above the greedy cost is FORCED once V is admissible, greedy
   being the minimum over the same set: a harness check on the wall
   computation and not evidence for the cap. The depth cell's cap trace
   carries the same caveat -- what carries evidence there is the
   availability census and the VALUES the cap takes.) (The wall
   values this uses reproduce the recorded 24, 240, 504, 480, 264,
   65520 at L = 2..12, which is the new helper's own control.)

SCOPE + HONESTY. The schema was first written asking for a fixed MOVE
available from every state; the design corrected it to a RECIPE before
the engine, and the correction is load-bearing -- the door at a fixed q
is a DIFFERENT element from state to state (5 at N = 71, 25 at N = 355),
so the uncorrected statement has nothing to point at in the very cell
that motivated it. D-DYN's inadmissible set at N is the divisors of
W(lambda(N))/N, so a fixed integer's admissibility genuinely does lapse;
that every m in 2..60 lapses at some N <= 4000 is scanned here and NOT
proved for all m, and the finding does not rest on it. The
dichotomy's third leg -- norm-finiteness plus absorption -- is imported
from the cascade record rather than re-proved here. AND THE WELD IS
UNEVEN, which the finding should not be read past: over Z the excess is
DEFINED out of the door formula, so "the invariant is the coordinate on
its floor" is a re-description of q^(v-e+2) and carries no new content
by itself. What carries content is the other side -- that a different
world, priced by a different construction, turns out to charge the SAME
quantity, and that its budget inequality bounds from above what the
invariant pins from below. Everything measured
is over Z apart from two specimens: NUM23 for floor 1 without floor 2,
and a four-element divisor region for floor 0; the censuses are bounded
(twelve seeds, twenty-five primes, six steps). The schema is stated for
cost-minimising walks and says nothing about thermal ones, which is
finding 4's whole point. What the schema does NOT recover in the depth
cell is WHICH prime the walk locks: the basin map is the wander bound's
and lies outside it. The stripped argument's SECOND target -- the wall
map of a sighted probe read as a closure operator, where the
always-available move is the one a closure always admits -- was run here
too and is finding 7; what stays untouched is any world outside Z and
the two specimens above.

PREDICTIONS (fixed before the engine; outcomes). PR1 REFUTED, and with
it the design's framing sentence that availability is the half doing all
the work. Floor 0 does have a standing family -- the maximum sits in
every nonempty admissible set, so a move object IS shared between
states, which is exactly what PR1 said could not happen -- and the floor
fails on PRICING instead, a bare order carrying no cost for (S2) to
read. The verdict of finding 6 survives the refutation and its reason
does not. PR2 confirmed (0/16 below the greedy cost). PR3 confirmed as an
observable (the deaths) and its reading -- no standing family -- later
corrected (explore_standing_recipe.py).
PR4 confirmed including the excess identification, with the bound
extending to every branch rather than the deepening one only, and the
coordinate's floor at -1 unpredicted. PR5 confirmed. PR6: no
kill-shape fired -- no greedy cost above its cap, no bounded standing
recipe in the breadth cell, the excess constant along the locked tail.

RUN RECORD (python 3, one process, 8.1 s wall, well under the memory
ceiling; exit 0, 8,126 checks).
  S1 control: 440/440 door closed-form vs brute agreements, of which
     429 at odd q and 11 at q = 2, where both routes scan and the
     agreement is vacuous; seed 71 picks 5, 7, 17, 17, 17, 17; D-IND
     picks 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
  S2 depth cell: 1800/1800 doors admissible; 22/22 deepening doors
     equal to q^(excess+2); 402 exact + 1326 strict bounds over 1728
     odd-q pairs; lowest excess -1 at 113 pairs; q = 2 apart, lowest
     excess 0 over 72 states with the bound 2^(x+3) at 71 of them;
     greedy at or under the cap at every printed step; locked tail
     constant at (-1, 17)
  S3 breadth cell: every move of cost <= 30 dead by step 10, none
     resurrected at any later step; costs the first twelve primes
  S4 mortality + floor 0: D-TRA tombstones 24, 240, 504; W control at
     L = 2..12 reproducing 24, 240, 504, 480, 264, 65520; the closure
     move admissible at 13 states, V descending
     48, 24, 12, 6, 3, 1 off seed 5; the region {1, 2, 3, 6} with the
     maximum standing in every nonempty A(s) and two weightings of that
     order disagreeing on the first move
  S5 floor 1: 0/16 a-multiples below the greedy cost; 141 up-closure
     pairs at N = 210
  S6 NUM23: n >= 5 carries both atoms for 5 <= n <= 29; twelve maximal
     independence paths, all of length <= 2, the four 2-move ones being
     the recorded (2,3), (3,2), (3,4), (4,3) -- this cell's control
  TOTAL 8,126 checks, exit 0.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

CHECKS = 0


def check(cond, msg=""):
    global CHECKS
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)
    CHECKS += 1


# ---------- primes / factorization ----------

def sieve(limit):
    is_p = bytearray([1]) * (limit + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            is_p[i * i:: i] = bytearray(len(is_p[i * i:: i]))
    return [i for i in range(limit + 1) if is_p[i]]


PRIMES = sieve(200_000)
PRIMESET = set(PRIMES)


def factorize(m):
    f = {}
    for p in PRIMES:
        if p * p > m:
            break
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


# ---------- lambda as a factor dict ----------

def lam_pp_factors(q, d):
    """Factor dict of lambda(q^d)."""
    if d == 0:
        return {}
    if q == 2:
        if d == 1:
            return {}
        if d == 2:
            return {2: 1}
        return {2: d - 2}
    f = dict(factorize(q - 1))
    if d >= 2:
        f[q] = f.get(q, 0) + (d - 1)
    return f


def maxmerge(A, B):
    out = dict(A)
    for p, e in B.items():
        if out.get(p, 0) < e:
            out[p] = e
    return out


def divides(A, B):
    """Does the integer with factor dict A divide the one with dict B?"""
    return all(B.get(p, 0) >= e for p, e in A.items())


def lam_factors(Nf):
    """lambda(N) as a factor dict, N given as a factor dict."""
    out = {}
    for q, d in Nf.items():
        out = maxmerge(out, lam_pp_factors(q, d))
    return out


def lam_int(Nf):
    out = 1
    for p, e in lam_factors(Nf).items():
        out *= p ** e
    return out


def to_int(Nf):
    out = 1
    for p, e in Nf.items():
        out *= p ** e
    return out


def mul_factors(Nf, mf):
    out = dict(Nf)
    for p, e in mf.items():
        out[p] = out.get(p, 0) + e
    return out


# ---------- the three demands over Z ----------

def dyn_admissible(Nf, m):
    """D-DYN: does multiplying N by m grow lambda?"""
    lam_N = lam_factors(Nf)
    lam_Nm = lam_factors(mul_factors(Nf, factorize(m)))
    return not divides(lam_Nm, lam_N)


def ind_admissible(Nf, m):
    """D-IND: is Z/Nm ~ Z/N x Z/m, i.e. gcd(N, m) = 1?"""
    return all(Nf.get(p, 0) == 0 for p in factorize(m))


def tra_admissible(Nf, m):
    """D-TRA: capacity grows with lambda frozen."""
    lam_N = lam_factors(Nf)
    lam_Nm = lam_factors(mul_factors(Nf, factorize(m)))
    return divides(lam_Nm, lam_N)


def greedy_move(Nf, admissible, cap=200_000):
    """The least m >= 2 the demand admits, or None inside the ceiling."""
    for m in range(2, cap + 1):
        if admissible(Nf, m):
            return m
    return None


# ---------- the door menu (the candidate standing family) ----------

def door_closed_form(Nf, q):
    """The door at q by the recorded closed form (explore_lock_prime.py)."""
    lam_N = lam_factors(Nf)
    e = Nf.get(q, 0)
    v = lam_N.get(q, 0)
    if q == 2:
        r = 1
        while divides(lam_pp_factors(2, e + r), lam_N):
            r += 1
        return 2 ** r
    if e >= 1:
        r = v - e + 2
        return q ** r
    if not divides(factorize(q - 1), lam_N):
        return q
    return q ** (v + 2)


def door_brute(Nf, q, rmax=64):
    """The door at q straight from the definition: least q^r growing lambda."""
    lam_N = lam_factors(Nf)
    e = Nf.get(q, 0)
    for r in range(1, rmax + 1):
        if not divides(lam_pp_factors(q, e + r), lam_N):
            return q ** r
    return None


def W_of(L):
    """The transparency wall: the largest n with lambda(n) dividing L.

    lambda(p^e) = p^(e-1)(p-1) for odd p, so p contributes iff (p-1) | L
    and then at exponent v_p(L) + 1; lambda(2^e) = 2^(e-2) for e >= 3,
    so 2 contributes at v_2(L) + 2 when L is even and at 1 when it is odd.
    """
    Lf = factorize(L) if L > 1 else {}
    divs = [1]
    for p, e in Lf.items():
        divs = [d * p ** i for d in divs for i in range(e + 1)]
    out = 2 ** (1 if L % 2 else Lf.get(2, 0) + 2)
    for d in divs:
        p = d + 1
        if p > 2 and (p in PRIMESET or (p > PRIMES[-1] and is_prime_slow(p))):
            out *= p ** (Lf.get(p, 0) + 1)
    return out


def is_prime_slow(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def excess(Nf, q):
    """The pricing coordinate: v_q(lambda(N)) - v_q(N)."""
    return lam_factors(Nf).get(q, 0) - Nf.get(q, 0)


# ---------- walks ----------

def walk(seed_factors, admissible, steps, cap=200_000):
    """Greedy trajectory: list of (state factor dict, move, cost)."""
    Nf = dict(seed_factors)
    out = []
    for _ in range(steps):
        m = greedy_move(Nf, admissible, cap)
        if m is None:
            out.append((dict(Nf), None, None))
            break
        out.append((dict(Nf), m, m))
        Nf = mul_factors(Nf, factorize(m))
    return out


# ---------- NUM23: the cancellative non-free world ----------
# elements are exponents n with n = 0 or n >= 2 (x^n); the monoid law is
# addition of exponents; atoms are 2 and 3.

def num23_elements(cap):
    return [0] + [n for n in range(2, cap + 1)]


def num23_atoms(n):
    """Which atoms divide x^n inside the monoid (n - 2 and n - 3 in M)."""
    out = set()
    for a in (2, 3):
        r = n - a
        if r == 0 or r >= 2:
            out.add(a)
    return out


def main():
    print("=" * 72)
    print("THE STANDING-MOVE DICHOTOMY -- the schema run at the selection")
    print("ladder. Sections S1-S6; the control is S1.")
    print("=" * 72)

    # ---------------- S1 POSITIVE CONTROL ----------------
    print("\nS1  POSITIVE CONTROL -- the harness against recorded facts")
    print("-" * 72)

    # (a) door closed form against the brute definition
    seeds = [1, 3, 5, 7, 9, 15, 71, 100, 121, 210, 1001]
    agree = odd_agree = 0
    for s in seeds:
        Nf = factorize(s) if s > 1 else {}
        for q in PRIMES[:40]:
            a = door_closed_form(Nf, q)
            b = door_brute(Nf, q)
            check(a == b, "door mismatch N=%d q=%d: %s vs %s" % (s, q, a, b))
            agree += 1
            if q != 2:
                odd_agree += 1
    print("  door closed form == brute definition: %d/%d state-prime pairs"
          % (agree, agree))
    print("  of which %d at odd q, where the closed form is a FORMULA; the"
          % odd_agree)
    print("  q = 2 door is a scan on both routes, so its %d agreements are"
          % (agree - odd_agree))
    print("  not evidence for anything and are not counted as control")

    # (b) D-DYN basin behaviour at seed 71
    tr = walk(factorize(71), dyn_admissible, 8)
    picks = [m for (_, m, _) in tr if m is not None]
    print("  D-DYN from seed 71, first picks:", picks[:6])
    check(picks[0] == 5 and picks[1] == 7,
          "seed 71 should ghost 5 then 7, got %s" % picks[:2])
    check(picks[2] == 17, "seed 71 should lock 17, got %s" % picks[2])
    check(all(p == 17 for p in picks[3:]),
          "post-lock picks should all be 17, got %s" % picks[3:])
    print("  ghosts 5, 7 then locks 17, every later pick 17: as recorded")

    # (c) D-IND from seed 1 is the primes in order
    tri = walk({}, ind_admissible, 12)
    ipicks = [m for (_, m, _) in tri if m is not None]
    print("  D-IND from seed 1, picks:", ipicks)
    check(ipicks == PRIMES[:len(ipicks)], "D-IND should be primes in order")
    print("  primes in increasing order: as recorded")
    print("  CONTROL PASSED -- verdicts below may be read.")

    # ---------------- S2 THE DEPTH CELL ----------------
    print("\nS2  THE DEPTH CELL (D-DYN over Z) -- is the door menu a")
    print("    standing family, and what coordinate prices it?")
    print("-" * 72)

    avail = 0
    for s in [1, 3, 5, 7, 9, 15, 71, 100, 121, 210, 1001, 2310]:
        Nf = factorize(s) if s > 1 else {}
        for _ in range(6):
            for q in PRIMES[:25]:
                d = door_closed_form(Nf, q)
                check(d is not None, "no door at q=%d" % q)
                check(dyn_admissible(Nf, d),
                      "door %d at q=%d not admissible from %d" % (d, q, s))
                avail += 1
            m = greedy_move(Nf, dyn_admissible)
            Nf = mul_factors(Nf, factorize(m))
    print("  (S1) standing availability: %d/%d state-prime pairs admissible"
          % (avail, avail))

    print("\n  (S2) pricing coordinate -- door cost against q^(excess+2)")
    print("  %-10s %-4s %-6s %-6s %-8s %-10s" %
          ("N", "q", "e_q", "v_q", "excess", "door"))
    priced = 0
    mism = 0
    for s in [71, 210, 1001]:
        Nf = factorize(s) if s > 1 else {}
        for _ in range(4):
            for q in (3, 5, 7, 17):
                e, v = Nf.get(q, 0), lam_factors(Nf).get(q, 0)
                d = door_closed_form(Nf, q)
                pred = q ** (excess(Nf, q) + 2) if e >= 1 else None
                if e >= 1:
                    priced += 1
                    if pred != d:
                        mism += 1
                    check(pred == d,
                          "deepening door != q^(excess+2) at N=%d q=%d"
                          % (to_int(Nf), q))
                if to_int(Nf) < 10 ** 7:
                    print("  %-10d %-4d %-6d %-6d %-8d %-10s" %
                          (to_int(Nf), q, e, v, excess(Nf, q), d))
            m = greedy_move(Nf, dyn_admissible)
            Nf = mul_factors(Nf, factorize(m))
    print("  deepening doors matching q^(excess+2): %d/%d (mismatches %d)"
          % (priced - mism, priced, mism))

    print("\n  is q^(excess+2) a bound on the door in EVERY branch, and")
    print("  how far down can the coordinate go?")
    exact = loose = 0
    floor_hits = 0
    lowest = 99
    for s in [1, 3, 5, 7, 9, 15, 71, 100, 121, 210, 1001, 2310]:
        Nf = factorize(s) if s > 1 else {}
        for _ in range(6):
            for q in PRIMES[1:25]:
                x = excess(Nf, q)
                d = door_closed_form(Nf, q)
                check(x >= -1, "excess %d below -1 at N=%d q=%d"
                      % (x, to_int(Nf), q))
                check(d <= q ** (x + 2),
                      "door %d above q^(excess+2) at N=%d q=%d"
                      % (d, to_int(Nf), q))
                if d == q ** (x + 2):
                    exact += 1
                else:
                    loose += 1
                if x == -1:
                    floor_hits += 1
                lowest = min(lowest, x)
            Nf = mul_factors(Nf, factorize(greedy_move(Nf, dyn_admissible)))
    print("  odd-q doors bounded by q^(excess+2): %d exact, %d strict"
          % (exact, loose))
    print("  lowest excess seen: %d, reached at %d of %d pairs"
          % (lowest, floor_hits, exact + loose))

    # q = 2 is a DIFFERENT coordinate: its recurrence invariant is e - 2,
    # not e - 1, so its floor sits one lower and its bound shifts by one.
    two_low = 99
    two_form = two_n = 0
    for s in [1, 3, 5, 7, 9, 15, 71, 100, 121, 210, 1001, 2310]:
        Nf = factorize(s) if s > 1 else {}
        for _ in range(6):
            x = excess(Nf, 2)
            two_low = min(two_low, x)
            two_n += 1
            if door_closed_form(Nf, 2) == 2 ** (x + 3):
                two_form += 1
            Nf = mul_factors(Nf, factorize(greedy_move(Nf, dyn_admissible)))
    print("  q = 2 apart: lowest excess %d over %d states, door = 2^(x+3)"
          % (two_low, two_n))
    print("  at %d of them -- the invariant at 2 is e - 2, so the floor and"
          % two_form)
    print("  the bound both shift by one and the odd-q figures exclude it")

    # NOTE ON WHAT THE NEXT CHECK IS WORTH. greedy is the minimum over
    # A(s) and the door is IN A(s), so greedy <= cap is forced the moment
    # standing availability holds: this is a harness check on the door
    # computation and the move scan, never independent evidence for the
    # cap. What carries evidence is the availability census above and the
    # VALUES the cap takes -- constant at the lock, growing off it.
    print("\n  the cap: greedy cost against min over the family")
    for s in [71, 210]:
        Nf = factorize(s) if s > 1 else {}
        for t in range(6):
            capv = min(door_closed_form(Nf, q) for q in PRIMES[:25])
            m = greedy_move(Nf, dyn_admissible)
            check(m <= capv, "greedy %d above cap %d" % (m, capv))
            print("    seed %-5d step %d  N=%-14d greedy=%-8d cap=%-8d"
                  % (s, t, to_int(Nf), m, capv))
            Nf = mul_factors(Nf, factorize(m))

    print("\n  the locked tail: the excess at the locked prime")
    Nf = factorize(71)
    for _ in range(3):
        Nf = mul_factors(Nf, factorize(greedy_move(Nf, dyn_admissible)))
    tail = []
    for _ in range(6):
        tail.append((to_int(Nf), excess(Nf, 17), door_closed_form(Nf, 17)))
        Nf = mul_factors(Nf, factorize(greedy_move(Nf, dyn_admissible)))
    for (n, x, d) in tail:
        print("    N=%-22d excess_17=%-4d door_17=%-6d" % (n, x, d))
    check(all(x == tail[0][1] for (_, x, _) in tail),
          "excess not constant along the locked tail")
    check(all(d == tail[0][2] for (_, _, d) in tail),
          "door not constant along the locked tail")
    print("  excess and door both constant along the tail: %d, %d"
          % (tail[0][1], tail[0][2]))

    # ---------------- S3 THE BREADTH CELL ----------------
    print("\nS3  THE BREADTH CELL (D-IND over Z) -- consumption")
    print("-" * 72)

    Nf = {}
    ceiling = 30
    dead_at = {}
    for t in range(15):
        for m in range(2, ceiling + 1):
            if m not in dead_at and not ind_admissible(Nf, m):
                dead_at[m] = t
            elif m in dead_at:
                check(not ind_admissible(Nf, m),
                      "move %d resurrected at step %d" % (m, t))
        Nf = mul_factors(Nf, factorize(greedy_move(Nf, ind_admissible)))
    for m in range(2, ceiling + 1):
        check(m in dead_at, "move %d never died under D-IND" % m)
        check(not ind_admissible(Nf, m),
              "move %d resurrected under D-IND" % m)
    print("  every move of cost <= %d permanently inadmissible by step %d"
          % (ceiling, max(dead_at.values())))
    print("  death step by move:",
          {m: dead_at[m] for m in sorted(dead_at)[:12]})
    costs = [m for (_, m, _) in walk({}, ind_admissible, 12)]
    print("  greedy costs:", costs)
    check(costs == sorted(costs) and costs[-1] > costs[0],
          "D-IND costs should diverge")
    print("  costs diverge, no move recurs, no lock")

    # ---------------- S4 THE MORTALITY CELL AND FLOOR 0 ----------------
    print("\nS4  THE MORTALITY CELL (D-TRA over Z) and FLOOR 0")
    print("-" * 72)

    for s in (3, 5, 7):
        tr = walk(factorize(s), tra_admissible, 30)
        last = tr[-1][0]
        check(tr[-1][1] is None, "D-TRA from %d did not die" % s)
        print("  D-TRA from seed %d dies at N=%d after %d moves"
              % (s, to_int(last), len(tr) - 1))
        check(greedy_move(last, tra_admissible) is None,
              "tombstone still has a move")
    # control for the new instrument: W against the recorded wall values
    walls = {2: 24, 4: 240, 6: 504, 8: 480, 10: 264, 12: 65520}
    for L, w in walls.items():
        check(W_of(L) == w, "W(%d) = %d, recorded %d" % (L, W_of(L), w))
    print("  W control: W(L) at L = 2..12 gives %s -- as recorded"
          % [walls[L] for L in sorted(walls)])

    # the closure's own move: jump the whole interval, m = V = W(lam(N))/N
    print("\n  the closure move m = V: admissible, and what prices it")
    print("  %-8s %-10s %-8s %-8s" % ("N", "V", "greedy", "V >= greedy"))
    vcount = 0
    for s in (3, 5, 7):
        Nf = factorize(s)
        while True:
            V = W_of(lam_int(Nf)) // to_int(Nf)
            g = greedy_move(Nf, tra_admissible)
            if g is None:
                check(V == 1, "tombstone with V = %d" % V)
                print("  %-8d %-10d %-8s %-8s"
                      % (to_int(Nf), V, "none", "-"))
                break
            check(tra_admissible(Nf, V), "closure move V=%d inadmissible" % V)
            check(g <= V, "greedy %d above the closure move %d" % (g, V))
            vcount += 1
            print("  %-8d %-10d %-8d %-8s" % (to_int(Nf), V, g, "yes"))
            Nf = mul_factors(Nf, factorize(g))
    print("  the closure move is admissible and caps greedy at %d states,"
          % vcount)
    print("  priced by ONE coordinate -- the headroom V itself -- so the")
    print("  mortality cell HAS a standing family; its coordinate is bounded")
    print("  and falls to 1, which is the dichotomy's absorbing branch")
    print("  (S1) fails only AT the tombstone, where A(s) is empty")

    # floor 0: which half of the schema actually fails here?
    region = [1, 2, 3, 6]
    up = {1: [2, 3, 6], 2: [6], 3: [6], 6: []}
    print("  poset region %s, interval demand:" % region)
    for s in region:
        print("    A(%d) = %s" % (s, up[s]))
    check(up[6] == [], "6 should be terminal")
    live = [s for s in region if up[s]]
    const = [d for d in region if all(d in up[s] for s in live)]
    check(const == [6], "expected the maximum to be the standing move")
    print("  destinations admissible from EVERY live state: %s" % const)
    print("  so availability is NOT what fails at floor 0 -- the maximum is")
    print("  a constant standing move over every state that still moves")
    # what fails is (S2): the order carries no cost and no coordinate
    firsts = []
    for w in ({1: 0, 2: 1, 3: 2, 6: 5}, {1: 0, 2: 2, 3: 1, 6: 5}):
        firsts.append(min(up[1], key=lambda d: w[d]))
    check(firsts[0] != firsts[1],
          "two weightings should disagree on the greedy first move")
    print("  two weightings of the SAME order pick %s and %s from state 1:"
          % (firsts[0], firsts[1]))
    print("  price is data the order does not carry, so (S2) has nothing to")
    print("  read -- floor 0 fails on PRICING, not on availability, and the")
    print("  standing move it does have reaches the tombstone in one step")

    # ---------------- S5 THE FLOOR-1 CLOSURE TEST ----------------
    print("\nS5  FLOOR 1 -- does up-closure supply a cost cap?")
    print("-" * 72)

    print("  cheapest admissible a-multiple against the greedy cost")
    print("  %-12s %-5s %-10s %-14s %-8s" %
          ("N", "a", "greedy", "cheapest a*", "ratio"))
    below = 0
    tested = 0
    Nf = factorize(71)
    for t in range(4):
        g = greedy_move(Nf, dyn_admissible)
        for a in (2, 3, 5, 7):
            best = None
            for k in range(1, 4000):
                m = a * k
                if m >= 2 and dyn_admissible(Nf, m):
                    best = m
                    break
            check(best is not None, "no admissible a-multiple found")
            tested += 1
            if best < g:
                below += 1
            if t < 2:
                print("  %-12d %-5d %-10d %-14d %-8.2f"
                      % (to_int(Nf), a, g, best, best / g))
        Nf = mul_factors(Nf, factorize(g))
    check(below == 0, "%d a-multiples fell below the greedy cost" % below)
    print("  a-multiples below the greedy cost: %d/%d" % (below, tested))

    # up-closure of D-DYN, the hypothesis floor 1 actually states
    Nf = factorize(210)
    upc = 0
    for m in range(2, 60):
        if dyn_admissible(Nf, m):
            for a in (2, 3, 5):
                check(dyn_admissible(Nf, a * m),
                      "up-closure fails at m=%d a=%d" % (m, a))
                upc += 1
    print("  up-closure a*A(s) subset A(s) holds: %d pairs at N=210" % upc)

    # ---------------- S6 NUM23: FLOOR 1 WITHOUT FLOOR 2 ----------------
    print("\nS6  NUM23 -- the cancellative non-free world")
    print("-" * 72)

    both = [n for n in range(5, 30) if num23_atoms(n) == {2, 3}]
    print("  elements x^n carrying BOTH atoms, n = 5..29:", both[:10], "...")
    check(both == list(range(5, 30)), "every n >= 5 should carry both atoms")
    # independence in NUM23: a move is admissible iff it shares no atom
    def n23_ind(state_n, move_n):
        return not (num23_atoms(state_n) & num23_atoms(move_n))
    maxpaths = []
    def extend(state, path):
        moves = [m for m in num23_elements(12) if m >= 2
                 and n23_ind(state, m)]
        if not moves:
            maxpaths.append(list(path))
            return
        for m in moves:
            extend(state + m, path + [m])
    extend(0, [])
    print("  maximal D-IND paths from the identity:", sorted(maxpaths))
    check(all(len(p) <= 2 for p in maxpaths),
          "D-IND in NUM23 should die by move 2")
    two = sorted(p for p in maxpaths if len(p) == 2)
    check(two == [[2, 3], [3, 2], [3, 4], [4, 3]],
          "the 2-move paths should be the recorded four, got %s" % two)
    print("  the four 2-move paths are the recorded set %s: control" % two)
    print("  every independence trajectory dead by move 2: floor 1 alone")
    print("  does not keep a consuming demand alive")

    print("\n" + "=" * 72)
    print("TOTAL CHECKS: %d" % CHECKS)
    print("=" * 72)


if __name__ == "__main__":
    main()
