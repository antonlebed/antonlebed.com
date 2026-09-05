"""
THE FINITE TABLE -- how many members the odd-residue member monoid has at
a designed window over ALL caps, derived from the existence criterion
and read at P = 4..20; the half-period stride as the one exception.

THE QUESTION. The existence criterion (explore_rung_existence.py D3-D6)
reads a member word at a designed window (P, A), odd shift r, as a row
(h, near set I, k) of a table: the word exists iff the base-phi
expansion of k phi^{P-1} - Lam has its support inside the deep slots,
Lam = (h phi^r + sum_I phi^{j+1} + k)/phi. The census to P = 11 built
that table to height 13, the caps reaching 13, and left open whether
the rows that fit are regular in the Zeckendorf digits of the height --
whether a column's member language is one automaton over every cap.
The question here is prior to that one: how many rows fit at all, over
every height and every cap?

THE HAND ATTACK (on paper before any engine code; conventions from
explore_rung_existence.py: slots 0..P-1, the class slot r - 1 carrying
the height h, near slots below it, deep slots above it, a nonzero digit
forcing the next slot below its cap cyclically, so a near unit at slot 0
and a deep unit at slot P - 1 exclude each other; phi^e = F_{e-1} +
F_e phi in the pair notation (u, v) for u + v phi).

  D1  ONE EQUATION IN Z[phi], TWO IN Z. Substituting Lam into the
      criterion and clearing the phi gives the golden identity in the
      form
          h phi^{r-1} + sum_S phi^j = k (phi^{P-1} - phi^{-1}),
      S = I union J the word's unit slots. Z[phi] is free of rank 2
      over Z, so this is TWO integer equations in the two integer
      unknowns (h, k), the slot set S fixed. Its matrix has columns
      phi^{r-1} = (F_{r-2}, F_{r-1}) and phi^{P-1} - phi^{-1} =
      (F_{P-2} + 1, F_{P-1} - 1); when it is nonsingular every slot set
      S determines AT MOST ONE (h, k), integral or not.
  D2  THE SLOT SETS ARE FINITE. S is a subset of the P - 2 slots other
      than the class slot and the slot above it (the slot above is free
      only when h = 0), no two cyclically adjacent, so S ranges over
      fewer than L_P sets (the Lucas count of cyclically nonconsecutive
      subsets of P slots). Hence: off the singular cells the member set
      at (P, r) over ALL caps is FINITE: at most one word per admissible
      slot set among the words that are members at two caps (D1 is
      their identity), and a one-cap word, none known, would sit below
      cap 8 with the same finite slot sets. The census to cap 13 read
      the bottom of a finite table, not the foot of a ladder. The regularity question as posed
      -- membership a function of the height's Zeckendorf digits below a
      fixed index -- is then false at every nonempty column, since a
      finite nonempty set of heights is no union of digit cylinders.
  D3  WHERE THE MATRIX IS SINGULAR. The columns are proportional over Q
      iff phi^r / (phi^P - 1) is rational, i.e. phi^P - q phi^r - 1 = 0
      for a rational q; the conjugate psi satisfies the same relation,
      and subtracting and adding the two gives q = F_P / F_r and then
      F_r (L_P - 2) = F_P L_r. With F_P L_r - F_r L_P = 2 (-1)^r F_{P-r}
      and r odd this is F_r = F_{P-r}: r = P - r, or the one coincidence
      F_1 = F_2, (P, r) = (3, 1). So the table is finite at every cell
      but the HALF-PERIOD stride 2r = P (P = 2 mod 4, r being odd) and
      the degenerate (3, 1).
  D4  THE HALF-PERIOD LAW. At 2r = P, r odd, phi^P - 1 = phi^r (phi^r -
      phi^{-r}) = phi^r L_r, so the right side is k L_r phi^{r-1} and
      the identity reads sum_S phi^j = c phi^{r-1} with the integer
      c = k L_r - h >= 0. A slot set fits iff its golden value is an
      integer multiple of phi^{r-1}; each fitting (S, c) then carries
      the whole progression h = k L_r - c, k = 1, 2, ..., so the column
      is a finite set of residues mod L_r (4, 11, 29, 76 at P = 6, 10,
      14, 18), each infinitely populated, and the heights are recognized
      by their residue and by no bounded set of Zeckendorf digits. c = 0
      is the pure tooth (h = k L_r, S empty); c = 1 is phi^{r-1} at the
      class slot, illegal; c = 2 is phi^r + phi^{r-3}, the slot above the
      class slot, illegal at h > 0; c = 3 is phi^{r+1} + phi^{r-3}, legal
      whenever r >= 3, so the height-8 word 0010801000 at (10, 5) is
      c = 3, k = 1, and 19, 30, ... follow it.
  D5  TRANSPLANTS, marked. That k > 1 recurs past P = 9 is imported from
      the census's small cells; here k = (v_u F_{r-1} - F_{r-2} v_v)/det
      is whatever the solve says, and the pure tooth alone guarantees
      k > 1 at the half-period cells.

THE SLATE (frozen before the engine ran).

  Controls (red voids the run): the determinant vanishes at exactly the
  cells D3 names, P = 3..30, every odd r; the complete table cut at
  h <= 13 equals explore_rung_existence.py's table(P, r) row for row --
  word, height, near set, deep set, k and first-fit cap -- at P = 4..11,
  every odd r, the half-period cells included; the half-period residues
  at (10, 5) include 0 (the pure tooth) and 8 (the height-8 word).

  P1  THE FINITE TABLE: at every cell P = 4..20, odd r, 2r != P, the
      complete row count, the largest height, the largest k and the
      admissible slot-set count. Predicted: every count finite (D2, a
      derivation, so the print is a control on the engine), at least one
      cell with P >= 11 carrying a row above height 13 (the census
      truncated), and k > 1 at some nondegenerate cell with P >= 11.
  P2  THE HALF-PERIOD: at (6, 3), (10, 5), (14, 7), (18, 9) the fitting
      (c, S) pairs and the residue set mod L_r. Predicted: c = 0 and
      c = 3 at every one, c = 1 and c = 2 at none.
  P3  THE DIGIT READING: at (10, 5), heights to 200, for each index m =
      1..8 whether two heights agreeing in every Zeckendorf digit below
      m differ in membership. Predicted: such a pair at every m (D4).

  KILL of the backlog's regularity question: P1 and P3 as predicted
  close it -- finite off the half-period, periodic at it, low-digit
  cylinders at neither. A nondegenerate cell whose row count grows past
  the slot-set bound, or a half-period column whose heights are not a
  union of residue classes, is a break in D1-D4 and voids the reading.

THE RUN. `python prime/code/explore_rung_finite.py` from anywhere;
estimate under a minute (fewer than 15,127 slot sets per cell at
P = 20), memory trivial.

THE FINDINGS (the post-run record; every number is a print of the run).

  THE CONTROLS PASSED (305 checks): the determinant vanishes exactly at
  2r = P and (3, 1) over P = 3..30; the complete table cut at h <= 13
  equals the census table row for row at all 28 cells P = 4..11; (10, 5)
  is singular with L = 11 and its residues include 0 and 8. (The first
  run failed the table control on two engine faults, not on the
  mathematics: the census's Fibonacci helper returned a float at a
  negative index, fixed at its source in explore_rung_existence.py, and
  the two engines listed a deep set in opposite orders.)

  F1  THE TABLE IS FINITE OFF THE HALF-PERIOD (theorem by D1-D3; the
      counts a print). Over P = 4..20, odd r, 2r != P, every column is a
      finite table: one row at r = 1 (and at r = P - 1), and once
      P >= 2r + 4 exactly 3, 8 and 21 rows at r = 3, 5, 7 -- F_{r+1}
      rows, one per Zeckendorf-legal near set, the near sets distinct
      and exhaustive at all 36 such cells (pattern, P <= 20), with the
      largest height 6, 17 and 46 there. The tables swell only
      beside the half-period, where the matrix is nearly singular: 23
      rows to height 61 at (11, 5), 59 to height 162 at (15, 7), 154 to
      height 426 at (19, 9), k reaching 5 at each; at 28 cells with
      P >= 11 a row sits above height 13, so the census to cap 13 read
      the bottom of a finite table. k > 1 recurs at 10 cells with
      P >= 11, all of them beside the half-period (P = 2r +- 1, 2r + 2).
      P1 held.

  F2  THE HALF-PERIOD IS PERIODIC (theorem by D4; the residues a print).
      At (6, 3), (10, 5), (14, 7), (18, 9) the fitting slot sets number
      2, 5, 13, 34 with c in {0, 3} at P = 6, {0, 3, 5, 7, 10} at P = 10,
      thirteen values to 28 at P = 14 and 34 values to 75 at P = 18; c =
      0 and c = 3 at every one, c = 1 and c = 2 at none. The heights are
      the residues -c mod L_r, each carried by the whole progression
      h = k L_r - c: 0 and 1 mod 4 at P = 6; 0, 1, 4, 6, 8 mod 11 at
      P = 10, the height-8 word c = 3 with slots {2, 6}; 13 residues mod
      29; 34 residues mod 76. P2 held.

  F3  NO BOUNDED SET OF DIGITS DECIDES MEMBERSHIP (the regularity
      question closed). At (10, 5) the member heights to 200 are the five
      residue classes, 91 heights, and for every index m = 1..8 two
      heights agreeing in every Zeckendorf digit below m differ in
      membership (1 against 2 at m <= 2, 2 against 8 at m = 3, 3 against
      8, 5 against 8, 1 against 9, 1 against 14, 2 against 23 at m = 8).
      Off the half-period the set is finite and nonempty, so no digit
      cylinder describes it either. P3 held; the backlog's question is
      answered NO in both regimes, and a column's member language over
      every cap is a finite lookup or a residue test, no automaton owed.

RUN RECORD. 2026-09-05, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_rung_finite.py`
from prime/code. One process, CPython, no BLAS. 305 checks passed, 2.1 s
wall against a one-minute estimate; peak working set 29.2 MB against the
512 MB ceiling.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from explore_rung_existence import fib, zadd, zsub, phipow, table, legal_sets  # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("CONTROL FAILED: " + msg)
        sys.exit(1)


def zmul(x, y):
    """(u1 + v1 phi)(u2 + v2 phi), phi^2 = phi + 1."""
    u1, v1 = x
    u2, v2 = y
    return (u1 * u2 + v1 * v2, u1 * v2 + v1 * u2 + v1 * v2)


def lucas(n):
    return fib(n - 1) + fib(n + 1)


def cyclic_sets(P, allowed):
    """Subsets of the allowed slots with no two cyclically adjacent."""
    allowed = sorted(allowed)
    out = []

    def rec(i, cur):
        if i == len(allowed):
            out.append(tuple(cur))
            return
        rec(i + 1, cur)
        j = allowed[i]
        if cur and cur[-1] == j - 1:
            return
        if j == P - 1 and cur and cur[0] == 0:
            return
        rec(i + 1, cur + [j])
    rec(0, [])
    return out


def det_of(P, r):
    a = phipow(r - 1)
    b = zsub(phipow(P - 1), phipow(-1))
    return a[1] * b[0] - a[0] * b[1]


def row(P, r, h, S, k):
    e = [0] * P
    e[r - 1] = h
    for j in S:
        e[j] = 1
    I = tuple(j for j in S if j <= r - 2)
    J = tuple(j for j in S if j >= r)
    cap = max(1, h + (1 if h and e[(r - 2) % P] else 0))
    return (tuple(e), h, I, J, k, cap)


def complete_table(P, r, hmax=None):
    """Every member word at (P, r) over all caps, by the 2x2 solve;
    at a singular cell the progressions are cut at hmax (None = the
    residue data only). Returns (rows, singular, info)."""
    a = phipow(r - 1)
    b = zsub(phipow(P - 1), phipow(-1))
    det = a[1] * b[0] - a[0] * b[1]
    rows = []
    sets_seen = 0
    if det != 0:
        for h_zero in (False, True):
            forbid = {r - 1} if h_zero else {r - 1, r}
            allowed = [j for j in range(P) if j not in forbid]
            for S in cyclic_sets(P, allowed):
                sets_seen += 1
                v = (0, 0)
                for j in S:
                    v = zadd(v, phipow(j))
                # h a - k b = -v  (two integer equations)
                num_h = v[0] * b[1] - b[0] * v[1]
                num_k = v[0] * a[1] - a[0] * v[1]
                if num_h % det or num_k % det:
                    continue
                h, k = num_h // det, num_k // det
                if k < 1 or h < 0 or (h == 0) != h_zero:
                    continue
                if h == 0 and not S:
                    continue
                rows.append(row(P, r, h, S, k))
        return rows, False, {"det": det, "sets": sets_seen}
    # singular: b = L * a with L an integer
    m = zmul(b, phipow(1 - r))
    ok(m[1] == 0, "singular cell (%d, %d) with b/a not rational" % (P, r))
    L = m[0]
    residues = []
    for h_zero in (False, True):
        forbid = {r - 1} if h_zero else {r - 1, r}
        allowed = [j for j in range(P) if j not in forbid]
        for S in cyclic_sets(P, allowed):
            v = (0, 0)
            for j in S:
                v = zadd(v, phipow(j))
            q = zmul(v, phipow(1 - r))
            if q[1] != 0 or q[0] < 0:
                continue
            c = q[0]
            if h_zero:
                if c == 0 or c % L:
                    continue
                residues.append((c, S, "h = 0 only, k = %d" % (c // L)))
                rows.append(row(P, r, 0, S, c // L))
            else:
                if not S and c != 0:
                    continue
                residues.append((c, S, "h = %d k - %d" % (L, c)))
                if hmax is not None:
                    k = 1
                    while L * k - c <= hmax:
                        if L * k - c >= 1:
                            rows.append(row(P, r, L * k - c, S, k))
                        k += 1
    return rows, True, {"L": L, "residues": residues}


def zeck(n):
    """Zeckendorf digits of n, index i for F_i (i >= 2), as a set."""
    out = set()
    i = 2
    while fib(i + 1) <= n:
        i += 1
    while n:
        if fib(i) <= n:
            out.add(i)
            n -= fib(i)
        i -= 1
    return out


def controls():
    print("CONTROLS")
    for P in range(3, 31):
        for r in range(1, P, 2):
            singular = det_of(P, r) == 0
            named = (2 * r == P) or (P, r) == (3, 1)
            ok(singular == named, "det at (%d, %d)" % (P, r))
    print("  the determinant vanishes exactly at 2r = P and (3, 1), P = 3..30")
    cells = 0
    for P in range(4, 12):
        for r in range(1, P, 2):
            mine, _, _ = complete_table(P, r, hmax=13)
            mine = {t for t in mine if t[1] <= 13}
            theirs = {(e, h, tuple(I), tuple(sorted(J)), k, cap)
                      for (e, _, h, I, J, k, cap) in table(P, r)}
            ok(mine == theirs, "table mismatch at (%d, %d): %d vs %d, e.g. %s"
               % (P, r, len(mine), len(theirs),
                  sorted(mine ^ theirs)[:2]))
            cells += 1
    print("  the complete table cut at h <= 13 equals the census table at"
          " %d cells, P = 4..11" % cells)
    _, sing, info = complete_table(10, 5)
    res = sorted({(-c) % info["L"] for c, _, _ in info["residues"]})
    ok(sing and info["L"] == 11 and 0 in res and 8 in res,
       "(10, 5) residues %s" % res)
    print("  (10, 5) is singular with L = 11 and residues %s" % res)


def finite_table():
    print("\nP1  THE FINITE TABLE (every cap; 2r != P)")
    print("  %-8s %5s %5s %5s %6s" % ("cell", "rows", "max h", "max k", "sets"))
    above13 = []
    kbig = []
    for P in range(4, 21):
        for r in range(1, P, 2):
            if 2 * r == P:
                continue
            rows, _, info = complete_table(P, r)
            mh = max((t[1] for t in rows), default=0)
            mk = max((t[4] for t in rows), default=0)
            print("  (%2d,%2d) %5d %5d %5d %6d" % (P, r, len(rows), mh, mk, info["sets"]))
            if mh > 13 and P >= 11:
                above13.append((P, r, mh))
            if mk > 1 and P >= 11:
                kbig.append((P, r, mk))
    print("  cells at P >= 11 with a row above height 13: %d (largest %s)"
          % (len(above13), max(above13, key=lambda t: t[2]) if above13 else None))
    print("  cells at P >= 11 with k > 1: %d (largest %s)"
          % (len(kbig), max(kbig, key=lambda t: t[2]) if kbig else None))
    stable = 0
    for P in range(4, 21):
        for r in range(1, P, 2):
            if P < 2 * r + 4:
                continue
            rows, _, _ = complete_table(P, r)
            near = [t[2] for t in rows]
            ok(len(set(near)) == len(near) and set(near) == set(legal_sets(0, r - 2)),
               "near sets at (%d, %d)" % (P, r))
            stable += 1
    print("  at the %d cells with P >= 2r + 4 the rows' near sets are distinct"
          " and exhaust the Zeckendorf-legal ones: F_{r+1} rows, one per near set" % stable)


def half_period():
    print("\nP2  THE HALF-PERIOD (2r = P)")
    for P in (6, 10, 14, 18):
        r = P // 2
        _, sing, info = complete_table(P, r)
        ok(sing, "(%d, %d) not singular" % (P, r))
        L = info["L"]
        ok(L == lucas(r), "L at (%d, %d) is %d not L_%d" % (P, r, L, r))
        cs = sorted({c for c, _, _ in info["residues"]})
        print("  (%2d,%2d) L_%d = %3d: %d fitting slot sets, c in %s"
              % (P, r, r, L, len(info["residues"]), cs))
        for c, S, law in sorted(info["residues"])[:6]:
            print("      c = %2d  slots %-22s %s" % (c, list(S), law))
        print("      heights = %s mod %d" % (sorted({(-c) % L for c in cs}), L))


def digit_reading():
    print("\nP3  THE DIGIT READING at (10, 5), heights to 200")
    rows, _, _ = complete_table(10, 5, hmax=200)
    members = {t[1] for t in rows}
    print("  member heights: %s" % sorted(members))
    for m in range(1, 9):
        low = {}
        found = None
        for h in range(1, 201):
            key = frozenset(i for i in zeck(h) if i < m)
            inm = h in members
            if key in low and low[key][1] != inm:
                found = (low[key][0], h)
                break
            low.setdefault(key, (h, inm))
        print("  digits below index %d: %s"
              % (m, "differ in membership at heights %s" % (found,)
                 if found else "NO pair found -- membership a function of them"))


def main():
    t0 = time.time()
    controls()
    finite_table()
    half_period()
    digit_reading()
    print("\n%d checks passed, %.1f s" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
