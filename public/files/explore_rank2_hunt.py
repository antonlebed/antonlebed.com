r"""explore_rank2_hunt.py -- THE FIRST FIELD OF 3-RANK 2, AND WHETHER ITS
GENERATED SUBGROUP IS Delta. The complex cubic box widened to |d| <= 50000
to buy a class group with Z/3 x Z/3 inside it, and the degeneracy
condition rebuilt as the LATTICE MEMBERSHIP it is, because the scalar
form the corpus has been running is meaningless there.
(Sibling of explore_noncyclic_level.py, whose walk shape, group reader and
generated-subgroup test this file reuses; of explore_image_share.py, whose
F4 census is the control this file's sub-box must reprint and whose F6
bracket is the supply this file's cap was bought from; and of
explore_ceiling_topband.py, whose wide class reading this file widens
again and whose T5 sieve guard is the thing that has to move first.)

THE QUESTION.

The degenerate image is the subgroup Delta of N = {(a, b, c) in Cl^3 :
a + b + c = 0} cut out by b_i - b_j in 3Cl, and [N : Delta] = 3^r for r
the 3-rank of Cl (property, derived: the map (a, b, c) -> (a - b, b - c)
into (Cl/3Cl)^2 has it as kernel and lands onto the diagonal). Every
measurement the
corpus has of that index was taken in a box where r <= 1 at every field
(explore_image_share.py F4: 769 trivial 3-parts, 484 at Z/3, 30 at Z/9,
nothing else -- that census is short by two fields on the reading below,
F7 and S3b, and the correction touches neither the Z/3 row nor the Z/9
one). At r <= 1 the only proper subgroup of N the h/3 test can
name IS Delta, so the derived index law and the IDENTIFICATION riding on
it -- that a field generating a proper subgroup generates Delta -- are
the same statement and no measurement separates them. At r = 2 they
part: an index-3 subgroup of N strictly CONTAINS the index-9 Delta.

So: find a complex cubic field whose class group has 3-rank 2, compute
the subgroup its mapped split triples generate, and read whether that
subgroup has index 9 in N or index 3.

Index 9 says the identification holds where it could first have failed
and the scalar h/3 test is the cyclic-3-part reduction of a subgroup
law. Index 3 leaves the derivation untouched -- [N : Delta] = 3^r is
proved -- and refutes the identification: degeneracy would then be a
strictly WEAKER condition than agreement in Cl/3Cl and would need a new
name.

WHOSE VOCABULARY THE SUSPICION IS IN, asked before anything was frozen.
The parents say NON-CYCLIC where this file says 3-RANK 2, and they are
different conditions: Z/6 x Z/2 is non-cyclic at r = 1 and this file
has no use for it. Nothing here is keyed by cyclicity, by h being 9, or
by the 3-part having order 9 -- the last being the SUPPLY population and
not the target. "Degenerate" is likewise the parents' word for the
output of a SCALAR test; every use of it below names which test
produced it, because the whole point is that the two can part.

THE HAND-ATTACK, on paper before any engine code.

 (a) THE SCALAR TEST IS THE LATTICE TEST AT 3-RANK <= 1, DERIVED. Write
     Cl = A (+) T with T the 3-part and A its 3-coprime complement, and
     h = 3^e u with u = |A|. Then h/3 = 3^(e-1) u. Multiplication by
     h/3 kills A entirely (u divides h/3), and on T it is multiplication
     by 3^(e-1) times the unit u. With T cyclic of order 3^e, the kernel
     of 3^(e-1) on T is 3T. So ker(h/3) = A (+) 3T. And 3Cl = 3A (+) 3T
     = A (+) 3T, since 3 is invertible on A. The two coincide. THE
     DERIVATION USES CYCLICITY OF T AT EXACTLY ONE STEP, where the
     agreement has until now been carried as a rule in range over 514
     fields; P1 below is the check that the derivation and the range
     agree, and if it passes the claim owes a tier.

 (b) AT 3-RANK 2 THE SCALAR TEST IS VACUOUS, AND THAT IS WHY IT CANNOT
     BE THE INSTRUMENT. With T = Z/3^s x Z/3^t and e = s + t, h/3 acts
     on T as 3^(e-1) times a unit. AND THAT KILLS T AT EVERY 3-RANK
     ABOVE 1, not only at the cheapest supply: r >= 2 forces s >= 1 and
     t >= 1, so e - 1 = s + t - 1 >= t and 3^(e-1) annihilates Z/3^t and
     a fortiori Z/3^s. At T = Z/3 x Z/3 it is multiplication by 3 and
     the arithmetic is visible; the general case is the same line. So
     ker(h/3) = Cl, the whole group, and the scalar test declares EVERY
     field of 3-rank 2 or more degenerate regardless of what its split
     triples do. 3Cl there is A alone, of index 3^r. P2
     freezes that as an observable: at every r = 2 field with
     T = Z/3 x Z/3 the scalar test must return degenerate, and the
     lattice test need not.

 (c) THE LATTICE FORM, WITH NO SCALAR IN IT. Cl = Z^k / L for L the
     pivot lattice the class map returns. 3Cl is the image of
     multiplication by 3, which as a sublattice of Z^k containing L is
     spanned by L's rows together with 3 e_1 ... 3 e_k. So b_i - b_j in
     3Cl is one echelon of those k + |L| rows and one in-span test per
     pair per split prime -- explore_cubic_class_map.py's echelon and
     in_span, unmodified. The echelon is per FIELD and not per prime,
     so the cost is one extra echelon on k columns per field.

 (d) THE INDEX IS READ OFF AN ORDER, AND THE ROUTINE'S NAME LIES. The
     sibling's generated_index returns h^2 / |Z^2k / span|, which is the
     ORDER of the generated subgroup and not its index. Index in N is
     h^2 / that order. Every print below names the ORDER and the INDEX
     separately so the two can never be read for each other, and the
     r = 2 reading is stated as the index.

 (e) THE GUARD THAT WILL FIRE FIRST, AND WHY IT IS NOT PARANOIA. The
     wide box's maximal-order routine asserts the ORDER's trace-form
     discriminant under 4 x 10^6 behind an index-prime sieve built to
     2000, and that pair is sound exactly when p^2 dividing d0 forces
     p <= 2000, i.e. |d0| < 4 x 10^6. Widening the cap raises the Hunter
     box and therefore raises max |d0|; the parent's own comment records
     1,849,700 at cap 24000. Both numbers move together or the sieve
     silently misses an index prime and returns a NON-maximal order,
     whose class group is not the field's. This file installs its own
     routine with the sieve at 10^4 and the assert at 10^8, which is the
     same soundness condition (p^2 dividing d0 with |d0| < 10^8 forces
     p <= 10^4), and PRINTS the observed maximum so the next widening
     has a measurement instead of an extrapolation. The swap is
     declared as T2.

 (f) A REPRINT IS THE ONLY CONTROL THAT CATCHES A WIDENED SIEVE GOING
     WRONG. A wrong index prime does not crash; it returns a smaller
     order with a bigger class number. The fields with |d| <= 24000
     inside the widened box are the SAME fields the sibling read, so
     their 3-part census must reprint F4 exactly -- 769 trivial, 484 at
     Z/3, 30 at Z/9, 0 else -- and their h > 1 count must reprint 1283.
     P3 runs it and it runs BEFORE any widened-box result is read.

 (g) THE SUPPLY IS A PREDICTION AND NOT AN ASSUMPTION. F6 refits the
     order-9 supply against the FIELD COUNT rather than the cap, giving
     ~0.00019 x (fields)^1.670, and the cap was chosen from it. The
     count of h > 1 fields and the count of order-9 fields at this cap
     are therefore both predictions this run can miss (P4, P5), and a
     miss on the first is what a miss on the second would otherwise be
     blamed on.

 (h) WHAT A ZERO IS WORTH, decided before the run so it cannot be
     decided by the result. The box carries 30 order-9 fields and 0 at
     Z/3 x Z/3. If the widened box carries n order-9 fields and still 0
     at Z/3 x Z/3, the exact-binomial upper bound on the Z/3 x Z/3
     fraction among order-9 fields at 95% is 1 - 0.05^(1/n): 0.095 at
     n = 30, and 0.029 at n = 100. A second empty box is a tightened
     bound and is a result; it is not a failure. S8 prints it
     either way, from the count the run actually got.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 THE CLASS READING IS THE TOPBAND SIBLING'S, WIDENED BY REBINDING ITS
    MODULE-LEVEL CAP. explore_ceiling_topband.wide_class_reading reads
    the parents' base box plus the increment to WIDE_CAP under its own
    T4 unresolved-share kill and T8 pin escalation; this file sets that
    global to its own cap and calls it. Its population, its exclusion
    policy and its pin escalation are taken whole, so the T4 kill still
    guards the widened box. ONE THING INSIDE IT IS NOT TAKEN WHOLE and
    T7 is that flag: the ladder's ACCEPTANCE RULE is replaced. Read T1
    as "the reading is the sibling's except where T7 says otherwise",
    never as "the reading is untouched".

 T2 THE MAXIMAL-ORDER ROUTINE IS SWAPPED A SECOND TIME, and the swap is
    an override of the sibling's own override: importing topband installs
    its cap-24000 routine into explore_cubic_principal, and this file
    installs its own after the import. A reader looking for which
    routine ran must read the LAST assignment, not the first. (e) has
    the arithmetic.

 T3 THE WALK IS THIS FILE'S AND IS LEANER THAN THE SIBLING'S. The
    sibling's read_population also accumulates the level cells for
    every stratum; nothing here reads a level, so the walk keeps only
    (|d|, h, invariant factors, mapped split count, the two degeneracy
    verdicts, the generated order). The group reader (snf, factors_of,
    torsion, group_name), the split-prime reader (read_field) and the
    generated-subgroup test are IMPORTED and not reimplemented.
    AND LEANER MEANS A CONTROL WAS DROPPED, which is the half of
    "leaner" that a flag has to say: the sibling's walk also counts
    split triples off the SUM-ZERO locus, and that count is what
    licenses reading the sum-zero group in the (a, b) coordinates at
    all. It is not run over this box, only at the two fields the verdict
    rests on (C5, both zero). WHICH QUANTITIES THAT TOUCHES IS NARROWER
    THAN IT SOUNDS, and the narrowing is the point: the 3-part census
    reads the relation lattice through factors_of and never looks at a
    triple, so it does not depend on the control at all, and the two
    degeneracy tests read DIFFERENCES b_i - b_j, which need no sum-zero
    either. The one quantity that does need it is the GENERATED SUBGROUP
    ORDER, which reads (b_0, b_1) as coordinates on the sum-zero group
    -- and that order is read nowhere in this file except at the hit
    fields, where C5 runs. So the walk stores an uncontrolled order per
    field and no section consumes one.

 T4 THE PARENTS' BAR VALUE STANDS AND ITS STATISTIC DOES NOT, which is
    worth separating because "the same bar" reads as both. MIN_SPLIT is
    the parents' 10, the prime cap is theirs, the unresolved-field
    exclusions are theirs. But the QUANTITY the 10 is applied to is this
    file's: the parents count split primes inside their binned window,
    through the level walk they run and this file does not, while this
    file counts every fully mapped split prime in the split reading.
    The two can differ, and mine is the matched one -- it counts exactly
    the triples fed to the subgroup test, which is what the bar exists
    to make trustworthy. The substitution is harmless here and the print
    says why: 0 fields fall under the bar in this box, and the two
    fields the verdict rests on carry 20 and 31. A field under the bar
    is counted and never classified.

 T5 WHAT IS MEASURED IS THE SUBGROUP THE OBSERVED SPLIT TRIPLES
    GENERATE, a lower bound on the Galois image and not the image.
    The bound on reading one as the other is a count and not a rate:
    a full image putting all of a field's ten-or-more triples inside
    one proper subgroup has probability under 4 x 3^-10. Every
    "index" below is the index of that generated subgroup in N.

 T6 THIS FILE'S CHECKPOINT IS ITS OWN AND CARRIES ITS CAP. R2_CKPT is
    keyed by the cap it was written at and a reload under a different
    cap is refused, which is the pin the sibling's T6 asks for. The
    sibling's NCL_CKPT is a different box and is never read here.

 T7 THE CLASS READING'S ACCEPTANCE RULE IS REPLACED, AND THIS IS THE
    ONE PLACE THIS FILE DEPARTS FROM T1. The sibling's read_one accepts
    an order as soon as two consecutive rungs of the relation ladder
    agree. Two STARVED rungs can agree with each other, and the widened
    box makes that routine rather than rare: it admits polynomials with
    larger coefficients which sort BEFORE the small ones (s1 = 0 ahead
    of s1 = 1) and become the field's representative, and a large
    polynomial's harvest inside a fixed box finds fewer relations. The
    specimen is |d| = 9187, whose widened representative reads 4, 4, 2
    across the three rungs where its old representative reads 2, 2, 2.
    Relations are GENUINE, so a harvest can only be missing them and the
    computed order is an upper bound on h that falls as the box grows;
    the MINIMUM over the ladder is therefore the sound reading, the
    early return is not, and the fix is not a tolerance. S2b counts
    every field the two rules disagree at, which is what the defect's
    lineage into the parents costs.

THE PREDICTIONS, frozen before any engine code.

 P0 THE REHEARSAL PASSES (positive control, read before anything else).
    Synthetic lattices with known class groups -- including three with
    3-rank 2, which no field in the old box realizes -- must give the
    right invariant factors, the right |Cl[3]|, the right index of 3Cl
    in Cl (3^r), and a lattice test that agrees with a hand-computed
    membership. Predicted: 0 mismatches.

 P1 THE SCALAR TEST AND THE LATTICE TEST AGREE AT 3-RANK <= 1.
    Predicted: 0 fields with 3 dividing h, r <= 1 and at least MIN_SPLIT
    mapped split primes where the two verdicts differ. Derivation (a).

 P2 THE SCALAR TEST IS VACUOUS AT T = Z/3 x Z/3. Predicted: every such
    field the run finds reads scalar-degenerate. Derivation (b). Vacuous
    if the count is 0, and printed as vacuous rather than as a pass.
    THE CODE TESTS THE GENERAL CASE AND THIS NAMES THE SPECIAL ONE: S4
    keys on 3-rank >= 2, which (b) licenses, while the prediction is
    written at Z/3 x Z/3 because that is the only group the priced
    supply could deliver. In this box the two populations are the same
    two fields and nothing reported turns on the difference; in a box
    carrying a Z/3 x Z/9 they part, and it is the CODE that is right.

 P3 THE SUB-BOX REPRINTS THE SIBLING'S CENSUS. Predicted: over the
    fields with |d| <= 24000, exactly 1283 with h > 1, and 3-parts
    769 trivial / 484 Z/3 / 30 Z/9 / 0 anything else. (f).

 P4 THE h > 1 SUPPLY LANDS IN THE BRACKET. Predicted: between 2670 and
    3270 fields with h > 1 at cap 50000, the two growth assumptions
    F6 brackets.

 P5 THE ORDER-9 SUPPLY LANDS IN ITS BRACKET. Predicted: between 100 and
    140 fields whose 3-part has order 9. A miss here with P4 passing is
    a miss on the structural fit; a miss with P4 missing is a miss on
    the population and says nothing about the fit.

 P6 THE HUNT IS A COIN FLIP AND IS FROZEN AS A COUNT. Predicted: at
    least 1 field with 3-rank 2. The prior bounding it is one-sided --
    F5 removed the 1/|Aut| weighting that would have priced it -- so a
    0 here is a bound and not a surprise, and (h) fixes what the bound
    is worth before the count is seen.

 P7 THE FIRST r = 2 FIELD GENERATES Delta. Predicted: its generated
    subgroup has order h^2/9 and index 9 in N. The rival, index 3, is
    the reading that refutes the identification. Read only if P6's
    count is positive, and read at EVERY r = 2 field the run finds, not
    only the first.

RESOURCE ENVELOPE, named before the run. One process, CPython, no BLAS.
The cap-24000 sibling cost 739 s (53 s enumerating, 584 s class reading,
102 s walking) at a peak of 125.5 MB. The field count over this range was
measured growing as ~cap^1.24, so cap 50000 is about 2.55 times the
population: roughly 31 minutes and a projected peak near 320 MB, under
memwatch's 512 MB default. THIS IS A >10-MINUTE RUN AND IT IS NECESSARY:
the question is about a field the existing box does not contain, so
nothing cheaper than enlarging the box can be asked. The pipeline is
REHEARSED END TO END at cap 6000 first -- the parents' own box, every
stage exercised in minutes -- so a kill costs minutes and not half an
hour, and the widened walk checkpoints so no later reading pays it
again.

 F1 THE IDENTIFICATION IS FALSE, AND ONE FIELD IN TWO KILLS IT
    (observation, the two 3-rank 2 fields in the box; S6, S7, attested
    through every representative at S7c). The box
    holds exactly two fields with Cl = Z/3 x Z/3, and they part:

        |d| = 24843, h = 9, 20 split primes: generated order 9,
              index 9 in N -- the subgroup IS Delta;
        |d| = 47628, h = 9, 31 split primes: generated order 27,
              index 3 in N -- a subgroup strictly CONTAINING Delta.

    THE CONTAINMENT IS MEASURED AND NOT INFERRED (S7b). The order alone
    does not give it: N/Delta is (Z/3)^2 at r = 2, and an index-3
    subgroup of N corresponds to a subgroup of N/Delta only if it
    contains Delta, so a subgroup of order 27 could have met Delta in
    anything. Delta is built as its own lattice -- the diagonal together
    with (3Cl, 0), both conditions cutting it out of N reducing to
    a - b in 3Cl -- and it lies inside the generated subgroup at both
    fields, its own order reproducing h^2/3^r at both as the control
    C4. AND |d| IS NOT A LOCATOR: cubic fields can share a
    discriminant, and |d| = 47628 carries four of them (h = 3, 6, 9 and
    3 again). The field meant here is the one with h = 9, which is
    unique at that discriminant; S7b keys on the 3-rank for the same
    reason.

    [N : Delta] = 3^r is proved and nothing here touches it. What dies
    is the IDENTIFICATION that r <= 1 could never test apart from it:
    that a field generating a PROPER subgroup of N generates Delta. At
    47628 the generated subgroup is proper and is not Delta. So
    "degenerate" as the corpus's test reports it is a STRICTLY WEAKER
    condition than agreement in Cl/3Cl, and the two names are not one
    name. A single counterexample settles it; the other field's
    agreement is why the claim survived to be tested.

 F2 THE SCALAR TEST CANNOT SEE THE DIFFERENCE, AS DERIVED (property,
    (b); the two fields, S6). Both fields read scalar-degenerate --
    at any 3-rank above 1 the multiplier h/3 annihilates the whole
    3-part, so the test is vacuously true whatever the split triples do,
    and Z/3 x Z/3 is only the smallest group where that bites. The
    LATTICE test separates them: degenerate at 24843, NOT degenerate at
    47628, agreeing with the generated order at both. So the corpus's
    scalar test does not merely lack a proof above 3-rank 1; it returns
    the wrong answer at the first field where a wrong answer is
    possible, and it would have assigned 47628 a share three times too
    large. It is the parents' h = 9 slip again in KIND and not in
    direction -- a denominator taken from an assumed image instead of
    read off the measured one -- and the direction is the opposite: the
    nine degenerate fields were given a share three times too SMALL. The
    stratum POOLED on that share read 1.359; split out onto the share
    they are owed, the nine read 0.674 against the twenty-one's 1.101 --
    a level divided by three exactly where the share was multiplied by
    it, and 1.359 is the pooled figure and never the nine's own. A share
    of 1 against the 1/3 that 47628's order of 27 owes moves a level the
    other way. Nothing the corpus currently prints moves,
    the levels being keyed on the generated ORDER already; what would
    have moved is a reading keyed on the scalar test.

 F3 THE SCALAR FORM IS THE LATTICE FORM AT 3-RANK <= 1, NOW DERIVED AND
    RE-MEASURED (property, derived in (a); 0 disagreements over the 1365
    fields with 3 | h, r <= 1 and ten or more mapped split primes, S4).
    The agreement has been carried as a rule in range over 514 fields;
    (a) derives it in four lines and the range measured against it
    grows by a factor of 2.66. The derivation uses
    cyclicity of the 3-part at exactly one step, which is what F2 shows
    is load-bearing rather than incidental.

 F4 THE BOX'S 3-PART CENSUS, AND THE FIRST NON-CYCLIC ONE THE CORPUS HAS
    (rule in range, the 3133 complex fields with h > 1 to |d| <= 50000;
    S5): 1766 with a trivial 3-part, 1277 at Z/3, 88 at Z/9 and 2 at
    Z/3 x Z/3. The sibling's box carried no non-cyclic 3-part at all, so
    r <= 1 there was a fact about the whole population; here it is not.
    THE ROWS ARE ONE-SIDED AND NOT EXACT, which follows from F7's
    algebra and is stated here because a census reads as exact: a
    settled order is a MULTIPLE of h, so Cl is a QUOTIENT of the group
    read, and a field can only ever be read at a 3-part its true one
    divides. The trivial row is therefore a floor -- everything in it
    genuinely has no 3-torsion, since 3 dividing nothing above divides
    nothing below -- while the Z/3 row and the order-9 row are
    CEILINGS, a field read at Z/3 being possibly trivial and one read at
    order 9 possibly smaller.

 F4b THE 3-RANK 2 COUNT IS THE ONE ROW THAT IS EXACT, and it is exact
    in the direction that matters (property, derived; the two fields
    attested at S7c). A quotient's 3-rank never exceeds its group's, so
    a field of true 3-rank 2 must be READ at 3-rank 2 or more and a shy
    reading cannot hide one: the hunt admits false positives and no
    false negatives. S7c removes the false positives at the two fields
    found, every representative of each settling at the same order and
    the same group. So the box holds exactly two fields of 3-rank 2 --
    not at most two, and not two observed.

 F5 THE ORDER-9 SUPPLY FIT OVERESTIMATES, AND THE POPULATION FIT DOES
    NOT (observation; S5, P4 against P5). The h > 1 supply lands at 3133
    inside the predicted 2670..3270, so the population is where it was
    priced. The order-9 supply lands at 90 against a predicted 100..140
    -- a miss with the population fit passing, which by the freeze's own
    reading is a miss on the STRUCTURAL fit and not on the box. The
    ~(fields)^1.670 exponent is too steep over this range, and F4's
    one-sidedness sharpens the miss rather than softening it: 90 is a
    CEILING on the order-9 supply, so the true supply is at most 90
    against a prediction of 100 to 140.

 F6 THE 1/|Aut| WEIGHTING IS FURTHER OUT, AND NOW AGAINST A MEASUREMENT
    RATHER THAN A ZERO (observation; S8). Among order-9 fields the
    weighting puts 1/9 of the mass on Z/3 x Z/3, expecting 10 of the 90
    here; the box has 2, a fraction of 0.022. The sibling's box could
    only bound the fraction from above at 0.095; this one measures it,
    at P(X <= 2) = 0.0019 against the weighting.
    THE FRACTION IS A FLOOR AND NOT A POINT, because its two halves are
    one-sided in opposite ways: the numerator is EXACT by F4b, while the
    denominator is a CEILING by F4, so the true fraction is at least
    2/90 and rises if any of the 90 is really smaller. THE SLACK IS
    BOUNDED AND IT IS SMALL: an order-9 reading is wrong only where the
    ladder was shy, which S2b measures at 11 of 4825 runs, so on that
    rate under a tenth of one field among the 90 is misplaced and the
    denominator cannot move enough to reach 1/9 -- the weighting would
    need the true count near 18. The comparison stands; it is the
    ARITHMETIC of the fraction that needed the qualifier, not the
    verdict.

 F7 THE CLASS READING'S ACCEPTANCE RULE IS NOT A CONVERGENCE TEST,
    AND THIS IS THE SHAPE'S THIRD FIRING RATHER THAN ITS FIRST
    (property, derived; the count measured at S2b, the corpus damage at
    S3b). The sibling accepts an order as soon as two consecutive rungs
    of the relation ladder agree. A settled reading's Hermite order is
    the index of a sublattice of the full relation lattice, so it is a
    MULTIPLE of the true class number and not merely an upper bound on
    it -- which is the sharper statement, since it makes the truth
    DIVIDE every settled reading and a gcd across readings meaningful
    where a minimum is only monotone. Two STARVED rungs can then agree
    with each other at a common multiple. NONE OF THAT IS NEW HERE:
    explore_ceiling_realcubic.py's T7 records two rungs of one
    representative reading twice the truth while another representative
    reads it at every rung, and explore_ceiling_fourthcell.py's T9
    carries the cure -- each composite reading attested through further
    representatives, the gcd adopted when one settles at exactly it,
    the field excluded when none does -- together with the sentence
    this file rediscovered the long way, that the rung agreement is a
    property of the PRESENTATION while the class number is the field's.
    NOR WAS THE SIBLING UNAWARE: explore_ceiling_topband.py's own T3
    names this residual in its design -- "a doubly-shy lattice, short
    by the same index at two boxes, would still slip through" -- and
    names the control for it in the same breath, the base subset where
    the truth is the parent's. So what happened here is not a defect
    found in an unsuspecting rig. It is a DECLARED residual firing, in
    the population that realizes it, and being caught by exactly the
    control its own designer nominated: this file's S3 is that base
    subset, and it stopped the first widened run before a single
    science figure was read. What the run adds is the measurement --
    how often the residual fires in the complex box, and what it costs
    the census -- and the fact that the cures written for two sibling
    rigs were never carried back to this one. On this box's representative polynomials the rule
    inflates 11 of 4825 ladder runs -- |d| = 9187 reading 4, 4, 2 and
    |d| = 46891 reading 16, 16, 8 -- and REFUSES 11 more on a FULL
    ladder that the minimum resolves, |d| = 7699 reading None, None, 2.
    A further 1446 ladders this reader TRUNCATED at order 1 and they
    score neither way: it stops the moment a rung reads 1, so the rungs
    the other rule would have gone on to run were never recorded. That
    truncation is the whole difference between this count and the 76
    an earlier pass printed, which read every truncated ladder as a
    refusal -- the instrument measuring its own short-circuit and
    calling it the other rule's failure. The exposure is the widening's doing and not the
    rule's: the larger Hunter box admits large-coefficient polynomials
    which sort AHEAD of the small ones and become the field's
    representative, and a large polynomial harvests worse inside a fixed
    box. WHAT IT COST THE CORPUS IS SMALL AND IS MEASURED, NOT ARGUED
    (S3b): over the sibling's own sub-box, ZERO class numbers change --
    the difference is two fields the sibling EXCLUDED that the minimum
    resolves (|d| = 7699 at h = 2, |d| = 7771 at h = 4) against one
    (|d| = 14087) whose widened representative this reader cannot
    resolve. So the sibling's census is right where it speaks and short
    by two fields, both with a trivial 3-part: 1284 fields with h > 1
    and 770 / 484 / 30 by 3-part order, against its 1283 and
    769 / 484 / 30. The Z/3 and Z/9 rows -- the only ones the hunt
    rides on -- are untouched. AND THE LADDER MINIMUM IS A PARTIAL CURE
    AND IS NOT THE STANDING ONE: a minimum over rungs of ONE
    presentation is still a multiple of the truth if every rung of that
    presentation is shy. The standing guard is to re-read the
    science-bearing subset through a SECOND presentation outright, and
    S7c is this file paying it.

THE PREDICTIONS, WEIGHED.

 P0 PASSES: 10 synthetic groups including three at 3-rank 2, 0
    mismatches on the invariant factors, on |Cl[3]| and on [Cl : 3Cl],
    and the hand-computed memberships at Z/3 x Z/3 both right. It
    earned its place twice: it caught the index read as h/[Cl : 3Cl]
    instead of as [Cl : 3Cl] itself, before the widened run.
 P1 PASSES: 0 disagreements between the scalar and lattice tests over
    1365 fields at 3-rank <= 1. F3.
 P2 PASSES, and F2 is what the pass is worth: both 3-rank 2 fields read
    scalar-degenerate, which is the derivation's vacuity and not the
    fields agreeing about anything.
 P3 FAILS AS FROZEN, at 1284 fields against 1283. The control was
    written as an EQUALITY against a sibling whose reader this file had
    not yet found a defect in; T7 resolves fields that sibling excluded,
    so the equality could not hold once the reader was fixed. S3b is the
    DIRECTIONAL control it should have been -- every difference must be
    a field entering or leaving the resolved population and never a
    class number that changed -- and it passes with 0 unexplained. The
    frozen control still did its job: it is what stopped the first
    widened run before any science was read.
 P4 PASSES: 3133 fields with h > 1, inside 2670..3270.
 P5 FAILS: 90 order-9 fields against 100..140. F5, and the freeze's own
    reading of a miss here with P4 passing stands.
 P6 PASSES: 2 fields at 3-rank 2 against a predicted at-least-1.
 P7 IS REFUTED, at one of the two: 24843 generates Delta and 47628 does
    not. F1. The prediction named index 9 and index 3 as the two
    readings and the box returned both.

WHAT THIS LEAVES. The subgroup condition b_i - b_j in 3Cl is the law and
the scalar h/3 test is its 3-rank <= 1 reduction, proved (F3) rather
than observed, and above that rank it is not a reduction but a wrong
answer (F2). What has no name yet is the condition 47628 satisfies: its
generated subgroup is proper in N, contains Delta, and is not Delta, so
the corpus's single word "degenerate" now covers two different regimes
and the shares they carry differ by a factor of 3. (Named later by
explore_genus_index.py: the index is 3 to the number of lines the
conductor carries, 47628's 126 carrying one to 24843's 91 carrying two;
every reading here survives as its measurement.) Naming that, and
re-reading the h = 9 stratum's levels against it, is the next question
and it needs no new population -- both fields are in this box and the
walk is checkpointed. What this file does NOT settle is whether index 3
at r = 2 is the general case or the exception: two fields is two fields,
and the honest reading is that both outcomes occur. THE UPSTREAM FIX IS
OWED AND IS NOT TAKEN HERE, NOR IS WHAT THIS FILE CARRIES THE FIX TO
PORT (F7): the ladder-minimum reader here is a PARTIAL cure, sound
against rungs that are shy at different depths and useless against a
presentation every rung of which is shy, and S3b MEASURES that it
changes no class number in the sibling's box rather than proving it
cannot. The cure to port is the sibling attestation
explore_ceiling_fourthcell.py already runs. Either way it re-runs
explore_ceiling_topband.py's own frozen band reprints, which is hours of
wall and belongs under its own envelope.

RUN RECORD, and the CHECK COUNT MOVED AFTER IT: the science run below
printed 6 checks, and the post-run sections S7b and S7c add 5 more (the
Delta lattice's order control, the sum-zero control at each of the two
hit fields, the cross-representative agreement, and the count of
representatives that did not settle at all), so the file prints
11 today and the 6 is the science run's alone. That differs from the
sibling convention, where post-run sections added no checks; the four
here are the audit's, and they re-run in 243 s off the checkpoint
because they re-enumerate the box.

 2026-08-23, Windows 11, Python 3, R2_CAP=50000,
R2_CKPT=prime/code/_ckpt/r2_walk_50000.json, run under
prime/code/memwatch.py. One process, CPython, no BLAS. 6 checks passed,
3210.2 s wall (2833.1 s class reading over 10,598 fields, 244.2 s walk
over 3133 fields with h > 1, the rest enumeration), peak working set
244.4 MB against memwatch's 512 MB ceiling -- a >10-minute run, and
necessary because the question is about a field the sibling's box
provably does not contain. THE ESTIMATE ABOVE SAYS 31 MINUTES AND THE
RUN TOOK 53, which is not the estimate having been bad: 31 was frozen
for the reader this file inherited, and the first widened run came in at
2134 s against it. The gap is T7, adopted after the reprint
control fired, whose ladder costs 1.62x the class reading at this cap.
An estimate frozen before a design change prices the old design, and
the honest reading of a 1.7x overrun is to name what changed rather than
to call the estimate wrong. The max |trace-form disc| over the widened
Hunter box is 5,480,748, ABOVE the sibling's own 4 x 10^6 assert and
past its sieve at 2000, so T2's widening was load-bearing and not
hygiene. THREE RUNS WERE SPENT, and the two that died are the record:
the first was stopped by S3 before any science, which is the control
working; the second was lost whole to a TypeError in a REPORTING
section that ran BEFORE the checkpoint was written -- 53 minutes for a
sort over tuples holding None. The checkpoint now precedes every
reading section, so the sections above re-run in 0.0 s. The rehearsal
at cap 6000 ran before all three and is not counted in the wall.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import json
import math
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_class_map as CCM
import explore_cubic_principal as ECP
import explore_cubic_split_triple as ST
import explore_ceiling_topband as TB
import explore_noncyclic_level as NCL

CHECKS = 0
MIN_SPLIT = NCL.MIN_SPLIT

CAP = int(os.environ.get("R2_CAP", "50000"))
CKPT = os.environ.get("R2_CKPT")

SUB_CAP = 24000                  # the sibling's box, the reprint control
SUB_H1 = 1283                    # its h > 1 count
SUB_CENSUS = {1: 769, 3: 484, 9: 30}     # its 3-part census by order

R2_SIEVE = ECP.CR._sieve(10 ** 4)        # T2: index primes, widened
_MAXD0 = [0]                             # observed max |trace-form disc|


def maximal_order3_r2(a, b, c):
    """T2: the sibling's routine with the sieve at 10^4 and the assert at
    10^8 -- the same soundness condition (p^2 dividing d0 with
    |d0| < 10^8 forces p <= 10^4), and the observed maximum recorded
    rather than assumed. Identical below 4 x 10^6, where the sibling's
    own guard stood."""
    R = (-c, -b, -a)
    trvec = (3, -a, a * a - 2 * b)
    O = TB.CFS.Order(R, trvec, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    d0 = O.trace_form_disc()
    if abs(d0) > _MAXD0[0]:
        _MAXD0[0] = abs(d0)
    assert abs(d0) < 10 ** 8, "discriminant out of the r2 sieve range"
    for p in R2_SIEVE:
        if p * p > abs(d0):
            break
        if d0 % (p * p) == 0:
            O = TB.CFS.p_maximalize(O, p)
    return O, O.trace_form_disc()


ECP.maximal_order3 = maximal_order3_r2   # T2: the LAST declared swap


# --------------------------------- T7: the ladder-minimum reader (partial)
def read_one_r2(d, cx, a, b, c, O):
    """T7: the sibling's read_one with its ACCEPTANCE RULE replaced. Its
    rule returns as soon as two consecutive rungs agree, and two starved
    rungs can agree with each other: at |d| = 9187 the widened box's
    first polynomial reads 4, 4, 2 over the three rungs and the rule
    returns 4. Relations are genuine, so a harvest can only ever be
    missing them -- the computed order is an upper bound on h and falls
    as the box grows. The MINIMUM over the ladder is therefore the sound
    reading and the early return is not. The certification path, the
    rungs and the unresolved verdict are the sibling's, unchanged; only
    the choice among the rungs moves. The one short-circuit kept is at
    order 1, which is a floor no deeper rung can beat."""
    rows = TB.ECP.t2_rows(O, a, b, c)
    gp = TB.CFS.relation_generators(O)
    mb = TB.CFS.minkowski_bound(d, O.n, cx)
    small = [t for t in TB.CFS.all_places_upto_prime(O, mb)
             if t[0] ** t[2] <= mb]
    if all(TB.ECP.find_gen(O, P, rows, p ** f, cx) is not None
           for (p, e, f, name, P) in small):
        return 1, 'cert', gp, None
    best = None
    bestrows = None
    seen = []
    for (box, cap) in TB.RUNGS:
        rows2 = TB.CFS.harvest_relations(O, gp, box=box, cap=cap)
        H = TB.CFS.hermite_order(rows2, len(gp))
        seen.append(H)
        if H is not None and (best is None or H < best):
            best, bestrows = H, rows2
        if best == 1:
            break
    if best is None:
        return None
    _LADDER.append((abs(d), tuple(seen), best))
    return best, ('relH1' if best == 1 else 'H'), gp, bestrows


_LADDER = []                    # T7: every ladder run, for the S2b count


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


def section(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ------------------------------------------------- the lattice instrument
def three_cl(piv, k):
    """(c) The echelon of 3Cl inside Z^k: L's rows together with 3 e_i."""
    rows = [list(row) for (_c, row) in piv]
    for i in range(k):
        e = [0] * k
        e[i] = 3
        rows.append(e)
    return CCM.echelon(rows, k)


def lattice_degenerate(per_prime, piv3, k):
    """(c) b_i - b_j in 3Cl at every fully mapped split prime -- the
    subgroup condition with no scalar in it."""
    for (_p, kd, vecs) in per_prime:
        if kd != 'split' or len(vecs) != 3 or any(v is None for v in vecs):
            continue
        for j in (1, 2):
            d = [x - y for x, y in zip(vecs[0], vecs[j])]
            if not CCM.in_span(d, piv3, k):
                return False
    return True


def three_rank(fac):
    return sum(1 for x in fac if x % 3 == 0)


def three_part(fac):
    """The invariant factors of the 3-part, above 1."""
    out = []
    for x in fac:
        t = 1
        while x % 3 == 0:
            x //= 3
            t *= 3
        if t > 1:
            out.append(t)
    return out


def three_order(fac):
    o = 1
    for t in three_part(fac):
        o *= t
    return o


# ----------------------------------------------------------------- S0
def s0_rehearsal():
    """P0: the instrument on lattices whose groups are known by hand,
    three of them at 3-rank 2 -- which no field in the old box realizes,
    so the engine has never met one."""
    section("S0  THE REHEARSAL -- synthetic lattices, 3-rank 2 included "
            "-- P0")
    cases = [
        ((1,), [[1]]),
        ((3,), [[3]]),
        ((9,), [[9]]),
        ((2, 6), [[2, 0], [0, 6]]),
        ((3, 3), [[3, 0], [0, 3]]),
        ((3, 9), [[3, 0], [0, 9]]),
        ((6, 6), [[6, 0], [0, 6]]),
        ((3, 3, 3), [[3, 0, 0], [0, 3, 0], [0, 0, 3]]),
        ((5,), [[5]]),
        ((2, 2), [[2, 0], [0, 2]]),
    ]
    bad = 0
    for (want, rows) in cases:
        k = len(rows[0])
        piv = CCM.echelon(rows, k)
        fac, h = NCL.factors_of([(0, r) for (_c, r) in piv], k)
        expect = [x for x in want if x > 1]
        r = three_rank(expect)
        t3 = NCL.torsion(expect, 3)
        piv3 = three_cl(piv, k)
        got_idx = CCM.span_order(piv3, k)   # (d): span_order IS the
        # index of 3Cl in Cl -- the order of Z^k modulo the 3Cl lattice --
        # and not its cofactor in h.
        okrow = (fac == expect and t3 == 3 ** r and got_idx == 3 ** r)
        if not okrow:
            bad += 1
        print("  %-14s factors %-14s |Cl[3]| %2d  r %d  [Cl : 3Cl] %s%s"
              % ("Z/" + " x Z/".join(str(x) for x in want),
                 NCL.group_name(fac), t3, r,
                 got_idx, "" if okrow else "   MISMATCH"))
    ok(bad == 0, "%d synthetic groups misread" % bad)

    # a hand-computed membership: in Z^2/<(3,0),(0,3)>, (3,3) is in 3Cl
    # and (1,2) is not, whatever the pivots look like.
    piv = CCM.echelon([[3, 0], [0, 3]], 2)
    piv3 = three_cl(piv, 2)
    ok(CCM.in_span([3, 3], piv3, 2), "(3,3) missed in 3Cl at Z/3 x Z/3")
    ok(not CCM.in_span([1, 2], piv3, 2), "(1,2) admitted to 3Cl")
    print("  [P0] membership by hand at Z/3 x Z/3: (3,3) in, (1,2) out")
    print("  [P0] %d synthetic groups, 0 mismatches" % len(cases))


# ----------------------------------------------------------------- walk
def walk(recs):
    """T3: the lean walk. Per complex field with h > 1 and the split
    reading done: (|d|, h, factors, n_split, scalar verdict, lattice
    verdict, generated order)."""
    t0 = time.time()
    out = []
    ctrl = dict(fac_bad=0, thin=0)
    for i, rec in enumerate(recs):
        if i and i % 1000 == 0:
            print("  ... %d/%d records, %.1f s" % (i, len(recs),
                                                   time.time() - t0))
        (d, cx, a, b, c, O, h, kind, gp, rel) = rec
        if h is None or h == 1 or not cx:
            continue
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        if H is None or H == 1:
            continue
        fac, hf = NCL.factors_of(piv, k)
        if hf != H or any(fac[j + 1] % fac[j]
                          for j in range(len(fac) - 1)):
            ctrl['fac_bad'] += 1
        ns = 0
        for (_p, kd, vecs) in per_prime:
            if kd == 'split' and len(vecs) == 3 and all(
                    v is not None for v in vecs):
                ns += 1
        scal = latt = g = None
        if ns >= MIN_SPLIT:
            if H % 3 == 0:
                scal = NCL.diagonal_mod(per_prime, piv, k, H // 3)
                latt = lattice_degenerate(per_prime, three_cl(piv, k), k)
            g = NCL.generated_index(per_prime, piv, k, H)
        else:
            ctrl['thin'] += 1
        out.append((abs(d), H, list(fac), ns, scal, latt, g))
    print("  walked %d fields with h > 1 in %.1f s"
          % (len(out), time.time() - t0))
    return out, ctrl


def ckpt_save(payload):
    if not CKPT:
        return
    fields, ctrl, nrec, ladder = payload
    with open(CKPT, "w") as fh:
        json.dump(dict(cap=CAP, fields=fields, ctrl=ctrl, nrec=nrec,
                       ladder=ladder), fh)
    print("  checkpoint written to %s" % CKPT)


def ckpt_load():
    if not CKPT or not os.path.exists(CKPT):
        return None
    with open(CKPT) as fh:
        blob = json.load(fh)
    if blob.get('cap') != CAP:
        print("  T6: checkpoint at cap %s refused under cap %d"
              % (blob.get('cap'), CAP))
        return None
    print("  checkpoint reloaded from %s -- the walk is not re-run" % CKPT)
    return ([tuple(f) for f in blob['fields']], blob['ctrl'], blob['nrec'],
            [(r[0], tuple(r[1]), r[2]) for r in blob.get('ladder', [])])


# ------------------------------------------------------------- sections
def s1_population():
    section("S1  THE WIDENED POPULATION -- cap %d (T1, T2)" % CAP)
    TB.WIDE_CAP = CAP
    TB.read_one = read_one_r2          # T7: the LAST declared swap
    recs = TB.wide_class_reading()
    print("  [T2] max |trace-form disc| seen: %d against the 10^8 assert"
          % _MAXD0[0])
    return recs


def s2_walk(recs):
    section("S2  THE WALK -- the group reader and the two degeneracy "
            "tests (T3, T4)")
    fields, ctrl = walk(recs)
    print("  [C1] fields whose factors miss the order or divisibility: %d"
          % ctrl['fac_bad'])
    ok(ctrl['fac_bad'] == 0, "%d fields with bad factors" % ctrl['fac_bad'])
    print("  [T4] fields under the %d-split bar, unclassified: %d"
          % (MIN_SPLIT, ctrl['thin']))
    return fields, ctrl


def s2b_ladder(ladder):
    """T7: what the acceptance rule cost, split into the two ways the
    rules part -- the sibling INFLATING an order it agreed on early, and
    the sibling REFUSING a field no two of whose rungs agree. Only the
    first is a wrong number; the second is a field thrown away."""
    section("S2b  THE ACCEPTANCE RULE -- the sibling's two-rung "
            "agreement against the ladder minimum (T7)")
    if not ladder:
        print("  no ladder runs recorded")
        return []
    inflated, refused, bad, mute = [], [], [], []
    nrungs = len(TB.RUNGS)
    for (ad, seen, best) in ladder:
        sib, prev = None, None
        for H in seen:
            if H is not None and H == prev:
                sib = H
                break
            prev = H
        if sib is None and len(seen) < nrungs:
            # THE SHORT-CIRCUIT TRUNCATED THE RECORD. This reader stops
            # the moment a rung reads 1, so the rungs the sibling would
            # have gone on to run were never recorded -- and on those it
            # would very likely have found its agreeing pair at 1. A
            # truncated ladder testifies to nothing about the other
            # rule, in either direction, and is counted apart rather
            # than scored as a refusal.
            mute.append((ad, seen, best))
            continue
        if sib == best:
            continue
        if sib is None:
            refused.append((ad, seen, best))
        elif sib > best:
            inflated.append((ad, seen, sib, best))
        else:
            bad.append((ad, seen, sib, best))
    print("  ladder runs: %d" % len(ladder))
    print("  [T7a] ladder runs the two-rung rule INFLATED, on THIS "
          "box's representative polynomials: %d" % len(inflated))
    for rw in sorted(inflated, key=lambda x: x[0])[:12]:
        print("    |d| %6d  rungs %-20s  two-rung %-5s  minimum %s"
              % (rw[0], str(rw[1]), rw[2], rw[3]))
    if len(inflated) > 12:
        print("    ... and %d more" % (len(inflated) - 12))
    print("  [T7b] fields the two-rung rule REFUSED on a FULL ladder "
          "that the minimum resolves: %d" % len(refused))
    for rw in sorted(refused, key=lambda x: x[0])[:8]:
        print("    |d| %6d  rungs %-20s  minimum %s"
              % (rw[0], str(rw[1]), rw[2]))
    if len(refused) > 8:
        print("    ... and %d more" % (len(refused) - 8))
    print("  [T7c] ladders this reader TRUNCATED at order 1, on which "
          "the other rule cannot be scored either way: %d" % len(mute))
    print("  [C2] fields where the two-rung rule read LOWER than the "
          "ladder minimum: %d (relations are genuine, so 0 is owed)"
          % len(bad))
    ok(not bad, "%d fields where the two-rung rule beat the minimum"
       % len(bad))
    return inflated, refused, mute


def s3_reprint(fields):
    section("S3  THE REPRINT CONTROL -- the |d| <= %d sub-box against "
            "the sibling's census -- P3" % SUB_CAP)
    sub = [f for f in fields if f[0] <= SUB_CAP]
    census = {}
    for f in sub:
        o = three_order(f[2])
        census[o] = census.get(o, 0) + 1
    print("  h > 1 fields: %d (P3 says %d)" % (len(sub), SUB_H1))
    for o in sorted(census):
        print("    3-part of order %3d: %4d fields%s"
              % (o, census[o],
                 "  (P3 says %d)" % SUB_CENSUS[o] if o in SUB_CENSUS
                 else "   NEW"))
    hit = (len(sub) == SUB_H1 and census == SUB_CENSUS)
    print("  [P3] VERDICT: %s -- the frozen control is an EQUALITY and "
          "T7 resolves fields the sibling excluded, so it cannot hold; "
          "S3b is the directional control it should have been and "
          "carries the kill" % ("passes" if hit else "FAILS"))


SIB_CKPT = os.environ.get("NCL_CKPT", "prime/code/_ckpt/ncl_walk.json")


def s3b_reconcile(fields):
    """POST-RUN (added after the printed output was in hand, and marked
    as such): P3 was frozen as an EQUALITY against the sibling's census
    and it FAILED, at 1284 against 1283. An equality cannot survive a
    reader that resolves fields the sibling excluded, which is what T7
    does by construction -- so the control P3 should have been is
    DIRECTIONAL, and this section is it: every field the two boxes
    differ at must be explained by T7, either as a field the sibling
    EXCLUDED and this reader resolves, or as one whose widened
    representative this reader cannot resolve. An unexplained difference
    -- a class number that simply changed -- kills the run, and that is
    the check P3 was reaching for."""
    section("S3b  THE RECONCILIATION -- POST-RUN, field by field "
            "against the sibling's own walk")
    if not os.path.exists(SIB_CKPT):
        print("  sibling checkpoint absent at %s -- not reconciled"
              % SIB_CKPT)
        return
    from collections import Counter
    with open(SIB_CKPT) as fh:
        sib = json.load(fh)
    O = Counter((f[0], f[1], tuple(f[2])) for f in sib['perfield'])
    N = Counter((f[0], f[1], tuple(f[2]))
                for f in fields if f[0] <= SUB_CAP)
    lost = sorted((O - N).elements())
    gained = sorted((N - O).elements())
    print("  sibling %d fields with h > 1, this reader %d"
          % (sum(O.values()), sum(N.values())))
    for x in lost:
        print("    LOST   |d| %6d  h %3d  %s" % x)
    for x in gained:
        print("    GAINED |d| %6d  h %3d  %s" % x)
    # an unexplained difference is a |d| present on BOTH sides at
    # different class numbers: a reading that changed rather than a
    # field that entered or left the population. THE KILL CANNOT MISS
    # ONE -- a changed class number puts its discriminant in both
    # multisets by construction -- and it CAN over-fire, where two
    # different cubic fields share a discriminant and one enters as the
    # other leaves. Over-firing is the safe direction for a kill, and
    # the print names the fields so the reader can tell the cases apart.
    lost_d = set(x[0] for x in lost)
    gained_d = set(x[0] for x in gained)
    both = sorted(lost_d & gained_d)
    print("  [C3] fields present on both sides at DIFFERENT class "
          "numbers: %d (a reading that changed, which T7 does not "
          "explain)" % len(both))
    for d in both:
        print("       |d| %6d  sibling %s  here %s"
              % (d, [x for x in lost if x[0] == d],
                 [x for x in gained if x[0] == d]))
    ok(not both, "%d fields whose class number changed unexplained"
       % len(both))
    print("  [S3b] every difference is a field entering or leaving the "
          "resolved population, none is a changed class number")


def s4_agreement(fields):
    section("S4  THE POSITIVE CONTROL -- the scalar test against the "
            "lattice test at 3-rank <= 1 -- P1, P2")
    dis = []
    n1 = n2 = 0
    vac = []
    for (ad, h, fac, ns, scal, latt, g) in fields:
        if scal is None:
            continue
        r = three_rank(fac)
        if r <= 1:
            n1 += 1
            if scal != latt:
                dis.append((ad, h, tuple(fac), scal, latt))
        else:
            n2 += 1
            vac.append((ad, h, tuple(fac), scal, latt))
    print("  [P1] fields with 3 dividing h, r <= 1, above the bar: %d; "
          "disagreements: %d" % (n1, len(dis)))
    for rw in dis[:10]:
        print("       |d| %6d  h %3d  %s  scalar %s  lattice %s" % rw)
    ok(not dis, "%d fields where the two tests disagree at r <= 1"
       % len(dis))
    if n2 == 0:
        print("  [P2] VACUOUS -- 0 fields at 3-rank 2 above the bar")
    else:
        allsc = all(x[3] for x in vac)
        print("  [P2] fields at 3-rank 2 above the bar: %d; "
              "scalar-degenerate at every one: %s" % (n2, allsc))
    return n1, n2


def s5_census(fields):
    section("S5  THE WIDENED CENSUS -- the 3-part over the whole box "
            "-- P4, P5")
    census = {}
    names = {}
    for f in fields:
        o = three_order(f[2])
        census[o] = census.get(o, 0) + 1
        nm = NCL.group_name(three_part(f[2]))
        names.setdefault(o, {})
        names[o][nm] = names[o].get(nm, 0) + 1
    print("  h > 1 fields at cap %d: %d (P4 bracket 2670..3270)"
          % (CAP, len(fields)))
    for o in sorted(census):
        print("    3-part of order %4d: %4d fields   %s"
              % (o, census[o],
                 ", ".join("%s %d" % (k, v)
                           for k, v in sorted(names[o].items()))))
    o9 = census.get(9, 0)
    print("  [P5] fields whose 3-part has order 9: %d "
          "(bracket 100..140)" % o9)
    return census, o9


def s6_hunt(fields):
    section("S6  THE HUNT -- fields of 3-rank 2 -- P6")
    hits = [f for f in fields if three_rank(f[2]) >= 2]
    print("  [P6] fields with 3-rank >= 2: %d" % len(hits))
    for (ad, h, fac, ns, scal, latt, g) in hits:
        print("    |d| %6d  h %4d  Cl = %s  split %3d  scalar %s "
              " lattice %s  generated order %s"
              % (ad, h, NCL.group_name(fac), ns, scal, latt, g))
    return hits


def s7_index(hits):
    section("S7  THE READING -- the index of the generated subgroup in "
            "N -- P7")
    if not hits:
        print("  no 3-rank 2 field in the box; P7 is not read")
        return []
    out = []
    for (ad, h, fac, ns, scal, latt, g) in hits:
        r = three_rank(fac)
        if ns < MIN_SPLIT or g in (None, 0):
            print("    |d| %6d  h %4d  UNREAD (split %d, order %s)"
                  % (ad, h, ns, g))
            continue
        idx = (h * h) // g
        delta = 3 ** r
        verdict = ("Delta (the identification holds)" if idx == delta
                   else "PROPER SUPERGROUP of Delta -- the "
                        "identification fails" if idx and delta % idx == 0
                        else "neither")
        print("    |d| %6d  h %4d  Cl = %s  r %d  generated order %d  "
              "index %s  |Delta| = h^2/%d  ->  %s"
              % (ad, h, NCL.group_name(fac), r, g, idx, delta, verdict))
        out.append((ad, h, tuple(fac), r, g, idx, delta))
    return out


def delta_lattice(piv, k):
    """Delta as a lattice in Z^2k, in the (a, b) coordinates where
    c = -a - b. Then b - c = a + 2b = (a - b) + 3b is congruent to a - b
    mod 3Cl, so BOTH conditions cutting Delta out of N reduce to the one
    condition a - b in 3Cl. The lattice is spanned by the diagonal
    (e_i, e_i) together with (w, 0) for w spanning 3Cl: given x - y in
    3Cl, (x, y) = (y, y) + (x - y, 0)."""
    rows = []
    for i in range(k):
        e = [0] * (2 * k)
        e[i] = 1
        e[k + i] = 1
        rows.append(e)
    for (_c, row) in three_cl(piv, k):
        rows.append(list(row) + [0] * k)
    return CCM.echelon(rows, 2 * k)


def s7b_containment(hits):
    """POST-RUN. S7 reads the generated subgroup's ORDER and S6 reads
    whether every triple lies INSIDE Delta. Neither says Delta lies
    inside the GENERATED subgroup, and a subgroup of index 3 in N need
    not contain the index-9 Delta -- N/Delta is (Z/3)^2 and only the
    subgroups CONTAINING Delta correspond to its subgroups. So the
    containment is an inference until measured, and this is the
    measurement. It re-reads the hit fields from the enumeration
    because the checkpoint carries verdicts and not the mapped
    vectors."""
    section("S7b  THE CONTAINMENT -- POST-RUN, is Delta INSIDE the "
            "generated subgroup?")
    if not hits:
        print("  no 3-rank 2 field in the box; nothing to contain")
        return []
    want = set(f[0] for f in hits)
    t0 = time.time()
    fields, _b = ECP.enumerate_fields(CAP)
    out = []
    for (ad, d, cx, polys) in fields:
        if ad not in want or not cx:
            continue
        a, b, c, O = polys[0]
        got = read_one_r2(d, cx, a, b, c, O)
        if got is None:
            continue
        h, _kind, gp, rel = got
        H, piv, k, per = ST.read_field(O, a, b, c, d, cx, gp,
                                       TB.rel_basis(rel, len(gp)))
        fac, _hf = NCL.factors_of(piv, k)
        r = three_rank(fac)
        if r < 2:
            continue          # another field at the same |d|: cubic
            # fields can share a discriminant, so |d| is not a locator
        g = NCL.generated_index(per, piv, k, H)
        rows = []
        nz = 0
        for (_p, kd, vecs) in per:
            if kd == 'split' and len(vecs) == 3 and all(
                    v is not None for v in vecs):
                # THE COORDINATES ARE ONLY VALID BECAUSE THE TRIPLE SUMS
                # TO ZERO: N is read as Cl^2 through (a, b) with
                # c = -a - b, so a triple off the sum-zero locus is not
                # a point of N and the subgroup it helps generate is not
                # a subgroup of N. The parent walk controls this over
                # its own box; this box is wider, so the fields the
                # verdict actually rests on are controlled here.
                if not ST.sums_to_zero(vecs, piv, k):
                    nz += 1
                rows.append(list(vecs[0]) + list(vecs[1]))
        for (_c2, row) in piv:
            rows.append(list(row) + [0] * k)
            rows.append([0] * k + list(row))
        Hpiv = CCM.echelon(rows, 2 * k)
        Dpiv = delta_lattice(piv, k)
        dord = CCM.span_order(Dpiv, 2 * k)
        dsize = (H * H) // dord if dord else None
        inside = all(CCM.in_span(row, Hpiv, 2 * k) for (_c2, row) in Dpiv)
        print("    |d| %6d  h %2d  Cl %-12s r %d  generated order %3s  "
              "|Delta| %3s (h^2/3^r = %d)  Delta inside generated: %s"
              % (ad, H, NCL.group_name(fac), r, g, dsize,
                 (H * H) // (3 ** r), inside))
        print("      [C5] split triples off the sum-zero locus at this "
              "field: %d" % nz)
        ok(nz == 0, "%d triples off sum-zero at |d| = %d" % (nz, ad))
        out.append((ad, H, g, dsize, inside, r))
    bad = [x for x in out if x[3] != (x[1] * x[1]) // (3 ** x[5])]
    print("  [C4] hit fields where the Delta lattice's order misses "
          "h^2/3^r: %d (the lattice construction's own control)"
          % len(bad))
    ok(not bad, "%d fields where |Delta| is not h^2/3^r" % len(bad))
    print("  [S7b] Delta lies inside the generated subgroup at %d of %d "
          "hit fields, in %.1f s"
          % (sum(1 for x in out if x[4]), len(out), time.time() - t0))
    # the control above is written against 3^r and not against the 9 that
    # this box's only 3-rank happens to give, so it still tests something
    # at a 3-rank 3 field rather than firing on a correct Delta.
    return out


def s7c_attest(hits):
    """POST-RUN, and it is a GUARD THIS FILE OWED FROM THE START rather
    than an idea of its own: a settled Hermite order is the index of a
    sublattice of the full relation lattice, so it is a MULTIPLE of h,
    and every rung of ONE presentation can be shy together. The
    standing cure -- explore_ceiling_fourthcell.py T9's -- is to read
    the science-bearing subset through the field's OTHER representative
    polynomials and adopt the gcd. The whole verdict of this file rests
    on two fields being Z/3 x Z/3, which is a claim about h; if either
    9 is a multiple of a smaller truth, the class group is not that and
    the verdict is gone. So both are re-read through every
    representative the box carries."""
    section("S7c  THE ATTESTATION -- POST-RUN, the hit fields through "
            "EVERY representative")
    if not hits:
        print("  no 3-rank 2 field in the box; nothing to attest")
        return []
    want = set(f[0] for f in hits)
    t0 = time.time()
    fields, _b = ECP.enumerate_fields(CAP)
    out = []
    for (ad, d, cx, polys) in fields:
        if ad not in want or not cx:
            continue
        reads = []
        for (a, b, c, O) in polys:
            got = read_one_r2(d, cx, a, b, c, O)
            if got is None:
                reads.append(None)
                continue
            H, _k, gp, rel = got
            HH, piv, k, _per = ST.read_field(O, a, b, c, d, cx, gp,
                                             TB.rel_basis(rel, len(gp)))
            fac, _hf = NCL.factors_of(piv, k)
            reads.append((HH, NCL.group_name(fac)))
        settled = [r[0] for r in reads if r]
        nfail = sum(1 for r in reads if r is None)
        if not settled:
            continue
        g = 0
        for x in settled:
            g = math.gcd(g, x)
        groups = sorted(set(r[1] for r in reads if r))
        print("    |d| %6d  %d representatives  readings %s  gcd %d  "
              "groups %s" % (ad, len(polys), [r[0] if r else None
                                              for r in reads], g,
                             " / ".join(groups)))
        out.append((ad, settled, g, groups, nfail, len(polys)))
    # the fields the verdict rests on are the 3-rank 2 ones: every
    # representative must settle at the SAME order, and that order must
    # be the gcd, or the group is not attested.
    rank2 = [x for x in out if x[2] % 9 == 0 and len(x[3]) == 1
             and x[3][0] == 'Z/3 x Z/3' and x[4] == 0 and len(x[1]) > 1]
    shaky = [x for x in out if len(set(x[1])) > 1]
    print("  [C6] hit-|d| readings that disagree ACROSS representatives: "
          "%d (the truth divides every settled reading, so a "
          "disagreement means at least one is shy)" % len(shaky))
    ok(not shaky, "%d discriminants read differently across "
       "representatives" % len(shaky))
    # AN UNSETTLED REPRESENTATIVE IS NOT AGREEMENT. C6 above compares the
    # readings that settled, and would pass VACUOUSLY on a field where
    # one representative settled and the rest returned None -- which is
    # exactly the state the word "attested" must not cover. So the count
    # of failures is printed and the attestation below requires it to be
    # zero and requires more than one representative to have spoken.
    mute = [x for x in out if x[4]]
    print("  [C7] hit-|d| fields with a representative that did NOT "
          "settle: %d (attestation needs every one of them, not every "
          "one that answered)" % len(mute))
    ok(not mute, "%d fields carry an unsettled representative" % len(mute))
    print("  [S7c] %d of the hit discriminants carry a Z/3 x Z/3 reading "
          "attested by EVERY representative the box holds (none "
          "unsettled, more than one read), in %.1f s"
          % (len(rank2), time.time() - t0))
    return out


def s8_bound(o9, hits):
    section("S8  WHAT THE COUNT IS WORTH -- the bound (h), decided "
            "before the run; the weighting test POST-RUN")
    n = o9
    kk = len([f for f in hits if three_order(f[2]) == 9])
    if n == 0:
        print("  no order-9 field in the box; no bound")
        return
    if kk == 0:
        b = 1 - 0.05 ** (1.0 / n)
        print("  %d order-9 fields, 0 at Z/3 x Z/3: the 95%% upper bound "
              "on the Z/3 x Z/3 fraction among them is %.3f" % (n, b))
    else:
        # THE FRACTION IS A FLOOR: its numerator is exact (no shy reading
        # hides a 3-rank 2 field) and its denominator is a ceiling (an
        # order-9 reading can be of a smaller truth), so the true
        # fraction is at least this and never less.
        print("  %d order-9 fields (a CEILING), %d at Z/3 x Z/3 (EXACT): "
              "the fraction is at least %.3f" % (n, kk, float(kk) / n))
        # POST-RUN, and marked as such: (h) froze what a ZERO would be
        # worth and this is the non-zero case, so the test below was not
        # frozen with the rest. It is an exact binomial tail rather than
        # an adjective, which is the only reason it is admissible late --
        # it has no free parameter to have been chosen after the count.
        pw = 1.0 / 9.0
        tail = 0.0
        for j in range(kk + 1):
            tail += (math.comb(n, j) * pw ** j * (1 - pw) ** (n - j))
        print("  the 1/|Aut| weighting puts 1/9 of the mass there, "
              "expecting %.1f; P(X <= %d) = %.4f" % (n * pw, kk, tail))


def main():
    t0 = time.time()
    s0_rehearsal()
    got = ckpt_load()
    if got is None:
        recs = s1_population()
        nrec = len(recs)
        fields, ctrl = s2_walk(recs)
        del recs
        ckpt_save((fields, ctrl, nrec, _LADDER))   # BEFORE any reading:
        # a crash in a reporting section must never cost the walk again.
        ladder = _LADDER
    else:
        fields, ctrl, nrec, ladder = got
        fields = [(f[0], f[1], list(f[2]), f[3], f[4], f[5], f[6])
                  for f in fields]
        section("S1-S2  RELOADED -- %d records, %d fields with h > 1"
                % (nrec, len(fields)))
    s2b_ladder(ladder)
    if CAP >= SUB_CAP:
        s3_reprint(fields)
        s3b_reconcile(fields)
    else:
        section("S3  SKIPPED -- cap %d is below the sub-box's %d"
                % (CAP, SUB_CAP))
    s4_agreement(fields)
    _census, o9 = s5_census(fields)
    hits = s6_hunt(fields)
    s7_index(hits)
    s7b_containment(hits)
    s7c_attest(hits)
    s8_bound(o9, hits)
    print()
    print("%d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
