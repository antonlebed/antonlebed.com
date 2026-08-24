"""THE CASCADE BOUNDARY, CHARACTERISTIC BY CHARACTERISTIC -- sweeping
the pinned-cap ladder's death rung over every small odd characteristic,
and shrinking the residual the three-characteristic close left behind.

THE QUESTION. explore_ghost_wander.py closed the cascade boundary at
p = 2, 3 and 5: the budget inequality pins the ladder's cap at p, and
at those three characteristics the walk at the pinned cap dies at a
certified rung. What it left open is the RESIDUAL -- rings whose
rank-1 characteristics avoid all three. Two things are already known
about that residual, and this rig acts on both.

  (a) Each further characteristic is a finite computation of the SAME
      shape, at cap p rather than at the unbounded cap the census had
      to sweep. So the residual shrinks one characteristic at a time,
      and nothing but arithmetic stands in the way.
  (b) The reduction (explore_module_law.py C) demands a carrier at
      EVERY characteristic carrying a rank-1 place -- a conjunction
      over infinitely many characteristics of which breaking ONE
      suffices. So a ring is closed the moment ANY ONE of its rank-1
      characteristics is closed, and a sweep over an initial segment of
      the primes closes every ring that has a rank-1 characteristic
      inside that segment.

So the question this rig asks is: how far does the initial segment go,
and does every characteristic in it die?

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE SUPPLY IS p-1 EXPLICIT NUMBERS PER RUNG, not a range scan.
      At rung V the affordable carriers are the norms n < p^(V+2) (the
      virgin door, odd p) with v_p(n-1) > V. Writing n - 1 = m*p^(V+1),
      the door gives m*p^(V+1) + 1 < p^(V+2), hence m < p - p^-(V+1),
      hence 1 <= m <= p-1. Conversely every such m clears the door. So

          supply(p, V) = {m*p^(V+1) + 1 : 1 <= m <= p-1}

      exactly -- p-1 numbers, generated directly. The parent rig scans
      range(2, p^(V+2)) for the same set, which is why it reaches
      p = 5 and no further; direct generation is O(p) per rung and the
      sweep below is what that buys.

  (2) HALF THE SUPPLY IS ALL BUT DEAD, BY PARITY. For odd p, p^(V+1)
      is odd, so m*p^(V+1) + 1 is EVEN exactly when m is ODD. An even
      prime power is a power of 2, so an odd multiplier contributes a
      carrier only when m*p^(V+1) + 1 = 2^t, i.e. m*p^(V+1) = 2^t - 1,
      which forces p^(V+1) | 2^t - 1 with 2^t < p^(V+2) -- so
      t < (V+2)*log_2(p) while ord_{p^(V+1)}(2) divides t. The
      effective supply is therefore the floor((p-1)/2) EVEN
      multipliers plus a thin exceptional set, and the exceptions are
      countable rather than estimated: this rig prints every one it
      meets. (At V = 0 the smallest is already visible by hand:
      p = 3, m = 1 gives 4 = 2^2. The rungs this rig walks start at
      V = 1, where the parent's own trace starts.)

  (3) WHY A DEATH IS EXPECTED AT ALL, AND ROUGHLY WHERE. The p-1
      candidates at rung V sit just under p^(V+2), so a prime-power
      count heuristic gives about (p-1)/((V+2)*ln p) hits per rung,
      falling below 1 near V ~ (p-1)/ln p. That is a HEURISTIC and it
      is the margin, not the kill: the kill below is the printed
      all-miss, and the heuristic is scored separately so that a miss
      against it costs a prediction and never a verdict.

  (4) WHY THE ANALYTIC ROUTE CANNOT REPLACE THE SWEEP. Surviving rung
      V asks for a prime power = 1 mod p^(V+1) below p^(V+2) -- a
      prime in an arithmetic progression below only p times its own
      modulus. The GRH least-prime bound in an AP places one below
      about q^2 polylog q, and the unconditional bounds are far weaker,
      so no known theorem reaches a window LINEAR in the modulus. The
      ladder asks for a prime where the analysis cannot promise one and
      cannot refuse one either; the death is certified per rung by
      arithmetic or it is not certified.

  (5) THE PRIME-POWER TEST MUST NOT FACTOR. n is a prime power iff n
      is prime, or n = q^a for some a >= 2 with q prime. The second is
      decided exactly by taking integer a-th roots for
      2 <= a <= log_2 n and testing each root for primality -- no
      factorization, and total for n around p^(V+2). The parent rig
      decides prime-power-ness by trial division with a certified
      cofactor, which returns NOT-A-PRIME-POWER when it merely fails to
      certify; that is safe on its own range and would manufacture
      false deaths on this one, so the test is rebuilt here and
      CONTROLLED against the parent's on the range where the parent's
      is sound. A false death is the failure mode this rig has to fear
      most: it would report the boundary closed where it is open.

PREDICTIONS (fixed before any engine code; hand-derived above).

  H1 (POSITIVE CONTROL, the supply). For p = 3 and 5 and every rung the
     parent walks, direct generation {m*p^(V+1)+1 : 1 <= m <= p-1}
     equals the parent's range scan {n in (2, p^(V+2)) : v_p(n-1) > V},
     as sets. KILL: any disagreement -- the sweep's supply would then
     not be the boundary's supply.
  H2 (POSITIVE CONTROL, the test). The rebuilt prime-power test agrees
     with explore_ghost_wander.py's is_prime_power on every integer
     below AGREE_LIMIT, and the two disagree in exactly one direction on
     a hand-built large specimen: a prime power the parent cannot
     certify. KILL: any n below AGREE_LIMIT where they differ.
  H3 (POSITIVE CONTROL, the verdict). Rebuilt supply plus rebuilt test
     reproduce the parent's published deaths: p = 3 dies at V = 2 and
     p = 5 at V = 3. KILL: either death moves.
  H4 (THE QUESTION; rule if it holds). Every odd prime p <= P_MAX has a
     finite death rung D(p) <= RUNG_CAP: a rung at which all p-1
     candidates are certified non-prime-powers. OBSERVABLE: the printed
     count of swept primes with no death below RUNG_CAP. KILL: that
     count is nonzero -- a characteristic whose ladder is still climbing
     at the ceiling is an OPEN characteristic, and the residual keeps it.
  H5 (THE MARGIN, distrusted by construction). D(p) <=
     2*(p-1)/ln p + 5 for every p swept. OBSERVABLE: the count of
     violations and the worst ratio D(p)*ln p/(p-1). This scores the
     heuristic of (3) and carries no verdict either way.
  H6 (THE PARITY EXCEPTIONS). Every odd-multiplier carrier the sweep
     accepts is a power of 2. OBSERVABLE: the printed list of accepted
     odd-m carriers with their factorizations. KILL: an accepted odd-m
     carrier that is not a power of 2 -- (2) would then be wrong.

WHAT A CLEAN RUN BUYS, and what it does not. It does not prove the
cascade boundary closed: the reduction itself is cited from
explore_module_law.py and read rather than checked there -- it has
SINCE been proved in that section, for the ideal world, so the citation
now carries a scope where it carried a debt -- and the sweep is an
initial segment and not all primes. What it buys is a rule of the
form "the boundary is closed at every characteristic below P_MAX",
which by (b) closes every ring possessing a rank-1 characteristic below
P_MAX -- and that is a statement about RINGS, which is what the residual
was a residual of.

FINDINGS.

  1. THE BOUNDARY IS CLOSED AT EVERY ODD CHARACTERISTIC BELOW 1000
     (rule, verified p <= 1000). All 167 odd primes below 1000 have a
     certified death rung: a rung V where every one of the p-1
     affordable carriers m*p^(V+1)+1 is a certified non-prime-power.
     Deaths run from D(19) = D(23) = 1 to D(719) = 62, and D is
     ERRATIC rather than increasing -- D(17) = 2 sits beside
     D(29) = 8, D(101) = 10 beside D(151) = 12, D(751) = 33 beside
     D(719) = 62. Three controls carry it: the directly generated
     supply equals the parent's range scan at every rung tested (H1),
     the rebuilt prime-power test agrees with the parent's below
     AGREE_LIMIT and departs from it in exactly the safe direction on a
     121-digit specimen (H2), and the parent's published deaths at
     p = 3 and p = 5 reproduce unchanged (H3).

  2. WHAT THIS BUYS IS A STATEMENT ABOUT RINGS, NOT ABOUT PRIMES. By
     the reduction's conjunction (the question, (b) above), a ring is
     closed as soon as ONE of its rank-1 characteristics is closed. So
     every char-0 ring possessing a rank-1 characteristic below 1000
     now has its cascade boundary closed -- which is what the residual
     was a residual OF. What stays open is the rings whose rank-1
     characteristics ALL exceed 1000, and that is a statement about
     splitting behaviour rather than about ladders: it is the front
     this rig hands on, and it is not answered here. (TAKEN SINCE by
     explore_cascade_residual.py: that residual is inhabited at every
     bound -- the primorial field Q(sqrt(2*3*...*P)) ramifies every prime
     <= P -- so no sweep empties it; a uniform close needs only density
     zero, and the retail case is decided by computing L(K).)

  3. THE MARGIN HELD FOR A REASON THE DERIVATION GOT WRONG. H5 passed with ZERO violations and a worst ratio
     of 1.30 at p = 7, which looks like a clean confirmation of
     hand-derivation (3) and is not one. (3) named the rung where the
     EXPECTED hit count falls below 1, about (p-1)/ln p -- 144 at
     p = 997. The observed D(997) = 45. Death is not where the
     expectation crosses 1; it is the FIRST rung whose draw happens to
     come up empty, which under the same model has probability
     exp(-(p-1)/((V+2) ln p)) per rung and therefore arrives far
     earlier than the crossing. The bound was loose by a factor of
     roughly three and passed for that reason. The kill (H4) was
     derived and the margin was vibes, exactly as the guard predicts;
     recorded because a passing margin is the easiest place to bank a
     wrong mechanism.

  4. THE PARITY HALF OF THE SUPPLY IS EMPTY, NOT MERELY THIN (H6).
     Hand-derivation (2) predicted that odd multipliers contribute only
     via m*p^(V+1)+1 = 2^t and expected a countable exceptional set.
     Across the whole sweep -- every rung below every death rung, all
     167 primes -- the number of accepted odd-multiplier carriers is
     ZERO. So the effective supply is the floor((p-1)/2) even
     multipliers exactly, and the ladder is working with half the
     candidates its own cap appears to grant it.

RUN RECORD. 14/14 checks pass. Peak working set 20.3 MB against the
512 MB ceiling, wall 107.6 s under memwatch.py (estimated at a few
minutes for the 1000-sweep; the earlier 150-sweep ran in 2.5 s).
P_MAX = 1000, RUNG_CAP = 120, AGREE_LIMIT = 20,000.

TWO THINGS ABOUT HOW THIS RIG GOT HERE, both recorded because neither
is visible in the code that survived.

  The sweep bound was RAISED from 150 to 1000 after a first clean run,
  not lowered onto a result. H4 quantifies over every odd prime below
  P_MAX, so raising it can only make the prediction harder to satisfy
  and cannot select for a verdict; the 150-sweep's numbers are a prefix
  of the 1000-sweep's, D(149) = 8 and max D = 14 among them. AGREE_LIMIT
  moved the other way, 200,000 to 20,000, during the pre-run
  performance rebuild and before any finding existed -- the parent's
  test trial-divides over ~670 small primes per integer, which is what
  made the control the most expensive line in the rig.

  THE FIRST RUN WAS A RUNAWAY AND THE CAUSE WAS THE FLOAT IN AN INTEGER
  ROUTINE. integer_root seeded its search with int(round(n**(1.0/a))).
  The carriers here pass 10^60 and reach 10^183, where that expression
  is lossy long before it raises OverflowError, so the correction loops
  walked instead of stepping. Rebuilt float-free -- bit-length seed,
  integer Newton -- and the same sweep that failed to finish in ten
  minutes finishes in under two. Floats have no business in this rig at
  any size, which is why isqrt and the integer Newton are the only
  roots taken.
"""

import io
import os
import sys
import contextlib
from math import log, isqrt, gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_bridge_reach as BR

# explore_ghost_wander.py has no __main__ guard, so importing it RUNS the
# parent rig; its output is captured rather than interleaved, and the line
# count is printed so the capture is visible rather than silent. The import
# also has a side effect this rig depends on being visible: the parent
# widens BR.SMALL_PRIMES at its own import time, so the parent's
# certify_composite reaches further here than it does in
# explore_bridge_reach.py run alone -- which makes the H2 control STRICTER,
# the parent being compared at its strongest.
_captured = io.StringIO()
with contextlib.redirect_stdout(_captured):
    import explore_ghost_wander as GW
print(f"    (parent rig imported; {len(_captured.getvalue().splitlines())} "
      f"lines of its output captured, BR.SMALL_PRIMES now reaches "
      f"{BR.SMALL_PRIMES[-1]})")

PASS = []


def ok(cond, label):
    PASS.append(bool(cond))
    print(f"    [{'PASS' if cond else 'FAIL'}] {label}")


# ---------------------------------------------------------------- primitives

def integer_root(n, a):
    """Largest r with r^a <= n. EXACT and float-free by construction:
    the carriers here run past 10^60, where float(n) is either lossy or
    an OverflowError, so the seed comes from the bit length and the
    refinement is integer Newton."""
    if a == 1:
        return n
    if a == 2:
        return isqrt(n)
    r = 1 << (n.bit_length() // a + 1)
    while True:
        nxt = ((a - 1) * r + n // r ** (a - 1)) // a
        if nxt >= r:
            break
        r = nxt
    while r ** a > n:
        r -= 1
    while (r + 1) ** a <= n:
        r += 1
    return r


# Cheap rejection before Miller-Rabin: a candidate sharing a factor with
# this primorial is composite, and one gcd replaces hundreds of trial
# divisions. It cannot reject a prime power q^a with q inside the wheel,
# so the gcd verdict is a HINT and the wheel primes are re-checked as
# possible bases before the candidate is discarded.
WHEEL = [q for q in range(3, 1000) if BR.is_primeZ(q)]
WHEEL_PRODUCT = 1
for _q in WHEEL:
    WHEEL_PRODUCT *= _q


def _power_of(n, q):
    """-> a if n = q^a exactly (a >= 1), else None."""
    a = 0
    while n % q == 0:
        n //= q
        a += 1
    return a if n == 1 else None


def is_prime_power(n):
    """-> (True, 'q^a') if n = q^a with q prime and a >= 1, else
    (False, None). Decided by primality plus EXACT integer roots and a
    small-prime wheel; it never needs a full factorization, so it is
    sound at any size (hand-derivation (5)).

    Three disjoint cases, and each returns a decision rather than a
    failure -- which is the whole difference from the parent's test.
      even n: a prime power iff a power of 2;
      n sharing a factor with the wheel: a prime power iff a power of
        that one wheel prime (two wheel primes dividing n settles it
        NEGATIVELY at once);
      n coprime to the wheel: prime, or q^a with q > 1000 and a >= 2,
        which the integer roots decide exactly."""
    if n < 2:
        return False, None
    if n % 2 == 0:
        a = _power_of(n, 2)
        return (True, f"2^{a}") if a else (False, None)
    g = gcd(n, WHEEL_PRODUCT)
    if g > 1:
        q = next(q for q in WHEEL if g % q == 0)
        a = _power_of(n, q)
        return (True, f"{q}^{a}" if a > 1 else str(q)) if a else (False, None)
    if BR.is_primeZ(n):
        return True, str(n)
    for a in range(2, n.bit_length() + 1):
        r = integer_root(n, a)
        if r < 2:
            break
        if r ** a == n and BR.is_primeZ(r):
            return True, f"{r}^{a}"
    return False, None


def supply(p, V):
    """The affordable carriers at rung V, generated directly."""
    base = p ** (V + 1)
    return [m * base + 1 for m in range(1, p)]


def death_rung(p, rung_cap):
    """First rung V >= 1 at which every candidate in supply(p, V) is a
    certified non-prime-power. -> (V, misses, odd_hits) with odd_hits
    the accepted ODD-multiplier carriers below that rung (H6), or
    (None, None, odd_hits).

    Odd p only: the budget inequality pins the rise at one, so the
    valuation and the rung index coincide and the walk is a scan.

    EVERY candidate at every rung is tested, not just up to the first
    hit: H6 needs the odd-multiplier accepts, and stopping early would
    make that list a function of multiplier ORDER rather than of the
    supply. The death verdict is unaffected -- an all-miss is an
    all-miss either way."""
    odd_hits = []
    for V in range(1, rung_cap + 1):
        base = p ** (V + 1)
        hit = False
        for m in range(1, p):
            n = m * base + 1
            pp, split = is_prime_power(n)
            if pp:
                hit = True
                if m % 2 == 1:
                    odd_hits.append((p, V, m, n, split))
        if not hit:
            return V, supply(p, V), odd_hits
    return None, None, odd_hits


# ------------------------------------------------------------------ soundness
# WHY THE DEATH CERTIFICATE IS A PROOF AND THE SURVIVAL IS NOT, which is
# the direction this rig needs. BR.is_primeZ is Miller-Rabin over fixed
# bases: a COMPOSITE verdict exhibits a witness and is a proof, while a
# PRIME verdict is probable-prime only. A death rung is a conjunction of
# composite verdicts (plus exact not-a-perfect-power), so it is
# certified; a surviving rung rests on a probable prime, which can only
# make a ladder look LONGER than it is. Both errors therefore point away
# from the false death of hand-derivation (5).

P_MAX = 1000
RUNG_CAP = 120
AGREE_LIMIT = 20000

print("=" * 72)
print("H1/H2/H3 CONTROLS: supply, test, and the parent's published deaths")
print("=" * 72)

for p in (3, 5):
    for V in range(1, 5):
        scan = sorted(n for n in range(2, p ** (V + 2)) if GW.vp(n - 1, p) > V)
        ok(sorted(supply(p, V)) == scan,
           f"H1: p={p} rung V={V} direct supply == parent range scan "
           f"({len(scan)} carriers)")

disagree = [n for n in range(2, AGREE_LIMIT)
            if is_prime_power(n)[0] != GW.is_prime_power(n)[0]]
ok(not disagree,
   f"H2: rebuilt prime-power test agrees with the parent below "
   f"{AGREE_LIMIT} ({len(disagree)} disagreements)")

BIG = 10 ** 60 + 7
while not BR.is_primeZ(BIG):
    BIG += 2
BIGPP = BIG ** 2
mine = is_prime_power(BIGPP)
theirs = GW.is_prime_power(BIGPP)
print(f"    large specimen q^2 with q = {BIG} ({len(str(BIGPP))} digits)")
print(f"      rebuilt: {mine[0]} ({mine[1]});  parent: {theirs[0]} ({theirs[1]})")
ok(mine[0] and not theirs[0],
   "H2: the one-directional disagreement is the parent's uncertified cofactor")

for p, want in ((3, 2), (5, 3)):
    D, misses, _ = death_rung(p, RUNG_CAP)
    ok(D == want, f"H3: p={p} dies at rung V={want} as published (got {D})")
    print(f"      all-miss certificate at V={D}: " + "; ".join(
        f"{n}={GW.factor_split(n)}" for n in misses))

print()
print("=" * 72)
print(f"H4 THE SWEEP: every odd prime p <= {P_MAX}, cap pinned at p")
print("=" * 72)
print("      p    D(p)   rung-V death certificate size   heuristic (p-1)/ln p")

odd_primes = [p for p in range(3, P_MAX + 1) if BR.is_primeZ(p)]
deaths, alive, odd_m_hits = {}, [], []
for p in odd_primes:
    D, misses, odd_hits = death_rung(p, RUNG_CAP)
    deaths[p] = D
    odd_m_hits.extend(odd_hits)
    if D is None:
        alive.append(p)
        continue
    if p <= 60 or p % 50 < 3:
        print(f"    {p:>5}   {D:>4}   {len(misses):>5} candidates, "
              f"{len(str(misses[-1])):>5} digits          "
              f"{(p - 1) / log(p):>8.1f}")

ok(not alive,
   f"H4: every odd prime <= {P_MAX} has a certified death rung "
   f"({len(alive)} still climbing at V={RUNG_CAP}: {alive})")
settled = [p for p in odd_primes if deaths[p] is not None]
print(f"    swept {len(odd_primes)} odd primes, {len(settled)} settled; "
      f"deaths run D(3)={deaths[3]} .. "
      f"D({settled[-1]})={deaths[settled[-1]]}, "
      f"max D = {max(deaths[p] for p in settled)} at p = "
      f"{max(settled, key=lambda q: deaths[q])}")

print()
print("=" * 72)
print("H5 THE MARGIN (scored, carries no verdict)")
print("=" * 72)
viol = [(p, deaths[p], 2 * (p - 1) / log(p) + 5) for p in settled
        if deaths[p] > 2 * (p - 1) / log(p) + 5]
worst = max(settled, key=lambda q: deaths[q] * log(q) / (q - 1))
print(f"    violations of D(p) <= 2(p-1)/ln p + 5: {len(viol)}")
for p, d, b in viol[:10]:
    print(f"      p={p}: D={d} against bound {b:.1f}")
print(f"    worst ratio D(p)*ln p/(p-1) = "
      f"{deaths[worst] * log(worst) / (worst - 1):.2f} at p = {worst} "
      f"(D = {deaths[worst]})")

print()
print("=" * 72)
print("H6 THE PARITY EXCEPTIONS: accepted odd-multiplier carriers")
print("=" * 72)
print(f"    {len(odd_m_hits)} accepted odd-m carriers below the death rungs")
for p, V, m, n, split in odd_m_hits[:20]:
    print(f"      p={p} V={V} m={m}: {n} = {split}")
ok(all(split.startswith("2^") or split == "2" for _, _, _, _, split in odd_m_hits),
   "H6: every accepted odd-multiplier carrier is a power of 2")

print()
print("=" * 72)
print(f"{sum(PASS)}/{len(PASS)} checks pass")
print("=" * 72)
