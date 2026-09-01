"""The uniform even-P close: is the increment of G = N_m - (T_odd +
T*_odd) a single closed form in the block continuants, positive at
every even P, every even nonzero residue, every A >= 2 and every m?

THE QUESTION
------------
The even-P lattice-avoidance lemma rests on the inequality
T_odd + T*_odd < N_m (the odd-support theorem's mass side,
explore_deep_pairs.py). It is closed at P <= 12 by a per-pair
block-recursion certificate, and at P >= 14 only above a threshold
a_0(P, r); the uniform close was thought to owe three base
inequalities per cell (G_2 > 0, DeltaG_2 > 0, DeltaG_3 >= DeltaG_2)
feeding the recursion. This probe asks whether DeltaG_m instead has
ONE closed form valid at every m >= 1, whose positivity is a paper
theorem — dissolving the certificate and the threshold at once.

THE HAND-ATTACK (pre-engine, on paper; conventions re-derived from
the engine: q_j = F_{j+1} for j <= P-1, A-quotients at j = 0 mod P
so q_P = A q_{P-1} + q_{P-2}, aligned caps A at odd slots
j = r-1 mod P, q_{-1} = 0 — confirmed against the worked deficit
vector g = (-18, 12, -6, 6, 6, 12, 18, 30) at (4, 2), a = 2, m = 2)
----------------------------------------------------------------------
D1  THE MASS IN BLOCK SUMS. M_m := T_odd + T*_odd
    = q_{mP-1} + 2 S_m + (A-1)(R_m + R'_m), with
    S_m = sum of q_j over odd j <= mP-3, R_m = sum_{t<m} q_{tP+r-1},
    R'_m = sum_{t<m} q_{tP+P-r-1}; G_m := N_m - M_m,
    N_m = p_{mP-1} + q_{mP} - 2.
D2  THE INCREMENT TELESCOPE. The quotients on [mP+1, (m+1)P-1] are
    all 1, so q_j = q_{j+1} - q_{j-1} telescopes over odd j in
    [mP+1, mP+P-3]:  Delta S_m = q_{mP-1} + q_{(m+1)P-2} - q_{mP}.
D3  ONE-BLOCK TRANSPORT. For 0 <= i <= P-1:
    q_{mP+i} = F_{i+1} q_{mP} + F_i q_{mP-1} (p likewise), and
    q_{(m+1)P} = (A F_P + F_{P-1}) q_{mP} + (A F_{P-1} + F_{P-2})
    q_{mP-1}.
D4  THE CLOSED FORM. Collecting D2 + D3 into
    Delta G_m = G_{m+1} - G_m, with x = q_{mP}, y = q_{mP-1},
    u = p_{mP}, v = p_{mP-1}:
        Delta G_m = alpha x + beta y + F_P u + (F_{P-1} - 1) v
    for EVERY m >= 1, where
        alpha = (A-1)(F_P - F_r - F_{P-r}) - F_{P-1} + 1,
        beta  = (A-1)(F_{P-1} - F_{r-1} - F_{P-r-1}) - F_{P-2} - 1.
    Hand check at (4, 2), a = 2: alpha = 0, beta = -2;
    Delta G_1 = -2*3 + 3*5 + 1*2 = 11 = G_2 - G_1 = 12 - 1;
    Delta G_2 = -2*30 + 3*50 + 19 = 109 = G_3 - G_2 = 121 - 12.
D5  THREE LEMMAS, all elementary. (a) alpha >= 0 at A >= 2:
    F_r + F_{P-r} <= F_2 + F_{P-2} on even 2 <= r <= P-2 (endpoint
    maximum — the base-case lemma of G_1's own proof), so
    alpha >= (A-2)(F_{P-1} - 1) >= 0; zero exactly at A = 2 with
    r in {2, P-2}. (b) Phi' := F_{P-1} - F_{r-1} - F_{P-r-1} >= 0:
    with a = r-1, b = P-r-1 >= 1, F_{a+b+1} = F_{a+1} F_{b+1}
    + F_a F_b >= F_a + F_b; zero exactly at (P, r) = (4, 2).
    (c) p_{mP} > q_{mP-1}: even convergents increase from
    p_2/q_2 = 1/2, so p_{mP} > q_{mP}/2 > (A/2) q_{mP-1}
    >= q_{mP-1} at A >= 2.
D6  THE ASSEMBLY. beta y = (A-1) Phi' y - (F_{P-2} + 1) y and
    F_P u - (F_{P-2} + 1) y > (F_P - F_{P-2} - 1) y
    = (F_{P-1} - 1) y by (c), so
        Delta G_m > alpha x + (A-1) Phi' y + (F_{P-1} - 1)(y + v)
    > 0 at every m >= 1 — and with the base theorem
    G_1 = (A-1)(F_P - F_r - F_{P-r}) > 0, G_m > 0 for ALL m: the
    UNIFORM EVEN-P THEOREM, T_odd + T*_odd < N_m at every even
    P >= 4, every even 0 < r < P, every A >= 2, every m >= 1, with
    no threshold and no strip. The block-recursion certificate, its
    two-increment handle, and the a_0 threshold machinery are all
    subsumed: the lattice-avoidance lemma's mass step is uniform.

FINDINGS (one run, every stage green, exact arithmetic; run record
at the end)
----------------------------------------------------------------------
F1  CONTROLS PASS: (4, 2), a = 2 reproduces G_1..G_3 = 1, 12, 121
    and DeltaG_1, DeltaG_2 = 11, 109 by the direct cap-weighted
    route.
F2  THE CLOSED FORM IS EXACT (N2): Delta G by the D4 formula equals
    the direct difference at all 3150 (P, r, A, m) instances —
    315 cells (every even P = 4..20, every even 0 < r < P,
    A = 2..8), m = 1..10.
F3  THE LEMMAS HOLD WITH THEIR EXACT EQUALITY LOCI (N3): alpha >= 0
    everywhere, zero at 17 triples, every one A = 2 with
    r in {2, P-2}; Phi' >= 0 everywhere, zero exactly at
    (P, r) = (4, 2); p_{mP} > q_{mP-1} everywhere; and the D6 bound
    sits strictly between 0 and Delta G_m at every instance.
F4  G_m > 0 EVERYWHERE, so with D5-D6 the UNIFORM EVEN-P THEOREM
    stands: T_odd + T*_odd < N_m at every even P >= 4, every even
    nonzero residue, every A >= 2, every m >= 1 — a paper theorem
    (D2-D6), machine-confirmed on the sweep. The worst ratio M/N_m
    sits at (r, A, m) = (2, 2, 1) at every P and falls from 0.8750
    (P = 4) toward 0.8090 (P = 20); no threshold, no strip. The
    per-pair block-recursion certificate and the a_0 machinery of
    the P >= 14 half are subsumed.

PREDICTIONS (frozen before the run; observables)
  N1 (controls; red voids the run): at (4, 2), a = 2 the rig
      reproduces G_1 = 1, G_2 = 12, G_3 = 121, Delta G_1 = 11,
      Delta G_2 = 109, computing G directly from the cap-weighted
      deficit vector and N_m, nothing from the closed form.
  N2 (the closed form is exact; red = derivation bug in D2-D4):
      Delta G computed by the D4 formula equals the direct
      difference G_{m+1} - G_m at every swept (P, r, A, m).
  N3 (the lemmas; red = derivation bug in D5): alpha >= 0
      everywhere, zero exactly at A = 2, r in {2, P-2};
      Phi' >= 0 everywhere, zero exactly at (P, r) = (4, 2);
      p_{mP} > q_{mP-1} everywhere; and the D6 lower bound is
      positive and strictly below Delta G_m everywhere.
  N4 (the theorem's terrain; derived): G_m > 0 at every swept
      cell; the worst ratio M/N_m prints per P for the record.

THE DESIGN
----------
Everything exact (integers end to end; the one float is the display
ratio). Cell imported from explore_parity_derivation (convergents to
depth 400); n_m and even_cells from explore_congruence_kill; the
cap-weighted deficit route — aligned_caps, gvec — from
explore_deep_pairs, so the direct side of N2 is the shipped rig's
own arithmetic and not a re-implementation. Sweep: every even
P = 4..20, every even 0 < r < P, A = 2..8, m = 1..10 (block indices
stay under the Cell depth). s0 the hand-value controls at (4, 2),
a = 2; s1 the closed-form identity N2 over the sweep; s2 the lemma
checks N3; s3 the terrain N4. One command runs all; wall-clock
estimate under a minute; memory trivial.

RUN RECORD: python explore_uniform_close.py — all stages, ~13 s
wall, memory trivial, exit 0, run twice byte-identical (25 lines).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell              # noqa: E402
from explore_congruence_kill import n_m, even_cells     # noqa: E402
from explore_deep_pairs import aligned_caps, gvec       # noqa: E402


def fib(n):
    """F_1 = F_2 = 1; F_0 = 0."""
    F = [0, 1]
    while len(F) <= n:
        F.append(F[-1] + F[-2])
    return F


def mass_direct(cell, r, m):
    """T_odd + T*_odd = sum over odd j of cap_j g_j (the shipped
    rig's own route)."""
    caps = aligned_caps(cell.P, cell.A, r, m)
    g = gvec(cell, m)
    return sum(caps[j] * g[j] for j in range(m * cell.P) if j % 2 == 1)


def g_direct(cell, r, m):
    return n_m(cell, m) - mass_direct(cell, r, m)


def coeffs(P, r, A):
    """alpha, beta of the closed form, plus Phi'."""
    F = fib(P + 1)
    alpha = (A - 1) * (F[P] - F[r] - F[P - r]) - F[P - 1] + 1
    phi2 = F[P - 1] - F[r - 1] - F[P - r - 1]
    beta = (A - 1) * phi2 - F[P - 2] - 1
    return alpha, beta, phi2


def dg_closed(cell, r, m):
    """Delta G_m by the D4 closed form."""
    P, A = cell.P, cell.A
    F = fib(P + 1)
    alpha, beta, _ = coeffs(P, r, A)
    x, y = cell.q[m * P], cell.q[m * P - 1]
    u, v = cell.p[m * P], cell.p[m * P - 1]
    return alpha * x + beta * y + F[P] * u + (F[P - 1] - 1) * v


def lower_bound(cell, r, m):
    """The D6 assembled lower bound."""
    P, A = cell.P, cell.A
    F = fib(P + 1)
    alpha, _, phi2 = coeffs(P, r, A)
    x, y = cell.q[m * P], cell.q[m * P - 1]
    v = cell.p[m * P - 1]
    return alpha * x + (A - 1) * phi2 * y + (F[P - 1] - 1) * (y + v)


def sweep_cells():
    for P in range(4, 21, 2):
        for A in range(2, 9):
            cell = Cell(P, A)
            for r in range(2, P, 2):
                yield cell, r


def s0_controls():
    print("== s0: hand-value controls at (4, 2), a = 2 ==")
    cell = Cell(4, 2)
    G = [g_direct(cell, 2, m) for m in (1, 2, 3)]
    print(f"  G_1..G_3 direct: {G}")
    assert G == [1, 12, 121]
    d1, d2 = G[1] - G[0], G[2] - G[1]
    print(f"  DeltaG_1, DeltaG_2 direct: {d1}, {d2}")
    assert (d1, d2) == (11, 109)
    print("  s0 PASS")


def s1_closed_form():
    print("== s1: closed form == direct difference over the sweep ==")
    checked = 0
    for cell, r in sweep_cells():
        for m in range(1, 11):
            lhs = dg_closed(cell, r, m)
            rhs = g_direct(cell, r, m + 1) - g_direct(cell, r, m)
            assert lhs == rhs, (cell.P, r, cell.A, m, lhs, rhs)
            checked += 1
    print(f"  identity exact at {checked} (P, r, A, m) instances")
    print("  s1 PASS")


def s2_lemmas():
    print("== s2: the three lemmas and the assembled bound ==")
    azero, pzero = [], []
    for cell, r in sweep_cells():
        P, A = cell.P, cell.A
        alpha, _, phi2 = coeffs(P, r, A)
        assert alpha >= 0, (P, r, A, alpha)
        assert phi2 >= 0, (P, r, phi2)
        if alpha == 0:
            azero.append((P, r, A))
        if A == 2 and phi2 == 0:
            pzero.append((P, r))
        for m in range(1, 11):
            assert cell.p[m * P] > cell.q[m * P - 1], (P, A, m)
            lb = lower_bound(cell, r, m)
            dg = dg_closed(cell, r, m)
            assert 0 < lb < dg, (P, r, A, m, lb, dg)
    ok_a = all(A == 2 and r in (2, P - 2) for P, r, A in azero)
    ok_p = pzero == [(4, 2)]
    print(f"  alpha = 0 at {len(azero)} triples, all A=2 r in "
          f"{{2, P-2}}: {ok_a}")
    print(f"  Phi' = 0 exactly at (4, 2): {ok_p}")
    assert ok_a and ok_p
    print("  s2 PASS")


def s3_terrain():
    print("== s3: G_m > 0 everywhere; worst ratio per P ==")
    worst = {}
    for cell, r in sweep_cells():
        P = cell.P
        for m in range(1, 11):
            g = g_direct(cell, r, m)
            assert g > 0, (P, r, cell.A, m, g)
            N = n_m(cell, m)
            ratio = (N - g) / N
            if ratio > worst.get(P, (0.0, None))[0]:
                worst[P] = (ratio, (r, cell.A, m))
    for P in sorted(worst):
        ratio, at = worst[P]
        print(f"  P={P:2d}: worst M/N = {ratio:.4f} at (r, A, m)={at}")
    print("  s3 PASS")


def main():
    cells = sum(1 for _ in sweep_cells())
    print(f"uniform even-P close: {cells} (P, r, A) cells, m = 1..10")
    print(f"even cells P <= 12 (the old exhaustion's 15): "
          f"{len(even_cells(12))}")
    s0_controls()
    s1_closed_form()
    s2_lemmas()
    s3_terrain()
    print("ALL STAGES GREEN")


if __name__ == "__main__":
    main()
