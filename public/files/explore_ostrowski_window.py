"""The third storey: the trailing Ostrowski window at four quadratic
irrationals — which completion does each window buy, and does the
gate track the unit group of the order?

THE QUESTION
------------
The two-gates law's trailing form — readable at bounded delay iff
the map acts continuously on the window's completion — is proved
or rule-tier at three trailing windows: b-adic (ring
completion — all integer multiplication continuous, division
gated), Zeckendorf (odometer completion — units only, x2's failure
proved: explore_zeckendorf_discontinuity.py), golden positional
(discrete completion — vacuous). Zeckendorf is the alpha = phi case
of OSTROWSKI numeration: for irrational alpha = [0; a_1, a_2, ...],
every nonnegative integer writes uniquely over the convergent
denominators q_k. This rig builds the Ostrowski trailing window at
four quadratic irrationals and measures which maps read — the
trichotomy's conjecture tested one storey up.

THE WINDOWS (all with eventually-periodic CF — quadratic):
  W1  phi        = [0; 1, 1, 1, ...]   (calibration: Zeckendorf)
  W2  sqrt(2)-1  = [0; 2, 2, 2, ...]   (Pell / silver)
  W3  bronze     = [0; 3, 3, 3, ...]
  W4  sqrt(3)-1  = [0; 1, 2, 1, 2, ...] (period 2)

THE WINDOW'S VOCABULARY (fixed before any engine). Weights: q_0 = 1,
q_1 = a_1, q_k = a_k q_{k-1} + q_{k-2}. Digits by GREEDY descent
(largest q first); the classical Ostrowski legality (checked in E1,
not assumed): b_0 <= a_1 - 1; b_k <= a_{k+1} for k >= 1;
b_k = a_{k+1} implies b_{k-1} = 0. The depth-t cell of n is
agreement on the t low-order digits b_0..b_{t-1}; cells nest, the
first-disagreement metric is an ultrametric by construction. At W1
the digit b_0 is identically 0 (a_1 = 1), so W1 depth-t equals the
Zeckendorf rig's depth-(t-1) and every c_min VALUE is unchanged
under the shift (both agreement depths gain the same vacuous
digit) — the calibration reads values, not row indices.

THE ORDERS AND THEIR UNITS (the storey's question). The shift-by-l
map (l the CF period) multiplies asymptotically by the dominant
eigenvalue of the period matrix: phi at W1, the silver mean
1+sqrt(2) at W2, (3+sqrt(13))/2 at W3, 2+sqrt(3) at W4 — each a
UNIT of its quadratic order. The RATIONAL integers m >= 2 are units
in NONE of these orders (norms m^2 != +-1). So the unit-gate
conjecture, read at this storey: the shifts and the odometer read
at bounded delay; every integer multiplication m >= 2 and every
floor-division is gated — at EVERY quadratic window, the completion
is an odometer and never a ring. The b-adic ring completion would
then be exclusive to non-unit (rational, positional) bases.

HAND-ATTACK (pre-engine). The Zeckendorf down-carry generalizes
verbatim to m = a at a constant-a window: from the recurrence,
a q_k = q_{k+1} - q_{k-1} (checked by hand: Pell 2*5 = 12 - 2;
bronze 3*10 = 33 - 3) — a borrow that rewrites a LOWER position, the
mechanism that killed x2 at Zeckendorf. For m != a the carry
algebra is unexplored and deliberately left unread: the slate's
risk is named below.

TRANSPLANT MARKS. P4 imports the Zeckendorf gate (a = 1) one storey
up to a >= 2 — flagged: the digit alphabet {0..a} at a >= 2 is
exactly the base-b feature that made ALL integer multiplication
readable at positional windows, so alphabet size and carry
direction are in open competition, and the slate bets on carry
direction. P2's odometer bound is adic-continuity folklore, not a
corpus row. P6's eigenvalue is imported from the period matrix, not
measured.

PREDICTIONS, FIXED BEFORE THE RUN (as observables; the rig prints
c_min(f, t) = least c <= C_MAX such that every pair with input
agreement depth >= t + c has image agreement depth >= t, or the
UNREADABLE flag when c = C_MAX fails):
  P1 (control)  f = id: c_min = 0 at every t, every window.
  P2 (odometer) f = n+1: c_min <= 2 at every window (exactly 1 at
      W1, the recorded Zeckendorf value).
  P3 (calibration) W1's full table reproduces the Zeckendorf rig's
      values: L = 0, R = 1, n+1 = 1, and 2n, 3n, n//2 UNREADABLE
      (explore_zeckendorf_window.py F1/F2).
  P4 (the gate; TRANSPLANT) at every window, f = 2n, 3n, n//2
      print UNREADABLE at every t in the top half of the t-range.
      KILL: a finite c_min plateau across the top half of the
      t-range for any integer m >= 2 at any window — read as the
      unit gate REFUTED at quadratic windows, with alphabet size /
      carry direction the real variable, not unit-ness.
  P5 (unit half) f = L (digits up by l), R (digits down by l):
      c_min(L) = 0 and c_min(R) <= l at every window.
  P6 (roof) the count R_t of realized depth-t strings grows by the
      period-matrix eigenvalue: R_{t+l}/R_t -> phi (W1), 2.414...
      (W2), 3.302... (W3), 3.732... (W4).

THE DESIGN
----------
Exhaustive over 0 <= n < N = 100000 per window, no sampling. Greedy
digit extraction ONLY — no closed form from any target law enters
the digit path. Images f(n) get their own greedy extraction.
Agreement depths by sorted-consecutive-pairs: sort n by low-first
digit string; any depth-d group holding two image-t-prefixes holds
a CONSECUTIVE such pair, so one pass over consecutive pairs yields
A(t) = the deepest input agreement realized by a pair whose images
differ before depth t, and c_min(t) = max(0, A(t) - t + 1), flagged
UNREADABLE past C_MAX. T_MAX = 10, C_MAX = 10, strings read to
depth 22.

E1  DIGIT SANITY. Greedy digits reconstruct n exactly (hard check)
    and satisfy the classical Ostrowski legality above (convention
    cross-check), all n < N, all windows. Positive controls
    c_min(id) = 0 and the P3 calibration row print before any gate
    verdict is read.
E2  THE GATE TABLE. c_min(f, t) for f in {n+1, 2n, 3n, n//2} over
    t = 1..T_MAX, each window; growth vs plateau flagged per the P4
    kill.
E3  THE UNIT FAMILY. c_min(L, t), c_min(R, t) with l = the window's
    CF period (L: b'_{k+l} = b_k, value sum b_k q_{k+l}; R: drops
    the l low digits, value sum_{k>=l} b_k q_{k-l}).
E4  THE ROOF. R_t = distinct realized depth-t prefixes, t <= T_MAX,
    with the R_{t+l}/R_t tail against P6's eigenvalues.
E5  EXTREMAL WITNESSES. For f = 2n at each window: the deepest
    input-agreement pair whose images differ at the first
    non-vacuous depth, printed as integers — the seed the storey's
    proof leg would grow a comb family from.
E6  RANGE SCALING (designed after E2's first run printed, its
    prediction frozen BEFORE its own run). E2's first run showed
    the a >= 2 gate columns are DATA-CAP-shaped: at N = 100000 the
    deepest realizable pair agreement (the cap) is ~13 at W2, 9 at
    W3, ~18 at W4 — every integer below N is nearly determined by its
    low digits, so a '>' there cannot separate "delay grows with
    range" (unreadable) from a genuine bounded plateau (readable).
    The separating observable: for N in {30000, 100000, 300000},
    print CAP(N) = the deepest realized pair agreement, and for
    f in {2n, 3n, n//2} the witness depth A(N) = the deepest
    agreement among pairs whose images differ at the first
    non-vacuous depth. PREDICTION P7 (frozen): A(N) tracks CAP(N)
    within 2 at every window as N grows — the gate binds, delay
    unbounded. KILL: A(N) freezing while CAP(N) rises by >= 3 at
    any window/map — a readable plateau, the P4 kill firing at
    range scale.

RESOURCE: estimate ~2 min base + ~4 min E6, trivial memory (digit
strings as bytes, ~3 MB per window at N = 100000).

RUN RECORD
----------
Two runs: E1-E5 first (all sanity green, controls green before any
verdict), then E6 added with P7 frozen and the whole rig rerun
(E1-E5 output byte-identical). Minutes, trivial memory. E1: zero
reconstruction failures, zero legality failures, all four windows.

FINDINGS (each at its own tier)
-------------------------------
F1  THE UNIT FAMILY READS AT EVERY WINDOW (rule at scanned scope).
    id = 0 everywhere; n+1 <= 1 at every window (the odometer);
    L = 0 uniformly; R bounded, alternating 1,2 at period 1 and
    2,3 at W4 (period 2) — every unit-family map readable at
    bounded delay. P1, P2, P5's qualitative half land; P5's frozen
    numeric bound c_min(R) <= l MISSED at a >= 2: dropping the low
    digit block can leave an illegal string (b_1 = a_2 lands on a
    b_0 slot capped at a_1 - 1), and the renormalization carry
    costs one extra digit — R's true bound is l + 1, parity-striped.
F2  THE GATE BINDS EVERY TESTED NON-UNIT AT EVERY WINDOW (rule at
    scanned scope; the E6 discriminator is the evidence). 2n, 3n,
    n//2: at W1 unreadable at every c <= 10 for t >= 2 (matching
    the Zeckendorf rig; the x2 half there is theorem). At W2/W3/W4
    the E2 columns are data-cap-shaped as E6's preamble says, and
    E6 separates the readings: A(N) tracks CAP(N) within 1 at
    every window, every map, every N in {30k, 100k, 300k}
    (W2: caps 11/13/14, A(2n) 11/12/13; W3: caps 8/9/10, A 8/9/9;
    W4: caps 16/17/19, A 15/17/19; W1: caps 22/24/26, A tracking).
    P7 lands, the kill misses everywhere: the delay grows with the
    range at every quadratic window — no plateau. P4's transplant
    resolved in the slate's favor: the digit alphabet {0..a} does
    NOT rescue integer multiplication — carry direction wins.
F3  THE CALIBRATION LANDS, WITH ONE MAP MISMATCH FOUND POST-RUN
    (honest miss, filed). W1 reproduces the Zeckendorf values for
    n+1 (1), L (0), and the gated maps — but this rig's R at W1 is
    NOT the Zeckendorf rig's R: with q_0 = q_1 = 1, dropping b_0
    (identically 0) keeps d_2 at weight q_0 = 1, where the
    Zeckendorf R drops d_2 itself. The measured alternating 1,2 is
    this map's own value, not a discrepancy in the recorded 1; the
    P3 freeze named the wrong map for R. Law unaffected: both maps
    are unit-family and both read bounded.
F4  THE ROOF GROWS BY THE UNIT (rule at scanned scope). R_t at W1
    is Fibonacci (1 2 3 5 8 ...); ratio tails 1.618 (W1), 2.4142
    (W2), 3.3028 (W3), 3.7320 (W4, per-period) — each the
    period-matrix eigenvalue, i.e. the fundamental unit of the
    window's order. P6 lands; W3's last ratio 2.33 is the N
    truncation (R_10 capped at N = 100000), named not hidden.
F5  THE PROOF SEED (observation, banked for the proof leg). The W2
    extremal pair (40390, 73851) differs by exactly q_12 = 33461,
    and 2 q_12 = q_13 - q_11 (the down-borrow identity a q_k =
    q_{k+1} - q_{k-1} at a = 2): doubling injects a -q_{k-1}
    BORROW that cascades to the bottom digit — subtraction where
    Zeckendorf's mechanism was a down-carry. The witness family
    behind it is not extracted here; (0, q_K) is checked by hand
    NOT to be a witness (2 q_K is the legal digit 2 at K), so the
    borrow needs receptive low digits, as the Zeckendorf comb did.
    (Settled: the family is the even Pell comb and the theorem is
    proved — explore_silver_discontinuity.py; this entry survives
    as the seed record.)

THE READING. The third storey's answer at its tested scope: at
every tested real quadratic Ostrowski window the completion is an
ODOMETER — never a ring (integer multiplication gated), never
discrete (infinite cells, the roof grows by the unit). The
trichotomy's ring cell stays exclusive to non-unit rational bases
(b-adic), the discrete cell to the unit positional base (Bergman);
the whole quadratic Ostrowski family sits in the odometer cell.
And the gate tracks the unit group of the order at the scope
tested: the readable multiplication-like maps are the shift action
of the fundamental unit (phi, 1+sqrt(2), (3+sqrt(13))/2,
2+sqrt(3) — each the unit of its window's order) and the odometer
n+1, while every rational integer m >= 2 — a unit in NONE of these
orders — is gated, with delay growing with range (E6). Beyond
these four windows the statement stays the conjecture it was.
(Settled since: explore_constant_a_borrow.py proves the xa half at
EVERY constant-a window, a >= 2, and explore_period2_borrow.py at
every [0; 1, a, 1, a, ...] period-2 window — so all four windows
here carry proved cells; the unit-gate statement's other halves,
and every other window, stay as stated.)
"""

import sys
from fractions import Fraction

T_MAX = 10
C_MAX = 10
DEPTH = T_MAX + C_MAX + 2   # input-string read depth
N = 100_000

WINDOWS = [
    ("W1 phi        [0;1,1,1,...]", [1]),
    ("W2 silver     [0;2,2,2,...]", [2]),
    ("W3 bronze     [0;3,3,3,...]", [3]),
    ("W4 sqrt3-1    [0;1,2,1,2,..]", [1, 2]),
]


def build_q(tail, top_value):
    """Weights q_0=1, q_1=a_1, q_k = a_k q_{k-1} + q_{k-2}; a_k =
    tail[(k-1) % len(tail)]. Extended until q exceeds top_value."""
    q = [1]
    a1 = tail[0]
    q.append(a1)
    k = 2
    while q[-1] <= top_value:
        a_k = tail[(k - 1) % len(tail)]
        q.append(a_k * q[-1] + q[-2])
        k += 1
    return q


def greedy_digits(v, q):
    """Greedy Ostrowski digits of v >= 0, low-to-high list, len(q)."""
    d = [0] * len(q)
    for k in range(len(q) - 1, -1, -1):
        if q[k] <= v:
            b = v // q[k]
            d[k] = b
            v -= b * q[k]
    return d


def legality_failures(d, tail):
    """Count violations of the classical Ostrowski conditions."""
    fails = 0
    a1 = tail[0]
    if d[0] > a1 - 1:
        fails += 1
    for k in range(1, len(d)):
        a_next = tail[k % len(tail)]        # a_{k+1} = tail[((k+1)-1) % l]
        if d[k] > a_next:
            fails += 1
        if d[k] == a_next and d[k - 1] != 0:
            fails += 1
    return fails


def run_window(name, tail):
    print("=" * 72)
    print(name)
    ell = len(tail)
    # q long enough for the largest image: L multiplies by ~eig^ell; 3n.
    q = build_q(tail, 8 * N * (4 ** ell))
    nq = len(q)

    # E1: full digits per n, reconstruction + legality.
    digits = []
    recon_fail = legal_fail = 0
    for n in range(N):
        d = greedy_digits(n, q)
        if sum(d[k] * q[k] for k in range(nq) if d[k]) != n:
            recon_fail += 1
        legal_fail += legality_failures(d, tail)
        digits.append(bytes(d))
    print(f"E1 digit sanity: reconstruction failures {recon_fail}, "
          f"legality failures {legal_fail}  (n < {N})")

    strings = [d[:DEPTH] for d in digits]
    order = sorted(range(N), key=lambda i: strings[i])

    def img_string(v):
        return bytes(greedy_digits(v, q)[:T_MAX])

    def shift_L(i):
        d = digits[i]
        return sum(d[k] * q[k + ell] for k in range(nq - ell) if d[k])

    def shift_R(i):
        d = digits[i]
        return sum(d[k] * q[k - ell] for k in range(ell, nq) if d[k])

    maps = [
        ("id",   lambda i: i),
        ("n+1",  lambda i: i + 1),
        ("L",    shift_L),
        ("R",    shift_R),
        ("2n",   lambda i: 2 * i),
        ("3n",   lambda i: 3 * i),
        ("n//2", lambda i: i // 2),
    ]

    print(f"E2/E3 c_min(f, t), t = 1..{T_MAX}  "
          f"('>' = UNREADABLE at c = {C_MAX}):")
    witness_2n = None
    for fname, f in maps:
        imgs = [img_string(f(i)) for i in range(N)]
        # A[t] = deepest input agreement among pairs with image
        # disagreement before depth t; witness pair tracked for 2n.
        A = [-1] * (T_MAX + 1)
        wit = [None] * (T_MAX + 1)
        for j in range(N - 1):
            i1, i2 = order[j], order[j + 1]
            s1, s2 = strings[i1], strings[i2]
            p = 0
            while p < DEPTH and s1[p] == s2[p]:
                p += 1
            u1, u2 = imgs[i1], imgs[i2]
            dpos = 0
            while dpos < T_MAX and u1[dpos] == u2[dpos]:
                dpos += 1
            if dpos < T_MAX:
                for t in range(dpos + 1, T_MAX + 1):
                    if p > A[t]:
                        A[t] = p
                        wit[t] = (i1, i2)
        row = []
        for t in range(1, T_MAX + 1):
            c = max(0, A[t] - t + 1)
            row.append(">" if c > C_MAX else str(c))
        print(f"  {fname:5s} " + " ".join(f"{x:>2s}" for x in row))
        if fname == "2n":
            # first non-vacuous depth: 2 at W1 (b_0 vacuous), else 1
            t0 = 2 if tail == [1] else 1
            witness_2n = (A[t0], wit[t0], t0)

    # E4: roof.
    print("E4 roof: realized depth-t prefix counts R_t and "
          f"R_(t+{ell})/R_t tail:")
    R = []
    for t in range(1, T_MAX + 1):
        R.append(len({s[:t] for s in strings}))
    print("  R_t: " + " ".join(str(x) for x in R))
    tail_ratios = [R[t + ell - 1] / R[t - 1]
                   for t in range(T_MAX - ell - 2, T_MAX - ell + 1)]
    print("  ratio tail: " + " ".join(f"{r:.4f}" for r in tail_ratios))

    # E5: extremal 2n witness.
    if witness_2n and witness_2n[1]:
        depth_a, (w1, w2), t0 = witness_2n
        print(f"E5 witness (2n, t = {t0}): pair ({w1}, {w2}) agrees to "
              f"input depth {depth_a}, doubles differ before depth {t0}")
    print()


def e6_range_scaling():
    """E6: CAP(N) vs witness depth A(N) for the gated maps."""
    DEPTH6 = 30
    print("=" * 72)
    print("E6 RANGE SCALING: CAP(N) and witness depth A(N), "
          "maps 2n / 3n / n//2")
    for name, tail in WINDOWS:
        t0 = 2 if tail[0] == 1 else 1   # first non-vacuous depth
        print(name)
        for N6 in (30_000, 100_000, 300_000):
            q = build_q(tail, 8 * N6 * (4 ** len(tail)))
            digs = [greedy_digits(n, q) for n in range(N6)]
            strs = [bytes(d[:DEPTH6]) for d in digs]
            order = sorted(range(N6), key=lambda i: strs[i])
            # common prefix of consecutive sorted strings
            pref = []
            for j in range(N6 - 1):
                s1, s2 = strs[order[j]], strs[order[j + 1]]
                p = 0
                while p < DEPTH6 and s1[p] == s2[p]:
                    p += 1
                pref.append(p)
            cap = max(pref)
            row = [f"CAP {cap:2d}"]
            for fname, f in (("2n", lambda i: 2 * i),
                             ("3n", lambda i: 3 * i),
                             ("n//2", lambda i: i // 2)):
                imgs = [bytes(greedy_digits(f(i), q)[:t0])
                        for i in range(N6)]
                A = -1
                for j in range(N6 - 1):
                    if (imgs[order[j]] != imgs[order[j + 1]]
                            and pref[j] > A):
                        A = pref[j]
                row.append(f"A({fname}) {A:2d}")
            print(f"  N = {N6:6d}: " + "  ".join(row))
    print()


def main():
    for name, tail in WINDOWS:
        run_window(name, tail)
    e6_range_scaling()


if __name__ == "__main__":
    main()
