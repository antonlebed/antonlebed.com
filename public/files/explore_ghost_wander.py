"""THE GHOST-WANDER LEDGER -- pricing the cascade boundary's one
unpriced quantity, the wander rate, and widening its carrier supply.

THE QUESTION. The cascade boundary (explore_module_law.py C) reduces
lock existence for all char-0 trajectories to ruling out an infinite
carrier ladder: a non-locking trajectory needs, at every stage, a fresh
carrier of norm m*p^(v+1)+1 with m < p^(1+w), CHEAPER THAN THE VIRGIN
p-DOOR. explore_bridge_reach.py R4 killed every CENSUSED cap M at a
certified all-miss exponent A(p, M) and priced the escape: in a
Cramer-type model a ladder survives only if its cap grows >~ v*ln v --
wander at least LOGARITHMIC in depth. So the open content is whether
the dynamics can pay log-depth wander along a trajectory: w has never
been read off the state at all. This rig reads it.

THE HAND-DERIVATION (pre-engine, on disk in passes). Two steps.

  (1) WHERE v_p(lambda) CAN RISE. lambda = lcm over seated places Q at
      depth e of N(Q)^(e-1) * (N(Q) - 1). Deepening a place over a
      residue char other than p adds only powers of that char, so it
      leaves v_p(lambda) alone; deepening the p-column itself is the
      lock. Hence v_p(lambda) = max over seated Q of residue char != p
      of v_p(N(Q) - 1), and only an OPENING can raise it.

  (2) THE BUDGET INEQUALITY. An opening is paid at face value N(Q), and
      the ladder premise is that it undercuts the virgin p-door,
      N(Q) < p^(v_p(lambda)+2). For any integer X >= 2 the p-part of
      X-1 divides X-1, so p^(v_p(X-1)) <= X - 1 < X; at X = N(Q) that
      gives v_p(N(Q) - 1) < log_p N(Q) < v + 2, hence

          v_p(N(Q) - 1) <= v + 1.

      No affordable move raises v_p(lambda) by more than ONE step. The
      carrier exponent is therefore v+1 exactly, w = v_p(lambda) - v is
      pinned at 0, and the cap is p at every stage, forever.

  The inequality reads only the SIZE of a door, never its shape, so no
  residue-degree or lifting-the-exponent route escapes it.

THE ESCAPE THE CENSUS DID NOT ENUMERATE. If w = 0 the ladder runs at
cap M = p and should die at once against the census -- but the census
enumerates carriers over PRIMES, and in a general char-0 ring a place's
norm is a prime POWER. The carrier condition is on the NORM, so the
supply is {m*p^(v+1)+1 : m canonical, m < p} intersected with the prime
POWERS, strictly wider. It bites immediately: at p = 2, v = 2 the prime
carrier 2^3+1 = 9 is composite, and 9 = 3^2 is the norm of an inert
place over 3 in a quadratic field -- a rung the prime census certifies
dead is alive over a ring.

PREDICTIONS (fixed before any engine code; hand-derived above).
  H1 (positive control, the parent's own values): BR.first_all_miss
     reproduces A(2,8) = 9, A(3,9) = 11, A(5,25) = 9.
  H2 (positive control, the engine): explore_lock_prime.py's census
     specimens reproduce through the imported trajectory engine --
     seed 11 -> ghosts [5], lock 7; seed 71 -> [5, 7], lock 17;
     seed 20231 -> [5, 7, 17], lock 19.
  H3 (the budget inequality on real dynamics; rule): along greedy
     trajectories, at EVERY move and for EVERY prime p not seated in
     the state, v_p(lambda) rises by at most 1. This is not vacuous --
     greedy takes the cheapest move, so every move undercuts every
     virgin door, which is exactly the hypothesis of (2). KILL
     OBSERVABLE: the printed maximum single-move rise over the sweep.
     Predicted 1; any 2 refutes the derivation.

  H3 FIRED, AND THE KILL IS THE FINDING (recorded pre-correction;
  the prediction above stands verbatim as the original record). The
  sweep printed a rise of 2: seed 31, p = 2, the move opening 17 at
  cost 17, v_2(lambda) 2 -> 4. The derivation read the virgin p-door
  as p^(V+2) for every p, and at p = 2 that is wrong -- the 2-adic
  unit group carries an extra Z/2, so lambda(2^d) = 2^(d-2) for
  d >= 3 and the virgin 2-door costs 2^(V+3), not 2^(V+2). The
  inequality itself is untouched (it reads only the door's SIZE); what
  changes is the size. Restated:

      v_p(lambda) rises by at most ONE step per move at odd p, and by
      at most TWO at p = 2.

  So the excess is unbuyable at every odd characteristic and costs
  exactly one unit at p = 2 -- and banking that unit needs a prime
  power of norm 2^(V+2)+1 inside the budget, with the multiplier
  pinned to 1: a FERMAT number. The corrected sections H4-H6 read the
  door from explore_lock_prime.py's own menu instead of assuming it.

  H4 (the excess brute-scanned, NO carrier form assumed): at the
     door's real budget D_p(V) enumerate EVERY prime power n < D_p(V)
     and take the largest v_p(n-1) any of them reaches. Predicted
     V+1 at odd p and V+2 at p = 2, at every row; anything higher
     refutes the corrected inequality and reopens the wander.
  H5 (the walk; the kill frozen as an observable, not a meaning): walk
     the ladder on the state variable that actually matters, V =
     v_p(lambda). A rung must STRICTLY raise V -- otherwise the p-door
     never rises and the move costs cannot diverge, which is the
     absorption theorem's lock. So each rung takes the affordable
     prime-power norm maximizing v_p(n-1), and the walk ends where
     none exists. Printed per rung: the carrier with its
     factorization, V, the wander w = V - v, and the Cramer survival
     line log_p(v*ln v). The walk starts at V = 1, the generic state
     in which the characteristic is already once in lambda; a V = 0
     start only prepends a rung. PREDICTED (hand-walked in advance
     under the corrected door):
       p = 2 dies at V = 8, trace V = 1, 3, 4, 5, 6, 8 -- carriers
         9 = 3^2, 17, 97, 193, 257, then all-miss at 513 = 3^3*19,
         1025 = 5^2*41, 1537 = 29*53;
       p = 3 dies at V = 2, trace V = 1, 2 -- carrier 19, then
         all-miss at 28 = 2^2*7, 55 = 5*11;
       p = 5 dies at V = 3, trace V = 1, 2, 3 -- carriers 101 then
         251, then all-miss at 626 = 2*313, 1251 = 3^2*139,
         1876 = 2^2*7*67, 2501 = 41*61.
     Every death is UNCONDITIONAL -- a printed factorization of every
     candidate. The wander observable: max w over the walk, against
     the survival line it would have to beat.
  H6 (the widening is real, not cosmetic): the carrier supply is the
     NORMS, which in a general char-0 ring are prime POWERS, so at
     least one rung must be carried by a prime power that is not
     prime. Predicted witness: p = 2, the norm 9 = 3^2 -- the rung the
     PRIME census certifies dead (2^3+1 composite) and a ring walks.

DESIGN. Primitives are IMPORTED, never reimplemented:
explore_bridge_reach.py for the canonical multipliers, the
deterministic-below-3.317e24 Miller-Rabin, composite certification and
first_all_miss; explore_lock_prime.py for the door menu, the greedy
step and the trajectory engine. explore_lock_prime.py runs its own
suite at import, so it is imported with stdout redirected -- its own
asserts still fire, and a failure there fails this run too. The ladder
walk is a plain integer loop; the widened-supply test factorizes each
candidate by trial division and prints the split. Est. well under a
minute, far under 512 MB, no numpy.

FINDINGS (printed output copied from the run).

1. THE BUDGET INEQUALITY, AND THE ONE UNIT p = 2 SELLS (rule, proved;
   verified over 5,656 greedy moves x 46 unseated primes and by brute
   scan over the 26,152 prime powers below 300,000). v_p(lambda) rises
   only at an OPENING (deepening a place over another residue char
   adds only that char's powers; deepening the p-column is the lock),
   an opening is paid at face value N(Q), and a non-locking trajectory
   pays less than the virgin p-door. Since p^(v_p(X-1)) divides X-1,
   v_p(N(Q) - 1) < log_p N(Q) < log_p(door). So:

     ODD p: door p^(V+2), so v_p(lambda) rises by AT MOST ONE per
     move -- the excess is UNBUYABLE and the cap is pinned at p.
     p = 2: the 2-adic unit group's extra Z/2 makes lambda(2^d) =
     2^(d-2), the door 2^(V+3), and the rise AT MOST TWO -- exactly
     one unit of excess, and no more.

   Those two door values are Z's, and they TRANSFER to any char-0 ring
   for the reason the reduction restricts to rank-1 places in the first
   place: a rank-1 place is unramified of residue degree 1, so its
   completion is Q_p exactly and its unit filtration is Z_p's verbatim.
   Nothing in the argument is rational beyond that.

   Measured maxima over the sweep: 2 at p = 2 (witness seed 31, the
   move opening 17 at cost 17, v_2(lambda) 2 -> 4), 1 at p = 3 and
   p = 5. The door formula agreed with explore_lock_prime.py's own
   menu at 40,753 of 40,753 real states, the lambda(4) = lambda(8)
   hiccup included (V = 0 sits at door 4, not 8). The inequality reads
   only the door's SIZE, never its shape, so no residue-degree or
   lifting-the-exponent route escapes it.

2. THE WANDER RATE IS PRICED, AND ITS CURRENCY IS A NAMED CONJECTURE
   (rule). The unpriced quantity was w = v_p(lambda) - v, the excess
   the cap p^(1+w) is read off -- which is NOT the ghost wander
   explore_lock_prime.py bounds by omega_odd(lambda(seed)). That one
   counts openings before a lock; this one is a valuation gap. They
   share a word because the ghost DOWRY is the mechanism proposed for
   moving the second, and the inequality is what refutes the proposal.
   Finding 1 pins its per-move growth at 0 for odd p and at most 1 for
   p = 2, and the p = 2 unit is not free
   either: banking it needs an affordable prime power of norm
   2^(V+2)+1, whose multiplier the budget pins to 1. And the numbers
   2^k+1 that are prime powers are EXACTLY the Fermat primes together
   with 9 = 2^3+1 -- a prime 2^k+1 forces k to be a power of 2, and
   Mihailescu leaves 9 as the only proper power (computed here for
   k <= 40: k = 1, 2, 3, 4, 8, 16). So the p = 2 excess supply is that
   list and nothing else: log-depth wander needs infinitely many
   Fermat primes, which five known members make a supply widely
   believed FINITE, while at every odd p it is impossible outright.
   The cascade boundary's escape hatch is therefore the SAME object
   the alphabet family already puts at its bottom (finding 2 of
   explore_bridge_reach.py, S = {2} stalling at 6): two independent
   routes through this corpus land on Fermat.

3. THE CARRIER SUPPLY WAS UNDERCOUNTED -- NORMS ARE PRIME POWERS
   (observation, one witness sufficient). The census enumerates
   carriers over PRIMES, but the carrier condition is on a place's
   NORM, which in a general char-0 ring is a prime POWER. The p = 2,
   V = 1 rung is carried by 9 = 3^2 -- the norm of an inert place over
   3 in a quadratic field, and a rung the prime census certifies dead
   (2^3 + 1 composite). The widened supply is what the walk below
   uses, so the deaths it certifies survive the correction.

4. THE WALK DIES IN ALL THREE CHARACTERISTICS, UNCONDITIONALLY (rule;
   printed factorization of every candidate, so no primality claim is
   load-bearing on the kill side). Walking the state variable that
   matters -- V = v_p(lambda), each rung taking the affordable
   prime-power norm that banks the most. That is an upper envelope and
   not merely one policy: raising V raises the THRESHOLD v_p(n-1) > V
   as well as the budget, so neither candidate set contains the other,
   but every value ABOVE V+1 that state V could reach is still
   reachable from V+1 under the larger budget, and the only value
   forgone is the state just left. Driving V maximally therefore
   reaches every V any policy reaches, one or more rungs sooner --
   and rung count is irrelevant to a question about an INFINITE
   ladder:
     p = 2: V trace 1, 3, 4, 5, 6, 8 via 9 = 3^2, 17, 97, 193, 257 --
       then ALL-MISS under the door 2^11 = 2048: 513 = 3^3*19,
       1025 = 5^2*41, 1537 = 29*53.
     p = 3: V trace 1, 2 via 19 -- then ALL-MISS under 3^4 = 81:
       28 = 2^2*7, 55 = 5*11.
     p = 5: V trace 1, 2, 3 via 101, 251 -- then ALL-MISS under
       5^5 = 3125: 626 = 2*313, 1251 = 3^2*139, 1876 = 2^2*7*67,
       2501 = 41*61.
   Every V trace and every death was hand-walked in advance and
   reproduced exactly. And the death is terminal rather than a stall:
   once v_p(lambda) is stuck the p-door is stuck, so every later move
   costs less than that fixed door forever; a move on a place costs at
   least that place's norm, and a norm-finite ring has finitely many
   places under a fixed ceiling, so some place is picked infinitely
   often at bounded cost and ABSORBS the tail (explore_module_law.py
   B(i), whose norm-finiteness hypothesis is what the pigeonhole
   step spends) -- which is the lock.

5. WHAT THIS DOES TO THE BOUNDARY (scope stated exactly). Modulo the
   explore_module_law.py C reduction, cited and not re-derived: a
   char-0 trajectory with a rank-1 place over 2, 3 or 5 LOCKS,
   unconditionally. Every number ring has rank-1 places at infinitely
   many chars (Chebotarev), so the open content is no longer a wander
   RATE at all -- it is the residual family of rings whose rank-1
   chars all avoid 2, 3 and 5, and for each such char the walk is a
   finite computation of the same shape, at cap p rather than at the
   unbounded cap the census had to sweep. The reading against the
   Cramer line is now moot where it used to be the whole question: at
   p = 2 the walk banks w = 3 over its 5 rungs against a survival line
   of 3.01 -- tracking it, because Fermat primes are dense at small
   exponents -- and then dies outright rather than falling behind.

6. THE NAMED CANDIDATE MECHANISM IS THIS WALK, AND THE KILL IS THE
   BUDGET (rule). explore_lock_prime.py's HONEST SCOPE names a
   candidate 2-adic ghost ladder -- "5, 17, 97, 193, 257, 7681, ...:
   each the least prime with v2(p-1) exceeding the accumulated dowry"
   -- with the bookkeeping called delicate and no construction
   claimed. It is this walk with the affordability constraint dropped,
   and the walk's carriers are that list with 9 = 3^2 in place of 5.
   Every named rung IS prime, 7681 included, so the ladder does not
   die for want of primes: at V = 8 the next rung must exceed
   v_2 = 8, and 7681 does (7680 = 2^9*3*5) -- while costing 7681
   against a door of 2^11 = 2048 it has to undercut. The supply is
   there and the budget is not, which is the whole content of the
   inequality read on a specimen.

RUN RECORD (this file, ~40 s, 0 failures, well under 512 MB, no numpy;
every section asserts). PRE-GREEN, and the kill is the finding: H3 was
frozen as "no move raises v_p(lambda) by more than one step" and FIRED
on the first run at seed 31, p = 2 -- the hand-derivation had read the
virgin 2-door as 2^(V+2) where the 2-adic unit group charges 2^(V+3).
The prediction stands verbatim above with the correction beneath it;
the inequality survived and its p = 2 row changed, which is what
promoted finding 2 from "the wander is nil" to "the wander costs a
Fermat number". A second pre-green: the door formula's V = 0 row at
p = 2 (the lambda(4) = lambda(8) hiccup), caught by the same control
against explore_lock_prime.py's menu. H4 was amended PRE-RUN from an
asserted constant to a brute scan over every prime power below the
door -- a section that asserts its own derivation measures nothing.
Predictions H1, H2, H5 and H6 held exactly, including all three
hand-walked V traces and death values.

Related scripts: explore_bridge_reach.py (the census and the model
threshold), explore_cascade_caps.py (the next caps),
explore_module_law.py (the reduction this rig's premise is quoted
from), explore_lock_prime.py (the door menu, the wander bound over Z).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import io
from contextlib import redirect_stdout
from math import log

import explore_bridge_reach as BR

BR.SMALL_PRIMES = [n for n in range(2, 5000)
                   if all(n % q for q in range(2, int(n ** 0.5) + 1))]

# explore_lock_prime.py runs its own suite at import; its asserts still
# fire, so a break there breaks this run too.
_buf = io.StringIO()
with redirect_stdout(_buf):
    import explore_lock_prime as LP

FAIL = [0]


def ok(cond, msg):
    print(("  [ok] " if cond else "  [FAIL] ") + msg)
    if not cond:
        FAIL[0] += 1
    assert cond, msg


def vp(n, p):
    """p-adic valuation of n."""
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def factor_split(n):
    """Full factorization by trial division over BR.SMALL_PRIMES, with
    the cofactor tested for primality. -> dict, or None if a composite
    cofactor survives the trial range."""
    f, m = {}, n
    for q in BR.SMALL_PRIMES:
        if q * q > m:
            break
        while m % q == 0:
            f[q] = f.get(q, 0) + 1
            m //= q
    if m > 1:
        if not BR.is_primeZ(m):
            return None
        f[m] = f.get(m, 0) + 1
    return f


def is_prime_power(n):
    """-> (True, printable split) if n = q^a, else (False, split)."""
    f = factor_split(n)
    if f is None:
        return False, "cofactor not certified"
    split = "*".join(f"{q}^{a}" if a > 1 else str(q)
                     for q, a in sorted(f.items()))
    return len(f) == 1, split


print("=" * 72)
print("H1 CONTROL: the parent census reproduces through its own primitives")
print("=" * 72)

for (p, M), want in [((2, 8), 9), ((3, 9), 11), ((5, 25), 9)]:
    got = BR.first_all_miss(p, M, 300)
    print(f"  A({p},{M}) = {got}")
    ok(got == want, f"H1: A({p},{M}) = {want} reproduced")

print()
print("=" * 72)
print("H2 CONTROL: the trajectory engine reproduces the wander specimens")
print("=" * 72)

for seed, want_g, want_lock in [(11, [5], 7), (71, [5, 7], 17),
                                (20231, [5, 7, 17], 19)]:
    ghosts, lock, moves, states = LP.run_trajectory(seed, 12)
    print(f"  seed {seed:>6}: ghosts {ghosts} -> lock {lock}")
    ok(ghosts == want_g and lock == want_lock,
       f"H2: seed {seed} reproduces ghosts {want_g}, lock {want_lock}")

print()
print("=" * 72)
print("H3 THE BUDGET INEQUALITY ON REAL DYNAMICS")
print("  every move of a greedy trajectory undercuts every virgin door,")
print("  so no move may raise v_p(lambda) by more than one step")
print("=" * 72)

SEEDS = list(range(1, 401)) + [5237, 20231, 2310, 30030]
STEPS = 14
WATCH = [q for q in LP.PRIMES if q < 200]

def door_exp(p, V):
    """The virgin p-door's exponent when (p-1) | lambda: p^door_exp.
    Odd p: lambda(p^d) = p^(d-1)(p-1), so escaping v_p = V needs
    d = V+2. p = 2: the extra Z/2 makes lambda(2^d) = 2^(d-2) for
    d >= 3, so escaping needs d = V+3 -- except at V = 0, where
    lambda(4) = 2 already escapes and the door is 4 (the
    lambda(4) = lambda(8) hiccup explore_lock_prime.py froze
    pre-run). Controlled below against that script's own door()."""
    if p != 2:
        return V + 2
    return 2 if V == 0 else V + 3


worst = {}                 # p -> (rise, witness)
moves_seen, doors_checked = 0, 0
for seed in SEEDS:
    Nf = LP.factorize(seed) if seed > 1 else {}
    lamd = LP.carmichael_dict(Nf)
    for _ in range(STEPS):
        best, Nf2, lamd2 = LP.step(Nf, lamd)
        for p in WATCH:
            if p in Nf2:            # seated: deepening it is the lock
                continue
            V = lamd.get(p, 0)
            rise = lamd2.get(p, 0) - V
            bound = door_exp(p, V) - 1 - V   # 1 at odd p, 2 at p = 2
            ok_rise = rise <= bound
            if not ok_rise:
                FAIL[0] += 1
                print(f"  [FAIL] p = {p}, V = {V}: rise {rise} > {bound}"
                      f" (seed {seed}, move {best})")
            if rise > worst.get(p, (0, None))[0]:
                worst[p] = (rise, (seed, best, V, lamd2.get(p, 0)))
            # the door control: the formula against the engine's menu
            if LP.divides(LP.lam_pp_factors(p, 1), lamd):
                ok_exp = LP.door(p, 0, lamd)
                assert ok_exp == door_exp(p, V), (
                    f"door formula wrong at p = {p}, V = {V}: "
                    f"menu {ok_exp}, formula {door_exp(p, V)}")
                doors_checked += 1
        Nf, lamd = Nf2, lamd2
        moves_seen += 1

print(f"  {len(SEEDS)} seeds x {STEPS} moves = {moves_seen} moves, "
      f"{len(WATCH)} unseated primes watched per move")
print(f"  door formula vs explore_lock_prime.py's menu: "
      f"{doors_checked} agreements, 0 disagreements")
print("     p   max single-move rise in v_p(lambda)   witness")
for p in sorted(worst):
    rise, wit = worst[p]
    s, mv, a, b = wit
    print(f"    {p:>2}   {rise:>34}   seed {s}, move "
          f"{mv[1]}^{mv[2]} cost {mv[0]}, v_p {a} -> {b}")
odd_max = max(worst[p][0] for p in worst if p != 2)
ok(odd_max <= 1,
   f"H3: at every ODD p the rise is at most 1 per move (max {odd_max})")
ok(worst.get(2, (0,))[0] <= 2,
   f"H3: at p = 2 the rise is at most 2 per move "
   f"(max {worst.get(2, (0,))[0]})")
ok(FAIL[0] == 0, "H3: every move obeys its own per-V budget bound")

print()
print("=" * 72)
print("H4 THE EXCESS, BRUTE-SCANNED -- no carrier form assumed")
print("  at the door's own budget, the largest v_p(n-1) any prime power")
print("  n < door reaches, against the bound the door's SIZE forces")
print("=" * 72)

SCAN_LIMIT = 300_000
SPF = BR.build_spf(SCAN_LIMIT)


def prime_power_below(limit):
    """Every prime power 2 <= n < limit, via the parent's SPF sieve."""
    out = []
    for n in range(2, limit):
        f = BR.spf_factor(n)
        if len(f) == 1:
            out.append(n)
    return out


PP = prime_power_below(SCAN_LIMIT)
print(f"  {len(PP)} prime powers below {SCAN_LIMIT}")

for p in (2, 3, 5):
    print(f"  p = {p}:")
    print("      V   door p^d, d =   budget   max v_p(n-1)   bound")
    V = 1
    while p ** door_exp(p, V) <= SCAN_LIMIT:
        B = p ** door_exp(p, V)
        best = max(vp(n - 1, p) for n in PP if n < B)
        bound = door_exp(p, V) - 1
        print(f"    {V:>3}   {door_exp(p, V):>13}   {B:>6}   "
              f"{best:>12}   {bound:>5}")
        ok(best <= bound,
           f"H4: p = {p}, V = {V}: no affordable prime power exceeds "
           f"v_p = {bound} (max {best})")
        V += 1

print()
print("=" * 72)
print("H5/H6 THE LADDER WALK at the pinned cap, over PRIME-POWER norms")
print("  each rung: the affordable carriers are m*p^(V+1)+1, m < p;")
print("  w = V - v is what the walk actually banks")
print("=" * 72)

RUNG_CAP = 40
walks = {}
for p in (2, 3, 5):
    print(f"  p = {p}:")
    print("      v      V   carrier (norm = factorization)"
          "            w   log_p(v*ln v)")
    V, death, witnesses, maxw, trace = 1, None, [], 0, [1]
    for v in range(1, RUNG_CAP + 1):
        B = p ** door_exp(p, V)
        cands = [n for n in range(2, B) if vp(n - 1, p) > V]
        hits, misses = [], []
        for n in cands:
            pp, split = is_prime_power(n)
            (hits if pp else misses).append((n, split))
        if not hits:
            print(f"    {v:>3}   {V:>4}   ALL-MISS under door p^"
                  f"{door_exp(p, V)} = {B} -- " + "; ".join(
                      f"{n} = {split}" for n, split in misses))
            death = V
            break
        n, split = max(hits, key=lambda h: vp(h[0] - 1, p))
        V = vp(n - 1, p)
        trace.append(V)
        w = V - v
        maxw = max(maxw, w)
        need = log(v * log(v)) / log(p) if v >= 2 else 0.0
        tag = "" if BR.is_primeZ(n) else "   (prime power, NOT prime)"
        print(f"    {v:>3}   {V:>4}   {n} = {split}{tag}"
              f"{'':>{max(1, 26 - len(split) - len(tag))}}{w:>3}   "
              f"{need:>8.2f}")
        if not BR.is_primeZ(n):
            witnesses.append((v, n, split))
    walks[p] = (death, maxw, witnesses, trace)
    print(f"    V trace: {trace}, dies at V = {death}, max w = {maxw}")
    ok(death is not None,
       f"H5: p = {p} the walk dies at a certified V <= {RUNG_CAP}")

print()
for p, want_death, want_trace in ((2, 8, [1, 3, 4, 5, 6, 8]),
                                  (3, 2, [1, 2]),
                                  (5, 3, [1, 2, 3])):
    death, maxw, _, trace = walks[p]
    ok(death == want_death,
       f"H5: p = {p} dies at V = {want_death} as hand-walked (got {death})")
    ok(trace == want_trace,
       f"H5: p = {p} V trace {want_trace} as hand-walked (got {trace})")

print()
print("  THE WANDER, read against the line it would have to beat:")
for p in (2, 3, 5):
    death, maxw, _, trace = walks[p]
    rungs = len(trace) - 1
    need = log(rungs * log(rungs)) / log(p) if rungs >= 2 else 0.0
    print(f"    p = {p}: max w = {maxw} over {rungs} rungs; the Cramer "
          f"survival line at that depth is {need:.2f}")

allwit = [(p, v, n, s) for p in walks for v, n, s in walks[p][2]]
print(f"  widening witnesses (prime-power carriers that are NOT prime): "
      f"{[(p, n, s) for p, v, n, s in allwit]}")
ok(any(p == 2 and n == 9 for p, v, n, s in allwit),
   "H6: the norm 9 = 3^2 carries a p = 2 rung -- the widening is real")

print()
print("=" * 72)
print("H7 THE NAMED CANDIDATE MECHANISM IS THIS WALK, and it dies on")
print("  BUDGET rather than on primes")
print("=" * 72)

# explore_lock_prime.py's HONEST SCOPE names a candidate 2-adic ghost
# ladder -- "5, 17, 97, 193, 257, 7681, ...: each the least prime with
# v2(p-1) exceeding the accumulated dowry" -- with the bookkeeping
# called delicate and no construction claimed. It is this walk without
# the affordability constraint.
CANDIDATE = [5, 17, 97, 193, 257, 7681]
for n in CANDIDATE:
    print(f"    {n}: prime {BR.is_primeZ(n)}, v_2(n-1) = {vp(n - 1, 2)}")
ok(all(BR.is_primeZ(n) for n in CANDIDATE),
   "H7: every named candidate rung is prime -- the supply is not the "
   "obstruction")
walk_carriers = [9, 17, 97, 193, 257]
print(f"  the walk's own carriers: {walk_carriers} -- the named list "
      f"with 9 = 3^2 in place of 5")
V_last = vp(257 - 1, 2)
door_last = 2 ** door_exp(2, V_last)
print(f"  at V = {V_last} the door is 2^{door_exp(2, V_last)} = "
      f"{door_last}, and the next named rung 7681 (v_2 = "
      f"{vp(7681 - 1, 2)}) costs {7681} > {door_last}")
ok(vp(7681 - 1, 2) > V_last and 7681 > door_last,
   "H7: the ladder's next rung supplies the valuation and EXCEEDS the "
   "door it must undercut -- the kill is the budget, not the primes")

print()
print("=" * 72)
print(f"TOTAL FAILURES: {FAIL[0]}")
print("=" * 72)
