"""THE NON-IDENTIFIED STATEMENT: what plane is the off-plane specimen on?

THE QUESTION
------------
The statement-law corpus (explore_uncounted_term.py) ends by placing
every documented overconfidence specimen on one plane: coverage is a
function of (b/sigma, h/sigma) and of nothing else, where b is the
uncounted term and h the stated half-width. One specimen it cannot
place. A mixture-proportion unlearning audit
(explore_deletion_ruler.py) matches covariance alone and drops its own
model's mean equation, so at equal class covariances the forgetting
rate pi and its complement 1 - pi are twin minima no sample size
separates. The record concedes the specimen has no bias coordinate to
place -- not a large one, none -- so the plane that fits everything
else has nothing to say about it.

TRANSPLANT, MARKED. The suspicion below is written in the COVERAGE
corpus's vocabulary -- b, sigma, h, nominal, the two ratios -- while
its object is an IDENTIFIABILITY failure, which that vocabulary was
not built for. Every term is re-earned here rather than carried over,
and the two questions are kept apart because the second does not
answer the first.

  (a) DOES THE SIGN LAW SURVIVE NON-IDENTIFICATION? A bound statement
      absorbs its uncounted term with a known sign and so cannot be
      overconfident; that is measured across dials where the term is a
      displacement. It has never been measured where the term is not a
      displacement at all. A bound need not CHOOSE between two minima,
      so a bound over a non-identified parameter may be the one
      construction that still behaves. The record has only a FIT arm
      here -- the tool's bootstrap band. The bound arm does not exist
      and this rig builds it.

  (b) WHAT IS THE PLANE, ONE LEVEL DOWN? A statement's arithmetic is a
      PROJECTION onto the coordinates its own model carries; the
      uncounted term is the residual off that projection, and the two
      ratios are a residual norm against a projected spread.
      Non-identification is then the projection failing to be onto a
      POINT -- which is why the specimen has no bias coordinate rather
      than a large one. If that reading is right, the specimen is not
      off the plane: it is on a MIXTURE of plane points, one per
      element of the fiber the projection lands on, weighted by how
      often a replicate lands there. That is a claim about every
      statement in the corpus and it earns its tier from the
      derivation, not from the one specimen that motivated it; what is
      measured here is whether the mixture reading tracks where the
      single-point reading fails.

THE HAND-ATTACK, BEFORE THE ENGINE
----------------------------------
The audit's estimator is the minimizer over pi in [0, 1] of

    f(p) = (A - p*G + p^2*B)^2,
    d = mu_n - mu_m,  B = d^2,  A = var_u - var_m,
    G = var_n - var_m + B.

Take the ring-free cell the record designed for this failure and give
it a DIAL: F_m = N(0, 1), F_n = N(2, 1 + gamma), mixture weight pi on
F_n. Then d = 2, B = 4, G = gamma + 4, and the population audited
variance is var_u = pi(1 + gamma) + (1 - pi) + 4pi(1 - pi), so
A = pi*gamma + 4pi(1 - pi). The critical equation is

    4p^2 - (4 + gamma)p + pi*gamma + 4pi(1 - pi) = 0,

and p = pi satisfies it identically. The roots multiply to
A/4, so the OTHER root is

    p2 = 1 - pi + gamma/4.

Three things follow on paper, and they set the whole design.

  1. gamma = 0 gives p2 = 1 - pi: the recorded twin minima, re-derived
     from the estimator's own objective rather than quoted.
  2. p2 is an EXACT root at every gamma. Unequal class variances do
     not destroy the second solution -- they SLIDE it. Both roots send
     f to zero exactly, so no amount of data prefers one.
  3. So identification here is restored by the PARAMETER BOX and not
     by the data: the spurious root stops competing when it leaves
     [0, 1], i.e. at gamma = 4*pi. At pi = 1/5 that is gamma = 0.8, a
     transition located before the engine ran.

That third point is the dial's mechanism. It is NOT what the recorded
world cells do: explore_noroot_margin.py computes their population
objectives exactly and both are IDENTIFIED, the second root sitting at
-113/65 and 17/10, far outside the box. Their 28-percent flip rate at
the audit size the tool's own paper reports as converged is therefore
not a second in-box minimum competing, and this rig does not explain
it.

The hand-attack also reads the tie-break, since with both roots exact
the selection cannot be statistical. The estimator scores candidates
and keeps the first strict improvement, so at gamma = 0 the two roots
differ only in the last bits of a float and the mode is chosen by
rounding noise -- which predicts a mode weight near 1/2 flat in n, and
is what the recorded flip rates 0.485 / 0.515 / 0.540 are.

THE ARMS -- ONE BOOTSTRAP, TWO STATEMENTS
-----------------------------------------
Both arms see the SAME three feature samples, use the SAME objective,
and resample the SAME set (the audited one) the same number of times.
They differ only in what their statement's arithmetic reports, which
is what isolates the STATEMENT as the object under measurement.

  FIT   -- the tool as it stands: the point estimate is the argmin,
           and the stated band is the {5%, 95%} quantiles of the
           bootstrap argmin distribution. Nominal 90 percent.
  BOUND -- the same resamples, but each one reports the SET of
           in-box roots rather than the winner. The statement is
           [quantile_5 of the smallest root, quantile_95 of the
           largest root]. The uncounted term here is WHICH ROOT IS THE
           TRUTH, and this statement absorbs it with a known sign: the
           truth is one of the roots, so widening to the set can only
           enlarge, never displace. Nominal 90 percent, the same
           quantiles at the same resample count. A resample whose
           objective has no in-box root reports its argmin as both
           endpoints -- the only statement available there -- and the
           rate of that fallback is printed.

That the bound arm never uses the mean equation is deliberate: it must
answer (a) on the SAME information as the fit, or it has changed the
problem instead of changing the statement.

THE CELLS
---------
  PC    positive control, harness only: F_m = N(0,1), F_n = N(3,4),
        pi = 0.3, n = 5000, one draw. The point estimate must land
        within 0.05 before any other cell is read.
  G0..G5  the ring-free dial at pi = 1/5, gamma in
        {0, 0.25, 0.5, 0.8, 1.0, 2.0}: hand-derived p2 = 0.80, 0.8625,
        0.925, 1.00, 1.05, 1.30. The box ejects the spurious root
        between G2 and G4, at the G3 boundary.
  W2, W3  the ring cells of the recorded audit -- the constant-menu
        depth world at (a, b) = (12, 3) and (2, 8), exact pi = 1/5 and
        4/5 -- so the reading is not purely Gaussian. Their class
        variances were taken here for close but unequal, the
        near-symmetric regime; they are in fact in ratio 0.727 and
        1.750 and both cells are IDENTIFIED
        (explore_noroot_margin.py). Every reading below that treats
        them as carrying a live twin fiber is scoped to the dial.

Audit sizes n in {50, 200, 1000}; R = 200 replicates per (cell, n);
B = 200 bootstrap resamples per replicate, the tool's own count.

THE PREDICTIONS, FIXED BEFORE THE ENGINE WAS WRITTEN
----------------------------------------------------
  Q0  CONTROL, two parts, read before anything else. (i) PC lands
      within 0.05. (ii) The engine's computed population roots at each
      gamma agree with the hand values pi and 1 - pi + gamma/4 to
      better than 1e-12. (iii) On a fresh seed stream the FIT arm at
      G0 reproduces the recorded non-identified cell: mode weight on
      the spurious root in 0.40 to 0.60 at every n, and band coverage
      in 0.80 to 0.92.
  Q1  (a) THE SIGN LAW UNDER NON-IDENTIFICATION. The BOUND arm's
      coverage is never below 0.858 at any (cell, n), gamma = 0
      included. That number is the nominal 0.90 less two Monte-Carlo
      standard errors at R = 200.
  Q2  NOT VALID BY BEING VACUOUS, two halves. (i) At G0 the bound's
      mean width is at least 0.55 at every n and falls by less than
      0.05 from n = 50 to n = 1000 -- the non-identification stays
      visible in the width forever. (ii) At G5, where the box has
      ejected the spurious root, the bound's mean width falls by at
      least 0.10 over that same range -- so the arm does contract when
      the parameter is identified.
  Q3  (b) THE MIXTURE PLANE. For each (cell, n) two coverage
      predictions are computed from the FIT arm's own printed
      quantities and compared with its measured coverage: the
      SINGLE-POINT reading of the recorded plane, from the pooled bias,
      pooled sd and mean half-width; and the MIXTURE reading, the same
      Gaussian formula evaluated per fiber element -- replicates split
      by which population root they are nearer -- and averaged with the
      measured mode weights. Prediction: the mixture reading is within
      0.08 everywhere, while the single-point reading exceeds 0.08 at
      G0 and at any cell whose minority mode weight is above 0.15.
      Cells with fewer than 10 replicates in a mode are excluded from
      the comparison and named.
  Q4  THE SHAPE OF THE DIAL. FIT coverage across gamma at n = 1000 is
      NOT monotone: its minimum falls at neither endpoint, and the
      gamma = 0 cell covers at least 0.05 above that minimum. The
      reading being tested is that EXACT non-identification is
      protective -- a bootstrap straddling two modes states a band wide
      enough to cover -- while APPROXIMATE identification is the
      dangerous regime, concentrating the band onto a mode that is
      wrong a substantial fraction of the time.

KILL-SHAPES, AS OBSERVABLES
---------------------------
  Q0 failed in any part: the rig is broken and nothing else is read.
  Q1 violated at any cell: the SIGN LAW DOES NOT SURVIVE
    non-identification, and the asymmetry the corpus files is scoped
    to terms that are displacements. That is the headline either way.
  Q2 violated: the bound arm is valid by being uninformative, and (a)
    is answered only in the trivial direction -- to be reported as
    such rather than as a surviving law.
  Q3's mixture deviation above 0.08 anywhere: the specimen is not on a
    mixture of plane points either, and (b)'s answer is that there is
    no plane here to be on.
  Q4 monotone: the protective reading is wrong; the measured curve is
    reported as it came.

THE SECOND PASS, AND WHY IT EXISTS
----------------------------------
The first pass passed all three parts of its control and missed four
of its five substantive predictions. Two of those misses are the same
mistake in the slate rather than four results, and the printed table
names both, so the second pass repairs the instrument rather than
restating the predictions. The first pass's numbers stand as they came
and its checks are left FAILING.

  MISS 1 -- THE BOUND ARM WAS NOT A BOUND. The recorded sign law is
  about a ONE-SIDED statement, whose uncounted term is absorbed in a
  known direction. A two-sided quantile band is not that: where the
  empirical objective has a single in-box root the root set IS the
  argmin, so the arm collapses onto the FIT arm exactly (identical
  coverage to three decimals at every such cell) and inherits the
  bootstrap's own calibration, which has nothing to do with the sign
  law. Every Q1 failure sits at such a cell. The repair is to state
  the bound one-sided, in both directions separately, and to make the
  fallback conservative rather than silent: a resample whose objective
  has NO in-box root contributes the box endpoint on the side being
  bounded, so the widening keeps its known sign there too.

  MISS 2 -- THE PLANE'S COORDINATES WERE READ OFF THE WRONG OBJECT.
  Both the single-point and the mixture readings underpredict coverage
  at every bimodal cell, and by far too much to be a mixture-weight
  question (0.405 against a measured 0.820 at gamma = 0). The formula
  assumes an interval of the form ESTIMATE +- HALF-WIDTH; a quantile
  band off a bimodal bootstrap is not centered on its own point
  estimate, and there the two are half the box apart. So the reading
  the first pass tested was not the plane's -- the plane's coordinates
  belong to the STATEMENT (where its interval sits and how wide) and
  not to the ESTIMATOR (where its point sits). Under identification
  the two coincide, which is why nothing before this had to tell them
  apart, and non-identification is the case that separates them.

The second pass adds three arms and one reading, on the SAME
resamples, in the same order, with no new draws -- so the first
pass's numbers reproduce unchanged.

  BND2  the first pass's two-sided band, kept and reported as it came.
  UPPER a one-sided upper bound on pi: the 95% quantile, over
        resamples, of the LARGEST in-box root, with a no-root resample
        contributing the box top 1. Nominal 95%.
  LOWER the mirror: the 5% quantile of the SMALLEST in-box root, a
        no-root resample contributing the box bottom 0. Nominal 95%.

  THE STATEMENT-CENTRE READING. The same Gaussian formula as the
  recorded plane, evaluated at the STATEMENT's coordinates: b* =
  mean(band centre) - pi, sigma* = sd(band centre), h = mean
  half-width, against the FIT arm's measured coverage.

  PREDICTIONS, FIXED BEFORE THE SECOND ENGINE EDIT
    Q11 The statement-centre reading is within 0.08 of the FIT arm's
        measured coverage at every cell, bimodal ones included.
    Q12 At the identified cells (gamma = 1.0 and 2.0, a single in-box
        root) the estimator bias and the statement-centre bias agree
        within 0.03 -- the two coordinates coincide exactly where the
        corpus has always read them, so the second pass generalizes
        the plane rather than replacing it.
    Q13 (a) THE SIGN LAW, PROPERLY STATED. UPPER and LOWER each cover
        at or above 0.919 -- the 0.95 nominal less two Monte-Carlo
        standard errors -- at EVERY cell, the non-identified ones
        included. A cell below that is the sign law failing under
        non-identification, and it is the headline either way.
    Q14 NOT VALID BY BEING VACUOUS. At gamma = 2.00 (identified) the
        UPPER bound's mean slack above pi falls below 0.10 by
        n = 1000; at gamma = 0 it stays above 0.40 at every n. The
        same statement contracts where the parameter is identified and
        refuses to where it is not -- which is the non-identification
        made visible in a width, exactly the coordinate the fit arm's
        own band does not carry.

  KILL-SHAPES
    Q11 above 0.08 anywhere: there is no plane here even in the
      statement's own coordinates, and (b) is a funeral.
    Q12 above 0.03: the statement-centre reading is a different law
      rather than a generalization, and the recorded plane's scope
      shrinks to the identified case.
    Q13 violated at any cell: the sign law does not survive
      non-identification.
    Q14 violated in either half: the bound is uninformative and Q13 is
      trivially true.

THE THIRD READ -- ONE DIAGNOSTIC, PRE-REGISTERED
------------------------------------------------
The second pass's plane readings fail in a direction the first pass's
did not: at the bimodal cells the statement-centre reading OVERpredicts
(1.000 against a measured 0.820 at gamma = 0), where the estimator
reading underpredicted. A band centred near the box middle and 0.76
wide contains 0.2 outright, so a formula fed the MEAN centre and the
MEAN half-width has to say 1, and the truth is that it misses 18% of
the time. That can only be the third assumption in the plane's
arithmetic, the one that never had to be written down: h is treated as
a CONSTANT at its mean, with all the randomness in the estimate. Under
identification the stated half-width concentrates and the assumption
is free. Non-identification is the case where the statement's own
width is itself a heavy random variable, and no choice of centre
repairs a formula that has already averaged it away.

  Q15, FIXED BEFORE THE QUANTITY WAS COMPUTED. Let cv(h) be the
      coefficient of variation of the stated half-width across
      replicates in a cell. Every cell with cv(h) below 0.15 has a
      statement-centre deviation below 0.08, and every cell that fails
      Q11 has cv(h) above 0.15. Kill: a cell on either wrong side of
      that split means the half-width's randomness is not what breaks
      the plane, and the diagnostic is discarded rather than reported.

RUN RECORD
----------
One run of the final engine, 10.5 s, single process, memory far under
the analysis ceiling. R = 200 replicates and B = 200 bootstrap
resamples at each of three audit sizes (50, 200, 1000) over eight
cells -- six on the ring-free dial, two on the constant-menu depth
world -- single seed stream (20260804). The second and third passes
add summaries over the SAME resamples and draw no new randomness, so
the first pass's numbers are the ones printed here. Of 17 checks 6
pass (Q0 in three parts, Q2(ii), Q14 in two halves) and 11 fail.
TWO of those failures, Q1 and Q2(i), come from ONE design error -- the
first pass's bound arm was not a bound -- caught by the printed table
and kept failing rather than restated, with the repair measured in the
second pass instead. The other nine are results: a prediction that was
wrong about the world rather than about the rig, and they are reported
below as they came.

FINDINGS
--------
F1  CONTROL, THREE PARTS, ALL PASSED -- and the second part is a
    result in its own right. The hand-derived fiber of the audit's
    objective, p = pi and p2 = 1 - pi + gamma/4, matched the engine's
    computed roots to 1.1e-16 at every dial setting. So the twin
    minima the record reports at equal class covariances are the
    gamma = 0 end of a one-parameter family, and the second solution
    is EXACT at every gamma: unequal class variances never destroy it,
    they slide it, and it stops competing only when it leaves the
    parameter box at gamma = 4*pi (0.8 at pi = 1/5). Identification
    here is restored by the BOX and not by the data, which is what
    the recorded world cells' 28% flip rate at their own converged
    audit size is. The box mechanism is not left as a derivation: the
    dial prints its signature directly, the weight the estimator puts
    on the spurious mode falling monotonically as p2 walks toward the
    box edge -- 0.54, 0.42, 0.34, 0.26 at the smallest audit size for
    p2 = 0.80, 0.8625, 0.925, 1.00 -- and vanishing to 0.00 at both
    settings where p2 is strictly outside. The boundary cell is the
    telling one: at p2 = 1.00 exactly the weight is 0.26 rather than
    zero, because sampling noise puts the root inside the box in some
    replicates and outside in others, which is the box doing the
    selecting in plain view. On a fresh seed stream the fit arm
    reproduced the
    recorded non-identified cell (spurious-mode weight 0.54, 0.56,
    0.59; band coverage 0.855, 0.915, 0.820), so the arms beside it
    can be read.

F2  THE SIGN LAW SURVIVES NON-IDENTIFICATION, AND NON-IDENTIFICATION
    MAKES THE BOUND SAFER RATHER THAN MORE DANGEROUS (observation, 24
    cells). At the exactly non-identified cell the one-sided upper
    bound covered 1.000, 1.000, 1.000 against its 0.95 nominal, while
    the fit band on the same resamples covered 0.855, 0.915, 0.820
    against its own 0.90. A bound does not have to choose between the
    minima, so the fiber term enters it with a known sign and only
    widens it -- which is the law's own mechanism, now measured where
    the term is not a displacement at all.
    THAT CONTRAST HAS A CONFOUND AND THE RUN SETTLES IT. Two things
    make the upper bound's 1.000 easier than it looks: it is a
    ONE-SIDED statement against the fit's two-sided one, and the whole
    Gaussian dial is run at pi = 1/5, which is the LOW element of the
    fiber, so a statement that reports the larger root covers by
    construction. The mirror arm is what carries the content. At that
    same cell the LOWER bound is the tight one -- its slack below the
    truth falls 0.196, 0.143, 0.046 as the audit grows -- and it still
    covers 0.945 to 1.000. A statement can be tight against a
    non-identified truth and stay honest; it is the direction the
    second root sits in that cannot be tightened. The ring cell at
    pi = 4/5 swaps the roles: there the LOWER bound is the trivial one
    (1.000 at every size) and the upper is the tight one that misses
    (0.810 to 0.890). That swap is BOX geometry and not a second
    reading of the hull -- that cell is identified, as the scope note
    in THE CELLS records.
    Read as a pair the bounds close on the FIBER'S HULL and not on a
    point. At gamma = 0 the bracket runs [0.004, 0.997], [0.057,
    0.946], [0.154, 0.845] across the three audit sizes, so its excess
    beyond the hull [0.2, 0.8] falls 0.196, 0.143, 0.046 at the low
    end and 0.197, 0.146, 0.045 at the high -- the two ends agreeing
    to within 0.003 at every size, which is what a pair closing on a
    SET rather than on a point looks like and is not something either
    arm was built to produce. Three sizes measure the approach; the
    limit is the identified set by construction and is not measured
    here. Either way it is the shape the fit's single band cannot
    report, its own width narrowing at that same cell while its
    coverage does not rise.
    The frozen bar was a single floor over every cell and it FAILED
    (0.810 to 0.890 at four cells for the upper bound; 0.875 and 0.915
    at two for the lower), and the run carries its own control, which
    points the same way the law does. On the Gaussian dial the upper
    bound's whole shortfall sits at the IDENTIFIED cells -- 0.875 to
    0.965 at gamma = 1.00 and 2.00, where the fiber is a single point
    and there is no uncounted fiber term to absorb -- while every
    twin-fiber cell runs 0.955 to 1.000. So the misses are not merely
    unrelated to the uncounted term, they are ANTICORRELATED with it:
    the arm is at its safest exactly where the term is largest, and
    what remains is the bootstrap quantile's own calibration, which
    the sign law never claimed to fix. The law is about the UNCOUNTED
    term, not the counted one.
    The six misses split into TWO populations and neither is the
    uncounted term, which is why the sentence above is about the dial
    only. On the DIAL the shortfall is the identified-cell one just
    described. On the RING cells it is BOX geometry: a one-sided bound
    fails where the truth sits near its own end of [0, 1], the upper
    at pi = 4/5 (0.810 to 0.890) and the lower at pi = 1/5 (0.875 at
    the largest audit size). The populations are disjoint and so are
    the bounds' failures -- no cell breaks both, so the pair is never
    simultaneously wrong, which is what makes reading them as a
    bracket legitimate.
    Q13 is left FAILING as frozen; the reading that survives is the
    comparison across cells and not the floor.

F3  THE FIRST PASS'S BOUND ARM WAS NOT A BOUND, AND THE TABLE SAID SO
    (Q1, Q2(i), kept failing). A two-sided quantile band over the root
    set collapses onto the fit arm wherever the population fiber is a
    single point: coverage identical to three decimals at four of
    those six cells and differing by at most 0.025 at the other two,
    where a resample with no in-box root falls back to its argmin. So
    it inherits the bootstrap's calibration and tests nothing about
    signs. Every Q1 failure sits at such a cell or at a ring cell
    where the no-root fallback dominates; across the twelve cells of
    the Gaussian dial that carry a live twin fiber it never dipped
    below its floor (0.875 to 0.955). The species is a
    statement kind named by its INTENT rather than by its arithmetic,
    and the repair is what F2 measures. Q2(i) failed with it: the
    two-sided arm's width at gamma = 0 does narrow (0.865 to 0.692),
    because narrowing is what its fit half does.

F4  THE SPECIMEN STAYS OFF THE PLANE, AND THREE REPAIRS FAIL ON
    MEASUREMENT (observation, 24 cells). The record files this
    specimen as unplaceable for want of a bias coordinate. It is not
    the missing coordinate.
      - The MIXTURE reading -- the plane evaluated per fiber element
        and averaged by the measured mode weights, which is what "the
        projection is not onto a point" predicts -- misses by 0.34 to
        0.47 at the non-identified cell, no better than the
        single-point reading it was built to repair.
      - The STATEMENT-CENTRE reading -- the plane's coordinates taken
        off the interval rather than off the estimator -- fails the
        other way, OVERpredicting (1.000 against a measured 0.820),
        and it reduces to the recorded reading only at the most
        separated cell and only at the two larger sizes (gamma = 2.00:
        biases agreeing to 0.023 and 0.002 against a 0.03 tolerance,
        but 0.049 apart at the smallest). At gamma = 1.00 -- still a
        single-point fiber, still identified -- it is 0.079 to 0.111
        apart at every size. A generalization has to agree wherever
        the thing it generalizes applies, and this one agrees only
        where the two coordinates were never going to differ.
      - The HALF-WIDTH'S RANDOMNESS, pre-registered as the third
        assumption, carries no association with the failure at all
        (Pearson +0.222, Spearman -0.042 over the 24 cells): the three
        lowest coefficients of variation, 0.072 to 0.087, carry
        deviations of 0.095 to 0.180, while the highest two, 0.687 and
        0.886, carry 0.008 and 0.337 -- the full range at both ends.
        Discarded by its own kill-shape, and recorded here so it is
        not proposed again.
    What the three misses share is that they all move a COORDINATE
    while keeping the plane's form. The form is the assumption: the
    arithmetic presumes a statement shaped as a point plus or minus a
    half-width with jointly near-Gaussian parts, and a quantile band
    off a multi-modal bootstrap is not that shape. So the specimen is
    off the plane for a reason one level up from the one the record
    guessed -- not a missing coordinate but a statement whose geometry
    the plane's arithmetic cannot express -- and the plane's scope is
    the statements that ARE that shape, which is every arm in the
    corpus so far and is not a vacuous scope.

F5  THE BOUND MAKES NON-IDENTIFICATION VISIBLE, AND THE FIT HIDES IT
    (Q14, both halves passed). The same one-sided bound contracts
    where the parameter is identified -- mean slack above the truth
    0.551, 0.152, 0.051 across the three audit sizes at gamma = 2.00
    -- and refuses to where it is not: 0.797, 0.746, 0.645 at
    gamma = 0, still two thirds of the box at the largest size. The
    fit band's own width at that same cell narrows (0.809 to 0.671)
    while its coverage does not rise. So the failure the record
    documents as invisible -- a band tightening while its coverage
    stays -- is invisible to that STATEMENT and not to the data: a
    bound statement built on the same resamples converts it into a
    width that will not close. That is a usable reading for an
    auditor, and it costs nothing but the statement kind.

F6  THE DIAL'S SHAPE, AS IT CAME (Q4 failed). Fit coverage across
    gamma at the largest audit size runs 0.820, 0.825, 0.905, 0.920,
    0.895, 0.875: the minimum is at gamma = 0 and the curve is not
    the interior-minimum shape the prediction named. So exact
    non-identification is the WORST cell for the fit band, not a
    protective one, and the reading that a straddling bootstrap buys
    coverage is wrong. The ring cells are worse still on this rig's
    own draws (0.690 to 0.770, against the 0.695 to 0.800 the sibling
    recorded on its own seed stream) and their damage is elsewhere:
    their empirical
    objective has NO in-box solution in 0.26 to 0.59 of resamples
    (0.586 at the smallest audit size, still 0.286 at the largest),
    a regime the tool's own procedure has no statement for. What
    separates it from the dial is the TRAJECTORY and not the level:
    every Gaussian cell reaches 0.145 to 0.268 at the smallest audit
    size and 0.000 at the largest, while both ring cells plateau near
    0.26 to 0.29 and stop falling. And the plateau is NOT
    misspecification -- the sibling rig's bridge establishes that the
    fiber decomposition makes the mixture assumption hold EXACTLY on
    these cells -- so whatever the persistence reads, it is not a
    model the world breaks. SETTLED SINCE, and not by the feature:
    explore_noroot_margin.py derives the rate from the coefficients
    alone -- a no-root sample is one whose A leaves the range of
    G*p - B*p^2 over the box, and these cells sit 0.0160 and 0.0156
    from that range's edge against the dial's 0.360. Discreteness acts
    only by shrinking that margin.

F7  WHAT THIS DOES NOT SETTLE. The bound arm here is one-sided in
    each direction separately and both were run; nothing here builds
    the two-sided bound statement an auditor reporting an interval
    would want, and F2's box effect says its two ends fail on
    different cells, so it is not their intersection. And the
    no-root regime of F6 is measured but not modelled: an objective
    with no solution in its own parameter box is a fourth thing,
    beside a point fiber, a twin fiber, and a displacement.
    One scope limit of the DIAL, since F2 turns on it: every Gaussian
    cell is run at pi = 1/5, below the fiber's midpoint, so the dial
    evidence for the UPPER bound is all from the easy side and the
    only cell placing the truth above that midpoint is a single ring
    cell. A dial run at pi = 4/5 would say whether the roles swap as
    cleanly as that one cell suggests.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
from fractions import Fraction

import numpy as np

RNG = np.random.default_rng(20260804)

R_REPLICATES = 200
B_BOOTSTRAP = 200
AUDIT_SIZES = (50, 200, 1000)
WINDOW = 3
NOMINAL = 0.90
MC_FLOOR = 0.858          # 0.90 nominal less two MC standard errors, R=200
MC_FLOOR95 = 0.919        # the one-sided arms' 0.95 nominal, same rule
PLANE_TOL = 0.08
MODE_MIN = 10             # replicates a mode needs to be read


# ------------------------------------------------------- the objective

def moments(feat_m, feat_n, feat_u):
    """(A, G, B) of the covariance-matching objective, computed once."""
    d = float(np.mean(feat_n) - np.mean(feat_m))
    bq = d * d
    a_ = float(np.var(feat_u) - np.var(feat_m))
    g_ = float(np.var(feat_n) - np.var(feat_m)) + bq
    return a_, g_, bq


def point_from(a_, g_, bq):
    """The audit's point estimate: argmin of f over [0, 1], with the
    candidate order the tool itself uses (endpoints, vertex, then the
    two roots), since with two exact roots the tie-break is what picks
    the mode."""
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


def roots_from(a_, g_, bq):
    """Every exact-moment solution inside [0, 1] -- the fiber the
    projection lands on, as the sample sees it."""
    out = []
    if bq > 0.0:
        disc = g_ * g_ - 4.0 * bq * a_
        if disc >= 0.0:
            r = disc ** 0.5
            for p in ((g_ + r) / (2.0 * bq), (g_ - r) / (2.0 * bq)):
                if 0.0 <= p <= 1.0:
                    out.append(p)
    elif abs(g_) > 0.0:
        p = a_ / g_
        if 0.0 <= p <= 1.0:
            out.append(p)
    return out


def both_statements(feat_m, feat_n, feat_u, rng):
    """One resample loop, four statements: the FIT band (quantiles of
    the argmin), the two-sided BND2 band (quantiles of the root set's
    endpoints, a no-root resample falling back to its argmin), and the
    one-sided UPPER and LOWER bounds (the same quantiles, a no-root
    resample contributing the box endpoint on the side being bounded,
    so the widening keeps its sign). Returns (point, fit_lo, fit_hi,
    bnd_lo, bnd_hi, upper, lower, no_root_fraction)."""
    a0, g0, b0 = moments(feat_m, feat_n, feat_u)
    point = point_from(a0, g0, b0)

    n = len(feat_u)
    var_m = float(np.var(feat_m))
    pts = np.empty(B_BOOTSTRAP)
    los = np.empty(B_BOOTSTRAP)
    his = np.empty(B_BOOTSTRAP)
    los_c = np.empty(B_BOOTSTRAP)   # conservative fallback, one-sided
    his_c = np.empty(B_BOOTSTRAP)
    no_root = 0
    for b in range(B_BOOTSTRAP):
        res = feat_u[rng.integers(0, n, size=n)]
        a_ = float(np.var(res)) - var_m
        p = point_from(a_, g0, b0)
        rts = roots_from(a_, g0, b0)
        pts[b] = p
        if rts:
            los[b] = los_c[b] = min(rts)
            his[b] = his_c[b] = max(rts)
        else:
            no_root += 1
            los[b] = his[b] = p
            los_c[b] = 0.0
            his_c[b] = 1.0
    return (point,
            float(np.quantile(pts, 0.05)), float(np.quantile(pts, 0.95)),
            float(np.quantile(los, 0.05)), float(np.quantile(his, 0.95)),
            float(np.quantile(his_c, 0.95)),
            float(np.quantile(los_c, 0.05)),
            no_root / B_BOOTSTRAP)


# ---------------------------------------------------------- the worlds

def gaussian_dial(gamma, pi, n, rng):
    """The ring-free cell with the identifiability dial: equal means
    gap 2, class variance ratio set by gamma."""
    sd_n = math.sqrt(1.0 + gamma)
    feat_m = rng.normal(0.0, 1.0, n)
    feat_n = rng.normal(2.0, sd_n, n)
    from_n = rng.random(n) < pi
    feat_u = np.where(from_n, rng.normal(2.0, sd_n, n),
                      rng.normal(0.0, 1.0, n))
    return feat_m, feat_n, feat_u


def gaussian_plain(mu_m, sd_m, mu_n, sd_n, pi, n, rng):
    feat_m = rng.normal(mu_m, sd_m, n)
    feat_n = rng.normal(mu_n, sd_n, n)
    from_n = rng.random(n) < pi
    feat_u = np.where(from_n, rng.normal(mu_n, sd_n, n),
                      rng.normal(mu_m, sd_m, n))
    return feat_m, feat_n, feat_u


def world_features(a, b, n, rng):
    """Fiber sampler for the constant-menu depth world at 2^a 3^b:
    class-conditional and unconditioned window-count features."""
    t = a + b

    def window_counts(twos, total, m):
        keys = rng.random((m, total))
        order = np.argsort(keys, axis=1)
        is_two = order < twos
        return is_two[:, :WINDOW].sum(axis=1).astype(float)

    feat_m = window_counts(a - 1, t - 1, n)
    feat_n = window_counts(a, t - 1, n)
    keys = rng.random((n, t))
    order = np.argsort(keys, axis=1)
    is_two = order < a
    feat_u = is_two[:, 1:1 + WINDOW].sum(axis=1).astype(float)
    return feat_m, feat_n, feat_u


# ------------------------------------------------------- the plane read

def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def gauss_coverage(bias, sd, half):
    """The recorded plane's two-sided formula at one point."""
    if sd <= 0.0:
        return 1.0 if abs(bias) <= half else 0.0
    return phi((half - bias) / sd) - phi((-half - bias) / sd)


def population_roots(gamma, pi):
    """The hand-derived fiber: pi always, and 1 - pi + gamma/4 when it
    is inside the box."""
    p2 = 1.0 - pi + gamma / 4.0
    return [pi, p2] if 0.0 <= p2 <= 1.0 else [pi]


# --------------------------------------------------------- measurement

def run_cell(name, sampler, pi_exact, roots_pop, sizes=AUDIT_SIZES):
    """roots_pop is the fiber the replicates are SPLIT by. On the
    Gaussian dial it is derived -- pi and the hand value p2, exact.
    On the ring cells it is the NOMINAL twin {pi, 1 - pi}, and that is
    a LABEL and not their fiber: explore_noroot_margin.py computes
    their second root exactly at -113/65 and 17/10, so both cells are
    identified and the split there partitions replicates rather than
    fiber elements."""
    pi_f = float(pi_exact)
    print(f"\n== {name}   exact pi = {pi_exact} = {pi_f:.4f}"
          f"   split fiber {[round(r, 4) for r in roots_pop]} ==")
    print(f"{'n':>6} | {'FIT cov':>7} {'width':>6} {'wt2':>5} "
          f"{'bias':>7} {'sd':>6} | {'BND2':>6} {'UP cov':>6} "
          f"{'up sl':>6} {'LO cov':>6} {'lo sl':>6} {'noroot':>6} | "
          f"{'pooled':>7} {'mixture':>7} {'centre':>7}")
    rows = []
    for n in sizes:
        pts = np.empty(R_REPLICATES)
        fit_half = np.empty(R_REPLICATES)
        fit_mid = np.empty(R_REPLICATES)
        fit_cov = 0
        bnd_w = np.empty(R_REPLICATES)
        bnd_cov = 0
        up_slack = np.empty(R_REPLICATES)
        lo_slack = np.empty(R_REPLICATES)
        up_cov = 0
        lo_cov = 0
        noroot = 0.0
        for r in range(R_REPLICATES):
            fm, fn, fu = sampler(n, RNG)
            p, flo, fhi, blo, bhi, up, lw, nr = both_statements(
                fm, fn, fu, RNG)
            pts[r] = p
            fit_half[r] = (fhi - flo) / 2.0
            fit_mid[r] = (fhi + flo) / 2.0
            if flo <= pi_f <= fhi:
                fit_cov += 1
            bnd_w[r] = bhi - blo
            if blo <= pi_f <= bhi:
                bnd_cov += 1
            up_slack[r] = up - pi_f
            lo_slack[r] = pi_f - lw
            if pi_f <= up:
                up_cov += 1
            if pi_f >= lw:
                lo_cov += 1
            noroot += nr
        fit_cov /= R_REPLICATES
        bnd_cov /= R_REPLICATES
        up_cov /= R_REPLICATES
        lo_cov /= R_REPLICATES
        noroot /= R_REPLICATES

        # the single-point reading of the plane
        bias = float(np.mean(pts)) - pi_f
        sd = float(np.std(pts))
        half = float(np.mean(fit_half))
        pooled = gauss_coverage(bias, sd, half)

        # the plane read at the STATEMENT's own coordinates
        cbias = float(np.mean(fit_mid)) - pi_f
        csd = float(np.std(fit_mid))
        centre = gauss_coverage(cbias, csd, half)
        cvh = float(np.std(fit_half)) / half if half > 0 else 0.0

        # the mixture reading: split by nearest population root
        idx = np.argmin(np.abs(pts[:, None] - np.array(roots_pop)[None, :]),
                        axis=1)
        mix = 0.0
        readable = True
        wt2 = 0.0
        for j, _root in enumerate(roots_pop):
            sel = idx == j
            cnt = int(sel.sum())
            if j == 1:
                wt2 = cnt / R_REPLICATES
            if cnt == 0:
                continue
            if cnt < MODE_MIN:
                readable = False
                continue
            w = cnt / R_REPLICATES
            mix += w * gauss_coverage(float(np.mean(pts[sel])) - pi_f,
                                      float(np.std(pts[sel])),
                                      float(np.mean(fit_half[sel])))
        mix_s = f"{mix:>7.3f}" if readable else f"{mix:>6.3f}*"

        print(f"{n:>6} | {fit_cov:>7.3f} {2 * half:>6.3f} {wt2:>5.2f} "
              f"{bias:>7.3f} {sd:>6.3f} | {bnd_cov:>6.3f} "
              f"{up_cov:>6.3f} {float(np.mean(up_slack)):>6.3f} "
              f"{lo_cov:>6.3f} {float(np.mean(lo_slack)):>6.3f} "
              f"{noroot:>6.3f} | "
              f"{pooled:>7.3f} {mix_s} {centre:>7.3f}")
        rows.append(dict(n=n, fit=fit_cov, bnd=bnd_cov,
                         bndw=float(np.mean(bnd_w)), wt2=wt2,
                         pooled=pooled, mix=mix, readable=readable,
                         centre=centre, cbias=cbias, bias=bias,
                         up=up_cov, lo=lo_cov, cvh=cvh,
                         upslack=float(np.mean(up_slack)),
                         loslack=float(np.mean(lo_slack))))
    return rows


def main():
    pi = 0.2

    # Q0 (i): the harness gate.
    fm, fn, fu = gaussian_plain(0.0, 1.0, 3.0, 2.0, 0.3, 5000, RNG)
    a0, g0, b0 = moments(fm, fn, fu)
    pc = point_from(a0, g0, b0)
    ok = abs(pc - 0.3) <= 0.05
    print(f"Q0(i)  PC harness: pi_hat = {pc:.4f} (0.30 +- 0.05) "
          f"-> {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("HARNESS FAILURE -- no other cell is readable.")
        return

    # Q0 (ii): the hand-derived fiber against the engine's own roots,
    # computed from exact population moments.
    gammas = (0.0, 0.25, 0.5, 0.8, 1.0, 2.0)
    worst = 0.0
    for gamma in gammas:
        bq = 4.0
        g_ = gamma + 4.0
        a_ = pi * gamma + 4.0 * pi * (1.0 - pi)
        eng = sorted(roots_from(a_, g_, bq))
        hand = sorted(r for r in (pi, 1.0 - pi + gamma / 4.0)
                      if 0.0 <= r <= 1.0)
        if len(eng) != len(hand):
            worst = float("inf")
        else:
            worst = max(worst, max(abs(e - h) for e, h in zip(eng, hand)))
    print(f"Q0(ii) hand fiber vs engine roots: max |diff| = {worst:.3e} "
          f"-> {'PASS' if worst < 1e-12 else 'FAIL'}")
    if not (worst < 1e-12):
        print("HAND-ATTACK DISAGREES WITH THE ENGINE -- nothing is read.")
        return

    # The ring-free dial.
    dial = {}
    for gamma in gammas:
        rows = run_cell(
            f"G gamma={gamma:.2f}  (ring-free dial)",
            lambda n, rng, gamma=gamma: gaussian_dial(gamma, pi, n, rng),
            Fraction(1, 5),
            population_roots(gamma, pi))
        dial[gamma] = rows

    # The ring cells of the recorded audit.
    ring = {}
    for (a, b) in ((12, 3), (2, 8)):
        p_exact = Fraction(b, a + b)
        pf = float(p_exact)
        ring[(a, b)] = run_cell(
            f"W (a,b)=({a},{b})  (constant-menu depth world)",
            lambda n, rng, a=a, b=b: world_features(a, b, n, rng),
            p_exact,
            [pf, 1.0 - pf])

    # ------------------------------------------------------- verdicts
    print("\n" + "=" * 68)
    allrows = ([(f"G{g:.2f}", r) for g in gammas for r in dial[g]]
               + [(f"W{k}", r) for k in ring for r in ring[k]])

    g0rows = dial[0.0]
    ok03 = all(0.40 <= r["wt2"] <= 0.60 and 0.80 <= r["fit"] <= 0.92
               for r in g0rows)
    print(f"Q0(iii) G0 reproduces the recorded cell "
          f"(wt2 in .40-.60, fit cov in .80-.92): "
          f"{'PASS' if ok03 else 'FAIL'}")

    bad = [(nm, r["n"], r["bnd"]) for nm, r in allrows
           if r["bnd"] < MC_FLOOR]
    print(f"Q1  BOUND coverage >= {MC_FLOOR} everywhere: "
          f"{'PASS' if not bad else 'FAIL ' + str(bad)}")

    w_small, w_large = g0rows[0]["bndw"], g0rows[-1]["bndw"]
    q2a = (all(r["bndw"] >= 0.55 for r in g0rows)
           and (w_small - w_large) < 0.05)
    g5 = dial[2.0]
    q2b = (g5[0]["bndw"] - g5[-1]["bndw"]) >= 0.10
    print(f"Q2(i)  G0 bound width >= 0.55 and flat "
          f"({w_small:.3f} -> {w_large:.3f}): {'PASS' if q2a else 'FAIL'}")
    print(f"Q2(ii) G5 bound width contracts >= 0.10 "
          f"({g5[0]['bndw']:.3f} -> {g5[-1]['bndw']:.3f}): "
          f"{'PASS' if q2b else 'FAIL'}")

    mixbad = [(nm, r["n"], round(abs(r["mix"] - r["fit"]), 3))
              for nm, r in allrows
              if r["readable"] and abs(r["mix"] - r["fit"]) > PLANE_TOL]
    print(f"Q3(a) mixture reading within {PLANE_TOL} at every readable "
          f"cell: {'PASS' if not mixbad else 'FAIL ' + str(mixbad)}")
    pool_should = [(nm, r["n"], round(abs(r["pooled"] - r["fit"]), 3))
                   for nm, r in allrows if r["wt2"] > 0.15]
    pool_fail = [x for x in pool_should if x[2] <= PLANE_TOL]
    print(f"Q3(b) single-point reading misses by > {PLANE_TOL} wherever "
          f"the minority mode carries > 0.15: "
          f"{'PASS' if not pool_fail else 'FAIL ' + str(pool_fail)}")
    print(f"      (single-point deviations at those cells: {pool_should})")

    curve = [(g, dial[g][-1]["fit"]) for g in gammas]
    lo_g = min(curve, key=lambda t: t[1])
    q4 = (lo_g[0] not in (gammas[0], gammas[-1])
          and curve[0][1] - lo_g[1] >= 0.05)
    print(f"Q4  FIT coverage across gamma at n=1000 is non-monotone with "
          f"an interior minimum: {'PASS' if q4 else 'FAIL'}")
    print(f"      curve {[(g, round(c, 3)) for g, c in curve]}, "
          f"minimum at gamma={lo_g[0]}")

    print("\n--- second pass ---")
    cbad = [(nm, r["n"], round(abs(r["centre"] - r["fit"]), 3))
            for nm, r in allrows if abs(r["centre"] - r["fit"]) > PLANE_TOL]
    print(f"Q11 statement-centre reading within {PLANE_TOL} at every "
          f"cell: {'PASS' if not cbad else 'FAIL ' + str(cbad)}")

    idcells = [(f"G{g:.2f}", r) for g in (1.0, 2.0) for r in dial[g]]
    dbad = [(nm, r["n"], round(abs(r["cbias"] - r["bias"]), 3))
            for nm, r in idcells if abs(r["cbias"] - r["bias"]) > 0.03]
    print(f"Q12 at the identified cells the two biases agree within "
          f"0.03: {'PASS' if not dbad else 'FAIL ' + str(dbad)}")
    print(f"      (estimator vs centre bias there: "
          f"{[(nm, r['n'], round(r['bias'], 3), round(r['cbias'], 3)) for nm, r in idcells]})")

    ubad = [(nm, r["n"], r["up"]) for nm, r in allrows
            if r["up"] < MC_FLOOR95]
    lbad = [(nm, r["n"], r["lo"]) for nm, r in allrows
            if r["lo"] < MC_FLOOR95]
    print(f"Q13 UPPER covers >= {MC_FLOOR95} everywhere: "
          f"{'PASS' if not ubad else 'FAIL ' + str(ubad)}")
    print(f"    LOWER covers >= {MC_FLOOR95} everywhere: "
          f"{'PASS' if not lbad else 'FAIL ' + str(lbad)}")

    q14a = dial[2.0][-1]["upslack"] < 0.10
    q14b = all(r["upslack"] > 0.40 for r in dial[0.0])
    print(f"Q14 UPPER slack contracts when identified "
          f"({dial[2.0][-1]['upslack']:.3f} < 0.10 at gamma=2, n=1000): "
          f"{'PASS' if q14a else 'FAIL'}")
    print(f"    and refuses to when not "
          f"({[round(r['upslack'], 3) for r in dial[0.0]]} all > 0.40): "
          f"{'PASS' if q14b else 'FAIL'}")

    print("\n--- third read ---")
    lowcv_bad = [(nm, r["n"], round(r["cvh"], 3),
                  round(abs(r["centre"] - r["fit"]), 3))
                 for nm, r in allrows
                 if r["cvh"] < 0.15 and abs(r["centre"] - r["fit"]) > PLANE_TOL]
    failcv_bad = [(nm, r["n"], round(r["cvh"], 3))
                  for nm, r in allrows
                  if abs(r["centre"] - r["fit"]) > PLANE_TOL
                  and r["cvh"] <= 0.15]
    print(f"Q15 cv(h) < 0.15 implies deviation < {PLANE_TOL}: "
          f"{'PASS' if not lowcv_bad else 'FAIL ' + str(lowcv_bad)}")
    print(f"    every Q11 failure has cv(h) > 0.15 "
          f"(the CONTRAPOSITIVE of the line above, not independent "
          f"evidence -- the slate froze one condition twice): "
          f"{'PASS' if not failcv_bad else 'FAIL ' + str(failcv_bad)}")
    print("    (cell, cv(h), |centre - measured|):")
    for nm, r in allrows:
        print(f"      {nm:>10} n={r['n']:>5}  cv(h)={r['cvh']:.3f}  "
              f"dev={abs(r['centre'] - r['fit']):.3f}")


if __name__ == "__main__":
    main()
