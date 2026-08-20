r"""THE FOURTH CELL: THE TOTALLY REAL CUBIC'S GENERATOR CEILING, AND THE
SUPPLY THAT PRICES IT -- the carrier verdict (explore_ceiling_realquad.py
F1/F2) rests on three cells of a form-by-unit-rank design: imaginary
quadratic (rank 0, form) keeps its top-band surplus, real quadratic
(rank 1, form) keeps it, complex cubic (rank 1, formless) exhausts it.
The fourth cell -- totally real cubic, rank 2, formless -- is the
discriminating population for the open unit question: if it exhausts,
the fracture is one place law (a quadratic place keeps the surplus, a
formless place loses it, with the unit rank irrelevant at every measured
value); if it persists, the carrier verdict fractures. This file asks
two questions at once, and the first governs the second: WHAT IS THE
COMPOSITE-h TOTALLY REAL SUPPLY at home-feasible discriminant caps --
the census that prices the open clause -- and WHAT DOES THE BEST READ
THAT SUPPLY AFFORDS SAY. Totally real cubic class numbers run small
(the rank-2 regulator absorbs the class number product), so the design
expects the census to be the finding and the read to be wide-barred;
an extreme reading would still be visible, and a middle reading is
worth knowing at the same price.

THE SUPPLY ARITHMETIC, measured before this freeze by an unfrozen
scratch enumeration (not shipped; this file re-derives every figure it
uses in-rig, at S2). At cap 6000 the totally real h-distribution is
{1: 206, 2: 3, 3: 6} -- no composite h at all, where the complex side
at the same cap holds strata {4, 6} with 24 fields. At cap 24000:
{1: 935, 2: 39, 3: 39, 4: 4, 5: 1, 7: 1}; at cap 50000: {1: 2023,
2: 109, 3: 112, 4: 11, 5: 6, 6: 1, 7: 1}. Only composite h feeds the
generator curve (at prime h the generator cell is the non-trivial cell
and the sum identity absorbs it), only non-Galois fields carry partial
places (a Galois cubic has no partial splitting type), and only a
cyclic class group has a generator cell -- so the usable supply is a
sliver: roughly one field per 4000-5000 of cap, growing. This file
widens the cap to 100000, reads the census at three nested caps for
the growth, and reads the ceiling over whatever the frozen rules admit
at bands the supply can power, including primes past the parents' 1000
where the per-field expectation is 20x the top band's.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 EVERYTHING RIDES IN. The enumeration, maximal order, class reading
    with the two-consecutive-rungs agreement and the exclusion policy,
    the bounded Hermite insertion, the memoized ideal ladders and the
    reduced-basis storage are explore_ceiling_topband.py's (importing
    it installs its engine swaps); the per-place reader is
    explore_cubic_split_triple.py's read_field; the population shape,
    admissibility, stratum cells, dispersion scale, curve and band
    estimators and both synthetic controls are
    explore_ceiling_curve.py's; the degree-2 comparators are
    explore_class_order.py's sweep at both signs, exactly as
    explore_ceiling_realquad.py ran them. Nothing is re-implemented.

 T2 THE MAXIMAL-ORDER GUARD WIDENS ONE MORE NOTCH, THE PARENTS' OWN
    MOVE REPEATED. The cap-100000 Hunter box carries polynomial
    discriminants past the topband guard of 4 * 10^6; this file
    installs the same routine with the index-prime sieve at 4000 and
    the guard at 1.6 * 10^7 (p^2 dividing a discriminant under that
    needs p <= 4000), byte-identical below 4 * 10^6 where the loop
    breaks before the bounds part. The box's largest polynomial
    discriminant is printed and asserted under the guard.

 T3 THE PLACE READER'S PRIME LIST IS A MODULE BINDING, SWAPPED PER
    CALL AND RESTORED. read_field iterates its module's ODD_PRIMES
    (primes below 1000). The composite-h fields are read with the list
    set to the odd primes below 10000 and the binding restored after,
    asserted; the certified-field pins re-run under the same swap. At
    p <= the shop's relation prime cap the reader takes the
    generator-basis shortcut, untouched by the swap.

 T4 THE WIDE PRIME RANGE IS UNEXERCISED MACHINERY AND GETS ITS OWN
    PIN. No parent read a cubic place past 1000 (the topband froze
    that as its own T2). Before any composite-h field is read wide,
    a sample of certified h = 1 totally real fields is read over a
    thinned wide prime list, and every mapped partial place must read
    principal -- the identity pin at exactly the machinery the verdict
    will consume. The unmapped-place (None) fraction over all wide
    reads is printed and killed above 0.25, since silent thinning
    would bias the read toward the mappable places.

 T5 THE COMPARATORS ARE IN-RIG WHERE THE BANDS NEED THEM. The
    imaginary side (bound 4000) and the real quadratic side (bound
    16000) are recomputed through the identical estimator path and
    PINNED to their parents' frozen prints before any totally real
    cubic number is read; both are then read at every band this file
    reads, so each cross-population z is same-estimator. The complex
    cubic side enters as the frozen constant 0.9780 +- 0.0123 in the
    top band only -- no complex place past 1000 exists in any frozen
    record, and the wide bands are compared against 1 and against
    degree 2, stated as such.

 T7 THE DOUBLY-SHY LATTICE IS REAL AT THIS SIGNATURE, AND THE
    AGREEMENT LAW DEEPENS -- an amendment made after the first run's
    P1 kill and its diagnostic, before any science print, flagged as
    such. The first run used the parents' two-consecutive-rungs law
    and P1 killed it: the cap-50000 census read {2: 107, 4: 13}
    against the scratch's {2: 109, 4: 11}. The diagnostic (unfrozen,
    not shipped) walked every field in 24000 < d <= 50000 under both
    boxes' representatives with a five-rung ladder: exactly two
    fields flip, d = 32081 and d = 45841, and both show the same
    print -- the wide box's representative walks [4, 4, 2, 2, 2],
    two consecutive SHY rungs agreeing at twice the truth before the
    harvest catches up, while the narrow box's representative and a
    sibling polynomial of the wide box both read h = 2 at every
    rung. A harvested lattice is a sublattice, so the smaller stable
    reading is the honest one. The topband recorded exactly this
    residual ("a doubly-shy lattice, short by the same index at two
    boxes, would still slip through") with the complex population as
    its measured control; the totally real signature, whose large
    units thin the smooth-relation supply, realizes it. The law
    here, grounded in that algebra rather than patched: since the
    harvested index is a MULTIPLE of h, a rung reading H = 1 is
    EXACT and returns immediately, and a reading above 1 is believed
    only when THREE consecutive rungs of a five-rung ladder agree
    ([4, 4, 2, 2, 2] settles at 2), the certification path
    unchanged, exclusion under the same kill when no three agree.
    Both scratch reprints then stand as frozen, the two diagnosed
    fields must print h = 2, and every composite-h field -- the
    science-bearing sliver, mostly at depths the diagnostic never
    walked -- is re-read through a second representative polynomial
    wherever the box carries one, which must agree (P4).

 T6 THE MEMORY SHAPE IS THE ENUMERATION'S. The cap-100000 box holds
    every field's order at once inside enumerate_fields (measured
    179 MB at cap 50000, extrapolating to ~360 MB); the complex
    records are dropped the moment the enumeration returns, and the
    run goes through memwatch. A kill here becomes a streaming flag,
    the topband's own T9 precedent.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE EXPECTATION ARITHMETIC. A non-Galois cubic field yields one
      degree-1 place per partially split prime, density 1/2; the
      generator cell's expectation is tot * phi(h)/h. Per h = 4 field:
      the top band [630, 1000) holds 47 primes, so ~47/2 * 1/2 = 11.7
      expected generators; the wide band [1000, 10000) holds 1061, so
      ~265. With N usable fields the pooled bar is
      scale * sqrt((1-q)/exp): at N = 15 and scale ~1.3 that is ~0.10
      in the top band and ~0.021 in the wide band, against the
      parents' top-band bars of 0.010-0.012. So the top band CANNOT
      decide here at any home cap, and the wide band separates the
      frozen hypotheses only if the signal there is >= ~0.06 -- while
      the degree-2 surpluses at those primes have decayed to
      +0.01-0.03 (imaginary cumulative 1.0240 at 10^4). The design
      therefore expects an indecisive z and prices the decisive cap
      instead: the bar falls as 1/sqrt(supply) and supply grows
      near-linearly, so matching +-0.012 in the top band needs
      roughly (0.10/0.012)^2 = 70x the supply, cap ~10^6 -- printed
      exactly at S2 from the fitted growth.

  (2) DENOMINATORS AND FLOORS. Every cell below MIN_CELL = 30 expected
      drops from curve_point, so the h = 6 stratum (1-2 fields) reads
      nowhere and the read is h = 4's [post-run flag: the guess
      undershot with the rest of P1's ranges -- the box carries seven
      h = 6 fields and the stratum reads in every band; the floor
      logic stands, the count was wrong]; the frozen-strata rule is
      applied and what it drops is printed. The dispersion scale with
      ~15 fields is noisy and within_scale falls back to 1.0 when no
      stratum holds two scale-eligible fields; the scale and its count
      are printed at every band. The excess ratio's h - 1 denominator
      is 3 at h = 4, no new zero. Admissibility needs 10 partial
      places below 250 against a mean of ~13.5, so it thins the
      roster; the roster is printed field by field.

  (3) THE CENSUS IS THREE NESTED CAPS OF ONE ENUMERATION. Counts at
      caps 24000 and 50000 are the |d| <= cap subsets of the one
      cap-100000 run -- same box, same reader -- so the growth points
      share every systematic. The scratch's counts at those caps are
      a reproduction check on the riding-in (P1), not a source.

  (4) INDEX CONVENTION, re-derived from the engine. Bands are
      half-open [lo, hi); stratum_cells reads lo <= p < hi; the wide
      band [1000, 10000) abuts the top band [630, 1000) with no
      overlap and no gap, and 10^4 itself is excluded exactly as the
      degree-2 extension cut excludes it.

  (5) WHAT THE READ CANNOT SAY, fixed now. The h = 4 stratum is one
      stratum: no cross-stratum consistency check exists at this
      supply, and a stratum-specific accident (a bad field's places)
      moves the point. The per-field levels are printed beside the
      pooled one, and the half-cap re-read plus the MIN_TOT = 20
      re-read bound the field-mix sensitivity. No shape claim, no
      asymptote claim, no one-curve claim is available from one
      stratum at two bands; the deliverable is the band levels, their
      z's, and the census.

THE PREDICTIONS, frozen before the engine ran. Kills name PRINTS.

 P1 THE CENSUS REPRINTS AND EXTENDS: the |d| <= 24000 and |d| <= 50000
    totally real h-distributions match the scratch counts quoted
    above exactly (same box, same reader, same agreement rule), and
    the cap-100000 distribution prints with its composite-h roster --
    expected 20-26 non-Galois composite-h fields, of which the
    cyclic-profile, admissible roster keeps 10-20.

 P2 THE ANCHORS: the in-rig imaginary pipeline reprints its parent's
    three frozen figures (top band 1.0426 +- 0.0101, cut-1000 raw
    1.0875, cut-10^4 raw 1.0240) to 5e-5; the in-rig real quadratic
    pipeline reprints its parent's top band 1.0613 +- 0.0069 and
    extension raws 1.0606, 1.0246 to 1e-4 (its parent printed four
    decimals). Kill on any miss.

 P3 THE SPLIT CENSUS, in the parent's own amended form -- an
    amendment flagged as made after this file's second run, whose
    pooled form killed at 0.1460 split fraction, the parent's own
    C4-amendment figure (0.1459) to the fourth decimal: the pooled
    tolerance tests Chebotarev's small-p convergence rate, not the
    instrument, exactly as recorded there. Replaced by the parent's
    C4b transplanted: the type census prints by prime bin (3-30,
    30-100, 100-300, 300-1000) over the non-Galois fields; the
    total variation distance from nominal (1/6, 1/2, 1/3) must be
    smaller in the top bin than in the bottom one, and each top-bin
    component must sit within 0.02 of nominal. Kill outside.

 P4 THE PINS: every partial place of the certified pin sample reads
    principal, at p < 1000 and on the thinned wide list (T4); the
    wide None-fraction stays under 0.25; the exclusion share stays
    under 1%; each composite-h field's read_field span order equals
    its rung-agreed h; the two T7-diagnosed fields d = 32081 and
    d = 45841 print h = 2; and each composite-h field with a second
    representative in the box re-reads the same h through it (T7).
    Kill on any miss.

 P5 THE SYNTHETICS on the admissible composite population: uniform
    within 0.08 of 1 at both cut-ladder ends and at each read band;
    planted recovers 1.30 within 0.06 at the smallest cut,
    non-increasing along the ladder, within 0.06 of 1 in the top
    band. THE MONOTONE SLACK IS AN AMENDMENT, flagged as made after
    this file's third run: the parents' absolute 0.02 was frozen at
    populations 40x this one, where each planted point's own wobble
    sits far beneath it; here the plant's per-point bar is ~0.05 and
    the third run killed on a rise of 0.0202 -- two ten-thousandths
    over a slack the plant's own noise dwarfs, the same
    hand-tolerance-at-the-wrong-scale shape P3 carried. The slack is
    re-derived per step as max(0.02, twice the two points' joint
    error), printed; the recovery and top-band clauses -- the
    load-bearing ones -- keep the parents' figures unchanged. Kill
    outside.

 P6 THE VERDICT PRINT, meaning weighed after: the totally real cubic
    level L +- s at the top band, the wide band and the combined band,
    each with z vs 1 and joint z vs the in-rig imaginary and real
    quadratic at the same band; vs the frozen complex cubic in the
    top band only. Beside them the cumulative levels at the parents'
    cuts, the per-field levels, and the bar-vs-supply table with the
    fitted growth and the extrapolated decisive cap.

 P7 ROBUSTNESS PRINTS (reference lines, not kills, at this supply):
    the half-cap (|d| <= 50000) and MIN_TOT = 20 re-reads beside the
    primary; the per-field vs pooled gap with the parents' 0.02 line
    named.

THE FINDINGS.

 F1 THE SUPPLY CENSUS, AND THE PRICE OF THE FOURTH CELL (observation;
    the census exact over the enumerated box). 4804 totally real
    cubic fields to discriminant 100000, h-distribution {1: 4192,
    2: 290, 3: 267, 4: 21, 5: 18, 6: 7, 7: 7, 8: 1, 9: 1}, the
    nested caps reprinting the scratch counts exactly (P1).
    Non-Galois composite-h fields: 28; the admissible roster keeps
    27 (h = 4: 18, h = 6: 7, h = 8: 1, h = 9: 1), the one exclusion
    being d = 35537 -- the signature's first Klein class group
    (Z/2 x Z/2), priced out by the profile rule as designed, beside
    the complex side's nine below 24000. The frozen rules admit
    strata [4, 6], and the top-band bar the roster affords is
    0.0367 against the parents' 0.010-0.012: three times too wide.
    The usable supply runs 4 / 10 / 27 at caps 24000 / 50000 /
    100000 -- growth ~ cap^1.34 -- so matching the parents' bar
    needs ~9x the supply at cap ~5.3e5: more than five times this
    run's enumeration volume (the cap ratio alone, before the box's
    superlinear growth), past the 512 MB ceiling in an engine that
    holds every order in memory at once (363 MB here), so the
    decisive read is priced at a streaming enumeration rewrite plus
    a multi-hour run, not bought. The open clause's "population
    large enough" now has a number.

 F2 THE FIRST READ OF THE FOURTH CELL: THE CEILING EXISTS, DECAYS,
    AND THE TOP BAND DECIDES NOTHING, LEANING EXHAUST-SIDE
    (observation; one design's two strata, wide bars, no verdict).
    The cumulative levels run 1.2147 +- 0.0315, 1.1417, 1.1071,
    1.0806 over the parents' cuts -- the generator surplus is real
    at this signature (6.8 of its own sigma at cut 250) and decays
    like every population read so far, with the cut-250 excess
    +0.1201 +- 0.0263 beside the real quadratic's +0.1208. The top
    band reads 1.0258 +- 0.0367: z +0.70 vs 1, -0.44 vs the in-rig
    imaginary, -0.95 vs the in-rig real quadratic, +1.24 vs the
    frozen complex cubic -- every hypothesis inside 1.3 sigma. The
    wide band [1000, 10000) reads 1.0028 +- 0.0073 where the same
    estimator puts imaginary at 1.0139 +- 0.0016 and real quadratic
    at 1.0122 +- 0.0012: z +0.38 vs 1, -1.49 and -1.27 against the
    two quadratic populations; combined [630, 10000) 1.0039 +-
    0.0070 (+0.56, -1.60, -1.50). The point estimates sit ON 1
    past the top band and below both quadratic populations --
    the exhaust side, where the one-place-law reading lives --
    and nothing reaches 2 sigma, exactly as derivation (1) priced
    for every outcome short of an extreme one.

 F3 THE WIDE BAND'S VERDICT WOULD RIDE ON A SHAPE ASSUMPTION THE TOP
    BAND DOES NOT NEED (property of the design, printed in the
    comparators). At [1000, 10000) the two degree-2 surpluses have
    decayed to +0.0139 +- 0.0016 and +0.0122 +- 0.0012, so the
    persists-hypothesis has no frozen prediction there: what it
    would predict must be imported by assuming the totally real
    surplus decays at the quadratic populations' rate -- exactly
    the shape claim this corpus refuses elsewhere, the two curves
    being measured as consistent along the lower cuts and nothing
    more. The raw power arithmetic does not close the band
    (separation^2 x expectation is comparable across the two), but
    a wide-band separation would test the imported shape as much as
    the carrier, where the top band tests the fracture where it was
    measured. The decisive instrument is therefore the top band at
    cap ~5.3e5. A population with the same cell coordinates and
    complex-cubic-like supply would dissolve the supply wall
    instead; none exists at degree 3, and the quartic (2,1)
    signature is a different engine, recorded as the open route.
    (Settled 2026-08-20: explore_ceiling_fourthcell.py ran the
    priced read at cap 530000 -- the fourth cell exhausts, on 1 in
    every band against both quadratic populations' held surplus, one
    place law across the design. This file's census, first read and
    price stand as the cap-100000 record.)

THE PREDICTIONS, WEIGHED.

 P1 PASSES on the reprints (both nested distributions exact); the
    guessed ranges undershot -- 28 non-Galois composite against
    "20-26", roster 27 against "10-20" -- the growth's convexity
    read linearly, and the miss is the guess's, flagged as such.
 P2 PASSES: imaginary reprints to 5e-5 (1.0426 +- 0.0101, 1.0875,
    1.0240); real quadratic to 1e-4 (1.0613 +- 0.0069, 1.0606,
    1.0246).
 P3 PASSES in the amended form: TV falls monotonically 0.0769,
    0.0339, 0.0234, 0.0148 over the four bins, and the top bin
    reads 0.1518 / 0.5021 / 0.3461, each component within 0.015 of
    nominal.
 P4 PASSES: 730 pin places principal (637 at p >= 1000), 0 unmapped
    of 17177 vectors over every wide read; 0 fields excluded of
    4804; span order equals rung h at all 28; the T7-diagnosed
    d = 32081 and d = 45841 read h = 2; all 21 fields with a second
    representative agree through it.
 P5 PASSES in the amended form: uniform 0.9922-1.0009 across cut
    ends and bands; the plant reads 1.2553 +- 0.0429 at cut 250
    (recovery gap 0.045 of the 0.06), the one rise 0.0202 against
    its derived slack 0.1108, top band 1.0017.
 P6 THE PRINT: F2's three band levels and their z's; the cumulative
    ladder; the supply table 4 / 10 / 27 with the ^1.34 fit and the
    ~5.3e5 decisive cap.
 P7 the half-cap re-read gives 0.9714 +- 0.0629 (top) and 0.9939 +-
    0.0088 (wide), same side of every line; MIN_TOT 20 keeps 26 of
    27 and reprints the primary bands unchanged; per-field vs
    pooled gaps 0.0015 (h = 4) and 0.0097 (h = 6) against the
    parents' 0.02 line.

RUN RECORD. 2026-08-18, Windows 11, Python 3, `python
prime/code/memwatch.py python prime/code/explore_ceiling_realcubic.py`.
One process, CPython, no BLAS. 873 checks passed here plus the
imported chains' own, 1656.0 s wall, peak working set 363.5 MB
against memwatch's 512 MB ceiling (T6's extrapolation said ~360).
The enumeration kept 21845 fields from 503106 box polynomials in
263 s; the totally real class reading took 1294 s for 4804 fields;
the 28 wide place reads 29 s, the 21 sibling cross-reads 32 s, the
pins 2 s. THREE EARLIER ATTEMPTS, each killed by a frozen
prediction before any science print, each kill becoming a flag
above: the first (two-rung agreement) killed by P1's census
reprint -- the doubly-shy flip T7 records; the second killed by
P3's pooled form at the parent's own C4-amendment figure; the
third killed by P5's absolute slack on a rise of 0.0202 against
0.02. The S1-S3 prints of the failed runs match this run's digit
for digit where their laws coincide."""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from collections import defaultdict

sys.stdout.reconfigure(line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_ceiling_topband as TB          # installs the engine swaps
import explore_ceiling_curve as CV
import explore_cubic_principal as ECP
import explore_cubic_field_shop as CFS
import explore_cubic_transposition as XT
import explore_cubic_split_triple as ST
import explore_class_order as CO
from explore_class_share import classes_real
from explore_principal_share import primes_upto, reduce_form, \
    class_data_real

CHECKS = 0

CAP = 100000                       # this file's box
CENSUS_CAPS = (24000, 50000, CAP)  # derivation (3)'s nested thirds
HALF_CAP = 50000                   # P7's re-read
WIDE_PRIME_CAP = 10000             # T3's swapped list
PIN_STRIDE_WIDE = 5                # T4: every 5th odd prime in the pin
PIN_FIELDS = 6                     # T4: certified fields in the pin
NONE_KILL = 0.25                   # T4's thinning kill
EXCL_KILL = 0.01                   # the topband's own exclusion kill

PROBE_24K = {1: 935, 2: 39, 3: 39, 4: 4, 5: 1, 7: 1}
PROBE_50K = {1: 2023, 2: 109, 3: 112, 4: 11, 5: 6, 6: 1, 7: 1}

DEG3_TOP = (0.9780, 0.0123)        # frozen, explore_ceiling_topband F1
IMAG_TOP = (1.0426, 0.0101)        # frozen, explore_ceiling_curve F5
IMAG_CUT1000 = 1.0875              # frozen, explore_ceiling_curve P5
IMAG_CUT10K = 1.0240               # frozen, explore_ceiling_curve P5
REAL_TOP = (1.0613, 0.0069)        # frozen, explore_ceiling_realquad F1
REAL_CUT2500 = 1.0606              # frozen, explore_ceiling_realquad P1
REAL_CUT10K = 1.0246               # frozen, explore_ceiling_realquad P1
DBOUND_REAL = 16000                # the realquad parent's bound

CUTS = CV.CUTS
TOPBAND = CV.BANDS[-1]             # (630, 1000)
WIDEBAND = (1000, WIDE_PRIME_CAP)
COMBBAND = (TOPBAND[0], WIDE_PRIME_CAP)

XSIEVE = ECP.CR._sieve(4000)
WIDE_ODD = [p for p in ECP.CR._sieve(WIDE_PRIME_CAP) if p != 2]


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise SystemExit("FAIL: " + msg)


def section(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


def maximal_order3_x(a, b, c):
    """T2: the topband's widened routine, one notch wider again --
    sieve 4000, guard 1.6e7; byte-identical below 4e6 where the loop
    breaks before either bound differs."""
    R = (-c, -b, -a)
    trvec = (3, -a, a * a - 2 * b)
    O = CFS.Order(R, trvec, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    d0 = O.trace_form_disc()
    assert abs(d0) < 16 * 10 ** 6, "discriminant out of the widened range"
    for p in XSIEVE:
        if p * p > abs(d0):
            break
        if d0 % (p * p) == 0:
            O = CFS.p_maximalize(O, p)
    return O, O.trace_form_disc()


ECP.maximal_order3 = maximal_order3_x     # T2: the declared swap

RUNGS5 = ((CFS.REL_BOX, 400), (CFS.REL_BOX + 6, 1500),
          (CFS.REL_BOX + 12, 4000), (CFS.REL_BOX + 18, 8000),
          (CFS.REL_BOX + 24, 16000))


def read_one3(d, cx, a, b, c, O):
    """T7: the topband's read_one with the agreement law deepened --
    a reading is believed only when three consecutive rungs of the
    five-rung ladder agree; the certification path is verbatim."""
    rows = ECP.t2_rows(O, a, b, c)
    gp = CFS.relation_generators(O)
    mb = CFS.minkowski_bound(d, O.n, cx)
    small = [t for t in CFS.all_places_upto_prime(O, mb)
             if t[0] ** t[2] <= mb]
    if all(ECP.find_gen(O, P, rows, p ** f, cx) is not None
           for (p, e, f, name, P) in small):
        return 1, 'cert', gp, None
    hist = []
    for (box, cap) in RUNGS5:
        rows2 = CFS.harvest_relations(O, gp, box=box, cap=cap)
        H = CFS.hermite_order(rows2, len(gp))
        if H == 1:
            return 1, 'relH1', gp, rows2      # T7: a multiple of h
        hist.append(H)
        if (len(hist) >= 3 and H is not None
                and hist[-2] == H and hist[-3] == H):
            return H, 'H', gp, rows2
    return None


def read_field_wide(rec):
    """T3: ST.read_field under the wide prime list, binding restored
    and asserted. rec is a read_one-shaped tuple."""
    (d, cx, a, b, c, O, h, kind, gp, rel) = rec
    old = ST.ODD_PRIMES
    ST.ODD_PRIMES = WIDE_ODD
    try:
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
    finally:
        ST.ODD_PRIMES = old
    ok(ST.ODD_PRIMES is old, "T3: the prime-list binding did not restore")
    return H, piv, k, per_prime


SPLIT_BINS = list(zip(ECP.BIN_EDGES, ECP.BIN_EDGES[1:]))
NOMINAL = (1 / 6.0, 1 / 2.0, 1 / 3.0)


def split_type_counts(a, b, c, d):
    """Per-bin (split, partial, inert) counts over odd unramified
    p < 1000 -- the P3 census in the parent's C4b binned form, by
    root count of the cubic mod p."""
    n = [[0, 0, 0] for _ in SPLIT_BINS]
    for p in ECP.ODD_PRIMES:
        if d % p == 0:
            continue
        roots = sum(1 for x in range(p)
                    if (((x + a) * x + b) * x + c) % p == 0)
        for j, (lo, hi) in enumerate(SPLIT_BINS):
            if lo <= p < hi:
                n[j][0 if roots == 3 else (1 if roots == 1 else 2)] += 1
                break
    return n


def census(rows):
    """The h-distributions at the nested caps (P1), Galois split."""
    for cap in CENSUS_CAPS:
        hs = defaultdict(int)
        hs_ng = defaultdict(int)
        for (d, cyc, h) in rows:
            if d > cap:
                continue
            hs[h] += 1
            if not cyc:
                hs_ng[h] += 1
        print("  cap %6d: %4d totally real, h %s" %
              (cap, sum(hs.values()), dict(sorted(hs.items()))))
        print("             non-Galois        h %s"
              % dict(sorted(hs_ng.items())))
        if cap == 24000:
            ok(dict(hs) == PROBE_24K,
               "P1: the 24000 census does not reprint the scratch")
        if cap == 50000:
            ok(dict(hs) == PROBE_50K,
               "P1: the 50000 census does not reprint the scratch")


def band_point(fields, keep, lo, hi):
    strata = CV.stratum_cells(fields, lo, hi)
    scale, nsc = CV.within_scale(strata, keep)
    mu, se, pts = CV.curve_point(strata, keep, scale)
    return mu, se, pts, scale, nsc


def print_band(tag, lo, hi, mu, se, pts, scale, nsc):
    cells = "  ".join("h=%d %.3f+-%.3f" % t for t in pts)
    print("  %-10s band %5d-%5d  %.4f +- %.4f  (scale %.3f/%d)  %s"
          % (tag, lo, hi, mu, se, scale, nsc, cells))


def run_sweep(sign, bound, plist):
    """CO.sweep with the module bound set for the call (the realquad
    parent's T3 move)."""
    old = CO.DBOUND
    CO.DBOUND = bound
    try:
        return CO.sweep(sign, plist)
    finally:
        CO.DBOUND = old


def deg2_side(sign, bound, tag, plist):
    """One degree-2 comparator population through the frozen chain."""
    rows, bad, id_bad, c2_bad, c4_bad, law_bad = run_sweep(
        sign, bound, plist)
    ok(CO.DBOUND == 4000, "the module bound did not restore")
    ok(bad[2] == 0 and bad[3] == 0, "the %s order walk failed" % tag)
    pop = CV.build_pop2(rows)
    del rows
    f = CV.admissible(pop, CUTS[0], CO.MIN_SPLIT)
    cnt = defaultdict(int)
    for (h, c, pl) in f:
        cnt[h] += 1
    f = [(h, c, pl) for (h, c, pl) in f if cnt[h] >= CV.MINSTRAT]
    keep, keepb = CV.frozen_strata(f, CUTS, CV.BANDS)
    keep = [h for h in keep if CV.is_composite(h)]
    keepb = [h for h in keepb if CV.is_composite(h)]
    print("  %s: %d fields, cumulative strata %s, band strata %s"
          % (tag, len(f), keep, keepb))
    return f, keep, keepb


def main():
    t0 = time.time()

    section("S1  THE ENUMERATION -- cap %d (T2, T6)" % CAP)
    t1 = time.time()
    fields, box = ECP.enumerate_fields(CAP)
    maxpd = max(abs(CFS.poly_disc3(a, b, c))
                for (ad, d, cx, polys) in fields
                for (a, b, c, O) in polys[:1])
    print("  %d polynomials -> %d fields, largest field polynomial"
          " discriminant %d, %.1f s"
          % (box[0], len(fields), maxpd, time.time() - t1))
    ok(maxpd < 16 * 10 ** 6, "T2: the box outran the widened guard")
    tre = [f for f in fields if not f[2]]
    del fields                                # T6: drop the complex side
    print("  %d totally real fields kept" % len(tre))

    section("S2  THE CLASS CENSUS (P1) AND THE ROSTER")
    t1 = time.time()
    rows_census = []
    recs = []
    excluded = []
    xpolys = {}                    # T7: siblings of the composite sliver
    for i, (ad, d, cx, polys) in enumerate(tre):
        if i and i % 500 == 0:
            print("  ... %d/%d fields, %.1f s"
                  % (i, len(tre), time.time() - t1))
        a, b, c, O = polys[0]
        got = read_one3(d, cx, a, b, c, O)
        if got is None:
            excluded.append(d)
            continue
        h, kind, gp, rel = got
        cyc = int(round(ad ** 0.5)) ** 2 == ad
        rows_census.append((d, cyc, h))
        if d in (32081, 45841):
            ok(h == 2, "P4: T7-diagnosed field d=%d reads h=%d" % (d, h))
        recs.append((d, cx, a, b, c, O, h, kind, gp,
                     TB.rel_basis(rel, len(gp)), cyc))
        if not cyc and CV.is_composite(h) and len(polys) > 1:
            xpolys[d] = polys[1]
    print("  class reading: %d read, %d excluded %s, %.1f s"
          % (len(recs), len(excluded), excluded, time.time() - t1))
    ok(len(excluded) <= EXCL_KILL * len(tre),
       "P4: %d of %d fields excluded" % (len(excluded), len(tre)))
    del tre                                   # T6
    census(rows_census)
    comp = [r for r in recs if not r[10] and CV.is_composite(r[6])]
    print("  non-Galois composite-h fields: %d" % len(comp))

    section("S3  THE SPLIT CENSUS (P3, the parent's C4b binned form)")
    tot = [[0, 0, 0] for _ in SPLIT_BINS]
    n_ng = 0
    for (d, cx, a, b, c, O, h, kind, gp, rel, cyc) in recs:
        if cyc:
            continue
        n_ng += 1
        s = split_type_counts(a, b, c, d)
        for j in range(len(SPLIT_BINS)):
            for t in range(3):
                tot[j][t] += s[j][t]
    tvs = []
    for j, (lo, hi) in enumerate(SPLIT_BINS):
        allp = float(sum(tot[j]))
        fr = [t / allp for t in tot[j]]
        tv = 0.5 * sum(abs(f - nm) for f, nm in zip(fr, NOMINAL))
        tvs.append(tv)
        print("  bin %4d-%4d  split/partial/inert %.4f / %.4f / %.4f"
              "  TV %.4f" % (lo, hi, fr[0], fr[1], fr[2], tv))
    print("  %d non-Galois fields pooled per bin" % n_ng)
    ok(tvs[-1] < tvs[0],
       "P3: the census does not converge, TV %.4f top vs %.4f bottom"
       % (tvs[-1], tvs[0]))
    allp = float(sum(tot[-1]))
    for f, nm, lab in zip((t / allp for t in tot[-1]), NOMINAL,
                          ("split", "partial", "inert")):
        ok(abs(f - nm) < 0.02,
           "P3: top-bin %s fraction %.4f" % (lab, f))

    section("S4  THE WIDE PIN (T4, P4) -- certified fields first")
    pin_odd = WIDE_ODD[::PIN_STRIDE_WIDE]
    pool = [r for r in recs if r[7] == 'cert' and not r[10]]
    pin = pool[::max(1, len(pool) // PIN_FIELDS)][:PIN_FIELDS]
    t1 = time.time()
    n_pin = n_pin_wide = n_none = n_vec = 0
    for rec in pin:
        old = ST.ODD_PRIMES
        ST.ODD_PRIMES = pin_odd
        try:
            H, piv, k, per_prime = ST.read_field(
                rec[5], rec[2], rec[3], rec[4], rec[0], rec[1],
                rec[8], rec[9])
        finally:
            ST.ODD_PRIMES = old
        ok(H is None or H == 1,
           "P4: certified field d=%d reads span order %s" % (rec[0], H))
        for (p, kd, vecs) in per_prime:
            if kd != 'partial' or len(vecs) != 1:
                continue
            n_vec += 1
            if vecs[0] is None:
                n_none += 1
                continue
            ok(ST.is_principal(vecs[0], piv, k),
               "P4: a certified field's place at p=%d reads"
               " non-principal" % p)
            n_pin += 1
            if p >= 1000:
                n_pin_wide += 1
    print("  %d certified fields, %d places principal (%d at p >= 1000),"
          " %d unmapped, %.1f s"
          % (len(pin), n_pin, n_pin_wide, n_none, time.time() - t1))
    ok(n_pin_wide > 0, "P4: the pin read no wide place at all")

    section("S5  THE COMPOSITE POPULATION, READ WIDE (T3, T7)")
    t1 = time.time()
    n_x = 0
    for rec in comp:
        if rec[0] not in xpolys:
            continue
        a2, b2, c2, O2 = xpolys[rec[0]]
        got2 = read_one3(rec[0], rec[1], a2, b2, c2, O2)
        ok(got2 is not None and got2[0] == rec[6],
           "P4: d=%d reads h=%d through the first representative and"
           " %s through the second"
           % (rec[0], rec[6], got2[0] if got2 else None))
        n_x += 1
    print("  T7: %d of %d composite-h fields cross-read through a"
          " second representative, all agreeing, %.1f s"
          % (n_x, len(comp), time.time() - t1))
    t1 = time.time()
    mapped = []
    n_none_w = n_vec_w = 0
    for rec in comp:
        H, piv, k, per_prime = read_field_wide(rec[:10])
        ok(H == rec[6], "P4: span order %s != rung h %d at d=%d"
           % (H, rec[6], rec[0]))
        prof = XT.group_profile(piv, k, H)
        ok(prof is not None and sum(prof.values()) == H,
           "profile control failed at d=%d" % rec[0])
        for (p, kd, vecs) in per_prime:
            if kd == 'partial' and len(vecs) == 1:
                n_vec_w += 1
                if vecs[0] is None:
                    n_none_w += 1
        mapped.append((rec[0], rec[1], rec[2], rec[3], rec[4], rec[5],
                       H, piv, k, per_prime, prof))
    frac_none = n_none_w / float(max(n_vec_w, 1))
    print("  %d fields read wide, unmapped fraction %.3f (%d of %d),"
          " %.1f s" % (len(mapped), frac_none, n_none_w, n_vec_w,
                       time.time() - t1))
    ok(frac_none < NONE_KILL, "T4: the wide read thinned by %.3f"
       % frac_none)
    pop = CV.build_pop3(mapped)
    f_r = CV.admissible(pop, CUTS[0], CV.MIN_TOT)
    keep, keepb = CV.frozen_strata(f_r, CUTS, CV.BANDS)
    keep = [h for h in keep if CV.is_composite(h)]
    keepb = [h for h in keepb if CV.is_composite(h)]
    hcnt = defaultdict(int)
    for f in f_r:
        hcnt[f[0]] += 1
    print("  admissible roster: %d of %d, by h %s"
          % (len(f_r), len(pop), dict(sorted(hcnt.items()))))
    print("  frozen strata: cumulative %s, band %s" % (keep, keepb))
    for (d, cx, a, b, c, O, H, piv, k, pp, prof) in mapped:
        if not CV.cyclic_profile(
                H, [(i, o) for i, o in
                    enumerate(sum(([oo] * cc for oo, cc in
                                   sorted(prof.items())), []))]):
            print("    non-cyclic profile: d=%d h=%d %s"
                  % (d, H, dict(sorted(prof.items()))))

    section("S6  THE ANCHORS (T5, P2) -- both degree-2 comparators")
    plist = primes_upto(CO.PCAP)
    f_i, keep_i, keep_ib = deg2_side(-1, 4000, "imaginary", plist)
    c_i = CV.read_curve(f_i, keep_i, CUTS + CV.EXT_CUTS, "imag")
    mu_it, se_it, _, _, _ = band_point(f_i, keep_ib, *TOPBAND)
    ok(abs(c_i[1000][0] - IMAG_CUT1000) < 5e-5,
       "P2: imaginary cut-1000 reprint off: %.4f" % c_i[1000][0])
    ok(abs(c_i[10000][0] - IMAG_CUT10K) < 5e-5,
       "P2: imaginary cut-10^4 reprint off: %.4f" % c_i[10000][0])
    ok(abs(mu_it - IMAG_TOP[0]) < 5e-5 and abs(se_it - IMAG_TOP[1]) < 5e-5,
       "P2: imaginary top band reprint off: %.4f +- %.4f"
       % (mu_it, se_it))
    print("  imaginary anchors reprint to 5e-5")
    f_q, keep_q, keep_qb = deg2_side(+1, DBOUND_REAL, "real quad", plist)
    c_q = CV.read_curve(f_q, keep_q, CUTS + CV.EXT_CUTS, "realq")
    mu_qt, se_qt, _, _, _ = band_point(f_q, keep_qb, *TOPBAND)
    ok(abs(c_q[2500][0] - REAL_CUT2500) < 1e-4,
       "P2: real quad cut-2500 reprint off: %.4f" % c_q[2500][0])
    ok(abs(c_q[10000][0] - REAL_CUT10K) < 1e-4,
       "P2: real quad cut-10^4 reprint off: %.4f" % c_q[10000][0])
    ok(abs(mu_qt - REAL_TOP[0]) < 1e-4 and abs(se_qt - REAL_TOP[1]) < 1e-4,
       "P2: real quad top band reprint off: %.4f +- %.4f"
       % (mu_qt, se_qt))
    print("  real quadratic anchors reprint to 1e-4")
    comp2 = {}
    for (tag, ff, kb) in (("imag", f_i, keep_ib), ("realq", f_q, keep_qb)):
        for band in (TOPBAND, WIDEBAND, COMBBAND):
            mu, se, pts, sc, nsc = band_point(ff, kb, *band)
            comp2[(tag, band)] = (mu, se)
            print_band(tag, band[0], band[1], mu, se, pts, sc, nsc)

    section("S7  THE SYNTHETIC CONTROLS (P5) on the admissible roster")
    u = CV.synth_uniform(f_r)
    for (lo, hi, tag) in ((0, CUTS[0], "cut 250"), (0, CUTS[-1],
                          "cut 1000"), (TOPBAND[0], TOPBAND[1], "top"),
                          (WIDEBAND[0], WIDEBAND[1], "wide"),
                          (COMBBAND[0], COMBBAND[1], "comb")):
        strata = CV.stratum_cells(u, lo, hi)
        mu, se, _ = CV.curve_point(strata, keep, 1.0)
        print("  uniform %-8s: %.4f" % (tag, mu))
        ok(abs(mu - 1.0) < 0.08, "P5: uniform reads %.4f at %s"
           % (mu, tag))
    pl = CV.synth_planted(f_r)
    vals, ses = [], []
    for cut in CUTS:
        strata = CV.stratum_cells(pl, 0, cut)
        mu, se, _ = CV.curve_point(strata, keep, 1.0)
        vals.append(mu)
        ses.append(se)
        print("  planted cut %4d: %.4f +- %.4f" % (cut, mu, se))
    strata = CV.stratum_cells(pl, *TOPBAND)
    mu_p, _, _ = CV.curve_point(strata, keep, 1.0)
    print("  planted top band: %.4f" % mu_p)
    ok(abs(vals[0] - CV.PLANT) < 0.06,
       "P5: the plant reads %.4f at the smallest cut" % vals[0])
    for i in range(len(vals) - 1):
        slack = max(0.02, 2 * (ses[i] ** 2 + ses[i + 1] ** 2) ** 0.5)
        print("  planted step %d->%d slack %.4f (rise %.4f)"
              % (CUTS[i], CUTS[i + 1], slack, vals[i + 1] - vals[i]))
        ok(vals[i] >= vals[i + 1] - slack,
           "P5: the planted curve rises %.4f against slack %.4f"
           % (vals[i + 1] - vals[i], slack))
    ok(abs(mu_p - 1.0) < 0.06, "P5: the planted top band reads %.4f"
       % mu_p)

    section("S8  P6 -- THE VERDICT PRINT")
    c_r = CV.read_curve(f_r, keep, CUTS, "real cubic")
    print("  cumulative: %s"
          % "  ".join("%d: %.3f" % (c, c_r[c][0]) for c in CUTS))
    for band in (TOPBAND, WIDEBAND, COMBBAND):
        mu, se, pts, sc, nsc = band_point(f_r, keepb, *band)
        print_band("real cubic", band[0], band[1], mu, se, pts, sc, nsc)
        z1 = (mu - 1.0) / se
        zi = CV.zdiff((mu, se), comp2[("imag", band)])
        zq = CV.zdiff((mu, se), comp2[("realq", band)])
        line = ("    z vs 1 %+.2f   vs imaginary %+.2f   vs real quad"
                " %+.2f" % (z1, zi, zq))
        if band == TOPBAND:
            line += "   vs frozen complex cubic %+.2f" % CV.zdiff(
                (mu, se), DEG3_TOP)
        print(line)
    strata = CV.stratum_cells(f_r, *TOPBAND)
    for h in keepb:
        s = strata.get(h)
        if s and s['gpf']:
            print("  per-field top-band levels (h=%d): %s"
                  % (h, " ".join("%.2f" % v for v in sorted(s['gpf']))))
            pf = sum(s['gpf']) / len(s['gpf'])
            print("  per-field mean %.4f vs pooled %.4f (gap %.4f;"
                  " the parents' line is 0.02)"
                  % (pf, CV.pooled_level(s, h),
                     abs(pf - CV.pooled_level(s, h))))

    section("S9  THE SUPPLY TABLE AND THE PRICE (P6)")
    caps = CENSUS_CAPS
    usable = []
    for cap in caps:
        n = sum(1 for f, m in zip(pop, mapped) if abs(m[0]) <= cap
                and f in f_r)
        usable.append(n)
        m, s2_, pts, sc, nsc = band_point(
            [f for f, mm in zip(pop, mapped)
             if abs(mm[0]) <= cap and f in f_r], keepb, *TOPBAND)
        bar = "%.4f" % s2_ if s2_ else "unreadable"
        print("  cap %6d: %2d usable fields, top-band bar %s"
              % (cap, n, bar))
    if usable[0] > 0 and usable[-1] > usable[0]:
        import math
        expo = (math.log(usable[-1] / float(usable[0]))
                / math.log(caps[-1] / float(caps[0])))
        mu, se, _, _, _ = band_point(f_r, keepb, *TOPBAND)
        need = (se / 0.012) ** 2
        cap_star = CAP * need ** (1.0 / expo)
        print("  supply growth ~ cap^%.2f; matching the parents'"
              " +-0.012 bar needs ~%.0fx the supply, cap ~%.1e"
              % (expo, need, cap_star))

    section("S10  P7 -- ROBUSTNESS PRINTS")
    f_h = [f for f, m in zip(pop, mapped)
           if abs(m[0]) <= HALF_CAP and f in f_r]
    for band in (TOPBAND, WIDEBAND):
        mu, se, pts, sc, nsc = band_point(f_h, keepb, *band)
        if mu is not None:
            print_band("half-cap", band[0], band[1], mu, se, pts, sc,
                       nsc)
    f_20 = CV.admissible(pop, CUTS[0], CV.MIN_TOT_HARD)
    print("  MIN_TOT 20 keeps %d of %d" % (len(f_20), len(f_r)))
    for band in (TOPBAND, WIDEBAND):
        mu, se, pts, sc, nsc = band_point(f_20, keepb, *band)
        if mu is not None:
            print_band("MIN_TOT 20", band[0], band[1], mu, se, pts,
                       sc, nsc)

    section("SUMMARY")
    print("  %d checks passed here (plus the imported chains' own),"
          " %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
