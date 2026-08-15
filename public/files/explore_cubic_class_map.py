r"""DOES THE MECHANISM THAT SURVIVED AT DEGREE 2 -- A PRINCIPAL SHARE SHORT
AT SMALL p AND A COUNT UNDER-DISPERSED AGAINST ITS OWN DENSITY --
REPRODUCE AT DEGREE 3? -- the two statistics explore_cubic_principal.py
could not read, bought by placing a degree-1 place in the class group
instead of exhibiting a generator for it.

THE QUESTION, AND WHY IT NEEDED A NEW INSTRUMENT. Over cubic fields the
coverage question is answered: every one of 1103 fields to |d_K| <= 6000
has a principal degree-1 place below 1000, at both signatures and at
every class number through 8, and the first-hit model at the nominal
Chebotarev density arrives early by 1.17x to 3.21x above h = 1
(explore_cubic_principal.py F1-F2). What is NOT answered there is the
pair of statistics that carried the mechanism at degree 2: the SHARE of
degree-1-carrying primes whose place is principal, read by prime bin,
and the INDEX OF DISPERSION of the per-field count of such primes. Both
COUNT the places that are not principal, and the rig's test -- exhibit
an element of the place with norm exactly p -- is a POSITIVE certificate:
a search that reaches none is silent, not negative. So both stood unrun.

The cheap route to the negative half was timed rather than assumed and
is a wall: explore_cubic_field_shop.py's non_principality_certificate
EXHAUSTS a unit-reduced box and so decides a complex field's place
negatively with no class group at all, at 0.184 s a place over the first
eight odd primes, with a box that scales with the target norm -- hours
at this population's ~10^5 degree-1 places (explore_cubic_principal.py
F6). This file takes the other route: build the map from a place to its
CLASS, which decides both directions at once, and demote the exhaustive
certificate to what the timing leaves it good for -- an independent
VALIDATOR of the map's negative verdicts on a sample where both run.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The suspicion
is imported from degree 2, where it is written in the vocabulary of a
SPLIT PRIME and its one place. Here the object is a PLACE and its residue
degree, and the statistic's unit is a PRIME: the share asks what fraction
of the primes that carry a degree-1 place at all carry a PRINCIPAL one,
which is the quantity the nominal q of the parent rig's derivation (2)
predicts -- q_split and q_partial are both probabilities that AT LEAST
ONE degree-1 place over p is principal. So the per-prime reading is not a
convenience; it is what makes the measured number and the modelled number
the same quantity.

THE SECOND VOCABULARY QUESTION, and it is the one that decides the whole
design: PRINCIPAL is a property of a place, but NON-PRINCIPAL, as this
file can know it, is a property of a place AND A LATTICE. The map places
P by writing its class in terms of a fixed generating set and reducing
against the relations known for that set. Triviality is a PROOF of
principality; non-triviality is a proof of non-principality only once the
relation lattice is SATURATED -- equal to the full kernel, not merely
contained in it. Every verdict below therefore carries which of the two
it is, and the saturation gap is priced (C3) rather than argued.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM DEGREE 2 TO DEGREE 3: the SHAPE of P1 and P2 below -- share
    short at the bottom and climbing, count under-dispersed -- is
    imported wholesale from explore_paired_division.py's quadratic
    measurements and is exactly what is under test.

 T2 FROM THE PARENT RIG: the enumeration, the maximal order, the place
    engines, the T2 rows, the LLL, the norm form, the unit-direction
    weight grids and the class reading are explore_cubic_principal.py's,
    imported rather than re-implemented; the relation harvest, the
    Hermite order, the ideal lattice tools and the exhaustive
    non-principality certificate are explore_cubic_field_shop.py's. The
    shop's FINGERPRINT ASSUMPTION rides in with the enumeration and is
    carried unexamined, as it was there: two non-isomorphic fields of one
    discriminant agreeing at every splitting shape to 300 would be
    counted once, which is a population one field short and not a wrong
    reading at any field.
    AND ONE CONTROL IS INHERITED RATHER THAN RE-RUN, which is worth naming
    because it is the one the map rests on: everything here assumes a
    degree-1 place has index exactly p in the order, since that is what
    makes an element of P with the right norm generate P rather than merely
    lie in it. explore_cubic_principal.py checks it at 172405 places with
    0 mismatches, on the same place engines this file imports, and it is
    not recomputed here. The map adds its own downstream guards -- the norm
    accounting and the lattice re-check of C2 -- but neither of those tests
    the place, so if that inherited control were ever narrowed the reading
    here would go with it.

 T3 FROM THE PARENT'S OWN CAUTION: the class number used to stratify is
    H, the relation reading, which the true h DIVIDES. A field where the
    two differ is misfiled into a neighbouring stratum. This file lowers
    H wherever its own machinery finds relations the harvest missed
    (derivation (4)), so its H is nearer the truth than the parent's, and
    the two are printed against each other rather than assumed equal.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE MAP. Fix the generating set G = the places of norm at most 30
      over the primes at most 29 -- the shop's own relation generators,
      which contains every place under any Minkowski bound in this range
      and so generates the class group. Let L be the lattice of known
      relations inside Z^G: each row is the valuation vector of a
      PRINCIPAL element whose divisor is supported on G. Then Z^G / L
      surjects onto the class group, with equality exactly when L is the
      full kernel.

      To place a degree-1 place P over an odd unramified p, find an
      element alpha of P whose norm is p times a cofactor supported on
      G's primes. Then (alpha) = P * prod Q_i^{a_i} with Q_i in G, so
      [P] = -sum a_i [Q_i], and P is principal if the vector a lies in L.
      The vector a is what the map returns.

      TWO CASES, AND THE CHEAP ONE IS HALF THE RANGE. If p <= 29 then P
      is ITSELF a member of G -- every degree-1 place there has norm
      p <= 30 -- and the map is the membership test e_P in L, with no
      search at all. The bottom prime bin is therefore free, and only
      p > 29 pays for a search.

  (2) THE SEARCH FOR ALPHA, WHICH IS THE PARENT'S SEARCH AT A WIDER
      TARGET. The parent enumerates a coefficient box in a T2-LLL-reduced
      basis of P and accepts |N| = p exactly, escalating through
      determinant-1 reweightings of the embeddings when the unweighted
      reduction fails -- because a generator's size is set by the unit
      group and not by the lattice (explore_cubic_principal.py F5). The
      map enumerates THE SAME BOX and accepts a strictly wider target:
      |N| = p * m with p not dividing m and m supported on G's primes.
      So the map's acceptance set CONTAINS the generator search's, every
      place the parent decided principal the map decides principal, and
      the escalation is paid far less often because any smooth hit will
      do rather than one exact one.
      REQUIRING p TO NOT DIVIDE m IS WHAT MAKES v_P(alpha) = 1 FREE: the
      p-part of the norm is then p^1, P has residue degree 1, and no
      other place over p can divide alpha. The valuation is read off the
      norm rather than computed.
      2 IS AN ALLOWED COFACTOR PRIME. The exclusion of p = 2 in this
      corpus is an exclusion from L_1's own prime range (the budget
      inequality owns p = 2); it says nothing about which places a
      relation may be supported on, and the places over 2 have norm at
      most 8 and sit in G.

  (3) THE COFACTOR IS VERIFIED BY NORM ACCOUNTING, NOT BY FACTORING. For
      each prime q dividing m, the valuations of alpha at G's places over
      q are computed and sum(val * f) is compared to v_q(m). Equality
      means the whole q-part of (alpha) is supported on G; inequality
      means some place over q is missing from G -- q inert of norm above
      30, say -- and the hit is REJECTED rather than mis-recorded. This
      is the shop's own harvest checksum, applied to one element at a
      time.

  (4) WHERE THE MISSING RELATIONS COME FROM, WHICH IS THE SATURATION
      LEVER AND IT IS FREE. The harvest gets L by sweeping a coefficient
      box in the ORDER and keeping the smooth principal elements. The map
      sweeps a box in EVERY PLACE, so it sees elements the harvest never
      reaches, and two of its by-products are relations:

        two hits alpha, alpha' at the SAME place P give
        [P] = -a.[Q] = -a'.[Q], so a - a' is a relation -- whatever P is,
        and whether or not P lies in G, and without either hit being
        known principal.

      That is the whole lever and it is the reason the map keeps more
      than one hit per place. It is adjoined before any verdict is read,
      so a place's verdict is taken against the largest lattice this rig
      can build. The resulting order H is a divisor of the parent's H by
      construction -- L only grows -- and the two are printed against
      each other, the drop being the amount of the parent's
      non-principality that was the harvest's blind spot rather than the
      arithmetic.
      THE OTHER SOURCE IS THE HARVEST'S OWN AND IS NOT DOUBLE-COUNTED. A
      hit at a place INSIDE G has its entire divisor on G and its full
      vector is a relation -- but the places inside G take the free
      membership route of (1) and are never searched, so this rig
      contributes none of those. Widening the harvest is the shop's
      escalation, which is used as it stands: where the default box
      leaves Z^G/L infinite the harvest is re-run at the wider box, since
      an infinite-index lattice makes every membership test meaningless
      rather than merely conservative.

  (5) THE TWO STATISTICS, AND WHERE h = 1 IS DEGENERATE. THE SHARE:
      within a prime bin, the fraction of degree-1-carrying primes whose
      degree-1 place is principal, divided by the mean of that prime's
      OWN nominal q -- q_split at a totally split prime, q_partial at a
      partially split one, both functions of h (the parent's derivation
      (2)). Reading each prime against its own type's q is what divides
      the splitting lag OUT: the deficit
      explore_cubic_principal.py F3 measured lives in WHICH primes carry
      a degree-1 place, and the share is conditioned on carrying one.
      The bin's type mix is printed beside the share so that this is
      visible rather than asserted.
      THE DISPERSION: per field, the count of primes below the cap
      carrying a principal degree-1 place. Under the model that count is
      a sum of independent Bernoullis at the field's own q_i, with mean
      sum q_i and variance sum q_i(1-q_i); the index of dispersion is the
      summed squared deviation over the summed variance, 1 under
      independence and below 1 under a more regular arrangement.
      AT h = 1 BOTH ARE DEGENERATE: every q is 1, the share is 1 over 1
      by arithmetic and the dispersion is 0 over 0. So the h = 1 stratum
      is not a measurement here -- it is the PIN (C1), where the map's
      answer is known in advance and any other answer is the instrument.

  (6) THE NOMINAL q IS WRONG AT A CYCLIC FIELD, AND THE CORRECTION IS
      DERIVED. Written after the first recorded run and flagged rather
      than folded away: the run's own diagnostic showed the two cyclic
      fields of the real h = 3 stratum reading 19 principal primes each
      against a predicted 43, where the four non-cyclic fields beside
      them read 36 to 38 against 46 to 49. The ratio is 3/7, and 3/7 is
      exactly (1/3)/(7/9).

      The parent's derivation (2) prices a totally split prime by
      modelling ([P_1], [P_2], [P_3]) as uniform over the h^2 triples
      summing to zero. At a NON-Galois cubic field nothing relates the
      three places and that is a fair model. At a CYCLIC one it is not:
      Gal(K/Q) = <sigma> of order 3 permutes them cyclically, so the
      three classes are c, sigma c, sigma^2 c -- one orbit, not three
      draws. Whether they can differ at all is a question about the
      action of sigma on Cl, and at h = 3 it has one answer: Aut(Z/3)
      has order 2, which has no element of order 3, so sigma acts
      TRIVIALLY and the three classes are EQUAL. The relation
      c + sigma c + sigma^2 c = 0 then reads 3c = 0, which is vacuous in
      Z/3, so c is uniform on all of Cl and

          q_split(cyclic, h = 3) = 1/3 = q_partial,

      against the 7/9 the uniform model gives. A totally split prime in
      a cyclic cubic field of class number 3 is exactly as likely to
      carry a principal place as a partially split one, because it
      carries the SAME class three times.

      This rig uses the corrected q and asserts what its scope is: every
      cyclic field in the population with H > 1 must have H = 3, since
      the derivation is only complete there -- at a class group whose
      automorphism group has order divisible by 3 the action need not be
      trivial and the correction is not derived. A cyclic field with any
      other H > 1 stops the rig rather than being modelled wrongly. S6
      prints the measurement beside both candidate values.

      THE ERROR HAS LINEAGE. explore_cubic_principal.py's derivation (2)
      carries the uncorrected q, its F2 table prices the real h = 3
      stratum with it, and F4 reads the unit-rank separation OFF that
      stratum -- 2 of whose 6 fields are cyclic. The correction raises
      the predicted L_1 there and so LOWERS that ratio; the size of the
      move is S6's to print.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. THE SHARE IS SHORT AT THE BOTTOM AND CLIMBS. At every class number
      at least 2 with at least 5 fields, the measured share divided by
      the mean nominal q is below 1 in the bottom prime bin, and larger
      in the top bin than in the bottom. This is the degree-2 shape:
      0.662 of nominal in 1-1000 against 0.964 in 3000-10000 at class
      number 8 (explore_paired_division.py).

  P2. THE COUNT IS UNDER-DISPERSED. The index of dispersion sits below 1
      at every stratum of at least 5 fields, at both signatures. At
      degree 2, counted to the cap against the field's own local density,
      it came in at 0.142 at h = 2.

  P3. SIGNATURE DOES NOT GRADE EITHER. At a class number carrying at
      least 5 fields on both signatures and above h = 1, the two shares
      in a common bin differ by less than 0.10 and the two indices of
      dispersion by less than 0.25. This is the clause the parent's P5
      could not test -- its ratio clause was KILLED at h = 3, where the
      higher unit rank waited 1.54 longer than P5 allowed
      (explore_cubic_principal.py F4), and the share clause rode on the
      statistic that did not run. This is that statistic.

  P4. THE HARVEST'S BLIND SPOT IS REAL BUT SMALL. The map's relation
      lattice lowers the parent's H at fewer than 10% of the fields with
      H > 1, and at no field certified h = 1.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, read after the
controls and never before.

  K1 kills P1: the printed share table, share over mean nominal q by
     prime bin. A stratum of at least 5 fields whose bottom bin sits at
     or above 1, or whose top bin does not exceed its bottom bin, kills
     it there.

  K2 kills P2: the printed index of dispersion. An index at or above 1
     in a stratum of at least 5 fields kills it there.

  K3 kills P3: the two signature columns at a shared class number above
     1 -- a share gap of 0.10 or more in a common bin, or a dispersion
     gap of 0.25 or more.

  K4 kills P4: the printed count of fields where the map's H is a proper
     divisor of the parent's H, against the count with H > 1; at or
     above 10% kills the first half, and any such field inside the
     certified h = 1 set kills the second.

THE POSITIVE CONTROLS, run and read FIRST.

  K2 AMENDMENT, made after the index came in above 1 on a trial run at
  |d_K| <= 1500 and before the recorded one, and flagged rather than
  folded away. The ported index measures deviation from the MODEL mean,
  so a stratum whose share is short everywhere -- which P1 predicts, and
  which the trial run showed at h = 3, a mean count of 39.8 against a
  predicted 47.2 -- is charged for that shortfall as if it were spread.
  Bias and spread are different claims and the one statistic cannot
  carry both. So the index is printed TWICE: as ported, against the
  model mean, and SAMPLE-CENTRED, against the stratum's own mean count.
  The second removes the level, since under-dispersion is a claim about
  arrangement and not about level; the first is kept because it is the
  quantity degree 2 reported. Where they disagree the gap IS the share
  deficit, and P1's table is where that is read.

  K2 AMENDMENT II, made in the audit of the recorded run and for a
  confound neither of those two removes. Both references take their
  VARIANCE from the nominal q, and P1 shows the nominal q is too high.
  For q below a half, q(1-q) RISES with q, so an inflated q inflates the
  variance denominator and DEFLATES the index toward the very conclusion
  P2 asserts. Centring the mean does not touch that: the level and the
  spread are read off the same wrong q. So a THIRD reference is printed
  and P2 is read on it -- the bin's own measured share taken
  LEAVE-ONE-OUT over the other fields of the stratum, each prime's q
  scaled by it, which is the reference the degree-2 rig used and the only
  one the share deficit cannot leak into. A field is excluded from that
  column where its own bin has no other field to estimate from. All three
  are printed because they disagree, and where they disagree the local
  one is the reading.

  THE STRATIFICATION AMENDMENT, made with (6) and for the same reason,
  and flagged rather than folded away. The slate stratifies by SIGNATURE
  and class number, which is the parent's key and degree 2's habit. It is
  the wrong key at degree 3: a cyclic cubic field reads a THIRD of the
  primes where a non-cyclic one reads two thirds, every prime it reads is
  TOTALLY split where a non-cyclic field's run three to one partial, and
  by (6) its split q is a third rather than seven ninths. Three of the
  model's laws differ, so the label "totally real, h = 3" names two
  populations, and a dispersion read across it measures the GAP between
  them rather than the arrangement inside either -- which is what the
  first recorded run's real h = 3 index was doing. The key is therefore
  signature, GALOIS TYPE and class number, and the cost is that the real
  side thins below the reading threshold, which is a fact about this
  population and not a choice: what it deletes is a comparison that was
  never there. Every stratum is printed either way and the ones under the
  threshold are marked, never dropped silently. This is the BUNDLED
  FACULTIES lens's own third tell -- a claim read at one member of a
  family whose members are classified by something FINER than the label
  the claim wears -- fired on the way past rather than looked for.

  C1. THE h = 1 PIN. At a field with h certified 1 -- every place under
      the Minkowski bound found principal by exhibited generator -- the
      class group is trivial, so the map MUST return principal at every
      degree-1 place, and Z^G/L must have order 1. Printed over a stride
      sample of the certified fields as three counts: fields whose map
      lattice has order above 1, places the map calls non-principal, and
      places the map cannot place at all. The first two must be 0. This
      is the roadmap's pin and it prices the saturation gap where the
      answer is known.

  C2. THE NORM ACCOUNTING AT EVERY ACCEPTED ELEMENT. For every alpha the
      map accepts, the exact integer norm of alpha must equal p times the
      product of the norms of G's places to the recorded exponents, and
      alpha must lie in the place's lattice. Printed as a count accepted
      and a mismatch count, which must be 0. A float reduction can lose a
      hit; it cannot manufacture one past this.

  C3. THE INDEPENDENT NEGATIVE, WHICH PRICES THE SATURATION GAP. On a
      sample of places the map calls NON-principal, at complex fields
      where the shop's exhaustive certificate runs at unit rank 1, that
      certificate is run: it must agree that no generator exists.
      Printed as a count checked and a count where the certificate found
      a generator the map had ruled out -- which must be 0, and each of
      which would be a field whose relation lattice is unsaturated.

  C4. THE LATTICE ONLY GROWS. The map's H must divide the parent's H at
      every field where both are finite. Printed as a mismatch count,
      which must be 0.

RESOURCE. Pure integer arithmetic, per-field float embeddings and a 3x3
LLL; no numpy, no arrays held beyond one field's places. Well under
512MB. The wall clock is the open quantity and it is over ten minutes by
design: the class reading over all 1103 fields is the parent's own
dominant cost (242 s there), and the map adds a box search at each
degree-1 place over a prime above 29 at the 236 fields with H > 1 plus
the pin sample. Estimated 10-20 minutes, printed at the close, run under
memwatch.py. The necessity is that the share is a per-bin statistic and
the top bin is 300-1000, so the prime cap cannot be lowered without
deleting the comparison P1 is about.

SECTIONS.
  S1 the class reading over the population -- the engine, run first
     because everything else reads it.
  S2 the h = 1 pin, the norm accounting and the lattice-growth check.
  S3 the independent negative certificate on a sample.
  S4 the share by prime bin, with the type mix beside it.
  S5 the index of dispersion.
  S6 the cyclic fields' own share against both candidate q's, and what
     the correction moves in the parent's ratio.

FINDINGS.

  F1. THE MAP PLACES THE WHOLE POPULATION, AND THE NEGATIVE HALF HOLDS
      (observation, 1103 cubic fields to |d_K| <= 6000, odd unramified
      primes to 1000; C1-C4 all zero). Every one of the 36929
      degree-1 PLACES at the 236 fields with H > 1 is placed, hence all
      25159 of their degree-1-carrying primes -- and the place count is
      the one to quote, a prime being decided only when every place over
      it is placed, since the verdict is "some place is principal" and
      one unplaced place among three would turn an undecided prime into
      a negative one. So the statistic the parent rig could not read has
      no censoring in it at all. The three
      independent prices of the negative verdict all come in at zero: at
      62 sampled fields with h certified 1 constructively the map's
      lattice has order 1 and calls no prime non-principal, which is the
      identity where the answer is known -- and that pin's population is
      non-circular by measurement rather than assumption, all 867 of the
      population's h = 1 fields reaching the verdict by exhibited
      generators and NONE off the relation lattice, which would have made
      the map's own lattice trivial for the same reason and so tested
      nothing; 40 of the map's non-principal
      verdicts re-run under the shop's exhaustive certificate are
      confirmed, none refuted; and 69323 accepted elements pass the norm
      accounting with no mismatch. What the certificate could not do at
      population scale -- hours, by the parent's own timing -- the map
      does in 219 s wall at 76.5 MB, and the exhaustive route is now what
      grades it rather than what it replaces.

  F2. THE SHARE IS SHORT AT THE BOTTOM AND CLOSES BY THE TOP, AT EVERY
      CLASS NUMBER (observation; P1 SURVIVES at all six read strata).
      Measured share over the mean nominal q, bottom prime bin (3-30)
      against top (300-1000), complex fields:

          h = 2  n = 94   0.635 -> 0.973
          h = 3  n = 83   0.795 -> 0.903
          h = 4  n = 18   0.411 -> 1.044
          h = 5  n = 18   0.537 -> 1.031
          h = 6  n =  6   0.117 -> 0.882
          h = 7  n =  6   0.265 -> 1.029

      Every bottom bin is short and every top bin exceeds its bottom
      bin, which is both of P1's clauses at every stratum. Two things
      the degree-2 reading did not have. The bottom-bin deficit is DEEPER
      AT LARGER CLASS NUMBER without being ordered by it -- 0.117 and
      0.265 at h = 6 and 7 against 0.635 at h = 2, but h = 3 sits above
      h = 2 at 0.795 and h = 7 above h = 6, so it is a direction and a
      spread and not a grading. And the
      climb reaches nominal rather than approaching it: the top bins run
      0.88 to 1.04, three of the six nominally above 1 by 3 to 4% on
      denominators of 417 to 1245. NO SIGNIFICANCE IS COMPUTED FOR THOSE
      EXCURSIONS and none is claimed from them: what the table
      establishes is that the deficit CLOSES by the top bin, not that it
      reverses. Closing is already the whole point -- a shortfall of 0.12
      to 0.80 at the bottom and nothing at the top is a deficit LOCATED
      at small p, which is what a first-hit statistic reading the bottom
      of the range is exposed to and what a pooled share would hide. This is the confound
      explore_cubic_principal.py F3 named from the splitting side, now
      measured on the side the splitting lag is divided out of: the
      share is conditioned on the prime carrying a degree-1 place and
      each prime is read against its OWN type's q, so what is left here
      is the class group's and not Chebotarev's.

  F3. THE COUNT IS UNDER-DISPERSED AT EVERY CLASS NUMBER BUT ONE, WITH
      NO TREND IN THE CLASS NUMBER (observation; P2 SURVIVES at five of
      six read strata, KILLED at h = 3). The index against the bin's own
      measured density, leave-one-out -- the reference of K2 amendment
      II, and the only one the share deficit cannot leak into -- over
      complex fields, with the index's own null spread beside it -- each
      field contributes a standardized squared deviation of mean 1 and
      variance 2, so the index is a chi-square over n and its null SD is
      sqrt(2/n), which the table prints as a z:

          h = 2  n = 94   0.325   z = -4.6
          h = 3  n = 83   1.583   z = +3.8
          h = 4  n = 18   0.461   z = -1.6
          h = 5  n = 18   0.291   z = -2.1
          h = 6  n =  6   0.364   z = -1.1
          h = 7  n =  6   0.123   z = -1.5

      So the mechanism that survived at degree 2 -- principal primes
      arranged more regularly than independence -- reproduces at degree
      3.
      FIVE OF SIX BELOW 1 IS A DIRECTION AND NOT FIVE RESULTS, and the
      spread is why: at n = 6 the null SD is 0.58, so 0.123 and 0.364 sit
      1.5 and 1.1 from 1 and carry nothing on their own however far below
      they look. Only h = 2 clears on its own, at 4.6, with h = 5
      marginal at 2.1. What the six DO carry jointly is the prediction
      P2 actually made, which was about all of them: combining the six
      z's by Stouffer gives -2.9, the h = 3 stratum pulling the other way
      inside it. That is the number the finding is worth -- one strong
      stratum, a consistent direction elsewhere, and one stratum in
      opposition.
      IT DOES NOT DEEPEN WITH THE CLASS NUMBER. The five below 1 are a
      scatter in 0.12 to 0.46 with no direction in it, and the apparent
      deepening the two nominal-referenced columns show was the share
      deficit leaking in, which is exactly what amendment II removes. That the amendment CHANGED a finding rather than
      confirming one is the argument for having made it.
      THE SIZE IS COMPARABLE ONLY AT h = 2, AND THERE THE REGULARITY IS
      WEAKER THAN AT DEGREE 2. Degree 2's one figure on this reference
      and counted to the cap is 0.142 at h = 2; this side reads 0.325 at
      h = 2. Below 1 on both, so the direction ports; a factor of two
      apart, so the SIZE does not, and no other class number has a
      degree-2 counterpart quoted on the same reference to compare with.
      THE h = 3 EXCEPTION IS THE FINDING'S OWN CAUTION AND IT IS SHARP.
      It sits at +3.8 on its own null spread at 83 fields, so it is not
      sampling; and it is above 1 on ALL THREE references -- 2.927,
      1.624 and 1.583 -- so it is neither the level nor the share
      deficit, both of which the last two columns remove. What is left
      is field-to-field heterogeneity at h = 3 specifically: the fields
      disagree with each other about their own principal density more
      than independence allows, at the one class number where the class
      group is Z/3 and both non-trivial classes are inverse to each
      other. Naming which structure does that is the front this leaves
      open, and it is a question about h = 3 and not about degree 3.
      (SETTLED SINCE, by explore_cubic_split_triple.py: the stratum holds
      two arithmetics, 38 of the 83 fields carrying ONE class at all
      three places over every totally split prime and the other 45
      carrying three, so the 1.583 is the gap between two means and the
      index reads 0.220 and 0.252 inside them. WHAT SURVIVES HERE
      UNCHANGED is every number above -- the three references, the null
      spread and the reading that the stratum is not sampling and not the
      level -- since all of them are correct about a population this file
      had no instrument to split. What does NOT survive is the closing
      sentence's implication that the heterogeneity is a property of the
      class number: it is a property of the field, and the class number
      is only where the two kinds happen to be able to coexist.)

  F4. THE NOMINAL DENSITY IS WRONG AT A CYCLIC CUBIC FIELD, BY A FACTOR
      OF 3/7, AND THE CORRECTION IS DERIVED RATHER THAN FITTED (rule,
      proved for h = 3 at derivation (6) and verified on the population's
      two cyclic fields with H > 1). At a cyclic field the three places
      over a totally split prime are one Galois orbit; at h = 3 the
      action is forced trivial, Aut(Z/3) having order 2, so the three
      classes are EQUAL and q_split collapses from 1 - (h-1)(h-2)/h^2 =
      7/9 to 1/h = 1/3. Measured, the two cyclic fields of discriminant
      3969 carry a principal degree-1 place at 0.3333 and 0.3519 of their
      split primes -- 1.000 and 1.056 of the corrected value, against
      0.429 and 0.452 of the uncorrected one. The per-field counts land
      at 19 against corrected predictions of 19.0 and 18.0, the uncorrected
      model's own being what those shares read as 0.429 and 0.452 of.
      AND THE STRATIFIER IS EXACT AT EXACTLY THESE TWO FIELDS, which T3
      does not give for free: H = 3 is a multiple of the true h, so h is
      1 or 3, and h = 1 would put the share at 1 rather than at a third.
      The measurement that confirms the rule is therefore also what
      certifies the class number the rule is stated at.
      IT HAS LINEAGE AND THE LINEAGE IS LIVE. explore_cubic_principal.py
      derivation (2) carries the uncorrected q; its F2 prices the real
      h = 3 stratum with it and its F4 reads the unit-rank separation
      off that stratum, 2 of whose 6 fields are cyclic. Corrected, that
      stratum's first-hit ratio falls from 2.709 to 1.826 -- the measured
      mean L_1 of 47.3 is unchanged, the prediction rising from 17.5 to
      25.9 -- so the unit-rank gap against the complex side's 1.172
      shrinks from 1.54 to 0.65. It still exceeds the 0.25 that killed
      the parent's P5, so the KILL stands; its SIZE was inflated by
      about 40% and the doc carrying it needs the corrected number.

  F5. ONCE THE GALOIS TYPE IS PART OF THE KEY, THE REAL SIDE CANNOT
      CARRY EITHER STATISTIC IN THIS POPULATION (observation; P3
      UNREADABLE, and the parent's F4 caution sharpened). Stratifying by
      signature, Galois type and class number -- which derivation (6)
      forces, three of the model's laws differing between the types --
      leaves no class number above 1 with at least 5 fields on both
      signatures: totally real non-cyclic h = 3 has FOUR fields, h = 2
      has three, and the cyclic h = 3 stratum has two. So the comparison
      P3 asked for does not exist here, and the parent's unit-rank
      separation rests on four non-cyclic fields rather than six.
      What the four do say, and it is printed rather than read: their
      counts are 36, 37, 38, 38 against their own NOMINAL predictions of 47.8,
      48.1, 49.3, 46.1 -- short by about ten each -- while against their
      LOCAL ones of 37.8, 37.2, 38.9, 35.5 they are flat, a local index
      of 0.121. A share deficit that uniform on four fields is worth the
      wider population it would take to read, and that population, not
      the model, is what the next widening of this front buys -- which is
      what the parent said and this measures.

  F6. THE HARVEST WAS ALREADY SATURATED WHEREVER THIS RIG CAN TELL
      (observation; P4 SURVIVES, at 0%). The map's own relation lever --
      two elements of the same place differ by a relation, whatever the
      place -- lowered the shop's H at NO field of the 236 with H > 1.
      So the negative verdicts do not rest on a lattice this rig grew;
      they rest on the pin and the exhaustive certificate of F1, which
      is the weaker of the two supports and the honest one to quote. The
      lever cost nothing and would have been the cheapest possible
      warning; that it fired nowhere is a fact about the shop's harvest
      box at this discriminant cap and not a proof of saturation.

RUN RECORD. `python prime/code/memwatch.py python
prime/code/explore_cubic_class_map.py`. One process, CPython, no BLAS.
246 checks, 219.2 s wall, peak working set 77.1 MB against memwatch's
512 MB ceiling. Enumeration 15370 polynomials -> 1103 fields in 7.7 s;
class reading 1103 fields in 158.2 s, 867 with h = 1 -- all 867
constructively, none off the relation lattice -- 236 with H > 1, none
unresolved; the pin 62 fields in
20.7 s; the map 236 fields, 36929 places and 25159 primes in 25.4 s; the
certificate
sample 40 places in 7.1 s. Four earlier runs are in the repository
history and none of their tables are quoted here: the first at a reduced
discriminant cap was a trial; the second and third were superseded by the
cyclic correction of derivation (6) and by the stratification amendment,
which the second's own diagnostic and the third's per-field line
respectively forced; and the fourth by K2 amendment II, which the audit
of the fourth's own share table forced.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_field_shop as CFS
import explore_cubic_principal as ECP

CHECKS = 0

DISC_CAP = ECP.DISC_CAP        # 6000, the parent's population
PRIME_CAP = ECP.PRIME_CAP      # 1000, the parent's sweep cap
BIN_EDGES = ECP.BIN_EDGES      # (3, 30, 100, 300, 1000), the parent's bins
MIN_STRATUM = ECP.MIN_STRATUM  # 5
ODD_PRIMES = ECP.ODD_PRIMES

MAP_BOX = 3                    # coefficient box in the reduced basis
MAP_LEVELS = (0, 1, 2)         # escalating unit-direction weight grids
MAP_KEEP = 3                   # accepted elements kept per place (R3)
MAX_COFACTOR = 30000           # cofactor size the smoothness strip bothers with
PIN_STRIDE = 14                # C1 sample: every PIN_STRIDE-th certified field
CERT_SAMPLE = 40               # C3 sample: map-negative places re-certified
CERT_DISC_CAP = 2000           # ... at complex fields no wider than this
CERT_PRIME_CAP = 60            # ... over primes no larger than this

ACCEPT_STATS = [0, 0]          # C2: elements accepted, accounting mismatches


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg


def section(t):
    print("\n" + "=" * 68)
    print(t)
    print("=" * 68)


# ------------------------------------------------- integer lattice in Z^k
def echelon(rows, k):
    """Row-echelon over Z with gcd pivots: a list of (col, row) with each
    row zero in every earlier pivot column. Membership below needs the
    gcd form and not merely a triangular one, so the elimination iterates
    a column until one nonzero entry survives it."""
    M = [list(r) for r in rows if any(r)]
    piv = []
    r0 = 0
    for c in range(k):
        best = None
        for r in range(r0, len(M)):
            if M[r][c] and (best is None or abs(M[r][c]) < abs(M[best][c])):
                best = r
        if best is None:
            continue
        M[r0], M[best] = M[best], M[r0]
        again = True
        while again:
            again = False
            for r in range(r0 + 1, len(M)):
                if M[r][c]:
                    q = M[r][c] // M[r0][c]
                    M[r] = [x - q * y for x, y in zip(M[r], M[r0])]
                    if M[r][c]:
                        M[r0], M[r] = M[r], M[r0]
                        again = True
        if M[r0][c] < 0:
            M[r0] = [-x for x in M[r0]]
        piv.append((c, M[r0]))
        r0 += 1
        if r0 >= len(M):
            break
    return piv


def in_span(v, piv, k):
    w = list(v)
    for (c, row) in piv:
        if w[c]:
            if w[c] % row[c]:
                return False
            q = w[c] // row[c]
            w = [x - q * y for x, y in zip(w, row)]
    return not any(w)


def span_order(piv, k):
    """Order of Z^k / span, or None if infinite."""
    if len(piv) < k:
        return None
    o = 1
    for (c, row) in piv:
        o *= abs(row[c])
    return o


# ------------------------------------------------------------- the map
def gen_index(gen_places):
    """(p, i) -> column, where i is maximal_places' own enumeration index
    at p, which is what all_places_upto_prime names its places by."""
    idx = {}
    for col, (p, e, f, name, P) in enumerate(gen_places):
        idx[(p, int(name.split(".")[1]))] = col
    return idx


def strip_smooth(m, prime_set):
    for q in prime_set:
        while m % q == 0:
            m //= q
    return m


def place_vector(O, alpha, m, gen_places, gen_by_prime, k):
    """The exponent vector of (alpha) / P over G, or None when some place
    dividing alpha is missing from G (derivation (3))."""
    a = [0] * k
    for q in sorted(gen_by_prime):
        if m % q:
            continue
        want = CFS.v_p(m, q)
        got = 0
        for (col, f, P) in gen_by_prime[q]:
            val = CFS.place_valuation(O, alpha, P, want + 1)
            a[col] = val
            got += val * f
        if got != want:
            return None
    return a


def map_place(O, P, p, rows, cx, gen_places, gen_by_prime, prime_set, k):
    """Up to MAP_KEEP exponent vectors for the class of P (derivation
    (1)-(3)), smallest norm first, and whether a GENERATOR was among the
    elements accepted. ([], False) means the search placed nothing --
    silent, and counted as such."""
    out = []
    saw_gen = False
    for level in MAP_LEVELS:
        for w in ECP.weight_grid(cx, level):
            wrows = [[w[i] * rows[i][j] for j in range(3)]
                     for i in range(len(rows))]
            red = ECP.reduced_basis(O, P, wrows)
            form = ECP.norm_form(O, red)
            hits = []
            for x in range(-MAP_BOX, MAP_BOX + 1):
                xp = (1, x, x * x, x ** 3)
                for y in range(-MAP_BOX, MAP_BOX + 1):
                    yp = (1, y, y * y, y ** 3)
                    A = [0, 0, 0, 0]
                    for (i, j, kk), c in form.items():
                        A[kk] += c * xp[i] * yp[j]
                    for z in range(-MAP_BOX, MAP_BOX + 1):
                        if x == 0 and y == 0 and z == 0:
                            continue
                        N = ((A[3] * z + A[2]) * z + A[1]) * z + A[0]
                        N = -N if N < 0 else N
                        if N == 0 or N > p * MAX_COFACTOR:
                            continue
                        m = N // p
                        if m * p != N or m % p == 0:
                            continue
                        if strip_smooth(m, prime_set) != 1:
                            continue
                        hits.append((N, m, (x, y, z), red))
            hits.sort(key=lambda t: t[0])
            for (N, m, (x, y, z), red) in hits:
                v = tuple(x * red[0][t] + y * red[1][t] + z * red[2][t]
                          for t in range(3))
                a = place_vector(O, v, m, gen_places, gen_by_prime, k)
                if a is None:
                    continue
                ACCEPT_STATS[0] += 1
                acc = p
                for col, (q, e, f, name, Q) in enumerate(gen_places):
                    if a[col]:
                        acc *= (q ** f) ** a[col]
                if acc != abs(O.norm(v)) or not CFS.in_lattice(v, P, 3):
                    ACCEPT_STATS[1] += 1
                if m == 1:
                    saw_gen = True
                if a not in out:
                    out.append(a)
                if len(out) >= MAP_KEEP:
                    return out, saw_gen
            if out:
                return out, saw_gen
    return out, saw_gen


def harvest(O, gen_places):
    """The shop's relation harvest with its own escalation: the wider box
    where the default one leaves Z^G/L infinite (derivation (4))."""
    rows = CFS.harvest_relations(O, gen_places)
    if CFS.hermite_order(rows, len(gen_places)) is None:
        rows = CFS.harvest_relations(O, gen_places,
                                     box=CFS.REL_BOX + 6, cap=1500)
    return [list(r) for r in rows]


def class_and_relations(O, d, cx, rows):
    """(h, kind, gen_places, relation rows) -- the parent's class reading
    with the harvest kept rather than thrown away, so the map does not
    pay for it twice. 'cert' means every place under the Minkowski bound
    was found principal by exhibited generator, which proves h = 1."""
    gen_places = CFS.relation_generators(O)
    mb = CFS.minkowski_bound(d, O.n, cx)
    small = [t for t in CFS.all_places_upto_prime(O, mb)
             if t[0] ** t[2] <= mb]
    if all(ECP.find_gen(O, P, rows, p ** f, cx) is not None
           for (p, e, f, name, P) in small):
        return 1, 'cert', gen_places, None
    rel = harvest(O, gen_places)
    H = CFS.hermite_order(rel, len(gen_places))
    if H is None:
        return None, None, gen_places, rel
    # 'relH1' is h = 1 read off the relation lattice rather than proved by
    # exhibited generators, and it is kept DISTINCT from 'cert' because the
    # pin cannot use it: where L is already Z^G the map's lattice has order
    # 1 by construction and calls everything principal, so such a field
    # would pass C1 without testing anything.
    return H, ('relH1' if H == 1 else 'H'), gen_places, rel


def run_field(O, a, b, c, d, cx, gen_places, rel0):
    """The whole per-field reading: every degree-1 place over an odd
    unramified prime to the cap, placed in the class group against the
    largest relation lattice this rig can build for the field.

    Returns (H_map, per_prime, unplaced) where per_prime is a list of
    (p, kind, n_deg1, principal|None) and principal is None where the map
    placed none of the prime's places."""
    pdisc = CFS.poly_disc3(a, b, c)
    rows = ECP.t2_rows(O, a, b, c)
    k = len(gen_places)
    idx = gen_index(gen_places)
    gen_by_prime = {}
    for col, (q, e, f, name, Q) in enumerate(gen_places):
        gen_by_prime.setdefault(q, []).append((col, f, Q))
    prime_set = sorted(gen_by_prime)

    rel = ([list(r) for r in rel0] if rel0 is not None
           else harvest(O, gen_places))
    per_place = []          # (p, kind, [vectors]) one entry per place
    unplaced = 0

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
                col = idx[(p, i)]
                e_P = [0] * k
                e_P[col] = 1
                vecs.append([e_P])
            per_place.append((p, kind, vecs))
            continue

        places, kind = ECP.deg1_places(O, a, b, c, pdisc, p)
        if kind in ('ramified', 'inert'):
            continue
        vecs = []
        for P in places:
            got, saw_gen = map_place(O, P, p, rows, cx, gen_places,
                                     gen_by_prime, prime_set, k)
            if not got:
                unplaced += 1
            else:
                for i in range(1, len(got)):        # (R3)
                    rel.append([x - y for x, y in zip(got[0], got[i])])
            vecs.append(got)
        per_place.append((p, kind, vecs))

    piv = echelon(rel, k)
    H_map = span_order(piv, k)

    per_prime = []
    for (p, kind, vecs) in per_place:
        n1 = len(vecs)
        # A prime is decided only when EVERY degree-1 place over it is
        # placed: the verdict is "some place is principal", so one
        # unplaced place among three leaves a False that could be a True,
        # and the direction of that error deflates the share. Partial
        # coverage is undecided, not negative.
        if any(not v for v in vecs):
            per_prime.append((p, kind, n1, None))
            continue
        prin = any(in_span(v[0], piv, k) for v in vecs)
        per_prime.append((p, kind, n1, prin))
    return H_map, per_prime, unplaced


# ----------------------------------------------------------- the sections
def bin_of(p):
    for i in range(len(BIN_EDGES) - 1):
        if BIN_EDGES[i] <= p < BIN_EDGES[i + 1]:
            return i
    return None


def s1_population():
    section("S1  THE ENGINE -- enumeration and the class reading over the "
            "population")
    t0 = time.time()
    fields, buckets = ECP.enumerate_fields(DISC_CAP)
    print("  %d polynomials -> %d fields, %.1f s"
          % (buckets[0], len(fields), time.time() - t0))
    ok(fields[0][1] == -23 or fields[0][1] == 49,
       "least |d| field is %d" % fields[0][1])
    recs = []
    t0 = time.time()
    for (ad, d, cx, polys) in fields:
        a, b, c, O = polys[0]
        rows = ECP.t2_rows(O, a, b, c)
        h, kind, gen_places, rel = class_and_relations(O, d, cx, rows)
        recs.append((d, cx, a, b, c, O, h, kind, gen_places, rel))
    n_cert = sum(1 for r in recs if r[7] == 'cert')
    n_rel1 = sum(1 for r in recs if r[7] == 'relH1')
    n_h1 = sum(1 for r in recs if r[6] == 1)
    n_hi = sum(1 for r in recs if r[6] is not None and r[6] > 1)
    n_un = sum(1 for r in recs if r[6] is None)
    print("  class reading: %d fields, %d with h = 1 -- %d proved "
          "constructively and %d read off the relation lattice, which the "
          "pin cannot use -- %d with H > 1, %d unresolved, %.1f s"
          % (len(recs), n_h1, n_cert, n_rel1, n_hi, n_un,
             time.time() - t0))
    ok(n_cert + n_rel1 == n_h1, "h = 1 labels do not partition")
    ok(n_un == 0, "%d fields unresolved by the class reading" % n_un)
    return recs


def s2_pin(recs):
    section("S2  CONTROL -- the h = 1 pin, the norm accounting, the "
            "lattice growth")
    sample = [r for i, r in enumerate([x for x in recs if x[7] == 'cert'])
              if i % PIN_STRIDE == 0]
    bad_H = bad_place = unplaced = 0
    t0 = time.time()
    for (d, cx, a, b, c, O, h, kind, gp, rel) in sample:
        H_map, per_prime, unpl = run_field(O, a, b, c, d, cx, gp, rel)
        if H_map != 1:
            bad_H += 1
        for (p, pk, n1, prin) in per_prime:
            if prin is None:
                unplaced += 1
            elif not prin:
                bad_place += 1
    print("  [C1] %d CONSTRUCTIVELY certified h = 1 fields sampled "
          "(every %dth), %.1f s"
          % (len(sample), PIN_STRIDE, time.time() - t0))
    print("       %d with map lattice order above 1, %d primes called "
          "non-principal, %d primes unplaced"
          % (bad_H, bad_place, unplaced))
    ok(bad_H == 0, "%d certified h = 1 fields with H_map > 1" % bad_H)
    ok(bad_place == 0,
       "%d primes called non-principal at h = 1" % bad_place)
    print("  [C2] %d elements accepted, %d norm-accounting mismatches"
          % (ACCEPT_STATS[0], ACCEPT_STATS[1]))
    ok(ACCEPT_STATS[1] == 0,
       "%d accepted elements fail the norm accounting" % ACCEPT_STATS[1])
    return len(sample), unplaced


def s1b_map(recs):
    section("S1b THE MAP over the fields with H > 1 -- the engine the "
            "statistics read")
    place_unpl = [0]
    place_tot = [0]
    out = []
    drops = 0
    t0 = time.time()
    for (d, cx, a, b, c, O, h, kind, gp, rel) in recs:
        if h is None or h == 1:
            continue
        H_map, per_prime, unpl = run_field(O, a, b, c, d, cx, gp, rel)
        place_unpl[0] += unpl
        place_tot[0] += sum(t[2] for t in per_prime)
        ok(H_map is not None and h % H_map == 0,
           "map H %s does not divide parent H %s at d = %d" % (H_map, h, d))
        if H_map != h:
            drops += 1
        out.append((d, cx, a, b, c, O, H_map, per_prime))
    n = len(out)
    print("  %d fields with H > 1 mapped, %.1f s" % (n, time.time() - t0))
    print("  [C4] map H divides parent H at every field; %d fields "
          "(%.1f%%) where it is a PROPER divisor"
          % (drops, 100.0 * drops / n if n else 0.0))
    unpl = sum(1 for r in out for t in r[7] if t[3] is None)
    tot = sum(len(r[7]) for r in out)
    print("  %d of %d primes undecided, %d of %d PLACES unplaced -- a "
          "prime is undecided when any one of its places is"
          % (unpl, tot, place_unpl[0], place_tot[0]))
    ok(unpl == 0 and place_unpl[0] == 0,
       "%d primes undecided, %d places unplaced" % (unpl, place_unpl[0]))
    return out, drops


def s3_certificate(mapped):
    section("S3  CONTROL -- the independent negative on a sample of the "
            "map's non-principal verdicts")
    checked = broken = 0
    t0 = time.time()
    for (d, cx, a, b, c, O, H_map, per_prime) in mapped:
        if not cx or abs(d) > CERT_DISC_CAP or checked >= CERT_SAMPLE:
            continue
        pdisc = CFS.poly_disc3(a, b, c)
        for (p, kind, n1, prin) in per_prime:
            if prin is not False or p > CERT_PRIME_CAP:
                continue
            places, kd = ECP.deg1_places(O, a, b, c, pdisc, p)
            if not places:
                continue
            cert, detail = CFS.non_principality_certificate(
                O, places[0], p, (a, b, c))
            checked += 1
            if not cert:
                broken += 1
            break
        if checked >= CERT_SAMPLE:
            break
    print("  [C3] %d map-negative places re-run under the exhaustive "
          "certificate, %.1f s" % (checked, time.time() - t0))
    print("       %d where the certificate found a generator the map "
          "had ruled out" % broken)
    ok(broken == 0,
       "%d map negatives refuted by the exhaustive certificate" % broken)
    return checked


def strata(mapped):
    """Keyed by signature, GALOIS TYPE and class number. The type is part
    of the key for the reason derivation (6) gives: a cyclic field reads a
    third of the primes where a non-cyclic one reads two thirds, every one
    it reads is totally split where a non-cyclic field's are three to one
    partial, and its split q is a third rather than seven ninths. Three
    laws differ, so a stratum holding both is two populations, and a
    dispersion read across it measures the gap between them and not the
    arrangement inside either."""
    st = {}
    for r in mapped:
        st.setdefault((r[1], is_cyclic(r[0]), r[6]), []).append(r)
    return st


def sig_label(cx, cyc):
    return "complex" if cx else ("real-cyc" if cyc else "real")


def is_cyclic(d):
    return d > 0 and int(d ** 0.5 + 0.5) ** 2 == d


def q_of(kind, h, cyc):
    """The nominal q of derivation (2), with the cyclic correction of
    derivation (6): at a cyclic cubic field of class number 3 the three
    places over a totally split prime carry ONE class, so its q is the
    partially split prime's."""
    if cyc and kind == 'split' and h > 1:
        assert h == 3, ("cyclic field with H = %d: the split-prime "
                        "correction is derived only at h = 3" % h)
        return 1.0 / h
    return ECP.q_nominal(kind, h)


def n_cyclic(fs):
    """Cyclic cubic fields in a stratum -- d_K a perfect square. A cyclic
    field reads a THIRD of the primes and every one it reads is TOTALLY
    split, so it enters the split MIX at 1 against a non-cyclic field's
    nominal 1/4, and a stratum holding both is two arithmetics under one
    label. Printed beside every reading for that reason."""
    n = 0
    for r in fs:
        if is_cyclic(r[0]):
            n += 1
    return n


def s4_share(mapped):
    section("S4  THE SHARE by prime bin -- measured over mean nominal q, "
            "with the type mix beside it")
    nb = len(BIN_EDGES) - 1
    labels = ["%d-%d" % (BIN_EDGES[i], BIN_EDGES[i + 1]) for i in range(nb)]
    print("  bin edges %s; 'mix' is the fraction of the bin's "
          "degree-1-carrying primes that are TOTALLY split"
          % (", ".join(labels)))
    rows = []
    for (cx, cyc, h), fs in sorted(strata(mapped).items(),
                                   key=lambda t: (not t[0][0], t[0][1],
                                                  t[0][2])):
        line = []
        for i in range(nb):
            num = den = qsum = split = 0
            for r in fs:
                cyc = is_cyclic(r[0])
                for (p, kind, n1, prin) in r[7]:
                    if bin_of(p) != i or prin is None:
                        continue
                    den += 1
                    num += 1 if prin else 0
                    qsum += q_of(kind, h, cyc)
                    split += 1 if kind == 'split' else 0
            if den == 0:
                line.append(None)
            else:
                line.append((num / float(den), qsum / float(den),
                             split / float(den), den))
        rows.append((cx, cyc, h, len(fs), line))
    print("  strata are keyed by signature, GALOIS TYPE and class number; "
          "'real-cyc' is a cyclic field, which reads a THIRD of the primes "
          "and every one of them totally split, so its mix is 1")
    print("  a stratum under %d fields is printed and NOT read" % MIN_STRATUM)
    print("  n is the bin's DENOMINATOR, the decided degree-1-carrying "
          "primes it pools; a ratio near 1 is read against it")
    print("  %-9s %-3s %-5s %s"
          % ("sig", "h", "n", " ".join("%-30s" % L for L in labels)))
    for (cx, cyc, h, n, line) in rows:
        cells = []
        for cell in line:
            if cell is None:
                cells.append("%-30s" % "--")
            else:
                s, q, mix, den = cell
                cells.append("%-30s" % ("%.3f/%.3f=%.3f m%.2f n%d"
                                        % (s, q, s / q if q else 0.0,
                                           mix, den)))
        print("  %-9s %-3d %-5d %s%s"
              % (sig_label(cx, cyc), h, n, " ".join(cells),
                 "" if n >= MIN_STRATUM else "   (not read)"))
    return rows


def s5_dispersion(mapped):
    section("S5  THE INDEX OF DISPERSION of the per-field count of primes "
            "carrying a principal degree-1 place")
    rows = []
    for (cx, cyc, h), fs in sorted(strata(mapped).items(),
                                   key=lambda t: (not t[0][0], t[0][1],
                                                  t[0][2])):
        nb = len(BIN_EDGES) - 1
        per = []
        for r in fs:
            cyc = is_cyclic(r[0])
            prim, skip = [], False
            for (p, kind, n1, prin) in r[7]:
                if prin is None:
                    skip = True
                    break
                i = bin_of(p)
                if i is not None:
                    prim.append((i, q_of(kind, h, cyc), 1 if prin else 0))
            if not skip and prim:
                per.append((r[0], prim))
        if not per:
            continue
        totq = [0.0] * nb
        totc = [0.0] * nb
        for (d, prim) in per:
            for (i, q, c) in prim:
                totq[i] += q
                totc[i] += c

        ss = vv = ssl = vvl = 0.0
        obs, detail = [], []
        for (d, prim) in per:
            myq = [0.0] * nb
            myc = [0.0] * nb
            for (i, q, c) in prim:
                myq[i] += q
                myc[i] += c
            # LOCAL DENSITY, LEAVE-ONE-OUT: the bin's measured share over
            # the OTHER fields of the stratum, which is the reference the
            # degree-2 rig used and the one this statistic needs -- a
            # nominal q that F2 shows is too high inflates the variance
            # denominator and so DEFLATES the index toward the finding.
            ratio = []
            for i in range(nb):
                dq = totq[i] - myq[i]
                ratio.append((totc[i] - myc[i]) / dq if dq > 0 else None)
            cnt = mu = var = mul = varl = 0.0
            usable = True
            for (i, q, c) in prim:
                cnt += c
                mu += q
                var += q * (1.0 - q)
                if ratio[i] is None:
                    usable = False
                    continue
                ql = min(1.0, q * ratio[i])
                mul += ql
                varl += ql * (1.0 - ql)
            if var <= 0:
                continue
            obs.append((cnt, mu, var))
            detail.append((d, cnt, mu, mul if usable else None))
            ss += (cnt - mu) ** 2
            vv += var
            if usable and varl > 0:
                ssl += (cnt - mul) ** 2
                vvl += varl
        if not obs:
            continue
        mc = sum(o[0] for o in obs) / float(len(obs))
        ssc = sum((o[0] - mc) ** 2 for o in obs)
        rows.append((cx, cyc, h, len(obs), ss / vv if vv else None,
                     ssc / vv if vv else None, mc,
                     sum(o[1] for o in obs) / float(len(obs)), detail,
                     ssl / vvl if vvl else None))
    print("  three references, and only the third answers P2. 'model' is "
          "the ported index against the NOMINAL model mean; 'centred' "
          "removes the stratum's level (K2 amendment); 'local' is against "
          "the bin's own measured share taken LEAVE-ONE-OUT, which is the "
          "reference degree 2 used and the only one a share deficit "
          "cannot leak into (K2 amendment II)")
    print("  z is (local - 1) in units of the index's OWN null spread. "
          "Each field contributes a standardized squared deviation of mean "
          "1 and variance 2 under independence, so the index is a chi-square "
          "over n and its null SD is sqrt(2/n) -- which at n = 6 is 0.58, "
          "and a stratum that thin cannot carry a reading on its own however "
          "far from 1 it lands")
    print("  %-9s %-3s %-6s %-8s %-10s %-8s %-8s %-8s %s"
          % ("sig", "h", "n", "mean", "predicted", "model", "centred",
             "local", "z"))
    for (cx, cyc, h, n, ix, ixc, mc, mp, detail, ixl) in rows:
        z = ((ixl - 1.0) / (2.0 / n) ** 0.5) if (ixl is not None and n)            else None
        print("  %-9s %-3d %-6d %-8.2f %-10.2f %-8s %-8s %-8s %-8s%s"
              % (sig_label(cx, cyc), h, n, mc, mp,
                 "%.3f" % ix if ix is not None else "--",
                 "%.3f" % ixc if ixc is not None else "--",
                 "%.3f" % ixl if ixl is not None else "--",
                 "%+.1f" % z if z is not None else "--",
                 "" if n >= MIN_STRATUM else "   (not read)"))
    print("  per-field (d_K: count against its nominal / its local mean) "
          "at every stratum thin enough for one field to set the index:")
    for (cx, cyc, h, n, ix, ixc, mc, mp, detail, ixl) in rows:
        if n > 8:
            continue
        print("    %s h = %d: %s"
              % (sig_label(cx, cyc), h,
                 ", ".join("%d: %d/%.1f/%s"
                           % (t[0], t[1], t[2],
                              "--" if t[3] is None else "%.1f" % t[3])
                           for t in detail)))
    return rows


def s6_cyclic(mapped):
    section("S6  THE CYCLIC CORRECTION -- the cyclic fields' own share "
            "against both candidate q's, and what it moves")
    cyc = [r for r in mapped if is_cyclic(r[0])]
    print("  %d cyclic fields with H > 1 in the population" % len(cyc))
    print("  %-8s %-4s %-7s %-7s %-7s %-8s %s"
          % ("d_K", "H", "split", "princ", "share", "/(7/9)", "/(1/3)"))
    for (d, cx, a, b, c, O, H, per_prime) in cyc:
        ns = sum(1 for t in per_prime if t[3] is not None)
        np_ = sum(1 for t in per_prime if t[3])
        sh = np_ / float(ns) if ns else 0.0
        ok(all(t[1] == 'split' for t in per_prime),
           "cyclic field %d carries a partially split prime" % d)
        print("  %-8d %-4d %-7d %-7d %-7.4f %-8.3f %.3f"
              % (d, H, ns, np_, sh, sh / (7.0 / 9.0), sh / (1.0 / 3.0)))

    print("\n  what the correction moves in the parent's first-hit ratio, "
          "at the stratum that carries it:")
    for (want_cx, want_h) in ((False, 3),):
        fs = [r for r in mapped if r[1] == want_cx and r[6] == want_h]
        meas, pred_old, pred_new, drop = [], [], [], 0
        for r in fs:
            cy = is_cyclic(r[0])
            l1 = None
            for (p, kind, n1, prin) in r[7]:
                if prin and l1 is None:
                    l1 = p
            seq_o = [(p, kind, ECP.q_nominal(kind, want_h))
                     for (p, kind, n1, prin) in r[7]]
            seq_n = [(p, kind, q_of(kind, want_h, cy))
                     for (p, kind, n1, prin) in r[7]]
            if l1 is None:
                drop += 1
                continue
            meas.append(l1)
            pred_old.append(ECP.model_mean(seq_o, PRIME_CAP)[0])
            pred_new.append(ECP.model_mean(seq_n, PRIME_CAP)[0])
        m = sum(meas) / float(len(meas))
        po = sum(pred_old) / float(len(pred_old))
        pn = sum(pred_new) / float(len(pred_new))
        print("  %s h = %d, %d fields (%d cyclic), %d with no principal "
              "place below the cap"
              % ("complex" if want_cx else "real", want_h, len(fs),
                 n_cyclic(fs), drop))
        print("    measured mean L_1 %.1f;  predicted %.1f uncorrected "
              "(ratio %.3f), %.1f corrected (ratio %.3f)"
              % (m, po, m / po, pn, m / pn))
    return cyc


def main():
    t0 = time.time()
    recs = s1_population()
    s2_pin(recs)
    mapped, drops = s1b_map(recs)
    s3_certificate(mapped)
    s4_share(mapped)
    s5_dispersion(mapped)
    s6_cyclic(mapped)
    section("SUMMARY")
    print("  %d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
