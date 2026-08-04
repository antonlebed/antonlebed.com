"""Can a membership auditor state the instability of their own number,
using only what the audit itself hands them?

THE QUESTION. The covariance-matching membership audit minimizes
(A - pi*G + pi^2*B)^2 over pi in [0, 1], where d = mean_n - mean_m,
B = d^2, A = var_u - var_m, G = var_n - var_m + B, computed from a
member-class sample, a non-member-class sample and the audited sample.
explore_flip_level.py settles what its FLIP is: wherever the
replicate's own vertex G/(2B) lies outside [0, 1], the objective's
level A(p) = G*p - B*p^2 is monotone on the box, the estimate is a
monotone continuous function of A-hat alone, and the estimate crosses
1/2 exactly at the level set A-hat = G/2 - B/4. That law is exact and
was broken by none of the 2174 replicates it covers.

Three of the four terms in that cut are computable WITHOUT the truth --
A-hat from the audited sample, G-hat and B-hat from the two class
samples. The fourth, the cut's DIRECTION, turns on whether pi is above
or below 1/2, which is the one thing an auditor does not have. So an
auditor cannot state a directed flip rate. What they CAN state is a
distance in units of a standard error, hence the probability that a
fresh sample's estimate lands on the OTHER SIDE OF 1/2 from the one
they are holding: an instability of their own number, needing no
oracle. That statement is DERIVED and has never been measured, and it
is the question the surrounding corpus keeps asking of every failure it
finds -- could an auditor with no known optimum have seen it coming.

THE HAND-ATTACK (paper, before this engine). Write the whole statement
in one scalar. With h = G/2 - B/4 the half-box cut and

    D = A - h = var_u - var_m/2 - var_n/2 - d^2/4

the signed distance to it, the level-set law says a replicate's
estimate is above 1/2 iff D has one particular sign, the sign depending
on the direction the auditor lacks. Two independent replicates land on
OPPOSITE sides of 1/2 exactly when sign(D1) != sign(D2) -- and that
event does NOT need the direction, both replicates carrying the same
unknown one. So the instability is a statement about the sign of a
single scalar, which is why it survives the missing term. Three things
follow, and the second and third are corrections to the form the
statement was first written in.

  (1) THE DENOMINATOR IS D'S SPREAD, NOT A-hat'S. The distance is
      |D1|, and D is a function of all THREE samples: var_u enters with
      coefficient +1, var_m with -1/2, var_n with -1/2, plus a d^2/4
      term that is itself of order 1/n. The first form of this
      statement divided by sd(A-hat), which is the spread of
      var_u - var_m only -- the right denominator when G and B are held
      at population values, as the derivation that produced the law
      held them, and the wrong one for an auditor who estimates all
      four terms from the same samples. The two are not even
      proportional: var_m enters A-hat and D with opposite signs, so
      the correlations differ in sign as well as size.

  (2) AND THE SPREAD IS PREDICTIVE, WHICH COSTS A FACTOR sqrt(2). The
      auditor holds D1 and asks about D2, not about the population's D.
      With D1 and D2 independent draws of spread sigma, an auditor who
      centers the predictive distribution on their own D1 has
      D2 | D1 ~ spread sigma*sqrt(2), so

          instability = Phi( -|D1| / (sqrt(2) * sigma_D) ).

      Dividing by sigma alone answers a different question -- the
      chance a fresh draw crosses a KNOWN cut at a KNOWN center -- and
      an auditor has neither. Both corrections push the same way: the
      first form UNDERSTATES how unstable the number is.

  (3) WHERE IT HAS NO DERIVATION AT ALL, and this is why the run needs
      a cell built for it. Everything above rests on A(p) being
      monotone on the box, which is the vertex G/(2B) lying outside
      [0, 1]. In terms the design can control that condition reads

          vertex outside the box  <=>  |var_n - var_m| > d^2

      -- the two classes' variances differing by STRICTLY more than the
      square of their mean gap. The boundary is where the test and the
      law come apart, and the direction matters: at equality G is 0 or
      2B exactly and the vertex sits ON a box endpoint, where A is
      still weakly monotone across the box, so the LAW holds while the
      rig's flag (0 <= vertex <= 1) reads the replicate as excluded.
      The applicability test is therefore CONSERVATIVE at its own
      boundary and never permissive, which is the safe direction for
      something an auditor is meant to trust. Neither
      cell in the surrounding corpus
      violates it at the population level, so nothing measured so far
      touches the excluded case. Inside it the level set of A-hat has
      TWO solutions rather than one, the estimate stops being a
      function of A-hat, and a statement built on the sign of one
      scalar has nothing behind it.

THE TRANSPLANTS, marked. Two. The normal reading of sd(A-hat) is
carried here from a POPULATION fourth-moment plug that was verified
against a measured spread (0.10732 against 0.10795); carrying that
accuracy to a PER-REPLICATE plug-in, where the fourth moments are
themselves estimated from the same n that produced A-hat, is the
assumption on trial and not a background fact. And "instability" is
being scored against a pair event, while the corpus's recorded "flip"
rates are marginal rates against the TRUTH -- related by the identity
in PR1(ii) and not the same number.

THE CELLS. Two carried forward and one built.
  W2 = (a, b) = (12, 3), pi = 1/5 and W3 = (2, 8), pi = 4/5: the depth
  world of explore_deletion_ruler.py, menu {2, 3} at every state, the
  audit feature the count of 2-moves in the WINDOW = 3 positions after
  the first, class m = first move 2, class n = first move 3, the
  unconditioned fiber a uniform arrangement. Population moments exact
  hypergeometric: feat_m ~ HG(T-1, a-1, W), feat_n ~ HG(T-1, a, W),
  feat_u ~ HG(T, a, W). Population vertices -0.769 and 1.250, both
  outside the box, so the law covers them.

  W4 = THE DESIGNED CELL, and the coefficients are chosen directly
  rather than hunted for in a world. Class m is (1/2, 1/4, 1/4) on
  {0, 1, 2} and class n is (3/20, 1/4, 3/10, 3/10) on {0, 1, 2, 3},
  giving var_m = 11/16 and var_n = 87/80 against d = 1, so
  |var_n - var_m| = 2/5 < 1 = d^2 and the vertex sits INSIDE the box at
  G/(2B) = 7/10. The audited sample is drawn as a genuine mixture --
  each unit from class n with probability pi, else from class m --
  which is what makes A = G*pi - B*pi^2 hold identically, as it does at
  the two world cells. At pi = 3/10 the exact constants are B = 1,
  G = 7/5, A = 33/100, with A(1) = G - B = 2/5 and the vertex value
  G^2/(4B) = 49/100, so the population objective still has a UNIQUE
  in-box root, and it sits at the truth. The cell is therefore
  identified exactly like the other two: what is different is only that
  A-hat drifting up by 2/25 puts a SECOND root in the box, and the
  half-box cut A(1/2) = 9/20 lies beyond that entry, so the level set
  the whole statement is built on is not reachable without passing
  through the two-root region first.

THE MEASUREMENT. R = 300 replicate PAIRS at each of n = 50, 200, 1000
for each of the three cells. Per pair: draw replicate 1, compute
A-hat, G-hat, B-hat, the estimate and the argmin's source; state the
instability three ways; then draw replicate 2 independently and record
whether its estimate is on the other side of 1/2. The three statements
are

  (a) PLUG-IN, the form first written down: Phi(-|D1| / sd_plug(A-hat))
      with sd_plug from the replicate's OWN fourth moments,
      sqrt(((mu4_u - var_u^2) + (mu4_m - var_m^2)) / n).
  (b) BOOTSTRAP A-hat: the same form with sd(A-hat) from resampling the
      audited and member samples, 150 draws. Isolates whether any miss
      by (a) is the SPREAD or the FORM.
  (c) PREDICTIVE D: Phi(-|D1| / (sqrt(2) * sd_boot(D))), both
      corrections applied, sd(D) from resampling all three samples.

THE TRAP, and it is not hypothetical. B-hat = d-hat^2 is exactly 0 --
d-hat being a difference of means of integer window counts -- at a rate
measured directly on this file's own sampler over 4000 draws per size
at W2: 1 in 23 at n = 25, 1 in 69 at n = 50, about 1 in 2000 at
n = 200, and none in 4000 at n = 1000. (An inherited figure of "1 in 90
at n = 50, none at n >= 200" was carried into an earlier draft of this
docstring and is superseded by that measurement: the event is commoner
than it said at the smallest size and does not vanish at n = 200.) The
n = 25 rate is recorded because it is the size a half-sample instrument
would run at, where one replicate in 23 has no vertex at all.
There is no vertex there, the objective is linear, and any
quantity that divides by B-hat or reads a vertex of infinity is wrong
on exactly the replicates the smallest audit size contributes. The
estimator below keeps the sibling's guard; nothing in the three
statements divides by B-hat at all, D being a plain combination of
variances and one squared mean gap.

PREDICTIONS (fixed before the run).

  PR1  POSITIVE CONTROL, both halves read before anything else.
       (i) The MARGINAL flip rate -- estimate nearer 1 - pi than pi --
       tracks the rates on record for this world, W2 0.385 / 0.280 /
       0.100 and W3 0.295 / 0.130 / 0.010 at n = 50 / 200 / 1000, each
       within 0.07. A miss means the sampler or estimator is not the
       tool being described.
       (ii) The realized PAIR rate equals 2q(1 - q), where q is this
       run's own pooled marginal flip rate over both replicates, within
       0.05 at every row of all three cells -- two independent
       replicates land on opposite sides of 1/2 iff exactly one of them
       flipped. A miss means the pair machinery is not measuring the
       event it names, and no calibration line is readable.

  PR2  THE FIRST FORM UNDERSTATES. Observable: at W2 and W3 the mean
       stated instability from (a) is BELOW the realized pair rate at
       every one of the six rows, and below it by at least 0.05 at
       n = 200 and n = 1000.

  PR3  THE CORRECTED FORM CALIBRATES. Observable: the mean stated
       instability from (c) is within 0.05 of the realized pair rate at
       W2 and W3 for n = 200 and n = 1000. The n = 50 rows are printed
       and weighed rather than gated: the normal reading of this
       estimator is already on record degrading there.

  PR4  THE SPREAD IS NOT WHAT MOVES. Observable: the mean bootstrap
       sd(A-hat) from (b) is within 10 percent of the mean plug-in
       sd(A-hat) from (a) at every row with n >= 200. Together with PR2
       this separates a wrong SPREAD from a wrong FORM: if (a) and (b)
       agree with each other and both miss, the miss is the form.

  PR5  THE DESIGNED CELL MISFIRES, and it is the point of running it
       rather than a second confirmation. Observable: at W4 with
       n = 1000 the mean stated instability from (c) -- the corrected
       form, the one that calibrates elsewhere -- is below the realized
       pair rate by at least 0.10. Hand expectation: |D| = 12/100 sits
       at 3.4 population sd there, sending every stated number to
       nearly 0, while a second root enters the box whenever A-hat
       drifts up by 8/100, which is only 2.0 sd.

  PR6  RELIABILITY, printed and weighed. Stated against realized in
       bins of stated instability, pooled over W2 and W3 and separately
       for W4. The hand-attack expects (c) near the diagonal on the
       world cells and (a) below it. A variant sitting off the diagonal
       in a way that REVERSES between bins is a different failure from
       a uniform shift, and which one it is decides whether the form or
       only its scale is wrong.

  PR7  WHERE THE TIE-BREAK DECIDES, printed and weighed. At W4, among
       replicates with TWO in-box roots, the share whose argmin came
       from the upper root. Both roots zero the objective in exact
       arithmetic, so this share is set by floating-point residue and
       the candidate ORDER, not by the data: near 1/2 says the estimate
       is a coin flip there, near 0 or 1 says the tie-break is
       systematic and the cell carries a bias rather than a variance.

RUN. python explore_flip_risk.py   (estimate ~90 s; MEASURED 3.9 s, the
estimate 23x high -- 2700 replicate pairs, each with a 150-draw
bootstrap of three samples; single process, largest array a 150 x 1000
resample, memory far under the analysis ceiling.)

FINDINGS (from the printed run below; R = 300 replicate pairs per row).

F1  PR1 PASS, both halves, and it is the only reason the rest is
    readable. The marginal flip rate tracks the rates on record within
    0.052 at every row (W2 0.410/0.267/0.077 against 0.385/0.280/0.100,
    W3 0.347/0.140/0.000 against 0.295/0.130/0.010), and the realized
    pair rate tracks 2q(1 - q) within 0.039 at all NINE rows, the
    designed cell included. The pair event is the one named.

F2  THE SPREAD IS SOLVED AND THE FORM IS NOT (PR4 pass, and it is the
    finding that makes every other line diagnosable). The per-replicate
    fourth-moment plug-in -- the assumption explicitly on trial, since
    the accuracy it inherits was verified against POPULATION moments --
    agrees with the bootstrap sd(A-hat) to 1.5 percent at the worst and
    under 0.7 percent at the other eight of the nine rows -- the worst
    being W2 at n = 50, 0.1007 against 0.0992, which is also the row
    where the plug-in sits furthest from the exact population value
    (6.2 percent). Both departures are at the smallest audit size and
    in the same place. So estimating the fourth moments from the same n
    that produced A-hat costs at most a percent and a half of the
    spread, against a form error below that reaches a factor of 5.4
    (W3 at n = 1000, a stated 0.073 against a normal-model 0.013 and a
    realized 0.010), and no miss below can be charged to ESTIMATING the
    spread. Which spread to estimate is a different question and is not
    settled by this paragraph -- that is the next one.
    BUT sd(D) IS NOT sd(A-hat), AND THE CORRECTION HAS NO FIXED SIGN:
    at W2 the gap's spread is NARROWER (0.0199 against 0.0238 at
    n = 1000, 16 percent), at W3 WIDER (0.0162 against 0.0146, 11
    percent). var_m enters A-hat and D with opposite signs, so which
    way the substitution moves is a property of the cell's variances
    and not a constant factor -- hand-attack (1) confirmed, including
    its reason.

F3  PR2 FAILED AS AN OBSERVABLE, AND THE FIRST FORM'S ERROR IS NOT
    ONE-SIGNED. The frozen bar had the plug-in statement below the
    realized pair rate at all six world rows. It is far below at the
    smaller sizes (0.261 against 0.503, 0.249 against 0.427 at W2) and
    ABOVE at n = 1000 in BOTH cells (0.144 against 0.137, 0.028 against
    0.010). So "the first form understates" is false as stated: it
    understates where the number is unstable and overstates where it is
    stable, which is F4's law already visible in the uncorrected form.

F4  THE COMPRESSION LAW, and it is the headline (rule, derived and
    confirmed on printed output). The measured mean of statement (c)
    equals that form's OWN expectation E[Phi(-|mu + Z| / sqrt 2)],
    mu = |D| / sd(D), to within 0.009 at every one of the six world
    rows -- so the rig implements the form and every miss below is the
    FORM. Across those rows mu sweeps 0.37 to 2.47 and the NORMAL-MODEL
    pair rate 2*Phi(-mu)*Phi(mu) sweeps 0.459 down to 0.013, while the
    stated number moves only 0.286 down to 0.073. That model value is
    not itself the measurement and is not treated as one here: the
    REALIZED rate sits above it at five of the six rows, by up to 0.061
    (0.427 against 0.366 at W2 n = 200), and below it only at the
    largest mu (0.010 against 0.013). Both readings give the same
    verdict and the realized one gives it harder, the under-warning at
    small mu being wider against the realized rate than against the
    model. The statement is
    COMPRESSED into a narrow band: it is right IN THE MEAN at mu near 1.1
    alone -- W3 n = 200, stated 0.228 against realized 0.243, and the
    only row where the form and the truth actually agree, 0.226 against
    0.231 -- and it UNDER-warns below that point and OVER-warns above
    it. Asymptotically the stated number decays like
    Phi(-mu / sqrt 3) -- 0.185 and 0.077 against the measured 0.172 and
    0.073 at the two largest mu -- while the truth decays like
    2*Phi(-mu), so the RATIO diverges and the statement becomes
    unboundedly conservative in relative terms as the audit grows. PR3
    is 2 of 4 and its two misses have OPPOSITE signs (W2 n = 200 low by
    0.151, W3 n = 1000 high by 0.063); that opposition is this law and
    not noise. The second row PR3 passes is not a second agreement:
    W2 n = 1000 clears the 0.05 bar against a REALIZED rate of 0.137
    that sits 0.023 above the 0.114 its own mu implies, while the
    stated 0.172 sits 0.058 above it -- so it passes on where the
    realized rate landed and not on the form being right there.
    The cause is exact and not a tuning miss: hand-attack (2)'s
    predictive spread is the Bayes answer under a FLAT prior on D,
    while a fixed cell holds D at a point. (c) beats (a) at five of six
    rows, but WHICH correction earns that is not measured here and the
    run cannot say: (c) changes the denominator and applies the sqrt(2)
    together, so no variant on this slate differs from another in one
    variable. Worse for any attribution, the two do not even push the
    same way. Decomposing the n = 1000 rows by hand: at W2 the swap to
    sd(D) moves the statement -0.037 and the sqrt(2) moves it +0.076 --
    OPPOSITE signs, the sqrt(2) dominating and the net gain smaller
    than either step -- which also refutes the slate's own hand-attack
    (2), where "both corrections push the same way" was asserted and is
    simply false at one of the two world cells. So
    the honest reading is that the PAIR is better centered than (a),
    and separating them needs the two one-variable arms this slate did
    not carry. Either way both buy centering, not calibration.

F5  THE MISSING TERM IS THE SIGN, AND IT IS WHAT THE DIAGRAM SLOPES ON
    (PR6, weighed). Conditional on the replicate in hand the truth is
    not the row's 2p(1 - p) and is not a constant either: it takes
    exactly TWO values. With p = Phi(-mu) the row's flip rate, a second
    replicate differs with probability p when the auditor's own D-hat
    fell on the MAJORITY side of the cut and 1 - p when it fell on the
    minority side -- the sign of D-hat decides, and its MAGNITUDE is
    irrelevant. The auditor's statement is a function of |D-hat| alone,
    which is precisely the coordinate that does not carry the sign; but
    it is not independent of it either, a small |D-hat| being far more
    likely to have come from the minority side. So binning on the
    statement mixes the two conditional values in bin-dependent
    proportions and the diagram must SLOPE. Derived, then checked
    against the row it predicts: at W2 n = 1000 (mu = 1.550, p = 0.061)
    the minority share runs 0.000, 0.004, 0.026, 0.093, 0.301 across the
    five bins and carries the realized rate from 0.061 to 0.325. The
    printed diagram is POOLED over W2, W3 and three sizes, and it slopes
    the same way: stated 0.023 against realized 0.119 in the bottom bin,
    0.423 against 0.461 in the top, monotone in between.
    SO "CALIBRATED" HAS TO BE SAID CAREFULLY, and the strong reading is
    FALSE. A perfectly calibrated forecast of this event as a function
    of |D-hat| DOES exist -- the mixture w(|D-hat|)(1 - p) +
    (1 - w(|D-hat|))p -- so nothing here forbids reliability in
    principle. What it costs is mu, hence D, hence the truth: w and p
    are both unavailable to an auditor. Calibration is an ORACLE's to
    have and not the auditor's, and what a truth-free statement can be
    scored on is the per-row MEAN, which is what PR3 does.

F6  THE DESIGNED CELL: PR5 FAILED AS ITS FROZEN OBSERVABLE AND THE CELL
    ANSWERED A BETTER QUESTION. The bar was statement (c) low by at
    least 0.10 at n = 1000; measured low by 0.011 there, by 0.101 at
    n = 200 and by 0.160 at n = 50. The misfire is real and GROWS AS n
    FALLS, and the frozen row was the one where it is smallest -- the
    observable was chosen against the hand expectation that the stated
    number goes to nearly 0 while the realized rate does not, and the
    realized rate falls with it.
    WHAT THE CELL DOES SHOW IS BETTER THAN A SIZE: the excluded case
    ANNOUNCES ITSELF FROM INSIDE. The population vertex sits at 7/10 by
    construction, and the replicate's own vertex G-hat/(2*B-hat) lies
    in the box for 0.950 / 1.000 / 1.000 of replicates -- a quantity
    needing no truth, so an auditor here can compute that the
    derivation does not cover them. The same check fires on 0.193 /
    0.070 / 0.000 of W2's replicates and 0.293 / 0.080 / 0.000 of W3's,
    where it correctly stands down as n grows. So the statement carries
    its own truth-free applicability test, and that test is what the
    designed cell verifies.
    AND THE ESTIMATE THERE IS A COIN FLIP, NOT A NUMBER (PR7, weighed).
    Two in-box roots occur in 0.203 / 0.237 / 0.063 of W4's replicates,
    and among them the UPPER root wins the argmin 0.475 / 0.507 / 0.421
    of the time. Both roots zero the objective in exact arithmetic, so
    that share is decided by floating-point residue and the candidate
    order -- near one half, hence a variance the audit cannot see and
    not a bias it could correct.

F7  WHAT THIS DOES NOT SETTLE, and the one thing it hands forward.
    Three cells, one audit tool, scalar window features, R = 300 pairs
    -- a per-row rate carries about 0.03 of noise, which is why F4 is
    argued from the form's own expectation rather than from any single
    row. The obvious alternative is the plug-in of the exact pair
    formula itself: 2*p-hat*(1 - p-hat) with
    p-hat = Phi(-|D-hat| / sd(D-hat)), no sqrt 2 and no prior. It is NOT
    a repair, and the reason is worth stating because it is the natural
    guess: p-hat is not unbiased for p either -- |D-hat| carries its own
    spread, so E[p-hat] runs 0.239 against a p of 0.356 at mu = 0.37 and
    0.039 against 0.007 at mu = 2.47, biased DOWN at small mu and UP at
    large, the same crossover shape one level down. Its expectation
    therefore compresses too, into Phi(-mu / sqrt 2) rather than
    Phi(-mu / sqrt 3), so the ratio against 2*Phi(-mu) still diverges
    and only the exponent improves. Derived here, not run: on those
    expectations it beats (c) at four of five mu and ties at the fifth,
    which makes it worth measuring and not worth expecting to fix
    anything. The suspicion it raises is the real handoff -- that EVERY
    statement formed by plugging D-hat into a smooth function of mu
    over-warns at large mu for the same reason, so the compression is a
    FLOOR on this family rather than a form to be corrected, and the
    instrument that beats it will have to come from outside the family.
    It needs no new world: the same three cells and the same drawn
    samples score all of it.

PRINTED OUTPUT (verbatim). Row 1 per size: n, marginal flip rate, the
rate on record, the realized pair rate, 2q(1 - q) from this run's own
pooled flip rate, and the three mean stated instabilities. Row 2: mean
plug-in and bootstrap sd(A-hat), the population sd(A-hat), mean
bootstrap sd(D), the in-box-vertex rate, the two-in-box-root rate, the
upper-root share among those, and the pair rate and statement (c)
restricted to vertex-outside replicates.

THE AUDITOR'S SELF-REPORTED INSTABILITY, scored as a forecast
PR1 is the gate: 'flip' must track 'rec' within 0.07, and 'pair' must track 2q(1-q) within 0.05.

  == cell W2 = depth (a,b) = (12,3)   pi = 1/5 = 0.2000
     A = -0.0159655  G = -0.0706436  B = 0.0459184   vertex = -0.7692   outside the box
     A(1/2) = -0.0468014   D = A - A(1/2) = 0.0308359   identity A == G*pi - B*pi^2: True
       n   flip    rec   pair  2q(1-q)     st_a   st_b   st_c
         sdA_pl sdA_bt sdA_pp   sdD_bt     v_in  2root up|2rt   then pair rate and st_c on vertex-outside only
      50  0.410  0.385  0.503    0.484    0.261  0.258  0.286
         0.1007 0.0992 0.1073   0.0836    0.193  0.000    nan   pair 0.508  st_c 0.288
     200  0.267  0.280  0.427    0.388    0.249  0.248  0.276
         0.0528 0.0525 0.0537   0.0439    0.070  0.000    nan   pair 0.423  st_c 0.281
    1000  0.077  0.100  0.137    0.133    0.144  0.143  0.172
         0.0238 0.0237 0.0240   0.0199    0.000  0.000    nan   pair 0.137  st_c 0.172

  == cell W3 = depth (a,b) = (2,8)   pi = 4/5 = 0.8000
     A = 0.1511111  G = 0.2777778  B = 0.1111111   vertex = 1.2500   outside the box
     A(1/2) = 0.1111111   D = A - A(1/2) = 0.0400000   identity A == G*pi - B*pi^2: True
       n   flip    rec   pair  2q(1-q)     st_a   st_b   st_c
         sdA_pl sdA_bt sdA_pp   sdD_bt     v_in  2root up|2rt   then pair rate and st_c on vertex-outside only
      50  0.347  0.295  0.437    0.452    0.208  0.208  0.278
         0.0630 0.0629 0.0654   0.0699    0.293  0.007  1.000   pair 0.443  st_c 0.291
     200  0.140  0.130  0.243    0.229    0.159  0.158  0.228
         0.0325 0.0323 0.0327   0.0360    0.080  0.000    nan   pair 0.246  st_c 0.230
    1000  0.000  0.010  0.010    0.010    0.028  0.028  0.073
         0.0146 0.0146 0.0146   0.0162    0.000  0.000    nan   pair 0.010  st_c 0.073

  == cell W4 = designed, vertex inside the box   pi = 3/10 = 0.3000
     A = 0.3300000  G = 1.4000000  B = 1.0000000   vertex = 0.7000   INSIDE the box
     A(1/2) = 0.4500000   D = A - A(1/2) = -0.1200000   identity A == G*pi - B*pi^2: True
       n   flip    rec   pair  2q(1-q)     st_a   st_b   st_c
         sdA_pl sdA_bt sdA_pp   sdD_bt     v_in  2root up|2rt   then pair rate and st_c on vertex-outside only
      50  0.287    nan  0.423    0.419    0.199  0.199  0.263
         0.1557 0.1554 0.1587   0.1653    0.950  0.203  0.475   pair 0.600  st_c 0.336
     200  0.183    nan  0.293    0.299    0.130  0.130  0.192
         0.0793 0.0790 0.0793   0.0843    1.000  0.237  0.507   pair nan  st_c nan
    1000  0.027    nan  0.047    0.052    0.014  0.014  0.036
         0.0354 0.0353 0.0355   0.0378    1.000  0.063  0.421   pair nan  st_c nan

  -- reliability, W2 and W3 pooled (bin: count, mean stated a / b / c, realized)
     [0.00,0.05)  n=  312   0.005 / 0.005 / 0.023   realized 0.119
     [0.05,0.15)  n=  414   0.046 / 0.045 / 0.101   realized 0.215
     [0.15,0.25)  n=  317   0.130 / 0.128 / 0.199   realized 0.287
     [0.25,0.35)  n=  312   0.242 / 0.241 / 0.300   realized 0.337
     [0.35,0.50)  n=  445   0.398 / 0.397 / 0.423   realized 0.461

  -- reliability, W4, the designed cell (bin: count, mean stated a / b / c, realized)
     [0.00,0.05)  n=  317   0.001 / 0.001 / 0.015   realized 0.073
     [0.05,0.15)  n=  188   0.027 / 0.025 / 0.094   realized 0.234
     [0.15,0.25)  n=  116   0.100 / 0.101 / 0.196   realized 0.276
     [0.25,0.35)  n=  123   0.215 / 0.214 / 0.299   realized 0.455
     [0.35,0.50)  n=  156   0.382 / 0.382 / 0.421   realized 0.474
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
from fractions import Fraction

import numpy as np

RNG = np.random.default_rng(20260804)

R_PAIRS = 300
AUDIT_SIZES = (50, 200, 1000)
WINDOW = 3
N_BOOT = 150

# Marginal flip rates on record for the depth world, for PR1(i). Source:
# explore_deletion_ruler.py PRINTED OUTPUT, cells (12,3) and (2,8).
RECORDED = {"W2": (0.385, 0.280, 0.100), "W3": (0.295, 0.130, 0.010)}
PC_TOL = 0.07
PAIR_TOL = 0.05

BINS = (0.0, 0.05, 0.15, 0.25, 0.35, 0.5001)


# ------------------------------------------------------- exact moments

def hyper_pmf(big_n, k, draw=WINDOW):
    """Exact pmf of Hypergeometric(N, K, n) as a dict x -> Fraction."""
    def binom(n, r):
        if r < 0 or r > n:
            return 0
        out = 1
        for i in range(r):
            out = out * (n - i) // (i + 1)
        return out
    total = binom(big_n, draw)
    out = {}
    for x in range(0, draw + 1):
        w = binom(k, x) * binom(big_n - k, draw - x)
        if w:
            out[x] = Fraction(w, total)
    return out


def central_moments(pmf):
    """(mean, var, mu4) of a pmf, exact."""
    mean = sum(x * p for x, p in pmf.items())
    var = sum((x - mean) ** 2 * p for x, p in pmf.items())
    mu4 = sum((x - mean) ** 4 * p for x, p in pmf.items())
    return mean, var, mu4


def population(pm, pn, pu, pi):
    """Exact (A, G, B, kurt) from three pmfs and the mixing weight."""
    mean_m, var_m, mu4_m = central_moments(pm)
    mean_n, var_n, _ = central_moments(pn)
    _, var_u, mu4_u = central_moments(pu)
    d = mean_n - mean_m
    bq = d * d
    g_ = var_n - var_m + bq
    a_ = var_u - var_m
    kurt = (mu4_u - var_u * var_u) + (mu4_m - var_m * var_m)
    return a_, g_, bq, kurt


# ------------------------------------------------------- the estimator

def smi_labelled(feat_m, feat_n, feat_u):
    """The covariance-matching point estimate, with the label of the
    candidate the argmin came from and the number of in-box roots.

    Candidate list and the strict-< first-wins tie-break are the
    sibling's (explore_flip_level.py), so the returned estimate is its
    estimate; the in-box root COUNT is the one thing added, since the
    designed cell is the first place two of them can occur."""
    d = float(np.mean(feat_n) - np.mean(feat_m))
    bq = d * d
    a_ = float(np.var(feat_u) - np.var(feat_m))
    g_ = float(np.var(feat_n) - np.var(feat_m)) + bq

    cands = [(0.0, "end0"), (1.0, "end1")]
    n_root = 0
    if bq > 0.0:
        cands.append((g_ / (2.0 * bq), "vert"))
        disc = g_ * g_ - 4.0 * bq * a_
        if disc >= 0.0:
            r = disc ** 0.5
            # At disc == 0 the two roots coincide and an in-box double
            # root would be counted twice here. That is the tangent
            # case, which needs disc to vanish to the last bit and does
            # not occur in any row below; the count is only ever read
            # as ">= 2", so the two-root share is unaffected either way.
            for p, tag in (((g_ + r) / (2.0 * bq), "root+"),
                           ((g_ - r) / (2.0 * bq), "root-")):
                cands.append((p, tag))
                if 0.0 <= p <= 1.0:
                    n_root += 1
    elif abs(g_) > 0.0:
        cands.append((a_ / g_, "root+"))
        if 0.0 <= a_ / g_ <= 1.0:
            n_root += 1

    best, best_f, best_tag = 0.0, None, "end0"
    for p, tag in cands:
        if 0.0 <= p <= 1.0:
            f = (a_ - p * g_ + p * p * bq) ** 2
            if best_f is None or f < best_f:
                best, best_f, best_tag = p, f, tag
    return best, best_tag, n_root, a_, g_, bq


# ---------------------------------------------------------- the worlds

def world_sampler(a, b):
    """The depth world's fiber sampler: window counts of 2-moves in the
    WINDOW positions after the first."""
    t = a + b

    def draw(n, rng):
        def window_counts(twos, total, m):
            keys = rng.random((m, total))
            order = np.argsort(keys, axis=1)
            return (order < twos)[:, :WINDOW].sum(axis=1).astype(float)

        feat_m = window_counts(a - 1, t - 1, n)
        feat_n = window_counts(a, t - 1, n)
        keys = rng.random((n, t))
        order = np.argsort(keys, axis=1)
        feat_u = (order < a)[:, 1:1 + WINDOW].sum(axis=1).astype(float)
        return feat_m, feat_n, feat_u

    pm = hyper_pmf(t - 1, a - 1)
    pn = hyper_pmf(t - 1, a)
    pu = hyper_pmf(t, a)
    return draw, pm, pn, pu, Fraction(b, t)


def designed_sampler(pm, pn, pi):
    """Two chosen classes plus a genuine mixture for the audited
    sample, so A = G*pi - B*pi^2 holds by construction."""
    xs_m = np.array(sorted(pm), dtype=float)
    ps_m = np.array([float(pm[x]) for x in sorted(pm)])
    xs_n = np.array(sorted(pn), dtype=float)
    ps_n = np.array([float(pn[x]) for x in sorted(pn)])
    pi_f = float(pi)

    def draw(n, rng):
        feat_m = rng.choice(xs_m, size=n, p=ps_m)
        feat_n = rng.choice(xs_n, size=n, p=ps_n)
        from_n = rng.random(n) < pi_f
        feat_u = np.where(from_n,
                          rng.choice(xs_n, size=n, p=ps_n),
                          rng.choice(xs_m, size=n, p=ps_m))
        return feat_m, feat_n, feat_u

    support = sorted(set(pm) | set(pn))
    pu = {x: (1 - pi) * pm.get(x, Fraction(0)) + pi * pn.get(x, Fraction(0))
          for x in support}
    return draw, pm, pn, pu, pi


# ------------------------------------------------- the three statements

def gap_of(a_h, g_h, b_h):
    """D = A-hat - (G-hat/2 - B-hat/4), the signed distance to the
    half-box cut. The only quantity the auditor needs the size of."""
    return a_h - (g_h / 2.0 - b_h / 4.0)


def plug_sd_a(feat_m, feat_u, n):
    """sd(A-hat) from the replicate's own fourth moments."""
    out = 0.0
    for f in (feat_u, feat_m):
        v = float(np.var(f))
        mu4 = float(np.mean((f - np.mean(f)) ** 4))
        out += mu4 - v * v
    return math.sqrt(max(out, 0.0) / n)


def boot_sds(feat_m, feat_n, feat_u, rng, n_boot=N_BOOT):
    """Bootstrap spreads of A-hat and of D, resampling within samples."""
    n = feat_m.size
    im = rng.integers(0, n, size=(n_boot, n))
    inn = rng.integers(0, n, size=(n_boot, n))
    iu = rng.integers(0, n, size=(n_boot, n))
    bm, bn, bu = feat_m[im], feat_n[inn], feat_u[iu]
    vm, vn, vu = bm.var(axis=1), bn.var(axis=1), bu.var(axis=1)
    dd = bn.mean(axis=1) - bm.mean(axis=1)
    a_star = vu - vm
    d_star = vu - vm / 2.0 - vn / 2.0 - dd * dd / 4.0
    return float(a_star.std()), float(d_star.std())


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def stated(gap, sd):
    """Phi(-|gap|/sd), guarding a degenerate spread. A spread of 0 with
    a nonzero gap is a claim of certainty; with a zero gap the estimate
    sits exactly on the cut and either side is equally likely."""
    if sd <= 0.0:
        return 0.5 if gap == 0.0 else 0.0
    return phi(-abs(gap) / sd)


# --------------------------------------------------------- measurement

def run_cell(name, draw, pm, pn, pu, pi, recorded=None):
    a_x, g_x, b_x, kurt_x = population(pm, pn, pu, pi)
    pi_f, a_p, g_p, b_p = (float(pi), float(a_x), float(g_x), float(b_x))
    half = g_p / 2.0 - b_p / 4.0
    vertex = g_p / (2.0 * b_p) if b_p > 0 else float("inf")

    print(f"\n== cell {name}   pi = {pi} = {pi_f:.4f}")
    print(f"   A = {a_p:.7f}  G = {g_p:.7f}  B = {b_p:.7f}"
          f"   vertex = {vertex:.4f}"
          f"   {'INSIDE' if 0.0 <= vertex <= 1.0 else 'outside'} the box")
    print(f"   A(1/2) = {half:.7f}   D = A - A(1/2) = {a_p - half:.7f}"
          f"   identity A == G*pi - B*pi^2: "
          f"{a_x == g_x * pi - b_x * pi * pi}")
    print(f"{'n':>6} {'flip':>6} {'rec':>6} {'pair':>6} {'2q(1-q)':>8}"
          f"   {'st_a':>6} {'st_b':>6} {'st_c':>6}")
    print(f"{'':>6} {'sdA_pl':>6} {'sdA_bt':>6} {'sdA_pp':>6} {'sdD_bt':>8}"
          f"   {'v_in':>6} {'2root':>6} {'up|2rt':>6}"
          f"   then pair rate and st_c on vertex-outside only")

    rows = []
    for idx, n in enumerate(AUDIT_SIZES):
        est1 = np.empty(R_PAIRS)
        est2 = np.empty(R_PAIRS)
        st = np.zeros((3, R_PAIRS))
        sd_pl = np.empty(R_PAIRS)
        sd_bt = np.empty(R_PAIRS)
        sd_dt = np.empty(R_PAIRS)
        v_in = np.zeros(R_PAIRS, dtype=bool)
        two_rt = np.zeros(R_PAIRS, dtype=bool)
        up_rt = np.zeros(R_PAIRS, dtype=bool)

        for r in range(R_PAIRS):
            fm, fn, fu = draw(n, RNG)
            p1, tag1, nroot1, a_h, g_h, b_h = smi_labelled(fm, fn, fu)
            gap = gap_of(a_h, g_h, b_h)
            sd_pl[r] = plug_sd_a(fm, fu, n)
            sd_bt[r], sd_dt[r] = boot_sds(fm, fn, fu, RNG)
            st[0, r] = stated(gap, sd_pl[r])
            st[1, r] = stated(gap, sd_bt[r])
            st[2, r] = stated(gap, math.sqrt(2.0) * sd_dt[r])
            # The auditor can see their own vertex, so whether the
            # derivation covers them is knowable at audit time.
            v_in[r] = (0.0 <= g_h / (2.0 * b_h) <= 1.0) if b_h > 0.0 else False
            two_rt[r] = nroot1 >= 2
            up_rt[r] = two_rt[r] and tag1 == "root+"
            est1[r] = p1

            gm, gn, gu = draw(n, RNG)
            est2[r] = smi_labelled(gm, gn, gu)[0]

        # An estimate landing exactly on 1/2 is counted as below it.
        # The box endpoints 0 and 1 are the common argmins and neither
        # is 1/2; a root at exactly 1/2 needs A-hat to hit the half-box
        # cut to the last bit, which no row here produced.
        side1 = est1 > 0.5
        side2 = est2 > 0.5
        pair = side1 != side2
        flip1 = np.abs(est1 - (1.0 - pi_f)) < np.abs(est1 - pi_f)
        flip2 = np.abs(est2 - (1.0 - pi_f)) < np.abs(est2 - pi_f)
        q = float(np.mean(np.concatenate([flip1, flip2])))
        pair_rate = float(np.mean(pair))
        out = ~v_in
        pair_out = float(np.mean(pair[out])) if out.any() else float("nan")
        stc_out = float(np.mean(st[2][out])) if out.any() else float("nan")
        up_share = (float(np.mean(up_rt[two_rt])) if two_rt.any()
                    else float("nan"))
        rec = recorded[idx] if recorded else float("nan")

        print(f"{n:>6} {float(np.mean(flip1)):>6.3f} {rec:>6.3f}"
              f" {pair_rate:>6.3f} {2 * q * (1 - q):>8.3f}   "
              f"{float(np.mean(st[0])):>6.3f} {float(np.mean(st[1])):>6.3f}"
              f" {float(np.mean(st[2])):>6.3f}")
        print(f"{'':>6} {float(np.mean(sd_pl)):>6.4f}"
              f" {float(np.mean(sd_bt)):>6.4f}"
              f" {math.sqrt(float(kurt_x) / n):>6.4f}"
              f" {float(np.mean(sd_dt)):>8.4f}   "
              f"{float(np.mean(v_in)):>6.3f} {float(np.mean(two_rt)):>6.3f}"
              f" {up_share:>6.3f}   pair {pair_out:.3f}  st_c {stc_out:.3f}")
        rows.append((name, n, st, pair))
    return rows


def reliability(rows, title):
    """Stated against realized, binned on the stated number."""
    print(f"\n-- reliability, {title} "
          f"(bin: count, mean stated a / b / c, realized)")
    st = np.concatenate([r[2] for r in rows], axis=1)
    pair = np.concatenate([r[3] for r in rows])
    for lo, hi in zip(BINS[:-1], BINS[1:]):
        sel = (st[2] >= lo) & (st[2] < hi)
        if not sel.any():
            continue
        print(f"   [{lo:.2f},{hi:.2f})  n={int(sel.sum()):>5}"
              f"   {float(np.mean(st[0][sel])):.3f}"
              f" / {float(np.mean(st[1][sel])):.3f}"
              f" / {float(np.mean(st[2][sel])):.3f}"
              f"   realized {float(np.mean(pair[sel])):.3f}")


def main():
    print("THE AUDITOR'S SELF-REPORTED INSTABILITY, scored as a forecast")
    print("PR1 is the gate: 'flip' must track 'rec' within "
          f"{PC_TOL:.2f}, and 'pair' must track 2q(1-q) within "
          f"{PAIR_TOL:.2f}.")

    world = []
    for name, (a, b) in (("W2", (12, 3)), ("W3", (2, 8))):
        draw, pm, pn, pu, pi = world_sampler(a, b)
        world += run_cell(f"{name} = depth (a,b) = ({a},{b})", draw,
                          pm, pn, pu, pi, RECORDED[name])

    pm4 = {0: Fraction(1, 2), 1: Fraction(1, 4), 2: Fraction(1, 4)}
    pn4 = {0: Fraction(3, 20), 1: Fraction(1, 4),
           2: Fraction(3, 10), 3: Fraction(3, 10)}
    draw, pm, pn, pu, pi = designed_sampler(pm4, pn4, Fraction(3, 10))
    designed = run_cell("W4 = designed, vertex inside the box", draw,
                        pm, pn, pu, pi)

    reliability(world, "W2 and W3 pooled")
    reliability(designed, "W4, the designed cell")


if __name__ == "__main__":
    main()
