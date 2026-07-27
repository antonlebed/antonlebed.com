"""
explore_fate_image.py -- THE FATE IMAGE OF A DEMAND LAW (sibling of
explore_fate_clock.py, explore_growth_laws.py, explore_demand_reading.py,
explore_lock_prime.py, explore_headroom.py, explore_slack_machine.py).

THE QUESTION. A state of the growing tower is a positive integer N; a move
multiplies it, N -> N*m with m >= 2; a DEMAND LAW says which moves may be
made; a POLICY picks one of the admissible moves; and a maximal trajectory
has a LIMIT, a supernatural number. Three fates are filed
(explore_growth_laws.py): BREADTH, every prime seated; DEPTH, some prime at
infinite depth; MORTALITY, a finite integer. They are three PROPERTIES and
not a partition, and a companion file (explore_fate_clock.py) showed that
under the independence law a FREE policy can land outside all three -- a
policy avoiding one prime seats every other and holds none of the fates.

That leaves the trichotomy classifying nothing in particular: not the world,
since a free policy escapes it, and not the greedy runs alone, since
mortality holds under every policy. This file asks what it IS a slice of.
The object proposed for the job is the FATE IMAGE:

    Im(L, s) = { the limit of a maximal L-run from s, over all policies }

-- the set of supernatural numbers a demand law can reach from a seed when
nothing but the law constrains the choice. The three fates are then
predicates ON that set, and the question "which fates does L hold" becomes
"where do the extremes of Im(L, s) sit".

THE SECOND QUESTION, which is why five laws are run and not one. A filed
square (explore_demand_reading.py) sorts the same demand laws on two
independent axes: READING -- can the law's one-bit probe see a decrement,
which the support-blind laws provably cannot and the lambda-reading ones
answer as a side effect of what they mean by admissible; and HOSTING --
whether the law admits the moves a counter machine needs, increment and
decrement both. That square was built to decide UNIVERSALITY. The question
here is whether it also decides the IMAGE, and it is a real question rather
than a restatement, because nothing connects a law's probe repertoire to the
shape of its reachable limits.

VOCABULARY FLAG, fixed at the freeze. The predictions below are written in
the FATES' vocabulary -- supports, exponents, limits -- and NOT in the
machine's -- counters, slack, probes. The crossing between the two is the
finding under test, so importing the machine's terms into the derivation
would make the answer true by translation. The square is consulted only in
the last section, after every image has been derived on its own terms.

TRANSPLANT FLAG. The construction used for the dynamics law below -- pad a
move with a fresh prime q chosen so that lambda must rise -- is imported
from explore_slack_machine.py, where it was built for a different job
(buying law-autonomy for a decrement). The condition it needs here is
re-derived rather than inherited, and the rig checks lambda at every step.

THE OBJECTS. lambda is Carmichael's function. omega counts distinct prime
factors, Omega counts them with multiplicity. W(L) is the largest modulus
whose lambda divides L. V(N) = W(lambda(N))/N is the transparency headroom.
A supernatural number is written by its exponent function p -> e_p in
{0, 1, 2, ...} u {oo}; it is FINITE iff its support is finite and every
exponent is finite. supp(X) is the set of primes with e_p > 0.

THE FIVE DEMAND LAWS, each with its full free policy class:
  INDEPENDENCE    -- m admissible iff gcd(m, N) = 1 (the extension splits).
  SEMISIMPLICITY  -- m admissible iff N*m is squarefree.
  NEW-IDEMPOTENTS -- m admissible iff Z/(N*m) has more idempotents than
                     Z/N, i.e. iff omega(N*m) > omega(N).
  TRANSPARENCY    -- m admissible iff lambda(N*m) = lambda(N), i.e. m | V(N).
  DYNAMICS        -- m admissible iff lambda(N*m) > lambda(N).

THE PREDICTIONS, fixed before any engine code was written. Each names what
the rig PRINTS; what it means is weighed afterwards. Each image claim has
two halves and they are checked by different means -- the CLOSURE half
(nothing outside) by a mechanical invariant over a state x move battery, the
REACH half (everything inside) by running the construction and checking
admissibility and divisibility at every step. A prefix is not a limit, so
the reach half is always a construction plus an argument that it never
stalls, with the rig checking the argument's hypothesis rather than its
conclusion.

Q1 TRANSPARENCY. Im = { W(lambda(s)) }: a single point, and a finite one.
   (Filed already; carried here as the control that the image machinery
   reproduces a known image.)
   KILL: a maximal transparent run ending anywhere else.

Q2 INDEPENDENCE. Im = { s * prod_{p in S} p^{e_p} : S an INFINITE set of
   primes disjoint from supp(s), each e_p finite and >= 1 }. Three clauses,
   each with its own mechanism: the seed's own exponents are FROZEN (a move
   coprime to N cannot carry a prime of N), every exponent is FINITE (a
   prime is seated by exactly one move and never touched again), and the
   support is INFINITE (every move seats at least one new prime, and no run
   halts).
   KILL: a reachable limit violating any clause, or a member of the set that
   the construction cannot reach.

Q3 SEMISIMPLICITY, run because it shares a square cell with independence and
   is the test of whether the cell determines the image. From a SQUAREFREE
   seed, Im = { s * prod_{p in S} p : S infinite, disjoint from supp(s) } --
   the same support freedom, every exponent pinned to 1. From a
   NON-SQUAREFREE seed nothing is admissible at all and Im = { s }.
   PREDICTION: the two images differ from independence's, so the square cell
   does NOT determine the image.
   KILL: the two images coincide.

Q4 NEW-IDEMPOTENTS. Im = { X : s | X, supp(X) infinite } -- support still
   forced infinite, but every exponent free, oo included, on seed primes as
   well. The demand asks only that a move carry SOME new prime, so a move
   may raise seated exponents alongside.
   KILL: a reachable limit of finite support, or an unreachable member.

Q5 DYNAMICS. Im = { X : s | X, X infinite } -- everything an infinite
   supernatural multiple of the seed, the MAXIMAL image any live law can
   have. Two constructions are needed: for a target of infinite support,
   pad each move with a support prime q > lambda(N) + 1, which forces
   lambda to rise because (q-1) cannot divide a smaller number; for a target
   of finite support with an infinite exponent, push that prime deep enough
   that its own contribution to lambda passes the current value.
   KILL: an infinite multiple of the seed at which the construction stalls,
   or a maximal run reaching a finite limit.

Q6 THE TWO COORDINATES AGAINST THE SQUARE. Read two bits off each image --
   DEPTH-AVAILABLE (some member has an infinite exponent) and
   FINITE-SUPPORT-AVAILABLE (some member has finite support) -- and compare
   with the law's filed square position. Prediction: HOSTING decides the
   first and READING decides the second, at all five laws.
   KILL: any mismatch, over the five laws.

Q7 THE DEAD CELL. A run whose limit has finite support and no infinite
   exponent is a run with a finite limit, and a state that only ever
   multiplies by 2 or more cannot take infinitely many moves inside a finite
   limit -- so such a run HALTS. Predict that the square cell (sighted,
   hosts nothing) is therefore forced mortal, and that this is why the
   mortality law sits exactly there.
   KILL: a live law in that cell, i.e. a law that reads lambda, hosts no
   unbounded depth, and still runs forever.

THE DESIGN, in five sections after the control.

S1 POSITIVE CONTROL, run before any image verdict is read; the run aborts if
   it fails. Six things this file leans on but did not derive here must come
   back: lambda against its brute-force definition (the maximum order in the
   unit group); W against ITS definition by search, compared only below the
   search cap; the two INDEX CONVENTIONS the hand-derivations dereference --
   v_p(lambda(p^c)) = c-1 for odd p and v_2(lambda(2^c)) = c-2 for c >= 3,
   both re-read off the engine rather than trusted, since an off-by-one here
   would corrupt the dynamics construction for a deep target; and the filed
   greedy facts this file contrasts free policies against -- independence
   greedy grows the primorial, dynamics greedy locks one prime's column,
   transparency greedy halts at the wall.

   STATES ARE CARRIED AS FACTORISATIONS everywhere a trajectory is walked: a
   state outgrows any factoring budget within a few steps, so the engine
   multiplies exponent dictionaries and reads lambda off them. Trial
   division is applied only to the small move m.

S2 THE ADMISSIBILITY ATLAS -- the mechanical basis of the two coordinates,
   measured before either is claimed. Over a battery of states and every
   move up to a cap, classify each admissible move by two bits: does it SEAT
   a prime the state did not have, and does it RAISE the exponent of one it
   already had. The counts are the closure half of Q2-Q5 in raw form, and
   they are engine consistency where the demand makes them tautological --
   that is stated in the print rather than left for the reader.

S3 THE REACH HALF -- run the construction for each law against a battery of
   targets, in-image and out. For an in-image target: every move must be
   admissible under the law, the state must divide the target at every step
   (a construction that overshoots has reached something else), and the
   target's data must be exhausted on a schedule the rig prints -- how many
   support primes seated, how many exponents already final. For an
   out-of-image target: print the mechanical reason no policy reaches it,
   verified by an exhaustive scan over moves rather than asserted.

S4 THE CLOSURE HALF -- for each law the invariant that bounds its image,
   checked over a state x move battery: the frozen-seed and
   frozen-once-seated invariants (independence), squarefreeness
   (semisimplicity), seats-a-new-prime (new-idempotents), never-empty
   (the three live laws, so no finite limit), and the finite reachable set
   (transparency, by exhaustion from several seeds).

S5 THE SQUARE TABLE -- the five laws, their filed square position, the two
   coordinates as S2-S4 measured them, liveness, and the mismatch count as
   the observable Q6 named; then the dead-cell derivation of Q7 exhibited on
   the one law that occupies the cell.

THE FINDINGS.

F1 THE FIVE IMAGES ARE FIVE SHAPES, and they form a CHAIN under inclusion
   (rule; closure halves exhaustive over the battery, reach halves
   constructed and argued). Writing s for the seed and P for the primes:

     transparency     { W(lambda(s)) }                    one finite point
     semisimplicity   s * prod_{p in S} p                 SQUAREFREE s only;
                                                          S infinite, S disjoint
                                                          from supp(s). From a
                                                          non-squarefree seed
                                                          nothing is admissible
                                                          and the image is { s }
     independence     s * prod_{p in S} p^{e_p}           S infinite and
                                                          disjoint, 1 <= e_p < oo
     new-idempotents  every X with s | X, supp(X) infinite
     dynamics         every X with s | X, X infinite      MAXIMAL

   The last four nest strictly, semisimplicity to dynamics, and the
   transparency point sits outside the chain because it is the only finite
   one. (SCOPE, made explicit by explore_fate_image_ff.py S6: the nesting
   is a SQUAREFREE-SEED statement. The table's own second row says the
   image from any other seed is the finite point { s }, and no
   infinite-support image contains one -- so at a non-squarefree seed
   semisimplicity leaves the chain by transparency's door instead of
   sitting at its bottom, and only three nest.) The dynamics image is everything a live law could possibly have --
   no run halts, so no limit is finite, and that exhausts the constraint;
   its closure half is vacuous, the only one here that is.

F2 THE SQUARE DECIDES TWO COORDINATES OF THE IMAGE AND NOT THE IMAGE
   (observation over five laws, mechanism named in each; 0 mismatches).
   Read two bits off an image -- is an infinite EXPONENT reachable, is a
   FINITE SUPPORT reachable -- and they are exactly the square's two axes:
   HOSTING decides the first, by TWO different mechanisms and not one: a law
   hosting no DECREMENT never revisits a prime, so nothing is ever deepened
   (independence, semisimplicity), while the law hosting no INCREMENT revisits
   primes constantly -- 26 of its 44 admissible moves over the battery raise a
   seated exponent -- and gets no depth from a finite reachable set instead
   (transparency). The column is right at all four and the crisp one-clause
   reading of it is wrong at one of them.
   READING decides the second (each
   filed blind demand can only be MET by new support, so a run under one
   cannot stop widening). Both coordinates are read off S3/S4 witnesses
   rather than off the square.
   THE AXIS IS NOT A THEOREM ABOUT BLINDNESS, and the attack that shows it
   costs one law: NON-semisimplicity -- m admissible iff N*m is NOT
   squarefree -- is support-blind by the same test the filed square uses,
   and 58 of 552 admissible moves over the battery seat nothing, so its
   image holds finite-support members the reading axis forbids. What the
   three filed blind demands share is stronger than blindness: coprimality,
   squarefreeness and a raised omega can each only be MET by new support.
   The correspondence is over the five FILED laws, and this is its boundary,
   found by attacking the axis rather than by assuming it.
   What the square does NOT decide is the image:
   independence and semisimplicity share the (blind, hosts nothing) cell and
   have different images -- same two coordinates, exponents free against
   exponents pinned to 1, verified by semisimplicity stalling at step 1 on a
   target wanting exponent 2. So the square is a coordinate map, not a
   classification, and the negative half is what keeps it honest.

F3 MORTALITY IS THE BOTTOM CORNER OF THE IMAGE, AND THE SQUARE DOES NOT
   REACH IT (rule for the corner; the cell reading was DERIVED AND THEN
   REFUTED here, and the refutation is the finding). The corner half is two
   lines and holds: a limit of finite support with no infinite exponent IS a
   finite integer, every move multiplies by at least 2, so a run with that
   limit halts -- mortality is the corner where both coordinates bottom out,
   and a law is mortal exactly when its image holds that corner.
   The cell half does not. It read "the cell (sighted, hosts nothing) buys
   finite support from its reading and forbids depth by its hosting, so it
   cannot hold a live law", and the quantifier is wrong in the first clause:
   sighted makes finite support AVAILABLE, not compulsory, so a law there may
   have infinite-support members and live forever. FRESH-DYNAMICS -- m
   admissible iff m is a prime not dividing N and lambda(N*m) > lambda(N) --
   reads lambda, never revisits a prime, and runs forever seating 20 primes
   at exponent 1: a live law in the supposedly dead cell. Transparency is
   mortal for a reason the square never carried, its FINITE reachable set,
   which is the headroom fact. So mortality is not a square coordinate, and
   the square's reach is exactly the two coordinates F2 names. The kill-shape
   Q7 froze is what fired, verbatim and on the first law built to meet it,
   which is the whole reason the prediction was written as an observable.
   Liveness is not a property of the law either: semisimplicity dies from
   seed 12 and lives from 1, so it belongs to the (law, seed) PAIR.

F4 THE THREE FATES ARE THE EXTREMES OF THE IMAGE, which is what the
   trichotomy is a slice of (synthesis). The image factors into a SUPPORT
   choice and an EXPONENT choice; breadth is the support maximal, depth is
   an exponent maximal, mortality is both minimal. (SHARPENED by
   explore_fate_image_ff.py: only mortality pins BOTH coordinates, so it
   alone is a corner -- breadth and depth are FACES, each extremal in one
   coordinate with the other free, which is what lets two trajectories both
   hold depth and still differ.) The two coordinates are
   SEPARATELY free, so breadth and depth co-occur over Z: 2^oo times every
   odd prime is reached under both hosting-both laws, and the filed reading
   that fate purity is ARCHIMEDEAN -- that the co-occurring class is one Z's
   trajectories never produce -- is corrected here to purity being GREED'S.
   Purity survives the ring: off Z the greedy dynamics limit still holds the
   lone depth fate, from an infinite support of density zero, so what the
   melt moves is WHERE in this body greed sits and not which fate it holds
   (explore_fate_image_ff.py, which redraws all five images over F_2[x] and
   finds the same shapes, the same chain and the same extremes). One corner
   and two faces of a two-coordinate body, and the generic member is interior and holds none of
   the three -- so the filed "a free policy can hold none of the fates" is
   not an anomaly of one avoiding policy but the ordinary condition, and the
   avoiding policy is simply an interior point named. Breadth in particular
   is ONE value of the support coordinate out of a continuum of infinite
   support sets, and independence greedy lands on it while taking the
   exponent lattice's bottom: the primorial limit is the corner where both
   coordinates are extreme in opposite directions.

F5 A FREE DYNAMICS POLICY REACHES THE 2-COLUMN FROM THE VOID (rule,
   constructed), where greedy dynamics locks the 3-column instead and never
   opens the 2-window at all (S1 reproduces the lock, 10 picks, every one
   a 3; the filed cold-door floor 16 is what makes 2 unaffordable). The
   construction is the whole of it: pushing 2 alone leaves lambda at 1, and
   pushing 4 raises it, so 2^oo is reached by a policy that simply refuses
   the least move. The 2-window's dynamic invisibility is GREED'S, not the
   law's -- an instance of the general point that a fate is chosen by the
   policy at fixed demand, now with the cheapest possible witness.

F6 THE TRANSPLANT FLAG PAID, and the same import failed the same way twice.
   The dynamics construction was first written with the padding condition
   q > lambda(N) + 1; the rig stalled at 3 of 4 targets, because that
   condition forces lcm(lambda, q-1) as high as lambda^2 and the witness
   search outruns any prime cap within seven steps. The operative condition
   is the weaker (q-1) does not divide lambda(N) -- sufficient for the rise,
   affordable, and the stronger one is retained only as the EXISTENCE
   argument, since (q-1) | lambda(N) forces q <= lambda(N) + 1 and so all
   but finitely many primes qualify. A neighbouring file recorded exactly
   this correction for exactly this device; importing the device without
   its correction is what the flag is for, and the flag caught it at the
   rig rather than in the prose.

ADDED AFTER THE FREEZE, recorded rather than folded into the design above,
which stands as written. Three checks the slate did not name: the
never-stalls hypothesis made observable (the least unseated support prime
must strictly rise across every in-image run, so a construction that
silently skipped a prime forever would fail rather than print a clean
prefix of the wrong limit); a coverage requirement on the coordinate table
(a law with neither a positive witness nor a closure reason FAILS instead
of printing "no"); and two seeded finite-support targets, since the
finite-support branch of the dynamics construction was otherwise exercised
only from the void. None of them changed a verdict; each closes a way the
rig could have printed a clean run for the wrong reason.

SCOPE, fixed here rather than after the fact. The images are claims about
LIMITS and the rig walks PREFIXES: every reach verdict is a finite
construction plus a stated argument that it continues, and the argument's
hypothesis -- a suitable prime exists at every step -- is what the rig
checks, within a bounded search that is an efficiency and not the argument.
The closure verdicts are exhaustive over the battery's move range only; the
general reason is one line in each case and is printed with the count, so a
range is never doing the work of a proof. Primality is deterministic
Miller-Rabin over the range this file uses.

THE NEIGHBOURS, named so nothing here reads as newer than it is. The image
of a nondeterministic rewriting system -- the set of limits its runs can
reach -- is the standard reachability-set object, and the supernatural
numbers and their divisibility order are classical. The construction that
pads a move to force a lambda rise is imported, with the correction its own
file records. What is not inherited is the pairing: an image read as a
two-coordinate body, the three filed fates recovered as its corners, and
the coordinates matched to a square that was built to decide universality.

RUN RECORD. Pure Python, no third-party imports; single process, 0.2 s wall
clock, well under the memory ceiling. All checks clean.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import gcd, inf

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("  FAIL: " + msg)
    return cond


def section(t):
    print("\n" + "=" * 68)
    print(t)
    print("=" * 68)


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


def lcm(a, b):
    return a // gcd(a, b) * b


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


def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
        i += 1
    return [i for i in range(n + 1) if sieve[i]]


PRIMES = primes_upto(200000)


def lam(n):
    """Carmichael's lambda of an integer."""
    if n == 1:
        return 1
    out = 1
    for p, e in factorint(n).items():
        out = lcm(out, _lam_pp(p, e))
    return out


def _lam_pp(p, e):
    if p == 2:
        return 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
    return p ** (e - 1) * (p - 1)


def lam_f(f):
    """Carmichael's lambda read off an exponent dictionary."""
    out = 1
    for p, e in f.items():
        if e:
            out = lcm(out, _lam_pp(p, e))
    return out


def mul_f(f, m):
    """The state after a move, as an exponent dictionary."""
    g = dict(f)
    for p, e in factorint(m).items():
        g[p] = g.get(p, 0) + e
    return g


def int_f(f):
    n = 1
    for p, e in f.items():
        n *= p ** e
    return n


def omega_f(f):
    return sum(1 for e in f.values() if e)


_WCACHE = {}


def wall(L):
    """W(L) -- the largest modulus whose lambda divides L."""
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


# ------------------------------------------------------------- the five laws
#
# Every law is a predicate on (state as an exponent dictionary, move m >= 2).

def adm_independence(f, m):
    return m >= 2 and all(not f.get(p) for p in factorint(m))


def adm_semisimplicity(f, m):
    if m < 2:
        return False
    g = mul_f(f, m)
    return all(e <= 1 for e in g.values())


def adm_newidem(f, m):
    return m >= 2 and omega_f(mul_f(f, m)) > omega_f(f)


def adm_transparency(f, m):
    return m >= 2 and lam_f(mul_f(f, m)) == lam_f(f)


def adm_dynamics(f, m):
    return m >= 2 and lam_f(mul_f(f, m)) > lam_f(f)


# name -> (predicate, reading, hosting) with the square position FILED, not
# derived here (explore_demand_reading.py owns it).
LAWS = [
    ("independence", adm_independence, "blind", "hosts nothing"),
    ("semisimplicity", adm_semisimplicity, "blind", "hosts nothing"),
    ("new-idempotents", adm_newidem, "blind", "hosts both"),
    ("transparency", adm_transparency, "sighted", "hosts nothing"),
    ("dynamics", adm_dynamics, "sighted", "hosts both"),
]


# ------------------------------------------------------------------ targets
#
# A supernatural number, given by its exponent function and its support.

class Sup(object):
    def __init__(self, name, expfn, finite_support=None):
        self.name = name
        self._e = expfn
        self.finite_support = finite_support   # None means infinite support

    def e(self, p):
        return self._e(p)

    def support_upto(self, B):
        if self.finite_support is not None:
            return [p for p in self.finite_support if p <= B]
        return [p for p in PRIMES if p <= B and self.e(p)]

    def divides_state(self, f):
        """Is the state a divisor of this supernatural number?"""
        return all(e <= self.e(p) for p, e in f.items() if e)


INF = inf


def sup_from_dict(name, d, extra=None):
    """Finite-support supernatural number from a {prime: exponent} dict."""
    return Sup(name, lambda p: d.get(p, 0), sorted(d))


# ---------------------------------------------------------------- S1 control

def s1_control():
    section("S1  POSITIVE CONTROL (run before any image verdict is read)")

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

    CAP = 20000
    biggest = {}
    for n in range(1, CAP + 1):
        L = lam(n)
        if L <= 24:
            biggest[L] = max(biggest.get(L, 0), n)
    tested, bad = 0, []
    for L, seen in sorted(biggest.items()):
        w = wall(L)
        if w > CAP:
            continue
        tested += 1
        if w != seen:
            bad.append((L, w, seen))
    check(not bad, "W formula disagrees with brute search: %s" % bad[:3])
    print("  W(L) = largest modulus with lambda | L: %d values of L checked "
          "under the search cap, %d failures" % (tested, len(bad)))

    # the two index conventions the hand-derivations dereference, re-read off
    # the engine: an off-by-one here corrupts the deep-target construction.
    bad = []
    for p in (3, 5, 7, 11):
        for c in range(1, 9):
            if v_p(lam(p ** c), p) != c - 1:
                bad.append((p, c))
    check(not bad, "v_p(lambda(p^c)) != c-1 at %s" % bad[:3])
    bad2 = [c for c in range(3, 14) if v_p(lam(2 ** c), 2) != c - 2]
    check(not bad2, "v_2(lambda(2^c)) != c-2 at %s" % bad2[:3])
    print("  index conventions off the engine: v_p(lambda(p^c)) = c-1 "
          "(odd p, c <= 8), v_2(lambda(2^c)) = c-2 (c = 3..13)")

    # filed greedy facts, reproduced
    f, picks = {}, []
    for _ in range(8):
        m = 2
        while not adm_independence(f, m):
            m += 1
        picks.append(m)
        f = mul_f(f, m)
    check(picks == [2, 3, 5, 7, 11, 13, 17, 19],
          "independence greedy is not the primorial: %s" % picks)
    print("  independence greedy from the void: %s" % picks)

    f, picks = {}, []
    for _ in range(10):
        m = 2
        while not adm_dynamics(f, m):
            m += 1
        picks.append(m)
        f = mul_f(f, m)
    check(set(picks[1:]) == {3},
          "dynamics greedy does not lock the 3-column: %s" % picks)
    print("  dynamics greedy from the void:      %s  (locks one column)" % picks)

    for s in (2, 6, 30):
        N = s
        while True:
            V = headroom(N)
            step = min([d for d in divisors(V) if d >= 2], default=None)
            if step is None:
                break
            N *= step
        check(N == wall(lam(s)),
              "transparency greedy from %d halts at %d, not W = %d"
              % (s, N, wall(lam(s))))
    print("  transparency greedy halts at W(lambda(s)) from seeds 2, 6, 30")


# ------------------------------------------------------- S2 the atlas

def s2_atlas():
    section("S2  THE ADMISSIBILITY ATLAS -- what an admissible move DOES")
    print("  Over a battery of states, every move 2..%d classified by two "
          "bits:" % ATLAS_MOVE_CAP)
    print("  SEATS a prime the state lacked / RAISES one it already had, plus")
    print("  the SEATLESS count (admissible and seating nothing) that the")
    print("  finite-support coordinate reads.\n")

    states = [{}, {2: 1}, {2: 2}, {3: 1}, {2: 1, 3: 1}, {2: 1, 3: 1, 5: 1},
              {2: 2, 3: 1}, {5: 1}, {2: 3, 5: 2}, {2: 1, 3: 1, 5: 1, 7: 1}]
    # NOT a "neither" column: every m >= 2 has a prime factor, seated or not,
    # so seats-or-raises always holds and a "neither" count could only ever
    # print 0. The informative column is SEATLESS = adm - seats, which is the
    # one the finite-support coordinate reads.
    print("  %-16s %8s %8s %8s %9s" %
          ("law", "adm", "seats", "raises", "seatless"))
    out = {}
    for name, adm, _r, _h in LAWS:
        tot = seats = raises = 0
        for f in states:
            for m in range(2, ATLAS_MOVE_CAP + 1):
                if not adm(f, m):
                    continue
                tot += 1
                fm = factorint(m)
                seats += any(not f.get(p) for p in fm)
                raises += any(f.get(p) for p in fm)
        out[name] = (tot, seats, raises, tot - seats)
        print("  %-16s %8d %8d %8d %9d" % (name, tot, seats, raises, tot - seats))

    check(out["independence"][2] == 0, "an independence move raised a seated prime")
    check(out["semisimplicity"][2] == 0, "a semisimplicity move raised a seated prime")
    check(out["new-idempotents"][1] == out["new-idempotents"][0],
          "a new-idempotents move seated nothing")
    for nm in ("transparency", "dynamics"):
        check(out[nm][2] > 0, "%s never raises a seated prime" % nm)
        check(out[nm][0] - out[nm][1] > 0,
              "%s has no admissible move that seats nothing" % nm)
    print("\n  The three blind ROWS print structural zeros -- two in RAISES,")
    print("  one in SEATLESS -- and each is a TAUTOLOGY given its demand, so")
    print("  they are engine consistency and not evidence: a coprime move")
    print("  cannot carry a seated prime, a squarefree state admits no second")
    print("  copy, and a move raising omega must carry an unseated prime.")
    print("  What is measured is the sighted rows -- both")
    print("  admit moves that seat NOTHING, which is what lets a run stop")
    print("  widening its support.")
    return out


ATLAS_MOVE_CAP = 400


# ------------------------------------------------ S3 the reach half

def build_independence(target, f, step, seed):
    """Seat the next unseated support prime at its final exponent."""
    for p in target.support_upto(REACH_PRIME_CAP):
        if not f.get(p):
            e = target.e(p)
            if e is INF:
                return None
            return p ** e
    return None


def build_semisimplicity(target, f, step, seed):
    for p in target.support_upto(REACH_PRIME_CAP):
        if not f.get(p):
            return p if target.e(p) == 1 else None
    return None


def build_newidem(target, f, step, seed):
    """One fresh prime (capped) plus progress on everything already seated."""
    m = 1
    fresh = None
    for p in target.support_upto(REACH_PRIME_CAP):
        if not f.get(p):
            fresh = p
            break
    if fresh is None:
        return None
    e = target.e(fresh)
    m *= fresh ** (step if e is INF else min(e, step))
    for p, have in sorted(f.items()):
        if not have:
            continue
        want = target.e(p)
        cap = step if want is INF else want
        if have < cap:
            m *= p ** (min(cap, have + 1) - have)
    return m


def build_dynamics(target, f, step, seed):
    """Seat the next support prime, PADDED with a witness q for which (q-1)
    does not divide lambda(N) -- the condition the algebra names. The
    stronger q > lambda(N) + 1 is sufficient and unaffordable: it forces
    lcm(lambda, q-1) as high as lambda^2, so lambda squares every step. It
    is what guarantees a witness EXISTS -- (q-1) | lambda(N) forces
    q <= lambda(N) + 1, so all but finitely many primes qualify -- and the
    search below is an efficiency, not the argument."""
    L = lam_f(f)
    m = 1
    for p, have in sorted(f.items()):          # progress on seated primes
        if not have:
            continue
        want = target.e(p)
        cap = step if want is INF else want
        if have < cap:
            m *= p ** (min(cap, have + 1) - have)

    unseated = [p for p in target.support_upto(REACH_PRIME_CAP)
                if not f.get(p)]
    if unseated:
        def cap_e(p):
            e = target.e(p)
            return step if e is INF else e
        p0 = unseated[0]
        m *= p0 ** cap_e(p0)
        if lam_f(mul_f(f, m)) > L:
            return m
        # (q-1) does not divide L. p0 is excluded on purpose: if p0 qualified
        # it would already have moved lambda above (its push carries p0-1), so
        # it cannot be both a non-riser and a witness -- excluding it makes
        # that argument structural instead of leaving a double push possible.
        wit = [q for q in unseated if q != p0 and L % (q - 1)]
        if wit:
            return m * wit[0] ** cap_e(wit[0])
        # no witness among the unseated: the support left is finite and small,
        # so fall through and buy the rise from an infinite column instead.

    # the target's support is finite (or exhausted): drive one of its
    # infinite columns deep enough that its own lambda-part passes L.
    col = [p for p in target.support_upto(REACH_PRIME_CAP)
           if target.e(p) is INF]
    if not col:
        return None
    p = min(col)
    k = 1
    while lam_f(mul_f(f, m * p ** k)) <= L:
        k += 1
        if k > 64:
            return None
    return m * p ** k


BUILDERS = {
    "independence": build_independence,
    "semisimplicity": build_semisimplicity,
    "new-idempotents": build_newidem,
    "dynamics": build_dynamics,
}

REACH_PRIME_CAP = 4000
REACH_STEPS = 14


def reach(lawname, seed, target, steps=REACH_STEPS):
    """Run the law's construction at a target; return a report dict."""
    adm = dict((n, a) for n, a, _r, _h in LAWS)[lawname]
    build = BUILDERS[lawname]
    f = dict(seed)
    lams = [lam_f(f)]
    stalled_at = None
    bad_adm = bad_div = 0
    # THE NEVER-STALLS HYPOTHESIS, made observable: the least UNSEATED
    # support prime must strictly rise across the run. The construction is
    # allowed to jump ahead (the dynamics witness does), but if the frontier
    # ever froze, some prime would be skipped forever and the limit would not
    # be the target -- a prefix that looks clean while reaching something else.
    frontier = []
    for step in range(1, steps + 1):
        un = [p for p in target.support_upto(REACH_PRIME_CAP) if not f.get(p)]
        frontier.append(un[0] if un else None)
        m = build(target, f, step, seed)
        if m is None:
            stalled_at = step
            break
        if not adm(f, m):
            bad_adm += 1
        g = mul_f(f, m)
        if not target.divides_state(g):
            bad_div += 1
        f = g
        lams.append(lam_f(f))
    seated = sum(1 for p, e in f.items() if e and not seed.get(p))
    final = sum(1 for p, e in f.items()
                if e and target.e(p) is not INF and e == target.e(p))
    return {
        "stalled_at": stalled_at, "bad_adm": bad_adm, "bad_div": bad_div,
        "seated": seated, "final": final, "state": f,
        "lam_rises": all(b > a for a, b in zip(lams, lams[1:])),
        "frontier": frontier, "digits": len(str(int_f(f))),
    }


def frontier_ok(r):
    """The least unseated support prime never stalls. None means the support
    is exhausted, which only a finite-support target reaches and which is
    progress, not a stall."""
    fr = [p for p in r["frontier"] if p is not None]
    return all(b > a for a, b in zip(fr, fr[1:]))


def s3_reach(wit):
    section("S3  THE REACH HALF -- constructions against a target battery")

    allp = Sup("every prime, exponent 1", lambda p: 1)
    mod4 = Sup("primes = 1 mod 4, exponent (p mod 3) + 1",
               lambda p: (p % 3) + 1 if p % 4 == 1 else 0)
    ladder = Sup("every prime, exponent = its index",
                 lambda p: PRIMES.index(p) + 1 if p in _PSET else 0)
    two_inf = sup_from_dict("2^oo alone", {2: INF})
    three_inf = sup_from_dict("3^oo alone", {3: INF})
    both = Sup("2^oo times every odd prime",
               lambda p: INF if p == 2 else 1)

    print("\n  (a) INDEPENDENCE from the void -- in-image targets")
    for t in (allp, mod4):
        r = reach("independence", {}, t)
        ok = (r["stalled_at"] is None and not r["bad_adm"]
              and not r["bad_div"] and frontier_ok(r))
        check(ok, "independence stalled or misstepped at %s: %s" % (t.name, r))
        print("      %-44s seated %2d, all exponents final %2d, %d steps clean"
              % (t.name, r["seated"], r["final"], REACH_STEPS))

    print("\n  (b) NEW-IDEMPOTENTS from the void -- exponents free")
    for t in (ladder, both):
        r = reach("new-idempotents", {}, t)
        ok = (r["stalled_at"] is None and not r["bad_adm"]
              and not r["bad_div"] and frontier_ok(r))
        check(ok, "new-idempotents stalled at %s: %s" % (t.name, r))
        print("      %-44s seated %2d, state %d digits, %d steps clean"
              % (t.name, r["seated"], r["digits"], REACH_STEPS))
    wit["depth"]["new-idempotents"] = "reaches " + both.name

    print("\n  (c) DYNAMICS from the void -- the maximal image")
    for t in (allp, both, three_inf, two_inf):
        r = reach("dynamics", {}, t)
        ok = (r["stalled_at"] is None and not r["bad_adm"]
              and not r["bad_div"] and r["lam_rises"] and frontier_ok(r))
        check(ok, "dynamics stalled at %s: %s" % (t.name, r))
        print("      %-44s seated %2d, lambda rose at every one of %d steps"
              % (t.name, r["seated"], REACH_STEPS))
    wit["depth"]["dynamics"] = "reaches " + three_inf.name
    wit["finsup"]["dynamics"] = "reaches " + three_inf.name
    print("      (2^oo is reachable though GREEDY dynamics never opens the")
    print("       2-window from the void: the invisibility is greed's, not")
    print("       the law's.)")

    print("\n  (d) DYNAMICS from a seed, and SEMISIMPLICITY's pinned exponents")
    r = reach("dynamics", {2: 1, 3: 1}, both)
    check(r["stalled_at"] is None and not r["bad_adm"] and not r["bad_div"],
          "dynamics stalled from seed 6: %s" % r)
    print("      seed 6, target 2^oo x every odd prime: %d steps clean, "
          "lambda rose %s" % (REACH_STEPS, r["lam_rises"]))
    # the finite-support branch from a NONEMPTY seed: an infinite column on a
    # prime the seed lacks, and one on a prime the seed already carries. The
    # void runs above never exercise either.
    for seed, tgt in (({2: 1, 3: 1}, sup_from_dict("6 x 7^oo",
                                                   {2: 1, 3: 1, 7: INF})),
                      ({2: 1, 3: 1, 5: 1}, sup_from_dict("30 x 5^oo",
                                                         {2: 1, 3: 1, 5: INF}))):
        r = reach("dynamics", seed, tgt)
        ok = (r["stalled_at"] is None and not r["bad_adm"]
              and not r["bad_div"] and r["lam_rises"])
        check(ok, "dynamics stalled at %s: %s" % (tgt.name, r))
        print("      %-40s %d steps clean, lambda rose at every one"
              % (tgt.name + ", finite support:", REACH_STEPS))
    r = reach("semisimplicity", {}, allp)
    check(r["stalled_at"] is None and not r["bad_adm"] and not r["bad_div"],
          "semisimplicity stalled: %s" % r)
    print("      semisimplicity, every prime once: seated %d, %d steps clean"
          % (r["seated"], REACH_STEPS))
    r = reach("semisimplicity", {}, mod4)
    print("      semisimplicity at a target wanting exponent 2: stalls at "
          "step %s (exponents are pinned to 1)" % r["stalled_at"])
    check(r["stalled_at"] is not None,
          "semisimplicity reached a target with an exponent above 1")

    print("\n  (e) OUT-OF-IMAGE targets -- the reason, scanned not asserted")
    SCAN = range(2, 2000)
    n_scan = len(SCAN)
    f = {7: 1}
    hits = [m for m in SCAN if adm_independence(f, m) and m % 7 == 0]
    check(not hits, "an independence move raised a seated 7: %s" % hits[:3])
    print("      independence, 7^oo: 0 of %d moves at state 7 touch the "
          "7-exponent -- seated depth is frozen, so no policy deepens it"
          % n_scan)
    f = {2: 1, 3: 1}
    hits = [m for m in SCAN
            if adm_independence(f, m) and (m % 2 == 0 or m % 3 == 0)]
    check(not hits, "an independence move touched a seed prime: %s" % hits[:3])
    print("      independence, a target raising a SEED exponent: 0 of %d "
          "moves at state 6 carry 2 or 3 -- the seed is frozen too" % n_scan)
    empty = [int_f(f) for f in
             ({2: 1}, {2: 1, 3: 1}, {2: 2, 3: 1, 5: 1}, {7: 3})
             if not any(adm_newidem(f, m) for m in range(2, 200))]
    check(not empty, "new-idempotents had an empty admissible set at %s" % empty)
    print("      new-idempotents, 3^oo alone: unreachable -- every admissible")
    print("      move seats a NEW prime (S2), so the support cannot stay finite")
    print("      while the run continues, and the run never halts")

    print("\n  (f) WHERE BREADTH SITS. The image factors into a SUPPORT choice")
    print("      and an EXPONENT choice, and breadth is one value of the first:")
    print("      the support must be ALL primes, out of a continuum of infinite")
    print("      support sets. Independence greedy takes the top of the support")
    print("      lattice AND the bottom of the exponent lattice -- every prime,")
    print("      every exponent 1 -- which is the single primorial limit. The")
    print("      filed avoiding policy keeps every exponent minimal and drops")
    print("      one support value, and that is the whole of why it holds no")
    print("      fate: it is an INTERIOR point of the same image.")

    # breadth, depth and mortality as corners of each image, witnessed
    print("\n  (g) THE THREE FATES AS CORNERS OF THE IMAGE")
    print("      %-16s %-9s %-9s %-9s" % ("law", "breadth", "depth", "mortality"))
    corners = {}
    for name, seed in (("independence", {}), ("semisimplicity", {}),
                       ("new-idempotents", {}), ("dynamics", {})):
        r = reach(name, seed, allp if name != "new-idempotents" else both)
        b = r["stalled_at"] is None and not r["bad_adm"] and not r["bad_div"]
        corners[name] = (b, name in wit["depth"], False)
    corners["transparency"] = (False, False, True)
    corners["semisimplicity"] = (corners["semisimplicity"][0], False, "seed 12")
    for name, _a, _r, _h in LAWS:
        c = corners[name]
        print("      %-16s %-9s %-9s %-9s"
              % (name, c[0], c[1], c[2]))
    check(corners["dynamics"][0] and corners["dynamics"][1],
          "dynamics does not hold both breadth and depth")
    print("      Breadth = support maximal, depth = an exponent maximal,")
    print("      mortality = both minimal (a finite limit). Three CORNERS of a")
    print("      two-coordinate body, and a generic member holds none of them.")
    print("      The breadth and depth columns are this section's own runs; the")
    print("      mortality column is S4's never-empty result, which prints")
    print("      BELOW this table -- it is cited here, not established here.")


_PSET = set(PRIMES)


# ------------------------------------------------ S4 the closure half

def s4_closure(wit):
    section("S4  THE CLOSURE HALF -- the invariant that bounds each image")

    states = [{}, {2: 1}, {2: 2}, {3: 1}, {2: 1, 3: 1}, {2: 1, 3: 1, 5: 1},
              {2: 2, 3: 1}, {5: 1}, {2: 3, 5: 2}, {2: 1, 3: 1, 5: 1, 7: 1},
              {7: 1}, {11: 2}, {2: 4, 3: 2, 5: 1}]
    MOVE = 600

    counts = {}
    for name, adm, _r, _h in LAWS:
        n_adm = n_touch = n_seatless = 0
        for f in states:
            for m in range(2, MOVE + 1):
                if not adm(f, m):
                    continue
                n_adm += 1
                fm = factorint(m)
                if any(f.get(p) for p in fm):
                    n_touch += 1
                if not any(not f.get(p) for p in fm):
                    n_seatless += 1
        counts[name] = (n_adm, n_touch, n_seatless)

    check(counts["independence"][1] == 0,
          "independence: %d moves touched a seated prime" % counts["independence"][1])
    check(counts["semisimplicity"][1] == 0, "semisimplicity touched a seated prime")
    check(counts["new-idempotents"][2] == 0,
          "new-idempotents admitted a move seating nothing")
    print("  independence:    %d admissible moves, %d touch a seated prime"
          % (counts["independence"][0], counts["independence"][1]))
    print("  semisimplicity:  %d admissible moves, %d touch a seated prime"
          % (counts["semisimplicity"][0], counts["semisimplicity"][1]))
    print("  new-idempotents: %d admissible moves, %d seat nothing"
          % (counts["new-idempotents"][0], counts["new-idempotents"][2]))
    print("  Each is a TAUTOLOGY given its demand; the range is engine")
    print("  consistency and the general reason is the demand itself.")

    # semisimplicity dies at a non-squarefree state -- the one blind law that
    # can halt, and the exception the coordinate reading needs.
    dead = [int_f(f) for f in states
            if any(e > 1 for e in f.values())
            and not any(adm_semisimplicity(f, m) for m in range(2, MOVE + 1))]
    check(len(dead) >= 3, "semisimplicity did not halt at a non-squarefree state")
    print("\n  semisimplicity halts outright at every non-squarefree state "
          "tested (%d of them: %s ...)" % (len(dead), dead[:3]))

    # never-empty for the three live laws
    for name, adm in (("independence", adm_independence),
                      ("new-idempotents", adm_newidem),
                      ("dynamics", adm_dynamics)):
        empties = []
        for n in range(1, 800):
            f = factorint(n) if n > 1 else {}
            if not any(adm(f, m) for m in range(2, 200)):
                empties.append(n)
        check(not empties, "%s had an empty admissible set at %s" % (name, empties[:3]))
        print("  %-16s admissible set nonempty at every state below 800"
              % name)
    print("  The general reason is one line each and not the range: a state")
    print("  has finitely many prime factors, so a coprime move exists")
    print("  (independence, and it seats a new prime so new-idempotents too);")
    print("  and any prime q > lambda(N) + 1 outside N has (q-1) not dividing")
    print("  lambda(N), so it raises lambda (dynamics). None of these three")
    print("  is mortal from ANY seed -- unlike semisimplicity just above.")

    # transparency: the reachable set is finite and is the filed lattice
    for s in (2, 6, 12, 30):
        seen, frontier = {s}, [s]
        while frontier:
            N = frontier.pop()
            for d in divisors(headroom(N)):
                if d < 2:
                    continue
                if N * d not in seen:
                    seen.add(N * d)
                    frontier.append(N * d)
        W = wall(lam(s))
        want = set(d * s for d in divisors(W // s))
        check(seen == want,
              "transparency reachable set from %d is not the lattice" % s)
        term = [N for N in seen if not [d for d in divisors(headroom(N)) if d >= 2]]
        check(term == [W], "transparency terminals from %d: %s" % (s, term))
    print("\n  transparency: reachable set = the multiples of s dividing "
          "W(lambda(s)),")
    print("  every maximal run terminal at that single state (seeds 2, 6, 12, 30)")
    print("  -- a FINITE image of one point, so finite support is available")
    print("  and infinite depth is not, both by exhaustion rather than by")
    print("  a move-level invariant.")
    print("\n  dynamics has NO closure invariant beyond never-empty, and that")
    print("  is the whole of it: no run halts, so no limit is finite, and")
    print("  every infinite multiple of the seed is reached (S3c). The image")
    print("  is maximal -- the only law here whose closure half is vacuous.")

    wit["finsup"]["transparency"] = "image is one finite point"
    wit["no"]["independence"] = "exponents frozen at seating (%d/%d moves)" % (
        counts["independence"][1], counts["independence"][0])
    wit["no"]["semisimplicity"] = "squarefree: exponents pinned to 1"
    wit["no"]["new-idempotents"] = "every move seats a new prime (%d/%d)" % (
        counts["new-idempotents"][2], counts["new-idempotents"][0])
    wit["no"]["transparency"] = "reachable set finite"
    wit["no"]["dynamics"] = ""
    return counts


# ------------------------------------------------------- S5 the square

def runs_forever(adm, seed, steps=40):
    """Greedy from the seed: True witnesses that SOME policy runs on, and is
    a proof of liveness. False says only that the GREEDY path dead-ends, and
    is not by itself a proof of mortality -- the two False rows below are
    mortal for reasons S4 establishes separately (transparency's reachable
    set is finite; semisimplicity has an empty admissible set at a
    non-squarefree state, so no policy has a move either)."""
    f = dict(seed)
    for _ in range(steps):
        m = 2
        while m < 4000 and not adm(f, m):
            m += 1
        if m >= 4000:
            return False
        f = mul_f(f, m)
    return True


def s5_square(wit):
    section("S5  THE TWO COORDINATES AGAINST THE FILED SQUARE")
    print("  Both coordinates are read off S3/S4 WITNESSES, never off the")
    print("  square: a column set to make the sort come out is not evidence.\n")

    # LIVENESS is measured per seed, not asserted: it is seed-dependent for
    # exactly one law and that is the exception the reading needs.
    print("  %-16s %-22s %-22s" % ("law", "live from 1", "live from 12"))
    live = {}
    for name, adm, _r, _h in LAWS:
        a = runs_forever(adm, {})
        b = runs_forever(adm, {2: 2, 3: 1})
        live[name] = (a, b)
        print("  %-16s %-22s %-22s" % (name, a, b))
    check(live["semisimplicity"] == (True, False),
          "semisimplicity liveness is not seed-dependent: %s"
          % (live["semisimplicity"],))
    check(live["transparency"] == (False, False),
          "transparency ran forever: %s" % (live["transparency"],))
    print("  Liveness is a property of (law, SEED), and semisimplicity is the")
    print("  witness: alive from a squarefree seed, dead on arrival from 12.")
    print("  A True here is a proof (a policy that runs on); a False is the")
    print("  GREEDY path dead-ending, and both False rows are mortal for the")
    print("  separate reasons S4 established -- a finite reachable set, and an")
    print("  empty admissible set that no policy can route around.")

    print("\n  %-16s %-9s %-14s %-6s %-9s %s" %
          ("law", "reading", "hosting", "depth", "fin-supp", "witness"))
    mism = 0
    for name, _a, r, h in LAWS:
        d = name in wit["depth"]
        s = name in wit["finsup"]
        # a NO must carry its closure invariant, or the column is unsupported
        # rather than negative -- an unwitnessed cell is a failure, not a "no".
        check(d or name in wit["no"],
              "%s has no depth witness and no closure reason" % name)
        check(s or name in wit["no"],
              "%s has no finite-support witness and no closure reason" % name)
        pred_depth = (h == "hosts both")
        pred_fin = (r == "sighted")
        bad = (pred_depth != d) or (pred_fin != s)
        mism += bad
        w = wit["depth"].get(name) or wit["finsup"].get(name) or wit["no"][name]
        print("  %-16s %-9s %-14s %-6s %-9s %s%s" %
              (name, r, h, "yes" if d else "no", "yes" if s else "no", w,
               "   <-- MISMATCH" if bad else ""))
    check(mism == 0, "square/coordinate mismatch count = %d" % mism)
    print("\n  mismatches: %d of %d laws" % (mism, len(LAWS)))
    print("  HOSTING decides whether an infinite exponent is reachable;")
    print("  READING decides whether a run may stop widening its support.")
    print("  The square does NOT decide the image itself -- independence and")
    print("  semisimplicity share a cell and have DIFFERENT images (S3d): same")
    print("  two coordinates, exponents free against exponents pinned to 1.")

    print("\n  MORTALITY IS THE BOTTOM CORNER, AND THE SQUARE DOES NOT REACH")
    print("  IT. What is true is a statement about the COORDINATES: a limit of")
    print("  finite support with no infinite exponent IS a finite integer, and")
    print("  every move multiplies by at least 2, so a run with that limit")
    print("  halts. Mortality is therefore the corner where both coordinates")
    print("  bottom out, and a law is mortal exactly when its image holds that")
    print("  corner. What does NOT follow is that the cell (sighted, hosts")
    print("  nothing) forces it: 'sighted' makes finite support AVAILABLE, not")
    print("  compulsory, so a law in that cell may still have infinite-support")
    print("  members and live forever. The attack is one law again --")
    print("  FRESH-DYNAMICS, m admissible iff m is a prime not dividing N and")
    print("  lambda(N*m) > lambda(N): it reads lambda (sighted), it never")
    print("  revisits a prime so it hosts no decrement (hosts nothing), and:")
    fd = lambda f, m: (m >= 2 and is_prime(m) and not f.get(m)
                       and lam_f(mul_f(f, m)) > lam_f(f))
    fresh_live = runs_forever(fd, {})
    f = dict()
    for _ in range(20):
        m = 2
        while not fd(f, m):
            m += 1
        f = mul_f(f, m)
    print("      live from the void: %s; after 20 steps %d primes seated, "
          "max exponent %d" % (fresh_live, omega_f(f), max(f.values())))
    check(fresh_live and max(f.values()) == 1,
          "the fresh-dynamics counterexample did not behave as derived")
    print("      -- a LIVE law in the cell, with no depth anywhere. The cell")
    print("      is not dead. Transparency is mortal for a reason the square")
    print("      never carried: its reachable set is FINITE (S4), which is the")
    print("      headroom fact, not a coordinate. So the square reads two")
    print("      coordinates of the image and mortality is not one of them.")
    print("  Liveness is not a property of the law either: semisimplicity dies")
    print("  from seed 12 and lives from 1, so it belongs to the PAIR.")

    # THE BOUNDARY OF THE CORRESPONDENCE, hunted rather than assumed: is the
    # reading axis a THEOREM about support-blind laws, or a fact about the
    # three filed ones? An adversarial blind law settles it.
    print("\n  IS THE READING AXIS A THEOREM ABOUT BLIND LAWS? A demand is")
    print("  support-blind when it is a function of prime support and")
    print("  squarefreeness alone -- and NON-semisimplicity, m admissible iff")
    print("  N*m is NOT squarefree, is blind by that same test. It is not one")
    print("  of the filed five; it is built here to attack the axis:")
    states = [{2: 1}, {2: 1, 3: 1}, {2: 2, 3: 1}, {5: 1}]
    adm_ct = seatless = 0
    for f in states:
        for m in range(2, 200):
            if m >= 2 and any(e > 1 for e in mul_f(f, m).values()):
                adm_ct += 1
                if not any(not f.get(p) for p in factorint(m)):
                    seatless += 1
    print("      %d admissible moves over the battery, %d of them seat NOTHING"
          % (adm_ct, seatless))
    check(seatless > 0, "the adversarial blind law admitted no seatless move")
    print("      -- so a blind law CAN stop widening its support (push a seated")
    print("      prime again), and its image holds finite-support members while")
    print("      the reading axis predicts none. The axis is therefore NOT a")
    print("      theorem about blindness. What the three filed blind demands")
    print("      share is stronger than blindness: each can only be MET by new")
    print("      support -- coprimality, squarefreeness, a raised omega. The")
    print("      correspondence is over the five filed laws, and this is its")
    print("      boundary, found by attacking it rather than by assuming it.")


def main():
    print("THE FATE IMAGE OF A DEMAND LAW")
    s1_control()
    if FAIL:
        print("\nPOSITIVE CONTROL FAILED -- no verdict is read.")
        return 1
    wit = {"depth": {}, "finsup": {}, "no": {}}
    s2_atlas()
    s3_reach(wit)
    s4_closure(wit)
    s5_square(wit)
    section("RESULT")
    if FAIL:
        print("FAILURES: %d" % len(FAIL))
        for m in FAIL:
            print("  - " + m)
        return 1
    print("all checks clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
