"""
The score-information criterion: WHICH class-constant losses break
the data-free universality of the exact reader's optimum -- is
"the loss reads the stream" the right law, and in what sense?

THE QUESTION
------------
explore_prediction_door.py showed that one loss outside the
trace-geometry family (the next-side prediction score) empties the
universal intersection that every trace-geometry loss had kept
nonempty, and explore_bandwidth_dial.py showed the break needs no
bandwidth (one future bit anywhere suffices; zero bits restore
universality). Both results are one species pair. This experiment
asks for the LAW behind them:

  CANDIDATE CRITERION. A class-constant loss opens the door --
  empties the universal intersection -- iff it READS THE STREAM:
  iff it is not a function of committed-trace geometry alone.

The candidate needs a non-degeneracy clause (a loss can read the
stream in its VALUES while never moving a comparison), and the
experiment's real product is the honest form of both clauses: what
"reads the stream" and "non-degenerate" must mean for the criterion
to survive the species below.

  Q1  Do straight prediction variants (delayed-side, next-digit-
      class) break universality the way the next-side loss does?
  Q2  Do the engineered counterexample attempts -- losses that read
      the stream yet are built to KEEP a universal optimum --
      succeed, and which clause does each success force?
  Q3  Do the degeneracy controls print as degenerate under the
      operational tests, never as universality verdicts?

HAND LEMMAS (fixed before the engine)
-------------------------------------
HL1 THE PAST-READER LEMMA (refutes the candidate as literally
    stated, before any engine). The FIXED-TARGET loss scores each
    counted state's wider-side guess at the next-side cut (the
    mediant of J_n) against the CONSTANT target R; the loss is the
    number of L-guesses. It is not a function of trace geometry
    alone -- the cuts are stream data, so two streams with
    identical demand geometry and different digit directions score
    the same committed trace differently -- but it consults only
    the stream's PAST (the cuts), no future bit. And it keeps a
    universal optimum: the four policies with both patiences
    infinite never receive a reference cell (run_reader gives them
    ref_t = ref_c = None), never commit, and hold the root cell
    forever; the root's right endpoint is infinite, so the
    extractor guesses R at every cut, and the REFUSER class scores
    0 on every row -- universal. Hence the honest first axis is
    WHICH stream data the evaluator consults: GEOMETRY (cell
    lengths) / PAST (the cuts) / FUTURE (truth bits unresolved by
    the committed prefix). The surviving candidate: the door opens
    iff the loss consults FUTURE bits and is non-degenerate.
HL2 THE SHIFT-DEGENERACY LEMMA. The row-constant shift
    L = deficit + c_r (c_r policy-free -- here the count of R's in
    the row's truth string, a genuine future read) preserves every
    within-row comparison: (num + c*den)/den = num/den + c, the
    infinity flag untouched. Identical per-row PREORDERS on
    classes, identical argmins, universality preserved. So
    degeneracy must be defined at the DISCRIMINATION level -- the
    family of induced per-row preorders -- not the value level.
HL3 THE FORCING LEMMA (for the deficit-primary attempt). Under the
    order (deficit, then next-side misses), the three dbl rows'
    deficit argmin is the universal class U alone
    (explore_bandwidth_dial.py, the anchor partition), so the only
    candidate universal class is U; universality holds iff U
    attains the within-argmin-set miss minimum on each of the
    other six rows. Not hand-decidable: U contains the greedy
    policies, which guess even the last bit wrong on id/phi and
    id/theta8, but the in-set rivals' miss counts are unknown.
HL4 DELAYED WELL-DEFINEDNESS. For horizon h, the cut m_{n+h-1} is
    interior to J_{n+h-1}, which sits inside J_n, which sits
    inside C_n (the containment invariant), so the cut is strictly
    interior to the committed cell and the wider-side guess is
    well-defined. Scored steps n with n+h-1 < the horizon:
    112-(h-1) bits.
HL5 THE COINCIDENCE LEMMA. The maps id and dbl commute with the
    mediant (dbl: (2(a+c), b+d) both ways), sq does not
    ((a+c)^2 vs a^2+c^2 cross terms). So the next-digit-class cut
    (the image of the cylinder mediant -- the boundary between the
    next-digit-1 child and the next-digit->=2 children, pushed
    through the map) equals the next-side cut on the seven id and
    dbl rows and differs exactly on sq/phi and sq/sqrt2.

THE SPECIES SLATE (frozen at design)
------------------------------------
S1  DELAYED-SIDE, horizon h in {2, 4, 8}: guess the wider side of
    C_n at the cut m_{n+h-1}; truth = the stream's side there
    (h = 1 is exactly explore_prediction_door.py's loss -- the
    reproduction is control C1). Consults the FUTURE.
S2  NEXT-DIGIT-CLASS: the cut is the image of the cylinder
    mediant (HL5); truth by deepening. The window's own next-digit
    question on every row; new content exactly on the sq rows.
    Consults the FUTURE.
S3  PERVERSE (anti-agreement): the loss is the number of HITS at
    the next-side cuts -- minimized by maximizing misses; the same
    future bits, direction reversed. The refuser is worst on
    id/sqrt3 (constant-R truth), and perfect anti-prediction is
    the complement of perfect prediction, which the eight perfect
    rows achieve by different policies -- the mirrored
    intersection is plausibly empty but not hand-decidable.
    GENUINELY OPEN. Consults the FUTURE.
S4  DEFICIT-PRIMARY COMPOSITE (counterexample attempt A): the
    order (deficit, then next-side misses) -- future bits act only
    below the geometry primary. HL3 forces the verdict through U;
    GENUINELY OPEN. Consults the FUTURE, in the tiebreak only.
S5  FIXED-TARGET (counterexample attempt B): HL1's loss, proved to
    keep universality via the refuser. Consults the PAST only.
S6  ROW-CONSTANT SHIFT (degeneracy control): HL2's loss, proved to
    keep universality; consults the FUTURE in value only. Must
    print DEGENERATE, never a universality verdict.

OPERATIONAL DEGENERACY TESTS (the non-degeneracy clause, made
printable): per species and row, (i) is the induced preorder on
classes identical to the deficit's? (catches S6); (ii) the
toothlessness watch -- the count of distinct loss values (a row
with one value discriminates nothing there); (iii) the
geometry-pair census -- within-row class pairs with identical
counted length sequences that the species separates (the direct
beyond-geometry witness; if no such pair exists at scope the test
is vacuous and is reported as such). Mirroring some trace-geometry
loss other than the deficit is not tested; the verdict names only
what these three tests decide.

PREDICTIONS (fixed before the run)
----------------------------------
P1  The controls pass (C1-C5 below); a failed control stops the
    read.
P2  S1 (every h) and S2 empty the universal intersection under
    both orders. MARKED TRANSPLANT: imported from the
    next-side/single-bit species pair; a keep is a first-class
    outcome, not an anomaly.
P3  S5 keeps universality via the refuser and prints
    non-degenerate under the operational tests -- the engine
    confirmation of HL1, fixing the criterion's first axis at
    consults-the-future.
P4  S3 and S4 are genuinely open; no outcome predicted. The
    observables are the universal-intersection prints and the
    discrimination watches. Candidate readings if either KEEPS
    universality, named now and weighed only after the run: S3 a
    direction clause, S4 an order-of-consultation clause (primary
    vs tiebreak).
P5  A species toothless on a row gets no universality weight from
    that row; a species toothless everywhere gets no universality
    verdict at all.

EXPERIMENTS
-----------
E1  CONTROLS. C1 the delayed scorer at h = 1 reproduces every
    stored (class, row) miss count. C2 the S2 cuts equal the
    next-side cuts on the seven id/dbl rows (exact fraction
    equality per step) with identical truth strings, and differ on
    the sq rows (count printed); interiority asserted everywhere.
    C3 the refuser class exists: the class of (st, ss, INF, INF)
    holds the root cell at every counted step on every row and its
    fixed-target loss is 0 on all rows (HL1's premise and
    conclusion). C4 the shift's per-row argmin sets equal the
    deficit's (HL2). C5 the deficit baseline reproduces the known
    anchor: exactly one universal class, and the argmin-set row
    partition has the three known blocks (the five-row block, the
    three dbl rows, sq/sqrt2 alone) with argmin sizes 5/1/11.
E2  THE SPECIES CENSUS: per species -- per-row minimum / spread /
    distinct-value count / argmin sizes; the universal
    intersection under the species' own order and, for
    integer-valued species, under the deficit-tiebreak composite;
    the row partition by argmin sets.
E3  THE DISCRIMINATION TABLE: per species x row, the
    preorder-vs-deficit flag and the toothlessness count; the
    degeneracy verdict per species.
E4  THE CRITERION TABLE: species x consults(geometry/past/future)
    x degeneracy x universality -- the criterion's truth table at
    scope, with mechanical violation lists (future-consulting
    non-degenerate species that keep universality; non-future or
    degenerate species that break it).
E5  THE GEOMETRY-PAIR CENSUS: within-row identical-geometry class
    pairs and which species separate one; vacuity reported.

EXTENSIONS (designed after reading the E1-E5 prints, before their
code ran; each records its expectation here, fixed pre-run)
E6  THE TIE MECHANISM. E2/E3 printed S4 as deficit-mirroring (the
    miss tiebreak never fires) and E5 printed 475 within-row
    identical-geometry pairs separated by NO species. Both would
    follow from one fact: a within-row VALUE tie (deficit or
    geometry signature) is a TRACE tie -- the tied classes hold
    identical committed cells on that row and differ only
    elsewhere. Per row, count deficit-tied pairs vs trace-identical
    deficit-tied pairs, and geometry-tied pairs vs trace-identical
    geometry-tied pairs. Expectation (fixed pre-run): all tied
    pairs are trace-identical. ADDENDUM (designed after the count
    printed 467 of 475): name the residual non-identical tied
    pairs -- row and class ids -- so they are inspectable.
E7  THE REPRESENTABILITY TABLE + THE MIXING WITNESS. The refuser
    holds the same all-root trace on every row -- a CROSS-ROW
    geometry collision -- so row-uniform-geometry-representability
    is decidable at scope: group (class, row) points by geometry
    signature, check each species for constancy on every collision
    group. Expectation (fixed pre-run): S0 and S5 representable;
    S1, S2, S3, S4, S6 not (the refuser's next-side misses differ
    by row). Also the mixing mechanism behind S5-composite's
    emptiness: print the refuser's per-row membership in the pure
    and composite argmins (expected: unique pure argmin on some
    rows, deficit-eliminated from fat zero-value ties on others --
    two universality-keepers mixing to a breaker because their
    witnesses are incompatible). ADDENDUM (designed after the first
    run printed 11 multi-row collision groups, among them the
    greedy class U sharing its full 112-cell geometry on id/phi and
    sq/phi -- verified independently: the sq/phi cells are the
    exact +1 translates of the id/phi cells, the golden identity
    phi^2 = phi + 1 acting as translation in the cover tree): the
    TWIN CENSUS -- per row pair, how many classes hold identical
    geometry columns on both rows; a row pair where ALL classes do
    would be un-splittable by any row-uniform geometry loss.
    Expectation: no full-column twin pair (S5, representable at
    scope, splits id/phi from sq/phi in its partition).
E8  THE GEOMETRY BREAKER. Is the break about stream data at all at
    the preorder level? Search the band-indicator family -- loss 0
    if the row's deficit lies in a value band, else 1, the band
    row-uniform -- for a specimen with no toothless row (every
    row's in-band set neither empty nor full) and an EMPTY
    universal intersection. Exact search in rank space: pooled
    sort of the 342 per-(class, row) deficit values (the full
    lexicographic order, infinity flags included), per-row
    prefix bitmasks, scan all rank bands. Expectation (marked
    hunch): specimens exist -- U carries every row's minimum
    deficit, so interior bands dodge U and catch different classes
    on different rows. A found specimen is a row-uniform function
    of trace geometry, non-degenerate, with an empty intersection:
    the necessity direction of any reads-the-stream criterion
    falls, and the family's universality re-attributes to its
    MONOTONE (tightness-extremal) structure.

FINDINGS (from the runs; all controls green first)
--------------------------------------------------
E1  All five controls pass. The universal deficit class U is the
    greedy class (class #0, patience-0 members); the digit cuts
    differ from the next-side cuts at all 112 steps on both sq
    rows and coincide exactly on the seven id/dbl rows (HL5
    realized at scope).

E2  EVERY STRAIGHT-PREDICTION SPECIES BREAKS, IN BOTH DIRECTIONS
    OF USE. S1 (h = 2, 4, 8), S2, and S3 all print an EMPTY
    universal intersection under both the pure and the
    deficit-tiebreak composite orders — delayed horizons, the
    digit-class target, and the perverse direction (no universal
    anti-predictor exists) all behave like the next-side loss. The
    counterexample attempts and controls keep universality as
    proved: S4 NONEMPTY (U inside), S5 pure NONEMPTY (the refuser),
    S6 NONEMPTY — but S5's COMPOSITE order (fixed-target, then
    deficit) is EMPTY: two universality-keepers mix into a breaker.
    Partitions: S1 fully discrete at h = 2, 4 (nine blocks; h = 8
    merges dbl/phi with dbl/fib); S3 fully discrete; S2 merges
    exactly {id/phi, sq/phi} — rows sharing a STREAM become
    argmin-indistinguishable when the target is the stream's own
    digit question. Aside: the aperiodic fib row's best miss count
    FALLS with delay (47 at h=1, then 42, 31, 30 over slightly
    shorter windows).

E3  THE DEGENERACY VERDICTS. S4 and S6 print DEFICIT-MIRRORING:
    their per-row preorders are IDENTICAL to the deficit's on all
    nine rows — S4's miss tiebreak never fires anywhere (see E6
    for the mechanism). All prediction species and S5 are
    non-degenerate; no species has a toothless row. (One per-row
    mirroring coincidence: S1 h=8 matches the deficit's preorder
    on sq/sqrt2 alone.)

E4  THE CRITERION TABLE AT SCOPE: future-consulting +
    non-degenerate -> EMPTY (five species); past-consulting (S5
    pure) -> NONEMPTY; degenerate (S4, S6) -> NONEMPTY; both
    mechanical violation lists empty at the species'-own-order
    level. The necessity direction dies elsewhere: E8 and the S5
    composite.

E5  475 within-row identical-geometry class pairs — and NO species
    separates a single one. Within a row, geometry exhausts
    everything every loss tried can see.

E6  THE TIE MECHANISM: 467 of the 475 tied pairs (deficit ties =
    geometry ties here) are TRACE-IDENTICAL on the tied row — a
    value tie is almost always a trace tie, which is exactly why
    S4's tiebreak never fires and no species separates E5's pairs.
    The 8 residual pairs all sit on sq/sqrt2 among the six classes
    holding INFINITE cells there (#4/#9/#14/#19 vs #20/#21):
    length-identical, position-different — and the wider-side
    extractor guesses R outright on any infinite right side, so
    every species scores them equally anyway.

E7  REPRESENTABILITY AND THE GOLDEN NEAR-TWIN. 83 geometry
    collision groups, 11 spanning rows. THE TWIN CENSUS: id/phi
    and sq/phi share identical full geometry columns for 32 OF 38
    CLASSES — the golden identity phi^2 = phi + 1 acts as the +1
    translation in the cover tree (verified on U: its sq/phi cells
    are the exact translates, (21/13, 34/21) -> (34/13, 55/21));
    every other row pair collides at 1-2 classes only (#20/#21 —
    the refuser and its near-refuser sibling; verified), and no
    pair is a full twin. S0 and S5 are
    REPRESENTABLE at scope (constant on every collision group);
    S1, S2, S3, S4, S6 are NOT — witnessed by U scoring
    differently across the near-twin pair (S2 by a cross-class
    collision instead). So at this scope, beyond-geometry reading
    is witnessable only CROSS-ROW, and its canonical witness is
    structural, not statistical. Note S5's two classifications
    DIVERGE BY LEVEL: its evaluator consults the cuts (the E4
    "past" column is design-level), yet its values are consistent
    with a row-uniform geometry function at scope — they agree on
    every collision group, the 32 golden-twin columns included,
    where the cells are exact translates but the cuts differ (the
    sq cut is a double-depth convergent, not the id cut's
    translate), so the cuts leave no witness here. The criterion
    verdict below is unaffected: necessity dies at E8 on
    representable losses regardless of S5's level. THE MIXING WITNESS: the refuser
    is the UNIQUE pure fixed-target argmin on id/phi and id/sqrt2
    but is ejected from the composite argmin on id/sqrt3,
    id/theta8, sq/phi, dbl/sqrt2 (deficit-eliminated inside fat
    zero-value ties) — incompatible witnesses, so the mix breaks.

E8  THE GEOMETRY BREAKER EXISTS, PLENTIFULLY. Over the 117 pooled
    distinct deficit values, 146 of 6903 order-interval bands are
    CLEAN BREAKERS: every row's in-band set neither empty nor
    full, universal intersection EMPTY — a row-uniform function
    of the DEFICIT VALUE ALONE, non-degenerate (two values on
    every row, tie structure coarser than the deficit's own),
    with no universal optimum. First specimen: rank band [1, 85],
    five partition blocks — this one happens to merge
    {id/phi, sq/phi}; only a FULL twin would force that merge (a
    geometry function can still split the near-twin pair through
    its six non-colliding classes, as S5's partition in fact does).

READING. The candidate criterion — "the door opens iff the loss
reads the stream" — is DEAD IN BOTH DIRECTIONS, and what replaces
it is sharper. Sufficiency fails at the value level: S6 and S4
consult future bits in their values yet keep universality because
their induced per-row preorders never move — degeneracy is a
preorder-family property (HL2), and the non-degeneracy clause
belongs there. Necessity fails outright: the band-indicator
specimens break universality reading NOTHING but the deficit
value, and the S5 composite breaks it by mixing two keepers with
incompatible witnesses. EMPTINESS OF THE UNIVERSAL INTERSECTION IS
THEREFORE NOT A STREAM-DATA PHENOMENON — breaks are generic, and
the thing that needs explaining is the KEEP: the trace family kept
universality through its monotone (tightness-extremal) structure,
where pointwise dominance hands every row the same witness, just
as the refuser's extremal position hands one to the fixed-target
loss. (The keep question is settled by explore_keep_law.py: both
extremal poles are theorems, monotone losses keep through them,
clean bands keep iff they contain a class's cross-row rank hull,
and the extremal law is sufficiency-only.) What survives at scope
as the honest law: (i) the
SUFFICIENCY PATTERN — every non-degenerate loss tried whose TOP
order consults future bits breaks universality (five species here,
plus the next-side loss and its single-bit atlas,
explore_prediction_door.py + explore_bandwidth_dial.py); (ii) the
DISCRIMINATION DEFINITION — universality verdicts are functions of
the preorder family alone; (iii) the CONTENT SIGNATURE — within a
row geometry exhausts the visible (E5/E6), so beyond-geometry
reading is witnessed only at CROSS-ROW COLLISION PAIRS, and the
golden near-twin pair id/phi ~ sq/phi is its canonical site: no
geometry function can score a colliding class differently on the
two rows, and S1, S3, S4, S6 all do (U's scores differ across the
pair). The litmus is CLASS-level, not partition-level — row-level
splitting of the near-twin stays open to geometry losses through
the six non-colliding classes (S5's partition splits it), while
the merges observed here (S0, E8's first specimen, and S2 — whose
target the twin streams share) are at-scope facts, not forced. Predictions against
outcomes: P1-P3, P5 as predicted (the P2 transplant survived
straight); P4 resolved — S3 breaks (no direction clause needed)
and S4 keeps but DEGENERATELY, so the order-of-consultation
question was never actually tested at this scope: deficit ties
are trace ties, and a tiebreak below the deficit has nothing to
act on.
Tier: HL1, HL2, HL4, HL5 are proved (HL3's forcing likewise, its
premise from explore_bandwidth_dial.py); everything else is exact
and exhaustive at the stated scope (this policy space, these nine
rows, these loss species, horizon 120) only; the surviving
criterion statements are patterns at scope, not rules.

Run record: run 1 (E1-E5) exit 0, all controls green, 4.4s; run 2
(E6-E8 added) exit 0, E1-E5 output unchanged, 4.7s; run 3 (E6
residual-pair print + E7 twin census added) exit 0, all else
unchanged, 4.6s.

DESIGN
------
Everything heavy is imported verbatim from
explore_prediction_door.py: streams, cylinders, images, the reader
engine, the truth machinery, the behavioral quotient (38 classes
from 100 policies, per-class counted cells, next-side hit vectors,
deficits). Index convention re-derived from that engine: counted
step n in [8, 120) has scored index i = n - 8; cells[i], cuts[i],
sides[i] all use it, and C1's h = 1 reproduction is the convention's
in-engine check. New machinery here: a generic deepening truth
resolver for arbitrary interior cuts (S2), the delayed scorer (S1),
and the census/discrimination framework (generic over comparator).
Exact arithmetic throughout; no floats in any comparison.
"""

import time
from fractions import Fraction
from functools import cmp_to_key

from explore_prediction_door import (
    N0, HORIZON, DEEP, ROWS, fmt_row, fmt_pol, cmp_lex, frac_eq, lt,
    mediant, MAPS, cylinders, stream_digits, build_images,
    truth_targets, build_classes, guess_side, check,
)

NBITS = HORIZON - N0          # 112 counted bits, indices 0..111
HS = [2, 4, 8]                # delayed-side horizons (h = 1 = control)

ROOT_IV = ((0, 1), (1, 0))    # the uncommitted root interval


# ----------------------------------------------------------------- #
# truth machinery for new cuts
# ----------------------------------------------------------------- #

def truth_for_cuts(J_deep, cuts):
    """Truth sides of the image point relative to arbitrary interior
    cuts, one per counted step, by deepening (the first later image
    interval that excludes the cut pins the side)."""
    sides = []
    for i, n in enumerate(range(N0, HORIZON)):
        lo, hi = J_deep[n]
        cut = cuts[i]
        assert lt(lo, cut) and lt(cut, hi), "cut not interior to J"
        side = None
        for m in range(n + 1, len(J_deep)):
            mlo, mhi = J_deep[m]
            if not lt(cut, mhi):
                side = "L"
                break
            if not lt(mlo, cut):
                side = "R"
                break
        assert side is not None, "truth unresolved at available depth"
        sides.append(side)
    return sides


def digit_cuts(row):
    """The next-digit-class cuts: the image of each counted
    cylinder's mediant (the digit-1 / digit->=2 boundary pushed
    through the row's map)."""
    map_name, stream_name = row
    cyl = cylinders(stream_digits(stream_name, DEEP))
    f = MAPS[map_name]
    return [f(mediant(*cyl[n])) for n in range(N0, HORIZON)]


# ----------------------------------------------------------------- #
# species scorers
# ----------------------------------------------------------------- #

def cell_guess(cell, cut):
    """The wider-side guess of a committed cell at a cut, with the
    interiority assert of HL4."""
    clo, chi = cell
    assert lt(clo, cut) and (chi[1] == 0 or lt(cut, chi)), \
        "cut not interior to committed cell"
    return guess_side(clo, chi, cut)[0]


def delayed_miss(cls, row, cuts, sides, h):
    """S1: misses of the state at step n guessing the side at the
    cut of step n+h-1."""
    cells = cls["rows"][row]["cells"]
    miss = 0
    for i in range(NBITS - (h - 1)):
        if cell_guess(cells[i], cuts[i + h - 1]) != sides[i + h - 1]:
            miss += 1
    return miss


def cut_miss(cls, row, cuts, sides):
    """Misses of each state at its own step's cut against the given
    truth string (S2 with the digit cuts; S5 with constant truth)."""
    cells = cls["rows"][row]["cells"]
    miss = 0
    for i in range(NBITS):
        if cell_guess(cells[i], cuts[i]) != sides[i]:
            miss += 1
    return miss


# ----------------------------------------------------------------- #
# generic census machinery
# ----------------------------------------------------------------- #

def cmp_int(a, b):
    return -1 if a < b else (1 if a > b else 0)


def cmp_pair_lex_int(a, b):
    """(deficit triple, int) lexicographic -- the S4 order."""
    c = cmp_lex(a[0], b[0])
    return c if c != 0 else cmp_int(a[1], b[1])


def cmp_int_then_lex(a, b):
    """(int, deficit triple) lexicographic -- the composite order
    for integer-valued species."""
    c = cmp_int(a[0], b[0])
    return c if c != 0 else cmp_lex(a[1], b[1])


def census(values, cmpf):
    """values: per class index, dict row -> comparable value.
    Returns per-row argmin sets, distinct counts, the universal
    intersection, and the row partition by argmin set."""
    ncls = len(values)
    argmin = {}
    distinct = {}
    for row in ROWS:
        vals = [values[ci][row] for ci in range(ncls)]
        best = min(range(ncls), key=lambda ci: cmp_to_key(cmpf)(vals[ci]))
        argmin[row] = frozenset(
            ci for ci in range(ncls) if cmpf(vals[ci], vals[best]) == 0)
        order = sorted(range(ncls), key=lambda ci: cmp_to_key(cmpf)(vals[ci]))
        d = 1
        for a, b in zip(order, order[1:]):
            if cmpf(vals[a], vals[b]) != 0:
                d += 1
        distinct[row] = d
    uni = frozenset.intersection(*(argmin[row] for row in ROWS))
    blocks = {}
    for row in ROWS:
        blocks.setdefault(argmin[row], []).append(row)
    return {"argmin": argmin, "distinct": distinct, "uni": uni,
            "partition": sorted(blocks.values(), key=len, reverse=True)}


def preorder_vs(values, cmpf, ref_values, ref_cmpf):
    """Per row: does the species' induced preorder on classes equal
    the reference's? Returns dict row -> bool."""
    ncls = len(values)
    out = {}
    for row in ROWS:
        same = True
        for a in range(ncls):
            for b in range(a + 1, ncls):
                s1 = cmpf(values[a][row], values[b][row])
                s2 = ref_cmpf(ref_values[a][row], ref_values[b][row])
                if s1 != s2:
                    same = False
                    break
            if not same:
                break
        out[row] = same
    return out


def fmt_partition(part):
    return " | ".join("{" + ",".join(fmt_row(r) for r in blk) + "}"
                      for blk in part)


# ----------------------------------------------------------------- #
# the run
# ----------------------------------------------------------------- #

def main():
    t0 = time.time()
    print("THE SCORE-INFORMATION CRITERION -- which losses open the"
          " data door")
    print("rows: %s" % ", ".join(fmt_row(r) for r in ROWS))
    imgs = build_images(DEEP)
    targets = {row: truth_targets(imgs[row]) for row in ROWS}
    classes = build_classes(imgs, targets)
    ncls = len(classes)
    print("behavior classes: %d" % ncls)
    print()

    # ---- species values ------------------------------------------ #
    deficit_vals = [{row: c["rows"][row]["deficit"] for row in ROWS}
                    for c in classes]
    delayed_vals = {h: [{row: delayed_miss(c, row, targets[row][0],
                                           targets[row][1], h)
                         for row in ROWS} for c in classes]
                    for h in HS}

    dcuts = {row: digit_cuts(row) for row in ROWS}
    dsides = {row: truth_for_cuts(imgs[row], dcuts[row]) for row in ROWS}
    digit_vals = [{row: cut_miss(c, row, dcuts[row], dsides[row])
                   for row in ROWS} for c in classes]

    perverse_vals = [{row: NBITS - c["rows"][row]["miss"] for row in ROWS}
                     for c in classes]

    defprim_vals = [{row: (c["rows"][row]["deficit"],
                           c["rows"][row]["miss"]) for row in ROWS}
                    for c in classes]

    const_R = ["R"] * NBITS
    fixed_vals = [{row: cut_miss(c, row, targets[row][0], const_R)
                   for row in ROWS} for c in classes]

    shift_c = {row: targets[row][1].count("R") for row in ROWS}
    shift_vals = [{row: (c["rows"][row]["deficit"][0]
                         + shift_c[row] * c["rows"][row]["deficit"][1],
                         c["rows"][row]["deficit"][1],
                         c["rows"][row]["deficit"][2]) for row in ROWS}
                  for c in classes]

    def geo_sig(ci, row):
        sig = []
        for clo, chi in classes[ci]["rows"][row]["cells"]:
            if chi[1] == 0:
                sig.append(None)
            else:
                sig.append(Fraction(chi[0] * clo[1] - clo[0] * chi[1],
                                    chi[1] * clo[1]))
        return tuple(sig)

    sigs = {(ci, row): geo_sig(ci, row)
            for ci in range(ncls) for row in ROWS}

    # ---- E1 controls --------------------------------------------- #
    print("E1 CONTROLS")
    ok = True

    c1 = all(delayed_miss(c, row, targets[row][0], targets[row][1], 1)
             == c["rows"][row]["miss"]
             for c in classes for row in ROWS)
    ok &= check("C1 delayed scorer at h=1 reproduces the next-side"
                " misses", c1)

    id_dbl = [row for row in ROWS if row[0] in ("id", "dbl")]
    sq_rows = [row for row in ROWS if row[0] == "sq"]
    coincide = all(frac_eq(dcuts[row][i], targets[row][0][i])
                   and dsides[row][i] == targets[row][1][i]
                   for row in id_dbl for i in range(NBITS))
    sq_diff = {row: sum(1 for i in range(NBITS)
                        if not frac_eq(dcuts[row][i], targets[row][0][i]))
               for row in sq_rows}
    ok &= check("C2 digit cuts = next-side cuts on id/dbl rows,"
                " truths equal", coincide,
                "sq rows differ at %s of %d steps" %
                ("/".join(str(sq_diff[r]) for r in sq_rows), NBITS))

    refusers = [ci for ci, c in enumerate(classes)
                if all(cell == ROOT_IV for row in ROWS
                       for cell in c["rows"][row]["cells"])]
    c3 = (len(refusers) == 1
          and sorted(classes[refusers[0]]["members"])
          == sorted((st, ss, None, None) for st in (0, 1) for ss in (0, 1))
          and all(fixed_vals[refusers[0]][row] == 0 for row in ROWS))
    ok &= check("C3 the refuser class: all-root cells, the four"
                " INF/INF policies, fixed-target loss 0", c3)

    cen_def = census(deficit_vals, cmp_lex)
    cen_shift = census(shift_vals, cmp_lex)
    c4 = all(cen_def["argmin"][row] == cen_shift["argmin"][row]
             for row in ROWS)
    ok &= check("C4 shift argmin sets = deficit argmin sets on every"
                " row", c4)

    exp_blocks = [frozenset([("id", "phi"), ("id", "sqrt2"),
                             ("id", "sqrt3"), ("id", "theta8"),
                             ("sq", "phi")]),
                  frozenset([("dbl", "phi"), ("dbl", "sqrt2"),
                             ("dbl", "fib")]),
                  frozenset([("sq", "sqrt2")])]
    got_blocks = [frozenset(blk) for blk in cen_def["partition"]]
    sizes = {row: len(cen_def["argmin"][row]) for row in ROWS}
    c5 = (len(cen_def["uni"]) == 1
          and sorted(got_blocks, key=len) == sorted(exp_blocks, key=len)
          and sizes[("id", "phi")] == 5 and sizes[("dbl", "phi")] == 1
          and sizes[("sq", "sqrt2")] == 11)
    ok &= check("C5 deficit baseline: one universal class, the known"
                " three-block anchor partition (5/1/11)", c5)

    if not ok:
        print("CONTROL FAILURE -- stop; no verdict may be read.")
        raise SystemExit(1)
    u_class = next(iter(cen_def["uni"]))
    print("  the universal deficit class U = class #%d (members %s)"
          % (u_class, ", ".join(fmt_pol(p)
                                for p in classes[u_class]["members"][:2])
             + (", ..." if len(classes[u_class]["members"]) > 2 else "")))
    print()

    # ---- E2 species census --------------------------------------- #
    print("E2 THE SPECIES CENSUS")
    species = []
    species.append(("S0 deficit (baseline)", deficit_vals, cmp_lex,
                    "geometry", None))
    for h in HS:
        species.append(("S1 delayed-side h=%d" % h, delayed_vals[h],
                        cmp_int, "future", "int"))
    species.append(("S2 next-digit-class", digit_vals, cmp_int,
                    "future", "int"))
    species.append(("S3 perverse (hits)", perverse_vals, cmp_int,
                    "future", "int"))
    species.append(("S4 deficit-primary", defprim_vals,
                    cmp_pair_lex_int, "future(tiebreak)", None))
    species.append(("S5 fixed-target", fixed_vals, cmp_int,
                    "past", "int"))
    species.append(("S6 row-constant shift", shift_vals, cmp_lex,
                    "future(value-only)", None))

    results = {}
    for name, vals, cmpf, consults, kind in species:
        cen = census(vals, cmpf)
        comp_cen = None
        if kind == "int":
            comp_vals = [{row: (vals[ci][row], deficit_vals[ci][row])
                          for row in ROWS} for ci in range(ncls)]
            comp_cen = census(comp_vals, cmp_int_then_lex)
        comp_uni = None if comp_cen is None else comp_cen["uni"]
        results[name] = (cen, comp_cen, consults)
        print("  %s" % name)
        if kind == "int":
            print("    per-row min/max: %s" % "  ".join(
                "%s %d/%d" % (fmt_row(row),
                              min(vals[ci][row] for ci in range(ncls)),
                              max(vals[ci][row] for ci in range(ncls)))
                for row in ROWS))
        print("    per-row distinct values: %s" % "  ".join(
            "%s %d" % (fmt_row(row), cen["distinct"][row])
            for row in ROWS))
        print("    per-row argmin sizes:    %s" % "  ".join(
            "%s %d" % (fmt_row(row), len(cen["argmin"][row]))
            for row in ROWS))
        line = "    universal intersection: %s" % (
            "EMPTY" if not cen["uni"] else
            "NONEMPTY (%d class%s%s)" % (
                len(cen["uni"]), "" if len(cen["uni"]) == 1 else "es",
                ", U inside" if u_class in cen["uni"] else ""))
        if comp_uni is not None:
            line += " ; composite order: %s" % (
                "EMPTY" if not comp_uni else "NONEMPTY (%d)" % len(comp_uni))
        print(line)
        print("    row partition (%d blocks): %s"
              % (len(cen["partition"]), fmt_partition(cen["partition"])))
    print()

    # ---- E3 discrimination table --------------------------------- #
    print("E3 THE DISCRIMINATION TABLE (preorder vs the deficit's;"
          " T = identical)")
    degeneracy = {}
    for name, vals, cmpf, consults, kind in species:
        po = preorder_vs(vals, cmpf, deficit_vals, cmp_lex)
        cen = results[name][0]
        mirrors = all(po[row] for row in ROWS)
        toothless_rows = [row for row in ROWS if cen["distinct"][row] <= 1]
        verdict = ("DEGENERATE (deficit-mirroring)" if mirrors else
                   "DEGENERATE (toothless everywhere)"
                   if len(toothless_rows) == len(ROWS) else
                   "non-degenerate")
        degeneracy[name] = verdict
        print("  %-22s %s   toothless rows: %s   -> %s"
              % (name,
                 "".join("T" if po[row] else "." for row in ROWS),
                 ",".join(fmt_row(r) for r in toothless_rows) or "none",
                 verdict))
    print()

    # ---- E4 the criterion table ---------------------------------- #
    print("E4 THE CRITERION TABLE")
    print("  %-22s %-18s %-34s %s"
          % ("species", "consults", "degeneracy", "universality"))
    for name, vals, cmpf, consults, kind in species:
        cen, comp_cen, _ = results[name]
        uni_txt = "EMPTY" if not cen["uni"] else "NONEMPTY"
        if comp_cen is not None:
            uni_txt += "/" + ("EMPTY" if not comp_cen["uni"] else "NONEMPTY")
        print("  %-22s %-18s %-34s %s"
              % (name, consults, degeneracy[name], uni_txt))
    viol_keep = [name for name, _, _, consults, _ in species
                 if consults.startswith("future")
                 and degeneracy[name] == "non-degenerate"
                 and results[name][0]["uni"]]
    viol_break = [name for name, _, _, consults, _ in species
                  if (not consults.startswith("future")
                      or degeneracy[name] != "non-degenerate")
                  and not results[name][0]["uni"]]
    print("  future-consulting non-degenerate species KEEPING"
          " universality: %s" % (", ".join(viol_keep) or "none"))
    print("  non-future or degenerate species BREAKING universality:"
          " %s" % (", ".join(viol_break) or "none"))
    print()

    # ---- E5 geometry-pair census --------------------------------- #
    print("E5 THE GEOMETRY-PAIR CENSUS")
    total_pairs = 0
    separated = {name: 0 for name, _, _, _, _ in species}
    row_groups = {}
    for row in ROWS:
        groups = {}
        for ci in range(ncls):
            groups.setdefault(sigs[(ci, row)], []).append(ci)
        row_groups[row] = groups
        for sig, members in groups.items():
            for x in range(len(members)):
                for y in range(x + 1, len(members)):
                    total_pairs += 1
                    for name, vals, cmpf, _, _ in species:
                        if cmpf(vals[members[x]][row],
                                vals[members[y]][row]) != 0:
                            separated[name] += 1
    print("  within-row identical-geometry class pairs: %d" % total_pairs)
    if total_pairs == 0:
        print("  the beyond-geometry witness test is VACUOUS at this"
              " scope (no two distinct traces share a row's exact"
              " length sequence)")
    else:
        for name, _, _, _, _ in species:
            print("  %-22s separates %d of %d"
                  % (name, separated[name], total_pairs))
    print()

    # ---- E6 the tie mechanism ------------------------------------ #
    print("E6 THE TIE MECHANISM (is a within-row value tie a trace"
          " tie?)")
    def_pairs = def_same = geo_pairs = geo_same = 0
    residual = []
    for row in ROWS:
        dgroups = {}
        order = sorted(range(ncls),
                       key=lambda ci: cmp_to_key(cmp_lex)(
                           deficit_vals[ci][row]))
        gid = 0
        prev = None
        for ci in order:
            if prev is not None and cmp_lex(deficit_vals[ci][row],
                                            deficit_vals[prev][row]) != 0:
                gid += 1
            dgroups.setdefault(gid, []).append(ci)
            prev = ci
        for members in dgroups.values():
            for x in range(len(members)):
                for y in range(x + 1, len(members)):
                    def_pairs += 1
                    if (classes[members[x]]["rows"][row]["cells"]
                            == classes[members[y]]["rows"][row]["cells"]):
                        def_same += 1
        for members in row_groups[row].values():
            for x in range(len(members)):
                for y in range(x + 1, len(members)):
                    geo_pairs += 1
                    if (classes[members[x]]["rows"][row]["cells"]
                            == classes[members[y]]["rows"][row]["cells"]):
                        geo_same += 1
                    else:
                        residual.append((row, members[x], members[y]))
    print("  deficit-tied pairs: %d, of which trace-identical: %d"
          % (def_pairs, def_same))
    print("  geometry-tied pairs: %d, of which trace-identical: %d"
          % (geo_pairs, geo_same))
    if residual:
        print("  residual non-identical geometry-tied pairs: %s"
              % "; ".join("%s #%d/#%d" % (fmt_row(row), a, b)
                          for row, a, b in residual))
    print()

    # ---- E7 representability + the mixing witness ---------------- #
    print("E7 THE REPRESENTABILITY TABLE (row-uniform geometry"
          " functions at scope)")
    cross = {}
    for ci in range(ncls):
        for row in ROWS:
            cross.setdefault(sigs[(ci, row)], []).append((ci, row))
    coll = {sig: pts for sig, pts in cross.items() if len(pts) > 1}
    cross_row_groups = sum(1 for pts in coll.values()
                           if len(set(r for _, r in pts)) > 1)
    print("  geometry collision groups: %d (of which spanning"
          " multiple rows: %d)" % (len(coll), cross_row_groups))
    twin_counts = []
    for xa in range(len(ROWS)):
        for xb in range(xa + 1, len(ROWS)):
            ra, rb = ROWS[xa], ROWS[xb]
            cnt = sum(1 for ci in range(ncls)
                      if sigs[(ci, ra)] == sigs[(ci, rb)])
            if cnt:
                twin_counts.append((ra, rb, cnt))
    print("  twin census (classes with identical geometry columns"
          " per row pair): %s" % ("; ".join(
              "%s~%s %d/%d" % (fmt_row(ra), fmt_row(rb), cnt, ncls)
              for ra, rb, cnt in twin_counts) or "none"))
    print("  full-column twin row pairs: %d"
          % sum(1 for _, _, cnt in twin_counts if cnt == ncls))
    for name, vals, cmpf, consults, kind in species:
        witness = None
        for sig, pts in coll.items():
            base = vals[pts[0][0]][pts[0][1]]
            for ci, row in pts[1:]:
                if cmpf(vals[ci][row], base) != 0:
                    witness = ((pts[0][0], pts[0][1]), (ci, row))
                    break
            if witness:
                break
        if witness is None:
            print("  %-22s REPRESENTABLE at scope (constant on every"
                  " collision group)" % name)
        else:
            (a, ra), (b, rb) = witness
            print("  %-22s NOT representable: class #%d on %s vs"
                  " class #%d on %s share geometry, differ in value"
                  % (name, a, fmt_row(ra), b, fmt_row(rb)))
    ref = refusers[0]
    s5_cen, s5_comp, _ = results["S5 fixed-target"]
    print("  the mixing witness (S5 composite): refuser = class #%d"
          % ref)
    print("    pure argmin membership:      %s" % "  ".join(
        "%s %s(%d)" % (fmt_row(row),
                       "in" if ref in s5_cen["argmin"][row] else "OUT",
                       len(s5_cen["argmin"][row])) for row in ROWS))
    print("    composite argmin membership: %s" % "  ".join(
        "%s %s(%d)" % (fmt_row(row),
                       "in" if ref in s5_comp["argmin"][row] else "OUT",
                       len(s5_comp["argmin"][row])) for row in ROWS))
    print()

    # ---- E8 the geometry breaker --------------------------------- #
    print("E8 THE GEOMETRY BREAKER (band-indicator search over the"
          " deficit order)")
    pts = [(ci, row) for ci in range(ncls) for row in ROWS]
    order = sorted(pts, key=lambda p: cmp_to_key(cmp_lex)(
        deficit_vals[p[0]][p[1]]))
    rank_of = {}
    r = 0
    for a, b in zip(order, order[1:]):
        rank_of[a] = r
        if cmp_lex(deficit_vals[a[0]][a[1]], deficit_vals[b[0]][b[1]]) != 0:
            r += 1
    rank_of[order[-1]] = r
    nranks = r + 1
    full = (1 << ncls) - 1
    prefix = {}
    for row in ROWS:
        pre = []
        mask = 0
        by_rank = {}
        for ci in range(ncls):
            by_rank.setdefault(rank_of[(ci, row)], []).append(ci)
        for t in range(nranks):
            for ci in by_rank.get(t, []):
                mask |= 1 << ci
            pre.append(mask)
        prefix[row] = pre
    specimens = 0
    first = None
    for i in range(nranks):
        for j in range(i, nranks):
            inter = full
            clean = True
            for row in ROWS:
                m = prefix[row][j] & ~(prefix[row][i - 1] if i else 0)
                if m == 0 or m == full:
                    clean = False
                    break
                inter &= m
            if clean and inter == 0:
                specimens += 1
                if first is None:
                    first = (i, j)
    print("  distinct deficit values pooled: %d; bands scanned: %d"
          % (nranks, nranks * (nranks + 1) // 2))
    print("  clean breaker specimens (no toothless row, empty"
          " intersection): %d" % specimens)
    if first is not None:
        i, j = first
        band_vals = [{row: (0 if i <= rank_of[(ci, row)] <= j else 1)
                      for row in ROWS} for ci in range(ncls)]
        bcen = census(band_vals, cmp_int)
        assert not bcen["uni"]
        print("  first specimen: rank band [%d, %d]; per-row in-band"
              " sizes: %s" % (i, j, "  ".join(
                  "%s %d" % (fmt_row(row), len(bcen["argmin"][row]))
                  for row in ROWS)))
        print("    row partition (%d blocks): %s"
              % (len(bcen["partition"]), fmt_partition(bcen["partition"])))
    print()
    print("done in %.1fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
