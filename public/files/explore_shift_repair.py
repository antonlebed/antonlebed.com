"""What decides a REPAIRING cell: the shift's legality repair, and
whether its cascade imports information from ABOVE the digit it lands
on.

THE QUESTION
------------
At a trailing Ostrowski window alpha = [0; a_1, a_2, ...] with weights
q_0 = 1, q_1 = a_1, q_k = a_k q_{k-1} + q_{k-2}, the stride-r shift
L_r sends n = sum b_k q_k to sum b_k q_{k+r}. The shifted digit string
is legal outright wherever the quotient sequence is NON-DECREASING
along stride r (b'_{k+r} = b_k needs b_k <= a_{k+r+1}, and legality
gave only b_k <= a_{k+1}), and there L_r is the bare coordinate map
and reads at delay 0. That sufficient half is settled
(explore_nonquadratic_window.py E9).

Its converse is FALSE, and what is left open is the REPAIRING cells:
those whose shifted string IS illegal, needs renormalization, and
reads at bounded delay anyway. Measured cells split both ways with no
known discriminator -- at e - 2 strides 1, 2 and 4 repair the
IDENTICAL 99390 of 100000 inputs while stride 2 reads at delay 0 at
every depth and strides 1 and 4 are gated. This rig asks what on
(quotient sequence, stride) decides that.

TWO CANDIDATES ARE DEAD ON PAPER AND OWE NO ENGINE, and they are set
down because both are what a reader supplies first.

ABSORPTION DEPTH. Chaining a_{j+1} q_j = q_{j+1} - q_{j-1} with
q_j = a_j q_{j-1} + q_{j-2} gives
(a_{j+1} + 1) q_j = q_{j+1} + (a_j - 1) q_{j-1} + q_{j-2}: one
overflow at j carries 1 up and lands at TWO positions below, a_j - 1
at j-1 and 1 at j-2, absorbed only if BOTH land legally, and either
prong failing repeats the rewrite one position down. Both conditions
read the INPUT digits, so the descent length is not an (a, r)
quantity at all.

TAIL MAGNITUDE. With D_k = q_k alpha - p_k, the recurrence gives
|D_{k-1}| = a_{k+1}|D_k| + |D_{k+1}|, which telescopes to
|D_{K-1}| = sum_{j >= K} a_{j+1}|D_j|. An input known to depth K has
image tail sum_{k >= K} b_k D_{k+r}, and since b_k <= a_{k+1} and
|D_{k+r}| <= |D_k| for r >= 0,
  |image tail| <= sum_{k >= K} a_{k+1}|D_{k+r}|
              <= sum_{k >= K} a_{k+1}|D_k| = |D_{K-1}|.
The image cell at depth t = K - c has scale |D_{t-1}| = |D_{K-c-1}|,
which is >= |D_{K-1}| for every c >= 0, with the slack growing in c.
So the image tail never exceeds the image cell's own scale, at any
stride and any window -- magnitude is never the gate, and no
inequality here needed the quotient sequence to do anything. What that
leaves is the only other way an ultrametric cell can be missed -- the
image landing on the far side of a cell BOUNDARY -- and a boundary is
crossed by the CASCADE, not by the size of the perturbation.

THE HAND-ATTACK (pre-engine, on paper). Normalizing an overflowing
digit at image position p uses q_{p+1} = a_{p+1} q_p + q_{p-1}: the
overflow carries ONE UNIT UP to position p+1 and injects a DOWN-CHARGE
at p-1. The down-charge is the half the two dead candidates were
reading, and it is input-dependent. The UP-CARRY is not: it lands on
position p+1, whose cap is a_{p+2}, and that cap is a function of the
quotient sequence and the stride alone. If a_{p+2} = 1 the up-carry
has no room -- the position it lands on is already at its cap for any
input holding a nonzero digit there -- and the rewrite fires AGAIN one
position up, whose own down-charge is injected one position higher,
and the event stops being local. If a_{p+2} >= 2 the up-carry has a
seat and the event terminates where it landed. So the candidate is the
cap ABOVE the landing site, and the object it decides is exactly the
open question's phrasing: whether the repair chains, and hence whether
what reaches the low digits was decided above them.

THE VOCABULARY (fixed before any engine; every quantity below is a
function of (a, r) and of nothing else -- no enumeration of n enters
it, which is what makes it a criterion rather than a summary).
  DROP SITE. Position j is a drop site for stride r when
      a_{j+1} > a_{j+r+1}
  -- the cap at input position j exceeds the cap at its image
  position j + r. The shifted string can be illegal at position
  j + r and nowhere else.
  LANDING SITE. The overflow at drop site j is rewritten at image
  position p = j + r and carries up to p + 1 = j + r + 1.
  LANDING HEADROOM. h(j, r) = a_{j+r+2}, the digit cap at the
  landing site.
  CHAIN SITE. A drop site with h(j, r) = 1.

THE HEADROOM CRITERION (frozen, and it is what this rig is here to
kill). A (window, stride) cell
  READS AT DELAY 0     when it has no drop site;
  READS AT BOUNDED DELAY when it has drop sites but no chain site, or
      only chain sites confined below some position;
  IS GATED           when chain sites recur without bound.
Its operational form, since a measurement reads a finite table: the
criterion predicts c_min(t) = 0 at every depth t below the lowest
chain site's landing and at every depth above the highest, and
predicts a gated (cap-shaped) column exactly where chain sites reach
the top of the readable range.

PREDICTIONS, FIXED BEFORE THE RUN (as observables -- the rig prints
c_min(f, t) = least c <= C_MAX with input agreement depth >= t + c
forcing image agreement depth >= t, or an UNREADABLE flag)
  P1 (positive control) f = id: c_min = 0 at every t, every window;
      digits reconstruct exactly and satisfy legality everywhere.
  P2 (calibration) the stride sweep at r = 1..4, N = 100000
      reproduces explore_nonquadratic_window.py's E9 rows -- W0 and
      W3 zero repairs and c_min 0 throughout; W1 repairs
      99390/87743/95040/97465 with strides 1 and 3 gated; W2 repairs
      99390/99390/0/99390 with strides 1 and 4 gated and stride 2 at
      delay 0. KILL: any disagreement -- the digit path differs from
      the parent's and nothing below is comparable.
  P3 (the criterion at e - 2, hand-derived to a closed form BEFORE
      the run, which is what makes the new cells predictions and not
      a fit). At e - 2 the quotients are a_k = 1 except
      a_{3m+2} = 2m + 2, so the big caps sit at positions
      j = 1 mod 3. A drop site needs a_{j+1} big and a_{j+r+1} not,
      which is j = 1 mod 3 and r != 0 mod 3; and its headroom
      a_{j+r+2} is big exactly when r = 2 mod 3. Hence
        r = 0 mod 3 -> no drop site   -> delay 0
        r = 2 mod 3 -> no chain site  -> bounded delay
        r = 1 mod 3 -> every drop site is a chain site -> GATED.
      The four measured strides agree (1 gated, 2 bounded, 3 no
      repair, 4 gated). The four UNMEASURED ones are the prediction:
      r = 5 BOUNDED, r = 6 NO REPAIR at delay 0, r = 7 GATED,
      r = 8 BOUNDED. KILL: any one of the four measured otherwise.
  P4 (the criterion elsewhere) at every (window, stride) cell the
      criterion's verdict, computed from the quotient sequence alone,
      equals the measured verdict. KILL: a disagreement. The cubic is
      where this is at risk and the risk is named: its chain sites
      are SPARSE rather than absent at strides 2 and 4, so the
      criterion predicts those cells are gated by events sitting
      ABOVE the depth an enumeration to N = 100000 can reach, and the
      recorded reading of them as bounded would then be a data-cap
      artifact. E4 is what separates those.
  P5 (the delay-0 floor) c_min(t) = 0 at every t at or below the
      lowest chain site's landing position, every cell. KILL: a
      nonzero c_min below that floor -- the criterion would then be
      locating the onset wrongly even where it gets the verdict
      right.
  P6 (range stability, and it is a claim the corpus already makes
      with no range scan behind it) the cubic's stride-2 and stride-4
      cells are recorded as Lipschitz with a LOCAL constant attained
      at one depth and 0 elsewhere, stable across every range, while
      the sweep that measured them ran at a single N. Frozen: if
      those constants are genuinely local they do not move as N goes
      30000 -> 100000 -> 300000. KILL: a local constant growing with
      N, which makes the bounded verdict a cap artifact and P4's
      named risk the true reading.
  P7 (the designed family) at the window [0; (1^{P-1}, A)^inf] --
      period P, one quotient A >= 2 per period, every other 1 -- the
      criterion's arithmetic closes: drop sites are the positions
      j = -1 mod P and exist iff r != 0 mod P, and their headroom
      a_{j+r+2} is A exactly when r = -1 mod P. So the verdict
      depends on r mod P ONLY and not on A at all:
        r = 0 mod P  -> delay 0 (this is the period shift)
        r = -1 mod P -> bounded delay
        otherwise    -> gated
      In particular a period-2 window has NO gated stride whatever,
      and a period-3 window reproduces e - 2's split exactly, which
      would make e - 2's pattern a fact about the period and not
      about e. KILL: any cell whose measured verdict disagrees, or
      any dependence on A.
  P8 (the parity candidate, tested for the record) the cubic's four
      measured strides read even/odd as bounded/gated, and e - 2
      already refutes that as a general law (stride 4 even and
      gated). Frozen: it fails window-relative too -- the criterion,
      not parity, predicts the cubic's strides 5..8. KILL of parity:
      any odd cubic stride reading at bounded delay or any even one
      gated. This prediction is DERIVED from P4 and is recorded
      separately only because parity is the first thing the measured
      table suggests.

THE DESIGN
----------
Digits by GREEDY descent, largest weight first, for inputs and images
alike -- no closed form from any target law enters the digit path.
Legality checked, never assumed: b_0 <= a_1 - 1; b_k <= a_{k+1};
b_k = a_{k+1} implies b_{k-1} = 0. Agreement depths from
sorted-consecutive pairs: sorting the strings makes any depth-d group
holding two differing image prefixes hold a CONSECUTIVE such pair, so
one pass yields A(t) = the deepest input agreement realized by a pair
whose images differ before depth t, and c_min(t) = max(0, A(t) - t + 1).

The four windows are the parent rig's, so P2's calibration is exact:
phi - 1 (quadratic, the control), cbrt(2) - 1 (cubic), e - 2, and the
CF-defined a_k = 2^k. The first two irrationals' partial quotients are
certified by interval arithmetic over exact rationals rather than read
off a decimal, which goes silently wrong at some depth: a term is
emitted only when an enclosure decides its floor, and the sequence
stops the moment it does not.

Digit strings are TUPLES of ints, never bytes -- the exploding window
passes alphabet 255 by position 8. Per window the usable depth K(N),
the largest t with q_t <= N, is computed and printed, and no table is
read past it, because beyond it every column is vacuous zeros that
would read as perfect agreement. Weights are built well past any image
the largest stride can produce, and the count of images exceeding the
built range is printed as a hard control.

E1  CONTROLS AND CALIBRATION. Reconstruction and legality over every
    n < N at every window; c_min(id) = 0; and the r = 1..4 stride
    rows against the parent rig's recorded ones.
E2  THE CRITERION FROM (a, r) ALONE. For r = 1..8 at each window:
    drop sites, chain sites, the lowest and highest chain site, and
    the criterion's verdict -- computed from the quotient sequence
    with no integer enumerated.
E3  THE MEASURED SWEEP AT r = 1..8. Repairs, lowest position the
    repair touches, and the c_min row, exhaustive over n < 100000 --
    twenty cells beyond the four the parent measured, and the table
    P4 is scored against.
E4  RANGE SCALING OF THE REPAIRING CELLS. The same rows at
    N = 30000, 100000, 300000 for the two windows that repair, with
    CAP(N) beside them: what separates a local Lipschitz constant
    from a cap artifact, and P6's observable.
E5  THE DESIGNED FAMILY. [0; (1^{P-1}, A)^inf] for P = 2..5 and
    A = 2, 3, 5, strides 1..2P, read at TWO ranges: the criterion and
    the measurement side by side over a family whose quotient sequence
    has exactly two parameters, so the criterion's dependence can be
    READ rather than fitted. P7's observable.
E6  OUT OF SAMPLE. The law E5 reads off, restated as a prediction and
    run at P = 6 and 7 with A = 2, 4 -- periods no fitted window
    carried, and P = 7 supplies the first even residue above 4.
    Added after E5 printed; the rule it scores was fixed by F4 before
    this experiment was written.

RESOURCE: estimate ~2 min wall, bounded, well under 512MB (digit
tuples, no numpy, no BLAS). Counted rather than guessed: E3 is
4 windows x 8 strides x 100000 greedy extractions, E4 is 2 x 8 x
430000, E5 is 12 windows x ~7 strides x 130000, and the parent rig's
measured 1.6M extractions in about 12 s sets the rate. E4 at
N = 300000 is the peak and is why the digit table is rebuilt per
window and dropped between them.

RUN RECORD
----------
Wall 84.9 s, peak working set 237.3 MB under a 512 MB ceiling. Six
rounds. E1 and E2 first (both controls green, and E2's closed form at
e - 2 read BEFORE any measurement of the new strides). Then E3, then
E4, then E5 at a single range. Then two corrections to the VERDICT
CLASSIFIER, each followed by a full rerun of everything -- and they
are recorded because the verdicts moved under them, so nothing here
was read off the first table. The classifier reads a c_min column and
must call it bounded or unbounded, and two distinct columns defeat
the obvious rule c_min(tmax) > 0: a cap-pinned column whose data cap
falls BELOW the top of the table has already declined to 0 inside it
and reads as bounded, while a genuine LOCAL constant that happens to
sit at the top of the table reads as gated. What separates them is
that a pinned column's witness depth is CONSTANT in t -- one witness
serving every depth is what an unbounded map looks like -- while a
local constant's is not, and a third signal, the witness tracking the
data cap, covers the cells where C_MAX truncates the column before
either shows. All three are unioned, and E5 adds growth across two
ranges on top. The lesson is the shape of the reading and not the
code: a single c_min column does not determine its own verdict, and
the corpus rows that read one did so with a range scan beside them.
E1 green at every window and every family member: zero reconstruction
failures, zero legality failures, zero images above the built
weights.

FINDINGS (each at its own tier)
-------------------------------
F1  CONTROLS AND CALIBRATION (P1, P2 land). c_min(id) = 0 at every
    depth and window. The r = 1..4 rows reproduce
    explore_nonquadratic_window.py's E9 exactly -- repairs
    99390/87743/95040/97465 at the cubic and 99390/99390/0/99390 at
    e - 2, the same gated cells, the same lowest touched positions.
    The digit path is the parent's and the tables are comparable.
F2  AT e - 2 THE VERDICT IS r MOD 3, AND THE FOUR NEW CELLS WERE
    CALLED BEFORE THEY WERE MEASURED (rule at scanned scope;
    P3 lands, its kill misses at all four). Predicted from the
    quotient sequence alone: r = 5 bounded, r = 6 no repair at
    delay 0, r = 7 gated, r = 8 bounded. Measured: exactly that.
    Repairs are 99390/100000 at every repairing stride -- one
    saturated count across three different verdicts, which is why no
    refinement of a repair COUNT could ever have separated them.
F3  THE HEADROOM CRITERION IS DEAD, AND NOT BY A DATA CAP (P4's kill
    fires at 29 cells -- five at the cubic, twenty-four across the
    designed family; P6 lands and removes the escape). The criterion
    over-predicts gating: it calls all eight cubic strides gated
    where five read at bounded delay, and it splits the designed
    family at r = -1 mod P where the measurement splits it somewhere
    else. Its named escape was that the cubic's bounded cells might
    be cap artifacts, and E4 closes it -- the cubic's stride-2
    constant (1 at t = 5) and stride-4 constants (3, 2, 1 at
    t = 3, 4, 5) are BYTE-IDENTICAL at N = 30000, 100000 and 300000
    while CAP(N) climbs, and strides 6, 7, 8 are stable too. So the
    up-carry's landing cap is not what decides a repairing cell. The
    hand-attack picked the wrong half of the rewrite for the third
    time in this thread, and the pattern is worth naming: absorption
    depth read the down-charge, tail magnitude read the size, the
    headroom read the up-carry, and all three are LOCAL features of
    one overflow event.
F4  WHAT DECIDES IT IS THE PARITY OF r MOD P (rule at scanned scope
    -- the leg's result; P7's frozen FORM is refuted and its family
    is what carries the law). Over the designed family
    [0; (1^(P-1), A)^inf] at P = 2, 3, 4, 5 and A = 2, 3, 5 -- twelve
    windows, every stride to 2P, both ranges -- the verdict is a
    function of r mod P alone, with no dependence on A whatever:
      r = 0 mod P            -> delay 0 (no repair; the period shift)
      r mod P EVEN, nonzero  -> bounded delay
      r mod P ODD            -> GATED.
    Unanimous, no exceptions, and F8 extends it out of sample. Three
    qualifiers the table earns and the sentence above does not carry.
    P = 2 tests only two of the three arms, having no even nonzero
    residue at all, so its whole content is that r odd gates and
    r even is the period shift. The even/odd reading is not the only
    rule fitting P <= 4 -- gated iff gcd(r, P) = 1 fits every cell
    through P = 4 -- and P = 5 is what parts them, its residues 2 and
    4 being coprime to 5 and bounded. And e - 2's large caps sit at
    j = 1 mod 3 while the designed family's sit at j = P - 1 mod P, a
    different residue class obeying the same law, which is evidence
    the law reads the SPACING of the large caps and not their
    address. It is not a fit: e - 2 is the P = 3 pattern with a
    GROWING A, and F2's independently derived r mod 3 law is exactly
    this one's P = 3 row. What the criterion turns on
    is that the down-borrow spans TWO positions (q_{p+1} - q_{p-1}),
    so the repair walks the digit lattice in steps of 2 and the
    question is whether it can return to the residue class carrying
    the big caps -- the same step-of-two recursion the max-string
    theorem runs on, one storey down. That reading is stated as the
    mechanism it looks like and is NOT proved here.
F5  THE DELAY-0 FLOOR IS THE LOWEST POSITION THE REPAIR TOUCHES
    (rule at scanned scope, 32 of 32 cells with zero violations --
    and it is NOT what P5 predicted). P5's kill fires: it froze the
    floor at the lowest CHAIN SITE'S LANDING, which is a quantity of
    the criterion F3 kills, and that floor is wrong at every cell
    where it is defined -- it puts the cubic's stride 1 floor at 4
    against a measured c_min(1) = 10, and e - 2's stride 1 at 3
    against a column already saturated at t = 2. The floor that does
    hold is the MEASURED reach, the lowest position any repair
    changes, and it was read off the run rather than predicted: every
    gated column's first nonzero entry sits exactly one above it, and
    e - 2's gated strides 1, 4, 7 touch 1, 3, 6 and open at
    t = 2, 4, 7. So the repair's REACH, which the storey below
    excluded as a verdict discriminator, is exactly right about WHERE
    the verdict starts and says nothing about what it is -- which is
    the same division of labour F4 draws, and neither half was
    available to the frozen criterion.
F6  THE PARITY CANDIDATE WAS RIGHT AND WAS READ AT THE WRONG MODULUS
    (P8's kill fires, and BOTH its halves lose: parity-of-r dies,
    and so does the criterion P8 offered in its place, so what
    replaces them is neither -- it is F4, parity at the right
    modulus). Parity of r itself fails: it survives 7 of the cubic's 8
    strides and dies at r = 7, odd and bounded, and e - 2 kills it at
    r = 4, even and gated. Parity of r MOD P is the law. The two look
    the same at every period-2 window, which is the whole reason the
    candidate looked plausible, and they come apart first at P = 3 --
    which is e - 2, the window that appeared to refute it.
F8  THE LAW HOLDS OUT OF SAMPLE (rule at scanned scope). F4 was read
    off P = 2..5. Restated as a prediction and run at P = 6 and 7
    with A = 2, 4 -- periods no fitted window carried, and P = 7
    carrying r mod P = 6, the first even residue above 4 anywhere in
    this rig -- it calls all 34 cells and misses none. So the law is
    not an artifact of the four periods it was read from, and the
    even/odd split is not the small-residue coincidence it could have
    been at P <= 5.
F7  THE CUBIC IS THE OPEN REMAINDER, AND ITS TABLE IS BANKED
    (observation). cbrt(2) - 1's quotients above 1 sit at positions
    0, 2, 5, 8, 10, 12, 13, 15, 16, 17, 18, 19, 21, 22 -- gaps of 1, 2
    and 3 from the start, on no residue class -- so F4's law has no
    subject there. Measured: strides 1, 3, 5 gated, strides 2, 4, 6,
    7, 8 at bounded delay, all stable across three ranges. Parity of
    r alone would call all of it and misses only r = 7, so the cubic
    behaves like an effective period-2 window with one exception, and
    that exception is the cheapest next handle on what P means at a
    window that has no period.
"""

from bisect import bisect_right
from fractions import Fraction

T_MAX = 10
C_MAX = 10
N = 100_000
R_MAX = 8
EXTRA = R_MAX + 12      # weight positions built beyond the largest image


# ---------------------------------------------------------------- windows

def cf_certified(lo, hi, want):
    """Certified partial quotients of any x with lo < x < hi.

    Emits a term only when the enclosure decides its floor, and stops
    the moment it does not -- so every term returned is exact.
    """
    out = []
    while len(out) < want:
        a = lo.numerator // lo.denominator
        if hi.numerator // hi.denominator != a and hi != a:
            break
        if lo - a <= 0:
            break
        out.append(a)
        lo, hi = Fraction(1) / (hi - a), Fraction(1) / (lo - a)
    return out


def icbrt(n):
    """Integer cube root by Newton descent."""
    x = 1 << ((n.bit_length() + 2) // 3 + 1)
    while True:
        y = (2 * x + n // (x * x)) // 3
        if y >= x:
            return x
        x = y


def quotients_cbrt2_minus_1(want):
    scale = 10 ** 400
    r = icbrt(2 * scale ** 3)
    lo, hi = Fraction(r, scale), Fraction(r + 1, scale)
    assert lo ** 3 < 2 < hi ** 3
    terms = cf_certified(lo - 1, hi - 1, want + 1)
    assert terms[0] == 0
    return terms[1:]


def quotients_e_minus_2(want):
    m, s, f = 400, Fraction(0), 1
    for k in range(m + 1):
        if k:
            f *= k
        s += Fraction(1, f)
    tail = Fraction(2, f * (m + 1))
    terms = cf_certified(s - 2, s + tail - 2, want + 1)
    assert terms[0] == 0
    return terms[1:]


WANT = 80
WINDOWS = [
    ("W0 phi-1      [0;1,1,1,...]   QUADRATIC", [1] * WANT),
    ("W1 cbrt(2)-1  cubic           CERTIFIED", quotients_cbrt2_minus_1(WANT)),
    ("W2 e-2        transcendental  CERTIFIED", quotients_e_minus_2(WANT)),
    ("W3 a_k = 2^k  CF-defined      EXPLODING", [2 ** k for k in range(1, WANT + 1)]),
]
REPAIRING = [WINDOWS[1], WINDOWS[2]]


def designed(period, big, want):
    """[0; (1^(P-1), A)^inf] -- one quotient A per period, rest 1."""
    return [big if (k + 1) % period == 0 else 1 for k in range(want)]


# ------------------------------------------------------------- numeration

def build_q(a, top):
    """Weights built until the last one passes top. a[k-1] is a_k."""
    q = [1, a[0]]
    k = 2
    while q[-1] <= top and k <= len(a):
        q.append(a[k - 1] * q[-1] + q[-2])
        k += 1
    return q


def build_q_positions(a, npos):
    """The same weights, built to exactly q_0 .. q_npos."""
    q = [1, a[0]]
    while len(q) <= npos and len(q) <= len(a):
        q.append(a[len(q) - 1] * q[-1] + q[-2])
    return q


def greedy(v, q):
    """Greedy Ostrowski digits of v >= 0, low-to-high, len(q) long."""
    d = [0] * len(q)
    for k in range(bisect_right(q, v) - 1, -1, -1):
        if q[k] <= v:
            b = v // q[k]
            d[k] = b
            v -= b * q[k]
    return d


def legality_failures(d, a):
    """Violations of the classical Ostrowski conditions."""
    fails = 0
    if d[0] > a[0] - 1:
        fails += 1
    for k in range(1, len(d)):
        if k >= len(a):
            break
        cap = a[k]                      # a_{k+1}
        if d[k] > cap:
            fails += 1
        if d[k] == cap and d[k - 1] != 0:
            fails += 1
    return fails


def usable_depth(q, top):
    """Largest t with q_t <= top."""
    t = 0
    while t + 1 < len(q) and q[t + 1] <= top:
        t += 1
    return t


def c_min_row(strings, order, imgs, tmax, depth):
    """A(t) from consecutive sorted pairs."""
    n = len(order)
    A = [-1] * (tmax + 1)
    for j in range(n - 1):
        i1, i2 = order[j], order[j + 1]
        s1, s2 = strings[i1], strings[i2]
        p = 0
        while p < depth and s1[p] == s2[p]:
            p += 1
        u1, u2 = imgs[i1], imgs[i2]
        dpos = 0
        while dpos < tmax and u1[dpos] == u2[dpos]:
            dpos += 1
        if dpos < tmax:
            for t in range(dpos + 1, tmax + 1):
                if p > A[t]:
                    A[t] = p
    return A


def fmt_row(A, tmax):
    out = []
    for t in range(1, tmax + 1):
        c = max(0, A[t] - t + 1)
        out.append(">" if c > C_MAX else str(c))
    return " ".join(f"{x:>2s}" for x in out)


def measured_verdict(repairs, A, tmax, cap):
    """GATED on any of three signals, because no one of them covers
    the whole table. A column SATURATED at c = C_MAX is unreadable
    outright. A column that is PINNED -- still open at the top of the
    table with the SAME witness depth serving two consecutive depths
    -- is an unbounded map's signature, and the constancy is what
    separates it from a local constant that happens to sit at the top
    of the table. And a column whose deepest witness TRACKS the data
    cap is unbounded even where the cap has fallen below the top of
    the table and the pinned column has already declined to 0 inside
    it -- the case that makes each of the first two alone wrong.
    Range stability is the authoritative call; E4 and E5 make it."""
    if repairs == 0:
        return "delay-0"
    saturated = any(A[t] - t + 1 > C_MAX for t in range(1, tmax + 1))
    pinned = A[tmax] - tmax + 1 > 0 and A[tmax] == A[tmax - 1]
    tracks_cap = A[tmax] >= cap - 2
    return "GATED" if (saturated or pinned or tracks_cap) else "bounded"


# -------------------------------------------------------- THE CRITERION

def criterion(a, r, jmax):
    """Drop sites, chain sites and the verdict, from (a, r) alone."""
    drops, chains = [], []
    for j in range(jmax + 1):
        if j + r + 2 >= len(a):
            break
        if a[j] > a[j + r]:             # a_{j+1} > a_{j+r+1}
            drops.append(j)
            if a[j + r + 1] == 1:       # headroom a_{j+r+2}
                chains.append(j)
    return drops, chains


def criterion_verdict(drops, chains, reach):
    """The frozen reading: no drop site -> delay 0; no chain site, or
    chain sites all landing below the readable range -> bounded;
    chain sites reaching the top of it -> gated."""
    if not drops:
        return "delay-0"
    if not chains:
        return "bounded"
    return "GATED" if max(chains) + 1 >= reach else "bounded"


# ------------------------------------------------------------ experiments

def stride_rows(name, a, n_top, tmax_cap=T_MAX, rmax=R_MAX, show=True):
    """Repairs, lowest touched position and c_min per stride, plus the
    criterion beside each. Returns {r: (repairs, lowest, A, verdicts)}."""
    kn = usable_depth(build_q(a, n_top), n_top)
    tmax = min(tmax_cap, kn - 1)
    depth = tmax + C_MAX + 2
    q = build_q_positions(a, kn + EXTRA)
    digits = [greedy(n, q) for n in range(n_top)]
    strings = [tuple(d[:depth]) for d in digits]
    order = sorted(range(n_top), key=lambda i: strings[i])
    qmax = q[-1]
    cap = 0
    for j in range(n_top - 1):
        s1, s2 = strings[order[j]], strings[order[j + 1]]
        p = 0
        while p < depth and s1[p] == s2[p]:
            p += 1
        if p > cap:
            cap = p
    out = {}
    if show:
        print(f"{name}   K(N) = {kn}, tables read to t = {tmax}, "
              f"CAP(N) = {cap}")
    for r in range(1, rmax + 1):
        if len(q) - r < 2:
            continue
        repairs, lowest, over = 0, None, 0
        imgs = []
        for n in range(n_top):
            d = digits[n]
            shifted = [0] * r + d[:len(q) - r]
            v = sum(d[k] * q[k + r] for k in range(len(q) - r) if d[k])
            over += v > qmax
            legal = greedy(v, q)
            if legal != shifted:
                repairs += 1
                pos = min(i for i in range(len(legal))
                          if legal[i] != shifted[i])
                if lowest is None or pos < lowest:
                    lowest = pos
            imgs.append(tuple(legal[:tmax]))
        A = c_min_row(strings, order, imgs, tmax, depth)
        mv = measured_verdict(repairs, A, tmax, cap)
        drops, chains = criterion(a, r, kn + EXTRA)
        cv = criterion_verdict(drops, chains, tmax)
        out[r] = (repairs, lowest, A, mv, cv, over, cap)
        if show:
            low = "-" if lowest is None else str(lowest)
            flag = "" if mv == cv else "   <<< DISAGREE"
            print(f"  r {r}: repairs {repairs:6d}/{n_top}  lowest {low:>2s}"
                  f"  c_min " + fmt_row(A, tmax)
                  + f"  | A_top {A[tmax]:2d}"
                  + f"  measured {mv:8s} criterion {cv:8s}"
                  + f" (drops {len(drops)}, chains {len(chains)})"
                  + f"{flag}")
        if over:
            print(f"    !! {over} images above the built weights at r = {r}")
    return out


def e1_controls():
    print("=" * 74)
    print("E1 CONTROLS AND CALIBRATION")
    for name, a in WINDOWS:
        kn = usable_depth(build_q(a, N), N)
        q = build_q_positions(a, kn + EXTRA)
        recon = legal = 0
        for n in range(N):
            d = greedy(n, q)
            recon += sum(x * w for x, w in zip(d, q)) != n
            legal += legality_failures(d, a)
        depth = min(T_MAX, kn - 1) + C_MAX + 2
        strings = [tuple(greedy(n, q)[:depth]) for n in range(N)]
        order = sorted(range(N), key=lambda i: strings[i])
        tmax = min(T_MAX, kn - 1)
        A = c_min_row(strings, order,
                      [s[:tmax] for s in strings], tmax, depth)
        idrow = fmt_row(A, tmax)
        print(f"{name}")
        print(f"  certified quotients: {len(a)};  a_1.. : "
              + " ".join(str(x) for x in a[:16]))
        print(f"  reconstruction failures {recon}, legality failures "
              f"{legal}  (n < {N});  c_min(id) {idrow}")
    print()


def e2_criterion():
    print("=" * 74)
    print("E2 THE CRITERION FROM (a, r) ALONE -- no integer enumerated")
    for name, a in WINDOWS:
        kn = usable_depth(build_q(a, N), N)
        tmax = min(T_MAX, kn - 1)
        print(f"{name}   (readable range top t = {tmax})")
        for r in range(1, R_MAX + 1):
            drops, chains = criterion(a, r, len(a) - r - 3)
            lo = chains[0] if chains else None
            hi = chains[-1] if chains else None
            v = criterion_verdict(drops, chains, tmax)
            print(f"  r {r}: drop sites {len(drops):3d}  chain sites "
                  f"{len(chains):3d}  lowest chain {str(lo):>4s}  "
                  f"highest chain {str(hi):>4s}  -> {v}")
    print()


def e3_sweep():
    print("=" * 74)
    print(f"E3 THE MEASURED SWEEP AT r = 1..{R_MAX}, n < {N}")
    for name, a in WINDOWS:
        stride_rows(name, a, N)
    print()


def e4_range():
    print("=" * 74)
    print("E4 RANGE SCALING OF THE REPAIRING CELLS")
    for name, a in REPAIRING:
        print(name)
        for n_top in (30_000, 100_000, 300_000):
            kn = usable_depth(build_q(a, n_top), n_top)
            print(f"  N = {n_top}:  K(N) = {kn}")
            rows = stride_rows("", a, n_top, show=False)
            for r in sorted(rows):
                repairs, lowest, A, mv, cv, _o, cap = rows[r]
                tmax = min(T_MAX, kn - 1)
                print(f"    r {r}: c_min " + fmt_row(A, tmax)
                      + f"  CAP {cap:2d} A_top {A[tmax]:2d}"
                      + f"  measured {mv:8s} criterion {cv}")
    print()


def e5_designed(ranges=(30_000, 100_000)):
    """The criterion and the measurement over a family whose quotient
    sequence has exactly two parameters, read at TWO ranges so the
    verdict rests on stability and not on one table's data cap."""
    print("=" * 74)
    print(f"E5 THE DESIGNED FAMILY [0; (1^(P-1), A)^inf], N = {ranges}")
    for period in (2, 3, 4, 5):
        for big in (2, 3, 5):
            a = designed(period, big, WANT)
            rows = [stride_rows("", a, n, rmax=2 * period, show=False)
                    for n in ranges]
            print(f"P = {period}, A = {big}")
            for r in sorted(rows[0]):
                cells = []
                for n, row in zip(ranges, rows):
                    kn = usable_depth(build_q(a, n), n)
                    tmax = min(T_MAX, kn - 1)
                    repairs, lowest, A, mv, cv, _o, cap = row[r]
                    cells.append((n, tmax, repairs, lowest, A, mv, cv, cap))
                # Range growth is one more gating signal on top of the
                # three the single-range verdict already carries: a
                # witness depth that rises with N is unbounded however
                # the column reads inside one table.
                grew = cells[1][4][cells[1][1]] > cells[0][4][cells[0][1]]
                stable = cells[-1][5]
                if grew and stable == "bounded":
                    stable = "GATED"
                cv = cells[-1][6]
                flag = "" if stable == cv else "   <<< DISAGREE"
                lo = cells[-1][3]
                print(f"  r {r}: repairs {cells[-1][2]:6d}  lowest "
                      f"{('-' if lo is None else str(lo)):>2s}  ")
                for n, tmax, _rep, _lo, A, mv, _c, cap in cells:
                    print(f"      N {n:6d}: c_min " + fmt_row(A, tmax)
                          + f"  CAP {cap:2d} A_top {A[tmax]:2d}")
                print(f"      -> measured {stable:8s} criterion {cv:8s}"
                      f"{flag}")
    print()


def e6_out_of_sample(n_top=100_000):
    """The law F4 reads off P = 2..5 stated as a PREDICTION and run at
    periods it has never seen. The rule is fixed before this
    experiment: delay 0 at r = 0 mod P, bounded delay at r mod P even
    and nonzero, gated at r mod P odd. P = 7 also supplies the first
    even residue above 4, which no fitted window contained."""
    print("=" * 74)
    print(f"E6 OUT OF SAMPLE: periods 6 and 7, n < {n_top}")
    miss = 0
    for period in (6, 7):
        for big in (2, 4):
            a = designed(period, big, WANT)
            rows = stride_rows("", a, n_top, rmax=period + 2, show=False)
            print(f"P = {period}, A = {big}")
            for r in sorted(rows):
                _rep, _lo, A, mv, _cv, _o, cap = rows[r]
                res = r % period
                pred = ("delay-0" if res == 0
                        else "bounded" if res % 2 == 0 else "GATED")
                ok = pred == mv
                miss += not ok
                print(f"  r {r}: r mod P = {res}  predicted {pred:8s}"
                      f"  measured {mv:8s}"
                      + ("" if ok else "   <<< LAW MISSES"))
    print(f"  law misses: {miss}")
    print()


def main():
    e1_controls()
    e2_criterion()
    e3_sweep()
    e4_range()
    e5_designed()
    e6_out_of_sample()


if __name__ == "__main__":
    main()
