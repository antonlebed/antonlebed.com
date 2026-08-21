r"""WHAT MAKES h = 3 THE ONE CLASS NUMBER WHOSE FIELDS DISAGREE WITH EACH
OTHER ABOUT THEIR OWN PRINCIPAL DENSITY? -- read one level DOWN, at the
TRIPLE of classes a totally split prime carries, where the model that
produced the disagreement is a uniformity assumption that mod-3 algebra
says can fail at h = 3 and cannot fail at a class number coprime to 3.

THE FINDING THIS ANSWERS. explore_cubic_class_map.py F3: the index of
dispersion of the per-field count of principal-carrying primes sits
below 1 at cubic class numbers 2, 4, 5, 6 and 7 -- the places are spaced
more regularly than chance -- and at h = 3 it reads 1.583 on 83 complex
fields, +3.8 on its own null spread and above 1 on all three references.
Neither sampling, nor the level, nor the share deficit. What is left is
field-to-field heterogeneity at the one class number where the class
group is Z/3.

WHERE THIS STANDS, AND WHY IT IS NOT THE EXCLUDED RIG. A degree-1
place's class is a Frobenius in the Hilbert class field H/K, so the
heterogeneity is a statement about how Frobenius distributes in a
degree-9 extension. This file does NOT build H. It reads the same
distribution off the object the map already produces -- the class of
every degree-1 place -- by asking a question about the three places over
one prime JOINTLY, which the count of principal primes marginalizes
away. The cyclic mechanism (a Galois orbit of three places carrying ONE
class, explore_cubic_class_map.py derivation (6)) is excluded from this
population by the population: a cyclic cubic field is totally real and
all 83 fields here are complex. What is NOT excluded, and is what this
file tests, is the MODULE DEGENERACY that the cyclic correction is one
instance of. That degeneracy is stated below for an arbitrary cubic
field and needs no Galois action on K at all.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. F3's
suspicion is written in the vocabulary of a FIELD and its COUNT -- 83
numbers, one per field, too spread out. The object here is a PRIME and
its TRIPLE, and the unit of the statistic is a totally split prime. The
translation is not a convenience: the count's model is built from a
per-prime probability q_split, and q_split is a marginal of the triple
distribution. So a wrong triple distribution is a wrong q_split, and a
q_split that differs field to field is over-dispersion in the count by
arithmetic. The suspicion becomes: the model's triple distribution is
uniform, and uniformity is a claim about a Galois image that mod-3
algebra allows to be smaller.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM THE CYCLIC CORRECTION: the SHAPE of the mechanism -- three
    places carrying one class rather than three -- is imported from
    derivation (6), which proves it at a CYCLIC field from an action of
    Gal(K/Q) on Cl(K). No such action exists at a non-Galois K, so the
    import is of the CONCLUSION's shape and not of its proof. The
    derivation below re-derives the trichotomy from the permutation
    symmetry of the three places alone, which every cubic field has.

 T2 FROM THE MAP: the enumeration, the maximal order, the place engines,
    the class reading, the relation harvest and the place-to-vector map
    are explore_cubic_class_map.py's and explore_cubic_principal.py's,
    imported rather than re-implemented. The per-field reader here is a
    near-copy of the map's own run_field, and it exists only because that
    function returns the boolean this file cannot use: it reports whether
    SOME place over p is principal and discards the vectors that say
    which. The two must agree, and C4 checks that they do at every prime.

 T3 THE INHERITED CONTROLS ARE RE-RUN, NOT ASSUMED. The map's h = 1 pin
    is the control the whole instrument rests on -- the identity where
    the answer is known in advance -- and it is run here rather than
    cited, because a file that reads new statistics off the same map is
    exactly a file that would carry a narrowed instrument silently.

 T4 THE STRATIFIER IS H, the relation reading, which the true h divides
    (the map's T3). A field whose true h is 1 misfiled at H = 3 would
    read a principal share of 1 and be a large positive outlier, which is
    a candidate explanation of the over-dispersion in its own right. It
    is not argued away: C5 measures it.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE TRIPLE, AND THE ONE CONSTRAINT ON IT. Let p be odd, unramified
      and totally split in the cubic field K, so (p) = P_1 P_2 P_3 with
      every P_i of residue degree 1. Then

          [P_1] + [P_2] + [P_3] = [(p)] = 0 in Cl(K),

      and there is no other constraint the class group imposes. Write

          M = { (c_1, c_2, c_3) in Cl^3 : c_1 + c_2 + c_3 = 0 },

      of order h^2. The model explore_cubic_principal.py derivation (2)
      uses -- and which the map's F3 index is computed against -- is that
      the triple is UNIFORM on M. That model gives

          q_split = P(some c_i = 0) = 1 - (h-1)(h-2)/h^2,

      which is 7/9 at h = 3.

  (2) WHAT THE TRIPLE ACTUALLY IS, AND WHY ITS RANGE IS A SUBGROUP. The
      three places over p are the three primes of K above p; there is no
      canonical order on them, so only permutation-invariant statements
      about the triple are well posed. THE SUBGROUP PROPERTY IS AN INPUT
      AND IS NAMED RATHER THAN WAVED AT, since everything below rests on
      it. Let N be the Galois closure of K and H~ the Galois closure of
      its Hilbert class field H. A prime is totally split in K exactly
      when its Frobenius is trivial in Gal(N/Q), so the primes this
      statistic runs over are exactly those whose Frobenius in H~/Q lies
      in the SUBGROUP Gal(H~/N). On that subgroup the assignment
      g |-> ([P_1], [P_2], [P_3]) is a group HOMOMORPHISM into M -- each
      coordinate is the restriction of g to one conjugate copy of H, and
      restriction is a homomorphism. Chebotarev fills Gal(H~/N), so the
      realized triples are exactly its image, hence a subgroup of M; and
      that image is stable under permuting the three coordinates because
      conjugating by an element of Gal(N/Q) permutes the copies while
      preserving the subgroup. Call it R. The two standard facts used are
      Chebotarev and the unramified-abelian description of H; nothing
      here computes in H~, whose degree is 54 at a generic field.

  (3) AT h = 3 THERE ARE EXACTLY THREE CANDIDATES FOR R. Take Cl = Z/3.
      M is 2-dimensional over F_3. Let sigma be the 3-cycle permuting
      coordinates. Over F_3 the permutation module is NOT semisimple:

          D = { (t, t, t) : t in Z/3 }

      lies in M -- the sum 3t is 0 -- and D is exactly the fixed space of
      sigma on M, since (sigma - 1) is nilpotent of square zero and
      nonzero on M -- so (sigma - 1)M = ker(sigma - 1) = D. Let L be a
      sigma-stable subgroup of order 3. For x in L, sigma(x) - x lies in
      L by stability and in D by the line above. If L were not D the two
      would be distinct subgroups of order 3, so L n D = 0, so sigma
      fixes L pointwise and L sits inside ker(sigma - 1) = D -- a
      contradiction. Hence L = D, and

          R is one of   0,   D,   M

      and nothing else. The three are three arithmetics:

          R = M   the model. q_split = 7/9. All three classes equal at
                  1/3 of split primes -- the triples (t,t,t).
          R = D   the DEGENERATE regime. Every split prime carries ONE
                  class three times. q_split = 1/3 = q_partial.
                  q_partial IS DERIVED AND NOT INHERITED, since the
                  triple argument says nothing about a prime with only
                  one degree-1 place: there (p) = P.Q with Q of degree 2
                  and [P] + [Q] = 0, so [P] alone carries the pair and
                  its realized set is a subgroup of Cl = Z/3 -- either 0
                  or all of it. Zero would make EVERY partially split
                  prime principal, which F1's measured shares exclude at
                  both regimes, so it is all of it and q_partial = 1/3
                  whatever R is. (SUPERSEDED IN ITS ARGUMENT AND NOT IN
                  ITS ANSWER, by explore_cubic_transposition.py: a
                  transposition Frobenius realizes a COSET and not a
                  subgroup, so the menu here is wrong and a realized set
                  of size 1 need not be the trivial class -- what
                  survives is the conclusion q_partial = 1/h, proved
                  there at every h from the ramification of N over K.) That is why the two regimes' shares
                  differ only through q_split.
      THE TWO SIDES OF THAT AGREEMENT ARE NOT EQUALLY STRONG, and F3's
      joint reading is why. At R = D both q's are 1/3, so the share is
      1/3 whatever else the triple distribution does and the agreement is
      a clean confirmation. At R = M the share depends on q_split, which
      the measured all-equal rate says is NOT 7/9 -- so the 45's landing
      within 3% of 4/9 is a NET of two departures pulling opposite ways
      and is weaker support than the 38's. What the 45 do confirm without
      qualification is that they are not degenerate: at R = D their share
      would be 1/3 and it is 0.4318.
          R = 0   every place principal, i.e. h = 1 -- the misfiling of
                  T4, not a regime of a genuine h = 3 field.

      THE CYCLIC FIELDS ARE THE KNOWN D. At a cyclic K the three places
      are one Gal(K/Q)-orbit and Aut(Z/3) has order 2, so sigma acts
      trivially on Cl and the three classes are equal -- R = D, which is
      derivation (6) of the map read in this vocabulary. The point of
      this file is that R = D is stated WITHOUT a Galois action on K, so
      it is available to a non-Galois field, where nothing has looked.

  (4) WHY THIS IS A MECHANISM FOR THE h = 3 EXCEPTION SPECIFICALLY. D is
      nontrivial exactly when Cl has 3-torsion, i.e. when 3 divides h;
      |D| = |Cl[3]| is 3 rather than 9 while 9 does not divide h, which
      no class number this population reaches does.
      Precisely: D is the group of triples that are EQUAL, and it is
      isomorphic to Cl[3], so at 3 not dividing h the only equal triple
      in M is (0,0,0) and a field whose every split prime had all three
      classes equal would have every place principal -- which is h = 1
      and not a regime. THE CLASSIFICATION ITSELF IS CLAIMED ONLY AT
      h = 3 AND THE SCOPE IS NOT DECORATIVE: at a composite class number
      M can carry proper stable subgroups that are not D at all -- at
      h = 4 the triples with entries killed by 2 form one, of order 4 --
      and this file neither classifies those nor tests for them. What it
      claims away from h = 3 is only that THIS degeneracy, the equal
      triple, is unavailable there. Concretely at h = 2, M has order 4,
      its only sigma-stable subgroups are 0 and M, and (1,1,1) does not
      even lie in M since 3 = 1 mod 2. So the degenerate regime DOES NOT
      EXIST at a class
      number coprime to 3, which is the shape of an answer to "why h = 3
      and no other class number". h = 6 is the one other stratum where D
      is nontrivial, and this population has 6 such fields -- below the
      reading threshold, printed and not read.

  (5) HOW A MIXTURE OF REGIMES BECOMES OVER-DISPERSION, WHICH IS THE
      WHOLE CLAIM. A field in the D regime has q_split = 1/3 where the
      model charges it 7/9. Its expected count of principal-carrying
      primes is therefore lower than the model's by (7/9 - 1/3) times its
      number of split primes -- about 0.44 * 28 = 12 primes at this cap,
      against a model mean near 47. A population mixing D fields and M
      fields has a bimodal count distribution whose spread is the GAP
      between the two means, not the arrangement inside either. That is
      exactly what an index of dispersion above 1 reports, and it is what
      the stratification amendment of the map already caught once, at the
      REAL h = 3 stratum, where the two populations were labelled cyclic
      and non-cyclic. The claim here is that the same thing is happening
      at the COMPLEX h = 3 stratum with no label on it.

  (6) THE ALGEBRAIC IDENTITY THAT MAKES THIS TESTABLE WITH NO MODEL. At
      h = 3, a triple in M with no zero entry has all three entries
      nonzero summing to 0 in Z/3, hence all equal -- {1,1,1} or {2,2,2}
      are the only such. So

          a totally split prime carries NO principal place
                  ==>  its three places have EQUAL class,

      with no probability in it. This is a pure control on the whole
      instrument (C3) and it is also the reason the regime is readable
      per field at this population's ~28 split primes per field: under
      R = M the equal-class fraction is 1/3, under R = D it is 1, and the
      binomial spread at n = 28 is 0.09.

  (7) THE TEST IS A MEMBERSHIP TEST AND NEEDS NO GROUP STRUCTURE. The
      map returns, for each place P, a vector a in Z^G with [P] = -a.[Q]
      against the relation lattice L. Then

          P is principal            iff  a in L
          P and P' have one class   iff  a - a' in L
          the triple sums to zero   iff  a + a' + a'' in L

      -- three calls to the same membership routine. No Smith normal
      form, no choice of generator for Cl, and every statistic below is
      invariant under relabelling the class group, which is what makes it
      comparable across fields. Non-membership is a proof of difference
      only once L is saturated, exactly as in the map; the map prices
      that gap and this file inherits the price rather than re-arguing it.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. THE DEGENERATE REGIME OCCURS AT NON-GALOIS FIELDS. At least one of
      the complex h = 3 fields reads an equal-class fraction above 0.9
      over at least 10 totally split primes.

  P2. THE FRACTION IS BIMODAL, NOT SPREAD. Sorting the complex h = 3
      fields by equal-class fraction leaves a gap of at least 0.25
      between two consecutive fields somewhere in [0.45, 0.95], and no
      field sits inside that gap -- the signature of two regimes rather
      than one noisy statistic.

  P3. THE REGIME EXPLAINS THE OVER-DISPERSION. Recomputing the index of
      dispersion of the principal count SEPARATELY within each regime
      group, every group of at least 5 fields reads below 1 -- so the
      1.583 of the map's F3 was the gap between the groups.

  P4. THE DEGENERACY IS ABSENT WHERE THE ALGEBRA FORBIDS IT. At every
      complex stratum with class number coprime to 3 and at least 5
      fields, the measured equal-class fraction agrees with the uniform
      model's |Cl[3]|/h^2 -- 1/4 at h = 2, 1/16 at h = 4, 1/25 at h = 5,
      1/49 at h = 7 -- within 0.10, and no field there reads above 0.9.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, read after the
controls and never before.

  K1 kills P1: the printed maximum equal-class fraction over complex
     h = 3 fields with at least 10 split primes. Below 0.9 kills it, and
     with it the mechanism: R = M at every field, and the heterogeneity
     is not this.

  K2 kills P2: the printed sorted fraction column. No gap of 0.25 in
     [0.45, 0.95] kills it -- a smooth spread is one arithmetic read
     noisily, or a third thing, and either way not the trichotomy.
     THE WINDOW IS A PROPERTY OF THE GAP AND NOT OF ITS LOWER END, which
     the first written form of this test got wrong and the trial run
     exposed: it required the gap to BEGIN inside [0.45, 0.95] and so
     scored a gap running 0.318 -> 1.000 -- which covers the window
     entirely and holds no field -- as no gap at all. What P2 says is
     that no field sits in the window and that the gap spanning it is at
     least 0.25, so that is what is measured: the largest gap
     INTERSECTING the window, beside the count of fields inside it.

  K3 kills P3: the printed per-regime index of dispersion, local
     reference. Any group of at least 5 fields at or above 1 kills it.

  K4 kills P4: the printed fraction against |Cl[3]|/h^2 at the coprime
     strata. A gap of 0.10 or more at a stratum of at least 5 fields, or
     any field above 0.9 there, kills it -- and would say the effect is
     not the mod-3 degeneracy but something the model gets wrong at every
     class number.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. THE CYCLIC PIN. The two cyclic cubic fields of the population with
      H > 1 -- discriminant 3969, totally real, H = 3 -- are PROVED to
      sit at R = D by derivation (6) of the map, which is independent of
      this file. Their equal-class fraction must print 1.000 exactly. A
      rig that cannot see D where D is proved is the instrument, and this
      is the one place in the population where the answer is known before
      the run. Printed as a fraction and a split-prime count per field.

  C2. THE INHERITED h = 1 PIN, RE-RUN. The map's C1: at fields with h
      certified 1 by exhibited generators, the map's lattice must have
      order 1 and no place may be called non-principal. Re-run here on
      the same stride sample rather than cited, since every statistic
      below reads the same map.

  C3. THE ALGEBRAIC IDENTITIES AT EVERY SPLIT PRIME, over the whole
      mapped population and not a sample. Two counts, both of which must
      be 0: primes whose three place-vectors do NOT sum into L (the class
      of (p) is not trivial, which is impossible); and, at h = 3 only,
      primes with no principal place whose three classes are NOT all
      equal (derivation (6), which is an identity and not a statistic).
      ITS DENOMINATOR IS PRINTED, added in the audit of the trial run and
      flagged rather than folded away: the second identity is vacuous at
      a split prime that DOES carry a principal place, so a zero
      violation count means nothing until the number of h = 3 split
      primes carrying none is beside it. That denominator is also what
      makes this control the SATURATION test the map could only price on
      a sample -- an unsaturated L is exactly what would make two places
      of one class read as different, which at a non-principal split
      prime is a violation. The identity is therefore checked where an
      unsaturated lattice would break it, at every such prime in the
      population rather than at 40.

  C4. THE MAP'S OWN VERDICT, RECOMPUTED. For every prime the reader here
      returns, "some place principal" computed from the vectors must
      equal what explore_cubic_class_map.py's run_field returns for the
      same field. Printed as a compared count and a mismatch count, which
      must be 0. This is what makes the near-copy of T2 safe.

  C6. THE INHERITED INDEX, REPRODUCED BEFORE IT IS SPLIT. P3 splits the
      map's F3 index of 1.583 into two groups, and a split of a number
      this file computes differently from the file that reported it is a
      split of a different number. So the whole-stratum index is computed
      here first and must agree with 1.583 to within 0.01 before any
      group reading is printed. ADDED AFTER THE FIRST RECORDED RUN AND
      FLAGGED RATHER THAN FOLDED AWAY, because it is what that run
      failed: the index came back 2.728 against the map's 1.583, and the
      cause was this file's own regime reader keying its per-field lookup
      by DISCRIMINANT, which up to four distinct cubic fields of this
      population share -- so the fields of a repeated discriminant were
      all handed one field's primes. Every S5 figure of that run was
      wrong and no other control could see it, all of them being about
      the map rather than about the reading built on it. The general
      species: a rig that RE-DERIVES an inherited statistic in order to
      decompose it owes a check that its own copy reproduces the
      original, and the check costs one line.

  C5. THE MISFILING CHECK OF T4. The printed per-field principal share
      at complex h = 3. A field whose true h is 1 reads 1.000; any field
      above 0.9 is reported as a misfiling candidate and excluded from
      the regime reading with the exclusion printed, never dropped
      silently.

RESOURCE. Pure integer arithmetic, per-field float embeddings and a 3x3
LLL, all inherited; no numpy, no BLAS, nothing held beyond one field's
places. Well under 512MB (the map peaked at 77 MB doing strictly more).
Wall clock: the class reading over the population is the dominant cost
at the map's own 158 s, the h = 1 pin 21 s, the map over the 236 fields
with H > 1 25 s, and this file adds only membership tests over vectors
already computed. Estimated 4-6 minutes, printed at the close, run under
memwatch.py. Over five minutes is possible and is the population read,
not this file's question.

SECTIONS.
  S1 the population and the class reading -- the engine, run first.
  S2 the controls: the h = 1 pin, the map's verdict recomputed, and the
     algebraic identities at every split prime.
  S3 the cyclic pin -- the equal-class fraction where R = D is proved.
  S4 the equal-class fraction at complex h = 3, per field and sorted,
     with the misfiling check beside it, and one covariate: how many
     fields of the population share the field's |d_K|. That column is a
     third amendment made in the audit of the trial run and flagged
     rather than folded away -- it is there because the trial's six
     non-degenerate fields were exactly the two discriminants carried by
     three fields each, which is the resolvent's 3-rank showing through
     the cheapest quantity that sees it. It is printed as a covariate and
     never as a prediction: nothing about it was frozen.
  S5 the index of dispersion recomputed within each regime group.
  S6 the coprime strata, where the algebra forbids the degeneracy.

FINDINGS.

  F1. THE DEGENERATE REGIME OCCURS AT NON-GALOIS CUBIC FIELDS, AND THE
      DICHOTOMY IS TOTAL RATHER THAN STATISTICAL (observation, 83 complex
      cubic fields of relation class number 3 to |d_K| <= 6000 over the
      odd unramified p <= 1000, 2023 totally split primes; P1 and P2 both
      SURVIVE; C1-C6 all clean). THIRTY-EIGHT of the 83 fields carry ONE
      class at all three places over EVERY totally split prime they have
      -- an equal-class fraction of exactly 1.000, on 17 to 27 split
      primes each. The other 45 read 0.000 to 0.375, mean 0.2143, against
      the uniform model's 1/3. NO FIELD LIES BETWEEN: the window
      [0.45, 0.95] holds none of the 83, and the sorted column jumps
      0.375 -> 1.000, a gap of 0.625 where P2 asked for 0.25. So this is
      not a tendency measured noisily; it is two arithmetics, and
      derivation (3) says there are exactly two available.
      THE SATURATION GAP CANNOT MANUFACTURE IT, and the direction is what
      says so rather than a price: two places read as ONE class only when
      their difference is PROVED to lie in the relation lattice, so an
      unsaturated lattice can only move a field from D toward M and never
      the reverse. The 38 are a positive certificate. The M side's
      non-equalities are the direction that needs saturation, and C3 is
      where an unsaturated lattice would surface -- the split primes
      carrying no principal place, every one of which must have equal
      classes by derivation (6), and every one of which does. (THE COUNT
      HERE READ 892 AND IS 753, corrected from
      explore_cubic_transposition.py's C6, which re-counts it: 892 is the
      DEGENERATE regime's split total from the line above, transcribed
      one quantity across. 753 = 595 at R = D and 158 at R = M, and it
      reconciles with the equal-class decomposition 1137 = 245 + 892 at
      384 all-principal equal triples. The control's verdict is
      untouched, the identity holding at every one of them.)
      AND THE TWO GROUPS' PRINCIPAL SHARES LAND ON THEIR OWN DERIVED
      VALUES, which was not frozen; at the degenerate group it is the
      finding's best independent support and at the other it is weaker,
      for the reason derivation (3) gives -- only R = D forces the share
      whatever else the triple distribution does. A non-Galois cubic field splits its primes 1/6 totally,
      1/2 partially and 1/3 inert, so the share of degree-1-carrying
      primes whose place is principal is (1/6 . q_split + 1/2 . 1/3)
      over 2/3 -- which is 1/3 at R = D and 4/9 at R = M. Measured, the
      38 read a mean share of 0.3232 (range 0.283-0.360) and the 45 read
      0.4318 (0.364-0.486): each low by about 3% of its own value -- 3.0%
      and 2.8% -- at
      R = D that 3% is the bottom-of-range share deficit and nothing else
      can enter, and at R = M it is a NET of the opposing departures F3
      measures, the same size by coincidence rather than by mechanism --
      and a factor of 4/3 apart -- which is NOT the two q's ratio of
      7/3 but what that ratio becomes once the partially split primes are
      averaged in, both regimes pricing those at 1/3 and those being
      three quarters of the degree-1-carrying primes.

  F2. THE h = 3 EXCEPTION DISSOLVES INTO THE MIXTURE, AND THE
      UNDER-DISPERSION HOLDS INSIDE BOTH HALVES (observation; P3
      SURVIVES). Recomputed on the map's own leave-one-out local
      reference, the index of dispersion of the per-field count of
      principal-carrying primes reads

          whole stratum   n = 83   1.583   z = +3.8   (C6, the map's F3)
          R = D           n = 38   0.220   z = -3.4
          R = M           n = 45   0.252   z = -3.5

      THE GROUPS ARE READ OFF THE SAME PRIMES THE COUNT IS, and that
      objection is answered by the size and the shape rather than left:
      removing a mixture carries an index down to 1 and no further, so
      0.220 and 0.252 are under-dispersion and not bookkeeping; and a
      degenerate field's fraction is 1.000 with no freedom in it, so the
      label is not a fitted cut through a continuum but the answer to
      whether the field has any unequal triple at all.
      -- so the entire excess was the GAP BETWEEN THE TWO GROUPS' means,
      and inside each the count is under-dispersed like every other class
      number, at 0.220 and 0.252 against the 0.123 to 0.461 the five
      unexceptional strata span. h = 3 was never an exception to the
      regularity; it was two populations under one label. That is the
      same failure the map's own stratification amendment caught at the
      REAL h = 3 stratum, where the two populations wore the labels
      cyclic and non-cyclic and the amendment could split them by
      reading a field's discriminant. Here they wear no label at all, and
      what separates them is a measurement.

  F3. THE DEGENERACY IS ABSENT WHERE THE ALGEBRA FORBIDS IT, AND THE
      COPRIME STRATA ARE SHORT OF THE MODEL IN THE SAME DIRECTION THE
      DISPERSION REPORTS (observation; P4 SURVIVES). Equal-class fraction
      measured against the uniform model's |Cl[3]|/h^2, complex fields:

          h = 2  n = 94   0.2147  against 0.2500   max field 0.375
          h = 4  n = 18   0.0273  against 0.0625   max field 0.120
          h = 5  n = 18   0.0125  against 0.0400   max field 0.042
          h = 7  n =  6   0.0069  against 0.0204   max field 0.040

      Every stratum inside P4's 0.10 and no field anywhere near 0.9, so
      the regime that splits h = 3 does not exist where 3 does not divide
      h -- which is what makes this an answer to "why h = 3 and no other
      class number" rather than a correction that would apply anywhere.
      ALL FOUR SIT BELOW THE MODEL, AND THE SHORTFALL DEEPENS WITH h,
      WHICH IS A SECOND THING AND IS NOT EXPLAINED HERE. Weighed against
      their own event counts rather than their field counts -- the
      statistic here is a count of all-equal triples, and its null spread
      is that count's -- the strata read

          h = 2   498 equal against 580.0 expected   0.859   z = -3.4
          h = 4    12 against 27.5                   0.436   z = -3.0
          h = 5     6 against 19.2                   0.312   z = -3.0
          h = 6     8 against 11.6                   0.691   z = -1.1
          h = 7     1 against 3.0                    0.338   z = -1.1

      so three of the five carry a reading and two do not, and the three
      that do run 0.86, 0.44, 0.31 -- a shortfall that GROWS with the
      class number. Two mechanisms would push this direction and neither
      fits: the share deficit of the parent rig's F2 is about 0.86 of
      nominal pooled and would give roughly that factor at every h, not a
      deepening; and a within-prime regularity WOULD deepen, since
      all-equal is a coincidence and h grows the number of ways to miss
      it, but the corpus's own index of dispersion is explicitly flat in
      h (the map's F3), so identifying the two is the thing this file
      must NOT do. It is left as measured and open (read 2026-08-21 by
      explore_triple_cube_term.py: the deepening is the explicit
      formula's cube term, the whole shortfall is not). h = 6, the one
      other stratum where D is nontrivial, reads 8 against 11.6 with
      its largest field at 0.167 -- no field degenerate by THIS
      fraction, though one of the six is by the exact 3-part test that
      file reads, at the equal fraction 1/4 its image gives -- and at
      z = -1.1 it decides nothing either way.

  F4. THE REGIME TRACKS WHETHER THE DISCRIMINANT IS SHARED, STRONGLY AND
      NOT EXACTLY (observation, and a COVARIATE rather than a prediction
      -- nothing about it was frozen; it is the third amendment's
      column). Of the 38 degenerate fields 31 are the only field of their
      d_K with class number above 1; of the 45 others, 44 share their d_K
      with at least one more. The arithmetic behind that is the
      resolvent's: the cubic fields of one discriminant correspond to the
      index-3 subgroups of the 3-class group of the quadratic resolvent
      Q(sqrt(d_K)), so their number is (3^r - 1)/2 for r its 3-rank --
      1 at r = 1 and 4 at r = 2. THE COLUMN AS PRINTED CANNOT SETTLE IT
      and says so by its own values: it counts only the fields with H > 1,
      so a family of 4 with a member at h = 1 shows here as 2 or 3, and
      2 and 3 are not possible family sizes. Nor is the association
      exact even allowing for that -- the three fields of d_K = -2891 are
      all degenerate while sharing a discriminant, and d_K = -2700 is
      alone at its own and is not. So what this leaves is a sharp next
      question and not a claim: whether R = D is exactly the r = 1 case,
      tested by enumerating each family over the WHOLE population rather
      than over its H > 1 part.

      SETTLING POINTER (explore_cubic_regime_sorter.py). That test was
      run and the answer is NO, in both directions: 24 of the 45 uniform
      fields have r = 1 and 35 of the 38 degenerate ones have r = 0. The
      reasoning in the paragraph above is wrong in one place and it is
      the same place both times -- the count (3^r - 1)/2 is the count of
      cubic fields of a FUNDAMENTAL discriminant, and d_K = -2891 =
      7^2 * (-59) is not one, so its family of three sits at conductor 7
      where a ray class group does the counting and 2 and 3 are legal
      sizes. What survives here is the COLUMN and not its reading: the
      association it measures is real, and what it tracks is the
      conductor rather than the 3-rank.

RUN RECORD. `python prime/code/memwatch.py python
prime/code/explore_cubic_split_triple.py`. One process, CPython, no BLAS.
10 checks, 237.4 s wall, peak working set 76.4 MB against memwatch's
512 MB ceiling. Enumeration 15370 polynomials -> 1103 fields in 7.8 s;
class reading 1103 fields in 157.8 s, 867 with h = 1 proved
constructively, 236 with H > 1, none unresolved; the inherited pin 62
fields in 20.8 s; the reader over the 236 mapped fields with the map's
own run_field beside it for C4, 25159 primes compared, in 51.0 s.
ONE EARLIER RUN IS IN THE REPOSITORY HISTORY AND ITS S5 TABLE IS NOT
QUOTED HERE: it read the whole stratum at 2.728 against the map's 1.583,
which is the disagreement C6 was written to catch and did -- the cause
being this file's own per-field lookup keyed by discriminant, which up
to four fields of this population share. Its S2, S3, S4 and S6 are
reproduced unchanged by the run above, the bug living wholly in the
regime reader.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_field_shop as CFS
import explore_cubic_principal as ECP
import explore_cubic_class_map as CCM

CHECKS = 0

DISC_CAP = ECP.DISC_CAP
PRIME_CAP = ECP.PRIME_CAP
BIN_EDGES = ECP.BIN_EDGES
MIN_STRATUM = ECP.MIN_STRATUM
ODD_PRIMES = ECP.ODD_PRIMES

MIN_SPLIT = 10          # split primes a field needs before its fraction reads
HIGH_FRAC = 0.9         # P1's degenerate threshold, and C5's misfiling one
GAP_LO, GAP_HI = 0.45, 0.95     # P2's window for the bimodality gap
GAP_MIN = 0.25                  # P2's gap
MAP_F3 = 1.583                  # C6: the index this file must reproduce


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg


def section(t):
    print("\n" + "=" * 68)
    print(t)
    print("=" * 68)


# ------------------------------------------------------- the reader
def read_field(O, a, b, c, d, cx, gen_places, rel0):
    """The map's run_field with the VECTORS kept (T2). Returns
    (H_map, piv, k, per_prime) where per_prime is a list of
    (p, kind, [vector or None per degree-1 place])."""
    pdisc = CFS.poly_disc3(a, b, c)
    rows = ECP.t2_rows(O, a, b, c)
    k = len(gen_places)
    idx = CCM.gen_index(gen_places)
    gen_by_prime = {}
    for col, (q, e, f, name, Q) in enumerate(gen_places):
        gen_by_prime.setdefault(q, []).append((col, f, Q))
    prime_set = sorted(gen_by_prime)

    rel = ([list(r) for r in rel0] if rel0 is not None
           else CCM.harvest(O, gen_places))
    per_place = []

    for p in ODD_PRIMES:
        if p <= CFS.REL_PRIME_CAP:
            pl = CFS.maximal_places(O, p)
            if any(e > 1 for (_, e, _) in pl):
                continue
            kind = ('split' if len(pl) == 3
                    else 'partial' if len(pl) == 2 else 'inert')
            if kind == 'inert':
                continue
            vecs = []
            for i, (Q, e, f) in enumerate(pl):
                if f != 1:
                    continue
                e_P = [0] * k
                e_P[idx[(p, i)]] = 1
                vecs.append(e_P)
            per_place.append((p, kind, vecs))
            continue

        places, kind = ECP.deg1_places(O, a, b, c, pdisc, p)
        if kind in ('ramified', 'inert'):
            continue
        vecs = []
        for P in places:
            got, saw_gen = CCM.map_place(O, P, p, rows, cx, gen_places,
                                         gen_by_prime, prime_set, k)
            if got:
                for i in range(1, len(got)):
                    rel.append([x - y for x, y in zip(got[0], got[i])])
                vecs.append(got[0])
            else:
                vecs.append(None)
        per_place.append((p, kind, vecs))

    piv = CCM.echelon(rel, k)
    return CCM.span_order(piv, k), piv, k, per_place


def is_principal(v, piv, k):
    return CCM.in_span(v, piv, k)


def same_class(u, v, piv, k):
    return CCM.in_span([x - y for x, y in zip(u, v)], piv, k)


def sums_to_zero(vs, piv, k):
    s = [0] * k
    for v in vs:
        s = [x + y for x, y in zip(s, v)]
    return CCM.in_span(s, piv, k)


def field_stats(per_prime, piv, k):
    """(n_split, n_equal, n_bad_sum, n_bad_identity, n_none, verdicts).

    n_equal counts totally split primes whose three places carry ONE
    class; n_bad_identity counts split primes with no principal place
    whose classes are not all equal, which derivation (6) forbids at
    h = 3 and which is meaningless elsewhere -- the caller reads it only
    at h = 3. n_none is that identity's DENOMINATOR, the split primes
    carrying no principal place at all, without which a zero violation
    count is not a control."""
    n_split = n_equal = n_bad_sum = n_bad_id = n_none = 0
    verdicts = []
    for (p, kind, vecs) in per_prime:
        if any(v is None for v in vecs):
            verdicts.append((p, kind, None))
            continue
        prin = any(is_principal(v, piv, k) for v in vecs)
        verdicts.append((p, kind, prin))
        if kind != 'split' or len(vecs) != 3:
            continue
        n_split += 1
        if not sums_to_zero(vecs, piv, k):
            n_bad_sum += 1
        eq = (same_class(vecs[0], vecs[1], piv, k)
              and same_class(vecs[0], vecs[2], piv, k))
        if not prin:
            n_none += 1
        if eq:
            n_equal += 1
        elif not prin:
            n_bad_id += 1
    return n_split, n_equal, n_bad_sum, n_bad_id, n_none, verdicts


# ------------------------------------------------------- the sections
def s1_population():
    section("S1  THE ENGINE -- enumeration and the class reading over the "
            "population")
    t0 = time.time()
    fields, buckets = ECP.enumerate_fields(DISC_CAP)
    print("  %d polynomials -> %d fields, %.1f s"
          % (buckets[0], len(fields), time.time() - t0))
    recs = []
    t0 = time.time()
    for (ad, d, cx, polys) in fields:
        a, b, c, O = polys[0]
        rows = ECP.t2_rows(O, a, b, c)
        h, kind, gen_places, rel = CCM.class_and_relations(O, d, cx, rows)
        recs.append((d, cx, a, b, c, O, h, kind, gen_places, rel))
    n_cert = sum(1 for r in recs if r[7] == 'cert')
    n_hi = sum(1 for r in recs if r[6] is not None and r[6] > 1)
    n_un = sum(1 for r in recs if r[6] is None)
    print("  class reading: %d fields, %d h = 1 proved constructively, "
          "%d with H > 1, %d unresolved, %.1f s"
          % (len(recs), n_cert, n_hi, n_un, time.time() - t0))
    ok(n_un == 0, "%d fields unresolved" % n_un)
    return recs


def s2_controls(recs):
    section("S2  CONTROLS -- the inherited h = 1 pin, the map's verdict "
            "recomputed, the algebraic identities")
    sample = [r for i, r in enumerate([x for x in recs if x[7] == 'cert'])
              if i % CCM.PIN_STRIDE == 0]
    bad_H = bad_place = 0
    t0 = time.time()
    for (d, cx, a, b, c, O, h, kind, gp, rel) in sample:
        H_map, piv, k, per_prime = read_field(O, a, b, c, d, cx, gp, rel)
        if H_map != 1:
            bad_H += 1
        for (p, kd, vecs) in per_prime:
            if any(v is None for v in vecs):
                continue
            if not any(is_principal(v, piv, k) for v in vecs):
                bad_place += 1
    print("  [C2] %d constructively certified h = 1 fields, %.1f s: "
          "%d with lattice order above 1, %d primes called non-principal"
          % (len(sample), time.time() - t0, bad_H, bad_place))
    ok(bad_H == 0, "%d certified h = 1 fields with H_map > 1" % bad_H)
    ok(bad_place == 0, "%d primes non-principal at h = 1" % bad_place)

    # the mapped population, read once and reused by every section below
    mapped = []
    bad_sum = bad_id = id_den = 0
    cmp_n = cmp_bad = 0
    t0 = time.time()
    for (d, cx, a, b, c, O, h, kind, gp, rel) in recs:
        if h is None or h == 1:
            continue
        H_map, piv, k, per_prime = read_field(O, a, b, c, d, cx, gp, rel)
        ns, ne, bs, bi, nn, verdicts = field_stats(per_prime, piv, k)
        bad_sum += bs
        if H_map == 3:
            bad_id += bi
            id_den += nn
        ref_H, ref_prime, unpl = CCM.run_field(O, a, b, c, d, cx, gp, rel)
        ref = dict((t[0], t[3]) for t in ref_prime)
        for (p, kd, prin) in verdicts:
            if p in ref:
                cmp_n += 1
                if ref[p] != prin:
                    cmp_bad += 1
        mapped.append((d, cx, H_map, ns, ne, verdicts))
    print("  [C4] %d primes compared against explore_cubic_class_map.py's "
          "own run_field, %d mismatches, %.1f s"
          % (cmp_n, cmp_bad, time.time() - t0))
    ok(cmp_bad == 0, "%d verdict mismatches against the map" % cmp_bad)
    print("  [C3] over every totally split prime of the %d mapped fields: "
          "%d whose three classes do not sum to zero; and of the %d h = 3 "
          "split primes carrying NO principal place -- the identity's own "
          "denominator, and the places an unsaturated lattice would break "
          "it at -- %d whose classes are not all equal"
          % (len(mapped), bad_sum, id_den, bad_id))
    ok(bad_sum == 0, "%d split primes with nonzero class sum" % bad_sum)
    ok(bad_id == 0, "%d split primes violating derivation (6)" % bad_id)
    return mapped


def share_of(verdicts):
    n = d = 0
    for (p, kd, prin) in verdicts:
        if prin is None:
            continue
        d += 1
        n += 1 if prin else 0
    return (float(n) / d if d else None), n, d


def s3_cyclic_pin(mapped):
    section("S3  C1 THE CYCLIC PIN -- the equal-class fraction where the "
            "degenerate regime is PROVED")
    print("  derivation (6) of explore_cubic_class_map.py proves R = D at "
          "a cyclic cubic field of class number 3, independently of this "
          "file. The fraction must read 1.000.")
    n = 0
    for (d, cx, H, ns, ne, verdicts) in mapped:
        if not CCM.is_cyclic(d) or H != 3:
            continue
        n += 1
        print("    d_K = %d  H = %d  split primes %d  equal-class %d  "
              "fraction %.3f" % (d, H, ns, ne, (float(ne) / ns) if ns else 0.0))
        ok(ns > 0 and ne == ns,
           "cyclic field d = %d reads %d of %d equal" % (d, ne, ns))
    ok(n >= 1, "no cyclic field with H = 3 in the population")
    print("  %d cyclic fields, all at fraction 1.000" % n)
    return n


def s4_fraction(mapped):
    section("S4  THE EQUAL-CLASS FRACTION at complex h = 3, per field")
    fs = [r for r in mapped if r[1] and r[2] == 3]
    mult = {}
    for r in mapped:
        mult[r[0]] = mult.get(r[0], 0) + 1
    rows = []
    for (d, cx, H, ns, ne, verdicts) in fs:
        sh, np_, dp = share_of(verdicts)
        # THE RECORD ITSELF AND NEVER ITS DISCRIMINANT (C6). A cubic
        # discriminant is carried by up to four distinct fields of this
        # population, so a per-field lookup keyed by d_K silently hands
        # every one of them the same field's primes.
        rows.append((d, ns, ne, (float(ne) / ns) if ns else None, sh,
                     mult[d], verdicts))
    rows.sort(key=lambda t: (t[3] is None, t[3]))
    print("  %d complex fields at H = 3. Model R = M gives 1/3; the "
          "degenerate R = D gives 1. Binomial SD at n = 28 is 0.089."
          % len(rows))
    mis = [t for t in rows if t[4] is not None and t[4] >= HIGH_FRAC]
    print("  [C5] misfiling check (T4): a true h = 1 field reads a "
          "principal SHARE of 1.000; %d fields at or above %.1f"
          % (len(mis), HIGH_FRAC))
    for t in mis:
        print("       d_K = %d  share %.3f" % (t[0], t[4]))
    print("  'sharing' is how many fields with H > 1 in this population "
          "carry the same d_K -- the covariate of the third amendment, "
          "printed and not predicted")
    print("  %-8s %-7s %-7s %-9s %-16s %s"
          % ("d_K", "split", "equal", "fraction", "principal share",
             "sharing"))
    for (d, ns, ne, fr, sh, mu, _v) in rows:
        print("  %-8d %-7d %-7d %-9s %-16s %d"
              % (d, ns, ne, "%.3f" % fr if fr is not None else "--",
                 "%.3f" % sh if sh is not None else "--", mu))
    read = [t for t in rows if t[1] >= MIN_SPLIT and t[3] is not None]
    hi = max((t[3] for t in read), default=None)
    print("  [K1] maximum fraction over %d fields with at least %d split "
          "primes: %s" % (len(read), MIN_SPLIT,
                          "%.3f" % hi if hi is not None else "--"))
    fr = sorted(t[3] for t in read)
    inside = sum(1 for x in fr if GAP_LO <= x <= GAP_HI)
    gap = (0.0, None)
    for i in range(1, len(fr)):
        g = fr[i] - fr[i - 1]
        if g > gap[0] and fr[i - 1] < GAP_HI and fr[i] > GAP_LO:
            gap = (g, (fr[i - 1], fr[i]))
    print("  [K2] fields with a fraction inside [%.2f, %.2f]: %d. Largest "
          "gap between consecutive fractions INTERSECTING that window: "
          "%.3f%s   (P2 asks for at least %.2f and none inside)"
          % (GAP_LO, GAP_HI, inside, gap[0],
             "" if gap[1] is None else "  (%.3f -> %.3f)" % gap[1],
             GAP_MIN))
    return rows, read


def index_local(group):
    """The map's S5 index against the bin's own measured share taken
    LEAVE-ONE-OUT (its K2 amendment II), computed over an arbitrary group
    of (d, verdicts, q_of_prime) records. Returns (n, index, z)."""
    nb = len(BIN_EDGES) - 1
    per = []
    for (d, prim) in group:
        if prim:
            per.append((d, prim))
    if not per:
        return 0, None, None
    totq = [0.0] * nb
    totc = [0.0] * nb
    for (d, prim) in per:
        for (i, q, c) in prim:
            totq[i] += q
            totc[i] += c
    ssl = vvl = 0.0
    n = 0
    for (d, prim) in per:
        myq = [0.0] * nb
        myc = [0.0] * nb
        for (i, q, c) in prim:
            myq[i] += q
            myc[i] += c
        ratio = []
        for i in range(nb):
            dq = totq[i] - myq[i]
            ratio.append((totc[i] - myc[i]) / dq if dq > 0 else None)
        cnt = mul = varl = 0.0
        usable = True
        for (i, q, c) in prim:
            cnt += c
            if ratio[i] is None:
                usable = False
                continue
            ql = min(1.0, q * ratio[i])
            mul += ql
            varl += ql * (1.0 - ql)
        if usable and varl > 0:
            ssl += (cnt - mul) ** 2
            vvl += varl
            n += 1
    if not n or vvl <= 0:
        return n, None, None
    ix = ssl / vvl
    return n, ix, (ix - 1.0) / (2.0 / n) ** 0.5


def prim_of(verdicts, h):
    out = []
    for (p, kind, prin) in verdicts:
        if prin is None:
            continue
        i = CCM.bin_of(p)
        if i is not None:
            out.append((i, ECP.q_nominal(kind, h), 1 if prin else 0))
    return out


def s5_regime(mapped, read):
    section("S5  THE INDEX OF DISPERSION recomputed WITHIN each regime "
            "group at complex h = 3")
    print("  the reference is the map's own local, leave-one-out one -- "
          "the only one a share deficit cannot leak into (its K2 "
          "amendment II). The map's F3 reads %.3f over the whole "
          "stratum, and [C6] this file must reproduce it before any "
          "split of it means anything." % MAP_F3)
    whole = [(t[0], prim_of(t[6], 3)) for t in read]
    n, ix, z = index_local(whole)
    print("  [C6] whole stratum as this file reads it: n = %d  index = %s"
          "  z = %s" % (n, "%.3f" % ix if ix else "--",
                        "%+.1f" % z if z is not None else "--"))
    ok(ix is not None and abs(ix - MAP_F3) < 0.01,
       "whole-stratum index %s does not reproduce the map's %.3f"
       % (ix, MAP_F3))
    groups = [("R = D  (fraction >= %.2f)" % HIGH_FRAC,
               [t for t in read if t[3] >= HIGH_FRAC]),
              ("R = M  (fraction <  %.2f)" % HIGH_FRAC,
               [t for t in read if t[3] < HIGH_FRAC])]
    out = []
    for (label, g) in groups:
        gg = [(t[0], prim_of(t[6], 3)) for t in g]
        n, ix, z = index_local(gg)
        print("  %-28s n = %-4d index = %-8s z = %s%s"
              % (label, n, "%.3f" % ix if ix else "--",
                 "%+.1f" % z if z is not None else "--",
                 "" if n >= MIN_STRATUM else "   (not read)"))
        out.append((label, n, ix, z))
    return out


def s6_coprime(mapped):
    section("S6  THE COPRIME STRATA -- where the algebra forbids the "
            "degeneracy")
    print("  the uniform model's equal-class fraction is |Cl[3]| / h^2: "
          "1/4 at h = 2, 1/3 at h = 3, 1/16 at h = 4, 1/25 at h = 5, "
          "1/12 at h = 6, 1/49 at h = 7. D is nontrivial only at h = 3 "
          "and h = 6.")
    print("  %-3s %-5s %-8s %-8s %-9s %-9s %s"
          % ("h", "n", "split", "equal", "measured", "model", "max field"))
    rows = []
    for h in (2, 3, 4, 5, 6, 7):
        fs = [r for r in mapped if r[1] and r[2] == h]
        if not fs:
            continue
        ns = sum(r[3] for r in fs)
        ne = sum(r[4] for r in fs)
        t3 = 3 if h % 3 == 0 else 1
        model = float(t3) / (h * h)
        best = max((float(r[4]) / r[3] for r in fs if r[3] >= MIN_SPLIT),
                   default=None)
        rows.append((h, len(fs), ns, ne, float(ne) / ns if ns else None,
                     model, best))
        print("  %-3d %-5d %-8d %-8d %-9s %-9.4f %s%s"
              % (h, len(fs), ns, ne,
                 "%.4f" % (float(ne) / ns) if ns else "--", model,
                 "%.3f" % best if best is not None else "--",
                 "" if len(fs) >= MIN_STRATUM else "   (not read)"))
    return rows


def main():
    t0 = time.time()
    recs = s1_population()
    mapped = s2_controls(recs)
    s3_cyclic_pin(mapped)
    rows, read = s4_fraction(mapped)
    s5_regime(mapped, read)
    s6_coprime(mapped)
    section("SUMMARY")
    print("  %d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
