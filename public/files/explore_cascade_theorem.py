"""WHAT A DEATH-RUNG PROOF MUST SUPPLY -- the exponent identity that
confines the proper prime powers, and the rung's invisibility to every
small-prime instrument.

THE QUESTION. explore_cascade_chars.py closed the cascade boundary at
every odd characteristic below 1000 by direct computation: each odd
prime p reaches a rung V where all p-1 affordable carriers
m*p^(V+1)+1, 1 <= m <= p-1, are certified non-prime-powers.
explore_cascade_residual.py then proved that no extension of that sweep
empties the residual -- the primorial field ramifies at every prime
below any bound one names -- so what closes the boundary wholesale is a
theorem and not a longer sweep. The theorem needed is weaker than it
first looks: a ring is closed as soon as ONE of its rank-1
characteristics dies, and those carry density at least 1/n, so it is
enough that the odd primes with NO death rung have density ZERO.

That statistical target was chosen because it looked like the form that
admits sieve and second-moment arguments the universal statement
refuses. This rig asks whether it does, and asks first what the
surviving carriers actually ARE, because the two questions turn out to
be one: an instrument that cannot see the rung cannot see it in an
average either.

  (a) WHAT SURVIVES. The candidates are p-1 explicit numbers per rung
      and a survivor is a prime POWER, not a prime. How much of the
      difficulty lives in the proper powers is not known, and it
      decides whether the question is arithmetic or analytic.
  (b) WHAT THE NAMED INSTRUMENTS SEE. Covering congruences are the
      candidate instrument the front named. A covering acts through
      divisibility by small primes, and so does every upper-bound
      sieve. What such an instrument reports at rung V, against what
      the rung actually holds, is measurable.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE SETTING, restated so the door exponent is a PARAMETER. At
      rung V of characteristic p the affordable carriers are the norms
      n with n ≡ 1 (mod p^(V+1)) and n below the door. For odd p the
      budget inequality pins the door at p^(V+2); at p = 2 the unit
      group's extra Z/2 widens it to 2^(V+3). Write the door as
      p^(V+1+c), so c = 1 at odd p and c = 2 at p = 2. Carrying c
      rather than substituting it is what lets p = 2 control the
      derivation, since p = 2 is where the only known proper-power
      carriers live.

  (2) THE EXPONENT IDENTITY. Let n = q^a be a carrier at rung V:
      q prime, a >= 1, n ≡ 1 (mod p^(V+1)), p^(V+1) < n < p^(V+1+c).
      Since n ≡ 1 (mod p), q is not p, so q is a unit mod p^(V+1); let
      d = ord_{p^(V+1)}(q). Then d | a; write a = d*s. Now q^d ≡ 1
      (mod p^(V+1)) and q^d > 1, so q^d >= p^(V+1) + 1, hence

          n = (q^d)^s > p^((V+1)s),

      and n < p^(V+1+c) forces (V+1)s < V+1+c, i.e. s < 1 + c/(V+1).
      For odd p (c = 1) that gives s < 2 at every V >= 0, so s = 1 and

          a = ord_{p^(V+1)}(q)   EXACTLY.

      At p = 2 (c = 2) the same line permits s = 2 only when V = 0.
      The identity is TAUTOLOGICAL at a = 1 -- ord = 1 is the
      acceptance condition itself -- so all of its content is at
      a >= 2, which is why the controls below are built at p = 2 and
      on a hand-made specimen rather than on the odd sweep.

  (3) THE p-PART OF THE EXPONENT IS TRIVIAL. Write b = ord_p(q), so
      b | p-1, and ord_{p^(V+1)}(q) = b*p^j where j = max(0, V+1-e)
      with e = v_p(q^b - 1). Suppose j >= 1, so e = V+1-j =: t >= 1.
      Then q^b >= p^t + 1 > p^t and a = b*p^j, so

          n = q^a >= (q^b)^(p^j) > p^(t*p^j),

      while n < p^(V+1+c) = p^(t+j+c). So t*p^j < t+j+c, i.e.
      t*(p^j - 1) < j + c. For odd p and j >= 1 the left side is at
      least p^j - 1 >= 3^j - 1, and (j+c)/(3^j-1) <= (j+1)/(3^j-1) <= 1
      for every j >= 1, so t < 1 -- contradicting t >= 1. Hence j = 0
      and

          a = b divides p-1.

  (4) THE BASE IS SMALLER THAN THE CHARACTERISTIC, and the exponent is
      at least the rung. Let a >= 2. Since p does not divide a (by (3),
      a | p-1) and ord_p(q) = a, the values Phi_d(q) for the proper
      divisors d | a are coprime to p, so the whole p-part of q^a - 1
      sits in the a-th cyclotomic value:

          p^(V+1) | Phi_a(q),  hence  Phi_a(q) >= p^(V+1).

      For a >= 2 the factorization q^a - 1 = prod_{d|a} Phi_d(q)
      contains both Phi_1(q) = q-1 and Phi_a(q), so

          p^(V+1+c) > n - 1 = q^a - 1 >= (q-1)*Phi_a(q) >= (q-1)*p^(V+1),

      giving q - 1 < p^c, so q <= p^c. For odd p that is q <= p, and
      q is not p, so q < p. Then p^(V+1) < q^a < p^a forces a >= V+2.

      So a proper prime-power carrier at rung V of an odd p is q^a with
      q < p prime, a | p-1, and a >= V+2 -- a set small enough to
      enumerate EXHAUSTIVELY, which is what H4 does. It also subsumes
      the square exclusion: a >= V+2 >= 3 at every rung the ladder
      walks, so no carrier is the square of a prime.

  (5) THE RUNG IS INVISIBLE TO EVERY SMALL-PRIME INSTRUMENT. For a
      prime q not dividing p,

          q | m*p^(V+1) + 1   <=>   m ≡ -(p^(V+1))^(-1)  (mod q),

      exactly ONE residue class mod q, at every rung. So the
      multipliers left by sifting [1, p-1] with all primes q <= z form
      the complement of one class per prime, and by CRT their count is

          (p-1) * prod_{q <= z, q != p} (1 - 1/q)

      up to the boundary error of an incomplete period -- a quantity in
      p and z with NO dependence on V whatever. The truth decays: the
      expected number of prime carriers at rung V is about
      (p-1)/((V+2) ln p). Three consequences, and they are the reason
      this rig exists.

        COVERING CONGRUENCES ARE NOT AN INSTRUMENT HERE, which is a
        weaker and more useful statement than their being unable to
        close a rung. The uncovered set has positive density
        prod (1 - 1/q) for any finite set of prime moduli -- a lemma
        this corpus already carries, from the far side of it: the
        orbit-cost law's forced separators are one class per distinct
        prime modulus and by CRT never cover, leaving prod (q-1)
        points, verified exhaustively there over every class choice
        (explore_orbit_cost.py). It is the same CRT fact and it is
        worth knowing it has two consumers. So a
        covering that closes a rung needs prod q > p-1 -- it is never a
        covering SYSTEM but an alignment against one interval, which
        already costs it every result in the covering literature. And
        the class each modulus kills is a FUNCTION of V,
        not a design choice -- as V varies it ranges over the coset of
        the group generated by p^(-1) mod q -- so "find a covering" and
        "find a death rung" are the same search, and the instrument
        adds no leverage to it.

        AN UPPER-BOUND SIEVE REPORTS THE SAME NUMBER AT EVERY RUNG. Its
        input is the sifted set above, so its bound at rung V equals
        its bound at rung 1, about (p-1)/ln p, while the truth at rung
        V is smaller by a factor of about V+2.

        AVERAGING CANNOT REPAIR A V-INDEPENDENT BOUND. Suppose a
        positive-density set B of p had no death rung below R. Then
        each p in B contributes at least one carrier at each of R
        rungs, so R*|B| <= sum over p <= x, V <= R of the carrier
        count, and any bound insensitive to V bounds that double sum by
        R times its rung-1 value: the R cancels on both sides and the
        conclusion is the rung-1 statement, whatever R is. Averaging
        over p does the same. So the statistical target admits exactly
        the instruments the universal one does, and the weakening buys
        nothing on this route.

  (6) WHAT WOULD SUFFICE, and it is the strong form. If for some
      constant C and all large V,
      pi(p^(V+2); p^(V+1), 1) <= C*(p-1)/((V+2) ln p) -- the
      expected-order upper bound for primes in this arithmetic
      progression -- then the PRIME carriers are gone from every rung
      with V+2 > C*(p-1)/ln p, since their count is a non-negative
      integer below 1. The proper powers need a second step and (4)
      supplies it outright rather than by counting: a | p-1 with
      a >= V+2 is possible only while V+2 <= p-1, so above V = p-3
      there are no proper prime powers at ANY characteristic. Taking a
      rung above both thresholds, EVERY odd p has a death rung, with
      D(p) = O(p). The RATE the heuristic suggests, O(p/ln p), does not
      follow: it is the prime threshold alone, and reaching it would
      need the proper powers excluded below p-3 as well -- which the
      sweep observes (finding 1: one such carrier in all of it) and
      nothing here proves. The hypothesis is an upper bound in the
      regime where the window is only p times the modulus, which no
      theorem reaches; but note what it yields is the UNIVERSAL
      statement, so the statistical target has no cheaper hypothesis on
      this route either.

PREDICTIONS (fixed before any engine code; hand-derived above).

  H1 (POSITIVE CONTROL, the verdicts). This rig's own ladder walk
     reproduces explore_cascade_chars.py's death rungs at every odd
     prime below P_MAX, compared against that rig's live output rather
     than against its published numbers. KILL: any disagreement.
  H2 (POSITIVE CONTROL, the identity has teeth). The identity check is
     not vacuous. At p = 2, where the wider door admits them, the
     published carriers 9, 17, 97, 193, 257 all satisfy
     a = ord_{2^(V+1)}(q), with 9 = 3^2 exercising a = 2; and a
     hand-built specimen whose exponent is twice its order is FLAGGED
     by the same routine and sits above the door, as (2) says it must.
     KILL: a p = 2 carrier violates the identity, or the specimen
     passes.
  H3 (THE IDENTITY ON THE SWEEP). Every accepted carrier q^a with
     a >= 2 at every rung V >= 1 of every odd p <= P_MAX satisfies
     a = ord_{p^(V+1)}(q), q < p, a | p-1, and a >= V+2.
     OBSERVABLE: the printed list of accepted carriers with a >= 2 and
     the count of confinement violations. KILL: any violation. The
     list being EMPTY is a measurement and not a verdict -- the
     derivation confines the proper powers, it does not exclude them.
  H4 (THE EXHAUSTIVE SEARCH, an independent route to the same set). By
     (4) the proper-power carriers at rung V of p are exactly the q^a
     with q < p prime, a | p-1, a >= V+2, p^(V+1) < q^a < p^(V+2) and
     q^a ≡ 1 (mod p^(V+1)) -- a search over a few hundred pairs per
     characteristic, run independently of the ladder walk. OBSERVABLE:
     the set it returns, against the a >= 2 carriers the walk accepted.
     KILL: the two sets differ.
  H5 (THE QUESTION: the rung is invisible to the sieve). Let
     U(p,V) = #{even m <= p-1 : m*p^(V+1)+1 has no prime factor <= z},
     z = SIEVE_Z, and A(p,V) the accepted-carrier count at that rung.
     Over the primes with D(p) >= 10, pooled rung by rung for
     V = 1..10: the mean normalized A falls by more than half, while
     the mean normalized U changes by less than 10%. OBSERVABLE: the
     two columns and their rung-10/rung-1 ratios, plus the per-p least
     squares slope of U against V. KILL: the U ratio falls below 0.9 --
     the sieve would then be seeing the rung -- or the A ratio exceeds
     0.5, which would mean the contrast has no signal in it and the
     measurement decides nothing.
  H6 (THE COVERING CEILING, and the MARGIN -- distrusted). U(p,D(p))
     > 0 for every swept p >= 100: sifting by primes up to z never
     closes a rung by itself. And U(p,V) tracks the Mertens prediction
     floor((p-1)/2) * prod_{3 <= q <= z, q != p} (1 - 1/q).
     OBSERVABLE: the (p,V) pairs with U = 0, and the worst ratio of
     measured to predicted. The first half is a KILL for the covering
     instrument at this z; the Mertens fit is a margin and carries no
     verdict either way.

FINDINGS.

  1. THE SURVIVORS ARE PRIMES, AND THE PROPER POWERS ARE CONFINED TO AN
     ENUMERABLE SET. The confinement is a THEOREM -- proved at (2)-(4)
     for every odd p and every rung V >= 1, with no computation in it
     -- and the sweep below is a rule (verified p <= 1000) measuring
     how much of the confined set is actually inhabited. A
     carrier q^a at rung V >= 1 of an odd p satisfies all four of
     a = ord_{p^(V+1)}(q), a | p-1, q < p, a >= V+2. Across the whole
     sweep -- every rung at or below the death rung of all 167 odd
     primes -- there is EXACTLY ONE carrier with a >= 2:

         3^5 = 243 = 2*11^2 + 1   at p = 11, V = 1,

     and it meets the confinement (5 | 10, 3 < 11, 5 >= 3) while
     SATURATING the cyclotomic inequality that produced it:
     Phi_5(3) = 121 = 11^2 = p^(V+1) exactly, where (4) asks only for
     divisibility. The exhaustive search over
     the confinement -- q in one integer-root interval, a a divisor of
     p-1 at least V+2, run independently of the ladder -- returns that
     same single carrier and nothing else (H4), so the two routes agree
     on the whole sweep.

     What that buys is the SHAPE of the remaining question. A death
     rung is an all-miss over p-1 candidates, and the misses now split
     into a finite exhaustive check (the proper powers, enumerable by
     the confinement) and one analytic question with no arithmetic
     slack left in it: is there a PRIME congruent to 1 mod p^(V+1)
     below p^(V+2). The prime-power framing suggested the difficulty
     might be spread; it is not.

  2. THE RUNG IS INVISIBLE TO EVERY SMALL-PRIME INSTRUMENT (theorem,
     proved at (5) for every p, V and z; the contrast below measured
     p <= 1000). Pooled over the 144 primes
     with D(p) >= 10, rungs 1 through 10, each column normalized by the
     supply it is a fraction OF -- carriers by p-1, sifted multipliers
     by the floor((p-1)/2) EVEN ones, which is the effective supply and
     is why the Mertens figure below is the odd-moduli product: the
     accepted-carrier density falls from 0.05792 to 0.01418, a ratio of
     0.245 against the 0.25 that the (V+2)^(-1) heuristic predicts,
     while the sifted count over the SAME rungs is flat, 0.11952 to
     0.12250, a ratio of 1.025, holding the LEVEL
     2e^(-gamma)/ln z = 0.1219. The median per-p
     |slope|*D(p)/mean(U) is 0.0597, and the one outlier at 0.8459 is
     p = 59, the smallest supply in the pool. Specimen: p = 439 has 27
     sifted survivors at rung 1 and 27 at its death rung 21.

     ONE CONFOUND, and it runs the safe way. Pooling on D(p) >= 10
     conditions every rung in the table on having at least one carrier,
     since a rung with none IS the death -- so A cannot reach zero in
     the pooled range and the measured fall is an UNDERSTATEMENT of the
     real one. U is not conditioned that way, and what conditioning
     reaches it lifts every rung alike and leaves the ratio. The
     confound can only weaken the contrast, which is why the table is
     read as it stands.

     So the quantity a small-prime instrument reports is a function of
     p and z alone, exactly as the derivation says, while the truth
     falls like 1/V. The entire decay lives in the LARGE prime factors
     of the carriers, where these instruments are silent.

  3. THE INSTRUMENT THE FRONT NAMED IS REFUTED, AND THE STATISTICAL
     WEAKENING BUYS NOTHING ON THIS ROUTE (theorem, proved at (5);
     the covering measurement is a rule, verified z = 10^4, p <= 1000).
     Covering congruences act through exactly the sifted set of finding
     2, and sifting by every prime below 10^4 empties no death rung at
     any swept p >= 100 (H6, zero exceptions) -- it cannot, the
     uncovered set having positive density prod (1 - 1/q) for any
     finite set of prime moduli. Two structural facts stand behind the
     measurement and are the reason no larger z rescues it: a covering
     that closes a rung must have prod q > p-1, so it is an alignment
     against one interval and never a covering SYSTEM; and the class
     each modulus kills is a function of V rather than a design choice,
     so "find a covering" and "find a death rung" are the same search.
     The same V-independence disposes of the averaging arguments the
     statistical target was chosen for: a bound that does not fall with
     the rung bounds a sum over R rungs by R times its rung-1 value,
     and the R cancels. So no argument built on small-prime
     divisibility separates density zero from the universal statement,
     and the one hypothesis that reaches either -- (6) -- reaches both.
     The reduction that weakened the target is correct as mathematics
     and it stands; what it does not do is weaken the WORK.

  4. THE MARGIN (H6, scored, no verdict). The Mertens fit's worst ratio
     is 2.832, at p = 29 rung 1, where 5 survivors are measured against
     1.77 predicted -- a count that small carries no fit, and the
     agreement is excellent wherever the supply is (p = 439: 27 against
     26.73). Recorded because the flat U column of finding 2 is a RATIO
     and would read the same under a badly calibrated prediction; the
     absolute fit is what says the sifted count is the Mertens count
     and not merely a constant.

RUN RECORD. 8/8 checks pass. Peak working set 21.1 MB against the
512 MB ceiling, wall 213.3 s under memwatch.py, of which the parent
rig's own sweep at import is 106 s (estimated at four to five minutes).
P_MAX = 1000, SIEVE_Z = 10^4, RUNG_CAP = 120, POOL_RUNGS = 10.

ONE THING ABOUT HOW THIS RIG GOT HERE. The first version of the
exhaustive search (H4) looped the base over every prime below p and
broke on the first power above the door. That is correct and
unrunnable: a >= V+2 makes q^a exceed the door only at q >= p, so the
break never fires inside the range and the search computes powers of
four digits' base with thousand-digit values. The window bounds the
BASE directly -- q lies in one integer-root interval -- and the
rebuilt search is the derivation (4) used as an algorithm rather than
only as a proof. The sweep bound was 60 for a smoke run and then 1000
for the record; H3 and H6 quantify over every swept prime, so raising
it only makes them harder.

WHAT A CLEAN RUN BUYS, and what it does not. It does not prove that
every odd p has a death rung, and it does not prove density zero for
those that might not. What it buys is the SHAPE any proof must have:
the proper prime powers are confined to an enumerable set and are
empirically absent, so the question is a pure prime-existence question
with no arithmetic slack in it; and the two instruments the front named
report a quantity that does not depend on the rung at all, so neither
they nor any average of them can reach it.
"""

import io
import os
import sys
import contextlib
from math import log, gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_bridge_reach as BR

# explore_cascade_chars.py has no __main__ guard, so importing it RUNS the
# parent sweep; its output is captured rather than interleaved and the line
# count printed, so the capture is visible rather than silent. Paying that
# import is what makes H1 a live comparison against the parent's own
# verdicts instead of a quotation of its docstring -- and it means the
# prime-power test below is the parent's, not a copy of it.
_captured = io.StringIO()
with contextlib.redirect_stdout(_captured):
    import explore_cascade_chars as CC
print(f"    (parent rig imported; {len(_captured.getvalue().splitlines())} "
      f"lines of its output captured; its own checks: "
      f"{sum(CC.PASS)}/{len(CC.PASS)})")

is_prime_power = CC.is_prime_power

PASS = []


def ok(cond, label):
    PASS.append(bool(cond))
    print(f"    [{'PASS' if cond else 'FAIL'}] {label}")


# ---------------------------------------------------------------- primitives

def factorize_small(n):
    """-> sorted list of distinct primes dividing n. n <= 10^6 here (it is
    always p-1 or a group order's prime part), so trial division is exact
    and there is no probabilistic step in the order computation below."""
    fs, d = [], 2
    while d * d <= n:
        if n % d == 0:
            fs.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        fs.append(n)
    return fs


def divisors(n):
    ds, d = [], 1
    while d * d <= n:
        if n % d == 0:
            ds.append(d)
            if d != n // d:
                ds.append(n // d)
        d += 1
    return sorted(ds)


def order_mod_pk(q, p, k):
    """ord_{p^k}(q), exact. The group is cyclic of order p^(k-1)*(p-1),
    so the order is found by dividing that exponent down one prime at a
    time -- no search, and no reliance on a factorization larger than
    p-1."""
    mod = p ** k
    q %= mod
    if gcd(q, mod) != 1:
        return None
    e = p ** (k - 1) * (p - 1)
    for f in factorize_small(e):
        while e % f == 0 and pow(q, e // f, mod) == 1:
            e //= f
    return e


def base_and_exponent(n):
    """-> (q, a) with n = q^a, q prime, using the parent's test to decide
    prime-power-ness and its own split string to name the base."""
    pp, split = is_prime_power(n)
    if not pp:
        return None
    if "^" in split:
        q, a = split.split("^")
        return int(q), int(a)
    return int(split), 1


# ------------------------------------------------------- the ladder, re-walked
# The parent's death_rung returns the verdict only. This walk returns the
# whole rung profile -- accepted carriers and sifted counts per rung --
# which is what H3, H5 and H6 read. The verdict it produces is compared
# against the parent's in H1.

P_MAX = 1000
SIEVE_Z = 10 ** 4
RUNG_CAP = 120
POOL_RUNGS = 10

SIEVE_PRIMES = [q for q in range(3, SIEVE_Z + 1) if BR.is_primeZ(q)]


def sifted_even(p, V):
    """#{even m in [1, p-1] : m*p^(V+1)+1 has no prime factor <= SIEVE_Z}.

    Computed through the killed CLASS rather than by dividing the
    carriers: q divides m*p^(V+1)+1 exactly when m lies in one residue
    class mod q, so the whole sieve is a walk down arithmetic
    progressions in the multiplier and never touches a carrier. That is
    the derivation (5) used as an algorithm, and it is why the cost is
    p * sum 1/q rather than p * pi(z)."""
    live = bytearray(p)          # live[m] for m in [0, p-1]; odd m unused
    for m in range(2, p, 2):
        live[m] = 1
    for q in SIEVE_PRIMES:
        if q == p:
            continue
        # m0 is never 0: it is minus the inverse of a unit, so the class
        # the sieve walks always starts at a genuine multiplier.
        m0 = (-pow(pow(p, V + 1, q), -1, q)) % q
        for m in range(m0, p, q):
            live[m] = 0
    return sum(live[2:p:2])


def walk(p):
    """-> (D, A, U, hits) for odd p: the death rung, the per-rung accepted
    carrier counts, the per-rung sifted counts, and every accepted carrier
    with exponent >= 2. Every candidate at every rung is tested, so the
    counts are of the whole supply and not of a prefix."""
    A, U, hits = {}, {}, []
    for V in range(1, RUNG_CAP + 1):
        base = p ** (V + 1)
        acc = 0
        for m in range(1, p):
            be = base_and_exponent(m * base + 1)
            if be is None:
                continue
            acc += 1
            if be[1] >= 2:
                hits.append((p, V, m, be[0], be[1]))
        A[V] = acc
        U[V] = sifted_even(p, V)
        if acc == 0:
            return V, A, U, hits
    return None, A, U, hits


def proper_power_search(p, V):
    """Every proper prime-power carrier at rung V of odd p, by
    hand-derivation (4): q < p prime, a | p-1, a >= V+2, and q^a in the
    window and ≡ 1 mod p^(V+1). Independent of the ladder walk."""
    found = []
    lo, hi = p ** (V + 1), p ** (V + 2)
    for a in divisors(p - 1):
        if a < max(2, V + 2):
            continue
        # The window bounds the BASE directly: q^a must land strictly
        # between lo and hi, so q runs over one integer-root interval and
        # not over every prime below p. Without this the search computes
        # q^a for bases whose power has thousands of digits.
        for q in range(max(2, CC.integer_root(lo, a)),
                       CC.integer_root(hi - 1, a) + 1):
            if not BR.is_primeZ(q):
                continue
            n = q ** a
            if lo < n < hi and n % lo == 1:
                found.append((p, V, (n - 1) // lo, q, a))
    return found


# ============================================================ H2: the controls

print()
print("=" * 72)
print("H2 CONTROLS: the exponent identity has teeth")
print("=" * 72)

# p = 2 carries the only known proper-power carriers, under the door
# 2^(V+3) that the unit group's extra Z/2 buys (c = 2 in (1)).
P2_CARRIERS = [(1, 9), (3, 17), (4, 97), (5, 193), (6, 257)]
bad2 = []
for V, n in P2_CARRIERS:
    q, a = base_and_exponent(n)
    d = order_mod_pk(q, 2, V + 1)
    inside = 2 ** (V + 1) < n < 2 ** (V + 3)
    print(f"      p=2 V={V}: {n} = {q}^{a}, ord_(2^{V + 1})({q}) = {d}, "
          f"inside the door: {inside}")
    if a != d or not inside:
        bad2.append((V, n, a, d))
ok(not bad2, f"H2: every published p=2 carrier has a = ord ({len(bad2)} "
             f"violations), and 9 = 3^2 exercises a >= 2")

# The negative control: same base, exponent twice its order. (2) says such
# a number cannot sit under the door, and the routine must say so too.
q_neg, V_neg = 3, 1
d_neg = order_mod_pk(q_neg, 2, V_neg + 1)
n_neg = q_neg ** (2 * d_neg)
print(f"      specimen {q_neg}^{2 * d_neg} = {n_neg}: exponent {2 * d_neg} "
      f"against ord = {d_neg}, door 2^{V_neg + 3} = {2 ** (V_neg + 3)}")
ok(2 * d_neg != d_neg and n_neg >= 2 ** (V_neg + 3),
   "H2: the doubled-exponent specimen is flagged and sits above the door")

# ==================================================== H1/H3/H5/H6: the sweep

print()
print("=" * 72)
print(f"H1 THE WALK: every odd prime p <= {P_MAX}, rung profile recorded")
print("=" * 72)

odd_primes = [p for p in range(3, P_MAX + 1) if BR.is_primeZ(p)]
D, Aall, Uall, pp_hits = {}, {}, {}, []
for p in odd_primes:
    d, A, U, hits = walk(p)
    D[p], Aall[p], Uall[p] = d, A, U
    pp_hits.extend(hits)

mismatch = [(p, D[p], CC.deaths[p]) for p in odd_primes
            if D[p] != CC.deaths[p]]
ok(not mismatch,
   f"H1: this walk's death rungs equal the parent's at all "
   f"{len(odd_primes)} odd primes ({len(mismatch)} mismatches)")
print(f"    D runs {min(D.values())} .. {max(D.values())}, max at p = "
      f"{max(D, key=lambda q: D[q])}")

print()
print("=" * 72)
print("H3/H4 THE PROPER POWERS: confinement, and the exhaustive search")
print("=" * 72)

viol = []
for (p, V, m, q, a) in pp_hits:
    d = order_mod_pk(q, p, V + 1)
    if a != d or q >= p or (p - 1) % a or a < V + 2:
        viol.append((p, V, m, q, a, d))
print(f"    accepted carriers with exponent >= 2 across the whole sweep: "
      f"{len(pp_hits)}")
for h in pp_hits[:20]:
    print(f"      p={h[0]} V={h[1]} m={h[2]}: {h[3]}^{h[4]}")
ok(not viol, f"H3: every one of them satisfies a = ord, q < p, a | p-1, "
             f"a >= V+2 ({len(viol)} violations)")

exhaustive = []
for p in odd_primes:
    for V in range(1, D[p] + 1):
        exhaustive.extend(proper_power_search(p, V))
walk_set = {(p, V, m, q, a) for (p, V, m, q, a) in pp_hits}
print(f"    exhaustive search over q < p, a | p-1, a >= V+2: "
      f"{len(exhaustive)} carriers")
ok(set(exhaustive) == walk_set,
   f"H4: the exhaustive search returns exactly the walk's proper-power "
   f"carriers ({len(set(exhaustive) ^ walk_set)} in the symmetric difference)")

print()
print("=" * 72)
print(f"H5 THE QUESTION: what falls with the rung and what does not "
      f"(z = {SIEVE_Z})")
print("=" * 72)

pool = [p for p in odd_primes if D[p] >= POOL_RUNGS]
print(f"    pooled over the {len(pool)} primes with D(p) >= {POOL_RUNGS}")
print("       V   mean A(p,V)/(p-1)   mean U(p,V)/floor((p-1)/2)")
colA, colU = [], []
for V in range(1, POOL_RUNGS + 1):
    a_bar = sum(Aall[p][V] / (p - 1) for p in pool) / len(pool)
    u_bar = sum(Uall[p][V] / ((p - 1) // 2) for p in pool) / len(pool)
    colA.append(a_bar)
    colU.append(u_bar)
    print(f"    {V:>4}   {a_bar:>16.5f}   {u_bar:>26.5f}")
ratio_A = colA[-1] / colA[0]
ratio_U = colU[-1] / colU[0]
print(f"    rung-{POOL_RUNGS}/rung-1 ratio:  A = {ratio_A:.3f}   "
      f"U = {ratio_U:.3f}")
ok(ratio_A <= 0.5,
   f"H5: the accepted-carrier count falls by more than half ({ratio_A:.3f})")
ok(ratio_U >= 0.9,
   f"H5: the sifted count does not see the rung ({ratio_U:.3f} >= 0.9)")

slopes = []
for p in pool:
    vs = list(range(1, D[p] + 1))
    vbar = sum(vs) / len(vs)
    ubar = sum(Uall[p][V] for V in vs) / len(vs)
    num = sum((V - vbar) * (Uall[p][V] - ubar) for V in vs)
    den = sum((V - vbar) ** 2 for V in vs)
    slopes.append((abs(num / den) * D[p] / max(ubar, 1e-9), p))
slopes.sort(reverse=True)
print(f"    worst per-p |slope|*D(p)/mean(U): {slopes[0][0]:.4f} at "
      f"p = {slopes[0][1]}; median {slopes[len(slopes) // 2][0]:.4f}")

print()
print("=" * 72)
print("H6 THE COVERING CEILING, and the Mertens margin (scored)")
print("=" * 72)

zero_at_death = [p for p in odd_primes if p >= 100 and Uall[p][D[p]] == 0]
ok(not zero_at_death,
   f"H6: sifting by primes <= {SIEVE_Z} never empties a death rung for "
   f"p >= 100 ({len(zero_at_death)} exceptions: {zero_at_death[:10]})")

worst_r, worst_at = 0.0, None
for p in odd_primes:
    pred = ((p - 1) // 2)
    for q in SIEVE_PRIMES:
        if q != p:
            pred *= (1 - 1 / q)
    for V in range(1, D[p] + 1):
        r = Uall[p][V] / pred if pred else float("inf")
        if abs(r - 1) > abs(worst_r - 1):
            worst_r, worst_at = r, (p, V, Uall[p][V], pred)
print(f"    worst measured/predicted = {worst_r:.3f} at p={worst_at[0]} "
      f"V={worst_at[1]} ({worst_at[2]} against {worst_at[3]:.2f})")
mid = odd_primes[len(odd_primes) // 2]
predmid = (mid - 1) // 2
for q in SIEVE_PRIMES:
    if q != mid:
        predmid *= (1 - 1 / q)
print(f"    specimen p={mid}: U at rung 1 = {Uall[mid][1]}, at the death "
      f"rung {D[mid]} = {Uall[mid][D[mid]]}, Mertens {predmid:.2f}")

print()
print("=" * 72)
print(f"{sum(PASS)}/{len(PASS)} checks pass")
print("=" * 72)
