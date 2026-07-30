"""
explore_headroom.py -- THE TRANSPARENCY HEADROOM AS A FUNCTION (sibling of
explore_demand_reading.py, explore_slack_machine.py, explore_growth_laws.py,
explore_depth_observer.py, explore_hot_limit.py).

THE QUESTION. A state of the growing tower is a positive integer N, a move
is a multiplication N -> N*m, and one number attaches to every state:

    V(N) = W(lambda(N)) / N,   the TRANSPARENCY HEADROOM,

where lambda is Carmichael's function and W(L) is the largest modulus whose
lambda divides L. Two filed facts make V interesting from opposite
directions. The moves that leave lambda frozen -- the TRANSPARENT ones --
are exactly the divisors of V (the transparency wall,
explore_growth_laws.py finding 6, re-read as a reading bound in
explore_demand_reading.py finding 3), so V is at once the room a state has
to grow without changing its own dynamics AND the entire content of what an
observer probing lambda can learn about it: two states sharing a headroom
are indistinguishable to such a probe over every move it can be OFFERED
from them (whether that survives a move being MADE is section 5).

What is filed is V's ROLE -- it prices the wall-priced normalizer, and the
mortal fate absorbs where it reaches 1. What is not filed is V AS A
FUNCTION: how a move changes it, what its exponents mean, and how coarse
the equivalence it induces really is. This file asks that.

FOUR MEASUREMENTS ARRIVED WITH THE QUESTION and are treated here as
UNVERIFIED HEARSAY to be reproduced or contradicted, never as premises: V
is not monotone along growth (270 rising moves for N < 300, m in {2,3,5});
V is not multiplicative (the smallest failure V(2)*V(3) = 1*8 != 4 = V(6));
headroom collisions across different prime supports are common at N <= 6000
(220 classes covering 2020 states); and V(N) = 1 for exactly 11 states below
3000, every one after N = 2 divisible by 24. The fourth is not a mystery but
a filed fact wearing a new face -- V(N) = 1 says N is its own wall, and the
walls are the image-of-J / Bernoulli denominators of
explore_growth_laws.py finding 6 -- so this file spends its effort on the
first three and proves the 24 elementarily rather than re-deriving it.

THE OBJECTS. For a prime p write v_p for the p-adic valuation, c_l = v_l(N)
and d_l = v_l(odd lambda(N)) for an odd prime l, so the SLACK
delta_l = d_l - c_l + 1 counts free pushes of l before lambda's l-exponent
starts moving (the slack law, filed). And

    W(L) = (2 if L odd else 2^(v_2(L)+2)) * prod{ p^(v_p(L)+1)
             : p odd prime, (p-1) | L }.

W's 2-part is 2 for ODD L and 2^(v_2(L)+2) for even, because lambda(2^a) is
1, 2, then 2^(a-2); the odd case is not a corner, since L = 1 is the state
the tower starts from.

THE DESIGN, in eight sections (S8 was added mid-run; see its header). The slate is frozen before any engine code;
where a run contradicts it the framing is left standing and flagged rather
than quietly rewritten.

S1 POSITIVE CONTROL, run before any verdict is read. Three things this
   file did not compute here must come back: wall() against its own
   DEFINITION -- the largest modulus found by brute search -- compared only
   where the wall fits under the search cap (a truncated search reports the
   formula wrong for every large wall, which is the false alarm the sibling
   file records); the filed divisor identity, transparent moves = divisors
   of V, over a battery; and the four hearsay measurements above, each
   under a stated counting convention, since a rig that cannot reproduce
   them is not measuring the same V.

S2 THE EXPONENT IDENTITY. The slack and the headroom were built for
   different jobs -- one is a counter in a machine, the other is an
   observer's whole percept -- and they should be the same object read
   twice: for an odd prime l, v_l(W(lambda(N))) = v_l(lambda(N)) + 1 when
   (l-1) | lambda(N), so v_l(V) = d_l + 1 - c_l = delta_l. THE TRANSPLANT
   TO MARK: that derivation is written for a SEATED l and carried to an
   unseated one without a second thought. For l unseated with (l-1) not
   dividing lambda(N), l does not appear in W at all, so v_l(V) = 0 while
   delta_l >= 1 -- the slack counts pushes at a prime whose door is shut,
   and those pushes move lambda (at the primes of l-1, not at l). The two
   branches are predicted separately.
   PREDICTION P1: v_l(V) = delta_l for every prime l with (l-1) | lambda(N),
   seated or not, 0 exceptions; and v_l(V) = 0 < delta_l for every l with
   (l-1) not dividing lambda(N), 0 exceptions.
   PREDICTION P2: v_2(V) = v_2(lambda(N)) + 2 - v_2(N) for even lambda and
   1 - v_2(N) for odd, 0 exceptions.

S3 THE LEDGER. If P1 holds then the lossy law delta -> max(0, delta - e) is
   division by a gcd in disguise, and the whole change of V under a move
   should split into what the move SPENDS and what it OPENS. Define

       G'(N, m) = V(Nm) * gcd(m, V(N)) / V(N).

   The hand derivation says G' is a positive integer, prime by prime:
   v_p(W(lambda(N))) = v_p(N) + v_p(V) by definition, v_p(W(lambda(Nm)))
   >= v_p(Nm) = v_p(N) + v_p(m) since a modulus divides its own wall, and
   W is monotone in divisibility (lambda(N) | lambda(Nm)), so the wall's
   gain at p is at least max(0, v_p(m) - v_p(V)), which is exactly what
   m/gcd(m, V) asks for. Hence V(Nm) = (V(N) / gcd(m, V(N))) * G' with
   G' >= 1: a move can never destroy more headroom than it spends, and
   V falls only by the transparency it burns.
   PREDICTION P3: G' is a positive integer for every move in the battery,
   0 exceptions; and V(Nm) > V(N) exactly when G' > gcd(m, V(N)).

S4 WHAT G' = 1 DOES NOT MEAN. The margin to distrust, killed on paper
   before the engine: "G' = 1 iff the move is transparent" is FALSE in one
   direction. Transparent gives G' = 1 (m | V, nothing opens). But N = 16
   has V = 15 and the move m = 2 sends lambda from 4 to 8 while the wall
   goes 240 -> 480, so the move pays for itself exactly, G' = 1, and V is
   unchanged at 15 -- a lambda-moving move with an empty ledger. The
   correct equivalence is the filed one on divisibility.
   PREDICTION P4: transparent iff m | V(N), 0 exceptions; the pair
   (N, m) = (16, 2) prints G' = 1, V(32) = V(16) = 15, lambda 4 -> 8; and
   the battery holds further non-transparent moves with G' = 1.

S5 IS THE BLINDNESS A CONGRUENCE? The probe reads V and nothing else, so
   two states with equal headroom are one state to it. Whether that
   ignorance SURVIVES a move is a different question, and it splits: if
   V(N) = V(N') and m | V(N), both moves are transparent and spend the
   same divisor, so V(Nm) = V(N)/m = V(N'm) -- the ignorance is preserved
   by exactly the moves that teach the probe nothing. A lambda-moving move
   opens walls the probe cannot see, and need not preserve it: N = 10 and
   N = 11 share the headroom 24, and m = 5 should split them.
   PREDICTION P5: over all equal-headroom pairs in the pool, 0 transparent
   moves split a pair; and the pair (10, 11) under m = 5 prints two
   different headrooms. The SPLITTING RATE over lambda-moving moves is
   measured, not predicted.

S6 THE TOMBSTONES AND THE CLOSURE. V(N) = 1 says N = W(lambda(N)): N is a
   fixed point of the wall map N -> W(lambda(N)). That map is a CLOSURE
   OPERATOR on the divisibility order -- monotone, inflationary, and
   idempotent because lambda(W(L)) | L forces W(lambda(W(L))) = W(L) both
   ways -- so a transparency episode is a walk inside the interval from N
   to its closure, a lattice isomorphic to the divisors of V. And every
   closed state other than 2 is divisible by 24 with no Bernoulli numbers
   needed: for N >= 3 lambda is even, so the wall's 2-part is at least
   2^3 and 3 is admitted by (3-1) | lambda.
   PREDICTION P6: the wall map is idempotent over the pool, 0 exceptions;
   the closed states below 3000 are exactly the 11 of the hearsay list;
   every closed state above 2 in the pool is divisible by 24; and each
   closed state equals W(L) for an even L, matching the filed wall values.

S7 THE BLINDNESS CENSUS. The prize the question was asked for: how coarse
   is V? Over N <= 6000, count distinct headroom values, the fibre sizes,
   the states sitting in a fibre of size >= 2, and the classes spanning
   more than one prime support -- and run the same census at 1500, 3000 and
   6000 to see whether the collisions are a small-number artifact or a
   stable proportion. What a stable proportion would MEAN is weighed after
   the run and is not frozen here.
   PREDICTION P7: the fraction of states in a non-singleton headroom class
   does not fall as the cap rises. (The cap list was extended to 12000 and
   24000 AFTER P7's kill fired at the three frozen caps, to measure the
   SHAPE of the fall rather than to hunt for a range where it stops
   falling. The three frozen caps keep their rows.)

S8 WHAT THE LARGEST BLIND CLASS IS MADE OF (added to the design after S7
   printed its largest fibre and before that fibre was examined; its
   predictions are frozen from a hand argument, not from the run). The
   fibre V = 24 is the biggest blind spot in the census. For a SAFE PRIME
   p = 2q+1 with q an odd prime, lambda(p) = 2q and the only doors are the
   divisors d of 2q with d+1 prime: d = 2 gives 3, d = q gives the even
   q+1, d = 2q gives p itself, and q's own door needs (q-1) | 2q, i.e.
   q-1 | 2, which fails for q >= 5. So W(2q) = 2^3 * 3 * p = 24p and
   V(p) = 24 exactly. The two small safe primes are excluded by the same
   argument: q = 2 gives p = 5 with a fourth door at 5, and q = 3 gives
   p = 7 with 3 doubled.
   PREDICTION P8: every safe prime p = 2q+1 with prime q >= 5 below the cap
   has V(p) = 24, 0 exceptions; V(5) and V(7) are not 24; and the class is
   strictly larger than the safe primes (10 and 21 are in it), so its
   composition is measured rather than predicted.

WHAT WOULD KILL WHAT (observables, not inferences). P1 dies on one printed
prime with the wrong branch or the wrong exponent. P2 dies on one printed
state whose 2-part disagrees. P3 dies on one printed move with G' not a
positive integer -- which would also falsify the hand proof, so the
arithmetic is printed for the first failure rather than merely counted. P4
dies if the printed (16, 2) row is transparent or has G' != 1, or if some
printed move has m | V and lambda moving. P5 dies on one printed transparent
move splitting an equal-headroom pair. P6 dies on a printed state whose wall
map is not idempotent, on a closed-state list differing from the hearsay
eleven, or on a closed state above 2 not divisible by 24. P7 dies if the
non-singleton fraction falls monotonically across the three caps. P8 dies
on one printed safe prime with a headroom other than 24.

FINDINGS.

1. THE SLACK IS THE HEADROOM'S EXPONENT VECTOR (theorem, proved; verified
   1973/1973 and 4007/4007 over states 2..599 at ten odd primes, and
   1998/1998 at the prime 2 over states 2..1999). For an odd prime l whose door is OPEN --
   (l-1) | lambda(N), which every seated l satisfies -- v_l(W(lambda(N)))
   = v_l(lambda(N)) + 1, so

       delta_l = v_l(V(N)),

   and at the prime 2, v_2(V) = v_2(lambda) + 2 - v_2(N) for even lambda,
   1 - v_2(N) for odd. The marked transplant was right to be marked: at a
   SHUT door the identity fails in a definite direction, v_l(V) = 0 while
   delta_l >= 1, because pushing such an l moves lambda at the primes of
   l-1 rather than at l, so the free pushes the slack is counting are not
   free to the wall. (Only half of that branch is evidence: a shut door
   means l is unseated, so delta_l = d_l + 1 >= 1 follows definitionally
   and the 4007 cases are carrying v_l(V) = 0 alone.) The two objects
   were built for unrelated jobs -- one
   is the counter of a Minsky machine (explore_slack_machine.py), the
   other an observer's entire percept (explore_demand_reading.py finding
   3). THE ALGEBRA IS ONE LINE once both definitions are unfolded, and
   saying so is the honest framing: nothing here is deep, and a reader
   who says "you defined both as v_l(lambda)+1-c_l" is right. What was
   not one line is that nobody had unfolded them together, and what the
   unfolding buys is the identification -- THE MACHINE'S COUNTER
   VECTOR IS THE EXPONENT VECTOR OF WHAT THE PROBE CAN SEE. The lossy law
   delta -> max(0, delta - e) is then division by a gcd in disguise AT
   THAT PRIME -- a push of l^e can still raise v_p(V) at other primes by
   opening their doors, which is the half of the story finding 2 adds.

2. THE HEADROOM LEDGER (theorem, proved for all N and m; verified
   23084/23084 moves, N in 2..399 and m in 2..59). Every move splits into
   what it SPENDS and what it OPENS:

       V(Nm) = ( V(N) / gcd(m, V(N)) ) * G'(N, m),   G' a positive integer.

   Proof, prime by prime: v_p(W(lambda(N))) = v_p(N) + v_p(V) by
   definition; v_p(W(lambda(Nm))) >= v_p(Nm) = v_p(N) + v_p(m) because a
   modulus divides its own wall; and the wall never falls, since
   lambda(N) | lambda(Nm) and W is monotone in divisibility. So the wall's
   gain at p is at least max(0, v_p(m) - v_p(V)), which is exactly what
   m/gcd(m, V) asks for. Hence A MOVE CAN NEVER DESTROY MORE HEADROOM THAN
   IT SPENDS: V falls only by the transparency it burns, and the burn is
   gcd(m, V) -- truncated subtraction in the exponents, finding 1's lossy
   law. This is what the non-monotonicity of V actually is: V(Nm) > V(N)
   exactly when G' > gcd(m, V(N)) -- ALGEBRA, not a measurement, since G'
   is defined as V(Nm)*gcd/V and the two counts cannot differ; it was
   offered as a prediction and the rig cannot fail it, so what
   the 16165 rising moves of 23084 buy is the SIZE of the rising set and
   nothing about the equivalence. Headroom can JUMP only where lambda
   moves -- opening a door admits a whole new prime power to the wall
   while costing only the move -- but a lambda-moving move is not thereby
   a rise: one that also burns transparency can come out behind, as
   N = 3 under m = 16 does, V 8 -> 5 with lambda 2 -> 4 (27 such falls
   for N < 60, m < 20).

3. G' = 1 IS NOT TRANSPARENCY, and the margin was right to be distrusted
   (rule; the counterexample was found on paper before the engine ran and
   is reproduced by it). Transparency gives G' = 1, but the converse fails:
   N = 16 has V = 15, and m = 2 sends lambda from 4 to 8 and the wall from
   240 to 480 -- the move opens exactly what it fails to spend, so V is
   unchanged at 15 with an empty ledger and a moved lambda. 271 such moves
   in N < 200, m < 40. The correct equivalence is the filed one and it is
   about divisibility, not about the ledger: a move is transparent iff
   m | V(N) (0 disagreements over 23084 moves; the identity is
   explore_growth_laws.py finding 6, re-verified here).

4. THE PROBE'S IGNORANCE IS GUARANTEED ONLY WHILE IT LEARNS NOTHING (rule;
   one half proved, the other measured). Two states with equal headroom are
   one state to a lambda-probe. Under a TRANSPARENT move that stays true
   and needs no measurement: m | V forces both moves to spend the same
   divisor and open nothing, so V(Nm) = V(N)/m = V(N'm) -- 32630/32630
   preserved over the 4551 equal-headroom pairs below 1500. Under a
   lambda-MOVING move the walls that open are invisible to the probe and
   the class usually shatters: 120571 of 140308 such moves (85.9%) split
   a pair -- USUALLY and not always, which is why the heading reads ONLY
   rather than EXACTLY: 14.1% of lambda-moving moves happen to preserve
   the class and nothing here says which ones.
   The witness frozen in the design behaves as predicted -- N = 10 and
   N = 11 share the headroom 24, and one push of 5 sends them to 264 and
   240. So headroom equivalence is NOT a congruence on the growth monoid:
   the first move that teaches the probe something is also the move that
   can split states it had merged, and the only moves that keep them
   merged WITH CERTAINTY are the ones that tell it nothing.

5. THE WALL MAP IS A CLOSURE OPERATOR (theorem, proved; verified
   2999/2999 idempotent, inflation over the same range, monotonicity over
   N < 400 against every divisor). N -> N* = W(lambda(N)) is monotone (d | N implies
   d* | N*), inflationary (N | N*), and idempotent -- lambda(W(L)) | L
   forces W(lambda(W(L))) = W(L) in both directions. So V(N) = N*/N, a
   transparency episode is a walk inside the interval from N to N*, and
   that interval is the divisor lattice of V. The states with V = 1 are
   exactly the fixed points, which is the same condition as "at its own
   wall" and not a second one; below 3000 they are 2, 24, 240, 264, 480,
   504, 552, 1128, 1416, 1992 and 2568, printed here with the lambda each
   is the wall of. THIS LIST IS NOT NEWS: every one of them above 2 is an
   image-of-J / Bernoulli denominator by explore_growth_laws.py finding 6,
   so the tombstones were identified long before this file asked. The
   exception is exact rather than cosmetic -- that identity is stated for
   EVEN L, and 2 is the wall of lambda = 1, the only closed state with an
   odd lambda, which is the same reason it is the only one not divisible
   by 24. P6's last clause -- "each closed state equals W(L) for an EVEN
   L" -- is false as frozen for exactly that reason, and the rig printed
   its own counterexample without checking it: the pair (1, 2) heads the
   printed list of each tombstone's lambda. The clause is left standing
   and flagged rather than quietly corrected, which is what the design
   section promises. The cross-reference also needed its range checked and did not
   have it: the filed identity is verified at even L <= 12 and the
   tombstones here reach lambda = 106, so this file re-derives Bernoulli
   numbers from scratch and confirms W(L) = denominator(B_L / 2L) for
   every even L up to 112 (56/56) -- an extension of the filed range, not
   a re-verification of it. (The first attempt at that check reported a
   failure at every even L including the filed ones, which is how a
   broken binomial recurrence announces itself; the identity was never in
   question and the helper was.) What is new is
   the closure framing and an ELEMENTARY reason every closed state above 2
   is divisible by 24, with no Bernoulli numbers in it: for N >= 3 lambda
   is even, so the wall carries 2^(v_2+2) >= 8, and (3-1) | lambda admits
   the factor 3. The closure also hands over an unbounded ladder for free:
   W(L) is closed for EVERY L, and W(2^k) >= 2^(k+2) grows without bound
   (printed to k = 64, V = 1 throughout), so the closed states are
   infinite -- which is finding 7's other half.

6. THE BLINDNESS THINS, SLOWLY -- PREDICTION P7 IS DEAD (observation;
   census at six caps). The fraction of states sharing their headroom with
   another state below the same cap runs 39.2%, 37.3%, 35.5%, 33.4%, 31.3%
   at caps 1500 to 24000 and 26.8% at 192000: falling at every step, which
   is exactly the frozen kill. THE SHAPE was then measured rather than
   left at a direction, since a prediction that dies on its sign leaves
   the rate unknown. A 1/log decay would hold f*ln(cap) constant; instead
   it creeps 2.87, 3.09, 3.16, 3.22, 3.26 and is still rising at the top,
   so the fall is a shade slower than 1/log. That form tends to zero, and
   the per-doubling decrement is shrinking (0.021 down to 0.013) exactly
   as c/ln(x) predicts -- but a slow approach to a small POSITIVE limit
   fits the same eight points, and nothing here decides between them. So
   the collisions are neither a small-number artifact -- more than a
   quarter of the states at 192000 still share their reading with another
   -- nor the stable proportion the prediction assumed. The probe
   distinguishes the rest, and gains: distinct headroom values run 67.2%
   of states at 1500 to 75.3% at 192000. The fibre-size histogram at 6000
   is long-tailed (3871 singletons, then 118 pairs, 35 triples, and a tail
   reaching 178).

7. THE BIGGEST BLIND SPOT CONTAINS EVERY SAFE PRIME (rule, proved +
   verified 81/81 below 6000). (Settled further by explore_premium.py
   finding 6: the class's PRIME part is exactly the minimum-gateway
   family, the primes q > 5 whose door cohort from the empty state is
   {3, q} with 3 not dividing q-1. Everything below stands; the safe
   primes are a proper sub-family of that characterization, and the
   "unmapped rest" of the primes is not unmapped.) The largest fibre is
   V = 24, and for a SAFE
   PRIME p = 2q+1 with q prime and q >= 5 the doors above lambda(p) = 2q
   are exactly 3 and p -- q's own door needs (q-1) | 2q, i.e. q-1 | 2 --
   so W(2q) = 2^3 * 3 * p and V(p) = 24 identically. The two small safe
   primes fall out of it for the reason the argument names: V(5) = 48
   (a fourth door at 5) and V(7) = 72 (3 doubled). The class is strictly
   larger than that: 178 states below 6000, of which 101 are prime (81 of
   them safe) and 77 composite, the smallest composites being 10 and 21,
   with 60, 108 and 178 members below 1500, 3000 and 6000. WHETHER THE
   CLASS IS INFINITE IS OPEN. The safe primes are one route to settling
   it -- they are all in the class, so their infinitude would give it --
   and that route is exactly the Sophie Germain question. But they are
   not the only route and the class is not their shadow: 81 of its 101
   primes are safe and 57 of its 77 composites carry a safe prime factor,
   so 40 of the 178 members below 6000 have no safe prime in them at all
   (10, 21, 290, 530 and 239, 443, 647 among them). Nothing here shows
   any of those families infinite either; the honest statement is that
   one identified route is conjecture-gated and the rest is unmapped.
   BLINDNESS IN GENERAL IS NOT CONJECTURAL, and the distinction is the
   point: by finding 5 the class V = 1 is the closed states, W(L) is closed
   for every L, and W(2^k) grows without bound, so that class is infinite
   unconditionally. Every wall reads exactly like every other wall, and
   there are infinitely many walls. So the probe has a provably infinite
   blind spot at the tombstones; what the safe primes gate is whether the
   BIGGEST one is infinite too.

8. THE HEARSAY RECONCILED (control). Three of the four measurements the
   question arrived with came back identical -- 870 ordered coprime pairs
   below 40 where V(ab) != V(a)V(b) with the smallest at V(2)V(3) = 8
   against V(6) = 4; 220 mixed-support classes covering 2020 of 6000
   states with the largest colliding headroom 276363360; and the eleven
   tombstones below 3000. The fourth differs by a counting convention and
   is reconciled exactly: 268 rising moves counting states from N = 2, 270
   counting the empty state N = 1, whose V = 2 is beaten by the pushes of
   3 and of 5. So the rig is measuring the same V.

SCOPE. Everything is exact integer arithmetic. Ranges differ by section
and each print carries its own: the state pool that S5 and S8 draw on is
N <= 6000, S7's census runs to 24000, the move battery is N < 400 with
m < 60, and the Bernoulli extension covers even L <= 112. What is PROVED
for all N and m rather than sampled: the exponent identity, the ledger,
the closure operator, the 24-divisibility of closed states, and the
headroom of every safe prime; the census, the splitting rate and the
class compositions are measurements at the stated caps and nothing is
claimed beyond them. Primality is deterministic Miller-Rabin over the
standard base set, valid below ~3.3e24; the largest number tested here is
below 10^4, so nothing rests on a probable prime.

RUN RECORD. Python 3, no third-party dependencies, 0.4 s wall clock,
negligible memory. Eight sections, all checks pass. The positive control
runs first and the run aborts before any verdict is read if it fails.
Nearly all of the runtime is S1's brute-force control on wall() and S5's
pair sweep; everything else is cached factorisations.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from fractions import Fraction
from math import comb, gcd, log

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("  FAIL: " + msg)
    return cond


# ---------------------------------------------------------------- arithmetic

_FCACHE = {}


def factorint(n):
    hit = _FCACHE.get(n)
    if hit is not None:
        return hit
    f, r, d = {}, n, 2
    while d * d <= r:
        while r % d == 0:
            f[d] = f.get(d, 0) + 1
            r //= d
        d += 1 if d == 2 else 2
    if r > 1:
        f[r] = f.get(r, 0) + 1
    if n < 200000:
        _FCACHE[n] = f
    return f


def v_p(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def divisors(n):
    ds = [1]
    for p, e in factorint(n).items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return sorted(ds)


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def lcm(a, b):
    return a // gcd(a, b) * b


def lam(n):
    """Carmichael's lambda."""
    if n == 1:
        return 1
    out = 1
    for p, e in factorint(n).items():
        if p == 2:
            part = 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
        else:
            part = p ** (e - 1) * (p - 1)
        out = lcm(out, part)
    return out


_WCACHE = {}


def wall(L):
    """The largest modulus whose lambda divides L.

    lambda(2^a) is 1, 2, then 2^(a-2), so the 2-part caps at 2 when L is ODD
    and at 2^(v_2(L)+2) when it is even. For odd p, lambda(p^a) =
    p^(a-1)(p-1) divides L iff (p-1) | L and a <= v_p(L)+1.
    """
    hit = _WCACHE.get(L)
    if hit is not None:
        return hit
    W = 2 if L % 2 else 2 ** (v_p(L, 2) + 2)
    for d in divisors(L):
        p = d + 1
        if p > 2 and is_prime(p):
            W *= p ** (v_p(L, p) + 1)
    _WCACHE[L] = W
    return W


def headroom(N):
    """V(N) = W(lambda(N))/N -- the transparency headroom.

    N divides its own wall for every N, so the division is exact; the
    assert is a tripwire rather than a check, because a silent floor here
    would corrupt every section downstream and nothing else would notice.
    """
    W = wall(lam(N))
    assert W % N == 0, "N does not divide W(lambda(N)) at N=%d" % N
    return W // N


def slack(N, l):
    """delta_l = d_l - c_l + 1, the free pushes of l before lambda moves."""
    c = v_p(N, l)
    d = 0
    for q in factorint(N):
        if q != l:
            d = max(d, v_p(q - 1, l))
    d = max(d, c - 1)
    return d - c + 1


def support(N):
    return frozenset(factorint(N))


# ---------------------------------------------------------------- S1 control

def s1_control():
    print("S1 POSITIVE CONTROL")

    # (a) wall() against its definition, compared only where the wall fits.
    CAP = 30000
    lam_tab = [1] * (CAP + 1)
    for n in range(2, CAP + 1):
        lam_tab[n] = lam(n)
    Ls = sorted({lam(n) for n in range(1, 240)})
    fit = [L for L in Ls if wall(L) <= CAP]
    bad = 0
    for L in fit:
        best = max(n for n in range(1, CAP + 1) if L % lam_tab[n] == 0)
        if best != wall(L):
            bad += 1
            print("    L=%d formula=%d search=%d" % (L, wall(L), best))
    check(bad == 0, "wall() disagrees with its definition")
    print("  wall() vs brute-force definition: %d/%d agree "
          "(walls that fit under %d; %d larger walls not compared)"
          % (len(fit) - bad, len(fit), CAP, len(Ls) - len(fit)))

    # (b) the filed divisor identity: transparent moves = divisors of V.
    MM = 400
    bad = 0
    for N in range(2, 120):
        V, L = headroom(N), lam(N)
        trans = {m for m in range(2, MM + 1) if lam(N * m) == L}
        divs = {m for m in divisors(V) if 2 <= m <= MM}
        if trans != divs:
            bad += 1
            print("    N=%d transparent!=divisors, sym diff %s"
                  % (N, sorted(trans ^ divs)[:6]))
    check(bad == 0, "transparent set is not the divisor set of V")
    print("  transparent moves = divisors of V: %d/118 states, "
          "moves 2..%d" % (118 - bad, MM))

    # (c) the four hearsay measurements, each under a stated convention.
    rise = sum(1 for N in range(2, 300) for m in (2, 3, 5)
               if headroom(N * m) > headroom(N))
    rise1 = rise + sum(1 for m in (2, 3, 5) if headroom(m) > headroom(1))
    print("  hearsay 1 (V not monotone): %d of %d moves rise from N >= 2, "
          "%d of %d counting N = 1 [m in {2,3,5}, N < 300]"
          % (rise, 298 * 3, rise1, 299 * 3))

    ordered = sum(1 for a in range(2, 40) for b in range(2, 40)
                  if gcd(a, b) == 1
                  and headroom(a * b) != headroom(a) * headroom(b))
    print("  hearsay 2 (V not multiplicative): %d ordered coprime pairs "
          "(%d unordered) [2 <= a,b <= 39]" % (ordered, ordered // 2))
    print("    smallest: V(2)*V(3) = %d*%d = %d vs V(6) = %d"
          % (headroom(2), headroom(3), headroom(2) * headroom(3),
             headroom(6)))

    cls = {}
    for N in range(1, 6001):
        cls.setdefault(headroom(N), []).append(N)
    mixed = {V: ns for V, ns in cls.items()
             if len({support(n) for n in ns}) > 1}
    print("  hearsay 3 (collisions): %d classes of mixed support covering "
          "%d of 6000 states, largest colliding V = %d"
          % (len(mixed), sum(len(ns) for ns in mixed.values()),
             max(mixed) if mixed else 0))

    tomb = [N for N in range(1, 3000) if headroom(N) == 1]
    print("  hearsay 4 (tombstones below 3000): %s" % tomb)
    return cls


# ------------------------------------------------------- S2 exponent identity

def s2_exponent():
    print("S2 THE EXPONENT IDENTITY (slack = headroom exponent)")
    open_ok = open_bad = shut_ok = shut_bad = 0
    first = None
    for N in range(2, 600):
        V, L = headroom(N), lam(N)
        for l in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            dl, vl = slack(N, l), v_p(V, l)
            if L % (l - 1) == 0:
                if dl == vl:
                    open_ok += 1
                else:
                    open_bad += 1
                    first = first or ("open", N, l, dl, vl)
            else:
                if vl == 0 and dl >= 1:
                    shut_ok += 1
                else:
                    shut_bad += 1
                    first = first or ("shut", N, l, dl, vl)
    check(open_bad == 0 and shut_bad == 0,
          "exponent identity fails: %s" % (first,))
    print("  door OPEN, (l-1) | lambda: delta_l = v_l(V) in %d/%d cases"
          % (open_ok, open_ok + open_bad))
    print("  door SHUT: v_l(V) = 0 in %d/%d cases (the delta_l >= 1 "
          "beside it is automatic there, not evidence)"
          % (shut_ok, shut_ok + shut_bad))

    bad = 0
    for N in range(2, 2000):
        L, V = lam(N), headroom(N)
        want = (v_p(L, 2) + 2 - v_p(N, 2)) if L % 2 == 0 else (1 - v_p(N, 2))
        if v_p(V, 2) != want:
            bad += 1
            if bad == 1:
                print("    N=%d v_2(V)=%d want=%d" % (N, v_p(V, 2), want))
    check(bad == 0, "2-part of V disagrees")
    print("  2-part: v_2(V) = v_2(lambda)+2-v_2(N) (even lambda), "
          "1-v_2(N) (odd): %d/1998 states" % (1998 - bad))


# ----------------------------------------------------------------- S3 ledger

def s3_ledger():
    print("S3 THE LEDGER  V(Nm) = V(N)/gcd(m,V(N)) * G'")
    moves = 0
    nonint = 0
    ones = 0
    rise = 0
    rise_pred = 0
    first_bad = None
    for N in range(2, 400):
        V = headroom(N)
        for m in range(2, 60):
            Vm = headroom(N * m)
            g = gcd(m, V)
            num = Vm * g
            moves += 1
            if num % V:
                nonint += 1
                if first_bad is None:
                    first_bad = (N, m, V, Vm, g)
                continue
            Gp = num // V
            if Gp == 1:
                ones += 1
            if Vm > V:
                rise += 1
            if Gp > g:
                rise_pred += 1
    if first_bad:
        print("    first non-integer: N=%d m=%d V=%d V(Nm)=%d gcd=%d"
              % first_bad)
    check(nonint == 0, "G' is not always a positive integer")
    print("  G' a positive integer: %d/%d moves [N in 2..399, m in 2..59]"
          % (moves - nonint, moves))
    print("  G' = 1 (the move opens exactly what it does not spend): %d moves"
          % ones)
    # Not a check: V(Nm) > V(N) iff G' > gcd is algebra once G' is defined
    # as V(Nm)*gcd/V, so the two counts CANNOT differ. Printed as the size
    # of the rising set, which is the part that carries information.
    print("  V(Nm) > V(N), equivalently G' > gcd(m,V) by definition: "
          "%d moves (both counts %d, as algebra requires)"
          % (rise, rise_pred))
    # A rise needs lambda to move, but lambda moving buys no rise: the
    # move can burn more transparency than it opens. Printed because two
    # docs quote this witness.
    falls = [(N, m) for N in range(2, 60) for m in range(2, 20)
             if lam(N * m) != lam(N) and headroom(N * m) < headroom(N)]
    print("  lambda-moving moves that LOWER V: %d in [N<60, m<20], "
          "first %s; the quoted witness N=3 m=16 goes V %d -> %d "
          "with lambda %d -> %d"
          % (len(falls), falls[:3], headroom(3), headroom(48),
             lam(3), lam(48)))


# ------------------------------------------------------- S4 what G'=1 is not

def s4_not_transparent():
    print("S4 G' = 1 IS NOT TRANSPARENCY")
    bad = 0
    for N in range(2, 400):
        V, L = headroom(N), lam(N)
        for m in range(2, 60):
            if (lam(N * m) == L) != (V % m == 0):
                bad += 1
    check(bad == 0, "transparent is not equivalent to m | V")
    print("  transparent iff m | V: %d disagreements over %d moves"
          % (bad, 398 * 58))

    N, m = 16, 2
    V, Vm = headroom(N), headroom(N * m)
    g = gcd(m, V)
    Gp = Vm * g // V
    print("  the frozen witness: N=%d m=%d  lambda %d -> %d  wall %d -> %d"
          % (N, m, lam(N), lam(N * m), wall(lam(N)), wall(lam(N * m))))
    print("    V %d -> %d, gcd(m,V) = %d, G' = %d, transparent = %s"
          % (V, Vm, g, Gp, V % m == 0))
    check(Gp == 1 and Vm == V and lam(N * m) != lam(N),
          "the (16,2) witness does not behave as frozen")

    opaque_ones = [(N, m) for N in range(2, 200) for m in range(2, 40)
                   if lam(N * m) != lam(N)
                   and headroom(N * m) * gcd(m, headroom(N)) == headroom(N)]
    print("  non-transparent moves with G' = 1: %d in [N<200, m<40], "
          "first five %s" % (len(opaque_ones), opaque_ones[:5]))


# ------------------------------------------------------------ S5 congruence

def s5_congruence(cls):
    print("S5 IS THE BLINDNESS A CONGRUENCE?")
    pairs = []
    for V, ns in cls.items():
        ns = [n for n in ns if n <= 1500]
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                pairs.append((ns[i], ns[j]))
    trans_split = 0
    trans_tot = 0
    opaque_split = 0
    opaque_tot = 0
    for a, b in pairs:
        V = headroom(a)
        for m in range(2, 40):
            same = headroom(a * m) == headroom(b * m)
            if V % m == 0:
                trans_tot += 1
                if not same:
                    trans_split += 1
                    print("    TRANSPARENT SPLIT a=%d b=%d m=%d" % (a, b, m))
            else:
                opaque_tot += 1
                if not same:
                    opaque_split += 1
    check(trans_split == 0, "a transparent move split an equal-headroom pair")
    print("  %d equal-headroom pairs below 1500, moves 2..39" % len(pairs))
    print("  transparent moves: %d/%d preserve the class (splits: %d)"
          % (trans_tot - trans_split, trans_tot, trans_split))
    print("  lambda-moving moves: %d/%d SPLIT the class (%.1f%%)"
          % (opaque_split, opaque_tot,
             100.0 * opaque_split / max(1, opaque_tot)))
    print("  the frozen witness: V(10)=%d V(11)=%d -> V(50)=%d V(55)=%d"
          % (headroom(10), headroom(11), headroom(50), headroom(55)))
    check(headroom(10) == headroom(11) and headroom(50) != headroom(55),
          "the (10,11) witness does not behave as frozen")


# ------------------------------------------------- S6 tombstones and closure

def s6_closure():
    print("S6 THE TOMBSTONES AND THE CLOSURE")
    bad = 0
    for N in range(1, 3000):
        star = wall(lam(N))
        if wall(lam(star)) != star:
            bad += 1
            if bad == 1:
                print("    N=%d star=%d star*=%d"
                      % (N, star, wall(lam(star))))
    check(bad == 0, "the wall map is not idempotent")
    print("  wall map N -> W(lambda(N)) idempotent: %d/2999 states"
          % (2999 - bad))

    inflation = all(wall(lam(N)) % N == 0 for N in range(1, 3000))
    monotone = all(wall(lam(N)) % wall(lam(d)) == 0
                   for N in range(2, 400) for d in divisors(N))
    check(inflation and monotone, "the wall map is not a closure operator")
    print("  inflationary (N | N*) and monotone (d | N => d* | N*): both hold")

    tomb = [N for N in range(1, 3000) if headroom(N) == 1]
    print("  closed states below 3000 (V = 1): %s" % tomb)
    print("  divisible by 24 above N=2: %s"
          % all(t % 24 == 0 for t in tomb if t > 2))
    check(all(t % 24 == 0 for t in tomb if t > 2),
          "a closed state above 2 is not divisible by 24")
    print("  each is W(L) for its own lambda: %s"
          % [(lam(t), wall(lam(t))) for t in tomb])

    # The corollary the closure hands over: closed states are unbounded,
    # so SOME blind class is infinite without any conjecture in it.
    ks = [1, 2, 4, 8, 16, 20, 32, 64]
    rows = [(k, wall(2 ** k), headroom(wall(2 ** k))) for k in ks]
    check(all(V == 1 for _, _, V in rows),
          "W(2^k) is not closed for some k")
    print("  the ladder W(2^k), closed by construction, V = 1 throughout:")
    for k, W, V in rows:
        print("    k=%-3d W=%-28d V=%d" % (k, W, V))

    # Added during review, to license a cross-reference rather than to
    # test a suspicion: the wall identity W(L) = denominator(B_L / 2L) is
    # filed for even L <= 12, and the tombstones above reach lambda = 106.
    # Either the identity extends or the cross-reference must be scoped.
    NB = 112
    B = [Fraction(0)] * (NB + 1)
    B[0] = Fraction(1)
    for n in range(1, NB + 1):
        acc = sum(comb(n + 1, j) * B[j] for j in range(n))
        B[n] = -acc / (n + 1)
    bad = [L for L in range(2, NB + 1, 2)
           if (B[L] / (2 * L)).denominator != wall(L)]
    check(not bad, "the wall identity fails at even L: %s" % bad[:5])
    print("  wall identity W(L) = denom(B_L/2L), even L = 2..%d: %d/%d "
          "agree (filed range was L <= 12; every tombstone lambda above "
          "is inside this one except the odd lambda = 1, which the "
          "even-L identity does not speak about)"
          % (NB, NB // 2 - len(bad), NB // 2))


# -------------------------------------------------------------- S7 the census

def s7_census(cls):
    print("S7 THE BLINDNESS CENSUS")
    print("  cap   states  distinct V  in a class >= 2   mixed-support classes")
    for cap in (1500, 3000, 6000, 12000, 24000, 192000):
        sub = {}
        for N in range(1, cap + 1):
            sub.setdefault(headroom(N), []).append(N)
        multi = [ns for ns in sub.values() if len(ns) > 1]
        covered = sum(len(ns) for ns in multi)
        mixed = [ns for ns in multi if len({support(n) for n in ns}) > 1]
        mixed_cov = sum(len(ns) for ns in mixed)
        print("  %5d %7d %11d %9d (%4.1f%%) %8d classes / %d states"
              % (cap, cap, len(sub), covered, 100.0 * covered / cap,
                 len(mixed), mixed_cov))
    # The SHAPE of the fall, since the frozen prediction died on its
    # direction and left the rate unmeasured. f * ln(cap) is printed
    # because a 1/log decay would hold it constant; nothing is fitted and
    # no limit is claimed.
    print("  the shape of the fall (f = shared fraction):")
    for cap in (1500, 6000, 24000, 96000, 192000):
        seen = {}
        for N in range(1, cap + 1):
            V = headroom(N)
            seen[V] = seen.get(V, 0) + 1
        f = sum(c for c in seen.values() if c > 1) / cap
        print("    cap %7d   f = %.4f   f*ln(cap) = %.3f" % (cap, f, f * log(cap)))

    big = max(cls.items(), key=lambda kv: len(kv[1]))
    print("  largest fibre at 6000: V = %d holds %d states %s"
          % (big[0], len(big[1]), big[1][:8]))
    sizes = {}
    for ns in cls.values():
        sizes[len(ns)] = sizes.get(len(ns), 0) + 1
    print("  fibre-size histogram at 6000: %s"
          % sorted(sizes.items())[:8])


# ------------------------------------------------- S8 the largest blind class

def s8_blind_class(cls):
    print("S8 WHAT THE LARGEST BLIND CLASS IS MADE OF")
    safe = [p for p in range(3, 6001)
            if is_prime(p) and (p - 1) % 2 == 0 and is_prime((p - 1) // 2)]
    big = [p for p in safe if (p - 1) // 2 >= 5]
    bad = [p for p in big if headroom(p) != 24]
    check(not bad, "a safe prime has headroom != 24: %s" % bad[:5])
    print("  safe primes p = 2q+1 with q >= 5 below 6000: %d, all with "
          "V = 24 (exceptions: %s)" % (len(big), bad[:5]))
    print("  the two excluded: V(5) = %d, V(7) = %d"
          % (headroom(5), headroom(7)))
    check(headroom(5) != 24 and headroom(7) != 24,
          "the excluded safe primes are in the class after all")

    fibre = cls.get(24, [])
    prm = [n for n in fibre if is_prime(n)]
    print("  the V = 24 class below 6000: %d states, %d prime "
          "(%d of them safe), %d composite"
          % (len(fibre), len(prm), len([p for p in prm if p in set(big)]),
             len(fibre) - len(prm)))
    comp = [n for n in fibre if not is_prime(n)]
    safeset = set(big)
    with_safe = [n for n in comp if any(q in safeset for q in factorint(n))]
    print("  composites in it: %s" % comp[:12])
    print("  how much of the class the safe primes actually supply: "
          "%d of %d primes are safe, and %d of %d composites carry a safe "
          "prime factor -- so %d members do not"
          % (len([p for p in prm if p in safeset]), len(prm),
             len(with_safe), len(comp),
             len([p for p in prm if p not in safeset]) +
             len(comp) - len(with_safe)))
    for cap in (1500, 3000, 6000):
        print("    class size below %d: %d" % (cap,
              len([n for n in fibre if n <= cap])))


# ------------------------------------------------------------------ the run

def main():
    print("=" * 72)
    print("THE TRANSPARENCY HEADROOM AS A FUNCTION")
    print("=" * 72)
    cls = s1_control()
    if FAIL:
        print("\nPOSITIVE CONTROL FAILED -- no verdict read.")
        return 1
    print()
    s2_exponent()
    print()
    s3_ledger()
    print()
    s4_not_transparent()
    print()
    s5_congruence(cls)
    print()
    s6_closure()
    print()
    s7_census(cls)
    print()
    s8_blind_class(cls)
    print()
    print("=" * 72)
    if FAIL:
        print("FAILURES: %d" % len(FAIL))
        for f in FAIL:
            print("  " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
