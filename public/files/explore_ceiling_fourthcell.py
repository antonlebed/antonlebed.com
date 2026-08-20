r"""THE DECISIVE FOURTH-CELL READ: THE STREAMING ENUMERATION, AND THE
TOP BAND AT THE PRICED CAP -- explore_ceiling_realcubic.py priced the
totally real cubic's generator-ceiling question rather than answering
it: the usable composite-h supply is 27 fields below discriminant
100000, growing as cap^1.34, so the band that decides -- the top band
[630, 1000), where the two quadratic populations hold their surplus at
+0.043 and +0.061 while the complex cubic reads consistent with 1 --
needs cap ~5.3e5, past the 512 MB ceiling of an engine that holds every
maximal order in memory at once (363 MB at cap 100000). This file is
the named rewrite: a STREAMING enumeration that keeps only each field's
defining data (discriminant, fingerprint, representative coefficient
triples) during the box walk, rebuilds one maximal order at a time
during the class reading, and retains full records only for the
composite-h non-Galois sliver the read consumes. The question it
decides: does the totally real cubic (unit rank 2, no form at the
degree-1 place) KEEP its top-band surplus like both quadratic
populations, or EXHAUST it like the complex cubic -- one place law (a
quadratic place keeps the surplus, a formless place loses it, the unit
rank irrelevant at every measured value), or a fractured carrier.

THE DESIGN IN ONE LINE: one enumeration to |d| <= 530000, the class
reading walked in ascending discriminant with a HARD CONTROL GATE at
100000 -- the parent rig's census and band figures must reprint exactly
before any field past the gate is read -- then the full-population read
through the parent's own frozen rules, nothing re-derived.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 EVERYTHING RIDES IN, THE PARENT'S OWN RIG WHERE IT EXISTS.
    Importing explore_ceiling_realcubic installs the whole stack (the
    topband engine swaps, the widened maximal order, the five-rung
    agreement reader); this file calls its read_one3, read_field_wide,
    split_type_counts, census, band_point, print_band and deg2_side
    directly, with its frozen comparator constants. New code is FOUR
    pieces only, each pinned: the streaming box walk, a divisor-based
    irreducibility screen, a Frobenius-based split counter, and the
    guard widened for this box.

 T2 THE MAXIMAL-ORDER GUARD, RE-DERIVED FOR THIS BOX. Hunter's box at
    cap 530000 has s1 in {0,1}, |s2| <= 243, |s3| <= 2059; the
    polynomial discriminant 18abc - 4a^3c + a^2b^2 - 4b^3 - 27c^2 is
    triangle-bounded by 18*243*2059 + 4*2059 + 243^2 + 4*243^3 +
    27*2059^2 = 180,934,966 < 2e8, so the index-prime sieve moves to
    15000 (p^2 dividing a discriminant under 2e8 needs p <= 14143) and
    the guard to 2e8. Byte-identical to the parent's routine below
    1.6e7, where the p^2 > |d0| break fires before either bound
    differs; the box's largest polynomial discriminant is printed and
    asserted under the guard.

 T3 THE STREAMING WALK SKIPS THE COMPLEX SIDE AT THE DISCRIMINANT
    SIGN. The parent enumerated both signatures and dropped the
    complex records after; this file skips any polynomial whose
    polynomial discriminant is <= 0 before maximalizing (a totally
    real cubic has positive discriminant; a zero discriminant means a
    repeated factor, hence reducible). The walk keeps the parent's
    exact loop order (s1, then s2, then s3 ascending) and its exact
    dedup rule (fields keyed by discriminant, separated within one by
    splitting-fingerprint compatibility, first-seen representative
    first), so the kept field list and each field's first
    representative are the parent's own.

 T4 THE IRREDUCIBILITY SCREEN IS THE RATIONAL ROOT TEST OVER THE
    DIVISORS OF c ONLY -- the same mathematical test as the parent's
    (which scans every r <= |c|), restated over the divisor set, exact
    by the rational root theorem. Pinned: on a stride of the walk's
    positive-discriminant polynomials the screen must agree with
    explore_cubic_field_shop.is_irreducible_cubic call for call, and
    the control gate (P1) re-verifies the kept set wholesale.

 T5 THE SPLIT COUNTER COUNTS ROOTS BY FROBENIUS, NOT BY SCAN. The
    parent's split_type_counts loops all residues x mod p; this file
    computes deg gcd(x^p - x, f) over F_p by square-and-multiply on
    degree-<3 polynomials -- 0, 1 or 3 distinct roots (the cubic is
    squarefree away from p | d), the same three splitting types.
    Pinned: on a stride of the non-Galois fields the per-bin counts
    must equal the parent's function's, bin for bin.

 T6 THE MEMORY SHAPE IS THE POINT. The box walk stores per field one
    small tuple (discriminant, fingerprint dict, coefficient triples);
    no Order object survives it. The class reading rebuilds one order
    at a time and keeps full records -- order, generators, relation
    basis, wide per-prime reads -- only for non-Galois composite-h
    fields (projected ~250 at this cap). Everything else is one
    (d, cyclic, h) row. The run goes through memwatch at the default
    512 MB ceiling; the projection is ~150 MB peak.

 T7 THE CONTROL GATE IS THE PARENT'S WHOLE SCIENCE REPRINTED
    MID-STREAM. The class reading walks ascending |d|; at the first
    field past 100000 the gate fires: the nested censuses (24000,
    50000, 100000) must equal the parent's printed distributions
    EXACTLY, the composite roster must be the parent's 28-with-27
    admissible at strata {4: 18, 6: 7, 8: 1, 9: 1}, and the control
    population's band figures must reprint the parent's F2 to 5e-5 --
    cut-250 cumulative 1.2147 +- 0.0315, top band 1.0258 +- 0.0367,
    wide band 1.0028 +- 0.0073, combined 1.0039 +- 0.0070. The same
    code path on the same population in the same order is digit-exact;
    5e-5 is print rounding. Kill at the gate spends minutes, not
    hours.

 T8 THE WIDE PRIME MACHINERY, THE AGREEMENT LAW AND THE PROFILE RULE
    RIDE IN UNCHANGED: the 10^4 prime list swap with its restore
    assert, the three-consecutive-rungs class agreement, the certified
    wide pin with the unmapped-place kill at 0.25, the sibling
    cross-read through a second representative wherever the box
    carries one, and the cyclic-profile admissibility that priced out
    the Klein field at d = 35537 -- every rule the parent froze, none
    reopened.

 T9 THE READ RETRIES THROUGH THE FIELD'S OTHER REPRESENTATIVES BEFORE
    EXCLUDING -- a flag, adopted after the first run was killed AT THE
    GATE by exactly the presentation dependence the parents' sibling
    cross-reads exist for: the wider box changes which polynomial is a
    field's first-seen representative, and one h = 2 field below
    24000 whose parent-representative read settled returned None
    through the wide box's first (the five-rung agreement is a
    property of the presentation, the class number is the field's),
    printing 1018 census rows against the parent's 1019 -- the walk
    itself checked identical to the parent record for record. The
    cure reads each representative in turn and excludes only when
    every one fails; the count of fields read through a later
    representative is printed, and the census gate then re-validates
    every read against the parent's, both directions. The sibling
    cross-read (T8) uses a representative different from the one the
    read consumed.

T10 THE PIN JUDGES AGAINST A PROVEN LATTICE -- a flag, adopted after
    the second run was killed at the wide pin, 5.6 hours in with the
    whole class reading green behind it: a certified field's place at
    p = 17 read non-principal. A certified field hands the pin no
    relation set (certification short-circuits before harvesting), so
    the wide reader harvested its own with its default box, and the
    pin's original tolerance -- span order 1 OR a rank-deficient
    harvest -- let a field through whose default lattice was
    sub-full, where a genuinely principal generator sits outside the
    span. Three deep certified fields probed clean through the same
    path, so the trigger is field-specific and the cure is
    structural: each pin candidate's relations are harvested through
    the five-rung ladder and the candidate serves only when the
    Hermite order settles at exactly 1 -- a provably complete lattice
    -- with unsettled candidates skipped and counted. The pin then
    tests what it was built to test, the wide place mapping, and its
    span-order assert tightens from "1 or None" to "1". The sibling
    cross-read gets the matching correction: a sibling no rung
    settles is printed as unsettled rather than read as a
    disagreement (T9's own lesson).

T11 A FLIP IS DATA, RESOLVED BY DIVISIBILITY -- a flag, adopted after
    the third run was killed by a settled disagreement the second
    run's design treated as fatal: d = 305977 reads h = 4 through its
    first representative and h = 2 through its second, the doubly-shy
    flip (rungs agreeing at a multiple of the truth) realized in the
    wide range, where at ~440 composite fields a flip is a
    population fact and not a redesign signal. The resolution rides
    on what the harvest guarantees: a settled reading's Hermite order
    is the index of a sublattice of the full relation lattice, hence
    a MULTIPLE of the true class number, so over several
    representatives the truth divides every settled reading. The
    rule, frozen: each composite reading is attested through up to
    four further representatives, stopping at the first agreement;
    on disagreement the gcd of the settled readings is adopted when
    some representative settles at exactly it -- that representative's
    whole read (order, generators, relations) riding forward, since
    the wide span downstream is computed against the adopted lattice
    -- and the field is excluded and printed when no representative
    attests the gcd. Both counts print, the resolution runs at read
    time so the census itself carries resolved readings, and a
    reading with no settled sibling is counted as unconfirmed rather
    than silently trusted.

T12 THE WIDE SPAN IS THE THIRD INSTRUMENT, AND IT OUTRANKS THE RUNG
    LADDER -- a flag, adopted after the fourth run was killed by a
    field T11's sibling walk had passed: d = 114561's rung readings
    attest h = 4 and the wide read's span order prints 2. The span is
    computed over the rung-agreed relations PLUS every relation the
    place mapping itself discovers, so it indexes a larger sublattice
    of the same relation lattice: the span order divides the rung
    reading and is a multiple of the true h -- the tightest
    attestation the rig owns, the third instrument the graded
    agreement law asks for above an exact floor. The rule, frozen:
    the equality kill becomes a divisibility check (a span order not
    dividing its rung reading is an integrity failure and still
    kills), a smaller span DEMOTES the field's h in place -- census
    rows corrected, the field leaving the composite roster when the
    demoted h is prime -- each demotion printed with its pair, and
    the census prints AFTER the resolution so what it states is what
    the run concluded. The control gate is untouched: at the
    parent's cap every span equals its rung reading, twice verified.

T13 THE READING CHECKPOINTS, AND THE DEAD WEIGHT LEAVES BEFORE THE
    COMPARATORS -- a flag, adopted after the fifth run completed
    every science stage (four demotions printed, 433 wide reads at
    zero unmapped, roster 406, both censuses, the imaginary anchor
    reprinted) and was killed by memwatch at 515.3 MB against the
    512 line during the real-quadratic comparator sweep: the sweep's
    transient landed on top of retained state nothing downstream
    still consumed -- the walk's 28076-entry field list, the pin
    pool's orders, the per-prime vectors of every wide read. Two
    cures, both structural. THE DIET: the field list is freed when
    the reading ends, the pin pool when the pin passes, and the
    mapped records collapse to their discriminant list once the
    population is built. THE CHECKPOINT: when the environment names
    FOURTHCELL_CKPT, the reading state -- census rows, exclusions,
    counters, each composite and pin record's winning representative
    -- is written the moment the reading completes, and a later run
    finding the file rebuilds the state instead of re-buying the
    multi-hour leg: rows verbatim, every record re-read through its
    checkpointed representative with the reprint asserted, and the
    whole control gate re-run on the rebuilt state. The wall-clock
    lesson generalizes: a kill inside a multi-hour run buys a
    redesign that makes the retry cheap, never a same-shape rerun.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE BOX. hunter_box(530000) gives t2max 485.7, s2max 243,
      s3max 2059: 2 * 487 * 4119 = 4,011,906 polynomials, 8.0x the
      parent's 503,106 (box volume ~ cap^(5/4)). The enumeration is
      minutes; the class reading dominates the wall.

  (2) THE SUPPLY AND THE BAR, the parent's fit carried forward as a
      GUESS and flagged as one: usable ~ 27 * 5.3^1.34 ~ 250 fields,
      top-band bar ~ 0.0367 / sqrt(250/27) ~ 0.012 -- the parents'
      own bar, at which the frozen alternatives sit apart: the real
      quadratic surplus +0.061 is ~5 bars, the complex cubic's
      consistent-with-1 is ~0. The growth fit's convexity was already
      seen to read low once (the parent's roster guess undershot), so
      the roster may overshoot 250; nothing downstream assumes the
      count.

  (3) DENOMINATORS AND FLOORS, re-checked at the new supply. The
      excess ratio divides by h - 1: 3 at h = 4, nonzero at every
      composite h, no new zero. New strata (h = 10, 12, ...) enter
      only through the frozen strata rule with its MINSTRAT floor;
      within_scale's two-field fallback and the MIN_CELL = 30 curve
      floor ride in; admissibility still wants 10 partial places
      below 250 against a mean of ~13.5, unchanged by the cap.

  (4) INDEX CONVENTION, re-derived from the engine: bands half-open
      [lo, hi), stratum_cells reads lo <= p < hi, the wide band
      [1000, 10000) abuts the top band [630, 1000), 10^4 excluded.

  (5) WALL-CLOCK AND MEMORY, estimated before the run. Class reading
      scales with field count (~25,500 totally real fields projected
      at 5.3x the parent's 4804) times a per-field cost that grows
      with the Minkowski bound (~sqrt(d), ~2.3x at the top): the
      estimate is ~4-6 hours wall, named in the run record against a
      runaway line of 10 hours. Memory: the walk's field tuples
      ~20 MB, one order at a time, ~250 full records ~20 MB;
      projection ~150 MB against the 512 MB ceiling.

  (6) WHAT THE READ CANNOT SAY, fixed now. One signature at one cap:
      a top-band verdict here is a verdict about the totally real
      cubic's place law, not an asymptote claim and not a one-curve
      claim across degrees; the wide band's comparison still rides
      the decay-shape assumption the parent's F3 named, and stays a
      reference line. Meaning is weighed after the print.

THE PREDICTIONS, frozen before the engine ran. Kills name PRINTS.

 P1 THE CONTROL GATE (T7): the three nested censuses reprint the
    parent's distributions exactly -- 24000: {1: 935, 2: 39, 3: 39,
    4: 4, 5: 1, 7: 1}; 50000: {1: 2023, 2: 109, 3: 112, 4: 11, 5: 6,
    6: 1, 7: 1}; 100000: {1: 4192, 2: 290, 3: 267, 4: 21, 5: 18,
    6: 7, 7: 7, 8: 1, 9: 1} -- with 28 non-Galois composite-h fields,
    admissible roster 27 at strata {4: 18, 6: 7, 8: 1, 9: 1}, and the
    four band figures reprint to 5e-5. Kill on any miss.

 P2 THE PINS: the irreducibility screen agrees with the parent's test
    at every strided call (T4); the Frobenius split counter equals
    the parent's per-bin counts at every strided field (T5); the
    box's largest polynomial discriminant sits under 2e8 (T2); every
    certified-field pin place reads principal against the
    ladder-settled lattice (T10) with at least one at p >= 1000; the
    wide unmapped fraction stays under 0.25; the exclusion share
    stays under 1%; every composite-h field's wide span order DIVIDES
    its rung-attested h, demotions printed and carried into the
    census (T12); every composite reading is attested through the
    representative walk -- agreement, a divisibility resolution, or
    an unconfirmed count, each printed (T8, T9, T11). Kill on any
    miss.

 P3 THE ANCHORS: the in-rig imaginary pipeline reprints its parent's
    frozen figures (top band 1.0426 +- 0.0101, cut-1000 raw 1.0875,
    cut-10^4 raw 1.0240) to 5e-5; the in-rig real quadratic pipeline
    reprints 1.0613 +- 0.0069 and raws 1.0606, 1.0246 to 1e-4. Kill
    on any miss.

 P4 THE SPLIT CENSUS, the parent's binned form over the full wide
    population: total variation from nominal (1/6, 1/2, 1/3) smaller
    in the top bin (300-1000) than in the bottom (3-30), each top-bin
    component within 0.02 of nominal. Kill outside.

 P5 THE SYNTHETICS on the wide admissible roster, the parent's
    amended form: uniform within 0.08 of 1 at both cut-ladder ends
    and at each read band; planted recovers 1.30 within 0.06 at the
    smallest cut, non-increasing along the ladder against the
    per-step derived slack max(0.02, twice the joint error), within
    0.06 of 1 in the top band. Kill outside.

 P6 THE VERDICT PRINT, meaning weighed after: the totally real cubic
    top band L +- s at cap 530000 with z vs 1, vs the in-rig
    imaginary, vs the in-rig real quadratic, vs the frozen complex
    cubic 0.9780 +- 0.0123; the wide and combined bands beside it as
    reference lines; the cumulative ladder at the parents' cuts; the
    per-field levels; the supply table at caps 100000 / 265000 /
    530000 with the growth fit; and the non-cyclic census (count and
    profiles) the strata question waits on.

 P7 ROBUSTNESS PRINTS (reference lines, not kills): the half-cap
    (|d| <= 265000) and MIN_TOT = 20 re-reads beside the primary;
    per-field vs pooled gaps with the parents' 0.02 line named.

THE FINDINGS.

 F1 THE CENSUS AT THE DECISIVE CAP (observation; exact over the
    enumerated box under the stated reading laws). 28,072 totally
    real cubic fields to discriminant 530000 (4 excluded, printed),
    h-distribution {1: 23561, 2: 2192, 3: 1697, 4: 247, 5: 134,
    6: 122, 7: 37, 8: 22, 9: 28, 10: 11, 11: 3, 12: 11, 13: 3,
    14: 2, 15: 1, 16: 1}. Non-Galois composite first readings: 439 --
    327 sibling-confirmed, 109 without a settled sibling, and 3 flips
    resolved by divisibility to h = 2 and OUT of the composite set
    (d = 305977, 347977, 360588, each [4, 2]) -- leaving 436, then
    433 after the span demotions (114561, 167593, 415092 from rung 4
    to 2 and out; 210649 from 16 to 4, staying);
    admissible roster 406 at strata {4: 224, 6: 122, 8: 17, 9: 22,
    10: 11, 12: 6, 14: 2, 15: 1, 16: 1}, band strata [4, 6, 8, 9,
    10, 12], top-band bar 0.0100 -- the parents' own. Supply growth
    ~ cap^1.63 across this run's caps: the first fit's 1.34 read the
    convexity low, the third such undershoot in this family. The
    non-cyclic composite count is 27 -- the population the
    no-generating-class question waits on.

 F2 THE VERDICT: THE FOURTH CELL EXHAUSTS, AND THE PLACE LAW HOLDS
    ACROSS THE WHOLE DESIGN (observation; three bands on one
    population against three in-rig comparators). Top band
    [630, 1000): 1.0167 +- 0.0100 -- z +1.67 vs 1, -3.66 vs the
    in-rig real quadratic (1.0613 +- 0.0069), -1.82 vs the in-rig
    imaginary (1.0426 +- 0.0101), +2.44 vs the frozen complex cubic
    (0.9780 +- 0.0123). Wide band [1000, 10^4): 1.0035 +- 0.0026
    against the quadratics' measured 1.0139 +- 0.0016 and
    1.0122 +- 0.0012 at the same band -- z -3.40 and -3.00, measured
    against measured, no shape assumption imported. Combined
    [630, 10^4): 1.0042 +- 0.0025 -- z -3.77 vs imaginary, -3.69 vs
    real quadratic, +1.64 vs 1. The totally real cubic sits ON 1 in
    every band (nothing reaches 2 sigma vs 1) while both quadratic
    populations hold their own surplus, and the separations reach 3
    sigma in the wide and combined bands against both and in the top
    band against the real quadratic (the top-band imaginary
    comparison stops at -1.82): the formless degree-1 place loses the
    surplus at unit
    rank 2 exactly as the complex cubic's does at rank 1, and the
    quadratic place keeps it at rank 0 and rank 1 -- one place law
    across all four cells of the form-by-rank design, the unit rank
    deciding nothing at any measured value. The cumulative ceiling
    is real and decays (1.1562 +- 0.0088 at cut 250).

 F3 WHAT THE TWO FORMLESS CELLS DO AND DO NOT SHARE (observation).
    The totally real top band sits +2.44 sigma above the frozen
    complex cubic point -- the two formless populations agree in
    EXHAUSTING (each within 1.8 sigma of 1, each separated from the
    quadratic populations at 3 sigma and beyond where both are
    measured) and are not resolved from EACH OTHER at verdict
    strength; the complex side has no wide-band read to compare (its
    rig froze primes below 1000). Whether the two formless cells
    share one asymptote is open and unpriced here.

 F4 THE INSTRUMENT RECORD AS POPULATION FACT (property of the rig).
    Of 28,076 fields, 29 read only through a later representative
    and 4 through none; of 439 composite first readings, 3 settled
    sibling-disagreements resolved by divisibility and 4 more
    doubled rungs fell to the wide span -- ~1.6% of the
    science-bearing sliver carried a presentation artifact some
    single instrument would have believed, every one caught by an
    attestation the design added after a control kill. The wide
    reads' unmapped fraction is 0.000 of 266,234 vectors; the split
    census TV falls 0.0672 to 0.0119 with every top-bin component
    inside 0.015 of nominal.

THE PREDICTIONS, WEIGHED.

 P1 PASSES at the gate, twice more (runs five and six): every census
    dict, the 28-with-27 roster, all four band figures to 5e-5.
 P2 PASSES: pins all green (783 places principal, 689 wide, 0
    unmapped; screen and counter pins 5886 and 560); exclusions 4 of
    28,076; span orders divide everywhere, 4 demotions printed.
 P3 PASSES: imaginary to 5e-5, real quadratic to 1e-4.
 P4 PASSES: TV monotone 0.0672 to 0.0119, top bin within 0.015.
 P5 PASSES: uniform 1.0000-1.0036 across cuts and bands; planted
    1.2601 +- 0.0105 at cut 250 (recovery gap 0.040 of the 0.06),
    one rise 0.0155 against slack 0.0272, top band 1.0001.
 P6 THE PRINT: F2's bands and z's; the supply table 27 / 156 / 406
    with the ^1.63 fit.
 P7 half-cap 1.0395 +- 0.0166 (top) and 1.0002 +- 0.0056 (wide),
    same side of every line as the primary; MIN_TOT 20 keeps 396 of
    406 and moves nothing; per-field vs pooled gaps 0.0001-0.0127
    against the parents' 0.02 line.

RUN RECORD. 2026-08-19/20, Windows 11, Python 3,
`FOURTHCELL_CKPT=<scratch>/fourthcell_ckpt.json python
prime/code/memwatch.py python prime/code/explore_ceiling_fourthcell.py`.
One process, CPython, no BLAS. 30,158 checks passed here plus the
imported chains' own, 22,647 s wall (6.3 h: the walk 307 s, the
gated reading 21,849 s, the split census 42 s, the wide reads
430 s), peak working set 357.6 MB against memwatch's 512 MB ceiling.
SIX RUNS STAND BEHIND THIS RECORD, the first five each killed by a
frozen control and each kill becoming a flag: the census gate on a
presentation-dependent exclusion (T9), the wide pin on an unproven
lattice (T10), a settled sibling disagreement (T11), a doubled rung
the sibling walk attested (T12), and memwatch itself at 515.3 MB
during the comparator sweep (T13's diet and checkpoint). The S1-S4
prints of the killed runs match run six digit for digit where their
laws coincide; run five's S5-S7 figures (demotions, roster, censuses,
imaginary anchor) reprint in run six exactly.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import json
import sys
import time
from collections import defaultdict
from math import gcd as gcd_int

sys.stdout.reconfigure(line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_ceiling_realcubic as RC     # installs the whole stack
import explore_ceiling_topband as TB
import explore_ceiling_curve as CV
import explore_cubic_principal as ECP
import explore_cubic_field_shop as CFS
import explore_cubic_transposition as XT
import explore_cubic_split_triple as ST
import explore_class_order as CO
from explore_principal_share import primes_upto

CHECKS = 0

CAP_WIDE = 530000                  # the priced decisive cap
CAP_CTRL = RC.CAP                  # 100000, the control gate (T7)
HALF_WIDE = 265000                 # P7's half-cap
SUPPLY_CAPS = (CAP_CTRL, HALF_WIDE, CAP_WIDE)

GUARD = 2 * 10 ** 8                # T2, derived above
XSIEVE_W = ECP.CR._sieve(15000)    # T2: covers sqrt(guard)
IRR_PIN_STRIDE = 97                # T4: every 97th screened polynomial
SPLIT_PIN_STRIDE = 50              # T5: every 50th non-Galois field

CTRL_CENSUS = {1: 4192, 2: 290, 3: 267, 4: 21, 5: 18, 6: 7, 7: 7,
               8: 1, 9: 1}
CTRL_STRATA = {4: 18, 6: 7, 8: 1, 9: 1}
CTRL_CUM250 = (1.2147, 0.0315)     # frozen, explore_ceiling_realcubic F2
CTRL_TOP = (1.0258, 0.0367)
CTRL_WIDE = (1.0028, 0.0073)
CTRL_COMB = (1.0039, 0.0070)

CUTS = RC.CUTS
TOPBAND = RC.TOPBAND
WIDEBAND = RC.WIDEBAND
COMBBAND = RC.COMBBAND


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


def maximal_order3_ww(a, b, c):
    """T2: the parent's widened routine one box wider -- sieve 15000,
    guard 2e8; byte-identical below 1.6e7 where the loop breaks before
    either bound differs."""
    R = (-c, -b, -a)
    trvec = (3, -a, a * a - 2 * b)
    O = CFS.Order(R, trvec, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    d0 = O.trace_form_disc()
    assert abs(d0) < GUARD, "discriminant out of the widened range"
    for p in XSIEVE_W:
        if p * p > abs(d0):
            break
        if d0 % (p * p) == 0:
            O = CFS.p_maximalize(O, p)
    return O, O.trace_form_disc()


ECP.maximal_order3 = maximal_order3_ww    # T2: the declared swap


def divisors_of(n):
    """All positive divisors of n > 0, by trial division to sqrt(n)."""
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i != n // i:
                out.append(n // i)
        i += 1
    return out


def is_irreducible_fast(a, b, c):
    """T4: the rational root test over the divisors of c -- the same
    test as explore_cubic_field_shop.is_irreducible_cubic, restated
    over the divisor set."""
    if c == 0:
        return False
    for r in divisors_of(abs(c)):
        for s in (r, -r):
            if ((s + a) * s + b) * s + c == 0:
                return False
    return True


def _polymul_mod(u, v, f1, p):
    """(u * v) mod (x^3 + a x^2 + b x + c, p): x^3 reduces by the row
    f1 = (-c, -b, -a) as (const, x, x^2); x^4 = x * x^3 reduces by the
    same row shifted, then its x^3 term reduces again."""
    c0 = (u[0] * v[0]) % p
    c1 = (u[0] * v[1] + u[1] * v[0]) % p
    c2 = (u[0] * v[2] + u[1] * v[1] + u[2] * v[0]) % p
    c3 = (u[1] * v[2] + u[2] * v[1]) % p
    c4 = (u[2] * v[2]) % p
    c1 += c4 * f1[0]
    c2 += c4 * f1[1]
    c3 += c4 * f1[2]
    c0 += c3 * f1[0]
    c1 += c3 * f1[1]
    c2 += c3 * f1[2]
    return (c0 % p, c1 % p, c2 % p)


def root_count_frob(a, b, c, p):
    """T5: distinct roots of x^3 + a x^2 + b x + c mod p as
    deg gcd(x^p - x, f), via square-and-multiply on degree-<3
    residues. Called only at p not dividing the field discriminant,
    where f is squarefree mod p and distinct roots = total roots."""
    f1 = ((-c) % p, (-b) % p, (-a) % p)          # x^3 row
    sq = (0, 1, 0)                               # x
    e = p
    acc = (1, 0, 0)
    while e:
        if e & 1:
            acc = _polymul_mod(acc, sq, f1, p)
        sq = _polymul_mod(sq, sq, f1, p)
        e >>= 1
    # g = x^p - x mod f
    g = (acc[0] % p, (acc[1] - 1) % p, acc[2] % p)
    # deg gcd(f, g) with f monic cubic: do one reduction step by hand.
    # gcd(f, g) where deg g <= 2: standard Euclid on (g, f mod g).
    fpoly = (c % p, b % p, a % p, 1)
    u = list(fpoly)
    v = [g[0], g[1], g[2], 0]

    def deg(w):
        for i in (3, 2, 1, 0):
            if w[i]:
                return i
        return -1

    du, dv = 3, deg(v)
    while dv >= 0:
        inv = pow(v[dv], p - 2, p)
        while du >= dv:
            coef = (u[du] * inv) % p
            for i in range(dv + 1):
                u[du - dv + i] = (u[du - dv + i] - coef * v[i]) % p
            du = deg(u)
        u, v = v, u
        du, dv = dv, deg(v)
    return du


def split_counts_fast(a, b, c, d):
    """T5: the parent's split_type_counts with the Frobenius root
    counter -- same bins, same skip at p | d, same type map."""
    n = [[0, 0, 0] for _ in RC.SPLIT_BINS]
    for p in ECP.ODD_PRIMES:
        if d % p == 0:
            continue
        roots = root_count_frob(a, b, c, p)
        for j, (lo, hi) in enumerate(RC.SPLIT_BINS):
            if lo <= p < hi:
                n[j][0 if roots == 3 else (1 if roots == 1 else 2)] += 1
                break
    return n


def stream_box(cap):
    """T3/T6: the streaming Hunter walk -- the parent's loop order and
    dedup rule, positive-discriminant polynomials only, no Order kept.
    Returns [(ad, d, fp, [(a, b, c), ...])] sorted like the parent's,
    plus the walk counts and the largest polynomial discriminant."""
    t2max, s2max, s3max = CFS.hunter_box(cap)
    del t2max
    n_poly = n_skip = n_red = n_over = n_kept = 0
    n_pin = 0
    max_pd = 0
    by_d = {}
    for s1 in (0, 1):
        for s2 in range(-s2max, s2max + 1):
            for s3 in range(-s3max, s3max + 1):
                n_poly += 1
                a, b, c = -s1, s2, -s3
                pd = CFS.poly_disc3(a, b, c)
                if pd <= 0:
                    n_skip += 1
                    continue
                irr = is_irreducible_fast(a, b, c)
                if n_poly % IRR_PIN_STRIDE == 0:
                    assert irr == CFS.is_irreducible_cubic(a, b, c), \
                        "T4: screen disagrees at (%d,%d,%d)" % (a, b, c)
                    n_pin += 1
                if not irr:
                    n_red += 1
                    continue
                if pd > max_pd:
                    max_pd = pd
                O, d = maximal_order3_ww(a, b, c)
                del O                             # T6: no order survives
                if abs(d) > cap:
                    n_over += 1
                    continue
                n_kept += 1
                fp = dict((p, CFS.shape_at(a, b, c, p))
                          for p in CFS.SMALL_PRIMES if pd % p)
                home = None
                for rec in by_d.setdefault(d, []):
                    if all(fp[p] == rec[0][p] for p in fp if p in rec[0]):
                        home = rec
                        break
                if home is None:
                    by_d[d].append((fp, [(a, b, c)]))
                else:
                    home[0].update(fp)
                    home[1].append((a, b, c))
    out = [(abs(d), d, fp, polys)
           for d in by_d for (fp, polys) in by_d[d]]
    out.sort(key=lambda t: (t[0], t[1]))
    return out, (n_poly, n_skip, n_red, n_over, n_kept, n_pin), max_pd


def control_gate(rows_census, recs, comp):
    """T7/P1: the parent's whole science, reprinted mid-stream on the
    |d| <= 100000 prefix before any deeper field is read."""
    section("CONTROL GATE at |d| <= %d (T7, P1)" % CAP_CTRL)
    RC.census(rows_census)                        # asserts 24000/50000
    hs = defaultdict(int)
    for (d, cyc, h) in rows_census:
        hs[h] += 1
    ok(dict(hs) == CTRL_CENSUS,
       "P1: the 100000 census does not reprint the parent: %s"
       % dict(sorted(hs.items())))
    ok(len(comp) == 28, "P1: %d composite fields, parent read 28"
       % len(comp))
    t1 = time.time()
    mapped = []
    for rec in comp:
        H, piv, k, per_prime = RC.read_field_wide(rec[:10])
        ok(H == rec[6], "P2: span order %s != rung h %d at d=%d"
           % (H, rec[6], rec[0]))
        prof = XT.group_profile(piv, k, H)
        ok(prof is not None and sum(prof.values()) == H,
           "profile control failed at d=%d" % rec[0])
        mapped.append((rec[0], rec[1], rec[2], rec[3], rec[4], rec[5],
                       H, piv, k, per_prime, prof))
    pop = CV.build_pop3(mapped)
    f_r = CV.admissible(pop, CUTS[0], CV.MIN_TOT)
    keep, keepb = CV.frozen_strata(f_r, CUTS, CV.BANDS)
    keep = [h for h in keep if CV.is_composite(h)]
    keepb = [h for h in keepb if CV.is_composite(h)]
    hcnt = defaultdict(int)
    for f in f_r:
        hcnt[f[0]] += 1
    print("  admissible roster: %d of %d, by h %s, wide reads %.1f s"
          % (len(f_r), len(pop), dict(sorted(hcnt.items())),
             time.time() - t1))
    ok(dict(hcnt) == CTRL_STRATA,
       "P1: roster strata %s, parent read %s"
       % (dict(sorted(hcnt.items())), CTRL_STRATA))
    c_r = CV.read_curve(f_r, keep, CUTS, "ctrl")
    got = [("cut-250", (c_r[CUTS[0]][0], c_r[CUTS[0]][1]), CTRL_CUM250)]
    for band, frz, tag in ((TOPBAND, CTRL_TOP, "top"),
                           (WIDEBAND, CTRL_WIDE, "wide"),
                           (COMBBAND, CTRL_COMB, "comb")):
        mu, se, pts, sc, nsc = RC.band_point(f_r, keepb, *band)
        got.append((tag, (mu, se), frz))
    for (tag, (mu, se), (fmu, fse)) in got:
        print("  %-8s %.4f +- %.4f  (parent %.4f +- %.4f)"
              % (tag, mu, se, fmu, fse))
        ok(abs(mu - fmu) < 5e-5 and abs(se - fse) < 5e-5,
           "P1: %s does not reprint: %.4f +- %.4f" % (tag, mu, se))
    print("  the gate passes: the parent's science reprints through"
          " the streaming engine")
    return mapped


def full_reading():
    """S1 + S2: the streaming walk and the gated class reading -- the
    multi-hour leg. Returns the reading state; T13 checkpoints it."""
    section("S1  THE STREAMING BOX -- cap %d (T2, T3, T6)" % CAP_WIDE)
    t1 = time.time()
    fields, walk, max_pd = stream_box(CAP_WIDE)
    (n_poly, n_skip, n_red, n_over, n_kept, n_pin) = walk
    print("  %d polynomials: %d non-positive disc, %d reducible,"
          % (n_poly, n_skip, n_red))
    print("  %d over cap, %d kept -> %d totally real fields"
          % (n_over, n_kept, len(fields)))
    print("  largest polynomial discriminant %d, %d screen pins,"
          " %.1f s" % (max_pd, n_pin, time.time() - t1))
    ok(max_pd < GUARD, "T2: the box outran the widened guard")
    ok(n_skip + n_red + n_over + n_kept == n_poly,
       "the walk's buckets do not sum")
    ok(n_pin > 0, "T4: the screen pin never fired")

    section("S2  THE CLASS READING, ascending |d|, gated (T6, T7)")
    t1 = time.time()
    rows_census = []
    rows_full = []
    recs = []
    excluded = []
    comp = []
    mapped_ctrl = None
    n_read = 0
    n_retry = 0
    n_cert_ng = 0
    n_sib_conf = 0
    n_sib_lone = 0
    n_flip = 0
    comp_rows = []
    for (ad, d, fp, polys) in fields:
        if mapped_ctrl is None and ad > CAP_CTRL:
            comp_c = [r for r in recs if not r[10]
                      and CV.is_composite(r[6])]
            mapped_ctrl = control_gate(rows_census, recs, comp_c)
            print("  ... resuming past the gate, %.1f s in"
                  % (time.time() - t1))
        got = None
        for (a, b, c) in polys:                   # T9: the retry walk
            O, d2 = maximal_order3_ww(a, b, c)
            ok(d2 == d,
               "the rebuilt order's discriminant moved at d=%d" % d)
            got = RC.read_one3(d, False, a, b, c, O)
            if got is not None:
                break
        n_read += 1
        if n_read % 1000 == 0:
            print("  ... %d/%d fields, %.1f s"
                  % (n_read, len(fields), time.time() - t1))
        if got is None:
            excluded.append(d)
            continue
        if (a, b, c) != polys[0]:
            n_retry += 1
        h, kind, gp, rel = got
        cyc = int(round(ad ** 0.5)) ** 2 == ad
        if not cyc and CV.is_composite(h):
            # T11: a composite reading is attested through further
            # representatives; a flip resolves by divisibility.
            reads = [((a, b, c, O), got)]
            for (a2, b2, c2) in [t for t in polys
                                 if t != (a, b, c)][:4]:
                O2, d22 = maximal_order3_ww(a2, b2, c2)
                ok(d22 == d,
                   "the sibling's discriminant moved at d=%d" % d)
                got2 = RC.read_one3(d, False, a2, b2, c2, O2)
                if got2 is None:
                    continue
                reads.append(((a2, b2, c2, O2), got2))
                if len(set(r[1][0] for r in reads)) == 1:
                    break                         # sibling agrees
            hs = [r[1][0] for r in reads]
            if len(reads) == 1:
                n_sib_lone += 1
            elif len(set(hs)) == 1:
                n_sib_conf += 1
            else:
                g = hs[0]
                for x in hs[1:]:
                    g = gcd_int(g, x)
                print("  T11: d=%d settled readings %s, gcd %d"
                      % (d, hs, g))
                if g not in hs:
                    excluded.append(d)
                    continue
                n_flip += 1
                (a, b, c, O), got = next(
                    r for r in reads if r[1][0] == g)
                h, kind, gp, rel = got
        rows_census.append((d, cyc, h))
        rows_full.append((d, cyc, h, a, b, c))
        if not cyc and CV.is_composite(h):
            rec = (d, False, a, b, c, O, h, kind, gp,
                   TB.rel_basis(rel, len(gp)), cyc)
            recs.append(rec)
            comp.append(rec)
            comp_rows.append(len(rows_census) - 1)
        elif kind == 'cert' and not cyc:
            n_cert_ng += 1
            if n_cert_ng % 50 == 1 and len(recs) < 400:
                recs.append((d, False, a, b, c, O, h, kind, gp,
                             TB.rel_basis(rel, len(gp)), cyc))
    print("  class reading: %d read (%d through a later"
          " representative), %d excluded %s, %.1f s"
          % (n_read - len(excluded), n_retry, len(excluded), excluded,
             time.time() - t1))
    ok(len(excluded) <= RC.EXCL_KILL * len(fields),
       "P2: %d of %d fields excluded" % (len(excluded), len(fields)))
    ok(mapped_ctrl is not None, "the control gate never fired")
    print("  non-Galois composite-h fields: %d (%d sibling-confirmed,"
          " %d without a settled sibling, %d flips resolved)"
          % (len(comp), n_sib_conf, n_sib_lone, n_flip))
    del fields                                    # T13: the diet
    counters = dict(n_read=n_read, n_retry=n_retry,
                    n_sib_conf=n_sib_conf, n_sib_lone=n_sib_lone,
                    n_flip=n_flip)
    return (rows_full, rows_census, excluded, comp, comp_rows, recs,
            mapped_ctrl, counters)


def rebuild_rec(d, a, b, c, h_exp, tag):
    """T13: one record re-read through its checkpointed winning
    representative, the reprint asserted."""
    O, d2 = maximal_order3_ww(a, b, c)
    ok(d2 == d, "T13: the rebuilt order's discriminant moved at d=%d"
       % d)
    got = RC.read_one3(d, False, a, b, c, O)
    ok(got is not None and got[0] == h_exp,
       "T13: %s d=%d reprints %s against the checkpointed h=%d"
       % (tag, d, got[0] if got else None, h_exp))
    h, kind, gp, rel = got
    return (d, False, a, b, c, O, h, kind, gp,
            TB.rel_basis(rel, len(gp)), False)


def resume_reading(ck):
    """T13: the reading state rebuilt from the checkpoint -- rows
    verbatim, the composite and pin records re-read through their
    winning representatives, and the control gate re-run whole."""
    section("S1/S2  RESUMED FROM THE T13 CHECKPOINT")
    rows_full = [tuple(r) for r in ck["rows_full"]]
    rows_census = [(d, bool(cy), h)
                   for (d, cy, h, a, b, c) in rows_full]
    excluded = list(ck["excluded"])
    ix = dict(((r[0], r[3], r[4], r[5]), i)
              for i, r in enumerate(rows_full))
    t1 = time.time()
    comp = []
    comp_rows = []
    recs = []
    for (d, a, b, c, h, kind) in ck["comp"]:
        rec = rebuild_rec(d, a, b, c, h, "composite")
        comp.append(rec)
        recs.append(rec)
        comp_rows.append(ix[(d, a, b, c)])
    for (d, a, b, c) in ck["cert"]:
        rec = rebuild_rec(d, a, b, c, 1, "pin")
        ok(rec[7] == 'cert',
           "T13: pin field d=%d no longer certifies" % d)
        recs.append(rec)
    print("  %d composite + %d pin records rebuilt, %.1f s"
          % (len(comp), len(ck["cert"]), time.time() - t1))
    print("  checkpointed reading: %s, %d excluded %s"
          % (ck["counters"], len(excluded), excluded))
    comp_c = [r for r in comp if r[0] <= CAP_CTRL]
    mapped_ctrl = control_gate(
        [r for r in rows_census if r[0] <= CAP_CTRL], recs, comp_c)
    return (rows_full, rows_census, excluded, comp, comp_rows, recs,
            mapped_ctrl, ck["counters"])


def main():
    t0 = time.time()
    ck_path = os.environ.get("FOURTHCELL_CKPT")
    ck = None
    if ck_path and os.path.exists(ck_path):
        with open(ck_path) as fh:
            ck = json.load(fh)
        ok(ck["cap"] == CAP_WIDE,
           "T13: checkpoint cap %s != %d" % (ck["cap"], CAP_WIDE))
    if ck is None:
        state = full_reading()
        if ck_path:
            (rows_full, rows_census, excluded, comp, comp_rows, recs,
             mapped_ctrl, counters) = state
            with open(ck_path, "w") as fh:
                json.dump(
                    {"cap": CAP_WIDE,
                     "rows_full": [list(r) for r in rows_full],
                     "excluded": excluded,
                     "counters": counters,
                     "comp": [[r[0], r[2], r[3], r[4], r[6], r[7]]
                              for r in comp],
                     "cert": [[r[0], r[2], r[3], r[4]]
                              for r in recs if r[7] == 'cert']}, fh)
            print("  T13: the reading is checkpointed to %s" % ck_path)
    else:
        state = resume_reading(ck)
    (rows_full, rows_census, excluded, comp, comp_rows, recs,
     mapped_ctrl, counters) = state

    section("S3  THE SPLIT CENSUS (P4, T5) -- pinned, then Frobenius")
    t1 = time.time()
    tot = [[0, 0, 0] for _ in RC.SPLIT_BINS]
    n_ng = n_spin = 0
    ng = [r for r in rows_full if not r[1]]
    for i, (d, cyc, h, a, b, c) in enumerate(ng):
        s = split_counts_fast(a, b, c, d)
        if i % SPLIT_PIN_STRIDE == 0:
            s_ref = RC.split_type_counts(a, b, c, d)
            assert s == s_ref, "T5: split counter disagrees at d=%d" % d
            n_spin += 1
        n_ng += 1
        for j in range(len(RC.SPLIT_BINS)):
            for t in range(3):
                tot[j][t] += s[j][t]
    tvs = []
    for j, (lo, hi) in enumerate(RC.SPLIT_BINS):
        allp = float(sum(tot[j]))
        fr = [t / allp for t in tot[j]]
        tv = 0.5 * sum(abs(f - nm) for f, nm in zip(fr, RC.NOMINAL))
        tvs.append(tv)
        print("  bin %4d-%4d  split/partial/inert %.4f / %.4f / %.4f"
              "  TV %.4f" % (lo, hi, fr[0], fr[1], fr[2], tv))
    print("  %d non-Galois fields pooled per bin, %d counter pins,"
          " %.1f s" % (n_ng, n_spin, time.time() - t1))
    ok(n_spin > 0, "T5: the counter pin never fired")
    ok(tvs[-1] < tvs[0],
       "P4: the census does not converge, TV %.4f top vs %.4f bottom"
       % (tvs[-1], tvs[0]))
    allp = float(sum(tot[-1]))
    for f, nm, lab in zip((t / allp for t in tot[-1]), RC.NOMINAL,
                          ("split", "partial", "inert")):
        ok(abs(f - nm) < 0.02, "P4: top-bin %s fraction %.4f" % (lab, f))

    section("S4  THE WIDE PIN (T8, T10, P2) -- certified fields first")
    pin_odd = RC.WIDE_ODD[::RC.PIN_STRIDE_WIDE]
    pool = [r for r in recs if r[7] == 'cert' and not r[10]]
    cand = pool[::max(1, len(pool) // (2 * RC.PIN_FIELDS))]
    pin = []
    n_unsettled = 0
    for rec in cand:                              # T10: proven lattice
        if len(pin) >= RC.PIN_FIELDS:
            break
        rel1 = None
        for (box, cap) in RC.RUNGS5:
            rows2 = CFS.harvest_relations(rec[5], rec[8], box=box,
                                          cap=cap)
            if CFS.hermite_order(rows2, len(rec[8])) == 1:
                rel1 = TB.rel_basis(rows2, len(rec[8]))
                break
        if rel1 is None:
            n_unsettled += 1
            print("  d=%d: no rung reaches order 1, skipped" % rec[0])
            continue
        pin.append((rec, rel1))
    ok(len(pin) > 0, "T10: no pin candidate's harvest settles")
    t1 = time.time()
    n_pinp = n_pin_wide = n_none = 0
    for (rec, rel1) in pin:
        old = ST.ODD_PRIMES
        ST.ODD_PRIMES = pin_odd
        try:
            H, piv, k, per_prime = ST.read_field(
                rec[5], rec[2], rec[3], rec[4], rec[0], rec[1],
                rec[8], rel1)
        finally:
            ST.ODD_PRIMES = old
        ok(H == 1,
           "P2: certified field d=%d reads span order %s" % (rec[0], H))
        for (p, kd, vecs) in per_prime:
            if kd != 'partial' or len(vecs) != 1:
                continue
            if vecs[0] is None:
                n_none += 1
                continue
            ok(ST.is_principal(vecs[0], piv, k),
               "P2: a certified field's place at p=%d reads"
               " non-principal" % p)
            n_pinp += 1
            if p >= 1000:
                n_pin_wide += 1
    print("  %d certified fields (%d candidates unsettled), %d places"
          " principal (%d at p >= 1000), %d unmapped, %.1f s"
          % (len(pin), n_unsettled, n_pinp, n_pin_wide, n_none,
             time.time() - t1))
    ok(n_pin_wide > 0, "P2: the pin read no wide place at all")
    del recs, pool, cand, pin                     # T13: the diet

    section("S5  THE COMPOSITE POPULATION, READ WIDE (T8, T12)")
    t1 = time.time()
    ctrl_by_d = dict(((m[0], m[2], m[3], m[4]), m) for m in mapped_ctrl)
    ok(len(ctrl_by_d) == len(mapped_ctrl),
       "two control fields collide on one key")
    mapped = []
    n_none_w = n_vec_w = 0
    n_demote = 0
    for i, rec in enumerate(comp):
        m = ctrl_by_d.get((rec[0], rec[2], rec[3], rec[4]))
        if m is None:
            H, piv, k, per_prime = RC.read_field_wide(rec[:10])
            ok(H is not None and rec[6] % H == 0,
               "P2: span order %s does not divide rung h %d at d=%d"
               % (H, rec[6], rec[0]))
            if H != rec[6]:                       # T12: the demotion
                n_demote += 1
                print("  T12: d=%d rung h %d demoted to span order %d"
                      % (rec[0], rec[6], H))
                ri = comp_rows[i]
                (dd, cy0, h0) = rows_census[ri]
                rows_census[ri] = (dd, cy0, H)
                (dd, cy0, h0, aa, bb, cc) = rows_full[ri]
                rows_full[ri] = (dd, cy0, H, aa, bb, cc)
                if not CV.is_composite(H):
                    continue                      # leaves the roster
            prof = XT.group_profile(piv, k, H)
            ok(prof is not None and sum(prof.values()) == H,
               "profile control failed at d=%d" % rec[0])
            m = (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5],
                 H, piv, k, per_prime, prof)
        for (p, kd, vecs) in m[9]:
            if kd == 'partial' and len(vecs) == 1:
                n_vec_w += 1
                if vecs[0] is None:
                    n_none_w += 1
        mapped.append(m)
    print("  T12: %d rung readings demoted by the wide span" % n_demote)
    frac_none = n_none_w / float(max(n_vec_w, 1))
    print("  %d fields read wide, unmapped fraction %.3f (%d of %d),"
          " %.1f s" % (len(mapped), frac_none, n_none_w, n_vec_w,
                       time.time() - t1))
    ok(frac_none < RC.NONE_KILL, "P2: the wide read thinned by %.3f"
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
    n_ncyc = 0
    for (d, cx, a, b, c, O, H, piv, k, pp, prof) in mapped:
        if not CV.cyclic_profile(
                H, [(i, o) for i, o in
                    enumerate(sum(([oo] * cc for oo, cc in
                                   sorted(prof.items())), []))]):
            n_ncyc += 1
            print("    non-cyclic profile: d=%d h=%d %s"
                  % (d, H, dict(sorted(prof.items()))))
    print("  non-cyclic composite fields: %d (P6's count for the"
          " strata question)" % n_ncyc)
    mdisc = [abs(m[0]) for m in mapped]
    del mapped, mapped_ctrl, ctrl_by_d, comp, comp_rows   # T13: diet

    section("S6  THE WIDE CENSUS AND THE NON-CYCLIC COUNT (P6) --"
            " after T11/T12 resolution")
    for cap in SUPPLY_CAPS:
        hs = defaultdict(int)
        hs_ng = defaultdict(int)
        for (d, cyc, h) in rows_census:
            if d > cap:
                continue
            hs[h] += 1
            if not cyc:
                hs_ng[h] += 1
        print("  cap %6d: %5d totally real, h %s" %
              (cap, sum(hs.values()), dict(sorted(hs.items()))))
        print("             non-Galois         h %s"
              % dict(sorted(hs_ng.items())))

    section("S7  THE ANCHORS (P3) -- both degree-2 comparators")
    plist = primes_upto(CO.PCAP)
    f_i, keep_i, keep_ib = RC.deg2_side(-1, 4000, "imaginary", plist)
    c_i = CV.read_curve(f_i, keep_i, CUTS + CV.EXT_CUTS, "imag")
    mu_it, se_it, _, _, _ = RC.band_point(f_i, keep_ib, *TOPBAND)
    ok(abs(c_i[1000][0] - RC.IMAG_CUT1000) < 5e-5,
       "P3: imaginary cut-1000 reprint off: %.4f" % c_i[1000][0])
    ok(abs(c_i[10000][0] - RC.IMAG_CUT10K) < 5e-5,
       "P3: imaginary cut-10^4 reprint off: %.4f" % c_i[10000][0])
    ok(abs(mu_it - RC.IMAG_TOP[0]) < 5e-5
       and abs(se_it - RC.IMAG_TOP[1]) < 5e-5,
       "P3: imaginary top band reprint off: %.4f +- %.4f"
       % (mu_it, se_it))
    print("  imaginary anchors reprint to 5e-5")
    f_q, keep_q, keep_qb = RC.deg2_side(+1, RC.DBOUND_REAL, "real quad",
                                        plist)
    c_q = CV.read_curve(f_q, keep_q, CUTS + CV.EXT_CUTS, "realq")
    mu_qt, se_qt, _, _, _ = RC.band_point(f_q, keep_qb, *TOPBAND)
    ok(abs(c_q[2500][0] - RC.REAL_CUT2500) < 1e-4,
       "P3: real quad cut-2500 reprint off: %.4f" % c_q[2500][0])
    ok(abs(c_q[10000][0] - RC.REAL_CUT10K) < 1e-4,
       "P3: real quad cut-10^4 reprint off: %.4f" % c_q[10000][0])
    ok(abs(mu_qt - RC.REAL_TOP[0]) < 1e-4
       and abs(se_qt - RC.REAL_TOP[1]) < 1e-4,
       "P3: real quad top band reprint off: %.4f +- %.4f"
       % (mu_qt, se_qt))
    print("  real quadratic anchors reprint to 1e-4")
    comp2 = {}
    for (tag, ff, kb) in (("imag", f_i, keep_ib), ("realq", f_q,
                                                   keep_qb)):
        for band in (TOPBAND, WIDEBAND, COMBBAND):
            mu, se, pts, sc, nsc = RC.band_point(ff, kb, *band)
            comp2[(tag, band)] = (mu, se)
            RC.print_band(tag, band[0], band[1], mu, se, pts, sc, nsc)

    section("S8  THE SYNTHETIC CONTROLS (P5) on the wide roster")
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

    section("S9  P6 -- THE VERDICT PRINT")
    c_r = CV.read_curve(f_r, keep, CUTS, "tot real cubic")
    print("  cumulative: %s"
          % "  ".join("%d: %.4f +- %.4f" % (c, c_r[c][0], c_r[c][1])
                      for c in CUTS))
    for band in (TOPBAND, WIDEBAND, COMBBAND):
        mu, se, pts, sc, nsc = RC.band_point(f_r, keepb, *band)
        RC.print_band("tot real", band[0], band[1], mu, se, pts, sc,
                      nsc)
        z1 = (mu - 1.0) / se
        zi = CV.zdiff((mu, se), comp2[("imag", band)])
        zq = CV.zdiff((mu, se), comp2[("realq", band)])
        line = ("    z vs 1 %+.2f   vs imaginary %+.2f   vs real quad"
                " %+.2f" % (z1, zi, zq))
        if band == TOPBAND:
            line += "   vs frozen complex cubic %+.2f" % CV.zdiff(
                (mu, se), RC.DEG3_TOP)
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

    section("S10  THE SUPPLY TABLE (P6)")
    usable = []
    for cap in SUPPLY_CAPS:
        sub = [f for f, md in zip(pop, mdisc) if md <= cap
               and f in f_r]
        usable.append(len(sub))
        m2, s2_, pts, sc, nsc = RC.band_point(sub, keepb, *TOPBAND)
        bar = "%.4f" % s2_ if s2_ else "unreadable"
        print("  cap %6d: %3d usable fields, top-band bar %s"
              % (cap, len(sub), bar))
    if usable[0] > 0 and usable[-1] > usable[0]:
        import math
        expo = (math.log(usable[-1] / float(usable[0]))
                / math.log(SUPPLY_CAPS[-1] / float(SUPPLY_CAPS[0])))
        print("  supply growth ~ cap^%.2f across this run's caps"
              % expo)

    section("S11  P7 -- ROBUSTNESS PRINTS")
    f_h = [f for f, md in zip(pop, mdisc)
           if md <= HALF_WIDE and f in f_r]
    for band in (TOPBAND, WIDEBAND):
        mu, se, pts, sc, nsc = RC.band_point(f_h, keepb, *band)
        if mu is not None:
            RC.print_band("half-cap", band[0], band[1], mu, se, pts,
                          sc, nsc)
    f_20 = CV.admissible(pop, CUTS[0], CV.MIN_TOT_HARD)
    print("  MIN_TOT 20 keeps %d of %d" % (len(f_20), len(f_r)))
    for band in (TOPBAND, WIDEBAND):
        mu, se, pts, sc, nsc = RC.band_point(f_20, keepb, *band)
        if mu is not None:
            RC.print_band("MIN_TOT 20", band[0], band[1], mu, se, pts,
                          sc, nsc)

    section("SUMMARY")
    print("  %d checks passed here (plus the imported chains' own),"
          " %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
