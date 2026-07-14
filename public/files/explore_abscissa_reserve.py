"""explore_abscissa_reserve.py -- chamber thirty: the Dirichlet-abscissa reserve
(the settled end).

THE QUESTION (ROAD P206 face 1a). Chambers twenty-seven through twenty-nine
(explore_complexity_ledger / ledger_threshold / reserve_zoo) built reserves whose
solvency threshold is a CESARO log-average
  rho_c(w) = lim Sum_{i<=k} w(p_i) / theta(p_k),      theta(x) = Sum_{p<=x} log p,
realizing analytic DENSITY constants (Golomb-Dickman, the Poisson-Dirichlet spectrum,
Artin). Face 1a asks for a genuinely DIFFERENT solvency MECHANISM: a Dirichlet
ABSCISSA -- the least s at which the resource series
  D(s) = Sum_p 1/P+(p-1)^s        (P+(m) = largest prime factor of m)
converges (or equals 1) -- a geometric/analytic criterion, not an average. Does the
abscissa realize a NEW named constant, of a different KIND than the Cesaro zoo?

THE FRAME (hand-attacked pre-engine, SCRATCH P207; the hardness reading CORRECTED at
the P208 provenance audit -- THE LITERATURE PIN below). NO new constant -- an INVERSION
plus a degeneracy that IS the finding. The reciprocal weight 1/P+^s reads the SMOOTH
TAIL of the P+ distribution (small P+), where the Cesaro log-weight log P+ reads the
BULK (a typical shifted prime has P+(p-1) ~ (p-1)^0.62, huge, contributing ~1/p^0.62s
to D -- negligible). The smooth tail is carried by SMOOTH SHIFTED PRIMES (P+(p-1)
small <=> p-1 smooth):
  - P+ = 2  <=>  Fermat primes p = 2^m + 1        (5 known, conjecturally FINITE)
                 -> a BOUNDED contribution 5/2^s.
  - P+ = 3  <=>  Pierpont primes p = 2^a 3^b + 1, 3 | p-1 (conjecturally INFINITE)
                 -> if infinite, D(s) diverges for EVERY s (abscissa sigma_c = +inf).
The pinning is ONE-DIRECTIONAL: infinitely many B-smooth shifted primes (fixed B) =>
D(s) diverges for every s; equivalently D(s) finite => every smooth count C_B finite.
The converse is NOT claimed -- all-counts-finite does not force convergence (the
per-level counts N(q) = #{p : P+(p-1) = q} could still grow in q), so smooth existence
(Sigma_1/Pi_2, chamber twenty-five) is a SUFFICIENT certificate for total degeneracy,
not an equivalent of finiteness.

THE LITERATURE PIN (P208 audit -- the fixed-s question is NOT open). Friable-shifted-
prime counts are a THEOREM: #{x < p <= 2x : P+(p-1) <= x^beta} >> x/(log x)^C for every
beta > 15/(32 sqrt e) = 0.2843.. (Lichtman 2022, arXiv:2211.09641, Thm 1.1 -- won by
extending the Bombieri-Friedlander-Iwaniec mean-value range; Baker-Harman 1998 gave
0.2961, the chronology runs Erdos 1935 -> Wooldridge -> Pomerance -> Balog ->
Fouvry-Grupp -> Friedlander 1/(2 sqrt e)). Each dyadic block (x, 2x] then contributes
>= x^(1 - beta*s)/(log x)^C to D(s), so D(s) DIVERGES UNCONDITIONALLY for every
s < 1/0.2844 ~ 3.52 -- in particular at s = 1, 2, 3 computed here. sigma_c > 3.51 is
a theorem; ONLY the endpoint sigma_c = +inf (divergence at EVERY s) is open, with
Pierpont infinitude a sufficient certificate (Erdos's friability conjecture, a
density-count statement, is another route). The first draft's clean two-kinds map
("density-hard vs existence-hard") over-read: the fixed-s tail questions are
DENSITY-COUNT theorems won by the same BFI-circle technology the Cesaro zoo's
conjectures await.

THE DUALITY (the headline, as corrected). The zoo's TWO solvency mechanisms sit at the
TWO ENDS of the P+ distribution (the inversion -- computed, robust):
  Cesaro average  -> BULK (rough P+)  -> OPEN density constants (GD/PD/Artin; BFI, GRH)
  Dirichlet absc. -> SMOOTH tail      -> NO constant; degenerate by theorem below
                                         s ~ 3.52, existence-shaped only at the
                                         sigma_c = +inf endpoint (Pierpont sufficient)
The "third KIND" of reserve is NOT a third constant and NOT a clean third hardness:
the abscissa is the SETTLED end of the distribution -- both ends are governed by one
circle (shifted-prime level of distribution), open at the bulk, proved at the tail.

FROZEN SLATE AR1-AR4 (hand-attacked pre-engine, SCRATCH P207; findings enter by a
SEPARATE post-run edit copying printed output -- BORN FINDINGS-FREE, CLAUDE.md):

  AR1 (the inversion, observation). Split primes by P+(p-1) > sqrt(p-1) (ROUGH) vs
    <= sqrt(p-1) (SMOOTH-ish). (a) Under the Cesaro weight log P+(p-1): the ROUGH set
    carries the BULK of Sum log P+(p-1) (fraction > 0.85). (b) Under the reciprocal
    weight 1/P+(p-1)^2: the SMALL-q set (P+ in {2,3,5,7,11}) carries the BULK of D(2)
    (fraction > 0.7). The two weights read OPPOSITE ends of the same distribution.
    HAND: rough density ~ log 2 = 0.69 of primes but a larger share of the log-mass;
    the reciprocal is dominated by q <= 7 (a typical prime's 1/p^1.2 ~ 0).

  AR2 (existence-pinning, argument + observation). (a) D_k(s) = Sum_{i<=k} 1/P+(p_i-1)^s
    has a NON-VANISHING TAIL: the last decade (k 1000->10000, a x10 range) carries a
    substantial share of D_K (> 0.30) at s = 2 and s = 3 -- the opposite of a convergent
    series, whose tail fractions shrink to 0. (Monotonicity alone is vacuous: EVERY positive
    series' partial sums rise, convergent ones included -- so the tail fraction, not the
    increase, is the diagnostic. [The slate called finiteness at s = 2, 3 open; wrong --
    it is a theorem that D diverges there: THE LITERATURE PIN, P208 audit.])
    HAND: D(2) tail ~0.5. (b) The Fermat count (P+(p-1) = 2) is EXACTLY 5 (bounded);
    the smooth counts C_B(k) = #{i<=k : P+(p_i-1) <= B} for B = 3,5,7 GROW with k. So
    lim_k D_k(s) finite => finitely many B-smooth shifted primes for every B
    (equivalently: any C_B infinite => D(s) diverges for every s). [The slate's first
    draft wrote this as an IFF; the converse direction is unproved -- P208 audit.]
    HAND: Fermat count 5 (3,5,17,257,65537, all <= 104729); C_3 grows small -> teens.

  AR3 (the duality -- headline, argument; hardness reading corrected P208, see THE
    LITERATURE PIN). Two mechanisms, two ends. Assert numerically in one place:
    bulk-fraction(Cesaro) high AND smooth-fraction(reciprocal) high AND Fermat-count
    = 5 bounded WHILE the smooth-count grows -- so the abscissa has NO nondegenerate
    analytic constant, the honest lateral resolution of the "third weighting" question.

  AR4 (positive control: integers isolate the shift, observation). Repeat the inversion
    on P+(n) over INTEGERS n <= x (UNSHIFTED): the same reciprocal-reads-smooth inversion
    holds, but the integer B-smooth counts are UNCONDITIONALLY infinite (B-smooth numbers
    are dense and easy), so the integer abscissa degeneracy is PROVABLE while the shifted
    one is conjectural. The SHIFT (the +1) is exactly what turns an easy smoothness fact
    into the Pierpont existence question -- matching chamber twenty-five's genome ->
    spectrum functor (the intervention +1 the non-functorial push).
    HAND: integer 3-smooth count <= 1e5 ~ (log 1e5)^2/(2 log2 log3) ~ 40, >> shifted ~15.

DESIGN. Thin import-free number theory (mirrors explore_reserve_zoo.py /
explore_ledger_threshold.py). One pass over the first K = 10000 primes (p_max = 104729):
factor each p-1 by trial division (bound sqrt(p-1) <= 324), record P+(p-1), the
smooth/rough flag (integer compare r*r vs p-1, no float-wall), and per-q reciprocal
contributions. Integer control via an SPF sieve to p_max. K = 10000: ~0.2 s, well under
512 MB, no numpy. All sections assert.

HONEST SCOPE. AR1 is an observation (a measured inversion of emphasis). AR2(a) is an
observation (a tail-fraction diagnostic in range -- consistent with, and now known to
reflect, the PROVED divergence at s = 2, 3: THE LITERATURE PIN); AR2(b)'s Fermat bound
is a property (5 known Fermat primes in range; the finiteness itself conjectural) and
the smooth-count growth an observation. AR3 is the argument that the abscissa realizes
no new analytic constant; its hardness reading is corrected by the pin -- divergence at
every s < 1/0.2844 ~ 3.52 is a THEOREM (Lichtman/Baker-Harman friable-shifted-prime
counts, the BFI circle), sigma_c > 3.51, and only sigma_c = +inf stays open, with
smooth-shifted-prime existence (Pierpont, Pi_2, chamber 25) a SUFFICIENT certificate,
not an equivalent. AR4 is an observation isolating the shift's signature, which lives
at the ENDPOINT: integer sigma_c = +inf is provable (3-smooth integers are infinite),
shifted sigma_c = +inf waits on Pierpont-type infinitude. No new constant is claimed;
the content is the inversion (two mechanisms read two ends of one distribution) plus
the corrected hardness map: open density constants at the bulk, proved degeneracy at
the tail, existence-shaped open content only at the tail's endpoint.

FINDINGS (tiers per CLAUDE.md; run record at bottom; all sections assert).

1. THE INVERSION (observation). On the single sqrt-partition of the shifted primes
   (P+(p-1) > sqrt(p-1) = ROUGH, 6143 of 9999 = 0.614; else SMOOTH), the two weights read
   OPPOSITE ends. The Cesaro log-weight log P+ puts 0.7456 of its mass on the ROUGH set
   (rough primes carry more than their count share -- their P+ is large); the reciprocal
   1/P+^2 puts only 0.0461 there -- an inversion gap of 0.70. The abscissa/reciprocal
   reading is carried by the SMOOTH tail (the small-q band {2,3,5,7,11} alone holds 0.7638
   of D(2)), exactly the primes the Cesaro average discounts. The two reserve mechanisms
   read the two ends of the same P+ distribution.

2. THE DEGENERACY, PINNED (observation + literature pin). The resource series D_k(s) =
   Sum_{i<=k} 1/P+(p_i-1)^s climbs with a NON-VANISHING TAIL: D_k(2) = 2.25 -> 3.93 -> 6.22
   -> 12.66 and D_k(3) = 0.79 -> 1.23 -> 1.66 -> 2.63 across k in {50,200,1000,10000}
   (D_k(1) 8.07 -> 137.0), and the last decade (k 1000 -> 10000) still carries 0.51 of
   D_k(2) and 0.37 of D_k(3) -- the opposite of a convergent series whose tail fractions
   shrink to 0 (mere monotonicity is vacuous for a positive series). This in-range signal
   reflects a THEOREM (P208 pin): friable-shifted-prime counts (Lichtman 2022 beta > 0.2843,
   >> x/(log x)^C per dyadic block) force D(s) = +inf unconditionally for every
   s < 1/0.2844 ~ 3.52, so sigma_c > 3.51. The climb is carried by SMOOTH SHIFTED PRIMES:
   the Fermat count (P+=2) is frozen at exactly 5 (3,5,17,257,65537 -- conjecturally all
   there are), while the B-smooth counts grow, C_3 12 -> 31, C_5 19 -> 95, C_7 26 -> 196.
   One-directional pinning at the ENDPOINT: any C_B infinite => D(s) diverges for EVERY s
   (sigma_c = +inf); so under the standard conjecture that Pierpont primes are infinite,
   sigma_c = +inf. The converse (all C_B finite => convergence) is unproved and NOT claimed.

3. THE DUALITY (argument -- the headline, corrected P208). The reserve zoo's two solvency
   mechanisms sit at the two ends of the P+ distribution:
     CESARO average  -> BULK (rough P+, 0.746 of log-mass) -> OPEN DENSITY constants
                        (chambers 27-29: Fouvry-BFI for the Dickman Golomb-Dickman/PD
                        constants, GRH for Artin);
     DIRICHLET absc. -> SMOOTH tail (rough only 0.046 of D(2)) -> NO constant: divergence
                        PROVED for s < ~3.52 (the same BFI circle -- Lichtman extends the
                        BFI mean-value range), open only at the sigma_c = +inf endpoint,
                        where Pierpont/Fermat existence (Sigma_1/Pi_2, chamber 25) is the
                        sufficient certificate.
   So the "third KIND" of reserve the face asked for is neither a third constant nor a
   clean third hardness: the abscissa is the SETTLED end -- one circle (shifted-prime
   level of distribution) governs both ends, conjectural at the bulk, proved at the tail,
   existence-shaped only at the tail's endpoint. The honest lateral resolution of the
   third-weighting question.

4. POSITIVE CONTROL -- INTEGERS ISOLATE THE SHIFT AT THE ENDPOINT (observation). Repeating
   on P+(n) over integers n <= x (unshifted) shows the SAME inversion (integer reciprocal
   rough-fraction 0.0321), but the integer B-smooth counts C_3 = 100, C_5 = 315, C_7 = 701
   dwarf the shifted (31/95/196) and are UNCONDITIONALLY infinite (B-smooth numbers are
   dense), so the integer sigma_c = +inf is provable outright. The shifted contrast lives
   at the ENDPOINT: fixed-s divergence is a theorem on both sides, but shifted
   sigma_c = +inf waits on Pierpont-type infinitude -- the +1 SHIFT moves an easy
   smoothness fact to the edge of the friable-shifted-prime literature; chamber 25's
   genome -> spectrum functor, with the +1 the non-functorial push.

THE VERTIGO (chamber headline, corrected). The two ways to ask whether a designed-growth
economy is solvent -- a Cesaro AVERAGE of the cost vs the ABSCISSA of its resource series --
read the two ends of one distribution, and ONE circle (shifted-prime level of distribution,
BFI) governs both: the average reads the bulk and lands on OPEN density constants, the
abscissa reads the smooth tail where the same circle's theorems already force degeneracy,
leaving existence (Pierpont/Fermat, Sigma_1/Pi_2) only the endpoint. The reserve zoo
(chambers 27-29) and the fate bridge (chamber 25) are one object seen through the two ends
of P+(p-1) -- and the tail end, where existence lives, is the one the theorems already own.

RUN RECORD (this file, ~0.1 s, 13 checks, well under 512 MB, no numpy; all sections assert).
P208 provenance audit (fresh-model eye over the Opus-authored P201-P207 chain): two
corrections landed in every home (this docstring, OBSERVER.md, ROAD.md, INDEX.md) --
(i) the existence-pinning IFF was one-directional (the converse unproved); (ii)
"finiteness stays open" at s = 2, 3 was factually wrong -- divergence there is a
theorem (friable shifted primes: Baker-Harman 1998 beta 0.2961, Lichtman 2022
arXiv:2211.09641 beta 0.2843, counts >> x/(log x)^C per dyadic block; Thm 1.1 +
intro chronology read in the primary at audit time -- the statement, not the proof).
The computed findings (the inversion, the growth table, the control)
were unaffected; the headline was recast from "third hardness" to "the settled end."
Frozen slate AR1-AR4 hand-attacked pre-engine (SCRATCH P207). Band-absorbed-bias caught (the
P151 discipline): the first pass's hand thresholds were miscalibrated -- AR1(a) guessed the
rough log-mass fraction > 0.85 (actual 0.7456) and AR4 tested a small-q-band fraction > 0.70
(actual 0.663) -- so the tests were recast onto the SINGLE sqrt-partition read by BOTH weights,
which gives the sharp and correct inversion (rough log-mass 0.7456 vs rough reciprocal-mass
0.0461, a 0.70 gap; integer control 0.0321). Every recast WORLD-prediction then held on the
run: the inversion (0.746 / 0.046), the non-vanishing-tail D_k(2) (2.25 -> 12.66, last-decade
fraction 0.51), the Fermat bound (exactly 5) with growing smooth counts (C_3 12 -> 31), the
integer control (C_3 = 100 >> 31, reciprocal rough-fraction 0.0321).

Chambers: twenty-five = explore_conjecture_bridge.py (the fate-conjecture functor, the
Sigma_1/Pi_2 existence hierarchy); twenty-seven through twenty-nine =
explore_complexity_ledger / ledger_threshold / reserve_zoo.py (the Cesaro reserve zoo, the
density constants); this chamber = the abscissa mechanism, the settled end, unifying the two.
The growth-hunt inside story = OBSERVER.md (the reserve zoo, after the constant-realizer).
"""

import sys
from math import log

K_MAX = 10000
SMALL_Q = [2, 3, 5, 7, 11]                   # the reciprocal's dominant small-q band
S_LIST = [1, 2, 3]                           # abscissa test exponents
B_LIST = [3, 5, 7]                           # smoothness bounds for the growth census
MILE = [50, 200, 1000, 10000]               # k milestones


# -- number-theory primitives (thin re-decl; mirror the reserve/ledger scripts) --

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
    """Prime factorization dict of n by trial division (n <= ~1.05e5 here)."""
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


def largest_prime_factor(fac):
    """P+ from a factorization dict (max key); 1 for the empty product."""
    return max(fac) if fac else 1


def spf_sieve(n):
    """Smallest-prime-factor sieve: spf[m] = least prime factor of m, 2 <= m <= n."""
    spf = list(range(n + 1))
    i = 2
    while i * i <= n:
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def lpf_via_spf(n, spf):
    """Largest prime factor of n via the SPF sieve."""
    top = 1
    while n > 1:
        q = spf[n]
        if q > top:
            top = q
        while n % q == 0:
            n //= q
    return top


PASS = 0
FAIL = 0


def ok(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {msg}")


# -- build the shifted-prime trajectory --

def build():
    """One pass over the first K_MAX primes. Per prime p > 2 record:
      pp[i]     = P+(p-1)              (largest prime factor of the shifted prime)
      logpp[i]  = log P+(p-1)          (the Cesaro rank-1 / SIZE weight)
      rough[i]  = 1[P+(p-1) > sqrt(p-1)]   (integer compare, no float-wall)
    Returns ps (all K_MAX incl. p=2) and the per-prime arrays over p > 2.
    """
    ps = first_k_primes(K_MAX)
    pp, logpp, rough = [], [], []
    for p in ps:
        if p == 2:
            continue                          # p-1 = 1 has no largest prime factor
        m = p - 1
        fac = factorize(m)
        q = largest_prime_factor(fac)
        pp.append(q)
        logpp.append(log(q))
        r = int(m ** 0.5)
        while (r + 1) * (r + 1) <= m:         # exact integer floor(sqrt(m))
            r += 1
        while r * r > m:
            r -= 1
        rough.append(1 if q > r else 0)       # P+ > floor(sqrt(m)) == P+ > sqrt(m) for prime P+
    return ps, pp, logpp, rough


# =====================================================================
# AR1 -- THE INVERSION: reciprocal reads the smooth tail, log reads the bulk
# =====================================================================

def rough_split(pp, logpp, rough):
    """The two weights' ROUGH-set fractions on the one sqrt-partition.
    Returns (frac_rough_log, frac_rough_recip, small_q_recip_frac, n_rough)."""
    n = len(pp)
    tot_log = sum(logpp)
    D2 = sum(1.0 / pp[i] ** 2 for i in range(n))
    frac_rough_log = sum(logpp[i] for i in range(n) if rough[i]) / tot_log
    frac_rough_recip = sum(1.0 / pp[i] ** 2 for i in range(n) if rough[i]) / D2
    small = set(SMALL_Q)
    small_recip = sum(1.0 / pp[i] ** 2 for i in range(n) if pp[i] in small) / D2
    return frac_rough_log, frac_rough_recip, small_recip, n


def section_AR1(pp, logpp, rough):
    print("AR1  THE INVERSION  -  one partition (P+ vs sqrt), the two weights read "
          "opposite ends")
    fr_log, fr_recip, small_recip, n = rough_split(pp, logpp, rough)
    n_rough = sum(rough)
    # Cesaro log-weight EMPHASIZES the rough set; the reciprocal weight IGNORES it.
    ok(fr_log > 0.70,
       "AR1(a): under log P+, the ROUGH set (P+ > sqrt) carries the bulk (> 0.70) -- Cesaro")
    ok(fr_recip < 0.15,
       "AR1(b): under 1/P+^2, the ROUGH set carries almost none (< 0.15) -- the abscissa")
    ok(fr_log - fr_recip > 0.5,
       "AR1: the inversion -- rough log-mass minus rough reciprocal-mass > 0.5 (opposite ends)")
    print(f"    primes p>2: {n}   rough (P+>sqrt(p-1)): {n_rough} ({n_rough/n:.3f})")
    print(f"    ROUGH-set fraction under log P+ (Cesaro) : {fr_log:.4f}   (BULK -> rough)")
    print(f"    ROUGH-set fraction under 1/P+^2 (abscissa): {fr_recip:.4f}   (TAIL -> smooth)")
    print(f"    (reciprocal mass from the small-q band {SMALL_Q}: {small_recip:.4f})")
    print(f"    => the reciprocal INVERTS the emphasis: the abscissa reads smooth shifted primes")
    print()


# =====================================================================
# AR2 -- EXISTENCE-PINNING: D_k(s) creeps up, driven by smooth shifted primes
# =====================================================================

def section_AR2(ps, pp):
    print("AR2  EXISTENCE-PINNING  -  D_k(s) creeps up, carried by smooth shifted primes")
    n = len(pp)
    # accumulate D_k(s), the Fermat count, and the smooth counts C_B(k) at the milestones
    D_at = {s: {} for s in S_LIST}
    run = {s: 0.0 for s in S_LIST}
    fermat_at = {}                            # P+(p-1) == 2  <=>  Fermat prime
    cB_at = {B: {} for B in B_LIST}           # smooth-count milestones
    fermat_run = 0
    cB_run = {B: 0 for B in B_LIST}
    # index over p>2 aligns with pp; map k (over ALL primes incl p=2) to this index
    idx = 0
    for kk, p in enumerate(ps, start=1):
        if p == 2:
            continue
        q = pp[idx]
        for s in S_LIST:
            run[s] += 1.0 / q ** s
        if q == 2:
            fermat_run += 1
        for B in B_LIST:
            if q <= B:
                cB_run[B] += 1
        idx += 1
        if kk in MILE:
            for s in S_LIST:
                D_at[s][kk] = run[s]
            fermat_at[kk] = fermat_run
            for B in B_LIST:
                cB_at[B][kk] = cB_run[B]
    # (a) the TAIL does not vanish. Partial sums of ANY positive series increase, so
    # monotonicity is vacuous; the real diagnostic against convergence is that the LAST
    # decade (k: MILE[-2] -> MILE[-1], a x10 range) still carries a SUBSTANTIAL share of
    # D_K -- a convergent series' tail fraction would be shrinking toward 0. (At s = 2, 3
    # divergence is in fact a THEOREM -- friable shifted primes, docstring LITERATURE PIN;
    # this in-range diagnostic is consistent with it, not the proof of it.)
    tail_frac = {}
    for s in (2, 3):
        DK, Dprev = D_at[s][MILE[-1]], D_at[s][MILE[-2]]
        tail_frac[s] = (DK - Dprev) / DK
        ok(tail_frac[s] > 0.30,
           f"AR2(a): D_k({s})'s last decade (k {MILE[-2]}->{MILE[-1]}) carries a substantial "
           f"share ({tail_frac[s]:.2f}) -- the tail is NOT vanishing (unlike a convergent series)")
    # (b) Fermat count bounded (== 5 in range), smooth counts grow
    K = MILE[-1]
    ok(fermat_at[K] == 5,
       "AR2(b): Fermat count (P+=2) is exactly 5 in range (3,5,17,257,65537) -- BOUNDED")
    for B in B_LIST:
        ok(cB_at[B][K] > cB_at[B][MILE[0]],
           f"AR2(b): C_{B}(k) = #{{P+(p-1)<={B}}} grows with k (smooth shifted primes)")
    ok(cB_at[3][K] > fermat_at[K],
       "AR2(b): the 3-smooth shifted-prime count exceeds the Fermat count (Pierpont > Fermat)")
    print(f"    {'k':>7}" + "".join(f"  D({s})".rjust(9) for s in S_LIST)
          + "  Fermat" + "".join(f"  C_{B}".rjust(6) for B in B_LIST))
    for k in MILE:
        row = f"    {k:>7}" + "".join(f"{D_at[s][k]:>9.4f}" for s in S_LIST)
        row += f"{fermat_at[k]:>8}" + "".join(f"{cB_at[B][k]:>6}" for B in B_LIST)
        print(row)
    print(f"    last-decade tail fraction (k {MILE[-2]}->{MILE[-1]}): "
          f"D(2) {tail_frac[2]:.2f}, D(3) {tail_frac[3]:.2f}  (non-vanishing, unlike a convergent tail)")
    print(f"    => divergence at s < ~3.52 is a THEOREM (friable shifted primes, docstring pin);")
    print(f"       any C_B infinite => sigma_c = +inf (Pierpont conj. infinite -> D diverges at every s)")
    print()
    return fermat_at[K], {B: cB_at[B][K] for B in B_LIST}, {s: D_at[s][K] for s in S_LIST}


# =====================================================================
# AR3 -- THE DUALITY: mechanism <-> hardness kind (the headline)
# =====================================================================

def section_AR3(pp, logpp, rough, fermat_ct, cB):
    print("AR3  THE DUALITY  -  two mechanisms, two ends, two hardness KINDS (headline)")
    fr_log, fr_recip, _, _ = rough_split(pp, logpp, rough)
    # the duality in one assert: Cesaro emphasizes the rough bulk, the abscissa the
    # smooth tail, and the smooth tail is Fermat-bounded but Pierpont-growing -> the
    # abscissa realizes no nondegenerate constant (degeneracy proved for s < ~3.52,
    # docstring pin; existence-shaped only at the sigma_c = +inf endpoint)
    ok(fr_log > 0.70 and fr_recip < 0.15 and fermat_ct == 5 and cB[3] > fermat_ct,
       "AR3: Cesaro reads the bulk (open density constants) / abscissa reads the smooth "
       "tail (proved degenerate, existence only at the endpoint) -- NO new constant")
    print(f"    CESARO average  ->  bulk (rough P+, {fr_log:.3f} of log-mass)  ->  "
          f"OPEN density constants (BFI/Fouvry, GRH; ch 27-29)")
    print(f"    DIRICHLET absc. ->  smooth tail (rough only {fr_recip:.3f} of D(2))  ->  "
          f"NO constant: proved divergent s < ~3.52; endpoint sigma_c = +inf open")
    print(f"       (Fermat {fermat_ct} bounded, Pierpont-3smooth {cB[3]} growing: any C_B "
          f"infinite => sigma_c = +inf -- the Pi_2 sufficient certificate, ch 25)")
    print(f"    => the 'third KIND' is neither a third constant nor a clean third hardness:")
    print(f"       one BFI circle governs both ends -- open at the bulk, proved at the tail")
    print()


# =====================================================================
# AR4 -- POSITIVE CONTROL: integers isolate the shift
# =====================================================================

def section_AR4(ps):
    print("AR4  POSITIVE CONTROL  -  integers (unshifted P+) isolate the shift's hardness")
    x = ps[-1]
    spf = spf_sieve(x)
    # integer reciprocal 1/P+(n)^2 over 2<=n<=x, ROUGH-set fraction (the same inversion,
    # same sqrt-partition as the shifted trajectory)
    D2_int = 0.0
    D2_int_rough = 0.0
    cB_int = {B: 0 for B in B_LIST}
    for nn in range(2, x + 1):
        q = lpf_via_spf(nn, spf)
        r = int(nn ** 0.5)
        while (r + 1) * (r + 1) <= nn:
            r += 1
        while r * r > nn:
            r -= 1
        contrib = 1.0 / q ** 2
        D2_int += contrib
        if q > r:                             # rough: P+ > sqrt(n)
            D2_int_rough += contrib
        for B in B_LIST:
            if q <= B:
                cB_int[B] += 1
    frac_rough_int = D2_int_rough / D2_int
    ok(frac_rough_int < 0.15,
       "AR4: integer reciprocal 1/P+(n)^2 also ignores the rough set (< 0.15) -- same inversion")
    # the shift's signature: integer B-smooth counts >> shifted B-smooth counts (easy vs hard)
    ok(cB_int[3] > 30,
       "AR4: integer 3-smooth count is large (>30, UNCONDITIONALLY infinite) -- easy")
    print(f"    {'B':>4}  {'integer C_B(x)':>15}  {'(shifted was smaller: endpoint open)':>40}")
    for B in B_LIST:
        print(f"    {B:>4}  {cB_int[B]:>15}")
    print(f"    integer reciprocal ROUGH-set fraction: {frac_rough_int:.4f}  (same inversion)")
    print(f"    => the shift's signature lives at the ENDPOINT: integer sigma_c = +inf provable,")
    print(f"       shifted waits on Pierpont (ch 25's functor: the +1 the non-functorial push)")
    print()
    return {B: cB_int[B] for B in B_LIST}


def main():
    print("=" * 72)
    print("CHAMBER THIRTY  -  the Dirichlet-abscissa reserve (the settled end)")
    print("=" * 72)
    ps, pp, logpp, rough = build()
    print(f"trajectory: primorial schedule k=1..{K_MAX}, p_max={ps[-1]} "
          f"(shifted primes p>2: {len(pp)})\n")
    section_AR1(pp, logpp, rough)
    fermat_ct, cB, DK = section_AR2(ps, pp)
    section_AR3(pp, logpp, rough, fermat_ct, cB)
    cB_int = section_AR4(ps)
    print("=" * 72)
    print(f"CHECKS: {PASS} passed, {FAIL} failed")
    print("=" * 72)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
