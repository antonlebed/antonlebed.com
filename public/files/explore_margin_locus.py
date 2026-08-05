"""Where the Lebesgue margin loses its digit, off the symmetric family.

THE QUESTION. Two locality laws lose exactly one digit at redundancy
index rho = 2 and nowhere else: the addition bound b^c * rho >= 4a and
the scaling bound's b-coprime branch, both measured over SYMMETRIC
digit sets {-a..a} (explore_redundant_lookback.py). What selects
rho = 2 is unidentified there: it is not thinness of the cover (rho = 1
is thinner and exact), and the radix-2 rows kill the excess-over-radix
guess. This run takes the family the symmetric sweep could not reach:
CONTIGUOUS ASYMMETRIC digit sets D = {-am..ap} at radix b, redundancy
index rho = am + ap + 1 - b, spread W = am + ap. Asymmetry decouples
the slack from the alphabet's shape, so whatever the one-digit loss
tracks either moves or it does not.

THE PARITY BLINDNESS, a property that frames the whole run: a
symmetric set has rho = 2a + 1 - b, so rho and b have opposite parity
-- odd radix sees only even rho, even radix only odd rho. The
symmetric sweep behind the rho = 2 statement saw exactly HALF the
(b, rho) grid, and every statement of the form "the locus is rho = 2"
was drawn on that half. The asymmetric family fills the other half:
radix 3 with rho = 3, even radix with rho = 2, neither of which any
symmetric set can realize.

THE MARGIN, generalized. The symmetric addition bound's 4a is the
spread of the injected sum set D + D, which is 2W; the scaling bound's
2a*m0 is the spread of m0*D, which is m0*W. So one form covers both:

    c_margin = smallest c with b^c * rho >= spread(S),

and the question is where that rounding parts from the measured game
value.

HAND-DERIVED before any engine code, by running the residual safety
game's fixed point on paper (win set the interval [-am*r_c, ap*r_c],
r_c the c-digit repunit; the index convention re-derived from
explore_redundant_lookback.py's engine: pre = b*R + s, emission
e * b^c):

    (3, {-1..3})  rho = 2: INFEASIBLE at c = 1 (the fixed point
                  empties), so rho = 2 SPLITS by shape.
    (3, {-2..3})  rho = 3: FEASIBLE at c = 1, where the margin says 2
                  -- a one-digit loss OFF rho = 2.
    (3, {-1..4})  rho = 3: feasible at c = 1, so the shape exception
                  does not extend up from rho = 2.
    (3, { 0..4})  rho = 2: feasible at c = 1, so the exception is
                  min = 1 exactly, not min <= 1.

THE DESIGN, frozen before the engine.

P-A The symmetric grid through the generalized code path reproduces
    the symmetric law exactly: c_min = 1 iff rho >= 2 and b >= 3,
    else 2, at all 58 systems with b <= 12, a <= 8, and the two
    anchor rows (2,1) -> 2, (10,6) -> 1 come back with the adder
    exact.

P-B Rho = 2 splits by shape: cells with min(am, ap) = 1 read at
    c = 2, all others (including min = 0) at c = 1. TRANSPLANT,
    marked: the min = 1 exception matches the hybrid-redundant
    paper's hedge over "a few cases of rho = 2" as secondary
    sources gloss the generalized-signed-digit framework; the
    framework itself is still unread and only the hand-run above
    is ours.

P-C The candidate exact law over the full asymmetric grid:

        c_min = 1  iff  rho >= 2 and b >= 3
                        and not (rho = 2 and min(am, ap) = 1),
        else c_min = 2.

P-D The margin's miss set is a WEDGE, not a rho value: it overpredicts
    by one exactly where the law grants c = 1 and b * rho < 2W, i.e.
    rho * (b - 2) < 2 * (b - 1). At b >= 4 that wedge is rho = 2
    alone; at b = 3 it includes rho = 3. So the locus MOVES: radix-3
    rho = 3 cells and even-radix rho = 2 cells join the miss set, and
    the rho = 2 min = 1 cells leave it (the margin says 2 there and
    is right).

P-E The margin never underpredicts: every miss is one digit HIGH.

P-F The scaling bound's misses on the same asymmetric cells also
    leave rho = 2: any wedge cell where the measured scaling c beats
    the margin by one at rho != 2 confirms the locus is the margin's,
    not the slack's.

KILLS, frozen as what this run PRINTS.

K1 Every printed overpredict cell has rho = 2 -> the locus closes as
   a law of rho after all and the wedge reading dies.
K2 An overpredict cell prints at rho != 2, or a rho = 2 cell prints
   exact where P-D says miss -> the locus is the margin's wedge (or
   whatever the grid actually shows), named from the printed table.
K3 A cell prints measured > margin -> the sufficiency reading itself
   breaks; reported separately from the locus question.
K4 An adder mismatch at a measured c -> harness bug, not a finding.

POSITIVE CONTROL, run and read before any verdict cell: the symmetric
anchors and grid of P-A, plus a mirror check (the game must be
invariant under (am, ap) -> (ap, am) with the digits negated).

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. Both anchors return their recorded values
   through the generalized path -- (2,1) at c_min = 2 with the adder
   exact on 6561 length-4 pairs, (10,6) at c_min = 1 on 28561
   length-2 pairs -- the symmetric law c_min = 1 iff rho >= 2 and
   b >= 3 comes back at all 58 symmetric systems, and the mirror
   check is silent at 52 cells. P-A holds and the asymmetric table
   is a real measurement.

F2 RHO = 2 SPLITS BY SHAPE [rule, exhaustive at the stated grid].
   Across the 214 contiguous systems swept (2 <= b <= 10,
   1 <= rho <= 5, am <= ap, spread <= 14, mirrors excluded), every
   rho = 2 cell with min(am, ap) = 1 reads at c_min = 2 -- the
   margin-exact list prints them at every radix 2..10 -- and every
   other rho = 2 cell at radix >= 3, min = 0 included, at c_min = 1
   (radix 2 reads 2 at every shape, (2,{0..3}) included). So the slack
   alone never was the selector: the symmetric family cannot build a
   min = 1 witness (its min is a, and rho = 2 forces a >= 2). P-B
   held, including the min = 0 clause the hand-run predicted.

F3 THE EXACT LAW EXTENDS [rule, exhaustive at the same grid; since
   PROVED as a criterion for every radix and every contiguous digit
   set in explore_lookahead_proof.py — this census survives as the
   check on that proof]:

       c_min = 1  iff  rho >= 2 and b >= 3
                       and not (rho = 2 and min(am, ap) = 1),
       else c_min = 2.

   214/214 cells, 160 at 1 and 54 at 2, no counterexample. The
   symmetric law is this one's restriction to am = ap, where the min
   clause is vacuous; the b >= 3 side condition survives asymmetry
   (every radix-2 cell reads 2 out to rho = 5). P-C held.

F4 THE LOCUS IS THE WEDGE, NOT THE SLACK, AND K2 FIRED [rule,
   exhaustive at the same grid]. The margin overpredicts at 31
   cells, always by exactly one digit, and is exact at 183; the miss
   set is EXACTLY the predicted wedge {law grants 1 and
   b * rho < 2W}, matched at 214/214 cells. The rho census of the
   misses: 28 at rho = 2, THREE AT RHO = 3 -- (3,{0..5}),
   (3,{-1..4}), (3,{-2..3}), all radix 3, the half of the grid the
   symmetric family's parity lock hides (rho = 2a + 1 - b ties rho's
   parity to b's, so odd radix sees only even rho). And rho = 2
   cells sit on BOTH sides: the min = 1 cells print margin-exact at
   every radix. Equivalently the wedge is rho * (b - 2) < 2 * (b - 1)
   intersected with the law's c = 1 region -- at b >= 4 that is
   rho = 2 alone, which is why a symmetric sweep could not tell "the
   wedge" from "rho = 2". P-D held cell-for-cell.

F5 THE MARGIN STAYS SUFFICIENT. No cell prints measured > margin
   (K3 never fired); the overprediction depth set is {1}. P-E held.

F6 THE SCALING BOUND WALKS THE SAME WEDGE [observation, scanned
   scope: m in {2, 3, 5} over eight cells]. Its misses land at the
   rho = 3 wedge cells (3,{-2..3}) and (3,{-1..4}) for m = 2,
   beside rho = 2 cells: the symmetric row already on record
   ((3,{-2..2}) at m = 2 and m = 5) and the asymmetric (4,{-2..3})
   and (5,{-2..4}) at m = 2 and (3,{-1..3}) at m = 5 -- the last a
   min = 1 cell, so addition's shape exception is addition's own and
   does not travel to scaling. Every miss is one digit high with the
   b-power branch exact throughout. The sibling bound's locus moves
   with addition's: one margin, two operations, one wedge. P-F held.

RUN RECORD: pure Python, integers only, standard library; largest
win set a few thousand residues, well under the analysis memory
ceiling; ~17s wall clock. Prints reproduced by:
python prime/code/explore_margin_locus.py
"""

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def digits(am, ap):
    return list(range(-am, ap + 1))


def repunit(b, c):
    return sum(b ** i for i in range(c))


def game_feasible(b, am, ap, c, S):
    return 0 in win_set(b, am, ap, c, S)


def transducer_run(b, am, ap, c, injected, win):
    """Emit inside the game's win set (any member choice is safe, the
    set being a fixed point), then flush c digits; None on a stuck
    state, which the caller treats as a harness bug."""
    R = 0
    out = []
    for s in injected:
        pre = b * R + s
        best = None
        for e in digits(am, ap):
            R2 = pre - e * b ** c
            if R2 in win and (best is None or abs(R2) < abs(best[1])):
                best = (e, R2)
        if best is None:
            return None
        out.append(best[0])
        R = best[1]
    for rem in range(c - 1, -1, -1):
        scale = b ** rem
        cands = [d for d in digits(am, ap)
                 if -am * repunit(b, rem) <= R - d * scale
                 <= ap * repunit(b, rem)]
        if not cands:
            return None
        e = min(cands, key=lambda d: abs(R - d * scale))
        out.append(e)
        R -= e * scale
    return out if R == 0 else None


def win_set(b, am, ap, c, S):
    """The greatest fixed point of the residual safety game with
    injected values S, emission granularity b^c, flushable residuals
    in [-am, ap] * repunit(b, c). The symmetric engine's game with the
    interval opened up; am = ap reproduces it exactly. Feasibility at
    lookahead c is 0 surviving in this set."""
    lo, hi = -am * repunit(b, c), ap * repunit(b, c)
    win = set(range(lo, hi + 1))
    changed = True
    while changed:
        changed = False
        for R in list(win):
            for s in S:
                pre = b * R + s
                if not any(pre - e * b ** c in win
                           for e in digits(am, ap)):
                    win.discard(R)
                    changed = True
                    break
    return win


def value(b, ds):
    v = 0
    for d in ds:
        v = v * b + d
    return v


def add_sums(am, ap):
    return sorted(set(x + y for x in digits(am, ap)
                      for y in digits(am, ap)))


def measured_cmin(b, am, ap, S=None, cap=3):
    if S is None:
        S = add_sums(am, ap)
    for c in range(cap + 1):
        if game_feasible(b, am, ap, c, S):
            return c
    return None


def margin_cmin(b, am, ap, spread, cap=6):
    """Smallest c with b^c * rho >= spread; the Lebesgue margin."""
    rho = am + ap + 1 - b
    for c in range(cap + 1):
        if b ** c * rho >= spread:
            return c
    return None


def law_cmin(b, am, ap):
    """The frozen candidate exact law (P-C)."""
    rho = am + ap + 1 - b
    if rho >= 2 and b >= 3 and not (rho == 2 and min(am, ap) == 1):
        return 1
    return 2


def adder_exact(b, am, ap, c, t, limit=30000):
    """Greedy adder against every (or a deterministic stride of)
    pair of length-t strings; None on any wrong sum."""
    S = add_sums(am, ap)
    win = win_set(b, am, ap, c, S)
    D = digits(am, ap)
    all_strings = [()]
    for _ in range(t):
        all_strings = [s + (d,) for s in all_strings for d in D]
    total = len(all_strings) ** 2
    stride = max(1, total // limit)
    n = 0
    i = 0
    for xs in all_strings:
        for ys in all_strings:
            i += 1
            if (i - 1) % stride:
                continue
            out = transducer_run(b, am, ap, c,
                                 [x + y for x, y in zip(xs, ys)], win)
            if out is None or value(b, out) != value(b, xs) + value(b, ys):
                return None
            n += 1
    return n


ANCHORS = [(2, 1, 2), (10, 6, 1)]


def s1_control():
    print("== S1 POSITIVE CONTROL ==")
    for (b, a, c_known) in ANCHORS:
        c = measured_cmin(b, a, a)
        ok(c == c_known,
           f"anchor ({b},{a}): game says c={c}, record says {c_known}")
        t = 4 if (2 * a + 1) ** 2 <= 25 else 2
        n = adder_exact(b, a, a, c_known, t)
        ok(n is not None, f"anchor ({b},{a}): adder wrong at c={c_known}")
        print(f"  symmetric ({b},{a}): c_min = {c}, record {c_known}, "
              f"adder exact on {n} length-{t} pairs")
    sym = [(r, a) for r in range(2, 13) for a in range(1, 9)
           if 2 * a + 1 > r]
    bad = []
    for (r, a) in sym:
        rho = 2 * a + 1 - r
        c = measured_cmin(r, a, a)
        want = 1 if (rho >= 2 and r >= 3) else 2
        if c != want:
            bad.append((r, a, rho, c, want))
    ok(not bad, f"symmetric law fails through this path at {bad[:6]}")
    print(f"  symmetric law reproduced at {len(sym) - len(bad)}/{len(sym)} "
          f"systems")
    mirror_bad = []
    n_mirror = 0
    for b in range(2, 6):
        for rho in range(1, 5):
            W = b - 1 + rho
            for am in range(0, W // 2 + 1):
                ap = W - am
                if measured_cmin(b, am, ap) != measured_cmin(b, ap, am):
                    mirror_bad.append((b, am, ap))
                n_mirror += 1
    ok(not mirror_bad, f"mirror symmetry fails at {mirror_bad}")
    print(f"  mirror check silent at {n_mirror} cells")


def grid():
    cells = []
    for b in range(2, 11):
        for rho in range(1, 6):
            W = b - 1 + rho
            if W > 14:
                continue
            for am in range(0, W // 2 + 1):
                cells.append((b, am, W - am))
    return cells


def s2_sweep():
    print("== S2 THE ASYMMETRIC GRID ==")
    rows = []
    for (b, am, ap) in grid():
        rho = am + ap + 1 - b
        c = measured_cmin(b, am, ap)
        ok(c is not None, f"({b},{am},{ap}): no feasible c through cap")
        if c is None:
            continue
        n = adder_exact(b, am, ap, c, 2)
        ok(n is not None, f"({b},{am},{ap}): adder wrong at c={c}")
        marg = margin_cmin(b, am, ap, 2 * (am + ap))
        rows.append((b, am, ap, rho, c, marg))
    print(f"  {len(rows)} cells measured, adder-checked at each "
          f"measured c")
    return rows


def s3_verdict(rows):
    print("== S3 THE LOCUS ==")
    law_bad = [(b, am, ap, rho, c) for (b, am, ap, rho, c, m) in rows
               if c != law_cmin(b, am, ap)]
    ok(not law_bad, f"candidate law fails at {law_bad[:8]}")
    ones = sum(1 for r in rows if r[4] == 1)
    print(f"  candidate law: {len(rows) - len(law_bad)}/{len(rows)} "
          f"cells ({ones} at c=1, {len(rows) - ones} at c=2)")
    under = [(b, am, ap, rho, c, m) for (b, am, ap, rho, c, m) in rows
             if c > m]
    ok(not under, f"margin UNDERpredicts at {under[:6]}")
    over = [(b, am, ap, rho, c, m) for (b, am, ap, rho, c, m) in rows
            if c < m]
    print(f"  margin overpredicts at {len(over)} cells, "
          f"underpredicts at {len(under)}, exact at "
          f"{len(rows) - len(over) - len(under)}")
    off = sorted(set(m - c for (_, _, _, _, c, m) in over))
    print(f"  overprediction depth(s): {off}")
    census = {}
    for (b, am, ap, rho, c, m) in over:
        census[rho] = census.get(rho, 0) + 1
    print(f"  miss census by rho: {dict(sorted(census.items()))}")
    off_rho2 = [(b, am, ap) for (b, am, ap, rho, c, m) in over
                if rho != 2]
    print(f"  misses OFF rho = 2: {off_rho2}")
    rho2_exact = [(b, am, ap, min(am, ap))
                  for (b, am, ap, rho, c, m) in rows
                  if rho == 2 and c == m]
    print(f"  rho = 2 cells where the margin is EXACT "
          f"(cell, min endpoint): {rho2_exact}")
    wedge_bad = []
    for (b, am, ap, rho, c, m) in rows:
        in_wedge = (law_cmin(b, am, ap) == 1
                    and b * rho < 2 * (am + ap))
        if in_wedge != (c < m):
            wedge_bad.append((b, am, ap, rho, c, m))
    ok(not wedge_bad,
       f"wedge characterization fails at {wedge_bad[:6]}")
    print(f"  wedge {{law grants 1 and b*rho < 2W}} matches the miss "
          f"set at {len(rows) - len(wedge_bad)}/{len(rows)} cells")


def scaling_margin(b, am, ap, m):
    """The scaling bound in its own two branches: b-power part at its
    exponent, b-coprime part at the margin against spread m0 * W."""
    s = 0
    while m % b == 0:
        m //= b
        s += 1
    if m == 1:
        return s
    return s + margin_cmin(b, am, ap, m * (am + ap))


def s4_scaling():
    print("== S4 THE SCALING SIBLING ==")
    cells = [(3, 2, 2), (10, 6, 6), (3, 2, 3), (3, 1, 4),
             (4, 2, 3), (5, 2, 4), (3, 1, 3), (6, 2, 4)]
    miss = []
    for (b, am, ap) in cells:
        for m in (2, 3, 5):
            p = scaling_margin(b, am, ap, m)
            S = sorted(set(m * d for d in digits(am, ap)))
            q = next((c for c in range(6)
                      if game_feasible(b, am, ap, c, S)), None)
            ok(q is not None, f"scaling ({b},{am},{ap}) m={m}: "
               f"no feasible c")
            if q is not None and p != q:
                miss.append((b, am, ap, am + ap + 1 - b, m, p, q))
    print(f"  (b,am,ap,rho,m,margin,measured) misses: {miss}")
    under = [x for x in miss if x[6] > x[5]]
    ok(not under, f"scaling margin underpredicts at {under}")
    rhos = sorted(set(x[3] for x in miss))
    print(f"  every scaling miss is one digit high; miss rho values: "
          f"{rhos}")


def main():
    s1_control()
    rows = s2_sweep()
    s3_verdict(rows)
    s4_scaling()
    print()
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}")
        for f in FAILURES:
            print(f"  - {f}")
    else:
        print("all checks passed")


if __name__ == "__main__":
    main()
