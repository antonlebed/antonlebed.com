"""explore_ceiling_ruler.py -- THE THRESHOLD FAMILY AS A RULER FOR
BAYES-ERROR ESTIMATORS (the eval-ceiling corpus turned from a subject
into an instrument; sibling of explore_eval_ceiling.py,
explore_ceiling_anatomy.py and explore_ceiling_dials.py).

THE QUESTION. The ceiling corpus ships evaluation families whose
Bayes-optimal score is a proved closed form. As SUBJECTS those
families were buried: incumbents ESTIMATE Bayes error over natural
data, the edge here is EXACTNESS on designed families, and
field-scale value needs the estimation move that voids the edge.
Every word of that says nothing about the families as INSTRUMENTS.
A family whose Bayes error is a closed form is a RULER: it can score
any Bayes-error ESTIMATOR against ground truth, which is the one role
exactness does not void. So: do standard Bayes-error estimators
recover the closed form, and where do they fail?

The ruler is aimed where the family's own dial says it is hard.
- FLOOR CELLS: the ceiling equals the no-evidence floor, so the true
  Bayes error is exactly the prior's error -- the evidence is
  provably worth nothing. But the posterior is NOT flat there (the
  two-scores finding: off the middle window the posterior moves and
  never crosses 1/2), so every cell sits near 1/2 and a finite
  sample sees structure that provably is not worth anything.
- THE WINDOW EDGE: inside the odd-c middle window the ceiling is
  (c+1)/2c independent of t, so the true Bayes error is FLAT across
  the window while the no-evidence value is a tent. The edge is a
  KINK, not a jump (re-derived in the HAND DERIVATION rather than
  inherited): R* is continuous in t and its SLOPE changes.
  The plateau is the observable -- an estimator either reproduces a
  flat truth under a tented naive value, or it does not.

THE ESTIMATORS (two, each run under its own standard hygiene).
  E1 THE PLUG-IN (histogram) ESTIMATOR -- the textbook estimator for
     a categorical evidence channel: estimate the per-cell posterior
     by empirical frequency and sum the minority mass. Two protocols,
     which is the whole practitioner-level disagreement about it:
       E1a RESUBSTITUTION: (1/n) sum_r min(n_r0, n_r1).
       E1b HELD-OUT: fit the majority rule on half the sample, score
           0-1 error on the other half.
  E2 THE 1-NN COVER-HART BRACKET -- the textbook distribution-free
     estimator: R_NN is the 1-nearest-neighbour error under Hamming
     distance on the residue tuple, and Cover-Hart gives
     R* <= R_NN <= 2 R*(1 - R*), i.e. the bracket
     [(1 - sqrt(1 - 2 R_NN))/2, R_NN].
  STATED ERROR BARS, as a practitioner would report them: the
  binomial 95% bar 1.96 sqrt(Rhat(1-Rhat)/n) on the sample the
  estimate is computed from, and for E2 both bracket endpoints pushed
  out by that bar before the Cover-Hart map (which is increasing, so
  the lo end takes the lo bar).

THE ONE PIECE OF NEW CODE, named in advance: NONE of
the three ceiling rigs SAMPLES -- all are exhaustive or closed-form.
An estimator eats samples, so this file builds the sampler: draw x
uniform from Z/N, hand over the readable residues (x mod p)_{p in S},
label [x >= t]. Everything else the probe needs is already proved.

SCORING. A single draw's deviation is noise, so the instrument
reports what an estimator is actually judged on: BIAS (mean estimate
minus truth over TRIALS trials) and COVERAGE (the fraction of trials
whose own stated 95% interval contains the exact truth). Nominal
coverage is 0.95; the ruler's whole point is that the truth it is
compared against is a Fraction, not another estimate.

DESIGN. Five cells of the threshold family, chosen from the dial and
NOT from a scan -- three floor cells and two window cells (table
below), at n in {500, 2000, 8000, 32000}, TRIALS = 40, one fixed
seed. Plus the profile leg: the N = 105 cell over t = 38..67, which
crosses both window edges, at n = 8000. Each threshold in the profile
draws its OWN samples (seeded per t) rather than sharing one draw
across the row. That costs more than common random numbers would and
is worth it: the window's 14 in-window estimates are then
INDEPENDENT, and 14 independent estimates agreeing on a flat value is
stronger evidence for the plateau than 14 views of a single sample
would be. Exact truth in Fraction throughout.

  cell         N    S        M    c   t     R*      no-evidence
  FLOOR-KNIFE  210  (3,5)    15   14  105   1/2     1/2
  FLOOR-ODD    105  (3,5)    15   7   45    3/7     3/7
  WINDOW-EDGE  105  (3,5)    15   7   46    3/7     46/105
  WINDOW-PEAK  105  (3,5)    15   7   52    3/7     52/105
  FLOOR-WIDE   1155 (3,5,7)  105  11  525   5/11    5/11

CONTROLS (run and asserted before any estimate is read -- a blow-up
from a harness bug would otherwise read as a real failure, which is
exactly what these exist to catch).
  K0 THE POSITIVE CONTROL: a two-cell Bernoulli problem carried
     through the SAME sampler interface and the SAME estimator code
     -- cells equiprobable, eta = (0.2, 0.9), so R* = 0.15 exactly,
     far from 1/2 and far from any floor. All three protocols must
     cover R* in at least 34 of 40 trials at n = 8000; the two POINT
     protocols must additionally have |bias| < 0.01. E2 is scored on
     its bracket instead, because its point estimate is R_NN and not
     an estimate of R* at all: the bracket must EXCLUDE the
     no-evidence value 0.45, which is what makes it informative
     rather than merely correct. (That distinction is the control's
     own correction: the first slate asked E2's point estimate for a
     bias it was never claiming to have, and the control caught it
     before any grid result was read -- which is the guard working,
     not a result.) This is the run where the estimators are KNOWN
     to be accurate; nothing else is read until it passes.
  K1 THE TRUTH CONTROL: the exact Bayes error recomputed by direct
     fiber count must equal 1 - the closed form on every (cell, t)
     the file touches, profile leg included.
  K2 THE SAMPLER CONTROL: over the pooled draws at the largest n the
     empirical cell frequency matches 1/M and the empirical label
     frequency matches the exact (N-t)/N, both within 4 binomial
     standard errors.

HAND DERIVATION (fixed before the engine; the index convention
re-derived from the anatomy rig rather than recalled: x in {0..N-1},
residue r has fiber {r + jM : j = 0..c-1}).

Write t = qM + s with 0 <= s < M. The fiber below-count is
B(r) = q + [r < s], so eta_r = P(x >= t | r) = (c - B(r))/c takes at
most two values -- and exactly ONE when s = 0, which is the case at
three of the five cells here (FLOOR-KNIFE, FLOOR-ODD, FLOOR-WIDE).
That is not a detail: at those cells EVERY fiber carries the same
posterior, which is what makes eta_r = 1/2 exact at FLOOR-KNIFE
rather than an average, and so what makes finding 5's exemption
exact. The exact Bayes error is
    R* = (1/N) sum_r min(B(r), c - B(r)),
which the closed form evaluates to 1 - (c+1)/(2c) = (c-1)/(2c) inside
the odd-c middle window (c odd, q = (c-1)/2, s != 0) and to the
no-evidence value min(t, N-t)/N everywhere else.

  THE EDGE IS A KINK. At the window's lower edge t = mM (s = 0) the
  closed form gives the floor min(mM, N-mM)/N = mM/N = m/(2m+1) =
  (c-1)/(2c); inside the window it gives (c-1)/(2c). Equal. Same at
  the upper edge. So R* is CONTINUOUS at both edges and constant
  across the window, while min(t, N-t)/N keeps climbing to its peak
  at t = N/2. The window is exactly the interval on which the truth
  stops tracking the naive value, and the gap is the tent
  min(s, M-s)/N. That is what the profile leg measures.

  WHY THE FLOOR CELLS ARE HARD FOR E1. At a floor cell every eta_r
  lies on one side of 1/2 but close to it (4/7, 6/11, or exactly 1/2
  at FLOOR-KNIFE). E1a's summand min(n_r0, n_r1)/n_r is a concave
  function of an empirical frequency, so Jensen sends it BELOW
  min(eta_r, 1-eta_r); near eta = 1/2 the deficit is of order
  sqrt(1/n_r) = sqrt(M/n), which is the scale to watch. E1b scores a
  RULE rather than the optimum, so it sits ABOVE R* by the cost of
  the cells whose empirical majority flipped: sum_r P(r) |2 eta_r - 1|
  P(flip at n_r). At FLOOR-KNIFE that cost is exactly zero for a
  reason no other cell has -- eta_r = 1/2 exactly, so EVERY rule errs
  at exactly 1/2 and there is nothing a flip can cost.

  WHY E2 CANNOT BE WRONG AND MAY STILL BE USELESS. Cover-Hart is a
  theorem, so the only ways the bracket can miss are sampling noise
  and a coding error. What is unpriced is its WIDTH. With n >> M a
  test point's nearest neighbour is an exact residue match, so 1-NN
  degenerates to "return a random same-cell training label" and
  R_NN -> sum_r P(r) 2 eta_r (1 - eta_r), which at eta_r near 1/2 is
  near 1/2 whatever R* is. The bracket then runs from near
  (1 - sqrt(1 - 1))/2 = 1/2 downward only slowly -- width is the
  quantity to print.

  A NOTE ON THE 1-NN IMPLEMENTATION, so the record is not read as an
  approximation: the evidence is a residue tuple over S, so Hamming
  distance takes at most |S|+1 values and depends only on the pair of
  CELLS. The rig precomputes the M x M cell-distance table, and for
  each test cell aggregates the label counts of all training points
  in the tied nearest cells. Drawing the prediction from that
  aggregate is exactly uniform over the tied training points, which
  is the 1-NN rule with random tie-breaking, computed exactly.

PREDICTIONS (fixed before the run).
  R1 E1a is biased DOWN at every floor cell at every n, and the
     deficit shrinks like sqrt(M/n): at FLOOR-WIDE (M = 105) it is
     larger than at FLOOR-KNIFE (M = 15) at equal n. Its coverage at
     FLOOR-WIDE is below 0.5 at n = 500 and n = 2000.
  R2 E1b is biased UP at FLOOR-ODD and FLOOR-WIDE, by roughly
     |2 eta - 1| times the empirical-flip probability (order +0.04 at
     n = 500 on both), and is UNBIASED at FLOOR-KNIFE -- the one cell
     where every rule is exactly optimal.
  R3 E2's bracket contains R* on every cell at every n, and is WIDE:
     width above 0.2 at every floor cell, i.e. wider than the whole
     tent (max 7/105 = 0.067) it would have to resolve.
  R4 THE PROFILE. True R* is flat at 3/7 across t = 45..60 while the
     no-evidence value tents to 52/105. E1b at n = 8000 reproduces
     the plateau to within about 0.01; E1a reproduces the plateau
     SHAPE but displaced down by its floor-cell bias; E2's bracket
     does not separate plateau from tent at any t in the window --
     its lower endpoint sits below 3/7 - 0.05 across the window.
  R5 No protocol's coverage reaches nominal 0.95 at any floor cell at
     any n run, and the failures are in OPPOSITE directions for E1a
     and E1b.

KILL (observable, frozen before the run).
  All three protocols' stated 95% intervals cover the exact truth at
  the nominal rate (coverage >= 0.90) at every floor cell and at both
  window cells, at every n run. Then standard estimators already
  recover this family's truth and the ruler has no customer. What a
  MISS buys is weighed after the run, not encoded here.

FINDINGS (tier-labeled; run record below; the kill did not fire, and
it did not come close -- coverage failures reach 0.00 against a
nominal 0.95).

1. THE RULER HAS A CUSTOMER (computed; the whole grid). At no cell
   do all three protocols hold nominal coverage ACROSS ALL FOUR
   sample sizes -- the scope matters, since at individual (cell, n)
   slices they often all do (FLOOR-ODD at n = 8000 is 1.00/0.95/
   1.00). Every cell breaks at least one protocol at some n, and the
   breakage is INVISIBLE from inside the estimator: each protocol's
   stated 95% interval is computed the same way whether it is right
   or wrong, and only the closed form says which. The kill required
   coverage >= 0.90 at every cell AND every n; the observed floor
   is 0.00.

2. THE FAILURE IS A MAP, NOT A VERDICT (computed). Which of the two
   POINT protocols fails is CELL-DEPENDENT and the ordering inverts
   across cells, so neither of them is simply the good one. (E2 is
   not the exception this needs: it covers at every cell and every n
   in the grid, 0.90-1.00, and pays for it by certifying nothing --
   finding 6. Coverage alone does not rank these three, which is
   why the map has two axes and not one. AND E2's FLOOR-KNIFE
   COLUMN IS NOT EVIDENCE: the bracket's upper end is capped at 1/2,
   which is legitimate -- a binary Bayes error cannot exceed it --
   but the truth at that cell IS exactly 1/2, so the interval covers
   almost by construction there and the printed 0.95-1.00 measures
   the cap rather than the estimator. At every other cell the
   binding end is the LOWER one and the coverage is real.)
     FLOOR-KNIFE (eta_r = 1/2 exactly): E1a covers 0.00/0.03/0.03/
       0.00 across the four n; E1b covers 0.93-0.97; E2 0.95-1.00.
     FLOOR-ODD (eta_r = 4/7, M = 15): E1b covers 0.70/0.72 at the
       two small n; E1a covers 0.90-1.00; E2 0.90-1.00.
     FLOOR-WIDE (eta_r = 6/11, M = 105): E1a covers 0.00/0.00/0.30
       and only recovers at n = 32000; E1b covers 0.90/0.50/0.25/
       0.15; E2 0.97-1.00.
     THE TWO WINDOW CELLS track FLOOR-ODD, which is why the map is
       not only about floor cells: E1b covers 0.72/0.78/0.88/0.95 at
       WINDOW-EDGE and 0.65/0.70/0.95/0.93 at WINDOW-PEAK, while E1a
       and E2 stay within 0.90-1.00 at both. An interior cell is no
       harder for these protocols than a floor cell of the same M
       and c -- what the window moves is the naive BASELINE, not
       what the estimators do.
   A practitioner who validated a Bayes-error pipeline on any one of
   these cells would carry the wrong conclusion to the next.

3. THE RESUBSTITUTION INTERVAL IS INCONSISTENT AT A KNIFE CELL
   (observation, derived closed form + confirmed at four n). Where
   every eta_r = 1/2 exactly, E1a's per-cell deficit is the mean
   absolute deviation of a fair binomial, (1/2)sqrt(2M/(pi n)),
   while its own half-bar is Z sqrt(1/(4n)) -- both scale as
   1/sqrt(n), so their RATIO is sqrt(2M/pi)/Z, free of n. Printed:
   the ratio runs -1.48, -1.55, -1.56, -1.59 over n = 500..32000
   against the derived 1.5766. The POINT estimate is consistent
   (bias -0.0644 -> -0.0087); the INTERVAL is not, and coverage
   stays at 0.00-0.03 at every sample size. More data never repairs
   it, which is the opposite of what a shrinking bar advertises.

4. MORE DATA CAN MAKE A HELD-OUT INTERVAL WORSE (computed;
   FLOOR-WIDE E1b). Coverage falls MONOTONICALLY as n grows --
   0.90, 0.50, 0.25, 0.15 on the grid -- because the bias shrinks
   slower than the bar: bias/half-bar climbs +0.48, +0.99, +1.51,
   +1.63. ROBUST, and the robustness leg is here because the
   tie-break is arbitrary and NOT neutral: at this cell the label-1
   rate is 630/1155 while R* = 5/11, so guessing 1 on an untrained
   cell scores exactly R* by coincidence, and the grid's tie->one is
   therefore the FRIENDLIEST of the three choices. All three fall
   monotonically -- tie->one 0.90/0.62/0.25/0.07, tie->zero
   0.65/0.38/0.12/0.03, tie->coin 0.78/0.45/0.25/0.10 -- and the two
   harsher ones fall further and start lower. Read the DIRECTION as
   the finding and not the rates: the leg's tie->one series differs
   from the grid's at two of four n (0.62 against 0.50, 0.07 against
   0.15) purely by rng stream, which is the honest scale of 40-trial
   coverage noise. The
   estimator is scoring a fitted RULE, whose excess over the optimum
   decays with the flip probability of 105 near-half cells, while
   its reported precision decays as 1/sqrt(n). This is the single
   row of the run that no ground-truth-free protocol could produce:
   without the closed form, the tightening interval reads as
   improving evidence.

5. THE PREDICTED UNBIASED CELL LANDED (computed; R2). E1b is
   biased UP wherever the plug-in rule can flip a cell -- +0.0446
   (FLOOR-ODD) and +0.0296 (FLOOR-WIDE) at n = 500, the predicted
   order of +0.04 -- and is UNBIASED at FLOOR-KNIFE (+0.0118,
   +0.0001, -0.0017, -0.0008), the one cell where eta_r = 1/2
   makes EVERY rule exactly optimal so a flip costs nothing. The
   family's own dial predicted which cell would exempt an
   estimator from its characteristic error.

6. THE DISTRIBUTION-FREE BRACKET IS CORRECT AND EMPTY (computed;
   the profile leg). E2 covers everywhere (0.90-1.00), as
   Cover-Hart requires. But across the window its bracket contains
   the NO-EVIDENCE value at 14 of 14 in-window thresholds, and
   contains truth and no-evidence TOGETHER at 14 of 14: it cannot
   certify that the evidence is worth anything at all, on a family
   where the exact answer is a 0.0667 lift. Its width is still
   0.057-0.090 at n = 32000, wider than the whole tent it would
   need to resolve. Correct is not the same as informative, and
   only a ruler separates them.

7. THE PLATEAU IS RECOVERABLE, AND R4's PREDICTED DISPLACEMENT WAS
   WRONG (computed). True R* is flat at 3/7 across t = 46..59 while
   the no-evidence value tents to 52/105. At n = 8000 on the M = 15
   cell BOTH plug-in protocols track the plateau -- max |E1a - R*|
   = 0.0017 and max |E1b - R*| = 0.0026 against a tent reaching
   0.0667 -- across 14 INDEPENDENTLY sampled thresholds, not 14
   views of one draw, so the flatness is 14 agreeing estimates and
   not one sample's shape. The downward displacement predicted for E1a did not
   occur here: E1a's bias is governed by how close eta_r sits to
   1/2 and by M/n, not by floor-ness, and at eta_r = 4/7 with
   n/M = 533 it is negligible. The plateau is thus a CLEAN
   discriminator rather than a universal trap -- it separates the
   protocols that can see a designed lift from the one that cannot
   (finding 6), which is more useful than a cell that breaks all
   three.

8. THE RULER ALSO PRICES E2's OWN ASYMPTOTE (rule, derived +
   confirmed on all five cells). Once n >> M every test point has an
   exact residue match, so 1-NN returns a random same-cell training
   label and R_NN -> sum_r P(r) 2 eta_r (1 - eta_r), a second closed
   form the family hands over: 1/2, 24/49, 24/49, 24/49, 60/121.
   At n = 32000 the measured gaps are +0.0007, +0.0006, +0.0005,
   +0.0007, -0.0005. So the family scores not only an estimator's
   accuracy against the optimum but the estimator's own limiting
   value against ITS closed form -- two rulers from one design.

THE PREDICTION LEDGER (every frozen prediction adjudicated, the
refuted ones included -- a findings section that reports only the
hits is not a record).
  R1 SPLIT. The FLOOR-WIDE coverage clause is confirmed and then
     some (0.00 at both small n, predicted "below 0.5"). The
     cross-cell clause is confirmed at n = 500 and 2000 (deficit
     0.1362 vs 0.0644, 0.0525 vs 0.0338) and REFUTED at n = 8000
     and 32000, where FLOOR-WIDE's deficit is the SMALLER one
     (0.0129 vs 0.0171, 0.0008 vs 0.0087). The prediction assumed
     sqrt(M/n) governs throughout; it governs only while cells are
     SPARSE. Once they are populated the distance of eta_r from 1/2
     takes over, and that decays with the flip probability rather
     than as a square root -- so FLOOR-WIDE (eta = 6/11) escapes
     while FLOOR-KNIFE (eta = 1/2 exactly) cannot, which is finding
     3 arriving from the other side. Also strictly, "biased DOWN at
     every floor cell at every n" fails at one slice: FLOOR-ODD at
     n = 32000 prints +0.0001, inside its own noise.
  R2 CONFIRMED, including the half that was not obvious (the
     FLOOR-KNIFE exemption) -- finding 5.
  R3 SPLIT. Coverage clause confirmed (0.90-1.00 everywhere, though
     see finding 2 on the knife cell's cap). Width clause REFUTED:
     widths run 0.057-0.190, never above 0.2. The operative claim
     survives in a stronger printed form -- the bracket contains the
     no-evidence value at 14 of 14 in-window thresholds (finding 6)
     -- but the number predicted was wrong.
  R4 SPLIT. The plateau is reproduced, and better than predicted
     (0.0017 and 0.0026 against "about 0.01"). Both other clauses
     REFUTED: E1a shows no downward displacement here (finding 7),
     and E2's lower endpoint sits at 0.385-0.395, above the
     predicted 3/7 - 0.05 = 0.3786. E2's failure to separate
     plateau from tent is real but for a reason the prediction
     named wrongly -- the bracket is too wide at the TOP, not too
     low at the bottom.
  R5 REFUTED outright. At every floor cell at least one protocol
     reaches nominal: E1b 0.93-0.97 at FLOOR-KNIFE, E1a 0.90-1.00
     at FLOOR-ODD, E2 throughout. The opposite-directions clause
     holds (E1a down, E1b up) but the coverage clause was simply
     too strong, and finding 2's map is what the run supports
     instead.

WHAT THE MISS BUYS, weighed after the run and not encoded in the
slate. The ceiling hunt's graduation verdict rests on
NON-COINCIDENCE: the edge is exactness on designed families, and
field-scale value needs an ESTIMATION move that voids the edge.
Findings 3 and 4 say the estimation move is not merely a different
regime -- it is a regime whose standard intervals are wrong in ways
that MORE DATA does not fix and that no ground-truth-free protocol
can detect. That does not overturn the verdict, and this file does
not claim it does: the instances remain toy-scale, and nothing here
builds a field-scale artifact. What it does is convert the verdict's
premise into a measured one. The hole is narrow and stated: the
argument treats "incumbents estimate" as a reason exactness has no
customer, where the measurement says estimation is exactly where a
customer for exactness lives.

HONEST LIMITS. (a) Five cells chosen from the dial, not scanned --
the grid is a designed probe, not a census, and the coverage
numbers are 40-trial estimates (a nominal 0.95 reads as 0.90-1.00
at that trial count, which is why only the gross failures are
read; the robustness leg measures that noise directly at 0.12
between two streams of the same setting, so no coverage rate here
should be read to better than about a tenth). (b) One seed, with
the tie-break varied three ways at the one cell where the choice
was shown to matter. (c) Three protocols, all elementary; the
divergence- and MST-based estimators are untouched and are the
obvious next rung. (d) 0-1 score only. (e) Uniform prior only --
the tilt dial of explore_ceiling_dials.py is a live axis here and
was not run. (f) Finding 3's closed form is asymptotic (the
binomial mean absolute deviation), which is why it is filed as an
observation confirmed at four n rather than as a rule.

RUN RECORD (this file, python explore_ceiling_ruler.py, ~8 s):
  K1 truth control: fiber-count = closed form on all 35 (cell, t)
     slices -- pass.
  K0 positive control: two-cell Bernoulli, eta = (0.2, 0.9),
     R* = 3/20, n = 8000 -- E1a bias +0.0001 coverage 0.93; E1b
     bias -0.0002 coverage 0.95; E2 coverage 1.00 with bracket
     [0.1368, 0.2629] excluding the no-evidence 0.45 -- pass.
  K2 sampler control: N = 1155, n = 200000, worst cell deviation
     3.36 SE, label rate 0.54609 vs exact 0.54545 (0.57 SE) -- pass.
  grid: 5 cells x 4 sample sizes x 40 trials, printed above.
  knife constant: sqrt(2M/pi)/Z = 1.5766 against -1.48/-1.55/
     -1.56/-1.59.
  profile: 30 thresholds at n = 8000, 40 trials; plateau summary
     max |E1a - R*| = 0.0017, max |E1b - R*| = 0.0026, tent 0.0667;
     E2 brackets the no-evidence value at 14 of 14 in-window
     thresholds.
  robustness: E1b at FLOOR-WIDE under three tie-breaks, all
     monotone -- one 0.90/0.62/0.25/0.07, zero 0.65/0.38/0.12/0.03,
     coin 0.78/0.45/0.25/0.10.
  all controls green.

RUN: python explore_ceiling_ruler.py
  (bounded: 5 cells x 4 sample sizes x 40 trials plus one profile
  leg that re-uses its draws; pure Python, no BLAS, well under the
  512 MB ceiling; estimated 2-4 minutes, measured ~8 s.)
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
from fractions import Fraction
from math import sqrt

Z = 1.96                      # the 95% normal bar a practitioner reports
TRIALS = 40
NS = (500, 2000, 8000, 32000)
SEED = 20260729
PROFILE_N = 8000
PROFILE_TRIALS = 40
PROFILE_TS = range(38, 68)


def product(xs):
    out = 1
    for x in xs:
        out *= x
    return out


# ---------------- the family: exact truth ----------------

def threshold_ceiling(N, M, t):
    """The proved closed form (explore_ceiling_anatomy.py finding 1)."""
    c = N // M
    q, s = divmod(t, M)
    if c % 2 == 1 and q == (c - 1) // 2 and s != 0:
        return Fraction(c + 1, 2 * c)
    return Fraction(max(t, N - t), N)


def bayes_error(N, M, t):
    return 1 - threshold_ceiling(N, M, t)


def bayes_error_brute(N, M, t):
    """K1: the same quantity by direct fiber count, no closed form."""
    c = N // M
    wrong = 0
    for r in range(M):
        below = sum(1 for j in range(c) if r + j * M < t)
        wrong += min(below, c - below)
    return Fraction(wrong, N)


def no_evidence_error(N, t):
    return Fraction(min(t, N - t), N)


def nn_asymptote(N, M, t):
    """The exact value 1-NN converges to once every test point has an
    exact residue match in training: sum_r P(r) 2 eta_r (1 - eta_r),
    with eta_r = (c - B(r))/c. A second closed form the family hands
    over -- the ruler prices E2's own asymptote, not just R*."""
    c = N // M
    q, s = divmod(t, M)
    tot = Fraction(0)
    for r in range(M):
        b = q + (1 if r < s else 0)
        tot += Fraction(2 * b * (c - b), c * c)
    return tot / M


# ---------------- the sampler (the one new piece) ----------------

class ThresholdSampler:
    """Draw x uniform from Z/N; the estimator sees the residue tuple
    (x mod p) for p in S, and the label [x >= t]."""

    def __init__(self, N, subset):
        self.N = N
        self.subset = subset
        self.M = product(subset)
        self.cells = self.M

    def draw(self, rng, n):
        return [rng.randrange(self.N) for _ in range(n)]

    def cell(self, x):
        """The CRT cell index -- x mod M, which the residue tuple
        determines and the estimator may reconstruct."""
        return x % self.M

    def coords(self, r):
        return tuple(r % p for p in self.subset)

    def label(self, x, t):
        return 1 if x >= t else 0


class BernoulliSampler:
    """K0's positive control, behind the same interface: two
    equiprobable cells with posteriors etas, so R* is closed-form."""

    def __init__(self, etas):
        self.etas = etas
        self.M = len(etas)
        self.cells = self.M

    def draw(self, rng, n):
        return [(rng.randrange(self.M), rng.random()) for _ in range(n)]

    def cell(self, x):
        return x[0]

    def coords(self, r):
        return (r,)

    def label(self, x, t):
        return 1 if x[1] < self.etas[x[0]] else 0


# ---------------- the estimators ----------------

def binom_bar(rhat, n):
    return Z * sqrt(max(rhat * (1 - rhat), 0.0) / n)


def est_resub(cells, labels, M, rng):
    """E1a: the plug-in histogram estimator, resubstitution."""
    n = len(cells)
    c1 = [0] * M
    c0 = [0] * M
    for r, y in zip(cells, labels):
        if y:
            c1[r] += 1
        else:
            c0[r] += 1
    minority = sum(min(a, b) for a, b in zip(c0, c1))
    rhat = minority / n
    bar = binom_bar(rhat, n)
    return rhat, rhat - bar, rhat + bar


def _split(cells, labels):
    h = len(cells) // 2
    return cells[:h], labels[:h], cells[h:], labels[h:]


def est_heldout(cells, labels, M, rng, tie="one"):
    """E1b: the plug-in majority rule fitted on half, scored on half.

    TIE-BREAK. A cell whose training counts are equal -- an EMPTY cell
    included, which is the common case when n/M is small -- has no
    majority, and the choice is arbitrary. It is also not neutral: at
    FLOOR-WIDE the label-1 rate is 630/1155 and R* = 5/11, so always
    guessing 1 on an untrained cell scores exactly R* by coincidence
    of that cell's own arithmetic. The `tie` argument exists so the
    robustness leg can show which conclusions survive the choice.
    """
    trc, trl, tec, tel = _split(cells, labels)
    c1 = [0] * M
    c0 = [0] * M
    for r, y in zip(trc, trl):
        if y:
            c1[r] += 1
        else:
            c0[r] += 1
    if tie == "one":
        rule = [1 if c1[r] >= c0[r] else 0 for r in range(M)]
    elif tie == "zero":
        rule = [1 if c1[r] > c0[r] else 0 for r in range(M)]
    elif tie == "coin":
        rule = [(1 if c1[r] > c0[r] else 0) if c1[r] != c0[r]
                else rng.randrange(2) for r in range(M)]
    else:
        raise ValueError(tie)
    err = sum(1 for r, y in zip(tec, tel) if rule[r] != y)
    nte = len(tec)
    rhat = err / nte
    bar = binom_bar(rhat, nte)
    return rhat, rhat - bar, rhat + bar


def _cell_distance_table(sampler, M):
    coords = [sampler.coords(r) for r in range(M)]
    tab = []
    for a in range(M):
        ca = coords[a]
        tab.append([sum(1 for u, v in zip(ca, coords[b]) if u != v)
                    for b in range(M)])
    return tab


def est_covhart(cells, labels, M, rng, dist):
    """E2: 1-NN error under Hamming distance on the residue tuple,
    mapped through the Cover-Hart bracket. The nearest-neighbour set
    is resolved exactly through the cell-distance table."""
    trc, trl, tec, tel = _split(cells, labels)
    c1 = [0] * M
    c0 = [0] * M
    for r, y in zip(trc, trl):
        if y:
            c1[r] += 1
        else:
            c0[r] += 1
    occupied = [r for r in range(M) if c0[r] or c1[r]]
    # per test cell: the label-1 share among all training points in
    # the tied nearest occupied cells (exactly uniform over ties)
    w = [None] * M
    for r in range(M):
        row = dist[r]
        best = min(row[o] for o in occupied)
        n1 = sum(c1[o] for o in occupied if row[o] == best)
        n0 = sum(c0[o] for o in occupied if row[o] == best)
        w[r] = n1 / (n1 + n0)
    err = 0
    for r, y in zip(tec, tel):
        pred = 1 if rng.random() < w[r] else 0
        err += pred != y
    nte = len(tec)
    rnn = err / nte
    bar = binom_bar(rnn, nte)
    lo_nn = max(rnn - bar, 0.0)
    hi_nn = min(rnn + bar, 1.0)
    lo = 0.5 * (1 - sqrt(max(1 - 2 * lo_nn, 0.0))) if lo_nn <= 0.5 else 0.5
    # The 1/2 cap is legitimate -- a binary Bayes error cannot exceed
    # it -- but it makes this bracket's coverage near-automatic at a
    # cell whose truth IS 1/2 (findings 2 and 6 say so where the
    # numbers are read).
    hi = min(hi_nn, 0.5)
    if hi < lo:
        hi = lo
    return rnn, lo, hi


PROTOCOLS = ("E1a resub", "E1b held-out", "E2 Cover-Hart")


def run_cell(sampler, t, n, trials, truth, seed, dist):
    """Return per-protocol (mean estimate, bias, coverage, mean width)."""
    rng = random.Random(seed)
    tf = float(truth)
    acc = {p: [0.0, 0, 0.0, 0.0, 0.0] for p in PROTOCOLS}
    # sum(point), covered, sum(width), sum(lo), sum(hi)
    for _ in range(trials):
        xs = sampler.draw(rng, n)
        cells = [sampler.cell(x) for x in xs]
        labels = [sampler.label(x, t) for x in xs]
        M = sampler.M
        run = (
            ("E1a resub", lambda: est_resub(cells, labels, M, rng)),
            ("E1b held-out", lambda: est_heldout(cells, labels, M, rng)),
            ("E2 Cover-Hart",
             lambda: est_covhart(cells, labels, M, rng, dist)),
        )
        for name, fn in run:
            point, lo, hi = fn()
            a = acc[name]
            a[0] += point
            a[1] += lo <= tf <= hi
            a[2] += hi - lo
            a[3] += lo
            a[4] += hi
    out = {}
    for p in PROTOCOLS:
        s, cov, wid, slo, shi = acc[p]
        mean = s / trials
        out[p] = (mean, mean - tf, cov / trials, wid / trials,
                  slo / trials, shi / trials)
    return out


# ---------------- the cells ----------------

CELLS = (
    ("FLOOR-KNIFE", 210, (3, 5), 105),
    ("FLOOR-ODD", 105, (3, 5), 45),
    ("WINDOW-EDGE", 105, (3, 5), 46),
    ("WINDOW-PEAK", 105, (3, 5), 52),
    ("FLOOR-WIDE", 1155, (3, 5, 7), 525),
)


def main():
    # ---- K1: the truth control, before anything is estimated ----
    n_truth = 0
    for _, N, sub, t in CELLS:
        M = product(sub)
        assert bayes_error_brute(N, M, t) == bayes_error(N, M, t), (N, sub, t)
        n_truth += 1
    for t in PROFILE_TS:
        assert bayes_error_brute(105, 15, t) == bayes_error(105, 15, t), t
        n_truth += 1
    print(f"K1 truth control: fiber-count Bayes error = closed form on "
          f"all {n_truth} (cell, t) slices -- pass")

    # ---- K0: the positive control, before any result is read ----
    ctrl = BernoulliSampler((0.2, 0.9))
    ctrl_truth = Fraction(15, 100)
    cdist = _cell_distance_table(ctrl, ctrl.M)
    cres = run_cell(ctrl, None, 8000, TRIALS, ctrl_truth, SEED, cdist)
    print(f"K0 positive control: two-cell Bernoulli, eta = (0.2, 0.9), "
          f"R* = {ctrl_truth} exactly, n = 8000, {TRIALS} trials")
    ctrl_naive = 0.45   # min(P(y=1), P(y=0)) = min(0.55, 0.45)
    for p in PROTOCOLS:
        mean, bias, cov, wid, lo, hi = cres[p]
        print(f"   {p:<14} mean {mean:.4f}  bias {bias:+.4f}  "
              f"coverage {cov:.2f}  interval [{lo:.4f}, {hi:.4f}] "
              f"width {wid:.4f}")
        assert cov >= 34 / TRIALS, (p, cov)
        if p == "E2 Cover-Hart":
            # informative, not merely correct
            assert hi < ctrl_naive, (p, hi)
        else:
            assert abs(bias) < 0.01, (p, bias)
    print(f"   all three cover; the two point protocols are unbiased and "
          f"the bracket excludes the no-evidence value {ctrl_naive} -- "
          f"pass")

    # ---- K2: the sampler control ----
    rng = random.Random(SEED + 1)
    s = ThresholdSampler(1155, (3, 5, 7))
    xs = s.draw(rng, 200000)
    M = s.M
    counts = [0] * M
    for x in xs:
        counts[s.cell(x)] += 1
    n = len(xs)
    exp = n / M
    se = sqrt(n * (1 / M) * (1 - 1 / M))
    worst = max(abs(v - exp) for v in counts)
    lab = sum(s.label(x, 525) for x in xs) / n
    lab_exact = float(Fraction(1155 - 525, 1155))
    lab_se = sqrt(lab_exact * (1 - lab_exact) / n)
    print(f"K2 sampler control: N = 1155, M = 105, n = {n} -- worst cell "
          f"deviation {worst / se:.2f} SE, label rate {lab:.5f} vs exact "
          f"{lab_exact:.5f} ({abs(lab - lab_exact) / lab_se:.2f} SE)")
    assert worst < 4 * se, worst / se
    assert abs(lab - lab_exact) < 4 * lab_se
    print("   -- pass")

    # ---- the main grid ----
    print()
    print("THE GRID: exact truth vs three standard protocols "
          f"({TRIALS} trials each, nominal coverage 0.95)")
    for name, N, sub, t in CELLS:
        M = product(sub)
        c = N // M
        truth = bayes_error(N, M, t)
        naive = no_evidence_error(N, t)
        sam = ThresholdSampler(N, sub)
        dist = _cell_distance_table(sam, M)
        print()
        asym = nn_asymptote(N, M, t)
        print(f"{name}: N = {N}, S = {sub}, M = {M}, c = {c}, t = {t}; "
              f"R* = {truth} = {float(truth):.4f}, no-evidence "
              f"{naive} = {float(naive):.4f}, 1-NN asymptote "
              f"{asym} = {float(asym):.4f}")
        for n in NS:
            res = run_cell(sam, t, n, TRIALS, truth, SEED + n, dist)
            for p in PROTOCOLS:
                mean, bias, cov, wid, lo, hi = res[p]
                # the bias measured in the estimator's OWN half-bar:
                # a ratio above 1 means the stated interval is
                # systematically on the wrong side of the truth
                ratio = bias / (wid / 2) if wid > 0 else float("nan")
                print(f"   n = {n:>5}  {p:<14} mean {mean:.4f}  "
                      f"bias {bias:+.4f}  bias/half-bar {ratio:+.2f}  "
                      f"coverage {cov:.2f}  interval [{lo:.4f}, "
                      f"{hi:.4f}] width {wid:.4f}")
        # A KNIFE cell has every eta_r = 1/2 exactly (s = 0 and
        # 2q = c). There E1a's deficit per cell is the mean absolute
        # deviation of a fair binomial, (1/2)sqrt(2 M / (pi n)), while
        # its own half-bar is Z sqrt(1/4 n) -- so the ratio of the two
        # is sqrt(2 M / pi) / Z, free of n. Coverage then cannot
        # improve with more data. Printed so the constant is measured
        # against the grid above rather than asserted.
        q0, s0 = divmod(t, M)
        if s0 == 0 and 2 * q0 == c:
            print(f"   knife cell: E1a's bias/half-bar tends to "
                  f"sqrt(2M/pi)/Z = {sqrt(2 * M / 3.141592653589793) / Z:.4f} "
                  f"-- free of n, so its coverage cannot improve with "
                  f"more data")
        big = run_cell(sam, t, NS[-1], TRIALS, truth, SEED + NS[-1], dist)
        nn_mean = big["E2 Cover-Hart"][0]
        print(f"   1-NN point estimate at n = {NS[-1]}: {nn_mean:.4f} vs "
              f"the exact asymptote {float(asym):.4f} "
              f"(gap {nn_mean - float(asym):+.4f})")

    # ---- the profile leg ----
    print()
    print(f"THE PROFILE: N = 105, S = (3, 5), M = 15, c = 7, "
          f"t = {PROFILE_TS.start}..{PROFILE_TS.stop - 1}, n = "
          f"{PROFILE_N}, {PROFILE_TRIALS} trials -- the window is "
          f"(45, 60), where R* is flat and the no-evidence value tents")
    sam = ThresholdSampler(105, (3, 5))
    dist = _cell_distance_table(sam, 15)
    print("     t   R*      naive   E1a     E1b     E2 lo   E2 hi   in-win")
    win_rows = []
    for t in PROFILE_TS:
        truth = bayes_error(105, 15, t)
        naive = no_evidence_error(105, t)
        rng2 = random.Random(SEED + 7 * t)
        sums = {p: [0.0, 0.0, 0.0] for p in PROTOCOLS}
        for _ in range(PROFILE_TRIALS):
            xs = sam.draw(rng2, PROFILE_N)
            cells = [sam.cell(x) for x in xs]
            labels = [sam.label(x, t) for x in xs]
            prof = (
                ("E1a resub", lambda: est_resub(cells, labels, 15, rng2)),
                ("E1b held-out",
                 lambda: est_heldout(cells, labels, 15, rng2)),
                ("E2 Cover-Hart",
                 lambda: est_covhart(cells, labels, 15, rng2, dist)),
            )
            for nm, fn in prof:
                pt, lo, hi = fn()
                sums[nm][0] += pt
                sums[nm][1] += lo
                sums[nm][2] += hi
        q, ss = divmod(t, 15)
        inwin = "yes" if (q == 3 and ss != 0) else "no"
        e1a = sums["E1a resub"][0] / PROFILE_TRIALS
        e1b = sums["E1b held-out"][0] / PROFILE_TRIALS
        e2lo = sums["E2 Cover-Hart"][1] / PROFILE_TRIALS
        e2hi = sums["E2 Cover-Hart"][2] / PROFILE_TRIALS
        print(f"   {t:>3}  {float(truth):.4f}  {float(naive):.4f}  "
              f"{e1a:.4f}  {e1b:.4f}  {e2lo:.4f}  {e2hi:.4f}  {inwin}")
        if inwin == "yes":
            win_rows.append((float(truth), float(naive), e1a, e1b,
                             e2lo, e2hi))

    # the plateau summary: can a protocol tell the flat truth from the
    # tented no-evidence value across the window?
    m1a = max(abs(a - tr) for tr, _, a, _, _, _ in win_rows)
    m1b = max(abs(b - tr) for tr, _, _, b, _, _ in win_rows)
    n_naive_in = sum(1 for _, nv, _, _, lo, hi in win_rows if lo <= nv <= hi)
    n_both_in = sum(1 for tr, nv, _, _, lo, hi in win_rows
                    if lo <= nv <= hi and lo <= tr <= hi)
    max_tent = max(nv - tr for tr, nv, _, _, _, _ in win_rows)
    print(f"   plateau summary over the {len(win_rows)} in-window "
          f"thresholds: max |E1a - R*| = {m1a:.4f}, max |E1b - R*| = "
          f"{m1b:.4f}; the tent it must not follow reaches "
          f"{max_tent:.4f}")
    print(f"   E2's bracket contains the NO-EVIDENCE value at "
          f"{n_naive_in} of {len(win_rows)} in-window thresholds, and "
          f"contains truth and no-evidence together at {n_both_in} "
          f"-- where it does, it certifies no lift at all")

    # ---- the robustness leg: does the held-out coverage series
    # survive the arbitrary tie-break? ----
    print()
    print("ROBUSTNESS: E1b's coverage series at FLOOR-WIDE under all "
          "three tie-breaks (the arbitrary choice is not neutral -- "
          "guessing 1 on an untrained cell scores exactly R* there)")
    sam = ThresholdSampler(1155, (3, 5, 7))
    dist = _cell_distance_table(sam, 105)
    truth = bayes_error(1155, 105, 525)
    tf = float(truth)
    for tie in ("one", "zero", "coin"):
        row = []
        for n in NS:
            rng3 = random.Random(SEED + n)
            cov = 0
            bsum = 0.0
            for _ in range(TRIALS):
                xs = sam.draw(rng3, n)
                cs = [sam.cell(x) for x in xs]
                ls = [sam.label(x, 525) for x in xs]
                pt, lo, hi = est_heldout(cs, ls, 105, rng3, tie=tie)
                cov += lo <= tf <= hi
                bsum += pt
            row.append((n, cov / TRIALS, bsum / TRIALS - tf))
        cells_txt = "  ".join(f"n={n}: cov {c:.2f} bias {b:+.4f}"
                              for n, c, b in row)
        print(f"   tie->{tie:<5} {cells_txt}")

    print()
    print("all controls green")


if __name__ == "__main__":
    main()
