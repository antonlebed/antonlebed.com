"""explore_reserve_zoo.py -- the reserve zoo (the constant-realizer).

THE QUESTION. A companion script (explore_ledger_threshold.py) built two designed
reserves whose solvency thresholds are named constants: a COUNT reserve (degenerate 0)
and a SIZE reserve (Golomb-Dickman ~0.6243). That work left a THIRD weighting at a
different constant open -- but with a warning: a shrinking third target usually means
the real question is "which constants are reachable AS thresholds?" This script answers
that broader question rather than hunting one constant.

THE FRAME (the realizer principle). For any prime-indexed cost w(p) >= 0, the reserve
  R(k) = rho*theta(p_k) - Sum_{i<=k} w(p_i),     theta(p_k) = Sum_{i<=k} log p_i
thrives (R -> +inf) iff rho > rho_c(w) = lim Sum w(p_i)/theta(p_k) -- the Cesaro
log-average of the weight, when it converges. PROOF: R(k) = theta(p_k)*[rho - S(k)/theta]
with S(k) = Sum w(p_i); if S/theta -> L then rho > L gives +inf, rho < L gives -inf, so
rho_c = L. So EVERY nonnegative value is trivially a reachable threshold (w = c*log p gives
rho_c = c exactly), and the lateral-escape content is therefore NOT which values are
reachable -- all of [0, inf) are -- but which STRUCTURED weights realize which NAMED analytic
constants. explore_ledger_threshold.py's SIZE reserve is the weight w = log P+(p-1) = the j=1 member of the
rank family below; this frame relocates the third-weighting question (rule) from reachability
to the structured zoo it realizes.

TWO STRUCTURED SUB-FAMILIES populate the zoo.

  FAMILY A -- RANK (a Poisson-Dirichlet spectrum, thresholds SUM TO 1). Weight
    w_j(p) = log P_j(p-1), the j-th LARGEST prime factor of p-1 with multiplicity
    (0 if p-1 has fewer than j prime factors). rho_c^(j) = lim Sum log P_j(p_i-1)/theta.
    CONSERVATION (exact per k): Sum_j w_j(p) = log(p-1) (the product of all prime factors
    with multiplicity is p-1), so Sum_j S_j(k) = Sum_i log(p_i-1) = log phi(p_k#) and
    Sum_j rho_c^(j)(k) = log phi/theta -> 1 (elementary: log(p-1) = log p + log(1-1/p),
    Sum log(1-1/p) = O(log log x) = o(x)). The rank thresholds SUM TO 1 -- a conserved
    constellation neither explore_complexity_ledger.py's nor explore_ledger_threshold.py's
    degenerate count-reserve had an analog of. The values
    are conjecturally the PD(1) / Shepp-Lloyd expectations {0.6243, ~0.210, ~0.088, ...}
    of the Dickman ordered factorization: j=1 = explore_ledger_threshold.py's SIZE threshold
    EXACTLY (same object; its limit conjecturally lambda_GD), j=2 ~ 0.21 the "third named
    constant" that motivated this script.

  FAMILY B -- DENSITY (any prime-density event realizes its density as a threshold, a
    DIFFERENT KIND than Dickman size). Weight w(p) = log p * 1[E(p)] for a density-delta
    event E; rho_c = delta (a log-weighted density = the natural density, PNT-in-AP).
    - E = "p == 1 mod 4"                -> delta = 1/2 (rational; Dirichlet/Chebotarev).
    - E = "2 is a primitive root mod p" -> delta = ARTIN's constant A = 0.3739558...
      (irrational; NOT a single Chebotarev class -- an infinite Kummer intersection,
      hence Hooley under GRH). Cheap: 2 is a primitive root iff for every prime
      q | (p-1), 2^((p-1)/q) != 1 (mod p); the factorization of p-1 is already in hand,
      and base 2 carries no Artin correction.

PREDICTIONS FR1-FR4 (fixed before the run; findings enter by a separate post-run
edit copying printed output):

  FR1 (the realizer identity, rule). rho_c(w) = lim Sum w/theta governs thrive/sink.
    Assert on KNOWN weights: w = log p gives rho_c = 1 EXACT (R = (rho-1) theta; sink at
    rho=0.9, thrive at rho=1.1); w = (1/2) log p gives rho_c = 1/2 EXACT; and the SIZE
    weight w = log P+(p-1) reproduces explore_ledger_threshold.py's rho_c(1e4) in (0.57, 0.59). Hand estimate:
    controls exact; SIZE ~0.579.

  FR2 (the rank family + conservation). (a) EXACT per k: Sum_{j>=1} S_j(k) = log phi
    (float tol), so Sum_j rho_c^(j)(k) = log phi/theta in (0.99, 1.0), -> 1. HAND k=1e4:
    log phi ~ 104389, log phi/theta ~ 0.9968. (b) ordered decreasing rho_c^(1) >
    rho_c^(2) > rho_c^(3) > 0, hand estimate ~0.58, ~0.20, ~0.09. (c) rho_c^(1) EQUALS explore_ledger_threshold.py's
    SIZE threshold (same object). (d) integer control mean(log P_j(n)/log n, n<=x) tracks
    the same decreasing spectrum and sits ABOVE the shifted mean for j=1 (a straddle
    already observed); int j=1 in (0.60,0.70), j=2 in (0.15,0.25), j=3 in (0.05,0.12). Conjectural
    limits = the Shepp-Lloyd / PD constants (cited, not asserted-exact).

  FR3 (the density family / Artin, observation). w = log p * 1[2 prim root mod p]:
    log-weighted density in (0.33, 0.42), a positive constant DISTINCT from the size
    family (conjecturally Artin 0.37396). Anchor w = log p * 1[p == 1 mod 4] -> (0.47,
    0.53) (conjecturally 1/2). The threshold IS the density -- a DIFFERENT KIND of constant
    (a density: Dirichlet for the anchor, Artin for the primitive root) than the size
    family's Dickman averages. Hand estimate: Artin ~0.373 (from
    below), 1-mod-4 ~0.500.

  FR4 (the realizer + the zoo table, argument -- the headline). The map w |-> rho_c(w)
    realizes ANY nonnegative prime log-average as a solvency threshold; every value is
    trivially reachable by scaling (w = c*log p), so the content is which STRUCTURED weights
    hit which NAMED constants, charted by two families (rank -> a PD spectrum with Sum = 1;
    density -> the density itself). The zoo prints three named irrational
    constants as reserve thresholds -- Golomb-Dickman 0.6243 (rank 1), the PD second
    moment ~0.21 (rank 2), Artin 0.3739 (density) -- plus rational anchors (1/2, and 1.0
    for w = log p), all mutually distinct in range. THIS is the lateral escape EXECUTED:
    not one third constant but the realizer principle + a conserved infinite family + a
    different-kind constant. The headline: designed-growth solvency thresholds realize the
    analytic-prime-constant zoo, and the size-rank thresholds are a conserved
    Poisson-Dirichlet spectrum partitioning the whole log budget (Sum -> 1).

DESIGN. Thin import-free number theory (mirrors explore_ledger_threshold.py). One pass
over the first K=10000 primes (p_max=104729): factor each p-1 by trial division, record
the sorted-descending prime factors with multiplicity (rank family), the base-2 primitive-
root flag and the p==1 mod 4 flag (density family), log(p-1) and log p. Integer control
spectrum via an SPF sieve to x. K=10000: ~0.1 s, well under 512 MB, no numpy. All
sections assert.

HONEST SCOPE. FR1 is a rule (elementary calculus of the reserve drift). FR2's conservation
is EXACT per k (a product identity) and -> 1 elementarily (rule); the rank VALUES' equality
to the exact PD / Shepp-Lloyd constants is a THEOREM under Elliott-Halberstam (level of
distribution 1 => the full joint PD(1) law, Bharadwaj-Rodgers arXiv:2402.11884 Thm 7;
the bridge from distributional convergence to these Cesaro log-averages is elementary --
ratios bounded by 1 carry the means, partial summation carries the log-weighting;
Pomerance's conjecture, j=1 Granville/Wang; shifted primes hold level 1/2 = BV
unconditionally, buying only restricted-support PD correlations -- open)
-- what is asserted is the ordered, positive, summing-to-1
spectrum and the j=1 identity with explore_ledger_threshold.py. FR3's threshold = density is a rule; the
value = Artin's constant is conjectural (Hooley/GRH). FR4 is the argument that the reserve
construction is a universal realizer of prime log-averages; the incumbent is analytic prime
number theory (Dickman/Golomb-Dickman for the size family, Artin/Hooley for the density
family). CAVEAT (do not over-read the vertigo): the realizer does NOT derive these constants
-- rho_c(w) IS the prime log-average of w by construction, so each named constant enters as
the average it already is (a Dickman integral, a Kummer density). The content is the
UNIFICATION (disparate constants as one construction's solvency thresholds) and the RANK
CONSERVATION (Sum -> 1, a genuine structural law here), not any new analytic result: the
reserve computes nothing the incumbent does not. The vertigo is that a designed-growth
economy's solvency boundary IS exactly these constants. The Dirichlet-abscissa
solvency mechanism (a geometric rather than Cesaro criterion), left open here as a
possible third kind, was settled by explore_abscissa_reserve.py: NO third constant --
the abscissa is the settled end.

FINDINGS (run record at bottom; all sections assert).

1. THE REALIZER IDENTITY (rule -- the frame). For any prime weight w(p) >= 0 the reserve
   R(k) = rho*theta(p_k) - Sum w(p_i) thrives iff rho > rho_c(w) = lim Sum w/theta.
   Verified on controls: w = log p realizes rho_c = 1.000000 EXACT (R sinks -10439 at
   rho=0.9, thrives +10439 at rho=1.1), w = (1/2) log p realizes 0.500000 EXACT, and the
   SIZE weight w = log P+(p-1) reproduces explore_ledger_threshold.py's rho_c = 0.5791. So the map
   w |-> rho_c(w) sends any nonnegative prime weight to its Cesaro log-average; EVERY value
   in [0, inf) is trivially reachable (w = c*log p gives rho_c = c, as the two controls show),
   so the content is NOT which values are reachable -- all are -- but which
   STRUCTURED weights realize which NAMED constants (findings 2-3).

2. THE RANK FAMILY -- A CONSERVED PD SPECTRUM SUMMING TO 1 (property + rule; values
   observation). Weight w_j(p) = log P_j(p-1) (j-th largest prime factor, multiplicity).
   The thresholds are an ordered, positive, decreasing spectrum. The weights PARTITION
   log(p-1) EXACTLY (Sum_j log P_j(p-1) = log(p-1), a product identity, every k), so the
   full sum is log phi/theta -> 1 (rule: log(p-1) ~ log p elementarily) -- the LIMITING
   thresholds sum to 1, the in-range sum 0.999971. At k=10^4: rho_c^(1..3) = 0.5791, 0.1931,
   0.0980 with tail (ranks >= 4) 0.1298, total 0.999971. rho_c^(1) = explore_ledger_threshold.py's SIZE threshold
   EXACTLY (same object). The values are in the limit the Poisson-Dirichlet(1) /
   Shepp-Lloyd expectations of the Dickman ordered factorization {0.6243, ~0.210, ~0.088}
   -- a theorem under EH, open unconditionally (see HONEST SCOPE above):
   the integer positive control mean(log P_j(n)/log n) = [0.6523, 0.2006, 0.0789] sits in
   those bands and (at j=1) ABOVE the shifted rho_c^(1) = 0.5791 -- the straddle noted above, so
   the exact identification with the PD constants is EH-conditional, the ordered
   summing-to-1 spectrum the measured fact. Rank 2 ~ 0.19-0.21 IS the "third named
   constant" that motivated this script -- but it arrives inside an infinite conserved family.

3. THE DENSITY FAMILY -- A THRESHOLD IS A DENSITY (rule; value conjectural). Weight
   w(p) = log p * 1[E(p)] for a density-delta event E realizes rho_c = delta (log-weighted
   = natural density). Base-2 primitive-root: 0.3749 at k=10^4 (conjecturally Artin's
   constant A = 0.3740, Hooley/GRH); p == 1 mod 4: 0.4987 -> 1/2 (Dirichlet, rational).
   The Artin threshold is DISTINCT from 1/2 -- a density constant (Artin is an infinite
   Kummer intersection, GRH; the anchor Dirichlet), a DIFFERENT KIND than the Dickman
   size-averages of finding 2.

4. THE REALIZER + THE ZOO (argument -- the headline). The reserve construction is a
   UNIVERSAL REALIZER: w |-> rho_c(w) realizes any nonnegative prime log-average as a
   solvency threshold -- so every value in [0, inf) is reachable (trivially, by scaling
   w = c*log p), and the content is which STRUCTURED weights land on which NAMED constants,
   charted by two families -- RANK (a PD spectrum with Sum = 1) and DENSITY (the density
   itself). Three named irrational constants appear as reserve thresholds,
   mutually distinct and ORDERED in range: PD_2 0.1931 < Artin 0.3749 < Golomb-Dickman
   0.5791, alongside rational anchors (1/2 for p==1 mod4, 1.0 for w=log p). This is the
   broader answer worked out above: not one third constant but the
   realizer principle + a conserved infinite family + a different-kind constant.

THE HEADLINE. Designed-growth solvency thresholds realize the
analytic-prime-constant zoo -- Golomb-Dickman, the Poisson-Dirichlet spectrum, Artin --
and the size-RANK thresholds are a CONSERVED Poisson-Dirichlet constellation that partitions
the whole log budget (Sum -> 1; the partition Sum_j log P_j = log(p-1) exact, in-range
0.99997), a conservation neither explore_complexity_ledger.py's nor explore_ledger_threshold.py's
degenerate count-reserve had an analog of.
The single lever is the weight w: SIZE-by-rank tiles the log budget (a Dickman
spectrum); DENSITY reads a density constant (Artin) off a fixed-density event.

RUN RECORD (this file, ~0.1 s, 16 checks, well under 512 MB, no numpy; all sections assert).
Predictions FR1-FR4 were worked out by hand before the run. Every predicted value held
on the first complete run: the realizer controls (1.000000 / 0.500000 exact, SIZE 0.5791 =
explore_ledger_threshold.py), the rank spectrum (0.5791 > 0.1931 > 0.0980, tail 0.1298, total 0.999971 -> 1;
rank 1 = explore_ledger_threshold.py), the integer straddle control ([0.6523, 0.2006, 0.0789] in the PD
bands, j=1 above shifted), the density family (2-primroot 0.3749 ~ Artin 0.3740, p==1 mod4
0.4987 ~ 1/2), the ordered distinct zoo (PD_2 < Artin < GD). Hand estimates (rho_c^(1..3) ~
0.58/0.20/0.09; conservation ~1; Artin ~0.373; 1-mod-4 ~0.5) all landed. A PARTITION check
verifies this independently of the conservation check above: the conservation total_at -> 1 uses log(p-1)
directly, so it could not catch a factorization bug corrupting the rank spectrum; the
direct check Sum_{q^e||p-1} e*log q = log(p-1) at every prime (max dev < 1e-9) verifies
the EXACT property and factorization completeness independently (adversarially confirmed:
a dropped factor drives the deviation to ~9).

Companion script: explore_ledger_threshold.py (the collision hinge -- the COUNT
reserve degenerate 0, the SIZE reserve Golomb-Dickman); this script generalizes the SIZE
reserve to the realizer principle (the rank family Sum=1, the density family Artin).
"""

import sys
from math import log

K_MAX = 10000
J_MAX = 3                                    # named ranks (P_1, P_2, P_3)
LAMBDA_GD = 0.6243299885435508               # Golomb-Dickman = mean log P+(n)/log n
SHEPP_LLOYD = [0.6243299885, 0.2095808742, 0.0883160989]  # PD(1) expectations (display only)
ARTIN = 0.3739558136192023                   # Artin's constant (base-2 primitive-root density)


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


def sorted_factors_desc(fac):
    """The prime factors of a factorization dict, WITH multiplicity, descending."""
    out = []
    for q in sorted(fac, reverse=True):
        out.extend([q] * fac[q])
    return out


def is_two_primitive_root(p, fac_pm1):
    """Is 2 a primitive root mod the odd prime p?  fac_pm1 = factorize(p-1)."""
    if p == 2:
        return False
    pm1 = p - 1
    for q in fac_pm1:
        if pow(2, pm1 // q, p) == 1:
            return False
    return True


def spf_sieve(n):
    """Smallest-prime-factor sieve: spf[m] = least prime factor of m, 2 <= m <= n."""
    spf = list(range(n + 1))
    i = 2
    while i * i <= n:
        if spf[i] == i:                      # i prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def factor_via_spf(n, spf):
    """Descending prime factors of n WITH multiplicity, via the SPF sieve."""
    out = []
    while n > 1:
        out.append(spf[n])
        n //= spf[n]
    out.sort(reverse=True)
    return out


PASS = 0
FAIL = 0


def ok(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {msg}")


# -- build the trajectory --

def build():
    """One pass over the primorial schedule. Per prime p record:
      Prank[i]  = [log P_1(p-1), .., log P_J(p-1)]   (0 past the factor count)
      logm[i]   = log(p-1)
      logp[i]   = log p
      pr2[i]    = 1[2 is a primitive root mod p]
      p1mod4[i] = 1[p == 1 mod 4]
      Pplus[i]  = P+(p-1)  (= rank-1 factor; ties explore_ledger_threshold.py)
    """
    ps = first_k_primes(K_MAX)
    Prank = []
    logm = []
    logp = []
    pr2 = []
    p1mod4 = []
    Pplus = []
    for p in ps:
        m = p - 1
        fac = factorize(m)
        facs = sorted_factors_desc(fac)                      # descending, with multiplicity
        row = [log(facs[j]) if j < len(facs) else 0.0 for j in range(J_MAX)]
        Prank.append(row)
        logm.append(log(m) if m > 1 else 0.0)
        logp.append(log(p))
        pr2.append(1 if is_two_primitive_root(p, fac) else 0)
        p1mod4.append(1 if p % 4 == 1 else 0)
        Pplus.append(facs[0] if facs else 1)
    return ps, Prank, logm, logp, pr2, p1mod4, Pplus


# =====================================================================
# FR1 -- THE REALIZER IDENTITY: rho_c(w) = lim Sum w/theta governs thrive/sink
# =====================================================================

def section_FR1(ps, logp, Pplus):
    print("FR1  THE REALIZER IDENTITY  -  rho_c(w) = lim Sum w/theta (rule)")
    theta = sum(logp)
    # control weights with exact averages
    w_full = sum(logp)                       # w = log p  -> rho_c = 1
    w_half = 0.5 * sum(logp)                 # w = (1/2)log p -> rho_c = 1/2
    rc_full = w_full / theta
    rc_half = w_half / theta
    ok(abs(rc_full - 1.0) < 1e-12, "FR1: w = log p realizes rho_c = 1 (exact)")
    ok(abs(rc_half - 0.5) < 1e-12, "FR1: w = (1/2) log p realizes rho_c = 1/2 (exact)")
    # R-sign crossover matches rho_c for w = log p: R = (rho-1) theta
    R_sink = 0.9 * theta - w_full
    R_thrive = 1.1 * theta - w_full
    ok(R_sink < 0 < R_thrive, "FR1: reserve sinks below / thrives above rho_c (w=log p)")
    # the SIZE weight reproduces explore_ledger_threshold.py
    w_size = sum(log(Pplus[i]) for i in range(len(ps)))
    rc_size = w_size / theta
    ok(0.57 < rc_size < 0.59, "FR1: w = log P+(p-1) reproduces the SIZE threshold rho_c ~ 0.579")
    print(f"    theta(p_k) = {theta:.1f}   (k={len(ps)}, p_max={ps[-1]})")
    print(f"    w=log p     -> rho_c = {rc_full:.6f}   (R sink@0.9 = {R_sink:.1f}, "
          f"thrive@1.1 = {R_thrive:.1f})")
    print(f"    w=(1/2)log p-> rho_c = {rc_half:.6f}")
    print(f"    w=log P+(p-1) (SIZE, ch28) -> rho_c = {rc_size:.4f}")
    print(f"    => any nonnegative prime weight realizes its log-average as a threshold")
    print()


# =====================================================================
# FR2 -- THE RANK FAMILY: a PD spectrum whose thresholds SUM TO 1
# =====================================================================

def section_FR2(ps, Prank, logm, logp):
    print("FR2  THE RANK FAMILY  -  a Poisson-Dirichlet spectrum, thresholds sum to 1")
    mile = [k for k in [50, 200, 1000, 10000] if k <= K_MAX]
    # cumulative rank sums S_j(k) and theta(k), plus log phi(k) = Sum log(p-1)
    Sj_cum = [0.0] * J_MAX
    theta_cum = 0.0
    logphi_cum = 0.0
    rho_at = {}                              # k -> [rho_c^(1..J)]
    rest_at = {}                             # k -> rho_c over ranks > J
    total_at = {}                            # k -> Sum_all_j rho_c^(j) = log phi/theta
    for i, p in enumerate(ps):
        for j in range(J_MAX):
            Sj_cum[j] += Prank[i][j]
        theta_cum += logp[i]
        logphi_cum += logm[i]
        k = i + 1
        if k in mile:
            rho_at[k] = [Sj_cum[j] / theta_cum for j in range(J_MAX)]
            total_at[k] = logphi_cum / theta_cum
            rest_at[k] = total_at[k] - sum(rho_at[k])
    K = mile[-1]
    # (a0) THE PARTITION IDENTITY (the EXACT property behind the conservation), verified
    # DIRECTLY and independently of logphi_cum: for every prime, the logs of ALL prime
    # factors of p-1 (re-derived, with multiplicity) sum to log(p-1). This is the
    # load-bearing exactness AND a completeness check on factorize -- a dropped factor
    # would corrupt the rank spectrum while the total_at conservation (which uses
    # log(p-1) directly, not the ranks) still passed.
    max_part_dev = 0.0
    for p in ps:
        m = p - 1
        if m <= 1:
            continue
        part = sum(e * log(q) for q, e in factorize(m).items())
        max_part_dev = max(max_part_dev, abs(part - log(m)))
    ok(max_part_dev < 1e-9,
       "FR2: Sum over ALL ranks of log P_j(p-1) = log(p-1) exactly (the partition, "
       "every prime; factorization complete)")
    # (a) conservation: Sum_all_j rho_c^(j) = log phi/theta, and Sum_j S_j == log phi
    ok(0.99 < total_at[K] < 1.0,
       "FR2: Sum_all_j rho_c^(j) = log phi/theta in (0.99, 1.0) -> 1 (conservation)")
    ok(rest_at[K] > 0,
       "FR2: the tail (ranks > J) carries the residual mass (positive)")
    # (b) ordered decreasing, positive
    rr = rho_at[K]
    ok(rr[0] > rr[1] > rr[2] > 0,
       "FR2: rho_c^(1) > rho_c^(2) > rho_c^(3) > 0 (ordered spectrum)")
    # (c) rank-1 == the SIZE threshold (explore_ledger_threshold.py)
    ok(0.57 < rr[0] < 0.59,
       "FR2: rho_c^(1) equals the SIZE threshold (~0.579)")
    # (d) integer control spectrum: mean(log P_j(n)/log n) over n <= x
    spf = spf_sieve(ps[-1])
    int_sum = [0.0] * J_MAX
    int_cnt = 0
    int_at = {}
    ptr = 0
    milestone_x = [ps[k - 1] for k in mile]
    for n in range(2, ps[-1] + 1):
        facs = factor_via_spf(n, spf)
        ln = log(n)
        for j in range(J_MAX):
            if j < len(facs):
                int_sum[j] += log(facs[j]) / ln
        int_cnt += 1
        while ptr < len(mile) and n == milestone_x[ptr]:
            int_at[mile[ptr]] = [int_sum[j] / int_cnt for j in range(J_MAX)]
            ptr += 1
    ic = int_at[K]
    ok(0.60 < ic[0] < 0.70 and 0.15 < ic[1] < 0.25 and 0.05 < ic[2] < 0.12,
       "FR2 control: integer spectrum in the PD/Shepp-Lloyd bands (rig computes P_j)")
    ok(ic[0] > rr[0],
       "FR2: integer mean (above) exceeds shifted rho_c^(1) (below) -- the straddle")
    print(f"    {'k':>6} {'rho_c^1':>8} {'rho_c^2':>8} {'rho_c^3':>8} {'tail':>7} "
          f"{'Sum(=logphi/th)':>16}")
    for k in mile:
        r = rho_at[k]
        print(f"    {k:>6} {r[0]:>8.4f} {r[1]:>8.4f} {r[2]:>8.4f} {rest_at[k]:>7.4f} "
              f"{total_at[k]:>16.6f}")
    print(f"    integer control (mean log P_j(n)/log n, n<=x): "
          f"[{ic[0]:.4f}, {ic[1]:.4f}, {ic[2]:.4f}]")
    print(f"    Shepp-Lloyd / PD(1) reference (conjectural limits): "
          f"[{SHEPP_LLOYD[0]:.4f}, {SHEPP_LLOYD[1]:.4f}, {SHEPP_LLOYD[2]:.4f}]  (sum 1)")
    print(f"    => the rank thresholds partition the log budget (Sum -> 1, a conserved "
          f"spectrum); rank 1 = ch28 SIZE (-> Golomb-Dickman conj), rank 2 the 'third constant'")
    print()
    return rr


# =====================================================================
# FR3 -- THE DENSITY FAMILY: any density realizes as a threshold (Artin)
# =====================================================================

def section_FR3(ps, logp, pr2, p1mod4):
    print("FR3  THE DENSITY FAMILY  -  a threshold IS a density (Artin, a different kind)")
    mile = [k for k in [50, 200, 1000, 10000] if k <= K_MAX]
    num_pr2 = 0.0
    num_p14 = 0.0
    theta_cum = 0.0
    d_pr2_at = {}
    d_p14_at = {}
    for i in range(len(ps)):
        theta_cum += logp[i]
        if pr2[i]:
            num_pr2 += logp[i]
        if p1mod4[i]:
            num_p14 += logp[i]
        k = i + 1
        if k in mile:
            d_pr2_at[k] = num_pr2 / theta_cum
            d_p14_at[k] = num_p14 / theta_cum
    K = mile[-1]
    ok(0.33 < d_pr2_at[K] < 0.42,
       "FR3: base-2 primitive-root log-density in (0.33, 0.42) -- a positive constant")
    ok(0.47 < d_p14_at[K] < 0.53,
       "FR3: p == 1 mod 4 log-density -> 1/2 (rational Dirichlet anchor)")
    ok(abs(d_pr2_at[K] - 0.5) > 0.05,
       "FR3: the Artin threshold is DISTINCT from the 1/2 anchor (a different constant)")
    print(f"    {'k':>6} {'2-primroot':>11} {'p=1mod4':>9}")
    for k in mile:
        print(f"    {k:>6} {d_pr2_at[k]:>11.4f} {d_p14_at[k]:>9.4f}")
    print(f"    conjectural limits: Artin A = {ARTIN:.4f} (2-primroot),  1/2 (p=1 mod4)")
    print(f"    => a density-delta event realizes delta as a threshold -- a density "
          f"constant (Artin, GRH), a DIFFERENT KIND than the Dickman size family")
    print()
    return d_pr2_at[K], d_p14_at[K]


# =====================================================================
# FR4 -- THE REALIZER + THE ZOO TABLE (the headline)
# =====================================================================

def section_FR4(rr, d_pr2, d_p14):
    print("FR4  THE REALIZER + THE ZOO  -  which constants are reachable as thresholds")
    zoo = [
        ("w = log p",              "rational",   1.0,        1.0),
        ("rank 2  log P_2(p-1)",   "PD / SL_2",  SHEPP_LLOYD[1], rr[1]),
        ("2-primroot density",     "Artin",      ARTIN,      d_pr2),
        ("p == 1 mod 4 density",   "rational",   0.5,        d_p14),
        ("rank 1  log P+(p-1)",    "Golomb-Dickman", LAMBDA_GD, rr[0]),
    ]
    # the three IRRATIONAL named constants realized must be mutually distinct in range
    vals = [rr[0], rr[1], d_pr2]             # GD, PD_2, Artin (in-range)
    distinct = (abs(vals[0] - vals[1]) > 0.1 and abs(vals[0] - vals[2]) > 0.1
                and abs(vals[1] - vals[2]) > 0.1)
    ok(distinct,
       "FR4: the three named irrational thresholds (GD, PD_2, Artin) are distinct in range")
    ok(rr[1] < d_pr2 < rr[0],
       "FR4: the zoo is ORDERED PD_2 < Artin < GD in range (rank2 < density < rank1)")
    print(f"    {'weight w(p)':>24} {'kind':>16} {'conj limit':>11} {'in-range':>9}")
    for name, kind, lim, val in zoo:
        vs = f"{val:.4f}" if isinstance(val, float) else "--"
        print(f"    {name:>24} {kind:>16} {lim:>11.4f} {vs:>9}")
    print(f"    => w |-> rho_c(w) realizes any prime log-average; EVERY value reachable")
    print(f"       trivially (w = c*log p -> rho_c = c), so the content is which STRUCTURED")
    print(f"       weights hit NAMED constants: rank (PD spectrum, Sum=1) + density (delta).")
    print(f"    LATERAL ESCAPE EXECUTED: not one third constant but the realizer principle")
    print(f"       + a conserved infinite family + a different-kind (Artin) constant.")
    print()


def main():
    print("=" * 72)
    print("THE RESERVE ZOO  -  the constant-realizer")
    print("=" * 72)
    ps, Prank, logm, logp, pr2, p1mod4, Pplus = build()
    print(f"trajectory: primorial schedule k=1..{K_MAX}, p_max={ps[-1]}\n")
    section_FR1(ps, logp, Pplus)
    rr = section_FR2(ps, Prank, logm, logp)
    d_pr2, d_p14 = section_FR3(ps, logp, pr2, p1mod4)
    section_FR4(rr, d_pr2, d_p14)
    print("=" * 72)
    print(f"CHECKS: {PASS} passed, {FAIL} failed")
    print("=" * 72)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
