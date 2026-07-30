"""Cunningham-chain miss bias — fluke or correlation?

At k=7 the Cunningham chain {41, 83, 167} was missed whole. Under the
independent random model P(miss) = (1 - 1/s)^(2^k - 1) the three
per-prime probabilities are 0.0435, 0.2145, 0.4664 and the joint miss
is 0.44%. (An earlier header here read ~1%, which is the same event
priced at the k=7 AGGREGATE miss rate 0.219 cubed rather than at each
prime's own probability; the model this script tests is the per-prime
one.) Rare either way, and this script tests whether chain membership
correlates misses, at the right scale.

THE RIGHT OBJECT. In the fixed window (p_k, 10 p_k] misses die out by
k ~ 11 (2^k subsets vs a window growing like 10 p_k), so "test at
larger k" cannot mean the same window. The scale-free quantity is the
ABSORPTION RUNG k_named(s): the smallest k at which some sub-ring of
rung k names s. By the reciprocal naming criterion (proved earlier),
s is named at rung k iff -1 mod s is a nonempty subset sum of
{p_i^{-1} - 1 mod s} over the first k primes (excluding s itself) —
computable for ALL s by an O(k*s) bitmask DP, no factorization, no
2^k enumeration.

THE TEST. Under the random model P(k_named(s) > k) = (1 - 1/s)^(2^m - 1)
(m = usable tower primes at rung k), giving a model mean E[k_named](s).
Residual r(s) = k_named(s) - E[k_named](s) standardizes out size. If
chain membership biases misses, Sophie Germain pairs (s, 2s+1) show
correlated residuals; a permutation test (partners reshuffled among
pairs) gives the p-value. A control pairing (s with the nearest prime
to 2s+1 that isn't 2s+1) checks the residualization itself.

A CONFOUND GUARDED, A NOISE BUMP DIAGNOSED. Any drift of the residual
with s would correlate size-linked pairs (t = 2s+1) spuriously, and
the permutation null would not account for it — so the pair tests use
residuals detrended against log s. The drift turned out nearly flat
(-0.03 per log s) and the result is detrend-insensitive (raw corr at
187 pairs: -0.001 vs -0.002 detrended): the +0.203 (p = 0.09) seen at
a 69-pair S_MAX = 5000 sample was small-sample noise, not drift.

FINDINGS (scope: all primes 7 < s <= 20000, k <= 30; seed=0):
1. (rule) The DP reproduces the brute-force -chi-divisibility miss
   sets exactly at k = 5, 6, 7 (full 10 p_k windows) and the known
   anchors k_named(41) = 8, k_named(83) = 9, k_named(281) = 11.
2. (observation) Absorption residuals are centered AND correctly
   scaled: mean r = +0.12, sd = 1.74 over 2258 primes vs a
   model-implied sd of 1.86 — the random model tracks the absorption
   rung, in mean and spread, far past the windows it was fit in (an earlier run).
3. (observation, the answer) NO CHAIN BIAS: over the 187 Sophie
   Germain pairs in range, corr(r(s), r(2s+1)) = -0.002, permutation
   p = 0.98 (two-sided, 10000 shuffles); control pairing (nearest
   prime to 2s+1) corr = +0.028, p = 0.70. Chain pairs are
   indistinguishable from arbitrary size-matched pairs. Second-kind
   chains (s, 2s-1) are likewise null: 186 pairs, corr +0.033,
   p = 0.67. The {41, 83, 167} joint miss was a coupon-collector
   accident, as the P+ analysis already suggested.
4. (observation) 26 chain triples (s, 2s+1, 4s+3) in range; 6 have
   all residuals positive vs ~4.8 expected by chance (the detrended
   residuals are skewed — 56.8% positive — so the baseline is
   26 * 0.568^3, not 26/8; unremarkable either way). {41, 83, 167}
   remains the most extreme (residual sum +6.9) — the fluke itself,
   not a mechanism.

Run: python prime/code/explore_cunningham_bias.py
"""
import random
from itertools import combinations
from math import prod

S_MAX = 20000
K_MAX = 30


def sieve(n):
    is_p = bytearray([1]) * (n + 1)
    is_p[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            is_p[i * i::i] = bytearray(len(is_p[i * i::i]))
    return [i for i in range(n + 1) if is_p[i]]


PRIMES = sieve(S_MAX * 2 + 10)
PRIME_SET = set(PRIMES)
TOWER = PRIMES[:K_MAX]


def section(title):
    print(f"\n{'=' * 72}\n  {title}\n{'=' * 72}")


def k_named(s):
    """Smallest rung k whose tower names s (criterion subset-sum DP)."""
    mask = (1 << s) - 1
    target = 1 << (s - 1)            # -1 mod s
    reach = 1                        # empty set: sum 0
    for k, p in enumerate(TOWER, start=1):
        if p == s:
            continue                 # sub-rings never contain s itself
        b = (pow(p, -1, s) - 1) % s
        reach |= ((reach << b) | (reach >> (s - b))) & mask if b else reach
        if reach & target:
            return k
    return None


def neg_chi(ps):
    N = prod(ps)
    return N * (len(ps) - 1) - sum(N // p for p in ps)


def model_survival(s, k):
    """P(k_named(s) > k) under the uniform-subset-sum random model."""
    m = sum(1 for p in TOWER[:k] if p != s)
    return (1 - 1 / s) ** (2 ** m - 1)


def model_mean(s):
    return sum(model_survival(s, k) for k in range(0, K_MAX))


# ----------------------------------------------------------------------
section("I. VALIDATION — DP vs brute-force -chi divisibility + anchors")

for k in (5, 6, 7):
    ps = TOWER[:k]
    horizon = 10 * ps[-1]
    window = [s for s in PRIMES if ps[-1] < s <= horizon]
    named_bf = set()
    for size in range(2, k + 1):
        for sub in combinations(ps, size):
            nc = neg_chi(list(sub))
            if nc:
                named_bf |= {s for s in window if abs(nc) % s == 0}
    missed_bf = sorted(set(window) - named_bf)
    missed_dp = sorted(s for s in window if k_named(s) > k)
    assert missed_bf == missed_dp, (k, missed_bf, missed_dp)
    print(f"  k={k}: window ({ps[-1]}, {horizon}], "
          f"missed {len(missed_dp)}/{len(window)}: {missed_dp}")

assert {41, 83, 167} <= set(s for s in PRIMES if 17 < s <= 170
                            and k_named(s) > 7)
for s, kk in ((41, 8), (83, 9), (281, 11)):     # reference anchors (previously computed)
    assert k_named(s) == kk, (s, k_named(s))
print("  anchors OK: k_named(41)=8, k_named(83)=9, k_named(281)=11; "
      "DP == brute force at k=5,6,7")

# ----------------------------------------------------------------------
section(f"II. ABSORPTION RUNG vs RANDOM MODEL — all primes 7 < s <= {S_MAX}")

residual = {}
for s in PRIMES:
    if 7 < s <= S_MAX:
        kn = k_named(s)
        assert kn is not None, s
        residual[s] = kn - model_mean(s)

rs = list(residual.values())
mean_r = sum(rs) / len(rs)
sd_r = (sum((r - mean_r) ** 2 for r in rs) / len(rs)) ** 0.5
tot_var = 0.0
for s in residual:
    surv = [model_survival(s, k) for k in range(K_MAX)]
    m1 = sum(surv)
    m2 = sum((2 * k + 1) * p for k, p in enumerate(surv))
    tot_var += m2 - m1 * m1
sd_model = (tot_var / len(residual)) ** 0.5
print(f"  {len(rs)} primes: mean residual {mean_r:+.2f}, sd {sd_r:.2f} "
      f"(model-implied sd {sd_model:.2f} — calibrated in mean AND spread)")

# de-trend r against log s: model drift would correlate size-linked
# pairs (t = 2s+1) spuriously, so the pair test must use detrended r
from math import log
raw_residual = dict(residual)
xs = [log(s) for s in residual]
ys = rs
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
b_fit = (sum((u - mx) * (v - my) for u, v in zip(xs, ys))
         / sum((u - mx) ** 2 for u in xs))
a_fit = my - b_fit * mx
residual = {s: r - (a_fit + b_fit * log(s)) for s, r in residual.items()}
print(f"  drift fit r ~ {a_fit:+.2f} {b_fit:+.2f}*log(s) removed "
      f"(pair tests use detrended residuals)")
print(f"  most-overdue absorptions: "
      f"{sorted(residual, key=residual.get, reverse=True)[:6]} "
      f"(r = {', '.join(f'{residual[s]:+.1f}' for s in sorted(residual, key=residual.get, reverse=True)[:6])})")

# ----------------------------------------------------------------------
section("III. SOPHIE GERMAIN PAIRS — residual correlation + permutation")

pairs = [(s, 2 * s + 1) for s in PRIMES
         if 7 < s and 2 * s + 1 <= S_MAX and 2 * s + 1 in PRIME_SET]
x = [residual[s] for s, _ in pairs]
y = [residual[t] for _, t in pairs]


def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    cov = sum((u - ma) * (v - mb) for u, v in zip(a, b))
    va = sum((u - ma) ** 2 for u in a) ** 0.5
    vb = sum((v - mb) ** 2 for v in b) ** 0.5
    return cov / (va * vb)


obs = pearson(x, y)
random.seed(0)
N_PERM = 10000
yy = y[:]
extreme = 0
for _ in range(N_PERM):
    random.shuffle(yy)
    if abs(pearson(x, yy)) >= abs(obs):
        extreme += 1
p_val = extreme / N_PERM
print(f"  {len(pairs)} chain pairs (s, 2s+1), s in "
      f"[{pairs[0][0]}, {pairs[-1][0]}]")
print(f"  corr(r(s), r(2s+1)) = {obs:+.3f}, permutation p = {p_val:.2f} "
      f"(two-sided, {N_PERM} shuffles)")
raw_corr = pearson([raw_residual[s] for s, _ in pairs],
                   [raw_residual[t] for _, t in pairs])
print(f"  detrend-insensitivity: raw (un-detrended) corr = {raw_corr:+.3f}")

# second-kind chains (s, 2s-1) — same test, same null
pairs2 = [(s, 2 * s - 1) for s in PRIMES
          if 7 < s and 7 < 2 * s - 1 <= S_MAX and 2 * s - 1 in PRIME_SET]
x2 = [residual[s] for s, _ in pairs2]
y2 = [residual[t] for _, t in pairs2]
obs2 = pearson(x2, y2)
yy2 = y2[:]
extreme = 0
for _ in range(N_PERM):
    random.shuffle(yy2)
    if abs(pearson(x2, yy2)) >= abs(obs2):
        extreme += 1
print(f"  second-kind chains (s, 2s-1): {len(pairs2)} pairs, "
      f"corr = {obs2:+.3f}, p = {extreme / N_PERM:.2f}")

# control: s paired with the nearest prime to 2s+1 that ISN'T 2s+1
ctrl = []
for s, t in pairs:
    c = min((q for q in PRIMES if 7 < q <= S_MAX and q != t and q != s
             and abs(q - t) <= 50),
            key=lambda q: abs(q - t))
    ctrl.append(residual[c])
obs_c = pearson(x, ctrl)
extreme = 0
cc = ctrl[:]
for _ in range(N_PERM):
    random.shuffle(cc)
    if abs(pearson(x, cc)) >= abs(obs_c):
        extreme += 1
print(f"  control pairing (nearest prime to 2s+1): corr = {obs_c:+.3f}, "
      f"p = {extreme / N_PERM:.2f}")

# ----------------------------------------------------------------------
section("IV. CHAIN TRIPLES (s, 2s+1, 4s+3) — the {41,83,167} fluke in context")

triples = [(s, 2 * s + 1, 4 * s + 3) for s in PRIMES
           if 7 < s and 4 * s + 3 <= S_MAX
           and 2 * s + 1 in PRIME_SET and 4 * s + 3 in PRIME_SET]
print(f"  {'triple':22s} {'k_named':>14s} {'residuals':>20s} {'sum':>6s}")
for t in triples:
    ks = [k_named(s) for s in t]
    rr = [residual[s] for s in t]
    print(f"  {str(t):22s} {str(ks):>14s} "
          f"{' '.join(f'{r:+.1f}' for r in rr):>20s} {sum(rr):>+6.1f}")
all_pos = [t for t in triples if all(residual[s] > 0 for s in t)]
frac_pos = sum(1 for r in residual.values() if r > 0) / len(residual)
print(f"  triples with all residuals positive: {len(all_pos)} "
      f"(expected {len(triples) * frac_pos ** 3:.1f} from the empirical "
      f"sign rate {frac_pos:.3f}): {all_pos}")


if __name__ == "__main__":
    print("\ndone.")
