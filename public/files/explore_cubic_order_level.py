r"""IS THE ORDER GRADING ONE LAW ACROSS DEGREE 2 AND DEGREE 3, OR TWO
EFFECTS WEARING ONE SHAPE? -- the degree-3 partial-prime shortfall and the
degree-2 principal-share shortfall report the same qualitative table, the
low orders short and the top order long, and the two have never been read
against each other. This file puts the degree-3 table into degree 2's
denomination -- the LEVEL, an observed count over its nominal -- and reads
the two gradients degree 2 carries PAST the shape.

WHAT THE COMPARISON NEEDS, and why it is not just a re-print.
explore_cubic_transposition.py S4 prints the degree-3 cells as BINOMIAL
z, and explore_class_level.py prints the degree-2 cells as LEVELS over
1/h+. A z carries the cell's count in it and
a level does not, so differencing the two tables reads their variance
models and not their content. The level is the denomination both sides can
be written in, and this file is the degree-3 half of that rewrite.

WHAT RIDES ON THE ANSWER. If the two are one law, the corpus holds one
class function graded by a class's order, seen twice at two degrees over
two different arithmetics -- and the degree-2 side's own scope caveat is
answered from outside, which is the payoff worth the run: degree 2's
CEILING is measured at the cells where the order equals h+, the
GENERATORS, which exist only where the narrow class group is CYCLIC and so
rest on a narrower population than the column beneath them. Every class
group in the degree-3 population is cyclic (explore_cubic_transposition.py
F6), so here the generator cell exists at EVERY stratum and rests on the
whole of it. If the two are not one law, two coincidences are being read
as a pattern and the shape is shared for a reason that is not the
mechanism.

WHOSE VOCABULARY THE SUSPICION IS WRITTEN IN, asked at the freeze. The
suspicion arrives in DEGREE 2's vocabulary -- "a ceiling at the
generators, a shortfall deepening beneath it with h+" -- and that is a
transplant across the degree, flagged T2. The two sides do not share a
class number either: degree 2 grades by the NARROW class number h+ and
degree 3 by the ORDINARY h, so the strata are not the same objects and
only the ORDER is a common coordinate. What ports is therefore the SHAPE
of a table indexed by (class number, order) and never a stratum-to-stratum
correspondence, and nothing below pairs an h with an h+.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_cubic_transposition.py AND ITS THREE PARENTS: the
    enumeration, the class reading, the h = 1 pin, the canonical
    representative, the class order, the order profile, the place engines,
    the population, the discriminant cap and the bin edges are IMPORTED,
    not re-implemented. Every control those files run rides in with them,
    including the profile control that certifies the representative before
    any distribution is read off it.

 T2 THE TWO GRADIENTS ARE A TRANSPLANT from degree 2, where they were
    measured over ten imaginary strata reaching h+ = 28. This population
    reaches h = 8. The derivation below asks what a stratum that small can
    carry BEFORE any number is read, and the answer changes what the run
    is allowed to conclude -- see (3).

 T3 THE ESTIMATOR IS NOT THE ONE DEGREE 2 USED. Degree 2 averages a
    PER-FIELD ratio over the fields of a cell; the degree-3 walk pools
    counts. Both are levels and both have 1 for their nominal, but one
    weights fields equally and the other weights them by their prime
    count. Both are printed here and P6 is the check that the choice is
    not carrying the answer.

 T4 THE PLACEBO IS DEGREE 2's OWN CONTROL, ported: rotate the order labels
    among a field's non-trivial classes, same multiset, same cell sizes,
    same constant sum, the trivial class left where it is. At degree 3 it
    has no freedom at a prime h, where every non-trivial class already
    carries the same order -- so it is scoped to h = 4, 6, 8 and says
    nothing about the rest, which is stated rather than discovered.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE LEVEL AND ITS NOMINAL. K is a complex cubic field of class
      number h, and p is partially split in K: (p) = P.Q with P of residue
      degree 1. explore_cubic_transposition.py derivation (4)-(5) proves
      [P] is uniform on Cl(K), so a field contributing n partial places
      contributes n.phi(d)/h expected places of class order d, the count
      of classes of order d in a cyclic group of order h being phi(d).
      The LEVEL of the (h, d) cell is the observed count over that
      expectation. Its nominal is 1 and the nominal is DERIVED, not
      fitted, which is what makes 1 a real zero of the scale.

  (2) THE SUM IDENTITY, WHICH IS AN IDENTITY AND NEVER A FINDING. Within
      one stratum the expectations sum to the place count and so do the
      observations, so the expectation-weighted mean of a stratum's levels
      is EXACTLY 1. A short trivial cell must therefore be paid for by the
      others, and half of "order 1 short, top order long" is bookkeeping
      at both degrees. What is not forced is HOW the surplus distributes,
      and that is the whole content of the reading -- the same
      de-artifacting explore_class_level.py and
      explore_cubic_transposition.py each already run at their own degree,
      so the two tables entering this comparison are BOTH already cleaned
      and neither is to be re-cleaned as if it were not.

  (3) WHAT A SMALL STRATUM CANNOT CARRY, and this is the derivation that
      changes the run. The (h, d) cells of a stratum are indexed by the
      DIVISORS of h. At a PRIME h the divisors are 1 and h, so the stratum
      has exactly TWO cells, and (2) then reads

          L(1)/h + L(h).phi(h)/h = 1,   phi(h) = h - 1,

      that is L(h) = (h - L(1)) / (h - 1). The generator level is a
      DETERMINISTIC function of the trivial level, and the two gradients
      degree 2 carries are not independent measurements there but one
      number written twice. Worse than that, they are ALTERNATIVES: a
      ceiling flat at c across the prime strata forces the trivial deficit
      to grow like (c - 1)(h - 1), while a trivial level flat at 1 - e
      forces the ceiling to decay to 1 like 1 + e/(h - 1). Both of degree
      2's gradients cannot hold at a prime stratum, and degree 2's own
      numbers say which mechanism it is running: its ceiling sits at about
      1.09 while e/(h+ - 1) runs 0.056 down to 0.035 across its column, so
      degree 2's surplus at the generators is paid by the OTHER
      non-trivial cells and not by the trivial one. A prime stratum has no
      other non-trivial cells. SO THE PORT IS DECIDED AT h = 4, 6 AND 8
      ALONE, the three strata with three or more order cells, and the
      prime strata h = 2, 3, 5, 7 enter as the ARITHMETIC CHECK that a
      forced number is not being read as agreement.

  (4) WHAT THE THIN STRATUM COSTS. h = 8 is two fields and 172 partial
      primes (that file's F3), so of the three deciding strata one is thin
      enough that a cell can miss the count floor entirely. The reading
      is therefore three strata at best and two at worst, and a majority
      verdict over three is stated as such rather than as a law.

  (5) WHERE THE SMALL-PRIME EFFECT COULD MASQUERADE. The degree-3
      shortfall is a small-p effect that has not closed by the top bin
      (that file's F2), and degree 2's level table is read at ITS bottom
      bin. A table pooled over all bins is therefore diluted by the large
      primes where the effect has mostly gone, and a table read at the
      bottom bin alone is the like-for-like one but is thin. Both are
      printed, and the top bin with them, so that a bin effect cannot be
      read as a stratum effect in either direction.

THE PREDICTIONS, frozen before any engine code. Each names what the rig
PRINTS; what a print MEANS is weighed after the run and not here.

 P1 THE GENERATOR CEILING PORTS. At the strata clearing the count floor
    the ord = h cells print levels ABOVE 1, with max - min at most 0.15
    and no monotone trend across the strata.
    KILL: the printed spread exceeds 0.30, or a generator level at or
    below 1.000 at two or more strata.

 P2 THE DEEPENING TRIVIAL SHORTFALL PORTS. The ord = 1 level is below 1 at
    every stratum, and its value at the largest stratum clearing the floor
    is below its value at h = 2 by at least 0.10.
    KILL: that difference is at or above zero.

 P3 THE FORCED HALF IS EXACTLY FORCED. At h = 2, 3, 5, 7 the printed pair
    satisfies L(h) = (h - L(1))/(h - 1) to within 1e-9.
    This is derivation (3) turned into an assert, not a discovery: it
    fires if the level machinery is wrong, and it is the reason the prime
    strata are not counted as evidence for P1.

 P4 THE SURPLUS SITS AT THE GENERATORS WHERE A STRATUM CAN SAY. At h = 4,
    6 and 8 the generator cell is the HIGHEST cell of its stratum and at
    least one middle order sits below 1.
    KILL: the generator cell is not the highest at two of the three.

 P5 THE PLACEBO. At h = 4, 6 and 8 the observed spread across the orders
    above 1 beats the median of five deterministic label rotations.
    KILL: it fails to at two of the three.

 P6 THE ESTIMATOR IS NOT LOAD-BEARING. The pooled and per-field-mean
    tables agree in direction on P1, P2 and P4.
    KILL: they disagree on any one of the three.

 P7 THE CEILING'S VALUE IS DEGREE 2's. At h = 4, 6 and 8 the generator
    level lands in [1.05, 1.15], the band degree 2's ten strata span.
    KILL: two of the three land outside [1.00, 1.25].

THE CONTROLS.

 C1 THE PROFILE IS CYCLIC AT EVERY FIELD -- the count of classes of order
    d equals phi(d) for every d dividing h. F6 there reports it as an
    observation over the profiles; here it is asserted, because the
    expectation in (1) is computed from phi and not from the profile, and
    a non-cyclic field would silently mis-price its own cells.

 C2 THE SUM IDENTITY holds numerically at every stratum: a stratum's
    expectations sum to its observed place count, since the phi(d) over
    the divisors of h sum to h. (The check as first written compared the
    weighted mean level to the pooled total, which is one quantity written
    twice and cannot fail; the audit replaced it with the identity that
    can.)

 C3 THE ORDER-1 LEVEL REPRODUCES THE PARENT'S WALK, stratum by stratum
    against the counts explore_cubic_transposition.py builds from its own
    independent pass over the same population.

 C4 POSITIVE CONTROL, UNIFORM. Every field's partial places are reassigned
    by a deterministic round robin over its class list, which is uniform
    by construction. Every readable cell must print 1.000 to within the
    remainder the round robin leaves, and the generator column must NOT
    come out above 1 everywhere -- a rig that reports a ceiling on a
    uniform population reports nothing.

 C5 POSITIVE CONTROL, PLANTED. The same reassignment with a planted
    grading: the trivial class depleted to a level of 0.80 and the whole
    deficit handed to the generators. The rig must recover 0.80 at the
    trivial cell and 1 + 0.20/phi(h) at the generator cell, within the
    rounding the integer counts force.

 C6 THE BINS. The whole table is printed over all bins, over the bottom
    two, and over the top one, so derivation (5)'s masquerade is visible
    rather than assumed away.

 C7 THE MIRROR (added at audit, with S9, and with the within-stratum
    dispersion the fits use). At a prime stratum the order-1
    and generator residuals are exact negatives, which is asserted rather
    than argued -- it is what disqualifies a generator dispersion pooled
    over all strata from being a second measurement of anything.

WHAT IS NOT CONTROLLED. The two degrees' populations share nothing but the
method -- different fields, different degrees, different class numbers,
different splitting types -- so an agreement here is an agreement of
SHAPES and never a joint measurement, and no pooled statistic over the two
is computed or would mean anything. The degree-2 numbers this file quotes
are read from explore_class_level.py and explore_class_order.py and are
not recomputed; if that side moves, this comparison is stale and says so by
citing the file rather than copying its table.

THE FINDINGS.

 F1 THE CEILING PORTS, AND THE THREE STRATA ENTITLED TO SAY SO FIT ONE
    CONSTANT AT 1.0935 (observation; S4 and S9, 227 complex cubic fields,
    18689 partial places, p < 1000). At the strata whose generator level is
    NOT forced by the sum identity -- h composite, so three or more order
    cells -- the ord = h cells read 1.086 +- 0.019, 1.153 +- 0.047 and
    1.070 +- 0.056 at h = 4, 6, 8, and a single constant fits them at
    1.0935 with a chi-square of 1.95 on 2 degrees of freedom. The error
    bars are the binomial ones scaled by the dispersion S9 measures on
    that cell over the same composite strata AND ABOUT EACH STRATUM'S OWN
    MEAN, which is the only reading that does not absorb the very
    between-stratum spread the fit is testing. The scale is 0.734, so the
    fit is tested against a model stricter than independence rather than a
    looser one. ONE MODELLING CHOICE IS UNSTATED ANYWHERE ELSE AND IS
    STATED HERE: a single scale is used for all three cells, which assumes
    the dispersion is common across the three strata. 26 fields cannot
    test that, and pooling them is the only way to get a scale at all --
    so it is an assumption and not a measurement, and a reader who doubts
    it can read the fit at the binomial scale instead, where the bars are
    wider still and the constant fits more easily. The degree-2 ceiling
    explore_class_level.py reads over ten strata is 1.096, 1.099, 1.079,
    1.085, 1.087, 1.091, 1.105, 1.100, 1.096 and 1.094 -- a mean of 1.0932
    and a spread of 0.026. The degree-3 constant lands inside that spread.
    The two sides are not the same ESTIMATOR -- degree 2 averages a
    per-field ratio and the fit above pools counts (T3) -- and P6 bounds
    what that costs: the per-field-mean table gives 1.086, 1.156 and 1.072
    at the same three cells, whose constant fit is 1.0937 -- two parts in
    ten thousand from the pooled one, so the estimator is not carrying the
    agreement.
    WHAT THAT IS AND IS NOT: the two agree to 0.0003 and the degree-3
    constant's own uncertainty is about 0.017, so the four-figure match is
    luck and must never be quoted -- what is measured is that one number
    lands inside the other's spread, at two different degrees, two
    different splitting types, two different class groups (narrow there,
    ordinary here) and two independently enumerated populations, which is
    what makes the two measurements statistically independent.

 F2 AND THE SAME COLUMN POOLED OVER ALL SEVEN STRATA REJECTS THAT CONSTANT
    (observation; S9). Read across every stratum the generator column is
    1.078, 1.036, 1.086, 1.019, 1.153, 1.034, 1.070 and a constant fits at
    chi-square 35.62 on 6 -- a flat refusal. The difference is entirely
    derivation (3): at a prime h the stratum has two cells and the
    generator level is FORCED to 1 + (1 - L(1))/(h - 1), which decays with
    h whatever the arithmetic does, so four of the seven values are the
    trivial cell divided by h - 1 and carry no independent content. P3
    confirms the identity numerically at 1e-15 in all three prime-range
    views. Same data, opposite verdicts, and the reading that is entitled
    to the word "ceiling" is the one that drops the forced cells. The rule
    the freeze had to derive to avoid is NOT that a constrained table has
    no columns -- the identity binds a composite stratum's cells too and
    costs them nothing, three or more cells leaving two or more free. It
    is that a stratum with ONE free number can spend it in one column
    only, and it is spent in the trivial one.

 F3 THE SECOND GRADIENT IS FLAT AT BOTH DEGREES OVER THE RANGE THEY SHARE,
    AND DEGREE 2'S STEP SITS BEYOND WHERE DEGREE 3 REACHES (observation;
    S4, against explore_class_level.py's printed column). Degree 2's
    deepening is a STEP and not a slope: its order-2 line reads 1.032,
    1.035, 1.012, 1.041, 1.011 over h+ = 4 to 12 -- flat -- and only then
    drops, 0.966, 0.919, 0.916, 0.814 over h+ = 16 to 28. This population
    stops at h = 8, and its own order-2 line is flat across it, 0.934 at
    h = 4 and 0.933 at h = 6 (h = 8's cell is below the count floor). So
    at every order ABOVE THE TRIVIAL ONE the two tables agree over the
    whole of the range degree 3 can carry, and the gradient's PRESENCE is
    not decidable here at those orders for the plainest of reasons: degree
    2 does not show it below h+ = 12 either. The trivial line is the
    exception at both degrees, it does fall from h+ = 4, and F4 is about
    it -- this finding claims nothing there. What would
    decide it is a degree-3 population reaching h = 16, which the
    discriminant cap does not supply.

 F4 THE ONE DEGREE-2 LINE THAT FALLS FROM THE BOTTOM IS THE ONE CARRYING A
    MECHANISM DEGREE 3 HAS NO ANALOGUE OF (observation; S9, and the
    derivation is explore_class_order.py's, not recomputed here). The
    trivial column is degree 2's exception -- the one order that falls
    monotonically, 0.833 to 0.334 over h+ = 4 to 20 -- and at degree 3 it
    is flat: 0.922, 0.928, 0.893, 0.924, 0.785, 0.798 over h = 2 to 7,
    fitting a constant at 0.9208 with chi-square 9.65 on 5, the two thin
    six-field strata carrying all of the departure at -2.2 and -1.8 sigma.
    That is the one place where the two tables could be said to disagree,
    and the disagreement is the one already explained: at D < 0 the
    trivial class of a binary quadratic form carries a DERIVED hard zero,
    no prime below |D|/4 being principal at all, and a stratum of larger
    h+ is a stratum of larger |D|. A degree-1 place of a cubic field has
    no form and no minimum, so nothing here can produce that fall. The
    gradient that fails to port is the one whose mechanism does not port,
    which is the outcome that argues FOR one law in the group and not
    against it.

 F5 THE THIRD GRADIENT DOES NOT APPEAR, ON THE ONE STRATUM THAT COULD SHOW
    IT (observation; S9). Degree 2 reports the odd orders breaking the
    rise, with order 3 sitting BELOW order 2 at h+ = 6. Here h = 6 is
    monotone in the order at every cell -- 0.785, 0.933, 0.988, 1.153 over
    orders 1, 2, 3, 6 -- and so is h = 4, the only other stratum with
    three readable cells. So the odd-order feature is absent from the one
    matched cell available. It is the weakest of the three at degree 2 by
    that side's own reading, three of its four inversions sitting inside
    their stratum's placebo spread, so one non-appearance settles nothing
    either way and is recorded as a miss rather than a refutation.

 F6 THE UNDER-DISPERSION REACHES THE GENERATOR CELL, ON THE 26 FIELDS
    WHERE THAT IS A SECOND MEASUREMENT AND NOT THE FIRST ONE MIRRORED
    (observation; S9 and C7). explore_cubic_transposition.py measures the
    per-field dispersion of the ORDER-1 count and its own audit scoped the
    result to that cell, no other having been read. The obvious extension
    -- read the same statistic on the generator cell over all 227 fields
    -- MEASURES NOTHING NEW at 201 of them, and this file's own F2 is why:
    at a prime h the two cells have equal variance and their counts sum to
    the field's, so the generator residual is exactly MINUS the order-1
    one. C7 asserts that at 3e-15 over the 201 prime-stratum fields, and
    the pooled reading duly returns the order-1 spread back: 0.631 against
    0.623. Restricted to the 26 fields of composite h, where the cell is
    free, the index is 0.506 over p < 1000, 0.635 over the bottom two bins
    and 0.843 in the top bin, against the order-1 cell's 0.388, 0.364 and
    0.525. So the cell is under-dispersed too over p < 1000, and the
    strength is stated exactly rather than in sigmas, 26 fields being few:
    an index of 0.506 is the 2 per cent point of a chi-square on 25 degrees
    of freedom, so the departure is real but one-in-fifty and not
    one-in-a-thousand. The top bin's 0.843 sits at the 31 per cent point,
    consistent with independence, and is not claimed. THE FITS ABOVE DO NOT
    USE THESE NUMBERS: an error bar on a stratum's level needs the spread
    about that stratum's OWN mean, which reads 0.539, 0.687 and 0.907 --
    the audit that separated the two expected the pooled reading to be
    inflated by the between-stratum spread and it is DEFLATED instead, at
    all three views. A confound named by argument claims the effect is
    possible and never its direction; here the direction argued for was
    the wrong one and the measurement said so. THE TOP-BIN ORDER-1 READING IS
    AN EXACT REPRODUCTION of that file's own: spread 0.725, index 0.525,
    mean residual -0.184, from an independently written pass over the same
    population. The all-bins figures are NOT comparable to its all-bins
    figures and are not offered as a reproduction: this file pools a
    field's four bins into ONE residual and that file reads a residual per
    field AND bin, so the two differ by construction and by an amount no
    simple factor gives (the means are -0.577 here and -0.208 there, and
    the bins are far too unequal for the ratio to be a root of their
    count).

 F7 THE CEILING'S VALUE MOVES WITH THE PRIME RANGE, SO IT IS NOT A
    CONSTANT OF THE ARITHMETIC (observation; S4, S9). The same three
    non-forced strata read 1.0340 with chi-square 0.23 on 2 in the top bin
    alone, against 1.0935 over p < 1000; over the bottom two bins the
    generator cells run to 1.393 at h = 4. The level is a function of the
    prime cut, decaying toward 1 as the cut rises, which is the parent's
    small-prime effect seen from the top of the ladder instead of the
    bottom. (Settled 2026-08-18 by explore_ceiling_curve.py: the cut made
    a parameter at both degrees, the two ceilings decay toward 1 together
    and nowhere separate by 3 sigma in any view, so the same-cut agreement
    survives as a point on one shared decay, at that consistency and no
    sharper.) So F1 is an agreement between two readings AT THE SAME CUT and
    not the discovery of a number: degree 2's table is priced below its
    own bottom-bin cut of 1000 and this file's bins stop at 1000, which is
    what makes the comparison legitimate at all. THE SHAPE, unlike the
    value, holds at both cuts that can test it: the three non-forced
    generator cells fit one constant over p < 1000 and in the top bin
    alike (chi-square 1.95 and 0.23 on 2) and the constant is above 1 at
    both. The bottom-two-bins view cannot test it at all -- only h = 4's
    generator cell clears the count floor there, so one point is no fit
    and the 1.393 quoted above is a single cell and not a column.

 F8 THE PLACEBO PASSES ON BOTH STRATA THAT CAN CARRY IT (observation; S6).
    The observed across-order spread is 0.152 at h = 4 against five
    rotations running 0.029 to 0.074, and 0.221 at h = 6 against 0.061 to
    0.153 -- above every rotated draw at both strata. THE FIVE DRAWS ARE
    NOT FIVE DISTINCT TABLES AT h = 4: every field there has exactly three
    non-trivial classes, so the rotation has period 3 and shifts 0 and 3,
    1 and 4 coincide at every field at once -- three distinct tables, which
    is all that stratum has, and the same shortage degree 2 records at its
    own h+ = 4. At h = 6 there are five non-trivial classes and five
    distinct tables, two of which happen to return the same spread to
    three places. A prime stratum has one non-trivial order and so no
    rotation to make; h = 8 has no third readable cell. Two strata is what this
    population offers and the finding is stated at two.

 F9 A DERIVATION FIXED BEFORE THE RUN NAMED THE WRONG VIEW AS
    LIKE-FOR-LIKE, AND IT WOULD HAVE FLIPPED A KILL. Derivation (5) took
    degree 2's table to be read on a bottom bin NARROWER than this file's
    range, and reasoned that pooling all four bins here would DILUTE the
    comparison. It is the other way: degree 2's bottom-bin cut is p < 1000
    (explore_class_order.py BIN0) and this file's bin edges stop at 1000,
    so ALL BINS is the matched view and the bottom-two-bins view is
    strictly finer than anything degree 2 reads. It matters because P1's
    kill was frozen as a spread with NO VIEW NAMED, and the three views
    print 0.134, 0.315 and 0.073 -- the frozen threshold of 0.30 fires on
    one of them and not the other two. The kill is read on the matched
    view, which is a choice the freeze should have made and did not.

THE PREDICTIONS, WEIGHED.

 P1 PASSES on the matched view (spread 0.134, seven of seven above 1) and
    F9 records that the freeze left the view open. F2 is the sharper
    reading of the same column.
 P2 PASSES ON ITS POINT ESTIMATE AND FAILS ONCE ITS VARIANCE IS ATTACHED:
    the trivial level drops 0.124 from h = 2 to h = 7, clearing the frozen
    0.10, while the same column fits a CONSTANT at chi-square 9.35 on 5.
    A threshold frozen with no variance model decides nothing on its own,
    which is the second time this file's parent has printed that lesson;
    S9 exists because of it.
 P3 PASSES at 1e-15 in all three views, and it is the load-bearing one:
    F2 rests on it.
 P4 PASSES on both strata with three readable cells; h = 8 has two.
 P5 PASSES on both strata that can carry a rotation (F8).
 P6 PASSES -- at every readable cell the pooled and per-field-mean tables
    agree to within 0.005 and never differ in direction. The two cells
    that move further are h = 8's order 1 and order 2, both below the
    count floor and neither read.
 P7 PASSES: 1.086, 1.153, 1.070 against the frozen [1.05, 1.15], two of
    three inside it and the third 0.003 outside, all three inside the
    [1.00, 1.25] the kill named.

RUN RECORD. 2026-08-17, Windows 11, Python 3, `python prime/code/memwatch.py
--limit 512 prime/code/explore_cubic_order_level.py`. One process, CPython,
no BLAS. 24 checks here and 10 in the imported parent, 199.0 s wall, peak
working set 77.0 MB against memwatch's 512 MB ceiling. The population is the
parent's: 227 mapped complex cubic fields with h > 1, 18689 partial places,
0 non-cyclic order profiles, and the order-1 counts agreeing with the
parent's independent walk exactly at all seven strata. S9 WAS WRITTEN AFTER
THE FIRST RUN; it adds no kill and can only make a passed prediction fail,
every threshold above having been stated on a point estimate. THE FILE WAS
RE-RUN WHOLE at every later change and every figure quoted above is the
LAST run's -- no number here was carried across an edit. Two audit rounds
changed prints. The first found the mirror C7 now asserts and restricted
the generator dispersion to the composite strata, which widened that cell's
bars by about a tenth and moved the fits they feed: 2.64 to 2.07 on the
headline and 48.24 to 37.93 on the pooled column. The second replaced C2,
which had been written as a comparison of one quantity to itself and
returned 0.00e+00 by construction; the identity that can fail reads
6.6e-16. The third separated the pooled dispersion from the within-stratum
one and gave the fits the latter, moving the headline to 1.95 and the
pooled column to 35.62. Across all three the headline constant never moved
from 1.0935 and its chi-square only fell, so the finding survives its own
repairs rather than being propped by them.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_transposition as XT

CHECKS = 0

BIN_EDGES = XT.BIN_EDGES
MIN_CELL = 30.0                 # expected count a cell needs before it reads
ALL_BINS = tuple(range(len(BIN_EDGES) - 1))
LOW_BINS = (0, 1)
TOP_BINS = (len(BIN_EDGES) - 2,)
N_ROTATE = 5                    # P5's deterministic label rotations
PLANT_LEVEL = 0.80              # C5's planted trivial level


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


def phi(n):
    r = 0
    for a in range(1, n + 1):
        x, y = a, n
        while y:
            x, y = y, x % y
        if x == 1:
            r += 1
    return r


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


# ------------------------------------------------- the population, once
def build_population(mapped):
    """One record per field: (h, |d|, classes, places).

    `classes` is the list of (representative, order) over the whole group,
    `places` the list of (bin, representative) over the field's partial
    primes. Everything downstream reads these two lists and nothing else,
    which is what lets the synthetic controls replace `places` wholesale.
    """
    pop = []
    for (d, cx, a, b, c, O, H, piv, k, per_prime, prof) in mapped:
        grid = [[0] * k]
        for (cc, row) in piv:
            n = abs(row[cc])
            nxt = []
            for r in grid:
                for t in range(n):
                    q = list(r)
                    q[cc] = t
                    nxt.append(q)
            grid = nxt
        classes = [(tuple(r), XT.class_order(r, piv, H)) for r in grid]
        places = []
        for (p, kd, vecs) in per_prime:
            if kd != 'partial' or len(vecs) != 1 or vecs[0] is None:
                continue
            bi = XT.bin_of(p)
            if bi is None:
                continue
            places.append((bi, XT.reduce_vec(vecs[0], piv)))
        pop.append((H, abs(d), classes, places))
    return pop


def check_profiles(pop):
    """C1: every group in the population is cyclic, read as phi."""
    bad = 0
    for (h, D, classes, places) in pop:
        prof = {}
        for (rep, o) in classes:
            prof[o] = prof.get(o, 0) + 1
        if len(classes) != h:
            bad += 1
            continue
        for dd in divisors(h):
            if prof.get(dd, 0) != phi(dd):
                bad += 1
                break
    print("  C1: %d fields whose order profile is not the cyclic one"
          % bad)
    ok(bad == 0, "%d non-cyclic order profiles" % bad)


# ------------------------------------------------------- the level table
def level_table(pop, bins, relabel=None):
    """(h, order) -> [observed, expected, per-field ratios].

    `relabel`, when given, maps (h, |d|, classes) to a dict sending a
    representative to the order it is to be COUNTED under -- P5's
    rotation. The counts, the cell sizes and the constant sum are
    untouched by it.
    """
    cells = {}
    nfield = {}
    for (h, D, classes, places) in pop:
        sel = [(bi, rep) for (bi, rep) in places if bi in bins]
        if not sel:
            continue
        if relabel is None:
            lab = dict((rep, o) for (rep, o) in classes)
        else:
            lab = relabel(h, D, classes)
        n = len(sel)
        nfield[h] = nfield.get(h, 0) + 1
        cnt = {}
        for (bi, rep) in sel:
            cnt[rep] = cnt.get(rep, 0) + 1
        for (rep, _o) in classes:
            cell = cells.setdefault((h, lab[rep]), [0, 0.0, []])
            cell[0] += cnt.get(rep, 0)
            cell[1] += float(n) / h
            cell[2].append(cnt.get(rep, 0) * float(h) / n)
    return cells, nfield


def rotate(shift):
    """T4/P5: rotate the order labels among the non-trivial classes."""
    def f(h, D, classes):
        lab = dict((rep, o) for (rep, o) in classes)
        keys = sorted(rep for (rep, o) in classes if o != 1)
        if len(keys) < 2:
            return lab
        labels = [lab[rep] for rep in keys]
        start = (D + shift) % len(keys)
        for i, rep in enumerate(keys):
            lab[rep] = labels[(i + start) % len(keys)]
        return lab
    return f


def pooled(cell):
    return cell[0] / cell[1] if cell[1] > 0 else None


def perfield(cell):
    v = cell[2]
    return sum(v) / len(v) if v else None


def strata_of(cells):
    return sorted(set(h for (h, o) in cells))


def orders_of(cells, h):
    return sorted(o for (hh, o) in cells if hh == h)


def readable(cells, h):
    """The orders of stratum h whose expectation clears the floor."""
    return [o for o in orders_of(cells, h)
            if cells[(h, o)][1] >= MIN_CELL]


def print_table(cells, nfield, label, est):
    print("  %s --" % label)
    for h in strata_of(cells):
        parts = []
        for o in orders_of(cells, h):
            cell = cells[(h, o)]
            v = est(cell)
            mark = " " if cell[1] >= MIN_CELL else "*"
            parts.append("ord %d: %s%s"
                         % (o, "--" if v is None else "%.3f" % v, mark))
        n = sum(cells[(h, o)][0] for o in orders_of(cells, h))
        print("    h = %d  %3d fields  %5d places   %s"
              % (h, nfield.get(h, 0), n, "  ".join(parts)))
    print("    (* = expectation below the %d floor, not read)"
          % int(MIN_CELL))


def check_sum_identity(cells):
    """C2: a stratum's expectations sum to its place count.

    THE VACUOUS VERSION OF THIS CHECK compares the expectation-weighted
    mean level to the pooled total, which is the same quantity written two
    ways and returns 0.0 whatever the data -- it was written that way and
    caught at audit. What has content is that the expectations THEMSELVES
    sum to the observations: sum over d | h of phi(d) is h, so a field
    contributing n places contributes n expected ones, and the identity
    fails the moment a class is missed, double-counted, or priced against
    a profile that is not the cyclic one. It is the identity derivation
    (2) rests on and the reason a stratum's levels average to 1 at all.
    """
    worst = 0.0
    for h in strata_of(cells):
        os_ = orders_of(cells, h)
        obs = sum(cells[(h, o)][0] for o in os_)
        exp = sum(cells[(h, o)][1] for o in os_)
        if obs == 0:
            continue
        worst = max(worst, abs(obs - exp) / float(obs))
    print("  C2: a stratum's expectations depart from its observed place "
          "count by at most %.2e of it" % worst)
    ok(worst < 1e-12, "the sum identity failed at %.2e" % worst)


def check_forced(cells, label):
    """P3: at a prime stratum the two cells are one number."""
    worst = 0.0
    seen = 0
    for h in strata_of(cells):
        if len(divisors(h)) != 2:
            continue
        c1, cg = cells.get((h, 1)), cells.get((h, h))
        if c1 is None or cg is None:
            continue
        l1, lg = pooled(c1), pooled(cg)
        if l1 is None or lg is None:
            continue
        seen += 1
        worst = max(worst, abs(lg - (h - l1) / float(h - 1)))
    print("  P3 (%s): %d prime strata, the identity L(h) = (h - L(1))"
          "/(h - 1) off by at most %.2e" % (label, seen, worst))
    ok(seen > 0, "no prime stratum reached P3")
    ok(worst < 1e-9, "P3's identity failed at %.2e" % worst)


def spread_of(cells, h):
    """P5's observable: max - min over the readable orders above 1."""
    vals = [pooled(cells[(h, o)]) for o in readable(cells, h) if o > 1]
    return (max(vals) - min(vals)) if len(vals) >= 2 else None


# ---------------------------------------------------- synthetic controls
def synth_uniform(pop):
    """C4: a deterministic round robin over each field's class list."""
    out = []
    for (h, D, classes, places) in pop:
        reps = [rep for (rep, o) in sorted(classes)]
        new = [(bi, reps[i % len(reps)])
               for i, (bi, rep) in enumerate(places)]
        out.append((h, D, classes, new))
    return out


def synth_planted(pop):
    """C5: the trivial class depleted to PLANT_LEVEL, the deficit given to
    the generators, every other order left at its nominal."""
    out = []
    for (h, D, classes, places) in pop:
        n = len(places)
        triv = [rep for (rep, o) in sorted(classes) if o == 1]
        gens = [rep for (rep, o) in sorted(classes) if o == h]
        mids = [rep for (rep, o) in sorted(classes)
                if o != 1 and o != h]
        want = [triv[0]] * int(round(n * PLANT_LEVEL / h))
        for rep in mids:
            want += [rep] * int(round(float(n) / h))
        want = want[:n]
        pool = gens if gens else triv
        i = 0
        while len(want) < n:
            want.append(pool[i % len(pool)])
            i += 1
        new = [(bi, want[i]) for i, (bi, rep) in enumerate(places)]
        out.append((h, D, classes, new))
    return out


# --------------------------------------------------------- the sections
def s4_levels(pop):
    section("S4  THE LEVEL TABLE, P1 P2 P3 P4 P6 P7, C2 C6")
    views = (("all bins", ALL_BINS), ("the bottom two bins", LOW_BINS),
             ("the top bin", TOP_BINS))
    tables = {}
    for (name, bins) in views:
        cells, nfield = level_table(pop, bins)
        tables[name] = (cells, nfield)
        print()
        print_table(cells, nfield, "POOLED, %s" % name, pooled)
        check_sum_identity(cells)
        check_forced(cells, name)
    print()
    cells, nfield = tables["all bins"]
    print_table(cells, nfield, "PER-FIELD MEAN, all bins (T3, P6)",
                perfield)
    return tables


def s5_gradients(tables):
    section("S5  THE TWO GRADIENTS READ AGAINST DEGREE 2")
    for name in ("all bins", "the bottom two bins", "the top bin"):
        cells, nfield = tables[name]
        print()
        print("  %s --" % name)
        gen, triv = [], []
        for h in strata_of(cells):
            cg, c1 = cells.get((h, h)), cells.get((h, 1))
            if cg is not None and cg[1] >= MIN_CELL:
                gen.append((h, pooled(cg)))
            if c1 is not None and c1[1] >= MIN_CELL:
                triv.append((h, pooled(c1)))
        print("    P1 the generator cells (ord = h): %s"
              % "  ".join("h=%d %.3f" % t for t in gen))
        if len(gen) >= 2:
            v = [x for (h, x) in gen]
            print("       spread %.3f over %d strata, %d of them above 1"
                  % (max(v) - min(v), len(v), sum(1 for x in v if x > 1)))
        print("    P2 the trivial cells (ord = 1): %s"
              % "  ".join("h=%d %.3f" % t for t in triv))
        if len(triv) >= 2:
            print("       largest stratum minus h = %d: %+.3f"
                  % (triv[0][0], triv[-1][1] - triv[0][1]))
        print("    P4 the deciding strata (three or more order cells) --")
        for h in strata_of(cells):
            ords = readable(cells, h)
            if len(ords) < 3:
                continue
            lv = [(o, pooled(cells[(h, o)])) for o in ords]
            top = max(lv, key=lambda t: t[1])
            print("       h = %d  %s  |  highest is ord %d, "
                  "%d middle orders below 1"
                  % (h, "  ".join("ord %d %.3f" % t for t in lv), top[0],
                     sum(1 for (o, x) in lv
                         if o not in (1, h) and x < 1)))


def s6_placebo(pop, tables):
    section("S6  P5 THE PLACEBO -- rotated order labels (T4)")
    cells, _ = tables["all bins"]
    for h in strata_of(cells):
        obs = spread_of(cells, h)
        if obs is None or len(readable(cells, h)) < 3:
            continue
        draws = []
        for s in range(N_ROTATE):
            rc, _ = level_table(pop, ALL_BINS, relabel=rotate(s))
            v = spread_of(rc, h)
            if v is not None:
                draws.append(v)
        draws.sort()
        med = draws[len(draws) // 2] if draws else None
        print("  h = %d  observed spread %.3f against rotations %s"
              % (h, obs, " ".join("%.3f" % x for x in draws)))
        if med is not None:
            print("         median rotation %.3f -- observed %s it"
                  % (med, "beats" if obs > med else "does not beat"))
    print("  (a prime stratum has one non-trivial order and no rotation "
          "to make, so it is")
    print("   absent by construction and not by a floor)")


def s7_synthetic(pop):
    section("S7  C4 C5 THE POSITIVE CONTROLS")
    print()
    print("  C4 uniform by construction --")
    cells, nfield = level_table(synth_uniform(pop), ALL_BINS)
    print_table(cells, nfield, "POOLED, all bins", pooled)
    worst = 0.0
    for (h, o), cell in cells.items():
        if cell[1] >= MIN_CELL:
            worst = max(worst, abs(pooled(cell) - 1.0))
    print("  C4: the furthest readable cell sits %.4f from 1.000" % worst)
    ok(worst < 0.05,
       "C4's uniform population read %.4f off nominal" % worst)
    gen = [pooled(cells[(h, h)]) for h in strata_of(cells)
           if cells.get((h, h)) and cells[(h, h)][1] >= MIN_CELL]
    print("  C4: %d of %d generator cells above 1.000"
          % (sum(1 for x in gen if x > 1.0), len(gen)))
    ok(sum(1 for x in gen if x > 1.0) < len(gen),
       "C4: every generator cell read above 1 on a uniform population")
    print()
    print("  C5 planted: trivial level %.2f, the deficit to the generators"
          % PLANT_LEVEL)
    cells, nfield = level_table(synth_planted(pop), ALL_BINS)
    print_table(cells, nfield, "POOLED, all bins", pooled)
    w1 = wg = 0.0
    for h in strata_of(cells):
        c1, cg = cells.get((h, 1)), cells.get((h, h))
        if c1 is not None and c1[1] >= MIN_CELL:
            w1 = max(w1, abs(pooled(c1) - PLANT_LEVEL))
        if cg is not None and cg[1] >= MIN_CELL:
            wg = max(wg, abs(pooled(cg)
                             - (1.0 + (1.0 - PLANT_LEVEL) / phi(h))))
    print("  C5: the trivial cells sit at most %.4f from the planted "
          "%.2f, the" % (w1, PLANT_LEVEL))
    print("      generator cells at most %.4f from theirs" % wg)
    ok(w1 < 0.05,
       "C5 did not recover the planted trivial level (%.4f)" % w1)
    ok(wg < 0.10,
       "C5 did not recover the planted generator level (%.4f)" % wg)


def s8_parent_agreement(pop, mapped):
    """C3: the order-1 cell against the parent's own independent walk."""
    section("S8  C3 THE ORDER-1 CELL AGAINST THE PARENT'S WALK")
    cells, _ = XT.walk(mapped)
    mine, _ = level_table(pop, ALL_BINS)
    worst = 0
    for h in strata_of(mine):
        tot = XT.merge(cells, h=h)
        obs = tot['obs'].get(1, 0)
        exp = tot['exp'].get(1, 0.0)
        got = mine[(h, 1)]
        print("  h = %d  parent %d/%.1f   here %d/%.1f"
              % (h, obs, exp, got[0], got[1]))
        worst = max(worst, abs(obs - got[0]))
        ok(abs(exp - got[1]) < 1e-6,
           "h = %d: the order-1 expectation disagrees with the parent" % h)
    print("  C3: the order-1 counts differ from the parent's by at most %d"
          % worst)
    ok(worst == 0, "the order-1 counts disagree with the parent")


# ------------------------------------------------ S9, the variance model
# WRITTEN AFTER THE FIRST RUN, and labelled as such. P1, P2 and P7 froze
# THRESHOLDS on a level with no variance model attached -- the species
# explore_cubic_transposition.py's own audit caught twice in one file --
# so a level could be read against a band without anything saying how
# far it was entitled to move. This section supplies the missing model and
# it is not a new kill: it can only make a passed prediction fail, never
# the reverse, because every threshold above was stated on the point
# estimate alone. The dispersion is MEASURED here rather than borrowed:
# that file's F7 measures the ORDER-1 cell's dispersion and its own audit
# scoped it to that cell, so the generator cell's is read from scratch by
# the same construction.
MIN_FIELD_CELL = 5.0            # expectation a field needs to enter S9


def field_residuals(pop, bins, want, composite_only=False):
    """Per-field standardized residuals of one order cell: (observed -
    expected) over the binomial sd, one value per field.

    `composite_only` drops the prime strata, and it is not a refinement --
    it is the only reading of the GENERATOR cell that measures anything
    new. At a prime h the two cells have equal variance and their counts
    sum to the field's, so the generator residual is EXACTLY minus the
    order-1 one; pooling all strata would report the order-1 dispersion
    twice and call the second reading independent. The mirror is asserted
    rather than argued (C7)."""
    out = []
    for (h, D, classes, places) in pop:
        if composite_only and len(divisors(h)) == 2:
            continue
        sel = [rep for (bi, rep) in places if bi in bins]
        n = len(sel)
        if n == 0:
            continue
        d = want(h)
        if h % d:
            continue
        q = phi(d) / float(h)
        exp = n * q
        if exp < MIN_FIELD_CELL or q >= 1.0:
            continue
        lab = dict((rep, o) for (rep, o) in classes)
        obs = sum(1 for rep in sel if lab[rep] == d)
        out.append((h, (obs - exp) / (n * q * (1 - q)) ** 0.5))
    return out


def spread_index(res, within_stratum=False):
    """Mean, spread and index of a residual list.

    `within_stratum` measures the spread about each STRATUM's own mean
    instead of the pooled one. That is the reading the constant fits need
    and the audit that added it says why: a residual is computed against a
    field's own expectation, so a stratum sitting above nominal pushes all
    of its fields' residuals up, and a spread taken about the pooled mean
    ABSORBS the between-stratum differences the chi-square is testing --
    inflating the error bars in exactly the direction that makes a
    constant fit pass. Pooled is the right reading for "is this cell
    under-dispersed", which is a statement about fields; within-stratum is
    the right one for an error bar on a stratum's level."""
    if len(res) < 2:
        return None, None, None
    vals = [x for (h, x) in res]
    m = sum(vals) / len(vals)
    if not within_stratum:
        v = sum((x - m) ** 2 for x in vals) / (len(vals) - 1)
        return m, v ** 0.5, v
    grp = {}
    for (h, x) in res:
        grp.setdefault(h, []).append(x)
    grp = dict((h, v) for h, v in grp.items() if len(v) >= 2)
    n = sum(len(v) for v in grp.values())
    if n <= len(grp):
        return m, None, None
    ss = 0.0
    for v in grp.values():
        mu = sum(v) / len(v)
        ss += sum((x - mu) ** 2 for x in v)
    v = ss / (n - len(grp))
    return m, v ** 0.5, v


def level_sd(cells, h, o, scale):
    """The sd of a cell's level: binomial, times the measured dispersion
    scale. q is read off the cell so a rotated table cannot use this."""
    cell = cells[(h, o)]
    q = phi(o) / float(h)
    if cell[1] <= 0 or q >= 1.0:
        return None
    return scale * ((1 - q) / cell[1]) ** 0.5


def constant_fit(pts):
    """Weighted mean of (level, sd) and its chi-square about it."""
    w = [1.0 / (s * s) for (h, l, s) in pts]
    mu = sum(wi * l for wi, (h, l, s) in zip(w, pts)) / sum(w)
    chi = sum(((l - mu) / s) ** 2 for (h, l, s) in pts)
    return mu, chi, len(pts) - 1


def check_mirror(pop):
    """C7: at a prime h the generator residual is minus the order-1 one,
    exactly. Asserted, because it is what disqualifies the pooled
    generator dispersion from being a second measurement."""
    worst = 0.0
    seen = 0
    for (h, D, classes, places) in pop:
        if len(divisors(h)) != 2 or not places:
            continue
        n = len(places)
        lab = dict((rep, o) for (rep, o) in classes)
        o1 = sum(1 for (bi, rep) in places if lab[rep] == 1)
        og = n - o1
        q = 1.0 / h
        r1 = (o1 - n * q) / (n * q * (1 - q)) ** 0.5
        rg = (og - n * (1 - q)) / (n * (1 - q) * q) ** 0.5
        worst = max(worst, abs(r1 + rg))
        seen += 1
    print("  C7: %d prime-stratum fields, |r(order 1) + r(generators)| at "
          "most %.2e" % (seen, worst))
    ok(seen > 0, "no prime-stratum field reached C7")
    ok(worst < 1e-9, "the mirror identity failed at %.2e" % worst)


def s9_variance(pop, tables):
    section("S9  THE VARIANCE MODEL THE PREDICTIONS WERE FROZEN WITHOUT")
    check_mirror(pop)
    print("  all bins is p < %d, which is degree 2's OWN bottom-bin cut"
          % BIN_EDGES[-1])
    print("  (explore_class_order.py BIN0), so that view and not a finer")
    print("  one is the like-for-like comparison.")
    scales = {}
    for name, bins in (("all bins", ALL_BINS),
                       ("the bottom two bins", LOW_BINS),
                       ("the top bin", TOP_BINS)):
        print()
        print("  %s -- the per-field dispersion of two cells:" % name)
        for what, want, comp in (("order 1", lambda h: 1, False),
                                 ("the generators", lambda h: h, True)):
            res = field_residuals(pop, bins, want, composite_only=comp)
            m, sd, idx = spread_index(res)
            mw, sdw, idxw = spread_index(res, within_stratum=True)
            if sd is None:
                print("    %-15s too few fields" % what)
                continue
            scales[(name, what)] = sdw if sdw is not None else sd
            print("    %-15s %3d fields%s, mean residual %+.3f, spread "
                  "%.3f, index %.3f"
                  % (what, len(res), " (h composite only)" if comp else "",
                     m, sd, idx))
            print("    %-15s about each stratum's OWN mean: spread %s, "
                  "index %s -- this is the one the fits use"
                  % ("", "--" if sdw is None else "%.3f" % sdw,
                     "--" if idxw is None else "%.3f" % idxw))
        a = field_residuals(pop, bins, lambda h: 1)
        b = field_residuals(pop, bins, lambda h: h)
        print("    C7: order 1 over ALL strata reads spread %.3f on %d "
              "fields," % (spread_index(a)[1], len(a)))
        print("        and the generator cell over all strata reads %.3f "
              "on %d --" % (spread_index(b)[1], len(b)))
        print("        the same number twice, the two residuals being "
              "exact negatives at every prime stratum.")
    for name in ("all bins", "the bottom two bins", "the top bin"):
        cells, nfield = tables[name]
        print()
        print("  %s -- the two columns with their sd:" % name)
        for what, want, key in (("P2 order 1", lambda h: 1, "order 1"),
                                ("P1 generators", lambda h: h,
                                 "the generators")):
            scale = scales.get((name, key), 1.0)
            pts = []
            for h in strata_of(cells):
                o = want(h)
                if (h, o) not in cells or cells[(h, o)][1] < MIN_CELL:
                    continue
                sd = level_sd(cells, h, o, scale)
                if sd is None:
                    continue
                pts.append((h, pooled(cells[(h, o)]), sd))
            if not pts:
                continue
            print("    %s: %s" % (what, "  ".join(
                "h=%d %.3f+-%.3f" % t for t in pts)))
            if len(pts) >= 2:
                mu, chi, df = constant_fit(pts)
                print("      constant fit %.4f, chi-square %.2f on %d dof "
                      "(dispersion scale %.3f)" % (mu, chi, df, scale))
            free = [t for t in pts if len(divisors(t[0])) > 2]
            if what.startswith("P1") and len(free) >= 2:
                mu, chi, df = constant_fit(free)
                print("      the strata that are NOT forced by the sum "
                      "identity (h composite):")
                print("      %s" % "  ".join(
                    "h=%d %.3f+-%.3f" % t for t in free))
                print("      constant fit %.4f, chi-square %.2f on %d dof"
                      % (mu, chi, df))
    print()
    print("  the column read in the order, per stratum (all bins) --")
    cells, _ = tables["all bins"]
    for h in strata_of(cells):
        ords = readable(cells, h)
        if len(ords) < 3:
            continue
        lv = [pooled(cells[(h, o)]) for o in ords]
        rising = all(lv[i] < lv[i + 1] for i in range(len(lv) - 1))
        inv = [ords[i + 1] for i in range(len(lv) - 1)
               if lv[i] >= lv[i + 1]]
        print("    h = %d  %s  --  %s%s"
              % (h, "  ".join("ord %d %.3f" % (o, v)
                              for o, v in zip(ords, lv)),
                 "monotone in the order" if rising else "not monotone",
                 "" if rising else ", inversions at %s"
                 % ", ".join("ord %d" % o for o in inv)))


def main():
    t0 = time.time()
    recs = XT.s1_population()
    XT.s2_pin(recs)
    mapped = XT.s3_profiles(recs)
    section("THE POPULATION IN THIS FILE'S TERMS")
    pop = build_population(mapped)
    print("  %d fields, %d partial places"
          % (len(pop), sum(len(p[3]) for p in pop)))
    check_profiles(pop)
    tables = s4_levels(pop)
    s5_gradients(tables)
    s6_placebo(pop, tables)
    s7_synthetic(pop)
    s8_parent_agreement(pop, mapped)
    s9_variance(pop, tables)
    section("SUMMARY")
    print("  %d checks passed here, %d in the parent, %.1f s wall"
          % (CHECKS, XT.CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
