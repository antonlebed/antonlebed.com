"""explore_drop_ascent.py -- THE PARITY-CHAIN THEOREM: at an Ostrowski
window with bounded quotients, is the drop by 1 finitely readable, and
what decides it?

THE QUESTION
------------
An Ostrowski window alpha = [0; a_1, a_2, ...] writes n = sum d_k q_k
(q_0 = 1, q_1 = a_1, q_{k+1} = a_{k+1} q_k + q_{k-1}; d_0 <= a_1 - 1,
d_k <= a_{k+1}, d_k = a_{k+1} forces d_{k-1} = 0). The DROP BY 1 deletes
the low digit: n -> sum_{k>=1} d_k q_{k-1}. Its lookahead column c(t) is
the least c-hat such that inputs sharing t + c-hat low digits have drops
sharing t low digits, infinite when none serves. Known: at the constant
windows [1], [2], [3] the column is finite with peak 2, at [1, 2] it is
infinite from depth 2 (the carry automaton, explore_limit_maps.py), at
e - 2 and at a Liouville-type tail it is infinite (explore_drop_column.py,
explore_relation_address.py). Open: a window whose quotients are BOUNDED
and NOT periodic -- does it ever read the drop by 1 infinitely?

THE HAND ATTACK (before the engine)
-----------------------------------
theta_k = q_k alpha - p_k alternates in sign, |theta_k| < 1/q_{k+1},
theta_{k+1} = a_{k+1} theta_k + theta_{k-1}; n's circle point is
sum d_k theta_k and its drop's point is sum d_k theta_{k-1}.

THE CUT LEMMA (explore_drop_column.py, exhaustive there): the depth-t
cells are the arcs cut by exactly the points -j alpha, 1 <= j <= q_t, so
two drops share t low digits iff no such cut separates their points.

STRADDLE(s, t): some depth-s input cylinder's drops meet two depth-t
cells. A depth-s cylinder sits inside a depth-(s-1) one, so STRADDLE is
downward closed in s, and c(t) = min{s : not STRADDLE(s, t)} - t,
infinite iff STRADDLE(s, t) at infinitely many s. FRESH(s, t): two
inputs agreeing to depth EXACTLY s (same depth-s cylinder, different
first tail digit d_s) whose drops part below t. STRADDLE(s, t) iff
FRESH(s', t) for some s' >= s.

THE EXACT DECISION. A cylinder with head digits d_1..d_{s-1} (d_0 is
deleted by the drop and free) has drop points P + T_s(z), P the head's
drop point sum_{k<s} d_k theta_{k-1} and T_s(z) the set of tail sums
sum_{k>=s} d_k theta_{k-1} over legal tails, z recording whether
d_{s-1} = 0 (which alone lets d_s reach its cap a_{s+1}). A drop's point
never sits ON a cut (that would need the drop to equal -j), so
STRADDLE(s, t) iff some cut lies STRICTLY inside the hull of P + T_s(z)
for some head: points below the cut and above it both exist then, the
hull's ends being limits of tail sums. The hull [lo_s(z), hi_s(z)] is a
two-state recursion down the positions (the extreme tail puts the cap at
every other position, the cap rule forcing the zero between). FRESH(s,
t) iff for some head and cut, sub-cylinders of two different first
digits d != d' have the cut above the infimum of one and below the
supremum of the other. Which heads exist is the DROP-REPRESENTABILITY
question: h = sum_{k=1}^{s-1} d_k q_{k-1} with d_k <= a_{k+1} and the cap
rule -- the coefficient at weight q_i may reach a_{i+2}, one quotient
LATER than the numeration's own a_{i+1}. The heads whose point lies in a
target arc are found in two steps: the integers N = h + j whose point
lies in the arc are walked down their own greedy digits (a cylinder of
the numeration is an arc, so a level keeps only the digits whose arc
meets the target), and each N - j is tested for drop-representability
by an integer-bounded search. Exact in the convergent p_96/q_96; a
comparison within the margin is a TIE, read as equality and counted (a
hull end can sit exactly on a cut: at golden the extreme drop tail
telescopes to the lattice point -theta_{s-2}). A first reader searched
the head's own digits against the real arc and ran for hours at the
finite-column windows, where no head exists and the real prune keeps
every branch alive; it was killed and this walk written in its place.

THE ASCENT FAMILY (the sufficient half, derived). Let s >= 4 and take
the head h = q_{s-2} - j, 1 <= j <= q_t. Then (h + j) alpha has point
theta_{s-2} = theta_s - a_s theta_{s-1} = -u theta_{s-1} with
    u = a_s + |theta_s| / |theta_{s-1}|,   a_s < u < a_s + 1,
never an integer. The first tail digits d_s = a_s and d_s = a_s + 1
sweep the drop to the two sides of the cut -j alpha, at distances
|theta_s| and |theta_{s-1}| - |theta_s| from it, both below |theta_t|
for t <= s - 1: the two inputs agree to depth exactly s and their drops
part below every t with q_t >= max(j, 2). The digit a_s + 1 is legal iff
a_{s+1} >= a_s + 1 -- AN ASCENT of the quotients at s -- and, at the
cap a_{s+1} = a_s + 1 exactly, iff the head has d_{s-1} = 0. At the
constant windows a_{s+1} = a_s and the family is dead at every s. At
e - 2 the landings of the parent rig sit at s = 3m - 2, a_{s+1} = 2m > 1
= a_s, ascents every one; at the cube-root window its landings at s =
2, 5, 8, 10, 12 are ascents and its silences at 13, 15, 16 are one
descent (a_14 = 2 < a_13 = 10) and two ascents its head cap cut short.
What the family does NOT prove: that q_{s-2} - j is drop-representable
(a lean, read below), and the CONVERSE -- that without an ascent no
straddle is fresh at s. The engine reads both.

THE HYPOTHESIS, in the object's own words: for t >= 2 and s >= t + 2,
FRESH(s, t) iff a_{s+1} > a_s. Then, with STRADDLE the union of the
FRESH cells above, c(t) is infinite iff the quotients ascend infinitely
often -- at bounded quotients, iff they are NOT eventually constant --
and at an eventually constant window c(t) = s_last - t + 1 for t <=
s_last - 2, s_last the last ascent. The band s = t + 1, where the
constant windows do straddle (their peak 2 says FRESH(t + 1, t)), is
outside the hypothesis and read open. Transplant marked: "ascent" is
this window's word for what the e - 2 family read as a big digit over
two ones; the constant a_s ahead of it, not its size, is the claim.

PREDICTIONS, FIXED BEFORE THE RUN (what the engine prints)
  C1 CONTROL, THE AUTOMATON: at golden, silver, bronze and every
     periodic window of the list the column read off exact STRADDLE at
     t = 2, 3, 4 equals the carry automaton's c_inf (an infinite
     automaton column read as >= S_TOP - t + 1). KILL: any
     disagreement.
  C2 CONTROL, BRUTE FORCE: at every window, s <= 8, t = 2, 3, over
     all inputs below min(q_{s+4}, 3 x 10^5), the straddles and fresh
     straddles found by enumeration are a SUBSET of the exact
     verdicts (brute-yes / exact-no kills the exact reader), and the
     two agree at every cell the range reaches q_{s+4}. KILL: a
     brute-yes exact-no cell.
  C3 CONTROL, THE WITNESSES: every FRESH verdict is accompanied by an
     integer pair, built from the head found and the two extreme tails,
     that agrees to depth exactly s with drops parting below t, checked
     digit by digit. KILL: a verdict without a pair.
  E1 THE ASCENT LAW: at every window, t = 2, 3, 4, t + 2 <= s <= S_TOP:
     FRESH(s, t) iff a_{s+1} > a_s; mismatches 0. KILL: any mismatch,
     in either direction.
  E2 THE COLUMN: at the eventually constant windows c(t) = s_last - t +
     1 for 2 <= t <= s_last - 2; at the window with a descent and no
     ascent, c(t) = 2 at t = 2, 3, 4 (predicted from the constant
     windows' peak: transplant); at the Fibonacci-word and Thue-Morse
     windows and at [1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2], [1,
     1, 2], [1, 2, 2], [2, 1, 1], [1, 2, 3], e - 2 and the cube root,
     STRADDLE(s, t) at every s <= S_TOP, the column >= S_TOP - t + 1.
     KILL: any other reading.
  E3 THE BAND s = t + 1: FRESH(t + 1, t) printed per window and t. No
     prediction; read open.
  E4 THE ASCENT FAMILY'S HEADS (lean, not a kill): at every ascent s
     >= 4 of the bounded windows some j <= q_2 has q_{s-2} - j
     drop-representable with d_{s-1} = 0 where the cap demands it, the
     printed u equal to a_s + |theta_s|/|theta_{s-1}| to the margin, and
     the lifted pair passing the digit check. Printed as a count of
     ascents served against ascents.

THE SECOND SLATE, frozen after the first run's smoke read and before
stage p ran. The smoke read killed E1 at the Fibonacci-word window: it
ascends at s = 9 and 12 and is fresh at neither, its column reading
finite at scope, while [1, 2] is infinite. The reason is REACH: the
family's head q_7 - j, j <= 3, sits in a gap of the drop-representable
set (position 7's cap-1 digit forbids position 6, so no drop on
positions 1..8 lies in (45, 68)). THE PARITY-CHAIN LEMMA: write R(K)
for "q_K - 1 is a drop on positions 1..K". Since q_K - 1 = a_K q_{K-1} +
q_{K-2} - 1, and the digit a_K is legal at position K when a_K <=
a_{K+1} (at the cap it forces position K - 1 to zero, which the
remainder q_{K-2} - 1 < q_{K-2} never uses), R(K - 2) implies R(K);
R(0) is trivial and R(1) needs a_1 - 1 <= a_2. So q_{s-2} - 1 is a drop
with d_{s-1} = 0 whenever a_i <= a_{i+1} at every i = s - 2, s - 4, ...
of s's parity, the base a_1 <= a_2 + 1 included. THE PARITY-CHAIN
THEOREM: at every s with a_{s+1} > a_s whose parity chain below is
non-descending, FRESH(s, t) for every 2 <= t <= s - 1, by the ascent
family; infinitely many such s make the column infinite at every t >=
2. A bounded NON-PERIODIC window with an infinite column therefore
exists: alpha = [0; 1, x_1, 1, x_2, ...] with x_m in {1, 2} not
eventually periodic and x_m = 2 infinitely often (the odd chain is
1 <= x_m, every odd s with x = 2 an ascent).
  P1 THE PARITY-CHAIN WINDOWS: at [1, x] with x the Fibonacci word and
     the Thue-Morse word over {1, 2}, and at [2, x] with x the Fibonacci
     word over {2, 3}, every ascent s <= S_TOP is fresh at t = 2, 3, 4
     (t <= s - 1), the family's head q_{s-2} - 1 is drop-representable
     with d_{s-1} = 0 at every one, its u equals a_s +
     |theta_s|/|theta_{s-1}| to the margin, and the column reads >=
     S_TOP - t + 1. KILL: an ascent in the chain that is not fresh, or
     whose family head is not a drop.
  P2 THE LEMMA'S CONVERSE IS OPEN: at every window of the first slate,
     the ascents whose family head is NOT a drop are printed with the
     chain's first descent; the fresh cells among them (served by
     another head, as fib12's s = 6 is) are counted. No prediction.

Estimate: two to five minutes for the first slate as written, the E1
depth-first searches at the infinite-column windows the cost; stage p
under a minute. Stages (argv): c controls, e the law and the columns,
p the parity-chain windows; all by default.

FINDINGS (each at its own tier; the prints copied, the asserts read)

F1  THE CONTROLS HOLD. C1: the exact column agrees with the carry
    automaton at all thirteen periodic windows, t = 2, 3, 4 -- the
    constants 2, 1, 2; [1, 1, 2] 4, 3, 2 and [2, 1, 1] 2, 1, 3 (FINITE,
    the automaton's column periodic with period 3); the other nine
    infinite, read >= 17, 16, 15. C2: no brute-yes / exact-no cell at
    23 windows x 13 cells; one complete-range exact-yes / brute-no at
    the cube root, its witness past q_{s+4}. C3: every fresh verdict's
    pair, built from the head found and the two extreme tails, agreed
    to depth exactly s with drops parting below t.
F2  THE ASCENT LAW IS DEAD (E1: 178 mismatches, both directions).
    Ascents with no fresh straddle: the Fibonacci-word windows at s =
    9, 12, 14, 17, the Thue-Morse windows at 7, 11, 13, 16, [1, 1, 2] at
    8, 11, 14, 17, [2, 1, 1] at every one, the cube root at 15, 16, 18
    -- at each the family's head q_{s-2} - j is no drop (P2 names the
    chain's first descent). Fresh straddles with no ascent: [2, 3] and
    [3, 2] at EVERY s, the descents served by a two-step sweep (first
    digits 0 and 2 over the head 1 q_0 + 2 q_2 + 2 q_4 + ...); e - 2
    at s = 3m, the big digit inside the head and the sweep 0 | 1; the
    cell s = t + 2 at the two-quotient windows.
F3  THE COLUMNS (t = 2, 3, 4). Eventually constant: [1,2]x4 then 1s
    reads 6, 5, 4 and 1x6, 2 then 2s reads 5, 4, 3, both s_last - t +
    1 as predicted; 3,2,3,2,3 then 3s reads 3, 2, 2; 2x8 then 1s (a
    descent, no ascent) reads 2, 1, 2, the constant windows' own -- the
    E2 line 2, 2, 2 was a transplant and misses at t = 3. The band
    s = t + 1 (E3): fresh at t = 2 and 4 and empty at t = 3 at the
    constant windows and the descent-only window, fresh at every t
    at the other windows but Thue-Morse {1,2} at t = 4. Bounded and
    non-periodic, FINITE at scope (no straddle from the last fresh s
    to 18): Fibonacci word {1,2} and {1,3} both 5, 4, 3; Thue-Morse
    {1,2} and {2,3} both 3, 2, 4 (observation). e - 2 infinite; the
    cube root 11, 10, 9 at scope, its last fresh cell s = 12, so the
    parent rig's silences at 15 and 16 were the object's and not its
    head cap's.
F4  THE FAMILY'S HEADS (E4). q_{s-2} - j serves every ascent at the six
    two-quotient periodic windows and at [1, 2, 2]; 1 of 5 at [1, 1,
    2], 0 of 5 at [2, 1, 1], 5 of 10 at [1, 2, 3], 2 of 6 at each
    Fibonacci word, 1 of 5 at each Thue-Morse word; u printed as
    a_s + |theta_s|/|theta_{s-1}| to the margin at every served cell.
F5  THE PARITY-CHAIN THEOREM HOLDS (P1, theorem by the hand attack;
    read at three windows). [1, x] with x the Fibonacci word {1,2}
    (ascents 3, 9, 13 to s = 18), [1, x] with x Thue-Morse {1,2}
    (ascents 3, 5, 9, 15, 17) and [2, x] with x the Fibonacci word
    {2,3} (ascents 3, 9, 13): every ascent's chain non-descending, the
    family's head a drop at every one, every ascent fresh at t = 2, 3,
    4, the columns >= 17, 16, 15. So a bounded non-periodic window
    with the drop by 1 infinite exists. P2: among ascents whose family
    head is no drop, fresh anyway at [1, 2, 3] 5 of 5, e - 2 4 of 4,
    the cube root 4 of 7, [1, 1, 2] 1 of 5, the Fibonacci and
    Thue-Morse words 0 of 4 each: the reach question is wider than the
    family and the converse of the theorem is false.

RUN RECORD (the estimate first, then what it cost)
Estimated two to five minutes; 114.1 s wall, peak working set 34.7 MB,
240,799 walk nodes, 20,613 ties at the margin. The first reader
(the head's digits searched against the real arc) ran 3.4 CPU-hours
past its third window and was killed; no verdict was read from it. Its
replacement first walked the integers from the top digit down and
blew its node cap at silver (a number's point is fixed by its LOW
digits), then went bottom-up; its first arc omitted the cut offset,
caught by the pair assertion before any verdict was read. The first
slate's predictions were not touched after the run; the second slate
was written after the smoke read and before stage p ran.
"""
import os
import sys
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_drop_column import (Win, represent, lift, check_pair,   # noqa: E402
                                 WANT, T_TOP, MARGIN)
from explore_nonquadratic_window import (                            # noqa: E402
    quotients_e_minus_2, quotients_cbrt2_minus_1)

K_TAIL = T_TOP - 4
S_TOP = 18
T_RANGE = (2, 3, 4)
Q_T_CAP = 60
BRUTE_S = 8
BRUTE_N = 300_000
LIFTS = range(-3, 4)

KILLS = []


def kill(msg):
    KILLS.append(msg)
    print("  KILL:", msg)


def fib_word(n, lo, hi):
    w = "a"
    while len(w) < n:
        w = "".join("ab" if ch == "a" else "a" for ch in w)
    return [lo if ch == "a" else hi for ch in w[:n]]


def tm_word(n, lo, hi):
    return [hi if bin(i).count("1") % 2 else lo for i in range(n)]


def windows():
    W = {}

    def add(key, name, a):
        W[key] = Win(name, list(a)[:WANT])
    add("golden", "golden [1]", [1] * WANT)
    add("silver", "silver [2]", [2] * WANT)
    add("bronze", "bronze [3]", [3] * WANT)
    for per in ([1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2],
                [1, 1, 2], [1, 2, 2], [2, 1, 1], [1, 2, 3]):
        add("p" + "".join(map(str, per)), "periodic %s" % per,
            per * (WANT // len(per) + 1))
    add("fib12", "Fibonacci word {1,2}", fib_word(WANT, 1, 2))
    add("fib13", "Fibonacci word {1,3}", fib_word(WANT, 1, 3))
    add("tm12", "Thue-Morse {1,2}", tm_word(WANT, 1, 2))
    add("tm23", "Thue-Morse {2,3}", tm_word(WANT, 2, 3))
    add("ev1", "[1,2]x4 then 1s (last ascent 7)", [1, 2] * 4 + [1] * WANT)
    add("ev2", "3,2,3,2,3 then 3s (last ascent 4)", [3, 2, 3, 2, 3] + [3] * WANT)
    add("ev3", "1x6, 2 then 2s (last ascent 6)", [1] * 6 + [2] * WANT)
    add("ev4", "2x8 then 1s (a descent, no ascent)", [2] * 8 + [1] * WANT)
    add("e-2", "e - 2 (certified)", quotients_e_minus_2(WANT + 4))
    add("cbrt", "cbrt(2) - 1 (certified)", quotients_cbrt2_minus_1(WANT + 4))
    return W


def ascent(w, s):
    """a_{s+1} > a_s; w.a[k] is a_{k+1}."""
    return w.a[s] > w.a[s - 1]


# ------------------------------------------------------------ the reader
class Reader:
    """Exact STRADDLE and FRESH at one window. A head's drop point must
    lie in a target arc; the integers N = h + j whose point lies in the
    arc are enumerated by a walk down their own greedy digits (a
    cylinder of the numeration is an arc, so the prune is tight), and
    each candidate's h = N - j is then tested for drop-representability
    by an integer-bounded search."""
    NODE_CAP = 2_000_000
    TIES = [0]

    def __init__(self, w):
        self.w = w
        th, a, q = w.th, w.a, w.q
        K = K_TAIL
        # drop-tail hulls lo[k][z], hi[k][z]: sums over positions >= k of
        # d_k theta_{k-1}, z = 1 when d_{k-1} = 0 so d_k may reach a[k].
        lo = [[Fraction(0)] * 2 for _ in range(K + 2)]
        hi = [[Fraction(0)] * 2 for _ in range(K + 2)]
        for k in range(K, 0, -1):
            for z in (0, 1):
                dmax = a[k] if z else a[k] - 1
                cl, ch = [lo[k + 1][1]], [hi[k + 1][1]]
                for d in {1, dmax} if dmax >= 1 else ():
                    cl.append(d * th[k - 1] + lo[k + 1][0])
                    ch.append(d * th[k - 1] + hi[k + 1][0])
                lo[k][z], hi[k][z] = min(cl), max(ch)
        self.lo, self.hi = lo, hi
        # the numeration's own tail hulls TL/TH[k][z] over positions >= k
        # of e_i theta_i (e_0 <= a_1 - 1, e_i <= a[i], the cap rule),
        # z = 1 when e_{k-1} = 0 so e_k may reach its cap.
        TL = [[Fraction(0)] * 2 for _ in range(K + 2)]
        TH = [[Fraction(0)] * 2 for _ in range(K + 2)]
        for k in range(K, -1, -1):
            cap = a[0] - 1 if k == 0 else a[k]
            for z in (0, 1):
                dmax = cap if z else cap - 1
                cl, ch = [TL[k + 1][1]], [TH[k + 1][1]]
                for d in {1, dmax} if dmax >= 1 else ():
                    cl.append(d * th[k] + TL[k + 1][0])
                    ch.append(d * th[k] + TH[k + 1][0])
                TL[k][z], TH[k][z] = min(cl), max(ch)
        self.TL, self.TH = TL, TH
        # the drop reach: max drop on positions 1..s-1 by top digit case
        self.nodes = 0

    @classmethod
    def inside(cls, P, a, b):
        """P strictly inside (a, b) beyond the margin; a tie is outside."""
        if P - a > MARGIN and b - P > MARGIN:
            return True
        if min(abs(P - a), abs(P - b)) <= MARGIN:
            cls.TIES[0] += 1
        return False

    @classmethod
    def overlap(cls, lo, hi, a, b):
        """The closed [lo, hi] meets the open (a, b) beyond the margin."""
        if hi <= a + MARGIN or lo >= b - MARGIN:
            if min(abs(hi - a), abs(lo - b)) <= MARGIN:
                cls.TIES[0] += 1
            return False
        return True

    def reach(self, s, z):
        """The largest drop on positions 1..s-1 with d_{s-1} = 0 iff z."""
        w = self.w
        best = 0
        # positions 1..s-1: caps a[k], weights q[k-1]; a simple DP on
        # (value max) by whether the next-higher digit is at cap
        mx = [[0, 0] for _ in range(s + 1)]        # mx[k][f]: positions 1..k
        for k in range(1, s):
            cap = w.a[k]
            for f in (0, 1):
                cands = [mx[k - 1][0]]
                if not f:
                    for d in range(1, cap + 1):
                        cands.append(d * w.q[k - 1] + mx[k - 1][1 if d == cap else 0])
                mx[k][f] = max(cands)
        if z:
            return mx[s - 2][0] if s >= 2 else 0
        cap = w.a[s - 1]
        for d in range(1, cap + 1):
            best = max(best, d * w.q[s - 2] + mx[s - 2][1 if d == cap else 0])
        return best

    def integers_in(self, nmax, targets):
        """Every integer 0 <= N <= nmax whose point sum e_k theta_k lies in
        one of the open target intervals (lifts included), by a walk UP
        its greedy digits from position 0: the numbers sharing low digits
        form an arc of the tail hull's width, so a level keeps only the
        digits whose arc meets a target."""
        w = self.w
        top = 0
        while w.q[top + 1] <= nmax:
            top += 1
        found = []

        def rec(k, z, V, P):
            """Positions below k chosen (value V, point P); z = 1 iff
            e_{k-1} = 0."""
            self.nodes += 1
            assert self.nodes < self.NODE_CAP, "the integer walk blew up"
            if any(self.inside(P, a, b) for a, b in targets):
                found.append(V)                      # zeros from k up
            if k > top:
                return
            cap = w.a[0] - 1 if k == 0 else w.a[k]
            dmax = cap if z else cap - 1
            for d in range(1, dmax + 1):
                V2 = V + d * w.q[k]
                if V2 > nmax:
                    break
                P2 = P + d * w.th[k]
                if any(self.overlap(P2 + self.TL[k + 1][0], P2 + self.TH[k + 1][0], a, b)
                       for a, b in targets):
                    rec(k + 1, 0, V2, P2)
            if any(self.overlap(P + self.TL[k + 1][1], P + self.TH[k + 1][1], a, b)
                   for a, b in targets):
                rec(k + 1, 1, V, P)
        rec(0, 1, 0, Fraction(0))
        return sorted(set(found))

    def is_drop(self, h, s, z):
        """Digits [0, d_1..d_{s-1}] of a drop-representation of h on
        positions 1..s-1 with d_{s-1} = 0 iff z, or None."""
        w = self.w
        if h < 0 or h > self.reach(s, z):
            return None
        if z:
            return represent(w, h, s, top_zero=True)
        cap = w.a[s - 1]
        for d in range(1, cap + 1):
            r = represent(w, h - d * w.q[s - 2], s - 1, top_zero=(d == cap))
            if r is not None:
                return r + [d]
        return None

    def sub(self, s, d):
        """Hull of the sub-cylinder with first tail digit d."""
        z = 1 if d == 0 else 0
        return (d * self.w.th[s - 1] + self.lo[s + 1][z],
                d * self.w.th[s - 1] + self.hi[s + 1][z])

    def cuts(self, t):
        return [(j, self.w.frac(-j * self.w.al)) for j in range(1, self.w.q[t] + 1)]

    def straddle(self, s, t):
        """(head digits, j, z) of a witness, or None."""
        for j, c in self.cuts(t):
            for z in (1, 0):
                # N = h + j has point P - c: the arc for N drops the cut
                tg = [(m - self.hi[s][z], m - self.lo[s][z]) for m in LIFTS]
                for N in self.integers_in(self.reach(s, z) + j, tg):
                    h = self.is_drop(N - j, s, z)
                    if h is not None:
                        return h, j, z
        return None

    def fresh(self, s, t):
        """(head digits, j, z, d, d') of a witness, or None."""
        w = self.w
        for j, c in self.cuts(t):
            for z in (1, 0):
                dmax = w.a[s] if z else w.a[s] - 1
                subs = {d: self.sub(s, d) for d in range(dmax + 1)}
                pairs, tg = [], []
                for d, (lo_d, _) in subs.items():
                    for d2, (_, hi_d2) in subs.items():
                        if d != d2 and lo_d < hi_d2:
                            pairs.append((d, d2))
                            tg += [(m - hi_d2, m - lo_d) for m in LIFTS]
                if not pairs:
                    continue
                for N in self.integers_in(self.reach(s, z) + j, tg):
                    h = self.is_drop(N - j, s, z)
                    if h is None:
                        continue
                    P = sum(h[k] * w.th[k - 1] for k in range(1, s))
                    for d, d2 in pairs:
                        for m in LIFTS:
                            if self.inside(P, c + m - subs[d2][1], c + m - subs[d][0]):
                                return h, j, z, d, d2
                    raise AssertionError("a head found off every pair")
        return None

    def extreme_tail(self, s, d, low):
        """Digits d_s.. d_K of the tail from s starting with d whose sum
        tends to the sub-cylinder's infimum (low) or supremum."""
        w = self.w
        digs = [d]
        prev = d
        for k in range(s + 1, K_TAIL + 1):
            z = 1 if prev == 0 else 0
            dmax = w.a[k] if z else w.a[k] - 1
            best, bestv = 0, (self.lo if low else self.hi)[k + 1][1]
            for dd in range(1, dmax + 1):
                v = dd * w.th[k - 1] + (self.lo if low else self.hi)[k + 1][0]
                if (v < bestv) if low else (v > bestv):
                    best, bestv = dd, v
            digs.append(best)
            prev = best
        return digs

    def witness_pair(self, s, t, h, j, z, d, d2):
        """Integers n, n' agreeing to depth exactly s whose drops part
        below t: the head h with tails from d (toward its infimum) and
        from d2 (toward its supremum)."""
        w = self.w
        c = w.frac(-j * w.al)
        P = sum(h[k] * w.th[k - 1] for k in range(1, s))
        t1 = self.extreme_tail(s, d, low=True)
        t2 = self.extreme_tail(s, d2, low=False)
        head = sum(h[k] * w.q[k] for k in range(1, s))
        n1 = head + sum(x * w.q[s + i] for i, x in enumerate(t1))
        n2 = head + sum(x * w.q[s + i] for i, x in enumerate(t2))
        p1 = P + sum(x * w.th[s + i - 1] for i, x in enumerate(t1))
        p2 = P + sum(x * w.th[s + i - 1] for i, x in enumerate(t2))
        assert any(p1 < c + m < p2 or p2 < c + m < p1 for m in LIFTS), \
            "the extreme tails do not bracket the cut"
        return n1, n2


# --------------------------------------------------------------- brute
def brute(w, s, t):
    """(straddle, fresh, complete) over inputs below min(q_{s+4}, BRUTE_N)."""
    N = min(w.q[s + 4], BRUTE_N)
    cyl = {}
    for n in range(N):
        d = w.digits(n)
        if not w.legal(d):
            continue
        key = tuple(d[:s])
        cell = tuple(w.digits(w.drop(d))[:t])
        cyl.setdefault(key, {}).setdefault(d[s], set()).add(cell)
    strad = fresh = False
    for sub in cyl.values():
        allc = set().union(*sub.values())
        if len(allc) >= 2:
            strad = True
            for d, cs in sub.items():
                for d2, cs2 in sub.items():
                    if d != d2 and any(x != y for x in cs for y in cs2):
                        fresh = True
    return strad, fresh, N == w.q[s + 4]


# --------------------------------------------------------------- stages
def stage_c(W, R):
    print("=" * 78)
    print("C1 THE AUTOMATON AGAINST EXACT STRADDLE (t = 2, 3, 4)")
    from explore_limit_column import Window                      # noqa: E402
    from explore_limit_maps import read, tail_caps               # noqa: E402
    periodic = [("golden", (1,)), ("silver", (2,)), ("bronze", (3,))]
    periodic += [(k, tuple(int(ch) for ch in k[1:])) for k in W if k[0] == "p"]
    for key, caps in periodic:
        res = read(W[key].name, Window(tail_caps(caps), len(caps)), "drop", r=1)
        lc = res["lc"]
        col, pre, per, inf = lc["col"], lc["pre"], lc["per"], lc["inf_from"]
        mine = [column(R[key], t) for t in T_RANGE]
        print(f"  {W[key].name:26s} exact column {mine}  automaton col[t] "
              f"{col} pre {pre} per {per} infinite from {inf}")
        for t, c in zip(T_RANGE, mine):
            if inf is not None and t >= inf:
                if not isinstance(c, str):
                    kill(f"C1 {key} t={t}: automaton infinite, exact {c}")
                continue
            au = col[t] if t < len(col) else col[pre + (t - pre) % per]
            if c != au:
                kill(f"C1 {key} t={t}: exact {c} automaton {au}")
    print("C2 BRUTE FORCE AGAINST THE EXACT READER (s <= %d, t = 2, 3)" % BRUTE_S)
    for key, w in W.items():
        bad = 0
        cells = 0
        partial = 0
        for t in (2, 3):
            if w.q[t] > Q_T_CAP:
                continue
            for s in range(t, BRUTE_S + 1):
                bs, bf, complete = brute(w, s, t)
                es = R[key].straddle(s, t) is not None
                ef = R[key].fresh(s, t) is not None
                cells += 1
                if (bs and not es) or (bf and not ef):
                    bad += 1
                    kill(f"C2 {key} s={s} t={t}: brute ({bs},{bf}) exact ({es},{ef})")
                elif complete and (bs != es or bf != ef):
                    partial += 1
        print(f"  {w.name:34s} cells {cells:3d}  brute-yes/exact-no {bad}  "
              f"complete-range disagreements {partial}")


def column(R, t):
    for s in range(t, S_TOP + 1):
        if R.straddle(s, t) is None:
            return s - t
    return ">=%d" % (S_TOP - t + 1)


def stage_e(W, R):
    print("=" * 78)
    print("E1 THE ASCENT LAW: FRESH(s, t) iff a_{s+1} > a_s, t + 2 <= s <= %d" % S_TOP)
    print("   rows: ascents then FRESH per s (from s = t + 2); '.' no, 'A'/'F' yes")
    tot_mis = 0
    for key, w in W.items():
        for t in T_RANGE:
            if w.q[t] > Q_T_CAP:
                print(f"  {w.name:34s} t={t}: q_t = {w.q[t]} over the cap, skipped")
                continue
            asc = "".join("A" if ascent(w, s) else "." for s in range(t + 2, S_TOP + 1))
            fr = []
            mis = 0
            wit = []
            for s in range(t + 2, S_TOP + 1):
                f = R[key].fresh(s, t)
                if f is not None:
                    n1, n2 = R[key].witness_pair(s, t, *f)
                    ag, dag = check_pair(w, n1, n2, s)
                    if not (ag == s and dag < t):
                        kill(f"C3 {key} s={s} t={t}: pair agrees {ag}, drops agree {dag}")
                    h, j, z, d, d2 = f
                    hv = sum(h[k] * w.q[k - 1] for k in range(1, s))
                    wit.append(f"s{s}:j{j},h{hv}={'+'.join(f'{x}q{k - 1}' for k, x in enumerate(h) if x and k)},d{d}|{d2}")
                fr.append("F" if f is not None else ".")
                mis += (f is not None) != ascent(w, s)
            tot_mis += mis
            band = R[key].fresh(t + 1, t) is not None
            print(f"  {w.name:34s} t={t} c(t)={str(column(R[key], t)):5s} "
                  f"band(s=t+1) {'F' if band else '.'}  mismatches {mis}")
            print(f"      ascents {asc}")
            print(f"      fresh   {''.join(fr)}")
            if t == 2 and wit:
                print("      witnesses " + "  ".join(wit))
            if mis:
                kill(f"E1 {key} t={t}: {mis} mismatches")
    print(f"  E1 total mismatches {tot_mis}")

    print("E2 THE COLUMN at the eventually constant windows")
    for key, s_last in (("ev1", 7), ("ev2", 4), ("ev3", 6), ("ev4", None)):
        w = W[key]
        cols = [column(R[key], t) for t in T_RANGE]
        pred = ([2] * 3 if s_last is None else
                [s_last - t + 1 if t <= s_last - 2 else "open" for t in T_RANGE])
        print(f"  {w.name:34s} c(2..4) = {cols}  predicted {pred}")
        for c, p in zip(cols, pred):
            if p != "open" and c != p:
                kill(f"E2 {key}: column {cols} predicted {pred}")

    print("E4 THE ASCENT FAMILY'S HEADS q_{s-2} - j (lean): served / ascents, s >= 4")
    for key, w in W.items():
        if key in ("e-2", "cbrt"):
            continue
        served = asc_n = 0
        us = []
        for s in range(4, S_TOP + 1):
            if not ascent(w, s):
                continue
            asc_n += 1
            need_zero = (w.a[s] == w.a[s - 1] + 1)
            ok = False
            for j in range(1, w.q[2] + 1):
                h = w.q[s - 2] - j
                if h < 0:
                    continue
                rep = represent(w, h, s, top_zero=need_zero)
                if rep is None:
                    continue
                n1 = lift(w, rep, s, w.a[s - 1])
                n2 = lift(w, rep, s, w.a[s - 1] + 1)
                ag, dag = check_pair(w, n1, n2, s)
                if ag == s and dag < 2:
                    ok = True
                    u = -w.frac((h + j) * w.al) / w.th[s - 1]
                    pred_u = w.a[s - 1] + abs(w.th[s]) / abs(w.th[s - 1])
                    assert abs(u - pred_u) < MARGIN, (key, s, float(u), float(pred_u))
                    us.append(f"{s}:{float(u):.3f}")
                    break
            served += ok
        print(f"  {w.name:34s} served {served} of {asc_n} ascents  u: {' '.join(us[:6])}")


def chain_descent(w, s):
    """The first i of s's parity, i <= s - 2, with a_i > a_{i+1} (the base
    counts a_1 > a_2 + 1), or None when the chain is non-descending."""
    for i in range(s - 2, 0, -2):
        if i == 1:
            if w.a[0] > w.a[1] + 1:
                return 1
        elif w.a[i - 1] > w.a[i]:
            return i
    return None


def family_head(w, s):
    """The ascent family at j = 1: the head q_{s-2} - 1 as a drop with
    d_{s-1} = 0, its pair and its u; None when the head is no drop."""
    h = w.q[s - 2] - 1
    rep = represent(w, h, s, top_zero=True)
    if rep is None:
        return None
    n1 = lift(w, rep, s, w.a[s - 1])
    n2 = lift(w, rep, s, w.a[s - 1] + 1)
    ag, dag = check_pair(w, n1, n2, s)
    u = -w.frac((h + 1) * w.al) / w.th[s - 1]
    pred_u = w.a[s - 1] + abs(w.th[s]) / abs(w.th[s - 1])
    return dict(h=h, rep=rep, ok=(ag == s and dag < 2), u=u, u_ok=abs(u - pred_u) < MARGIN)


def stage_p(W, R):
    print("=" * 78)
    print("P1 THE PARITY-CHAIN WINDOWS: every ascent fresh by the family")
    PW = {
        "px_fib": Win("[1, x], x Fibonacci {1,2}",
                      [v for x in fib_word(WANT, 1, 2) for v in (1, x)][:WANT]),
        "px_tm": Win("[1, x], x Thue-Morse {1,2}",
                     [v for x in tm_word(WANT, 1, 2) for v in (1, x)][:WANT]),
        "px_23": Win("[2, x], x Fibonacci {2,3}",
                     [v for x in fib_word(WANT, 2, 3) for v in (2, x)][:WANT]),
    }
    for key, w in PW.items():
        Rw = Reader(w)
        asc = [s for s in range(3, S_TOP + 1) if ascent(w, s)]
        bad = 0
        served = 0
        for s in asc:
            fam = family_head(w, s)
            if fam is None or not fam["ok"] or not fam["u_ok"]:
                bad += 1
                kill(f"P1 {key} s={s}: family head {fam}")
                continue
            served += 1
            for t in T_RANGE:
                if t <= s - 1 and w.q[t] <= Q_T_CAP and Rw.fresh(s, t) is None:
                    bad += 1
                    kill(f"P1 {key} s={s} t={t}: an ascent in the chain, not fresh")
        cols = [column(Rw, t) for t in T_RANGE]
        chain = [chain_descent(w, s) for s in asc]
        print(f"  {w.name:30s} a_1..a_12 {w.a[:12]}")
        print(f"      ascents {asc}  chain descents {chain}  family served {served}/{len(asc)}"
              f"  failures {bad}  c(2..4) {cols}")
    print("P2 ASCENTS WHOSE FAMILY HEAD IS NO DROP (first slate's windows), fresh among them")
    for key, w in W.items():
        rows = []
        for s in range(4, S_TOP + 1):
            if not ascent(w, s):
                continue
            fam = family_head(w, s)
            if fam is not None and fam["ok"]:
                continue
            fr = R[key].fresh(s, 2) is not None if w.q[2] <= Q_T_CAP else None
            rows.append(f"s{s}(desc@{chain_descent(w, s)}){'F' if fr else '.'}")
        if rows:
            print(f"  {w.name:34s} {' '.join(rows)}")


def main():
    t0 = time.time()
    stages = sys.argv[1:] or ["c", "e", "p"]
    W = windows()
    R = {k: Reader(w) for k, w in W.items()}
    if "c" in stages:
        stage_c(W, R)
    if "e" in stages:
        stage_e(W, R)
    if "p" in stages:
        stage_p(W, R)
    print("=" * 78)
    nodes = sum(r.nodes for r in R.values())
    print(f"search nodes {nodes}; ties at the margin {Reader.TIES[0]}; "
          f"{time.time() - t0:.1f} s; kills {len(KILLS)}")
    for k in KILLS:
        print("  ", k)


if __name__ == "__main__":
    main()
