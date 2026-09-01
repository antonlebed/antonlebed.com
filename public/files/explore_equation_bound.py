"""The uniform equation bound: is EVERY period-multiple's congruence an
exact integer equation past one explicit threshold a_0(P, r)?

THE QUESTION
------------
The even-P lattice-avoidance lemma's period-P layer is proved by one
congruence functional forced to an exact integer equation by a size
bound (explore_congruence_kill.py D1-D2, F4). The higher layers m >= 2
(periods 2P and up) carry the same congruence mod N_m =
p_{mP-1} + q_{mP} - 2, and the measured coefficient mass over N_m is
flat in m and ~1/A (explore_congruence_kill.py F5) — an observation.
This probe tests the hand derivation that turns the observation into a
closed-form bound: an explicit R(P, r, A), rational in A, with
sum_j cap_j |c_j^(m)| <= R * q_{mP-1} <= (R/A) * N_m for ALL m at
once, so R < A makes every layer an exact equation simultaneously,
with a_0(P, r) = the least A from which R < A holds on.

THE HAND-ATTACK (pre-engine, on paper; conventions re-derived from
the engine: quotients 1-based with a_i = A iff i = 0 mod P else 1,
q_k = K(a_1..a_k) with q_0 = 1, p_k = K(a_2..a_k), digit caps
cap(k) = a_{k+1} with the class at k = P-1 mod P, aligned position
j = (k+r) mod mP putting the class caps at j = r-1 mod P)
----------------------------------------------------------------------
D1  THE PALINDROME COLLAPSES THE FOLD. Generalized d'Ocagne:
    p_n q_j - q_n p_j = (-1)^j K(a_{j+2}..a_n). With n = mP-1 the
    aligned coefficient is c_j = (-1)^j K(a_{j+2}..a_{mP-1}) - q_j
    mod N_m — and a_1..a_{mP-1} = 1^{P-1} (A 1^{P-1})^{m-1} is a
    PALINDROME (reversal maps index i to mP-i, preserving i = 0 mod
    P), while continuants are reversal-invariant. So
        chat_j := (-1)^j q_{mP-2-j} - q_j     (q_{-1} = 0):
    the whole coefficient system at every m is the q-sequence read
    from both ends. At m = 1 this is the proved layer's functional
    verbatim (q_{P-2-j} = F_{P-1-j}). Wrap positions need no separate
    case: the row of adj(I - M^m) is well-defined on L/(1-eta^m)L
    since adj(I-M^m)(1-eta^m)w = det * w = 0 mod N_m. FREE
    COROLLARY: the m-fold alternating comb solves EVERY layer's
    equation — sum over even j of chat_j = 0 because j <-> mP-2-j is
    a bijection on even indices (mP even).
D2  THE BOUND, UNIFORM IN m. |chat_j| <= q_j + q_{mP-2-j}, and the
    mirrored reindexing gives sum_j cap_j |chat_j| <= sum_j w_j q_j
    with w_j = 2 + (A-1)[j = r-1 mod P] + (A-1)[j = P-r-1 mod P]
    (merging to 2A at r = P/2). Decay down from the top via
    y_i = q_i/q_{i-1} = [a_i; a_{i-1}, ..., a_1]: s ones above an
    A-position with ratio y_0 give y_s = (F_{s+1} y_0 + F_s) /
    (F_s y_0 + F_{s-1}), a Moebius step of determinant (-1)^s —
    increasing in y_0 at EVEN s, decreasing at ODD s toward its limit
    F_{s+1}/F_s from above. So with y_0 >= A: at even s,
    y_s >= g_s(A) = (F_{s+1} A + F_s)/(F_s A + F_{s-1}) (below the
    F-ratio, which the bottom block attains); at odd s, y_s >
    F_{s+1}/F_s (the bottom block attaining it). Both parities:
    y_i >= h_s := min(F_{s+1}/F_s, g_s(A)) — the min IS the parity
    split — with s = i mod P >= 1, and y >= A at s = 0. Hence
    q_{mP-1-t}/q_{mP-1} <= D_t = prod_{s=P-t}^{P-1} 1/h_s for
    t <= P-1, blocks decay by 1/H with H = A * prod_{s=1}^{P-1} h_s,
    the weights are P-periodic in t (the A-weights land at t = r and
    t = P-r), and
        sum_j w_j q_j <= q_{mP-1} * R,
        R(P, r, A) = [sum_{t=0}^{P-1} w_t D_t] * H/(H-1).
    With N_m >= q_{mP} - 2 >= A q_{mP-1} (any m >= 1, mP >= 4),
    R < A is SUFFICIENT for sum cap |chat| < N_m at every m at once.
    AND THE THRESHOLD IS FOR-ALL-A BY A MONOTONE DOMINATOR: h_s(A)
    is nondecreasing in A (even s: an increasing Moebius map of A;
    odd s: constant), so every D_t is nonincreasing, H increasing,
    H/(H-1) decreasing — hence with chi_t = [t = r mod P] +
    [t = P-r mod P] (the count of A-weights at t, so w_t =
    2 + (A-1) chi_t), U(A) := [sum_t (2/A + chi_t) D_t] * H/(H-1)
    dominates R/A (since (A-1)/A <= 1) and is NONINCREASING in A.
    U(a_0) < 1 therefore proves R < A for ALL A >= a_0 at once, no
    scan interval left open.
D3  THE MARGIN IS THE m = 1 CLASS MASS. As A -> inf: h_s ->
    F_{s+1}/F_s, D_t -> F_{P-t}/F_P, H -> inf, so R/A ->
    (F_{P-r} + F_r)/F_P — the proved layer's class mass — and
    F_{P-r} + F_r <= F_{P-2} + 1 < F_P at every even P >= 4 (ends
    dominate by Fibonacci convexity). So a_0(P, r) := the least A
    from which R < A stays true is FINITE AT EVERY CELL, closed form
    end to end: for A >= a_0(P, r), every legal period-mP pattern
    whose value lies in (1 - eta^m)L satisfies the exact integer
    equation sum_k d_k chat_{(k+r) mod mP} = 0, for all m >= 1.

PREDICTIONS, FIXED BEFORE THE RUN (observables)
  N1 (controls; red voids the run): the palindrome identity
      K(a_{j+2}..a_{mP-1}) = q_{mP-2-j} holds exactly; the engine's
      raw coefficient at digit k equals chat_{(k+r) mod mP} exactly
      at non-wrap positions and mod N_m at wrap positions; chat at
      m = 1 equals the proved layer's closed form; the comb functional
      value is 0 at m = 1..4; |det(I - H^m)| = N_m.
  N2 (the bound chain): at every cell (even P <= 12, even r), m <= 6,
      A in {2, 5, 10, 20, 40, 100}: sum_j cap_j|chat_j| <=
      sum_j w_j q_j <= R * q_{mP-1}, and N_m >= A * q_{mP-1}. A
      violated inequality is a derivation bug — red.
  N3 (the threshold table): a_0(P, r) finite at every cell;
      prediction a_0 <= 30 everywhere (worked estimate at (4, 2):
      ~13), R < A rechecked exactly at A = 10^4 and 10^6; at
      A = a_0 the actual sum cap|chat| < N_m at every m <= 6.
  N4 (the margin): R/A's limit (F_{P-r} + F_r)/F_P < 1 at all 15
      cells, the worst cell (4, 2) at 2/3.

FINDINGS (run record at the end; every stage green, exact arithmetic)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1): the palindrome identity
    K(a_{j+2}..a_{mP-1}) = q_{mP-2-j} holds exactly, the engine's raw
    coefficient equals chat at every non-wrap position and mod N_m at
    every wrap position, chat at m = 1 equals the proved layer's
    closed form, the m-fold comb's functional value is 0 at m = 1..4,
    and |det(I - H^m)| = N_m — at all 15 cells (even P <= 12, even
    r), A in {5, 12}.
F2  THE BOUND CHAIN HOLDS (N2): sum cap|chat| <= sum w q <=
    R * q_{mP-1} and N_m >= A * q_{mP-1} at all 15 cells x A in
    {2, 5, 10, 20, 40, 100} x m = 1..6, no exception. The actual
    mass over N_m (max over m <= 6) against R/A: (4, 2): 1.082 vs
    1.660 at A = 5, 0.896 vs 1.141 at A = 10, 0.729 vs 0.782 at
    A = 40; (12, 6): 0.749 vs 1.136 at A = 5, 0.208 vs 0.239 at
    A = 40 — R is lossy by a bounded factor and tightens as A grows
    (the sweep's worst actual/N_m, 1.486, prints at (4, 2), A = 2,
    m = 6 — below every threshold).
F3  THE THRESHOLD IS AT MOST 17, AND IT COVERS EVERY A ABOVE IT (N3
    lands, sharpened post-run to close the scan gap the first
    threshold left: a_0 is now the least A with U < 1, U the
    monotone dominator of D2, so R < A is PROVED for all A >= a_0
    rather than scanned): a_0 per cell — 17 at (4, 2), 11 at (6, 2)
    and (6, 4), 10 at (8, 2) and (8, 6), 9 at (10, 2), (10, 8),
    (12, 2), (12, 10), 8 at (8, 4), 7 at (10, 4), (10, 6), (12, 4),
    (12, 8), 6 at (12, 6) — max 17; U >= 1 verified at every A in
    2..a_0-1 (so a_0 is exactly the crossing), the domination
    R <= U*A asserted across the whole s1 sweep, and at A = a_0 the
    actual
    mass sits below N_m at every m <= 6. The pre-run worked estimate
    at (4, 2) (~13) was 17 by exact arithmetic with the for-all-A
    dominator.
F4  THE MARGIN IS THE m = 1 CLASS MASS AND IT CLOSES EVERY CELL
    (N4): (F_{P-r} + F_r)/F_P runs 1/9 at (12, 6) to 2/3 at the
    worst cell (4, 2), below 1 everywhere — and below 1 at EVERY
    even P by Fibonacci convexity (D3). So the chain is closed form
    end to end (rule — proved in A and m at every even P and even
    nonzero r by the hand chain D1-D3; thresholds evaluated exactly
    at P <= 12): for A >= a_0(P, r), EVERY period-multiple's
    congruence is an exact integer equation, all m >= 1 at once.
    What it does not give: the equation's solution set at m >= 2
    (the kill) and the layers at A < a_0 — a_0 <= 17 leaves a
    finite strip per cell, unreachable by scan since every A below
    a_0 still carries infinitely many m. (Settled since:
    explore_urow_kill.py — the u-row identity collapses the kill to
    one divisibility and the census theorem closes it for all
    A >= a_0, and the strip's negative-multiple exclusion cuts the
    open pairs to a = 2 everywhere plus a = 3 at (4, 2).)

RUN RECORD: python explore_equation_bound.py — s0..s3, under a
second of wall, memory trivial, exit 0, run twice byte-identical
(the audit round's U-threshold rewrite re-run the same way).

THE DESIGN
----------
Everything exact (integers and Fractions end to end). Cell imported
from explore_parity_derivation (convergents to depth 400). s0 the
controls (palindrome, wrap congruence, m = 1 closed form, comb
kernel, the determinant); s1 the bound chain at the A-sweep with the
actual-over-bound ratio table and the U-domination assert; s2 the
a_0 table off the monotone dominator (least A with U < 1, U >= 1
verified below it, spot monotonicity at 10^4); s3 the asymptotic
margin per cell. One command runs all; wall-clock seconds; memory
trivial.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell              # noqa: E402
from explore_congruence_kill import (                   # noqa: E402
    n_m, raw_coeffs, caps_vec, even_cells, hand_c, c1_pattern)


def fibs(n):
    F = [0, 1]
    while len(F) <= n:
        F.append(F[-1] + F[-2])
    return F


def continuant(a):
    """K(a) for a list of quotients; K([]) = 1."""
    k0, k1 = 1, 0
    for x in a:
        k0, k1 = x * k0 + k1, k0
    return k0


def chat(cell, m):
    """chat_j = (-1)^j q_{mP-2-j} - q_j, j = 0..mP-1 (q_{-1} = 0)."""
    n = m * cell.P
    q = cell.q
    out = []
    for j in range(n):
        mirror = q[n - 2 - j] if n - 2 - j >= 0 else 0
        out.append((mirror if j % 2 == 0 else -mirror) - q[j])
    return out


def h_bounds(P, A):
    """h_s for s = 1..P-1 (Fractions), and H = A * prod h_s."""
    F = fibs(P + 2)
    hs = {}
    for s in range(1, P):
        g = Fraction(F[s + 1] * A + F[s], F[s] * A + F[s - 1])
        hs[s] = min(Fraction(F[s + 1], F[s]), g)
    H = Fraction(A)
    for s in range(1, P):
        H *= hs[s]
    return hs, H


def big_r(P, r, A):
    """R(P, r, A) = [sum_t w_t D_t] * H/(H-1), exact Fraction."""
    hs, H = h_bounds(P, A)
    W = Fraction(0)
    D = Fraction(1)
    for t in range(P):
        w = 2
        if t % P == r % P:
            w += A - 1
        if t % P == (P - r) % P:
            w += A - 1
        W += w * D
        if t < P - 1:
            D /= hs[P - 1 - t]
    return W * H / (H - 1)


def big_u(P, r, A):
    """U(P, r, A) = [sum_t (2/A + chi_t) D_t] * H/(H-1): dominates
    R/A and is nonincreasing in A (h_s nondecreasing in A), so
    U(a) < 1 proves R < A for every A >= a."""
    hs, H = h_bounds(P, A)
    W = Fraction(0)
    D = Fraction(1)
    for t in range(P):
        chi = (1 if t % P == r % P else 0) + \
              (1 if t % P == (P - r) % P else 0)
        W += (Fraction(2, A) + chi) * D
        if t < P - 1:
            D /= hs[P - 1 - t]
    return W * H / (H - 1)


def cap_mass(cell, r, m):
    """sum_j cap_j |chat_j| with aligned caps (A at j = r-1 mod P)."""
    P, A = cell.P, cell.A
    c = chat(cell, m)
    return sum((A if j % P == (r - 1) % P else 1) * abs(cj)
               for j, cj in enumerate(c))


def wq_mass(cell, r, m):
    """sum_j w_j q_j (the mirrored triangle bound)."""
    P, A = cell.P, cell.A
    n = m * P
    tot = 0
    for j in range(n):
        w = 2
        if j % P == (r - 1) % P:
            w += A - 1
        if j % P == (P - r - 1) % P:
            w += A - 1
        tot += w * cell.q[j]
    return tot


def mat_pow(M, m):
    a, b, c, d = M
    R = (1, 0, 0, 1)
    for _ in range(m):
        ra, rb, rc, rd = R
        R = (ra * a + rb * c, ra * b + rb * d,
             rc * a + rd * c, rc * b + rd * d)
    return R


def main():
    cells = even_cells(12)

    print("s0: controls — palindrome, wrap congruence, m = 1 form,")
    print("    comb kernel, determinant")
    for (P, r) in cells:
        for A in (5, 12):
            cell = Cell(P, A)
            for m in (1, 2, 3, 4):
                n = m * P
                N = n_m(cell, m)
                ch = chat(cell, m)
                # palindrome identity, exact
                for j in range(n):
                    K = continuant(cell.a[j + 1:n - 1])
                    mirror = cell.q[n - 2 - j] if n - 2 - j >= 0 else 0
                    assert K == mirror or (j == n - 1 and mirror == 0), \
                        (P, r, A, m, j)
                # engine raw coefficient vs chat
                raw = raw_coeffs(cell, r, m)
                for k in range(n):
                    j = (k + r) % n
                    if k + r <= n - 1:
                        assert raw[k] == ch[j], (P, r, A, m, k)
                    else:
                        assert (raw[k] - ch[j]) % N == 0, (P, r, A, m, k)
                # comb kernel
                c1 = c1_pattern(P, m)
                assert sum(ch[(k + r) % n] * d
                           for k, d in enumerate(c1)) == 0, (P, r, A, m)
                # determinant control
                a2, b2, c2, d2 = mat_pow(cell.H, m)
                det = (1 - a2) * (1 - d2) - b2 * c2
                assert abs(det) == N, (P, r, A, m)
            # m = 1 closed form
            ch1 = chat(cell, 1)
            assert ch1 == [hand_c(P, j) for j in range(P)], (P, r, A)
    print("  PASS at %d cells, A in {5, 12}, m = 1..4" % len(cells))

    print("s1: the bound chain — actual <= wq <= R*q, N_m >= A*q")
    worst = Fraction(0)
    worst_at = None
    for (P, r) in cells:
        for A in (2, 5, 10, 20, 40, 100):
            R = big_r(P, r, A)
            cell = Cell(P, A)
            for m in range(1, 7):
                q_top = cell.q[m * P - 1]
                N = n_m(cell, m)
                actual = cap_mass(cell, r, m)
                wq = wq_mass(cell, r, m)
                assert actual <= wq, (P, r, A, m)
                assert wq <= R * q_top, (P, r, A, m)
                assert N >= A * q_top, (P, r, A, m)
                assert R <= big_u(P, r, A) * A, (P, r, A, m)
                ratio = Fraction(actual, N)
                if ratio > worst:
                    worst, worst_at = ratio, (P, r, A, m)
    print("  PASS at %d cells x 6 A x m = 1..6; worst actual/N_m"
          % len(cells))
    print("  over the sweep = %.4f at (P,r,A,m) = %s"
          % (float(worst), str(worst_at)))
    for (P, r) in [(4, 2), (8, 4), (12, 6)]:
        row = []
        for A in (5, 10, 40):
            cell = Cell(P, A)
            R = big_r(P, r, A)
            act = max(Fraction(cap_mass(cell, r, m), n_m(cell, m))
                      for m in range(1, 7))
            row.append("A=%3d act %.3f  R/A %.3f" % (A, float(act),
                                                     float(R / A)))
        print("  (%2d,%2d): %s" % (P, r, "; ".join(row)))

    print("s2: the a_0 table — least A with U < 1 (U nonincreasing,")
    print("    so R < A is proved for EVERY A >= a_0, no scan gap)")
    a0max = 0
    for (P, r) in cells:
        a0 = 2
        while big_u(P, r, a0) >= 1:
            a0 += 1
            assert a0 <= 500, (P, r)
        assert big_u(P, r, a0 + 1) <= big_u(P, r, a0), (P, r)
        assert big_u(P, r, 10 ** 4) <= big_u(P, r, a0), (P, r)
        assert big_r(P, r, 10 ** 6) < 10 ** 6, (P, r)
        for A in range(2, a0):
            assert big_u(P, r, A) >= 1, (P, r, A)
        cell = Cell(P, a0)
        ok = all(cap_mass(cell, r, m) < n_m(cell, m)
                 for m in range(1, 7))
        assert ok, (P, r, a0)
        a0max = max(a0max, a0)
        print("  (P,r)=(%2d,%2d): a_0 = %3d" % (P, r, a0))
    print("  max a_0 over the 15 cells: %d" % a0max)

    print("s3: the asymptotic margin (F_{P-r} + F_r)/F_P per cell")
    F = fibs(14)
    worstm = Fraction(0)
    worstc = None
    for (P, r) in cells:
        mass = Fraction(F[P - r] + F[r], F[P])
        assert mass < 1, (P, r)
        if mass > worstm:
            worstm, worstc = mass, (P, r)
        print("  (P,r)=(%2d,%2d): %s = %.4f" % (P, r, mass,
                                                float(mass)))
    print("  worst cell %s at %s" % (worstc, worstm))

    print("ALL STAGES GREEN")


if __name__ == "__main__":
    main()
