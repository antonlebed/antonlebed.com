"""DOES THE PRINCIPAL DEFICIT DIAGONALIZE IN THE CHARACTER BASIS? -- the
same per-class shares carried to the finite Fourier transform of the narrow
class group, over the fields where that group is CYCLIC.

THE QUESTION. Probes 1-3 left a shape with no derivation: the bottom-bin
principal share is graded by a class's ORDER, absolutely a fixed ceiling at
the generators (order = h+, spread 0.026 with no trend over ten imaginary
strata) with the shortfall deepening beneath it as h+ grows, and an odd part
of the order that does not participate. Those three are jointly a statement
about ONE class function on the group. A class function is diagonal in the
group's own character basis, so the move is a change of BASIS and not a
fourth dial. The count of split primes below x in class C is
(1/h) sum_chi conj(chi)(C) pi_chi(x), so the deviation from nominal is
dev(C) = (1/h) sum_{chi != 1} conj(chi)(C) E_chi with E_chi one character's
own bias, and the transform E_chi = sum_C chi(C) dev(C) recovers those
exactly. It is INVERTIBLE, so it derives rather than grades: nothing is
fitted, no cell is scored against a rival, and the two readings carry the
same information.

WHOSE VOCABULARY THE SUSPICION IS WRITTEN IN. Probe 1's was the FORM's (a
class has a minimum) and it graded nothing. Probes 2 and 3 spoke the GROUP's
in its ELEMENT vocabulary -- a class has an order, an inverse, a subgroup,
an index -- and it graded. This probe stays in the group and changes to its
DUAL vocabulary: not a property of a class but a coordinate of the whole
function. THE TRANSPLANT, flagged: everything probes 2 and 3 measured was
measured over ALL fields, and this rig can only run where the discrete log
exists, so the population is the CYCLIC subset. Probe 3 named that subset
itself, as the sharpest case of its own mixture problem -- its index-1 line
rests on exactly these fields -- so the ceiling this probe is chasing was
already read on this population while everything under the ceiling was not.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE BASIS, AND WHAT A GENERATOR CHOICE COSTS. On a cyclic Cl+ of
      order h a generator g gives every class an exponent a with C = g^a,
      and the characters are chi_j(g^a) = e(ja/h), j = 0..h-1. A DIFFERENT
      generator g' = g^u with u coprime to h relabels j -> j u^{-1}, so an
      individual chi_j is NOT an invariant of the field and no statistic
      may be pooled across fields at fixed j. What IS invariant is the
      ORDER of the character, h/gcd(j,h), which the relabelling preserves,
      and there are exactly phi(d) characters of order d for each d | h.
      So the only pooling this rig is allowed is BY CHARACTER ORDER, and
      that is also exactly the third of the three readings the basis was
      brought in to separate.

  (2) THE TRANSFORM'S OWN IDENTITIES, WHICH ARE THE CONTROLS. E_0 =
      sum_C dev(C) = 0 exactly, by the constant sum probe 3 measured (the
      r(C) sum to h at every field, so the dev sum to 0). Inversion
      dev(a) = (1/h) sum_j conj(chi_j)(a) E_j returns the measured
      deviations. Parseval sum_j |E_j|^2 = h sum_a dev(a)^2 fixes the TOTAL
      energy at the observed variance of dev, which is the reason the
      reading below is a SHARE and never a size: the transform cannot
      create or destroy energy, it can only say where it sits.

  (3) THE MEASURED FUNCTION IS EVEN AND THE BASIS IS NOT, AND THIS IS
      SETTLED HERE RATHER THAN AFTER THE RUN. A split prime p has TWO
      places above it carrying INVERSE classes; the sweep assigns p to one
      of them through form_at, which takes the square root sqrt_mod_p(D, p)
      returns -- one of two, by a convention in the code and by nothing
      arithmetic. Every dial probes 2 and 3 read was blind to this, an
      order, an ambiguity, an index and a least represented prime all being
      shared by a class and its inverse. A CHARACTER IS NOT: chi(C^-1) =
      conj(chi)(C), so a complex character separates precisely what the
      measurement cannot. The object that is well defined is therefore the
      SYMMETRIZED deviation dev_s(C) = (dev(C) + dev(C^-1))/2, and the
      primary reading is of that. It has a sharp printed consequence --
      dev_s even makes E_j = sum_a dev_s(a) cos(2 pi j a / h), REAL at
      every j -- which is control C4. And the ANTISYMMETRIC part of the raw
      dev is then a free instrument rather than a nuisance: it is energy
      the convention put there, so its share of the total is the scale at
      which any raw-basis reading would have been convention and not
      arithmetic. The quadratic characters are real and self-conjugate and
      survive symmetrization untouched, which is why the genus reading is
      the one prediction the ambiguity cannot touch -- and that is a reason
      to DISTRUST a clean answer there, not to trust it.

  (4) A DELTA IS FLAT, SO FLAT IS THE LEAST INFORMATIVE ANSWER AND NOT A
      CLEAN REFUTATION. If dev is a spike at a single class plus the
      constant that zeroes its sum, dev = v(delta_C0 - 1/h) up to scale,
      then E_j = v chi_j(C0) and |E_j| is CONSTANT over every j != 0.
      Probes 2 and 3 leave a large single-cell effect on the table at
      D < 0 -- the trivial class's derived hard zero, no split prime below
      |D|/4 being principal, which runs its ratio down to 0.334 at
      h+ = 20 where the other orders sit near 1 -- so a flat energy
      spectrum is what the ALREADY EXPLAINED part of the table predicts,
      and reading flatness as "no structure" would be reading a derived
      mechanism as noise. Both readings are printed: with the trivial
      class's deviation in place, and with it removed and the remaining
      classes re-centred so that E_0 stays 0.

  (5) AND AN ORDER-GRADED FUNCTION IS A COMBINATION OF SUBGROUP INDICATORS,
      WHICH IS WHY THE GENUS PREDICTION IS NOT SEPARABLE FROM THE LADDER
      UNTIL THE LADDER IS PROJECTED OUT. In a cyclic group the classes of
      order dividing d are the unique subgroup H_d, and
      sum_{a in H_d} e(ja/h) = d if d | j and 0 otherwise -- so the
      indicator of H_d transforms onto the characters of order dividing
      h/d and onto no others. A function of ord(C) alone is a combination
      of those indicators, so the order ladder probes 2 and 3 measured
      ALREADY predicts a specific non-flat energy spectrum, and in
      particular the 2-torsion term (d = 2) puts energy only at even j,
      which is to say only at characters of order dividing h/2 -- never at
      a character of maximal order h. A quadratic-character excess read
      against FLAT would therefore be the ladder returning in a new
      coat. The reference this rig reads against is thus not flat: it is
      the transform of the FITTED ORDER PROFILE, dev_fit(a) = the stratum's
      own mean r at ord(a), re-centred to sum to zero. That vector is the
      SAME at every field of a stratum, a cyclic group of order h having
      exactly phi(d) elements of order d for every d | h, so its spectrum
      is one derived curve per stratum and costs nothing. The finding is
      the RESIDUAL dev_s - dev_fit and where its energy sits.

  (6) THE NOISE IS FLAT, DERIVED AND NOT ASSUMED. Per field the counts
      n0(C) are a multinomial over tot0 split primes, so under the nominal
      1/h the deviations have variance (h-1)/tot0 and are EXCHANGEABLE
      across classes; an exchangeable perturbation has the same expected
      energy at every j != 0. So counting noise dilutes any shape TOWARD
      flat and can never manufacture one -- which is what makes a SHARE
      against a derived reference readable at all, and it is also why the
      placebo below is a confirmation of a derived null rather than the
      whole scale. The dilution is real and one-directional: a share
      excess measured here is a floor on the excess in the arithmetic.

  (7) THE POPULATION IS PROBE 2'S SWEEP, CUT TO THE CYCLIC FIELDS. Same
      discriminant bound, same prime cap, same bottom bin, same MIN_SPLIT,
      same composition, so probe 2's composition controls re-print
      unchanged. A field is kept when some class has order h+ -- which for
      a finite abelian group is cyclicity -- and the discrete log is then
      built by the same walk that measured the orders. Strata are h+, and
      a stratum with h+ PRIME carries no shape at all, every non-trivial
      character having order h+, so only composite strata can be read.
      WIDENING TRIGGER, declared before the run: if fewer than three
      composite strata across both signs carry MINSTRAT cyclic fields, the
      sweep re-runs at |D| <= 8000 under memwatch and both populations are
      reported.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE, AT BOTH SIGNS.

  P1. THE CONVENTION IS LOAD-BEARING IN THE RAW BASIS. The antisymmetric
      part of the raw dev carries at least 0.30 of the total energy at
      every readable stratum. The reason: the two places above p are
      assigned by a square-root convention that is arithmetically
      meaningless, so at the noise level the raw dev splits its energy
      roughly evenly between the even and odd parts, and only the even part
      can carry arithmetic. If this holds, no raw-basis reading is
      admissible and the symmetrized one is the object.

  P2. AND THE RESIDUAL IS FLAT AT THE QUADRATIC CHARACTERS. After the
      fitted order profile of derivation (5) is removed, the energy share
      at character order 2 does not exceed its flat allowance
      phi(2)/(h-1) = 1/(h-1) by more than the placebo band, at any
      readable stratum of either sign. The reason: the genus reading was
      already answered at the subgroup level -- the ambiguous classes form
      a SUBGROUP whose order equals that of the principal genus QUOTIENT
      through which the genus congruences were cleared, same order,
      different subobject, opposite verdicts -- so a genus mechanism
      surviving in the dual would have to be new and there is nothing on
      the table predicting it.

  P3. AND THE MAXIMAL-ORDER CHARACTERS ARE STARVED. The energy share at
      character order h+ falls BELOW its flat allowance phi(h)/(h-1) at
      every readable stratum, on the full symmetrized dev, before any
      residual is taken. The reason is derivation (5) run forward: the
      2-torsion component of an order-graded function contributes nothing
      at a character of maximal order, and the table's largest structured
      term below the trivial class is exactly the order-2 line.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, weighed for meaning only
after the controls are read.

  K1 kills P1: the printed per-stratum antisymmetric energy share of the
     raw dev. Any readable stratum below 0.30 is the kill, and a share
     near ZERO would say the convention is not free -- that the square root
     chosen tracks something arithmetic -- which is a finding about the
     sweep and not about the group.

  K2 kills P2: the printed per-stratum energy share at character order 2 of
     the RESIDUAL, against the flat allowance and against the placebo band.
     A share exceeding both at any readable stratum kills P2, and it is
     the informative outcome: a genus mechanism the element-vocabulary
     probes could not see.

  K3 kills P3: the printed per-stratum energy share at character order h+
     of the symmetrized dev, against phi(h)/(h-1). At or above the
     allowance at any readable stratum is the kill.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. INVERSION. The inverse transform must return the measured deviations:
      max over every kept field and class of |dev(a) - (1/h) sum_j
      conj(chi_j)(a) E_j|, printed. Anything above 1e-9 voids the rig --
      a transform that does not invert is arithmetic, not a finding.

  C2. THE TRIVIAL CHARACTER IS EXACTLY ZERO. max |E_0| over every kept
      field, which is probe 3's constant sum seen in the dual. Above 1e-9
      voids every share below, the shares being taken over j != 0.

  C3. PARSEVAL. max relative deviation of sum_j |E_j|^2 from h sum_a
      dev(a)^2, printed. This is what licenses reading a SHARE.

  C4. THE SYMMETRIZED TRANSFORM IS REAL. max |Im E_j| over every kept field
      and every j on the symmetrized dev, printed. Derivation (3) says it
      must vanish; a non-zero value means the inverse pairing is wrong.

  C5. THE DISCRETE LOG IS A BIJECTION. Per kept field the walk must visit
      every class exactly once and assign exponent 0 to the trivial class:
      violation count printed, and must be zero.

  C6. PROBE 2'S COMPOSITION CONTROLS, RE-PRINTED through the imported
      sweep as violation counts -- discriminant and integrality, key in
      inventory, walk overrun, order divides h+, two-sided identity,
      commutativity, associativity, and the order-at-most-2 count against
      the independent form-symmetry ambiguity test.

  C7. THE EXCHANGEABILITY PLACEBO. Derivation (6) derives a flat null;
      this measures it on the actual counts. The deviations are ROTATED
      across the non-trivial classes within each field over five fixed
      offsets read off |D|, none of them the identity, and the result is
      re-symmetrized exactly as the treatment is -- which holds the
      constant sum (a rotation is a permutation and symmetrizing preserves
      sums), holds the trivial class fixed since it carries a derived
      mechanism and is exchangeable with nothing, and moves only WHICH
      class carries which deviation, that being the whole content of a
      spectrum. The permutation runs over CLASSES rather than over inverse
      PAIRS on purpose: a pair carries two classes and a self-inverse
      class one, so rotating pairs would move a two-class value onto a
      one-class slot and break the constant sum, leaving a null that
      differs from the treatment in two variables. The same share
      statistics are read off the result and printed beside the observed
      ones. The count of DISTINCT draws per field is printed beside the
      band: a field of narrow class number h admits h - 2 non-identity
      rotations, so five offsets give fewer than five distinct tables at
      the small strata and exactly ONE at h+ = 4, where the band collapses
      to a point and is not a band.

  C8 (added at audit, and K2 is not readable without it). THE PER-FIELD
      AMPLITUDE. RES subtracts the STRATUM'S order profile from every
      field, so if the ladder runs at a field-varying SIZE the residual
      keeps a term proportional to the profile itself and therefore the
      profile's own quadratic-heavy spectrum -- which would fire K2
      without a second mechanism existing. RES-a subtracts alpha * profile
      with alpha the per-field least-squares amplitude
      <dev_s, fit>/<fit, fit>, so what survives is orthogonal to the
      ladder at every field rather than to its stratum mean. The control
      is CONSERVATIVE by construction: alpha is fitted on the same data
      and absorbs some of the field's own noise along the fit direction,
      which is the quadratic-heavy direction, so it can only understate
      what remains there.

THE FINDINGS.

  THE CONTROLS. C6 prints zero at all eight composition counts over 1216
  real and 1217 imaginary fields -- the imported sweep is the object probes
  2 and 3 measured. C5 prints zero discrete-log violations: every kept
  field's walk visits every class exactly once, seats the trivial class at
  exponent 0, and assigns each class the exponent its independently
  measured ORDER demands. The transform's own four identities hold at float
  noise and nothing above it: inversion 2.0e-15 real and 3.1e-14 imaginary,
  |E_0| 6.7e-16 and 9.3e-15, Parseval 1.5e-15 and 4.0e-15 relative, and the
  symmetrized transform's largest imaginary part 8.0e-15 and 2.6e-13. So
  the transform inverts, the trivial character is the constant sum seen in
  the dual, the total energy is the observed variance and a SHARE is what
  there is to read, and derivation (3)'s evenness consequence is exact.

  **THE SQUARE ROOT IS LOAD-BEARING IN THE RAW BASIS, AND IT CARRIES MORE
  THAN AN EXCHANGEABLE SHARE** (observation; P1 SURVIVES, K1 misses at
  every stratum). The antisymmetric part of the raw dev -- which is the
  choice of square root in form_at and nothing else -- carries 0.340 and
  0.517 of the total energy at h+ = 4 and 6 real, and 0.312, 0.533, 0.505,
  0.509, 0.573, 0.614 at h+ = 4 through 14 imaginary. Every reading is at
  or above the frozen 0.30, so no unsymmetrized reading in this basis is
  admissible and the symmetrized dev is the object, exactly as derivation
  (3) settled on paper. THIS DOES NOT RE-PRICE PROBES 2 AND 3: every dial
  they read -- order, ambiguity, index, least represented prime -- is shared
  by a class and its inverse, so their statistics cannot see the
  antisymmetric part at all, and this is the first probe whose basis can.
  Against the exchangeable allowance the audit control supplies, the share
  is ABOVE it at seven of the eight strata and by 0.065 to 0.152 wherever
  h+ >= 6, the one exception being imaginary h+ = 4 (0.312 against 0.333),
  which is the one stratum with a single antisymmetric degree of freedom
  and the largest structured even part to be measured against. A mechanism
  is available and is an argument rather than a measurement: the two places
  above p draw from ONE prime and the convention hands it to exactly one of
  them, which correlates a pair's counts negatively far harder than the
  generic multinomial does, and that surplus negative correlation IS
  antisymmetric energy.

  **AND THE OBSERVED SPECTRUM IS THE ORDER LADDER DILUTED BY FLAT NOISE TO
  FIRST ORDER, AT EVERY STRATUM OF BOTH SIGNS** (observation; the reading
  the change of basis was made for, and first order is load-bearing --
  what the profile does NOT account for is the block below). The deficit's
  energy is CONCENTRATED at the quadratic characters and STARVED at the
  maximal-order ones. The quadratic
  share runs 0.7217 and 0.2953 at h+ = 4 and 6 real and 0.7992, 0.4585,
  0.3555, 0.2306, 0.2318, 0.1984 at h+ = 4 through 14 imaginary, against a
  flat allowance of 0.3333, 0.2000, 0.3333, 0.2000, 0.1429, 0.1111, 0.0909,
  0.0769 -- between 1.48 and 2.58 times nominal, and above the WHOLE
  placebo band at all eight strata. (SETTLED LATER by explore_class_null.py:
  the flat allowance is the wrong reference for a SYMMETRIZED spectrum.
  Symmetrizing sends E to Re E, so the real characters -- exactly those of
  order dividing 2 -- keep their energy whole while complex ones lose the
  imaginary part, and the allowance is 2*n2/(h-1+n2), here 1.50 to 1.83
  times flat. Most of the 1.48-to-2.58 multiple is that geometry. What
  survives unchanged is everything compared against the PLACEBO, both arms
  being symmetrized alike -- which is the "above the whole band at all
  eight" beside it, and the starvation below.) But it is BELOW what the order ladder
  alone predicts at all eight: the transform of the stratum's own fitted
  order profile puts 0.9409, 0.3431, 0.9124, 0.5325, 0.4395, 0.2691,
  0.3492, 0.2665 there. The observed share sits strictly BETWEEN the flat
  allowance and the fitted one at every stratum, at the quadratic
  characters and again at the maximal-order ones (0.2783 and 0.3102 real,
  0.2008, 0.1884, 0.4426, 0.3402, 0.2862, 0.3040 imaginary, each between a
  fit of 0.0591 to 0.3114 and a flat allowance of 0.3636 to 0.6667) --
  sixteen cells of sixteen. That is precisely the shape derivation (6)
  derived before the run: a profile applied without noise plus counting
  noise that is exchangeable and therefore flat, the noise diluting the
  concentration toward flat and never manufacturing it. The eight
  intermediate cells sit at or below BOTH references at six of them and
  between the two at the other two (chi of order 4 at h+ = 12 and chi of
  order 7 at h+ = 14); against the placebo band they are inside at five,
  below at two (chi of order 4 at h+ = 8 and chi of order 3 at h+ = 12)
  and above at one, chi of order 7 at h+ = 14 reading 0.4976 against a
  band reaching 0.4952 with the fit higher still at 0.5415. So the odd
  part of the CHARACTER order carries nothing the profile does not. AND
  THE CONCENTRATION IS NOT THE TRIVIAL CLASS'S DELTA, which derivation (4)
  named as the thing that would fake a reading here: removing that
  deviation and re-centring moves the quadratic share by at most 0.045 at
  any stratum and raises it at five of the eight, where a delta contributes
  FLAT and its removal would have to lower a concentration it was causing.

  **AND THE MAXIMAL-ORDER CHARACTERS ARE STARVED, WHICH IS THE LADDER
  TRANSPORTING AND NOT A NEW FACT** (observation; P3 SURVIVES, K3 fires
  nowhere). The energy share at character order h+ is below its flat
  allowance at all eight strata and below the WHOLE placebo band at all
  eight as well. Derivation (5) derived this from the ladder before the
  run -- the 2-torsion term of an order-graded function transforms onto
  even j alone and a character of maximal order has j coprime to h+ -- so
  it is a check that the ladder transports into the dual, and it must NOT
  be welded to probe 3's fixed ceiling at the generators: that is a
  statement about the CLASS of order h+, this one is about the CHARACTER
  of order h+, and the two are the same object only through derivation (5).

  **BUT THE QUADRATIC CHARACTERS CARRY MORE THAN THE LADDER GIVES THEM,
  AND A PER-FIELD AMPLITUDE ABSORBS MOST OF IT AND NOT ALL** (observation;
  P2 DIES, K2 fires at five strata and at three under the control that is
  built to understate it). After the stratum's fitted order profile is
  removed, the residual's quadratic share is 0.3309 and 0.3400 real and
  0.4485, 0.2413, 0.1652, 0.1427, 0.0934, 0.1082 imaginary. K2 asked for a
  share above BOTH the flat allowance and the placebo band and gets one at
  five of the eight strata -- real h+ = 6 and imaginary h+ = 4, 6, 10 and
  14 -- so the prediction that the residual would be flat there is
  refuted as frozen. THE FIRST THING TO ASK IS WHETHER IT IS A SECOND
  MECHANISM AT ALL, and C8 is that question: RES removes the STRATUM's
  profile, so a ladder running at a field-varying SIZE leaves a term
  proportional to the profile and therefore the profile's own
  quadratic-heavy spectrum. Removing a PER-FIELD amplitude instead drops
  the quadratic share to 0.0591 and 0.2887 real and 0.0876, 0.2654,
  0.1799, 0.1305, 0.0690, 0.1056 imaginary: the two h+ = 4 strata, where
  the profile is nearly the whole signal (fit 0.9409 and 0.9124), fall
  from above both references to far BELOW both, and the kill survives at
  three strata only -- real h+ = 6 (0.2887 against a flat 0.2000 and a band
  to 0.2358), imaginary h+ = 6 (0.2654 against 0.2000 and 0.2258) and
  imaginary h+ = 10 (0.1305 against 0.1111 and 0.1261). So most of the
  residual excess is the ladder's amplitude varying field to field, which
  is not a mechanism, and what is left is small, marginal, and at three
  strata of eight. Two things keep it from being dismissed and one keeps
  it from being believed. C8 is CONSERVATIVE -- alpha is fitted on the same
  field and absorbs noise along the quadratic-heavy fit direction -- so
  what survives it is understated; and the three survivors are not the
  strata with the largest quadratic signal, which an artifact of the fit
  would have preferred. Against that, the placebo band at h+ = 6 rests on
  about two distinct draws per field (1.95 and 1.98 printed) where h+ = 10
  has 3.59, so two of the three survivors are read against the thinnest
  bands in the table. AND ON A CYCLIC GROUP
  THE QUADRATIC CHARACTER IS THE GENUS CHARACTER, which is what makes this
  worth the care: the genus characters are the characters trivial on
  Cl+^2, and for cyclic Cl+ of even order that quotient is Z/2, so there
  is exactly ONE non-trivial genus character per stratum and it is
  chi_{h/2}. The surviving component therefore sits ON the genus character
  and not merely near it -- but the same coincidence is why this
  population cannot say whether it is GENUS or merely the order-2
  character as a size class, the two being the same object here. The
  separation lives in the non-cyclic groups, where the genus characters
  are 2^(t-1) - 1 of the dual's 2-torsion and the quadratic characters are
  strictly more. (SETTLED, explore_class_dual.py: that last sentence is
  FALSE. A genus character is one trivial on Cl+^2, i.e. chi^2 = 1, i.e.
  order dividing 2 -- genus and quadratic are the same set at every field
  and no population separates them, the two counts agreeing because
  |G[2]| = |G/G^2|. What survives here is the coincidence's other half:
  a cyclic group carries ONE quadratic character where a general one
  carries 2^(t-1) - 1, so this population confounds the whole 2-torsion of
  the dual with a single coordinate. The split that IS real is whether the
  ladder's 2-torsion TERM reaches a given quadratic character, and it does
  not grade the residual.) The subgroup-level verdict -- the ambiguous classes are a
  SUBGROUP where the genus congruences were cleared through a QUOTIENT,
  same order, different subobject -- is not overturned, since that verdict
  is about a subobject of the GROUP and this is a coordinate of the dual;
  what it loses is its claim to be the last word.

  AND WHERE THE EXCESS SURVIVES IS NOT SCATTERED. The three survivors are
  h+ = 6 real and h+ = 6 and 10 imaginary, every one of them h+ = 2 mod 4,
  and the fourth stratum of that shape (h+ = 14) misses its band by 0.002
  while all four strata with 4 | h+ fail outright. A derived fact stands
  beside that and may or may not be the reason: the quadratic character is
  chi_{h/2}, whose index is EVEN exactly when 4 | h, and the order-2
  subgroup indicator transforms onto even indices alone -- so at
  h+ = 2 mod 4 the ladder's 2-torsion term cannot reach the quadratic
  character at all, and whatever profile energy lands there comes from the
  identity delta and the odd-order subgroups instead. That is a WHERE with
  a mechanism-shaped fact next to it, not a mechanism, and it is the
  sharpest thing this probe hands the next one.

  WHAT THIS LEAVES THE FRONT. The basis was brought in because three
  observed shapes were jointly a statement about one class function, and
  the transform is invertible so its verdict is a derivation rather than a
  ranking. The verdict is that the observed function is the order ladder
  to first order and that a quadratic-character component survives the
  ladder at three strata after the amplitude control. So the dual is NOT
  spent, and the next question is sharper than the one this probe asked:
  is that component the genus characters specifically -- which is
  answerable, the genus characters being an identified subgroup of the
  dual rather than a size class -- and does it survive a leave-one-out
  amplitude and a wider population. (SETTLED, explore_class_dual.py: the
  first of those is not a question, per the note above; the wider
  population and the leave-one-out amplitude both ran, and the amplitude
  fitted with the tested coordinate held out leaves 1.353 to 3.184 times
  the order-2 energy the same-data alpha below leaves, so C8 understates
  the surviving component by a factor.) The three candidate readings frozen in
  advance resolve as: not flat; graded by the order of chi exactly insofar
  as the class-order ladder forces it; and quadratic beyond that, at the
  edge of what this population can carry.

RUN RECORD: wall 4.9 s, peak working set 124.7 MB and peak commit 120.6 MB
under memwatch at a 512 MB ceiling. Probe 2's population unchanged per
derivation (7) -- 1216 real and 1217 imaginary fundamental discriminants to
|D| <= 4000 over the odd split p <= 10^4 -- cut to the 166 real and 820
imaginary fields whose narrow class group is cyclic with h+ >= 3. Eight
composite strata carry 30 fields or more (h+ = 4, 6 real; 4, 6, 8, 10, 12,
14 imaginary), so the widening trigger of derivation (7) did NOT fire.
Pure Python; the cost is probe 2's sweep run once per sign, the class
inventory rebuilt once per cyclic field to recover the group law the sweep
discards, and h^2 arithmetic per transform.

WHAT IS NOT CONTROLLED, stated rather than left for a reader to find. THE
POPULATION IS THE CYCLIC ONE and that is not a detail: probe 3 named these
fields as the sharpest case of its own mixture problem, its index-1 line
resting on exactly them, so the ceiling this probe transported was already
read here while everything BELOW the ceiling was read over cyclic and
non-cyclic fields together. A non-cyclic group has a character group of the
same order and the transform exists there too; what it needs is a structure
decomposition rather than one discrete log, and until that runs the verdict
above is a verdict about cyclic Cl+ alone. The FIT is fitted on the same
fields it is then subtracted from and C8's amplitude on the same field it
is then subtracted from, with no leave-one-out at either level, so both
residuals are biased LOW along the profile's own direction -- which is the
conservative direction for the surviving quadratic component and does
nothing to P3, read before any residual is taken. A leave-one-out
amplitude is the cheap next control and was not run. The strata are h+
and nothing finer, so a stratum still mixes fields whose group is cyclic of
the same order but whose arithmetic is not otherwise matched. The placebo
rotates values across CLASSES and re-symmetrizes, which holds the constant
sum and the trivial class exactly and destroys only which class carries
which deviation -- but the band it gives is a null for "the spectrum is
unstructured" and never for "the spectrum is the fit", and it THINS toward
the small strata: h - 2 rotations exist and two of them coincide after
re-symmetrization at h+ = 4, where the printed band is one point. No error
bar is computed on any cell mean, and two shares close together are not
thereby distinguished. And the mechanism offered for the antisymmetric
surplus above its allowance is an argument from how the convention
allocates a shared prime, not a measurement: a rig that resampled the
square root would settle it and none was run.
"""

import os
import sys
import time
from cmath import exp as cexp, pi
from collections import defaultdict
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_class_order as P2                      # noqa: E402
from explore_principal_share import (                 # noqa: E402
    primes_upto, class_data_real, class_number_imag,
)
from explore_class_share import (                     # noqa: E402
    classes_imag, classes_real, mean,
)

MINSTRAT = 30                 # cyclic fields a stratum needs to be read
PLACEBO_SHIFTS = (1, 2, 3, 4, 5)


def totient(n):
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)


def dlog_of(D, sign, orders, hplus):
    """Exponent of every class under some generator, or None if not cyclic.

    The walk is class_orders' walk kept rather than discarded: composing a
    generator with itself enumerates the group in exponent order, so the
    position in that sequence IS the discrete log. Which generator is found
    is arbitrary and derivation (1) says no statistic may depend on it.
    """
    gen = next((k for k, o in orders.items() if o == hplus), None)
    if gen is None:
        return "acyclic"
    if sign < 0:
        recs, triv = classes_imag(D)
        member = rt = None
    else:
        recs, member, triv, rt = classes_real(D)
    comp = P2.make_composer(D, sign, recs, member, rt, [0, 0, 0, 0])
    dlog, cur = {triv: 0}, gen
    for j in range(1, hplus):
        if cur is None or cur in dlog:
            return "walk"
        dlog[cur] = j
        cur = comp(cur, gen)
    if cur != triv or len(dlog) != hplus:
        return "walk"
    return dlog


def transform(dev):
    """E_j = sum_a dev[a] e(2 pi i j a / h)."""
    h = len(dev)
    return [sum(dev[a] * cexp(2j * pi * j * a / h) for a in range(h))
            for j in range(h)]


def invert(E):
    """dev[a] = (1/h) sum_j conj(chi_j)(a) E_j -- control C1."""
    h = len(E)
    return [(sum(E[j] * cexp(-2j * pi * j * a / h)
                 for j in range(h)) / h).real for a in range(h)]


def energy_by_order(E):
    """Energy at each character order, over j != 0."""
    h = len(E)
    acc = defaultdict(float)
    for j in range(1, h):
        acc[h // gcd(j, h)] += abs(E[j]) ** 2
    return acc


def shares(acc):
    tot = sum(acc.values())
    return {d: v / tot for d, v in acc.items()} if tot > 0 else {}


def symmetrize(dev):
    h = len(dev)
    return [(dev[a] + dev[(h - a) % h]) / 2 for a in range(h)]


def antisym_share(dev):
    """Energy fraction of the raw dev the square-root convention carries."""
    h = len(dev)
    tot = sum(x * x for x in dev)
    if tot <= 0:
        return None
    anti = sum(((dev[a] - dev[(h - a) % h]) / 2) ** 2 for a in range(h))
    return anti / tot


def antisym_allowance(h):
    """Share of the energy an exchangeable perturbation puts in the odd part.

    One degree of freedom per genuine inverse pair and NONE at a
    self-inverse class, over the h - 1 non-trivial classes. A self-inverse
    class is its own inverse, so the convention K1 measures never touches
    it and it contributes to the even part alone.
    """
    n = sum(1 for a in range(1, h) if a != (h - a) % h)
    return (n / 2) / (h - 1)


def placebo(dev, D, shift):
    """C7: rotate the values across the non-trivial classes, then re-even.

    The null is that a field's non-trivial classes are EXCHANGEABLE, which
    is the null derivation (6) derives flatness from, so the permutation
    runs over the classes and not over the inverse pairs. Rotating pairs
    instead would move a two-class value onto a one-class self-inverse
    slot and back, which changes the SUM -- and the constant sum is the
    one thing the treatment obeys exactly, so a null that breaks it
    differs from the treatment in two variables rather than one. A
    rotation is a permutation and symmetrizing preserves sums, so this
    holds the sum and the trivial class fixed and moves only WHICH class
    carries which deviation. The offset never lands on the identity.
    """
    h = len(dev)
    n = h - 1
    start = 1 + (abs(D) + shift) % (n - 1) if n > 1 else 0
    out = [dev[0]] + [dev[1 + (i + start) % n] for i in range(n)]
    return symmetrize(out)


def centred(vec):
    m = sum(vec) / len(vec)
    return [x - m for x in vec]


def collect(sign, plist, bad_box):
    """Per cyclic field: (D, h, dev by exponent), plus the dlog violations."""
    rows, bad, idb, c2b, c4b, lawb = P2.sweep(sign, plist)
    bad_box.append((bad, idb, c2b, c4b, lawb, len(rows)))
    out, viol = [], [0, 0]
    for D, h, recs, orders, n0, tot0, q, _ in rows:
        if h < 3 or tot0 == 0:
            continue
        dlog = dlog_of(D, sign, orders, h)
        if dlog == "acyclic":
            continue
        if dlog == "walk":            # a generator exists and the walk on
            viol[1] += 1              # it failed: never a silent drop
            continue
        if sorted(dlog.values()) != list(range(h)):
            viol[0] += 1
            continue
        if any(orders[k] != h // gcd(a, h) for k, a in dlog.items()):
            viol[0] += 1
            continue
        dev = [0.0] * h
        for k, a in dlog.items():
            dev[a] = P2.ratio(n0.get(k, 0), tot0, h) - 1.0
        out.append((D, h, dev))
    return out, viol


def fit_profile(fields):
    """Derivation (5): the stratum's own mean r at each class order."""
    acc = defaultdict(list)
    for D, h, dev in fields:
        for a in range(h):
            acc[h // gcd(a, h)].append(dev[a])
    prof = {d: mean(v) for d, v in acc.items()}
    h = fields[0][1]
    return centred([prof[h // gcd(a, h)] for a in range(h)])


def main():
    t0 = time.time()
    plist = primes_upto(P2.PCAP)
    print("population: |D| <= %d both signs, odd split p <= %d, bottom bin"
          " p < %d, min split %d; CYCLIC Cl+ with h+ >= 3, strata need %d"
          " fields" % (P2.DBOUND, P2.PCAP, P2.BIN0, P2.MIN_SPLIT, MINSTRAT))

    pops, viols, boxes = {}, {}, {}
    for sign, name in ((+1, "real"), (-1, "imag")):
        box = []
        fields, viol = collect(sign, plist, box)
        pops[sign], viols[sign], boxes[sign] = fields, viol, box[0]
        bad, idb, c2b, c4b, lawb, nrows = box[0]
        print("\n%s: %d fields kept by the sweep, %d of them cyclic with"
              " h+ >= 3" % (name, nrows, len(fields)))
        print("  C6 composition: disc/integrality %d | key not in inventory"
              " %d | walk overran %d | order does not divide h+ %d |"
              " identity %d | non-commuting %d | non-associative %d |"
              " order<=2 vs form-symmetry disagreements %d"
              % (bad[0], bad[1], bad[2], bad[3], idb, lawb[0], lawb[1], c2b))
        print("  C5 discrete log a bijection onto Z/h+ with the trivial"
              " class at 0, and every exponent agreeing with the"
              " independently measured order: %d violations, plus %d"
              " fields where a generator exists and its walk failed"
              % (viols[sign][0], viols[sign][1]))

    # ---- C1, C2, C3, C4: the transform's own identities.
    print("\n--- C1/C2/C3/C4: THE TRANSFORM'S IDENTITIES. Inversion returns"
          "\n    the measured deviations; the trivial character is exactly"
          "\n    zero by the constant sum; Parseval fixes the total energy,"
          "\n    which is what licenses reading a SHARE; and the"
          "\n    symmetrized transform is real by derivation (3).")
    for sign, name in ((+1, "real"), (-1, "imag")):
        w1 = w2 = w3 = w4 = 0.0
        for D, h, dev in pops[sign]:
            E = transform(dev)
            w1 = max(w1, max(abs(x - y) for x, y in zip(dev, invert(E))))
            w2 = max(w2, abs(E[0]))
            par = sum(abs(x) ** 2 for x in E)
            ref = h * sum(x * x for x in dev)
            w3 = max(w3, abs(par - ref) / ref if ref > 0 else 0.0)
            Es = transform(symmetrize(dev))
            w4 = max(w4, max(abs(x.imag) for x in Es))
        print("  %-5s inversion %.2e | |E_0| %.2e | Parseval rel %.2e |"
              " max |Im E| symmetrized %.2e" % (name, w1, w2, w3, w4))

    # ---- Reading A / K1: what the square-root convention carries.
    print("\n--- READING A / K1: THE CONVENTION'S OWN ENERGY. The sweep"
          "\n    assigns a split prime to ONE of the two inverse classes"
          "\n    above it by the square root sqrt_mod_p returns. The"
          "\n    antisymmetric part of the raw dev is that choice and"
          "\n    nothing else; its share of the total energy is the scale"
          "\n    at which a raw-basis reading would have been convention."
          "\n    ALLOW (added at audit, K1 not readable without it): the"
          "\n    share an exchangeable perturbation would put there, which"
          "\n    is the count of genuine inverse PAIRS over h+ - 1, the"
          "\n    antisymmetric part having one degree of freedom per pair"
          "\n    and none at a self-inverse class. K1's 0.30 was frozen"
          "\n    with no such scale behind it and this supplies it.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        by_h = defaultdict(list)
        for D, h, dev in pops[sign]:
            s = antisym_share(dev)
            if s is not None:
                by_h[h].append(s)
        line = ["h+ %d: %.3f vs allow %.3f (%d)"
                % (h, mean(v), antisym_allowance(h), len(v))
                for h, v in sorted(by_h.items()) if len(v) >= MINSTRAT]
        print("  %-5s %s" % (name, "  ".join(line) or "no readable stratum"))

    # ---- Readings B and C: the spectrum by character order.
    print("\n--- READINGS B AND C / K2, K3: THE ENERGY SHARE BY CHARACTER"
          "\n    ORDER, on the SYMMETRIZED dev (derivation 3). Only the"
          "\n    character ORDER is invariant under the choice of"
          "\n    generator (derivation 1), so it is the only pooling"
          "\n    available. FLAT is phi(d)/(h+-1). FIT is the transform of"
          "\n    the stratum's own order profile (derivation 5) -- the"
          "\n    reference the ladder already predicts, and the reason a"
          "\n    quadratic excess read against FLAT would be the ladder in"
          "\n    a new coat. RES is the residual after that profile is"
          "\n    removed. PLA is the placebo band over five inverse-pair"
          "\n    permutations (C7). NO-TRIV repeats the observed share with"
          "\n    the trivial class's deviation removed and the rest"
          "\n    re-centred, per derivation (4): a delta is flat, so the"
          "\n    already-explained hard zero at D < 0 predicts flatness by"
          "\n    itself.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        by_h = defaultdict(list)
        for rec in pops[sign]:
            by_h[rec[1]].append(rec)
        print("  %s:" % name)
        any_read = False
        for h in sorted(by_h):
            fields = by_h[h]
            if len(fields) < MINSTRAT:
                continue
            divs = sorted(d for d in range(2, h + 1) if h % d == 0)
            if len(divs) < 2:
                print("    h+ %2d (%4d fields): PRIME -- every non-trivial"
                      " character has order %d, no shape to read"
                      % (h, len(fields), h))
                continue
            any_read = True
            fit = fit_profile(fields)
            obs, res, notriv, resa = (defaultdict(list) for _ in range(4))
            pla = defaultdict(list)
            draws = set()
            for D, _, dev in fields:
                ds = symmetrize(dev)
                for d, v in shares(energy_by_order(transform(ds))).items():
                    obs[d].append(v)
                r = [x - y for x, y in zip(ds, fit)]
                for d, v in shares(energy_by_order(transform(r))).items():
                    res[d].append(v)
                den = sum(y * y for y in fit)
                al = (sum(x * y for x, y in zip(ds, fit)) / den
                      if den > 0 else 0.0)
                ra = [x - al * y for x, y in zip(ds, fit)]
                for d, v in shares(energy_by_order(transform(ra))).items():
                    resa[d].append(v)
                nt = centred([0.0] + ds[1:])
                for d, v in shares(energy_by_order(transform(nt))).items():
                    notriv[d].append(v)
                for sh in PLACEBO_SHIFTS:
                    p = placebo(ds, D, sh)
                    draws.add(tuple(round(x, 12) for x in p))
                    for d, v in shares(
                            energy_by_order(transform(p))).items():
                        pla[(d, sh)].append(v)
            fitsh = shares(energy_by_order(transform(fit)))
            print("    h+ %2d (%d fields, %.2f distinct placebo draws per"
                  " field):" % (h, len(fields), len(draws) / len(fields)))
            for d in divs:
                band = [mean(pla[(d, sh)]) for sh in PLACEBO_SHIFTS
                        if pla[(d, sh)]]
                print("      chi order %2d: OBS %.4f  FLAT %.4f  FIT %.4f "
                      " RES %.4f  RES-a %.4f  NO-TRIV %.4f  PLA %.4f-%.4f"
                      % (d, mean(obs[d]) if obs[d] else float("nan"),
                         totient(d) / (h - 1), fitsh.get(d, 0.0),
                         mean(res[d]) if res[d] else float("nan"),
                         mean(resa[d]) if resa[d] else float("nan"),
                         mean(notriv[d]) if notriv[d] else float("nan"),
                         min(band) if band else float("nan"),
                         max(band) if band else float("nan")))
        if not any_read:
            print("    no readable composite stratum")

    print("\nwall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
