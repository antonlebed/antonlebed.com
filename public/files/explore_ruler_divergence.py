"""explore_ruler_divergence.py -- THE RULER'S NEXT RUNG: THE
DIVERGENCE/MST FAMILY OF BAYES-ERROR ESTIMATORS SCORED AGAINST THE
CLOSED FORM (sibling of explore_ceiling_ruler.py, which scored the
three elementary protocols, and explore_ruler_boundary.py, which
re-ran their failures ring-free).

THE QUESTION. The ruler's first run scored two plug-in protocols and
one distribution-free bracket, and its own stated limit (c) is that
"the divergence- and MST-based estimators are untouched and are the
obvious next rung". Those are a different estimator FAMILY, not
another protocol: they never fit a rule and never score one. They
estimate a DIVERGENCE between the two class-conditional laws from a
GEOMETRIC GRAPH on the pooled sample, and turn it into a Bayes-error
bracket through a theorem. So: does the divergence family recover
this family's closed form where the plug-ins fail, and where does it
fail itself?

THE ESTIMATOR (one family, two regimes, plus its own exact limit).
  E3 THE HENZE-PENROSE / FRIEDMAN-RAFSKY ESTIMATOR. Build the
     minimum spanning tree of the POOLED sample under the evidence
     metric; let R be the number of tree edges whose endpoints carry
     different labels. The Henze-Penrose divergence estimate is
        Dhat = 1 - R (n0 + n1) / (2 n0 n1),
     and the Berisha-Hero bracket on the Bayes error is
        (1 - sqrt(u))/2  <=  R*  <=  (1 - u)/2,
        u = 4 p q Dhat + (p - q)^2,   p = n1/n,  q = n0/n.
     STATED ERROR BAR, as a practitioner would report it: the
     binomial 95% bar on rhat = R/n, both endpoints pushed out
     before the (decreasing) maps, exactly the hygiene E2 was given.
     The rig also prints the ACROSS-TRIAL SD of rhat beside that
     bar, because the MST's edges are dependent and the binomial bar
     is a naive stand-in whose price is measurable here.

  THE TWO REGIMES ARE THE POINT, AND THEY ARE NOT A ROBUSTNESS LEG.
  On a CATEGORICAL evidence channel the MST is not unique: every
  pair of points sharing a residue tuple sits at distance 0, so the
  0-weight edges inside a cell admit any spanning tree of that
  cell's clique, and each of them is a genuine minimum spanning
  tree. R is therefore not identified by the data. The two regimes
  are the two orderings a practitioner actually hands the algorithm:
    E3r RANDOM ties -- each cell's chain is an explicit random
        permutation of its points. The draw order is already random,
        so the shuffle changes no distribution; it makes the regime
        independent of how the rows happened to arrive, which is the
        property the jitter fix has and the one being tested.
    E3g GROUPED ties -- the sample as X = concatenate([X0, X1]),
        which is how two class arrays are usually assembled and what
        a deterministic MST routine then chains. Inside a cell every
        class-0 point precedes every class-1 point.
  Nothing about the DATA differs between them.

THE THIRD CLOSED FORM THE FAMILY HANDS OVER, derived below and
asserted before any estimate is read: u has an exact population
value on every cell of the threshold family,
        u_p = E[(2 eta_r - 1)^2] = (1/M) sum_r ((c - 2 B(r))/c)^2,
so the bracket's exact endpoints are available in Fraction, and the
ruler prices the divergence estimator's own limit the way it already
prices 1-NN's (explore_ceiling_ruler.py finding 8).

DESIGN. The same five cells, the same four sample sizes, the same
TRIALS = 40 and the same fixed seed as the first run, so the two
families are read on one grid; the sampler, the exact truth, the
no-evidence value and the 1-NN asymptote are IMPORTED from
explore_ceiling_ruler.py rather than re-implemented. Plus the same
profile leg (N = 105, t = 38..67, n = 8000), which is what crosses
the window edge. Exact truth in Fraction throughout.

CONTROLS (run and asserted before any estimate is read).
  K0 THE POSITIVE CONTROL: the same two-cell Bernoulli problem the
     first run used -- eta = (0.2, 0.9), R* = 0.15 -- carried
     through the same sampler interface and the new estimator. Its
     u_p = ((0.6)^2 + (0.8)^2)/2 = 0.5 exactly, so the exact bracket
     is [0.1464, 0.2500]: it contains R* and, unlike the threshold
     cells, does NOT contain it at an endpoint, because |2 eta - 1|
     takes two values there. E3r must recover u to within 0.02 at
     n = 8000, cover R*, and exclude the no-evidence value 0.45.
     This is the run where the estimator is KNOWN to work; nothing
     else is read until it passes.
  K1 THE IDENTITY CONTROL: (1 - u_p)/2 must equal the 1-NN
     asymptote of explore_ceiling_ruler.py, in Fraction, on every
     cell and every profile threshold. That is not a coincidence to
     be noticed after the fact -- it is the algebra
     (1 - E[(2eta-1)^2])/2 = E[2 eta (1 - eta)] -- and if it ever
     failed, one of the two closed forms would be wrong.
  K2 THE ALGEBRA CONTROL: the Berisha-Hero u computed through the
     stated Dhat/p/q route must equal 1 - 2R/n to 1e-9 on every
     trial, since 4 n0 n1 + (n0 - n1)^2 = n^2. It is asserted rather
     than used, so a mis-transcribed formula cannot pass silently.
  K3 THE JITTER CONTROL: at n = 500 on FLOOR-ODD, embed each cell at
     (r mod 3, r mod 5), add uniform jitter of 0.01 (far below the
     inter-cell spacing 1), and compute the EXACT Euclidean MST by
     Prim. Its SAME-CELL cross-class edge count must agree with the
     E3r regime's within-cell count within sampling noise. That is
     what licenses reading E3r as the jitter fix rather than as a
     convenience: the control is scoped to the within-cell edges,
     which is the only place the tie-break acts.
  K4 the imported truth and sampler controls of the first run
     (fiber-count = closed form; cell and label frequencies), re-run
     here because this file's grid depends on them.

HAND DERIVATION (fixed before the engine; the index convention
re-derived from the imported rig, not recalled: x in {0..N-1},
residue r has fiber {r + jM : j = 0..c-1}, t = qM + s with
0 <= s < M, below-count B(r) = q + [r < s], eta_r = (c - B(r))/c).

  1. u_p = E[(2 eta - 1)^2]. Writing the class-1 prior p with
  density f1 and class 0 with q, f0, one has p f1(r) = P(r) eta_r
  and q f0(r) = P(r)(1 - eta_r), so
     4 p q D_p + (p-q)^2 = sum_r (p f1 - q f0)^2/(p f1 + q f0)
                         = sum_r P(r) (2 eta_r - 1)^2.
  With P(r) = 1/M and 2 eta_r - 1 = (c - 2 B(r))/c this is the
  closed form stated above.

  2. THE UPPER BOUND IS THE 1-NN ASYMPTOTE. (1 - u_p)/2 =
  E[(1 - (2 eta - 1)^2)/2] = E[2 eta (1 - eta)], which is exactly
  the quantity explore_ceiling_ruler.py finding 8 derived as 1-NN's
  limit. So on ANY family the Henze-Penrose upper bound and the
  asymptotic 1-NN error are the same number, and the two estimator
  families are not bracketing the truth from different sides -- they
  are two statistics for ONE bracket. (Cover-Hart's lower endpoint
  is likewise (1 - sqrt(1 - 2 R_NN))/2, which is (1 - sqrt(u))/2
  under the same substitution.) What separates E2 from E3 is
  therefore not the bound but how the shared quantity is measured:
  E2 fits and scores a rule on half the sample, E3 counts edges on
  all of it and fits nothing.

  3. WHERE THE LOWER BOUND IS TIGHT. R* = 1/2 - E|2 eta - 1|/2 and
  the lower bound is 1/2 - sqrt(E[(2 eta - 1)^2])/2, so the gap is
  exactly the Jensen gap of |2 eta - 1|: the bound is TIGHT iff
  |2 eta - 1| is CONSTANT across cells. Here B(r) takes the two
  values q and q+1, so |c - 2B| takes |c - 2q| and |c - 2q - 2|,
  equal iff c - 2q - 1 = 0, i.e. c odd and q = (c-1)/2 -- which is
  the odd-c middle window -- or iff s = 0, where B is constant.
  THE TIGHTNESS SET OF THE HENZE-PENROSE BOUND IS EXACTLY THE
  FAMILY'S OWN WINDOW (together with the s = 0 thresholds). All five
  grid cells have s = 0 or sit in the window, so the exact lower
  endpoint equals R* at every one of them; the profile leg is where
  a strictly conservative endpoint can be seen at all.

  4. WHY THE KNIFE CELL BREAKS THIS ESTIMATOR TOO, AND DIFFERENTLY.
  At FLOOR-KNIFE every eta_r = 1/2, so u_p = 0 and the exact bracket
  is the POINT [1/2, 1/2]. But u is estimated as 1 - 2 rhat with
  rhat concentrating at 1/2, so uhat fluctuates around 0 with SD of
  order 1/sqrt(n), and the lower endpoint moves as sqrt(uhat) --
  the square-root map is singular exactly at u = 0. The lower
  endpoint's error is therefore of order n^{-1/4}, not n^{-1/2}:
  the cell that made a resubstitution INTERVAL inconsistent makes
  the divergence bracket converge at a fourth root, by an unrelated
  mechanism (a singular map rather than a self-cancelling ratio).
  The upper endpoint at that cell is (1 - max(uhat_lo, 0))/2, which
  clips to exactly 1/2 whenever the bar reaches rhat = 1/2 -- the
  truth -- so coverage there is an artifact of the clip and not
  evidence, the same caveat E2's FLOOR-KNIFE column carries.

  5. WHAT THE GROUPED REGIME DOES. Chained in class order, a cell's
  spanning path has exactly ONE cross-class edge if both labels are
  present and none otherwise, so R is at most (#occupied cells) plus
  the (#occupied - 1) between-cell edges, independent of n. Then
  rhat = R/n -> 0, uhat -> 1, and both bracket endpoints -> 0: the
  estimate does not merely degrade with more data, it converges to
  the assertion that the classes are perfectly separable.

PREDICTIONS (fixed before the run).
  H1 The exact lower endpoint (1 - sqrt(u_p))/2 equals R* at all
     five cells; the exact upper endpoint equals the 1-NN asymptote
     (1/2, 24/49, 24/49, 24/49, 60/121). Both in Fraction.
  H2 On the profile the exact lower endpoint equals R* at every
     in-window threshold and at t = 45, 60 (s = 0), and is strictly
     below R* at every other threshold: gap 0.0173 at t = 38
     (0.3446 against 38/105) and 0.0075 at t = 44 (0.4116 against
     44/105), symmetrically above 60.
  H3 E3r's rhat converges to the 1-NN asymptote: |rhat - asymptote|
     < 0.01 at every cell at n = 32000.
  H4 E3g collapses at every cell: its reported interval lies
     entirely below 0.05 at n >= 8000 against truths 0.43-0.50, its
     coverage is 0.00 there, and rhat FALLS monotonically in n.
  H5 At FLOOR-KNIFE, E3r's point lower endpoint is biased down by
     about -0.09, -0.07, -0.05, -0.03 across the four n, each step
     shrinking by ~1.41 rather than by 2 -- the fourth-root
     signature -- while its reported coverage reads 1.00 through the
     upper clip.
  H6 THE BOUND IS TOO WEAK IN THE WINDOW EVEN WITH EXACT KNOWLEDGE.
     The exact bracket [3/7, 24/49] contains the no-evidence value
     min(t, 105-t)/105 at every in-window threshold whose naive
     value is below 24/49 = 0.4898, i.e. it certifies a lift at
     exactly 2 of the 14 in-window thresholds (t = 52 and t = 53,
     naive 52/105 = 0.4952). With the sampling bar at n = 8000 it
     certifies a lift at 0 of 14 -- agreeing with E2's 14-of-14
     containment for a reason that is not sampling noise.
  H7 The naive binomial bar on rhat is not the MST's actual
     dispersion: the across-trial SD of rhat differs from
     sqrt(rhat(1-rhat)/n) by more than 10% at FLOOR-WIDE at n = 500,
     where between-cell edges are a fifth of the tree.

KILL (observable, frozen before the run). E3r's reported 95%
interval covers the exact truth at nominal rate (coverage >= 0.90)
at every cell at every n, AND its width at the window cells is below
the tent 0.0667 it would have to resolve at n = 32000. Then the
divergence family recovers this family's truth where the plug-ins
did not, the ruler's customer is the elementary protocols only, and
the instrument reading narrows to them. What a MISS buys is weighed
after the run, not encoded here.

FINDINGS (tier-labeled; run record below; the kill did not fire --
E3r's coverage clause was met and its width clause missed, which is
the two-slack verdict of finding 6).

1. THE FAMILY HANDS OVER A THIRD CLOSED FORM, AND IT IS THE SECOND
   ONE SEEN AGAIN (rule; derived by hand, confirmed in Fraction on
   all 35 (cell, t) slices). u_p = (1/M) sum_r ((c - 2B(r))/c)^2 is
   0, 1/49, 1/49, 1/49 and 1/121 on the five cells, so the exact
   Henze-Penrose bracket is [1/2, 1/2], [3/7, 24/49] three times,
   and [5/11, 60/121]. Its UPPER endpoint equals the 1-NN asymptote
   of explore_ceiling_ruler.py finding 8 on every slice, because
   (1 - E[(2eta-1)^2])/2 = E[2 eta (1 - eta)] identically. THE TWO
   ESTIMATOR FAMILIES ARE NOT TWO BRACKETS. Cover-Hart's endpoints
   are (1 - sqrt(1 - 2 R_NN))/2 and R_NN; Berisha-Hero's are
   (1 - sqrt(u))/2 and (1 - u)/2 with u = 1 - 2 rhat. They are ONE
   bracket read at two statistics for the same population quantity,
   so adding the divergence family buys a different ESTIMATOR of it
   and never a different bound.

2. THE BOUND'S TIGHTNESS SET IS THE FAMILY'S OWN WINDOW (rule;
   derived, confirmed across the 30-threshold profile). The lower
   endpoint's gap is exactly the Jensen gap of |2 eta - 1|, so it
   vanishes iff that is CONSTANT across cells -- which happens iff
   s = 0 or c is odd with q = (c-1)/2, and the second condition IS
   the odd-c middle window. So on t = 45..60 the exact lower
   endpoint equals R* to the digit, and off it the endpoint is
   strictly conservative: 0.3446 against 38/105 at t = 38, 0.4116
   against 44/105 at t = 44, the largest gap 0.0178 sitting at
   t = 39 and its mirror 66, not at the profile's ends. A window
   to make a plug-in's plateau visible turns out to be the exact
   equality case of an unrelated divergence bound.

3. THE BOUND IS TOO WEAK TO CERTIFY THE FAMILY'S OWN LIFT, WITH OR
   WITHOUT DATA (computed; the profile leg). Across the 14
   in-window thresholds the EXACT bracket [3/7, 24/49] excludes the
   no-evidence value at 2 of them (t = 52 and 53, naive 52/105 =
   0.4952 above 24/49 = 0.4898) and contains it at the other 12.
   With the sampling bar at n = 8000 it certifies at 0 of 14. That
   reproduces E2's 14-of-14 containment (finding 6 of the first
   run) and sharpens its reading: the distribution-free bracket was
   not empty because it was noisy, it was empty because the bound
   itself is, and the divergence family inherits the same emptiness
   through the same population quantity. Correct and empty is a
   property of the BOUND on this family, not of a protocol.

4. THE MST IS NOT IDENTIFIED BY THE DATA HERE, AND THE DEFAULT
   ORDERING IS THE BAD ONE (computed; mechanism derived). On a
   categorical channel every same-cell pair sits at distance 0, so
   each cell's points admit any spanning tree of its clique and
   every one of them is a genuine MST. Chained in class order --
   what X = concatenate([X0, X1]) hands a deterministic routine --
   a cell contributes exactly ONE cross edge if both labels are
   present, so R is set by the cell COUNT and not by the labels:
   rhat runs 0.0300, 0.0075, 0.0019, 0.0005 across the four n at
   EVERY M = 15 cell, identically at FLOOR-KNIFE (R* = 1/2) and at
   the three cells with R* = 3/7, with across-trial SD 0.0000. Its
   reported interval there lies below 0.0113 at n = 2000 and below
   0.0007 at n = 32000; at FLOOR-WIDE, where M = 105 sets a
   proportionately larger floor, below 0.0623 and 0.0039. Coverage
   is 0.00 at every cell at every n, and the
   estimate converges to the assertion that the classes are
   perfectly separable. A shuffle of the input rows -- no change to
   the data -- moves the same estimator to 0.4897, and finding 5
   says what the shuffle is actually buying.
   AND THE TWO REGIMES ARE NOT THE EXTREMES, they are two points in
   a range that covers the whole answer (derived, not measured).
   Since a cell's 0-weight edges admit ANY spanning tree of its
   clique, they admit a spanning tree of the complete BIPARTITE
   graph between its two label classes -- available whenever both
   are present -- whose n_r - 1 edges are ALL cross. So R ranges
   over roughly [M, n - 1] across genuine MSTs of one sample, rhat
   over [M/n, 1], and the reported bracket from [0, 0] to
   [1/2, 1/2]: the identified set is the entire interval a binary
   Bayes error can occupy. Non-identification here is not a
   perturbation of an answer, it is the absence of one.

5. WHAT THE FIX ACTUALLY REQUIRES IS LABEL-INDEPENDENCE, NOT
   RANDOMNESS (computed + controlled; the criterion derived). E3r's
   rhat at n = 32000 is 0.5000, 0.4897, 0.4896, 0.4896, 0.4953
   against exact asymptotes 0.5000, 0.4898, 0.4898, 0.4898, 0.4959.
   But randomness is not what earns that: for ANY within-cell tree
   whose SHAPE does not consult the labels, the labels are exchange-
   able across its n_r - 1 edges and the expected cross count is
   2 n_r1 n_r0 / n_r whatever the tree -- which is the population
   quantity. So a deterministic order is fine and a random one
   buys nothing extra; what E3g does wrong is not being determinis-
   tic but being label-CORRELATED, and concatenating two class
   arrays makes the row order BE the label. K3 is the case in hand:
   the exact Euclidean MST on the jittered embedding builds a
   within-cell tree by geometry, which the labels do not touch, and
   it gives 233.1 same-cell cross edges against E3r's 239.8
   (1.39 SE, a Poisson bound on the count and so a conservative
   one) at n = 500 -- two structurally unrelated label-blind trees
   agreeing, which is the criterion and not a coincidence.

6. ITS COVERAGE IS HIGH FOR TWO WRONG REASONS AT ONCE (computed;
   the whole grid). E3r covers 0.95-1.00 at every cell at every n,
   and neither reason is accuracy. That it covers everywhere is not
   news on its own -- E2 did too, at 0.90-1.00 -- and finding 1
   says why it could hardly have done otherwise: the two are the
   same bracket. What is new is the pricing of the slack. (a) The
   bound is loose: the truth sits AT the bracket's lower endpoint
   on all five cells (finding 2), so covering it costs the
   estimator nothing at the top. (b) The stated bar overstates the
   statistic's real dispersion by a factor of 1.75 to 2.75 at every
   cell and every n: the across-trial SD of rhat runs
   0.0224-0.0251 against a binomial bar of 0.0438 at n = 500 and
   0.0020-0.0025 against 0.0055 at n = 32000, because the MST's
   n-1 edges are strongly dependent (each cell contributes a FIXED
   edge count). The width pays for
   both: 0.0838 at the window cells at n = 32000, against the
   0.0667 tent it would have to resolve -- which is why the kill's
   coverage clause was met and its width clause was not. High
   coverage from a loose bound and a slack bar is the exact mirror
   of E1a's 0.00 from a tight bar around a biased point, and only a
   ruler tells the two apart.

7. THE KNIFE CELL DEGRADES THIS FAMILY TOO, THROUGH A SINGULAR MAP
   (observation; derived rate, confirmed at four n). At FLOOR-KNIFE
   u_p = 0, where d/du of (1 - sqrt u)/2 is unbounded, so the
   estimated lower endpoint moves as the square root of an O(1/sqrt
   n) fluctuation. Its bias runs -0.0413, -0.0319, -0.0282, -0.0133
   over n = 500..32000: a shrink of 3.10 across a 64-fold increase
   in n, against 2.83 for a fourth root and 8.00 for a square root.
   The cell that made a resubstitution INTERVAL inconsistent
   (finding 3 of the first run) slows a divergence bracket to a
   fourth-root rate by an unrelated mechanism, and the two are
   visible as the same cell only because the truth there is exact.
   Its coverage reads 1.00 at three of the four n and 0.95 at the
   fourth, and reads it through the upper endpoint's clip at 1/2
   rather than through the estimator -- the same artifact E2's
   FLOOR-KNIFE column carries, and not evidence. The clip binds
   whenever rhat + bar reaches 1/2, which is why the one slice that
   misses is a slice where it did not.

8. THE PLATEAU SURVIVES IN SHAPE AND NOT IN LEVEL (computed; the
   profile leg). E3r's sampled lower endpoint across the 14
   in-window thresholds runs 0.3937-0.4000, a spread of 0.0063
   against the 0.0667 tent it must not follow -- so the divergence
   family reproduces the plateau as cleanly as the plug-ins did
   (finding 7 of the first run) while sitting 0.032 below it.
   The plateau is therefore a discriminator that survives a change
   of estimator FAMILY, which is more than the first run could say
   of it.

THE PREDICTION LEDGER (every frozen prediction adjudicated, the
refuted ones included).
  H1 CONFIRMED in Fraction on all five cells and all 35 slices.
  H2 CONFIRMED, both quoted gaps to the digit (0.3446 at t = 38,
     0.4116 at t = 44). The prediction implied the gap grows away
     from the window; it does not -- the maximum over the profile
     is 0.0178 at t = 39 and its mirror 66, not at the ends.
  H3 CONFIRMED (worst |rhat - asymptote| 0.0006, at FLOOR-WIDE).
  H4 CONFIRMED in every clause, and the run adds the sharper form
     the prediction missed: the grouped statistic is not merely
     collapsing, it is CONSTANT across cells of equal M and has
     zero across-trial variance -- it has stopped reading the
     labels at all (finding 4).
  H5 SPLIT. The mechanism and the RATE hold (3.10 against 2.83 for
     a fourth root, 8.00 for a square root); the coverage clause
     predicted a flat 1.00 and got 1.00 at three n and 0.95 at the
     fourth, the clip binding at three of four. The magnitudes were about
     twice too large -- predicted -0.09/-0.07/-0.05/-0.03 against
     -0.0413/-0.0319/-0.0282/-0.0133 -- because the derivation
     averaged sqrt|uhat| over all trials where the clip at u = 0
     zeroes the penalty on the half with rhat > 1/2. The factor is
     the clip, not the rate.
  H6 CONFIRMED exactly: 2 of 14 from the exact bracket, 0 of 14
     with the bar, and the named thresholds are t = 52 and 53.
  H7 CONFIRMED at FLOOR-WIDE at n = 500 (0.0224 against 0.0438) and
     then some -- the gap is not a small-n or wide-cell effect but
     a uniform factor of about two at every cell and every n, which
     is what finding 6(b) reads.

WHAT THE MISS BUYS, weighed after the run. The first run's reading
was that standard Bayes-error protocols fail this family's designed
cells structurally, from a sample of three elementary protocols.
A second estimator FAMILY -- different in kind: no fitted rule, no
train/test split, a graph statistic and a divergence theorem --
fails on the same cells, and the two failures do not overlap:
the plug-ins' intervals are wrong (findings 3 and 4 of the first
run), the divergence bracket's interval is RIGHT and useless
(finding 6 here), and one of its two equally valid tie regimes is
catastrophic on data nothing distinguishes (finding 4). The
structural reading survives the widening, with one claim RETRACTED
in scope by finding 1: the divergence family is not an independent
check on the Cover-Hart result, because both bounds are the same
functional of the same population quantity. What the ruler measured
is the STATISTIC, not a second opinion on the bound. The hunt's
graduation verdict is untouched: still toy-scale, still no
field-scale artifact.

HONEST LIMITS. (a) One estimator family, two tie regimes; the
k-NN-graph variant of the same divergence and the ensemble-of-
orthogonal-MSTs variance reduction are untouched. (b) The stated
bar is the naive binomial one a practitioner reaches for; a
bootstrap bar would be wider or narrower by an amount this run
measures (finding 6b) but does not itself compute. (c) The tie
regimes are the two orderings that arise in practice, not a census
of the spanning trees; what the census WOULD say is derived in
finding 4 and not measured here. (d) 0-1 score
and uniform prior only, as in the first run: the tilt dial remains
untouched. (e) K3 is scoped to the WITHIN-cell edges, which is
where the tie-break acts; the jittered embedding's between-cell
tree is Euclidean and the rig's is Hamming, and those are not the
same tree.

RUN RECORD (this file, python explore_ruler_divergence.py, ~9 s):
  K1/K4 identity + truth control: (1 - u_p)/2 = the 1-NN asymptote
     and the fiber count = the closed form on all 35 slices; the
     sampler half at N = 1155, n = 200000 -- worst cell deviation
     3.36 SE, label rate 0.54609 against the exact 0.54545 (0.57 SE)
     -- pass.
  K0 positive control: eta = (0.2, 0.9), exact u_p = 0.5000, exact
     bracket [0.1464, 0.2500] with R* = 0.15 strictly inside; E3r at
     n = 8000 gives uhat 0.5007, interval [0.1396, 0.2591],
     coverage 1.00, no-evidence 0.45 excluded -- pass.
  K2 algebra control: asserted inside every est_hp call, all pass.
  K3 jitter control: 233.1 against 239.8 same-cell cross edges
     (1.39 SE) -- pass.
  grid: 5 cells x 4 sample sizes x 2 regimes x 40 trials, printed
     above; E3r coverage 0.95-1.00 throughout, E3g 0.00 throughout.
  profile: 30 thresholds at n = 8000, 40 trials; exact bracket
     certifies at 2 of 14 in-window, sampled at 0 of 14; largest
     exact lower-end gap outside the window 0.0178.
  all controls green.

RUN: python explore_ruler_divergence.py
  (bounded: 5 cells x 4 sample sizes x 40 trials x 2 regimes, a
  30-threshold profile leg at n = 8000, and one O(n^2) jitter
  control at n = 500; pure Python, no BLAS, well under the 512 MB
  ceiling; estimated 1-3 minutes, measured ~9 s.)
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
from fractions import Fraction
from math import sqrt

from explore_ceiling_ruler import (          # noqa: E402
    CELLS, NS, SEED, TRIALS, Z,
    PROFILE_N, PROFILE_TRIALS, PROFILE_TS,
    ThresholdSampler, BernoulliSampler,
    bayes_error, bayes_error_brute, no_evidence_error, nn_asymptote,
    product, _cell_distance_table,
)

REGIMES = ("E3r random ties", "E3g grouped ties")


# ---------------- the exact population divergence ----------------

def u_exact(N, M, t):
    """u_p = (1/M) sum_r ((c - 2 B(r))/c)^2, the exact value the
    Henze-Penrose estimator converges to on this cell."""
    c = N // M
    q, s = divmod(t, M)
    tot = Fraction(0)
    for r in range(M):
        b = q + (1 if r < s else 0)
        tot += Fraction((c - 2 * b) ** 2, c * c)
    return tot / M


def u_exact_bernoulli(etas):
    tot = 0.0
    for e in etas:
        tot += (2 * e - 1) ** 2
    return tot / len(etas)


def hp_bracket(u):
    """The Berisha-Hero bracket, both endpoints decreasing in u."""
    u = min(max(u, 0.0), 1.0)
    return 0.5 * (1 - sqrt(u)), 0.5 * (1 - u)


def hp_bracket_exact(u):
    """The upper endpoint in Fraction; the lower one carries a
    square root and is returned as a float."""
    return 0.5 * (1 - sqrt(float(u))), (1 - u) / 2


# ---------------- the Friedman-Rafsky statistic ----------------

def cell_mst_edges(occupied, dist):
    """Prim over the OCCUPIED cells, the contracted graph whose
    0-weight components are the cells themselves."""
    if len(occupied) < 2:
        return []
    root = occupied[0]
    rest = set(occupied[1:])
    best = {b: (dist[root][b], root) for b in rest}
    edges = []
    while rest:
        b = min(rest, key=lambda x: (best[x][0], x))
        _, a = best[b]
        edges.append((a, b))
        rest.discard(b)
        for x in rest:
            d = dist[b][x]
            if d < best[x][0]:
                best[x] = (d, b)
    return edges


def fr_cross_edges(cells, labels, M, dist, rng, regime):
    """R = the number of MST edges joining points of different
    labels, plus the within-cell count separately (K3 reads it).

    The MST is built the only way it can be built here: every cell's
    points are mutually at distance 0, so they span into one
    component with n_r - 1 zero-weight edges in an order the tie-
    break chooses, and the cells are then joined by a minimum
    spanning tree of the contracted graph.
    """
    by_cell = [[] for _ in range(M)]
    for r, y in zip(cells, labels):
        by_cell[r].append(y)
    within = 0
    for r in range(M):
        ys = by_cell[r]
        if len(ys) < 2:
            continue
        if regime == "E3r random ties":
            order = ys[:]
            rng.shuffle(order)
        else:
            order = sorted(ys)          # every 0 before every 1
        within += sum(1 for a, b in zip(order, order[1:]) if a != b)
    occupied = [r for r in range(M) if by_cell[r]]
    between = 0
    for a, b in cell_mst_edges(occupied, dist):
        if regime == "E3r random ties":
            la = by_cell[a][rng.randrange(len(by_cell[a]))]
            lb = by_cell[b][rng.randrange(len(by_cell[b]))]
        else:
            la = 0 if 0 in by_cell[a] else 1
            lb = 0 if 0 in by_cell[b] else 1
        between += la != lb
    return within + between, within, len(occupied)


def est_hp(cells, labels, M, rng, dist, regime):
    """Return (rhat, u, point bracket, reported interval)."""
    n = len(labels)
    n1 = sum(labels)
    n0 = n - n1
    R, _, _ = fr_cross_edges(cells, labels, M, dist, rng, regime)
    # K2: the stated Berisha-Hero route, asserted against 1 - 2R/n
    dhat = 1 - R * n / (2 * n0 * n1)
    p, q = n1 / n, n0 / n
    u = 4 * p * q * dhat + (p - q) ** 2
    assert abs(u - (1 - 2 * R / n)) < 1e-9, (u, R, n)
    rhat = R / n
    bar = Z * sqrt(max(rhat * (1 - rhat), 0.0) / n)
    lo_r = max(rhat - bar, 0.0)
    hi_r = min(rhat + bar, 1.0)
    u_lo = min(max(1 - 2 * hi_r, 0.0), 1.0)
    u_hi = min(max(1 - 2 * lo_r, 0.0), 1.0)
    plo, phi = hp_bracket(u)
    lo = 0.5 * (1 - sqrt(u_hi))
    hi = 0.5 * (1 - u_lo)
    return rhat, u, (plo, phi), (lo, hi)


def run_cell(sampler, t, n, trials, truth, seed, dist, regime):
    rng = random.Random(seed)
    tf = float(truth)
    s_r = s_lo = s_hi = s_plo = s_phi = 0.0
    s_r2 = 0.0
    cov = 0
    for _ in range(trials):
        xs = sampler.draw(rng, n)
        cells = [sampler.cell(x) for x in xs]
        labels = [sampler.label(x, t) for x in xs]
        rhat, u, (plo, phi), (lo, hi) = est_hp(
            cells, labels, sampler.M, rng, dist, regime)
        s_r += rhat
        s_r2 += rhat * rhat
        s_lo += lo
        s_hi += hi
        s_plo += plo
        s_phi += phi
        cov += lo <= tf <= hi
    m_r = s_r / trials
    sd_r = sqrt(max(s_r2 / trials - m_r * m_r, 0.0))
    return {
        "rhat": m_r, "sd": sd_r, "cov": cov / trials,
        "lo": s_lo / trials, "hi": s_hi / trials,
        "plo": s_plo / trials, "phi": s_phi / trials,
        "bar": Z * sqrt(max(m_r * (1 - m_r), 0.0) / n),
    }


# ---------------- K3: the jitter control ----------------

def jitter_same_cell_cross(sampler, t, n, rng, eps=0.01):
    """Exact Euclidean MST (Prim, O(n^2)) on the jittered embedding
    r -> (r mod p for p in S) + U(-eps, eps); return the number of
    cross-class edges among SAME-CELL edges only, which is where the
    tie-break acts."""
    xs = sampler.draw(rng, n)
    cells = [sampler.cell(x) for x in xs]
    labels = [sampler.label(x, t) for x in xs]
    pts = []
    for r in cells:
        base = sampler.coords(r)
        pts.append(tuple(v + rng.uniform(-eps, eps) for v in base))
    n = len(pts)
    inside = [False] * n
    best = [float("inf")] * n
    frm = [0] * n
    inside[0] = True
    for j in range(1, n):
        best[j] = sum((a - b) ** 2 for a, b in zip(pts[0], pts[j]))
    cross = 0
    for _ in range(n - 1):
        j = min((x for x in range(n) if not inside[x]), key=lambda x: best[x])
        inside[j] = True
        i = frm[j]
        if cells[i] == cells[j] and labels[i] != labels[j]:
            cross += 1
        for x in range(n):
            if not inside[x]:
                d = sum((a - b) ** 2 for a, b in zip(pts[j], pts[x]))
                if d < best[x]:
                    best[x] = d
                    frm[x] = j
    return cross


def random_within_cross(sampler, t, n, rng):
    xs = sampler.draw(rng, n)
    cells = [sampler.cell(x) for x in xs]
    labels = [sampler.label(x, t) for x in xs]
    dist = _cell_distance_table(sampler, sampler.M)
    _, within, _ = fr_cross_edges(cells, labels, sampler.M, dist, rng,
                                  "E3r random ties")
    return within


def main():
    # ---- K1 + K4: the closed forms, before anything is estimated ----
    n_id = 0
    for _, N, sub, t in CELLS:
        M = product(sub)
        assert bayes_error_brute(N, M, t) == bayes_error(N, M, t)
        assert (1 - u_exact(N, M, t)) / 2 == nn_asymptote(N, M, t)
        n_id += 1
    for t in PROFILE_TS:
        assert bayes_error_brute(105, 15, t) == bayes_error(105, 15, t)
        assert (1 - u_exact(105, 15, t)) / 2 == nn_asymptote(105, 15, t)
        n_id += 1
    print(f"K1/K4 identity + truth control: (1 - u_p)/2 = the 1-NN "
          f"asymptote and the fiber count = the closed form on all "
          f"{n_id} (cell, t) slices -- pass")

    # ---- K4, the sampler half: re-run here, this grid resting on it ----
    rs = random.Random(SEED + 1)
    sk = ThresholdSampler(1155, (3, 5, 7))
    xs = sk.draw(rs, 200000)
    nk, Mk = len(xs), sk.M
    counts = [0] * Mk
    for x in xs:
        counts[sk.cell(x)] += 1
    se = sqrt(nk * (1 / Mk) * (1 - 1 / Mk))
    worst = max(abs(v - nk / Mk) for v in counts)
    lab = sum(sk.label(x, 525) for x in xs) / nk
    lab_exact = float(Fraction(1155 - 525, 1155))
    lab_se = sqrt(lab_exact * (1 - lab_exact) / nk)
    print(f"   sampler half: N = 1155, M = {Mk}, n = {nk} -- worst cell "
          f"deviation {worst / se:.2f} SE, label rate {lab:.5f} vs exact "
          f"{lab_exact:.5f} ({abs(lab - lab_exact) / lab_se:.2f} SE) -- pass")
    assert worst < 4 * se, worst / se
    assert abs(lab - lab_exact) < 4 * lab_se

    # ---- K0: the positive control ----
    ctrl = BernoulliSampler((0.2, 0.9))
    ctrl_truth = Fraction(15, 100)
    ctrl_u = u_exact_bernoulli((0.2, 0.9))
    clo, chi = hp_bracket(ctrl_u)
    cdist = _cell_distance_table(ctrl, ctrl.M)
    res = run_cell(ctrl, None, 8000, TRIALS, ctrl_truth, SEED, cdist,
                   "E3r random ties")
    print(f"K0 positive control: two-cell Bernoulli, eta = (0.2, 0.9), "
          f"R* = {float(ctrl_truth):.4f}, exact u_p = {ctrl_u:.4f}, exact "
          f"bracket [{clo:.4f}, {chi:.4f}] (R* strictly inside)")
    print(f"   E3r at n = 8000: rhat {res['rhat']:.4f}  uhat "
          f"{1 - 2 * res['rhat']:+.4f}  interval [{res['lo']:.4f}, "
          f"{res['hi']:.4f}]  coverage {res['cov']:.2f}")
    assert abs((1 - 2 * res["rhat"]) - ctrl_u) < 0.02
    assert res["cov"] >= 34 / TRIALS, res["cov"]
    assert res["hi"] < 0.45, res["hi"]
    print("   u recovered, R* covered, the no-evidence value 0.45 "
          "excluded -- pass")

    # ---- K2 is asserted inside every est_hp call ----
    # ---- K3: the jitter control ----
    sam = ThresholdSampler(105, (3, 5))
    jt, jn = 0, 0
    rj = random.Random(SEED + 3)
    for _ in range(10):
        jt += jitter_same_cell_cross(sam, 45, 500, rj)
    rr = random.Random(SEED + 3)
    for _ in range(10):
        jn += random_within_cross(sam, 45, 500, rr)
    jt, jn = jt / 10, jn / 10
    se = sqrt(max(jt, 1.0)) / sqrt(10)
    print(f"K3 jitter control: FLOOR-ODD, n = 500, 10 trials -- exact "
          f"Euclidean MST on the jittered embedding gives {jt:.1f} "
          f"same-cell cross edges against E3r's {jn:.1f} "
          f"({abs(jt - jn) / se:.2f} SE)")
    assert abs(jt - jn) < 4 * se, (jt, jn)
    print("   -- pass; the random tie-break IS the jitter fix")

    # ---- the exact brackets ----
    print()
    print("THE EXACT BRACKET ON EVERY CELL (the third closed form the "
          "family hands over)")
    for name, N, sub, t in CELLS:
        M = product(sub)
        u = u_exact(N, M, t)
        truth = bayes_error(N, M, t)
        lo, hi = hp_bracket_exact(u)
        tight = "TIGHT" if abs(lo - float(truth)) < 1e-12 else "loose"
        print(f"   {name:<12} u_p = {u} = {float(u):.6f}  bracket "
              f"[{lo:.6f}, {float(hi):.6f}]  R* = {float(truth):.6f}  "
              f"lower end {tight}")

    # ---- the main grid ----
    print()
    print(f"THE GRID: exact truth vs the divergence family, both tie "
          f"regimes ({TRIALS} trials, nominal coverage 0.95)")
    for name, N, sub, t in CELLS:
        M = product(sub)
        truth = bayes_error(N, M, t)
        naive = no_evidence_error(N, t)
        asym = nn_asymptote(N, M, t)
        sam = ThresholdSampler(N, sub)
        dist = _cell_distance_table(sam, M)
        print()
        print(f"{name}: N = {N}, M = {M}, c = {N // M}, t = {t}; R* = "
              f"{float(truth):.4f}, no-evidence {float(naive):.4f}, "
              f"1-NN asymptote = HP upper end {float(asym):.4f}")
        for regime in REGIMES:
            for n in NS:
                r = run_cell(sam, t, n, TRIALS, truth, SEED + n, dist,
                             regime)
                print(f"   {regime:<17} n = {n:>5}  rhat {r['rhat']:.4f} "
                      f"(sd {r['sd']:.4f} vs bar {r['bar']:.4f})  point "
                      f"[{r['plo']:.4f}, {r['phi']:.4f}]  interval "
                      f"[{r['lo']:.4f}, {r['hi']:.4f}]  coverage "
                      f"{r['cov']:.2f}")

    # ---- the profile leg ----
    print()
    print(f"THE PROFILE: N = 105, M = 15, c = 7, t = {PROFILE_TS.start}.."
          f"{PROFILE_TS.stop - 1}, n = {PROFILE_N}, {PROFILE_TRIALS} "
          f"trials, E3r -- the exact lower end against R*, and what the "
          f"bracket certifies")
    sam = ThresholdSampler(105, (3, 5))
    dist = _cell_distance_table(sam, 15)
    print("     t   R*      naive   exLo    exHi    E3r lo  E3r hi  in-win")
    n_pt_cert = n_bar_cert = n_win = 0
    max_gap_out = 0.0
    for t in PROFILE_TS:
        truth = bayes_error(105, 15, t)
        naive = float(no_evidence_error(105, t))
        u = u_exact(105, 15, t)
        exlo, exhi = hp_bracket_exact(u)
        r = run_cell(sam, t, PROFILE_N, PROFILE_TRIALS, truth,
                     SEED + 7 * t, dist, "E3r random ties")
        q, s = divmod(t, 15)
        inwin = (q == 3 and s != 0)
        print(f"   {t:>3}  {float(truth):.4f}  {naive:.4f}  {exlo:.4f}  "
              f"{float(exhi):.4f}  {r['lo']:.4f}  {r['hi']:.4f}  "
              f"{'yes' if inwin else 'no':>6}")
        if inwin:
            n_win += 1
            if not (exlo <= naive <= float(exhi)):
                n_pt_cert += 1
            if not (r["lo"] <= naive <= r["hi"]):
                n_bar_cert += 1
        elif s != 0:
            max_gap_out = max(max_gap_out, float(truth) - exlo)
    print(f"   over the {n_win} in-window thresholds: the EXACT bracket "
          f"certifies a lift (excludes the no-evidence value) at "
          f"{n_pt_cert}; the sampled interval at n = {PROFILE_N} at "
          f"{n_bar_cert}")
    print(f"   largest exact-lower-end gap below R* outside the window "
          f"(s != 0): {max_gap_out:.4f}")

    print()
    print("all controls green")


if __name__ == "__main__":
    main()
