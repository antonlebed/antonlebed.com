"""Where does the flip of x m sit at a window whose continued fraction is
NOT periodic -- is the address bounded there at all, and by what?

THE QUESTION
------------
At every periodic window the flip address of x m is a theorem
(explore_witness_family.py D1-D3): the raised-top family n = (q_K - 1)/m
against its top raised by one cap has images straddling the cut -alpha,
and the two codings of -alpha part at the lowest admissible digit. The
derivation consults periodicity exactly ONCE -- to make m | q_K - 1
recur, the pair (q_K, q_{K-1}) mod m advancing by an invertible matrix
per period. Off periodicity no automaton exists and nothing makes
q_K = 1 mod m recur. Does the same argument run at whatever residue
q_K mod m DOES take infinitely often, and what address does it read?

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
Notation: alpha = [0; a_1, a_2, ...] irrational, q_{-1} = 0, q_0 = 1,
q_k = a_k q_{k-1} + q_{k-2}, p_{-1} = 1, p_0 = 0, same recurrence;
theta_k = q_k alpha - p_k, sign (-1)^k, |theta_k| = ||q_k alpha||,
|theta_{k+2} / theta_k| < 2/3 at every k (explore_witness_family.py
D1). The star of an integer N is N alpha mod 1 taken in [-alpha,
1 - alpha), equal to the star value sum b_k theta_k of its greedy
string. The cuts -- the circle points with two legal codings -- are
-t alpha, t >= 1.

D1  THE CELLS ARE THE THREE-DISTANCE ARCS. Telescoping a_{k+1}
    theta_k = theta_{k+1} - theta_{k-1} over one parity, the legal
    tails from position d range over [-|theta_d|, |theta_{d-1}|] (d
    even; mirrored at d odd), shrinking by |theta_d| at the top when
    the digit below is nonzero. So the depth-d cell of a prefix of
    value n_P < q_d is the arc n_P alpha + [tail range]: q_{d-1} cells
    of length |theta_{d-1}| + |theta_d| and q_d - q_{d-1} of length
    |theta_{d-1}|, summing to 1; they tile the circle (the star map is
    continuous on the compact string space and hits the dense set
    n alpha). At d even the left endpoints are (n_P - q_d) alpha =
    -(q_d - n_P) alpha; at d odd the same set is the right endpoints.
    THE CUT SET AT DEPTH d IS {-t alpha : 1 <= t <= q_d} -- the
    hand-check explore_witness_family.py D2 made at golden depth 3 is
    a theorem.
D2  THE PARTING DEPTH. -t alpha separates two DISTINCT depth-(p+1)
    cells iff t <= q_{p+1} and q_{p+1} >= 2 (with one cell the cut is
    the wrap point of the single arc, not a boundary between two).
    So the two codings of -t alpha part at
        p_t = min{ p >= 0 : q_{p+1} >= max(t, 2) }.
    Golden: p_1 = p_2 = 1 (q_2 = 2), p_3 = 2 -- the b_1 of the x 3
    witness and the b_2 of D4 there. p_1 = 0 iff a_1 >= 2, else 1:
    the lowest admissible digit, at every window.
D3  WHAT ANY WITNESS IS. A witness family for x m has inputs n, n'
    agreeing to depth D -> infinity and images m n, m n' parting at a
    fixed p. Then some cut -t alpha with t <= q_{p+1} lies between the
    images, both within 2m |theta_{D-1}| of it (the inputs share a
    depth-D cell, of length under 2 |theta_{D-1}|): Y = m n + t and
    Y' = m n' + t have tiny stars of opposite signs, hence zero low
    digits (0's depth-d cell contains the ball of radius |theta_d|).
    Write Y alpha = P_Y + star(Y) with P_Y the nearest integer. Then
    n alpha = (P_Y + star(Y) - t alpha) / m converges to the point
    c_r = (r - t alpha) / m with r = P_Y mod m. Inputs converging to
    a common c_r off the cuts agree ever deeper; inputs converging to
    different limits agree to a bounded depth only; and c_r is a cut
    only at (t, r) = (m, 0), where c = -alpha and n alpha = -alpha +
    star(Y)/m puts each input on the side of ITS image, so the two
    inputs part at p_1 themselves. So a witness at the cut -t alpha
    is exactly a residue PAIR (Y, P_Y) mod m = (t, r) != (m, 0)
    realized by zero-low-digit Y with star -> 0 from BOTH sides; it
    parts at p_t; the address is the least p_t over the realized t.
D4  EVERY PAIR IS REALIZED, AT EVERY IRRATIONAL WINDOW. A zero-low-
    digit Y = sum c_i q_{k_i} has pair sum c_i (q_{k_i}, p_{k_i}) mod
    m. Consecutive convergents are UNIMODULAR -- q_k p_{k+1} - q_{k+1}
    p_k = +-1 -- so the two pairs at any k, k+1 span (Z/m)^2: every
    (t, r) is a (q_k, p_k) + b (q_{k+1}, p_{k+1}) with 0 <= a, b < m,
    uniquely. No recurrence hypothesis at all. The "recurring residue
    set" this file's first pass named was the artifact of using ONE
    convergent where two are unimodular; the raised-top family is the
    sub-case a = b = 0 with q_K itself = 1 mod m.
D5  THE EXPLICIT FAMILY at the cut -alpha, r = 0. For K >= 0 put
    K' = K + 4, let (a_K, b_K) in [0, m)^2 solve
        a (q_{K'}, p_{K'}) + b (q_{K'+1}, p_{K'+1}) = (1, 0) mod m,
    and set Y_K = m q_K + a_K q_{K'} + b_K q_{K'+1}, n_K = (Y_K - 1)/m.
    Then Y_K = 1 and P_{Y_K} = 0 mod m. The star: m theta_K plus a
    remainder of modulus at most 2 (m - 1) |theta_{K+4}| < (8/9)
    (m - 1) |theta_K| < m |theta_K|, so star(Y_K) has the sign (-1)^K
    and modulus in (|theta_K|, (2m - 1) |theta_K|). The images
    m n_K = Y_K - 1 sit beside -alpha on the side (-1)^K, consecutive
    K on opposite sides, within (2m - 1) |theta_K| of it -- the raised
    top's own bound; at every depth d with |theta_{d-1}| > (2m - 1)
    |theta_K| -- every d <= K - c_m -- no other cut is nearer (best
    approximation: ||j alpha|| >= |theta_{d-1}| for 0 < |j| < q_d),
    so the images' depth-d cells are the two neighbours of -alpha, its
    two codings: they part at EXACTLY p_1 once K >= p_1 + 1 + c_m.
    The inputs: n_K alpha = -alpha/m + star(Y_K)/m mod 1, all within
    (2m - 1) |theta_K| / m of the point -alpha/m, which is never a
    cut; the depth-d cell of -alpha/m contains the ball of radius
    (1/m) min_{0 < j < m q_d} ||j alpha|| >= |theta_{d+c}| / m with
    q_{d+c+1} > m q_d, so n_K and n_{K+1} agree to a depth >= K - c'
    -> infinity. With q_{d+6} >= 13 q_d and |theta_{K-2j}| > (3/2)^j
    |theta_K|, c' <= 20 at m <= 7 (loose; the print sits far above
    it). The slate below was frozen at 18 off a first pass that
    bounded the star by (m + 1) |theta_K|, which holds only at m = 2;
    the print's slack of 5 clears both figures.
    THEOREM (x m). At every irrational window and every m >= 2 the
    x m column is unbounded from depth p_1 + 1: the flip address is
    the lowest admissible digit, with no periodicity anywhere.
D6  THE FLOORS. Inputs x_0 + Y and x_0 + Y' with Y, Y' zero-low-digit
    of DIFFERENT residue pairs converge to x_0 alpha, never a cut, so
    they agree deeply; the images floor((x_0 + Y)/m) converge to
    ((x_0 - rho) alpha + r) / m with rho = (x_0 + t) mod m -- the jump
    of explore_witness_family.py L4, now general -- and two pairs
    (t, r) != (t', r') give limit points a FIXED nonzero rotation
    apart. Take Y = m q_K, pair (0, 0), and Y' = m q_K + q_{K+4},
    pair (q_{K+4}, p_{K+4}) mod m != (0, 0) since gcd(q, p) = 1. As
    x_0 steps by m both limits rotate by alpha, densely; the depth-
    (p_1 + 1) partition has q_{p_1+1} >= 2 arcs, and a dense orbit
    cannot keep a fixed nonzero displacement inside one arc (C minus
    (C - delta) is a nonempty open set): some x_0 puts the two limits
    in different depth-(p_1 + 1) cells off the cuts, and the depth-p_1
    partition is one cell. THEOREM (floors): the same address at
    every irrational window, by the same macroscopic tear.
D7  THE DESIGNED TAIL. A window where q_K = 1 mod m NEVER recurs
    kills the raised-top route while D5 runs unchanged: a_1 = 2, and
    for k >= 2 a_k the least a >= u_k (u_k the Sturmian word
    floor((k+1) sqrt 2) - floor(k sqrt 2) in {1, 2}) with a q_{k-1} +
    q_{k-2} != 1 mod m -- possible at every m >= 3 (when q_{k-1} = 0
    mod m the residue is q_{k-2}'s, already != 1; otherwise at most
    one class of a is bad, so a <= u_k + 1). At m = 2 no window
    avoids q_K odd (consecutive denominators are coprime), so the
    designed tail exists at m = 3..7 only.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean). Agreement of two strings is the number of
low positions on which they agree; parting is the first position on
which they differ. p_1 = 0 at a_1 >= 2 and 1 at a_1 = 1.
  C1 (controls, run FIRST; nothing below is read if any is red)
      (a) positive: the D5 family at the golden window, m = 3, 5, 7,
      parts at exactly 1 at every K >= 8, and at bronze, m = 2, at
      exactly 0 -- the shipped periodic address; (b) negative: the
      SAME-parity pair (n_K, n_{K+2}) at e - 2, m = 2..7, has images
      agreeing to depth >= K - 18 at every K (same side of the cut:
      no witness); (c) the designed tails at m = 3..7 print q_k != 1
      mod m at every k >= 2 built, and have no period <= 20 over the
      terms built; (d) the (a_K, b_K) solve is unique at every K read
      (unimodularity as an assert).
  P1  THE FAMILY AT THE APERIODIC WINDOWS. At e - 2 and cbrt(2) - 1,
      m = 2..7, and at the designed tail for m = 3..7, at every K from
      8 to the top of the certified ladder: the inputs n_K, n_{K+1}
      agree to depth >= K - 18, and the images part at EXACTLY p_1.
      KILL: a parting != p_1 at any K >= 8, or an agreement below
      K - 18.
  P2  THE FLOORS. Same windows and m, K = 8, 12, 16, ...: some x_0 <
      3000 gives inputs x_0 + m q_K, x_0 + m q_K + q_{K+4} agreeing
      to depth >= K - 18 with images floor(./m) parting at EXACTLY
      p_1. KILL: no such x_0 at some K.
  P3  THE SCAN'S HALF (the instrument the storey used off
      periodicity, explore_nonquadratic_window.py). The finite-range
      lookahead c_N(p_1 + 1) of x 2, x 3, floor(n/2), floor(n/3) at
      e - 2 and cbrt(2) - 1 rises by at least 1 from N = 10^4 to
      N = 10^5. KILL: flat across the decade.

THE DESIGN
----------
Certified quotients, greedy digits and the weight builder are imported
from explore_nonquadratic_window.py (its W1 and W2). p_k is built
beside q_k. Everything is exact integer arithmetic: the inputs and
images are integers, their greedy strings are read against a weight
table built past the top of every number used, and agreement and
parting are read off the strings -- no float enters a verdict. Stages
(argv): s0 controls, s1 the x m family, s2 the floors, s3 the scan's
half, all by default. Each stage is bounded (under a minute
estimated, far under the memory ceiling) and rerunnable.

FINDINGS (each at its own tier)

L1  THE CONTROLS ARE GREEN. (a) The D5 family parts at exactly 1 at
    golden m = 3, 5, 7 and at exactly 0 at bronze m = 2, at every K
    from 8 to 56 -- the shipped periodic address, recovered by the
    new family with no raised cap. (b) The same-parity pair at e - 2,
    m = 2..7, never witnesses: its images agree to 7 at K = 8 and
    within 2 of K at every K read after (16, 23, 31, 40, 47, 53 at
    m = 2 for K = 16..54 by eights; 16, 22, 31, 40, 46, 52 at m = 5).
    (c) The designed tails hold q_k != 1
    mod m at every k >= 2 of the 70 built, at m = 3..7, with no
    period <= 20 (at m = 3 the residues are {0, 2} only). (d) The
    unimodular solve was unique at every K read.
L2  THE FAMILY WITNESSES EVERY APERIODIC CELL (rule at 17 cells x 49
    K; the derivation D1-D5 a theorem). At e - 2 (p_1 = 1), cbrt(2)
    - 1 (p_1 = 0) and the five designed tails (p_1 = 0), every m, at
    every K = 8..56: the images part at EXACTLY p_1 -- no other
    value printed anywhere -- and the inputs agree to a depth in
    [K - 5, K], rising from 4..8 at K = 8 to 51..56 at K = 56. The
    derived slack 18 is loose by a factor above 3. P1 confirmed at
    833 readings, 0 off. The designed tails are the cell the
    raised-top family cannot enter at all, and the address there is
    the same.
L3  THE FLOORS' JUMP FINDS ITS x_0 BELOW 29 EVERYWHERE (rule at 17
    cells x 13 K; D6 a theorem). Some x_0 < 29 -- and 0 at 126 of the
    221 readings -- puts the two limit points in different depth-
    (p_1 + 1) cells at every K = 8, 12, ..., 56 at every window and
    every m, the images parting at exactly p_1 with the inputs
    agreeing past K - 18. P2 confirmed, 0 off; the scan's ceiling
    3000 was never approached.
L4  THE SCAN AGREES (pattern at scanned scope). c_N(p_1 + 1) rises by
    1 or 2 from N = 10^4 to 10^5 at all eight (window, map) cells:
    10 -> 11 and 10 -> 12 for x 2 and x 3 at e - 2, 9 -> 11 for both
    at cbrt(2) - 1, the floors 11 -> 12 and 10 -> 12. P3 confirmed.
    The finite reading is the lower bound the theorem says it is,
    at the depth the theorem names.

THE READING. The flip address of x m and of floor(n/m) is the lowest
admissible digit at EVERY irrational window and every m >= 2: a
theorem with no periodicity in it. What periodicity had bought was
q_K = 1 mod m recurring, and that was the price of witnessing with a
single convergent; two consecutive convergents are unimodular, every
residue pair is a bounded combination of them at every K, and the
witness is then an explicit family at every window. The storey's one
open front at the address closes; the recurring-residue object of
this file's first pass never existed.

RUN RECORD (the estimate first, then what it cost)
Under a minute estimated for all four stages; s0 under 0.1 s, s1-s3
23 s wall together (s3 the whole of it: two greedy strings for each
of 10^5 inputs at eight cells). Pure Python, standard library, exact
integers throughout; memory far below the ceiling (the largest table
10^5 digit tuples of 71 positions). Each stage ran once.
"""

import os
import sys
from math import isqrt

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_nonquadratic_window import (  # noqa: E402
    greedy, quotients_cbrt2_minus_1, quotients_e_minus_2)

WANT = 70
MS = range(2, 8)
K_FIRST = 8
SLACK = 18          # the loose agreement bound of D5
X_TOP = 3000        # the floors' x_0 scan
POS_EXTRA = 12      # weight positions above the largest K read


def build_qp(a, npos):
    """q_0..q_npos and p_0..p_npos from the 1-indexed quotients a."""
    q = [1, a[0]]
    p = [0, 1]
    while len(q) <= npos:
        k = len(q)
        q.append(a[k - 1] * q[-1] + q[-2])
        p.append(a[k - 1] * p[-1] + p[-2])
    return q, p


def designed_tail(m, want):
    """D7: a_1 = 2, then the least a >= u_k with q_k != 1 mod m."""
    a = [2]
    q = [1, 2]
    for k in range(2, want + 1):
        u = isqrt(2 * (k + 1) ** 2) - isqrt(2 * k * k)   # in {1, 2}
        x = u
        while (x * q[-1] + q[-2]) % m == 1:
            x += 1
        a.append(x)
        q.append(x * q[-1] + q[-2])
    return a


def least_period(a, top):
    for P in range(1, top + 1):
        if all(a[k] == a[k + P] for k in range(len(a) - P)):
            return P
    return None


def agreement(d1, d2):
    for i, (x, y) in enumerate(zip(d1, d2)):
        if x != y:
            return i
    return len(d1)


def solve_ab(q, p, k, m, target=(1, 0)):
    """The unique (a, b) in [0, m)^2 with a (q_k, p_k) + b (q_{k+1},
    p_{k+1}) = target mod m (D4)."""
    sols = [(a, b) for a in range(m) for b in range(m)
            if ((a * q[k] + b * q[k + 1]) % m == target[0] % m
                and (a * p[k] + b * p[k + 1]) % m == target[1] % m)]
    assert len(sols) == 1, (k, m, sols)
    return sols[0]


def family_input(q, p, K, m):
    """D5: n_K = (m q_K + a q_{K+4} + b q_{K+5} - 1) / m."""
    a, b = solve_ab(q, p, K + 4, m)
    Y = m * q[K] + a * q[K + 4] + b * q[K + 5]
    assert Y % m == 1
    return (Y - 1) // m


def p1_of(a):
    return 0 if a[0] >= 2 else 1


class Win:
    def __init__(self, name, a):
        self.name = name
        self.a = a
        self.q, self.p = build_qp(a, len(a))
        self.p1 = p1_of(a)
        self.k_top = len(a) - POS_EXTRA - 1

    def digits(self, v):
        return greedy(v, self.q)


def windows():
    ws = {
        "golden": Win("golden [1,1,1,...]", [1] * WANT),
        "bronze": Win("bronze [3,3,3,...]", [3] * WANT),
        "e-2": Win("e - 2 (certified)", quotients_e_minus_2(WANT)),
        "cbrt": Win("cbrt(2) - 1 (certified)", quotients_cbrt2_minus_1(WANT)),
    }
    for m in range(3, 8):
        ws["designed%d" % m] = Win("designed tail, m = %d" % m,
                                   designed_tail(m, WANT))
    return ws


def read_family(w, m, K, step=1):
    n1 = family_input(w.q, w.p, K, m)
    n2 = family_input(w.q, w.p, K + step, m)
    ag = agreement(w.digits(n1), w.digits(n2))
    im = agreement(w.digits(m * n1), w.digits(m * n2))
    return ag, im


def s0_controls(ws):
    print("== s0 controls ==")
    ok = True
    for name, ms, want in (("golden", (3, 5, 7), 1), ("bronze", (2,), 0)):
        w = ws[name]
        for m in ms:
            parts = [read_family(w, m, K)[1] for K in range(K_FIRST, w.k_top)]
            good = all(x == want for x in parts)
            ok &= good
            print("C1(a) %-20s m=%d parting over K=%d..%d: %s -> %s"
                  % (w.name, m, K_FIRST, w.k_top - 1,
                     sorted(set(parts)), "OK" if good else "RED"))
    w = ws["e-2"]
    for m in MS:
        worst = None
        for K in range(K_FIRST, w.k_top - 1):
            ag, im = read_family(w, m, K, step=2)
            gap = im - (K - SLACK)
            if worst is None or gap < worst[0]:
                worst = (gap, K, ag, im)
        good = worst[0] >= 0
        ok &= good
        print("C1(b) e-2 m=%d same-parity pair: min(image agreement - "
              "(K - 18)) = %d at K=%d (inputs agree %d, images %d) -> %s"
              % (m, worst[0], worst[1], worst[2], worst[3],
                 "OK" if good else "RED"))
    for m in range(3, 8):
        w = ws["designed%d" % m]
        res = [w.q[k] % m for k in range(2, len(w.q))]
        never1 = 1 not in res
        per = least_period(w.a, 20)
        ok &= never1 and per is None
        print("C1(c) designed m=%d a_1..a_30 = %s ; q_k mod m over k>=2 "
              "takes %s (1 absent: %s); least period <= 20: %s -> %s"
              % (m, "".join(str(x) for x in w.a[:30]), sorted(set(res)),
                 never1, per, "OK" if (never1 and per is None) else "RED"))
    print("C1(d) unimodular solve: asserted inside every family call")
    print("s0 verdict:", "GREEN" if ok else "RED")
    return ok


def s1_family(ws):
    print("== s1 the x m family at the aperiodic windows ==")
    kills = 0
    cells = [(ws["e-2"], m) for m in MS] + [(ws["cbrt"], m) for m in MS]
    cells += [(ws["designed%d" % m], m) for m in range(3, 8)]
    for w, m in cells:
        rows = []
        for K in range(K_FIRST, w.k_top):
            ag, im = read_family(w, m, K)
            rows.append((K, ag, im))
            if im != w.p1 or ag < K - SLACK:
                kills += 1
        parts = sorted(set(r[2] for r in rows))
        slack = min(r[1] - r[0] for r in rows)
        print("%-26s m=%d p1=%d K=%d..%d: parting %s; input agreement - K "
              "in [%d, %d]; first/last agreement %d/%d"
              % (w.name, m, w.p1, rows[0][0], rows[-1][0], parts, slack,
                 max(r[1] - r[0] for r in rows), rows[0][1], rows[-1][1]))
    print("s1 kills:", kills)
    return kills == 0


def floors_pair(w, m, K, x0):
    n1 = x0 + m * w.q[K]
    n2 = n1 + w.q[K + 4]
    ag = agreement(w.digits(n1), w.digits(n2))
    im = agreement(w.digits(n1 // m), w.digits(n2 // m))
    return ag, im


def s2_floors(ws):
    print("== s2 the floors ==")
    kills = 0
    cells = [(ws["e-2"], m) for m in MS] + [(ws["cbrt"], m) for m in MS]
    cells += [(ws["designed%d" % m], m) for m in range(3, 8)]
    for w, m in cells:
        found = []
        for K in range(K_FIRST, w.k_top, 4):
            hit = None
            for x0 in range(X_TOP):
                ag, im = floors_pair(w, m, K, x0)
                if im == w.p1 and ag >= K - SLACK:
                    hit = (x0, ag)
                    break
            if hit is None:
                kills += 1
            found.append((K, hit))
        print("%-26s m=%d p1=%d: least x0 per K %s"
              % (w.name, m, w.p1,
                 " ".join("%d:%s" % (K, "NONE" if h is None else h[0])
                          for K, h in found)))
    print("s2 kills:", kills)
    return kills == 0


def c_finite(w, imgs_of, t, N):
    """c_N(t): least c with every input pair agreeing to >= t + c
    having images agreeing to >= t; read as the max input agreement
    over pairs whose images differ below t, minus t, plus 1."""
    depth = len(w.q)
    ins = [tuple(w.digits(n)) for n in range(N)]
    outs = [tuple(w.digits(imgs_of(n))[:t]) for n in range(N)]
    for D in range(depth, -1, -1):
        seen = {}
        for i in range(N):
            key = ins[i][:D]
            o = outs[i]
            prev = seen.get(key)
            if prev is None:
                seen[key] = o
            elif prev != o:
                return max(0, D - t + 1)
    return 0


def s3_scan(ws):
    print("== s3 the scan's half ==")
    kills = 0
    for name in ("e-2", "cbrt"):
        w = ws[name]
        t = w.p1 + 1
        for label, f in (("x2", lambda n: 2 * n), ("x3", lambda n: 3 * n),
                         ("n//2", lambda n: n // 2), ("n//3", lambda n: n // 3)):
            cs = [c_finite(w, f, t, N) for N in (10_000, 100_000)]
            rise = cs[1] - cs[0]
            if rise < 1:
                kills += 1
            print("%-26s %-5s t=%d: c_N at N=1e4, 1e5 = %s (rise %d)"
                  % (w.name, label, t, cs, rise))
    print("s3 kills:", kills)
    return kills == 0


def main():
    stages = sys.argv[1:] or ["s0", "s1", "s2", "s3"]
    ws = windows()
    for k, w in ws.items():
        print("window %-12s %-26s positions built %d, K read to %d, p1=%d"
              % (k, w.name, len(w.q) - 1, w.k_top - 1, w.p1))
    if "s0" in stages and not s0_controls(ws):
        print("controls red: nothing below is read")
        return
    if "s1" in stages:
        s1_family(ws)
    if "s2" in stages:
        s2_floors(ws)
    if "s3" in stages:
        s3_scan(ws)


if __name__ == "__main__":
    main()
