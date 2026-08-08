"""Can one class carry TWO unsaturated levels below J? The hypothesis
the closed form rests on, hunted as pure arithmetic.

THE QUESTION. explore_slope_dodge.py closes the tree condition below
depth J level by level: at level j the survivors of a class are one run
per gap of that level's point set longer than the block lam. Assembling
W from those level descriptions is closed when a class carries at most
ONE unsaturated level below J, and open when it carries two -- the two
survivor unions then sit under different multipliers b^j and must be
intersected. Its (T) states that honestly and its census never produced
a two-level class. This asks whether one EXISTS: some class t whose
orbit under the class map is unsaturated at two levels j < J while
saturated at every level j >= J. Finding one hands over a concrete
intersection problem; finding none over a wide census is the evidence a
proof would close.

The predicate needs no game, no interval walk and no W: it reads the
class map, the saturated set A and the depth J, all of which
explore_slope_tree.py's cell() already computes per cell. So the census
can be widened far past the scope that was affordable when the tree had
to be walked.

THE DERIVATION, hand-attacked on paper before this engine existed.
Notation is explore_slope_tree.py's: N = L b^c, q = L u / v,
g = gcd(q, N), n = N/g, I = [lo, hi] of length span <= N, A the
saturated classes, f(t) = b t - (b-1) L phi (mod g) the class map,
J the least j with 2 a r_j + 1 >= n, and level j of a state of class t
sitting in class f^j(t). Levels below J are j = 1 .. J-1; level 0 is
the state itself, which lies in I by definition.

(A) THE UNSATURATED CLASSES ARE ONE CYCLIC BLOCK OF N - span OF THEM.
explore_slope_dodge.py's (P) gives lam_t = 0 iff a0 >= lamB, with
lamB = N - span, B0 = (hi + 1) mod N and a0 = (t - B0) mod g. So

    t is unsaturated  iff  (t - B0) mod g < N - span,

a cyclic block V of min(N - span, g) classes. Two consequences are
free. A cell has some saturated and some unsaturated class only when
N - g < span < N, so span sits within g of N at every cell that can
carry a mismatch at all. And V's LENGTH is fixed by the cell while its
POSITION is fixed by B0, so the question below is whether the orbit's
geometry and V's can be aimed at each other.

(B) A DEEP-SATURATED CLASS HITS V ONLY INSIDE ITS PRE-PERIOD. If f^j(t)
lies in V for some j on the CYCLE of the orbit, that class recurs at
arbitrarily large j, hence at some j >= J, and the class is not
saturated from J on. So every unsaturated level of a deep-saturated
class is strictly inside the pre-period.

(C) COPRIME RADIX AND MODULUS KILL IT OUTRIGHT. If gcd(b, g) = 1 then
t -> b t + kappa is a bijection of Z/g, every orbit is a pure cycle, the
pre-period is 0, and (B) leaves no level at all. This is why
explore_slope_tail.py's residual test opens with the same gcd.

(D) TWO HITS NEED A PRE-PERIOD OF AT LEAST 3. Two levels 1 <= j1 < j2
strictly inside the pre-period tau force tau >= 3. In the shifted
coordinate x = t - L phi -- the start class is the fixed point of f, so
f acts as x -> b x (mod g) there -- the pre-period of x is
max over p | gcd(b, g) of ceil((v_p(g) - v_p(x)) / v_p(b)), so
tau >= 3 is possible only where some prime of b divides g to more than
twice its multiplicity in b. That is a cheap O(1) filter on a cell and
it is what makes a wide census affordable.

(E) THE ABSTRACT SHAPE IS NOT OBSTRUCTED, which is why this is a census
and not a proof attempt. Over b = 2, g = 8, x = 1 the orbit of x is
2, 4, 0, 0, ... with tau = 3; taking the start class 0 and V = {2, 3, 4}
-- a legal cyclic block of three classes missing the start class --
puts levels 1 and 2 in V and every level from 3 on outside it. Nothing
in (A)-(D) forbids two hits; what may forbid them is the arithmetic
tying V's length N - span, V's position B0 and the start class L phi to
the same cell.

THE DESIGN, frozen before the engine.

R-A THE CONTROLS, three, all against explore_slope_tree.py's own
    objects rather than against a claim. (A)'s block formula against
    cell()'s A, class by class, at every cell read. The pre-period
    formula of (D) against explore_slope_tree.py's preperiod() at every
    class of a sampled cell set. And the parent's own residual test:
    this file's own reading of the predicate -- some class carrying an
    unsaturated level strictly inside its pre-period and below J -- must
    agree with is_residual() cell for cell over the parent's
    wide_scope, in BOTH directions. That control was frozen in a
    stronger form, that every parent residual cell carries a
    DEEP-SATURATED class with a level below J, and the stronger form is
    not what is_residual() says: it reads any class, deep-saturated or
    not. It is restated here to match its own object, and what the
    stronger form measures is reported as a finding rather than
    asserted as a control.
R-B THE PREDICATE. For each cell and each class t of I, walk the orbit
    over its whole transient and cycle. Call t DEEP-SATURATED when
    f^j(t) is in A for every j >= J, and let its BELOW-COUNT be
    #{1 <= j < J : f^j(t) not in A}. Report the distribution of the
    below-count over deep-saturated classes: how many carry 0, how many
    carry 1, and -- the question -- how many carry 2 or more.
R-C THE HUNT, over a census far wider than the parent's: radices to 16,
    digit sets to a = 12, slopes to 16/16, lookahead to 6, plus the
    parent's phase slice at the same widened radices. Cells whose g
    exceeds a working cap are SKIPPED and counted, never silently
    dropped, and the skipped count prints beside the read count.
R-D THE FILTER CHAIN, printed as a funnel so the census says where the
    candidates die: cells read, then those with gcd(b, g) > 1, then
    those with 0 < N - span < g, then those with J >= 3, then those
    whose modulus admits a pre-period of 3 by (D), then those carrying a
    class with below-count >= 2. A funnel that empties at a named stage
    says which hypothesis of (A)-(D) is doing the work.
R-E THE PRE-PERIOD CEILING, MEASURED. Over the cells surviving the
    third filter, the largest pre-period any class attains. (D) makes
    this the binding quantity: a census whose pre-periods never reach 3
    has not tested the question at all, whatever its cell count.
R-F THE NEAR MISSES. For cells carrying a class with below-count 1,
    report how many, and at how many distinct cells -- the population
    the two-level case would have to come from.

R-G WHICH TWO CONDITIONS COLLIDE, frozen after R-A..R-F printed and
    before this pass was written. The funnel above dies at the
    pre-period stage: over the whole census no cell that carries both a
    mismatch-capable span and J >= 3 admits a pre-period of 3. That is
    a collision between conditions, not an absence of cells, so measure
    the three populations separately over the same census -- cells with
    ceiling >= 3 alone, with ceiling >= 3 and 0 < N - span < g, and
    with ceiling >= 3 and J >= 3 -- and for each non-empty one report
    the range of the quantity the other condition reads (J, or the span
    deficit N - span against g). Naming which pair is empty is naming
    what a proof would have to derive. Also report the below-count
    distribution over the J >= 3 survivors rather than over the
    ceiling >= 3 ones, which is where R-F should have read it: with a
    ceiling of 2 the only level a deep-saturated class can lose is
    j = 1, so that distribution is the hypothesis stated as a
    measurement.

R-H HOW ROBUST IS THE COLLISION, frozen after R-G printed and before
    this pass was written. R-G finds the pair (ceiling >= 3, J >= 3)
    empty while each half is populated, so the whole open case now
    rests on one incompatibility. Both halves are O(1) per cell, so
    test it at a scope no other pass here could afford: radices to 24,
    digit sets to a = 20, slopes to 24/24, lookahead to 8, plus the
    phase slice. Report the largest J attained by a cell with
    ceiling >= 3, the largest ceiling attained by a cell with J >= 3,
    and the same two restricted to mismatch-capable cells. A pair that
    stays empty across that scope is the statement a proof must
    derive; either maximum crossing is the counterexample the whole
    file is hunting, and it prints its cell.

R-I THE CONSTRUCTION, frozen after R-H printed and before this pass
    was written -- and it is a hand derivation the censuses above
    should have made first. R-H reports the pair empty, so ask what
    the mismatch condition actually forces rather than sweeping for it.
    Take the corner b = 2, a = 1, z = 1, where E binds both ends of the
    interval: E = N - q, span = 2E + 1 and the span deficit is
    D = N - span = 2q - N - 1. Now g divides q and N, so g divides
    D + 1; and D < g by the mismatch condition, so

        D = g - 1  and  2q = N + g,

    exactly one class saturated. Writing N = g n and q = g s with
    gcd(s, n) = 1 that last identity is 2s = n + 1, so n is ODD at
    every mismatch-capable cell of this corner -- a rigidity neither
    census had any way to see. Nothing in it bounds n, so J >= 3 (which
    needs n >= 8, hence n >= 9) is free, and 8 | g gives a pre-period
    of 3 independently. n = 9, s = 5, g = 8 is the smallest solution:
    N = 72, q = 40, L = 9, c = 3, so (b, a, c, u, v) = (2, 1, 3, 40, 9),
    whose u lies past every census above -- the cap that hid the case
    was the SLOPE NUMERATOR and never the radix or the digit set.
    With exactly one saturated class t*, and t* forced to be the unique
    fixed point of f, a class is deep-saturated exactly when its orbit
    REACHES t*, and its below-count is then min(tau, J) - 1. So the
    two-level case is precisely tau >= 3 and J >= 3 together.
    Run this pass on the constructed cell and on a sweep of the family
    it comes from -- n odd and at least 9, g a multiple of 8 -- and
    report, for each, the span deficit against g - 1, the below-count
    distribution, and for every class with below-count >= 2 the orbit,
    its unsaturated levels, and the two multipliers b^j whose survivor
    unions the closed form would have to intersect.

R-J THE SPECIMEN AGAINST THE PARENT'S TREE WALK, frozen after R-I
    printed and before this pass was written. R-I finds two-level
    classes by reading the class map alone, which is the same reading
    every pass above uses -- so a shared error in it would produce
    exactly this. The specimen therefore goes through
    explore_slope_tree.py's w_tree(), which walks the tree over the
    interval and knows nothing of this file: its okdeep must agree with
    this file's deep-saturated set class for class, its per-level bad
    sets must be non-empty at BOTH of the levels claimed unsaturated,
    and W must differ from W*. Anything less and the specimen is this
    file talking to itself.

R-K THE RIGIDITY'S REAL SCOPE, frozen after R-J printed and before this
    pass was written, because R-I stated it at the corner it was found
    in and confirmed it on cells CONSTRUCTED to satisfy it -- evidence
    that cannot fail. Two repairs, and the second is the interesting
    one. Measure the deficit on cells nobody selected: every
    mismatch-capable cell of an unrestricted sweep, counting how many
    have D = g - 1. And read the derivation again for what it actually
    used. E = floor(a (N - q) / (b - 1)), so where the floor is exact
    2E = rho (N - q) with rho = 2a/(b-1), and

        D + 1 = N - 2E = N (1 - rho) + rho q,

    which g divides for any INTEGER rho, g dividing both N and q -- the
    radix and the digit set never entering except through that one
    ratio. So the prediction is that the deficit is forced exactly where
    rho is an integer and not otherwise. Report, per (b, a) of a sweep
    to radix 12, the count of mismatch-capable cells and how many carry
    D = g - 1, and whether integer rho and totality coincide row for
    row. A row of either kind breaking that is the kill.

R-L IS THE WITNESS THE SMALLEST, frozen after R-K printed and before
    this pass was written. G2 called its witness the smallest and no
    pass here had searched for a smaller one: the construction reached
    it by building a family, not by ordering cells. So order them. Sweep
    every cell with N <= 6000 over radices to 12, digit sets to a = 8,
    lookahead to 8, slopes u to 600 over v to 80 at phase 0 -- N = v b^c
    does not depend on u, so the bound is checked once per (v, c) and
    the sweep is cheap -- keep every cell carrying a class with
    below-count >= 2, and report them sorted by N. The claim stands only
    at the scope this prints, and the count of witnesses says whether
    the case is rare or ordinary.

R-M DOES THE DEEPEST LOST LEVEL SUBSUME THE SHALLOWER ONES, frozen
    after R-L printed and before this pass was written. At the witness
    the level-2 survivors turned out to be a SUBSET of the level-1
    survivors, so the intersection (T) calls an obstruction was there
    the deeper level's description alone. If that held generally the
    obstruction would dissolve outright, the assembly being closed by
    the deepest lost level and the shallower ones costing nothing. The
    point set grows with j, so within ONE coordinate the survivor set
    does shrink with j -- but the levels sit in different coordinates,
    multiplier b^j, so nothing about containment follows. Test it: over
    every two-level cell with N <= 3000, for every class losing two or
    more levels, compare the survivors of the DEEPEST lost level alone
    against the intersection over all its lost levels, both read off
    explore_slope_tree.py's own bad sets. Report the agreement count,
    the disagreement count, and the parameters of the first
    disagreements. Agreement everywhere kills (T); a disagreement is
    what the next closed form has to handle, and its cell is the one to
    work at.

KILLS, frozen as what this rig PRINTS.

L1 A control misses -> the block formula, the pre-period formula or the
   agreement with the parent's residual test is wrong, and nothing
   below is read.
L2 A class with below-count >= 2 -> the hypothesis is FALSE and the
   closed form's (T) is a real boundary; the cell prints in full
   (b, a, c, u, v, phase, g, n, J, the class, its orbit and its
   unsaturated levels) so the intersection problem can be set up.
L3 No class with below-count >= 2 while R-E reports a pre-period
   ceiling of at least 3 and R-F a non-empty one-level population ->
   the census tested the question and the hypothesis survives it.
L4 No class with below-count >= 2 while R-E reports a ceiling below 3
   -> the census did NOT test the question, whatever its size, and the
   scope has to move rather than the verdict.

POSITIVE CONTROL, run and read before any verdict line: R-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

G1 THE CONTROLS HOLD. (A)'s block formula reproduces cell()'s saturated
   set class for class at 7636 cells; the pre-period formula of (D)
   equals the measured worst pre-period at 78 sampled cells; and this
   file's reading of the residual predicate agrees with
   explore_slope_tree.py's is_residual() cell for cell, both
   directions, over the parent's whole wide_scope.

G2 THE ANSWER IS YES, AND THE HYPOTHESIS IS FALSE. A class carrying TWO
   unsaturated levels below J exists, and the case is ordinary rather
   than exotic: 262 witnesses sit below N = 6000 alone. The smallest is
   radix 2, digits {-1, 0, 1}, slope 40/9, lookahead 3, phase 0 --
   smallest by N over every cell with N <= 6000 at radices to 12, digit
   sets to a = 8, lookahead to 8 and slopes u to 600 over v to 80, at
   phase 0 (R-L), which is where that word's scope ends: N = 72, q = 40, g = 8, n = 9, J = 3, span = 65. Its
   saturated set is the single class {0}, and classes 1, 3, 5 and 7 are
   each deep-saturated with below-count 2 -- class 1's orbit runs
   2, 4, 0, so levels 1 and 2 are both unsaturated and every level from
   3 on sits at the fixed point. The two survivor unions the closed
   form would have to intersect there sit under multipliers 2 and 4.
   explore_slope_tree.py's own tree walk, which knows nothing of this
   file, agrees on the deep-saturated set exactly, rules out 12 states
   at level 1 and 24 at level 2, and prints |W| = 37 against
   |W*| = 17 -- so this is a real mismatch cell and not a bookkeeping
   artifact.

G3 THE CENSUS ROUTE MISSED IT, AND THE CAP THAT HID IT WAS THE SLOPE
   NUMERATOR. The broad census read 19227 cells and the phase census
   6095, none skipped, and the funnel dies the same way in both: 2170
   and 1870 cells with gcd(b, g) > 1, 661 and 515 with a
   mismatch-capable span, 133 and 149 with J >= 3, and ZERO admitting a
   pre-period of 3. The below-count over deep-saturated classes at those
   cells is {0: 1093, 1: 132} and {0: 838, 1: 280} -- never 2, exactly
   as a ceiling of 2 forces. The wide pass read 110571 cells (115879
   past its N cap, which prints) and found the pair (ceiling >= 3,
   J >= 3) empty in both directions, each maximum sitting at exactly 2.
   All of that is one artifact: the witness needs u = 40 at v = 9, and
   every census here caps u below it -- at 16 in the broad pass, 24 in
   the wide one, and 8 in both phase slices, whose slope list is the
   parent's. A funnel dying at a named
   stage says where the SCOPE ends and not what the object does.

G4 WHAT FOUND IT WAS A RIGIDITY THE CENSUSES COULD NOT SEE, AND ITS
   DIAL IS ONE RATIO. The endpoint bound gives E = floor(a (N - q) /
   (b - 1)); where that floor is exact, 2E = rho (N - q) with
   rho = 2a/(b - 1), so the span deficit satisfies
   D + 1 = N (1 - rho) + rho q, which g divides whenever rho is an
   INTEGER, g dividing N and q both. The mismatch condition D < g then
   forces

       D = g - 1,  that is, EXACTLY ONE CLASS IS SATURATED,

   and the radix and the digit set never enter except through rho. That
   is the whole law, and it is a RULE at the scope measured: over an
   unselected sweep to radix 12 the 29 (b, a) rows with integer rho
   carry D = g - 1 at 931 of 931 mismatch-capable cells, the 34
   fractional rows at 368 of 886, and NO row of either kind disagrees
   with its prediction. (R-I confirmed the same identity on 9120 cells
   of a family CONSTRUCTED to satisfy it, which is evidence that cannot
   fail; the unselected sweep is what carries this.)
   Writing N = g n, q = g s at rho = 2 the identity is 2s = n + 1, so n
   is ODD there. Nothing in it bounds n, so J >= 3 and a pre-period of 3
   are independent and both free. With one saturated class, which is
   forced to be f's fixed point, a class is deep-saturated exactly when
   its orbit REACHES that point and its below-count is min(tau, J) - 1
   -- so the two-level case is precisely tau >= 3 with J >= 3, and the
   constructed family's below-count distribution runs
   {0: 18240, 1: 18240, 2: 36480, 3: 46368, 4: 52416, 5: 50048,
   6: 29952}. Below-counts of six are ordinary there.

G5 SO (T) IS A REAL BOUNDARY AND NOT A CENSUS SHORTFALL, and it is now
   a concrete problem rather than an unmet case: intersect the survivor
   unions of two levels under multipliers b^j1 and b^j2 over one class.
   The specimen hands over the smallest instance of it. What is
   UNTOUCHED is the delay: the start class is f's fixed point, so
   c_min still reads one class and no orbit, at every cell here
   included -- at the witness the start class is 0, the one saturated
   class, and the game is feasible.

G6 A NEGATIVE WORTH KEEPING. 24 of the parent's 55 residual cells carry
   a deep-saturated class with an unsaturated level below J. The
   residual predicate reads ANY class; the closed form's assembly reads
   only the deep-saturated ones, so the residual census was never a
   census of the cells the assembly has to handle, and the two counts
   should not be quoted for each other.

G7 THE INTERSECTION IS NOT TRIVIAL, BUT IT NEARLY IS. At the witness
   the level-2 survivors are a SUBSET of the level-1 survivors, so the
   assembly there is the deeper level's description alone and (T)'s
   obstruction never bites. That is not general: over 219 two-level
   cells with N <= 3000 and 2346 class tests, the deepest lost level
   alone gives the full intersection at 2290 and is strictly larger at
   56. So the shallower levels do cut, rarely. At the first
   disagreement, (b, a, c, u, v) = (4, 2, 3, 448, 25), the deepest
   level leaves 4 survivors in a class and the intersection 3.
   [CORRECTED by explore_slope_assemble.py: this finding read the
   example list above, which R-M caps at three, as the population, and
   said every disagreement sits at that one cell. They sit at FOUR --
   (4,2,3,448,25) and (4,2,3,512,29) with 24 classes each,
   (6,4,3,248,3) and (6,4,4,496,1) with 4 each. All four do carry
   fractional rho, but rho is not the dial here: lam = 1 at every
   binding level of the whole census, that cell's deficit is g - 1
   despite rho = 4/3, and what decides the 56 is an O(1) inequality on
   the offset between the two levels' pulled-back centres. Nor do the
   shallower levels cost anything once they do cut: the assembly is
   closed at all 2346 class tests.]

RUN RECORD: pure Python, integers only, standard library. Roughly 145k
cells read across the census passes, plus an unselected sweep for the
deficit law, an N-ordered sweep for the minimality claim, and the
parent's wide_scope for the controls; 11.0s wall clock against a ~30s
estimate, peak working set 87.2 MB against the 512 MB analysis ceiling
(memwatch.py). The
115879 cells past the wide pass's N cap print rather than being
dropped silently. Prints reproduced by:
python prime/code/explore_slope_twolevel.py
"""

import os
import sys
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_slope_tree import (  # noqa: E402
    cell, interval, params, depth_J, preperiod, is_residual, wide_scope,
    orbit, w_tree,
)

FAILURES = []
RESIDUAL = [0, 0]

G_CAP = 20000          # working cap on the class modulus
N_CAP = 2 * 10 ** 9    # working cap on the state modulus


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ----------------------------------------------------------- the cheap
# facts, all O(1) or O(g) and none of them touching the game


def unsat_block(ce):
    """(A): the cyclic block of unsaturated classes, as (B0 mod g,
    length). Length is capped at g, where no class is saturated."""
    N, g, span, hi = ce["N"], ce["g"], ce["span"], ce["hi"]
    b0 = (hi + 1) % N
    return b0 % g, min(N - span, g)


def in_block(t, start, length, g):
    return ((t - start) % g) < length


def preperiod_ceiling(b, g):
    """(D): the largest pre-period any class can attain under
    x -> b x (mod g), read off the shared primes."""
    tau, d, p = 0, gcd(b, g), 2
    while d > 1:
        if p * p > d:
            p = d
        if d % p == 0:
            vg = vb = 0
            m = g
            while m % p == 0:
                m //= p
                vg += 1
            m = b
            while m % p == 0:
                m //= p
                vb += 1
            tau = max(tau, -(-vg // vb))
            while d % p == 0:
                d //= p
        p += 1
    return tau


def orbit_levels(f, t, g):
    """The orbit t_1, t_2, ... to the end of the transient plus one
    full cycle, and the pre-period."""
    seen, cur, j, seq = {t: 0}, t, 0, []
    while True:
        cur = f(cur)
        j += 1
        seq.append(cur)
        if cur in seen:
            return seq, seen[cur]
        seen[cur] = j


def classes_of(ce):
    """The classes I actually meets."""
    lo, hi, g = ce["lo"], ce["hi"], ce["g"]
    hi_scan = min(hi, lo + g - 1)
    return {m % g for m in range(lo, hi_scan + 1)}


def residual_here(b, ce):
    """This file's own reading of the parent's residual predicate: some
    class of I unsaturated at a level strictly inside its pre-period
    and below J."""
    f, A, g, J = ce["f"], ce["A"], ce["g"], ce["J"]
    if gcd(b, g) == 1 or J == 1:
        return False
    for t in classes_of(ce):
        seq, tau = orbit_levels(f, t, g)
        for j, x in enumerate(seq, start=1):
            if j >= J or j >= tau:
                break
            if x not in A:
                return True
    return False


def below_counts(ce):
    """R-B: for every class of I, its below-count if it is
    deep-saturated. Returns {t: count} over deep-saturated classes
    only, plus the largest pre-period attained."""
    f, A, g, J = ce["f"], ce["A"], ce["g"], ce["J"]
    out, tau_max = {}, 0
    for t in classes_of(ce):
        seq, tau = orbit_levels(f, t, g)
        tau_max = max(tau_max, tau)
        deep = True
        below = 0
        for j, x in enumerate(seq, start=1):
            if x in A:
                continue
            # (B): an unsaturated class ON THE CYCLE recurs at
            # arbitrarily large j, hence at some j >= J, whatever the
            # index it is first seen at -- so the walked window is
            # never what decides deep-saturation.
            if j >= J or j >= tau:
                deep = False
                break
            below += 1
        if deep:
            out[t] = below
    return out, tau_max


# ------------------------------------------------------------ the runs


def r_a_controls():
    print("R-A CONTROLS")
    n_block = n_tau = n_cells = 0
    for (b, a, u, v, w, z, c) in wide_scope():
        L, phi, N, q, g = params(b, a, c, u, v, w, z)
        if g > 4000 or N > N_CAP:
            continue
        ce = cell(b, a, c, u, v, w, z)
        if ce is None:
            continue
        n_cells += 1
        start, length = unsat_block(ce)
        for t in range(ce["g"]):
            want = t in ce["A"]
            got = not in_block(t, start, length, ce["g"])
            if want != got:
                ok(False, f"block formula at {(b,a,c,u,v,w,z)} class {t}")
                return
        n_block += 1
        mine = residual_here(b, ce)
        theirs = is_residual(b, a, ce)
        if mine != theirs:
            ok(False, f"residual predicate at {(b,a,c,u,v,w,z)}: "
                      f"{mine} vs {theirs}")
            return
        if theirs:
            RESIDUAL[0] += 1
            counts, _ = below_counts(ce)
            if any(k >= 1 for k in counts.values()):
                RESIDUAL[1] += 1
        if n_cells % 97 == 0:
            ceiling = preperiod_ceiling(b, ce["g"])
            worst = max(preperiod(ce["f"], t, ce["g"])
                        for t in range(ce["g"]))
            if worst != ceiling:
                ok(False, f"pre-period ceiling at {(b,a,c,u,v,w,z)}: "
                          f"{worst} vs {ceiling}")
                return
            n_tau += 1
    print(f"  block formula = cell()'s A at {n_block} cells")
    print(f"  pre-period ceiling = measured worst at {n_tau} sampled cells")
    n_res, n_agree = RESIDUAL[0], RESIDUAL[1]
    print(f"  parent residual cells: {n_res}, of which this file finds a "
          f"deep-saturated class with a level below J: {n_agree}")
    print("  (the residual predicate itself agreed cell for cell; the "
          "line above is a finding, not the control)")
    print()
    return n_res


def hunt(scope, label):
    """R-C/R-D/R-E/R-F: the funnel, the ceiling and the hits."""
    read = skipped = f_gcd = f_span = f_depth = f_tau = 0
    hits = []
    one_cells = one_classes = 0
    tau_ceiling = 0
    for (b, a, u, v, w, z, c) in scope:
        L, phi, N, q, g = params(b, a, c, u, v, w, z)
        if N > N_CAP or g > G_CAP:
            skipped += 1
            continue
        lo, hi, span, _ = interval(b, a, c, u, v, w, z)
        if lo > hi or span > N:
            continue
        read += 1
        if gcd(b, g) == 1:
            continue
        f_gcd += 1
        if not (0 < N - span < g):
            continue
        f_span += 1
        n = N // g
        if depth_J(b, a, n) < 3:
            continue
        f_depth += 1
        ceiling = preperiod_ceiling(b, g)
        tau_ceiling = max(tau_ceiling, ceiling)
        if ceiling >= 3:
            f_tau += 1
        # R-F reads the below-count at every J >= 3 survivor, not only
        # where the ceiling admits a second level: the one-level
        # population is the census the two-level case would come from.
        ce = cell(b, a, c, u, v, w, z)
        counts, _ = below_counts(ce)
        ones = [t for t, k in counts.items() if k == 1]
        twos = [t for t, k in counts.items() if k >= 2]
        if ones:
            one_cells += 1
            one_classes += len(ones)
        for t in twos:
            seq, tau = orbit_levels(ce["f"], t, ce["g"])
            hits.append({
                "cell": (b, a, c, u, v, w, z), "g": ce["g"], "n": n,
                "J": ce["J"], "t": t, "tau": tau,
                "levels": [j for j, x in enumerate(seq, start=1)
                           if x not in ce["A"] and j < ce["J"]],
                "orbit": seq[:ce["J"]],
            })
    print(f"{label}")
    print(f"  cells read {read}, skipped over the caps {skipped}")
    print(f"  gcd(b, g) > 1:          {f_gcd}")
    print(f"  0 < N - span < g:       {f_span}")
    print(f"  J >= 3:                 {f_depth}")
    print(f"  pre-period ceiling >=3: {f_tau}")
    print(f"  classes with below-count >= 2: {len(hits)}")
    print(f"  pre-period ceiling over the J>=3 survivors: {tau_ceiling}")
    print(f"  one-level population: {one_classes} classes "
          f"at {one_cells} cells")
    for h in hits[:20]:
        print(f"    HIT {h}")
    return hits, tau_ceiling, one_classes


def broad_scope():
    """R-C: radices to 16, digit sets to 12, slopes to 16/16,
    lookahead to 6, no phase."""
    pairs = [(b, a) for b in range(2, 17) for a in range(1, 13)
             if 2 * a + 1 >= b]
    for (b, a) in pairs:
        for u in range(1, 17):
            for v in range(1, 17):
                if gcd(u, v) != 1:
                    continue
                for c in range(7):
                    yield (b, a, u, v, 0, 1, c)


PHASE_SLOPES2 = [(1, 3), (3, 5), (5, 3), (2, 5), (8, 3), (7, 4), (1, 6)]
PHASES2 = [(1, 2), (2, 3), (3, 5), (1, 7), (1, 8), (3, 8), (5, 12)]


def phase_scope():
    """R-C: the parent's phase slice at the widened radices."""
    pairs = [(b, a) for b in range(2, 17) for a in range(1, 13)
             if 2 * a + 1 >= b]
    for (b, a) in pairs:
        for (u, v) in PHASE_SLOPES2:
            for (w, z) in PHASES2:
                for c in range(7):
                    yield (b, a, u, v, w, z, c)


def collide(scope, label):
    """R-G: the three populations, and the below-count distribution
    read at the J >= 3 survivors."""
    only = span_pair = depth_pair = 0
    js, defs = [], []
    dist = {}
    for (b, a, u, v, w, z, c) in scope:
        L, phi, N, q, g = params(b, a, c, u, v, w, z)
        if N > N_CAP or g > G_CAP:
            continue
        lo, hi, span, _ = interval(b, a, c, u, v, w, z)
        if lo > hi or span > N:
            continue
        n = N // g
        mism = 0 < N - span < g
        deep = depth_J(b, a, n) >= 3
        if mism and deep:
            counts, _ = below_counts(cell(b, a, c, u, v, w, z))
            for k in counts.values():
                dist[k] = dist.get(k, 0) + 1
        if preperiod_ceiling(b, g) < 3:
            continue
        only += 1
        if mism:
            span_pair += 1
            js.append(depth_J(b, a, n))
        if deep:
            depth_pair += 1
            defs.append((N - span, g))
    print(f"{label}")
    print(f"  ceiling >= 3 alone:                 {only}")
    print(f"  ceiling >= 3 and 0 < N-span < g:    {span_pair}"
          + (f"  J range {min(js)}..{max(js)}" if js else ""))
    print(f"  ceiling >= 3 and J >= 3:            {depth_pair}"
          + (f"  (N-span, g) sample {defs[:4]}" if defs else ""))
    print(f"  below-count distribution over deep-saturated classes at "
          f"the mismatch-capable J >= 3 cells: {dict(sorted(dist.items()))}")
    return only, span_pair, depth_pair, dist


def huge_scope():
    """R-H: both halves of the collision are O(1) per cell, so the
    scope goes where no walk could."""
    pairs = [(b, a) for b in range(2, 25) for a in range(1, 21)
             if 2 * a + 1 >= b]
    for (b, a) in pairs:
        for u in range(1, 25):
            for v in range(1, 25):
                if gcd(u, v) != 1:
                    continue
                for c in range(9):
                    yield (b, a, u, v, 0, 1, c)
    for (b, a) in pairs:
        for (u, v) in PHASE_SLOPES2:
            for (w, z) in PHASES2:
                for c in range(9):
                    yield (b, a, u, v, w, z, c)


def robust():
    """R-H: the two maxima, plain and restricted to mismatch-capable
    cells, plus the cell attaining each."""
    best = {"J_at_tau3": (0, None), "tau_at_J3": (0, None),
            "J_at_tau3_m": (0, None), "tau_at_J3_m": (0, None)}
    read = skipped = 0
    for (b, a, u, v, w, z, c) in huge_scope():
        L, phi, N, q, g = params(b, a, c, u, v, w, z)
        if N > N_CAP:
            skipped += 1
            continue
        lo, hi, span, _ = interval(b, a, c, u, v, w, z)
        if lo > hi or span > N:
            continue
        read += 1
        ceiling = preperiod_ceiling(b, g)
        if ceiling < 3 and depth_J(b, a, N // g) < 3:
            continue
        n = N // g
        J = depth_J(b, a, n)
        mism = 0 < N - span < g
        key = (b, a, c, u, v, w, z, g, n, J, ceiling)
        if ceiling >= 3 and J > best["J_at_tau3"][0]:
            best["J_at_tau3"] = (J, key)
        if J >= 3 and ceiling > best["tau_at_J3"][0]:
            best["tau_at_J3"] = (ceiling, key)
        if mism and ceiling >= 3 and J > best["J_at_tau3_m"][0]:
            best["J_at_tau3_m"] = (J, key)
        if mism and J >= 3 and ceiling > best["tau_at_J3_m"][0]:
            best["tau_at_J3_m"] = (ceiling, key)
    print("R-H  THE COLLISION AT THE WIDE SCOPE")
    print(f"  cells read {read}, skipped over the N cap {skipped}")
    for k, (val, key) in best.items():
        print(f"  {k}: {val}   at {key}")
    return best


def construction():
    """R-I: the family the rigidity 2q = N + g names, and the
    constructed cell at its foot."""
    print("R-I  THE CONSTRUCTION")
    cells = []
    for c in range(2, 9):
        for gg in range(8, 260, 8):
            for n in range(9, 200, 2):
                N = gg * n
                s = (n + 1) // 2
                q = gg * s
                if gcd(s, n) != 1 or gcd(q, N) != gg:
                    continue
                if N % 2 ** c:
                    continue
                # z = 1 makes L = v, and then q = L u / v = u, so the
                # cell is read straight off (N, q): v = L = N / b^c and
                # u = q, with no divisibility owed.
                L = N // 2 ** c
                if L < 1:
                    continue
                v, u = L, q
                if params(2, 1, c, u, v, 0, 1)[2:] != (N, q, gg):
                    continue
                cells.append((2, 1, c, u, v, 0, 1))
    seen, hits, checked = set(), [], 0
    dist = {}
    for cl in cells:
        if cl in seen:
            continue
        seen.add(cl)
        b, a, c, u, v, w, z = cl
        L, phi, N, q, g = params(b, a, c, u, v, w, z)
        if g > G_CAP or N > N_CAP:
            continue
        lo, hi, span, _ = interval(b, a, c, u, v, w, z)
        if lo > hi or span > N:
            continue
        if not (0 < N - span < g):
            continue
        if N - span != g - 1:
            ok(False, f"span deficit {N - span} != g - 1 = {g - 1} at {cl}")
            return []
        checked += 1
        ce = cell(b, a, c, u, v, w, z)
        counts, _ = below_counts(ce)
        for k in counts.values():
            dist[k] = dist.get(k, 0) + 1
        for t, k in counts.items():
            if k >= 2:
                seq, tau = orbit_levels(ce["f"], t, ce["g"])
                hits.append((cl, ce["g"], ce["n"], ce["J"], t, tau,
                             seq[:ce["J"]],
                             [j for j, x in enumerate(seq, 1)
                              if j < ce["J"] and x not in ce["A"]]))
    print(f"  mismatch-capable cells of the family read: {checked}")
    print(f"  span deficit = g - 1 at every one of them")
    print(f"  below-count distribution: {dict(sorted(dist.items()))}")
    print(f"  classes with below-count >= 2: {len(hits)}")
    for h in hits[:6]:
        cl, g, n, J, t, tau, orb, lev = h
        print(f"    HIT cell (b,a,c,u,v,w,z)={cl} g={g} n={n} J={J}")
        print(f"        class {t}, pre-period {tau}, orbit below J {orb},"
              f" unsaturated levels {lev},"
              f" multipliers {[2 ** j for j in lev]}")
    return hits


def specimen(cl):
    """R-J: the two-level cell through the parent's own tree walk."""
    b, a, c, u, v, w, z = cl
    ce = cell(b, a, c, u, v, w, z)
    W, star, bad = w_tree(b, a, c, u, v, ce, w, z)
    counts, _ = below_counts(ce)
    theirs = set()
    for t in range(ce["g"]):
        orb = orbit(ce["f"], t, ce["J"] + ce["g"])
        if all(x in ce["A"] for x in orb[ce["J"] - 1:]):
            theirs.add(t)
    print("R-J  THE SPECIMEN AGAINST THE PARENT'S TREE WALK")
    print(f"  cell (b,a,c,u,v,w,z) = {cl}")
    print(f"  N={ce['N']} q={ce['q']} g={ce['g']} n={ce['n']} "
          f"J={ce['J']} span={ce['span']} N-span={ce['N'] - ce['span']}")
    print(f"  saturated classes A = {sorted(ce['A'])}")
    print(f"  deep-saturated, this file: {sorted(counts)}")
    print(f"  deep-saturated, the parent's okdeep: {sorted(theirs)}")
    ok(set(counts) == theirs, "deep-saturated sets disagree")
    print(f"  below-counts: {dict(sorted(counts.items()))}")
    for j in sorted(bad):
        print(f"  level {j}: the parent rules out {len(bad[j])} states "
              f"of the interval")
    ok(all(len(bad[j]) > 0 for j in bad), "a claimed level rules out nothing")
    print(f"  |W| = {len(W)}, |W*| = {len(star)}, W == W*: {W == star}")
    ok(W != star, "the specimen shows no mismatch")
    two = [t for t, k in counts.items() if k >= 2]
    print(f"  classes with below-count >= 2: {sorted(two)}")
    ok(bool(two), "the specimen carries no two-level class")
    return two


def rigidity():
    """R-K: the deficit law's scope, on cells nobody selected."""
    rows, broken = [], []
    for b in range(2, 13):
        for a in range(1, 9):
            if 2 * a + 1 < b:
                continue
            tot = eq = 0
            for u in range(1, 120):
                for v in range(1, 40):
                    if gcd(u, v) != 1:
                        continue
                    for c in range(1, 8):
                        L, phi, N, q, g = params(b, a, c, u, v, 0, 1)
                        if N > 10 ** 7:
                            continue
                        lo, hi, span, _ = interval(b, a, c, u, v, 0, 1)
                        if lo > hi or span > N:
                            continue
                        if not (0 < N - span < g):
                            continue
                        tot += 1
                        if N - span == g - 1:
                            eq += 1
            if not tot:
                continue
            integral = (2 * a) % (b - 1) == 0
            rows.append((b, a, integral, eq, tot))
            if integral != (eq == tot):
                broken.append((b, a, eq, tot))
    ints = [r for r in rows if r[2]]
    fracs = [r for r in rows if not r[2]]
    print("R-K  THE RIGIDITY'S REAL SCOPE")
    print(f"  (b, a) rows read: {len(rows)}; integer 2a/(b-1): {len(ints)}, "
          f"fractional: {len(fracs)}")
    print(f"  integer rows, cells with D = g-1: "
          f"{sum(r[3] for r in ints)} of {sum(r[4] for r in ints)}")
    print(f"  fractional rows, cells with D = g-1: "
          f"{sum(r[3] for r in fracs)} of {sum(r[4] for r in fracs)}")
    print(f"  rows where integer-rho and totality disagree: {broken}")
    ok(not broken, "the deficit law's scope is not integer 2a/(b-1)")
    return rows


def smallest(cap=6000):
    """R-L: every two-level witness with N <= cap, sorted by N."""
    found = []
    for b in range(2, 13):
        for a in range(1, 9):
            if 2 * a + 1 < b:
                continue
            for v in range(1, 81):
                for c in range(1, 9):
                    N0 = v * b ** c
                    if N0 > cap:
                        break
                    for u in range(1, 601):
                        if gcd(u, v) != 1:
                            continue
                        L, phi, N, q, g = params(b, a, c, u, v, 0, 1)
                        if gcd(b, g) == 1:
                            continue
                        lo, hi, span, _ = interval(b, a, c, u, v, 0, 1)
                        if lo > hi or span > N:
                            continue
                        if not (0 < N - span < g):
                            continue
                        n = N // g
                        if depth_J(b, a, n) < 3:
                            continue
                        if preperiod_ceiling(b, g) < 3:
                            continue
                        ce = cell(b, a, c, u, v, 0, 1)
                        cnt, _ = below_counts(ce)
                        two = [t for t, k in cnt.items() if k >= 2]
                        if two:
                            found.append((N, g, n, ce["J"],
                                          (b, a, c, u, v), len(two)))
    found.sort()
    print("R-L  IS THE WITNESS THE SMALLEST")
    print(f"  two-level witnesses with N <= {cap}: {len(found)}")
    for r in found[:5]:
        print(f"    N={r[0]} g={r[1]} n={r[2]} J={r[3]} "
              f"(b,a,c,u,v)={r[4]} two-level classes={r[5]}")
    return found


def nesting(cap=3000):
    """R-M: deepest lost level alone, against the full intersection."""
    agree = disagree = cells = 0
    ex = []
    for b in range(2, 13):
        for a in range(1, 9):
            if 2 * a + 1 < b:
                continue
            for v in range(1, 81):
                for c in range(1, 9):
                    if v * b ** c > cap:
                        break
                    for u in range(1, 601):
                        if gcd(u, v) != 1:
                            continue
                        L, phi, N, q, g = params(b, a, c, u, v, 0, 1)
                        if gcd(b, g) == 1:
                            continue
                        lo, hi, span, _ = interval(b, a, c, u, v, 0, 1)
                        if lo > hi or span > N:
                            continue
                        if not (0 < N - span < g):
                            continue
                        n = N // g
                        if depth_J(b, a, n) < 3:
                            continue
                        if preperiod_ceiling(b, g) < 3:
                            continue
                        ce = cell(b, a, c, u, v, 0, 1)
                        cnt, _ = below_counts(ce)
                        two = [t for t, k in cnt.items() if k >= 2]
                        if not two:
                            continue
                        cells += 1
                        W, star, bad = w_tree(b, a, c, u, v, ce, 0, 1)
                        for t in two:
                            cls = [m for m in range(ce["lo"], ce["hi"] + 1)
                                   if m % g == t]
                            lost = [j for j in sorted(bad)
                                    if any(m in bad[j] for m in cls)]
                            if len(lost) < 2:
                                continue
                            deep = {m for m in cls if m not in bad[lost[-1]]}
                            inter = {m for m in cls
                                    if all(m not in bad[j] for j in lost)}
                            if deep == inter:
                                agree += 1
                            else:
                                disagree += 1
                                if len(ex) < 3:
                                    ex.append(((b, a, c, u, v), t, lost,
                                               len(deep), len(inter)))
    print("R-M  DOES THE DEEPEST LOST LEVEL SUBSUME THE SHALLOWER ONES")
    print(f"  two-level cells with N <= {cap}: {cells}; "
          f"class tests: {agree + disagree}")
    print(f"  deepest lost level alone = the full intersection: {agree}")
    print(f"  it is strictly larger: {disagree}")
    for e in ex:
        print(f"    disagreement (b,a,c,u,v)={e[0]} class {e[1]} "
              f"lost levels {e[2]}: deepest gives {e[3]}, "
              f"intersection {e[4]}")
    return agree, disagree


def main():
    print("=" * 68)
    print("TWO UNSATURATED LEVELS BELOW J -- does any class carry them?")
    print("=" * 68)
    print()
    r_a_controls()
    if FAILURES:
        print("CONTROL FAILED -- nothing below is read.")
        return 1
    h1, tau1, one1 = hunt(broad_scope(), "R-C/D/E/F  THE BROAD CENSUS")
    print()
    h2, tau2, one2 = hunt(phase_scope(), "R-C/D/E/F  THE PHASE CENSUS")
    print()
    collide(broad_scope(), "R-G  THE COLLISION, BROAD CENSUS")
    print()
    collide(phase_scope(), "R-G  THE COLLISION, PHASE CENSUS")
    print()
    robust()
    print()
    rigidity()
    print()
    smallest()
    print()
    nesting()
    print()
    con = construction()
    print()
    specimen((2, 1, 2, 40, 18, 0, 1))
    print()
    # the same (N, q, g) at a slope in LOWEST TERMS, which the cell
    # above is not: gcd(40, 18) = 2, and L = v reads the denominator as
    # written, so a non-reduced slope is a different cell and not the
    # same one relabelled. The reduced witness is what puts the case
    # inside the corpus's own stated scope.
    specimen((2, 1, 3, 40, 9, 0, 1))
    print()
    print("VERDICT")
    total = len(h1) + len(h2) + len(con)
    print(f"  two-level classes found: {total}")
    print(f"  pre-period ceiling reached: {max(tau1, tau2)}")
    print(f"  one-level classes found: {one1 + one2}")
    print()
    print("FAILURES:", FAILURES if FAILURES else "none")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
