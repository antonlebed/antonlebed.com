"""The uninhabited cell: the trailing Ostrowski window at alpha whose
continued fraction is NOT eventually periodic — is there a fourth
completion, and does anything read when no unit family acts?

THE QUESTION
------------
The trailing gate's law — readable at bounded delay iff the map acts
continuously on the window's completion — is carried by three
completion cells, each REALIZED by a window rather than exhausting the
question: RING (b-adic), ODOMETER (Zeckendorf and the whole quadratic
Ostrowski family), DISCRETE (the golden positional base). Every
Ostrowski row the corpus holds is at a QUADRATIC alpha, and by
Lagrange the quadratic irrationals are EXACTLY the alpha whose
continued fraction is eventually periodic — which is what gives the
digit string a SHIFT action for the order's fundamental unit to be. Off
that case there is no period, so no shift action, so no unit family
acting on the window at all. This rig builds the window there and reads
what is left.

THE UNIT FAMILY THE GATE NAMES IS THE UNITS THAT ACT ON THE WINDOW,
NOT THE UNITS THE FIELD CONTAINS, and the two must not be conflated.
A real cubic field has unit rank >= 1 — Q(cbrt 2)'s fundamental unit is
cbrt(2) - 1 — so at the cubic window units EXIST in abundance while
the window cannot use them: eps * n is not an integer, so eps is not a
map on the window at all, the window's maps being Z -> Z. That is the
positionality control's move (explore_goldenbase_control.py) applied
one axis over: hold "units exist" fixed and delete "units act".

THE WINDOWS. Ostrowski numeration needs only irrationality: for
alpha = [0; a_1, a_2, ...] with weights q_0 = 1, q_1 = a_1,
q_k = a_k q_{k-1} + q_{k-2}, every nonnegative integer writes uniquely
by greedy descent. Four windows, differing in KIND, so the run can
separate "non-quadratic" from "this alpha":
  W0  phi - 1      [0;1,1,1,...]        QUADRATIC — the calibration,
                   the recorded W1 of explore_ostrowski_window.py
  W1  cbrt(2) - 1  [0;3,1,5,1,1,4,...]  CUBIC — units exist in the
                   field, none act on the window; quotients bounded in
                   no obvious way and dropping constantly
  W2  e - 2        [0;1,2,1,1,4,1,1,6,...] quotients UNBOUNDED but
                   growing slowly, the alphabet growing with no
                   periodic shift anywhere
  W3  a_k = 2^k    [0;2,4,8,16,32,...]  quotients unbounded FAST — the
                   alphabet explodes, and the quotient sequence is
                   strictly INCREASING, which W1 and W2 are not
W1 and W2's partial quotients are not read off a decimal
approximation, which would go silently wrong at some depth: they are
computed by interval arithmetic over exact rationals (an enclosure
lo < alpha < hi; a term is emitted ONLY when floor(lo) = floor(hi),
and the sequence stops the moment the enclosure stops deciding), so
every term used is certified and E1 prints them for eyeball.
W3 is DEFINED by its quotient sequence, which is legitimate — the
window depends on the a_k alone — and NO transcendence or
Liouville-ness is claimed for it: with q_k ~ 2^(k^2/2) its
approximation exponent tends to 2, so it is not a Liouville number.
Irrationality (every infinite CF) is all this rig uses of it, and the
axis it carries is alphabet growth, not transcendence.

THE VOCABULARY (fixed before any engine). Digits by GREEDY descent,
largest weight first. Legality (checked in E1, never assumed):
b_0 <= a_1 - 1; b_k <= a_{k+1} for k >= 1; b_k = a_{k+1} implies
b_{k-1} = 0. The depth-t cell of n is agreement on b_0..b_{t-1}; cells
nest and first-disagreement is an ultrametric by construction. At W0
b_0 is identically 0 (a_1 = 1), so W0 depth-t equals the Zeckendorf
rig's depth-(t-1) and every c_min VALUE is unchanged under that shift
— the calibration reads values, never row indices.

HAND-ATTACK (pre-engine, on paper). Ostrowski normalization of an
OVERFLOWING digit is generic to the numeration and needs no
periodicity: if b_k > a_{k+1}, then since q_{k+1} = a_{k+1} q_k +
q_{k-1}, subtracting a_{k+1} q_k and adding q_{k+1} - q_{k-1} carries
UP one position while injecting a DOWN-BORROW of q_{k-1}. That is
exactly the mechanism proved to kill x2 at Zeckendorf and xa at every
constant-a window — and the derivation above uses only the recurrence,
so it survives the loss of the period. Under doubling a digit
overflows iff b_k > a_{k+1}/2, which is roughly half the alphabet at
any alphabet size, so the borrow should keep firing however large the
alphabet gets. Checked by hand the other way: 2 q_k on its own is the
legal digit 2 at position k whenever a_{k+1} >= 3, so single-weight
inputs never trigger it and the witness needs receptive low digits, as
at every earlier storey.
The SHIFT is where periodicity is genuinely load-bearing, and the hand
attack says so: b'_{k+1} = b_k needs b_k <= a_{k+2}, while legality
only gave b_k <= a_{k+1}. At a constant-a or periodic window the two
caps agree at the shift's own stride and the shift is digit-local; off
periodicity the shifted string is ILLEGAL exactly where the quotient
sequence DROPS, and repairing it runs the down-borrow above. W3's
quotients strictly increase, so its shift never needs the repair —
which makes the shift's readability a prediction about the quotient
sequence's MONOTONICITY and not about units at all.

TRANSPLANT MARKS. The odometer bound imported to a non-quadratic
window (P3) is adic-continuity folklore plus a quadratic measurement,
not a corpus row off periodicity — flagged. The gate's transplant
(P4) is the reverse of the previous storey's: there the risk was
importing a = 1 up to a >= 2, here it is importing a BOUNDED alphabet
out to an unbounded one, and the alphabet-vs-carry competition the
third storey resolved in carry's favour is re-run at W3 with the
alphabet given every advantage it can have.

PREDICTIONS, FIXED BEFORE THE RUN (as observables; the rig prints
c_min(f, t) = least c <= C_MAX such that every pair with input
agreement depth >= t + c has image agreement depth >= t, or the
UNREADABLE flag when c = C_MAX fails):
  P1 (control) f = id: c_min = 0 at every t, every window.
  P2 (calibration) W0 reproduces explore_ostrowski_window.py's W1
      row: n+1 = 1, L = 0, R alternating 1,2, and 2n, 3n, n//2
      UNREADABLE.
  P3 (the odometer) f = n+1: c_min <= 2 at EVERY window, the
      non-quadratic ones included, because the successor's carry
      propagates UP. KILL: n+1's c_min growing with t, or with range
      in E5, at any non-quadratic window — the fourth cell arriving on
      the first probe, since the odometer is the one map the odometer
      cell is named for.
  P4 (the gate with no unit family) f = 2n, 3n, n//2 gated at every
      window, delay tracking the data cap under range scaling.
      KILL: a c_min plateau while CAP rises by >= 3 at any
      window/map — a readable non-unit at a window with no unit family
      to be a unit of, the gate refuted off periodicity.
  P5 (the shift, which is nobody's unit here) c_min(L) = 0 at W3,
      whose quotients strictly increase so the shifted string is
      always legal, and c_min(L) > 0 at W1 and W2, whose quotients
      drop. Whether that > 0 is bounded or unbounded is the
      measurement and is deliberately not predicted. If it lands, the
      shift's readability is a fact about MONOTONICITY of the
      quotient sequence and not about unit-ness — an axis the
      quadratic rows could not see, every periodic window having both.
  P6 (the roof as a count) R_t, the number of realized depth-t
      strings, equals q_t EXACTLY at every window wherever q_t <= N,
      because the legal depth-t strings enumerate 0..q_t - 1. This
      would re-read the quadratic law rather than extend it: R_{t+l} /
      R_t -> the period-matrix eigenvalue is the special case of
      q_{t+l}/q_t at a periodic CF, so the roof count was never about
      units — it is the convergent denominator, and off periodicity
      R_{t+1}/R_t is about a_{t+1} and hence UNBOUNDED wherever the
      quotients are. KILL: any window and t with q_t <= N and
      R_t != q_t — the enumeration claim is wrong and the roof reading
      must be rebuilt from the measurement.
  P7 (the roof as cell SIZES — the other quantity of that name) at
      depth t the cell sizes over n < q_T take EXACTLY TWO values,
      split by whether b_{t-1} = 0, at every window. Ground: the count
      of legal completions above position t depends on the low block
      only through the legality coupling b_t = a_{t+1} => b_{t-1} = 0.
      Zeckendorf's exactly-two-valued roof would then be a
      window-independent fact about the numeration and not a Fibonacci
      one. KILL: three or more sizes at any (window, t), or a size not
      determined by [b_{t-1} = 0].
  P8 (range scaling) for the gated maps, A(N) tracks CAP(N) within 2
      at every window as N grows. Same kill as P4, read at range.
  P9 (the shift at range — E7, DESIGNED AFTER E2's FIRST RUN PRINTED,
      this prediction frozen before its own run) E2's L columns at W1
      and W2 are data-cap-shaped, exactly the ambiguity E5 exists to
      resolve for the arithmetic maps, and the first pass did not
      range-scale L — so P5's "> 0" cannot yet be told from a bounded
      plateau. Frozen: A(L) tracks CAP(N) within 2 at W1 and W2 as N
      grows (gated, delay unbounded), while at W0 and W3 no pair
      differs at the first non-vacuous image depth at all (delay 0).
      KILL: A(L) freezing while CAP rises by >= 3 at W1 or W2 — L is
      bounded-delay readable there too and P5's monotonicity reading
      is wrong; or any differing pair at W0 or W3 — L is not delay-0
      there and the E2 row was misread.
      The image depth this is read at is determined EMPIRICALLY and
      printed — the least position where two L-images differ at all —
      rather than set by the a_1 convention E5 uses, because L's own
      image carries a vacuous bottom digit wherever the shifted string
      needs no repair and a repaired one wherever it does, so no fixed
      convention is right at all four windows at once.

THE DESIGN
----------
Exhaustive over 0 <= n < N = 100000 per window, no sampling. Greedy
extraction ONLY, for inputs and for images alike — no closed form from
any target law enters the digit path. Agreement depths by
sorted-consecutive-pairs: sort n by low-first digit string; any
depth-d group holding two image-t-prefixes holds a CONSECUTIVE such
pair, so one pass over consecutive pairs yields A(t) = the deepest
input agreement realized by a pair whose images differ before depth t,
and c_min(t) = max(0, A(t) - t + 1), flagged UNREADABLE past C_MAX.

Digit strings are TUPLES of ints, never bytes: at W3 the alphabet
passes 255 by position 8 and a bytes() string would raise or truncate
there. Per-window the usable depth K(N) — the largest t with
q_t <= N — is computed and PRINTED, and every table is read only to
t <= K(N) - 1, because at W3 the weights outrun N by depth 6 and any
deeper column is vacuous zeros that would read as perfect agreement.
T_MAX = 10 capped per window at K(N) - 1; C_MAX = 10.

E1  CF CERTIFICATE AND DIGIT SANITY. The certified partial quotients
    print for W1 and W2. Greedy digits reconstruct n exactly (hard
    check) and satisfy the legality above (convention cross-check),
    all n < N, all windows; every image stays inside the built weight
    range (hard check, since the shift's images grow by a factor that
    is unbounded at W3). The positive controls c_min(id) = 0 and the
    P2 calibration row print BEFORE any gate verdict is read.
E2  THE GATE TABLE. c_min(f, t) for f in {n+1, L, R, 2n, 3n, n//2}
    over t = 1..T_MAX(window), each window.
E3  THE ROOF AS A COUNT. R_t against q_t, and the ratio R_{t+1}/R_t
    against a_{t+1}.
E4  THE ROOF AS CELL SIZES. Over n < q_T for the largest T with
    q_T <= N: the distinct depth-t cell sizes and whether the size is
    a function of [b_{t-1} = 0]. Exact by construction — no N
    truncation enters, which is why the range is q_T and not N.
E5  RANGE SCALING. For N in {30000, 100000, 300000}: CAP(N) = the
    deepest realized pair agreement, and for f in {n+1, 2n, 3n, n//2}
    the witness depth A(N) = the deepest agreement among pairs whose
    images differ at the first non-vacuous depth. n+1 rides along
    because P3's kill is a range statement.
E6  EXTREMAL WITNESSES. For f = 2n at each window, the deepest
    input-agreement pair whose images differ at the first non-vacuous
    depth, printed as integers — the seed a proof leg would grow a
    witness family from.
E7  THE SHIFT AT RANGE. The same discriminator run on L alone, over
    the same three N, with the image depth found empirically and
    printed. Added after E2's first run; see P9.
E8  RENORMALIZATION CENSUS. Whether the shift is the bare coordinate
    shift or needs legality repair, how often, and the lowest digit
    position the repair reaches — the MECHANISM P5 asserted
    pre-engine, and which E2 and E7 only ever measured the
    consequence of. Added later; everything it counts is at stride 1.
E9  THE SHIFT AT STRIDE r, r = 1..4. E2's L is the stride-1 shift
    while the quadratic rig's L is the shift by the PERIOD, so "the
    shift" was being read off a single stride; this sweeps them,
    printing monotonicity along the stride, the repair count, the
    lowest position touched, and c_min. Added last, and it is where
    the stride-1 reading of P5 fails to generalize — see P-STRIDE
    and F3.

RESOURCE: estimate ~10 min — counted rather than guessed: the greedy
descent costs one pass over the built weights per extraction, and E5
alone runs 4 windows x 4 maps x 300000 of them. Well under 512MB
(digit tuples, no numpy, no BLAS); the E5 pass at N = 300000 is the
peak and is run last.

RUN RECORD
----------
Four rounds of running, each adding an experiment to the one before
and rerunning the whole rig. E1-E6 first (all sanity green, both
controls green before any verdict was read). Then E7, with P9 frozen
before its own run — E1-E6 output byte-identical, checked by diff and
not by eye. Then E8, added on noticing that P5's mechanism was being
asserted with no measurement anywhere behind it; the mechanism itself
was frozen pre-engine and unchanged, so E8 confirms a pre-registered
claim rather than reading one off. Then E9, with P-STRIDE frozen
before its own run, after noticing that "the shift" had been read off
stride 1 alone — and E9 is what refutes the stride-1 reading, so the
last experiment added is the one that changed the storey.
Wall 14.0 s at E1-E6, 19.5 s with E7, 25.3 s for the rig as it now
stands; peak working set 170.5 MB rising to 280.4 MB, against
memwatch's 512 MB ceiling. The ~10 min estimate overshot by about 40x
and the reason is in the code: the greedy descent starts at the
largest weight below v rather than at the top of the built list, so it
costs the digit count and not the built length — the counted estimate
counted the wrong loop.
E1 green at every window: zero reconstruction failures, zero legality
failures, zero images outside the built weights, n < 100000. The
certified quotients printed as
cbrt(2)-1 = [0; 3,1,5,1,1,4,1,1,8,1,14,1,10,2,1,4,12,2,3,2,1,3,4,1,...]
and e-2 = [0; 1,2,1,1,4,1,1,6,1,1,8,1,1,10,...], both matching the
classical expansions.

FINDINGS (each at its own tier)
-------------------------------
F1  THE ODOMETER READS AT EVERY WINDOW (rule at scanned scope).
    c_min(n+1) <= 1 at every window and every depth, and E5 shows it
    is not a data-cap artifact: A(n+1) is CONSTANT at 1 or 2 across
    N = 30k, 100k, 300k while CAP climbs to 26 (W0), 12 (W1), 15
    (W2). P1's control green everywhere, P3 lands and its kill
    misses. The successor's carry propagates UP, and periodicity was
    never what bounded it.
F2  THE GATE BINDS EVERY TESTED NON-UNIT OFF PERIODICITY (rule at
    scanned scope; the E5 discriminator is the evidence). 2n, 3n and
    n//2 are gated at all four windows. E2's columns at W1/W2/W3 are
    data-cap-shaped exactly as the third storey's were, and E5
    separates the readings: A tracks CAP within 1 at every window,
    every map, every N (W1 caps 10/12/12, A(2n) 9/11/11; W2 caps
    13/13/15, A(2n) 12/12/14; W3 caps 4/5/5, A(2n) 4/4/4). P4 and P8
    land, the kill misses everywhere. The hand-attack's mechanism is
    what carries it off periodicity: overflow normalization at ANY
    window rewrites b_k > a_{k+1} through q_{k+1} - q_{k-1}, an up
    carry with a DOWN-borrow attached, and that derivation uses the
    recurrence alone and never the period. The alphabet-vs-carry
    competition, re-run at W3 where the alphabet explodes, resolves
    in carry's favour again.
    CAVEAT, named rather than buried: W3 is the weakest cell and
    STRUCTURALLY so. Depth t costs q_t, which explodes with the
    quotients, so a tenfold range buys CAP 4 -> 5 -> 5 and the
    discriminator has almost no room. No budget fixes this: an
    exploding-alphabet window cannot be probed deep by range scaling
    at all, and what W3 needs is a proof leg or a different
    observable.
F3  THE SHIFT'S READABILITY IS A PROPERTY OF THE STRIDE, AND UNITS
    ARE NOWHERE IN IT (rule at scanned scope — the storey's result).
    E2's L is the stride-1 shift while the quadratic rig's L is the
    shift by the PERIOD, the same map only where the period is 1 — so
    "the shift" has to be read at every stride, and E9 does.
    THE SUFFICIENT HALF, mechanism and measurement agreeing: where
    the quotient sequence is NON-DECREASING along stride r, the
    shifted string is never illegal (b'_{k+r} = b_k needs
    b_k <= a_{k+r+1}, and legality gave b_k <= a_{k+1}), the repair
    fires on 0 of 100000 inputs, the shift is the bare coordinate
    map, and c_min = 0 at every depth. That is W0 and W3 at every
    stride scanned, and W2 at stride 3 — where e - 2's quotient
    pattern 1, 1, 2n makes stride 3 non-decreasing with no periodicity
    anywhere.
    THE CONVERSE FAILS, and P-STRIDE's kill FIRES against the neat story:
    W1 strides 2 and 4 and W2 stride 2 repair on 88 to 99 percent of
    inputs and STILL read at bounded delay (c_min <= 1, <= 3, and 0
    respectively). A repair can be absorbed locally. So monotonicity
    along the stride is SUFFICIENT for delay 0 and is not necessary,
    and the earlier reading of this rig — that the split is exactly
    whether the quotients drop — was stride-1 evidence generalized
    one step too far.
    AND THE OBVIOUS REPAIR TO THAT STORY ALSO FAILS. The natural
    discriminator, how far DOWN the repair reaches, does not separate
    the cells either: at W2 strides 1 and 2 the repair reaches
    position 1 in both, and stride 1 is gated at every depth past the
    first while stride 2 reads at all of them. What decides a
    repairing cell is NOT settled here and is named as open.
    THE GATED CELLS, for the record: W1 strides 1 and 3, W2 strides 1
    and 4, each c_min data-cap-shaped, and stride 1's unboundedness
    confirmed directly at range by E7 — A(L) tracks CAP at W1
    (10, 10, 12 against CAP 10, 12, 12) and W2 (10, 13, 13 against
    13, 13, 15, the one gap of 3 at the smallest N closing as the
    range grows), against a constant 1 and 0 at W0 and W3.
    P5 lands in direction, P9's kill misses. P9's frozen FORM for W0
    and W3 is an honest MISS, filed: it said no pair would differ at
    the first non-vacuous image depth at all, and pairs do differ, at
    BOUNDED agreement depth — which is delay 0 and not the absence of
    a witness. The observable was frozen one notch too strong.
    AND THIS IS THE STOREY'S POINT, which the stride sweep
    STRENGTHENS rather than costs. At every non-quadratic window here
    there is no unit family for any shift to be the action of — no
    period, no order, no fundamental unit, and at e - 2 no algebraic
    units of any kind — and at every one of them some stride reads at
    bounded delay anyway, and at delay 0 in six of the twelve
    (window, stride) cells scanned. The window where NO
    scanned stride reads at delay 0 is the CUBIC, which is the one
    whose field has units.
F4  BOTH QUANTITIES CALLED THE ROOF ARE WINDOW-INDEPENDENT (rule; the
    count follows from the standard uniqueness theorem, and both are
    verified exhaustively at every window and depth measured).
    R_t = q_t EXACTLY, no exceptions anywhere — the legal depth-t
    strings enumerate 0..q_t - 1. And the depth-t cell sizes take
    EXACTLY TWO values, split by whether b_{t-1} = 0, at every window
    and every depth (the t = 1 row at W0 and W2 degenerate, a_1 = 1
    forcing b_0 = 0 and leaving one class empty).
    WHAT THIS DEFLATES: neither quantity ever carried information
    about units, and both recorded quadratic readings are corollaries
    of periodicity. "The roof count grows by the unit" is
    q_{t+l}/q_t -> the period-matrix eigenvalue, which is convergent
    asymptotics at a periodic CF; off periodicity R_{t+1}/R_t is
    about a_{t+1} and is UNBOUNDED wherever the quotients are (W3:
    4.5, 8.2, 16.1 and climbing). And Zeckendorf's roof being
    "exactly two-valued, the two consecutive Fibonacci numbers, ratio
    -> phi" is the window-independent two-valuedness above, plus the
    fact that at phi the two values happen to be Fibonacci.
F6  THE SHIFT'S MECHANISM, MEASURED (rule at scanned scope — the
    measurement P5's hand-attack asserted without ever taking).
    At W0 and W3, the two windows whose quotients never drop, the
    shift needs NO repair at all: 0 of 100000 shifted strings are
    illegal, so L is the bare coordinate shift and its delay-0 read
    in E2 and E7 is exactly that. At W1 and W2, whose quotients drop
    at k = 2, 5, 8, 10, 12, 13 and k = 1, 4, 7, 10, 13, the repair
    fires on 99390 of 100000 inputs and reaches the LOWEST
    non-vacuous position — position 0 at W1 (a_1 = 3) and position 1
    at W2 (a_1 = 1, b_0 vacuous). Read this as stride 1's census and
    not the shift's: E9 shows the other strides behave differently at
    the same two windows. The smallest instance is the
    down-borrow in three digits: at W1, n = 2 shifts to [0, 2, 0, ...],
    illegal because b_1 <= a_2 = 1, and legalizes to [2, 0, 1, ...] —
    that is 2 q_1 = q_2 + 2 q_0, an up carry with a down term, the
    same identity shape that gates multiplication. P5's mechanism is
    confirmed exactly as stated pre-engine; only its measurement was
    late.
    ONE NUMBER CHASED AND CLEARED: W1 and W2 both leave exactly 610
    inputs unrepaired at N = 100000, and two unrelated windows
    agreeing to the digit is not a shared law — at N = 30000 the
    counts are 233 and 610, W2's set having saturated (its largest
    member is 27277) while W1's is still growing. Coincidence of the
    cutoff, recorded because the agreement looks like a law.
F5  THE PROOF SEEDS (observation, banked). Extremal 2n pairs: W1
    (78909, 74096) agreeing to input depth 11, W2 (94716, 13816) to
    12, W3 (95624, 20317) to 4; W0's (69551, 98208) at depth 22
    recovers the recorded Zeckendorf extremal shape. Off periodicity
    no comb telescope is available — there is no repeating identity
    for a comb to telescope through — so a proof leg here would run
    through the max-string theorem, which is already proved at
    ARBITRARY tail with periodicity never used
    (explore_general_max_string.py), rather than through a bespoke
    comb.

THE READING. No fourth completion at any of the three non-quadratic
windows: each completes to an ODOMETER, the same cell the whole
quadratic family occupies — the odometer n+1 reads at bounded delay,
every tested integer m >= 2 and n//2 is gated with delay growing with
range. So the odometer cell is NOT the unit cell; it is inhabited by
windows with no unit family at all, and the cubic control is what
isolates that axis — units exist in abundance in Q(cbrt 2) and none of
them act on the window. On the arithmetic maps it then behaves exactly
like the transcendental window; on the SHIFTS it does not, and the
difference runs the wrong way for units — e - 2 has a stride reading
at delay 0 and the cubic has none among the four scanned.
What the probe moves is the READING of the gate. Its two statements —
UNIT-NESS in the table, CONTINUITY of the action on the completion in
the paragraph after it — come apart here for the first time, and
CONTINUITY is the one that survives. At every window here unit-ness
has no subject, and at every one of them some stride reads at bounded
delay anyway; where that read is at delay 0 the reason is that the
shift is literally a coordinate map, which is continuity and nothing
else. What continuity has NOT been shown to do is decide the
REPAIRING cells — those needing legality repair and reading at bounded
delay all the same — and that is the open half F3 names, the first
thing a next leg should take. The unit-ness form is a
periodicity artifact: where a CF is eventually periodic the digit
shift and multiplication by the order's fundamental unit are the SAME
map, and no quadratic row could tell which of the two was doing the
work. The fourth-completion question stays open — these three windows
do not answer it; they fix the terms the answer has to be stated in.
(Settled since, off this family: a fourth shape is realized at the
trailing Tribonacci window, explore_tribonacci_discontinuity.py, and a
fifth past it, explore_silent_window.py.)
"""

from bisect import bisect_right
from fractions import Fraction

T_MAX = 10
C_MAX = 10
N = 100_000
EXTRA = 10          # weight positions built beyond the largest image


def cf_certified(lo, hi, want):
    """Certified partial quotients of any x with lo < x < hi.

    Emits a term only when the enclosure decides its floor, and stops
    the moment it does not — so every term returned is exact.
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


WANT = 70
WINDOWS = [
    ("W0 phi-1      [0;1,1,1,...]   QUADRATIC", [1] * WANT, True),
    ("W1 cbrt(2)-1  cubic           CERTIFIED", quotients_cbrt2_minus_1(WANT), True),
    ("W2 e-2        transcendental  CERTIFIED", quotients_e_minus_2(WANT), True),
    ("W3 a_k = 2^k  CF-defined      EXPLODING", [2 ** k for k in range(1, WANT + 1)], False),
]


def build_q(a, top):
    """Weights q_0 = 1, q_1 = a_1, q_k = a_k q_{k-1} + q_{k-2}, built
    until the last one passes top. a is 1-indexed as a[k-1]."""
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
    """A(t) and the witness pair per t, from consecutive sorted pairs."""
    n = len(order)
    A = [-1] * (tmax + 1)
    wit = [None] * (tmax + 1)
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
                    wit[t] = (i1, i2)
    return A, wit


def run_window(name, a, certified):
    print("=" * 72)
    print(name)
    if certified:
        print("  quotients a_1.. : " + " ".join(str(x) for x in a[:24]))
    kn = usable_depth(build_q(a, N), N)
    tmax = min(T_MAX, kn - 1)
    depth = tmax + C_MAX + 2
    # weights built well past any image the maps can produce: the
    # shift multiplies by q_{k+1}/q_k, unbounded at W3.
    q = build_q_positions(a, kn + EXTRA)
    print(f"  usable depth K(N) = {kn} at N = {N}; tables read to "
          f"t = {tmax}; weights built to q_{len(q) - 1}")

    digits = [greedy(n, q) for n in range(N)]
    recon = sum(1 for n in range(N)
                if sum(d * w for d, w in zip(digits[n], q)) != n)
    legal = sum(legality_failures(d, a) for d in digits)
    print(f"E1 digit sanity: reconstruction failures {recon}, "
          f"legality failures {legal}  (n < {N})")

    strings = [tuple(d[:depth]) for d in digits]
    order = sorted(range(N), key=lambda i: strings[i])
    qmax = q[-1]

    def shift_L(i):
        d = digits[i]
        return sum(d[k] * q[k + 1] for k in range(len(q) - 1) if d[k])

    def shift_R(i):
        d = digits[i]
        return sum(d[k] * q[k - 1] for k in range(1, len(q)) if d[k])

    maps = [
        ("id", lambda i: i),
        ("n+1", lambda i: i + 1),
        ("L", shift_L),
        ("R", shift_R),
        ("2n", lambda i: 2 * i),
        ("3n", lambda i: 3 * i),
        ("n//2", lambda i: i // 2),
    ]

    print(f"E2 c_min(f, t), t = 1..{tmax}  "
          f"('>' = UNREADABLE at c = {C_MAX}):")
    witness = None
    overflow = 0
    for fname, f in maps:
        vals = [f(i) for i in range(N)]
        overflow += sum(1 for v in vals if v > qmax)
        imgs = [tuple(greedy(v, q)[:tmax]) for v in vals]
        A, wit = c_min_row(strings, order, imgs, tmax, depth)
        row = []
        for t in range(1, tmax + 1):
            c = max(0, A[t] - t + 1)
            row.append(">" if c > C_MAX else str(c))
        print(f"  {fname:5s} " + " ".join(f"{x:>2s}" for x in row))
        if fname == "2n":
            t0 = 2 if a[0] == 1 else 1
            witness = (A[t0], wit[t0], t0)
    print(f"E1 image range check: images above the built weights: "
          f"{overflow}")

    print("E3 roof as a count: R_t vs q_t, and R_(t+1)/R_t vs a_(t+1):")
    mism = []
    for t in range(1, tmax + 1):
        rt = len({s[:t] for s in strings})
        if rt != q[t]:
            mism.append((t, rt, q[t]))
    print("  R_t: " + " ".join(str(len({s[:t] for s in strings}))
                               for t in range(1, tmax + 1)))
    print("  q_t: " + " ".join(str(q[t]) for t in range(1, tmax + 1)))
    print(f"  R_t != q_t at: {mism if mism else 'nowhere'}")
    print("  R_(t+1)/R_t: " + " ".join(
        f"{q[t + 1] / q[t]:.3f}" for t in range(1, tmax)))
    print("  a_(t+1):     " + " ".join(
        f"{a[t]:.3f}" for t in range(1, tmax)))

    print("E4 roof as cell sizes (exact over n < q_T, no truncation):")
    tt = kn
    span = q[tt]
    dig_s = [greedy(n, q)[:tt] for n in range(span)]
    for t in range(1, tt):
        cells = {}
        for d in dig_s:
            cells[tuple(d[:t])] = cells.get(tuple(d[:t]), 0) + 1
        sizes = sorted(set(cells.values()))
        by_class = {0: set(), 1: set()}
        for pref, c in cells.items():
            by_class[0 if pref[t - 1] == 0 else 1].add(c)
        ok = (len(by_class[0] & by_class[1]) == 0
              and len(by_class[0]) <= 1 and len(by_class[1]) <= 1)
        print(f"  t = {t}: sizes {sizes}  "
              f"b_(t-1)=0 -> {sorted(by_class[0])}, "
              f"!=0 -> {sorted(by_class[1])}  "
              f"two-valued-by-class: {ok}")

    if witness and witness[1]:
        da, (w1, w2), t0 = witness
        print(f"E6 witness (2n, t = {t0}): pair ({w1}, {w2}) agrees to "
              f"input depth {da}, doubles differ before depth {t0}")
    print()


def range_scaling():
    print("=" * 72)
    print("E5 RANGE SCALING: CAP(N) and witness depth A(N), "
          "maps n+1 / 2n / 3n / n//2")
    for name, a, _ in WINDOWS:
        t0 = 2 if a[0] == 1 else 1
        print(name)
        for n6 in (30_000, 100_000, 300_000):
            kn6 = usable_depth(build_q(a, n6), n6)
            q = build_q_positions(a, kn6 + EXTRA)
            d6 = kn6 + C_MAX + 2
            strs = [tuple(greedy(n, q)[:d6]) for n in range(n6)]
            order = sorted(range(n6), key=lambda i: strs[i])
            pref = []
            for j in range(n6 - 1):
                s1, s2 = strs[order[j]], strs[order[j + 1]]
                p = 0
                while p < d6 and s1[p] == s2[p]:
                    p += 1
                pref.append(p)
            cap = max(pref)
            row = [f"CAP {cap:2d}"]
            for fname, f in (("n+1", lambda i: i + 1),
                             ("2n", lambda i: 2 * i),
                             ("3n", lambda i: 3 * i),
                             ("n//2", lambda i: i // 2)):
                imgs = [tuple(greedy(f(i), q)[:t0]) for i in range(n6)]
                best = -1
                for j in range(n6 - 1):
                    if (imgs[order[j]] != imgs[order[j + 1]]
                            and pref[j] > best):
                        best = pref[j]
                row.append(f"A({fname}) {best:2d}")
            print(f"  N = {n6:6d}: " + "  ".join(row))
    print()


def shift_at_range():
    """E7: the same CAP-vs-A discriminator run on the shift L, with
    the image depth found empirically rather than by convention."""
    print("=" * 72)
    print("E7 THE SHIFT AT RANGE: CAP(N) and witness depth A(L)")
    for name, a, _ in WINDOWS:
        print(name)
        for n6 in (30_000, 100_000, 300_000):
            kn6 = usable_depth(build_q(a, n6), n6)
            q = build_q_positions(a, kn6 + EXTRA)
            d6 = kn6 + C_MAX + 2
            digs = [greedy(n, q) for n in range(n6)]
            strs = [tuple(d[:d6]) for d in digs]
            order = sorted(range(n6), key=lambda i: strs[i])
            pref = []
            for j in range(n6 - 1):
                s1, s2 = strs[order[j]], strs[order[j + 1]]
                p = 0
                while p < d6 and s1[p] == s2[p]:
                    p += 1
                pref.append(p)
            cap = max(pref)
            imgs = [tuple(greedy(sum(d[k] * q[k + 1]
                                     for k in range(len(q) - 1) if d[k]),
                                 q)[:6])
                    for d in digs]
            t0 = None
            for pos in range(6):
                if len({im[pos] for im in imgs}) > 1:
                    t0 = pos + 1
                    break
            best = -1
            if t0 is not None:
                for j in range(n6 - 1):
                    if (imgs[order[j]][:t0] != imgs[order[j + 1]][:t0]
                            and pref[j] > best):
                        best = pref[j]
            shown = "none" if best < 0 else f"{best:2d}"
            print(f"  N = {n6:6d}: CAP {cap:2d}  image depth t0 = {t0}"
                  f"  A(L) {shown}")
    print()


def renormalization_census():
    """E8: does the shift need repair, and where does the repair land?

    P5's hand-attack asserted the mechanism pre-engine — the shifted
    string is illegal exactly where the quotients DROP, and repairing
    it runs the down-borrow down to the bottom. E2 and E7 measured the
    CONSEQUENCE (delay 0 against gated) and never the mechanism, so
    this counts it directly. Everything here is at STRIDE 1, which is
    the stride E2's L uses; E9 sweeps the others and is where the
    stride-1 reading turns out not to generalize.
    """
    print("=" * 72)
    print("E8 RENORMALIZATION CENSUS: is the shift the bare coordinate "
          "shift, and if not, how low does the repair reach?")
    for name, a, _ in WINDOWS:
        kn = usable_depth(build_q(a, N), N)
        q = build_q_positions(a, kn + EXTRA)
        drops = [k for k in range(1, kn + 2)
                 if k + 1 < len(a) and a[k + 1] < a[k]]
        repaired, touched, first = 0, set(), None
        for n in range(N):
            d = greedy(n, q)
            shifted = [0] + d[:len(q) - 1]
            v = sum(d[k] * q[k + 1] for k in range(len(q) - 1) if d[k])
            legal = greedy(v, q)
            if legal != shifted:
                repaired += 1
                pos = min(i for i in range(len(legal))
                          if legal[i] != shifted[i])
                touched.add(pos)
                if first is None:
                    first = (n, shifted[:6], legal[:6])
        print(f"{name}")
        print(f"  quotient drops at k = {drops[:8]}")
        print(f"  repaired: {repaired} / {N};  lowest position the "
              f"repair changes: {sorted(touched)[:8]}")
        if first:
            print(f"  first repair: n = {first[0]}, shifted {first[1]}"
                  f" -> legal {first[2]}")
    print()


def stride_sweep():
    """E9: the shift at STRIDE r, r = 1..4.

    E2's L is the stride-1 shift, while the quadratic rig's L is the
    shift by the PERIOD — the same map only where the period is 1. So
    "the shift is gated here" was being read off stride 1 alone, and a
    window with no period can still have a stride its quotient
    sequence never decreases along. This sweeps them.

    PREDICTION P-STRIDE, frozen before this run: c_min(L_r) = 0 at exactly
    those (window, r) where the quotient sequence is non-decreasing
    along stride r, and gated elsewhere — the legality-repair
    mechanism of P5 and E8, now read as a statement about a STRIDE
    rather than about the sequence as a whole. KILL: any cell where
    the monotonicity flag and the readability verdict disagree.
    Provenance: the repair COUNTS at each stride were seen before this
    experiment was written; the c_min verdicts it prints were not.
    """
    print("=" * 72)
    print("E9 THE SHIFT AT STRIDE r: monotonicity along the stride, "
          "repairs, and c_min")
    for name, a, _ in WINDOWS:
        kn = usable_depth(build_q(a, N), N)
        tmax = min(T_MAX, kn - 1)
        depth = tmax + C_MAX + 2
        q = build_q_positions(a, kn + EXTRA)
        digits = [greedy(n, q) for n in range(N)]
        strings = [tuple(d[:depth]) for d in digits]
        order = sorted(range(N), key=lambda i: strings[i])
        print(f"{name}")
        for r in range(1, 5):
            if len(q) - r < 2:
                continue
            mono = all(a[j + r] >= a[j] for j in range(kn + 2)
                       if j + r < len(a))
            repairs, lowest = 0, None
            imgs = []
            for n in range(N):
                d = digits[n]
                shifted = [0] * r + d[:len(q) - r]
                v = sum(d[k] * q[k + r]
                        for k in range(len(q) - r) if d[k])
                legal = greedy(v, q)
                if legal != shifted:
                    repairs += 1
                    pos = min(i for i in range(len(legal))
                              if legal[i] != shifted[i])
                    if lowest is None or pos < lowest:
                        lowest = pos
                imgs.append(tuple(legal[:tmax]))
            A, _w = c_min_row(strings, order, imgs, tmax, depth)
            row = []
            for t in range(1, tmax + 1):
                c = max(0, A[t] - t + 1)
                row.append(">" if c > C_MAX else str(c))
            low = "-" if lowest is None else str(lowest)
            print(f"  stride {r}: non-decreasing {str(mono):5s}  "
                  f"repairs {repairs:6d}/{N}  lowest touched {low:>2s}"
                  f"  c_min " + " ".join(f"{x:>2s}" for x in row))
    print()


def main():
    for name, a, certified in WINDOWS:
        run_window(name, a, certified)
    range_scaling()
    shift_at_range()
    renormalization_census()
    stride_sweep()


if __name__ == "__main__":
    main()
