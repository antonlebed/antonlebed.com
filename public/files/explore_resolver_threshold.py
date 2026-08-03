"""explore_resolver_threshold.py — how cheaply a blind pair resolves, and
what a watcher's position costs against a chooser's.

QUESTION. Two states with the same transparency headroom are one state to
the probe that reads it. Multiplying both by some d can tell them apart,
and no pair is blind under EVERY multiplier -- the constructed witness is
a prime congruent to 1 modulo the lcm of the two Carmichael values, which
is astronomically larger than the multipliers that are observed to work.
So the open object is not WHETHER a pair resolves but the THRESHOLD: the
least d > 1 with V(N_1 d) != V(N_2 d), and the structure of the whole
resolving set R = {d : V(N_1 d) != V(N_2 d)}. Is the threshold bounded?
Is it a function of what the probe can SEE? Does R have order structure?
And the sharper half: a probe that CHOOSES its multiplier always wins,
while a WATCHER takes the move it is given and reads inside it -- which
moves keep a pair blind at every internal reading, and is that class
describable?

THE HAND-DERIVATION THIS RIG IS BUILT TO CHECK (done before any code, and
its two conclusions are CONTROLS here, not findings).

  (A) THE RESOLUTION CRITERION. V(N_i d) = W(lambda(N_i d))/(N_i d), and a
  blind pair satisfies W(lambda_i) = V*N_i with one shared V. So

      V(N_1 d) = V(N_2 d)  <=>  gain_1(d) = gain_2(d),
      gain_i(d) := W(lambda(N_i d)) / W(lambda_i).

  The d cancels and the unpaid part d/gcd(d,V) is the same for both states
  because the reading is the same, so resolution is EXACTLY a disagreement
  of wall gains -- equivalently of premiums -- for every d, with no
  coprimality hypothesis. The mechanism was known on fresh imports; the
  cancellation makes it general.

  (B) THE TRANSPARENCY FLOOR, AND IT IS READABLE. gain_i(d) = 1 iff
  W(lambda(N_i d)) = W(lambda_i) iff N_i d divides W(lambda_i) = V*N_i iff
  d | V. Both directions in one line. The two states share V, so either
  BOTH gains are 1 or NEITHER: every divisor of V fails to resolve. Hence
  every resolver is a non-divisor of V and

      least resolver >= floor(V) := min over primes q of q^(v_q(V)+1),

  the least non-divisor of V, which is always a prime power (if the least
  non-divisor were p^a*m with m > 1 coprime to p, then p^a and m are both
  smaller, both divide V, and being coprime their product would too). The
  floor is a function of the READING ALONE: the probe can compute its own
  cheapest conceivable resolver without knowing the state. V = 24 gives 5.

  (C) THE LAMBDA-FIBRE REDUCTION. For d coprime to N_1 N_2, lambda(N_i d)
  = lcm(lambda_i, lambda(d)), so gain_i sees d only through lambda(d) and R
  is a union of lambda-fibres there. Off the coprime case the seated depth
  v_l(N_i) enters, and that is the only way two states at the same prime of
  the move can part.

  (D) THE WATCHER, EXACTLY. The depth ladder collapses (the readings inside
  a move are exactly {V(N_i d) : d | m}), so a watcher wins on m iff some
  DIVISOR of m resolves. The fully-blind moves are the m whose entire
  divisor set misses R -- a divisor-closed family which by (B) contains
  every divisor of V. Every blind pair therefore has at least tau(V) - 1
  moves -- the divisors above 1 -- that keep it blind at every internal
  reading, with certainty, and a chooser never picks one.

PREDICTIONS, frozen before the engine.

  1. (derived, control) Resolution and gain-disagreement coincide with no
     exceptions; gain = 1 and d | V coincide with no exceptions. A single
     counterexample to either kills the derivation and the run aborts
     before any verdict is read.
  2. (derived) No resolver divides V, so no pair's least resolver falls
     below its floor. 0 violations.
  3. (open) The floor is ATTAINED often: the least resolver EQUALS
     floor(V) for a majority -- guessed above 70% -- of the pairs in the
     standard pool. This is a guess and not a derivation; the derivation
     gives the inequality only.
  4. (open) The threshold is UNBOUNDED. Blind classes whose reading is
     divisible by every small number should exist, and their floors then
     grow without bound. Kill-shape as an observable: if the largest floor
     over populated blind classes does not move as the enumeration
     deepens, the unboundedness story is not exhibited at this scale.
  5. (open) R is neither an up-set for divisibility nor closed under
     multiplication -- both should have counterexamples, because a second
     factor can re-merge two states the first split.
  6. (open) The fully-blind family is STRICTLY larger than the divisors of
     V for at least some pairs, but not by much: the certainty half is the
     divisors, the rest is coincidence.

  A SECOND FREEZE, written after the first run and only for the question
  that run raised. The floor is a function of the reading and is attained
  far more often than guessed, which asks whether the THRESHOLD itself is
  readable -- whether the least resolver depends on the pair at all, or
  only on the V both states show.

  7. (open) It is NOT a function of the reading: two different pairs drawn
     from the SAME blind class should have different least resolvers, and
     a class with three members below the pool cap should already show it.
     Kill-shape as an observable: every class in the pool reports one
     least resolver across all its pairs.

FINDINGS.

  1. THE RESOLUTION CRITERION AND THE TRANSPARENCY FLOOR both hold with no
     exceptions (theorem, proved and then checked: 5664 (pair, move) cases
     for the criterion, 23482 (state, move) cases for the floor identity).
     A move is invisible to the probe -- gain 1 at both states -- exactly
     when it divides the shared reading. The FORWARD half was already
     argued (a transparent move spends the same divisor at both states and
     opens nothing); what is new is the CONVERSE, and the converse is the
     load-bearing half: every non-divisor of the reading moves the wall at
     BOTH states, so the resolving set is confined to the non-divisors from
     the outset and the floor below exists at all. It also identifies two
     descriptions the corpus had been using as if interchangeable: the
     transparent moves are exactly the wall-freezing moves and exactly the
     lambda-freezing moves, since N d | W(lambda(N)) forces lambda(Nd) =
     lambda(N) and conversely.

  2. THE THRESHOLD IS FLOORED BY THE READING, AND THE FLOOR IS NEARLY
     ALWAYS THE ANSWER (theorem for the bound, measurement for the rate).
     No pair's least resolver falls below floor(V) = min_q q^(v_q(V)+1),
     and 90 of the 96 pairs -- 93.8% -- resolve at exactly that value, far
     above the 70% guessed at the freeze. Nothing is censored: every pair
     in the pool resolves under 200, and the floors present run 2, 3, 4, 5,
     7, 8, 9, 11. The six misses are small and all land on 3, 4 or 7. So
     the probe can compute a sharp lower bound on its own cheapest
     resolving multiplier from its reading alone, without knowing the state
     -- and that bound is usually the exact price.

  3. THE THRESHOLD GROWS WITH THE READING, AND ITS UNBOUNDEDNESS IS OPEN
     -- reduced, not settled (observation; floors 5, 7, 11, 17 realised by
     actual pairs). Prediction 4 guessed "unbounded" and the run does NOT
     establish it: exhibiting floors to 17 shows the threshold exceeds
     anything the standard pool suggested, not that it exceeds every bound.
     What the run does is REDUCE the question. Because floor(V) grows with
     the divisibility of V, a blind class with a very divisible
     reading forces a large threshold, and the walls are exactly the supply
     of divisible readings -- so "is the threshold unbounded" becomes "do
     arbitrarily divisible readings host blind PAIRS", and that is a
     question about class occupancy rather than about resolution. It is not
     automatic: two of the ten targets have no pair at all in range.
     Enumerating a class EXACTLY -- V(N) = V_0 means
     N = W(lambda(N))/V_0, so running lambda over a range finds every
     member whose lambda is in it -- gives blind pairs at V = W(2), W(4),
     W(12), W(60), W(180), the last three carrying floor 17 on states of up
     to eight digits. In EVERY ladder case the least resolver equals the
     floor. Two of the ten targets have no pair with lambda <= 600 and are
     reported as such rather than dropped, so the ladder's reach is a
     property of the enumeration and not of the classes. The frozen
     kill-shape is EVALUATED rather than assumed: the largest floor
     carrying a pair is 11 at lambda <= 150, 17 at 300, and 17 again at
     600. It moves, so the observable did not fire -- but it stalled on the
     last doubling, which is weak evidence and is why finding 3 is a
     reduction and not a verdict. (Settled since, in reach though not in
     the tail, by explore_proth_window.py: every member's lambda is a
     multiple of an explicit base, the base-multiple sweep reaches
     lambda in the billions, occupancy is dense -- membership above 80
     percent of base multiples, every target populated by k <= 6 -- and
     designed readings host pairs at floors 47 and 81, each attained.
     The stall here was the flat sweep's, not the classes'.)

  4. THE THRESHOLD IS NOT ITSELF READABLE (observation; 52 classes with
     three or more members below 1500). 34 of them carry more than one
     least resolver across their pairs -- the class of the closed states,
     V = 1, already resolves at 2, 3 and 4 depending on which two members
     are compared. So the reading fixes the FLOOR exactly and the price
     only usually: what the probe cannot compute is which of its blind
     partners it is being compared against.

  5. THE LEAST RESOLVER IS ALWAYS A PRIME POWER (observation; 4498 of 4498
     pair comparisons, of which 1011 land strictly above the floor, so the
     count is not the floor's own prime-power shape read back). The natural
     mechanism for it is DEAD: a least resolver that is not a prime power
     would split into two coprime non-resolvers, so the observation would
     follow if the non-resolvers were closed under coprime products -- and
     they are not, 22 of 944 unordered tests failing, N = 16 and N = 32 staying
     blind under 4 and under 7 and splitting at 28. That is the primes of a
     move failing to decouple, seen from the blindness side. The
     observation stands and its proof is open. (Settled since, by
     explore_proth_window.py: REFUTED past the pool -- the pair
     (2^11, 2^12), blind at V = 65535, keeps every d <= 27 blind and
     splits first at 28 = 2^2 * 7, the door 12289 = 3 * 2^12 + 1; the
     within-pool count stands as measured, a cap artifact.)

  6. THE RESOLVING SET IS A UNION OF LAMBDA-FIBRES AND NOTHING TIDIER
     (theorem for the fibres, 1533/1533; measurement for the rest). Two
     multipliers coprime to both states with the same lambda resolve or
     fail together. But R is not an up-set -- 138 of 5964 (resolver,
     cofactor) tests re-merge the pair -- and not closed under
     multiplication, 45 of 1434 unordered resolver pairs. The first witness
     of both is the pair N = 9, N = 513, which splits at 3 and at 19 and is
     blind at 57. The product tests are counted once per UNORDERED pair
     because a*b is symmetric, which is the convention the composite move's
     symmetric sections use; the up-set test is not symmetric and keeps its
     (resolver, cofactor) orientation.

  7. THE WATCHER/CHOOSER GAP, STATED EXACTLY. A watcher wins on m iff some
     DIVISOR of m resolves, so the moves that keep a pair blind at every
     internal reading are the m whose whole divisor set misses R. That
     family always contains the divisors of V, which are blind by finding
     1 -- so every blind pair has at least tau(V) - 1 moves it survives
     with CERTAINTY (the divisors above 1), and a chooser never picks one. Over the pool a watcher is
     told the pair apart on 75.1% of the moves 2..60 while a chooser wins
     on every pair; of the 1411 fully-blind moves 1074 are divisors of the
     reading, and the family is strictly larger for 67 of the 96 pairs
     (N = 3 against N = 30 at V = 8 survives 23, 46, 47 and 59, none of
     them a divisor). So the gap decomposes: a guaranteed part the reading
     names in advance, and a coincidental part it does not.

  8. THE STITCH: slow motion IS the failure of R to be an up-set. The
     measured worth of watching inside a move -- pairs blind across a whole
     move that some intermediate reading splits -- is by finding 7 exactly
     the case of a resolver d whose multiple dk is not a resolver. It is one
     PHENOMENON with two measurements, not one number: the slow-motion rate
     counts blind-pair-and-move cases over the composite moves of its own
     battery, this counts (resolver, cofactor) tests over the moves to 60,
     and the two denominators are different objects. What they share is the
     witness -- the pair N = 9 and N = 513 under the move 57, which the
     slow-motion rate quotes and which is also the first the up-set test
     finds.

DESIGN. Six sections.

  S1 POSITIVE CONTROL, run first and aborting the run on failure: the
  criterion (A) and the floor identity (B) checked against the direct
  readings over the pair pool and a wide (state, move) battery, plus the
  factorisation layer of S3 checked against the ordinary integer path.

  S2 THE FLOOR. For every blind pair in the pool: the least resolver by
  brute force, floor(V) from the reading, the violation count (must be
  zero), the attainment rate, and the pairs whose least resolver is
  censored by the search cap, which are reported rather than dropped.

  S2b IS THE THRESHOLD READABLE? Every pair inside a class of three or
  more members, so that one reading is compared against several pairs.
  This section answers the question the first run raised and its
  prediction was frozen separately, after that run and before it.

  S3 THE LADDER. The members of a blind class are enumerated EXACTLY
  rather than searched for: V(N) = V_0 says N = W(lambda(N))/V_0, so
  running lambda over a range and keeping W(L)/V_0 whenever it reads back
  as V_0 finds every member whose lambda is in range. The class V_0 =
  W(L_0) is the natural supply of divisible readings. States here are far
  too large to factor, so lambda, the wall and the reading are computed
  from factorisations carried as exponent maps.

  S4 THE RESOLVING SET. Its order structure: up-sets, products, and the
  lambda-fibre reduction (C) as a check rather than a measurement.

  S5 THE WATCHER. The fully-blind moves against the divisors of V, and the
  chooser/watcher gap stated as two rates over the same move battery.

SCOPE. Exact integer arithmetic throughout. The pair pool is the standard
one -- one representative pair per headroom class below 1500, the two
smallest members -- so the threshold is measured on the same pool the
no-permanent-blindness result was proved over. S2b is the ONE section that
leaves that pool: it needs several pairs per reading, so it runs every pair
inside every class of three or more members below the same cap, and its
counts are therefore not comparable with the other sections'. The
brute-force resolver
search runs to 200, and pairs beyond it are counted as censored, never as
resolved. The ladder enumerates lambda to 600, which is complete for the
members of a class whose lambda lies in that range and says nothing about
members above it. Primality is deterministic Miller-Rabin over the
standard base set. What is PROVED for all pairs rather than sampled: the
resolution criterion, the floor identity and the floor bound, the
lambda-fibre reduction, and the containment of the divisors of V in the
fully-blind family. Attainment rates, the reach of the ladder and the
structure counts are measurements at the stated caps.

RUN RECORD. Python 3, no third-party dependencies, 0.3 s wall clock, peak
working set 18.1 MB under the memory watchdog. Six sections, all checks
pass. The positive control runs first and the run aborts before any verdict
is read if it fails. The floor identity, the pair count, the violation
count and the attainment rate were additionally reproduced by an
independent implementation sharing no code with this one, whose wall was
itself checked against a brute-force search for the largest modulus of a
given Carmichael value.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import gcd

from explore_premium import (divisors, doors, factorint, headroom, is_prime,
                             lam, lcm, two_part, v_p, wall)
from explore_composite_move import blind_pairs

FAIL = []

POOL_CAP = 1500          # the standard blind-pair pool
SEARCH_CAP = 200         # brute-force reach for a least resolver
LADDER_LAM = 600         # lambda range the class enumeration is complete for


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("  FAIL: " + msg)
    return cond


# ------------------------------------------------------- the base quantities

def gain(N, d):
    """W(lambda(Nd)) / W(lambda(N)) -- the wall gain of the move d."""
    return wall(lam(N * d)) // wall(lam(N))


def floor_of(V):
    """The least non-divisor of V, which is the floor on any resolver.

    Always a prime power, so it is the least q^(v_q(V)+1) over primes q;
    the search may stop at the first prime that does not divide V, since
    that prime itself is a candidate and every later one is larger.
    """
    best = None
    q = 2
    while True:
        cand = q ** (v_p(V, q) + 1)
        if best is None or cand < best:
            best = cand
        if V % q:
            return best
        q += 1
        while not is_prime(q):
            q += 1


def least_resolver(N1, N2, cap=SEARCH_CAP):
    """The least d > 1 telling the pair apart, or None if the cap hides it."""
    V1, V2 = headroom(N1), headroom(N2)
    assert V1 == V2, "not a blind pair"
    for d in range(2, cap + 1):
        if headroom(N1 * d) != headroom(N2 * d):
            return d
    return None


# ---------------------------------- an exponent-map layer for huge states

def fwall(L):
    """The factorisation of W(L) as an exponent map."""
    out = {2: two_part(L)}
    for p in doors(L):
        if p > 2:
            out[p] = v_p(L, p) + 1
    return out


def flam(f):
    """lambda of a state given as an exponent map."""
    out = 1
    for p, e in f.items():
        if e == 0:
            continue
        if p == 2:
            part = 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
        else:
            part = p ** (e - 1) * (p - 1)
        out = lcm(out, part)
    return out


def fmul(f, g):
    """The exponent map of a product."""
    out = dict(f)
    for p, e in g.items():
        out[p] = out.get(p, 0) + e
    return out


def fvalue(f):
    """The integer a map stands for."""
    out = 1
    for p, e in f.items():
        out *= p ** e
    return out


def fheadroom(f):
    """V(N) for N given as an exponent map, or None if the map is not a
    state's (a negative exponent, or a wall that does not contain N)."""
    if any(e < 0 for e in f.values()):
        return None
    W = wall(flam(f))
    N = fvalue(f)
    return W // N if W % N == 0 else None


def fdiv(f, g):
    """f / g as an exponent map, or None if g does not divide f."""
    out = dict(f)
    for p, e in g.items():
        out[p] = out.get(p, 0) - e
        if out[p] < 0:
            return None
    return {p: e for p, e in out.items() if e}


# ---------------------------------------------------------------- S1 control

def s1_control():
    print("S1 POSITIVE CONTROL")
    pairs = blind_pairs(POOL_CAP)
    bad_crit = 0
    for N1, N2 in pairs:
        for d in range(2, 61):
            resolves = headroom(N1 * d) != headroom(N2 * d)
            gains_differ = gain(N1, d) != gain(N2, d)
            if resolves != gains_differ:
                bad_crit += 1
    check(bad_crit == 0,
          "the resolution criterion fails on %d (pair, move) cases"
          % bad_crit)
    print("  the criterion: resolution and wall-gain disagreement coincide"
          " on all %d" % (len(pairs) * 59))
    print("    (pair, move) cases of the pool -- the unpaid part cancels"
          " because the reading is shared")

    bad_floor = 0
    n_cases = 0
    for N in range(2, 400):
        V = headroom(N)
        for d in range(2, 61):
            n_cases += 1
            if (gain(N, d) == 1) != (V % d == 0):
                bad_floor += 1
    check(bad_floor == 0,
          "gain = 1 and d | V part company on %d (state, move) cases"
          % bad_floor)
    print("  the floor identity: gain(N,d) = 1 exactly when d divides V(N),"
          " on all %d" % n_cases)
    print("    (state, move) cases -- so a transparent move is blind to the"
          " probe by ALGEBRA")

    # the layer is checked on the maps S3 actually reads -- quotients
    # W(L)/V_0, whose readings vary -- and not only on the walls, where
    # every reading is 1 by idempotence and the comparison is vacuous
    bad_layer = n_layer = 0
    for L in range(1, 200):
        f = fwall(L)
        n_layer += 1
        if fvalue(f) != wall(L) or flam(f) != lam(wall(L)):
            bad_layer += 1
        for V0 in (2, 24, 240, 504):
            q = fdiv(f, factorint(V0))
            if q is None or not q:
                continue
            n = fvalue(q)
            if n > 10 ** 6:
                continue
            n_layer += 1
            if flam(q) != lam(n) or fheadroom(q) != headroom(n):
                bad_layer += 1
    check(bad_layer == 0,
          "the exponent-map layer disagrees with the integer path in %d"
          " of %d cases" % (bad_layer, n_layer))
    print("  the exponent-map layer reproduces the integer path on %d cases"
          " -- the walls of every" % n_layer)
    print("    lambda < 200 and the quotients of them the class enumeration"
          " actually reads")
    print()


# ------------------------------------------------------------- S2 the floor

def s2_floor():
    print("S2 THE THRESHOLD AND ITS FLOOR")
    pairs = blind_pairs(POOL_CAP)
    violations = censored = attained = 0
    gaps = {}
    floors = {}
    for N1, N2 in pairs:
        V = headroom(N1)
        fl = floor_of(V)
        floors[fl] = floors.get(fl, 0) + 1
        d = least_resolver(N1, N2)
        if d is None:
            censored += 1
            continue
        if d < fl:
            violations += 1
            if violations == 1:
                print("  a resolver below the floor at N=%d, N=%d: d=%d < %d"
                      % (N1, N2, d, fl))
        if d == fl:
            attained += 1
        else:
            gaps[(fl, d)] = gaps.get((fl, d), 0) + 1
    n = len(pairs)
    check(violations == 0,
          "%d pairs have a resolver below the floor" % violations)
    print("  %d pairs; no resolver divides the reading, so none falls below"
          " the floor (0 violations)" % n)
    print("  the floor is ATTAINED by %d of the %d resolved pairs (%.1f%%)"
          % (attained, n - censored, 100.0 * attained / max(1, n - censored)))
    print("  %d pairs are censored by the search cap %d"
          % (censored, SEARCH_CAP))
    print("  floors present in the pool: %s"
          % ", ".join("%d (x%d)" % (f, c) for f, c in sorted(floors.items())))
    if gaps:
        print("  the pairs the floor MISSES, as (floor, least resolver):")
        for (fl, d), c in sorted(gaps.items())[:8]:
            print("    (%d, %d) x%d" % (fl, d, c))
    print()
    return floors


# ------------------------------------------- S2b is the threshold readable?

def s2b_readable():
    print("S2b IS THE THRESHOLD ITSELF A FUNCTION OF THE READING?")
    pool = {}
    for N in range(2, POOL_CAP):
        pool.setdefault(headroom(N), []).append(N)
    classes = {V: mem for V, mem in pool.items() if len(mem) >= 3}
    spread = one_valued = 0
    example = None
    powers = notpowers = 0
    above = [0]
    for V, mem in sorted(classes.items()):
        fl = floor_of(V)
        seen = set()
        for i in range(len(mem)):
            for j in range(i + 1, len(mem)):
                d = least_resolver(mem[i], mem[j])
                if d is not None:
                    seen.add(d)
                    if d > fl:
                        above[0] += 1
                    if len(factorint(d)) == 1:
                        powers += 1
                    else:
                        notpowers += 1
        if len(seen) > 1:
            spread += 1
            if example is None:
                example = (V, floor_of(V), sorted(seen), mem[:3])
        else:
            one_valued += 1
    print("  over the %d classes with three or more members below %d:"
          % (len(classes), POOL_CAP))
    print("    %d carry MORE THAN ONE least resolver across their pairs,"
          " %d carry exactly one" % (spread, one_valued))
    if example:
        print("    e.g. V=%d (floor %d) resolves at %s depending on WHICH"
              " two states are compared"
              % (example[0], example[1],
                 ", ".join(str(x) for x in example[2])))
        print("      (members: %s ...)"
              % ", ".join(str(x) for x in example[3]))
    print("  the least resolver is a prime power in %d of %d pair"
          " comparisons, composite in %d" % (powers, powers + notpowers,
                                             notpowers))
    print("    -- and %d of those comparisons land ABOVE the floor, so the"
          " count is not the floor's" % above[0])
    print()


# ------------------------------------------------------------ S3 the ladder

def class_members(V0, lam_cap=LADDER_LAM, want=2):
    """Every state of reading V0 whose lambda is at most lam_cap.

    V(N) = V0 says W(lambda(N)) = V0*N, so N = W(L)/V0 for L = lambda(N).
    Running L over the range and keeping the quotients that read back as V0
    is therefore an EXACT enumeration over that range, not a search.
    """
    fV0 = factorint(V0)
    out = []
    for L in range(1, lam_cap + 1):
        f = fdiv(fwall(L), fV0)
        if f is None:
            continue
        if flam(f) == L and fheadroom(f) == V0:
            out.append(f)
            if len(out) >= want:
                break
    return out


def s3_ladder():
    print("S3 IS THE THRESHOLD BOUNDED?")
    print("  a class's floor is min_q q^(v_q(V)+1), so a reading divisible"
          " by every small number")
    print("  forces a large threshold. the walls are the supply of"
          " divisible readings:")
    reached = []
    for L0 in [2, 4, 6, 12, 24, 60, 120, 180, 240, 420]:
        V0 = wall(L0)
        fl = floor_of(V0)
        mem = class_members(V0)
        if len(mem) < 2:
            print("    V = W(%d) = %d: floor %d, %d member(s) with lambda <="
                  " %d -- no pair" % (L0, V0, fl, len(mem), LADDER_LAM))
            continue
        f1, f2 = mem[0], mem[1]
        d = None
        for cand in range(2, SEARCH_CAP + 1):
            fc = factorint(cand)
            r1, r2 = fheadroom(fmul(f1, fc)), fheadroom(fmul(f2, fc))
            assert r1 is not None and r2 is not None, \
                "a ladder state stopped being a state at V=%d, d=%d" % (V0,
                                                                        cand)
            if r1 != r2:
                d = cand
                break
        reached.append((fl, d))
        print("    V = W(%d) = %d: floor %d, least resolver %s, states of"
              " %d and %d digits"
              % (L0, V0, fl, d if d else "> %d" % SEARCH_CAP,
                 len(str(fvalue(f1))), len(str(fvalue(f2)))))
    if reached:
        print("  largest floor exhibited by an actual blind pair: %d"
              % max(f for f, _ in reached))
    # the frozen kill-shape: does the largest exhibited floor MOVE as the
    # enumeration deepens, or is it a property of the shallow range?
    depths = []
    for cap in (150, 300, LADDER_LAM):
        best = 0
        for L0 in [2, 4, 6, 12, 24, 60, 120, 180, 240, 420]:
            V0 = wall(L0)
            if len(class_members(V0, lam_cap=cap)) >= 2:
                best = max(best, floor_of(V0))
        depths.append((cap, best))
    print("  the frozen kill-shape, evaluated: largest floor with a pair at"
          " lambda <= %s"
          % ", ".join("%d is %d" % (c, b) for c, b in depths))
    print("    -- it MOVES with the enumeration"
          if len({b for _, b in depths}) > 1 else
          "    -- it does NOT move, which is the kill the freeze named")
    print()
    return reached


# ------------------------------------------------- S4 the resolving set

def s4_structure():
    print("S4 THE SHAPE OF THE RESOLVING SET")
    pairs = blind_pairs(POOL_CAP)
    up_fail = up_test = mul_fail = mul_test = 0
    fibre_fail = fibre_test = 0
    blind_fail = blind_test = 0
    first_up = first_mul = first_blind = None
    for N1, N2 in pairs:
        R = set()
        for d in range(2, 61):
            if headroom(N1 * d) != headroom(N2 * d):
                R.add(d)
        # up-set: does a resolver stay a resolver under multiplication?
        for d in sorted(R):
            for k in range(2, 61 // max(d, 1) + 1):
                if d * k > 60:
                    break
                up_test += 1
                if d * k not in R:
                    up_fail += 1
                    if first_up is None:
                        first_up = (N1, N2, d, k)
        # multiplicative closure on pairs of resolvers
        for a in sorted(R):
            for b in sorted(R):
                if b < a or a * b > 60:      # symmetric: one test per pair
                    continue
                mul_test += 1
                if a * b not in R:
                    mul_fail += 1
                    if first_mul is None:
                        first_mul = (N1, N2, a, b)
        # coprime products of NON-resolvers: the candidate mechanism under
        # the prime-power observation, since a least resolver that is not a
        # prime power splits into two coprime non-resolvers
        # a*b is symmetric in a and b, so one test per UNORDERED pair
        for a in range(2, 61):
            if a in R:
                continue
            for b in range(a + 1, 61 // a + 1):
                if b in R or gcd(a, b) > 1 or a * b > 60:
                    continue
                blind_test += 1
                if a * b in R:
                    blind_fail += 1
                    if first_blind is None:
                        first_blind = (N1, N2, a, b)
        # the lambda-fibre reduction, on multipliers coprime to both states
        by_lam = {}
        for d in range(2, 61):
            if gcd(d, N1 * N2) > 1:
                continue
            by_lam.setdefault(lam(d), []).append(d in R)
        for L, verdicts in by_lam.items():
            fibre_test += 1
            if len(set(verdicts)) > 1:
                fibre_fail += 1
    check(fibre_fail == 0,
          "the lambda-fibre reduction fails on %d fibres" % fibre_fail)
    print("  the lambda-fibre reduction holds on all %d (pair, lambda)"
          " fibres of multipliers" % fibre_test)
    print("    coprime to both states: two such moves of equal lambda"
          " resolve or fail TOGETHER")
    print("  an up-set? NO on %d of %d (resolver, cofactor) tests"
          % (up_fail, up_test))
    if first_up:
        print("    first: N=%d, N=%d resolve at d=%d and re-merge at %d"
              % (first_up[0], first_up[1], first_up[2],
                 first_up[2] * first_up[3]))
    print("  but its COMPLEMENT is closed under coprime products on %d of"
          " %d tests" % (blind_test - blind_fail, blind_test))
    if first_blind:
        print("    exception: N=%d, N=%d stay blind under %d and %d and"
              " split at %d"
              % (first_blind[0], first_blind[1], first_blind[2],
                 first_blind[3], first_blind[2] * first_blind[3]))
    print("  closed under multiplication? NO on %d of %d resolver pairs"
          % (mul_fail, mul_test))
    if first_mul:
        print("    first: N=%d, N=%d resolve at %d and at %d, not at %d"
              % (first_mul[0], first_mul[1], first_mul[2], first_mul[3],
                 first_mul[2] * first_mul[3]))
    print()


# --------------------------------------------------------- S5 the watcher

def s5_watcher():
    print("S5 THE WATCHER AGAINST THE CHOOSER")
    pairs = blind_pairs(POOL_CAP)
    strict = 0
    tot_blind = tot_div = 0
    watcher_wins = watcher_tests = 0
    example = None
    for N1, N2 in pairs:
        V = headroom(N1)
        R = set()
        for d in range(2, 61):
            if headroom(N1 * d) != headroom(N2 * d):
                R.add(d)
        fully_blind = [m for m in range(2, 61)
                       if not any(d in R for d in divisors(m))]
        divs = [m for m in divisors(V) if 1 < m <= 60]
        tot_blind += len(fully_blind)
        tot_div += len(divs)
        extra = sorted(set(fully_blind) - set(divs))
        if extra:
            strict += 1
            if example is None:
                example = (N1, N2, V, extra[:4])
        watcher_tests += 59
        watcher_wins += 59 - len(fully_blind)
    n = len(pairs)
    print("  a watcher wins on m iff SOME divisor of m resolves -- the"
          " readings inside a move")
    print("    are exactly {V(N d) : d | m}, so the depth ladder buys"
          " nothing beyond one split")
    print("  over the %d pairs and moves 2..60: the watcher is told apart"
          " on %.1f%% of moves," % (n, 100.0 * watcher_wins / watcher_tests))
    print("    while a chooser wins on every pair -- the gap is the %d"
          " fully-blind moves" % (tot_blind))
    print("  of those, %d are divisors of the reading and blind BY ALGEBRA;"
          " the family is" % tot_div)
    print("    strictly larger for %d of the %d pairs" % (strict, n))
    if example:
        print("    e.g. N=%d, N=%d at V=%d stay blind under %s, none a"
              " divisor of V"
              % (example[0], example[1], example[2],
                 ", ".join(str(x) for x in example[3])))
    print()


# ------------------------------------------------------------------ the run

def main():
    s1_control()
    if FAIL:
        print("POSITIVE CONTROL FAILED -- no verdict is read.")
        return 1
    s2_floor()
    s2b_readable()
    s3_ladder()
    s4_structure()
    s5_watcher()
    if FAIL:
        print("FAILURES: %d" % len(FAIL))
        for f in FAIL:
            print("  " + f)
        return 1
    print("all sections pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
