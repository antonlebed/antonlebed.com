"""DOES THE MEASURED SHARE, USED AS THE MODEL'S OWN DENSITY, ACCOUNT FOR
THE FIRST HIT EXACTLY? -- the paired division: each field's least
principal rank-1 characteristic against a first-hit model built on the
LOCAL principal share at the primes that field actually reads.

THE QUESTION. Two rigs have narrowed one number. explore_real_principal.py
found that the first-hit model at the Chebotarev density 1/(2h)
undershoots the measured L_1 by 1.15x at h = 1 rising to 3.23x at h = 6,
with the coverage floor removed and so unable to be the cause.
explore_principal_share.py then found what the deficit is: the model's
density is ASYMPTOTIC in p while L_1 by construction reads the very
bottom of the range, where the measured principal share of split primes
is 0.332 of nominal at narrow class number 8 rather than the pooled
0.662. That is a lengthening of about 3.0x against a measured undershoot
of 2.27x at wide h = 4, where 81 of the 117 fields carry that narrow
class number.

THAT COMPARISON IS OF ORDERS AND IT IS NOT A DIVISION. It pairs a share
read at one stratification (narrow h+, a prime band) against an
undershoot read at another (wide h, a whole range), it runs in the wrong
direction at wide h = 4 -- 3.0x offered against 2.27x measured, an
OVERSHOOT -- and it never puts one field's own density next to that same
field's own first hit. So the honest statement standing in the corpus is
that the share is the same ORDER as the thing it explains, and that
nothing measured yet requires a second mechanism or rules one out.

This rig performs the division. For each field it builds the first-hit
model on the measured share as a FUNCTION OF p -- a density per prime
rather than a constant 1/h -- integrates it to a predicted L_1 for that
field, and divides the measured L_1 by it. If the ratio sits at 1 across
the class numbers the undershoot is fully priced and the thread closes.
If a residual survives with the local density in hand, it is a real
second effect and the first one this front has that nothing already
measured explains away.

THE SUSPICION IN ITS OWN VOCABULARY. The suspicion is about a DENSITY at
a SCALE, so the model must be one whose density is a function of the
scale, and the statistic it is divided into must be the incumbent's own
L_1 and not a re-definition. Nothing here is a share: the share is the
INPUT. What is compared is a first hit against a first hit.

THE TRANSPLANT, FLAGGED. The expectation that the local density prices
the whole undershoot is imported from a comparison of ORDERS made across
two different stratifications (narrow h+ = 8 and 12 against wide h = 4
and 6), and one of those two orders overshoots. P1 is what that import
commits to; K1 is what refuses it.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) WHAT THE MODEL IS. Fix a field K with wide class number h. Its
      odd split primes below the cap, in order, are p_1 < p_2 < ... The
      incumbent draws every odd prime as a hit with probability 1/(2h)
      -- the 1/2 for splitting and the 1/h for principality. Splitting
      is not what is in question and it is not random: chi_D decides
      it. So the model here runs over the field's OWN split sequence
      and randomizes only principality, at a probability q(p) read from
      the measurement. Then

          P(L_1 = p_i)  =  q(p_i) * prod_{j<i} (1 - q(p_j)),

      and the predicted mean is sum p_i P(L_1 = p_i) divided by the
      mass, which is what conditioning on the hit landing at or below
      the cap means. Setting q = 1/h constant recovers a SHARPENED
      incumbent -- same density, the splitting nuisance removed -- and
      the difference between that and the incumbent's own number is
      model FORM and not density.

  (2) WHERE q(p) COMES FROM, AND WHY IT CANNOT BE THE FIELD'S OWN BITS.
      The roadmap's trap (2) asks for the same field at the same prime
      scale. The scale half is met by binning: q is read from the bin p
      falls in, on frozen geometric edges about three and a half to the
      decade, so a share pooled over 1-1000 is never fed to a model
      hitting at p ~ 30. The field half CANNOT be met literally and the
      reason is fatal rather than technical: a single field's own share
      at its own primes IS its principality bit sequence, and the first
      hit read off it is the measurement itself. The model would predict
      L_1 from L_1. So q is pooled over the field's STRATUM -- fields of
      the same wide class number -- and computed LEAVE-ONE-OUT, with the
      field's own split count and own hit count subtracted from the
      stratum totals in each bin. That is the finest resolution at which
      this question is a prediction at all, and the fact that it is
      forced is part of the finding rather than a compromise in it.

      A cell can empty: a thin stratum whose only split prime in some
      bin belongs to the field being left out leaves no denominator. The
      convention is q = 0 there, and the COUNT of such cells is printed
      rather than buried, because the convention is not neutral -- it
      forbids a hit where the data are silent and so pushes the
      prediction LATE, which is the direction the residual runs. What
      makes it safe is not the count being small but C3b sharing it: the
      reference regenerates under the full share and is then read by
      this same leave-one-out, empty cells and all, so whatever the
      convention costs is inside the number every ratio is compared to.

  (3) THE MARGIN TO DISTRUST IS THE ONE THIS CREATES. The predicted mean
      is a convex function of the small early q's -- roughly 1/q in the
      bottom bins -- so NOISE in the leave-one-out share INFLATES the
      predicted L_1 on average, which pushes the ratio measured/predicted
      DOWN toward and below 1. A ratio at 1 is therefore not
      self-certifying: it could be a real residual cancelled by the
      pipeline's own small-sample bias. C3 measures that bias directly by
      running the entire pipeline on a population where the constant
      model is true by construction, and every printed ratio is read
      against what C3 prints and not against 1.

  (4) THE PIN AT h = 1, WHICH IS AN IDENTITY AND NOT A STATISTIC. At
      wide h = 1 every split prime is principal, so every bin's share is
      exactly 1 at every field, the leave-one-out share is exactly 1
      too, and the model puts probability 1 on the FIRST split prime.
      Predicted L_1 must equal measured L_1 at every one of those fields
      individually, not on average. Any binning apparatus that shows a
      p-dependence there is broken before it is read. This also settles
      what the incumbent's 1.15x at h = 1 was: there is no density
      deficit available at h = 1, so that 1.15 is model FORM -- the
      geometric draw over all odd primes against the actual split
      sequence -- and derivation (1)'s sharpened constant model must
      read 1.00 there.

  (5) THE CENSORING IS ON BOTH SIDES OR THE COMPARISON IS VOID. The
      measurement drops fields whose L_1 exceeds the cap. The model must
      condition on the same event, which is the division by the mass in
      (1). Both are printed, including the mass itself, so a stratum
      where the conditioning is doing real work is visible rather than
      inferred.

  (6) ODD CHARACTERISTICS THROUGHOUT. p = 2 is the budget inequality's
      and is not part of L_1; including it would measure a different
      quantity and compare it to this one. Both prior rigs had to be
      re-run over exactly this.

  (7) THE IMAGINARY SIDE COMES FOR FREE AND TESTS SOMETHING ELSE. There
      the coverage floor makes the share identically ZERO below |D|/4.
      A model reading the local share therefore prices the floor too,
      having been told nothing about |D| -- provided the stratum's
      fields share a floor closely enough for the pooled share to mean
      anything, which is why the imaginary strata are cut by (h, |D|
      band) and the real ones are not. That is a second, independent
      demand on the same machinery: one mechanism the corpus derived
      from arithmetic and one it could not explain, both priced by the
      same measured density.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. THE DIVISION CLOSES. With the local density in hand, the ratio of
      measured mean L_1 to predicted mean L_1 sits within 0.15 of 1 at
      every wide class number carrying at least 5 fields -- against the
      incumbent's 1.15 rising to 3.23.

  P2. THE PAIRED READ AGREES, NOT ONLY THE MEANS. The mean over each
      stratum of the model's own probability integral transform at the
      measured L_1 -- P(model L_1 < measured) + half P(equal), divided
      by the mass -- sits in [0.45, 0.55]. A model can match means and
      still have the wrong shape; this is the reading that sees it.

  P3. THE RESIDUAL HAS NO TREND IN h. Whatever P1's ratios are, they do
      not climb or fall monotonically across the class numbers. The
      incumbent's did climb, and a surviving trend is what a second
      mechanism graded by the class number would look like.

  P4. THE h = 1 RESIDUAL IS MODEL FORM. The sharpened constant model of
      derivation (1) -- q = 1/h over the field's own split sequence --
      reads 1.00 at h = 1, where the incumbent read 1.15.

  P5. THE SAME MODEL PRICES THE IMAGINARY FLOOR. On the imaginary side,
      with strata cut by (h, |D| band), the ratio sits within 0.15 of 1
      as well, the floor entering only as a share of zero in the bins
      below it and nothing about |D| reaching the model.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, read after the
controls and never before.

  K1 kills P1: the printed per-h column "ratio" on the real side. Any
     stratum of at least 5 fields whose ratio differs from 1 by more
     than 0.15, once C3's own offset at that h is subtracted, kills it
     at that h.

  K2 kills P2: the printed per-h column "PIT". Any stratum of at least
     5 fields outside [0.45, 0.55] after C3's offset kills it there.

  K3 kills P3: the same "ratio" column read top to bottom. A run across
     h = 2..8 monotone in one direction, of total span above 0.15,
     kills it.

  K4 kills P4: the printed h = 1 row of the sharpened constant model.

  K5 kills P5: the printed per-(h, |D| band) ratio on the imaginary
     side.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. THE IDENTITY AT h = 1. Derivation (4): predicted L_1 equals
      measured L_1 at every individual wide-h = 1 field. Printed as the
      maximum absolute difference over those fields, which must be
      exactly 0, and as the count of fields it ran over.

  C2. THE INCUMBENT REGRESSION. The constant model at density 1/(2h)
      over all odd primes to 1000, on the same population (real
      fundamental discriminants to 4000, strata of at least 5, fields
      with L_1 <= 1000), must reproduce explore_real_principal.py's
      printed ratios 1.15, 1.68, 2.11, 2.27, 1.89, 3.23, 3.21, 2.81 at
      h = 1..8. A new rig that disagrees with the incumbent on the
      incumbent's own statistic is wrong until shown otherwise.

  C3. THE SYNTHETIC NULL, WHICH IS WHAT EVERY RATIO IS READ AGAINST.
      Replace every field's principality bits by independent draws at
      the constant probability 1/h on that field's own split primes,
      and run the ENTIRE pipeline -- leave-one-out shares, per-field
      model, division -- on the result. The constant model is true
      there by construction, so the printed ratio and PIT are the
      pipeline's own bias at each h, from the binning, the pooling and
      the convexity of derivation (3). Read as an OFFSET and not as a
      pass/fail: it is subtracted from K1 and K2 rather than compared
      to a tolerance.

  C4. LEAVE-ONE-OUT INTEGRITY. For a sample of fields the share is
      recomputed independently over the stratum with that field gone,
      and compared against the subtraction. Printed as a mismatch
      count, which must be 0. The subtraction is the whole reason the
      model is a prediction; an error there would make it a fit.

  C5. THE SPLIT SEQUENCE AGAINST THE INCUMBENT. The measured L_1 and
      the class data come from explore_principal_share.py's own tested
      routines, imported rather than re-implemented. What is checked
      here is the one thing this rig adds to them: that the least
      principal split prime equals the imported L_1 at every field, on
      both signs, printed as a mismatch count.

THE FOLLOW-UP SLATE -- frozen AFTER the first five kills printed and
BEFORE the second engine, and flagged as post-hoc for that reason.

  WHAT THE FIRST ENGINE LEFT. The division does not leave the incumbent's
  undershoot: it flips it. With the local density in hand the model runs
  10-30% LATE rather than 100-220% early, and flat in h. There is one
  mechanism available for a residual of exactly that sign and it is the
  pipeline's, not the arithmetic's. The stratum's fields do not share one
  density: a pooled q is a MIXTURE read as a constant, the mixture's
  first-hit distribution is heavier in BOTH tails than the constant's, and
  the cap cuts the late tail out of the MEASUREMENT -- a field with
  L_1 > 1000 leaves the measured mean entirely -- while the model, run at
  the pooled q, believes it has almost no late tail to lose (its mass sits
  at 0.999). So the measured mean is trimmed and the predicted one is not,
  and the ratio falls below 1 for a reason that has nothing to do with the
  share.

  P7. THE MEASUREMENT DROPS MORE THAN THE MODEL EXPECTS. At every stratum
      carrying a residual, the observed drop rate -- fields with no
      principal split prime below the cap -- exceeds the model's own mean
      1 - mass.

  P8. THE RESIDUAL SHRINKS WHEN THE CAP RISES. Rerun at cap 10000, where
      the drop rate is far smaller: the ratios move toward 1 and the PITs
      toward 0.5 at every stratum of at least 5 fields.

  K7 kills P7: the printed "drop obs" and "drop mdl" columns. A stratum
     with a residual below 1 and an observed drop no larger than the
     model's kills it there.

  K8 kills P8: the printed two-cap table. A ratio no nearer 1 at the
     higher cap kills it at that stratum.

THE THIRD SLATE -- frozen after P7 and P8 printed and BEFORE the
reference engine, and post-hoc for the same reason.

  WHAT KILLED THEM. The observed drop rate is 0.000 at every real
  stratum through h = 8: every field there has a principal split prime
  below 1000, so there is no censoring for a mixture to interact with,
  and raising the cap to 10000 moves no ratio. The residual is not the
  cap and the second slate's mechanism is refuted rather than
  unsupported.

  So what remains is to decide whether the residual is a residual at
  all. C3's single draw cannot say: one synthetic realization carries
  the same sampling error as the data it is grading. The instrument is
  a REFERENCE DISTRIBUTION -- regenerate the bits under the local-share
  model itself, R times, and run the whole pipeline on each. Under that
  null the model is exactly right by construction, so where the
  observed ratio falls in the printed spread is the verdict on P1 and
  needs no tolerance chosen by hand.

  P9. THE RESIDUAL IS REAL AND NOT THE PIPELINE'S. At the two strata
      with enough fields to read -- h = 2 with 392 and h = 4 with 117 --
      the observed ratio sits below the 5th percentile of that
      reference.

  K9 kills P9: the printed percentile of the observed ratio within the
     reference, per stratum. A percentile above 5 kills it there, and
     the residual is sampling.

THE FOURTH SLATE -- frozen after P9 printed and BEFORE its two engines.
Post-hoc, and the last of them.

  WHAT SURVIVED, AND ITS SIGN. The residual is real and it points the
  OTHER WAY from the incumbent's: fields hit EARLIER than their own
  stratum's measured local density says. Two things can produce that and
  they are told apart by two cheap prints.

  The first is the instrument. The share is read on frozen bins, and a
  bin is a claim that the density is constant across it. Halving the
  bins tests it.

  The second is arithmetic, and it is the interesting one. A first
  arrival's mean is not set by the rate alone: for an INDEPENDENT
  sequence at rate q it sits at 1/q, but for a perfectly REGULAR one at
  the same rate it sits at 1/(2q), the first arrival being uniform over
  one spacing. Anything under-dispersed relative to independence lands
  between. So a first hit arriving 10-30% early at a measured rate is
  the signature of principal primes spaced more EVENLY than chance --
  the class group equidistributing over primes with less than the
  fluctuation an independent draw would give. That is a statement about
  a COUNT and not about a first hit, so it is testable without the model
  at all: the index of dispersion of the number of principal split
  primes below the cap, each field against its own local density.

  PA. THE RESIDUAL IS NOT THE BIN RESOLUTION. At bins twice as fine --
       about seven to the decade rather than three and a half -- the
       observed ratio at h = 2 and h = 4 still sits below the 5th
       percentile of the reference regenerated on those same bins.

  PB. THE PRINCIPAL PRIMES ARE UNDER-DISPERSED. The index of
       dispersion -- sum over fields of (count - expected)^2 divided by
       the sum of the local model's own variances -- sits BELOW 1 at
       the strata carrying the residual, and below the reference
       distribution's own value, which is 1 by construction.

  KA kills PA: the printed fine-bin percentile.

  KB kills PB: the printed per-stratum index of dispersion beside the
      reference's. An index at or above the reference kills it, and the
      residual's mechanism is not the spacing.

RESOURCE. Pure integer arithmetic plus per-field float accumulation, no
numpy, no arrays held beyond one principal cycle per field and one
stratum's bin counters. Odd primes to 1000, real and imaginary
fundamental discriminants to 4000; the follow-up re-sweeps the real side
to 10000. Well under 512MB; wall-clock is the open quantity and is
printed.

THE FINDINGS.

  F1. THE LOCAL DENSITY PRICES THE WHOLE UNDERSHOOT AND OVERSHOOTS IT
      (observation, 1216 real fields, 8 class numbers; P1 KILLED, but
      by the far side). Measured mean L_1 against the model built on
      the field's own stratum's local share, and against the same model
      run at the constant 1/h for comparison:

          h    n     measured   constant   ratio      local   ratio
           1  583         6.1        6.1   1.000        6.1   1.000
           2  392        19.3       14.7   1.321       22.4   0.865
           3   52        39.9       18.4   2.172       45.0   0.887
           4  117        61.2       30.7   1.994       76.4   0.802
           5   17        67.1       33.2   2.022       94.0   0.714
           6   27       143.7       44.6   3.223      160.3   0.896
           7    6       173.0       55.0   3.143      187.2   0.924
           8   14       178.6       66.0   2.705      212.4   0.841

      The incumbent's undershoot of 1.15x to 3.23x is not reduced by
      the local density, it is REVERSED: with the measured share in
      hand the model runs LATE, by 8% of the measured mean at h = 7
      to 29% at h = 5. So the answer to the question
      the roadmap asked -- does the share account for the first hit
      exactly -- is no in a direction nobody had named. The share is
      not merely the same ORDER as the undershoot, it is slightly
      MORE than it.

  F2. AND THE RESIDUAL IS FLAT IN h, WHICH IS THE FINDING THAT CLOSES
      THE OLD QUESTION (pattern; P3 SURVIVES). The ratios above run
      0.865, 0.887, 0.802, 0.714, 0.896, 0.924, 0.841 across h = 2..8,
      and flatness is measured rather than eyeballed: regressing the
      ratio on h with each stratum weighted by 1/sd^2 of its own
      reference gives a slope of -0.0049 +/- 0.0141 (z = -0.34) about a
      weighted mean of 0.849, with a chi^2 of 2.64 on 6 degrees of
      freedom -- a constant fits the seven strata better than their
      error bars demand. The same regression on the constant model,
      which is the contrast, gives +0.3199 +/- 0.0141 (z = +22.6) and a
      chi^2 of 634. That climb was the whole evidence for "a second
      mechanism graded by the class number". The grading is gone. What
      is left is not graded by h and so is not that mechanism, whatever
      else it is.

  F3. THE INCUMBENT'S RESIDUAL AT h = 1 WAS MODEL FORM (observation;
      P4 SURVIVES). At h = 1 there is no density deficit available --
      every split prime is principal -- yet the incumbent read 1.15
      there. Running the same constant density 1/h over the field's
      OWN split sequence rather than as a geometric draw over all odd
      primes reads exactly 1.000. So that 1.15 was the 1/2 in 1/(2h)
      standing in for the actual splitting pattern, and nothing else.
      It is the one part of the old undershoot that was never
      arithmetic at all.

  F4. THE RESIDUAL IS REAL AND IT IS NOT THE INSTRUMENT (observation;
      P9 and PA SURVIVE, P7 and P8 KILLED). Four ways it was attacked
      and none of them takes it:

        - CENSORING. The observed drop rate is 0.000 at every real
          stratum through h = 8 -- all 1208 fields those strata hold
          have a principal split prime below 1000 -- so there is no
          truncation for a mixture to interact with. P7 dies on its own
          print. The population is 1216 and exactly ONE field of it is
          uncovered at this cap; it sits in one of the six strata under
          the minimum of 5 that no table here prints.
        - THE CAP. Raised to 10000 the ratios read 1.000, 0.865, 0.887,
          0.802, 0.714, 0.896, 0.923, 0.837 -- the same numbers. P8
          dies with it.
        - THE PIPELINE. Regenerating the bits under the local-share
          model itself and running the whole pipeline 60 times gives a
          reference mean of 0.998 at h = 2 and 0.993 at h = 4, so the
          binning, the pooling and the convexity of derivation (3) are
          worth under 1%. The observed 0.865 and 0.802 sit at z =
          -3.95 and -4.29, with 0 of 60 replicates below either. The
          thin strata say nothing either way (h = 7 sits at the 53rd
          percentile on 6 fields).
        - THE BIN RESOLUTION. At bins twice as fine, about seven to the
          decade, the same two strata read 0.863 and 0.808 against a
          reference of 0.993 and 0.997, still 0 of 60 below.

      The PIT agrees and is the shape reading rather than the mean one:
      0.457 and 0.464 where the model would give 0.500, against the
      incumbent constant model's 0.644 and 0.789.

  F5. THE PRINCIPAL PRIMES ARE UNDER-DISPERSED, WHICH IS THE RIGHT
      SIGN AND HAS TO BE READ AT THE RIGHT SCALE (observation; PB
      SURVIVES, with its size unestablished). A first arrival's mean is
      not fixed by the rate: independent draws at rate q give 1/q,
      perfectly regular ones give 1/(2q). So an early first hit at a
      measured rate is what more-even-than-chance spacing looks like,
      and that is a claim about a COUNT, testable without the model.
      The index of dispersion of the number of principal split primes
      per field, each against its own local density, with the same 60
      replicates as the reference:

          h      to 1000    ref      z        to 100    ref      z
           2       0.142   1.005  -11.77       0.386   1.007   -9.20
           3       0.322   0.998   -3.52       0.550   1.015   -2.16
           4       0.314   1.027   -4.77       0.655   1.026   -2.33
           5       0.190   1.023   -2.10       0.674   1.109   -1.14
           6       0.298   1.022   -2.78       1.054   1.022    0.15
           7       0.205   1.265   -1.40       1.200   1.348   -0.40
           8       0.312   1.198   -1.66       0.873   1.159   -0.81

      Counted to 1000 -- which is PB's own frozen observable -- the
      variance is a seventh to a third of what independence gives, at
      every stratum, and that is what PB survives on.

      BUT THE SCALE MATTERS AND IT IS THE SAME TRAP THIS WHOLE FRONT
      TURNED ON, so the second pair of columns was added after PB was
      frozen and is weaker in exactly the way a post-hoc reading should
      be reported as. Interpolating naively between the regular and
      independent limits, an index of 0.14 would buy a ratio near 0.57
      against a measured 0.865, which is what says the cap-wide reading
      is the wrong scale. Over the bottom decade where L_1 actually
      lives the index is 0.386 at h = 2 and 0.655 at h = 4 -- present,
      weaker, and of a size that no longer contradicts a 13-20% early
      arrival. It is NOT present everywhere there: h = 6 reads 1.054
      against a reference of 1.022, which is KB's kill on that column
      at that stratum, and h = 7 reads above 1 as well though below its
      own reference. Two of the seven strata therefore show no
      bottom-decade under-dispersion at all, and they are small ones
      (27 and 6 fields) whose z is inside 0.5 either way. So the
      mechanism is established in SIGN at the cap-wide scale, MIXED at
      the scale that matters with the two large strata carrying it and
      two small ones not, and its SIZE is not established at either:
      nothing here derives 0.865 from 0.386, and that derivation is
      what would close it.

  F6. THE FLOOR IS PRICED ONLY AS SHARPLY AS A STRATUM SHARES ONE
      (observation, 1217 imaginary fields; P5 KILLED, and killed in the
      cleanest band rather than only at the top). Told nothing about
      |D|, the model prices the coverage floor purely as a measured
      share of zero below it, and one half of that works: where the
      measurement loses fields to the cap the model loses about as many
      (0.273 observed against 0.206 predicted at h = 20 in the second
      band, 0.333 against 0.364 in the fourth).

      The RATIO does not sit at 1. In the |D| <= 1000 band it runs
      1.000, 1.213, 1.437, 1.121, 1.067, 0.964, 1.178, 0.897 at
      h = 1..8 -- median 1.12, five of the eight above 1, three of them
      outside P5's own 0.15. So P5 fails where the floor is SMALLEST,
      not only where it is largest. Across the bands at fixed h the
      ratio then climbs in most strata (h = 8: 0.897, 1.118, 1.163,
      1.346; h = 6 and h = 16 are the exceptions), reaching 1.25-1.35
      in the top band.

      The SIGN is the tell and derivation (7) named it in advance. The
      floor sits at |D|/4, so a band 1000 wide spreads a stratum's
      floors over 250; pooling them hands some fields a nonzero share
      at primes below their OWN floor, the model hits where that field
      cannot, and the measured first hit lands LATE of the prediction.
      Ratio above 1, growing with the spread. That is the OPPOSITE sign
      from the real side's residual, and it is a property of the
      stratification rather than a second phenomenon -- which is also
      why the imaginary side is not evidence for or against F5.

RUN RECORD: wall ~23 s, 1216 real and 1217 imaginary fundamental
discriminants, odd primes to 1000 with the follow-up re-sweeping the
real side to 10000, 60 replicates for each of the two reference
distributions, pure integer arithmetic with per-field float
accumulation, and K3's flatness regression over the printed ratios. All five controls green and read first -- C5 found the
least principal split prime equal to the imported L_1 at all 2433
fields of both signs; C1 found predicted equal to measured EXACTLY at
all 583 wide-h = 1 fields; C2 reproduced explore_real_principal.py's
1.15, 1.68, 2.11, 2.27, 1.89, 3.23, 3.21, 2.81 at h = 1..8 to two
decimals on every stratum; C4 found the leave-one-out subtraction equal
to a from-scratch recomputation at all 10 strata sampled; and C3a found
the pipeline unbiased under the incumbent's own constant density, mean
0.997 at h = 2 and 0.998 at h = 4 over 60 replicates. Six measurements
are POST-HOC and say so where they are printed: P7 and P8 were frozen
after the first five kills, P9 after those two, and PA, PB and the
two-scale reading of PB after P9 -- each before its own engine, and
the frozen tables keep the edges they were written against.
"""

import sys
import time
from math import isqrt
from random import Random

import explore_principal_share as ps


# ------------------------------------------------------------------ frozen

CAP = 1000                      # the incumbent's cap, so C2 is a regression
DBOUND = 4000                   # the incumbent's population
MIN_FIELDS = 5                  # the incumbent's stratum cut
SEED = 1729                     # C3's draws, fixed so the run reproduces

# Geometric bin edges, about three and a half to the decade, half-open
# [lo, hi). Frozen before the engine. The bottom bins are the ones L_1
# actually lives in -- 94.2% of first hits land at or below 100 -- so the
# resolution is placed there and the top of the range is left coarse.
BIN_EDGES = [3, 6, 10, 18, 32, 56, 100, 178, 316, 562, CAP + 1]
# The follow-up's higher cap, the same edges continued at the same rate.
CAP_HI = 10000
BIN_EDGES_HI = BIN_EDGES[:-1] + [1000, 1778, 3162, 5623, CAP_HI + 1]
# PA's resolution test: about seven to the decade rather than three and
# a half, on the same range.
BIN_EDGES_FINE = [3, 4, 6, 8, 11, 16, 22, 30, 42, 58, 80, 111, 155, 215,
                  298, 415, 576, 800, CAP + 1]
NBINS = len(BIN_EDGES) - 1

# The imaginary side's strata are cut by |D| as well as by h, because the
# floor at |D|/4 is a property of the field and a stratum pooling fields
# with different floors pools different densities.
DBANDS = [1000, 2000, 3000, 4000]


def bin_of(p, edges=None):
    e = edges or BIN_EDGES
    for i in range(len(e) - 1):
        if p < e[i + 1]:
            return i
    raise ValueError(p)


# ------------------------------------------------------------- the fields

def real_fields(plist):
    """Per field: wide h, narrow h+, the odd split sequence with a wide
    principality bit on each, and L_1 = the least prime carrying one."""
    out = []
    for D in ps.fundamental_discriminants(0, DBOUND, +1):
        rt = isqrt(D)
        if rt * rt == D:        # D = 1 is not a field; the form machinery
            continue            # divides by zero on it
        h, hplus, neps = ps.class_data_real(D, rt)
        prin = set(ps.principal_cycle(D, rt))
        splits, L1 = [], None
        for p in plist:
            if ps.kronecker(D, p) != 1:
                continue
            b = ps.form_at(D, p)
            _, wide = ps.principal_real(D, p, b, prin, rt)
            splits.append((p, wide))
            if wide and L1 is None:
                L1 = p
        out.append({"D": D, "h": h, "hplus": hplus, "neps": neps,
                    "splits": splits, "L1": L1, "key": h})
    return out


def imag_fields(plist):
    out = []
    for D in ps.fundamental_discriminants(0, DBOUND, -1):
        h = ps.class_number_imag(D)
        b0 = D % 2
        prin_form = ps.reduce_definite((1, b0, (b0 * b0 - D) // 4), D)
        splits, L1 = [], None
        for p in plist:
            if ps.kronecker(D, p) != 1:
                continue
            b = ps.form_at(D, p)
            hit = ps.principal_imag(D, p, b, prin_form)
            splits.append((p, hit))
            if hit and L1 is None:
                L1 = p
        band = 0
        while band < len(DBANDS) - 1 and -D > DBANDS[band]:
            band += 1
        out.append({"D": D, "h": h, "hplus": None, "neps": None,
                    "splits": splits, "L1": L1, "key": (h, DBANDS[band])})
    return out


# -------------------------------------------------------------- the model

def first_hit(splits, qs, cap):
    """(sum of p times its first-hit probability, total mass below cap).

    The model of derivation (1): the field's own split sequence, each
    prime a hit with its own probability. Everything is conditioned on
    the hit landing at or below the cap, which is division by the mass."""
    num = mass = 0.0
    surv = 1.0
    for (p, _), q in zip(splits, qs):
        if p > cap:
            break
        pr = surv * q
        num += pr * p
        mass += pr
        surv *= (1.0 - q)
    return num, mass


def pit(splits, qs, cap, target):
    """P(model L_1 < target) + half P(model L_1 = target), unconditioned."""
    below = at = 0.0
    surv = 1.0
    for (p, _), q in zip(splits, qs):
        if p > cap:
            break
        pr = surv * q
        if p < target:
            below += pr
        elif p == target:
            at += pr
        surv *= (1.0 - q)
    return below + 0.5 * at


def loo_shares(group, cap, edges=None):
    """Leave-one-out local shares, per field, per prime.

    Stratum totals per bin minus the field's own contribution -- the
    subtraction of derivation (2), whose integrity is C4's."""
    e = edges or BIN_EDGES
    nb = len(e) - 1
    tot_n = [0] * nb
    tot_h = [0] * nb
    for f in group:
        f["own_n"] = [0] * nb
        f["own_h"] = [0] * nb
        for p, hit in f["splits"]:
            if p > cap:
                break
            b = bin_of(p, e)
            f["own_n"][b] += 1
            tot_n[b] += 1
            if hit:
                f["own_h"][b] += 1
                tot_h[b] += 1
    empty = 0
    for f in group:
        qs = []
        for p, _ in f["splits"]:
            if p > cap:
                break
            b = bin_of(p, e)
            n = tot_n[b] - f["own_n"][b]
            k = tot_h[b] - f["own_h"][b]
            if n <= 0:
                empty += 1
                qs.append(0.0)
            else:
                qs.append(k / n)
        f["qs"] = qs
    return tot_n, tot_h, empty


def evaluate(fields, cap, constant=False, edges=None):
    """One row per stratum: measured mean, predicted mean, ratio, PIT.

    constant=True runs the sharpened incumbent -- q = 1/h over the same
    split sequence -- which isolates model FORM from density."""
    strata = {}
    for f in fields:
        strata.setdefault(f["key"], []).append(f)
    rows, empties = [], 0
    for key in sorted(strata, key=lambda k: (k if isinstance(k, tuple)
                                             else (k, 0))):
        group = strata[key]
        if constant:
            for f in group:
                f["qs"] = [1.0 / f["h"] for p, _ in f["splits"] if p <= cap]
        else:
            _, _, e = loo_shares(group, cap, edges)
            empties += e
        seen = [f for f in group if f["L1"] is not None and f["L1"] <= cap]
        if len(seen) < MIN_FIELDS:
            continue
        meas = sum(f["L1"] for f in seen) / len(seen)
        pred = 0.0
        masses = 0.0
        us = 0.0
        for f in seen:
            num, mass = first_hit(f["splits"], f["qs"], cap)
            pred += num / mass if mass > 0 else float("nan")
            masses += mass
            us += pit(f["splits"], f["qs"], cap, f["L1"]) / mass
        pred /= len(seen)
        # PB's index of dispersion, over EVERY field in the stratum and
        # not only the seen ones: a count is defined whether or not the
        # field ever hits. Expected and variance are the local model's own.
        # Read at TWO scales, because that is what this whole front turned
        # on: the count to the cap, and the count over the bottom decade
        # where L_1 actually lives. A dispersion measured over the wrong
        # range prices a first arrival no better than a density did.
        obs = exp = var = 0.0
        obs100 = var100 = 0.0
        for f in group:
            n = sum(1 for p, hit in f["splits"] if p <= cap and hit)
            mu = sum(f["qs"])
            obs += (n - mu) ** 2
            exp += mu
            var += sum(q * (1.0 - q) for q in f["qs"])
            ps100 = [(p, hit) for p, hit in f["splits"] if p <= 100]
            q100 = f["qs"][:len(ps100)]
            n100 = sum(1 for _, hit in ps100 if hit)
            mu100 = sum(q100)
            obs100 += (n100 - mu100) ** 2
            var100 += sum(q * (1.0 - q) for q in q100)
        # The two censoring rates of P7: what the MEASUREMENT drops, and
        # what the MODEL says it should have dropped. They are the same
        # quantity only if the stratum's fields share one density.
        drop_meas = 1.0 - len(seen) / len(group)
        drop_model = 1.0 - masses / len(seen)
        rows.append({"key": key, "n": len(seen), "meas": meas, "pred": pred,
                     "ratio": meas / pred, "pit": us / len(seen),
                     "mass": masses / len(seen), "all": len(group),
                     "dm": drop_meas, "dq": drop_model,
                     "disp": obs / var if var > 0 else float("nan"),
                     "disp100": obs100 / var100 if var100 > 0
                     else float("nan")})
    return rows, empties


REPLICATES = 60


def replicate_null(fields, rng, constant_null, cap=CAP, edges=None):
    """The reference distribution: regenerate every field's principality
    bits under a stated null, rerun the WHOLE pipeline, and collect the
    ratio and the PIT per stratum over R replicates.

    constant_null=True draws at 1/h -- the incumbent's density, so what
    comes back is the pipeline's bias from binning, pooling and the
    convexity of derivation (3). constant_null=False draws at the
    stratum's OWN measured share per bin, which is the hypothesis under
    test: under it the model is exactly right, so where the observed
    ratio sits in this distribution IS the verdict."""
    e = edges or BIN_EDGES
    strata = {}
    for f in fields:
        strata.setdefault(f["key"], []).append(f)
    # the generating density per (stratum, bin): the FULL share, not the
    # leave-one-out one -- the pipeline's own leave-one-out runs inside
    gen = {}
    for key, group in strata.items():
        nb = len(e) - 1
        tn, th = [0] * nb, [0] * nb
        for f in group:
            for p, hit in f["splits"]:
                if p > cap:
                    break
                b = bin_of(p, e)
                tn[b] += 1
                th[b] += hit
        gen[key] = [th[i] / tn[i] if tn[i] else 0.0 for i in range(nb)]
    acc = {}
    for _ in range(REPLICATES):
        synth = []
        for f in fields:
            q0 = 1.0 / f["h"] if constant_null else None
            sp, L1 = [], None
            for p, _ in f["splits"]:
                if p > cap:
                    break
                q = q0 if constant_null else gen[f["key"]][bin_of(p, e)]
                hit = rng.random() < q
                sp.append((p, hit))
                if hit and L1 is None:
                    L1 = p
            synth.append({"D": f["D"], "h": f["h"], "splits": sp, "L1": L1,
                          "key": f["key"]})
        for r in evaluate(synth, cap, edges=e)[0]:
            acc.setdefault(r["key"], []).append((r["ratio"], r["pit"],
                                                 r["disp"], r["disp100"]))
    out = []
    for key in sorted(acc, key=lambda k: (k if isinstance(k, tuple)
                                          else (k, 0))):
        v = acc[key]
        rs = [x[0] for x in v]
        ps_ = [x[1] for x in v]
        m = sum(rs) / len(rs)
        sd = (sum((x - m) ** 2 for x in rs) / max(1, len(rs) - 1)) ** 0.5
        # A stratum thin enough for every leave-one-out cell in a range to
        # be empty has no model variance there and so no index; those
        # replicates are dropped rather than allowed to poison the mean.
        ds = [x[2] for x in v if x[2] == x[2]]
        d1 = [x[3] for x in v if x[3] == x[3]]
        dm = sum(ds) / len(ds) if ds else float("nan")
        dsd = ((sum((x - dm) ** 2 for x in ds) / max(1, len(ds) - 1)) ** 0.5
               if len(ds) > 1 else 0.0)
        d1m = sum(d1) / len(d1) if d1 else float("nan")
        d1sd = ((sum((x - d1m) ** 2 for x in d1) / max(1, len(d1) - 1)) ** 0.5
                if len(d1) > 1 else 0.0)
        out.append({"key": key, "reps": len(rs), "mean": m, "sd": sd,
                    "lo": sorted(rs)[len(rs) // 20],
                    "hi": sorted(rs)[-1 - len(rs) // 20],
                    "pit": sum(ps_) / len(ps_), "rs": rs,
                    "disp": dm, "dispsd": dsd, "ds": ds,
                    "disp100": d1m, "d100sd": d1sd, "nd": len(ds),
                    "nd100": len(d1)})
    return out


def show_null(rows, title):
    print("\n%s" % title)
    print("     %-12s %5s %9s %9s %19s %8s"
          % ("stratum", "reps", "mean", "sd", "5th-95th pct", "PIT"))
    for r in rows:
        k = r["key"]
        label = ("h=%d |D|<=%d" % k) if isinstance(k, tuple) else "h=%d" % k
        print("     %-12s %5d %9.3f %9.3f   %8.3f %8.3f %8.3f"
              % (label, r["reps"], r["mean"], r["sd"], r["lo"], r["hi"],
                 r["pit"]))


def incumbent_mean(h, plist, cap):
    """explore_real_principal.py's own model: every odd prime a hit at
    density 1/(2h). Reproduced here so C2 is a regression and not a
    quotation."""
    q = 1.0 / (2 * h)
    num = mass = 0.0
    surv = 1.0
    for p in plist:
        if p > cap:
            break
        pr = surv * q
        num += pr * p
        mass += pr
        surv *= (1.0 - q)
    return num / mass if mass > 0 else float("nan")


# ------------------------------------------------------------------ table

def show(rows, title):
    print("\n%s" % title)
    print("     %-12s %5s %5s %9s %9s %7s %6s %8s %8s"
          % ("stratum", "n", "all", "meas mean", "pred mean", "ratio", "PIT",
             "drop obs", "drop mdl"))
    for r in rows:
        k = r["key"]
        label = ("h=%d |D|<=%d" % k) if isinstance(k, tuple) else "h=%d" % k
        print("     %-12s %5d %5d %9.1f %9.1f %7.3f %6.3f %8.3f %8.3f"
              % (label, r["n"], r["all"], r["meas"], r["pred"], r["ratio"],
                 r["pit"], r["dm"], r["dq"]))


def main():
    t0 = time.time()
    plist = [q for q in ps.primes_upto(CAP) if q != 2]
    print("ODD PRIMES to %d: %d;  bins %s" % (CAP, len(plist), BIN_EDGES))

    print("\nsweeping real fundamental discriminants to %d ..." % DBOUND)
    real = real_fields(plist)
    print("sweeping imaginary fundamental discriminants to %d ..." % DBOUND)
    imag = imag_fields(plist)
    print("     %d real, %d imaginary" % (len(real), len(imag)))

    # ---------------------------------------------------------- controls
    print("\n=== CONTROLS, read first ===")

    # C5 -- the split sequence against the imported principality test.
    bad = 0
    for f in real + imag:
        least = None
        for p, hit in f["splits"]:
            if hit:
                least = p
                break
        if least != f["L1"]:
            bad += 1
    print("[C5] least principal split prime vs L_1: %d mismatches over %d "
          "fields" % (bad, len(real) + len(imag)))

    # C1 -- the identity at h = 1.
    ones = [f for f in real if f["h"] == 1]
    loo_shares(ones, CAP)
    worst, n1 = 0.0, 0
    for f in ones:
        if f["L1"] is None or f["L1"] > CAP:
            continue
        num, mass = first_hit(f["splits"], f["qs"], CAP)
        worst = max(worst, abs(num / mass - f["L1"]))
        n1 += 1
    print("[C1] h = 1 pin: max |predicted - measured| = %.3g over %d fields"
          % (worst, n1))

    # C2 -- the incumbent regression.
    strata = {}
    for f in real:
        if f["L1"] is not None and f["L1"] <= CAP:
            strata.setdefault(f["h"], []).append(f["L1"])
    print("[C2] incumbent constant model at 1/(2h), ratios at h = 1..8:")
    got = []
    for h in range(1, 9):
        v = strata.get(h, [])
        if len(v) < MIN_FIELDS:
            got.append(float("nan"))
            continue
        got.append((sum(v) / len(v)) / incumbent_mean(h, plist, CAP))
    print("     " + "  ".join("%.2f" % x for x in got))
    print("     incumbent printed 1.15  1.68  2.11  2.27  1.89  3.23  3.21  "
          "2.81")

    # C4 -- leave-one-out integrity, recounted independently.
    rng = Random(SEED)
    mism = 0
    checked = 0
    by_h = {}
    for f in real:
        by_h.setdefault(f["h"], []).append(f)
    for h, group in sorted(by_h.items()):
        if len(group) < 2:
            continue
        loo_shares(group, CAP)
        f = group[rng.randrange(len(group))]
        rest = [g for g in group if g is not f]
        tn = [0] * NBINS
        th = [0] * NBINS
        for g in rest:
            for p, hit in g["splits"]:
                if p > CAP:
                    break
                b = bin_of(p)
                tn[b] += 1
                if hit:
                    th[b] += 1
        qs = []
        for p, _ in f["splits"]:
            if p > CAP:
                break
            b = bin_of(p)
            qs.append(th[b] / tn[b] if tn[b] else 0.0)
        checked += 1
        if any(abs(a - b) > 1e-12 for a, b in zip(qs, f["qs"])):
            mism += 1
    print("[C4] leave-one-out by subtraction vs independent recount: %d "
          "mismatches "
          "over %d strata" % (mism, checked))

    # C3 -- the synthetic nulls, REPLICATED. A single draw carries the same
    # sampling error as the data it is meant to grade, so one realization
    # is not an offset; R of them are a reference DISTRIBUTION.
    srows = replicate_null(real, rng, constant_null=True)
    show_null(srows, "[C3a] SYNTHETIC NULL at constant density 1/h -- the "
                     "pipeline's own bias, %d replicates:" % REPLICATES)

    # ------------------------------------------------------------- kills
    print("\n=== THE DIVISION ===")
    crows, _ = evaluate(real, CAP, constant=True)
    show(crows, "[K4] sharpened constant model (q = 1/h, own split "
                "sequence) -- model form only:")

    rows, empt = evaluate(real, CAP)
    show(rows, "[K1/K2/K3] LOCAL SHARE model, real side -- the paired "
               "division:")
    print("     empty leave-one-out cells: %d" % empt)

    irows, iempt = evaluate(imag, CAP)
    show(irows, "[K5] LOCAL SHARE model, imaginary side (strata by h and "
                "|D| band) -- the floor priced by the same machinery:")
    print("     empty leave-one-out cells: %d" % iempt)

    # C3b / K9 -- the reference distribution under the model being tested.
    brows = replicate_null(real, rng, constant_null=False)
    show_null(brows, "[C3b] REFERENCE under the LOCAL-SHARE model itself -- "
                     "what the pipeline prints when the model is true, %d "
                     "replicates:" % REPLICATES)
    ref = {r["key"]: r for r in brows}
    prev_coarse = {r["key"]: r["ratio"] for r in rows}
    print("\n[K1/K2/K9] the verdict: observed ratio against that reference")
    print("     %-8s %10s %10s %10s %10s %10s"
          % ("h", "observed", "ref mean", "ref sd", "z", "pct below"))
    for r in rows:
        h = r["key"]
        if h not in ref:
            continue
        g = ref[h]
        z = (r["ratio"] - g["mean"]) / g["sd"] if g["sd"] > 0 else 0.0
        below = sum(1 for x in g["rs"] if x < r["ratio"]) / len(g["rs"])
        print("     %-8d %10.3f %10.3f %10.3f %10.2f %9.1f%%"
              % (h, r["ratio"], g["mean"], g["sd"], z, 100.0 * below))

    # ------------------------------------------------- the follow-up engine
    print("\n=== THE FOLLOW-UP: the same division at cap %d ===" % CAP_HI)
    plist_hi = [q for q in ps.primes_upto(CAP_HI) if q != 2]
    print("     odd primes to %d: %d;  bins %s"
          % (CAP_HI, len(plist_hi), BIN_EDGES_HI))
    real_hi = real_fields(plist_hi)
    hrows, hempt = evaluate(real_hi, CAP_HI, edges=BIN_EDGES_HI)
    show(hrows, "[K8] LOCAL SHARE model, real side, cap %d:" % CAP_HI)
    print("     empty leave-one-out cells: %d" % hempt)
    prev = {r["key"]: r["ratio"] for r in rows}
    ppit = {r["key"]: r["pit"] for r in rows}
    print("\n[K8] the two caps side by side:")
    print("     %-6s %10s %10s %10s %10s"
          % ("h", "ratio 1e3", "ratio 1e4", "PIT 1e3", "PIT 1e4"))
    for r in hrows:
        h = r["key"]
        if h not in prev:
            continue
        print("     %-6d %10.3f %10.3f %10.3f %10.3f"
              % (h, prev[h], r["ratio"], ppit[h], r["pit"]))

    # K3's observable made numeric. "Flat in h" was read off the column by
    # eye on the first pass, and a claim that retires a mechanism should
    # not rest on that. The slope of the ratio against h, each stratum
    # weighted by 1/sd^2 of its OWN reference, is what says flat -- printed
    # beside the same slope for the constant model, which is the thing the
    # flatness is a contrast with.
    print("\n[K3] is the residual FLAT in h? weighted slope of the ratio "
          "on h:")
    for src, lbl in ((rows, "local-share model"),
                     (crows, "constant model")):
        pts = [(r["key"], r["ratio"], ref[r["key"]]["sd"]) for r in src
               if isinstance(r["key"], int) and r["key"] > 1
               and r["key"] in ref and ref[r["key"]]["sd"] > 0]
        w = [1.0 / sd ** 2 for _, _, sd in pts]
        S = sum(w)
        Sx = sum(wi * x for wi, (x, _, _) in zip(w, pts))
        Sy = sum(wi * y for wi, (_, y, _) in zip(w, pts))
        Sxx = sum(wi * x * x for wi, (x, _, _) in zip(w, pts))
        Sxy = sum(wi * x * y for wi, (x, y, _) in zip(w, pts))
        det = S * Sxx - Sx * Sx
        slope = (S * Sxy - Sx * Sy) / det
        se = (S / det) ** 0.5
        mean = Sy / S
        chi2 = sum(wi * (y - mean) ** 2 for wi, (_, y, _) in zip(w, pts))
        print("     %-18s slope %+7.4f +/- %.4f (z = %+5.2f), mean %.4f, "
              "chi2 %.2f on %d dof"
              % (lbl, slope, se, slope / se, mean, chi2, len(pts) - 1))

    # ------------------------------------------- PA: the bin resolution
    print("\n=== THE FOURTH SLATE ===")
    frows, _ = evaluate(real, CAP, edges=BIN_EDGES_FINE)
    fref = {r["key"]: r
            for r in replicate_null(real, rng, False, edges=BIN_EDGES_FINE)}
    print("\n[KA] the same division at bins twice as fine (%d bins):"
          % (len(BIN_EDGES_FINE) - 1))
    print("     %-6s %10s %10s %10s %10s %10s"
          % ("h", "coarse", "fine", "ref mean", "ref sd", "pct below"))
    for r in frows:
        h = r["key"]
        if h not in fref or h not in prev_coarse:
            continue
        g = fref[h]
        below = sum(1 for x in g["rs"] if x < r["ratio"]) / len(g["rs"])
        print("     %-6d %10.3f %10.3f %10.3f %10.3f %9.1f%%"
              % (h, prev_coarse[h], r["ratio"], g["mean"], g["sd"],
                 100.0 * below))

    # ------------------------------------------ PB: the index of dispersion
    print("\n[KB] index of dispersion of the principal-prime COUNT -- "
          "each field against its own local density:")
    print("     %-4s %9s %9s %7s   %9s %9s %7s"
          % ("h", "obs<=1e3", "ref", "z", "obs<=100", "ref", "z"))
    for r in rows:
        h = r["key"]
        if h not in ref:
            continue
        g = ref[h]
        def cell(obs, m, sd):
            if obs != obs or m != m:
                return "%9s %9s %7s" % ("-", "-", "-")
            z = (obs - m) / sd if sd > 0 else 0.0
            return "%9.3f %9.3f %7.2f" % (obs, m, z)
        print("     %-4d %s   %s"
              % (h, cell(r["disp"], g["disp"], g["dispsd"]),
                 cell(r["disp100"], g["disp100"], g["d100sd"])))

    print("\nwall: %.1f s" % (time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
