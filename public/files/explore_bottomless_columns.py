"""
explore_bottomless_columns.py -- THE BOTTOMLESS COLUMNS (sibling of
explore_class_gap.py).

THE QUESTION: explore_class_gap.py proved the absorption profile law
IN-UNIVERSE -- over a finite atom set, a thermal element run can only
absorb once every nonprincipal atom sits at depth >= 2 -- and read the
infinite world off it only by argument: the thermal element limit would
complete exactly the nonprincipal columns, the class group read as a
partition of places into shallow (trivial class) and bottomless
(nontrivial class). That reading is the record's open edge. This rig takes
the infinite world on its own terms, where the question is not WHETHER a
run absorbs but at what RATE each column grows.

THE TRANSPLANT UNDER TEST is exactly that vocabulary: "driven to depth
>= 2" and "coprime mass -> 0" are finite-universe sentences (a finite
universe exhausts its fresh supply and absorbs). In the infinite world the
fresh supply is never empty at any finite time, so the law must be stated
as a per-column growth rate.

THE MODEL (the corpus's thermal D-IND element growth, no atom set). K a
number field, O its ring of integers, Cl its class group, beta > 1. A
state is a principal ideal s; a move is a principal ideal m carrying
weight N(m)^-beta; the move is ADMISSIBLE iff the class sequence of
gcd(m, s) is ZERO-SUM-FREE (the sensor criterion, proved --
explore_class_gap.py). One step samples the admissible moves with
probability proportional to weight and multiplies. The total mass over all
principal ideals is zeta_princ(beta) < infinity for beta > 1, so the step
is well defined without a cap; a RIG must truncate, which is why every
reading below is taken as a CAP-TO-CAP TREND and never at one cap.

THE RINGS. Z[sqrt(-5)] (h = 2, Cl = C2) is the subject; Z[i] (h = 1) is
the control the split must be EMPTY at; Q(sqrt(-23)) (h = 3, Cl = C3) is
the scope leg, where the predicate itself is looser -- over C3 a shared
P^2 is still zero-sum-free (2c =/= 0) and P^3 is a principal move.

PREDICTIONS (fixed before the engine; the paper attack is in the design
notes below, and the frozen bands are the kill criteria).

PR1 THE SHALLOW HALF. Every principal prime Q keeps e_t(Q) in {0, 1} for
    all t, in every run, over every ring. PRINTS: max_Q e_t(Q) over
    principal Q. KILL: it prints 2 or more, ever. [Frozen as stated; the
    run killed it and the mechanism it was a consequence of replaced it --
    finding 1.]
PR2 THE BOTTOMLESS HALF, AS A RATE. For a nonprincipal P the exponent
    grows LINEARLY, slope r(P) = N(P)^-beta / (1 + C_beta), where C_beta
    is the sum of N(P)^-beta over NONPRINCIPAL primes. PRINTS: the
    late-phase slope over the predicted r(P), for the three smallest
    nonprincipal primes. BAND: [0.7, 1.4]. KILL: a slope indistinguishable
    from zero at every cap, or the ratio outside the band at every cap and
    moving further out as the cap grows.
PR3 THE MECHANISM. The one-step raising probability p_t(P) does not decay,
    because the P-raising mass and the total admissible mass are both
    TAILS OF THE SAME PRIME SUM. PRINTS: min over the late phase of
    p_t(P)/r(P). BAND: > 0.3. KILL: p_t(P) falling monotonically to 0
    across the late phase at every cap.
PR4 THE CHEBOTAREV LEG. The fresh principal and fresh nonprincipal
    prime-zeta tails have ratio a(x)/b(x) -> 1. PRINTS: the ratio at
    x = 10^3 .. 10^6. BAND: |a/b - 1| < 0.1 at x = 10^6, beta = 2.
PR5 THE h = 1 CONTROL. Over Z[i] every prime is principal, so no column is
    bottomless and the state stays squarefree forever -- the sensor
    criterion's "exact iff h = 1" seen dynamically. PRINTS: max_p e_t(p)
    over ALL primes. KILL: any column reaching 2.
PR6 THE h = 3 SCOPE LEG. Over Q(sqrt(-23)) the trivial/nontrivial split
    persists -- principal entry-once, nonprincipal unbounded -- while the
    constant changes. PRINTS: the same two. KILL: a principal prime at
    depth 2, or a nonprincipal column flat over the late phase.

DESIGN NOTES (the paper attack, pre-engine).
 * The shallow half is a PROPERTY: if e_s(Q) >= 1 for principal Q then any
   move divisible by Q has [Q] = 0 inside its gcd's class sequence, whose
   one-term subsequence sums to zero. No probability enters. PR1 and PR5
   are one fact; PR5 adds that at h = 1 it applies to every prime.
 * A raising move for nonprincipal P at depth e needs gcd = P^1 exactly
   (over C2; a larger class group leaves the gcd more room).
   At e = 1 the FIXED-weight move P^{2k} is admissible and lands the
   column at depth 3; past that every raising move is P * (fresh
   nonprincipal partner), weight N(P)^-beta N(Q)^-beta. So the fresh
   NONPRINCIPAL supply is the load-bearing resource.
 * Hence the ratio, which is where the argument turns. With a(x), b(x) the
   fresh principal/nonprincipal prime-zeta tails and K the sum of
   N(P')^-beta over nonprincipal P' already in the state: numerator
   N(P)^-beta b(x), denominator a(x) + K b(x) + O(b^2) plus the
   fixed-weight P^{2k} terms. Both leading terms are tails of the same
   prime sum, so the ratio does NOT decay, and with a/b -> 1 (PR4) and
   K -> C_beta the one-step probability tends to N(P)^-beta/(1 + C_beta).
 * WHERE THE STATISTIC BLOWS UP, which is not where the derivation does.
   (i) a, b and the admissible mass all go to 0 as the menu recedes, so
   the reading is a 0/0 in the limit: read the RATIO, never the masses,
   and keep beta low enough that the cap still carries tail weight -- the
   grid is beta = 1.5 and 2.0 for that reason. (ii) EARLY the fixed-weight
   P^{2k} moves dominate the denominator and DEPRESS p_t(P): the reading
   belongs in the late phase and a whole-run slope fit would read the
   transient. (iii) A capped run absorbs by the finite-universe law, so
   every reading sits before the absorption step. (iv) Index convention,
   re-derived from the engine: e is the IDEAL exponent and P^2 raises it
   by 2, so depth 2 is reachable in one move from 0 and the depth-1
   channel is transient by construction.
 * THE CONFOUND NAMED BY ARGUMENT OWES A COUNT. "The run could consume
   fresh NONPRINCIPAL primes faster than principal ones, driving b/a to 0
   and freezing every column." The count: consuming a fresh nonprincipal
   prime needs a PARTNER (weight b(x) N^-beta), consuming a fresh
   principal prime costs one move (weight N^-beta), so the nonprincipal
   side is consumed at a rate smaller by the factor b(x). The rig measures
   a/b ALONG THE TRAJECTORY, not only over the static primes.
 * POSITIVE CONTROLS, run before any kill/survive is read: (A) the class
   map against classical representability -- every principal prime norm
   must be represented by the principal form and no nonprincipal one may
   be; (B) the h = 1 ring, where the split must be empty; (C) the
   accounting identity, the measured late-phase slope against the mean of
   the independently computed one-step probabilities over the same window.

FINDINGS (tiers per the standard naming scale; all sections assert; run
record below).

1. THE SHALLOW HALF IS A PROPERTY, AND IT IS ENTRY-ONCE IN MOVES RATHER
   THAN DEPTH <= 1 (property, proved; verified S3 over 39 runs at
   h = 1, 2, 3). If a principal prime Q has e_s(Q) >= 1, every move
   divisible by Q puts the TRIVIAL class into the gcd's class sequence,
   whose one-term subsequence sums to zero, so the move is inadmissible: a
   principal column is written by AT MOST ONE move and is frozen for all
   time after it, over any class group, with no probability entering and
   no limit taken. The record's argued half is therefore not argued at all
   on this side. What is bounded is the number of WRITES and not the
   exponent: a FRESH Q is coprime to the state, so a move carrying Q^2 is
   admissible and writes the column at depth 2 in one stroke -- 3 of 12
   runs at h = 1 do exactly that. Measured: 0 rewrites of a written
   principal column over 39 runs across the three rings. At h = 1 the law
   covers every prime, so no column is bottomless there at all -- the
   sensor criterion's "exact iff h = 1" read dynamically (PR1 and PR5's
   OBSERVABLES both falsified as frozen, PR5's claim surviving -- see the
   prediction record).

2. THE BOTTOMLESS HALF IS A RATE, AND THE RATE IS AN IDENTITY (rule in
   range, 3 caps x 2 temperatures x 5 seeds; verified S4). Past depth 1
   EVERY raising move for a nonprincipal P must carry at least one FRESH
   NONPRINCIPAL factor -- over C2 the gcd has to read P^1 exactly (any
   second prime in it is either principal, whose class sums to zero
   alone, or nonprincipal, which pairs with P to zero), so the rest of
   the move is coprime to the state and principality forces an odd count
   of nonprincipal primes in it; over a larger class group the gcd has
   more room and only the FRESH-factor conclusion carries over, the rest
   of the move still needing nonzero total class -- and the LEADING
   family is the two-prime move P * Q. (The fixed-weight P^{2k} channel is
   admissible at depths 0 and 1 only, landing the column at 2 or 3; from
   depth 2 up it is dead, checked against the engine.) Writing a, b for
   the fresh principal / nonprincipal prime-zeta tails and K for the
   nonprincipal mass already in the state, the one-step raising
   probability is
       p(P) = N(P)^-beta * b / (a + K b),
   measured against the trajectory's own a, b, K to 0.1-4.3% at cap 32000
   (p_hat/p = 0.999, 1.043, 1.003, 1.018), the error falling 3.12 -> 0.164
   -> 0.043 across caps 2000 -> 8000 -> 32000. The residue is the
   TRUNCATION and its instrument is the dry share -- the fraction of
   late-window steps with no admissible raising move at all -- which reads
   0.26-0.28 at cap 2000 for the columns above 3 (0.008 for the one above
   2, whose weight keeps a partner affordable longest) and 0.000 at every
   larger cap for all of them: a capped rig is a
   finite universe and absorbs, which is the transplant this rig was built
   to separate out.
   THE DENOMINATOR IS MEASURED AND NOT INFERRED FROM ITS OWN RATIO (S4b):
   decomposed at the end of a top-cap run, the admissible mass is 57.1%
   fresh principal primes and 41.6% the K b family, with 1.4% left in the
   fixed-weight channel and NOTHING anywhere else -- so the two families
   the derivation names carry 98.6% of it, and the ratio's agreement is
   not two errors cancelling.
   With K rising to C_beta = sum of N(P)^-beta over NONPRINCIPAL primes
   and a/b settling at rho_beta, the rate closes to within 0.2% at the
   prime above 2 and 4% at the two above 3:
       r(P) = N(P)^-beta / (rho_beta + C_beta)
   -- at beta = 2, C_beta = 0.52056 and rho = 0.641 give 0.21523 against
   the measured 0.21476 (and 0.09566 against 0.09401 at norm 3); at
   beta = 1.5, C_beta = 0.90068 and rho = 0.925 give 0.19366 against
   0.19432 (0.10541 against 0.10128 at norm 3). So every nonprincipal
   column
   grows LINEARLY in the move count, which is strictly more than the
   record's "unbounded depth": pooled slopes at the top cap 0.195, 0.115,
   0.084 (beta 1.5) and 0.221, 0.097, 0.085 (beta 2), positive at every
   cap and every seed.

3. WHAT IS PROVED, WHAT IS MEASURED, AND THE ONE LEG LEFT (synthesis).
   The limit law's SHALLOW side is now a property (finding 1). Its
   BOTTOMLESS side reduces, by the identity of finding 2, to ONE
   quantitative question: is the fresh-tail ratio rho = a/b bounded above
   along a trajectory? If it is, r(P) >= N(P)^-beta/(rho_sup + C_beta) is
   a positive constant and every nonprincipal column is bottomless with a
   linear rate; if a/b could diverge, the rate could vanish. Measured, rho
   is cap-STABLE and below the static Chebotarev value: 0.925 (beta 1.5)
   and 0.641 (beta 2) at cap 32000 against 0.875 / 0.648 at cap 8000, so
   the bound r_low = N^-beta/(1 + C_beta) <= p <= N^-beta/C_beta = r_high
   holds at every row of the top cap. Boundedness of rho is an
   OBSERVATION here and not a derivation, and it is the whole of what the
   infinite-world law now waits on.

4. THE CONFOUND NAMED BY ARGUMENT GOT ITS COUNT, AND IT POINTS THE OTHER
   WAY (observation; verified S2 + S4). The static tails are balanced --
   a(x)/b(x) = 1.0004 at x = 10^6, beta = 2 (0.9998 at beta = 1.5), the
   Chebotarev density 1/2 per class read at the prime-zeta level (PR4
   CONFIRMED). The TRAJECTORY's ratio is smaller, 0.641 at beta = 2, and
   that is the consumption asymmetry the pre-run count predicted from the
   move weights: consuming a fresh nonprincipal prime needs a PARTNER
   (weight b * N^-beta) where a principal one costs a single move (weight
   N^-beta), so the nonprincipal side is consumed more slowly and its
   fresh tail stays the fatter one. The direction matters: it RAISES the
   rate, so the frozen constant 1 + C_beta is a lower-bound denominator
   rather than the true one.

5. THE SPLIT IS ABOUT TRIVIALITY OF THE CLASS, NOT ABOUT PARITY (rule in
   range; verified S3, PR6 CONFIRMED). Over Q(sqrt(-23)) (Cl = C3) the
   predicate itself is looser -- a shared P^2 is still zero-sum-free
   (2c =/= 0) and P^3 is a principal move -- and the partition survives
   unchanged: 0 rewrites and no principal column written deeper than 1,
   max nonprincipal depth 48 over 200 steps, late slopes 0.166, 0.254,
   0.053. What C2 supplies is the
   CONSTANT, not the dichotomy.

PREDICTION RECORD. PR1 is FALSIFIED AS FROZEN and replaced by the law it
was a special case of. The frozen sentence said a principal column keeps
e_t(Q) in {0, 1} for all t, with the kill "it prints 2 or more, ever"; a
wider sweep prints 2, at h = 1, in 3 of 12 runs. The slate had read the
write-once mechanism off runs where the entering move's SQUARE happens to
be rare and had frozen the consequence it saw rather than the mechanism,
which only ever bounded the WRITES: 0 rewrites over 39 runs is the
invariant that holds, and the exponent is free. PR5's OBSERVABLE went the
same way and for the same reason -- it read "max_p e_t = 1" and killed on
"any column reaching 2", which is the h = 1 face of PR1's consequence, and
the sweep that killed PR1 killed it at exactly those 3 runs; PR5's CLAIM
survives whole, no column at h = 1 being bottomless, but it now stands on
the write-once law rather than on a level. PR4 and PR6 CONFIRMED as
frozen, observable and all. PR2 and PR3
CONFIRMED at caps 8000 and 32000 (slope/r_low in [0.828, 1.442] against
the frozen [0.7, 1.4] band, min p/r_low in [0.711, 1.080] against the
frozen 0.3) and MISSED at cap 2000 (0.360 and 0.000), the dry share
naming the reason: at that cap the late window sits inside the
truncation's own exhaustion. One refinement the slate did not carry: the
frozen constant 1 + C_beta is the STATIC Chebotarev denominator, and the
trajectory's is rho_beta + C_beta with rho_beta < 1, so the frozen
constant is a bound and not the rate (finding 4).

SLATE CORRECTIONS. (iii) is an audit correction and is marked as such;
(i) and (ii) were made before any verdict was read. (iii) The frozen
observable of PR1 also sat against what is already known one floor up: in
the FREE world a column is entered once with GEOMETRIC depths, so an
exponent pinned at 1 was never the statement to freeze -- only the number
of writes was. Reading a frozen observable against the neighbouring
statement of the same object is the cheapest tell there is, and it was
available before the run. (i) The first
rate leg fitted single-run slopes; over a 125-step window at p ~ 0.08 the
sd is 30-40% of the slope, so the readings were noise and the leg was
rebuilt to pool five seeds per cell and to report the one-step
probabilities beside the slope. (ii) The form-reduction helper failed to
terminate at b = -a (a reduced-window edge, not a finding); fixed by
normalising -a to a, which leaves b^2 and hence c unchanged.

RUN RECORD. python prime/code/explore_bottomless_columns.py: "RESULT: all
209 checks pass", 80.0 s, peak 53.1 MB under memwatch (limit 512).
Sections S1-S5 with S4b the denominator's decomposition; S3 runs 13
trajectories per ring, one tracked and twelve for the invariant. Rings:
Z[i] (h = 1), Z[sqrt(-5)] (h = 2, disc -20), Q(sqrt(-23)) (h = 3,
disc -23). Caps 2000 / 8000 / 32000 (menus 1391 /
5602 / 22453 principal moves), 250 steps, beta = 1.5 and 2.0, seeds
4242 / 90210 / 15213 / 271828 / 31337 offset by the cap; S2's static
tails over the rational primes to 10^7. Predictions PR1-PR6 fixed before
the run; outcomes above.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
import random
import time

FAIL = 0
CHECKS = 0


def ok(cond, msg=""):
    global FAIL, CHECKS
    CHECKS += 1
    if not cond:
        FAIL += 1
        print("  FAIL: %s" % msg)


# ------------------------------------------------------------------ #
# S0: the rings -- prime ideals, norms, classes
# ------------------------------------------------------------------ #

def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(2, n + 1) if s[i]]


def kronecker(a, n):
    """Kronecker symbol (a/n) for odd positive n and a any integer."""
    if n == 0:
        return 1 if a in (1, -1) else 0
    result = 1
    if n < 0:
        n = -n
        if a < 0:
            result = -result
    while n % 2 == 0:
        n //= 2
        if a % 2 == 0:
            return 0
        if a % 8 in (3, 5):
            result = -result
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def reduce_form(a, b, c):
    """Reduce a positive definite binary quadratic form."""
    while True:
        if c < a:
            a, b, c = c, -b, a
            continue
        if b > a or b <= -a:
            m = (b + a) // (2 * a)
            b2 = b - 2 * a * m
            if b2 == -a:                    # -a < b <= a is the window
                b2 = a                      # (b^2 unchanged, so c is too)
            c = (b2 * b2 - (b * b - 4 * a * c)) // (4 * a)
            b = b2
            continue
        if a == c and b < 0:
            b = -b
        return (a, b, c)


class Ring:
    """Prime ideals of an imaginary quadratic field up to a norm cap.

    Each prime ideal is (norm, class), the class an element of Z/h taken
    so that the class of a product is the SUM of classes.
    """

    def __init__(self, name, disc, h, cap):
        self.name = name
        self.disc = disc
        self.h = h
        self.cap = cap
        self.primes = []          # (norm, cls)
        rp = sieve(cap)
        for p in rp:
            ks = kronecker(disc, p) if p % 2 else self._sym2()
            if disc % p == 0:
                self.primes.append((p, self._cls_ramified(p)))
            elif ks == 1:
                for cls in self._cls_split(p):
                    self.primes.append((p, cls))
            else:
                if p * p <= cap:
                    self.primes.append((p * p, 0))
        self.primes.sort()

    def _sym2(self):
        d = self.disc % 8
        return 1 if d == 1 else (-1 if d == 5 else 0)

    def _cls_ramified(self, p):
        raise NotImplementedError

    def _cls_split(self, p):
        raise NotImplementedError


class RingC2(Ring):
    """Q(sqrt(-5)), disc -20, Cl = C2. Genus theory: a prime of norm p is
    principal iff p = x^2 + 5y^2, i.e. p = 5 or p = 1, 9 (mod 20)."""

    def _cls_ramified(self, p):
        return 0 if p == 5 else 1          # (sqrt(-5)) principal; P2 not

    def _cls_split(self, p):
        c = 0 if p % 20 in (1, 9) else 1
        return (c, c)                      # conjugates: inverse = equal


class RingC1(Ring):
    """Z[i], disc -4, h = 1."""

    def _cls_ramified(self, p):
        return 0

    def _cls_split(self, p):
        return (0, 0)


class RingC3(Ring):
    """Q(sqrt(-23)), disc -23, Cl = C3. The class of a split prime is read
    off the reduced form (p, b, (b^2+23)/(4p))."""

    REDUCED = {(1, 1, 6): 0, (2, 1, 3): 1, (2, -1, 3): 2}

    def _cls_ramified(self, p):
        return 0

    def _cls_split(self, p):
        out = []
        for b in range(1, 2 * p, 2):
            if (b * b + 23) % (4 * p) == 0:
                c = (b * b + 23) // (4 * p)
                out.append(self.REDUCED[reduce_form(p, b, c)])
        return tuple(out)


def represented(disc, n):
    """Is n represented by the PRINCIPAL form of discriminant disc?
    -20: n = x^2 + 5y^2.  -23: 4n = (2x+y)^2 + 23y^2."""
    if disc == -20:
        y = 0
        while 5 * y * y <= n:
            r = n - 5 * y * y
            s0 = math.isqrt(r)
            if s0 * s0 == r:
                return True
            y += 1
        return False
    if disc == -23:
        y = 0
        while 23 * y * y <= 4 * n:
            r = 4 * n - 23 * y * y
            u = math.isqrt(r)
            if u * u == r and (u - y) % 2 == 0:
                return True
            y += 1
        return False
    raise ValueError(disc)


# ------------------------------------------------------------------ #
# the menu: principal ideals up to the cap, and the process
# ------------------------------------------------------------------ #

def build_menu(ring, beta):
    """All principal ideals of norm <= cap (excluding 1), as
    (mask, ((idx, exp), ...), weight, norm). Class sums to 0 mod h."""
    prs = ring.primes
    n = len(prs)
    out = []
    stack = [(0, 1, 0, 0, ())]
    while stack:
        i, norm, cls, mask, exps = stack.pop()
        if norm > 1 and cls % ring.h == 0:
            out.append((mask, exps, float(norm) ** (-beta), norm))
        for j in range(i, n):
            pn, pc = prs[j]
            if norm * pn > ring.cap:
                break
            m, e = norm * pn, 1
            while m <= ring.cap:
                stack.append((j + 1, m, cls + e * pc, mask | (1 << j),
                              exps + ((j, e),)))
                e += 1
                m *= pn
    return out


def zsf(classes, h):
    """Is the multiset of classes zero-sum-free over Z/h?"""
    if not classes:
        return True
    if len(classes) > 10:
        return False
    for mask in range(1, 1 << len(classes)):
        s = 0
        for k in range(len(classes)):
            if mask >> k & 1:
                s += classes[k]
        if s % h == 0:
            return False
    return True


def admissible(mv, st, st_mask, ring):
    """Is move mv admissible against state st (exponent dict)?"""
    mask, exps, w, norm = mv
    shared = mask & st_mask
    if not shared:
        return True
    cls = []
    for idx, e in exps:
        if shared >> idx & 1:
            k = min(e, st[idx])
            cls.extend([ring.primes[idx][1]] * k)
    return zsf(cls, ring.h)


def run(ring, beta, steps, seed, track, verbose=False):
    """One thermal element run. Returns a record dict."""
    menu = build_menu(ring, beta)
    rg = random.Random(seed)
    st = {}
    st_mask = 0
    hist = {i: [] for i in track}
    probs = {i: [] for i in track}
    incs = {i: [] for i in track}
    tails = []
    rewrites = 0
    absorbed_at = None
    for t in range(steps):
        adm = []
        cum = []
        tot = 0.0
        rmass = {i: 0.0 for i in track}
        rmass_w = {i: 0.0 for i in track}
        for mv in menu:
            if admissible(mv, st, st_mask, ring):
                adm.append(mv)
                tot += mv[2]
                cum.append(tot)
                for idx, e in mv[1]:
                    if idx in rmass:
                        rmass[idx] += mv[2]
                        rmass_w[idx] += mv[2] * e
        if not adm:
            absorbed_at = t
            break
        for i in track:
            hist[i].append(st.get(i, 0))
            probs[i].append(rmass[i] / tot if tot > 0 else 0.0)
            incs[i].append(rmass_w[i] / tot if tot > 0 else 0.0)
        a = b = kk = 0.0
        for idx, (nn, cc) in enumerate(ring.primes):
            w = nn ** (-beta)
            if st_mask >> idx & 1:
                if cc % ring.h:
                    kk += w
            else:
                if cc % ring.h:
                    b += w
                else:
                    a += w
        tails.append((a, b, kk))
        x = rg.random() * cum[-1]
        lo, hi = 0, len(cum) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if cum[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        mv = adm[lo]
        for idx, e in mv[1]:
            if st.get(idx, 0) > 0 and ring.primes[idx][1] % ring.h == 0:
                rewrites += 1
            st[idx] = st.get(idx, 0) + e
        st_mask |= mv[0]
    maxprin = max([st.get(i, 0) for i, (n, c) in enumerate(ring.primes)
                   if c % ring.h == 0] + [0])
    maxnon = max([st.get(i, 0) for i, (n, c) in enumerate(ring.primes)
                  if c % ring.h] + [0])
    return dict(menu=len(menu), hist=hist, probs=probs, incs=incs,
                tails=tails, rewrites=rewrites,
                absorbed_at=absorbed_at, state=st, maxprin=maxprin,
                maxnon=maxnon, steps=len(tails))


def slope(ys, lo, hi):
    """Least-squares slope of ys over [lo, hi)."""
    xs = list(range(lo, hi))
    n = len(xs)
    if n < 3:
        return 0.0
    mx = sum(xs) / n
    my = sum(ys[lo:hi]) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys[lo:hi]))
    den = sum((x - mx) ** 2 for x in xs)
    return num / den if den else 0.0


def track_smallest_nonprincipal(ring, k=3):
    out = []
    for i, (n, c) in enumerate(ring.primes):
        if c % ring.h:
            out.append(i)
            if len(out) == k:
                break
    return out


def c_beta(ring, beta):
    return sum(float(n) ** (-beta) for n, c in ring.primes if c % ring.h)


T0 = time.time()
print("explore_bottomless_columns.py -- THE BOTTOMLESS COLUMNS")
print()

# ------------------------------------------------------------------ #
print("S1: control A -- the class map against classical representability")
# ------------------------------------------------------------------ #
for name, disc, h, cls_ring in (("Q(sqrt(-5))", -20, 2, RingC2),
                                ("Q(sqrt(-23))", -23, 3, RingC3)):
    R = cls_ring(name, disc, h, 500)
    npr = nnp = 0
    for n, c in R.primes:
        rep = represented(disc, n)
        if c % h == 0:
            ok(rep, "%s: principal prime of norm %d not represented"
               % (name, n))
            npr += 1
        else:
            ok(not rep, "%s: nonprincipal prime of norm %d represented"
               % (name, n))
            nnp += 1
    print("  %s: %d principal / %d nonprincipal prime ideals of norm"
          " <= 500, every class agreeing with the principal form"
          % (name, npr, nnp))
    W = cls_ring(name, disc, h, 4000)
    pair = {}
    for n, c in W.primes:
        pair.setdefault(n, []).append(c)
    two = [(n, cs) for n, cs in pair.items() if len(cs) == 2]
    ok(all((cs[0] + cs[1]) % h == 0 for _, cs in two),
       "%s: the two primes above a split p are not inverse" % name)
    print("      and over %d split norms to 4000 the two primes above p"
          " carry INVERSE classes, which is what makes (p) principal"
          % len(two))
print()

# ------------------------------------------------------------------ #
print("S2: PR4 -- the Chebotarev leg, the fresh tails a(x) and b(x)")
# ------------------------------------------------------------------ #
YCAP = 10 ** 7
rp = sieve(YCAP)
print("  rational primes to %d: %d" % (YCAP, len(rp)))
for beta in (1.5, 2.0):
    row = []
    for x in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6):
        a = b = 0.0
        for p in rp:
            if p <= x:
                continue
            if p == 2 or p == 5:
                continue
            if kronecker(-20, p) == 1:
                w = 2.0 * float(p) ** (-beta)
                if p % 20 in (1, 9):
                    a += w
                else:
                    b += w
            else:
                if p * p <= YCAP and p * p > x:
                    a += float(p * p) ** (-beta)
        row.append((x, a / b))
    print("  beta = %.1f: " % beta + ", ".join(
        "a/b(%d) = %.4f" % (x, r) for x, r in row))
    if beta == 2.0:
        ok(abs(row[-1][1] - 1.0) < 0.10,
           "PR4 band |a/b - 1| < 0.10 at x = 10^6")
del rp
print()

# ------------------------------------------------------------------ #
print("S3: PR1 + PR5 + PR6 -- the shallow half over three class groups")
# ------------------------------------------------------------------ #
print("  The invariant is ENTRY-ONCE IN MOVES: once a principal column is")
print("  written, no later move may touch it.  Its DEPTH is whatever the")
print("  one writing move carried, which need not be 1 -- a fresh Q is")
print("  coprime to the state, so a move carrying Q^2 is admissible.")
print()
RING_ROW = (("Z[i] (h = 1)", RingC1, -4, 1, 2000),
            ("Z[sqrt(-5)] (h = 2)", RingC2, -20, 2, 2000),
            ("Q(sqrt(-23)) (h = 3)", RingC3, -23, 3, 2000))
for name, ctor, disc, h, cap in RING_ROW:
    R = ctor(name, disc, h, cap)
    track = track_smallest_nonprincipal(R)
    rec = run(R, 2.0, 200, 20250821, track)
    n = rec["steps"]
    sl = [slope(rec["hist"][i], n // 2, n) for i in rec["hist"]]
    deep = 0
    worst = rec["maxprin"]
    rw = rec["rewrites"]
    RUNS = 12
    for sd in range(RUNS):
        r2 = run(R, 2.0, 200, 777 + sd, [])
        rw += r2["rewrites"]
        worst = max(worst, r2["maxprin"])
        if r2["maxprin"] > 1:
            deep += 1
    print("  %-21s menu %5d moves, %3d steps, max nonprincipal depth %2d,"
          " late slopes %s" % (name, rec["menu"], rec["steps"],
                               rec["maxnon"],
                               "[" + ", ".join("%.3f" % x for x in sl) + "]"))
    print("  %-21s %d further runs: %d rewrite(s) of a written principal"
          " column, %d run(s) writing one deeper than 1 (worst depth %d)"
          % ("", RUNS, rw, deep, worst))
    ok(rw == 0,
       "PR1 a written principal column was rewritten at %s" % name)
    if h > 1:
        ok(all(x > 0 for x in sl),
           "PR6/PR2 a tracked nonprincipal column is flat at %s" % name)
    else:
        ok(rec["maxnon"] == 0, "PR5 a bottomless column at h = 1")
print()

# ------------------------------------------------------------------ #
print("S4: PR2 + PR3 -- the rate law over Z[sqrt(-5)], cap by cap")
# ------------------------------------------------------------------ #
print("  Five seeds per cell; the slope is pooled over them, the one-step")
print("  readings are means over the late half of every run.  'dry' is the")
print("  share of late-window steps at which the tracked column has NO")
print("  admissible raising move -- the truncation's own exhaustion, which")
print("  is the finite universe's absorption seen through a cap.")
print()
print("   cap beta   menu  N   r_low   r_high    slope  slope/r_low"
      "   mean p  p/r_low  min p/r_low  p_hat/p  slope/E[inc]   dry"
      "     a/b")
SEEDS = (4242, 90210, 15213, 271828, 31337)
RATE = []
for cap in (2000, 8000, 32000):
    R = RingC2("Z[sqrt(-5)]", -20, 2, cap)
    track = track_smallest_nonprincipal(R, 3)
    for beta in (1.5, 2.0):
        Cb = c_beta(R, beta)
        recs = [run(R, beta, 250, sd + cap, track) for sd in SEEDS]
        if cap == 32000:
            ok(all(r["absorbed_at"] is None for r in recs),
               "a top-cap run absorbed inside the measured window")
        acc = {i: [] for i in track}
        qm = {i: [] for i in track}
        pm = {i: [] for i in track}
        pmin = {i: [] for i in track}
        dry = {i: [] for i in track}
        aa = bb = kk = 0.0
        for rec in recs:
            n = rec["steps"]
            lo = n // 2
            win = rec["tails"][lo:n]
            aa += sum(w[0] for w in win) / len(win) / len(recs)
            bb += sum(w[1] for w in win) / len(win) / len(recs)
            kk += sum(w[2] for w in win) / len(win) / len(recs)
            for i in track:
                acc[i].append((rec["hist"][i][n - 1] - rec["hist"][i][lo])
                              / float(n - 1 - lo))
                ps = rec["probs"][i][lo:n]
                qs = rec["incs"][i][lo:n]
                pm[i].append(sum(ps) / len(ps))
                qm[i].append(sum(qs) / len(qs))
                pmin[i].append(min(ps))
                dry[i].append(sum(1 for x in ps if x == 0.0) / len(ps))
        for i in track:
            N = R.primes[i][0]
            wN = float(N) ** (-beta)
            r_lo, r_hi = wN / (1.0 + Cb), wN / Cb
            sl = sum(acc[i]) / len(acc[i])
            mp = sum(pm[i]) / len(pm[i])
            dr = sum(dry[i]) / len(dry[i])
            mn = min(pmin[i])
            mq = sum(qm[i]) / len(qm[i])
            p_hat = wN * bb / (aa + kk * bb)
            RATE.append((cap, beta, N, r_lo, r_hi, sl, mp, p_hat, dr,
                         aa / bb if bb else float("nan"), mn, mq))
            print("  %5d %.1f  %5d %3d  %.5f  %.5f  %.5f    %.3f "
                  "   %.5f   %.3f      %.3f      %.3f      %.3f"
                  "      %.3f   %.3f"
                  % (cap, beta, recs[0]["menu"], N, r_lo, r_hi, sl,
                     sl / r_lo, mp, mp / r_lo, mn / r_lo,
                     p_hat / mp if mp else float("nan"),
                     sl / mq if mq else float("nan"), dr,
                     aa / bb if bb else float("nan")))
print()

# ------------------------------------------------------------------ #
print("S4b: the denominator decomposed, so the identity is not read off")
print("     its own ratio -- the families the derivation names, weighed")
print("     against the true admissible mass at the end of a top-cap run")
# ------------------------------------------------------------------ #
Rtop = RingC2("Z[sqrt(-5)]", -20, 2, 32000)
mtop = build_menu(Rtop, 2.0)
rtop = run(Rtop, 2.0, 250, 4242 + 32000,
           track_smallest_nonprincipal(Rtop, 3))
st = rtop["state"]
mask = 0
for i in st:
    mask |= 1 << i
prim = Rtop.primes
tot = 0.0
fam = {"a  fresh principal prime": 0.0,
       "Kb state nonprincipal x fresh nonprincipal": 0.0,
       "b^2 two fresh nonprincipal": 0.0,
       "fixed P^2k at a depth-1 column": 0.0,
       "everything else": 0.0}
for mv in mtop:
    if not admissible(mv, st, mask, Rtop):
        continue
    tot += mv[2]
    e = mv[1]
    fresh = [(i, k) for i, k in e if not (mask >> i) & 1]
    old_ = [(i, k) for i, k in e if (mask >> i) & 1]
    nf = [(i, k) for i, k in fresh if prim[i][1]]
    if not old_ and len(e) == 1 and e[0][1] == 1 and prim[e[0][0]][1] == 0:
        fam["a  fresh principal prime"] += mv[2]
    elif (len(old_) == 1 and old_[0][1] == 1 and prim[old_[0][0]][1]
          and len(fresh) == 1 and len(nf) == 1 and nf[0][1] == 1):
        fam["Kb state nonprincipal x fresh nonprincipal"] += mv[2]
    elif (not old_ and len(fresh) == 2 and len(nf) == 2
          and all(k == 1 for _, k in fresh)):
        fam["b^2 two fresh nonprincipal"] += mv[2]
    elif not fresh and len(old_) == 1 and old_[0][1] >= 2:
        fam["fixed P^2k at a depth-1 column"] += mv[2]
    else:
        fam["everything else"] += mv[2]
for k in fam:
    print("     %-44s %.3e  %5.1f%%" % (k, fam[k], 100.0 * fam[k] / tot))
lead = (fam["a  fresh principal prime"]
        + fam["Kb state nonprincipal x fresh nonprincipal"]) / tot
ok(lead > 0.95, "the two named families carry the admissible mass")
print()

# ------------------------------------------------------------------ #
print("S5: the verdicts")
# ------------------------------------------------------------------ #
for cap in (2000, 8000, 32000):
    rows = [q for q in RATE if q[0] == cap]
    print("  cap %5d: slope/r_low in [%.3f, %.3f], p/r_low in [%.3f,"
          " %.3f], dry %.3f, worst identity error %.4f"
          % (cap, min(q[5] / q[3] for q in rows),
             max(q[5] / q[3] for q in rows),
             min(q[6] / q[3] for q in rows),
             max(q[6] / q[3] for q in rows),
             max(q[8] for q in rows),
             max(abs(q[7] / q[6] - 1.0) for q in rows)))
TOP = [q for q in RATE if q[0] == 32000]
ok(all(q[5] > 0 for q in RATE),
   "every tracked column has a positive pooled late-phase slope at every"
   " cap")
ok(all(q[3] <= q[6] <= q[4] for q in TOP),
   "the two-sided bound r_low <= p <= r_high at the top cap")
ok(max(abs(q[7] / q[6] - 1.0) for q in TOP) < 0.05,
   "the one-step identity p = N^-beta b / (a + K b) within 5% at the top"
   " cap")
ok(max(abs(q[7] / q[6] - 1.0) for q in TOP)
   < max(abs(q[7] / q[6] - 1.0) for q in RATE if q[0] == 8000)
   < max(abs(q[7] / q[6] - 1.0) for q in RATE if q[0] == 2000),
   "the identity's error falls monotonically with the cap")
ok(max(q[8] for q in TOP) < max(q[8] for q in RATE if q[0] == 2000),
   "the dry share falls with the cap (the exhaustion is the truncation's)")
ok(min(q[10] / q[3] for q in TOP) > 0.3,
   "PR3 band min p / r_low > 0.3 at the top cap")
ok(all(abs(q[5] / q[11] - 1.0) < 0.25 for q in TOP),
   "control C: the pooled slope tracks the independently computed"
   " expected increment at the top cap")
print()
print("  checks: %d, failures: %d, wall %.1f s"
      % (CHECKS, FAIL, time.time() - T0))
print("RESULT: %s" % ("all %d checks pass" % CHECKS if FAIL == 0
                      else "%d FAILURES" % FAIL))
