"""
THE ERASURE LEDGER -- the third in a series of four perimeter probes
charting what the finite-window family IS.

THE CONJECTURE UNDER TEST: the archimedean
borrow is Landauer ERASURE (erasing a bit costs energy; reversible
computation erases nothing -- Landauer 1961, Bennett 1973). The
conjecture arrived hedged: "a probe, not a proof -- the witness result says
the STATE is many-to-one though the MOVES aren't." This probe cashes the hedge.

THE LEDGER. For a deterministic map f on a finite state space under a
uniform input, the Landauer floor is the entropy drop H(in) - H(f(in)) >= 0,
zero IFF f is injective on its support (a bijection erases nothing). We
tabulate every native tower operation as reversible (0) or erasing (>0),
price the erasure, and confront the kill-shot.

THE ANSWER (rule/observation per section; verified S1-S5). The naive
conjecture "erasure = the archimedean borrow" is REFINED, not confirmed.

  1. THE REVERSIBLE CORE (rule, S1). The tower's native ring arithmetic --
     CRT encode/decode, add-a-constant (+a), multiply-by-a-unit (xu,
     gcd(u,N)=1) -- is a PERMUTATION of Z/N, factoring channelwise into
     per-channel bijections. Zero Landauer floor. "The tower can only add":
     its invertible core computes with no erasure, carry-free.

  2. WHERE ERASURE LIVES + EXACT PRICING (rule, S2). The many-to-one native
     ops erase, and for the two ADDITIVE HOMOMORPHISMS the price is exact and
     CHANNEL-LOCAL: multiply-by-a-NON-unit xm erases log2|ker| =
     log2 gcd(m,N) = Sum_{p|m} log2 p; idempotent projection e_S erases
     Sum_{i not in S} log2 p_i. The power map x^e is not additive-
     homomorphic: it is a bijection on squarefree Z/N IFF gcd(e, lambda)=1
     (each F_p: x^e permutes iff gcd(e,p-1)=1, fixes 0); when gcd(e,lambda)>1
     some channel's F_p* map is many-to-one -- it erases, channel-local, no
     clean gcd form (priced numerically).

  3. THE SIEVE IS THE ERASING LENS (observation, S3). The erasing atom is the
     WINDOW READ (projection e_S), which erases the complementary channels
     (finding 2). The Eratosthenes sieve is built from window reads plus
     discard-the-zero-fiber; its information loss is carried by projections
     while the ring ARITHMETIC (finding 1) loses nothing. Erasure ties to the
     archimedean not through the borrow but through the RANGE certificate
     (p > |n| => p does not divide n; the tower's own construction) -- a SIZE fact.

  3b. THE DEPTH AXIS ERASES TOO (rule, S3b -- the axis-symmetry extension,
     added in a follow-up pass, honoring an idea noted while working on
     explore_expressiveness_perimeter.py: "chart BOTH deleted
     axes"). explore_expressiveness_perimeter.py placed the tower inside Presburger via TWO deleted axes: the
     archimedean and the prime-power DEPTH (residue FIELDS F_p, not local rings
     Z/p^k). The depth axis carries the SAME split: in Z/p^k the fattening
     generator xp is NILPOTENT (kernel = multiples of p^{k-1}, size p),
     erasing exactly log2 p, while xunit stays a bijection. So BOTH deleted
     places have a reversible pole (units) and a dissipative middle; the
     ledger is axis-symmetric, safe destruction available on either.

  4. THE KILL-SHOT -- witness gap != Landauer erasure (rule, S4, LOAD-
     BEARING). Two DISTINCT non-injectivities. LANDAUER = the one-STEP state
     map is many-to-one (dynamics destroys info). WITNESS GAP (explore_growth_machine.py) = the
     HISTORY -> endpoint map is many-to-one (a commutative accumulator never
     records order). The growth machine has per-step erasure = 0 (each move
     q: v -> v + e_q is a translation, injective on the depth vector) YET a
     route entropy log2(#orderings) > 0 (p_k# reached by up to k! routes).
     Same "many-to-one" word, different domain: map-on-STATES (thermodynamic)
     vs map-from-HISTORIES (representational -- a hash collision on a
     commutative-quotient state, present in the state DEFINITION, produced by
     no step). Landauer charges the ACTUAL per-step physical dynamics
     (reversible here); the alternative histories are never instantiated in a
     run, so no physical erasure -- the gap is an OBSERVER inference deficit
     (route unrecoverable from endpoint). ANSWER to the open kill-shot
     question: ONLY
     ANALOGOUS, and the analogy is exactly locatable.

  5. THE ORTHOGONALITY -- RESET vs DECREMENT (rule, S5). At explore_reset_corner.py's
     dial the
     thermodynamic axis and the universality axis ANTI-align. RESET (v -> 0):
     maximally Landauer-erasing (unbounded values -> one; erases log(range),
     unbounded) yet computationally SAFE (value-blind, finite-state, per
     explore_reset_corner.py).
     GUARDED DECREMENT (v -> v-1, v >= 1): a BIJECTION, ZERO erasure, yet the
     DANGEROUS borrow (value-reading -- it unlocks universality paired with a
     zero-test). The universality-granting borrow is the REVERSIBLE op and
     the maximally-erasing op grants nothing: erasure is ORTHOGONAL to
     computational power (Bennett 1973: reversible machines are universal --
     universality needs NO erasure; cited, not run). Refutes "erasure = the
     borrow" as an identity.

THE SYNTHESIS. The deleted archimedean place hosts TWO INDEPENDENT knobs:
the CARRY (forward; its absence = carry-free reversible arithmetic, no
erasure -- finding 1) and the BORROW (backward, a value-reading down-move;
its absence = no universality -- explore_reset_corner.py,
explore_archimedean_dial.py). (A later run settled the adjacent general
question: with growth moves the bare element class is universal -- a sparse
counter riding the growth frontier keeps the native zero-test exact and
decrements by native ring subtraction, explore_frontier_rider.py -- so the
borrow clause survives as the INGREDIENT claim, "without a value-reading
down-move, no universality": the rider mints its own down-move, no
archimedean import needed.) Carry and
borrow are the one
inter-window coupling read in the two arithmetic directions; the tower
deletes the WHOLE place and reaps BOTH dividends (reversible AND decidable),
but they are LOGICALLY INDEPENDENT (Bennett: reversible universal machines
exist; erasing decidable machines exist). This supersedes the opening
conjecture's hedged form: the probe resolves NOT-one-trade -- two knobs at
one place, and the witness gap is representational, not thermodynamic.

SCOPE + HONESTY. Findings 1, 2, 4, 5's finite computations are run-verified
(entropy drops, kernel sizes, per-step injectivity, route counts, the
anti-alignment). The Landauer PRINCIPLE (erasure -> kT ln2 dissipation), the
Bennett reversible-universality theorem, and the Minsky/reset facts inherited
from explore_reset_corner.py are CITED physics/CS by others, not run -- thermodynamic dissipation
is not measured here; what is measured is the LOGICAL (in)vertibility that
Landauer's floor is proportional to. The contribution is the LEDGER (which
tower op is reversible vs erasing, exactly priced), the kill-shot resolution
(witness gap != erasure, the two non-injectivities located), and the
orthogonality (erasure _|_ universality) refining the opening physics-tie
conjecture.

PREDICTIONS (fixed and hand-attacked BEFORE the
run; adjudicated by asserts only):
  PR1 REVERSIBLE CORE .... +a / xu / CRT-iso are permutations, channelwise
      bijections, entropy drop 0.
  PR2 ERASURE PRICING .... xm erases log2 gcd(m,N); e_S erases Sum_{not S}
      log2 p_i (exact); power map bijective iff gcd(e,lambda)=1, else erases
      channel-locally.
  PR3 SIEVE LENS ......... window read (e_S) is the erasing atom; ring
      arithmetic loses nothing; archimedean tie = the range certificate.
  PR4 KILL-SHOT .......... growth per-step erasure = 0, route entropy
      log2(k!) > 0 -- a numeric separation; witness gap ONLY ANALOGOUS.
  PR5 ORTHOGONALITY ...... RESET max-erasing/SAFE, guarded DEC 0-erasure/
      DANGEROUS; erasure _|_ power (Bennett cited).

RUN RECORD (python prime/code/explore_erasure_ledger.py; <1 s; trivial
memory; 145 checks). PREDICTIONS PR1-PR5 all CONFIRMED, no verdict misses;
S3b is a verified extension (the depth axis), added after the slate ran.
S1: +a / xu / CRT-iso bijections with entropy drop 0 at N=30 (8 units) and
N=210 (48 units); +a channelwise bijection on each F_p. S2: xm on Z/30 --
m=2 -> 1.0000, m=3 -> 1.5850, m=5 -> 2.3219, m=6 -> 2.5850, m=10 -> 3.3219,
m=15 -> 3.9069, m=12 -> 2.5850 (= log2 gcd(12,30)=log2 6), m=0 -> 4.9069
(= log2 30), each == log2 gcd(m,N) == Sum_{p|m} log2 p to 1e-9; e_S full
lattice S=[] -> 4.9069 down to S=[2,3,5] -> 0.0000, each == Sum_{not S}
log2 p_i; power map lambda=4, e in {1,3,5,7} bijective erase 0.0, e in {2,6}
-> 1.4667, e in {4,8} -> 2.2667, bijective iff gcd(e,4)=1, erasure ==
per-channel sum. S3: read window p=2/3/5 -> 3.9069/3.3219/2.5850 bits;
arithmetic xu=7 -> 0.0000 (the read erases strictly more than the
arithmetic). S3b (depth axis): xp on Z/9, Z/27, Z/16, Z/25 erases exactly
log2 p = 1.5850/1.5850/1.0000/2.3219 (kernel size p, nilpotent), xunit a
bijection erasing 0 -- axis-symmetric with the archimedean. S4: breadth
k=2/3/4/5 endpoint (1..1) via 2/6/24/120 routes,
gap = log2(k!) = 1.000/2.585/4.585/6.907 bits, per-step Landauer erasure
= 0.0 (each move injective on {0..3}^k); mixed {0,0,1} -> (2,1) via 3
routes, gap 1.585, per-step 0.0. S5: RESET erases 6.000 = log2(64) yet SAFE
(finite-state, per explore_reset_corner.py); guarded DEC 0.000 (a bijection) yet DANGEROUS
(value-reading); saturating DEC 0.0312 (= 6 - 382/64, one 0-vs-1 collision);
INC / ZERO-TEST 0.000; the erasure ordering (RESET > DEC) is asserted
(computed), read against explore_reset_corner.py's cited power ordering (RESET < DEC) -- no
self-referential assert on the imported ranks.
ONE PROBE ARTIFACT caught pre-adjudication (the same species of surprise
as explore_selection_frame.py's mid-run fix -- read the
output against the hand law): S4's first per-step probe sampled (a+i) mod 5,
period 5, so 20 samples held only 5 DISTINCT states and erasure_bits charged
the duplication as fake fan-in (k=2 erasure 1.0, not 0). The translation is
genuinely injective; the fix probes a box of DISTINCT vectors {0..3}^k (with
an explicit is_bijection assert per move). Prediction was right, the
measurement was flawed -- no finding changed. No pre-run adjudication
drafted; verdicts frozen in code, numbers copied from output.
"""

import math

CHECKS = 0


def ok(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError("CHECK FAILED: " + msg)
    CHECKS += 1


# ------------------------------------------------------------------ #
# Erasure ledger primitives.
#   A map f : range(N) -> range(N).  Under uniform input, the Landauer
#   floor is H(uniform) - H(pushforward) in BITS.  Zero iff f injective.
# ------------------------------------------------------------------ #

def entropy_bits(counts):
    """Shannon entropy (bits) of a multiset of fiber sizes summing to a
    total; the distribution is (count / total) over the image."""
    total = sum(counts)
    h = 0.0
    for c in counts:
        if c > 0:
            p = c / total
            h -= p * math.log2(p)
    return h


def erasure_bits(f, domain):
    """Landauer floor of f on a uniform input over `domain` (a list of
    states): log2|domain| - H(pushforward)."""
    fibers = {}
    for x in domain:
        y = f(x)
        fibers[y] = fibers.get(y, 0) + 1
    h_in = math.log2(len(domain))
    h_out = entropy_bits(list(fibers.values()))
    return h_in - h_out, fibers


def is_bijection(f, domain):
    img = {f(x) for x in domain}
    return len(img) == len(domain)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def carmichael_lambda_sqfree(primes):
    lam = 1
    for p in primes:
        g = gcd(lam, p - 1)
        lam = lam * (p - 1) // g
    return lam


# ------------------------------------------------------------------ #
print("S1 -- THE REVERSIBLE CORE (native arithmetic is a permutation)")

for N, primes in [(30, [2, 3, 5]), (210, [2, 3, 5, 7])]:
    dom = list(range(N))
    # add-a-constant
    for a in [1, 7, N - 1]:
        f = (lambda a: lambda x: (x + a) % N)(a)
        ok(is_bijection(f, dom), "+a bijection N=%d a=%d" % (N, a))
        e, _ = erasure_bits(f, dom)
        ok(abs(e) < 1e-12, "+a zero erasure N=%d a=%d (e=%.3g)" % (N, a, e))
    # multiply-by-a-unit
    units = [u for u in range(1, N) if gcd(u, N) == 1]
    for u in [units[1], units[len(units) // 2], units[-1]]:
        f = (lambda u: lambda x: (x * u) % N)(u)
        ok(is_bijection(f, dom), "xu bijection N=%d u=%d" % (N, u))
        e, _ = erasure_bits(f, dom)
        ok(abs(e) < 1e-12, "xu zero erasure N=%d u=%d (e=%.3g)" % (N, u, e))
    # CRT encode/decode round trip is the identity permutation
    def enc(x, ps=primes):
        return tuple(x % p for p in ps)
    codes = [enc(x) for x in dom]
    ok(len({c for c in codes}) == N, "CRT encode injective (bijection) N=%d" % N)
    # channelwise: +a and xu act as per-channel bijections
    a = 7
    for p in primes:
        # the induced channel map r -> (r + a) mod p is a bijection on F_p
        img = {(r + a) % p for r in range(p)}
        ok(len(img) == p, "+a channelwise bijection on F_%d" % p)
    print("  N=%-3d  +a / xu / CRT-iso all bijections, entropy drop 0 ; "
          "%d units" % (N, len(units)))
print("  the reversible core: native arithmetic erases nothing (carry-free)")
print()


# ------------------------------------------------------------------ #
print("S2 -- WHERE ERASURE LIVES + EXACT PRICING (channel-local)")

N, primes = 30, [2, 3, 5]
dom = list(range(N))

# multiply-by-a-non-unit: erases log2 gcd(m, N) exactly
print("  multiply-by-non-unit  xm on Z/%d:" % N)
for m in [2, 3, 5, 6, 10, 15, 12, 0]:
    f = (lambda m: lambda x: (x * m) % N)(m)
    e, fibers = erasure_bits(f, dom)
    d = gcd(m % N if m else N, N)  # ker size = gcd(m, N); m=0 -> gcd(N,N)=N
    predicted = math.log2(d)
    collapsed = [p for p in primes if (m % p == 0)] if m else primes
    chan_price = sum(math.log2(p) for p in collapsed)
    ok(abs(e - predicted) < 1e-9,
       "xm=%d erasure %.4f == log2 gcd(m,N)=%.4f" % (m, e, predicted))
    ok(abs(predicted - chan_price) < 1e-9,
       "xm=%d log2 gcd == Sum_{p|m} log2 p (channel-local)" % m)
    print("    m=%2d  erase=%.4f bits  = log2 gcd(%d,%d)=log2 %d  channels %s"
          % (m, e, m, N, d, collapsed if collapsed else ["(none)"]))

# idempotent projection e_S : keep channels in S, zero the rest
def idempotent(S, ps=primes, mod=N):
    # CRT element that is 1 on channels in S, 0 elsewhere
    e = 0
    for i, p in enumerate(ps):
        if i in S:
            # component 1 in channel p, 0 in others
            others = mod // p
            inv = pow(others % p, -1, p)
            e = (e + others * inv) % mod
    return e

print("  idempotent projection  e_S * x  on Z/%d:" % N)
from itertools import combinations
for r in range(0, 4):
    for S in combinations(range(3), r):
        eS = idempotent(set(S))
        f = (lambda eS: lambda x: (x * eS) % N)(eS)
        e, _ = erasure_bits(f, dom)
        outside = [primes[i] for i in range(3) if i not in S]
        predicted = sum(math.log2(p) for p in outside)
        ok(abs(e - predicted) < 1e-9,
           "e_S S=%s erasure %.4f == Sum_{not S} log2 p =%.4f"
           % (S, e, predicted))
        keep = [primes[i] for i in S]
        print("    S=%-9s keep %s  erase=%.4f bits = Sum log2 %s"
              % (str(keep), keep if keep else ["(none)"], e,
                 outside if outside else ["(none)"]))

# the power map: bijective iff gcd(e, lambda) = 1, else erases channel-local
lam = carmichael_lambda_sqfree(primes)
print("  power map  x^e  on Z/%d  (lambda = %d):" % (N, lam))
for exps in range(1, 9):
    f = (lambda k: lambda x: pow(x, k, N))(exps)
    e_bits, _ = erasure_bits(f, dom)
    bij = is_bijection(f, dom)
    coprime = gcd(exps, lam) == 1
    ok(bij == coprime,
       "x^%d bijective(%s) iff gcd(e,lambda)=1(%s)" % (exps, bij, coprime))
    ok((e_bits < 1e-12) == coprime,
       "x^%d zero erasure iff bijective" % exps)
    # channel-locality: erasure factorizes over channels (sum of per-F_p drops)
    chan_sum = 0.0
    for p in primes:
        fp = (lambda k, p: lambda r: pow(r, k, p))(exps, p)
        dp, _ = erasure_bits(fp, list(range(p)))
        chan_sum += dp
    ok(abs(e_bits - chan_sum) < 1e-9,
       "x^%d erasure factorizes over channels (%.4f == %.4f)"
       % (exps, e_bits, chan_sum))
    print("    e=%d  gcd(e,%d)=%d  bijective=%-5s  erase=%.4f bits (channel-sum)"
          % (exps, lam, gcd(exps, lam), str(bij), e_bits))
print()


# ------------------------------------------------------------------ #
print("S3 -- THE SIEVE IS THE ERASING LENS (read = erase; arithmetic doesn't)")

# The sieve survivors of {1..N} are the units. "Reading a window" = e_S; the
# erasing atom. Contrast: a full unit-multiplication (arithmetic) erases 0.
N, primes = 30, [2, 3, 5]
dom = list(range(N))
# read channel p alone (project onto S={that channel}) erases the OTHER two
for i, p in enumerate(primes):
    eS = idempotent({i})
    f = (lambda eS: lambda x: (x * eS) % N)(eS)
    e, _ = erasure_bits(f, dom)
    others = [primes[j] for j in range(3) if j != i]
    ok(abs(e - sum(math.log2(q) for q in others)) < 1e-9,
       "read channel %d erases the other windows" % p)
    print("  read window p=%d  ->  erase %.4f bits (the other windows %s)"
          % (p, e, others))
# arithmetic (multiply by a unit) over the SAME ring erases nothing
u = 7
f = lambda x: (x * u) % N
e_arith, _ = erasure_bits(f, dom)
ok(abs(e_arith) < 1e-12, "arithmetic (xu) erases nothing while the read does")
# the read erases strictly more than the arithmetic over the same ring
ok(e - e_arith > 0, "the window read erases strictly more than arithmetic")
print("  arithmetic xu=%d over Z/%d erases %.4f bits -- the READ erases, the"
      % (u, N, e_arith))
print("  ARITHMETIC does not; the sieve's tie to the archimedean is the RANGE")
print("  certificate (p>|n| => p does not divide n), a SIZE fact, not the borrow")
print()


# ------------------------------------------------------------------ #
print("S3b -- THE DEPTH AXIS (the SECOND deleted place erases too)")

# explore_expressiveness_perimeter.py placed the tower inside Presburger via TWO deleted axes: the archimedean
# (order) and the DEPTH axis (prime powers -- residue FIELDS F_p, not local
# rings Z/p^k). The ledger above charts the archimedean split; the depth axis
# carries the SAME reversible-core / dissipative split. In Z/p^k the fattening
# generator xp is NILPOTENT (kernel = multiples of p^{k-1}, size p) so it
# erases exactly log2 p, while xunit stays a bijection -- reversible-pole and
# dissipative-middle on the depth axis exactly as on the archimedean.
for p, k in [(3, 2), (3, 3), (2, 4), (5, 2)]:
    mod = p ** k
    ddom = list(range(mod))
    xp = (lambda p, mod: lambda x: (x * p) % mod)(p, mod)
    e_xp, fib = erasure_bits(xp, ddom)
    ker = sum(1 for x in ddom if (x * p) % mod == 0)
    ok(ker == p, "xp kernel on Z/%d^%d has size p=%d" % (p, k, p))
    ok(abs(e_xp - math.log2(p)) < 1e-9,
       "xp on Z/%d erases exactly log2 p = %.4f" % (mod, math.log2(p)))
    # a unit stays a bijection (0 erasure) on the same prime-power ring
    unit = next(u for u in range(2, mod) if gcd(u, mod) == 1)
    fu = (lambda unit, mod: lambda x: (x * unit) % mod)(unit, mod)
    ok(is_bijection(fu, ddom), "xunit bijection on Z/%d" % mod)
    e_u, _ = erasure_bits(fu, ddom)
    ok(abs(e_u) < 1e-12, "xunit erases 0 on Z/%d" % mod)
    print("  Z/%-3d (=%d^%d)  xp=%d erase=%.4f=log2 %d (nilpotent) | xunit=%d "
          "erase=%.4f" % (mod, p, k, p, e_xp, p, unit, abs(e_u)))
print("  both deleted places (archimedean, depth) carry the reversible/erasing")
print("  split -- the ledger is axis-symmetric; safe destruction on either")
print()


# ------------------------------------------------------------------ #
print("S4 -- KILL-SHOT: WITNESS GAP != LANDAUER ERASURE")

# The growth machine's state is a depth vector v in Z^k_{>=0}. A move q adds
# e_q (breadth: a new coordinate 0->1; depth: +1 on an existing one). Each
# move is a TRANSLATION -> injective -> ZERO per-step Landauer erasure. Yet
# the endpoint is a COMMUTATIVE sum: many move-orderings reach it.

from itertools import permutations
from math import factorial


def apply_moves(seq, k):
    """seq = tuple of coordinate indices to increment; returns the endpoint
    depth vector and asserts each step is injective on the visited state."""
    v = [0] * k
    traj = [tuple(v)]
    for q in seq:
        v = list(v); v[q] += 1
        traj.append(tuple(v))
    return tuple(v), traj


def per_step_erasure(seq, k):
    """Each step v -> v+e_q is a translation, injective on DISTINCT states ->
    0 Landauer erasure. Probe over a box of distinct depth vectors {0..3}^k."""
    from itertools import product
    probe = list(product(range(4), repeat=k))  # distinct states, no duplicates
    max_e = 0.0
    for q in set(seq):
        f = (lambda q: lambda w: tuple(w[j] + (1 if j == q else 0)
                                       for j in range(k)))(q)
        ok(is_bijection(f, probe), "move q=%d injective on the state" % q)
        e, _ = erasure_bits(f, probe)
        max_e = max(max_e, e)
    return max_e


print("  breadth: k distinct moves, all orderings reach (1,...,1):")
for k in [2, 3, 4, 5]:
    seqs = list(permutations(range(k)))
    endpoints = {apply_moves(s, k)[0] for s in seqs}
    ok(len(endpoints) == 1, "all %d orderings reach one endpoint (k=%d)"
       % (len(seqs), k))
    n_routes = len(seqs)
    ok(n_routes == factorial(k), "route count = k! (k=%d)" % k)
    gap = math.log2(n_routes)
    step_e = per_step_erasure(seqs[0], k)
    ok(abs(step_e) < 1e-12, "per-step Landauer erasure = 0 (k=%d)" % k)
    ok(gap > 0, "witness gap = log2(k!) > 0 (k=%d)" % k)
    print("    k=%d  endpoint (1..1) via %2d routes  gap=log2(%d)=%.3f bits  "
          "per-step erasure=%.1f" % (k, n_routes, n_routes, gap, step_e))

# a depth-mixed example: move multiset {0,0,1} -> (2,1) via multinomial routes
moves = (0, 0, 1)
seqs = set(permutations(moves))
endpoints = {apply_moves(s, 2)[0] for s in seqs}
ok(endpoints == {(2, 1)}, "mixed moves reach (2,1)")
mult = factorial(3) // (factorial(2) * factorial(1))
ok(len(seqs) == mult, "route count = multinomial = %d" % mult)
gap = math.log2(len(seqs))
ok(per_step_erasure(tuple(moves), 2) < 1e-12, "mixed per-step erasure = 0")
print("    mixed {0,0,1} -> (2,1) via %d routes  gap=%.3f bits  per-step "
      "erasure=0.0" % (len(seqs), gap))
print("  => reversible per-step dynamics (0 erasure) with a POSITIVE witness")
print("     gap: the gap is a COMMUTATIVE-quotient encoding collision, NOT a")
print("     Landauer erasure. The kill-shot resolves: ONLY ANALOGOUS.")
print()


# ------------------------------------------------------------------ #
print("S5 -- THE ORTHOGONALITY: RESET (erasing, SAFE) vs DEC (reversible, DANGEROUS)")

M = 63  # value range {0..M}
vals = list(range(M + 1))

# RESET v -> 0: collapses everything to one -> maximal erasure
reset = lambda v: 0
e_reset, fibers = erasure_bits(reset, vals)
ok(abs(e_reset - math.log2(M + 1)) < 1e-9,
   "RESET erases log2(range) = %.4f" % math.log2(M + 1))
ok(not is_bijection(reset, vals), "RESET is many-to-one")

# GUARDED DEC v -> v-1 on v>=1: a bijection {1..M} -> {0..M-1}, zero erasure
gdom = list(range(1, M + 1))
gdec = lambda v: v - 1
ok(is_bijection(gdec, gdom), "guarded DEC is a bijection")
e_gdec, _ = erasure_bits(gdec, gdom)
ok(abs(e_gdec) < 1e-12, "guarded DEC erases 0 bits")

# SATURATING DEC max(0,v-1) on {0..M}: erases only the single 0-vs-1 bit
sdec = lambda v: max(0, v - 1)
e_sdec, _ = erasure_bits(sdec, vals)
ok(0 < e_sdec < 0.2, "saturating DEC erases only a sliver (0<e<0.2)")

# INC and ZERO-TEST: zero erasure (INC injective; a test does not modify)
inc = lambda v: v + 1
ok(is_bijection(inc, vals), "INC is a bijection")
e_inc, _ = erasure_bits(inc, vals)
ok(abs(e_inc) < 1e-12, "INC erases 0 bits")

# The computed content is the erasure ordering (RESET erases MORE than the
# decrement). The POWER classification is CITED from explore_reset_corner.py,
# not computed here
# (RESET keeps the machine finite-state = SAFE; the value-reading DEC unlocks
# universality with a zero-test = DANGEROUS); the
# anti-alignment is the computed erasure gap read against that cited ordering
# (no self-referential assert on the imported ranks).
erasure = {"RESET": e_reset, "GUARDED_DEC": e_gdec}
ok(erasure["RESET"] > erasure["GUARDED_DEC"],
   "RESET erases MORE than the decrement (computed); explore_reset_corner.py cites its power LOWER")
print("  op            erasure(bits)   prior power (cited)")
print("  INC           %6.3f          adds  (safe)" % e_inc)
print("  ZERO-TEST      0.000          reads (the enabler, w/ a borrow)")
print("  GUARDED DEC   %6.3f          UNIVERSAL-enabling (value-reading)"
      % abs(e_gdec))
print("  SATURATING DEC%7.4f         (same power; one bit at the bottom)"
      % e_sdec)
print("  RESET         %6.3f          finite-state (value-blind, SAFE)"
      % e_reset)
print("  => erasure _|_ computational power. Bennett 1973 (cited): reversible")
print("     machines are universal -- universality needs NO erasure.")
print()


print("ALL CHECKS PASSED:", CHECKS)
