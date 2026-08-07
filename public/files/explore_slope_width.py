"""Is containment width 3 inhabited? The one quantity that would leave
the closed form, hunted by solving for the slope instead of sweeping it.

THE QUESTION. explore_slope_assemble.py closes |W_t| below J by
inclusion-exclusion and its H3 replaces the level count with the WIDTH
of the containment order: a level contained in a deeper one leaves the
union, so a family of any size reduces to its maximal elements and (D)
is closed as soon as at most TWO survive. Over its census the width is
{1: 2290, 2: 56} and never 3. A width-3 class is the only object that
would reopen the case -- |B_i cap B_j cap B_k| with no level-0 factor,
three runs under three multipliers, a rank-3 lattice count with no
Euclidean descent. Nothing yet says one exists. This asks whether one
does, and if not, at what scope the answer holds.

THE DERIVATION, hand-attacked on paper before this engine existed.
Notation is explore_slope_tree.py's and explore_slope_assemble.py's:
N = L b^c, q = L u / v, g = gcd(q, N), n = N/g, I = [lo, hi] of span
span, B = Z/N \\ pi(I) the block of D = N - span residues from
B0 = hi + 1, sigma = q/g a unit of Z/n, r_j the repunit, M_j = a r_j,
J the least j with 2 M_j + 1 >= n, f(t) = b t - (b-1) phi the class
map, and lam_j the number of residues of B inside class f^j(t).

(F) lam = 1 IS FORCED, NOT MEASURED. explore_slope_twolevel.py's (A)
gives the unsaturated classes as the cyclic block
{t : (t - B0) mod g < D} of min(D, g) of them, so a cell carries both a
saturated and an unsaturated class only when D < g. A cell with D >= g
has NO saturated class, hence no deep-saturated class, hence nothing
the assembly is about. And B is D contiguous residues of Z/N, so a
residue class mod g holds at most ceil(D/g) of them: D < g gives
lam <= 1 at every class of every cell that can carry a mismatch at all.
So explore_slope_assemble.py's H6 reports as a census measurement --
"lam = 1 at every binding level of every class of this census" -- what
is a corollary of the parent's own block formula, and (E)'s criterion is
never out of its lam = 1 scope at a cell this question can be asked at.
The lam > 1 exclusion counted by its reduce_levels can never fire.

(G) THE SLOPE IS NOT A FREE AXIS -- IT IS SOLVED. span is a function of
E = floor(a (N - q) / (b - 1)) alone through
htop = min(E, wtop - phi), lbot = max(-E, wbot - phi), and it is
nondecreasing in E while E is decreasing in u. So the mismatch-capable
window N - g < span < N pins E to a window of at most g values, and each
E pins N - u to an interval of length (b-1)/a. At phase 0 the admissible
u for a given (b, a, c, v, g) are therefore at most about
(b - 1)/(2a) + 1 multiples of g -- a HANDFUL, not a range. Every census
before this one swept u to a fixed cap (600 over N <= 6000), which is
the cap explore_slope_twolevel.py's G7 and explore_slope_assemble.py's
H7 both name as the one that hid what they were looking for; solving for
u instead removes the axis rather than widening it, and what is left to
push is N. The three branches of span in E are enumerated separately and
every candidate u is verified against interval() exactly, so the
solution is a superset filter and cannot lose a cell.

(H) CONTAINMENT IS A CARRY. Write delta_t = (t - B0) mod g for the
offset of class t's bad residue inside the block. explore_slope_
assemble.py's (E) has containment B_i subset B_j (Delta = j - i) iff
|eps| <= a r_Delta with eps = sigma^{-1} (b^Delta x_i - x_j
- (b-1) phi r_Delta)/g, and x_t = B0 + delta_t. Since
(b-1) r_Delta = b^Delta - 1 this collapses to

    eps = sigma^{-1} R / g,   R = (b^Delta - 1)(B0 - phi)
                                  + b^Delta delta_i - delta_j.

Where the endpoint bound binds both ends -- span = 2E + 1, hi = E, and
(b-1) | a(N - q) so E is exact -- (b^Delta - 1) E = a r_Delta (N - q)
= -q M_Delta (mod N), so R = (b^Delta - 1) + b^Delta delta_i - delta_j
+ q M_Delta and eps = sigma^{-1} R / g - M_Delta. The criterion
|eps| <= M_Delta then reads: containment iff
y = sigma^{-1} (R/g) mod n satisfies y <= 2 M_Delta -- the shift by
M_Delta sits OUTSIDE sigma^{-1}, not inside it. With the rigidity
explore_slope_twolevel.py measured -- D = g - 1, so B0 = 1 mod g and
every class but one is unsaturated -- delta_t = t - 1 and R/g collapses
to the CARRY floor(b^Delta t_i / g) of the class map's own
multiplication. A carry of zero is containment for free. So the whole
containment order of a class is read off the carries of the orbit
t, b t, b^2 t, ... mod g against one unit sigma^{-1}, and the width is a
property of that carry sequence.

THE DESIGN, frozen before the engine.

W-A THE CONTROLS, four, all against the parent's own objects rather
    than against a claim. (1) The solved enumerator of (G), capped where
    explore_slope_assemble.py's two_level_cells caps, must reproduce its
    cell and class list EXACTLY and in BOTH directions, at min_below 2
    over N <= 3000 and at min_below 3 over N <= 6000 -- a solver that
    silently loses cells would answer this question with a census it
    never took. (2) Width by the imported reduce_levels must equal width
    measured by DIRECT set containment among the level sets, both
    directions tested, at every class of the old census -- the parent's
    own watch, since reduce_levels tests only shallower-inside-deeper
    and its count is an upper bound until the reverse is measured.
    (3) (F) tested where it has CONTENT. Asserting lam <= 1 on cells
    the enumerator already filtered to D < g is a control that cannot
    fail, since the filter grants it; the claim that can fail is about
    the cells thrown away, so an UNFILTERED sweep checks that a cell
    with deficit >= g carries no saturated class. The lam <= 1
    tripwire is kept beside it and reported as the redundant check it
    is. (4) The parent's
    headline through the imported path, |W| = 37 against |W*| = 17.
    And a fifth that belongs to the ANSWER rather than to the census:
    whatever cell the headline lands at, its per-level bad sets are
    re-checked against w_tree's own bad[j] AT THAT CELL, since a
    control run over a census the witness is not in is a control for a
    different cell.

W-B THE WIDE HUNT. With u solved rather than swept, push N as far as
    the wall-clock allows over radices to 12, digit sets to a = 8,
    lookahead c to 8, v to the N cap, phase 0. Report the funnel, the
    number of cells carrying a class of below-count >= 3, the width
    distribution over every deep-saturated class with two or more lost
    levels, the largest width attained, and -- if any -- the smallest
    width-3 witness by N with its cell, its class and its lost levels.

W-C THE REVERSE DIRECTION AT ITS OWN CELL. Every width >= 3 candidate
    of W-B is re-measured by direct set containment in both directions
    before it is reported as a width, and the reverse containment count
    over the whole wide census is printed beside it. A candidate that
    reduces further under the reverse is NOT a width-3 witness.
    THE WITNESS IN FULL, frozen after W-B printed and before this part
    was written: K2 fired, so the smallest width-3 class is exhibited
    whole -- its three maximal level sets, every pairwise intersection,
    and the TRIPLE intersection the two-level closed form has no
    formula for, as a number beside the tree walk's own |W_t|. A
    frontier stated as a count is a claim; stated as a specimen with the
    missing term exhibited it is a construction, which is what the
    question after this one needs.

W-D THE CARRY FORM, and what the criterion is worth off its old scope.
    Over the wide census, test (H) against the parent's own criterion --
    (H) claims to RESTATE it, so that is the comparison it owes -- and
    report how often its precondition (span = 2E + 1, E exact, D = g - 1)
    holds. Separately, and this is the sharper number, test the
    CRITERION against measured set containment: the parent files its
    forward half as a property and its converse as a rule at scope
    N <= 3000, and a wider census is exactly what puts a rule's scope to
    the question.
    The width-TWO population's pair is the BASELINE this needs: an
    empty pair reported only at width 3 has nothing to be surprising
    against, so it is counted at width 2 over the same census.
    THE TRIPLE TERM ITSELF, frozen after W-C printed and before this
    part was written: the smallest witness turned out to have an EMPTY
    triple intersection, which makes the two-level truncation
    unjustified there but not WRONG. Those are different findings and
    the census can tell them apart, so compute
    |B_i cap B_j cap B_k| at every width-3 class found, report the
    distribution, and name the smallest class where it is non-zero --
    the first place the parent's closed form actually returns a wrong
    number.

W-E THE PHASE AXIS, the one (G) does not solve. Brute-sweep w/z over
    z <= 6 at a small N cap with u swept rather than solved, and report
    the width distribution there. Phase 0 is where every census in this
    family has lived; a width of 3 that only exists off it is a scope
    statement the hunt would otherwise have missed.

KILLS, frozen as what this rig PRINTS.

K1 A control misses -> the solver, the width measurement or (F) is
   wrong, and nothing below is read.
K2 A class whose measured width -- both directions -- is 3 or more ->
   width 3 is INHABITED, the closed form of the parent's (D) is
   incomplete, and the rank-3 lattice count is owed.
K3 No such class anywhere in W-B or W-E -> width 3 is not inhabited at
   the scope reached, which is then stated as the scope and not as the
   object.
K4 A cell carrying a deep-saturated class with lam > 1 at a binding
   level -> (F) is wrong and the parent's lam scope caveat stands.
K5 The carry form of (H) disagrees with the measured containment at a
   class whose precondition holds -> (H) is wrong; not a kill for
   K2/K3, which never use it.

POSITIVE CONTROL, run and read before any verdict line: W-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

I1 WIDTH 3 IS INHABITED. K2 fired: 812 classes of measured containment
   width 3 over 11095 cells with N <= 60000, against a width
   distribution of {1: 314756, 2: 3824, 3: 812} over 319392 classes
   carrying two or more lost levels. Every one is measured by DIRECT
   set containment in BOTH directions rather than by the criterion, so
   none is the upper bound the parent's reduce_levels would have
   reported; the reverse containment occurs at 0 pairs of the whole
   census, as it did in the parent's. The smallest by N is N = 11664,
   (b, a, c, u, v) = (6, 4, 4, 4384, 9), g = 16, n = 729, J = 4,
   class 1, whose orbit 1 -> 6 -> 4 -> 8 loses levels 1, 2 and 3 with
   |B_1| = 9, |B_2| = 54, |B_3| = 351. So the answer to the question
   the parent left is YES, and the assembly of its (D) is NOT closed
   unconditionally.

I2 AND IT COSTS THE CLOSED FORM NOTHING, BECAUSE THE TRIPLE TERM IS
   EMPTY. |B_i cap B_j cap B_k| is 0 at 812 of 812 width-3 classes, and
   the reason is one level down: of the three PAIRWISE terms among the
   maximal levels, the number that vanish is {1: 728, 2: 72, 3: 12} --
   never zero -- and WHICH pair vanishes is sharper still: the SHALLOW
   pair, the two shallowest of the three maximal levels, is empty at
   812 of 812, while the mid pair is empty at 64 and the deep pair at
   32. The law to derive is therefore not "some pair vanishes" but
   "the two shallowest maximal levels never meet". Against a BASELINE
   that makes this a finding rather
   than a curiosity: over the same census the width-TWO population has
   its single pair empty at only 128 of 3824, so a vanishing pair is a
   3% event at width 2 and a certainty at width 3.
   A width-3 class always carries an empty pair, so the
   term with no closed form is empty before it is ever reached. At the
   smallest witness the truncation and the full inclusion-exclusion
   both give |W_t| = 327, which is the tree walk's own count. The
   parent's (D) is therefore UNJUSTIFIED at width 3 and not WRONG
   anywhere measured, and those are different statements: what is now
   open is not width 3 but a width-3 class whose three pairwise terms
   are all non-empty, which no cell of this census has.

I3 THE PARENT'S CRITERION IS NOT EXACT -- ITS CONVERSE BREAKS OFF ITS
   OWN SCOPE. |eps| <= a r_Delta agrees with measured containment at
   1775806 + 10568 pairs and errs at 284, ALL in the same direction:
   the criterion says no where containment holds, never the reverse.
   That is exactly the split the parent's own verdict predicted -- the
   forward half is a PROPERTY and holds with 0 counterexamples at a
   census 400 times wider, while the converse is a RULE and its scope
   line needs BOTH of its qualifiers, which the measured locations
   show one at a time. At phase 0 the 284 failures sit at N from 22784
   to 56576 and 284 of 284 are in classes with THREE or more lost
   levels -- a regime the parent's S-D never put the criterion to,
   having tested only classes with exactly two -- so what protected the
   old census was the level count as much as the N cap. Off phase 0 the
   failures arrive far earlier: 16 pairs at N from 1160 to 2496, none
   of them in a 3+-level class, which is INSIDE the range where the
   parent measured no disagreement at all. So "exact below N = 3000" is
   a phase-0 statement, and the two qualifiers are independent. The
   cost is 124 classes where the criterion's width EXCEEDS the measured
   width, so the parent's H3 reading of reduce_levels as exact is a
   statement about its census and not about the object. Nothing in I1
   or I2 rests on the converse: every width printed here is measured.

I4 CONTAINMENT IS A CARRY, EXACTLY. (H) agrees with the criterion at
   1782350 of 1782350 pairs where its precondition holds, 0
   disagreements, with the precondition off at 4308 of the wide census
   and at 22300 of the phase census -- the phase axis is where
   span = 2E + 1 with E exact and D = g - 1 stops being the ordinary
   case. So at phase 0 the containment order of a class is the sequence
   of carries floor(b^Delta t_i / g) of its own class orbit, read
   against the single unit sigma^{-1} mod n: a carry of 0 is
   containment for free, and otherwise containment is
   sigma^{-1} carry mod n <= 2 a r_Delta. K5 fired once during
   development and is what caught the only error in this file: the
   shift by M_Delta was written INSIDE sigma^{-1} rather than outside
   it, disagreeing at 1213370 of 1782350 pairs. The failure was
   loudest exactly where the truth is easiest -- at carry 0 the correct
   y is 0 and containment is FREE, while the misplaced shift reads
   sigma^{-1} M_Delta there and denies it -- which is why 1209590 of
   the 1213370 were denied containments. A derivation whose error
   concentrates on its own trivial case is one that was never checked
   against its trivial case.

I5 lam = 1 IS FORCED. K4 never fired: 0 binding levels with lam > 1
   across all three censuses -- but that tripwire runs on cells the
   enumerator has already filtered to D < g, which GRANTS lam <= 1, so
   it is a control that cannot fail and is reported as the redundant
   check it is. The claim with content is about the cells thrown away,
   and it is tested unfiltered: of 54178 cells read with no deficit
   condition at all, 53648 have D >= g and 0 of those carry a
   saturated class. That is (F), and it is a corollary of the parent's
   own block formula rather than a census fact -- a cell with D >= g
   has no saturated class at all, so no deep-saturated class, so
   nothing the assembly is about. explore_slope_assemble.py's
   H6 files this as a measurement and its S-E hunts a discriminator for
   it in rho; there is none to hunt. Its reduce_levels' lam > 1
   exclusion, and the roadmap's warning that a lam > 1 cell must be
   counted separately, can never fire.

I6 THE SLOPE WAS NEVER AN AXIS, WHICH IS WHY EVERY CENSUS MISSED THIS.
   (G)'s solver reproduces two_level_cells exactly -- 219 of 219 at
   N <= 3000 below-count >= 2, 68 of 68 at N <= 6000 below-count >= 3,
   both directions -- and with the u cap dropped and NOTHING else
   changed, the same N <= 6000 census carries 768 cells rather than 68.
   The mismatch-capable window pins E to at most g values and each E
   pins N - u to a length-(b-1)/a interval, so the admissible u for a
   given (b, a, c, v, g) number about (b-1)/(2a) + 1 -- a handful whose
   VALUES run up to N. Sweeping u to 600 while N ran to 6000 was
   therefore not a narrow scope but a wrong-shaped one, and the
   correction is to delete the axis rather than widen it. H7's
   "smallest by N" for the three-level case moves accordingly: N = 272,
   the same cell, is smallest here too, but 11095 cells now carry a
   three-level class where the swept census found 68.

VERDICT, by piece.
  - lam = 1 (F) is a PROPERTY: it follows from the parent's block
    formula plus D < g, itself forced by a saturated class existing.
    Checked 0 violations over three censuses, which is a check on the
    derivation and not evidence for it.
  - THE SOLVER (G) is a PROPERTY: span is nondecreasing in E, E is
    decreasing in u, and every candidate is verified against interval()
    exactly, so it cannot lose a cell. Checked 219/219 and 68/68
    against the swept census in both directions.
  - THE CARRY FORM (H) is a PROPERTY under its stated precondition:
    it is the parent's criterion rewritten, all cases, nothing asked
    about which residues are attained. Checked 1782350/1782350.
  - WIDTH 3 IS INHABITED (I1) is an OBSERVATION promoted by exhibit: a
    single witness settles an existence question, and it is measured
    rather than inferred. The 812 count is a RULE at the scope stated.
  - THE EMPTY TRIPLE (I2) is a PATTERN, 812 of 812 with no proof: what
    would make it a rule is a derivation that a width-3 family must
    carry an empty pair, and none is offered here. It is the load-
    bearing one -- the parent's (D) survives on it.
  - THE CRITERION'S CONVERSE (I3) is FALSIFIED as a general claim and
    survives as a rule at N <= 3000, phase 0, which is where the parent
    filed it.

I7 THE PHASE SLICE DOES NOT TEST THE PHASE AXIS FOR WIDTH, AND SAYING
   SO IS THE FINDING. W-E reads 1513 cells, 1403 of them off phase 0,
   and its width distribution is {1: 15780, 2: 292} with no width 3 --
   which is NOT evidence that width 3 needs phase 0, because its N cap
   of 3000 sits far below N = 11664, the smallest width-3 cell AT
   phase 0. A slice too small to contain the phenomenon at the setting
   where it is known to occur cannot report its absence at any other
   setting. What W-E does test is the criterion, and there the converse
   fails too, at 16 pairs of 24460 -- so that failure is not a phase-0
   artefact. The phase axis stays open for width because (G) solves u
   at phase 0 only; a phase census reaching N = 60000 needs the solver
   extended to phi, not the sweep run longer.

RUN RECORD: pure Python, integers only, standard library;
explore_slope_tree.py's cell, interval, params, depth_J, repunit and
w_tree, explore_slope_twolevel.py's below_counts and
preperiod_ceiling, and explore_slope_assemble.py's level_data,
reduce_levels, in_runs and two_level_cells imported rather than copied,
so every control reads the same code path the comparison does. 243.9 s
wall, peak working set 35.6 MB against the 512 MB analysis ceiling
(memwatch.py). The censuses: phase 0 with u SOLVED over radices to 12,
digit sets to a = 8, lookahead to 8, every v with N = v b^c <= 60000 at
below-count >= 3 (11095 cells) and <= 20000 at below-count >= 2 (9116),
plus a phase slice with u SWEPT to 400 over N <= 3000, v <= 40 and
z <= 6 (1513 cells, 1403 of them off phase 0). Prints reproduced by:
python prime/code/explore_slope_width.py
"""

import os
import sys
import time
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_slope_tree import (  # noqa: E402
    cell, params, interval, depth_J, repunit, w_tree,
)
from explore_slope_twolevel import (  # noqa: E402
    below_counts, preperiod_ceiling,
)
from explore_slope_assemble import (  # noqa: E402
    level_data, reduce_levels, subsumes, in_runs, two_level_cells,
)

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------- (G) solving for u

def divisors(N):
    ds, i = [], 1
    while i * i <= N:
        if N % i == 0:
            ds.append(i)
            if i != N // i:
                ds.append(N // i)
        i += 1
    return sorted(ds)


def _e_windows(N, g, wtop, wbot):
    """The E intervals (inclusive) on which N - g < span < N, one per
    branch of span(E) = min(E, wtop) - max(-E, wbot) + 1. span is
    nondecreasing in E, so each branch inverts directly."""
    out = []
    mE = -wbot                      # -wbot = a r_c L, the lower clip
    # branch 1: E <= min(wtop, mE), span = 2E + 1
    lo = (N - g - 1) // 2 + 1
    hi = (N - 2) // 2
    hi = min(hi, wtop, mE)
    if lo <= hi:
        out.append((lo, hi))
    # branch 2: wtop <= E <= mE, span = wtop + E + 1
    lo, hi = N - g - wtop, N - 2 - wtop
    lo, hi = max(lo, wtop), min(hi, mE)
    if lo <= hi:
        out.append((lo, hi))
    # branch 3: mE <= E <= wtop, span = E + mE + 1
    lo, hi = N - g - mE, N - 2 - mE
    lo, hi = max(lo, mE), min(hi, wtop)
    if lo <= hi:
        out.append((lo, hi))
    return out


def u_candidates(b, a, c, v, g, N, u_cap=None):
    """(G): the u with gcd(u, N) = g whose interval is mismatch-capable,
    at phase 0. A SUPERSET generated from the E windows; the caller
    verifies each against interval() exactly."""
    rc = repunit(b, c)
    wtop, wbot = (a * rc + 1) * v - 1, -a * rc * v
    seen = set()
    for elo, ehi in _e_windows(N, g, wtop, wbot):
        # E = floor(a (N - u) / (b - 1))  =>  N - u in
        # [ceil(elo (b-1)/a), floor(((ehi+1)(b-1) - 1)/a)]
        nu_lo = -((-elo * (b - 1)) // a)
        nu_hi = ((ehi + 1) * (b - 1) - 1) // a
        u_lo, u_hi = N - nu_hi, N - nu_lo
        u_lo = max(u_lo, 1)
        if u_cap is not None:
            u_hi = min(u_hi, u_cap)
        if u_lo > u_hi:
            continue
        start = ((u_lo + g - 1) // g) * g
        for u in range(start, u_hi + 1, g):
            if gcd(u, v) != 1 or gcd(u, N) != g:
                continue
            seen.add(u)
    return sorted(seen)


def solved_cells(n_cap, min_below, b_cap=12, a_cap=8, c_cap=8,
                 v_cap=None, u_cap=None):
    """Every phase-0 cell with N <= n_cap carrying a deep-saturated
    class of below-count >= min_below, with u SOLVED rather than swept.
    Same shape as explore_slope_assemble.two_level_cells."""
    out = []
    tau_need = min_below + 1
    for b in range(2, b_cap + 1):
        for a in range(1, a_cap + 1):
            if 2 * a + 1 < b:
                continue
            for c in range(1, c_cap + 1):
                if b ** c > n_cap:
                    break
                vtop = n_cap // b ** c
                if v_cap is not None:
                    vtop = min(vtop, v_cap)
                for v in range(1, vtop + 1):
                    N = v * b ** c
                    for g in divisors(N):
                        if preperiod_ceiling(b, g) < tau_need:
                            continue
                        n = N // g
                        if depth_J(b, a, n) < tau_need:
                            continue
                        for u in u_candidates(b, a, c, v, g, N, u_cap):
                            L, phi, N2, q, g2 = params(b, a, c, u, v, 0, 1)
                            if N2 != N or g2 != g:
                                continue
                            lo, hi, span, _ = interval(b, a, c, u, v, 0, 1)
                            if lo > hi or span > N or not (0 < N - span < g):
                                continue
                            ce = cell(b, a, c, u, v, 0, 1)
                            if ce is None:
                                continue
                            cnt, _ = below_counts(ce)
                            two = sorted(t for t, k in cnt.items()
                                         if k >= min_below)
                            if two:
                                out.append((N, (b, a, c, u, v), ce, two))
    out.sort(key=lambda r: (r[0], r[1]))
    return out


def brute_cells(n_cap, min_below, u_cap, v_cap, z_max=1):
    """The old sweep's shape, kept for the control and for the phase
    axis (G) does not solve: u swept, phases w/z with z <= z_max."""
    out = []
    for b in range(2, 13):
        for a in range(1, 9):
            if 2 * a + 1 < b:
                continue
            for z in range(1, z_max + 1):
                for w in range(0, z):
                    if gcd(w, z) != 1 and not (w == 0 and z == 1):
                        continue
                    for v in range(1, v_cap + 1):
                        for c in range(1, 9):
                            L = v * z // gcd(v, z)
                            if L * b ** c > n_cap:
                                break
                            for u in range(1, u_cap + 1):
                                if gcd(u, v) != 1:
                                    continue
                                L, phi, N, q, g = params(b, a, c, u, v, w, z)
                                if gcd(b, g) == 1:
                                    continue
                                lo, hi, span, _ = interval(b, a, c, u, v,
                                                           w, z)
                                if lo > hi or span > N:
                                    continue
                                if not (0 < N - span < g):
                                    continue
                                if depth_J(b, a, N // g) < min_below + 1:
                                    continue
                                if preperiod_ceiling(b, g) < min_below + 1:
                                    continue
                                ce = cell(b, a, c, u, v, w, z)
                                if ce is None:
                                    continue
                                cnt, _ = below_counts(ce)
                                two = sorted(t for t, k in cnt.items()
                                             if k >= min_below)
                                if two:
                                    out.append((N, (b, a, c, u, v, w, z),
                                                ce, two))
    out.sort(key=lambda r: (r[0], r[1]))
    return out


# ------------------------------------------- widths, criterion and set

def level_sets(ce, lv):
    n = ce["n"]
    return [{w for w in range(n)
             if in_runs(x["mult"] * w + x["d"], x["runs"], n)} for x in lv]


def measured_width(ce, deep):
    """The number of maximal level sets under ACTUAL inclusion, both
    directions, equal sets collapsed. This is the width the closed form
    cares about; reduce_levels' count is an upper bound on it."""
    sets = level_sets(ce, deep)
    uniq = []
    for s in sets:
        if not any(s == t for t in uniq):
            uniq.append(s)
    maximal = [s for i, s in enumerate(uniq)
               if not any(s < t for k, t in enumerate(uniq) if k != i)]
    return len(maximal), sets


def carry_form(b, a, ce, A, C):
    """(H): containment read off the class orbit's own carry. Returns
    (precondition holds, verdict)."""
    N, g, n, q = ce["N"], ce["g"], ce["n"], ce["q"]
    if (a * (N - q)) % (b - 1) != 0 or ce["hi"] != a * (N - q) // (b - 1):
        return False, None
    if N - ce["span"] != g - 1:
        return False, None
    dl = C["j"] - A["j"]
    M = a * repunit(b, dl)
    carry = (b ** dl * A["tj"]) // g
    y = (pow((q // g) % n, -1, n) * carry) % n
    return True, y <= 2 * M


# ------------------------------------------------------------- passes

def f_control(n_cap=1200, b_cap=6, a_cap=4, v_cap=12):
    """(F) against cells the deficit filter never sees. Asserting
    lam <= 1 on cells already filtered to D < g is a control that
    cannot fail -- the filter grants it. The claim with content is the
    one about the cells thrown away: D >= g leaves NO saturated class."""
    seen = ge = viol = 0
    for b in range(2, b_cap + 1):
        for a in range(1, a_cap + 1):
            if 2 * a + 1 < b:
                continue
            for c in range(1, 8):
                if b ** c > n_cap:
                    break
                for v in range(1, min(v_cap, n_cap // b ** c) + 1):
                    N = v * b ** c
                    for u in range(1, N + 1):
                        if gcd(u, v) != 1:
                            continue
                        lo, hi, span, _ = interval(b, a, c, u, v, 0, 1)
                        if lo > hi or span > N:
                            continue
                        ce = cell(b, a, c, u, v, 0, 1)
                        if ce is None:
                            continue
                        seen += 1
                        if N - span >= ce["g"]:
                            ge += 1
                            if ce["A"]:
                                viol += 1
    return seen, ge, viol


def w_a_controls():
    print("W-A  THE CONTROLS")
    t0 = time.time()
    seen, ge, viol = f_control()
    print(f"  (F) on UNFILTERED cells: {seen} read, {ge} with deficit "
          f">= g, of which carrying a saturated class: {viol}")
    ok(viol == 0, "(F): a deficit >= g cell with a saturated class")
    for cap, mb in ((3000, 2), (6000, 3)):
        brute = two_level_cells(cap, min_below=mb)
        solved = solved_cells(cap, mb, v_cap=80, u_cap=600)
        bk = {(k, tuple(two)) for _, k, _, two in brute}
        sk = {(k, tuple(two)) for _, k, _, two in solved}
        ok(bk == sk, f"solver vs sweep at cap {cap} min_below {mb}: "
                     f"{len(bk - sk)} lost, {len(sk - bk)} spurious")
        print(f"  cap {cap}, below-count >= {mb}: swept {len(bk)} "
              f"(cell, classes), solved {len(sk)}, identical: {bk == sk}")
    free = solved_cells(6000, 3)
    print(f"  what dropping the u cap alone buys at the OLD N cap: "
          f"below-count >= 3 cells over N <= 6000, u <= 600: 68; "
          f"u solved: {len(free)}")
    cells = two_level_cells(3000, min_below=2)
    agree = lam_hi = classes = 0
    for N, key, ce, two in cells:
        b, a = key[0], key[1]
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            for x in lv:
                if x["lam"] != 1:
                    lam_hi += 1
            deep = [x for x in lv if x["j"] > 0]
            keep = reduce_levels(b, a, ce["n"], deep)
            ok(keep is not None, f"lam scope {key} t={t}")
            mw, _ = measured_width(ce, deep)
            classes += 1
            if mw == len(keep):
                agree += 1
            else:
                ok(False, f"width {key} t={t}: criterion {len(keep)} "
                          f"vs measured {mw}")
    print(f"  width by criterion equals width by measured containment: "
          f"{agree} of {classes} classes")
    print(f"  binding levels with lam > 1 (K4): {lam_hi}")
    wce = cell(2, 1, 3, 40, 9, 0, 1)
    W, star, _ = w_tree(2, 1, 3, 40, 9, wce, 0, 1)
    print(f"  the witness through the imported path: |W| = {len(W)}, "
          f"|W*| = {len(star)}")
    ok(len(W) == 37 and len(star) == 17, "witness headline")
    print(f"  control failures: {len(FAILURES)}  [{time.time() - t0:.1f} s]")


def scan(cells, label, deep_measure=True):
    """Width distribution over a cell list, with every width >= 3
    candidate re-measured in both directions (W-C)."""
    widths, lam_hi, rev, hits, checked = {}, 0, 0, [], 0
    carry_conf = {(True, True): 0, (True, False): 0,
                  (False, True): 0, (False, False): 0}
    crit_conf = dict(carry_conf)
    crit_where = []
    carry_skip = wider = w2_empty = w2_full = 0
    for N, key, ce, two in cells:
        b, a = key[0], key[1]
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            for x in lv:
                if x["lam"] != 1:
                    lam_hi += 1
            deep = [x for x in lv if x["j"] > 0]
            if len(deep) < 2:
                continue
            keep = reduce_levels(b, a, ce["n"], deep)
            if keep is None:
                continue
            wd = len(keep)
            if deep_measure or wd > 2:
                mw, sets = measured_width(ce, deep)
                checked += 1
                for i in range(len(deep)):
                    for k in range(i + 1, len(deep)):
                        if sets[k] <= sets[i]:
                            rev += 1
                        crit = subsumes(b, a, ce["n"], deep[i], deep[k])
                        crit_conf[(crit, sets[i] <= sets[k])] += 1
                        if crit != (sets[i] <= sets[k]):
                            crit_where.append((N, len(deep)))
                        app, verd = carry_form(b, a, ce, deep[i], deep[k])
                        if not app:
                            carry_skip += 1
                        else:
                            carry_conf[(verd, crit)] += 1
                if mw != wd:
                    wider += 1
                wd = mw
                if mw == 2:
                    # the BASELINE for the empty-pair law: how often a
                    # pair vanishes when only two levels survive. Without
                    # it, "empty at every width-3 class" has nothing to
                    # be surprising against
                    mx = [s for s in sets if not any(s < o for o in sets)]
                    uq = []
                    for s in mx:
                        if not any(s == o for o in uq):
                            uq.append(s)
                    if len(uq) == 2:
                        if uq[0] & uq[1]:
                            w2_full += 1
                        else:
                            w2_empty += 1
            widths[wd] = widths.get(wd, 0) + 1
            if wd >= 3:
                hits.append((N, key, t, [x["j"] for x in deep], wd))
    mode = ("every class" if deep_measure
            else "width >= 3 candidates only")
    print(f"  {label}: classes with 2+ lost levels {sum(widths.values())}; "
          f"measured in both directions: {mode} ({checked})")
    # the criterion OVERSTATES width, so where a class was not measured
    # its entry here is an upper bound and the row must say so -- an
    # unlabelled distribution is the one that gets quoted later
    tag = ("measured" if deep_measure
           else "measured at width >= 3, criterion UPPER BOUND below it")
    print(f"    width distribution ({tag}): {dict(sorted(widths.items()))}")
    print(f"    binding levels with lam > 1 (K4): {lam_hi}")
    print(f"    reverse containment (deeper inside shallower): {rev} "
          f"over the {checked} classes measured")
    print(f"    the parent's criterion vs MEASURED containment: "
          f"both yes {crit_conf[(True, True)]}, both no "
          f"{crit_conf[(False, False)]}, says yes and it is no "
          f"{crit_conf[(True, False)]}, says no and it is yes "
          f"{crit_conf[(False, True)]}")
    print(f"    classes where the criterion's width exceeds the measured "
          f"one: {wider}")
    if crit_where:
        print(f"      those failures sit at N from {min(n for n, _ in crit_where)}"
              f" to {max(n for n, _ in crit_where)}, and "
              f"{sum(1 for _, d in crit_where if d >= 3)} of "
              f"{len(crit_where)} are in classes with 3+ lost levels")
    print(f"    carry form vs THE CRITERION (K5): "
          f"agree {carry_conf[(True, True)] + carry_conf[(False, False)]}, "
          f"disagree {carry_conf[(True, False)] + carry_conf[(False, True)]}"
          f"; precondition off at {carry_skip}")
    if carry_conf[(True, False)] or carry_conf[(False, True)]:
        ok(False, f"carry form (K5) in {label}")
    if crit_conf[(True, False)]:
        ok(False, f"the criterion's PROPERTY half fails in {label}")
    if w2_empty + w2_full:
        print(f"    BASELINE, the width-2 population: pair empty at "
              f"{w2_empty} of {w2_empty + w2_full}")
    if hits:
        hits.sort()
        print(f"    WIDTH >= 3 (K2): {len(hits)}; smallest by N: {hits[0]}")
    else:
        print(f"    width >= 3 (K2): none")
    return widths, hits


def w_b_wide(n_cap):
    print(f"W-B  THE WIDE HUNT, u SOLVED, N <= {n_cap}")
    t0 = time.time()
    cells = solved_cells(n_cap, 3)
    print(f"  cells carrying a class of below-count >= 3: {len(cells)}"
          f"  [{time.time() - t0:.1f} s]")
    if cells:
        N, key, ce, two = cells[0]
        print(f"    smallest: N={N} (b,a,c,u,v)={key} g={ce['g']} "
              f"n={ce['n']} J={ce['J']} classes {two}")
        N, key, ce, two = cells[-1]
        print(f"    largest:  N={N} (b,a,c,u,v)={key} g={ce['g']} "
              f"n={ce['n']} J={ce['J']} classes {two}")
    return scan(cells, "wide census")


def w_b2_all(n_cap):
    print(f"W-B2 THE SAME CENSUS AT BELOW-COUNT >= 2, N <= {n_cap}")
    t0 = time.time()
    cells = solved_cells(n_cap, 2)
    print(f"  cells: {len(cells)}  [{time.time() - t0:.1f} s]")
    return scan(cells, "two-or-more census", deep_measure=False)


def w_c_witness(hits):
    """The smallest width-3 witness in full: the three maximal level
    sets, every intersection among them, and the |W_t| the two-level
    closed form cannot produce -- the triple term it has no formula
    for, exhibited as a number."""
    print("W-C  THE SMALLEST WIDTH-3 WITNESS, IN FULL")
    if not hits:
        print("  none")
        return
    N, key, t, levels, wd = sorted(hits)[0]
    b, a, c, u, v = key
    ce = cell(b, a, c, u, v, 0, 1)
    lv, sinv = level_data(b, a, ce, t)
    deep = [x for x in lv if x["j"] > 0]
    n, g = ce["n"], ce["g"]
    sets = level_sets(ce, deep)
    # the headline rests on the level sets INDIVIDUALLY, and the
    # parent's per-level control ran over a census this cell is not in:
    # so re-run it here, against w_tree's own bad[j] at this very cell
    W0, _, bad = w_tree(b, a, c, u, v, ce, 0, 1)
    cls = [m for m in range(ce["lo"], ce["hi"] + 1) if m % g == t]
    for x in deep:
        got = {m for m in cls
               if in_runs(x["mult"] * (sinv * ((m - t) // g)) + x["d"],
                          x["runs"], n)}
        ok(got == {m for m in cls if m in bad[x["j"]]},
           f"witness level law j={x['j']}")
    print(f"  per-level control at THIS cell against the tree's own bad "
          f"sets: {len(deep)} levels over {len(cls)} states, "
          f"failures {len(FAILURES)}")
    print(f"  N={N} (b,a,c,u,v)={key} g={g} n={n} J={ce['J']} "
          f"deficit={N - ce['span']} class {t}")
    print(f"  class orbit {[t] + [x['tj'] for x in lv if x['j'] > 0]}, "
          f"lost levels {levels}, level-0 bound: "
          f"{any(x['j'] == 0 for x in lv)}")
    for x, s in zip(deep, sets):
        print(f"    level {x['j']}: M={x['M']}, |B_j| = {len(s)}")
    for i in range(len(deep)):
        for k in range(i + 1, len(deep)):
            print(f"    |B_{deep[i]['j']} cap B_{deep[k]['j']}| = "
                  f"{len(sets[i] & sets[k])}")
    triple = sets[0] & sets[1] & sets[2]
    print(f"    THE TRIPLE TERM |B_{deep[0]['j']} cap B_{deep[1]['j']} "
          f"cap B_{deep[2]['j']}| = {len(triple)}  <- no closed form")
    want = sum(1 for m in W0 if m % g == t)
    union = set()
    for s in sets:
        union |= s
    zero = [x for x in lv if x["j"] == 0]
    if zero:
        zs = level_sets(ce, zero)[0]
        union |= zs
    print(f"  tree walk's |W_t| = {want}; n - |union of levels| = "
          f"{n - len(union)}")
    ok(want == n - len(union), "witness union against the tree walk")
    incl = n - sum(len(s) for s in sets)
    for i in range(len(deep)):
        for k in range(i + 1, len(deep)):
            incl += len(sets[i] & sets[k])
    print(f"  inclusion-exclusion truncated at pairs (what the two-level "
          f"closed form computes, level 0 aside): {incl}; with the triple "
          f"term: {incl - len(triple)}")


def w_d_triples(hits):
    """The term the closed form has no formula for, as a number at every
    width-3 class found. A width of 3 makes the two-level assembly
    UNJUSTIFIED; a NON-ZERO triple there makes it WRONG, and the two are
    different findings."""
    print("W-D  THE TRIPLE TERM AT EVERY WIDTH-3 CLASS")
    dist, nonzero, worst, pair_empty, which = {}, [], None, {}, {}
    for N, key, t, levels, wd in sorted(hits):
        b, a, c, u, v = key
        ce = cell(b, a, c, u, v, 0, 1)
        lv, _ = level_data(b, a, ce, t)
        deep = [x for x in lv if x["j"] > 0]
        _, sets = measured_width(ce, deep)
        maximal = [s for i, s in enumerate(sets)
                   if not any(s < o for o in sets)]
        uniq = []
        for s in maximal:
            if not any(s == o for o in uniq):
                uniq.append(s)
        tri = uniq[0] & uniq[1] & uniq[2] if len(uniq) >= 3 else None
        if tri is None:
            continue
        # a triple is empty as soon as ONE of its pairs is: report how
        # many of the three pairwise terms vanish, since "the triple is
        # empty" and "the pair below it is empty" are different laws
        pe = sum(1 for i in range(3) for k in range(i + 1, 3)
                 if not (uniq[i] & uniq[k]))
        pair_empty[pe] = pair_empty.get(pe, 0) + 1
        # uniq is in ascending level order, so WHICH pair vanishes is a
        # sharper statement than how many -- and it is the one a
        # derivation would have to target
        for lbl, (i, k) in (("shallow", (0, 1)), ("mid", (0, 2)),
                            ("deep", (1, 2))):
            if not (uniq[i] & uniq[k]):
                which[lbl] = which.get(lbl, 0) + 1
        sz = len(tri)
        dist[sz] = dist.get(sz, 0) + 1
        if sz:
            nonzero.append((N, key, t, levels, sz,
                            sorted(len(s) for s in uniq)))
        if worst is None or sz > worst[4]:
            worst = (N, key, t, levels, sz)
    print(f"  width-3 classes read: {sum(dist.values())}")
    print(f"  triple-term size distribution: {dict(sorted(dist.items()))}")
    print(f"  of the three pairwise terms, how many are EMPTY: "
          f"{dict(sorted(pair_empty.items()))}")
    print(f"  WHICH pair vanishes (levels in ascending order): {which}")
    if nonzero:
        print(f"  NON-ZERO triple terms: {len(nonzero)}; smallest by N: "
              f"{nonzero[0]}")
        print(f"  largest triple term: {worst}")
    else:
        print("  NON-ZERO triple terms: none -- every width-3 class found "
              "has an empty triple intersection, so the two-level "
              "truncation is unjustified there but not yet wrong")
    return dist, nonzero, pair_empty


def w_e_phase(n_cap, u_cap, v_cap, z_max):
    print(f"W-E  THE PHASE AXIS, u SWEPT, N <= {n_cap}, u <= {u_cap}, "
          f"z <= {z_max}")
    t0 = time.time()
    cells = brute_cells(n_cap, 2, u_cap, v_cap, z_max)
    off = [r for r in cells if r[1][5] != 0]
    print(f"  cells: {len(cells)}, of them off phase 0: {len(off)}"
          f"  [{time.time() - t0:.1f} s]")
    return scan(cells, "phase census")


def main():
    w_a_controls()
    if FAILURES:
        print(f"\nCONTROL FAILURES: {len(FAILURES)} -- nothing below read")
        return
    print()
    _, hits = w_b_wide(60000)
    print()
    w_c_witness(hits)
    print()
    w_d_triples(hits)
    print()
    w_b2_all(20000)
    print()
    w_e_phase(3000, 400, 40, 6)
    print(f"\nfailures: {len(FAILURES)}")


if __name__ == "__main__":
    main()
