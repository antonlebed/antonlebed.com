"""explore_function_field_melt.py — the function-field melt.

THE QUESTION (a thermal remainder from the cold-sprawl study). Thermal
D-DYN over F_2[x]: soften the cold greedy (explore_function_field_lock.py)
into the thermal law — pick admissible monic m (deg >= 1) with probability
proportional to |m|^(-beta) = 2^(-beta deg m), the norm at the infinite
place of F_2(x), normalizable iff beta > 1. Over Z the lock melts at every
finite beta (explore_thermal_growth.py; hot limit: explore_hot_limit.py)
and the discontinuity sits at beta = infinity exactly. Over F_2[x] the
cold dynamics has NO lock — it sprawls (one fresh per degree, the sibling
shadow, x+1 starved forever, a lone x depth thread). So WHAT melts, and
where between the sprawl and the thermal clocks (the beta_col^g spectrum,
explore_irreducibility_crossfield.py) does the melt sit?

Predictions FM1-FM8 were fixed and hand-attacked BEFORE this engine was
written; findings written from the
green run's output. All eight confirmed; the
mortality split (finding 5) is the unpredicted discovery — found when the
first run CRASHED on an emptied menu. A pre-run FINDINGS draft was
fabricated and expunged (a known fabrication-reflex species, recurring here);
two of its invented specifics were checked and are FALSE (mid-window
0.999 at door 3; "deeper frontier is stickier" — the truth is
phase-constant 1/2).

FINDINGS (tiers per the naming conventions; run record at bottom; all sections assert).

1. THE RATIONAL PARTITION FUNCTION (rule, proved; asserted at 4 betas
   with exact geometric tail brackets). The free thermal law over monic
   m, deg m >= 1, has partition function Z(beta) = zeta_{F_2[x]}(beta)-1
   = r/(1-r), r = 2^(1-beta) — RATIONAL in 2^(-beta) (2^d monics per
   degree make the zeta sum geometric; Z(2) = 1 exactly). The degree law
   is exactly geometric: P(deg m = d) = (1-r) r^(d-1). Where Z's thermal
   tower has the Riemann zeta as partition function, F_2[x]'s
   bookkeeping is closed-form throughout.

2. THERMAL D-IND TRANSFERS VERBATIM (rule, proved; exact truncated
   enumeration at 3 states x places x 4 betas + MC). Entry-once is
   monoid-level (a coprime move cannot touch an open place — the
   demand's shape, property). The depth law is Z's weight-factorization
   argument unchanged: P(v_g = k | g enters) = |g|^(-beta(k-1))
   (1 - |g|^(-beta)), geometric with ratio 2^(-beta d), independent
   across places (MC at beta = 2, 1200 trajectories: joint depth-1 of
   x and x+1 0.547 vs product 0.555; depth-1 at entry 0.743 vs 0.750).

3. THE CRYSTAL PROBABILITY IS EXACTLY 1 - 2^(1-beta) (rule, proved;
   Euler product over deg <= 16 vs closed form, bracket widths 6.5e-4 /
   1.8e-6 / 1.4e-11 at beta = 1.5, 2, 3). P(hot D-IND limit squarefree)
   = prod_g (1 - |g|^(-beta)) = 1/zeta_{F_2[x]}(beta) = 1 - 2^(1-beta).
   At beta = 2 the crystal fraction is EXACTLY 1/2 (Z's is 1/zeta(2) =
   0.6079): no transcendental content survives the function-field move.

4. UPWARD CLOSURE + THE RIDER BOUND — THE HOT-LIMIT THEOREM TRANSFERS
   (rule, proved). lambda is divisibility-monotone over F_2[x] (unit
   reduction is surjective, PID CRT — brute: lambda(N) | lambda(N*s) on
   ALL 77,828 monic divisor pairs at deg <= 12), so D-DYN's admissible
   set is UPWARD-CLOSED in divisibility and nonempty (the fresh door,
   ch. 18). The rider injection m -> m g^k gives P(v_g(pick) >= k) >=
   |g|^(-beta k) uniformly in the state (mass inequality asserted on
   enumerated menus, 10 states x 2 betas x 3 riders); conditional
   Borel-Cantelli fires every place open and every depth unbounded
   a.s.: thermal D-DYN reaches the FULL profinite completion of
   F_2[x], every beta > 1 — the sprawl's skeleton (one place per
   degree + the x thread) is a beta = infinity artifact, as Z's lock is.

5. THE MORTALITY SPLIT (an unpredicted discovery — the module law's thermal
   dress; rule for F_2[x] mortality, proved + MC; the Z witness closed
   form). In the BOUNDED-ALPHABET model (moves of degree <= D only)
   every F_2[x] thermal D-DYN trajectory HALTS: admissibility doubles
   lambda each move (old | new + strict), the odd part is bounded by
   odd(seed) * prod_{d<=D}(2^d - 1) (one fresh Mersenne-ish factor per
   degree, ever), so the dyadic clock c must climb ~1 per move — but
   HOLDING reading c requires some place's depth > 2^(c-1) and total
   degree grows only D per move: LINEAR budget vs EXPONENTIAL demand.
   COROLLARY (true dynamics, rule): every untruncated trajectory's
   pick degrees are UNBOUNDED — were picks eventually of degree <= D,
   the tail would be a bounded-alphabet trajectory from its own seed
   and would halt, contradicting the always-nonempty menu. MC (D = 10,
   T = 60): 100/100 runs halt at both betas, median move 13/12, max 13;
   the doubling + odd-budget invariants asserted move-by-move. Over Z
   the same bounded model has an immortal witness: the pure 2-column,
   lambda(2^a) = 2^(a-2) strictly increasing (asserted a = 3..30) —
   m = 2 admissible forever at bounded cost. Equal char: NO infinite
   bounded-alphabet thermal trajectory exists; mixed char: one does
   (the locked column). This is explore_module_law.py's cost divergence
   (bounded-cost tail <=> lock at p^rank) BECOME mortality — cite the
   module law, not a new theorem. And the death is CLOCK-AUTHORED: at
   D = 10 every run dies at the same reading c* = 5 (c-gain exactly 4,
   min = max, at beta = 1.5, 2, 3 — temperature-independent;
   observation), while the halt TIME varies by route. RESOLVED:
   c* = 5 is the closed law c*(D) = floor(log2 D) + 2, and only
   the MODE is temperature-independent — explore_halt_clock.py.

6. WHAT MELTS IS THE SHADOW (rule via finding 4; MC measured before
   the halt). Cold-forever geography dies at every finite beta: x+1
   (starved forever at T = 0) opens in 96/100 runs at beta = 2 (98/100
   at 1.5; median move 3 and 2); the sibling shadow breaks — both
   deg-3 irreducibles open in 7/100 and 12/100 runs within ~13-move
   lives (cold: proved impossible, ch. 18 finding 6); breadth >= 6
   places in 100/100; depth leaves the monopolist (second-place depth
   >= 2 in 93/100, 96/100). Over Z temperature's gift to D-DYN was
   DEPTH (the radical); over F_2[x] cold growth already spends on one
   column's radical while starving breadth, and the gift is BREADTH
   (the shadowed siblings). The gift is characteristic-dependent; the
   discontinuity's seat (beta = infinity) is not.

7. THE TIE-BREAK MELTS (property — the shape of the thermal law).
   Cold F_2[x] REQUIRED a tie-break axis (determinism is archimedean,
   ch. 18). The thermal law takes no tie-break parameter at any finite
   beta: equal-degree moves share weight democratically. The
   archimedean import cold F_2[x] needed is dissolved by temperature —
   the engine has no tie-break argument anywhere.

8. THE DEVIATION LINE BREATHES — THE MODULE LAW'S THERMAL SIGNATURE
   (rule in range a <= 64, beta = 2; exact inside mass, two-sided
   outside brackets). Along the pure x-column the inside mass is an
   exact geometric series (x^r admissible iff a + r > 2^c), so P(pick
   leaves the pure column) oscillates with the DYADIC PHASE of the
   depth: at frontiers a = 4, 8, 16, 32 it is 0.500-0.501 —
   phase-constant ONE HALF (closed form at the frontier, c -> infinity:
   m_in = q/(1-q) = 1/3 and m_out = [Z - smooth] + riders = 2/9 + 1/9 =
   1/3 at q = 1/4) — and one step off the frontier the door recedes to
   2^c - a + 1 and the column melts: P(out) in [0.9989, 1] at a = 33.
   Z's 2-column deviation line was a phase-constant band [0.312, 0.374]
   because the linear pump prices the door at 2 forever. Rank-finite
   linear pump = constant stickiness; rank-infinite log clock = dyadic
   breathing — sticky one move per window, molten the rest.

9. THE MELT'S SEAT (rule via finding 4 + observation for rates). The
   D-DYN limit object is CONSTANT (the full completion) on the whole
   interval beta in (1, infinity): no dynamical transition at the
   clock spectrum's beta_col^g or its window top beta* = 2 — the
   thermal clocks' critical structure belongs to the zeta MEASURE's
   genesis mode, not to the growth dynamics' limit.
   Rates move smoothly and gently (fresh-pick fraction 0.753 / 0.735 /
   0.720 at beta = 1.5 / 2 / 3; 3-point scan, observation). THE
   THE ANSWER: the melt of the sprawl's GEOGRAPHY sits at
   beta = infinity exactly (as Z's lock melt does); the sprawl's
   ESCALATOR — diverging move costs, the forced march up degrees —
   NEVER melts (finding 5: it kills bounded-alphabet growers at every
   temperature). Selection-authored structure melts; module-authored
   structure is temperature-invariant. Between the sprawl and the
   thermal clocks there is no intermediate dynamical phase — only the
   breathing of the frontier.

RUN RECORD (from the green run, 2026-07-10, 386 checks, ~21 s, well
under 512 MB — tables to deg 14 only).
  S1 betas 1.25/1.5/2/3, truncation D = 40, degree law d <= 12 exact.
  S2 exact enumeration: states 1, x, x(x+1) x places x, x+1, x^2+x+1
     x 4 betas, k = 1..4, tolerance 4x truncated-tail fraction (3.5e-1
     at beta = 1.25 honest-loose, 2.4e-4 at beta = 2); MC 1200
     trajectories x 12 moves, D = 10.
  S3 necklace-formula irreducible counts asserted vs the sieve
     (d <= 14); Euler product deg <= 16.
  S4 77,828 divisor pairs; 10 states (5 fixed + 5 MC-reached) x
     betas 1.5, 2 x riders x, x+1, x^2+x+1; menu closure under
     multiplication by x, x+1 within deg <= 10.
  S5 100 trajectories x betas 2, 1.5 from seed x^2, D = 10, T = 60:
     numbers in findings 5-6; invariants asserted every move.
  S6 a = 2..64 at beta = 2, D = 12; frontier-vs-next dip asserted at
     a = 4, 8, 16, 32; mid-window thresholds door >= 4 -> P(out) >
     0.95, door >= 7 -> > 0.99 (hand-derived pre-run).
  S7 100 trajectories x betas 1.5, 2, 3, D = 10: rates + the fixed
     halt clock (min = max = 4 c-gain, all betas).

Companion records: explore_function_field_lock.py (the cold sprawl),
explore_thermal_growth.py (Z's melt),
explore_hot_limit.py (Z's hot limit), explore_module_law.py
(the rank dichotomy this record reads thermally).
"""

import random
from math import gcd

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


# ----------------------------------------------------- F_2[x] on int encodings
def pdeg(a):
    return a.bit_length() - 1


def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pdivmod(a, b):
    q = 0
    db = pdeg(b)
    while a and pdeg(a) >= db:
        s = pdeg(a) - db
        q ^= 1 << s
        a ^= b << s
    return q, a


def pmod(a, b):
    return pdivmod(a, b)[1]


def pmulmod(a, b, m):
    return pmod(pmul(a, b), m)


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


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


def is_irr(f):
    """Rabin irreducibility test on the int encoding."""
    d = pdeg(f)
    if d < 1:
        return False
    if d == 1:
        return True
    if f & 1 == 0:
        return False  # divisible by x
    if bin(f).count("1") % 2 == 0:
        return False  # f(1) = 0
    x = 2
    t = x
    for _ in range(d):
        t = pmulmod(t, t, f)
    if t != x:
        return False
    for p in prime_divisors(d):
        t = x
        for _ in range(d // p):
            t = pmulmod(t, t, f)
        if pgcd(t ^ x, f) != 1:
            return False
    return True


# --------------------------------------------- factor + lambda tables (sieved)
def ceil_log2(a):
    return (a - 1).bit_length()  # a >= 1


def lam_pp(d, a):
    """lambda(g^a) for deg g = d (the char-2 1-unit law, ch. 18/20)."""
    return ((1 << d) - 1) << ceil_log2(a)


def lcm(a, b):
    return a // gcd(a, b) * b


DMAX = 14  # factor/lambda tables cover all monics of degree <= DMAX

_SPF = {}  # monic (deg 1..DMAX) -> smallest (encoding) irreducible factor
_FAC = {}  # monic -> {irr: mult}
_LAM = {}  # monic -> lambda
_IRR_BY_DEG = {}


def build_tables():
    monics = sorted(range(2, 2 << DMAX), key=lambda f: (pdeg(f), f))
    for f in monics:
        if f in _SPF:
            continue
        # f is irreducible (no smaller factor marked it)
        _IRR_BY_DEG.setdefault(pdeg(f), []).append(f)
        # mark multiples f*s for all monic s, deg(f*s) <= DMAX
        for s in range(1, 1 << (DMAX - pdeg(f) + 1)):
            prod = pmul(f, s)
            if pdeg(prod) <= DMAX and prod not in _SPF:
                _SPF[prod] = f
    for f in monics:
        fac = {}
        g = f
        while pdeg(g) >= 1:
            p = _SPF[g]
            fac[p] = fac.get(p, 0) + 1
            g = pdivmod(g, p)[0]
        _FAC[f] = fac
        L = 1
        for p, e in fac.items():
            L = lcm(L, lam_pp(pdeg(p), e))
        _LAM[f] = L


def lam_of_fac(fac):
    L = 1
    for g, e in fac.items():
        L = lcm(L, lam_pp(pdeg(g), e))
    return L


def v2(n):
    return (n & -n).bit_length() - 1


# ------------------------------------------------------------ the thermal menu
def lam_after(state_fac, lam_N, m):
    """lambda(N*m) from the state's places + m's factor table.

    Valid because lam_pp is monotone in depth: unchanged places keep
    their (dividing) contributions inside lam_N."""
    L = lam_N
    for g, e in _FAC[m].items():
        L = lcm(L, lam_pp(pdeg(g), state_fac.get(g, 0) + e))
    return L


def thermal_menu(state_fac, beta, D, demand):
    """Enumerate admissible monics of degree <= D with weights 2^(-beta*deg).

    demand: 'DYN' (lambda-growing) or 'IND' (coprime).
    Returns (moves, weights, mass, free_mass) — free_mass = truncated
    free-law mass, for truncation reporting."""
    lam_N = lam_of_fac(state_fac)
    moves, weights = [], []
    mass = 0.0
    free_mass = 0.0
    for m in range(2, 2 << D):
        dm = pdeg(m)
        if dm < 1 or m >> dm != 1:
            continue
        w = 2.0 ** (-beta * dm)
        free_mass += w
        if demand == "DYN":
            if lam_after(state_fac, lam_N, m) <= lam_N:
                continue
        else:  # IND
            if any(g in state_fac for g in _FAC[m]):
                continue
        moves.append(m)
        weights.append(w)
        mass += w
    return moves, weights, mass, free_mass


def sample(moves, weights, mass, rng):
    t = rng.random() * mass
    acc = 0.0
    for m, w in zip(moves, weights):
        acc += w
        if acc >= t:
            return m
    return moves[-1]


def run_thermal(seed_fac, beta, D, T, demand, rng):
    """One truncated-model thermal trajectory: (final_fac, picks, halted).

    halted = the deg <= D menu emptied before T moves. For D-DYN this
    HAPPENS (the mortality split, S5) — a property of the truncated
    model; the true (untruncated) dynamics always has the fresh door
    at deg = bit_length(lambda) + 1 (ch. 18 finding 3)."""
    fac = dict(seed_fac)
    picks = []
    for _ in range(T):
        moves, weights, mass, _ = thermal_menu(fac, beta, D, demand)
        if not moves:
            return fac, picks, True
        m = sample(moves, weights, mass, rng)
        for g, e in _FAC[m].items():
            fac[g] = fac.get(g, 0) + e
        picks.append(m)
    return fac, picks, False


# ------------------------------------------------------------------- sections
def s1_partition():
    """FM1: rational partition function + geometric degree law."""
    print("== S1 THE RATIONAL PARTITION FUNCTION ==")
    for beta in (1.25, 1.5, 2.0, 3.0):
        r = 2.0 ** (1.0 - beta)
        closed = r / (1.0 - r)
        # truncated sum over degrees (2^d monics of degree d, weight 2^(-beta d))
        Dtr = 40
        trunc = sum((2.0**d) * 2.0 ** (-beta * d) for d in range(1, Dtr + 1))
        tail = r ** (Dtr + 1) / (1.0 - r)  # geometric tail, exact
        ok(trunc <= closed <= trunc + tail + 1e-12,
           f"S1 partition bracket beta={beta}")
        # degree law: P(deg = d) = (1-r) r^(d-1)
        for d in range(1, 13):
            pd = (2.0**d) * 2.0 ** (-beta * d) / closed
            ok(abs(pd - (1.0 - r) * r ** (d - 1)) < 1e-12,
               f"S1 degree law beta={beta} d={d}")
        print(f"  beta={beta}: Z = {closed:.6f} = r/(1-r), r = 2^(1-beta) "
              f"= {r:.4f} (bracket ok, degree law d<=12 exact)")


def s2_depth_law():
    """FM2: D-IND geometric depth law by exact truncated enumeration + MC."""
    print("== S2 THERMAL D-IND: THE DEPTH LAW ==")
    x, x1, g2 = 2, 3, 7  # x, x+1, x^2+x+1
    states = [{}, {x: 1}, {x: 1, x1: 1}]
    for beta in (1.25, 1.5, 2.0, 3.0):
        r = 2.0 ** (1.0 - beta)
        tail_frac = r ** (DMAX + 1) / (1.0 - r) / (r / (1.0 - r))
        for st in states:
            for g in (x, x1, g2):
                if g in st:
                    continue
                dg = pdeg(g)
                moves, weights, mass, _ = thermal_menu(st, beta, DMAX, "IND")
                # mass of picks with v_g = k, k = 1..4
                by_k = {}
                enter = 0.0
                for m, w in zip(moves, weights):
                    k = _FAC[m].get(g, 0)
                    if k:
                        enter += w
                        by_k[k] = by_k.get(k, 0.0) + w
                ratio = 2.0 ** (-beta * dg)
                for k in range(1, 5):
                    pred = ratio ** (k - 1) * (1.0 - ratio)
                    got = by_k.get(k, 0.0) / enter
                    ok(abs(got - pred) < max(4 * tail_frac, 1e-9),
                       f"S2 depth law beta={beta} g={g} k={k}")
        print(f"  beta={beta}: geometric depth law ratio 2^(-beta d) at "
              f"3 states x places (tol {max(4 * tail_frac, 1e-9):.2e})")
    # MC cross-place independence at beta = 2
    rng = random.Random(177)
    beta, NTR = 2.0, 1200
    d1x = d1x1 = joint = 0
    entx = entx1 = 0
    for _ in range(NTR):
        fac, _, _ = run_thermal({}, beta, 10, 12, "IND", rng)
        vx, vx1 = fac.get(x, 0), fac.get(x1, 0)
        if vx:
            entx += 1
            if vx == 1:
                d1x += 1
        if vx1:
            entx1 += 1
            if vx1 == 1:
                d1x1 += 1
        if vx == 1 and vx1 == 1:
            joint += 1
    px, px1 = d1x / NTR, d1x1 / NTR
    pj = joint / NTR
    print(f"  MC independence (beta=2, {NTR} traj): P(v_x=1)={px:.3f}, "
          f"P(v_x+1=1)={px1:.3f}, joint={pj:.3f} vs product={px * px1:.3f}")
    ok(abs(pj - px * px1) <= 0.05, "S2 cross-place independence (MC)")
    # per-entry depth-1 frequency vs 1 - 2^(-beta) = 0.75
    f1 = d1x / entx if entx else 0.0
    print(f"  MC depth-1 at entry (x): {f1:.3f} vs {1 - 2.0**-beta:.3f} predicted"
          f" (entered {entx}/{NTR})")
    ok(abs(f1 - (1 - 2.0**-beta)) <= 0.05, "S2 depth-1 frequency at entry (MC)")
    return f1


def s3_crystal():
    """FM3: crystal probability = 1 - 2^(1-beta) exactly."""
    print("== S3 THE CRYSTAL PROBABILITY ==")
    # irreducible counts by degree (from the sieve, checked vs necklace formula)
    for d in range(1, DMAX + 1):
        # necklace: N_d = (1/d) sum_{e | d} mu(e) 2^(d/e)
        tot = 0
        for e in range(1, d + 1):
            if d % e == 0:
                # mobius of e
                mu, n = 1, e
                for p in prime_divisors(e):
                    if n % (p * p) == 0:
                        mu = 0
                        break
                    mu = -mu
                tot += mu * (1 << (d // e))
        ok(len(_IRR_BY_DEG.get(d, [])) == tot // d, f"S3 irr count d={d}")
    DE = 16  # Euler product over deg <= DE (needs counts beyond DMAX)
    counts = {}
    for d in range(1, DE + 1):
        tot = 0
        for e in range(1, d + 1):
            if d % e == 0:
                mu, n = 1, e
                for p in prime_divisors(e):
                    if n % (p * p) == 0:
                        mu = 0
                        break
                    mu = -mu
                tot += mu * (1 << (d // e))
        counts[d] = tot // d
    import math
    for beta in (1.5, 2.0, 3.0):
        closed = 1.0 - 2.0 ** (1.0 - beta)
        logprod = sum(counts[d] * math.log1p(-2.0 ** (-beta * d))
                      for d in range(1, DE + 1))
        prod = math.exp(logprod)
        # tail bracket: |log tail| <= sum_{d>DE} 2^d/d * 2^(-beta d) * 2
        rr = 2.0 ** (1.0 - beta)
        tail = 2.0 * rr ** (DE + 1) / (1.0 - rr) / (DE + 1)
        ok(prod * math.exp(-tail) <= closed <= prod * math.exp(tail) + 1e-12,
           f"S3 crystal bracket beta={beta}")
        print(f"  beta={beta}: Euler product (deg<={DE}) = {prod:.6f}, "
              f"closed 1 - 2^(1-beta) = {closed:.6f}, bracket width "
              f"{prod * (math.exp(tail) - math.exp(-tail)):.2e}")
    ok(abs((1.0 - 2.0 ** (1.0 - 2.0)) - 0.5) < 1e-15, "S3 beta=2 crystal = 1/2")


def s4_closure():
    """FM4: lambda monotone on divisibility; menu upward-closed; rider bound."""
    print("== S4 UPWARD CLOSURE + THE RIDER BOUND ==")
    # (a) lambda divisibility-monotone: all monic pairs N | N*s, deg <= 12
    pairs = 0
    for N in range(2, 1 << 11):
        dN = pdeg(N)
        if dN < 1 or N >> dN != 1 or dN > 10:
            continue
        for s in range(2, 2 << (12 - dN)):
            ds = pdeg(s)
            if ds < 1 or s >> ds != 1:
                continue
            Ns = pmul(N, s)
            if pdeg(Ns) > 12:
                continue
            assert _LAM[Ns] % _LAM[N] == 0, f"S4 monotone N={N} s={s}"
            pairs += 1
    ok(pairs > 60000, "S4 monotonicity pair count")
    print(f"  lambda(N) | lambda(N*s) on ALL {pairs} monic divisor pairs "
          f"(deg <= 12): upward closure of D-DYN admissibility follows")
    # (b) menu upward closure + (c) rider bound on enumerated thermal menus
    rng = random.Random(178)
    states = [{2: 1}, {2: 2}, {3: 1}, {7: 1}, {2: 1, 3: 1}]
    for _ in range(5):  # 5 MC-reached states for coverage
        fac, _, _ = run_thermal({2: 2}, 2.0, 8, 6, "DYN", rng)
        states.append(fac)
    D = 10
    for beta in (1.5, 2.0):
        for st in states:
            moves, weights, mass, _ = thermal_menu(st, beta, D, "DYN")
            adm = set(moves)
            lam_N = lam_of_fac(st)
            # (b) closure: m admissible, deg(m*s) <= D => m*s admissible
            for m in moves:
                if pdeg(m) > D - 1:
                    continue
                for s in (2, 3):  # multiply by x, x+1
                    ms = pmul(m, s)
                    if pdeg(ms) <= D:
                        assert ms in adm, f"S4 closure m={m} s={s} st={st}"
            ok(True, f"S4 menu closure state={sorted(st)} beta={beta}")
            # (c) rider bound (truncated-honest form):
            # mass(A n (g), deg <= D) >= |g|^(-beta) mass(A, deg <= D - deg g)
            for g in (2, 3, 7):
                dg = pdeg(g)
                mass_low = sum(w for m, w in zip(moves, weights)
                               if pdeg(m) <= D - dg)
                mass_g = sum(w for m, w in zip(moves, weights)
                             if _FAC[m].get(g, 0) >= 1)
                ok(mass_g >= 2.0 ** (-beta * dg) * mass_low - 1e-15,
                   f"S4 rider g={g} state={sorted(st)} beta={beta}")
    print(f"  menu closure + rider mass bound asserted at {len(states)} states "
          f"x 2 betas x riders (x, x+1, x^2+x+1)")


def lamZ_2col(a):
    """Exponent of (Z/2^a)^x: 1, 1, 2, then 2^(a-2)."""
    return 1 if a <= 2 else (2 if a == 3 else 1 << (a - 2))


def s5_mortality_and_melt():
    """FM5 + the mortality split (an unpredicted discovery, found during the run).

    (i) the truncated D-DYN model over F_2[x] is uniformly MORTAL:
    lambda at least doubles per move, its odd part is bounded by
    odd(seed) * prod_{d<=D}(2^d-1), and the depth budget grows only
    linearly — asserted along every MC trajectory, all runs halt.
    (ii) Z's contrast witness: the pure 2-column keeps m = 2
    admissible forever (linear pump) — closed form asserted.
    (iii) melt events before the halt: the shadow's geography dies."""
    print("== S5 THE MORTALITY SPLIT + WHAT MELTS ==")
    x, x1 = 2, 3
    deg3 = [11, 13]  # x^3+x+1, x^3+x^2+1
    NTR, T, D = 100, 60, 10
    B_odd = 1
    for d in range(1, D + 1):
        B_odd *= (1 << d) - 1
    results = {}
    for beta in (2.0, 1.5):
        rng = random.Random(int(beta * 1000))
        x1_open = both3 = many = depth2 = halted_n = 0
        x1_moves, halts = [], []
        for _ in range(NTR):
            # re-run move by move to assert the doubling + odd bound
            fac = {x: 2}
            lam_prev = lam_of_fac(fac)
            picks = []
            halted = False
            for t in range(T):
                moves, weights, mass, _ = thermal_menu(fac, beta, D, "DYN")
                if not moves:
                    halted = True
                    break
                m = sample(moves, weights, mass, rng)
                for g, e in _FAC[m].items():
                    fac[g] = fac.get(g, 0) + e
                lam_now = lam_of_fac(fac)
                assert lam_now % lam_prev == 0 and lam_now >= 2 * lam_prev, \
                    "S5 lambda must at least double per admissible move"
                odd = lam_now >> v2(lam_now)
                assert odd <= B_odd, "S5 odd part exceeds the fresh budget"
                lam_prev = lam_now
                picks.append(m)
            if halted:
                halted_n += 1
                halts.append(len(picks))
            if fac.get(x1, 0):
                x1_open += 1
                for i, m in enumerate(picks):
                    if _FAC[m].get(x1, 0):
                        x1_moves.append(i + 1)
                        break
            if all(fac.get(g, 0) for g in deg3):
                both3 += 1
            if len(fac) >= 6:
                many += 1
            second = sorted(fac.values(), reverse=True)
            if len(second) >= 2 and second[1] >= 2:
                depth2 += 1
        results[beta] = (x1_open, both3, many, depth2, halted_n, halts)
        med = sorted(x1_moves)[len(x1_moves) // 2] if x1_moves else -1
        medh = sorted(halts)[len(halts) // 2] if halts else -1
        print(f"  beta={beta}: HALTED {halted_n}/{NTR} (median halt move "
              f"{medh}, max {max(halts) if halts else -1}); x+1 opens "
              f"{x1_open}/{NTR} (median move {med}), both deg-3 siblings "
              f"{both3}/{NTR}, >=6 places {many}/{NTR}, second-place "
              f"depth>=2 {depth2}/{NTR}")
        ok(halted_n == NTR,
           f"S5 mortality: every truncated-model run halts (beta={beta})")
    # (ii) Z witness: linear pump keeps the bounded alphabet alive forever
    for a in range(3, 31):
        ok(lamZ_2col(a + 1) > lamZ_2col(a),
           f"S5 Z 2-column pump strict at a={a}")
    print("  Z contrast: lambda(2^a) = 2^(a-2) strictly increasing (a=3..30)"
          " — m=2 stays admissible forever: the bounded alphabet is immortal"
          " in mixed characteristic (the module law's thermal dress)")
    # (iii) melt asserts (geography dies before the halt)
    x1o, b3, mny, d2, _, _ = results[2.0]
    ok(x1o >= 95, "S5 x+1 starvation melts (>=95/100, beta=2)")
    # the shadow-melt witness is a COLD-IMPOSSIBLE event (ch. 18 finding 6
    # proves the second same-degree sibling never opens at T = 0): any
    # occurrence is the melt; counts reported above, short lives (~13
    # moves, the mortality above) keep them small
    ok(b3 >= 1, "S5 sibling shadow melts (cold-impossible event observed)")
    ok(results[1.5][1] >= 1, "S5 sibling shadow melts at beta=1.5 too")
    ok(mny >= 80, "S5 breadth: >=6 places in >=80% of runs")
    ok(d2 >= 60, "S5 depth spreads off the monopolist")
    ok(results[1.5][0] >= 95, "S5 x+1 melts at beta=1.5 too")
    return results


def s6_deviation():
    """FM7: the deviation line breathes with dyadic phase along x^a."""
    print("== S6 THE DEVIATION LINE BREATHES ==")
    x = 2
    out = {}
    for beta in (2.0,):
        for a in range(2, 65):
            c = ceil_log2(a)
            # inside mass: pure x-powers x^r, admissible iff a + r > 2^c; EXACT
            rmin = (1 << c) - a + 1
            q = 2.0 ** (-beta)
            m_in = q**rmin / (1.0 - q)
            # outside mass: all admissible non-pure-x monics, deg <= D, bracket
            st = {x: a}
            D = 12
            moves, weights, mass, free_mass = thermal_menu(st, beta, D, "DYN")
            m_out = sum(w for m, w in zip(moves, weights)
                        if _FAC[m].keys() != {x})
            r = 2.0 ** (1.0 - beta)
            tail = r ** (D + 1) / (1.0 - r)  # all monics beyond D
            lo = m_out / (m_out + tail + m_in)
            hi = (m_out + tail) / (m_out + tail + m_in)
            out[(beta, a)] = (lo, hi)
    # frontier dips: P(out) at a = 2^c is a local min of its window
    for c in (2, 3, 4, 5):
        a = 1 << c
        lo_f, hi_f = out[(2.0, a)]
        lo_n, hi_n = out[(2.0, a + 1)]
        ok(hi_f < lo_n, f"S6 frontier dip a={a} vs a+1")
    fr = {a: out[(2.0, a)] for a in (4, 8, 16, 32)}
    print("  frontier P(out) at beta=2: " + ", ".join(
        f"a={a}: [{lo:.3f}, {hi:.3f}]" for a, (lo, hi) in fr.items()))
    # mid-window melt: P(out) -> 1 as the door recedes (the FM7 shape fixed in advance;
    # thresholds hand-derived pre-run: m_out ~ 0.22 at beta = 2, door >= 3
    # gives m_in <= 4^-4/(3/4) ~ 0.005 -> P(out) >~ 0.97; door >= 6 -> 0.999-)
    for a in range(2, 65):
        c = ceil_log2(a)
        door = (1 << c) - a + 1
        if door >= 4 and c >= 3:
            lo, hi = out[(2.0, a)]
            ok(lo > 0.95, f"S6 mid-window melt a={a}")
        if door >= 7 and c >= 3:
            lo, hi = out[(2.0, a)]
            ok(lo > 0.99, f"S6 mid-window deep melt a={a}")
    a_mid = 33
    lo, hi = out[(2.0, a_mid)]
    print(f"  mid-window (a=33, door 32 away): P(out) in [{lo:.6f}, {hi:.6f}]"
          f" — the column melts; Z's 2-column band was [0.312, 0.374]")
    return out


def s7_rate_scan():
    """FM8: rate observables across the clock window — observation tier."""
    print("== S7 THE RATE SCAN (observation) ==")
    x = 2
    NTR, T, D = 100, 30, 10
    rows = []
    for beta in (1.5, 2.0, 3.0):
        rng = random.Random(int(beta * 7000))
        fresh_frac = []
        c_gain = []
        for _ in range(NTR):
            fac = {x: 2}
            lamc0 = v2(lam_of_fac(fac))
            fresh = made = 0
            for _ in range(T):
                moves, weights, mass, _ = thermal_menu(fac, beta, D, "DYN")
                if not moves:
                    break
                m = sample(moves, weights, mass, rng)
                made += 1
                if any(g not in fac for g in _FAC[m]):
                    fresh += 1
                for g, e in _FAC[m].items():
                    fac[g] = fac.get(g, 0) + e
            fresh_frac.append(fresh / made)
            c_gain.append(v2(lam_of_fac(fac)) - lamc0)
        ff = sum(fresh_frac) / NTR
        cg = sum(c_gain) / NTR
        rows.append((beta, ff, cg))
        print(f"  beta={beta}: fresh-pick fraction {ff:.3f}, "
              f"c-growth {cg:.2f} (min {min(c_gain)}, max {max(c_gain)}) "
              f"over each run's life")
        # observed on the first green run and pinned: every run dies at
        # the SAME clock reading — the halt is clock-authored (D = 10)
        ok(min(c_gain) == max(c_gain),
           f"S7 fixed halt clock reading c* (beta={beta})")
    # sanity only: fractions in (0,1), monotone direction reported not asserted
    for beta, ff, cg in rows:
        ok(0.0 < ff < 1.0, f"S7 sane fresh fraction beta={beta}")
        ok(cg > 0.0, f"S7 clock grows beta={beta}")
    return rows


def main():
    import time
    t0 = time.time()
    build_tables()
    ok(_LAM[2] == 1 and _LAM[4] == 2 and _LAM[8] == 4 and _LAM[16] == 4,
       "table sanity: lambda(x)=1, lambda(x^2)=2, lambda(x^3)=4, lambda(x^4)=4")
    ok(_LAM[7] == 3 and _LAM[3] == 1, "table sanity: lambda(x^2+x+1)=3, lambda(x+1)=1")
    s1_partition()
    s2_depth_law()
    s3_crystal()
    s4_closure()
    s5_mortality_and_melt()
    s6_deviation()
    s7_rate_scan()
    print(f"\nALL SECTIONS GREEN — {CHECKS} checks, {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
