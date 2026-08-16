"""IS THE PRINCIPAL DEFICIT THE IDENTITY CLASS'S ALONE? -- the share of
split primes falling in EVERY narrow class, not just the trivial one,
read at small p and graded by what a class can represent.

THE QUESTION. explore_principal_share.py measured the share of split
primes that are narrow principal and found it short of the nominal 1/h+
at small p, graded by the narrow class number h+ and FLAT in |D| across a
four-fold range. It read the identity class and nothing else, so the
deficit's own SHAPE has never been looked at: whether the trivial class
is uniquely short, or is the extreme of a law that grades every class.
The distinction decides what the effect IS. If every class carries a
characteristic share at small p and the trivial one merely sits at an
end, the grading is a property of a CLASS, which is a group quantity --
and a group quantity is blind to |D| for free, which is exactly the
property the field-side models could not produce.

WHOSE VOCABULARY THE SUSPICION IS WRITTEN IN. "Equidistribution
shortfall" is Chebotarev's vocabulary, and Chebotarev's objects are the
FIELD and its conductor -- which is the vocabulary in which the flatness
in |D| is a paradox. The suspicion here is written in the FORM's
vocabulary instead: a class is a class of binary quadratic forms, and a
form has a minimum. Nothing below a form's minimum is represented by it
at all, so a share at small p is a statement about minima before it is a
statement about equidistribution. The two vocabularies name the same
classes and do not have the same variables.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE CLASS OF A SPLIT PRIME, BY THE INCUMBENT'S OWN TEST. For odd p
      with chi_D(p) = +1 take b with b^2 = D mod 4p and b = D mod 2; then
      (p, b, (b^2-D)/(4p)) has discriminant D and represents p
      (explore_principal_share.py derivation 5). At D < 0 the reduced
      representative of that form IS the class, definite classes having
      one apiece. At D > 0 the class is the CYCLE containing the
      reduction, narrow equivalence being cycle equality. So the same
      test that returned one bit returns a class, and the count of
      classes reached plus those never reached is h+ -- which is C1
      rather than an assumption.

  (2) THE GRADING MUST BE COMPUTABLE WITHOUT COMPOSITION, and two are.
      THE MINIMUM m(C): the least value a class represents at a nonzero
      argument, which for a definite class is the reduced form's leading
      coefficient a, and for an indefinite one is min |a| over the cycle
      (every value of smallest absolute value is a leading coefficient of
      a reduced form in the cycle). AMBIGUITY: C has order at most 2 iff
      C = C^-1, and the inverse of (a, b, c) is (a, -b, c), so the test
      is whether reducing the opposite lands in the same class. Both are
      exact and neither needs Gauss composition, which is why the full
      ORDER of a class is out of scope here.

  (3) THE SIGN, RE-DERIVED HERE AND NOT IMPORTED. The trivial class's
      reduced form is (1, 0, |D|/4) at D = 0 mod 4 and (1, 1, (1+|D|)/4)
      at D = 1 mod 4. Its minimum is 1, attained at (1, 0) -- and 1 is
      NOT PRIME. Off that argument, at D < 0, completing the square
      settles both parities of b at once: x^2 + bxy + cy^2 of
      discriminant D is (x + by/2)^2 + (|D|/4) y^2, at least |D|/4 where
      y is nonzero whether b is 0 or 1, and a square where y is 0 and so
      never an odd prime. So at D < 0 NO prime below |D|/4 lies in the
      trivial class, while a class of reduced form (a, b, c) represents a
      outright at (1, 0) and a may itself be a small prime. The trivial
      class is therefore UNIQUELY handicapped at small p, and it is
      handicapped by the one feature that makes it trivial. This is a
      mechanism the pooled reading could not see, because a mechanism
      that acts on one class is invisible to a statistic that reads one
      class.

  (4) AND IT DOES NOT TRANSPLANT -- FLAGGED. At D > 0 the forms are
      indefinite, the trivial class's cycle contains forms of small |a|
      with no square constraint on the represented values, and the
      argument of (3) has no force: every class's minimum is O(sqrt D),
      the trivial one's included. So (3) predicts the imaginary side
      only. That the two sides were measured to AGREE to within the band
      is the fact this rig has to confront rather than inherit, and P3 is
      what that commitment costs.

  (5) THE POPULATION IS THE INCUMBENT'S. Fundamental discriminants of
      both signs to |D| <= 4000 over the odd split p <= 10^4, so that the
      trivial class's column here is comparable to the share already
      measured rather than to a fresh one, and C3 is the check that it is
      the same number.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. THE DEFICIT IS THE TRIVIAL CLASS'S ALONE, AT D < 0. In the bottom
      prime bin the trivial class's share ratio to nominal is the
      SMALLEST of the field's h+ ratios at a majority of imaginary fields
      with h+ > 1.

  P2. THE GRADING IS THE MINIMUM. Over NON-trivial classes at D < 0, the
      bottom-bin share ratio falls as m(C) rises, monotonically across
      the printed m bands -- a class represents nothing below its
      minimum, so a larger minimum must cost share where the primes are
      small.

  P3. THE REAL SIDE CARRIES THE SAME TRIVIAL-CLASS DEFICIT WITHOUT THE
      MECHANISM. At matched h+ the trivial class's bottom-bin ratio at
      D > 0 sits within 0.10 of the D < 0 one, while m(C) grades the real
      side's non-trivial classes weakly or not at all -- a spread across
      the m bands below half the imaginary side's.

  P4. AMBIGUITY ADDS NOTHING once m(C) is fixed. At either sign the
      ambiguous and non-ambiguous columns agree within 0.05 inside every
      m band.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, read after the
controls and weighed for meaning only afterward.

  K1 kills P1: the printed count of imaginary fields at which the trivial
     class holds the minimum bottom-bin ratio, against the count of
     imaginary fields with h+ > 1. At or below half is the kill.

  K2 kills P2: the printed bottom-bin ratio by m band over non-trivial
     imaginary classes. A column that is flat, non-monotone, or rising
     is the kill.

  K3 kills P3: the printed trivial-class bottom-bin ratio, real beside
     imaginary, row by matched h+; any matched pair differing by more
     than 0.10 kills the first half. And the printed real-side m-band
     column with a spread at least half the imaginary side's kills the
     second.

  K4 kills P4: the printed ambiguous/non-ambiguous pair inside each m
     band; any band where they differ by more than 0.05 at a sign.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. THE CLASS COUNT PIN, AND WHAT IT DOES NOT COVER. At every field the
      class inventory's size must equal h+ as the incumbent computes it
      -- the cycle count at D > 0, the reduced-form count at D < 0. A
      single disagreement invalidates every ratio at that field, the
      nominal 1/h+ being the denominator of all of them. But the two
      counts SHARE their enumeration: at D > 0 both run over
      all_reduced_forms and cycle_of, so a gap in the enumeration itself
      would be invisible here, and at D < 0 the two walks are separate
      code over the same bound. What covers that gap is not this control
      but the shape of the lookup: a split prime reducing to a form the
      inventory does not hold raises rather than mis-counts, so an
      enumeration gap ends the run instead of biasing a share. C1 is a
      pin on the GROUPING, and the KeyError is the pin on the
      enumeration; neither substitutes for the other.

  C2. THE PARTITION PIN. Per field and per bin the per-class counts must
      sum to that field's split-prime count in that bin. This is what
      catches a prime assigned to no class or to two, which the ratio
      columns would otherwise absorb silently.

  C3. THE TRIVIAL COLUMN AGAINST THE INCUMBENT. Restricted to the same
      population, bins and filters, the trivial class's share must
      reproduce explore_principal_share.py's narrow share. A rig that
      disagrees with the incumbent on the incumbent's own statistic is
      wrong until shown otherwise.

  C4. THE HAND-DERIVED HARD ZERO. At D < 0 no prime below |D|/4 may lie
      in the trivial class, by derivation (3). Printed as a violation
      count; anything but zero means the derivation is wrong and the
      slate built on it is void.

THE FOLLOW-UP READING -- frozen AFTER K1-K4 printed and before the bin
sweep that answers it, and flagged post-hoc for that reason.

  K5. IS THE AMBIGUOUS EFFECT A BOTTOM-OF-RANGE ONE? K4 reads one bin, so
      an ambiguous deficit there is consistent with a standing one and
      with a small-p one alike -- the same ambiguity the pooled reading
      of the trivial class had before its own bins were cut. Printed as
      the ambiguous and non-ambiguous means in all three bins with m
      pooled. A deficit that persists into the top bin is a standing
      property of the 2-torsion; one that closes is the trivial class's
      effect wearing a wider hat.

THE FINDINGS.

  THE CONTROLS. C1 and C2 print zero failures at both signs over 1217
  imaginary and 1216 real fields -- every field's class inventory has the
  size the incumbent's h+ says, with the caveat C1 states about the
  enumeration they share, and every split prime lands in exactly one
  class. C3 reproduces explore_principal_share.py's narrow
  share exactly where that rig printed it: 0.6615, 0.8550, 0.9640 over
  the three bins at h+ = 8 on the real side, against its 0.662, 0.855,
  0.964. C4 prints zero violations, so derivation (3) holds as stated --
  no prime below |D|/4 lies in the trivial class at D < 0.

  **THE DEFICIT IS THE TRIVIAL CLASS'S, AND IT HAS COMPANY**
  (observation; P1 survives, and K1 says how -- ON THE CONTROLLED
  POPULATION, the raw reading being partly an artifact this rig's own
  first pass did not separate). The trivial class holds its field's
  smallest bottom-bin ratio at 0.818 of real fields with h+ > 1 and 0.768
  of imaginary ones, so P1's majority holds at both signs. The STRICT
  rates are where the shape is, and the zero-tie control is what makes
  them readable: raw, they run 0.744 real against 0.427 imaginary, but
  227 of the 928 imaginary weak hits are ties AT ZERO against 1 of 802 on
  the real side -- manufactured by the very hard zero C4 verifies, since
  a class empty by construction ties with every other empty class. On
  fields carrying at least 4 split primes per class in the bin, where an
  empty class is a measurement rather than a shortage, the ties fall to 4
  and 0 and the rates become 0.746 real against 0.542 imaginary. So the
  gap is 0.204 and not the 0.317 the uncontrolled reading showed, and it
  survives: on the real side the trivial class is alone at the bottom,
  and on the imaginary side it is not. The real side's own rate is
  unmoved by the control (0.744 to 0.746), which is what says the control
  removed an artifact rather than a signal. AND THE OBVIOUS DEFLATION OF
  THAT SURVIVING GAP DIES TOO, printed beside it: a class is harder to
  isolate at the bottom where more classes are short, so the imaginary
  side's lower strict rate would be explained if its fields carried more
  short company. They carry LESS -- 1.54 non-trivial ambiguous classes
  per field against the real side's 1.90 -- so the side with MORE company
  holds the HIGHER strict rate and the deflation runs backwards. The gap
  stands unexplained, which is a different and better state than
  explained away.

  **THE MINIMUM GRADES NOTHING** (K2 fires; P2 dead). Over non-trivial
  classes in the bottom bin the ratio runs 0.9846, 1.0596, 1.0221 across
  the imaginary m bands and 1.0140, 1.0687, 1.0530 across the real ones
  -- non-monotone at both signs, where P2 wanted a fall. So the fact that
  a class represents nothing below its minimum, which is exactly what
  produces the trivial class's hard zero at C4, does NOT extend to a
  grading over the other classes. The vocabulary of derivation (2) was
  right about the class it was derived on and wrong as a general dial.

  SETTLED SINCE BY explore_class_order.py, and the pointer is here
  because the block below is the one a reader would quote: ambiguity is
  order at most 2, and what grades the share is the ORDER -- small-order
  classes short and order 5 or more running LONG, at both signs. The
  MEASUREMENT below survives and that rig reproduces it exactly; the
  reading of the 2-torsion as the OBJECT does not, it being the finest
  cut reachable without composition.

  **WHAT GRADES THE SHARE IS AMBIGUITY, AT BOTH SIGNS** (K4 fires at
  D < 0; P4 dead. THE POOLED READING SAYS "IMAGINARY ONLY" AND K6 SHOWS
  THAT IS ITS COMPOSITION TALKING -- see the block after next, which is
  the controlled one and the one to quote). Inside every m band at D < 0
  the ambiguous non-trivial classes sit at 0.8901, 0.9264, 0.8888 against
  1.0090, 1.0681, 1.0284 for the non-ambiguous -- a gap of 0.119 to
  0.142, uniform across the bands and so not a minimum effect in
  disguise, on 361 to 906 pairs per cell. AND
  THIS IS NOT THE GENUS READING COMING BACK: explore_principal_share.py
  cleared the genus congruences by factoring the share through the
  principal GENUS, a QUOTIENT of the narrow class group, finding deficits
  of the same shape on both factors and an ordinary one at the one-genus
  fields. The ambiguous classes are the 2-TORSION SUBGROUP, which C6
  prints as carrying exactly the order of that quotient -- 2^(t-1), at
  every field of both signs, zero disagreements. Same order, different
  subobject, opposite verdicts; the coincidence of orders is precisely
  why the two have to be named apart. At
  D > 0 the same POOLED split gives 1.0594 against 1.0802 and 1.0625
  against 1.0481: inside the 0.05 band, which is what makes the pooled
  reading say the effect is one sign's. K6 says it is not.

  **AND THE FAMILY EFFECT IS A BOTTOM-OF-RANGE ONE** (K5, post-hoc).
  Pooled over m, the imaginary ambiguous mean runs 0.9014, 0.9921, 1.0158
  over the three bins against 1.0430, 1.0169, 1.0050 non-ambiguous: the
  deficit is spent by the top bin. The real side pooled runs 1.0401,
  1.0218, 1.0069 against 1.0711, 1.0182, 1.0077 -- which reads as no
  deficit in any bin and is the reading K6 corrects.

  **AND THE POOLING WAS THE WHOLE OF THE SIGN DIFFERENCE** (K6, added at
  audit; it supersedes K4's and K5's real-side verdicts and nothing
  else). K4 and K5 average over (field, class) pairs drawn from
  DIFFERENT fields for the two columns, and within any field the h+
  ratios average to 1 by construction -- so a short trivial class
  inflates that field's other classes, and WHICH COLUMN RECEIVES THAT
  INFLATION is decided by a structural fact about the field that has
  nothing to do with ambiguity. There are two ways to hold only one kind
  and THEY PUSH OPPOSITE COLUMNS: a one-genus field has no non-trivial
  ambiguous class, so its whole surplus lands in the non-ambiguous
  column, while a field whose group is ENTIRELY 2-torsion has no
  non-ambiguous class and lands its whole surplus in the ambiguous one.
  The two signs do not fail the same way, and the census says so: of the
  real fields with h+ > 1, 757 are entirely 2-torsion and only 35 are
  one genus, while of the imaginary ones 273 are one genus and only 55
  entirely 2-torsion. So the real side's pooled AMBIGUOUS column is
  mostly all-2-torsion fields carrying the trivial class's surplus among
  themselves -- which is what masked the deficit there and made the
  effect look like one sign's. Only 189 real fields hold both kinds
  against 880 imaginary. Restricted to the fields holding both, where the
  two columns differ in ambiguity ALONE, the bottom-bin gap is -0.1507 on
  the real side with the ambiguous mean lower at 0.841 of fields, and
  -0.2160 imaginary with 0.777. It closes with p at both signs: -0.017
  and -0.044 in the middle bin, -0.001 and +0.015 in the top. So the
  2-torsion classes are short at small p at BOTH signs, and the deficit
  is bottom-of-range at both. **THE CLAIM IS COMPARATIVE AND ITS SCOPE IS
  THE COMPARISON'S OWN**: what is measured is the ambiguous classes
  against the NON-ambiguous ones OF THE SAME FIELD, on the fields holding
  both. It does not say a 2-torsion class is short in absolute terms, and
  in a field whose group is entirely 2-torsion it cannot -- there the
  non-trivial ambiguous classes must average ABOVE nominal, since they
  are all that is left to carry the trivial class's surplus. That is not
  a limitation of the measurement but of the question: where a field
  holds one kind only, "ambiguous against non-ambiguous" has no second
  arm, and the 757 real and 55 imaginary all-2-torsion fields are outside
  what any version of this comparison can ask. K7 BELOW IS THE READING
  THAT REACHES THEM, and it is worth keeping for exactly that: it is
  ABSOLUTE where this one is comparative, pricing the trivial class
  against 1/h+ over every field at its own h+, all-2-torsion fields
  included, and it finds the deficit deepening with the amount of
  2-torsion the group carries. Two readings of one question over
  populations that barely overlap.

  **AND THE TWO SIDES AGREE, WHICH IS NOW THE WHOLE FINDING RATHER THAN
  HALF OF ONE** (K3; first half survives, second half UNREADABLE AS
  FRAMED --
  it compares the spread of the m column across the signs, and the two
  sign's band sets are not the same set: the real side has an m = 1 band
  with no imaginary counterpart, since only an indefinite form's minimum
  can be 1 at a non-trivial class, and its top band holds 4 pairs. Over
  the bands the signs share, the real spread is 0.026 against the 0.038
  the kill wanted, and including the uncommon band it is 0.055 -- the
  verdict flips on which bands are compared, so no verdict is taken. P2
  dying at BOTH signs is what makes the comparison moot anyway). The
  trivial
  class's bottom-bin ratio differs between the signs by at most 0.021 at
  every h+ from 1 through 8 -- 0.9380 against 0.9170 at h+ = 2 and 0.6615
  against 0.6740 at h+ = 8 -- an agreement five times tighter than the
  band P3 asked for. With K6 in hand the whole picture is
  sign-independent: the 2-torsion classes are short at small p at both
  signs, the trivial class is the extreme member at both, and both
  deficits are spent by the top bin. What is NOT sign-independent is the
  only mechanism anyone has derived -- (3)'s hard zero, which exists at
  D < 0 and has no indefinite counterpart -- and the only dial tried,
  the class minimum, which grades nothing at either sign. So one effect
  with no derivation behind it, and a derivation that explains the
  extreme member of it at one sign. Those are not the same thing, and
  the first ROUND of this rig's own reading mistook a composition
  artifact for the difference between them.

  **AND THE 2-RANK GRADES THE TRIVIAL CLASS AT FIXED h+, WHICH IS THE
  FAMILY FINDING SEEN FROM ITS EXTREME MEMBER** (K7, added at audit).
  The narrow class number was the grading the pooled reading arrived at,
  |D| and the unit's norm having died to it. It is not the only one. At
  h+ = 4 the trivial class's bottom-bin ratio runs 0.8568 then 0.8059
  over t = 2, 3 on the real side and 0.8619 then 0.7963 imaginary; at
  h+ = 8 it runs 0.7340, 0.7062, 0.5988 over t = 2, 3, 4 real and 0.7038,
  0.6749, 0.5489 imaginary. Monotone in t at both signs and both strata,
  and it must be read at FIXED h+ or it is not a second cut at all --
  2^(t-1) divides h+, so the two are entangled and a t column read across
  h+ is largely h+ again. Both dials are live: at fixed t = 2 the ratio
  still falls from 0.86 to about 0.72 as h+ goes 4 to 8. This is what the
  family finding predicts from the other end, the trivial class being the
  extreme member of the 2-torsion: the more 2-torsion the group carries,
  the shorter its extreme member is. And the sign agreement TIGHTENS
  under the finer cut rather than dissolving -- the two signs sit within
  0.032 of each other at four of the five cells and 0.050 at the fifth.
  THE CONFOUND TO NAME IS |D|, since more prime discriminant factors
  means a larger discriminant and the t = 4 cells are necessarily large
  ones. It is answered by a measurement already standing rather than by a
  new cut, whose cells would be too thin to read:
  explore_principal_share.py cut the same ratio by |D| at fixed h+ = 8
  and found it FLAT across a four-fold range -- 0.662, 0.628, 0.661,
  0.687, a spread of 0.059 --
  where the t dial moves 0.734 to 0.599 at that same h+, a spread of
  0.135. A dial that is flat cannot deliver twice the motion of itself.

WHAT IS NOT CONTROLLED, stated rather than left for a reader to find: the
minimum band and the within-field pairing are never applied AT ONCE. K4
conditions on the band and pools across fields; K6 pairs within a field
and pools the bands. The gap the two leave is a within-field ambiguity
effect that is really a band effect, and what argues against it is that
K4's gap is uniform across the bands rather than carried by one -- an
argument, not a control. The combined cut would need cells thin enough
to be worth running only against a specific rival.

RUN RECORD: wall 4.1 s, 1217 imaginary and 1216 real fundamental
discriminants to |D| <= 4000 over the odd split p <= 10^4, fields with
fewer than 20 split primes dropped. Pure Python, well inside the analysis
ceiling. The class enumerations are the dominant cost and are computed
once per field. The wall is measured on the rig AS IT STANDS, C6, K6, K7
and the company census included -- all of them added during the audit,
and none of them costing a second sweep, since each re-reads the per-bin
counts the one sweep already holds.
"""

import os
import sys
import time
from collections import defaultdict

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_principal_share import (          # noqa: E402
    primes_upto, kronecker, fundamental_discriminants,
    all_reduced_forms, cycle_of, reduce_form, class_data_real,
    reduce_definite, class_number_imag, form_at, prime_discriminants,
)
from math import isqrt                          # noqa: E402

DBOUND = 4000
PCAP = 10 ** 4
BINS = ((3, 1000), (1000, 3000), (3000, PCAP))
BIN_LABELS = ("p<1000", "1k-3k", "3k-10k")
MIN_SPLIT = 20            # a field with fewer split primes carries no share
M_BANDS = ((1, 1), (2, 5), (6, 15), (16, 10 ** 9))
M_LABELS = ("m=1", "m 2-5", "m 6-15", "m>=16")


def bin_index(p):
    for i, (lo, hi) in enumerate(BINS):
        if lo <= p < hi:
            return i
    return None


def band_index(m):
    for i, (lo, hi) in enumerate(M_BANDS):
        if lo <= m <= hi:
            return i
    return None


# ------------------------------------------------- the class inventories

def classes_imag(D):
    """Every definite class of discriminant D as (reduced form) -> record.

    record = (is_trivial, minimum, is_ambiguous). The minimum of a
    definite class is its reduced form's leading coefficient; the class
    is ambiguous iff reducing the opposite form returns the form itself.
    """
    absD, a, out = -D, 1, {}
    while 3 * a * a <= absD:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (a == c and b < 0):
                continue
            f = (a, b, c)
            out[f] = None
        a += 1
    b0 = D % 2
    triv = reduce_definite((1, b0, (b0 * b0 - D) // 4), D)
    for f in out:
        a, b, c = f
        out[f] = (f == triv, a, reduce_definite((a, -b, c), D) == f)
    return out, triv


def classes_real(D):
    """Every narrow class of discriminant D as (cycle key) -> record.

    The key is the smallest reduced form in the cycle, so the key is a
    function of the class and not of the form the walk started at. The
    minimum is min |a| over the cycle; ambiguity is the opposite form
    reducing into the same cycle.
    """
    rt = isqrt(D)
    forms, seen, out, member = set(all_reduced_forms(D, rt)), set(), {}, {}
    for f in sorted(forms):
        if f in seen:
            continue
        cyc = cycle_of(f, D, rt)
        seen.update(cyc)
        key = min(cyc)
        for g in cyc:
            member[g] = key
        out[key] = cyc
    b0 = D % 2
    triv = member[reduce_form((1, b0, (b0 * b0 - D) // 4), D, rt)]
    recs = {}
    for key, cyc in out.items():
        a, b, c = key
        opp = reduce_form((a, -b, c), D, rt)
        recs[key] = (key == triv, min(abs(g[0]) for g in cyc),
                     member[opp] == key)
    return recs, member, triv, rt


# ------------------------------------------------------------- the sweep

def sweep(sign, plist):
    """Per (field, class, bin) counts plus the controls, one sign."""
    rows, c1_bad, c2_bad, c4_bad = [], 0, 0, 0
    for D in fundamental_discriminants(1, DBOUND, sign):
        if sign < 0:
            recs, triv = classes_imag(D)
            member, rt = None, None
            hplus = class_number_imag(D)
        else:
            recs, member, triv, rt = classes_real(D)
            _, hplus, _ = class_data_real(D, rt)
        if len(recs) != hplus:
            c1_bad += 1
            continue
        counts = defaultdict(lambda: [0, 0, 0])
        totals = [0, 0, 0]
        for p in plist:
            if D % p == 0 or kronecker(D, p) != 1:
                continue
            bi = bin_index(p)
            if bi is None:
                continue
            b = form_at(D, p)
            num = b * b - D
            if sign < 0:
                key = reduce_definite((p, b, num // (4 * p)), D)
                if key == triv and 4 * p < -D:
                    c4_bad += 1
            else:
                key = member[reduce_form((p, b, num // (4 * p)), D, rt)]
            counts[key][bi] += 1
            totals[bi] += 1
        if sum(totals) < MIN_SPLIT:
            continue
        if sum(sum(v) for v in counts.values()) != sum(totals):
            c2_bad += 1
            continue
        rows.append((D, hplus, recs, dict(counts), tuple(totals)))
    return rows, c1_bad, c2_bad, c4_bad


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def ratio(cnt, total, hplus):
    """A class's share in one bin, against the nominal 1/h+."""
    return cnt * hplus / total


def trivial_by_h(rows, bi):
    """C3/K3: mean trivial-class ratio per h+, one bin. Over FIELDS."""
    acc = defaultdict(list)
    for D, hplus, recs, counts, totals in rows:
        if totals[bi] == 0 or hplus > 8:
            continue
        triv = [k for k, r in recs.items() if r[0]][0]
        acc[hplus].append(ratio(counts.get(triv, [0, 0, 0])[bi],
                                totals[bi], hplus))
    return {h: (mean(v), len(v)) for h, v in sorted(acc.items())}


def by_band(rows, bi, want_trivial=False, split_ambiguous=False):
    """K2/K4: mean ratio per minimum band, over (field, class) PAIRS."""
    acc = defaultdict(list)
    for D, hplus, recs, counts, totals in rows:
        if totals[bi] == 0 or hplus == 1:
            continue
        for key, (is_triv, m, amb) in recs.items():
            if is_triv != want_trivial:
                continue
            bd = band_index(m)
            tag = (bd, amb) if split_ambiguous else bd
            acc[tag].append(ratio(counts.get(key, [0, 0, 0])[bi],
                                  totals[bi], hplus))
    return {t: (mean(v), len(v)) for t, v in sorted(acc.items())}


def trivial_rank(rows, bi, occupancy=0):
    """K1: how often the trivial class holds the field's minimum ratio.

    THE ZERO-TIE CONTROL. A field whose bin holds few split primes leaves
    most of its classes empty, so the trivial class ties at zero with them
    and scores a WEAK minimum on no merit at all -- and at D < 0 the
    trivial class is empty below |D|/4 by construction (C4), which makes
    that tie systematically likelier at one sign. Both readings are
    therefore reported: the raw one, and the one restricted to fields with
    at least `occupancy` split primes per class in the bin, where an empty
    class is a measurement rather than a shortage. The count of weak hits
    that are ties AT ZERO is printed beside them, since that is the
    quantity the uncontrolled reading cannot separate.
    """
    fields = weak = strict = atzero = 0
    for D, hplus, recs, counts, totals in rows:
        if hplus == 1 or totals[bi] == 0:
            continue
        if totals[bi] < occupancy * hplus:
            continue
        fields += 1
        rs = {k: ratio(counts.get(k, [0, 0, 0])[bi], totals[bi], hplus)
              for k in recs}
        triv = [k for k, r in recs.items() if r[0]][0]
        lo = min(rs.values())
        if rs[triv] <= lo:
            weak += 1
            if sum(1 for v in rs.values() if v <= lo) == 1:
                strict += 1
            elif lo == 0.0:
                atzero += 1
    return fields, weak, strict, atzero


def main():
    t0 = time.time()
    plist = primes_upto(PCAP)
    print("population: |D| <= %d both signs, odd split p <= %d, bins %s"
          % (DBOUND, PCAP, " ".join(BIN_LABELS)))
    out = {}
    for sign, name in ((-1, "imaginary"), (+1, "real")):
        rows, c1, c2, c4 = sweep(sign, plist)
        out[sign] = rows
        print("\n%s: %d fields kept; C1 class-count failures %d; "
              "C2 partition failures %d; C4 trivial-below-|D|/4 %s"
              % (name, len(rows), c1, c2, c4 if sign < 0 else "n/a"))

    print("\n--- C6 (added at audit): the ambiguous classes number 2^(t-1),"
          "\n    which is the GENUS COUNT -- printed because the deficit"
          "\n    below lands on a subgroup of the order of a quotient this"
          "\n    corpus has already cleared, and the two must not be read"
          "\n    as one object")
    for sign, name in ((-1, "imaginary"), (+1, "real")):
        bad = 0
        for D, hplus, recs, counts, totals in out[sign]:
            t = len(prime_discriminants(D))
            if sum(1 for r in recs.values() if r[2]) != 2 ** (t - 1):
                bad += 1
        print("  %-10s fields %4d   disagreements %d"
              % (name, len(out[sign]), bad))

    print("\n--- C3 + K3: trivial-class ratio to nominal, by h+ and bin")
    print("%-4s | %-24s | %-24s" % ("h+", "real (n)", "imaginary (n)"))
    for bi, lab in enumerate(BIN_LABELS):
        r, i = trivial_by_h(out[+1], bi), trivial_by_h(out[-1], bi)
        print("  bin %s" % lab)
        for h in sorted(set(r) | set(i)):
            rv = "%.4f (%d)" % r[h] if h in r else "--"
            iv = "%.4f (%d)" % i[h] if h in i else "--"
            gap = ("%+.4f" % (r[h][0] - i[h][0])) if h in r and h in i else ""
            print("%-4d | %-24s | %-24s %s" % (h, rv, iv, gap))

    print("\n--- K1: is the trivial class the field's minimum in bin 0")
    for occ in (0, 4):
        print("  occupancy >= %d split primes per class in the bin"
              % occ if occ else "  raw, no occupancy control")
        for sign, name in ((-1, "imaginary"), (+1, "real")):
            f, w, s, z = trivial_rank(out[sign], 0, occ)
            print("  %-10s fields %4d   min: %4d (%.3f)   strictly: %4d "
                  "(%.3f)   weak hits tied AT ZERO: %4d"
                  % (name, f, w, w / f if f else 0, s, s / f if f else 0, z))
    print("  and the COMPANY the trivial class has, which is the obvious"
          "\n  deflation of any gap between those strict rates -- a class is"
          "\n  harder to isolate at the bottom where more classes are short:")
    for sign, name in ((-1, "imaginary"), (+1, "real")):
        comp = [sum(1 for r in recs.values() if r[2] and not r[0])
                for D, hplus, recs, c, t in out[sign] if hplus > 1]
        print("  %-10s mean NON-TRIVIAL ambiguous classes per field with "
              "h+ > 1: %.2f  (on %d fields)" % (name, mean(comp), len(comp)))

    print("\n--- K2: ratio by class minimum m(C), bin 0, NON-trivial classes")
    print("%-8s | %-22s | %-22s" % ("band", "real (pairs)", "imag (pairs)"))
    br, bi_ = by_band(out[+1], 0), by_band(out[-1], 0)
    for j, lab in enumerate(M_LABELS):
        rv = "%.4f (%d)" % br[j] if j in br else "--"
        iv = "%.4f (%d)" % bi_[j] if j in bi_ else "--"
        print("%-8s | %-22s | %-22s" % (lab, rv, iv))

    print("\n--- K4: ambiguous vs not, inside each band, bin 0, non-trivial")
    print("%-8s | %-18s %-18s | %-18s %-18s"
          % ("band", "real amb", "real non", "imag amb", "imag non"))
    ar, ai = (by_band(out[+1], 0, split_ambiguous=True),
              by_band(out[-1], 0, split_ambiguous=True))
    for j, lab in enumerate(M_LABELS):
        cells = []
        for tbl in (ar, ai):
            for flag in (True, False):
                cells.append("%.4f (%d)" % tbl[(j, flag)]
                             if (j, flag) in tbl else "--")
        print("%-8s | %-18s %-18s | %-18s %-18s" % (lab, *cells))

    print("\n--- K5 (frozen AFTER K4 printed, post-hoc): the ambiguous"
          "\n    deficit across the bins, non-trivial classes, m pooled")
    print("%-8s | %-20s %-20s | %-20s %-20s"
          % ("bin", "real amb", "real non", "imag amb", "imag non"))
    for bi, lab in enumerate(BIN_LABELS):
        cells = []
        for sign in (+1, -1):
            acc = {True: [], False: []}
            for D, hplus, recs, counts, totals in out[sign]:
                if totals[bi] == 0 or hplus == 1:
                    continue
                for key, (is_triv, m, amb) in recs.items():
                    if is_triv:
                        continue
                    acc[amb].append(ratio(counts.get(key, [0, 0, 0])[bi],
                                          totals[bi], hplus))
            for flag in (True, False):
                cells.append("%.4f (%d)" % (mean(acc[flag]), len(acc[flag])))
        print("%-8s | %-20s %-20s | %-20s %-20s" % (lab, *cells))

    print("\n--- K6 (added at audit): the ambiguity split WITHIN a field."
          "\n    K4 and K5 pool across fields, and within any field the h+"
          "\n    ratios average to 1 by construction, so a short trivial"
          "\n    class inflates that field's OTHER classes -- entirely into"
          "\n    the non-ambiguous column at a one-genus field, which has no"
          "\n    non-trivial ambiguous class to take any of it. Restricted"
          "\n    to fields holding BOTH kinds, which is the only population"
          "\n    where the two differ in ambiguity alone. The census of WHY"
          "\n    a field fails to hold both is printed first, because the"
          "\n    two failure modes push opposite columns and the signs do"
          "\n    not fail the same way.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        a = b = c = 0
        for D, hplus, recs, counts, totals in out[sign]:
            if hplus == 1:
                continue
            amb = sum(1 for r in recs.values() if r[2] and not r[0])
            non = sum(1 for r in recs.values() if not r[2])
            if amb and non:
                c += 1
            elif not amb:
                a += 1
            else:
                b += 1
        print("  %-5s h+>1 fields %4d | one genus, no non-trivial ambiguous"
              " %4d | ENTIRELY 2-torsion %4d | both kinds %4d"
              % (name, a + b + c, a, b, c))
    for bi, lab in enumerate(BIN_LABELS):
        cells = []
        for sign in (+1, -1):
            diffs = []
            for D, hplus, recs, counts, totals in out[sign]:
                if totals[bi] == 0 or hplus == 1:
                    continue
                grp = {True: [], False: []}
                for key, (is_triv, m, amb) in recs.items():
                    if is_triv:
                        continue
                    grp[amb].append(ratio(counts.get(key, [0, 0, 0])[bi],
                                          totals[bi], hplus))
                if grp[True] and grp[False]:
                    diffs.append(mean(grp[True]) - mean(grp[False]))
            below = sum(1 for d in diffs if d < 0)
            cells.append("%+.4f on %d fields, amb lower at %.3f"
                         % (mean(diffs), len(diffs),
                            below / len(diffs) if diffs else 0))
        print("  %-8s real: %-44s\n           imag: %s"
              % (lab, cells[0], cells[1]))

    print("\n--- K7 (added at audit): the trivial class's own deficit by"
          "\n    2-RANK at FIXED h+. If the 2-torsion is the short family,"
          "\n    then how MUCH 2-torsion a group has should grade its"
          "\n    extreme member -- and t must be held against h+, not read"
          "\n    across it, since 2^(t-1) divides h+ and the two would"
          "\n    otherwise be the same cut twice.")
    for hfix in (4, 8):
        for sign, name in ((+1, "real"), (-1, "imag")):
            acc = defaultdict(list)
            for D, hplus, recs, counts, totals in out[sign]:
                if totals[0] == 0 or hplus != hfix:
                    continue
                triv = [k for k, r in recs.items() if r[0]][0]
                acc[len(prime_discriminants(D))].append(
                    ratio(counts.get(triv, [0, 0, 0])[0], totals[0], hplus))
            cells = "  ".join("t=%d: %.4f (%d)" % (t, mean(v), len(v))
                              for t, v in sorted(acc.items()))
            print("  h+ = %d  %-5s %s" % (hfix, name, cells))

    print("\nwall %.1f s" % (time.time() - t0))
    return out


if __name__ == "__main__":
    main()
