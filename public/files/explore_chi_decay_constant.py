"""
explore_chi_decay_constant.py -- THE -CHI DECAY'S FLATNESS CONSTANT
DERIVED (descends from explore_chi_primality.py, whose census, model
and flatness statistic this script re-derives as its control).

THE QUESTION. A sub-ring S of the first k tower primes (|S| = m >= 2,
N = prod S) has -chi(S) = N(m-1) - sum_i N/p_i, and a sub-ring names
primes only when -chi is prime. The census reads the prime fraction
frac(k) over all size>=2 sub-rings decaying 82% (k=4) -> 12.9%
(k=20) -> 1.5% (k=128), tracked by a conditioned-Cramer model, and its
flatness statistic frac(k) * theta(p_k) / sqrt(ln p_k) sits at
3.7-4.2 from k = 8 to 128 with no derivation behind the number. THIS
SCRIPT ASKS: what is the constant, and what does the flatness
statistic converge to?

THE HAND ANALYSIS (derived before the engine; the sections verify it).

 1. THE PER-PRIME FACTOR. The model weights a sub-ring by
        w(S) = survive(S) / (ln(-chi) * prod_{s in T} (1 - 1/s)),
    T = {s <= 100} union S, survive = no prime s <= 100 outside S
    divides -chi (members never divide, -chi is always odd: the two
    proved properties). Over S uniform on subsets, hold every
    coordinate but one prime p <= p_k fixed. If p is a member
    (probability 1/2) it survives and boosts by (1-1/p)^-1; if not,
    it survives with probability 1 - 1/p WHEN -chi mod p is
    equidistributed over the sub-rings missing p (the naming fraction
    1/p) and boosts by the same (1-1/p)^-1. Either way the expected
    factor is (1-1/p)^-1 * (1/2 + (1-1/p)/2) = 1 + 1/(2(p-1)). A
    prime with p_k < s <= 100 contributes (1-1/s)(1-1/s)^-1 = 1, so
    the cutoff 100 drops out; a member above 100 contributes 1/2 +
    (1-1/p)^-1/2, the same 1 + 1/(2(p-1)); and p = 2 contributes
    exactly 2. Hence, with the divisibility events taken independent
    of each other and of ln(-chi),
        frac(k) ~ G(k) * E[1/ln(-chi)],
        G(k) = 2 * prod_{3 <= p <= p_k} (1 + 1/(2(p-1))).
    Independence is a HYPOTHESIS here and is counted, not argued:
    the census reads 3 named by 51% of 3-prime sub-rings at k = 8
    against 33%, so at small k the survival off members sits below
    1 - 1/p for the smallest p.

 2. THE LOGARITHM. ln(-chi) = ln N + ln(m-1) - O(m/p_min) with
    ln N = sum_{p in S} ln p of mean theta(p_k)/2 and variance
    sum (ln p)^2 / 4, relative spread ~ sqrt(ln p_k / p_k), so
    E[1/ln(-chi)] = (2/theta(p_k)) * (1 + o(1)), the ln(m-1) term
    worth 1-2% at k <= 128 and the Jensen term less.

 3. MERTENS. prod_{3 <= p <= x} (1 - 1/p) ~ 2 e^-gamma / ln x, and
    (1 + 1/(2(p-1))) sqrt(1 - 1/p) = 1 + 1/(8p^2) + O(p^-3), so
        prod_{3 <= p <= x} (1 + 1/(2(p-1))) ~ K sqrt(e^gamma ln x / 2),
        K = prod_{p odd} (1 + 1/(2(p-1))) sqrt(1 - 1/p),
    and the flatness statistic's limit is
        C_inf = lim frac * theta / sqrt(ln p_k) = 2 K sqrt(2 e^gamma).
    Hand: K ~ 1.034, 2 sqrt(2 e^gamma) = 3.775, C_inf ~ 3.90. The
    finite-k reading 2 G(k)/sqrt(ln p_k) runs above the limit
    (4.01 at k = 10 by hand) because Mertens' finite product does.

PREDICTIONS, FROZEN. P1: K computed over the odd primes to 10^7 lands
in 1.02-1.05 and C_inf = 2 K sqrt(2 e^gamma) in 3.7-4.2, the band the
census reads. P2: the first-moment form F(k) = G(k) * E[1/ln(-chi)]
(E exact over all sub-rings at k <= 20, sampled above) lands within
10% of the exact-conditioning model at every k >= 10, and within 3%
at k = 20, ABOVE it where the small primes' naming excess bites. P3:
the Jensen ratio E[1/ln(-chi)] * theta(p_k)/2 lands in 1.00-1.10 at
every k >= 10 and decreases with k. P4: the per-prime count at k =
20 -- over the sub-rings missing p, the fraction with p | -chi
against 1/p -- lands within 20% of 1/p for every odd p <= 71, and the
product over p of the measured factor (survival * boost, members and
non-members pooled) against 1 + 1/(2(p-1)) lands within 5% of 1.
P5: 2 G(k)/sqrt(ln p_k) lands within 5% of C_inf for every k >= 10.
KILLS, as prints: C_inf outside 3.7-4.2; F(k)/model outside 0.90-1.10
at some k >= 10; the pooled per-prime product off 1 by more than 5%;
2 G(k)/sqrt(ln p_k) off C_inf by more than 5% at some k >= 10.

THE DESIGN. Section S1: K and C_inf from the product to 10^7 with
the tail bounded by sum 1/(8p^2). S2: the exhaustive subset DP over
the first 20 primes (as the census's), recording per sub-ring -chi's
primality, the model weight w (the census's classify), 1/ln(-chi),
and -chi mod p for every odd p <= 71 -- per rung k <= 20: frac, the
model, F(k) = G(k) * E[1/ln(-chi)], the Jensen ratio. S3: the per-prime
count at k = 20 (P4). S4: the sampled rungs k = 24..128 (20,000
uniform size>=2 sub-rings each, seed 20260827): frac, model, F(k),
Jensen ratio. S5: the flatness statistic per k -- measured, model,
F(k), and 2 G(k)/sqrt(ln p_k) -- against C_inf (P5). Positive
control: S2's frac and model reproduce the census's k = 8 anchor
(110/247) and its k = 20 fraction to the printed digit.

Resource: pure Python; the DP holds two 2^20 bigint arrays (the
census's 116 MB) plus per-mask residues -- run under memwatch at the
512 MB default; wall estimated ~40 s.

FINDINGS (the run's prints; tiers as the charter names them).

 F1. THE CONSTANT (derivation within the conditioned-Cramer
     heuristic; P1 held): K = 1.03424560 (settled to eight digits by
     10^6, tail past 10^7 under 10^-9), 2 sqrt(2 e^gamma) = 3.774729,
     C_inf = 3.903997. The census's 3.7-4.2 brackets it.

 F2. THE FIRST-MOMENT FORM IS THE MODEL (rule in range; P2 held): F(k)
     = G(k) E[1/ln(-chi)] over the exact-conditioning model reads
     1.094 at k = 10, 1.027 at k = 20, 1.012 at 24, 1.024 at 32, 1.021
     at 48, 1.006 at 64, 1.002 at 96, 1.001 at 128 -- above it at
     every k, so the correlation the first-moment form drops is
     NEGATIVE and dies. It is not the marginals: at k = 20 the naming
     fraction off members is 1/p within 0.2% at every odd p <= 71 but
     59 (2.2%: 9,085 of 524,268) and the pooled per-prime factor
     multiplies to 0.9996 of prod (1 + 1/(2(p-1))) (P4 held) -- the
     item-1 suspicion that the smallest primes' naming excess bites at
     small k is a stratum fact (3-prime sub-rings at k = 8) and not a
     marginal one at k = 20. The measured fraction tracks F(k) at
     0.926-0.979 over k = 8..20 (F above the census as it is above the
     model).

 F3. THE JENSEN RATIO CROSSES 1 (observation; P3 FAILED at its lower
     edge): E[1/ln(-chi)] theta(p_k)/2 reads 1.068 at k = 10, falls
     through 1.000 at k = 19 and sits at 0.998 (k = 20), 0.992, 0.990,
     0.995, 0.996, 0.995, 0.995 to k = 128. The hand analysis named
     both terms -- convexity above, ln(m-1) below -- and froze the
     band 1.00-1.10 without the second's sign; the ratio is the
     convexity term winning at small k and the ln(m-1) term (about
     2 ln(k/2)/theta) winning past k = 19. The eight prints failing
     that band are this and nothing else.

 F4. THE FLATNESS STATISTIC IS MERTENS' FINITE PRODUCT (rule in range;
     P5 held): 2 G(k)/sqrt(ln p_k) reads 4.007 at k = 10, 3.962 at 20,
     3.941 at 32, 3.924 at 64, 3.915 at 128 against C_inf = 3.904 --
     within 2.7% from k = 10 and descending -- and the model's own
     flatness statistic reads 3.912 (k = 10), 3.847 (20), 3.883 (24),
     3.810 (32), 3.820 (48), 3.884 (64), 3.897 (96), 3.891 (128), the
     measured 3.962, 3.856, 3.889, 3.808, 3.853, 3.805, 3.730, 3.906
     (sampled +/- 0.10 relative at k >= 64). "Flat at 3.7-4.2" is
     the finite Mertens product over the first k primes read against
     sqrt(ln p_k), the two moving together from k = 10 on.

RUN RECORD. python memwatch.py explore_chi_decay_constant.py --
CHECKS: 50/58 passed (the eight P3 prints, F3), 20.0 s, peak working
set 122.5 MB. The first run divided by ln(-chi) = ln 1 = 0 at the
sub-ring {2, 3}, whose -chi = 1; that sub-ring carries weight 0 in
the census's model and contributes 0 to E[1/ln(-chi)] here.

ASSUMED, NOT RUN: Mertens' theorem in the form prod_{p <= x}(1 - 1/p)
~ e^-gamma / ln x, and the conditioned-Cramer model itself, whose
tracking of the census is the sibling script's record. Everything
else asserts.
"""

import os
import sys
from math import exp, log, sqrt
from random import Random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_chi_primality import (primes_upto, neg_chi_direct, classify,
                                   is_prime_big)

EULER_GAMMA = 0.57721566490153286


def section_1():
    """K over the odd primes to 10^7, its tail, C_inf."""
    print("S1. THE CONSTANT: K = prod_{p odd} (1 + 1/(2(p-1))) sqrt(1 - 1/p)")
    print("-" * 72)
    P = 10 ** 7
    ps = primes_upto(P)
    logK = 0.0
    partial = {}
    marks = (10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7)
    for p in ps:
        if p == 2:
            continue
        logK += log(1.0 + 0.5 / (p - 1)) + 0.5 * log(1.0 - 1.0 / p)
        for m in marks:
            if p <= m:
                partial[m] = logK
    K = exp(logK)
    tail = 1.0 / (8.0 * P * log(P))     # sum_{p > P} 1/(8 p^2) ~ 1/(8 P ln P)
    for m in marks:
        print(f"  K to {m:>10,}: {exp(partial[m]):.8f}")
    print(f"  tail past 10^7 < {tail:.2e} (relative)")
    A2 = 2.0 * sqrt(2.0 * exp(EULER_GAMMA))
    C_inf = A2 * K
    print(f"  2 sqrt(2 e^gamma) = {A2:.6f}")
    print(f"  C_inf = 2 K sqrt(2 e^gamma) = {C_inf:.6f}")
    check(1.02 <= K <= 1.05, f"P1: K = {K:.4f} in 1.02-1.05")
    check(3.7 <= C_inf <= 4.2, f"P1: C_inf = {C_inf:.3f} in 3.7-4.2")
    print()
    return K, C_inf


def G_of(pk_list):
    """2 prod_{3 <= p <= p_k} (1 + 1/(2(p-1)))."""
    g = 2.0
    for p in pk_list:
        if p > 2:
            g *= 1.0 + 0.5 / (p - 1)
    return g


CHECKS = []


def check(cond, label):
    CHECKS.append((bool(cond), label))
    print(f"  [{'ok' if cond else 'FAIL'}] {label}")


def section_2_3(PR, K_EXH=20):
    """Exhaustive DP over the first K_EXH primes; per-rung F(k), model,
    frac, Jensen ratio; the per-prime count at k = K_EXH."""
    print(f"S2. EXHAUSTIVE k <= {K_EXH}: frac, model, F(k) = G(k) E[1/ln -chi]")
    print("-" * 72)
    pk = PR[:K_EXH]
    odd_ps = [p for p in pk if p > 2]
    size = 1 << K_EXH
    N = [1] * size
    S_ = [0] * size
    tot = [0] * K_EXH        # per max-bit
    pri = [0] * K_EXH
    wsum = [0.0] * K_EXH     # model weight
    lsum = [0.0] * K_EXH     # 1/ln(-chi)
    # per-prime count at k = K_EXH: over ALL size>=2 sub-rings
    # miss[p] = sub-rings missing p; div[p] = those with p | -chi;
    # boost[p] pooled: sum over sub-rings of (survive_p * (1-1/p)^-1)
    miss = {p: 0 for p in odd_ps}
    div = {p: 0 for p in odd_ps}
    n_all = 0
    for mask in range(1, size):
        low = mask & -mask
        i = low.bit_length() - 1
        rest = mask ^ low
        Nr = N[rest]
        N[mask] = Nm = Nr * pk[i]
        S_[mask] = Sm = S_[rest] * pk[i] + Nr
        m = mask.bit_count()
        if m < 2:
            continue
        nc = Nm * (m - 1) - Sm
        isp, w = classify(nc, ())
        mb = mask.bit_length() - 1
        tot[mb] += 1
        pri[mb] += isp
        wsum[mb] += w
        lsum[mb] += 1.0 / log(nc) if nc >= 3 else 0.0   # {2,3}: -chi = 1
        n_all += 1
        for j, p in enumerate(odd_ps):
            if not (mask >> (j + 1)) & 1:
                miss[p] += 1
                if nc % p == 0:
                    div[p] += 1
    del N, S_
    print(f"  {'k':>3} {'p_k':>4} {'frac':>7} {'model':>7} {'F(k)':>7} "
          f"{'F/model':>8} {'frac/F':>7} {'Jensen':>7}")
    rows = []
    ct = cp = 0
    cw = cl = 0.0
    counts = {}
    for k in range(2, K_EXH + 1):
        ct += tot[k - 1]
        cp += pri[k - 1]
        cw += wsum[k - 1]
        cl += lsum[k - 1]
        counts[k] = (cp, ct)
        if k < 4:
            continue
        fr = cp / ct
        fe = cw / ct
        El = cl / ct
        th = sum(log(p) for p in pk[:k])
        F = G_of(pk[:k]) * El
        jen = El * th / 2.0
        rows.append((k, fr, fe, F, jen))
        print(f"  {k:>3} {pk[k-1]:>4} {100*fr:>6.2f}% {100*fe:>6.2f}% "
              f"{100*F:>6.2f}% {F/fe:>8.3f} {fr/F:>7.3f} {jen:>7.3f}")
    check(counts[8] == (110, 247), f"control: k=8 anchor {counts[8]}")
    check(abs(100 * counts[20][0] / counts[20][1] - 12.9) < 0.05,
          f"control: k=20 frac {100*counts[20][0]/counts[20][1]:.2f}%")
    for k, fr, fe, F, jen in rows:
        if k >= 10:
            check(0.90 <= F / fe <= 1.10, f"P2: k={k} F/model = {F/fe:.3f}")
            check(1.00 <= jen <= 1.10, f"P3: k={k} Jensen = {jen:.3f}")
    k20 = [r for r in rows if r[0] == 20][0]
    check(abs(k20[3] / k20[2] - 1) <= 0.03,
          f"P2: k=20 F/model = {k20[3]/k20[2]:.3f} within 3%")
    print()

    print(f"S3. THE PER-PRIME COUNT AT k = {K_EXH}: p | -chi off members, "
          f"and the pooled factor")
    print("-" * 72)
    print(f"  {'p':>3} {'missing':>9} {'p|-chi':>8} {'frac':>8} {'1/p':>8} "
          f"{'ratio':>6} {'factor':>8} {'pred':>8}")
    prod_ratio = 1.0
    worst = 0.0
    for p in odd_ps:
        fr_div = div[p] / miss[p]
        r = fr_div * p
        # pooled factor: members (n_all - miss) always survive; non-members
        # survive (miss - div) times; every survivor boosts (1-1/p)^-1
        factor = ((n_all - miss[p]) + (miss[p] - div[p])) / n_all
        factor /= (1.0 - 1.0 / p)
        pred = 1.0 + 0.5 / (p - 1)
        prod_ratio *= factor / pred
        worst = max(worst, abs(r - 1))
        print(f"  {p:>3} {miss[p]:>9,} {div[p]:>8,} {fr_div:>8.5f} "
              f"{1/p:>8.5f} {r:>6.3f} {factor:>8.5f} {pred:>8.5f}")
    print(f"  product over p of measured factor / predicted: {prod_ratio:.4f}")
    check(worst <= 0.20, f"P4: worst naming-fraction ratio off 1 by {worst:.3f}")
    check(abs(prod_ratio - 1) <= 0.05,
          f"P4: pooled product {prod_ratio:.4f} within 5% of 1")
    print()
    return rows


def section_4(PR, rows):
    """Sampled rungs k = 24..128."""
    print("S4. SAMPLED k = 24..128 (20,000 uniform size>=2 sub-rings, "
          "seed 20260827)")
    print("-" * 72)
    rng = Random(20260827)
    print(f"  {'k':>4} {'p_k':>4} {'frac':>7} {'+/-':>5} {'model':>7} "
          f"{'F(k)':>7} {'F/model':>8} {'Jensen':>7}")
    for k in (24, 32, 48, 64, 96, 128):
        M = 20000
        ps_k = PR[:k]
        got = 0
        wsum = lsum = 0.0
        done = 0
        while done < M:
            mask = rng.getrandbits(k)
            if mask.bit_count() < 2:
                continue
            ps = [ps_k[i] for i in range(k) if mask >> i & 1]
            nc = neg_chi_direct(ps)
            isp, w = classify(nc, [p for p in ps if p > 100])
            got += isp
            wsum += w
            lsum += 1.0 / log(nc) if nc >= 3 else 0.0
            done += 1
        fr = got / M
        fe = wsum / M
        El = lsum / M
        th = sum(log(p) for p in ps_k)
        F = G_of(ps_k) * El
        jen = El * th / 2.0
        se = sqrt(fr * (1 - fr) / M)
        rows.append((k, fr, fe, F, jen))
        print(f"  {k:>4} {ps_k[-1]:>4} {100*fr:>6.2f}% {100*se:>4.2f} "
              f"{100*fe:>6.2f}% {100*F:>6.2f}% {F/fe:>8.3f} {jen:>7.3f}")
        check(0.90 <= F / fe <= 1.10, f"P2: k={k} F/model = {F/fe:.3f}")
        check(1.00 <= jen <= 1.10, f"P3: k={k} Jensen = {jen:.3f}")
    print()


def section_5(PR, rows, C_inf):
    """The flatness statistic against its limit."""
    print("S5. THE FLATNESS STATISTIC frac theta / sqrt(ln p_k) AGAINST C_inf")
    print("-" * 72)
    print(f"  {'k':>4} {'measured':>9} {'model':>8} {'F(k)':>8} "
          f"{'2G/sqrt':>8} {'C_inf':>7}")
    for k, fr, fe, F, jen in rows:
        th = sum(log(p) for p in PR[:k])
        sl = sqrt(log(PR[k - 1]))
        g2 = 2.0 * G_of(PR[:k]) / sl
        print(f"  {k:>4} {fr*th/sl:>9.3f} {fe*th/sl:>8.3f} {F*th/sl:>8.3f} "
              f"{g2:>8.3f} {C_inf:>7.3f}")
        if k >= 10:
            check(abs(g2 / C_inf - 1) <= 0.05,
                  f"P5: k={k} 2G/sqrt(ln p_k) = {g2:.3f} within 5% of C_inf")
    print()


def main():
    print("THE -CHI DECAY'S FLATNESS CONSTANT DERIVED")
    print("=" * 72)
    print()
    PR = primes_upto(10 ** 4)[:128]
    K, C_inf = section_1()
    rows = section_2_3(PR)
    section_4(PR, rows)
    section_5(PR, rows, C_inf)
    n_ok = sum(1 for ok, _ in CHECKS if ok)
    print("=" * 72)
    print(f"CHECKS: {n_ok}/{len(CHECKS)} passed")
    for ok, label in CHECKS:
        if not ok:
            print(f"  FAILED: {label}")


if __name__ == "__main__":
    main()
