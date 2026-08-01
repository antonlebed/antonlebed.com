"""explore_deletion_ruler.py -- THE DELETION-AUDIT RULER
(sibling of explore_ceiling_ruler.py, which scores Bayes-error
estimators against evaluation families whose optimum is a closed
form; worlds under measurement: explore_forgetting_certificate.py).

THE QUESTION. The amnesia worlds compute the posterior of a
forgotten datum given the still-working state as an exact Fraction,
so a tool that ESTIMATES that posterior from samples is scoreable on
bias and on what its own stated uncertainty band actually covers.
Does a real deletion-audit tool estimate a functional these worlds
express -- and how does it score?

THE CUSTOMER (read in full before this script was written). SMI --
Statistical Membership Inference (Sun, Wei, Zou, Gong, Fu, Dong, Xu,
Li and Liu, "SMI: Statistical Membership Inference for Reliable
Unlearned Model Auditing", arXiv:2602.01150v2). The tool audits an
unlearned model by modelling the audited feature distribution F_u as
an exact two-component mixture

    F_u = pi * F_n + (1 - pi) * F_m,

F_m the member (still-present) feature distribution, F_n the
non-member one, and estimating the mixture coefficient pi -- the
"forgetting rate" -- as the audit verdict. Uncertainty is a
bootstrap over the audited set (200 resamples in the paper's
experiments) reported as the {5%, 95%} quantile band, which the
paper names a REFERENCE RANGE, explicitly not a confidence
interval. Two facts about the estimator, from the paper's own
Lemma 3.2 and Algorithm 1, are load-bearing here:

  (i) The point estimate matches COVARIANCE ONLY: pi minimizes
      || Sigma_u - [pi Sigma_n + (1-pi) Sigma_m
                    + pi(1-pi) d d^T] ||_F^2,   d = mu_n - mu_m,
      over pi in [0, 1]. Algorithm 1 computes means and covariances
      of the member and non-member sets but only the COVARIANCE of
      the audited set: the mean equation of the paper's own
      Proposition 3.1 (mu_u = mu_m + pi d), which identifies pi
      linearly, is not used by the estimator.
 (ii) The predicted covariance is invariant under
      pi <-> 1 - pi whenever Sigma_n = Sigma_m, so at equal
      class covariances the objective cannot distinguish a
      forgetting rate from its complement.

THE BRIDGE (why the worlds score this tool exactly). In the
constant-menu depth world the fiber over a state is, by
construction, an exact mixture of the two first-move classes with
mixing weight the first-move posterior -- so handing SMI
class-conditional fiber samples as D_m and D_n and unconditioned
fiber samples as D_u makes its target pi IDENTICAL to the world's
exact Fraction. The mixture assumption the tool must take on faith
in a neural feature space holds here exactly; what remains is the
estimator itself, which is what a ruler is for.

THE WORLD. The constant-menu depth world of the amnesia-certificate
corpus: menu {2, 3} at every state, endpoint 2^a * 3^b at age
T = a + b. Every route to the endpoint has the same weight at every
temperature (the normalizer is one polynomial; weight-side symmetry,
Lemma C of explore_forgetting_certificate.py), so the route
posterior is uniform over the C(T, a) arrangements and the
first-move posterior is EXACTLY (a/T, b/T) -- temperature-free. The
forgotten datum X is the first move; member class X = 2, non-member
class X = 3; the exact target is pi = b/T, placed at a chosen
rational by the dial (a, b) (the count leak of the amnesia corpus).

THE SAMPLER (the piece the corpus lacked -- every census there is
exhaustive). Uniform over arrangements: D_u draws n histories as
uniform shuffles of the multiset {2^a, 3^b}; D_m fixes first move 2
and shuffles the remaining (a-1, b); D_n fixes first move 3 and
shuffles (a, b-1). The audit FEATURE of a history is the count of
2-moves in a window of the w positions after the first (w = 3
here) -- a statistic that overlaps between the classes, as a neural
feature does, rather than reading X off.

THE CELLS.
  PC   positive control, harness only: F_m = N(0,1), F_n = N(3,4),
       pi = 0.3, n = 5000, one draw. The rig must recover pi to
       +-0.05 before any other cell is read.
  S    the designed identifiability cell, ring-free: F_m = N(0,1),
       F_n = N(2,1) -- equal class variances BY DESIGN, pi = 0.2.
       By (ii) the exact-moment objective has two global minima,
       pi and 1 - pi.
  W1   world cell (a,b) = (5,5):  pi = 1/2, leak zero.
  W2   world cell (a,b) = (12,3): pi = 1/5.
  W3   world cell (a,b) = (2,8):  pi = 4/5.
World-cell class variances are close but unequal (hypergeometric
window counts at neighbouring compositions), so the symmetry of (ii)
is approximate there and exact only in S.

THE MEASUREMENT. For each cell and each audit size
n in {50, 200, 1000}: R = 200 independent replicates; each replicate
draws fresh D_m, D_n, D_u of size n, computes the SMI point estimate
(the covariance-matching minimizer, solved exactly: the objective is
a quartic in pi, minimized over {0, 1} and the real critical points
in [0, 1]), then bootstraps D_u alone B = 200 times (the paper's
procedure) and takes the {5%, 95%} quantiles of the bootstrap
estimates. Printed per (cell, n): mean bias, RMSE, the FLIP RATE
(fraction of replicates with pi_hat closer to 1 - pi than to pi),
and the COVERAGE of the {5%, 95%} band (fraction of replicates whose
band contains the exact pi).

PREDICTIONS (fixed before the run).
  PR1 (PC): the harness recovers 0.30 +- 0.05.
  PR2 (S): the estimate is bimodal at {0.2, 0.8}; the flip rate does
      NOT vanish as n grows -- at exact moments both are minima, so
      noise picks between them at every sample size.
  PR3 (W1-W3): where class variances differ (W2, W3) the bias
      shrinks with n; the flip rate at small n is substantial and
      falls as n grows. W1 (pi = 1/2) has nothing to flip to.
  PR4 (coverage): printed, weighed after the run. The shape the
      sibling ruler measured -- a stated band shrinking while the
      miss does not -- would appear here as coverage of the
      {5%, 95%} band far below 90% in any flip-prone cell, because
      a bootstrap around a flipped point estimate concentrates on
      the wrong mode.

RUN. python explore_deletion_ruler.py   (measured: ~15 s,
single process, memory far under the analysis ceiling).

FINDINGS (from the printed run below; R = 200 replicates,
B = 200 bootstrap resamples per replicate).

  PC PASS: pi_hat = 0.2756 against 0.30 +- 0.05.

  PR2 CONFIRMED (cell S, equal class variances, pi = 1/5): the flip
  rate is 0.485 / 0.515 / 0.540 at n = 50 / 200 / 1000 -- it does
  not fall with n, and the mean bias sits at +0.30..0.32, i.e. half
  the replicates return ~0.8 for a truth of 0.2. At equal class
  covariances the covariance-matching objective has both pi and
  1 - pi as exact-moment minimizers, and no sample size cures a
  two-minimum objective.

  PR3 CONFIRMED (world cells, unequal class variances): bias falls
  with n (W2: +0.181 -> +0.005; W3: -0.117 -> +0.011) and the flip
  rate falls but is substantial at audit sizes the tool's own paper
  reports as converged (~200): W2 flips 28% of replicates at
  n = 200, still 10% at n = 1000.

  PR4, the ruler reading (coverage of the {5%, 95%} band against
  the exact Fraction): NEVER near 90% in the world cells --
  0.695..0.740 at W2 across all n, 0.710..0.800 at W3, 0.795..0.855
  at the leak-free W1 -- and the band WIDTH shrinks with n (W2:
  0.69 -> 0.37) while the coverage does not rise. The same shape
  the sibling ruler measured in Bayes-error protocols: a stated
  band tightening while the miss it should cover stays.

  Scope: one audit tool (SMI's low-order-moment variant), scalar
  window features, one world family, one seed stream. The
  identifiability gap (ii) is a fact about the estimator's own
  objective, reproduced ring-free in cell S.

PRINTED OUTPUT (verbatim):

  PC positive control: pi_hat = 0.2756 (target 0.30 +- 0.05) -> PASS

  == cell S  (equal-variance Gaussians)  exact pi = 1/5 = 0.2000 ==
       n  mean bias     RMSE   flip  cover90  band width
      50     0.3049   0.4304  0.485    0.890      0.8188
     200     0.3122   0.4333  0.515    0.840      0.7387
    1000     0.3245   0.4401  0.540    0.845      0.6671

  == cell W (a,b)=(5,5)  exact pi = 1/2 = 0.5000 ==
       n  mean bias     RMSE   flip  cover90  band width
      50     0.0283   0.3865  0.000    0.830      0.7248
     200     0.0063   0.3530  0.000    0.795      0.6266
    1000    -0.0163   0.2976  0.000    0.855      0.6714

  == cell W (a,b)=(12,3)  exact pi = 1/5 = 0.2000 ==
       n  mean bias     RMSE   flip  cover90  band width
      50     0.1811   0.4191  0.385    0.720      0.6943
     200     0.1046   0.3205  0.280    0.740      0.5930
    1000     0.0050   0.1931  0.100    0.695      0.3691

  == cell W (a,b)=(2,8)  exact pi = 4/5 = 0.8000 ==
       n  mean bias     RMSE   flip  cover90  band width
      50    -0.1166   0.3166  0.295    0.710      0.6205
     200    -0.0498   0.2151  0.130    0.800      0.4835
    1000     0.0109   0.1446  0.010    0.780      0.3082
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from fractions import Fraction

import numpy as np

RNG = np.random.default_rng(20260801)

R_REPLICATES = 200
B_BOOTSTRAP = 200
AUDIT_SIZES = (50, 200, 1000)
WINDOW = 3


# ---------------------------------------------------------------- SMI

def smi_point(feat_m, feat_n, feat_u):
    """The SMI point estimate (paper Lemma 3.2 / Algorithm 1), 1-D.

    Covariance matching only: minimize
        f(pi) = (A - pi*G + pi^2*B)^2
    with d = mean_n - mean_m, Bq = d^2, A = var_u - var_m,
    G = var_n - var_m + Bq, over pi in [0, 1]. Candidates: the
    endpoints and every real critical point of f in [0, 1] (the
    roots of A - pi*G + pi^2*B and, when B > 0, pi = G / (2B))."""
    d = float(np.mean(feat_n) - np.mean(feat_m))
    bq = d * d
    a_ = float(np.var(feat_u) - np.var(feat_m))
    g_ = float(np.var(feat_n) - np.var(feat_m)) + bq

    cands = [0.0, 1.0]
    if bq > 0.0:
        cands.append(g_ / (2.0 * bq))
        disc = g_ * g_ - 4.0 * bq * a_
        if disc >= 0.0:
            r = disc ** 0.5
            cands.append((g_ + r) / (2.0 * bq))
            cands.append((g_ - r) / (2.0 * bq))
    elif abs(g_) > 0.0:
        cands.append(a_ / g_)

    best, best_f = 0.0, None
    for p in cands:
        if 0.0 <= p <= 1.0:
            f = (a_ - p * g_ + p * p * bq) ** 2
            if best_f is None or f < best_f:
                best, best_f = p, f
    return best


def smi_band(feat_m, feat_n, feat_u, rng):
    """The paper's uncertainty procedure: bootstrap the audited set
    alone, re-estimate, report the {5%, 95%} quantiles."""
    n = len(feat_u)
    ests = np.empty(B_BOOTSTRAP)
    for b in range(B_BOOTSTRAP):
        res = feat_u[rng.integers(0, n, size=n)]
        ests[b] = smi_point(feat_m, feat_n, res)
    return float(np.quantile(ests, 0.05)), float(np.quantile(ests, 0.95))


# ------------------------------------------------------------- samplers

def world_features(a, b, n, rng):
    """Fiber sampler for the constant-menu depth world at 2^a 3^b.

    Returns (feat_m, feat_n, feat_u): window-count features (number
    of 2-moves in the WINDOW positions after the first) for n
    class-conditional member samples (first move 2), n non-member
    samples (first move 3), and n unconditioned fiber samples --
    each an independent uniform arrangement, which IS the route
    posterior at every temperature (weight-side symmetry)."""
    t = a + b

    def window_counts(twos, total, m):
        # m independent uniform shuffles of `twos` 2s among `total`
        # slots; count 2s landing in the first WINDOW slots.
        keys = rng.random((m, total))
        order = np.argsort(keys, axis=1)
        # positions 0..twos-1 of each row's order are the 2-slots
        is_two = order < twos
        return is_two[:, :WINDOW].sum(axis=1).astype(float)

    feat_m = window_counts(a - 1, t - 1, n)   # first move 2 fixed
    feat_n = window_counts(a, t - 1, n)       # first move 3 fixed
    # unconditioned: shuffle all T, feature reads positions 2..1+W,
    # i.e. the first WINDOW slots after dropping position 1.
    keys = rng.random((n, t))
    order = np.argsort(keys, axis=1)
    is_two = order < a
    feat_u = is_two[:, 1:1 + WINDOW].sum(axis=1).astype(float)
    return feat_m, feat_n, feat_u


def gaussian_features(mu_m, sd_m, mu_n, sd_n, pi, n, rng):
    """Ring-free synthetic cell: exact Gaussian mixture with known
    pi. Returns (feat_m, feat_n, feat_u)."""
    feat_m = rng.normal(mu_m, sd_m, n)
    feat_n = rng.normal(mu_n, sd_n, n)
    from_n = rng.random(n) < pi
    feat_u = np.where(from_n, rng.normal(mu_n, sd_n, n),
                      rng.normal(mu_m, sd_m, n))
    return feat_m, feat_n, feat_u


# ------------------------------------------------------------ the cells

def run_cell(name, sampler, pi_exact, sizes=AUDIT_SIZES):
    pi_f = float(pi_exact)
    print(f"\n== cell {name}  exact pi = {pi_exact} = {pi_f:.4f} ==")
    print(f"{'n':>6} {'mean bias':>10} {'RMSE':>8} {'flip':>6} "
          f"{'cover90':>8} {'band width':>11}")
    for n in sizes:
        ests = np.empty(R_REPLICATES)
        covered = 0
        widths = np.empty(R_REPLICATES)
        for r in range(R_REPLICATES):
            fm, fn, fu = sampler(n, RNG)
            ests[r] = smi_point(fm, fn, fu)
            lo, hi = smi_band(fm, fn, fu, RNG)
            widths[r] = hi - lo
            if lo <= pi_f <= hi:
                covered += 1
        bias = float(np.mean(ests) - pi_f)
        rmse = float(np.sqrt(np.mean((ests - pi_f) ** 2)))
        flip = float(np.mean(np.abs(ests - (1.0 - pi_f))
                             < np.abs(ests - pi_f)))
        print(f"{n:>6} {bias:>10.4f} {rmse:>8.4f} {flip:>6.3f} "
              f"{covered / R_REPLICATES:>8.3f} "
              f"{float(np.mean(widths)):>11.4f}")


def main():
    # PC: positive control, one large draw, gate before everything.
    fm, fn, fu = gaussian_features(0.0, 1.0, 3.0, 2.0, 0.3, 5000, RNG)
    pc = smi_point(fm, fn, fu)
    ok = abs(pc - 0.3) <= 0.05
    print(f"PC positive control: pi_hat = {pc:.4f} "
          f"(target 0.30 +- 0.05) -> {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("HARNESS FAILURE -- no other cell is readable.")
        return

    # S: the designed identifiability cell (equal class variances).
    run_cell("S  (equal-variance Gaussians)",
             lambda n, rng: gaussian_features(0.0, 1.0, 2.0, 1.0,
                                              0.2, n, rng),
             Fraction(1, 5))

    # World cells: the constant-menu depth world, X = first move.
    for (a, b) in ((5, 5), (12, 3), (2, 8)):
        pi = Fraction(b, a + b)
        run_cell(f"W (a,b)=({a},{b})",
                 lambda n, rng, a=a, b=b: world_features(a, b, n, rng),
                 pi)


if __name__ == "__main__":
    main()
