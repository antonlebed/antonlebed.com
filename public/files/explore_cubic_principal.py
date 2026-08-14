r"""DOES THE PER-PLACE READING'S FLAT COVERAGE SURVIVE MORE PLACES AND A
BIGGER CLASS GROUP? -- the least principal degree-1 place over cubic
fields, both signatures, against a first-hit model at the nominal
splitting density.

THE QUESTION. Over quadratic fields one statistic has been narrowed
by three earlier rigs: L_1, the least prime carrying a PRINCIPAL
residue-degree-1 place. Over imaginary quadratic fields it carries a
coverage floor L_1 >= |D|/4, and that floor is a UNIT-RANK phenomenon --
a definite norm form has a size floor and an indefinite one does not --
so over real quadratic fields the floor is ABSENT and coverage runs flat
at 99.8-100% across every sweep band (explore_real_principal.py F1-F2).
What is left there is a small residual: fed each field's own measured
local principal share as its density, the first-hit model OVERSHOOTS the
measured L_1 by 8-29%, flat in the class number, and traced in SIGN to
the under-dispersion of the principal primes -- index 0.386 at h = 2 over
the bottom decade against 1 for independence (explore_paired_division.py
F1-F4).

Rank and signature are ONE condition at degree 2: by Dirichlet a number
field has unit rank 0 exactly when it is Q or imaginary quadratic, which
is exactly when the norm form is definite. So no quadratic field tells
them apart and widening within degree 2 cannot ask which the floor
answered to. What a widening to degree 3 CAN ask is a different question,
and it is the one this rig asks: does the flat coverage survive when a
field has MORE PLACES OVER EACH PRIME and a BIGGER CLASS GROUP, and does
the mechanism that survived at degree 2 -- a share short at small p, a
count under-dispersed against its own density -- reproduce there.

Both cubic signatures have infinite unit groups (rank 1 complex, rank 2
totally real), so neither carries the floor, and the comparison inside
degree 3 is a comparison of RANKS at a fixed absence of the floor. That
is the one thing degree 2 could not stage.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The suspicion
is about a DENSITY of principal places among the primes a field reads,
so it is written in the SPLITTING TYPE's vocabulary and not in the
quadratic engine's. At degree 2 a prime is split or it is not, and the
quadratic rigs could speak of "split primes" and mean "primes carrying a
degree-1 place" in one breath. At degree 3 those come apart: a rational
prime has three unramified shapes and TWO of them carry a degree-1 place.
So every statement here is about a PLACE and its residue degree, never
about a prime and its splitting, and the principality test is applied to
the degree-1 PLACE. That is the roadmap's fifth trap and it is what
forces the vocabulary.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM DEGREE 2 TO DEGREE 3: the SHAPE of every prediction below --
    coverage flat, share short at the bottom, model undershooting and
    climbing in h, count under-dispersed -- is imported from quadratic
    measurements and is exactly what is under test. Nothing is assumed
    from it; P1-P4 are what the import commits to and K1-K4 are what
    refuse it.
 T2 FROM THE SHOP: the enumeration (Hunter's box), the Round-2 maximal
    order, the algebra-split places, the relation Hermite order and the
    unit-reduced certificate are explore_cubic_field_shop.py's, imported
    rather than re-implemented, and its own certified values are the
    control (C2, C3). What this file ADDS to them is the ideal-lattice
    generator search of derivation (3) and everything downstream of it,
    and the widened maximal order the shop's own sieve assert refuses at
    this discriminant cap. The shop's FINGERPRINT ASSUMPTION comes with
    them and is carried unexamined: fields are separated inside one
    discriminant by their splitting shapes at the primes to 300, so two
    non-isomorphic fields of the same discriminant agreeing at every one
    of those primes would be counted once. Nothing here tests that, and
    the direction is a population one field short rather than a wrong
    reading at any field.
 T3 THE NOMINAL DENSITY is Chebotarev's over the Galois closure plus a
    uniform-class assumption; it is a MODEL and the measurement is what
    grades it, never the other way round.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) WHAT L_1 IS AT DEGREE 3, AND WHICH PRIMES IT READS. L_1(K) is the
      least ODD prime p, UNRAMIFIED in K, carrying a residue-degree-1
      place that is PRINCIPAL. Three restrictions, each with a reason
      the quadratic rigs already paid for. ODD: p = 2 is the budget
      inequality's and is not part of L_1 anywhere in this corpus.
      UNRAMIFIED: the quadratic statistic ran over chi_D(p) = +1 and so
      excluded the ramified primes, whose place has residue degree 1
      too; including them here would measure a different quantity and
      compare it to that one. DEGREE-1 PLACE, not "split prime": at
      degree 3 a prime with a degree-1 place may also carry a degree-2
      place, and it is the place that is tested.

  (2) THE SPLITTING TYPES AND THE NOMINAL DENSITY. Let K be cubic with
      Galois closure L. For p unramified, Frobenius is a conjugacy class
      in Gal(L/Q). If K is non-cyclic (L has group S3) the classes are
      the identity (density 1/6, p splits completely, THREE degree-1
      places), a transposition (density 1/2, one degree-1 place beside
      one degree-2 place), and a 3-cycle (density 1/3, p inert, NO
      degree-1 place). If K is cyclic (group C3, d_K a perfect square)
      only two shapes occur: split completely (density 1/3) and inert
      (2/3). So a non-cyclic cubic field reads 2/3 of the primes and a
      cyclic one reads 1/3, against a quadratic field's 1/2.

      Now the classes. Write h for the class number. At a partially
      split prime, P * Q = pO is principal with P of degree 1 and Q of
      degree 2, so [P] = -[Q] and nothing constrains [P]; modelled
      uniform on Cl it is principal with probability 1/h. At a totally
      split prime, P1 P2 P3 = pO, so [P1] + [P2] + [P3] = 0, and
      modelled uniform on that subgroup the triple is uniform over the
      h^2 pairs ([P1], [P2]). The chance that NO place is principal is
      the count of pairs with c1, c2 and c1 + c2 all nonzero, divided by
      h^2. Inclusion-exclusion over the three conditions gives
      h^2 - (3h - 2) pairs excluded, hence (h-1)(h-2) pairs surviving --
      a count independent of the GROUP STRUCTURE, only of h. So

          q_split(h)   = 1 - (h-1)(h-2)/h^2,
          q_partial(h) = 1/h,

      and q_split is 1 at h = 1 and 2 alike, first dropping below 1 at
      h = 3 (7/9). That the split shape is MUCH likelier to yield a
      principal place than the partial one is the concrete form of "more
      places" in this question.

      THIS IS WRONG AT A CYCLIC FIELD, corrected after the run below and
      swapped in here rather than narrated: at a cyclic cubic field the
      three places over a totally split prime are ONE Galois orbit, not
      three draws, and at h = 3 the action is forced trivial (Aut(Z/3)
      has order 2), so the three classes are EQUAL and q_split is 1/h and
      not 1 - (h-1)(h-2)/h^2. The derivation and the measurement
      confirming it are explore_cubic_class_map.py derivation (6) and F4.
      The affected stratum here is the totally real h = 3 one, 2 of whose
      6 fields are cyclic; F2 and F4 below carry the corrected reading.

  (3) THE PRINCIPALITY TEST, WHICH IS THE ONE NEW INSTRUMENT. A
      degree-1 place P has norm p, so an element alpha in P with
      |N(alpha)| = p satisfies alpha*O contained in P with equal index,
      hence alpha*O = P: finding one PROVES P principal, and no class
      group is consulted. The search is over the rank-3 lattice P, and a
      raw coefficient box in the order's own basis is the wrong shape --
      the short elements of P sit at coordinates the basis does not make
      small. So P is LLL-reduced against the T2 form
      sum_k |sigma_k(alpha)|^2 -- three real embeddings when d > 0, one
      real and the doubled complex pair when d < 0 -- and the search box
      is a coefficient box in the REDUCED basis. Every hit is checked by
      the exact integer norm, so a float reduction cannot manufacture
      one; it can only fail to find one.
      AND ONE REDUCTION IS NOT ENOUGH, WHICH THE PIN IS WHAT TAUGHT.
      T2 alone finds the SHORTEST elements of P, and the shortest element
      of a principal place need not be a generator: everything in P has
      norm divisible by p, and an element of norm 2p or 3p can be shorter
      than the best-balanced generator whenever the fundamental unit is
      large -- which it is, the regulator of a complex cubic growing with
      the discriminant. A generator's SIZE is set by the unit group, so
      growing the box is the wrong axis and grows as its cube for
      nothing. What the search sweeps instead is the UNIT DIRECTION: the
      same lattice re-reduced under embeddings reweighted by a
      determinant-1 weighting, which undoes a power of the unit and makes
      the generator near-minimal under one weighting of the grid. One
      direction for a complex cubic, two for a totally real one -- the
      unit ranks -- and the grid escalates only where the unweighted
      reduction failed, so the common case pays one reduction.
      THE FAILURE DIRECTION IS THE WHOLE CAUTION AND IT IS ONE-SIDED. A
      missed generator makes the field's L_1 LARGER and coverage
      SMALLER, never the reverse. Every coverage number printed here is
      therefore a LOWER bound on the truth, which is the safe side for
      P1 and the unsafe side for nothing.
      C1 is what prices it: at a field with h = 1 every place is
      principal, so L_1 must equal the least odd unramified prime
      carrying a degree-1 place at all, and any field where it does not
      is a field where the box was too small. The pin is an identity and
      the mismatch count is the instrument's error rate, printed rather
      than assumed to be zero.

  (4) THE CLASS NUMBER, AND WHY IT IS A STRATIFIER AND NOT A RESULT.
      L_1 does not consult h; h only sorts the fields. Two readings are
      used and they differ in what they prove. If every place of norm
      under the Minkowski bound is found principal by (3), then h = 1 is
      CERTIFIED constructively -- the class group is generated by those
      places. Otherwise the relation reading of the shop applies: smooth
      principal elements over the places to a fixed norm cap give a
      lattice L inside Z^k, Z^k/L surjects onto Cl, and its order H is a
      multiple of h. So H is an upper reading and h divides it; where
      H = 1 it is exact. A field misfiled by H lands in a neighbouring
      stratum and nothing else -- which is why this is allowed to be a
      reading rather than a certificate, and why C2 and C3 grade it
      against values the shop certified.

  (5) THE FIRST-HIT MODEL AND ITS CENSORING. The model runs over the
      field's OWN sequence of odd unramified primes carrying a degree-1
      place -- the splitting is not random, Frobenius decides it -- and
      randomizes only principality, at the q of (2) chosen by that
      prime's own type. With hits at p_1 < p_2 < ... and probabilities
      q_i,

          P(L_1 = p_i) = q_i * prod_{j<i} (1 - q_j),

      and the predicted mean is sum p_i P(L_1 = p_i) divided by the mass
      P(L_1 <= cap). Dividing by the mass is what conditioning on the
      hit landing below the cap means, and the MEASUREMENT drops the
      same fields for the same reason: censor both sides or the
      comparison is void. Both the mass and the observed drop rate are
      printed. This is the paired division's sharpened constant model,
      which is the right incumbent to port: the old geometric draw over
      all odd primes was shown to be model FORM worth 1.15x at h = 1,
      and a rig that ports the error would re-remove what is
      already removed.

  (6) THE SHARE, READ AT THE SCALE IT IS FED AT. The share is the
      fraction of degree-1-carrying primes whose degree-1 place is
      principal, and at degree 2 it was found to be a function of p that
      CLIMBS -- 0.662 of nominal in 1-1000 against 0.964 in 3000-10000
      at narrow class number 8 -- so a share pooled over a range and fed
      to a model hitting at p ~ 30 is the error the quadratic rigs had
      to remove. Here the share is reported in frozen prime bins and
      never pooled into the model. This rig does not FEED it back: the
      local-share division is the next instrument and it needs the
      leave-one-out machinery of explore_paired_division.py. What is
      asked here is only whether the degree-2 SHAPE reproduces.

  (7) THE DISPERSION, WHICH IS THE MECHANISM THAT SURVIVED. Count, per
      field, the primes below the cap carrying a principal degree-1
      place. Under the model of (5) that count is a sum of independent
      Bernoullis with the field's own q_i, so its mean is sum q_i and
      its variance sum q_i(1-q_i). The index of dispersion -- summed
      squared deviation over summed variance -- is 1 under independence
      and below 1 under a more regular arrangement. At degree 2 it came
      in at 0.386 at h = 2 over the bottom decade. Being a statement
      about a COUNT it needs no first-hit model at all, which is what
      makes it the cleanest port.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. COVERAGE IS FLAT AND FULL AT BOTH SIGNATURES. The fraction of
      fields with L_1 at or below the sweep bound is at least 99% at
      every band from 100 upward, at both signatures and at every class
      number carrying at least 5 fields. The degree-2 real side ran
      99.8-100%; more places should only help.

  P2. THE SHARE IS SHORT AT THE BOTTOM AND CLIMBS. At every class number
      at least 2 with at least 5 fields, the measured share of
      degree-1-carrying primes with a principal degree-1 place, divided
      by the nominal q of (2), is below 1 in the bottom bin and larger
      in the top bin than in the bottom.

  P3. THE NOMINAL MODEL UNDERSHOOTS AND THE UNDERSHOOT CLIMBS IN h.
      Measured mean L_1 over predicted mean L_1 exceeds 1.10 at every
      class number at least 2 with at least 5 fields, and the ratios do
      not fall as h rises. This is the degree-2 incumbent's own
      signature (1.15 at h = 1 rising to 3.23 at h = 6) and it is what a
      density deficit at small p looks like through a first hit.

  P4. THE COUNT IS UNDER-DISPERSED. The index of dispersion of (7) sits
      below 1 at every class number with at least 5 fields, at both
      signatures.

  P5. SIGNATURE DOES NOT GRADE ANY OF IT. At a fixed class number
      carrying at least 5 fields on both sides, the complex and totally
      real ratios of P3 differ by less than 0.25, and the shares of P2
      by less than 0.10. Both signatures have infinite unit groups and
      no floor; if unit RANK graded the reading, this is where it would
      show.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, read after the
controls and never before.

  K1 kills P1: the printed coverage table, one row per signature and
     class number, one column per band. A cell below 99% at a band of
     100 or more, in a stratum of at least 5 fields, kills it there.

  K2 kills P2: the printed share table, share over nominal by prime bin.
     A stratum whose bottom bin sits at or above 1, or whose top bin
     does not exceed its bottom bin, kills it there.

  K3 kills P3: the printed "ratio" column. A stratum of at least 5
     fields at h >= 2 with a ratio at or below 1.10 kills it there; a
     ratio column falling as h rises kills the second half.

  K4 kills P4: the printed index of dispersion. An index at or above 1
     in a stratum of at least 5 fields kills it there.

  K5 kills P5: the two signature-split columns of the ratio and share
     tables at a shared class number.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. THE IDENTITY PIN AT h = 1. At every field with h certified 1,
      predicted L_1 equals measured L_1 exactly, because every q is 1
      and the model puts all its mass on the first degree-1-carrying
      prime; and measured L_1 equals the least odd unramified prime
      carrying a degree-1 place. Printed as two mismatch counts over the
      certified stratum, both of which must be 0, and as the count of
      fields they ran over. This is the roadmap's fourth trap -- pin the
      instrument where the answer is an identity -- and it doubles as
      the price of the search box of derivation (3).

  C2. THE CLASS ENGINE AT DEGREE 2. The relation reading, run on the
      three filed quadratic rings, must give 1, 2, 3 for Z[i],
      Z[sqrt(-5)] and Z[omega] of discriminant -23.

  C3. THE ENUMERATION AND THE FIRST h > 1 FIELD, against the shop's own
      certified line: the least complex cubic discriminant is -23 and
      the least totally real one is 49; the first field with h > 1 in
      |d| order is d = -283 with H = 2.

  C4. THE SPLITTING CENSUS AGAINST CHEBOTAREV. Pooled over the
      non-cyclic fields, the fractions of odd unramified primes below
      the cap that split completely, split partially and stay inert must
      sit within 0.02 of 1/6, 1/2 and 1/3; over the cyclic fields,
      within 0.03 of 1/3, 0 and 2/3. The place engine and the model's
      density are then reading the same arithmetic.

  C4 AMENDMENT, made after C4's pooled form FIRED on a trial run and
  before the recorded one, and flagged rather than folded away. The
  pooled fractions over odd primes to 1000 came in at 0.1459, 0.5115,
  0.3426 against 1/6, 1/2, 1/3 -- the split fraction low by 0.021, nine
  times its own standard error, so not sampling. Extending the same
  census to 10000 shows why: the split fraction runs 0.062, 0.115,
  0.155, 0.154, 0.162 over the bins 3-30, 30-100, 100-300, 300-1000,
  1000-10000. It CONVERGES to nominal from below, and slowly, which is
  Chebotarev's own rate at small p and not an engine fault -- the
  cross-engine check below confirms the place count independently. So
  the frozen C4 was mis-specified: a tolerance on a pooled fraction over
  a range whose bottom is exactly where the density is not yet nominal
  tests the ARITHMETIC and not the instrument, and the tolerance itself
  was a margin chosen by hand rather than derived. It is replaced by two
  controls that are neither.

  C4a. THE TWO PLACE ENGINES AGREE. Off the polynomial discriminant the
      degree-1 places are read from the linear factors of the defining
      polynomial; on it, from the algebra O/pO. Run BOTH on a sample of
      (field, prime) pairs off the discriminant, where either is valid:
      the degree-1 place COUNT must agree everywhere. Printed as a
      mismatch count, which must be 0.

  C4b. THE CENSUS CONVERGES. The type census is printed by prime bin
      rather than pooled, and what is required of it is monotone
      approach and not a hand tolerance: each of the three fractions
      must be nearer nominal in the top bin than in the bottom one --
      measured as the TOTAL VARIATION distance of the census from
      nominal, the census being a distribution and TV the scalar that
      reads it as one, a per-component demand being wrong for a
      component that starts near nominal and crosses over -- and each
      component of the top bin within 0.02 for the non-cyclic fields.

  THAT SMALL-p DEFICIT IS ITSELF A DATUM AND IT IS LOAD-BEARING FOR P3.
  At degree 2 the bottom-of-range deficit lived entirely in the
  principal SHARE, the splitting being decided by a quadratic character
  with no such lag. At degree 3 part of it lives in the SPLITTING, before
  principality is asked. So a nominal-density model here is short at
  small p for a reason that has nothing to do with the class group, and
  any undershoot P3 reports carries that component inside it. S4 prints
  the share against the nominal q, so this is exactly the confound to
  read for -- and it is why the local-share division, which reads the
  measured density including the splitting lag, is the next instrument
  rather than an optional refinement.

  C5. THE NORM IDENTITY AT EVERY CERTIFIED GENERATOR. Every generator
      the search returns is re-checked: it lies in the place's lattice
      and its exact integer norm has absolute value exactly p. Printed
      as a count of generators certified and a mismatch count, which
      must be 0.

  C6. THE PLACE HAS THE NORM THE TEST ASSUMES. Everything downstream
      rests on a degree-1 place having index exactly p in the order: it
      is what makes an element of P with |N| = p a GENERATOR rather than
      merely a member, and it is the one error whose direction inflates
      coverage -- a lattice larger than P would admit elements of norm p
      that generate something else, and every such hit would read as a
      principal place. So the determinant of each place's Hermite basis
      is computed and compared to p. Printed as a count of places
      checked and a mismatch count, which must be 0.

RESOURCE. Pure integer arithmetic plus per-field float embeddings and a
3x3 LLL, no numpy, no arrays held beyond one field's places. Cubic fields
by Hunter's box to |d_K| <= 6000; odd unramified primes to 1000. Well
under 512MB. Wall clock is the open quantity, dominated by the relation
reading at the fields with h > 1, estimated at under ten minutes and
printed at the close; the run is under memwatch.py.

SECTIONS. The sweep runs BEFORE the controls that read it, which is why
it sits inside the S1 block rather than after it.
  S1a the degree-2 class engine against three filed class numbers.
  S1b the enumeration, against the shop's own least discriminants.
  S1c the sweep: class reading and L_1 per field -- the engine.
  S1d the two place engines, the census by bin, the h = 1 identity pin.
  S2  the population: fields by signature and class number.
  S3  coverage: L_1 against the sweep bands, by signature and class
      number.
  S4  the first-hit model at the nominal density: measured mean L_1
      over predicted, by signature and class number.

FINDINGS.

  F1. COVERAGE SURVIVES THE DEGREE LIFT WHOLE, AND THE SCALE FALLS
      (observation, 1103 cubic fields to |d_K| <= 6000, odd unramified
      primes to 1000; P1 SURVIVES at the bands from 250 up, KILLED at
      100). Every stratum -- both signatures, class numbers 1 to 8 --
      reads 100.0% coverage at the sweep bands 250 and 1000, and no
      field in the population lacks a certified principal degree-1 place
      below 1000. Coverage is a LOWER bound by derivation (3), so 100.0%
      is exact. The mean L_1 runs 5.6 at complex h = 1 to 66.0 at
      complex h = 7 and 6.1 to 47.3 across the real side, against the
      real QUADRATIC side's 6.1 to 178.6 over the same statistic and the
      same prime cap. The two populations are not the same range --
      |D| <= 4000 there against |d| <= 6000 here -- and the difference
      runs AGAINST the comparison, a wider discriminant range carrying
      larger class groups ON AVERAGE and so a longer wait -- which is an
      argument from the class number formula and not something measured
      here. So
      more places over each prime buys a SHORTER wait, which is what
      2/3 of the primes carrying a degree-1 place rather than 1/2, and
      three chances at a split one, should do.

      What kills P1 at the band of 100 is the tail at large h, and it is
      the honest half of the answer: complex h = 6 and h = 7 read 66.7%
      there on 6 fields each, and h = 4 reads 83.3% at the band of 50.
      Coverage is flat in the class number only from 250 up; below that
      it grades with h, sharply. The floor's absence is what makes the
      coverage FULL; it is the class group that decides how long it
      takes, and the two are separate facts.

  F2. THE NOMINAL MODEL UNDERSHOOTS AT EVERY CLASS NUMBER ABOVE 1, AND
      IS AN IDENTITY AT 1 (observation; P3's first half SURVIVES, its
      second half UNREADABLE; C1 exact). Measured mean L_1 over the mean
      predicted by the first-hit model at the nominal Chebotarev density
      of derivation (2):

          complex   h = 1  n = 661   5.6 /   5.6 = 1.000
                    h = 2  n =  94  11.3 /   7.1 = 1.594
                    h = 3  n =  83  14.3 /  12.2 = 1.172
                    h = 4  n =  18  28.9 /  17.4 = 1.661
                    h = 5  n =  18  30.1 /  22.1 = 1.364
                    h = 6  n =   6  62.0 /  19.3 = 3.206
                    h = 7  n =   6  66.0 /  41.9 = 1.577
          real      h = 1  n = 206   6.1 /   6.1 = 1.000
                    h = 3  n =   6  47.3 /  25.9 = 1.826

      The h = 1 rows are the identity of C1 and not a measurement: every
      q is 1 there, the model puts all its mass on the first
      degree-1-carrying prime, and it lands on it at all 867 certified
      fields individually. Above h = 1 the model arrives EARLY at every
      readable stratum -- the degree-2 incumbent's own direction, and by
      1.17x to 3.21x against that incumbent's 1.15x to 3.23x. So the
      thing the quadratic corpus priced across three rigs is not a
      quadratic artifact: a first hit read at the bottom of the prime
      range arrives later than a nominal density says, at degree 3 too.

      The two strata under 5 fields -- complex h = 8 on 2 and real h = 2
      on 3 -- are printed by the rig and left out of the table above
      rather than dropped silently; neither is read.

      The real h = 3 row is the CORRECTED one: the engine below computes
      it at the uncorrected q of derivation (2) and prints 17.5 and
      2.709, and the corrected prediction of 25.9 is
      explore_cubic_class_map.py S6's, measured over the same six fields
      and the same measured mean of 47.3. The engine is left as it ran;
      the number quoted is the true one.

      P3's second half asked for no FALL in h and the column does not
      answer: 1.594, 1.172, 1.661, 1.364, 3.206, 1.577 is not monotone
      in either direction, and at 6 to 94 fields a stratum there is no
      reference distribution here to say whether that is trend or noise.
      It is recorded as unreadable rather than as survived. Building the
      reference is the local-share division's job, where the quadratic
      side regenerated the bits 60 times to price exactly this.

  F3. AT DEGREE 3 PART OF THE BOTTOM-OF-RANGE DEFICIT LIVES IN THE
      SPLITTING, BEFORE PRINCIPALITY IS ASKED (observation; the C4
      amendment's own census, 1091 non-cyclic fields). The fraction of
      odd unramified primes that split completely runs 0.1043, 0.1212,
      0.1414, 0.1575 over the bins 3-30, 30-100, 100-300, 300-1000
      against a nominal 1/6, and the total variation of the whole census
      from nominal falls 0.0685 -> 0.0092 across those bins. It
      converges, and slowly. At degree 2 the splitting was decided by a
      quadratic character with no such lag and the entire
      bottom-of-range deficit sat in the principal SHARE; here a
      component of it is upstream of the class group entirely. That is a
      confound the nominal model of F2 carries inside its undershoot,
      and it is the sharpest argument that the local-share division --
      which reads the density a field actually has, splitting lag
      included -- is the next instrument and not a refinement.

  F4. THE UNIT RANK SEPARATES THE TWO SIGNATURES AT A SHARED CLASS
      NUMBER, ON SIX FIELDS (observation; P5 KILLED on its ratio clause,
      its share clause carried by the unrun P2). Two class numbers carry
      at least 5 fields on both signatures, h = 1 and h = 3, and at
      h = 1 both sides read 1.000 because both are the identity of C1 --
      P5 cannot be tested where its two sides are forced equal. So h = 3
      is the only stratum where the comparison is a measurement, and the
      ratios there are 1.172
      (complex, 83 fields, unit rank 1) against 1.826 (real, 6 fields,
      unit rank 2) -- a gap of 0.65 where P5 allowed 0.25. The mean L_1
      behind it is 14.3 against 47.3. The gap read 1.54 before the
      cyclic correction of explore_cubic_class_map.py F4, which raises
      the real prediction from 17.5 to 25.9: the KILL survives the
      correction and its SIZE does not. The direction is that the HIGHER
      unit rank waits LONGER at the same class number, which is the
      opposite of what the floor story would suggest if it were about
      units making generators easier to find, and it is the one
      comparison degree 2 could not stage at all.
      IT IS SIX FIELDS AND THE THINNESS IS THE FINDING'S OWN CAUTION,
      AND IT IS REALLY FOUR: two of the six are CYCLIC, which reads a
      third of the primes rather than two thirds and every one of them
      totally split, so the stratum is two arithmetics under one label
      and the unit-rank reading belongs to the four non-cyclic ones
      (explore_cubic_class_map.py F5).
      Totally real cubic fields with h > 1 are RARE at small
      discriminant -- 9 of 215 here -- so this is a stratum the
      population cannot thicken without a much larger cap, and that, not
      the model, is what the next widening of this front would buy.

  P2 AND P4 ARE NOT RUN, and the reason is the instrument and not the
  budget: both count the primes that do NOT carry a principal degree-1
  place, and the test of derivation (3) is a positive certificate -- a
  search that reaches no generator is silent, not negative. Deciding a
  place NON-principal needs its CLASS, which is the map the local-share
  division needs too and which nothing here builds. So the share by
  prime bin and the index of dispersion -- the mechanism that survived
  at degree 2, and the sharpest reason to lift a degree at all -- stand
  unanswered rather than answered either way, and S4 prints that where
  their tables would have been.

  F5. THE INSTRUMENT'S OWN LESSON: A GENERATOR'S SIZE IS THE UNIT
      GROUP'S, NOT THE LATTICE'S (observation; the miss rates below are
      exhaustive over the 867 certified h = 1 fields, the claim they
      support is not; derivation (3)). The T2-reduced search with a
      coefficient box missed the generator at 11.7% of those fields at
      |d| <= 6000 -- and growing the box is the wrong axis, the miss
      rate at |d| <= 1000 being 0 for the same escalating search. Re-reducing the same
      lattice under a determinant-1 REWEIGHTING of the embeddings, which
      undoes a power of the unit, takes the miss rate to 0 over the
      whole population at a box of 3, and the escalation is paid only
      where the unweighted reduction failed.
      THE LESSON IS NOT NEW TO THE CORPUS AND THE RECORD SHOULD NOT READ
      AS IF IT WERE: explore_cubic_field_shop.py's non-principality
      certificate already bounds its box by the fundamental unit's real
      embedding, which is the same fact in the same place. What is new
      here is the shape the fact takes when the search must run at
      population scale and at BOTH signatures: that route finds a unit
      first and derives bounds from it, which the shop implements for
      unit rank 1 and declines for rank 2, while sweeping the unit
      DIRECTION never computes a unit at all and does not care what the
      rank is beyond the dimension of the grid.
      WHAT THE PIN DOES NOT REACH is the 236 fields with h > 1, where no
      identity is available to check L_1 against. The argument that they
      are the EASIER case rather than the unchecked one is the class
      number formula: h times the regulator scales with the square root
      of the discriminant, so at a fixed |d| a larger class number means
      a SMALLER regulator, a less spread unit orbit and a generator the
      search reaches sooner. The pin sits at h = 1, which is the
      conservative end of that, and the argument is an argument and not
      a measurement. The pin is what found this:
      a control on a stratum where the answer is an identity prices the
      instrument in a way no amount of reading the outputs would.

  F6. THE CHEAP ROUTE TO THE MISSING HALF IS A WALL, TIMED AND NOT
      ASSUMED (measurement, taken after the run above and not part of
      it). What the positive certificate cannot do,
      explore_cubic_field_shop.py's non_principality_certificate can at
      unit rank 1: it EXHAUSTS a unit-reduced box and so decides a
      complex field's place NEGATIVELY with no class group. Timed over
      86 places of 20 complex fields at |d| <= 2000 over the first eight
      odd primes, it costs 0.184 s a place, worst 0.826 s, median 8010
      elements exhausted and 194202 at the worst. Its box scales with
      the target NORM, so a place over p ~ 100 costs many times one over
      p ~ 3, and the complex side of this population alone carries on
      the order of 10^5 degree-1 places. That is hours at the sweep cap
      and it is a WALL rather than a budget question. What it IS good
      for is the use the timing leaves open: a VALIDATOR, spot-checking
      a class-group map's negative verdicts on the sample where both
      instruments run. So the map is the route and this is how its price
      gets measured rather than argued.

RUN RECORD. `python prime/code/memwatch.py python
prime/code/explore_cubic_principal.py`. One process, CPython, no BLAS.
17 checks, 242.3 s wall, peak working set 77.6 MB against memwatch's 512
MB ceiling. Enumeration: 15370 polynomials -> 829 reducible, 10350 over
cap, 4191 kept -> 1103 fields (888 complex, 215 totally real, 12
cyclic), least discriminants -23 and 49, 7.6 s. Class numbers: 867
certified 1 constructively, the rest by the relation reading, none
unresolved, none above 8; the first h > 1 field in |d| order is d = -283
with h = 2, the shop's own certified winner. Controls: 5515 cross-engine
place-count pairs with 0 mismatches, 172405 degree-1 places whose index
is p with 0 mismatches, 6605 generators certified with 0 re-check
mismatches, 0 L_1 and 0 model mismatches over the 867-field identity
pin. Three earlier runs are in the repository history and
none of their tables are quoted here: the first was stopped by the
shop's own sieve assert at the widened discriminant cap, the second and
third by the pin at 101 and then 2 mismatches, which is the sequence F5
records.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from math import acos, cos, pi, sqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_field_shop as CFS
import explore_cubic_ring as CR

CHECKS = 0

DISC_CAP = 6000          # |d_K| ceiling for the population
PRIME_CAP = 1000         # odd primes the sweep reads
BANDS = (10, 25, 50, 100, 250, 1000)
BIN_EDGES = (3, 30, 100, 300, 1000)   # prime bins, frozen: the census
                                      # reads them, the unrun share would have
GEN_BOX = 3              # coefficient box in the reduced basis
GEN_LEVELS = (0, 1, 2, 3)  # escalating unit-direction weight grids
MIN_STRATUM = 5          # a stratum smaller than this is printed, never read
XCHECK_PER_FIELD = 5     # C4a: cross-engine samples per field ...
XCHECK_PRIME_CAP = 50    # ... at primes below this, where both routes run

ODD_PRIMES = [p for p in CR._sieve(PRIME_CAP) if p != 2]


MAX_SIEVE = CR._sieve(1000)      # index primes: p^2 | disc needs p <= 1000


def maximal_order3(a, b, c):
    """The maximal order of Q[t]/(t^3 + a t^2 + b t + c) and d_K. The
    shop's own routine sieves index primes out of a list capped at 300
    and asserts |disc| < 90000 rather than reading a wrong answer; the
    Hunter box at this file's discriminant cap carries polynomial
    discriminants past that, so the sieve is widened here. A prime with
    p^2 | disc and p > 1000 would need |disc| > 10^6, which the assert
    forbids."""
    R = (-c, -b, -a)
    trvec = (3, -a, a * a - 2 * b)
    O = CFS.Order(R, trvec, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    d0 = O.trace_form_disc()
    assert abs(d0) < 10 ** 6, "polynomial discriminant out of sieve range"
    for p in MAX_SIEVE:
        if p * p > abs(d0):
            break
        if d0 % (p * p) == 0:
            O = CFS.p_maximalize(O, p)
    return O, O.trace_form_disc()


def enumerate_fields(cap):
    """Hunter's box to |d_K| <= cap, fields keyed by discriminant and
    separated inside a discriminant by their splitting fingerprint. The
    shop's own enumeration with the widened maximal order and a
    dictionary in place of its linear scan over records."""
    t2max, s2max, s3max = CFS.hunter_box(cap)
    del t2max
    n_poly = n_red = n_over = n_kept = 0
    by_d = {}
    for s1 in (0, 1):
        for s2 in range(-s2max, s2max + 1):
            for s3 in range(-s3max, s3max + 1):
                n_poly += 1
                a, b, c = -s1, s2, -s3
                if not CFS.is_irreducible_cubic(a, b, c):
                    n_red += 1
                    continue
                O, d = maximal_order3(a, b, c)
                if abs(d) > cap:
                    n_over += 1
                    continue
                n_kept += 1
                pd = CFS.poly_disc3(a, b, c)
                fp = dict((p, CFS.shape_at(a, b, c, p))
                          for p in CFS.SMALL_PRIMES if pd % p)
                home = None
                for rec in by_d.setdefault(d, []):
                    if all(fp[p] == rec[0][p] for p in fp if p in rec[0]):
                        home = rec
                        break
                if home is None:
                    by_d[d].append((fp, [(a, b, c, O)]))
                else:
                    home[0].update(fp)
                    home[1].append((a, b, c, O))
    out = [(abs(d), d, d < 0, polys)
           for d in by_d for (fp, polys) in by_d[d]]
    out.sort(key=lambda t: (t[0], t[1]))
    return out, (n_poly, n_red, n_over, n_kept)


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg


def section(t):
    print("\n" + "=" * 68)
    print(t)
    print("=" * 68)


# ------------------------------------------------------------- embeddings
def cubic_roots(a, b, c):
    """Roots of x^3 + a x^2 + b x + c as (real_roots, complex_pair|None)."""
    p = b - a * a / 3.0
    q = 2.0 * a ** 3 / 27.0 - a * b / 3.0 + c
    if -(4.0 * p ** 3 + 27.0 * q * q) > 0.0:          # three real roots
        m = 2.0 * sqrt(-p / 3.0)
        arg = 3.0 * q / (p * m)
        arg = max(-1.0, min(1.0, arg))
        th = acos(arg) / 3.0
        return [m * cos(th - 2.0 * pi * k / 3.0) - a / 3.0
                for k in range(3)], None
    r = CFS.real_root_cubic(a, b, c)
    q1 = a + r
    q0 = b + r * q1
    im2 = q0 - q1 * q1 / 4.0
    return [r], (-q1 / 2.0, sqrt(max(im2, 0.0)))


def t2_rows(O, a, b, c):
    """Rows M with T2(v) = |M v|^2 for v in the order's own coordinates."""
    rs, cp = cubic_roots(a, b, c)
    cols = []
    for bv in O.basis:
        t = [float(x) for x in bv]
        col = [t[0] + t[1] * r + t[2] * r * r for r in rs]
        if cp is not None:
            zr, zi = cp
            re = t[0] + t[1] * zr + t[2] * (zr * zr - zi * zi)
            im = t[1] * zi + t[2] * (2.0 * zr * zi)
            col.append(sqrt(2.0) * re)
            col.append(sqrt(2.0) * im)
        cols.append(col)
    return [[cols[j][i] for j in range(3)] for i in range(len(cols[0]))]


# -------------------------------------------------------------------- LLL
def lll_reduce(vecs, U):
    """LLL with delta = 3/4 on float vectors, carrying the integer
    transform U alongside. Float only decides the ORDER of the search;
    every hit is confirmed by an exact integer norm."""
    n = len(vecs)
    B = [list(v) for v in vecs]
    U = [list(u) for u in U]

    def gso():
        Bs, mu = [], [[0.0] * n for _ in range(n)]
        for i in range(n):
            v = list(B[i])
            for j in range(i):
                d = sum(x * x for x in Bs[j])
                m = (sum(B[i][k] * Bs[j][k]
                         for k in range(len(v))) / d) if d else 0.0
                mu[i][j] = m
                v = [x - m * y for x, y in zip(v, Bs[j])]
            Bs.append(v)
        return Bs, mu

    k, guard = 1, 0
    while k < n and guard < 400:
        guard += 1
        Bs, mu = gso()
        for j in range(k - 1, -1, -1):
            r = int(round(mu[k][j]))
            if r:
                B[k] = [x - r * y for x, y in zip(B[k], B[j])]
                U[k] = [x - r * y for x, y in zip(U[k], U[j])]
                Bs, mu = gso()
        if sum(x * x for x in Bs[k]) >= ((0.75 - mu[k][k - 1] ** 2)
                                         * sum(x * x for x in Bs[k - 1])):
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            U[k], U[k - 1] = U[k - 1], U[k]
            k = max(k - 1, 1)
    return U


def reduced_basis(O, P, rows):
    """P's basis, LLL-reduced against T2, in the order's coordinates."""
    vecs = [[sum(rows[i][j] * P[r][j] for j in range(3))
             for i in range(len(rows))] for r in range(3)]
    U = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    U = lll_reduce(vecs, U)
    return [tuple(sum(U[i][k] * P[k][j] for k in range(3)) for j in range(3))
            for i in range(3)]


GEN_STATS = [0, 0]        # generators certified, lattice re-check mismatches
ENGINE_STATS = [0, 0]     # cross-engine pairs sampled, place-count mismatches
PLACE_STATS = [0, 0]      # degree-1 places checked, index-not-p mismatches


def det3_int(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def norm_form(O, red):
    """The norm as a ternary cubic FORM in the reduced basis's own
    coordinates -- det(x M0 + y M1 + z M2), expanded once per place. The
    search then costs a handful of integer multiplies per candidate
    instead of a 3x3 determinant built from three ring multiplications."""
    mats = []
    for u in red:
        mats.append([O.mul(u, tuple(1 if j == i else 0 for j in range(3)))
                     for i in range(3)])
    coef = {}
    perms = (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
             ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1))
    for sigma, sign in perms:
        # the three linear forms L_r = sum_t mats[t][r][sigma[r]] * var_t
        terms = [tuple(mats[t][r][sigma[r]] for t in range(3))
                 for r in range(3)]
        for i in range(3):
            if not terms[0][i]:
                continue
            for j in range(3):
                if not terms[1][j]:
                    continue
                for k in range(3):
                    if not terms[2][k]:
                        continue
                    key = [0, 0, 0]
                    key[i] += 1
                    key[j] += 1
                    key[k] += 1
                    c = sign * terms[0][i] * terms[1][j] * terms[2][k]
                    key = tuple(key)
                    coef[key] = coef.get(key, 0) + c
    return dict((k, v) for k, v in coef.items() if v)


def weight_grid(cx, level):
    """Weightings of the embeddings, of determinant 1, sweeping the UNIT
    direction. A generator's size is set by the unit group and not by T2:
    the minimal-T2 element of a principal place need not be a generator,
    because a larger-norm element can be shorter than the best-balanced
    generator when the fundamental unit is large. So the search does not
    grow the box -- it re-reduces the same lattice under a weighted T2
    whose weighting undoes a power of the unit, and every generator
    becomes near-minimal under one of them. Complex cubics have one unit
    direction (real embedding against the complex pair), totally real
    ones have two, which is why the real grid is square."""
    if level == 0:
        return [(1.0, 1.0, 1.0)]
    T, step = {1: (2.0, 1.0), 2: (6.0, 1.0), 3: (12.0, 0.5)}[level]
    ts = []
    t = -T
    while t <= T + 1e-9:
        ts.append(t)
        t += step
    out = []
    if cx:
        for t in ts:
            e = 2.718281828459045
            out.append((e ** (2.0 * t), e ** (-t), e ** (-t)))
    else:
        for t1 in ts:
            for t2 in ts:
                e = 2.718281828459045
                out.append((e ** t1, e ** t2, e ** (-t1 - t2)))
    return out


def find_gen(O, P, rows, target, cx, box=GEN_BOX, levels=GEN_LEVELS):
    """An element of P of |norm| = target, or None -- a POSITIVE
    certificate only: None means the search did not reach one, never that
    none exists. The grid escalates so the common case stays cheap. Every
    hit is re-checked in the lattice and by the order's own norm (C5)."""
    for level in levels:
        for w in weight_grid(cx, level):
            wrows = [[w[i] * rows[i][j] for j in range(3)]
                     for i in range(len(rows))]
            red = reduced_basis(O, P, wrows)
            form = norm_form(O, red)
            for x in range(-box, box + 1):
                xp = (1, x, x * x, x ** 3)
                for y in range(-box, box + 1):
                    yp = (1, y, y * y, y ** 3)
                    A = [0, 0, 0, 0]
                    for (i, j, k), c in form.items():
                        A[k] += c * xp[i] * yp[j]
                    for z in range(-box, box + 1):
                        if x == 0 and y == 0 and z == 0:
                            continue
                        N = ((A[3] * z + A[2]) * z + A[1]) * z + A[0]
                        if N != target and N != -target:
                            continue
                        v = tuple(x * red[0][t] + y * red[1][t]
                                  + z * red[2][t] for t in range(3))
                        GEN_STATS[0] += 1
                        if (abs(O.norm(v)) != target
                                or not CFS.in_lattice(v, P, 3)):
                            GEN_STATS[1] += 1
                        return v
    return None


# ------------------------------------------------------------ class number
def class_reading(O, d, cx, rows):
    """(h, kind): 'cert' when every Minkowski place is found principal,
    'H' for the relation reading, None when the relations are rank
    deficient."""
    mb = CFS.minkowski_bound(d, O.n, cx)
    small = [t for t in CFS.all_places_upto_prime(O, mb)
             if t[0] ** t[2] <= mb]
    if all(find_gen(O, P, rows, p ** f, cx) is not None
           for (p, e, f, name, P) in small):
        return 1, 'cert'
    H = CFS.relation_H(O)
    if H is None:
        return None, None
    return H, ('cert' if H == 1 else 'H')


# -------------------------------------------------------- places and types
def deg1_places(O, a, b, c, pdisc, p):
    """Degree-1 places over an odd prime p, and the splitting type. Off
    the polynomial discriminant Z[theta] is p-maximal and the linear
    factors of the defining polynomial mod p name the places; on it the
    algebra O/pO is decomposed instead."""
    if pdisc % p:
        rts = [r for r in range(p) if (((r + a) * r + b) * r + c) % p == 0]
        assert len(rts) in (0, 1, 3), \
            "cubic with %d roots mod %d off its discriminant" % (len(rts), p)
        out = []
        for r in rts:
            gens = [tuple(p if j == i else 0 for j in range(3))
                    for i in range(3)]
            el = O.coords_of((-r, 1, 0))
            for i in range(3):
                gens.append(O.mul(el, tuple(1 if j == i else 0
                                            for j in range(3))))
            out.append(CFS.hnf_red(gens, 3))
        return out, ('split' if len(rts) == 3
                     else 'partial' if len(rts) == 1 else 'inert')
    pl = CFS.maximal_places(O, p)
    if any(e > 1 for (P, e, f) in pl):
        return None, 'ramified'
    out = [P for (P, e, f) in pl if f == 1]
    return out, ('split' if len(pl) == 3
                 else 'partial' if len(pl) == 2 else 'inert')


def q_nominal(kind, h):
    if kind == 'split':
        return 1.0 - (h - 1) * (h - 2) / float(h * h)
    if kind == 'partial':
        return 1.0 / h
    return 0.0


# ------------------------------------------------------------ per-field run
def sweep_field(O, a, b, c, h, cx):
    """Walk the odd unramified primes to the cap. Returns a dict with the
    per-prime record the coverage, share, model and dispersion readings
    all read from."""
    pdisc = CFS.poly_disc3(a, b, c)
    rows = t2_rows(O, a, b, c)
    seq = []                 # (p, kind, q) over degree-1-carrying primes
    inert = []               # unramified primes with no degree-1 place
    l1 = None
    checked = 0
    for p in ODD_PRIMES:
        places, kind = deg1_places(O, a, b, c, pdisc, p)
        if checked < XCHECK_PER_FIELD and p < XCHECK_PRIME_CAP and pdisc % p:
            checked += 1
            ENGINE_STATS[0] += 1
            alg = [P for (P, e, f) in CFS.maximal_places(O, p) if f == 1]
            if len(alg) != len(places):
                ENGINE_STATS[1] += 1
        if kind == 'ramified':
            continue
        if kind == 'inert':
            inert.append(p)
            continue
        for P in places:
            PLACE_STATS[0] += 1
            if abs(det3_int(P)) != p:
                PLACE_STATS[1] += 1
        seq.append((p, kind, q_nominal(kind, h)))
        if l1 is None and any(find_gen(O, P, rows, p, cx) is not None
                              for P in places):
            l1 = p
    return {'l1': l1, 'seq': seq, 'inert_primes': inert}


def model_mean(seq, cap):
    """Predicted mean L_1 and mass, over the field's own degree-1-carrying
    primes below cap (derivation (5))."""
    surv, mass, tot = 1.0, 0.0, 0.0
    for (p, kind, q) in seq:
        if p > cap:
            break
        pr = surv * q
        tot += p * pr
        mass += pr
        surv *= (1.0 - q)
    return (tot / mass if mass > 0 else None), mass


# ------------------------------------------------------------- S1 controls
def s1_degree2_class_engine():
    section("S1a CONTROL -- the relation class engine at degree 2")
    for (name, a1, a0, want) in CFS.QUAD_CONTROLS:
        O = CFS.Order((-a0, -a1), (2, -a1), [(1, 0), (0, 1)])
        H = CFS.relation_H(O)
        print("  %-12s d = %-5d H = %s (filed h = %d)"
              % (name, O.trace_form_disc(), H, want))
        ok(H == want, "%s: relation reading %s, filed %d" % (name, H, want))


def s1_enumeration():
    section("S1b CONTROL -- Hunter enumeration to |d_K| <= %d" % DISC_CAP)
    t0 = time.time()
    fields, buckets = enumerate_fields(DISC_CAP)
    n_poly, n_red, n_over, n_kept = buckets
    print("  %d polynomials: %d reducible, %d over cap, %d kept -> %d fields"
          % (n_poly, n_red, n_over, n_kept, len(fields)))
    ok(n_red + n_over + n_kept == n_poly, "bucket counts do not sum")
    nc = sum(1 for f in fields if f[2])
    print("  %d complex (unit rank 1), %d totally real (unit rank 2)"
          % (nc, len(fields) - nc))
    first_c = next(f for f in fields if f[2])
    first_r = next(f for f in fields if not f[2])
    print("  least |d| complex %d, least totally real %d, %.1f s"
          % (first_c[1], first_r[1], time.time() - t0))
    ok(first_c[1] == -23, "least complex cubic disc %d" % first_c[1])
    ok(first_r[1] == 49, "least totally real cubic disc %d" % first_r[1])
    return fields


def s1_census_and_pin(recs):
    section("S1d CONTROL -- the two place engines, the census by bin, "
            "and the h = 1 identity pin")
    print("  [C4a] cross-engine degree-1 place count: %d pairs sampled, "
          "%d mismatches" % (ENGINE_STATS[0], ENGINE_STATS[1]))
    ok(ENGINE_STATS[1] == 0,
       "%d cross-engine place-count mismatches" % ENGINE_STATS[1])
    print("  [C6]  degree-1 place index against p: %d places checked, "
          "%d mismatches" % (PLACE_STATS[0], PLACE_STATS[1]))
    ok(PLACE_STATS[1] == 0,
       "%d degree-1 places whose index is not p" % PLACE_STATS[1])

    edges = list(BIN_EDGES)
    for cyc, want in ((False, (1 / 6.0, 0.5, 1 / 3.0)),
                      (True, (1 / 3.0, 0.0, 2 / 3.0))):
        lab = "cyclic" if cyc else "non-cyclic"
        st = [r for r in recs if r['cyclic'] == cyc]
        if not st:
            continue
        print("  [C4b] %s: nominal split %.4f partial %.4f inert %.4f"
              % (lab, want[0], want[1], want[2]))
        rowvals = []
        for i in range(len(edges) - 1):
            tot = {'split': 0, 'partial': 0, 'inert': 0}
            for r in st:
                for (p, kind, q) in r['seq']:
                    if edges[i] <= p < edges[i + 1]:
                        tot[kind] += 1
                for p in r['inert_primes']:
                    if edges[i] <= p < edges[i + 1]:
                        tot['inert'] += 1
            n = sum(tot.values())
            if not n:
                continue
            got = tuple(tot[k] / float(n)
                        for k in ('split', 'partial', 'inert'))
            rowvals.append(got)
            print("         %5d-%-5d n = %6d  split %.4f  partial %.4f  "
                  "inert %.4f" % (edges[i], edges[i + 1], n,
                                  got[0], got[1], got[2]))
        tv = [0.5 * sum(abs(g - w) for g, w in zip(row, want))
              for row in rowvals]
        print("         total variation from nominal, bottom bin %.4f "
              "-> top bin %.4f" % (tv[0], tv[-1]))
        ok(tv[-1] < tv[0], "%s census no nearer nominal in the top bin "
                           "(%.4f against %.4f)" % (lab, tv[-1], tv[0]))
        if not cyc:
            for j in range(3):
                ok(abs(rowvals[-1][j] - want[j]) <= 0.02,
                   "non-cyclic top bin off nominal by %.4f"
                   % abs(rowvals[-1][j] - want[j]))

    pin = [r for r in recs if r['kind'] == 'cert']
    bad_l1 = bad_model = 0
    for r in pin:
        least = r['seq'][0][0] if r['seq'] else None
        if r['l1'] != least:
            bad_l1 += 1
            if bad_l1 <= 5:
                print("  PIN MISS d = %d: L_1 = %s, least carrier = %s"
                      % (r['d'], r['l1'], least))
        pred, _ = model_mean(r['seq'], PRIME_CAP)
        if r['l1'] is not None and pred is not None \
                and abs(pred - r['l1']) > 1e-9:
            bad_model += 1
    print("  %d fields with h certified 1: %d L_1 mismatches, "
          "%d model mismatches" % (len(pin), bad_l1, bad_model))
    print("  %d generators certified, %d re-check mismatches"
          % (GEN_STATS[0], GEN_STATS[1]))
    ok(bad_l1 == 0, "%d certified-h=1 fields where L_1 is not the least "
                    "degree-1 carrier" % bad_l1)
    ok(bad_model == 0, "%d certified-h=1 fields where the model misses the "
                       "identity" % bad_model)
    ok(GEN_STATS[1] == 0, "%d generator re-check mismatches" % GEN_STATS[1])


# ------------------------------------------------------------ the readings
def s2_population(recs):
    section("S2  THE POPULATION -- fields by signature and class number")
    print("  %-16s %s" % ("class number", "  ".join("%5d" % h
                                                    for h in range(1, 9))))
    for cx, lab in ((True, "complex  rank 1"), (False, "real     rank 2")):
        row = []
        for h in range(1, 9):
            row.append(sum(1 for r in recs
                           if r['cx'] == cx and r['h'] == h))
        print("  %-16s %s" % (lab, "  ".join("%5d" % n for n in row)))
    big = sorted(set(r['h'] for r in recs if r['h'] and r['h'] > 8))
    print("  beyond 8: %s   unresolved: %d"
          % (big if big else "none",
             sum(1 for r in recs if r['h'] is None)))
    cyc = sum(1 for r in recs if r['cyclic'])
    print("  cyclic (square discriminant): %d of %d" % (cyc, len(recs)))


def s3_coverage(recs):
    section("S3  COVERAGE -- fields with L_1 at or below the sweep bound")
    print("  %-22s %5s  %s" % ("stratum", "n",
                               "  ".join("%6d" % b for b in BANDS)))
    for cx, lab in ((True, "complex"), (False, "real")):
        for h in sorted(set(r['h'] for r in recs
                            if r['h'] is not None and r['cx'] == cx)):
            st = [r for r in recs if r['cx'] == cx and r['h'] == h]
            cov = ["%6.1f" % (100.0 * sum(1 for r in st
                                          if r['l1'] is not None
                                          and r['l1'] <= b) / len(st))
                   for b in BANDS]
            mark = "" if len(st) >= MIN_STRATUM else "  (thin)"
            print("  %-22s %5d  %s%s"
                  % ("%s h = %d" % (lab, h), len(st), "  ".join(cov), mark))
    for cx, lab in ((True, "complex"), (False, "real")):
        st = [r for r in recs if r['cx'] == cx]
        cov = ["%6.1f" % (100.0 * sum(1 for r in st if r['l1'] is not None
                                      and r['l1'] <= b) / len(st))
               for b in BANDS]
        print("  %-22s %5d  %s" % ("ALL %s" % lab, len(st), "  ".join(cov)))


def s4_model(recs):
    section("S4  THE FIRST-HIT MODEL AT THE NOMINAL DENSITY")
    print("  %-22s %5s %9s %9s %7s %7s"
          % ("stratum", "n", "measured", "predicted", "ratio", "mass"))
    for cx, lab in ((True, "complex"), (False, "real")):
        for h in sorted(set(r['h'] for r in recs
                            if r['h'] is not None and r['cx'] == cx)):
            st = [r for r in recs if r['cx'] == cx and r['h'] == h]
            meas, pred, mass, n = 0.0, 0.0, 0.0, 0
            for r in st:
                pm, m = model_mean(r['seq'], PRIME_CAP)
                if r['l1'] is None or pm is None:
                    continue
                meas += r['l1']
                pred += pm
                mass += m
                n += 1
            if not n:
                continue
            mark = "" if len(st) >= MIN_STRATUM else "  (thin)"
            print("  %-22s %5d %9.1f %9.1f %7.3f %7.3f%s"
                  % ("%s h = %d" % (lab, h), n, meas / n, pred / n,
                     (meas / pred) if pred else float('nan'), mass / n,
                     mark))
    drop = sum(1 for r in recs if r['l1'] is None)
    print("  fields with no certified principal degree-1 place below %d: "
          "%d of %d" % (PRIME_CAP, drop, len(recs)))
    print("\n  P2 (the share by prime bin) and P4 (the index of dispersion)"
          " are NOT RUN,")
    print("  and the reason is the instrument rather than the budget: both"
          " count the")
    print("  primes that do NOT carry a principal degree-1 place, and this"
          " rig's test")
    print("  is a positive certificate -- a box that reaches no generator"
          " is silent,")
    print("  not negative. Deciding a place NON-principal needs the class"
          " of that")
    print("  place, which is the class-group map the local-share division"
          " needs too.")
    print("  One cheaper route exists on half the population and this rig"
          " does not take")
    print("  it: the shop's non-principality certificate is EXHAUSTIVE at"
          " unit rank 1,")
    print("  so on the %d complex fields a place can be decided negatively"
          " with no" % sum(1 for r in recs if r['cx']))
    print("  class group. It is declined here because a statistic read on"
          " the complex")
    print("  side alone cannot be compared to one read on both, and the"
          " totally real")
    print("  side is where the signature question lives.")


# -------------------------------------------------------------------- main
def main():
    t0 = time.time()
    s1_degree2_class_engine()
    fields = s1_enumeration()

    section("S1c THE SWEEP -- class reading and L_1 per field")
    recs = []
    first_big = None
    for i, (ad, d, cx, polys) in enumerate(fields):
        a, b, c, O = polys[0]
        rows = t2_rows(O, a, b, c)
        h, kind = class_reading(O, d, cx, rows)
        rec = sweep_field(O, a, b, c, h if h else 1, cx)
        rec.update({'d': d, 'cx': cx, 'h': h, 'kind': kind,
                    'cyclic': int(round(sqrt(ad))) ** 2 == ad and d > 0})
        recs.append(rec)
        if h is not None and h > 1 and first_big is None:
            first_big = (d, h)
        if (i + 1) % 200 == 0:
            print("  %4d/%d fields, %.1f s" % (i + 1, len(fields),
                                               time.time() - t0))
    print("  %d fields swept, %.1f s" % (len(recs), time.time() - t0))
    print("  first field with h > 1 in |d| order: d = %d, h = %d"
          % first_big)
    ok(first_big == (-283, 2), "first h > 1 cubic field is %s, not (-283, 2)"
       % (first_big,))

    s1_census_and_pin(recs)
    s2_population(recs)
    s3_coverage(recs)
    s4_model(recs)

    section("SUMMARY")
    print("  %d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
