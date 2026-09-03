r"""explore_image_share.py -- THE IMAGE SETS THE SHARE, FOR BOTH EVENTS:
the all-EQUAL event re-read on the corrected degeneracy modulus at every
stratum instead of at h = 3 alone, and the price of the population that
could separate the index law from the IDENTIFICATION riding on it.
(Sibling of
explore_noncyclic_level.py, whose walk, checkpoint and generated-subgroup
test this file imports whole; of explore_triple_cube_term.py, whose
all-equal read at h = 3 is the control the general share must reproduce;
and of explore_ceiling_fourthcell.py, whose composite-h supply fit is the
shape this file's price copies and whose population it does not.)

THE QUESTION, in two parts that are one question.

The Galois image decides the model share. Where the image is all of
N = {(a, b, c) in Cl^3 : a + b + c = 0} the share of an event is its size
over h^2; where the image is the degenerate subgroup Delta the same
event's share is its size over |Delta|, and [N : Delta] = 3^r for r the
3-rank of Cl. The all-PRINCIPAL event has been read that way. The
all-EQUAL event has not: its only levelled read runs at h = 3, where the
two moduli agree and the degenerate share happens to be 1. So (i) what
does the all-equal event read at every stratum once its share is taken
off the image, and does the h = 9 stratum move the way the all-principal
one did when the nine misclassified fields were split out?

And nothing in this box separates the index law from the identification
that rides on it. [N : Delta] = 3^r is derived and no measurement touches
it; what a measurement decides is whether a field generating a PROPER
subgroup generates Delta, and at r <= 1 -- which every field in the
complex box has -- Delta is the only proper subgroup the h/3 test can
name, so the two questions coincide. At r = 2 they part: an index-3
subgroup there strictly CONTAINS the index-9 Delta. Index 9 needs
Z/3 x Z/3 inside Cl. So (ii) what does the population say about where
such a field first appears -- which is a question about SUPPLY and is
answered by a price, not by an enumeration.

WHOSE VOCABULARY THE SUSPICION IS IN, asked before anything was frozen.
"The level", "the stratum", "the share" were all minted on the
all-PRINCIPAL event, whose share on a full image is 1/h^2 -- a formula
with no group in it. The all-equal event's share has a group in it at
every image, |Cl[3]| being 3^r and not 1, so carrying the principal
event's phrasing across would silently assume r = 0. Every share in this
file is written as a size over an image size and never as a reciprocal
of h. The second part's vocabulary is worse: the parents say NON-CYCLIC
where the law says 3-RANK 2, and those are different conditions --
Z/6 x Z/2 is non-cyclic with r = 1. Nothing here is keyed by
cyclicity.

THE HAND-ATTACK, on paper before any engine code.

 (a) THE ALL-EQUAL EVENT'S SIZE, derived rather than inherited. E is the
     triples (c, c, c) in N. The sum-zero condition reads 3c = 0, so
     E = {(c, c, c) : c in Cl[3]} and |E| = |Cl[3]| = prod_i gcd(3, d_i)
     over the invariant factors, which is 3^r exactly. So

         share_E(full image)       = 3^r / h^2
         share_E(degenerate image) = 3^r / |Delta| = 3^(2r) / h^2,

     since |Delta| = h^2 / 3^r. E lies inside Delta at every field --
     a - b = 0 is in 3Cl -- so the second line is a share and not a
     conditional probability with a hole in it. THAT CONTAINMENT IS WHY
     THE IMAGE HAS TO BE NAMED AND NOT MERELY SIZED. N has four subgroups
     of index 3 at r = 1 and E need not sit inside an arbitrary one, so a
     share written as |E| over an order is unlicensed unless the
     order-3^r subgroup that was generated IS Delta. The sibling settles
     that by the conjunction of the generated order with the h/3 test;
     K4 runs the conjunction here rather than carrying its conclusion.

 (b) THE SLIP, RE-DERIVED FROM THE SHARE SIDE. The parents' share_of
     returns 1/(3 m^2) on the degenerate regime with m = h stripped of
     all its 3s. Write the 3-part of h as 3^e, so h = 3^e m. The size
     over |Delta| gives 3^r / h^2 = 3^(r - 2e) / m^2. The parents'
     formula is 3^(-1) / m^2. The two agree iff r = 1 and e = 1. Every
     field in this box has r <= 1, so the parents' formula is correct
     exactly where the 3-part of h is 3 -- which is the sibling's F5
     read off the share instead of off the test, and P1 below is the
     check that the two derivations meet.

 (c) THE EVENTS COINCIDE WHERE THERE IS NO 3-TORSION, and that is a
     control the walk owes without any new code. At 3 coprime to h,
     r = 0, so |Cl[3]| = 1 and E is the identity alone -- the
     all-principal event. So every stratum with 3 not dividing h must
     have neq equal to n3 and cE equal to c3 field by field. P2 runs it.
     The nesting is general and holds everywhere: all-principal implies
     all-equal, so neq >= n3 and cE >= c3 at every field. P3 runs that.

 (d) THE STATISTIC'S ALGEBRA, attacked where it can blow up. The level
     is (neq + cE) / ((ns + cN) x share). Two blow-ups. At large h the
     share 3^r/h^2 is small and the expectation can fall below anything
     the count can resolve, so every row prints its expectation and no
     row under MIN_READ is read -- the bar the parents set and this file
     does not move. And on the degenerate image the share is 3^r times
     LARGER, so the same cell's expectation jumps by that factor: a cell
     readable on one classification can be unreadable on the other and
     the reading must not quietly switch bars. Every h = 9 row therefore
     prints both expectations side by side.

 (e) THE PRICE'S POPULATION, which is where the shape gets used wrong.
     The fourth-cell sibling prices a cap by fitting the COMPOSITE-h
     supply. That is the right shape of argument and the wrong
     population: composite h is common and 3-rank 2 is rare, so a fit on
     it bounds the target cap from below and delivers nothing else. The
     population that prices r = 2 is the one differing from it only in
     STRUCTURE: fields whose 3-part has ORDER 9. Z/9 and Z/3 x Z/3 are
     the two groups of that order, so a heuristic that is a distribution
     on GROUPS gives their counts a ratio constant in the cap, and the
     supply of the first prices the arrival of the second. S7 censuses the
     3-parts, S8 measures that supply against the cap and turns it into a
     price, and S10 re-takes the price when S8's control refuses the fit.

 (f) A CONFOUND NAMED BY ARGUMENT OWES A COUNT. The nine degenerate
     h = 9 fields are a ninth of the readable box's proper cases and
     they surfaced in the widened band, so any difference between them
     and the twenty-one full-image fields could be a discriminant effect
     wearing an image's name. The count owed is the two halves' |d|
     distributions printed side by side, and S6 prints them before its
     verdict is read.

 (g) A CONFOUND NAMED BY ARGUMENT OWES A COUNT, on the other side too.
     A Cohen-Lenstra weighting by 1/|Aut| gives 8 fields at Z/9 for
     every one at Z/3 x Z/3 (|Aut(Z/9)| = 6, |Aut(Z/3 x Z/3)| = 48).
     That weighting is not licensed here -- 3 divides |S_3|, which is
     exactly the case the group-ring heuristics decline to cover -- so
     it is printed as a RIVAL to be measured against and never as the
     price. S9 does that, and the argument that it should fail owes the
     count that says whether it does.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 THE WALK IS IMPORTED WHOLE, AND MOSTLY AS RESULTS RATHER THAN AS
    FUNCTIONS -- which is worth saying because a reader looking for the
    calls will not find them. explore_noncyclic_level.py's Smith normal
    form and generated-subgroup test run on the CHECKPOINT's side of the
    line: their outputs, the invariant factors and the generated order,
    arrive per field in the reloaded walk and are never recomputed here.
    Only ckpt_load, torsion, group_name and -- on the no-checkpoint
    fallback path alone -- read_population and ckpt_save are called. This
    file adds no walk and no map. Its new code is the share formula, the
    per-image regrouping of the per-field cells, and the structural
    supply census.

 T2 THE CORRECTED REGIME IS THE GENERATED SUBGROUP AND NOT THE PARENTS'
    REGIME LETTER. The checkpoint carries both: reg is the parents'
    classification, which is wrong at nine h = 9 fields, and g is the
    order of the generated subgroup. Every read here keys on g. reg is
    carried only to print the disagreement.

 T3 THE FLATNESS OF THE ALL-PRINCIPAL LEVEL ACROSS h is a pattern on the
    principal event and says nothing about the equal event's level. It
    is carried in as an expectation only and P5 states it as a
    prediction that can fail.

 T4 THE PARENTS' EXCLUSIONS AND BARS STAND: the same three unresolved
    fields dropped, the same prime cap, MIN_SPLIT = 10 mapped split
    primes before a field is classified, MIN_READ = 10 expected
    corrected counts before a row is read.

 T6 THIS FILE IS PINNED TO THIS BOX AND REFUSES ANY OTHER, which is
    worth stating because the checkpoint is a path in an environment
    variable and the next widened population will be handed to whatever
    reads one. K3 asserts nine degenerate fields with 9 | h, and it runs
    in S2 -- before the census, before both prices. So a wider checkpoint
    stops the run at the population pin rather than reaching a fit whose
    cap bins were chosen for THIS box. The derived field count and box
    cap in the second price are hygiene under that pin and not a guard
    standing without it; a widened box wants its own file, not this one
    pointed at a new path.

 T5 WHAT IS MEASURED IS THE SUBGROUP THE OBSERVED TRIPLES GENERATE, a
    lower bound on the Galois image and not the image. Reading it as the
    image is an inference with a bound the sibling states and this file
    inherits: at most 0.09 of the fields misread. Every sentence here
    that says "image" is shorthand for the generated subgroup and the
    print says so.

THE PREDICTIONS, frozen before any engine code.

 P1 THE TWO DERIVATIONS MEET. The general share 3^r/h^2 on a full image
    and 3^(2r)/h^2 on a degenerate one reproduces the parents' share_of
    for the ALL-PRINCIPAL event (|E| replaced by 1) at every field whose
    3-part of h is 3 or whose h is coprime to 3, and differs from it at
    exactly the fields with 9 | h. Predicted: 0 disagreements off
    9 | h, and disagreement at every field with 9 | h and a degenerate
    image.

 P2 THE EVENTS COINCIDE OFF 3. Predicted: 0 fields with 3 coprime to h
    where neq differs from n3 or cE differs from c3 by more than 1e-9.

 P3 THE NESTING HOLDS EVERYWHERE. Predicted: 0 fields with neq < n3 or
    cE < c3 - 1e-9.

 P4 THE PARENTS' h = 3 EQUAL READ IS REPRODUCED. Feeding the general
    share to the h = 3 fields with a full image must reprint the
    parents' own all-equal level and z to within 0.002, their share
    1/3 being the general formula at r = 1. This is the positive
    control and it is read before any h = 9 result.

 P5 THE h = 9 EQUAL LEVEL COMES DOWN WHEN THE NINE ARE SPLIT OUT, and by
    a factor near 3 on that half: they were read against 3/81 where
    9/81 is owed. Predicted: the degenerate half's equal level after the
    correction is below its level before by a factor in [2.5, 3.5], and
    the pooled h = 9 equal level falls. A rise, or a half that does not
    move, means cE is not tracking the image the share was taken from
    and that is the finding rather than the failure.

 P6 THE 3-PART CENSUS FINDS NO Z/3 x Z/3. Predicted: every field in the
    box has a CYCLIC 3-part, so r <= 1 at all of them, which the sibling
    states for this box and this file re-derives from the invariant
    factors directly rather than from h.

 P7 THE ORDER-9 SUPPLY IS TOO THIN TO PRICE r = 2 FROM BELOW. Predicted:
    the count of fields whose 3-part has order 9 is under 60, so a zero
    observation bounds the Z/3 x Z/3 fraction only above and the price
    that comes out is a REQUIRED SUPPLY and a cap that buys it, never a
    cap where the first field sits.

 P8 THE NAIVE WEIGHTING IS REFUTED BY THE BOX. Predicted: the
    1/|Aut| weighting expects at least 3 fields at Z/3 x Z/3 in this
    box and the box has none, so the weighting is rejected at better
    than 2 sigma and cannot be the price's input.

THE KILLS, named as observables and not as inferences.

 K1 If P4 fails -- the general share does not reprint the parents' h = 3
    all-equal level -- the share derivation is wrong and nothing below
    S4 is read.

 K2 If P2 or P3 fails, the walk's cE is not the all-equal event's
    correction and the whole of part (i) is void.

 K3 If the printed count of fields with 9 | h and a degenerate image is
    not 9, the checkpoint is not the sibling's population and the run
    stops.

 K4 If any field with 3 | h has its generated ORDER and its h/3 test
    disagreeing, the order-3^r subgroup it generated is not known to be
    Delta, the all-equal share |E| over that order has no containment
    under it, and the run stops. This is the sibling's conjunction re-run
    rather than inherited, and it is load-bearing HERE in a way it is not
    there: the all-principal event's identity lies in every subgroup, and
    the equal event's Cl[3] does not.

 K5 If any field carries the SENTINEL -- generated_index returning None,
    or the field sitting under the split-prime bar -- the run stops. Such
    a field is dropped silently from every image-keyed read here while
    staying in the census and the price, so the two halves of this file
    would be reading different populations and nothing would say so. The
    guard is the taxonomy's own for a sentinel filed as a branch: assert
    it never occurred and print the count, at the BOUNDARY and not in
    each caller. It also settles the sibling, whose proper-subgroup count
    files a None return on the proper side.

THE REHEARSAL, run before any science print.

 C1 THE DERIVED FORMULAS AGAINST SYNTHETIC GROUPS. |Cl[3]| = 3^r is
    checked against the sibling's own torsion count over a spread of
    invariant-factor lists including non-cyclic 3-parts this box does not
    contain, so the r >= 2 arithmetic is exercised even though no field
    realizes it; the 3-part extractor is checked against the factors it
    came from; the two shares are checked to stand in the ratio 3^r; and
    the supply fit is checked to recover a power law planted in it. None
    of this touches the population and all of it fails loudly.

RESOURCE ENVELOPE, named before the run. The walk is the sibling's and
is loaded from the checkpoint (NCL_CKPT), which makes this file's own
cost the reads alone: seconds, one process, no BLAS, well under the
512 MB default. Without a checkpoint the walk costs the sibling's
twelve minutes and the file says so and runs it.

 F1 THE SHARE IS ONE FORMULA AND THE IMAGE IS ITS DENOMINATOR:
    share(event) = |event| / |image|, with |image| the order of the
    subgroup the observed split triples generate -- h^2 on a full image,
    h^2/3^r on the degenerate one -- and |event| equal to 1 for the
    all-principal event and to |Cl[3]| = 3^r for the all-equal one
    (property, derived in (a); the reduction checked at all 1283
    fields the walk carries, S3 and S4 -- against the parents' TRIPLE-EVENT
    shares alone, the totally split count's own 1/6 being a density over
    the Galois group and not an event over the class map). The parents
    carry FOUR formulas
    where this is one: 1/h^2 and 1/(3 m^2) for the all-principal event
    on the two images, and a hard-coded 1/3 and 1 for the all-equal
    event at h = 3. Off 9 | h the derived share reproduces theirs at
    every one of the 1253 classified fields; at 9 | h it agrees at the
    21 full-image fields and parts company at the 9 degenerate ones,
    which is where their 3^(1-2e)/m^2 and the derived 3^(r-2e)/m^2
    separate. So the slip at 9 | h is not a second modulus needing a
    second correction: it is what happens when the denominator is
    rebuilt out of h instead of read off the image.

 F2 THE ALL-EQUAL EVENT SITS AT 1 WHEREVER IT CARRIES INFORMATION --
    inside 2 sigma at every readable row but one, which is not the same
    claim as flatness and is all that six rows support -- five of them,
    the h = 3 degenerate cell reading 1 by construction (observation;
    the six readable rows with 3 | h, S5). Off 3 the two events COINCIDE
    -- 0 of the fields with h coprime to 3 differ in either the raw
    count or the correction -- so those strata reprint the all-principal
    levels exactly: 1.058, 1.061, 1.068, 1.114, 1.294 at h = 2, 4, 5, 7,
    8. Where 3 | h the event is new, and it reads 0.934 (z = -3.46) at
    h = 3 on a full image, 1.000 at h = 3 on the degenerate one -- where
    the share is 1 and the row is a tautology rather than a measurement
    -- 0.993 (z = -0.07) and 1.059 (z = +0.59) at h = 6 on the two
    images, and 1.101 (z = +0.47) and 0.674 (z = -1.65) at h = 9. The
    one row past 2 sigma is h = 3's full-image regime, which is the cell
    the all-principal event departs at too, and by the residual the
    corpus already records there.

 F3 THE h = 9 EQUAL LEVEL DISSOLVES THE WAY THE ALL-PRINCIPAL ONE DID
    (observation; the split is 9 fields against 21, S6). Pooled on the
    share the parents' modulus gave it, the stratum reads 1.359 at
    z = +1.98. Split by the subgroup generated, the nine read 0.674 at
    z = -1.65 and the twenty-one 1.101 at z = +0.47, both consistent
    with 1. THE FACTOR OF 3 IS ARITHMETIC AND NOT EVIDENCE: only the
    share moved, so the nine's level had to fall by exactly 3, and what
    the run buys is where the two halves LAND and not that they moved.
    The readability hazard named at the freeze fired: on the share they
    were given the nine expect 8.6 corrected counts and sit under the
    bar of 10, and on the share they are owed they expect 25.7 and are
    read -- the same cell, two classifications, one of them unreadable.
    The |d| confound owed a count and the count does not support it: the
    degenerate half spans 6468..22099 with median 16023 and the
    full-image half 7724..23683 with median 17723, so the degenerate
    fields sit LOWER rather than higher and a widened-band effect is not
    what separates the halves. That rules out the confound as ARGUED and
    not every discriminant effect there could be.

 F4 THE BOX CARRIES NO NON-CYCLIC 3-PART AT ALL (rule in range, the
    1283 fields with h > 1, read off the invariant factors and not off h;
    S7): 769 with a trivial 3-part, 484 at Z/3, 30 at Z/9, and nothing
    else. The rest of the box is the h = 1 fields, whose 3-part is
    trivial by definition, so the range is the whole of it. So r <= 1
    everywhere is not a remark about h = 9's group being cyclic -- it is
    a fact about every stratum in the box at once, and nothing here
    separates the index law from the identification riding on it, the
    two coinciding at r <= 1.

 F5 THE 1/|Aut| WEIGHTING DOES NOT SURVIVE THIS BOX (observation,
    P(0) = 0.036; S9) -- evidence against it at one box and one zero, and
    not a refutation, which one p-value at that size cannot be. Among
    groups of order 9 the weighting puts 1/9 of the mass on Z/3 x Z/3,
    which over 30 order-9 fields expects 3.33 and the box has 0. That is
    the expected direction -- 3 divides |S_3| and the group-ring
    heuristics decline to speak there -- and it matters because it is the
    only cheap prior that could have priced the hunt, so what the box
    takes away is a shortcut and not a rival.

 F6 THE PRICE IS A BRACKET AND NOT A LOCATION (observation; S8 and the
    post-run S10). The population that prices r = 2 is the one differing
    from it only in structure -- fields whose 3-part has ORDER 9 -- and
    the box holds 30, none of them Z/3 x Z/3, which bounds the fraction
    only from above and the arrival cap only from below. Fitted against
    the cap, the order-9 supply reads ~cap^2.078 -- but the same fit
    gives the supply of fields with h > 1 as ~cap^1.239 where 1 is owed,
    the count of complex cubic fields below a cap being asymptotically
    linear in it and nothing here showing the h = 1 share drifting, so
    the range is short, every cap-fitted exponent is inflated, and the
    caps that come out are floors. Refitting the supply against the
    FIELD COUNT divides that bias out: order-9 supply
    ~ 0.00019 x (fields)^1.670, which prices a supply of 100 at cap
    ~50000, 300 at ~96000 and 1000 at ~198000 against the cap-fit's
    43788, 74303 and 132644. AND THE FIRST ORDER-9 FIELD IN THIS
    POPULATION SITS ABOVE |d| = 6000: the parents' original box holds
    none, so the question could not have been asked there at all.

THE PREDICTIONS, WEIGHED.

 P1 PASSES: 0 disagreements between the derived share and the parents'
    off 9 | h over 1253 classified fields, and disagreement at exactly
    the 9 degenerate fields with 9 | h.
 P2 PASSES: 0 fields with 3 coprime to h where the equal and
    all-principal counts or corrections differ.
 P3 PASSES: 0 fields where the equal count or correction sits below the
    all-principal one.
 K4 PASSES: 0 of the 514 fields with 3 | h have the generated order and
    the h/3 test disagreeing, so every order-3^r image here IS Delta and
    the equal event's share has its containment.
 K5 PASSES: 0 fields carry the sentinel, so every field the census and
    the price count is a field the level reads count too -- and the
    sibling's 155 proper subgroups are 155 fields and not 155 fields plus
    a silent return.
 P4 PASSES: the general share reprints the h = 3 full-image all-equal
    level at 0.934, the figure the corpus already carries, and the
    degenerate cell at 1.000 on a share of 1.
 P5 PASSES, and F3 is what the pass is worth: the fall is 3.000 against
    a predicted window of [2.5, 3.5], which the derivation forces rather
    than the data, and the pooled level falls from 1.359 as predicted.
 P6 PASSES: 0 fields with a non-cyclic 3-part, now read off the
    invariant factors directly.
 P7 PASSES: 30 order-9 fields against a predicted ceiling of 60, so the
    zero is one-sided and the price is a required supply.
 P8 PASSES as written -- the weighting expects 3.33 and P(0) = 0.036 --
    and F5 is what the pass is worth: the prediction said "rejected at
    better than 2 sigma", which is a threshold and not a refutation.

WHAT THIS LEAVES. The all-equal event is now read wherever it says
anything, and it says what the all-principal event does: a level sitting at
1 -- inside 2 sigma at every readable row -- once the share is taken off the
image, with the one row past that, at h = 3's
full-image regime, which is a residual the corpus already owns and this
file does not touch. What it does NOT leave is a second correction to
make -- F1 turns two corrected moduli into one share formula, and the
only thing left to check about that formula is the case this box cannot
supply. That case needs a field with Z/3 x Z/3 inside its class group;
F4 says the box has none, F5 removes the prior that would have priced
the hunt, and F6 prices it as a bracket running from fifty to two
hundred thousand rather than as a place. TWO ROUTES STAND AND NEITHER IS
THIS ENUMERATION. The complex box can be widened, which costs the class
reading linearly in the field count and buys a supply the bracket says
is still thin. Or the TOTALLY REAL population can be read, where the
register that already exists carries exactly ONE field of class number 9
and does not record its GROUP -- one class reading against a chance the
naive weighting no longer licenses, and a lottery ticket named as one.
That register came out of a six-hour run, so the field has to be reached
by a targeted read and never by re-running the census that found it.

RUN RECORD. 2026-08-23, Windows 11, Python 3,
NCL_CKPT=prime/code/_ckpt/ncl_walk.json, run under
prime/code/memwatch.py. One process, CPython, no BLAS. 13 checks passed
here plus the imported chains' own, 0.3 s wall, peak working set 18.1 MB
against memwatch's 512 MB ceiling. THE WALK BEHIND IT IS THE SIBLING'S
AND IS NOT THIS FILE'S COST: it was regenerated on the same date into a
durable checkpoint at 738.8 s and a peak of 125.5 MB, reprinting its own
5 checks, its 21 structural strata and its 155 proper subgroups at
130 / 15 / 9 / 1 by class number, which is what makes the population
here the same population. The rehearsal ran before any science print and
is S0: 14 synthetic groups, three of them with a non-cyclic 3-part no
field realizes, 0 mismatches on |Cl[3]|, on the 3-part extraction and on
the share ratio, and a planted power law recovered to six figures. S10
is a POST-RUN section, added after the printed output was in hand and
marked as such in the print: S8's own control refused the fit it was
there to license, and the second price is what that refusal asks for.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_noncyclic_level as NCL
import explore_triple_cube_term as TCT

CHECKS = 0
MIN_READ = TCT.MIN_READ


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


# ------------------------------------------------------- the share, derived
def rank3(fac):
    """r, the 3-rank of Cl: the number of invariant factors 3 divides."""
    return sum(1 for x in fac if x % 3 == 0)


def three_part(fac):
    """The invariant factors of the 3-part, as a tuple above 1."""
    out = []
    for x in fac:
        v = 1
        while x % 3 == 0:
            x //= 3
            v *= 3
        if v > 1:
            out.append(v)
    return tuple(out)


def group_of(fac):
    return NCL.group_name(list(fac))


def share_event(size, image_order):
    """(a): an event's model share is its SIZE over the IMAGE's order.
    The image is the subgroup the observed triples generate (T5)."""
    return float(size) / image_order


def image_kind(g, h, r):
    """'full' when the generated subgroup is all of N, 'deg' when it is
    the degenerate one of index 3^r, None when it is neither."""
    if g is None or g == 0:
        return None
    if g == h * h:
        return 'full'
    if g * (3 ** r) == h * h:
        return 'deg'
    return 'other'


def read(count, corr, total, share):
    return TCT.level(count, corr, total, share)


# ------------------------------------------------------------ the sections
def s_controls(perfield):
    section("S2  THE WALK'S OWN CONTROLS -- P2, P3, K2, K3")
    off3_bad = nest_bad = 0
    kinds = {}
    deg9 = 0
    for (ad, h, fac, reg, c, g, dpar, dcor) in perfield:
        r = rank3(fac)
        if h % 3:
            if c['neq'] != c['n3'] or abs(c['cE'] - c['c3']) > 1e-9:
                off3_bad += 1
        if c['neq'] < c['n3'] or c['cE'] < c['c3'] - 1e-9:
            nest_bad += 1
        k = image_kind(g, h, r)
        kinds[k] = kinds.get(k, 0) + 1
        if k == 'deg' and h % 9 == 0:
            deg9 += 1
    print("  [P2] fields with 3 coprime to h where the equal and "
          "all-principal counts differ: %d" % off3_bad)
    ok(off3_bad == 0, "K2: %d fields break the coincidence off 3" % off3_bad)
    print("  [P3] fields where the equal count or correction sits BELOW "
          "the all-principal one: %d" % nest_bad)
    ok(nest_bad == 0, "K2: %d fields break the nesting" % nest_bad)
    print("  generated subgroup: %d full, %d degenerate, %d neither, "
          "%d unclassified (under the split-prime bar)"
          % (kinds.get('full', 0), kinds.get('deg', 0),
             kinds.get('other', 0), kinds.get(None, 0)))
    ok(kinds.get('other', 0) == 0,
       "%d fields generate a subgroup that is neither N nor the "
       "degenerate one" % kinds.get('other', 0))
    ok(kinds.get(None, 0) == 0,
       "K5: %d fields carry the SENTINEL -- generated_index returned None "
       "or the field sat under the split-prime bar -- and such a field is "
       "silently dropped from every image-keyed read while staying in the "
       "census and the price" % kinds.get(None, 0))
    conj_bad = conj_ran = 0
    for (ad, h, fac, reg, c, g, dpar, dcor) in perfield:
        if h % 3:
            continue
        conj_ran += 1
        deg = image_kind(g, h, rank3(fac)) == 'deg'
        if deg != bool(dcor):
            conj_bad += 1
    print("  [K4] the CONJUNCTION, run here rather than inherited: N has "
          "four subgroups of")
    print("     index 3 at r = 1, so the generated ORDER alone does not "
          "name the degenerate")
    print("     one -- and the all-equal share needs it named, since the "
          "equal triples need")
    print("     not lie inside an arbitrary index-3 subgroup. Fields with "
          "3 | h where the")
    print("     order test and the h/3 test disagree: %d of %d"
          % (conj_bad, conj_ran))
    ok(conj_bad == 0,
       "K4: %d fields where the generated order and the h/3 test disagree"
       % conj_bad)
    byh = {}
    for (ad, h, fac, reg, c, g, dpar, dcor) in perfield:
        if image_kind(g, h, rank3(fac)) == 'deg':
            byh[h] = byh.get(h, 0) + 1
    print("  the proper cases by class number: %s"
          % ", ".join("h = %d: %d" % (h, byh[h]) for h in sorted(byh)))
    print("  [K3] fields with 9 | h and a degenerate image: %d "
          "(the sibling's nine)" % deg9)
    ok(deg9 == 9, "K3: %d fields with 9 | h are degenerate, not 9" % deg9)
    return kinds


def s_share_agreement(perfield):
    section("S3  THE TWO DERIVATIONS MEET -- the general share against "
            "the parents' share_of on the ALL-PRINCIPAL event -- P1")
    off9 = on9 = 0
    off9_bad = on9_agree = 0
    for (ad, h, fac, reg, c, g, dpar, dcor) in perfield:
        r = rank3(fac)
        k = image_kind(g, h, r)
        if k is None:
            continue
        mine = share_event(1, g)
        theirs = TCT.share_of(h, 'D' if k == 'deg' else 'M')
        same = abs(mine - theirs) < 1e-12 * max(mine, theirs)
        if h % 9:
            off9 += 1
            off9_bad += 0 if same else 1
        else:
            on9 += 1
            on9_agree += 1 if same else 0
    print("  off 9 | h: %d classified fields, %d where the two shares "
          "disagree" % (off9, off9_bad))
    ok(off9_bad == 0, "K1: %d disagreements off 9 | h" % off9_bad)
    print("  at 9 | h: %d classified fields, %d where the two shares "
          "AGREE" % (on9, on9_agree))
    print("     (the parents' formula is 3^(1-2e)/m^2 and the derived one "
          "3^(r-2e)/m^2; at r = 1 they part company exactly at e >= 2)")
    return off9, on9


def equal_rows(perfield, key):
    """Pool the per-field cells by key(field) -> label, carrying the
    field count and the |d| list."""
    out = {}
    for rec in perfield:
        (ad, h, fac, reg, c, g, dpar, dcor) = rec
        lab = key(rec)
        if lab is None:
            continue
        e = out.setdefault(lab, [TCT.new_cell(), 0, []])
        TCT.merge(e[0], c)
        e[1] += 1
        e[2].append(ad)
    return out


def print_equal(label, c, nf, size, image_order, extra=""):
    """One all-equal row on the share |E| / |image|."""
    share = share_event(size, image_order)
    lr, _zr, _er = read(c['neq'], 0.0, c['ns'], share)
    lc, zc, exp = read(c['neq'], c['cE'], c['ns'] + c['cN'], share)
    mark = "" if exp is not None and exp >= MIN_READ else "   [thin]"
    if size == image_order:
        # the event EXHAUSTS the image, so the level is 1 by
        # construction and the row is not a measurement
        mark += "   [tautology: the event is the whole image]"
    print("  %-30s %4d fields  split %5d  equal %4d  raw %s  corr +%.1f"
          "  share %s  exp %6.1f  level %s  z %s%s%s"
          % (label, nf, c['ns'], c['neq'],
             "%.3f" % lr if lr is not None else "--", c['cE'],
             "%d/%d" % (size, image_order), exp,
             "%.3f" % lc if lc is not None else "--",
             "%+.2f" % zc if zc is not None else "--", extra, mark))
    return lc, zc, exp


def s_h3_control(perfield):
    section("S4  THE POSITIVE CONTROL -- the general share reprints the "
            "parents' all-equal read at h = 3 -- P4")
    for want in ('full', 'deg'):
        rows = equal_rows(perfield, lambda rec, w=want: (
            'k' if rec[1] == 3
            and image_kind(rec[5], rec[1], rank3(rec[2])) == w else None))
        if 'k' not in rows:
            continue
        c, nf, ds = rows['k']
        r = 1                      # h = 3 forces the 3-part to be Z/3
        size = 3 ** r
        order = 9 if want == 'full' else 3
        print_equal("h = 3, image %s" % ("N" if want == 'full' else "Delta"),
                    c, nf, size, order)
    print("     the parents read the h = 3 full-image cell against a share")
    print("     of 1/3, which is 3^1/9 -- the general formula at r = 1; and")
    print("     the degenerate cell against 1, which is 3^1/3.")


def s_equal_by_image(perfield):
    section("S5  THE ALL-EQUAL EVENT AT EVERY STRATUM, on the share the "
            "IMAGE sets -- the deliverable")
    hs = sorted(set(f[1] for f in perfield))
    out = {}
    for h in hs:
        for want in ('full', 'deg'):
            rows = equal_rows(perfield, lambda rec, hh=h, w=want: (
                'k' if rec[1] == hh
                and image_kind(rec[5], rec[1], rank3(rec[2])) == w
                else None))
            if 'k' not in rows:
                continue
            c, nf, ds = rows['k']
            fac = [f[2] for f in perfield
                   if f[1] == h and image_kind(f[5], f[1], rank3(f[2]))
                   == want]
            rs = sorted(set(rank3(x) for x in fac))
            if len(rs) != 1:
                print("  h = %d %s: MIXED 3-rank %s -- not pooled"
                      % (h, want, rs))
                continue
            r = rs[0]
            size = 3 ** r
            order = h * h if want == 'full' else (h * h) // (3 ** r)
            lc, zc, exp = print_equal(
                "h = %2d, image %s, r = %d"
                % (h, "N    " if want == 'full' else "Delta", r),
                c, nf, size, order)
            out[(h, want)] = (lc, zc, exp, nf, c)
    print("  rows marked [thin] sit under the bar of %.0f expected "
          "corrected counts and are not read; a row marked [tautology] "
          "reads 1 by construction," % MIN_READ)
    print("  its event filling the image it is scored against, and is not "
          "a measurement either.")
    return out


def s_nine(perfield, byimage):
    section("S6  THE h = 9 STRATUM -- what the misclassification was "
            "doing to the EQUAL event -- P5, and the |d| confound (f)")
    nine = [f for f in perfield if f[1] == 9
            and image_kind(f[5], f[1], rank3(f[2])) is not None]
    deg = [f for f in nine if image_kind(f[5], 9, rank3(f[2])) == 'deg']
    full = [f for f in nine if image_kind(f[5], 9, rank3(f[2])) == 'full']
    print("  the split: %d degenerate, %d full-image, %d classified in all"
          % (len(deg), len(full), len(nine)))
    rs = sorted(set(rank3(f[2]) for f in nine))
    print("  the 3-ranks present at h = 9: %s (the shares below are "
          "written at r = 1)" % rs)
    ok(rs == [1], "h = 9 carries 3-ranks %s, not r = 1 alone" % rs)
    for (lab, grp) in (("degenerate", deg), ("full-image", full)):
        ds = sorted(abs(f[0]) for f in grp)
        if not ds:
            continue
        print("     %-11s |d| %6d .. %6d, median %6d, mean %8.1f"
              % (lab, ds[0], ds[-1], ds[len(ds) // 2],
                 sum(ds) / float(len(ds))))
    pooled = TCT.new_cell()
    for f in nine:
        TCT.merge(pooled, f[4])
    print("  the stratum BEFORE the split -- every field read as full-image,")
    print("  which is what the parents' modulus said:")
    print_equal("h = 9 pooled, share 3/81", pooled, len(nine), 3, 81)
    print("  the stratum AFTER the split, each half on its own image:")
    dc = TCT.new_cell()
    for f in deg:
        TCT.merge(dc, f[4])
    fc = TCT.new_cell()
    for f in full:
        TCT.merge(fc, f[4])
    # the numerator is |E| = 3^r and the denominator the ORDER of the
    # image scored against -- 81 for N, 27 for Delta. Writing the owed
    # share as 9/81 gives the same ratio off a decomposition that is
    # neither quantity, so both rows carry the real pair.
    before, _z, _e = print_equal("  the nine, on the FULL image (as given)",
                                 dc, len(deg), 3, 81)
    after, _z2, _e2 = print_equal("  the nine, on DELTA (as owed)",
                                  dc, len(deg), 3, 27)
    print_equal("  the twenty-one, on the full image", fc, len(full), 3, 81)
    if before is not None and after is not None and after > 0:
        ratio = before / after
        print("  [P5] the nine's equal level falls by a factor of %.3f "
              "when the share is taken off the image it generates "
              "(the derivation says 3)" % ratio)
    return before, after


def s_census(perfield):
    section("S7  THE 3-PART CENSUS -- which groups the box actually "
            "carries -- P6")
    by3 = {}
    for (ad, h, fac, reg, c, g, dpar, dcor) in perfield:
        tp = three_part(fac)
        e = by3.setdefault(tp, [0, []])
        e[0] += 1
        e[1].append(ad)
    print("  %-16s %-6s %5s   %s" % ("3-part", "rank", "count", "|d| range"))
    noncyc3 = 0
    for tp in sorted(by3, key=lambda t: (len(t), t)):
        n, ds = by3[tp]
        r = len(tp)
        if r > 1:
            noncyc3 += n
        print("  %-16s %-6d %5d   %6d .. %6d"
              % (group_of(tp) if tp else "trivial", r, n, min(ds), max(ds)))
    print("  [P6] fields whose 3-part is NON-CYCLIC (r >= 2): %d" % noncyc3)
    order9 = [(tp, by3[tp]) for tp in by3 if _order(tp) == 9]
    tot9 = sum(v[0] for (_t, v) in order9)
    print("  fields whose 3-part has ORDER 9 -- the population that "
          "prices r = 2: %d" % tot9)
    for (tp, v) in sorted(order9, key=lambda x: -x[1][0]):
        print("     %-16s %5d" % (group_of(tp), v[0]))
    return by3, tot9, noncyc3


def _order(tp):
    o = 1
    for x in tp:
        o *= x
    return o


def loglog_fit(pts):
    """(A, b) for N ~ A cap^b by least squares on the logs."""
    xs = [math.log(x) for (x, y) in pts if y > 0]
    ys = [math.log(y) for (x, y) in pts if y > 0]
    n = len(xs)
    if n < 2:
        return None, None
    mx = sum(xs) / n
    my = sum(ys) / n
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    if sxx == 0:
        return None, None
    b = sxy / sxx
    return math.exp(my - b * mx), b


def s_price(perfield, tot9):
    section("S8  THE PRICE -- the cap an r = 2 field needs, fitted on the "
            "ORDER-9 supply and not on the composite-h one -- P7")
    caps = [6000, 9000, 12000, 15000, 18000, 21000, 24000]
    sup9, supall, sup3 = [], [], []
    for cap in caps:
        n9 = sum(1 for f in perfield if abs(f[0]) <= cap
                 and _order(three_part(f[2])) == 9)
        n3 = sum(1 for f in perfield if abs(f[0]) <= cap
                 and _order(three_part(f[2])) >= 3)
        na = sum(1 for f in perfield if abs(f[0]) <= cap)
        sup9.append((cap, n9))
        sup3.append((cap, n3))
        supall.append((cap, na))
        print("  cap %6d: %5d fields, %4d with 3 | h, %3d with a 3-part "
              "of order 9" % (cap, na, n3, n9))
    Aa, ba = loglog_fit(supall)
    A3, b3 = loglog_fit(sup3)
    A9, b9 = loglog_fit(sup9)
    print("  fitted supply exponents: fields with h > 1 %.3f -- THE "
          "CONTROL, and it should read 1:" % (ba if ba else float('nan')))
    print("     the count of complex cubic fields below a cap is "
          "asymptotically LINEAR in the cap,")
    print("     and unless the h = 1 share drifts this subfamily's count "
          "is too.")
    print("     3 | h  %.3f,  3-part of order 9  %.3f"
          % (b3 if b3 else float('nan'), b9 if b9 else float('nan')))
    print("  THE ZERO IS ONE-SIDED. With %d order-9 fields and none of "
          "them Z/3 x Z/3, the" % tot9)
    if tot9 > 0:
        print("     95%% upper bound on the Z/3 x Z/3 fraction among "
              "them is 3/%d = %.3f, which bounds the arrival cap from "
              "BELOW and nothing more." % (tot9, 3.0 / tot9))
    print("  SO THE PRICE IS A REQUIRED SUPPLY AND THE CAP THAT BUYS IT:")
    print("     %-12s %-14s %s" % ("fraction", "supply needed", "cap"))
    for p in (1.0 / 9, 1.0 / 30, 1.0 / 100, 1.0 / 300, 1.0 / 1000):
        need = 1.0 / p
        cap = ((need / A9) ** (1.0 / b9)) if (A9 and b9) else None
        print("     1 in %-7.0f %-14.0f %s"
              % (1.0 / p, need,
                 "%d" % int(cap) if cap else "--"))
    print("     read the rows as: if one field in every N with a 3-part of")
    print("     order 9 carries Z/3 x Z/3, the first one is expected by")
    print("     that cap. The box rules out the top row and no other.")
    return A9, b9


def s_rival(perfield, tot9, noncyc3):
    section("S9  THE RIVAL PRICE -- the 1/|Aut| weighting, measured "
            "against the box rather than believed -- P8")
    w_cyc = 1.0 / 6                # |Aut(Z/9)| = 6
    w_ele = 1.0 / 48               # |Aut(Z/3 x Z/3)| = 48
    frac = w_ele / (w_cyc + w_ele)
    exp = tot9 * frac
    print("  |Aut(Z/9)| = 6, |Aut(Z/3 x Z/3)| = 48, so among groups of "
          "order 9 the")
    print("  weighting puts %.4f of the mass on Z/3 x Z/3 -- one field in "
          "%.1f." % (frac, 1.0 / frac))
    print("  over the %d order-9 fields of this box it expects %.2f and the "
          "box has %d." % (tot9, exp, noncyc3))
    p0 = math.exp(-exp)
    print("  [P8] a Poisson with that mean gives P(0) = %.4f -- evidence "
          "against the weighting at %s, at one box and one zero, which is "
          "not a refutation" % (p0, "p < 0.05" if p0 < 0.05
                                else "p = %.3f" % p0))
    print("  which is the expected direction and the reason it is not "
          "the price's input: 3 divides |S_3|, and that is where the")
    print("  group-ring heuristics decline to speak.")
    return exp, p0


def s_rehearsal():
    section("S0  THE REHEARSAL -- the derived formulas against synthetic "
            "groups, including the r >= 2 this box has none of -- C1")
    cases = [(), (2,), (3,), (9,), (2, 4), (3, 3), (3, 9), (2, 6),
             (3, 3, 3), (6, 12), (2, 2), (5,), (27,), (3, 3, 9)]
    bad_t = bad_p = bad_s = 0
    for fac in cases:
        r = rank3(fac)
        if NCL.torsion(list(fac), 3) != 3 ** r:
            bad_t += 1
        tp = three_part(fac)
        if len(tp) != r or any(x % 3 for x in tp):
            bad_p += 1
        h = 1
        for x in fac:
            h *= x
        if h:
            full = share_event(3 ** r, h * h)
            deg = share_event(3 ** r, (h * h) // (3 ** r))
            if full > 0 and abs(deg / full - 3 ** r) > 1e-9 * 3 ** r:
                bad_s += 1
    print("  %d synthetic groups: |Cl[3]| != 3^r %d, 3-part extraction "
          "%d, share ratio != 3^r %d" % (len(cases), bad_t, bad_p, bad_s))
    ok(bad_t == 0, "%d torsion mismatches" % bad_t)
    ok(bad_p == 0, "%d 3-part mismatches" % bad_p)
    ok(bad_s == 0, "%d share-ratio mismatches" % bad_s)
    pts = [(c, 0.7 * c ** 1.4) for c in (1000, 2000, 4000, 8000, 16000)]
    A, b = loglog_fit(pts)
    print("  planted supply law 0.7 cap^1.400 recovered as %.3f cap^%.3f"
          % (A, b))
    ok(abs(b - 1.4) < 1e-6 and abs(A - 0.7) < 1e-6,
       "the supply fit does not recover a planted power law")


def s_price_again(perfield, A9, b9, tot9):
    """POST-RUN, added after the printed output was in hand: S8's own
    control says the fit is biased, so the price is re-taken under the
    correction the control asks for."""
    section("S10  THE PRICE AGAIN -- POST-RUN, because S8's control "
            "refused the fit it was there to license")
    caps = [6000, 9000, 12000, 15000, 18000, 21000, 24000]
    _Aa, ba = loglog_fit([(cap, sum(1 for f in perfield
                                    if abs(f[0]) <= cap)) for cap in caps])
    print("  THE CONTROL FAILED IN THE DIRECTION THAT MATTERS. The count "
          "of complex cubic")
    print("  fields below a cap is asymptotically LINEAR in it, and the "
          "fields this walk")
    print("  carries -- those with h > 1 -- are a share of them that no "
          "measurement here")
    print("  shows drifting, so their exponent should read 1 too and it "
          "read %.3f: the" % ba)
    print("  range is short, the asymptotics are not reached, and every "
          "exponent")
    print("  fitted against the cap is inflated by roughly the same "
          "factor -- which")
    print("  makes the extrapolated cap TOO SMALL.")
    pts = []
    for cap in caps:
        n9 = sum(1 for f in perfield if abs(f[0]) <= cap
                 and _order(three_part(f[2])) == 9)
        na = sum(1 for f in perfield if abs(f[0]) <= cap)
        if n9 > 0 and na > 0:
            pts.append((na, n9))
    Ar, br = loglog_fit(pts)
    print("  SO FIT THE SUPPLY AGAINST THE FIELD COUNT INSTEAD OF AGAINST "
          "THE CAP, which")
    print("  divides the bias out: order-9 supply ~ %.3g x (field count)"
          "^%.3f." % (Ar, br))
    nbox = len(perfield)
    capbox = max(abs(f[0]) for f in perfield)
    print("  Then read the cap off the field count at its own measured "
          "rate (%d fields at" % nbox)
    print("  cap %d, and linear beyond it), which is the assumption the "
          "control licenses." % capbox)
    print("     %-12s %-10s %-14s %s"
          % ("fraction", "supply", "fields needed", "cap (linear)"))
    for pfrac in (1.0 / 30, 1.0 / 100, 1.0 / 300, 1.0 / 1000):
        need = 1.0 / pfrac
        nf = (need / Ar) ** (1.0 / br) if (Ar and br) else None
        cap = float(capbox) * nf / nbox if nf else None
        print("     1 in %-7.0f %-10.0f %-14.0f %s"
              % (need, need, nf if nf else 0,
                 "%d" % int(cap) if cap else "--"))
    print("  THE TWO PRICES BRACKET IT, and the bracket is the answer: the "
          "cap-fit row")
    print("  is a floor and this one a working figure. Neither is a place "
          "a field is")
    print("  known to sit -- the box contains no Z/3 x Z/3 and cannot "
          "locate one.")
    return Ar, br


def main():
    s_rehearsal()
    section("S1  THE POPULATION -- the sibling's walk, off its checkpoint")
    got = NCL.ckpt_load()
    if got is None:
        print("  no checkpoint at NCL_CKPT -- walking (about twelve "
              "minutes)")
        import explore_ceiling_topband as TB
        got = NCL.read_population(TB.wide_class_reading())
        NCL.ckpt_save(got)
    cells, meta, bad, image, ctrl, perfield = got
    print("  %d fields carried per-field, %d structural strata"
          % (len(perfield), len(cells)))
    ok(bad == 0, "%d power triples do not sum to zero" % bad)

    s_controls(perfield)
    s_share_agreement(perfield)
    s_h3_control(perfield)
    byimage = s_equal_by_image(perfield)
    s_nine(perfield, byimage)
    by3, tot9, noncyc3 = s_census(perfield)
    A9, b9 = s_price(perfield, tot9)
    s_rival(perfield, tot9, noncyc3)
    s_price_again(perfield, A9, b9, tot9)

    print()
    print("%d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
