"""The parity-blind corner: is the worst mass ratio's limit at
(r, a, m) = (2, 2, 2) exactly phi/2, and why does the class-slot
parity wash out?

THE QUESTION. Both parities' worst Dmax/N_m ratio sits at the
(r, a, m) = (2, 2, 2) corner and tends to ~0.8090 as P grows
(explore_odd_transfer.py s2 prints 0.8125, 0.8095, 0.8091, 0.8090 at
odd P = 5..11; explore_uniform_close.py s3 prints 0.875 -> 0.8092 at
even P = 4..16). phi/2 = 0.80902. Write the ratio's closed form at
the corner, take P -> infinity, and say whether the limit is exactly
phi/2 and why the parity of P plays no part.

THE DERIVATION (worked on paper before this engine ran; the engine
checks every step as exact integers):

  The corner quantity. n = mP = 2P. caps_j = 2 at j = 1 mod P, else
  1; g_j = q_j + q_{2P-2-j} at odd j. Odd P: Dmax (DP over legal
  cyclic patterns). Even P: the recorded quantity is the mass bound
  M = sum over odd j of caps_j g_j (the uniform even-P theorem's own
  ratio; V0 takes the same expression at odd P).

  D1 (the sandwich closes at the corner). The charging remainder at
      (r, A) = (2, 2) is U = (2F_2 - F_3)Q + (2F_1 - F_2)F_P
      - 2F_{P-2} - F_{P-3} = F_{P-1} - F_{P-2} - F_{P-3} = 0, so
      V0 <= Dmax <= V0 + [U]_+ = V0: Dmax = V0 EXACTLY at every odd
      P, by the charging bound alone (explore_odd_m2_bound.py F4's
      theorem; no weave form consumed).
  D2 (shifted-Fibonacci continuants at A = 2). q_k = F_{k+1} for
      k <= P-1; q_{P+t} = F_{P+t+2} - F_t F_{P-1} and
      p_{P+t} = F_{P+t+1} - F_t F_{P-2}, both for 0 <= t <= P-1
      ONLY — the second A-quotient breaks the telescope at t = P,
      where the A-recursion gives the separate forms
      q_{2P} = F_{2P+3} - F_{P-1}F_{P+1} (and p_{2P} its mirror).
      In particular q_P = F_{P+2} (the A-step absorbs into the
      shift), q_{2P-1} = F_{2P+1} - F_{P-1}^2,
      p_{2P-1} = F_{2P} - F_{P-1}F_{P-2}.
  D3 (the odd-mass telescope). M = 2T + q_{2P-1} + extras with
      T = sum of q_j over odd j <= 2P-3; the extras are the cap-2
      slots landing on ODD support: j = 1 at both parities
      (g_1 = 1 + F_{2P-1} - F_{P-3}F_{P-1}), j = P+1 at even P only
      (g_{P+1} = F_{P+3} - F_{P-1} + F_{P-2}) — THE ONE PLACE THE
      PARITY OF P ENTERS THE MASS. Telescoping the odd-index sums:
      odd P:  M = q_{2P} - 1;
      even P: M = q_{2P} - 1 + F_{P+2} - F_{P-1}.
  D4 (two Fibonacci identities).
      (i)  q_{2P} = 2 F_{P+1} F_{P+2} - (-1)^P
           (reduces to F_P F_{P+3} - F_{P+1}F_{P+2} = (-1)^{P+1});
      (ii) N_2 = p_{2P-1} + q_{2P} - 2 = 4 F_{P+1}^2 - 2(1 + (-1)^P)
           (via p_{2P-1} = F_P F_{P+1} + F_{P-1}^2 and Cassini at
           P+1). So N_2 is a PERFECT SQUARE 4F_{P+1}^2 at odd P.
  D5 (the ratio and the limit).
      odd P:  rho_P = 2F_{P+1}F_{P+2} / (4F_{P+1}^2)
                    = F_{P+2} / (2 F_{P+1})
              — HALF THE FIBONACCI CONVERGENT to phi. Exactly:
              rho_P - phi/2 = psi^{P+1}/(2F_{P+1}) > 0 (psi = -1/phi,
              P+1 even), so rho_P decreases to phi/2 at rate
              ~ sqrt5/2 * phi^{-(2P+2)}.
      even P: rho_P = (2F_{P+1}F_{P+2} + F_{P+2} - F_{P-1} - 2)
                      / (4F_{P+1}^2 - 4);
              rho_P - phi/2 = (2F_{P+1}psi^{P+1} + F_{P+2} - F_{P-1}
                      + 2/phi) / (4F_{P+1}^2 - 4)
              ~ (sqrt5/2) phi^{-(P+2)} > 0.
      LIMIT phi/2 EXACTLY, BOTH PARITIES, both from above. WHY
      PARITY-BLIND: mass and N_2 are order phi^{2P}; the parity
      enters only through the j = P+1 slot term (~ phi^P, even P
      only) and Cassini's (-1)^P (O(1)) — both subdominant. With the
      slot term absent, the odd side converges at the SQUARE of the
      even side's rate.

PREDICTIONS (frozen): every equality in D1-D4 holds as exact
integers at every P in range, both parities; DP Dmax == V0 ==
q_{2P} - 1 at every odd P scanned; the recorded prints reproduce
(0.8125 at P = 5, 0.875 at P = 4); scaled deviations
(rho - phi/2) * phi^{2P+2} (odd) and * phi^{P+2} (even) tend to
sqrt5/2 = 1.1180.

KILL-SHAPES (observables): any FAIL line in s0/s1 (a closed form
differing from the engine integer); a DP value differing from V0 at
any odd cell in the DP range; a scaled deviation drifting rather
than settling.

FINDINGS.

F1  THE CLOSED FORMS ARE EXACT (s0 + s1, zero FAIL at P = 3..40
    both parities): the shifted-Fibonacci continuants match the
    window's own q/p at every index in the stated range with the
    separate q_{2P} form at the second A-step, U = 0 at every odd P,
    and the corner mass, N_2 and ratio equal their D3/D4 closed
    forms as exact integers — N_2 = 4F_{P+1}^2 a perfect square at
    every odd P, the half-convergent identity
    mass * 2F_{P+1} == N_2 * F_{P+2} exact, and DP Dmax == V0 ==
    q_{2P} - 1 at every odd P <= 13 (the sandwich D1 makes that a
    THEOREM at every odd P; the DP is its control here). The first
    engine run killed the slate's own D2 range overclaim — the
    telescoped form was asserted through t = P where the second
    A-quotient breaks it (76 FAILs, all at t = P exactly); the
    derivation only ever consumed t <= P-1, so the range clause was
    corrected and no downstream form moved.

F2  THE LIMIT IS EXACTLY phi/2, BOTH PARITIES, FROM ABOVE (s2,
    exact rationals + 80-digit Decimal after the first draft's
    double arithmetic printed 0.00000 at P = 39 — the odd deviation
    ~ phi^-80 sits far below the float wall): the recorded corner
    prints reproduce (0.8125 at P = 5, 0.875 at P = 4; P = 3 and
    P = 6 print this rig's own corner value 5/6 — P = 3's RECORDED
    worst is 0.9156 at (8, 6), off the corner, see F3), rho
    strictly decreases along each parity (no
    DESC-FAIL), and the scaled deviations settle on sqrt5/2 =
    1.11803 — (rho - phi/2)*phi^(2P+2) prints 1.11803 at P = 39
    odd, (rho - phi/2)*phi^(P+2) prints 1.11803 at P = 40 even.
    Tier: the odd-P statement rho_P = F_{P+2}/(2F_{P+1}) — half the
    Fibonacci convergent — is a THEOREM at every odd P (D1 + D3 +
    D4 are complete proofs), and so are the even-P mass-ratio
    closed form and both limits; what stays at the records' tier is
    only the even-P reading of M/N_2 as the worst DMAX ratio, which
    this rig does not touch.

F3  THE CORNER RATIO IS m-FREE, AND THE CORNER SEAT HAS A FLOOR
    (s3, added after the first findings landed): at every
    P = 3..20 the corner's mass ratio is ONE Fraction across every
    period multiple scanned (m = 2, 4, 6 at odd P; m = 1..6 at
    even; e.g. 5/6, 13/16 odd and 7/8, 5/6, 9/11 even) — a rule at
    scanned scope, the derivation left open. And the recorded
    worst-sits-at-the-corner reading holds from P = 5 up ONLY:
    P = 3's worst Dmax/N is 0.9156 at (A, m) = (8, 6) against the
    corner's 5/6, so the corner is the recorded sweeps' seat at
    P >= 4, not a theorem about every cell.

RUN RECORD. python explore_corner_limit.py — ~3 s, well under
512MB. Run twice byte-identical, 16 lines.
"""

import os
import sys
from decimal import Decimal, getcontext
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_parity_derivation import Cell                # noqa: E402
from explore_deep_pairs import (                          # noqa: E402
    aligned_caps, gvec, dp_max)
from explore_congruence_kill import n_m                   # noqa: E402


def fib(n):
    """F_1 = F_2 = 1; F_0 = 0; F at negative index = 0 (unused)."""
    if n < 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def mass(cell, r, m):
    """Sum over odd j of caps_j g_j (= V0 at odd P, M at even P)."""
    caps = aligned_caps(cell.P, cell.A, r, m)
    g = gvec(cell, m)
    return sum(caps[j] * g[j] for j in range(1, m * cell.P, 2))


def corner_closed(P):
    """(mass, N2) at the corner from the D2-D4 closed forms."""
    F = fib
    q2p = 2 * F(P + 1) * F(P + 2) - (-1) ** P
    if P % 2 == 1:
        return q2p - 1, 4 * F(P + 1) ** 2
    return q2p - 1 + F(P + 2) - F(P - 1), 4 * F(P + 1) ** 2 - 4


def s0():
    print("== s0: D2 continuants + D1 U=0 vs the window's own ==")
    bad = 0
    for P in range(3, 41):
        cell = Cell(P, 2, top=2 * P + 4)
        for t in range(0, P):
            if cell.q[P + t] != fib(P + t + 2) - fib(t) * fib(P - 1):
                bad += 1
                print(f"  FAIL q P={P} t={t}")
            if cell.p[P + t] != fib(P + t + 1) - fib(t) * fib(P - 2):
                bad += 1
                print(f"  FAIL p P={P} t={t}")
        if cell.q[2 * P] != fib(2 * P + 3) - fib(P - 1) * fib(P + 1):
            bad += 1
            print(f"  FAIL q2P P={P}")
        for k in range(P):
            if cell.q[k] != fib(k + 1) or cell.p[k] != fib(k):
                bad += 1
                print(f"  FAIL low P={P} k={k}")
        if P % 2 == 1:
            g = gvec(cell, 2)
            u = 2 * g[P + 1] - g[P + 2]
            if u != 0:
                bad += 1
                print(f"  FAIL U={u} P={P}")
    print(f"  P = 3..40 both parities: "
          f"{'all pass' if bad == 0 else f'{bad} FAIL'}")


def s1():
    print("== s1: corner mass, N2, ratio vs closed forms ==")
    bad = 0
    for P in range(3, 41):
        cell = Cell(P, 2, top=2 * P + 4)
        mnum, nnum = mass(cell, 2, 2), n_m(cell, 2)
        mcl, ncl = corner_closed(P)
        if (mnum, nnum) != (mcl, ncl):
            bad += 1
            print(f"  FAIL P={P}: num ({mnum},{nnum}) != "
                  f"closed ({mcl},{ncl})")
        if P % 2 == 1:
            if nnum != 4 * fib(P + 1) ** 2:
                bad += 1
                print(f"  FAIL square P={P}")
            # ratio == F_{P+2}/(2F_{P+1}) as exact integers
            if mnum * 2 * fib(P + 1) != nnum * fib(P + 2):
                bad += 1
                print(f"  FAIL half-convergent P={P}")
            if P <= 13:
                dmax, _ = dp_max(gvec(cell, 2), aligned_caps(P, 2, 2, 2))
                if dmax != mnum:
                    bad += 1
                    print(f"  FAIL DP {dmax} != V0 {mnum} P={P}")
    print(f"  closed forms, the square, the half-convergent, DP==V0: "
          f"{'all pass' if bad == 0 else f'{bad} FAIL'}")


def s2():
    """Exact rationals + 80-digit Decimal phi: the float wall sits
    far below the odd-P deviation (~ phi^-80 at P = 39), so no
    double arithmetic touches the deviations."""
    print("== s2: the ratios, monotone descent, scaled deviations ==")
    getcontext().prec = 80
    root5 = Decimal(5).sqrt()
    phi = (1 + root5) / 2
    prev = {0: None, 1: None}
    for P in range(3, 41):
        mcl, ncl = corner_closed(P)
        rho = Fraction(mcl, ncl)
        par = P % 2
        mono = "" if prev[par] is None else \
            ("  DESC-FAIL" if rho >= prev[par] else "")
        prev[par] = rho
        rho_d = Decimal(mcl) / Decimal(ncl)
        scale = phi ** (2 * P + 2) if par else phi ** (P + 2)
        dev = (rho_d - phi / 2) * scale
        tag = "odd " if par else "even"
        if P <= 7 or P >= 39:
            print(f"  P={P:2d} {tag}: rho = {float(rho_d):.6f}  "
                  f"scaled dev = {float(dev):.5f}{mono}")
        elif mono:
            print(f"  P={P:2d} {tag}: rho = {float(rho_d):.6f}{mono}")
    print(f"  sqrt5/2 = {float(root5 / 2):.5f}; "
          f"phi/2 = {float(phi / 2):.6f}")


def s3():
    """The audit probe formalized: is the corner's mass ratio free of
    the period multiple m, and where does the per-P worst actually
    sit? (The recorded sweeps' worst sits at the corner from P = 5
    up; P = 3's sits deeper in the (a, m) grid.)"""
    print("== s3: m-independence of the corner ratio; the P = 3 seat ==")
    bad = 0
    for P in range(3, 21):
        cell = Cell(P, 2, top=8 * P + 4)
        ratios = set()
        ms = (2, 4, 6) if P % 2 else (1, 2, 3, 4, 5, 6)
        for m in ms:
            caps = aligned_caps(P, 2, 2, m)
            g = gvec(cell, m)
            mm = sum(caps[j] * g[j] for j in range(1, m * P, 2))
            ratios.add(Fraction(mm, n_m(cell, m)))
        if len(ratios) != 1:
            bad += 1
            print(f"  M-DEP P={P}: {sorted(ratios)}")
    print(f"  corner ratio one Fraction per P across m (P = 3..20, "
          f"m to 6): {'all pass' if bad == 0 else f'{bad} FAIL'}")
    # the P = 3 seat: worst Dmax/N over the full (r, A, m) grid
    best = (Fraction(0), None)
    for A in (2, 8):
        cell = Cell(3, A)
        for m in (2, 4, 6):
            val, _ = dp_max(gvec(cell, m), aligned_caps(3, A, 2, m))
            rr = Fraction(val, n_m(cell, m))
            if rr > best[0]:
                best = (rr, (A, m))
    print(f"  P = 3 worst Dmax/N over A in {{2,8}}, m to 6: "
          f"{float(best[0]):.4f} at (A, m) = {best[1]} "
          f"(corner gives 5/6)")


def main():
    s0()
    s1()
    s2()
    s3()


if __name__ == "__main__":
    main()
