"""
THE DROP'S COLUMN: is the digit shift down finitely readable at a
window whose quotients grow without bound but sit far below its
denominators?

THE QUESTION
------------
An Ostrowski window alpha = [0; a_1, a_2, ...] writes n = sum d_k q_k
(q_0 = 1, q_1 = a_1, q_{k+1} = a_{k+1} q_k + q_{k-1}; d_0 <= a_1 - 1,
d_k <= a_{k+1}, d_k = a_{k+1} forces d_{k-1} = 0). The DROP BY 1 deletes
the low digit: n -> sum_{k>=1} d_k q_{k-1}. Its lookahead column c(t) is
the least c-hat such that inputs sharing t + c-hat low digits have drops
sharing t low digits, infinite when none serves. At every purely periodic
window the drop's column is finite (explore_limit_maps.py L3, a rule at
four cells); at a designed Liouville-type window it is infinite from the
lowest admissible digit (explore_relation_address.py L4, a theorem). The
middle was open: e - 2 = [0; 1, 2, 1, 1, 4, 1, 1, 6, ...], whose quotients
grow linearly while its denominators grow like a factorial, read a flat
finite-range column across a decade of range (L6 there) and the paper
decided nothing.

THE HAND-ATTACK, derived before the engine
------------------------------------------
Write theta_k = q_k alpha - p_k (alternating sign, |theta_k| < 1/q_{k+1},
theta_{k+1} = a_{k+1} theta_k + theta_{k-1}); n's point is n alpha mod 1
= sum d_k theta_k, the drop's point is sum d_k theta_{k-1}.

THE CUT LEMMA. The depth-t cylinder of a head h' < q_t is the arc from
h' alpha to h' alpha plus the closure of the tail stars, whose endpoints
are -theta_{t-1} and -theta_t when d_{t-1} = 0 and -theta_t and
-theta_{t-1} - theta_t otherwise (the extreme strings are one parity's
full digits, telescoping); the arcs' lengths sum to q_t |theta_{t-1}| +
q_{t-1} |theta_t| = 1. So the depth-t cells are the arcs cut by EXACTLY
the points -j alpha, 1 <= j <= q_t, and two drops share t low digits iff
no such cut separates them.

THE STRADDLE. STRADDLE(s, t): some depth-s input cylinder's drops meet
two depth-t cells. It is downward closed in s, so c(t) = min{s : not
STRADDLE(s, t)} - t, infinite iff STRADDLE(s, t) at infinitely many s.

THE SWEEP CRITERION (sufficient). The first tail digit d_s in [0,
a_{s+1}] moves the drop by d theta_{s-1}, a sweep of reach a_{s+1}
|theta_{s-1}| from the head's drop h. If some legal head (drop h, with
d_{s-1} = 0 when the top digit is used) and some cut j <= q_t have
<(h + j) alpha> = -u theta_{s-1} with u in (0, a_{s+1}) and u not an
integer, the digits floor(u) and floor(u) + 1 land on opposite sides of
-j alpha within |theta_{s-1}| <= |theta_t| of it, inside the two cells
adjacent to the cut: STRADDLE(s, t) for every t <= s - 1 with at least
two cells and the cut present, q_t >= max(j, 2).
The parent rig's D5 is the case h = 0 with the sweep wrapping the circle.

THE LANDING FAMILY AT e - 2. The big digits sit at s = 3m - 2 with
a_{s+1} = 2m, a_s = a_{s-1} = 1, a_{s-2} = 2m - 2. Let
    i_m = (m - 1) q_{s-3} + q_{s-4},   h_m = i_m - 1  (j = 1, the cut -alpha).
By theta_{s-2} = (2m - 2) theta_{s-3} + theta_{s-4} the star of i_m is
theta_{s-2} - (m - 1) theta_{s-3}, of magnitude |theta_{s-2}| + (m - 1)
|theta_{s-3}| = (2m - 1)|theta_{s-1}| + m|theta_s| (using |theta_{s-2}| =
|theta_{s-1}| + |theta_s| and |theta_{s-3}| = 2|theta_{s-1}| + |theta_s|)
and of sign opposite to theta_{s-1}. Adding d theta_{s-1}: at d = 2m - 1
the drop sits m|theta_s| from -alpha on one side, at d = 2m it sits
|theta_{s-1}| - m|theta_s| = m|theta_s| + |theta_{s+1}| on the other
(|theta_{s-1}| = 2m|theta_s| + |theta_{s+1}|). Both distances are below
|theta_{s-1}| <= |theta_t| for t <= s - 1, so the two drops lie in the two
cells adjacent to -alpha at every depth 2 <= t <= s - 1. The head is
drop-representable by the recursion h_m = (2m - 2) q_{s-4} + h_{m-1},
h_2 = 1 (the big digit a_{s-2} at position s - 3, legal since the cap
forces d_{s-4} = 0 and h_{m-1} uses positions <= s - 6): as an input
string, d_1 = 1, d_{3k-2} = 2k for k = 2..m-1, d_{3m-2} = 2m - 1 or 2m,
all zeros elsewhere, legal (2m = a_{s+1} needs d_{s-1} = 0, true). The
pair agrees to depth exactly s and its drops part below every t <= s - 1.
Hence THE THEOREM: at e - 2 the drop's column is infinite at every t >= 2
(t = 1 has one cell, a_1 = 1). The scan's flat column was the range's:
the m = 5 witness needs n' = h_5 + 10 q_13 = 189,349 > 10^5; at N = 3 x
10^5 the column read 12 11 10 9 at t = 2..5 (a preliminary scan), the
14 - t the m = 5 witness forces.

PREDICTIONS, FIXED BEFORE THE RUN (what the rig PRINTS)
  C1 the cut lemma, exhaustive: at six windows and t = 2..6, over all
     m < N the sorted points m alpha change depth-t digits between
     neighbours exactly where a cut -j alpha (j <= q_t) lies between
     them: 0 exceptions in both directions. KILL: any exception.
  C2 the criterion against the carry automaton (explore_limit_maps.py
     read(win, "drop", r=1), exact at every purely periodic window): at
     golden, silver and bronze the drop by 1 reads c_inf = 0 0 2 1 2 /
     0 1 2 1 2 / 0 1 2 1 2 (peak 2; golden's dead d_0 normalizes at the
     bottom), so the landing search must find NO landing at any
     s >= t + 2, t = 2, 3, s to 12, every j <= q_t. KILL: a landing
     there (the criterion is then unsound). At sqrt(3) - 1 = [1, 2] the
     automaton reads the drop by 1 INFINITE from t = 2 (the drop by the
     period 2 is the finite one); the rig prints those four automaton
     columns first: the search finds a landing at some
     s >= 5 for t = 2 and its pair, checked digit by digit, agrees to s
     with drops parting below 2 (positive control). KILL: no landing.
  E1 e - 2, m = 2..M: both witness strings legal, agreement exactly s,
     drops' digit agreement < t at every t = 2..s-1: 0 failures. The
     exact u = <(i_m) alpha> / theta_{s-1} prints as -(2m - 1) -
     m|theta_s|/|theta_{s-1}|, between -2m and -(2m - 1). KILL: any
     failure.
  K1 cbrt(2) - 1 (certified quotients): at every position s <= S with
     a_{s+1} >= 2, the exhaustive head search finds a landing on some
     depth-2 cut -j alpha (j <= q_2) at every such s from 5 on; each landing's pair
     is then checked digit by digit (as E1). Lean: landings at every
     big quotient, so c(t) >= s_max - t + 1 at scanned scope, the
     column growing with the scope. A position with a_{s+1} >= 2 and
     NO landing is printed as such and refutes nothing (the criterion
     is sufficient only).

THE DESIGN
----------
Exact integers throughout for strings, drops and digits (greedy digits
of the integer are the ground truth for every agreement). Points are
read through alpha ~ p_T/q_T at T = 96 as Fractions; every sign or
magnitude comparison asserts a margin above the convergent's error
(coefficients below 10^15 against an error below 10^-40, the margin 10^-15). The head
search enumerates every drop-representable head by a DP over positions,
capped at HEAD_CAP entries (the scope stops where the cap bites and says
so). Stages (argv): c controls, e the e - 2 theorem, k the cube root;
all by default. Bounded: minutes, far under the memory ceiling.

FINDINGS (each at its own tier; the prints copied, the asserts read)

L1  THE CUT LEMMA IS EXACT (C1: 0 exceptions at all six windows, m < 3000,
    t = 2..6, both directions). The criterion is SOUND where the column
    is known (C2): no landing at s >= t + 2 at golden, silver or bronze
    (the automaton's peak 2), and at sqrt(3) - 1 the first landing on
    -alpha sits at s = 5 (h = 3, the pair 19 and 34 agreeing to 5 with
    drops parting at 1), the automaton reading the drop by 1 infinite
    from t = 2 there. The C2 control was first written against a wrong
    premise -- golden's column read as 1 by the shift identity, which
    fails at the dead d_0 -- and against the drop by the PERIOD at
    [1, 2]; the automaton's own columns replaced both before the verdict
    was read.
L2  THE LANDING FAMILY HOLDS AT e - 2 (theorem; E1 exact at m = 2..12).
    At every m the head h_m = (2m - 2) q_{s-4} + h_{m-1} is
    drop-representable with d_{s-1} = 0, u = <(h_m + 1) alpha> /
    (-theta_{s-1}) equals (2m - 1) + m|theta_s|/|theta_{s-1}| to the
    convergent's margin (3.4410, 5.4596, 7.4693, 9.4753, 11.4794,
    13.4823, 15.4845, 17.4862, 19.4875, 21.4887, 23.4896), and the pair
    h-lift + (2m - 1) q_s, + 2m q_s agrees to depth exactly s = 3m - 2
    with drops agreeing to 1 -- parting below every t >= 2. The pairs
    reach 1.9 x 10^16 at m = 12. So the drop by 1's column at e - 2 is
    infinite at every depth t >= 2; the m = 5 pair (171266, 189355) is
    what the N = 3 x 10^5 scan met and the N = 10^5 scan could not.
L3  THE CUBE-ROOT WINDOW AT SCANNED SCOPE (observation). Landings on a
    depth-2 cut at s = 2, 5, 8, 10, 12 (a_{s+1} = 5, 4, 8, 14, 10; u =
    1.180, 3.442, 7.448, 13.805, 4.386), every pair checked digit by
    digit; the criterion silent at s = 13, 15, 16 (a_{s+1} = 2, 4, 12)
    and the head cap of 3 x 10^6 ending the scope at s = 17. So c(2) >=
    11 there, above the finite-range scan's 10 at N = 10^5; K1's lean
    of a landing at EVERY big quotient did not print, and the criterion
    being sufficient only, the silences refute nothing.

THE READING. The drop's column is decided by where a big digit's sweep
lands: a_{s+1} steps of theta_{s-1} from a head, against the cuts
-j alpha of the depth being read. Where the quotients are periodic the
heads never reach a cut's neighbourhood beyond a bounded depth; at
e - 2 every big digit lands on -alpha over a head assembled from the
big digits below it, one per storey, and the column is infinite at
every depth; a Liouville tail lands with the empty head. Growth
relative to nothing (L5 of the parent rig) was the single-digit
sweep's reach, not the column's: the heads carry the reach to the cut.

RUN RECORD (the estimate first, then what it cost)
Seconds to a minute estimated; 3 min 26 s wall, the estimate missed
by the C2 head enumerations to s = 12 at three windows and the
cube-root DP to its cap. Pure Python, standard
library, exact integers; the head DP at the cube-root window's s = 16
is the largest table, under the 3 x 10^6 cap; memory far below the
ceiling.
"""
import os
import sys
import time
from bisect import bisect_left, bisect_right
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_aperiodic_address import build_qp, agreement        # noqa: E402
from explore_nonquadratic_window import (                        # noqa: E402
    greedy, quotients_e_minus_2, quotients_cbrt2_minus_1)

WANT = 100
T_TOP = 96
HEAD_CAP = 3_000_000
M_TOP = 12
S_TOP_K = 22
N_CUT = 3000
MARGIN = Fraction(1, 10 ** 15)


class Win:
    def __init__(self, name, a):
        self.name, self.a = name, list(a)[:WANT]
        self.q, self.p = build_qp(self.a, len(self.a))
        self.al = Fraction(self.p[T_TOP], self.q[T_TOP])
        self.th = [self.q[k] * self.al - self.p[k] for k in range(T_TOP)]

    def digits(self, v):
        return greedy(v, self.q)

    def drop(self, d):
        return sum(d[k] * self.q[k - 1] for k in range(1, len(d)) if d[k])

    def legal(self, d):
        if d[0] > self.a[0] - 1:
            return False
        for k in range(1, len(d)):
            if k >= len(self.a):
                return not any(d[k:])
            if d[k] > self.a[k] or (d[k] == self.a[k] and d[k - 1] != 0):
                return False
        return True

    def frac(self, x):
        """x mod 1 in (-1/2, 1/2], asserting the convergent's margin."""
        x = x - (x.numerator // x.denominator)
        x = x if x <= Fraction(1, 2) else x - 1
        assert abs(x) > MARGIN, "a point at the convergent's error"
        return x

    def heads(self, s):
        """Every drop-representable head at positions 1..s-1 (weights
        q_0..q_{s-2}) as {value: top digit d_{s-1}}, None past the cap."""
        cur = {(0, 0)}
        for k in range(1, s):
            cap = self.a[k]
            nxt = set()
            for v, prev in cur:
                for d in range(cap + 1):
                    if d == cap and prev != 0:
                        continue
                    nxt.add((v + d * self.q[k - 1], d))
            if len(nxt) > HEAD_CAP:
                return None
            cur = nxt
        out = {}
        for v, d in cur:
            out[v] = min(out.get(v, d), d)     # prefer a head with d_{s-1} = 0
        return out

    def landing(self, s, j=1):
        """A head h and integer floor(u) with <(h + j) alpha> = -u theta_{s-1},
        0 < u < a_{s+1}, u not integral, legal for the digits used."""
        H = self.heads(s)
        if H is None:
            return "cap"
        big = self.a[s]                                  # a_{s+1}
        th = self.th[s - 1]
        best = None
        for h, top in H.items():
            u = -self.frac((h + j) * self.al) / th
            if 0 < u < big:
                c = int(u)
                assert abs(u - c) > MARGIN and abs(u - c - 1) > MARGIN
                if c + 1 == big and top != 0:
                    continue
                if best is None or u > best[1]:
                    best = (h, u, c)
        return best


def represent(w, h, s, top_zero=False):
    """Digits d_1..d_{s-1} with sum d_k q_{k-1} = h, d_k <= a_{k+1} and the
    cap rule (d_{k+1} = a_{k+2} forces d_k = 0); d_{s-1} = 0 when top_zero.
    Returns [0, d_1, ..., d_{s-1}] or None. DFS from the top, bounded below
    by what the lower positions can still pay."""
    maxbelow = [0] * s
    for k in range(1, s):
        maxbelow[k] = maxbelow[k - 1] + w.a[k] * w.q[k - 1]

    def rec(k, v, zero):
        if k == 0:
            return [] if v == 0 else None
        cap = w.a[k]
        hi = 0 if zero else min(cap, v // w.q[k - 1])
        lo = max(0, -((maxbelow[k - 1] - v) // w.q[k - 1]))
        for d in range(hi, lo - 1, -1):
            r = rec(k - 1, v - d * w.q[k - 1], d == cap)
            if r is not None:
                return r + [d]
        return None
    r = rec(s - 1, h, top_zero)
    return None if r is None else [0] + r


def lift(w, rep, s, d):
    """The input with digits rep[1..s-1] one position up and d at s."""
    return sum(rep[k] * w.q[k] for k in range(1, s)) + d * w.q[s]


def windows():
    return {
        "golden": Win("golden [1]", [1] * WANT),
        "silver": Win("silver [2]", [2] * WANT),
        "bronze": Win("bronze [3]", [3] * WANT),
        "sqrt3": Win("sqrt(3) - 1 [1, 2]", [1, 2] * (WANT // 2)),
        "e-2": Win("e - 2 (certified)", quotients_e_minus_2(WANT + 4)),
        "cbrt": Win("cbrt(2) - 1 (certified)", quotients_cbrt2_minus_1(WANT + 4)),
    }


def stage_c(ws):
    print("=" * 78)
    print("C1 THE CUT LEMMA (exhaustive, m < %d, t = 2..6)" % N_CUT)
    ok = True
    for w in ws.values():
        bad = 0
        pts = sorted((w.frac(m * w.al), m) for m in range(1, N_CUT))
        for t in range(2, 7):
            cuts = sorted(w.frac(-j * w.al) for j in range(1, w.q[t] + 1))
            for (x1, m1), (x2, m2) in zip(pts, pts[1:]):
                same = w.digits(m1)[:t] == w.digits(m2)[:t]
                between = bisect_right(cuts, x1) < bisect_left(cuts, x2)
                bad += same == between
        ok &= bad == 0
        print(f"  {w.name:26s} exceptions {bad}")
    print("C2 THE CRITERION AGAINST THE AUTOMATON (peak 2 at the constant windows)")
    from explore_limit_column import Window                      # noqa: E402
    from explore_limit_maps import read, tail_caps               # noqa: E402
    for name, caps in (("golden [1]", (1,)), ("silver [2]", (2,)),
                       ("bronze [3]", (3,)), ("sqrt(3) - 1 [1, 2]", (1, 2))):
        read(name, Window(tail_caps(caps), len(caps)), "drop", r=1)
    for key in ("golden", "silver", "bronze"):
        w = ws[key]
        hits = []
        for t in (2, 3):
            for s in range(t + 2, 13):
                for j in range(1, w.q[t] + 1):
                    L = w.landing(s, j)
                    if L not in (None, "cap"):
                        hits.append((t, s, j, L[0]))
        ok &= not hits
        print(f"  {w.name:26s} landings at s >= t + 2: {hits[:4] if hits else 'none'}")
    w = ws["sqrt3"]
    found = None
    for s in range(5, 13):
        L = w.landing(s, 1)
        if L not in (None, "cap"):
            h, u, c = L
            rep = represent(w, h, s, top_zero=(c + 1 == w.a[s]))
            n1 = lift(w, rep, s, c)
            ag, oag = check_pair(w, n1, n1 + w.q[s], s)
            found = (s, h, n1, n1 + w.q[s], ag, oag)
            break
    ok &= found is not None and found[4] == found[0] and found[5] < 2
    print(f"  {w.name:26s} positive control (automaton: infinite from t = 2): "
          f"{'s=%d h=%d pair (%d, %d) agree %d drops agree %d' % found if found else 'NO LANDING'}")
    print("STAGE C:", "ALL GREEN" if ok else "RED")
    return ok


def check_pair(w, n1, n2, s):
    d1, d2 = w.digits(n1), w.digits(n2)
    assert w.legal(d1) and w.legal(d2), (n1, n2)
    ag = agreement(d1, d2)
    o1, o2 = w.digits(w.drop(d1)), w.digits(w.drop(d2))
    return ag, agreement(o1, o2)


def stage_e(ws):
    print("=" * 78)
    print("E1 THE LANDING FAMILY AT e - 2, m = 2..%d" % M_TOP)
    w = ws["e-2"]
    ok = True
    h = 1
    for m in range(2, M_TOP + 1):
        s = 3 * m - 2
        assert w.a[s] == 2 * m and w.a[s - 1] == 1 and w.a[s - 2] == 1
        if m > 2:
            h = (2 * m - 2) * w.q[s - 4] + h
        i = (m - 1) * w.q[s - 3] + w.q[s - 4]
        assert i == h + 1
        u = -w.frac(i * w.al) / w.th[s - 1]
        pred = (2 * m - 1) + m * abs(w.th[s]) / abs(w.th[s - 1])
        rep = represent(w, h, s, top_zero=True)
        assert rep is not None, (m, h)
        n1 = lift(w, rep, s, 2 * m - 1)
        n2 = n1 + w.q[s]
        ag, oag = check_pair(w, n1, n2, s)
        good = ag == s and oag < 2 and abs(u - pred) < MARGIN and 2 * m - 1 < u < 2 * m
        ok &= good
        print(f"  m={m:2d} s={s:2d} h={h} u={float(u):.4f} pair ({n1}, {n2}) agree {ag} "
              f"drops agree {oag} {'ok' if good else 'FAIL'}")
    print("STAGE E:", "as predicted" if ok else "a prediction is off")
    return ok


def stage_k(ws):
    print("=" * 78)
    print("K1 THE CUBE-ROOT WINDOW: landings on -alpha at every a_(s+1) >= 2, s <= %d" % S_TOP_K)
    w = ws["cbrt"]
    print("  quotients:", w.a[:S_TOP_K + 2])
    ok = True
    smax = None
    for s in range(2, S_TOP_K + 1):
        if w.a[s] < 2:
            continue
        t1 = time.time()
        L = None
        for j in range(1, w.q[2] + 1):
            L = w.landing(s, j)
            if L != None:
                break
        if L == "cap":
            print(f"  s={s:2d} a_(s+1)={w.a[s]:2d}: head cap {HEAD_CAP} reached, scope ends here")
            break
        if L is None:
            print(f"  s={s:2d} a_(s+1)={w.a[s]:2d}: no landing (the criterion is silent)")
            continue
        h, u, c = L
        rep = represent(w, h, s, top_zero=(c + 1 == w.a[s]))
        assert rep is not None, (s, h)
        n1 = lift(w, rep, s, c)
        n2 = n1 + w.q[s]
        ag, oag = check_pair(w, n1, n2, s)
        good = ag == s and oag < 2
        ok &= good
        smax = s if good else smax
        print(f"  s={s:2d} a_(s+1)={w.a[s]:2d}: h={h} j={j} u={float(u):.3f} digits {c},{c + 1}: "
              f"pair agree {ag}, drops agree {oag} {'ok' if good else 'FAIL'} ({time.time() - t1:.1f}s)")
    if smax:
        print(f"  => c(t) >= {smax} - t + 1 at scanned scope: c(2) >= {smax - 1}")
    print("STAGE K:", "as predicted" if ok else "a check failed")
    return ok


def main():
    ws = windows()
    stages = set(sys.argv[1:]) or {"c", "e", "k"}
    res = []
    if "c" in stages:
        res.append(stage_c(ws))
    if "e" in stages:
        res.append(stage_e(ws))
    if "k" in stages:
        res.append(stage_k(ws))
    print("=" * 78)
    print("ALL GREEN" if all(res) else "SOMETHING IS RED")


if __name__ == "__main__":
    main()
