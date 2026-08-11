r"""explore_gaussian_runaway.py — the ramified runaway, hunted at Z[i].

THE QUESTION. The mixed-universe law prices a place by its recurrent
PRODUCT — a norm raised to that place's own tail gap — and the smallest
product takes the recurrent slot (explore_tick_pump.py F9). Every ring
walked so far puts its ramified places out of the running: at Z[sqrt(-5)]
the wild place over 2 has product 4 against a split lock at 3, and at
Z[w] (w^2 = w - 6) the ramified place over 23 has product 529 against a
split lock at 3. So the corpus has never seen a runaway that was not an
unramified place, and explore_tick_pump.py F11 files that as a ring's own
reading of the mixed law.

Z[i] INVERTS THE ORDERING. There 2 ramifies with norm 2 and e = 2, so its
product is 4, while the least UNRAMIFIED norm is 5 — split primes are
1 mod 4 and inert ones square. So the mixed law predicts the ramified
place takes the recurrent slot, and with it a limit whose deep coordinate
sits at a ramified place, the first the corpus would have.

TWO TRANSPLANTS, both flagged before the run. (T1) The suspicion is
written in the SYNTHETIC cell's vocabulary, where a ladder is a
parameter and has no head; a ring has heads, at exactly the places
explore_tick_pump.py F1 files (p - 1 <= e). (T2) It is
carried from two rings where the ramified place loses to a ring where
the product ordering flips, and only the ordering was checked.

THE DESIGN, and why it is a module rather than an engine. The two ring
engines are hardcoded — explore_number_field_lock.py fixes t^2 = -5 in
its place enumeration, its genus bit and its ramified tables, and
explore_module_law.py fixes w^2 = w - 6 the same way — so there is no
discriminant to turn. But the WALKER above them is already generic:
explore_lock_budget.py's step_once / walk_to_lock and
explore_tick_pump.py's ring_walk take a ring MODULE and touch it only
through UNIVERSE, place_norm, place_key, lam_P, lam_state, door_r and
ideal_menu. So Z[i] enters as a module of seven names and the walk that
reads it is IMPORTED — no result below comes from code written to
produce it.

THE HAND-ATTACK, on paper before this file existed, and it overturns the
naive reading. The residue field at (1+i) is F_2, so every unit is a
1-unit and |(O/P^n)^*| = 2^(n-1). Now i lies in U_1 \ U_2 (v(i-1) = 1)
and -1 in U_2 \ U_3 (v(-2) = 2), so U_1 = mu_4 x U_3 with U_3 free of
rank 2, and squaring carries U_a to U_(a+2) for a > e/(p-1) = 2. Hence

    lambda(P^n) = max(4, 2^ceil((n-3)/2))   for n >= 3,

a PLATEAU five depths wide (n = 3..7) before the tail gap of 2 begins.
The same method run at Z[sqrt(-5)]'s wild place, whose local field holds
only mu_2, reproduces the door sequence 1,1,4,3,2,1,2,1 that
explore_tick_pump.py F1 already publishes — a sequence it was not fitted
to, which is why the method is trusted this far and no further.

Read against the engine's own door — the least r with lambda(P^(e+r)) not
dividing the state's invariant, priced N(P)^r — the plateau makes the
walk's third move at the wild place cost 32. That is the whole question:
the product law prices the TAIL, and a walk that cannot cross the HEAD
never reaches it.

PREDICTIONS, fixed before the run and stated as observables.
  PR1  The void walk locks, and its recurrent vehicle is the INERT place
       of norm 9, at cost 9 — not the ramified place and not the least
       unramified norm.
  PR2  The wild place is SEATED from the void and ends at exponent
       exactly 3, which no ring in the corpus has done.
  PR3  Its price at the locked state is strictly above the lock's, so it
       is a strand rather than a snapshot.
  PR4  lambda(P^n) brute-forced from the actual unit group of O/P^n
       equals max(4, 2^ceil((n-3)/2)) at n = 3..12.
  PR5  The wild plateau at Z[i] is strictly WIDER than at Z[sqrt(-5)].
       (The width is the observable. Whether the local p-power torsion
       sets it is a reading to be weighed after the run, not a
       prediction — the two rings' plateaux were derived by different
       routes and only one of them from the torsion.)
  PR6  The mixed law's min over products is 4, at the ramified place,
       and the walk's recurrent cost is 9. Law and walk DISAGREE.

KILL-SHAPES, as observables.
  K1  the walk locks on the ramified place at cost 4 — the product law
      is right, the head was crossable, and the corpus has its ramified
      runaway.
  K2  the walk locks on the split place of norm 5 at cost 5 — the
      least-unramified-norm reading is right and the inert place is a
      distraction.
  K3  the brute-forced lambda disagrees with the closed form — the hand
      derivation is wrong and everything resting on it falls.

DISTRUST THE MARGIN. The derived half is the plateau formula. The VIBES
half is "nothing cheaper than 4 exists at the void", which rests on Z[i]
having no place of norm 3 or 4 — checked by scanning the whole universe
in S2, never asserted.

THE POSITIVE CONTROL (S1, run before any verdict is read). One generic
brute-forcer over quadratic orders t^2 = T*t + N0 enumerates O/I from an
HNF basis, keeps the units, and takes the exponent of the group. It is
run first against the two rings whose ramified and unramified tables are
already filed and independently written — Z[sqrt(-5)] and Z[w] — and
only then against Z[i]. A forcer that reproduces two tables it did not
write is the instrument; a forcer that does not is the finding.

FINDINGS (tiers below; run record at bottom; all sections assert).

1. THE PRODUCT LAW PRICES THE TAIL AND THE WALK PAYS THE HEAD — the
   ramified runaway does not happen, and the ordering was never the
   reason (rule in range; the void walk plus the whole universe of norm
   <= 30 scanned at every state). Z[i] does invert the ordering exactly
   as designed: the ramified place's product is 4 against a least
   unramified 5, and the law seats it. The walk locks on the INERT place
   of norm 9 at cost 9 — neither the ramified place nor the least
   unramified norm — in 12 steps, at the support R2^3 * Q3^50. K1 and K2
   both missed, and the miss is the finding: N^gap prices a place's
   PERIODIC TAIL, and the walk pays whatever the place charges at the
   depth it has actually reached.

2. THE FIRST RING TO SEAT A RAMIFIED PLACE FROM THE VOID, AND IT STRANDS
   THERE (rule in range; same walk). explore_tick_pump.py F11 records
   that no ramified place is seated at all in either ring's void walk.
   Here the void's CHEAPEST opening is the ramified place, at 4 — the
   universe scan shows why, Z[i] having no place of norm 3 or 4 at all —
   and the walk takes it (r = 2, cost 4), then takes its ONE CHEAP MOVE
   (r = 1, cost 2), reaching exponent 3 before the ladder shuts. That
   cheap move is not this rig's observation: explore_tick_pump.py F9's
   hand-attack correction already derives that a wide item's door is 1
   exactly ONCE, an item's reachable depths missing every member of its
   own ladder after the first step. This is that law's first instance in
   arithmetic rather than in a cell, and it is what makes the seating
   possible at all. At the locked state its door is 7
   and its price 128 against a lock at 9, so it is a strand and not a
   snapshot. (That 7 is worth more than this section made of it --
   explore_headed_ladder.py F9: the LONE-place door at exponent 3 is 5, so
   this state WIDENS the door, which explore_tick_pump.py F11 reports never
   happening at 472 readings over the two rings it walks. The carrier is
   the lock itself: the inert place over 3 has residue field F_9, so its
   lambda carries q - 1 = 8, and that 2-part covers the two depths the
   place over 2 would otherwise have escaped at.)
   F11's "never seats" was two rings' geography; what survives
   is the STRAND, which now has a third instance and the first that
   nobody planted — first among the rings that HAVE ramified places,
   which is the three number rings and not the function fields, whose
   engines carry no such place kind.
   THE "ONLY AS THE CHEAPEST OPENING" IS A COUNT OF THREE, not a proof,
   and half of it is argued: an UNSEATED place's door is nondecreasing
   as the walk's invariant grows (door_r is the least r whose lambda
   escapes an LCM that only gains divisors), so a place that loses the
   opening never gets cheaper in absolute terms. What is NOT argued is
   that the menu's own minimum cannot rise past it later — at Z[i] the
   lock's 9 is well above the void's cheapest 4, so that gap is real and
   the rule is a measurement. (SETTLED SINCE, explore_late_seating.py:
   the missing half is a winner-kind dichotomy — proved where the void's
   winner is split or inert of odd norm, and genuinely FALSE where it is
   ramified,
   Z[sqrt(-30)] seating a second ramified place from the void at step 3.
   What survives here is Z[i]'s own record: one ram, seated first.)

3. THE HEAD IS A FILED OBJECT AND ITS WIDTH IS NOT — and the width is
   what the walk cannot buy (rule in range; the ladder brute-forced from
   the actual unit groups to depth 12, tabulated to 14, over every place
   of small residue characteristic in three rings). WHAT IS ALREADY
   FILED, and this rig only re-instances it: explore_tick_pump.py F1
   records that a head — leading depths whose gap exceeds the tail's —
   sits at exactly the places with p - 1 <= e, at 90 of 90, because
   below e/(p-1) the principal units are still SQUARING and above it
   STEPPING by e. So a head is NOT a wildness fact: an unramified place
   over 2 has e = 1 and meets the criterion, which is why
   explore_lock_budget.py F6 already notes Z[w]'s split place over 2
   carrying one. The criterion is re-checked here as the axis of the
   table rather than assumed, and predicts the excess's sign at 6 of 6.
   WHAT IS NEW IS THE WIDTH. lambda at Z[i]'s place over 2 runs
   1,2,4,4,4,4,4,8,8,16,16,32,32,64 — flat at 4 across depths 3..7 — so
   the doors run 1,1,5,4,3,2,1,2,1,... and the tail's own alternation
   (2,1 at prices 4,2) only begins at depth 6. The walk arrives at depth
   3, where the door is 5 and the price 32 against rivals at 9. PR4 held
   at every brute-forced depth. The EXCESS (longest run of one lambda,
   less e) reads 1, 2, 3 at the three headed places — Z[w]'s split pair
   at e = 1, Z[sqrt(-5)]'s ramified place at e = 2, Z[i]'s at e = 2 —
   and 0 at both places failing the criterion. The two at e = 2 differ,
   and they differ arithmetically in one measured way: x^2 + 1 keeps a
   root in O/P^12 at Z[i] and has none at Z[sqrt(-5)], so mu_4 lies in
   one completion only. That the torsion SETS the width is a reading and
   not a claim (observation) — three headed places do not determine a
   formula, and the filed criterion says only where a head IS.
   BOTH HALVES CORRECTED BY explore_head_width.py. The torsion reading is
   REFUTED (F3): Q_2(sqrt 2) and Q_2(sqrt -5) agree in p, e, f and in the
   torsion order and carry widths 1 and 2. The width is the splice's
   level-1 arrival landing less the Kummer seat and less e, which at
   e = 2 is explore_arrival_defect.py F1's trichotomy plus one: 0/1/2 as
   K(i)/K is ramified, unramified or split.
   And the criterion is not p - 1 <= e but f = 1 with mu_p in K_P and
   e = (p-1)p^t (F2).

4. THE DISAGREEMENT WAS ALREADY IN THE CORPUS, AT A RING ALREADY WALKED
   (rule in range; three rings, each from the void, through the imported
   walker). Z[w]'s two split places over 2 have product 2 against its own
   lock at 3 — so the least product has been failing to take the
   recurrent slot in a ring the corpus has walked and re-walked, and
   nothing read it, because F11 asked the question of ramified places
   only and those two are split.
   BUT THE LAW HAS TWO QUANTIFIERS AND THEY FAIL AT DIFFERENT RINGS, and
   flattening them was this rig's own first reading. F9 measures the flat
   tail minimum over SEATED items; the corpus then uses the same product
   to predict which place gets seated AT ALL, over the whole universe,
   which is strictly wider. Separated:
     - Z[w] breaks the WIDE reading only. Neither norm-2 place is ever
       seated, so over seated items its least product is 3 and AGREES
       with the walk.
     - Z[i] breaks BOTH. Its ramified place IS seated, at exponent 3,
       and its product is 4 against a walk paying 9 — the least product
       failing to hold the recurrent slot under F9's own quantifier and
       not merely under the corpus's extension of it.
     - Z[sqrt(-5)] satisfies both.
   This does not falsify F9 in its measured range, which is synthetic
   cells; it says the law does not TRANSFER to a ring even when read at
   its own strength, and the head is why.

5. TWO MECHANISMS, AND THE OBVIOUS TEST CONFLATES THEM (rule in range;
   every below-ranked place at all three rings, read at the DECIDING
   state — the one where the walk first took the vehicle it kept, not
   the locked state, where the invariant carries everything and every
   place reads as covered). A place the law ranks below the lock is
   passed over for exactly one of two reasons:
     - HEADED: its OWN ladder, at the seat it has there, prices its door
       above the law's product. Z[w]'s norm-2 splits at 4 rather than 2
       (their first rung is trivial, N - 1 being 1); Z[i]'s ramified
       place at 32 rather than 4.
     - COVERED: the STATE widens the door past the lone place's. Z[i]'s
       two norm-5 splits, door 1 -> 2, price 25 rather than 5.
   All five fall in exactly one, and the split is mechanical: the state
   can only ever widen a lone-place door, so a price above the product
   with no widening is the place's own head. The natural test — does the
   place's first rung divide the invariant — is DEGENERATE, reading
   every trivial-rung place as covered against an invariant of 1, which
   is the head wearing the other name; it fired that way on all five
   before the split was made mechanical.
   So the law's defect is one of SCOPE rather than of arithmetic:
   N^gap prices a place ALONE AND DEEP, and a greedy walk prices it
   WHERE IT STANDS. The mixed cells could not see this because a
   synthetic ladder is a gap and has no head, and no cell puts two
   items on one invariant.

RUN RECORD. One command, 99 checks, 0.4 s wall clock, peak working set
21.2 MB under memwatch.py's 512 MB ceiling. The brute-forcer ran 64 rows
against the two filed rings and 25 at this one with 0 disagreements.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import gcd, isqrt

import explore_lock_budget as LB
import explore_module_law as K23
import explore_number_field_lock as K5
import explore_tick_pump as TP

CHECKS = 0

MAXP = 2000          # rational primes enumerated into the universe
BRUTE_CAP = 4096     # residues allowed in one brute-forced quotient
TAIL_N = 40          # recurrent moves recorded past the lock
DEPTH_N = 14         # depths of the ramified ladder tabulated


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def lcm(a, b):
    return a * b // gcd(a, b)


# ------------------------------------------------------------------ the ring
# K = Q(i), O = Z[i] = Z[t], t^2 = -1. h = 1, disc -4, units {+-1, +-i}.
# Place keys, matching the shape the imported walker reads:
#   ('ram', 2)        P = (1+i), e = 2, f = 1, WILD
#   ('split', p, r)   P = (p, t - r), r^2 = -1 mod p; conjugate root p - r
#   ('inert', q)      (q), f = 2, q = 3 mod 4
T_TR, T_NM = 0, -1   # t^2 = T_TR*t + T_NM


def _sieve(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(2, n + 1) if s[i]]


PRIMES = _sieve(MAXP)


def place_norm(pl):
    return pl[1] * pl[1] if pl[0] == 'inert' else pl[1]


def place_char(pl):
    return pl[1]


def place_ef(pl):
    return 1 if pl[0] == 'split' else 2   # inert f = 2; ramified e = 2


def place_bit(pl):
    return 0                              # h = 1: every place is principal


def place_key(pl):
    return (place_norm(pl), pl[2] if pl[0] == 'split' else 0)


def conj_place(pl):
    if pl[0] == 'split':
        return ('split', pl[1], pl[1] - pl[2])
    return pl


def build_universe():
    places = [('ram', 2)]
    for p in PRIMES:
        if p == 2:
            continue
        if p % 4 == 1:
            r = next(r for r in range(1, p) if (r * r + 1) % p == 0)
            places.append(('split', p, r))
            places.append(('split', p, p - r))
        elif p * p <= MAXP:
            places.append(('inert', p))
    places.sort(key=place_key)
    return places


UNIVERSE = build_universe()


def lam_P(pl, a):
    """lambda of the prime-power column P^a — the exponent of (O/P^a)^*.

    Split and inert are the standard local units. The ramified column is
    the hand-derived plateau, brute-checked in S1: U_1 = mu_4 x U_3 with
    U_3 free of rank 2, so the exponent is stuck at 4 until the free part
    outgrows the torsion.
    """
    if a == 0:
        return 1
    k, p = pl[0], pl[1]
    if k == 'split':
        return (p - 1) * p ** (a - 1)
    if k == 'inert':
        return (p * p - 1) * p ** (a - 1)
    if a == 1:
        return 1
    if a == 2:
        return 2
    return max(4, 2 ** (-((3 - a) // 2)))     # 2^ceil((a-3)/2)


def lam_state(st):
    L = 1
    for pl, e in st.items():
        L = lcm(L, lam_P(pl, e))
    return L


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


# ------------------------------------- a generic quadratic-order brute-forcer
# One instrument for all three rings. An order is Z[t] with t^2 = T*t + N0;
# an element is the pair (a, b) meaning a + b*t; an ideal is a Z-module given
# by generators and reduced to the HNF basis [(d, 0), (c, e)], whose residues
# are exactly {(x, y) : 0 <= x < d, 0 <= y < e}.
def qmul(u, v, T, N0):
    a1, b1 = u
    a2, b2 = v
    return (a1 * a2 + b1 * b2 * N0,
            a1 * b2 + a2 * b1 + b1 * b2 * T)


def qnorm(u, T, N0):
    a, b = u
    return a * a + a * b * T - b * b * N0


def xgcd(a, b):
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    g, x, y = xgcd(b, a % b)
    return (g, y, x - (a // b) * y)


def hnf2(gens):
    """[(d, 0), (c, e)] for the Z-lattice spanned by gens (pairs)."""
    e, w = 0, (0, 0)
    for a, b in gens:
        if b == 0:
            continue
        if e == 0:
            e, w = abs(b), (a if b > 0 else -a, abs(b))
            continue
        g, s, u = xgcd(e, b)
        w = (s * w[0] + u * a, s * w[1] + u * b)
        e = g
    assert e > 0, "degenerate lattice: no second coordinate"
    d = 0
    for a, b in gens:
        k = b // e
        d = gcd(d, a - k * w[0])
    assert d > 0, "degenerate lattice: no first coordinate"
    return d, w[0] % d, e


def reduce_mod(u, d, c, e):
    a, b = u
    b0 = b % e
    return ((a - ((b - b0) // e) * c) % d, b0)


def ideal_gens(pl, T, N0):
    """Z-module generators of the place, as pairs. ('ram'/'split'/'inert')."""
    p = pl[1]
    if pl[0] == 'inert':
        return [(p, 0), (0, p)]
    if pl[0] == 'split':
        r = pl[2]
    else:
        r = next(r for r in range(p) if (r * r - T * r - N0) % p == 0)
    # P = (p, t - r); the Z-module also needs t times each generator
    return [(p, 0), (0, p), (-r, 1), (N0, T - r)]


def ideal_pow_gens(gens, a, T, N0):
    out = [(1, 0), (0, 1)]
    for _ in range(a):
        prod = [qmul(u, v, T, N0) for u in out for v in gens]
        d, c, e = hnf2(prod)
        out = [(d, 0), (c, e)]
    return out


def unit_exponent(pl, a, T, N0):
    """Exponent of (O/P^a)^*, brute-forced from the actual residue ring."""
    p = pl[1]
    d, c, e = hnf2(ideal_pow_gens(ideal_gens(pl, T, N0), a, T, N0))
    n = place_norm_generic(pl) ** a
    assert d * e == n, "residue count %d is not the norm %d" % (d * e, n)
    one = reduce_mod((1, 0), d, c, e)
    order = n // p * (p - 1) if pl[0] != 'inert' else n // (p * p) * (p * p - 1)
    fac = []
    m = order
    q = 2
    while q * q <= m:
        while m % q == 0:
            fac.append(q)
            m //= q
        q += 1
    if m > 1:
        fac.append(m)
    fac = sorted(set(fac))

    def powmod(u, k):
        res, base = one, u
        while k:
            if k & 1:
                res = reduce_mod(qmul(res, base, T, N0), d, c, e)
            base = reduce_mod(qmul(base, base, T, N0), d, c, e)
            k >>= 1
        return res

    exp = 1
    for x in range(d):
        for y in range(e):
            u = (x, y)
            if qnorm(u, T, N0) % p == 0:
                continue
            o = order
            for q in fac:
                while o % q == 0 and powmod(u, o // q) == one:
                    o //= q
            exp = lcm(exp, o)
    return exp


def place_norm_generic(pl):
    return pl[1] * pl[1] if pl[0] == 'inert' else pl[1]


# ------------------------------------------------------- S1 positive control
def s1_control():
    section("S1  POSITIVE CONTROL -- one brute-forcer against two rings whose "
            "tables it did not write, and only then against this one")
    print("  The instrument: enumerate O/P^a from an HNF basis, keep the")
    print("  units, take the exponent of the group. Run first at the two")
    print("  rings already carrying independently written lambda tables.")

    trials = [("K5", K5, 0, -5), ("K23", K23, 1, -6)]
    print("\n  %-5s %-8s %-4s %-9s %-9s %s"
          % ("ring", "place", "a", "brute", "filed", ""))
    for name, M, T, N0 in trials:
        for pl in M.UNIVERSE:
            if pl[0] == 'split' and pl[2] != min(
                    q[2] for q in M.UNIVERSE
                    if q[0] == 'split' and q[1] == pl[1]):
                continue
            n = place_norm_generic(pl)
            for a in range(1, 13):
                if n ** a > BRUTE_CAP:
                    break
                got = unit_exponent(pl, a, T, N0)
                want = M.lam_P(pl, a)
                print("  %-5s %-8s %-4d %-9d %-9d %s"
                      % (name, LB.show_place(M, pl), a, got, want,
                         "" if got == want else "  <-- DISAGREE"))
                ok(got == want,
                   "%s: brute exponent %d at %s^%d against the filed %d"
                   % (name, got, LB.show_place(M, pl), a, want))
            if n > 30:
                break

    print("\n  and only now this ring, whose table is the hand derivation:")
    print("  %-8s %-4s %-9s %-9s %s" % ("place", "a", "brute", "closed", ""))
    for pl in UNIVERSE[:4]:
        n = place_norm(pl)
        for a in range(1, DEPTH_N + 1):
            if n ** a > BRUTE_CAP:
                break
            got = unit_exponent(pl, a, T_TR, T_NM)
            want = lam_P(pl, a)
            print("  %-8s %-4d %-9d %-9d %s"
                  % (LB.show_place(sys.modules[__name__], pl), a, got, want,
                     "" if got == want else "  <-- DISAGREE"))
            ok(got == want,
               "Z[i]: brute exponent %d at %s^%d against the closed form %d"
               % (got, LB.show_place(sys.modules[__name__], pl), a, want))


# --------------------------------------------------------- S2 the void walk
def s2_void_walk():
    section("S2  THE VOID WALK -- whether the product ordering decides, "
            "through the imported walker")
    M = sys.modules[__name__]

    # the margin, checked rather than asserted: the whole universe at the void
    print("  every place of norm <= 30 at the void, door and price:")
    print("  %-8s %-7s %-6s %s" % ("place", "norm", "door", "price"))
    scan = LB.scan_universe(M, {}, 1, ceiling=30)
    for nrm, r, cost, pl in sorted(scan):
        print("  %-8s %-7d %-6d %d" % (LB.show_place(M, pl), nrm, r, cost))
    cheapest = min(scan, key=lambda t: (t[2], t[0]))
    print("  cheapest opening: %s at %d"
          % (LB.show_place(M, cheapest[3]), cheapest[2]))

    got = TP.ring_walk(M, {}, tail=TAIL_N)
    ok(got is not None, "the void seed does not lock inside the walker's cap")
    st, L, pl, cost, steps = got
    ram = ('ram', 2)
    print("\n  lock vehicle %s at recurrent cost %d, %d steps to the lock"
          % (LB.show_place(M, pl), cost, steps))
    print("  locked support: %s" % LB.show_state(M, st))
    print("  the ramified place stands at exponent %d" % st.get(ram, 0))

    strands = TP.strand_prices(M, st, L, pl, cost)
    for sq, se, sr, sc in strands:
        print("  strand %s at exponent %d, door %d, price %d against a lock "
              "at %d" % (LB.show_place(M, sq), se, sr, sc, cost))
    return st, L, pl, cost, strands


# ------------------------------------------------- S3 the head and the tail
def s3_head_tail():
    section("S3  THE HEAD AND THE TAIL -- what the product law prices and "
            "what the walk pays")
    M = sys.modules[__name__]
    ram = ('ram', 2)
    print("  the ramified ladder, and the door read at each depth from the")
    print("  lone place's own invariant:")
    print("  %-6s %-10s %-6s %s" % ("depth", "lambda", "door", "price"))
    rows = []
    for a in range(1, DEPTH_N + 1):
        lam = lam_P(ram, a)
        r = door_r(ram, a, lam)
        rows.append((a, lam, r, 2 ** r))
        print("  %-6d %-10d %-6d %d" % (a, lam, r, 2 ** r))
    plateau = [a for a, lam, _, _ in rows if lam == 4]
    print("  the plateau (lambda flat at 4) spans depths %d..%d, %d wide"
          % (plateau[0], plateau[-1], len(plateau)))
    # the tail is where the DOOR sequence becomes periodic in the gap, which
    # is not where lambda starts moving again -- read it as the last depth at
    # which the pattern 2,1 is broken, never as the first depth it appears
    doors = [r for _, _, r, _ in rows]
    # the longest ALTERNATING suffix, found by walking back from the end --
    # never by assuming which parity carries the 2, which is a phase this
    # ladder does not have to share with its depth index
    i = len(doors) - 1
    while i > 0 and (doors[i - 1], doors[i]) in ((2, 1), (1, 2)):
        i -= 1
    per0 = i + 1
    ok(all((doors[j], doors[j + 1]) in ((2, 1), (1, 2))
           for j in range(i, len(doors) - 1)),
       "the door suffix from depth %d does not alternate" % per0)
    print("  the door sequence alternates (2,1 at prices 4,2) from depth %d"
          % per0)
    print("  the walk's own reach is what decides, and it stops short of it")
    return rows, plateau, per0


# ----------------------------------------------------- S4 the cross-ring read
def s4_cross_ring():
    section("S4  THE HEAD'S WIDTH ACROSS THREE RINGS -- the filed criterion "
            "says WHERE one is; this asks HOW WIDE")
    print("  A place without a head repeats each lambda exactly e times --")
    print("  that is the ladder. The observable is the EXCESS: the longest")
    print("  run of one lambda, minus e. Zero excess = no head.")
    print("  explore_tick_pump.py F1 already files WHICH places carry one,")
    print("  at 90 of 90: exactly those with p - 1 <= e, because below")
    print("  e/(p-1) the principal units are still squaring. So the axis is")
    print("  that criterion and NOT ramification -- an unramified place over")
    print("  2 has e = 1 and meets it. Scanned over every place of small")
    print("  residue characteristic, ramified or not, to keep the criterion")
    print("  the measured thing rather than the assumed one.")
    print("  %-5s %-7s %-4s %-4s %-7s %-22s %-5s %-6s %s"
          % ("ring", "place", "p", "e", "p-1<=e", "lambda by depth", "run",
             "excess", "i in the completion"))
    rings = [("K5", K5, 0, -5), ("K23", K23, 1, -6),
             ("Zi", sys.modules[__name__], T_TR, T_NM)]
    out = []
    for name, M, T, N0 in rings:
        for pl in M.UNIVERSE:
            p = pl[1]
            e = 2 if pl[0] == 'ram' else 1
            if pl[0] == 'inert':
                continue          # f = 2; its lambda is the split shape in N
            if not (p - 1 <= e or pl[0] == 'ram'):
                continue          # the criterion's own complement, sampled
                                  # by the ramified places that fail it
            lams = [M.lam_P(pl, a) for a in range(1, DEPTH_N + 1)]
            run = max(sum(1 for x in lams if x == v)
                      for v in set(lams) if v > 1)
            # the candidate mechanism, MEASURED where it can be: a p-power
            # root of unity beyond the residue field lives in the completion
            # iff its polynomial keeps a root at every depth
            deep = max(a for a in range(1, DEPTH_N + 1)
                       if place_norm_generic(pl) ** a <= BRUTE_CAP)
            fourth = has_i(pl, deep, T, N0) if p == 2 else None
            headed = p - 1 <= e
            print("  %-5s %-7s %-4d %-4d %-7s %-22s %-5d %-6d %s"
                  % (name, LB.show_place(M, pl), p, e,
                     "yes" if headed else "no",
                     ",".join(str(x) for x in lams[:8])[:22], run, run - e,
                     ("yes" if fourth else "no") + " (depth %d)" % deep
                     if fourth is not None else "-- (p odd)"))
            # the filed criterion PREDICTS the excess's sign, and that is the
            # check: a head exactly where p - 1 <= e, never where ramified
            ok((run > e) == headed,
               "%s: %s has excess %d against the filed criterion p-1<=e "
               "saying %s" % (name, LB.show_place(M, pl), run - e, headed))
            out.append((name, pl, p, e, run, run - e, headed, fourth))
    return out


def has_i(pl, a, T, N0):
    """Does x^2 + 1 keep a root in O/P^a? At depth past the ramification the
    answer is Hensel's, so this reads whether the completion holds mu_4."""
    d, c, e = hnf2(ideal_pow_gens(ideal_gens(pl, T, N0), a, T, N0))
    one = reduce_mod((1, 0), d, c, e)
    zero = (0, 0)
    for x in range(d):
        for y in range(e):
            u = (x, y)
            sq = reduce_mod(qmul(u, u, T, N0), d, c, e)
            if reduce_mod((sq[0] + one[0], sq[1] + one[1]), d, c, e) == zero:
                return True
    return False


def deciding_state(M, steps):
    """The state the walk stood in when it first took the vehicle it would
    keep. Reading a mechanism at the LOCKED state is vacuous -- by then the
    invariant carries every place's first rung and everything reads as
    covered. The choice was made here, and the primitives are imported."""
    st, L = {}, M.lam_state({})
    hist = [(dict(st), L)]
    for _ in range(steps):
        _, (pl, r) = LB.step_once(M, st, L)
        st = LB.apply_move(st, pl, r)
        L = M.lam_state(st)
        hist.append((dict(st), L))
    return hist[max(0, steps - LB.LOCK_R)]


def s6_law_vs_walk_all_rings():
    section("S6  THE SAME COMPARISON AT EVERY RING THE CORPUS HAS WALKED -- "
            "is the disagreement this ring's, or was it always there")
    print("  For each ring: the mixed law's least product over the whole")
    print("  universe, against the recurrent cost the imported walker")
    print("  actually pays from the void. Then every place the law ranked")
    print("  BELOW the observed lock, with its own lambda head.")
    rings = [("K5", K5, 0, -5), ("K23", K23, 1, -6),
             ("Zi", sys.modules[__name__], T_TR, T_NM)]
    rows = []
    for name, M, T, N0 in rings:
        prods = []
        for pl in M.UNIVERSE:
            if M.place_norm(pl) > 60:
                break
            g = 2 if pl[0] == 'ram' else 1
            prods.append((M.place_norm(pl) ** g, M.place_norm(pl), g, pl))
        best = min(prods)
        got = TP.ring_walk(M, {}, tail=TAIL_N)
        ok(got is not None, "%s: the void seed no longer locks" % name)
        st, L, vpl, cost, steps = got
        # TWO READINGS OF THE LAW, and they are not the same claim. F9
        # measures the flat tail minimum over SEATED items; the corpus then
        # uses the same product to predict which place gets seated at all,
        # which is a strictly wider quantifier. Both are reported, because
        # a ring can break the wide one and satisfy the strict one.
        seated = [(M.place_norm(q) ** (2 if q[0] == 'ram' else 1), q)
                  for q, e in st.items() if e]
        sbest = min(seated)
        print("\n  %-5s law over the WHOLE universe: least product %-5d at "
              "%-8s | walk locks %-8s at %d"
              % (name, best[0], LB.show_place(M, best[3]),
                 LB.show_place(M, vpl), cost))
        print("        law over SEATED items only (F9's own quantifier): "
              "least product %d at %s -- %s the walk's %d"
              % (sbest[0], LB.show_place(M, sbest[1]),
                 "AGREES with" if sbest[0] == cost else "DISAGREES with",
                 cost))
        under = [t for t in prods if t[0] < cost]
        dst, dL = deciding_state(M, steps)
        if under:
            print("        the deciding state -- where the walk first took "
                  "the vehicle it kept: %s, invariant %d"
                  % (LB.show_state(M, dst), dL))
        for prod, nrm, g, pl in sorted(under):
            lams = [M.lam_P(pl, a) for a in range(1, 7)]
            # WHICH mechanism, read where the choice was made: a place is
            # COVERED when its first rung already divides the invariant the
            # walk carries THERE, and HEADED when its own ladder is flat over
            # a stretch wider than its gap. The two are independent, and the
            # second is a property of the place alone while the first is not.
            seat = dst.get(pl, 0)
            r_here = M.door_r(pl, seat, dL)
            # the two mechanisms, separated mechanically rather than by
            # eye. The place ALONE at this seat prices its door off its own
            # ladder; the state can only widen that. So a price above the
            # law's product with no widening is the place's own HEAD, and a
            # widening is the state COVERING it. Testing "the first rung
            # divides the invariant" instead reads every trivial-rung place
            # as covered against an invariant of 1, which is the head again
            # wearing the other name.
            lone = M.door_r(pl, seat, M.lam_P(pl, seat))
            why = []
            if nrm ** lone > prod:
                why.append("HEADED (its own ladder prices the door %d here, "
                           "not %d)" % (nrm ** lone, prod))
            if r_here > lone:
                why.append("COVERED (the state widens the door %d -> %d)"
                           % (lone, r_here))
            print("        law said %-8s at %-4d (norm %d, gap %d); THERE it "
                  "sat at exponent %d, door %d, price %d"
                  % (LB.show_place(M, pl), prod, nrm, g, seat, r_here,
                     nrm ** r_here))
            print("             lambda head %s -- %s"
                  % (",".join(str(x) for x in lams),
                     "; ".join(why) or "neither covered nor headed"))
            ok(nrm ** r_here > cost,
               "%s: %s is priced %d at the deciding state, at or below the "
               "lock's %d, yet the walk did not take it"
               % (name, LB.show_place(M, pl), nrm ** r_here, cost))
        if not under:
            print("        no place is ranked below the lock: law and walk "
                  "agree here")
        rows.append((name, best[0], cost, len(under)))
    return rows


# --------------------------------------------- S5 the law against the walk
def s5_law_vs_walk(lock_cost):
    section("S5  THE MIXED LAW'S PRODUCT AGAINST THE WALK'S OWN PRICE")
    M = sys.modules[__name__]
    print("  the law: price a place by N^gap, gap = e at a ramified place")
    print("  and 1 elsewhere, and the least product takes the slot.")
    print("  %-8s %-7s %-5s %s" % ("place", "norm", "gap", "product"))
    prods = []
    for pl in UNIVERSE:
        if place_norm(pl) > 30:
            break
        g = 2 if pl[0] == 'ram' else 1
        prods.append((place_norm(pl) ** g, pl, g))
        print("  %-8s %-7d %-5d %d"
              % (LB.show_place(M, pl), place_norm(pl), g,
                 place_norm(pl) ** g))
    best = min(prods)
    print("  the law's least product: %d, at %s"
          % (best[0], LB.show_place(M, best[1])))
    print("  the walk's recurrent cost: %d" % lock_cost)
    return best, lock_cost


def main():
    s1_control()
    st, L, pl, cost, strands = s2_void_walk()
    rows, plateau, tail = s3_head_tail()
    cross = s4_cross_ring()
    best, lock_cost = s5_law_vs_walk(cost)
    allrings = s6_law_vs_walk_all_rings()

    section("VERDICT -- the predictions read against what printed")
    ram = ('ram', 2)
    M = sys.modules[__name__]
    print("  PR1 lock vehicle %s at cost %d"
          % (LB.show_place(M, pl), cost))
    print("  PR2 the ramified place ends at exponent %d" % st.get(ram, 0))
    print("  PR3 strands: %s"
          % (", ".join("%s priced %d" % (LB.show_place(M, s[0]), s[3])
                       for s in strands) or "(none)"))
    print("  PR4 the brute-forcer agreed with every filed and closed-form "
          "lambda in S1")
    print("  PR5 the plateau here is %d wide" % len(plateau))
    print("  PR6 law %d at %s, walk %d at %s"
          % (best[0], LB.show_place(M, best[1]), lock_cost,
             LB.show_place(M, pl)))
    print("  and beyond the slate, under the WIDE quantifier (least product "
          "over the whole universe, not over seated items -- S6 separates "
          "them): %s"
          % ", ".join("%s (%d vs %d, %d place(s))" % r for r in allrings))
    print("\n  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
