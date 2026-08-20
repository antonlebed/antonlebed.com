r"""WHAT CARRIES THE TOP-BAND PERSISTENCE -- THE FORM, OR THE UNIT RANK?
-- the two generator ceilings separate in the band 630 <= p < 1000
(explore_ceiling_topband.py F1: imaginary quadratic 1.0426 +- 0.0101
against complex cubic 0.9780 +- 0.0123, +4.05 joint sigma), and the two
populations differ in TWO variables at once: the imaginary field's
places live in a definite binary form with its hard zero, and its unit
rank is 0 against the cubic's 1. The carrier is open, and one
population discriminates: REAL QUADRATIC, rank 1 like the complex
cubics but WITH a form. This file reads the generator ceiling
over that population with the frozen curve machinery, cut ladder and
band unchanged.

WHAT RIDES ON THE ANSWER. If the real quadratic top band sits above 1
where the cubic sits at it, persistence follows the FORM: the surplus
belongs to the binary-form structure a quadratic place carries and a
cubic degree-1 place lacks, definite or not. If the real quadratic top
band is consistent with 1, persistence follows the RANK: a fundamental
unit is what exhausts the surplus, and the imaginary field keeps it
because it alone has no unit to pay with. Either way one confounded
mechanism dies; a middle reading (separated from both comparators) says
the pair was never the right axis and is worth knowing at the same
price.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 EVERYTHING RIDES IN. The real quadratic sweep -- enumeration,
    indefinite reduction, narrow classes, composition, orders, the
    parents' own identity/commutativity/associativity probes and the
    order-vs-ambiguous cross-check -- is explore_class_order.py's
    sweep(+1), whose machinery explore_class_share.py and
    explore_principal_share.py built and pinned. The population build,
    admissibility, frozen-strata rule, stratum cells, curve, excess and
    band estimators, the identity checks and both synthetic controls
    are explore_ceiling_curve.py's, imported as functions. Nothing is
    re-implemented.

 T2 THE LADDER, THE BAND AND THE FLOORS DO NOT MOVE. Cuts (250, 400,
    630, 1000), extension cuts (2500, 10^4), bands, MIN_CELL = 30,
    MIN_SPLIT = 20, MINSTRAT = 30 are the parents' constants read from
    their modules; a moved dial would re-pose the question instead of
    re-asking it at the new sign.

 T3 ONE MODULE CONSTANT IS WIDENED FOR ONE CALL, AND CHECKED. The
    sweep's enumeration bound is CO.DBOUND = 4000, a module global read
    at call time. The real sweep runs with it set to DBOUND_REAL and
    the imaginary sweep with it restored to the parent's 4000; the rig
    asserts the restored value AND pins the imaginary output to the
    parent's own printed figures (C3), so a leaked bound cannot pass.

 T4 THE GROUP IS A DIAL THAT EXISTS ONLY AT THIS SIGN, so the choice
    could carry the verdict silently. At D < 0 the narrow and wide
    groups coincide, and a complex cubic field has only its ideal
    class group; a real quadratic field is the one population where
    forms grade the NARROW group Cl+ while ideals grade its quotient
    Cl. Both parents' vocabulary transplants ambiguously. The rig
    therefore reads BOTH views on ONE frozen population: primary the
    narrow view (the form vocabulary, and the group the degree-2
    parents' own sweeps grade at both signs), the wide view printed
    beside it through the quotient by the class of (-1, b0, -c0),
    which is trivial exactly at negative Pell (N(eps) = -1,
    explore_principal_share.py::class_data_real) and order 2
    otherwise. If the two views' top bands agree, the choice carries
    nothing; if they differ, that difference is itself a reading (the
    two groups differ by exactly one unit-sign bit, so a view split
    would locate the mechanism at the units with no further rig).

 T5 THE AGREEMENT DISCIPLINE MAPS, IT DOES NOT COPY. The cubic parent's
    two-rung harvest agreement guarded a relation engine this side does
    not run: degree-2 class data comes from complete enumeration of
    reduced forms, not from a harvest that can stop early. The rungs
    here are the parents' own: the composition table is checked against
    the form-symmetry ambiguity count computed without composition
    (CO.sweep's c2 gate), the group law is probed per field, and the
    whole imaginary pipeline must reprint the parent's frozen figures
    before the real numbers are read (C3) -- reproduction standing
    where a second harvest rung would.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) DBOUND_REAL IS CHOSEN BY POPULATION ARITHMETIC, NOT BY THE
      PHENOMENON. A scratch enumeration run before this freeze (2-rank
      proxy for cyclicity, split places below 1000) counted admissible real
      quadratic fields and top-band generator expectations by bound:
      at 4000, 132 fields across every composite stratum, with
      expectations 752 / 355 / 190 at h+ = 4 / 6 / 8; at 16000, 618
      such fields, of which 524 sit in h+ = 4 / 6 / 8 / 10 with
      expectations 3142 / 1472 / 837 / 660. The imaginary comparator's top-band
      bar is +-0.0101; matching it needs the summed expectation near
      16000's, and the sweep there measured 1.8 s of enumeration --
      so DBOUND_REAL = 16000, the parent's own move (widen the
      population to halve the bar) at the parent's own precision. The
      caps then differ across the compared populations, as they
      already do at degree 3 (24000) against imaginary (4000): the
      level is a ratio to its own population's expectation with
      nominal 1 by equidistribution at every cap, so the cap moves
      power and the field MIX, not the nominal -- and the mix is what
      the frozen-strata rule plus the per-stratum cells printed at
      every point keep readable.

  (2) THE NOMINAL IS 1 IN BOTH VIEWS. Split primes equidistribute over
      the narrow classes (Chebotarev for the narrow class field, the
      ray class field with modulus the infinite places) and over the
      wide classes (the Hilbert class field); the generator cell's
      expectation is tot * phi(h)/h in the group read. The square-root
      choice at each p lands the place in C or C^-1; every statistic
      read here is invariant under that choice in both views (orders
      match, cosets map to inverse cosets of the same order), by the
      degree-2 parent's own derivation (3).

  (3) THE WIDE VIEW'S QUOTIENT, checked rather than trusted. For a
      field with cyclic Cl+ and N(eps) = +1, Cl = Cl+/<j> with j the
      class of the reduced (-1, b0, -c0): the rig recomputes classes
      (member, rt), asserts ord(j) <= 2 and [j trivial <=> N(eps) =
      -1], forms cosets by composition, asserts the coset count equals
      class_data_real's wide h at every field, and takes the wide
      order of a class as the least n with C^n in <j> -- walked with
      the same composer, bounded by ord(C). A quotient of a cyclic
      group is cyclic, so the wide profile check (C2) must pass
      identically; its failure would indict the quotient code, not the
      field. At N(eps) = +1 an h+ = 4 field lands at wide h = 2, a
      forced stratum: the wide view is strictly weaker-powered by
      construction, which is priced, not fixed -- it is a consistency
      view, and no verdict rides on it alone.

  (4) THE STATISTIC'S ALGEBRA rides in unchanged: cumulative
      denominators floored by the freeze at the smallest cut, band
      denominators pooled-only with the dispersion scale measured at
      the band, nested cumulative points compared pointwise and never
      chi-squared across cuts. One new place it DOES blow up, caught
      by the first run's crash rather than by this paragraph's first
      draft, which claimed no new denominator reaches zero: an h+ = 2
      field with N(eps) = +1 quotients to the TRIVIAL wide group, and
      the per-field excess ratio divides by h - 1 = 0. The cure is
      the parent's own h = 1 rule (build_pop2 drops such fields,
      having no cell to read): the wide build skips them and prints
      the count. Wide h = 2 is fine (h - 1 = 1) and prime, so the
      composite filter keeps it off every curve.

  (5) THE COMPARATORS. The imaginary side is RECOMPUTED in-rig at the
      parent's bound through the identical estimator path, so the
      form-population comparison is same-estimator by construction and
      C3 pins it to the parent's frozen prints (top band 1.0426 +-
      0.0101, cut 1000 raw 1.0875, cut 10^4 raw 1.0240). The cubic
      side cannot ride in at this price; its top band enters as the
      frozen constant 0.9780 +- 0.0123 quoted from
      explore_ceiling_topband.py F1's print, and every z against it
      says so.

THE PREDICTIONS, fixed before the engine ran. Kills name what the rig
PRINTS; the meaning is weighed after.

 P1 THE REAL CEILING DECAYS: the four cumulative narrow-view levels at
    cuts 250 to 1000 are strictly decreasing, each above 1, and the
    extension continues below the cut-1000 value, as at every
    population read so far.

 P2 THE QUESTION, three printed z's on the narrow top band L +- s:
    z1 = (L - 1)/s, z2 against the in-rig imaginary top band (joint),
    z3 against the frozen cubic 0.9780 +- 0.0123 (joint). FORM-carried
    reads z1 >= +3 with |z2| < 3; RANK-carried reads |z1| < 3 with
    z2 <= -3. Any other sign pattern is the middle reading and is
    reported as what it is.

 P3 THE VIEWS AGREE: narrow and wide top-band levels within 3 joint
    sigma, the N(eps) = +1 field count printed beside (the check has
    content only there; if it FAILS, T4's last clause is the reading
    and the failure ships as a finding, not a bug).

 P4 ROBUSTNESS: MIN_SPLIT 20 -> 30 and DBOUND_REAL 16000 -> 8000
    re-reads move no P2 z across its own verdict line; per-field and
    pooled levels agree to within 0.01 at every readable stratum-cut.
    [Post-first-print amendment, flagged as such: the 30-floor
    register came back EMPTY -- 82 fields and no readable stratum,
    because the population's expected split count below 250 is about
    27, so a floor of 30 sits above the supply's own mean; a fact the
    hand-attack should have priced and did not. The 30 print stands
    as the record and a 25-floor probe runs beside it as the working
    re-read.]

 P5 THE TRIVIAL COLUMN HAS NO HARD ZERO AT D > 0: the real trivial
    level at cut 250 prints ABOVE the imaginary one at the same cut
    (whose depth is the derived |D|/4 zero's), and its fall to 10^4 is
    printed against the imaginary factor-8 fall for the tail reading.

THE CHECKS.

 C1 the sum and forced identities at every view and cut (imported,
    runs inside every read_curve call).
 C2 cyclic profile in the wide view at every N(eps) = +1 field, and
    coset count == class_data_real's h everywhere.
 C3 the reproduction anchor: the imaginary pipeline at the parent's
    bound reprints the three frozen figures of derivation (5) to the
    printed precision (5e-5), before any real number is read.
 C4 uniform synthetic on the real population reads 1 within the
    parent's 0.08 at both ladder ends, both views.
 C5 planted synthetic on the real population recovers the plant within
    the parent's tolerances (0.06 at the smallest cut, non-increasing
    within 0.02, top band within 0.06).

THE FINDINGS.

 F1 THE PERSISTENCE FOLLOWS THE FORM, NOT THE UNIT RANK (observation;
    2086 admissible real quadratic fields to D <= 16000, 524 in the
    readable strata h+ = 4, 6, 8, 10). The real quadratic top band
    reads 1.0613 +- 0.0069: z1 = +8.84 above 1, z2 = +1.52 against
    the in-rig imaginary 1.0426 +- 0.0101, z3 = +5.90 against the
    frozen cubic 0.9780 +- 0.0123 -- P2's form pattern exactly as
    frozen (z1 >= +3 with |z2| < 3). A population with the complex
    cubics' own unit rank keeps its top-band surplus at full size, so
    a fundamental unit is not what exhausts the cubic surplus, and
    the fracture line runs between quadratic places and cubic places,
    not between rank 0 and rank 1.

 F2 AND NOT THE HARD ZERO EITHER (observation). The real trivial
    column at cut 250 reads 0.8893 against the imaginary 0.1519 --
    the derived |D|/4 zero is absent at D > 0, as it must be for an
    indefinite form -- and the top-band surplus persists anyway, at a
    point estimate ABOVE the definite population's. The confounded
    axis "the form, with its hard zero" therefore splits:
    the hard zero is a definite-form accident the persistence never
    needed, and what carries it is the quadratic place itself --
    whatever of the binary form's arithmetic survives losing both the
    minimum and the rank-0 unit group. (Settled 2026-08-20,
    explore_ceiling_squares.py: the surplus is the explicit formula's
    prime-power term, removed exactly on the imaginary side and to
    three quarters here; it is carried by any population whose
    Frobenius class is a square in its Galois group, the quadratic
    place being one such. This file's measurements stand as the
    record of what was to be explained.)

 F3 THE TWO SIGNS' CEILINGS AGREE AT BOTH ENDS OF THE LADDER AND PART
    IN THE MIDDLE (observation). Real: 1.1867, 1.1654, 1.1247, 1.1041
    over the shared cuts, then 1.0606 and 1.0246 on the extension;
    imaginary: 1.1926, 1.1551, 1.1095, 1.0875, then 1.0569 and
    1.0240. Everywhere within 0.017 in absolute terms, but the
    pointwise joint z's, computed from those printed pairs, run -0.6,
    +1.5, +2.7, +3.7 along the shared cuts and +1.3, +0.4 on the
    extension: agreement at the smallest cut and at the tail (10^4
    raw z +0.4; excesses 0.0110 +- 0.0009 against 0.0115 +- 0.0012,
    z +0.3), with the real side ABOVE through the middle cuts --
    and the cumulative points are nested, so that mid-ladder run is
    one correlated fact and not three. Across disjoint strata sets
    (4-10 against 6-14), caps (16000 against 4000) and signs, what is
    measured is two close but not coincident curves meeting at the
    ends of the range; a first draft of this finding said "one
    degree-2 law, read twice", which is the shape-claim the printed
    pairs refuse at cut 1000.

 F4 THE GROUP CHOICE CARRIES NOTHING (observation). The wide view's
    top band reads 1.0855 +- 0.0118 over strata h = 4, 6 (the band's
    dispersion scale measured on 146 fields, those with band
    expectation >= 5), narrow - wide joint z = -1.77: the surplus persists
    in the ideal group as in the form group. The view is
    weaker-powered by construction -- 1133 of the frozen population's
    h+ = 2 fields quotient to the trivial wide group and leave, and
    N(eps) = +1 holds at 1518 of 2086 fields.

THE PREDICTIONS, WEIGHED.

 P1 PASSES: 1.1867 > 1.1654 > 1.1247 > 1.1041, all above 1, and the
    extension falls on through 1.0606 to 1.0246.
 P2 the FORM pattern fires as frozen: z1 = +8.84, z2 = +1.52,
    z3 = +5.90.
 P3 PASSES: |z| = 1.77.
 P4 the 30-floor register came back empty as the amended slate
    records; the 25-floor re-read gives 1.0653 +- 0.0087 (z1 +7.52)
    and the half-bound 1.0512 +- 0.0097 (z1 +5.29) -- no z crosses a
    verdict line; per-field vs pooled gap 0.0035.
 P5 PASSES: 0.8893 against 0.1519 at cut 250; the tail prints 0.9756
    against 0.9012 at 10^4, both columns closing toward 1 with the
    imaginary one climbing out of its zero.

RUN RECORD. 2026-08-18, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_ceiling_realquad.py`.
One process, CPython, no BLAS. 8186 checks passed (the per-field wide
quotient checks dominate the count), 16.8 s wall, peak working set
295.4 MB. The first complete run peaked at 531 MB and was killed at
the 512 ceiling with every science print already emitted; the fix
drops each sweep's rows once its population is built, and the numbers
above are the clean run's, which reproduced the killed run's prints
digit for digit.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from collections import defaultdict
from math import isqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_ceiling_curve as CV
import explore_class_order as CO
from explore_class_share import classes_real
from explore_principal_share import (
    primes_upto, reduce_form, class_data_real,
)

CHECKS = 0

DBOUND_REAL = 16000               # derivation (1)
DBOUND_HALF = 8000                # P4's re-read
DEG3_TOP = (0.9780, 0.0123)       # frozen, explore_ceiling_topband F1
IMAG_TOP = (1.0426, 0.0101)       # frozen, explore_ceiling_curve F5
IMAG_CUT1000 = 1.0875             # frozen, explore_ceiling_curve P5
IMAG_CUT10K = 1.0240              # frozen, explore_ceiling_curve P5
CUTS = CV.CUTS
EXT_CUTS = CV.EXT_CUTS
BANDS = CV.BANDS
TOPBAND = BANDS[-1]


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise SystemExit("FAIL: " + msg)


def section(t):
    print("\n== " + t + " ==")


def run_sweep(sign, bound, plist):
    """CO.sweep with the module bound set for the call (T3)."""
    old = CO.DBOUND
    CO.DBOUND = bound
    try:
        return CO.sweep(sign, plist)
    finally:
        CO.DBOUND = old


def frozen_fields(rows):
    """rows -> [(D, field)] surviving the parents' full frozen chain:
    h > 1, admissibility (place floor + cyclic profile), stratum field
    floor. Keeps D so the wide view can rebuild classes (T4)."""
    keyed = []
    for r in rows:
        for f in CV.build_pop2([r]):
            if CV.admissible([f], CUTS[0], CO.MIN_SPLIT):
                keyed.append((r[0], f))
    cnt = defaultdict(int)
    for (D, f) in keyed:
        cnt[f[0]] += 1
    return [(D, f) for (D, f) in keyed if cnt[f[0]] >= CV.MINSTRAT]


def build_wide(keyed):
    """The wide view of the SAME fields, derivation (3). Returns
    (wide fields, n_plus)."""
    out, n_plus, n_h1 = [], 0, 0
    for (D, (hplus, classes, places)) in keyed:
        recs, member, triv, rt = classes_real(D)
        h, hp2, neps = class_data_real(D, rt)
        ok(hp2 == hplus, "D=%d: h+ mismatch %d vs %d" % (D, hp2, hplus))
        b0 = D % 2
        c0 = (b0 * b0 - D) // 4
        j = member[reduce_form((-1, b0, -c0), D, rt)]
        bad = [0, 0, 0, 0]
        comp = CO.make_composer(D, +1, recs, member, rt, bad)
        orders = dict(classes)
        ok(orders[j] <= 2, "D=%d: j has order %d" % (D, orders[j]))
        ok((j == triv) == (neps == -1),
           "D=%d: j-trivial vs N(eps) disagree" % D)
        if neps == +1:
            n_plus += 1
        if h == 1:
            n_h1 += 1
            continue
        sub = {triv, j}
        coset, worder = {}, {}
        for key in recs:
            part = comp(key, j)
            ck = min(key, part)
            coset[key] = ck
            if ck not in worder:
                acc, n = key, 1
                while acc not in sub:
                    acc = comp(acc, key)
                    n += 1
                worder[ck] = n
        wide_classes = sorted(set(
            (coset[k], worder[coset[k]]) for k in recs))
        ok(len(wide_classes) == h,
           "D=%d: %d cosets against wide h %d"
           % (D, len(wide_classes), h))
        ok(CV.cyclic_profile(h, wide_classes),
           "D=%d: wide profile not cyclic" % D)
        wide_places = sorted((p, coset[k]) for (p, k) in places)
        out.append((h, wide_classes, wide_places))
    print("  wide h = 1 fields dropped (no cell to read): %d" % n_h1)
    return out, n_plus


def strata_pipeline(fields, tag):
    """The parents' stratum floors on an already-admissible set."""
    cnt = defaultdict(int)
    for f in fields:
        cnt[f[0]] += 1
    kept = [f for f in fields if cnt[f[0]] >= CV.MINSTRAT]
    cum, band = CV.frozen_strata(kept, CUTS, BANDS)
    cum = [h for h in cum if CV.is_composite(h)]
    band = [h for h in band if CV.is_composite(h)]
    print("  %s: %d fields, cumulative strata %s, band strata %s"
          % (tag, len(kept), cum, band))
    return kept, cum, band


def band_point(fields, keep, lo, hi):
    strata = CV.stratum_cells(fields, lo, hi)
    scale, nsc = CV.within_scale(strata, keep)
    mu, se, pts = CV.curve_point(strata, keep, scale)
    return mu, se, pts, scale, nsc


def trivial_level(fields, lo, hi):
    """Pooled trivial-class level over lo <= p < hi, all strata."""
    obs, exp = 0, 0.0
    for f in fields:
        tot, cnt = CV.field_counts(f, lo, hi)
        if tot == 0:
            continue
        obs += cnt.get(1, 0)
        exp += tot / float(f[0])
    return obs / exp if exp else float("nan")


def main():
    t0 = time.time()

    section("C3  THE REPRODUCTION ANCHOR (imaginary, the parent's own"
            " bound)")
    plist = primes_upto(CO.PCAP)
    rows_i, bad, id_bad, c2_bad, c4_bad, law_bad = run_sweep(
        -1, 4000, plist)
    ok(CO.DBOUND == 4000, "the module bound did not restore")
    print("  sweep: %d fields, composition failures %s, identity %d,"
          " order-vs-ambiguous %d, minimum %d, law %s"
          % (len(rows_i), bad, id_bad, c2_bad, c4_bad, law_bad))
    ok(bad[2] == 0 and bad[3] == 0, "the imaginary order walk failed")
    pop_i = CV.build_pop2(rows_i)
    f_i = CV.admissible(pop_i, CUTS[0], CO.MIN_SPLIT)
    f_i, keep_i, keep_ib = strata_pipeline(f_i, "imaginary")
    del rows_i, pop_i        # the sweep rows double every place tuple's
    # list; the first run peaked at 531 MB and was killed at the 512
    # ceiling, so each rows list is dropped once its population stands
    c_i = CV.read_curve(f_i, keep_i, CUTS + EXT_CUTS, "imag")
    mu_it, se_it, _, _, _ = band_point(f_i, keep_ib, *TOPBAND)
    print("  imag band %d-%d  raw %.4f +- %.4f"
          % (TOPBAND[0], TOPBAND[1], mu_it, se_it))
    ok(abs(c_i[1000][0] - IMAG_CUT1000) < 5e-5,
       "cut-1000 reprint off: %.4f" % c_i[1000][0])
    ok(abs(c_i[10000][0] - IMAG_CUT10K) < 5e-5,
       "cut-10^4 reprint off: %.4f" % c_i[10000][0])
    ok(abs(mu_it - IMAG_TOP[0]) < 5e-5 and abs(se_it - IMAG_TOP[1]) < 5e-5,
       "top-band reprint off: %.4f +- %.4f" % (mu_it, se_it))
    print("  C3: three frozen figures reprint to 5e-5")

    section("THE REAL QUADRATIC POPULATION (sweep at DBOUND_REAL,"
            " T3)")
    rows_r, bad, id_bad, c2_bad, c4_bad, law_bad = run_sweep(
        +1, DBOUND_REAL, plist)
    ok(CO.DBOUND == 4000, "the module bound did not restore")
    print("  sweep: %d fields, composition failures %s, identity %d,"
          " order-vs-ambiguous %d, minimum %d, law %s"
          % (len(rows_r), bad, id_bad, c2_bad, c4_bad, law_bad))
    ok(bad[2] == 0 and bad[3] == 0, "the real order walk failed")
    ok(max(r[0] for r in rows_r) > 4000,
       "no real field past the parent bound: the widening leaked")
    keyed = frozen_fields(rows_r)
    del rows_r               # same 512-ceiling cure as the imaginary side
    f_r = [f for (D, f) in keyed]
    f_r, keep_r, keep_rb = strata_pipeline(f_r, "real narrow")

    section("THE NARROW CURVE (P1, C1)")
    c_r = CV.read_curve(f_r, keep_r, CUTS + EXT_CUTS, "real")
    lv = [c_r[c][0] for c in CUTS]
    ok(all(lv[i] > lv[i + 1] for i in range(3)),
       "P1: the cumulative levels are not strictly decreasing: %s" % lv)
    ok(all(v > 1 for v in lv), "P1: a cumulative level at or below 1")
    ok(c_r[10000][0] < c_r[1000][0],
       "P1: the extension does not continue the fall")

    section("THE TOP BAND (P2)")
    mu_r, se_r, pts, scale, nsc = band_point(f_r, keep_rb, *TOPBAND)
    cells = "  ".join("h=%d %.3f+-%.3f" % t for t in pts)
    print("  real band %d-%d  raw %.4f +- %.4f  (scale %.3f/%d)  %s"
          % (TOPBAND[0], TOPBAND[1], mu_r, se_r, scale, nsc, cells))
    z1 = (mu_r - 1.0) / se_r
    z2 = CV.zdiff((mu_r, se_r), (mu_it, se_it))
    z3 = CV.zdiff((mu_r, se_r), DEG3_TOP)
    print("  z1 (vs 1)         = %+.2f" % z1)
    print("  z2 (vs imaginary) = %+.2f   [imag %.4f +- %.4f in-rig]"
          % (z2, mu_it, se_it))
    print("  z3 (vs cubic)     = %+.2f   [deg3 %.4f +- %.4f frozen]"
          % (z3, DEG3_TOP[0], DEG3_TOP[1]))

    section("THE WIDE VIEW (P3, C2, derivation (3))")
    wide, n_plus = build_wide(keyed)
    print("  N(eps) = +1 at %d of %d fields (the views differ only"
          " there)" % (n_plus, len(keyed)))
    f_w, keep_w, keep_wb = strata_pipeline(wide, "real wide")
    if keep_wb:
        mu_w, se_w, ptsw, scw, nscw = band_point(f_w, keep_wb, *TOPBAND)
        cellsw = "  ".join("h=%d %.3f+-%.3f" % t for t in ptsw)
        print("  wide band %d-%d  raw %.4f +- %.4f  (scale %.3f/%d)  %s"
              % (TOPBAND[0], TOPBAND[1], mu_w, se_w, scw, nscw, cellsw))
        zv = CV.zdiff((mu_r, se_r), (mu_w, se_w))
        print("  narrow - wide joint z = %+.2f" % zv)
    else:
        print("  no readable wide band stratum")

    section("P4  THE FLOOR AND THE BOUND")
    for floor in (30, 25):
        f_rf = CV.admissible([f for (D, f) in keyed], CUTS[0], floor)
        f_rf, kf, kfb = strata_pipeline(f_rf, "MIN_SPLIT %d" % floor)
        if kfb:
            mf, sf, _, _, _ = band_point(f_rf, kfb, *TOPBAND)
            print("  MIN_SPLIT %d top band %.4f +- %.4f  z1 %+.2f"
                  % (floor, mf, sf, (mf - 1.0) / sf))
    keyed_h = [(D, f) for (D, f) in keyed if D <= DBOUND_HALF]
    f_rh = [f for (D, f) in keyed_h]
    f_rh, kh, khb = strata_pipeline(f_rh, "DBOUND 8000")
    if khb:
        mh, sh, _, _, _ = band_point(f_rh, khb, *TOPBAND)
        print("  DBOUND 8000 top band %.4f +- %.4f  z1 %+.2f"
              % (mh, sh, (mh - 1.0) / sh))
    worst = 0.0
    for cut in CUTS:
        strata = CV.stratum_cells(f_r, 0, cut)
        for h in keep_r:
            s = strata.get(h)
            if s is None or s['exp'][h] < CV.MIN_CELL or not s['gpf']:
                continue
            pf = sum(s['gpf']) / len(s['gpf'])
            worst = max(worst, abs(pf - CV.pooled_level(s, h)))
    print("  per-field vs pooled: largest gap %.4f" % worst)
    ok(worst < 0.01, "P4: the estimator gap reaches %.4f" % worst)

    section("P5  THE TRIVIAL COLUMN")
    for cut in (CUTS[0], 10 ** 4):
        tr = trivial_level(f_r, 0, cut)
        ti = trivial_level(f_i, 0, cut)
        print("  cut %5d  real trivial %.4f   imaginary trivial %.4f"
              % (cut, tr, ti))
    ok(trivial_level(f_r, 0, CUTS[0]) > trivial_level(f_i, 0, CUTS[0]),
       "P5: the real trivial level is not above the imaginary at the"
       " bottom cut")

    section("C4  POSITIVE CONTROL, UNIFORM (both views)")
    for (fields, keep, tag) in ((f_r, keep_r, "narrow"),
                                (f_w, keep_w, "wide")):
        u = CV.synth_uniform(fields)
        pts = {}
        for cut in (CUTS[0], CUTS[-1]):
            strata = CV.stratum_cells(u, 0, cut)
            mu, se, _ = CV.curve_point(strata, keep, 1.0)
            pts[cut] = mu
            print("  %s uniform cut %4d: %.4f" % (tag, cut, mu))
            ok(abs(mu - 1.0) < 0.08,
               "%s uniform reads %.4f at %d" % (tag, mu, cut))
        ok(abs(pts[CUTS[0]] - pts[CUTS[-1]]) < 0.08,
           "%s uniform curve decays by %.4f"
           % (tag, pts[CUTS[0]] - pts[CUTS[-1]]))

    section("C5  POSITIVE CONTROL, PLANTED DECAY (narrow)")
    pl = CV.synth_planted(f_r)
    vals = []
    for cut in CUTS:
        strata = CV.stratum_cells(pl, 0, cut)
        mu, se, _ = CV.curve_point(strata, keep_r, 1.0)
        vals.append(mu)
        print("  planted cut %4d: %.4f" % (cut, mu))
    strata = CV.stratum_cells(pl, TOPBAND[0], TOPBAND[1])
    mu, se, _ = CV.curve_point(strata, keep_r, 1.0)
    print("  planted band %d-%d: %.4f" % (TOPBAND[0], TOPBAND[1], mu))
    ok(abs(vals[0] - CV.PLANT) < 0.06,
       "the plant reads %.4f at the smallest cut" % vals[0])
    ok(all(vals[i] >= vals[i + 1] - 0.02 for i in range(len(vals) - 1)),
       "the planted curve is not non-increasing: %s" % vals)
    ok(abs(mu - 1.0) < 0.06, "the top band reads %.4f" % mu)

    section("SUMMARY")
    print("  %d checks passed here (plus the imported estimators' own"
          " inside every read), %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
