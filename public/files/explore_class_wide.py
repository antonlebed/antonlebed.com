"""DOES THE SURVIVING QUADRATIC COMPONENT SURVIVE A DOUBLING OF THE
POPULATION, AND DOES THE REAL SIDE BECOME READABLE? -- probe 6's held-out
reading and its orbit null, run at |D| <= 4000 and again at |D| <= 8000 in
one process, so the two population sizes are compared by the same code path
rather than across two docstrings.

THE QUESTION, AND WHY IT IS A KILL RATHER THAN AN EXTENSION. Probe 6
(explore_class_null.py) gave the held-out reading its first null and the
component came in at 1.206 times the top of that null's band, pooled
field-weighted over the 344 fields at the seven strata of complement real
dimension >= 3. Three things are wrong with that as a finding. The strata
disagree -- four clear their whole band, two sit inside theirs and one sits
below the whole of its own -- and nothing printed selects the survivors.
Every gated stratum is IMAGINARY, so there is no two-sign statement and
never has been. And each per-stratum band is a range over five fixed
offsets that collapse to as few as two distinct draws. A component that is
real only pooled, absent at three strata singly, unexplained in its pattern
and one-signed is the shape the charter's HARD PIVOT names: the burden is
on continuing, and one run at twice the discriminant bound discharges it.

WHOSE VOCABULARY THE SUSPICION IS WRITTEN IN. Probe 6's, unchanged and
imported -- the object is the same residual, the null is the same rotation
within inverse orbit size, the gate is the same complement dimension. This
probe introduces no new statistic; it changes ONE parameter and reads the
same columns at both of its values. THE TRANSPLANT, flagged: nothing is
carried from a neighbouring parameter value here, because both values are
run. What IS inherited without re-derivation is probe 5's decomposition and
probe 2's composition, whose violation counts are re-printed at both bounds.

THE HAND-DERIVATION (pre-engine, on paper, one line per VARIABLE).

  (1) THE WIDENING IS THE ONLY CHANGE, AND IT IS A MODULE GLOBAL. The
      sweep reads its discriminant bound from explore_class_order.DBOUND at
      call time, so setting that global and re-calling probe 5's collect is
      the whole of the widening. The prime cap (10^4), the bottom bin, the
      minimum split count, the 30-field stratum floor, the five placebo
      offsets, the iso-type strata and the complement-dimension gate are
      all untouched, and each is printed at both bounds so the claim that
      they are untouched is checkable rather than asserted.

  (2) THE GATE AND THE NULL'S DEGENERACY ARE THE SAME FACT, WHICH IS WHY
      THE KILL'S DENOMINATOR CANNOT BE DEGENERATE. A finite abelian group
      has exactly as many characters of order dividing 2 as elements of
      order dividing 2, so writing n2 for the non-trivial ones of either,
      the number of characters of order > 2 is h - 1 - n2 and the number of
      CLASSES of order > 2 is the same. The printed complement dimension
      counts conjugate pairs of characters of order > 2, and the orbit
      rotation's pair family counts inverse orbits of classes of order > 2;
      both are (h - 1 - n2)/2 and they are EQUAL at every stratum. So a
      stratum at complement dimension >= 3 has at least three two-element
      orbits, the pair family admits a non-identity offset, and the null on
      the gated set is never the treatment under another name. Probe 6
      found degenerate nulls only at complement dimension 1, and this is
      the reason it could not have found one above 2.

  (3) THE KILL IS A RATIO AND ITS DENOMINATOR SHRINKS WITH THE POPULATION.
      The pooled band is the range over five offsets of a FIELD-WEIGHTED
      MEAN, and each field's offset is set by |D| mod (m-1), so across many
      fields the five means are five averages of decorrelated per-field
      draws and their spread falls like n^(-1/2). Doubling n therefore
      narrows the band by about sqrt(2) and RAISES the ratio to the band's
      TOP with nothing underneath it changing. At probe 6's pooled figures
      -- MIDPOINT 0.1313, half-width 0.0048, a relative half-width of 3.7%
      -- that mechanical rise carries 1.206 to about 1.217, which is small
      against the frozen floor of 1.1 and so does not threaten the kill.
      But the ratio to the band's MEAN is the population-stable statistic
      (about 1.25 at probe 6 read off the midpoint), and both are printed
      at both bounds with the relative half-width beside them, so the
      narrowing is MEASURED here rather than predicted here. TWO CORRECTIONS
      AT AUDIT, both to this paragraph's arithmetic and neither to its
      conclusion. The midpoint is not the mean: probe 6 printed only the
      band's min and max, so the midpoint was all that was available before
      the run, and the rig's own mean of the five offset means puts the
      4000 arm at 0.1345 and its true relative half-width at 3.57%, so the
      probe-6 mean ratio is 1.231 and not 1.25. Reading a band's centre off
      its edges is the same conflation this derivation exists to warn about,
      committed one line into the warning. And the measured narrowing is
      0.62 rather than the 1/sqrt(2) predicted here, because the strata
      count rises with the field count and each new stratum averages too.

  (4) WHAT A LARGER POPULATION MOVES AND WHAT IT CANNOT. The strata are iso
      types, which are properties of a field and not of the sample, so no
      existing stratum's group gets richer: its distinct-draw count per
      field is fixed by its group and rises only by new, larger types
      crossing the 30-field floor. What the widening does move is the
      number of fields per type, the number of types above the floor, and
      the tightness of every cell mean. That is why the real side is a
      counting question and not a design question: a real stratum becomes
      readable only if some iso type with h+ - 1 - n2 >= 6 reaches 30
      fields.

  (5) A STRATUM WITH NO CHARACTER OF ORDER 2 HAS NO TESTED COORDINATE, AND
      THE INHERITED READABILITY TEST DOES NOT SAY SO -- added at audit,
      after the first run and before any finding was written. Probe 5's
      test admits an iso type carrying more than one character ORDER, which
      an odd-order group passes; but the statistic under test is the energy
      at the characters of order exactly 2, so over an odd-order group its
      numerator is an empty sum and RES-h*, RES-a* and the whole band are
      identically 0.0000 by construction. Probe 6 never met one because no
      odd-order iso type cleared the 30-field floor at |D| <= 4000; at 8000
      cyclic Z/15 does, and it entered the gate at complement dimension 7
      contributing 31 fields of structural zeros to both halves of the
      pooled ratio. Readability here therefore also requires n2 >= 1, and
      the count of strata dropped for that reason is printed per sign.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. THE POOLED COMPONENT SURVIVES THE DOUBLING. At |D| <= 8000 the
      pooled RES-h* over the complement-dimension >= 3 strata clears the
      whole pooled NULL-B band, with a ratio to the band's top above 1.1.
      The reason: the object is unchanged and the statistic was 1.206 at
      half this population with four of seven strata clearing singly, so
      only a sampling accident at 4000 would put it inside the band here.

  P2. THE REAL SIDE STAYS EMPTY. No REAL iso type reaches complement real
      dimension >= 3 with 30 or more fields even at |D| <= 8000. The
      reason: that gate needs h+ - 1 - n2 >= 6, and the narrow class
      groups of real quadratic fields in this range are overwhelmingly of
      small order with their non-trivial part 2-torsion; doubling the
      sample doubles the count of a rare type rather than making it
      common. This prediction is the one the roadmap's move was aimed at
      buying, and it is frozen as a NO so that the run decides it.

  P3. THE PER-STRATUM PATTERN STAYS UNEXPLAINED. Over the gated strata at
      |D| <= 8000, the ratio to the band's top is not monotone in class
      number, nor in complement dimension, nor in rank. The reason: probe
      6 found no order over seven strata, and more strata is more chances
      to break a spurious order rather than to create a real one.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS. Each is arithmetic on a
printed number; the meaning is weighed after the controls are read.

  K1 kills P1, and it is the roadmap's frozen observable verbatim: the
     printed pooled RES-h* at |D| <= 8000 against the printed pooled
     NULL-B band at complement dimension >= 3. Inside the band, or a
     printed ratio to the band's top below 1.1, is the kill.

  K2 kills P2: the printed count of REAL strata at complement dimension
     >= 3 that clear the field floor at |D| <= 8000. One or more is the
     kill.

  K3 kills P3: the gated strata printed sorted by their ratio to the
     band's top, with h, complement dimension and rank beside each. If
     that ratio is monotone in any one of the three columns across every
     gated stratum, P3 is dead.

THE POSITIVE CONTROLS, run and read FIRST, at BOTH bounds.

  N1. THE ORBIT ROTATION PRESERVES WHAT DERIVATION (3) OF PROBE 6 SAYS IT
      DOES. Over every kept field and every draw: max |sum of the rotated
      residual - sum of the treatment residual|, max relative deviation of
      the rotated residual's total energy from the treatment's, and max
      |E_0| of its transform. Above 1e-9 voids every null reading.

  N2. THE ORBIT ROTATION PRESERVES SYMMETRY EXACTLY. Max over fields and
      draws of |v(C) - v(C^-1)| on the rotated residual, and max |Im E_j|
      of its transform. Above 1e-9 means the orbit partition is wrong.

  N3. THE ROTATION IS NOT THE IDENTITY, AND WHERE IT IS THE ROW SAYS SO.
      Mean distinct draws per field and the two orbit counts, per stratum,
      with a degeneracy verdict printed on the row rather than inferred.
      Derivation (2) says no gated row may carry it.

  N4. THE IDENTITY DRAW REPRODUCES THE TREATMENT. Max over kept fields of
      |RES-h*(zero offset) - RES-h*|. Above 1e-12 means the null pipeline
      and the treatment pipeline are not the same pipeline.

  N5. THE IMPORTED SWEEP IS THE ONE PROBES 2 THROUGH 6 MEASURED. Probe 2's
      eight composition counts and probe 5's five decomposition counts,
      re-printed at both bounds, all zero.

  N6. THE |D| <= 4000 ARM REPRODUCES PROBE 6. Every figure in the 4000
      table -- RES-a*, RES-h*, the band, the pooled line -- must agree with
      explore_class_null.py's printed figures to the printed digits. This
      arm exists to make the comparison exact, so a disagreement anywhere
      in it voids the comparison and not just the arm.

THE FINDINGS.

  THE CONTROLS, at BOTH bounds. N5 prints probe 2's eight composition
  counts and probe 5's five decomposition counts at zero over all four
  populations. The orbit rotation's identities hold exactly or at float
  noise: N1 prints the constant sum preserved EXACTLY (0.00e+00) at both
  signs and both bounds, the residual's total energy to 1.4e-15 relative
  and |E_0| to 1.5e-14; N2 prints the symmetry |v(C) - v(C^-1)| preserved
  EXACTLY (0.00e+00) everywhere with the transform's largest imaginary part
  at 7.1e-15; N4 prints the identity draw reproducing the treatment
  EXACTLY. N6 holds to every printed digit: the |D| <= 4000 arm returns 7
  gated strata over 344 fields with pooled RES-h* 0.1640 against NULL-B
  0.1265-0.1361 and a top ratio of 1.206, which is explore_class_null.py's
  line. Derivation (5) drops exactly one iso type across the four
  populations -- imaginary Z/15, 31 fields, at |D| <= 8000 only. And
  derivation (2) is confirmed rather than assumed: it predicts that a
  stratum's complement dimension EQUALS its count of two-element inverse
  orbits, and the two are computed by different routes -- one over the
  character table, one over the class inversion map -- and printed in the
  same row. They agree at every stratum at both bounds (Z/8 dimension 3
  against 3.0 two-element orbits per field, Z/2 x Z/6 dimension 4 against
  4.0, and so on down the table), which is why no gated row can carry the
  degeneracy flag.

  **THE COMPONENT DOES NOT SURVIVE ITS OWN GATE BEING RAISED, AND THAT
  CLOSES IT** (observation, D1 at both bounds; the frozen kill K1 misses by
  its own last digit and is superseded by a mechanism its own table
  carries). Every figure here is the IMAGINARY arm, which is what probe 6
  measured and the only arm comparable across the two bounds. Pooled over
  its 22 gated strata and 1213 fields at |D| <= 8000, RES-h* is 0.1061
  against NULL-B 0.0924-0.0965: a ratio to the band's top of 1.100, against
  a frozen floor of "below about 1.1". So P1 does not survive its own
  observable so much as land exactly on it, at three and a half times the
  population that produced the 1.206. And swept over the gate the excess
  decays through it and then flattens below the band: the ratio to the
  band's MEAN -- the band's centre being the only reference comparable
  across population sizes, per the rule below -- is 1.134 at complement
  dimension >= 3, 1.094 at >= 4 over 1151 fields, 1.038 at >= 6 over 850,
  and 0.946 at >= 8 over 643, BELOW the band and on nearly twice the
  population the whole probe-6 finding stood on, then 0.955 at >= 10 over
  442. The decay is monotone to >= 8 and the last step is flat, not a
  recovery. The |D| <= 4000 arm runs 1.231, 1.140, 1.147 and 0.853 through
  its own four thresholds -- the same fall to below the band, with one
  0.007 step out of order at >= 6, where only 3 strata and 128 fields
  remain. So the pooled excess is not a property of the residual spread
  evenly over the gated strata; it is concentrated at the strata nearest
  the gate and drains steadily as they leave, and no single stratum
  carries it -- dropping complement dimension 3, which is Z/8 alone and 62
  of 1213 fields, takes 1.134 to 1.094; dropping dimensions 4 and 5, four
  strata and 301 fields, takes it to 1.038; dropping 6 and 7, three strata
  and 207 fields, takes it below the band to 0.946. A component would not
  thin in step with the number of degrees of freedom its own control was
  fitted against.

  WHY THAT IS A CLOSE AND NOT A NARROWING. Probe 5 set the gate at
  complement dimension >= 3 as the dimension at which a one-parameter
  held-out fit stops ANNIHILATING its complement -- the pathology visible
  at dimension 1, where RES-h* prints 1.7190 and 2.9474, more order-2
  energy after the subtraction than the whole spectrum held before it. It
  was never the dimension at which that fit stops DISTORTING its
  complement, and nothing in the corpus ever argued that it was. The
  printed column is continuous straight through the gate -- RES-h* runs 1.7
  to 4.3 at dimension 1, 0.20 to 0.74 at dimension 2, 0.17 to 0.37 at
  dimension 3, and down from there -- so the excess at the gate is the tail
  of the same one-parameter distortion, thinning as the complement it is
  fitted against grows. The honest reading of these seven probes together
  is therefore that the surviving quadratic component is NOT established:
  the statistic that reports it is graded by exactly the parameter that
  measures how much its own control distorts the reading.

  WHAT WOULD HAVE TO BE TRUE FOR THE OTHER READING, stated because it is
  not excluded. The complement dimension is (h - 1 - n2)/2, so it is
  essentially half the class number, and "the excess falls as the fit's
  complement grows" and "the excess falls as the class number grows" are
  the SAME column here. An arithmetic effect genuinely concentrated at
  small class number would print identically. The two are not separable by
  this rig or by any rig that fits one amplitude per field, because the
  confound is between the statistic's parameter count and the group's size,
  and both are set by h. What decides it on the evidence available is the
  continuity above: a real arithmetic grading would not have to run
  smoothly out of the cells where the fit is agreed to be pathological,
  and this one does.

  **THE REAL SIDE BECOMES READABLE AT TWICE THE BOUND, AND THE STRATUM
  THAT CLEARS ITS BAND IS THE MOST DISTORTED CELL ADMITTED** (observation;
  K2 FIRES at 2 against a frozen 0, P2 is DEAD). At |D| <= 8000 the real
  side yields 2005 decomposed fields and five strata above the floor, two
  of them at complement dimension >= 3: cyclic Z/8, 30 fields, RES-h*
  0.3653 against NULL-B 0.0853-0.0861, a ratio of 4.241; and Z/2 x Z/6, 40
  fields, 0.2847 against 0.2640-0.3281, a ratio of 0.868. So a two-sign
  statement is available for the first time in this line of work and it
  does not survive contact with the finding above: the real stratum that
  clears its band sits at complement dimension 3, the lowest the gate
  admits, beside
  the imaginary Z/8 at the same dimension and a ratio of 1.786 -- the two
  largest excesses in the table are the two cells with the smallest
  complement. The widening bought the missing arm and the arm confirms the
  artifact rather than the component. Z/2 x Z/6 is the only real cell above
  the gate that is not at its floor, and it sits inside its band. Pooled,
  the real arm reads 0.3193 against NULL-B 0.1878-0.2244 over its 70
  fields, a top ratio of 1.423 -- and at complement dimension >= 4, which
  drops Z/8 alone, 0.2847 against 0.2640-0.3281, a top ratio of 0.868.
  One stratum is the whole of the real side's excess and it is the cell
  the gate barely admits.

  **AND A FIXED-OFFSET BAND NARROWS WITH THE POPULATION, SO A RATIO TO ITS
  TOP IS NOT COMPARABLE ACROSS POPULATION SIZES** (rule, derivation (3),
  measured at two nested bounds). The band is a range over five offsets of
  a field-weighted mean, and on the imaginary arm its relative half-width
  falls from 3.57% at |D| <= 4000 to 2.21% at 8000, a factor of 0.62
  against the 0.71 that the field count alone predicts -- the rest being
  the 7 strata becoming 22, each contributing its own averaging. A ratio to
  the band's TOP therefore rises with n under a fixed effect, and the two
  arms move the other way (1.206 to 1.100) only because the effect itself
  fell further than the band narrowed. The ratio to the band's MEAN is the
  population-stable statistic and is printed beside it throughout (1.231 to
  1.134). The rule: where a null band is a range over a FIXED number of
  draws rather than a quantile, its width is a sample-size artifact and
  only its centre is a reference; a kill observable built on the band's
  edge silently changes meaning when the population does.

  **THE PATTERN IS NOT MONOTONE AND IS STILL GRADED** (observation; K3
  MISSES, P3 survives on its frozen observable and is uninformative). The
  K3 table is a sorted DISPLAY of all 24 gated strata at both signs and
  never a pooled reading, so the signs stand together there and nowhere
  else. Over it the top ratio is not monotone in class number, in
  complement dimension or in rank -- Z/24 at cdim 11 sits lowest and Z/12
  at cdim 5 sits second lowest. But the frozen observable asked for
  monotonicity and the table carries a grading: the twelve lowest ratios
  average complement dimension 10.9 and the twelve highest average 7.4.
  That is the same fact D1 measures properly, and it is the reason a
  monotonicity test was the wrong observable to freeze -- a trend over a
  noisy 24-row table is a pooled question, not a sorting question.

  WHAT THIS LEAVES THE FRONT. Nothing live. The held-out reading's
  surviving quadratic component was the last thing standing here, and at
  twice the population it is a function of the gate rather
  than of the arithmetic: at the threshold it sits on its own kill floor,
  by three dimensions above it is gone, and by five it has reversed.
  Probe 5's 1.353-to-3.184 was already correctly renamed by probe 6 as a
  comparison between two fits; probe 6's 1.206 is
  now correctly named as the amplification tail of the held-out fit read at
  the cells where that fit has least to work with. The two-sign statement
  these probes wanted arrived and pointed the same way. What survives them
  is METHOD and not content, and it is in the two rules above --
  a permutation null for a fixed-denominator statistic must preserve every
  symmetry the treatment already has (probe 6), and a fixed-draw band's
  EDGE is not a reference across population sizes (here).

RUN RECORD: wall 22.0 s, peak working set 284.5 MB and peak commit 281.2 MB
under memwatch at a 512 MB ceiling. Two bounds in one process: |D| <= 4000
gives 1216 real and 1217 imaginary fundamental discriminants kept by the
sweep, 981 and 1208 of them decomposed at h+ >= 2, 3 real and 10 imaginary
strata above the floor and 7 gated cells over 344 fields; |D| <= 8000 gives
2431 and 2430 kept, 2005 and 2421 decomposed, 5 real and 25 imaginary
readable strata -- 26 imaginary cleared the floor and derivation (5) drops
one -- with 22 imaginary gated cells over 1213 fields and 2 real ones over
70. Every pooled figure is per sign; the signs are never pooled together.
Odd split p <= 10^4, bottom bin p < 1000, MIN_SPLIT 20, 30-field stratum
floor, five fixed offsets -- all identical at both bounds. Pure Python; the cost is
probe 5's pipeline once per sign per bound plus six orbit draws per field.

WHAT IS NOT CONTROLLED, declared with the design. Every limitation of
probe 5's population is inherited whole and only its size changes: the
readable table is a minority of the fields at both signs, the strata are
iso types and nothing finer, the two signs are never pooled, the stratum
PROFILE is still fitted on the fields it is subtracted from and only the
per-field AMPLITUDE is held out, and no error bar is computed on any cell
mean. The band is still read off five fixed offsets, so it is a range over
five draws and not a quantile. The two bounds are NESTED -- the 4000
population is a subset of the 8000 one -- so the two arms are not
independent samples and no difference between them carries a significance;
the comparison is a continuity check and a measurement of the band's
narrowing, never a test.
"""

import os
import sys
import time
from collections import defaultdict

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_class_order as P2                         # noqa: E402
import explore_class_dual as P5                          # noqa: E402
from explore_class_dual import (                         # noqa: E402
    MINSTRAT, PLACEBO_SHIFTS, amplitudes, char_order, chars_of,
    energy_split, fit_profile, fit_vec, invariant_factors, label,
    symmetrize, transform,
)
from explore_class_null import offset, orbit_rotate, orbits  # noqa: E402
from explore_class_share import mean                     # noqa: E402

BOUNDS = (4000, 8000)


def read_sign(sign, plist):
    """One sign at one bound: the controls and the per-stratum reading.

    Returns (control tuple, list of stratum records). The population is
    built, read and dropped here so only one sign is resident at a time.
    """
    box = []
    fields, viol = P5.collect(sign, plist, box)
    nrows = box[0][5]
    by = defaultdict(list)
    for rec in fields:
        by[invariant_factors(rec[2])].append(rec)
    del fields

    w = [0.0] * 6                     # N1 sum, energy, |E_0|; N2 sym, Im; N4
    out = []
    no2 = []                          # derivation (5): no tested coordinate
    for inv in sorted(by, key=lambda t: (len(t), t)):
        grp = by[inv]
        h = grp[0][1]
        dims0 = grp[0][2]
        chars0 = chars_of(dims0)
        co0 = [char_order(j, dims0) for j in chars0]
        n2 = sum(1 for o in co0 if o == 2)
        readable = len(set(co0[1:])) >= 2 and len(grp) >= MINSTRAT
        if readable and n2 == 0:              # derivation (5)
            no2.append((label(inv), len(grp)))
            readable = False
        prof = fit_profile(grp)
        resas = reshs = 0.0
        nb = defaultdict(float)
        draws = []
        npair = nsing = 0
        for D, hh, dims, dev, inv_ix, M, cords, reach in grp:
            fit = fit_vec(prof, dims)
            ds = symmetrize(dev, inv_ix)
            Es = transform(M, ds)
            Ef = transform(M, fit)
            tot = energy_split(Es, cords, reach)[0]
            al, alh = amplitudes(Es, Ef, cords)
            av = [x - al * y for x, y in zip(ds, fit)]
            resas += (energy_split(transform(M, av), cords, reach)[1] / tot
                      if tot > 0 else 0.0)
            rv = [x - alh * y for x, y in zip(ds, fit)]
            Erv = transform(M, rv)
            t_en, t_q = energy_split(Erv, cords, reach)[:2]
            treat = t_q / tot if tot > 0 else 0.0
            reshs += treat
            base = sum(rv)
            pairs, singles = orbits(inv_ix)
            npair += len(pairs)
            nsing += len(singles)
            fams = (pairs, singles)
            seen = set()
            for sh in list(PLACEBO_SHIFTS) + ["id"]:
                offs = ((0, 0) if sh == "id" else
                        (offset(len(pairs), D, sh),
                         offset(len(singles), D, sh)))
                v = orbit_rotate(rv, fams, offs)
                Ev = transform(M, v)
                tt, qq = energy_split(Ev, cords, reach)[:2]
                share = qq / tot if tot > 0 else 0.0
                if sh == "id":
                    w[5] = max(w[5], abs(share - treat))
                    continue
                nb[sh] += share
                seen.add(tuple(round(x, 12) for x in v))
                w[0] = max(w[0], abs(sum(v) - base))
                if t_en > 0:
                    w[1] = max(w[1], abs(tt - t_en) / t_en)
                w[2] = max(w[2], abs(Ev[0]))
                w[3] = max(w[3], max(abs(v[a] - v[inv_ix[a]])
                                     for a in range(h)))
                w[4] = max(w[4], max(abs(x.imag) for x in Ev))
            draws.append(len(seen))
        if not readable:
            continue
        n = len(grp)
        cdim = len({frozenset((jx, chars0.index(
            tuple((-v) % d for v, d in zip(chars0[jx], dims0)))))
            for jx in range(1, h) if co0[jx] != 2})
        out.append({
            "inv": inv, "label": label(inv), "n": n, "h": h, "cdim": cdim,
            "rank": len(inv), "resa": resas / n, "resh": reshs / n,
            "band": [nb[sh] / n for sh in PLACEBO_SHIFTS],
            "sum_h": reshs, "sum_b": {sh: nb[sh] for sh in PLACEBO_SHIFTS},
            "draws": mean(draws), "npair": npair / n, "nsing": nsing / n,
        })
    return (nrows, sum(len(v) for v in by.values()), box[0], viol, w,
            no2), out


def run_bound(bound, plist):
    """The whole reading at one discriminant bound. Returns the pooled line."""
    P2.DBOUND = bound
    print("\n" + "=" * 70)
    print("|D| <= %d -- odd split p <= %d, bottom bin p < %d, min split %d,"
          " iso-type strata needing %d fields"
          % (bound, P2.PCAP, P2.BIN0, P2.MIN_SPLIT, MINSTRAT))
    print("=" * 70)

    pooled = {}
    gated_real = 0
    for sign, name in ((+1, "real"), (-1, "imag")):
        (nrows, nkept, bx, viol, w, no2), strata = read_sign(sign, plist)
        bad, idb, c2b, c4b, lawb, _ = bx
        print("\n%s: %d fields kept by the sweep, %d decomposed at h+ >= 2"
              % (name, nrows, nkept))
        print("  N5 composition (probe 2's): disc/integrality %d | key not in"
              " inventory %d | walk overran %d | order does not divide h+ %d"
              " | identity %d | non-commuting %d | non-associative %d |"
              " order<=2 vs form-symmetry %d"
              % (bad[0], bad[1], bad[2], bad[3], idb, lawb[0], lawb[1], c2b))
        print("  N5 decomposition (probe 5's): span %d | bijection %d |"
              " trivial off zero %d | order vs coordinates %d |"
              " reachability vs direct evaluation %d" % tuple(viol))
        print("  N1 sum %.2e | total energy rel %.2e | |E_0| %.2e ||  N2"
              " symmetry %.2e | max |Im E| %.2e ||  N4 identity draw %.2e"
              % tuple(w))
        print("  derivation (5): %d iso type(s) above the floor dropped for"
              " carrying NO character of order 2, so no tested coordinate%s"
              % (len(no2),
                 " -- " + ", ".join("%s (%d fields)" % x for x in no2)
                 if no2 else ""))
        for s in strata:
            top = max(s["band"])
            s["top"] = top
            s["ratio"] = s["resh"] / top if top > 0 else 0.0
            deg = s["draws"] <= 1.0 and s["npair"] <= 1.0 and s["nsing"] <= 1.0
            s["deg"] = deg
            print("    %-14s (%4d fields, h %d, complement real dim %d, %s):"
                  % (s["label"], s["n"], s["h"], s["cdim"],
                     "cyclic" if s["rank"] == 1 else "rank %d" % s["rank"]))
            print("      RES-a* %.4f  RES-h* %.4f  ||  NULL-B %.4f-%.4f  ->"
                  "  RES-h*/top %.3f"
                  % (s["resa"], s["resh"], min(s["band"]), top, s["ratio"]))
            print("      N3: %.2f distinct draws per field, %.1f two-element"
                  " and %.1f one-element orbits per field%s"
                  % (s["draws"], s["npair"], s["nsing"],
                     "  <-- NULL DEGENERATE" if deg else ""))
        gated = [s for s in strata if s["cdim"] >= 3]
        print("    %d strata printed, %d of them at complement dim >= 3"
              % (len(strata), len(gated)))
        if sign > 0:
            gated_real = len(gated)
        pooled[name] = gated

    print("\n  K2: %d REAL strata at complement dim >= 3 (P2 predicts 0)"
          % gated_real)

    rows = pooled["imag"] + pooled["real"]
    print("\n  K3: the gated strata sorted by RES-h*/top, with the three"
          " columns P3 says do not order them (r = real):")
    for x in sorted(rows, key=lambda r: r["ratio"]):
        print("      %-14s%s ratio %.3f   h %2d   cdim %d   rank %d   (%d"
              " fields)" % (x["label"], " r" if x in pooled["real"] else "  ",
                            x["ratio"], x["h"], x["cdim"], x["rank"], x["n"]))

    # D1, frozen after K3 was read and before this block was written, as a
    # DIAGNOSTIC and never a kill. K3's table shows the excess falling as
    # the complement dimension rises, and the gate at >= 3 was set by probe
    # 5 as the point where a one-parameter held-out fit stops annihilating
    # its complement -- not as the point where it stops distorting it. If
    # the component is the tail of that same distortion, the pooled ratio
    # falls toward 1 as the gate is raised; if it is a property of the
    # residual, the ratio holds while only the field count drops.
    #
    # POOLED PER SIGN AND NEVER ACROSS THEM (corrected at audit). The corpus
    # has kept the two signs apart since probe 2, and probe 6's figure is
    # IMAGINARY-only -- so pooling them here would both break that rule and
    # make the two bounds incomparable, the real side being empty at 4000
    # and not at 8000: a combined column would carry the sign's ARRIVAL as
    # if it were a change in the component. The imaginary arm is the one
    # comparable across bounds; the real arm is printed beside it.
    def pool(sel):
        if not sel:
            return None
        gn = sum(x["n"] for x in sel)
        gb = [sum(x["sum_b"][sh] for x in sel) / gn for sh in PLACEBO_SHIFTS]
        gt = sum(x["sum_h"] for x in sel) / gn
        bm = mean(gb)
        return {"n": gn, "k": len(sel), "t": gt, "lo": min(gb), "hi": max(gb),
                "mean": bm,
                "relhalf": ((max(gb) - min(gb)) / 2.0 / bm) if bm > 0 else 0.0}

    print("\n  D1 (diagnostic, frozen after K3 and before it was read): the"
          " pooled\n      reading as a function of the GATE, to separate a"
          " component from the\n      held-out fit's amplification tail."
          " Per SIGN, never across them.")
    for nm in ("imag", "real"):
        print("      %s:" % nm)
        for g in (3, 4, 6, 8, 10):
            r = pool([x for x in pooled[nm] if x["cdim"] >= g])
            if r is None:
                continue
            print("        cdim >= %-2d : %2d strata, %4d fields, RES-h*"
                  " %.4f against NULL-B %.4f-%.4f -> top %.3f, mean %.3f"
                  % (g, r["k"], r["n"], r["t"], r["lo"], r["hi"],
                     r["t"] / r["hi"] if r["hi"] > 0 else 0.0,
                     r["t"] / r["mean"] if r["mean"] > 0 else 0.0))

    out = {"bound": P2.DBOUND, "gated_real": gated_real}
    for nm in ("imag", "real"):
        r = pool(pooled[nm])
        out[nm] = r
        if r is None:
            continue
        print("\n  K1 POOLED over the %d %s fields at complement dim >= 3:"
              " RES-h*\n      %.4f against NULL-B %.4f-%.4f -- ratio to the"
              " band's TOP %.3f,\n      ratio to the band's MEAN %.3f, band"
              " relative half-width %.2f%%"
              % (r["n"], nm, r["t"], r["lo"], r["hi"],
                 r["t"] / r["hi"] if r["hi"] > 0 else 0.0,
                 r["t"] / r["mean"] if r["mean"] > 0 else 0.0,
                 100.0 * r["relhalf"]))
    return out


def main():
    t0 = time.time()
    plist = P5.primes_upto(P2.PCAP)
    print("PROBE 7: probe 6's held-out reading and its orbit null, run at two"
          "\n  discriminant bounds in ONE process. Derivation (1): the bound"
          "\n  is a module global read by the sweep at call time and is the"
          "\n  only thing that changes between the two arms. Derivation (3):"
          "\n  the pooled band is a range over five field-weighted means and"
          "\n  narrows like n^(-1/2), so the ratio to its TOP rises with the"
          "\n  population on its own -- the ratio to its MEAN is printed"
          "\n  beside it and the relative half-width beside both.")

    res = [run_bound(b, plist) for b in BOUNDS]

    print("\n" + "=" * 70)
    print("THE COMPARISON -- the same code path at two nested populations."
          "\n  N6: the %d arm must reproduce explore_class_null.py's printed"
          "\n  figures. The two arms are NESTED, so no difference here is a"
          "\n  significance; the columns say whether the component moved and"
          "\n  how much of any move in the TOP ratio is the band narrowing."
          % BOUNDS[0])
    print("=" * 70)
    print("  the IMAGINARY arm, which is the one probe 6 measured and the"
          " only one\n  comparable across the two bounds -- the real side is"
          " empty at the first:")
    print("  %-8s %7s %7s %9s %9s %9s %8s %7s %6s"
          % ("bound", "fields", "strata", "RES-h*", "band lo", "band hi",
             "ratio", "toMEAN", "half%"))
    for r in res:
        q = r and r["imag"]
        if not q:
            continue
        print("  %-8d %7d %7d %9.4f %9.4f %9.4f %8.3f %7.3f %6.2f"
              % (r["bound"], q["n"], q["k"], q["t"], q["lo"], q["hi"],
                 q["t"] / q["hi"], q["t"] / q["mean"], 100 * q["relhalf"]))
    if len(res) == 2 and res[0] and res[1] and res[0]["imag"] \
            and res[1]["imag"]:
        a, b = res[0]["imag"], res[1]["imag"]
        print("  band relative half-width %.2f%% -> %.2f%% (a factor of"
              " %.2f; derivation (3) predicts about 1/sqrt(2) = 0.71 from"
              " the\n    population alone), and the TOP ratio %.3f -> %.3f"
              % (100 * a["relhalf"], 100 * b["relhalf"],
                 b["relhalf"] / a["relhalf"] if a["relhalf"] else 0.0,
                 a["t"] / a["hi"], b["t"] / b["hi"]))
        print("  the population-stable MEAN ratio %.3f -> %.3f, which is the"
              " reading of whether the component itself moved."
              % (a["t"] / a["mean"], b["t"] / b["mean"]))
    print("  and the REAL arm, which has no gated cell at all until the"
          " second bound:")
    for r in res:
        q = r and r["real"]
        print("  %-8d %s" % (r["bound"], "no gated stratum" if not q else
              "%d fields, %d strata, RES-h* %.4f against NULL-B %.4f-%.4f,"
              " top %.3f, mean %.3f"
              % (q["n"], q["k"], q["t"], q["lo"], q["hi"], q["t"] / q["hi"],
                 q["t"] / q["mean"])))

    print("\nwall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
