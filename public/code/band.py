"""band.py -- at a fixed rank, which depths of flattening make the
least-height polynomial beat every product of factors x^d - 1, and the
single product that takes over past them.

QUESTION. flatten.py finds the chart's failing cells (h < ph) at ranks
r = M - J from 5 to 18 only. Is that range a fact about the rank, or
the chart's width M <= 40 crossing something that moves with the depth?
Read one rank at a time over unbounded depth: where does the rank first
fail, where does it last fail, and what attains h past the last
failure?

THE OBJECTS (flatten.py's senses). h(M, J) is the least height of a
nonzero multiple of (x - 1)^J of degree < M; ph(M, J) the least height
of an admissible pure product prod (x^{g_i} - 1), at least J parts and
degree < M; the cell FAILS when h < ph. At rank r the pure products
admissible are exactly (x - 1)^J q with q = (x - 1)^t prod_{d in E}
[d]_x, [d]_x = 1 + x + ... + x^(d-1), over multisets E of parts >= 2
with t + sum (d - 1) <= r - 1 and |E| <= J + t -- a list that depends
on the rank and not on the depth, so ph at a fixed rank costs the same
at every depth.
  THE CHAMPION. CHAMP(r, J) = (1 + x)^(r-1) (x - 1)^J, the pure product
      (x^2 - 1)^(r-1) (x - 1)^(J-r+1), admissible from J = r - 1.
  THE BAND at rank r: J_lo(r), the least failing depth, and J_hi(r),
      the greatest one the scan reaches; J_ch(r), the least depth from
      which CHAMP attains h at every depth the scan reaches.

THE HAND ATTACK, on paper before the engine.
  (1) THE ROOT AT -1 (a heuristic, carrying no tier). The row of
      (x - 1)^J is a Gaussian of width about sqrt(J)/2 in absolute
      value, and a factor 1 + x of the cofactor differences it, which
      costs a factor of order 1/sqrt(J) in the height. So s = ord_{-1} q
      buys about J^(-s/2), the most a cofactor of degree <= r - 1 can
      carry is s = r - 1, attained only by c(1 + x)^(r-1), and at fixed
      rank and large depth the champion should be the minimiser. It says
      nothing at small depth, where r - 1 differences of a narrow row are
      not smooth.
  (2) RANK 1 AND RANK 2. At rank 1 no cell fails (the lattice is one
      pure product). At rank 2 the least height is the champion's at
      every J >= 2, a theorem (rank2.py). So the scan's ranks 1 and 2
      re-measure proved facts and are controls, not evidence.
  (3) THE RANGE'S DERIVATION. A rank can fail on the chart only if
      J_lo(r) <= min(30, 40 - r); inside 5..18 that is the chart's own
      census restated, so the content is at the ranks outside it.
  (4) THE STOPPING RULE IS NOT A PROOF. A scan that stops after STOP
      clean depths with the champion attaining h cannot rule out a
      failure further out; J_hi and J_ch are the scan's, and four
      further depths past each stop are read out of sample.

THE SLATE, frozen before the engine ran. The figures are TRANSPLANTS
from an older enumeration of the same question.
  P1 THE LOW EDGE. Ranks 1..4 never fail at J = 2..140.
  P2 THE HIGH EDGE IS THE CHART'S. Ranks 19..22 fail, first at J = 26, 23,
     25 and 30, all past the chart's widths.
  P3 THE RANGE. {r : J_lo(r) <= min(30, 40 - r)} over r = 1..22 is
     {5, ..., 18}.
  P4 THE TAKEOVER. At ranks 5..10, J_ch = J_hi + 1 (the older values
     J_ch = 31, 34, 59, 61 at ranks 5..8), and the champion attains h
     at the four out-of-sample depths past each stop.
  P5 THE LOW RANKS. At ranks 2, 3 and 4 the champion attains h from
     J = 2, 7 and 13 through J = 140.
  P6 THE BAND HAS HOLES. Some rank in 5..10 is clean at a depth
     strictly between J_lo and J_hi (older: ranks 6, 7, 8).

KILLS, as prints.
  K1 A failing cell at rank 1..4 (P1 dies).
  K2 A rank in 19..22 with no failure up to its scan ceiling (P2 dies
     at that rank).
  K3 The derived range printed different from {5, ..., 18}.
  K4 J_ch != J_hi + 1 at a rank of 5..10, or an out-of-sample depth
     where the champion does not attain h.
  K5 At rank 2, 3 or 4, a depth past the printed start where the
     champion does not attain h.
  KB (bugs) h > ph; a witness not cleared or of the wrong height; the
     champion's height below h; ph above the champion's height where
     the champion is admissible.

CONTROLS, run before any verdict is read.
  C1 (POSITIVE, THE CHART) At every chart cell of ranks 1..22 the
     per-rank ph equals flatten.py's multiset ph.
  C2 (POSITIVE, THE THEOREM) At rank 2 the champion attains h at every
     J scanned, as rank2.py proves.

THE DESIGN. h is flatten.least_height's. ph at rank r is the least
height over the admissible cofactors, enumerated once per rank. Ranks
1..4 are scanned over J = 2..140. Ranks 5..10 are scanned upward from
J = 2 until STOP = 8 consecutive depths past the last failure have the
champion attaining h, with a ceiling of J = 140, then read at four
further depths. Ranks 11..22 are scanned upward only to their first
failure, with a ceiling of J = 60.

RESOURCE NOTE. Estimated before any run: a few minutes, the deepest
cells (rank 10 near J = 100, width 110) under a second each; under
a 512 MB memory guard.

FINDINGS (copied from the printed output).
  F1 THE CONTROLS PASS. C1: the per-rank ph equals flatten.py's
     multiset ph at all 560 chart cells of ranks 1..22. C2: at rank 2
     the champion attains h from J = 2 through 140.
  F2 THE LOW EDGE (P1 holds, K1 never fired). Ranks 1..4 are clean at
     every depth 2..140, widths to 144.
  F3 THE HIGH EDGE IS THE CHART'S (P2 holds). Ranks 19..22 first fail at
     J = 26, 23, 25, 30, widths 45, 43, 46, 52, all past 40. Ranks
     11..18 first fail at J = 14, 15, 10, 19, 17, 23, 19, 20.
  F4 THE RANGE (P3 holds). {r : J_lo(r) <= min(30, 40 - r)} is
     5..18, the chart's failing ranks.
  F5 THE TAKEOVER (P4 holds at six ranks). Ranks 5..10:
       rank   J_lo  J_hi  J_ch  holes
         5     18    30    31   none
         6     22    33    34   23
         7     26    58    59   55, 57
         8     19    60    61   20, 25, 27..31
         9     12    88    89   17 depths, 13..35 and 87
        10     24   106   107   105
     J_ch = J_hi + 1 at every one, and the champion attains h (with
     h = ph) at all 24 out-of-sample depths.
  F6 THE LOW RANKS (P5 holds). The champion attains h from J = 2, 7
     and 13 at ranks 2, 3, 4 through J = 140.
  F7 THE HOLES (P6 holds). Ranks 6..10 each carry clean depths inside
     their band; rank 5 alone fails at an unbroken run of depths.

RUN RECORD. 27.4 s against an estimate of a few minutes, peak working
set 26.1 MB, under a 512 MB memory guard; KB 0.
"""
import sys
import time

from flatten import (pow_xm1, height, clears, least_height, pure_table,
                     ph_of)

STOP = 8


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def cofactors(r):
    """[(q, t, |E|)] over the pure cofactors of rank r, independent of J:
    q = (x - 1)^t prod_{d in E} [d]_x, t + sum (d - 1) <= r - 1."""
    out = []

    def walk(q, E, budget, last):
        qt = q
        for t in range(0, budget + 1):
            out.append((qt, t, len(E)))
            qt = pmul(qt, [-1, 1])
        for d in range(max(last, 2), budget + 2):
            E.append(d)
            walk(pmul(q, [1] * d), E, budget - (d - 1), d)
            E.pop()

    walk([1], [], r - 1, 2)
    return out


def ph_rank(cof, J):
    base = pow_xm1(J)
    best = None
    for q, t, e in cof:
        if e <= J + t:
            hq = height(pmul(q, base))
            if best is None or hq < best:
                best = hq
    return best


def champ(r, J):
    q = [1]
    for _ in range(r - 1):
        q = pmul(q, [1, 1])
    return height(pmul(q, pow_xm1(J)))


def cell(r, J, cof):
    M = r + J
    h, v, _ = least_height(M, J)
    p = ph_rank(cof, J)
    c = champ(r, J) if J >= r - 1 else None
    kb = (len(v) != M or height(v) != h or not clears(v, J) or h > p
          or (c is not None and (c < h or p > c)))
    return h, p, c, kb


def controls():
    table = pure_table(39)
    off = n = 0
    for r in range(1, 23):
        cof = cofactors(r)
        for J in range(2, min(30, 40 - r) + 1):
            n += 1
            off += ph_rank(cof, J) != ph_of(table, r + J, J)[0]
    print("C1 per-rank ph against the multiset ph: %d chart cells, %d off"
          % (n, off))
    return off


def main():
    t0 = time.time()
    bad = controls()
    kb = 0
    rows = {}
    for r in range(1, 23):
        cof = cofactors(r)
        fails, att = [], {}
        J = 1
        ceiling = 140 if r <= 10 else 60
        while J < ceiling:
            J += 1
            h, p, c, b = cell(r, J, cof)
            kb += b
            if h < p:
                fails.append(J)
                if r >= 11:
                    break
            att[J] = c == h
            if 5 <= r <= 10 and J - (fails[-1] if fails else 0) >= STOP \
                    and fails and all(att[j] for j in range(J - STOP + 1,
                                                            J + 1)):
                break
        jlast = J
        jch = None
        for j in range(jlast, 1, -1):
            if not att.get(j):
                break
            jch = j
        oos = []
        if 5 <= r <= 10:
            for j in range(jlast + 1, jlast + 5):
                h, p, c, b = cell(r, j, cof)
                kb += b
                oos.append(c == h and h == p)
        rows[r] = (fails, jch, jlast, oos)
        holes = ([j for j in range(fails[0], fails[-1] + 1)
                  if j not in fails] if fails else [])
        print("rank %2d: J_lo %s, J_hi %s, J_ch %s, scanned to %d; holes %s;"
              " out of sample %s (%.1f s)"
              % (r, fails[0] if fails else None,
                 fails[-1] if fails else None, jch, jlast, holes,
                 oos or "-", time.time() - t0))
    k1 = [r for r in range(1, 5) if rows[r][0]]
    k2 = [r for r in range(19, 23) if not rows[r][0]]
    ranks = [r for r in range(1, 23)
              if rows[r][0] and rows[r][0][0] <= min(30, 40 - r)]
    k4 = [r for r in range(5, 11)
          if rows[r][1] != (rows[r][0][-1] + 1 if rows[r][0] else None)
          or not all(rows[r][3])]
    print("P1 low edge: failing ranks among 1..4 %s (K1 %s)" % (k1, bool(k1)))
    print("P2 ranks 19..22 first fail at %s (K2 %s)"
          % ([rows[r][0][0] if rows[r][0] else None for r in range(19, 23)],
             k2))
    print("P3 derived range %s (K3 %s)" % (ranks,
                                             ranks != list(range(5, 19))))
    print("P4 J_ch = J_hi + 1 with the out-of-sample depths at ranks 5..10:"
          " off at %s" % k4)
    print("P5 champion start at ranks 2, 3, 4: %s"
          % [rows[r][1] for r in (2, 3, 4)])
    print("C2 rank 2: champion attains h from J = %s through %d"
          % (rows[2][1], rows[2][2]))
    print("KB %d; wall %.1f s" % (kb, time.time() - t0))
    return bad + kb + (rows[2][1] != 2)


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
