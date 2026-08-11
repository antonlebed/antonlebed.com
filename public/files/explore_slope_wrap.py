"""The upper-arc criterion over the wrapped pairs: the same inequality,
proved total by the landing lemma.

THE QUESTION. explore_slope_arc.py derived the upper-arc emptiness
criterion n.h >= 2a b^Delta + h.step.y_max and verified it at 4668 of
the 10,852 non-contained pairs; 3996 have overlapping arcs and no upper
arc at all, and 2188 have a tightest coordinate whose cost wraps
(up_lim.kappa >= h.N), where the criterion's derivation -- which needs
the cost form N.tau' - y'.kappa to BE the carry -- did not reach. This
file derives the wrapped case. The answer is that no new criterion is
needed: the inequality was already total, and what was missing was the
proof.

Notation is the family's, unchanged, at phase 0: N = v b^c, u = q,
g = gcd(u, N), n = N/g, sigma = u/g a unit of Z/n, r_j the repunit,
M_j = a r_j, Delta = j - i, up_lim = 2M_j - 2M_Delta,
kappa = 2a.u - (2a-b+1)N, h = gcd(2a, b-1), s = kappa/(h g),
alpha = 2a/h, tau(y) = (-y(b-1)) mod 2a, tau' = 2a - tau. The upper
arc is y = n - y', y' in [1, up_lim], carrying
2a g c(y') = N tau' - y' kappa + 2a N m(y') with m(y') >= 0 the wrap
count of the generalized closed form.

THE DERIVATION, hand-attacked on paper before this engine existed and
checked by hand at the smallest wrapped cell,
(b, a, c, u, v) = (6, 4, 4, 4384, 9), N = 11664, levels 1 and 3.

(L) THE LANDING LEMMA. Within a class y' = y_0 + k.alpha the carry
    falls by s per step, wrapping up by n when it crosses zero; the
    value it holds just before each wrap -- the LANDING -- lies in
    [0, s). And the step is capped: kappa = (b-1)(D+1) with the span
    deficit D < g forced (the one-block law), so kappa <= (b-1)g and

        s <= (b-1)/h <= b-1 < b <= b^Delta.

    So every landing is an attainable coordinate: a class that
    completes a wrap inside the arc deposits a carry below b^Delta at
    an admissible y'. A pair that actually wraps has a NON-EMPTY upper
    arc, unconditionally -- the wrap is not an obstruction to the
    criterion, it is a witness against emptiness.

(M) WRAP-EXISTENCE IS THE TIGHTEST CLASS'S QUESTION. m(y') >= 1 iff
    y'.kappa >= N.tau'(y'). Stepping tau' up by h costs N.h and moves
    a class's largest admissible member by less than alpha, so the
    quantity y_max(class).kappa - N.tau' drops at every step: N.h =
    n g h > 2a g s = alpha.kappa, using the lower arc's own hypothesis
    n h > 2a b^Delta and s < b^Delta from (L). So a wrap exists
    anywhere on the arc iff it exists in the tau' = h class at its
    y_max:

        the pair wraps  iff  y_max . s >= n.

(N) THE CRITERION IS TOTAL. If y_max.s >= n the arc is non-empty by
    (L), and the inequality n h >= 2a b^Delta + h s y_max fails
    automatically -- it would force 2a b^Delta <= 0. If y_max.s < n
    then m = 0 across the whole arc and the parent's derivation (H)
    applies verbatim. Either way

        the upper arc is empty  iff  n h >= 2a b^Delta + h s y_max,

    the SAME inequality, now over every disjoint-arc non-contained
    pair. The m = 0 restriction was a restriction on the PROOF and
    never on the criterion, and the "wrapped case" dissolves rather
    than costing a second form. The landing also comes with an exact
    witness: with y_first the least member of the tightest class,
    c_first = (N h - y_first kappa)/(2a g) needs no wrap (y_first <=
    alpha and alpha kappa < N h), and the first landing sits at

        y' = y_first + floor(c_first / s) . alpha,  carry c_first mod s.

    Hand-checked at the specimen: y_first = 5, c_first = 11264/128 =
    88, witness y' = 5 + 17*8 = 141, carry 3 -- which is the true
    minimum of the whole arc there.

THE DESIGN, frozen before the engine.

E-A THE CRITERION, TOTAL. The inequality against the arc-split count
    at EVERY disjoint-arc non-contained pair -- the parent's 4668
    scored plus the 2188 it skipped, 6856 in all, with the skipped
    population's agreement reported separately since it is what this
    file adds. The count machinery is the parent's own floor-sum,
    imported.

E-B THE LANDING WITNESS. At every actual-wrap pair (y_max.s >= n):
    the witness coordinate is admissible (1 <= y' <= up_lim, in the
    tightest class), its true carry -- computed by the generalized
    form, independently of the landing algebra -- equals
    c_first mod s, and that value is below b^Delta. Report the count
    and the maximum landing seen against s.

E-C THE SPLIT. The 2188 split by actual wrap (y_max.s >= n) against
    none; the no-wrap part's emptiness verdicts both ways, the wrap
    part all non-empty. Report the joint. Also the cap (L) rests on:
    s <= (b-1)/h at every pair the walk sees, and the count of pairs
    where the parent's scope condition up_lim.kappa >= h.N holds but
    no admissible coordinate actually wraps -- the gap between the
    scope's conservative reading and (M)'s exact one.

KILLS, frozen as what this rig PRINTS.

K1 the criterion disagrees with the arc-split count at any
   disjoint-arc pair -> (N) is wrong.
K2 a landing witness is inadmissible, or its true carry differs from
   c_first mod s, or reaches b^Delta -> (L) is wrong.
K3 s > (b-1)/h at any pair -> the cap under (L) is wrong and the
   lemma's proof does not reach, whatever the verdicts say.
K4 an actual-wrap pair with an EMPTY upper arc -> (L) or (M) is
   wrong.

POSITIVE CONTROL, run and read before any verdict line: the parent's
populations reproduced through this file's own walk -- 3516 below the
cut, 6792 own-y-in-W, and the non-contained split 4668 scored / 3996
overlapped / 2188 wrap-scope, which must match the parent's N4 exactly.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

N1 THE CRITERION IS TOTAL. The inequality n h >= 2a b^Delta +
   h.s.y_max agrees with the arc-split count at 6856 of 6856
   disjoint-arc non-contained pairs -- the parent's 4668 and all 2188
   of the wrap-scope population it could not score, zero
   disagreements -- and its hypothesis n h > 2a b^Delta holds at all
   6856 read rather than assumed. What was "not yet derived" was
   never a missing criterion: it was a missing proof, and (L)+(M)
   supply it.

N2 THE LANDING WITNESS IS EXACT EVERYWHERE IT IS PROMISED. Every one
   of the 2188 actual-wrap pairs carries its witness: the coordinate
   admissible and in the tightest class, the true carry -- computed
   through the generalized form, with no landing algebra in the check
   -- equal to c_first mod s, and the landing below b^Delta at all
   2188, zero failures. The largest landing anywhere is 4, and the
   least b^Delta at any wrap is 4 -- different pairs, since per pair
   the landing stays under s <= b-1 < b^Delta. The cap (L) rests on
   holds at every one of the 1,786,658 pairs walked, zero breaks.

N3 THE SCOPE CONDITION IS EXACT HERE, NOT CONSERVATIVE. The parent
   skipped on up_lim.kappa >= h.N where (M)'s exact condition is
   y_max.s >= n; the gap between them -- wrap-scope pairs whose
   tightest class never actually wraps -- is EMPTY at this census: 0
   pairs. So the wrap scope IS the actual-wrap population here, and
   its verdict is uniform: 0 empty, 2188 non-empty. The two
   conditions can differ only by a coordinate inside the last alpha
   of the arc, and no census cell puts one there.

VERDICT, by piece.
  - THE LANDING LEMMA (L) is a PROPERTY: three lines from the capped
    step, checked at 2188 witnesses with 0 misses, the cap itself at
    1,786,658 pairs with 0 breaks.
  - WRAP-EXISTENCE AT THE TIGHTEST CLASS (M) is a PROPERTY, its
    stepping bound the parent's own; its hypothesis n h > 2a b^Delta
    is printed to hold at all 6856 pairs rather than assumed.
  - THE TOTAL CRITERION (N) is a RULE at this scope: exhaustive at
    6856 of 6856 disjoint-arc pairs, N <= 60,000 and phase 0. Its
    wrapped half rests on (L)+(M) and needs no census; its m = 0
    half is the parent's (H) unchanged.

RUN RECORD: pure Python, integers only, standard library;
explore_slope_empty.py's pair_y and pair_report,
explore_slope_step.py's kappa_of, and explore_slope_window.py's walk,
window and in_window imported rather than copied, with the parent's
carry_gen, count_arcs and upper_ymax re-imported from
explore_slope_arc.py, so the count adjudicated against is the one the
parent verified against the loop. 25.3 s wall, peak working set
34.7 MB against the 512 MB analysis ceiling (memwatch.py); the census
is solved_cells at N <= 60,000, phase 0, below-count >= 3, walked
ONCE. Prints reproduced by:
python prime/code/explore_slope_wrap.py
"""

import os
import sys
import time
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_slope_arc import carry_gen, count_arcs, upper_ymax  # noqa: E402
from explore_slope_empty import pair_y, pair_report  # noqa: E402
from explore_slope_step import kappa_of  # noqa: E402
from explore_slope_window import MU_CUT, in_window, walk, window  # noqa: E402

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def run(cap, min_below=3):
    print(f"THE CENSUS, N <= {cap}, below-count >= {min_below}, phase 0; "
          f"every population below is the parent rig's, re-walked")
    t0 = time.time()
    pairs = below = cross = 0
    scored = overlapped = wrapscope = 0
    # E-A
    bad_crit = 0
    first_bad = None
    ws_empty = ws_nonempty = 0
    # E-B
    wrap_pairs = bad_witness = 0
    max_landing = None
    min_bd_at_wrap = None
    # E-C
    bad_cap = 0
    gap = gap_empty = 0
    nh_fail = 0
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        pairs += 1
        b, a, c, u, v = key
        g = N // n
        kap = kappa_of(b, a, N, u)
        h = gcd(2 * a, b - 1)
        step = kap // (h * g)
        r = pair_report(b, a, n, A, C)
        y, _, MD, bd = pair_y(b, a, n, A, C)
        Mj = C["M"]
        w = window(n, MD, Mj)
        if (not r["contained"]) and r["mu"] < MU_CUT:
            below += 1
        if in_window(y, w):
            cross += 1
        # the cap (L) rests on, at every pair the walk sees
        if step * h > b - 1:
            bad_cap += 1
        if r["contained"]:
            continue
        tot, low, up, disj = count_arcs(b, a, N, g, n, kap, MD, Mj, bd,
                                        h, step)
        if not disj:
            overlapped += 1
            continue
        scored += 1
        up_lim = 2 * Mj - 2 * MD
        in_wrapscope = up_lim * kap >= h * N
        if in_wrapscope:
            wrapscope += 1
        if n * h <= 2 * a * bd:
            nh_fail += 1
        ymax = upper_ymax(b, a, h, up_lim)
        # E-A the total criterion against the parent's verified count
        crit = True if ymax is None \
            else n * h >= 2 * a * bd + h * step * ymax
        if crit != (up == 0):
            bad_crit += 1
            if first_bad is None:
                first_bad = (N, key, t, A["j"], C["j"], bd, up, crit,
                             in_wrapscope)
        if in_wrapscope:
            if up == 0:
                ws_empty += 1
            else:
                ws_nonempty += 1
        # E-B / E-C the wrap split and the landing witness
        wraps = ymax is not None and ymax * step >= n
        if in_wrapscope and not wraps:
            gap += 1
            if up == 0:
                gap_empty += 1
        if wraps:
            wrap_pairs += 1
            if min_bd_at_wrap is None or bd < min_bd_at_wrap:
                min_bd_at_wrap = bd
            alpha = 2 * a // h
            y_first = ymax - ((ymax - 1) // alpha) * alpha
            c_first = (N * h - y_first * kap) // (2 * a * g)
            y_wit = y_first + (c_first // step) * alpha
            landing = c_first % step
            true_c = (n - carry_gen(b, a, N, g, n, y_wit, kap)) % n
            good = (1 <= y_wit <= up_lim and y_wit % alpha
                    == ymax % alpha and true_c == landing
                    and landing < bd)
            if not good:
                bad_witness += 1
            if max_landing is None or landing > max_landing:
                max_landing = landing
            if up == 0:
                ok(False, "K4: an actual-wrap pair with an empty "
                          "upper arc")
    el = time.time() - t0
    print(f"POSITIVE CONTROL  pairs read {pairs}; below-cut {below} "
          f"(parent: 3516); own y in W {cross} (parent: 6792); "
          f"non-contained disjoint-arc split: scored {scored - wrapscope}"
          f" + wrap-scope {wrapscope}, overlapped {overlapped} "
          f"(parent N4: 4668 / 2188 / 3996)   [{el:.1f} s]")
    if cap == 60000 and min_below == 3:
        ok(below == 3516, "control: the below-cut population is 3516")
        ok(cross == 6792, "control: 6792 pairs whose own y is in W")
        ok(scored - wrapscope == 4668, "control: 4668 m = 0 pairs")
        ok(wrapscope == 2188, "control: 2188 wrap-scope pairs")
        ok(overlapped == 3996, "control: 3996 overlapped pairs")
    print("E-A  THE CRITERION, TOTAL")
    print(f"  disagreements with the arc-split count over ALL "
          f"{scored} disjoint-arc pairs: {bad_crit}"
          + (f"; first {first_bad}" if first_bad else ""))
    print(f"  the wrap-scope 2188's verdicts: {ws_empty} empty, "
          f"{ws_nonempty} non-empty")
    print(f"  pairs failing the derivation's hypothesis "
          f"n h > 2a b^Delta: {nh_fail} of {scored}")
    ok(bad_crit == 0, "K1 (N): the criterion is total")
    print("E-B  THE LANDING WITNESS")
    print(f"  actual-wrap pairs (y_max.s >= n): {wrap_pairs}; witness "
          f"failures: {bad_witness}; largest landing {max_landing} "
          f"against the least b^Delta at a wrap, {min_bd_at_wrap}")
    ok(bad_witness == 0, "K2 (L): the landing witness is exact")
    print("E-C  THE SPLIT AND THE CAP")
    print(f"  s > (b-1)/h: {bad_cap} of {pairs} pairs walked")
    ok(bad_cap == 0, "K3 (L): the step cap holds")
    print(f"  wrap-scope pairs with NO actual wrap -- the conservative "
          f"gap: {gap}, of which empty {gap_empty}; so the wrap-scope "
          f"empties ({ws_empty}) all sit in the gap: "
          f"{ws_empty == gap_empty}")


def main():
    run(60000)
    if FAILURES:
        print(f"\nFAILURES: {len(FAILURES)}")
        return
    print("\nall checks passed")


if __name__ == "__main__":
    main()
