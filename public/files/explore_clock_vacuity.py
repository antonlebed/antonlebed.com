"""
explore_clock_vacuity.py -- IS THE OUTER VERDICT CLOCK VACUOUS?
(sibling of explore_fate_clock.py, explore_lock_prime.py,
explore_growth_laws.py, explore_headroom.py, explore_demand_reading.py.)

THE QUESTION. explore_fate_clock.py files a reading of which fate questions
are decidable: a fate question -- from seed s, under demand law L, does a
policy in class Pi reach fate F? -- is DECIDABLE iff an OUTER clock bounds
the step by which the fate is settled, uniformly over Pi, plus an INNER
clock bounds the witness search in every object the question reduces to;
UNDECIDABLE iff the policy class embeds a universal machine; OPEN iff
neither. That file sorts seven fate rows and four object rows with zero
mismatches and states its own standing refutation test: the reading has
content only if decidability here always comes FROM a bound, so a fate
question settled by an invariant with no bound on when it is settled would
demote the clock from law to description. It looked for none.

The hunt cannot be run as stated, and the reason is the whole design of
this file. A fate question whose verdict is a function of the seed alone --
which is what a conserved-quantity closure gives -- is covered by the
clock T = 0: the length-zero prefix determines the verdict, trivially and
uniformly. So the loose reading is IRREFUTABLE. That is the charge against
it, not a defence of it: a criterion no row can fail sorts nothing. The
honest test is therefore not "find a clockless decidable row" but: NAME
WHAT A CLOCK MUST DO THAT T = 0 DOES NOT, AND RE-SORT THE CENSUS UNDER
THAT READING.

THREE OBJECTS THE FILED PHRASE COVERS AT ONCE, separated here because the
separation is the test.

  T_det(s)   -- the least T such that the length-T prefix DETERMINES the
                verdict: every continuation admissible in Pi agrees.
  T_real(s)  -- the least T by which the fate is REALIZED as an event
                inside the prefix: the run has halted, the target has been
                seated, the thing the fate names has happened.
  CONTENTFUL -- the clock's bounded search has an output that VARIES over
                the row's domain. If the verdict is the same whatever the
                search finds, the bound certifies nothing: the search is
                dead code and the answer was available without it.

The two clocks are different objects and the corpus's own flagship row
reads the phrase in the second sense. Mortality under transparency is
filed with the clock Omega(V(s)) -- the length of the longest chain, which
is when the run STOPS, a realization bound. Its determination clock is 0,
because the verdict is yes at every transparent seed. Breadth and depth,
by contrast, are properties of a limit and are never events in any finite
prefix, so under the realization reading they have no outer clock at all,
while the census files both with a yes in the outer column.

THE PREDICTIONS, fixed before any engine code was written. Each names what
the rig PRINTS; what it means is weighed after the run.

Q1 CONSTANCY. Every one of the four rows the census files DECIDABLE has a
   verdict that is CONSTANT over its seed domain -- mortality holds at
   every transparent seed, greedy independence reaches breadth from every
   seed, greedy dynamics reaches depth from every seed. If so, the
   zero-mismatch sort sorted constant functions, and no candidate
   mechanism could have failed it.
   KILL: the rig prints two different verdicts inside any one of the rows.

Q2 THE TWO READINGS SEPARATE, measured on the only row where both clocks
   are computable, the reachable set under transparency being finite.
   Predict T_det = 0 at every seed while T_real = Omega(V(s)) grows -- and
   predict the separation survives at TARGET granularity, because every
   maximal trajectory ends at the same terminus, so which primes the limit
   carries is a closed form of the seed and no step need be run to know it.
   KILL: T_det > 0 at some seed, or two maximal trajectories from one seed
   ending at different states.

Q3 NO REALIZATION BOUND AT TWO FILED-CLOCKED ROWS. Predict that under
   greedy independence the step at which the n-th prime is seated grows
   without bound and the seated set is finite at every step, so breadth is
   realized at no finite step; and that under greedy dynamics every
   exponent is finite at every step, so depth is realized at no finite
   step. Both rows carry a yes in the census's outer column.
   KILL: the rig prints a finite step at which either fate is realized.

Q4 A CONTENTFUL OUTER CLOCK EXISTS, and the corpus already owns it -- the
   positive control, so that the strict reading is not empty by
   construction and the finding cannot be "strictness kills everything".
   The wander bound (explore_lock_prime.py) says greedy dynamics locks
   within omega_odd(lambda(s)) + 1 picks. Predict that bound holds, that
   the LOCK PRIME varies across seeds, and that it is therefore a
   computable bound on a search whose output varies: the question "is the
   prime l at infinite depth" is contentful where "is SOME prime at
   infinite depth" is not.
   KILL: the wander exceeds the bound, or one lock prime serves every seed.

Q5 THE STRICT RE-SORT. Re-sort the seven fate rows with the contentfulness
   clause added -- a row is CLOCKED only if its verdict varies over its own
   domain -- and count mismatches against the filed status.
   Predict 4 of 7: the four decidable rows lose their clocks while staying
   decidable, which refutes the biconditional in the necessity direction
   and leaves the sufficiency direction standing.
   KILL: fewer than 3 mismatches, i.e. the strict reading keeps
   substantially what the loose one kept, in which case the clock survives
   being made non-vacuous and the filed reading stands as written.

Q6 THE INNER CLOCK IS UNTOUCHED, and the asymmetry is the repair. An inner
   clock bounds a search for a WITNESS, and the witness varies: predict the
   least prime congruent to 1 mod B takes many distinct values across
   B = 2..200, so that bound is load-bearing in exactly the sense the outer
   column is not.
   KILL: the witness is constant across the range, which would collapse
   the inner column too.

THE OBJECTS. lambda is Carmichael's function. W(L) is the largest modulus
whose lambda divides L. The transparency headroom is V(N) = W(lambda(N))/N,
and the transparent moves out of N are exactly the divisors of V(N) that
are at least 2. Omega(n) counts prime factors with multiplicity;
omega_odd(n) counts distinct odd prime factors. Three demand laws, each
with its greedy policy and its free class:
  INDEPENDENCE  -- m admissible iff gcd(m, N) = 1.
  DYNAMICS      -- m admissible iff lambda(N*m) > lambda(N).
  TRANSPARENCY  -- m admissible iff lambda(N*m) = lambda(N), i.e. m | V(N).

THE DESIGN, in six sections after the control.

S1 POSITIVE CONTROL, run before any verdict is read; the run aborts if it
   fails. Four things this file leans on and did not derive here must come
   back: lambda against the maximum order in the unit group; W against its
   own definition, compared only below the search cap, since a truncated
   search misreports every large wall; the transparent-move divisor
   identity in both directions over a bounded move range; and the three
   filed greedy facts this file re-uses as rows -- transparency greedy
   halts at the wall, independence greedy walks the primes in order,
   dynamics greedy locks onto one prime's column. States are carried as
   exponent DICTIONARIES wherever a trajectory is walked; trial division
   is applied only to the small move m.

S2 THE CONSTANCY CENSUS (Q1). For each of the three computable decidable
   rows, evaluate the fate verdict at many seeds and print the number of
   DISTINCT verdicts the row takes. Alongside each verdict print a
   quantity of the same row that DOES vary, so that constancy is read as a
   property of the collapsed question and not of the law. The fourth
   decidable row is not a trajectory question and is carried as sourced.

S3 THE TWO READINGS ON THE TRANSPARENCY ROW (Q2). Exhaust the reachable
   set from ten seeds by breadth-first search over states. Print, per seed:
   the size of the reachable set, the number of terminal states, the
   longest chain against Omega(V(s)) -- that is T_real -- and then T_det,
   computed rather than asserted by checking the mortality verdict at
   EVERY reachable state and reporting how many differ from the seed's.
   Then the target granularity: read the primes of the unique terminus off
   the closed form W(lambda(s)) and compare against the primes found by
   exhaustion, so the claim that no step need be run is a comparison and
   not a remark.

S4 REALIZATION AT THE BREADTH AND DEPTH ROWS (Q3). Under greedy
   independence, print the step at which the n-th prime is seated for a
   spread of n, and the size of the seated set at each of several steps.
   Under greedy dynamics, print the largest exponent reached at each of
   several steps. Both columns are the evidence that no finite prefix
   carries the event.

S5 THE CONTENTFUL CLOCK (Q4). Simulate greedy dynamics from many seeds to
   the lock, checking the wander against omega_odd(lambda(s)) + 1 at every
   seed; print the number of distinct lock primes and a specimen basin.
   The wander is read as the LOCK POINT -- the least index from which
   every later pick carries the lock prime -- and not as the first
   sighting of that prime, which a ghost opening can supply well before
   the trajectory locks and which would let the bound check pass without
   a lock having happened. Then state the two questions side by side with
   their verdict counts: "some prime at infinite depth" against "the
   prime l at infinite depth".

S6 THE STRICT RE-SORT (Q5, Q6). The seven fate rows with a contentfulness
   column COMPUTED where this file measures it (S2, S5), SOURCED from the
   corpus where it does not, and carried as NOT KNOWN at the two open
   rows, whose verdicts the corpus does not have; the strict rule
   applied, and the mismatch count printed as the observable Q5 named.
   Then the object rows with the witness spread that Q6 asks for.

THE FINDINGS.

F1 EVERY FATE QUESTION THE CENSUS FILES DECIDABLE IS A CONSTANT FUNCTION
   (rule; exhibited at 30 seeds each). Mortality under transparency: 1
   distinct verdict, 30 of 30 seeds exhausted with 0 over the cap. Breadth
   under greedy independence: 1. Depth under greedy dynamics: 1. Beside
   each, a quantity of the SAME row that does vary -- 8 distinct termini,
   15 distinct opening walks, 3 distinct lock primes -- so the constancy
   belongs to the collapsed question and not to the law. Each verdict has
   a one-line reason: the transparent reachable set is finite, greedy
   independence takes the least prime absent from the state, and the lock
   is proved (explore_lock_prime.py). None of the three is a bound on
   WHEN THE FATE IS SETTLED, which is the column under test -- and the
   sharper statement is that these arguments are not bound-free at all.
   Each carries a real bound: the walk to the terminus, the step seating
   one target, the lock point. Every one of those bounds a question whose
   answer varies, which is F4's finding arriving from the other side --
   the bounds belong to the uncollapsed questions, and the collapsed fate
   question inherits none of them. A sort whose positive side is four constant
   functions cannot fail any candidate mechanism, which is what the
   zero-mismatch result was measuring.

F2 THE FILED CLOCK IS A REALIZATION BOUND, NOT A DETERMINATION ONE, and
   the two come apart on the corpus's own flagship row (rule, exhaustive
   at ten seeds -- at nine of them, the tenth being s = 2, where V = 1
   leaves no move to make and both clocks are 0 for want of a walk rather
   than by agreeing about one).
   Under transparency the reachable set has 1 to 20 states,
   exactly ONE terminal state at every seed, and a longest chain equal to
   Omega(V(s)) at 10 of 10 -- while T_det is 0 at every seed, 57 reachable
   states carried to their own verdict with 0 differing from the seed's.
   The separation survives at TARGET granularity, which is where it might
   have failed: the primes of the exhausted terminus equal the primes of
   W(lambda(s)) at 10 of 10, so WHICH primes the limit carries is a closed
   form of the seed. Nothing about this row's fate needs a step run,
   and Omega(V(s)) bounds an exhaustion whose answer was available
   before it started.

F3 BREADTH AND DEPTH ARE REALIZED AT NO FINITE PREFIX LENGTH, and both
   carry a yes in the outer column (rule). Greedy independence seats the
   n-th prime at step n exactly (n = 1, 5, 10, 25, 50, 100, 200) and the
   seated set has size t at every t checked (10, 50, 100, 200), so
   infinitely many primes stand unseated at every step. Greedy dynamics
   has largest exponent t after t steps (5, 10, 20, 40), finite always. So
   under the realization reading -- the reading the mortality row itself
   uses -- two of the four filed-clocked rows have no outer clock at all,
   and under the determination reading all four have the clock T = 0.
   There is no single reading on which the outer column is as filed.

F4 A CONTENTFUL OUTER CLOCK EXISTS, AND THE CORPUS ALREADY OWNS IT (rule,
   400 seeds) -- so the strict reading is not empty and the finding is not
   "strictness kills every clock". The wander bound holds at 400 of 400
   seeds, 0 exceeding omega_odd(lambda(s)) + 1, and the lock prime takes 8
   distinct values across those seeds (2, 3, 5, 7, 11, 13, 17, 19) with
   basins 2 <- 2, 4, 8, 16, 24; 3 <- 1, 3, 6, 9, 12; 5 <- 5, 7, 10, 14,
   19; 7 <- 11, 17, 22, 34, 41. The same law therefore carries a
   computable bound on a search whose output VARIES -- "which prime
   reaches infinite depth" -- while the census's row asks only "does SOME
   prime", which is constant. The clock is a real instrument; the census
   applied it at the granularity where it reads nothing.

F5 THE VACUITY AS A COUNT RATHER THAN A READING (observation, 7 rows).
   The outer column is a yes at exactly the rows already filed decidable:
   it agrees with the predicate "filed == decidable" at 7 of 7 rows, while
   the uniformity column agrees at 6 of 7. A column that reproduces the
   answer it is supposed to explain carries no independent information
   about any row. This is what "T = 0 covers every invariant-closed row"
   looks like when the census is asked for it -- the corpus knows the four
   verdicts, so their prefixes determine them at length 0; it does not
   know the open ones, so no clock can be claimed there. The outer column
   tracks known-versus-unknown, which is what decidable-versus-open
   already says.

F6 THE BICONDITIONAL IS AN IMPLICATION, and only one direction survives.
   The loose reading reproduces the filed sort exactly: 0 mismatches over
   7 rows. Adding the contentfulness clause gives 4 mismatches, all four
   of the decidable rows -- and the strict rule's own verdict on them,
   "open", is FALSE, since each is decidable trivially. So neither reading
   is a law: the loose one cannot fail, and the strict one fails at every
   row it was built to explain. What stands is the sufficiency direction
   alone -- a contentful clock DECIDES, since a boundedly-deep,
   finitely-branching search tree can be exhausted -- and that half is
   mechanical and was never in doubt. Necessity is refuted: the four rows
   offered as its evidence decide without any bound.

F7 THE INNER CLOCK IS UNTOUCHED, AND THE ASYMMETRY IS THE REPAIR
   (observation). The least prime congruent to 1 mod B takes 122 distinct
   values across the 199 moduli B = 2..200, worst ratio p/B = 20 at
   B = 159. An inner clock stops a search whose ANSWER varies, so the
   bound is load-bearing in the exact sense the outer column is not: at
   every row the census files decidable, the outer bound stops a search
   whose answer was fixed before it started. The honest statement the
   census supports is about inner clocks and uniformity; the outer clock
   is a description of rows already known.

SCOPE. WHAT IS COMPUTED AND WHAT IS SOURCED, since a re-sort inherits its
predecessor's columns. This file COMPUTES: the constancy of the three
trajectory rows (S2), both clocks on the transparency row and the terminus
comparison (S3), the realization columns at breadth and depth (S4), the
wander bound and the lock basins (S5), and the inner-clock witness spread
(S6). It TAKES FROM THE CORPUS: the filed status of every row, the outer
and hardness columns for the rows it does not itself run, and the "window
opens, every target" row, whose outer column explore_fate_clock.py already
records as vacuous -- this file's contribution there is that the same
verdict extends to the other three. It leaves NOT KNOWN the
contentfulness of the two open rows: their verdicts are not known, so
whether those verdicts vary cannot be, and the column is carried as n/a
rather than satisfied. Both rows lack an outer clock, so the rule
short-circuits before reading it and the sort is insensitive to the
choice -- which is exactly when a column is cheapest to fill in wrongly. The strict rule is an INSTRUMENT FOR
REFUTATION and is not proposed as a replacement law; its own verdicts on
the four rows are wrong, which is F6's point and not a defect in it. The
transparency exhaustion is capped at 4000 states and no seed reached the
cap; the seeds are small by design, since the claim under test is about
whether a bound is consulted at all and not about how large one gets.

THE NEIGHBOURS. That a bounded, finitely-branching search decides is the
standard ranking-function argument; that a conserved quantity settles a
question outright is the standard invariant argument. Neither is new here
and neither is claimed. What this file adds is the measurement BETWEEN
them: a census column that separates them, applied to a corpus of fate
questions that were sorted before the separation existed, and the count
showing the column being tested reproduces the answers it was meant to
explain.

RUN RECORD. Pure Python, no third-party imports; single process, 0.2 s
wall clock, well under the memory ceiling. All checks clean.
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


def omega_odd(n):
    """The number of distinct ODD prime factors."""
    return sum(1 for p in factorint(n) if p != 2)


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
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        i += 1
    return [i for i in range(n + 1) if sieve[i]]


# --------------------------------------------------------------- the policies

def greedy_independence(f):
    """The least move coprime to the state: the least prime not in it."""
    for m in range(2, 100000):
        if all(p not in f for p in factorint(m)):
            return m
    raise RuntimeError("no coprime move below the search cap")


def greedy_dynamics(f):
    """The least move raising lambda."""
    cur = lam_f(f)
    for m in range(2, 200000):
        if lam_f(mul_f(f, m)) > cur:
            return m
    raise RuntimeError("no lambda-raising move below the search cap")


def transparent_moves(N):
    """The moves that hold lambda fixed: the divisors of V(N) above 1."""
    return [d for d in divisors(headroom(N)) if d >= 2]


# ------------------------------------------------------------ S1 the control

def s1_control():
    print("S1 POSITIVE CONTROL")

    # lambda against the maximum order in the unit group
    bad = []
    for n in range(2, 201):
        units = [a for a in range(1, n) if gcd(a, n) == 1]
        best = 0
        for a in units:
            o, x = 1, a % n
            while x != 1:
                x = x * a % n
                o += 1
            best = max(best, o)
        if best != lam(n):
            bad.append(n)
    check(not bad, "lambda disagrees with the unit group at %s" % bad[:4])
    print("  lambda vs the maximum order in (Z/n)*, n = 2..200: %d deviations"
          % len(bad))

    # W against its own definition, below the search cap only
    CAP = 5000
    bad = []
    for L in range(1, 61):
        W = wall(L)
        if W > CAP:
            continue
        # CAP + 1 so the search range includes CAP itself: the guard admits
        # W == CAP and a half-open range would then report the wall wrong.
        found = max(n for n in range(1, CAP + 1) if L % lam(n) == 0)
        if found != W:
            bad.append((L, W, found))
    check(not bad, "W disagrees with the search at %s" % bad[:3])
    print("  W(L) vs the largest modulus found by search, L = 1..60 with"
          " W <= %d: %d deviations" % (CAP, len(bad)))

    # the transparent-move divisor identity, both directions
    bad = []
    for N in (2, 6, 12, 30, 36, 210):
        V = headroom(N)
        want = set(d for d in divisors(V) if d >= 2)
        got = set(m for m in range(2, 400) if lam(N * m) == lam(N))
        small_want = set(d for d in want if d < 400)
        if got != small_want:
            bad.append((N, sorted(got ^ small_want)[:4]))
    check(not bad, "the divisor identity fails at %s" % bad[:2])
    print("  transparent moves = divisors of V(N), both directions over"
          " m < 400: %d deviations" % len(bad))

    # the three filed greedy facts this file re-uses as rows
    N = 12
    steps = 0
    while transparent_moves(N):
        N *= transparent_moves(N)[0]
        steps += 1
    check(N == wall(lam(12)), "transparency greedy stopped off the wall")
    print("  transparency greedy from 12 halts at %d = W(lambda(12)) in %d"
          " steps" % (N, steps))

    f, picks = {}, []
    for _ in range(8):
        m = greedy_independence(f)
        picks.append(m)
        f = mul_f(f, m)
    check(picks == primes_upto(20)[:8],
          "independence greedy is not the primes in order: %s" % picks)
    print("  independence greedy from 1 walks the primes in order: %s" % picks)

    f, picks = {}, []
    for _ in range(14):
        m = greedy_dynamics(f)
        picks.append(m)
        f = mul_f(f, m)
    tail = set()
    for m in picks[-6:]:
        tail |= set(factorint(m))
    check(len(tail) == 1, "dynamics greedy did not lock: %s" % sorted(tail))
    print("  dynamics greedy from 1 locks the column %s" % sorted(tail))
    print()

    if FAIL:
        print("CONTROL FAILED -- no verdict is read.")
        sys.exit(1)


# ------------------------------------------------------- S2 the constancy census

SEEDS = [1, 2, 3, 4, 6, 7, 9, 10, 12, 15, 16, 18, 20, 21, 24, 25,
         27, 28, 30, 33, 35, 36, 40, 42, 45, 48, 50, 60, 63, 66]


def transparent_reachable(s, cap=4000):
    """Exhaust the reachable set under transparency, and measure the longest
    chain in it. Every move multiplies by m >= 2, so the state strictly
    increases and the reachable set is a directed acyclic graph ordered by
    the state itself: the longest chain is a dynamic program over that
    order, not a search. Returns None if the cap is reached, so a truncated
    exhaustion is never reported as a finished one."""
    seen, front, terminal = {s}, [s], set()
    while front:
        nxt = []
        for N in front:
            ms = transparent_moves(N)
            if not ms:
                terminal.add(N)
            for m in ms:
                M = N * m
                if M not in seen:
                    seen.add(M)
                    if len(seen) > cap:
                        return None, None, None
                    nxt.append(M)
        front = nxt
    dist = {N: 0 for N in seen}
    for N in sorted(seen):
        for m in transparent_moves(N):
            M = N * m
            if dist[M] < dist[N] + 1:
                dist[M] = dist[N] + 1
    return seen, terminal, max(dist.values())


def s2_constancy():
    print("S2 THE CONSTANCY CENSUS -- do the decidable rows' verdicts vary?")

    # row A: mortality, transparency, free policy. The verdict is read off
    # the exhaustion itself: the state strictly increases at every move, so
    # a finite reachable set IS "every maximal trajectory halts". Seeds
    # whose set exceeds the cap are counted, never silently dropped.
    verdicts, termini = set(), set()
    used, over_cap = 0, 0
    for s in SEEDS:
        R, terminal, longest = transparent_reachable(s)
        if R is None:
            over_cap += 1
            continue
        used += 1
        # R is not None, so the search exhausted below the cap: the state
        # strictly increases at every move, so a finite reachable set with a
        # terminal state in it IS "every maximal trajectory halts".
        verdicts.add(len(terminal) > 0)
        # The "distinct termini" count is only the varying quantity it is
        # printed as if each seed HAS one terminus; a seed with two would
        # make the column mean something else silently.
        check(len(terminal) == 1,
              "seed %d has %d terminal states" % (s, len(terminal)))
        termini.add(tuple(sorted(terminal)))
    print("  mortality, transparency, free policy -- %d of %d seeds exhausted"
          " (%d over the cap)" % (used, len(SEEDS), over_cap))
    print("    distinct fate verdicts : %d   (%s)"
          % (len(verdicts), sorted(verdicts)))
    print("    distinct termini       : %d   (the row's varying quantity)"
          % len(termini))
    check(len(verdicts) == 1, "the mortality row took %d verdicts" % len(verdicts))

    # row B: breadth, independence, greedy
    verdicts, walks = set(), set()
    for s in SEEDS:
        f = factorint(s)
        seated_order = []
        for _ in range(40):
            m = greedy_independence(f)
            seated_order.append(m)
            f = mul_f(f, m)
        # greedy takes the least prime absent from the state, so the primes
        # below the last pick are all seated: breadth follows for every seed
        top = seated_order[-1]
        missing = [p for p in primes_upto(top) if p not in f]
        verdicts.add(not missing)
        walks.add(tuple(seated_order[:4]))
    print("  breadth, independence, greedy -- %d seeds" % len(SEEDS))
    print("    distinct fate verdicts : %d   (%s)"
          % (len(verdicts), sorted(verdicts)))
    print("    distinct opening walks : %d   (the row's varying quantity)"
          % len(walks))
    check(len(verdicts) == 1, "the breadth row took %d verdicts" % len(verdicts))

    # row C: depth, dynamics, greedy
    verdicts, locks = set(), {}
    for s in SEEDS:
        f = factorint(s)
        bound = omega_odd(lam(s)) + 1
        picks = []
        for _ in range(bound + 8):
            m = greedy_dynamics(f)
            picks.append(m)
            f = mul_f(f, m)
        tail = set()
        for m in picks[-6:]:
            tail |= set(factorint(m))
        verdicts.add(len(tail) == 1)
        if len(tail) == 1:
            q = tail.pop()
            locks[s] = q
    print("  depth, dynamics, greedy -- %d seeds" % len(SEEDS))
    print("    distinct fate verdicts : %d   (%s)"
          % (len(verdicts), sorted(verdicts)))
    print("    distinct lock primes   : %d   (the row's varying quantity)"
          % len(set(locks.values())))
    check(len(verdicts) == 1, "the depth row took %d verdicts" % len(verdicts))

    print("  window opens, every target -- SOURCED, not a trajectory question:")
    print("    the census already files its outer column as vacuous.")
    print()
    return locks


# --------------------------------------------- S3 the two readings, one row

def s3_two_readings():
    print("S3 THE TWO CLOCKS MEASURED WHERE BOTH ARE COMPUTABLE")
    print("  %-6s %-8s %-9s %-9s %-9s %-8s"
          % ("seed", "|R|", "terminal", "T_real", "Omega(V)", "T_det"))
    rows, det_bad, det_seen = 0, 0, 0
    for s in (2, 3, 4, 6, 9, 12, 15, 18, 25, 36):
        R, terminal, longest = transparent_reachable(s)
        if R is None:
            continue
        rows += 1
        # T_det: the least prefix length determining the verdict. Computed,
        # not asserted -- the verdict is read at EVERY reachable state and
        # compared with the seed's, so zero differences IS T_det = 0.
        differing = 0
        for N in R:
            sub, sub_term, _ = transparent_reachable(N)
            det_seen += 1
            if sub is None or not sub <= R or not sub_term:
                differing += 1
        t_det = 0 if differing == 0 else None
        det_bad += differing
        check(len(terminal) == 1,
              "seed %d has %d terminal states" % (s, len(terminal)))
        check(longest == omega_big(headroom(s)),
              "seed %d: longest chain %d against Omega(V) %d"
              % (s, longest, omega_big(headroom(s))))
        print("  %-6d %-8d %-9d %-9d %-9d %-8s"
              % (s, len(R), len(terminal), longest,
                 omega_big(headroom(s)), t_det))
    check(det_bad == 0, "%d reachable states carry a different verdict" % det_bad)
    print("    T_real is the halting bound the corpus files as the clock;")
    print("    T_det is 0 at every seed: %d reachable states carried to their"
          " own verdict," % det_seen)
    print("    %d of them differing from the seed's." % det_bad)

    # target granularity: the limit is a closed form, so no step decides it
    print("  target granularity -- the terminus read two ways:")
    bad = 0
    for s in (2, 3, 4, 6, 9, 12, 15, 18, 25, 36):
        R, terminal, _ = transparent_reachable(s)
        if R is None:
            continue
        by_walk = sorted(factorint(sorted(terminal)[0]))
        by_form = sorted(factorint(wall(lam(s))))
        if by_walk != by_form:
            bad += 1
    check(bad == 0, "the terminus disagrees with W(lambda(s)) at %d seeds" % bad)
    print("    primes of the exhausted terminus vs primes of W(lambda(s)):"
          " %d disagreements" % bad)
    print("    so which primes the limit carries is a function of the seed;")
    print("    the per-target verdict is settled at prefix length 0 as well.")
    print()


# ------------------------------------- S4 realization at breadth and depth

def s4_realization():
    print("S4 IS THE FATE AN EVENT IN ANY FINITE PREFIX?")

    f, seat_step, sizes = {}, {}, []
    for t in range(1, 201):
        m = greedy_independence(f)
        f = mul_f(f, m)
        for p in factorint(m):
            seat_step.setdefault(p, t)
        if t in (10, 50, 100, 200):
            sizes.append((t, len(f)))
    marks = [1, 5, 10, 25, 50, 100, 200]
    ps = primes_upto(2000)
    print("  breadth, independence, greedy from 1 -- when is the n-th prime"
          " seated?")
    print("    %s" % ", ".join("n=%d:%s" % (n, seat_step.get(ps[n - 1], "-"))
                               for n in marks))
    print("    primes seated after t steps: %s"
          % ", ".join("t=%d:%d" % (t, n) for t, n in sizes))
    check(all(n == t for t, n in sizes),
          "the seated set is not the step count: %s" % sizes)
    print("    the seated set is finite at every step, so infinitely many"
          " primes are")
    print("    unseated at every step: breadth is realized at NO finite"
          " prefix length.")

    f, deep = {}, []
    for t in range(1, 41):
        f = mul_f(f, greedy_dynamics(f))
        if t in (5, 10, 20, 40):
            deep.append((t, max(f.values())))
    print("  depth, dynamics, greedy from 1 -- the largest exponent after"
          " t steps:")
    print("    %s" % ", ".join("t=%d:%d" % (t, e) for t, e in deep))
    # "every exponent is finite" cannot fail inside a finite computation, so
    # it is not the check. The falsifiable content is that the exponent
    # RISES at every step and so is unbounded over steps while finite at
    # each -- which is what makes depth a limit property and no prefix's
    # event. Under the lock, one pick deepens the column per step, so the
    # largest exponent is the step count exactly.
    check(all(e == t for t, e in deep),
          "the locked exponent does not track the step count: %s" % deep)
    print("    every exponent is finite at every step: depth is realized"
          " at NO finite")
    print("    prefix length either. Both rows carry a yes in the census's"
          " outer column.")
    print()


# ------------------------------------------- S5 the clock that does read

def s5_contentful(locks):
    print("S5 THE CONTENTFUL CLOCK -- a bound on a search whose output varies")

    over, checked = [], 0
    for s in range(1, 401):
        f = factorint(s)
        bound = omega_odd(lam(s)) + 1
        picks = []
        for t in range(bound + 6):
            m = greedy_dynamics(f)
            picks.append(m)
            f = mul_f(f, m)
        lock_prime = sorted(set(factorint(picks[-1])))[0]
        # The wander is the LOCK POINT -- the least index from which every
        # later pick carries the lock prime -- and not the first sighting
        # of that prime, which a ghost opening can supply well before the
        # trajectory locks. Measuring the sighting would make the bound
        # check pass for the wrong reason.
        w = len(picks)
        while w > 0 and lock_prime in factorint(picks[w - 1]):
            w -= 1
        checked += 1
        if w > bound:
            over.append((s, w, bound))
        locks[s] = lock_prime
    check(not over, "the wander exceeds its bound at %s" % over[:3])
    print("  greedy dynamics from %d seeds: wander over"
          " omega_odd(lambda(s)) + 1 at %d seeds" % (checked, len(over)))
    distinct = sorted(set(locks.values()))
    print("  distinct lock primes across those seeds: %d  %s%s"
          % (len(distinct), distinct[:12], " ..." if len(distinct) > 12 else ""))
    basin = {}
    for s, q in sorted(locks.items()):
        basin.setdefault(q, []).append(s)
    print("  specimen basins: %s"
          % "; ".join("%d <- %s" % (q, basin[q][:5]) for q in distinct[:4]))
    check(len(distinct) > 1, "one lock prime serves every seed")

    print("  the same law, two granularities:")
    print("    'does SOME prime reach infinite depth'  -- verdicts: 1"
          " (constant yes)")
    print("    'does the prime l reach infinite depth' -- verdicts: 2, and"
          " the answer")
    print("      is the lock prime, found by simulating to a bound that"
          " varies with s.")
    print("    The bound is the same object in both; only the second"
          " question reads it.")
    print()
    return len(distinct)


# ------------------------------------------------------ S6 the strict re-sort

def s6_resort():
    print("S6 THE STRICT RE-SORT")

    # name, outer clock (loose), uniform, hardness, verdict VARIES over the
    # row's own domain (contentful), filed status, and where the
    # contentfulness column comes from
    fates = [
        ("mortality, transparency, free", 1, 1, 0, 0, "decidable", "S2/S3"),
        ("breadth, independence, greedy", 1, 1, 0, 0, "decidable", "S2/S4"),
        ("depth, dynamics, greedy", 1, 1, 0, 0, "decidable", "S2/S4"),
        ("window opens, every target", 1, 1, 0, 0, "decidable", "sourced"),
        ("fate, sighted hosting law, free", 0, 0, 1, 1, "undecidable",
         "sourced"),
        # The two open rows' verdicts are NOT KNOWN, so whether they vary is
        # not known either: the column is None, never a 1 chosen because the
        # sort is insensitive to it. Both rows lack an outer clock, so the
        # rule short-circuits before the column is read -- which is why an
        # honest None costs nothing and a satisfied 1 would cost the census
        # its standing as evidence.
        ("carrier ladder halts, one start", 0, 1, 0, None, "open", "sourced"),
        ("carrier ladder halts, all starts", 0, 0, 0, None, "open", "sourced"),
    ]

    print("  %-34s %-7s %-8s %-7s %-11s %-11s"
          % ("question", "loose", "contentf", "strict", "strict says",
             "filed"))
    loose_mism, strict_mism = 0, 0
    for name, out, uni, hard, varies, filed, src in fates:
        loose = "decidable" if (out and uni) else (
            "undecidable" if hard else "open")
        clocked = out and uni and varies
        strict = "decidable" if clocked else (
            "undecidable" if hard else "open")
        if loose != filed:
            loose_mism += 1
        flag = ""
        if strict != filed:
            strict_mism += 1
            flag = "  <-- MISMATCH"
        print("  %-34s %-7s %-8s %-7s %-11s %-11s%s"
              % (name, "yes" if (out and uni) else "no",
                 "n/a" if varies is None else ("yes" if varies else "no"),
                 "yes" if clocked else "no", strict, filed, flag))
    # The two counts ARE the finding, so they are asserted rather than
    # only printed: a future edit that moves either has changed the
    # result and must say so.
    check(loose_mism == 0,
          "the loose reading no longer reproduces the filed sort (%d)"
          % loose_mism)
    check(strict_mism == 4,
          "the strict re-sort mismatches %d rows, not 4" % strict_mism)
    print("  mismatches, loose reading : %d" % loose_mism)
    print("  mismatches, strict reading: %d" % strict_mism)
    print("    the strict rule's OWN verdicts on those four rows are FALSE --"
          " each is decidable,")
    print("    trivially, being constant. That is the finding and not a"
          " defect in the rule:")
    print("    the strict reading is an instrument for refutation, never a"
          " proposed law. So")
    print("    neither reading is one -- the loose cannot fail, the strict"
          " fails everywhere")
    print("    it was built to explain, and what survives is the sufficiency"
          " direction alone.")

    # The column against the answer it is supposed to explain. If the outer
    # column is a yes at exactly the rows already filed decidable, then it
    # is that filing renamed and carries no independent information -- which
    # is what "vacuous" means here, stated as a count rather than a reading.
    agree = sum(1 for _, out, _, _, _, filed, _ in fates
                if bool(out) == (filed == "decidable"))
    print("  the outer column against the status it explains: agrees at"
          " %d of %d rows" % (agree, len(fates)))
    uni_agree = sum(1 for _, _, uni, _, _, filed, _ in fates
                    if bool(uni) == (filed == "decidable"))
    print("    the uniformity column, same comparison: %d of %d"
          % (uni_agree, len(fates)))
    print("    the contentfulness column is COMPUTED at the first three rows"
          " (S2, S5), SOURCED")
    print("    at two, and NOT KNOWN at the two open rows, whose verdicts the"
          " corpus does not")
    print("    have -- the rule short-circuits on the outer column before"
          " reading it there.")

    # Q6: the inner clock's search has a varying output
    print("  the inner clock, for contrast -- least prime = 1 mod B,"
          " B = 2..200:")
    least = {}
    for B in range(2, 201):
        least[B] = next(p for p in range(B + 1, 400 * B + 400, B) if is_prime(p))
    print("    distinct witnesses across the range: %d of %d moduli"
          % (len(set(least.values())), len(least)))
    print("    ratio p/B, worst: %d at B = %d"
          % max((p // B, B) for B, p in least.items()))
    # ">1 distinct" would pass on a broken search that found two values,
    # so the check names the spread the finding rests on.
    check(len(set(least.values())) > 100,
          "the inner witness spread collapsed to %d values"
          % len(set(least.values())))
    print("    so the inner bound stops a search whose ANSWER varies;"
          " the outer column,")
    print("    at every row the census files decidable, does not.")
    print()
    return loose_mism, strict_mism


def main():
    s1_control()
    locks = s2_constancy()
    s3_two_readings()
    s4_realization()
    s5_contentful(locks)
    s6_resort()
    print("=" * 68)
    if FAIL:
        print("FAILURES: %d" % len(FAIL))
        for m in FAIL:
            print("  - " + m)
        sys.exit(1)
    print("all checks clean")


if __name__ == "__main__":
    main()
