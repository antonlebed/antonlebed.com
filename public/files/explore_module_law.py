"""explore_module_law.py — the module law.

THE QUESTION (a descent from earlier work on explore_function_field_lock.py
and explore_number_field_lock.py). Earlier work measured: lock price =
p^(ef) = p^(rank of the local 1-unit module) on every censused
trajectory (Q, Z[sqrt(-5)]), and F_2[x] sprawls. THIS script proves the
law as a general statement and runs the global shadow: over
Q(sqrt(-23)) (maximal order Z[w], w^2 = w - 6, h = 3, Cl = C3, 2
SPLITS) does the element monobasin persist, or does the basin map read
ord[P]-vs-e resonance?

Predictions: Theorems A/B/C and observations MR1-MR7 were fixed before
the run and hand-checked in advance (the check caught MR6's ride-count
off-by-one before any run).

THE THEOREMS (proved by hand ahead of the run, harvested here;
brute-instantiated in s1/s2; these are theory, not run output):

A. THE LOCAL MODULE LAW (theorem — standard local-field structure;
   instances brute-verified in s1). For a complete DVR with finite
   residue field F_q, q = p^f, E(a) = exp(U1/U_a), lambda(P^a) =
   lcm(q-1, E(a)):
   - mixed char (char 0): K_P is finite over Q_p (Cohen), U1 has
     Z_p-rank d = ef; x -> x^p is an iso U_b -> U_{b+e} for
     b > e/(p-1), so m(a+e) = m(a)+1 eventually (E = p^m): a LINEAR
     pump — one lambda_p-tick per e depth, price q^e = p^(ef) =
     p^rank, eventually constant.
   - equal char (char p): O_P = F_q[[t]], (1+u)^(p^m) = 1 + u^(p^m),
     E(a) = p^ceil(log_p a) EXACTLY, rank infinite: a LOG clock — a
     tick from depth a needs depth > p^ceil(log_p a), so tick prices
     are UNBOUNDED along any recurring column (single-step ticks
     exist exactly at the p-power frontiers; the boundary gaps
     p^(k+1) - p^k force r -> infinity between consecutive ticks).
     No recurrent constant door.
   Fate and price read the local 1-unit module; Cohen structure makes
   "finite rank at some place" = "char 0" automatically.

B. CRYSTAL + ABSORPTION (rule, proved — the leapfrog endgame is the
   delicate step; census-verified). O Dedekind, residue fields finite,
   norm-finite (finitely many places per norm bound). Moves are
   single-place: a ticking part of any bundle ticks alone at strictly
   smaller norm (some column's lambda must leave L, and that column
   alone is cheaper) — Z's door lemma survives in the IDEAL world at
   every h; the ELEMENT world is where it dies (s3's product scan
   asserts this at every census move). Then:
   (i) a place picked infinitely often at bounded cost ABSORBS the
   tail (ownership makes its pick cost -> constant p^d; two such
   places is impossible: distinct chars give two equal prime powers
   of distinct primes, same char leapfrogs one out);
   (ii) equal char: move costs DIVERGE — THE SPRAWL, now general
   (any equal-characteristic Dedekind ring with finite residue
   fields, semilocal degenerates included — this settles an earlier
   "general equal-char Dedekind untested" scope at the
   cost-divergence level);
   (iii) mixed char: bounded-cost tail <=> lock, recurrent price
   exactly p^rank at the lock place.
   Supporting lemmas (verified move-by-move in s3): doors are
   monotone OFF-MOVE (the moved place's door CAN fall — move costs
   are NOT monotone); a ticking deepening leaves the column OWNING
   v_p; external v_p-raises cost > p^(v+1).

C. THE CASCADE BOUNDARY (the REDUCTION is a rule, proved by hand in the
   ideal world; what stays open is the ladder's death, not the
   reduction). Lock existence for ALL trajectories in general char 0
   reduces to ruling out an infinite carrier ladder: a non-locking
   trajectory needs, at every stage and for EVERY char with a rank-1
   place, a fresh carrier q_R = m*p^(v+1)+1 (m <= p-1) cheaper than the
   virgin p-door — Proth-form primes in narrow exponential windows,
   chained forever.
   THE DERIVATION, three steps, over a norm-finite Dedekind ring of
   char 0 under cold D-DYN (the least-norm lambda-growing move):
   (1) NON-LOCK MAKES COSTS DIVERGE. If infinitely many moves cost
       <= B, each deepens a place of norm <= B (moves are single-place,
       B) and there are finitely many such places, so one is picked
       infinitely often at bounded cost and B(i) absorbs the tail — a
       lock. So along a non-locking trajectory cost_n -> infinity.
   (2) EVERY RANK-1 CHAR CAPS THE COST, WHICH IS WHY THE DEMAND IS A
       CONJUNCTION. Let P be rank-1 over p (e = f = 1, so K_P = Q_p
       exactly and theorem A reads E(a) = p^(a-1)) and let
       v = v_p(lambda_n). Deepening P to depth v+2 raises v_p, and it
       costs at most p^(v+2) (2^(v+3) at p = 2, the extra Z/2): a
       lambda-growing move available whatever the state. Greedy is
       minimal, so cost_n <= p^(v_p(lambda_n)+2) — for every rank-1
       char at once. With (1), v_p(lambda_n) -> infinity at every one
       of them SIMULTANEOUSLY. The trajectory does not get to choose
       which characteristic to keep unsettled: each one caps its cost
       independently at every stage, so it must defeat all of them.
   (3) THE RISES NEED OUTSIDE CARRIERS, AND THE DOOR CAPS THEIR SIZE.
       By (2) v_p rises infinitely often. Only finitely many rises can
       run through a place OVER p: there are finitely many such places
       and a recurrent one owns v_p at the constant price p^rank (A, B),
       which is bounded and contradicts (1). At a place Q not over p,
       lambda(Q^b) = lcm(N(Q)-1, E_Q(b)) with E_Q(b) a power of Q's own
       residue char, so the p-part can only come from N(Q)-1 — whence
       the carrier form p^(v+1) | N(Q)-1, paid at face value N(Q). And
       greedy against the door of (2) gives N(Q) = m*p^(v+1)+1 <
       p^(v+2), i.e. m <= p-1: THE CAP IS PINNED AT w = 0 by the door
       alone (the budget inequality reaches the same pin by a different
       route, explore_ghost_wander.py). A place opens once, so the
       carriers are all distinct: the ladder, chained forever, at every
       rank-1 char.
   So the conjunction is real and the disjunction reading is refuted:
   breaking ONE characteristic closes the ring, which is what turns a
   sweep over primes into a statement about rings.
   WHERE IT WAS DERIVED, and where it now holds: the three steps are
   written above for THE IDEAL WORLD, element moves not being
   single-place, and all three carry over — the first by a repair, the
   second with a constant, the third with a loosening
   (explore_element_cascade.py, which owns the element-world derivation
   and re-walks the ladder under it). Step (1)'s pigeonhole moves from
   PLACES of bounded norm to IDEALS of bounded norm, both finite for the
   same reason, and the always-available constant-price move becomes a
   power of the recurrent BUNDLE rather than of the place: cost
   divergence survives at a field constant max(N(A)^e, p^(n*h)) in place
   of p^rank, a bounded recurrent price of the kind finding 3 censuses.
   Step (2)'s door is charged on a GENERATOR, at tau_K = max over ideal
   classes of the LEAST NORM in the class (a
   value, exactly computable, not merely the Minkowski bound that
   dominates it; tau_K = 1 iff h = 1), so P^(v+2) principalizes at norm
   <= tau_K*p^(v+2). Step (3)'s cap loosens to m < tau_K*p. So the
   reduction holds in the ideal world of every char-0 ring and in the
   element world of every number field, the cap being the only thing the
   class group moves.
   WHAT STAYS OPEN is the ladder's death, unchanged: heuristically dead
   at any bounded cap (chained window hits ~ prod c/v_i -> 0; the
   cap-growth model threshold ~ v ln v and certified per-cap
   all-miss censuses: explore_bridge_reach.py),
   unprovable with current least-prime-in-progression bounds. (SINCE:
   dead RETAIL at every odd p < 1000, each char reaching a rung of
   certified non-prime-powers, explore_cascade_chars.py, and what a
   WHOLESALE proof must supply is named in explore_cascade_theorem.py;
   the wholesale statement stands open as written.) Z's
   lock existence is proved elsewhere; K's and Q(sqrt(-23))'s are
   censused.

FINDINGS (run record at bottom; all sections assert; copied from run
output only).

1. THE LOCAL LAW HOLDS AT EVERY INSTANCE (theorem A instantiated; s1
   brute over full 1-unit grids). Mixed char — Z columns p = 2, 3, 5;
   K23 split-2 (E = 1, 2, then 2^(a-2): the Z 2-column verbatim at a
   SPLIT place — wildness belongs to the residue char, not the
   splitting type), split-3, split-13, inert-5, inert-7, ram-23 (one
   tick per e = 2 depth): E(a+e) = p*E(a) beyond a threshold <= 3 at
   every instance, price q^e = p^(ef) = p^rank per tick. Equal char —
   F_2[[t]], F_3[[t]], F_9[[t]]: E(a) = p^ceil(log_p a) EXACTLY
   (f-independent; the odd-q law now RUN, not only stated — closing
   an earlier stated-not-run gap at the law level), tick depth
   diverging.

2. THE IDEAL WORLD OF Q(sqrt(-23)) LOCKS, Z-STYLE (rule in range; 80
   seeds — void + all ideals of norm 2..40 + inert (17) — x 40 moves,
   every move re-verified by the norm-<=cost product scan): ALL LOCK;
   lock chars {2: 24, 3: 46, 5: 1, 13: 8, 29: 1}; recurrent price =
   p^(ef) on every trajectory (2-locks pay 2 — the p^rank floor is
   COMMON here because 2 splits to rank-1 places, where Z[sqrt(-5)]'s
   wild P2 paid 4; the (5) seed locks inert 5 at 25); every tie a
   conjugate pair at equal r (15 tie moves); max wander 2; the void
   repeats Z's column a third time (P3-tie at 3/move, frozen MR1).
   ZERO GHOSTS fired across the belt (unfrozen; K = Z[sqrt(-5)] had
   3): no belt dowry lands a char inside lambda at r = 1 here — the
   ghost spectrum is field geography, not a mixed-char constant.

3. THE MONOBASIN IS REFUTED AT h = 3 — the element world has TWO
   basins (the headline; rule in range; 41 element seeds x 40 moves;
   frozen MR4 MISSED, and the miss is the finding). 38 seeds
   (2)-lock at 4/move; 3 seeds — (5) and the two norm-26 elements —
   lock INERT 5 at 25/move: a pure principal column at the IDEAL
   price q^e, tax-free, with the 2-passenger never lifted (asserted:
   2-depths stay at seed level). Mechanism: the seed's own dowry
   lambda(P5) = 24 is a graveyard for every cheaper door (riders and
   cubes need 3-parts and shallow 2-parts that 24 already covers),
   so the cheapest live door is the column's own 25 — and a
   trajectory that never rides never wakes (2). THE PASSENGER LIFT
   (frozen MR4's mechanism) is real but CONDITIONAL: it forces the
   (2)-tail only on trajectories that ride bundles.

4. THE BASIN MAP IS A NORM RACE AMONG PRINCIPAL VEHICLES (the
   resonance answer, corrected by the census). Element basins are
   decided by which principal vehicle is cheapest once the seed's
   dowry kills the small menu: at K23 inert-5's own door (25)
   undercuts the 3-cube (27); at Z[sqrt(-5)] the same race went the
   other way (inert-11 at 121 loses to everything) — the earlier
   monobasin was FIELD GEOGRAPHY, not an h > 1 law. THE
   ELEMENT PRICE (observation, quadratic fields; four tail species):
   the tail pays its cheapest 1-move principal vehicle, and the two
   candidates are always P^m (the class-order power, norm p^(fm))
   and the rational (p) (norm p^2 in ANY quadratic field) — so the
   per-move price is p^min(fm, 2): Z's columns at p (f = m = 1);
   Z[sqrt(-5)]'s wild (2) = P2^2 at 4 (m = 2, where the power IS
   the bundle); K23's split (2) = P2*P2' at 4 (m = 3); K23's inert
   (5) at 25 (f = 2, m = 1 — the ideal price, tax-free). The tax
   over the ideal price p^(ef) exists only at fm > 2, and there it
   is PURE MYOPIA: the cube (2-w) = P2^3 offers 3 ticks at norm 8 =
   2/tick, tax-free, available forever, and is NEVER picked
   (asserted) — greedy minimizes per-move norm, not per-tick price.
   (Degree-n fields should read p^min(fm, n); untested.)

5. MOVE COSTS ARE NOT MONOTONE (rule; frozen MR2b + census). Doors
   are monotone off-move (asserted at every census move on the
   norm-<=60 probe set), but the MOVED place's door falls after a
   catch-up: ideal seed (7) pays 23, 23 (fresh tame P23 + deepen),
   27 (P3 catch-up), then locks 3 at 3/move — a 27 -> 3 drop;
   element seed (7) opens 23, 23, 27 then rides 6s to the (2)-tail
   at 4. Greedy cost sequences are catch-up-then-cheap, not
   staircases: Theorem B's route (bounded => concentration =>
   absorption) is forced — a naive monotone-cost argument is FALSE.

6. THE ELEMENT sqrt(-23) DOOR (frozen MR6's miss, the slate's second
   correction). The tame ramified place is PRINCIPAL here
   (sqrt(-23) = 2w - 1, norm 23), so the element world owns a cheap
   odd vehicle the hand-run forgot: seeds (5), (7), (17) all open
   23, 23 (two sqrt(-23) moves) before their basin plays out — MR6's
   cube-rides-takeover shape held from move 3 ((7): 23, 23, 27, six
   6-rides, then 4s; asserted as observed). The void is untouched
   (its overture 6, 6, 6 then 4s — frozen MR3 — never sees 23).

Run: `python explore_module_law.py`. RUN RECORD (94718 checks,
~5.7 min): s1 Z 1-unit pumps p = 2 (a <= 12), 3, 5 (a <= 8); K23
1-unit grids split-2 a <= 9, split-3 a <= 6, split-13 a <= 2,
inert-5 a <= 3, inert-7 a <= 2, ram-23 j <= 3 (+ full-unit lambda
cross-check at a <= 2 per place); equal char full-group F_2 a <= 8,
F_3 a <= 5, F_9 a <= 4 + deg-1 ladders a <= 32/27/9 — every E law
exact, mixed thresholds <= 3, tick depth diverging. s2 independent
lattice brute: 13 engine moves = full grid scan over all_ideals(40)
(ideal: void x3, P2^5 x2, P3^2 x2, (7) x1; element void x5); 39
element factorizations lattice-exact. s3 ideal census 80 seeds x
T = 40, every move product-scanned + off-move door monotonicity on
the probe set + ownership at every ticking deepening: ALL LOCK,
price law exact per trajectory, 15 tie moves all conjugate pairs at
equal r, max wander 2, ZERO ghosts, cost drops seen; MR1 + MR2b hit;
P2^5 locks split-2 at 2/move. s4 element census 41 seeds x 40: TWO
BASINS {2: 38, 5: 3} (frozen MR4's monobasin REFUTED); (2)-tails at
norm 4 with exactly one flat 2-part per move; (5)-tails at norm 25,
pure ticks, passenger never lifted; void overture 6,6,6-then-4s
(MR3 hit); (7) = 23,23,27, rides, 4s (MR6's opener missed, shape
from move 3 hit); (5) = 23,23,25-forever; the cube never picked;
1510 flat-part multi-place moves (the (2)-tails included: every
(2)-move carries its shallow twin flat); 12 element tie moves, all
conjugation-closed. s5 Galois equivariance 3 ideal + 3 element seed
pairs, conjugate move-by-move under flipped tie-break. Predictions
MR1-MR7: MR1, MR2, MR2b, MR3, MR7 hit; MR5 hit as
scoped to the (2)-basin; MR4 REFUTED (two basins); MR6 refuted in
part (the sqrt(-23) opener). Findings beyond the predictions: the
(5)-basin trio + the dowry-graveyard mechanism, the zero-ghost belt,
the 24 cheap split-2 locks, the ideal 5- and 29-locks. (An earlier
drafting pass had carried invented totals, histograms, and a
fictional P23^3 lock before any run; expunged pre-run, and the real
census then refuted that fabricated monobasin story outright.)
"""

import sys, os
import itertools
from math import gcd, isqrt

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def lcm(a, b):
    return a // gcd(a, b) * b


def v_p(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def prime_divisors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def _sieve(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(2, n + 1) if s[i]]


# ------------------------------------------------- the ring O = Z[w], K23
# w = (1 + sqrt(-23))/2, w^2 = T*w + N0 with T = 1, N0 = -6.
# N(x + y*w) = x^2 + xy + 6y^2. Ideals in HNF (n1, s, n2) =
# Z*n1 + Z*(s + n2*w), n2 | n1, 0 <= s < n1, norm n1*n2.
T, N0 = 1, -6
MAXP = 2000
PRIMES = _sieve(MAXP)


def emul(a, b):
    """(x1 + y1 w)(x2 + y2 w) with w^2 = T w + N0."""
    x1, y1 = a
    x2, y2 = b
    return (x1 * x2 + N0 * y1 * y2, x1 * y2 + x2 * y1 + T * y1 * y2)


def mem(A, x, y):
    n1, s, n2 = A
    return y % n2 == 0 and (x - (y // n2) * s) % n1 == 0


def hnf_from_vecs(vecs):
    """HNF (n1, s, n2) of the Z-module spanned by (x, y) vectors."""
    v2 = None
    xs = []
    for (x, y) in vecs:
        if y == 0:
            xs.append(x)
            continue
        if v2 is None:
            v2 = (x, y)
            continue
        a, b = v2, (x, y)
        while b[1] != 0:
            q = a[1] // b[1]
            a, b = b, (a[0] - q * b[0], a[1] - q * b[1])
        v2 = a
        if b[0]:
            xs.append(b[0])
    assert v2 is not None and v2[1] != 0, "hnf: rank-1 input"
    if v2[1] < 0:
        v2 = (-v2[0], -v2[1])
    n2 = v2[1]
    n1 = 0
    for x in xs:
        n1 = gcd(n1, abs(x))
    assert n1 > 0, "hnf: infinite index"
    s = v2[0] % n1
    assert n1 % n2 == 0, "hnf: not an O-lattice shape"
    return (n1, s, n2)


def ideal_from_gens(gens):
    """O-ideal generated by elements (x, y): close under w-multiplication."""
    vecs = []
    for g in gens:
        vecs.append(g)
        vecs.append(emul(g, (0, 1)))
    A = hnf_from_vecs(vecs)
    n1, s, n2 = A
    assert mem(A, 0, n1) and mem(A, N0 * n2, s + T * n2), \
        "ideal_from_gens: not w-closed"
    return A


def ideal_mul(A, B):
    n1, s, n2 = A
    m1, t, m2 = B
    ga = [(n1, 0), (s, n2)]
    gb = [(m1, 0), (t, m2)]
    return ideal_from_gens([emul(a, b) for a in ga for b in gb])


def ideal_pow(A, e):
    R = (1, 0, 1)
    while e:
        if e & 1:
            R = ideal_mul(R, A)
        if e > 1:
            A = ideal_mul(A, A)
        e >>= 1
    return R


def ideal_norm(A):
    return A[0] * A[2]


def qmul(A, a, b):
    """Multiply in O/A."""
    n1, s, n2 = A
    x, y = emul(a, b)
    yr = y % n2
    x = (x - ((y - yr) // n2) * s) % n1
    return (x, yr)


def qpow(A, u, e):
    r, b = (1, 0), u
    while e:
        if e & 1:
            r = qmul(A, r, b)
        b = qmul(A, b, b)
        e >>= 1
    return r


# ------------------------------------------------------------------ places
# ('split', p, r): P = (p, w - r), r a root of z^2 - T z - N0 mod p;
# ('inert', q); ('ram', 23) with the double root 12.
SPLIT_ROOT = {}


def place_norm(pl):
    return pl[1] * pl[1] if pl[0] == 'inert' else pl[1]


def place_char(pl):
    return pl[1]


def place_ef(pl):
    return 1 if pl[0] == 'split' else 2


def place_key(pl):
    return (place_norm(pl), pl[2] if pl[0] == 'split' else 0)


def conj_place(pl):
    if pl[0] == 'split':
        return ('split', pl[1], (T - pl[2]) % pl[1])
    return pl


def build_universe():
    places = []
    for p in PRIMES:
        rts = [r for r in range(p) if (r * r - T * r - N0) % p == 0]
        if len(rts) == 2:
            SPLIT_ROOT[p] = rts[0]
            places.append(('split', p, rts[0]))
            places.append(('split', p, rts[1]))
        elif len(rts) == 1:
            places.append(('ram', p))
        elif p * p <= MAXP:
            places.append(('inert', p))
    places.sort(key=place_key)
    return places


UNIVERSE = build_universe()
RAM_ROOT = 12  # the double root of z^2 - z + 6 mod 23


def place_hnf(pl):
    k, p = pl[0], pl[1]
    if k == 'split':
        return ideal_from_gens([(p, 0), (-pl[2], 1)])
    if k == 'inert':
        return ideal_from_gens([(p, 0)])
    return ideal_from_gens([(p, 0), (-RAM_ROOT, 1)])


SPLIT2_TABLE = (1, 2)


def lam_P(pl, a):
    """lambda of the column P^a (laws brute-verified in s1)."""
    if a == 0:
        return 1
    k, p = pl[0], pl[1]
    if k == 'split':
        if p == 2:
            return SPLIT2_TABLE[a - 1] if a <= 2 else 2 ** (a - 2)
        return (p - 1) * p ** (a - 1)
    if k == 'inert':
        return (p * p - 1) * p ** (a - 1)
    return 22 * 23 ** (a // 2)


def lam_state(st):
    L = 1
    for pl, e in st.items():
        L = lcm(L, lam_P(pl, e))
    return L


# --------------------------------------------------------- the ideal engine
def door_r(pl, e, L):
    r = 1
    while L % lam_P(pl, e + r) == 0:
        r += 1
        assert r < 500, "door search runaway"
    return r


def ideal_menu(st, L):
    best, ties = None, []
    for pl in UNIVERSE:
        nrm = place_norm(pl)
        if best is not None and nrm > best:
            break
        r = door_r(pl, st.get(pl, 0), L)
        cost = nrm ** r
        if best is None or cost < best:
            best, ties = cost, [(pl, r)]
        elif cost == best:
            ties.append((pl, r))
    assert best <= MAXP, "universe guard: door beyond MAXP"
    ties.sort(key=lambda t: place_key(t[0]))
    return best, ties


def classify(st, L, pl, r):
    if st.get(pl, 0) > 0:
        return 'deepen'
    if r == 1:
        return 'ghost' if L % place_char(pl) == 0 else 'fresh'
    return 'clocked'


SCAN_CAP = 600
_scan_cache = {}


def gen_products(maxnorm):
    if maxnorm in _scan_cache:
        return _scan_cache[maxnorm]
    pls = [pl for pl in UNIVERSE if place_norm(pl) <= maxnorm]
    out = []

    def rec(i, cur, nrm):
        if cur:
            out.append((nrm, dict(cur)))
        for j in range(i, len(pls)):
            pl = pls[j]
            n2 = nrm * place_norm(pl)
            if n2 > maxnorm:
                break
            e = 1
            while n2 <= maxnorm:
                cur[pl] = e
                rec(j + 1, cur, n2)
                e += 1
                n2 *= place_norm(pl)
            del cur[pl]

    rec(0, {}, 1)
    out.sort(key=lambda x: x[0])
    _scan_cache[maxnorm] = out
    return out


def scan_check(st, L, cost, ties):
    """No ideal of norm < cost ticks; the norm-cost tickers = ties."""
    at_cost = set()
    for nrm, m in gen_products(cost):
        L2 = L
        for pl, e in m.items():
            L2 = lcm(L2, lam_P(pl, st.get(pl, 0) + e))
        tick = L2 > L
        if nrm < cost:
            ok(not tick, "scan: cheaper ticking ideal at norm %d" % nrm)
        elif tick:
            ok(len(m) == 1, "scan: min-cost ticking ideal not a prime power")
            (pl, e), = m.items()
            at_cost.add((pl, e))
    ok(at_cost == set(ties), "scan ties != menu ties")


PROBE = [pl for pl in UNIVERSE if place_norm(pl) <= 60]


def run_ideal(seed, Tm, flip=False, scan=False, monitor=False):
    st, L = dict(seed), lam_state(seed)
    log = []
    prev_doors, last_pl = None, None
    for _ in range(Tm):
        cost, ties = ideal_menu(st, L)
        if scan:
            ok(cost <= SCAN_CAP, "census door above scan cap")
            scan_check(st, L, cost, ties)
        if monitor:
            doors = {pl: place_norm(pl) ** door_r(pl, st.get(pl, 0), L)
                     for pl in PROBE}
            # Lemma 1: unmoved probe doors never fall
            if prev_doors is not None:
                for q in PROBE:
                    if q != last_pl:
                        ok(prev_doors[q] <= doors[q],
                           "off-move door fell at %s" % (q,))
        if flip:
            pl, r = min(ties, key=lambda t: place_key(conj_place(t[0])))
        else:
            pl, r = ties[0]
        kind = classify(st, L, pl, r)
        old_dep = st.get(pl, 0)
        st[pl] = old_dep + r
        L2 = lam_state(st)
        ok(L2 > L, "chosen move grows lambda")
        if monitor:
            prev_doors, last_pl = doors, pl
            # Lemma 2: a ticking deepening owns its char's part of lambda
            p = place_char(pl)
            if old_dep > 0 and v_p(lam_P(pl, old_dep + r), p) > v_p(L, p):
                ok(v_p(L2, p) == v_p(lam_P(pl, old_dep + r), p),
                   "ownership failed at %s" % (pl,))
        log.append((pl, r, cost, kind, len(ties)))
        L = L2
    return log, st, L


# -------------------------------------------------------- the element engine
def elem_candidates(n):
    """Canonical reps (y, x) of norm n (units {+-1}: y > 0, or y=0, x >= 2)."""
    out = []
    if n >= 4:
        x = isqrt(n)
        if x * x == n and x >= 2:
            out.append((0, x))
    y = 1
    while 23 * y * y <= 4 * n:
        d2 = 4 * n - 23 * y * y
        d = isqrt(d2)
        if d * d == d2 and (d - y) % 2 == 0:
            x1, x2 = (-y + d) // 2, (-y - d) // 2
            out.append((y, x1))
            if x2 != x1:
                out.append((y, x2))
        y += 1
    return sorted(out)


def factor_elem(x, y):
    """Place factorization of the principal ideal (x + y w)."""
    n = x * x + T * x * y - N0 * y * y
    assert n > 1
    fac = {}
    for p in prime_divisors(n):
        v = v_p(n, p)
        if p == 23:
            fac[('ram', 23)] = v
        elif p in SPLIT_ROOT:
            r = SPLIT_ROOT[p]
            xx, yy, c = x, y, 0
            while xx % p == 0 and yy % p == 0:
                xx //= p
                yy //= p
                c += 1
            rem = v - 2 * c
            e0, e1 = c, c
            if rem:
                if (xx + yy * r) % p == 0:
                    e0 += rem
                else:
                    assert (xx + yy * ((T - r) % p)) % p == 0, "split val"
                    e1 += rem
            if e0:
                fac[('split', p, r)] = e0
            if e1:
                fac[('split', p, (T - r) % p)] = e1
        else:
            assert v % 2 == 0, "inert valuation odd"
            fac[('inert', p)] = v // 2
    nn = 1
    for pl, e in fac.items():
        nn *= place_norm(pl) ** e
    assert nn == n, "factor_elem norm mismatch"
    return fac


def conj_elem(yx):
    y, x = yx
    if y == 0:
        return yx
    return (y, -(x + T * y))


def elem_menu(st, L, nmax=4000):
    for n in range(2, nmax + 1):
        hits = []
        for (y, x) in elem_candidates(n):
            fac = factor_elem(x, y)
            L2 = L
            for pl, e in fac.items():
                L2 = lcm(L2, lam_P(pl, st.get(pl, 0) + e))
            if L2 > L:
                hits.append(((y, x), fac))
        if hits:
            return n, hits
    raise AssertionError("element scan exhausted")


def canon_elem(yx):
    y, x = yx
    if y > 0 or (y == 0 and x >= 2):
        return yx
    return (-y, -x)


def run_elem(seed, Tm, flip=False):
    st, L = dict(seed), lam_state(seed)
    log = []
    for _ in range(Tm):
        n, hits = elem_menu(st, L)
        if len(hits) > 1:
            hset = set(h[0] for h in hits)
            ok(set(canon_elem(conj_elem(yx)) for yx in hset) == hset,
               "element tie set not conjugation-closed")
        if flip:
            tgt = min(conj_elem(h[0]) for h in hits)
            (yx, fac), = [h for h in hits if conj_elem(h[0]) == tgt]
        else:
            yx, fac = hits[0]
        flat = tuple(pl for pl, e in fac.items()
                     if L % lam_P(pl, st.get(pl, 0) + e) == 0)
        for pl, e in fac.items():
            st[pl] = st.get(pl, 0) + e
        L2 = lam_state(st)
        ok(L2 > L, "element move grows lambda")
        log.append((yx, fac, n, flat, len(hits)))
        L = L2
    return log, st, L


# ------------------------------------- independent brute (lattice arithmetic)
def ideal_contains(B, A):
    n1, s, n2 = A
    return mem(B, n1, 0) and mem(B, s, n2)


def all_ideals(B):
    """Every integral ideal of norm <= B by direct lattice closure."""
    out = []
    for n2 in range(1, B + 1):
        n1 = n2
        while n1 * n2 <= B:
            for s in range(n1):
                A = (n1, s, n2)
                if mem(A, 0, n1) and mem(A, N0 * n2, s + T * n2):
                    out.append(A)
            n1 += n2
    out.sort(key=lambda A: (ideal_norm(A), A))
    return out


def brute_tick(Ihnf, mhnf, L):
    """Ground truth: lambda(I*m) > L? Unit screen by place membership."""
    Am = ideal_mul(Ihnf, mhnf)
    div_places = []
    for p in prime_divisors(ideal_norm(Am)):
        for pl in UNIVERSE:
            if place_char(pl) == p and ideal_contains(place_hnf(pl), Am):
                div_places.append(place_hnf(pl))
    n1, s, n2 = Am
    for x in range(n1):
        for y in range(n2):
            if any(mem(P, x, y) for P in div_places):
                continue
            if qpow(Am, (x, y), L) != (1, 0):
                return True
    return False


def state_hnf(st):
    A = (1, 0, 1)
    for pl, e in st.items():
        A = ideal_mul(A, ideal_pow(place_hnf(pl), e))
    return A


def one_unit_exp(pl, a):
    """Brute exponent of U1/U_a at place pl, over the full grid."""
    A = ideal_pow(place_hnf(pl), a)
    P = place_hnf(pl)
    n1, s, n2 = A
    L = 1
    for x in range(n1):
        for y in range(n2):
            if not mem(P, x - 1, y):
                continue
            u, o = (x, y), 1
            t = u
            while t != (1, 0):
                t = qmul(A, t, u)
                o += 1
                assert o <= ideal_norm(A), "order runaway"
            L = lcm(L, o)
    return L


def lam_pp_brute(pl, a):
    """Brute exponent of the full unit group (O/P^a)^*."""
    A = ideal_pow(place_hnf(pl), a)
    P = place_hnf(pl)
    n1, s, n2 = A
    L = 1
    for x in range(n1):
        for y in range(n2):
            if mem(P, x, y):
                continue
            u, o = (x, y), 1
            t = u
            while t != (1, 0):
                t = qmul(A, t, u)
                o += 1
                assert o <= ideal_norm(A), "order runaway"
            L = lcm(L, o)
    return L


# ------------------------------------------------ equal characteristic brute
def fq_arith(q):
    """(add, mul, zero, one, nonzero list) for F_q, q in {2, 3, 9}."""
    if q in (2, 3):
        return (lambda a, b: (a + b) % q, lambda a, b: (a * b) % q,
                0, 1, list(range(1, q)))
    # F_9 = F_3[u]/(u^2 + 1), elements (c0, c1) = c0 + c1*u
    add = lambda a, b: ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)

    def mul(a, b):
        return ((a[0] * b[0] - a[1] * b[1]) % 3,
                (a[0] * b[1] + a[1] * b[0]) % 3)

    nz = [(c0, c1) for c0 in range(3) for c1 in range(3) if (c0, c1) != (0, 0)]
    return add, mul, (0, 0), (1, 0), nz


def poly_one_unit_order(q, a, coeffs):
    """Order of 1 + sum coeffs[i] t^(i+1) in (F_q[t]/t^a)^*."""
    add, mul, zero, one, _ = fq_arith(q)
    u = ([one] + list(coeffs) + [zero] * a)[:a]

    def pmul(f, g):
        h = [zero] * a
        for i, fi in enumerate(f):
            if fi == zero:
                continue
            for j, gj in enumerate(g):
                if i + j >= a:
                    break
                h[i + j] = add(h[i + j], mul(fi, gj))
        return h

    ident = [one] + [zero] * (a - 1)
    t, o = u, 1
    while t != ident:
        t = pmul(t, u)
        o += 1
        assert o <= 4 ** a, "poly order runaway"
    return o


def ceil_log(p, a):
    m, v = 0, 1
    while v < a:
        v *= p
        m += 1
    return m


# ================================================================== sections
def s1_local_law():
    """Theorem A instantiated: 1-unit exponent laws, mixed and equal."""
    # --- Z columns (mixed, e = f = 1)
    for p, amax in ((2, 12), (3, 8), (5, 8)):
        E = []
        for a in range(1, amax + 1):
            L = 1
            for u in range(1, p ** a, p):
                o, t = 1, u
                while t != 1:
                    t = t * u % p ** a
                    o += 1
                L = lcm(L, o)
            E.append(L)
        for a, got in enumerate(E, 1):
            if p > 2:
                ok(got == p ** (a - 1), "Z 1-unit law p=%d a=%d" % (p, a))
            else:
                want = (1, 2)[a - 1] if a <= 2 else 2 ** (a - 2)
                ok(got == want, "Z 1-unit law p=2 a=%d" % a)
        thr = 3 if p == 2 else 1
        for a in range(thr, amax):
            ok(E[a] == p * E[a - 1], "linear pump Z p=%d a=%d" % (p, a))
    print("s1 Z columns: 1-unit pumps linear (threshold 3 wild, 1 tame)")

    # --- K23 places (mixed): brute E over the lattice, cross-check lam_P
    instances = [
        (('split', 2, SPLIT_ROOT[2]), 9),
        (('split', 3, SPLIT_ROOT[3]), 6),
        (('split', 13, SPLIT_ROOT[13]), 2),
        (('inert', 5), 3),
        (('inert', 7), 2),
        (('ram', 23), 3),
    ]
    for pl, amax in instances:
        p = place_char(pl)
        e = 2 if pl[0] == 'ram' else 1
        E = [one_unit_exp(pl, a) for a in range(1, amax + 1)]
        for a, got in enumerate(E, 1):
            ok(got == p ** v_p(lam_P(pl, a), p),
               "K23 E law at %s a=%d: brute %d" % (pl, a, got))
        rel = range(1, amax + 1 - e)
        fails = [a for a in rel if E[a + e - 1] != p * E[a - 1]]
        thr = (fails[-1] + 1) if fails else 1
        ok(thr <= 3, "K23 pump threshold at %s: %d" % (pl, thr))
        for a in range(thr, amax + 1 - e):
            ok(E[a + e - 1] == p * E[a - 1],
               "linear pump at %s a=%d" % (pl, a))
        for a in range(1, min(amax, 2) + 1):
            ok(lam_pp_brute(pl, a) == lam_P(pl, a),
               "lambda law at %s a=%d" % (pl, a))
    print("s1 K23 places: E laws exact (split-2 = the Z 2-column verbatim), "
          "pumps linear, price q^e = p^(ef)")

    # --- equal characteristic: E(a) = p^ceil(log_p a) exactly
    for q, p, afull, adeg1 in ((2, 2, 8, 32), (3, 3, 5, 27), (9, 3, 4, 9)):
        add, mul, zero, one, nz = fq_arith(q)
        for a in range(2, afull + 1):
            L = 1
            for coeffs in itertools.product([zero] + nz, repeat=a - 1):
                if all(c == zero for c in coeffs):
                    continue
                L = lcm(L, poly_one_unit_order(q, a, coeffs))
            ok(L == p ** ceil_log(p, a),
               "equal-char E full q=%d a=%d: %d" % (q, a, L))
        for a in range(2, adeg1 + 1):
            for c in nz:
                ok(poly_one_unit_order(q, a, [c]) == p ** ceil_log(p, a),
                   "equal-char deg-1 q=%d a=%d" % (q, a))
        last = 0
        for k in range(1, 4):
            a = p ** k
            r = p ** ceil_log(p, a + 1) + 1 - a
            ok(r > last, "equal-char tick depth not diverging q=%d" % q)
            last = r
    print("s1 equal char q=2,3,9: E(a) = p^ceil(log_p a) exact "
          "(odd q RUN; f-independent), tick depth diverges")


def s2_cross_gates():
    """Independent grid brute: engine menus and factorizations exact."""
    pool = all_ideals(40)
    ideal_states = [
        ({}, 3),
        ({('split', 2, SPLIT_ROOT[2]): 5}, 2),
        ({('split', 3, SPLIT_ROOT[3]): 2}, 2),
        ({('inert', 7): 1}, 1),
    ]
    n_moves = 0
    for seed, nmoves in ideal_states:
        st, L = dict(seed), lam_state(seed)
        for _ in range(nmoves):
            cost, ties = ideal_menu(st, L)
            ok(cost <= 40, "s2 door beyond the brute pool")
            Ihnf = state_hnf(st)
            at_cost = []
            for m in pool:
                nm = ideal_norm(m)
                if nm < 2:
                    continue
                if nm > cost:
                    break
                tick = brute_tick(Ihnf, m, L)
                if nm < cost:
                    ok(not tick, "brute: cheaper ticking ideal norm %d" % nm)
                elif tick:
                    at_cost.append(m)
            want = sorted(ideal_pow(place_hnf(pl), r) for pl, r in ties)
            ok(sorted(at_cost) == want, "brute ties != engine ties")
            pl, r = ties[0]
            st[pl] = st.get(pl, 0) + r
            L = lam_state(st)
            n_moves += 1
    # element void: first 5 moves against the grid
    st, L = {}, 1
    for _ in range(5):
        n, hits = elem_menu(st, L)
        Ihnf = state_hnf(st)
        for nn in range(2, n + 1):
            for (y, x) in elem_candidates(nn):
                tick = brute_tick(Ihnf, ideal_from_gens([(x, y)]), L)
                engine_tick = any(h[0] == (y, x) for h in hits) and nn == n
                if nn < n:
                    ok(not tick, "element brute: cheaper tick at %d" % nn)
                else:
                    ok(tick == engine_tick, "element brute tick mismatch")
        yx, fac = hits[0]
        for pl, e in fac.items():
            st[pl] = st.get(pl, 0) + e
        L = lam_state(st)
        n_moves += 1
    # element factorization = lattice arithmetic, norms <= 60
    n_fac = 0
    for nn in range(2, 61):
        for (y, x) in elem_candidates(nn):
            fac = factor_elem(x, y)
            ok(state_hnf(fac) == ideal_from_gens([(x, y)]),
               "factor_elem != lattice ideal at (%d,%d)" % (x, y))
            n_fac += 1
    print("s2 independent brute: %d engine moves = grid scan; "
          "%d element factorizations lattice-exact" % (n_moves, n_fac))


def lock_of(log, tail):
    moves = log[-tail:]
    pl0 = moves[0][0]
    if all(pl == pl0 and kind == 'deepen'
           for (pl, r, c, kind, nt) in moves):
        return pl0
    return None


def s3_ideal_census():
    """The ideal world locks Z-style; price law; lemma verifiers live."""
    Tm = 40
    seeds = [{}]
    for A in all_ideals(40):
        if ideal_norm(A) < 2:
            continue
        fac = {}
        for p in prime_divisors(ideal_norm(A)):
            for pl in UNIVERSE:
                if place_char(pl) != p:
                    continue
                k = 0
                while ideal_contains(ideal_pow(place_hnf(pl), k + 1), A):
                    k += 1
                if k:
                    fac[pl] = k
        nn = 1
        for pl, e in fac.items():
            nn *= place_norm(pl) ** e
        ok(nn == ideal_norm(A), "seed factorization norm mismatch")
        seeds.append(fac)
    seeds.append({('inert', 17): 1})
    lock_hist, ghost_chars, tie_moves, wander_max = {}, {}, 0, 0
    drop_seen = False
    for seed in seeds:
        log, st, L = run_ideal(seed, Tm, scan=True, monitor=True)
        pl = lock_of(log, 25)
        ok(pl is not None, "a census trajectory failed to lock")
        p = place_char(pl)
        lock_hist[p] = lock_hist.get(p, 0) + 1
        for (mpl, r, c, kind, nt) in log[-25:]:
            ok(c == p ** place_ef(pl), "price law: %d != %d^%d at %s"
               % (c, p, place_ef(pl), pl))
        w = next(i for i, mv in enumerate(log) if mv[0] == pl)
        wander_max = max(wander_max, w)
        ok(log[w][3] != 'ghost', "lock place entered by a ghost")
        ok(all(mv[0] == pl and mv[3] == 'deepen' for mv in log[w + 1:]),
           "a move after the first lock-place pick left the column")
        costs = [mv[2] for mv in log]
        if any(costs[i + 1] < costs[i] for i in range(len(costs) - 1)):
            drop_seen = True
        for (mpl, r, c, kind, nt) in log:
            if kind == 'ghost':
                ghost_chars[place_char(mpl)] = \
                    ghost_chars.get(place_char(mpl), 0) + 1
            if nt > 1:
                tie_moves += 1
                ok(nt == 2, "ideal tie set larger than a Galois pair")
    # ties are conjugate pairs at equal r: replay the menus
    for seed in seeds:
        st, L = dict(seed), lam_state(seed)
        for _ in range(Tm):
            cost, ties = ideal_menu(st, L)
            if len(ties) == 2:
                (p0, r0), (p1, r1) = ties
                ok(conj_place(p0) == p1 and r0 == r1,
                   "ideal tie not a conjugate pair at equal r")
            pl, r = ties[0]
            st[pl] = st.get(pl, 0) + r
            L = lam_state(st)
    ok(drop_seen, "no cost drop in the ideal census (MR2b shape)")
    # MR1: the void = Z's column a third time
    log, st, L = run_ideal({}, Tm)
    ok(log[0][4] == 2 and log[0][2] == 3,
       "MR1 the void's first move is the P3/P3' tie at 3")
    ok(all(place_char(mv[0]) == 3 and mv[2] == 3 for mv in log),
       "MR1 void locks a norm-3 place at 3/move")
    # MR2b: seed (7) pays 23, 23, 27 then locks 3 — the cost drop
    log, st, L = run_ideal({('inert', 7): 1}, Tm)
    costs = [mv[2] for mv in log]
    ok(costs[:3] == [23, 23, 27] and set(costs[3:]) == {3},
       "MR2b (7): 23,23,27 then 3/move (got %s)" % costs[:6])
    ok(place_char(log[0][0]) == 23 and log[0][3] == 'fresh',
       "MR2b (7) move 1 is the fresh tame P23")
    # constructed deep 2-seed: the split 2-lock at 2/move (p^rank floor)
    log, st, L = run_ideal({('split', 2, SPLIT_ROOT[2]): 5}, Tm)
    ok(place_char(lock_of(log, 25)) == 2 and all(mv[2] == 2 for mv in log),
       "P2^5 does not lock split-2 at 2/move")
    ok(5 not in ghost_chars, "a 5-ghost fired (inert-5 gate)")
    print("s3 ideal census (%d seeds, T=%d): ALL LOCK; lock chars %s"
          % (len(seeds), Tm, sorted(lock_hist.items())))
    print("   ghosts by char %s; tie moves %d (all Galois pairs); "
          "max wander %d; cost drops seen (catch-up-then-cheap)"
          % (sorted(ghost_chars.items()), tie_moves, wander_max))
    return lock_hist


def s4_element_census():
    """The two-basin element map at h = 3 (MR4's monobasin REFUTED):
    the passenger lift vs the tax-free inert column, and the myopia tax."""
    Tm = 40
    seeds = [{}]
    for nn in range(2, 61):
        for (y, x) in elem_candidates(nn):
            seeds.append(factor_elem(x, y))
    seeds.append({('inert', 17): 1})
    P2 = ('split', 2, SPLIT_ROOT[2])
    P2c = conj_place(P2)
    two_move = {P2: 1, P2c: 1}
    five_move = {('inert', 5): 1}
    n_rider, tie_moves = 0, 0
    basins = {}
    for seed in seeds:
        log, st, L = run_elem(seed, Tm)
        tail = log[-25:]
        ok(all(fac == tail[0][1] for (yx, fac, n, flat, nt) in tail),
           "a tail is not a single recurrent vehicle (seed %s)" % (seed,))
        fac0 = tail[0][1]
        ok(fac0 in (two_move, five_move),
           "a tail vehicle beyond (2)/(5) (seed %s)" % (seed,))
        if fac0 == two_move:
            basins['2'] = basins.get('2', 0) + 1
            for (yx, fac, n, flat, nt) in tail:
                ok(n == 4, "(2)-tail move not at norm 4")
                ok(len(flat) == 1 and place_char(flat[0]) == 2,
                   "(2)-tail move without exactly one flat 2-part")
        else:
            basins['5'] = basins.get('5', 0) + 1
            # the tax-free inert lock: norm 25 = the IDEAL price p^(ef),
            # one tick per move, no flat part (a pure principal column)
            for (yx, fac, n, flat, nt) in tail:
                ok(n == 25 and flat == (), "(5)-tail move not a pure tick")
            # and the passenger never lifts: 2-depths stay at seed level
            ok(st.get(P2, 0) == seed.get(P2, 0)
               and st.get(P2c, 0) == seed.get(P2c, 0),
               "(5)-basin trajectory lifted a 2-passenger")
        for (yx, fac, n, flat, nt) in log:
            if len(fac) > 1 and flat:
                n_rider += 1
            if nt > 1:
                tie_moves += 1
    ok(basins == {'2': 38, '5': 3},
       "basin histogram moved: %s" % (basins,))
    # MR3: the void overture
    log, st, L = run_elem({}, Tm)
    norms = [n for (yx, fac, n, flat, nt) in log]
    ok(norms[:3] == [6, 6, 6] and set(norms[3:]) == {4},
       "MR3 void overture 6,6,6 then 4 forever (got %s)" % norms[:6])
    ok(log[0][4] == 2, "MR3 move 1 is the norm-6 Galois tie")
    ok(log[1][4] == 1 and log[2][4] == 1, "MR3 moves 2-3 unique")
    ok(elem_menu({}, 1)[0] == 6,
       "MR3 norm-4 not dead at birth (menu norm != 6)")
    # the myopia tax: the cube (2-w) = P2^3 offers 2/tick, never picked
    cube_fac = factor_elem(2, -1)
    ok(cube_fac in ({P2: 3}, {P2c: 3}), "the cube (2-w) is not a P2^3")
    d = max(st.get(P2, 0), st.get(P2c, 0))
    ok(lam_P(P2, d + 3) == 8 * lam_P(P2, d),
       "the cube from the tail depth is not 3 ticks")
    ok(all(fac not in ({P2: 3}, {P2c: 3})
           for (yx, fac, n, flat, nt) in log),
       "the cube was picked (no myopia tax?)")
    # MR6 REFUTED IN PART: the frozen path for seed (7) missed the
    # element sqrt(-23) door (norm 23, principal). The RUN's path:
    # two sqrt(-23) moves, THEN the frozen shape (cube at 27, 6-rides,
    # (2)-takeover). Asserted as observed:
    log7, st7, L7 = run_elem({('inert', 7): 1}, Tm)
    norms7 = [n for (yx, fac, n, flat, nt) in log7]
    ok(norms7[:3] == [23, 23, 27], "(7) opening (got %s)" % norms7[:3])
    k = 3
    while norms7[k] == 6:
        k += 1
    ok(k > 3 and set(norms7[k:]) == {4},
       "(7): rides then (2) forever (got %s)" % norms7[:k + 2])
    ok(log7[2][4] == 2, "(7) move 3 is the conjugate cube tie")
    ok(len(log7[2][1]) == 1, "(7) move 3 not a pure 3-cube")
    # the (5)-basin members: the seed's own dowry (24 = lambda(P5))
    # kills every door below 25 and its column is principal
    log5, st5, L5 = run_elem(five_move, Tm)
    norms5 = [n for (yx, fac, n, flat, nt) in log5]
    ok(norms5[:3] == [23, 23, 25] and set(norms5[3:]) == {25},
       "(5): two sqrt(-23) moves then the 25-lock (got %s)" % norms5[:5])
    print("s4 element census (%d seeds, T=%d): TWO BASINS %s — the "
          "monobasin is REFUTED at h=3 (frozen MR4 missed); %d rider "
          "moves; %d tie moves (all conjugation-closed)"
          % (len(seeds), Tm, sorted(basins.items()), n_rider, tie_moves))
    print("   void overture norms %s...; (7): %s...; (5): %s..."
          % (norms[:5], norms7[:9], norms5[:5]))
    print("   the myopia tax: the P2^3 cube (norm 8, 2/tick) exists and "
          "is never picked; the (2)-tail pays 4/tick = 2^min(ord,2);")
    print("   the (5)-tail pays 25 = q^e = the IDEAL price, tax-free "
          "(inert places are principal)")


def s5_galois():
    """Conj(seed) + flipped tie-break = conj(trajectory)."""
    Tm = 30
    for seed in [{}, {('inert', 7): 1}, {('split', 3, SPLIT_ROOT[3]): 2}]:
        cseed = {conj_place(pl): e for pl, e in seed.items()}
        log, _, _ = run_ideal(seed, Tm)
        clog, _, _ = run_ideal(cseed, Tm, flip=True)
        ok([(conj_place(pl), r, c, k, nt) for (pl, r, c, k, nt) in log]
           == clog, "ideal Galois equivariance")
    for seed_yx in [None, (1, 1), (2, 1)]:
        seed = {} if seed_yx is None else factor_elem(seed_yx[1], seed_yx[0])
        cseed = {conj_place(pl): e for pl, e in seed.items()}
        log, _, _ = run_elem(seed, Tm)
        clog, _, _ = run_elem(cseed, Tm, flip=True)
        ok([canon_elem(conj_elem(yx)) for (yx, fac, n, flat, nt) in log]
           == [yx for (yx, fac, n, flat, nt) in clog],
           "element Galois equivariance")
    print("s5 Galois equivariance: 3 ideal + 3 element seed pairs, "
          "trajectories conjugate move-by-move")


def s6_synthesis(lock_hist):
    print("s6 synthesis: THE MODULE LAW — fate and price read the local")
    print("   1-unit module: linear pump/lock/price p^rank in mixed char,")
    print("   log clock/sprawl in equal char (theorem, instances exact).")
    print("   Q(sqrt(-23)) h=3: ideal basins %s;" % sorted(lock_hist.items()))
    print("   element world TWO basins ((2) at 4, inert (5) at 25):")
    print("   the basin map is a norm race among the principal vehicles,")
    print("   the tail pays its 1-move vehicle p^min(fm,2) (P^m vs the")
    print("   rational (p)) — monobasins are field accidents, not an")
    print("   h>1 law, and the fm>2 tax is pure greedy myopia.")


def main():
    s1_local_law()
    s2_cross_gates()
    hist = s3_ideal_census()
    s4_element_census()
    s5_galois()
    s6_synthesis(hist)
    print("ALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
