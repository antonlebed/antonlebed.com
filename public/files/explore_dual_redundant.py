"""The redundant-digit door: what signed digits buy back at the
archimedean window, and what they pay.

THE QUESTION
------------
The dual pole reads the integers through the size window only —
sign, exponent, leading base-b digits — and its exact-locality
classification (explore_dual_locality.py) is austere: with ordinary
(non-redundant) digits, the exactly window-local class is the
fiber-cellular maps, whose arithmetic core is the thin family of
scalings floor((u/v)n) gated by rad(u) | rad(b); addition by a
nonzero constant, rough scalings, and squaring are graded at every
lookahead. Hardware arithmetic has long claimed a door: REDUNDANT
digit sets {-a..a} with 2a+1 > b (signed-digit / carry-save), on
which most-significant-digit-first pipelines compute with bounded
"on-line delay" (Trivedi-Ercegovac 1977; generalized in Frougny,
Pavelka, Pelantova, Svobodova, DMTCS 21:3 (2019) #14, whose OL
Property, integer-base delay inequality, and divisor-preprocessing
condition were read full-text and are re-verified as laws here, not
imported). This experiment charts the door in the window/fiber
vocabulary: which walled reads become exactly local once digits are
redundant, at what lookahead, and what the redundancy pays.

One folklore correction fixed at the design freeze: at integer base
b with digit set {-a..a}, a <= b-1, ZERO HAS ONLY THE ALL-ZERO
representation (V != 0 implies |bV + d| >= b - a >= 1), so the
division wall below is built from NEAR-zero prefixes, never from
nontrivial zero representations (those live at the literature's
non-integer bases).

THE MODEL
---------
Base b >= 2, digit set D = {-a..a}; redundant iff 2a+1 > b; primary
scope ceil(b/2) <= a <= b-1 (over-redundant a >= b visited once for
the leak-restoration criterion). MSB-first strings d_1..d_t with
value V = sum d_i b^{t-i}. The completions of a t-prefix by j more
digits form its FIBER. A function is EXACTLY LOCAL AT LOOKAHEAD c
if a transducer can emit the output digit at value scale s once the
input is read down to value scale s*b^c, its emitted prefix valid
(extendable to an exact representation of the true output) at every
step and every termination, for ALL inputs.

Two engines decide locality, one per direction:

THE SAFETY GAME (sufficiency AND necessity, digitwise-linear maps):
for x -> m*x the whole future constraint is carried by the integer
residual R (the part of the true output the emitted prefix still
owes), stepping R' = b*R + m*x - e*b^c with adversary digit x and
controller digit e; the emitted prefix stays valid iff R stays in
the flushable set |R| <= a*R_c, R_c = (b^c - 1)/(b - 1). Locality
at lookahead c is EQUIVALENT to 0 lying in the greatest fixed point
of "some e keeps R' flushable-and-winning for every x" (R is a
sufficient statistic; any transducer induces an R-strategy). The
fixed point is computed exhaustively — a hand-played game at
(b,a,m,c) = (2,1,3,2) survives shallow play yet dies in the full
fixed point, so sampled plays are never trusted for a verdict. The
same game with injected values {x + y} decides pair addition.

THE COVER VIEW (the mechanism): the fiber of an operand prefix is
an integer interval (verified, not assumed); an output digit can be
emitted iff the image interval fits inside ONE output prefix
interval. Non-redundant reading is the Lebesgue-number-0 case of
this cover; redundancy buys a positive Lebesgue number, and every
dissolved gate below is that one purchase.

Pair multiplication and division are verified through the
Trivedi-Ercegovac residual invariants W_k = b^k (X_k Y_k - P_{k-1})
and W_k = b^k (N_{k+delta} - Q_{k-1} D_{k+delta}) over exact
Fractions (the identity form of their recursions), with select =
clamped rounding; the emitted prefix's validity is re-checked from
the definition at every scope, never from the bookkeeping.

PREDICTIONS, fixed before the engine ran
----------------------------------------
P-A [derived, property] THE PREFIX-INTERVAL LAW: a t-prefix's fiber
    is the full contiguous interval V*b^j +- a*R_j; consecutive
    prefix intervals overlap in 2a*R_j - b^j + 1 integers; the
    cover's Lebesgue count is lambda_j = 2a*R_j - b^j + 2 (every
    integer interval of <= lambda_j points fits in one cell, some
    interval of lambda_j + 1 fits in none). At (2,1): lambda_j =
    2^j. Non-redundant digits give lambda = 0: the partition.
P-B [derived recursion; the identification an expected observation]
    THE MULTIPLICITY LAW: the representation count obeys
    r_t(n) = sum_{d == n mod b, d in D} r_{t-1}((n-d)/b); at (2,1)
    this is Stern's diatomic recursion, and r_t(n) = stern(2^t - |n|)
    is expected from hand cases n in {0,1,2,3}. The redundant window
    is a RELATION, and its string measure weights value n by
    r_t(n)/(2a+1)^t — not counting measure.
P-C [derived upper bound by construction; tightness expected, to be
    measured] THE DELAY LAW: x -> m*x is exactly local at every
    lookahead c with b^c (2a - b + 1) >= 2am. HEADLINE: bounded
    lookahead for EVERY m — the numerator gate rad(m) | rad(b)
    DISSOLVES. Expected minimal delay c_min(m) = v_b(m) +
    ceil(log_b(2a*m0/(2a - b + 1))) for the coprime part m0 > 1
    (marked: the v-additivity is a transplant from shift intuition,
    the m0 form rests on one hand-played fixed point), and
    c_min(b^v) = v exactly.
P-D [derived, rule] THE ADDITION LAW: X + Y is exactly local at c
    with b^c (2a - b + 1) >= 4a ((2,1): c = 2; (10,6): c = 1);
    constant shift n + s rides the pair adder; negation is free
    (c = 0). The non-redundant shift wall dissolves.
P-E [expected from the literature's delay inequality, conventions
    reconciled never forced] PAIR MULTIPLICATION: exactly local at
    bounded lookahead (the delay inequality gives 2 at (2,1), 1 at
    (10,6) in the padded-fraction convention); squaring rides it,
    dissolving the curvature wall. The non-redundant pair-exception
    density 2(1 - b^-j)/b^c (explore_dual_measure.py) was the
    Lebesgue-number-0 artifact.
P-F [derived, rule] THE ORDER WALL (the price, first direction):
    sign, equality, comparison, and NORMALIZATION (converting to
    the non-redundant window — reading one's own exponent) are
    non-local at EVERY lookahead. Witnesses: the all-zero prefix
    (completions of both signs at every depth); THE ORDER-BLUR LAW
    (both orders realizable for prefix values V, V' iff
    |V - V'|*b^j < 2a*R_j, an ambiguity ~ 2a/(b-1) cells wide where
    the non-redundant window's is 1 cell — comparison strictly
    WORSE than non-redundant, where distinct windows are ordered).
P-G [derived, rule] THE REDUNDANCY LEAK (the price, second
    direction; every density states its measure): for p | b, on a
    depth-j prefix fiber the counting-measure residue bias is
    exactly zero iff p | 2a*R_j + 1, which for p | b reduces to
    p | 2a+1 — otherwise O(1/b^j), vanishing but never zero: exact
    deep hiding degrades to graded. Under the STRING measure (the
    door's own), value mod p equals the last digit mod p, bias
    CONSTANT: zero iff p | 2a+1. Restoration criterion
    rad(b) | 2a+1 is unsatisfiable at every even base (2a+1 odd):
    THE PARITY LEAK. Odd radicals restore (b=9, a=4).
P-H [derived wall; certified door from the literature, verified]
    THE DIVISION CERTIFICATE: the quotient of two redundant streams
    is non-local at every lookahead bare (near-zero divisor prefix:
    quotients of both signs and unbounded ratio share every input
    window); with the archimedean side-condition |D_k| >= Dmin
    (the literature's divisor preprocessing) the Trivedi-Ercegovac
    division runs exactly. The one archimedean bit the redundant
    window cannot manufacture internally.
P-I [synthesis, no engine; sharpened since by
    explore_reading_geometry.py — Lipschitz at cell scale, with a
    one-digit stream correction at redundant covers] THE MIRROR: a
    window reads at bounded
    lookahead what is Lipschitz in its own metric; non-redundant
    reading adds a boundary-alignment clause (the radical gates =
    Lebesgue number 0); redundancy deletes the alignment clause and
    keeps continuity — so bounded-carry arithmetic enters whole,
    and the discontinuous order reads (the archimedean data itself)
    stay walled at any redundancy. Redundancy is the archimedean
    deletion performed inside the archimedean window.

KILL CRITERIA, fixed at the freeze: K1 any m infeasible at P-C's
upper lookahead kills the construction; K2 any order read passing
the locality tests at some lookahead kills P-F; K3 a leak bias off
the exact formulas kills P-G; K4 a non-contiguous prefix fiber
kills P-A and both engines. POSITIVE CONTROLS: PC1 balanced ternary
(b,a) = (3,1) is non-redundant — the game must reproduce the
numerator gate (x3 local at c=1, x2 infeasible at every scanned c);
PC2 every transducer output is re-verified from the definition;
PC3 the literature's delay values are reconciled through an explicit
convention dictionary. The flush margin b^c/2 <= a*R_c inside P-C is
a margin, not the kill — it is asserted separately at every scope.

Engine: pure python, exact integers and Fractions, no sampling in
any wall verdict; seconds.

FINDINGS (from the run: 90309 checks, exit 0, ~2 s)
---------------------------------------------------
F1 THE PREFIX-INTERVAL LAW (rule; exhaustive at five (b,a), depths
   1-3): the fiber is the full interval V*b^j +- a*R_j, overlap
   2a*R_j - b^j + 1, Lebesgue count lambda_j = 2a*R_j - b^j + 2 —
   both directions (lambda_j fits, lambda_j + 1 fails). At (2,1)
   lambda_j = 2^j exactly; balanced ternary overlaps 0 (the
   partition). The redundant window is an overlapping COVER; the
   non-redundant one is its Lebesgue-number-0 degeneration.
F2 THE STERN LAW (rule): the multiplicity recursion holds exactly
   ((2,1) t=5 on 63 values; (10,6) t=3 on 1333), and at (2,1) the
   representation count IS Stern's diatomic sequence read from the
   top: r_t(n) = stern(2^t - |n|), whole-range exhaustive at
   t = 3, 5, 8 (both sides satisfy the same recursion and boundary,
   so the identity is forced; the door's own measure weights value
   n by stern(2^t - |n|)/3^t).
F3 THE DELAY LAW (rule at 19 scanned scopes; the formula conjectured
   general): x -> m*x is exactly local at bounded lookahead for
   EVERY m — the numerator gate rad(m) | rad(b) DISSOLVES — and the
   minimal lookahead matched the predicted closed form at every
   scanned point: c_min(m) = v_b(m) + ceil(log_b(2a*m0 /
   (2a - b + 1))) for b-coprime part m0 > 1 (matched at the scopes
   below and AT THOSE ONLY: swept later at 2a - b + 1 = 2, the form
   overpredicts by one digit at m = 2 for each of (3,2), (5,3),
   (7,4) and at m = 5 for (3,2) — explore_redundant_lookback.py,
   where the same margin loses the same digit for addition);
   pure b-powers sit at
   c_min = v exactly (x10 at (10,6) is 1, not the formula's 2).
   Measured tables: (2,1): x1:0, x2:1, x3:3, x4:2, x5:4, x6:4,
   x7:4, x9:5, x10:5, x12:5; (4,2): x2:2, x3:2, x5:3, x6:3;
   (10,6): x2:1, x3:2, x7:2, x10:1, x20:2. The derived sufficient
   bound b^c (2a - b + 1) >= 2am held at every scope, flush margin
   asserted separately. THE PRICING MIRROR: the finite pole gates a
   scaling by its RADICAL, the dual pole prices it by its SIZE —
   log_b m plus a redundancy-margin constant log_b(2a/(2a-b+1)) —
   each pole charging in its own currency. Control: balanced
   ternary reproduced the numerator gate (x3 c=1, x9 c=2, x2/x5
   infeasible through c=8).
F4 THE ADDITION LAW (rule): X + Y exactly local at c_min = 2 at
   (2,1) and c_min = 1 at (10,6) — the game feasible at the
   predicted c and infeasible one below (b^c (2a - b + 1) >= 4a
   tight at both, and AT BOTH ONLY: swept later over 58 symmetric
   systems, that inequality is sufficient and overpredicts by one
   digit at every 2a - b + 1 = 2 system, the exact threshold being
   c = 1 iff 2a - b + 1 >= 2 and b >= 3 —
   explore_redundant_lookback.py) — with the greedy adder exact on all 59049
   length-5 pairs at (2,1) and all 28561 length-2 pairs at (10,6);
   negation digitwise (c = 0); n + s exact through the adder for
   s = 1, 3, -5. The shift wall dissolves.
F5 PAIR MULTIPLICATION (rule at the literature delay; the smaller
   delay an observation): the Trivedi-Ercegovac transducer with
   select = clamped round keeps every emitted prefix valid at the
   integer-base delay inequality's delta, RUN DIRECTLY at that
   delta — (2,1) delta 2 across exhaustive length-4 pairs plus 150
   random length-35 streams; (10,6) delta 1 across 1500 random
   length-8 plus 150 random length-35 (scanned, not exhaustive) —
   and squaring rides the same transducer: the curvature wall
   dissolves. Scanned minimal working delta at (2,1) is 1, one
   below the inequality (the inequality is sufficient, not claimed
   tight; observation, scanned scope only).
F6 THE ORDER WALL (rule; witness families at every lookahead):
   sign is open on the all-zero prefix at every depth; both orders
   are realizable for prefix values V, V' exactly iff
   |V - V'| b^j < 2a*R_j (the order-blur law, verified as an iff),
   making order ambiguous across 3 cells at both scanned systems
   where the non-redundant window's ambiguity is 1 cell — the
   equality wall widens to an order wall; and the prefix V = 1
   straddles the exponent boundary b^j at every depth: the window
   cannot read its own exponent (no in-window normalization).
F7 THE DIVISION CERTIFICATE (wall a rule; the certified door
   verified at scanned scope): the divisor prefix 0^6 admits
   quotients +-64 — opposite signs, magnitude growing with depth,
   so no output window at any lookahead covers the fiber — while
   under the certificate |D_k| >= 1/2 the Trivedi-Ercegovac
   division emitted valid prefixes on 100/100 scanned quotients at
   delta = 4. The bare wall is the archimedean bit; the
   preprocessing is its import.
F8 THE REDUNDANCY LEAK (rule; exact rationals): counting bias on
   depth-3 fibers: 1/30 at (2,1) p=2, 1/2666 at (10,6) p=2,
   3/6665 at (10,6) p=5 — vanishing O(1/b^j) but zero only when
   p | 2a+1; string-measure bias CONSTANT: 1/6, 1/26, 3/65 at the
   same scopes, with exact restoration at (10,7) p=5 (5 | 15) and
   (9,4) p=3 (3 | 9), bias exactly 0 under BOTH measures there.
   The parity leak stands: 2a+1 is odd, so rad(b) | 2a+1 fails at
   every even base — an even-base redundant window always leaks
   the parity the non-redundant window hides exactly.

RUN RECORD: one folklore kill at the freeze (nontrivial zero
representations do not exist at integer base, a <= b-1); one
hand-played game (2,1,3,2) that survived shallow play and died in
the full fixed point — recorded as the reason no verdict path
samples plays; the delay-law formula, transplant-marked at the
freeze, confirmed at all 19 scopes including the v-additivity and
the minimal-redundancy base (4,2). All eight predictions landed;
no kill criterion fired; positive controls green.
"""

import itertools
import random
from fractions import Fraction

CHECKS = [0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        raise AssertionError(msg)


def repunit(b, j):
    return (b**j - 1) // (b - 1)


def digits(a):
    return range(-a, a + 1)


def strings(a, t):
    return itertools.product(digits(a), repeat=t)


def value(b, s):
    v = 0
    for d in s:
        v = b * v + d
    return v


def frac_value(b, s):
    return Fraction(value(b, s), b**len(s))


# ----------------------------------------------------------------- S1
# P-A: prefix-interval law, overlap, Lebesgue count.

def s1_prefix_intervals():
    print("== S1 THE PREFIX-INTERVAL LAW ==")
    for (b, a) in [(2, 1), (3, 2), (4, 2), (10, 6), (10, 7)]:
        for j in (1, 2, 3):
            R = repunit(b, j)
            fib = sorted(set(value(b, s) for s in strings(a, j)))
            ok(fib == list(range(-a * R, a * R + 1)),
               f"fiber not the full interval at (b,a,j)=({b},{a},{j})")
            lam = 2 * a * R - b**j + 2
            if 2 * a + 1 > b and lam > 0:
                def fits(x, ln):
                    lo = -(-(x + ln - 1 - a * R) // b**j)  # ceil
                    hi = (x + a * R) // b**j
                    return lo <= hi
                ok(all(fits(x, lam) for x in range(-b**j, b**j + 1)),
                   f"Lebesgue count too small at ({b},{a},{j})")
                ok(not all(fits(x, lam + 1)
                           for x in range(-b**j, b**j + 1)),
                   f"Lebesgue count too large at ({b},{a},{j})")
            ov = 2 * a * R - b**j + 1
            ov_true = len(set(range(-a * R, a * R + 1))
                          & set(range(b**j - a * R, b**j + a * R + 1)))
            ok(ov_true == max(0, ov), f"overlap law off at ({b},{a},{j})")
            print(f"  (b,a)=({b},{a}) j={j}: fiber = V*{b**j} +- {a*R}, "
                  f"overlap {max(0, ov)}, Lebesgue count {max(lam, 0)}")
    b, a = 3, 1
    for j in (1, 2, 3):
        ok(2 * a * repunit(b, j) - b**j + 1 <= 0,
           "balanced ternary claims overlap")
    print("  control (3,1) balanced ternary: overlap 0 at j=1..3 "
          "(the partition, Lebesgue number 0)")


# ----------------------------------------------------------------- S2
# P-B: multiplicity recursion + the Stern identification at (2,1).

def stern(n, memo={0: 0, 1: 1}):
    if n not in memo:
        if n % 2 == 0:
            memo[n] = stern(n // 2)
        else:
            memo[n] = stern(n // 2) + stern(n // 2 + 1)
    return memo[n]


def s2_multiplicity():
    print("== S2 THE MULTIPLICITY LAW ==")
    for (b, a) in [(2, 1), (10, 6)]:
        t = 5 if b == 2 else 3
        cnt, cnt1 = {}, {}
        for s in strings(a, t):
            v = value(b, s)
            cnt[v] = cnt.get(v, 0) + 1
        for s in strings(a, t - 1):
            v = value(b, s)
            cnt1[v] = cnt1.get(v, 0) + 1
        for n, c in cnt.items():
            rec = sum(cnt1.get((n - d) // b, 0)
                      for d in digits(a) if (n - d) % b == 0)
            ok(rec == c, f"multiplicity recursion off at ({b},{a}) n={n}")
        print(f"  (b,a)=({b},{a}) t={t}: recursion exact on "
              f"{len(cnt)} values")
    b, a = 2, 1
    for t in (3, 5, 8):
        cnt = {}
        for s in strings(a, t):
            v = value(b, s)
            cnt[v] = cnt.get(v, 0) + 1
        for n in range(-(2**t - 1), 2**t):
            ok(cnt.get(n, 0) == stern(2**t - abs(n)),
               f"Stern law fails at t={t} n={n}")
        print(f"  (2,1) t={t}: r_t(n) = stern(2^t - |n|) on the whole "
              f"range ({len(cnt)} values)")


# ----------------------------------------------------------------- S3
# The safety game: exact locality of x -> m*x at lookahead c.

def game_feasible(b, a, c, S):
    """0 in the greatest fixed point of the residual safety game
    with injected values S, emission granularity b^c, flushable set
    |R| <= a*R_c."""
    F = a * repunit(b, c)
    win = set(range(-F, F + 1))
    changed = True
    while changed:
        changed = False
        for R in list(win):
            for s in S:
                pre = b * R + s
                if not any(pre - e * b**c in win for e in digits(a)):
                    win.discard(R)
                    changed = True
                    break
    return 0 in win


def c_min_scaling(b, a, m, cap=10):
    for c in range(cap + 1):
        if game_feasible(b, a, c, [m * x for x in digits(a)]):
            return c
    return None


def s3_delay_law():
    print("== S3 THE DELAY LAW (the safety game) ==")
    for (b, a, ms) in [(2, 1, [1, 2, 3, 4, 5, 6, 7, 9, 10, 12]),
                       (4, 2, [2, 3, 5, 6]),
                       (10, 6, [2, 3, 7, 10, 20])]:
        marg = 2 * a - b + 1
        for m in ms:
            cu = 0
            while b**cu * marg < 2 * a * m:
                cu += 1
            ok(game_feasible(b, a, cu, [m * x for x in digits(a)]),
               f"K1: m={m} infeasible at derived upper c={cu} "
               f"(b,a)=({b},{a})")
            ok(2 * a * repunit(b, cu) >= b**cu,
               f"flush margin fails at (b,a,c)=({b},{a},{cu})")
            cm = c_min_scaling(b, a, m)
            v, m0 = 0, m
            while m0 % b == 0:
                m0 //= b
                v += 1
            if m0 == 1:
                pred = v
            else:
                p = 0
                while b**p * marg < 2 * a * m0:
                    p += 1
                pred = v + p
            tag = "=" if cm == pred else "  != predicted"
            print(f"  (b,a)=({b},{a}) x{m}: c_min = {cm} "
                  f"(upper {cu}, predicted {pred}) {tag}")
    b, a = 3, 1
    ok(c_min_scaling(b, a, 3, cap=6) == 1, "PC1: x3 not c=1 at (3,1)")
    ok(c_min_scaling(b, a, 9, cap=6) == 2, "PC1: x9 not c=2 at (3,1)")
    for m in (2, 5):
        ok(c_min_scaling(b, a, m, cap=8) is None,
           f"PC1: x{m} claims locality at balanced ternary")
    print("  control (3,1) balanced ternary: x3 c=1, x9 c=2, x2/x5 "
          "infeasible to c=8 -- the numerator gate reproduced")


# ----------------------------------------------------------------- S4
# P-D: addition (injected set {x+y}), negation, constant shift.

def transducer_run(b, a, c, injected):
    """Greedy residual transducer: one injected integer per step,
    one emitted digit per step at granularity b^c, then c flush
    digits; returns emitted digits or None if stuck. Exactness is
    re-checked by the caller from the definition."""
    R = 0
    out = []
    for s in injected:
        pre = b * R + s
        best = None
        for e in digits(a):
            R2 = pre - e * b**c
            if abs(R2) <= a * repunit(b, c) and \
                    (best is None or abs(R2) < abs(best[1])):
                best = (e, R2)
        if best is None:
            return None
        out.append(best[0])
        R = best[1]
    for rem in range(c - 1, -1, -1):
        scale = b**rem
        cands = [d for d in digits(a)
                 if abs(R - d * scale) <= a * repunit(b, rem)]
        if not cands:
            return None
        e = min(cands, key=lambda d: abs(R - d * scale))
        out.append(e)
        R -= e * scale
    return out if R == 0 else None


def s4_addition():
    print("== S4 THE ADDITION LAW ==")
    for (b, a, c_pred) in [(2, 1, 2), (10, 6, 1)]:
        S = sorted(set(x + y for x in digits(a) for y in digits(a)))
        ok(game_feasible(b, a, c_pred, S),
           f"addition infeasible at predicted c={c_pred} ({b},{a})")
        if c_pred > 0:
            ok(not game_feasible(b, a, c_pred - 1, S),
               f"addition feasible below predicted c ({b},{a})")
        t = 5 if b == 2 else 2
        n_pairs = 0
        for xs in strings(a, t):
            for ys in strings(a, t):
                out = transducer_run(b, a, c_pred,
                                     [x + y for x, y in zip(xs, ys)])
                ok(out is not None and
                   value(b, out) == value(b, xs) + value(b, ys),
                   f"adder wrong at {xs}+{ys}")
                n_pairs += 1
        print(f"  (b,a)=({b},{a}): c_min = {c_pred} (game, tight), "
              f"adder exact on all {n_pairs} length-{t} pairs")
    b, a = 2, 1
    for s in strings(a, 4):
        ok(value(b, tuple(-d for d in s)) == -value(b, s), "negation")
    for const in (1, 3, -5):
        cd = []
        v = abs(const)
        while v:
            cd.append((v % b) * (1 if const > 0 else -1))
            v //= b
        for xs in strings(a, 4):
            ys = [0] * (4 - len(cd)) + list(reversed(cd))
            out = transducer_run(b, a, 2,
                                 [x + y for x, y in zip(xs, ys)])
            ok(out is not None and
               value(b, out) == value(b, xs) + const,
               f"shift n+{const} failed at {xs}")
    print("  negation c=0 digitwise; n+s exact through the adder "
          "(s = 1, 3, -5): the shift wall dissolves")


# ----------------------------------------------------------------- S5
# P-E: pair multiplication via the Trivedi-Ercegovac invariant
# W_k = b^k (X_k Y_k - P_{k-1}), select = clamped round.

def te_multiply(b, a, delta, xs, ys):
    """Multiply padded fraction streams 0.(0^delta)xs, 0.(0^delta)ys;
    return emitted digits and the running validity flag (checked by
    definition at every step: the true product must stay inside the
    emitted prefix's completion interval)."""
    xs = [0] * delta + list(xs)
    ys = [0] * delta + list(ys)
    X = Y = P = Fraction(0)
    out = []
    valid = True
    for k in range(1, len(xs) + 1):
        X += Fraction(xs[k - 1], b**k)
        Y += Fraction(ys[k - 1], b**k)
        W = b**k * (X * Y - P)
        pk = max(-a, min(a, round(W)))
        out.append(pk)
        P += Fraction(pk, b**k)
        if abs(X * Y - P) > Fraction(a, (b - 1) * b**k):
            valid = False
    Xf = frac_value(b, xs)
    Yf = frac_value(b, ys)
    k = len(out)
    if abs(Xf * Yf - P) > Fraction(a, (b - 1) * b**k):
        valid = False
    return out, valid


def s5_pair_multiplication():
    print("== S5 PAIR MULTIPLICATION (the curvature wall included) ==")
    for (b, a) in [(2, 1), (10, 6)]:
        def scan(delta):
            if b == 2:
                for xs in strings(a, 4):
                    for ys in strings(a, 4):
                        _, valid = te_multiply(b, a, delta, xs, ys)
                        if not valid:
                            return False
            else:
                rng = random.Random(268)
                for _ in range(1500):
                    xs = [rng.randint(-a, a) for _ in range(8)]
                    ys = [rng.randint(-a, a) for _ in range(8)]
                    _, valid = te_multiply(b, a, delta, xs, ys)
                    if not valid:
                        return False
            rng = random.Random(269)
            for _ in range(150):
                xs = [rng.randint(-a, a) for _ in range(35)]
                ys = [rng.randint(-a, a) for _ in range(35)]
                _, valid = te_multiply(b, a, delta, xs, ys)
                if not valid:
                    return False
            return True

        dlit = 0
        while Fraction(b, 2) + Fraction(2 * a * a, b**dlit * (b - 1)) \
                > Fraction(2 * a + 1, 2):
            dlit += 1
        found = None
        for delta in range(0, dlit + 3):
            if scan(delta):
                found = delta
                break
        # the rule's own scope: the literature delta is run directly,
        # never inferred from a smaller working delta
        ok(scan(dlit), f"pair mult fails at the literature delta "
                       f"({b},{a})")
        ok(found is not None and found <= dlit,
           f"minimal delta above the literature delta ({b},{a})")
        scope = "exhaustive length-4 pairs +" if b == 2 else "scanned"
        print(f"  (b,a)=({b},{a}): valid at literature delta {dlit} "
              f"AND at minimal delta {found} ({scope} random long)")
        rng = random.Random(270)
        for _ in range(100):
            xs = [rng.randint(-a, a) for _ in range(30)]
            _, valid = te_multiply(b, a, dlit, xs, xs)
            ok(valid, "squaring invalid")
    print("  squaring exact through the same transducer: the "
          "curvature wall dissolves")


# ----------------------------------------------------------------- S6
# P-F: the order wall -- witnesses by definition.

def s6_order_wall():
    print("== S6 THE ORDER WALL (the price, first direction) ==")
    for (b, a) in [(2, 1), (10, 6)]:
        for t in (3, 6):
            plus = (0,) * t + (1,)
            minus = (0,) * t + (-1,)
            ok(value(b, plus) > 0 > value(b, minus), "sign witness")
        j = 3
        R = repunit(b, j)
        blur = 0
        for dV in range(0, 4 * a):
            lo1, hi1 = -a * R, a * R
            lo2, hi2 = dV * b**j - a * R, dV * b**j + a * R
            both = (lo1 < hi2) and (lo2 < hi1)
            ok(both == (dV * b**j < 2 * a * R),
               f"order-blur law off at ({b},{a}) dV={dV}")
            if both and dV > 0:
                blur += 1
        width = 2 * blur + 1
        print(f"  (b,a)=({b},{a}) j={j}: sign open on the all-zero "
              f"prefix at every depth; order ambiguous across {width} "
              f"cells (non-redundant: 1) -- comparison strictly worse")
        for j in (2, 4):
            R = repunit(b, j)
            ok(b**j - a * R <= b**j - 1 and b**j <= b**j + a * R,
               "normalization witness fails")
    print("  normalization: prefix V=1 straddles the exponent "
          "boundary b^j at every scanned depth -- the window cannot "
          "read its own exponent")


# ----------------------------------------------------------------- S7
# P-H: division -- the bare wall and the certified door, via
# W_k = b^k (N_{k+delta} - Q_{k-1} D_{k+delta}), select = clamped
# round of W/D.

def te_divide(b, a, delta, ns, ds, dmin):
    """Divide padded fraction streams (ns starts with delta zeros);
    divisor partial sums must stay >= dmin in modulus (the
    certificate); returns emitted digits and the validity flag."""
    K = len(ns)
    Q = Fraction(0)
    out = []
    for k in range(1, K - delta + 1):
        kk = k + delta
        Nk = sum(Fraction(ns[i], b**(i + 1)) for i in range(min(kk, K)))
        Dk = sum(Fraction(ds[i], b**(i + 1))
                 for i in range(min(kk, len(ds))))
        if abs(Dk) < dmin:
            return None, False
        W = b**k * (Nk - Q * Dk)
        qk = max(-a, min(a, round(W / Dk)))
        out.append(qk)
        Q += Fraction(qk, b**k)
    Nv = frac_value(b, ns)
    Dv = frac_value(b, ds + [0] * (K - len(ds)))
    k = len(out)
    valid = abs(Nv / Dv - Q) <= Fraction(a, (b - 1) * b**k)
    return out, valid


def s7_division():
    print("== S7 DIVISION: the bare wall and the certificate ==")
    b, a = 2, 1
    t = 6
    n_str = (1,) + (0,) * t
    qp = Fraction(value(b, n_str), value(b, (0,) * t + (1,)))
    qm = Fraction(value(b, n_str), value(b, (0,) * t + (-1,)))
    ok(qp > 0 > qm and abs(qp) == abs(qm) == 2**t,
       "division wall witness")
    print(f"  bare: divisor prefix 0^{t} admits quotients +-{2**t} -- "
          f"opposite signs, magnitude growing with depth: no output "
          f"window at any lookahead covers both")
    rng = random.Random(271)
    for delta in (4, 5, 6, 7, 8):
        good = tried = 0
        while tried < 100:
            ds = [1] + [rng.choice([0, 1]) for _ in range(23)]
            ns = [0, 0] + [rng.randint(-1, 1) for _ in range(22)]
            outq, valid = te_divide(b, a, delta, ns, ds, Fraction(1, 2))
            if outq is None:
                continue
            tried += 1
            if valid:
                good += 1
        if good == tried:
            print(f"  certified (|D_k| >= 1/2, delta={delta}): "
                  f"{good}/{tried} scanned quotients valid at every "
                  f"emitted precision")
            break
    ok(good == tried, "certified division never validated")


# ----------------------------------------------------------------- S8
# P-G: the redundancy leak, both measures.

def s8_leak():
    print("== S8 THE REDUNDANCY LEAK (both measures) ==")
    for (b, a, p) in [(2, 1, 2), (10, 6, 2), (10, 6, 5), (10, 7, 5),
                      (10, 7, 2), (9, 4, 3)]:
        j = 3
        R = repunit(b, j)
        L = 2 * a * R + 1
        counts = [0] * p
        for n in range(-a * R, a * R + 1):
            counts[n % p] += 1
        flat = all(c == L // p for c in counts)
        ok(flat == (L % p == 0), "counting-hiding criterion off")
        ok((L % p == 0) == ((2 * a + 1) % p == 0),
           f"p | 2aR_j+1 vs p | 2a+1 mismatch ({b},{a},{p})")
        bias_c = max(abs(Fraction(c, L) - Fraction(1, p))
                     for c in counts)
        t = 4 if b == 2 else 3
        counts_s = [0] * p
        for s in strings(a, t):
            counts_s[value(b, s) % p] += 1
        tot = (2 * a + 1) ** t
        digit_counts = [0] * p
        for d in digits(a):
            digit_counts[d % p] += 1
        for r in range(p):
            ok(Fraction(counts_s[r], tot) ==
               Fraction(digit_counts[r], 2 * a + 1),
               f"string-measure law off ({b},{a},{p}) r={r}")
        bias_s = max(abs(Fraction(dc, 2 * a + 1) - Fraction(1, p))
                     for dc in digit_counts)
        verdict = "EXACT hiding" if bias_s == 0 else f"leak {bias_s}"
        print(f"  (b,a)=({b},{a}) p={p}: counting bias {bias_c} "
              f"(zero iff {p} | {2*a+1}), string bias {bias_s} "
              f"-> {verdict}")
    for b in (2, 4, 10):
        for a in range((b + 1) // 2, b):
            ok((2 * a + 1) % 2 == 1, "parity")
    print("  even bases: 2a+1 odd, rad(b) | 2a+1 impossible -- the "
          "parity leak stands; b=9, a=4 restores (3 | 9)")


def main():
    s1_prefix_intervals()
    s2_multiplicity()
    s3_delay_law()
    s4_addition()
    s5_pair_multiplication()
    s6_order_wall()
    s7_division()
    s8_leak()
    print(f"ALL CHECKS PASSED: {CHECKS[0]}")


if __name__ == "__main__":
    main()
