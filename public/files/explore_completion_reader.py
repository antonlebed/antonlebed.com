"""What is the COMPLETION reader's OWN minimum lookahead? The interval
game on the residual, solved over one period, at the cells the flush
price was printed at.

THE QUESTION
------------
explore_flush_price.py prices the flush as c_int - c_saf, and its H2
says plainly that the price UNDERSTATES the gap it is a proxy for:
c_saf's reader tracks the integer-offset branches, is confined in the
conjugate coordinate as well, and carries a box derived over an
ACCEPTING tail. The completion reader meets less than any of that. It
is the map on INFINITE strings: it tracks no offsets, and its whole
requirement is that the real star stay in range. So c_comp <= c_saf and
the other end of the comparison has never been measured.

It is not this game with a different box. It is not a game on a state
space at all. At level L the reader has seen d_0..d_{L+c} and owes a
residual that is an INTERVAL -- the unseen input tail, scaled by m --
and the level-L range is the union of its members e theta_L + [level
L + 1 range], overlapping consecutively. The reader wins iff it can
always name a member containing that whole interval, forever. The
interval's width and the members' widths and spacings are all fixed
multiples of |theta_L| at a periodic window, so the whole question is a
game on ONE real coordinate -- where the interval's left endpoint sits
inside the level-L range -- with the phase running around the period.

Two numbers come out of it and they are different:

    c_ov   the least c at which EVERY placement is coverable (the
           overlap lemma read with the TRUE widths, not the estimates
           the OVERLAP BOUND of explore_redundant_ostrowski.py H3 uses)
    c_comp the least c at which the reader WINS the game -- the
           placements it cannot cover need also be REACHABLE

c_ov is a sufficient bound and sharpens that overlap bound, which
throws away a factor 2 on the interval and uses a ratio test on |theta|
in place of the overlap itself. c_comp is the reader's actual minimum:
c_comp <= c_ov, and a gap between them is the adversary failing to
steer.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
H1  THE INDEX CONVENTION, RE-DERIVED FROM THE ENGINE. Game.step emits y
    at pos and then reads input index pos + look + 1; cap_in(k) is
    a_1 - 1 at k = 0 and a_{k+1} otherwise, at the cap only over a zero;
    cap_out(pos) is a_1 - 1 + s_0 at 0 and a_{pos+1} + s otherwise;
    theta_k = q_k alpha - p_k with theta_{-1} = 1, theta_0 = alpha, and
    a string's value is sum_k d_k theta_k. So a reader at lookahead c
    emits e_t having seen d_0..d_{t+c}, the parent's convention.
H2  WHAT THE RESIDUAL IS, EXACTLY. Write X = m val(d) and let M be the
    integer the coding is free to shift by (two codings of one integer
    differ by an integer in the real star). At level t the residual
    owed is R_t = X - M - sum_{k<t} e_k theta_k, and the reader wins iff
    R_t lies in the level-t range T_t = {sum_{k>=t} e_k theta_k} at
    every t -- necessary because an admissible tail must exist,
    sufficient because one then does. Knowing d_0..d_{t+c} pins R_t to
    an interval I_t = (known part) + m A_{t+c+1}, A_i the set of values
    of legal input tails from index i. The reader must place I_t whole
    inside one member, because the union of the members it could
    otherwise fall into over the unseen digits IS I_t.
H3  THE WIDTHS, AND WHERE THE OVERLAP BOUND LOSES ITS FACTOR 2 (the
    item labels here are this file's own; the bound is
    explore_redundant_ostrowski.py's). T_k has width
    W_k = |theta_{k-1}| + |theta_k| + s S_k, S_k = sum_{j>=k}|theta_j|,
    and its members are spaced |theta_k| apart with width W_{k+1}, so
    they overlap by W_{k+1} - |theta_k| = |theta_{k+1}| + s S_{k+1}.
    The unseen tail A_i is an interval of width sum_{j>=i} a_{j+1}
    |theta_j| = |theta_{i-1}| + |theta_i| -- the greedy rule removes
    OVERLAPS between members and not width, the extremal strings
    (a_{i+1}, 0, a_{i+3}, 0, ...) obeying it since same-sign positions
    are two apart. So |I_t| = m(|theta_{t+c}| + |theta_{t+c+1}|), where
    the overlap bound writes 2m|theta_{t+c}| -- an overestimate,
    strictly, and that tightening is the whole of c_ov's edge over it.
H4  WHERE THE GREEDY RULE DOES BITE: the WIDTH OF THE UNSEEN TAIL
    DEPENDS ON THE LAST DIGIT SEEN. After d_{t+c} = 0 the next digit
    may reach its cap and the tail set is the full A^(1); otherwise the
    top member is barred and the tail set is a strictly smaller
    A^(0) = A^(1) less its extreme member. So the game's state carries
    that flag, exactly as Game's pzd does, and the interval's width is
    a function of (phase, flag) and not of phase alone. Dropping the
    flag would over-state the adversary and could forge a loss.
H5  THE PLACEMENT ARITHMETIC, AND WHY IT NEEDS NO SIGNS. Measure a
    placement u as (left endpoint of I_t - min T_t) in units of
    |theta_t|. Whatever the sign of theta_t, the members' left
    endpoints are then exactly u = 0, 1, ..., N_phi with N_phi the
    output cap, each of width W_{k+1}: for theta_t > 0 the member index
    is e, for theta_t < 0 it is N_phi - e, and the range's own width is
    N_phi |theta_t| + W_{k+1} either way. The reader's move is legal iff
    j <= u and u + |I_t| <= j + W_{k+1}. The adversary's digit x then
    picks a sub-interval of I_t whose left offset is m times the offset
    of x's member inside A^(g) -- and THOSE members do have unequal
    widths (x = 0 leaves the flag set, x >= 1 clears it), so their
    offsets are computed from the A endpoints and not from x alone.
H6  WHY THE FIXPOINT'S TWO VERDICTS ARE BOTH FINITE CERTIFICATES. The
    bad set grows monotonically from B_0 = the uncoverable placements;
    an initial state entering it at round n is a LOSS proved by an
    n-step adversary strategy, and a round changing nothing is a WIN
    proved by an invariant. Neither needs the iteration to be known to
    converge, which is what makes "no finite decision" a reportable
    third outcome rather than a rig fault.
H7  WHERE IT CAN BLOW UP. The tail sums S_k and the sets A_i and T_k are
    computed as FIXPOINTS over the period and not from a truncated
    theta recursion: theta_k = a theta_{k-1} + theta_{k-2} in floats is
    cancellation garbage by depth 24 (the parent's h3_bound says so in
    its own docstring), so every ratio here is built from the continued
    fraction tails r_phi = [0; a_phi, a_{phi+1}, ...], which are a
    contraction fixpoint and lose nothing. And the interval lists must
    be merged with a tolerance or they fragment without bound; the
    verdict is re-run with the bad set inflated and deflated by a
    margin, and a cell whose verdict moves between the two is reported
    and not read.
TRANSPLANT, marked: the windows, the grid, the slacks, the frozen band
cells and the frozen c_int/c_saf answer key are the parent rigs'
(explore_redundant_ostrowski.py, explore_lookahead_band.py,
explore_flush_price.py). Nothing here re-derives them. What is NOT
transplanted is the box: this rig has none, and that is the point.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  C1 (controls, run FIRST; nothing below is read if any leg is red)
     (a) THE INTERVAL MACHINERY AGAINST BRUTE FORCE. At every window,
         the fixpoint endpoints of A_i^(0), A_i^(1) BRACKET the min and
         max over an explicit enumeration of legal strings, and sit
         within the tail that enumeration truncates; and |A_i^(1)| and
         W_k agree to 1e-9 with |theta_{i-1}| + |theta_i| and with
         |theta_{k-1}| + |theta_k| + s S_k built from the same ratios.
         (THE TOLERANCE HERE WAS MIS-SPECIFIED AT THE FREEZE and is
         corrected in place: the first text asked for agreement to 1e-9
         against a depth-12 enumeration, which no window can meet --
         the truncated tail is 5e-3 at golden and 1e-8 only at [5], and
         the first run printed exactly that spread, the fixpoint lying
         OUTSIDE the enumeration at all 40 flagged legs and inside its
         own truncation window at every one. What the corrected leg
         asks is strictly two-sided and directional, and the two closed
         forms it is checked against were green on that run and are
         untouched.)
     (b) c_comp <= c_ov AT EVERY CELL PRINTED (H6: an empty B_0 leaves
         an empty bad set).
     (c) c_comp <= c_saf AT EVERY CELL WHERE THE PARENT PRINTS ONE
         (H2 of explore_flush_price.py). This is the one leg that tests
         this rig against a rig built on none of its machinery.
     (d) c_comp = 0 AT EVERY CELL WHERE THE DIGITWISE READER FITS
         (e_k = m d_k is admissible and exact, so no lookahead is owed).
  P1 c_ov OVER THE PUBLISHED GRID: for the six windows, x2..x5 and the
     six (s, s_0) pairs, the rig prints c_ov beside H3's bound and the
     digitwise bound, and the tally of c_ov - H3 over the cells where
     H3 gives one.
  P2 c_comp AT THE TWELVE CELLS THE PRICE WAS READ AT: the ten band
     cells and the two cells printing price 2 (V1 (1,1,1,2) x3 at
     s = s_0 = 3 and V2 (2,1,3,1) x3 at s = 5), each printed beside the
     frozen c_int and c_saf and the rounds the fixpoint took.
  P3 THE TRUE GAP, printed as c_int - c_comp per cell of P2, beside the
     flush price c_int - c_saf. This is what the aim asks for.
  P4 THE THIRD OUTCOME AS AN OBSERVABLE: a cell whose fixpoint neither
     stabilizes nor swallows an initial state within MAXROUND, or whose
     verdict differs between the inflated and deflated runs, prints
     "open" and is read as no finite decision AT THAT CELL. It is a
     finding, not a licence to raise MAXROUND until a number appears.

THE DESIGN
----------
EXACT, IN THE WINDOW'S OWN QUADRATIC FIELD. The first instrument was
floats with a tolerance and a two-margin re-run, and C1d printed RED
against it for a reason that is the object's and not the arithmetic's:
where the digitwise reader fits, the residual interval fills a member
EXACTLY, so the reader's winning placements are ISOLATED POINTS and no
tolerance can tell a genuine tie from a gap of 1e-12. Every quantity
here is therefore an element of Q(sqrt(Disc)), Disc the discriminant of
the window's own quadratic, carried as a pair of Fractions: alpha as the
root of that quadratic, the continued fraction tails by the exact
recursion r_{phi+1} = 1/r_phi - a_phi (which must close, r_P = r_0, and
is asserted to), and the cyclic recursions for the redundant ranges T_k,
their low endpoints, and the greedy tail sets A_i^(g) solved as LINEAR
SYSTEMS by elimination over that field rather than iterated to a
tolerance. The branch each A endpoint takes -- which digit attains the
min and which the max -- is read off a float pass and then VERIFIED
exactly against every other digit, so a wrong branch is a control
failure and not a silent number.

The game is then the reader's WINNING set as a GREATEST fixpoint of
CLOSED sets, which is what carries the ties: W starts as the whole
placement domain per (phase, flag) and a round replaces it by the union
over reader moves j of [j, j + span] intersected with the preimage,
under every legal adversary digit, of the next phase's W. Closed
intervals are closed under all of it, a degenerate [a, a] is a point
that survives, and the set only shrinks. A round that changes nothing is
a WIN with an invariant behind it; a round after which the seam admits
no (M, e_0) is a LOSS with an n-step adversary strategy behind it (the
set only shrinks, so a seam that fails never recovers); neither within
MAXROUND is P4's third outcome. P4's "margin" leg retires with the float
instrument -- there is no margin left to disagree about.

Stages: s0 the C1 controls, s1 the P1 grid of c_ov, s2 the P2/P3 game at
the eleven priced cells. Stage selection from the environment
(COMP_STAGES).
c_ov is the same machinery read one step earlier: the least c at which
every placement is coverable is the least c at which span >= 1 at every
(phase, flag), the members being spaced one unit apart, plus the seam at
level 0, where the integers step by 1 and T_0 has width 1 + E.

FINDINGS (entered post-run; every number below sits in this file's
printed output. One process under memwatch at the 512 MB default, 317 s,
peak WORKING SET 147.7 MB -- s3 builds the parent's own games beside this
rig's and is the whole of that figure; nothing ran bare, nothing killed.)

F1  THE CONTROLS HOLD, AND ONE OF THEM HAD TO BE REBUILT TWICE BEFORE IT
    COULD (C1a-C1e, 0 bad each). C1a is exact: the branch each greedy
    tail endpoint takes is verified against every other digit in
    Q(sqrt Disc), |A^(1)| is |theta_{i-1}| + |theta_i| exactly and W_k
    its own recursion exactly, and both endpoints BRACKET a brute-force
    enumeration inside the tail that enumeration truncates. C1e is the
    only leg that can catch a game printing wins that are not there, and
    it holds: at (s, s_0) = (0, 0) the rig prints no completion reader at
    any of 32 (window, map) cells, which is the corpus's own theorem
    ("dropping the rule alone buys nothing") in the killing direction.
F2  c_ov, THE OVERLAP BOUND WITH TRUE WIDTHS, BEATS THE CORPUS'S OWN
    (explore_redundant_ostrowski.py H3) AT 89 OF THE 120 GRID CELLS
    WHERE BOTH READ, by 2 at 30 and by 1 at 59, and is never above it.
    The whole of the gain is that bound's two estimates: 2m|theta_{t+c}|
    for the residual arc where the exact width is m(|theta_{t+c}| +
    |theta_{t+c+1}|), and a ratio test on |theta| where the exact
    quantity is the overlap itself.
F3  AND c_ov IS NOT THE COMPLETION READER'S MINIMUM. At 15 grid cells
    the digitwise reader fits, so c_comp is 0 there by construction --
    and c_ov reads 1 at nine of them and 2 at one (golden x2 at
    (s, s_0) = (1, 0)). So the every-placement reading overstates the
    reader by up to two units, and the witness is not exotic: it is the
    digitwise identity, where the residual arc fills its member EXACTLY
    and the reader's winning placements are isolated points that no
    condition quantified over all placements can see. The necessary side
    of the overlap bound is therefore NOT the overlap condition, which
    is what the aim asked and is a negative.
F4  THE GAP THE PRICE STANDS FOR, AT THE ELEVEN CELLS THE PRICE WAS READ
    AT (P2/P3; the slate said TWELVE and that is a miscount of this
    rig's own: the ten band cells and the two cells pricing 2 share
    V2 (2,1,3,1) x3 at s = 5, so eleven distinct cells, and the table
    has always had eleven rows). c_comp EQUALS c_saf at every one. Nine
    read c_comp = c_saf = 1 against c_int = 2, and two read
    c_comp = c_saf = 0 against c_int = 2. So the TRUE GAP is the flush
    price at all eleven: 1 at nine cells and 2 at two.
F5  AND OVER THE WHOLE GRID (s3): c_comp = c_saf at ALL 110 cells where
    both read, NEVER above and NEVER below, with 10 cells undecided.
    So the flush price is not an understatement anywhere it can be
    checked -- it is the gap.
F6  WHICH KILLS H2's ARGUMENT AND NOT ITS INEQUALITY (s4, and this
    is what the rest of this rig was built to reach).
    explore_flush_price.py H2 argues
    the direction "by one line": a box-confined safe strategy holds
    |real/theta| <= breal at every step, "which IS the completion
    reader's requirement". It is not. breal is the box of
    explore_limit_maps.py D9 widened by SLACK
    and a +1, and it is far wider than the level range a residual must
    sit in to be completable at all, so a branch can hold inside the box
    with its star out of range. s4 exhibits exactly that on the PARENT's
    own automaton in the parent's own coordinates: at sqrt3-1 [1,2] x3,
    (s, s_0) = (1, 0), a safety strategy at the parent's own c_saf = 2
    reaches a SAFE state with no completable branch at all in 300 of 300
    runs. At three control cells the same probe reaches none in 300. The
    branches read are the ones the box still CARRIES, and the reading
    would be the pruning's rather than safety's if the box could have
    pruned a completable branch -- so the stage prints the margin by
    which it cannot, breal over the completability reach, and it is
    10.10 at the witness and 16 to 26 at the controls.
    The inequality c_comp <= c_saf survives every cell this rig decides
    -- with equality at all 110 -- and it has no proof.
F7  WHAT THE INSTRUMENT COSTS, AS A SCOPE AND NOT AN APOLOGY. The two
    verdicts are certificates and neither assumes a lift: an EMPTY
    winning set is a loss from every placement, a FULL one plus the
    level-0 seam is a win from every placement, and the point game wins
    under one lift exhibited. What sits between them is undecided, and
    10 of the 120 grid cells sit there -- eight at (s, s_0) with
    s_0 < s or s_0 > s, two at (3, 3) for x5. They print "open" and are
    not read (P4). (SETTLED, explore_completion_lift.py: all ten decide
    under the mod-1 reading, each input taking its own lift, and every
    one reads c_comp = c_saf. Five of them were certificates this rig
    held and read as open -- an untruncated point-game loss is the
    exact reachable game's verdict, and play() discards it -- and five
    needed the wrap. The scope of this file's verdicts is unchanged;
    the ten are decided there.)

TIER. F2 and F3 are exhaustive computations at the cells named, exact in
Q(sqrt Disc) with no tolerance anywhere. F4 and F5 are OBSERVATIONS at
11 and 110 cells, each decided by a certificate; no mechanism is derived
for the equality and none is claimed -- that c_comp and c_saf agree
everywhere they are both read is a fact about 110 cells, not a law. F6
is a KILL of an argument and needs only its one witness; the inequality
it argued for is left standing as an observation with no proof under it.
The 10 undecided cells are stated as undecided and nothing is inferred
from where they fall.
"""

import os
import sys
import time
from fractions import Fraction
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_limit_maps import tail_caps                 # noqa: E402
from explore_limit_column import Window                  # noqa: E402
from explore_redundant_ostrowski import (                # noqa: E402
    GRID, WINDOWS, digitwise_bound, h3_bound)

STAGES = os.environ.get("COMP_STAGES", "s0,s1,s2,s3,s4").split(",")

MAXROUND = 40
COMPCAP = 6

# explore_flush_price.py F2 and F3, frozen here as the answer key:
# (window name, period, m, s, s_0, c_int, c_saf).
CELLS = [
    ("[4]", (4,), 2, 3, 3, 2, 1),
    ("[5]", (5,), 2, 3, 3, 2, 1),
    ("[5]", (5,), 2, 4, 4, 2, 1),
    ("bronze [3]", (3,), 3, 5, 5, 2, 1),
    ("V2 (2,1,3,1)", (2, 1, 3, 1), 3, 5, 5, 2, 0),
    ("[4]", (4,), 3, 5, 5, 2, 1),
    ("[5]", (5,), 3, 5, 5, 2, 1),
    ("[4]", (4,), 3, 7, 7, 2, 1),
    ("bronze [3]", (3,), 4, 8, 8, 2, 1),
    ("[5]", (5,), 3, 9, 9, 2, 1),
    ("V1 (1,1,1,2)", (1, 1, 1, 2), 3, 3, 3, 2, 0),
]


# --------------------------------------------------- Q(sqrt D), exactly

class QQ:
    """a + b sqrt(D), a and b rational, D a non-square positive integer."""

    __slots__ = ("a", "b", "D")

    def __init__(self, a, b, D):
        self.a, self.b, self.D = Fraction(a), Fraction(b), D

    def lift(self, o):
        return o if isinstance(o, QQ) else QQ(o, 0, self.D)

    def __add__(self, o):
        o = self.lift(o)
        return QQ(self.a + o.a, self.b + o.b, self.D)

    __radd__ = __add__

    def __neg__(self):
        return QQ(-self.a, -self.b, self.D)

    def __sub__(self, o):
        return self + (-self.lift(o))

    def __rsub__(self, o):
        return self.lift(o) + (-self)

    def __mul__(self, o):
        o = self.lift(o)
        return QQ(self.a * o.a + self.b * o.b * self.D,
                  self.a * o.b + self.b * o.a, self.D)

    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - self.b * self.b * self.D
        assert n != 0
        return QQ(self.a / n, -self.b / n, self.D)

    def __truediv__(self, o):
        return self * self.lift(o).inv()

    def sign(self):
        """Exact sign of a + b sqrt(D)."""
        if self.b == 0:
            return (self.a > 0) - (self.a < 0)
        if self.a == 0:
            return (self.b > 0) - (self.b < 0)
        sa = 1 if self.a > 0 else -1
        sb = 1 if self.b > 0 else -1
        if sa == sb:
            return sa
        c = self.a * self.a - self.b * self.b * self.D
        if c == 0:
            return 0
        return sa if c > 0 else sb

    def __lt__(self, o):
        return (self - self.lift(o)).sign() < 0

    def __le__(self, o):
        return (self - self.lift(o)).sign() <= 0

    def __gt__(self, o):
        return (self - self.lift(o)).sign() > 0

    def __ge__(self, o):
        return (self - self.lift(o)).sign() >= 0

    def __eq__(self, o):
        return (self - self.lift(o)).sign() == 0

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return hash((self.a, self.b))

    def __float__(self):
        return float(self.a) + float(self.b) * self.D ** 0.5

    def __repr__(self):
        return "%.12f" % float(self)


def solve_linear(n, rows):
    """Gaussian elimination over Q(sqrt D): rows are (coeffs, rhs)."""
    A = [list(co) + [r] for co, r in rows]
    Z = A[0][0].lift(0)
    for col in range(n):
        piv = next(i for i in range(col, len(A)) if A[i][col] != Z)
        A[col], A[piv] = A[piv], A[col]
        f = A[col][col].inv()
        A[col] = [v * f for v in A[col]]
        for i in range(len(A)):
            if i != col and A[i][col] != Z:
                g = A[i][col]
                A[i] = [v - g * w for v, w in zip(A[i], A[col])]
    return [A[i][n] for i in range(n)]


# ------------------------------------------------------------ intervals

def merge(iv):
    """Sorted, disjoint, degenerate points KEPT; exact throughout.

    The sort is on the QQ values themselves and not on their floats: two
    endpoints this game generates can agree to well past double
    precision -- that is exactly what a tie IS here -- and a float key
    that mis-orders such a pair silently breaks the disjointness every
    caller assumes.
    """
    iv = [(a, b) for a, b in iv if a <= b]
    if not iv:
        return []
    iv.sort(key=lambda ab: ab[0])
    out = [list(iv[0])]
    for a, b in iv[1:]:
        if a <= out[-1][1]:
            if b > out[-1][1]:
                out[-1][1] = b
        else:
            out.append([a, b])
    return [(a, b) for a, b in out]


def inter(u, v):
    """Intersection, degenerate points KEPT (a tie is a point, not empty)."""
    out = []
    i = j = 0
    while i < len(u) and j < len(v):
        a = u[i][0] if u[i][0] > v[j][0] else v[j][0]
        b = u[i][1] if u[i][1] < v[j][1] else v[j][1]
        if a <= b:
            out.append((a, b))
        if u[i][1] < v[j][1]:
            i += 1
        else:
            j += 1
    return out


def same(u, v):
    return (len(u) == len(v)
            and all(a == c and b == d for (a, b), (c, d) in zip(u, v)))


# --------------------------------------------------------------- frames

class Frames:
    """The ranges and the tail sets of one (window, s, s_0, m, c) cell.

    Lengths at level k are carried in units of |theta_k|, which makes
    each of them a function of the PHASE alone (H5). PP = lcm(P, 2) so
    that the sign of theta_k is (-1)^phase.
    """

    def __init__(self, period, s, s0, m, c):
        self.a = list(period)
        self.P = P = len(period)
        self.PP = PP = P * 2 // gcd(P, 2)
        self.s, self.s0, self.m, self.c = s, s0, m, c
        q = {-1: 0, 0: 1}
        pp = {-1: 1, 0: 0}
        for k in range(1, P + 1):
            q[k] = self.a[(k - 1) % P] * q[k - 1] + q[k - 2]
            pp[k] = self.a[(k - 1) % P] * pp[k - 1] + pp[k - 2]
        A2, A1, A0 = q[P - 1], q[P] - pp[P - 1], -pp[P]
        Disc = A1 * A1 - 4 * A2 * A0
        assert int(Disc ** 0.5 + 0.5) ** 2 != Disc, "window is rational"
        self.D = Disc
        self.Z, self.I = QQ(0, 0, Disc), QQ(1, 0, Disc)
        root = QQ(Fraction(-A1, 2 * A2), Fraction(1, 2 * A2), Disc)
        alt = QQ(Fraction(-A1, 2 * A2), Fraction(-1, 2 * A2), Disc)
        self.alpha = root if (self.Z < root and root < self.I) else alt
        assert self.Z < self.alpha and self.alpha < self.I
        r = [self.alpha]
        for phi in range(P):
            r.append(r[-1].inv() - self.a[phi])
        assert r[P] == r[0], "the tail recursion does not close"
        self.r = r[:P]
        top = PP + c + 6
        t = {-1: self.I}
        for k in range(0, top + 1):
            t[k] = t[k - 1] * self.r[k % P]
        self.t = t
        self.N = [self.a[phi % P] + s for phi in range(PP)]
        self._ranges()
        self._tails()
        self.N0 = self.a[0] - 1 + s0
        self.Wr0 = self.Wr[1 % PP] * self.r[1 % P] + self.N0
        self.LT0 = self.LT[1 % PP] * self.r[1 % P]
        self.Rc = []
        for phi in range(PP):
            v = self.I
            for j in range(1, c + 2):
                v = v * self.r[(phi + j) % P]
            self.Rc.append(v)

    def _ranges(self):
        """The two cyclic systems: T_k's width and its low endpoint."""
        PP, Z = self.PP, self.Z
        for name in ("Wr", "LT"):
            rows = []
            for phi in range(PP):
                co = [Z] * PP
                co[phi] = co[phi] + self.I
                nxt = (phi + 1) % PP
                co[nxt] = co[nxt] - self.r[(phi + 1) % self.P]
                if name == "Wr":
                    rhs = QQ(self.N[phi], 0, self.D)
                else:
                    rhs = QQ(0 if phi % 2 == 0 else -self.N[phi], 0, self.D)
                rows.append((co, rhs))
            setattr(self, name, solve_linear(PP, rows))

    def _tails(self):
        """A_i^(g): branch off a float pass, then solved exactly."""
        PP, P = self.PP, self.P
        rf = [float(x) for x in self.r]
        fL = [[0.0, 0.0] for _ in range(PP)]
        fH = [[0.0, 0.0] for _ in range(PP)]
        for _ in range(400):
            nL = [[0.0, 0.0] for _ in range(PP)]
            nH = [[0.0, 0.0] for _ in range(PP)]
            for phi in range(PP):
                sg = 1.0 if phi % 2 == 0 else -1.0
                rho, nxt = rf[(phi + 1) % P], (phi + 1) % PP
                for g in (0, 1):
                    xs = self.digits(phi, g)
                    nL[phi][g] = min(x * sg + rho * fL[nxt][1 if x == 0 else 0]
                                     for x in xs)
                    nH[phi][g] = max(x * sg + rho * fH[nxt][1 if x == 0 else 0]
                                     for x in xs)
            fL, fH = nL, nH
        pick = {}
        for phi in range(PP):
            sg = 1.0 if phi % 2 == 0 else -1.0
            rho, nxt = rf[(phi + 1) % P], (phi + 1) % PP
            for g in (0, 1):
                xs = self.digits(phi, g)
                def key(arr):
                    return lambda x: (x * sg
                                      + rho * arr[nxt][1 if x == 0 else 0])
                pick[("L", phi, g)] = min(xs, key=key(fL))
                pick[("H", phi, g)] = max(xs, key=key(fH))
        self.pick = pick
        idx = {(phi, g): 2 * phi + g for phi in range(PP) for g in (0, 1)}
        for tag in ("L", "H"):
            rows = []
            for phi in range(PP):
                sg = 1 if phi % 2 == 0 else -1
                rho, nxt = self.r[(phi + 1) % P], (phi + 1) % PP
                for g in (0, 1):
                    x = pick[(tag, phi, g)]
                    co = [self.Z] * (2 * PP)
                    co[idx[(phi, g)]] = co[idx[(phi, g)]] + self.I
                    j = idx[(nxt, 1 if x == 0 else 0)]
                    co[j] = co[j] - rho
                    rows.append((co, QQ(x * sg, 0, self.D)))
            sol = solve_linear(2 * PP, rows)
            setattr(self, "A" + tag,
                    [[sol[idx[(phi, g)]] for g in (0, 1)]
                     for phi in range(PP)])

    def verify_tails(self):
        """C1a, exactly: the picked digit really is the min and the max."""
        bad = 0
        for phi in range(self.PP):
            sg = 1 if phi % 2 == 0 else -1
            rho, nxt = self.r[(phi + 1) % self.P], (phi + 1) % self.PP
            for g in (0, 1):
                for tag, arr, cmp in (("L", self.AL, -1), ("H", self.AH, 1)):
                    got = arr[phi][g]
                    for x in self.digits(phi, g):
                        v = QQ(x * sg, 0, self.D) + \
                            rho * arr[nxt][1 if x == 0 else 0]
                        if (v < got if cmp < 0 else v > got):
                            bad += 1
                    x = self.pick[(tag, phi, g)]
                    v = QQ(x * sg, 0, self.D) + \
                        rho * arr[nxt][1 if x == 0 else 0]
                    if v != got:
                        bad += 1
        return bad

    def digits(self, phi, g):
        cap = self.a[phi % self.P]
        return list(range(cap + 1)) if g else list(range(cap))

    def width(self, phi, g):
        psi = (phi + self.c + 1) % self.PP
        return (self.AH[psi][g] - self.AL[psi][g]) * self.Rc[phi] * self.m

    def memwidth(self, phi):
        return self.Wr[(phi + 1) % self.PP] * self.r[(phi + 1) % self.P]

    def span(self, phi, g):
        return self.memwidth(phi) - self.width(phi, g)

    def offset(self, psi, g, x):
        sg = 1 if psi % 2 == 0 else -1
        rho = self.r[(psi + 1) % self.P]
        h = 1 if x == 0 else 0
        return (QQ(x * sg, 0, self.D) + rho * self.AL[(psi + 1) % self.PP][h]
                - self.AL[psi][g])

    def domain(self, phi, g):
        hi = self.Wr[phi] - self.width(phi, g)
        return [(self.Z, hi)] if hi >= self.Z else []

    def prefix_ok(self):
        """The level-0 seam, under a SINGLE integer lift -- a WIN route.

        The completion map is a map to the CIRCLE and the lift M is
        whatever the output makes it, so it may differ between inputs.
        Two readings therefore exist and neither is uniformly sharper.
        Under a SINGLE lift the whole picture is an interval one: the
        residual arc must sit inside T_0 for one M, which is
        |I_0| <= |T_0| - 1 = E -- the overlap bound's second half, with
        the true width rather than 2m|theta_c| -- and then it must fit a
        member, which
        is the ordinary span condition at level 0 under position 0's own
        caps a_1 - 1 + s_0 and a_1 - 1. From level 1 on it is the
        periodic game and nothing here is needed again. That reading is
        SUFFICIENT, which is all a win route has to be, and it is what
        c_ov is measured against.

        The mod-1 reading is the sharper question and it is not asked
        here: it lets each input take its own lift, at the price of a
        WRAP -- while |T_t| >= 1 the level range's own two ends are
        identified and the members cover the circle with a seam overlap
        of |T_t| - 1, so an arc longer than that fits nowhere. It buys
        wins the single-lift reading misses and it costs conditions the
        single-lift reading does not owe. What matters for this rig is
        that the LOSS route needs neither: an empty winning set is a
        loss from every placement under every lift.
        """
        psi = (self.c + 1) % self.PP
        w0 = ((self.AH[psi][1] - self.AL[psi][1]) * self.t[self.c + 1]
              * self.m / self.t[0])
        return (self.Wr[1 % self.PP] * self.r[1 % self.P] - w0 >= self.I
                and w0 * self.t[0] <= self.Wr0 * self.t[0] - self.I)

# ----------------------------------------------------------------- c_ov

def c_ov(period, s, s0, m, cap=COMPCAP):
    """The least c at which EVERY placement is coverable, seam included."""
    for c in range(cap + 1):
        F = Frames(period, s, s0, m, c)
        if (all(F.span(phi, g) >= F.I
                for phi in range(F.PP) for g in (0, 1))
                and F.prefix_ok()):
            return c
    return None


# ------------------------------------------------------------- the game

def pre_reads(F):
    """Every legal d_0..d_c, with the value prefix and the trailing flag."""
    out = [([], F.Z, True)]
    for k in range(F.c + 1):
        nxt = []
        for ds, val, pzd in out:
            cap = F.a[0] - 1 if k == 0 else F.a[k % F.P]
            xs = range(cap + 1) if (k == 0 or pzd) else range(cap)
            sg = 1 if k % 2 == 0 else -1
            for x in xs:
                nxt.append((ds + [x], val + F.t[k] * (x * sg), x == 0))
        out = nxt
    return out


def point_game(F, cap=20000):
    """A WIN certificate that survives a fixpoint which never closes.

    The greatest fixpoint of a safety game on a continuum need not be
    reached at any finite round: it can fragment forever while the
    reader wins throughout, and the digitwise cells are exactly that --
    there the residual fills its member EXACTLY, the reader's winning
    placements are ISOLATED POINTS, and a descending sequence of
    interval unions grinds toward them without ever arriving. What
    certifies a win instead is an INVARIANT, and the placements
    themselves supply one: close the reachable points forward from the
    seam under EVERY reader move and every adversary digit, and if that
    closure is finite, solve the finite game on it. A win there is a win
    in the real game -- the strategy it exhibits is a strategy -- and a
    loss there is no verdict at all, the closure being an
    under-approximation and a truncated node counted as lost.
    """
    succ = {}

    def edges(phi, g, u):
        sp = F.span(phi, g)
        if sp < F.Z:
            return []
        rho = F.r[(phi + 1) % F.P]
        psi = (phi + F.c + 1) % F.PP
        out = []
        for j in range(F.N[phi] + 1):
            jj = QQ(j, 0, F.D)
            if u < jj or u > jj + sp:
                continue
            kids = []
            for x in F.digits(psi, g):
                h = 1 if x == 0 else 0
                K = F.offset(psi, g, x) * F.Rc[phi] * F.m
                kids.append(((phi + 1) % F.PP, h, (u - jj + K) / rho))
            out.append(kids)
        return out

    psi = (F.c + 1) % F.PP
    span0 = F.Wr[1 % F.PP] * F.r[1 % F.P]
    rho = F.r[1 % F.P]
    lo0 = F.LT0 * F.t[0]
    roots = []
    for _ds, val, pzd in pre_reads(F):
        g = 1 if pzd else 0
        w0 = (F.AH[psi][g] - F.AL[psi][g]) * F.t[F.c + 1] * F.m / F.t[0]
        left = (val * F.m + F.AL[psi][g] * F.t[F.c + 1] * F.m - lo0) / F.t[0]
        opts = []
        for M in range(-4 * F.m - 4, 4 * F.m + 5):
            u0 = left - QQ(M, 0, F.D) / F.t[0]
            if u0 < F.Z or u0 + w0 > F.Wr0:
                continue
            for j in range(F.N0 + 1):
                jj = QQ(j, 0, F.D)
                if u0 < jj or u0 + w0 > jj + span0:
                    continue
                kids = []
                for x in F.digits(psi, g):
                    h = 1 if x == 0 else 0
                    K = F.offset(psi, g, x) * F.t[F.c + 1] * F.m / F.t[0]
                    kids.append((1 % F.PP, h, (u0 - jj + K) / rho))
                opts.append(kids)
        if not opts:
            return False, 0
        roots.append(opts)
    frontier = [k for opts in roots for kids in opts for k in kids]
    dropped = set()
    while frontier:
        st = frontier.pop()
        if st in succ or st in dropped:
            continue
        if len(succ) >= cap:
            dropped.add(st)
            continue
        succ[st] = edges(*st)
        for kids in succ[st]:
            frontier.extend(kids)
    W = set(succ)
    changed = True
    while changed:
        changed = False
        for st in list(W):
            if not any(all(k in W for k in kids) for kids in succ[st]):
                W.discard(st)
                changed = True
    ok = all(any(all(k in W for k in kids) for kids in opts)
             for opts in roots)
    return ok, len(succ)


def step(F, W):
    """One round of the reader's winning set."""
    nxt = {}
    for phi in range(F.PP):
        rho = F.r[(phi + 1) % F.P]
        psi = (phi + F.c + 1) % F.PP
        for g in (0, 1):
            sp = F.span(phi, g)
            got = []
            if sp >= F.Z:
                for j in range(F.N[phi] + 1):
                    jj = QQ(j, 0, F.D)
                    here = [(jj, jj + sp)]
                    for x in F.digits(psi, g):
                        h = 1 if x == 0 else 0
                        K = F.offset(psi, g, x) * F.Rc[phi] * F.m
                        pre = [(rho * p - K + jj, rho * q - K + jj)
                               for p, q in W[((phi + 1) % F.PP, h)]]
                        here = inter(here, merge(pre))
                        if not here:
                            break
                    got.extend(here)
            nxt[(phi, g)] = merge(got)
    return nxt


def gfp(F, icap=4000):
    """The greatest fixpoint of the winning set, with NO seam in it.

    Two of its readings are unconditional, and they are the only ones
    this rig reads as verdicts. EMPTY at every (phase, flag) is a LOSS
    from every placement whatever the prefix did and whatever lift the
    coding takes. The FULL DOMAIN at every one of them is a WIN from
    every placement, so a prefix that arrives anywhere at all arrives
    winning -- and that reading is exactly c_ov's span condition.
    """
    W = {(phi, g): F.domain(phi, g)
         for phi in range(F.PP) for g in (0, 1)}
    for rnd in range(1, MAXROUND + 1):
        nxt = step(F, W)
        if all(same(nxt[k], W[k]) for k in W):
            return nxt, rnd, True
        W = nxt
        if sum(len(v) for v in W.values()) > icap:
            return W, rnd, False
    return W, MAXROUND, False


def play(F):
    """(verdict, size): the reader's minimum, on unconditional certificates.

    WIN, two routes, both sound: every placement winning and the level-0
    arc fitting a member (c_ov's condition, no lift assumed anywhere), or
    the point game finding a strategy under ONE lift -- a win under a
    fixed M is a win. LOSS, one route and no lift in it either: the
    seam-free winning set empty at every phase, so there is nowhere to
    arrive. Anything else is P4's third outcome and prints "open".
    """
    W, rnd, stable = gfp(F)
    if stable and not any(W.values()):
        return False, 0
    if (stable and all(same(W[(phi, g)], F.domain(phi, g))
                       for phi in range(F.PP) for g in (0, 1))
            and F.prefix_ok()):
        return True, rnd
    won, n = point_game(F)
    if won:
        return True, n
    return None, n


def c_comp(period, s, s0, m, cap=COMPCAP):
    """(c, nodes, note): the completion reader's own minimum lookahead."""
    tot = 0
    for c in range(cap + 1):
        F = Frames(period, s, s0, m, c)
        won, n = play(F)
        tot = max(tot, n)
        if won is None:
            return None, tot, "open"
        if won:
            return c, tot, ""
    return None, tot, "cap"


# ------------------------------------------------------------- controls

def brute(period, i, g):
    """min and max of legal tails from index i, by enumeration.

    Truncated at a depth the alphabet can afford, so the enumeration
    reaches the extremes only to within the tail it drops -- and that
    tail is returned as the tolerance rather than guessed at: what is
    dropped from index i + depth is at most |theta_{i+depth-1}| +
    |theta_{i+depth}|. The check the tolerance leaves standing is
    two-sided and directional: the exact endpoint must BRACKET the
    enumeration and sit inside its own truncation window.
    """
    P = len(period)
    depth = max(5, min(12, int(20.0 / max(period).bit_length())))
    r = [0.5] * P
    for _ in range(400):
        r = [1.0 / (period[phi] + r[(phi + 1) % P]) for phi in range(P)]
    t = {i - 1: 1.0}
    for k in range(i, i + depth + 1):
        t[k] = t[k - 1] * r[k % P]
    best = [None, None]

    def walk(k, val, pzd):
        if k == i + depth:
            if best[0] is None or val < best[0]:
                best[0] = val
            if best[1] is None or val > best[1]:
                best[1] = val
            return
        cap = period[k % P]
        xs = range(cap + 1) if pzd else range(cap)
        sg = 1.0 if k % 2 == 0 else -1.0
        for x in xs:
            walk(k + 1, val + x * sg * t[k], x == 0)

    walk(i, 0.0, bool(g))
    tol = (t[i + depth - 1] + t[i + depth]) / t[i]
    return best[0] / t[i], best[1] / t[i], tol


ALLW = WINDOWS + [("[4]", (4,)), ("[5]", (5,))]


def s0_controls():
    print("== s0  C1a: the interval machinery, exactly and against brute")
    bad = 0
    for name, period in ALLW:
        F = Frames(period, 1, 1, 2, 1)
        bad += F.verify_tails()
        for phi in range(F.PP):
            for g in (0, 1):
                lo, hi, tol = brute(list(period), phi + 2 * F.PP, g)
                fl, fh = float(F.AL[phi][g]), float(F.AH[phi][g])
                if not (lo + 1e-12 >= fl >= lo - tol
                        and hi - 1e-12 <= fh <= hi + tol):
                    print("    BAD A %s phi=%d g=%d: exact (%.12f, %.12f) "
                          "brute (%.12f, %.12f) tol %.2e"
                          % (name, phi, g, fl, fh, lo, hi, tol))
                    bad += 1
            if F.AH[phi][1] - F.AL[phi][1] != F.r[phi % F.P].inv() + F.I:
                print("    BAD |A| %s phi=%d" % (name, phi))
                bad += 1
        for s in (1, 3):
            G = Frames(period, s, s, 2, 1)
            for phi in range(G.PP):
                want = (QQ(G.N[phi], 0, G.D)
                        + G.Wr[(phi + 1) % G.PP] * G.r[(phi + 1) % G.P])
                if G.Wr[phi] != want:
                    print("    BAD W %s s=%d phi=%d" % (name, s, phi))
                    bad += 1
    print("  control C1a: %d bad" % bad)
    return bad


def s0b_controls():
    print("== s0  C1b/C1d: c_comp <= c_ov, and 0 where digitwise fits")
    bad = 0
    for name, period in ALLW:
        win = Window(tail_caps(period), len(period))
        for m in (2, 3):
            for s, s_0 in GRID:
                if s_0 > s + 1:
                    continue
                ov = c_ov(period, s, s_0, m)
                cc, _r, note = c_comp(period, s, s_0, m)
                if cc is not None and ov is not None and cc > ov:
                    print("    BAD c_comp > c_ov %s x%d (%d,%d): %s > %s"
                          % (name, m, s, s_0, cc, ov))
                    bad += 1
                if digitwise_bound(win, m, s, s_0) == 0 and cc != 0:
                    print("    BAD digitwise cell not 0: %s x%d (%d,%d): %s %s"
                          % (name, m, s, s_0, cc, note))
                    bad += 1
    print("  control C1b/C1d: %d bad" % bad)
    return bad


def s0c_control():
    """C1c: c_comp <= c_saf at the eleven cells the parent priced.

    The one leg that tests this rig against a rig built on none of its
    machinery -- explore_flush_price.py's c_saf comes off a finite state
    space inside a derived box, this rig's c_comp off an interval game
    with neither, and H2 there says the first must bound the second.

    IT HOLDS AT THESE ELEVEN AND IT IS NOT A LAW. Widened to the whole
    grid (s3) it FAILS at two cells, and the failure is H2's and not
    this rig's: H2 argues that a box-confined safe strategy meets the
    completion reader's whole requirement, where that box is
    explore_limit_maps.py D9's widened by SLACK and a +1 and is far
    WIDER than the level range a
    residual has to sit in to be completable at all. A branch can hold
    inside the box with its star outside the range, so safety does not
    imply completability and the inequality has no proof. s4 witnesses
    exactly that, directly, on the parent's own automaton. The leg
    therefore stays as a control over the eleven cells the parent's own
    claim was read at, and the grid is where it is reported rather than
    gated.
    """
    print("== s0  C1c: c_comp <= c_saf at the eleven cells the "
          "parent's own claim was read at")
    bad = 0
    for name, period, m, s, s_0, _c_int, c_saf in CELLS:
        cc, _n, note = c_comp(period, s, s_0, m)
        if cc is None or cc > c_saf:
            print("    BAD c_comp vs c_saf %s x%d s=%d: %s%s > %d"
                  % (name, m, s, cc, (" (%s)" % note) if note else "", c_saf))
            bad += 1
    print("  control C1c: %d bad" % bad)
    return bad


def s0e_control():
    """C1e, ADDED IN THE AUDIT: no completion reader at zero excess.

    Every leg above is an inequality or an agreement, and none of them
    can catch a game that is too GENEROUS -- one printing wins that are
    not there would still satisfy c_comp <= c_saf and would still read 0
    where the digitwise reader fits. The (s, s_0) = (0, 0) column is the
    one place the corpus already knows the answer in the KILLING
    direction: at EXCESS = 0 the tear survives at the legal address for
    every reader, the completion reader included (the parent's H2 --
    dropping the rule alone buys nothing), so any lookahead printed
    there is a rig fault and not a finding.
    """
    print("== s0  C1e: the (0, 0) column must print NO completion reader")
    bad = 0
    for name, period in ALLW:
        for m in (2, 3, 4, 5):
            cc, _n, note = c_comp(period, 0, 0, m)
            if cc is not None:
                print("    BAD a reader at zero excess: %s x%d: %s %s"
                      % (name, m, cc, note))
                bad += 1
    print("  control C1e: %d bad" % bad)
    return bad


# --------------------------------------------------------------- stages

def s1_grid():
    print("== s1  P1: c_ov over the grid, beside the overlap and "
          "digitwise bounds")
    tally = {}
    for name, period in WINDOWS:
        win = Window(tail_caps(period), len(period))
        for m in (2, 3, 4, 5):
            row = []
            for s, s_0 in GRID:
                ov = c_ov(period, s, s_0, m)
                hb = h3_bound(win, m, s, s_0)
                db = digitwise_bound(win, m, s, s_0)
                row.append("%s/%s/%s" % ("-" if ov is None else ov,
                                         "-" if hb is None else hb,
                                         "-" if db is None else db))
                if ov is not None and hb is not None:
                    tally[ov - hb] = tally.get(ov - hb, 0) + 1
            print("  %-14s x%d  %s" % (name, m, "  ".join(row)))
    print("  c_ov/overlap/digitwise per cell; c_ov - overlap where "
          "both:")
    for d in sorted(tally):
        print("    %+d: %d cells" % (d, tally[d]))


def s2_cells():
    print("== s2  P2/P3: the game at the eleven priced cells")
    for name, period, m, s, s_0, c_int, c_saf in CELLS:
        t0 = time.time()
        ov = c_ov(period, s, s_0, m)
        cc, rnd, note = c_comp(period, s, s_0, m)
        print("  %-14s x%d s=%-2d  c_int %d  c_saf %d  c_ov %s  c_comp %s%s"
              "  flush %d  TRUE GAP %s  nodes %d  %.0f s"
              % (name, m, s, c_int, c_saf, "-" if ov is None else ov,
                 "-" if cc is None else cc, (" (%s)" % note) if note else "",
                 c_int - c_saf, "-" if cc is None else str(c_int - cc),
                 rnd, time.time() - t0))


def s3_grid_gap():
    """P3 over the whole grid, ADDED IN THE AUDIT.

    s2 reads the gap at eleven cells, which is a reading about the band
    and about the two cells that priced 2 -- not about the grid the
    price was tallied over. This stage runs c_comp at all 144 grid cells
    and the parent's own c_saf beside it, so the question "does the
    completion reader ever read BELOW the safety reader" is asked of the
    whole population rather than of the eleven cells s2 names.
    """
    from explore_flush_price import price                # noqa: E402
    print("== s3  P3 over the published grid: c_comp against c_saf")
    tally = {}
    below, above = [], []
    for name, period in WINDOWS:
        win = Window(tail_caps(period), len(period))
        for m in (2, 3, 4, 5):
            row = []
            for s, s_0 in GRID:
                cc, _n, note = c_comp(period, s, s_0, m)
                c_int, c_saf, _st = price(win, m, s, s_0)
                row.append("%s/%s" % ("-" if cc is None else cc,
                                      "-" if c_saf is None else c_saf))
                if cc is not None and c_int is not None and cc > c_int:
                    # C1f: an INTEGER reader is a completion reader at the
                    # same lookahead -- its output codes the residual, so
                    # the star is in range at every level. c_comp > c_int
                    # is impossible and is what caught this rig forcing a
                    # single integer lift M at the seam.
                    print("    BAD c_comp > c_int: %s x%d (%d,%d): %d > %d"
                          % (name, m, s, s_0, cc, c_int))
                if cc is not None and c_saf is not None:
                    tally[c_saf - cc] = tally.get(c_saf - cc, 0) + 1
                    if cc < c_saf:
                        below.append((name, m, s, s_0, cc, c_saf, c_int))
                    if cc > c_saf:
                        above.append((name, m, s, s_0, cc, c_saf, c_int))
                elif cc is None and c_saf is not None:
                    print("    UNDECIDED c_comp where c_saf reads: %s x%d "
                          "(%d,%d) %s" % (name, m, s, s_0, note))
            print("  %-14s x%d  %s" % (name, m, "  ".join(row)))
    print("  c_comp/c_saf per cell; c_saf - c_comp over the cells where "
          "both read:")
    for dd in sorted(tally):
        print("    %+d: %d cells" % (dd, tally[dd]))
    print("  where the completion reader reads BELOW the safety reader:")
    for name, m, s, s_0, cc, cs, ci in below:
        print("    %-14s x%d (%d,%d)  c_comp %d  c_saf %d  c_int %s"
              % (name, m, s, s_0, cc, cs, "-" if ci is None else ci))
    if not below:
        print("    none")
    print("  and where it reads ABOVE it -- H2's inequality, refuted:")
    for name, m, s, s_0, cc, cs, ci in above:
        print("    %-14s x%d (%d,%d)  c_comp %d  c_saf %d  c_int %s"
              % (name, m, s, s_0, cc, cs, "-" if ci is None else ci))
    if not above:
        print("    none")


def s4_witness(cells, trials=300, steps=80, seed=11):
    """P5, ADDED IN THE AUDIT: is a SAFE branch set ever uncompletable?

    s3 reports two cells where the completion reader needs MORE
    lookahead than the safety reader, which contradicts H2 of
    explore_flush_price.py -- so one of the two rigs is wrong and no
    amount of this rig's own machinery can say which. This stage asks
    the question on the PARENT's automaton and in the parent's own
    coordinates, with none of this rig's game in it: run a safety
    strategy at the parent's own c_saf and ask, at every step, whether
    ANY alive branch's residual interval still fits inside the level
    range. A step where none does is a safe state that cannot be
    completed, and settles the direction without appeal.

    In signed units of theta_phi every ratio is P-periodic (the frame's
    H sends theta_k to theta_{k+P}), so no parity phase is needed here:
    T_phi/theta_phi and A_phi^(g)/theta_phi are read off their own
    recursions with kappa_phi = theta_{phi+1}/theta_phi < 0.

    AND THE BRANCHES READ ARE THE ONES THE BOX STILL CARRIES, which is
    the hole this probe would otherwise have: a branch the box PRUNED
    could have been completable, and then "no completable branch" would
    be a fact about the pruning and not about safety. It cannot be, and
    the rig prints the check rather than asserting it. A pruned branch
    has |real/theta_phi| > breal; for it to be completable its residual
    -real/theta_phi + m A/theta_phi would have to sit inside
    [TL_phi, TH_phi], which needs |real/theta_phi| <= max(|TL|, |TH|) +
    m max|A/theta_phi|. So the probe is blind to nothing as long as
    breal exceeds that bound at every phase, and the margin is printed.
    """
    import random
    from explore_redundant_ostrowski import Game
    from explore_flush_price import window_of
    print("== s4  P5: does a SAFE branch set ever fail to be completable?")
    for name, period, m, s, s_0, look in cells:
        P = len(period)
        rf = [0.5] * P
        for _ in range(400):
            rf = [1.0 / (period[phi] + rf[(phi + 1) % P]) for phi in range(P)]
        kap = [-rf[(phi + 1) % P] for phi in range(P)]
        N = [period[phi] + s for phi in range(P)]
        TL, TH = [0.0] * P, [1.0] * P
        for _ in range(400):
            TL, TH = ([kap[phi] * TH[(phi + 1) % P] for phi in range(P)],
                      [N[phi] + kap[phi] * TL[(phi + 1) % P]
                       for phi in range(P)])

        def digs(phi, g):
            return (range(period[phi] + 1) if g else range(period[phi]))

        AL = [[0.0, 0.0] for _ in range(P)]
        AH = [[0.0, 0.0] for _ in range(P)]
        for _ in range(400):
            nAL = [[0.0, 0.0] for _ in range(P)]
            nAH = [[0.0, 0.0] for _ in range(P)]
            for phi in range(P):
                for g in (0, 1):
                    nAL[phi][g] = min(
                        x + kap[phi] * AH[(phi + 1) % P][1 if x == 0 else 0]
                        for x in digs(phi, g))
                    nAH[phi][g] = max(
                        x + kap[phi] * AL[(phi + 1) % P][1 if x == 0 else 0]
                        for x in digs(phi, g))
            AL, AH = nAL, nAH
        ratio = []
        for phi in range(P):
            v = 1.0
            for j in range(1, look + 2):
                v *= kap[(phi + j) % P]
            ratio.append(v)
        win = window_of(period)
        g = Game(win, 1, m, (0,), look, s, s_0)
        W = set(i for i in g.trans if g.alive[i])
        ch = True
        while ch:
            ch = False
            for st in list(W):
                if not any(all(s2 in W for _x, s2 in succ)
                           for succ in g.trans[st].values()):
                    W.discard(st)
                    ch = True
        if not all(i in W for i in g.init):
            print("  %-14s x%d (%d,%d) c=%d: SAFETY LOSES -- not a witness"
                  % (name, m, s, s_0, look))
            continue
        slack = None
        for phi in range(P):
            psi = (phi + look + 1) % P
            reach = max(abs(TL[phi]), abs(TH[phi])) + m * max(
                abs(AL[psi][gg] * ratio[phi]) for gg in (0, 1))
            room = g.breal[phi] - reach
            slack = room if slack is None else min(slack, room)
        if slack <= 0:
            print("  %-14s x%d (%d,%d) c=%d: BOX TOO TIGHT to read (%.3f)"
                  % (name, m, s, s_0, look, slack))
            continue
        random.seed(seed)
        nofit, first = 0, None
        for _ in range(trials):
            cur = random.choice(g.init)
            for t in range(steps):
                pos, br, pzd, _pze = g.states[cur]
                phi = pos % P
                psi = (phi + look + 1) % P
                gg = 1 if pzd else 0
                fit = False
                for (u, w) in br:
                    rr = win.real(u, w) / g.thf[phi]
                    a = -rr + m * AL[psi][gg] * ratio[phi]
                    b = -rr + m * AH[psi][gg] * ratio[phi]
                    if b < a:
                        a, b = b, a
                    if TL[phi] - 1e-12 <= a and b <= TH[phi] + 1e-12:
                        fit = True
                        break
                if not fit:
                    nofit += 1
                    first = first or (t, pos, len(br))
                    break
                ys = [y for y, succ in g.trans[cur].items()
                      if all(s2 in W for _x, s2 in succ)]
                cur = random.choice(g.trans[cur][ys[0]])[1]
        print("  %-14s x%d (%d,%d) c=%d  safe |W| %d  box margin over "
              "completability %.2f  runs reaching a SAFE state with no "
              "completable branch: %d/%d  first %s"
              % (name, m, s, s_0, look, len(W), slack, nofit, trials, first))


def main():
    t0 = time.time()
    if "s0" in STAGES:
        if (s0_controls() or s0b_controls() or s0c_control()
                or s0e_control()):
            print("CONTROL RED -- nothing below is read")
            return
    if "s1" in STAGES:
        s1_grid()
    if "s2" in STAGES:
        s2_cells()
    if "s3" in STAGES:
        s3_grid_gap()
    if "s4" in STAGES:
        s4_witness([("golden [1]", (1,), 5, 1, 0, 3),
                    ("sqrt3-1 [1,2]", (1, 2), 3, 1, 0, 2),
                    ("bronze [3]", (3,), 3, 1, 1, 2),
                    ("[4]", (4,), 2, 3, 3, 1)])
    print("total %.0f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
