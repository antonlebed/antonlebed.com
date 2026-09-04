"""
explore_four_prints.py -- four conjectures, each decided by the one print
that can end it: whether the subset-sum instance itself re-keys the
abandoned atom's fate, whether the least split prime's non-square bias is
reduction theory, whether an escape from a stall drops a committed cell,
and whether a full single-coordinate clique leaves any class stalled.

THE FOUR QUESTIONS.

  Q1. THE UNDER-KEYED AUDIT, keyed by the instance. On the set-valued
      ruler an atom's fate under the min-cost covering optimum is no
      function of its own numbers (explore_ruler_dual.py D3: 67 of 444
      keys collide), nor of its numbers plus the certificate's room
      (explore_three_seats.py F1: 138 collisions at reuse 0.998). The
      optimum is the strict-above set plus the cheapest sub-collection
      of the TIED BLOCK at the operative level that closes the deficit
      (explore_ruler_barecell.py), a min-cost subset sum whose instance
      is the multiset of the tied pairs' weights and the deficit. The
      question: keyed by its own numbers plus that whole instance, does
      any forced atom still collide?

  Q2. THE FORM-MINIMUM SEAT. The least odd split prime of a quadratic
      field with a cyclic even class group lands in a non-square class
      0.77 (real) and 0.69 (imaginary) of the time against an exact
      Minkowski-generation null of 0.51 (explore_three_seats.py F3),
      and whether the seat is the place's RANK or its NORM was
      undecided there. The reduction-theory reading: a prime p lies in
      a class C only if p is at least C's least value, the leading
      coefficient of its reduced form for a non-principal class and
      the constant term for the principal one, so the least split
      prime can only sit in the classes whose minima it clears, and a
      small least prime is confined to the few classes of small
      minimum. The question: over the imaginary fields to |D| <= 32000,
      does the rank-1 non-square share exceed the share of non-square
      classes among the classes the prime CAN sit in (the reduction
      null), and does the fixed-prime rank contrast survive at a
      standard error that resolves 0.05?

  Q3. THE ESCAPE THAT FORGETS. Every finite-loss stall of the reader
      corpus has escape radius exactly 2 through the cure graph
      (explore_charged_radius.py). A reader built as monotone growth
      would keep every cell it has committed; the question is whether
      the escape class's members hold, at every counted step, a cell
      inside the one the stall's members committed there, or whether
      one escape DROPS a committed cell -- holds a cell not inside the
      stall's. Read over the three unresourced horizon-cut stalls
      (explore_shift_telescope.py SQ_SPECIMENS, evaluated by
      explore_stall_assembly.py), the cell where no budget can decrement
      anything; the six burst traps run under a budget and the
      disagreement is a composite over nine rows, both outside the
      question's own frame, and are not read here.

  Q4. THE FLOOR IS THE WHOLE ALPHABET. Thirty of the 601 off-bottom
      classes of the ten stall landscapes have no improving patience
      jump at any distance and are cured only by a route flip or a
      drawdown move (explore_move_set.py). The question: under a clique
      on EVERY coordinate separately -- either route bit, either
      patience to any value, the drawdown to any value -- does any
      class still stall, so that a two-coordinate move is needed?

WHOSE VOCABULARY. Q1 in the knapsack's (pair, tied block, deficit,
forced fate); Q2 in reduced binary quadratic forms' (a reduced definite
form (a, b, c), its leading coefficient the class's minimum, a square
being a class whose order divides h/2); Q3 and Q4 in the reader
corpus's (policy, class, committed cell, cure graph, patience axis).

TRANSPLANTS, MARKED.
  Q1 imports from the LP dual the belief that the fate is decided
     locally at the tied block; the parent measured that belief
     failing at one number and at two, so it enters weak.
  Q2 imports the cubic seat's "rank" across the one thing reduction
     theory says differs: a quadratic class has an explicit minimum
     and a cubic partial place's class does not carry one so cheaply.
  Q3 imports "forgetting" from the budgeted trap, where a budget is
     what a decrement spends; unresourced there is no budget, and the
     only thing an escape can drop is a cell.
  Q4 imports "clique" from the patience axis, where it dissolved every
     stall; the drawdown axis is a different grade.

THE HAND ATTACK, before any engine code.

  Q1. A per-cell key added to a per-atom key separates atoms of
      different cells for free, so the read carries the key's REUSE
      (share of keys whose forced atoms come from two or more cells)
      beside its collision count, as the parent did; a kill needs zero
      collisions at a reuse not near zero. The instance is exact in
      Fraction. Two keys are read: weights alone, and weights plus the
      deficit, since the deficit is the instance's target and the
      weights alone are not the instance. The equal-weight arms are the
      positive control (zero collisions proved), and the parent key
      must reprint 444 / 67 before the new keys are read.

  Q2. The kill as first written -- split the fields by whether the
      least split prime lies below the principal form's least non-unit
      value (|D|+1)/4 -- cannot be read: that line is above 3 at every
      |D| >= 11, so the above-line cell holds only the handful of
      fields with |D| < 11 and its share is unreadable. The count is
      printed rather than assumed. The observable is refrozen on the
      reduction null: per field, the classes whose minimum the least
      odd split prime clears, the non-square share among them, averaged
      over fields; the prime's own class is always among them (its
      reduced form's leading coefficient is at most the prime), so the
      set is never empty. The census at |D| <= 32000 holds every split
      prime of every field if run the parent's way and would pass the
      memory line; it is run in bands of 4000 with per-field
      accumulation, and the parent's |D| <= 8000 numbers (0.685 +-
      0.014 at rank 1, D = +0.045 se 0.025) are the reprint control at
      the first two bands.

  Q3. "Inside" is the parent's cell_inside (explore_stall_tie.py), an
      interval containment in exact rationals. A drop is counted per
      (stall member, escape member, counted step). The positive control
      is the reader reproducing each member's class signature,
      and the decision lemma's own print: patience-down neighbours
      whose steps are forced nest, so some patience-down pair of the
      same landscape must be fully nested or the read is not looking at
      the same cells the corpus did. A stall member's cell at a step is
      read at the step's END; the trace's third entry.

  Q4. Stalls are monotone under adding edges, so the count under the
      full single-coordinate clique is at most the 30 classes patience
      jumps alone leave, which is the reprint control. The two-coordinate clique is
      read beside it for the survivors' anatomy only.

PREDICTIONS, frozen before the run.
  P1. The instance key leaves collisions: at least 5 survive under
      weights plus deficit, at reuse above 0.5.
  P2. Under 10 fields have their least odd split prime above the
      principal form's line. The reduction null sits between 0.55 and
      0.65 (the small-minimum classes are mostly non-square, since the
      principal class and the ambiguous classes of small minimum are
      squares or non-squares by the genus, not by the coin); the
      rank-1 excess over it is under 0.10; D at |D| <= 32000 prints
      between 0.02 and 0.07.
  P3. Every escape drops at least one committed cell: an escape is a
      coarser reader at the step where the stall over-committed.
  P4. Zero classes stall under the full single-coordinate clique.

KILL CRITERIA, as observables.
  Q1 KILLED (the class was under-keyed; fate is a function of the atom
     and the instance) iff the weights-plus-deficit key prints ZERO
     collisions on the unequal arms at reuse >= 0.1; HOLDS WHOLE iff
     it prints 5 or more. Between, refrozen on the print.
  Q2 KILLED as form-seated iff the rank-1 share minus the reduction
     null is under 0.05 at two standard errors AND D at |D| <= 32000 is
     under 0.05 at two standard errors; CARRIED iff the excess over the
     reduction null is at least 0.10 at two se AND D is at least 0.10
     at two se. Otherwise BETWEEN, refrozen on the print.
  Q3 KILLED (a growth walk cannot be the escape) iff at least one
     escape member at one stall drops a committed cell; SURVIVES iff
     the drop count is zero over every stall's every radius-2 escape.
  Q4 KILLED (one grade's floor does not reach it) iff any class stalls
     under the full single-coordinate clique; SURVIVES iff zero.

CONTROLS, run before any verdict is read.
  C1 (Q1) Equal-weight arms: zero collisions under every key.
  C2 (Q1) Parent key on the unequal arms: 444 distinct, 67 colliding.
  C3 (Q2) The first two bands (|D| <= 8000) reprint 1,096 fields, the
     rank-1 share 0.685 within 0.005 and the parent's D within 0.01.
  C4 (Q2) Class count equals the class number, cyclicity certified,
     and the least odd split prime's own class is among the classes
     whose minimum it clears, at every field.
  C5 (Q3) At every stall landscape the reader reproduces each
     member's class signature, and at least one patience-down pair of
     the landscape is fully nested.
  C6 (Q4) Patience jumps alone (any distance, no route or drawdown
     move) leave 30 classes with no improving neighbour over the ten
     landscapes.

FINDINGS (entered after the run; 4,058 controls run, 0 failed; wall
54.7 s, peak working set 170.7 MB under memwatch's 512 MB default).

  F1. THE INSTANCE RE-KEYS ALL BUT SIX, AND THE SIX ARE THE OVER-CLOSING
      EXCHANGE. Equal-weight arms: zero collisions under all three keys
      (26, 63 and 113 keys). Unequal arms, 38,250 cells: the parent key
      reprints 444 distinct and 67 colliding; the weights-only key
      splits them into 9,022 keys with 246 colliding (reuse 0.998); the
      instance key -- weights plus deficit -- into 16,232 keys with 6
      colliding at reuse 0.997. Tied blocks run 1 to 6 pairs. At five
      of the six the cheapest closing of the block leaves a surplus
      over the deficit at least as large as the atom's own strictly-
      above coverage (3/25 against 3/100 at the first), so the optimum
      may drop the atom's above-level pair or another atom's, and which
      it drops is not in the key; the sixth atom has no strictly-above
      label, its whole fate the block's one pair against a lighter
      label below the level. Both are the exchanges
      explore_ruler_exchange.py records. Witness: mass 1/20, row
      (3/5, 1/5, 1/5), level 1/5, block (1/20, 1/20, 4/5, 4/5), deficit
      1/25 -- abandoned at 8 cells, served at 4. P1 held (6 >= 5).
      Q1 HOLDS WHOLE: fate is not a function of the atom and the
      subset-sum instance; the above-level set decides too, through the
      surplus the block's over-closing leaves.

  F2. THE SEAT IS MOSTLY FORM MINIMA, AND WHAT IS LEFT IS SMALL AND
      SHARP. The first two bands reprint the parent: 1,096 fields,
      rank-1 share 0.685 +- 0.014, D = +0.045 (se 0.025); C4 holds at
      every field (the least prime's class always clears its minimum).
      Over |D| <= 32000: 4,044 fields; exactly ONE has its least odd
      split prime above the principal form's line, as the hand attack
      said; the classes the least prime can sit in number 1 to 17, the
      median 3. Rank-1 non-square share 0.657 +- 0.007, ranks 2 to 5 at
      0.588, 0.591, 0.567, 0.560. The reduction null averages 0.595, so
      of the +0.157 excess over the coin, +0.095 is where the least
      prime is ALLOWED to sit and +0.062 (se 0.007, nine standard
      errors) is not. The fixed-prime rank contrast D = +0.030 (se
      0.013), down from +0.045 at a quarter of the population, with
      the rank-1 column above the rank>=2 column at p = 5 (0.71 against
      0.58) and below it at p = 7 (0.56 against 0.62). P2 held on every
      count but the excess, which is under 0.10 and not under 0.05.
      Neither the form-seated kill (D + 2 se = 0.056) nor the carrying
      bar is met. Q2 BETWEEN. What decides it next is D at a standard
      error under 0.008, |D| <= 100000 in the same bands.

  F3. EVERY UNRESOURCED STALL ESCAPES BY DROPPING A CELL. The three
      horizon-cut landscapes carry 19, 21 and 17 classes, one stall
      each of one member, at ranks 11, 12 and 3, with 5, 4 and 3
      radius-2 escapes; the reader reproduces every member's class
      signature, and 67, 67 and 73 patience-down pairs are fully nested
      (C5). Of 40 (stall member, escape member) pairs, 16 drop a
      committed cell; at the first stall the rank-4 escape's members
      drop the stall's cell at the first counted step (8) and the
      rank-7 escape's at steps 8, 10 and 11; per stall the dropping
      pairs are 8 of 10, 6 of 8 and 2 of 22. P3 FAILED: it predicted
      all 40, and the other 24 pairs refine the stall's trace at every
      counted step and rank lower even so. Q3 KILLED: a reader
      forbidden to drop a
      committed cell cannot take 16 of the 40 escapes, and every stall
      here has one.

  F4. ONE COORDINATE ALWAYS SUFFICES. Over the ten landscapes' 601
      off-bottom classes, patience jumps alone leave 30 with no
      improving neighbour (the reprint); the full single-coordinate
      clique leaves 0, as does the two-coordinate clique. P4 held.
      Q4 SURVIVES: no class needs a two-coordinate move; what the 30
      need is a route flip or a drawdown jump, each one coordinate.

RUN RECORD. Three runs. The first failed two controls of its own
making: C5 compared the reader's loss triple against the quotient's
lexicographic loss object, a format and not a fact, and C6 counted
stalls under the patience clique WITH the cure moves (0) where the
corpus's 30 are counted under patience jumps ALONE; both were
rewritten to what the corpus prints and the science was unchanged
across all three runs. Second run identical to the first (a patch
that did not land). Third: wall 54.7 s, peak 170.7 MB.

RESOURCE NOTE. Q1 is the parent's sweep with the tied block read per
cell (about 20 s, 15 MB). Q2 is eight bands of the imaginary census,
each dropped before the next; the parent's whole |D| <= 8000 census
peaked at 283 MB, so a 4000-band should sit near 150 MB; wall estimate
three to five minutes. Q3 evaluates three landscapes (seconds). Q4
rebuilds the ten landscapes as explore_move_set.py does (about 15 s).
Run under memwatch at the default ceiling.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import math                                          # noqa: E402
import sys                                           # noqa: E402
import time                                          # noqa: E402
from collections import defaultdict                  # noqa: E402
from fractions import Fraction                       # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_abandon import (                  # noqa: E402
    ALPHA, MENU_A, MENU_B, ROWS, WEIGHTS, EQUAL, make_cell, check_truth,
    all_optima,
)
from explore_ruler_barecell import operative_level   # noqa: E402
import explore_class_order as CO                     # noqa: E402
import explore_principal_share as PS                 # noqa: E402
import explore_scale_clock as SC                     # noqa: E402
import explore_stall_tie as ST                       # noqa: E402
import explore_stall_assembly as SA                  # noqa: E402
import explore_shift_telescope as TS                 # noqa: E402
import explore_move_set as MS                        # noqa: E402

F = Fraction
CHECKS = [0, 0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        CHECKS[1] += 1
        print("  CONTROL FAILED: %s" % msg)
    return cond


def section(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


# =============================================================== Q1

def instance_of(cell, level):
    """The tied block's weight multiset and the deficit it must close."""
    target = 1 - ALPHA
    strict = F(0)
    weights = []
    for r in range(cell.M):
        w = cell.atom_prob(r)
        for v in cell.posterior(r):
            if v > level:
                strict += w * v
            elif v == level:
                weights.append(w)
    return tuple(sorted(weights)), target - strict


def min_surplus(weights, deficit, level):
    """The surplus over the deficit left by the cheapest sub-multiset
    of the tied block that closes it: pair of weight w covers w*level
    and costs w, so the cheapest closing is the min-weight subset whose
    weight sum times the level reaches the deficit; returns coverage
    minus deficit at that subset, or None if the block cannot close."""
    best = None
    n = len(weights)
    for mask in range(1 << n):
        tot = sum(weights[i] for i in range(n) if mask >> i & 1)
        if tot * level >= deficit and (best is None or tot < best):
            best = tot
    return None if best is None else best * level - deficit


def key_parent(cell, r, level, inst):
    return (cell.atom_prob(r),
            tuple(sorted(cell.posterior(r), reverse=True)), level)


def key_weights(cell, r, level, inst):
    return key_parent(cell, r, level, inst) + (inst[0],)


def key_instance(cell, r, level, inst):
    return key_parent(cell, r, level, inst) + inst


def sweep_keys(menu, tag, rows_list, weights, keyfns, indexes):
    cells = 0
    for rows in rows_list:
        for wts in weights:
            cell = make_cell(menu, tag, rows, wts)
            if not check_truth(cell):
                continue
            level, _m, _c, _s = operative_level(cell, ALPHA)
            best, arg = all_optima(cell, ALPHA)
            if best is None:
                continue
            cells += 1
            inst = instance_of(cell, level)
            cid = (tag, rows, wts)
            for r in range(cell.M):
                if all(s[r] == 0 for s in arg):
                    fate = "ab"
                elif all(s[r] > 0 for s in arg):
                    fate = "sv"
                else:
                    continue
                for kf, idx in zip(keyfns, indexes):
                    slot = idx.setdefault(kf(cell, r, level, inst),
                                          {"ab": set(), "sv": set()})
                    slot[fate].add(cid)
    return cells


def read_index(idx):
    coll = [k for k, s in idx.items() if s["ab"] and s["sv"]]
    reuse = sum(1 for s in idx.values() if len(s["ab"] | s["sv"]) >= 2)
    return len(idx), len(coll), reuse, coll


def q1():
    section("Q1  THE UNDER-KEYED AUDIT -- the subset-sum instance in the key")
    t0 = time.time()
    kf = (key_parent, key_weights, key_instance)
    names = ("parent", "weights", "instance")
    eq = [{}, {}, {}]
    un = [{}, {}, {}]
    n_eq = sweep_keys(MENU_A, "A-EQ", ROWS, [EQUAL], kf, eq)
    n_eq += sweep_keys(MENU_B, "B-EQ", ROWS, [EQUAL], kf, eq)
    n_un = sweep_keys(MENU_A, "A-UN", ROWS, WEIGHTS, kf, un)
    n_un += sweep_keys(MENU_B, "B-UN", ROWS, WEIGHTS, kf, un)
    print("  cells: %d equal-weight, %d unequal (%.1fs)"
          % (n_eq, n_un, time.time() - t0))
    for name, idx in zip(names, eq):
        n, c, _r, _ = read_index(idx)
        print("  C1 equal weights, %-8s key: %d keys, %d collisions"
              % (name, n, c))
        ok(c == 0, "equal-weight collisions under the %s key" % name)
    out = {}
    for name, idx in zip(names, un):
        n, c, r, coll = read_index(idx)
        out[name] = (n, c, r / n, coll)
        print("  unequal, %-8s key: %d distinct, %d colliding, %d reused "
              "across cells (%.3f)" % (name, n, c, r, r / n))
    ok(out["parent"][0] == 444 and out["parent"][1] == 67,
       "C2 parent key reprints 444 / 67")
    sizes = sorted({len(k[3]) for k in un[1]})
    print("  tied-block sizes seen across the forced atoms: %s"
          % (sizes,))
    over = 0
    for k in out["instance"][3]:
        s = un[2][k]
        # the atom's own strictly-above coverage against the surplus
        # the cheapest closing of the block leaves: the pair is
        # droppable only if the surplus covers what it covered
        own = k[0] * sum(v for v in k[1] if v > k[2])
        surplus = min_surplus(k[3], k[4], k[2])
        drop = surplus is not None and own > 0 and surplus >= own
        over += drop
        print("  surviving collision: mass %s row (%s) level %s block %s "
              "deficit %s -- abandoned in %d cell(s), served in %d; "
              "cheapest closing's surplus %s against the atom's own "
              "strict-above coverage %s: %s"
              % (k[0], ",".join(str(v) for v in k[1]), k[2],
                 "(" + ",".join(str(v) for v in k[3]) + ")", k[4],
                 len(s["ab"]), len(s["sv"]), surplus, own,
                 "droppable" if drop else
                 ("no strict-above pair" if own == 0
                  else "NOT droppable")))
    print("  surviving collisions whose surplus lets the atom's own "
          "strict-above pair go: %d of %d" % (over, out["instance"][1]))
    c, reuse = out["instance"][1], out["instance"][2]
    if c == 0 and reuse >= 0.1:
        verdict = "KILLED -- fate is a function of the atom and the instance"
    elif c >= 5:
        verdict = "HOLDS WHOLE"
    else:
        verdict = "BETWEEN"
    print("  Q1 verdict: %s (instance-key collisions %d, reuse %.3f)"
          % (verdict, c, reuse))
    return verdict, out


# =============================================================== Q2

def is_square(order, h):
    return (h // 2) % order == 0


class Acc:
    """Per-arm accumulators over a streamed census."""

    def __init__(self):
        self.fields = 0
        self.rank = defaultdict(lambda: [0, 0])
        self.red_null = []
        self.pr1 = defaultdict(lambda: [0, 0])
        self.prk = defaultdict(lambda: [0, 0])
        self.above_line = 0
        self.own_not_avail = 0
        self.avail_sizes = []


def band_census(sign, lo, hi, plist, acc):
    """CO.sweep over fundamental discriminants in (lo, hi], streamed
    into acc; the band's rows are dropped on return."""
    gen = PS.fundamental_discriminants

    def banded(a, b, s):
        for D in gen(1, b, s):
            if abs(D) > lo:
                yield D
    old_gen, old_b = CO.fundamental_discriminants, CO.DBOUND
    CO.fundamental_discriminants = banded
    CO.DBOUND = hi
    try:
        rows, _bad, _ib, _c2, _c4, _lb = CO.sweep(sign, plist)
    finally:
        CO.fundamental_discriminants = old_gen
        CO.DBOUND = old_b
    for D, hplus, recs, orders, _n0, _t0, _q, hits in rows:
        h = hplus
        if h % 2 or h < 2 or max(orders.values()) != h:
            continue
        ok(len(recs) == h, "D=%d class count %d against h %d"
           % (D, len(recs), h))
        acc.fields += 1
        triv = next(k for k, rec in recs.items() if rec[0])
        line = triv[2]                         # the principal form's c
        p1, k1 = hits[0]
        if p1 > line:
            acc.above_line += 1

        def minimum(k):
            return k[2] if k == triv else k[0]
        avail = [k for k in orders if minimum(k) <= p1]
        if k1 not in avail:
            acc.own_not_avail += 1
        acc.avail_sizes.append(len(avail))
        ns_avail = sum(1 for k in avail if not is_square(orders[k], h))
        acc.red_null.append(ns_avail / len(avail))
        for i, (p, k) in enumerate(hits[:8]):
            ns = not is_square(orders[k], h)
            acc.rank[i + 1][0] += ns
            acc.rank[i + 1][1] += 1
            if p <= 50:
                (acc.pr1 if i == 0 else acc.prk)[p][0] += ns
                (acc.pr1 if i == 0 else acc.prk)[p][1] += 1
    del rows


def read_acc(acc, tag):
    print("  %s: %d fields with a cyclic even class group" % (tag, acc.fields))
    r1 = acc.rank[1]
    sh = r1[0] / r1[1]
    se = math.sqrt(sh * (1 - sh) / r1[1])
    print("  rank-1 non-square share %.3f +- %.3f (%d of %d); ranks 2..5: %s"
          % (sh, se, r1[0], r1[1],
             ", ".join("%.3f" % (acc.rank[r][0] / acc.rank[r][1])
                       for r in (2, 3, 4, 5) if acc.rank[r][1])))
    nl = sum(acc.red_null) / len(acc.red_null)
    print("  fields whose least odd split prime lies above the principal "
          "form's line: %d of %d" % (acc.above_line, acc.fields))
    print("  reduction null (non-square share among the classes whose "
          "minimum the least prime clears, averaged over fields): %.3f; "
          "classes available per field: min %d, median %d, max %d"
          % (nl, min(acc.avail_sizes),
             sorted(acc.avail_sizes)[len(acc.avail_sizes) // 2],
             max(acc.avail_sizes)))
    print("  rank-1 excess over 1/2: %+.3f; over the reduction null: "
          "%+.3f (se %.3f)" % (sh - 0.5, sh - nl, se))
    wsum = dsum = 0.0
    print("  (p, rank) table, non-square share at rank 1 / rank >= 2:")
    for p in sorted(set(acc.pr1) | set(acc.prk)):
        a, b = acc.pr1.get(p, [0, 0]), acc.prk.get(p, [0, 0])
        if p <= 23:
            print("    p = %2d: rank 1 %s (%d)   rank >= 2 %s (%d)"
                  % (p, "%.2f" % (a[0] / a[1]) if a[1] else "  -", a[1],
                     "%.2f" % (b[0] / b[1]) if b[1] else "  -", b[1]))
        if a[1] >= 15 and b[1] >= 15:
            s1, sk = a[0] / a[1], b[0] / b[1]
            var = (max(s1 * (1 - s1), 0.01) / a[1]
                   + max(sk * (1 - sk), 0.01) / b[1])
            wsum += 1 / var
            dsum += (s1 - sk) / var
    Dc, Dse = dsum / wsum, 1 / math.sqrt(wsum)
    print("  rank against norm: pooled rank-1 minus rank->=2 share at fixed "
          "p, D = %+.3f (se %.3f)" % (Dc, Dse))
    return (sh, se), nl, (Dc, Dse)


def q2():
    section("Q2  THE FORM-MINIMUM SEAT -- the imaginary fields to |D| <= 32000")
    plist = PS.primes_upto(CO.PCAP)
    acc = Acc()
    t0 = time.time()
    band_census(-1, 0, 4000, plist, acc)
    band_census(-1, 4000, 8000, plist, acc)
    print("  bands to 8000 done (%.1fs)" % (time.time() - t0))
    (sh, se), nl, (Dc, Dse) = read_acc(acc, "C3 reprint, |D| <= 8000")
    ok(acc.fields == 1096 and abs(sh - 0.685) <= 0.005
       and abs(Dc - 0.045) <= 0.01,
       "C3 reprint of 1,096 fields, 0.685, D = +0.045")
    ok(acc.own_not_avail == 0, "C4 the least prime's own class clears "
       "its minimum at every field")
    for lo in range(8000, 32000, 4000):
        band_census(-1, lo, lo + 4000, plist, acc)
        print("  band (%d, %d] done, %d fields (%.1fs)"
              % (lo, lo + 4000, acc.fields, time.time() - t0))
    ok(acc.own_not_avail == 0, "C4 at |D| <= 32000")
    (sh, se), nl, (Dc, Dse) = read_acc(acc, "imaginary, |D| <= 32000")
    exc = sh - nl
    form = exc + 2 * se < 0.05 and Dc + 2 * Dse < 0.05
    carry = exc - 2 * se >= 0.10 and Dc - 2 * Dse >= 0.10
    if form:
        verdict = "KILLED -- form-seated"
    elif carry:
        verdict = "CARRIED"
    else:
        verdict = "BETWEEN"
    print("  Q2 verdict: %s (excess over the reduction null %+.3f se %.3f; "
          "D %+.3f se %.3f)" % (verdict, exc, se, Dc, Dse))
    return verdict, (sh, se, nl, Dc, Dse, acc.above_line, acc.fields)


# =============================================================== Q3

def cells_of(J, pol, horizon):
    tr = SC.run_reader(J, pol[:4], horizon)[3]
    return [tr[n][2] for n in range(SC.N0, horizon)]


def q3():
    section("Q3  THE ESCAPE THAT FORGETS -- the unresourced horizon-cut stalls")
    drops_total = 0
    escapes_total = 0
    for tag, digs, horizon in TS.SQ_SPECIMENS:
        ev = SA.evaluate(list(digs), "sq", horizon)
        J, mem, nbrs, qranks = ev["J"], ev["mem"], ev["nbrs"], ev["qranks"]
        # C5a: the reader reproduces each member's class signature
        bad = 0
        for s, pols in mem.items():
            for p in pols:
                if ST.run_pol(J, p, None, 0, horizon)[1] != s:
                    bad += 1
        # C5b: some patience-down pair fully nested
        nested_pairs = 0
        cache = {}

        def cells(p):
            if p not in cache:
                cache[p] = cells_of(J, p, horizon)
            return cache[p]
        sig_of = {p: s for s, ps in mem.items() for p in ps}
        for p in sig_of:
            st, ss, pt, pc, d = p
            for q in ((st, ss, pt, 0, d), (st, ss, 0, pc, d)):
                if q in sig_of and q != p and pt is not None \
                        and pc is not None and q[2:4] != p[2:4]:
                    if all(ST.cell_inside(a, b)
                           for a, b in zip(cells(q), cells(p))):
                        nested_pairs += 1
        print("  %s (sq h=%d): %d classes, %d stalls; C5 signature "
              "mismatches %d, fully nested patience-down pairs %d"
              % (tag, horizon, len(mem), len(ev["stalls"]), bad,
                 nested_pairs))
        ok(bad == 0, "C5 signature reproduction at %s" % tag)
        ok(nested_pairs > 0, "C5 a nested patience-down pair at %s" % tag)
        for s0 in ev["stalls"]:
            r0 = qranks[s0]
            escapes = set()
            for t in nbrs[s0]:
                for u in nbrs[t]:
                    if u != s0 and u not in nbrs[s0] and qranks[u] < r0:
                        escapes.add(u)
            print("    stall %s rank %d, members %d, radius-2 escapes %d"
                  % (s0, r0, len(mem[s0]), len(escapes)))
            here = [0, 0]
            for u in sorted(escapes, key=lambda x: qranks[x]):
                for q in mem[u]:
                    cq = cells(q)
                    for p in mem[s0]:
                        cp = cells(p)
                        dropped = [SC.N0 + i for i, (a, b)
                                   in enumerate(zip(cq, cp))
                                   if not ST.cell_inside(a, b)]
                        escapes_total += 1
                        here[1] += 1
                        if dropped:
                            drops_total += 1
                            here[0] += 1
                            if drops_total <= 4:
                                print("      escape %s rank %d member %s "
                                      "drops the cell of stall member %s "
                                      "at steps %s"
                                      % (u, qranks[u], SC.fmt_pol5(q),
                                         SC.fmt_pol5(p), dropped[:6]))
            print("      pairs at this stall %d, dropping %d"
                  % (here[1], here[0]))
    print("  (stall member, escape member) pairs %d; pairs where the "
          "escape drops a committed cell %d" % (escapes_total, drops_total))
    verdict = "KILLED -- an escape drops a committed cell" if drops_total \
        else "SURVIVES"
    print("  Q3 verdict: %s" % verdict)
    return verdict, escapes_total, drops_total


# =============================================================== Q4

def nb_full(p, axis, daxis):
    """Every single-coordinate move to any value: both route bits,
    either patience to any value, the drawdown to any value."""
    st, ss, pt, pc, d = p
    out = [(1 - st, ss, pt, pc, d), (st, 1 - ss, pt, pc, d)]
    out += [(st, ss, v, pc, d) for v in axis if v != pt]
    out += [(st, ss, pt, v, d) for v in axis if v != pc]
    out += [(st, ss, pt, pc, v) for v in daxis if v != d]
    return out


def nb_two(p, axis, daxis):
    """Every move changing at most two coordinates, each to any value."""
    seen = set()
    out = []
    for q in nb_full(p, axis, daxis):
        for u in nb_full(q, axis, daxis):
            if u != p and u not in seen:
                seen.add(u)
                out.append(u)
        if q not in seen:
            seen.add(q)
            out.append(q)
    return out


def q4():
    section("Q4  THE FLOOR IS THE WHOLE ALPHABET -- the full clique")
    t0 = time.time()
    lands = MS.collect()
    print("  %d landscapes rebuilt (%.1fs)" % (len(lands), time.time() - t0))
    tot_off = n_pat = n_full = n_two = 0
    survivors = []
    for (fam, name, world, setting, space, sig_of, mem, qranks,
         daxis, stalls, _f) in lands:
        off = sum(1 for s in mem if qranks[s] > 0)
        tot_off += off
        e_pat = MS.edges(space, sig_of,
                         lambda q: MS._patience_jumps(q, SC.AX_BASE,
                                                      len(SC.AX_BASE)))
        e_full = MS.edges(space, sig_of,
                          lambda q: nb_full(q, SC.AX_BASE, daxis))
        e_two = MS.edges(space, sig_of,
                         lambda q: nb_two(q, SC.AX_BASE, daxis))
        s_pat = MS.stalls_of(e_pat, qranks)
        s_full = MS.stalls_of(e_full, qranks)
        s_two = MS.stalls_of(e_two, qranks)
        n_pat += len(s_pat)
        n_full += len(s_full)
        n_two += len(s_two)
        print("  %-24s %-11s off-bottom %3d | stalled: patience jumps alone "
              "%d, full single-coordinate clique %d, two-coordinate %d"
              % (name, setting, off, len(s_pat), len(s_full), len(s_two)))
        for s in s_full:
            survivors.append((name, s, qranks[s], len(mem[s])))
    print("  over the ten: off-bottom classes %d; stalled under the "
          "patience jumps alone %d, the full clique %d, the two-coordinate "
          "clique %d" % (tot_off, n_pat, n_full, n_two))
    ok(n_pat == 30, "C6 patience jumps alone reprint 30")
    for name, s, r, m in survivors[:6]:
        print("    survivor under the full clique: %s class rank %d, %d "
              "members" % (name, r, m))
    verdict = "KILLED -- a class needs a two-coordinate move" if n_full \
        else "SURVIVES"
    print("  Q4 verdict: %s" % verdict)
    return verdict, n_pat, n_full, n_two


if __name__ == "__main__":
    t0 = time.time()
    v1 = q1()
    v4 = q4()
    v3 = q3()
    v2 = q2()
    print("\nSUMMARY")
    print("  Q1 %s" % v1[0])
    print("  Q2 %s" % v2[0])
    print("  Q3 %s" % v3[0])
    print("  Q4 %s" % v4[0])
    print("  controls: %d run, %d failed" % (CHECKS[0], CHECKS[1]))
    print("  wall %.1fs" % (time.time() - t0))
