"""HOW BIG IS THE SURVIVING QUADRATIC COMPONENT WHEN THE HELD-OUT READING
IS GIVEN A NULL? -- the fixed-denominator order-2 energy left by an
amplitude fitted off the tested coordinate, against a rotation of the
residual that changes which class carries which value and nothing else.

THE QUESTION, AND WHY IT IS THE ONE LEFT. Probe 5
(explore_class_dual.py) found that probe 4's per-field amplitude control
was fitted on the same coordinate it was protecting, and that re-fitting
with that coordinate HELD OUT leaves 1.353 to 3.184 times the order-2
energy the same-data fit leaves, measured against a fixed pre-residual
total, at the seven strata whose held-out complement carries three or more
real degrees of freedom. So the surviving component is larger than the
corpus says by a factor. What probe 5 could NOT say is how much of that is
signal, because the held-out reading has no null: RES-h* and RES-a* were
printed against each other and against nothing else. The share-form
columns had the rotation band beside them; the starred columns had
nothing. This probe supplies the missing band and asks one question of it:
does the held-out residual carry MORE order-2 energy than a residual whose
values have been shuffled across the classes?

WHOSE VOCABULARY THE SUSPICION IS WRITTEN IN. The dual's, unchanged from
probes 4 and 5, and the object under test is a RESIDUAL and not a
deviation -- which is the whole of why the null had to be rebuilt rather
than inherited. THE TRANSPLANT, flagged: probe 5's placebo is a null for
the SHARE, a scale-free statistic, and carrying it to a statistic with a
fixed denominator is exactly the move derivation (2) below shows is
invalid. The inherited instrument is the thing being replaced, not the
thing being reused.

THE HAND-DERIVATION (pre-engine, on paper, one line per VARIABLE).

  (1) WHERE THE PERMUTATION BELONGS. The hypothesis under test is that
      the residual after the held-out subtraction is exchangeable across
      the non-trivial classes -- that no class order and no reachability
      condition predicts which class carries a large value. So the
      permutation belongs at the RESIDUAL, the last step whose
      exchangeability is the hypothesis, and nowhere earlier. A null built
      by permuting the DEVIATION and then subtracting alpha*fit differs
      from the treatment in everything downstream: the rotation destroys
      the alignment between data and fit, so the same subtraction cancels
      the ladder in the treatment and INJECTS it in the null. Probe 5
      wrote that rig, printed a null of 0.27 where exchangeability says 1,
      and threw it away. That is variable one and it is settled by
      placement.

  (2) THE LITERAL FORM CARRIES A SECOND VARIABLE, AND A FIXED DENOMINATOR
      IS WHAT EXPOSES IT. The treatment's residual is already symmetric:
      ds is the symmetrized deviation and fit is a class function of the
      ORDER, which is inversion-invariant, so rv = ds - alpha*fit satisfies
      rv(C) = rv(C^-1) and re-symmetrizing it is the IDENTITY. A cyclic
      rotation across the non-trivial classes does not respect inversion,
      so the rotated vector is not symmetric and re-symmetrizing it is a
      PROJECTION -- it strictly loses energy the treatment never loses.
      Under a share this cancels, numerator and denominator shrinking
      together, which is why probe 5's placebo was sound where it stood.
      Under the FIXED pre-residual denominator this reading needs, it does
      not cancel: the null is deflated by the projection alone and would
      sit below the treatment even under perfect exchangeability. So the
      literal instruction is anti-conservative, and by an amount that is
      itself measurable.

  (3) THE PERMUTATION THAT CHANGES ONE VARIABLE. Let the non-trivial
      classes be partitioned into INVERSE ORBITS: two-element orbits
      {C, C^-1} with C not self-inverse, and one-element orbits, the
      classes of order dividing 2 other than the trivial one. A symmetric
      vector is constant on each orbit, so it IS a function on the orbit
      set. Permute values among the two-element orbits and, separately,
      among the one-element orbits. Then: symmetry is preserved exactly,
      so no projection and no loss; the constant sum is preserved, being
      sum over orbits of (orbit size times value) and the permutation
      acting within fixed-size families; the total energy is preserved for
      the same reason; and the trivial class is untouched. The ONLY thing
      that changes is which class carries which value, which is the
      hypothesis. This is the same reasoning probe 5 used to REJECT
      rotating over pairs -- that it moves a two-class value onto a
      one-class slot and breaks the constant sum -- taken one step
      further: the fix is not to rotate over classes but to rotate within
      orbit SIZE.

  (4) WHAT THE NULL IS A NULL FOR, stated so it is not over-read, and
      CORRECTED AT AUDIT. It is a null for "the residual's values are
      unstructured across classes of the same inversion type" and never
      for "the residual is the fit". The freeze said more than that: it
      said the expected order-2 energy under the null is the residual's
      total energy times the order-2 characters' share of the dual's
      dimension, so that the band's LEVEL would be readable as a
      dimensional allowance. THAT IS FALSE and the rig now prints why. A
      permutation group acting transitively on the non-trivial classes
      would give the flat level; this one does NOT act transitively on
      the dual, because it may not move a self-inverse class onto a class
      of an inverse pair. So whatever the residual carries differently on
      the 2-torsion classes than on the rest SURVIVES every draw, and the
      order-2 characters read it on either side. Measured, the band sits
      at 1.28 to 3.10 times the flat prediction at the thirteen readable
      strata. THAT MECHANISM IS THE WRONG ONE and a second audit pass
      refuted it with the rig's own columns: read as a share of its own
      arm's total, the orbit null sits BELOW the free-rotation null --
      which destroys the orbit structure entirely -- at five of the seven
      readable strata. Preserving the structure lowers the order-2 share
      rather than raising it, so non-transitivity is not what puts either
      null above flat.

      WHAT PUTS THEM THERE IS SYMMETRIZATION, and it is an identity. For
      real v, E_j(sym v) = (E_j(v) + conj(E_j(v)))/2 = Re E_j(v), because
      the inverse class carries the conjugate character value. A REAL
      character therefore keeps its energy WHOLE, and the real characters
      are exactly those of order dividing 2 -- exactly the tested set --
      while every complex character loses Im(E_j)^2, half of it under
      random phase. So the allowance for a share taken AFTER symmetrizing
      is 2*n2/(h-1+n2) and not n2/(h-1); here that is 1.40 to 1.86 times
      flat, and both nulls sit at 0.85 to 1.19 times it at every stratum
      whose null is not degenerate. The flat allowance is simply the
      wrong reference for a symmetrized spectrum, and it is the reference
      probes 4 and 5 read their quadratic concentration against.

      The consequence for THIS rig is unchanged and is why the design
      survives its own derivation being wrong twice: treatment and null
      are both symmetrized and both divide by the same fixed total, so
      the comparison between them never touches this. Only the band's
      POSITION against the treatment is readable, never its level, and a
      level was never what the reading needed.

  (5) THE DENOMINATOR IS THE PRE-RESIDUAL TOTAL AND IS IDENTICAL IN BOTH
      ARMS. Probe 5 added the starred columns for this reason: a share
      divides by the residual's own total, which the held-out fit shrinks
      by construction, so RES-h and RES-a are not on one scale. Every
      reading here divides the order-2 energy by the energy of the
      symmetrized deviation's transform over j != 0, which is computed
      before any subtraction and is the same number in the treatment and
      in every draw of both nulls.

  (6) THE COMPLEMENT DIMENSION GATES THE READING AND IS PRINTED BESIDE
      EVERY ROW. The held-out amplitude is ONE parameter fitted against
      the real dimension of the complement -- conjugate character pairs
      carrying one real degree of freedom between them. At dimension 1 the
      fit annihilates the complement and amplifies the tested coordinate
      (probe 5: RES-h exactly 1.0000 at both Z/4 strata, RES-h* 4.2835 and
      1.7190, above 1); at dimension 2 the factor is larger than anywhere
      above it, the same instability one step milder. So the reading is
      restricted to complement real dimension >= 3, which is seven strata
      and every one IMAGINARY -- the real side has no readable cell and no
      two-sign statement is available without widening the population.
      Every stratum is still printed, with its dimension, so the void
      cells are read rather than hidden.

  (7) THE POPULATION IS PROBE 5'S, UNCHANGED AND IMPORTED. Same sweep,
      same discriminant bound, same prime cap, same bottom bin, same
      MIN_SPLIT, same iso-type strata and same 30-field floor, so probe
      5's decomposition and composition controls govern this rig too and
      are re-printed rather than re-derived. Nothing here re-measures the
      arithmetic; the treatment column must reproduce probe 5's RES-h* to
      the printed digits, and that is a control and not a finding.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. THE HELD-OUT RESIDUAL IS ORDER-2 HEAVY AGAINST ITS OWN NULL. At the
      strata of complement real dimension >= 3, the treatment RES-h*
      exceeds the WHOLE orbit-null band at four or more of the seven. The
      reason: probe 4 and probe 5 both measured the order-2 concentration
      in the deviation, probe 5 showed the held-out fit removes less of it
      than the same-data fit did, and the concentration is what is left to
      be band-tested.

  P2. THE LITERAL FORM IS ANTI-CONSERVATIVE, AND MEASURABLY. The
      rotate-then-resymmetrize null retains less total residual energy
      than the treatment at every stratum: the printed mean ratio of the
      re-symmetrized rotated residual's total energy to the treatment
      residual's total energy is below 1 everywhere. The reason is
      derivation (2): re-symmetrization is a projection off a subspace the
      rotated vector generically leaves.

  P3. THE VOID CELLS DECLARE THEMSELVES AGAINST THE NULL TOO. At
      complement dimension 1 and 2 the treatment's excess over the null
      band's top is LARGER than at any stratum of dimension >= 3 -- the
      one-parameter fit's amplification reading as apparent signal. The
      reason: probe 5 found RES-h* above 1 at both dimension-1 strata,
      which is more energy at order 2 after the subtraction than the whole
      spectrum held before it, and a null cannot follow a fit there.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS. Each is arithmetic on a
printed number, and the meaning is weighed after the controls are read.

  K1 kills P1: the printed count of complement-dimension >= 3 strata whose
     treatment RES-h* exceeds the maximum of the orbit-null band. Three or
     fewer is the kill. A treatment INSIDE the band at most or all of them
     is the informative opposite: the surviving component would then be no
     larger than its dimensional allowance of what the held-out fit left,
     and the factor probe 5 measured would be a statement about the two
     fits and not about a component.

  K2 kills P2: the printed per-stratum mean of (total energy of the
     re-symmetrized rotated residual)/(total energy of the treatment
     residual). At or above 1 at any stratum is the kill.

  K3 kills P3: the printed excess ratio RES-h*/(top of the orbit-null
     band) at every stratum. If the maximum over the dimension-1 and
     dimension-2 strata does not exceed the maximum over the dimension >=
     3 strata, P3 is dead.

THE POSITIVE CONTROLS, run and read FIRST.

  N1. THE ORBIT ROTATION PRESERVES WHAT DERIVATION (3) SAYS IT DOES. Over
      every kept field and every draw: max |sum of the rotated residual
      over all classes - sum of the treatment residual|, max relative
      deviation of the rotated residual's total energy from the
      treatment's, and max |E_0| of the rotated residual's transform.
      Above 1e-9 voids every orbit-null reading below.

  N2. THE ORBIT ROTATION PRESERVES SYMMETRY EXACTLY. Max over fields and
      draws of |v(C) - v(C^-1)| on the rotated residual, and max |Im E_j|
      of its transform. Above 1e-9 means the orbit partition is wrong and
      the null is the literal form under another name.

  N3. THE ROTATION IS NOT THE IDENTITY, AND WHERE IT IS THE ROW SAYS SO.
      Printed per stratum: the mean number of DISTINCT draws per field,
      and the mean orbit counts -- how many two-element and how many
      one-element orbits the rotation has to work with. A family of size
      one admits no non-identity rotation, so a stratum whose one-element
      family is a singleton is rotating only its pairs and the row must
      show it.

  N4. THE IDENTITY DRAW REPRODUCES THE TREATMENT. Rotating by a zero
      offset in both families must return the treatment statistic
      exactly: max |RES-h*(identity draw) - RES-h*| over every kept field,
      printed. Above 1e-12 means the null pipeline and the treatment
      pipeline are not the same pipeline and no comparison between them is
      readable.

  N5. THE TREATMENT REPRODUCES PROBE 5. RES-a*, RES-h* and their ratio are
      printed per stratum and must agree with explore_class_dual.py's
      printed figures; the composition and decomposition controls are
      re-printed through the imported sweep as violation counts.

THE FINDINGS.

  THE CONTROLS. N5 re-prints probe 2's eight composition counts and probe
  5's five decomposition and reachability counts at zero over 1216 real and
  1217 imaginary fields, 981 and 1208 of them decomposed at h+ >= 2 -- the
  imported object is the one probes 2 through 5 measured. The orbit
  rotation's own identities hold at float noise or exactly: N1 prints the
  constant sum preserved EXACTLY at both signs (0.00e+00), the residual's
  total energy preserved to 7.0e-16 real and 1.2e-15 imaginary relative,
  and |E_0| of the rotated residual at 1.1e-15 and 7.3e-15; N2 prints the
  symmetry |v(C) - v(C^-1)| preserved EXACTLY (0.00e+00) at both signs
  with the transform's largest imaginary part at 5.6e-16 and 3.9e-15; and
  N4 prints the identity draw reproducing the treatment EXACTLY. The two
  exact zeros are the derivation and not luck: rotating within orbit size
  moves floats between slots without arithmetic on them, so the sum is a
  reordering and the symmetry is structural. N5's treatment columns
  reproduce probe 5's starred figures to the printed digits at all seven
  readable strata, the factor RES-h*/RES-a* running 1.353 to 3.183 against
  that probe's 1.353 to 3.184.

  **THE SURVIVING COMPONENT CLEARS ITS OWN NULL, AND BY A FIFTH RATHER
  THAN BY THE FACTOR THE TWO-FIT COMPARISON SUGGESTED** (observation; P1
  SURVIVES at exactly its frozen threshold, K1 missing at 4 of the 7
  strata of complement real dimension >= 3). Pooled field-weighted over
  the 344 fields at those strata, RES-h* is 0.1640 against an orbit-null
  band of 0.1265 to 0.1361 -- a ratio to the band's top of 1.206. Per
  stratum the excess is uneven and mostly small: imaginary Z/8 at 1.802 is
  the only one above 1.4, then Z/2 x Z/8 1.328, Z/10 1.149 and Z/2 x Z/6
  1.069. The other three do NOT clear, and the three ratios do not say how:
  a ratio to the band's TOP below 1 places the treatment under that top and
  not under the band, so Z/14 at 0.996 and Z/2 x Z/10 at 0.743 sit INSIDE
  their bands (0.0895 in 0.0743-0.0898 and 0.1278 in 0.1262-0.1719) and
  only Z/12 at 0.495 sits below the whole of its own (0.0555 against
  0.0698-0.1121). So the component is real as a pooled
  statement and is not a property of the strata one at a time. THE TWO
  FACTORS ARE DIFFERENT QUANTITIES AND THIS IS THE READING PROBE 5 COULD
  NOT TAKE: 1.353 to 3.184 is the held-out fit against ANOTHER FIT, and
  1.206 is the held-out fit against EXCHANGEABILITY. The first says probe
  4's control was absorbing; only the second says anything survives, and
  what it says is a fifth above the null.

  **AND THE FLAT ALLOWANCE IS THE WRONG REFERENCE FOR A SYMMETRIZED
  SPECTRUM, WHICH DEFLATES THE CONCENTRATION THE LAST TWO PROBES READ
  AGAINST IT** (rule, derivation (4) as corrected; the identity plus the
  rig's own share columns). Symmetrizing sends E_j to Re(E_j), so a REAL
  character keeps its energy whole while a complex one loses Im(E_j)^2 --
  and the real characters are exactly those of order dividing 2, the tested
  set. The allowance for a share taken after symmetrizing is therefore
  2*n2/(h-1+n2), which is 1.40 to 1.86 times flat over these strata, and
  both nulls land at 0.85 to 1.19 times it wherever the null is not
  degenerate. Probe 4 reported the quadratic share at 1.48 to 2.58 times
  FLAT; the symmetrization factor alone accounts for 1.50 to 1.83 of that
  range at the class numbers in question, so most of the reported
  concentration is the geometry of an even function read in a basis with
  complex characters in it. What SURVIVES untouched is every comparison
  where both arms are symmetrized -- probe 4 beating its own rotation band
  at all eight strata, and this probe's 1.206 -- which is why the finding
  above stands while the framing beneath it does not.

  **AND THE SAME-DATA AMPLITUDE PUSHED THE TESTED COORDINATE BELOW ITS OWN
  NULL, WHICH IS THE ABSORPTION READ DIRECTLY RATHER THAN INFERRED**
  (observation, the same table's RES-a* column against the same NULL-B
  band). Probe 4's fit leaves less order-2 energy than SHUFFLING the
  residual leaves, at six of the seven readable strata -- 0.0629 against
  0.0994 at Z/8, 0.0534 against 0.0751 at Z/10, 0.0235 against 0.0698 at
  Z/12, 0.0481 against 0.0743 at Z/14, 0.1433 against 0.2073 at Z/2 x Z/6
  and 0.0886 against 0.1262 at Z/2 x Z/10 -- and at the seventh, Z/2 x Z/8,
  it sits INSIDE the band at 0.1704 against 0.1516 to 0.1735 rather than
  above it. A control that removes MORE than exchangeability leaves is
  over-subtracting at the coordinate it protects, which is probe 5's OWN
  derivation (4) -- the hold-out's reason for existing, inherited here and
  not restated above -- measured against a null instead of against a rival
  fit. This is
  the sharpest form of probe 5's verdict and it needed the band to be
  sayable at all.

  **THE LITERAL INSTRUCTION WOULD HAVE BUILT AN ANTI-CONSERVATIVE NULL,
  AND THE PROJECTION IT LOSES IS ABOUT HALF THE RESIDUAL** (rule,
  derivation (2), measured; P2 SURVIVES, K2 misses everywhere). The
  rotate-then-re-symmetrize form keeps only 0.4500 to 0.7151 of the
  treatment residual's total energy -- every stratum below 1, the cyclic
  ones at 0.45 to 0.50 and the rank-2 ones at 0.55 to 0.72 --
  because the treatment's residual is already symmetric and the rotated
  one is not, so re-symmetrizing is a projection in the null arm and the
  identity in the treatment arm. Its NULL-R band accordingly sits below
  NULL-B at twelve of the thirteen strata and at the two Z/4 strata prints
  0.0000 outright; the exception is Z/2 x Z/8, where NULL-R 0.1632-0.1827
  overlaps and tops NULL-B 0.1516-0.1735 -- the projection's loss and the
  free rotation's own excess at order 2 running opposite ways there, which
  is why the loss is reported as its own column rather than inferred from
  where the two bands sit. Under a SHARE that loss cancels, which is why
  probe 5's placebo was sound where it stood; under the fixed denominator
  this reading needs it does not, and a rig built to the literal
  instruction would have reported the component as roughly twice the
  excess it has. The rule: a permutation null for a fixed-denominator
  statistic must preserve every symmetry the treatment's own object
  already has, and rotating within INVERSE ORBIT SIZE is the permutation
  that does.

  **AND THE VOID CELLS SHOW UP AGAINST THE NULL TOO, BUT NOT BY THE
  MECHANISM THE SLATE NAMED** (observation; P3 SURVIVES on the frozen
  observable, K3 missing at 2.945 against 1.802, and the reason it gives
  is wrong). The excess ratio over the void cells peaks at imaginary Z/6,
  complement dimension 2, at 2.945 -- above every dimension >= 3 stratum,
  as predicted. But the two dimension-1 cells contributed NOTHING to that
  maximum, and could not have: N3's degeneracy flag prints at both of
  them, because a group whose non-trivial classes form one inverse pair
  and one self-inverse class has no non-identity rotation within either
  family, so the null IS the treatment and the ratio is 1.000 by
  construction. The frozen prediction reasoned from probe 5's RES-h* above
  1 at exactly those cells and the null cannot see that at all. So P3's
  observable passes on the dimension-2 cells alone, and what the
  dimension-1 cells actually earn is a different verdict: they are void
  because no null exists there, which is a stronger reason than
  instability and one the slate did not anticipate.

  WHAT THIS LEAVES THE FRONT. The held-out reading now has a band and the
  answer is quantitative: the surviving quadratic component is about 1.2
  times its own null pooled over 344 imaginary fields, real as
  a pooled statement, indistinguishable from exchangeable at two of the
  seven strata taken singly and reversed at a third,
  and read at every stratum through a band off two to five distinct
  draws. Probe 5's 1.353-to-3.184 is now correctly named as a comparison
  between two fits and not as the size of anything. The real side has no
  readable cell at any complement dimension >= 3, so nothing here is a
  two-sign statement and widening the population is what would buy one. And
  the component's per-stratum pattern is not monotone in class number or in
  complement dimension, so what selects the strata it survives at is
  unmeasured and is the shape of any next question.

RUN RECORD: wall 6.1 s, peak working set 136.3 MB and peak commit 131.9 MB
under memwatch at a 512 MB ceiling. Probe 5's population imported unchanged
per derivation (7) -- 1216 real and 1217 imaginary fundamental discriminants
to |D| <= 4000 over the odd split p <= 10^4, cut to the 981 real and 1208
imaginary fields with h+ >= 2, strata the iso types carrying more than one
character order and clearing a 30-field floor. Thirteen such strata print,
three real and ten imaginary; the seven of complement real dimension >= 3
that the reading is gated to are ALL imaginary and carry 344 fields. Pure Python,
the cost being probe 5's pipeline run once per sign plus five orbit draws
and five literal draws per field.

WHAT IS NOT CONTROLLED, declared with the design rather than left for a
reader to find. Every limitation of probe 5's population is inherited
whole: the readable table is a minority of the fields at both signs, the
strata are iso types and nothing finer, the two signs are never pooled,
the stratum PROFILE is still fitted on the fields it is subtracted from
(only the per-field AMPLITUDE is held out), and no error bar is computed
on any cell mean. The gate of derivation (6) leaves seven strata and all
of them imaginary, so nothing here is a two-sign statement. The orbit null
is a null for exchangeability WITHIN inversion type and never for "the
residual is the fit", so a treatment above the band says the order-2
coordinate is favoured over the other coordinates of the same residual and
never that the fit was the right fit. And the band is read off five fixed
offsets, so it is a range over five draws per field and not a quantile of
anything; it thins toward the small strata exactly as probe 5's did.
"""

import os
import sys
import time
from collections import defaultdict

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_class_dual as P5                         # noqa: E402
from explore_class_dual import (                        # noqa: E402
    MINSTRAT, PLACEBO_SHIFTS, amplitudes, char_order, chars_of, char_table,
    energy_split, fit_profile, fit_vec, invariant_factors, label, reachable,
    symmetrize, transform,
)
from explore_class_share import mean                    # noqa: E402


def orbits(inv_ix):
    """Derivation (3): the inverse orbits of the NON-trivial classes.

    Returned as two families, the two-element orbits and the one-element
    ones, each as a list of the class indices carrying that orbit's value.
    """
    pairs, singles = [], []
    for a in range(1, len(inv_ix)):
        b = inv_ix[a]
        if b == a:
            singles.append([a])
        elif a < b:
            pairs.append([a, b])
    return pairs, singles


def offset(m, D, shift):
    """A non-identity offset within a family of m orbits, 0 if none exists."""
    return 1 + (abs(D) + shift) % (m - 1) if m > 1 else 0


def orbit_rotate(vec, fams, offs):
    """Move each family's values along by its own offset. Nothing else."""
    out = list(vec)
    for fam, off in zip(fams, offs):
        m = len(fam)
        if m == 0:
            continue
        for i, cells in enumerate(fam):
            val = vec[fam[(i + off) % m][0]]
            for c in cells:
                out[c] = val
    return out


def main():
    t0 = time.time()
    plist = P5.primes_upto(P5.P2.PCAP)
    print("population: probe 5's, imported unchanged (derivation 7) --"
          " |D| <= %d both signs, odd split p <= %d, bottom bin p < %d,"
          " min split %d, every field with h+ >= 2, strata are ISO TYPES"
          " needing %d fields"
          % (P5.P2.DBOUND, P5.P2.PCAP, P5.P2.BIN0, P5.P2.MIN_SPLIT,
             MINSTRAT))
    print("\nWHAT THIS RIG ADDS: a null for the FIXED-DENOMINATOR held-out"
          "\n  reading. The permutation sits at the RESIDUAL (derivation 1)"
          "\n  and moves values within INVERSE ORBIT SIZE (derivation 3),"
          "\n  which preserves symmetry, the constant sum and the total"
          "\n  energy exactly -- so treatment and null differ in one thing,"
          "\n  which class carries which value. The literal"
          "\n  rotate-then-resymmetrize form is printed beside it as"
          "\n  NULL-R, with the energy it loses to the projection.")

    pops, viols, boxes = {}, {}, {}
    for sign, name in ((+1, "real"), (-1, "imag")):
        box = []
        fields, viol = P5.collect(sign, plist, box)
        pops[sign], viols[sign], boxes[sign] = fields, viol, box[0]
        bad, idb, c2b, c4b, lawb, nrows = box[0]
        print("\n%s: %d fields kept by the sweep, %d decomposed at h+ >= 2"
              % (name, nrows, len(fields)))
        print("  N5 composition (probe 2's, re-printed): disc/integrality %d"
              " | key not in inventory %d | walk overran %d | order does not"
              " divide h+ %d | identity %d | non-commuting %d |"
              " non-associative %d | order<=2 vs form-symmetry %d"
              % (bad[0], bad[1], bad[2], bad[3], idb, lawb[0], lawb[1], c2b))
        print("  N5 decomposition (probe 5's): span %d | bijection %d |"
              " trivial off zero %d | order vs coordinates %d |"
              " reachability vs direct evaluation %d" % tuple(viol))

    print("\n--- N1/N2/N4: THE ORBIT ROTATION'S OWN IDENTITIES, over every"
          "\n    kept field and every draw. The sum, the total energy, the"
          "\n    trivial character and the symmetry must all survive the"
          "\n    permutation; and rotating by a zero offset must return the"
          "\n    treatment statistic itself.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        by = defaultdict(list)
        for rec in pops[sign]:
            by[invariant_factors(rec[2])].append(rec)
        w_sum = w_en = w_e0 = w_sym = w_im = w_id = 0.0
        for inv, fields in by.items():
            prof = fit_profile(fields)
            for D, h, dims, dev, inv_ix, M, cords, reach in fields:
                fit = fit_vec(prof, dims)
                ds = symmetrize(dev, inv_ix)
                Es = transform(M, ds)
                Ef = transform(M, fit)
                tot = energy_split(Es, cords, reach)[0]
                _, alh = amplitudes(Es, Ef, cords)
                rv = [x - alh * y for x, y in zip(ds, fit)]
                Erv = transform(M, rv)
                t_en = energy_split(Erv, cords, reach)[0]
                base = sum(rv)
                pairs, singles = orbits(inv_ix)
                fams = (pairs, singles)
                treat = (energy_split(Erv, cords, reach)[1] / tot
                         if tot > 0 else 0.0)
                for sh in list(PLACEBO_SHIFTS) + ["id"]:
                    if sh == "id":
                        offs = (0, 0)
                    else:
                        offs = (offset(len(pairs), D, sh),
                                offset(len(singles), D, sh))
                    v = orbit_rotate(rv, fams, offs)
                    Ev = transform(M, v)
                    tt, qq, _, _, _, _ = energy_split(Ev, cords, reach)
                    if sh == "id":
                        w_id = max(w_id, abs(
                            (qq / tot if tot > 0 else 0.0) - treat))
                        continue
                    w_sum = max(w_sum, abs(sum(v) - base))
                    if t_en > 0:
                        w_en = max(w_en, abs(tt - t_en) / t_en)
                    w_e0 = max(w_e0, abs(Ev[0]))
                    w_sym = max(w_sym, max(abs(v[a] - v[inv_ix[a]])
                                           for a in range(h)))
                    w_im = max(w_im, max(abs(x.imag) for x in Ev))
        print("  %-5s N1 sum %.2e | total energy rel %.2e | |E_0| %.2e ||"
              "  N2 symmetry %.2e | max |Im E| %.2e ||  N4 identity draw"
              " %.2e" % (name, w_sum, w_en, w_e0, w_sym, w_im, w_id))

    print("\n--- THE READING: RES-h* AGAINST ITS NULL, per ISO TYPE. RES-a*"
          "\n    and RES-h* are probe 5's starred columns (N5), both divided"
          "\n    by the PRE-residual total (derivation 5); NULL-B is the"
          "\n    orbit rotation's band over five fixed offsets and NULL-R"
          "\n    the literal rotate-then-resymmetrize form, with LOSS the"
          "\n    mean fraction of the residual's total energy that form"
          "\n    keeps (derivation 2, K2). K1 counts the strata of"
          "\n    complement real dimension >= 3 (derivation 6) whose RES-h*"
          "\n    clears the whole NULL-B band.")
    excess = {}
    pool_t = pool_n = 0.0
    pool_b = defaultdict(float)
    for sign, name in ((+1, "real"), (-1, "imag")):
        by = defaultdict(list)
        for rec in pops[sign]:
            by[invariant_factors(rec[2])].append(rec)
        print("  %s:" % name)
        k1 = 0
        for inv in sorted(by, key=lambda t: (len(t), t)):
            fields = by[inv]
            h = fields[0][1]
            dims0 = fields[0][2]
            chars0 = chars_of(dims0)
            co0 = [char_order(j, dims0) for j in chars0]
            if len(set(co0[1:])) < 2 or len(fields) < MINSTRAT:
                continue
            prof = fit_profile(fields)
            resas = reshs = rtot = 0.0
            nb = defaultdict(float)
            nr = defaultdict(float)
            loss = []
            shb, shr, sht = [], [], []
            draws = []
            npair = nsing = 0
            for D, hh, dims, dev, inv_ix, M, cords, reach in fields:
                fit = fit_vec(prof, dims)
                ds = symmetrize(dev, inv_ix)
                Es = transform(M, ds)
                Ef = transform(M, fit)
                tot = energy_split(Es, cords, reach)[0]
                al, alh = amplitudes(Es, Ef, cords)
                for a, store in ((al, "a"), (alh, "h")):
                    v = [x - a * y for x, y in zip(ds, fit)]
                    qq = energy_split(transform(M, v), cords, reach)[1]
                    if store == "a":
                        resas += qq / tot if tot > 0 else 0.0
                    else:
                        reshs += qq / tot if tot > 0 else 0.0
                rv = [x - alh * y for x, y in zip(ds, fit)]
                t_en = energy_split(transform(M, rv), cords, reach)[0]
                rtot += t_en / tot if tot > 0 else 0.0
                q_en = energy_split(transform(M, rv), cords, reach)[1]
                sht.append(q_en / t_en if t_en > 0 else 0.0)
                pairs, singles = orbits(inv_ix)
                npair += len(pairs)
                nsing += len(singles)
                fams = (pairs, singles)
                seen = set()
                for sh in PLACEBO_SHIFTS:
                    offs = (offset(len(pairs), D, sh),
                            offset(len(singles), D, sh))
                    v = orbit_rotate(rv, fams, offs)
                    seen.add(tuple(round(x, 12) for x in v))
                    tb, qb, _, _, _, _ = energy_split(
                        transform(M, v), cords, reach)
                    nb[sh] += qb / tot if tot > 0 else 0.0
                    p = P5.placebo(rv, D, sh, inv_ix)
                    tp, qp, _, _, _, _ = energy_split(
                        transform(M, p), cords, reach)
                    nr[sh] += qp / tot if tot > 0 else 0.0
                    loss.append(tp / t_en if t_en > 0 else 0.0)
                    # Added at audit. The two nulls are not on one scale
                    # under a fixed denominator, the free rotation having
                    # lost energy to the projection, so each is ALSO read
                    # as a share of its own arm's total. That is the only
                    # comparison that separates what the orbit structure
                    # contributes from what symmetrization does to a share
                    # regardless -- order-2 characters being exactly the
                    # REAL ones, whose coefficients symmetrization keeps
                    # whole while it averages every conjugate pair.
                    shb.append(qb / tb if tb > 0 else 0.0)
                    shr.append(qp / tp if tp > 0 else 0.0)
                draws.append(len(seen))
            n = len(fields)
            bandb = [nb[sh] / n for sh in PLACEBO_SHIFTS]
            bandr = [nr[sh] / n for sh in PLACEBO_SHIFTS]
            cdim = len({frozenset((jx, chars0.index(
                tuple((-v) % d for v, d in zip(chars0[jx], dims0)))))
                for jx in range(1, h) if co0[jx] != 2})
            t = reshs / n
            top = max(bandb)
            print("    %-14s (%4d fields, complement real dim %d, %s):"
                  % (label(inv), n, cdim,
                     "cyclic" if len(inv) == 1 else "rank %d" % len(inv)))
            print("      RES-a* %.4f  RES-h* %.4f  (factor %.3f)"
                  % (resas / n, t, (reshs / resas) if resas > 0 else 0.0))
            print("      NULL-B %.4f-%.4f  ->  RES-h*/top %.3f ||"
                  "  NULL-R %.4f-%.4f  LOSS %.4f"
                  % (min(bandb), top, t / top if top > 0 else 0.0,
                     min(bandr), max(bandr), mean(loss)))
            # Derivation (4) as CORRECTED at audit: the flat level the
            # freeze expected the band to sit at, printed beside the band
            # it does not sit at. The permutation cannot move a
            # self-inverse class onto a paired one, so it is not
            # transitive on the dual and the null keeps whatever the
            # residual carries differently on the 2-torsion classes.
            n2 = sum(1 for o in co0 if o == 2)
            fpred = (rtot / n) * n2 / (h - 1)
            print("      the FLAT level derivation (4) expected the band at:"
                  " residual/pre-residual energy %.4f x %d/%d = %.4f, which"
                  " the band exceeds by %.2fx -- so FLAT is the wrong"
                  " reference here; read the band's POSITION, not its level"
                  % (rtot / n, n2, h - 1, fpred,
                     top / fpred if fpred > 0 else 0.0))
            # Added at audit, and it is the round's real finding. For real
            # v, symmetrizing sends E_j to Re(E_j): a REAL character --
            # order 1 or 2, which is exactly the tested set -- keeps its
            # energy whole, while every complex character loses Im(E_j)^2,
            # half of it under random phase. So a share taken AFTER
            # symmetrizing has allowance 2*n2/(h-1+n2) and not n2/(h-1),
            # and the second is the reference probes 4 and 5 used.
            symflat = 2.0 * n2 / (h - 1 + n2)
            print("      and on ONE scale, each as a SHARE of its own arm's"
                  " total: treatment %.4f, orbit null %.4f, free-rotation"
                  " null %.4f" % (mean(sht), mean(shb), mean(shr)))
            print("      against flat %.4f -- WRONG for a symmetrized"
                  " spectrum -- and against the symmetrized allowance"
                  " 2x%d/(%d+%d) = %.4f, which is %.2fx flat and which both"
                  " nulls sit at (%.2fx and %.2fx)"
                  % (n2 / (h - 1), n2, h - 1, n2, symflat,
                     symflat * (h - 1) / n2,
                     mean(shb) / symflat, mean(shr) / symflat))
            # N3, added at audit as a VERDICT rather than a count a reader
            # must convert: both orbit families of size 1 admit no
            # non-identity offset, so the "null" IS the treatment and the
            # row's band is not a band. The count alone said this and was
            # one inference away from saying it.
            deg = max(draws) == 1 and npair / n <= 1.0 and nsing / n <= 1.0
            print("      N3: %.2f distinct draws per field, %.1f two-element"
                  " orbits and %.1f one-element orbits per field%s"
                  % (mean(draws), npair / n, nsing / n,
                     "  <-- NULL DEGENERATE: no non-identity rotation exists,"
                     " the band is the treatment" if deg else ""))
            excess[(name, inv)] = (cdim, t / top if top > 0 else 0.0, deg)
            if cdim >= 3 and t > top:
                k1 += 1
            if cdim >= 3:
                pool_t += reshs
                pool_n += n
                for sh in PLACEBO_SHIFTS:
                    pool_b[sh] += nb[sh]
        print("    K1: %d strata of complement dim >= 3 with RES-h* above"
              " the whole NULL-B band" % k1)

    hi = [v for (cd, v, d) in excess.values() if cd >= 3]
    lo = [v for (cd, v, d) in excess.values() if cd < 3]
    lond = [v for (cd, v, d) in excess.values() if cd < 3 and not d]
    print("\n--- K3: the excess ratio RES-h*/(top of NULL-B), max over the"
          "\n    readable strata (complement dim >= 3) %.3f against max over"
          "\n    the void ones (dim 1 and 2) %.3f -- and over the void ones"
          "\n    whose null is not degenerate %.3f, which is the same figure"
          "\n    with the rows that have no null taken out."
          % (max(hi) if hi else float("nan"),
             max(lo) if lo else float("nan"),
             max(lond) if lond else float("nan")))

    # Added at audit: a per-stratum band read off two to five distinct
    # draws is thin, so the same treatment and the same five offsets are
    # pooled field-weighted across the seven readable strata. RES-h* is
    # already per-field normalized by that field's own pre-residual total,
    # so a field-weighted mean is on one scale across strata.
    if pool_n:
        pb = [pool_b[sh] / pool_n for sh in PLACEBO_SHIFTS]
        print("\n--- POOLED over the %d fields at complement dim >= 3, added"
              "\n    at audit because a two-draw band is thin: RES-h* %.4f"
              "\n    against NULL-B %.4f-%.4f, a ratio to the band's top of"
              "\n    %.3f" % (int(pool_n), pool_t / pool_n, min(pb), max(pb),
                              (pool_t / pool_n) / max(pb) if max(pb) > 0
                              else float("nan")))

    print("\nwall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
