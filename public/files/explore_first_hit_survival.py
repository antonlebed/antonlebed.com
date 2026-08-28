"""DOES THE DISPERSION, READ AT THE FIRST HIT'S OWN SCALE, DERIVE THE
SIZE OF THE EARLY FIRST HIT? -- the first hit as the survival function
of the count, and a two-moment law carrying the index of dispersion at
every scale to a predicted first-hit mean.

THE QUESTION. explore_paired_division.py left one residual standing on
the real quadratic side: fed the field's own stratum's measured
principal share as density, the first-hit model runs LATE by 13% at wide
class number h = 2 and 20% at h = 4 (measured over predicted 0.865 and
0.802), flat in h, and every rival cause -- censoring, the cap, the
pipeline, the bin resolution -- is killed by measurement. What has the
right sign is the SPACING: the per-field count of principal split primes
is under-dispersed against its own local density, index 0.142 at h = 2
counted to the cap and 0.386 over the bottom decade. Its SIZE was never
derived: interpolating naively, an index of 0.14 would buy a ratio near
0.57, far more than the measured shortfall, and the reading over the
bottom decade no longer contradicts it but does not derive it either.
This rig derives it.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) WHOSE PHASE IS RANDOM -- NOBODY'S. Per field, the odd split
      primes p_1 < p_2 < ... carry principality bits b_i; the COUNT on
      the index line is N(n) = sum_{i<=n} b_i, the first hit is
      I = min{i : b_i = 1} and L_1 = p_I. For ANY joint law of the bits,

          E[I]   = sum_{n>=0} P(N(n) = 0),
          E[L_1] = p_1 + sum_{n>=1} P(N(n) = 0) (p_{n+1} - p_n)

      per field. The first hit IS the survival function of the count.
      No phase enters. What enters is the count's zero-probability at
      every scale n up to a few multiples of 1/q, and nothing at the cap.

  (2) THE RENEWAL RESIDUAL-LIFE LAW, PLACED. A stationary renewal
      process with inter-arrival mean m and squared coefficient of
      variation c^2 has E N(n) = n/m at every n and a first arrival
      from the origin at mean m (1 + c^2)/2 -- the law that turns 0.14
      into 0.57. An ordinary renewal process started AT an arrival has
      its first arrival at m whatever c^2 is, and E N(n) below n/m for
      n < m. The model here integrates the MEASURED share, so E N(n) =
      sum q_j is pinned to the data at every scale: the mean function is
      the stationary one by construction and the phase is not a free
      choice. What is wrong with 0.14 -> 0.57 is not the phase but the
      MODEL: a renewal process carries ONE index at every window, while
      the measured index depends on the scale it is read at -- 0.142 at
      the cap, 0.386 over the bottom decade at h = 2 -- and at n = 1 its
      EXPECTATION is 1 under any joint law: for one Bernoulli bit
      E (b - q)^2 = q (1 - q) whatever the per-field probabilities are,
      the mixture variance across fields and the within-field variance
      summing to the pooled binomial. No regularity can live in one bit,
      so the index curve rises from the cap's 0.142 to 1 within noise at
      n = 1, and the first hit lives
      at n ~ 1/q -- 2.5 at h = 2, 5 at h = 4 -- where the index is
      whatever this rig reads it to be.

  (3) THE DERIVATION. At scale n the stratum has mean mu_n = sum q_j,
      binomial variance V_n = sum q_j (1 - q_j), and index of dispersion
      c^2_n = sum_fields (N - mu)^2 / sum_fields V, the same statistic
      the paired-division rig reads at the cap, now read at every n. A
      two-moment family carries (mu, V, c^2) to a zero-probability:
      N(n) ~ Binomial(M, pi) with M pi = mu and M pi (1 - pi) = c^2 V,
      so 1 - pi = c^2 V / mu, M = mu^2 / (mu - c^2 V), P_bin = (1-pi)^M.
      It is used only as the dispersion's FACTOR on the exact
      independent survival,

          S_n = prod_{j<=n} (1 - q_j) * phi_n,
          phi_n = P_bin(c^2_n) / P_bin(1),

      so c^2 == 1 at every scale returns the paired-division model
      exactly and phi is the whole of what the dispersion adds. The
      family is exact at the REGULAR extreme as well: a period-k
      sequence at a random phase has N(n) Bernoulli(n/k) for n < k,
      which is Binomial(1, n/k) -- at k = 3 the family prints S = 2/3,
      1/3, 0 and E[I] = 2 against 3 independent, ratio 2/3 = (1+1/3)/2.
      Exact at both ends; the model dependence lives between them and
      is what the scale-by-scale print measures.

  (4) WHERE THE ALGEBRA BLOWS UP. mu - c^2 V <= 0 -- over-dispersion
      above 1/(1 - qbar) -- makes M infinite or negative: the index is
      clamped just under that line and the clamp is COUNTED. mu = 0
      (every leave-one-out cell empty) gives S = 1 in both models and
      phi = 1. c^2 -> 0 with mu < 1 sends P_bin to 0 where a regular
      process at random phase has 1 - mu: below the Bernoulli line the
      family overshoots, and the measured survival is printed beside it
      so the reader sees where. The noise: c^2_n has null standard
      deviation sqrt(2 / n_fields), 0.07 at h = 2 and 0.13 at h = 4, and
      d phi_2 / d c^2 is about 0.5 at h = 2, so the derived ratio
      carries a few per cent of sampling noise, measured by a PAIRED
      bootstrap over fields -- the density held fixed, the fields'
      bits resampled -- which gives the standard deviation of derived
      minus measured and hence a z.

  (5) THE SCALE-BY-SCALE READ. The measured survival S^meas_n -- the
      fraction of the stratum's fields with no principal prime among
      their first n split primes -- divided by the independent
      prod (1 - q_j) is the survival DEFICIT at scale n, and it is what
      phi_n claims to derive. Printed side by side at every n <= 8, the
      comparison says at which scales the dispersion accounts for the
      early hit and at which it does not, which the summed ratio alone
      cannot.

  (6) THE RESIDUAL-LIFE READING, CORRECTED FOR SCALE, is printed beside
      the derivation: (1 + c^2_{n*})/2 with n* the model's own mean
      first-hit index, rounded -- the naive formula with its index read
      where the first hit is rather than at the cap.

THE SLATE -- PREDICTIONS, FIXED BEFORE THE ENGINE.

  P1. THE DERIVATION LANDS. At h = 2 and h = 4, the two strata carrying
      the residual at better than three standard deviations, the derived
      ratio (measured mean L_1 over the survival model's predicted mean
      L_1, conditioned on the hit landing below the cap exactly as the
      paired-division rig conditions) sits inside the measured band:
      |derived - measured| / sd(derived - measured) < 2 on the paired
      bootstrap.

  P2. THE REGULARITY IS PRESENT AT THE FIRST HIT'S SCALE. At h = 2 the
      index at n = 3 sits below 1 by more than two null standard
      deviations (z < -2 with sd = sqrt(2/392) = 0.071).

  P3. THE SCALES AGREE ONE BY ONE. At h = 2, at every n from 2 to 5, the
      measured survival deficit S^meas_n / prod (1 - q_j) and phi_n
      differ by less than two bootstrap standard deviations of their
      difference.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS.

  K1 kills P1: the printed per-stratum column "z" at h = 2 or h = 4 at
     or beyond 2 in absolute value.
  K2 kills P2: the printed index-curve row n = 3 at h = 2 with z >= -2.
  K3 kills P3: the printed scale table at h = 2, any n in 2..5 with
     |deficit - phi| / sd >= 2.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. THE INDEPENDENT END IS EXACT. With c^2 forced to 1 at every scale
      the survival model's predicted mean L_1 must equal the
      paired-division rig's own local-model prediction at every stratum
      -- printed as the maximum absolute difference, which must be
      under 1e-9 -- and reproduce its printed 22.4, 45.0, 76.4, 94.0,
      160.3, 187.2, 212.4 at h = 2..8.
  C2. THE REGULAR END IS EXACT. A synthetic population of period-k
      sequences at uniformly random phase (k = 2, 3, 5; 400 fields each,
      homogeneous q = 1/k) must print a derived first-hit index ratio
      equal to (k + 1)/(2k) to within 1e-9 when the exact per-scale
      index is supplied, and within the sampling noise of the measured
      index when the index is read from the sample.
  C3. ONE BIT CARRIES NO REGULARITY. The index at n = 1 sits within two
      null standard deviations of 1 at h = 2 and h = 4.
  C4. THE IMPORT. The rig's index at the cap-wide and bottom-decade
      scales in p-space reproduces the paired-division rig's 0.142 and
      0.386 at h = 2 to three decimals.
  C5. THE PIPELINE UNDER ITS OWN NULL. Bits regenerated at the stratum's
      full share per bin -- the paired-division reference -- run through
      the whole machinery 20 times: the index curve reads 1 within noise
      at every scale, and the derived ratio's mean sits within 0.02 of
      the measured ratio's mean, both near 1. Read as the offset every
      z in K1 is compared against.

RESOURCE. Pure integer arithmetic plus per-field float accumulation, no
numpy; the field sweep is explore_paired_division.py's own, imported.
Real fundamental discriminants to 4000, odd primes to 1000, 20 reference
replicates, 200 bootstrap resamples per stratum. Well under 512MB;
wall-clock printed.

THE FINDINGS.

  F1. THE DERIVATION LANDS AT EVERY STRATUM (pattern over the seven real
      strata h = 2..8; P1 SURVIVES). Fed the index of dispersion read at
      every index scale n = 1..40, the survival model returns the
      measured mean L_1 within its own noise everywhere:

        h   n  measured indep.  ratio derived  ratio   sd     z | index ratios
        2 392    19.35  22.37  0.865   19.03  1.017 0.028 +0.60 | 0.838  0.966
        3  52    39.88  44.99  0.887   41.51  0.961 0.097 -0.40 | 0.954  1.011
        4 117    61.24  76.39  0.802   63.97  0.957 0.064 -0.66 | 0.843  0.975
        5  17    67.12  94.04  0.714   74.53  0.901 0.172 -0.58 | 0.815  0.968
        6  27   143.67 160.29  0.896  150.10  0.957 0.116 -0.37 | 0.978  1.030
        7   6   173.00 187.21  0.924  166.11  1.041 0.216 +0.19 | 0.936  1.016
        8  14   178.57 212.39  0.841  185.02  0.965 0.159 -0.22 | 0.876  0.979

      At h = 2 and h = 4, the two strata carrying the residual at z =
      -3.95 and -4.29 in the paired division, the derived ratio sits at
      1.017 +/- 0.028 and 0.957 +/- 0.064. In index units, where E[I] =
      sum S_n is exact and no prime gap weights the scales, the same
      three means read 0.966 and 0.975 against 0.838 and 0.843
      uncorrected. So the early first hit IS the spacing, in size as
      well as sign: the regularity read at the first hit's own scales
      accounts for it to within a few per cent, in both units, at every
      class number -- with F3 saying which few and why the two units
      differ.

  F2. THE INDEX HAS A SCALE, AND THE FIRST HIT LIVES WHERE IT IS NEAR 1
      (observation; P2 SURVIVES). At h = 2 the index reads 0.943, 0.717,
      0.612, 0.523, 0.459, 0.453, 0.428, 0.411 at n = 1..8 (exact null
      sd 0.057 to 0.068; z -1.0 at n = 1, -4.7 at n = 2, -6.2 at n = 3,
      -8.7 at n = 8), falling to 0.142 at the cap: 1 within noise at one
      bit, as derivation (2) says its expectation must be, and already
      0.61 at n = 3, where
      the model's own mean first hit sits. At h = 4 the curve reads 0.49
      to 0.86 over n = 1..8 with no single scale beyond 1.4 null sd --
      eight coherent scales, none individually significant -- and the
      derived ratio moves 2.4 bootstrap sd toward 1 on them. The renewal
      residual-life law with its index read at the first hit's own scale
      n* prints 0.806 at h = 2 and 0.906 at h = 4 against measured 0.865
      and 0.802: nearer than the cap-scale 0.571 and wrong in both
      directions, a renewal process having one index where this process
      has one per scale.

  F3. THE FAMILY IS EXACT AT BOTH ENDS AND TOO SLOW IN THE TAIL BETWEEN
      THEM (observation; P3 KILLED at n = 4 and 5). Scale by scale at
      h = 2, the measured survival deficit S_meas / S_indep against the
      model's S_model / S_indep: 1.042 vs 0.992 at n = 1 (z +1.4), 0.854
      vs 0.895 at n = 2 (-0.8), 0.681 vs 0.757 at n = 3 (-1.4), 0.467 vs
      0.585 at n = 4 (-2.3), 0.183 vs 0.426 at n = 5 (-4.5), 0.111 vs
      0.345, 0.060 vs 0.258, and 0.000 vs 0.192 at n = 8: every one of
      the 392 fields has a principal prime among its first eight split
      primes, where independence keeps 2.5% alive and the two-moment
      binomial 0.5%. The real regularity is STRONGER in the tail than a
      two-moment law fed the index can say -- the count's zero-
      probability dies faster than any binomial with that variance --
      and slightly weaker at n = 1, where a bin's pooled share is not
      the first split prime's share (a field whose first split prime is
      3 and one whose first is 5 draw the same bin). WHERE THE p-UNIT
      LANDING COMES FROM is printed as a decomposition, exact because
      sum_n (1[N(n) = 0] - S_n)(p_{n+1} - p_n) IS measured minus model
      per field: at h = 2 the +0.32 the measured mean sits above the
      model is +0.72 from the first scale -- that pooled-bin density
      term, present against the independent model too (+0.68) -- and
      -0.65 from scales 4 to 8 plus -0.03 beyond, the tail the law
      under-regularizes. So in p-units the landing at 1.017 is a
      cancellation of a density term and a model term of opposite sign,
      and the index-unit 0.966, which no prime gap weights, is the
      reading that shows the tail's 3.4% as what the two-moment law
      leaves. Against independence the same decomposition reads +0.68
      at the first scale and -3.70 past it (-0.17, -0.51, -0.77, -0.74,
      -0.59, -0.35, -0.25, tail -0.32), summing to the -3.02; the model
      brings the -3.70 to -0.40, so 89% of the shortfall past the first
      scale is the dispersion's by this law, and the rest is the law's
      floor. At h = 4 the model
      sits early at scales 1 to 8 (+0.31 to +0.56 each) and late in the
      tail past 8 (-4.91 of the -2.73 total), against independence's
      -15.61 there; the eight printed scales agree within 1.4 sd.

  F4. THE NULL ADDS NOTHING AT THE STRATA THAT CARRY THE FINDING. Bits
      regenerated at the stratum's full share and run through the whole
      machinery 20 times: the index curve reads 1.00 within 0.01 at
      every scale at h = 2, and the derived ratio equals the independent
      one to 0.000 there and to 0.013 at h = 4. At h = 4 the null curve
      sits at 1.08 to 1.12 over n >= 2 -- the leave-one-out share's own
      inflation -- so the measured 0.68 to 0.86 there is read against
      1.1 rather than 1. The thin strata h = 5..8 clamp the index at 16
      to 106 field-scales where a handful of fields put it above
      1/(1 - q), and say nothing individually.

RUN RECORD: wall 16.1 s, 1216 real fundamental discriminants to 4000,
odd primes to 1000, index scales 1..40, 200 bootstrap resamples per
stratum, 20 null replicates, pure integer arithmetic with per-field
floats. All controls green and read first: C1 the c^2 = 1 model equals
the paired-division prediction to 8.5e-14 at all seven strata; C2
period-2, -3 and -5 sequences at random phase return (k + 1)/(2k) to
1.1e-16 at the exact index (0.7500, 0.6653, 0.5992 at the sampled index
against measured 0.755, 0.691, 0.614); C3 the index at n = 1 reads 0.943
and 0.494 at h = 2 and 4, z -1.0 and -1.2 on the exact null sd; C4 the
p-space index reproduces 0.142 and 0.386; C5 is F4. Two controls were
corrected after their first print and before any kill was read, and both
corrections were to the CONTROL: C3 first used the chi-square null sd
sqrt(2 / n_fields), which read the h = 4 value at z = -3.9 on two hits
against 4.7 expected -- wrong for rare bits, where (b - q)^2 is a skewed
two-point variable -- and was replaced by the exact Bernoulli null of
index_curve's docstring; C2's k = 5 read 0.600011 against a 1e-9
tolerance because the control's own independent side was truncated at
60 primes (0.8^60), and reads exact at 300. The scale table's phi was
first computed at the stratum-mean (mu, V) while the prediction applies
it per field; the table now averages the per-field model survival, so
both columns are the same average. A noisy index can lift S_n above
S_{n-1}; the model keeps S a survival function by taking the running
minimum, which never fired at h = 2..4 (clamps 0).
"""

import time
from math import log, exp, sqrt
from random import Random

import explore_paired_division as pd
import explore_principal_share as ps

CAP = pd.CAP
MIN_FIELDS = pd.MIN_FIELDS
NSCALE = 40                     # index scales read: n = 1 .. NSCALE
NSHOW = 8                       # scales printed in the scale-by-scale table
BOOT = 200
REPS = 20
SEED = 2027


# --------------------------------------------------------- the survival

def field_arrays(f, cap):
    """The field's split primes at or below the cap, its bits, and its
    leave-one-out q per prime, as parallel lists."""
    ps_, bs, qs = [], [], []
    for (p, hit), q in zip(f["splits"], f["qs"]):
        if p > cap:
            break
        ps_.append(p)
        bs.append(1 if hit else 0)
        qs.append(q)
    return ps_, bs, qs


def index_curve(group, cap, nscale, c2=None):
    """Per scale n = 1..nscale: sum over fields of (N - mu)^2, sum of V,
    sum of mu, fields reaching that scale, fields with N(n) = 0, sum of
    the independent survival prod(1-q), the null variance of the
    (N - mu)^2 sum under independent bits, and -- when an index curve
    is supplied -- the sum of the per-field MODEL survival.

    The null variance is exact for a sum of independent Bernoullis:
    var (N - mu)^2 = sum_j kappa4_j + 2 V^2 with kappa4 = q(1-q)(1 -
    6q(1-q)); the chi-square sqrt(2/n_fields) is its large-n limit and
    is wrong for rare bits, where (b - q)^2 is a skewed two-point
    variable."""
    obs = [0.0] * (nscale + 1)
    var = [0.0] * (nscale + 1)
    mus = [0.0] * (nscale + 1)
    cnt = [0] * (nscale + 1)
    zero = [0] * (nscale + 1)
    ind = [0.0] * (nscale + 1)
    nullv = [0.0] * (nscale + 1)
    smod = [0.0] * (nscale + 1)
    for f in group:
        _, bs, qs = field_arrays(f, cap)
        N = mu = V = k4 = 0.0
        surv = 1.0
        prev = 1.0
        for n in range(1, min(nscale, len(bs)) + 1):
            N += bs[n - 1]
            q = qs[n - 1]
            mu += q
            V += q * (1.0 - q)
            k4 += q * (1.0 - q) * (1.0 - 6.0 * q * (1.0 - q))
            surv *= (1.0 - q)
            obs[n] += (N - mu) ** 2
            var[n] += V
            mus[n] += mu
            cnt[n] += 1
            zero[n] += (N == 0)
            ind[n] += surv
            nullv[n] += k4 + 2.0 * V * V
            if c2 is not None:
                ph, _ = phi(mu, V, c2[n])
                S = min(prev, surv * ph)
                smod[n] += S
                prev = S
    return obs, var, mus, cnt, zero, ind, nullv, smod


def phi(mu, V, c2):
    """The dispersion's factor on the independent survival: the
    binomial two-moment zero-probability at index c2 over the same at
    index 1. Returns (phi, clamped)."""
    if mu <= 0.0 or V <= 0.0:
        return 1.0, False
    clamped = False
    top = mu / V
    if c2 >= top:
        c2 = top * (1.0 - 1e-9)
        clamped = True

    def pzero(c):
        if c <= 0.0:
            return 0.0
        r = c * V / mu              # 1 - pi
        M = mu * mu / (mu - c * V)
        return exp(M * log(r))
    p1 = pzero(1.0)
    if p1 <= 0.0:
        return 1.0, clamped
    return pzero(c2) / p1, clamped


def survival_model(group, cap, c2, nscale):
    """Per field, the survival-model first-hit mean in p-units,
    conditioned on the hit landing at or below the cap: S_n = prod(1-q)
    * phi_n with the stratum's c2[n] at each scale; beyond nscale the
    factor is held at phi_nscale. Returns (mean of predicted L_1 over
    the fields with a hit, the mean mass, the count of clamps, the mean
    of the model's first-hit INDEX, the measured mean L_1 and index)."""
    pred = mass_s = 0.0
    clamps = 0
    idx_mean = 0.0
    seen = 0
    for f in group:
        if f["L1"] is None or f["L1"] > cap:
            continue
        seen += 1
        ps_, bs, qs = field_arrays(f, cap)
        num = mass = 0.0
        nidx = 0.0
        prev = 1.0                  # S_{n-1}
        surv = 1.0
        mu = V = 0.0
        ph = 1.0
        for n in range(1, len(ps_) + 1):
            q = qs[n - 1]
            mu += q
            V += q * (1.0 - q)
            surv *= (1.0 - q)
            if n <= nscale:
                ph, cl = phi(mu, V, c2[n])
                clamps += cl
            S = surv * ph
            if S > prev:            # a noisy index can lift S; keep it
                S = prev            # a survival function
            pr = prev - S
            num += pr * ps_[n - 1]
            nidx += pr * n
            mass += pr
            prev = S
        pred += num / mass if mass > 0 else float("nan")
        idx_mean += nidx / mass if mass > 0 else float("nan")
        mass_s += mass
    return (pred / seen, mass_s / seen, clamps, idx_mean / seen)


def gap_decomposition(group, cap, c2, nscale, nshow):
    """Where the p-unit difference between the measured and the model
    mean L_1 comes from, scale by scale: per field, sum over n of
    (1[N(n) = 0] - S_n) (p_{n+1} - p_n) is exactly measured L_1 minus
    the model's, so the per-scale terms locate it. Returns (per-scale
    list for n = 1..nshow, the tail beyond nshow, the total) against
    the survival model and against the independent one, per field."""
    dm = [0.0] * (nshow + 2)
    di = [0.0] * (nshow + 2)
    seen = 0
    for f in group:
        if f["L1"] is None or f["L1"] > cap:
            continue
        seen += 1
        ps_, bs, qs = field_arrays(f, cap)
        N = 0
        mu = V = 0.0
        surv = prev = 1.0
        ph = 1.0
        for n in range(1, len(ps_)):
            N += bs[n - 1]
            q = qs[n - 1]
            mu += q
            V += q * (1.0 - q)
            surv *= (1.0 - q)
            if n <= nscale:
                ph, _ = phi(mu, V, c2[n])
            S = min(prev, surv * ph)
            prev = S
            gap = ps_[n] - ps_[n - 1]
            slot = n if n <= nshow else nshow + 1
            dm[slot] += ((N == 0) - S) * gap
            di[slot] += ((N == 0) - surv) * gap
    return ([x / seen for x in dm[1:]], [x / seen for x in di[1:]])


def measured(group, cap):
    seen = [f for f in group if f["L1"] is not None and f["L1"] <= cap]
    L = sum(f["L1"] for f in seen) / len(seen)
    idx = 0.0
    for f in seen:
        for i, (p, hit) in enumerate(f["splits"]):
            if hit:
                idx += i + 1
                break
    return L, idx / len(seen), len(seen)


def c2_from_curve(obs, var, nscale):
    c2 = [1.0] * (nscale + 1)
    for n in range(1, nscale + 1):
        c2[n] = obs[n] / var[n] if var[n] > 0 else 1.0
    return c2


def evaluate_group(group, cap, nscale=NSCALE):
    """Everything for one stratum: the index curve, the derived ratio,
    the independent ratio, the scale table."""
    obs, var, mus, cnt, zero, ind, nullv, _ = index_curve(group, cap, nscale)
    c2 = c2_from_curve(obs, var, nscale)
    _, _, _, _, _, _, _, smod = index_curve(group, cap, nscale, c2)
    ones = [1.0] * (nscale + 1)
    L, I, n = measured(group, cap)
    pred_d, mass_d, clamps, nstar_d = survival_model(group, cap, c2, nscale)
    pred_1, mass_1, _, nstar_1 = survival_model(group, cap, ones, nscale)
    scales = []
    for m in range(1, nscale + 1):
        if cnt[m] == 0:
            break
        smeas = zero[m] / cnt[m]
        sind = ind[m] / cnt[m]
        sm = smod[m] / cnt[m]
        nsd = sqrt(nullv[m]) / var[m] if var[m] > 0 else float("nan")
        scales.append({"n": m, "c2": c2[m], "cnt": cnt[m], "nullsd": nsd,
                       "smeas": smeas, "sind": sind, "smod": sm,
                       "deficit": smeas / sind if sind > 0 else float("nan"),
                       "phi": sm / sind if sind > 0 else float("nan"),
                       "mu": mus[m] / cnt[m]})
    ns = max(1, min(nscale, int(round(nstar_1))))
    return {"n": n, "meas": L, "pred_d": pred_d, "pred_1": pred_1,
            "ratio_d": L / pred_d, "ratio_1": L / pred_1,
            "mass_d": mass_d, "mass_1": mass_1, "clamps": clamps,
            "nstar": nstar_1, "nstar_d": nstar_d,
            "rl": 0.5 * (1.0 + c2[ns]),
            "c2": c2, "scales": scales, "meas_idx": I}


def bootstrap(group, cap, rng, nboot, nscale=NSCALE):
    """Paired bootstrap over fields, the density fixed: fields are
    resampled with replacement and the whole evaluation -- index curve,
    survival model, measured mean -- is recomputed on each resample, so
    the sd of ratio_d is the sd of measured over derived with both
    halves moving together, and the sd of (deficit_n - phi_n) is read
    the same way at each printed scale."""
    rd, r1, diffs = [], [], [[] for _ in range(NSHOW + 1)]
    for _ in range(nboot):
        samp = [group[rng.randrange(len(group))] for _ in group]
        r = evaluate_group(samp, cap, nscale)
        rd.append(r["ratio_d"])
        r1.append(r["ratio_1"])
        for s in r["scales"][:NSHOW]:
            diffs[s["n"]].append(s["deficit"] - s["phi"])

    def sd(xs):
        if len(xs) < 2:
            return float("nan")
        m = sum(xs) / len(xs)
        return sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
    # ratio_d - ratio_1 is the paired quantity: the same measured mean
    # over two predictions; its sd is the sd of the derivation itself.
    return {"sd_d": sd(rd), "sd_1": sd(r1),
            "sd_gap": sd([a - b for a, b in zip(rd, r1)]),
            "sd_scale": [sd(d) for d in diffs]}


# ----------------------------------------------------------- the strata

def strata_of(fields):
    out = {}
    for f in fields:
        out.setdefault(f["key"], []).append(f)
    return out


def regen(fields, rng, cap):
    """The paired-division reference: bits redrawn at the stratum's
    FULL share per bin."""
    gen = {}
    for key, group in strata_of(fields).items():
        nb = pd.NBINS
        tn, th = [0] * nb, [0] * nb
        for f in group:
            for p, hit in f["splits"]:
                if p > cap:
                    break
                b = pd.bin_of(p)
                tn[b] += 1
                th[b] += hit
        gen[key] = [th[i] / tn[i] if tn[i] else 0.0 for i in range(nb)]
    synth = []
    for f in fields:
        sp, L1 = [], None
        for p, _ in f["splits"]:
            if p > cap:
                break
            hit = rng.random() < gen[f["key"]][pd.bin_of(p)]
            sp.append((p, hit))
            if hit and L1 is None:
                L1 = p
        synth.append({"D": f["D"], "h": f["h"], "splits": sp, "L1": L1,
                      "key": f["key"]})
    return synth


def regular_population(k, nfields, rng, nprimes=300):
    """C2: period-k bit sequences at a uniformly random phase over a
    common prime list, q = 1/k homogeneous, no leave-one-out."""
    plist = [q for q in ps.primes_upto(2500) if q != 2][:nprimes]
    out = []
    for i in range(nfields):
        ph = rng.randrange(k)
        sp = [(p, (j % k) == ph) for j, p in enumerate(plist)]
        L1 = next(p for p, h in sp if h)
        out.append({"D": i, "h": k, "splits": sp, "L1": L1, "key": k,
                    "qs": [1.0 / k] * len(plist)})
    return out


# ------------------------------------------------------------------ main

def main():
    t0 = time.time()
    rng = Random(SEED)
    plist = [q for q in ps.primes_upto(CAP) if q != 2]
    print("ODD PRIMES to %d: %d; index scales 1..%d; bins %s"
          % (CAP, len(plist), NSCALE, pd.BIN_EDGES))
    print("\nsweeping real fundamental discriminants to %d ..." % pd.DBOUND)
    real = pd.real_fields(plist)
    print("     %d real fields" % len(real))
    strata = strata_of(real)
    keys = [k for k in sorted(strata) if k >= 2 and
            sum(1 for f in strata[k] if f["L1"] is not None
                and f["L1"] <= CAP) >= MIN_FIELDS]
    for k in sorted(strata):
        pd.loo_shares(strata[k], CAP)

    print("\n=== CONTROLS, read first ===")

    # C1 -- the independent end against the paired-division rig itself.
    worst = 0.0
    print("[C1] c^2 == 1 survival model vs explore_paired_division's "
          "local model, per stratum:")
    for k in keys:
        group = strata[k]
        seen = [f for f in group if f["L1"] is not None and f["L1"] <= CAP]
        ref = 0.0
        for f in seen:
            num, mass = pd.first_hit(f["splits"], f["qs"], CAP)
            ref += num / mass
        ref /= len(seen)
        ones = [1.0] * (NSCALE + 1)
        mine, _, _, _ = survival_model(group, CAP, ones, NSCALE)
        worst = max(worst, abs(mine - ref))
        print("     h=%d  paired-division %8.3f   survival(c2=1) %8.3f"
              % (k, ref, mine))
    print("     max |difference| = %.2e  (must be < 1e-9)" % worst)

    # C2 -- the regular end.
    print("[C2] period-k sequences at random phase, derived first-hit "
          "INDEX ratio vs (k+1)/(2k):")
    worst2 = 0.0
    for k in (2, 3, 5):
        pop = regular_population(k, 400, rng)
        nsc = 3 * k
        # exact per-scale index for a random-phase period-k sequence:
        # N(n) = floor(n/k) + Bernoulli(frac), so var = r(1-r)/... per
        # field against V = n q(1-q).
        c2x = [1.0] * (nsc + 1)
        for n in range(1, nsc + 1):
            r = (n % k) / k
            c2x[n] = (r * (1.0 - r)) / (n * (1.0 / k) * (1.0 - 1.0 / k))
        _, I, _ = measured(pop, 10 ** 9)
        # the model's first-hit index under the exact curve
        pred_d, _, _, nstar_d = survival_model(pop, 10 ** 9, c2x, nsc)
        ones = [1.0] * (nsc + 1)
        _, _, _, nstar_1 = survival_model(pop, 10 ** 9, ones, nsc)
        exact = (k + 1) / (2.0 * k)
        got = nstar_d / nstar_1
        worst2 = max(worst2, abs(got - exact))
        r = evaluate_group(pop, 10 ** 9, nsc)
        print("     k=%d  exact-index derived %.6f  target %.6f  | sampled-"
              "index derived %.4f  measured index ratio %.4f"
              % (k, got, exact, r["nstar_d"] / r["nstar"], I / nstar_1))
    print("     max |difference| at the exact index = %.2e (must be < "
          "1e-9)" % worst2)

    # C4 -- the import: the cap-wide and bottom-decade p-space indices.
    print("[C4] p-space index at h = 2, to the cap and to 100 (paired-"
          "division printed 0.142 and 0.386):")
    for cap100 in (CAP, 100):
        obs = var = 0.0
        for f in strata[2]:
            n = mu = V = 0.0
            for (p, hit), q in zip(f["splits"], f["qs"]):
                if p > cap100:
                    break
                n += hit
                mu += q
                V += q * (1.0 - q)
            obs += (n - mu) ** 2
            var += V
        print("     to %4d: %.3f" % (cap100, obs / var))

    # ------------------------------------------------ the index curves
    print("\n=== THE INDEX CURVE, per stratum: c^2_n at n = 1..%d "
          "(exact null sd under independent bits) ===" % NSHOW)
    results = {}
    for k in keys:
        r = evaluate_group(strata[k], CAP)
        results[k] = r
        nf = len(strata[k])
        sc = r["scales"]
        row = "  ".join("%.3f" % r["c2"][n] for n in range(1, NSHOW + 1))
        sds = "  ".join("%.3f" % sc[n - 1]["nullsd"] if n <= len(sc)
                        else "  nan" for n in range(1, NSHOW + 1))
        zs = "  ".join("%+5.1f" % ((r["c2"][n] - 1.0) / sc[n - 1]["nullsd"])
                       if n <= len(sc) and sc[n - 1]["nullsd"] > 0
                       else "  nan" for n in range(1, NSHOW + 1))
        print("  h=%d (%3d fields)  c2: %s" % (k, nf, row))
        print("      %-17s   sd: %s" % ("exact null", sds))
        print("      %-17s    z: %s" % ("", zs))

    def zc(k, n):
        s = results[k]["scales"][n - 1]
        return (s["c2"] - 1.0) / s["nullsd"]
    print("[C3] index at n = 1: h=2 %.3f (z %+.2f), h=4 %.3f (z %+.2f)"
          % (results[2]["c2"][1], zc(2, 1), results[4]["c2"][1], zc(4, 1)))
    print("[K2] index at n = 3, h = 2: %.3f, z = %+.2f"
          % (results[2]["c2"][3], zc(2, 3)))

    # ------------------------------------------------ the derivation
    print("\n=== THE DERIVED FIRST HIT (bootstrap %d over fields, density "
          "fixed) ===" % BOOT)
    print("   h    n   measured  indep.   ratio    derived   ratio    "
          "gap    sd     z    n*   resid-life  clamps | index-space: "
          "meas  indep  derived  ratios")
    boots = {}
    for k in keys:
        r = results[k]
        b = bootstrap(strata[k], CAP, rng, BOOT)
        boots[k] = b
        gap = r["ratio_d"] - 1.0        # derived ratio's distance from 1
        z = gap / b["sd_d"] if b["sd_d"] > 0 else float("nan")
        print("  %2d  %3d  %8.2f  %7.2f  %6.3f   %7.2f   %6.3f  %+6.3f "
              "%6.3f  %+5.2f  %4.1f   %6.3f    %3d  | %5.2f  %5.2f  %5.2f"
              "  %.3f %.3f"
              % (k, r["n"], r["meas"], r["pred_1"], r["ratio_1"],
                 r["pred_d"], r["ratio_d"], gap, b["sd_d"], z, r["nstar"],
                 r["rl"], r["clamps"], r["meas_idx"], r["nstar"],
                 r["nstar_d"], r["meas_idx"] / r["nstar"],
                 r["meas_idx"] / r["nstar_d"]))
    print("  'ratio' = measured / predicted; the derived column's ratio "
          "reads 1 when the dispersion accounts for the whole early hit;")
    print("  the index-space columns read the same three means in units of "
          "the field's own split-prime index, where E[I] = sum S_n exactly.")
    print("  z = (derived ratio - 1) / bootstrap sd -- K1 fires at |z| >= "
          "2 at h = 2 or 4. 'resid-life' = (1 + c^2_{n*})/2, the naive")
    print("  law with its index read at the first hit's own scale n*.")

    # ------------------------------------------------ scale by scale
    print("\n=== SCALE BY SCALE at h = 2 and h = 4: the measured survival "
          "deficit against phi_n ===")
    for k in (2, 4):
        r = results[k]
        b = boots[k]
        print("  h=%d   n   fields   mu_n    c2_n    S_meas   S_model  "
              "S_indep   deficit   phi     diff    sd     z" % k)
        for s in r["scales"][:NSHOW]:
            sd = b["sd_scale"][s["n"]]
            d = s["deficit"] - s["phi"]
            print("       %2d   %4d   %6.3f  %6.3f   %6.4f   %6.4f   "
                  "%6.4f   %6.4f  %6.4f  %+6.4f  %5.4f  %+5.2f"
                  % (s["n"], s["cnt"], s["mu"], s["c2"], s["smeas"],
                     s["smod"], s["sind"], s["deficit"], s["phi"], d, sd,
                     d / sd if sd > 0 else float("nan")))
        print("  S_model = mean over fields of prod(1-q) * phi at the "
              "field's own (mu, V); deficit = S_meas/S_indep, phi = "
              "S_model/S_indep.")
    print("  K3 fires at h = 2 for any n in 2..5 with |z| >= 2.")

    print("\n=== WHERE THE p-UNIT DIFFERENCE LIVES: per field, "
          "(1[N(n)=0] - S_n)(p_{n+1} - p_n) summed per scale ===")
    print("  (the sum over scales IS measured L_1 minus the model's; "
          "'tail' is every scale past %d)" % NSHOW)
    for k in (2, 4):
        dm, di = gap_decomposition(strata[k], CAP, results[k]["c2"],
                                   NSCALE, NSHOW)
        print("  h=%d  vs survival model: %s  tail %+.3f  total %+.3f"
              % (k, " ".join("%+.3f" % x for x in dm[:NSHOW]), dm[NSHOW],
                 sum(dm)))
        print("       vs independent:    %s  tail %+.3f  total %+.3f"
              % (" ".join("%+.3f" % x for x in di[:NSHOW]), di[NSHOW],
                 sum(di)))

    # ------------------------------------------------ C5: the null
    print("\n[C5] the pipeline under its own null: bits regenerated at "
          "the full share, %d replicates" % REPS)
    acc = {k: [] for k in keys}
    curves = {k: [0.0] * (NSHOW + 1) for k in keys}
    for _ in range(REPS):
        synth = regen(real, rng, CAP)
        st = strata_of(synth)
        for k in keys:
            pd.loo_shares(st[k], CAP)
            r = evaluate_group(st[k], CAP)
            acc[k].append((r["ratio_1"], r["ratio_d"]))
            for n in range(1, NSHOW + 1):
                curves[k][n] += r["c2"][n] / REPS
    print("   h   indep.ratio   derived.ratio   |diff|    c2 curve n=1..%d"
          % NSHOW)
    for k in keys:
        a = acc[k]
        m1 = sum(x[0] for x in a) / len(a)
        md = sum(x[1] for x in a) / len(a)
        print("  %2d     %.3f          %.3f        %.3f    %s"
              % (k, m1, md, abs(m1 - md),
                 " ".join("%.2f" % curves[k][n] for n in range(1, NSHOW + 1))))

    print("\nwall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
