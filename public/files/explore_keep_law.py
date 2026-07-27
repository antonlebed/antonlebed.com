"""
The keep law: WHICH class-constant losses keep the data-free
universality of the exact reader's optimum -- is the keep an
extremal phenomenon of the refinement order?

THE QUESTION
------------
explore_score_criterion.py inverted the door question: emptiness of
the universal intersection is generic (146 band-indicator losses
break it reading nothing but the deficit value), so the special
thing needing a law is the KEEP -- what structure hands every row
the same witness? The candidate from that experiment's close: THE
EXTREMAL LAW -- a loss keeps universality when its per-row optima
sit at a shared pointwise EXTREMAL of the cell-refinement order:
losses that reward tightness keep via a pointwise-tightest class
(the greedy class, if it is one), losses that reward coarseness
keep via the pointwise-coarsest (the refuser, which provably is
one), and interior-optimum losses (the bands) break. This
experiment freezes the law's three arms and attacks each:

  Q1  TIGHT ARM: does a pointwise-tightest class exist at scope --
      is the greedy class's committed cell contained in EVERY
      class's cell at every counted step on every row? -- and does
      every monotone-tight species then keep through it?
  Q2  COARSE ARM: the refuser is pointwise-coarsest by
      construction (lemma A below); does the anti-deficit, the
      concrete coarseness-rewarding loss, in fact keep through it
      at scope (its monotonicity carries a caveat, lemma C)?
  Q3  INTERVAL ARM + NECESSITY: for clean value bands, keep iff
      the band contains some class's cross-row rank hull (lemma D,
      proved) -- asserted band-by-band, with the hull spectrum
      printed as an instrument; and does a NON-monotone,
      non-interval keeper exist (lemma E's construction), making
      the extremal law sufficiency-only?

HAND LEMMAS (fixed before the engine)
-------------------------------------
HL-A THE COARSEST LEMMA (proved). The refuser class holds the root
    cell at every counted step on every row (established control,
    explore_score_criterion.py C3), and the root interval contains
    every cell. So the refuser is the pointwise-coarsest class,
    and every class-constant loss that is MONOTONE-COARSE
    (A pointwise inside B implies loss(A) >= loss(B)) has the
    refuser in every row's argmin: universal intersection
    nonempty, KEEP. Two lines, no engine needed.
HL-B THE LENGTH BOUND FAILS. "Every finite committed cell has
    length <= 1" is FALSE: a straddle cell's interval
    (l + kv, r + kv) has cross-product (r x l) + k[(v x l) + (r x v)];
    at the root (l = 0/1, r = 1/0, v = 1/1) this is 2k + 1 with
    endpoints k/(k+1), (k+1)/k -- length (2k+1)/(k(k+1)), which is
    3/2 > 1 at k = 1 and <= 1 for every k >= 2. The k = 1 root
    straddle (1/2, 2) is reachable: on the id/phi row the golden
    point lies in (1/2, 2) but above 3/2, so the root chain index
    maxes at 1 for any deep reference, and a chain-only policy
    (tree patience INF) commits it before counting starts and can
    never tree-refine -- a class holding a finite cell of length
    3/2 at every counted step. The census of finite counted cells
    with length > 1 is therefore a real observable (C4).
HL-C PRODUCT MONOTONICITY, WITH A CAVEAT. Product species (the
    deficit, weighted deficits) skip infinite factors. For A
    pointwise inside B, A's infinite steps are a subset of B's
    (containment forces the right endpoints), and: A finite-flagged
    vs B infinite-flagged compares A below B unconditionally;
    both finite-flagged compares componentwise, A <= B
    unconditionally; both INFINITE-flagged leaves A's product
    carrying extra factors at steps where B is infinite and A
    finite -- if every such factor is <= 1 then A <= B, but an
    extra factor > 1 (HL-B's cells) could invert the comparison.
    So MAX-LENGTH and LAST-CELL are monotone-tight
    unconditionally; the weighted deficit is monotone-tight modulo
    the caveat; the anti-deficit is monotone-coarse modulo the
    mirror caveat (the refuser's finite part is the empty product
    1; an all-infinite class with finite part > 1 would beat it).
HL-D THE HULL LEMMA (proved). Band loss: 0 if the class's deficit
    value on the row lies in B, else 1, with B an order-interval
    of the pooled distinct deficit values, row-uniform. CLEAN =
    every row's in-band set neither empty nor full. For a clean
    band each row realizes both loss values, so the row's argmin
    is exactly its in-band set; the universal intersection is
    nonempty iff some class is in-band on every row iff B contains
    all nine of its values iff (B an order interval) B contains
    that class's cross-row rank-interval HULL
    [min over rows, max over rows]. KEEP iff B contains some
    class's hull. Pure order only; the composite (band, deficit)
    order is a different object and is reported separately.
    Corollary instrument: THE HULL SPECTRUM -- per class its hull
    and width; clean breakers = clean bands containing no hull; a
    narrow hull is a ROW-STABLE class (its deficit rank barely
    moves as the world changes -- the standing carries no row
    dependence, echoing the data-free reading); emptiness is
    generic exactly when hulls are wide.
HL-E THE UNION-BAND CONSTRUCTION. Take any class c and a gap of
    two or more between consecutive ranks in c's sorted rank set
    (every rank is a realized value, so the gap excludes realized
    values); the union of the two flanking bands covers all of c's
    values. The indicator loss of that union is NON-INTERVAL and
    NON-MONOTONE in the deficit value (0 then 1 then 0 along the
    value axis), and c witnesses KEEP whenever the union is clean.
    A specimen whose witness is neither the greedy class nor the
    refuser is a keep the extremal law cannot explain: the value
    table, not monotone structure, hands it out.
HL-F NON-LAMINARITY (filed at the freeze as "why Q1 is genuinely
    open"). The cell family is NOT laminar: a straddle cell
    crosses its tree node's boundary, so a straddle and a tree
    cell can overlap with neither containing the other, both
    containing the image interval -- no chain/laminarity argument
    exists. (Correction, found at audit after the run: the freeze
    filed the question as open, but it never was -- the bottom
    lemma of explore_bootstrap_cures.py, proved for this cover and
    move family, gives the containing-cell sub-poset an inclusion
    MINIMUM that greedy multi-commit reaches, and every committed
    cell contains the image interval by the ratchet invariant, so
    the greedy cell sits inside every class's cell as a two-step
    corollary. The in-engine assert is that corollary's engine
    echo, guarding the gap between the lemma's engine and this
    one; the non-laminarity above is why nothing SIMPLER forces
    it.)

THE SPECIES SLATE (frozen at design; all class-constant, values
compared exactly as (num, den, inf) triples)
--------------------------------------------
K1a MAX-LENGTH: the maximum counted cell length (infinite if any
    counted cell is infinite; all-infinite maxima tie). Monotone-
    tight unconditionally (componentwise max, infinity on top).
K1b LAST-CELL: the last counted cell's length (or infinite).
    Monotone-tight unconditionally (a single coordinate).
K1c W-DEFICIT: the product of counted lengths with the second half
    of the counted window (scored index >= 56) SQUARED; infinite
    factors skipped and flagged, the engine deficit's convention.
    Monotone-tight modulo HL-C's caveat. MARKED TRANSPLANT:
    "weighting preserves the keep" is imported from the deficit's
    behavior, not derived.
K2  ANTI-DEFICIT: the deficit under the reversed order (coarseness
    rewarded). Monotone-coarse modulo HL-C's mirror caveat; HL-A
    predicts keep via the refuser if the caveat is empty at scope.
K3  THE BAND FAMILY: every order-interval band over the pooled
    distinct deficit values (the geometry-breaker family of
    explore_score_criterion.py E8) -- HL-D asserted band-by-band,
    the known clean-breaker count recounted, the hull spectrum
    printed.
K4  THE UNION-BAND SEARCH: HL-E's construction over all classes
    and all rank gaps; specimens printed with their witnesses.

PREDICTIONS (fixed before the run)
----------------------------------
P1  The controls pass (C1-C4 below); a failed control stops the
    read.
P2  The dominance assert prints TRUE on all nine rows. MARKED
    HUNCH -- transplanted from the reader-descent corpus's
    "tighter never hurt" folklore, which was minted for the
    deficit SUM, never for per-step containment; HL-F says the
    question is genuinely open.
P3  If P2 holds: K1a and K1b keep with the greedy class in every
    argmin (theorem-shape given the assert); K1c keeps unless
    HL-C's inversion realizes at scope.
P4  K2 keeps via the refuser (HL-A, with HL-C's mirror caveat
    empty at scope).
P5  The hull lemma verifies on every clean band and the clean-
    breaker count is exactly 146 (the established count).
P6  A clean union-band keeper exists with a witness that is
    neither the greedy class nor the refuser (marked hunch) --
    landing the extremal law as sufficiency-only.
Kills as observables: the per-row TRUE/FALSE dominance prints with
first witness site; per-species universal-intersection prints; the
band verdict-vs-hull equality count; the union-band specimen
print. The meaning is weighed after the run.

EXPERIMENTS
-----------
E1  CONTROLS. C1 the deficit baseline reproduces: exactly one
    universal class, the greedy policy inside it, and the known
    argmin-set row partition (the five-row block at argmin size 5,
    the three dbl rows at size 1, sq/sqrt2 alone at size 11). C2
    the refuser class (both patiences infinite) holds the root
    cell at every counted step on every row. C3 the band recount:
    clean breakers = 146 over the pooled deficit ranks. C4 the
    length census: finite counted cells with length > 1 -- count,
    sites, the maximum finite length (HL-B says nonzero is
    expected; where they sit conditions HL-C's caveat).
E2  THE EXTREMAL ASSERTS. Per row: is the greedy class's cell
    contained in every class's cell at every counted step
    (TRUE/FALSE, first witness on failure)? The mirror assert for
    the refuser (containment the other way, expected TRUE by
    HL-A). The nesting census: over all class pairs and counted
    steps, how many sites hold two cells with NEITHER containing
    the other (HL-F's non-laminarity, quantified at scope).
E3  THE MONOTONE SPECIES. For K1a, K1b, K1c, K2: per-row argmin
    sizes and distinct-value counts, the universal intersection
    under the species' own pure order and under the (species,
    deficit) composite, the row partition by argmin set, and the
    greedy/refuser membership prints.
E4  THE HULL SPECTRUM + THE BAND LEMMA AT SCOPE. The per-class
    hulls printed as a spectrum (sorted by width, narrowest and
    widest named); for every band, the keeper verdict (nonempty
    intersection) asserted equal to hull-containment; clean bands
    / keepers / breakers counted, breakers asserted 146; the
    witness census (which classes' hulls sit inside at least one
    clean keeper band).
E5  THE UNION-BAND SEARCH. All classes, all internal rank gaps of
    size >= 2: clean union-keepers counted; a specimen with a
    non-extremal witness printed with its bands, per-row in-union
    sizes, and full intersection membership. ADDENDUM (designed
    after the first run, at audit -- the bare found count pools
    witness types, so quoting it as "non-extremal keepers" would
    overclaim): print how many of the found unions are seeded by a
    non-pole class and how many have universal intersections
    containing NEITHER pole at all.

FINDINGS (from the run; all controls green first)
--------------------------------------------------
E1  All controls pass. The greedy class is #0 (4 members, the
    patience-0 policies), the refuser #21; the clean-band census
    splits 403 = 257 keepers + 146 breakers (the breaker count
    reproducing exactly). C4: the length census prints 224
    (class, step) sites with finite length > 1 -- all of them the
    single predicted cell, the k = 1 root straddle (1/2, 2) of
    length 3/2, held at all 112 counted steps on id/phi and
    id/sqrt3 (the two streams above 3/2; on id/sqrt2 the point
    sits below 3/2, the root chain index reaches 2, and the cell
    is already length 5/6). HL-B realized to the letter, and the
    maximum finite counted length is exactly 3/2.

E2  THE TIGHT EXTREMAL EXISTS -- BY THE BOTTOM LEMMA, NOT BY
    LAMINARITY. The dominance assert prints TRUE on all nine rows:
    the greedy class's committed cell is contained in every
    class's cell at every counted step. The nesting census shows
    what does NOT force this: 76058 non-nested (row, pair, step)
    sites across 1347 (row, pair) combinations -- the
    committed-cell family is massively non-laminar (straddles
    crossing tree boundaries), so no chain argument applies. What
    does force it is the bottom lemma (explore_bootstrap_cures.py,
    proved): the containing-cell sub-poset's inclusion minimum,
    which greedy reaches, sits inside every ratcheted cell (HL-F's
    audit correction) -- the assert is the corollary's engine
    echo, and it holds. The refuser mirror assert prints TRUE on
    all rows (HL-A's engine echo).

E3  EVERY MONOTONE SPECIES KEEPS, EACH THROUGH ITS OWN POLE, EACH
    WITH A SINGLETON INTERSECTION. K1a MAX-LENGTH, K1b LAST-CELL,
    K1c W-DEFICIT: universal intersection NONEMPTY of size 1 =
    the greedy class alone, pure and composite. K2 ANTI-DEFICIT:
    NONEMPTY of size 1 = the refuser alone, pure and composite.
    HL-C's caveat is real but toothless at scope: the 3/2 cells
    live in a chain-stuck class that is finite-flagged on those
    rows, so no product comparison crosses the infinite boundary
    carrying them. The keeps read little: the argmin-set row
    partitions have 3-4 blocks (vs 9 for the prediction species),
    and the anti-deficit's argmins are tiny (1-2 classes; 6 on
    sq/sqrt2, the six infinite-cell classes) -- the refuser is
    nearly uniquely the coarseness optimum everywhere.

E4  THE HULL LEMMA VERIFIED; THE SPECTRUM IS BIMODAL. Keep iff
    the band contains some class's hull holds on every one of the
    403 clean bands. The hull spectrum: the refuser has width 0
    (rank 116 -- the pooled MAXIMUM deficit -- on every row) and
    its sibling #20 width 2; EVERY other class has width >= 85 of
    a 117-rank spectrum. Row-stability of standing is a property
    of the refusing corner alone; every adapted class's deficit
    rank sweeps at least 73 percent of the pooled order as the
    row changes. That is the mechanism of generic
    emptiness: an interior band narrower than 85 ranks can
    contain no adapted class's hull, so only refuser-corner bands
    and huge bands keep. 34 of 38 classes witness some clean
    keeper. A hull is witnessed iff its own tightest band is clean
    (a containing band only loosens the full test, and emptiness is
    impossible -- the class's own rank is inside), and the four
    that never are (#4, #9, #14, #19) fail it decisively: every
    row's maximum rank is 116 (the refuser's seat), so their bands
    [0..11, 116] are FULL on every row whose minimum rank sits at
    or above their floor -- 8 to 9 of the 9 rows (row minima are
    the greedy ranks, 0 to 85, and only id/theta8's 0 ever dips
    below a floor). The refusing corner also reaches 116 but its
    floors (114, 116) sit above every row minimum: full nowhere,
    witnessed.

E5  THE EXTREMAL LAW IS SUFFICIENCY-ONLY. 213 clean union-band
    keepers exist; 209 are seeded by a non-pole class, and in 201
    the universal intersection contains NEITHER pole -- the whole
    optimum set avoids both extremals (the addendum census). The
    specimen: class #1's values covered by [0,0] u [13,88], clean
    on every row, universal intersection {#1, #2, #3} -- none of
    them greedy or refuser. A non-monotone, non-interval,
    row-uniform geometry loss keeping universality through a
    witness at no pointwise extremal: the value table, not
    monotone structure, hands out this keep.

READING. The keep law at scope has the shape the extremal
candidate proposed, with its quantifier honest: monotone structure
toward a pointwise extremal GUARANTEES a keep, and BOTH POLES ARE
THEOREMS -- the greedy class is pointwise-tightest as a two-step
corollary of the proved bottom lemma (HL-F's audit correction;
the design had filed the question open, missing that the
reader-descent corpus's pointwise-optimality lemma already
answers per-step containment), the refuser pointwise-coarsest by
construction, and all four monotone species keep with the
respective pole as the SOLE universal optimum, composite orders
included. But the law is
sufficiency-only: keeps without extremal structure exist (the
union-band specimens), handed out by the value table. The honest
criterion for the interval family is exact and proved -- clean-
band keep iff the band contains some class's cross-row rank hull
-- and the hull spectrum it induces is this experiment's
instrument find: BIMODAL, refusing corner (widths 0-2) against everything
adapted (widths >= 85). Emptiness of the universal intersection is
generic because adaptation makes every class's standing violently
row-dependent; the only optima whose standing survives the change
of world are the ones that refuse to adapt at all. Predictions
against outcomes: P1-P6 all as predicted, with one correction to
the freeze's modality rather than its content -- P2 called the
dominance genuinely open when it was already a corollary of the
bottom lemma (HL-F's audit correction): the marked hunch was a
theorem the design failed to recognize as one. HL-C's caveat
named the exact cell that realizes it and the run confirmed both
its presence and its harmlessness.
Tier: HL-A, HL-D, HL-E are proved (HL-B's 3/2 cell arithmetic
likewise), and the dominance fact is a corollary of the proved
bottom lemma (explore_bootstrap_cures.py), so both extremal poles
-- and with them the max-length and last-cell keeps -- are
theorem-grade for this cover and move family; the weighted and
anti-deficit keeps (their monotonicity caveat checked at scope),
the bimodal spectrum, and the sufficiency-only verdict are exact
and exhaustive at the stated scope (this policy space, these nine
rows, horizon 120) only.

Run record: run 1 exit 0, all controls green, 1.8s; run 2 (E5
addendum census added) exit 0, all else unchanged, 1.8s.

DESIGN
------
Everything heavy is imported verbatim: the reader engine, rows,
class construction from explore_prediction_door.py; the census /
comparator / partition helpers from explore_score_criterion.py.
Index convention re-derived from the engine: counted step n in
[8, 120) has scored index i = n - 8; the class dicts store the 112
counted cells per row in that order, and the deficit triple
(num, den, inf) is the product of finite counted lengths with
infinite cells skipped and flagged. Cell containment is exact
cross-multiplied endpoint comparison (infinite right endpoints
handled by the fraction order itself). All species values are
exact triples under the engine's lexicographic comparator; no
floats in any comparison.
"""

import time
from functools import cmp_to_key

from explore_prediction_door import (
    N0, HORIZON, DEEP, ROWS, fmt_row, fmt_pol, cmp_lex, lt,
    build_images, truth_targets, build_classes, check,
)
from explore_score_criterion import census, cmp_int, fmt_partition

NBITS = HORIZON - N0
ROOT_IV = ((0, 1), (1, 0))
W_SPLIT = 56                  # scored index where the double weight starts

INF_TRIPLE = (1, 1, True)     # canonical infinite species value


# ----------------------------------------------------------------- #
# exact cell helpers
# ----------------------------------------------------------------- #

def le(a, b):
    """a <= b on fractions (num, den), infinity as (x, 0)."""
    return not lt(b, a)

def cell_inside(A, B):
    """Interval A contained in interval B (both (lo, hi) pairs)."""
    return le(B[0], A[0]) and le(A[1], B[1])

def length_of(cell):
    """(num, den, False) for a finite cell, INF_TRIPLE otherwise."""
    lo, hi = cell
    if hi[1] == 0:
        return INF_TRIPLE
    return (hi[0] * lo[1] - lo[0] * hi[1], hi[1] * lo[1], False)


# ----------------------------------------------------------------- #
# species values
# ----------------------------------------------------------------- #

def max_length(cells):
    best = None
    for cell in cells:
        t = length_of(cell)
        if t[2]:
            return INF_TRIPLE
        if best is None or cmp_lex(t, best) > 0:
            best = t
    return best

def last_cell(cells):
    return length_of(cells[-1])

def w_deficit(cells):
    num, den, inf = 1, 1, False
    for i, cell in enumerate(cells):
        t = length_of(cell)
        if t[2]:
            inf = True
            continue
        w = 2 if i >= W_SPLIT else 1
        for _ in range(w):
            num *= t[0]
            den *= t[1]
    return (num, den, inf)

def cmp_anti(a, b):
    return -cmp_lex(a, b)

def cmp_comp(cmp_primary):
    """(primary, deficit) composite comparator factory."""
    def cf(a, b):
        c = cmp_primary(a[0], b[0])
        return c if c != 0 else cmp_lex(a[1], b[1])
    return cf


# ----------------------------------------------------------------- #
# rank machinery (the band family)
# ----------------------------------------------------------------- #

def build_ranks(classes, deficit_vals):
    ncls = len(classes)
    pts = [(ci, row) for ci in range(ncls) for row in ROWS]
    order = sorted(pts, key=lambda p: cmp_to_key(cmp_lex)(
        deficit_vals[p[0]][p[1]]))
    rank_of = {}
    r = 0
    for a, b in zip(order, order[1:]):
        rank_of[a] = r
        if cmp_lex(deficit_vals[a[0]][a[1]],
                   deficit_vals[b[0]][b[1]]) != 0:
            r += 1
    rank_of[order[-1]] = r
    return rank_of, r + 1


def main():
    t0 = time.time()
    print("THE KEEP LAW -- which class-constant losses keep"
          " universality")
    print("rows: %s" % ", ".join(fmt_row(r) for r in ROWS))
    imgs = build_images(DEEP)
    targets = {row: truth_targets(imgs[row]) for row in ROWS}
    classes = build_classes(imgs, targets)
    ncls = len(classes)
    print("behavior classes: %d" % ncls)
    print()

    deficit_vals = [{row: c["rows"][row]["deficit"] for row in ROWS}
                    for c in classes]

    # ---- E1 controls --------------------------------------------- #
    print("E1 CONTROLS")
    ok = True

    cen_def = census(deficit_vals, cmp_lex)
    uni_def = cen_def["uni"]
    ok &= check("C1a deficit universality: exactly one universal class",
                len(uni_def) == 1, "uni size %d" % len(uni_def))
    U = next(iter(uni_def))
    ok &= check("C1b greedy policy (0,0,0,0) in the universal class",
                (0, 0, 0, 0) in classes[U]["members"],
                "class #%d, %d members" % (U, len(classes[U]["members"])))
    five = [("id", "phi"), ("id", "sqrt2"), ("id", "sqrt3"),
            ("id", "theta8"), ("sq", "phi")]
    dbls = [("dbl", "phi"), ("dbl", "sqrt2"), ("dbl", "fib")]
    sizes_ok = (
        all(len(cen_def["argmin"][r]) == 5 for r in five)
        and all(len(cen_def["argmin"][r]) == 1 for r in dbls)
        and len(cen_def["argmin"][("sq", "sqrt2")]) == 11)
    ok &= check("C1c anchor argmin sizes 5/1/11 reproduce", sizes_ok,
                " ".join("%s %d" % (fmt_row(r), len(cen_def["argmin"][r]))
                         for r in ROWS))

    ref_idx = None
    for ci, c in enumerate(classes):
        if (0, 0, None, None) in c["members"]:
            ref_idx = ci
            break
    root_everywhere = all(
        cell == ROOT_IV
        for row in ROWS for cell in classes[ref_idx]["rows"][row]["cells"])
    ok &= check("C2 refuser class holds the root cell at every counted"
                " step on every row", root_everywhere,
                "class #%d" % ref_idx)

    rank_of, nranks = build_ranks(classes, deficit_vals)
    full = (1 << ncls) - 1
    prefix = {}
    for row in ROWS:
        by_rank = {}
        for ci in range(ncls):
            by_rank.setdefault(rank_of[(ci, row)], []).append(ci)
        pre = []
        mask = 0
        for t in range(nranks):
            for ci in by_rank.get(t, []):
                mask |= 1 << ci
            pre.append(mask)
        prefix[row] = pre
    hulls = []
    for ci in range(ncls):
        rs = [rank_of[(ci, row)] for row in ROWS]
        hulls.append((min(rs), max(rs)))
    clean_n = keep_n = break_n = 0
    lemma_ok = True
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
            if not clean:
                continue
            clean_n += 1
            hull_in = any(lo >= i and hi <= j for (lo, hi) in hulls)
            if (inter != 0) != hull_in:
                lemma_ok = False
            if inter != 0:
                keep_n += 1
            else:
                break_n += 1
    ok &= check("C3 clean breaker recount = 146", break_n == 146,
                "clean %d = keep %d + break %d"
                % (clean_n, keep_n, break_n))

    over1 = {}
    max_len = None
    for row in ROWS:
        sites = 0
        cells_seen = set()
        for ci in range(ncls):
            for i, cell in enumerate(
                    classes[ci]["rows"][row]["cells"]):
                t = length_of(cell)
                if t[2]:
                    continue
                if t[0] > t[1]:          # length > 1
                    sites += 1
                    cells_seen.add(cell)
                if max_len is None or cmp_lex(t, max_len) > 0:
                    max_len = t
        over1[row] = (sites, cells_seen)
    tot_over1 = sum(v[0] for v in over1.values())
    print("  C4 length census: %d (class, step) sites with finite"
          " length > 1" % tot_over1)
    for row in ROWS:
        if over1[row][0]:
            print("      %s: %d sites, cells %s"
                  % (fmt_row(row), over1[row][0],
                     sorted(over1[row][1])))
    print("      max finite counted length: %d/%d"
          % (max_len[0], max_len[1]))
    if not ok:
        print("CONTROL FAILURE -- stop")
        raise SystemExit(1)
    print()

    # ---- E2 the extremal asserts --------------------------------- #
    print("E2 THE EXTREMAL ASSERTS")
    print("  dominance (greedy class #%d pointwise-tightest):" % U)
    dom_all = True
    for row in ROWS:
        ucells = classes[U]["rows"][row]["cells"]
        witness = None
        for ci in range(ncls):
            if ci == U:
                continue
            bcells = classes[ci]["rows"][row]["cells"]
            for i in range(NBITS):
                if not cell_inside(ucells[i], bcells[i]):
                    witness = (i, ci)
                    break
            if witness:
                break
        dom_all &= witness is None
        print("    %s: %s%s" % (
            fmt_row(row), "TRUE" if witness is None else "FALSE",
            "" if witness is None
            else " -- first witness step %d vs class #%d" % witness))
    print("  refuser class #%d pointwise-coarsest:" % ref_idx)
    coarse_all = True
    for row in ROWS:
        rcells = classes[ref_idx]["rows"][row]["cells"]
        bad = None
        for ci in range(ncls):
            for i in range(NBITS):
                if not cell_inside(
                        classes[ci]["rows"][row]["cells"][i], rcells[i]):
                    bad = (i, ci)
                    break
            if bad:
                break
        coarse_all &= bad is None
        if bad:
            print("    %s: FALSE at step %d class #%d"
                  % (fmt_row(row), bad[0], bad[1]))
    print("    %s on all rows" % ("TRUE" if coarse_all else "FALSE"))
    nonnest = 0
    pairs_nonnest = set()
    for row in ROWS:
        allcells = [classes[ci]["rows"][row]["cells"]
                    for ci in range(ncls)]
        for a in range(ncls):
            for b in range(a + 1, ncls):
                ca, cb = allcells[a], allcells[b]
                for i in range(NBITS):
                    A, B = ca[i], cb[i]
                    if A == B:
                        continue
                    if not cell_inside(A, B) and not cell_inside(B, A):
                        nonnest += 1
                        pairs_nonnest.add((row, a, b))
    print("  nesting census: %d non-nested (row, pair, step) sites"
          " across %d (row, pair) combinations" % (
              nonnest, len(pairs_nonnest)))
    print()

    # ---- E3 the monotone species --------------------------------- #
    print("E3 THE MONOTONE SPECIES")
    species = [
        ("K1a MAX-LENGTH",
         [{row: max_length(classes[ci]["rows"][row]["cells"])
           for row in ROWS} for ci in range(ncls)], cmp_lex),
        ("K1b LAST-CELL",
         [{row: last_cell(classes[ci]["rows"][row]["cells"])
           for row in ROWS} for ci in range(ncls)], cmp_lex),
        ("K1c W-DEFICIT",
         [{row: w_deficit(classes[ci]["rows"][row]["cells"])
           for row in ROWS} for ci in range(ncls)], cmp_lex),
        ("K2 ANTI-DEFICIT", deficit_vals, cmp_anti),
    ]
    for name, vals, cmpf in species:
        cen = census(vals, cmpf)
        comp_vals = [{row: (vals[ci][row], deficit_vals[ci][row])
                      for row in ROWS} for ci in range(ncls)]
        cen_c = census(comp_vals, cmp_comp(cmpf))
        print("  %s:" % name)
        print("    per-row argmin sizes: %s" % "  ".join(
            "%s %d" % (fmt_row(row), len(cen["argmin"][row]))
            for row in ROWS))
        print("    distinct values per row: %s" % "  ".join(
            "%d" % cen["distinct"][row] for row in ROWS))
        for tag, c in (("pure", cen), ("composite", cen_c)):
            uni = c["uni"]
            print("    %s universal intersection: %s (size %d)%s%s"
                  % (tag, "NONEMPTY" if uni else "EMPTY", len(uni),
                     " greedy IN" if U in uni else "",
                     " refuser IN" if ref_idx in uni else ""))
        print("    row partition (%d blocks): %s"
              % (len(cen["partition"]),
                 fmt_partition(cen["partition"])))
    print()

    # ---- E4 the hull spectrum ------------------------------------ #
    print("E4 THE HULL SPECTRUM + THE BAND LEMMA AT SCOPE")
    print("  pooled distinct deficit values: %d" % nranks)
    print("  band lemma (keep iff band contains some hull), all clean"
          " bands: %s" % ("VERIFIED" if lemma_ok else "VIOLATED"))
    print("  clean bands %d = keepers %d + breakers %d"
          % (clean_n, keep_n, break_n))
    spec = sorted(range(ncls), key=lambda ci: hulls[ci][1] - hulls[ci][0])
    print("  hull spectrum (class: [lo, hi] width), narrowest first:")
    for ci in spec:
        lo, hi = hulls[ci]
        print("    #%-2d [%3d, %3d] width %3d%s%s"
              % (ci, lo, hi, hi - lo,
                 "  <- greedy" if ci == U else "",
                 "  <- refuser" if ci == ref_idx else ""))
    witnessed = set()
    for i in range(nranks):
        for j in range(i, nranks):
            clean = True
            for row in ROWS:
                m = prefix[row][j] & ~(prefix[row][i - 1] if i else 0)
                if m == 0 or m == full:
                    clean = False
                    break
            if not clean:
                continue
            for ci in range(ncls):
                lo, hi = hulls[ci]
                if lo >= i and hi <= j:
                    witnessed.add(ci)
    print("  witness census: %d classes witness at least one clean"
          " keeper band: %s"
          % (len(witnessed),
             " ".join("#%d" % c for c in sorted(witnessed))))
    print()

    # ---- E5 the union-band search -------------------------------- #
    print("E5 THE UNION-BAND SEARCH")
    found = []
    for ci in range(ncls):
        rs = sorted(set(rank_of[(ci, row)] for row in ROWS))
        for a, b in zip(rs, rs[1:]):
            if b - a < 2:
                continue
            lo_c, hi_c = rs[0], rs[-1]
            inter = full
            clean = True
            for row in ROWS:
                m1 = prefix[row][a] & ~(prefix[row][lo_c - 1]
                                        if lo_c else 0)
                m2 = prefix[row][hi_c] & ~prefix[row][b - 1]
                m = m1 | m2
                if m == 0 or m == full:
                    clean = False
                    break
                inter &= m
            if clean and inter != 0:
                found.append((ci, (lo_c, a), (b, hi_c), inter))
    print("  clean union-band keepers found: %d (over all classes and"
          " internal rank gaps >= 2)" % len(found))
    seeded_np = sum(1 for f in found if f[0] != U and f[0] != ref_idx)
    nopole = sum(1 for f in found
                 if not (f[3] >> U & 1) and not (f[3] >> ref_idx & 1))
    print("  seeded by a non-pole class: %d; universal intersection"
          " contains neither pole: %d" % (seeded_np, nopole))
    nonext = [f for f in found if f[0] != U and f[0] != ref_idx]
    if nonext:
        ci, b1, b2, inter = nonext[0]
        members = [c for c in range(ncls) if inter >> c & 1]
        print("  specimen: class #%d (neither greedy nor refuser),"
              " bands [%d,%d] u [%d,%d]" % (ci, *b1, *b2))
        print("    intersection members: %s"
              % " ".join("#%d" % c for c in members))
        band_vals = [{row: (0 if (b1[0] <= rank_of[(cj, row)] <= b1[1]
                                  or b2[0] <= rank_of[(cj, row)] <= b2[1])
                            else 1) for row in ROWS}
                     for cj in range(ncls)]
        bcen = census(band_vals, cmp_int)
        print("    per-row in-union sizes: %s" % "  ".join(
            "%s %d" % (fmt_row(row), len(bcen["argmin"][row]))
            for row in ROWS))
        assert bcen["uni"], "specimen lost universality on recheck"
    print()
    print("done in %.1fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
