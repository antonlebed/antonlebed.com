"""The sign automaton off contiguous digit sets: what its minimal state
count is when the digit set has holes.

THE QUESTION. A signed-digit system reads digits from a finite set D of
integers in radix b, most-significant-first, and the SIGN of the value is
finite-state: v <- b*v + d, absorbing once no tail can overturn the
verdict. Over contiguous sets {-a^-..a^+} the minimal count is known --
2*ceil(a/(b-1)) + 1 on symmetric sets (a theorem) and
ceil(a^-/(b-1)) + ceil(a^+/(b-1)) + 1 on asymmetric ones (a rule there,
its reachability step proved in G3 below; the reaches crossing: a positive
prefix is killed by the NEGATIVE reach), both in explore_sign_minimal.py. That file records that the object underneath
is not the digit set but the integers no tail returns to zero under the
affine family x -> b*x + d, and that this is the level to descend to for a
closed form off contiguous sets. This file descends to it: D is now ANY
finite set of integers with at least one negative and one positive member.

The question is a real one outside this corpus. Sign detection in a
redundant (carry-free) representation is a standard hardware task, and
which integers a digit set represents at all is the classical question of
BASIC digit sets (Matula 1982; Odlyzko 1978 on nonnegative sets), where
the answer is a statement about cycles of the backward map n -> (n-d)/b
and not about residues alone. Nothing below cites those results as
hypotheses; they are named so a reader knows the neighbourhood.

THE OBJECT. Write a^- = -min D >= 1 and a^+ = max D >= 1 (the REACHES),
L = (a^- + a^+)/(b-1) (the hull length), and Delta for the largest gap
between consecutive members of D. A prefix of value v followed by a tail
t_1..t_m has value b^m * (v + tau) with tau = sum t_i b^-i, so its sign is
the sign of v + tau, and tau ranges over the level-m points A_m of the
iterated function system f_d(x) = (x + d)/b, whose attractor A sits in the
hull H = [-a^-/(b-1), a^+/(b-1)] of length L. Two prefixes are
Myhill-Nerode equivalent iff sign(v + tau) = sign(w + tau) for every tau in
every A_m. The minimal automaton's states are the classes of the values
REACHABLE from the empty prefix, which are the integers with a finite
D-expansion read as integers (the forward-reachable set R), not the
attractor's points.

HAND-ATTACK, on paper before the engine, in four steps.

  (i) THE THRESHOLDS ARE THE EXTREMES' ALONE. The all-(-a^-) tail gives
      tau -> -a^-/(b-1) from above, and no tail goes lower, so a prefix
      v > 0 keeps its sign under every tail iff v >= a^-/(b-1); likewise
      v < 0 is absorbing iff v <= -a^+/(b-1). This is Part II's crossed
      form and it never looks at the interior of D. So the undecided
      states are the reachable integers in the OPEN crossed interval
      I = (-a^+/(b-1), a^-/(b-1)), and every one of them is non-absorbing
      (the extreme tail flips it), so the count is
        2 + (number of Nerode classes on R meet I),
      with the two absorbing classes existing whenever something reaches
      them, which every cell here does (an extreme digit repeated).

  (ii) CONNECTEDNESS SEPARATES. The level-1 cylinders f_d(H) have length
      L/b and consecutive ones overlap iff Delta <= L; then by induction
      the level-m cylinders cover H, each of length L/b^m and each
      containing its own point of A_m (0 lies in H, since a^- and a^+ are
      positive). Take reachable integers v < w in I: the open interval
      (-w, -v) has length at least 1 and sits inside the interior of H, so
      for m with 2L/b^m < 1 some level-m cylinder lies wholly inside it,
      and its point tau has v + tau < 0 < w + tau. Same argument separates
      any v != 0 in I from the all-zeros class. So under Delta <= L there
      are NO merges and the count is EXACTLY 2 + |R meet I|. For a
      contiguous set Delta = 1 and the condition reads a^- + a^+ + 1 >= b:
      the covering condition explore_sign_minimal.py assumed is this one
      in its own vocabulary, which is why that file never met a merge.

  (iii) AT b = 2 EVERY SET IS CONNECTED, since L = a^- + a^+ >= Delta.
      A merge needs b >= 3 and a gap in A of length at least 1 sitting
      inside H's interior with reachable integers on both sides; the
      level-1 gaps have length (Delta - L)/b, so it needs Delta - L >= b
      at least.

  (iv) REACHABILITY IS THE REMAINING FACTOR and it is a cycle question.
      Any digit keeps the backward image (n - d)/b of an n in I inside I,
      so an integer of I is reachable iff the backward map, choosing a
      digit congruent to n mod b at each step, can reach 0 from it. If D
      misses a residue class mod b the integers of I in that class are
      unreachable outright (a prefix's residue is its last digit's). If D
      holds a complete residue system the obstruction can only be a cycle
      of the backward map inside I that 0 does not lie on, and whether
      such cycles occur at small parameters is what the sweep reads.

PREDICTIONS, fixed here and weighed only after the run.
  P1 At every cell the surviving (non-absorbing, reachable) states are
     exactly the reachable integers in the open crossed interval I.
  P2 At every cell with Delta <= L the number of classes on R meet I
     equals |R meet I|: no merges. (Proved in (ii); the sweep is the check
     on the proof.)
  P3 At every cell with Delta <= L whose D contains a complete residue
     system mod b, every integer of I is reachable, so the count equals
     the contiguous formula ceil(a^-/(b-1)) + ceil(a^+/(b-1)) + 1.
  P4 Some cell with Delta > L carries a merge (two distinct reachable
     integers of I in one class), and none does at b = 2.

KILLS, named as things this file PRINTS.
  K1 A cell whose printed survivor set is not R meet I kills P1.
  K2 A cell with Delta <= L printing merges > 0 kills P2 -- and the proof
     with it, which is the reading that would matter most.
  K3 A cell with Delta <= L and complete residues printing an unreachable
     integer of I kills P3; its D and the unreachable integer are printed.
  K4 The sweep printing zero merges over every disconnected cell kills
     P4's first half; a merge printed at b = 2 kills its second.

CONTROLS, run and read BEFORE any count is weighed.
  C1 EXACTNESS: the minimized automaton is replayed against brute-force
     sign on every digit string up to the widest width the budget allows.
  C2 PADDING: the automaton with every state duplicated minimizes back to
     the same count.
  C4 CONTIGUOUS CELLS: every cell whose D is an interval must print the
     Part II formula; a disagreement there is a bug in this build.
  C5 THE CLAMP IS NOT THE COUNT: the machine rebuilt with the absorbing
     clamp pushed out by 3 on each side must minimize to the same count.
  C6 A HAND CELL: b = 2, D = {-5, 0, 3}. On paper: I = (-3, 5), its
     seven integers -2..4 all reached (0; 3; 3*2-5 = 1; 2; 4; 2*2-5 = -1;
     -2 = 2*(-1)+0), Delta = 5 <= L = 8, complete residues, so the count
     must print 9 = ceil(5) + ceil(3) + 1.

SCOPE. b = 2..6, reaches a^-, a^+ = 1..5, and D = {-a^-, a^+} together
with EVERY subset of the interior {-a^- + 1, .., a^+ - 1} (the digit 0
included or not, since the empty prefix has value 0 either way): 1,922
digit sets per base, 9,610 cells. Sets that are a common multiple of a
smaller one are swept as they are -- they carry the same automaton and
simply agree. State spaces are the integers of I plus two, at most a few
dozen; the brute replay is the cost, bounded by the string budget per
cell. Well under the 512 MB ceiling; estimated a minute or two.

RUN RECORD, PART I: 9,610 cells, C1/C2/C4/C5 clean at every one, C6
prints 9; 3.0 s, peak 59 MB under memwatch.

FINDINGS, PART I.

F1 THE SURVIVORS ARE R MEET I AT EVERY CELL (K1 = 0): the thresholds are
   the extremes' alone, whatever the interior of D (property, step (i)).

F2 THE CONNECTEDNESS THEOREM HOLDS AS PROVED (K2 = 0 over 4,728 connected
   cells): no merge under Delta <= L, so there the count is exactly
   2 + |R meet I|.

F3 P3 IS KILLED: COMPLETE RESIDUES DO NOT BUY FULL REACHABILITY, at 643
   of the 4,098 connected complete-residue cells. Witness b = 2,
   D = {-1, 2, 3}: I = {-2, -1, 0} and -2 is never reached, because it is
   a fixed point of the backward map (-2 = 2*(-2) + 2) and the digit 2 is
   the only one of its residue -- the cycle obstruction step (iv) allowed
   for, at length one. The count there is 4 against the contiguous
   formula's 5; the formula holds at 3,455 of the 4,098. So the
   contiguous count is the count of a set with NO backward cycle off 0
   in I, which contiguity guarantees (the descent in G3 below) and
   completeness does not. At the 4,421
   cells missing a residue class the unreachable integers are exactly the
   missing residues at 3,837 and carry a cycle on top at the rest.

F4 P4 IS KILLED INSIDE THIS SCOPE AND THE SCOPE IS WHY: zero merges at
   the 4,882 disconnected cells, so the count is 2 + |R meet I| at every
   one of the 9,610 cells. Step (iii)'s necessary condition Delta - L >= b
   IS met inside the grid (b = 3, D = {-5, 5}: Delta - L = 5), but a merge
   needs more: a unit interval inside the gap with a reachable integer at
   each end, and at {-5, 5} the residue 0 is missing and the rest cycle
   (1 -> 2 -> -1 -> -2 -> 1 under the backward map), so R meet I = {0}. The
   sweep is too small in a^+ to hold both. On paper, b = 3 with
   D = {-1, 0, 13} has L = 6.5, hull [-1/2, 13/2], level-1 cylinders
   [-1/2, 11/6], [-1/6, 13/6], [25/6, 13/2], so the gap (13/6, 25/6)
   holds (3, 4) whole; -3 and -4 are both reached (0 -> -1 -> -4 and
   -1 -> -3), so they are one state. The merge regime is real and sits
   past reach 5. Part II populates it and states the closed form for it.

================================================================
PART II -- THE MERGE CRITERION AND THE CLOSED FORM. Slate frozen before
the engine below was written.

THE CLOSED FORM, derived. For reachable integers v < w in I, v ~ w iff
sign(v + tau) = sign(w + tau) for every finite point tau of A, iff no
finite point lies in the open interval (-w, -v) and neither -v nor -w is
one. The finite points are dense in A and the interval is open, so the
first clause reads (-w, -v) meet A = empty; the second is automatic when
the first holds: were -v a finite point f_t(0), then f_t followed by k
copies of the digit -a^- is a finite point below -v by less than
a^-/b^(|t|+k), inside (-w, -v) for large k, and -w mirrors with a^+.
Equivalence
is convex (a subinterval of a gap is a gap), so the classes on R meet I
are RUNS of consecutive reachable integers, and

  count = 2 + |R meet I| - #{ consecutive reachable pairs v_i < v_{i+1}
                              in I with (-v_{i+1}, -v_i) meet A = empty }.

"Meets A" is exactly decidable by the expanding recursion: an open
interval J meets A iff J contains an endpoint of H (both lie in A, as the
fixed points of the extreme maps), or J = int H, or for some digit d the
interval b*J - d meets A; J disjoint from H does not. Lengths grow by b
per level, so the recursion terminates. A gap of A holding a unit
interval must be a level-1 gap (level-k gaps are b^k times shorter), so a
merge needs Delta - L >= b, and none exists at b = 2.

PREDICTIONS, fixed here.
  Q1 At every cell of the extended sweep the minimized count equals the
     closed form above, the pairs decided by the recursion.
  Q2 The hand cell b = 3, D = {-1, 0, 13} prints count 5 with the merged
     class {-4, -3}.
  Q3 Merges occur in the extended sweep, only at cells with
     Delta - L >= b, and at none with b = 2.

KILLS, as prints.
  M1 Any cell whose minimized count differs from the closed form kills
     Q1 -- the cell, both counts and the disputed pair are printed.
  M2 The hand cell printing anything but 5 with {-4, -3} kills Q2.
  M3 A merge at a cell with Delta - L < b kills Q3; zero merges over the
     extended sweep kills its first clause.

CONTROLS. C1, C2, C5 as in Part I over every cell of the extended sweep.

SCOPE, PART II. b = 2..5, a^- = 1..3, a^+ = 1..15, and D of three or
four members: the two extremes plus one or two interior digits. The
merge regime Delta - L >= b is inside the grid from a^+ = 13 at b = 3.

RUN RECORD, PART II: 9,840 cells, C1/C2/C5 clean at every one; the hand
cell prints count 5 with {-4, -3} merged, from the minimizer and from the
closed form alike. Both parts together 7.5 s, peak 62 MB under memwatch.

FINDINGS, PART II.

G1 THE CLOSED FORM IS THE COUNT AT EVERY CELL (M1 = 0 over 9,840 cells,
   the 236 merging ones included). So the minimal sign automaton of an
   arbitrary finite digit set has exactly
     2 + |R meet I| - (number of consecutive reachable pairs of I whose
                        interval, reflected, misses the attractor)
   states -- a theorem, the derivation in the Part II design above and
   the sweep its check: the thresholds from step (i), the Nerode classes
   as runs from the density of the finite points, and the recursion
   deciding each run. Its three factors are three different objects: the
   extremes of D fix the interval, the backward map's cycles fix which of
   its integers are reached, and the attractor's gaps fix which reached
   neighbours are one state.

G2 THE MERGE REGIME IS INHABITED AND SITS WHERE THE DERIVATION PUT IT
   (Q3 clean): 236 merging cells, 83 at b = 3, 101 at b = 4, 52 at b = 5,
   none at b = 2, every one with Delta - L >= b; 2,532 cells meet that
   necessary condition and 236 of them merge, so the condition is loose
   by an order of magnitude and the recursion is what decides. The
   merging cell of least positive reach in the sweep (a^- at most 3
   there; a larger negative reach mirrors under negation) is b = 3,
   D = {-2, -1, 7}: cylinders
   [-1, 1/2], [-2/3, 5/6], [2, 7/2], the gap (5/6, 2) holding (1, 2), and
   -2, -1 each one digit from the start -- three reachable integers of I
   in two classes, four states where the contiguous count would say
   ceil(2/2) + ceil(7/2) + 1 = 6. The most merges in one cell is two, at
   b = 3, D = {-3, -2, -1, 14}: seven reachable integers, five classes.

G3 WHAT THE CONTIGUOUS FORMULA WAS. Part I's F3 and this file's G1 read
   together: ceil(a^-/(b-1)) + ceil(a^+/(b-1)) + 1 is the count of a set
   whose interval integers are ALL reached and NONE merged, and contiguity
   secures both. Connectedness is step (ii). Reachability is a DESCENT,
   which settles the one step explore_sign_minimal.py's Part II left as a
   rule: take an integer n > 0 of I (the negative side mirrors). If
   n <= a^+ it is a digit and one digit reaches it. Otherwise let d be the
   largest digit congruent to n mod b; the covering condition
   a^- + a^+ + 1 >= b puts the b consecutive integers ending at a^+ inside
   D, so d lies in (a^+ - b, a^+]. Then n' = (n - d)/b is an integer, it
   is positive because d <= a^+ < n, and it is below n because
   d >= a^+ - b + 1 > -(b-1)n. So n = b*n' + d with n' a smaller positive
   integer of I, and induction lands on a digit. Hence the asymmetric
   contiguous count is a THEOREM over signed contiguous covering sets,
   the Part II rule of that file now proved at its open step. A set with
   holes can lose states to either factor, never gain one: the contiguous
   count is the maximum over every digit set with those reaches, and the
   two ways down are a cycle of the backward map and a gap of the
   attractor of unit length.
"""

import sys
from fractions import Fraction
from itertools import combinations, product

BASES = range(2, 7)
REACHES = range(1, 6)
BRUTE_BUDGET = 1500  # digit strings replayed per cell in control C1
POS, NEG = "POS", "NEG"


def sgn(x):
    return (x > 0) - (x < 0)


def digit_sets(am, ap):
    interior = list(range(-am + 1, ap))
    for r in range(len(interior) + 1):
        for sub in combinations(interior, r):
            yield tuple(sorted((-am,) + sub + (ap,)))


def thresholds(b, D):
    am, ap = -D[0], D[-1]
    return am, ap


def clamp_state(v, b, am, ap, push=0):
    # absorbing iff v >= am/(b-1) or v <= -ap/(b-1); 'push' widens the
    # integer band kept before absorbing, for control C5.
    if v * (b - 1) >= am + push * (b - 1):
        return POS
    if v * (b - 1) <= -ap - push * (b - 1):
        return NEG
    return v


def build(b, D, push=0):
    am, ap = thresholds(b, D)
    start = 0
    states = {start}
    delta = {}
    frontier = [start]
    while frontier:
        s = frontier.pop()
        for d in D:
            if s in (POS, NEG):
                t = s
            else:
                t = clamp_state(b * s + d, b, am, ap, push)
            delta[(s, d)] = t
            if t not in states:
                states.add(t)
                frontier.append(t)
    out = {s: (1 if s == POS else -1 if s == NEG else sgn(s)) for s in states}
    return states, delta, out, start


def minimize(states, delta, out, start, D):
    # Moore partition refinement on the output function.
    block = {s: out[s] for s in states}
    while True:
        sig = {s: (block[s],) + tuple(block[delta[(s, d)]] for d in D)
               for s in states}
        ids = {}
        newblock = {}
        for s in states:
            newblock[s] = ids.setdefault(sig[s], len(ids))
        if len(set(newblock.values())) == len(set(block.values())):
            return newblock
        block = newblock


def pad(states, delta, out, start, D):
    st = set()
    dl = {}
    ot = {}
    for s in states:
        for c in (0, 1):
            st.add((s, c))
            ot[(s, c)] = out[s]
            for d in D:
                dl[((s, c), d)] = (delta[(s, d)], 1 - c)
    return st, dl, ot, (start, 0)


def replay(b, D, delta, out, start):
    n = len(D)
    width = 1
    while n ** (width + 1) <= BRUTE_BUDGET:
        width += 1
    bad = 0
    for w in range(1, width + 1):
        for digits in product(D, repeat=w):
            v = 0
            s = start
            for d in digits:
                v = b * v + d
                s = delta[(s, d)]
            if out[s] != sgn(v):
                bad += 1
    return bad


def ceil_div(x, y):
    return -(-x // y)


def analyse(b, D):
    am, ap = thresholds(b, D)
    states, delta, out, start = build(b, D)
    block = minimize(states, delta, out, start, D)
    count = len(set(block.values()))
    interior = [s for s in states if s not in (POS, NEG)]
    # the open crossed interval's integers
    I = [v for v in range(-ap, am + 1)
         if v * (b - 1) > -ap and v * (b - 1) < am]
    R_in_I = sorted(v for v in interior if v in I)
    survivors = sorted(interior)
    classes_on_R = len(set(block[v] for v in R_in_I))
    merges = len(R_in_I) - classes_on_R
    delta_gap = max(D[i + 1] - D[i] for i in range(len(D) - 1))
    connected = delta_gap * (b - 1) <= am + ap
    complete = len(set(d % b for d in D)) == b
    formula = ceil_div(am, b - 1) + ceil_div(ap, b - 1) + 1
    contiguous = all(D[i + 1] - D[i] == 1 for i in range(len(D) - 1))
    unreachable = [v for v in I if v not in R_in_I]
    return dict(b=b, D=D, am=am, ap=ap, count=count, formula=formula,
                I=I, R=R_in_I, survivors=survivors, merges=merges,
                connected=connected, complete=complete,
                contiguous=contiguous, unreachable=unreachable,
                states=states, delta=delta, out=out, start=start,
                block=block, gap=delta_gap)


def controls(cell):
    b, D = cell["b"], cell["D"]
    fails = []
    bad = replay(b, D, cell["delta"], cell["out"], cell["start"])
    if bad:
        fails.append(("C1", bad))
    st, dl, ot, s0 = pad(cell["states"], cell["delta"], cell["out"],
                         cell["start"], D)
    if len(set(minimize(st, dl, ot, s0, D).values())) != cell["count"]:
        fails.append(("C2", None))
    if cell["contiguous"] and cell["count"] != cell["formula"]:
        fails.append(("C4", cell["count"]))
    st, dl, ot, s0 = build(b, D, push=3)
    if len(set(minimize(st, dl, ot, s0, D).values())) != cell["count"]:
        fails.append(("C5", None))
    return fails


def fmt(D):
    return "{" + ",".join(str(d) for d in D) + "}"


def main():
    print("SIGN OFF CONTIGUOUS SETS: b = 2..6, reaches 1..5, every interior")
    print()
    # C6 first, by hand.
    hand = analyse(2, (-5, 0, 3))
    print("C6 hand cell b=2 D={-5,0,3}: count %d (paper 9), R meet I = %s"
          % (hand["count"], hand["R"]))
    print()
    cells = []
    control_fails = 0
    for b in BASES:
        for am in REACHES:
            for ap in REACHES:
                for D in digit_sets(am, ap):
                    cell = analyse(b, D)
                    f = controls(cell)
                    if f:
                        control_fails += 1
                        if control_fails <= 10:
                            print("CONTROL FAIL b=%d D=%s %s" % (b, fmt(D), f))
                    cells.append(cell)
    print("cells %d, control failures %d" % (len(cells), control_fails))
    print()

    k1 = [c for c in cells if c["survivors"] != c["R"]]
    print("K1 survivor set != R meet I: %d cells" % len(k1))
    for c in k1[:5]:
        print("   b=%d D=%s survivors %s R %s" % (c["b"], fmt(c["D"]),
                                                  c["survivors"], c["R"]))

    conn = [c for c in cells if c["connected"]]
    disc = [c for c in cells if not c["connected"]]
    k2 = [c for c in conn if c["merges"] > 0]
    print("connected cells %d, disconnected %d" % (len(conn), len(disc)))
    print("K2 merges at connected cells: %d" % len(k2))
    for c in k2[:5]:
        print("   b=%d D=%s merges %d" % (c["b"], fmt(c["D"]), c["merges"]))

    cc = [c for c in conn if c["complete"]]
    k3 = [c for c in cc if c["unreachable"]]
    print("connected+complete cells %d, with an unreachable integer of I: %d"
          % (len(cc), len(k3)))
    for c in k3[:12]:
        print("   b=%d D=%s I %d..%d unreachable %s count %d formula %d"
              % (c["b"], fmt(c["D"]), c["I"][0], c["I"][-1],
                 c["unreachable"], c["count"], c["formula"]))
    eq = sum(1 for c in cc if c["count"] == c["formula"])
    print("   count == contiguous formula at %d of %d" % (eq, len(cc)))

    k4 = [c for c in disc if c["merges"] > 0]
    print("K4 merges at disconnected cells: %d of %d; at b = 2: %d"
          % (len(k4), len(disc),
             sum(1 for c in cells if c["b"] == 2 and c["merges"] > 0)))
    for c in k4[:12]:
        cls = {}
        for v in c["R"]:
            cls.setdefault(c["block"][v], []).append(v)
        merged = [vs for vs in cls.values() if len(vs) > 1]
        print("   b=%d D=%s gap %d L=%d/%d merged %s count %d (2+|R|=%d)"
              % (c["b"], fmt(c["D"]), c["gap"], c["am"] + c["ap"], c["b"] - 1,
                 merged, c["count"], 2 + len(c["R"])))
    if k4:
        print("   least b with a merge: %d; least gap - L: %s"
              % (min(c["b"] for c in k4),
                 min((c["gap"] - (c["am"] + c["ap"]) / (c["b"] - 1)) for c in k4)))

    # the count against 2 + |R meet I| everywhere
    off = [c for c in cells if c["count"] != 2 + len(c["R"])]
    print("count != 2 + |R meet I|: %d cells (all merges: %s)"
          % (len(off), all(c["merges"] > 0 for c in off)))

    # incomplete-residue cells: the missing residues are unreachable
    inc = [c for c in cells if not c["complete"]]
    missing_only = sum(1 for c in inc if all(
        (v % c["b"]) not in set(d % c["b"] for d in c["D"])
        for v in c["unreachable"]))
    print("incomplete-residue cells %d; unreachable set = missing residues"
          " only at %d" % (len(inc), missing_only))
    print()
    part_two()
    return 0


# ---------------------------------------------------------------- PART II

def meets_A(lo, hi, b, D, memo):
    """Does the open interval (lo, hi) meet the attractor of
    x -> (x + d)/b, d in D?  Exact rationals; the expanding recursion of
    the Part II design."""
    key = (lo, hi)
    if key in memo:
        return memo[key]
    am, ap = -D[0], D[-1]
    Hlo, Hhi = Fraction(-am, b - 1), Fraction(ap, b - 1)
    if hi <= Hlo or lo >= Hhi:
        ans = False
    elif lo < Hlo < hi or lo < Hhi < hi or (lo <= Hlo and hi >= Hhi):
        ans = True
    else:
        memo[key] = False  # guards a self-loop, which the growth excludes
        ans = any(meets_A(b * lo - d, b * hi - d, b, D, memo) for d in D)
    memo[key] = ans
    return ans


def closed_form(cell):
    b, D, R = cell["b"], cell["D"], cell["R"]
    memo = {}
    merged_pairs = []
    for v, w in zip(R, R[1:]):
        if not meets_A(Fraction(-w), Fraction(-v), b, D, memo):
            merged_pairs.append((v, w))
    return 2 + len(R) - len(merged_pairs), merged_pairs


def part_two():
    print("PART II: the merge criterion, b = 2..5, a^- = 1..3, a^+ = 1..15,")
    print("         three- and four-member sets")
    print()
    hand = analyse(3, (-1, 0, 13))
    cf, pairs = closed_form(hand)
    cls = {}
    for v in hand["R"]:
        cls.setdefault(hand["block"][v], []).append(v)
    merged = sorted(vs for vs in cls.values() if len(vs) > 1)
    print("Q2 hand cell b=3 D={-1,0,13}: count %d (paper 5), merged %s,"
          " closed form %d pairs %s" % (hand["count"], merged, cf, pairs))
    print()
    cells = 0
    fails = 0
    m1 = []
    merges = []
    necessary = 0
    for b in range(2, 6):
        for am in range(1, 4):
            for ap in range(1, 16):
                interior = list(range(-am + 1, ap))
                subs = []
                for r in (1, 2):
                    subs.extend(combinations(interior, r))
                for sub in subs:
                    D = tuple(sorted((-am,) + sub + (ap,)))
                    cell = analyse(b, D)
                    cells += 1
                    if controls(cell):
                        fails += 1
                    cf, pairs = closed_form(cell)
                    if cf != cell["count"]:
                        m1.append((b, D, cell["count"], cf, pairs))
                    gapL = cell["gap"] - Fraction(am + ap, b - 1)
                    if gapL >= b:
                        necessary += 1
                    if cell["merges"] > 0:
                        merges.append((b, D, cell["merges"], gapL, pairs,
                                       cell["count"], len(cell["R"])))
    print("cells %d, control failures %d" % (cells, fails))
    print("M1 count != closed form: %d cells" % len(m1))
    for row in m1[:8]:
        print("   b=%d D=%s count %d closed %d pairs %s"
              % (row[0], fmt(row[1]), row[2], row[3], row[4]))
    print("cells with merges: %d; cells meeting Delta - L >= b: %d;"
          " merges at b = 2: %d; merges with Delta - L < b: %d"
          % (len(merges), necessary,
             sum(1 for m in merges if m[0] == 2),
             sum(1 for m in merges if m[3] < m[0])))
    by_b = {}
    for m in merges:
        by_b[m[0]] = by_b.get(m[0], 0) + 1
    print("   merging cells by base: %s" % sorted(by_b.items()))
    if merges:
        least = min(merges, key=lambda m: (m[1][-1], m[0]))
        print("   least a^+ with a merge: b=%d D=%s" % (least[0], fmt(least[1])))
        deepest = max(merges, key=lambda m: m[2])
        print("   most merges in one cell: %d at b=%d D=%s (count %d, |R meet I| %d)"
              % (deepest[2], deepest[0], fmt(deepest[1]), deepest[5], deepest[6]))
    for m in merges[:10]:
        print("   b=%d D=%s merged pairs %s  Delta-L=%s" % (m[0], fmt(m[1]), m[4], m[3]))


if __name__ == "__main__":
    sys.exit(main())
