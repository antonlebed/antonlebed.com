"""The cyclotomic ghost: does a numeration window's doubling read the part
of its Parry polynomial that beta cannot see?

THE QUESTION
------------
The census over the Pisot family (explore_pisot_confound.py) left one row
its arithmetic reading misses. At the window 10001 -- the plastic
number's greedy numeration, q_k = q_{k-1} + q_{k-5} -- the reading
count = img / gcd(img, s*) predicts 5 phases and the run counts 15; and
the phases' least period in K is 210 where count x s* would give 105,
each phase visited twice per turn. The row is the one where the word's
ORDER (5) and beta's algebraic DEGREE (3) come apart:

    x^5 - x^4 - 1 = (x^2 - x + 1)(x^3 - x - 1).

THE MECHANISM, derived by hand before the engine. The Parry-seeded places
q_k satisfy the order-5 recurrence but NOT the plastic one: the residual
D_k = q_k - q_{k-2} - q_{k-3} runs 1, 0, -1, -1, 0, 1 with period 6 from
k = 3. So q_k = P_k + C_k with P annihilated by x^3 - x - 1 and C by
x^2 - x + 1 -- a PERIODIC component of period 6 with C_{k+3} = -C_k.
Solving 3 C_k - C_{k-1} = D_k (x^3 - x - 1 is congruent to -x - 2 modulo
x^2 - x + 1, and x^3 to -1) gives C_2..C_7 = (2, 3, 1, -2, -3, -1)/7,
the 7 being the resultant of the two factors. Call C the GHOST: an
integer sequence's periodic part of amplitude under 1, invisible to
beta, to the growth rate and to the completion's torus, and able to move
an integer comparison only at a NEAR-TIE of the Pisot parts.

TWO RETRODICTIONS off the recorded row, worth nothing as evidence and
stated as the shape the law must take. With A = img / gcd(img, s*) the
arithmetic reading, s* the selected step and the top tooth at
K = lo + j s*: the top's residue mod img has period A in j; the ghost's
phase K mod m has period m / gcd(m, s*) in j. If the phase is a generic
function of both, the ORBIT has period lcm(A, m / gcd(m, s*)) in j; and
if the phase forgets the ghost's SIGN, the COUNT is the same lcm with m
replaced by m' -- m for odd m, m/2 for even m. At 10001: A = 5, s* = 7,
m = 6, m' = 3 -- orbit lcm(5, 6) x 7 = 210 and count lcm(5, 3) = 15,
both the recorded numbers. Two fits to one row.

THE LAW UNDER TEST, frozen per word from its factorization BEFORE its
count is read. Let the Parry polynomial x^n - t_1 x^{n-1} - ... - t_n
factor over Z as (the factor carrying beta) x R.
  (a) R has cyclotomic factors Phi_{m_1} ... Phi_{m_r}: m = lcm(m_i),
      m' = m for odd m and m/2 for even m; predict
          count = lcm(A, m' / gcd(m', s*)),
          orbit period in K = s* x lcm(A, m / gcd(m, s*)).
  (b) R has every root strictly inside the unit circle: the ghost
      decays; predict count = A, orbit = A x s* (one orbit, each phase
      once), exactly as the trivial-cofactor windows read.
  (c) R has a non-cyclotomic root of modulus >= 1: no prediction; the
      row is reported.
  (d) R has both cyclotomic and contracting factors: (a) decides.
Where the single-step selector is silent, A does not exist and the
prefix-count instrument of explore_silent_window.py reads the count and
the label sequence still reads the orbit; there only the RATIO orbit /
(count x s) is predicted -- m / m' -- and that is stated as the weaker
test it is.

THE FAMILY 1 0^{n-2} 1, whose polynomial is x^n - x^{n-1} - 1: under
x -> -x at odd n it is -(x^n + x^{n-1} + 1), the reciprocal of Selmer's
trinomial x^n + x + 1, reducible iff n = 2 mod 3 with cofactor Phi_3 --
so Phi_6 after the sign -- and irreducible at even n (x^n - x - 1 is
irreducible for every n). So 10001 (n = 5) and 1 0^9 1 (n = 11) carry the
same ghost, and 100001 (n = 6), the fifth-shape window, carries none.
The factorization step confirms this classical fact; it does not prove
it.

TRANSPLANTS, flagged at the freeze. The engine (legality, seeding,
greedy, the comb, the selector, the depth-prefix count and the period
reader) is the census's own, carried unchanged through
explore_silent_window.py; every dial it carries (depths 40/80, spans
60/90, the tail ladder, the bottom at 10, the K range of the period
reader) is inherited and NOT retuned here, for the reason the census
gave: retuning an instrument on the question it is about to answer is
how a depth-12 reading once returned 2 where the truth was 1. What is
new is the factorization and the per-word prediction, which is read
from the polynomial and touches no dial.

THE HAND-ATTACK on the statistic. The count is a count of distinct
strings and is bounded by the tail it is read over (F6 of the census):
predicted counts here reach lcm(A, m') and could exceed 12, so the tail
ladder runs 30, 60, 120, 240 and a row is read only where the last three
agree. The period reader has the same ceiling in its own search bound:
it searches periods to 120 over 300 samples where the census searched to
60 over 120, because the predicted orbits reach lcm(A, m) x s* / s* =
lcm(A, m) in j. A period found AT the search bound is printed as
unread. And a prediction from a factorization can be wrong in one silent
way -- a cofactor misclassified because a root sits within float
tolerance of the unit circle -- so cyclotomic factors are identified
EXACTLY, by equality with Phi_m over Z for m up to 200, and only the
contracting verdict rests on numeric roots, with the largest modulus
printed.

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  CONTROLS. The seeding rule reproduces 1, 2, 4 at 111 and 1, 2, 3 at
    101; the seven speaking binary windows with an IRREDUCIBLE Parry
    polynomial (11, 111, 1111, 11111, 111111, 101, 1001) read count = A
    and orbit = A x s*, reproducing the census's F2/F7d.
P2  THE GHOST AT 10001. D_k has period 6 with the pattern
    (1, 0, -1, -1, 0, 1) from k = 3; the exact rational C with
    C_2..C_7 = (2, 3, 1, -2, -3, -1)/7 makes q - C satisfy the plastic
    recurrence at every k in range, in exact arithmetic.
P3  THE LAW (a). At every reducible legal word to length 9 with a
    cyclotomic cofactor where the selector speaks, the measured count
    equals lcm(A, m'/gcd(m', s*)) and the measured orbit equals
    s* x lcm(A, m/gcd(m, s*)). 10001 is one such row and is printed as
    the retrodiction it is, never as a confirmation.
P4  THE LAW (b). At every reducible word with a contracting cofactor
    where the selector speaks, count = A and orbit = A x s*.
P5  THE FAMILY. Among 1 0^{n-2} 1 for n <= 11 (and n = 17 if it runs in
    budget), exactly n = 5 and n = 11 are reducible, each with cofactor
    Phi_6.
P6  THE MECHANISM AT ONE TOOTH. At 10001 the canonical carry of a single
    place -- the greedy digit set of 2 q_k, written as offsets from k --
    is NOT one form at every k the way the spine's and Narayana's are:
    it takes more than one form, and the form is a function of k mod 6
    (or of k mod 3) for all k past a printed threshold. If the carry is
    one form at every k, the ghost is read at the cascade's BOTTOM and
    not at the tooth, which is a different mechanism and is said so.

THE KILLS, as observables and never as inferences
-------------------------------------------------
K1  P1 fails at the seeding or at any of the seven controls -> no row is
    read.
K2  P2's exact check fails -> the ghost decomposition is wrong and P3
    has no mechanism; the sweep still runs, as a census with no law.
K3  P3 misses at some cyclotomic row: the row is printed with predicted
    and measured count and orbit, and the law is an observation with a
    named exception at best.
K4  No reducible word other than 10001 is read by either instrument ->
    the third outcome named in the aim: the deliverable is the
    decomposition at 10001 alone.
K5  A count unstable across the last three tails, or a period found at
    the search bound -> that row is unread and is excluded, in either
    direction.
K6  P6: the carry is one form at every k in range.

THE DESIGN
----------
D0  Controls: the seeding rule at the two theorem windows; the seven
    irreducible speaking windows' count and orbit against A and A x s*.
D1  The ghost at 10001: D_k printed for k = 3..20, the exact C, and the
    exact check that q - C obeys x^3 = x + 1 for k in range.
D2  The population: every legal word to length 9 on digits 0..2 (the
    census's filter), its Parry polynomial factored over Z; the
    reducible ones classified (a)/(b)/(c)/(d) with m, m' and the
    prediction printed BEFORE any count. The 1 0^{n-2} 1 family to
    n = 11 explicitly, with n = 17 appended if the sweep is under budget.
D3  Per reducible word: the selector over s = 3..40; at the least
    selected step, A, the tail ladder of counts, the label sequence's
    least period; predicted against measured.
D4  Where the selector is silent: the least admissible growing step
    with a depth-4 prefix count above 1, its count over the tail ladder
    and its orbit, and the ratio test.
D5  The one-tooth carry at 10001 and at 1 0^9 1: the offset form of the
    greedy digits of 2 q_k for k = 12..60, grouped by k mod 6.
D6  THE TABLE and the verdicts on P3-P6.

THE FINDINGS (every number below is copied from the printed output)
--------------------------------------------------------------------
F0  CONTROLS PASS. The seeding rule gives 1, 2, 4, 7, 13, 24 at 111 and
    1, 2, 3, 4, 6, 9 at 101; the seven irreducible speaking windows read
    count = A and orbit = A x s* at every tail (11: 2; 111: 3; 1111: 4;
    11111: 5; 111111: 6; 101: 3 at s* = 7; 1001: 3 at s* = 15, image
    step 9). P1 met.

F1  THE GHOST AT 10001 IS EXACT (rule, exact arithmetic). D_k runs
    1, 0, -1, -1, 0, 1 from k = 3 with period 6 over k <= 399, and with
    C_2..C_7 = (2, 3, 1, -2, -3, -1)/7 the sequence q - C satisfies
    x^3 = x + 1 at every k in 3..399: the Pisot part begins 10/7, 15/7,
    19/7, 25/7, 34/7, 44/7, 59/7, 78/7. P2 met.

F2  THE POPULATION. 3499 legal words to length 9 on digits 0..2; 505 are
    reducible -- 504 with a cyclotomic cofactor, 1 WILD (20001111,
    cofactor x^3 - x^2 + 1 with a root of modulus 1.1510, a second root
    outside the unit circle beside beta) -- and 1 0^9 1 is appended as a 506th row. By m: Phi_2 at
    297 words, Phi_3 at 100, Phi_4 at 75, Phi_6 at 23 (with 1 0^9 1),
    Phi_10 at 9, Phi_12 at 1. THE FAMILY 1 0^{n-2} 1 for n = 3..11 is
    reducible at n = 5 and n = 11 exactly, each with cofactor Phi_6, as
    Selmer's trinomial says. P5 met.

F3  THE LAW DIES (K3 fires, P3 refuted). 217 selector-read rows carry a
    NONZERO ghost (F6 decides which); at 206 of them the ghost prediction
    differs from the ghost-free (A, A s*), and it lands at 10001 ALONE.
    The other 205 read (A, A s*) -- and every one of the 374 selector-read
    misses has t_1 = 2 and A = 1 with a measured count of 1: the image IS
    the witness there, one limit point over one input limit, the
    alphabet story the census's F5 told (its no-carry mechanism holds at
    the bulk of such words and fails at the ones beginning 2 0, some of
    which sit among the 205 -- what is common to all 205 is the count of
    1, not the mechanism). At 11 nonzero-ghost rows, all with A = 1, the
    prediction coincides with the null (m / gcd(m, s*) = 1 there) and
    says nothing. K4 does not fire: rows were read. P4 is VACUOUS -- there is
    no contracting row to hold at, by F5.

F4  THE BINARY POPULATION, where a doubling carries. 29 reducible binary
    words to length 9, plus 1 0^9 1. The ghost is nonzero at 11 of the 30:
    10001, 1001001, 1101011, 10100101, 101000101, 110001011, 110100011,
    110101001, 111100111, 111101011, 1 0^9 1. The selector speaks at
    10001 only; the prefix instrument reads six of the other ten --
    1101011 (count 10, orbit 30), 101000101 (12, 60, each phase visited
    5/3 times per turn: a NON-UNIFORM orbit), 110100011 (6, 18),
    110101001 (6, 18), 111100111 (3, 9), 111101011 (3, 9) -- and four
    print 240 at every tail and are UNREAD at the instrument's ceiling:
    1001001, 10100101, 110001011 and 1 0^9 1, the last behaving as
    100001 did in the census. Read in comb steps, the ghost's own period
    m / gcd(m, s) is 4 at 111100111 and 6 at 111101011 against measured
    orbits of 3: THE GHOST IS ABSENT FROM THE ORBIT THERE, though it is
    nonzero in the places. The plastic row's sign-pairing -- each phase
    visited twice -- appears at none of the six. Every zero-ghost binary
    word that reads (17 of 19) has each phase visited once.

F5  KRONECKER (property, proved; 506 of 506). No cofactor is contracting:
    a Parry cofactor is monic over Z with constant term dividing -t_n, so
    the product of its roots' moduli is at least 1, and all moduli <= 1
    forces cyclotomic. The kinds are cyclotomic and wild only. P7 met.

F6  THE GHOST CRITERION (property, proved; 505 of 505 cyclotomic words,
    zero failures). The places' generating function is
    (1 - x^n) / ((1 - x)(1 - T(x))), so the ghost on a simple Phi_m
    vanishes iff m divides the word's length n. Ghost nonzero at 227 of
    505: by m, {2: [143 zero, 154 nonzero], 3: [89, 11], 4: [43, 32],
    6: [3, 20], 10: [0, 9], 12: [0, 1]}. P8 met. So which words carry a
    ghost is a divisibility fact about the WORD'S LENGTH, not about beta.

F7  THE DEFECT AT 10001 (rule, exact; k in 5..299 for the identity,
    12..199 for the digits). 2 q_k - q_{k+2} - q_{k-5} = 3 C_k - 2 C_{k+1}
    exactly, an integer running 0, -1, -1, 0, 1, 1 from k = 5 -- that is
    0, 1, 1, 0, -1, -1 at k = 2, 3, 4, 5, 0, 1 mod 6 -- and the greedy
    digits of 2 q_k are {k+2, k-5} at defect 0, {k+2, k-5, 0} at +1, and
    a representation not containing both at -1. P9 met. The ghost, a
    7-denominated real of amplitude 3/7, reaches the arithmetic as an
    INTEGER shadow of period 6, and D5's 27 forms are that shadow: the
    -1 rows borrow down a comb that lengthens by one tooth every six k.

F8  P6 FAILED ON ITS OWN LETTER (K6 false: 27 forms, not one). The
    frozen observable asked that each form sit at one residue mod 6; the
    forms at k = 0, 1 mod 6 are shared and the -1 forms grow with k, so
    the count of forms was the wrong observable and F7 names the right
    one. Recorded as the miss it is.

F9  P9b met on both halves: every selector-read miss has t_1 = 2 and
    A = 1, and the prefix-instrument rows are exactly the binary
    reducible words.

WHAT THIS LEAVES. The ghost is real, its presence is decided by m | n,
and it reaches the arithmetic at one tooth wherever it is present (F7's
shape is forced by the decomposition at any word). What is NOT general
is that the comb's phase count reads it: the plastic row's 15 and 210
are lcm(5, 3) and 7 x lcm(5, 6), and no second window shows the same
reading -- two binary ghost windows show the ghost's period absent from
the orbit outright. Why the comb reads its ghost at 10001 and not at
111101011 is the residue, and it is a question about the CASCADE, not
about the places.

RUN RECORD: one process, 45.0 s wall-clock (11.1 s to factor the 3499
words over Z with sympy, the rest the readers), ordinary-analysis
footprint. Every count read at tails 30, 60, 120 and 240 with the last
three agreeing; every orbit found below the search bound of 120.
"""

import bisect
import sys
import time
from fractions import Fraction
from math import gcd, lcm

from sympy import Poly, cyclotomic_poly, factor_list, symbols

X = symbols("x")
WIDTH = 4200
NPLACES = 1200          # enough for the selector (K <= lo + 26 s at s <= 40)
MAXLEN = 9
t0 = time.time()
FAILS = []


def report(label, ok):
    print("[%s] %s" % ("ok" if ok else "FAIL", label))
    if not ok:
        FAILS.append(label)


def verdict(label, val):
    print("[verdict] %s -> %s" % (label, val))


# ---- the census's engine, copied unchanged (explore_pisot_confound.py via
# ---- explore_silent_window.py); only WIDTH/NPLACES are larger
def legal(t):
    n = len(t)
    if t[-1] == 0:
        return False
    ext = list(t) + [0] * (2 * n)
    for k in range(1, n):
        if not ext[k:k + n + 1] < ext[:n + 1]:
            return False
    return True


def words(maxlen):
    out = []
    for n in range(2, maxlen + 1):
        for code in range(3 ** n):
            t, c = [], code
            for _ in range(n):
                t.append(c % 3)
                c //= 3
            t = t[::-1]
            if t[0] == 0:
                continue
            out.append(tuple(t))
    return out


def places(t, n=NPLACES):
    L = len(t)
    Q = [1]
    for k in range(1, n):
        if k < L:
            Q.append(sum(t[i] * Q[k - 1 - i] for i in range(k)) + 1)
        else:
            Q.append(sum(t[i] * Q[k - 1 - i] for i in range(L)))
    return Q


def greedy(v, Q):
    d = [0] * WIDTH
    for k in range(bisect.bisect_right(Q, v) - 1, -1, -1):
        while Q[k] <= v:
            if k < WIDTH:
                d[k] += 1
            v -= Q[k]
    assert v == 0, v
    return tuple(d)


def digit_set(v, Q):
    return {k for k, b in enumerate(greedy(v, Q)) if b}


def comb_T(K, Q, lo, step):
    return sum(Q[j] for j in range(lo, K + 1, step))


def agree(a, b, Q):
    da, db = greedy(a, Q), greedy(b, Q)
    i = 0
    while i < WIDTH and da[i] == db[i]:
        i += 1
    return i


def comb_ok(Q, s, lo=None):
    lo = s if lo is None else lo
    Ks = list(range(lo + 6 * s, lo + 12 * s, s))
    for K in Ks:
        if digit_set(comb_T(K, Q, lo, s), Q) != set(range(lo, K + 1, s)):
            return False, False
    ag = [agree(comb_T(K, Q, lo, s), comb_T(K + s, Q, lo, s), Q) for K in Ks]
    return True, all(ag[i] < ag[i + 1] for i in range(len(ag) - 1))


def image_gaps(Q, s, bottom=10, lo=None):
    lo = s if lo is None else lo
    gaps, teeth = set(), []
    for K in range(lo + 20 * s, lo + 26 * s, s):
        ds = [k for k in sorted(digit_set(2 * comb_T(K, Q, lo, s), Q))
              if k >= bottom]
        teeth.append(len(ds))
        gaps |= {ds[i + 1] - ds[i] for i in range(len(ds) - 1)}
    return gaps, (min(teeth) if teeth else 0)


def prefixes(Q, s, deep, span=90, tail=12, lo=None):
    lo = s if lo is None else lo
    seen = []
    for K in range(lo + (span - tail) * s, lo + span * s, s):
        x = greedy(2 * comb_T(K, Q, lo, s), Q)[:deep]
        if x not in seen:
            seen.append(x)
    return seen


# ---- this rig's own readers
TAILS = (30, 60, 120, 240)
PER_SAMPLES, PER_BOUND = 300, 120


def count_ladder(Q, s, lo=None):
    """The count at depth 80 over each tail; the span is tail + 90 so the
    K range read always sits past the census's own settling span."""
    return [len(prefixes(Q, s, 80, span=90 + tl, tail=tl, lo=lo))
            for tl in TAILS]


def orbit(Q, s, lo=None):
    """The label sequence's least period in j, over PER_SAMPLES combs
    starting where the census's reader starts (K = lo + 200 s)."""
    lo = s if lo is None else lo
    seen, seq = {}, []
    for K in range(lo + 200 * s, lo + (200 + PER_SAMPLES) * s, s):
        x = greedy(2 * comb_T(K, Q, lo, s), Q)[:120]
        seq.append(seen.setdefault(x, len(seen)))
    per = next((pp for pp in range(1, PER_BOUND + 1)
                if all(seq[i] == seq[i + pp] for i in range(len(seq) - pp))),
               None)
    return per, len(seen)


def reach(t, s):
    """The place list a reader at step s needs: the period reader ends at
    K = lo + (200 + PER_SAMPLES) s and the tail ladder at lo + 330 s."""
    return places(t, s + (200 + PER_SAMPLES + 2) * s)


def selector(Q, smax=40):
    for s in range(3, smax + 1):
        adm, grows = comb_ok(Q, s)
        if not (adm and grows):
            continue
        g, teeth = image_gaps(Q, s)
        if len(g) == 1 and teeth >= 3:
            return s, sorted(g)[0]
    return None, None


def silent_step(Q, smax=40):
    """explore_silent_window.py's D4 rule: the least admissible growing
    step whose depth-4 prefix count over span 60 / tail 12 exceeds 1."""
    for s in range(3, smax + 1):
        adm, grows = comb_ok(Q, s)
        if not (adm and grows):
            continue
        pref = prefixes(Q, s, 80, span=60, tail=12)
        if len({p[:4] for p in pref}) > 1:
            return s
    return None


# ---- the factorization and the frozen prediction
CYC = {m: Poly(cyclotomic_poly(m, X), X) for m in range(1, 201)}


def parry_poly(t):
    n = len(t)
    return Poly(X ** n - sum(int(c) * X ** (n - 1 - i)
                             for i, c in enumerate(t)), X)


def classify(t):
    """Factor over Z; return (kind, m, mprime, detail)."""
    p = parry_poly(t)
    _, fl = factor_list(p.as_expr(), X)
    facs = [(Poly(f, X), e) for f, e in fl]
    if len(facs) == 1 and facs[0][1] == 1:
        return "irr", None, None, "irreducible"
    # the factor carrying beta: the one with the largest real root
    def top_root(f):
        return max(abs(r) for r in Poly(f, X).nroots(n=30))
    beta_f = max(facs, key=lambda fe: top_root(fe[0]))[0]
    cofs = []
    for f, e in facs:
        if f == beta_f and e == 1:
            continue
        cofs.append((f, e - 1 if f == beta_f else e))
    orders, contracting, wild = [], [], []
    for f, e in cofs:
        m = next((mm for mm, c in CYC.items() if c == f), None)
        if m is not None:
            orders.append(m)
            continue
        big = max(abs(r) for r in f.nroots(n=30))
        (contracting if big < 1 - 1e-9 else wild).append((f, float(big)))
    detail = "beta in %s; cofactors %s" % (
        beta_f.as_expr(),
        [("Phi_%d" % m) for m in orders]
        + ["contracting %s (max |root| %.4f)" % (f.as_expr(), b)
           for f, b in contracting]
        + ["WILD %s (max |root| %.4f)" % (f.as_expr(), b) for f, b in wild])
    if orders:
        m = 1
        for mm in orders:
            m = lcm(m, mm)
        return "cyc", m, (m if m % 2 else m // 2), detail
    if wild:
        return "wild", None, None, detail
    return "con", None, None, detail


def predict(kind, m, mp, A, s):
    if kind == "cyc":
        return lcm(A, mp // gcd(mp, s)), s * lcm(A, m // gcd(m, s))
    if kind == "con":
        return A, A * s
    return None, None


def w(t):
    return "".join(map(str, t))


# ---------------------------------------------------------------- D0
print("--- D0 controls: the seeding rule, then the seven irreducible "
      "speaking windows against A and A x s* ---")
seed_ok = True
for t, want in (((1, 1, 1), [1, 2, 4, 7, 13, 24]),
                ((1, 0, 1), [1, 2, 3, 4, 6, 9])):
    got = places(t, 6)
    print("D0 word %s -> places %s (want %s)" % (w(t), got, want))
    seed_ok = seed_ok and got == want
report("D0 the seeding rule reproduces both known place sequences", seed_ok)
if not seed_ok:
    print("SEEDING FAILED -- no row is read.")
    sys.exit(1)

CONTROLS = [(1, 1), (1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1, 1),
            (1, 1, 1, 1, 1, 1), (1, 0, 1), (1, 0, 0, 1)]
ctrl_ok = True
print("     word     s*  img   A  counts(tails %s)  orbit/s*  A*s*" % (TAILS,))
for t in CONTROLS:
    kind = classify(t)[0]
    Q = places(t)
    s, img = selector(Q)
    A = img // gcd(img, s)
    Q = reach(t, s)
    lad = count_ladder(Q, s)
    per, nlab = orbit(Q, s)
    ok = kind == "irr" and len(set(lad[1:])) == 1 and lad[-1] == A \
        and per == A and per < PER_BOUND
    ctrl_ok = ctrl_ok and ok
    print("     %-7s %3d %4d %3d  %-22s %5s %8d  %s"
          % (w(t), s, img, A, lad, per, A, "" if ok else "<== MISS"))
report("D0 the seven irreducible speaking windows read count = A and "
       "orbit = A x s*", ctrl_ok)
if not ctrl_ok:
    print("CONTROL FAILED -- no row is read.")
    sys.exit(1)

# ---------------------------------------------------------------- D1
print("\n--- D1 the ghost at 10001, in exact arithmetic ---")
T5 = (1, 0, 0, 0, 1)
Q5 = places(T5, 400)
D = [Q5[k] - Q5[k - 2] - Q5[k - 3] for k in range(3, 400)]
print("D1 places %s" % Q5[:16])
print("D1 D_k = q_k - q_{k-2} - q_{k-3}, k = 3..20: %s" % D[:18])
per6 = all(D[i] == D[i + 6] for i in range(len(D) - 6))
report("D1 D_k has period 6 with pattern %s from k = 3" % (D[:6],),
       per6 and D[:6] == [1, 0, -1, -1, 0, 1])
C = {}
base = [Fraction(v, 7) for v in (2, 3, 1, -2, -3, -1)]
for k in range(400):
    C[k] = base[(k - 2) % 6]
P = [Fraction(Q5[k]) - C[k] for k in range(400)]
plastic = all(P[k] == P[k - 2] + P[k - 3] for k in range(3, 400))
print("D1 C_2..C_7 = %s; P_0..P_7 = %s"
      % ([str(c) for c in base], [str(p) for p in P[:8]]))
report("D1 q - C satisfies the plastic recurrence x^3 = x + 1 exactly at "
       "every k in 3..399", plastic)
print("D1 |C| <= 3/7 at every k, so the ghost moves an integer comparison "
      "only at a near-tie of Pisot parts (a property of the decomposition)")

# ---------------------------------------------------------------- D2
print("\n--- D2 the population: legal words to length %d, factored over Z, "
      "predictions frozen before any count ---" % MAXLEN)
LEGAL = [t for t in words(MAXLEN) if legal(t)]
print("D2 legal words: %d" % len(LEGAL))
ROWS = []
for t in LEGAL:
    kind, m, mp, detail = classify(t)
    if kind != "irr":
        ROWS.append(dict(t=t, kind=kind, m=m, mp=mp, detail=detail))
by_kind = {}
for r in ROWS:
    by_kind.setdefault(r["kind"], []).append(w(r["t"]))
print("D2 reducible: %d of %d -- by kind %s"
      % (len(ROWS), len(LEGAL), {k: len(v) for k, v in by_kind.items()}))
for r in ROWS:
    print("     %-10s %-4s m=%-4s m'=%-4s %s"
          % (w(r["t"]), r["kind"], r["m"], r["mp"], r["detail"]))
fam = []
for n in range(3, 12):
    t = (1,) + (0,) * (n - 2) + (1,)
    kind, m, mp, detail = classify(t)
    fam.append((n, kind, m))
    print("D2 family 1 0^%d 1 (n=%d): %s %s" % (n - 2, n, kind, detail))
report("D2 P5: among 1 0^{n-2} 1 for 3 <= n <= 11 exactly n = 5 and n = 11 "
       "are reducible, each with cofactor Phi_6",
       all((kind == "cyc" and m == 6) == (n in (5, 11))
           for n, kind, m in fam)
       and all(kind in ("irr", "cyc") for n, kind, m in fam))
T11 = (1,) + (0,) * 9 + (1,)
if T11 not in [r["t"] for r in ROWS]:
    kind, m, mp, detail = classify(T11)
    ROWS.append(dict(t=T11, kind=kind, m=m, mp=mp, detail=detail))
print("D2 time so far %.1f s" % (time.time() - t0))

# ---------------------------------------------------------------- D3/D4
print("\n--- D3/D4 every reducible word: the selector, then the silent "
      "instrument where it is silent; predicted against measured ---")
print("     word       kind   s*  img   A   count pred/meas   "
      "orbit pred/meas   visits  verdict")
READ, MISS, UNREAD, SILENT = [], [], [], []
for r in ROWS:
    t = r["t"]
    Q = places(t)
    s, img = selector(Q)
    if s is not None:
        A = img // gcd(img, s)
        Q = reach(t, s)
        lad = count_ladder(Q, s)
        per, nlab = orbit(Q, s)
        pc, po = predict(r["kind"], r["m"], r["mp"], A, s)
        stable = len(set(lad[1:])) == 1
        readable = stable and per is not None and per < PER_BOUND
        meas_c = lad[-1]
        meas_o = None if per is None else per * s
        visits = None if per is None else Fraction(per, meas_c)
        r.update(s=s, img=img, A=A, lad=lad, per=per, pc=pc, po=po,
                 meas_c=meas_c, meas_o=meas_o, visits=visits,
                 readable=readable, mode="selector")
        if not readable:
            tag = "UNREAD (ladder %s, per %s)" % (lad, per)
            UNREAD.append(r)
        elif pc is None:
            tag = "no prediction (wild)"
        elif (pc, po) == (meas_c, meas_o):
            tag = "predicted" if t != T5 else "RETRODICTED (the fit row)"
            READ.append(r)
        else:
            tag = "<== MISS"
            MISS.append(r)
        print("     %-10s %-5s %3d %4d %3d   %4s / %-4s     %5s / %-5s   "
              "%5s   %s"
              % (w(t), r["kind"], s, img, A, pc, meas_c, po, meas_o,
                 visits, tag))
    else:
        s = silent_step(Q)
        if s is None:
            r.update(mode="none")
            print("     %-10s %-5s selector silent to 40 and no separating "
                  "comb to 40" % (w(t), r["kind"]))
            SILENT.append(r)
            continue
        Q = reach(t, s)
        lad = count_ladder(Q, s)
        per, nlab = orbit(Q, s)
        stable = len(set(lad[1:])) == 1
        readable = stable and per is not None and per < PER_BOUND
        meas_c = lad[-1]
        visits = None if per is None else Fraction(per, meas_c)
        ratio = None
        if r["kind"] == "cyc":
            ratio = Fraction(r["m"], r["mp"])
        elif r["kind"] == "con":
            ratio = Fraction(1)
        r.update(s=s, A=None, lad=lad, per=per, meas_c=meas_c,
                 meas_o=None if per is None else per * s, visits=visits,
                 readable=readable, mode="prefix", ratio=ratio)
        if not readable:
            tag = "UNREAD (ladder %s, per %s)" % (lad, per)
            UNREAD.append(r)
        elif ratio is None:
            tag = "no prediction (wild)"
        elif visits == ratio:
            tag = "ratio %s predicted" % ratio
            READ.append(r)
        else:
            tag = "<== ratio MISS (predicted %s)" % ratio
            MISS.append(r)
        print("     %-10s %-5s %3d  --  --   -- / %-4s     -- / %-5s   "
              "%5s   %s  [prefix instrument]"
              % (w(t), r["kind"], s, meas_c, r["meas_o"], visits, tag))
print("D3/D4 time so far %.1f s" % (time.time() - t0))

# ---------------------------------------------------------------- D5
print("\n--- D5 the one-tooth carry: greedy digits of 2 q_k as offsets from "
      "k, grouped by k mod 6 ---")


def carry_forms(t, lo=12, hi=60):
    Q = places(t, 400)
    forms = {}
    for k in range(lo, hi + 1):
        off = tuple(sorted(j - k for j in digit_set(2 * Q[k], Q)))
        forms.setdefault(off, []).append(k)
    return forms


for t in (T5, T11, (1, 0, 1), (1, 1, 1)):
    forms = carry_forms(t)
    print("D5 %s: %d carry form(s)" % (w(t), len(forms)))
    for off, ks in sorted(forms.items(), key=lambda kv: kv[1][0]):
        print("     offsets %-28s at k mod 6 = %s (k = %s...)"
              % (off, sorted({k % 6 for k in ks}), ks[:6]))
f5 = carry_forms(T5)
one_form = len(f5) == 1
by_res = all(len({k % 6 for k in ks}) == 1 or len(ks) == 1
             for ks in f5.values())
verdict("D5 K6: the carry at 10001 is ONE form at every k in 12..60",
        one_form)
report("D5 P6: the carry at 10001 takes more than one form and each form "
       "sits at one residue of k mod 6", (not one_form) and by_res)

# ---------------------------------------------------------------- D6
print("\n--- D6 the table and the verdicts ---")
cyc_read = [r for r in READ if r["kind"] == "cyc" and r["t"] != T5]
con_read = [r for r in READ if r["kind"] == "con"]
cyc_miss = [r for r in MISS if r["kind"] == "cyc"]
con_miss = [r for r in MISS if r["kind"] == "con"]
print("D6 read and predicted: %d (cyclotomic beyond 10001: %s; "
      "contracting: %s)"
      % (len(READ), [w(r["t"]) for r in cyc_read],
         [w(r["t"]) for r in con_read]))
print("D6 misses: %s" % [(w(r["t"]), r["kind"]) for r in MISS])
print("D6 unread: %s" % [w(r["t"]) for r in UNREAD])
print("D6 silent under both instruments: %s" % [w(r["t"]) for r in SILENT])
verdict("D6 K4: no reducible word beyond 10001 read by either instrument",
        not [r for r in READ + MISS if r["t"] != T5])
report("D6 P3: the law (a) holds at every read cyclotomic row beyond 10001, "
       "and there is at least one", bool(cyc_read) and not cyc_miss)
report("D6 P4: the law (b) holds at every read contracting row",
       not con_miss)
verdict("D6 P4 has at least one contracting row to hold at", bool(con_read))

# ---------------------------------------------------------------- D7
# ADDED AFTER D0-D6 RAN AND FROZEN BEFORE IT RAN. D6's table said the
# ghost law misses at nearly every reducible word while retrodicting 10001,
# and no contracting cofactor appeared at all. Four things the hand can
# settle, each frozen here as a prediction the print then checks:
#  P7 KRONECKER: a cofactor R of a Parry polynomial is monic over Z with
#     constant term dividing -t_n != 0, so the product of its roots' moduli
#     is at least 1: R cannot be contracting. If every root has modulus
#     <= 1, Kronecker makes R cyclotomic. So the kinds are cyc and wild only,
#     at every legal word, and law (b) is vacuous.
#  P8 THE GHOST CRITERION: with T(x) = sum t_i x^i the places' generating
#     function is Q(x) = (1 - x^n) / ((1 - x)(1 - T(x))) -- the "+1" of the
#     seeding runs exactly over k = 0..n-1 -- and 1 - T(x) is the reciprocal
#     of the Parry polynomial. The ghost on a cyclotomic factor Phi_m is the
#     partial fraction at its roots, and it VANISHES iff Phi_m divides
#     1 + x + ... + x^{n-1}, i.e. iff m | n (for a simple factor; a repeated
#     Phi_m always leaves one). So: ghost nonzero iff some m_i does not
#     divide n, or some Phi_m is repeated. Read against the residual of the
#     beta-factor's own recurrence, computed exactly at every cyc word.
#  P9 THE DEFECT AT 10001: 2x^5 - x^7 - 1 vanishes modulo x^3 - x - 1, so
#     2 q_k - q_{k+2} - q_{k-5} = 3 C_k - 2 C_{k+1} exactly -- an INTEGER,
#     both sides being integers -- running 0, 1, 1, 0, -1, -1 at
#     k = 2, 3, 4, 5, 0, 1 mod 6. The greedy digits of 2 q_k then contain
#     {k+2, k-5} at defect 0, {k+2, k-5, 0} at defect +1 (q_0 = 1), and at
#     defect -1 a different representation, which is D5's growing comb.
#  P9b THE POPULATION THAT CAN READ A GHOST is the binary one: at t_1 = 2
#     the greedy digits of 2 T_K are the digit 2 on the comb (the census's
#     no-carry mechanism), so no carry identity is ever invoked and the
#     ghost has nothing to enter. Predict: every selector-read miss in D6
#     has t_1 = 2 and A = 1, and the binary reducible words are the whole
#     of the prefix-instrument rows.
print("")
print("--- D7 added after the run: Kronecker, the ghost criterion, the "
      "defect, and the population ---")
kinds = {r["kind"] for r in ROWS}
report("D7 P7: every cofactor is cyclotomic or wild (no contracting cofactor "
       "at any of the %d reducible words), as Kronecker forces" % len(ROWS),
       kinds <= {"cyc", "wild"})


def ghost_residual(t):
    """The residual of the beta-factor's recurrence on the seeded places,
    exact."""
    p = parry_poly(t)
    _, fl = factor_list(p.as_expr(), X)
    facs = [(Poly(f, X), e) for f, e in fl]
    bf = max(facs, key=lambda fe: max(abs(r) for r in fe[0].nroots(n=30)))[0]
    co = [int(c) for c in bf.all_coeffs()]
    d = len(co) - 1
    Q = places(t, 240)
    return [sum(co[i] * Q[k - i] for i in range(d + 1)) for k in range(d, 240)]


def cyc_orders(t):
    p = parry_poly(t)
    _, fl = factor_list(p.as_expr(), X)
    out = []
    for f, e in fl:
        m = next((mm for mm, c in CYC.items() if c == Poly(f, X)), None)
        if m is not None:
            out.append((m, e))
    return out


crit_ok, crit_bad, nz_count = True, [], 0
for r in ROWS:
    if r["kind"] != "cyc":
        continue
    t = r["t"]
    n = len(t)
    D = ghost_residual(t)
    nz = any(D)
    r["ghost"] = nz
    nz_count += nz
    orders = cyc_orders(t)
    pred = any(n % m != 0 or e > 1 for m, e in orders)
    if pred != nz:
        crit_ok = False
        crit_bad.append((w(t), orders, nz))
print("D7 ghost nonzero at %d of %d cyclotomic words; criterion failures: %s"
      % (nz_count, sum(r["kind"] == "cyc" for r in ROWS), crit_bad))
report("D7 P8: the ghost is nonzero iff some Phi_m has m not dividing n or "
       "is repeated, at every cyclotomic word", crit_ok)
by_m = {}
for r in ROWS:
    if r["kind"] == "cyc":
        by_m.setdefault(r["m"], [0, 0])[r["ghost"]] += 1
print("D7 by m: {m: [ghost zero, ghost nonzero]} = %s" % by_m)

d5 = [2 * Q5[k] - Q5[k + 2] - Q5[k - 5] for k in range(5, 300)]
want = {2: 0, 3: 1, 4: 1, 5: 0, 0: -1, 1: -1}
ok9 = all(d5[k - 5] == want[k % 6] for k in range(5, 300)) and \
    all(Fraction(d5[k - 5]) == 3 * C[k] - 2 * C[k + 1] for k in range(5, 300))
print("D7 defect 2 q_k - q_{k+2} - q_{k-5} at k = 5..22: %s" % d5[:18])
digs_ok = True
for k in range(12, 200):
    ds = digit_set(2 * Q5[k], Q5)
    dk = want[k % 6]
    if dk == 0:
        digs_ok = digs_ok and ds == {k + 2, k - 5}
    elif dk == 1:
        digs_ok = digs_ok and ds == {k + 2, k - 5, 0}
    else:
        digs_ok = digs_ok and not ({k + 2, k - 5} <= ds)
report("D7 P9: the defect is 3 C_k - 2 C_{k+1}, an integer running "
       "0, 1, 1, 0, -1, -1 by k mod 6, and the greedy digits of 2 q_k are "
       "{k+2, k-5} (+ q_0 at +1) except at -1, for k in 12..199",
       ok9 and digs_ok)

sel_miss = [r for r in MISS if r["mode"] == "selector"]
report("D7 P9b: every selector-read miss has t_1 = 2 and A = 1 (%d misses)"
       % len(sel_miss),
       all(r["t"][0] == 2 and r["A"] == 1 for r in sel_miss))
pre_rows = [r for r in ROWS if r.get("mode") == "prefix"]
report("D7 P9b: the prefix-instrument rows are exactly the binary reducible "
       "words (%d)" % len(pre_rows),
       all(max(r["t"]) == 1 for r in pre_rows)
       and all(r.get("mode") == "prefix" for r in ROWS
               if max(r["t"]) == 1 and r["t"] != T5))
print("D7 the binary reducible words, with m, ghost, and the reading:")
for r in ROWS:
    if max(r["t"]) > 1:
        continue
    print("     %-12s m=%-3s ghost=%-5s mode=%-8s count=%-4s orbit=%-5s "
          "visits=%s" % (w(r["t"]), r["m"], r.get("ghost"), r.get("mode"),
                         r.get("meas_c"), r.get("meas_o"), r.get("visits")))
ghost_sel = [r for r in ROWS if r.get("ghost") and r.get("mode") == "selector"
             and r.get("readable")]
distinct = [r for r in ghost_sel if (r["pc"], r["po"]) != (r["A"], r["A"] * r["s"])]
hits = [r for r in distinct
        if (r["pc"], r["po"]) == (r["meas_c"], r["meas_o"])]
print("D7 selector-read rows with a NONZERO ghost: %d, of which the ghost "
      "prediction differs from the ghost-free (A, A s*) at %d; it lands at %s"
      % (len(ghost_sel), len(distinct), [w(r["t"]) for r in hits]))
verdict("D7 the ghost prediction lands at the plastic row ALONE among the "
        "selector-read nonzero-ghost rows where it differs from the null",
        [w(r["t"]) for r in hits] == ["10001"])

print("\nwall-clock %.1f s" % (time.time() - t0))
print("FAILS: %s" % (FAILS or "none"))
