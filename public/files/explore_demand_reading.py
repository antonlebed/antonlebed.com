"""
explore_demand_reading.py -- WHICH DEMAND LAWS CAN READ, AND WHICH CAN
RUN? (sibling of explore_slack_machine.py, explore_growth_laws.py,
explore_archimedean_dial.py, explore_growth_machine.py).

THE QUESTION. A Minsky machine runs on the growth world using nothing
but multiplication: the counters are SLACKS delta_l = v_l(odd lambda(N))
- v_l(N) + 1 at seated odd primes, DEC is a push of the counter prime,
INC is an import of a fresh prime, and the branch is one bit -- did
lambda move? Whether that bit is legible turns out to depend on the
DEMAND LAW, i.e. on what the observer's admissibility probe is asking.
Three filed laws cannot see it and a fourth can, so "the growth world is
not universal" was never a statement about the growth world. It was a
statement about a probe repertoire.

That leaves the classification. Order the filed demand laws --
independence, new-idempotents, semisimplicity, dynamics, new-orders,
transparency -- by what their admissibility predicates can see, and find
where universality switches on.

THE SUSPICION ABOUT THE QUESTION ITSELF. The question above is written
in ONE-AXIS vocabulary, inherited from the filed demand CHAIN
(semisimplicity inside independence inside new-idempotents: three
strictly nested admissible sets). A machine needs TWO different things
from a law and only one of them is reading:

  the GATE   -- which moves may be MADE (the admissible set itself);
  the PROBE  -- one bit about an OFFERED move, made or not.

"Reading power" is the probe alone. Whether a law's admissible set can
carry an increment and a decrement at all is the gate, and it is a
separate question that the corpus has never asked. So this file derives
on two axes and expects a SQUARE rather than a chain.

THE MODEL (unchanged). A state is a positive integer N; a move is a
multiplication N -> N*m by any m >= 2. Write c_l = v_l(N) and
d_l = v_l(odd lambda(N)) for an odd prime l, so

    d_l = max(0, c_l - 1, max{ v_l(q-1) : q | N, q != l }),
    delta_l = d_l - c_l + 1,

and a push of l^e sends delta_l -> max(0, delta_l - e). A demand law is
an admissibility predicate A(N, m) on moves; the filed six are

  D-IND   independence     gcd(N, m) = 1
  D-MEM   new idempotents  omega(Nm) > omega(N)
  D-SEMI  semisimplicity   coprime, and N and m both squarefree
  D-DYN   new dynamics     lambda(Nm) != lambda(N)
  D-ORD   new orders       the set of realized unit orders grows
  D-TRA   transparency     N grows with lambda frozen

(D-RATE, the seventh, is an optimizer over D-MEM's admissible set rather
than a demand: it contributes a policy, not a predicate, so it inherits
D-MEM's probe and appears nowhere below.)

THE DESIGN, in seven sections. The slate is frozen before any engine
code; where a run contradicts it the framing is left standing and
flagged rather than quietly rewritten.

S1 POSITIVE CONTROL. Before any verdict is read, the engine's own
   Carmichael lambda must reproduce two things it did not compute here:
   the filed test pair -- N = 855 and N = 2565, identical prime support,
   both non-squarefree, slacks at 3 of 1 and 0, on which the three
   support-blind predicates score 0 disagreements over 398 offered moves
   while the dynamics predicate scores 17 -- and the filed hand word
   15 -> 105 -> 1995 -> 5985 -> 17955 -> 53865 with its slack track.

S2 THE ORDER IDENTITY. D-ORD is stated on unit orders and D-DYN on
   lambda, and they should be the SAME predicate: the orders realized by
   units of Z/N ought to be exactly the divisors of lambda(N), and
   lambda(N) divides lambda(Nm) always, so the order set grows strictly
   iff lambda moves. Brute-enumerated over a battery, every unit's order
   computed from the group rather than from the identity being tested.
   PREDICTION P1: 0 exceptions, and D-ORD's response vector equals
   D-DYN's move for move.

S3 THE READING TABLE. Every filed law scored on the ONE test object of
   S1, so the classification is a property of the predicate rather than
   of how each case was argued. The transplant to watch: "the
   admissibility probe answers the guard" is measured only at D-DYN, and
   D-TRA is its COMPLEMENT. A probe returns one bit, and the states a
   predicate separates are exactly the states its negation separates, so
   complementation should not change the score at all.
   PREDICTION P2: D-TRA's score equals D-DYN's exactly; the three
   support-blind laws stay at 0.

S4 THE PARTITION INSTRUMENT. A single pair is a coarse instrument. The
   general one: over a pool of states, a predicate induces a PARTITION
   by response vector (which offered moves it admits), and reading power
   is the refinement order on those partitions. The section computes
   every law's partition, compares each pair by refinement, and compares
   all of them against the partition by (prime support, squarefreeness).
   PREDICTION P3: the support-blind three coarsen the support partition;
   dynamics, new-orders and transparency induce ONE partition; and the
   two families are INCOMPARABLE -- neither refines the other.

S5 THE PADDED DECREMENT. The gate axis starts here. A bare DEC is a
   transparent push, so it is D-DYN-INADMISSIBLE exactly when the
   counter is positive -- the objection the filed verdict answers by
   separating the hand (which injects moves irrespective of
   admissibility) from the probe (which reads one bit). But a move is a
   multiplication by ANY m, so pad it: m = l*q with q a fresh prime
   chosen by coprime congruences to satisfy q != 1 mod every counter
   prime, so no counter's d moves, and (q-1) not dividing lambda(N), so
   lambda does move. Each seed is first raised by real increments so
   that the walk down crosses BOTH branches of the guard.
   PREDICTION P4: the padded move gives delta_l -> max(0, delta_l - 1)
   with every sibling untouched, and raises lambda in both branches --
   so it is admissible under D-DYN and under D-MEM, always.

S6 THE AUTONOMOUS RUN. If S5 holds, the machine can be made
   LAW-AUTONOMOUS: every move it MAKES is admissible, and the probe is
   spent on a move it never makes -- the bare push of l, whose
   admissibility bit is exactly the guard. The three filed programs
   (halts-iff-even, transfer, roundtrip) run on padded decrements and
   Dirichlet increments against a reference interpreter on plain
   integers, with every move made checked against the D-DYN predicate.
   PREDICTION P5: traces agree step for step, and 0 moves made are
   inadmissible. [The HAND-DRIVEN contrast in this section was added
   AFTER the run, and it is what corrects finding 7: with the moves
   supplied by a hand the law is consulted only as a probe, so a
   sighted law that cannot host the machine drives it perfectly well.
   The design above did not think to ask, and the square was first
   written as though hosting were required unconditionally.]

S7 THE HOSTING TABLE. The gate axis for the rest of the laws, each by
   its own argument, each measured.
     D-IND and D-SEMI host NO DECREMENT: delta_l falls only if c_l
       rises, i.e. only if l divides m; but l divides N once the counter
       is seated, so every such move is non-coprime. A coprime move can
       only raise a seated slack.
     D-TRA hosts NO INCREMENT: raising delta_l requires raising d_l
       (c_l never falls), and v_l(odd lambda) = d_l, so every increment
       moves lambda. And the transparent moves from N are exactly the m
       with Nm dividing W(lambda(N)) -- a FINITE set, where
       W(L) = 2^(v_2(L)+2) * prod{ p^(v_p(L)+1) : p odd, (p-1) | L }
       is the largest modulus with lambda dividing L. A finite reachable
       set cannot hold an unbounded counter.
     D-MEM hosts BOTH, by S5's padding, and is blind by S3.
   PREDICTIONS P6/P7: 0 moves raise a slack with lambda frozen, the
   transparent set is exactly the divisors of W/N in range; and 0
   coprime moves lower a seated counter's slack.

WHAT WOULD KILL WHAT (observables, not inferences). P1 dies if the rig
prints a realized order not dividing lambda, or a divisor of lambda not
realized. P2 dies if the printed D-TRA score differs from the printed
D-DYN score. P3 dies if the printed refinement table shows either family
containing the other. P4 dies on one printed padded move with the wrong
slack, a moved sibling, or a frozen lambda. P5 dies on one printed step
disagreeing with the reference, or one move made that the D-DYN
predicate rejects. P6 dies on a printed slack-raising move with lambda
frozen, or a transparent m outside the divisors of W/N. P7 dies on a
printed coprime move lowering a seated slack. What the square MEANS --
whether "universality switches on at D-DYN" is the right sentence, and
what it does or does not do to the three fates -- is weighed after the
run and is not frozen here.

FINDINGS.

1. THE ORDER IDENTITY -- ALREADY FILED; THIS IS A RE-VERIFICATION
   (rule, and NOT this file's result: explore_growth_laws.py finding 5
   states it and verifies it exhaustively over N = 3..1200, a wider
   range than the 407 states checked here). The orders realized by
   units of Z/N are exactly the divisors of lambda(N). (Lagrange on the
   exponent gives one inclusion; for the other, factor d | lambda as
   prod l^e and place each l^e in a CRT component whose own order has
   l-part at least e -- one exists because lambda is the lcm -- so the
   lcm of the parts is d.) And lambda(N) | lambda(Nm) always (0
   violations over 3582 pairs), so the order set grows strictly exactly
   when lambda moves: D-ORD and D-DYN are the SAME PREDICATE, not
   merely two laws with the same greedy pick. The six filed demand laws
   are five predicates, which is what this file needs it for. Kept
   because the control is worth having: Z/8 has four units and realizes
   only {1, 2}, so the engine is reading orders and not divisors of a
   group order. The first draft of this docstring presented it as a
   fresh theorem of its own, which it is not.

2. COMPLEMENT-INVARIANCE OF READING (the complementarity is filed --
   explore_hot_limit.py already has D-DYN and D-TRA partitioning the
   move space; the consequence for READING is this file's). D-TRA is
   the exact complement of D-DYN, and
   a probe returns ONE BIT about an offered move: the states a
   predicate separates are literally the states its negation separates,
   so two complementary demands have IDENTICAL reading power however
   opposed their admissible sets. Both score 17 disagreements over the
   398 offered moves of the filed test pair, as does D-ORD, while
   semisimplicity, independence and new-idempotents score 0. So reading
   power is a property of the PARTITION a predicate induces and never of
   which side of it the law calls admissible, and the sighted family is
   ONE predicate up to identity and complement.

3. THE FILED TRANSPARENCY WALL, RE-READ AS A READING BOUND (the wall:
   rule, explore_growth_laws.py finding 6, which owns the lcm-closure
   argument; the re-reading: this file's). Because lambda(N) |
   lambda(Nm), a move is transparent iff lambda(Nm) | lambda(N) iff
   Nm | W(lambda(N)), so the transparent moves from N are exactly the
   divisors of

       V(N) = W(lambda(N)) / N,   THE TRANSPARENCY HEADROOM,

   where W(L) is the largest modulus whose lambda divides L. That set
   identity is NOT new -- V is the wall cofactor whose divisors
   explore_depth_observer.py's wall-priced normalizer sums over, and
   whose complement explore_hot_limit.py names as the dynamics law's
   upward-closed admissible set. What is new is what it means for
   READING: a lambda-probe's response to N is precisely the indicator
   of that divisor set, so V is the sighted family's ENTIRE reading of
   a state, one number, and finding 4 follows from that. Verified
   exactly here over 11 states against every move up to 3000. (W's
   2-part is 2 when L is odd and 2^(v_2(L)+2) when it is even -- not a
   corner to wave past, since L = 1 is the state the tower starts from
   and lambda(4) = 2 does not divide 1. The first draft of wall() had
   2^(v_2(L)+2) unconditionally and was wrong at every odd lambda; it is
   now controlled against its DEFINITION -- the largest modulus found by
   search -- over the 79 states whose wall fits under the search cap,
   which is the check that would have caught it immediately. Comparing
   only where the wall fits is load-bearing: a truncated search reports
   the formula wrong for every large wall, which is exactly the false
   alarm the first attempt at this control produced.)

4. THE TWO READINGS ARE INCOMPARABLE (rule; both directions proved
   rather than measured). The blind family's response is exactly a
   function of (prime support, squarefreeness) -- constant on every such
   class over the pool -- and by finding 3 the sighted family's response
   is exactly a function of the headroom. Neither number determines the
   other, and there is a witness each way:
     SIGHTED SEES, BLIND CANNOT: N = 855 and N = 2565 share support
       {3, 5, 19} and squarefreeness, with headrooms 161616 and 53872.
     BLIND SEES, SIGHTED CANNOT: N = 10 and N = 11 share the headroom
       24 with supports {2, 5} and {11}. Equal headroom means an equal
       transparent set, so the sighted probe agrees on EVERY move there
       is -- a proof of blindness, not a range-limited measurement.
   So reading power is neither a chain nor a refinement order, and the
   filed demand chain's nesting says nothing about what its members can
   see. The frozen prediction called incomparability correctly and
   justified it WRONGLY -- the offered reason was lambda(3) = lambda(4)
   with different support, which fails, since the headrooms are 8 and 6
   and the sighted probe separates them. The first refinement check was
   also written in the wrong direction (a predicate that is a function
   of support induces a partition COARSER than the support partition,
   not finer) and printed three failures that were the code's, not the
   world's. Both are recorded rather than quietly corrected.

5. THE PADDED DECREMENT (rule; verified over 18 decrements at 2, 3 and 4
   counters, each walk crossing both branches of the guard). A move is a
   multiplication by ANY m, so the decrement need not be the bare push.
   Take m = l*q with q a fresh prime satisfying q != 1 mod every counter
   prime (coprime congruences, so Dirichlet supplies them) and
   (q-1) not dividing lambda(N). Then delta_l -> max(0, delta_l - 1)
   exactly, no sibling moves, and lambda moves in BOTH branches:
   0 wrong slacks, 0 perturbed siblings, 0 frozen lambdas. The pad
   contributes 0 to every counter's genome exponent, so it stays inert
   for the rest of the run.

6. THE MACHINE IS LAW-AUTONOMOUS (rule; verified, three programs
   against a reference interpreter, 0 inadmissible moves in the whole
   suite). With finding 5 the machine makes ONLY admissible moves and
   still reads its guard, by spending 79 probes on a move it never
   makes: the bare push of l, whose admissibility bit is exactly
   delta_l = 0. This DISSOLVES the objection the filed verdict has to
   argue around -- the hand no longer injects anything inadmissible, so
   "a machine restricted to admissible moves would have no decrement" is
   false UNDER THIS LAW (it stays true under independence and
   semisimplicity, which admit no slack-lowering move at all -- finding
   7), and the separation of the observer's two gifts stops being
   load-bearing for universality HERE. It is still exactly what carries
   the hand-driven machine of finding 7, where the law is consulted only
   as a probe. What survives of it in general is exact
   and about a SINGLE move: a move admissible in both branches carries
   no bit, and a move carrying the bit is inadmissible in one branch. A
   machine that wants both uses two different moves, which is what this
   one does. (Largest import 1.61e6, below the deterministic
   Miller-Rabin base set's ~3.3e24, so nothing here rests on a probable
   prime.)

7. THE READING-HOSTING SQUARE (the headline; rule). A machine needs two
   different things from a demand law and the corpus had only ever asked
   for one. The GATE is which moves may be made; the PROBE is one bit
   about an offered move. Hosting, measured:
     D-IND, D-SEMI host NO DECREMENT. delta_l falls only if c_l rises,
       i.e. only if l | m, and l | N once the counter is seated, so
       every such move is non-coprime: 0 of 2342 coprime moves lowered a
       seated slack.
     D-TRA hosts NO INCREMENT. Raising delta_l requires raising d_l, and
       v_l(odd lambda) = d_l: 0 of 721 slack-raising moves left lambda
       frozen. Worse, by finding 3 its whole reachable set is the
       divisors of one headroom -- 5, 20, 20, 160, 10 and 80 states for
       the tabled seeds -- and a finite reachable set cannot hold an
       unbounded counter.
     D-MEM hosts BOTH, by finding 5's padding (the pad is a new prime
       every time, so the idempotent count grows).
   Each law in the first column still hosts the OTHER instruction: the
   coprime import is exactly what D-IND and D-SEMI admit, and the
   transparent push IS the decrement (a push of a SEATED l is transparent
   iff delta_l >= 1, the lambda-move criterion read the other way and at
   the criterion's own scope, a first push moving lambda for another
   reason -- which is exactly when the decrement does anything). So the
   column is a law
   missing ONE of the pair and never a law hosting neither.
   With finding 4 the two axes are independent, and the filed laws fill
   all four cells:

                     hosts one            hosts both
       blind         D-IND, D-SEMI        D-MEM
       sighted       D-TRA                D-DYN == D-ORD

   WHICH CELL BUYS UNIVERSALITY DEPENDS ON WHAT THE MACHINE IS ALLOWED
   TO DO, and both answers are measured here rather than argued:
     HAND-DRIVEN (the filed model -- moves come from the hand
       irrespective of admissibility and the law supplies only the
       probe): universality is exactly SIGHTEDNESS. The transparency
       law drives all three programs step for step against the
       reference while making 104 moves it rejects itself, so a law
       that cannot host the machine still buys it when something else
       supplies the moves.
     LAW-AUTONOMOUS (every move MADE is admissible): universality is
       sighted AND hosting, which exactly one filed law is. Here D-MEM
       supplies the moves and cannot read them, and D-TRA reads the bit
       and cannot supply them.
   So HOSTING IS THE PRICE OF AUTONOMY, and the square classifies the
   autonomous case. Universality does not switch on at a point along a
   reading chain; it switches on at a corner whose position depends on
   whether the machine is allowed a hand. The first draft of this
   finding said flatly that universality needs both coordinates, which
   is the autonomous half stated as the whole -- caught by running the
   hand-driven contrast that S6 now carries.

8. WHAT THIS DOES NOT DO TO THE THREE FATES (scope, and it is the
   claim most worth not making). The universal machine is a FREE policy
   over a law's admissible set; the fates are filed at TWO different
   policy strengths, and lumping them is the error to avoid.
     MORTALITY is policy-INDEPENDENT -- explore_selection_frame.py
       verifies that every policy dies at W -- and finding 7 says why in
       the machine's own vocabulary: the reachable set is the divisors
       of one headroom, so there is no room for a policy to matter.
       Non-hosting and policy-independence are ONE fact seen twice.
     BREADTH and DEPTH are greedy and thermal statements, and only
       there does a free policy have room to do something else.
   So a hosting law does not touch the filed fate results; it makes the
   FREE-POLICY fate question undecidable over its own admissible set,
   which is a different question. "The three fates are
   demand-law-relative" would be an overclaim, and so is "the three
   fates classify greedy runs" -- the first draft of this finding said
   exactly that, annexing the one fate that holds under every policy.
   The honest statement is that fate is decidable-by-policy rather than
   by demand, and that the fate with no policy freedom is precisely the
   one whose law cannot host the machine.

SCOPE AND CAVEATS. The classification covers the SIX filed demand laws
and no more; a seventh predicate could land anywhere in the square, and
the instruments here are built to take one (append a row to
DEMAND_LAWS, or hand blind_score a predicate). D-RATE is an optimizer
over D-MEM's admissible set rather than a demand, so it contributes a
policy and no probe, and is classified nowhere. Findings 1, 2 and 3 are
proofs checked against a battery; findings 5, 6 and 7's hosting rows are
measurements over the stated ranges, and universality in finding 7 is
Minsky's theorem applied to a verified instruction set, not an
exhaustive claim over programs. The transparency wall's divisor
identity is exact, but its verification here is capped at moves up to
3000.

RUN RECORD. Python 3, no third-party dependencies, ~2 s wall clock,
negligible memory. Seven sections, all checks pass. Nearly all of the
runtime is S4's control on wall(), which brute-forces the largest
modulus with lambda | L over a 60000-wide search for 79 states; the rest
of the file is a tenth of a second, because products are never factored
(a move's lambda is read by merging two cached factorizations) and the
machine holds its state as a depth vector, so a product of large imports
stays tractable. The positive control runs first and the run aborts
before any verdict is read if it fails.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import gcd, lcm

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
        d += 1
    if r > 1:
        f[r] = f.get(r, 0) + 1
    if n < 1 << 22:
        _FCACHE[n] = f
    return f


def lam_pp(q, a):
    if q == 2:
        return 1 if a == 1 else (2 if a == 2 else 1 << (a - 2))
    return q ** (a - 1) * (q - 1)


def lam_fac(f):
    """Carmichael lambda from a factorization dict."""
    L = 1
    for q, a in f.items():
        L = lcm(L, lam_pp(q, a))
    return L


def lam(n):
    return lam_fac(factorint(n))


def merge(f, g):
    h = dict(f)
    for p, a in g.items():
        h[p] = h.get(p, 0) + a
    return h


def lam_prod(N, m):
    """lambda(N*m) without ever factoring the product -- the hot path."""
    return lam_fac(merge(factorint(N), factorint(m)))


def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


def v_p(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def d_of(N, l):
    return v_p(oddpart(lam(N)), l)


def c_of(N, l):
    return v_p(N, l)


def delta(N, l):
    """The slack at l: free pushes of l left before l writes to the genome."""
    return d_of(N, l) - c_of(N, l) + 1


def delta_prod(N, m, l):
    """The slack at l after the move N -> N*m, product never factored."""
    f = merge(factorint(N), factorint(m))
    return v_p(oddpart(lam_fac(f)), l) - f.get(l, 0) + 1


def sqfree(n):
    return all(a == 1 for a in factorint(n).values())


def divisors(n):
    ds = [1]
    for p, a in factorint(n).items():
        ds = [d * p ** i for d in ds for i in range(a + 1)]
    return sorted(ds)


def wall(L):
    """The largest modulus whose Carmichael lambda divides L.

    lambda(2^a) is 1, 2, then 2^(a-2), so the 2-part caps at 2 when L is ODD
    and at 2^(v_2(L)+2) when it is even -- the odd case is not a corner to be
    waved past, since L = 1 is the state the tower starts from. For odd p,
    lambda(p^a) = p^(a-1)(p-1) divides L iff (p-1) | L and a <= v_p(L)+1.
    """
    W = 2 if L % 2 else 2 ** (v_p(L, 2) + 2)
    for d in divisors(L):
        p = d + 1
        if p > 2 and is_prime(p):
            W *= p ** (v_p(L, p) + 1)
    return W


def headroom(N):
    """The transparency headroom V(N) = W(lambda(N))/N.

    By S4's re-reading of the filed transparency wall, this single number IS
    the sighted family's entire reading of N: the transparent moves from N are
    exactly the divisors of V, so two states sharing a headroom are
    indistinguishable to a lambda-reading probe over EVERY offered move, not
    merely over a range.
    """
    return wall(lam(N)) // N


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


# ------------------------------------------------------------ the demand laws

# Each law as (name, predicate) on (state, offered move). The probe axis is
# measured through this table alone, so classifying a further law is appending
# one row. D-ORD is stated on unit orders, not on lambda -- S2 is what earns
# the right to implement it through the divisor set.
def adm_ind(N, m):
    return gcd(N, m) == 1


def adm_mem(N, m):
    return any(N % p != 0 for p in factorint(m))


def adm_semi(N, m):
    return gcd(N, m) == 1 and sqfree(m) and sqfree(N)


def adm_dyn(N, m):
    return lam_prod(N, m) != lam(N)


def adm_tra(N, m):
    return lam_prod(N, m) == lam(N)


def adm_ord(N, m):
    return set(divisors(lam_prod(N, m))) != set(divisors(lam(N)))


DEMAND_LAWS = [
    ("D-SEMI  semisimplicity", adm_semi),
    ("D-IND   independence", adm_ind),
    ("D-MEM   new idempotents", adm_mem),
    ("D-DYN   new dynamics", adm_dyn),
    ("D-ORD   new orders", adm_ord),
    ("D-TRA   transparency", adm_tra),
]

TEST_PAIR = (855, 2565)
TEST_MOVES = range(2, 400)


def blind_score(pred, A, B, moves=TEST_MOVES):
    """How often a predicate distinguishes two states -- 0 means blind to them.

    A pair agreeing on prime support and squarefreeness but differing on the
    slack guard is a TEST OBJECT: a predicate scoring 0 on it cannot evaluate
    the guard, hence cannot drive a fused test-and-decrement, while a predicate
    scoring above 0 is a candidate reader.
    """
    return sum(1 for m in moves if pred(A, m) != pred(B, m))


# ---------------------------------------------------- S1  positive control

def s1_positive_control():
    print("S1  POSITIVE CONTROL -- the engine reproduces figures fixed elsewhere")
    A, B = TEST_PAIR
    ok = True
    ok &= check(set(factorint(A)) == set(factorint(B)),
                "S1 the test pair shares prime support")
    ok &= check(not sqfree(A) and not sqfree(B),
                "S1 both states of the test pair are non-squarefree")
    ok &= check(delta(A, 3) == 1 and delta(B, 3) == 0,
                "S1 the test pair has slacks 1 and 0 at the counter prime 3")
    print("    N=%d and N=%d: support %s, both non-squarefree, slacks %d and %d"
          % (A, B, sorted(factorint(A)), delta(A, 3), delta(B, 3)))
    for name, pred, want in (("independence", adm_ind, 0),
                             ("new-idempotents", adm_mem, 0),
                             ("semisimplicity", adm_semi, 0),
                             ("dynamics", adm_dyn, 17)):
        got = blind_score(pred, A, B)
        ok &= check(got == want,
                    "S1 filed score for %s is %d, engine says %d"
                    % (name, want, got))
    print("    filed scores over %d offered moves reproduced: 0, 0, 0, and 17"
          % len(TEST_MOVES))

    word = [(15, 0, 0), (105, 1, 0), (1995, 2, 0),
            (5985, 1, 0), (17955, 0, 0), (53865, 0, 0)]
    for N, x, y in word:
        ok &= check(delta(N, 3) == x, "S1 hand word: delta_3(%d) == %d" % (N, x))
        ok &= check(delta(N, 5) == y, "S1 hand word: delta_5(%d) == %d" % (N, y))
    ok &= check(d_of(17955, 3) == 2 and d_of(53865, 3) == 3,
                "S1 hand word: the push at slack zero raises the genome")
    print("    hand word 15 -> 105 -> 1995 -> 5985 -> 17955 -> 53865 reproduced")
    print("    control %s\n" % ("PASSES" if ok else "FAILS"))
    return ok


# ------------------------------------------------------- S2  the order identity

def realized_orders(N):
    """Every order realized by a unit of Z/N, computed from the group itself."""
    if N == 1:
        return {1}
    L = lam(N)
    Lp = list(factorint(L)) if L > 1 else []
    got = set()
    for u in range(1, N):
        if gcd(u, N) != 1:
            continue
        o = L
        for p in Lp:
            while o % p == 0 and pow(u, o // p, N) == 1:
                o //= p
        got.add(o)
    return got


def s2_order_identity():
    print("S2  THE ORDER IDENTITY -- are D-ORD and D-DYN the same predicate?")
    # A control first: a section whose only possible print is "they agree" is
    # not a test. realized_orders must compute ORDERS, so it must reproduce
    # known ones and must NOT return the divisors of the group ORDER -- Z/8 has
    # four units and no element of order 4, which is the standard separation.
    ok = check(all(pow(u, o, 7) == 1 and
                   all(pow(u, k, 7) != 1 for k in range(1, o))
                   for u, o in ((2, 3), (3, 6), (6, 2))),
               "S2 control: the engine's element orders mod 7 are right")
    phi8 = sum(1 for u in range(1, 8) if gcd(u, 8) == 1)
    ok &= check(realized_orders(8) == {1, 2} != set(divisors(phi8)),
                "S2 control: Z/8 realizes {1,2}, not the divisors of its order")
    print("    control: orders mod 7 correct; Z/8 has %d units and realizes %s,"
          " not %s" % (phi8, sorted(realized_orders(8)), divisors(phi8)))
    battery = list(range(1, 401)) + [512, 561, 855, 1024, 1155, 1729, 2565]
    bad = [N for N in battery if realized_orders(N) != set(divisors(lam(N)))]
    ok &= check(not bad,
                "S2 realized unit orders are the divisors of lambda (%d exceptions)"
                % len(bad))
    print("    orders(Z/N) == divisors(lambda(N)) over %d states: %d exceptions"
          % (len(battery), len(bad)))
    pairs, mono = 0, 0
    for N in range(1, 200):
        for m in range(2, 20):
            pairs += 1
            if lam_prod(N, m) % lam(N) != 0:
                mono += 1
    ok &= check(mono == 0, "S2 lambda(N) divides lambda(Nm) over the battery")
    print("    lambda(N) | lambda(Nm) over %d (state, move) pairs: %d violations"
          % (pairs, mono))
    A, B = TEST_PAIR
    same = all(adm_ord(A, m) == adm_dyn(A, m) and adm_ord(B, m) == adm_dyn(B, m)
               for m in TEST_MOVES)
    ok &= check(same, "S2 D-ORD and D-DYN agree move for move on the test pair")
    print("    D-ORD and D-DYN agree on every offered move of the test pair: %s"
          % ("yes" if same else "NO"))
    print("    -- so the order set grows strictly exactly when lambda moves,")
    print("       and the six filed laws are five predicates.\n")
    return ok


# -------------------------------------------------------- S3  the reading table

def s3_reading_table():
    print("S3  THE READING TABLE -- every filed law on the one test object")
    A, B = TEST_PAIR
    by = {}
    for name, pred in DEMAND_LAWS:
        s = blind_score(pred, A, B)
        by[name] = s
        print("    %-24s %-7s  %3d disagreements over %d offered moves"
              % (name, "BLIND" if s == 0 else "SIGHTED", s, len(TEST_MOVES)))
    ok = check(by["D-TRA   transparency"] == by["D-DYN   new dynamics"],
               "S3 the complement law scores exactly what the law scores")
    ok &= check(by["D-ORD   new orders"] == by["D-DYN   new dynamics"],
                "S3 D-ORD scores what D-DYN scores")
    for n in ("D-SEMI  semisimplicity", "D-IND   independence",
              "D-MEM   new idempotents"):
        ok &= check(by[n] == 0, "S3 %s is blind to the test pair" % n)
    ok &= check(by["D-DYN   new dynamics"] > 0, "S3 the dynamics law is sighted")
    # complement-invariance is not a coincidence of this pair: the states a
    # predicate separates are literally the states its negation separates.
    comp = all(blind_score(pred, A, B) ==
               blind_score(lambda N, m, p=pred: not p(N, m), A, B)
               for _, pred in DEMAND_LAWS)
    ok &= check(comp, "S3 every law scores what its complement scores")
    print("    complementing a predicate never changes its score: %s"
          % ("yes" if comp else "NO"))
    print("    -- so the reading axis has TWO points here, not a chain, and the")
    print("       sighted laws are ONE predicate up to identity and complement.\n")
    return ok


# ---------------------------------------------- S4  the partition instrument

POOL = sorted(set([3 ** a * 5 * e for a in range(1, 7) for e in (1, 7, 19, 163)]
                  + [4, 8, 9, 16, 27, 32, 45, 105, 225, 315, 1155]))
POOL_MOVES = range(2, 40)


def partition_of(pred, pool=POOL, moves=POOL_MOVES):
    """Group states by response vector -- the states a probe cannot tell apart."""
    blocks = {}
    for N in pool:
        blocks.setdefault(tuple(pred(N, m) for m in moves), []).append(N)
    return frozenset(frozenset(b) for b in blocks.values())


def refines(P, Q):
    """Every block of P sits inside a block of Q -- P sees at least what Q sees."""
    return all(any(b <= c for c in Q) for b in P)


def s4_partition_instrument():
    print("S4  THE PARTITION INSTRUMENT -- what each family's probe reveals")
    ok = True
    # (a) THE HEADROOM LEMMA. lambda(N) always divides lambda(Nm), so a move is
    # transparent iff lambda(Nm) | lambda(N) iff Nm | W(lambda(N)) iff m | V(N).
    # The transparent set is therefore the divisor set of ONE number, and the
    # sighted response vector reveals that number and nothing else.
    # A control on wall() first, against its DEFINITION rather than its
    # formula: the largest modulus whose lambda divides L, found by search.
    # Only states whose wall fits under the search cap are comparable -- a
    # truncated search would report the formula wrong for every large wall.
    cap_w, wbad, wtested = 60000, 0, 0
    for N in range(1, 120):
        L = lam(N)
        if wall(L) >= cap_w:
            continue
        wtested += 1
        if max(M for M in range(1, cap_w) if L % lam(M) == 0) != wall(L):
            wbad += 1
    ok &= check(wbad == 0, "S4 control: wall() is the largest modulus with"
                           " lambda | L (%d bad)" % wbad)
    print("    control: wall() == the brute-forced largest modulus over %d"
          " comparable states, %d mismatches" % (wtested, wbad))
    cap, bad = 3000, 0
    for N in (1, 2, 3, 4, 15, 45, 105, 225, 315, 855, 2565):
        want = [d for d in divisors(headroom(N)) if 2 <= d <= cap]
        got = [m for m in range(2, cap + 1) if lam_prod(N, m) == lam(N)]
        if got != want:
            bad += 1
        print("    N=%-6d lambda=%-8d headroom V=%-10d transparent m<=%d: %d %s"
              % (N, lam(N), headroom(N), cap, len(got),
                 "== divisors of V" if got == want else "!= divisors of V"))
    ok &= check(bad == 0, "S4 the transparent set is the divisor set of V (%d bad)"
                % bad)
    # (b) and the blind family reveals exactly (prime support, squarefreeness)
    groups = {}
    for N in POOL:
        groups.setdefault((tuple(sorted(factorint(N))), sqfree(N)), []).append(N)
    blind_const = True
    for block in groups.values():
        for name, pred in DEMAND_LAWS[:3]:
            vecs = set(tuple(pred(N, m) for m in POOL_MOVES) for N in block)
            blind_const &= len(vecs) == 1
    ok &= check(blind_const,
                "S4 the blind response is a function of (support, squarefreeness)")
    print("    the blind response is constant on each (support, squarefree)"
          " class: %s" % ("yes" if blind_const else "NO"))
    # (c) so the two readings are two numbers, and neither determines the other.
    #     Both directions are PROVED, not measured: same headroom means the
    #     sighted probe agrees on every move there is.
    A, B = TEST_PAIR
    ok &= check(headroom(A) != headroom(B) and
                (tuple(sorted(factorint(A))), sqfree(A)) ==
                (tuple(sorted(factorint(B))), sqfree(B)),
                "S4 the filed pair shares a support class and splits the headroom")
    print("    sighted sees, blind cannot:  N=%d and N=%d -- support %s and"
          " squarefreeness\n      shared, headrooms %d and %d"
          % (A, B, sorted(factorint(A)), headroom(A), headroom(B)))
    C = D = None
    seen = {}
    for N in range(1, 4001):
        V = headroom(N)
        for M in seen.get(V, []):
            if set(factorint(M)) != set(factorint(N)):
                C, D = M, N
                break
        if C:
            break
        seen.setdefault(V, []).append(N)
    ok &= check(C is not None, "S4 a headroom collision across supports exists")
    if C:
        print("    blind sees, sighted cannot: N=%d and N=%d -- supports %s and"
              " %s,\n      one headroom %d, so the sighted probe agrees on EVERY"
              " move" % (C, D, sorted(factorint(C)), sorted(factorint(D)),
                         headroom(C)))
        ok &= check(all(adm_dyn(C, m) == adm_dyn(D, m) for m in range(2, 400)),
                    "S4 the collision pair is invisible to the dynamics probe")
        ok &= check(blind_score(adm_ind, C, D) > 0,
                    "S4 the collision pair is visible to independence")
    # the partition table, as a summary of the two characterizations above
    support = frozenset(frozenset(b) for b in groups.values())
    parts = dict((name, partition_of(pred)) for name, pred in DEMAND_LAWS)
    print("    pool of %d states, %d offered moves; the (support, squarefree)"
          " partition has %d blocks" % (len(POOL), len(POOL_MOVES), len(support)))
    print("    %-24s blocks  coarsens (support, squarefree)?" % "law")
    for name, _ in DEMAND_LAWS:
        P = parts[name]
        r = refines(support, P)
        print("    %-24s %6d  %s" % (name, len(P), "yes" if r else "no"))
        if name.split()[0] in ("D-SEMI", "D-IND", "D-MEM"):
            ok &= check(r, "S4 %s coarsens the support partition" % name.split()[0])
    dyn = parts["D-DYN   new dynamics"]
    ok &= check(dyn == parts["D-ORD   new orders"] == parts["D-TRA   transparency"],
                "S4 dynamics, new-orders and transparency induce ONE partition")
    print("    dynamics, new-orders and transparency induce one partition: %s"
          % ("yes" if dyn == parts["D-ORD   new orders"] ==
             parts["D-TRA   transparency"] else "NO"))
    print("    -- so reading power is not a chain and not a refinement: the blind")
    print("       family reads (support, squarefreeness), the sighted family")
    print("       reads the headroom, and neither number determines the other.\n")
    return ok


# -------------------------------------------------------- S5  padded decrement

COUNTERS = (3, 5)


def d_vec(state, l):
    return max([0, state.get(l, 0) - 1] +
               [v_p(q - 1, l) for q in state if q != l])


def delta_vec(state, l):
    return d_vec(state, l) - state.get(l, 0) + 1


def lam_vec(state):
    return lam_fac(state)


def push(state, q, e=1):
    s = dict(state)
    s[q] = s.get(q, 0) + e
    return s


def dirichlet_witness(l, j, others, tries=20000):
    """An increment: v_l(q-1) exactly j, and q != 1 mod any sibling counter."""
    base = l ** j
    step = base * l
    for k in range(tries):
        q = base + 1 + k * step
        if any((q - 1) % o == 0 for o in others):
            continue
        if is_prime(q) and v_p(q - 1, l) == j:
            return q
    return None


def growth_inc(state, l, counters):
    """Raise the slack at l, disturbing no sibling counter."""
    q = dirichlet_witness(l, d_vec(state, l) + 1,
                          [p for p in counters if p != l])
    return push(state, q), q


def junk_prime(state, counters, tries=20000):
    """A prime that moves lambda and touches no counter -- the decrement's pad.

    Wanted: q prime, absent from the state, with q != 1 mod every counter prime
    (so no counter's genome exponent moves) and (q-1) not dividing lambda(N)
    (so the padded move raises lambda in BOTH branches of the guard). All the
    conditions are coprime congruences plus one divisibility, so such primes
    are plentiful; the search is bounded by candidates tried, not by magnitude.
    """
    L = lam_vec(state)
    q = max(state) | 1
    for _ in range(tries):
        q += 2
        if q in state or any((q - 1) % c == 0 for c in counters):
            continue
        if is_prime(q) and L % (q - 1) != 0:
            return q
    return None


def padded_dec(state, l, counters):
    """DEC as the single move m = l*q -- the slack falls, and lambda moves."""
    q = junk_prime(state, counters)
    if q is None:
        return None, None
    return push(push(state, l), q), q


def s5_padded_decrement():
    print("S5  THE PADDED DECREMENT -- a decrement that raises lambda anyway")
    ok = True
    print("    counters         l   delta walk            siblings moved"
          "   lambda frozen")
    checked, sib_bad, lam_bad, slack_bad = 0, 0, 0, 0
    for counters, l, raises in (((3, 5), 3, 3), ((3, 5), 5, 3),
                                ((3, 5, 7), 3, 2), ((3, 5, 7, 11), 7, 2)):
        state = dict((p, 1) for p in counters)
        for _ in range(raises):          # real increments first, so the walk
            state, _ = growth_inc(state, l, counters)   # down crosses BOTH
        walk, sibs, frozen = [delta_vec(state, l)], 0, 0
        for _ in range(raises + 2):      # two steps past zero
            before = dict((p, delta_vec(state, p)) for p in counters)
            lam_before = lam_vec(state)
            state, q = padded_dec(state, l, counters)
            ok &= check(state is not None, "S5 no junk prime available")
            if state is None:
                break
            after = dict((p, delta_vec(state, p)) for p in counters)
            checked += 1
            walk.append(after[l])
            if after[l] != max(0, before[l] - 1):
                slack_bad += 1
            n = sum(1 for p in counters if p != l and after[p] != before[p])
            sibs += n
            sib_bad += n
            if lam_vec(state) == lam_before:
                frozen += 1
                lam_bad += 1
        print("    %-16s %2d   %-21s %14d   %13d"
              % (str(counters), l, " -> ".join(str(v) for v in walk),
                 sibs, frozen))
    ok &= check(slack_bad == 0, "S5 every padded move gave truncated subtraction")
    ok &= check(sib_bad == 0, "S5 no padded move perturbed a sibling counter")
    ok &= check(lam_bad == 0, "S5 every padded move raised lambda")
    print("    %d padded decrements: %d wrong slacks, %d moved siblings,"
          " %d frozen lambdas" % (checked, slack_bad, sib_bad, lam_bad))
    print("    -- so the decrement is admissible under the dynamics law in BOTH")
    print("       branches, and the probe is spent on a move never made.\n")
    return ok


# ------------------------------------------------------- S6  the autonomous run

PARITY = {"L0": ("DEC", "x", "L1", "HALT"),
          "L1": ("DEC", "x", "L0", "LOOP")}
TRANSFER = {"T0": ("DEC", "x", "T1", "HALT"),
            "T1": ("INC", "y", "T0")}
ROUNDTRIP = {"R0": ("DEC", "x", "R1", "R2"),
             "R1": ("INC", "y", "R0"),
             "R2": ("DEC", "y", "R3", "HALT"),
             "R3": ("INC", "x", "R2")}


def reference_run(x0, program=PARITY, budget=200):
    cnt = {"x": x0, "y": 0}
    pc, trace = sorted(program)[0], []
    for _ in range(budget):
        if pc in ("HALT", "LOOP"):
            return pc, trace
        ins = program[pc]
        if ins[0] == "DEC":
            _, c, nz, z = ins
            if cnt[c] > 0:
                cnt[c] -= 1
                pc = nz
            else:
                pc = z
        else:
            _, c, nxt = ins
            cnt[c] += 1
            pc = nxt
        trace.append((pc, cnt["x"], cnt["y"]))
    return "BUDGET", trace


def autonomous_run(x0, program=PARITY, budget=200):
    """The machine with every move it MAKES admissible under the dynamics law.

    DEC is the padded move l*q of S5; INC is a Dirichlet import. The branch bit
    comes from OFFERING the bare push of l -- a move the machine never makes --
    and asking the same law whether that offer is admissible.
    """
    PR = {"x": COUNTERS[0], "y": COUNTERS[1]}
    state = dict((p, 1) for p in COUNTERS)
    inadmissible, biggest, probes = 0, 0, 0

    def move(new, q):
        nonlocal state, inadmissible, biggest
        if lam_vec(new) == lam_vec(state):
            inadmissible += 1
        state, biggest = new, max(biggest, q)

    for _ in range(x0):
        move(*growth_inc(state, PR["x"], COUNTERS))
    pc, trace = sorted(program)[0], []
    for _ in range(budget):
        if pc in ("HALT", "LOOP"):
            return pc, trace, inadmissible, probes, biggest
        ins = program[pc]
        if ins[0] == "DEC":
            _, c, nz, z = ins
            l = PR[c]
            guard = lam_vec(push(state, l)) != lam_vec(state)  # offered, not made
            probes += 1
            move(*padded_dec(state, l, COUNTERS))
            pc = z if guard else nz
        else:
            _, c, nxt = ins
            move(*growth_inc(state, PR[c], COUNTERS))
            pc = nxt
        trace.append((pc, delta_vec(state, PR["x"]), delta_vec(state, PR["y"])))
    return "BUDGET", trace, inadmissible, probes, biggest


def hand_run(x0, program=PARITY, budget=200):
    """The HAND-DRIVEN machine under TRANSPARENCY: bare pushes, branch on lambda.

    The contrast that decides what the hosting axis is worth. Here the moves
    come from the hand irrespective of admissibility and the law supplies only
    the probe, so a SIGHTED law drives the branch whether or not its admissible
    set could carry the run. Transparency is the law on purpose: it is the one
    that cannot host the machine. Returns the count of moves MADE it rejects -- the
    price of dropping autonomy, paid in inadmissible moves.
    """
    PR = {"x": COUNTERS[0], "y": COUNTERS[1]}
    state = dict((p, 1) for p in COUNTERS)
    inadmissible = 0

    def move(new):
        nonlocal state, inadmissible
        if lam_vec(new) != lam_vec(state):   # transparency admits frozen lambda
            inadmissible += 1
        state = new

    for _ in range(x0):
        move(growth_inc(state, PR["x"], COUNTERS)[0])
    pc, trace = sorted(program)[0], []
    for _ in range(budget):
        if pc in ("HALT", "LOOP"):
            return pc, trace, inadmissible
        ins = program[pc]
        if ins[0] == "DEC":
            _, c, nz, z = ins
            l = PR[c]
            nxt = push(state, l)                  # the BARE push, made not offered
            transparent = lam_vec(nxt) == lam_vec(state)
            move(nxt)
            pc = nz if transparent else z
        else:
            _, c, nxtlab = ins
            move(growth_inc(state, PR[c], COUNTERS)[0])
            pc = nxtlab
        trace.append((pc, delta_vec(state, PR["x"]), delta_vec(state, PR["y"])))
    return "BUDGET", trace, inadmissible


def s6_autonomous_run():
    print("S6  THE AUTONOMOUS RUN -- every move MADE is admissible")
    ok = True
    total_bad, total_probes, biggest = 0, 0, 0
    for name, program, span in (("halts-iff-even", PARITY, range(0, 7)),
                                ("transfer x to y", TRANSFER, range(0, 6)),
                                ("roundtrip x->y->x", ROUNDTRIP, range(0, 5))):
        fates = []
        for x0 in span:
            ref_fate, ref_trace = reference_run(x0, program)
            got_fate, got_trace, bad, probes, big = autonomous_run(x0, program)
            total_bad += bad
            total_probes += probes
            biggest = max(biggest, big)
            fates.append(got_fate)
            ok &= check(ref_fate == got_fate and ref_trace == got_trace,
                        "S6 %s x0=%d: reference %s, autonomous %s"
                        % (name, x0, ref_fate, got_fate))
        print("    %-18s x0=%d..%d: %s"
              % (name, span[0], span[-1], " ".join(fates)))
    ok &= check(total_bad == 0,
                "S6 %d moves made were inadmissible under the dynamics law"
                % total_bad)
    print("    moves made that the dynamics law rejects: %d" % total_bad)
    print("    guard probes on moves never made: %d;  largest import: %.3g"
          % (total_probes, biggest))
    print("    -- so the machine is law-autonomous: nothing inadmissible is")
    print("       ever injected, and the probe still reads the guard.")
    # THE CONTRAST that says what the hosting axis is actually worth. Drop
    # autonomy and the HAND makes the moves while the law supplies only the
    # probe -- and then a sighted law that hosts NOTHING drives the machine
    # perfectly well, because its admissible set is never consulted.
    print("    the same programs HAND-DRIVEN, branch read from the TRANSPARENCY")
    print("    probe -- a law whose own admissible set hosts no increment:")
    hand_bad = 0
    for name, program, span in (("halts-iff-even", PARITY, range(0, 7)),
                                ("transfer x to y", TRANSFER, range(0, 6)),
                                ("roundtrip x->y->x", ROUNDTRIP, range(0, 5))):
        fates = []
        for x0 in span:
            ref_fate, ref_trace = reference_run(x0, program)
            got_fate, got_trace, bad = hand_run(x0, program)
            hand_bad += bad
            fates.append(got_fate)
            ok &= check(ref_fate == got_fate and ref_trace == got_trace,
                        "S6 hand-driven %s x0=%d: reference %s, got %s"
                        % (name, x0, ref_fate, got_fate))
        print("      %-18s x0=%d..%d: %s"
              % (name, span[0], span[-1], " ".join(fates)))
    ok &= check(hand_bad > 0,
                "S6 the hand-driven run makes moves transparency rejects")
    print("      moves made that the transparency law rejects: %d" % hand_bad)
    print("    -- so SIGHTEDNESS alone buys universality once a hand supplies")
    print("       the moves; hosting is the price of doing without one.\n")
    return ok


# --------------------------------------------------------- S7  the hosting table

def s7_hosting_table():
    print("S7  THE HOSTING TABLE -- which admissible sets can carry the machine")
    ok = True
    battery = [15, 45, 105, 225, 315, 855, 1995, 2565, 5985, 45045]
    lowered = tried = 0
    for N in battery:
        for l in (3, 5, 7):
            if N % l:
                continue
            base = delta(N, l)
            for m in range(2, 200):
                if gcd(N, m) != 1:
                    continue
                tried += 1
                if delta_prod(N, m, l) < base:
                    lowered += 1
    ok &= check(lowered == 0,
                "S7 a coprime move lowered a seated slack %d times" % lowered)
    print("    coprime moves lowering a seated counter's slack: %d of %d"
          % (lowered, tried))
    print("      -- so D-IND and D-SEMI host no decrement at all")

    frozen_raise = raised = 0
    for N in battery:
        for l in (3, 5, 7, 11):
            base = delta(N, l)
            for m in range(2, 200):
                if delta_prod(N, m, l) > base:
                    raised += 1
                    if lam_prod(N, m) == lam(N):
                        frozen_raise += 1
    ok &= check(frozen_raise == 0,
                "S7 %d moves raised a slack with lambda frozen" % frozen_raise)
    print("    slack-raising moves with lambda frozen: %d of %d slack-raising"
          " moves" % (frozen_raise, raised))
    print("      -- so D-TRA hosts no increment")

    # and by the transparency wall (S4) D-TRA's admissible set from N is the
    # divisors of V(N) -- FINITE, so its whole reachable set is the divisors of
    # one wall and no counter in it can grow without bound.
    print("    N        headroom V(N)   admissible moves   reachable states")
    for N in (15, 45, 105, 225, 315, 855):
        V = headroom(N)
        ok &= check(V >= 1 and wall(lam(N)) % N == 0,
                    "S7 the wall is a multiple of the state at %d" % N)
        print("    %-8d %13d   %16d   %16d"
              % (N, V, len(divisors(V)) - 1, len(divisors(V))))
    print("      -- a finite reachable set cannot hold an unbounded counter")

    state, mem_ok = dict((p, 1) for p in COUNTERS), True
    for _ in range(3):
        before = state
        state, q = padded_dec(state, 3, COUNTERS)
        mem_ok &= q not in before        # a new prime, so omega grows
    ok &= check(mem_ok, "S7 the padded decrement adds a new prime every time")
    print("    the padded decrement adds a new prime every time: %s"
          % ("yes" if mem_ok else "NO"))
    print("      -- so D-MEM hosts both instructions, and S3 says it cannot read")
    print()
    print("    each law in the first column hosts the OTHER instruction:")
    print("      the coprime import is what D-IND and D-SEMI admit, and the")
    print("      transparent push IS the decrement (a SEATED l's push is")
    print("      transparent iff delta_l >= 1)")
    print()
    print("    THE SQUARE               hosts one            hosts both")
    print("      blind                  D-IND, D-SEMI        D-MEM")
    print("      sighted                D-TRA                D-DYN == D-ORD")
    print("    hand-driven, universality = the SIGHTED row (S6);")
    print("    law-autonomous, universality = the sighted-and-hosting CORNER.")
    print()
    return ok


# ------------------------------------------------------------------- driver

def main():
    print("explore_demand_reading.py -- WHICH DEMAND LAWS CAN READ, AND WHICH RUN?")
    print("=" * 72)
    if not s1_positive_control():
        print("POSITIVE CONTROL FAILED -- no verdict read.")
        return 1
    s2_order_identity()
    s3_reading_table()
    s4_partition_instrument()
    s5_padded_decrement()
    s6_autonomous_run()
    s7_hosting_table()
    print("=" * 72)
    if FAIL:
        print("FAILURES (%d):" % len(FAIL))
        for f in FAIL:
            print("  " + f)
        return 1
    print("all checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
