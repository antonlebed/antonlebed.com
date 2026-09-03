"""DOES THE PRINCIPAL-SHARE DEFICIT PERSIST AT THE SCALE A SCAN RUNS AT?
-- the trivial class's share of split primes, resolved into DECADES of p
and cut against a 512x lever on |D|, over both signs.

THE QUESTION. explore_principal_share.py, explore_class_order.py and
explore_class_level.py leave one ADVANTAGE standing: a scan for a
principal representative over small split primes is slower than a uniform
1/h model predicts, and the shortfall is graded by the class group rather
than by a fudge factor. Every reading behind it was taken on |D| <= 4000
with the split primes capped at 10^4, and the sharpest of those readings
says the deficit is mostly spent by the top of that range. So the standing
question
was whether the deficit is a small-p transient a real scan runs straight
past, or a bias it pays throughout.

THAT QUESTION IS UNDERSPECIFIED AND THIS RIG SAYS WHY BEFORE ANSWERING IT.
"The scale a scan runs at" is not a scale of p alone. A scan stops at L_1,
the least NARROW principal split prime -- WHICH IS THIS FILE'S L_1 AND
NOT THE CORPUS'S: both walk the split primes only (a rank-1 characteristic
is UNRAMIFIED of residue degree 1, explore_principal_place.py derivation
3), but the corpus's L_1 tests WIDE principality, the sign disjunction of
explore_real_principal.py, which accepts more primes; C5 measures the gap
and P4 below quotes the corpus's figure, which is why P4 is scored on a
trend. (This paragraph first blamed the gap on ramified primes; the wide
test rerun beside the narrow one over the same 1216 fields reproduces
94.1%, mean 26.8, median 11 against this rig's 89.3%, 40.2, 17, so the
gap is the notion and not the population.)
L_1 is a function of the FIELD: at
D < 0 no split prime below |D|/4 is principal at all (a derived hard zero,
explore_principal_share.py derivation 5), so the scan cannot even start
below that. Raising the prime cap at a FIXED |D| <= 4000 therefore asks
about primes no scan at those fields ever reaches, and answers a question
no consumer has. The decidable question is whether the deficit's decay is
a function of p ABSOLUTELY -- in which case a scan at any realistic field
size pays it only in the first decade and the correction is a curiosity --
or a function of p RELATIVE to the field, in which case the scan pays it
across its whole actual range and the correction is the edge it was
scouted as. That needs both levers moved at once, and the |D| lever is the
one nothing has moved: the incumbent's widest cut spans a factor of four.

THE SUSPICION IN ITS OWN VOCABULARY. The incumbent's dials -- h+, the
2-rank, a class's order -- are all GROUP quantities, read at one prime
range. The question here is written in a different vocabulary: it is about
the SIZE of the primes against the size of the DISCRIMINANT, and the group
enters only as a stratifying variable to be held fixed. So h+ is not a
dial here, it is a control, and every load-bearing table fixes it.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE REAL SIDE HAS A SOFT ANALOGUE OF THE IMAGINARY FLOOR, AND ITS
      SCALE IS sqrt(D) AND NOT D. A split prime p is narrow principal at
      D > 0 exactly when the form (p, b, (b^2-D)/(4p)) reduces into the
      principal cycle. Every REDUCED indefinite form (a, b, c) of
      discriminant D has 0 < b < sqrt(D) and |a| < sqrt(D), so the
      principal cycle contains only forms whose leading coefficient is
      below sqrt(D). A prime p < sqrt(D) that is narrow principal must
      therefore appear as a leading coefficient IN that cycle -- the form
      (p, b, c) with p < sqrt(D) and |c| < sqrt(D) is at or one step from
      reduced -- and the cycle has finitely many entries, of order the
      regulator. So the supply of small principal primes is drawn from a
      bounded pool whose scale is set by sqrt(D), where the supply of
      small SPLIT primes is not. Above sqrt(D) the argument gives nothing:
      p is no longer a candidate leading coefficient of a reduced form and
      principality is decided by the reduction rather than by membership.
      This is a scale, not a bound: indefinite forms represent both signs
      and the cycle is not thin, so nothing here forbids a small principal
      prime. It predicts WHERE a transient ends, and it predicts sqrt(D).

  (2) THE IMAGINARY SIDE'S IS HARD AND ITS SCALE IS D. Completing the
      square on the definite principal form puts its values at |D|/4 or
      above off (1, 0), so no prime below |D|/4 is principal (the
      incumbent's derivation 5). At |D| <= 4000 that ceiling is <= 1000
      and sits inside the bottom two decades, which is why the incumbent
      could read the two signs against each other at all; at the bands
      here it passes the prime cap entirely. So the two signs are
      predicted to shift at DIFFERENT rates -- one decade per 100x in |D|
      on the real side, one per 10x on the imaginary -- and that
      difference is the rig's own check that it is reading a scale and not
      a sampling artifact, since no artifact of the sweep distinguishes
      the signs.

  (3) THE POPULATION OF A CELL, WHICH IS WHAT THE DENOMINATOR MOVES WITH.
      The statistic is a mean over FIELDS of a per-field ratio
      (m_d / n_d) * h+, where n_d is the field's split primes in decade d
      and m_d the principal ones. Three things move with d and are
      controlled rather than assumed: n_d grows by roughly a factor of ten
      per decade, so the per-field ratio's variance falls by the same
      factor and the bottom decade is the noisy one; the FIELD SET must
      not move with d, so a field enters a row only if it clears the
      per-decade floor at EVERY decade, and the all-fields row is printed
      beside it; and the nominal 1/h+ does NOT move with d -- it is a
      density, constant in p, which is the one thing that makes the
      decades comparable at all. What moves with the BAND is h+ itself,
      which is why every load-bearing table fixes it.

  (4) WHY h+ CAN BE FIXED ACROSS A 512x LEVER AT ALL, AND ONLY AT D > 0.
      Narrow class numbers of REAL quadratic fields stay small as D grows
      -- h+ = 1, 2, 4 remain common at |D| ~ 10^6 -- so a fixed-h+ row can
      be populated in every band and the |D| lever is separable from the
      group. At D < 0, h grows like sqrt(|D|) and no h+ is common in two
      distant bands, so the imaginary side carries NO matched comparison
      and is reported for its floor alone. That asymmetry is a property of
      the fields and not a choice, and it means the load-bearing table is
      the real one.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1 (THE TRANSPLANT, FLAGGED). The incumbent found the deficit BLIND to
     |D|: flat along a fixed-h+ row across its |D| bands, 0.662, 0.628,
     0.661, 0.687 at h+ = 8. Imported here, that says the rows of the
     table below coincide -- the decay is a function of p absolutely. The
     import is from a FOUR-FOLD |D| range read at ONE pooled prime range,
     and a pooled reading cannot see a shift; this is exactly the
     parameter this rig varies, so P1 is what the import commits to and
     K2 is what refuses it.

  P2 (THE HAND-DERIVATION'S RIVAL). Derivation (1): the real-side deficit
     is a transient whose end scales as sqrt(D). The rows shift RIGHT by
     one decade per 100x in |D|.

  P3. Derivation (2): the imaginary trivial-class share is identically
     zero at every decade wholly below |D|/4, at every field, and the
     rig reproduces that at zero exceptions.

  P4. The consumer reading follows the shift: the share of fields whose
     L_1 exceeds 100 -- 5.8% at the incumbent's population -- rises with
     the band, so the scan's own range moves out of the bottom decade and
     into the decades the deficit is being measured at.

  P5 (FROZEN AFTER THE FIRST RUN AND BEFORE THE SECOND, and flagged as
     such: the first run's table is its motivation and the reading below
     did not exist when that table printed). Derivation (1) says the pool
     a small principal prime is drawn from is the PRINCIPAL CYCLE, whose
     size is the regulator. It predicts the pool's SIZE and not its REACH,
     so it predicts no shift in p -- but it does predict a LEVEL effect
     graded by the cycle length l: at fixed h+, a field with a longer
     principal cycle has a deeper pool of small principal forms and so a
     SHALLOWER bottom-decade deficit. And it predicts which variable is
     the real one: at fixed h+ the class number formula ties the regulator
     to sqrt(D), so l and |D| are nearly one column and any |D| gradient
     at fixed h+ is a regulator gradient in disguise. THE CONFOUND IS THE
     POINT AND IT IS NOT SEPARABLE ACROSS BANDS -- it is separable WITHIN
     one, a band being a factor of two wide while l spreads over an order
     of magnitude inside it.

THE SECOND READING'S KILL.

  K6. The two-way table at fixed h+, real side: rows are |D| bands and
      columns are GLOBAL terciles of the principal cycle length l, cell is
      the bottom-decade ratio. If the columns separate and the rows within
      a column agree, the grading is l's and derivation (1)'s mechanism
      survives. If the rows separate at fixed l-tercile and the columns do
      not, l is not the variable and the |D| gradient stands as an
      observation with no mechanism. The cell counts are printed because
      the corner cells -- a long cycle in a small band, a short one in a
      large band -- are exactly the rare fields the separation rests on,
      and a table whose off-diagonal is empty has not separated anything
      and the rig says so rather than leaving it to be noticed.

  K7 (frozen after K6 printed and before it was read as a verdict: K6's
      GLOBAL terciles put a band's fields into one or two columns and pool
      the rest, so its all-bands column is a comparison across bands and
      not a controlled one). The same contrast on WITHIN-BAND terciles,
      which by construction fills all three columns at every band and
      holds |D| to a factor of two. The statistic is the top-minus-bottom
      tercile contrast, printed per band and pooled over bands with the
      standard error the per-field ratios themselves supply. Derivation
      (1) predicts a positive contrast at every band, pooling to the size
      K6's global column spread showed. A pooled contrast inside its own
      error, with K6's global spread outside it, says the global gradient
      is |D|'s transported along the l-|D| coupling and that l does not
      grade at fixed |D|. The error is quoted because this is the reading
      whose extremes K6 could not power.

  K8 (frozen after K7 printed, and it is the reading the ADVANTAGE is
      actually written in -- everything above is a share, and a scan pays
      in TRIALS). Per field record J, the number of split primes the scan
      examines before its first principal one. Under the uniform model the
      advantage is scouted against, J is geometric with success 1/h+, so
      its median is the least j with 1 - (1 - 1/h+)^j >= 1/2, computed
      exactly and not simulated. The overshoot is the observed median J
      over that. This is the correction in the consumer's own units, it
      has no free parameter, and it is read per |D| band: an overshoot
      STABLE across the lever is a fixed multiplier a scan-cost model can
      carry, one DECAYING toward 1 is a small-field artifact, and one
      growing is the edge widening with the field. J is capped by the
      prime list, so the rig prints the share of fields with no principal
      split prime below the cap and a median computed where that share is
      non-zero is marked -- a censored median is not a median.

THE KILLS, FROZEN AS OBSERVABLES AND NOT AS INFERENCES.

  K1. THE TABLE: mean ratio by (sign, h+, |D| band, decade of p), with the
      field count in each cell. Read against C2's exchangeability band.

  K2. THE ROWS COINCIDE. If at fixed h+ every band's cell at a given
      decade lies inside every other band's C2 band at that decade, P1
      stands: the deficit is a transient in ABSOLUTE p. The advantage
      then retires on the condition it was scouted under: a correction
      confined to p <= 100 whatever the field, which no scan at a
      realistic field size spends its time in.

  K3. THE ROWS SHIFT. If the cell at decade d and band B matches the cell
      at decade d-1 and a band 100x smaller, to within C2's band, the
      deficit is relative and P2 holds. The edge is then real at scale and
      the next question is a literature read, not a run.

  K4. THE SHIFT RATE, printed rather than eyeballed: per (sign, h+), the
      log10 p at which the row first reaches 0.95 of nominal, linearly
      interpolated in log10 p between the bracketing decades and printed
      as "-" where the row never reaches it or starts above it, regressed
      on log10|D| at the band centres. Slope 0 is P1, 1/2 is P2, 1 is a
      D-linear floor. The slope is printed with its residuals; two points
      make a line and the rig prints how many bands actually contributed.

  K5. THE CONSUMER COLUMN: per (sign, band), the median L_1 and the share
      of fields with L_1 > 100, > 1000, > 10^4.

THE CONTROLS, and C1 is read before any verdict.

  C1. INSTRUMENT PIN. At h+ = 1 every split prime is narrow principal, so
      the ratio is identically 1 at every decade and every band, at both
      signs. Any deviation is the instrument and not the arithmetic.

  C2. THE EXCHANGEABILITY NULL. Per field, redistribute its OWN total
      principal count uniformly over its OWN split primes, preserving both
      the per-decade split counts and the field's overall level, and
      recompute the cell. This destroys any dependence on p while changing
      nothing else, so it is the null the whole question is asked against.
      R draws at a fixed seed; the band is the min and max over draws.

  C3. THE DERIVED ZERO. P3's check, printed as a count of violations.

  K9 (frozen after the audit asked WHOSE VOCABULARY K8 is written in, and
      it was not its own). Everything above measures NARROW principality
      against 1/h+, which is what the genus characters and every share
      reading this rig extends are defined on. But a scan "for a principal
      representative" is a scan for a GENERATOR, which is the WIDE notion:
      narrow principal means a TOTALLY POSITIVE generator and implies wide,
      not conversely, and the two differ at exactly the real fields where
      the fundamental unit has norm +1, where h+ = 2h. So K8's consumer
      sentence is written in a vocabulary its numbers do not use, and at
      half the real population the narrow scan counts trials a wide scan
      would not. The rig already computes wide principality per split prime
      and was discarding it. K9 is the same trials reading in the wide
      vocabulary -- J_w to the first WIDE-principal split prime against the
      uniform model's exact mean of h -- in its own table after K8's, per
      band, stratified by h and not by h+. If the
      wide overshoot tracks the narrow one, the vocabulary was harmless and
      the finding is one finding; if it does not, the consumer's number is
      K9's and K8 measures a statistic about totally positive generators.

  C5 (frozen after the audit found it MISSING, and it is the control this
      rig should have opened with). Every table here is a BREAKDOWN of a
      figure another rig published, and a breakdown that never prints the
      WHOLE against the original is checked only on its own internals: the
      shared instrument's controls all pass while a defect introduced in
      the new reading survives. So the rig sweeps the incumbent's exact
      population as well -- real fundamental discriminants |D| <= 4000,
      which is not one of the bands -- and prints its own p <= 100,
      100 < p <= 1000 and pooled p <= 1000 ratios beside the published
      0.868/0.949/0.938, 0.630/0.844/0.815, 0.414/0.823/0.764 and
      0.332/0.714/0.662 at h+ = 2, 4, 6 and 8, under the incumbent's own
      per-bin floors of 8 and 20 rather than this rig's. These are the same
      quantity computed by a different principality path at a ten-times
      wider prime cap, so they must agree to rounding, and any band table
      is worth what this check is worth.

  C4. THE GATES, SWEPT AS FUNCTIONS OF THEMSELVES rather than quoted at
      one value: the field sample size per band, the per-decade minimum
      split count a field needs to enter a cell, and the fixed-field-set
      restriction of derivation (3) -- each printed at two settings, so a
      verdict that moves with a gate is visible as such.

WHAT THIS RIG DOES NOT DO. It reads the TRIVIAL class only. The order
ladder, the 2-rank and the character decomposition are all readings ACROSS
the classes of one field and they need the group's composition, which the
wide bands here do not compute; the order axis stays where it was, at
|D| <= 4000. And the field sample within a band is a uniform stride over
the band's fundamental discriminants, which is a sample of the band and
not the band.

FINDINGS.

CONTROLS, READ FIRST. C1: 612 fields at h+ = 1, zero decades where the
principal count differs from the split count. ALL 612 ARE REAL and the
rig prints why rather than reporting a coverage it has not got: no
imaginary quadratic field has class number 1 above |D| = 163, so the pin
cannot run at D < 0 in this population at all, by theorem and not by
sampling. C3: 14,706 imaginary decade-cells lying wholly below |D|/4,
zero carrying a principal prime -- P3 exact. C6, which the audit added
because the D < 0 verdict was resting on an unmeasured clause: ABOVE the
floor the imaginary share does not read nominal, and what it reads is
ordered by CLEARANCE -- the decade's lower edge over |D|/4 -- and not by
band. The four readable cells run 0.812 at clearance x1.1 on 300 fields,
0.805 at x1.3 on 606, 0.884 at x3.3 on 1200 and 0.939 at x13.3 on 606.
It RISES with clearance and is NOT monotone: the two lowest cells invert
by 0.007, and C6 prints no error bar, so they are a tie and not a step.
What orders the four is clearance and not |D| -- the floor's own tail
decaying with distance from it, leaving a 6% residual at the only
well-cleared cell. At |D| >= 128000 the floor passes the 10^5 prime
cap and the rig sees nothing above it at all, which is printed rather
than argued past. C5, the one this rig should have opened with and did
not, and which caught a second thing nobody asked it for: on the
incumbent's own population every cell of the undecomposed figure
reproduces to three decimals -- 0.868, 0.949, 0.938
at h+ = 2 on 442 fields, 0.630, 0.844, 0.815 at h+ = 4 on 334, 0.414,
0.823, 0.764 at h+ = 6 on 42 and 0.332, 0.714, 0.662 at h+ = 8 on 85,
against the published values exactly. That is a different principality
path at a ten-times wider prime cap returning the same twelve numbers,
so the band tables below are a breakdown of a figure this rig can
reproduce and not of one it has merely inherited. AND THE SAME CONTROL
SHOWS THAT L_1 IS NOT L_1: on that population the least NARROW principal
split prime reads 89.3% at or below 100, mean 40.2, median 17 on 1216
fields, against the corpus's published 94.2%, 25.7 and 11. The corpus's
L_1 is WIDE principality over the same split primes (the sign
disjunction), and every narrow-principal prime is wide-principal, so a
further candidate can only LOWER a least and the published figures have
to be the more optimistic ones on all three statistics, which they are.
Everything called L_1 here is the NARROW one.
P4 is therefore scored on its TREND across the bands and never on its
level, K5's medians are not comparable to the corpus's, and K8 and K9 are
untouched: they count trials over split primes, which is the scan they
describe.

**THE DECAY IN p NEVER MOVES THE WAY sqrt(D) SAYS, AND WHERE IT MOVES AT
ALL IT MOVES THE OTHER WAY** (observation; K1, K4). The prime at which a
fixed-h+ row reaches 0.95 of nominal, regressed on log10|D|, has slope
-0.245, +0.002, -0.136, +0.003 and -0.080 at h+ = 2, 3, 4, 6, 8 -- five
bands each but h+ = 3, whose top band never falls below 0.95 and so
contributes four. Derivation (1) predicted +0.5 and P2 dies on it with
room to spare: every slope is at or below zero. THE SLOPES ARE NOT ZERO
AND THE READING IS NOT "FLAT" -- at h+ = 2 the reach runs 2.32, 2.12,
1.88, 2.15, 1.57 over the bands, which across the lever is the transient
ending a factor of four EARLIER at the largest fields, and at h+ = 4 a
factor of two. That is the level finding below showing through the reach
statistic, a row that starts shallower crossing 0.95 sooner, and it is
the opposite of the sqrt(D) direction rather than the absence of a
direction. The h+ = 2 fit is poor besides, residuals to +-0.29 on five
points. Every row is at 0.97-1.00 of nominal by the top decade at every
band, and the C2 exchangeability band there runs 0.958 to 1.001.

**BUT THE LEVEL AT THE BOTTOM DECADE IS NOT INVARIANT, AND A FOUR-FOLD
LEVER COULD NOT SEE IT** (observation; K1). At p <= 100 the ratio RISES
with |D| -- 0.880, 0.912, 0.918, 0.903, 0.940 at h+ = 2; 0.659, 0.742,
0.784, 0.782, 0.826 at h+ = 4; 0.342, 0.410, 0.552, 0.545, 0.627 at
h+ = 8 -- so the deficit shallows by 0.285 at h+ = 8 across the lever,
where the incumbent read 0.662, 0.628, 0.661, 0.687 across |D| bands to
4000 and called it flat. Both readings are right: the shortfall is blind
to |D| over a factor of four and graded by it over a factor of 512, and
it has not levelled off by |D| ~ 10^6. The incumbent's flatness was the
lever and not the arithmetic.

**AND THE PRINCIPAL CYCLE DOES NOT GRADE THE LEVEL: THE POOLED READING
THAT SAYS IT DOES IS THE CONFOUND THE PREDICTION FLAGGED** (observation;
K6, K7. P5 DIES). Pooled over bands, the bottom-decade ratio rises with
the global tercile of the cycle length l -- 0.710, 0.786, 0.805 at
h+ = 4 and 0.402, 0.563, 0.587 at h+ = 8 -- which reads as derivation
(1)'s level prediction confirmed. It is not a controlled comparison: at
fixed h+ the class number formula ties l to sqrt(D), so a global tercile
is mostly a band. With terciles taken WITHIN each band, which holds |D|
to a factor of two and fills all three columns everywhere, the
top-minus-bottom contrast pools to -0.031 +- 0.014 at h+ = 2 -- the
WRONG SIGN -- and to +0.031 +- 0.025 at h+ = 4 and +0.051 +- 0.048 at
h+ = 8, against global spreads of 0.009, 0.095 and 0.185: neither
positive figure reaches 1.3 standard errors. And within each h+ the
contrast decays across the lever and reverses: +0.100, +0.056, +0.039,
+0.012, -0.040 at h+ = 4 and +0.169, +0.239, -0.000, -0.040, -0.110 at
h+ = 8. THE ONE STRATUM THAT SUPPORTS P5 IS QUOTED RATHER THAN DROPPED,
because dropping the arm that favours the refuted prediction is how a
refutation is manufactured: h+ = 6 pools to +0.254 +- 0.074, the largest
contrast in the table. It is not evidence, and the reason is in its own
rows -- +0.298, +0.336, -0.445, +0.605 on 35 to 48 fields a band, a
pooled figure averaging a swing of 1.05 between two adjacent bands.
A stratum whose bands disagree in SIGN reports its noise, not its
effect. So the |D| gradient stands as an
observation with no mechanism, and the one candidate is refuted by the
control its own prediction asked for at the two strata that can carry
one.

**THE CONSUMER'S RANGE DOES NOT MOVE AT D > 0 AND TRACKS |D| AT D < 0,
WHICH SPLITS THE ADVANTAGE BY SIGN** (observation; K5). The real median least
principal SPLIT prime runs 19, 23, 23, 29, 29 across the lever: a scan over
a real
quadratic field finishes at p of order 20 to 30 whatever the field size,
permanently inside the transient the rows above measure. The share of
fields needing p > 100 rises only 0.138 to 0.250, so P4 is right about
the tail and wrong about the median. The imaginary median L_1 runs 929,
3541, 14323, 48311, tracking |D|/4, and at |D| >= 512000 no sampled
field carries a principal split prime below 10^5 at all.

**AND IN THE CONSUMER'S OWN UNITS THE CORRECTION IS A FIXED MULTIPLIER
GRADED BY h+** (observation; K8, and this is what the advantage is
written in). Mean trials to the first principal split prime, over the
uniform model's exact mean of h+: 1.155, 1.096, 1.068, 1.070, 1.131
(+- 0.037 to 0.045) at h+ = 2 and 1.257, 1.303, 1.165, 1.219, 1.174
(+- 0.046 to 0.061) at h+ = 4, flat across the lever; 1.886, 1.541,
1.446, 1.472, 1.314 (+- 0.073 to 0.145) at h+ = 8, declining with the
band but 4.3 standard errors above 1 at the top of it. THE SIZE AND THE
FLATNESS COME APART and the qualifier is load-bearing: the multiplier is
flat where it is SMALL and decays where it is LARGE, so K8 establishes a
constant of 1.07 to 1.30 to |D| ~ 10^6 at h+ = 2 and 4, and at h+ = 8 a
larger correction that has fallen by a third across the lever with
nothing here saying where it stops. Read as one row of "a fixed
multiplier" the table would be overstated at the only stratum where the
multiplier is big enough to matter.

**AND IN THE CONSUMER'S OWN VOCABULARY THE FLATNESS IS h = 2's ALONE**
(observation; K9). Translated to WIDE principality against 1/h -- a
generator rather than a totally positive one, which is what "a principal
representative" means -- only h = 2 holds: 1.187, 1.201, 1.153, 1.152,
1.152 (+- ~0.04) across the lever. Every other stratum DECAYS, and hard:
1.812, 1.523, 1.274, 1.298, 1.224 at h = 4; 3.231, 2.041, 1.355, 1.371,
1.132 at h = 6; 2.194, 2.393, 1.831, 1.358, 1.316 at h = 8. So the
narrow flatness at h+ = 4 does not survive the translation, on a
population that is not the same one -- h+ = 4 mixes h = 4 and h = 2
fields while h = 4 mixes h+ = 4 and h+ = 8 -- which is exactly why the
vocabulary had to be asked rather than assumed. WHAT SURVIVES TO
|D| ~ 10^6 IS A CORRECTION OF ROUGHLY 1.13 TO 1.32 AT EVERY h, arrived at
by DECAY rather than by constancy -- 1.152 +- 0.041, 1.224 +- 0.066,
1.132 +- 0.122 and 1.316 +- 0.101 at h = 2, 4, 6, 8, clearing 1 by 3.7,
3.4, 1.1 and 3.1 standard errors, so THREE of the four stand and h = 6
does not -- and the corpus's 1.15-to-3.23 is a small-field figure. One
cell runs the other way and is quoted at its own weight: h = 3 reads
0.791 +- 0.075 at the top band on 51 fields, below 1 by 2.8 standard
errors, having fallen from 1.845 -- one stratum out of twenty-five cells,
so it is an anomaly to name and not a result, though it sits beside the
section's standing observation that the odd part does not grade the way
its size says. h+ = 3 and 6 rest
on 11 to 48 fields a band and are quoted as noise, not as rows. The
imaginary rows read 8.70 and 6.93 at |D| <= 4000, which is the floor
being paid and not the deficit. THE MEDIAN IS THE READING NOT TO TAKE
and the rig prints it to show why: at h+ = 2 it is 2 against a model 1
at every band, so its overshoot is exactly 2 five times over and that is
one trial's difference throughout.

**THE VERDICT ON THE ADVANTAGE, AND THE FROZEN KILL DID NOT DELIVER IT.**
K2's letter -- the deficit shrinking to noise by the top decade -- fires:
every row reaches 0.97-1.00 there. But K2 was written on a presumption,
that a scan's range grows with the prime cap, and K5 refutes that
presumption at D > 0 and confirms it at D < 0. So the verdict is the
consumer column's and not the share table's, and it splits: at D > 0 the
advantage SURVIVES as a correction of about 1.13 to 1.32 in trials at
|D| ~ 10^6, flat in |D| only at h = 2 and reached by decay elsewhere, and
and at D < 0 it is NOT MEASURABLE, which is a weaker and truer statement
than the one this file first wrote. The scan there starts AT |D|/4, so it
runs in the x1-to-x2 clearance region where C6 reads 0.81 -- a 23%
correction it certainly pays -- but that is the floor's tail, and the
floor is classical and not ours. Separating the class group's deficit
from it needs a cell both well clear of the floor AND at large |D|, and
the prime cap forbids exactly that conjunction: clearance x13 exists only
at |D| <= 4000, where h+ is small. So the thread's own advantage is
neither confirmed nor killed at D < 0 -- it is out of the rig's reach,
and calling it DEAD there would have been a verdict resting on the one
arm nothing had measured.

**FOUR FACTORS ARE NOW QUOTED IN THIS THREAD AND THEY ARE FOUR
QUANTITIES, AND TWO OF THEM END AT 3.23 BY COINCIDENCE.** 1.15 to 3.23x
is the first-hit model at density 1/(2h) over
ALL odd primes at WIDE h; the exchangeability ratio is a character
component's energy against a null; K8's 1.07 to 1.89 is mean NARROW
trials over SPLIT primes against 1/h+; and K9's 0.79 to 3.23 is mean WIDE
trials against 1/h. None is a restatement of another, and the last two
differ in population as well as in notion.

C4, THE GATES, AND ONE VERDICT DOES MOVE WITH ONE OF THEM. The floor at 3
and the fixed-field-set restriction on or off move no cell of the h+ = 4
table by more than 0.007. Halving the field sample moves the bottom decade
by up to 0.032 and every other cell by 0.018 or less. The floor at 12 is
the one that bites, and only in the bottom decade: it moves the smallest
band by 0.071 and the largest by 0.001, which is not a shift of the table
but a compression of THE GRADIENT the level finding rests on. Read as the
verdict rather than as cells, the bottom-decade rise across the lever is
0.167 at the setting, 0.176 at nmin 3, 0.145 at half the sample and 0.097
at nmin 12 -- same-signed and substantial at all four, and about 40%
smaller at the strictest floor. The row itself rises at every setting and
is MONOTONE at two of them (nmin 12 and the halved sample); at the other
two it dips at the fourth band by 0.002 and 0.006 -- an order of
magnitude inside the width of the C2 null bands at those cells, which is
the only scale the rig prints there. The mechanism is visible in which end
moves: a
floor on split primes BELOW 100 removes the fields that have fewest of
them, and those are where the small-|D| deficit is deepest, so part of the
gradient is carried by the sparsest fields. The gradient is not an
artifact of the floor -- it survives every setting -- but its SIZE is a
function of one, and any number put on it inherits that.

WHAT IS NOT CONTROLLED, stated rather than left to be found. The |D|
gradient at fixed h+ has no mechanism and the remaining candidate is not
separable in this population: at fixed h+ the class number formula makes
the regulator a function of D, so "large |D| at fixed h+" and "large
regulator" are one column by construction, and l -- a COUNT of cycle
entries -- is not the regulator, which is a sum of logarithms over them.
K7 refutes the count and says nothing about the size. The h+ = 8
decline in K8 could be that same gradient. And the fields are a uniform
stride over each band, so every figure is a statement about a sample.

RUN RECORD: wall 231.8 s, peak working set 42.4 MB and peak commit
32.2 MB under memwatch at a 512 MB ceiling. 9,591 odd primes to 10^5
against 10,815 fundamental discriminants -- 1200 sampled per band per
sign, less where a band holds fewer, the smallest band yielding 609 real
and 606 imaginary -- over five bands from 2000 to 1,024,000, plus C5's
1,216 real fields to |D| <= 4000. Pure Python plus numpy for one exact
multivariate hypergeometric draw, which C2 needs per field per draw. The
wall sits INSIDE the five-minute no-ceremony band, at 3.9 minutes: the
cost is one principality test per split prime per field and it is flat in
|D| at about 22 ms a field, so the bands buy their lever at the price of
the field count alone and a wider one would cost the same per field.
"""

import os
import sys
import time
from math import isqrt, log10

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

# numpy is here for ONE thing: an exact multivariate hypergeometric draw,
# which C2 needs per field per draw and which the standard library has no
# fast exact route to. The BLAS thread guard above is set before the
# import, per the charter's arena rule.
import numpy as np                                             # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_principal_share import (                          # noqa: E402
    primes_upto, kronecker, form_at, fundamental_discriminants,
    class_data_real, principal_cycle, class_number_imag,
    reduce_definite, principal_real, principal_imag)

PCAP = 10 ** 5
DEC_EDGES = [100, 1000, 10000, 100000]
DEC_LABELS = ["p<=100", "10^2-10^3", "10^3-10^4", "10^4-10^5"]
ND = len(DEC_EDGES)

# Geometric bands with a 4x gap between them: the centres span 512x, which
# is the lever derivation (4) says is separable from the group at D > 0.
DBANDS = [(2000, 4000), (8000, 16000), (32000, 64000),
          (128000, 256000), (512000, 1024000)]

NF = 1200                 # fields sampled per band per sign (C4 sweeps it)
NMIN = 6                  # split primes a field needs in a decade (C4)
MINF = 8                  # fields a cell needs to print
HPLUS = [2, 3, 4, 6, 8]   # the fixed-h+ rows; derivation (4)
RDRAWS = 5                # C2 draws
SEED = 20844


def dec_of(p):
    for i, e in enumerate(DEC_EDGES):
        if p <= e:
            return i
    return None


def band_label(b):
    return "%d-%d" % b


def sample_fields(lo, hi, sign, nf):
    """A uniform stride over the band's fundamental discriminants."""
    ds = fundamental_discriminants(lo, hi, sign)
    if len(ds) <= nf:
        return ds
    step = len(ds) / nf
    return [ds[int(i * step)] for i in range(nf)]


def sweep_band(lo, hi, sign, plist, nf):
    """Per field: (D, h+, [n_d], [m_d], L_1, l) over the decades.

    l is the principal CYCLE LENGTH at D > 0 and 0 at D < 0, where a
    definite class is a single reduced form and there is no cycle."""
    out = []
    for D in sample_fields(lo, hi, sign, nf):
        if sign > 0:
            rt = isqrt(D)
            if rt * rt == D:
                continue
            hwide, hplus, _ = class_data_real(D, rt)
            pc = set(principal_cycle(D, rt))
            cyc = len(pc)
        else:
            cyc = 0
            hplus = class_number_imag(D)
            hwide = hplus            # narrow = wide, the units being roots
                                     # of unity
            b0 = D % 2
            pf = reduce_definite((1, b0, (b0 * b0 - D) // 4), D)
        n = [0] * ND
        m = [0] * ND
        l1 = None
        jj = 0                     # split primes examined so far
        jhit = None                # J: trials to the first NARROW principal
        jwide = None               # J_w: the same for WIDE principality
        for p in plist:
            if kronecker(D, p) != 1:
                continue
            jj += 1
            b = form_at(D, p)
            if sign > 0:
                nar, wid = principal_real(D, p, b, pc, rt)
            else:
                nar = principal_imag(D, p, b, pf)
                wid = nar
            i = dec_of(p)
            n[i] += 1
            if wid and jwide is None:
                jwide = jj
            if nar:
                m[i] += 1
                if l1 is None:
                    l1 = p
                    jhit = jj
        out.append((D, hplus, n, m, l1, cyc, jhit, hwide, jwide))
    return out


# ------------------------------------------------------------ the readings

def cell_ratios(rows, hplus, nmin, fixed_set):
    """Per-decade lists of the per-field ratio, for one h+ stratum.

    fixed_set: a field enters every decade or none (derivation (3))."""
    cols = [[] for _ in range(ND)]
    for D, hp, n, m, l1, cyc, jhit, hw, jw in rows:
        if hp != hplus:
            continue
        ok = [n[d] >= nmin for d in range(ND)]
        if fixed_set and not all(ok):
            continue
        for d in range(ND):
            if ok[d]:
                cols[d].append((m[d] / n[d]) * hp)
    return cols


def null_band(rows, hplus, nmin, fixed_set, rng):
    """C2: redistribute each field's own principal total over its own
    split primes, preserving the per-decade split counts and the level."""
    lo = [None] * ND
    hi = [None] * ND
    for _ in range(RDRAWS):
        cols = [[] for _ in range(ND)]
        for D, hp, n, m, l1, cyc, jhit, hw, jw in rows:
            if hp != hplus:
                continue
            ok = [n[d] >= nmin for d in range(ND)]
            if fixed_set and not all(ok):
                continue
            mm = rng.multivariate_hypergeometric(n, sum(m))
            for d in range(ND):
                if ok[d]:
                    cols[d].append((mm[d] / n[d]) * hp)
        for d in range(ND):
            if len(cols[d]) >= MINF:
                v = sum(cols[d]) / len(cols[d])
                lo[d] = v if lo[d] is None else min(lo[d], v)
                hi[d] = v if hi[d] is None else max(hi[d], v)
    return lo, hi


def fmt(v):
    return "%7s" % "-" if v is None else "%7.3f" % v


def print_table(all_rows, sign, hplus, nmin, fixed_set, rng, show_null):
    name = "real" if sign > 0 else "imaginary"
    print("\n  %s, h+ = %d   (nmin %d, fixed field set %s)"
          % (name, hplus, nmin, "on" if fixed_set else "off"))
    hdr = "    %-14s" % "|D| band"
    for lab in DEC_LABELS:
        hdr += " %16s" % lab
    print(hdr)
    any_row = False
    reach = []
    for b in DBANDS:
        rows = all_rows[(sign, b)]
        cols = cell_ratios(rows, hplus, nmin, fixed_set)
        if max(len(c) for c in cols) < MINF:
            continue
        any_row = True
        line = "    %-14s" % band_label(b)
        means = []
        for d in range(ND):
            if len(cols[d]) >= MINF:
                v = sum(cols[d]) / len(cols[d])
                means.append(v)
                line += " %8.3f(%5d)" % (v, len(cols[d]))
            else:
                means.append(None)
                line += " %16s" % "-"
        print(line)
        reach.append((b, means))
        if show_null:
            lo, hi = null_band(rows, hplus, nmin, fixed_set, rng)
            nline = "      %-12s" % "C2 null"
            for d in range(ND):
                nline += " %16s" % (
                    "-" if lo[d] is None else "%.3f-%.3f" % (lo[d], hi[d]))
            print(nline)
    if not any_row:
        print("    (no cell reaches %d fields)" % MINF)
    return reach


def reach_point(means, target=0.95):
    """K4: log10 p at which the row first reaches `target` of nominal,
    interpolated in log10 p between decade midpoints."""
    mid = [1.0, 2.5, 3.5, 4.5]
    prev = None
    for d in range(ND):
        v = means[d]
        if v is None:
            continue
        if v >= target:
            if prev is None:
                return None          # starts at or above target
            pv, pm = prev
            if v == pm:
                return mid[d]
            f = (target - pm) / (v - pm)
            return pv + f * (mid[d] - pv)
        prev = (mid[d], v)
    return None


def slope_fit(pts):
    """Least squares slope of reach against log10|D|, with residuals."""
    if len(pts) < 2:
        return None, None, len(pts)
    xs = [x for x, y in pts]
    ys = [y for x, y in pts]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    den = sum((x - mx) ** 2 for x in xs)
    if den == 0:
        return None, None, len(pts)
    sl = sum((x - mx) * (y - my) for x, y in pts) / den
    res = [y - (my + sl * (x - mx)) for x, y in pts]
    return sl, res, len(pts)


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    plist = [q for q in primes_upto(PCAP) if q != 2]
    print("ODD PRIMES to %d: %d" % (PCAP, len(plist)))
    print("bands: %s" % ", ".join(band_label(b) for b in DBANDS))
    print("fields sampled per band per sign: %d (uniform stride)" % NF)

    print("\n=== SWEEP ===")
    all_rows = {}
    for b in DBANDS:
        for sign in (+1, -1):
            t = time.time()
            all_rows[(sign, b)] = sweep_band(b[0], b[1], sign, plist, NF)
            print("  %-14s %-9s %5d fields   (%.1f s)"
                  % (band_label(b), "real" if sign > 0 else "imag",
                     len(all_rows[(sign, b)]), time.time() - t))

    # ---- C1: the instrument pin ----------------------------------------
    print("\n=== C1  INSTRUMENT PIN AT h+ = 1 (control, read first) ===")
    bad = tested = 0
    per = {+1: 0, -1: 0}
    for (sign, b), rows in all_rows.items():
        for D, hp, n, m, l1, cyc, jhit, hw, jw in rows:
            if hp != 1:
                continue
            tested += 1
            per[sign] += 1
            if any(m[d] != n[d] for d in range(ND)):
                bad += 1
    print("  h+ = 1 fields: %d (%d real, %d imaginary)   decades where "
          "principal != split: %d" % (tested, per[+1], per[-1], bad))
    if per[-1] == 0:
        print("  the imaginary count is 0 BY THEOREM, not by sampling: no")
        print("  imaginary quadratic field has class number 1 above")
        print("  |D| = 163, so this pin is a real-side control in this")
        print("  population, and the rig says so rather than reporting a")
        print("  coverage it does not have.")

    # ---- C3: the derived zero ------------------------------------------
    print("\n=== C3  THE DERIVED ZERO BELOW |D|/4 AT D < 0 (control) ===")
    bad3 = cells3 = 0
    for b in DBANDS:
        for D, hp, n, m, l1, cyc, jhit, hw, jw in all_rows[(-1, b)]:
            for d in range(ND):
                top = DEC_EDGES[d]
                if top < -D / 4:
                    cells3 += 1
                    if m[d]:
                        bad3 += 1
    print("  decade cells wholly below |D|/4: %d   with a principal prime: %d"
          % (cells3, bad3))

    # ---- C5: the breakdown against the figure it decomposes -------------
    print("\n=== C5  THE UNDECOMPOSED FIGURE, AGAINST THE PUBLISHED ONE "
          "(control) ===")
    print("  real fundamental discriminants |D| <= 4000, the incumbent's "
          "own population\n  and its own per-bin floors (8 below 100, 20 "
          "above); a different\n  principality path at a ten-times wider "
          "prime cap must reproduce it.")
    chk = sweep_band(0, 4000, +1, plist, 10 ** 9)
    print("    %-4s %6s %15s %15s %15s"
          % ("h+", "n", "p<=100", "100<p<=1000", "pooled p<=1000"))
    for hp, pub in ((2, (0.868, 0.949, 0.938)), (4, (0.630, 0.844, 0.815)),
                    (6, (0.414, 0.823, 0.764)), (8, (0.332, 0.714, 0.662))):
        col = [[], [], []]
        for D, h, n, m, l1, cyc, jhit, hw, jw in chk:
            if h != hp:
                continue
            if n[0] >= 8:
                col[0].append((m[0] / n[0]) * hp)
            if n[1] >= 20:
                col[1].append((m[1] / n[1]) * hp)
            if n[0] + n[1] >= 20:
                col[2].append(((m[0] + m[1]) / (n[0] + n[1])) * hp)
        line = "    %-4d %6d" % (hp, len(col[2]))
        for j in range(3):
            line += " %7.3f/%-7.3f" % (sum(col[j]) / len(col[j]), pub[j]) \
                if len(col[j]) >= 4 else " %15s" % "-"
        print(line)
    print("    (measured / published; the incumbent's population is |D| "
          "<= 4000 whole,\n     which is NOT any band above -- the bands "
          "start at 2000)")
    lchk = sorted(r[4] for r in chk if r[4] is not None)
    print("    THE LEAST PRINCIPAL SPLIT PRIME ON THAT SAME POPULATION, "
          "against the")
    print("    published L_1 figures of 94.2% at or below 100, mean 25.7, "
          "median 11:")
    print("      %.1f%% at or below 100, mean %.1f, median %d, on %d fields"
          % (100.0 * sum(1 for x in lchk if x <= 100) / len(lchk),
             sum(lchk) / len(lchk), lchk[len(lchk) // 2], len(lchk)))
    print("      THESE ARE NOT THE SAME QUANTITY and the control is here to")
    print("      say so. The corpus's L_1 is the least principal RANK-1")
    print("      CHARACTERISTIC, and a RAMIFIED p (p | D) carries a place of")
    print("      residue degree 1 too, so L_1 draws on primes this rig skips")
    print("      -- it counts split primes only. Ramified candidates can")
    print("      only LOWER a least, so the published figures must be the")
    print("      more optimistic ones on all three statistics, and they are.")
    print("      Everything this rig calls L_1 is the SPLIT one; P4 is")
    print("      therefore scored on its TREND across the bands and never on")
    print("      its level, and K5's medians are not comparable to the")
    print("      corpus's. K8 and K9 are unaffected: they count trials over")
    print("      split primes, which is the scan they describe.")

    # ---- C6: the imaginary share ABOVE its own floor --------------------
    print("\n=== C6  THE IMAGINARY SHARE IN THE DECADES WHOLLY ABOVE "
          "|D|/4 (control) ===")
    print("  The D < 0 verdict says the scan's range is pushed above the "
          "transient and\n  finds nominal there. That is the half of it "
          "the rig can check, and only\n  where a decade clears the floor "
          "AND the cap: pooled over all h+, since no\n  h+ is common "
          "across these bands.")
    print("  PER DECADE, because 'above |D|/4' is not 'clear of the "
          "floor': the density\n  rises continuously off the floor, so a "
          "decade STARTING at it sits in its\n  tail, which is the same "
          "defect as reading a gate at its own edge. The\n  CLEARANCE -- "
          "the decade's lower edge over |D|/4, median over the\n  "
          "contributing fields -- is printed so a cell near x1 can be "
          "discounted.")
    hdr = "    %-14s" % "|D| band"
    for lab in DEC_LABELS:
        hdr += " %21s" % lab
    print(hdr)
    for b in DBANDS:
        line = "    %-14s" % band_label(b)
        for d in range(ND):
            low = 3 if d == 0 else DEC_EDGES[d - 1]
            vals, clear = [], []
            for D, hp, n, m, l1, cyc, jhit, hw, jw in all_rows[(-1, b)]:
                if hp < 2 or n[d] < NMIN or low < -D / 4:
                    continue
                vals.append((m[d] / n[d]) * hp)
                clear.append(low / (-D / 4))
            if len(vals) >= MINF:
                clear.sort()
                line += " %8.3f(%4d,x%4.1f)" % (
                    sum(vals) / len(vals), len(vals), clear[len(clear) // 2])
            else:
                line += " %21s" % "-"
        print(line)
    print("    (share/nominal, fields, median clearance over |D|/4. A band "
          "blank\n     throughout has no decade above both its floor and "
          "the 10^5 cap -- a\n     limit of the rig, printed rather than "
          "argued past.)")

    # ---- K1/K2/K3: the table -------------------------------------------
    print("\n=== K1  SHARE / NOMINAL BY |D| BAND AND DECADE OF p ===")
    print("  (1.00 = no deficit; per-field mean, field count in parens)")
    reaches = {}
    for sign in (+1, -1):
        for hp in HPLUS:
            r = print_table(all_rows, sign, hp, NMIN, True, rng, True)
            if r:
                reaches[(sign, hp)] = r

    # ---- K4: the shift rate --------------------------------------------
    print("\n=== K4  WHERE THE ROW REACHES 0.95 OF NOMINAL, "
          "AGAINST log10|D| ===")
    print("    %-6s %-4s %-46s %8s" % ("sign", "h+", "reach log10 p by band",
                                       "slope"))
    for (sign, hp), r in sorted(reaches.items(), reverse=True):
        pts = []
        cells = []
        for b, means in r:
            rp = reach_point(means)
            x = log10((b[0] + b[1]) / 2.0)
            cells.append("-" if rp is None else "%.2f" % rp)
            if rp is not None:
                pts.append((x, rp))
        sl, res, n = slope_fit(pts)
        print("    %-6s %-4d %-46s %8s  (%d bands%s)"
              % ("real" if sign > 0 else "imag", hp, " ".join(cells),
                 "-" if sl is None else "%.3f" % sl, n,
                 "" if res is None else ", resid " +
                 " ".join("%+.2f" % v for v in res)))

    # ---- K5: the consumer column ---------------------------------------
    print("\n=== K5  WHERE A SCAN ACTUALLY STOPS: THE LEAST PRINCIPAL "
          "SPLIT PRIME BY BAND ===")
    print("  (NARROW principality; NOT the corpus's L_1, which is the WIDE "
          "notion -- C5\n   measures the gap. Read the trend "
          "across the bands, not the level.)")
    print("    %-6s %-14s %6s %8s %8s %8s %8s"
          % ("sign", "|D| band", "fields", "med L_1", "L1>100", "L1>10^3",
             "L1>10^4"))
    for sign in (+1, -1):
        for b in DBANDS:
            rows = all_rows[(sign, b)]
            ls = sorted(x[4] for x in rows if x[4] is not None)
            if not ls:
                print("    %-6s %-14s %6d %8s %8s %8s %8s"
                      % ("real" if sign > 0 else "imag", band_label(b),
                         len(rows), "none", "-", "-", "-"))
                continue
            med = ls[len(ls) // 2]
            f = len(rows)
            print("    %-6s %-14s %6d %8d %7.3f %7.3f %7.3f"
                  % ("real" if sign > 0 else "imag", band_label(b), f, med,
                     sum(1 for x in ls if x > 100) / f,
                     sum(1 for x in ls if x > 1000) / f,
                     sum(1 for x in ls if x > 10000) / f))

    # ---- K6: the cycle length against |D|, at fixed h+ ------------------
    print("\n=== K6  THE BOTTOM DECADE BY |D| BAND AND PRINCIPAL CYCLE "
          "LENGTH ===")
    print("  (real side only -- a definite class has no cycle; terciles of "
          "l are\n   global at each h+, so a row and a column are the same "
          "field set cut two ways)")
    for hp in HPLUS:
        pool = []
        for b in DBANDS:
            for r in all_rows[(+1, b)]:
                if r[1] == hp and r[2][0] >= NMIN:
                    pool.append((b, r[5], (r[3][0] / r[2][0]) * hp))
        if len(pool) < 3 * MINF:
            continue
        ls = sorted(x[1] for x in pool)
        c1 = ls[len(ls) // 3]
        c2 = ls[2 * len(ls) // 3]
        print("\n  h+ = %d   l terciles at %d and %d   (%d fields)"
              % (hp, c1, c2, len(pool)))
        print("    %-14s %16s %16s %16s %16s"
              % ("|D| band", "l < %d" % c1, "%d <= l < %d" % (c1, c2),
                 "l >= %d" % c2, "all l"))
        for b in DBANDS:
            cells = [[], [], [], []]
            for bb, lcyc, v in pool:
                if bb != b:
                    continue
                j = 0 if lcyc < c1 else (1 if lcyc < c2 else 2)
                cells[j].append(v)
                cells[3].append(v)
            line = "    %-14s" % band_label(b)
            for j in range(4):
                line += " %16s" % (
                    "%.3f(%4d)" % (sum(cells[j]) / len(cells[j]),
                                   len(cells[j]))
                    if len(cells[j]) >= MINF else "-")
            print(line)
        line = "    %-14s" % "all bands"
        for j in range(4):
            v = [x[2] for x in pool
                 if j == 3 or (0 if x[1] < c1 else (1 if x[1] < c2 else 2)) == j]
            line += " %16s" % ("%.3f(%4d)" % (sum(v) / len(v), len(v))
                               if len(v) >= MINF else "-")
        print(line)

    # ---- K7: the same contrast, terciles taken WITHIN a band ------------
    print("\n=== K7  TOP-MINUS-BOTTOM l TERCILE, TERCILES TAKEN WITHIN "
          "EACH BAND ===")
    print("    %-4s %-14s %6s %8s %8s %9s %8s"
          % ("h+", "|D| band", "n", "low l", "high l", "contrast", "s.e."))
    for hp in HPLUS:
        num = den = 0.0
        shown = 0
        for b in DBANDS:
            vs = [(r[5], (r[3][0] / r[2][0]) * hp)
                  for r in all_rows[(+1, b)]
                  if r[1] == hp and r[2][0] >= NMIN]
            if len(vs) < 3 * MINF:
                continue
            # Sort on l ALONE. A bare tuple sort tie-breaks on the second
            # element, which is the ratio being contrasted, so equal-l
            # fields would be split low-ratio into the bottom tercile and
            # high-ratio into the top -- a control biased in the direction
            # of the effect it tests. Python's sort is stable, so ties keep
            # the sweep's own order, which is by |D|.
            vs.sort(key=lambda t: t[0])
            k = len(vs) // 3
            lo = [v for _, v in vs[:k]]
            hi = [v for _, v in vs[-k:]]
            ml = sum(lo) / len(lo)
            mh = sum(hi) / len(hi)
            vl = sum((x - ml) ** 2 for x in lo) / max(1, len(lo) - 1)
            vh = sum((x - mh) ** 2 for x in hi) / max(1, len(hi) - 1)
            se = (vl / len(lo) + vh / len(hi)) ** 0.5
            print("    %-4d %-14s %6d %8.3f %8.3f %9.3f %8.3f"
                  % (hp, band_label(b), len(vs), ml, mh, mh - ml, se))
            shown += 1
            if se > 0:
                num += (mh - ml) / se ** 2
                den += 1.0 / se ** 2
        if shown >= 2:
            print("    %-4d %-14s %6s %8s %8s %9.3f %8.3f   <-- pooled "
                  "over %d bands"
                  % (hp, "POOLED", "", "", "", num / den, den ** -0.5, shown))

    # ---- K8: the overshoot in the consumer's own units ------------------
    print("\n=== K8  TRIALS TO THE FIRST PRINCIPAL SPLIT PRIME, AGAINST "
          "THE UNIFORM MODEL ===")
    print("  (J = split primes examined. THE MEAN IS THE READING and the "
          "median is\n   printed beside it as the thing NOT to read: a "
          "geometric median at small\n   h+ is a small integer, so its "
          "overshoot is quantized and a ratio stable\n   across the lever "
          "may be one trial's difference throughout. The model mean\n   is "
          "exactly h+, with no fitted constant.)")
    print("    %-6s %-4s %-14s %6s %8s %9s %7s %7s %8s"
          % ("sign", "h+", "|D| band", "n", "mean J", "mean/h+ +- s.e.",
             "med J", "med mdl", "censored"))
    for sign in (+1, -1):
        for hp in HPLUS:
            for b in DBANDS:
                rows = [r for r in all_rows[(sign, b)] if r[1] == hp]
                if len(rows) < MINF:
                    continue
                js = sorted(r[6] for r in rows if r[6] is not None)
                cens = 1.0 - len(js) / len(rows)
                if not js:
                    continue
                q = 1.0 - 1.0 / hp
                j = 1
                while 1.0 - q ** j < 0.5:
                    j += 1
                mj = js[len(js) // 2]
                avg = sum(js) / len(js)
                sd = (sum((x - avg) ** 2 for x in js)
                      / max(1, len(js) - 1)) ** 0.5
                se = sd / len(js) ** 0.5 / hp
                print("    %-6s %-4d %-14s %6d %8.2f %6.3f+-%.3f %7d %7d "
                      "%8.3f%s"
                      % ("real" if sign > 0 else "imag", hp, band_label(b),
                         len(rows), avg, avg / hp, se, mj, j, cens,
                         "  CENSORED" if cens > 0 else ""))

    # ---- K9: the same, in the WIDE vocabulary ---------------------------
    print("\n=== K9  THE SAME TRIALS READING FOR WIDE PRINCIPALITY ===")
    print("  (J_w = split primes to the first WIDE-principal one -- a "
          "generator, not a\n   totally positive one -- against the "
          "uniform model's exact mean of the WIDE\n   h. Strata are by h "
          "here and not by h+, which is the whole point.)")
    print("    %-6s %-4s %-14s %6s %8s %9s %8s"
          % ("sign", "h", "|D| band", "n", "mean J_w", "mean/h",
             "censored"))
    for sign in (+1, -1):
        for hw0 in HPLUS:
            for b in DBANDS:
                rows = [r for r in all_rows[(sign, b)] if r[7] == hw0]
                if len(rows) < MINF:
                    continue
                js = sorted(r[8] for r in rows if r[8] is not None)
                cens = 1.0 - len(js) / len(rows)
                if not js:
                    continue
                avg = sum(js) / len(js)
                sd = (sum((x - avg) ** 2 for x in js)
                      / max(1, len(js) - 1)) ** 0.5
                print("    %-6s %-4d %-14s %6d %8.2f %6.3f+-%.3f %8.3f%s"
                      % ("real" if sign > 0 else "imag", hw0, band_label(b),
                         len(rows), avg, avg / hw0,
                         sd / len(js) ** 0.5 / hw0, cens,
                         "  CENSORED" if cens > 0 else ""))

    # ---- C4: the gates swept -------------------------------------------
    print("\n=== C4  THE GATES, EACH AT TWO SETTINGS ===")
    for label, nmin, fixed in (("nmin 3, fixed on", 3, True),
                               ("nmin 6, fixed on (the setting)", 6, True),
                               ("nmin 12, fixed on", 12, True),
                               ("nmin 6, fixed OFF", 6, False)):
        print("\n  -- %s --" % label)
        print_table(all_rows, +1, 4, nmin, fixed, rng, False)
    print("\n  -- field sample halved (stride over the same bands) --")
    half = {}
    for b in DBANDS:
        half[(+1, b)] = all_rows[(+1, b)][::2]
    print_table(half, +1, 4, NMIN, True, rng, False)

    print("\nwall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
