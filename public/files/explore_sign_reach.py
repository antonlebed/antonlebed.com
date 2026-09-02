"""Reach in the merge regime: whether the window criterion's reach clause
closes to a statement about the digit set, and what decides it.

THE QUESTION. explore_sign_window.py proved that consecutive reached
integers v < w of the crossed interval I = (-a^+/(b-1), a^-/(b-1)) are
one state of the minimal sign automaton iff no digit string of length K
(the least with b^K > L, L the hull length) has a value in the window
[b^K(-w) - c^+ + 1, b^K(-v) + c^- - 1]. The gap clause is that window,
a statement about D. The reach clause is the backward map's cycle
question, n -> (n - d)/b over the digits d of n's residue with every
step inside I, and explore_sign_sparse.py F3 showed a complete residue
system does not settle it. Of the 2,532 sweep cells meeting the loose
condition Delta - L >= b, 1,103 carry an adjacent pair of I with an
empty level-K window (ALIGNED), and 236 of those merge: reach refuses
867. This file asks what decides reach at the aligned pair, and whether
anything short of the backward graph decides it.

WHOSE VOCABULARY. The backlog's candidate was written in the contiguous
sweep's terms -- "every residue mod b held by a digit of the hull's near
end" -- and it cannot be necessary: 52 merging cells sit at b = 5 with at
most four digits, so no set of near digits covers five residues there.
Reach is a CHAIN and a chain needs only the residues it passes through,
so the candidates below are chain-wise. The hand-attack is on the
window sweep's own cells.

THE OBJECT. For n in I, n != 0, a backward step is n -> n' = (n - d)/b
with d in D, d = n (mod b), n' in I; n is REACHED iff some chain of
steps ends at 0 (the empty prefix), which is the descent
explore_sign_sparse.py states. A step is MONOTONE when |n'| < |n| with
n' on n's side or 0: for n < 0 that is n <= d <= (b-1)|n| - 1, for
n > 0 it is -(b-1)n < d <= n. Three digit-side readings of a pair:
  RES   both integers' residues are held by some digit (necessary:
        an integer whose residue no digit holds has no step at all);
  MONO  both integers have a chain of monotone steps to 0 (sufficient:
        it is a reach witness, and it reads D one residue window at a
        time without the graph);
  LEN   the shortest witnessing chain of each reached integer, against
        K -- whether the criterion reads strings of length at most K.

HAND-ATTACK, on paper before the engine.

  (i) THE MONOTONE STEP AT -1 needs the digit -1 itself: the window is
      [-1, b-2] and the only digit of residue -1 in it is -1. So every
      MONO chain from the negative side ends through -1, and a set
      without -1 reaches -1 only through a non-monotone chain (from -2
      through 2b-1, or from 1 through -b-1).

  (ii) A NON-MONOTONE MERGE INSIDE THE SWEEP. b = 3, D = {-1, 1, 15}:
      L = 8, K = 2 (9 > 8), c^+ = 8, c^- = 1, I = (-7.5, 0.5), digit gap
      14 >= b + c^+ + c^- = 12. Level-1 cylinders: digit 1 gives
      [1/6, 17/6], digit 15 gives [29/6, 8]; the gap (17/6, 29/6) holds
      (3, 4), so the pair (-4, -3) is aligned. Reach: -4 = -1 (mod 3),
      (-4 + 1)/3 = -1, (-1 + 1)/3 = 0 -- monotone, length 2. -3 = 0
      (mod 3) and the only digit of residue 0 is 15: (-3 - 15)/3 = -6,
      the only step; -6 -> (-6 - 15)/3 = -7, the only step; -7 = 2
      (mod 3) -> (-7 + 1)/3 = -2; -2 = 1 (mod 3) -> (-2 - 1)/3 = -1;
      -1 -> 0. Every step forced, all inside I, so -3 is reached by
      exactly one chain, of length 5, through -6 and -7 which lie
      DEEPER than -3. So MONO fails at -3 while the pair merges, and
      the chain is longer than K = 2: the criterion does not read
      strings of length at most K.

  (iii) A SECOND HAND CELL, all reached. b = 4, D = {-3, -2, -1, 12}:
      residues 1, 2, 3, 0, complete; L = 5, K = 2 (16 > 5), c^+ = 4,
      c^- = 1, I = (-4, 1), integers -3..0; digit gap 13 >= b + c^+ +
      c^- = 9. Level-1 cylinders: -1 gives [-1/2, 3/4], 12 gives
      [11/4, 4]; the gap (3/4, 11/4) holds (1, 2), so (-2, -1) is
      aligned. Reach, one monotone step each: -1 -> 0 by -1, -2 -> 0
      by -2, -3 -> 0 by -3. So the cell merges with MONO true, chain
      length 1 at both integers: the shape the contiguous descent
      predicts, and the control that the readings agree there. A cycle
      loss with the residues present is not hand-built here; Y1 says
      only that the sweep holds some, and the rig names them.

PREDICTIONS, fixed here and weighed only after the run.
  Y1 RES holds at both integers of every merging pair (a control: it
     is necessary), and fails at some but not all reach-lost aligned
     cells -- the residue-missing share of the 867 is a MINORITY, the
     rest lost with the residues present.
  Y2 MONO is sufficient at every aligned pair (a control) and NOT
     necessary: b = 3, D = {-1, 1, 15} prints the pair (-4, -3) merged
     with MONO false at -3 and -3's shortest chain of length 5 > K = 2.
     So neither the monotone descent nor "strings of length at most K"
     is the reach clause.
  Y3 Over the merging pairs, the shortest chain exceeds K at some
     pairs and the chain passes through an integer deeper than the pair
     (farther from 0) at some -- so reach in the merge regime reads the
     graph beyond the pair's own neighbourhood.

KILLS, as prints.
  X1 A merging pair with RES false kills the reach reading of this
     file (a bug or a wrong step law); a reach-lost share with RES
     false at every one makes RES exact and the criterion digit-only --
     the YES the backlog asked for, and it kills Y1's second clause.
  X2 The cell of (ii) printing MONO true at -3, or not merging, or a
     shortest chain other than 5, kills Y2.
  X3 Every merging pair's chain at most K long kills Y3.

CONTROLS. C1 MONO true => reached, at every integer of I of every
aligned cell (the chain is a witness). C2 RES false => unreached,
likewise. C3 the reached set R of explore_sign_sparse.py's analyse
equals the set reachable from 0 in this file's backward graph, at every
aligned cell (the two reach readings agree). A failure of any is a bug
in this build, not a finding.

SCOPE. explore_sign_window.py's sweep (b = 2..5, a^- = 1..3,
a^+ = 1..15, three- and four-member sets, 9,840 cells), restricted to
the aligned cells; the aligned pair is every adjacent pair (v, v+1) of
I with an empty level-K window, and at a merging cell the pairs read
are the criterion's merged pairs, consecutive REACHED integers that may
step over an unreached one (explore_sign_window.py Z2) -- the first
build read adjacent pairs only and filed the 9 cells whose one merge
steps over a hole as reach-lost (227 against 236), the count that
caught it. ~10 s (the minimizer runs once per
cell), well under 512 MB.

Cross-script: explore_sign_window.py (the criterion), explore_sign_sparse.py
(the count and the descent).

RUN RECORD. 1,103 aligned cells, 236 merging and 867 reach-lost (the
criterion's own counts reproduced), C1/C2/C3 clean at every cell and at
the two hand cells; under a second, peak 13 MB under memwatch.

FINDINGS.

H1 THE RESIDUES AT THE PAIR ARE NECESSARY AND NOT SUFFICIENT (X1 = 0;
   Y1's first clause holds, its second clause holds and its guess at
   the share is WRONG): of the 867 reach-lost cells, 566 lose the pair
   to a residue no digit holds -- the majority, not the minority
   predicted -- and 301 lose it with both residues held, to the
   backward graph. So no condition on the pair's residues closes the
   reach clause, and the digit-only YES the backlog asked for is dead
   at 301 cells.

H2 THE MONOTONE DESCENT IS SUFFICIENT AND NOT NECESSARY (C1 clean; Y2
   holds, X2 missed): 161 merging cells reach their merged pair by
   monotone steps and 75 do not. The witness prints as the hand-attack
   said -- b = 3, D = {-1, 1, 15}, pair (-4, -3), -3 reached by one
   chain of length 5 through -6 and -7 against K = 2 -- and the first
   in the sweep's order is b = 3, D = {-1, 0, 10}, pair (-3, -2), -2
   reached in 3 steps through -4.

H3 REACH READS THE GRAPH PAST THE PAIR'S NEIGHBOURHOOD (Y3 holds, X3
   missed): 49 merging cells need a chain longer than K for a merged
   integer, and at 75 a shortest chain to a merged integer passes an
   integer farther from 0 than the pair -- the same 75 cells as the
   non-monotone ones (the print: 75 both, 75 either). Half of that is a
   derivation: no merged integer of the sweep is positive (0 cells),
   and a negative n steps to (n - d)/b > 0 only with d < n, which at
   a^- <= 3, b >= 3 and n <= -1 never divides, so a non-monotone step
   from the merge regime's side is deeper than ITS SOURCE. That the
   chain then passes deeper than the PAIR, and that a monotone cell's
   shortest chain never does, are the sweep's readings and not derived.

So the answer to the backlog's question is NO with the counterexamples:
the criterion's gap clause is one window in V_K and its reach clause is
reachability in the backward graph on the crossed interval, decided
neither by the residues at the pair (301 cells), nor by a monotone
descent (75), nor by strings of length at most K (49). The criterion is
a statement about D through the finite graph D induces on I, and none
of those three shorter readings is it (rule over the sweep; the step
law in H3 is the one proved clause). Whether some other local reading
closes it is not asked here.
"""

import os
import sys
from collections import deque
from fractions import Fraction
from itertools import combinations

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_sign_sparse import analyse, fmt  # noqa: E402
from explore_sign_window import params, values, window_meets, pair_window, criterion  # noqa: E402


def steps(n, b, D, I):
    """Backward steps from n: (n - d)/b for digits of n's residue, inside I."""
    out = []
    for d in D:
        if (n - d) % b == 0:
            m = (n - d) // b
            if m in I:
                out.append((m, d))
    return out


def monotone(n, m):
    return m == 0 or (abs(m) < abs(n) and (m > 0) == (n > 0))


def reach_graph(b, D, I):
    """Shortest chain length to 0 for every integer of I (None if unreached),
    read forward from 0 over the reverse of the backward steps."""
    Iset = set(I)
    pred = {n: [m for m, _ in steps(n, b, D, Iset)] for n in I if n != 0}
    succ = {n: [] for n in I}
    for n, ms in pred.items():
        for m in ms:
            succ[m].append(n)
    dist = {0: 0}
    q = deque([0])
    while q:
        m = q.popleft()
        for n in succ[m]:
            if n not in dist:
                dist[n] = dist[m] + 1
                q.append(n)
    return dist


def mono_reach(b, D, I):
    """Integers of I with a chain of monotone steps to 0."""
    Iset = set(I)
    ok = {0}
    for n in sorted(I, key=abs):
        if n == 0:
            continue
        if any(monotone(n, m) and m in ok for m, _ in steps(n, b, D, Iset)):
            ok.add(n)
    return ok


def deepest_on_chain(n, b, D, I, dist):
    """The largest |m| along ONE shortest chain from n to 0 (ties broken
    by the digit order): a reading of that chain, not of every chain."""
    Iset = set(I)
    cur, worst = n, abs(n)
    while cur != 0:
        nxt = min((m for m, _ in steps(cur, b, D, Iset) if m in dist),
                  key=lambda m: dist[m])
        worst = max(worst, abs(nxt))
        cur = nxt
    return worst


def aligned_pairs(cell):
    b, D, I = cell["b"], cell["D"], cell["I"]
    am, ap, cm, cp, K = params(b, D)
    vals = values(b, D, k=K)
    out = []
    for v in I:
        w = v + 1
        if w in I and not window_meets(vals, *pair_window(b, v, w, K, cm, cp)):
            out.append((v, w))
    return out, K


def study(b, D, verbose=False):
    cell = analyse(b, D)
    pairs, K = aligned_pairs(cell)
    if not pairs:
        return None
    # the cell's pairs are the criterion's merged pairs (consecutive REACHED
    # integers, which may step over an unreached one) where it merges, and
    # the aligned adjacent pairs where it does not
    _, merged, _ = criterion(cell)
    if merged:
        pairs = [(v, w) for v, w, _ in merged]
    I = cell["I"]
    dist = reach_graph(b, D, I)
    mono = mono_reach(b, D, I)
    held = {n for n in I if any((n - d) % b == 0 for d in D)}
    R = set(cell["R"])
    # controls
    c1 = all(n in dist for n in mono)
    c2 = all(n not in dist for n in I if n not in held and n != 0)
    c3 = set(dist) == R | {0}
    rows = []
    for v, w in pairs:
        rows.append(dict(v=v, w=w, reached=(v in dist and w in dist),
                         res=(v in held and w in held),
                         mono=(v in mono and w in mono),
                         lens=(dist.get(v), dist.get(w)),
                         deep=(max(deepest_on_chain(v, b, D, I, dist),
                                   deepest_on_chain(w, b, D, I, dist))
                               if v in dist and w in dist else None)))
    if verbose:
        print("  b=%d D=%s level %d I=%s merges %d; R=%s"
              % (b, fmt(D), int(K), I, cell["merges"], cell["R"]))
        for r in rows:
            print("    pair (%d, %d): reached %s res %s mono %s chain lengths %s"
                  " deepest |.| on chain %s" % (r["v"], r["w"], r["reached"],
                                                r["res"], r["mono"], r["lens"],
                                                r["deep"]))
    return dict(cell=cell, K=K, rows=rows, controls=(c1, c2, c3))


def main():
    print("REACH IN THE MERGE REGIME")
    print()
    print("hand cells:")
    study(3, (-1, 1, 15), verbose=True)
    study(4, (-3, -2, -1, 12), verbose=True)
    print()
    n_al = n_merge = 0
    bad_controls = 0
    x1 = []
    lost_res_false = lost_res_true = 0
    merge_mono = merge_nonmono = 0
    over_k = deeper = deeper_nonmono = positive_pairs = 0
    over_k_cells = []
    nonmono_cells = []
    for b in range(2, 6):
        for am in range(1, 4):
            for ap in range(1, 16):
                interior = list(range(-am + 1, ap))
                subs = []
                for r in (1, 2):
                    subs.extend(combinations(interior, r))
                for sub in subs:
                    D = tuple(sorted((-am,) + sub + (ap,)))
                    gapL = max(D[i + 1] - D[i] for i in range(len(D) - 1)) \
                        - Fraction(am + ap, b - 1)
                    if gapL < b:
                        continue
                    s = study(b, D)
                    if s is None:
                        continue
                    n_al += 1
                    if not all(s["controls"]):
                        bad_controls += 1
                    merged_rows = [r for r in s["rows"] if r["reached"]]
                    if merged_rows:
                        n_merge += 1
                        for r in merged_rows:
                            if not r["res"]:
                                x1.append((b, D, r))
                        if any(r["mono"] for r in merged_rows):
                            merge_mono += 1
                        else:
                            merge_nonmono += 1
                            nonmono_cells.append((b, D, merged_rows[0]))
                        if any(max(r["lens"]) > s["K"] for r in merged_rows):
                            over_k += 1
                            over_k_cells.append((b, D, s["K"], merged_rows[0]))
                        if any(r["deep"] > max(abs(r["v"]), abs(r["w"]))
                               for r in merged_rows):
                            deeper += 1
                            if not any(r["mono"] for r in merged_rows):
                                deeper_nonmono += 1
                        if any(r["v"] > 0 or r["w"] > 0 for r in merged_rows):
                            positive_pairs += 1
                    else:
                        if any(r["res"] for r in s["rows"]):
                            lost_res_true += 1
                        else:
                            lost_res_false += 1
    print("aligned cells %d, merging %d, reach-lost %d; control failures %d"
          % (n_al, n_merge, n_al - n_merge, bad_controls))
    print("X1 merging pairs with RES false: %d" % len(x1))
    print("Y1 reach-lost cells: RES false at every aligned pair %d;"
          " RES true at some aligned pair (lost with the residues present) %d"
          % (lost_res_false, lost_res_true))
    print("Y2 merging cells with a MONO pair %d, with no MONO pair %d"
          % (merge_mono, merge_nonmono))
    for b, D, r in nonmono_cells[:6]:
        print("   b=%d D=%s pair (%d, %d) chain lengths %s"
              % (b, fmt(D), r["v"], r["w"], r["lens"]))
    print("Y3 merging cells whose merged pair needs a chain longer than K: %d;"
          " whose chain passes deeper than the pair: %d" % (over_k, deeper))
    for b, D, lev, r in over_k_cells[:6]:
        print("   b=%d D=%s level %d pair (%d, %d) chain lengths %s deepest %s"
              % (b, fmt(D), lev, r["v"], r["w"], r["lens"], r["deep"]))
    print("   cells both deeper and without a MONO pair: %d; merging cells"
          " with a positive merged integer: %d" % (deeper_nonmono, positive_pairs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
