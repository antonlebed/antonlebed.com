"""Is the estimator failure shape a tower fact or a boundary fact?

THE QUESTION. The ruler run (explore_ceiling_ruler.py) found two
STRUCTURAL failures of standard Bayes-error estimators on the
threshold family: at the knife cell (every posterior exactly 1/2)
resubstitution's deficit and its own half-bar both scale as 1/sqrt(n),
so the interval never covers and the deficit-to-half-bar ratio is
sqrt(2M/pi)/Z free of n; and held-out coverage FALLS as data grows,
because it scores a fitted rule whose excess over the optimum decays
slower than its reported precision. Neither derivation used the ring:
what did the work was a posterior near 1/2 and a cell count M against
a sample size n. So the tower may only be supplying EXACTNESS of the
ground truth, not causing the failure. THE MOVE, ring-free: the same
estimators, the same protocols, on a synthetic family — M equiprobable
cells with per-cell label probability eta, no CRT, no residues, no
threshold — at tunable distance from 1/2.

THE DESIGN DECISION THAT MAKES THE COMPARISON CLEAN: this rig IMPORTS
the ruler rig's estimator functions and its BernoulliSampler rather
than copying them, so the estimator code is IDENTICAL by construction
and the one variable that changes is the sampler — cells drawn
uniformly with Bernoulli labels instead of x mod p residues of a
thresholded uniform draw. (BernoulliSampler was built for the ruler's
own ring-free positive control; here it IS the treatment.)

THE HAND DERIVATION (fixed before the engine). At eta = 1/2 every
cell's minority count has E[min(n0, n1)] = n_r/2 - E|n0 - n1|/2 with
E|n0 - n1| ~ sqrt(2 n_r / pi), so summing M cells at n_r ~ n/M the
resubstitution deficit is (1/2) sqrt(2M/(pi n)) while the stated
half-bar is Z/(2 sqrt(n)): the ratio is sqrt(2M/pi)/Z, n-free, and
NOTHING in the derivation mentions the ring — at M = 15 it is
1.5766, the exact constant the ring rig measured. The held-out
failure needs only a fixed gap delta = |eta - 1/2| small against
1/sqrt(n_r): per-cell majority flips persist while delta sqrt(n_r)
is order 1, so the fitted rule's true excess decays slower than the
test half's binomial bar until n_r passes 1/delta^2 — at M = 105,
delta = 1/22, that crossover sits beyond n = 32000, which is why the
ring series kept falling across the whole grid. Both derivations are
ring-free, so the SLATE'S PREDICTION IS REAPPEARANCE — and the kill
(either failure NOT reappearing) is the more valuable outcome, since
it would make the CRT geometry load-bearing where the derivation says
it is not.

THE CELLS, matched to the ring rig's by (M, eta) — the replication
detail that matters: at the ring's FLOOR-WIDE cell the single-valued
posterior is eta_r = P(x >= t | r) = 6/11 (label-1 rate 630/1155),
so R* = min(eta, 1-eta) = 5/11 and the tie->one untrained-cell guess
scores exactly R*; the synthetic cell uses eta = 6/11, not 5/11, to
carry that structure over.

  leg   M    eta          R*      matches ring cell
  S1    15   1/2          1/2     FLOOR-KNIFE (N=210, s=0)
  S2    105  6/11         5/11    FLOOR-WIDE (N=1155, s=0)
  S3    15   1/2 + delta  varies  none — the dial the ring cannot turn

n in {500, 2000, 8000, 32000}, TRIALS = 40, one fixed seed, exact
truth in Fraction — the ruler rig's own grid.

FROZEN PREDICTIONS (fixed before any code ran):
  PR0 (positive control, read FIRST — the ruler rig's K0 verbatim
      through the import): two cells, etas (0.2, 0.9), R* = 0.15,
      n = 8000: all three protocols cover in >= 34/40 trials, the two
      point protocols have |bias| < 0.01, and the Cover-Hart bracket
      excludes the no-evidence value 0.45 in >= 34/40.
  PR1 (the knife, ring-free): at M = 15, eta = 1/2, resubstitution
      coverage <= 0.10 at EVERY n, and the measured deficit-to-
      half-bar ratio sits in [-2.0, -1.2] at every n (asymptote
      -1.5766; the ring measured -1.48/-1.55/-1.56/-1.59).
  PR2 (the falling series, ring-free): at M = 105, eta = 6/11,
      held-out (tie -> one) coverage against R* = 5/11 starts
      >= 0.70 at n = 500, ends <= 0.35 at n = 32000, and falls by
      >= 0.40 across the grid (the ring series: 0.90, 0.50, 0.25,
      0.15).
  PR3 (the dial, the leg the ring cannot run): at M = 15, n = 8000,
      delta in {0, 1/64, 1/32, 1/16, 1/8, 1/4}: resubstitution
      coverage <= 0.10 at delta in {0, 1/64} and >= 0.85 at delta in
      {1/8, 1/4} — the failure is a distance-to-1/2 fact with its
      boundary near delta ~ sqrt(M/n) (here ~ 0.043), crossed inside
      the dial's range.
  KILL OBSERVABLES: a PR1 coverage above 0.10 at any n, a PR1 ratio
      drifting with n, or a PR2 series that holds or rises — any of
      which says the ring's geometry was load-bearing after all.

Memory trivial (counting arrays of size M); wall-clock estimate
~2 min (about 6M draws through pure-Python loops). Run:
python prime/code/explore_ruler_boundary.py

FINDINGS (entered by the post-run edit; the creating write ended at
the design).

  F0 (PR0 CONFIRMED). The imported estimators through the synthetic
      sampler at (0.2, 0.9): resub bias -0.0002 coverage 1.00,
      held-out bias -0.0010 coverage 1.00, Cover-Hart bracket
      coverage 0.95 with 0.45 excluded in 40/40. Healthy off 1/2.

  F1 (PR1 CONFIRMED — the knife is ring-free). M = 15, eta = 1/2:
      resubstitution coverage 0.05/0.00/0.00/0.05 at the four n, and
      the deficit-to-half-bar ratio -1.609/-1.599/-1.621/-1.519 —
      n-free against the derived sqrt(2M/pi)/Z = 1.5766, and
      indistinguishable from the ring rig's -1.48/-1.55/-1.56/-1.59.

  F2 (PR2 CONFIRMED — the falling series is ring-free). M = 105,
      eta = 6/11, held-out tie->one: coverage 0.88/0.68/0.23/0.25
      against the ring's 0.90/0.50/0.25/0.15 — the DIRECTION
      reappears (falls 0.63 across the grid; the 0.23 -> 0.25 tail
      step is inside the 40-trial noise the ring rig measured, 0.12).

  F3 (PR3 KILLED AS FROZEN, and the kill is the finding). The dial's
      coverage runs 0.00/0.85/1.00/0.95/0.95/0.95 at delta = 0, 1/64,
      1/32, 1/16, 1/8, 1/4 — the crossing sits BEFORE delta = 1/64 at
      n = 8000, not near sqrt(M/n) = 0.043 as frozen. The slate's
      kill predictions were derived and held; its boundary location
      was a margin guess and broke (the kill/margin split, again).
      The knife band is NARROW: one sixty-fourth from 1/2 lifts
      coverage from 0.00 to 0.85 at this n, still short of the
      nominal 0.95, and one thirty-second restores it outright.

  F4 (S3b, post-hoc leg, its mini-slate fixed before it ran —
      observation, one M, one seed). The crossing is a function of
      u = 2*delta*sqrt(n/M) alone within noise: coverage 0.57 at BOTH
      equal-u configs (1/128, 8000) and (1/64, 2000), and 0.95 at
      (1/128, 32000) against 0.85 at S3's equal-u (1/64, 8000). The
      interval-failure regime is the band u <~ 1.

  VERDICT (rule — the reappearance derived ring-free in the hand
      derivation and confirmed at the ring grid's own M, eta, n):
      BOTH structural failures are ESTIMATOR facts, not tower facts.
      What the ring supplies is not the failure but the PLACEMENT:
      its floor cells sit at eta = 1/2 EXACTLY, on a boundary the
      dial shows is ~1/64 wide at n = 8000, with the ground truth a
      Fraction — calibrated placement on a thin edge, not a cause.

  RUN RECORD: python prime/code/explore_ruler_boundary.py — 2.035 s
      real, all sections green, S0 asserts pass, verdict BOUNDARY
      FACT. One pre-verdict repair: the trial seed tuple was passed
      to random.Random, which rejects tuples — reseeded via an
      f-string; no verdict-path change.
"""

from fractions import Fraction
from math import pi, sqrt

from explore_ceiling_ruler import (
    Z, BernoulliSampler, _cell_distance_table,
    est_resub, est_heldout, est_covhart,
)
import random


def section(title):
    print(f"\n{'=' * 72}\n  {title}\n{'=' * 72}")


def run_trials(etas, n, trials, seed, est, **kw):
    """One (family, n) config: TRIALS draws through the imported
    sampler and estimator; returns per-trial (rhat, lo, hi). The seed
    keys on (M, n, trial) and not on eta, so S3's dial legs share
    random streams across delta — paired comparisons, and its
    delta = 0 row reprints S1's n = 8000 row exactly."""
    sam = BernoulliSampler(etas)
    out = []
    for t in range(trials):
        rng = random.Random(f"{seed}-{len(etas)}-{n}-{t}")
        xs = sam.draw(rng, n)
        cells = [sam.cell(x) for x in xs]
        labels = [sam.label(x, None) for x in xs]
        out.append(est(cells, labels, sam.M, rng, **kw))
    return out


def report(rows, truth, label):
    tf = float(truth)
    bias = sum(r[0] for r in rows) / len(rows) - tf
    cover = sum(1 for r in rows if r[1] <= tf <= r[2]) / len(rows)
    print(f"  {label}  bias {bias:+.4f}  coverage {cover:.2f}")
    return bias, cover


TRIALS = 40
SEED = 20260731
NS = [500, 2000, 8000, 32000]

# -- S0: the positive control, through the import ------------------------

section("S0. POSITIVE CONTROL — the ruler's K0 through the imported code")
etas = [0.2, 0.9]
truth = Fraction(15, 100)
sam = BernoulliSampler(etas)
dist = _cell_distance_table(sam, sam.M)
rows_a = run_trials(etas, 8000, TRIALS, SEED, est_resub)
rows_b = run_trials(etas, 8000, TRIALS, SEED, est_heldout, tie="one")
rows_c = run_trials(etas, 8000, TRIALS, SEED, est_covhart, dist=dist)
ba, ca = report(rows_a, truth, "resub   ")
bb, cb = report(rows_b, truth, "held-out")
cov_c = sum(1 for r in rows_c if r[1] <= float(truth) <= r[2]) / TRIALS
excl = sum(1 for r in rows_c if r[2] < 0.45 or r[1] > 0.45) / TRIALS
print(f"  covhart   bracket coverage {cov_c:.2f}  excludes 0.45 {excl:.2f}")
assert ca >= 34 / 40 and cb >= 34 / 40 and cov_c >= 34 / 40, "K0 cover"
assert abs(ba) < 0.01 and abs(bb) < 0.01, "K0 bias"
assert excl >= 34 / 40, "K0 informative"
print("  CONTROL PASSES — the imported estimators are healthy off 1/2")

# -- S1: the knife, ring-free --------------------------------------------

section("S1. THE KNIFE RING-FREE — M = 15, eta = 1/2, resubstitution")
M1 = 15
truth1 = Fraction(1, 2)
asym = sqrt(2 * M1 / pi) / Z
print(f"  asymptotic deficit/half-bar ratio sqrt(2M/pi)/Z = {asym:.4f}")
s1 = {}
for n in NS:
    rows = run_trials([0.5] * M1, n, TRIALS, SEED, est_resub)
    bias, cover = report(rows, truth1, f"n={n:5d}")
    halfbar = sum((r[2] - r[1]) / 2 for r in rows) / len(rows)
    ratio = bias / halfbar
    s1[n] = (bias, cover, ratio)
    print(f"           mean half-bar {halfbar:.4f}  ratio {ratio:+.3f}")

# -- S2: the falling series, ring-free -----------------------------------

section("S2. THE FALLING SERIES RING-FREE — M = 105, eta = 6/11, held-out")
M2 = 105
truth2 = Fraction(5, 11)
s2 = {}
for n in NS:
    rows = run_trials([6 / 11] * M2, n, TRIALS, SEED, est_heldout,
                      tie="one")
    bias, cover = report(rows, truth2, f"n={n:5d}")
    s2[n] = (bias, cover)

# -- S3: the dial — distance to 1/2, the leg the ring cannot run ---------

section("S3. THE DIAL — M = 15, n = 8000, eta = 1/2 + delta")
DELTAS = [0, Fraction(1, 64), Fraction(1, 32), Fraction(1, 16),
          Fraction(1, 8), Fraction(1, 4)]
s3 = {}
for d in DELTAS:
    eta = Fraction(1, 2) + d
    truth = Fraction(1, 2) - d
    rows = run_trials([float(eta)] * M1, 8000, TRIALS, SEED, est_resub)
    bias, cover = report(rows, truth, f"delta={float(d):.4f}")
    s3[d] = (bias, cover)
print(f"  boundary scale sqrt(M/n) = {sqrt(M1 / 8000):.4f}")

# -- S3b: POST-HOC (added after S3 printed; its mini-slate fixed before
# it ran). S3's frozen window misplaced the crossing: coverage was
# already 0.85 at delta = 1/64, so the boundary sits near
# 2*delta*sqrt(n/M) ~ 0.7, not at delta ~ sqrt(M/n). If the crossing
# is a pure function of u = 2*delta*sqrt(n/M), then equal-u configs
# have equal coverage within the 40-trial noise (~0.12): predict
# (1/128, 8000) and (1/64, 2000) agree (u = 0.36 both), and
# (1/128, 32000) agrees with S3's (1/64, 8000) = 0.85 (u = 0.72).

section("S3b. POST-HOC — is the crossing a function of u = 2*delta*sqrt(n/M)?")
for d, n in [(Fraction(1, 128), 8000), (Fraction(1, 64), 2000),
             (Fraction(1, 128), 32000)]:
    u = 2 * float(d) * sqrt(n / M1)
    truth = Fraction(1, 2) - d
    rows = run_trials([float(Fraction(1, 2) + d)] * M1, n, TRIALS,
                      SEED, est_resub)
    report(rows, truth, f"delta={float(d):.4f} n={n:5d} u={u:.2f}")

# -- S4: the verdict ------------------------------------------------------

section("S4. THE VERDICT — do the ring's structural failures need the ring?")
p1 = all(s1[n][1] <= 0.10 and -2.0 <= s1[n][2] <= -1.2 for n in NS)
p2 = (s2[500][1] >= 0.70 and s2[32000][1] <= 0.35
      and s2[500][1] - s2[32000][1] >= 0.40)
p3 = (all(s3[d][1] <= 0.10 for d in DELTAS[:2])
      and all(s3[d][1] >= 0.85 for d in DELTAS[-2:]))
print(f"  PR1 (knife reappears, ratio n-free):   {p1}")
print(f"  PR2 (falling series reappears):        {p2}")
print(f"  PR3 (dial crosses the boundary):       {p3}")
verdict = ("BOUNDARY FACT — the failures are estimator facts, no ring"
           if p1 and p2 else "RING LOAD-BEARING")
print(f"\n  VERDICT: {verdict}")
