"""
THE RUNG LAW -- what fixes the heights of the odd-residue member monoid's
tooth-plus-unit generators, derived, and read against the census and
against the untouched P = 10 column.

THE QUESTION. At a designed window (P, A) -- partial quotients 1 at every
place but the last of each period, where a_P = A -- and an odd shift r,
the odd-residue members are the legal aligned words e (the class slot at
j = r - 1 holding a digit up to A, every other slot a digit up to 1,
nonzero forcing the next below its cap cyclically) whose sum
S = sum_j e_j theta_j (the slots j < r wrapping to theta_{j+P}) lies in
(1 - eta)L. Every member is a sum of the cell's indecomposables, and
every indecomposable read to P = 9 is the comb, a pure class-slot tooth
or a TOOTH-PLUS-UNIT word: a height h at the class slot with unit digits
elsewhere. The rung ladder -- the r = 3 column's heights 4, 6, 8, 10
landing -theta_{r+2}, -theta_{r+3}, 2(-theta_{r+2}), -theta_{r+4}, the
same at P = 8 and P = 9 with the caps they first fit 4, 7, 8, 11, and the
r = 5 column's 4, 6, 13 -- had no law (explore_monoid_ladder.py,
explore_shifts_next_cap.py F5). This file derives one and reads it.

THE HAND ATTACK (before any engine code; index conventions re-derived
from the engines: Cell(P, A).a has A at index P - 1 and q_k = a[k-1]
q_{k-1} + q_{k-2}, so a_P = A in the usual 1-indexed notation and
theta_P = A theta_{P-1} + theta_{P-2}; d_k = e_{(k+r) mod P} multiplies
theta_{k+r}, so the aligned slot j >= r reads theta_j and j < r reads
theta_{j+P}; the class slot j = r - 1 reads theta_{P-1+r}; lam_of returns
lambda with S = (1 - eta) lambda in (1, alpha) coordinates).

  D1  THE BASIS THAT HIDES THE CAP. Write x = theta_{P-2}, y = theta_{P-1},
      a unimodular pair. Backward from y the partial quotients are all 1,
      so every theta_j with j <= P - 1 is a Fibonacci combination of x and
      y with NO A in it: theta_{P-1-n} = (-1)^{n+1} F_n x + (-1)^n F_{n-1} y
      for n >= 1 (F_0 = 0, F_1 = F_2 = 1), and theta_{P-1} = y. Forward,
      theta_P = x + A y and then all-ones again, so for 0 <= n' <= P - 1
      theta_{P+n'} = F_{n'+1} x + (A F_{n'+1} + F_{n'}) y: the cap enters
      exactly once, as A times the x-coefficient, in every forward theta.
  D2  THE WORD'S TWO SIDES. The tooth theta_{P-1+r} is forward with
      n' = r - 1: (F_r, A F_r + F_{r-1}). A unit at aligned slot j < r - 1
      is forward with n' = j: (F_{j+1}, A F_{j+1} + F_j) -- call these the
      NEAR units. A unit at j >= r is theta_j, backward, A-free -- the DEEP
      units. So the y-coordinate of S is A (h F_r + s) + (A-free), with
      s = sum over near units of F_{j+1}.
  D3  THE VALUE'S SIDE. Write lambda = a x + b y (unique). Then eta x =
      theta_{2P-2} and eta y = theta_{2P-1} are forward with n' = P - 2,
      P - 1, so the y-coordinate of (1 - eta) lambda is
      -A (a F_{P-1} + b F_P) + (A-free). Define N(lambda) = -(a F_{P-1} +
      b F_P). For a single cut lambda = -theta_j with j <= P - 1,
      d'Ocagne's identity gives N = F_{j+1}, and N is additive.
  D4  THE LAW, AND WHAT IS PROVED OF IT. Write Delta = h F_r + s -
      N(lambda) and lambda = a x + b y. The x-coordinate of the member
      identity reads h F_r + s + D = a + N, with D the deep units' x-sum
      (cap-free), so a = Delta + D; the y-coordinate reads A (h F_r + s)
      + c = A N + b (1 - F_{P-1}) - a F_{P-2}, with c the word's cap-free
      y-part, so b (1 - F_{P-1}) = Delta (A + F_{P-2}) + K with K
      cap-free. A word that is a member at two CONSECUTIVE caps has an
      integer b at both, so (F_{P-1} - 1) divides Delta: THE CONGRUENCE
      h F_r + s == N(lambda) mod (F_{P-1} - 1) is a theorem for such
      words (vacuous at P = 4, where the modulus is 1). THE LAW is the
      equality Delta = 0, which every scanned generator satisfies; what
      would make it a theorem is a bound |Delta| < F_{P-1} - 1 or an
      argument that a Delta = 0 word exists whenever any does, and this
      file has neither. Under the equality the near sum s is a sum of
      F_{j+1} over nonconsecutive j in 0..r-2, so 0 <= s <= F_r - 1, and
      the height is FORCED: h = floor(N / F_r), s = N mod F_r. The
      heights are then a function of r and the cut alone -- no P, no A,
      no index det(I - H), no class order -- which is why the r = 3
      column reads the same at P = 8 and 9.
      Checked by hand at every recorded rung: r = 3 (F_3 = 2): -theta_5 has
      N = F_6 = 8, h = 4, s = 0; -theta_6 has N = 13, h = 6, s = 1;
      2(-theta_5) has N = 16, h = 8; -theta_7 has N = 21, h = 10, s = 1;
      2(-theta_6) has N = 26, h = 13; the non-cut value 2(-theta_5) -
      theta_2 at (7, 9, 3) has N = 16 + 2 = 18, h = 9, s = 0. r = 5
      (F_5 = 5): -theta_7 has N = 21, h = 4, s = 1; -theta_8 has N = 34,
      h = 6, s = 4; 2(-theta_8) has N = 68, h = 13, s = 3. All twelve
      recorded heights, and every recorded word's unit placement, agree.
  D5  THE CAP A RUNG FIRST FITS. The tooth needs A >= h, and a near unit
      at j = r - 2 (the slot before the tooth) forces h <= A - 1. Zeckendorf
      forces that slot exactly when s >= F_{r-1}, so the first cap is h +
      [s >= F_{r-1}]: 4, 7, 8, 11 on r = 3 and 4, 7, 13 on r = 5, as
      recorded.
  D6  WHAT THE LAW DOES NOT DECIDE. The A-free parts give two more
      equations on the deep units -- signed Fibonacci sums with the
      Zeckendorf legality -- and they decide which rungs EXIST at a given
      (P, r); the law fixes the height of any rung that does. The r = 1
      and r = 7 columns at P = 9 carry no rung, and the law is silent on
      why; that system is the open front the doc states.
  D7  TRANSPLANTS, MARKED. "The P = 10 column carries the same rungs at
      the same heights" is imported from P = 8, 9; the law says the
      heights cannot differ, and says nothing about existence. A word
      that is a member at ONE cap only escapes the law by construction;
      whether any generator is such a word is a print, not a prediction.

THE SLATE (frozen before the engine ran).

  Controls (red voids the run): the generators at (8, 8, 3) reprint as
  the comb, 00400010, 01600100 and 00801001; (8, 11, 3) carries the
  height-10 word 0.1.10.0.0.0.0.1; (7, 9, 3) carries 0090010 with value
  (11, -18); the N of -theta_j equals F_{j+1} for j = 0..P-1 at three
  cells, computed from lambda's (x, y) coordinates against the Fibonacci
  table.

  P1  THE LAW (the kill): at every cell P = 4..9, odd r < P, A = 2..13,
      every indecomposable that is a member at cap A + 1 too satisfies
      h F_r + s = N(lambda) exactly. Print: the count checked, the count
      PERSISTENT, the count of law failures among the persistent, and
      every failure's word. One failure among the persistent KILLS the
      law. The comb and the pure tooth are included (their s and h are
      what they are; the law is about every member word).
  P2  THE ONE-CAP WORDS: the count of generators that are NOT members at
      cap A + 1, with the cells; no prediction, a print.
  P3  THE P = 10 COLUMN (the transplant): at r = 3 the ladder lands
      -theta_5, -theta_6, 2(-theta_5), -theta_7 at heights 4, 6, 8, 10,
      first fitting at caps 4, 7, 8, 11. Print per (r, A) at P = 10 every
      non-comb generator's word, height, s, value, N and the law's
      verdict; and the first cap of each rung. P3 is read as a guess:
      heights off the law would kill P1 already; a MISSING rung at P = 10
      kills only the transplant and is D6's open front.

THE RUN. `python prime/code/memwatch.py --limit 512
prime/code/explore_rung_law.py` from prime/code; estimate 5 minutes,
memory trivial.

THE FINDINGS (the post-run record; every number is a print of the run).

  THE CONTROLS PASSED (28 checks): the three recorded cells reprint
  their generators and values, and N(-theta_j) = F_{j+1} at every
  j < P in three cells.

  F1  THE RUNG LAW HOLDS AT EVERY GENERATOR (rule at the census's scope;
      its congruence mod F_{P-1} - 1 a theorem for every word that is a
      member at two consecutive caps, D4, and the equality owed a bound;
      the bound landed in explore_rung_existence.py D2, which makes the
      equality the theorem for every such word). Over
      P = 4..9, odd r < P, A = 2..13 the census carries 349
      indecomposables, every one a member at cap A + 1 as well (no
      one-cap word exists at this scope), and h F_r + s = N(lambda)
      holds at all 349 with zero failures. Every generator's height is
      floor(N / F_r) and its near units are the Zeckendorf digits of
      N mod F_r.

  F2  THE P = 10 COLUMN: THE HEIGHTS ARE THE LAW'S AND THE RUNGS ARE NOT
      P = 8's (observation, one run). At r = 3 the column carries
      -theta_5 at height 4 (cap 4) and -theta_6 at height 6 (cap 7) and
      NOTHING ELSE to cap 13: the height-8 and height-10 rungs of P = 8
      and 9 are absent, so the transplant P3 dies on existence while
      every height that does appear is the law's. At r = 5 the column
      carries -theta_7 at height 4 (cap 4, s = 1), -theta_8 at height 6
      (cap 7, s = 4), 2(-theta_7) at height 8 (cap 8, s = 2) and
      -theta_9 as a PURE TOOTH of height 11 (cap 11, s = 0, N = 55 =
      11 F_5). At r = 7 it carries -theta_9 at height 4 (cap 4, s = 3),
      the first rung any r = 7 column has shown. The r = 1 and r = 9
      columns are the comb alone. The column's 113 generators over the
      five odd r and caps 2..13 are every one a member at the next cap,
      so the law's hypothesis holds there as at P <= 9. Which rungs
      exist at a given (P, r) is D6's deep-unit system, open.

RUN RECORD. 2026-09-05, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_rung_law.py` from
prime/code. One process, CPython, no BLAS. 28 checks passed, 0.3 s wall
(the estimate of 5 minutes was two orders high: a cell enumerates a few
hundred legal words, not thousands); peak working set 15.4 MB against
the 512 MB ceiling.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from explore_parity_derivation import Cell                       # noqa: E402
from explore_member_monoid import (members_at, indecomposables,   # noqa: E402
                                   lam_of, theta, comb_aligned)
from explore_deep_pairs import d_of                              # noqa: E402
from explore_odd_doubling import direct_member                   # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("CONTROL FAILED: " + msg)
        sys.exit(1)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def xy_coords(cell, v):
    """(a, b) with v = a theta_{P-2} + b theta_{P-1}, v in (1, alpha)."""
    x, y = theta(cell, cell.P - 2), theta(cell, cell.P - 1)
    det = x[0] * y[1] - x[1] * y[0]
    assert abs(det) == 1
    a = (v[0] * y[1] - v[1] * y[0]) * det
    b = (x[0] * v[1] - x[1] * v[0]) * det
    assert (a * x[0] + b * y[0], a * x[1] + b * y[1]) == tuple(v)
    return a, b


def n_of(cell, lam):
    a, b = xy_coords(cell, lam)
    return -(a * fib(cell.P - 1) + b * fib(cell.P))


def word_str(e):
    return ".".join(str(d) for d in e) if max(e) > 9 else "".join(str(d) for d in e)


def read_gen(cell, r, e):
    """(h, s, lam, N, law_ok) for a generator word."""
    P = cell.P
    h = e[r - 1]
    s = sum(fib(j + 1) for j in range(r - 1) if e[j])
    lam = lam_of(cell, r, e)
    N = n_of(cell, lam)
    return h, s, lam, N, (h * fib(r) + s == N)


def persistent(P, A, r, e):
    c2 = Cell(P, A + 1)
    return direct_member(c2, r, list(d_of(e, r)), 1)


def controls():
    print("CONTROLS")
    c = Cell(8, 8)
    gens = set(indecomposables(members_at(c, 3, 1)))
    want = {(1, 0, 1, 0, 1, 0, 1, 0), (0, 0, 4, 0, 0, 0, 1, 0),
            (0, 1, 6, 0, 0, 1, 0, 0), (0, 0, 8, 0, 1, 0, 0, 1)}
    ok(gens == want, "(8, 8, 3) generators %s" % sorted(gens))
    c = Cell(8, 11)
    gens = set(indecomposables(members_at(c, 3, 1)))
    ok((0, 1, 10, 0, 0, 0, 0, 1) in gens, "(8, 11, 3) lacks the height-10 word")
    c = Cell(7, 9)
    gens = set(indecomposables(members_at(c, 3, 1)))
    ok((0, 0, 9, 0, 0, 1, 0) in gens, "(7, 9, 3) lacks 0090010")
    ok(lam_of(c, 3, (0, 0, 9, 0, 0, 1, 0)) == (11, -18), "0090010's value")
    for (P, A) in ((7, 9), (8, 4), (9, 13)):
        c = Cell(P, A)
        for j in range(P):
            t = theta(c, j)
            ok(n_of(c, (-t[0], -t[1])) == fib(j + 1),
               "N(-theta_%d) at (%d, %d)" % (j, P, A))
    print("  all controls pass (%d checks)" % CHECKS)


def census():
    print("\nP1/P2  THE LAW OVER THE CENSUS (P = 4..9, odd r, A = 2..13)")
    t0 = time.time()
    checked = pers = fails = onecap = 0
    onecap_cells = []
    for P in range(4, 10):
        for A in range(2, 14):
            cell = Cell(P, A)
            for r in range(1, P, 2):
                for e in indecomposables(members_at(cell, r, 1)):
                    checked += 1
                    h, s, lam, N, law = read_gen(cell, r, e)
                    if persistent(P, A, r, e):
                        pers += 1
                        if not law:
                            fails += 1
                            print("  LAW FAILS (persistent): (%d, %d, %d) %s h=%d s=%d N=%d"
                                  % (P, A, r, word_str(e), h, s, N))
                    else:
                        onecap += 1
                        onecap_cells.append(((P, A, r), word_str(e), h, s, N, law))
        print("  P = %d done, %.0f s" % (P, time.time() - t0))
    print("  generators checked %d; persistent %d; LAW FAILURES among persistent %d;"
          " one-cap words %d" % (checked, pers, fails, onecap))
    for row in onecap_cells[:40]:
        print("    one-cap: %s %s h=%d s=%d N=%d law=%s" % row)
    print("  P1 VERDICT: " + ("KILLED" if fails else "THE LAW HOLDS at every persistent generator"))


def column_ten():
    print("\nP3  THE P = 10 COLUMN")
    P = 10
    first = {}
    n_gen = n_pers = 0
    for r in range(1, P, 2):
        print("  r = %d" % r)
        for A in range(2, 14):
            cell = Cell(P, A)
            rows = []
            for e in indecomposables(members_at(cell, r, 1)):
                n_gen += 1
                n_pers += persistent(P, A, r, e)
                if e == comb_aligned(P, A, r):
                    continue
                h, s, lam, N, law = read_gen(cell, r, e)
                key = (r, lam)
                if key not in first:
                    first[key] = (A, h, s, word_str(e))
                rows.append("%s h=%d s=%d lam=%s N=%d %s"
                            % (word_str(e), h, s, lam, N, "ok" if law else "LAW-FAIL"))
            if rows:
                print("    A = %2d: " % A + "; ".join(rows))
    print("  P = 10 generators %d, persistent %d (the law's hypothesis at P = 10)"
          % (n_gen, n_pers))
    print("  first caps per (r, value): ")
    for (r, lam), (A, h, s, w) in sorted(first.items()):
        print("    r = %d value %s: cap %d, height %d, s %d, word %s" % (r, lam, A, h, s, w))


def main():
    t0 = time.time()
    controls()
    census()
    column_ten()
    print("\n%d checks passed, %.0f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
