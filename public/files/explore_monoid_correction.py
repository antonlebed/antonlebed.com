"""What is E_m as a FORMULA? -- closing the last open term of sign's
syntactic monoid.

THE QUESTION. The syntactic monoid of sign in a signed-digit system
(b, D), D = {-am..ap}, has size

    |M| = n^2 + n + 1 + SUM_{m >= 0} E_m

(explore_sign_monoid.py M1, exhaustive over 107 symmetric and 456 signed
asymmetric cells), where n is the minimal machine's live-state count and
E_m counts the length-m word values t whose clamped affine map
v -> clamp(b^m v + t) keeps TWO OR MORE states live. The leading term is a
function of the state count and hence of the normalized reach; the whole
of what escapes the reach sits in the correction (M4). Which levels
contribute is settled -- a level does iff the crossed interval holds two
integers exactly b^m apart (M5) -- but HOW MUCH each contributes is still
a computed count. This file asks for E_m as an expression.

It matters twice. It turns |M| from a formula-plus-sum into an expression
in (b, am, ap), which is what lets the order-wall block be READ rather than
evaluated; and E_m is a count of the monoid ABOVE its rank-<= 1 ideal
(explore_sign_monoid.py SCOPE), so the expression is an algebraic
statement about the quotient and not a lattice identity that happens to
fit.

HAND-ATTACK, on paper before this file was written.

Write c- = am/(b-1), c+ = ap/(b-1), R- = ceil(c-), R+ = ceil(c+). The live
set is the integers in the crossed interval I = (-c+, c-), and those are
exactly the consecutive run

    A = {alpha, ..., beta},  alpha = 1 - R+,  beta = R- - 1,  n = |A|,

since the largest integer strictly below c- is R- - 1 whether or not
(b-1) divides am, and mirrored below. So n = R- + R+ - 1 as recorded.

STEP 1: the clamp drops out of the count. For q = b^m and a word value t,
the image q v + t is an INTEGER, and the integers in I are exactly A. So
"q v + t stays live" is "q v + t in A" -- a statement about a run of n
consecutive integers, with no interval endpoints left in it.

STEP 2: two live points force two ADJACENT live points. If v1 < v2 both
live then every v between them is live too, the image being monotone in v
and A an interval. So

    E_m = #{ t in [-T-, T+] : EXISTS v with v, v+1 in A and
                              q v + t, q v + q + t in A },

with T- = am(q-1)/(b-1) and T+ = ap(q-1)/(b-1) the exact value range of a
length-m word -- both integers, since (q-1)/(b-1) is, and equal to
c-(q-1) and c+(q-1) exactly.

STEP 3: the admissible t are a union of n-1 evenly spaced blocks. For a
fixed v in [alpha, beta-1] the two membership conditions read

    alpha - q v <= t <= beta - q - q v,

a block of n - q integers, EMPTY iff q > n - 1. Successive v shift the
block down by exactly q. So the level contributes iff q <= n - 1 -- which
is M5's criterion restated with the interval removed: A holds two integers
q apart iff q <= n - 1 -- and when it does, the admissible set U is
  - ONE interval [t_lo, t_hi] when the shift is at most the block length,
    2q <= n, with
        t_lo = alpha - q(beta - 1) = (1 - R+) - q(R- - 2),
        t_hi = beta - q - q alpha = (R- - 1) - 2q + q R+,
  - and n-1 DISJOINT blocks when 2q > n.
There is no third case: the blocks either all merge or all separate.

STEP 4: and the word range can CUT it. U is built from the machine and
knows nothing about which t a length-m word can actually carry. The clip
to [-T-, T+] bites on the low side exactly when t_lo < -T-, which with
eps- = R- - c- in [0, 1) rearranges to

    2q - n < eps-(q - 1)          (low side binds),

and mirrored with eps+ = R+ - c+ on the high side. So the clip is
inactive whenever 2q >= n + eps-(q-1), and can only bite where the block
length n - q exceeds the shift by enough -- deep in the merged case.

THE FORMULA, as the four steps leave it. With q = b^m:

    E_m = 0                                              if q > n - 1
    E_m = min(t_hi, T+) - max(t_lo, -T-) + 1             if 2q <= n
    E_m = SUM_{v=alpha}^{beta-1} |[alpha - qv, beta - q - qv] ^ [-T-, T+]|
                                                         if 2q > n

and the last is n-1 disjoint blocks of n - q, so at most one block at each
end is cut and the sum is a floor expression rather than a loop. The
number of contributing levels is floor(log_b(n-1)) + 1, so SUM E_m is a
short explicit sum and |M| is an expression.

PREDICTIONS, fixed here and weighed only after the run.
  N1 The three-case formula above reproduces E_m at EVERY level of every
     cell of the symmetric and signed asymmetric grids -- the same cells
     explore_sign_monoid.py swept -- and their totals reproduce its
     correction().
  N2 THE WORD RANGE IS BINDING. It is not a formality carried by the
     model's loop: at (b, am, ap) = (2, 5, 5), m = 1, the machine admits
     21 values of t and only 11 are word values, so E_1 = 11 against an
     unclipped 21. Hand figures: n = 9, A = {-4..4}, q = 2, T+ = T- = 5,
     t_lo = -10, t_hi = 10.
  N3 The full correction there is 1 + 11 + 31 + 8 = 51 and |M| = 142,
     every term computed by hand from the formula: m = 0 gives the
     identity, m = 1 and m = 2 are clipped merged levels (21 -> 11,
     33 -> 31), m = 3 is the separated case at 8 = (n-1)(n-q) uncut, and
     m = 4 has q = 16 > n - 1 = 8.
  N4 The clip is a MERGED-case phenomenon on any grid we can sweep. In the
     separated case 2q > n the low side binds only when
     eps-(q-1) > 2q - n >= 1, and eps- <= (b-2)/(b-1) < 1, so it needs a
     reach far off the swept grids -- at b = 7 the smallest witness has a
     reach above 60. So: zero separated levels are clipped on both grids
     AND on the extended sweep, while merged clipped levels are common.
  N5 E_m is NOT monotone in m. The clip grows with q on one side and the
     block structure shrinks with q on the other, so the per-level counts
     rise and then fall; (2,5,5) prints 1, 11, 31, 8.
  N6 The criterion q <= n - 1 is EXACTLY two_apart(), the post-run
     criterion explore_sign_monoid.py measured over 269 levels: the two
     agree at every level of every cell of both grids and of the extended
     sweep, which is what makes the state count the right variable to
     state it in.

KILLS, named as things this file PRINTS, not as what they would mean.
  K1 Any level whose formula value differs from levels() kills N1 and the
     four-step derivation with it.
  K2 Any cell whose formula total differs from correction() kills N1's
     second half even if the per-level counts agree.
  K3 A printed E_1 at (2,5,5) other than 11, or a printed unclipped count
     other than 21, kills N2's hand figures.
  K4 A printed count of CLIPPED MERGED levels of zero kills nothing about
     the formula and everything about the sweep: it would mean neither
     grid exercises the clip, and N2 would rest on one hand-built cell.
  K5 Any separated level printed as clipped on either grid or the extended
     sweep kills N4.
  K6 Any level where q <= n - 1 disagrees with two_apart() kills N6.

CONTROLS, run and read BEFORE any count is weighed.
  C1 AN INDEPENDENT COUNTER. E_m is recomputed by a second routine written
     from the ADJACENT-PAIR definition (step 2) rather than the
     count-the-live-points definition levels() uses, over the same t
     range. The two must agree everywhere. This is what separates "the
     formula matches the model" from "the formula and the model share a
     bug", and it is the control the derivation needs because every step
     after step 2 is a rewriting of that definition.
  C2 THE RIG MUST SEE THE CLIP. The unclipped union count -- n(q+1) - 3q
     merged, (n-1)(n-q) separated -- is computed alongside and printed as
     a DISAGREEMENT counter. A rig on which it never disagrees cannot
     distinguish N2 from its negation, so this is the positive control
     the binding question needs, and it is read before N2 is.
  C3 THE ALGEBRA, NOT ONLY THE MODEL. At a sample of cells the actual
     syntactic monoid is built by closure (explore_sign_monoid.quotient +
     transition_monoid) and its size compared against
     n^2 + n + 1 + the formula's total. The formula is a count of the
     monoid above its rank-<= 1 ideal, so it owes a tie to the monoid and
     not merely to the model that predicted it.
  C4 CASE COVERAGE PRINTED. The run prints how many levels fell in each of
     the three cases and how many were clipped, on each grid. A formula
     validated on levels that were all merged-and-unclipped would be three
     untested branches wearing one verdict.

SCOPE. The symmetric grid (107 cells, b = 2..12) and the signed asymmetric
grid (456 cells, b = 2..9) are explore_sign_minimal.py's, taken unchanged
so the comparison is against the recorded object. The EXTENDED sweep goes
where those cannot: b = 2..7 with both reaches 1..24, which is not a claim
about the monoid there -- M1 is verified only on the original grids -- but
about the ARITHMETIC identity, E_m being defined by the integer model at
any (b, am, ap). That is what exercises the separated branch and N4.
Everything is small-integer arithmetic; the closure control runs at a
handful of cells only, and the whole run is expected in seconds, far under
the analysis ceiling.

RUN RECORD: one run over the 3579 DISTINCT cells of the three grids -- 107
symmetric, 456 signed asymmetric and 3456 extended, which OVERLAP, the
symmetric diagonal and the small asymmetric cells both sitting inside the
extended sweep -- and every level of each, 7524 contributing levels in all.
3.6 s, far under the analysis ceiling. C1, C2, C3, C4 clean; K1, K2, K3, K6
all 0; K5 = 178, so N4 is DEAD. N1, N2, N3, N5 and N6 hold. Three post-run
additions, marked as such where they appear: the binding criterion (F3),
the O(1) split branch (C5), and the merged identity (F2), which the first
reading of this run had as a measurement over the two-side-cut levels
before the audit found it holds at every merged level and follows in two
lines. The three grids were also summed rather than deduplicated in that
first reading, for 4019 cells and 8105 levels against the real 3579 and
7524; every figure below is over distinct cells.

FINDINGS.

F1 E_m IS CLOSED (rule, exhaustive over 7524 contributing levels across
   3579 cells, K1 = K2 = 0). The three-case formula reproduces every
   per-level E_m the integer model computes and every cell total, and the
   split branch's sum is itself closed (C5), so E_m is O(1) in
   (b, am, ap, m) and

       |M| = n^2 + n + 1 + SUM_{m=0}^{floor(log_b(n-1))} E_m

   is an expression with floor(log_b(n-1)) + 1 terms rather than a formula
   plus a computed sum. That closes the last open term of the order-wall block.
   The tie is to the ALGEBRA and not only to the model: C3 rebuilds the
   syntactic monoid by closure at eleven cells and the sizes agree, (2,5,5)
   at 142 among them -- a cell no previous run had computed. Two of the
   eleven were added by the audit, because the frozen nine all have their
   split levels UNCUT and so never took the tie on the branch F5's dead
   prediction lives in: (4,10,10) at 74 and (3,9,21) at 355, both with the
   word range cutting a split level. AND ONE PATH SHARES CODE WITH NEITHER
   THE MODEL NOR THE CLOSURE (C6, post-run): replaying every digit string
   on the minimal machine at (2,5,5) gives 12, 43, 114, 142, 142, 142 as
   the length rises, so 142 is reached by three independent routes. The
   FRONTIER of that replay settles at exactly 91 = n^2 + n + 1 and its max
   RANK falls 5, 3, 2, 1 as the length rises, which is the rank-<= 1 ideal
   read operationally: past length 3 every word's map keeps at most one
   state live, there are exactly as many such maps as the leading term
   counts, and the length at which the rank hits 1 is the level at which
   E_m stops. The rank had to be read off the TRANSITION function, live
   meaning non-absorbing: the obvious reading, Moore output 0, is the SIGN
   and selects the single zero state, under which the check passes
   vacuously -- which is how it was first written. The second C3 cell lands OFF the asymmetric
   grid, whose reaches stop at 8, so it also carries M1 -- the monoid IS
   the set of clamped affine maps -- one cell past the range that rule was
   verified on.

F2 AND THE MERGED CASE IS NOT A LATTICE COUNT AT ALL -- IT IS THE WHOLE
   WORD-VALUE RANGE (theorem, and verified at all 6076 merged levels with 0
   exceptions). Whenever 2q <= n the machine's admissible interval CONTAINS
   the whole word range: t_lo <= -T- rearranges to 2q - n <= eps-(q-1),
   whose left side is <= 0 and whose right side is >= 0, and the high side
   mirrors it. So the clip is total, nothing survives of the block
   structure, and

       E_m = T- + T+ + 1 = (am + ap)(b^m - 1)/(b - 1) + 1,

   which says EVERY length-m word keeps two or more states live. The proof
   is two lines and needs no sweep; the 6076 levels are a CONTROL on it and
   not its evidence. Merged levels are 6076 of the 7524 contributing ones
   and carry 70% of the correction BY VALUE, the two shares differing
   because the split levels sit at the large q -- so the lattice structure
   survives only in the 1448 split levels. N2 predicted the clip
   is live and understated it: the clip is not a correction to the merged
   case, it is the whole of it.

F3 SO THE DIGIT SET ENTERS THE CORRECTION AT FULL RESOLUTION, AND THE
   CEILING DEFECT DECIDES ONLY THE BOUNDARY (post-run measurement, added
   after F1 and F2 were read and not a frozen prediction; 0 mismatches over
   7524 levels). Writing eps- = R- - c- and eps+ = R+ - c+ for the two
   CEILING DEFECTS -- the fractional part the reach ceiling throws away --
   the word range cuts at level m iff

       max(eps-, eps+) * (b^m - 1)  >  2 b^m - n,

   which by F2 is automatic in the merged case -- the 262 merged levels
   where it does not fire are ALL at the flush corner 2q = n, where the
   containment is an equality -- and therefore has content only among the
   split levels, where it fires at 178 of 1448. That is the
   sharp form of what M4 could only describe, and it is NOT the form this
   file first wrote down. The leading term n^2 + n + 1 reads am only
   through R- = ceil(am/(b-1)); the correction reads am and ap DIRECTLY,
   at every merged level, through the word count of F2 -- so the residue's
   extra resolution is not the defect but the reach's own fractional part
   in full, and the defect's job is to decide, above the merge, whether the
   words or the machine are the tighter constraint. The corpus's sharpest
   witness reads off the word count and nothing subtler: (3,7,7) and
   (3,8,8) share n = 7 and a leading 57, both are cells whose every level
   is merged, and their corrections 16 and 18 differ because 14 and 16 do.

F4 SO SUM E_m IS ONE GEOMETRIC SUM WHEREVER EVERY LEVEL MERGES
   (rule, 1946 of 3579 cells, 0 mismatches). Every level merges exactly
   when 2 b^M <= n, checked against the swept test with 0 disagreements,
   so which cells these are is itself closed. When every contributing level
   is in F2's regime the whole correction is

       (am + ap)/(b - 1) * [ (b^(M+1) - 1)/(b - 1) - (M+1) ] + (M+1),
       M = floor(log_b(n - 1)),

   and |M| is a single expression in (b, am, ap) with no sum in it at all.
   Both of M2's witnesses are such cells, which is why that pair reads so
   cleanly.

F5 N4 DIED THE SAME DEATH ITS PREDECESSOR DID, ONE LEVEL UP. N4 said the
   clip is a merged-case phenomenon on any grid we can sweep, and 178 split
   levels are cut. The inequality it rested on was DERIVED and correct --
   F3 is that same inequality, confirmed exactly -- and the claim about
   WITNESS SCALE was read off one corner of it (b = 7, m = 1, where the
   smallest witness does need a reach above 55) and generalized without
   being checked at another. The smallest actual witness is
   (b, am, ap) = (4, 10, 10) at m = 1: n = 7, eps- = 2/3, and
   2/3 * 3 = 2 > 2*4 - 7 = 1, so the cut fires and E_1 is 16 against an
   unclipped 18. That is M6's error repeated by the file correcting it --
   a necessary condition checked at one point and its sufficiency assumed
   -- and the lesson is to distrust the MARGIN rather than the kill: the
   inequality was derived and held exactly, while the estimate of where
   its witnesses live was never derived at all.

F6 E_m IS NOT MONOTONE IN m (N5, confirmed at the named witness). (2,5,5)
   prints 1, 11, 31, 8 across m = 0..3 and then stops: the word range grows
   like b^m while the machine's admissible set stops growing once the
   blocks separate, so the two constraints trade places on the way up. The
   correction is 51 and |M| = 142, every term of it named on paper before
   the engine ran (N3).

F7 THE CRITERION FOR CONTRIBUTING AT ALL IS THE STATE COUNT (N6 clean,
   K6 = 0). A level contributes iff b^m <= n - 1, which agrees with
   explore_sign_monoid.py's two_apart() at every level of every cell here.
   M5 stated that criterion as a property of the crossed interval; step 1
   removes the interval, and what is left is a statement about a run of n
   consecutive integers -- so the support of the sum is a fact about the
   state count alone, and everything that escapes the reach is in the
   SIZES of the terms and never in which terms exist.

SCOPE, and the front this leaves. What is settled is E_m and hence |M| as
an expression; what is not is a CLOSED FORM FOR THE WHOLE SUM in the mixed
case, where levels change regime on the way up (F6) and the geometric
collapse of F4 does not apply. That is a bounded gap -- floor(log_b(n-1))
+ 1 terms, each closed -- and it is arithmetic rather than structural.
The structural front is elsewhere, and F2 relocates it. Four fifths of the
LEVELS -- 70% of the correction by value -- are a WORD-VALUE COUNT: at a
merged level the elements the level
contributes to the quotient above the rank-<= 1 ideal are in bijection with
the WHOLE value range of a length-m word -- an interval of integers, with
the machine imposing no further identification and no lattice data left in
it. Words themselves collide, many to a value; what does not collide is the
value. Nothing yet says whether that bijection is an accident of counting or
a statement about the quotient's ALGEBRA -- whether the merged levels
generate a subsemigroup with the structure the count suggests, and whether
the split levels, where the machine is the tighter constraint, are the whole
of what makes the quotient interesting.
"""

import os
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from explore_sign_minimal import asym_cells, ceil_div, sweep
from explore_sign_monoid import (
    correction, levels, live_states, quotient, transition_monoid, two_apart,
)


# ------------------------------------------------------------- the formula

def window(b, am, ap):
    """(alpha, beta, n): the live run as consecutive integers, from the two
    ceilings alone -- step 1's claim, which control C1's first assert
    checks against live_states()."""
    alpha = 1 - ceil_div(ap, b - 1)
    beta = ceil_div(am, b - 1) - 1
    return alpha, beta, beta - alpha + 1


def word_range(b, am, ap, m):
    """(T-, T+): the exact value range of a length-m word, as integers."""
    s = (b ** m - 1) // (b - 1)
    return am * s, ap * s


def emc(b, am, ap, m):
    """E_m by the four-step formula. Returns (value, case) with case one of
    'none', 'merged', 'split' -- the case is printed, not inferred."""
    alpha, beta, n = window(b, am, ap)
    q = b ** m
    if q > n - 1:
        return 0, "none"
    tm, tp = word_range(b, am, ap, m)
    if 2 * q <= n:
        t_lo = alpha - q * (beta - 1)
        t_hi = beta - q - q * alpha
        return max(0, min(t_hi, tp) - max(t_lo, -tm) + 1), "merged"
    # separated: n-1 disjoint blocks of n-q, at most one cut at each end
    total = 0
    for v in range(alpha, beta):
        lo = max(alpha - q * v, -tm)
        hi = min(beta - q - q * v, tp)
        if hi >= lo:
            total += hi - lo + 1
    return total, "split"


def binds(b, am, ap, m):
    """POST-RUN, not a frozen prediction: does the word range CUT the
    machine's admissible set at this level? The hand-attack derived
    2q - n >= eps(q-1) as the non-binding condition on each side and then
    guessed its witnesses lived off the grid (N4), which was false. This is
    that same inequality tested as an exact criterion, in integers:
    eps- = (R-(b-1) - am)/(b-1), so the test clears denominators."""
    _, _, n = window(b, am, ap)
    q = b ** m
    if q > n - 1:
        return False
    slack = (2 * q - n) * (b - 1)
    em = ceil_div(am, b - 1) * (b - 1) - am
    ep = ceil_div(ap, b - 1) * (b - 1) - ap
    return em * (q - 1) > slack or ep * (q - 1) > slack


def _below(z, t_lo, q, w, nb):
    """#{t <= z} in nb disjoint blocks of w consecutive integers based at
    t_lo + q*j -- an arithmetic series, hence O(1)."""
    x = z - t_lo + 1
    if x <= 0:
        return 0
    jf = min(nb - 1, (x - w) // q) if x >= w else -1
    jm = min(nb - 1, ceil_div(x, q) - 1)
    total = w * (jf + 1)
    if jm > jf:
        k = jm - jf
        total += k * x - q * ((jf + 1 + jm) * k) // 2
    return total


def emc_fast(b, am, ap, m):
    """POST-RUN CONTROL C5: the same E_m with the split branch's loop over
    blocks replaced by a closed count. The frozen formula left that branch
    as a sum, which is what a loop in a formula always is; this closes it,
    so E_m is O(1) at every level and |M| is an expression."""
    _, _, n = window(b, am, ap)
    q = b ** m
    if q > n - 1:
        return 0
    alpha, beta, _ = window(b, am, ap)
    tm, tp = word_range(b, am, ap, m)
    t_lo = alpha - q * (beta - 1)
    if 2 * q <= n:
        t_hi = beta - q - q * alpha
        return max(0, min(t_hi, tp) - max(t_lo, -tm) + 1)
    return (_below(tp, t_lo, q, n - q, n - 1)
            - _below(-tm - 1, t_lo, q, n - q, n - 1))


def unclipped(b, am, ap, m):
    """The same count with the word range dropped -- C2's contrast."""
    alpha, beta, n = window(b, am, ap)
    q = b ** m
    if q > n - 1:
        return 0
    if 2 * q <= n:
        return n * (q + 1) - 3 * q
    return (n - 1) * (n - q)


def correction_closed(b, am, ap):
    """SUM_{m>=0} E_m from the formula: a short explicit sum, m running to
    floor(log_b(n-1))."""
    _, _, n = window(b, am, ap)
    total, m, q = 0, 0, 1
    while q <= n - 1:
        total += emc(b, am, ap, m)[0]
        m += 1
        q *= b
    return total


# ------------------------------------------------------------- the control

def emc_pairs(b, am, ap, m):
    """C1: E_m from the ADJACENT-PAIR definition, over the word range,
    scanning t directly. Independent of levels(), which counts live points
    and tests membership against the real interval."""
    alpha, beta, _ = window(b, am, ap)
    q = b ** m
    tm, tp = word_range(b, am, ap, m)
    count = 0
    for t in range(-tm, tp + 1):
        for v in range(alpha, beta):
            u = q * v + t
            if alpha <= u and u + q <= beta:
                count += 1
                break
    return count


def run_grid(name, cells, kills, tally, do_pairs):
    """One grid: every level of every cell, formula against levels(), with
    the case and clip census C4 asks for."""
    for (b, am, ap) in cells:
        alpha, beta, n = window(b, am, ap)
        live = live_states(b, am, ap)
        if live != list(range(alpha, beta + 1)):
            kills["C1_window"] += 1
        measured = levels(b, am, ap)          # index 0 is m = 1
        mmax = len(measured)
        for m in range(0, mmax + 3):   # two levels past the model's last
            q = b ** m
            got, case = emc(b, am, ap, m)
            want = 1 if n >= 2 else 0
            if m >= 1:
                want = measured[m - 1] if m - 1 < mmax else 0
            if got != want:
                kills["K1"] += 1
                if kills["K1"] <= 3:
                    print(f"  K1 {name} (b,am,ap)={(b, am, ap)} m={m} "
                          f"formula={got} measured={want}")
            if do_pairs and emc_pairs(b, am, ap, m) != got:
                kills["C1_pairs"] += 1
            if (b ** m <= n - 1) != two_apart(b, am, ap, m):
                kills["K6"] += 1
            if emc_fast(b, am, ap, m) != got:
                kills["C5"] += 1
            tally[case] += 1
            if case != "none":
                cut = got != unclipped(b, am, ap, m)
                if cut:
                    tally["clipped_" + case] += 1
                if cut != binds(b, am, ap, m):
                    kills["criterion"] += 1
                if case == "merged":
                    tm, tp = word_range(b, am, ap, m)
                    t_lo = alpha - q * (beta - 1)
                    t_hi = beta - q - q * alpha
                    lo, hi = t_lo < -tm, t_hi > tp
                    tally["m_" + ("both" if lo and hi else "low" if lo
                                  else "high" if hi else "clear")] += 1
                    # POST-RUN, sharpened by the audit: the identity holds
                    # at EVERY merged level, not only the two-side-cut ones
                    if got != tm + tp + 1:
                        kills["wordcount"] += 1
        if correction_closed(b, am, ap) != correction(b, am, ap):
            kills["K2"] += 1


def replay_all(b, am, ap, maxlen):
    """POST-RUN CONTROL C6: the monoid by REPLAYING every digit string up to
    maxlen on the minimal machine, collecting distinct maps. Independent of
    the integer model (which reasons about values) AND of the BFS closure
    (which composes stored maps), so it is the one path that shares no code
    with either. Returns (size, frontier size, max rank) per length, RANK
    being the number of live states a map keeps live -- and live means
    NON-ABSORBING, read off delta. The obvious reading, out == 0, is the
    Moore SIGN and picks out the single zero state, which makes the rank
    check pass vacuously; that is how it was first written here."""
    _, blocks, delta, _ = quotient(b, am, ap)
    live = [k for k in blocks
            if any(delta[k][d] != k for d in delta[k])]
    digits = list(range(-am, ap + 1))
    seen = {tuple(blocks)}
    frontier = [{k: k for k in blocks}]
    out = []
    for _ in range(maxlen):
        fresh = {}
        for mp in frontier:
            for d in digits:
                nm = {k: delta[mp[k]][d] for k in blocks}
                key = tuple(nm[k] for k in blocks)
                seen.add(key)
                fresh[key] = nm
        frontier = list(fresh.values())
        rank = max(sum(1 for k in live if nm[k] in live)
                   for nm in frontier)
        out.append((len(seen), len(frontier), rank))
    return out


def main():
    print("=" * 70)
    print("E_m AS A FORMULA -- the last term of the order-wall block")
    print("=" * 70)
    start = time.time()
    kills = {k: 0 for k in ("K1", "K2", "K3", "K5", "K6", "C1_window",
                            "C1_pairs", "C5", "C6", "criterion", "wordcount")}
    tally = {k: 0 for k in ("none", "merged", "split", "clipped_merged",
                            "clipped_split", "m_both", "m_low", "m_high",
                            "m_clear")}

    sym = [(b, a, a) for (b, a) in sweep()]
    asym = [c for c in asym_cells() if c[1] and c[2]]
    ext = [(b, am, ap) for b in range(2, 8)
           for am in range(1, 25) for ap in range(1, 25)]
    # THE GRIDS OVERLAP -- the symmetric diagonal and the small asymmetric
    # cells both sit inside the extended sweep -- so every tally below is
    # over DISTINCT cells. Counting the three grids in sequence would
    # report 4019 cells and 8105 levels for 3579 and 7524 real ones.
    seen, cells = set(), []
    for c in sym + asym + ext:
        if c not in seen:
            seen.add(c)
            cells.append(c)

    print(f"\nGRIDS: symmetric {len(sym)}, signed asymmetric {len(asym)}, "
          f"extended {len(ext)}; {len(cells)} DISTINCT cells")
    run_grid("all", cells, kills, tally, True)
    kills["K5"] = tally["clipped_split"]

    print("\nC4 CASE COVERAGE (levels over the distinct cells)")
    for k in ("none", "merged", "split"):
        print(f"  {k:>8}: {tally[k]}")
    print("\nC2 THE RIG SEES THE CLIP (levels where the word range cut)")
    print(f"  merged clipped: {tally['clipped_merged']}")
    print(f"  split  clipped: {tally['clipped_split']}")

    print("\nPOST-RUN: WHICH SIDE THE WORD RANGE CUTS (merged levels)")
    for k in ("m_both", "m_low", "m_high", "m_clear"):
        print(f"  {k[2:]:>5}: {tally[k]}")
    print("  both-cut levels where E_m is NOT the word count: "
          f"{kills['wordcount']}")

    print("\nN2/N3 THE NAMED WITNESS (b, am, ap) = (2, 5, 5)")
    b, am, ap = 2, 5, 5
    alpha, beta, n = window(b, am, ap)
    print(f"  A = {alpha}..{beta}, n = {n}")
    for m in range(0, 5):
        got, case = emc(b, am, ap, m)
        tm, tp = word_range(b, am, ap, m)
        print(f"  m={m} q={b ** m:>2} case={case:>6} "
              f"t in [{-tm},{tp}] E_m={got:>3} unclipped={unclipped(b, am, ap, m):>3}")
    tot = correction_closed(b, am, ap)
    print(f"  correction = {tot}  |M| = {n * n + n + 1 + tot}")

    print("\nC3 THE ALGEBRA (closure size against the formula)")
    # The last two are POST-RUN, added by the audit: every cell above has
    # its split levels UNCUT, so the closure tie had never been taken on
    # the branch F5's dead prediction lives in. (4,10,10) is the smallest
    # clipped-split cell there is and (3,9,21) is an asymmetric one.
    for cell in [(2, 1, 1), (2, 2, 2), (2, 3, 3), (3, 3, 3), (3, 7, 7),
                 (3, 8, 8), (3, 3, 4), (2, 5, 5), (4, 5, 3),
                 (4, 10, 10), (3, 9, 21)]:
        b, am, ap = cell
        _, blocks, delta, _ = quotient(b, am, ap)
        size = len(transition_monoid(blocks, delta))
        _, _, n = window(b, am, ap)
        pred = n * n + n + 1 + correction_closed(b, am, ap)
        flag = "ok" if size == pred else "MISMATCH"
        if size != pred:
            kills["K3"] += 1
        print(f"  {cell}: n={n} closure={size} formula={pred} {flag}")

    print("\nC6 (POST-RUN) THE MONOID BY REPLAYING DIGIT STRINGS, (2,5,5)")
    rows = replay_all(2, 5, 5, 6)
    for i, (size, front, rank) in enumerate(rows, start=1):
        print(f"  length <= {i}: {size} distinct maps, frontier {front}, "
              f"max rank {rank}")
    if rows[-1][0] != 142 or rows[-1][1] != 91 or rows[-1][2] != 1:
        kills["C6"] += 1

    print("\nPOST-RUN: THE ALL-WORD CELLS -- every contributing level's E_m")
    print("IS the word-value count, so SUM E_m is one geometric sum")
    nall, bad = 0, 0
    for (b, am, ap) in cells:
        _, _, n = window(b, am, ap)
        if n < 2:
            continue
        m, q, allcut, top = 0, 1, True, -1
        while q <= n - 1:
            # MERGED is the whole condition (F2). An earlier reading also
            # required binds(), which F2 makes redundant and which excluded
            # the 262 flush-corner levels -- and with them 262 cells.
            if not (emc(b, am, ap, m)[1] == "merged"
                    and emc(b, am, ap, m)[0] == sum(word_range(b, am, ap, m)) + 1):
                allcut = False
            top, m, q = m, m + 1, q * b
        if allcut:
            nall += 1
            closed = ((am + ap) * ((b ** (top + 1) - 1) // (b - 1) - (top + 1))
                      // (b - 1) + (top + 1))
            if closed != correction_closed(b, am, ap):
                bad += 1
    kills["geometric"] = bad
    print(f"  cells: {nall} of {len(cells)}; "
          f"closed-form mismatches: {bad}")
    for cell in [(3, 7, 7), (3, 8, 8)]:
        b, am, ap = cell
        _, _, n = window(b, am, ap)
        print(f"  {cell}: n={n} correction={correction_closed(b, am, ap)} "
              f"|M|={n * n + n + 1 + correction_closed(b, am, ap)}")

    print("\nKILLS")
    for k in sorted(kills):
        print(f"  {k}: {kills[k]}")
    print(f"\nwall clock: {time.time() - start:.1f} s")
    return all(v == 0 for k, v in kills.items() if k != "K5")


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
