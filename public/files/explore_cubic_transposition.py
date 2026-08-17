r"""IS THE CLASS OF A DEGREE-1 PLACE UNIFORM WHEN ITS FROBENIUS IS A
TRANSPOSITION? -- the corpus prices a partially split prime's one
degree-1 place at a principal probability of 1/h, and the whole
justification on record is that [P] + [P'] = 0 is one constraint on two
classes. The totally split side was not left there: its realized triples
were pinned to a permutation-stable SUBGROUP by a Frobenius argument that
runs because such a prime's Frobenius lies in the subgroup Gal(H~/N),
where the map to the triple of classes is a homomorphism. A partially
split prime's Frobenius is a TRANSPOSITION. It lies in no such subgroup
and that argument does not port. This file settles the distribution on
paper and then measures it.

WHAT RIDES ON THE ANSWER. The nominal 1/h is the reference every partial
share in the corpus is quoted against -- explore_cubic_zero_tilt.py
derivation (5) states it, its S4 measures against it, and the same
per-place nominal is what the degree-2 reading of
explore_cubic_principal.py uses. If the true distribution is uniform, the
measured partial-side shortfall is arithmetic and must be located in the
primes rather than in the model. If it is not uniform, part of that
shortfall is a modelling artifact and the deficit at degree 2 inherits
the same correction.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The suspicion
arrives in the TRIPLE's vocabulary -- "the split side was pinned to a
subgroup, so the partial side is probably pinned too" -- and that is a
transplant from a neighbouring splitting type, flagged T2 below. The
object here has no triple in it at all: one place, one class, and the
question is the distribution of a single group element. The right unit is
therefore the class of ONE place, and the statistic this file reads is
that class's ORDER in Cl(K), which is canonical and so poolable across
fields where a class LABEL is not.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_cubic_split_triple.py AND ITS TWO PARENTS: the
    enumeration, the maximal order, the place engines, the class reading,
    the relation harvest, the per-place vector reader (read_field), the
    principality test, the population, the discriminant cap, the prime
    cap and the bin edges are IMPORTED, not re-implemented. Every control
    those files run rides in with them.

 T2 THE SUSPICION ITSELF IS A TRANSPLANT from the totally split type,
    where the realized set IS a proper subgroup at 38 of 83 fields. The
    derivation below does not assume the transplant either way: it
    computes the realized set for the transposition type from scratch and
    the answer is a coset, whose index it then settles.

 T3 THE ORDER STATISTIC IS NEW HERE and nothing upstream computes it. It
    needs a canonical representative of a class, which the parents never
    needed -- they only ever asked principal or not. C2 certifies the
    representative before any distribution is read off it.

 T4 THE INHERITED CONTROLS ARE RE-COUNTED WHERE THIS FILE'S OWN WALK
    ALREADY HOLDS THE DATA. A number quoted by a parent and re-derivable
    here for free is re-derived (C6), the parent's controls otherwise
    riding in with T1 unexamined.

THE HAND-DERIVATION (pre-engine, on paper).

  (0) SCOPE. K is a cubic field, N its Galois closure. A partially split
      prime EXISTS only when K is non-Galois, since a cyclic cubic field
      has no splitting type (1,2) at all -- Gal(N/Q) = Z/3 has no
      transposition. So throughout, Gal(N/Q) = S_3, and K is the fixed
      field of a point stabiliser <t> for a transposition t, under the
      action of S_3 on the three cosets {1, 2, 3}. H is the Hilbert class
      field of K -- the maximal abelian extension unramified at EVERY
      place, the infinite ones included, so Gal(H/K) is the ordinary
      class group Cl(K), which is the group the corpus's h counts. H~ is
      the Galois closure of H over Q, and A = Gal(H~/N).

  (1) THE ONE CONSTRAINT, AND WHAT IT DOES NOT SAY. p unramified and
      partially split: (p) = P.Q with P of residue degree 1 and Q of
      residue degree 2. Then [P] + [Q] = [(p)] = 0, one linear condition
      on two unknowns, so [P] is unconstrained BY THAT CONDITION and the
      corpus reads it as uniform on Cl. An unconstrained coordinate is
      not a uniform one: the constraint says what the class group forbids
      and says nothing about which values a Frobenius actually takes.

  (2) THE RESTRICTION HOMOMORPHISM THE TRANSPOSITION DOES ADMIT. Write
      H^(1), H^(2), H^(3) for the three conjugate copies of H inside H~,
      indexed so that H^(i) sits over the i-th conjugate of K and
      H^(1) = H sits over K = K^(1). Let

          Stab = { g in Gal(H~/Q) : g(H^(1)) = H^(1) },

      the preimage of <t> under Gal(H~/Q) -> Gal(N/Q) = S_3, of order
      2|A|. Every g in Stab restricts to K as the identity, because its
      image in S_3 lies in <t> and t fixes K pointwise. H/K is abelian,
      hence Galois, so

          res : Stab -> Gal(H/K) = Cl(K),   g |-> g|_H

      is a group HOMOMORPHISM. This is the transposition's replacement
      for the split type's homomorphism onto the triple: not a map to
      Cl^3 defined on Gal(H~/N), but a map to Cl defined on the larger
      subgroup Stab, which is exactly the subgroup a transposition
      Frobenius CAN be arranged to lie in.

  (3) THE FROBENIUS LANDS THERE, AND ITS IMAGE IS WELL DEFINED. Let p be
      unramified in H~ and partially split in K. Its Frobenius is a
      conjugacy class in Gal(H~/Q) whose image in S_3 is the class of
      transpositions. Choose a prime of H~ over p whose Frobenius g has
      image t; then g lies in Stab. The places of K over p correspond to
      the orbits of <t> on {1, 2, 3}, with residue degree the orbit size,
      so the FIXED point is the degree-1 place P and the 2-cycle is Q.
      Artin reciprocity for H/K identifies [P] with the Frobenius of P in
      Gal(H/K), which is g|_H since P has residue degree 1 over p. So

          [P] = res(g).

      The value does not depend on which prime over p was chosen: two
      admissible choices differ by conjugation by an element of Stab, and
      res(hgh^-1) = res(h)res(g)res(h)^-1 = res(g) because Cl(K) is
      abelian. So [P] is a well-defined function of the Frobenius class,
      which is what makes Chebotarev applicable to it.

  (4) THE REALIZED SET IS A COSET, AND ITS SUBGROUP IS NAMED. Fix any
      lift u in Stab of t. Then Stab is the union of A and u.A, and the
      elements of Stab lying over a transposition are exactly u.A. Hence

          { [P] : p partially split } = res(u) . res(A),

      and res(A) = { a|_H : a in Gal(H~/N) }. Restriction to H carries
      Gal(H~/N) onto Gal(H/(H n N)) -- the standard restriction
      isomorphism, H/(H n N) being Galois since H/K is abelian. Write

          S = res(A) = Gal(H / (H n N))  <=  Cl(K).

      So [P] is equidistributed over the COSET res(u).S. The fibres of
      res over that coset are cosets of one kernel and so of one size;
      what carries Chebotarev's density from CONJUGACY CLASSES to the
      coset is that the centralizer of any g in u.A lies inside Stab --
      an x with xgx^-1 in Stab has its image normalizing <t>, and <t> is
      its own normalizer in S_3 -- so every G-class meeting Stab meets it
      in exactly one Stab-class, of a third the size, and the three
      transpositions contribute alike. And since H n N lies between K and
      N with [N : K] = 2,

          [Cl(K) : S] = [H n N : K] = 1 or 2,

      the value 2 occurring exactly when N is contained in H. THE
      DICHOTOMY IS THEREFORE TOTAL. Either S = Cl(K) and [P] is uniform
      on the whole class group, the nominal 1/h being exactly right; or
      [Cl : S] = 2 and [P] is uniform on the NONTRIVIAL coset of an
      index-2 subgroup, in which case a partially split prime's place is
      NEVER principal and the true partial share is 0 rather than 1/h.
      There is no third possibility and no approximate one.

  (5) THE EXCEPTIONAL BRANCH IS EMPTY, BY TWO DIFFERENT ROUTES AT THE
      TWO KINDS OF CUBIC FIELD. AT A CYCLIC ONE there is nothing to
      prove: N = K, so H n N = K and the index is 1 outright. That case
      carries no partially split prime at all, but corollary (a) below
      runs there and needs S, so it is settled rather than skipped.
      AT A NON-CYCLIC ONE THE STATEMENT IS THAT N/K IS RAMIFIED.
      N contains the quadratic resolvent k = Q(sqrt(disc K)),
      which is a genuine quadratic field, so some prime p ramifies in k.
      Its inertia group I in Gal(N/Q) = S_3 surjects onto the inertia in
      Gal(k/Q) = Z/2, so |I| is even: I is generated by a transposition,
      or I = S_3 (an order-6 cyclic inertia is impossible, S_3 having no
      element of order 6, and no other even-order subgroup exists).

        - I = <s> for a transposition s. The places of K over p are the
          orbits of the decomposition group on {1, 2, 3}, and the
          ramification index of a place is the size of an I-orbit inside
          it. The orbits of <s> are a fixed point and a 2-cycle, so some
          place P of K over p has e(P/p) = 1. In N the ramification index
          over p is |I| = 2, so e(N/K) at P is 2/1 = 2: RAMIFIED.

        - I = S_3. Then p has one place in K, with e = 3 and f = 1, while
          e(p) = 6 in N, so again e(N/K) = 6/3 = 2: RAMIFIED.

      Either way N/K is ramified at a finite prime, so N is not contained
      in H, H n N = K, and S = Cl(K) -- the same conclusion the cyclic
      case reaches for free.

      A SECOND AND INDEPENDENT KILL COVERS THE POPULATION THIS FILE
      MEASURES, which is the complex cubic fields. Such a K has exactly
      one real embedding and disc K < 0, so k is imaginary and N is
      totally imaginary: the real place of K ramifies in N. H is
      unramified at the infinite places too, so N is not inside H for
      that reason alone. The two kills are independent and the finite one
      is the general statement.

  (6) THE LAW, AND WHAT IT DOES AND DOES NOT LICENCE. Combining (4) and
      (5): AT EVERY CUBIC FIELD, THE CLASS OF THE DEGREE-1 PLACE OVER A
      PARTIALLY SPLIT PRIME IS EQUIDISTRIBUTED OVER THE WHOLE OF Cl(K).
      The corpus's nominal 1/h is therefore derived and not assumed, and
      the partial-side shortfall it measures is arithmetic -- a
      small-prime effect that must close as the primes grow, since
      Chebotarev's error is the only slack left in the statement.

      TWO COROLLARIES the same computation hands over.

        (a) THE SPLIT SIDE'S MARGINAL IS UNIFORM TOO, IN BOTH REGIMES, AND FOR
            THE SAME REASON. For a totally split prime the realized triples
            form the subgroup R of M = {(c1,c2,c3) : sum = 0} computed in
            explore_cubic_split_triple.py derivation (3), R being the image of
            A under the triple of restrictions. So a coordinate projection of R
            is res(A) = S, which (5) makes the whole of Cl(K) -- every
            coordinate of the triple is uniform, at every cubic field, cyclic
            ones included by (5)'s first route, and whatever R is. The two h =
            3 regimes are instances: at R = M the projection is onto by
            inspection, and at R = D = {(t,t,t)} it is the isomorphism t |-> t,
            also onto. So a SINGLE place is uniform on Cl at a degenerate field
            exactly as at a generic one, and R = 0 forces h = 1. The degeneracy
            that file measures is entirely a CORRELATION between the three
            coordinates and is invisible to any one of them. This says that no
            per-place statistic can see the regime split, which is a prediction
            with teeth: the partial primes at the 38 degenerate fields must
            read the same share as at the 45 others.

        (b) DEGREE 2 GETS THE SAME NOMINAL DERIVED, more cheaply. For a
            quadratic K, H/Q is Galois and a split prime's Frobenius lies
            in Gal(H/K) = Cl(K); Chebotarev distributes it uniformly
            there, and the conjugation action of the nontrivial element
            of Gal(K/Q) sends c to -c, which is exactly the pairing
            [P'] = -[P] of the two places. So each place's class is
            uniform on Cl and the 1/h of explore_cubic_principal.py is
            derived. No resolvent and no closure are needed, the
            transposition having no analogue at degree 2.

PREDICTIONS, FROZEN BEFORE ANY ENGINE CODE, AS OBSERVABLES.

 P1 THE ORDER DISTRIBUTION MATCHES THE GROUP'S OWN PROFILE. Over
    partially split primes, the ORDER of [P] in Cl(K) distributes as the
    order profile of Cl(K) itself -- each field contributing its own
    profile, since two groups of the same h need not have the same one
    (Z/4 against Z/2 x Z/2 at h = 4). Kill observable: in the top prime
    bin, pooled over the whole population, some order cell reads
    |z| >= 4.0 against the summed profile, with the cell's variance
    computed as the sum of per-field Bernoulli variances and not as a
    multinomial's.

 P2 THE SHORTFALL IS LOCATED IN THE SMALL PRIMES AND CLOSES. The
    principal cell (order 1) is short at the bottom bin and within noise
    at the top. Kill observable: the top bin's order-1 cell reads
    |z| >= 4.0, or the bottom bin's reads z >= 0 -- either would say the
    departure is not a small-prime effect. This prediction is DIRECTIONAL
    and the direction is the parent's measurement, not this file's
    derivation, which is silent about the size of Chebotarev's error.

 P3 THE INDEX-2 BRANCH IS NOT REALIZED. Kill observable: at any stratum
    with h even, the partial-prime order-1 count is 0 while the stratum
    holds at least 100 partial primes. That is the signature of
    [Cl : S] = 2 and derivation (5) forbids it.

 P4 THE REGIME SPLIT IS INVISIBLE PER PLACE (corollary (a)). Kill
    observable: at h = 3, the partial-prime principal share over the
    degenerate fields and over the others differ by |z| >= 4.0 from each
    other, or either differs from 1/3 by |z| >= 4.0 in the top two bins.

 P5 THE SPLIT SIDE'S MARGINAL IS UNIFORM (corollary (a) again). Kill
    observable: at the degenerate h = 3 fields, where all three places
    carry one class so that each split prime is ONE independent draw, the
    common class is principal at a rate differing from 1/3 by |z| >= 4.0
    pooled over the top two bins.

CONTROLS, run before any kill or survive verdict is read.

 C1 THE POSITIVE CONTROL IS THE h = 1 PIN. At a field with h = 1 every
    class is trivial, so every partial place must read order 1 and the
    share must be exactly 1.000 with no fitted freedom. A rig that cannot
    print that is not measuring the class of a place. Run on a stride
    sample of the certified h = 1 fields.

 C2 THE CANONICAL REPRESENTATIVE IS CERTIFIED BEFORE IT IS USED (T3).
    Three checks on every mapped field: the reduction of a vector already
    in the relation span is the zero tuple; the box of reduced
    representatives has exactly h members and their orders divide h with
    exactly one of order 1; and reduction agrees with the parents'
    principality test at every read place -- order 1 if and only if
    is_principal.

 C3 THE INDEX CONVENTION IS RE-DERIVED FROM THE ENGINE AND NOT REMEMBERED.
    read_field returns a vector list per prime; a partially split prime
    must return exactly one, a totally split prime exactly three. Counted
    and asserted over the pin sample AND over the whole walked
    population, since every statistic below indexes that list.

 C4 THE DROPS ARE COUNTED AND REPORTED BY TYPE. A place the map fails to
    place carries no vector; if the failure rate differed between the two
    splitting types the comparison of their shares would be confounded.

 C5 THE KILL'S DENOMINATOR IS MEASURED, NOT ASSUMED (added at the audit
    and the reason the P1 verdict below reads as it does). Every z here
    prices a cell with the sum of per-prime Bernoulli variances, which
    assumes one field's primes are independent -- and the corpus already
    measures the SPLIT count as UNDER-dispersed. Under-dispersion makes
    that denominator too big and every |z| too small, the direction that
    turns a kill into a survive, so the per-field standardized residual's
    spread across fields is read and every threshold is met on the
    rescaled number.

 C6 A NUMBER THE PARENT QUOTES IS RE-COUNTED WHERE THIS WALK ALREADY HOLDS
    THE DATA (T4, added at the audit). The parent's control names the
    split primes at h = 3 carrying no principal place; that count is
    re-derived here and reconciled against the two decompositions of the
    same stratum.

SECTIONS. S1 the population and the class reading (T1). S2 the controls
C1 and C3. S3 the per-field order profiles and C2. S4 the partial-prime
order distribution against those profiles, pooled and per bin -- P1 and
P3. S5 where the departure sits: the per-bin principal share, and the
regime comparison at h = 3 -- P2 and P4. S6 the split side's marginal at
the degenerate fields -- P5, with C6 beside it. S7 the dispersion of the
count every kill is read on -- C5.

FINDINGS.

 F1 THE NOMINAL IS DERIVED, AND THE POPULATION HAS NOT REACHED IT (rule,
    proved, derivations (2) to (5); observation, 227 complex cubic
    fields at the parent's discriminant cap and 18689 partially split
    primes below 1000).
    The class of the degree-1 place over a partially split prime is
    equidistributed over the WHOLE class group -- the realized set is a
    coset of Gal(H/(H n N)), that subgroup has index [H n N : K] in
    Cl(K), and N/K is ramified at every cubic field, so the index is 1.
    The corpus's 1/h stops being a uniformity assumption. THE
    MEASUREMENT DOES NOT REACH THAT REFERENCE AT THIS PRIME CAP, AND
    P1 SURVIVES ONLY ON THE CELL IT NAMED AND ONLY NARROWLY. The
    observable was frozen on the POOLED top bin, which reads 4306
    principal against 4449.7, z = -2.81 on the binomial variance and
    -3.88 once F7's measured dispersion is priced in, against a kill at
    4.0. It does not fire. Finer than the observable -- and so not the
    kill, however tempting -- the h = 2 stratum's own order-1 cell is at
    -3.08 and -4.25, past the same number. WHAT NEITHER READING COULD
    TOUCH IS THE LAW: derivations (2) to (5) are a proof, and a count
    over primes below 1000 cannot refute a Chebotarev asymptotic -- it
    can only say the population has not arrived, which is F2's statement
    made sharp. The frozen kill was under-specified in two ways worth
    naming: it fixed a threshold and left the VARIANCE MODEL to be
    chosen after the run, and it named a POOLING at which the effect is
    diluted, so the same data reads either side of 4.0 depending on a
    choice the freeze did not make. P3's branch is a COUNT and is
    immune to all of that -- the index-2 alternative, which would make a
    partial place NEVER principal, is refuted directly at every even
    stratum: 3571 of 7745 at h = 2, 326 of 1460 at h = 4, 64 of 489 at
    h = 6, 21 of 172 at h = 8.

 F2 THE DEPARTURE IS A SMALL-PRIME EFFECT AND IT CLOSES, BUT IT HAS NOT CLOSED
    BY 1000 (observation; S5). Pooled over every stratum the principal cell
    reads 176 against 349.9 at z = -12.14 over primes 3 to 30, then 510 against
    627.8 at z = -6.13, 1444 against 1568.4 at z = -4.09, and 4306 against
    4449.7 at z = -2.81 in the top bin. The sign is negative at 25 of the 28
    stratum-by-bin cells, and all three exceptions sit at the top of the prime
    range and within noise -- z = +0.10 at h = 5's top bin, +0.12 and +0.29 at
    h = 8's two -- while the pooled magnitude falls monotonically. THE RESIDUAL
    AT THE TOP BIN IS THE HONEST STATE: this is a bound and not a vanishing,
    and the derivation is silent about the rate, so what the run establishes is
    that the shortfall is arithmetic and shrinking rather than that it is gone
    -- and on the measured denominator the top bin is short at z = -3.88
    pooled, so at this cap it is not gone by a wide margin. This is the
    degree-3 per-place reading of the same shortfall explore_principal_share.py
    measures at degree 2.

 F3 THE SHORTFALL IS GRADED BY THE ORDER OF THE CLASS, WHICH ONLY A
    FULL-DISTRIBUTION READ CAN SEE (observation; S4). All three strata
    with more than two order classes put the deficit at the LOW orders
    and the excess at the highest, and at two of the three the reading is
    MONOTONE in the order: h = 4 reads z = -2.36, -1.45, +3.30 at orders
    1, 2, 4 and h = 6 reads -2.12, -0.67, -0.19, +2.40 at orders
    1, 2, 3, 6, while h = 8 reads -0.12, -2.19, +0.70, +0.91 at orders
    1, 2, 4, 8 -- top-heavy like the others but with its order-1 cell
    ABOVE its order-2 one. THE EXCEPTION IS THE THINNEST STRATUM IN THE
    POPULATION, two fields and 172 primes with an order-1 expectation of
    21.5, so what the run supports is the deficit-low/excess-high shape
    and not a monotone ladder. Every previous reading of this population
    collapsed the class group to principal-or-not and could not have seen
    either. It is the per-place form of the ladder
    explore_class_level.py grades by a class's order at degree 2,
    where the generators sit at a ceiling and everything below falls
    away -- the same direction, low orders short.

 F4 THE REGIME SPLIT IS INVISIBLE TO A SINGLE PLACE (observation; S5,
    corollary (a)). At h = 3 the 38 degenerate fields and the 45 others
    read partial-prime principal shares of 0.3205 and 0.2995, differing
    at z = +1.88, and in the top two bins each sits within noise of 1/3
    (z = -1.14 and -2.93; rescaled by F7, +2.33, -1.41 and -3.63, all
    inside the frozen kill). The degeneracy the parent file measures is
    therefore a CORRELATION among the three coordinates of a split
    triple and not a property of the field's degree-1 places. The
    all-bins reading at R = M is z = -4.34, which is F2's small-prime
    effect and not a regime difference -- the frozen kill was on the top
    two bins for exactly that reason.

 F5 AT THE DEGENERATE FIELDS THE SPLIT SIDE'S MARGINAL IS UNIFORM ON THE NOSE
    (observation; S6). There every split prime carries one class three times,
    so each is a single independent draw, and 297 of the 892 such primes carry
    a principal class against 297.3 expected -- z = -0.02, and +0.89 over the
    top two bins, which no rescaling moves. This is the cleanest per-place
    confirmation in the file, and it comes from the very population whose
    TRIPLE distribution is maximally non-uniform.

 F6 EVERY CLASS GROUP IN THIS POPULATION IS CYCLIC, SO ONE GUARD DID NOT
    FIRE (observation; S3). The design computes each field's own order
    profile because two groups of the same h need not share one; over
    the 227 fields the profiles are those of Z/2, Z/3, Z/4, Z/5, Z/6,
    Z/7 and Z/8 and nothing else, so no field in this population would
    have been misread by the coarser assumption. The machinery is
    correct and untested by a counterexample, which is what it is worth
    and no more.

 F7 THE PARTIAL COUNT IS UNDER-DISPERSED, ON A SPLITTING TYPE THAT
    CARRIES NO TRIPLE (observation; S7). Across 227 field-and-top-bin
    cells the per-field standardized residual has spread 0.725 where
    independence gives 1.000 -- an index of dispersion of 0.526 -- and
    0.807 over all bins, index 0.651, with mean residuals of -0.184 and
    -0.208 carrying F2's shortfall. THE INSTRUMENT'S OWN BIAS RUNS
    AGAINST THE FINDING, which is why the finding is stated at all: a
    shortfall that is proportional rather than additive makes a big
    field's residual larger than a small one's by the square root of its
    count, so unequal field sizes push the measured spread UP, and the
    true dispersion is at most what is printed. So the regularity
    explore_cubic_class_map.py finds in the SPLIT count is present in the
    partial one too, where there is no triple and no sum-to-zero
    constraint available to host it. The two indices are not the same
    statistic -- that one is read leave-one-out against a measured local
    density and this one against a derived nominal -- so what carries is
    the direction and the presence and not the size. WHAT IT LICENSES IS
    NARROWER THAN IT LOOKS: the residual read here is the ORDER-1 cell's,
    so the rescalings in F1 and F4 are on that same cell and are
    measurements, while any other order cell's dispersion is UNMEASURED
    -- F3's shape is an ordering of cells and survives a common rescaling
    whatever it is, which is the property that makes it readable without
    one.

 F8 A NUMBER THE CORPUS QUOTED TWICE WAS ONE QUANTITY (observation; C6,
    added at the audit). The split primes at h = 3 carrying NO principal
    place were recorded as 892 in explore_cubic_split_triple.py's control
    and from there in the doc and on the page, and 892 is the DEGENERATE
    regime's split TOTAL sitting a line away. Re-counted here: 753, being
    595 at R = D and 158 at R = M, and it reconciles three ways -- against
    2023 = 1131 + 892 split, against 1137 = 245 + 892 equal, and against
    the identity that a split prime with no principal place has all three
    classes equal, which puts the all-principal equal triples at 384.
    The control's VERDICT is untouched: the identity still holds at every
    one of them, and only its denominator was another statistic.

RUN RECORD. `python prime/code/memwatch.py python
prime/code/explore_cubic_transposition.py`. One process, CPython, no BLAS. 16
checks, 200.3 s wall, peak working set 76.6 MB against memwatch's 512 MB
ceiling. Enumeration 15370 polynomials -> 1103 fields; class reading 1103
fields, 0 unresolved; the h = 1 pin 48 fields and 3985 partial places in 9.6 s;
the profile pass over 227 mapped complex fields in 24.3 s, 35477 places read
with 0 order-1 disagreements against the parents' principality test; the walk
0.2 s over 32 cells with 0 vector lists of the wrong length and 0 places
dropped by the map on either splitting type; S7 reads 227 top-bin field cells,
S6 and C6 the 2023 split primes of the h = 3 stratum. AN EARLIER RUN IS NOT
QUOTED HERE AND ITS DEFECT IS WHY S4 READS ITS STRATA OFF THE WALK: a declared
tuple of class numbers stopped at 7, so the two h = 8 fields appeared in every
pooled row and in no stratum row, which cost 172 primes from the population
count and hid the one stratum that breaks F3's monotone reading. """

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_principal as ECP
import explore_cubic_class_map as CCM
import explore_cubic_split_triple as ST

CHECKS = 0

DISC_CAP = ECP.DISC_CAP
BIN_EDGES = ECP.BIN_EDGES
MIN_SPLIT = ST.MIN_SPLIT        # the parent's per-field reading floor
HIGH_FRAC = ST.HIGH_FRAC        # the parent's R = D threshold

PIN_STRIDE = 14                 # C1: every PIN_STRIDE-th certified field
MIN_CELL = 30                   # expected count a cell needs before it reads
Z_KILL = 4.0                    # every kill observable's threshold


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def section(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


def bin_of(p):
    for i in range(len(BIN_EDGES) - 1):
        if BIN_EDGES[i] <= p < BIN_EDGES[i + 1]:
            return i
    return None


def bin_name(i):
    return "%d-%d" % (BIN_EDGES[i], BIN_EDGES[i + 1])


# --------------------------------------------- the canonical class label
def reduce_vec(v, piv):
    """The Hermite-reduced representative of v modulo the relation span.

    Each echelon row is zero in every earlier pivot column, so reducing
    the pivot columns in order never disturbs one already reduced, and
    the result depends only on the coset."""
    w = list(v)
    for (c, row) in piv:
        if row[c]:
            q = w[c] // row[c]
            if q:
                w = [x - q * y for x, y in zip(w, row)]
    return tuple(w)


def class_order(v, piv, h):
    """The order of the class of v in the quotient, or None if it exceeds
    h -- which C2 turns into a failure rather than a silent cell."""
    w = [0] * len(v)
    for m in range(1, h + 1):
        w = [x + y for x, y in zip(w, v)]
        if CCM.in_span(w, piv, len(v)):
            return m
    return None


def group_profile(piv, k, h):
    """order -> count over the whole quotient group, by enumerating the
    box of reduced representatives. Returns None if the box is not the
    group (which C2 catches)."""
    ranges = []
    for (c, row) in piv:
        ranges.append((c, abs(row[c])))
    reps = [[0] * k]
    for (c, n) in ranges:
        nxt = []
        for r in reps:
            for t in range(n):
                q = list(r)
                q[c] = t
                nxt.append(q)
        reps = nxt
    if len(reps) != h:
        return None
    prof = {}
    for r in reps:
        d = class_order(r, piv, h)
        if d is None:
            return None
        prof[d] = prof.get(d, 0) + 1
    return prof


# ------------------------------------------------------- the sections
def s1_population():
    section("S1  THE ENGINE -- enumeration and the class reading (T1)")
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


def s2_pin(recs):
    section("S2  C1 THE h = 1 POSITIVE CONTROL, C3 THE INDEX CONVENTION")
    t0 = time.time()
    pool = [r for r in recs if r[7] == 'cert' and r[1]]
    sample = pool[::PIN_STRIDE]
    n_part = n_bad = 0
    n_vec_bad = 0
    for (d, cx, a, b, c, O, h, kind, gp, rel) in sample:
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        for (p, kd, vecs) in per_prime:
            if kd == 'partial' and len(vecs) != 1:
                n_vec_bad += 1
            if kd == 'split' and len(vecs) != 3:
                n_vec_bad += 1
            if kd != 'partial' or len(vecs) != 1 or vecs[0] is None:
                continue
            n_part += 1
            if reduce_vec(vecs[0], piv) != tuple([0] * k):
                n_bad += 1
    print("  C1: %d h = 1 fields, %d partial places, %d not reduced to zero"
          % (len(sample), n_part, n_bad))
    print("  C3: %d vector lists of the wrong length over the same sample"
          % n_vec_bad)
    print("  %.1f s" % (time.time() - t0))
    ok(n_part > 0, "the pin read no partial places at all")
    ok(n_bad == 0, "%d partial places non-principal at h = 1" % n_bad)
    ok(n_vec_bad == 0, "%d vector lists of the wrong length" % n_vec_bad)
    return sample


def s3_profiles(recs):
    section("S3  C2 THE CANONICAL REPRESENTATIVE, AND THE ORDER PROFILES")
    t0 = time.time()
    mapped = []
    prof_bad = ord_bad = agree_bad = span_bad = 0
    n_place = 0
    seen = {}
    for (d, cx, a, b, c, O, h, kind, gp, rel) in recs:
        if h is None or h == 1 or not cx:
            continue
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        if H is None or H == 1:
            continue
        prof = group_profile(piv, k, H)
        if prof is None:
            prof_bad += 1
            continue
        if prof.get(1, 0) != 1 or sum(prof.values()) != H:
            prof_bad += 1
            continue
        if any(H % dd for dd in prof):
            ord_bad += 1
            continue
        for (cc, row) in piv:
            if reduce_vec(row, piv) != tuple([0] * k):
                span_bad += 1
        for (p, kd, vecs) in per_prime:
            for v in vecs:
                if v is None:
                    continue
                n_place += 1
                o = class_order(v, piv, H)
                if (o == 1) != ST.is_principal(v, piv, k):
                    agree_bad += 1
        key = tuple(sorted(prof.items()))
        seen[(H, key)] = seen.get((H, key), 0) + 1
        mapped.append((d, cx, a, b, c, O, H, piv, k, per_prime, prof))
    print("  %d mapped complex fields with H > 1, %.1f s"
          % (len(mapped), time.time() - t0))
    print("  C2: %d profile failures, %d order failures, %d span rows not "
          "reduced to zero, %d order-1 disagreements over %d places"
          % (prof_bad, ord_bad, span_bad, agree_bad, n_place))
    print("  the profiles found, as h: {order: count} x fields --")
    for (H, key) in sorted(seen):
        print("    h = %d  %-28s  %d fields"
              % (H, "{" + ", ".join("%d:%d" % kv for kv in key) + "}",
                 seen[(H, key)]))
    ok(prof_bad == 0, "%d fields failed the profile control" % prof_bad)
    ok(ord_bad == 0, "%d fields carried an order not dividing h" % ord_bad)
    ok(span_bad == 0, "%d span rows did not reduce to zero" % span_bad)
    ok(agree_bad == 0, "%d order-1 disagreements" % agree_bad)
    ok(n_place > 0, "no places read")
    return mapped


def regime_of(per_prime, piv, k, H):
    """The parent's field classification: 'A' everywhere but h = 3, where
    a field reads 'M', 'D' or 'X' by its own equal-class fraction."""
    if H != 3:
        return 'A'
    ns = neq = 0
    for (p, kd, vecs) in per_prime:
        if kd != 'split' or len(vecs) != 3 or any(v is None for v in vecs):
            continue
        ns += 1
        if (ST.same_class(vecs[0], vecs[1], piv, k)
                and ST.same_class(vecs[0], vecs[2], piv, k)):
            neq += 1
    if ns < MIN_SPLIT:
        return 'X'
    return 'D' if float(neq) / ns >= HIGH_FRAC else 'M'


def walk(mapped):
    """One pass over the mapped population. Returns (cells, drop), where
    cells maps (h, regime, bin) to observed and expected order counts for
    the partial primes plus the split-side counters S6 reads."""
    cells = {}
    bad = [0]
    per_field = []
    drop = {'split': 0, 'partial': 0}
    t0 = time.time()
    for (d, cx, a, b, c, O, H, piv, k, per_prime, prof) in mapped:
        reg = regime_of(per_prime, piv, k, H)
        mine = {}
        for (p, kd, vecs) in per_prime:
            bi = bin_of(p)
            if bi is None:
                continue
            if kd == 'partial' and len(vecs) != 1:
                bad[0] += 1
            if kd == 'split' and len(vecs) != 3:
                bad[0] += 1
            if any(v is None for v in vecs):
                drop[kd] = drop.get(kd, 0) + 1
                continue
            cell = cells.setdefault((H, reg, bi), dict(
                obs={}, exp={}, var={}, n=0, nsplit=0, neq=0, neqp=0, nnone=0))
            if kd == 'partial' and len(vecs) == 1:
                o = class_order(vecs[0], piv, H)
                cell['obs'][o] = cell['obs'].get(o, 0) + 1
                cell['n'] += 1
                for dd, cnt in prof.items():
                    q = float(cnt) / H
                    cell['exp'][dd] = cell['exp'].get(dd, 0.0) + q
                    cell['var'][dd] = cell['var'].get(dd, 0.0) + q * (1 - q)
                q1 = float(prof.get(1, 0)) / H
                m = mine.setdefault(bi, [0, 0.0, 0.0])
                m[0] += 1 if o == 1 else 0
                m[1] += q1
                m[2] += q1 * (1 - q1)
            elif kd == 'split' and len(vecs) == 3:
                cell['nsplit'] += 1
                if not any(ST.is_principal(v, piv, k) for v in vecs):
                    cell['nnone'] += 1
                if (ST.same_class(vecs[0], vecs[1], piv, k)
                        and ST.same_class(vecs[0], vecs[2], piv, k)):
                    cell['neq'] += 1
                    if ST.is_principal(vecs[0], piv, k):
                        cell['neqp'] += 1
        for bi, m in mine.items():
            per_field.append((H, bi, m[0], m[1], m[2]))
    print("  the mapped population walked in %.1f s, %d cells"
          % (time.time() - t0, len(cells)))
    print("  C3: %d vector lists of the wrong length over the population"
          % bad[0])
    print("  C4: places dropped by the map -- %d split, %d partial"
          % (drop['split'], drop['partial']))
    ok(bad[0] == 0, "%d vector lists of the wrong length" % bad[0])
    return cells, per_field


def strata_of(cells):
    """The class numbers the population actually holds. Declared as a
    tuple in the first version of this file, which silently dropped the
    h = 8 fields from every per-stratum row while the pooled rows kept
    them -- so it is read off the walk instead."""
    return sorted(set(h for (h, r, b) in cells))


def merge(cells, h=None, reg=None, bins=None):
    tot = dict(obs={}, exp={}, var={}, n=0, nsplit=0, neq=0, neqp=0, nnone=0)
    for (hh, rr, bb), cell in cells.items():
        if h is not None and hh != h:
            continue
        if reg is not None and rr != reg:
            continue
        if bins is not None and bb not in bins:
            continue
        for key in ('obs', 'exp', 'var'):
            for dd, x in cell[key].items():
                tot[key][dd] = tot[key].get(dd, 0) + x
        for key in ('n', 'nsplit', 'neq', 'neqp', 'nnone'):
            tot[key] += cell[key]
    return tot


def zscore(tot, d):
    e = tot['exp'].get(d, 0.0)
    v = tot['var'].get(d, 0.0)
    if v <= 0:
        return None
    return (tot['obs'].get(d, 0) - e) / (v ** 0.5)


def print_orders(tot, label):
    ds = sorted(set(list(tot['obs']) + list(tot['exp'])))
    parts = []
    for d in ds:
        z = zscore(tot, d)
        parts.append("ord %d: %d/%.1f%s"
                     % (d, tot['obs'].get(d, 0), tot['exp'].get(d, 0.0),
                        "" if z is None else " z=%+.2f" % z))
    print("  %-22s n = %-6d %s" % (label, tot['n'], "  ".join(parts)))


def s4_orders(cells):
    section("S4  P1 THE ORDER DISTRIBUTION OF A TRANSPOSITION PLACE, "
            "P3 THE INDEX-2 BRANCH")
    top = len(BIN_EDGES) - 2
    strata = strata_of(cells)
    print("  every stratum, pooled over all bins --")
    worst = (0.0, None)
    for h in strata:
        tot = merge(cells, h=h)
        if tot['n'] == 0:
            continue
        print_orders(tot, "h = %d  all bins" % h)
    print()
    print("  the top prime bin (%s), where the derivation is tested --"
          % bin_name(top))
    for h in strata:
        tot = merge(cells, h=h, bins={top})
        if tot['n'] == 0:
            continue
        print_orders(tot, "h = %d" % h)
        for d in tot['exp']:
            if tot['exp'][d] < MIN_CELL:
                continue
            z = zscore(tot, d)
            if z is not None and abs(z) > worst[0]:
                worst = (abs(z), (h, d, z))
    tot_all = merge(cells, bins={top})
    print_orders(tot_all, "pooled")
    frozen = (0.0, None)
    for d in tot_all['exp']:
        if tot_all['exp'][d] >= MIN_CELL:
            z = zscore(tot_all, d)
            if z is not None and abs(z) > frozen[0]:
                frozen = (abs(z), (d, z))
    print()
    # P1 was frozen on the POOLED cells; the per-stratum scan is finer
    # than the observable and is reported as a separate line, never as
    # the kill.
    if frozen[1] is None:
        print("  P1: no pooled top-bin cell reached the %d-count floor"
              % MIN_CELL)
    else:
        dd, zz = frozen[1]
        print("  P1 as frozen (POOLED top bin): the furthest cell is "
              "order %d at z = %+.2f, against the kill at %.1f"
              % (dd, zz, Z_KILL))
    if worst[1] is not None:
        hh, dd, zz = worst[1]
        print("  finer than the observable, not the kill: the furthest "
              "PER-STRATUM cell is h = %d order %d at z = %+.2f"
              % (hh, dd, zz))
    print()
    n_even = 0
    for h in strata:
        if h % 2:
            continue
        tot = merge(cells, h=h)
        if tot['n'] < 100:
            continue
        n_even += 1
        print("  P3: h = %d holds %d partial primes, %d of them principal"
              % (h, tot['n'], tot['obs'].get(1, 0)))
        ok(tot['obs'].get(1, 0) > 0,
           "h = %d realizes the index-2 branch" % h)
    ok(n_even > 0, "no even stratum reached the P3 floor")
    return worst


def s5_location(cells):
    section("S5  P2 WHERE THE DEPARTURE SITS, P4 THE REGIME COMPARISON")
    print("  the principal cell by prime bin, per stratum --")
    neg = tot_cell = 0
    for h in strata_of(cells):
        row = []
        for bi in range(len(BIN_EDGES) - 1):
            tot = merge(cells, h=h, bins={bi})
            if tot['n'] == 0:
                continue
            z = zscore(tot, 1)
            if z is not None:
                tot_cell += 1
                neg += 1 if z < 0 else 0
            row.append("%s: %d/%.1f%s"
                       % (bin_name(bi), tot['obs'].get(1, 0),
                          tot['exp'].get(1, 0.0),
                          "" if z is None else " z=%+.2f" % z))
        if row:
            print("  h = %d  %s" % (h, "   ".join(row)))
    print("  the principal cell reads short at %d of the %d "
          "stratum-by-bin cells" % (neg, tot_cell))
    print()
    print("  pooled over every stratum, which is the corpus's own read --")
    for bi in range(len(BIN_EDGES) - 1):
        tot = merge(cells, bins={bi})
        if tot['n'] == 0:
            continue
        z = zscore(tot, 1)
        print("  %-10s n = %-6d principal %d against %.1f%s"
              % (bin_name(bi), tot['n'], tot['obs'].get(1, 0),
                 tot['exp'].get(1, 0.0),
                 "" if z is None else ", z = %+.2f" % z))
    print()
    print("  P4: h = 3, the degenerate fields against the others --")
    top = len(BIN_EDGES) - 2
    out = {}
    for reg in ('D', 'M'):
        tot = merge(cells, h=3, reg=reg)
        hi = merge(cells, h=3, reg=reg, bins={top - 1, top})
        out[reg] = (tot, hi)
        for lab, t in (("all bins", tot), ("top two", hi)):
            if t['n'] == 0:
                continue
            z = zscore(t, 1)
            print("  R = %s  %-9s n = %-5d principal %d against %.1f%s"
                  % (reg, lab, t['n'], t['obs'].get(1, 0),
                     t['exp'].get(1, 0.0),
                     "" if z is None else ", z = %+.2f" % z))
    dt, dh = out.get('D', (None, None))
    mt, mh = out.get('M', (None, None))
    if dt and mt and dt['n'] and mt['n']:
        pd = float(dt['obs'].get(1, 0)) / dt['n']
        pm = float(mt['obs'].get(1, 0)) / mt['n']
        pp = (float(dt['obs'].get(1, 0) + mt['obs'].get(1, 0))
              / (dt['n'] + mt['n']))
        se = (pp * (1 - pp) * (1.0 / dt['n'] + 1.0 / mt['n'])) ** 0.5
        z = (pd - pm) / se if se > 0 else None
        print("  the two shares are %.4f and %.4f, difference z = %s"
              % (pd, pm, "n/a" if z is None else "%+.2f" % z))
    return out


def s6_split_marginal(cells):
    section("S6  P5 THE SPLIT SIDE'S MARGINAL AT THE DEGENERATE FIELDS")
    top = len(BIN_EDGES) - 2
    for lab, bins in (("all bins", None), ("top two", {top - 1, top})):
        tot = merge(cells, h=3, reg='D', bins=bins)
        if tot['nsplit'] == 0:
            continue
        exp = tot['neq'] / 3.0
        var = tot['neq'] * (1.0 / 3.0) * (2.0 / 3.0)
        z = (tot['neqp'] - exp) / (var ** 0.5) if var > 0 else None
        print("  %-9s %d split primes, %d all-equal, %d of those principal "
              "against %.1f%s"
              % (lab, tot['nsplit'], tot['neq'], tot['neqp'], exp,
                 "" if z is None else ", z = %+.2f" % z))
    print("  the all-equal triples are the independent draws here: one "
          "class per prime, uniform on Cl under the derivation.")
    print()
    print("  C6, added at the audit: the parent's own C3 denominator "
          "re-counted, since 892 is quoted BOTH as the degenerate "
          "regime's")
    print("  split total and as the split primes carrying no principal "
          "place, and the two cannot both be it --")
    whole = merge(cells, h=3)
    dd = merge(cells, h=3, reg='D')
    mm = merge(cells, h=3, reg='M')
    print("    h = 3 whole stratum: %d split, %d with no principal place"
          % (whole['nsplit'], whole['nnone']))
    print("    R = D: %d split, %d none;  R = M: %d split, %d none"
          % (dd['nsplit'], dd['nnone'], mm['nsplit'], mm['nnone']))
    ok(whole['nnone'] <= whole['nsplit'], "more none than split")


def s7_dispersion(cells, per_field, worst):
    """C5, added at the audit: the kill statistic's own denominator.

    Every z above prices a pooled cell with the sum of per-prime
    Bernoulli variances, which assumes the primes of ONE FIELD are
    independent -- and the corpus's own reading of the SPLIT side finds
    that count UNDER-dispersed, index 0.12 to 0.46
    (explore_cubic_class_map.py). Under-dispersion makes that denominator
    too big and every |z| above too small, which is the direction that
    turns a survive into a kill, so it is measured rather than assumed.
    The instrument is the per-field standardized residual: under
    independence its spread across fields is 1 whatever the shortfall
    does to its centre, so the sample variance around the sample mean
    isolates dispersion from the effect. It is read on the ORDER-1 cell
    and nothing here extends it to the others."""
    section("S7  C5 THE DENOMINATOR -- IS THE PARTIAL COUNT DISPERSED "
            "AS THE KILL ASSUMES?")
    top = len(BIN_EDGES) - 2
    for lab, bins in (("top bin", {top}), ("all bins", None)):
        xs = []
        for (H, bi, o1, e1, v1) in per_field:
            if bins is not None and bi not in bins:
                continue
            if v1 < 4.0:
                continue
            xs.append((o1 - e1) / (v1 ** 0.5))
        if len(xs) < 10:
            print("  %-9s too few field-bins to read" % lab)
            continue
        mu = sum(xs) / len(xs)
        var = sum((x - mu) ** 2 for x in xs) / (len(xs) - 1)
        print("  %-9s %d field-bins, mean residual %+.3f, spread %.3f "
              "against 1.000 under independence"
              % (lab, len(xs), mu, var ** 0.5))
        if lab == "top bin" and worst[1] is not None:
            hh, dd, zz = worst[1]
            print("    the furthest PER-STRATUM top-bin cell rescaled by "
                  "that spread: z = %+.2f becomes %+.2f, against the kill "
                  "at %.1f -- which was frozen on the POOLED cell, S4's "
                  "own line" % (zz, zz / (var ** 0.5), Z_KILL))


def main():
    t0 = time.time()
    recs = s1_population()
    s2_pin(recs)
    mapped = s3_profiles(recs)
    section("THE WALK")
    cells, per_field = walk(mapped)
    worst = s4_orders(cells)
    s5_location(cells)
    s6_split_marginal(cells)
    s7_dispersion(cells, per_field, worst)
    section("SUMMARY")
    print("  %d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
