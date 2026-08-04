"""THE UNCOUNTED TERM: why a stated uncertainty fails in ONE direction.

THE QUESTION
------------
Three instrument corpora here report the same shape in different
vocabularies: a tool's STATED certainty outruns the accuracy behind it.
Six specimens are on record --- resubstitution's interval at the knife
cell (consistent point estimate, inconsistent interval, coverage 0.00
to 0.03 at every sample size), held-out plug-in coverage FALLING as
data grows (0.90, 0.50, 0.25, 0.15), a mixture unlearning audit whose
bootstrap band narrows while its coverage sits at 69 to 86 percent
against a nominal 90, a per-example likelihood-ratio audit whose stated
probability is strictly more extreme than the exact posterior --- and,
pointing the other way, two bracket estimators that cover at or above
nominal while certifying nothing.

Read together those six do NOT share a mechanism. One prices sampling
noise and omits its own bias at equal rates; one reports a precision
that decays faster than its fitted rule's excess risk; one is not
identified at all; one smooths an atomic truth with a continuous class.
So "one direction" is either a genre observation about audit tools, or
it is a law about something else entirely.

This rig asks the second reading. The proposed object is not the audit
and not the estimator: it is the UNCERTAINTY STATEMENT, and where its
arithmetic gets its terms. A stated uncertainty is a functional of the
estimator's OWN model, so it can count only error that model admits.
Error the model has no coordinate for is UNCOUNTED. Two claims follow,
and this rig is built to break either:

  THE SIGN LAW.  Direction is set by whether the uncounted term's sign
  is KNOWN. A BOUND statement absorbs it with a known sign, so it
  cannot be overconfident whatever the dial. A FIT statement carries no
  such guarantee, which is what makes it the only kind that CAN be ---
  an asymmetry, not a symmetry: nothing here forces a fit to fail in
  the bad direction, and the knife arm's own stated bar turns out to be
  3.10 to 3.26 times the true dispersion.

  THE RATE LAW.  Whether data cures it is decided by the trajectory of
  the uncounted term b(n) against the counted half-width h(n). Three
  regimes: b/h -> 0 (coverage -> nominal), b/h -> const (coverage sits
  at a constant below nominal, sample size irrelevant), b/h -> infinity
  (coverage -> 0, and more data makes it worse).

If both hold, the direction is not a property of audits at all: the six
specimens are points on one plane, and what differs between them is
which region of it their construction can reach.

THE WORLD
---------
The eval-ceiling corpus's own object, kept exact. M = 15 discrete cells
with a uniform cell prior; cell r carries a label rate eta_r as a
Fraction. The target is the Bayes error

    E = sum_r P(r) * min(eta_r, 1 - eta_r)

which is a closed form, not an estimate --- which is the whole reason
this family can serve as a ruler. Two worlds:

  W_CLEAR --- fifteen rates, none closer than 1/10 to 1/2, arranged in
    three groups of five with each group STRADDLING 1/2.
  W_KNIFE --- every eta_r = 1/2 exactly (the knife cell).

THE ARMS (four here; a second pass below adds two more)
-------------------------------------------------------
All four estimate the SAME target from the same draw, and differ only
in what their statement's arithmetic knows.

  A1 WELL-SPECIFIED FIT --- per-cell plug-in on W_CLEAR. The model
     class contains the truth.
  A2 KNIFE FIT --- per-cell plug-in on W_KNIFE. Same model class, same
     code; only the world moves onto the knife.
  A3 MISSPECIFIED FIT --- the same plug-in on W_CLEAR with the cells
     POOLED into the three groups. Since min is concave and each group
     straddles 1/2, the pooled model cannot represent the truth and its
     bias does not decay at all. The world is A1's; only the MODEL moves.
  A4 BOUND --- on either world: fit the per-cell majority rule on half
     the draw, score its 0-1 error on the other half, and state the
     one-sided upper confidence bound. Held-out risk exceeds the Bayes
     error by the rule's excess risk, a quantity of KNOWN SIGN, so the
     upper bound remains valid while the slack it carries is exactly
     the term A1 to A3 omit.

Every fit arm states the model-implied interval: Ehat read as an error
rate over n draws, half-width z * sqrt(Ehat (1 - Ehat) / n) at z = 1.96
for a nominal 95 percent. Empty cells take etahat = 1/2 (the corpus
records that this tie-break matters; it is fixed here and, at these
sample sizes over fifteen uniform cells, never fires).

THE HAND-ATTACK, BEFORE THE ENGINE
----------------------------------
Arm A2 is derivable on paper, and the derivation is what licenses the
rig to say anything new. On W_KNIFE, Ehat = sum_r Phat_r (1/2 -
|etahat_r - 1/2|), so the bias is minus the expected mean absolute
deviation. With n_r about n/M and etahat_r - 1/2 about N(0, 1/(4 n_r)),

    b  = -sqrt(M / (2 pi n))            (downward, order 1/sqrt(n))
    h  = z / (2 sqrt(n))                (the stated half-width)
    |b| / h = sqrt(2M/pi) / z           --- FREE OF n

At M = 15, z = 1.96 that constant is sqrt(30/pi)/1.96 = 1.5766. That
closed form is NOT new here: explore_ceiling_ruler.py derived the same
expression asymptotically for resubstitution's knife cell and measured
it at -1.48, -1.55, -1.56, -1.59 across four sample sizes. What the
re-derivation buys is a CONTROL, not a result — a differently written
estimator on a differently constructed world must land on that same
constant if A2 really is that cell, so reproducing 1.5766 is read
before any kill or survive result below.

The same derivation gives A2's coverage in closed form. The half-normal
terms give sd(Ehat) about sqrt((1 - 2/pi)/(4n)) = 0.3014/sqrt(n),
against b = -1.5451/sqrt(n) and h = 0.98/sqrt(n), so the coverage is
Phi(8.38) - Phi(1.875) = 0.030 --- flat in n, and inside the corpus's
measured 0.00 to 0.03.

THE PREDICTIONS, FIXED BEFORE THE ENGINE WAS WRITTEN
------------------------------------------------------------------
  Q1  CONTROL. A2 prints |b|/h in 1.55 to 1.60 at every n.
  Q2  A1 coverage within Monte-Carlo noise of the nominal 0.95 at every
      n (the well-specified regime: b/h -> 0).
  Q3  A2 coverage in 0.01 to 0.06 and FLAT in n --- no monotone trend
      beyond noise (the constant regime), hand value 0.030.
  Q4  A3 coverage strictly DECREASING across the four n and below 0.10
      at the largest; its |b|/h strictly INCREASING and above 3 at the
      largest (the divergent regime: more data makes it worse).
  Q5  A4 coverage never significantly below its OWN nominal on BOTH
      worlds and at every n. The bound uses the same z one-sided, so
      that nominal is 0.975 and not the fit arms' two-sided 0.95 ---
      scoring it against 0.95 would hand it a free margin of
      construction. Its interval contains the no-evidence value at half
      the settings or more --- correct and empty.
  Q6  THE LAW. At every (arm, world, n) cell the measured coverage
      agrees with the two-parameter Gaussian prediction computed from
      the MEASURED bias b, mean stated half-width h and measured sd
      sigma --- two-sided Phi((h-b)/sigma) - Phi((-h-b)/sigma) for the
      fit arms, one-sided Phi((b+h)/sigma) for the bound --- to within
      0.08 at 400 trials.

KILL-SHAPES, AS OBSERVABLES
---------------------------
  Q1 outside its band: the rig is broken and nothing else is read.
  Q6's largest deviation above 0.08: the direction is not a
    two-parameter phenomenon, the sign law is a genre observation, and
    the campaign is a funeral.
  Q5 violated at any cell: the sign law is FALSE outright and the
    fit/bound split is decoration.

THE SECOND PASS, AND WHY IT EXISTS
----------------------------------
The first run passed its control and its law, and MISSED Q4 in FORM: on
W_CLEAR the pooled model's gap is 0.1933, already 4.34 half-widths at
the smallest sample size, so the arm's coverage reads 0.000 at every n.
Coverage has a floor, and a kill frozen on a saturating observable
cannot be read --- the divergent regime is visible only in the ratio
there (4.34, 8.87, 17.78, 35.45). Rather than restate Q4, a second
world is run at a gap small enough that the CROSSING falls inside the
sample-size range.

W_MILD --- three groups of five, each holding four cells well off 1/2
and one cell just past it, so the pooled model's own limit misses the
truth by exactly 7/750 = 0.009333, against half-widths that run from
0.038 down to 0.005. The predictions, frozen before the second engine
edit:

  Q7  CONTROL. Per-cell fit on W_MILD: coverage within Monte-Carlo
      noise of nominal at every n --- the world is not the cause.
  Q8  Pooled fit on W_MILD: coverage strictly DECREASING across the
      four n, above 0.80 at the smallest and below 0.10 at the largest
      --- the shape the held-out specimen showed (0.90, 0.50, 0.25,
      0.15) with the gap now known exactly.
  Q9  The crossing is LOCATED by the ratio: at the smallest n where
      |b|/h exceeds 1, coverage is already below 0.5.
  Q10 Q6 still holds on the new cells (within 0.08).

RUN RECORD
----------
One run, 0.3 s, well under the memory default. 400 trials at each of
four sample sizes (500, 2000, 8000, 32000) on six arms across three
worlds, single seed stream (20638). 16 of 17 checks pass; the one FAIL
is Q4 as frozen and is reported below rather than restated. Exact
targets: 19/75 on W_CLEAR, 1/2 on W_KNIFE, the pooled model's own limit
67/150 (gap 0.193333) and 7/750 = 0.009333 on W_MILD.

FINDINGS
--------
F1  CONTROL: A2 IS THE CORPUS'S KNIFE CELL (the control, passed). The
    knife arm printed |b|/h = 1.5726, 1.5947, 1.5813, 1.5906 across a
    64-fold range of n against the pre-engine value sqrt(2M/pi)/z =
    1.5766. The closed form is the eval-ceiling corpus's own and is not
    a finding here; what the agreement establishes is that a
    differently written estimator on a differently constructed world
    lands on the same constant, so this arm is that cell and the arms
    beside it can be read. The agreement is also closer to the derived
    value than that corpus's own measurement of the same quantity
    (-1.48 to -1.59 there at 40 trials, 1.573 to 1.595 here at 400),
    which is mostly the trial count and is not claimed as a result. One
    thing the arm does add: the stated bar is the wrong size in its own
    right at that cell (h/sigma 3.10 to 3.26, too WIDE), so what destroys the
    coverage there is the bias and not the bar.

F2  THE SIGN LAW HOLDS ON ONE SIDE ONLY, AND ITS USUAL COROLLARY DOES
    NOT HOLD AT ALL (observation, 8 cells). The bound arm never covered
    significantly below its own one-sided nominal of 0.975 --- 0.963 to
    0.988 over eight cells, every one inside the Monte-Carlo band,
    including the knife world, where the fit arm on that same world
    (an independent draw, not a paired one) collapses to 0.015-0.035.
    No dial setting made it overconfident,
    which is the kill Q5 named and did not get. Two scopings the
    measurement forces, both against the law's own first statement:
      - the ASYMMETRY is the content. What is forced is that a bound
        cannot be overconfident, not that a fit must be: A1 is a fit
        and covers at nominal, and the knife arm's stated bar is 3.10
        to 3.26 times the true dispersion, so a fitted bar can be too WIDE and
        its failure direction is unguaranteed rather than guaranteed
        bad. A fit is the only kind that CAN fail downward, which is
        enough to explain why every documented overconfident specimen
        is one.
      - "correct and empty" belongs to the corpus's TWO brackets and
        not to bound statements as such: this bound excluded the
        no-evidence value 1/2 in 100% of trials on W_CLEAR at every n
        (it was not run on W_MILD). Q5b passed only because W_KNIFE's
        truth IS 1/2, so containing it there is correctness, not
        vacuity. Conservatism is forced by the sign; vacuity is not.

F3  THE RATE LAW, THREE REGIMES ON ONE DIAL (observation; the placing
    of each arm into its regime follows from construction, the
    trajectories do not). The same
    plug-in code, the same target, the trajectory of the uncounted term
    b against the counted half-width h deciding everything:
      b/h -> 0      (well-specified)  0.032 -> 0.002, coverage 0.955,
                    0.945, 0.932, 0.953 --- nominal, data cures it;
      b/h -> const  (knife)           1.573 to 1.595, coverage 0.035,
                    0.015, 0.025, 0.035 --- flat, data is irrelevant;
      b/h -> inf    (misspecified)    0.259 -> 1.781, coverage 0.915,
                    0.875, 0.555, 0.045 --- data makes it WORSE.
    In the third regime the bias sits on the exact misspecification gap
    7/750 = 0.009333 from n = 2000 on (0.00922, 0.00957, 0.00935), with
    a small-sample excess at the smallest n (0.01088), while the stated
    half-width halves at every step: nothing degrades except the claim.
    And the crossing has a usable location --- the
    coverage passes 1/2 where the uncounted term equals the stated
    half-width (0.555 at |b|/h = 0.911). That reading needs h to
    outrun the true sd, which holds at every fit arm here (h/sigma
    about 1.9 to 2.1, and 3.10 to 3.26 at the knife): at b = h the near tail
    contributes 1/2 and the far tail Phi(-2h/sigma) is negligible.

F4  COVERAGE IS A FUNCTION OF TWO RATIOS, AND OF NOTHING ELSE
    (observation, 28 cells; under approximate normality of the
    estimate the formula follows from construction, and what is
    measured is that the approximation holds at every cell). Across
    both statement kinds, six arms, three worlds and four sample sizes,
    the measured coverage matched the prediction
    computed from the measured bias, mean stated half-width and
    measured true sd --- largest deviation 0.0133, mean 0.0049, against
    a 0.08 tolerance at 400 trials. So mechanisms that read as distinct
    are not distinct where it counts: each acts only by moving
    (b/sigma, h/sigma), and the direction is set by which region of
    that plane a construction can reach. The scope is exactly what ran
    --- TWO of the four documented overconfidence mechanisms are
    instantiated here (the equal-rate omitted bias at the knife, and a
    model class that cannot hold the truth), plus the bound kind.
    Held-out's precision outrunning its excess risk, and the smoothing
    of an atomic truth by a continuous class, were not run; placing the
    documented specimens on this plane one by one is work this leaves.

F5  THE MISS, KEPT (Q4). Q4 froze the divergent regime's kill on
    coverage's TRAJECTORY, and on W_CLEAR the pooling gap is already
    4.34 half-widths at the smallest sample size, so coverage reads
    0.000 at all four n and cannot decrease. The prediction is wrong in
    FORM, not in content --- the ratio carried the regime there
    (4.344, 8.866, 17.776, 35.454) and W_MILD showed the trajectory
    the prediction wanted. The species is a kill frozen on a saturating
    observable; the check is left FAILING rather than restated.

F6  WHAT THIS DOES NOT SETTLE. Every arm here reports a bias with a
    KNOWN cause (a concave functional, or a named pooling gap), so the
    rig demonstrates the two-ratio law and the sign law but says
    nothing about whether an uncounted term is DETECTABLE from inside
    the estimator --- which is the question an auditor actually has.
    The non-identification specimen (twin minima) is also absent: it
    has no bias in this sense at all, its sigma being the wrong
    coordinate, so it sits outside the plane rather than on it.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
from fractions import Fraction

import numpy as np

Z = 1.96
NOMINAL = 0.95
ONE_SIDED = 0.975      # the bound arm's own nominal at the same z
TRIALS = 400
SIZES = (500, 2000, 8000, 32000)
SEED = 20638

# --- the worlds -----------------------------------------------------

# fifteen cells, three groups of five, every group straddling 1/2 and
# no rate closer than 1/10 to it.
W_CLEAR = [
    Fraction(1, 10), Fraction(3, 10), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5),
    Fraction(1, 5), Fraction(1, 4), Fraction(7, 10), Fraction(3, 4), Fraction(9, 10),
    Fraction(1, 10), Fraction(2, 5), Fraction(3, 5), Fraction(7, 10), Fraction(9, 10),
]
W_KNIFE = [Fraction(1, 2)] * 15

# the same three-group shape with a SMALL pooling gap: four cells well
# off 1/2 and one just past it, per group.
W_MILD = [
    Fraction(3, 10), Fraction(3, 10), Fraction(3, 10), Fraction(3, 10), Fraction(13, 25),
    Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(27, 50),
    Fraction(2, 5), Fraction(2, 5), Fraction(2, 5), Fraction(2, 5), Fraction(51, 100),
]

M = len(W_CLEAR)
GROUP = [r // 5 for r in range(M)]      # the misspecified model's classes
NGROUP = 3


def bayes_error(etas):
    """Exact target: sum_r P(r) min(eta_r, 1-eta_r), uniform P."""
    m = len(etas)
    return sum((min(e, 1 - e) for e in etas), Fraction(0)) / m


def group_truth(etas):
    """Exact value the POOLED model converges to: min of the group mean."""
    tot = Fraction(0)
    for g in range(NGROUP):
        members = [etas[r] for r in range(len(etas)) if GROUP[r] == g]
        bar = sum(members, Fraction(0)) / len(members)
        tot += min(bar, 1 - bar) * Fraction(len(members), len(etas))
    return tot


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def draw(rng, etas, n):
    """One draw: per-cell counts and per-cell positive-label counts."""
    p = np.full(M, 1.0 / M)
    counts = rng.multinomial(n, p)
    etaf = np.array([float(e) for e in etas])
    ones = rng.binomial(counts, etaf)
    return counts, ones


def fit_percell(counts, ones, n):
    """Per-cell plug-in estimate + the model-implied half-width."""
    with np.errstate(invalid="ignore", divide="ignore"):
        eta = np.where(counts > 0, ones / np.maximum(counts, 1), 0.5)
    est = float(np.sum((counts / n) * np.minimum(eta, 1.0 - eta)))
    half = Z * math.sqrt(max(est * (1.0 - est), 0.0) / n)
    return est, half


def fit_pooled(counts, ones, n):
    """The same plug-in with the cells pooled into the three groups."""
    gc = np.zeros(NGROUP)
    go = np.zeros(NGROUP)
    for r in range(M):
        gc[GROUP[r]] += counts[r]
        go[GROUP[r]] += ones[r]
    eta = np.where(gc > 0, go / np.maximum(gc, 1), 0.5)
    est = float(np.sum((gc / n) * np.minimum(eta, 1.0 - eta)))
    half = Z * math.sqrt(max(est * (1.0 - est), 0.0) / n)
    return est, half


def bound_arm(rng, etas, n):
    """Fit the per-cell majority rule on one half, score it on the other,
    and state the one-sided upper confidence bound."""
    n1 = n // 2
    n2 = n - n1
    c1, o1 = draw(rng, etas, n1)
    c2, o2 = draw(rng, etas, n2)
    with np.errstate(invalid="ignore", divide="ignore"):
        eta1 = np.where(c1 > 0, o1 / np.maximum(c1, 1), 0.5)
    pred1 = (eta1 >= 0.5)                      # ties predict label 1
    wrong = np.where(pred1, c2 - o2, o2)
    err = float(np.sum(wrong)) / n2
    half = Z * math.sqrt(max(err * (1.0 - err), 0.0) / n2)
    return err, half


def run_fit(name, etas, fitter, n, rng):
    ests = np.empty(TRIALS)
    halves = np.empty(TRIALS)
    for t in range(TRIALS):
        counts, ones = draw(rng, etas, n)
        ests[t], halves[t] = fitter(counts, ones, n)
    truth = float(bayes_error(etas))
    dev = ests - truth
    cov = float(np.mean(np.abs(dev) <= halves))
    b = float(np.mean(dev))
    h = float(np.mean(halves))
    s = float(np.std(dev, ddof=1))
    pred = phi((h - b) / s) - phi((-h - b) / s)
    return dict(arm=name, n=n, cov=cov, b=b, h=h, sd=s, pred=pred,
                ratio=abs(b) / h, truth=truth)


def run_bound(name, etas, n, rng):
    errs = np.empty(TRIALS)
    halves = np.empty(TRIALS)
    for t in range(TRIALS):
        errs[t], halves[t] = bound_arm(rng, etas, n)
    truth = float(bayes_error(etas))
    upper = errs + halves
    cov = float(np.mean(upper >= truth))
    noev = float(np.mean(upper >= 0.5))         # the no-evidence value
    dev = errs - truth
    b = float(np.mean(dev))
    h = float(np.mean(halves))
    s = float(np.std(dev, ddof=1))
    pred = phi((b + h) / s)
    return dict(arm=name, n=n, cov=cov, b=b, h=h, sd=s, pred=pred,
                ratio=abs(b) / h, truth=truth, noev=noev)


def main():
    rng = np.random.default_rng(SEED)
    print("THE UNCOUNTED TERM --- the statement, not the tool")
    print("=" * 68)
    e_clear = bayes_error(W_CLEAR)
    e_knife = bayes_error(W_KNIFE)
    print("W_CLEAR  exact Bayes error = %s = %.6f" % (e_clear, float(e_clear)))
    print("W_KNIFE  exact Bayes error = %s = %.6f" % (e_knife, float(e_knife)))
    for label, w in (("W_CLEAR", W_CLEAR), ("W_MILD", W_MILD)):
        print("pooled model's own limit on %s = %s = %.6f  (misspecification"
              " gap %s = %.6f)"
              % (label, group_truth(w), float(group_truth(w)),
                 group_truth(w) - bayes_error(w),
                 float(group_truth(w) - bayes_error(w))))
    print("W_MILD   exact Bayes error = %s = %.6f"
          % (bayes_error(W_MILD), float(bayes_error(W_MILD))))
    print("M = %d cells, %d trials, z = %.2f, nominal %.2f" % (M, TRIALS, Z, NOMINAL))
    print()

    rows = []
    for n in SIZES:
        rows.append(run_fit("A1 well-specified fit", W_CLEAR, fit_percell, n, rng))
    for n in SIZES:
        rows.append(run_fit("A2 knife fit", W_KNIFE, fit_percell, n, rng))
    for n in SIZES:
        rows.append(run_fit("A3 misspecified fit", W_CLEAR, fit_pooled, n, rng))
    for n in SIZES:
        rows.append(run_bound("A4 bound (clear)", W_CLEAR, n, rng))
    for n in SIZES:
        rows.append(run_bound("A4 bound (knife)", W_KNIFE, n, rng))
    for n in SIZES:
        rows.append(run_fit("A5 mild control", W_MILD, fit_percell, n, rng))
    for n in SIZES:
        rows.append(run_fit("A6 mild misspecified", W_MILD, fit_pooled, n, rng))

    print("%-22s %7s %8s %9s %9s %8s %8s %8s" %
          ("arm", "n", "coverage", "bias", "stated h", "true sd", "|b|/h", "predicted"))
    print("-" * 88)
    last = None
    for r in rows:
        if last is not None and r["arm"] != last:
            print("-" * 88)
        last = r["arm"]
        print("%-22s %7d %8.3f %9.5f %9.5f %8.5f %8.3f %8.3f" %
              (r["arm"], r["n"], r["cov"], r["b"], r["h"], r["sd"],
               r["ratio"], r["pred"]))
    print()

    checks = []

    # Q1 --- the positive control, read first.
    a2 = [r for r in rows if r["arm"] == "A2 knife fit"]
    hand = math.sqrt(2 * M / math.pi) / Z
    print("Q1 CONTROL  hand-derived |b|/h = sqrt(2M/pi)/z = %.4f" % hand)
    for r in a2:
        print("            n = %6d  measured %.4f" % (r["n"], r["ratio"]))
    ok = all(1.55 <= r["ratio"] <= 1.60 for r in a2)
    checks.append(("Q1 control: A2 |b|/h in [1.55, 1.60] at every n", ok))
    if not ok:
        print("\nCONTROL FAILED --- the rig is broken; no result below is read.")
        for label, good in checks:
            print("  %-62s %s" % (label, "PASS" if good else "FAIL"))
        return

    # Q2 --- the well-specified regime.
    a1 = [r for r in rows if r["arm"] == "A1 well-specified fit"]
    tol = 3.0 * math.sqrt(NOMINAL * (1 - NOMINAL) / TRIALS)
    print("\nQ2  well-specified coverage against nominal %.2f (3-sigma MC band"
          " %.3f)" % (NOMINAL, tol))
    for r in a1:
        print("    n = %6d  coverage %.3f   |b|/h %.4f" % (r["n"], r["cov"], r["ratio"]))
    checks.append(("Q2 A1 coverage within MC noise of nominal at every n",
                   all(abs(r["cov"] - NOMINAL) <= tol for r in a1)))
    checks.append(("Q2b A1 |b|/h falls with n (the b/h -> 0 regime)",
                   a1[-1]["ratio"] < a1[0]["ratio"]))

    # Q3 --- the constant regime.
    print("\nQ3  knife coverage, hand value 0.030")
    for r in a2:
        print("    n = %6d  coverage %.3f" % (r["n"], r["cov"]))
    covs2 = [r["cov"] for r in a2]
    checks.append(("Q3 A2 coverage in [0.01, 0.06] at every n",
                   all(0.01 <= c <= 0.06 for c in covs2)))
    checks.append(("Q3b A2 coverage flat: spread <= 0.04",
                   max(covs2) - min(covs2) <= 0.04))

    # Q4 --- the divergent regime.
    a3 = [r for r in rows if r["arm"] == "A3 misspecified fit"]
    print("\nQ4  misspecified: coverage and the uncounted ratio against n")
    for r in a3:
        print("    n = %6d  coverage %.3f   |b|/h %8.3f" % (r["n"], r["cov"], r["ratio"]))
    covs3 = [r["cov"] for r in a3]
    rat3 = [r["ratio"] for r in a3]
    checks.append(("Q4 A3 coverage strictly decreasing in n",
                   all(covs3[i] > covs3[i + 1] for i in range(len(covs3) - 1))))
    checks.append(("Q4b A3 coverage < 0.10 at the largest n", covs3[-1] < 0.10))
    checks.append(("Q4c A3 |b|/h strictly increasing in n",
                   all(rat3[i] < rat3[i + 1] for i in range(len(rat3) - 1))))
    checks.append(("Q4d A3 |b|/h > 3 at the largest n", rat3[-1] > 3.0))

    # Q5 --- the sign law.
    a4 = [r for r in rows if r["arm"].startswith("A4")]
    print("\nQ5  the bound, both worlds: coverage and how often it contains 1/2")
    for r in a4:
        print("    %-18s n = %6d  coverage %.3f   contains 1/2 in %.3f"
              % (r["arm"], r["n"], r["cov"], r["noev"]))
    # the bound states a ONE-SIDED interval at the same z, so its own
    # nominal is 0.975 --- scoring it at the fit arms' 0.95 would hand
    # it a margin it did not earn.
    band1 = 3.0 * math.sqrt(ONE_SIDED * (1 - ONE_SIDED) / TRIALS)
    print("    (the bound's own nominal is %.3f one-sided; 3-sigma MC band"
          " %.3f)" % (ONE_SIDED, band1))
    checks.append(("Q5 A4 coverage never significantly below its own nominal",
                   all(r["cov"] >= ONE_SIDED - band1 for r in a4)))
    checks.append(("Q5b A4 contains the no-evidence value at >= half the settings",
                   sum(1 for r in a4 if r["noev"] >= 0.5) >= len(a4) / 2))

    # Q7-Q9 --- the second pass, where the crossing is visible.
    a5 = [r for r in rows if r["arm"] == "A5 mild control"]
    a6 = [r for r in rows if r["arm"] == "A6 mild misspecified"]
    print("\nQ7  the mild world's own control (per-cell fit)")
    for r in a5:
        print("    n = %6d  coverage %.3f   |b|/h %.4f" % (r["n"], r["cov"], r["ratio"]))
    checks.append(("Q7 control: A5 coverage within MC noise of nominal at every n",
                   all(abs(r["cov"] - NOMINAL) <= tol for r in a5)))

    print("\nQ8/Q9  the mild pooling gap: the crossing, in coverage and in the ratio")
    for r in a6:
        print("    n = %6d  coverage %.3f   |b|/h %8.3f   bias %.5f"
              % (r["n"], r["cov"], r["ratio"], r["b"]))
    covs6 = [r["cov"] for r in a6]
    checks.append(("Q8 A6 coverage strictly decreasing in n",
                   all(covs6[i] > covs6[i + 1] for i in range(len(covs6) - 1))))
    checks.append(("Q8b A6 coverage > 0.80 at the smallest n", covs6[0] > 0.80))
    checks.append(("Q8c A6 coverage < 0.10 at the largest n", covs6[-1] < 0.10))
    crossed = [r for r in a6 if r["ratio"] > 1.0]
    print("    first n with |b|/h > 1: %s" % (crossed[0]["n"] if crossed else "none"))
    checks.append(("Q9 at the first n with |b|/h > 1, coverage is below 0.5",
                   bool(crossed) and crossed[0]["cov"] < 0.5))

    # Q6 --- the law itself.
    devs = [(abs(r["cov"] - r["pred"]), r["arm"], r["n"]) for r in rows]
    worst = max(devs)
    print("\nQ6  measured coverage against the two-parameter prediction")
    print("    largest deviation %.4f  (at %s, n = %d)" % (worst[0], worst[1], worst[2]))
    print("    mean deviation    %.4f" % (sum(d[0] for d in devs) / len(devs)))
    checks.append(("Q6 every cell within 0.08 of the two-parameter prediction",
                   worst[0] <= 0.08))

    print("\n" + "=" * 68)
    for label, good in checks:
        print("  %-62s %s" % (label, "PASS" if good else "FAIL"))
    print("\n%d/%d checks pass" % (sum(1 for _, g in checks if g), len(checks)))


if __name__ == "__main__":
    main()
