"""Is the auditor's compressed self-report a form to fix or a floor on a
whole family -- and can any truth-free statement beat it?

THE QUESTION. explore_flip_risk.py measured what a membership auditor's
own stated instability is worth. The statement is Phi(-|D-hat| / s) for
a scale s, where D = var_u - var_m/2 - var_n/2 - d^2/4 is the signed
distance from the audited sample's objective level to the half-box cut,
and the event forecast is that a fresh replicate's estimate lands on the
other side of 1/2. That run found the statement COMPRESSED: right in the
mean at one standardized distance and wrong in both directions around
it, decaying like Phi(-mu / sqrt 3) against a truth decaying like
2*Phi(-mu), so the ratio diverges as the audit grows. It also showed the
natural repair -- the plug-in of the exact pair formula -- compresses
into Phi(-mu / sqrt 2), moving the exponent and not the divergence.
That is the whole open half: FORM or FLOOR.

THE HAND-ATTACK (paper, before this engine). It settles the family and
leaves the rival open.

  (1) THE COMPRESSION FORMULA, one line, and it subsumes both numbers on
      record. Write mu = |D| / sigma for the population standardized
      distance, sigma the spread of D-hat. At large mu the auditor's
      mu-hat = |D-hat| / sigma is mu + Z with Z standard normal, the
      absolute value being irrelevant once mu is several sigma. For the
      statement Phi(-mu-hat / s),

          E[ Phi(-(mu + Z) / s) ] = Phi( -mu / sqrt(s^2 + 1) ),

      the exact Gaussian convolution. s = sqrt 2 gives Phi(-mu/sqrt 3)
      and s = 1 gives Phi(-mu/sqrt 2): both figures on record are this
      one identity at two scales, and neither was a property of its
      form.

  (2) SO THE FLOOR IS REAL BUT IT IS A TRADE, NOT A WALL. Any statement
      whose tail decays like exp(-a*x^2/2) has E[f(mu + Z)] decaying
      like exp(-mu^2 * a/(2(1 + a))), and a/(1 + a) < 1 for every finite
      a: the estimation noise strictly flattens the exponent below the
      truth's, for every member, so the ratio to 2*Phi(-mu) diverges.
      The exponent is bought back by SHARPENING -- a -> infinity, s -> 0
      -- and that is a real dial an auditor can turn, needing no truth.
      What it costs is the other end: the same sharpening drives the
      statement to 0 at small mu, where the truth is 1/2. The floor is
      therefore not "every member over-warns at large mu", which a
      sharpened member falsifies outright; it is that NO member is right
      at both ends, the exponent and the small-mu value being one dial.
      This engine turns that dial rather than arguing about it.

  (3) WHICH LEAVES ONE SHAPE WORTH A COLUMN. The pair form
      2*p(1 - p) is 1/2 at mu = 0 by construction, so sharpening it
      moves the large-mu exponent while the small-mu end is pinned by
      the shape rather than by the scale. On the compression formula its
      sharpened version is within a factor of about 2 of the truth at
      BOTH ends of the measured sweep, which no member on record is.
      That is a prediction of the formula and not a measurement.

  (4) THE RIVAL FROM OUTSIDE THE FAMILY IS SPLIT-HALF, and it is outside
      because it reads the event rather than a derivation: cut all three
      samples, run the SAME estimator on each half, and count whether
      the two halves land on opposite sides of 1/2. Cutting only the
      audited sample would leave both halves sharing one G-hat and one
      B-hat, so they stop being independent replicates and the count
      stops estimating the event. Two costs are the subject and not
      incidentals. A half runs at n/2, where mu is smaller by sqrt 2, so
      the raw count answers the question at the wrong size; the BRIDGE
      back to n inverts the normal pair model and re-imports exactly the
      parametric assumption the instrument was chosen to avoid, so
      bridged and unbridged are scored apart. And one split is a single
      Bernoulli, so only rates pooled over re-splits of the auditor's
      own samples read at all -- which is available to a single auditor,
      the way a bootstrap is, and is what makes this a statement rather
      than a coin.

THE TRANSPLANTS, marked. One. The compression formula is derived in the
large-mu regime, where |mu + Z| may be read as mu + Z; it is applied
below across a sweep whose smallest mu is 0.37, where that reading is
wrong and the folded tail contributes. Every prediction that leans on it
at small mu is therefore a transplant from the large-mu derivation and
is marked at the point of use.

THE CELLS AND THE SAMPLES. Unchanged and imported, not re-derived:
explore_flip_risk.py's three cells (W2 = depth (12,3) at pi = 1/5,
W3 = depth (2,8) at pi = 4/5, W4 = the designed cell whose population
vertex sits inside the box at 7/10), its samplers, and its estimator.
The population D and the measured spread of D-hat give the standardized
distance mu each row sits at, which is the axis every prediction below
is written on: about 0.37 / 0.70 / 1.55 at W2, 0.57 / 1.11 / 2.47 at W3,
0.73 / 1.42 / 3.18 at W4, for n = 50 / 200 / 1000.

THE ARMS. Eight, all truth-free, all computed from the same replicate.
Write sd_D for the bootstrap spread of D-hat and sd_A for the
replicate's own fourth-moment plug-in spread of A-hat, both as the
sibling computes them.

  (a) LEGACY: Phi(-|D| / sd_A). The first form written down; carried
      only as the anchor the other columns are read against.
  (c) CORRECTED: Phi(-|D| / (sqrt 2 * sd_D)). The sibling's headline
      form, carried for the same reason.
  (d) DENOMINATOR ONLY: Phi(-|D| / sd_D). The swap without the sqrt 2.
  (e) SQRT 2 ONLY: Phi(-|D| / (sqrt 2 * sd_A)). The sqrt 2 without the
      swap. (d) and (e) are the two one-variable arms the sibling's
      slate did not carry, which is why it could not say which of its
      two corrections earned what.
  (f) PAIR PLUG-IN: 2*p*(1 - p) with p = Phi(-|D| / sd_D). The natural
      guess, derived on the sibling's expectations and never run.
  (g) SHARPENED PAIR: the same with p = Phi(-2|D| / sd_D). The designed
      falsifier of the naive floor, and hand-attack (3)'s candidate.
  (h) SPLIT-HALF, UNBRIDGED: the pooled rate over SPLITS random halvings
      of all three samples, each half scored with the sibling's own
      estimator and the two halves compared across 1/2.
  (i) SPLIT-HALF, BRIDGED: (h) inverted through the normal pair model
      2*Phi(-m)*Phi(m) to a half-size distance m, scaled to m*sqrt 2 for
      the full size, and re-read through the same model.

THE MEASUREMENT. R = 300 replicate PAIRS at each of n = 50, 200, 1000
for each of the three cells, the sibling's shape exactly, so the two
runs' rows are comparable line by line. Per pair: draw replicate 1,
compute all eight arms from it alone; draw replicate 2 independently and
record whether its estimate is on the other side of 1/2. SPLITS = 32
re-splits per replicate.

THE TRAP, measured and not guessed. B-hat = d-hat^2 is exactly 0 in 1
replicate in 23 at n = 25, the size a half runs at when n = 50 -- a
figure measured on this sampler by the sibling and not inherited from
further back. On those halves there is no vertex, the objective is
linear, and the estimator's own guard returns a box endpoint. They are
NEVER filtered: filtering them would hand the split-half instrument the
derivation it exists to avoid. Their share is printed, and the pooled
rate is printed a second time with them dropped, so the cost of letting
them through is read rather than assumed.

PREDICTIONS (fixed before the run).

  PC1  POSITIVE CONTROL, THE BATCH ESTIMATOR. The vectorized estimator
       this engine adds -- needed because the split arms call it 19200
       times per row -- agrees with the sibling's scalar estimator to
       the last bit at every cell and size, on BOTH shapes it is called
       with: 198 one-row calls, and 792 rows inside stacks, each drawn
       replicate being cut into a stack of 4 for the purpose. The stack
       is the shape the split arms actually use and a one-row check does
       not reach it. Read before anything else. A miss means the split
       arms are not running the tool they name.

  PC2  POSITIVE CONTROL, THE CARRIED ARMS. (a) and (c) reproduce the
       sibling's printed means within 0.02 at all nine rows. A miss
       means the cells or the samplers moved and no column is
       comparable to what is on record.

  PR1  THE COMPRESSION FORMULA IS THE LAW, not a fit to one form.
       Observable: at every one of the six world rows, the measured mean
       of each of (a), (c), (d), (e) is within 0.02 of
       Phi(-mu / sqrt(s^2 + 1)) evaluated at that row's own mu and that
       arm's own s, where s is taken from the row's measured mean
       spreads (s = sd_A/sd_D for (a), sqrt 2 for (c), 1 for (d),
       sqrt 2 * sd_A/sd_D for (e)). TRANSPLANT: the formula is a
       large-mu derivation and the smallest rows sit at mu = 0.37, so a
       miss confined to the two smallest-mu rows confirms the transplant
       and not a wrong law; a miss at mu > 1.5 refutes the law itself.

  PR2  THE DIVERGENCE IS THE WHOLE FAMILY. Observable: for each of the
       five plug-in arms (a), (c), (d), (e), (f), the ratio of the
       stated mean to the normal-model pair rate 2*Phi(-mu)*Phi(mu) is
       larger at W3 n = 1000 (mu = 2.47) than at W2 n = 50 (mu = 0.37),
       and exceeds 2 there. The model rather than the realized rate is
       the denominator because a realized rate carries about 0.03 of
       noise, which is the whole quantity at the largest mu; the
       realized rate is printed beside it at every row.

  PR3  THE SHARPENED ARM FALSIFIES THE NAIVE FLOOR AND PAYS FOR IT.
       Observable, both halves: at W3 n = 1000 arm (g)'s ratio to the
       model is below every one of the five ratios in PR2 and below 3;
       and at W2 n = 50 its stated mean is below (f)'s. If the first
       half fails, sharpening does not buy the exponent and the naive
       floor stands; if the second fails, it buys it for free and the
       trade in hand-attack (2) is wrong.

  PR4  THE TWO ONE-VARIABLE ARMS SEPARATE, AND THEY DISAGREE IN SIGN.
       Observable: (e) > (a) at all nine rows -- dividing by a larger
       denominator can only raise the statement -- while (d) - (a) is
       NEGATIVE at all three W2 rows and POSITIVE at all three W3 rows,
       the sign following sd_D against sd_A, which the sibling measured
       narrower at W2 and wider at W3. And at both n = 1000 world rows
       |(e) - (a)| > |(d) - (a)|: the sqrt 2 is the larger of the two
       corrections. A miss on the sign pattern means the swap is not the
       cell-dependent move the sibling's F2 says it is.

  PR5  SPLIT-HALF UNBRIDGED ANSWERS THE WRONG SIZE, and the size is
       exactly n/2. Observable: at the six world rows the mean of (h) is
       within 0.05 of the normal-model pair rate at mu / sqrt 2, and it
       exceeds the realized pair rate at n at the four rows with
       mu > 0.5. This is the cost being priced, not a failure.

  PR6  THE BRIDGE DOES NOT ESCAPE THE FLOOR. Observable: at the two
       largest-mu world rows arm (i)'s ratio to the model exceeds 1.5.
       The instrument is outside the family but the bridge is a smooth
       function of a noisy pooled rate, so hand-attack (2) applies to it
       as well. A ratio at or below 1.5 at both rows kills the floor as
       a claim about truth-free statements in general and leaves it a
       claim about plug-ins only -- which is the outcome that would make
       the instrument worth building.

  PR7  THE DESIGNED CELL, printed and weighed. W4's applicability test
       fires on nearly every replicate, so no arm there has a derivation
       behind it. The split arms read the event directly and touch no
       derivation, so they should degrade least. Observable: at W4 the
       absolute error of (i) against the realized pair rate is below
       that of (c) at at least two of the three sizes. Weighed rather
       than gated: W4's realized rates are the noisiest quantities in
       the run.

  PR8  THE TRAP IS PAID AND NOT FILTERED, printed and weighed. At n = 50
       the share of halves with B-hat exactly 0 is near 1 in 23, and the
       pooled split rate recomputed with those splits dropped differs
       from the reported one by less than 0.02. A larger difference
       means the instrument's number is being set by the degenerate
       halves rather than merely tolerating them.

RUN. This file needs explore_flip_risk.py beside it: the cells, the
samplers and the audit estimator are imported from there rather than
copied, so the two are one program in two files.

python explore_flip_floor.py   (estimate ~60 s; MEASURED 6.0 s, the
estimate 10x high -- 2700 replicate pairs, each with a 150-draw
bootstrap of three samples and 32 re-splits scored in batch; single
process, largest array a 150 x 1000 resample, memory far under the
analysis ceiling.)

FINDINGS (from the printed run below; R = 300 replicate pairs per row,
SPLITS = 32).

F1  THE CONTROLS: PC1 PASS, PC2 SHORT AT ONE ROW OF NINE, and the scope
    of the second is what makes the rest readable. The batch estimator
    equals the scalar one to the last bit on all 200 draws at every
    cell, so the 19200 half-estimates behind each split row are the
    sibling's tool and not a lookalike. The carried arms reproduce the
    sibling's printed means within 0.020 at eight rows and miss at W4
    n = 200 by 0.027 and 0.025 -- both arms at one row, which is one
    event and not two, the two statements being computed from the same
    gaps. It is a different seed and about 3 standard errors of a
    300-replicate mean, at the cell whose spreads are widest; the six
    WORLD rows, which every scored prediction below is read on, all
    pass. Independently of it, F2 pins the same two arms to a derived
    law at 0.023, which is a tighter check than PC2 was.

F2  THE COMPRESSION LAW IS EXACT, AND THE FIGURES ON RECORD WERE ITS
    LARGE-mu READING (rule, derived and confirmed on printed output;
    PR1 FAILED AS ITS FROZEN OBSERVABLE and the law survives, which is
    not the same sentence -- see the paragraph below this one). Every
    arm formed as Phi(-|D-hat| / s) has
    mean E[Phi(-|mu + Z| / s)] -- the folded convolution, evaluated by
    quadrature -- and that value sits within 0.023 of the measured mean
    at all 36 arm-rows: four arms, three cells, three sizes, s sweeping
    0.90 to 1.72. The closed form Phi(-mu / sqrt(s^2 + 1)) is that same
    integral with the absolute value dropped, and the two readings of
    the law converge monotonically in mu: they differ by 0.158 at
    mu = 0.37 and 0.002 at mu = 2.47, so the closed form's own miss
    against measurement runs 0.147 at the smallest mu and under 0.010 at
    both largest-mu rows.
    PR1 WAS FROZEN AGAINST THE CLOSED FORM, so it failed: the bar was
    0.02 at every world row and the closed form misses it at FOUR of the
    six (0.147, 0.092, 0.128, 0.030 at mu = 0.37, 0.70, 0.57, 1.12),
    passing only the two above mu = 1.5. Its transplant clause says a
    miss at mu > 1.5 refutes the law and a miss confined to "the two
    smallest-mu rows" confirms the transplant, and neither branch is
    literally what happened -- the refuting branch stayed empty, and the
    confirming one named two rows where the fold in fact bites at four.
    That clause was frozen without pricing where the absolute value
    stops mattering, which the run now answers: not until mu passes
    about 1.5. So the slate's transplant was real, it was the ONLY thing
    wrong with the closed form, and it was WIDER than the slate guessed;
    the law under its folded reading is refuted nowhere, and that
    evaluation was added after the run and is named as such where it is
    computed. This subsumes both numbers the sibling left: sqrt 3 is
    s = sqrt 2 and sqrt 2 is s = 1, neither a property of its form.
    AND IT HOLDS AT W4, where no derivation covers any replicate: the
    folded law lands within 0.023 there too. What a statement SAYS is
    governed by the law; whether what it says is right is governed by
    the derivation, and the designed cell separates the two.

F3  THE TWO CORRECTIONS SEPARATE, AND THE SIBLING'S HAND-DECOMPOSITION
    HAD THE SIGNS (PR4 pass, all four clauses). The sqrt 2 alone raises
    the statement at all nine rows, as it must. The denominator swap
    alone is NEGATIVE at all three W2 rows (-0.031, -0.030, -0.026) and
    POSITIVE at all three W3 rows (+0.016, +0.017, +0.008), tracking
    sd(D) against sd(A-hat), narrower at W2 and wider at W3. At both
    n = 1000 world rows the sqrt 2 move is the larger: +0.058 against
    -0.026 at W2, +0.031 against +0.008 at W3. So the sqrt 2 is the
    correction that earns the sibling's gain, the swap is a cell-signed
    minority term, and at W2 they fight -- which is the one-variable
    measurement the sibling's slate could not make and the reason its
    hand-attack "both corrections push the same way" was false.

F4  THE FLOOR IS A TRADE, NOT A WALL, and the trade is the headline
    (PR2 pass on the divergence, one clause short on magnitude; PR3 pass
    both halves). Ratio to the normal-model pair rate, smallest mu
    (0.37) against largest (2.47): (a) 0.61 -> 1.78, (c) 0.66 -> 5.11,
    (d) 0.55 -> 2.35, (e) 0.73 -> 4.03, (f) 0.73 -> 3.98. Five of five
    rise, so the divergence is the family and not one form; the frozen
    "exceeds 2 at the largest mu" is met by four and missed by (a) at
    1.78 -- and (a) is the SHARPEST OF THOSE FIVE at that cell, though
    not of the slate, (g) below being sharper still (s = 0.90 against
    1.41 for (c)), so the one arm that misses the bar misses it for the
    reason the trade names. The designed sharpened arm settles it: (g)
    has ratio 0.45 at the smallest mu and 0.79 at the largest WORLD row,
    so it does NOT over-warn at large mu where the model it is scored
    against is the truth -- the naive floor is falsified outright -- and
    it pays exactly where the hand-attack said, stating
    0.205 against a realized 0.457 at mu = 0.37, under-warning by more
    than a factor of two. THE SIX WORLD ROWS ARE THE SCOPE OF THAT
    SENTENCE and W4 does not extend it: (g) reads 4.05 there at
    mu = 3.18, against a model of 0.001 that F8 shows is not the truth
    at that cell, so the row says nothing about over-warning either way.
    Its ratio still climbs with mu, and on the law
    it must: sharpening moves the exponent from mu/sqrt(1 + s^2) toward
    mu but reaches it only at s = 0, where the statement is 0
    everywhere. So no member is right at both ends, and the dial between
    them is one number.

F5  AND THE LEAST-WRONG STATEMENT IS OPTIMISTIC EVERYWHERE, WHICH IS THE
    WRONG SIGN FOR AN AUDIT. Over the six world rows the sharpened arm's
    ratio band is 0.42 to 0.80 against the corrected form's 0.66 to
    5.11: a factor of 1.9 across the sweep against a factor of 7.7, and
    the smallest worst-row error of anything measured. But every one of
    those six ratios is BELOW 1. A statement that is never more than
    2.4x wrong is worth more than one that is right at a single distance
    only if the direction is acceptable, and an instability the auditor
    is told is half its true size fails toward confidence. That is a
    property of the arm and not of the sweep: 2p(1 - p) is pinned at 1/2
    where the truth is 1/2, so sharpening can only push it down.

F6  SPLIT-HALF ANSWERS THE WRONG SIZE AND CARRIES A THIRD COST THE SLATE
    DID NOT NAME (PR5 pass on direction, one row 0.003 outside the
    band). The unbridged rate tracks the normal-model pair rate at
    mu / sqrt 2 -- the half's own distance -- within 0.046 at five of
    six world rows and 0.053 at the sixth, and it exceeds the realized
    rate at n at every row with mu > 0.5 -- FIVE such rows, where the
    slate said four, having named the count before mu was measured -- by
    up to 0.136. The residual
    IS ONE-SIGNED OVER THE BULK AND NOT EVERYWHERE: (h) sits above the
    half-size model by 0.027 to 0.053 at five of the six world rows and
    BELOW it by 0.012 at the sixth -- W3 at n = 1000, where the rate
    itself is 0.066 and the exception is inside this run's own noise.
    Complementary halves of one sample are ANTICORRELATED by
    construction -- a high D-hat in one half forces a low one in the
    other, given the whole -- which inflates the crossing rate above
    what two independent replicates would give. The n/2 bridge and the
    single-Bernoulli cost were priced before the run; this one was not,
    and it is the cost that does not go away with pooling.

F7  THE BRIDGE DOES NOT ESCAPE THE FLOOR, AND IT BEATS THE CORRECTED
    FORM WITHOUT BEATING THE FAMILY (PR6 failed as its frozen
    observable). The
    bar was ratio above 1.5 at both largest-mu world rows: measured 1.44
    at W2 and 2.71 at W3, so the bar is missed at one row by 0.06 while
    the claim it was chosen to test survives -- (i)'s ratio runs
    0.85 / 0.91 / 1.44 at W2 and 0.85 / 1.11 / 2.71 at W3, rising with
    mu at both cells. The instrument is outside the plug-in family, but
    the bridge is a smooth function of a pooled rate that is itself a
    noisy function of the auditor's own sample, so the convolution
    argument reaches it and the divergence survives -- measured across
    three sizes at both cells, argued beyond them, and not proved.
    WHAT IT BUYS IS CENTERING AGAINST ONE RIVAL AND NOT AGAINST THE
    SLATE. (i) is closer to the model than (c) at five of the six world
    rows, band 0.85 to 2.71 against 0.66 to 5.11 -- but it is the
    CLOSEST arm at only three of the six, losing the largest-mu row of
    each cell to (d) and to (g). On the worst row it is 1.71 away from
    the model against the sharpened arm's 0.58, and on the mean of
    |ratio - 1| the two are 0.442 and 0.412. So the honest ranking is
    that the bridge dominates the form the corpus had, and the sharpened
    plug-in still holds the smallest worst case of anything here.

F8  THE DESIGNED CELL IS WHERE THE DERIVATION-FREE INSTRUMENT WINS, AND
    IT WINS BY A LOT (PR7 pass, 3 of 3, weighed). At W4 the
    applicability test fires on nearly every replicate, so no arm has a
    derivation behind it. Absolute error against the realized pair rate,
    (i) against (c): 0.058 against 0.137 at n = 50, 0.000 against 0.090
    at n = 200, 0.016 against 0.043 at n = 1000. The bridged split-half
    is the better instrument at all three sizes, and lands on the
    realized rate at n = 200 to the printed precision.
    THE FROZEN BAR WAS TWO OF THREE AND THAT IS WHAT THE RUN CARRIES.
    The third row is inside its own noise and must not be read as a
    third win: a realized rate of 0.077 from 300 pairs has a standard
    error of 0.015, the two errors it separates differ by 0.027, and the
    sibling measured this same cell and size at 0.047 -- against which
    the comparison REVERSES. The two smaller sizes are decided by gaps
    of 0.079 and 0.090 and are safe; the verdict rests on those.
    AND THE MODEL COLUMN IS NOT THE TRUTH THERE, which is the reading
    trap this cell sets: at W4 n = 1000 the normal-model pair rate is
    0.001 against a realized 0.077, because the level-set law the model
    rests on does not hold at this cell at all. Every ratio printed in
    that row -- 8.58 through 64.15 -- measures the model failing and not
    an arm over-warning, and W4's ratios are not comparable with the
    world cells'. The absolute errors above are, which is why PR7 was
    frozen on those.

F9  THE TRAP IS PAID AND IT COSTS NOTHING (PR8 pass, once its two
    quantities are put in the same units -- the prediction named a share
    of HALVES and the rig prints a share of SPLITS, a split being
    degenerate when EITHER of its halves is). At n = 50, where each half
    runs at 25, a split has a degenerate half -- B-hat exactly 0, no
    vertex, a linear objective -- in 0.078 of splits at W2, which is
    0.040 per half and is the 1 in 23 = 0.043 the prediction asked for;
    the two-half figure would be 0.085 were the halves independent, and
    they are not. It is 0.018 of splits
    at W3 and 0.000 at W4: the 1-in-23 figure is W2's feature
    distribution and does not carry across cells. Dropping those splits
    moves the pooled rate by 0.001 at every row where any occur. They
    are never filtered in the reported number, and the record now shows
    that tolerating them costs nothing rather than assuming it.

F10 WHAT THIS DOES NOT SETTLE, and the two things it hands forward.
    Three cells, one audit tool, scalar window features, R = 300 pairs,
    so a realized rate carries about 0.03 -- which is why every scored
    prediction reads against the model or against another arm, and why
    W4's realized rates are the weakest numbers here. Two open.
    (i) THE SIGN IS NOW THE DESIGN QUESTION. F5 says the bounded arm is
    optimistic everywhere and F7 says the centered one diverges upward;
    nothing measured here is bounded AND conservative. Whether a
    truth-free statement can be bounded on the wrong side only -- never
    below the truth by more than a factor, free to be above -- is a
    different optimization from the one this slate ran, and the
    compression law is enough to attack it on paper before any engine.
    (ii) THE ANTICORRELATION IS FIXABLE AND WAS NOT FIXED. F6's
    one-signed residual comes from cutting one sample into two
    complementary halves. Drawing two DISJOINT subsamples of size n/4
    each, or subsampling with replacement, breaks the constraint at the
    cost of size. Whether the residual is worth the size is one row of
    the same rig.

PRINTED OUTPUT (verbatim). Row 1 per size: n, the standardized distance
mu = |D| / mean sd(D-hat), the normal-model pair rate at that mu, the
realized pair rate, and the eight arm means. Row 2: mean sd(A-hat) and
sd(D-hat), the sibling's printed means for the two carried arms, the
ratios to the model, the model at half size, the pooled split rate with
degenerate halves dropped, and their share. Row 3: the compression law
for the four scalable arms, folded and asymptotic.

CAN ANY TRUTH-FREE STATEMENT BEAT THE COMPRESSION?
PC1 is the gate: the batch estimator must equal the scalar one
to the last bit before any split arm is read.

PC1  batch == scalar on 198 one-row and 792 stacked calls per cell: PASS

== cell W2 = depth (a,b) = (12,3)   pi = 1/5 = 0.2000   population D = 0.0308359
     n     mu  model realiz        a      c      d      e      f      g      h      i
          sdA    sdD  sib_a  sib_c   then ratio to model for a c d e f g i, then split-half extras
    50  0.368  0.459  0.457    0.281  0.305  0.250  0.333  0.334  0.205  0.524  0.392
       0.1018 0.0839  0.261  0.286   ratio  0.61  0.66  0.55  0.73  0.73  0.45  0.85   half-model 0.479  drop0 0.525  zero 0.078
       law a c d e   folded  0.270  0.294  0.239  0.323   asym  0.408  0.416  0.397  0.427
   200  0.704  0.366  0.350    0.247  0.274  0.217  0.302  0.297  0.167  0.473  0.331
       0.0526 0.0438  0.249  0.276   ratio  0.67  0.75  0.59  0.82  0.81  0.46  0.91   half-model 0.427  drop0 0.473  zero 0.004
       law a c d e   folded  0.243  0.269  0.214  0.298   asym  0.326  0.342  0.309  0.361
  1000  1.541  0.116  0.130    0.159  0.186  0.133  0.217  0.188  0.093  0.265  0.167
       0.0240 0.0200  0.144  0.172   ratio  1.38  1.61  1.15  1.88  1.63  0.80  1.44   half-model 0.238  drop0 0.265  zero 0.000
       law a c d e   folded  0.145  0.173  0.119  0.205   asym  0.162  0.187  0.138  0.217

== cell W3 = depth (a,b) = (2,8)   pi = 4/5 = 0.8000   population D = 0.0400000
     n     mu  model realiz        a      c      d      e      f      g      h      i
          sdA    sdD  sib_a  sib_c   then ratio to model for a c d e f g i, then split-half extras
    50  0.567  0.408  0.383    0.209  0.283  0.225  0.266  0.309  0.173  0.488  0.345
       0.0637 0.0705  0.208  0.278   ratio  0.51  0.69  0.55  0.65  0.76  0.42  0.85   half-model 0.451  drop0 0.487  zero 0.018
       law a c d e   folded  0.210  0.281  0.226  0.265   asym  0.337  0.372  0.344  0.363
   200  1.121  0.228  0.253    0.172  0.246  0.189  0.229  0.263  0.140  0.389  0.253
       0.0322 0.0357  0.159  0.228   ratio  0.76  1.08  0.83  1.00  1.15  0.61  1.11   half-model 0.336  drop0 0.389  zero 0.000
       law a c d e   folded  0.153  0.224  0.168  0.207   asym  0.202  0.259  0.214  0.244
  1000  2.465  0.014  0.007    0.024  0.070  0.032  0.055  0.054  0.011  0.066  0.037
       0.0146 0.0162  0.028  0.073   ratio  1.78  5.11  2.35  4.03  3.98  0.79  2.71   half-model 0.078  drop0 0.066  zero 0.000
       law a c d e   folded  0.032  0.076  0.039  0.062   asym  0.033  0.077  0.041  0.064

== cell W4 = designed, vertex inside the box   pi = 3/10 = 0.3000   population D = -0.1200000
     n     mu  model realiz        a      c      d      e      f      g      h      i
          sdA    sdD  sib_a  sib_c   then ratio to model for a c d e f g i, then split-half extras
    50  0.716  0.362  0.383    0.180  0.246  0.190  0.236  0.264  0.141  0.442  0.325
       0.1573 0.1676  0.199  0.263   ratio  0.50  0.68  0.52  0.65  0.73  0.39  0.90   half-model 0.425  drop0 0.442  zero 0.000
       law a c d e   folded  0.203  0.268  0.212  0.258   asym  0.301  0.340  0.306  0.333
   200  1.417  0.144  0.257    0.103  0.167  0.111  0.156  0.166  0.066  0.361  0.257
       0.0795 0.0847  0.130  0.192   ratio  0.71  1.15  0.77  1.08  1.15  0.45  1.78   half-model 0.266  drop0 0.361  zero 0.000
       law a c d e   folded  0.125  0.188  0.133  0.177   asym  0.151  0.207  0.158  0.197
  1000  3.184  0.001  0.077    0.012  0.034  0.014  0.030  0.023  0.006  0.147  0.093
       0.0355 0.0377  0.014  0.036   ratio  8.58 23.78  9.82 20.42 15.92  4.05 64.15   half-model 0.024  drop0 0.147  zero 0.000
       law a c d e   folded  0.010  0.033  0.012  0.028   asym  0.010  0.033  0.012  0.028
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
from fractions import Fraction

import numpy as np

from explore_flip_risk import (
    boot_sds,
    designed_sampler,
    gap_of,
    phi,
    plug_sd_a,
    population,
    smi_labelled,
    stated,
    world_sampler,
)

RNG = np.random.default_rng(20260609)

R_PAIRS = 300
AUDIT_SIZES = (50, 200, 1000)
SPLITS = 32
PC1_PER_SIZE = 66
PC1_STACK = 4
SHARPEN = 2.0

ARMS = ("a", "c", "d", "e", "f", "g", "h", "i")
N_ARMS = len(ARMS)


# --------------------------------------------------- the batch estimator

def smi_batch(fm, fn, fu):
    """The sibling's covariance-matching estimate, over a stack of
    replicates at once.

    Candidate order and the strict-first-wins tie-break are the scalar
    version's, since np.argmin returns the first minimum; PC1 checks the
    two agree to the last bit rather than trusting that reading."""
    d = fn.mean(axis=1) - fm.mean(axis=1)
    bq = d * d
    a_ = fu.var(axis=1) - fm.var(axis=1)
    g_ = fn.var(axis=1) - fm.var(axis=1) + bq

    rows = d.size
    cands = np.full((5, rows), np.nan)
    cands[0] = 0.0
    cands[1] = 1.0
    with np.errstate(divide="ignore", invalid="ignore"):
        has_b = bq > 0.0
        cands[2] = np.where(has_b, g_ / (2.0 * bq), np.nan)
        disc = g_ * g_ - 4.0 * bq * a_
        root = np.sqrt(np.where(disc >= 0.0, disc, np.nan))
        lin = np.where((~has_b) & (np.abs(g_) > 0.0), a_ / g_, np.nan)
        cands[3] = np.where(has_b, (g_ + root) / (2.0 * bq), lin)
        cands[4] = np.where(has_b, (g_ - root) / (2.0 * bq), np.nan)

    ok = np.isfinite(cands) & (cands >= 0.0) & (cands <= 1.0)
    obj = np.where(ok, (a_ - cands * g_ + cands * cands * bq) ** 2, np.inf)
    pick = np.argmin(obj, axis=0)
    return cands[pick, np.arange(rows)], bq


def split_rate(fm, fn, fu, rng, splits=SPLITS):
    """The pooled split-half crossing rate, and the same rate with the
    zero-B-hat halves dropped.

    All THREE samples are cut, so the two halves are independent
    replicates of the whole audit rather than two readings of one pair
    of class samples."""
    n = fm.size
    half = n // 2
    order = np.argsort(rng.random((splits, n)), axis=1)
    lo, hi = order[:, :half], order[:, half:2 * half]

    left, bq_l = smi_batch(fm[lo], fn[lo], fu[lo])
    right, bq_r = smi_batch(fm[hi], fn[hi], fu[hi])
    cross = (left > 0.5) != (right > 0.5)
    clean = (bq_l > 0.0) & (bq_r > 0.0)
    kept = float(np.mean(cross[clean])) if clean.any() else float("nan")
    zero_share = float(np.mean((bq_l <= 0.0) | (bq_r <= 0.0)))
    return float(np.mean(cross)), kept, zero_share


def pair_model(mu):
    """The normal model's pair rate at standardized distance mu."""
    return 2.0 * phi(-mu) * phi(mu)


_QZ = np.linspace(-12.0, 12.0, 240001)
_QW = np.exp(-_QZ * _QZ / 2.0)
_QW /= _QW.sum()
_ERF = np.vectorize(math.erf)


def law_folded(mu, s):
    """E[ Phi(-|mu + Z| / s) ] by quadrature -- the compression law with
    the folded tail KEPT.

    Added after the run, as the check the slate's marked transplant asks
    for: the closed form Phi(-mu/sqrt(s^2 + 1)) drops the absolute value
    and is a large-mu reading, so the question a small-mu miss raises is
    whether the LAW is wrong or only that reading of it."""
    if s <= 0.0:
        return 0.0
    x = np.abs(mu + _QZ) / (s * math.sqrt(2.0))
    return float(np.sum(_QW * 0.5 * (1.0 + _ERF(-x))))


def law_asym(mu, s):
    """The same law's closed form, valid once |mu + Z| may be read as
    mu + Z."""
    return phi(-mu / math.sqrt(s * s + 1.0))


def bridge(rate):
    """Invert the normal pair model at half size, scale the distance to
    full size, and read the model again. The one step that re-imports
    the parametric assumption the split arm avoids."""
    if not math.isfinite(rate) or rate >= 0.5:
        return 0.5
    lo, hi = 0.0, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if pair_model(mid) > rate:
            lo = mid
        else:
            hi = mid
    return pair_model(0.5 * (lo + hi) * math.sqrt(2.0))


# ------------------------------------------------------ the eight arms

def arms_of(fm, fn, fu, n, rng):
    """All eight truth-free statements from one replicate."""
    _, _, _, a_h, g_h, b_h = smi_labelled(fm, fn, fu)
    gap = gap_of(a_h, g_h, b_h)
    sd_a = plug_sd_a(fm, fu, n)
    _, sd_d = boot_sds(fm, fn, fu, rng)
    rt2 = math.sqrt(2.0)

    p_f = stated(gap, sd_d)
    p_g = stated(SHARPEN * gap, sd_d)
    raw, kept, zero = split_rate(fm, fn, fu, rng)

    out = {
        "a": stated(gap, sd_a),
        "c": stated(gap, rt2 * sd_d),
        "d": p_f,
        "e": stated(gap, rt2 * sd_a),
        "f": 2.0 * p_f * (1.0 - p_f),
        "g": 2.0 * p_g * (1.0 - p_g),
        "h": raw,
        "i": bridge(raw),
    }
    return out, sd_a, sd_d, kept, zero


# ---------------------------------------------------------- measurement

def check_batch(draw, rng):
    """PC1: the batch estimator against the scalar one, to the last bit,
    on BOTH shapes it is called with.

    The one-row call is not the path the split arms use -- they hand it a
    stack of PC1_STACK-and-more rows of fancy-indexed sub-samples -- so
    each draw is also cut into a stack and checked row by row. The cut
    consumes no randomness of its own, which is what keeps this control
    from moving the measurement's stream."""
    bad = 0
    for n in AUDIT_SIZES:
        for _ in range(PC1_PER_SIZE):
            fm, fn, fu = draw(n, rng)
            scalar = smi_labelled(fm, fn, fu)[0]
            one = smi_batch(fm[None, :], fn[None, :], fu[None, :])[0][0]
            bad += scalar != one

            h = n // PC1_STACK
            sm = fm[:PC1_STACK * h].reshape(PC1_STACK, h)
            sn = fn[:PC1_STACK * h].reshape(PC1_STACK, h)
            su = fu[:PC1_STACK * h].reshape(PC1_STACK, h)
            stack = smi_batch(sm, sn, su)[0]
            for i in range(PC1_STACK):
                bad += smi_labelled(sm[i], sn[i], su[i])[0] != stack[i]
    return bad == 0


def run_cell(name, draw, pm, pn, pu, pi, sib):
    a_x, g_x, b_x, _ = population(pm, pn, pu, pi)
    pi_f = float(pi)
    half = float(g_x) / 2.0 - float(b_x) / 4.0
    gap_pop = float(a_x) - half

    print(f"\n== cell {name}   pi = {pi} = {pi_f:.4f}"
          f"   population D = {gap_pop:.7f}")
    print(f"{'n':>6} {'mu':>6} {'model':>6} {'realiz':>6}   "
          + " ".join(f"{k:>6}" for k in ARMS))
    print(f"{'':>6} {'sdA':>6} {'sdD':>6} {'sib_a':>6} {'sib_c':>6}"
          f"   then ratio to model for a c d e f g i,"
          f" then split-half extras")

    for idx, n in enumerate(AUDIT_SIZES):
        acc = {k: np.empty(R_PAIRS) for k in ARMS}
        sd_a = np.empty(R_PAIRS)
        sd_d = np.empty(R_PAIRS)
        kept = np.empty(R_PAIRS)
        zero = np.empty(R_PAIRS)
        est1 = np.empty(R_PAIRS)
        est2 = np.empty(R_PAIRS)

        for r in range(R_PAIRS):
            fm, fn, fu = draw(n, RNG)
            vals, sd_a[r], sd_d[r], kept[r], zero[r] = arms_of(
                fm, fn, fu, n, RNG)
            for k in ARMS:
                acc[k][r] = vals[k]
            est1[r] = smi_labelled(fm, fn, fu)[0]
            gm, gn, gu = draw(n, RNG)
            est2[r] = smi_labelled(gm, gn, gu)[0]

        realized = float(np.mean((est1 > 0.5) != (est2 > 0.5)))
        mean_sd_a = float(np.mean(sd_a))
        mean_sd_d = float(np.mean(sd_d))
        mu = abs(gap_pop) / mean_sd_d
        model = pair_model(mu)
        means = {k: float(np.mean(acc[k])) for k in ARMS}
        sib_a, sib_c = sib[idx] if sib else (float("nan"), float("nan"))

        print(f"{n:>6} {mu:>6.3f} {model:>6.3f} {realized:>6.3f}   "
              + " ".join(f"{means[k]:>6.3f}" for k in ARMS))
        ratios = " ".join(f"{means[k] / model:>5.2f}"
                          for k in ("a", "c", "d", "e", "f", "g", "i"))
        print(f"{'':>6} {mean_sd_a:>6.4f} {mean_sd_d:>6.4f}"
              f" {sib_a:>6.3f} {sib_c:>6.3f}   ratio {ratios}"
              f"   half-model {pair_model(mu / math.sqrt(2.0)):.3f}"
              f"  drop0 {float(np.nanmean(kept)):.3f}"
              f"  zero {float(np.mean(zero)):.3f}")
        rho = mean_sd_a / mean_sd_d
        scales = (("a", rho), ("c", math.sqrt(2.0)), ("d", 1.0),
                  ("e", math.sqrt(2.0) * rho))
        fold = " ".join(f"{law_folded(mu, s):>6.3f}" for _, s in scales)
        asym = " ".join(f"{law_asym(mu, s):>6.3f}" for _, s in scales)
        print(f"{'':>6} law a c d e   folded {fold}   asym {asym}")


# The sibling's printed means for arms (a) and (c), for PC2. Source:
# explore_flip_risk.py PRINTED OUTPUT, columns st_a and st_c.
SIB = {
    "W2": ((0.261, 0.286), (0.249, 0.276), (0.144, 0.172)),
    "W3": ((0.208, 0.278), (0.159, 0.228), (0.028, 0.073)),
    "W4": ((0.199, 0.263), (0.130, 0.192), (0.014, 0.036)),
}


def main():
    print("CAN ANY TRUTH-FREE STATEMENT BEAT THE COMPRESSION?")
    print("PC1 is the gate: the batch estimator must equal the scalar one")
    print("to the last bit before any split arm is read.")

    cells = []
    for tag, (a, b) in (("W2", (12, 3)), ("W3", (2, 8))):
        draw, pm, pn, pu, pi = world_sampler(a, b)
        cells.append((tag, f"{tag} = depth (a,b) = ({a},{b})",
                      draw, pm, pn, pu, pi))
    pm4 = {0: Fraction(1, 2), 1: Fraction(1, 4), 2: Fraction(1, 4)}
    pn4 = {0: Fraction(3, 20), 1: Fraction(1, 4),
           2: Fraction(3, 10), 3: Fraction(3, 10)}
    draw, pm, pn, pu, pi = designed_sampler(pm4, pn4, Fraction(3, 10))
    cells.append(("W4", "W4 = designed, vertex inside the box",
                  draw, pm, pn, pu, pi))

    ok = [check_batch(c[2], RNG) for c in cells]
    each = PC1_PER_SIZE * len(AUDIT_SIZES)
    print(f"\nPC1  batch == scalar on {each} one-row and "
          f"{each * PC1_STACK} stacked calls per cell: "
          f"{'PASS' if all(ok) else 'FAIL'}")
    if not ok:
        print("PC1 failed -- nothing below is readable.")
        return

    for tag, label, draw, pm, pn, pu, pi in cells:
        run_cell(label, draw, pm, pn, pu, pi, SIB[tag])


if __name__ == "__main__":
    main()
