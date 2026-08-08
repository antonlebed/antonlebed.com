"""Is the empty middle window empty of ATTAINABLE coordinates, or only
of the class's own? The fork explore_slope_empty.py left, taken.

THE QUESTION. explore_slope_empty.py's J3 measured a dichotomy: a
NON-CONTAINED pair of maximal levels whose meeting measure mu is small
enough never meets -- 0.0000 across 20,128 such pairs below mu = 0.3 --
so beneath that measure a pair CONTAINS or MISSES and the middle is
empty. Its J4 established that the coordinate is not near the boundary
(y clears the meeting radius by 1.098x at the tightest, 2.938x at the
median), so no discreteness argument reaches it, and named the handle
without taking it: y qualifies as a carry iff sigma.y mod n < b^Delta,
so the y a pair COULD carry are a Steinhaus set of b^Delta points and
the window's emptiness would be a three-distance statement about
sigma/n. That is a claim about the SET. Nothing in that file measured
it. The window could equally be full of attainable y that the carries
simply never pick, and those are different laws with different objects:
one is about sigma, the other about the class map's carry sequence.
This asks which.

Notation is the family's, unchanged: N = L b^c, g = gcd(q, N),
n = N/g, sigma = q/g a unit of Z/n, r_j the repunit, M_j = a r_j,
Delta = j - i for a pair of levels i < j, and y the coordinate of
explore_slope_empty.py's (P), for which

    CONTAINMENT   needs  y <= 2 M_Delta,
    MEETING       needs  y <= 2 M_j  or  y >= n - 2 M_j + 2 M_Delta.

THE DERIVATION, hand-attacked on paper before this engine existed.

(R) THE ATTAINABLE SET IS A THREE-DISTANCE SET, AND ITS SIZE IS b^Delta.
    explore_slope_width.py's (H) writes the coordinate as
    y = sigma^{-1} (R/g) mod n with the M_Delta shift OUTSIDE the
    inverse, and under the rigidity that census runs at -- D = g - 1,
    span = 2E + 1, E exact -- R/g is the carry floor(b^Delta t_i / g)
    of the class map's own multiplication, an integer in [0, b^Delta)
    because t_i < g. So over all classes of a cell, at a fixed level
    pair, y ranges inside

        Y_Delta = {sigma^{-1} C mod n : 0 <= C < b^Delta}
                = {y in Z/n : sigma.y mod n < b^Delta},

    which is b^Delta points whose gaps take at most three values (the
    three-distance theorem applied to sigma/n). The membership test is
    one multiplication, so the set never needs building.

(S) THE WINDOW, AND WHY THE FORK IS SHARP. A non-contained pair meets
    only if y sits in one of the two arcs (P) admits, so the region
    that decides the dichotomy is

        W = (2 M_Delta, 2 M_j]  union  [n - 2 M_j + 2 M_Delta, n),

    of total length 4 M_j - 2 M_Delta - 2 M_Delta = mu.n - 4 M_Delta - 1
    give or take the endpoints -- essentially the pair's whole measure
    minus its containment arc. Now M_j = b^Delta M_i + M_Delta exactly,
    so the lower arc alone has length 2 b^Delta M_i. If Y_Delta were
    spread evenly, the count inside W would be about

        b^Delta . |W| / n  ~  b^Delta . mu,

    which for the census's own shallow median mu = 0.178 exceeds 1 as
    soon as b^Delta >= 6, and b^Delta is the ratio of the two radii and
    is typically far larger than that. So an empty W is NOT what an
    evenly placed Y_Delta would give, and measuring |Y_Delta cap W|
    separates two laws that the parent's numbers cannot tell apart.

    THE PREDICTION, fixed here and read after: I expect W to hold
    attainable y at most pairs -- the counting above is not close --
    and therefore expect the object to be the CARRY rather than sigma,
    which would make J4's three-distance handle the wrong instrument
    and is worth knowing before anything is built on it.

THE DESIGN, frozen before the engine.

E-H THE CONTROLS, four, run and read before any verdict.
    (1) THE CLASS'S OWN COORDINATE IS ATTAINABLE. At every pair of the
        census, test sigma.y mod n < b^Delta. This is (R) put to the
        question directly and it can fail: (H)'s carry collapse has a
        precondition and this file does not check the precondition, it
        checks the consequence. If it fails anywhere, the attainable
        set is not what (R) says and nothing below means what it says.
    (2) OWN-y INSIDE W IMPLIES A NON-EMPTY COUNT. Wherever the class's
        own y lands in W, the C-loop must report at least one member --
        two computations (interval membership on y, and a loop over
        carries) that share no code path, so agreement is a control
        and not a restatement. Run over the WHOLE census and never over
        the below-cut population alone, where it has no content: there
        the own y is attainable by (1) and the attainable set turns out
        to miss W, so own-y-outside-W is a THEOREM and the check cannot
        fail. The count of pairs it actually ran on is printed beside
        it, since a control's verdict is worth its case count.
    (3) THE DICHOTOMY REPRODUCED through this file's own path: the
        non-contained meeting rate by mu bucket, and the count of
        non-contained pairs below the cut. A mechanism explained
        against numbers this file did not reproduce is a mechanism for
        somebody else's census.
    (4) THE MEETING ARC IS NECESSARY, re-tested here: no pair meets
        with y outside W union the containment arc. It is the half
        explore_slope_empty.py asserts and everything here rests on it.

E-I THE FORK MEASURED. Over every non-contained pair below the mu cut,
    count |Y_Delta cap W| by looping C over [0, b^Delta) and testing
    membership of sigma^{-1} C mod n in the two arcs. Report the
    distribution of that count, the fraction at zero, and -- since the
    loop is O(b^Delta) and b^Delta is unbounded above by anything this
    file controls -- the number of pairs skipped by the loop cap, so a
    census that quietly dropped its hard cases says so.

E-J WHAT THE CARRIES DO. If W holds attainable y, the object is which
    C the classes realize. Report the realized carry C = sigma.y mod n
    as a FRACTION of b^Delta over the same population, with its
    quantiles, beside the fraction of [0, b^Delta) that maps into W.
    If the realized carries were spread over [0, b^Delta) the second
    number would be the meeting rate, and the dichotomy says it is not:
    so the gap between the two is exactly the size of what a
    derivation still owes.

E-K, E-L, E-M and E-N were frozen LATER, each after the pass before it
printed and before it was written; each carries its own freeze in its
own function docstring, which is where the reason it exists is legible.

KILLS, frozen as what this rig PRINTS.

K1 A control of E-H misses -> the attainable set, the window or the
   reproduction is wrong and nothing below is read.
K2 |Y_Delta cap W| = 0 at every non-contained pair below the cut ->
   the middle window is empty of ATTAINABLE coordinates, the carry is
   irrelevant to the dichotomy, and what is owed is a gap statement
   about sigma/n -- J4's handle is the right one. AS FROZEN this kill
   is absolute ("every"), which is a shape the census can only refute:
   it read 3508 of 3516, so the kill did not fire AS WRITTEN and the
   exceptions are reported as the residual rather than the verdict
   being rounded up to it. The scope is corrected here, not the
   finding written around it.
K3 |Y_Delta cap W| > 0 at a substantial fraction of them -> the window
   is NOT empty of attainable y, the object is the carry sequence and
   not sigma, and J4's three-distance frame is the wrong instrument
   for this dichotomy. This is what (S) predicts.
K4 A pair whose own y is not attainable -> (R) is wrong at this scope.

POSITIVE CONTROL, run and read before any verdict line: E-H whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

L1 THE WINDOW IS EMPTY OF ATTAINABLE COORDINATES, NOT MERELY OF THE
   CLASS'S OWN -- and (S)'s prediction was WRONG. |Y_Delta cap W| = 0
   at 3508 of the 3516 non-contained pairs below mu = 0.4, with no pair
   skipped by the loop cap. NEITHER KILL FIRED AS FROZEN: K2 demanded
   every pair and got 3508, K3 demanded a substantial fraction and got
   0.0023. What the census actually says sits between the two shapes
   the slate offered, which is a defect in the slate and not a result
   to be rounded -- and the 8 exceptions are L4, one cell. The counting
   argument of (S) misses by a factor of about 800, not the three
   orders a first reading of the printed 0.0003 suggests: the fraction
   of [0, b^Delta) landing in W has mean 0.0003 against the ~mu = 0.2
   an evenly placed Y_Delta would give. The mean is the weak way to say
   it and is carried entirely by the 8 exceptions; the strong way is
   that the fraction is EXACTLY zero at 3508 of 3516 and its median is
   0.0000. So the
   dichotomy is a fact about sigma and the radii, not about which carry
   the class map happens to realize. The carry does no work because
   there is no carry for it to do work with -- the emptiness is of the
   whole set. E-J's realized-carry quartiles (0.2500, 0.3333, 0.5000 of
   b^Delta) are NOT a second piece of evidence for that and are not
   read as one: with b^Delta = 4 at most pairs and the containing
   carries filtered out, the only values left are 1 and 2, so the
   spread is forced by the census rather than observed in it. The
   controls that let this be read: the class's own y is an attainable
   carry at 1,786,658 of
   1,786,658 pairs, which is (R) tested by its consequence rather than
   its precondition; the carry loop and interval membership agree at
   all 6792 pairs whose own y lands in W, a population that exists
   only above the cut and is empty below it; no pair meets with y
   outside the arcs; and the dichotomy reproduces through this file's
   own path at
   0.0000 across all four buckets below the cut, 3516 pairs.

L2 AND THE ATTAINABLE SET IS TINY, WHICH RETIRES THE THREE-DISTANCE
   HANDLE RATHER THAN CONFIRMING IT. Over the whole below-cut
   population b^Delta takes four values -- 4 at 2784 pairs, 6 at 688,
   10 at 12, 36 at 32 -- so Y_Delta is at most 36 points and at 2784
   of 3516 it is exactly FOUR. explore_slope_empty.py's J4 named the
   emptiness "a THREE-DISTANCE statement about sigma/n" and pointed at
   explore_slope_dodge.py's instrument for it. The statement is true
   and the instrument is oversized: a three-distance theorem counts
   gaps in a set large enough for the count to mean something, and
   this one is four points. What the emptiness actually needs is a
   finite check, which is a cheaper thing to owe and a different one.

L3 THE SHAPE: THE CONTAINING CARRIES ARE AN ARITHMETIC PROGRESSION OF
   STEP 3, AND THE REST OF Y_Delta IS ALREADY PAST THE MEETING RADIUS.
   The containing carries S = {C : y_C <= 2 M_Delta} are EXACTLY the
   multiples of their least positive member below b^Delta at 3508 of
   3516; that member is 3 at 3324 pairs and 5 or more at 192; and
   |S| = 2 at 3480, so S = {0, 3} at nearly every pair. The fraction
   of Y_Delta inside the containment arc then has median and max 0.5000
   and min 0.2000, and THAT IS NOT A THIRD FACT: where S is a
   progression |S| = ceil(b^Delta / s), checked at the same 3508, so
   the fraction is ceil(b^Delta/s)/b^Delta and both extremes are read
   off s and b^Delta rather than measured -- 2/4 at the top and 2/10 at
   the bottom, which are exactly the printed 0.5000 and 0.2000. The
   half is a consequence of the step being at least 3 and carries no
   evidence of its own. Past it, the least attainable y sits at 1.95x
   the MEETING radius at the first quartile and 2.75x at the median,
   exceeding it at 3508 of 3516, and the upper arc is clear at 3516 of
   3516 though by only 1.0051x at the tightest, which is the one place
   the shape is delicate. So the sentence the dichotomy reduces to is:
   the first attainable coordinate past the containment radius is
   already past the meeting radius -- one radius apart in the
   statement, a factor of about 2.75 apart in fact.

L4 THE RESIDUAL IS ONE CELL, AND THE THREE WAYS OF FAILING ARE ONE
   FAILURE. All 8 exceptions -- the pairs where W does hold attainable
   y, 4 of them each, and the class's carry declines every one -- are
   the SAME cell at the SAME level pair: N = 54432,
   (b, a, c, u, v) = (6, 3, 5, 9088, 7), levels 1 and 3, b^Delta = 36,
   mu = 0.2792, at eight classes t = 3, 7, 9, 13, 19, 23, 25, 29. So
   the carry decides in one place in the census and sigma everywhere
   else, and that place is a single object to derive against rather
   than a scattered population.
   AND THE THREE RESIDUALS OF E-I, E-K AND E-L ARE THE SAME EIGHT
   PAIRS, set-equal and not merely equinumerous (E-M, which exists
   because three counts of eight printed side by side are an invitation
   to read a coincidence as an identity). The window holds an
   attainable y exactly where the least attainable point past
   containment fails to clear the meeting radius, and exactly where S
   stops being an arithmetic progression. That welds L3 to L1: the
   progression SHAPE and the empty window are one fact seen twice, so
   deriving why S is a progression of step 3 would derive the
   dichotomy, and the eight places the shape breaks are the eight
   places the dichotomy has an exception. That is a sharper handoff
   than three separate residuals of equal size.

L5 AND b^Delta IS SMALL BECAUSE OF mu, NOT BECAUSE OF N -- SO L2 IS A
   PROPERTY OF THE QUESTION AND NOT A SCOPE STATEMENT. The census
   reaches Delta = 5 (18,560 pairs) and is thick at every value from 1
   to 5, with 880,114 at Delta = 1. The below-cut population reaches
   Delta = 2. Only: 3484 pairs at Delta = 1 and 32 at Delta = 2, and
   nothing above. So the cut is doing the work and the cap is not, and
   the derivation is short: mu is essentially 4 M_j / n, so mu < 0.4
   forces M_j < 0.1 n; M_j = a r_j grows like b^j, so a small M_j
   forces a small j; and Delta <= j. The surviving level pairs say the
   same thing more sharply -- (1,2) at 3452, (1,3) at 32, (2,3) at 32,
   and no other pair at all -- so the whole dichotomy lives at the
   three shallowest levels. That closes the first of the two questions
   the handoff was carrying: b^Delta is bounded because the measure cut
   bounds it, and a wider N cannot change that. What is left open is
   why the step is 3.

VERDICT, by piece.
  - (R), THE ATTAINABLE SET, is a PROPERTY at the census's rigidity:
    derived from (H)'s carry collapse, checked by its consequence at
    1,786,658 pairs with 0 misses.
  (SETTLED SINCE: explore_slope_step.py derives the step as
  kappa/(h g) and turns L1 into an exhaustive criterion -- the lower
  arc is empty iff (h r_Delta + 1) step >= b^Delta -- under which the 8
  exceptions below are not exceptions but the criterion's other side.
  What survives here unchanged: every measurement, and the demotion of
  the three-distance frame.)
  - THE EMPTY WINDOW (L1) is a PATTERN and deliberately not a rule: a
    rule is exhaustive over its stated range and this one has 8
    exceptions inside its range, so calling it a rule would mean
    carving the named cell out of the scope to keep the tier, which is
    the move that makes tiers worthless. It is nonetheless a STRONGER
    statement than the one it replaces, holding of every coordinate the
    pair COULD carry and not only of the one it does, at N <= 60,000
    and phase 0.
  - THE SHAPE (L3) is a PATTERN: S is an arithmetic progression at
    3508 of 3516 and its step is 3 at most of them, with no derivation
    here of why 3.
  - J4's THREE-DISTANCE FRAME is DEMOTED, not confirmed (L2): true as
    stated and the wrong size for the object -- and the demotion is
    itself a PROPERTY rather than a census reading, since L5 derives
    the smallness from the measure cut instead of observing it.

RUN RECORD: pure Python, integers only, standard library;
explore_slope_assemble.py's level_data, explore_slope_width.py's
solved_cells, and explore_slope_empty.py's pair_y and pair_report
imported rather than copied, so the window this file loops over is the
window that file measured. 118.2 s wall, peak working set 34.1 MB
against the 512 MB analysis ceiling (memwatch.py); the census is
solved_cells at N <= 60,000, phase 0, below-count >= 3, walked four
times (once per pass) rather than held in memory, which is what keeps
the footprint flat. Every attainable-set loop runs to completion: the
b^Delta cap of 200,000 is never reached, so no pair is skipped.
Prints reproduced by:
python prime/code/explore_slope_window.py
"""

import os
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_slope_assemble import level_data  # noqa: E402
from explore_slope_width import solved_cells  # noqa: E402
from explore_slope_empty import pair_y, pair_report  # noqa: E402

FAILURES = []
MU_CUT = 0.4
LOOP_CAP = 200000
CTRL_CAP = 20000


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def window(n, MD, Mj):
    """(S)'s W: the two arcs a non-contained pair must land in to meet.
    Returned as (lo1, hi1, lo2, hi2), both inclusive."""
    return (2 * MD + 1, 2 * Mj, n - 2 * Mj + 2 * MD, n - 1)


def in_window(y, w):
    return w[0] <= y <= w[1] or w[2] <= y <= w[3]


def attainable_in_window(n, sigma_inv, bd, w, cap=None):
    """|Y_Delta cap W| by (R)'s loop over carries. Returns None if the
    loop would exceed the cap -- a skip that is reported, never a zero."""
    if bd > (LOOP_CAP if cap is None else cap):
        return None
    cnt = 0
    y = 0
    for _ in range(bd):
        if in_window(y, w):
            cnt += 1
        y += sigma_inv
        if y >= n:
            y -= n
    return cnt


def walk(cap, min_below=3):
    """Every pair of lost levels of the census, with (R)'s data."""
    cells = solved_cells(cap, min_below)
    for N, key, ce, two in cells:
        b, a = key[0], key[1]
        n, g, q = ce["n"], ce["g"], ce["q"]
        sigma = (q // g) % n
        sigma_inv = pow(sigma, -1, n)
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            deep = [x for x in lv if x["j"] > 0]
            for i in range(len(deep)):
                for k in range(i + 1, len(deep)):
                    yield (N, key, t, b, a, n, sigma, sigma_inv,
                           deep[i], deep[k])


def run(cap):
    print(f"THE CENSUS, N <= {cap}")
    t0 = time.time()
    pairs = 0
    # E-H controls
    bad_attain = bad_cross = bad_arc = 0
    cross_seen = cross_skip = 0
    first_bad_attain = None
    # E-H (3): the dichotomy through this file's path
    nc_buckets = {}
    # E-I / E-J
    counts = {}
    skipped = 0
    below = 0
    zero_w = 0
    frac_realized = []
    exc = []
    frac_window = []
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap):
        pairs += 1
        r = pair_report(b, a, n, A, C)
        y, _, MD, bd = pair_y(b, a, n, A, C)
        w = window(n, MD, C["M"])
        # (1) the class's own coordinate is attainable
        carry = (sigma * y) % n
        if carry >= bd:
            bad_attain += 1
            if first_bad_attain is None:
                first_bad_attain = (N, key, t, A["j"], C["j"], carry, bd)
        # (4) the meeting arc is necessary
        if r["meets"] and not (r["contained"] or in_window(y, w)):
            bad_arc += 1
        if not r["contained"]:
            bk = min(9, int(r["mu"] * 10))
            m, tt = nc_buckets.get(bk, (0, 0))
            nc_buckets[bk] = (m + (1 if r["meets"] else 0), tt + 1)
        # (2) own y in W implies the count is non-zero. Run over the
        # WHOLE census and not the below-cut population, where it has
        # no content: there the own y is attainable and the attainable
        # set misses W, so own-y-outside-W is a theorem and the check
        # could not fail. Above the cut pairs do meet, and then the
        # own y is IN W and the loop must find it
        if in_window(y, w):
            cross_seen += 1
            c2 = attainable_in_window(n, sigma_inv, bd, w,
                                      cap=CTRL_CAP)
            if c2 is None:
                cross_skip += 1
            elif c2 == 0:
                bad_cross += 1
        if r["contained"] or r["mu"] >= MU_CUT:
            continue
        below += 1
        cnt = attainable_in_window(n, sigma_inv, bd, w)
        if cnt is None:
            skipped += 1
            continue
        counts[min(cnt, 20)] = counts.get(min(cnt, 20), 0) + 1
        if cnt == 0:
            zero_w += 1
        else:
            # the residual: W holds an attainable y and the class's own
            # carry declines it. Exhibited rather than counted, since
            # this is the only population where the carry does the work
            exc.append((N, key, t, A["j"], C["j"], bd, cnt,
                        round(r["mu"], 4)))
        frac_realized.append(carry / bd)
        frac_window.append(cnt / bd)
    el = time.time() - t0
    print(f"E-H  THE CONTROLS   [{el:.1f} s]")
    print(f"  pairs read: {pairs}")
    print(f"  (1) own y NOT attainable (sigma.y mod n >= b^Delta): "
          f"{bad_attain}" + (f"; first {first_bad_attain}"
                             if first_bad_attain else ""))
    print(f"  (2) own y in W but the carry loop counts 0: "
          f"{bad_cross}, over {cross_seen} pairs whose own y IS in W "
          f"({cross_skip} skipped, b^Delta > {CTRL_CAP}) -- a control "
          f"run over the below-cut population alone would have had "
          f"ZERO such pairs and could not have failed")
    print(f"  (4) a pair meeting with y outside the containment arc "
          f"and W: {bad_arc}")
    ok(bad_attain == 0, "(R): the class's own y is an attainable carry")
    ok(bad_cross == 0, "the window loop agrees with window membership")
    ok(bad_arc == 0, "(P)'s meeting arc is necessary")
    print("  (3) the dichotomy reproduced, NON-CONTAINED pairs only:")
    for bk in sorted(nc_buckets):
        m, tt = nc_buckets[bk]
        print(f"      mu [{bk / 10:.1f},{(bk + 1) / 10:.1f}) | "
              f"{tt:7d} pairs | meet {m:6d} | rate {m / tt:.4f}")
    if FAILURES:
        print("\nK1: controls failed -- nothing below is read.")
        return
    print(f"E-I  THE FORK, non-contained pairs with mu < {MU_CUT}")
    print(f"  population {below}; skipped by the loop cap "
          f"(b^Delta > {LOOP_CAP}): {skipped}")
    print(f"  |Y_Delta cap W| distribution (20 = twenty or more): "
          f"{dict(sorted(counts.items()))}")
    meas = below - skipped
    if meas:
        print(f"  K2 (W empty of ATTAINABLE y): {zero_w} of {meas}  "
              f"= {zero_w / meas:.4f}")
        print(f"  K3 (W holds attainable y): {meas - zero_w} of {meas}  "
              f"= {(meas - zero_w) / meas:.4f}")
    for e in exc[:10]:
        print(f"    N={e[0]} {e[1]} t={e[2]} levels {e[3]},{e[4]}: "
              f"b^Delta={e[5]}, |Y cap W|={e[6]}, mu={e[7]}")
    if frac_window:
        fw = sorted(frac_window)
        fr = sorted(frac_realized)
        print("E-J  WHAT THE CARRIES DO")
        print(f"  fraction of [0, b^Delta) landing in W: min {fw[0]:.4f}, "
              f"median {fw[len(fw) // 2]:.4f}, mean "
              f"{sum(fw) / len(fw):.4f}, max {fw[-1]:.4f}")
        print(f"  the REALIZED carry as a fraction of b^Delta: "
              f"min {fr[0]:.4f}, q1 {fr[len(fr) // 4]:.4f}, median "
              f"{fr[len(fr) // 2]:.4f}, q3 {fr[3 * len(fr) // 4]:.4f}, "
              f"max {fr[-1]:.4f}")


def e_k_where(cap, min_below=3):
    """E-K, frozen after E-I printed and before this pass was written.
    E-I answered the fork against (S)'s prediction: W is empty of
    ATTAINABLE y, not merely of the class's own. That turns the object
    into the placement of Y_Delta, and the placement has a shape worth
    naming rather than a rate worth reporting. The containment arc is
    [0, 2 M_Delta] and the meeting arc is [0, 2 M_j], one coordinate at
    two radii; if the window between them is empty of attainable points
    then the FIRST attainable point above the containment radius is
    already above the MEETING radius, and the dichotomy is that
    sentence. So measure it as a ratio: lo = (least attainable
    y > 2 M_Delta) / (2 M_j), which exceeds 1 exactly when the lower
    arc is empty, and hi = (n - greatest attainable y) /
    (2 M_j - 2 M_Delta), which exceeds 1 exactly when the upper arc is.
    A ratio barely above 1 would say the window closes by a hair and
    the statement is delicate; a ratio far above 1 says the attainable
    set has a gap around the containment arc that dwarfs the window,
    which is a three-distance statement with room in it."""
    print(f"E-K  WHERE THE ATTAINABLE POINTS SIT, N <= {cap}")
    t0 = time.time()
    in_cont, lo_r, hi_r = [], [], []
    tot = skipped = 0
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        r = pair_report(b, a, n, A, C)
        if r["contained"] or r["mu"] >= MU_CUT:
            continue
        tot += 1
        _, _, MD, bd = pair_y(b, a, n, A, C)
        if bd > LOOP_CAP:
            skipped += 1
            continue
        Mj = C["M"]
        cont_hi = 2 * MD
        cnt = 0
        lo = None
        hi = 0
        y = 0
        for _ in range(bd):
            if y <= cont_hi:
                cnt += 1
            elif lo is None or y < lo:
                lo = y
            if y > hi:
                hi = y
            y += sigma_inv
            if y >= n:
                y -= n
        in_cont.append(cnt / bd)
        if lo is not None:
            lo_r.append(lo / (2 * Mj))
        hi_r.append((n - hi) / (2 * Mj - 2 * MD))
    print(f"  population {tot}, skipped {skipped}  "
          f"[{time.time() - t0:.1f} s]")
    for name, v in (("attainable y inside the CONTAINMENT arc, as a "
                     "fraction of b^Delta", in_cont),
                    ("lo = (least attainable y past containment) / "
                     "(2 M_j)", lo_r),
                    ("hi = (n - greatest attainable y) / "
                     "(2 M_j - 2 M_Delta)", hi_r)):
        if not v:
            continue
        v = sorted(v)
        under = sum(1 for x in v if x <= 1.0)
        print(f"  {name}:")
        print(f"      min {v[0]:.4f}, q1 {v[len(v) // 4]:.4f}, median "
              f"{v[len(v) // 2]:.4f}, max {v[-1]:.4f}; at or below 1: "
              f"{under} of {len(v)}")


def e_l_shape(cap, min_below=3):
    """E-L, frozen after E-K printed and before this pass was written.
    E-K found the placement is not a rate but a SHAPE: about half of
    Y_Delta lies inside the containment arc and the rest is already
    past the meeting radius. Half is a suspiciously exact number, so
    what wants naming is the set of carries that contain,

        S = {C in [0, b^Delta) : sigma^{-1} C mod n <= 2 M_Delta},

    read in the C coordinate where it is a subset of an interval rather
    than of a circle. Three shapes would explain a half: an INITIAL
    SEGMENT [0, b^Delta / 2), which would say the containment order is
    a size comparison on the carry; an ARITHMETIC PROGRESSION of step
    s, which would say sigma^{-1} s is the small quantity and the whole
    phenomenon is one number; or neither, which would leave a
    three-distance pattern with no shorter description. They are told
    apart by two cheap statistics on S: the number of maximal runs of
    consecutive C (1 for the segment, |S| for a progression of step
    >= 2) and whether S is exactly the multiples of its least positive
    member below b^Delta."""
    print(f"E-L  THE SHAPE OF THE CONTAINING CARRIES, N <= {cap}")
    t0 = time.time()
    runs_d, is_ap, tot, steps = {}, 0, 0, {}
    is_ceil = 0
    bds, sizes = {}, {}
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        r = pair_report(b, a, n, A, C)
        if r["contained"] or r["mu"] >= MU_CUT:
            continue
        _, _, MD, bd = pair_y(b, a, n, A, C)
        if bd > LOOP_CAP:
            continue
        tot += 1
        bds[min(bd, 64)] = bds.get(min(bd, 64), 0) + 1
        cont_hi = 2 * MD
        S = []
        y = 0
        for c in range(bd):
            if y <= cont_hi:
                S.append(c)
            y += sigma_inv
            if y >= n:
                y -= n
        nruns = sum(1 for i, c in enumerate(S)
                    if i == 0 or c != S[i - 1] + 1)
        runs_d[min(nruns, 5)] = runs_d.get(min(nruns, 5), 0) + 1
        s = S[1] if len(S) > 1 else 0
        steps[min(s, 5)] = steps.get(min(s, 5), 0) + 1
        if s and S == list(range(0, bd, s)):
            is_ap += 1
        # the containment-arc fraction is NOT a third fact: where S is a
        # progression |S| = ceil(b^Delta / s), so the fraction is
        # ceil(b^Delta/s)/b^Delta and its extremes are read off s and
        # b^Delta alone rather than measured independently
        if s and len(S) == -(-bd // s):
            is_ceil += 1
        sizes[min(len(S), 8)] = sizes.get(min(len(S), 8), 0) + 1
    print(f"  population {tot}  [{time.time() - t0:.1f} s]")
    print(f"  |Y_Delta| = b^Delta (64 = sixty-four or more): "
          f"{dict(sorted(bds.items()))}")
    print(f"  |S| (8 = eight or more): {dict(sorted(sizes.items()))}")
    print(f"  maximal runs of consecutive C in S (5 = five or more): "
          f"{dict(sorted(runs_d.items()))}")
    print(f"  least positive member s of S (5 = five or more): "
          f"{dict(sorted(steps.items()))}")
    print(f"  S is EXACTLY the multiples of s below b^Delta: "
          f"{is_ap} of {tot}")
    print(f"  |S| = ceil(b^Delta / s), so the containment-arc fraction "
          f"is a COROLLARY of s and not a third measurement: "
          f"{is_ceil} of {tot}")


def e_m_coincide(cap, min_below=3):
    """E-M, frozen after E-L printed and before this pass was written.
    Three residuals of the same SIZE came out of E-I, E-K and E-L -- the
    window holding attainable y at 8 pairs, the least attainable point
    past containment failing to clear the meeting radius at 8, and S
    failing to be an arithmetic progression at 8. Three counts of eight
    printed next to each other are either one population or a
    coincidence, and reading them as one without checking is exactly
    the error the numbers invite. So compute all three per pair and
    print the pairwise agreement rather than the three totals."""
    print(f"E-M  ARE THE THREE RESIDUALS ONE POPULATION? N <= {cap}")
    t0 = time.time()
    a_set, b_set, c_set = set(), set(), set()
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        r = pair_report(b, a, n, A, C)
        if r["contained"] or r["mu"] >= MU_CUT:
            continue
        _, _, MD, bd = pair_y(b, a, n, A, C)
        if bd > LOOP_CAP:
            continue
        w = window(n, MD, C["M"])
        tag = (N, key, t, A["j"], C["j"])
        if attainable_in_window(n, sigma_inv, bd, w):
            a_set.add(tag)
        S, lo, y = [], None, 0
        for c in range(bd):
            if y <= 2 * MD:
                S.append(c)
            elif lo is None or y < lo:
                lo = y
            y += sigma_inv
            if y >= n:
                y -= n
        if lo is not None and lo <= 2 * C["M"]:
            b_set.add(tag)
        st = S[1] if len(S) > 1 else 0
        if not (st and S == list(range(0, bd, st))):
            c_set.add(tag)
    print(f"  W holds attainable y: {len(a_set)}; least point past "
          f"containment does NOT clear the meeting radius: "
          f"{len(b_set)}; S is not an arithmetic progression: "
          f"{len(c_set)}  [{time.time() - t0:.1f} s]")
    print(f"  the three sets are IDENTICAL: {a_set == b_set == c_set}")
    print(f"  pairwise: |A^B| {len(a_set & b_set)}, |A^C| "
          f"{len(a_set & c_set)}, |B^C| {len(b_set & c_set)}")


def e_n_delta(cap, min_below=3):
    """E-N, frozen after E-M printed and before this pass was written.
    L2 reports b^Delta in {4, 6, 10, 36} over the below-cut population
    and calls the three-distance instrument oversized on that basis --
    but it never asked WHY the set is small, and the two available
    answers are not close. Either N <= 60,000 is simply too narrow to
    have produced a large Delta, in which case L2 is a scope statement
    that a wider census deletes; or the mu cut itself forces Delta
    down, in which case the smallness is a property of the question and
    survives any N. The tell is one comparison the file has not made:
    the Delta distribution over the WHOLE census beside the same
    distribution over the below-cut population. If the whole census
    reaches Delta the below-cut population does not, the cut is doing
    the work and not the cap. The (i, j) pairs are printed beside it,
    since which LEVELS survive the cut is the sharper form of the same
    fact."""
    print(f"E-N  IS b^Delta SMALL BECAUSE OF N, OR BECAUSE OF mu? "
          f"N <= {cap}")
    t0 = time.time()
    all_d, below_d, below_ij = {}, {}, {}
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        d = C["j"] - A["j"]
        all_d[d] = all_d.get(d, 0) + 1
        r = pair_report(b, a, n, A, C)
        if r["contained"] or r["mu"] >= MU_CUT:
            continue
        below_d[d] = below_d.get(d, 0) + 1
        ij = (A["j"], C["j"])
        below_ij[ij] = below_ij.get(ij, 0) + 1
    print(f"  Delta over the WHOLE census : "
          f"{dict(sorted(all_d.items()))}  [{time.time() - t0:.1f} s]")
    print(f"  Delta over the BELOW-CUT pop: "
          f"{dict(sorted(below_d.items()))}")
    print(f"  the (i, j) that survive the cut: "
          f"{dict(sorted(below_ij.items()))}")


def main():
    t0 = time.time()
    run(60000)
    print()
    e_k_where(60000)
    print()
    e_l_shape(60000)
    print()
    e_m_coincide(60000)
    print()
    e_n_delta(60000)
    print(f"\ntotal failures: {len(FAILURES)}  [{time.time() - t0:.1f} s]")


if __name__ == "__main__":
    main()
