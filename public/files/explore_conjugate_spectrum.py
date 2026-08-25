"""The conjugate spectrum of a numeration window: is a binary window's
shape in the completion atlas read off its Parry polynomial's non-beta
roots?

THE QUESTION
------------
The silent-window census (explore_silent_window.py, D7) sorted the 21
legal binary windows to length 6 by one instrument -- the number of
distinct depth-80 prefixes of the doubled comb's image over tails of
120, 240 and 480 samples -- and found two behaviours: at most windows
the count SATURATES (it reads phases, and the controls Tribonacci and
10101 print 3, 3, 3 and 5, 5, 5), while at 100001, 101001 and 110101
every sample is distinct at every tail, the FIFTH SHAPE, unboundedly
many limit points over one input limit. What that census left open is
the proof: no cascade argument was derived for any silent window. The
ghost rig (explore_cyclotomic_ghost.py) then read the COFACTOR of a
reducible Parry polynomial -- cyclotomic factors carry a periodic ghost
-- and filed every irreducible polynomial as "irr", never asking about
beta's own conjugates.

THE HAND-ATTACK, before any engine. The Parry polynomial's largest root
modulus after beta, cofactors included, at the 21 windows:
  inside the circle (beta Pisot, irreducible)   11 101 111 1001 1111
        10101 11001 11011 11101 11111 110011 111011 111111 -- the 13
        settled windows, spine and fourth shape together;
  ON the circle (a cyclotomic cofactor)         1101 10001 110001
        111001 111101 -- the ghost rows;
  OUTSIDE the circle (beta not Pisot)           100001 (1.03283),
        101001 (1.04260), 110101 (1.12847) -- exactly the three
        fifth-shape windows and no other.
The settled row that settles LAST, 111011 (tail-12 reading capped, then
17 phases), has the settled rows' conjugate nearest the circle
(0.98533). And 1 0^9 1, named as a second ghost window, carries beside
its Phi_6 factor a cofactor root at 1.07565: a growing component under
the periodic one.

THE MECHANISM, and the transplant flagged. The places obey the Parry
recurrence, so q_k = sum c_i alpha_i^k over the polynomial's roots: a
root inside the circle decays, a root on it is a ghost of fixed
amplitude, a root outside GROWS. The finiteness of the phase count at a
Pisot beta is the Berend-Frougny theorem -- normalization in base beta
is computable by a finite automaton if and only if beta is Pisot
(Frougny 1992 for the Pisot direction, Berend and Frougny 1994 for the
converse) -- read through the census's instrument: 2 T(K) is a sum of
places, its greedy digits are the normalization of the digit string 2
on the comb's positions, and a finite transducer produces them, so the
low prefixes over the comb's tail take finitely many values. That gives
the Pisot direction outright. The theorem is about normalization on a
fixed alphabet over ALL strings, while the census reads ONE string
family at one bounded depth; so at a non-Pisot beta the theorem only
MOTIVATES the fifth shape -- a non-Pisot beta could in principle still
normalize this one family finitely -- and that is what the sweep tests.

THE POPULATION, counted. Legal binary words to length 9: 125 -- 62 WILD
(a root outside the circle), 63 Pisot, of which 18 carry a cyclotomic
cofactor and 15 have a conjugate above 0.98. The wild rows' second root
runs from 1.0073 (110010001) to 1.1839 (11010101), its 480th power from
33 to 10^35. A wild root barely outside the circle grows too slowly to
show at the instrument's tails -- the same reason near-unit Pisot rows
settle late -- so the SCORED wild set is frozen at |alpha_2| >= 1.03,
just under the smallest known fifth-shape row (100001 at 1.03283); the
wild rows below 1.03 are read, reported and never scored: the
instrument's margin, named before the run.

THE STATISTIC'S ALGEBRA. The count at tail T is a count of distinct
depth-80 prefixes over T samples, capped at T. Three readings off the
printed triple at tails 120 / 240 / 480: DISTINCT = (120, 240, 480)
exactly; FLAT = the three equal; GROWING otherwise (capped, not
saturated -- the late-settler reading). One step per window: the
single-step selector's step where it speaks, else the census's silent
step (the least admissible growing step whose depth-4 prefix count over
span 60 / tail 12 exceeds 1), else the row is UNREAD and said so. The
instrument, its dials (depth 80, span = tail + 150, WIDTH 6000, steps
3..40) and the step rules are the census's own, carried unchanged --
what is new is the root classification and the per-row prediction,
which is read off the polynomial and touches no dial. Places are
generated to 632 s + 2 so that span 630 at step s fits.

THE DESIGN -- predictions frozen before the run; a kill names what the
rig PRINTS.
  P1  Every scored wild row (|alpha_2| >= 1.03) prints DISTINCT.
      KILL: a scored wild row prints FLAT.
  P2  Every Pisot row prints FLAT or GROWING, never DISTINCT.
      KILL: a Pisot row prints (120, 240, 480).
  P3  Every ghost row (Pisot beta with a cyclotomic cofactor) prints
      FLAT like the other Pisot rows: a ghost is periodic and adds
      phases, never samples. KILL: a ghost row prints DISTINCT.
  P4  GROWING among Pisot rows belongs to the near-unit ones: every
      GROWING Pisot row has |alpha_2| > 0.95. KILL: a GROWING Pisot row
      with |alpha_2| < 0.95.
  P5  1 0^9 1 prints DISTINCT (wild at 1.07565 beside its Phi_6).
POSITIVE CONTROLS, run first; no row is read unless all three pass:
Tribonacci (111, step 4) prints 3, 3, 3; 10101 (step 3) prints 5, 5, 5;
100001 at its silent step prints 120, 240, 480 -- the census's D7.
RETRODICTION, stated and worth nothing as evidence: the 21-word split
above against the census's record.

STAGE 2 -- frozen after stage 1 printed and before it ran. Stage 1's
wild rows sorted by |alpha_2| are a BAND and not a threshold: every wild
row below 1.020 prints FLAT, every one above 1.048 prints DISTINCT (one
at 120, 240, 479), and the band between is mixed -- and |alpha_2|^K at
K ~ 2000 is astronomical on both sides of 1.03, so the growth rate is
not what decides a FLAT wild row. The FLAT wild rows print spine-like
counts (3, 3, 3; 5, 5, 5), the counts of a window whose doubling closes
in a FIXED carry: the CASCADE, 2 q_k = a sum of q_{k-i} over a fixed
finite offset set, an identity of the recurrence and not of the roots
(the one-tooth carry of the spine, Narayana's two, 10101's three).
Observable A, the cascade depth: the greedy digit set of 2 q_k at
k = 300, 600, 1200 as offsets from k -- FINITE = the same offset set at
all three k and no digit below k - 60; INFINITE = a digit below
position 60 at k = 1200, the expansion running to the floor; anything
else OTHER, reported. Observable B: DISTINCT at 480 is also what a
finite set with least period above 480 prints, so the two ghost rows
that printed DISTINCT and the two rows at 479 are read again at tails
960 and 1920.
  Q1  Every FLAT wild row has a FINITE cascade. KILL: a FLAT wild row
      with an INFINITE cascade.
  Q2  Every DISTINCT wild row has an INFINITE cascade. KILL: a DISTINCT
      wild row with a FINITE cascade.
  Q3  1001001 and 10100101 print FLAT by tail 1920 (a ghost's long
      period, finite). KILL: 960 and 1920 distinct at both.
  Q4  Pisot rows may have either cascade -- Berend-Frougny bounds the
      carry without closing it -- so no kill; the split is REPORTED.

STAGE 3 -- frozen after stages 1 and 2 printed. The two cofactor
exceptions are read by a second reader, explore_cyclotomic_ghost.py's
orbit reader carried unchanged: depth-120 prefixes over 300 combs
starting at K = lo + 200 s, the label sequence's least period searched
to 120. Q5: at 1001001 and 10100101 the reader prints 300 distinct
labels and no period; the controls 111 and 10101 print their counts (3
and 5) with a period. KILL: a period found at either exception.

FINDINGS (post-run; the printed output copied, nothing inferred)
----------------------------------------------------------------
The controls pass (3, 3, 3; 5, 5, 5; 120, 240, 480). 125 words, 125
read, none unread. Two counts in the frozen population paragraph were
wrong and the tally is the record: 24 ghost rows among the 63 Pisot
rows (not 18), and 5 of the 62 wild rows also carry a cyclotomic
factor; the scored wild set is 41 and the margin 21 (not 50 and 12).

F1  THE LAW AS FROZEN IS DEAD IN BOTH DIRECTIONS AT LENGTH 7 TO 9.
    Scored wild (41): 34 DISTINCT, 6 FLAT -- 1010001 (1.0442, count
    7), 1110101 (1.0312, 5), 11000011 (1.0377, 4), 110110001 (1.0314,
    3), 111110011 (1.0472, 9), 111110101 (1.0472, 3) -- and 100000001
    at 120, 240, 479. Margin wild (21): 17 FLAT, 4 DISTINCT (11001011,
    11100101, 101000001, 111100011, at 1.0212 to 1.0285). Pisot (63):
    61 FLAT and 2 DISTINCT, both GHOST rows -- 1001001 (Phi_4, alpha_2
    0.9337) and 10100101 (Phi_3, 0.9709) -- and both still every-sample
    -distinct at tails 960 and 1920. P1, P2, P3 killed; P4 vacuous (no
    Pisot row GROWING; the latest settler is FLAT at alpha_2 0.9967).
    At length <= 6 the retrodiction holds exactly (wild = 100001,
    101001, 110101).

F2  WHAT SURVIVES IS THE THEOREM'S OWN HYPOTHESIS, READ EXACTLY. The
    classical statement (Frougny 1992, as restated in Frougny 2002,
    Sect. 2.6) is: for a linearly recurrent sequence whose
    characteristic polynomial is EXACTLY the minimal polynomial of a
    Pisot number, normalization on any alphabet is computable by a
    finite automaton -- and the Parry seeding here is that paper's
    Fibonacci-like sequence to the letter. Every one of the 39 Pisot
    rows with an IRREDUCIBLE Parry polynomial prints FLAT (rule at
    scanned scope, 39 of 39), and both DISTINCT Pisot rows are outside
    the hypothesis, their polynomial being beta's minimal polynomial
    times a cyclotomic factor. The route from the automaton to a
    settled count: a rational function is a composition of a
    left-sequential and a right-sequential function (Elgot-Mezei), and
    the doubled comb's digit string read from either end is eventually
    periodic in K with period a multiple of s, so the depth-80 prefix
    is eventually periodic in K and the count saturates. The
    Berend-Frougny converse (no finite automaton at a non-Pisot base)
    says nothing about one string family, and the sweep is the
    measurement of that gap: 23 of 62 non-Pisot rows print FLAT.

F3  SO THE FIFTH SHAPE NEEDS THE HYPOTHESIS TO FAIL, AND WHERE IT FAILS
    EITHER SHAPE OCCURS (rule in range for the first clause, 125 of
    125: every DISTINCT row is a non-Pisot row or a ghost row;
    observation for the second). Outside the hypothesis: 38 of 62
    non-Pisot rows DISTINCT, 23 FLAT, 1 at 479; 2 of 24 ghost rows
    DISTINCT, 22 FLAT. No root reads which: sorted by alpha_2 the
    non-Pisot rows are all FLAT below 1.020 and all DISTINCT above
    1.048, mixed between, and alpha_2^K is astronomical on both sides.

F4  THE CASCADE OF 2 DOES NOT SORT THEM EITHER. The greedy expansion of
    2 q_k is FINITE at only 2 of the 62 non-Pisot rows -- 11001001
    (FLAT, offsets 10, 8, 5, 3, -1) and 111100011 (DISTINCT, offsets
    13, 12, 9, 8, 6, 5, -1) -- and INFINITE at the other 60, FLAT and
    DISTINCT alike (Q1 killed by 22 rows, Q2 by one). A finite
    expansion of 2 does not close the comb: the doubled teeth's
    expansions overlap at step s and their sum normalizes again. Among
    Pisot rows the cascade is FINITE at 34 (26 irreducible, 8 ghost)
    and INFINITE at 29, the count FLAT either way -- the automaton
    bounds the carry without closing it, as Q4 said.

F5  1 0^9 1 IS NOT A SECOND GHOST WINDOW FOR THE COUNT TO READ. Beside
    its Phi_6 factor its cofactor carries a root at 1.07565, and its
    count prints 120, 240, 479 and 958, 1918 -- one to two repeated
    prefixes in every tail, the fifth shape with a coincidence rather
    than a period (P5 killed by the letter, 479 not 480, and read as
    that). 100000001 prints the same at 479 and 959, 1919.

F6  One sort read AFTER the run and unfrozen (observation): the 6
    non-Pisot rows whose extra root outside the circle is REAL
    (negative) all print DISTINCT; the 56 whose extra roots are a
    complex pair split 32 DISTINCT, 23 FLAT, 1 at 479.

F7  THE TWO EXCEPTIONS READ THE SAME ON THE SECOND READER (Q5 passes):
    the ghost rig's orbit reader prints 300 distinct depth-120 labels
    over 300 combs and no period to 120 at both 1001001 and 10100101,
    where the controls print 3 labels with period 3 (Tribonacci) and 5
    with period 5 (10101). Two readers, two depths, two K ranges, one
    reading.

TIERS. F2's first clause: rule at scanned scope (39 of 39), the
finiteness argued from the classical automaton through Elgot-Mezei and
not proved here for this instrument's depth. F3's first clause: rule in
range (125 of 125 to length 9). F1, F3's second clause, F4, F5, F6:
observation at scanned scope. Others' results keep their names:
Frougny 1992 (normalization in a Pisot-minimal-polynomial linear
numeration system), Berend-Frougny 1994 (the base-beta converse),
Elgot-Mezei 1965 (the sequential decomposition).

RUN RECORD: one process, 19.7 s wall-clock, peak working set 73 MB
under memwatch (limit 512), sympy for the factorization and the roots.
CS_MAXLEN=6 reproduces the census's 21 rows in 2.7 s.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import bisect
import sys
import time

from sympy import Poly, cyclotomic_poly, factor_list, symbols

t0 = time.time()
X = symbols("x")
WIDTH = 6000
MAXLEN = int(os.environ.get("CS_MAXLEN", "9"))
TAILS = (120, 240, 480)
DEPTH = 80
SCORED_WILD = 1.03
NEAR_UNIT = 0.95

FAILS = []


def report(label, ok):
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        FAILS.append(label)


def verdict(label, val):
    print("VERDICT %s: %s" % (label, val))


# ---- the census's engine, carried unchanged (explore_silent_window.py)
def legal(t):
    n = len(t)
    if t[-1] == 0:
        return False
    ext = list(t) + [0] * (2 * n)
    for k in range(1, n):
        if not ext[k:k + n + 1] < ext[:n + 1]:
            return False
    return True


def binary_words(maxlen):
    out = []
    for n in range(2, maxlen + 1):
        for code in range(2 ** n):
            t = tuple((code >> (n - 1 - i)) & 1 for i in range(n))
            if t[0] == 1 and legal(t):
                out.append(t)
    return out


def places(t, n):
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


def selector(Q, smax=40):
    for s in range(3, smax + 1):
        adm, grows = comb_ok(Q, s)
        if not (adm and grows):
            continue
        g, teeth = image_gaps(Q, s)
        if len(g) == 1 and teeth >= 3:
            return s
    return None


def silent_step(Q, smax=40):
    for s in range(3, smax + 1):
        adm, grows = comb_ok(Q, s)
        if not (adm and grows):
            continue
        pref = prefixes(Q, s, 80, span=60, tail=12)
        if len({p[:4] for p in pref}) > 1:
            return s
    return None


# ---- this rig's own reading: the root classification
CYC = {m: Poly(cyclotomic_poly(m, X), X) for m in range(1, 80)}


def parry_poly(t):
    n = len(t)
    return Poly(X ** n - sum(int(c) * X ** (n - 1 - i)
                             for i, c in enumerate(t)), X)


def classify(t):
    """(kind, alpha2, cyclotomic orders): kind is 'wild' if some non-beta,
    non-cyclotomic root has modulus > 1, else 'pisot'; alpha2 the largest
    non-beta modulus among the non-cyclotomic roots."""
    p = parry_poly(t)
    _, fl = factor_list(p.as_expr(), X)
    orders, mods = [], []
    for f, e in fl:
        fp = Poly(f, X)
        m = next((mm for mm, c in CYC.items() if c == fp), None)
        if m is not None:
            orders.append(m)
            continue
        mods += [abs(r) for r in fp.nroots(n=30)] * e
    mods.sort(reverse=True)
    beta = float(mods[0])
    alpha2 = float(mods[1]) if len(mods) > 1 else 0.0
    kind = "wild" if alpha2 > 1 + 1e-9 else "pisot"
    return kind, beta, alpha2, orders


def w(t):
    return "".join(map(str, t))


def shape(counts):
    if list(counts) == list(TAILS):
        return "DISTINCT"
    if counts[0] == counts[1] == counts[2]:
        return "FLAT"
    return "GROWING"


def read_row(t, s):
    Q = places(t, 632 * s + 2)
    return [len(prefixes(Q, s, DEPTH, span=tl + 150, tail=tl)) for tl in TAILS]


def step_for(t):
    Q = places(t, 41 * 62)
    s = selector(Q)
    how = "selector"
    if s is None:
        s = silent_step(Q)
        how = "silent"
    return s, how


# ---------------------------------------------------------------- controls
print("=== the conjugate spectrum of a numeration window (binary words to "
      "length %d) ===" % MAXLEN)
print("\n--- positive controls: the census's D7 rows, read with the same "
      "instrument ---")
ctrl_ok = True
for t, s_fixed, want in (((1, 1, 1), 4, [3, 3, 3]),
                         ((1, 0, 1, 0, 1), 3, [5, 5, 5]),
                         ((1, 0, 0, 0, 0, 1), None, list(TAILS))):
    s = s_fixed if s_fixed is not None else step_for(t)[0]
    cs = read_row(t, s)
    print("     %-8s s=%2d  count by tail 120/240/480: %s  (want %s)"
          % (w(t), s, cs, want))
    ctrl_ok = ctrl_ok and cs == want
report("C  the three controls print the census's own numbers", ctrl_ok)
if not ctrl_ok:
    print("CONTROL FAILED -- no row is read.")
    print("\nwall-clock %.1f s" % (time.time() - t0))
    sys.exit(1)

# ---------------------------------------------------------------- the sweep
print("\n--- the sweep: every legal binary word to length %d, classified "
      "by its non-beta roots, then read ---" % MAXLEN)
print("     word       kind   beta    alpha2  cofactor   step      "
      "count 120/240/480   shape")
rows = []
for t in binary_words(MAXLEN):
    kind, beta, a2, orders = classify(t)
    s, how = step_for(t)
    if s is None:
        cs, sh = None, "UNREAD"
    else:
        cs = read_row(t, s)
        sh = shape(cs)
    rows.append(dict(t=t, w=w(t), kind=kind, beta=beta, a2=a2,
                     orders=orders, s=s, how=how, cs=cs, shape=sh))
    print("     %-10s %-6s %.5f %.5f  %-9s  %-13s %-18s %s"
          % (w(t), kind, beta, a2,
              ("Phi_" + ",".join(map(str, orders))) if orders else "-",
              ("s=%d %s" % (s, how)) if s else "none",
              str(cs) if cs else "-", sh))
    sys.stdout.flush()

read = [r for r in rows if r["cs"] is not None]
unread = [r for r in rows if r["cs"] is None]
wild = [r for r in read if r["kind"] == "wild"]
pisot = [r for r in read if r["kind"] == "pisot"]
ghost = [r for r in pisot if r["orders"]]
scored = [r for r in wild if r["a2"] >= SCORED_WILD]
margin = [r for r in wild if r["a2"] < SCORED_WILD]

print("\n--- the tally ---")
print("     %d words; %d read, %d unread (no admissible growing step): %s"
      % (len(rows), len(read), len(unread), [r["w"] for r in unread]))
print("     wild %d (scored %d at |alpha2| >= %.2f, margin %d below it); "
      "pisot %d (ghost rows %d)"
      % (len(wild), len(scored), SCORED_WILD, len(margin), len(pisot),
         len(ghost)))
for name, grp in (("scored wild", scored), ("margin wild", margin),
                  ("pisot", pisot), ("ghost", ghost)):
    tally = {}
    for r in grp:
        tally[r["shape"]] = tally.get(r["shape"], 0) + 1
    print("     %-12s %s" % (name, tally))

# ---------------------------------------------------------------- verdicts
p1_bad = [r["w"] for r in scored if r["shape"] == "FLAT"]
p1_ng = [r["w"] for r in scored if r["shape"] == "GROWING"]
report("P1 every scored wild row prints DISTINCT (FLAT would kill)",
       not p1_bad and not p1_ng)
verdict("P1 scored wild rows FLAT", p1_bad)
verdict("P1 scored wild rows GROWING (neither reading)", p1_ng)
print("     margin wild rows by shape: %s"
      % [(r["w"], "%.4f" % r["a2"], r["shape"]) for r in margin])

p2_bad = [r["w"] for r in pisot if r["shape"] == "DISTINCT"]
report("P2 no Pisot row prints DISTINCT", not p2_bad)
verdict("P2 Pisot rows DISTINCT", p2_bad)

p3_bad = [r["w"] for r in ghost if r["shape"] == "DISTINCT"]
p3_grow = [r["w"] for r in ghost if r["shape"] == "GROWING"]
report("P3 no ghost row prints DISTINCT", not p3_bad)
verdict("P3 ghost rows GROWING", p3_grow)

p4_rows = [r for r in pisot if r["shape"] == "GROWING"]
p4_bad = [(r["w"], "%.4f" % r["a2"]) for r in p4_rows if r["a2"] < NEAR_UNIT]
report("P4 every GROWING Pisot row has |alpha2| > %.2f" % NEAR_UNIT,
       not p4_bad)
verdict("P4 GROWING Pisot rows (word, alpha2)",
        sorted(((r["w"], "%.4f" % r["a2"]) for r in p4_rows),
               key=lambda x: x[1]))
verdict("P4 largest alpha2 among FLAT Pisot rows",
        max(("%.4f" % r["a2"] for r in pisot if r["shape"] == "FLAT"),
            default=None))

T11 = (1,) + (0,) * 9 + (1,)
kind11, beta11, a211, ord11 = classify(T11)
s11, how11 = step_for(T11)
cs11 = read_row(T11, s11) if s11 else None
print("\n     1 0^9 1: %s beta %.5f alpha2 %.5f cofactor Phi_%s step %s "
      "(%s) count %s -> %s"
      % (kind11, beta11, a211, ord11, s11, how11, cs11,
         shape(cs11) if cs11 else "UNREAD"))
report("P5 1 0^9 1 prints DISTINCT", cs11 is not None and
       shape(cs11) == "DISTINCT")

# ---------------------------------------------------------------- stage 2
print("\n--- stage 2, observable A: the cascade -- the greedy digit set of "
      "2 q_k as offsets from k, at k = 300 / 600 / 1200 ---")
CASC_K = (300, 600, 1200)


def cascade(t):
    Q = places(t, CASC_K[-1] + 40)
    offs, lows = [], []
    for k in CASC_K:
        ds = sorted(digit_set(2 * Q[k], Q))
        offs.append(tuple(k - d for d in ds))
        lows.append(ds[0])
    if offs[0] == offs[1] == offs[2] and min(lows[i] >= CASC_K[i] - 60
                                             for i in range(3)):
        return "FINITE", offs[0], lows
    if lows[2] < 60:
        return "INFINITE", offs[2][:6], lows
    return "OTHER", offs[2][:6], lows


for r in rows:
    kind, off, lows = cascade(r["t"])
    r["casc"], r["off"], r["lows"] = kind, off, lows
casc_tally = {}
for r in rows:
    key = (r["kind"], "ghost" if r["orders"] else "irr", r["shape"], r["casc"])
    casc_tally[key] = casc_tally.get(key, 0) + 1
print("     (kind, factor, shape, cascade) -> rows")
for key in sorted(casc_tally):
    print("     %-40s %d" % (key, casc_tally[key]))
print("     FINITE cascades among wild rows (word, alpha2, shape, offsets):")
for r in rows:
    if r["kind"] == "wild" and r["casc"] == "FINITE":
        print("        %-10s %.4f %-9s %s" % (r["w"], r["a2"], r["shape"],
                                              r["off"]))
print("     wild rows NOT finite, by shape (word, alpha2, shape, cascade, "
      "lowest digit at k = 300/600/1200):")
for r in rows:
    if r["kind"] == "wild" and r["casc"] != "FINITE":
        print("        %-10s %.4f %-9s %-9s %s" % (r["w"], r["a2"], r["shape"],
                                                   r["casc"], r["lows"]))

q1_bad = [r["w"] for r in wild if r["shape"] == "FLAT" and r["casc"] != "FINITE"]
report("Q1 every FLAT wild row has a FINITE cascade", not q1_bad)
verdict("Q1 FLAT wild rows without a finite cascade",
        [(r["w"], r["casc"], r["lows"]) for r in wild
         if r["shape"] == "FLAT" and r["casc"] != "FINITE"])
q2_bad = [r["w"] for r in wild if r["shape"] == "DISTINCT" and r["casc"] == "FINITE"]
report("Q2 every DISTINCT wild row has an INFINITE cascade", not q2_bad)
verdict("Q2 DISTINCT wild rows with a finite cascade", q2_bad)
verdict("Q4 Pisot rows by (factor, shape, cascade)",
        {k[1:]: v for k, v in casc_tally.items() if k[0] == "pisot"})

print("\n--- stage 2, observable B: the DISTINCT ghost rows and the 479 rows "
      "at tails 960 and 1920 ---")
LONG = (960, 1920)


def read_long(t, s):
    Q = places(t, (LONG[-1] + 152) * s + 2)
    return [len(prefixes(Q, s, DEPTH, span=tl + 150, tail=tl)) for tl in LONG]


long_rows = {}
for t in ((1, 0, 0, 1, 0, 0, 1), (1, 0, 1, 0, 0, 1, 0, 1),
          (1, 0, 0, 0, 0, 0, 0, 0, 1), T11):
    s = step_for(t)[0]
    cl = read_long(t, s)
    long_rows[w(t)] = cl
    print("     %-12s s=%2d  count by tail 960/1920: %s  %s"
          % (w(t), s, cl, "every sample distinct" if cl == list(LONG)
             else ("FLAT" if cl[0] == cl[1] else "GROWING")))
q3_ok = all(long_rows[k][0] == long_rows[k][1]
            for k in ("1001001", "10100101"))
report("Q3 the two DISTINCT ghost rows print FLAT by tail 1920", q3_ok)
verdict("Q3 ghost rows still distinct at 1920",
        [k for k in ("1001001", "10100101") if long_rows[k] == list(LONG)])

# ---------------------------------------------------------------- stage 3
print("\n--- stage 3: the ghost rig's orbit reader at the two cofactor "
      "exceptions (depth 120, 300 combs from K = lo + 200 s, period to 120) "
      "---")
PER_SAMPLES, PER_BOUND = 300, 120


def orbit(Q, s, lo=None):
    lo = s if lo is None else lo
    seen, seq = {}, []
    for K in range(lo + 200 * s, lo + (200 + PER_SAMPLES) * s, s):
        x = greedy(2 * comb_T(K, Q, lo, s), Q)[:120]
        seq.append(seen.setdefault(x, len(seen)))
    per = next((pp for pp in range(1, PER_BOUND + 1)
                if all(seq[i] == seq[i + pp] for i in range(len(seq) - pp))),
               None)
    return per, len(seen)


orb = {}
for t, s_fixed in (((1, 1, 1), 4), ((1, 0, 1, 0, 1), 3),
                   ((1, 0, 0, 1, 0, 0, 1), None), ((1, 0, 1, 0, 0, 1, 0, 1), None)):
    s = s_fixed if s_fixed is not None else step_for(t)[0]
    Q = places(t, (200 + PER_SAMPLES + 2) * s + 2)
    per, nlab = orbit(Q, s)
    orb[w(t)] = (per, nlab)
    print("     %-9s s=%d  labels %3d  least period %s" % (w(t), s, nlab, per))
q5_ctrl = orb["111"] == (3, 3) and orb["10101"][1] == 5 and orb["10101"][0]
q5_ok = all(orb[k] == (None, PER_SAMPLES) for k in ("1001001", "10100101"))
report("Q5 controls read their counts with a period; both exceptions print "
       "300 distinct labels and no period", bool(q5_ctrl) and q5_ok)

# the retrodiction, printed and not scored
six = [r for r in rows if len(r["t"]) <= 6]
print("\n     retrodiction (length <= 6, worth nothing as evidence): "
      "wild = %s" % [r["w"] for r in six if r["kind"] == "wild"])

print("\n%d FAIL" % len(FAILS) if FAILS else "\nall checks pass")
for f in FAILS:
    print("   ", f)
print("wall-clock %.1f s" % (time.time() - t0))
