"""
The bandwidth dial: score an exact reader on predicting its stream
at every m-th counted step only, and watch where the data-dependence
of the optimum dies as the coupling thins.

THE QUESTION
------------
explore_prediction_door.py opened the data door at full coupling:
under the next-side prediction loss -- one future side bit per
counted step -- destination universality fails (the universal
intersection is empty), pointwise dominance dies, and the optimum
SET becomes stream-readable, while the pure deficit (a
trace-geometry loss) keeps a universal optimum on the same space.
This experiment interpolates between the two: the composite loss
family L_m scores next-side misses on every m-th counted step only,
with the lexicographic deficit as tiebreak, m running over a grid
from 1 (full coupling) through {2, 4, 8, 16, 28, 56} to 112 (a
single scored bit), with the pure deficit as the m = infinity
anchor. Same frozen space: the 100 unresourced commitment policies,
the nine rows, the behavioral quotient of
explore_prediction_door.py.

  Q1  THE KNIFE EDGE: what is the largest m on the grid whose
      universal intersection is still EMPTY -- does a single
      scored future bit already break universality?
  Q2  THE MECHANISM: where universality returns, does it return by
      OVERLAP (a genuinely shared optimum among discriminating
      bits) or by AGREEMENT (the scored bits stop discriminating
      -- every class scores zero, and the loss degenerates to the
      deficit mechanically)?
  Q3  CONSERVATION: at each m, does every strict specialist
      advantage refine the readability partition -- or does a
      (row, m) print where a specialist strictly beats the pooled
      winner on its row while the row's partition block stays
      merged with another row's (FREE ADAPTATION: the row's data
      enters the optimum without becoming readable from it)?

INDEX CONVENTION (re-derived from the engine before the freeze)
---------------------------------------------------------------
In explore_prediction_door.py's score_trace, counted steps are
n in [8, 119] with scored index i = n - 8 in [0, 111]: 112 bits,
hits[i] the per-step hit flag. THE LAST COUNTED STEP is index 111
(step 119). The scored set is END-ANCHORED, a frozen design
choice: S_m = { i : (111 - i) = 0 mod m }, so |S_m| = 112/m for
every grid m (all divide 112) and m = 112 scores exactly the last
counted bit. One alternate placement prints as a sensitivity
check: the first-anchored S'_m = { i : i = 0 mod m }.

HAND LEMMAS (fixed before the engine)
-------------------------------------
H1  SUBSET INHERITANCE. For m | m' the end-anchor nests the scored
    sets: S_{m'} is a subset of S_m. Per (class, row) the scored
    miss count is therefore non-increasing along the divisor
    chains 1|2|4|8|16|112, 1|2|4|8|56|112, 1|2|4|28|56|112, and so
    is the row minimum; on the eight rows with a perfect
    full-window predictor the row minimum is 0 at EVERY m. The
    engine asserts both.
H2  THE ANCHOR CRITERION. Let U be the deficit-universal class
    (unique on this quotient, greedy inside). U carries the row
    minimum deficit on every row, so U sits in row r's composite
    argmin at m exactly when U achieves row r's minimum scored
    miss count -- on perfect rows, exactly when S_m avoids U's
    miss set. Universality via U is thus a miss-set /
    arithmetic-progression intersection question; universality can
    also return via a non-U class (minimum deficit among each
    row's minimal-miss classes simultaneously). The census
    decides.
H3  THE SINGLE BIT. At m = 112 the composite argmin of a row is
    the minimum-deficit class among the hitters of bit 111. If U
    hits the last counted bit on all nine rows, universality
    returns there via U. Not hand-decidable; genuinely open.
H4  NON-MONOTONICITY IS LIVE. The shape "empty at small m,
    nonempty above a knife edge" is imported intuition (from the
    full-coupling break and the anchor), marked as such: composite
    argmin sets do not nest along chains (the tiebreak
    reshuffles), the grid is not a chain (16 and 28 are
    divisibility-incomparable), and the family is discontinuous at
    the anchor by construction -- any finite m puts one stream bit
    lexicographically above the whole deficit.
H5  TOOTHLESSNESS. At a (row, m) where ALL classes score zero the
    loss degenerates to the deficit mechanically. The mechanism
    observable for Q2: per (row, m), the zero-miss class count and
    the number of distinct scored-miss values.

PREDICTIONS (fixed before the run)
----------------------------------
P1  The controls pass: the m = 1 column reproduces
    explore_prediction_door.py (empty universal intersection under
    both orders, pooled best 171, readability partition 9 blocks
    pure / 8 composite with exactly id/sqrt2 + id/sqrt3 merged),
    and the m = infinity anchor reproduces deficit universality
    (a universal class exists, greedy inside). A failed control
    stops the read.
P2  Monotone emptiness along the grid -- empty on an initial
    segment, nonempty from some grid point on. MARKED TRANSPLANT:
    this is the imported shape H4 warns about; a non-monotone
    vector is a first-class outcome, not an anomaly.
P3  Any knife edge found is an INTERVAL, not a value: the report
    is the bracket [largest empty m, smallest nonempty m] with the
    integers between grid points named unscanned.
P4  Conservation is genuinely open; no outcome predicted. The
    observable is the FREE ADAPTATION table: (row, m) pairs with
    strict specialist advantage (in scored misses) whose composite
    partition block stays merged.
P5  = H1, asserted in-engine (a derived control).

EXPERIMENTS
-----------
E1  CONTROLS: the m = 1 reproduction, the anchor reproduction,
    the H1 asserts (subset nesting + row-minimum monotonicity +
    perfect-row zeros), class count 38 from 100 policies.
E2  THE DIAL CENSUS: per m -- per-row minimum / spread / argmin
    sizes (pure and composite) / zero-miss class counts, the
    universal intersections, the readability partitions (block
    counts and members), greedy's standing; the knife-edge
    summary as a bracket (P3).
E3  CONSERVATION AND PRICE: per m -- the pooled winner (total
    scored misses, deficit-product tiebreak), per-row strict
    specialist advantage, specialist pooled excess, merged-block
    flags, the FREE ADAPTATION verdicts.
E4  PLACEMENT SENSITIVITY: the universal-intersection vector under
    the first-anchored placement, printed beside the end-anchored
    one.
E5  THE SINGLE-BIT ATLAS: for every placement j in [0, 111], the
    universal intersections of the one-bit loss scoring index j
    alone -- the count of placements whose intersection is empty
    (pure and composite), and any placement admitting a universal
    class printed explicitly. Decides whether the single-bit break
    is placement-uniform or bit-dependent.
E6  THE ANCHOR PARTITION: the readability partition of the anchor
    itself -- rows grouped by their pure-deficit argmin sets. The
    baseline for every set-level readability claim: whether a
    stream-reading loss CREATES set-level readability (baseline
    one block) or merely COMPLETES it (baseline already split)
    depends on this print.

FINDINGS (from the runs; all controls green first)
--------------------------------------------------
E1  All controls pass: 38 classes from 100 policies; the scored
    sets nest and row minima are non-increasing along the divisor
    chains, with the eight perfect rows perfect at every m (H1
    asserted); the m = 1 column reproduces
    explore_prediction_door.py exactly (universal intersection
    empty under both orders, pooled best 171 with one winner,
    partition 9 blocks pure / 8 composite, the merged pair
    id/sqrt2 + id/sqrt3); the anchor reproduces deficit
    universality (one universal class, greedy inside).

E2  THE DIAL HAS NO KNIFE EDGE. The universal intersection is
    EMPTY at every grid m, under both the pure and the composite
    order -- down to m = 112, a single scored future bit. The
    anchor (zero stream bits) has universality; every positive
    bandwidth tried lacks it: the dial is a step at zero, not a
    threshold. The failure is never by agreement: eight of nine
    rows keep at least two distinct scored-miss values at every m.
    The toothlessness watch fired on exactly one row -- sq/sqrt2
    scores zero for all 38 classes at every m >= 2, because its
    entire discrimination (six classes missing 56 bits at m = 1)
    sits at even indices, the half the end-anchored S_2 does not
    score; a placement-sensitive fact, not a family one. The PURE
    readability partition stays FULLY DISCRETE (nine blocks) at
    every m including the single bit: the nine hitter-sets of one
    future bit are already pairwise distinct, so set-level row
    readability under the pure order needs no bandwidth at this
    scope (under the composite order -- the loss's own -- blocks
    do merge; see below). The COMPOSITE
    partition coarsens NON-MONOTONICALLY (blocks 8, 7, 7, 7, 6, 7,
    6, 6 across the grid): the triple {id/sqrt2, id/sqrt3, sq/phi}
    merges from m = 2 on, while {dbl/sqrt2, dbl/fib} merges at
    m = 16, splits again at m = 28, and re-merges at 56 and 112 --
    the non-monotonicity H4 warned about realizes in the
    partition, not in the emptiness vector. The aperiodic fib row
    becomes perfectly predictable in-family once the coupling
    thins: best misses 47, 21, 10, 3, 1, 1, 0, 0 along the grid.
    Greedy never returns to universality at any bandwidth: it
    stays out of the pure argmin on id/phi, id/theta8, and dbl/phi
    at every m -- it guesses even the single last bit wrong there.

E3  THE PRICE OF ADAPTATION COLLAPSES WITH BANDWIDTH, AND FREE
    ADAPTATION EXISTS. The conservation question resolves
    negative: at six of the eight grid points a strict specialist
    advantage coexists with a merged composite block (sq/phi at
    m = 2, 4, 8, 16, 28, 112; dbl/fib additionally at 16) -- the
    row's data strictly matters to the optimum while the row's
    identity stays ambiguous inside its merged block, not pinned
    by its optimum set. The exchange rate inverts as
    the coupling thins: at m = 1 a specialist pays roughly 4 to 15
    pooled misses per miss of row advantage (advantage 56/56/12
    against excess 222/287/175); by m = 8 the pooled excess is 1
    per specialist against advantages of 14 and 3; at m = 112 it is
    ZERO -- the sq/phi specialist ties the pooled winner's miss
    total (both sacrifice exactly one row's bit, different rows)
    and loses only the deficit tiebreak. Adaptation at one scored
    bit is free in the miss currency and priced only in trace
    geometry. (The definitional argument that a specialist's
    excess must be nonzero applies to the pure pooled order; the
    composite pooled order separates ties by deficit, which is
    exactly where the last of the price retreats.)

E4  Placement-insensitive at every m: the first-anchored vector is
    identical (empty everywhere, both orders).

E5  THE ATLAS IS TOTAL: all 112 single-bit placements have an
    empty universal intersection, pure and composite. EVERY future
    side bit, alone atop the full deficit tiebreak, breaks
    destination universality at this scope.

E6  THE BASELINE IS NOT BLANK. The anchor's own readability
    partition has THREE blocks: {id/phi, id/sqrt2, id/sqrt3,
    id/theta8, sq/phi} (a shared 5-class argmin set), {dbl/phi,
    dbl/sqrt2, dbl/fib} (argmin = the universal class ALONE), and
    {sq/sqrt2} (an 11-class argmin set). Even the pure deficit's
    argmin SETS read some stream data: sq/sqrt2 and sq/phi share a
    map and differ only in stream, yet their argmin sets differ
    (11 vs 5 classes) -- a stream-driven split with no future bit
    scored. So the stream-reading loss COMPLETES set-level
    readability rather than creating it from zero: the anchor's
    three blocks refine to nine under the pure miss order at every
    m, and to six-to-eight under the composite order along the
    grid. The state-level
    data-freeness of the trace-loss optimum (the factoring
    witness) and the universality contrast (nonempty vs empty
    intersection) are untouched: what varies by stream at the
    anchor is which classes TIE with the universal optimum, never
    the optimum itself.

READING. explore_prediction_door.py opened the door at full
coupling; this experiment measures its threshold and finds none: the
data-dependence of the optimum is not bought by bandwidth --
one future bit anywhere in the window already forces it, while
zero bits restore universality. Set-level readability of the row
is equally bandwidth-free under the pure order -- and has a
nonzero zero-bandwidth baseline: the anchor's argmin sets already
carry a three-block partition with one stream-driven split (E6),
so the door completes the partition rather than opening it from
blank. What bandwidth
DOES buy is the price structure: thick coupling makes adaptation
expensive (pooled misses per advantage), thin coupling makes it
first cheap, then miss-free, with the residual price paid in the
trace-geometry tiebreak -- and free adaptation (advantage without
readability refinement) prints throughout the thin regime.
Predictions against outcomes: P2's transplant-marked monotone
shape failed in the unanticipated direction -- not non-monotone,
but with no return point at all; the knife-edge question dissolved
rather than resolved, so P3's interval discipline had nothing to
fire on.
Tier: H1 is proved; everything else is exact and exhaustive at
the stated scope (this policy space, these nine rows, this loss
family, horizon 120) only.

Run record: run 1 (E1-E4) exit 0, all controls green, 1.0s;
run 2 (E5 added) exit 0, controls green, E1-E4 output unchanged,
3.4s; run 3 (E6 added) exit 0, controls green, E1-E5 output
unchanged, 3.4s.

DESIGN
------
Everything heavy is imported verbatim from
explore_prediction_door.py: streams, cylinder/image machinery, the
reader engine, the truth targets, the behavioral quotient with
per-step hit vectors and deficits. This script only re-scores the
frozen hit vectors on the scored subsets and runs the census per
grid point. Exact integer arithmetic throughout; the pooled
tiebreak multiplies deficit triples (numerators, denominators,
infinity flags OR), preserving the lexicographic semantics. Grid:
m in {1, 2, 4, 8, 16, 28, 56, 112}; anchor m = infinity as the
empty scored set.
"""

import time

from explore_prediction_door import (
    N0, HORIZON, DEEP, ROWS, FIB_ROW, fmt_row, cmp_lex,
    build_images, truth_targets, build_classes, check,
)

GRID = [1, 2, 4, 8, 16, 28, 56, 112]
NBITS = HORIZON - N0          # 112 counted bits, indices 0..111
LAST = NBITS - 1              # the last counted index


def scored_set(m, anchor="end"):
    if m is None:
        return []
    if anchor == "end":
        return [i for i in range(NBITS) if (LAST - i) % m == 0]
    return [i for i in range(NBITS) if i % m == 0]


def scored_miss(cls, row, S):
    hits = cls["rows"][row]["hits"]
    return sum(1 for i in S if not hits[i])


def mul_deficit(a, b):
    return (a[0] * b[0], a[1] * b[1], a[2] or b[2])


def census_at(classes, S):
    """Argmin structure of L_m with scored set S. Returns a dict:
    per-row miss lists, pure/composite argmins, intersections."""
    out = {"miss": {}, "pure": {}, "comp": {}}
    for row in ROWS:
        losses = [scored_miss(c, row, S) for c in classes]
        best = min(losses)
        pure = [ci for ci, v in enumerate(losses) if v == best]
        bestd = None
        comp = []
        for ci in pure:
            d = classes[ci]["rows"][row]["deficit"]
            if bestd is None or cmp_lex(d, bestd) < 0:
                bestd = d
                comp = [ci]
            elif cmp_lex(d, bestd) == 0:
                comp.append(ci)
        out["miss"][row] = losses
        out["pure"][row] = set(pure)
        out["comp"][row] = set(comp)
    out["uni_pure"] = set.intersection(*(out["pure"][r] for r in ROWS))
    out["uni_comp"] = set.intersection(*(out["comp"][r] for r in ROWS))
    return out


def partition(argmin):
    blocks = {}
    for row in ROWS:
        blocks.setdefault(frozenset(argmin[row]), []).append(row)
    return blocks


def greedy_classes(classes):
    out = set()
    for ci, c in enumerate(classes):
        for pol in c["members"]:
            if pol[2] == 0 and pol[3] == 0:
                out.add(ci)
    return out


def pooled_winners(classes, cen):
    """Composite pooled order: total scored misses, then the
    product of per-row deficit triples."""
    totals = [sum(cen["miss"][row][ci] for row in ROWS)
              for ci in range(len(classes))]
    best = min(totals)
    tied = [ci for ci, t in enumerate(totals) if t == best]
    bestd = None
    winners = []
    for ci in tied:
        d = (1, 1, False)
        for row in ROWS:
            d = mul_deficit(d, classes[ci]["rows"][row]["deficit"])
        if bestd is None or cmp_lex(d, bestd) < 0:
            bestd = d
            winners = [ci]
        elif cmp_lex(d, bestd) == 0:
            winners.append(ci)
    return best, winners, totals


def main():
    t0 = time.time()
    print("THE BANDWIDTH DIAL -- L_m = next-side misses on every"
          " m-th counted step, deficit tiebreak")
    print("grid m: %s + anchor (pure deficit); %d counted bits,"
          " end-anchored" % (GRID, NBITS))
    print()
    imgs = build_images(DEEP)
    targets = {row: truth_targets(imgs[row]) for row in ROWS}
    classes = build_classes(imgs, targets)
    gcls = greedy_classes(classes)

    print("E1 CONTROLS")
    ok = True
    npol = sum(len(c["members"]) for c in classes)
    ok &= check("quotient size", (len(classes), npol) == (38, 100),
                "%d classes / %d policies" % (len(classes), npol))

    # H1: subset nesting + row-minimum monotonicity + perfect rows
    nest_ok = True
    for a in GRID:
        for b in GRID:
            if b % a == 0 and a < b:
                nest_ok &= set(scored_set(b)) <= set(scored_set(a))
    ok &= check("H1 scored sets nest along divisor chains", nest_ok)
    cen = {m: census_at(classes, scored_set(m)) for m in GRID}
    cen[None] = census_at(classes, [])
    mono_ok = True
    for a in GRID:
        for b in GRID:
            if b % a == 0 and a < b:
                for row in ROWS:
                    if min(cen[b]["miss"][row]) > min(cen[a]["miss"][row]):
                        mono_ok = False
    ok &= check("H1 row minima non-increasing along chains", mono_ok)
    perf_ok = all(min(cen[m]["miss"][row]) == 0
                  for m in GRID for row in ROWS if row != FIB_ROW)
    ok &= check("H1 perfect rows stay perfect at every m", perf_ok)

    # m = 1 reproduction of explore_prediction_door.py
    c1 = cen[1]
    ok &= check("m=1 universal intersection empty (pure, comp)",
                (len(c1["uni_pure"]), len(c1["uni_comp"])) == (0, 0))
    pbest, pwin, _ = pooled_winners(classes, c1)
    ok &= check("m=1 pooled best 171", pbest == 171,
                "best %d, winners %d" % (pbest, len(pwin)))
    bp, bc = partition(c1["pure"]), partition(c1["comp"])
    merged = [rows for rows in bc.values() if len(rows) > 1]
    ok &= check("m=1 partition 9 pure / 8 comp blocks",
                (len(bp), len(bc)) == (9, 8))
    ok &= check("m=1 merged pair is id/sqrt2 + id/sqrt3",
                len(merged) == 1 and
                sorted(merged[0]) == [("id", "sqrt2"), ("id", "sqrt3")])

    # anchor reproduction: pure deficit universality, greedy inside
    ca = cen[None]
    ok &= check("anchor universal class exists",
                len(ca["uni_comp"]) > 0,
                "%d class(es)" % len(ca["uni_comp"]))
    ok &= check("anchor greedy inside", gcls <= ca["uni_comp"],
                "greedy classes: %d" % len(gcls))
    if not ok:
        print("CONTROL FAILURE -- stop; no verdict may be read.")
        raise SystemExit(1)
    print()

    print("E2 THE DIAL CENSUS")
    for m in GRID:
        c = cen[m]
        print("  m = %3d (%d scored bit(s))" % (m, len(scored_set(m))))
        for row in ROWS:
            losses = c["miss"][row]
            best, worst = min(losses), max(losses)
            nzero = sum(1 for v in losses if v == 0)
            ndist = len(set(losses))
            gin = any(ci in gcls for ci in c["pure"][row])
            print("    %-10s best %3d worst %3d | argmin %2d/%d"
                  " (comp %2d) | zero-miss %2d distinct %2d |"
                  " greedy in argmin: %s"
                  % (fmt_row(row), best, worst, len(c["pure"][row]),
                     len(classes), len(c["comp"][row]), nzero, ndist,
                     "yes" if gin else "NO"))
        bp, bc = partition(c["pure"]), partition(c["comp"])
        print("    universal intersection pure %d comp %d |"
              " partition blocks pure %d comp %d"
              % (len(c["uni_pure"]), len(c["uni_comp"]),
                 len(bp), len(bc)))
        for key, rows in sorted(bc.items(),
                                key=lambda kv: fmt_row(kv[1][0])):
            if len(rows) > 1:
                print("    comp block merged: {%s} argmin size %d"
                      % (", ".join(fmt_row(r) for r in rows), len(key)))
    print("  KNIFE-EDGE SUMMARY (composite; then pure)")
    for label, k in (("comp", "uni_comp"), ("pure", "uni_pure")):
        vec = [(m, len(cen[m][k])) for m in GRID]
        print("    %s: %s" % (label,
              "  ".join("m=%d:%d" % mv for mv in vec)))
        empty = [m for m, v in vec if v == 0]
        nonempty = [m for m, v in vec if v > 0]
        if empty and nonempty:
            lo = max(empty)
            hi = min(v for v in nonempty if v > lo) \
                if any(v > lo for v in nonempty) else None
            if hi is not None:
                print("    %s knife edge: an INTERVAL -- empty still"
                      " at m=%d, nonempty by m=%d; integers in"
                      " (%d, %d) unscanned" % (label, lo, hi, lo, hi))
        elif not nonempty:
            print("    %s: empty at every grid m -- one scored bit"
                  " already breaks universality" % label)
        else:
            print("    %s: nonempty at every grid m" % label)
    print()

    print("E3 CONSERVATION AND PRICE")
    for m in GRID:
        c = cen[m]
        best, winners, totals = pooled_winners(classes, c)
        bc = partition(c["comp"])
        merged_rows = set()
        for key, rows in bc.items():
            if len(rows) > 1:
                merged_rows.update(rows)
        print("  m = %3d pooled best %3d, winners %d class(es)"
              % (m, best, len(winners)))
        free = []
        for row in ROWS:
            best_r = min(c["miss"][row])
            pooled_r = min(c["miss"][row][ci] for ci in winners)
            regret = pooled_r - best_r
            if regret > 0:
                spec = [ci for ci, v in enumerate(c["miss"][row])
                        if v == best_r]
                excess = min(totals[ci] for ci in spec) - best
                tag = ""
                if row in merged_rows:
                    tag = "  <-- FREE ADAPTATION (block merged)"
                    free.append(row)
                print("    %-10s specialist advantage %3d, pooled"
                      " excess %3d%s"
                      % (fmt_row(row), regret, excess, tag))
        if not free:
            print("    no FREE ADAPTATION print at this m")
    print()

    print("E4 PLACEMENT SENSITIVITY (first-anchored scored sets)")
    for m in GRID:
        c = census_at(classes, scored_set(m, anchor="first"))
        print("  m = %3d uni pure %d comp %d   (end-anchored: pure"
              " %d comp %d)"
              % (m, len(c["uni_pure"]), len(c["uni_comp"]),
                 len(cen[m]["uni_pure"]), len(cen[m]["uni_comp"])))
    print()

    print("E5 THE SINGLE-BIT ATLAS (all %d placements)" % NBITS)
    empty_p = empty_c = 0
    open_placements = []
    for j in range(NBITS):
        c = census_at(classes, [j])
        if len(c["uni_pure"]) == 0:
            empty_p += 1
        if len(c["uni_comp"]) == 0:
            empty_c += 1
        else:
            open_placements.append((j, len(c["uni_comp"])))
    print("  empty universal intersection: pure %d/%d placements,"
          " comp %d/%d" % (empty_p, NBITS, empty_c, NBITS))
    if open_placements:
        print("  placements admitting a universal class (comp):")
        for j, sz in open_placements:
            print("    bit %d (step %d): %d universal class(es)"
                  % (j, N0 + j, sz))
    else:
        print("  no single-bit placement admits a universal class:"
              " every future bit breaks universality")
    print()

    print("E6 THE ANCHOR PARTITION (pure-deficit baseline)")
    blocks = partition(cen[None]["comp"])
    print("  %d block(s)" % len(blocks))
    for key, rows in sorted(blocks.items(),
                            key=lambda kv: fmt_row(kv[1][0])):
        print("    {%s} argmin set size %d"
              % (", ".join(fmt_row(r) for r in rows), len(key)))
    print()
    print("done in %.1fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
