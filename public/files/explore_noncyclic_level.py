r"""explore_noncyclic_level.py -- THE LEVEL WHERE NO CLASS GENERATES: the
corrected all-principal level read on the cubic fields whose class group
is NOT cyclic, the cell the generator machinery cannot pose. (Sibling of
explore_triple_cube_term.py, whose walk and population this file imports
whole; of explore_ceiling_topband.py, whose F4 surfaced the non-cyclic
groups; and of explore_cubic_zero_tilt.py, which isolated the residual
the correction pays.)

THE QUESTION. The generator ceiling is stated with a GENERATING CLASS in
it, so over a class group with none the law has no subject. The corrected
all-principal level is a different statistic and its ingredients are not
obviously cyclic: the model share is 1/h^2, and the correction is the
explicit formula's prime-power term put back per field and per prime.
Does that level, read on the non-cyclic strata alone, sit where the
cyclic strata put it -- and does the closed form that predicts it survive
being written over a group instead of over a number?

WHOSE VOCABULARY THE SUSPICION IS IN, asked before anything was frozen.
Every phrase available for this question -- "the level", "the stratum",
"the corrected level's flatness" -- was minted on CYCLIC strata indexed
by h. The object here is a class GROUP and h is a lossy name for it. So
the strata of this file are keyed by the INVARIANT FACTORS and never by
h, and the flatness of the corrected level across h is carried in as a
TRANSPLANT (T3) rather than as a law.

THE HAND-ATTACK, on paper before any engine code.

 (a) THE INDEX CONVENTION, re-derived from the engine before the freeze.
     explore_cubic_class_map.py's `k` is the AMBIENT DIMENSION -- the
     number of generator columns -- and not a modulus: echelon() walks
     `for c in range(k)` and span_order() returns None when
     `len(piv) < k`. The class group is therefore Z^k / L with L the
     full-rank lattice spanned by the pivot rows, and h = span_order is
     the product of the pivot entries. Nothing in that representation
     names the group's structure. This file writes the torsion parameter
     as m to keep it off the ambient k.

 (b) WHAT IS ALREADY GROUP-GENERAL, and what is not -- the distinction
     the whole design rests on, read off the parent's body and not its
     prose. The MEASURED correction is general: walk_field decides every
     landing by is_principal and same_class in the field's own lattice,
     so a non-cyclic field's corrected level needs no new derivation at
     all. What is cyclic is the COMPARATOR -- count_pow's own docstring
     says "Cl cyclic of order h" and its body counts m-torsion as
     gcd(m, h). The parent's hand-derivation (4) already writes those
     counts as |Cl[m]| and |Cl[3m]|, general as written, so what this
     file owes is the group's torsion counts and not a new argument.

 (c) THE TORSION COUNT, re-derived rather than inherited. For a finite
     abelian Cl with invariant factors d_1 | ... | d_r,
         |Cl[m]| = #{x : m.x = 0} = prod_i gcd(m, d_i),
     since Cl = (+)_i Z/d_i and the m-torsion of Z/d is cyclic of order
     gcd(m, d). The three counts of the parent's (4), re-derived here on
     an arbitrary Cl rather than copied:
       - split, sigma = e: (v, e)^m = e iff m.v = 0 with v in N, and
         N = {(a, b, c) : a + b + c = 0} has (a, b) free and c forced,
         so N[m] = Cl[m]^2 and the count is |Cl[m]|^2.
       - partial, sigma a transposition: (v, t)^m for even m is
         (m/2).(2a, -a, -a) with a the fixed coordinate's class, which
         is the identity iff (m/2).a = 0 -- a in Cl[m/2], the other two
         coordinates free subject to the sum, so h |Cl[m/2]| per
         transposition and 3 h |Cl[m/2]| over the three.
       - inert, sigma a 3-cycle: (v, r)^3 = (s, s, s) with s the sum of
         v's coordinates, zero on N, so every v works at every multiple
         of 3: 2 h^2.
     Each reduces to the parent's gcd form at a cyclic Cl, which is P1's
     job to print rather than this paragraph's to assert.

 (d) THE STATISTIC'S ALGEBRA, attacked where it can blow up. The level is
     (count + correction) / (corrected total x share). On a five-field
     cell the raw all-principal COUNT can be zero, and the level is then
     built entirely of correction -- a positive number over a positive
     expectation, printing as a level with no observation under it. So
     every non-cyclic row prints its raw count beside its level, and a
     row whose count is 0 is named as such in the reading. The
     denominator carries its own correction (the parent measures it at
     about 15 % of the count and never near zero), so it is not where
     the blow-up lives.

 (e) A CONFOUND NAMED BY ARGUMENT OWES A COUNT. The non-cyclic fields
     surfaced only in the WIDENED box, so they sit at larger |d| than the
     bulk of their own h stratum, and any difference this file measures
     could be a discriminant effect wearing a group's name. The count
     owed is a MATCHED control: the cyclic fields of the same h
     restricted to the |d| window the non-cyclic ones occupy, read
     through the same walk. S5 owes that row and the verdict is not
     read without it.

 (f) THE HYPOTHESIS NOBODY CHECKED. The uniform model's share 1/h^2 wants
     the Galois image to FILL N. The parent records this as forced at
     prime h, decided at h = 3 and 6, and UNCHECKED at composite h
     beyond -- which is exactly where h = 4 and h = 8 sit, and the
     non-cyclic groups with them. The image is observable rather than
     assumable: the split primes' own triples lie in the image, so the
     subgroup they generate is a lower bound on it, and a field whose
     mapped triples generate all of N has the hypothesis confirmed at
     that field. S7 runs that on every composite-h field.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 THE POPULATION, THE CLASS READING AND THE WALK ARE IMPORTED, not
    re-implemented: explore_ceiling_topband.py's wide_class_reading to
    |d| <= 24000, explore_cubic_split_triple.py's read_field, and
    explore_triple_cube_term.py's place_over_two, walk_field, merge,
    level, share_of and bin table. Every control those files run rides
    in with them. New code is THREE pieces only: a Smith normal form, a
    structural keying of the strata, and the generated-subgroup test.

 T2 FROM explore_triple_cube_term.py (4): the closed form's shape. What
    is NOT transplanted is its cyclic evaluation -- (c) re-derives the
    counts over an arbitrary group, and P1 checks the reduction.

 T3 THE CORRECTED LEVEL'S FLATNESS ACROSS h IS A PATTERN ON CYCLIC
    STRATA and is carried in as an expectation only. No line of this
    file treats it as a law, and P5 states it as a prediction that can
    fail.

 T4 THE PARENTS' EXCLUSIONS STAND: the three fields their T4 policy
    drops stay dropped, the prime 2 and the ramified primes stay in the
    unallocated bound, and MIN_READ = 10 expected corrected counts is
    the parents' own readability bar, not a bar chosen here.

THE PREDICTIONS, frozen before the engine ran. Each names what the rig
PRINTS and not what it would mean.

 P1 (positive control, run before any verdict is read) At every field
    whose invariant factors are a single number, |Cl[m]| computed from
    the factors equals gcd(m, h) for every m in 2..12. Print: the count
    of mismatches, expected 0.

 P2 (positive control) At every field the invariant factors multiply to
    span_order's h and each divides the next. Print: the count of
    violations, expected 0.

 P3 (positive control) The structural census over |d| <= 24000
    reproduces explore_ceiling_topband.py F4 exactly: 5 fields at
    Z/2 x Z/2 with h = 4 and 4 fields at Z/2 x Z/4 with h = 8. Print:
    the two counts.

 P4 (positive control) Summing the structural strata back over h
    reprints the parent's corrected all-principal levels. Print: the
    per-h corrected level beside explore_triple_cube_term.py's own,
    with the h = 2 row at 1.058 +- 0.017 the tightest of them.

 P5 The corrected level on the non-cyclic cells lands within 2 sigma of
    1, because the walk's correction is measured in the field's own
    lattice and the model share is group-blind. Print: level, z and the
    raw count per non-cyclic cell.

 P6 Neither non-cyclic cell clears MIN_READ = 10 expected corrected
    counts, so neither is readable by the parents' own bar and the
    deliverable is a level with its spread. Print: the expectation per
    cell against the bar.

 P7 The generalized closed form parts from the cyclic one on exactly the
    non-cyclic cells: at h = 4 the square's group count 3h + |Cl[2]|^2
    reads 28 over Z/2 x Z/2 against 16 over Z/4, and at h = 8 it reads
    40 over Z/2 x Z/4 against 28 over Z/8. Print: both counts per cell
    and the expected correction each implies.

 P8 The mapped split triples generate all of N at every composite-h
    field with at least MIN_SPLIT mapped split primes. Print: the count
    of fields whose generated subgroup is proper, with its order.

THE KILL-SHAPES, as observables. P1, P2, P3 or P4 printing a nonzero
mismatch kills the reading outright -- the reader, not the question, is
what failed, and no level below it is read. P8 printing proper subgroups
at composite h does not kill the reading: it demotes the model share at
those fields, and the rows it touches are named.

THE FINDINGS.

 F1 THE GROUP READER, AND WHAT THE STRATA ACTUALLY WERE (observation;
    exact over the enumerated box). 4865 fields kept to |d| <= 24000,
    1367 with h > 1, the parents' three unresolved exclusions standing.
    Keyed by invariant factors the population splits into 21 structural
    strata, of which exactly two are non-cyclic: Z/2 x Z/2 at h = 4,
    5 fields over |d| 6571..22123, and Z/2 x Z/4 at h = 8, 4 fields over
    |d| 11003..21443 -- explore_ceiling_topband.py F4's counts, reached
    by a different route. AND THE NON-CYCLIC FIELDS WERE NEVER ABSENT
    FROM THE CORRECTED LEVEL: the h = 4 stratum holds 106 fields and the
    h = 8 stratum 23, which are 101 + 5 and 19 + 4. The cell was unread
    as a CELL and its fields were being read all along, pooled into an
    h stratum that does not name them.

 F2 THE NON-CYCLIC LEVEL, AND IT DOES NOT SEPARATE (observation; the
    cells are below the parents' own readability bar and are reported
    with their spread rather than as a verdict). Z/2 x Z/2: 5 fields,
    128 split primes, raw all-principal 4 (raw level 0.500), correction
    +12.0, expected corrected count 9.8 against the bar of 10.0,
    corrected level 1.635 at z = +1.99. Its control -- the CYCLIC fields
    of the same h in the same |d| window, 70 of them -- reads 1.065 at
    z = +0.73 on an expectation of 125.6. THAT CONTROL MATCHES A WINDOW
    AND NOT A DISTRIBUTION, which is a weaker thing and is why S5 prints
    both: the level is known to move with |d|, so a five-field cell
    could sit at one end of a window its control spreads across. Here it
    does not -- cell mean |d| 13936 against the control's 14778 (medians
    16871 and 15243), and at h = 8 16033 against 16258 (18923 and
    16411) -- so the window match happens to carry a distribution match
    too, measured rather than assumed. THE TWO LEVELS -- 1.635 and
    1.065 -- differ by about 1.8 of the non-cyclic cell's own sigma,
    which is not a separation. Z/2 x Z/4: 4 fields, 95 split primes, raw all-principal
    ZERO, so its corrected level of 1.924 is CORRECTION ALONE over an
    expectation of 1.8, exactly the degeneracy the hand-attack (d) said
    to print rather than to quote; its own window's cyclic control reads
    1.292 on 12 fields. Neither cell answers the question at this cap, and the cap
    a separation would need is the deliverable in their place: the
    difference of 0.570 sits at 1.72 of the two cells' combined sigma
    (0.319 on the Klein cell, 0.089 on its control), so 3 sigma needs
    the Klein cell's own sigma at 0.168 -- an expectation of about 35
    against the present 9.8, which at this correction density is roughly
    18 Klein fields against the present 5.

 F3 THE COMPARATOR OVER A GROUP, AND WHY IT CANNOT ARBITRATE HERE
    (observation). The group-general closed form parts from the cyclic
    one exactly where predicted: the square's group count reads 28 over
    Z/2 x Z/2 against 16 over Z/4 and 40 over Z/2 x Z/4 against 28 over
    Z/8, while the cube's count is unmoved (33 and 129 both ways),
    because the 3-part of both groups is trivial and the cube term is
    2h^2 regardless. Expected corrections: 14.49 against 9.91, and 6.40
    against 4.80. BUT THE CLOSED FORM OVERSHOOTS EVERYWHERE -- the
    measured-over-predicted ratio runs 0.23 to 0.66 across the nineteen
    strata that carry any measured correction at all -- the two
    single-field cells at h = 12 D and h = 16 measure 0.0 -- and is not
    constant in h (0.659 at h = 2, 0.494 at h = 4,
    0.557 at h = 5, 0.382 at h = 8, 0.257 at h = 9), so there is no
    calibration to test a rival form against. What can be said is weak
    and is stated weakly: in BOTH non-cyclic cells the group-general
    form moves the ratio toward the same-h cyclic neighbour's and the
    cyclic form moves it away (0.829 against 1.213 at h = 4, where the
    neighbour reads 0.494; 0.546 against 0.729 at h = 8, where the
    neighbour reads 0.382) -- two cells of five and four fields, an
    observation and not a measurement.

 F4 THE SUBGROUP THE OBSERVED TRIPLES GENERATE IS N OR IT IS THE
    DEGENERATE ONE, WHOSE INDEX IS 3^r FOR r THE 3-RANK (the index a
    property, derived below; which of the two is generated, an
    observation over 1283 fields with at least 10 mapped split primes;
    what that says about the IMAGE, an inference with a bound, below;
    S7 and S9; the printed sections call this the IMAGE TEST, which is
    its working name and not a claim -- what it computes is the
    generated subgroup). 1128 fields generate all of N.
    The other 155 are proper and every one has index exactly 3: order 3
    of 9 at h = 3 (130 fields), 12 of 36 at h = 6 (15), 27 of 81 at
    h = 9 (9), 48 of 144 at h = 12 (1).
    THE INDEX IS NOT A MEASUREMENT. Write Delta for the degenerate
    subgroup {(a, b, c) in N : a = b = c mod 3Cl} and r for the 3-rank,
    dim_F3 of Cl/3Cl. The map N -> (Cl/3Cl)^2 sending (a, b, c) to
    (a - b, b - c) has kernel Delta; its image lies in the DIAGONAL,
    because (a - b) - (b - c) = (a + b + c) - 3b = 0 there; and it hits
    every diagonal element, (u, 0, -u) being in N. So that MAP's image is
    the diagonal -- a different image from the Galois one below, and the
    only place this file uses the word for anything else -- and
    [N : Delta] = 3^r exactly. EVERY field in this box has
    r <= 1 -- h = 9's group is cyclic Z/9, so its 3-rank is 1, not 2 --
    which is why 3 is the only index that appears, and the appearance is
    therefore not evidence about r >= 2 at all.
    AND WHAT IS MEASURED IS THE OBSERVED TRIPLES, NOT THE IMAGE. The
    subgroup the mapped split primes GENERATE is a lower bound on the
    Galois image; generating all of N proves the image is N, but
    generating Delta leaves open that the image is N and every observed
    triple happened to land in a proper subgroup. That is an inference
    with a bound rather than a proof: N has four subgroups of index 3 at
    r = 1, each triple of a full image lands in a given one with
    probability 1/3, and every tested field has at least 10 of them, so
    the expected number of the 1283 misread this way is at most
    1283 x 4 x 3^-10 = 0.09. Under that bound the census settles the
    hypothesis the uniform model needs and the parents record as
    unchecked at composite h: the image fills N, or it is Delta and the
    field's honest model share is 1 over |Delta| rather than 1/h^2.

 F5 THE DEGENERACY CONDITION IS A SUBGROUP ONE, AND THE SCALAR TEST IT
    REDUCES TO TAKES h/3 AND NOT h STRIPPED OF ITS 3s, THE TWO PARTING
    COMPANY AT 9 | h (rule in range, all 514 fields
    with 3 | h and at least 10 mapped split primes; the two moduli run
    against the generated subgroup directly). The
    parents' regime sorter asks whether m.(b_i - b_j) = 0 on every
    mapped split prime with m = h stripped of ALL its factors of 3.
    The index-3 subgroup asks for h/3. Those agree whenever the 3-part
    of h is exactly 3 -- h = 3, 6, 12, where both tests flag 130, 15 and
    1 fields and the generated subgroup agrees with both -- and part
    company at
    h = 9, where the parents' modulus is 1, the test demands the three
    classes be EQUAL, no field satisfies it, and all 30 fields are
    called full-image. The h/3 test flags 9 of them, and the generated
    subgroup flags the same 9: over all 514 the h/3 test and the generated
    subgroup disagree at ZERO fields. IT IS THE CONJUNCTION OF THE TWO
    THAT IDENTIFIES THE SUBGROUP, and neither alone does. The generated
    ORDER alone says only that some index-3 subgroup was generated, and
    N has four of them at r = 1; the h/3 test alone says only that every
    observed triple lies inside Delta. Together they give containment
    and equal order, hence equality: the generated subgroup IS Delta.
    What F4's derivation asks for is b_i - b_j in 3Cl, and
    (h/3).(b_i - b_j) = 0 is what that becomes when the 3-part of Cl is
    cyclic -- which every field with 3 | h in this box has, so the
    subgroup form is the one to carry forward and the scalar form is
    verified only where it was run.

 F6 SO THE h = 9 CORRECTED LEVEL WAS READING A MISCLASSIFICATION
    (observation; the split is 9 fields against 21). The parents' h = 9
    stratum reads 1.200 pooled. Split by the subgroup generated, the 9
    degenerate fields on their honest share 1/27 read 0.805 at
    z = -0.57 -- against 2.414 at z = +2.39 on the share 1/81 they were
    being given -- and the 21 that generate all of N read 0.727 at
    z = -0.74. Both halves sit
    BELOW 1 and both are consistent with it inside their own spread
    (expectations 8.6 and 7.3), so what the pooled 1.200 was is the
    average of a correct cell and a cell whose denominator was three
    times too small. The corrected level's flatness across h loses its
    h = 9 point, and loses it downward.

THE PREDICTIONS, WEIGHED.

 P1 PASSES: 0 cyclic fields where |Cl[m]| differs from gcd(m, h) over
    m = 2..12.
 P2 PASSES: 0 fields whose invariant factors miss span_order's h or the
    divisibility chain.
 P3 PASSES exactly: 5 fields at Z/2 x Z/2 with h = 4, 4 at Z/2 x Z/4
    with h = 8.
 P4 PASSES to the printed precision: the strata summed back over h
    reprint 1.058, 1.061, 1.068, 1.114 and 1.294 at h = 2, 4, 5, 7 and
    8, each differing from the parent's own by less than 0.0005.
 P5 PASSES, barely and not usefully: both cells land inside 2 sigma of
    1 (z = +1.99 and +1.25), which F2 reads as the cells being too small
    to land anywhere else.
 P6 PASSES: 9.8 and 1.8 expected corrected counts against the bar of
    10.0, so neither cell is readable and the deliverable is F2's.
 P7 PASSES with the numbers named at the freeze: 28 against 16, 40
    against 28. F3 is what the pass is worth.
 P8 PASSES as stated -- no composite-h field classified as full-image
    by the CORRECTED test, with enough split primes, generates a proper
    subgroup -- but the prediction was written expecting nothing to be
    found, and F4 and F5 are what the test found instead. The nine
    h = 9 fields are composite-h fields generating a proper subgroup,
    and they are proper against the parents' classification rather than
    against the corrected one.

WHAT THIS LEAVES. The question as posed -- does the corrected level move
when the class group stops being cyclic -- is answered "not at this cap,
and here is the cap it would need". What outran it is the control: an
instrument built to check a hypothesis nobody had checked found the
hypothesis true everywhere except at nine fields, and found the test the
corpus was using for it to be a formula that coincides with the right one
only when the 3-part of the class number is exactly 3. Two things are NOT
asked here. Whether the index law's r >= 2 case reads 9, which needs a
class group of 3-RANK 2 -- Z/3 x Z/3 inside Cl, hence 9 | h with a
non-cyclic 3-part. This box holds none: being non-cyclic is NOT the
requirement and Z/6 x Z/2 would not meet it either, its 3-rank being 1.
The scalar h/3 test has no reason to reproduce the subgroup condition
there, so that population tests both halves of F5 at once. (Priced 2026-08-23
by explore_image_share.py F4-F6: this box has no non-cyclic 3-part at any
stratum -- over the 1283 fields with h > 1 the census reads 769 with a
trivial 3-part, 484 at Z/3 and 30 at Z/9 and nothing else, and an h = 1
field's is trivial by definition -- so the requirement fails everywhere and
not only at h = 9, and the arrival cap is a bracket near 50000-200000 rather
than a place.) And whether the same
modulus slip touches the all-EQUAL event's regime sorting as it touches
the all-principal one; only the all-principal share was re-read here.
(Settled 2026-08-23 by explore_image_share.py F1-F3: it does, the two
corrected moduli being one share formula -- an event's size over the order
of the image -- and the h = 9 equal level dissolves the same way, its pooled
1.359 splitting into 1.101 and 0.674, both consistent with 1.)

RUN RECORD. 2026-08-23, Windows 11, Python 3,
`NCL_CKPT=<scratch>/ncl_ckpt2.json python prime/code/memwatch.py python
prime/code/explore_noncyclic_level.py`. One process, CPython, no BLAS.
5 checks passed, 730.5 s wall, peak working set 125.5 MB against
memwatch's 512 MB ceiling. Population: 15370 + 85050 polynomials ->
1103 base + 3765 increment fields in 51 s; class reading 4865 kept,
3 excluded unresolved, 571 s; the structural walk 101 s. The estimate
before the run was 13-16 minutes and the run was 12.2. REHEARSAL AND
EARLIER ATTEMPTS, all before any science print: the Smith normal form,
the torsion count and the group-general closed form were unit-rehearsed
against the parent's cyclic count_pow over h = 2..19 and m = 2..9 with 0
mismatches, and the whole pipeline was rehearsed on a 419-field box at
cap 2500 in 16 s. That rehearsal is what surfaced the C2 control -- the
image test reproducing the parents' h = 3 degenerate classification from
the other side -- which the freeze did not name and which is what made
F4 and F5 readable. The first science run died in S5 on a print that
read its own return value before the call returned; nothing was read
from it beyond the sections above S5, and the checkpoint (NCL_CKPT) was
added in the same repair so that no later reading costs the walk again.
S8, S9 and S10 are POST-RUN readings, added after the printed output was
in hand and marked as such in the print itself; so is S5's comparison of
the cell's |d| distribution against its control's, added by the audit
that found "matched" claiming more than a window match delivers. Every
one of them re-ran off the checkpoint in under a second and none of
them adds a check, so the count and the wall above are the science
run's and are not restated by the re-reads.
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
import explore_triple_cube_term as TCT

CHECKS = 0
MIN_READ = TCT.MIN_READ
MIN_SPLIT = TCT.MIN_SPLIT
PRIME_CAP = TCT.PRIME_CAP


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


# --------------------------------------------------------- the group reader
def snf(rows):
    """Invariant factors of Z^n / span(rows) for a square full-rank
    integer matrix: the Smith normal form's diagonal, each dividing the
    next, ones kept so the product is the order."""
    M = [list(r) for r in rows]
    n = len(M)
    m = len(M[0]) if n else 0
    t = 0
    while t < min(n, m):
        piv = None
        for i in range(t, n):
            for j in range(t, m):
                if M[i][j] and (piv is None
                                or abs(M[i][j]) < abs(M[piv[0]][piv[1]])):
                    piv = (i, j)
        if piv is None:
            break
        while True:
            i0, j0 = piv
            M[t], M[i0] = M[i0], M[t]
            for r in range(n):
                M[r][t], M[r][j0] = M[r][j0], M[r][t]
            done = True
            for i in range(t + 1, n):
                if M[i][t]:
                    q = M[i][t] // M[t][t]
                    M[i] = [x - q * y for x, y in zip(M[i], M[t])]
                    if M[i][t]:
                        done = False
            for j in range(t + 1, m):
                if M[t][j]:
                    q = M[t][j] // M[t][t]
                    for r in range(n):
                        M[r][j] -= q * M[r][t]
                    if M[t][j]:
                        done = False
            if done:
                break
            piv = None
            for i in range(t, n):
                for j in range(t, m):
                    if M[i][j] and (piv is None
                                    or abs(M[i][j])
                                    < abs(M[piv[0]][piv[1]])):
                        piv = (i, j)
        if M[t][t] < 0:
            M[t] = [-x for x in M[t]]
        t += 1
    d = [abs(M[i][i]) for i in range(min(n, m))]
    # the divisibility pass: fix any adjacent pair out of order
    again = True
    while again:
        again = False
        for i in range(len(d) - 1):
            a, b = d[i], d[i + 1]
            if a and b and b % a:
                g = math.gcd(a, b)
                d[i], d[i + 1] = g, a * b // g
                again = True
    return d


def factors_of(piv, k):
    """(invariant factors above 1, h) for the class group Z^k / span."""
    d = snf([row for (_c, row) in piv])
    h = 1
    for x in d:
        h *= x
    return [x for x in d if x > 1], h


def torsion(fac, m):
    """|Cl[m]| = prod gcd(m, d_i) over the invariant factors."""
    out = 1
    for x in fac:
        out *= math.gcd(m, x)
    return out


def group_name(fac):
    if not fac:
        return "trivial"
    return " x ".join("Z/%d" % x for x in fac)


def count_pow_g(fac, h, m, event):
    """(4) over an arbitrary Cl: #{g in G : g^m in event}."""
    ev = 1 if m % 2 == 0 else 0
    th = 1 if m % 3 == 0 else 0
    if event == 'e':
        return (torsion(fac, m) ** 2
                + ev * 3 * h * torsion(fac, m // 2)
                + th * 2 * h * h)
    if event == 'D':
        return (torsion(fac, 3 * m) * torsion(fac, m)
                + ev * 3 * h * torsion(fac, 3 * m // 2)
                + th * 2 * h * h)
    return h * h * (1 + ev * 3 + th * 2)


def expected_corr_g(fac, h, event, nfields, lo, hi):
    """E[c_event] over nfields fields for q^m in [lo, hi), m >= 2."""
    tot = 0.0
    for q in [2] + list(TCT.ODD_PRIMES):
        for (m, n) in TCT.powers(q):
            if m < 2 or not (lo <= n < hi):
                continue
            tot += (1.0 / m) * count_pow_g(fac, h, m, event) / (6.0 * h * h)
    return tot * nfields


# ------------------------------------------------------- the image test
def generated_index(per_prime, piv, k, h):
    """The order of the subgroup of N generated by the mapped split
    triples, via N = Cl^2 in the (a, b) coordinates: Z^2k modulo the
    lattice spanned by those pairs together with L (+) L."""
    rows = []
    for (_p, kd, vecs) in per_prime:
        if kd != 'split' or len(vecs) != 3 or any(v is None for v in vecs):
            continue
        rows.append(list(vecs[0]) + list(vecs[1]))
    if not rows:
        return 0
    for (_c, row) in piv:
        rows.append(list(row) + [0] * k)
        rows.append([0] * k + list(row))
    p2 = CCM.echelon(rows, 2 * k)
    idx = CCM.span_order(p2, 2 * k)
    if idx is None:
        return None
    return (h * h) // idx if idx and (h * h) % idx == 0 else None


# ------------------------------------------------------------- the walk
def read_population(recs):
    """One walk. Returns (cells_by_key, meta, badsum, image) with key
    (h, tuple(factors), reg) and meta[key] = (nfields, [|d| ...])."""
    cells, meta, perfield = {}, {}, []
    image = dict(tested=0, full=0, proper=[], thin=0)
    bad = 0
    ctrl = dict(cyc_mismatch=0, fac_bad=0)
    t0 = time.time()
    for rec in recs:
        (d, cx, a, b, c, O, h, kind, gp, rel) = rec
        if h is None or h == 1 or not cx:
            continue
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        if H is None or H == 1:
            continue
        fac, hf = factors_of(piv, k)
        if hf != H or any(fac[i + 1] % fac[i] for i in range(len(fac) - 1)):
            ctrl['fac_bad'] += 1
        if len(fac) <= 1:
            for m in range(2, 13):
                if torsion(fac, m) != math.gcd(m, H):
                    ctrl['cyc_mismatch'] += 1
        two = TCT.place_over_two(rec)
        cl, nb, _small = TCT.walk_field(rec, per_prime, piv, k, two)
        bad += nb
        ns = sum(x['ns'] for x in cl.values())
        neq = sum(x['neq'] for x in cl.values())
        reg = 'A'
        if H % 3 == 0:
            exact = TCT.diagonal_3part(per_prime, piv, k, H)
            if H == 3:
                reg = ('X' if ns < MIN_SPLIT
                       else 'D' if float(neq) / ns >= TCT.HIGH_FRAC else 'M')
            else:
                reg = 'X' if ns < MIN_SPLIT else 'D' if exact else 'M'
        g = None
        dpar = dcor = None
        if H % 3 == 0 and ns >= MIN_SPLIT:
            dpar = diagonal_mod(per_prime, piv, k, TCT.three_free(H))
            dcor = diagonal_mod(per_prime, piv, k, H // 3)
        if ns >= MIN_SPLIT:
            image['tested'] += 1
            g = generated_index(per_prime, piv, k, H)
            if g == H * H:
                image['full'] += 1
            else:
                image['proper'].append((d, H, group_name(fac), g, reg))
            image.setdefault('byreg', {}).setdefault((H, reg), [0, 0])
            image['byreg'][(H, reg)][0] += 1
            image['byreg'][(H, reg)][1] += 1 if g == H * H else 0
        else:
            image['thin'] += 1
        key = (H, tuple(fac), reg)
        m_ = meta.setdefault(key, [0, []])
        m_[0] += 1
        m_[1].append(abs(d))
        st = cells.setdefault(key, {})
        one = TCT.new_cell()
        for bi, cell in cl.items():
            TCT.merge(st.setdefault(bi, TCT.new_cell()), cell)
            TCT.merge(one, cell)
        perfield.append((abs(d), H, tuple(fac), reg, one, g, dpar, dcor))
    print("  mapped complex population walked in %.1f s, %d structural "
          "strata" % (time.time() - t0, len(cells)))
    return cells, meta, bad, image, ctrl, perfield


def diagonal_mod(per_prime, piv, k, m):
    """The parents' diagonal test with its modulus made a parameter:
    m.(b_i - b_j) = 0 on every fully mapped split prime."""
    for (_p, kd, vecs) in per_prime:
        if kd != 'split' or len(vecs) != 3 or any(v is None for v in vecs):
            continue
        u = [TCT.scale(v, m) for v in vecs]
        if not (ST.same_class(u[0], u[1], piv, k)
                and ST.same_class(u[0], u[2], piv, k)):
            return False
    return True


def pooled(st):
    out = TCT.new_cell()
    for cell in st.values():
        TCT.merge(out, cell)
    return out


def row(label, c, h, reg, nf, extra=""):
    share = TCT.share_of(h, reg)
    lv_raw, _zr, _er = TCT.level(c['n3'], 0.0, c['ns'], share)
    lv, z, exp = TCT.level(c['n3'], c['c3'], c['ns'] + c['cN'], share)
    print("  %-26s %3d fields  split %5d  all-p %4d  raw %s  corr +%.1f"
          "  exp %5.1f  level %s  z %s%s"
          % (label, nf, c['ns'], c['n3'],
             "%.3f" % lv_raw if lv_raw is not None else "--",
             c['c3'], exp,
             "%.3f" % lv if lv is not None else "--",
             "%+.2f" % z if z is not None else "--", extra))
    return lv, z, exp


CKPT = os.environ.get("NCL_CKPT")


def ckpt_save(payload):
    if not CKPT:
        return
    cells, meta, bad, image, ctrl, perfield = payload
    blob = dict(
        bad=bad, ctrl=ctrl,
        image=dict(tested=image['tested'], full=image['full'],
                   thin=image['thin'], proper=image['proper'],
                   byreg=[[list(k), v] for k, v in
                          image.get('byreg', {}).items()]),
        cells=[[list(k), [[bi, cell] for bi, cell in st.items()]]
               for k, st in cells.items()],
        meta=[[list(k), v] for k, v in meta.items()],
        perfield=[[ad, h, list(f), reg, one, g, dp, dc]
                  for (ad, h, f, reg, one, g, dp, dc) in perfield])
    with open(CKPT, "w") as fh:
        json.dump(blob, fh)
    print("  checkpoint written to %s" % CKPT)


def ckpt_load():
    if not CKPT or not os.path.exists(CKPT):
        return None
    with open(CKPT) as fh:
        blob = json.load(fh)
    cells = {tuple(k[:1]) + (tuple(k[1]), k[2]): {int(bi): cell
                                                  for bi, cell in st}
             for k, st in blob['cells']}
    meta = {tuple(k[:1]) + (tuple(k[1]), k[2]): v for k, v in blob['meta']}
    perfield = [(ad, h, tuple(f), reg, one, g, dp, dc)
                for (ad, h, f, reg, one, g, dp, dc) in blob['perfield']]
    image = blob['image']
    image['byreg'] = {(k[0], k[1]): v for k, v in image['byreg']}
    image['proper'] = [tuple(x) for x in image['proper']]
    print("  checkpoint reloaded from %s -- the walk is not re-run"
          % CKPT)
    return cells, meta, blob['bad'], image, blob['ctrl'], perfield


def exp_ok(exp):
    return exp is not None and exp >= MIN_READ


def main():
    t0 = time.time()
    section("S1  THE POPULATION -- explore_ceiling_topband.py's wide "
            "class reading to |d| <= %d" % TB.WIDE_CAP)
    got = ckpt_load()
    if got is None:
        recs = TB.wide_class_reading()

    section("S2  THE GROUP READER -- invariant factors, and the two "
            "positive controls -- P1, P2")
    if got is None:
        got = read_population(recs)
        ckpt_save(got)
    cells, meta, bad, image, ctrl, perfield = got
    print("  [C1] split-prime power triples off zero-sum: %d" % bad)
    ok(bad == 0, "%d power triples do not sum to zero" % bad)
    print("  [P2] fields whose factors miss span_order or divisibility: %d"
          % ctrl['fac_bad'])
    ok(ctrl['fac_bad'] == 0, "%d fields with bad factors" % ctrl['fac_bad'])
    print("  [P1] cyclic fields where |Cl[m]| != gcd(m, h), m = 2..12: %d"
          % ctrl['cyc_mismatch'])
    ok(ctrl['cyc_mismatch'] == 0,
       "%d cyclic torsion mismatches" % ctrl['cyc_mismatch'])

    section("S3  THE STRUCTURAL CENSUS -- P3")
    noncyc = []
    for key in sorted(cells, key=lambda x: (x[0], len(x[1]), x[1], x[2])):
        (h, fac, reg) = key
        nf, ds = meta[key]
        mark = ""
        if len(fac) > 1:
            noncyc.append(key)
            mark = "   NON-CYCLIC"
        print("  h = %2d  %-14s %-2s %4d fields  |d| %6d..%6d%s"
              % (h, group_name(list(fac)), reg, nf, min(ds), max(ds), mark))
    klein4 = sum(meta[k][0] for k in noncyc if k[0] == 4 and k[1] == (2, 2))
    z28 = sum(meta[k][0] for k in noncyc if k[0] == 8 and k[1] == (2, 4))
    print("  [P3] Z/2 x Z/2 at h = 4: %d fields (F4 says 5); "
          "Z/2 x Z/4 at h = 8: %d fields (F4 says 4)" % (klein4, z28))
    ok(klein4 == 5, "Z/2 x Z/2 count is %d, not 5" % klein4)
    ok(z28 == 4, "Z/2 x Z/4 count is %d, not 4" % z28)

    section("S4  THE CYCLIC REPRINT -- the strata summed back over h -- P4")
    byh = {}
    for key, st in cells.items():
        (h, fac, reg) = key
        k2 = (h, reg)
        into = byh.setdefault(k2, [TCT.new_cell(), 0])
        TCT.merge(into[0], pooled(st))
        into[1] += meta[key][0]
    parent = {2: 1.058, 4: 1.061, 5: 1.068, 6: 1.117, 7: 1.114,
              8: 1.294, 9: 1.200}
    for (h, reg) in sorted(byh):
        c, nf = byh[(h, reg)]
        lv, _z, _e = row("h = %d %s" % (h, reg), c, h, reg, nf)
        if reg == 'A' and h in parent and lv is not None:
            print("       parent's own level %.3f, this reading %.3f, "
                  "difference %+.3f" % (parent[h], lv, lv - parent[h]))

    section("S5  THE NON-CYCLIC CELLS, and the matched control -- P5, P6")
    for key in noncyc:
        (h, fac, reg) = key
        nf, ds = meta[key]
        c = pooled(cells[key])
        lv, z, exp = row("%s %s" % (group_name(list(fac)), reg), c, h, reg,
                         nf)
        print("       expected corrected count %.1f against the parents'"
              " bar of %.1f -- %s" % (exp, MIN_READ,
                                      "readable" if exp_ok(exp)
                                      else "UNDER THE BAR"))
        lo, hi = min(ds), max(ds)
        mc, mn = TCT.new_cell(), 0
        for (ad, hh, ff, rr, one, _g, _dp, _dc) in perfield:
            if hh == h and rr == reg and len(ff) <= 1 and lo <= ad <= hi:
                TCT.merge(mc, one)
                mn += 1
        print("       raw all-principal count %d%s"
              % (c['n3'], "  (the level is correction alone)"
                 if c['n3'] == 0 else ""))
        if mn:
            cd = sorted(ad for (ad, hh, ff, rr, _o, _g, _p, _c) in perfield
                        if hh == h and rr == reg and len(ff) <= 1
                        and lo <= ad <= hi)
            print("       the control matches the WINDOW; how well it "
                  "matches the distribution inside it is the reading: "
                  "cell mean |d| %.0f median %d, control mean %.0f "
                  "median %d"
                  % (sum(ds) / float(len(ds)), sorted(ds)[len(ds) // 2],
                     sum(cd) / float(len(cd)), cd[len(cd) // 2]))
            row("  matched cyclic |d| %d..%d" % (lo, hi), mc, h, reg, mn)
        else:
            print("       no cyclic field of this h sits in |d| %d..%d"
                  % (lo, hi))

    section("S6  THE COMPARATOR OVER A GROUP -- P7")
    for key in noncyc:
        (h, fac, reg) = key
        nf, _ds = meta[key]
        sq_g = count_pow_g(list(fac), h, 2, 'e')
        sq_c = TCT.count_pow(h, 2, 'e')
        cb_g = count_pow_g(list(fac), h, 3, 'e')
        cb_c = TCT.count_pow(h, 3, 'e')
        eg = expected_corr_g(list(fac), h, 'e', nf, 0, PRIME_CAP)
        ec = TCT.expected_corr(h, 'e', nf, 0, PRIME_CAP)
        print("  %-14s h = %2d  square count %3d (cyclic %3d)  cube count "
              "%4d (cyclic %4d)  E[corr] %.2f (cyclic %.2f)"
              % (group_name(list(fac)), h, sq_g, sq_c, cb_g, cb_c, eg, ec))

    section("S7  THE IMAGE TEST -- does the split triples' subgroup fill "
            "N -- P8")
    print("  fields with at least %d mapped split primes: %d; generating "
          "all of N: %d; thin: %d"
          % (MIN_SPLIT, image['tested'], image['full'], image['thin']))
    print("  [C2] by stratum and regime -- the h = 3 rows are the "
          "parents' own degenerate classification seen from the image "
          "side, a control the rehearsal surfaced and the freeze did not:")
    for (h, reg) in sorted(image.get('byreg', {})):
        tested, full = image['byreg'][(h, reg)]
        print("     h = %2d %s  %4d tested  %4d fill N  %4d proper"
              % (h, reg, tested, full, tested - full))
    tally = {}
    for (d, h, nm, g, reg) in image['proper']:
        key = (h, reg, nm, g)
        tally[key] = tally.get(key, 0) + 1
    print("  the proper images by stratum, order and count -- the share the"
          " uniform model owes each is 1/order, not 1/h^2:")
    for (h, reg, nm, g) in sorted(tally):
        print("     h = %2d %s  %-12s generated order %4s of %4d   %3d "
              "fields   model share 1/%s" % (h, reg, nm, g, h * h,
                                             tally[(h, reg, nm, g)], g))
    print("  [P8] proper subgroups at %d of %d tested fields"
          % (len(image['proper']), image['tested']))

    section("S8  THE COMPARATOR CALIBRATED -- a post-run reading, not a "
            "frozen prediction")
    print("  the closed form is a first-order model and the parent records"
          " it overshooting at small x, so its ABSOLUTE value decides"
          " nothing; the ratio measured/predicted is what can be compared"
          " across strata.")
    print("  %-16s %-3s %6s %10s %10s %8s %8s"
          % ("stratum", "reg", "fields", "measured", "predicted",
             "ratio", "cyc-ratio"))
    for key in sorted(cells, key=lambda x: (x[0], len(x[1]), x[1], x[2])):
        (h, fac, reg) = key
        nf, _ds = meta[key]
        c = pooled(cells[key])
        pg = expected_corr_g(list(fac), h, 'e', nf, 0, PRIME_CAP)
        pc = TCT.expected_corr(h, 'e', nf, 0, PRIME_CAP)
        print("  %-16s %-3s %6d %10.1f %10.2f %8s %8s"
              % (group_name(list(fac)), reg, nf, c['c3'], pg,
                 "%.3f" % (c['c3'] / pg) if pg else "--",
                 "%.3f" % (c['c3'] / pc) if pc else "--"))

    section("S9  WHAT THE PROPER IMAGES ARE -- a post-run reading")
    idx = {}
    for (_ad, h, _f, reg, _one, g, _dp, _dc) in perfield:
        if g and g != h * h:
            idx[(h, reg, h * h // g if (h * h) % g == 0 else None)] =                 idx.get((h, reg, h * h // g if (h * h) % g == 0 else None),
                        0) + 1
    print("  every proper image by its INDEX in N:")
    for (h, reg, i) in sorted(idx, key=lambda x: (x[0], x[1])):
        print("     h = %2d %s  index %s  %3d fields" % (h, reg, i,
                                                         idx[(h, reg, i)]))
    print()
    print("  the two diagonal tests at 3 | h -- the parents' modulus is h"
          " stripped of ALL its 3s, and h/3 is the one the index-3"
          " subgroup asks for; they coincide unless 9 divides h:")
    print("  %-4s %-3s %7s %9s %9s %9s"
          % ("h", "reg", "fields", "proper", "parent", "h/3"))
    tab = {}
    for (_ad, h, _f, reg, _one, g, dp, dc) in perfield:
        if dp is None:
            continue
        t = tab.setdefault((h, reg), [0, 0, 0, 0])
        t[0] += 1
        t[1] += 1 if (g and g != h * h) else 0
        t[2] += 1 if dp else 0
        t[3] += 1 if dc else 0
    for (h, reg) in sorted(tab):
        t = tab[(h, reg)]
        print("  %-4d %-3s %7d %9d %9d %9d"
              % (h, reg, t[0], t[1], t[2], t[3]))
    mism = sum(1 for (_ad, h, _f, reg, _one, g, dp, dc) in perfield
               if dc is not None and dc != (bool(g) and g != h * h))
    print("  the h/3 test against the image directly: %d fields where they"
          " disagree" % mism)

    section("S10  THE STRATA AT 3 | h RE-READ ON THE IMAGE'S OWN SHARE")
    print("  a field whose image has order g owes the model share 1/g and"
          " not 1/h^2; the parents' regime gives 1/(3 m^2), which is 1/g"
          " only where it agrees with the index-3 reading.")
    grp = {}
    for (_ad, h, _f, reg, one, g, dp, dc) in perfield:
        if h % 3 or g is None:
            continue
        k2 = (h, reg, g)
        into = grp.setdefault(k2, [TCT.new_cell(), 0])
        TCT.merge(into[0], one)
        into[1] += 1
    for (h, reg, g) in sorted(grp):
        c, nf = grp[(h, reg, g)]
        share_img = 1.0 / g
        share_par = TCT.share_of(h, reg)
        lv_i, z_i, e_i = TCT.level(c['n3'], c['c3'], c['ns'] + c['cN'],
                                   share_img)
        lv_p, z_p, e_p = TCT.level(c['n3'], c['c3'], c['ns'] + c['cN'],
                                   share_par)
        print("  h = %2d %s  image order %4d  %3d fields  all-p %4d  "
              "| on 1/%d: exp %6.1f level %s z %s  | on the parents' "
              "share 1/%.4g: exp %6.1f level %s z %s"
              % (h, reg, g, nf, c['n3'], g, e_i,
                 "%.3f" % lv_i if lv_i is not None else "--",
                 "%+.2f" % z_i if z_i is not None else "--",
                 1.0 / share_par, e_p,
                 "%.3f" % lv_p if lv_p is not None else "--",
                 "%+.2f" % z_p if z_p is not None else "--"))

    section("SUMMARY")
    print("  %d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
