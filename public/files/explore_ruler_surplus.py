"""explore_ruler_surplus.py -- THE SURPLUS IS THE CERTIFICATE'S WHOLE GAP
OVER THE RELAXATION, and that turns a mechanism into a criterion.

(The cells, the certificate, the exhaustive optimum and the exact solver
are all IMPORTED from explore_ruler_barecell.py, explore_ruler_exchange.py,
explore_ruler_setvalued.py and explore_ruler_optimum.py. What is new here
is one identity, one criterion derived from it, and the census that says
how far the criterion reaches.)

THE QUESTION. The marginal optimum's certificate -- every (atom, label)
pair strictly above the operative level t*, plus the cheapest tied
sub-collection closing the deficit -- is a sound upper bound that is
sometimes the optimum and sometimes not. What separates the two cases
was last read off four ring cells as a MECHANISM: the tied fill
overshoots the target by a surplus D, and an optimum spends the
overshoot. The surplus was 2.0e-2 where the certificate overstates and
2.8e-6 where it is exact. No criterion followed, because nothing said
how small a surplus must be, and a raw surplus is not a scale-free
quantity in the first place.

So: is there a NECESSARY half -- a condition on the surplus that FORBIDS
a disagreement rather than permitting one?

WHOSE VOCABULARY. LINEAR PROGRAMMING RELAXATION and its dual price, plus
one LATTICE argument about the costs a rule can have. Not the conformal
literature's, and not the exchange argument's: the whole point of the
derivation below is that it never argues about an exchange, which is
what let the previous route reach a sufficient condition and stop.
ATOM, LEVEL, TIED BLOCK and SURPLUS keep the parent files' senses. COST
LATTICE is this file's word for the set of costs a rule can have, which
is where the criterion's threshold comes from.

AND NEITHER ARGUMENT IS NEW AS AN ARGUMENT, which is worth saying before
any result is read. The identity is complementary slackness for this
program, and the step from a bounded integrality gap to an integral
optimum is the standard rounding argument. What is new is neither: it is
that these two, applied to THIS certificate, answer a question the
corpus had recorded as open and had been trying to answer by dialling
cells. The claim to make is about the answer, never about the machinery, and
reading this file as a discovery of either technique misreads it.

TRANSPLANT, MARKED. The reading that a smaller surplus goes with an
exact certificate is imported from the four ring cells and is the thing
under test, not a premise. Nothing else is carried in.

THE HAND ATTACK, worked on paper before any engine code, and it settled
the question outright -- what remains for the rig is a census and a
control on the arithmetic.

FIRST, THE IDENTITY. Write T = 1 - alpha for the target, A for the pairs
strictly above t*, S for the tied subset the fill picks, and

    above_cost = sum_{a in A} w_a,   above_cov = sum_{a in A} w_a p_a,
    deficit = T - above_cov,         fill = cost of S,
    cert = above_cost + fill,        coverage = above_cov + t* * fill,

the last because every tied pair covers exactly its cost times t*. The
surplus is D = coverage - T. The relaxation at price 1/t* gives each
pair the reduced cost rc_i = w_i (1 - p_i/t*), negative exactly on A, so

    L = T/t* + sum_{rc < 0} rc_i = above_cost + deficit/t*.

Subtracting,

    cert - L = fill - deficit/t* = (t* * fill - deficit)/t* = D / t*.

THE CERTIFICATE'S GAP OVER THE RELAXATION IS THE SURPLUS DIVIDED BY THE
LEVEL, exactly, for every cell. It uses nothing about S being minimal,
so it holds whatever the subset sum returned -- a capped greedy fill
included. It is stated against L and not against certified_optimum's
returned `lower`, which is above_cost in the deficit <= 0 branch and is
a different number there; a rig reading `lower` would find the identity
false at exactly those cells and would be reading the wrong quantity.

SECOND, THE ERROR CAP. Every feasible rule costs at least L, so

    0 <= cert - OPT <= D / t*.

The surplus does not correlate with exactness. It BOUNDS the
inexactness. In particular D = 0 forces cert = L = OPT: a tied fill that
lands exactly on the target certifies its own optimality, which is the
necessary half the mechanism was missing -- a disagreement REQUIRES a
positive surplus.

THIRD, THE CRITERION, which is the cap plus one integrality step. A
rule's cost is sum_r s_r w_r over integer sizes s_r, so cert and OPT
both lie in the lattice the weights generate, and their difference lies
in its difference group. For weights w_r = n_r/Q in lowest common terms
that group is (d/Q) Z with d = gcd(n_1, ..., n_M), so the smallest
possible positive gap is g = d/Q. Hence

    D / t*  <  g   =>   cert = OPT,

a sufficient condition for EXACTNESS that needs no search and no
exchange argument -- only the certificate, the level, and the weights.

FOURTH, IT SUBSUMES THE PROVED CASE. At equal weights every w_r = w0 =
1/M, so Q = M, every n_r = 1 and g = w0. S is irredundant -- a min-cost
subset cannot contain a removable item, every weight being positive, and
that step is named here because it is the one the argument RIDES on --
so removing any tied item breaks feasibility and the coverage it carried,
w_s t*, exceeds the surplus: D < w_s t* = w0 t* for any s in S,
hence D/t* < w0 = g and the criterion fires at EVERY equal-weight cell.
The equal-weight exactness theorem is this criterion's special case, so
the criterion is a THIRD route to it, sharing no step with the exchange
bound or the count-the-labels greedy that reached it before.

FIFTH, WHERE THIS CAN BE WRONG RATHER THAN WEAK. The identity is
arithmetic and the rig checks it in exact Fractions at every cell it
scores; a single failure means the imported machinery is not what this
derivation describes. The criterion inherits the cap, so a firing at a
cell where cert > OPT refutes it outright. What it CANNOT be is a
characterization: g is a property of the weights alone, so a cell whose
weights generate a fine lattice gets no help however small its surplus
is, and the census below is what says how much of the exactness verdict
is left undecided.

SIXTH, THE ALGEBRA OF THE STATISTIC ITSELF. t* > 0 at every cell, so
D/t* never blows up -- and that is DERIVED and not observed, the
derivation added at audit where the freeze had only asserted it: the
candidate levels are the posterior values, including every positive one,
and taking all of those covers mass 1, which clears any target below 1;
so the largest level still reaching the target is at least the smallest
positive posterior. The same argument run one step further is what makes
certified_optimum's deficit <= 0 branch unreachable at the operative
level (see the run record). The SPEND FRACTION (cert - OPT)/(D/t*) is the one
quantity here with a vanishing denominator: it is defined only where
D > 0, and where D = 0 the cap already forces the numerator to zero, so
the rig reports the D = 0 cells as a COUNT and never as a ratio.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. The identity cert - L = D/t* holds in exact Fractions at every
      cell scored -- the bare cells, the whole designed sweep, the four
      ring cells and the theta walk. (Derivation; one failure refutes.)
  P2. The criterion fires at ZERO cells where cert > OPT. (Derivation.)
  P3. It fires at ALL 125 equal-weight sweep cells (FOURTH), and at
      FLAT-3 and DEAD-7, whose fifteen atoms carry equal weight.
  P4. It does NOT fire at TILT-4-WIDE. That cell's certificate IS exact
      and its surplus is the smallest measured, but its 105 geometric
      weights generate a lattice whose gap is far below its D/t* of
      4.3e-6 -- so the criterion misses an exactness it cannot see.
  P5. At the unequal-weight sweep cells where the certificate is exact,
      the criterion decides at least a third of them. (A guess at the
      reach, and the number is what the census is for.)
  P6. On the theta walk at TILT-3's ring shape, D/t* and g SHRINK
      TOGETHER as theta rises toward 1, so the criterion's reach does
      not improve monotonically with a finer tied block. (The reading
      the four cells invite is that a finer block is better; this says
      the weights that make it finer make the threshold finer too.)

KILLS, as observables rather than as inferences -- what the rig prints,
with what it would mean weighed only after the run.
  K-A. Any nonzero count of cells where the criterion fires and
       cert > OPT.
  K-B. Any nonzero count of cells where cert - L != D/t* in Fraction.
  K-C. Any cell printing OPT < L or OPT > cert.
  K-D. Any ring or walk cell where the solver returns CAPPED. That is a
       refusal with its node count named, not a result.

CONTROLS, run and read BEFORE any kill or survive result, each printing
HOW MANY cases it exercised.
  C1 (POSITIVE, ON THE AXIS THE ARM VARIES). The criterion must fire at
     UNEQUAL-weight cells where the certificate is exact -- counted, with
     the share of such cells it reaches. The equal-weight point is where
     FOURTH proves it fires, so a control read there could not fail on
     the axis this arm walks and would certify nothing about reach.
  C2 (PARITY). The seven bare cells: certificate against exhaustive
     optimum, reproducing the parent files' own 7/7 agreement.
  C3 (TRUTH). Every generated cell's posteriors sum to 1 per atom and
     its weights sum to 1, in Fraction.
  C4 (BRANCH). The count of cells where certified_optimum's returned
     `lower` differs from the true relaxation L -- the deficit <= 0
     branch FIRST names. Printed so the identity is never read off the
     wrong number silently, and so that branch is known to be exercised
     rather than assumed absent.
  C5 (WITNESS). At every ring and walk cell, the certificate's rule is
     rebuilt explicitly and its cost and coverage recomputed from the
     cell, so the reported number is known to belong to a rule that
     EXISTS. Every other control here compares a number to a number.

THE ARMS.
  1. The seven bare cells (C2, P1).
  2. The 19,125-cell designed sweep plus its 125 equal-weight cells:
     the identity, the criterion's firing census against the exhaustive
     optimum, and the spend fraction (P1, P2, P3, P5, C1, C3, C4).
  3. The four ring cells, with the solver supplying OPT (P1, P3, P4, C5).
  4. THE THETA WALK. TILT-3's ring shape held fixed -- primes (3,5,7),
     read (3,5), so M = 15 atoms, c = 7, k = 3 -- with theta walked over
     a geometric ladder in 1 - theta: theta = (n-1)/n for n in 3, 5, 10,
     25, 50, 100, 200, 400, 1000. That ladder is a DESIGN CHOICE and not
     a measurement: n = 25 is TILT-3 itself and n = 200 is TILT-4-WIDE's
     tilt carried onto TILT-3's shape, and the rest walk out from those
     two in both directions. THE DIALS ARE LOCKED ON THIS ARM and it is
     read that way: theta sets the atom weights (geometric at ratio
     theta) AND the posteriors (geometric at ratio q = theta^M), so a
     walk here moves both at once. What separates them is arm 2, whose
     designed cells cross 125 posterior menus with 153 weight vectors
     independently; this arm adds SCALE (M = 15 rather than 3) with the
     dials tied, and no conclusion about which dial did the work is
     read off it (P6, P1, K-D).

RESOURCE NOTE. Exact Fractions throughout, no numpy. Arm 2 is the same
19,125 cells the exchange rig scored in 14.8s with the same 64-vector
exhaustive optimum, plus a handful of Fraction operations per cell. Arm
3 re-solves the four ring cells, whose peak is TILT-4-WIDE's truth at
about 184 MB in the parent file. Arm 4 solves nine cells at M = 15, the
size TILT-3 solved in 17 nodes. Estimated a couple of minutes and well
under the 512 MB default; the run record below carries what it cost.

RUN RECORD (wall 27.0s, peak working set 182.8 MB against the 512 MB
default under memwatch -- the peak is TILT-4-WIDE's truth, as it is in
the parent files). 19,270 SCORINGS in exact Fractions over 19,269
distinct cells: 7 bare, 19,125 designed unequal-weight, 125 equal-weight,
4 ring and 9 walk. The one cell scored twice is TILT-3, which is also the
walk's n = 25 rung, and that is a PARITY CONTROL nothing had to build:
the walk's constructor is handed the ring cell's own arguments at that
rung and reproduces every figure it prints -- relaxation 0.9008338,
certificate 0.9287750, optimum 0.9194957, D/t* 2.794e-02, spend 0.3321 --
so the eight other rungs are known to be the same family and not a
lookalike. No floats anywhere in a verdict; the tables below are output
copied verbatim and run wider than this file's prose.

READING THE PRINTS CAUGHT TWO THINGS NO ASSERT WOULD HAVE.

The first is which certificate the ring arm was reading.
certified_optimum falls back to a GREEDY fill past its subset-sum cap,
so its `upper` at TILT-4-WIDE is 0.9027944 -- a feasible rule 6.1e-3
worse than the certificate whose exactness the corpus asks about, which
is the one with the fill computed exactly, 0.8967012. The first run
printed CERT EXACT False there, contradicting the parent file, and the
contradiction was the instrument reading a different object under the
same name. The arms now read the exact-fill certificate and print the
capped one beside it wherever the two differ. THE IDENTITY HOLDS OF
BOTH, which is not a patch but the point: it never uses the fill's
minimality, so a capped greedy fill satisfies it exactly as an optimal
subset sum does -- 6.097e-3 = 3.982e-3 / 0.652981 at the capped rule and
4.349e-6 = 2.840e-6 / 0.652981 at the exact one.

The second is that C4 NEVER FIRED, at any of the 19,270 scorings, and the
reason is a derivation the hand attack had missed rather than a sample
that happened to miss the branch. The operative level is the LARGEST
level whose full inclusion reaches the target, so if the strictly-above
set alone already covered the target, the next posterior value up would
be operative instead. Hence the deficit is strictly positive at the
operative level ALWAYS, certified_optimum's `lower` always equals the
relaxation L, and the deficit <= 0 branch is unreachable there. FIRST's
warning about reading `lower` is therefore about robustness against a
non-operative level and never about a live case -- and the control is
what says which of those two it is, since a zero from a control that
could not have fired reads exactly like a zero from one that could.

P1 HOLDS. Zero identity failures at all 19,270 scorings: cert - L = D/t*
in exact Fraction everywhere, at both the exact and the capped fill.
P2 HOLDS. The criterion fires at ZERO of the 5,447 cells where the
certificate overstates, and at zero of the walk's eight.
P3 HOLDS. 125/125 equal-weight cells, and FLAT-3 and DEAD-7.
P4 HOLDS. TILT-4-WIDE's 105 geometric weights generate a lattice of gap
6.0e-242 against a D/t* of 4.3e-6, so the criterion misses an exactness
that is real by 236 orders of magnitude.
P5 HOLDS, at 55.9%. The criterion decides 7,643 of the 13,678 exact
unequal-weight cells -- 3,326 of them the trivial D = 0 half, so what
the LATTICE buys over the zero-surplus reading is 4,317 cells, a third
of the exact ones again.

  arm                 cells  identity  fires  at exact  overstating
  bare                    7         7      7       7/7            0
  designed unequal   19,125    19,125  7,643  7,643/13,678   5,447
  designed equal        125       125    125     125/125          0
  ring                    4         4      2       2/3 exact      1
  theta walk              9         9      0       0/1 exact      8

  cell            M   k      relax certificate    optimum      D/t*         g  fires
  TILT-3         15   3  0.9008338  0.9287750  0.9194957 2.794e-02 2.345e-21  False
      t* 0.715991  mult 10  surplus 2.001e-02  cert exact False  spend 0.3321
  FLAT-3         15   3  1.9500000  2.0000000  2.0000000 5.000e-02 6.667e-02   True
      t* 0.285714  mult 30  surplus 1.429e-02  cert exact True   spend 0.0000
  DEAD-7         15   7  4.9000000  4.9333333  4.9333333 3.333e-02 6.667e-02   True
      t* 0.142857  mult 105 surplus 4.762e-03  cert exact True   spend 0.0000
  TILT-4-WIDE   105   4  0.8966969  0.8967012  0.8967012 4.349e-06 6.024e-242  False
      t* 0.652981  mult 26  surplus 2.840e-06  cert exact True   spend 0.0000

THE FOUR-CELL MECHANISM IS SUBSUMED, AND ITS ORDERING IS REAL RATHER
THAN AN ARTIFACT -- the correction the audit made to this paragraph, the
first draft having blamed the units. The two levels are 0.716 and 0.653,
so rescaling by them moves nothing: 2.0e-2 against 2.8e-6 becomes
2.8e-2 against 4.3e-6, the same four orders. What was wrong was the
INFERENCE and not the arithmetic.
What the corpus read as "a smaller surplus goes with an exact
certificate" is the cap: D/t* is the entire room between the certificate
and the relaxation, so TILT-4-WIDE's certificate is pinned within 4.3e-6
of optimal by its surplus alone -- the EQUALITY there is still the
search's, and no surplus decides it -- while TILT-3's room of 2.8e-2
pins nothing, and its optimum takes a third of it. Nothing about a wider
tied block being a finer one is needed to say that -- the two bounds
differ by four orders and only one of them is strong enough to force its
answer, which is the whole of it.

P6 IS REFUTED, AND IN THE DIRECTION THAT MATTERS FOR THE CRITERION.

  cell     theta      t*  mult      D/t*          g  fires   spend  nodes
  W-3        2/3  1.0000     5  5.314e-03  6.985e-08  False  0.9983   5519
  W-5        4/5  0.9988    10  5.920e-03  3.396e-11  False  0.9767     39
  W-10      9/10  0.9576    10  7.008e-04  1.259e-15   True* 0.0000      1
  W-25     24/25  0.7160    10  2.794e-02  2.345e-21  False  0.3321     17
  W-50     49/50  0.2817     5  5.380e-02  1.253e-25  False  0.2164   1881
  W-100   99/100  0.2954     5  2.518e-02  7.146e-30  False  0.1016   2892
  W-200  199/200  0.2935     5  3.537e-02  4.213e-34  False  0.0940  31928
  W-400  399/400  0.2904     5  4.259e-02  2.527e-38  False  0.0394 3899149
  W-1000 999/1000 0.2877     5  7.202e-03  6.713e-44  False  0.0463  28153
  (* W-10's certificate IS exact; the criterion does not fire there
   either -- the column is the exactness verdict, not the criterion's.)

The two quantities do NOT shrink together. g collapses MONOTONICALLY
across thirty-six orders of magnitude, since the lattice a geometric
weight vector generates gets finer with every rung; D/t* WANDERS with no
trend at all, between 7.0e-4 and 5.4e-2, and is larger at the finest
rung than at the coarsest. So g alone settles every rung of the walk and
the surplus never gets a say.

READ PER RUNG AND NOT IN AGGREGATE, because "fires nowhere on the walk"
counts nine rungs where only ONE of them could ever have fired. Eight
carry an overstating certificate, so no valid test may fire there and
their silence is not evidence of anything. The single live rung is W-10,
the only one whose certificate is exact, and the criterion misses it by
eleven orders of magnitude -- 1.259e-15 against a D/t* of 7.008e-4. That
one rung is the whole of the walk's evidence, and it is still the
prediction's refutation: at geometric weights the criterion has no reach
where reach was available, and the reading the four cells invited (that
a finer block helps) is not merely unproved but irrelevant, because the
weights that make the block finer make the threshold finer faster.

THE DIALS ARE LOCKED ON THIS ARM and nothing about which one did the
work is read off it. What arm 2 says with the dials crossed
independently is that the criterion's reach is a WEIGHT property: it
fires at 100% of the equal-weight cells and 55.9% of the unequal ones,
and the /20 weight grid keeps g at 1/20 or better where the geometric
family drives it to 1e-21 at fifteen atoms.

THE OPTIMUM NEVER TAKES ALL THE ROOM. The spend fraction
(cert - OPT)/(D/t*) is exactly 1 at NONE of the 15,882 cells with room,
mean 0.1825 over the unequal sweep, worst 0.9808. So the cap is sound
and nowhere attained on this family -- OPT = L would need the relaxation
to be reached by an integral rule, and no cell here does it. On the walk
the fraction falls as theta rises, 0.998 at n = 3 to 0.046 at n = 1000,
which is the room growing while the optimum stops chasing it.

WHAT THIS LEAVES OPEN. The criterion is sufficient and not necessary,
and the census says how far short: 6,035 of the 13,678 exact unequal
cells are exact for a reason it cannot see. Nothing here bounds the
spend fraction away from 1 -- that it never reaches 1 is measured over
15,882 cells and not derived. And the walk's cost is not uniform: W-400
took 3.9M search nodes against W-10's one, which no property of the cell
printed here predicts.
"""

import os
import sys
import time
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_setvalued import CELLS, Cell  # noqa: E402
from explore_ruler_barecell import (  # noqa: E402
    BARE,
    certified_optimum,
    exhaustive_optimum,
    operative_level,
)
from explore_ruler_exchange import (  # noqa: E402
    ALPHA, EQUAL, ROWS, WEIGHTS, check_truth, make_cell,
)
from explore_ruler_optimum import (  # noqa: E402
    control_C6, solve, surplus as exact_fill_surplus,
)

F = Fraction

# The theta ladder of arm 4: theta = (n-1)/n, geometric in 1 - theta.
LADDER = (3, 5, 10, 25, 50, 100, 200, 400, 1000)


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lattice_gap(cell):
    """g -- the smallest positive difference between two rule costs.

    A rule costs sum_r s_r w_r over integer sizes, so the reachable
    costs lie in the lattice the weights generate and their differences
    in its difference group. Writing w_r = n_r/Q over the common
    denominator, that group is (d/Q) Z with d = gcd of the numerators.
    """
    ws = [cell.atom_prob(r) for r in range(cell.M)]
    Q = 1
    for w in ws:
        Q = Q * w.denominator // _gcd(Q, w.denominator)
    d = 0
    for w in ws:
        d = _gcd(d, w.numerator * (Q // w.denominator))
    return F(d, Q)


def ring_truth(cell):
    """C3 on a RING cell, which carries no explicit weight vector: its
    atom marginal and every posterior row sum to 1 in Fraction."""
    if sum(cell.atom_prob(r) for r in range(cell.M)) != 1:
        return False
    for r in range(cell.M):
        if sum(cell.posterior(r)) != 1:
            return False
    return True


def measure(cell, alpha):
    """The identity, the cap and the criterion at one cell.

    Returns a dict of exact Fractions. L is recomputed here rather than
    read from certified_optimum's `lower`, which is a different number
    in the deficit <= 0 branch.
    """
    target = 1 - alpha
    level, mult, _cov, _sets = operative_level(cell, alpha)
    above_cost = above_cov = F(0)
    for r in range(cell.M):
        w = cell.atom_prob(r)
        post = cell.posterior(r)
        for y in range(cell.k):
            if post[y] > level:
                above_cost += w
                above_cov += w * post[y]
    lower, cert, exact_fill, cov = certified_optimum(cell, alpha, level)
    L = above_cost + (target - above_cov) / level
    D = cov - target
    gap = lattice_gap(cell)
    return dict(level=level, mult=mult, L=L, lower=lower, cert=cert,
                D=D, room=D / level, gap=gap, fires=D / level < gap,
                exact_fill=exact_fill,
                identity=(cert - L == D / level),
                branch=(lower != L))


def spend(m, opt):
    """The share of the room the optimum actually takes, or None where
    the room is zero -- the cap already forces the gap to zero there."""
    if m["room"] == 0:
        return None
    return (m["cert"] - opt) / m["room"]


def arm_sweep(weights, tag):
    """Arm 2: identity, criterion census and spend fraction per cell."""
    out = dict(seen=0, bad_truth=0, bad_identity=0, bad_order=0,
               branch=0, zero_room=0, fires=0, fires_exact=0,
               fires_inexact=0, exact=0, inexact=0, fires_at_exact=0,
               capped_fill=0, fires_zero=0,
               worst_spend=None, spend_n=0, spend_sum=F(0), spend_one=0)
    for rows in ROWS:
        for wts in weights:
            cell = make_cell(tag, rows, wts)
            if not check_truth(cell):
                out["bad_truth"] += 1
                continue
            m = measure(cell, ALPHA)
            opt = exhaustive_optimum(cell, ALPHA)
            out["seen"] += 1
            if not m["identity"]:
                out["bad_identity"] += 1
            if m["branch"]:
                out["branch"] += 1
            if m["room"] == 0:
                out["zero_room"] += 1
            if not m["exact_fill"]:
                out["capped_fill"] += 1
            if opt is None:
                continue
            if opt < m["L"] or opt > m["cert"]:
                out["bad_order"] += 1
            is_exact = opt == m["cert"]
            out["exact" if is_exact else "inexact"] += 1
            if m["fires"]:
                out["fires"] += 1
                out["fires_exact" if is_exact else "fires_inexact"] += 1
                if m["room"] == 0:
                    out["fires_zero"] += 1
                if is_exact:
                    out["fires_at_exact"] += 1
            s = spend(m, opt)
            if s is not None:
                out["spend_n"] += 1
                out["spend_sum"] += s
                if s == 1:
                    out["spend_one"] += 1
                if out["worst_spend"] is None or s > out["worst_spend"][0]:
                    out["worst_spend"] = (s, rows, wts)
    return out


def report_cell(cell, m, s):
    """One ring or walk cell, read at the EXACT-FILL certificate.

    certified_optimum falls back to a greedy fill past its subset-sum
    cap, so its `upper` is not the certificate whose exactness the
    corpus asks about wherever `exact_fill` is False -- at TILT-4-WIDE
    it is a rule 6.8e-3 worse. The solver recomputes the fill exactly,
    and that is the certificate read here; the capped one is printed
    beside it wherever the two differ, since the identity holds of
    BOTH and holding of a capped fill is part of what it says.
    """
    opt = s.opt
    cert = m["cert"] if s.cert is None else s.cert
    if s.cert is None:
        D, room = m["D"], m["room"]
    else:
        D = exact_fill_surplus(cell, ALPHA, m["level"], s)
        room = D / m["level"]
    opts = "CAPPED" if opt is None else "%.7f" % float(opt)
    print("  %-12s %4d %3d %10.7f %10.7f %10s %9.3e %9.3e %6s"
          % (cell.name, cell.M, cell.k, float(m["L"]), float(cert),
             opts, float(room), float(m["gap"]), room < m["gap"]))
    if opt is None:
        print("      REFUSED: solver capped at %d nodes" % s.nodes)
        return
    sp = None if room == 0 else (cert - opt) / room
    print("      t* %.6f  mult %d  surplus %.3e  identity %s  "
          "cert exact %s  spend %s"
          % (float(m["level"]), m["mult"], float(D),
             cert - m["L"] == room, opt == cert,
             "--" if sp is None else "%.4f" % float(sp)))
    if not m["exact_fill"]:
        print("      capped fill stands at %.7f (surplus %.3e, identity "
              "%s) -- the parent bound, not this certificate"
              % (float(m["cert"]), float(m["D"]), m["identity"]))


def main():
    print("THE SURPLUS AS A CRITERION -- the certificate's gap over the")
    print("relaxation, and the cost lattice that turns it into a test.")
    print("alpha = %s, nominal coverage %s" % (ALPHA, 1 - ALPHA))
    print()

    print("C2 PARITY -- the seven bare cells")
    par_ok = par_n = par_branch = 0
    for cell in BARE:
        m = measure(cell, ALPHA)
        ex = exhaustive_optimum(cell, ALPHA)
        print("  %-12s cert %9.5f  exhaustive %9s  identity %s  "
              "room %.3e  g %.3e  fires %s"
              % (cell.name, float(m["cert"]),
                 "--" if ex is None else "%.5f" % float(ex),
                 m["identity"], float(m["room"]), float(m["gap"]),
                 m["fires"]))
        if m["branch"]:
            par_branch += 1
        if ex is not None:
            par_n += 1
            if ex == m["cert"]:
                par_ok += 1
    print("  certificate == exhaustive at %d/%d bare cells; "
          "C4 branch fires at %d" % (par_ok, par_n, par_branch))
    print()

    for weights, tag, label in ((WEIGHTS, "SW", "UNEQUAL-weight sweep"),
                                ([EQUAL], "EQ", "EQUAL-weight arm")):
        t0 = time.time()
        r = arm_sweep(weights, tag)
        print("%s: %d cells, %.1fs" % (label, r["seen"], time.time() - t0))
        print("  K-B identity failures: %d   K-C order violations: %d"
              "   C3 truth failures: %d"
              % (r["bad_identity"], r["bad_order"], r["bad_truth"]))
        print("  C4 branch (returned lower != L): %d   "
              "zero-room cells: %d" % (r["branch"], r["zero_room"]))
        print("  certificate exact: %d   overstating: %d"
              % (r["exact"], r["inexact"]))
        print("  K-A criterion fires where it overstates: %d"
              % r["fires_inexact"])
        print("  C1 criterion fires at %d cells, %d of them exact "
              "(%d at zero room, %d bought by the lattice)"
              % (r["fires"], r["fires_exact"], r["fires_zero"],
                 r["fires"] - r["fires_zero"]))
        print("      capped tied fills over the arm: %d"
              % r["capped_fill"])
        if r["exact"]:
            print("      reach: %d/%d = %.1f%% of the exact cells"
                  % (r["fires_at_exact"], r["exact"],
                     100.0 * r["fires_at_exact"] / r["exact"]))
        if r["spend_n"]:
            print("  spend fraction over %d cells with room: mean %.4f, "
                  "at 1.0 exactly %d"
                  % (r["spend_n"], float(r["spend_sum"]) / r["spend_n"],
                     r["spend_one"]))
            s, rows, wts = r["worst_spend"]
            print("      worst %.4f at rows=%s weights=%s"
                  % (float(s), rows, [str(x) for x in wts]))
        print()

    print("THE FOUR RING CELLS -- the solver supplies the optimum")
    print("  %-12s %4s %3s %10s %10s %10s %9s %9s %6s"
          % ("cell", "M", "k", "relax", "certificate", "optimum",
             "D/t*", "g", "fires"))
    for cell in CELLS:
        t0 = time.time()
        m = measure(cell, ALPHA)
        s = solve(cell, ALPHA)
        report_cell(cell, m, s)
        w = control_C6(cell, ALPHA, s)
        print("      C5 witness: cost matches %s, covers %s   "
              "C3 truth %s   (%.1fs)"
              % (w if w is None else w[0], w if w is None else w[1],
                 ring_truth(cell), time.time() - t0))
    print()

    print("THE THETA WALK -- TILT-3's ring shape, theta = (n-1)/n")
    print("  %-12s %4s %3s %10s %10s %10s %9s %9s %6s"
          % ("cell", "M", "k", "relax", "certificate", "optimum",
             "D/t*", "g", "fires"))
    for n in LADDER:
        cell = Cell("W-%d" % n, (3, 5, 7), (3, 5), 3, F(n - 1, n))
        t0 = time.time()
        if not ring_truth(cell):
            print("  W-%-10d TRUTH FAILURE" % n)
            continue
        m = measure(cell, ALPHA)
        s = solve(cell, ALPHA)
        report_cell(cell, m, s)
        w = control_C6(cell, ALPHA, s)
        print("      C5 witness: cost matches %s, covers %s   "
              "nodes %d   (%.1fs)"
              % (w if w is None else w[0], w if w is None else w[1],
                 s.nodes, time.time() - t0))


if __name__ == "__main__":
    main()
