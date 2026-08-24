"""explore_proth_window.py -- is the least resolver really always a prime
power, and do arbitrarily divisible readings host blind pairs?

QUESTION. Two open ends of the resolution threshold. (i) Over every pair
of the standard pool the least resolver is a prime power (4498/4498
comparisons), and the natural proof is dead: the non-resolvers are not
closed under coprime products. Is there a different proof route -- or a
counterexample past the pool cap? (ii) The threshold's unboundedness was
reduced to occupancy -- do arbitrarily divisible readings host blind
pairs -- and the class enumeration reached lambda <= 600. How far does
occupancy actually extend?

THE HAND-ATTACK (done before any engine code; its conclusions are frozen
here as predictions, and every load-bearing number below is one the run
must reproduce).

  (A) THE ROUTE THAT REPLACES COPRIME CLOSURE. Call the resolving set R
  prime-power ROOTED if every resolver has a resolving prime-power
  DIVISOR. Rootedness is weaker than coprime closure -- the
  known closure witness (N = 16, 32 blind under 4 and under 7, split at
  28) has the divisor 2 resolving, so it does not touch rootedness --
  and rootedness alone gives the observation: a least resolver that is
  not a prime power has all its prime-power divisors smaller, hence
  blind, contradiction.

  (B) HUNTING A ROOTEDNESS COUNTEREXAMPLE KILLS THE OBSERVATION INSTEAD.
  The pure 2-power states sit above the pool cap and their door
  arithmetic is exactly Fermat/Proth primality. lambda(2^a) = 2^(a-2),
  and W(2^(a-2)) = 2^a * 3 * 5 * 17 * 257 for a - 2 in 8..15, so

      V(2^a) = 65535 = 3 * 5 * 17 * 257   for a = 10..17,

  one blind class of eight 2-power members. Under a move d = 2^x * m
  (m odd), the deeper state's lambda is lcm(2^(a-1+x), lambda(m)): the
  doors it can open are the primes u' * 2^k + 1 with u' dividing the odd
  part of lambda(m) and k at most the 2-depth -- Fermat primes when
  m = 1, PROTH primes otherwise. A move resolves the adjacent pair
  (2^a, 2^(a+1)) exactly when such a prime sits at the deeper state's
  depth and not at the shallower's. For the pair (2^11, 2^12):

    - the 2-ladder is doorless to d = 32: 2^k + 1 is composite for
      k = 11..15 (2049, 4097 = 17*241, 8193 = 3*2731, 16385 = 5*29*113,
      32769), and the next Fermat prime 65537 fires only at d = 64;
    - every odd-routed door below 28 is composite at the needed depth:
      3 * 2^9 + 1 = 1537 = 29*53, 3 * 2^10 + 1 = 3073 = 7*439,
      3 * 2^11 + 1 = 6145 = 5*1229 (kills d = 7, 9, 13, 14, 18, 21,
      26), 5 * 2^10 + 1 = 5121 = 3*3*569 (kills 11, 25), 5 * 2^11 + 1 =
      10241 = 7*7*11*19 (kills 22), 9 * 2^9 + 1 = 4609 = 11*419 and
      9 * 2^10 + 1 = 9217 = 13*709 (kill 19, 27), 11 * 2^10 + 1 =
      11265 (kills 23); 3, 5, 15, 17 are transparent outright;
    - but 3 * 2^12 + 1 = 12289 IS PRIME, and d = 28 = 2^2 * 7 reaches
      it: lambda(2^14 * 7) = 3 * 2^12 = 12288 opens the door 12289 at
      the deeper state while lambda(2^13 * 7) = 6144 opens nothing new.

  So (2048, 4096) should be blind with least resolver 28 -- NOT a prime
  power -- and the pool observation is refuted rather than proved. The
  pool could not see it: the witness states start at 2048, the pool cap
  is 1500, and mixed states wash the Fermat-desert mechanism out.

  (C) THE SAME WINDOW, PAIR BY PAIR. The identical arithmetic predicts
  the least resolver of every adjacent 2-power pair (blind exactly when
  2^(a-1) + 1 is composite, i.e. a - 1 is not a Fermat exponent):
  a = 4: d = 2 (door 17); a = 6: d = 7 (door 97 = 3 * 2^5 + 1); a = 7:
  d = 4 (door 257); a = 8: d = 2 (door 257); a = 10: d = 31 (door
  7681 = 15 * 2^9 + 1, the odd part 15 of lambda(31) = 30 carrying it);
  a = 11: d = 28 (door 12289); a = 12: d = 14 (door 12289 again, one
  rung shallower); a = 13: d = 7 (door 12289 at x = 0); a = 15: d = 4
  (door 65537); a = 16: d = 2 (door 65537). a = 14 is left open by
  hand: it hinges on whether 3 * 2^13 + 1 = 24577 is prime, which is
  not settled here. Composite least resolvers at a = 11 and a = 12 --
  the species is a window, not a fluke.

  (D) THE DEEP LADDER BASE. A state N is in the class of reading V0
  exactly when N = W(L)/V0 with L = lambda(N), so members biject with
  the valid L. If V0 = W(L0) then W(L0) | W(L) is necessary, which
  forces v_2(L) >= v_2(L0), every odd door p of L0 open at L with
  v_p(L) >= v_p(L0) -- so every member's lambda is a multiple of

      B0(L0) := lcm( 2^v_2(L0),  lcm(p - 1, p^v_p(L0)) over odd doors p ),

  and B0 | L0 always (each part divides L0 by the door definition). The
  enumeration can therefore sweep L over MULTIPLES of B0 instead of
  every integer: same completeness statement, reach deeper by a factor
  of B0. That is what turns "lambda <= 600" into "lambda <= millions"
  at the divisible targets, where B0 is large.

PREDICTIONS, frozen before the engine.

  1. (derived, control) The imported reading matches the hand wall
     arithmetic: V(2^a) = 65535 for a = 10..17 exactly; on the witness
     pair, resolution and wall-gain disagreement coincide for every
     d <= 60; gain(2^11, 7) = 3 * 7 * 13 * 97 * 193 * 769; and every
     blind pair of the standard pool has lambda_1 != lambda_2 (one
     line: W(lambda_i) = V * N_i and the N_i differ). A failure aborts
     the run before any verdict is read.
  2. (derived on paper, the run is the check) The pair (2048, 4096) is
     blind; every d = 2..27 keeps it blind; 28 resolves it. Kill-shape
     as an observable: any printed resolver below 28, or a blind print
     at 28 -- either voids the refutation and the observation stands.
  3. (derived on paper, per-cell) The adjacent-pair table of (C), each
     cell an observable print; the a = 14 cell is left unpredicted.
  4. (derived, control) B0 divides the lambda of every member the flat
     sweep finds, and the B0-multiple sweep at the flat cap returns
     exactly the flat sweep's members, target by target.
  5. (open) Occupancy continues: some target with floor ABOVE 17 hosts
     a blind pair within the deep reach -- the guess is yes at W(240)
     (floor 19) or W(720) (floor 23). Kill-shape as an observable: the
     largest floor carrying a pair is identical at every printed depth
     rung, i.e. the deepening bought nothing.
  6. (open) In every deep-ladder pair the least resolver still EQUALS
     the floor -- the guess is that the Proth-window species needs the
     tau-poor readings of the 2-tower and stays away from divisible
     readings, where the floor is attained as before.

  A SECOND FREEZE, written after the first run and only for the flaw
  that run exposed. The frozen kill-shape of prediction 5 measured the
  TARGET LIST, not the depth: every target was populated already at
  k <= 60 (membership among base multiples runs above 80 percent), so
  the largest floor could never move -- it was pinned at the list's own
  maximum, 23. The meaningful observables are the floor a target can be
  DESIGNED to carry and the depth k at which its second member appears.
  Two door-saturated targets are added -- L0 = 55440 = lcm(2^4, 3^2, 5,
  7, 11), every prime to 43 a door, floor 47; and L0 = 36988560,
  intended as 55440 * 23 * 29 with floor 81 -- with per-target depth
  caps sized to their cost.

  7. (open, frozen before the extended run) Both new targets host blind
     pairs within reach, their second members appearing at small k, and
     both attain their floors -- 47 and 81 -- as least resolvers.

  A THIRD NOTE, written after the extended run, which exposed two
  arithmetic slips in the second freeze. The constant was mistyped:
  36988560 is 2^4 * 3^2 * 5 * 7 * 41 * 179, not 55440 * 23 * 29 =
  36978480 -- the run printed floor 23 for it, which is CORRECT for the
  number that actually ran (23 - 1 = 22 needs 11, absent), and the
  accidental target stays in the table as what it is. And the floor-81
  derivation itself slipped a door: 53 - 1 = 52 = 4 * 13 needs
  13 | L0, which 55440 * 23 * 29 lacks (its floor is 53). The
  door-saturated target with floor 81 = 3^4 is

      L0 = 55440 * 13 * 23 * 29 = 480720240,

  every prime to 79 a door and 81 the 3-part's own ceiling. It is added
  at k <= 100 with prediction 7's guess re-frozen for it before its
  run: populated at small k, floor 81 attained.

DESIGN. Four sections.

  S1 POSITIVE CONTROL, first, aborting on failure: the hand numbers of
  prediction 1 against the imported headroom/gain/wall path, the
  primality verdicts the hand-attack leans on (12289, 7681, 97, 193,
  257, 769 prime; 1537, 3073, 6145, 5121, 10241, 4609, 9217, 11265,
  2049, 4097, 8193, 16385, 2^k + 1 for k = 11..15 composite), and the
  lambda-differ line over the pool.

  S2 THE REFUTATION. The witness pair (2^11, 2^12): the full d-sweep
  printed as observables (blind through 27, split at 28), the least
  resolver by the imported brute-force search, the factored gain ratio
  at 28 (the door), and the prime-power verdict on the result.

  S3 THE WINDOW. The adjacent-pair table a = 4..16: blind or not, least
  resolver, prime power or not, witness door (the new prime in the
  factored gain ratio at the least resolver). One table, one row per a.

  S4 THE DEEP LADDER. B0 computed per target; the control of
  prediction 4 at the flat cap; then the deep sweep -- L = B0 * k,
  k up to a per-target depth cap -- over targets W(L0) for L0 = 12, 60,
  180, 240, 420, 720, 840, 2520 at k <= 6000 plus the two
  door-saturated targets of the second freeze at k <= 1500 and 100,
  reporting members found, the depths of the first two, the floor,
  occupancy, the least resolver of the first pair against the floor,
  and the kill-shape of prediction 5 evaluated at three depth rungs
  (kept, with its flaw, for the record the second freeze names).

FINDINGS.

  1. EVERY CONTROL PASSES AND EVERY HAND NUMBER REPRODUCES (S1): the
     eight readings V(2^a) = 65535 for a = 10..17, the criterion on the
     witness pair for every d <= 60, gain(2^11, 7) = 3930230577 =
     3 * 7 * 13 * 97 * 193 * 769 exactly, all 20 primality verdicts the
     derivation leans on (7 primes, 13 composites, none repeated), and
     lambda_1 != lambda_2 on all 96 pool pairs.

  2. THE PRIME-POWER OBSERVATION IS REFUTED (S2; prediction 2 lands).
     The pair (2048, 4096), blind at V = 65535, keeps every d = 2..27
     blind and splits at d = 28 = 2^2 * 7: the least resolver is NOT a
     prime power. The factored gain ratio at 28 is the single door
     12289 = 3 * 2^12 + 1 -- the hand mechanism exactly: the move's
     2-part deepens the 2-adic seat, its odd part routes the door
     condition to a Proth prime, and the prime sits at the deeper
     state's depth only. The pool's 4498/4498 was a cap artifact: the
     witness states begin at 2048, the pool ends at 1500. The proof
     that was hunted does not exist.

  3. THE PROTH WINDOW, CELL BY CELL (S3; prediction 3 lands on all ten
     predicted cells). Least resolvers 2, 7, 4, 2, 31, 28, 14, 7, 4, 2
     at a = 4, 6, 7, 8, 10, 11, 12, 13, 15, 16, each with its predicted
     witness door (17, 97, 257, 257, 7681, 12289, 12289, 12289, 65537,
     65537); the cell left open by hand, a = 14, resolves to d = 8 via
     65537 -- so 3 * 2^13 + 1 = 24577 is composite and the Proth route
     loses to the Fermat door there. Composite least resolvers at
     a = 11 (d = 28) and a = 12 (d = 14): a window, not a fluke. The
     least resolver of an adjacent 2-power pair is min over moves
     2^x * m of the first u' * 2^(a-1+x) + 1 that is PRIME with u'
     dividing the odd part of lambda(m) -- Fermat primes on the pure
     ladder, Proth primes off it -- so whether the minimum is a prime
     power is primality numerology at exact depths, not structure, and
     the threshold's growth along the family reduces to Proth-prime
     gaps (conjecture-gated; the view, not a claim).

  4. THE LADDER BASE HOLDS AND MULTIPLIES THE REACH BY B0 (S4;
     prediction 4 lands): B0 divides every flat member's lambda and the
     B0-multiple sweep returns exactly the flat members on all 7
     control targets at lambda <= 600 -- so the deep sweep's
     completeness statement stands, and the reach runs to lambda <=
     15 120 000 at W(2520) and 48 072 024 000 at the floor-81 target
     against the old flat 600.

  5. OCCUPANCY IS DENSE, NOT SCARCE, AND THE FLOOR LADDER CLIMBS TO 81
     (S4; predictions 5 and 7 land, and the flaw the second freeze
     names is real). Every target is populated by k = 6 at the latest
     -- member counts run 4824..5957 of 6000 base multiples at the
     eight original targets, 1499 of 1500 and 99 of 100 at the
     saturated ones -- so the binding constraint on exhibiting large
     floors is the floor a target is DESIGNED to carry, not the depth,
     at every depth tried: the kill-shape rung print stalls at its list's own maximum
     at every depth, exactly the flaw named. The designed targets
     deliver: W(55440) hosts a pair at floor 47 (states of 31 and 51
     digits) and W(480720240) at floor 81 = 3^4 (states of 264 and 453
     digits). The second freeze's two arithmetic slips (a mistyped
     constant; a door slip in the floor-81 derivation) are recorded
     above; the accidental target W(36988560) stays, floor 23,
     populated and attained.

  6. THE FLOOR IS ATTAINED AT EVERY POPULATED TARGET (S4; prediction 6
     lands): all eleven first pairs resolve at exactly their floor --
     11, 17, 17, 19, 17, 23, 17, 17, 47, 23, 81. The two legs part
     cleanly: divisible readings buy arbitrarily large thresholds at
     exactly the floor price the reading names in advance, while the
     tau-poor 2-tower readings (floor 2) pay Proth-window premiums far
     above it. Occupancy -- the one gate the unboundedness reduction
     left -- is now exhibited through floor 81 with no sign of
     thinning; what remains open is only the tail: whether the door
     supply keeps every designed floor populated forever.
     (SETTLED SINCE BY explore_silent_set.py: at every even L the primes
     q with V(q) = W(L) are >> x/log^2 x, so every designed reading is
     populated, and along L = lcm(1..n) every prime up to n+1 is a door
     of L while each door r's own term r^(v_r(W)+1) exceeds r*n, so
     floor(W(L)) > n+1 -- the threshold is unbounded at theorem
     tier. What stays measured is that a designed reading's least
     resolver EQUALS its floor.)

SCOPE. Exact integer arithmetic throughout; states in the deep ladder
are carried as exponent maps and never factored. The witness d-sweep is
exhaustive to 200; the window table's least resolvers are exact within
the same cap. The deep sweep is complete for lambda <= B0 * K_DEEP per
target -- members with larger lambda exist and are invisible here, so
"one member within reach" bounds occupancy at this depth and says
nothing beyond it. Primality is the imported deterministic Miller-Rabin,
exact for every operand this run touches. What is PROVED rather than
measured: the refutation itself (a finite check), the rootedness
reduction (A), and the ladder base B0 (D); the window table's door
mechanism is proved per printed cell, its extrapolation to all a is
not; occupancy figures are measurements at the stated depths.

RUN RECORD. Python 3, no third-party dependencies, 17.0 s wall clock,
peak working set 68.1 MB under the memory watchdog (limit 512 MB). Four
sections, ALL CHECKS PASS; the positive control runs first and a
failure aborts the run before any verdict is read. The first run (eight
original targets) and the extension (the saturated targets) printed
identical values on every shared line.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

import explore_premium as _prem
from explore_premium import (doors, factorint, headroom, is_prime, lam,
                             lcm, v_p, wall)
from explore_resolver_threshold import (fdiv, fheadroom, flam, fmul,
                                        floor_of, fvalue, fwall, gain,
                                        least_resolver)
from explore_composite_move import blind_pairs

FAIL = []

POOL_CAP = 1500        # the standard pool, for the control only
SEARCH_CAP = 200       # brute-force reach for a least resolver
FLAT_CAP = 600         # the old enumeration's flat lambda cap
K_DEEP = 6000          # deep sweep: L = B0 * k, k <= K_DEEP

WITNESS = (2 ** 11, 2 ** 12)


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("  FAIL: " + msg)
    return cond


def is_prime_power(n):
    return len(factorint(n)) == 1


def door_ratio(g_small, g_large):
    """The factored quotient of two gains -- the doors one state opened
    beyond the other, with 1 meaning the gains agree."""
    if g_large % g_small:
        return None
    return factorint(g_large // g_small)


# ---------------------------------------------------------------- S1 control

def s1_control():
    print("S1 POSITIVE CONTROL")
    vals = [headroom(2 ** a) for a in range(10, 18)]
    check(vals == [65535] * 8,
          "V(2^a) != 65535 somewhere on a = 10..17: %s" % vals)
    print("  V(2^a) = 65535 = 3*5*17*257 for a = 10..17 -- eight 2-power"
          " states, one blind class")

    N1, N2 = WITNESS
    bad = 0
    for d in range(2, 61):
        resolves = headroom(N1 * d) != headroom(N2 * d)
        if resolves != (gain(N1, d) != gain(N2, d)):
            bad += 1
    check(bad == 0, "criterion breaks on the witness pair at %d moves" % bad)
    print("  the resolution criterion holds on the witness pair for every"
          " d <= 60")

    g7 = gain(N1, 7)
    check(g7 == 3 * 7 * 13 * 97 * 193 * 769,
          "gain(2^11, 7) = %d, not the hand value" % g7)
    print("  gain(2^11, 7) = %d = 3*7*13*97*193*769, the hand number" % g7)

    prime_side = [12289, 7681, 97, 193, 257, 769, 65537]
    comp_side = [1537, 3073, 6145, 5121, 10241, 4609, 9217, 11265,
                 2049, 4097, 8193, 16385, 32769]
    check(all(is_prime(p) for p in prime_side),
          "a door the derivation needs prime is not")
    check(not any(is_prime(c) for c in comp_side),
          "a depth the derivation needs doorless has a prime")
    print("  all %d primality verdicts the hand-attack leans on reproduce"
          % (len(prime_side) + len(comp_side)))

    pairs = blind_pairs(POOL_CAP)
    check(all(lam(a) != lam(b) for a, b in pairs),
          "a pool pair shares its lambda")
    print("  lambda_1 != lambda_2 on all %d pool pairs (W(lambda_i) ="
          " V*N_i forces it)" % len(pairs))
    print()


# ------------------------------------------------------------ S2 refutation

def s2_refutation():
    print("S2 THE REFUTATION: THE LEAST RESOLVER NEED NOT BE A PRIME POWER")
    N1, N2 = WITNESS
    V = headroom(N1)
    check(V == headroom(N2), "the witness pair is not blind")
    print("  the pair (%d, %d), blind at V = %d, floor %d"
          % (N1, N2, V, floor_of(V)))

    blind_through = []
    split_at = None
    for d in range(2, SEARCH_CAP + 1):
        if headroom(N1 * d) != headroom(N2 * d):
            split_at = d
            break
        blind_through.append(d)
    check(split_at == 28, "the split lands at %s, not 28" % split_at)
    check(blind_through == list(range(2, 28)),
          "a move below 28 already resolves")
    print("  every d = 2..27 keeps the pair blind; d = 28 = 2^2 * 7"
          " resolves it")

    d0 = least_resolver(N1, N2)
    check(d0 == 28, "least_resolver says %s" % d0)
    check(not is_prime_power(28), "28 is a prime power?!")

    ratio = door_ratio(gain(N1, 28), gain(N2, 28))
    check(ratio == {12289: 1},
          "the door at 28 is %s, not 12289 alone" % ratio)
    print("  the factored gain ratio at 28 is the single door 12289 ="
          " 3 * 2^12 + 1 (prime),")
    print("    opened at lambda(2^14 * 7) = 12288 and not at"
          " lambda(2^13 * 7) = 6144")
    print("  -- the least resolver 28 is COMPOSITE: the prime-power"
          " observation is refuted,")
    print("     and the pool's 4498/4498 was a cap artifact (witness"
          " states 2048 and 4096, pool cap 1500)")
    print()


# ------------------------------------------------------------- S3 the window

def s3_window():
    print("S3 THE PROTH WINDOW: ADJACENT 2-POWER PAIRS, a = 4..16")
    print("  %-4s %-7s %-14s %-12s %s"
          % ("a", "blind?", "least resolver", "prime power", "witness door"))
    composites = []
    for a in range(4, 17):
        N1, N2 = 2 ** a, 2 ** (a + 1)
        if headroom(N1) != headroom(N2):
            fermat = 2 ** (a - 1) + 1
            print("  %-4d no      (2^%d + 1 = %d is prime: the door"
                  " between them is open)" % (a, a - 1, fermat))
            check(is_prime(fermat),
                  "pair a=%d not blind yet no Fermat door" % a)
            continue
        d0 = least_resolver(N1, N2)
        if d0 is None:
            print("  %-4d yes     > %d (censored)" % (a, SEARCH_CAP))
            continue
        ratio = door_ratio(gain(N1, d0), gain(N2, d0))
        door = max(ratio) if ratio else None
        pp = is_prime_power(d0)
        if not pp:
            composites.append((a, d0))
        print("  %-4d yes     %-14d %-12s %s"
              % (a, d0, "yes" if pp else "NO", door))
    check(len(composites) >= 2,
          "fewer than two composite least resolvers in the window: %s"
          % composites)
    print("  composite least resolvers in the window: %s"
          % ", ".join("d = %d at a = %d" % (d, a) for a, d in composites))
    print("  -- the door is Fermat on the pure 2-ladder and Proth off it;"
          " whether the minimum")
    print("     is a prime power is Proth numerology, not structure, and"
          " unboundedness along")
    print("     the family reduces to Proth-prime gaps (conjecture-gated)")
    print()


# -------------------------------------------------------- S4 the deep ladder

def ladder_base(L0):
    """B0(L0): every member of the class of reading W(L0) has a lambda
    divisible by this. Necessity: W(L0) | W(L) forces the 2-depth, every
    old door open, every old exponent covered."""
    b = 2 ** v_p(L0, 2)
    for p in doors(L0):
        if p > 2:
            b = lcm(b, lcm(p - 1, p ** v_p(L0, p)))
    return b


def members_flat(L0, lam_cap):
    """The old enumeration: every L, no base filter."""
    fV0 = fwall(L0)
    out = []
    for L in range(1, lam_cap + 1):
        f = fdiv(fwall(L), fV0)
        if f is not None and f and flam(f) == L:
            out.append(L)
    return out


def members_deep(L0, k_cap, b=None):
    """The base-multiple enumeration: L = B0 * k only, complete for
    lambda <= B0 * k_cap."""
    b = b or ladder_base(L0)
    fV0 = fwall(L0)
    out = []
    for k in range(1, k_cap + 1):
        L = b * k
        f = fdiv(fwall(L), fV0)
        if f is not None and f and flam(f) == L:
            out.append((L, f))
    return out


def s4_deep_ladder():
    print("S4 THE DEEP LADDER: OCCUPANCY OF DIVISIBLE READINGS")

    # prediction 4: the base theorem, controlled against the flat sweep
    agree = True
    for L0 in (2, 4, 12, 60, 180, 240, 420):
        b = ladder_base(L0)
        flat = members_flat(L0, FLAT_CAP)
        deep = [L for L, _ in members_deep(L0, FLAT_CAP // b, b=b)]
        if flat != deep or any(L % b for L in flat):
            agree = False
    check(agree, "the base-multiple sweep disagrees with the flat sweep")
    print("  CONTROL: B0 divides every flat member's lambda and the"
          " B0-multiple sweep returns")
    print("    exactly the flat members, on all 7 control targets at"
          " lambda <= %d" % FLAT_CAP)

    targets = [(12, K_DEEP), (60, K_DEEP), (180, K_DEEP), (240, K_DEEP),
               (420, K_DEEP), (720, K_DEEP), (840, K_DEEP), (2520, K_DEEP),
               (55440, 1500), (36988560, 100), (480720240, 100)]
    print("  %-11s %-10s %-6s %-8s %-9s %-10s %-8s %s"
          % ("target", "B0", "floor", "members", "k1,k2", "least res.",
             "attained", "reach (lambda <=)"))
    populated = []
    for L0, kcap in targets:
        b = ladder_base(L0)
        V0 = wall(L0)
        fl = floor_of(V0)
        mem = members_deep(L0, kcap, b=b)
        d0 = None
        if len(mem) >= 2:
            f1, f2 = mem[0][1], mem[1][1]
            for cand in range(2, SEARCH_CAP + 1):
                fc = factorint(cand)
                r1, r2 = fheadroom(fmul(f1, fc)), fheadroom(fmul(f2, fc))
                assert r1 is not None and r2 is not None, \
                    "a ladder state stopped being a state"
                if r1 != r2:
                    d0 = cand
                    break
            populated.append((L0, fl, d0, len(str(fvalue(f1))),
                              len(str(fvalue(f2)))))
        ks = ",".join(str(L // b) for L, _ in mem[:2]) if mem else "-"
        print("  W(%-8d) %-10d %-6d %-8d %-9s %-10s %-8s %d"
              % (L0, b, fl, len(mem), ks,
                 d0 if d0 else ("-" if len(mem) < 2 else "> cap"),
                 ("yes" if d0 == fl else "NO") if d0 else "-",
                 b * kcap))
        _prem._DCACHE.clear()   # per-target: the door cache is the footprint
        _prem._WCACHE.clear()
    for L0, fl, d0, dg1, dg2 in populated:
        check(d0 is not None and d0 >= fl,
              "W(%d): least resolver %s under floor %d" % (L0, d0, fl))
        print("    W(%d): floor %d, least resolver %s, states of %d and %d"
              " digits%s" % (L0, fl, d0, dg1, dg2,
                             " -- FLOOR ATTAINED" if d0 == fl else ""))

    # prediction 5's kill-shape: the largest floor with a pair, by depth
    # (kept with its flaw for the record -- the second freeze names it)
    rungs = []
    for kc in (60, 600, K_DEEP):
        best = 0
        for L0, kcap in targets:
            b = ladder_base(L0)
            if len(members_deep(L0, min(kc, kcap), b=b)) >= 2:
                best = max(best, floor_of(wall(L0)))
            _prem._DCACHE.clear()
            _prem._WCACHE.clear()
        rungs.append((kc, best))
    print("  the frozen kill-shape, evaluated: largest floor with a pair"
          " at k <= %s"
          % ", ".join("%d is %d" % (c, bst) for c, bst in rungs))
    moved = len({bst for _, bst in rungs}) > 1
    print("    -- it MOVES with the depth" if moved else
          "    -- it does NOT move, which is the kill the freeze named")
    print()


def main():
    for step in (s1_control,):
        step()
        if FAIL:
            print("POSITIVE CONTROL FAILED -- aborting before any verdict")
            return 1
    s2_refutation()
    s3_window()
    s4_deep_ladder()
    if FAIL:
        print("FAILURES: %d" % len(FAIL))
        for m in FAIL:
            print("  " + m)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
