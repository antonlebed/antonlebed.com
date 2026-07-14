"""
-chi primality decay: the census + conditioned heuristic (MAP 8).

A sub-ring S (a subset of the first k tower primes, |S| = m >= 2) has
CRT Euler characteristic chi = N(1 - m + sum 1/p_i), N = prod(S), so

    -chi(S) = N*(m-1) - sum_i N/p_i        (-chi = -1 for m <= 1)

The seed-flower names primes through -chi; PRIMALITY of -chi is the
gate. MAP 8: the fraction of size>=2 sub-rings with -chi prime decays
(82% at k=4 -> 45% at k=8). Why, and toward what limit?

TWO EXACT PROPERTIES (proved here, verified exhaustively k <= 12):

  P1 (member coprimality). For p in S: N == 0 and N/p_i == 0 (mod p)
     for all p_i != p, so -chi == -N/p (mod p), nonzero. -chi is
     coprime to EVERY member prime. (Naming criterion's complement:
     ALGEBRA.md handles absent primes; members never divide.)
  P2 (always odd). If 2 in S: P1. If 2 not in S: N and every N/p_i
     are odd, so -chi == (m-1) - m == 1 (mod 2). (Same parity
     arithmetic as the 2-invisibility rule: 2 is never named, present
     OR absent.)

So -chi arrives pre-sieved: coprime to 2 and to all of S by
construction. The conditioned-Cramer model (the P35 shape) is then
forced: check divisibility by primes s <= 100 EXACTLY per sub-ring
(members can't divide, by P1), and weight survivors

    P(-chi prime) ~ 1/(ln(-chi) * prod_(s in T)(1 - 1/s)),
    T = {s <= 100} U S   (the conditioning set; min'd at 1 for tiny -chi)

Sections:
  I.   Property verification k <= 12 (P1, P2, sign, the -N/p identity)
       + DP-vs-direct -chi cross-check + MR-vs-trial-division cross-check
  II.  Pinned anchors: 9/11 = 82% (k=4) ... 110/247 = 45% (k=8)
  III. Exhaustive census k = 4..20 (all 2^20 subsets, subset DP):
       per-rung fraction vs model, size strata at k = 20
  IV.  Sampled census k = 24..128 (fixed seed): fraction vs model
  V.   The decay law: frac * theta(p_k) / sqrt(ln p_k) flatness test

FINDINGS (run at K_EXH = 20, sampled to k = 128):
  1. (property) -chi is odd and coprime to every member prime
     (== -N/p mod p); verified exhaustively k <= 12, proved all k.
  2. (rule, k <= 18 deterministic MR bound; k = 19..20 MR-25) the
     prime fraction over size>=2 sub-rings decays 82% (k=4) -> 45%
     (k=8) -> 20.6% (k=14) -> 12.9% (k=20).
  3. (pattern, sampled, MR-25) the decay continues 9.98% (k=24) ->
     7.29% (k=32) -> 4.34% (k=48) -> 3.34% (k=64) -> 2.12% (k=96) ->
     1.54% (k=128); no floor.
  4. (heuristic) the conditioned-Cramer model tracks the measured
     fraction at ratio 0.97-1.07 at every rung k >= 8, exhaustive and
     sampled alike. The limit is ZERO at rate ~ sqrt(ln p_k)/theta(p_k):
     ln(-chi) ~ theta(p_k)/2 for typical sub-rings (the 1/ln null),
     and the P1/P2 conditioning boost E[prod_(s in T)(1-1/s)^-1] grows
     ~ sqrt(ln p_k) (Mertens over the ~k/2 member primes). Flatness
     test: frac * theta(p_k) / sqrt(ln p_k) holds at 3.7-4.2 across
     k = 10..128 while the unboosted frac * theta(p_k) climbs
     steadily (7.3 -> 10.6); the residual drift is lower-order terms.
  5. (observation) the SUPPLY explodes while the fraction dies: prime
     -chi sub-rings number 110 at k=8, 135,556 at k=20, and the
     population still multiplies ~1.9x per rung (2 * frac ratio).
     The size strata at k=20 are nearly FLAT (12-13% from size 8 to
     18): bigger sub-rings have bigger -chi (thinner 1/ln) but fewer
     small primes left to divide it (P1) -- the two effects nearly
     cancel, and the model reproduces the flatness. The decay is no
     starvation of the seed-flower: it is plain 1/ln thinning of
     ever-bigger integers, with the tower's only structural help
     (P1/P2 pre-sieving) already accounted for.

Tier: properties proved; census is rule to k = 18 (deterministic MR
base set below the 3.317e24 bound), MR-25 census at k = 19..20 and all
sampled rungs (error < 4^-25 per test, no known MR-25 pseudoprime);
sampled fractions are pattern; the limit statement is heuristic.

Resource: pure Python (no numpy), peak commit 116 MB at K_EXH = 20
(two 2^20 bigint DP arrays, memwatch-verified), wall ~15 s. K_EXH and
the sample plan are constants in main().
"""

from math import gcd, log, sqrt
from random import Random


# ---------------------------------------------------------------- primes

def primes_upto(n):
    isp = bytearray([1]) * (n + 1)
    isp[0] = isp[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if isp[i]:
            isp[i * i:: i] = bytearray(len(isp[i * i:: i]))
    return [i for i in range(n + 1) if isp[i]]


SMALL = primes_upto(100)                  # the exact-divisibility set
SMALL_SET = set(SMALL)
TRIAL = primes_upto(1000)                 # speed-only prefilter (big k)
COND100 = 1.0
for _s in SMALL:
    COND100 *= 1.0 - 1.0 / _s

# Sorenson & Webster: first 13 prime bases are a deterministic MR test
# below this bound.
MR_DET_BOUND = 3_317_044_064_679_887_385_961_981
BASES13 = primes_upto(41)                 # 13 bases
BASES25 = primes_upto(97)                 # 25 bases


def mr_strong(n, bases):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in bases:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime_big(n):
    """n odd, > 100, already coprime to all primes <= 100."""
    bases = BASES13 if n < MR_DET_BOUND else BASES25
    return mr_strong(n, bases)


def is_prime_trial(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def neg_chi_direct(ps):
    N = 1
    for p in ps:
        N *= p
    return N * (len(ps) - 1) - sum(N // p for p in ps)


# ------------------------------------------------------- classification

def classify(nc, member_big):
    """(is_prime, model_weight) for one -chi value.

    member_big = primes in S above 100 (their (1-1/s) joins the
    conditioning product; coprimality to them is P1, free).
    """
    if nc < 3:
        return False, 0.0
    for s in SMALL:
        if nc % s == 0:
            return nc == s, 1.0 if nc == s else 0.0
    cond = COND100
    for s in member_big:
        cond *= 1.0 - 1.0 / s
    w = min(1.0, 1.0 / (log(nc) * cond))
    for s in TRIAL:
        if s <= 100:
            continue
        if nc % s == 0:
            return nc == s, w     # composite found early; weight stands
    return is_prime_big(nc), w


def main():
    K_EXH = 20
    SAMPLED = [(24, 20000), (32, 20000), (48, 20000), (64, 20000),
               (96, 12000), (128, 8000)]
    K_MAX = max(k for k, _ in SAMPLED)
    PR = primes_upto(10 ** 4)[:K_MAX]     # first 128 primes (p_128 = 719)

    print(f"-CHI PRIMALITY DECAY: exhaustive k <= {K_EXH}, "
          f"sampled to k = {K_MAX}")
    print("=" * 72)
    print()

    # --- I. properties + cross-checks (k <= 12 exhaustive) ---
    print("I. PROPERTIES (proved in header; verified exhaustively k <= 12)")
    print("-" * 72)
    pk12 = PR[:12]
    n_checked = 0
    for mask in range(1, 1 << 12):
        ps = [pk12[i] for i in range(12) if mask >> i & 1]
        if len(ps) < 2:
            continue
        nc = neg_chi_direct(ps)
        assert nc > 0, f"sign: -chi({ps}) = {nc}"
        assert nc % 2 == 1, f"parity: -chi({ps}) even"
        N = 1
        for p in ps:
            N *= p
        for p in ps:
            assert gcd(nc, p) == 1, f"member {p} divides -chi({ps})"
            assert nc % p == (-(N // p)) % p, f"-N/p identity fails {ps}"
        n_checked += 1
    print(f"  P1 (member-coprime, == -N/p mod p), P2 (odd), sign > 0: "
          f"all {n_checked:,} size>=2 sub-rings of k=12 pass")

    # MR vs trial division on every -chi < 10^7 in the k=12 family
    n_x = 0
    for mask in range(1, 1 << 12):
        ps = [pk12[i] for i in range(12) if mask >> i & 1]
        if len(ps) < 2:
            continue
        nc = neg_chi_direct(ps)
        if nc < 10 ** 7:
            got, _ = classify(nc, ())
            assert got == is_prime_trial(nc), f"MR vs trial at {nc}"
            n_x += 1
    print(f"  MR pipeline == trial division on all {n_x:,} "
          f"values of -chi < 10^7 in the k=12 family")
    print()

    # --- exhaustive subset DP over the first K_EXH primes ---
    # N[mask] = prod, S_[mask] = sum N/p_i; -chi = N*(m-1) - S_
    pk = PR[:K_EXH]
    size = 1 << K_EXH
    N = [1] * size
    S_ = [0] * size
    # per-maxbit accumulators -> cumulative per-rung census
    tot_mb = [0] * K_EXH
    pri_mb = [0] * K_EXH
    exp_mb = [0.0] * K_EXH
    # size strata at k = K_EXH
    tot_sz = [0] * (K_EXH + 1)
    pri_sz = [0] * (K_EXH + 1)
    exp_sz = [0.0] * (K_EXH + 1)

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
        if mask % 99991 == 0:      # DP-vs-direct spot check, ~10 masks
            ps = [pk[j] for j in range(K_EXH) if mask >> j & 1]
            assert nc == neg_chi_direct(ps), f"DP mismatch at {mask:x}"
        isp, w = classify(nc, ())
        mb = mask.bit_length() - 1
        tot_mb[mb] += 1
        exp_mb[mb] += w
        tot_sz[m] += 1
        exp_sz[m] += w
        if isp:
            pri_mb[mb] += 1
            pri_sz[m] += 1
    del N, S_
    rng = Random(20260610)

    # --- II. anchors ---
    print("II. PINNED ANCHORS (ROAD MAP 8, recomputed P35)")
    print("-" * 72)
    cum_t = cum_p = 0
    fracs = {}
    counts = {}
    for k in range(2, K_EXH + 1):
        cum_t += tot_mb[k - 1]
        cum_p += pri_mb[k - 1]
        fracs[k] = cum_p / cum_t if cum_t else 0.0
        counts[k] = (cum_p, cum_t)
    assert counts[4] == (9, 11), f"k=4 anchor: {counts[4]}"
    assert counts[8] == (110, 247), f"k=8 anchor: {counts[8]}"
    for k, pct in [(5, 62), (6, 56), (7, 51)]:
        assert round(100 * fracs[k]) == pct, f"k={k}: {100*fracs[k]:.1f}%"
    print(f"  k=4: {counts[4][0]}/{counts[4][1]} = {100*fracs[4]:.0f}%   "
          f"k=8: {counts[8][0]}/{counts[8][1]} = {100*fracs[8]:.0f}%   "
          f"(intermediate {100*fracs[5]:.0f}%, {100*fracs[6]:.0f}%, "
          f"{100*fracs[7]:.0f}%)")
    print()

    # --- III. exhaustive census ---
    print(f"III. EXHAUSTIVE CENSUS k = 4..{K_EXH} "
          f"(deterministic MR bound covers k <= 18; MR-25 above)")
    print("-" * 72)
    print(f"  {'k':>3} {'p_k':>4} {'sub-rings':>10} {'prime':>8} "
          f"{'frac':>6} {'model':>6} {'ratio':>6}")
    rows = []          # (k, frac, model_frac) for section V
    cum_t = cum_p = 0
    cum_e = 0.0
    for k in range(2, K_EXH + 1):
        cum_t += tot_mb[k - 1]
        cum_p += pri_mb[k - 1]
        cum_e += exp_mb[k - 1]
        if k < 4:
            continue
        fr = cum_p / cum_t
        fe = cum_e / cum_t
        rows.append((k, fr, fe))
        print(f"  {k:>3} {pk[k-1]:>4} {cum_t:>10,} {cum_p:>8,} "
              f"{100*fr:>5.1f}% {100*fe:>5.1f}% {fr/fe:>6.3f}")
    print()
    print(f"  size strata at k = {K_EXH} (bigger sub-ring => bigger -chi "
          f"=> rarer prime):")
    print(f"  {'size':>5} {'sub-rings':>10} {'prime':>8} {'frac':>6} "
          f"{'model':>6} {'ratio':>6}")
    for m in range(2, K_EXH + 1):
        if tot_sz[m] == 0:
            continue
        fr = pri_sz[m] / tot_sz[m]
        fe = exp_sz[m] / tot_sz[m]
        r = f"{fr/fe:>6.3f}" if fe else "     -"
        print(f"  {m:>5} {tot_sz[m]:>10,} {pri_sz[m]:>8,} "
              f"{100*fr:>5.1f}% {100*fe:>5.1f}% {r}")
    print()

    # --- IV. sampled census ---
    print("IV. SAMPLED CENSUS (uniform size>=2 sub-rings, seed 20260610)")
    print("-" * 72)
    print(f"  {'k':>4} {'p_k':>4} {'samples':>8} {'prime':>7} "
          f"{'frac':>7} {'+/-':>5} {'model':>7} {'ratio':>6}")
    for k, M in SAMPLED:
        ps_k = PR[:k]
        got = 0
        exp = 0.0
        done = 0
        while done < M:
            mask = rng.getrandbits(k)
            if mask.bit_count() < 2:
                continue
            ps = [ps_k[i] for i in range(k) if mask >> i & 1]
            nc = neg_chi_direct(ps)
            isp, w = classify(nc, [p for p in ps if p > 100])
            got += isp
            exp += w
            done += 1
        fr = got / M
        fe = exp / M
        se = sqrt(fr * (1 - fr) / M)
        rows.append((k, fr, fe))
        print(f"  {k:>4} {ps_k[-1]:>4} {M:>8,} {got:>7,} "
              f"{100*fr:>6.2f}% {100*se:>4.2f} {100*fe:>6.2f}% "
              f"{fr/fe:>6.3f}")
    print()

    # --- V. the decay law ---
    print("V. DECAY LAW: zero, at rate ~ sqrt(ln p_k) / theta(p_k)")
    print("-" * 72)
    print("  ln(-chi) ~ theta(p_k)/2 for typical sub-rings (the 1/ln")
    print("  null) and the P1/P2 conditioning boost grows ~ sqrt(ln p_k)")
    print("  (Mertens over the ~k/2 member primes). Flatness test:")
    print()
    print(f"  {'k':>4} {'frac':>7} {'frac*theta':>10} "
          f"{'frac*theta/sqrt(ln p)':>21}")
    for k, fr, fe in rows:
        th = sum(log(p) for p in PR[:k])
        print(f"  {k:>4} {100*fr:>6.2f}% {fr*th:>10.3f} "
              f"{fr*th/sqrt(log(PR[k-1])):>21.3f}")
    print()

    print("=" * 72)
    print("FINDINGS")
    k20 = rows[K_EXH - 4]
    last = rows[-1]
    print(f"  1. (property) -chi is odd and coprime to every member prime"
          f" (== -N/p mod p); proved all k, verified exhaustively k<=12")
    print(f"  2. (rule k<=18 / MR-25 census k<=20) prime fraction decays "
          f"82% (k=4) -> 45% (k=8) -> {100*k20[1]:.1f}% (k=20)")
    print(f"  3. (pattern, sampled) decay continues to "
          f"{100*last[1]:.2f}% at k={last[0]}; no floor")
    print(f"  4. (heuristic) conditioned-Cramer model tracks at ratio "
          f"{min(r[1]/r[2] for r in rows if r[0] >= 8):.2f}-"
          f"{max(r[1]/r[2] for r in rows if r[0] >= 8):.2f} for k >= 8; "
          f"limit ZERO at rate ~ sqrt(ln p_k)/theta(p_k)")
    print(f"  5. (observation) supply explodes while the gate closes: "
          f"{counts[8][0]} prime -chi sub-rings at k=8, "
          f"{counts[K_EXH][0]:,} at k=20 -- the population multiplies "
          f"~{counts[K_EXH][0] / counts[K_EXH - 1][0]:.1f}x per rung")


if __name__ == "__main__":
    main()
