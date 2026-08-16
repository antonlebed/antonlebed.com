"""WHAT LEVEL DOES THE ORDER LADDER SIT AT, AND IS THE ORDER THE DIAL OR
THE SUBGROUP INDEX? -- the same per-class shares priced ABSOLUTELY against
1/h+ over the (h+, order) table, which is the reading the within-field
pairing cannot give.

THE QUESTION. Probe 2 (explore_class_order.py) found the principal deficit
at small p graded by a class's ORDER in the narrow class group: small order
short, order 5-or-more long, rung by rung a ladder with shrinking steps at
D < 0. Every one of those numbers is a WITHIN-FIELD pairing, and a field's
h+ ratios average to 1 by construction, so what is measured is the ORDERING
of the rungs and never their LEVEL -- if the small orders are short the
large ones MUST be long, and no rung's sign is independent of the others.
Probe 2 filed this in its own WHAT IS NOT CONTROLLED. An absolute reading
is what settles it, and one exists: price each order class against 1/h+
over every field AT ITS h+, which is what explore_principal_share.py
already prints for the trivial class alone. The ladder then either keeps
its shape at fixed h+, or turns out to be one column moving and the rest
reacting.

The same table answers the rival the group level itself raises. A class's
order is the size of the cyclic subgroup it generates, so at a FIXED h+
"small order" and "small subgroup" are one cut and cannot be told apart.
The INDEX h+/ord is the rival, it runs the other way, and it is consistent
with everything probe 2 printed because probe 2 cut no field by h+ at all.
Order and index separate ACROSS h+ and nowhere else: order 2 at h+ = 4 and
order 4 at h+ = 8 are the same index and different orders, and the (h+,
order) table holds both cells.

WHOSE VOCABULARY THE SUSPICION IS WRITTEN IN. Probe 1's was the FORM's (a
class has a minimum) and it graded nothing; probe 2's was the GROUP's (a
class has an order, an inverse, a subgroup) and it graded. This probe stays
in the group's vocabulary deliberately -- it is not hunting a new dial, it
is asking which of two group invariants the surviving grading belongs to,
and where the zero of the scale is. THE TRANSPLANT, flagged: probe 2's
ladder was measured POOLED over h+ and is here asked of individual h+
strata, which is a coarser control than the pairing (a stratum fixes h+, a
pair fixes the field) applied to a finer question. A shape that survives
the pairing is not thereby guaranteed to survive a stratum, and a stratum
cell can be thin where a pooled pairing was not.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE RATIO, AND THE CONSTANT SUM IT OBEYS. For a field of narrow
      class number h with tot0 split primes below the bottom-bin cut and
      n0(C) of them in class C, the ratio is r(C) = n0(C) h / tot0 -- the
      class's share against its nominal 1/h. Since the n0(C) sum to tot0,
      the r(C) sum to h EXACTLY, at every field. That identity is the
      whole reason probe 2 could not read a level, and it is also what
      makes an absolute reading possible at all: 1 is a real zero, set by
      the arithmetic (equidistribution) and not by the other classes.

  (2) WHAT THE CONSTANT SUM STILL FORBIDS, WHICH IS LESS THAN IT LOOKS.
      At a fixed h, let the order-1 (trivial) class run at 1 - d on
      average. Then the remaining h - 1 classes average exactly
      1 + d/(h-1), by (1), over that same population -- an IDENTITY and
      not a prediction, so the COMMON LEVEL of the non-trivial column is
      not a finding and must never be quoted as one. What is NOT forced is
      how that surplus DISTRIBUTES across the orders, and that is the
      finding this probe is after: flat across orders 2, 3, 4, 5+ is one
      column moving and the rest reacting; graded is the ladder with a
      level.

  (3) THREE LAWS, AND THE TABLE SEPARATES THEM. The cell (h, o) holds the
      mean r over every class of order o in a field of narrow class number
      h. Three candidate laws, each a statement that the table is constant
      along one family of lines:
        L_ord: r depends on the ORDER alone -- constant down a column.
        L_h:   r depends on h+ alone -- constant across a row.
        L_idx: r depends on the INDEX h/o alone -- constant along the
               lines o/h fixed, which is the diagonal family.
      L_h is already refuted and by probe 2, not by this rig: within a
      single field h is constant, so L_h forbids ANY within-field variation
      across orders, and probe 2's paired rungs are exactly that variation
      (-0.147 imaginary at order 2 against order 3 on 290 fields). It is
      kept in the comparison as the reference a dial must beat, never as a
      live candidate.

  (4) AND L_ord IS ALREADY IN TROUBLE AT ORDER 1, FROM A PRINTED
      INCUMBENT. The order-1 row of this table IS explore_principal_share's
      trivial-class bottom-bin share by h+, which reads 0.938, 0.815,
      0.764, 0.662 at h+ = 2, 4, 6, 8 on the real side (F1 there). At
      FIXED order the deficit deepens with h+ across a range of 0.28,
      which L_ord forbids outright and L_idx predicts, the trivial class's
      index being h+ itself. So the rival is not idle before the run: it
      already explains a number the corpus has held since probe 0, and the
      contest this rig settles is L_idx against the residual h+ grading,
      not against L_ord. This also fixes the control below at zero cost.

  (5) THE FAIR COMPARISON IS ONE CELL SET GROUPED THREE WAYS. The three
      laws are three PARTITIONS of the identical set of table cells, so
      they are compared by the weighted within-group sum of squares of the
      cell means -- lower is a tighter law -- with each cell weighted by
      its pair count. A partition into more groups wins for free, so the
      group count and the SS per degree of freedom (ncells - ngroups) are
      printed beside the raw SS, and cells that are singletons under any
      grouping are dropped from all three so that no law is scored on a
      group that cannot vary. Nothing here is a significance test; it is a
      ranking, and its inputs are printed so the ranking can be checked by
      eye.

  (6) ORDER 1 IS READ APART, AND THE REASON IS A DERIVED MECHANISM. At
      D < 0 the trivial class carries the one DERIVED mechanism here
      -- its form's minimum is 1, 1 is not prime, so no split prime below
      |D|/4 is principal at all -- so any reading including order 1 mixes
      an explained effect into the dial under test. The primary reading of
      A and B therefore EXCLUDES order 1; the version including it is
      printed beside, because per (4) it is also the index law's strongest
      single piece of evidence, and the two must be weighed apart.

  (7) AND THE SMALL-ORDER SHARE IS THE 2-RANK RELABELLED UNLESS IT IS
      BUILT NOT TO BE. The direct form of the 2-rank reading is asked for:
      the share of a field's group sitting at small order, against the
      trivial class's absolute deficit. But at fixed h+ the count of
      classes of order at most 2 is exactly 2^(t-1), so the share at
      order <= 2 IS the 2-rank, and grading by it would be the 2-rank
      reading wearing a new name -- the failure already paid for once, a
      dial that is a weaker copy of the incumbent. A scalar that is not
      forced to coincide is the SMALL-ORDER WEIGHT s = mean over the
      field's classes of 1/ord(C), which reads the whole order profile and
      not the 2-torsion alone. Whether it separates from the 2-rank at all
      at these h+ is an empirical question this rig prints rather than
      assumes, and a printed answer of "it does not, at any usable
      stratum" is a complete answer to that standing question.

  (8) THE POPULATION IS PROBE 2'S, UNCHANGED, AND THE SWEEP IS IMPORTED
      RATHER THAN REBUILT. Same discriminant bound, same prime cap, same
      bottom bin, same MIN_SPLIT, same composition and the same order walk
      -- so C1 below compares against printed numbers and the composition
      controls C1/C2/C6 of probe 2 re-print here unchanged. WIDENING
      TRIGGER, declared before the run rather than after seeing thin
      cells: if fewer than three h+ strata at a sign carry two or more
      usable order cells, the sweep re-runs at |D| <= 8000 under memwatch
      and both populations are reported.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE, AT BOTH SIGNS.

  P1. THE LADDER KEEPS ITS SHAPE ABSOLUTELY. At each usable h+ stratum,
      the mean r over the orders above 1 RISES with the order, with a
      spread of at least 0.03 between its ends, at both signs where cells
      allow. The reason to expect it: the within-field pairing that
      produced the ladder controls the field and therefore h+ as well, so
      a stratum can only attenuate the shape by mixing order profiles,
      never invert it.

  P2. AND THE INDEX GRADES BETTER THAN THE ORDER. Over the same cell set,
      L_idx carries a lower within-group SS per degree of freedom than
      L_ord, at both signs, with order 1 excluded. The reason is (4)
      restated where it is no longer an identity: if the deficit deepens
      with h+ at fixed order 1, the dial is reading the group AROUND the
      class and not just the class.

  P3. AND THE SMALL-ORDER WEIGHT IS THE 2-RANK AT EVERY USABLE STRATUM.
      Within each h+ stratum with at least 30 fields, the partition of
      fields by the small-order weight s and the partition by 2-rank
      COINCIDE, at both signs -- so the direct form is not a second
      dial here, and no comparison of the two is available in this
      population.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, weighed for meaning only
after the controls are read.

  K1 kills P1: the printed per-stratum column of mean r by order over
     orders above 1, cells of at least MINCELL pairs. A column whose ends
     differ by less than 0.03, or which falls rather than rises, at a sign
     with two or more usable cells, is the kill -- and a FLAT column is
     the named rival (one column moving, the rest reacting) rather than
     noise.

  K2 kills P2: the printed SS-per-degree-of-freedom triple for L_ord, L_h
     and L_idx over the identical cell set, order 1 excluded. L_ord at or
     below L_idx at either sign is the kill.

  K3 kills P3: the printed count, per stratum, of distinct 2-ranks and of
     distinct small-order weights, and of distinct pairs. Any stratum
     where the pair count exceeds both is a stratum where the two dials
     separate, and P3 dies there -- which is the informative outcome, and
     the rig then prints the trivial class's mean r at each pair.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. THE INCUMBENT'S ORDER-1 ROW. The order-1 cells at h+ = 2, 4, 6, 8 on
      the real side must reproduce explore_principal_share.py's F1 row of
      trivial-class bottom-bin shares -- 0.938, 0.815, 0.764, 0.662 -- to
      within 0.05, the slack being the population difference of probe 2's
      composition controls and nothing else. A rig that disagrees with the
      incumbent on the incumbent's own absolute statistic is wrong until
      shown otherwise, and this is the statistic the whole probe is built
      on.

  C2. THE CONSTANT SUM, MEASURED AND NOT ASSUMED. Derivation (1) says the
      r(C) of a field sum to h+ exactly. Printed as the maximum absolute
      deviation over every kept field of both signs. Anything above 1e-9
      voids every absolute number in this rig, since the zero of the scale
      is what that identity fixes.

  C3. THE REACTION IDENTITY. Derivation (2) says the non-trivial column's
      common level at a stratum equals 1 + d/(h-1) with d the stratum's
      order-1 deficit. Printed as the maximum deviation over the strata.
      It is a check on the stratification arithmetic AND the standing
      reminder that the level of that column is not a finding.

  C6 (added at audit, and K1 is not readable without it). THE
      EXCHANGEABILITY PLACEBO. K1's spread threshold was frozen with no
      noise scale behind it, which is a kill criterion whose null was
      never derived. The null is that a field's non-trivial classes are
      exchangeable, so the ORDER LABELS are rotated within each field over
      five fixed offsets -- same order multiset, same cell sizes, same
      constant sum, trivial class held fixed -- and the same spread read
      off the result. Printed per stratum beside the observed spread.

  C4. PROBE 2'S OWN PAIRED NUMBER, THROUGH THE IMPORTED SWEEP. The
      within-field paired ambiguous-vs-non-ambiguous bottom-bin gap must
      still print -0.1507 real on 189 fields and -0.2160 imaginary on 880.
      The sweep is imported rather than copied, so this is the check that
      the import is the object probe 2 measured.

  C5. THE COMPOSITION CONTROLS, RE-PRINTED. Probe 2's C1, C2 and C6 come
      through the imported sweep as violation counts and must all be zero:
      discriminant and integrality, key in inventory, walk overrun, order
      divides h+, two-sided identity, and the order-at-most-2 count against
      the independent form-symmetry ambiguity test.

THE FINDINGS.

  THE CONTROLS. C5 prints zero at all eight counts over 1216 real and 1217
  imaginary fields -- the imported sweep is the object probe 2 measured.
  C2 prints 7.1e-15 real and 7.1e-14 imaginary for the constant sum, which
  is float noise and not a deviation, so the absolute zero this probe reads
  against is the arithmetic one. C4 reproduces probe 2's paired statistic
  exactly, -0.1507 on 189 real fields and -0.2160 on 880 imaginary. C3
  prints 0.0 and 2.2e-16 for the reaction identity. And C1 reproduces the
  INCUMBENT'S OWN ROW to three decimals with no slack used: the order-1
  cells read 0.938, 0.815, 0.764, 0.662 at h+ = 2, 4, 6, 8 on the real
  side against explore_principal_share.py's F1 of exactly those four
  numbers. The order-1 row of this table IS that incumbent statistic, so
  the whole (h+, order) table is an extension of a number the corpus has
  held since probe 0 rather than a new measurement resting on new code.

  **THE LADDER HAS A LEVEL AND THE REACTING COLUMN DIES, BUT THE RISE IS
  NOT EXCEPTIONLESS** (observation; P1 survives on the spread at 12 of 13
  strata once C6 supplies the scale the kill lacked, and K1's monotonicity
  clause fires at four imaginary strata). Priced absolutely against 1/h+
  instead of against the field's other classes, the spread across a
  stratum's orders runs 0.050, 0.062, 0.098 at h+ = 4, 6, 8 real and 0.064
  to 0.279 over the ten imaginary strata from h+ = 4 to 28. **THE FROZEN
  0.03 IS NOT THE RIGHT LINE TO READ THAT AGAINST AND C6 SAYS SO**: rotate
  the order labels within each field and the same statistic still returns
  0.003 to 0.125, so a spread of 0.03 is inside the noise at most strata
  and the kill as frozen would have passed on nothing. Against the
  placebo the reading is sharper than the threshold made it look -- the
  observed spread exceeds ALL FIVE rotated draws at 12 of the 13 usable
  strata, the single exception being imaginary h+ = 6 (0.1066 against a
  placebo reaching 0.1089). The five draws are five DISTINCT tables at
  every stratum but the two at h+ = 4, where a field admits only three
  rotations and the rig prints so. So the ladder is NOT one column moving and the
  rest reacting, which was the named rival, and the evidence for that is
  the placebo comparison and not the frozen number.
  The rise is exceptionless at the real side and at six of the ten
  imaginary strata. Where it breaks, it breaks at an ODD-order cell every
  time and at no other -- AND WHAT CARRIES THAT IS WHERE THE INVERSIONS
  FALL, NOT HOW BIG THEY ARE, which C6 is equally the scale for: three of
  the four steps below are smaller than their own stratum's placebo
  spread (0.043 against 0.109 at h+ = 6, 0.029 against 0.061 at 10, 0.060
  against 0.080 at 12) and only h+ = 20 clears alone, at 0.122 against
  0.080. Four of four at odd cells and none at an even one is the
  observation; the individual steps are not four results: h+ = 6 puts order 3 at 0.9919 below order 2 at
  1.0346, h+ = 10 puts order 5 at 1.0122 below order 2 at 1.0407, h+ = 12
  puts order 3 at 0.9516 below order 2 at 1.0112, and h+ = 20 puts order 5
  at 0.9475 below order 4 at 1.0691. The strata whose orders are ALL powers
  of 2 -- h+ = 4, 8, 16 imaginary and 4, 8 real -- rise without exception,
  and the one even-order inversion anywhere in the table is order 4 at
  1.0915 above order 6 at 1.0797 at h+ = 12, on 74 pairs against 494. So
  the order grades the level, and the odd part of the order does not
  participate in the grading the way its size says it should.

  **AND THE INDEX IS NOT THE DIAL -- THE ORDER IS** (observation; P2 DIES,
  K2 fires at both signs on every reading that could be scored). Over the
  identical cell set grouped three ways, order 1 excluded, the imaginary
  side scores L_ord at 0.124 SS per degree of freedom against L_idx at
  0.247 and L_h at 0.746 on 31 cells; including order 1 it is 0.343
  against 1.081 and 2.748 on 38 cells, and the real side (unrankable with
  order 1 excluded, no cell surviving) reads 0.818 against 3.178 and 4.816
  on 7. The index loses by a factor of two everywhere and loses hardest on
  the reading built to flatter it. The pre-engine argument for it,
  derivation (4), was sound and is answered rather than confirmed: the
  order-1 row DOES fall with h+, but so does every fixed-order row, and
  the index cannot absorb both because it forces cells of different order
  together -- at h+ = 6 it puts order 3 (index 2, 0.992) BELOW order 2
  (index 3, 1.035), the wrong way round for a law where a bigger index is
  a bigger deficit.

  **AND THE SECOND GRADIENT IS h+, PINNED AT THE GENERATORS** (observation;
  this is what the SS residual is made of, and it is the reading the level
  question was actually asking for). The table has two gradients, not one.
  At fixed order the level falls with h+, and it falls in a STEP rather
  than rung by rung: order 2 imaginary runs 1.032, 1.035, 1.012, 1.041,
  1.011, 0.966, 0.919, 0.916, 0.814 over h+ = 4, 6, 8, 10, 12, 16, 20, 24,
  28 -- spanning 1.011 to 1.041 through h+ = 12, then dropping -- while
  order 1, the one order that falls monotonically, runs 0.833 down to
  0.334 over h+ = 4 to 20. The step sits at the same place the 2-rank
  grading below turns over. But one line of the table does NOT move: the
  cells where the order EQUALS h+ -- the generators, index 1, which exist
  only where the group is CYCLIC and therefore rest on a NARROWER
  population than any other line of the column -- read
  1.096, 1.099, 1.079, 1.085, 1.087, 1.091, 1.105, 1.100, 1.096, 1.094
  across those same ten strata, a spread of 0.026 with no trend, against
  the 0.23 the order-2 line moves over the same range (1.041 down to
  0.814). So the ladder's TOP
  is level-invariant and everything below it falls away as the group
  grows. That is an absolute anchor, which is exactly what probe 2's
  constant-sum constraint said no within-field reading could supply, and
  it is the shape any derivation now has to hit: not one number per order,
  but a fixed ceiling with a shortfall that deepens with h+ at every order
  below the top.

  **AND THE SMALL-ORDER SHARE IS THE 2-RANK, AT EVERY STRATUM THAT CAN
  CARRY A COMPARISON** (P3 SURVIVES on K3, and it closes the standing
  item rather than answering it). The partition of fields by the
  small-order weight s = mean 1/ord coincides with the partition by 2-rank
  at every usable stratum of both signs, with one exception that is not
  one: at h+ = 16 imaginary, s splits the 2-rank-2 fields into 46 and ONE.
  So the direct form asked for above is not a second dial in
  this population, and the corpus should stop expecting one from it -- a
  scalar reading the whole order profile is the 2-rank relabelled here,
  which is derivation (7)'s flag paid rather than dodged.

  **AND THE 2-RANK GRADING OF THE TRIVIAL CLASS REVERSES ABOVE h+ = 16**
  (observation; the same reading, at strata the incumbent never reached).
  The trivial class's absolute ratio by 2-rank reproduces the incumbent
  t-grading
  EXACTLY where the two overlap -- 0.734, 0.706, 0.599 over 2-ranks 1, 2,
  3 at h+ = 8 real, against 0.734, 0.706, 0.599 at t = 2, 3, 4 there --
  and the imaginary side agrees in shape (0.704, 0.675, 0.549). It holds
  at h+ = 4 (0.857, 0.806 real; 0.862, 0.796 imaginary) and weakly at
  h+ = 12 (0.533, 0.512). Then it turns over: h+ = 16 is flat and
  non-monotone (0.425, 0.434, 0.406), and h+ = 20, 24 and 28 run the OTHER
  WAY -- 0.324 then 0.341; 0.223, 0.316, 0.402; 0.120 then 0.226 -- with
  the deficit SHALLOWEST at the largest 2-rank. The incumbent's claim was
  read at h+ = 4 and 8 and is true there; stated without a ceiling it is
  false, and the ceiling sits between 12 and 20. This is the same
  statistic, not a re-derived one, which is why the reversal is quotable.

RUN RECORD: wall 4.5 s, peak working set 178.2 MB under memwatch at a 512
MB ceiling. 1216 real and 1217 imaginary fundamental discriminants to
|D| <= 4000 over the odd split p <= 10^4, probe 2's population unchanged
per derivation (8). The widening trigger of (8) did NOT fire: the
imaginary side carries ten strata with two or more usable order cells and
the real side three, against the three the trigger asked for. Pure Python,
no new sweep -- the cost is probe 2's sweep run once per sign and the
table built over its output.

WHAT IS NOT CONTROLLED, stated rather than left for a reader to find. A
stratum fixes h+ and nothing else, so the cells of one column mix fields of
different group STRUCTURE -- a cyclic C8 field and a C2 x C4 field both sit
at h+ = 8 and carry different order profiles, and any column effect is a
mixture over those profiles rather than a statement about one. The three
laws are compared as partitions of a table, which is a ranking and not a
test: no error bars are computed on a cell mean, and two laws close in SS
are not thereby distinguished. C6's draws are not independent either, and
in two ways it prints rather than hides: a field of narrow class number h
admits only h - 1 rotations, so five offsets give FEWER than five
distinct tables at the small strata and the count of distinct draws is
printed beside them; and the rotation runs over the classes SORTED BY
KEY, which for a definite form is sorted by the class minimum, so the
draws preserve whatever the minimum carries instead of destroying it. If
the minimum carries any of the share, that makes the placebo spread too
LARGE and the comparison conservative -- but the direction is an argument
and not a measurement, and a placebo built on an independent shuffle
would settle it. The index-1 line is the sharpest case of
the mixture problem rather than an exception to it: a class of order h+
exists only in a CYCLIC group, so that line is measured on a subset of
each stratum's fields while every other line pools cyclic and non-cyclic
ones -- its flatness across h+ is a fact about those fields, and reading
it against the order-2 line is a comparison across two populations. And the index law and the h+ law are close
relatives on this population -- the index equals h+ at every order-1 cell
and stays within a factor of the small orders -- so a win for L_idx over
L_ord is a cleaner statement than a win for L_idx over L_h.
"""

import os
import sys
import time
from collections import defaultdict

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_class_order as P2                # noqa: E402
from explore_principal_share import primes_upto  # noqa: E402
from explore_class_share import mean             # noqa: E402

MINCELL = 50              # pairs a (h+, order) cell needs to be read
MINSTRAT = 30             # fields an h+ stratum needs to be read


def strip(rows):
    """Drop the per-field prime list once the counts are extracted."""
    return [(D, h, recs, orders, n0, tot0, q, ())
            for (D, h, recs, orders, n0, tot0, q, hits) in rows]


def table(rows):
    """(h+, order) -> list of r; plus h+ -> field count and order-1 r."""
    cells = defaultdict(list)
    fields = defaultdict(int)
    triv = defaultdict(list)
    worst = 0.0
    for D, h, recs, orders, n0, tot0, q, _ in rows:
        if h == 1 or tot0 == 0:
            continue
        fields[h] += 1
        tot = 0.0
        for key in recs:
            r = P2.ratio(n0.get(key, 0), tot0, h)
            tot += r
            cells[(h, orders[key])].append(r)
            if orders[key] == 1:
                triv[h].append(r)
        worst = max(worst, abs(tot - h))
    return cells, fields, triv, worst


def table_placebo(rows, shift):
    """C6: the same table with the ORDER LABELS rotated within each field.

    K1 reads a SPREAD across the orders of a stratum against a threshold
    frozen with no noise scale behind it, which is what this supplies. The
    null K1 is against is that the non-trivial classes of a field are
    EXCHANGEABLE -- one column moving and the rest reacting equally. So
    rotate which non-trivial class carries which order, by a fixed offset
    read off |D| plus `shift` so the control reproduces: the field's order
    MULTISET is untouched, every cell keeps its exact size, the constant
    sum still holds, and the trivial class stays where it is -- order 1
    carries a derived mechanism and is not exchangeable with anything.
    Any spread left is what this statistic shows on structure that is not
    there.
    """
    cells = defaultdict(list)
    for D, h, recs, orders, n0, tot0, q, _ in rows:
        if h == 1 or tot0 == 0:
            continue
        keys = sorted(k for k in recs if orders[k] != 1)
        if not keys:
            continue
        labels = [orders[k] for k in keys]
        start = (abs(D) + shift) % len(keys)
        for i, k in enumerate(keys):
            cells[(h, labels[(i + start) % len(keys)])].append(
                P2.ratio(n0.get(k, 0), tot0, h))
        for k in recs:
            if orders[k] == 1:
                cells[(h, 1)].append(P2.ratio(n0.get(k, 0), tot0, h))
    return cells


def spread_of(cells, h):
    """K1's own observable at one stratum: max - min over orders above 1."""
    vals = [mean(v) for (hh, o), v in cells.items()
            if hh == h and o > 1 and len(v) >= MINCELL]
    return (max(vals) - min(vals)) if len(vals) >= 2 else None


def cell_means(cells, fields, drop_order_1):
    """Usable cells only: stratum big enough, cell big enough."""
    out = {}
    for (h, o), vals in cells.items():
        if fields[h] < MINSTRAT or len(vals) < MINCELL:
            continue
        if drop_order_1 and o == 1:
            continue
        out[(h, o)] = (mean(vals), len(vals))
    return out


def within_ss(cm, keyfn):
    """Weighted within-group SS of cell means under one grouping."""
    grp = defaultdict(list)
    for (h, o), (m, n) in cm.items():
        grp[keyfn(h, o)].append((m, n))
    ss = 0.0
    for members in grp.values():
        w = sum(n for _, n in members)
        mu = sum(m * n for m, n in members) / w
        ss += sum(n * (m - mu) ** 2 for m, n in members)
    return ss, len(grp)


GROUPINGS = (("L_ord  (order alone)", lambda h, o: o),
             ("L_h    (h+ alone)", lambda h, o: h),
             ("L_idx  (index h+/o)", lambda h, o: h // o))


def law_ranking(cm, label):
    """K2: the same cell set scored under the three laws."""
    keep = dict(cm)
    while True:                                      # derivation (5)
        before = len(keep)
        for name, fn in GROUPINGS:
            sizes = defaultdict(int)
            for (h, o) in list(keep):
                sizes[fn(h, o)] += 1
            keep = {k: v for k, v in keep.items() if sizes[fn(*k)] > 1}
        if len(keep) == before:                      # dropping a cell can
            break                                    # orphan another, so
                                                     # this runs to fixpoint
    print("    %s: %d cells survive the no-singleton rule" % (label, len(keep)))
    if len(keep) < 3:
        print("      too few cells to rank")
        return keep
    for name, fn in GROUPINGS:
        ss, g = within_ss(keep, fn)
        df = len(keep) - g
        print("      %-22s SS %8.4f over %2d groups, df %2d, SS/df %s"
              % (name, ss, g, df, ("%.5f" % (ss / df)) if df > 0 else "--"))
    return keep


def small_order_weight(recs, orders):
    return sum(1.0 / orders[k] for k in recs) / len(recs)


def rank2(recs, orders):
    n = sum(1 for k in recs if orders[k] <= 2)
    return n.bit_length() - 1


def main():
    t0 = time.time()
    plist = primes_upto(P2.PCAP)
    print("population: |D| <= %d both signs, odd split p <= %d, bottom bin"
          " p < %d, min split %d; cells need %d pairs, strata %d fields"
          % (P2.DBOUND, P2.PCAP, P2.BIN0, P2.MIN_SPLIT, MINCELL, MINSTRAT))

    out, tabs = {}, {}
    for sign, name in ((+1, "real"), (-1, "imag")):
        rows, bad, idb, c2b, c4b, lawb = P2.sweep(sign, plist)
        out[sign] = strip(rows)
        tabs[sign] = table(out[sign])
        print("\n%s: %d fields kept" % (name, len(rows)))
        print("  C5 composition: disc/integrality %d | key not in inventory"
              " %d | walk overran %d | order does not divide h+ %d |"
              " identity %d | non-commuting %d | non-associative %d |"
              " order<=2 vs form-symmetry disagreements %d"
              % (bad[0], bad[1], bad[2], bad[3], idb, lawb[0], lawb[1], c2b))

    print("\n--- C2: the constant sum. Derivation (1) says a field's r(C)"
          "\n    sum to h+ exactly; the absolute zero rests on it.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        print("  %-5s max |sum r - h+| over kept fields: %.3e"
              % (name, tabs[sign][3]))

    print("\n--- C4: probe 2's own paired statistic through the imported"
          "\n    sweep. explore_class_order.py C3 printed -0.1507 on 189"
          "\n    real fields and -0.2160 on 880 imaginary.")
    famb = lambda k, r, o: r[2] and not r[0]           # noqa: E731
    fnon = lambda k, r, o: not r[2]                    # noqa: E731
    for sign, name in ((+1, "real"), (-1, "imag")):
        g, n, frac = P2.paired(out[sign], famb, fnon)
        print("  %-5s %+.4f on %d fields, ambiguous lower at %.3f"
              % (name, g, n, frac))

    print("\n--- C1: the order-1 row against the incumbent. F1 of"
          "\n    explore_principal_share.py prints the trivial class's"
          "\n    bottom-bin share by h+ on the real side as 0.938, 0.815,"
          "\n    0.764, 0.662 at h+ = 2, 4, 6, 8.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        cells, fields, triv, _ = tabs[sign]
        row = ["h+ %d: %.3f (%d fields)" % (h, mean(triv[h]), fields[h])
               for h in (2, 4, 6, 8) if h in triv]
        print("  %-5s %s" % (name, " | ".join(row)))

    print("\n--- READING A / K1: THE ABSOLUTE COLUMN. Mean r by order at"
          "\n    fixed h+, which prices each order against 1/h+ instead of"
          "\n    against the field's other classes. Order 1 is printed"
          "\n    apart per derivation (6): at D < 0 it carries the derived"
          "\n    hard zero. The non-trivial column's common LEVEL is the"
          "\n    identity of derivation (2) and is not a finding -- only"
          "\n    its distribution across the orders is.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        cells, fields, triv, _ = tabs[sign]
        print("  %s:" % name)
        for h in sorted(fields):
            if fields[h] < MINSTRAT:
                continue
            usable = [(o, mean(v), len(v)) for (hh, o), v in
                      sorted(cells.items()) if hh == h and len(v) >= MINCELL]
            if not usable:
                continue
            body = "  ".join("ord %d: %.4f (%d)" % u for u in usable)
            above = [u for u in usable if u[0] > 1]
            if len(above) >= 2:
                spread = max(u[1] for u in above) - min(u[1] for u in above)
                rising = all(above[i][1] <= above[i + 1][1]
                             for i in range(len(above) - 1))
                verdict = "spread %.4f over %d cells, rising %s" % (
                    spread, len(above), rising)
            else:
                verdict = "fewer than 2 usable cells above order 1"
            d = 1.0 - mean(triv[h]) if h in triv else float("nan")
            print("    h+ %-3d (%4d fields) %s\n         %s | reaction"
                  " identity 1+d/(h-1) = %.4f"
                  % (h, fields[h], body, verdict, 1 + d / (h - 1)))

    print("\n--- C3: the reaction identity, measured. The pair-weighted"
          "\n    mean of r over the classes of order above 1 at a stratum"
          "\n    must equal 1 + d/(h-1) exactly.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        cells, fields, triv, _ = tabs[sign]
        worst = 0.0
        for h in sorted(fields):
            if fields[h] < MINSTRAT or h not in triv:
                continue
            vals = [r for (hh, o), v in cells.items() if hh == h and o > 1
                    for r in v]
            if not vals:
                continue
            d = 1.0 - mean(triv[h])
            worst = max(worst, abs(mean(vals) - (1 + d / (h - 1))))
        print("  %-5s max deviation over strata: %.3e" % (name, worst))

    print("\n--- C6 (added at audit, and K1 is not readable without"
          " it): K1's spread threshold was frozen with no noise scale."
          "\n    The null is that a field's non-trivial classes are"
          " EXCHANGEABLE, so the order labels are ROTATED within each"
          "\n    field -- same multiset, same cell sizes, same"
          " constant sum, trivial class fixed -- and the same spread"
          "\n    read off the result, over five fixed offsets.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        cells, fields, triv, _ = tabs[sign]
        print("  %s:" % name)
        for h in sorted(fields):
            if fields[h] < MINSTRAT:
                continue
            obs = spread_of(cells, h)
            if obs is None:
                continue
            pl = [spread_of(table_placebo(out[sign], k), h)
                  for k in range(1, 6)]
            pl = [x for x in pl if x is not None]
            print("    h+ %-3d observed %.4f | placebo %s | max %.4f |"
                  " %d distinct of %d draws"
                  % (h, obs, " ".join("%.4f" % x for x in pl),
                     max(pl) if pl else float("nan"),
                     len({round(x, 6) for x in pl}), len(pl)))

    print("\n--- READING B / K2: WHICH LAW THE TABLE OBEYS. The identical"
          "\n    cell set grouped three ways -- by order, by h+, by index"
          "\n    h+/ord -- scored by weighted within-group SS of the cell"
          "\n    means. Lower is tighter. L_h is the reference probe 2"
          "\n    already refuted within a field, not a live candidate.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        cells, fields, triv, _ = tabs[sign]
        print("  %s:" % name)
        cm = cell_means(cells, fields, drop_order_1=True)
        kept = law_ranking(cm, "order 1 excluded (primary)")
        cm_all = cell_means(cells, fields, drop_order_1=False)
        law_ranking(cm_all, "order 1 included (index law's own evidence)")
        print("    the RANKED cells, order 1 excluded (%d of the %d usable"
              " cells; the rest are singletons under some grouping): %s"
              % (len(kept), len(cm),
                 ", ".join("(h+%d,o%d)=%.3f" % (h, o, m)
                           for (h, o), (m, n) in sorted(kept.items()))))

    print("\n--- READING C / K3: IS THE SMALL-ORDER SHARE THE 2-RANK? Per"
          "\n    stratum, the partition of fields by 2-rank against the"
          "\n    partition by the small-order weight s = mean 1/ord. At"
          "\n    fixed h+ the share at order <= 2 IS 2^(t-1)/h+, so only a"
          "\n    scalar reading the whole order profile can separate.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        print("  %s:" % name)
        prof = defaultdict(lambda: defaultdict(list))
        counts = defaultdict(int)
        for D, h, recs, orders, n0, tot0, q, _ in out[sign]:
            if h == 1 or tot0 == 0:
                continue
            counts[h] += 1
            triv_key = [k for k in recs if orders[k] == 1][0]
            s = round(small_order_weight(recs, orders), 6)
            prof[h][(rank2(recs, orders), s)].append(
                P2.ratio(n0.get(triv_key, 0), tot0, h))
        for h in sorted(prof):
            if counts[h] < MINSTRAT:
                continue
            pairs = prof[h]
            ranks = {p[0] for p in pairs}
            weights = {p[1] for p in pairs}
            sep = len(pairs) > max(len(ranks), len(weights))
            print("    h+ %-3d %4d fields | %d distinct 2-ranks, %d distinct"
                  " s, %d distinct pairs -> %s"
                  % (h, counts[h], len(ranks), len(weights), len(pairs),
                     "THEY SEPARATE" if sep else "one partition"))
            if sep or len(pairs) > 1:
                for p in sorted(pairs):
                    print("        2-rank %d, s %.4f: trivial r %.4f on %d"
                          " fields" % (p[0], p[1], mean(pairs[p]),
                                       len(pairs[p])))

    print("\nwall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
