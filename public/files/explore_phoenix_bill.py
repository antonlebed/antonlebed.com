"""explore_phoenix_bill.py — the intervention price list.

THE QUESTION (the melt's last remainder, plus an open lead from
explore_interactive_observer.py, unified). Two remainders are one
object. (i) THE UNTRUNCATED ESCALATOR: along TRUE (no degree bound)
thermal D-DYN trajectories over F_2[x], what is the recurrence of the
minimal admissible move degree m*_t — the law whose truncated face is
the halt clock's rider-creep (explore_halt_clock.py findings 2, 5)?
(ii) THE GENERAL PHOENIX: the phoenix protocol (explore_interactive_
observer.py) with NON-MINIMAL pushes — what does an intervention buy,
at what price? The unifier: the min-admissible-degree recurrence IS
the phoenix's price list; paying the minimum sustains, paying above it
programs.

PREDICTIONS E1-E4 were fixed before the run and hand-checked before
this engine was written. Findings enter by a separate post-run edit
copying printed output.

  E1 (criterion): m*(state) = min of (a) d*(S) = min{d >= 2 : d divides
     no d' in S} (fresh open door), (b) min over places deg(g) *
     (2^c + 1 - e_g) (old crossing), (c) min over degrees with a fresh
     irreducible available d * (2^c + 1) (fresh crossing). Exact on
     every battery state vs brute (all monics deg <= 11).
  E2 (the untruncated escalator; exact sampling within a reported
     degree truncation, tail renormalized): E2a skip-closures = 0 at
     beta in {2, 3}; E2b d*(T=26) >= T - 8 (alphabet linear); E2c
     c(T=26) in [5, 7] at beta = 2 (clock logarithmic); E2d mean pick
     overhead vs r/(1-r), r = 2^(1-beta) (pass-2 refinement predicts
     ~ 2r/(1-r) instead); E2e m*_t = min{n : A(n) > 0} every move.
  E3 (the phoenix bill, D-truncated afterlife): E3a doors never reopen
     under any injection; E3b minimal revival = a column topped up to
     within its native reach of the frontier (the prediction guessed
     the deepest degree-1 column; brute adjudicates); E3c the bill
     recurrence bill' = 2*bill + D (geometric — vs Z's constant-2
     linear pump, the module law as intervention economics); E3d each
     revival buys EXACTLY ONE native move (the dead thermostat); E3e
     odd(lambda) constant through the whole afterlife (the DNA law
     transfers unchanged).
  E4 (the general phoenix over Z): E4a the generalized spectrum law —
     windows ever opened = {p : (p-1) | 2^t * D}, D = odd(lambda) after
     pushes, schedule-independent; E4b the price list (fiat / depth /
     cover branches; single-push brute minima 97 -> 7, 641 -> 11,
     1009 -> 127, 257 -> free); E4c the discount law (census: discount
     > 0 fraction in (0, 0.5); algebra bound fiat - depth >
     v2(p-1) - sum log2 l; Proth-3 cost constant; Fermat cost 0);
     E4d the exactness obstruction: adding l^e to the DNA with no odd
     side effect needs a prime l^e * 2^a + 1 — a Proth-type existence
     question (the designed-DNA obstruction is Sierpinski-shaped).

DESIGN. Untruncated menus are counted exactly per degree by a
generating-function DP (quiet caps: old place j <= 2^c - e, fresh
closed-degree depth <= 2^c, fresh open-degree depth 0), A(n) = 2^n -
Q(n); moves are sampled exactly within degree <= n_max = m* + slack
(tail bound 2^((1-beta)n) geometric, max relative tail asserted small
and reported), split into door species (uniform rejection) and
crossing-only species (core + NoDoor cofactor with multiplicity
correction). Needs a general F_2[x] factorizer (DDF + char-2 trace
EDF), GATED against the melt's tables on all monics deg <= 14, and the
DP is GATED per degree against brute counts on every battery state
(plus the all-monics 2^n identity). Z side reimplements the phoenix
protocol from explore_interactive_observer.py (greedy D-TRA fill to
the wall, push at death) with arbitrary push schedules.

FINDINGS (run record at bottom; all sections
assert. E1/E3 confirmed as predicted; E2 and E4 carry three upgraded
misses — predictions are not tame.)

1. THE MOVE-DEGREE CRITERION (criterion, proved; asserted exhaustively:
   14 states x all monics deg <= 11, DP gated per degree). The minimal
   admissible move degree m*(state) is the min of THREE named channels
   (E1) — a fresh OPEN door d*(S) = min{d >= 2 : d divides no place-
   degree in S}, an OLD crossing deg(g)*(2^c + 1 - e_g), a fresh CLOSED
   crossing d*(2^c + 1) — and the per-degree admissible count A(n) =
   2^n - Q(n) is computed exactly by a generating-function DP over the
   place menu (quiet set Q). Both were brute-confirmed: formula == brute
   m* and DP == brute at every degree on every battery state, and the
   char-2 factorizer (DDF + trace-EDF) reproduces the melt's tables on
   all 32766 monics deg <= 14. This is the halt clock's two-channel
   criterion (findings 1-2) promoted to the untruncated menu with an
   exact counting layer — the escalator's per-move floor made decidable.

2. THE UNTRUNCATED ESCALATOR (rule for the structure; MC for the
   distribution; exact within a reported degree truncation, max
   relative tail 1e-4 / 9e-6 / 2e-9 at beta 1.5 / 2 / 3). Along TRUE
   thermal D-DYN trajectories from the light seed x^2 (T = 26 moves):
   THE ALPHABET IS LINEAR — the fresh-open-door degree d*(T) tracks the
   move count, d*(T) >= T - 8 at beta 2 (min 21) and beta 3 (min 22),
   d*(T)/T -> 1; THE CLOCK IS LOGARITHMIC — c(T) in [5, 6] at beta 2,
   {6} at beta 3 (E2b, E2c confirmed). Two frozen sub-predictions were
   MISSED and upgraded:
   (i) E2a said skip-closures (opening a MULTIPLE of a still-open door,
   killing it unused) are ZERO at beta 2, 3. FALSE — 8 at beta 2, 1
   even at beta 3 — but all in SHALLOW windows (pre-move d* <= 7 at
   beta 2, = 2 at beta 3): the upgraded law is GEOMETRIC SUPPRESSION,
   a skip at door-degree d* costs an overshoot >= d* at thermal price
   ~2^((1-beta) d*), so the lattice tax vanishes as the window deepens
   (none past d* ~ 14/(beta-1)), not identically.
   (ii) E2d froze the mean pick-degree overhead E[deg - m*] at r/(1-r)
   (r = 2^(1-beta)); pass 2 (pre-run) refined to 2r/(1-r); BOTH miss
   LOW — measured 2.729 / 1.132 at beta 2 / 3 (vs 1.0 / 2.0 and 0.33 /
   0.67). The mechanism the frozen forms omit: admissibility SATURATES
   (A(n) -> 2^n a few degrees above m*, since almost every high-degree
   monic carries a fresh open factor), so the overhead = a saturation
   gap (m* to the near-2^n floor) PLUS the geometric tail — the tail
   alone was frozen. The escalator's floor is exact (finding 1); its
   thermal ROOF sits a saturation gap higher than the naive geometric.

3. THE PHOENIX BILL IS GEOMETRIC (rule, proved + asserted; the melt's
   D = 6 world, beta = 2). Give the dead bounded-alphabet world minimal
   life support — at each death inject the cheapest reviving monic — and
   the afterlife obeys a closed price law. Doors never reopen (E3a: 5
   closed doors survive all 510 injections deg <= 8; H3). The minimal
   revival tops a degree-1 column to within its native reach D/1 of the
   frontier (E3b, brute-minimal below the bill), and each revival buys
   EXACTLY ONE native move (E3d: menu size 1 — the afterlife is
   deterministic, temperature irrelevant) that re-kills the world one
   clock-tick deeper, so THE BILL DOUBLES: bill_{k+1} = 2*bill_k + D,
   bills 2, 10, 26, 58, 122 at D = 6 (E3c) — closed form
   bill_k = 2^(c_0 + k - 1) - D (c_0 = 4 the death clock: 2, 10, 26,
   58, 122), the frontier receding geometrically while the alphabet
   stays fixed.
   The frozen DNA law transfers (E3e: odd(lambda) constant through the
   afterlife). THIS IS THE MODULE LAW AS ECONOMICS: over Z the 2-column
   linear pump crosses every frontier at CONSTANT cost 2 (rank-1, the
   immortal witness, melt S5) so its bill is 0 — no phoenix needed;
   over F_2[x] the same frontier recession is unpayable by a bounded
   alphabet, and the intervention bill is the module law's diverging
   cost read as a price the operator pays.

4. THE GENERAL PHOENIX PROGRAMS THE DNA — AT A PRICE (rules + census;
   the explore_interactive_observer.py phoenix over Z with non-minimal
   pushes). THE
   SPECTRUM LAW GENERALIZES exactly (E4a, 4 runs): the windows a
   phoenix ever opens are {p : odd(p-1) | D} at depths v_p(D)+1, D =
   odd(lambda) after the pushes — so a push writes the world's genome,
   and richer pushes open strictly more windows (DNA 3: 12 odd windows
   incl. the Fermat + Proth-3 families; DNA 9 adds 8 more: 19, 37, 73,
   577, ...). (A theorem, not a run count: every death lands on the
   wall W(lambda), whose primes are the doors of lambda = 2^t * D at
   exponent v_p(lambda)+1, and a revival pushes only 2, raising t and
   leaving D frozen.) PREDICTED E4a MISS (upgraded): pushes are NOT schedule-
   independent — the same push 9 = 3^2 gives DNA 3 when it lands on a
   virgin 3-column (odd(lambda(3^2)) = 3) but DNA 9 when it lands on the
   world's SELF-GROWN 3-column at death 4 (the exponents COMPOUND); the
   spectrum law holds per run, but the realized D depends on WHEN you
   push relative to the world's own growth of that column.
   (SETTLED SINCE BY explore_genome_fibre.py F1 and F2, at theorem
   tier: the schedule dependence recorded here as a witness is a law
   with a proof for every state and every odd prime. The slack
   delta_l = d_l - c_l + 1 is a countdown of free pushes, e of them
   give Delta d_l = max(0, e - delta_l), and the witness above is the
   single case delta = 1 against delta = 0 at e = 2. So the fibre
   coordinate over a genome does not accompany the compounding rate
   -- it IS the rate, and the largest genome-exponent SPREAD across a
   fibre over D is v_l(D)+1.) THE PRICE
   LIST (E4b, brute single-push minima): opening a target prime p costs
   the min of FIAT (push p: log2 p bits), DEPTH (push l^(e+1) per l^e ||
   odd(p-1)), COVER (push the least prime q* with the odd part dividing
   odd(q*-1)) — 97 opens via 7 (2.81 bits vs fiat 6.60), 641 via 11,
   1009 via 127, 257 for FREE (a Fermat window the minimal phoenix
   already opens). THE DISCOUNT IS COMMON (E4c census p < 50000): 31.3%
   of primes cost strictly less than fiat, the cover branch winning 935
   times; the discount concentrates on 2-heavy / odd-smooth shifted
   primes (fiat - depth > v2(p-1) - sum log2 l, an exact per-prime
   bound), the Proth-3 family costs a constant <= log2 7 while fiat
   grows, Fermat windows cost 0. THE EXACTNESS OBSTRUCTION (E4d) is the
   third greedy-fate <-> classical-conjecture bridge: an EXACT DNA edit
   (add l^e with no extra odd factor) needs a Proth prime l^e*2^a + 1,
   and its price has NO a-priori bound — least a is 1-8 for almost every
   l^e <= 59 but 583 for l^e = 47, and a Sierpinski number l^e would
   make the edit IMPOSSIBLE. Designed-DNA feasibility is a Proth/
   Sierpinski question (joining the Linnik blockers and the cascade
   boundary's Proth ladder — three bridges now).

HONEST SCOPE. The escalator distribution (finding 2) is exact only
within the reported degree truncation (tail renormalized, max relative
tail 1e-4 at beta 1.5); the saturation-gap mechanism is a qualitative
reading of the measured overhead, not a closed form. The bill
recurrence (finding 3) is proved for the single-leader minimal-revival
policy on the melt's light seed; richer revival policies are unexplored
(the analog of the halt clock's multi-column open edge). The census
(finding 4) is single-push and p < 50000; multi-push cost optima and
the Sierpinski obstruction's density are open. All Z windows assume the
observer reads exact states and knows the law family.

RUN RECORD (this file, ~4 s, 46038 checks, well under 512 MB; all
sections assert. Predictions E1-E4 were hand-checked before this
engine was built: E1/E3 confirmed clean; E2a/E2d/E4a missed and
upgraded as above, every miss a real refinement.)
  SA 14 states (8 constructed + 6 MC-reached) x all 1022 monics deg
     <= 11: formula m* == brute, DP (quiet/NoDoor/all-monics) == brute
     per degree; factorizer == melt tables on all 32766 monics deg
     <= 14; icount == table counts.
  SB T = 26, beta 1.5/2/3 (16/24/16 trajectories): overhead 5.71/2.73/
     1.13, d*(T) >= 18/21/22, c(T) 5-6, skips 16/8/1 all shallow, max
     rel tail 1.2e-4/9.1e-6/2.1e-9.
  SC D = 6 death (c = 4, 6 places, DNA 9765): bills 2/10/26/58/122
     (recurrence 2b+6), each revival menu size 1, DNA frozen, 5 closed
     doors stay closed under 510 injections.
  SD 4 spectrum runs (DNA 3/3/3/9, depths v_p(D)+1); single-push minima
     97->7, 641->11, 1009->127, 257 free; census 5132 primes 31.3%
     discounted, 935 cover wins; E4d Proth table (47 resistant at 583).

Related scripts: explore_function_field_melt.py (+ its closure
explore_halt_clock.py — the truncated face), explore_module_law.py
(the rank dichotomy priced here as economics), and
explore_interactive_observer.py (the minimal phoenix).
"""

import random
import sys
import os
from math import log2

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_function_field_melt as melt
from explore_function_field_melt import (
    pdeg, pmul, pdivmod, pmod, pmulmod, pgcd, ceil_log2, lam_pp, lcm,
    lam_of_fac, thermal_menu, run_thermal, v2,
)

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


# ---------------------------------------------------------------- F2[x] tools
def pderiv(f):
    """Formal derivative in F_2[x]: odd-exponent bits shift down."""
    r = 0
    i = 1
    while (1 << i) <= f:
        if f & (1 << i):
            r |= 1 << (i - 1)
        i += 2
    return r


def psqrt(f):
    """Inverse Frobenius: f = g^2 (all exponents even) -> g."""
    r = 0
    j = 0
    while (1 << (2 * j)) <= f:
        if f & (1 << (2 * j)):
            r |= 1 << j
        j += 1
    return r


def _edf(g, r, rng):
    """Equal-degree factorization, char 2: g = product of deg-r irreducibles."""
    if pdeg(g) == r:
        return [g]
    while True:
        a = rng.randrange(2, 1 << pdeg(g))
        t = pmod(a, g)
        cur = t
        for _ in range(r - 1):
            cur = pmulmod(cur, cur, g)
            t ^= cur
        for cand in (t, t ^ 1):
            d = pgcd(cand, g)
            if 0 < pdeg(d) < pdeg(g):
                return _edf(d, r, rng) + _edf(pdivmod(g, d)[0], r, rng)


def _factor_squarefree(u, rng):
    """Distinct-degree + equal-degree factorization of squarefree monic u."""
    out = []
    v = u
    h = 2  # x
    r = 0
    while pdeg(v) >= 1:
        r += 1
        if 2 * r > pdeg(v):
            out.append(v)
            break
        h = pmulmod(h, h, v)
        g = pgcd(h ^ 2, v)  # gcd(x^(2^r) - x, v)
        if pdeg(g) >= 1:
            out.extend(_edf(g, r, rng))
            v = pdivmod(v, g)[0]
            h = pmod(h, v)
    return out


def pfactor(f):
    """Full factorization {irr: mult} of a monic f, any degree."""
    res = {}
    rng = random.Random(0xF2F2 ^ f)
    mult = 1
    while pdeg(f) >= 1:
        fp = pderiv(f)
        if fp == 0:
            f = psqrt(f)
            mult *= 2
            continue
        u = pdivmod(f, pgcd(f, fp))[0]  # product of odd-multiplicity irrs
        for g in _factor_squarefree(u, rng):
            e = 0
            while True:
                q, rr = pdivmod(f, g)
                if rr:
                    break
                f = q
                e += 1
            res[g] = res.get(g, 0) + e * mult
    return res


_MOB = {1: 1}


def mobius(n):
    if n in _MOB:
        return _MOB[n]
    m, r, d = n, 1, 2
    while d * d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                r = 0
                break
            r = -r
        d += 1
    if r != 0 and m > 1:
        r = -r
    _MOB[n] = r
    return r


_ICACHE = {}


def icount(d):
    """Number of monic irreducibles of degree d over F_2 (necklace formula)."""
    if d not in _ICACHE:
        tot = 0
        for e in range(1, d + 1):
            if d % e == 0:
                tot += mobius(e) * (1 << (d // e))
        _ICACHE[d] = tot // d
    return _ICACHE[d]


# ------------------------------------------------------------- state geometry
def clock_c(fac):
    return max(ceil_log2(e) for e in fac.values())


def degset(fac):
    return set(pdeg(g) for g in fac)


def degcounts(fac):
    cnt = {}
    for g in fac:
        d = pdeg(g)
        cnt[d] = cnt.get(d, 0) + 1
    return cnt


def opendoor(S, d):
    """Fresh door at degree d: open iff d divides no degree in S (d=1 never)."""
    return all(dd % d for dd in S)


def dstar(S):
    d = 2
    while not opendoor(S, d):
        d += 1
    return d


def mstar(fac):
    """E1: the minimal admissible move degree."""
    S = degset(fac)
    c = clock_c(fac)
    F = (1 << c) + 1  # crossing target depth
    best = dstar(S)
    for g, e in fac.items():
        cost = pdeg(g) * (F - e)
        if cost < best:
            best = cost
    cnt = degcounts(fac)
    d = 1
    while d * F < best:
        if icount(d) > cnt.get(d, 0):
            best = d * F
            break
        d += 1
    return best


def fires(fac, L, mf):
    """lambda-growth test from the single-factor law (H1)."""
    for g, e in mf.items():
        if L % lam_pp(pdeg(g), fac.get(g, 0) + e):
            return True
    return False


# --------------------------------------------------- per-degree count DP (GF)
def _polmul(a, b, n_max):
    r = [0] * (n_max + 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if i + j > n_max:
                    break
                if bj:
                    r[i + j] += ai * bj
    return r


def _polpow(base, e, n_max):
    r = [0] * (n_max + 1)
    r[0] = 1
    b = base[: n_max + 1] + [0] * max(0, n_max + 1 - len(base))
    while e:
        if e & 1:
            r = _polmul(r, b, n_max)
        b = _polmul(b, b, n_max)
        e >>= 1
    return r


def gf_counts(fac, n_max, capped, include_open_fresh=False):
    """Counts by degree of monics whose every factor is 'allowed'.

    capped=True: old place extra depth <= 2^c - e, fresh closed-degree
    place depth <= 2^c (the QUIET set = inadmissible monics).
    capped=False: depths unbounded (with open fresh still excluded:
    the NoDoor set). include_open_fresh=True + capped=False must give
    ALL monics = 2^n (the DP sanity identity)."""
    c = clock_c(fac)
    S = degset(fac)
    cnt = degcounts(fac)
    acc = [0] * (n_max + 1)
    acc[0] = 1
    # old places, grouped by (degree, cap)
    groups = {}
    for g, e in fac.items():
        d = pdeg(g)
        cap = ((1 << c) - e) if capped else n_max
        cap = min(cap, n_max // d)
        groups[(d, cap)] = groups.get((d, cap), 0) + 1
    for (d, cap), k in groups.items():
        base = [0] * (cap + 1)
        for j in range(cap + 1):
            base[j] = 1  # compressed in y = z^d
        comp = _polpow(base, k, n_max // d)
        poly = [0] * (n_max + 1)
        for j, cj in enumerate(comp):
            if cj and j * d <= n_max:
                poly[j * d] = cj
        acc = _polmul(acc, poly, n_max)
    # fresh places by degree
    for d in range(1, n_max + 1):
        fresh = icount(d) - cnt.get(d, 0)
        if fresh <= 0:
            continue
        is_open = opendoor(S, d)
        if is_open and not include_open_fresh:
            continue
        cap = (1 << c) if (capped and not is_open) else n_max
        cap = min(cap, n_max // d)
        if cap <= 0:
            continue
        base = [1] * (cap + 1)  # compressed in y = z^d, depth 0..cap
        comp = _polpow(base, fresh, n_max // d)
        poly = [0] * (n_max + 1)
        for j, cj in enumerate(comp):
            if cj and j * d <= n_max:
                poly[j * d] = cj
        acc = _polmul(acc, poly, n_max)
    return acc


# ----------------------------------------------------- exact untruncated menu
def sample_untrunc(fac, beta, rng, tail_log):
    """One exact thermal pick from the UNTRUNCATED admissible menu,
    within degree <= n_max = m* + slack (tail renormalized, bound
    recorded). Returns (factorization of the pick, diagnostics)."""
    ms = mstar(fac)
    c = clock_c(fac)
    S = degset(fac)
    cnt = degcounts(fac)
    slack = 14 + int(round(14.0 / (beta - 1.0)))
    n_max = ms + slack
    Q = gf_counts(fac, n_max, capped=True)
    ND = gf_counts(fac, n_max, capped=False)
    A = [0] + [(1 << n) - Q[n] for n in range(1, n_max + 1)]
    first = next(n for n in range(1, n_max + 1) if A[n] > 0)
    ok(first == ms, f"E2e: min positive-degree {first} != m* {ms}")
    r = 2.0 ** (1.0 - beta)
    masses = [A[n] * 2.0 ** (-beta * n) for n in range(n_max + 1)]
    mass = sum(masses)
    tail = 2.0 ** ((1.0 - beta) * (n_max + 1)) / (1.0 - r)
    tail_log.append(tail / (mass + tail))
    t = rng.random() * mass
    n = n_max
    accum = 0.0
    for i in range(1, n_max + 1):
        accum += masses[i]
        if accum >= t:
            n = i
            break
    door_n = (1 << n) - ND[n]
    if rng.random() * A[n] < door_n:
        # door species: uniform monic with >= 1 fresh open-degree factor
        for _ in range(20000):
            m = (1 << n) | rng.getrandbits(n)
            mf = pfactor(m)
            if any(g not in fac and opendoor(S, pdeg(g)) for g in mf):
                break
        else:
            ok(False, "door-species rejection cap hit")
    else:
        # crossing-only species: core + NoDoor cofactor, multiplicity-corrected
        while True:
            cores = []  # (g, d, j, weight)
            for g, e in fac.items():
                d = pdeg(g)
                cap = (1 << c) - e
                for j in range(cap + 1, n // d + 1):
                    w = ND[n - j * d]
                    if w:
                        cores.append((g, d, j, w))
            for d in range(1, n + 1):
                freshcnt = icount(d) - cnt.get(d, 0)
                if freshcnt <= 0 or opendoor(S, d):
                    continue
                for j in range((1 << c) + 1, n // d + 1):
                    w = ND[n - j * d] * freshcnt
                    if w:
                        cores.append((None, d, j, w))
            tot = sum(w for _, _, _, w in cores)
            ok(tot > 0, "crossing species with no cores")
            pickw = rng.random() * tot
            accw = 0
            for g, d, j, w in cores:
                accw += w
                if accw >= pickw:
                    break
            if g is None:  # fresh closed-degree place: pick one from the table
                pool = [h for h in melt._IRR_BY_DEG[d] if h not in fac]
                g = pool[rng.randrange(len(pool))]
            k = n - j * d
            # uniform NoDoor cofactor of degree k
            if k == 0:
                cof = {}
            else:
                while True:
                    mm = (1 << k) | rng.getrandbits(k)
                    cof = pfactor(mm)
                    if not any(h not in fac and opendoor(S, pdeg(h))
                               for h in cof):
                        break
            mf = dict(cof)
            mf[g] = mf.get(g, 0) + j
            paths = 0
            for h, add in mf.items():
                cap = ((1 << c) - fac[h]) if h in fac else (1 << c)
                if add > cap:
                    paths += add - cap
            if rng.random() < 1.0 / paths:
                break
    # diagnostics
    L = lam_of_fac(fac)
    ok(fires(fac, L, mf), "sampled move must be admissible")
    opened = sorted(set(pdeg(g) for g in mf
                        if g not in fac and opendoor(S, pdeg(g))))
    crossed = any(fac.get(g, 0) + e > (1 << c) for g, e in mf.items())
    skips = 0
    for dpr in opened:
        for dd in range(2, dpr):
            if dpr % dd == 0 and opendoor(S, dd) and dd not in opened:
                skips += 1
    deg_m = sum(pdeg(g) * e for g, e in mf.items())
    ok(deg_m == n, "factorization degree mismatch")
    return mf, dict(deg=n, ms=ms, opened=opened, crossed=crossed, skips=skips)


# --------------------------------------------------------------------- Z side
def is_primeZ(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def lamZ_pp(q, a):
    if q == 2:
        return 1 if a == 1 else (2 if a == 2 else 1 << (a - 2))
    return q ** (a - 1) * (q - 1)


def lamZ(st):
    L = 1
    for q, a in st.items():
        L = lcm(L, lamZ_pp(q, a))
    return L


def divisors(n):
    ds = [1]
    for q, a in factorint(n).items():
        ds = [d * q ** i for d in ds for i in range(a + 1)]
    return ds


def phoenixZ(schedule, t2max):
    """The phoenix from seed 1 (explore_interactive_observer.py),
    generalized pushes.

    Greedy D-TRA: fill to the wall W(lambda) (every prime power whose
    lambda divides lambda(N)); at death k push schedule.get(k, 2).
    Runs until v2(lambda) >= t2max and the schedule is exhausted.
    Returns (state dict, DNA = odd(lambda), deaths)."""
    st = {}
    deaths = 0
    smax = max(schedule) if schedule else 0
    while True:
        L = lamZ(st)
        for d in divisors(L):
            q = d + 1
            if not is_primeZ(q):
                continue
            if q == 2:
                t = v2(L)
                cap = 1 if t == 0 else t + 2
            else:
                a = 0
                x = L
                while x % q == 0:
                    x //= q
                    a += 1
                cap = a + 1
            if st.get(q, 0) < cap:
                st[q] = cap
        L = lamZ(st)
        if v2(L) >= t2max and deaths >= smax:
            return st, oddpart(L), deaths
        deaths += 1
        push = schedule.get(deaths, 2)
        for q, e in factorint(push).items():
            st[q] = st.get(q, 0) + e


def qstar(o, kcap=200000):
    """Least prime q = 1 (mod o), q > 2 (the cover push for odd o)."""
    if o == 1:
        return 3
    for k in range(2, kcap, 2):
        q = k * o + 1
        if is_primeZ(q):
            return q
    return None


# ------------------------------------------------------------------- sections
def sa_criterion():
    print("SA  THE CRITERION + THE COUNT GATES (E1)")
    rng = random.Random(2400)
    g2 = melt._IRR_BY_DEG[2][0]
    g3 = melt._IRR_BY_DEG[3][0]
    g3b = melt._IRR_BY_DEG[3][1]
    g6 = melt._IRR_BY_DEG[6][0]
    battery = [
        {2: 2}, {2: 3}, {2: 5, 3: 1}, {2: 9, g2: 2},
        {2: 17, g3: 1, 3: 4}, {g2: 5, 2: 1},
        {2: 1, 3: 1, g2: 1, g3: 1, g3b: 1}, {g6: 1, 2: 4},
    ]
    for _ in range(6):
        fac, _, _ = run_thermal({2: 2}, 2.0, 8, 6, "DYN", rng)
        battery.append(fac)
    nmax = 11
    for idx, fac in enumerate(battery):
        L = lam_of_fac(fac)
        S = degset(fac)
        A = [0] * (nmax + 1)
        NDb = [0] * (nmax + 1)
        for m in range(2, 2 << nmax):
            dm = pdeg(m)
            if m >> dm != 1 or dm < 1:
                continue
            mf = melt._FAC[m]
            if fires(fac, L, mf):
                A[dm] += 1
            if not any(g not in fac and opendoor(S, pdeg(g)) for g in mf):
                NDb[dm] += 1
        brute_ms = next(n for n in range(1, nmax + 1) if A[n] > 0)
        ok(brute_ms == mstar(fac),
           f"E1 state {idx}: brute {brute_ms} != formula {mstar(fac)}")
        Q = gf_counts(fac, nmax, capped=True)
        ND = gf_counts(fac, nmax, capped=False)
        ALL = gf_counts(fac, nmax, capped=False, include_open_fresh=True)
        for n in range(1, nmax + 1):
            ok(Q[n] == (1 << n) - A[n],
               f"state {idx} deg {n}: quiet DP {Q[n]} != brute")
            ok(ND[n] == NDb[n],
               f"state {idx} deg {n}: NoDoor DP {ND[n]} != brute {NDb[n]}")
            ok(ALL[n] == 1 << n,
               f"state {idx} deg {n}: all-monics DP {ALL[n]} != 2^n")
    # factorizer gate: every monic deg <= DMAX vs the melt's table
    for m in range(2, 2 << melt.DMAX):
        dm = pdeg(m)
        if m >> dm != 1 or dm < 1:
            continue
        ok(pfactor(m) == dict(melt._FAC[m]), f"factorizer wrong at {m}")
    # irreducible-count gate
    for d in range(1, melt.DMAX + 1):
        ok(icount(d) == len(melt._IRR_BY_DEG[d]), f"I({d}) mismatch")
    print(f"  {len(battery)} battery states: formula == brute; DP == brute "
          f"(quiet/NoDoor/all) at every degree <= {nmax}")
    print(f"  factorizer == table on all monics deg <= {melt.DMAX}; "
          f"I(d) == table counts")


def sb_escalator():
    print("\nSB  THE UNTRUNCATED ESCALATOR (E2)")
    T = 26
    results = {}
    for beta, ntraj in ((1.5, 16), (2.0, 24), (3.0, 16)):
        rng = random.Random(int(beta * 1000) + 24)
        r = 2.0 ** (1.0 - beta)
        tail_log = []
        overhead = []
        skip_events = []
        dstars, clocks, crosses, doorc = [], [], [], []
        for _ in range(ntraj):
            fac = {2: 2}
            ncross = 0
            opened_all = []
            for _t in range(T):
                ds_pre = dstar(degset(fac))
                mf, diag = sample_untrunc(fac, beta, rng, tail_log)
                overhead.append(diag["deg"] - diag["ms"])
                if diag["skips"]:
                    skip_events.append((ds_pre, diag["skips"]))
                if diag["crossed"]:
                    ncross += 1
                opened_all.extend(diag["opened"])
                for g, e in mf.items():
                    fac[g] = fac.get(g, 0) + e
            S = degset(fac)
            ndoors = len(opened_all)
            ok(ndoors == len(set(opened_all)),
               "door ledger: a door degree opened twice")
            ok(set(opened_all) <= S, "door ledger: opened degree not in S")
            dstars.append(dstar(S))
            clocks.append(clock_c(fac))
            crosses.append(ncross)
            doorc.append(ndoors)
        mo = sum(overhead) / len(overhead)
        md = sum(dstars) / len(dstars)
        mc = sum(clocks) / len(clocks)
        mx = sum(crosses) / len(crosses)
        mt = max(tail_log)
        skips_tot = sum(k for _, k in skip_events)
        results[beta] = (mo, md, mc, mx, skips_tot, mt)
        print(f"  beta={beta}: mean overhead {mo:.3f} "
              f"(r/(1-r)={r/(1-r):.3f}, 2r/(1-r)={2*r/(1-r):.3f}), "
              f"mean d*(T) {md:.2f}, mean c(T) {mc:.2f}, "
              f"mean #cross {mx:.2f}, skips {skips_tot} "
              f"(at pre-move d* {sorted(set(d for d, _ in skip_events))}), "
              f"max rel tail {mt:.2e}")
        print(f"    d*(T) values {sorted(dstars)}")
        print(f"    c(T) values {sorted(clocks)}")
        ok(mt < 1e-3, f"tail bound too fat at beta {beta}")
        # the true suppression law: a skip needs an opened MULTIPLE of an
        # open door, priced ~ r^(offset >= d*) = 2^((1-beta) d*): no events
        # past the depth where the whole run expects << 1 of them
        deep = 14.0 / (beta - 1.0)
        ok(all(d <= deep for d, _ in skip_events),
           f"skip-closure past the suppression depth at beta {beta}")
        if beta in (2.0, 3.0):
            ok(all(d >= T - 8 for d in dstars),
               f"E2b: d*(T) below {T - 8} at beta {beta}")
        if beta == 2.0:
            ok(all(5 <= c <= 7 for c in clocks),
               f"E2c: c(T) out of [5,7] at beta 2: {sorted(clocks)}")
    # E2d adjudication printed for the findings edit
    for beta in (2.0, 3.0):
        r = 2.0 ** (1.0 - beta)
        mo = results[beta][0]
        print(f"  E2d at beta={beta}: |{mo:.3f} - {r/(1-r):.3f}| "
              f"{'<=' if abs(mo - r/(1-r)) <= 0.5 * r/(1-r) else '>'} "
              f"0.5*r/(1-r); vs pass-2 2r/(1-r) = {2*r/(1-r):.3f}")
    return results


def sc_bill():
    print("\nSC  THE PHOENIX BILL (E3)")
    rng = random.Random(2403)
    D = 6
    beta = 2.0
    fac, picks, halted = run_thermal({2: 2}, beta, D, 400, "DYN", rng)
    ok(halted, "the D=6 world must die (halt clock)")

    def native(fac):
        moves, _, _, _ = thermal_menu(fac, beta, D, "DYN")
        return moves

    ok(not native(fac), "death state must have an empty native menu")
    dna0 = oddpart(lam_of_fac(fac))
    c0 = clock_c(fac)
    print(f"  death: clock c = {c0}, |places| = {len(fac)}, "
          f"DNA odd(lambda) = {dna0}")

    def min_revival(fac):
        """The general minimal reviving injection: bring a column to
        within its native reach floor(D/d) of the frontier."""
        c = clock_c(fac)
        best = None
        for g, e in fac.items():
            d = pdeg(g)
            k = D // d
            if k == 0:
                continue
            j = (1 << c) + 1 - k - e
            ok(j > 0, "dead state has every column out of native reach")
            if best is None or d * j < best[2]:
                best = (g, j, d * j)
        cnt = degcounts(fac)
        for d in range(1, D + 1):
            if icount(d) > cnt.get(d, 0) and d * ((1 << c) + 1 - D // d) < \
                    best[2]:
                g = [h for h in melt._IRR_BY_DEG[d] if h not in fac][0]
                best = (g, (1 << c) + 1 - D // d, d * ((1 << c) + 1 - D // d))
        return best

    g1, j1, bill1 = min_revival(fac)
    print(f"  first bill: column deg {pdeg(g1)} depth {fac.get(g1, 0)} "
          f"topped by {j1} -> bill {bill1}")
    # E3b: brute minimality over ALL monic injections of degree < bill
    ok(bill1 <= 12, "first bill small enough to brute")
    for m in range(2, 2 << (bill1 - 1) if bill1 > 1 else 2):
        dm = pdeg(m)
        if m >> dm != 1 or dm < 1 or dm >= bill1:
            continue
        fac2 = dict(fac)
        for g, e in melt._FAC[m].items():
            fac2[g] = fac2.get(g, 0) + e
        ok(not native(fac2), f"E3b: injection {m} (deg {dm}) revives "
                             f"below the bill {bill1}")
    fac2 = dict(fac)
    fac2[g1] = fac2.get(g1, 0) + j1
    ok(len(native(fac2)) >= 1, "E3b: the bill injection must revive")
    # E3a: doors closed forever, injection battery
    S0 = degset(fac)
    closed0 = [d for d in range(2, 13) if not opendoor(S0, d)]
    for m in range(2, 2 << 8):
        dm = pdeg(m)
        if m >> dm != 1 or dm < 1:
            continue
        S2 = S0 | set(pdeg(g) for g in melt._FAC[m])
        for d in closed0:
            ok(not opendoor(S2, d), f"E3a: door {d} reopened by {m}")
    print(f"  E3a: {len(closed0)} closed doors stay closed under all "
          f"510 injections deg <= 8")
    # the afterlife loop
    bills = []
    cols = []
    for k in range(5):
        g, j, bill = min_revival(fac)
        bills.append(bill)
        cols.append(pdeg(g))
        c_pre = clock_c(fac)
        fac[g] = fac.get(g, 0) + j
        menu = native(fac)
        ok(len(menu) == 1, f"E3d: revival {k}: menu size {len(menu)} != 1")
        m = menu[0]
        mf = melt._FAC[m]
        ok(list(mf) == [g] and mf[g] == D // pdeg(g),
           "E3d: the one native move is the seeded column's crossing")
        for h, e in mf.items():
            fac[h] = fac.get(h, 0) + e
        ok(clock_c(fac) == c_pre + 1, "revival must advance the clock by 1")
        ok(not native(fac), "dead again after the bought move")
        ok(oddpart(lam_of_fac(fac)) == dna0, "E3e: DNA drifted")
    print(f"  bills {bills} on column degrees {cols}")
    for k in range(1, len(bills) - 1):
        ok(bills[k + 1] == 2 * bills[k] + D,
           f"E3c: bill recurrence fails at k={k}: "
           f"{bills[k + 1]} != 2*{bills[k]}+{D}")
    print(f"  E3c: bill' = 2*bill + D from k=1 on "
          f"(k=0 -> 1: {bills[1]} vs 2*{bills[0]}+{D} = {2 * bills[0] + D}); "
          f"Z contrast: the 2-column pump pays a constant 2 per frontier "
          f"(melt S5) — bill 0")
    return bills


def sd_dna():
    print("\nSD  THE GENERAL PHOENIX OVER Z (E4)")
    # E4a: the spectrum law per run + the compounding of pushes with growth
    t2 = 20

    def spectrum(D):
        want = set()
        for d in divisors(D):
            for a in range(1, t2 + 1):
                p = d * (1 << a) + 1
                if is_primeZ(p):
                    want.add(p)
        return want

    stA, dnaA, _ = phoenixZ({1: 9}, t2)   # 9 on a FRESH 3-column: depth 2
    stB, dnaB, _ = phoenixZ({4: 3}, t2)   # 3 on the SELF-GROWN 3-column
    stC, dnaC, _ = phoenixZ({1: 7}, t2)   # the cover push
    stD, dnaD, _ = phoenixZ({4: 9}, t2)   # 9 late: lands at depth 3
    ok((dnaA, dnaB, dnaC, dnaD) == (3, 3, 3, 9),
       f"DNA {(dnaA, dnaB, dnaC, dnaD)} != (3, 3, 3, 9)")
    for st, dna in ((stA, dnaA), (stB, dnaB), (stC, dnaC), (stD, dnaD)):
        w = set(q for q in st if q != 2)
        ok(w == spectrum(dna), f"E4a: spectrum != theory for DNA {dna}")
        for q in w:
            a = 0
            x = dna
            while x % q == 0:
                x //= q
                a += 1
            ok(st[q] == a + 1, f"window {q} depth != v_q(D)+1")
    ok(spectrum(3) < spectrum(9), "DNA 9 spectrum must contain DNA 3's")
    print(f"  spectrum law exact on 4 runs: windows == "
          f"{{p : odd(p-1) | D, v2 <= {t2}}}, depths v_p(D)+1")
    print(f"    DNA 3 ({len(spectrum(3))} windows): {sorted(spectrum(3))}")
    print(f"    DNA 9 adds: {sorted(spectrum(9) - spectrum(3))}")
    print(f"  COMPOUNDING: push 9@death1 -> DNA 3 (fresh column, depth 2); "
          f"push 9@death4 -> DNA 9 (the self-grown column lifts it to "
          f"depth 3); push 3@death4 -> DNA 3 at a third of the push")
    # E4b: brute single-push minima
    for target, expect, t2b in ((97, 7, 12), (641, 11, 12), (1009, 127, 12)):
        for m in range(2, expect):
            st, _, _ = phoenixZ({1: m}, t2b)
            ok(target not in st, f"E4b: push {m} < {expect} opens {target}")
        st, _, _ = phoenixZ({1: expect}, t2b)
        ok(target in st, f"E4b: push {expect} fails to open {target}")
        print(f"  target {target}: brute minimal single push = {expect} "
              f"({log2(expect):.2f} bits vs fiat {log2(target):.2f})")
    st0, _, _ = phoenixZ({}, 12)
    ok(257 in st0, "E4b: 257 must open for free (D = 1)")
    print("  target 257: free (the minimal phoenix opens it, cost 0)")
    # E4c: the discount census
    N = 50000
    sieve = list(range(N + 1))
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i] == i:
            for j in range(i * i, N + 1, i):
                if sieve[j] == j:
                    sieve[j] = i
    primes = [p for p in range(3, N + 1) if sieve[p] == p]
    npos = 0
    best_disc = []
    cover_wins = 0
    qcache = {}
    for p in primes:
        o = oddpart(p - 1)
        vv = v2(p - 1)
        fiat = log2(p)
        if o == 1:
            best = 0.0
        else:
            of = {}
            oo = o
            while oo > 1:
                q = sieve[oo]
                of[q] = of.get(q, 0) + 1
                while oo % q == 0:
                    oo //= q
            depth = sum((e + 1) * log2(l) for l, e in of.items())
            if o not in qcache:
                qcache[o] = qstar(o)
            cw = log2(qcache[o])
            mix = 0.0
            for l, e in of.items():
                le = l ** e
                if le not in qcache:
                    qcache[le] = qstar(le)
                mix += min((e + 1) * log2(l), log2(qcache[le]))
            best = min(fiat, depth, cw, mix)
            # the algebra bound (exact, per prime)
            ok(fiat - depth > vv - sum(log2(l) for l in of) - 1e-9,
               f"algebra bound fails at {p}")
            if best == cw and cw < fiat:
                cover_wins += 1
        disc = fiat - best
        if disc > 1e-9:
            npos += 1
            best_disc.append((disc, p))
        if o == 3:
            ok(best <= log2(7) + 1e-9, f"Proth-3 member {p} costs > log2(7)")
        if o == 1 and p > 2:
            ok(best == 0.0, f"Fermat member {p} not free")
    frac = npos / len(primes)
    best_disc.sort(reverse=True)
    print(f"  census p < {N}: {len(primes)} primes, discount > 0 on {npos} "
          f"({100 * frac:.1f}%), cover-branch wins {cover_wins}")
    print(f"    top discounts: "
          f"{[(p, round(d, 2)) for d, p in best_disc[:6]]}")
    ok(0.0 < frac < 0.5, f"E4c: discount fraction {frac} out of (0, 0.5)")
    # E4d: the exactness obstruction — an exact DNA edit (add l^e with NO
    # extra odd factor) needs a prime q = l^e * 2^a + 1 (a PROTH prime);
    # its price log2(a)+... has NO a-priori bound — the Sierpinski
    # phenomenon is the designed-DNA obstruction. Record the least a; do
    # NOT assert existence (that is the open question).
    print("  E4d: exact-DNA edits l^e -> least a with l^e * 2^a + 1 prime "
          "(the exact-edit price; unbounded = the obstruction):")
    row = []
    resistant = []
    for le in (3, 5, 7, 9, 11, 13, 17, 19, 23, 25, 27, 29, 31, 37, 41, 43,
               47, 49, 53, 59):
        a = next((a for a in range(1, 1200)
                  if is_primeZ(le * (1 << a) + 1)), None)
        row.append((le, a))
        if a is None or a > 50:
            resistant.append((le, a))
    print(f"    {row}")
    print(f"    RESISTANT (least a > 50, or none < 1200): {resistant} "
          f"— the price of an exact edit is a Proth search with no bound; "
          f"a Sierpinski number l^e would make the edit IMPOSSIBLE "
          f"(the third greedy-fate <-> classical-conjecture bridge)")
    return frac, row


def main():
    import time
    t0 = time.time()
    melt.build_tables()
    sa_criterion()
    sb_escalator()
    sc_bill()
    sd_dna()
    print(f"\nALL SECTIONS GREEN — {CHECKS} checks, {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
