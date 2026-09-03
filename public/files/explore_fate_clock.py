"""
explore_fate_clock.py -- WHICH FATE QUESTIONS ARE DECIDABLE, AND WHY
(sibling of explore_growth_laws.py, explore_lock_prime.py,
explore_headroom.py, explore_demand_reading.py, explore_slack_machine.py,
explore_conjecture_bridge.py, explore_bridge_reach.py).

THE QUESTION. A state of the growing tower is a positive integer N; a move
multiplies it, N -> N*m with m >= 2; a DEMAND LAW says which moves may be
made; a POLICY picks one of the admissible moves; and the trajectory's FATE
is the class of its limit supernatural number. Three fates are filed
(explore_growth_laws.py): BREADTH, every prime seated; DEPTH, some prime
at infinite depth; MORTALITY, a finite integer -- the trajectory halts
because nothing is admissible. (Why breadth is stated as SEATING and not
as "all primes at finite depth" is the definitional point below.)

Two neighbouring files leave a remark half-made. explore_conjecture_bridge.py
observes that a fate's provability is inherited from its object's level and
NOT from the surface quantifier shape, on the strength of one pair: two
growth-fate questions are both surface-Pi_2 ("for every target, some prime
exists"), and one is a theorem while the other is open. explore_demand_reading.py
observes that mortality is policy-INDEPENDENT while breadth and depth are
greedy statements with room for a free policy to differ, so a rich enough
law makes the free-policy fate question undecidable instead.

Neither remark is a statement about fate questions in general, and the two
are written in different vocabularies -- one in shifted-prime existence
objects, one in admissible sets. This file asks for the JOIN: is there ONE
statement in which a fate question's difficulty is a function of the OBJECT
and the POLICY CLASS, with the three fates as its instances?

THE PROPOSED ANSWER, to be tested rather than assumed: every fate question
the corpus has settled was settled the same way, and it was never by
evaluating a quantifier prefix. In each case there is a computable bound on
WHEN THE FATE IS ALREADY DETERMINED. Call it a VERDICT CLOCK. For a fate F,
law L, policy class Pi and seed s, a verdict clock is a computable T such
that every policy in Pi has its F-verdict fixed by step T. This is not a
synonym for decidability: it is a concrete object, and a decision procedure
could in principle exist without one, which is what makes the claim
refutable.

The clock comes in two pieces, and the corpus's own pair separates them:
an INNER clock bounds the search for a witness MOVE, an OUTER clock bounds
the step at which the fate is settled. The claim under test is that a fate
question is decidable when both exist and the outer clock is UNIFORM over
the policy class -- and that the surface quantifier prefix reads nothing.

A DEFINITIONAL POINT THAT IS LOAD-BEARING, and the argument for it is NOT
disjointness. The three fates are stated as classes of the limit, and the
loose wording "all primes at finite depth" for breadth is satisfied by
every finite integer, so it would file mortality inside breadth. The fix
is not to tighten breadth to "every prime seated AT FINITE DEPTH", which
overshoots in the other direction: a free policy over Z reaches 2^oo times
every odd prime (explore_fate_image.py), depth and breadth CO-OCCURRING in
one limit, so a definition excluding infinite depth from breadth would
contradict it. The three fates are therefore three
PROPERTIES and not a partition, their exclusivity over Z being the filed
fate-purity fact, itself archimedean. (SUPERSEDED in that last clause by
explore_fate_image.py: a FREE policy over Z reaches a limit carrying
breadth and depth at once, so the purity is greed's and not the
archimedean place's. What survives is exclusivity over Z FOR THE GREEDY
laws, which is the scope everything below uses.) BREADTH is EVERY PRIME SEATED (what
the healing rule asserts -- the window set converges to all primes in
entry order), DEPTH is some prime at infinite depth, MORTALITY is a halt.
Under that reading a limit missing one prime forever holds none of the
three, and section S3 is the test of whether such a limit is reachable.

THE OBJECTS. lambda is Carmichael's function. W(L) is the largest modulus
whose lambda divides L, so W(L) = (2 if L odd else 2^(v_2(L)+2)) times the
product of p^(v_p(L)+1) over odd primes p with (p-1) | L. The TRANSPARENCY
HEADROOM is V(N) = W(lambda(N))/N, and the transparent moves out of N are
exactly the divisors of V(N) that are at least 2 (filed,
explore_headroom.py). Omega(n) counts prime factors with multiplicity.

Three demand laws are exercised, each with its free policy class as well as
its filed greedy one:
  INDEPENDENCE  -- m admissible iff gcd(m, N) = 1 (the extension splits).
  DYNAMICS      -- m admissible iff lambda(N*m) > lambda(N).
  TRANSPARENCY  -- m admissible iff lambda(N*m) = lambda(N), i.e. m | V(N).

THE PREDICTIONS, fixed before any engine code was written, in the fates'
own vocabulary rather than the bridge's or the machine's. Each names what
the rig PRINTS, so the verdict is an observation and its meaning is weighed
afterwards.

P1 INDEPENDENCE, and the sharp one. No policy reaches DEPTH: once l is
   seated its exponent can never move again, since any m carrying l fails
   the coprimality demand. No policy reaches MORTALITY: a prime missing
   from N is always admissible. But a free policy can AVOID a fixed prime
   forever, and the prediction is that the resulting limit is in none of
   the three classes -- the free policy LEAVES the trichotomy rather than
   moving inside it.
   KILL: the rig prints a policy that misses a prime and still lands in one
   of the three classes, or prints that no prime-avoiding policy runs on.

P2 DYNAMICS. The filed greedy policy locks into one prime's column (the
   lock-prime law, explore_lock_prime.py). Predict that a FREE policy under
   the SAME law reaches BREADTH, by a padded move: to seat p, push p*q with
   q a prime chosen so that lambda rises whatever p does.
   One law, two fates, chosen by the policy alone.
   TRANSPLANT FLAG: the padded move is imported from explore_slack_machine.py,
   where it was built to buy law-autonomy for a DECREMENT -- a different job
   for the same device. The rig therefore re-derives that lambda rises at
   every padded step rather than inheriting the claim.
   PADDING CORRECTION, recorded rather than swapped in silence. The
   prediction was first fixed with q "a prime exceeding lambda(N)+1". That
   is a sufficient condition for lambda to rise and an unaffordable one:
   q-1 > lambda forces lcm(lambda, q-1) as high as lambda^2, so lambda
   SQUARES at every step and the trajectory drowns in its own digits within
   a few dozen primes. The operative condition is the weaker one actually
   used by the derivation -- (q-1) does not divide lambda(N) -- which is
   exactly what makes lambda rise, admits a small q, and keeps the growth
   modest. The prediction's content is unchanged; its construction moved to
   the condition the algebra names.
   KILL: the rig prints a padded step where lambda does not rise, or a
   prime no padded move can seat.

P3 TRANSPARENCY. Every policy halts, and the clock is UNIFORM over the
   whole free policy class -- which is the content, the filed result being
   about the greedy trajectory. Predict the reachable set from s is exactly
   the multiples of s dividing W(lambda(s)), a finite lattice; that EVERY
   maximal trajectory ends at the single state W(lambda(s)); and that the
   longest trajectory has length Omega(V(s)).
   KILL: the rig prints a reachable state outside that lattice, a terminal
   state other than the wall, or a trajectory longer than the bound.

P4 THE CENSUS. Sort every charted fate question in the corpus by whether
   its object supplies the two clocks, and check the sort reproduces the
   filed settled/open split exactly. A settled-but-clockless or an
   open-but-clocked row refutes the whole reading.
   KILL: the rig prints a nonzero mismatch count.
   SCOPE, fixed here rather than after the fact: "inner clock" is defined
   for EXISTENCE objects and has no meaning for the density, average and
   abscissa objects the corpus files as a change of KIND rather than a
   climb in level. Those rows are out of scope and are printed as such.

THE DESIGN, in five sections after the control.

S1 POSITIVE CONTROL, run before any verdict is read; the run aborts if it
   fails. Four things this file leans on but did not derive here must come
   back: lambda against its brute-force definition (the maximum order in
   the unit group); W against ITS definition (the largest modulus found by
   search) compared only below the search cap, since a truncated search
   reports the formula wrong for every large wall; the filed divisor
   identity, transparent moves = divisors of V, checked in BOTH directions
   over a bounded move range rather than by enumerating past V, which runs
   to nine figures well inside the range of states this file walks; and the
   filed greedy facts this file contrasts its free policies against --
   independence greedy grows the primorial, transparency greedy halts at
   the wall.

   STATES ARE CARRIED AS FACTORISATIONS in every section that walks a
   trajectory. A trajectory state is a product of many primes and outgrows
   any factoring budget within a few steps, so the engine multiplies
   exponent dictionaries and reads lambda off them; trial division is
   applied only to the small move m.

S2 MORTALITY UNDER EVERY POLICY (P3). Exhaust the transparent reachable set
   from several seeds by breadth-first search over states, compare it with
   the predicted lattice element by element, collect the terminal states,
   and measure the longest chain against Omega(V(s)). Exhaustion is the
   point: sampling would show the greedy trajectory again, and uniformity
   over the policy class is precisely what sampling cannot see.

S3 INDEPENDENCE LEAVES THE TRICHOTOMY (P1). Three mechanical checks --
   no admissible move disturbs a seated prime's exponent, the admissible
   set is never empty, and a first move may seat any finite depth (so the
   reason depth is unreachable is the infinitude of pushes, not a bound on
   one move). Then run the avoiding policy and classify its limit against
   all three classes, printing the justification for each verdict rather
   than the verdict alone.

S4 ONE LAW, TWO FATES (P2). Run the filed greedy policy under DYNAMICS and
   confirm it settles into a single prime's column; then run the padded
   free policy under the same admissibility test, checking at every step
   that lambda strictly rises and that the intended prime is seated, until
   every prime below a cap is seated at depth 1.

S5 THE CLOCK CENSUS (P4). Exhibit the two sides on live computations
   rather than by assertion. The settled side: the least prime in an
   arithmetic progression, found by bounded search at every modulus in
   range -- an inner clock made of a classical bound. The open side: the
   least exponent a with m*2^a + 1 prime over the odd prime powers below
   60, whose spread is the missing bound's shadow; and the covering-set
   certificate at 78557, which proves no clock can exist family-wide by
   exhibiting a base whose search never ends. Then the smooth-shifted-prime
   counts over a nested alphabet chain. Finally the table: every charted
   fate question with its two clocks, its uniformity, the status the clock
   reading PREDICTS, and the status actually filed -- with the mismatch
   count as the observable P4 named.

THE FINDINGS.

F1 MORTALITY'S CLOCK IS UNIFORM OVER THE WHOLE FREE POLICY CLASS, and the
   reachable set has a closed form (rule, proved, exhaustive at ten seeds).
   From s the transparent moves reach exactly the multiples of s dividing
   W(lambda(s)) -- ten seeds, 0 deviations, sets compared element by
   element. The proof is one line in each direction: s | N | W(lambda(s))
   forces lambda(N) = lambda(s), so every such N is a state; and m = V(N)
   is itself transparent, so the wall is one move away from anywhere. Two
   consequences the greedy result could not see. EVERY maximal trajectory
   ends at the SINGLE state W(lambda(s)) -- not merely the same fate but
   the same terminus, at all ten seeds. And the longest chain is exactly
   Omega(V(s)) at all ten (1, 0, 3, 5, 5, 4, 1, 6, 5, 6 against the same),
   so the clock is not just uniform but tight. Policy-independence and
   the finiteness of the reachable set are one fact, as the filed square
   says in the machine's words; the closed form is that fact in the fates'.

F2 A FREE POLICY CAN HOLD NONE OF THE THREE FATES (rule) -- and the
   headline is worded that way on purpose. "The three fates classify
   greedy runs" is an OVERCLAIM already rejected in
   explore_demand_reading.py, because it annexes MORTALITY, which holds
   under every policy and never was a greedy statement (S2 above re-proves
   it here). The correction is to the CLASSIFICATION, not to any fate:
   mortality is policy-independent, breadth and depth are greedy, and the
   new half is that a free policy can leave the classification entirely.
   Under INDEPENDENCE no admissible move disturbs a seated
   prime's exponent -- a TAUTOLOGY given the demand rather than a
   measurement, since gcd(m, N) = 1 and l | N force l not to divide m, and
   the sweep's 0 of 28554 is engine consistency and nothing more. The
   load-bearing step is its CONSEQUENCE: infinite depth needs infinitely
   many pushes of one prime and the demand allows exactly one, so depth is
   unreachable by any policy -- though a FIRST move seats any depth it likes (1..8 verified
   at N = 2), which locates the obstruction in the infinitude of pushes
   rather than in a bound on one move. No state below 3000 has an empty
   admissible set (0 of 2999), and the general reason is one line rather
   than the range -- a state has finitely many prime factors and there are
   infinitely many primes, so a coprime move always exists and mortality
   is unreachable at every state, not merely the checked ones. And the avoiding
   policy -- least coprime move that is not a multiple of 7 -- runs 300
   steps, seats 300 primes all at depth 1, and never seats 7. Its limit
   is therefore in NONE of the three classes: not mortal, not deep, and
   not breadth, since breadth is EVERY prime. A free policy under the
   filed law does not move between the fates; it leaves the trichotomy.

F3 ONE LAW, TWO FATES (rule). Under DYNAMICS the filed greedy policy locks
   on the 3-column (14 picks, every one a 3). The padded free policy under
   the SAME admissibility test seats every prime below 100 in 18 steps, 12
   of them padded, with lambda rising at 18 of 18 and every prime at depth
   1 (30 seated in all). So the fate is a function of the POLICY at fixed
   demand law, and the two canonical fates both occur under one law. The
   padding condition that works is (q-1) not dividing lambda(N), not the
   sufficient-but-unaffordable q > lambda(N)+1 the design first named.
   THE PREFIX IS NOT THE FATE, so the extrapolation is argued and not
   assumed: breadth is a property of the LIMIT, and the run exhibits 18
   steps. The construction never stalls, because a suitable q always
   exists -- (q-1) | lambda(N) forces q <= lambda(N)+1, so every prime
   above lambda(N)+1 outside the state qualifies, and there are
   infinitely many. Hence the policy continues for every prime in turn
   and seats them all; the rig's bounded search for q is an efficiency,
   not the argument, and it never had to reach far.

F4 THE FROZEN SORT WAS REFUTED BY ITS OWN KILL-SHAPE, and the repair is
   the finding. The two-valued rule -- decidable iff clocked, undecidable
   otherwise -- mismatched at 1 row of 7: the carrier ladder over all
   starts is clockless and non-uniform, which that rule calls UNDECIDABLE
   while the corpus files it OPEN. The fault is exactly the standing one:
   absence of a clock was being read as proof that no clock exists. The
   repaired rule is THREE-valued and needs a positive ingredient for the
   negative verdict -- decidable iff an outer clock uniform over the
   policy class plus an inner clock on every object the question reduces
   to; UNDECIDABLE iff the policy class embeds a universal machine; OPEN
   iff neither. It sorts 7 fate rows and 4 object rows with 0 mismatches,
   and no row is both clocked and hard (the consistency the rule needs).
   Tier: the mechanical half (a uniform clock decides) is a rule; the
   SORT over the charted corpus is an observation, not a confirmed
   prediction, because the three-valued form was not fixed in advance.

F5 LEVEL AND STATUS ARE SEPARATE READINGS, which is what the frozen rule
   had fused (observation). The two carrier rows differ in UNIFORMITY
   alone: over one start the question is Sigma_1, over all starts Pi_2 --
   and both are OPEN. So the policy/seed quantifier moves the LEVEL while
   the clock moves the STATUS, and neither is read off the surface prefix.
   This is what makes the corpus's own refuting pair explicable by a
   single object rather than by a prefix: the progression's least prime is
   bounded by a classical theorem (worst ratio p/B = 20 at B = 159 over
   B = 2..200, every modulus resolved by bounded search), while the
   Proth family has no such bound -- 19 of 20 odd prime powers below 60
   reach a witness at a <= 8 and 47 needs a = 583 -- and carries a
   certificate that none can exist family-wide: 78557 against the residues
   3, 5, 7, 13, 19, 37, 73, whose orders of 2 are 2, 4, 3, 12, 18, 36, 9
   for a joint period of 36, with 0 of the 36 exponents uncovered. A
   proof that a search never ends is STRONGER than a bound on one and
   still decides nothing.

F6 THE CASCADE BOUNDARY COMES OUT OPEN FOR THE REASON THE READING
   PREDICTS, in three named pieces rather than one: no outer clock (no
   bound on the all-miss cap), no hardness construction (ruling the ladder
   out is owned by no technique), and non-uniformity over starts, which is
   what lifts Sigma_1 to Pi_2 without touching the status.
   (Two of those three survive: explore_clock_vacuity.py finds the outer
   column carrying no information at any row, so "no outer clock" is not
   one of the reasons this row is open. What is left is the missing
   INNER clock on the carrier object and the missing hardness
   construction, with non-uniformity moving the level alone.)
   The alphabet
   family sits beside it, clockless per alphabet: the S-smooth shifted
   primes below 10^6 number 6, 42, 141 and 324 along the nested chain
   {2}, {2,3}, {2,3,5}, {2,3,5,7} -- the bottom one stalled at the Fermat
   primes, each one an open conjecture of its own.

SCOPE. WHICH COLUMNS ARE COMPUTED AND WHICH ARE FILED, since "0
mismatches" would otherwise read as a machine verdict on both sides. The
rig COMPUTES: mortality's uniformity and its closed form (S2, by
exhaustion), the non-uniformity of the independence and dynamics clocks
(S3, S4, by exhibiting the policies that break them), and every object
row's evidence (S5 -- the progression search, the exponent spread, the
covering certificate, the smooth counts). It TAKES FROM THE CORPUS: the
filed status of each row, and the outer-clock and hardness columns for
the rows it does not itself run (the greedy breadth and depth clocks,
the universal-machine embedding, the carrier ladder). The sort is
therefore a census whose columns are sourced, not derived, and its
value is that the rule survives contact with rows it did not choose.

THE NEIGHBOURS, named so nothing here reads as newer than it is. An outer
clock is a computable bound on when a verdict is fixed, which is the
RANKING-FUNCTION / well-founded-measure idea standard in termination
analysis; mortality's finite reachable set is a well-structured-transition
argument of the kind already cited for the machine half
(Finkel-Schnoebelen). What is not inherited from either is the SPLIT this
file is for -- status carried by clocks, level carried by the policy
quantifier, and the two moving independently across one corpus of fate
questions. The instrument is borrowed; the two-axis reading and the sort
it produces are the contribution.

AND THE STANDING REFUTATION TEST, which this file does NOT discharge: the
clock reading has content only if decidability here always comes FROM a
bound. A fate question decidable by some other route -- a parity or
invariant argument settling a fate without bounding when it is settled --
would make the clock a description rather than a law. None was found, and
none was looked for systematically.
  DISCHARGED by explore_clock_vacuity.py, and the OUTER half does not
  survive it. The hunt as posed cannot succeed -- a verdict that is a
  function of the seed alone is covered by the clock T = 0 -- so the test
  was run the other way, by asking what a clock must do that T = 0 does
  not. Every row F4's sort files DECIDABLE turns out to have a CONSTANT
  verdict, settled by an invariant with no bound in the argument, and the
  outer column agrees with the predicate "already filed decidable" at 7 of
  7 rows. So the biconditional above is an IMPLICATION: a clock decides,
  and decidability here does not come from one. The INNER clock and the
  uniformity clause are untouched, and F1's closed form is the clearest
  case of the correction -- it settles mortality without running a step,
  Omega(V(s)) being the length of a walk whose answer was already known.

ONE COLUMN IS VACUOUS AND IS MARKED RATHER THAN QUIETLY SET. The "window
opens, every target" row is not a trajectory question and has no step
count, so it has no outer clock to speak of; it is entered as satisfied
because the INNER clock discharges the question outright, and the rule
that covers it is the full one -- decidable iff the outer clock is
uniform over the policy class AND every object carries an inner clock.
Recording this matters because a column set to make a sort come out is
exactly how a census stops being evidence. (The mark was right and its
SCOPE was too narrow: explore_clock_vacuity.py finds the same emptiness
at the other three decidable rows, so the vacuous column is the rule on
that side of the sort rather than the one exception.)

The sort is a census over the fate questions this corpus has
charted, not a theorem that no other decision mechanism exists; a
decidable-but-clockless instance would refute it and none was found here.
The density, average and abscissa objects are out of scope by
construction -- "inner clock" is undefined for a non-existence object.
Uniformity is always read relative to a row's OWN policy class, so a
singleton class is uniform by construction and the free-policy rows are
where it can fail.

RUN RECORD. Pure Python, no third-party imports; single process, 0.4 s
wall clock, well under the memory ceiling. All checks clean. Primality
above the deterministic Miller-Rabin range (~3.3e24) is a
strong-probable-prime verdict and is labelled as such where it is used,
which is section S5's exponent search alone.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import gcd

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


def omega_big(n):
    """Omega(n) -- prime factors with multiplicity."""
    return sum(factorint(n).values())


_SMALL = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(n):
    if n < 2:
        return False
    for p in _SMALL:
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in _SMALL:
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
    """The largest modulus whose lambda divides L."""
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
    """V(N) = W(lambda(N))/N."""
    W = wall(lam(N))
    assert W % N == 0, "N does not divide W(lambda(N)) at N=%d" % N
    return W // N


def lam_f(f):
    """Carmichael's lambda read off an exponent dictionary."""
    out = 1
    for p, e in f.items():
        if p == 2:
            part = 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
        else:
            part = p ** (e - 1) * (p - 1)
        out = lcm(out, part)
    return out


def mul_f(f, m):
    """The state after a move, as a dictionary; m is small enough to factor."""
    g = dict(f)
    for p, e in factorint(m).items():
        g[p] = g.get(p, 0) + e
    return g


def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
        i += 1
    return [i for i in range(n + 1) if sieve[i]]


# ------------------------------------------------------- the three demands

def adm_independence(N, m):
    return m >= 2 and gcd(m, N) == 1


def adm_dynamics(N, m):
    return m >= 2 and lam(N * m) > lam(N)


def adm_transparency(N, m):
    return m >= 2 and lam(N * m) == lam(N)


# ---------------------------------------------------------------- S1 control

def s1_control():
    print("S1 POSITIVE CONTROL")

    # lambda against the maximum order in the unit group
    bad, agree = [], 0
    for n in range(2, 300):
        best = 1
        for a in range(1, n):
            if gcd(a, n) != 1:
                continue
            o, x = 1, a % n
            while x != 1:
                x = x * a % n
                o += 1
            best = lcm(best, o)
        if best == lam(n):
            agree += 1
        else:
            bad.append(n)
    check(not bad, "lambda disagrees with the unit-group definition at %s" % bad[:5])
    print("  lambda = max unit order, n < 300: %d agreements, %d failures"
          % (agree, len(bad)))

    # W against its own definition, only where the wall fits under the cap
    CAP = 20000
    biggest = {}
    for n in range(1, CAP + 1):
        L = lam(n)
        if L <= 24:
            biggest[L] = max(biggest.get(L, 0), n)
    tested = 0
    bad = []
    for L, seen in sorted(biggest.items()):
        w = wall(L)
        if w > CAP:
            continue          # a truncated search cannot adjudicate this L
        tested += 1
        if w != seen:
            bad.append((L, w, seen))
    check(not bad, "wall formula disagrees with brute search: %s" % bad[:3])
    print("  W(L) = largest modulus with lambda | L: %d values of L adjudicated"
          " under the cap, %d failures" % (tested, len(bad)))

    # transparent moves are exactly the divisors of V, at least 2 -- both
    # directions over a bounded move range, since V itself is unbounded here
    MRANGE = 300
    bad, cells = [], 0
    for N in range(1, 400):
        V = headroom(N)
        for d in divisors(V):
            if d >= 2 and d <= MRANGE:
                cells += 1
                if not adm_transparency(N, d):
                    bad.append((N, d, "divisor not transparent"))
        for m in range(2, MRANGE + 1):
            if V % m:
                cells += 1
                if adm_transparency(N, m):
                    bad.append((N, m, "non-divisor transparent"))
    check(not bad, "transparent-iff-divides-V fails at %s" % bad[:3])
    print("  transparent moves = divisors of V(N) >= 2, N < 400, moves <= %d:"
          " %d cells, %d failures" % (MRANGE, cells, len(bad)))

    # the filed greedy facts this file contrasts against
    N, picks = 1, []
    for _ in range(8):
        m = next(m for m in range(2, 200) if adm_independence(N, m))
        picks.append(m)
        N *= m
    check(picks == [2, 3, 5, 7, 11, 13, 17, 19],
          "independence greedy does not grow the primorial: %s" % picks)
    print("  independence greedy from seed 1: %s" % picks)

    N, steps = 3, 0
    while True:
        m = next((m for m in range(2, 4 * headroom(N) + 4)
                  if adm_transparency(N, m)), None)
        if m is None:
            break
        N *= m
        steps += 1
    check(N == wall(lam(3)),
          "transparency greedy halts at %d, wall is %d" % (N, wall(lam(3))))
    print("  transparency greedy from seed 3: halts at %d in %d steps, wall %d"
          % (N, steps, wall(lam(3))))

    if FAIL:
        print("\nCONTROL FAILED -- no verdict below is readable.")
        sys.exit(1)
    print("  control clean\n")


# ------------------------------------------------- S2 mortality, every policy

def s2_mortality():
    print("S2 MORTALITY UNDER EVERY POLICY (the uniform clock)")
    print("  seed   W(lam(s))   |reach|  lattice?  terminals  longest  Omega(V)")

    for s in (1, 2, 3, 5, 7, 9, 12, 25, 27, 49):
        W = wall(lam(s))
        # exhaust the free policy's reachable set
        seen, frontier = {s}, [s]
        terminals = set()
        while frontier:
            nxt = []
            for N in frontier:
                V = headroom(N)
                moves = [d for d in divisors(V) if d >= 2]
                if not moves:
                    terminals.add(N)
                for m in moves:
                    if N * m not in seen:
                        seen.add(N * m)
                        nxt.append(N * m)
            frontier = nxt
        lattice = set(s * d for d in divisors(W // s))
        ok = (seen == lattice)
        check(ok, "reachable set is not the predicted lattice at seed %d" % s)
        check(terminals == {W},
              "terminal states at seed %d are %s, wall %d"
              % (s, sorted(terminals), W))

        # longest chain, by depth-first descent over the divisor lattice
        depth = {}

        def longest(N):
            if N in depth:
                return depth[N]
            V = headroom(N)
            best = 0
            for m in divisors(V):
                if m >= 2:
                    best = max(best, 1 + longest(N * m))
            depth[N] = best
            return best

        L = longest(s)
        bound = omega_big(headroom(s))
        check(L == bound,
              "longest transparent chain at seed %d is %d, Omega(V) is %d"
              % (s, L, bound))
        print("  %4d   %9d   %6d   %5s     %-9s %5d    %5d"
              % (s, W, len(seen), "yes" if ok else "NO",
                 sorted(terminals), L, bound))
    print()


# ------------------------------------------ S3 independence and the trichotomy

def s3_independence():
    print("S3 INDEPENDENCE: DOES A FREE POLICY LEAVE THE TRICHOTOMY?")

    # (a) no admissible move disturbs a seated prime's exponent. This is a
    # TAUTOLOGY given the demand -- gcd(m, N) = 1 and l | N force l not to
    # divide m -- so the sweep is a consistency check on the engine, not
    # evidence for anything. It is kept because the CONSEQUENCE (no policy
    # reaches depth) is the load-bearing step, and it is worth seeing that
    # the implemented admissibility really does have this shape.
    moved, tested = 0, 0
    for N in range(2, 400):
        for m in range(2, 120):
            if not adm_independence(N, m):
                continue
            tested += 1
            for l in factorint(N):
                if v_p(N * m, l) != v_p(N, l):
                    moved += 1
    check(moved == 0, "%d admissible moves disturbed a seated exponent" % moved)
    print("  seated exponents disturbed by an admissible move: %d of %d moves"
          " (a tautology given the demand -- engine consistency, not evidence)"
          % (moved, tested))

    # (b) the admissible set is never empty
    empty = [N for N in range(1, 3000)
             if not any(adm_independence(N, m) for m in range(2, 200))]
    check(not empty, "no admissible independence move at %s" % empty[:3])
    print("  states below 3000 with no admissible move: %d of 2999"
          % len(empty))

    # (c) a FIRST move may seat any finite depth -- so what blocks depth is
    #     the infinitude of pushes, not a bound on one move
    depths = [e for e in range(1, 9) if adm_independence(2, 3 ** e)]
    print("  depths a single move can seat at N=2 (3^e, e=1..8): %s" % depths)

    # (d) the avoiding policy
    AVOID = 7
    facs, seated, steps = {}, [], 0
    while steps < 300:
        m = next(m for m in range(2, 5000)
                 if m % AVOID != 0
                 and all(p not in facs for p in factorint(m)))
        facs = mul_f(facs, m)
        seated.append(m)
        steps += 1
    maxdepth = max(facs.values())
    print("  avoiding policy (never a multiple of %d), %d steps:" % (AVOID, steps))
    print("    first picks       : %s" % seated[:12])
    print("    primes seated     : %d" % len(facs))
    print("    max depth reached : %d" % maxdepth)
    print("    is %d seated      : %s" % (AVOID, AVOID in facs))
    check(AVOID not in facs, "the avoided prime got seated")
    check(maxdepth == 1, "the avoiding policy reached depth %d" % maxdepth)

    print("    verdict against the three classes:")
    print("      MORTALITY  no -- the admissible set was never empty (b)")
    print("      DEPTH      no -- every depth is 1, and (a) freezes it there")
    print("      BREADTH    no -- %d is never seated, and BREADTH is EVERY"
          " prime" % AVOID)
    print("    so the limit lies outside all three classes.")
    print()


# ------------------------------------------------- S4 one law, two fates

def s4_dynamics():
    print("S4 DYNAMICS: ONE LAW, TWO FATES")

    # the filed greedy policy: least lambda-raising move
    f, picks = {}, []
    for _ in range(14):
        cur = lam_f(f)
        m = next(m for m in range(2, 4000) if lam_f(mul_f(f, m)) > cur)
        picks.append(m)
        f = mul_f(f, m)
    print("  greedy from seed 1: %s" % picks)
    print("    last six picks carry the primes: %s"
          % [sorted(factorint(p)) for p in picks[-6:]])
    lock = set()
    for p in picks[-6:]:
        lock |= set(factorint(p))
    check(len(lock) == 1,
          "the greedy tail is not a single prime's column: %s" % sorted(lock))
    print("    column: %s (the lock)" % sorted(lock))

    # the padded free policy under the SAME admissibility test
    CAP = 100
    f = {}
    steps, padded, rises = 0, 0, 0
    for p in primes_upto(CAP):
        if p in f:
            continue
        before = lam_f(f)
        if lam_f(mul_f(f, p)) > before:
            m = p
        else:
            # the operative condition: (q-1) must not divide lambda, which
            # is exactly what makes the lcm move, and admits a small q
            q = next(q for q in range(3, 100000)
                     if is_prime(q) and q not in f and before % (q - 1))
            m = p * q
            padded += 1
        after = lam_f(mul_f(f, m))
        check(after > before,
              "padded move %d at lambda %d is inadmissible" % (m, before))
        f = mul_f(f, m)
        steps += 1
        if after > before:
            rises += 1
    facs = f
    missing = [p for p in primes_upto(CAP) if p not in f]
    print("  padded free policy, seating every prime <= %d:" % CAP)
    print("    steps %d, of which padded %d; lambda rose at %d of %d"
          % (steps, padded, rises, steps))
    print("    primes below the cap left unseated: %s" % missing)
    print("    primes seated in all: %d, max depth %d"
          % (len(facs), max(facs.values())))
    check(not missing, "the padded policy missed %s" % missing[:5])
    check(rises == steps, "lambda failed to rise at %d steps" % (steps - rises))
    check(max(facs.values()) == 1, "the padded policy deepened a prime")
    print("    so the same law hosts the lock AND a trajectory seating every"
          " prime at depth 1.")
    print()


# ------------------------------------------------------------ S5 the census

def s5_census():
    print("S5 THE CLOCK CENSUS")

    # the settled side: the least prime in an arithmetic progression
    worst = (0, 0)
    for B in range(2, 201):
        p = next(p for p in range(B + 1, 400 * B + 400, B) if is_prime(p))
        if p // B > worst[0]:
            worst = (p // B, B)
    print("  least prime = 1 mod B, B = 2..200: found by bounded search at"
          " every modulus")
    print("    worst ratio p/B: %d at B = %d (a classical bound covers the"
          " search)" % worst)

    # the open side: the least exponent with m*2^a + 1 prime
    small = primes_upto(1000)
    prime_powers = []
    for n in range(3, 60, 2):
        f = factorint(n)
        if len(f) == 1:
            prime_powers.append(n)
    least_a, big = {}, 0
    for m in prime_powers:
        a = 1
        while a <= 700:
            cand = m * (1 << a) + 1
            if not any(cand % s == 0 for s in small if s * s <= cand):
                if is_prime(cand):
                    break
            a += 1
        least_a[m] = a if a <= 700 else None
        if least_a[m]:
            big = max(big, least_a[m])
    print("  least a with m*2^a + 1 prime, m an odd prime power < 60:")
    print("    %s" % ", ".join("%d:%s" % (m, least_a[m]) for m in prime_powers))
    print("    spread: %d of %d land at a <= 8, the largest is %d"
          % (sum(1 for m in prime_powers if least_a[m] and least_a[m] <= 8),
             len(prime_powers), big))
    print("    (witnesses above ~3.3e24 are strong probable primes)")

    # the certificate that no clock can exist family-wide
    COVER = (3, 5, 7, 13, 19, 37, 73)
    uncovered = []
    for a in range(36):
        n = 78557 * (1 << a) + 1
        if not any(n % q == 0 for q in COVER):
            uncovered.append(a)
    check(not uncovered, "78557's covering set misses a = %s" % uncovered[:4])
    ords = [next(o for o in range(1, 100) if pow(2, o, q) == 1) for q in COVER]
    period = 1
    for o in ords:
        period = lcm(period, o)
    print("  covering certificate at 78557: residues %s, orders of 2 %s,"
          % (list(COVER), ords))
    print("    joint period %d, exponents 0..35 uncovered: %d -- so the search"
          " never ends" % (period, len(uncovered)))

    # the alphabet chain: smooth shifted primes
    LIM = 10 ** 6
    ps = primes_upto(LIM)
    for S in ({2}, {2, 3}, {2, 3, 5}, {2, 3, 5, 7}):
        cnt = 0
        for p in ps:
            n = p - 1
            for q in S:
                while n % q == 0:
                    n //= q
            if n == 1:
                cnt += 1
        print("  S-smooth shifted primes below %d, S = %-12s: %d"
              % (LIM, sorted(S), cnt))

    # ---- the sort, and the frozen rule's own kill --------------------
    # Uniformity is read RELATIVE TO THE ROW'S OWN POLICY CLASS, so a
    # singleton class (greedy, or one named trajectory) is uniform by
    # construction; the free-policy rows are where it can fail.
    fates = [
        # name, outer clock, uniform over its class, hardness construction,
        # level, filed status
        ("mortality, transparency, free policy", 1, 1, 0, "decidable",
         "decidable"),
        ("breadth, independence, greedy",        1, 1, 0, "decidable",
         "decidable"),
        ("depth, dynamics, greedy",              1, 1, 0, "decidable",
         "decidable"),
        ("window opens, every target",           1, 1, 0, "Pi_2 surface",
         "decidable"),
        ("fate, sighted hosting law, free",      0, 0, 1, "undecidable",
         "undecidable"),
        ("carrier ladder halts, one start",      0, 1, 0, "Sigma_1", "open"),
        ("carrier ladder halts, all starts",     0, 0, 0, "Pi_2", "open"),
    ]

    # The rule as frozen: two-valued, reading absence of a clock as a
    # verdict. It is printed FIRST because its mismatch is the finding.
    frozen_mism = 0
    for name, out, uni, hard, lvl, filed in fates:
        pred = "decidable" if (out and uni) else (
            "undecidable" if not uni else "open")
        if pred != filed:
            frozen_mism += 1
    print()
    print("  THE SORT AS FROZEN (decidable / undecidable, no third value):"
          " %d mismatches" % frozen_mism)
    print("    the mismatching row is 'carrier ladder halts, all starts' --"
          " clockless and")
    print("    non-uniform, which the frozen rule calls UNDECIDABLE while"
          " the corpus files")
    print("    it OPEN. Absence of a clock was being read as proof that"
          " none exists.")

    # The repaired rule, which the same run's rows support but which was
    # NOT predicted in advance: undecidability needs a POSITIVE hardness
    # construction, and open is the absence of both.
    print()
    print("  FATE QUESTIONS -- outer clock, uniformity, hardness, and the"
          " three-valued sort")
    print("  %-36s %-6s %-8s %-6s %-13s %-11s"
          % ("question", "outer", "uniform", "hard", "level", "filed"))
    mism = 0
    for name, out, uni, hard, lvl, filed in fates:
        pred = "decidable" if (out and uni) else (
            "undecidable" if hard else "open")
        flag = ""
        if pred != filed:
            mism += 1
            flag = "  <-- MISMATCH"
        # a row may not be both clocked and hard; that would be a contradiction
        check(not (out and uni and hard),
              "row '%s' claims a clock and a hardness construction" % name)
        print("  %-36s %-6s %-8s %-6s %-13s %-11s%s"
              % (name, "yes" if out else "no", "yes" if uni else "no",
                 "yes" if hard else "no", lvl, filed, flag))
    print("  mismatches under the repaired rule: %d" % mism)
    check(mism == 0, "%d rows sit on the wrong side of the repaired sort" % mism)
    print("    'window opens, every target' is NOT a trajectory question --"
          " it has no step")
    print("    count, so its outer column is VACUOUS and the inner clock"
          " below is what")
    print("    decides it; it is carried here because the corpus files it"
          " as a growth fate.")
    print("    the two carrier rows differ in UNIFORMITY alone, and that"
          " moves the LEVEL")
    print("    (Sigma_1 -> Pi_2) while leaving the STATUS open -- level and"
          " status are")
    print("    separate readings, which the frozen rule had fused.")

    print()
    print("  THE OBJECTS these questions reduce to -- the inner clock")
    print("  %-40s %-6s %-11s" % ("object", "inner", "status"))
    objs = [
        ("prime in an arithmetic progression", 1, "settled"),
        ("m*2^a + 1 prime, one base", 0, "open"),
        ("S-smooth shifted primes infinite", 0, "open"),
        ("carrier prime in a linear window", 0, "open"),
    ]
    for name, inn, status in objs:
        pred = "settled" if inn else "open"
        check(pred == status, "object '%s' sits on the wrong side" % name)
        print("  %-40s %-6s %-11s" % (name, "yes" if inn else "no", status))
    print("    and the second row carries a certificate that no clock can"
          " exist family-wide,")
    print("    which is a stronger fact than the first row's clock and"
          " still not a decision.")
    print("  OUT OF SCOPE (a change of kind, not a level): the density,"
          " average and")
    print("  abscissa objects -- 'inner clock' is undefined for a"
          " non-existence object.")
    print()


def main():
    s1_control()
    s2_mortality()
    s3_independence()
    s4_dynamics()
    s5_census()
    print("=" * 68)
    if FAIL:
        print("FAILURES: %d" % len(FAIL))
        for f in FAIL:
            print("  " + f)
        sys.exit(1)
    print("all checks clean")


if __name__ == "__main__":
    main()
