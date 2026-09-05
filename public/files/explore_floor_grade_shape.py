"""explore_floor_grade_shape.py -- three conjectures, each decided by the
one print frozen to end it: whether every stall a patience jump cannot
cure is cured by a move landing at its coordinate's own end, whether the
non-square share of a quadratic class group's classes is graded by the
size of the reduced form's leading coefficient, and whether two
paradigms of different shape grow different substrates under one base.

THE THREE QUESTIONS.

  Q1. THE FLOOR LANDING. Of the 601 off-bottom classes of the reader
      corpus's ten stall landscapes, 30 have no improving patience jump
      at any distance and are cured only by a route flip or a drawdown
      jump, each a single coordinate (explore_four_prints.py F4,
      explore_move_set.py). The floor lemma says an exact descent's
      stall is a unit-step artifact: the floor sits a bounded jump away
      and is strictly better by a lemma about the grade alone. The
      question: for those 30, does the curing move land at the
      coordinate's own END -- the first or last value of its axis --
      so that the target is computed from the grade, or does it land
      mid-axis, where it can only be searched for?

  Q2. THE LEADING-COEFFICIENT GRADE. Over the imaginary quadratic
      fields with a cyclic even class group to |D| <= 100000 (11,833 of
      them, explore_five_prints.py F3), the least odd split prime lands
      in a non-square class 0.640 of the time, +0.060 over the
      reduction null -- the non-square share among the classes whose
      reduced-form minimum the prime clears. The question: is that
      residual the small end of a curve -- the non-square share among
      ALL classes, every class counted once, falling as the reduced
      form's leading coefficient a rises -- or is the share flat in a,
      the residual then the least prime's own and not the form's?

  Q3. THE PARADIGM SHAPE. In the grammar arena a substrate grown by
      least-new over a divisibility demand followed the input CODE:
      base 30 grows {2, 3, 5} and base 35 grows {2, 3, 5, 7} for the
      same paradigm (explore_grammar_growth.py finding 1). The question:
      under ONE base, with the same lexeme count and the same cell
      count, do two paradigms of different SHAPE -- agglutinative,
      form = stem . s1 . s2 with one symbol per feature, against
      fusional, form = stem . s with one symbol per cell -- grow
      different substrates, so the paradigm is visible through the
      code, or the same one, so the code is the only knob?

WHOSE VOCABULARY. Q1 in the reader corpus's (policy, class, rank,
committed cell, the route bits, the patience axis, the drawdown axis).
Q2 in reduced binary quadratic forms' (a reduced definite form (a, b,
c), its leading coefficient the class's minimum, the principal class
the form with a = 1, a square being a class whose order divides h/2).
Q3 in grammar's (stem, suffix, feature, cell, paradigm) mapped by the
arena's stated place-value encoding, stem high-order.

TRANSPLANTS, MARKED.
  Q1 imports "floor" from the patience axis, where the floor lemma was
     proved; a route bit and the drawdown axis are different grades,
     and a bit has no interior at all.
  Q2 imports "graded by size" from the least prime's seat, one class
     per field chosen by an outside event; here every class is counted
     and no prime chooses.
  Q3 imports the single-symbol suffix mechanism from finding 1: a
     cross-cell difference is congruent to a nonzero symbol difference
     mod B, so B's own prime factors resolve it. A two-symbol suffix
     breaks that mechanism whenever two cells share their last symbol.

THE HAND ATTACK, before any engine code.

  Q1. A route bit takes two values, so a route flip lands at an end by
      arithmetic and cannot read the question; the print separates the
      classes cured ONLY by route flips (the kill unreadable on them)
      from those with a drawdown cure, and the drawdown cures are the
      cells the question is asked of. The axis ends are taken from the
      landscape's own drawdown axis (explore_move_set.py daxis_of:
      finite values ascending, then the spend-all sentinel), and the
      patience axis is SC.AX_BASE; no patience cure exists among the 30
      by construction (the reprint of 30 is the control). "Improving"
      is the corpus's own: the neighbour's class ranks strictly lower.

  Q2. The coin is not 1/2. In a cyclic group of even order h the
      squares number h/2, the principal class among them, so among the
      h - 1 NON-principal classes the non-square share is
      (h/2)/(h - 1); the null for a bin is the mean of that prior over
      the classes it holds, never the flat coin. Each class is one
      reduced form, and a class and its inverse (b against -b) share an
      order, so the classes in a bin come in correlated pairs: the
      standard error is computed on the number of inverse-pairs in the
      bin, not on the class count. Two gradings are printed, absolute
      a in fixed bins and a's rank among the field's non-principal
      minima, since a fixed a means a different thing at |D| = 200 and
      at 100000. The statistic can blow up only at an empty bin, which
      prints as such. Positive controls: 11,833 fields reprinted, every
      a = 1 class a square, the total non-square count equal to the sum
      of h/2 over the fields.

  Q3. The confound is code LENGTH: the agglutinative form carries a
      two-symbol suffix and the fusional a one-symbol one, so a
      difference between them may be the suffix width and not the
      paradigm. The third arm removes the ingredient: a fusional
      paradigm whose nine cells are coded by nine distinct TWO-symbol
      strings, the same width as the agglutinative code with the
      feature structure erased. Under base 30 the mechanism predicts
      the one-symbol fusional demand inside {2, 3, 5} and any
      two-symbol code -- agglutinative or fusional -- reaching 7
      whenever two cells share a last symbol (nine strings over thirty
      last symbols share one with probability about 0.7 per draw; the
      print names whether they did). The kill is read with the code
      held fixed. Control: the arena's own B = 30 feature stream still
      grows inside {2, 3, 5}.

KILLS, FROZEN AS PRINTS.
  Q1  KILLED if the count of the 30 classes with at least one curing
      move landing at an axis end is under 30; printed beside it, the
      count cured only by route flips (where the reading is arithmetic)
      and, over the drawdown-cured classes alone, how many land at an
      end. If no class has a drawdown cure the kill is undecidable on
      this arena and the verdict prints UNREADABLE.
  Q2  KILLED if every populated bin of the absolute grading with at
      least 30 inverse-pairs has its non-square share within two
      standard errors of its null AND the rank grading's first bin (the
      least non-principal minimum) is within two standard errors of
      its null. CARRIED if the share falls with a by more than two
      standard errors at both the smallest and the largest populated
      bin. Otherwise BETWEEN.
  Q3  KILLED if the agglutinative grown set differs from BOTH fusional
      arms' (paradigm visible with the code held fixed). SURVIVES,
      refrozen on the print, if agglutinative equals the two-symbol
      fusional arm and differs from the one-symbol one (the code
      decides). SURVIVES as written if all three coincide.

PREDICTIONS (fixed before the run).
  P1  At least 20 of the 30 are cured by a route flip alone; the
      drawdown-cured classes, if any, number under 10.
  P2  Flat: no absolute bin with 30 or more pairs departs its null by
      two standard errors; the rank-1 bin within two as well.
  P3  Agglutinative and two-symbol fusional both grow {2, 3, 5, 7}
      under base 30; one-symbol fusional grows inside {2, 3, 5}; the
      entry survives refrozen.

RUN. python prime/code/memwatch.py prime/code/explore_floor_grade_shape.py
(expected about three minutes, the class census the bulk of it, under
300 MB).

FINDINGS (entered after the run; 15 controls run, 0 failed; 3
predictions, 3 missed; wall 117.8 s, peak working set 205.5 MB under
memwatch's 512 MB default).

  F1. EVERY UNCURED STALL'S CURE LANDS AT AN END, AND THE SPEND-ALL END
      IS THE BEST DRAWDOWN CURE. Patience jumps alone reprint 30 stalled
      classes; each has a curing single-coordinate move and none of the
      cures is a patience move. All 30 have a cure landing at an axis
      end: 18 are cured only by route flips (a bit, so the reading is
      arithmetic there) and 12 have a drawdown cure, every one of them
      in a (B, W) = (2, 2) setting whose drawdown axis holds three
      values, 0, 1 and the spend-all sentinel. Of the 12, all 12 have a
      drawdown cure landing at an end, 4 have every drawdown cure at an
      end, and at all 12 an end-landing cure is among the lowest-ranked
      drawdown cures: at the eight classes that also cure mid-axis
      (d = 0 to d = 1) the mid-axis landing reaches the same rank as the
      spend-all end at the spike1@6 trap (0, 1, 2, 3 both ways) and a
      strictly worse one at the spike1@12 trap (2 against 0, 3 against
      1, 5 against 4, 7 against 6). P1 MISSED on the
      count (18 route-only, 12 drawdown-cured, against 20 and under
      10). Q1 SURVIVES its frozen kill: no class needs a mid-axis
      landing. The power is low, since a three-value axis has one
      interior point; the entry is refrozen on a wider drawdown axis.

  F2. THE GRADE IS GENUS, NOT SIZE, AND THE BIAS IS THE SMALLEST
      PRIMES. Over the 11,833 fields (reprinted; every a = 1 class a
      square; 591,376 non-squares, the sum of h/2) the non-square share
      is anything but flat and anything but a size curve: a = 2 reads
      0.636 and a = 3 reads 0.640 against nulls of 0.507 and 0.508 (22
      standard errors on the inverse-pair count), a = 4 reads 0.000
      over 9,019 classes, 5-6 reads 0.582, 7-10 reads 0.444, and the
      bins from 11 up sit within 0.02 of their nulls (0.525, 0.498,
      0.508, 0.509). By rank of a within the field: 0.620, 0.506,
      0.388, 0.543, 0.496, then 0.505 from rank 6 on. The pattern is
      multiplicative in a: the class with a = 4 is the square of the
      class of norm 2 and is always a square; the class with a = p a
      split prime is a non-square exactly when its genus character at
      the +q prime discriminant of D is -1, at 9,023 of 9,023 classes
      with a = 2 over odd D and 9,375 of 9,375 with a = 3 over the D
      not divisible by 3 that carry a +q factor (the control), which
      is genus theory read on a
      class group of 2-rank 1, where the squares ARE the principal
      genus. The bias at a = 2 and a = 3 is where the smallest prime
      FACTORS OF D sit: the character at 2 is -1 on the factors 3 and 5
      mod 8 and +1 on 1 and 7 mod 8, residue classes whose least primes
      are 3 and 5 against 7 and 17; the character at 3 is -1 when the
      +q factor is 5 mod 12 and +1 when it is 1 mod 12, 5 against 13.
      Over the fields whose least prime factor of |D| exceeds 7 the
      a = 3 share falls from 0.824 to 0.493 while the a = 2 share falls
      from 0.781 to 0.604. P2 MISSED (not flat). Q2 KILLED on its own
      print read whole: the size of a grades nothing; a's factorization
      does, through the genus character, and the +0.060 residual of the
      least split prime over the reduction null is that character's
      finite-scale bias from the discriminant's smallest prime factors,
      decaying as the census leaves them behind (the 0.604 at a = 2
      says the decay is slower there and is the open number).

  F3. THE PARADIGM IS VISIBLE AT ONE BASE, AS A CODE. The arena's own
      B = 30 feature stream grows [2, 3, 5] (control); the three arms
      carry 10 lexemes and 9 cells each at every base. At B = 30 the
      agglutinative feature stream grows [2, 3, 7, 11] (six cell pairs
      share a last symbol, a difference divisible by 30 present, min
      cov 0), the one-symbol fusional grows [2, 3, 5] and the
      two-symbol fusional grows [2, 3, 5] too, its nine random codes
      sharing no last symbol by the draw; the lemma streams grow
      [2, 3, 7, 11], [2, 3, 5, 7, 11] and [2, 3, 5, 7, 11]. At B = 29
      all three arms grow [2, 3, 5, 7, 11]. At B = 35 the agglutinative
      arm grows [2, 3, 5, 11], the one-symbol fusional [2, 3, 5, 7] and
      the two-symbol fusional, one shared last symbol, [2, 3, 5, 7,
      11]. P3 MISSED (the third arm did not carry its ingredient at
      B = 30 and differs from the agglutinative arm where it does).
      Q3 KILLED as frozen: under one base the grown set differs
      between paradigms, and the third arm says the difference is not
      the code's width but its whole difference structure -- which
      cells share a symbol at which position -- so no table indexed by
      the radix reads the substrate, and a table indexed by the code's
      difference set is the hitting-set reduction restated.

RUN RECORD. Three runs. The first printed the frozen observables; the
second added the lowest-ranked-cure comparison at the drawdown-cured
classes after the first run's prints showed eight of them curing
mid-axis as well; the third added the genus-character control and the
least-prime split after the second run's a = 4 row read 0.000 and the
a = 2 and a = 3 rows read alike. No verdict changed between runs; the
tables reprinted to the digit.
"""

import os                                                # noqa: E402
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math                                              # noqa: E402
import random                                            # noqa: E402
import sys                                               # noqa: E402
import time                                              # noqa: E402
from collections import defaultdict                      # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_class_order as CO                         # noqa: E402
import explore_principal_share as PS                     # noqa: E402
import explore_four_prints as FP                         # noqa: E402
import explore_move_set as MS                            # noqa: E402
import explore_scale_clock as SC                         # noqa: E402
import explore_grammar_growth as GG                      # noqa: E402
from explore_collision_growth import grow_least_new, diffs_of  # noqa: E402

CHECKS = [0, 0]
PREDS = [0, 0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        CHECKS[1] += 1
    print("  [%s] %s" % ("ok" if cond else "FAIL", msg))


def pred(cond, msg):
    PREDS[0] += 1
    if not cond:
        PREDS[1] += 1
    print("  [P %s] %s" % ("held" if cond else "MISSED", msg))


def section(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


# ------------------------------------------------------------ Q1
def move_kind(p, q, axis, daxis):
    """Which coordinate q changed from p, and whether the landing value
    is an end of that coordinate's axis."""
    st, ss, pt, pc, d = p
    if q[0] != st:
        return "route", True
    if q[1] != ss:
        return "route", True
    if q[2] != pt:
        return "patience", axis.index(q[2]) in (0, len(axis) - 1)
    if q[3] != pc:
        return "patience", axis.index(q[3]) in (0, len(axis) - 1)
    return "drawdown", daxis.index(q[4]) in (0, len(daxis) - 1)


def q1():
    section("Q1  THE FLOOR LANDING -- where the 30 uncured stalls' cures land")
    t0 = time.time()
    lands = MS.collect()
    print("  %d landscapes rebuilt (%.1fs)" % (len(lands), time.time() - t0))
    n_pat = 0
    rows = []
    for (fam, name, world, setting, space, sig_of, mem, qranks,
         daxis, stalls, _f) in lands:
        e_pat = MS.edges(space, sig_of,
                         lambda q: MS._patience_jumps(q, SC.AX_BASE,
                                                      len(SC.AX_BASE)))
        s_pat = MS.stalls_of(e_pat, qranks)
        n_pat += len(s_pat)
        for s in sorted(s_pat, key=lambda x: qranks[x]):
            kinds = defaultdict(lambda: [0, 0])   # kind -> [cures, at end]
            best = {}                             # drawdown: rank reached
            for p in mem[s]:
                for q in FP.nb_full(p, SC.AX_BASE, daxis):
                    t = sig_of.get(q)
                    if t is None or qranks[t] >= qranks[s]:
                        continue
                    kind, at_end = move_kind(p, q, SC.AX_BASE, daxis)
                    kinds[kind][0] += 1
                    kinds[kind][1] += at_end
                    if kind == "drawdown":
                        for key in (("all",) + (("end",) if at_end else ())):
                            best[key] = min(best.get(key, qranks[t]), qranks[t])
            rows.append((name, setting, qranks[s], len(mem[s]), dict(kinds),
                         best, len(daxis)))
    ok(n_pat == 30, "C1 patience jumps alone reprint 30 stalled classes")
    ok(all(r[4] for r in rows), "C1 every one of the 30 has a curing "
       "single-coordinate move (F4's zero under the full clique)")
    ok(not any("patience" in r[4] for r in rows),
       "C1 no curing move of the 30 is a patience move")
    any_end = only_route = draw_cured = draw_end = draw_all_end = 0
    best_is_end = 0
    for name, setting, r, m, kinds, best, nd in rows:
        ends = sum(v[1] for v in kinds.values())
        any_end += ends > 0
        only_route += set(kinds) == {"route"}
        if "drawdown" in kinds:
            draw_cured += 1
            c, e = kinds["drawdown"]
            draw_end += e > 0
            draw_all_end += e == c
            best_is_end += "end" in best and best["end"] == best["all"]
        desc = ", ".join("%s %d/%d at an end" % (k, v[1], v[0])
                         for k, v in sorted(kinds.items()))
        if best:
            desc += "; best drawdown cure rank %d, best end-landing %s" \
                % (best["all"], best.get("end", "none"))
        print("    %-24s %-8s rank %3d, %3d members, drawdown axis %d "
              "values: %s" % (name, setting, r, m, nd, desc))
    print("  over the 30: %d with a curing move landing at an axis end; "
          "%d cured only by route flips; %d with a drawdown cure, of "
          "which %d have a drawdown cure landing at an end, %d have "
          "every drawdown cure at an end, and %d have an end-landing "
          "cure among their lowest-ranked drawdown cures"
          % (any_end, only_route, draw_cured, draw_end, draw_all_end,
             best_is_end))
    pred(only_route >= 20 and draw_cured < 10,
         "P1 at least 20 cured by a route flip alone, under 10 drawdown-"
         "cured (%d, %d)" % (only_route, draw_cured))
    if draw_cured == 0:
        verdict = "UNREADABLE -- every cure is a bit flip"
    elif any_end < 30:
        verdict = "KILLED -- %d of 30 have no end-landing cure" % (30 - any_end)
    else:
        verdict = "SURVIVES -- every class has an end-landing cure"
    print("  Q1 verdict: %s" % verdict)
    return verdict, any_end, only_route, draw_cured, draw_end, draw_all_end


# ------------------------------------------------------------ Q2
ABINS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 6), (7, 10), (11, 20),
         (21, 50), (51, 100), (101, 10 ** 9)]


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def kronecker2(q):
    """(2/q) for odd q: +1 iff q = +-1 mod 8."""
    return 1 if q % 8 in (1, 7) else -1


def legendre3(q):
    """(q/3) for q not divisible by 3, which is (3/q) when q = 1 mod 4."""
    return 1 if q % 3 == 1 else -1


class Grade:
    def __init__(self):
        self.fields = 0
        self.nonsq_total = 0
        self.half_total = 0
        self.a1_nonsq = 0
        # bin -> [classes, nonsquares, null sum, pairs]
        self.abs = defaultdict(lambda: [0, 0, 0.0, 0])
        self.rank = defaultdict(lambda: [0, 0, 0.0, 0])
        # genus reading at a = 2 (D odd) and a = 3 (3 not dividing D):
        # [classes, agreeing with the character], and the non-square
        # share split by the least prime factor of |D|
        self.genus = {2: [0, 0], 3: [0, 0]}
        self.small = {2: defaultdict(lambda: [0, 0]),
                      3: defaultdict(lambda: [0, 0])}

    def add(self, D, h, orders, triv):
        self.fields += 1
        self.half_total += h // 2
        prior = (h / 2) / (h - 1)
        qs = prime_factors(abs(D))
        qstar = next((q for q in qs if q % 4 == 1), None)  # the +q factor
        nonp = []
        for k, o in orders.items():
            ns = not FP.is_square(o, h)
            self.nonsq_total += ns
            if k == triv:
                self.a1_nonsq += ns
                continue
            nonp.append((k, ns))
            a = k[0]
            if a in (2, 3) and D % a and qstar is not None:
                # the genus character of a at the prime discriminant q*
                chi = kronecker2(qstar) if a == 2 else legendre3(qstar)
                self.genus[a][0] += 1
                self.genus[a][1] += (ns == (chi == -1))
                cell = self.small[a]["least q <= 7" if min(qs) <= 7
                                     else "least q > 7"]
                cell[0] += 1
                cell[1] += ns
        # inverse pairs: (a, b, c) and (a, -b, c); self-inverse when b == 0,
        # b == a or a == c
        for k, ns in nonp:
            a, b, c = k
            selfinv = (b == 0 or b == a or a == c)
            first = selfinv or b > 0
            pairw = 1 if selfinv else 0.5
            for lo, hi in ABINS:
                if lo <= a <= hi:
                    cell = self.abs[(lo, hi)]
                    break
            cell[0] += 1
            cell[1] += ns
            cell[2] += prior
            cell[3] += pairw
        mins = sorted({k[0] for k, _ in nonp})
        rank_of = {m: i + 1 for i, m in enumerate(mins)}
        for k, ns in nonp:
            a, b, c = k
            selfinv = (b == 0 or b == a or a == c)
            r = min(rank_of[a], 6)
            cell = self.rank[r]
            cell[0] += 1
            cell[1] += ns
            cell[2] += prior
            cell[3] += 1 if selfinv else 0.5


def grade_census(lo, hi, plist, g):
    gen = PS.fundamental_discriminants

    def banded(a, b, s):
        for D in gen(1, b, s):
            if abs(D) > lo:
                yield D
    old_gen, old_b = CO.fundamental_discriminants, CO.DBOUND
    CO.fundamental_discriminants = banded
    CO.DBOUND = hi
    try:
        rows, _bad, _ib, _c2, _c4, _lb = CO.sweep(-1, plist)
    finally:
        CO.fundamental_discriminants = old_gen
        CO.DBOUND = old_b
    for D, hplus, recs, orders, _n0, _t0, _q, hits in rows:
        h = hplus
        if h % 2 or h < 2 or max(orders.values()) != h:
            continue
        triv = next(k for k, rec in recs.items() if rec[0])
        g.add(D, h, orders, triv)
    del rows


def read_grade(table, label, minpairs):
    print("  %s" % label)
    print("    %-12s %7s %7s %7s %7s %7s  %s"
          % ("bin", "classes", "pairs", "share", "null", "se", "z"))
    out = {}
    for key in sorted(table):
        n, ns, nullsum, pairs = table[key]
        if n == 0:
            continue
        share = ns / n
        null = nullsum / n
        se = math.sqrt(null * (1 - null) / pairs) if pairs > 0 else float("inf")
        z = (share - null) / se if se > 0 else 0.0
        name = ("%d" % key[0] if key[0] == key[1] else "%d-%d" % key) \
            if isinstance(key, tuple) else ("rank %d%s" % (key, "+" if key == 6 else ""))
        flag = "" if pairs >= minpairs else "  (under %d pairs)" % minpairs
        print("    %-12s %7d %7.0f %7.3f %7.3f %7.3f %+6.1f%s"
              % (name, n, pairs, share, null, se, z, flag))
        out[key] = (n, pairs, share, null, se, z)
    return out


def q2():
    section("Q2  THE LEADING-COEFFICIENT GRADE -- every class of 11,833 "
            "fields, binned by its reduced form's a")
    plist = PS.primes_upto(CO.PCAP)
    g = Grade()
    t0 = time.time()
    for lo in range(0, 100000, 4000):
        grade_census(lo, lo + 4000, plist, g)
        if lo % 20000 == 16000:
            print("  bands to %d done, %d fields (%.1fs)"
                  % (lo + 4000, g.fields, time.time() - t0))
    ok(g.fields == 11833, "C2 reprint of 11,833 fields (%d)" % g.fields)
    ok(g.a1_nonsq == 0, "C2 every a = 1 class is a square")
    ok(g.nonsq_total == g.half_total,
       "C2 non-squares total the sum of h/2 (%d against %d)"
       % (g.nonsq_total, g.half_total))
    for a in (2, 3):
        n, agree = g.genus[a]
        ok(n > 0 and agree == n, "C2 the a = %d class is a non-square exactly "
           "when its genus character at the +q prime discriminant is -1 "
           "(%d of %d)" % (a, agree, n))
        for key, (c, ns) in sorted(g.small[a].items()):
            print("    a = %d, %s: %d classes, non-square share %.3f"
                  % (a, key, c, ns / c if c else float("nan")))
    A = read_grade(g.abs, "absolute grading (a = 1 is the principal class)", 30)
    R = read_grade(g.rank, "rank grading (a's rank among the field's "
                   "non-principal minima)", 30)
    pop = [(k, v) for k, v in A.items() if k[0] >= 2 and v[1] >= 30]
    flat_abs = all(abs(v[5]) < 2 for _k, v in pop)
    r1 = R.get(1)
    flat_r1 = r1 is not None and abs(r1[5]) < 2
    small, large = pop[0][1], pop[-1][1]
    falling = small[5] > 2 and large[5] < -2
    worst = max(pop, key=lambda kv: abs(kv[1][5]))
    print("  populated absolute bins (a >= 2, >= 30 pairs): %d; the widest "
          "departure at a = %s, z = %+.1f; rank-1 bin z = %+.1f"
          % (len(pop), "%d-%d" % worst[0] if worst[0][0] != worst[0][1]
             else "%d" % worst[0][0], worst[1][5], r1[5] if r1 else float("nan")))
    pred(flat_abs and flat_r1, "P2 flat: every populated bin and the "
         "rank-1 bin within two standard errors of its null")
    if flat_abs and flat_r1:
        verdict = "KILLED -- the share is flat in a"
    elif falling:
        verdict = "CARRIED -- the share falls with a at both ends"
    else:
        verdict = "BETWEEN"
    print("  Q2 verdict: %s" % verdict)
    return verdict, A, R


# ------------------------------------------------------------ Q3
def agglutinative_forms(rng, n_stems, v1, v2, B, len_stem=2):
    """form = stem . s1 . s2, one symbol per feature; cell = (s1, s2)."""
    stems = {tuple(GG.random_string(rng, len_stem, B)) for _ in range(n_stems)}
    s1 = rng.sample(range(B), v1)
    s2 = rng.sample(range(B), v2)
    forms = {}
    for i, st in enumerate(sorted(stems)):
        for a in s1:
            for b in s2:
                forms[(i, (a, b))] = GG.enc(list(st) + [a, b], B)
    return forms, len(stems)


def fusional_forms(rng, n_stems, n_cells, B, width, len_stem=2):
    """form = stem . s, s one code of `width` symbols per cell, the nine
    codes distinct; cell = the code."""
    stems = {tuple(GG.random_string(rng, len_stem, B)) for _ in range(n_stems)}
    codes = set()
    while len(codes) < n_cells:
        codes.add(tuple(GG.random_string(rng, width, B)))
    forms = {}
    for i, st in enumerate(sorted(stems)):
        for c in sorted(codes):
            forms[(i, c)] = GG.enc(list(st) + list(c), B)
    return forms, len(stems), sorted(codes)


def shared_last(codes):
    last = [c[-1] for c in codes]
    return len(last) - len(set(last))


def q3():
    section("Q3  THE PARADIGM SHAPE -- agglutinative against fusional under "
            "one base, the code width held fixed by a third arm")
    # control: the arena's own B = 30 feature stream
    rng = random.Random(11)
    fA, _ns, _nf = GG.concat_forms(rng, 10, 5, 30)
    SA = grow_least_new(diffs_of(GG.labeling_from(fA, lambda i, j: j)), GG.POOL5)
    ok(set(SA) <= {2, 3, 5}, "C3 the arena's B = 30 feature stream grows "
       "inside {2, 3, 5} (%s)" % SA)
    results = {}
    for B in (30, 29, 35):
        rng = random.Random(1146 + B)
        agg, n1 = agglutinative_forms(rng, 10, 3, 3, B)
        fus1, n2, codes1 = fusional_forms(rng, 10, 9, B, 1)
        fus2, n3, codes2 = fusional_forms(rng, 10, 9, B, 2)
        ok(n1 == n2 == n3, "C3 B=%d the three arms carry the same lexeme "
           "count (%d, %d, %d)" % (B, n1, n2, n3))
        ok(len({k[1] for k in agg}) == 9 == len(codes1) == len(codes2),
           "C3 B=%d nine cells in every arm" % B)
        grown = {}
        for name, forms in (("agglutinative", agg), ("fusional-1", fus1),
                            ("fusional-2", fus2)):
            D = GG.diffs_of_cells(forms, lambda k: k[1])
            Dl = GG.diffs_of_cells(forms, lambda k: k[0])
            grown[name] = (grow_least_new(D, GG.POOL5),
                           grow_least_new(Dl, GG.POOL5), GG.min_cov(D),
                           any(d % B == 0 for d in D))
        agg_last = 9 - len({k[1][1] for k in agg})
        print("  B=%2d  agglutinative: %d cell pairs share a last symbol; "
              "fusional-2: %d" % (B, agg_last, shared_last(codes2)))
        for name, (S, Sl, mc, mult) in grown.items():
            print("    %-14s feature grew %-16s lemma grew %-20s min cov %d  "
                  "a diff = 0 mod B: %s" % (name, S, Sl, mc, mult))
        results[B] = grown
    g = results[30]
    A, F1, F2 = (set(g[k][0]) for k in ("agglutinative", "fusional-1", "fusional-2"))
    pred(A == F2 == {2, 3, 5, 7} and F1 <= {2, 3, 5},
         "P3 at B = 30 agglutinative and fusional-2 grow {2, 3, 5, 7}, "
         "fusional-1 inside {2, 3, 5} (%s, %s, %s)"
         % (sorted(A), sorted(F1), sorted(F2)))
    if A != F1 and A != F2:
        verdict = "KILLED -- the paradigm is visible with the code held fixed"
    elif A == F2 and A != F1:
        verdict = "SURVIVES, refrozen -- the code width decides, not the paradigm"
    else:
        verdict = "SURVIVES -- all three arms coincide"
    print("  Q3 verdict at B = 30: %s" % verdict)
    for B in (29, 35):
        g = results[B]
        A, F1, F2 = (set(g[k][0]) for k in ("agglutinative", "fusional-1", "fusional-2"))
        print("  B=%d: agglutinative %s, fusional-1 %s, fusional-2 %s"
              % (B, sorted(A), sorted(F1), sorted(F2)))
    return verdict, results


def main():
    t0 = time.time()
    v1 = q1()
    v2 = q2()
    v3 = q3()
    section("SUMMARY")
    print("  Q1 %s\n  Q2 %s\n  Q3 %s" % (v1[0], v2[0], v3[0]))
    print("  controls %d run, %d failed; predictions %d, %d missed; "
          "wall %.1f s" % (CHECKS[0], CHECKS[1], PREDS[0], PREDS[1],
                            time.time() - t0))
    return 1 if CHECKS[1] else 0


if __name__ == "__main__":
    sys.exit(main())
