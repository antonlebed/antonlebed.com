"""The merge criterion of the sign automaton in closed form: which two
reached integers are one state, decided by one window at one level.

THE QUESTION. explore_sign_sparse.py proved that the minimal sign
automaton of a finite digit set D in radix b has
  2 + |R meet I| - #{consecutive reached pairs v < w of I with
                     (-w, -v) meet A = empty}
states, A the attractor of x -> (x + d)/b, I the open crossed interval
(-a^+/(b-1), a^-/(b-1)), R the reached integers, and it decided "meets A"
by an expanding recursion. Its necessary condition for a merge,
Delta - L >= b (Delta the largest digit gap, L = (a^- + a^+)/(b-1) the
hull length), is loose by an order of magnitude: 2,532 cells of its
sweep meet it and 236 merge. This file asks for the EXACT form: a closed
inequality in (b, D, v) that is the recursion's verdict, proved both
ways, and what it says about the 2,296 cells the necessary condition
admits and the recursion refuses.

THE OBJECT. H = [-a^-/(b-1), a^+/(b-1)] is the hull, H_k the union of the
level-k cylinders f_u(H) over digit strings u of length k, and A the
intersection of the H_k. A string u = u_1..u_k read most-significant
first has the integer value c_u = sum u_j b^(k-j), and its cylinder is
f_u(H) = [(c_u - a^-/(b-1))/b^k, (c_u + a^+/(b-1))/b^k]. Write V_k for
the set of values of length-k strings (V_0 = {0}, V_k = b V_(k-1) + D)
and c^- = ceil(a^-/(b-1)), c^+ = ceil(a^+/(b-1)) -- the two ceilings of
the contiguous count.

HAND-ATTACK, on paper before the engine.

  (i) ONE LEVEL DECIDES. Let K be the least k with b^k > L, so every
      level-K cylinder is shorter than 1. Claim: for an open interval
      J = (p, q) of length >= 1, J meets A iff J meets H_K. Forward is
      A inside H_K. Backward: a level-K cylinder meeting J either lies
      inside J, and then its endpoints f_u(-a^-/(b-1)), f_u(a^+/(b-1))
      -- points of A, the images of H's endpoints, which are the fixed
      points of the extreme maps -- lie in J; or it contains p or q as
      an interior point, and then the endpoint of it on J's side is a
      point of A inside J, being less than 1 away; or it has p as its
      right endpoint or q as its left one and does not meet J at all.
      So a cylinder meeting J puts a point of A in J. (The recursion of
      explore_sign_sparse.py unrolls to exactly this, its termination
      being the same length argument.)

  (ii) THE WINDOW. The cylinder of u meets (p, q) iff
      c_u + a^+/(b-1) > b^K p and c_u - a^-/(b-1) < b^K q. With c_u, p, q
      integers, t < a/(b-1) for an integer t reads t <= ceil(a/(b-1)) - 1
      whether or not (b-1) divides a. So the cylinder meets (p, q) iff
        b^K p - c^+ + 1 <= c_u <= b^K q + c^- - 1.
      THE CRITERION: two consecutive reached integers v < w of I are one
      state iff NO length-K string has a value in the window
        W = [b^K (-w) - c^+ + 1, b^K (-v) + c^- - 1],
      i.e. iff V_K meets W in nothing. Both directions are (i) and (ii);
      the reach of v and w is the backward descent explore_sign_sparse.py
      states, unchanged.

  (iii) WHAT THE NECESSARY CONDITION WAS. At K = 1 the window is a hole
      of D of length b + c^+ + c^- - 1 with a prescribed alignment; so a
      merge decided at level 1 needs some consecutive digit pair with
      d_(i+1) - d_i >= b + c^+ + c^-, which is Delta - L >= b with the
      hull length rounded up to the ceilings, plus an ALIGNMENT that the
      inequality does not see, plus REACH. (A merge decided at a higher
      level owes D nothing sharper than Delta - L >= b; the sharpened
      form is a statement about level-1 merges, which is every merge of
      this sweep.) The order of magnitude is three cuts and the sweep
      says which one cuts.

  (iv) THE LEVEL CLAIM IS WRONG. explore_sign_sparse.py's Part II design
      says a gap of A holding a unit interval must be a level-1 gap,
      level-k gaps being b^k times shorter. The image f_w(g) of a level-1
      gap g under a length-(k-1) string has length (Delta - L)/b^k, which
      is at least 1 as soon as Delta - L >= b^k; where no neighbouring
      cylinder covers that image (cylinders of one level overlap when
      two strings' values differ by less than L), it is a gap of A
      holding a unit interval, so the claim can fail once
      Delta - L >= b^2 -- beyond the sweep, whose largest Delta - L is
      12.5 against b^2 = 25 at b = 5 and 7.5 against 9 at b = 3. Paper
      witness: b = 3, D = {-1, 1, 30}, L = 31/2, hull
      [-1/2, 15], level-1 cylinders [-1/2, 14/3], [1/6, 16/3],
      [59/6, 15], the one level-1 gap g = (16/3, 59/6) holding (6, 7),
      (7, 8), (8, 9); its image under the digit 30 is
      (106/9, 239/18) = (11.78, 13.28), holding (12, 13). By the
      criterion, K = 3 (27 > 15.5), c^+ = 15, c^- = 1, and the pair
      (-13, -12) has window [27*12 - 14, 27*13 + 0] = [310, 351];
      V_3 = 9D + 3D + D has 303 (30,1,30) and 359 (30,30,-1) and
      nothing between, so the pair merges, and (12, 13) sits in no
      level-1 gap. Reach: -13 -> (-13+1)/3 = -4 -> (-4+1)/3 = -1, a
      digit; -12 -> (-12-30)/3 = -14 -> -5 -> -2 -> -1. The necessary
      condition Delta - L >= b survives the correction, the level-1
      gaps being the longest.

  (v) THE TWO PAPER CELLS, by the criterion. b = 3, D = {-2, -1, 7}:
      L = 9/2, K = 2, c^+ = 4, c^- = 1, V_2 = {-8, -7, -5, -4, 1, 4, 19,
      20, 28}, R meet I = {-2, -1, 0} (-3 has residue 0 and no digit
      does). Pair (-2, -1): W = [9 - 3, 18 + 0] = [6, 18], empty of V_2,
      one state; pair (-1, 0): W = [-3, 9] holds 1 and 4, two states.
      Count 2 + 3 - 1 = 4. b = 3, D = {-3, -2, -1, 14}: L = 17/2,
      K = 2, c^+ = 7, c^- = 2, V_2 = {-12, -11, -10, -9, -8, -7, -6, -5,
      -4, 5, 8, 11, 39, 40, 41, 56}, R meet I = {-6, .., 0} (1 -> 1
      cycles under -2 and 14 misses). Pairs: (-3, -2) has W = [12, 28]
      and (-4, -3) has W = [21, 37], both empty; (-2, -1) has [3, 19]
      holding 5, (-5, -4) has [30, 46] holding 39, (-6, -5) has
      [39, 55] holding 39, (-1, 0) has [-6, 10] holding -6. Two merges,
      count 2 + 7 - 2 = 7 (the design as frozen wrote 5 here and in W2, an
      arithmetic slip the run caught; the pairs and windows stood).

PREDICTIONS, fixed here and weighed only after the run.
  W1 At every cell of explore_sign_sparse.py's Part II sweep (b = 2..5,
     a^- = 1..3, a^+ = 1..15, three- and four-member sets, 9,840 cells)
     the window criterion's count equals the minimized count, and its
     merging cells number 236: 83 at b = 3, 101 at b = 4, 52 at b = 5,
     none at b = 2.
  W2 The two paper cells print 4 with the pair (-2, -1) and 7 with the
     pairs (-4, -3), (-3, -2), from the criterion and the minimizer
     alike (7 corrected from the frozen 5 post-run, see (v)).
  W3 The witness b = 3, D = {-1, 1, 30} prints a merged pair (-13, -12)
     from the minimizer, and the criterion's least deciding level for
     that pair is 2.
  W4 Every merging pair of the sweep is decided at level 1 -- the
     sweep's Delta - L never reaches b^2 -- and every merged pair is a
     pair of ADJACENT integers (a consecutive reached pair v < w with
     w - v >= 2 never merges in the sweep).

KILLS, as prints.
  X1 Any cell whose criterion count differs from the minimized count
     kills W1 and the criterion with it -- the cell, both counts and
     the disputed pair are printed. A by-base total other than
     83/101/52 kills W1's second clause.
  X2 Either paper cell printing other than the above kills W2.
  X3 The witness printing no merged pair (-13, -12), or the criterion
     deciding it at level 1, kills W3.
  X4 A merging pair of the sweep decided only at level >= 2, or a merged
     non-adjacent pair, kills W4's clause -- the cell is printed.

CONTROLS, run and read before any count is weighed.
  C1/C2/C5 of explore_sign_sparse.py at every cell (exact replay, padded
  minimization, pushed clamp), and at the witness cell.
  C3 CONNECTED CELLS: at every cell with Delta <= L the criterion must
  print zero merges (the connectedness theorem); a nonzero is a bug in
  this build, not a finding.

THE DECOMPOSITION, printed and read after W1. Over the cells meeting
Delta - L >= b: how many meet the ceiling-sharpened digit-gap condition
of (iii); how many have some integer n with the pair (-n-1, -n) inside
I and an EMPTY window at level K (alignment, reach ignored); how many
merge (both reached). Nothing is predicted about these counts; they say
which of the three cuts does the cutting.

SCOPE. The Part II sweep as above, 9,840 cells; K is at most 5 (b = 2,
L <= 18) and V_K at most 4^5 values. The minimizer and its controls are
the cost, 7.5 s for the whole file last time; well under 512 MB.
Estimated under a minute.

Cross-script: explore_sign_sparse.py (the theorem this file gives its
closed form to), explore_sign_minimal.py (the contiguous count).

RUN RECORD. 9,840 cells, C1/C2/C5 clean at every one and at the three
hand cells, C3 zero; 4.5 s, peak 23 MB under memwatch.

FINDINGS.

Z1 THE WINDOW CRITERION IS THE VERDICT AT EVERY CELL (X1 = 0 over
   9,840 cells; 236 merging cells, 83/101/52 at b = 3/4/5, none at
   b = 2). So: two consecutive reached integers v < w of the crossed
   interval are one state of the minimal sign automaton iff no digit
   string of length K -- the least K with b^K > L -- has a value in
   [b^K(-w) - c^+ + 1, b^K(-v) + c^- - 1]; a criterion, proved both ways
   in (i)-(ii) and the sweep its check. Every merging pair of the sweep
   is already decided at level 1 (the first clause of W4 holds), and
   the witness of (iv) prints the pair (-13, -12) merged, decided at
   level 2 and at no lower one: the level-1 claim is dead as (iv) said,
   and the sweep never saw it fail because its Delta - L stays under
   b^2. The witness carries three level-1 merges besides, -9..-6 one
   state, 13 states in all.

Z2 THE MERGED PAIRS ARE NOT ALWAYS NEIGHBOURING INTEGERS (W4's second
   clause killed): of the 240 merged pairs, 9 are consecutive REACHED
   integers two apart with the integer between them unreached -- b = 3,
   D = {-2, -1, 13}: -3 has the residue no digit has, the gap (11/6, 4)
   holds (2, 4) whole, and -4, -2 are one state. The classes are runs
   of consecutive reached integers, as the theorem says, and a run can
   step over a hole of R; the unit-interval reading of the merge
   condition is the adjacent case and not the condition.

Z3 WHERE THE ORDER OF MAGNITUDE GOES. Of the 2,532 cells meeting
   Delta - L >= b, 2,177 meet the ceiling-sharpened digit-gap condition
   d_(i+1) - d_i >= b + c^+ + c^-, 1,103 have an aligned empty window at
   some pair of integers of I (every merging cell among them), and 236
   merge: ALIGNMENT refuses 1,429 and REACH 867, the rounding 355. By
   base (necessary / aligned / merging): 557/270/83 at b = 3,
   965/496/101 at b = 4, 1010/337/52 at b = 5. So the loose condition
   is loose first because a hole in D of the right length need not sit
   where a unit interval of int H reflects into it, and second because
   the integers it would merge need not be reached; neither clause is
   closable past what it already is -- the window is the alignment
   written out, and reach is the backward map's cycle question
   (explore_sign_sparse.py F3).
"""

import os
import sys
from bisect import bisect_left
from fractions import Fraction
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_sign_sparse import analyse, controls, closed_form, fmt, ceil_div  # noqa: E402


def values(b, D, k):
    V = {0}
    for _ in range(k):
        V = {b * x + d for x in V for d in D}
    return sorted(V)


def window_meets(V, lo, hi):
    i = bisect_left(V, lo)
    return i < len(V) and V[i] <= hi


def params(b, D):
    am, ap = -D[0], D[-1]
    cm, cp = ceil_div(am, b - 1), ceil_div(ap, b - 1)
    K = 1
    while b ** K * (b - 1) <= am + ap:
        K += 1
    return am, ap, cm, cp, K


def pair_window(b, v, w, k, cm, cp):
    return b ** k * (-w) - cp + 1, b ** k * (-v) + cm - 1


def criterion(cell):
    """The window criterion: count, merged pairs, and each pair's least
    deciding level (the least k at which V_k misses the level-k window;
    the criterion itself reads level K only)."""
    b, D, R = cell["b"], cell["D"], cell["R"]
    am, ap, cm, cp, K = params(b, D)
    vals = values(b, D, k=K)
    merged = []
    for v, w in zip(R, R[1:]):
        lo, hi = pair_window(b, v, w, K, cm, cp)
        if not window_meets(vals, lo, hi):
            level = 1
            while window_meets(values(b, D, level), *pair_window(b, v, w, level, cm, cp)):
                level += 1
            merged.append((v, w, level))
    return 2 + len(R) - len(merged), merged, K


def aligned(cell):
    """Some integer n with (-n-1, -n) inside I and an empty level-K
    window: the gap clause with reach ignored."""
    b, D, I = cell["b"], cell["D"], cell["I"]
    am, ap, cm, cp, K = params(b, D)
    vals = values(b, D, k=K)
    for v in I:
        w = v + 1
        if w not in I:
            continue
        if not window_meets(vals, *pair_window(b, v, w, K, cm, cp)):
            return True
    return False


def sharpened(cell):
    b, D = cell["b"], cell["D"]
    am, ap, cm, cp, K = params(b, D)
    return any(D[i + 1] - D[i] >= b + cp + cm for i in range(len(D) - 1))


def merged_classes(cell):
    cls = {}
    for v in cell["R"]:
        cls.setdefault(cell["block"][v], []).append(v)
    return sorted(vs for vs in cls.values() if len(vs) > 1)


def hand(b, D):
    cell = analyse(b, D)
    f = controls(cell)
    cnt, merged, K = criterion(cell)
    print("  b=%d D=%s: minimizer count %d merged classes %s; criterion"
          " count %d pairs %s (K=%d); controls %s"
          % (b, fmt(D), cell["count"], merged_classes(cell), cnt, merged, K,
             f or "clean"))


def main():
    print("THE MERGE CRITERION IN WINDOW FORM")
    print()
    print("W2 paper cells:")
    hand(3, (-2, -1, 7))
    hand(3, (-3, -2, -1, 14))
    print("W3 level witness:")
    hand(3, (-1, 1, 30))
    print()
    cells = 0
    fails = 0
    x1 = []
    conn_bad = 0
    merging = []
    by_b = {}
    necessary = []
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
                    cnt, merged, K = criterion(cell)
                    if cnt != cell["count"]:
                        x1.append((b, D, cell["count"], cnt, merged,
                                   closed_form(cell)[1]))
                    if cell["connected"] and merged:
                        conn_bad += 1
                    gapL = cell["gap"] - Fraction(am + ap, b - 1)
                    if gapL >= b:
                        necessary.append(cell)
                    if merged:
                        merging.append((b, D, merged))
                        by_b[b] = by_b.get(b, 0) + 1
    print("cells %d, control failures %d, C3 connected cells with a"
          " criterion merge %d" % (cells, fails, conn_bad))
    print("X1 criterion count != minimized count: %d cells" % len(x1))
    for row in x1[:8]:
        print("   b=%d D=%s count %d criterion %d pairs %s recursion %s"
              % (row[0], fmt(row[1]), row[2], row[3], row[4], row[5]))
    print("merging cells %d, by base %s" % (len(merging), sorted(by_b.items())))
    pairs = [(b, D, p) for b, D, m in merging for p in m]
    deep = [x for x in pairs if x[2][2] >= 2]
    nonadj = [x for x in pairs if x[2][1] - x[2][0] >= 2]
    print("X4 merged pairs %d; decided only at level >= 2: %d;"
          " non-adjacent: %d" % (len(pairs), len(deep), len(nonadj)))
    for x in (deep + nonadj)[:8]:
        print("   b=%d D=%s pair %s" % (x[0], fmt(x[1]), x[2]))
    print()
    print("THE DECOMPOSITION over cells with Delta - L >= b:")
    n_nec = len(necessary)
    n_sharp = sum(1 for c in necessary if sharpened(c))
    n_al = sum(1 for c in necessary if aligned(c))
    n_sharp_al = sum(1 for c in necessary if sharpened(c) and aligned(c))
    n_merge = sum(1 for c in necessary if c["merges"] > 0)
    n_al_merge = sum(1 for c in necessary if aligned(c) and c["merges"] > 0)
    print("  Delta - L >= b: %d; digit gap >= b + c^+ + c^-: %d;"
          " an aligned empty window: %d (both: %d); merging: %d"
          " (aligned and merging: %d)"
          % (n_nec, n_sharp, n_al, n_sharp_al, n_merge, n_al_merge))
    print("  so the necessary condition loses %d to alignment and %d to"
          " reach" % (n_nec - n_al, n_al - n_merge))
    by_b_nec = {}
    for c in necessary:
        key = c["b"]
        t = by_b_nec.setdefault(key, [0, 0, 0])
        t[0] += 1
        t[1] += aligned(c)
        t[2] += c["merges"] > 0
    print("  by base (necessary, aligned, merging): %s" % sorted(by_b_nec.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
