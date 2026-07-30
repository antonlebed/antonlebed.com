"""explore_number_field_lock.py — the number-field lock.

THE QUESTION (an open remainder from explore_function_field_lock.py).
explore_function_field_lock.py proved the lock/sprawl split reads the
CHARACTERISTIC: Q locks (the lock-prime law, explore_lock_prime.py),
F_2[x] sprawls — but the mixed-characteristic side was instantiated at Q
only. THIS script runs cold D-DYN over O = Z[sqrt(-5)] (h = 2, Cl = C2) in
BOTH worlds:
  - the IDEAL world: states = integral ideals, move = least-NORM ideal
    m != (1) with lambda(I*m) > lambda(I) (lambda = exponent of (O/I)^*);
  - the ELEMENT world (explore_class_gap.py's mezzanine): states and moves
    PRINCIPAL.
Does every mixed-characteristic ring lock, and does the lock split
ideal-vs-element, reading the class group, the way the thermal clock
did (K2: element 1.3527 < ideal 1.5492)?

Predictions (fixed before the run): PR1-PR10, frozen and hand-attacked
before this script ran. FINDINGS below were written from the first
green run's output.

FINDINGS (tiers below; run record at bottom; all sections assert).

1. THE LOCK SURVIVES MIXED CHARACTERISTIC (rule in range; 54 ideal
   seeds x 40 moves: all ideals of norm 2..40 + the void + 2
   constructed seeds). Every ideal trajectory LOCKS — asserted in
   full: at most 2 pre-lock moves (census max wander), the first pick
   of the lock place is non-ghost, and every move after it deepens
   that place. Z's recurrence argument transfers: every place's own-prime
   pump is LINEAR in depth (finding 8), so a non-ghost pick prices its
   door at a constant while every rival door is nondecreasing. With
   explore_function_field_lock.py the characteristic dichotomy is now instantiated
   on BOTH sides: mixed characteristic locks (Q and K), equal
   characteristic sprawls (F_2[x]).

2. THE PRICE LAW — the lock price is p^(local degree) (rule in range;
   this script's own descent). Every locked trajectory's recurrent move
   cost is exactly p^(e*f) at the lock place (asserted on every
   censused trajectory): split 3-locks pay 3/move, split 23-locks 23,
   the ramified P5-lock pays 25 = 5^2 (one P5^2 move per lambda-tick,
   e = 2), 2-locks pay 4 = 2^2 in BOTH worlds. Since
   rank_{Z_p} U1(K_P) = e*f, the price IS the local 1-unit module
   rank: lock price = p^rank. The function-field sprawl is the same
   law's rank-infinity limit (Frobenius flattening makes the price
   diverge — no recurrent door). One law covers Q, K, F_q[x]; the
   general local-field statement landed in explore_module_law.py (the
   local module law proved, crystal + absorption, the cascade boundary
   named).

3. EVERY TIE IS A GALOIS ORBIT (rule in range: 21 ideal + 16 element
   tie moves, every tie set asserted a conjugate pair at equal r;
   equivariance verified on 3 ideal + 3 element seed pairs,
   conj(seed) + flipped tie-break = conj(trajectory) move by move).
   Door costs are prime powers of distinct rational primes — distinct
   integers, Z's determinism argument — EXCEPT at conjugate places,
   which share every door price by lambda-symmetry. So the only
   nondeterminism mixed characteristic admits is the Galois symmetry
   itself, and the greedy must spontaneously break it (the void's
   first move: P3 vs P3'). Locks are defined up to conjugacy.
   (Settled since, by explore_greedy_image_nf.py: in the IDEAL world
   this is a proof and not a census — a door costs N(place)^r, always
   a power of its rational prime, so equal costs lie over one rational
   prime and only a split prime carries two places — while the ELEMENT
   world keeps it as a measurement, a bundle being able to straddle two
   rational primes. And the per-MOVE statement does not lift to the
   trajectory: two independent conjugate ties compose into four limits,
   more than the group has elements, so the set of reachable limits is
   an orbit only when at most one tie fires.)
   explore_function_field_lock.py's "determinism is archimedean"
   sharpens: the greedy RULE
   is complete (no tie-break clause needed) over Q alone — a
   tie-break is required exactly when distinct moves can share a
   cost, split pairs supply such pairs, and every number field K != Q
   has split primes (Chebotarev); at K the void itself already ties.
   Determinism is a RATIONAL accident, not just an archimedean one.

4. THE GHOST RETURNS, CLASS-FIELD-EDITED (rule for the mechanism;
   specimen + census). F_2[x]'s type separation emptied the ghost
   class (explore_function_field_lock.py); mixed characteristic
   restores it — state residue
   chars and lambda share Z again. Specimen (frozen PR4): seed P29
   (lambda = 28) opens Q7 at cost 7 with 7 | 28 — a ghost, Galois-tied
   with Q7'; its dowry (lambda -> 84) lifts the 3-door from 9 to 27,
   and the fresh norm-23 pair locks instead (ghost -> fresh -> lock,
   Z's wander in ideal dress; PR5a). THE EDIT (proved): a 5-ghost
   needs 5 | lambda with 4 not| lambda — impossible in K, because
   every 5-carrier drags 4 in: split p = 1 mod 5 is chi20-gated to
   p = 1, 9 mod 20 (so 4 | p-1), inert q gives 8 | q^2-1, and P5's own
   column carries 4. Census: ghosts fire at char 7 only. The Fermat-
   gate mechanism reaches the ghost spectrum: class field
   theory edits which hauntings are possible. (Z has 5-ghosts: seed
   11, explore_lock_prime.py finding 5.)

5. THE LOCK SPLITS BY THE CLASS GROUP (the headline; rule in range).
   The IDEAL void locks a norm-3 place at 3/move — Z's void column
   (lock 3, explore_lock_prime.py finding 6) verbatim, up to the new
   Galois tie. The
   ELEMENT void locks (2) = P2^2 at 4/move, via the frozen overture
   (2), (2), the conjugate norm-9 tie (2 +- sqrt-5) = a P3-conjugate
   squared, THE FREE-RIDER DOOR (norm 6: the ticking nonprincipal
   3-place bundled with a FLAT P2 — Z's door lemma DIES at h > 1: the
   minimal principal move need not be a prime power), then (2)
   forever. Mechanism: the cheapest ideal seat (split 3, price 3) is
   nonprincipal, so the element world pays its class-order tax (P3^2
   at 9, riders at 6) — while P2's tax is REFUNDED by the resonance
   ord[P2] = e = 2: the forced bundle (2) = P2^2 is exactly one
   lambda-tick, price 4 = the ideal price. The thermal clock split
   (K2: element 1.3527 < ideal 1.5492) is this cold asymmetry's
   thermal shadow.

6. THE MONOBASIN — the class group collapses the element basin map
   (observation, 42/42 element seeds all (2)-lock; mechanism proved in
   part; FIELD GEOGRAPHY, not an h > 1 law — Q(sqrt(-23)) has two
   element basins, explore_module_law.py finding 3). The ideal world keeps Z-like basin geography (locks at 2,
   3, 7, 23 in the norm-40 belt, plus the constructed ramified
   5-lock), the element world has ONE basin. No
   principal ideal has norm 2 or 3, so (2) at 4 is the cheapest
   possible recurrent door (the principal P5 door at 5 ticks only
   every other depth — never recurrent below 25); the only cheap
   vehicle for a NONPRINCIPAL column is the free-rider bundle at 6,
   and every rider FEEDS the P2 column it rides (+1 depth per move;
   all 144 censused rider moves are P2-flat at ride time) until the
   wild 2-clock regularizes and (2) absorbs the trajectory. The rider
   pays Charon: the bundling that makes nonprincipal doors cheap
   ferries the 2-column to its regular regime.

7. THE WILD SEAT HOLDS ONLY FROM DEPTH (rule in range; the (2, 1)
   census entry was unfrozen — found by the census, assert added
   after). Ideal seed (2) = P2^2 grabs its own norm-2 door once
   (j 2->3), lands in the wild chain's flat window (lambda = 4 for
   j = 3..6), and loses the lock to fresh Q7 at 7 — greedy myopia
   parks it at the worst spot (PR6). But seed P2^5, born PAST the
   window, locks 2 at 4/move from move 1: the wild seat can't hold
   what it grabs shallow, yet holds what it is given deep. The 2-adic
   seat — thermal max of every clock spectrum — is
   cold-dynamically fragile in the ideal world and universal in the
   element world (finding 6): the seat law's cold fate splits by
   world, both readings through the same wild chain.

8. THE FOUR PUMP SHAPES (rule, brute-verified over full unit grids).
   lambda(P2^j) = 1, 2, 4, 4 then 2^floor((j-1)/2) from j = 5 (chain
   j = 1..13: 1,2,4,4,4,4,8,8,16,16,32,32,64 — PR10's predicted
   16,32,32,64 at j = 10..13 all hit); split lambda(P^a) =
   (p-1)p^(a-1) (O/P^a = Z/p^a, completion); inert (q^2-1)q^(a-1);
   ramified-tame lambda(P5^j) = 4*5^floor(j/2) (j <= 6:
   4,20,20,100,100,500). All four are LINEAR pumps in depth — the
   mixed-characteristic signature (contrast the Frobenius log pump,
   explore_function_field_lock.py finding 4) — differing only in tick
   spacing e and coin p^f,
   which is exactly what the price law reads (finding 2).

Run: `python explore_number_field_lock.py`. RUN RECORD (27273 checks,
~1.0 s): s1 lambda laws brute over full unit grids (P2 j <= 13, P5
j <= 6, split p in {3, 7, 23, 29, 43, 89} both conjugates, inert
{11, 13}) — all exact. s2 independent lattice brute: 14 engine moves
(void m1-2, (2) m1-3, (4) m1-2, P29 m1-2, element void m1-5) = full
grid-scan ground truth (all_ideals lattice-closure enumeration +
u^lambda unit tests); 41 element factorizations lattice-exact.
s3 ideal census 54 seeds x T = 40 with EVERY move re-verified by the
norm-<=cost product scan (PR1: no cheaper ticking ideal, min-cost
tickers = the menu's prime-power ties): ALL LOCK; lock chars
{2: 1, 3: 26, 5: 1, 7: 23, 23: 3}; ghosts {7: 3 fires}, no 5-ghost;
21 tie moves, each asserted a conjugate pair at equal r; max wander 2;
price law exact on
every trajectory. Void: P3-tie -> 3/move. P29: ghost Q7 (7) -> fresh
P23-tie (23) -> 23-lock. P89*P43: immediate P5^2 -> 25/move (THE
RAMIFIED LOCK, PR5b). P2^5 -> 2-lock at 4/move (unfrozen). s4 element
census 42 seeds x 40: ALL (2)-lock; void overture norms 4, 4, 9-tie,
6-rider, then 4 forever (PR7/PR8); 144 rider moves, every one P2-flat;
16 tie moves, each asserted a conjugate pair. s5 Galois equivariance 3 + 3 seed
pairs. Slate PR1-PR10 (PR5 corrected before the run): all hit; no
misses; unfrozen finds: the P2^5 deep-seed 2-lock, the census
histograms.
"""

import sys, os
from math import gcd, isqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_irreducibility_crossfield import (  # guarded module (lineage)
    ideal_from_gens, ideal_mul, ideal_pow, ideal_norm, qmul)

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


# ------------------------------------------------------------------ places
# K = Q(sqrt(-5)), O = Z[t], t^2 = -5. Place keys:
#   ('ram', 2)        P2 = (2, 1+t), e=2 f=1, wild, NONPRINCIPAL
#   ('ram', 5)        P5 = (t),      e=2 f=1, tame, PRINCIPAL
#   ('split', p, r)   P = (p, t - r), r^2 = -5 mod p; conjugate root p - r
#   ('inert', q)      (q), f=2, principal
MAXP = 2000


def _sieve(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(2, n + 1) if s[i]]


PRIMES = _sieve(MAXP)
SPLIT_ROOT = {}  # p -> least root of r^2 = -5 mod p


def place_norm(pl):
    return pl[1] * pl[1] if pl[0] == 'inert' else pl[1]


def place_char(pl):
    return pl[1]


def place_ef(pl):
    return 1 if pl[0] == 'split' else 2  # inert f=2; ramified e=2


def place_bit(pl):  # genus class bit: 1 = nonprincipal
    if pl[0] == 'split':
        return 1 if pl[1] % 20 in (3, 7) else 0
    return 1 if pl == ('ram', 2) else 0


def place_key(pl):
    return (place_norm(pl), pl[2] if pl[0] == 'split' else 0)


def conj_place(pl):
    if pl[0] == 'split':
        return ('split', pl[1], pl[1] - pl[2])
    return pl


def build_universe():
    places = [('ram', 2), ('ram', 5)]
    for p in PRIMES:
        if p in (2, 5):
            continue
        rts = [r for r in range(1, p) if (r * r + 5) % p == 0]
        if rts:
            SPLIT_ROOT[p] = rts[0]
            places.append(('split', p, rts[0]))
            places.append(('split', p, rts[1]))
        elif p * p <= MAXP:
            places.append(('inert', p))
    places.sort(key=place_key)
    return places


UNIVERSE = build_universe()

RAM2_TABLE = (1, 2, 4, 4)


def lam_P(pl, a):
    """lambda of the prime-power column P^a (laws brute-verified in s1)."""
    if a == 0:
        return 1
    k, p = pl[0], pl[1]
    if k == 'split':
        return (p - 1) * p ** (a - 1)
    if k == 'inert':
        return (p * p - 1) * p ** (a - 1)
    if p == 5:
        return 4 * 5 ** (a // 2)
    return RAM2_TABLE[a - 1] if a <= 4 else 2 ** ((a - 1) // 2)


def lam_state(st):
    L = 1
    for pl, e in st.items():
        L = lcm(L, lam_P(pl, e))
    return L


def place_hnf(pl):
    k, p = pl[0], pl[1]
    if k == 'split':
        return ideal_from_gens([(p, 0), (-pl[2], 1)])
    if k == 'inert':
        return ideal_from_gens([(p, 0)])
    if p == 5:
        return ideal_from_gens([(0, 1)])
    return ideal_from_gens([(2, 0), (1, 1)])


# --------------------------------------------------------- the ideal engine
def door_r(pl, e, L):
    r = 1
    while L % lam_P(pl, e + r) == 0:
        r += 1
        assert r < 500, "door search runaway"
    return r


def ideal_menu(st, L):
    """(cost, ties): ties = all min-cost (place, r), sorted by place_key."""
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


# PR1 verification: full product scan at every census move
SCAN_CAP = 200
_scan_cache = {}


def gen_products(maxnorm):
    """All nontrivial place-power products of norm <= maxnorm."""
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
    """PR1: no ideal of norm < cost ticks; the norm-cost tickers = ties."""
    at_cost = set()
    for nrm, m in gen_products(cost):
        L2 = L
        for pl, e in m.items():
            L2 = lcm(L2, lam_P(pl, st.get(pl, 0) + e))
        tick = L2 > L
        if nrm < cost:
            ok(not tick, "PR1 cheaper ticking ideal at norm %d" % nrm)
        elif tick:
            ok(len(m) == 1, "PR1 min-cost ticking ideal not a prime power")
            (pl, e), = m.items()
            at_cost.add((pl, e))
    ok(at_cost == set(ties), "PR1 scan ties != menu ties")


def run_ideal(seed, T, flip=False, scan=False):
    st, L = dict(seed), lam_state(seed)
    log = []
    for _ in range(T):
        cost, ties = ideal_menu(st, L)
        if scan:
            ok(cost <= SCAN_CAP, "census door above scan cap")
            scan_check(st, L, cost, ties)
        if flip:
            pl, r = min(ties, key=lambda t: place_key(conj_place(t[0])))
        else:
            pl, r = ties[0]
        kind = classify(st, L, pl, r)
        st[pl] = st.get(pl, 0) + r
        L2 = lam_state(st)
        ok(L2 > L, "chosen move grows lambda")
        log.append((pl, r, cost, kind, len(ties)))
        L = L2
    return log, st, L


# -------------------------------------------------------- the element engine
def elem_candidates(n):
    """Canonical reps (y, x) of norm n (units {+-1}: y > 0, or y=0, x >= 2)."""
    out = []
    y = 0
    while 5 * y * y <= n:
        rem = n - 5 * y * y
        x = isqrt(rem)
        if x * x == rem:
            if y == 0:
                if x >= 2:
                    out.append((0, x))
            elif x == 0:
                out.append((y, 0))
            else:
                out.append((y, -x))
                out.append((y, x))
        y += 1
    return sorted(out)


def factor_elem(x, y):
    """Place factorization of the principal ideal (x + y t)."""
    n = x * x + 5 * y * y
    assert n > 1
    fac = {}
    for p in prime_divisors(n):
        v = v_p(n, p)
        if p == 2 or p == 5:
            fac[('ram', p)] = v
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
                    assert (xx + yy * (p - r)) % p == 0, "split valuation"
                    e1 += rem
            if e0:
                fac[('split', p, r)] = e0
            if e1:
                fac[('split', p, p - r)] = e1
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
    return (y, -x) if x != 0 and y != 0 else yx


def elem_menu(st, L, nmax=2000):
    """(norm, hits): hits = [((y,x), fac)] for ALL ticking elements at the
    least ticking norm, in canonical (y, x) order."""
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


def run_elem(seed, T, flip=False):
    st, L = dict(seed), lam_state(seed)
    ok(sum(place_bit(pl) * e for pl, e in st.items()) % 2 == 0,
       "element seed not principal")
    log = []
    for _ in range(T):
        n, hits = elem_menu(st, L)
        if flip:
            tgt = min(conj_elem(h[0]) for h in hits)
            (yx, fac), = [h for h in hits if conj_elem(h[0]) == tgt]
        else:
            yx, fac = hits[0]
        # rider structure: which factor places tick / ride flat
        flat = [pl for pl, e in fac.items()
                if L % lam_P(pl, st.get(pl, 0) + e) == 0]
        for pl, e in fac.items():
            st[pl] = st.get(pl, 0) + e
        L2 = lam_state(st)
        ok(L2 > L, "element move grows lambda")
        ok(sum(place_bit(pl) * e for pl, e in st.items()) % 2 == 0,
           "element state left the principal class")
        log.append((yx, fac, n, tuple(flat), len(hits)))
        L = L2
    return log, st, L


# ------------------------------------- independent brute (lattice arithmetic)
def mem(B, x, y):
    n1, s, n2 = B
    return y % n2 == 0 and (x - (y // n2) * s) % n1 == 0


def ideal_contains(B, A):
    return mem(B, A[0], 0) and mem(B, A[1], A[2])


def all_ideals(B):
    """Every integral ideal of norm <= B, by direct lattice closure —
    independent of the place machinery."""
    out = []
    for n2 in range(1, B + 1):
        n1 = n2
        while n1 * n2 <= B:
            for s in range(n1):
                L = (n1, s, n2)
                if mem(L, 0, n1) and mem(L, -5 * n2, s):
                    out.append(L)
            n1 += n2
    out.sort(key=lambda A: (ideal_norm(A), A))
    return out


def qpow(A, u, e):
    r, b = (1, 0), u
    while e:
        if e & 1:
            r = qmul(A, r, b)
        b = qmul(A, b, b)
        e >>= 1
    return r


def brute_tick(Ihnf, mhnf, L):
    """Ground truth: lambda(I*m) > L? (L = lambda(I), which divides
    lambda(I*m): units reduce onto units.) Unit screen by place membership."""
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


def lam_pp_brute(pl, a):
    """Brute exponent of (O/P^a)^* over the full unit grid."""
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


def factor_hnf(A):
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
    ok(nn == ideal_norm(A), "factor_hnf norm mismatch")
    return fac


# ================================================================== sections
def s1_lambda_laws():
    """PR10 + all four pump shapes vs the full-grid brute."""
    chain2 = [lam_pp_brute(('ram', 2), j) for j in range(1, 14)]
    for j, got in enumerate(chain2, 1):
        ok(got == lam_P(('ram', 2), j),
           "PR10 wild law at j=%d: brute %d != law %d"
           % (j, got, lam_P(('ram', 2), j)))
    chain5 = [lam_pp_brute(('ram', 5), j) for j in range(1, 7)]
    for j, got in enumerate(chain5, 1):
        ok(got == lam_P(('ram', 5), j), "tame ram law at j=%d" % j)
    for p, amax in ((3, 4), (7, 3), (23, 1), (29, 1), (43, 1), (89, 1)):
        for r in (SPLIT_ROOT[p], p - SPLIT_ROOT[p]):
            for a in range(1, amax + 1):
                ok(lam_pp_brute(('split', p, r), a)
                   == (p - 1) * p ** (a - 1), "split law p=%d a=%d" % (p, a))
    for q in (11, 13):
        ok(lam_pp_brute(('inert', q), 1) == q * q - 1, "inert law q=%d" % q)
    print("s1 lambda laws: P2 chain j=1..13 =", chain2)
    print("   P5 chain j=1..6 =", chain5,
          "; split/inert laws exact in brute range")


def s2_door_brute():
    """Independent grid-brute: engine menu = full norm-order scan."""
    r29 = SPLIT_ROOT[29]
    ideal_states = [
        ({}, 2), ({('ram', 2): 2}, 3), ({('ram', 2): 4}, 2),
        ({('split', 29, r29): 1}, 2),
    ]
    pool = all_ideals(40)
    n_states = 0
    for seed, nmoves in ideal_states:
        st, L = dict(seed), lam_state(seed)
        for _ in range(nmoves):
            cost, ties = ideal_menu(st, L)
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
            n_states += 1
    # element world: the void's first 5 moves against the element scan
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
        n_states += 1
    # cross-gate: element factorization = lattice arithmetic, norms <= 60
    n_fac = 0
    for nn in range(2, 61):
        for (y, x) in elem_candidates(nn):
            fac = factor_elem(x, y)
            ok(state_hnf(fac) == ideal_from_gens([(x, y)]),
               "factor_elem != lattice ideal at (%d,%d)" % (x, y))
            n_fac += 1
    print("s2 independent brute: %d engine moves = grid scan; "
          "%d element factorizations lattice-exact" % (n_states, n_fac))


def lock_of(log, tail):
    moves = log[-tail:]
    pl0 = moves[0][0]
    if all(pl == pl0 and kind == 'deepen'
           for (pl, r, c, kind, nt) in moves):
        return pl0
    return None


def s3_ideal_census():
    """PR2/PR4/PR5a/PR5b/PR6: the ideal world locks, Z-style geography."""
    T = 40
    seeds = []
    for A in all_ideals(40):
        if ideal_norm(A) >= 2:
            seeds.append(factor_hnf(A))
    r29, r43, r89 = SPLIT_ROOT[29], SPLIT_ROOT[43], SPLIT_ROOT[89]
    extra = [{}, {('split', 29, r29): 1},
             {('split', 89, r89): 1, ('split', 43, r43): 1}]
    lock_hist, ghost_chars, tie_moves, wander_max = {}, {}, 0, 0
    for seed in extra + seeds:
        log, st, L = run_ideal(seed, T, scan=True)
        pl = lock_of(log, 25)
        ok(pl is not None, "PR2 a census trajectory failed to lock")
        p = place_char(pl)
        lock_hist[p] = lock_hist.get(p, 0) + 1
        # the price law: recurrent cost = p^(e*f)
        for (mpl, r, c, kind, nt) in log[-25:]:
            ok(c == p ** place_ef(pl), "price law: %d != %d^%d"
               % (c, p, place_ef(pl)))
        # wander = moves before the first pick of the lock place; the lock
        # criterion: the first pick is non-ghost and NOTHING follows but
        # deepenings of the same place (not only the asserted tail)
        w = next(i for i, mv in enumerate(log) if mv[0] == pl)
        wander_max = max(wander_max, w)
        ok(log[w][3] != 'ghost', "lock place entered by a ghost")
        ok(all(mv[0] == pl and mv[3] == 'deepen' for mv in log[w + 1:]),
           "a move after the first lock-place pick left the column")
        for (mpl, r, c, kind, nt) in log:
            if kind == 'ghost':
                ghost_chars[place_char(mpl)] = \
                    ghost_chars.get(place_char(mpl), 0) + 1
                ok(place_char(mpl) != 5, "a 5-ghost fired (chi20 edit)")
            if nt > 1:
                tie_moves += 1
                ok(nt == 2, "tie set larger than a Galois pair")
    # every tie is a Galois orbit: replay each census menu and check the
    # tie places are conjugates at the same r (same rational prime forced)
    for seed in extra + seeds:
        st, L = dict(seed), lam_state(seed)
        for _ in range(T):
            cost, ties = ideal_menu(st, L)
            if len(ties) == 2:
                (p0, r0), (p1, r1) = ties
                ok(conj_place(p0) == p1 and r0 == r1,
                   "ideal tie not a conjugate pair at equal r")
            pl, r = ties[0]
            st[pl] = st.get(pl, 0) + r
            L = lam_state(st)
    # the void: Z's column verbatim
    log, st, L = run_ideal({}, T)
    ok(log[0][4] == 2, "PR2 the void's first move is the P3/P3' tie")
    ok(all(place_char(mv[0]) == 3 and mv[2] == 3 for mv in log),
       "PR2 void locks a norm-3 place at 3/move")
    # PR4 + PR5a: seed P29
    log, st, L = run_ideal({('split', 29, r29): 1}, T)
    ok(log[0][3] == 'ghost' and log[0][2] == 7 and log[0][4] == 2,
       "PR4 P29's first move is the tied Q7 ghost")
    ok(log[1][3] == 'fresh' and log[1][2] == 23 and log[1][4] == 2,
       "PR5a move 2 is the fresh norm-23 tie")
    ok(place_char(lock_of(log, 25)) == 23, "PR5a P29 locks 23")
    # PR5b: the ramified lock
    log, st, L = run_ideal({('split', 89, r89): 1, ('split', 43, r43): 1}, T)
    ok(place_char(lock_of(log, 25)) == 5 and log[-1][2] == 25,
       "PR5b P89*P43 locks P5 at 25/move")
    ok(all(mv[2] == 25 for mv in log), "PR5b every move is P5^2 at 25")
    # PR6: the wild seat can't hold what it grabs shallow...
    log, st, L = run_ideal({('ram', 2): 2}, T)
    ok(log[0][0] == ('ram', 2) and log[0][2] == 2,
       "PR6 seed (2) grabs its own norm-2 door")
    ok(place_char(lock_of(log, 25)) == 7, "PR6 seed (2) locks 7")
    # ...but HOLDS from the regular regime (unfrozen; found by the census)
    log, st, L = run_ideal({('ram', 2): 5}, T)
    ok(place_char(lock_of(log, 25)) == 2 and all(mv[2] == 4 for mv in log),
       "seed P2^5 locks 2 at 4/move from move 1")
    ok(5 not in ghost_chars, "no 5-ghost across the census")
    print("s3 ideal census (%d seeds, T=%d): ALL LOCK; lock chars %s"
          % (len(extra + seeds), T, sorted(lock_hist.items())))
    print("   ghosts by char %s; tie moves %d (all Galois pairs); "
          "max wander %d" % (sorted(ghost_chars.items()), tie_moves,
                             wander_max))
    return lock_hist


def s4_element_census():
    """PR7/PR8/PR9: free-rider doors, the void's 2-lock, THE MONOBASIN."""
    T = 40
    seeds = [{}]
    for nn in range(2, 61):
        for (y, x) in elem_candidates(nn):
            seeds.append(factor_elem(x, y))
    n_rider = 0
    tie_moves = 0
    for seed in seeds:
        log, st, L = run_elem(seed, T)
        tail = log[-25:]
        ok(all(fac == {('ram', 2): 2} and n == 4
               for (yx, fac, n, flat, nt) in tail),
           "PR9 MONOBASIN: a trajectory did not (2)-lock")
        for (yx, fac, n, flat, nt) in log:
            if len(fac) > 1:
                n_rider += 1
                ok(('ram', 2) in fac, "a bundle without the P2 rider")
                ok(('ram', 2) in flat, "rider move with a ticking P2 part")
            if nt > 1:
                tie_moves += 1
                ok(nt == 2, "element tie beyond a conjugate pair")
    # element ties are conjugate element pairs: replay the menus
    for seed in seeds:
        st, L = dict(seed), lam_state(seed)
        for _ in range(T):
            n, hits = elem_menu(st, L)
            if len(hits) == 2:
                ok(conj_elem(hits[0][0]) == hits[1][0],
                   "element tie not a conjugate pair")
            yx, fac = hits[0]
            for pl, e in fac.items():
                st[pl] = st.get(pl, 0) + e
            L = lam_state(st)
    # the void overture, frozen (PR7/PR8)
    log, st, L = run_elem({}, T)
    norms = [n for (yx, fac, n, flat, nt) in log]
    ok(norms[:4] == [4, 4, 9, 6] and set(norms[4:]) == {4},
       "PR8 void overture 4,4,9,6 then (2) forever (got %s)" % norms[:6])
    ok(log[2][4] == 2, "PR7 move 3 is the conjugate norm-9 tie")
    ok(len(log[3][1]) == 2 and ('ram', 2) in log[3][3],
       "PR7 move 4 is the free-rider bundle (P2 flat)")
    print("s4 element census (%d seeds, T=%d): ALL (2)-LOCK (monobasin); "
          "%d rider moves (every rider P2-flat); %d tie moves "
          "(all conjugate pairs)" % (len(seeds), T, n_rider, tie_moves))
    print("   void overture: norms %s..." % norms[:6])


def s5_galois():
    """PR3: conj(seed) + flipped tie-break = conj(trajectory)."""
    T = 30
    r29 = SPLIT_ROOT[29]
    for seed in [{}, {('split', 29, r29): 1}, {('ram', 2): 2}]:
        cseed = {conj_place(pl): e for pl, e in seed.items()}
        log, _, _ = run_ideal(seed, T)
        clog, _, _ = run_ideal(cseed, T, flip=True)
        ok([(conj_place(pl), r, c, k, nt) for (pl, r, c, k, nt) in log]
           == clog, "ideal Galois equivariance")
    for seed_yx in [None, (2, 3), (1, 0)]:
        seed = {} if seed_yx is None else factor_elem(seed_yx[1], seed_yx[0])
        cseed = {conj_place(pl): e for pl, e in seed.items()}
        log, _, _ = run_elem(seed, T)
        clog, _, _ = run_elem(cseed, T, flip=True)
        ok([conj_elem(yx) for (yx, fac, n, flat, nt) in log]
           == [yx for (yx, fac, n, flat, nt) in clog],
           "element Galois equivariance")
    print("s5 Galois equivariance: 3 ideal + 3 element seed pairs, "
          "trajectories conjugate move-by-move")


def s6_synthesis(lock_hist):
    print("s6 synthesis: the price law p^(ef) per move -- split 3-lock 3, "
          "split 23-lock 23,")
    print("   ramified 5-lock 25, element 2-lock 4 (= ideal price: the "
          "class tax refunded)")
    print("   ideal basins %s vs element MONOBASIN {2}" %
          sorted(lock_hist.items()))


def main():
    s1_lambda_laws()
    s2_door_brute()
    hist = s3_ideal_census()
    s4_element_census()
    s5_galois()
    s6_synthesis(hist)
    print("ALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
