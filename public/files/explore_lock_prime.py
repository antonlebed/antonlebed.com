"""
explore_lock_prime.py — the lock-prime law (sibling of
explore_growth_laws.py, explore_growth_capability.py,
explore_size_crystallization.py).

THE QUESTION. Prior work measured D-DYN (grow by the least m >= 2 with
lambda(N*m) > lambda(N)) locking onto a single prime — 11/11 seeds,
40-step scope, lock target varying with the seed, no proof and no
formula. This script proves the lock and computes the basin map:
WHICH prime does a seed fall into, WHEN is the fall decided, and is
every prime somebody's destiny?

FINDINGS (naming tiers below; run record follows; all sections assert).

1. THE DOOR MENU (rule, proved; verified exhaustively N <= 20000).
   The minimal growth move is always a PRIME POWER q^r: lambda(Nm) =
   lcm of channel contributions, so growth needs one channel's
   contribution to escape lambda, and that channel's prime-power part
   of m alone is a smaller legal move. Per prime, the DOOR is the
   least q^r with lambda(q^{e+r}) not dividing lambda(N) (e = v_q(N)):
     odd q, e >= 1 (deepening):  r = v_q(lambda) - e + 2
     odd q, e = 0  (opening):    r = 1 if (q-1) does not divide lambda,
                                 else r = v_q(lambda) + 2
     q = 2: same scan with contributions 1, 2, 2^{d-2}.
   Door costs are powers of distinct primes, hence pairwise distinct:
   D-DYN is DETERMINISTIC — no tie-break axis exists (contrast:
   costless D-IND needed one, explore_size_crystallization.py).

2. THE GHOST TRICHOTOMY (rule, proved; classified over the sweep).
   Every minimal move is one of: a DEEPENING (q | N); a FRESH OPENING
   (q coprime, v_q(lambda) = 0); or a GHOST OPENING (q coprime,
   q | lambda, (q-1) not dividing lambda) — a prime whose period
   already haunts the dynamics with no window of its own. Cost of a
   ghost: q. What a ghost buys: nothing recurrent — its post-move
   door jumps to q^{v_q(lambda)+1} or worse.

3. THE LOCK CRITERION (rule, proved; verified 2000 seeds x 30
   post-lock steps). Deepenings and fresh openings establish THE
   RECURRENCE INVARIANT — v_q(lambda) = e_q - 1 (odd q; e_q - 2 for
   q = 2, e >= 3) — which prices q's door at q FOREVER, while every
   rival door is nondecreasing (lambda only grows) and can never
   equal q (powers of distinct primes). So THE FIRST NON-GHOST PICK
   LOCKS THE TRAJECTORY: all later picks deepen the same prime.
   (One q = 2 hiccup, frozen pre-run: lambda(4) = lambda(8) = 2, so a
   2-lock passing e = 2 pays one cost-4 double step, then cost 2.)

4. THE WANDER BOUND (rule, proved; verified 2000 seeds + census).
   Pre-lock picks are all ghosts; ghosts strictly increase (ghost
   legality (q-1) not dividing lambda only SHRINKS as lambda grows, so
   a cheaper legal ghost would have fired earlier); and a later
   ghost's prime divides lambda(seed) already (factors added to
   lambda by ghost q_j are factors of q_j - 1 < q_j, too small to
   mint later ghosts). So the wander visits only odd prime factors of
   lambda(seed): LOCK IS CERTAIN within omega_odd(lambda(seed)) + 1
   picks. Upgrades explore_growth_laws.py's miser observation (11/11 seeds, 40-step
   scope) to a rule with no scope caveat — and explains why that script
   never met the wander at all: its 11 seeds all have wander 0 (the
   observation itself was safe either way; locks are certain).

5. THE GHOST DOWRY (rule; specimens verified). A ghost opening q
   adds the factors of q - 1 to lambda, CLOSING cheaper locking doors
   behind it — wandering can LIFT the lock far above the seed's
   cheapest lock. Specimens (trajectories asserted):
     seed 11    ghost 5        -> LOCK 7   (outside the earlier seed set)
     seed 71    ghosts 5, 7    -> LOCK 17  (ghost 7's dowry 6 blocks
                the 9-door that would have locked 3)
     seed 20231 ghosts 5, 7, 17 -> LOCK 19 (wander 3, = omega_odd
                bound tight: 20230 = 2 * 5 * 7 * 17^2)
   Same prime, both roles: 17 is seed 71's LOCK (17 not dividing
   lambda = fresh) and seed 20231's GHOST (17 | lambda = ghost).

6. THE LOCK MAP (rule for the map, observation for the census). The
   basin map seed -> lock prime is computable in <= omega_odd + 1
   menu evaluations — the depth fate's basin geography is DECIDABLE, and
   the fall is decided at the first non-ghost move. Census over
   seeds <= 20000: lock histogram, wander histogram, minimal seed
   per lock target — measured outputs in the RUN RECORD below (no
   census number was predicted; the specimens of finding 5 were).
   THE VOID'S COLUMN: seed 1 locks 3 (trajectory 1, 3, 9, 27, ...) —
   2 is dynamically invisible at birth (lambda(2) = 1; the 2-window's
   cheapest door from the void costs 4 while the 3-door costs 3):
   free dynamics grows the 3-adic column, not the 2-adic.

7. LOCK-TARGET COMPLETENESS (rule, proved for all q via the enriched
   blocker; instantiated + verified q <= 47). Every prime is some
   seed's lock: THE LINNIK BLOCKER seed q * P, with P a prime
   P == 1 (mod B), P != 1 (mod q), for the enriched modulus
   B = lcm( lcm{p - 1 : p prime <= q},  r^{c_r} for r prime < q )
   where c_r is least with r^{c_r + 2} > q. Then lambda(seed) =
   P - 1 (q - 1 | B); q's own door costs q (q never divides B or
   P - 1); every opening below q is blocked ((r-1) | B) and its
   blocked door r^{v_r + 2} >= r^{c_r + 2} > q BY CONSTRUCTION (this
   is what the enrichment buys — plain M = lcm{p-1} does not
   guarantee it for large q); every door above q costs > q; no ghost
   fires below q. So the first pick deepens q and locks — and
   Dirichlet supplies P (q does not divide B, so the class 1 mod B
   avoiding 1 mod q carries primes). In range the enrichment is a
   NO-OP — B == M for every q <= 47 (asserted): the verified seeds
   instantiate the general construction exactly, with P a
   Linnik-least-prime object — the same function governing the
   tower's lambda entry order here manufactures
   BASINS on demand. (An earlier draft of this construction, D9, used M over p < q and
   claimed q-1 | M — false at q = 5; the assert caught it. And D9's
   'blocked doors exceed q' was stated bare — true in range, not
   forced in general; the enrichment closes the gap.)
   THE PLATEAU RESONANCE (observation, from the run): the blocker is
   ONE prime, P = 55441 = 55440 + 1, for all of q = 29, 31, 37, 41,
   43 — because M = lcm{p-1 : p <= q} is the tower's lambda at the
   rung topped by q, and 31, 37, 41, 43 are the transparent run of
   the k = 10..14 plateau (jump rung 29): transparency
   = the blocker modulus standing still. The plateau constant
   re-enters as the basin manufacturer for its own rungs.

8. THE COLD DOORS (rule, proved; verified over the sweep). For every
   N >= 3: OPENING the 2-window costs >= 16 (lambda is even, so
   contributions 1, 2, 2 at depths 1-3 are all swallowed) and OPENING
   the 3-window costs >= 9 ((3-1) = 2 always divides lambda). The
   floors are UNIQUE to 2 and 3: every prime q >= 5 opens at face
   value (cost q) from some state — any lambda that (q-1) does not
   divide; lambda = 2 works for all of them (asserted, q <= 47).
   D-DYN marks up exactly the two primes D-IND buys first; they
   enter a D-DYN world only as seeds' own channels or at
   quadratic-plus door prices.

THE SYNTHESIS. The depth fate now has a decidable basin geography:
which infinite column a freely-growing system falls into is decided
at its first non-ghost move, at most omega_odd(lambda(seed)) ghost
moves in; every prime is a reachable destiny (Linnik blockers
manufacture basins); and the pre-decision wander is a ghost story —
primes whose periods already haunt the dynamics open cheap doors
that never bind, each one shutting cheaper destinies behind it (the
dowry). One level down, this is again selection theory
over a poset of doors: rising rival costs + one absorbing invariant
= lock; the tower picked its poset (explore_size_crystallization.py), the column picks its
absorbing door.

HONEST SCOPE. Multiplicative threshold-greedy D-DYN over Z/N only
(as in the sibling scripts); stochastic and additive moves remain open
questions. Whether wander length is UNBOUNDED over seeds is open — the
candidate mechanism is a 2-adic ghost ladder (5, 17, 97, 193, 257,
7681, ...: each the least prime with v2(p-1) exceeding the
accumulated dowry), but the blocker bookkeeping is delicate and no
construction is claimed; the max wander over the census range is a
measured output (RUN RECORD), with the wander-3 specimen 20231
asserted individually in S5.

PREDICTIONS (fixed before the run; a later pass amended PR5's q = 2
cost clause PRE-RUN — the
lambda(4) = lambda(8) hiccup was hand-caught before any code).
Adjudication:
  PR1 menu rule ......... CONFIRMED (S1: brute == formula, 20000/20000)
  PR2 trichotomy/no-tie . CONFIRMED (S1: costs distinct, class exclusive)
  PR3 prior seed reproduction . CONFIRMED (S4: 11/11 locks match, wander 0)
  PR4 specimens ......... CONFIRMED (S5: 11 -> [5] -> 7; 71 -> [5,7] ->
                          17; 20231 prime -> [5,7,17] -> 19; 1 -> 3-adic)
  PR5 lock criterion .... CONFIRMED as amended (S3: 2000 seeds x 30
                          post-lock steps; q=2 hiccup exactly as frozen)
  PR6 wander bound ...... CONFIRMED (S3)
  PR7 cold doors ........ CONFIRMED (S7: measured minima 16 and 9; the
                          frozen bound was the weaker >= 8)
  PR8 completeness ...... CONFIRMED AFTER TWO CONSTRUCTION FIXES — the
                          D9 blocker construction failed its own assert
                          twice at q = 5 (P = q slipped the filter;
                          q-1 | M false for M over p < q); the p <= q
                          form restores the proof.
                          The law survived; the hand-built witness
                          needed the machine.

RUN RECORD (python explore_lock_prime.py, ~1.8 s, trivial memory):
  S0 lambda cross-check: 299 moduli n <= 300 — lam_pp/carmichael ==
     the exponent of U(n) computed raw from element orders (the
     formula both S1 sides share is verified outside itself)
  S1/S2/S7 door-menu sweep: 20000 states — brute minimal move ==
     formula door everywhere (closed-form odd-q door formulas
     asserted per door), every minimal move a prime power, door
     costs pairwise distinct, classification exclusive; cold-door
     minima: 2-opening 16, 3-opening 9; every 5 <= q <= 47 opens at
     face value from lambda = 2 (the floors are unique to 2 and 3)
  S3 lock criterion + wander bound: seeds 1..2000, 30 post-lock steps
     each — first non-ghost pick locks, invariant at every step,
     ghosts increasing/dividing lambda(seed)/within omega_odd
  S4 prior-script seeds: 11/11 reproduced (2->2, 3->3, 5->5, 6->3, 10->5,
     21->5, 30->3, 105->5, 210->5, 2310->7, 30030->7), wander 0
  S5 specimens: as PR4; seed 1 trajectory 1 -> 3 -> 9 -> 27
  S6 census seeds 1..20000 (measured): locks {2: 3674, 3: 4193,
     5: 4672, 7: 3105, 11: 2612, 13: 202, 17: 1249, 19: 229, 23: 54,
     29: 10}; wander {0: 17749, 1: 2101, 2: 147, 3: 3}; max wander 3
     (least specimen seed 5237); minimal seed per lock target
     {2: 2, 3: 1, 5: 5, 7: 11, 11: 13, 13: 299, 17: 31, 19: 241,
     23: 1531, 29: 3169}
  S8 Linnik blockers: 15/15 primes q <= 47 lock at q, wander 0 —
     P = 13 (q = 5, 7), 61 (11, 13), 241 (17), 2161 (19), 23761 (23),
     55441 (29, 31, 37, 41, 43), 1275121 (47); largest seed
     59930687 = 47 * 1275121; enrichment no-op (B == M) asserted
     at every q
  TOTAL 558,628 checks, exit 0.
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

PRIMES = sieve(1_000_000)
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


def is_prime_mr(n):
    """Deterministic Miller-Rabin for n < 3.3e24 (fixed base set)."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


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


def divides(A, B):
    """Does the integer with factor dict A divide the one with dict B?"""
    return all(B.get(p, 0) >= e for p, e in A.items())


def maxmerge(A, B):
    out = dict(A)
    for p, e in B.items():
        if out.get(p, 0) < e:
            out[p] = e
    return out


def carmichael_dict(Nf):
    out = {}
    for p, e in Nf.items():
        out = maxmerge(out, lam_pp_factors(p, e))
    return out


def dict_to_int(f):
    n = 1
    for p, e in f.items():
        n *= p ** e
    return n


# ---------- the door menu ----------

def door(q, e, lamd):
    """Least r >= 1 with lambda(q^{e+r}) not dividing lambda. -> r"""
    for r in range(1, 90):
        if not divides(lam_pp_factors(q, e + r), lamd):
            return r
    raise AssertionError("door scan exhausted")


def menu(Nf, lamd):
    """All doors up to the winner. -> (best_door, doors); door =
    (cost, q, r, kind)."""
    doors = []
    best = None
    for q in sorted(Nf):
        r = door(q, Nf[q], lamd)
        d = (q ** r, q, r, "deepen")
        doors.append(d)
        if best is None or d[0] < best[0]:
            best = d
    for q in PRIMES:
        if best is not None and q > best[0]:
            break
        if q in Nf:
            continue
        r = door(q, 0, lamd)
        d = (q ** r, q, r, "open")
        doors.append(d)
        if best is None or d[0] < best[0]:
            best = d
    check(best is not None and best[0] < PRIMES[-1],
          "menu scan exhausted the prime table")
    return best, doors


def is_ghost(move, lamd):
    cost, q, r, kind = move
    return kind == "open" and r == 1 and lamd.get(q, 0) >= 1


def step(Nf, lamd):
    """One D-DYN move. -> (move, Nf', lamd')"""
    best, _ = menu(Nf, lamd)
    cost, q, r, kind = best
    Nf2 = dict(Nf)
    Nf2[q] = Nf2.get(q, 0) + r
    lamd2 = maxmerge(lamd, lam_pp_factors(q, Nf2[q]))
    return best, Nf2, lamd2


def run_trajectory(seed, max_steps):
    """-> (ghosts, lock_prime, moves, states) with classification
    against the PRE-move lambda."""
    Nf = factorize(seed) if seed > 1 else {}
    lamd = carmichael_dict(Nf)
    ghosts, lock, moves, states = [], None, [], []
    for _ in range(max_steps):
        best, _ = menu(Nf, lamd)
        ghost = is_ghost(best, lamd)
        cost, q, r, kind = best
        Nf = dict(Nf)
        Nf[q] = Nf.get(q, 0) + r
        lamd = maxmerge(lamd, lam_pp_factors(q, Nf[q]))
        moves.append(best)
        states.append((dict(Nf), dict(lamd)))
        if lock is None:
            if ghost:
                ghosts.append(q)
            else:
                lock = q
    return ghosts, lock, moves, states


# ---------- brute reference ----------

def carmichael_int(Nf):
    from math import gcd
    L = 1
    for p, e in Nf.items():
        c = dict_to_int(lam_pp_factors(p, e))
        L = L * c // gcd(L, c)
    return L


def merge_add(A, B):
    out = dict(A)
    for p, e in B.items():
        out[p] = out.get(p, 0) + e
    return out


def brute_min_move(Nf, upto):
    """Least m in [2, upto] with lambda(N*m) > lambda(N), or None."""
    lamN = carmichael_int(Nf)
    for m in range(2, upto + 1):
        if carmichael_int(merge_add(Nf, factorize(m))) > lamN:
            return m
    return None


def is_prime_power(m):
    f = factorize(m)
    return len(f) == 1


# =========================================================
print("=" * 64)
print("S0: lambda formula vs brute unit-group exponent (n <= 300)")
print("=" * 64)

from math import gcd as _g

for n in range(2, 301):
    exp = 1
    for a in range(1, n):
        if _g(a, n) == 1:
            o, x = 1, a % n
            while x != 1:
                x = x * a % n
                o += 1
            exp = exp * o // _g(exp, o)
    check(exp == carmichael_int(factorize(n)), f"lambda({n}) mismatch")
print("  299 moduli: lam_pp/carmichael == exponent of U(n), computed raw")

# =========================================================
print("=" * 64)
print("S1/S2/S7: THE DOOR MENU sweep (brute vs formula, N <= 20000)")
print("=" * 64)

SWEEP = 20000
min_door2 = None
min_door3 = None
for N in range(1, SWEEP + 1):
    Nf = factorize(N) if N > 1 else {}
    lamd = carmichael_dict(Nf)
    best, doors = menu(Nf, lamd)
    cost, q, r, kind = best
    # S2: door costs pairwise distinct (powers of distinct primes)
    costs = [d[0] for d in doors]
    check(len(set(costs)) == len(costs), f"tie in door costs at N={N}")
    # S1: the closed-form door formulas (finding 1) match the scan
    for dcost, dq, dr, dkind in doors:
        if dq == 2:
            continue
        de = Nf.get(dq, 0)
        dv = lamd.get(dq, 0)
        if de >= 1:
            check(dr == dv - de + 2, f"N={N}: deepening formula q={dq}")
        elif divides(factorize(dq - 1), lamd):
            check(dr == dv + 2, f"N={N}: blocked-opening formula q={dq}")
        else:
            check(dr == 1, f"N={N}: fresh-opening formula q={dq}")
    # S1: brute confirms — nothing cheaper grows, the door itself grows
    m = brute_min_move(Nf, cost)
    check(m == cost, f"N={N}: brute min {m} != formula door {cost}")
    check(is_prime_power(m) and m == q ** r,
          f"N={N}: minimal move {m} not the door prime power")
    # S2: classification is exclusive and exhaustive
    ghost = is_ghost(best, lamd)
    locking = (kind == "deepen") or (kind == "open" and not ghost)
    check(ghost != locking, f"N={N}: move classifies as both/neither")
    # S7: cold doors (openings of 2 and 3 for N >= 3)
    if N >= 3:
        if 2 not in Nf:
            c2 = 2 ** door(2, 0, lamd)
            check(c2 >= 8, f"N={N}: 2-opening door {c2} < 8 (PR7)")
            check(c2 >= 16, f"N={N}: 2-opening door {c2} < 16 (sharp)")
            min_door2 = c2 if min_door2 is None else min(min_door2, c2)
        if 3 not in Nf:
            c3 = 3 ** door(3, 0, lamd)
            check(c3 >= 9, f"N={N}: 3-opening door {c3} < 9")
            min_door3 = c3 if min_door3 is None else min(min_door3, c3)
# S7: the floors are unique to 2 and 3 — every q >= 5 opens at face
# value from lambda = 2 (the seed-3 state)
for q in PRIMES:
    if q > 47:
        break
    if q >= 5:
        check(door(q, 0, {2: 1}) == 1, f"q={q}: no face-value opening")
print(f"  {SWEEP} states: brute == formula (incl. closed forms), "
      f"prime-power moves, no ties")
print(f"  cold doors: min 2-opening {min_door2}, min 3-opening {min_door3};"
      f" every 5 <= q <= 47 opens at cost q from lambda = 2")

# =========================================================
print("=" * 64)
print("S3: LOCK CRITERION + WANDER BOUND (seeds 1..2000)")
print("=" * 64)

POST = 30
for seed in range(1, 2001):
    Nf0 = factorize(seed) if seed > 1 else {}
    lam0 = carmichael_dict(Nf0)
    omega_odd = sum(1 for p in lam0 if p != 2)
    ghosts, lock, moves, states = run_trajectory(seed, omega_odd + 1 + POST)
    check(lock is not None, f"seed {seed}: no lock within bound")
    # wander bound: ghosts strictly increasing odd primes dividing lambda0
    check(len(ghosts) <= omega_odd,
          f"seed {seed}: wander {len(ghosts)} > omega_odd {omega_odd}")
    check(all(g % 2 == 1 for g in ghosts), f"seed {seed}: even ghost")
    check(all(lam0.get(g, 0) >= 1 for g in ghosts),
          f"seed {seed}: ghost not dividing lambda(seed)")
    check(all(a < b for a, b in zip(ghosts, ghosts[1:])),
          f"seed {seed}: ghosts not increasing")
    # lock criterion: every post-lock pick is the lock prime, with the
    # recurrence invariant (q=2 hiccup allowed exactly at e=2, PASS 3)
    w = len(ghosts)
    for i in range(w, len(moves)):
        cost, q, r, kind = moves[i]
        check(q == lock, f"seed {seed}: post-lock pick {q} != {lock}")
        Nf_i, lam_i = states[i]
        e = Nf_i[lock]
        v = lam_i.get(lock, 0)
        if lock == 2:
            check(e == 2 or v == e - 2,
                  f"seed {seed}: 2-invariant broken (e={e}, v={v})")
            if i > w and e != 4:  # the one allowed cost-4 step is e 2->4
                check(cost == 2, f"seed {seed}: post-lock 2-cost {cost}")
        else:
            check(v == e - 1,
                  f"seed {seed}: invariant broken (q={lock}, e={e}, v={v})")
            if i > w:
                check(cost == lock,
                      f"seed {seed}: post-lock cost {cost} != {lock}")
print("  2000 seeds: first non-ghost pick locks; invariant holds;")
print("  ghosts increasing, dividing lambda(seed), within omega_odd")

# =========================================================
print("=" * 64)
print("S4: SEED REPRODUCTION (reference table)")
print("=" * 64)

REF = {2: 2, 3: 3, 5: 5, 6: 3, 10: 5, 21: 5, 30: 3, 105: 5,
        210: 5, 2310: 7, 30030: 7}
for seed, expected in sorted(REF.items()):
    ghosts, lock, _, _ = run_trajectory(seed, 12)
    check(lock == expected, f"seed {seed}: lock {lock} != reference {expected}")
    check(ghosts == [], f"seed {seed}: unexpected wander {ghosts}")
    print(f"  seed {seed:>6} -> lock {lock} (wander 0)  == reference")

# =========================================================
print("=" * 64)
print("S5: WANDER SPECIMENS (frozen PR4)")
print("=" * 64)

SPECIMENS = [(1, [], 3), (11, [5], 7), (71, [5, 7], 17),
             (20231, [5, 7, 17], 19)]
check(is_prime_mr(20231), "20231 not prime")
for seed, exp_ghosts, exp_lock in SPECIMENS:
    ghosts, lock, moves, _ = run_trajectory(seed, 12)
    check(ghosts == exp_ghosts,
          f"seed {seed}: ghosts {ghosts} != {exp_ghosts}")
    check(lock == exp_lock, f"seed {seed}: lock {lock} != {exp_lock}")
    print(f"  seed {seed:>6} -> ghosts {ghosts} -> LOCK {lock}")
# seed 1's trajectory is the 3-adic column from the void
_, _, moves1, states1 = run_trajectory(1, 3)
check([m[1] for m in moves1] == [3, 3, 3], "seed 1 not 3-adic")
check(dict_to_int(states1[2][0]) == 27, "seed 1 traj != 1,3,9,27")
print("  seed      1 trajectory: 1 -> 3 -> 9 -> 27 (the void's column)")

# =========================================================
print("=" * 64)
print("S6: THE LOCK CENSUS (seeds 1..20000, measured)")
print("=" * 64)

lock_hist = {}
wander_hist = {}
min_seed = {}
max_wander, max_wander_seed = -1, None
for seed in range(1, SWEEP + 1):
    Nf0 = factorize(seed) if seed > 1 else {}
    lam0 = carmichael_dict(Nf0)
    omega_odd = sum(1 for p in lam0 if p != 2)
    ghosts, lock, _, _ = run_trajectory(seed, omega_odd + 1)
    check(lock is not None, f"census seed {seed}: no lock in bound")
    lock_hist[lock] = lock_hist.get(lock, 0) + 1
    w = len(ghosts)
    wander_hist[w] = wander_hist.get(w, 0) + 1
    if lock not in min_seed:
        min_seed[lock] = seed
    if w > max_wander:
        max_wander, max_wander_seed = w, seed
print(f"  locks: {dict(sorted(lock_hist.items()))}")
print(f"  wander: {dict(sorted(wander_hist.items()))}")
print(f"  max wander {max_wander} (least specimen seed {max_wander_seed})")
print(f"  minimal seed per lock target: "
      f"{dict(sorted(min_seed.items()))}")

# =========================================================
print("=" * 64)
print("S8: LOCK-TARGET COMPLETENESS — the Linnik blockers (q <= 47)")
print("=" * 64)

from math import gcd as _gcd
for q in [p for p in PRIMES if p <= 47]:
    if q in (2, 3):
        seed = q
        P = None
    else:
        M = 1
        for p in PRIMES:
            if p > q:
                break
            M = M * (p - 1) // _gcd(M, p - 1)
        check(M % q != 0, f"q={q}: q divides M")
        # the general proof's enriched blocker B (finding 7) is a
        # no-op in range: M already carries every needed r-power
        B = M
        for r in PRIMES:
            if r >= q:
                break
            c = 0
            while r ** (c + 2) <= q:
                c += 1
            B = B * (r ** c) // _gcd(B, r ** c)
        check(B == M, f"q={q}: enrichment changed the blocker in range")
        k = 1
        while True:
            P = k * M + 1
            if k % q != 0 and P != q and is_prime_mr(P):
                break
            k += 1
        seed = q * P
        lamd = carmichael_dict(factorize(seed))
        check(dict_to_int(lamd) == P - 1, f"q={q}: lambda != P-1")
    ghosts, lock, _, _ = run_trajectory(seed, 8)
    check(lock == q, f"q={q}: blocker seed locks {lock}")
    check(ghosts == [], f"q={q}: blocker seed wanders {ghosts}")
    tag = f"(P = {P})" if P else "(bare seed)"
    print(f"  q = {q:>2}: seed {seed} locks {q}, wander 0 {tag}")

print("=" * 64)
print(f"TOTAL {CHECKS} checks, all passed")
