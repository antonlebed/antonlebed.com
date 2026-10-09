"""fates.py -- which atoms the marginal optimum hands the empty set:
the abandonment condition at equal masses, its failure in both
directions off them, the death of every predicate on one atom's own
numbers, and the finite key that decides an atom's fate exactly.

QUESTION. A set rule minimizing expected set size under marginal
coverage T = 1 - alpha can give a whole atom the EMPTY SET, and an
auditor asking whether a subpopulation is served wants a test run on
that subpopulation alone. The certificate of sets.py serves every atom
carrying a label above the operative level t* and abandons every atom
whose whole row sits below it. When is that the optimum's own verdict,
what decides an atom when it is not, and how much of the rest of the
cell does the deciding need?

THE OBJECTS (sets.py's: cells, pairs, t*, the certificate, the
enumeration of size vectors). An atom's FATE is FORCED-ABANDONED if
every optimum gives it size 0, FORCED-SERVED if every optimum gives it
size at least 1, and OPEN otherwise. The ABANDONMENT CONDITION: no atom
with max p > t* is forced-abandoned and no atom with max p < t* is
forced-served. With P_s the sum of an atom's s largest posteriors and
Lambda(v) the least cost at which the OTHER atoms cover at least v (0 at
v <= 0, infinite when they cannot), the atom's REST KEY is
(w, its sorted row, Lambda(T - w P_s) for s = 0..k).

THE ARGUMENT (written before the engine).
  (A) EQUAL MASSES (property). The certificate is an optimum there
      (sets.py) and gives size 0 to exactly the atoms below t*, size
      at least 1 to every atom above it: so no above-level atom is
      forced-abandoned and no below-level atom forced-served. The
      condition holds; nothing says every optimum agrees with the
      certificate, and where the surplus covers a swap another optimum
      trades an above-level pair for a tied one.
  (B) THE OUTNUMBERED ATOM. Eight atoms of mass 1/8, seven peaked at
      0.86, 0.85, ..., 0.80 and one at (0.40, 0.32, 0.28): the seven
      tops cover 5.81/8 = 0.72625 >= 0.70 and the tops down to 0.81
      cover 5.01/8 < 0.70, so t* = 4/5 with b = 1. Seven labels are
      the fewest reaching the bar (the seven largest posteriors of the
      cell are those tops), and dropping any top for any other label
      falls below it, so the optimum is unique: seven singletons and
      the empty set at the eighth, OPT = 7/8. The abandoned atom is
      not light, rare or adversarial; it is outnumbered. Split
      conformal thresholds an estimate of the same posterior, so its
      worst atom is predicted to read 0, as the optimum's eighth does.
  (C) OFF EQUAL MASSES (property, by two exhibited cells).
      ABOVE: w = (1/10, 9/20, 9/20), rows (1, 0, 0), (1, 0, 0),
      (4/5, 1/5, 0), T = 7/10. t* = 4/5; a cost 9/10 needs sizes with
      s_0/10 + 9(s_1 + s_2)/20 = 9/10, so s_0 = 0 and s_1 + s_2 = 2,
      and only (0, 1, 1) covers (0.81); every cheaper vector covers
      less than 0.70. The atom at p = 1 > t* is forced-abandoned.
      BELOW: w = (17/20, 1/10, 1/20), rows (4/5, 1/5, 0),
      (4/5, 1/5, 0), (3/5, 2/5, 0). Level 4/5 covers 0.76, so t* = 4/5
      and the third atom sits wholly below it. (1, 0, 1) costs 9/10 and
      covers 0.68 + 0.03 = 0.71; the certificate (1, 1, 0) costs 19/20;
      no other vector reaches the bar at 9/10 or less. The below-level
      atom is forced-served.
  (D) NO PREDICATE ON ONE ATOM (property, by an exhibited pair). A
      predicate reading an atom's own mass, its row and the level is a
      function of the key (w, sorted row, t*); two cells sharing that
      key with opposite forced fates kill every such predicate at
      once. Min-cost covering is not pointwise once purchases are lumpy.
  (E) THE REST PRICE DECIDES (property). A rule of size s at an atom
      is no better than its top-s prefix, and the rest of the cell is
      bought independently, so
          OPT = min_s [ s w + Lambda(T - w P_s) ].
      The atom is forced-abandoned iff the s = 0 term is strictly
      below every s >= 1 term, forced-served iff some s >= 1 term is
      strictly below the s = 0 term, and open on a tie. So the rest
      key, k + 3 numbers, decides the fate exactly. The THIRD ARM is
      the same key with R replaced by the rest's FRACTIONAL price (its
      pairs bought greedily by posterior, the last one in part): if
      that key never collides, the lumps do no work.

DESIGN. sets.py's sweep (its equal-weight and unequal-weight cells)
plus a four-atom unequal arm: weights on the tenths, each part at
least 1/10, rows on the tenths, 1,500 cells from a fixed seed. Every
size vector of a cell is enumerated and every optimum kept; each
atom's fate is read off them; R is read off the vectors of the other
atoms. Split and Mondrian conformal run on the eight-atom cell as in
sets.py (n in {2000, 8000, 32000}, 20 trials).

PREDICTIONS (fixed before the engine; figures carried from an earlier
record are TRANSPLANTS until re-measured).
  K1 CONTROL: at the eight-atom cell, sets.py's solver equals the
     enumeration.
  K2 CONTROL: the fate counter reads a forced-abandoned and a
     forced-served atom somewhere in the sweep (it can print both).
  P1 (A) the condition holds at every atom of every equal-weight cell;
     the counts of atoms whose fate some optimum reverses are printed.
  P2 (B) t* = 4/5, b = 1, OPT = 7/8, one optimum, the eighth atom
     empty; split conformal's worst atom at exact coverage 0 in every
     trial at every n (TRANSPLANT) with mean marginal coverage at least
     0.70; Mondrian's worst atom at least 0.6 on average at n = 32000.
  P3 (C) both witnesses as derived: one optimum each, the named atom
     forced-abandoned (ABOVE) and forced-served (BELOW).
  P4 (D) some key (w, sorted row, t*) carries a forced-abandoned atom
     in one cell and a forced-served one in another (TRANSPLANT).
  P5 (E) the fate read off the rest key by the formula equals the
     enumerated fate at every atom of every cell.
  P6 the fractional key collides: some (w, sorted row, fractional
     prices) carries both forced fates (TRANSPLANT).

KILL. K1 or K2 off: nothing is read. P1, P3 or P5 off: an argument
above is wrong. P6 off: the fractional price decides, and the claim
that the lumps do the work dies.
[Read later, on a code read: P5 reads one enumeration table two ways,
the prefix step built into it, so it cannot fail; it is printed as a
record, not checked. The proof carries (E).]

FINDINGS. No kill fired. One frozen clause miscounted: (E)'s rest key
is 2k + 2 numbers (mass, row, k + 1 prices), not k + 3; the k + 1
sums s w + Lambda(T - w P_s) alone decide the fate.
  controls  the solver equals the enumeration at the eight-atom cell;
            all three fates occur in the sweep.
  equal     the condition holds at every atom of the 400 equal-weight
            cells. Some optimum abandons 28 above-level atoms and
            serves no below-level one; none is forced. By hand, at
            w = 1/4, rows (3/5, 3/10, 1/10), (1/2, 2/5, 1/10), (1, 0, 0),
            (3/5, 3/10, 1/10), t* = 2/5, surplus 3/40: the optimum
            (0, 2, 1, 2), one of six optima at the certificate's cost
            5/4, drops the first atom's 3/5 and buys the fourth's 3/10,
            below the level, covering exactly 7/10.
  straddle  t* 4/5, b 1, OPT 7/8, the one optimum (1, ..., 1, 0).
            Split: marginal 0.7262 and its worst atom, which one not
            printed, at coverage 0 in 20 of 20 trials at every n. Mondrian's worst atom 0.7660,
            0.7500, 0.7200.
  witnesses ABOVE: CERT 1, OPT 9/10, one optimum (0, 1, 1), the p = 1
            atom forced-abandoned. BELOW: CERT 19/20, OPT 9/10, one
            optimum (1, 0, 1), the atom peaking at 3/5 < t* = 4/5
            forced-served.
  dead      276 of the 1,255 keys (w, sorted row, t*) carrying a forced
            fate carry both forced fates, 206 with the atom strictly off
            the level. The atom
            w = 1/10, row (1, 0, 0), t* = 1/2: in w = (11/20, 7/20,
            1/10), rows (7/10, 3/10, 0), (1/2, 1/2, 0), (1, 0, 0), the
            one optimum (1, 2, 0) costs 5/4 and abandons it; in
            w = (3/5, 3/10, 1/10), rows (1/2, 1/2, 0), (1/2, 2/5, 1/10),
            (1, 0, 0), the one optimum (2, 0, 1) costs 13/10 and serves
            it, every rule without it costing at least 3/2.
  rest      the formula equals the enumerated fate at all 16,300 atoms;
            the fractional key collides at 115 of the 12,190 keys that
            forced fates carry.

RUN RECORD. python fates.py: run 1, 9 of 9, 2.0 s, peak commit 48.5
MB; the strict-pair print added after it, the gated counts unchanged.
After a code read, 8 of 8, 2.1 s, peak commit 49.1 MB: the witnesses'
optima cover 81/100 and 71/100, the dead pair's optima cost 5/4 and
13/10, and every rule without the served atom at least 3/2.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
import sys
import time
from fractions import Fraction as F
from itertools import product

from sets import (Anatomy, Cell, NS, SEED, TRIALS, conformal, score,
                  solve, sweep)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail
                                                     else ""))


def section(title):
    print()
    print(title)
    print("-" * len(title))


def row(*xs):
    return [F(x, 100) for x in xs]


STRADDLE = Cell("STRADDLE", [F(1, 8)] * 8,
                [row(86, 9, 5), row(85, 11, 4), row(84, 13, 3),
                 row(83, 15, 2), row(82, 17, 1), row(81, 12, 7),
                 row(80, 14, 6), row(40, 32, 28)])
ABOVE = Cell("ABOVE", [F(1, 10), F(9, 20), F(9, 20)],
             [[F(1), F(0), F(0)], [F(1), F(0), F(0)],
              [F(4, 5), F(1, 5), F(0)]])
BELOW = Cell("BELOW", [F(17, 20), F(1, 10), F(1, 20)],
             [[F(4, 5), F(1, 5), F(0)], [F(4, 5), F(1, 5), F(0)],
              [F(3, 5), F(2, 5), F(0)]])


def four_arm():
    rng = random.Random(SEED + 4)
    tenths = [tuple(F(x, 10) for x in (a, b, 10 - a - b))
              for a in range(11) for b in range(11 - a)
              if a >= b >= 10 - a - b]
    comps = [c for c in product(range(1, 8), repeat=4) if sum(c) == 10]
    cells = []
    for i in range(1500):
        ws = rng.choice(comps)
        cells.append(Cell(f"Q{i}", [F(x, 10) for x in ws],
                          [rng.choice(tenths) for _ in range(4)]))
    return cells


class Fates:
    """Every optimum of a cell by enumeration, each atom's fate, and
    each atom's rest key, integer and fractional."""

    def __init__(self, cell):
        self.cell = cell
        an = self.an = Anatomy(cell)
        sc, M, k = an.sc, cell.M, cell.k
        best, opts = None, []
        table = {}
        for sz in product(range(k + 1), repeat=M):
            cov = sum(sc.V[r][sz[r]] for r in range(M))
            cost = sum(sc.W[r] * sz[r] for r in range(M))
            table[sz] = (cost, cov)
            if cov >= sc.TQ:
                if best is None or cost < best:
                    best, opts = cost, [sz]
                elif cost == best:
                    opts.append(sz)
        self.opt, self.opts = best, opts
        self.fate = []
        for r in range(M):
            zero = [o[r] == 0 for o in opts]
            self.fate.append("A" if all(zero) else
                             "S" if not any(zero) else "O")
        self.rest, self.lp = [], []
        for r in range(M):
            prices, fracs = [], []
            for s in range(k + 1):
                need = sc.TQ - sc.V[r][s]
                cands = [c - sc.W[r] * sz[r] for sz, (c, v) in table.items()
                         if sz[r] == 0 and v >= need]
                prices.append(min(cands) if cands else None)
                fracs.append(self.fractional(r, need))
            self.rest.append(prices)
            self.lp.append(fracs)

    def fractional(self, r, need):
        if need <= 0:
            return F(0)
        sc, cell = self.an.sc, self.cell
        pairs = sorted(((cell.srt[q][i], q) for q in range(cell.M)
                        if q != r for i in range(cell.k)), reverse=True)
        cost = F(0)
        for p, q in pairs:
            if p == 0:
                break
            cov = sc.W[q] * p
            if cov >= need:
                return cost + F(need) / p
            cost += sc.W[q]
            need -= cov
        return None

    def predicted(self, r):
        sc = self.an.sc
        terms = [None if R is None else s * sc.W[r] + R
                 for s, R in enumerate(self.rest[r])]
        served = [x for x in terms[1:] if x is not None]
        z = terms[0]
        if z is not None and (not served or z < min(served)):
            return "A"
        if served and (z is None or min(served) < z):
            return "S"
        return "O"

    def key(self, r):
        c = self.cell
        return (c.w[r], tuple(c.srt[r]), self.an.t)

    def value(self, x):
        return F(x) / self.an.sc.Q


def section_controls(fates):
    section("CONTROLS")
    st = Fates(STRADDLE)
    check("K1 STRADDLE: sets.py's solver == enumeration",
          solve(st.an)[0] == st.opt)
    kinds = {f for x in fates for f in x.fate}
    check("K2 the counter reads both forced fates in the sweep",
          {"A", "S"} <= kinds, f"fates seen {sorted(kinds)}")
    return st


def section_equal(fates):
    section("EQUAL MASSES (A)")
    bad = above = below = 0
    for x in fates:
        if not x.cell.equal():
            continue
        for r in range(x.cell.M):
            mx = x.cell.srt[r][0]
            if mx > x.an.t:
                bad += x.fate[r] == "A"
                above += any(o[r] == 0 for o in x.opts)
            if mx < x.an.t:
                bad += x.fate[r] == "S"
                below += any(o[r] > 0 for o in x.opts)
    print(f"  some optimum abandons {above} above-level atoms and serves "
          f"{below} below-level ones; {bad} forced")
    check("P1 the condition holds at every atom of every equal-weight cell",
          bad == 0, f"{bad} violations")


def section_straddle(st):
    section("THE OUTNUMBERED ATOM (B)")
    an = st.an
    print(f"  t* {an.t}, m {an.m}, OPT {st.value(st.opt)}, optima "
          f"{st.opts}")
    ok = (an.t == F(4, 5) and an.m == 1 and st.value(st.opt) == F(7, 8)
          and st.opts == [(1,) * 7 + (0,)])
    zero = marg = True
    worst32 = 0.0
    for n in NS:
        rows = []
        for tr in range(TRIALS):
            rng = random.Random(SEED + 7000 + 10 * n + tr)
            split, mond, _ = conformal(STRADDLE, n, rng)
            rows.append(score(STRADDLE, split) + score(STRADDLE, mond))
        zs = sum(1 for x in rows if x[1] == 0)
        sm = sum(x[0] for x in rows) / TRIALS
        mw = sum(x[4] for x in rows) / TRIALS
        print(f"  n {n:6d}: split marginal {sm:.4f}, worst atom 0 in "
              f"{zs}/{TRIALS}; Mondrian worst atom {mw:.4f}")
        zero &= zs == TRIALS
        marg &= sm >= 0.70
        if n == NS[-1]:
            worst32 = mw
    check("P2 t* 4/5, m 1, OPT 7/8, the one optimum empties the eighth "
          "atom", ok)
    check("P2 split's worst atom 0 in every trial, marginal >= 0.70; "
          "Mondrian's worst >= 0.6 at n = 32000",
          zero and marg and worst32 >= 0.6)


def section_witnesses():
    section("OFF EQUAL MASSES (C)")
    a, b = Fates(ABOVE), Fates(BELOW)
    for x in (a, b):
        sc = x.an.sc
        print(f"  {x.cell.name}: t* {x.an.t}, CERT {x.value(x.an.cert)}, "
              f"OPT {x.value(x.opt)}, optima {x.opts}, covering "
              f"{[str(x.value(sum(sc.V[r][s] for r, s in enumerate(o)))) for o in x.opts]}, "
              f"fates {x.fate}")
    ok = (a.an.t == F(4, 5) and a.opts == [(0, 1, 1)] and a.fate[0] == "A"
          and a.cell.srt[0][0] > a.an.t)
    ok &= (b.an.t == F(4, 5) and b.opts == [(1, 0, 1)] and b.fate[2] == "S"
           and b.cell.srt[2][0] < b.an.t and b.value(b.an.cert)
           == F(19, 20))
    check("P3 ABOVE: an above-level atom forced-abandoned; BELOW: a "
          "below-level atom forced-served", ok)


def collisions(fates, keyf):
    seen = {}
    for x in fates:
        for r in range(x.cell.M):
            if x.fate[r] in "AS":
                seen.setdefault(keyf(x, r), {}).setdefault(x.fate[r],
                                                           (x, r))
    return {k: v for k, v in seen.items() if len(v) == 2}, len(seen)


def section_dead(fates):
    section("NO PREDICATE ON ONE ATOM (D)")
    hits, keys = collisions(fates, lambda x, r: x.key(r))
    print(f"  {len(hits)} of {keys} keys (w, sorted row, t*) carry both "
          f"forced fates")
    strict = {k: v for k, v in hits.items() if k[1][0] != k[2]}
    print(f"  {len(strict)} of them with the atom strictly above or below "
          f"the level (a print added after run 1)")
    if hits:
        pool = strict or hits
        k, v = min(pool.items(), key=lambda kv: (kv[1]["A"][0].cell.M,
                                                 kv[1]["S"][0].cell.M,
                                                 str(kv[0])))
        for f in "AS":
            x, r = v[f]
            print(f"   {f}: w {[str(y) for y in x.cell.w]}, rows "
                  f"{[[str(y) for y in s] for s in x.cell.srt]}, atom {r}, "
                  f"t* {x.an.t}, optima {x.opts}, OPT {x.value(x.opt)}, "
                  f"least cost without the atom {x.value(x.rest[r][0])}")
    check("P4 some key (w, sorted row, t*) carries both forced fates",
          len(hits) > 0)


def section_rest(fates):
    section("THE REST PRICE DECIDES (E)")
    bad = n = 0
    for x in fates:
        for r in range(x.cell.M):
            n += 1
            bad += x.predicted(r) != x.fate[r]
    print(f"  the rest key's formula gives the enumerated fate at {n} "
          f"atoms, {bad} off (one table read two ways: a record)")
    hits, keys = collisions(
        fates, lambda x, r: (x.cell.w[r], tuple(x.cell.srt[r]),
                             tuple(None if p is None else p / x.an.sc.Q
                                   for p in x.lp[r])))
    print(f"  fractional key: {len(hits)} of {keys} keys carry both "
          f"forced fates")
    if hits:
        v = next(iter(hits.values()))
        for f in "AS":
            x, r = v[f]
            print(f"   {f}: w {[str(y) for y in x.cell.w]}, rows "
                  f"{[[str(y) for y in s] for s in x.cell.srt]}, atom {r}, "
                  f"integer {[None if p is None else str(x.value(p)) for p in x.rest[r]]}")
    check("P6 the fractional key collides", len(hits) > 0)


def main():
    t0 = time.time()
    fates = [Fates(c) for c in sweep() + four_arm()]
    st = section_controls(fates)
    if not all(CHECKS):
        print("\nCONTROL FAILED: nothing below is read.")
        sys.exit(1)
    section_equal(fates)
    section_straddle(st)
    section_witnesses()
    section_dead(fates)
    section_rest(fates)
    print()
    print(f"{sum(CHECKS)} of {len(CHECKS)} checks, "
          f"{time.time() - t0:.1f} s")
    sys.exit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
