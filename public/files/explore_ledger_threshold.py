"""explore_ledger_threshold.py — chamber twenty-eight: the fusion's remainders
(the collision hinge — where alpha->0 goes analytic-hard, and a nontrivial threshold).

THE QUESTION (ROAD P205 face 1). Chamber twenty-seven (explore_complexity_ledger.py)
made a growth FATE depend on the transparency estimate: alpha = log lambda/log phi is
dominated by the non-transparent density (alpha <~ nt_frac), so density -> 1 IMPLIES
alpha -> 0, and a designed COUNT-weighted reserve thrives-for-all-reward iff density -> 1
(threshold rho_c = limsup nt_frac, DEGENERATE at 0 under the conjecture). Two remainders
burn. (i) Is alpha -> 0 provable UNCONDITIONALLY, or is it genuinely analytic (BV/BFI)?
(ii) Is there a DESIGNED growth fate whose threshold is a NONTRIVIAL analytic constant,
not a degenerate 0? VERTIGO: a combinatorial reserve-solvency threshold sitting at an
irrational analytic value.

THE HINGE (found pre-engine, SCRATCH P205): both remainders are the SAME object —
COLLISIONS (a prime power q^a dividing several shifted primes p-1). Let
  N(q^a) = #{prime p <= p_k : q^a | p-1}.
Then EXACTLY (log lcm = sum of increments; log prod = sum with multiplicity):
  log phi(p_k#)    = Sum_{q^a} log q * N(q^a)          [WITH multiplicity]
  log lambda(p_k#) = Sum_{q^a} log q * [N(q^a) >= 1]   [DISTINCT / hit-indicator]
  collision mass   = log phi - log lambda = Sum_{q^a: N>=1} log q * (N(q^a) - 1).
So alpha = log lambda/log phi = 1 - collision/log phi: alpha -> 0 IFF collisions absorb
almost all of capacity. The lcm keeps each hit prime power ONCE; the product pays every
occurrence. That one distinction runs the whole chamber:
  - alpha (distinct) LOSES the collision mass -> analytic-hard to force to 0 (face i);
  - a SIZE reserve that pays every occurrence KEEPS it -> a positive nontrivial
    constant, the Golomb-Dickman constant (face ii).

THE OBJECTS. Primorial schedule (size order); accumulator lambda(p_k#) = lcm(p_i-1).
P+(m) = largest prime factor of m. theta(x) = Sum_{p<=x} log p ~ x (Mertens/PNT).
log phi(p_k#) = Sum_{i<=k} log(p_i - 1) ~ theta(p_k). The complexity-ledger raise at a
non-transparent NEW-prime step is dominated by log P+(p-1) (chamber 27, CL1: new prime
== P+(p-1), 100% in range). Golomb-Dickman constant lambda_GD = 0.6243299... = the mean
of log P+(n)/log n over integers n (a Dickman integral, irrational).

FROZEN SLATE FR1-FR4 (SCRATCH P205; hand-attacked pre-engine. Findings enter by a
SEPARATE post-run edit copying printed output -- BORN FINDINGS-FREE, CLAUDE.md):

  FR1 (the collision identity, property exact -- the spine). log phi = Sum_{q^a} log q *
    N(q^a) and log lambda = Sum_{q^a} log q * [N(q^a)>=1], both EXACT. Their gap is the
    collision mass Sum (N-1)^+ log q, and alpha = 1 - collision/log phi. Assert: log phi
    recomputed via the N(q^a) multiplicity sum == Sum log(p_i-1) (direct); log lambda via
    the [N>=1] indicator sum == the lcm ledger (chamber 27); collision == the difference,
    all to float tol. HAND: k=1e4, log phi ~ theta ~ 1.03e5, log lambda 17237 (ch27),
    alpha 0.165, collision fraction 1 - 0.165 = 0.835.

  FR2 (the mass-locus, observation -- WHERE the complexity lives). log lambda restricted
    to prime powers q^a <= x^{1/5} (the Linnik-guaranteed-hit range, least prime = 1 mod
    q^a is << (q^a)^5) is NEGLIGIBLE, and even q <= sqrt(x) is small: nearly all of
    log lambda is DISTINCT LARGE primes q in (sqrt x, x) -- each the P+ of some shifted
    prime, each hit but counted once. That distinct-large-shifted-prime-factor count is
    the crux (a shifted-prime distribution question). Assert: frac(log lambda from
    q^a <= x^{1/5}) < 1e-3; frac(from q <= sqrt x) < 0.05; frac(from q > sqrt x) > 0.9.
    HAND: x^{1/5}=10.1 -> psi ~ log 2520 = 7.8 vs 17237 (4.5e-4); sqrt x = 324.

  FR3 (the elementary sandwich, argument -- alpha->0 is analytic, not elementary). Linnik
    gives log lambda >= psi(x^{1/5}) ~ x^{1/5} = o(x) (lower); the elementary a-priori
    UPPER bound is psi(x) ~ theta(x) ~ log phi (every prime power < x COULD divide some
    p-1; elementarily NO large q can be excluded), giving only alpha <= 1+o(1). The actual
    alpha (0.165) sits far below the ceiling; the excluded mass IS the collision mass
    (0.835 log phi), whose control is exactly a lower bound on how much large shifted-prime
    factors REPEAT -- a statement in the shifted-prime distribution circle (BV / Fouvry-
    BFI / Fouvry-Tenenbaum). So alpha -> 0 is IMPLIED BY MAP problem 1 (rigorous, ch27's
    domination); converse heuristic (near-equivalence, both hinge on N_nt=o(k)); the
    natural elementary bounds give only alpha <= 1 -- so alpha -> 0 is a consequence of
    the conjecture, not established unconditionally. Assert: psi(x^{1/5})/log phi < alpha < 1 (the sandwich
    holds strictly, in range) and the ceiling psi(x) >= log lambda. HAND: psi(10.1)=7.8,
    log phi~1.03e5 -> lower 7.6e-5 < 0.165 < 1.

  FR4 (the SIZE reserve -- threshold = Golomb-Dickman, observation. FACE ii, the VERTIGO).
    Re-weight the reserve by SIZE, not count: pay the largest-prime-factor size s_p =
    log P+(p-1) of each shifted prime EVERY step (= the ledger raise only on new-prime
    steps -- CL1; transparent and power-bump steps still pay their P+), earn rho*log p.
    R(k) = rho*theta(p_k) - Sum_{i<=k} log P+(p_i - 1). Thrives
    (R -> +inf) iff rho > rho_c = lim Sum log P+(p-1)/theta(p_k) = the shifted-prime
    Golomb-Dickman constant lambda_GD' (~0.6243: Pomerance's conjecture, a THEOREM under
    Elliott-Halberstam -- Granville/Wang, the mean-from-distribution bridge elementary;
    full PD spectrum Bharadwaj-Rodgers arXiv:2402.11884; unconditionally open --
    contact P225). NONTRIVIAL, irrational, UNconditionally positive
    and STABLE -- unlike alpha's decline and unlike ch27's degenerate 0. Assert (the DATA,
    not the algebraically-forced sign): rho_c(k) in (0.5, 0.65) at every milestone and
    NOT decreasing to 0 (contrast alpha); rho_c > alpha always; the mean of
    log P+(p-1)/log(p-1) tracks rho_c and sits below the classical 0.6243 in range
    (finite-x, converging up). Sink below the band, thrive above. HAND: rho_c(1e4)
    expect ~0.56-0.61; rho=0.50 -> sink, rho=0.65 -> thrive.

DESIGN. Thin import-free number theory (mirrors explore_complexity_ledger.py). One pass
over the first K=10000 primes (p_max=104729): grow lcm by tracking running max exponents,
accumulate log lambda / log phi, factor each p-1 by trial division (p-1<=1.05e5, cheap),
record P+(p-1) and the per-prime-power hit counts N(q^a). K=10000: a few seconds, well
under 512 MB, no numpy. All sections assert.

HONEST SCOPE. FR1 is EXACT (lcm/product identities). FR2/FR3 quantities are exact IN RANGE
but the asymptotic reading (mass all in the analytic range; the ceiling gap lives in the
shifted-prime distribution circle) is an ARGUMENT, not a theorem -- alpha -> 0
UNCONDITIONALLY stays open (EQUIVALENT to MAP open problem 1, TOWER.md SVII --
the collision equivalence, explore_collision_equivalence.py; not resolved here). FR4's rho_c is the in-range mean; its
equality to the classical Golomb-Dickman 0.6243 is a theorem under Elliott-Halberstam
(Pomerance's conjecture; Granville/Wang, full PD spectrum Bharadwaj-Rodgers) and open
unconditionally (best tail: Ding-Wang limsup <= -(7/2)log c) -- what is asserted is that the
threshold is a positive, stable, nontrivial constant well away from 0 and from alpha, i.e.
NOT the degenerate ch27 threshold. The incumbent is smooth/rough-shifted-prime analytic
number theory (Fouvry / BFI / Fouvry-Tenenbaum); this chamber MAPS the dependence.

FINDINGS (tiers per CLAUDE.md; run record at bottom; all sections assert).

1. THE COLLISION IDENTITY (property, EXACT -- the spine). With N(q^a) = #{prime
   p <= p_k : q^a | p-1}: log phi(p_k#) = Sum_{q^a} log q * N(q^a) (multiplicity) and
   log lambda(p_k#) = Sum_{q^a} log q * [N(q^a) >= 1] (distinct) -- both recomputed and
   agreeing with the direct Sum log(p_i-1) and the lcm ledger to < 1e-6. Their gap IS
   the collision mass Sum (N-1)^+ log q. At k=10000: log phi = 104389.2, log lambda =
   17237.2 (= chamber 27), collision = 87152.0, so alpha = log lambda/log phi = 0.1651
   and collision/log phi = 0.8349 (sum 1 exactly). Hence alpha -> 0 IFF collisions
   absorb almost all of capacity: the lcm keeps each hit prime power ONCE, the product
   pays every occurrence, and that single distinction is the whole chamber.

2. THE MASS-LOCUS (observation -- WHERE the complexity lives). Nearly all of log lambda
   is DISTINCT LARGE primes: the Linnik-guaranteed mass psi(x^{1/5}) (every prime power
   <= x^{1/5}=10.1 divides some p-1) is 7.83, only 4.5e-4 of log lambda; the mass from
   q <= sqrt(x)=323.6 is 0.0251; the mass from q > sqrt(x) is 0.9749. So the Theta(x)
   mass of the dynamical complexity is entirely in the shifted-prime range q in (sqrt x,
   x): each such q is the largest prime factor P+(p-1) of some shifted prime, hit but
   counted once by the lcm. The crux of alpha -> 0 is therefore a DISTINCT-large-shifted-
   prime-factor count.

3. THE ELEMENTARY SANDWICH (argument -- alpha -> 0 lives in shifted-prime NT). Linnik
   (least prime = 1 mod q^a << (q^a)^5) forces log lambda >= psi(x^{1/5}), so the lower
   bound is psi(x^{1/5})/log phi = 7.5e-5 -> 0; the NATURAL elementary bounds give only
   alpha <= 1 (log lambda = lcm(p-1) | phi = prod(p-1) exactly; the a-priori psi(x)
   ceiling is the same order, no large q being elementarily excludable). The actual
   alpha = 0.1651 sits strictly inside this sandwich, and the excluded mass = the
   collision mass = 0.8349*log phi is exactly what any improvement must supply -- a LOWER
   bound on how much large shifted-prime factors REPEAT, a statement in the shifted-prime
   distribution circle (Bombieri-Vinogradov / Fouvry-BFI / Fouvry-Tenenbaum). alpha -> 0
   is EQUIVALENT to MAP problem 1 (forward: chamber 27's domination alpha <~ nt_frac;
   converse: THE COLLISION EQUIVALENCE, theorem, elementary -- nt_frac - alpha -> 0 via
   the write-once bound, explore_collision_equivalence.py P228), so the VALUE stays open
   exactly as the density conjecture does; the natural elementary bounds on the value give
   only alpha <= 1. (The sandwich locates why the value is hard; the equivalence settles
   the question's shape, not its answer.)

4. THE SIZE RESERVE -- A NONTRIVIAL POSITIVE THRESHOLD (observation. FACE ii, the VERTIGO).
   Re-weight the reserve by SIZE, not count: pay the largest-prime-factor size s_p =
   log P+(p-1) of each shifted prime EVERY step (= the ledger raise only on new-prime
   steps -- CL1; transparent and power-bump steps still pay their P+), earn rho*log p;
   R(k) = rho*theta(p_k) - Sum log P+(p_i-1) thrives iff rho >
   rho_c = lim Sum log P+(p-1)/theta(p_k). rho_c(k) climbs MONOTONE 0.5243 (k=50) ->
   0.5384 (200) -> 0.5630 (1000) -> 0.5791 (10000) -- a nontrivial POSITIVE, stable
   analytic constant, the opposite of chamber 27's degenerate limsup-density 0. Meanwhile
   alpha DECLINES 0.2963 -> 0.1651, and rho_c > alpha at every milestone. The crossover:
   rho = 0.55 sinks (R = -3036), rho = 0.60 thrives (R = +2184), so the threshold sits at
   rho_c ~ 0.58 in range. THE VERTIGO: a purely combinatorial reserve-solvency threshold
   (does the reserve stay solvent for a given reward?) sitting at an IRRATIONAL analytic
   value. Its LIMIT is the Golomb-Dickman constant lambda_GD = 0.6243 under
   Elliott-Halberstam (Dickman governance of P+(p-1): Pomerance's conjecture, conditional
   proof Granville/Wang; unconditionally open -- contact P225),
   but the in-range value does NOT pin it: the POSITIVE CONTROL (same P+ machinery on the
   INTEGERS n <= x) gives the integer mean 0.6636 -> 0.6523, approaching GD from ABOVE,
   while the shifted mean 0.5377 -> 0.5783 approaches from BELOW -- the two STRADDLE 0.6243,
   so finite-x confirms the rig (integer mean in the GD ballpark) and the positive
   nontrivial threshold, but "= lambda_GD" is an asymptotic identification, not a measured
   constant (a theorem under EH, unconditionally open -- contact P225). The vertigo is
   robust to the exact value; the identification is the EH-conditional part.

THE UNIFICATION (chamber headline). Both remainders are the SAME collision structure.
alpha (distinct / lcm) LOSES the collision mass, so it -> 0 -- and forcing that is
analytic-hard, EQUIVALENT to the density conjecture (the collision equivalence,
explore_collision_equivalence.py; face i). The SIZE reserve (multiplicity / product) KEEPS
every occurrence, so its threshold is a positive nontrivial constant (~0.58 in range,
the Golomb-Dickman constant under EH) (face ii, the vertigo). Collisions are the
hinge: the same prime-power repeats that make the count-threshold degenerate-and-hard
make the size-threshold an irrational analytic
value.

RUN RECORD (this file, ~2 s, 14 checks, well under 512 MB, no numpy; all sections assert).
Frozen slate FR1-FR4 hand-attacked pre-engine (SCRATCH P205). Every WORLD-prediction held
on the first complete run: the collision identity (three paths agree < 1e-6, alpha = 0.1651
= chamber 27), the mass-locus (0.975 of log lambda from q > sqrt x, Linnik-guaranteed
psi(x^{1/5}) = 4.5e-4 of it), the elementary sandwich (7.5e-5 < 0.1651 < 1), the size
threshold (rho_c climbs 0.524 -> 0.579, positive & stable, alpha declines 0.296 -> 0.165,
sink 0.55 / thrive 0.60; hand call rho_c(1e4) ~ 0.56-0.61 landed at 0.579). The /check
POSITIVE CONTROL added post-hoc (integer P+ mean, same machinery) revealed the GD picture
is a STRADDLE -- integer 0.664 -> 0.652 (from above), shifted 0.538 -> 0.578 (from below),
GD = 0.6243 between -- so "= lambda_GD" is asymptotic conjecture, downgraded from the
initial "converging toward GD" reading; the positive nontrivial threshold stands.

Chambers: twenty-seven = explore_complexity_ledger.py (the fate that DEPENDS on the
estimate -- alpha <~ nt_frac, the COUNT reserve degenerate at 0); this chamber = the two
remainders resolved through collisions (alpha->0 analytic-hard; the SIZE reserve's positive
nontrivial threshold, Golomb-Dickman under EH). The transparency law = TOWER.md SII/SVII; the density fusion =
explore_transparency_bridge.py (twenty-six); the spectrum functor = explore_conjecture_
bridge.py (twenty-five).
"""

import sys
from math import log

K_MAX = 10000
LAMBDA_GD = 0.6243299885435508   # Golomb-Dickman constant (mean log P+(n)/log n)


# -- number-theory primitives (thin re-decl; mirror the ledger/bridge scripts) --

def primes_up_to(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        i += 1
    return [i for i in range(2, n + 1) if sieve[i]]


def first_k_primes(k):
    bound = int(k * (log(k) + log(log(k)))) + 100
    ps = primes_up_to(bound)
    while len(ps) < k:
        bound *= 2
        ps = primes_up_to(bound)
    return ps[:k]


def lpf_sieve(n):
    """Largest-prime-factor sieve: lpf[m] = P+(m) for 2 <= m <= n (n <= ~1.05e5)."""
    lpf = [0] * (n + 1)
    for i in range(2, n + 1):
        if lpf[i] == 0:            # i prime
            for j in range(i, n + 1, i):
                lpf[j] = i         # last (largest) prime to hit j
    return lpf


def factorize(n):
    """Prime factorization of n by trial division (n <= ~1.05e5 here)."""
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


PASS = 0
FAIL = 0


def ok(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {msg}")


# -- build the trajectory + the full collision ledger --

def build():
    """One pass over the primorial schedule. Track:
      running{q: max exp}  -> lcm ledger (log lambda)
      Nhit{(q,a): count}   -> N(q^a), the hit multiplicity of each prime power
      per-step: transparent?, P+(p-1), log(p-1)
    """
    ps = first_k_primes(K_MAX)
    running = {}
    loglam = 0.0          # via lcm increments
    logphi = 0.0          # via Sum log(p-1)
    Nhit = {}             # (q, a) -> #primes p<=p_k with q^a | p-1
    Pplus = []            # P+(p-1) per step
    logm = []             # log(p-1) per step
    transparent = []      # bool per step
    for k, p in enumerate(ps, start=1):
        m = p - 1
        fac = factorize(m)
        Pp = max(fac) if fac else 1
        # count hits N(q^a): q^a | m for a = 1..v_q(m)
        for q, e in fac.items():
            for a in range(1, e + 1):
                key = (q, a)
                Nhit[key] = Nhit.get(key, 0) + 1
        # lcm increments
        raised = False
        for q, e in fac.items():
            old = running.get(q, 0)
            if e > old:
                loglam += (e - old) * log(q)
                running[q] = e
                raised = True
        tr = (not raised) and (k > 1)   # k=1 opener adds nothing (lambda(2)=1)
        transparent.append(tr)
        Pplus.append(Pp)
        logm.append(log(m) if m > 0 else 0.0)
        logphi += log(m) if m > 0 else 0.0
    return ps, running, loglam, logphi, Nhit, Pplus, logm, transparent


def theta_of(ps):
    return sum(log(p) for p in ps)


# =====================================================================
# FR1 -- THE COLLISION IDENTITY: log phi = Sum N(q^a) log q (multiplicity),
#        log lambda = Sum [N>=1] log q (distinct); gap = collision mass
# =====================================================================

def section_FR1(ps, running, loglam, logphi, Nhit):
    print("FR1  THE COLLISION IDENTITY  -  distinct vs multiplicity (EXACT)")
    # log phi via the multiplicity sum over prime powers
    logphi_mult = sum(cnt * log(q) for (q, a), cnt in Nhit.items())
    # log lambda via the hit-indicator sum over prime powers
    loglam_ind = sum(log(q) for (q, a), cnt in Nhit.items() if cnt >= 1)
    # log lambda via the lcm ledger (direct, chamber 27 path)
    loglam_lcm = sum(e * log(q) for q, e in running.items())
    collision = sum((cnt - 1) * log(q) for (q, a), cnt in Nhit.items() if cnt >= 1)
    ok(abs(logphi_mult - logphi) < 1e-6 * max(1.0, logphi),
       "FR1: log phi (Sum N(q^a) log q, multiplicity) == Sum log(p_i-1) (direct)")
    ok(abs(loglam_ind - loglam_lcm) < 1e-6 * max(1.0, loglam),
       "FR1: log lambda (Sum [N>=1] log q, indicator) == lcm ledger")
    ok(abs(loglam_ind - loglam) < 1e-6 * max(1.0, loglam),
       "FR1: the two log lambda paths agree with the running lcm sum")
    ok(abs((logphi - loglam) - collision) < 1e-6 * max(1.0, logphi),
       "FR1: log phi - log lambda == collision mass Sum (N-1)^+ log q")
    alpha = loglam / logphi
    print(f"    log phi = {logphi:.1f}   log lambda = {loglam:.1f}   "
          f"collision = {collision:.1f}")
    print(f"    alpha = log lambda/log phi = {alpha:.4f}   "
          f"collision/log phi = {collision / logphi:.4f}   (sum = 1)")
    print(f"    => alpha -> 0 IFF collisions absorb ~all of capacity (log phi)")
    print()
    return alpha


# =====================================================================
# FR2 -- THE MASS-LOCUS: nearly all of log lambda is distinct LARGE primes
# =====================================================================

def section_FR2(ps, running, loglam):
    print("FR2  THE MASS-LOCUS  -  the complexity lives in q > sqrt(x)")
    x = ps[-1]
    cut15 = x ** 0.2      # x^{1/5}: Linnik-guaranteed-hit prime powers
    cut12 = x ** 0.5      # sqrt(x)
    # Linnik-guaranteed mass = sum over prime POWERS q^a <= x^{1/5} of log q = psi(x^{1/5})
    # (every such power divides some p-1, so all are present in the lcm).
    mass_le15 = 0.0
    for q, e in running.items():
        a = 1
        while q ** a <= cut15:
            mass_le15 += log(q)
            a += 1
    mass_le_q12 = sum(e * log(q) for q, e in running.items() if q <= cut12)
    mass_gt_q12 = loglam - mass_le_q12
    f15 = mass_le15 / loglam
    fq12 = mass_le_q12 / loglam
    fgt = mass_gt_q12 / loglam
    ok(f15 < 1e-3,
       "FR2: log lambda from q^a <= x^{1/5} (Linnik range) is negligible (<1e-3)")
    ok(fq12 < 0.05,
       "FR2: log lambda from q <= sqrt(x) is small (<0.05)")
    ok(fgt > 0.9,
       "FR2: > 0.9 of log lambda is DISTINCT large primes q in (sqrt x, x)")
    print(f"    x = {x}   x^(1/5) = {cut15:.1f}   sqrt(x) = {cut12:.1f}")
    print(f"    frac(log lambda) from  q^a<=x^(1/5): {f15:.2e}   "
          f"q<=sqrt x: {fq12:.4f}   q>sqrt x: {fgt:.4f}")
    print(f"    => the Theta(x) mass is entirely in the shifted-prime range: each "
          f"large q = P+(p-1) of some p, hit but counted once -> a distinct-large-"
          f"shifted-prime-factor count")
    print()


# =====================================================================
# FR3 -- THE ELEMENTARY SANDWICH: alpha->0 lives in shifted-prime NT (implied by density)
# =====================================================================

def section_FR3(ps, loglam, logphi, alpha):
    print("FR3  THE ELEMENTARY SANDWICH  -  alpha->0 lives in shifted-prime NT")
    x = ps[-1]
    # Linnik lower bound: every prime power <= x^{1/5} is hit (least prime 1 mod q^a
    # is << (q^a)^5), so log lambda >= psi(x^{1/5}).
    cut15 = x ** 0.2
    psi_lo = sum(log(p) for p in ps if p <= cut15)   # ~ psi(x^{1/5}) (primes; +pp small)
    # add prime-power contributions <= x^{1/5}
    pp = 0.0
    for p in ps:
        if p * p > cut15:
            break
        a = 2
        while p ** a <= cut15:
            pp += log(p)
            a += 1
    psi_lo += pp
    # elementary a-priori ceiling: every prime power < x COULD divide some p-1 ~ psi(x)
    psi_hi = logphi  # psi(x) ~ theta(x) ~ log phi (same order); use log phi as the ceiling proxy
    lo_frac = psi_lo / logphi
    ok(lo_frac < alpha < 1.0,
       "FR3: psi(x^{1/5})/log phi < alpha < 1 (the elementary sandwich, strict)")
    ok(loglam <= psi_hi + 1e-9,
       "FR3: log lambda <= psi(x) ~ log phi (the elementary ceiling)")
    collision_frac = 1.0 - alpha
    print(f"    lower psi(x^(1/5))/log phi = {lo_frac:.2e}   alpha = {alpha:.4f}   "
          f"ceiling = 1.0")
    print(f"    the excluded (collision) mass = {collision_frac:.4f} * log phi is what "
          f"analytic control must supply")
    print(f"    => the natural elementary bounds give only alpha <= 1 (lcm | prod; no "
          f"large q excludable); alpha -> 0 needs a lower bound on large-shifted-prime-"
          f"factor REPEATS (BV / Fouvry-BFI), EQUIVALENT to density -> 1 (the collision "
          f"equivalence, explore_collision_equivalence.py)")
    print()


# =====================================================================
# FR4 -- THE SIZE RESERVE: threshold = the Golomb-Dickman constant (FACE ii)
# =====================================================================

def section_FR4(ps, Pplus, logm, transparent):
    print("FR4  THE SIZE RESERVE  -  a nontrivial positive threshold (the VERTIGO)")
    # rho_c(k) = Sum_{i<=k} log P+(p_i-1) / theta(p_k), at milestones
    mile = [50, 200, 1000, 10000]
    mile = [k for k in mile if k <= K_MAX]
    logPplus_cum = 0.0
    theta_cum = 0.0
    loglam_cum = 0.0
    running = {}
    # ratio-mean of log P+(p-1)/log(p-1)
    ratio_sum = 0.0
    ratio_n = 0
    rho_at = {}
    alpha_at = {}
    ratio_at = {}
    for i, p in enumerate(ps):
        m = p - 1
        logPplus_cum += log(Pplus[i])
        theta_cum += log(p)
        # track alpha in parallel (lcm)
        fac = factorize(m)
        for q, e in fac.items():
            if e > running.get(q, 0):
                loglam_cum += (e - running.get(q, 0)) * log(q)
                running[q] = e
        if m > 1:
            ratio_sum += log(Pplus[i]) / log(m)
            ratio_n += 1
        k = i + 1
        if k in mile:
            rho_at[k] = logPplus_cum / theta_cum
            # alpha via lcm / Sum log(p-1)
            logphi_k = sum(logm[:k])
            alpha_at[k] = loglam_cum / logphi_k
            ratio_at[k] = ratio_sum / ratio_n
    # POSITIVE CONTROL (the rig must pass): the INTEGER mean of log P+(n)/log n over
    # n <= x = p_k. This is the statistic that provably -> lambda_GD (Golomb-Dickman);
    # computing it with the same P+ machinery both sanity-checks the rig AND shows how
    # far the SHIFTED-prime mean sits from the integer one in range.
    lpf = lpf_sieve(ps[-1])
    int_num = 0.0
    int_cnt = 0
    int_mean_at = {}
    ptr = 0
    for n in range(2, ps[-1] + 1):
        int_num += log(lpf[n]) / log(n)
        int_cnt += 1
        # snapshot when we pass a milestone x = p_k
        while ptr < len(mile) and n == ps[mile[ptr] - 1]:
            int_mean_at[mile[ptr]] = int_num / int_cnt
            ptr += 1

    rhos = [rho_at[k] for k in mile]
    positive_stable = all(0.5 < r < 0.65 for r in rhos)
    rising = rho_at[mile[-1]] > rho_at[mile[0]]        # climbing, not collapsing (vs alpha)
    above_alpha = all(rho_at[k] > alpha_at[k] for k in mile)
    ok(positive_stable,
       "FR4: rho_c(k) in (0.50, 0.65) at every milestone -- a nontrivial POSITIVE "
       "constant, not ch27's degenerate 0")
    ok(rising, "FR4: rho_c RISES across milestones (contrast alpha, which declines)")
    ok(above_alpha, "FR4: rho_c(k) > alpha(k) at every milestone (size keeps collisions)")
    # positive control + the honest straddle: the integer mean brackets GD from ABOVE,
    # the shifted-prime mean sits BELOW -- so the in-range value does NOT match GD, and
    # "= lambda_GD" is an ASYMPTOTIC (Dickman) conjecture, not a measured constant.
    ok(0.60 < int_mean_at[mile[-1]] < 0.70,
       "FR4 control: integer mean log P+(n)/log n is in the GD ballpark (0.60,0.70) "
       "-- the rig computes P+ correctly")
    ok(ratio_at[mile[-1]] < LAMBDA_GD < int_mean_at[mile[-1]],
       "FR4: in range the shifted mean (below) and integer mean (above) STRADDLE GD "
       "0.6243 -- finite-x does not pin the limit")
    print(f"    {'k':>6} {'rho_c':>7} {'alpha':>7} {'shift-mu':>9} {'int-mu(ctrl)':>13}")
    for k in mile:
        print(f"    {k:>6} {rho_at[k]:>7.4f} {alpha_at[k]:>7.4f} {ratio_at[k]:>9.4f} "
              f"{int_mean_at[k]:>13.4f}")
    # the sink/thrive crossover: report R(K)-sign at a rho grid (the DATA, not the
    # forced sign identity -- the substance is the threshold VALUE ~ rho_c, nontrivial)
    theta_x = theta_cum
    sumP = logPplus_cum
    print(f"    integer mean -> lambda_GD from ABOVE ({int_mean_at[mile[0]]:.3f}->"
          f"{int_mean_at[mile[-1]]:.3f}); shifted -> from BELOW ({ratio_at[mile[0]]:.3f}->"
          f"{ratio_at[mile[-1]]:.3f}); GD classical = {LAMBDA_GD:.4f}")
    print(f"    {'rho':>6} {'R(K)=rho*theta - Sum logP+':>26} {'fate':>16}")
    for rho in [0.40, 0.50, 0.55, 0.60, 0.65, 0.70]:
        R = rho * theta_x - sumP
        print(f"    {rho:>6.2f} {R:>26.1f} "
              f"{('THRIVE (R->inf)' if R > 0 else 'sink'):>16}")
    rho_c_final = rho_at[mile[-1]]
    print(f"    => threshold rho_c = {rho_c_final:.4f} (in range): a nontrivial POSITIVE, "
          f"stable analytic constant -- NOT ch27's degenerate 0.")
    print(f"       -> Golomb-Dickman under EH (Dickman governance of P+(p-1); open "
          f"unconditionally), and the in-range value straddles GD, not pins it.")
    print()


def main():
    print("=" * 72)
    print("CHAMBER TWENTY-EIGHT  -  the fusion's remainders (the collision hinge)")
    print("=" * 72)
    ps, running, loglam, logphi, Nhit, Pplus, logm, transparent = build()
    n_tr = sum(transparent)
    print(f"trajectory: primorial schedule k=1..{K_MAX}, p_max={ps[-1]}; "
          f"transparent steps={n_tr}, non-transparent={K_MAX - n_tr}\n")
    alpha = section_FR1(ps, running, loglam, logphi, Nhit)
    section_FR2(ps, running, loglam)
    section_FR3(ps, loglam, logphi, alpha)
    section_FR4(ps, Pplus, logm, transparent)
    print("=" * 72)
    print(f"CHECKS: {PASS} passed, {FAIL} failed")
    print("=" * 72)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
