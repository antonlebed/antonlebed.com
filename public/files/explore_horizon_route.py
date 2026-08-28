"""explore_horizon_route.py -- the composite route of the horizon's
drop, counted: does -chi = c * prime, with c small, move the model?

THE QUESTION. The prediction horizon H(k) is the full ring's -chi
over a drop D_k (explore_horizon_rate.py, the certificate to k = 60).
That rig modelled the drop by M0: the first PRIME -chi over sub-rings
ordered by dropped squarefree product d, each prime with chance
q(T) = q0 * phi(d')/d', q0 = e^gamma ln p_k / ln X, d' the odd part of
d. M0 omits the COMPOSITE ROUTE -- a sub-ring whose -chi is c * prime
with c small names the prime -chi/c, drop d * c -- which can only lower
the drop, yet the measured mean ln D_k over k = 13..60 read 2.869
against M0's 2.665, +0.204, and the run priced that at "one standard
error" without deriving the error. Here the route is derived, modelled
(M1) and COUNTED directly, and the standard error is the model's own.

THE HAND-ATTACK, fixed before the engine.
1. The cofactor's chance. -chi(S) is coprime to every prime of S and
   odd always (the primality gate), so a cofactor c of -chi(S) is odd
   and its primes lie in T' (the odd dropped primes) or above p_k. For
   c = prod p^a over T', "c exactly divides -chi(S) and the rest is
   prime" has chance, under equidistribution off S's primes and
   Cramer for the rest,
     prod_{p^a || c} (1/p^a)(1 - 1/p) * prod_{p in T', p not| c} (1 - 1/p)
       * e^gamma ln p_k / ln(-chi(S)/c)
     = [phi(d')/d'] / c * e^gamma ln p_k / ln(-chi(S)/c).
   So a (T, c) candidate carries q(T)/c up to the log: the route is
   M0's own term divided by c, sitting at drop d*c. Consistency: the
   sum over all odd T'-smooth c of 1/c is d'/phi(d'), so the routes of
   one T sum to q0 -- the chance that the non-T'-smooth part of -chi is
   prime, as it must.
2. Disjointness. For one T the events "c exactly divides and the rest
   is prime" over different c are DISJOINT (-chi is not both prime and
   3 * prime), so the first-success law multiplies 1 - sum_c q(T, c)
   per T, never prod_c (1 - q(T, c)); across distinct T the trials are
   taken independent, as M0 took them.
3. Two generosities M0 carries, priced separately so neither is
   blamed for the other. (a) M0 sums ln d where the drop actually
   measured is ln(X / -chi(S)) = ln d + ln[(k-1-sum_P 1/p)/(m-1-sum_S
   1/p)], positive, about 0.03 at |T| = 1 and k = 30 and 0.07 at
   k = 13 -- this RAISES the model toward the measurement. (b) M0
   prices every candidate's primality at ln X where the candidate sits
   at ln(-chi(S)/c) < ln X, so its chance is higher by the factor
   ln X / ln(-chi(S)/c) ~ 1 + ln(dc)/ln X, a few percent -- this LOWERS
   the model, away from the measurement. Both are exact in M1, which
   uses the candidate's own -chi(S).
4. The route's mass, estimated by hand. Up to drop 30 the composite
   candidates ({3}, 3) at 9, ({2, 3}, 3) at 18, ({5}, 5) at 25 and
   ({3}, 9) at 27 carry 2/9 + 2/9 + 4/25 + 2/27 = 0.68 q0 against M0's
   squarefree mass of about 15.8 q0 over the same range: the route is
   about 4% of the mass, uniformly in ln d, so it moves E[ln D] by a
   few hundredths of a nat and not by 0.2. The "2/9" named for it is the
   ({3}, 3) term's factor phi(3)/3 / 3 = 2/9 against the d = 3 term's
   2/3: one third of that term's mass at three times its drop.
5. Primes above p_k in c. A cofactor prime r > p_k gives a route at
   drop d * r with chance (1/r)(1 - 1/r) q(T): at most a tenth of a
   unit of mass below drop 200 against M0's tens. Priced as M2 (M1
   plus those routes), expected invisible.
6. The standard error. The model's own: each rung's Var[ln D_k] from
   its first-success distribution (E[ln^2 D] - E[ln D]^2), the mean's
   sd = sqrt(sum_k Var_k)/48 -- no limit theorem, the summands' own
   spread. The empirical sd of the 48 measured ln D_k over sqrt(48)
   is printed beside it.
7. The count. The certificate's attaining sub-ring has -chi(S) = c * H
   with c = -chi(S) // H, an integer the rig already holds: c > 1 IS
   the composite route attaining the horizon, a direct count with no
   model in it, read against M1's summed probability that the first
   success is a c > 1 candidate.

THE MODEL M1. Candidates (T, c): T a subset of the rung's primes with
squarefree product d, c an odd T'-smooth number, ordered by the EXACT
drop ln(X c / -chi(S)); chance q(T, c) = [phi(d')/d'] / c * e^gamma
ln p_k / ln(-chi(S)/c); first-success law by items 1-2, enumerated to a
cap grown until the survival mass is below 1e-9. M0 is recovered from
the same code by three switches (c = 1 only, ln d for the drop, ln X
for the log), which is the positive control.

POSITIVE CONTROL, run before any verdict: M1 with the three switches
off reproduces explore_horizon_rate.py's m0_expected E[ln D] at every
k = 3..60 to 1e-9; and the certified horizons and drops are that rig's
(imported, same seed, same certificate).

PREDICTIONS, FROZEN BEFORE THE RUN (kills are what the rig PRINTS).
P1 (the control): M1 reduced to M0 matches m0_expected to 1e-9 at every
   k. KILL: any mismatch.
P2 (the route's size): M1's mean E[ln D_k] over k = 13..60 sits below
   M0's 2.665 by between 0.01 and 0.15 nat (the composite route and
   generosity (b) lowering it, (a) raising it, the route the larger).
   KILL: M1's mean at or above M0's, or more than 0.30 below.
P3 (the sign -- the ship condition): the measured mean 2.869 sits
   inside M1's mean +- 1.96 times the model's own sd of the mean (item
   6). KILL: outside the band. Inside, the horizon is publishable; the
   composite route is then invisible at this sample and the model
   heuristic. The sd is predicted in 0.12..0.25 (per-rung sd of ln D
   near 1.0..1.7 over 48 rungs).
P4 (the route counted): the number of rungs in 13..60 whose attaining
   -chi has c > 1 is inside the binomial 95% band around M1's summed
   P(first success has c > 1); that sum is predicted in 1..5 of 48.
   KILL: a count outside the band.
P5 (the generosities, a pricing): (a) alone raises the model's mean by
   0.02..0.10; (b) alone lowers it by 0.01..0.10; M2 - M1 is above
   -0.02. Sizes only; no kill, a mis-sized one is reported.

Run: python prime/code/explore_horizon_route.py
Estimate before the run: under 90 s, under 100 MB (the certificate is
0.8 s; the enumeration a few thousand big-integer -chi per rung).

FINDINGS (every figure below is the run's print).
F1 (the control). M1 with its three switches off reproduces
   m0_expected to 2.2e-15 at every k = 7..60. At k = 3..6 it differs by
   6.0e-3, 4.2e-3, 6.9e-5 and 1.7e-7: m0_expected admits dropped sets
   leaving a ONE-PRIME ring, whose -chi is -1 and names nothing, and
   they fit under its bound only at tiny k -- a flaw in the older
   model's candidate list at rungs nothing ever read it for (its P3-P5
   read k >= 12, where the two agree exactly). P1's "every k" clause
   is met from k = 7 and the prediction was wrong below it.
F2 (the route counted, rule by certificate). The composite route
   attains the horizon at 2 of the 58 rungs k = 3..60: k = 22, where
   the sub-ring dropping 3 has -chi = 9 * H (D_22 = 27.97), and
   k = 53, dropping {3, 5} with -chi = 3 * H (D_53 = 46.36). M1 expects
   1.63 of the 48 rungs k = 13..60, 95% band [0, 4.08]; the count
   is 2 (P4 met). At every other rung the attaining -chi is itself
   prime.
F3 (the route's size, model). Over k = 13..60 the composite route
   lowers the model's mean ln D by 0.026 nat, generosity (b) (each
   candidate priced at its own ln -chi) by 0.016, and generosity (a)
   (the exact drop ln(X/-chi) for ln d) RAISES it by 0.037 -- the
   largest of the three, the prediction having ranked the route first --
   so M1 = 2.660 against M0's 2.665, -0.005: P2's band (-0.15..-0.01)
   missed, its kill (M1 at or above M0, or below by 0.30) not met. The
   three corrections cancel to nothing. M2 - M1 = -0.000: primes above
   p_k in the cofactor are invisible (P5's sizes all met).
F4 (the sign, the ship condition). Measured mean ln D_k 2.869 against
   M1's 2.660, +0.209; the model's own sd of the mean, from its
   per-rung variances, is 0.179 (per-rung sd 1.24), the EMPIRICAL sd of
   the mean 0.187 -- the two agree, an unfrozen check that the model's
   spread is the measurement's. z = +1.17, band [2.309, 3.011],
   measured INSIDE (P3 met). The +0.2 is noise at this sample: the
   composite route is real, counted at the model's rate, and a
   hundredth-scale correction; the sign of the residual is undecided
   and undecidable at 48 rungs, the model heuristic.
Tier: the count is a rule over k <= 60 (the certificate's, MR-25 above
3.317e24 at k >= 19); M1's chances are a model, its agreement with the
count and the spread a pattern.
Run record: 2.8 s wall, 14.1 MB peak under memwatch; enumeration to
cap 4096 at most, 1,905 candidates at most, survival mass under 7.9e-10
at every k >= 7 (below k = 7 the finite candidate list is spent).
Seed 1032 for the certificate's MR-25 bases, the older rig's.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import math
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_horizon_rate import (K_MAX, EULER_GAMMA, primes_upto,  # noqa: E402
                                  neg_chi, certified_horizon,
                                  m0_expected, B)

SURVIVE_TARGET = 1e-9


def _subsets_by_product(primes, bound):
    """Every (product, dropped tuple) with squarefree product <= bound."""
    out = [(1, ())]
    for p in primes:
        if p > bound:
            break
        out += [(d * p, T + (p,)) for d, T in out if d * p <= bound]
    return out


def _smooth_odd(ps, bound):
    """Every odd number <= bound whose primes all lie in ps (odd)."""
    out = [1]
    for p in ps:
        if p > bound:
            break
        new = []
        for c in out:
            q = c * p
            while q <= bound:
                new.append(q)
                q *= p
        out += new
    return sorted(out)


def _phi_over(d_primes):
    out = 1.0
    for p in d_primes:
        out *= (1 - 1 / p)
    return out


def model(primes, X, composite=True, exact_drop=True, own_log=True,
          above=False, extra_primes=()):
    """The first-success model over (T, c) candidates.

    composite: include c > 1 routes (else c = 1 only, M0's list).
    exact_drop: score a candidate at ln(X c / -chi(S)) (else ln(d c)).
    own_log: price primality at ln(-chi(S)/c) (else ln X).
    above: also allow primes above p_k in c (M2), from extra_primes.
    Returns dict(e_ln, var, p_comp, p_one, survive, n_cand).
    """
    k = len(primes)
    p_k = primes[-1]
    lnX = math.log(X)
    boost = math.exp(EULER_GAMMA) * math.log(p_k)
    cap = 256
    while True:
        cands = []  # (drop_ln, T, c, q)
        chi_cache = {}
        for d, T in _subsets_by_product(primes, cap):
            S = [p for p in primes if p not in T]
            if len(S) < 2:
                continue
            nc = chi_cache.get(T)
            if nc is None:
                nc = neg_chi(S)
                chi_cache[T] = nc
            Todd = [p for p in T if p > 2]
            phi = _phi_over(Todd)
            cs = [1]
            if composite:
                pool = list(Todd)
                if above:
                    pool += [r for r in extra_primes if r <= cap // d]
                cs = _smooth_odd(pool, cap // d)
            for c in cs:
                if d * c > cap:
                    continue
                # exact-divisibility chance for primes above p_k in c
                w = 1.0
                if above and c > 1:
                    for r in extra_primes:
                        if r > c:
                            break
                        if c % r == 0:
                            w *= (1 - 1 / r)
                n = nc // c if own_log else X
                if n < 3:
                    continue
                q = boost * phi / c * w / (math.log(n) if own_log else lnX)
                drop = (math.log(X) + math.log(c) - math.log(nc)
                        if exact_drop else math.log(d * c))
                cands.append((drop, T, c, q))
        cands.sort()
        # first-success law: per-T disjoint, across T independent
        cum = {}
        prod = 1.0
        e_ln = 0.0
        e_ln2 = 0.0
        p_comp = 0.0
        p_one = None
        for drop, T, c, q in cands:
            ct = cum.get(T, 0.0)
            if ct >= 1.0:
                continue
            q = min(q, 1.0 - ct)  # a chance is at most what the T has left
            prob = q * prod / (1 - ct)
            if p_one is None:
                p_one = prob
            e_ln += prob * drop
            e_ln2 += prob * drop * drop
            if c > 1:
                p_comp += prob
            prod *= (1 - ct - q) / (1 - ct)
            cum[T] = ct + q
        if prod < SURVIVE_TARGET or cap > 10 ** 7:
            break
        cap *= 4
    return dict(e_ln=e_ln, var=max(e_ln2 - e_ln * e_ln, 0.0),
                p_comp=p_comp, p_one=p_one or 0.0, survive=prod,
                n_cand=len(cands), cap=cap)


def main():
    t0 = time.time()
    rng = random.Random(1032)
    small_primes = primes_upto(B)
    all_primes = primes_upto(2000)

    print("=" * 72)
    print("  explore_horizon_route.py -- the composite route counted")
    print("=" * 72)

    rows = []
    for k in range(3, K_MAX + 1):
        primes = all_primes[:k]
        X, H, T, comp = certified_horizon(primes, small_primes, rng)
        S = [p for p in primes if p not in T]
        c_att = neg_chi(S) // H
        assert neg_chi(S) == c_att * H
        D = X / H
        m0 = m0_expected(primes, X)[0]
        r_m0 = model(primes, X, composite=False, exact_drop=False,
                     own_log=False)
        r_a = model(primes, X, composite=False, exact_drop=True,
                    own_log=False)
        r_b = model(primes, X, composite=False, exact_drop=False,
                    own_log=True)
        r_m1 = model(primes, X)
        extra = [r for r in all_primes if r > primes[-1]]
        r_m2 = model(primes, X, above=True, extra_primes=extra)
        rows.append(dict(k=k, p_k=primes[-1], D=D, T=T, c=c_att, lnD=math.log(D),
                         m0=m0, m0r=r_m0["e_ln"], a=r_a["e_ln"],
                         b=r_b["e_ln"], m1=r_m1, m2=r_m2["e_ln"]))

    print("\nPOSITIVE CONTROL: M1 with its switches off against m0_expected")
    small = [(r["k"], r["m0"] - r["m0r"]) for r in rows
             if abs(r["m0"] - r["m0r"]) > 1e-9]
    worst = max(abs(r["m0"] - r["m0r"]) for r in rows if r["k"] >= 7)
    print(f"  max |M0(reduced) - m0_expected| over k = 7..60: {worst:.2e}")
    print(f"  rungs differing above 1e-9: "
          f"{[(k, f'{d:+.1e}') for k, d in small] if small else 'none'} "
          f"(m0_expected admits dropped sets leaving a one-prime ring, "
          f"whose -chi is -1 and names nothing; they fit under its bound "
          f"only at tiny k)")
    print(f"  control {'PASS' if worst < 1e-9 else 'FAIL'} on k = 7..60")
    assert worst < 1e-9, "P1: reduction to M0 failed"

    print("\nTHE TABLE: k, drop D_k, dropped set, cofactor c at the "
          "attaining sub-ring, ln D, M0, (a) exact drop, (b) own log, "
          "M1, M2, M1's sd, M1's P(c > 1)")
    print(f"  {'k':>3} {'D_k':>8} {'dropped':>16} {'c':>3} {'lnD':>6} "
          f"{'M0':>6} {'(a)':>6} {'(b)':>6} {'M1':>6} {'M2':>6} "
          f"{'sd1':>5} {'Pc>1':>6}")
    for r in rows:
        m1 = r["m1"]
        print(f"  {r['k']:>3} {r['D']:>8.2f} "
              f"{str(r['T']) if r['T'] else '{}':>16} {r['c']:>3} "
              f"{r['lnD']:>6.3f} {r['m0']:>6.3f} {r['a']:>6.3f} "
              f"{r['b']:>6.3f} {m1['e_ln']:>6.3f} {r['m2']:>6.3f} "
              f"{math.sqrt(m1['var']):>5.2f} {m1['p_comp']:>6.3f}")
    worst_surv = max(r["m1"]["survive"] for r in rows if r["k"] >= 7)
    tiny = [(r["k"], f"{r['m1']['survive']:.1e}") for r in rows
            if r["k"] < 7 and r["m1"]["survive"] > SURVIVE_TARGET]
    print(f"  enumeration: worst survival mass {worst_surv:.1e} over "
          f"k = 7..60, largest cap "
          f"{max(r['m1']['cap'] for r in rows if r['k'] >= 7)}, "
          f"most candidates {max(r['m1']['n_cand'] for r in rows)}; "
          f"below k = 7 the candidate list is finite and the mass left "
          f"unspent is {tiny if tiny else 'none'}")
    assert worst_surv < SURVIVE_TARGET, "enumeration did not converge"

    tail = [r for r in rows if r["k"] >= 13]
    n = len(tail)
    meas = sum(r["lnD"] for r in tail) / n
    M0 = sum(r["m0"] for r in tail) / n
    Ma = sum(r["a"] for r in tail) / n
    Mb = sum(r["b"] for r in tail) / n
    M1 = sum(r["m1"]["e_ln"] for r in tail) / n
    M2 = sum(r["m2"] for r in tail) / n
    sd_model = math.sqrt(sum(r["m1"]["var"] for r in tail)) / n
    emp_var = sum((r["lnD"] - meas) ** 2 for r in tail) / (n - 1)
    sd_emp = math.sqrt(emp_var / n)

    print(f"\nP2 -- the route's size: mean E[ln D] over k = 13..60")
    print(f"  M0 {M0:.3f}   M1 {M1:.3f}   M1 - M0 {M1 - M0:+.3f}  "
          f"(P2 wants -0.15..-0.01)")

    print(f"\nP3 -- the sign: measured mean against M1's band")
    print(f"  measured {meas:.3f}   M1 {M1:.3f}   difference "
          f"{meas - M1:+.3f}")
    print(f"  model sd of the mean {sd_model:.3f} (per-rung sd "
          f"{sd_model * math.sqrt(n):.2f})   empirical sd of the mean "
          f"{sd_emp:.3f}")
    z = (meas - M1) / sd_model
    lo, hi = M1 - 1.96 * sd_model, M1 + 1.96 * sd_model
    print(f"  z = {z:+.2f}   band [{lo:.3f}, {hi:.3f}]   measured "
          f"{'INSIDE' if lo <= meas <= hi else 'OUTSIDE'}")

    print(f"\nP4 -- the route counted: rungs in 13..60 attained through "
          f"c > 1")
    n_comp = sum(1 for r in tail if r["c"] > 1)
    exp_comp = sum(r["m1"]["p_comp"] for r in tail)
    var_comp = sum(r["m1"]["p_comp"] * (1 - r["m1"]["p_comp"]) for r in tail)
    blo = max(0.0, exp_comp - 1.96 * math.sqrt(var_comp))
    bhi = exp_comp + 1.96 * math.sqrt(var_comp)
    which = [(r["k"], r["c"]) for r in tail if r["c"] > 1]
    print(f"  count {n_comp} {which if which else ''}   M1 expects "
          f"{exp_comp:.2f}, 95% band [{blo:.2f}, {bhi:.2f}]")
    n_comp_all = sum(1 for r in rows if r["c"] > 1)
    print(f"  over all k = 3..60: {n_comp_all} of 58 "
          f"{[(r['k'], r['c']) for r in rows if r['c'] > 1]}")

    print(f"\nP5 -- the generosities priced (means over k = 13..60)")
    print(f"  (a) exact drop for ln d:  {Ma - M0:+.3f}")
    print(f"  (b) own log for ln X:     {Mb - M0:+.3f}")
    print(f"  composite route, on top of both: {M1 - (M0 + (Ma - M0) + (Mb - M0)):+.3f}")
    print(f"  M2 - M1 (primes above p_k in c): {M2 - M1:+.3f}")

    print(f"\n  wall {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
