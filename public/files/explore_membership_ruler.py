"""explore_membership_ruler.py -- THE DELETION-AUDIT RULER, SECOND
TOOL (sibling of explore_deletion_ruler.py, which scored a
mixture-proportion unlearning audit; worlds under measurement:
explore_forgetting_certificate.py).

THE QUESTION. The constant-menu amnesia world computes the posterior
of a forgotten datum given the still-working state as an exact
Fraction, so any audit that STATES a membership probability is
scoreable on the calibration of that statement. The first tool scored
was a population estimator (mixture proportion + bootstrap band).
This rig scores a SECOND published audit from a DIFFERENT estimator
family -- the per-example likelihood-ratio family -- on the same
dial placements. Do two independent tool families fail the same way?

THE CUSTOMER (read in full before this script was written). U-LiRA
(Hayes, Shumailov, Triantafillou, Khalifa and Papernot, "Inexact
Unlearning Needs More Careful Evaluations to Avoid a False Sense of
Privacy", arXiv:2403.01218), the per-example unlearning membership
inference audit: LiRA (Carlini et al.) adapted to unlearning.
Algorithm 1, verbatim in structure:

    for each shadow world t: collect the score of the audited
        example under the unlearned model (in-world) and under the
        retrained-without model (out-world);
    fit a Gaussian N(mu1, sigma1^2) to the in-world scores and
        N(mu0, sigma0^2) to the out-world scores;
    for the released model's score o:
        p_member = N(o; mu1, sigma1^2)
                   / (N(o; mu1, sigma1^2) + N(o; mu0, sigma0^2));
    predict member iff p_member > 1/2.

Its two stated outputs (Sec. 4.3, "Evaluation metrics"): balanced
membership-inference attack accuracy on equal-size member/non-member
sets, and the per-sample PREDICTED MEMBERSHIP PROBABILITY p_member
-- "an optimal unlearning algorithm would result in a predicted
membership probability of 1/2 for all z". The paper states NO
interval: its stated uncertainty IS the per-sample probability.
So where the first tool was scored on band coverage, this one is
scored on CALIBRATION -- the distance between the probability it
states and the exact posterior the world computes -- which is the
coverage question asked of a tool whose interval is a point
probability. (The paper's logit rescaling phi applies to softmax
confidences; here the audit score is already a scalar feature, so
the Gaussian fit is applied to it directly -- the fit-Gaussians-to-
the-two-score-populations step IS the estimator.) The paper's own
per-example shadow count is 128, the top of this rig's N axis.

THE BRIDGE (why the world scores this tool exactly). U-LiRA's
p_member is by construction the Bayes posterior of membership at
prior 1/2 under the fitted Gaussians, so its estimand at fiber
inputs is the EQUAL-PRIOR posterior q = P(f|member) /
(P(f|member) + P(f|non-member)) -- and in the constant-menu world
both class-conditionals are exact hypergeometric Fractions, so q is
an exact Fraction per feature value, and the optimal balanced
accuracy (the other stated output's ceiling) is an exact Fraction
too. The tool's whole output surface has exact ground truth here.

THE WORLD (the parent rig's, unchanged). Constant menu {2, 3},
endpoint 2^a * 3^b, age T = a + b; route posterior uniform over the
C(T, a) arrangements at every temperature (weight-side symmetry,
Lemma C of explore_forgetting_certificate.py). Forgotten datum X =
first move; member class X = 2, non-member X = 3. Audit feature of
a history: the count of 2-moves in the WINDOW = 3 positions after
the first. Class-conditionals: hypergeometric -- member draws its
window from a-1 twos among T-1 slots, non-member from a twos among
T-1 slots:  P(c | K twos among M slots) = C(w,c) C(M-w, K-c) / C(M,K).

HAND-ATTACK (pre-engine; the index convention re-derived from the
parent: the window is the WINDOW positions AFTER the first move,
i.e. the first WINDOW slots of the remaining T-1). At (a,b) = (12,3),
M = 14, w = 3:
    member  K = 11: Pm = (1, 33, 165, 165)/364
    non     K = 12: Pn = (0, 12, 132, 220)/364
    exact q       = (1, 11/15, 5/9, 3/7)
    exact Bayes balanced accuracy = (199 + 220)/728 = 419/728
Gaussian-limit posteriors (fits at their exact hypergeometric means
and variances -- what infinite shadow data converges to):
    mu_m = 33/14, var_m = 1089/2548; mu_n = 18/7, var_n = 198/637
    p_limit ~= (0.982, 0.840, 0.554, 0.414)
so the limit is OVERCONFIDENT at the interior tail cell c=1 (0.840
against 11/15 = 0.733) and UNDERCONFIDENT exactly where the truth
is certain (0.982 against q(0) = 1): a deterministic miscalibration
that no shadow count cures, carrying ~0.62 of the audited mass to
the more-extreme side at this dial. The ring-free reproduction
(cell S): a two-atom feature at {0, 3}, member mass (0.9, 0.1),
non-member mirrored -- exact posterior at the member atom 0.9,
Gaussian-limit 1/(1 + exp(-40/9)) ~= 0.988, because a Gaussian tail
prices a far atom at exp(-squared distance) where the true
distribution holds linear mass. And at (a,b) = (2,8), N = 8 shadow
samples, the member feature takes two values with mass (2/3, 1/3),
so with probability (2/3)^8 + (1/3)^8 ~= 0.039 the fit COLLAPSES
(sample variance zero) and the stated probability degenerates to
certainty; either-class collapse there ~= 0.044.

THE CELLS.
  PC  positive control, harness only: member N(0,1), non N(3,4) --
      the Gaussian model WELL-SPECIFIED, so p_member must calibrate
      and accuracy must reach the Gaussian Bayes accuracy. Gate.
  S   the designed discreteness cell, ring-free: two atoms {0, 3},
      member mass (0.9, 0.1), non-member (0.1, 0.9).
  W1  world cell (5,5):  q = (5/7, 4/7, 3/7, 2/7), Bayes 25/42.
  W2  world cell (12,3): the hand-attacked cell above.
  W3  world cell (2,8):  supports differ -- Pm = (2/3, 1/3, 0, 0),
      Pn = (15, 18, 3, 0)/36; q = (8/13, 2/5, 0, -), Bayes 5/8.

THE MEASUREMENT. Shadow sizes N in {8, 32, 128} (128 = the paper's
own), R = 400 replicates per (cell, N). Each replicate draws N
member and N non-member shadow features, fits the two Gaussians
(mean + MLE variance; a zero variance is kept as the degenerate
point-mass limit the fit converges to), and is scored EXACTLY over
the discrete support (no evaluation sampling):
  acc      balanced accuracy of the fitted rule (member iff
           p_hat > 1/2), against the exact Bayes accuracy;
  ECE      sum_c P_u(c) |p_hat(c) - q(c)|, the u-fiber-weighted
           calibration error, P_u = (a/T) Pm + (b/T) Pn;
  OVERCONF sum of P_u(c) where p_hat(c) is strictly more extreme
           than q(c) on the same side of 1/2;
  SAT      sum of P_u(c) where p_hat(c) > 0.99 or < 0.01 while
           0.01 < q(c) < 0.99 (stated near-certainty at an interior
           truth);
  COLLAPSE fraction of replicates with a zero-variance fit.
PC is scored by Monte Carlo (2000 eval draws per class) against the
closed-form Gaussian posterior. Printed per (cell, N); plus the
per-feature-cell table (mean p_hat against the Gaussian-limit and
exact q) at N = 128 for S and W2.

PREDICTIONS (fixed before the run).
  PR1 (PC gate): at N = 128 balanced accuracy within +-0.02 of the
      Gaussian Bayes accuracy and mean |p_hat - true posterior|
      < 0.05. Must pass before any other cell is read.
  PR2 (the deterministic limit, hand-derived): at N = 128 the mean
      per-cell p_hat approaches the Gaussian-limit values -- W2
      ~= (0.982, 0.840, 0.554, 0.414) against exact (1, 0.733,
      0.556, 0.429); S ~= 0.988 at the member atom against exact
      0.9 -- and ECE does NOT fall to zero as N grows (limits
      ~0.014 at W2, ~0.09 at S).
  PR3 (the decision survives): balanced accuracy sits within a few
      points of exact Bayes at N = 128 in every cell -- the failure
      lands in the stated probability, not the membership call.
  PR4 (small N): at N = 8 the W3 collapse rate is near the
      hand-derived 0.044 and SAT is nonzero in flip-prone cells;
      the full coverage-style reading (does stated certainty outrun
      accuracy, and in the first tool's direction?) is weighed
      after the run.

RUN. python explore_membership_ruler.py   (estimate: well under a
minute, single process, memory far under the analysis ceiling).

FINDINGS (from the printed run below; R = 400 replicates per
discrete (cell, N) and 100 for PC; the parent tool's control rerun
first and reproducing its frozen record byte for byte).

  PR1 PASS: acc 0.8530 against Bayes 0.8539, posterior MAE 0.0174.

  PR2 CONFIRMED (the deterministic limit): at N = 128 the mean
  per-cell stated probability sits at the hand-derived Gaussian
  limit, not at the exact posterior -- W2 (0.951, 0.830, 0.559,
  0.412) against exact (1, 0.733, 0.556, 0.429) with limit (0.982,
  0.840, 0.554, 0.414); S states 0.985 at the member atom against
  an exact 0.9 (limit 0.988). ECE plateaus instead of vanishing:
  S 0.091 / 0.080 / 0.085 across N = 8/32/128 (deterministic floor
  ~0.088); W2 falls 0.142 -> 0.060 -> 0.032 toward its ~0.014
  floor, bounded away from zero.

  PR3 CONFIRMED (the decision survives): balanced accuracy at
  N = 128 matches exact Bayes to <= 4e-4 in every cell (0.9000 /
  0.9, 0.5951 / 0.5952, 0.5752 / 0.5755, 0.6250 / 0.6250). The
  membership CALL is fine; the failure lands entirely in the
  stated probability.

  PR4 + the ruler reading: the W3 collapse rate at N = 8 is 0.043
  (hand-derived 0.044) and SAT is nonzero in every flip-prone cell
  at N = 8 -- at S, 0.642 of the audited mass gets a stated
  near-certainty (past 0.99) against an exact posterior of 0.9 or
  0.1, still 0.491 at N = 128. And OVERCONF RISES with shadow
  data -- S 0.890 -> 0.970 -> 1.000, W3 0.571 -> 0.720 -> 0.808 --
  because more data does not cure the miscalibrated limit, it
  concentrates every replicate onto it: the Gaussian smoothing
  moves certainty from where it belongs (the structurally certain
  cell q = 1 is stated at 0.95) to where it does not (interior
  cells stated past 0.99). SAME DIRECTION AS THE FIRST TOOL:
  stated certainty outrunning the accuracy behind it -- there a
  bootstrap band narrowing while its coverage stays low, here a
  stated probability strictly more extreme than the exact
  posterior on an audited-mass fraction that GROWS with the
  tool's own data axis.

  Scope: one audit tool (U-LiRA with scalar features and the
  Gaussian fits of its own Algorithm 1), one world family, one
  seed stream; the deterministic-limit miscalibration is a fact
  about the estimator's model class (a Gaussian tail pricing
  atoms), reproduced ring-free in cell S.

PRINTED OUTPUT (verbatim):

  PC positive control (N=128): acc = 0.8530 vs Bayes 0.8539,
  posterior MAE = 0.0174 -> PASS

  == cell S  (two atoms {0,3})  exact Bayes acc = 9/10 = 0.9000 ==
       N  mean acc      ECE  overconf     sat  collapse
       8    0.9000   0.0911     0.890   0.642     0.642
      32    0.9000   0.0798     0.970   0.547     0.052
     128    0.9000   0.0851     1.000   0.491     0.000
     per-cell at N=128:    c  mean p_hat  gauss limit   exact q
                           0      0.9848       0.9884    0.9000
                           3      0.0147       0.0116    0.1000

  == cell W (a,b)=(5,5)  exact Bayes acc = 25/42 = 0.5952 ==
       N  mean acc      ECE  overconf     sat  collapse
       8    0.5511   0.1300     0.540   0.023     0.003
      32    0.5809   0.0560     0.552   0.000     0.000
     128    0.5951   0.0267     0.542   0.000     0.000

  == cell W (a,b)=(12,3)  exact Bayes acc = 419/728 = 0.5755 ==
       N  mean acc      ECE  overconf     sat  collapse
       8    0.5317   0.1422     0.520   0.046     0.030
      32    0.5620   0.0604     0.572   0.004     0.000
     128    0.5752   0.0320     0.638   0.000     0.000
     per-cell at N=128:    c  mean p_hat  gauss limit   exact q
                           0      0.9513       0.9816    1.0000
                           1      0.8300       0.8400    0.7333
                           2      0.5588       0.5540    0.5556
                           3      0.4119       0.4141    0.4286

  == cell W (a,b)=(2,8)  exact Bayes acc = 5/8 = 0.6250 ==
       N  mean acc      ECE  overconf     sat  collapse
       8    0.5943   0.1297     0.571   0.040     0.043
      32    0.6226   0.0637     0.720   0.000     0.000
     128    0.6250   0.0417     0.808   0.000     0.000
"""

import math
from fractions import Fraction

import numpy as np

RNG = np.random.default_rng(20260804)

R_REPLICATES = 400
SHADOW_SIZES = (8, 32, 128)
WINDOW = 3
EXTREME = 0.01


# ------------------------------------------------- exact world tables

def hyper_pmf(K, M, w=WINDOW):
    """P(window count = c | K twos among M slots), c = 0..w. Exact."""
    return [Fraction(math.comb(w, c) * math.comb(M - w, K - c),
                     math.comb(M, K))
            if 0 <= K - c <= M - w else Fraction(0)
            for c in range(w + 1)]


def world_tables(a, b):
    """Exact member/non-member class-conditionals, equal-prior
    posterior q, u-fiber weights, and Bayes balanced accuracy for
    the dial cell (a, b). Member = first move 2 (window drawn from
    a-1 twos among T-1), non-member = first move 3 (a twos)."""
    t = a + b
    pm = hyper_pmf(a - 1, t - 1)
    pn = hyper_pmf(a, t - 1)
    q = [Fraction(m, m + n) if m + n else None
         for m, n in zip(pm, pn)]
    pu = [Fraction(a, t) * m + Fraction(b, t) * n
          for m, n in zip(pm, pn)]
    bayes = Fraction(1, 2) * (sum(m for m, n in zip(pm, pn) if m > n)
                              + sum(n for m, n in zip(pm, pn)
                                    if m <= n))
    return pm, pn, q, pu, bayes


def atom_tables(atoms, pm, pn, prior_m=Fraction(1, 2)):
    """Same exact tables for a designed discrete cell."""
    pm = [Fraction(x) for x in pm]
    pn = [Fraction(x) for x in pn]
    q = [Fraction(m, m + n) if m + n else None
         for m, n in zip(pm, pn)]
    pu = [prior_m * m + (1 - prior_m) * n for m, n in zip(pm, pn)]
    bayes = Fraction(1, 2) * (sum(m for m, n in zip(pm, pn) if m > n)
                              + sum(n for m, n in zip(pm, pn)
                                    if m <= n))
    return pm, pn, q, pu, bayes


# ------------------------------------------------------------ U-LiRA

def gauss_logpdf(x, mu, var):
    return -0.5 * ((x - mu) ** 2 / var + math.log(2 * math.pi * var))


def ulira_posterior(o, mu1, var1, mu0, var0):
    """Algorithm 1's p_member at score o. A zero variance is the
    degenerate point-mass limit: density infinite at its mean, zero
    elsewhere."""
    d1 = (var1 == 0.0)
    d0 = (var0 == 0.0)
    if d1 or d0:
        hit1 = d1 and o == mu1
        hit0 = d0 and o == mu0
        if d1 and d0:
            if hit1 and hit0:
                return 0.5
            return 1.0 if hit1 else 0.0
        if d1:
            return 1.0 if hit1 else 0.0
        return 0.0 if hit0 else 1.0
    l1 = gauss_logpdf(o, mu1, var1)
    l0 = gauss_logpdf(o, mu0, var0)
    return 1.0 / (1.0 + math.exp(min(700.0, max(-700.0, l0 - l1))))


def fit(sample):
    return float(np.mean(sample)), float(np.var(sample))


# ------------------------------------------------- discrete-cell rig

def run_discrete_cell(name, atoms, pm, pn, q, pu, bayes,
                      limit_table=False):
    """Score U-LiRA exactly over a discrete support: shadow draws
    are the only randomness; accuracy, ECE, OVERCONF, SAT computed
    against the exact Fractions."""
    pmf_m = np.array([float(x) for x in pm])
    pmf_n = np.array([float(x) for x in pn])
    atoms_f = [float(x) for x in atoms]
    print(f"\n== cell {name}  exact Bayes acc = {bayes} "
          f"= {float(bayes):.4f} ==")
    print(f"{'N':>6} {'mean acc':>9} {'ECE':>8} {'overconf':>9} "
          f"{'sat':>7} {'collapse':>9}")
    mean_phat_at_top = None
    for n_sh in SHADOW_SIZES:
        accs = np.empty(R_REPLICATES)
        eces = np.empty(R_REPLICATES)
        overs = np.empty(R_REPLICATES)
        sats = np.empty(R_REPLICATES)
        collapses = 0
        phat_sum = np.zeros(len(atoms))
        for r in range(R_REPLICATES):
            sm = RNG.choice(atoms_f, size=n_sh, p=pmf_m)
            sn = RNG.choice(atoms_f, size=n_sh, p=pmf_n)
            mu1, var1 = fit(sm)
            mu0, var0 = fit(sn)
            if var1 == 0.0 or var0 == 0.0:
                collapses += 1
            ph = [ulira_posterior(o, mu1, var1, mu0, var0)
                  for o in atoms_f]
            phat_sum += ph
            acc = ece = over = sat = 0.0
            for c, p in enumerate(ph):
                if pm[c] + pn[c] == 0:
                    continue
                acc += 0.5 * (float(pm[c]) if p > 0.5
                              else float(pn[c]))
                qc, puc = float(q[c]), float(pu[c])
                ece += puc * abs(p - qc)
                if (p - 0.5) * (qc - 0.5) > 0 and \
                        abs(p - 0.5) > abs(qc - 0.5):
                    over += puc
                if (p > 1 - EXTREME or p < EXTREME) and \
                        EXTREME < qc < 1 - EXTREME:
                    sat += puc
            accs[r], eces[r], overs[r], sats[r] = acc, ece, over, sat
        print(f"{n_sh:>6} {np.mean(accs):>9.4f} {np.mean(eces):>8.4f} "
              f"{np.mean(overs):>9.3f} {np.mean(sats):>7.3f} "
              f"{collapses / R_REPLICATES:>9.3f}")
        mean_phat_at_top = phat_sum / R_REPLICATES
    if limit_table:
        mu_m = float(sum(f * m for f, m in zip(atoms, pm)))
        mu_n = float(sum(f * m for f, m in zip(atoms, pn)))
        vm = float(sum(f * f * m for f, m in zip(atoms, pm))) - mu_m ** 2
        vn = float(sum(f * f * m for f, m in zip(atoms, pn))) - mu_n ** 2
        print(f"   per-cell at N=128: {'c':>4} {'mean p_hat':>11} "
              f"{'gauss limit':>12} {'exact q':>9}")
        for c in range(len(atoms)):
            if pm[c] + pn[c] == 0:
                continue
            lim = ulira_posterior(atoms_f[c], mu_m, vm, mu_n, vn)
            print(f"{'':>21} {atoms_f[c]:>4.0f} "
                  f"{mean_phat_at_top[c]:>11.4f} {lim:>12.4f} "
                  f"{float(q[c]):>9.4f}")


# ---------------------------------------------------------------- PC

def run_pc():
    """Well-specified control: member N(0,1), non N(3,4). Gaussian
    Bayes accuracy by numeric integration on a fine grid; U-LiRA at
    N = 128 must reach it and must calibrate."""
    n_sh, n_ev = 128, 2000
    xs = np.linspace(-12.0, 15.0, 200001)
    dm = np.exp(-0.5 * xs ** 2) / math.sqrt(2 * math.pi)
    dn = np.exp(-0.5 * ((xs - 3.0) / 2.0) ** 2) / (2.0
                                                   * math.sqrt(2 * math.pi))
    dx = xs[1] - xs[0]
    bayes = 0.5 * (np.sum(np.where(dm > dn, dm, dn)) * dx)
    accs, maes = [], []
    for r in range(100):
        mu1, var1 = fit(RNG.normal(0.0, 1.0, n_sh))
        mu0, var0 = fit(RNG.normal(3.0, 2.0, n_sh))
        em = RNG.normal(0.0, 1.0, n_ev)
        en = RNG.normal(3.0, 2.0, n_ev)
        pm_ = np.array([ulira_posterior(o, mu1, var1, mu0, var0)
                        for o in em])
        pn_ = np.array([ulira_posterior(o, mu1, var1, mu0, var0)
                        for o in en])
        accs.append(0.5 * (np.mean(pm_ > 0.5) + np.mean(pn_ <= 0.5)))
        ev = np.concatenate([em, en])
        pv = np.concatenate([pm_, pn_])
        lm = -0.5 * ev ** 2
        ln = -0.5 * ((ev - 3.0) / 2.0) ** 2 - math.log(2.0)
        true_post = 1.0 / (1.0 + np.exp(ln - lm))
        maes.append(np.mean(np.abs(pv - true_post)))
    acc, mae = float(np.mean(accs)), float(np.mean(maes))
    ok = abs(acc - bayes) <= 0.02 and mae < 0.05
    print(f"PC positive control (N=128): acc = {acc:.4f} vs Bayes "
          f"{bayes:.4f}, posterior MAE = {mae:.4f} "
          f"-> {'PASS' if ok else 'FAIL'}")
    return ok


def main():
    if not run_pc():
        print("HARNESS FAILURE -- no other cell is readable.")
        return

    # S: the designed discreteness cell, ring-free.
    pm, pn, q, pu, bayes = atom_tables(
        (0, 3), (Fraction(9, 10), Fraction(1, 10)),
        (Fraction(1, 10), Fraction(9, 10)))
    run_discrete_cell("S  (two atoms {0,3})", (0, 3), pm, pn, q, pu,
                      bayes, limit_table=True)

    # World cells: the constant-menu depth world, X = first move.
    for (a, b) in ((5, 5), (12, 3), (2, 8)):
        pm, pn, q, pu, bayes = world_tables(a, b)
        run_discrete_cell(f"W (a,b)=({a},{b})",
                          tuple(range(WINDOW + 1)), pm, pn, q, pu,
                          bayes, limit_table=(a, b) == (12, 3))


if __name__ == "__main__":
    main()
