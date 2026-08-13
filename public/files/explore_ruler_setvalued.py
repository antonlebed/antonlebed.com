"""explore_ruler_setvalued.py -- THE SET-VALUED READ: SCORING CONFORMAL
PREDICTION SETS AGAINST A DERIVED ORACLE (the eval-ceiling corpus as a
ruler for a SET-valued instrument rather than a point one; sibling of
explore_ceiling_ruler.py and explore_ruler_divergence.py, whose grid and
scoring discipline this file inherits).

THE QUESTION. Every instrument the ceiling ruler has scored estimates a
NUMBER -- a Bayes error, a deletion posterior -- and is scored on bias
and on the coverage of its own stated interval. A conformal predictor
returns a SET instead, and it is sold on a coverage guarantee that is
not in question: it holds by construction, under exchangeability alone.
So coverage cannot rank two of them, and the property that can --
INFORMATIVENESS, how small the set is -- has no reference point on
natural data, because the optimal set is unknown there. On these
families it is derived. So: what does a distribution-free guarantee
cost in set size against the exact optimum, and does the loss
concentrate where the family's dial says the task is hard?

THE GATE, ANSWERED FIRST (a dial that PLACES an optimal set, or no
instrument). The corpus's instances ask a single archimedean BIT, and
over two labels a prediction set lives in the four-element lattice
{}, {0}, {1}, {0,1} -- set size takes the values 1 and 2 and the only
informativeness observable is the fraction of atoms carrying a
singleton, which is one bit of resolution. The read that is
non-degenerate is the same family at k labels: the k-ary archimedean
magnitude class

    Y = floor(k x / N),

which is the sign bit at k = 2 and is otherwise the family's unopened
non-binary anatomy. Its dial is derived in the HAND DERIVATION below:
the class blocks are a Sturmian pattern whose density is (c mod k)/k
and whose PHASE is the atom r/M, so the optimal set's identity moves
with the observable while its size is a closed form. The fiber-index
read Y = j was considered and rejected at the gate: under the uniform
prior j is independent of r, and under the geometric tilt the r factor
cancels, so its posterior is the same at every atom and there is no
conditional object to measure.

INCUMBENT CONTACT (full text, before any engine).
  - Barber, Candes, Ramdas and Tibshirani, "The limits of
    distribution-free conditional predictive inference": the
    impossibility of approximate conditional coverage is stated "for
    all distributions P where the marginal distribution P_X has no
    atoms", and the exact version concludes only "at almost all points
    x aside from the atoms of P_X".
  - Vovk, "Conditional validity of inductive conformal predictors",
    Proposition 4, carries the same non-atom hypothesis and then says
    what the exclusion means: "Of course, the condition that x be a
    non-atom is essential: if P_X({x}) > 0, an inductive conformal
    predictor that ignores all examples with objects different from x
    will have 1-eps object conditional validity and can give narrow
    predictions if the training set is big enough to contain many
    examples with x as their object."
    THE HYPOTHESIS DOES NOT BIND HERE. The observable is r = x mod M:
    M atoms of mass exactly 1/M under the uniform prior, and the
    per-atom sample grows with n. So per-atom conditional coverage is
    ATTAINABLE, the conditional comparison is legitimate rather than a
    comparison against an impossibility, and the rival that collects it
    is the Mondrian predictor with the taxonomy K = the residue itself,
    whose guarantee is that paper's Proposition 3 (error probability
    given the CATEGORY does not exceed eps).
  - Sadinle, Lei and Wasserman, "Least ambiguous set-valued classifiers
    with bounded error levels": ambiguity is E|H(X)|, and the
    ambiguity-minimizing classifier subject to the MARGINAL constraint
    P{Y in H(X)} >= 1-alpha is the thresholded posterior
    H* = {(x,y) : p(y|x) >= t_alpha}. The oracle scored here is that
    object, not an invention of this file; what these families add is
    that p(y|x) is an exact Fraction, so the threshold and the set are
    derived rather than plugged in.
  - Vovk, Fedorova, Nouretdinov and Gammerman, "Criteria of efficiency
    for conformal prediction": the field's own size criteria are the N
    criterion, the average |Gamma_i|, and the E criterion, "the average
    amount the size of the prediction set exceeds 1 ... as compared
    with the ideal situation of one-element prediction sets", the
    formula (|Gamma_i| - 1)+. Excess is measured over ONE because on
    natural data the optimal size is unknown and one is the only
    defensible stand-in. Wherever the optimum is genuinely larger than a
    singleton, that criterion charges an unavoidable cost as
    inefficiency and cannot separate it from the avoidable kind. Excess
    over the ORACLE is what this file measures instead.

TWO ORACLES, AND SCORING EACH METHOD AGAINST ITS OWN. The marginal and
conditional constraints have different optima and it would be a rigged
comparison to score a marginal method against the conditional one:
  O_marg -- the SLW object: {y : p(y|r) >= t}, t the largest level whose
     marginal coverage is still >= 1-alpha. Minimizes E|H| under the
     marginal constraint.
  O_cond -- per atom, the smallest set whose mass at THAT atom is
     >= 1-alpha. The attainable target, by the Vovk passage above.
Split conformal is scored against O_marg, Mondrian against O_cond. And
the gap E|O_cond| - E|O_marg| is itself an observable this file can
print exactly and nobody can print on natural data: THE DERIVED PRICE
OF CONDITIONAL COVERAGE on the family.

THE METHODS (each under its own standard hygiene, both on the LAC
score s = 1 - phat(y | r), the score SLW's Theorem 1 makes optimal).
  M1 SPLIT CONFORMAL: fit phat on a training half, take the
     ceil((n_cal+1)(1-alpha))-th smallest calibration score as one
     global qhat, predict {y : phat(y|r) >= 1 - qhat}. Marginal
     guarantee.
  M2 MONDRIAN CONFORMAL, taxonomy = the atom: the same score and the
     same phat, but the quantile taken WITHIN each atom's calibration
     subsample; where ceil((n_r+1)(1-alpha)) exceeds n_r the set is all
     labels, which is the standard convention and the honest one.
     Conditional guarantee.
  Empty training atoms fall back to the pooled label frequencies. The
  choice is arbitrary and is stated because the point ruler found such
  a tie-break can move a result; at these sample sizes every atom is
  expected to be populated, and the rig prints how often the fallback
  fired.

WHY COVERAGE NEEDS NO TEST SET HERE. The true posterior is an exact
Fraction, so a produced set's coverage is computed EXACTLY as the sum
of the true masses of the labels in it -- conditionally at each atom and
marginally by weighting with the exact P(r). No Monte-Carlo test split,
no test-set noise in the quantity the guarantee is about. That is the
ruler doing the one thing a natural-data benchmark cannot.

THE ONE PIECE OF NEW CODE, named in advance: the k-ARY LABEL and the
TILTED SAMPLER. explore_ceiling_ruler.py samples uniform x and labels
with a binary threshold; this file samples x with P(x) proportional to
theta^x and labels with the magnitude class. Everything else -- the
exact posterior, the oracle sets, the conformal machinery -- is written
here for the first time but is closed-form or textbook, not new
mathematics.

DESIGN. Four cells, chosen from the dial and NOT from a scan, at
n in {2000, 8000, 32000}, TRIALS = 40, alpha = 0.30 throughout, one
fixed seed per (cell, n, trial). alpha = 0.30 is frozen because it is
the level at which the uniform-prior oracle is INTERIOR at every cell
here (neither a singleton nor the full label set), which is the only
regime in which a size comparison carries information.

  cell        N     S        M    c    k   theta    what it is
  TILT-3      105   (3,5)    15   7    3   24/25    LIVE: c mod k = 1,
                                                    tilted, so the atoms
                                                    differ in profile
  FLAT-3      105   (3,5)    15   7    3   1        the same cell with
                                                    the tilt off: every
                                                    atom carries the same
                                                    mass MULTISET, so
                                                    there is no
                                                    conditional structure
                                                    to lose and any excess
                                                    is estimation noise
  DEAD-7      105   (3,5)    15   7    7   1        k | c: the posterior
                                                    is exactly flat at
                                                    every atom, the k-ary
                                                    sibling of the
                                                    anatomy's parity
                                                    deadness
  TILT-4-WIDE 1155  (3,5,7)  105  11   4   199/200  LIVE at 105 atoms and
                                                    c mod k = 3, so three
                                                    classes carry the big
                                                    block

FLAT-3 is the differential control the design turns on: excess there is
what estimation noise alone buys, and only excess at TILT-3 ABOVE that
is a conditional cost. Reporting TILT-3 alone would confound the two.

PREDICTIONS, fixed before the engine.
  P1 At TILT-3 and TILT-4-WIDE the exact oracle sizes VARY across atoms;
     at FLAT-3 and DEAD-7 they do not. (Derived, so this is really
     control K1's business -- it is listed here because the whole design
     rests on it.)
  P2 Split conformal's set is a GLOBAL level set of phat while O_cond is
     a per-atom cumulative rule. These coincide only where the crossing
     level is the same at every atom, which the tilt breaks. So at the
     tilted cells split conformal's per-atom coverage spreads around
     1-alpha -- over at the easy atoms, under at the hard ones -- while
     its marginal coverage holds.
  P3 Mondrian tracks O_cond's per-atom size but pays variance: with
     n/(2M) calibration points per atom its threshold is noisy, so its
     median excess is 0 and its max excess is positive, and the excess
     falls with n.
  P4 The derived price of conditional coverage E|O_cond| - E|O_marg| is
     strictly positive at the tilted cells and zero at FLAT-3 and
     DEAD-7, where every atom has the same profile and the two optima
     coincide.
  P5 Split conformal's excess over ITS OWN oracle O_marg is positive at
     the tilted cells and larger than at FLAT-3 at the same n.

KILL-SHAPE, an observable and not an inference, and it rides the
CONDITIONAL basis the Vovk hypothesis selected: if per-atom set-size
excess over the method's own oracle prints median AND max of 0 at every
non-degenerate cell (TILT-3 and TILT-4-WIDE) for BOTH methods, there is
nothing here for a ruler to separate and the question is closed on this
family rather than re-asked on another one.

CONTROLS (run and asserted before any estimate is read).
  K0 THE POSITIVE CONTROL: a bare categorical problem with no ring
     anywhere -- three atoms of equal probability with hand-set
     posteriors (0.8, 0.15, 0.05), (0.5, 0.3, 0.2) and
     (0.34, 0.33, 0.33) -- carried through the SAME sampler interface
     and the SAME estimator code. At alpha = 0.30 the conditional
     oracle sizes are 1, 2 and 3, all three distinct, so a method that
     tracks the atom is visibly different from one that does not. At
     n = 32000 Mondrian's median per-atom excess over O_cond must be 0
     and its max at most 1, and both methods' exact marginal coverage
     must be at least 1 - alpha - 0.02. This is the run where the
     machinery is KNOWN to work; nothing else is read until it passes.
  K1 THE TRUTH CONTROL: at every (cell, atom) the closed-form class mass
     (q^lo - q^hi)/(1 - q^c) must equal a direct count/sum over the
     fiber, in exact Fractions; and the per-atom masses must sum to 1.
  K2 THE SAMPLER CONTROL: at the largest n the pooled empirical atom
     frequency must match the exact P(r) and the pooled empirical label
     frequency the exact P(Y = y), both within 4 binomial standard
     errors.
  K3 THE DEGENERACY CONTROL: at DEAD-7 the exact posterior must be
     exactly flat (every mass 1/7) at every atom -- the divisibility
     deadness the gate derived -- and O_cond's size must be constant.

HAND DERIVATION (fixed before the engine; the index convention
re-derived from explore_ceiling_ruler.py rather than recalled).

x in {0..N-1}, r = x mod M, fiber {r + jM : j = 0..c-1}. The map
(r, j) -> r + jM is a bijection onto {0..N-1}: r <= M-1 and j <= c-1
give r + jM <= cM - 1 = N - 1.

Prior P(x) proportional to theta^x. Then

    P(j | r) proportional to theta^(r + jM) proportional to q^j,
    q := theta^M,

the theta^r factor cancelling -- so the posterior over the fiber INDEX
is a truncated geometric with ratio q, the same at every atom. That is
what kills the fiber-index read at the gate, and it is also what makes
the k-ary read work: the label is a function of x and not of j alone.

Y = floor(kx/N) is increasing in j at fixed r, so each class occupies a
CONTIGUOUS block of j. Writing the block of class y as [lo_y, hi_y),

    P(Y = y | r) = (q^lo_y - q^hi_y) / (1 - q^c)        (q != 1)
                 = (hi_y - lo_y) / c                    (q = 1).

The blocks depend on (r, k, c, M) and NOT on theta: the tilt reweights
the blocks, it does not move them. Under q = 1, writing c = ak + b with
0 <= b < k, the block lengths are

    n_y = a + [ ceil((y+1)b/k - f) - ceil(yb/k - f) ],   f := r/M,

so exactly b = c mod k classes carry a+1 and the rest carry a, at every
atom, and WHICH ones is the Sturmian word of density b/k at phase f.
Hence: b = 0 (k | c) is the DEAD cell, exactly flat; b >= 1 with q = 1
gives every atom the same mass MULTISET so the conditional and marginal
optima coincide; and q != 1 makes the masses themselves atom-dependent,
which is the live regime.

The uniform-prior 0-1 Bayes error is 1 - ceil(c/k)/c, which for c >> k
sits just above the no-evidence floor 1 - ceil(N/k)/N: the POINT read is
nearly worthless on these cells while the SET read is not, which is this
file's sentence in miniature.

RESOURCE ENVELOPE. Pure Python integers, Fractions and lists; no numpy
and no BLAS arenas. Peak footprint is one sample of at most 32000
(atom, label) pairs, far under the 512MB default. 4 cells x 3 sample
sizes x 40 trials, each trial linear in n: estimated well under 5
minutes, no ceremony required.

RUN RECORD (post-run edit; printed output copied, slate above UNCHANGED
-- where a prediction was wrong or an object was misnamed, the
correction is here and the frozen text is left standing).

Run: 4 cells x 3 sample sizes x 40 trials, wall 3.0s, peak working set
21.3 MB against the 512 MB default (memwatch). All four controls passed
before any result was read: K0 oracle sizes [1, 2, 3] with Mondrian
median/max excess 0/0, K1 closed form == fiber sum in exact Fractions at
every atom of every cell, K2 atom and label frequencies within 4 SE, K3
DEAD-7 exactly flat with constant oracle size 5. The empty-atom fallback
never fired.

  cell         O_cond sizes  E|O_cond|   O_marg sizes  E|O_marg|  cov
  TILT-3       [1]           1.0000      [1]           1.0000     .7710
  FLAT-3       [2]           2.0000      [3]           3.0000     1.000
  DEAD-7       [5]           5.0000      [7]           7.0000     1.000
  TILT-4-WIDE  [1, 2]        1.2010      [1]           1.0000     .7675

  per-atom excess over the method's OWN oracle, and EXACT coverage
  (split | mondrian); med/max/mean over 40 trials x all atoms
  cell           n | SPLIT med max  mean  | MOND med max  mean  |
  TILT-3      2000 |   0    0   -0.0783   |   0    2   0.2967  |
  TILT-3      8000 |   0    0   -0.0717   |   0    1   0.2267  |
  TILT-3     32000 |   0    0   -0.0683   |   0    1   0.0700  |
  FLAT-3      2000 |  -1    0   -1.0000   |   1    1   0.5167  |
  FLAT-3      8000 |  -1    0   -1.0133   |   0    1   0.3333  |
  FLAT-3     32000 |  -1    0   -1.0017   |   0    1   0.1917  |
  DEAD-7      2000 |  -2    0   -2.0517   |   1    2   0.6883  |
  DEAD-7      8000 |  -2    0   -2.0650   |   0    2   0.4300  |
  DEAD-7     32000 |  -2    0   -2.0483   |   0    2   0.2633  |
  TILT-4-W    2000 |   0    1   -0.0836   |   0    3   0.5207  |
  TILT-4-W    8000 |   0    0   -0.1145   |   0    3   0.0374  |
  TILT-4-W   32000 |   0    0   -0.1250   |   0    1  -0.0229  |

  exact marginal coverage / exact WORST-ATOM conditional coverage
  cell           n | split marg  split min | mond marg  mond min
  TILT-3      2000 |   0.7212     0.0000   |  0.8319     0.7160
  TILT-3      8000 |   0.7265     0.0000   |  0.8181     0.7160
  TILT-3     32000 |   0.7272     0.0000   |  0.7848     0.7160
  FLAT-3      2000 |   0.7126     0.2857   |  0.8619     0.7143
  FLAT-3      8000 |   0.7105     0.4286   |  0.8095     0.7143
  FLAT-3     32000 |   0.7138     0.4286   |  0.7690     0.7143
  DEAD-7      2000 |   0.7069     0.2857   |  0.8126     0.5714
  DEAD-7      8000 |   0.7050     0.4286   |  0.7757     0.7143
  DEAD-7     32000 |   0.7074     0.2857   |  0.7519     0.7143
  TILT-4-W    2000 |   0.7071     0.0000   |  0.8667     0.6530
  TILT-4-W    8000 |   0.7043     0.0000   |  0.8252     0.6530
  TILT-4-W   32000 |   0.7011     0.0000   |  0.8180     0.6530

KILL-SHAPE: MISSED, on the basis frozen. Per-atom size excess over the
method's own oracle does NOT print median AND max of 0 for both methods
at either live cell: Mondrian's max excess is 1 or more at every sample
size at TILT-3 and at TILT-4-WIDE. This line of work continues.

WHAT THE RUN SAYS, at the honest tier.

1. THE OBJECT NAMED O_marg IN THE SLATE IS NOT THE MARGINAL OPTIMUM; it
   is the best THRESHOLD set, and prediction P4 is FALSE as stated. The
   tell is in the print: E|O_marg| exceeds E|O_cond| at FLAT-3 (3 against
   2) and at DEAD-7 (7 against 5), so the "price of conditional
   coverage" comes out NEGATIVE, which is impossible -- O_cond meets
   conditional coverage at every atom, hence meets marginal coverage,
   hence is FEASIBLE for the marginal constraint, so the marginal optimum
   can never be larger. What the number actually measures is the cost of
   the FORM: SLW's Theorem 1 makes the thresholded posterior optimal, and
   its optimality argument needs the posterior to have no ties. These
   families are finite rings read through a modulus, so p(y|r) takes
   FINITELY many values with heavy ties -- at FLAT-3 every atom carries
   the multiset {3/7, 2/7, 2/7}, and no threshold on those two values can
   produce a size-2 set, so the best threshold rule jumps from coverage
   3/7 straight to coverage 1 and pays a whole extra label. Observation,
   exact: on these cells the incumbent's optimal FORM is strictly
   suboptimal by 1 label (FLAT-3) and 2 labels (DEAD-7), certified by a
   feasible non-threshold rule the same rig computes.
   THIS IS THE SAME HYPOTHESIS FAILING TWICE, IN OPPOSITE DIRECTIONS.
   Atomicity is what voids the conditional-coverage impossibility
   (Vovk's non-atom clause, quoted above) and it is also what voids
   SLW's optimal form. This line of work was built to check one such
   hypothesis against the family before scoring; the run says the
   discipline was needed twice and the slate only checked once.
   (SUPERSEDED IN ITS SECOND HALF by explore_ruler_barecell.py: the form
   failure is a TIE fact and not an atomicity one -- it reproduces on a
   ring-free cell with a SINGLE atom, where the conditional and marginal
   constraints coincide. The first half stands: atomicity is still what
   makes the conditional comparison legal. What survives of this
   paragraph is that one hypothesis was load-bearing twice, not that
   atomicity was the hypothesis both times. The suboptimality itself,
   and the two numbers below, stand as printed.)
   AND THE PENALTY IS ON THE FORM, NOT ON THE PRACTICE -- the same table
   says so and prediction P5 is FALSE because of it. Split conformal
   thresholds an ESTIMATED posterior, whose ties sampling noise breaks,
   so it is not confined to the level sets of the true one: its mean
   excess over the exact threshold optimum is -1.0000 at FLAT-3 and
   -2.0483 at DEAD-7, reliably SMALLER than the best rule of its own
   form, and negative at the live cells too. So the claim is NOT that a
   deployed conformal predictor pays a label for atomicity. It is that
   the theorem certifying its shape optimal does not hold here, and that
   what rescues the practice is the estimation error the theorem
   idealizes away.

2. THE SEPARATION THE RULER WAS BUILT FOR IS IN THE COVERAGE COLUMN, NOT
   THE SIZE COLUMN. Split conformal holds its marginal guarantee at every
   cell and every n (0.7011 to 0.7272 against a nominal 0.70) while its
   EXACT worst-atom conditional coverage is 0.0000 at both live cells and
   every sample size -- some atom receives a set whose true mass is zero,
   and more data does not repair it. Mondrian on the same draws holds
   0.7160 at TILT-3 (nominal 0.70) and 0.6530 at TILT-4-WIDE. Its worst
   atom is not bounded below by the nominal level and the table above
   shows where it is not: 0.5714 at DEAD-7 at n = 2000, back to 0.7143
   by n = 8000. That is the guarantee behaving as stated -- Mondrian's
   is an expectation over the calibration draw, and DEAD-7 gives each
   atom only about 67 calibration points at that n -- and it is why the
   contrast here is drawn on the SHAPE of the two failures rather than
   on a floor. Two predictors, indistinguishable on the guarantee each
   advertises, differing by everything on the one an auditor cares about;
   and the gap is only visible because the truth is a Fraction rather
   than a held-out estimate. Prediction P2 is CONFIRMED and is stronger
   than it was written: the spread is not merely "over at the easy atoms,
   under at the hard ones" but reaches exactly zero.

3. WHAT MORE DATA BUYS IS ASYMMETRIC. Mondrian's mean excess falls with n
   at every cell (TILT-3: 0.2967, 0.2267, 0.0700; TILT-4-WIDE: 0.5207,
   0.0374, -0.0229), which is P3 confirmed -- it pays variance for the
   conditional guarantee and buys it back with sample. Split conformal's
   worst-atom coverage is 0.0000 at n = 2000 and still 0.0000 at
   n = 32000. The failure is in the FORM, not the sample, which is the
   same shape the point ruler found for held-out plug-in and is the
   second instrument to show it.

4. A DESIGN MISS, NAMED. TILT-3's tilt (theta = 24/25, so q = 0.542) is
   too strong: its conditional oracle is a singleton at EVERY atom, so
   the cell carries no oracle-size variation and only its coverage column
   is informative. TILT-4-WIDE (sizes [1, 2]) is the only cell that
   carries the size structure the gate derived. Any next rung picks the
   tilt so that O_cond's size varies -- a one-line dial on theta, and the
   rig prints the size profile to aim it.

5. WHAT THE FAMILY CONTRIBUTED, on the placement/truth split the point
   ruler established: PLACEMENT and truth, again, not the failure. The
   dial chose cells whose oracle is exactly known and whose atoms differ
   by a derived amount; the failures are properties of the protocols. The
   bare-cell leg that would make that a rule rather than an observation
   is probe 2, and K0 already carries half of it -- the same code on a
   ring-free three-atom problem reproduces the qualitative split (Mondrian
   median excess 0, both methods marginally valid) without any ring.
"""

import os
import random
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

ALPHA = Fraction(3, 10)
TRIALS = 40
SAMPLE_SIZES = (2000, 8000, 32000)
BASE_SEED = 20260808


# ---------------------------------------------------------------- family

class Cell:
    """A k-ary archimedean magnitude-class read on a squarefree ring."""

    def __init__(self, name, primes, read, k, theta):
        self.name = name
        self.N = 1
        for p in primes:
            self.N *= p
        self.M = 1
        for p in read:
            self.M *= p
        assert self.N % self.M == 0
        self.c = self.N // self.M
        self.k = k
        self.theta = Fraction(theta)
        self.q = self.theta ** self.M
        self.primes = primes
        self.read = read

    # --- exact truth -------------------------------------------------

    def blocks(self, r):
        """Class -> [lo, hi) block of fiber indices j, contiguous."""
        out = [None] * self.k
        lo = 0
        for j in range(self.c):
            y = (self.k * (r + j * self.M)) // self.N
            if out[y] is None:
                out[y] = [j, j + 1]
            else:
                out[y][1] = j + 1
        for y in range(self.k):
            if out[y] is None:
                out[y] = [lo, lo]
            lo = out[y][1]
        return out

    # The exact truth is a property of the CELL, not of a trial: it is
    # built once and cached, in Fractions, with float mirrors for the
    # per-trial scoring. Recomputing it per trial is what makes a
    # thousands-of-digits Fraction sum into a runaway.

    def _build_truth(self):
        self._post = [self._posterior_closed(r) for r in range(self.M)]
        den = sum(self.theta ** x for x in range(self.N))
        self._atom = [sum(self.theta ** (r + j * self.M)
                          for j in range(self.c)) / den
                      for r in range(self.M)]
        self._postf = [[float(v) for v in row] for row in self._post]
        self._atomf = [float(v) for v in self._atom]

    def posterior(self, r):
        if not hasattr(self, "_post"):
            self._build_truth()
        return self._post[r]

    def posterior_f(self, r):
        if not hasattr(self, "_postf"):
            self._build_truth()
        return self._postf[r]

    def atom_prob_f(self, r):
        if not hasattr(self, "_atomf"):
            self._build_truth()
        return self._atomf[r]

    def _posterior_closed(self, r):
        """Exact P(Y = y | r) as Fractions, by the closed form."""
        blks = self.blocks(r)
        if self.q == 1:
            return [Fraction(hi - lo, self.c) for lo, hi in blks]
        denom = 1 - self.q ** self.c
        return [(self.q ** lo - self.q ** hi) / denom for lo, hi in blks]

    def posterior_by_count(self, r):
        """Same thing the slow way, for the truth control."""
        w = [Fraction(0)] * self.k
        for j in range(self.c):
            x = r + j * self.M
            w[(self.k * x) // self.N] += self.theta ** x
        tot = sum(w)
        return [wi / tot for wi in w]

    def atom_prob(self, r):
        """Exact P(r), the marginal over atoms."""
        if not hasattr(self, "_atom"):
            self._build_truth()
        return self._atom[r]

    def label_prob(self):
        """Exact P(Y = y), the marginal over labels."""
        w = [Fraction(0)] * self.k
        for x in range(self.N):
            w[(self.k * x) // self.N] += self.theta ** x
        tot = sum(w)
        return [wi / tot for wi in w]

    # --- the two oracles ---------------------------------------------

    def oracle_cond(self, r, alpha):
        """Smallest set with mass >= 1-alpha AT THIS ATOM."""
        post = self.posterior(r)
        order = sorted(range(self.k), key=lambda y: (-post[y], y))
        acc, chosen = Fraction(0), []
        for y in order:
            chosen.append(y)
            acc += post[y]
            if acc >= 1 - alpha:
                break
        return set(chosen), acc

    def oracle_marg(self, alpha):
        """SLW: {y : p(y|r) >= t}, t the largest level still covering.

        The candidate levels are the finitely many posterior values, so
        the optimum is found exactly by scanning them.
        """
        post = {r: self.posterior(r) for r in range(self.M)}
        pr = {r: self.atom_prob(r) for r in range(self.M)}
        levels = sorted({v for r in post for v in post[r]}, reverse=True)
        best = None
        for t in levels:
            cov = sum(pr[r] * sum(v for v in post[r] if v >= t)
                      for r in range(self.M))
            if cov >= 1 - alpha:
                best = t
                break
        assert best is not None
        return {r: {y for y in range(self.k) if post[r][y] >= best}
                for r in range(self.M)}

    # --- sampling -----------------------------------------------------

    def sample(self, n, rng):
        pop = range(self.N)
        if self.theta == 1:
            xs = [rng.randrange(self.N) for _ in range(n)]
        else:
            th = float(self.theta)
            w = [th ** x for x in pop]
            xs = rng.choices(pop, weights=w, k=n)
        return [(x % self.M, (self.k * x) // self.N) for x in xs]


class BareCell(Cell):
    """K0's ring-free sibling: hand-set posteriors, same interface."""

    def __init__(self, name, atom_posteriors):
        self.name = name
        self.M = len(atom_posteriors)
        self.k = len(atom_posteriors[0])
        self.post = [[Fraction(v).limit_denominator(1000) for v in row]
                     for row in atom_posteriors]
        self.theta = Fraction(1)

    def posterior(self, r):
        return self.post[r]

    def posterior_f(self, r):
        return [float(v) for v in self.post[r]]

    def atom_prob(self, r):
        return Fraction(1, self.M)

    def atom_prob_f(self, r):
        return 1.0 / self.M

    def label_prob(self):
        return [sum(self.post[r][y] for r in range(self.M)) / self.M
                for y in range(self.k)]

    def sample(self, n, rng):
        out = []
        for _ in range(n):
            r = rng.randrange(self.M)
            u, acc, y = rng.random(), 0.0, self.k - 1
            for yy in range(self.k):
                acc += float(self.post[r][yy])
                if u <= acc:
                    y = yy
                    break
            out.append((r, y))
        return out


# ------------------------------------------------------------- methods

def fit_phat(train, M, k):
    """Empirical per-atom posterior; pooled fallback on empty atoms."""
    cnt = [[0] * k for _ in range(M)]
    tot = [0] * M
    pool = [0] * k
    for r, y in train:
        cnt[r][y] += 1
        tot[r] += 1
        pool[y] += 1
    n = max(1, len(train))
    fallback = [pool[y] / n for y in range(k)]
    fired = 0
    phat = []
    for r in range(M):
        if tot[r] == 0:
            fired += 1
            phat.append(list(fallback))
        else:
            phat.append([cnt[r][y] / tot[r] for y in range(k)])
    return phat, fired


def _quantile(scores, alpha):
    """The conformal ceil((n+1)(1-alpha))-th smallest; None if it runs off."""
    n = len(scores)
    num = int(round((n + 1) * (1 - alpha) * 1000000))
    rank = -(-num // 1000000)
    if rank > n:
        return None
    return sorted(scores)[rank - 1]


def split_sets(phat, cal, M, k, alpha):
    a = float(alpha)
    scores = [1.0 - phat[r][y] for r, y in cal]
    qhat = _quantile(scores, a)
    if qhat is None:
        return {r: set(range(k)) for r in range(M)}
    return {r: {y for y in range(k) if 1.0 - phat[r][y] <= qhat}
            for r in range(M)}


def mondrian_sets(phat, cal, M, k, alpha):
    a = float(alpha)
    per = [[] for _ in range(M)]
    for r, y in cal:
        per[r].append(1.0 - phat[r][y])
    out = {}
    for r in range(M):
        qhat = _quantile(per[r], a) if per[r] else None
        if qhat is None:
            out[r] = set(range(k))
        else:
            out[r] = {y for y in range(k) if 1.0 - phat[r][y] <= qhat}
    return out


# ------------------------------------------------------------- scoring

def exact_coverage(cell, sets):
    """Per-atom exact coverage, and the exact marginal, as floats."""
    cond, marg = {}, 0.0
    for r in range(cell.M):
        post = cell.posterior_f(r)
        cv = sum(post[y] for y in sets[r])
        cond[r] = cv
        marg += cell.atom_prob_f(r) * cv
    return cond, marg


def excess(sets, oracle):
    return [len(sets[r]) - len(oracle[r]) for r in sorted(sets)]


def median(v):
    s = sorted(v)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


# ---------------------------------------------------------------- runs

def trial(cell, n, seed, oc, om, alpha):
    rng = random.Random(seed)
    data = cell.sample(n, rng)
    half = n // 2
    train, cal = data[:half], data[half:]
    phat, fired = fit_phat(train, cell.M, cell.k)
    sp = split_sets(phat, cal, cell.M, cell.k, alpha)
    mo = mondrian_sets(phat, cal, cell.M, cell.k, alpha)
    csp, msp = exact_coverage(cell, sp)
    cmo, mmo = exact_coverage(cell, mo)
    return {
        "split_excess": excess(sp, om),
        "mond_excess": excess(mo, oc),
        "split_cond": list(csp.values()),
        "mond_cond": list(cmo.values()),
        "split_marg": msp,
        "mond_marg": mmo,
        "fallback": fired,
    }


def aggregate(cell, n, oc, om, alpha, seed0):
    acc = {"split_excess": [], "mond_excess": [], "split_cond": [],
           "mond_cond": [], "split_marg": [], "mond_marg": [],
           "fallback": 0}
    for t in range(TRIALS):
        r = trial(cell, n, seed0 + t, oc, om, alpha)
        acc["split_excess"] += r["split_excess"]
        acc["mond_excess"] += r["mond_excess"]
        acc["split_cond"] += r["split_cond"]
        acc["mond_cond"] += r["mond_cond"]
        acc["split_marg"].append(r["split_marg"])
        acc["mond_marg"].append(r["mond_marg"])
        acc["fallback"] += r["fallback"]
    return acc


CELLS = [
    Cell("TILT-3", (3, 5, 7), (3, 5), 3, Fraction(24, 25)),
    Cell("FLAT-3", (3, 5, 7), (3, 5), 3, Fraction(1)),
    Cell("DEAD-7", (3, 5, 7), (3, 5), 7, Fraction(1)),
    Cell("TILT-4-WIDE", (3, 5, 7, 11), (3, 5, 7), 4, Fraction(199, 200)),
]


# ------------------------------------------------------------ controls

def control_K1(cell):
    for r in range(cell.M):
        closed = cell.posterior(r)
        counted = cell.posterior_by_count(r)
        assert closed == counted, (cell.name, r, closed, counted)
        assert sum(closed) == 1, (cell.name, r, sum(closed))
    return True


def control_K2(cell, n, seed):
    rng = random.Random(seed)
    data = cell.sample(n, rng)
    ar = [0] * cell.M
    al = [0] * cell.k
    for r, y in data:
        ar[r] += 1
        al[y] += 1
    lp = cell.label_prob()
    for r in range(cell.M):
        p = float(cell.atom_prob(r))
        se = (p * (1 - p) / n) ** 0.5
        assert abs(ar[r] / n - p) <= 4 * se + 1e-9, (cell.name, "atom", r)
    for y in range(cell.k):
        p = float(lp[y])
        se = (p * (1 - p) / n) ** 0.5
        assert abs(al[y] / n - p) <= 4 * se + 1e-9, (cell.name, "label", y)
    return True


def control_K3(cell):
    assert cell.c % cell.k == 0, cell.name
    sizes = set()
    for r in range(cell.M):
        post = cell.posterior(r)
        assert all(v == Fraction(1, cell.k) for v in post), (cell.name, r)
        sizes.add(len(cell.oracle_cond(r, ALPHA)[0]))
    assert len(sizes) == 1, (cell.name, sizes)
    return sorted(sizes)[0]


def control_K0():
    bare = BareCell("K0-BARE", [(0.8, 0.15, 0.05),
                               (0.5, 0.3, 0.2),
                               (0.34, 0.33, 0.33)])
    oc = {r: bare.oracle_cond(r, ALPHA)[0] for r in range(bare.M)}
    om = bare.oracle_marg(ALPHA)
    sizes = [len(oc[r]) for r in range(bare.M)]
    assert sizes == [1, 2, 3], sizes
    acc = aggregate(bare, 32000, oc, om, ALPHA, BASE_SEED)
    me = acc["mond_excess"]
    assert median(me) == 0, ("K0 mondrian median excess", median(me))
    assert max(me) <= 1, ("K0 mondrian max excess", max(me))
    lo = float(1 - ALPHA) - 0.02
    for key in ("split_marg", "mond_marg"):
        m = sum(acc[key]) / len(acc[key])
        assert m >= lo, ("K0 marginal coverage", key, m)
    return sizes, median(me), max(me)


# ---------------------------------------------------------------- main

def main():
    print("=" * 70)
    print("CONTROLS")
    print("=" * 70)
    k0 = control_K0()
    print("K0 positive control PASS  oracle sizes %s  "
          "mondrian median/max excess %s/%s" % k0)
    for cell in CELLS:
        control_K1(cell)
    print("K1 truth control PASS     closed form == fiber sum, all cells")
    for cell in CELLS:
        control_K2(cell, max(SAMPLE_SIZES), BASE_SEED + 777)
    print("K2 sampler control PASS   atom and label frequencies within 4 SE")
    dead = [c for c in CELLS if c.c % c.k == 0]
    for cell in dead:
        sz = control_K3(cell)
        print("K3 degeneracy control PASS  %s flat, oracle size %d"
              % (cell.name, sz))

    print()
    print("=" * 70)
    print("THE FAMILY: exact oracles")
    print("=" * 70)
    price = {}
    oracles = {}
    for cell in CELLS:
        oc = {r: cell.oracle_cond(r, ALPHA)[0] for r in range(cell.M)}
        om = cell.oracle_marg(ALPHA)
        oracles[cell.name] = (oc, om)
        ec = sum(float(cell.atom_prob(r)) * len(oc[r]) for r in range(cell.M))
        em = sum(float(cell.atom_prob(r)) * len(om[r]) for r in range(cell.M))
        price[cell.name] = ec - em
        szc = sorted({len(oc[r]) for r in range(cell.M)})
        szm = sorted({len(om[r]) for r in range(cell.M)})
        cov = sum(float(cell.atom_prob(r))
                  * float(sum(cell.posterior(r)[y] for y in om[r]))
                  for r in range(cell.M))
        print("%-12s N=%-5d M=%-4d c=%-3d k=%d  theta=%-8s" %
              (cell.name, cell.N, cell.M, cell.c, cell.k, cell.theta))
        print("             O_cond sizes %s  E|O_cond|=%.4f" % (szc, ec))
        print("             O_marg sizes %s  E|O_marg|=%.4f "
              "(marginal coverage %.4f)" % (szm, em, cov))
        print("             PRICE OF CONDITIONAL COVERAGE = %+.4f"
              % price[cell.name])

    print()
    print("=" * 70)
    print("THE SCORE: per-atom set-size excess over each method's own oracle")
    print("(split vs O_marg, mondrian vs O_cond; %d trials, alpha=%s)"
          % (TRIALS, ALPHA))
    print("=" * 70)
    hdr = ("%-12s %6s | %-22s | %-22s | %s" %
           ("cell", "n", "SPLIT excess med/max/mean",
            "MOND excess med/max/mean", "exact coverage split|mond"))
    print(hdr)
    for cell in CELLS:
        oc, om = oracles[cell.name]
        for n in SAMPLE_SIZES:
            acc = aggregate(cell, n, oc, om, ALPHA,
                            BASE_SEED + 1000 * SAMPLE_SIZES.index(n))
            se, me = acc["split_excess"], acc["mond_excess"]
            sc, mc = acc["split_cond"], acc["mond_cond"]
            sm = sum(acc["split_marg"]) / len(acc["split_marg"])
            mm = sum(acc["mond_marg"]) / len(acc["mond_marg"])
            print("%-12s %6d | %5.1f %5d %8.4f    | %5.1f %5d %8.4f    | "
                  "marg %.4f|%.4f  cond min %.4f|%.4f  max %.4f|%.4f"
                  % (cell.name, n,
                     median(se), max(se), sum(se) / len(se),
                     median(me), max(me), sum(me) / len(me),
                     sm, mm, min(sc), min(mc), max(sc), max(mc)))
            if acc["fallback"]:
                print("             (empty-atom fallback fired %d times)"
                      % acc["fallback"])

    print()
    print("KILL-SHAPE READ: median AND max excess both 0 at TILT-3 and")
    print("TILT-4-WIDE for BOTH methods would end this line of work.")


if __name__ == "__main__":
    main()
