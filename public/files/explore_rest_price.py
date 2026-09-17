"""
explore_rest_price.py -- whether an atom's fate under the min-cost
covering optimum is a function of its own numbers plus the price the
REST of the cell charges for each deficit the atom can leave, at three
atoms and at four.

THE QUESTION. On the set-valued ruler (explore_ruler_abandon.py) a cell
of weighted atoms, each with an exact posterior row, must reach marginal
coverage T = 7/10 at least cost, a pair (atom, label) costing the atom's
weight w and covering w times the label's posterior. Whether every
optimum abandons an atom (FORCED-ABANDONED) or every optimum serves it
(FORCED-SERVED) is no function of the atom's own numbers and the
operative level (explore_ruler_dual.py: 67 of 444 such keys collide),
and 6 keys still collide when the tied block's weight multiset and the
deficit are added (explore_four_prints.py Q1). The question: is there a
finite per-atom key that decides the fate exactly at every arity, and
which ingredient of it does the work?

THE ARGUMENT, fixed before the run. For a fixed number s of labels at
an atom the top-s posteriors are cheapest, so an atom's options are
its prefixes s = 0..k, costing s*w and covering w*P_s, P_s the sum of
its s largest posteriors. Let g(c) be the least cost at which the other
atoms reach coverage at least c (0 at c <= 0, infinite if they cannot).
Every rule splits into the atom's part and the rest's, so the optimum
is OPT = min over s of [s*w + g(T - w*P_s)]. Every optimum abandons the
atom iff the s = 0 term is strictly below every s >= 1 term, and every
optimum serves it iff some s >= 1 term is strictly below the s = 0
term; a non-prefix optimum is matched by the prefix of its size. So
the REST-PRICE key, (w, the sorted row, g(T - w*P_s) for s = 0..k),
decides the forced fate at every arity: a property, and a key of k + 3
numbers. The auditor's reading it rules out is a key the rest's price
does not enter.

THE DESIGN. Integer arithmetic throughout: posteriors in twentieths
(the two menus of explore_ruler_abandon.py), weights in D-ths, coverage
in units of 1/(20D), cost in units of 1/D. Every size vector of a cell
is enumerated; the optimum set and each atom's forced fate are read
off it; g is read off the vectors that give the atom size 0.
  ARM 3: three atoms, both menus, every row triple, the 153 unequal
    weight vectors in twentieths (the sweep of explore_four_prints.py
    Q1, one key index across both menus).
  ARM 4: four atoms, both menus, every row quadruple, the 84 weight
    vectors in tenths with every part at least 1/10.
Four keys per forced atom, one index per arm:
  PARENT   (w, sorted row, level t*)
  INSTANCE PARENT + the tied block's weight multiset + the deficit
  REST     (w, sorted row, the integer rest price at the k+1 deficits)
  LP       (w, sorted row, the FRACTIONAL rest price at the same
            deficits: the rest's pairs bought greedily by posterior,
            the last one in part) -- the third arm, the integer
            price's lumpiness removed.
A key COLLIDES when it carries a forced-abandoned atom in one cell and a
forced-served atom in another.

PREDICTIONS, frozen before the engine was written.
  P1 REST collisions 0 at ARM 3 and at ARM 4 (the argument; a nonzero
     print is an engine or argument error, never a finding).
  P2 LP collisions > 0 at both arms: the fractional price is the
     threshold rule's own relaxation and misses the lumps.
  P3 INSTANCE collisions > 0 at ARM 4: the collisions of the instance
     key do not vanish with a fourth atom.
  P4 (the direct form of P1) the fate computed from the REST key by the
     argmin formula equals the enumerated fate at every atom of both
     arms, the ambiguous atoms included.

CONTROLS. C1 parity: ARM 3's PARENT index reprints 444 keys with 67
collisions and its INSTANCE index 6 collisions (explore_ruler_dual.py,
explore_four_prints.py), so the integer engine is the Fraction engine.
C2 the level: the integer t* equals explore_ruler_barecell.py's
operative_level on the first 500 cells of ARM 3. C3 positive for the
collision counter: PARENT at ARM 4 collides (the counter can print a
nonzero count on this engine).

KILLS, as prints. The argument dies if P1 or P4 prints a nonzero
mismatch count. The ablation reading (that the integer price, not the
extra numbers, is what decides) dies if P2 prints 0 at both arms.

FINDINGS.
  F1 THE REST PRICE DECIDES THE FATE (property, by the decomposition
     above; checked exhaustively). REST collisions 0 at ARM 3 (6,022
     keys, 6,021 spanning two or more cells) and at ARM 4 (2,730 keys,
     all spanning two or more), and the argmin formula matches the
     enumerated fate at all 114,750 + 420,000 + 27,000 atoms, the
     22,016 + 1,222 + 828 ambiguous ones included. The key takes FEWER
     distinct values than the instance key at every arm (6,022 against
     16,232 at ARM 3; not checked to be a coarsening of it), so it does
     not decide by separating more cells.
  F2 THE LUMPS ARE THE INGREDIENT (observation). The same k + 1
     deficits priced FRACTIONALLY collide at 179 keys at ARM 3, 9 at
     ARM 4 and 10 at ARM 3 on tenths: the threshold rule's relaxation
     prices the rest linearly, and an atom's fate reads the rest's
     integer price; the distance from the level is one reading of a
     linear price, which this ablation shows cannot suffice alone.
  F3 THE INSTANCE KEY'S ZERO AT FOUR ATOMS IS THE GRID'S (observation).
     P3 missed: INSTANCE collisions 0 at ARM 4. The control added after
     the first run, ARM 3 with weights in tenths (C4), also prints 0
     (3,403 keys), against 6 at twentieths; the zero reads the coarser
     weight grid, not the fourth atom.
  Controls: C1 444 / 67 and 6 reprinted; C2 500/500; C3 PARENT 13
  collisions at ARM 4 and 19 at ARM 3 on tenths.

RUN RECORD. One run, 21.8 s wall, peak working set 202 MB (memwatch).
The reuse column and the C4 arm were added after the first run, which
printed every other number above unchanged.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import itertools                                     # noqa: E402
import sys                                           # noqa: E402
import time                                          # noqa: E402
from fractions import Fraction                       # noqa: E402

import numpy as np                                   # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_abandon import (                  # noqa: E402
    MENU_A, MENU_B, ROWS, WEIGHTS, make_cell,
)
from explore_ruler_barecell import operative_level   # noqa: E402

F = Fraction
ALPHA = F(3, 10)
K = 3
FAILS = []


def ok(cond, msg):
    print("  [%s] %s" % ("ok" if cond else "FAIL", msg))
    if not cond:
        FAILS.append(msg)


def int_menu(menu):
    return [[int(v * 20) for v in row] for row in menu]


class Arm:
    """One arity's size-vector table and its four key indexes."""

    def __init__(self, M):
        self.M = M
        self.S = np.array(list(itertools.product(range(K + 1), repeat=M)),
                          dtype=np.int64)
        self.idx = {n: {} for n in ("parent", "instance", "rest", "lp")}
        self.cells = 0
        self.atoms = 0
        self.fate_mismatch = 0
        self.fates = {"ab": 0, "sv": 0, "amb": 0}

    def add(self, name, fate, key, cid):
        slot = self.idx[name].setdefault(key, (set(), set()))
        slot[0 if fate == "ab" else 1].add(cid)

    def collisions(self, name):
        coll = [k for k, s in self.idx[name].items() if s[0] and s[1]]
        return len(self.idx[name]), len(coll)

    def reuse(self, name):
        return sum(1 for s in self.idx[name].values()
                   if len(s[0] | s[1]) >= 2)


def level_and_instance(rows, w, target):
    vals = sorted({v for row in rows for v in row}, reverse=True)
    for t in vals:
        cov = sum(w[r] * sum(v for v in rows[r] if v >= t)
                  for r in range(len(rows)))
        if cov >= target:
            strict = sum(w[r] * sum(v for v in rows[r] if v > t)
                         for r in range(len(rows)))
            block = tuple(sorted(w[r] for r in range(len(rows))
                                 for v in rows[r] if v == t))
            return t, block, target - strict
    return None, None, None


def lp_price(rows, w, skip, need):
    """Least fractional cost for the atoms other than `skip` to cover
    `need` coverage units, buying pairs by posterior, the last in part;
    None if they cannot."""
    if need <= 0:
        return F(0)
    pairs = sorted(((v, w[q]) for q in range(len(rows)) if q != skip
                    for v in rows[q] if v > 0), reverse=True)
    cost = F(0)
    for v, wq in pairs:
        if wq * v >= need:
            return cost + F(need, v)
        cost += wq
        need -= wq * v
    return None


def run_cell(arm, rows, w, D, cid):
    M = arm.M
    target = 14 * D                          # 7/10 of 20*D
    tops = np.array([[sum(sorted(row, reverse=True)[:s])
                      for s in range(K + 1)] for row in rows],
                    dtype=np.int64)
    wv = np.array(w, dtype=np.int64)
    S = arm.S
    cov = (wv[None, :] * tops[np.arange(M)[None, :], S]).sum(axis=1)
    cost = (S * wv[None, :]).sum(axis=1)
    feas = cov >= target
    if not feas.any():
        return
    best = cost[feas].min()
    opt = feas & (cost == best)
    arm.cells += 1
    t, block, deficit = level_and_instance(rows, w, target)
    for r in range(M):
        sr = S[opt, r]
        if (sr == 0).all():
            fate = "ab"
        elif (sr > 0).all():
            fate = "sv"
        else:
            fate = "amb"
        arm.atoms += 1
        arm.fates[fate] += 1
        zero = S[:, r] == 0
        rc, rk = cov[zero], cost[zero]
        prices = []
        for s in range(K + 1):
            need = target - w[r] * int(tops[r, s])
            if need <= 0:
                prices.append(0)
            else:
                m = rc >= need
                prices.append(int(rk[m].min()) if m.any() else None)
        terms = [None if p is None else s * w[r] + p
                 for s, p in enumerate(prices)]
        t0 = terms[0]
        rest_min = min((x for x in terms[1:] if x is not None),
                       default=None)
        if rest_min is None or (t0 is not None and t0 < rest_min):
            pred = "ab"
        elif t0 is None or rest_min < t0:
            pred = "sv"
        else:
            pred = "amb"
        arm.fate_mismatch += pred != fate
        if fate == "amb":
            continue
        row = tuple(sorted(rows[r], reverse=True))
        parent = (w[r], row, t)
        arm.add("parent", fate, parent, cid)
        arm.add("instance", fate, parent + (block, deficit), cid)
        arm.add("rest", fate, (w[r], row, tuple(prices)), cid)
        lps = tuple(lp_price(rows, w, r, target - w[r] * int(tops[r, s]))
                    for s in range(K + 1))
        arm.add("lp", fate, (w[r], row, lps), cid)


def sweep3(D=20):
    arm = Arm(3)
    if D == 20:
        wlist = [tuple(int(x * 20) for x in wts) for wts in WEIGHTS]
    else:
        wlist = [(a, b, D - a - b) for a in range(1, D)
                 for b in range(1, D) if D - a - b >= 1]
    for tag, menu in (("A", MENU_A), ("B", MENU_B)):
        im = int_menu(menu)
        for rows_i in ROWS:
            rows = [im[i] for i in rows_i]
            for w in wlist:
                run_cell(arm, rows, list(w), D, (tag, rows_i, w))
    return arm


def sweep4():
    arm = Arm(4)
    wlist = [(a, b, c, 10 - a - b - c)
             for a in range(1, 10) for b in range(1, 10)
             for c in range(1, 10) if 10 - a - b - c >= 1]
    rows4 = list(itertools.product(range(5), repeat=4))
    for tag, menu in (("A", MENU_A), ("B", MENU_B)):
        im = int_menu(menu)
        for rows_i in rows4:
            rows = [im[i] for i in rows_i]
            for w in wlist:
                run_cell(arm, rows, list(w), 10, (tag, rows_i, w))
    return arm, len(wlist)


def control_level(n=500):
    agree = total = 0
    im = int_menu(MENU_A)
    for rows_i in ROWS:
        for wts in WEIGHTS:
            if total >= n:
                return agree, total
            cell = make_cell(MENU_A, "C2", rows_i, wts)
            lvl = operative_level(cell, ALPHA)[0]
            rows = [im[i] for i in rows_i]
            w = [int(x * 20) for x in wts]
            t, _b, _d = level_and_instance(rows, w, 280)
            agree += F(t, 20) == lvl
            total += 1
    return agree, total


def report(arm, label):
    print("  %s: %d cells, %d atoms (forced-abandoned %d, forced-served "
          "%d, ambiguous %d)" % (label, arm.cells, arm.atoms,
                                  arm.fates["ab"], arm.fates["sv"],
                                  arm.fates["amb"]))
    out = {}
    for name in ("parent", "instance", "rest", "lp"):
        n, c = arm.collisions(name)
        out[name] = (n, c)
        print("    %-8s key: %6d distinct, %4d colliding, %6d spanning "
              "two or more cells" % (name, n, c, arm.reuse(name)))
    print("    argmin formula against the enumerated fate: %d mismatches"
          % arm.fate_mismatch)
    return out


def main():
    print("THE REST PRICE -- does what the rest charges decide the atom?")
    t0 = time.time()
    agree, total = control_level()
    print("C2 level parity: %d/%d" % (agree, total))
    ok(agree == total, "C2 integer t* equals operative_level")

    a3 = sweep3()
    o3 = report(a3, "ARM 3")
    print("  (%.1fs)" % (time.time() - t0))
    ok(o3["parent"] == (444, 67), "C1 PARENT reprints 444 / 67")
    ok(o3["instance"][1] == 6, "C1 INSTANCE reprints 6 collisions")

    a4, nw = sweep4()
    print("  ARM 4 weight vectors: %d" % nw)
    o4 = report(a4, "ARM 4")
    print("  (%.1fs)" % (time.time() - t0))
    ok(o4["parent"][1] > 0, "C3 the counter prints a nonzero PARENT count")

    a3t = sweep3(10)
    print("  C4 (added after the first run): ARM 3 on ARM 4's grid, "
          "weights in tenths")
    o3t = report(a3t, "ARM 3 tenths")

    ok(o3["rest"][1] == 0 and o4["rest"][1] == 0, "P1 REST collisions 0")
    ok(a3.fate_mismatch == 0 and a4.fate_mismatch == 0,
       "P4 argmin formula equals enumerated fate")
    print("  P2 LP collisions: ARM 3 %d, ARM 4 %d (predicted > 0)"
          % (o3["lp"][1], o4["lp"][1]))
    print("  P3 INSTANCE collisions at ARM 4: %d (predicted > 0)"
          % o4["instance"][1])
    print("FAILS: %d" % len(FAILS))
    for f in FAILS:
        print("  " + f)


if __name__ == "__main__":
    main()
