"""The odd-P even-multiple transfer: with the class slots on BOTH
parities, is the legal cyclic maximum of the deficit functional
still below N_m — and does the mass object have a closed form?

THE QUESTION
------------
The even-P lattice-avoidance half is a theorem at every even P
(explore_uniform_close.py). At odd P and even nonzero residue, every
EVEN period multiple m inherits the congruence layer and the census
divisibility verbatim — the u-row identity's proof needs only mP
even (det H^m = (-1)^{mP} = +1); the positive-multiple bound rides
along only as a measured fact (D1, s1b). What does NOT transport is
the odd-support charging: at odd P the class
slot alternates parity once per 2P, so half the class slots sit at
EVEN positions, where the even-P theorem's all-odd argmax cannot
take their cap. This probe derives the two-parity mass object — the
legal cyclic max Dmax of D(e) = sum e_j g_j — by the deep pairs' DP,
reads its argmax structure, tests a local-exchange closed form, and
asks whether Dmax < N_m at the scanned cells.

THE HAND-ATTACK (pre-engine, on paper; conventions re-derived from
the engine: quotients a_k = A iff (k+1) % P == 0 so q_P = A q_{P-1}
+ q_{P-2}, q_j = F_{j+1} for j <= P-1; aligned caps A at
j = r-1 mod P; g_j = q_j - (-1)^j q_{mP-2-j}; worked cell (3, 2),
A = 2, m = 2: q = 1,1,2,5,7,12,31, g = (-6,6,0,6,6,12),
caps = (1,2,1,1,2,1))
----------------------------------------------------------------------
D1  WHAT TRANSPORTS. m even makes n = mP even: the reflection
    j <-> n-2-j preserves parity, the palindrome forms
    chat_j = (-1)^j q_{n-2-j} - q_j and N_m = p_{n-1} + q_n - 2
    = tr(H^m) - 2 stand verbatim (|det(1 - H^m)| = tr - 2 needs
    det H^m = +1, i.e. mP even), and on Phi_m = 0 membership is the
    census divisibility q_{n-1} | w. The positive-multiple kill
    does NOT transport verbatim: the even-P proof w* <= q_{n-1} was
    the mirrored comb telescope with every even cap 1, and at odd P
    the even class slots carry cap A — the max legal w* is its own
    DP object (checked in s1b below), and w* < N_m is what the kill
    needs. Open: the mass step Dmax vs N_m.
D2  THE TWO-PARITY CLASS SLOTS. Slots j = r-1 + tP, t = 0..m-1;
    P odd alternates their parity per block (t even -> odd slot,
    t odd -> even slot), m even -> exactly m/2 of each. An even
    class slot in the TOP half carries g_j = q_j - q_{n-2-j} > 0 at
    cap A — mass the all-odd pattern cannot reach.
D3  THE LOCAL EXCHANGE. Even class slots sit P >= 3 apart and a
    class slot's neighbors are never class slots (j +- 1 differ
    from j mod P), so their neighborhoods {j-1, j, j+1} are
    disjoint and both odd neighbors carry cap 1 (the exchange
    below reads cap_{j-1}, cap_{j+1} anyway). Legality forbids
    (._, A, 1):
    e_j != 0 forces e_{j+1} = 0... < cap. Relative to the all-odd
    baseline the slot has three local options:
      keep       (c_-, 0, c_+):  c_- g_{j-1} + c_+ g_{j+1}
      break both (0,  A,  0  ):  A g_j
      break right(c_-, A-1, 0 ):  c_- g_{j-1} + (A-1) g_j
    (c_- = cap_{j-1}, c_+ = cap_{j+1}; break-left is illegal).
    Conjectured closed form:
      M_two = sum_{odd j} cap_j g_j
            + sum_{even class slots j} max(0,
                A g_j - c_- g_{j-1} - c_+ g_{j+1},
                (A-1) g_j - c_+ g_{j+1}).
D4  THE PROMOTION IS REAL AND THE BOUND GOES TIGHT. At the top even
    class slot j = n - P + r - 1, A g_j ~ A q_j beats the kept
    neighbors from A ~ 3 on — the even-P statement (max = all-odd)
    genuinely fails to transport. Worked asymptotics at (3, 2),
    m = 2, general A: q3 = 2A+1, q4 = 2A+3, q5 = 4A+4,
    N = 4A^2 + 8A + 4, all-odd = 2A^2 + 8A + 6, break-both at j = 4
    gains 2A^2 - 4A - 6, so M_two = 4A^2 + 4A and
    N - M_two = 4A + 4 > 0: the inequality SURVIVES but the ratio
    approaches 1 - 1/A — tight where even P held 0.875. Whether
    that persists at every odd cell is the run's question.
D5  THE COMB'S OWN VERDICT (hand, at (3, 2), A = 2, m = 2): the
    m-fold comb (1 at even aligned positions) is legal and
    Phi(comb) = 0 by reflection alone, but w(comb) = q0 + q2 + q4
    = 10 and q_{n-1} = 12 does not divide it — the comb FAILS the
    census divisibility, so at odd P even multiples the Phi = 0
    layer may hold the ZERO pattern alone, matching the recorded
    acyclicity reading (explore_lattice_avoidance.py F5 side). The
    rig prints the verdict per cell.

FINDINGS (all stages green, exact arithmetic; run record at the end)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1): DP == brute enumeration at all 8 small
    odd-P instances (e.g. (3,2) A=2 m=2: 30; (3,2) A=2 m=4: 1200),
    and DP == m_closed at all 15 even-P cells (a = 2, m = 2), 84
    against N = 96 at (4, 2).
F2  THE TRANSPORT IS EXACT (N2): the u-row identity holds at all
    4500 swept (odd P, A, even m, j) instances, and Phi_m(comb) = 0
    at every one — the congruence layer, the identity and the
    census divisibility stand verbatim at mP even. The
    positive-multiple kill transports as a FACT and not by the
    even-P proof (s1b, audit round): the max legal cyclic w* sits
    <= q_{n-1} at all 315 instances — 0 over — even though the
    verbatim telescope argument breaks on the cap-A even class
    slots; observation tier, the bound's own proof owed.
    [SETTLED: explore_odd_m2_bound.py — w* maximizes at the
    all-even-at-cap pattern and a telescope identity gives
    w* <= q_{n-1} - 1 at every m and A, a theorem.]
F3  NO CROSSING (N3): Dmax < N_m at all 315 sweep instances
    (P = 3..11, even r, A = 2..8, m = 2, 4, 6) and throughout s5/s6
    (A to 256, m to 16). But the terrain differs from even P in
    both directions the hand-attack predicted: the global worst
    ratio 0.9156 sits at (3, 2), A = 8, m = 6 — at even P the worst
    always sat at (r, A, m) = (2, 2, 1)-shape corners — and at
    (3, 2) the ratio climbs in BOTH dials: to 0.9961 at A = 256
    (m = 2, gap N - Dmax = 4A + 4 exactly as D4 derived) and to a
    plateau ~0.91565 in m at A = 8. The inequality is
    asymptotically TIGHT in A at (3, 2): no uniform even-P-style
    margin exists. [SETTLED: explore_odd_m2_bound.py — the
    right-charging bound Dmax <= V0 + sum of slot remainders holds
    at every m, and its margin telescopes positive: Dmax < N_m is
    a theorem at every even m.]
F4  THE ARGMAX WEAVES PARITIES (N4 fails as frozen): even
    non-class positions at cap 1 join the argmax (20 off-slot
    argmaxes printed) — e.g. (11,10) A=8 m=2: all-odd through 11,
    then even 14, 16, 18, 20(cap) — and at m = 6 it weaves back
    and forth around each top even class slot. The two-parity mass
    object is NOT a one-exchange perturbation of the all-odd
    pattern. The weave's structure is charted in
    explore_weave.py: one even run per top even class slot, ending
    at the slot, extending P - 3 below it clear of the half line.
F5  THE LOCAL EXCHANGE IS NOT THE CLOSED FORM (N5 fails as frozen,
    and wider than first recorded): DP == M_two at 69 of 105
    m = 2 instances — the 36 failures all at r >= 6 with A >= 3,
    where the even run extends below its slot at m = 2 already —
    and at 42 of 210 m >= 4 instances (diffs small: 840 on 145425
    at (5,2) A=3 m=4). [This entry originally read "exact at all
    105 m = 2 instances, 6 of 210 at m >= 4" — a misreading of
    s4's own print, which caps witnesses at 8 (all m >= 4 in loop
    order) and prints only the total 204; the referee is
    explore_weave.py s0b, DP == brute enumeration at every odd
    cell.] The closed form that IS exact is the interval-surgery
    max M_weave (explore_weave.py, DP-equal at all 189 instances
    swept there).
F6  LEGALITY IS LOAD-BEARING AT EVERY SCALE (hand, off F3's gap):
    the cap-only positive-part bound sum cap_j max(g_j, 0) at
    (3, 2), m = 2 is 4A^2 + 10A + 6 > N = 4A^2 + 8A + 4 — the
    legality-free relaxation CROSSES at every A, so no even-P-style
    mass-only close exists at odd P; any uniform proof must consume
    legality at all A, not just below a threshold.
F7  THE COMB IS DEAD AND THE LAYER IS EMPTY (N6 + census): the comb
    fails the census divisibility at every swept (P, r, A, m) — no
    COMB DIVIDES line printed — and full enumeration at 12 small
    cells (38..4354 legal patterns) finds the ZERO pattern as the
    ONLY member every time, the identity-derived criterion agreeing
    with the primary full_member on every legal pattern (audit
    round; the verdict rests on the primary definition). At odd P, even residue, even period
    multiples, the certified terrain holds NO nonzero periodic
    member at all — the acyclicity reading
    (explore_lattice_avoidance.py F5 side) confirmed at the
    enumerated scope, STRONGER than even P's {0, comb}.
    [SETTLED: explore_odd_m2_bound.py F6 — the zero-only verdict
    is now a THEOREM at every odd P, even nonzero r, even m: the
    strict w* bound pinches the census divisibility to t = 0, so
    this enumeration is the theorem's control.]

PREDICTIONS (frozen before the run; observables)
  N1 (controls; red voids the run): the cyclic DP equals brute
      enumeration at every small odd-P cell swept (n <= 12); and at
      the even-P control cells (all 15 cells of even_cells(12),
      a = 2, m = 2) the DP reproduces the odd-support closed form
      m_closed, 84 against N = 96 at (4, 2).
  N2 (the transport; red = D1 is wrong and everything stops): the
      u-row identity q_{n-1} b_j + q_j N_m + (q_n - 1) chat_j = 0
      holds at every j at every swept odd-P (cell, even m), and
      Phi_m(comb) = 0 everywhere there.
  N3 (the mass observable): Dmax and N_m print at every swept
      instance; the kill-shape observable is a printed crossing
      Dmax >= N_m. [Frozen expectation from D4: no crossing, with
      the worst ratio at r = P-1 approaching 1 from below in A.]
  N4 (argmax structure): every nonzero EVEN-position entry of a
      printed argmax sits at a class slot (exceptions printed with
      witnesses).
  N5 (the closed form): DP == M_two at every swept instance
      (mismatches printed with witnesses).
  N6 (the comb verdict, printed per (P, r, m)): whether
      q_{n-1} | w(comb) — expectation from D5: it fails.

THE DESIGN
----------
Everything exact (integers end to end; floats only in display
ratios). Cell from explore_parity_derivation; n_m from
explore_congruence_kill; aligned_caps, gvec, dp_max, m_closed,
enum_legal_cyclic, phi_of, w_of from explore_deep_pairs (the
shipped rig's own arithmetic, not a re-implementation); qtilde,
bvec, chat from explore_urow_kill. Sweep: every odd P = 3..11,
every even 0 < r < P (15 cells), A = 2..8, m in {2, 4, 6}
(315 instances); the tightness probe s5 adds A in {16, 64, 256} at
the r = P-1 cells, m = 2. Stages: s0 the N1 controls; s1 the N2
transport checks; s2 the N3 sweep; s3 the N4 argmax dump; s4 the
N5 closed-form comparison; s5 the large-A tightness probe. One
command runs all; wall-clock estimate under a minute; memory
trivial. The second run adds s6 (the m-trend, even m = 2..16 at
A in {2, 8} — the first run's worst ratio sat at m = 6, so m <= 6
did not bound the trend) and s7 (the survivor census by full
enumeration at 12 small cells, membership by the identity-derived
criterion).

RUN RECORD: python explore_odd_transfer.py — all stages, ~8 s wall,
memory trivial, exit 0, run twice byte-identical (128 lines); the
first run was s0..s5 without s6/s7, every shared stage's prints
unchanged in the second. The audit round adds s1b (max legal w*,
the positive-multiple kill checked rather than carried) and the
full_member cross-check inside s7; run twice byte-identical again
(130 lines), every prior stage's prints unchanged.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell              # noqa: E402
from explore_congruence_kill import n_m, even_cells     # noqa: E402
from explore_deep_pairs import (                        # noqa: E402
    aligned_caps, gvec, dp_max, m_closed, enum_legal_cyclic,
    phi_of, w_of)
from explore_urow_kill import qtilde, bvec, chat        # noqa: E402


def odd_cells(pmax):
    """Every odd P = 3..pmax with every even 0 < r < P."""
    return [(P, r) for P in range(3, pmax + 1, 2) for r in range(2, P, 2)]


def comb_pattern(n):
    """The m-fold comb in aligned coordinates: 1 at even positions
    (r even preserves the parity under rotation)."""
    return [1 if j % 2 == 0 else 0 for j in range(n)]


def class_slots(P, r, m):
    return [j for j in range(m * P) if j % P == (r - 1) % P]


def m_two(cell, r, m):
    """The local-exchange closed form (D3)."""
    P, A = cell.P, cell.A
    n = m * P
    caps = aligned_caps(P, A, r, m)
    g = gvec(cell, m)
    base = sum(caps[j] * g[j] for j in range(1, n, 2))
    gain = 0
    for j in class_slots(P, r, m):
        if j % 2 != 0:
            continue
        cm, cp = caps[(j - 1) % n], caps[(j + 1) % n]
        keep = cm * g[(j - 1) % n] + cp * g[(j + 1) % n]
        both = A * g[j]
        right = cm * g[(j - 1) % n] + (A - 1) * g[j]
        gain += max(0, both - keep, right - keep)
    return base + gain


def s0():
    print("== s0: N1 controls (DP vs brute force; even-P closed form)")
    # brute force at small odd-P instances (n <= 12)
    small = [(3, 2, A, 2) for A in (2, 3, 4)] + \
            [(5, 2, A, 2) for A in (2, 3)] + \
            [(5, 4, A, 2) for A in (2, 3)] + \
            [(3, 2, 2, 4)]
    for (P, r, A, m) in small:
        cell = Cell(P, A)
        n = m * P
        caps = aligned_caps(P, A, r, m)
        g = gvec(cell, m)
        val, arg = dp_max(g, caps)
        brute = max(sum(e[j] * g[j] for j in range(n))
                    for e in enum_legal_cyclic(caps))
        assert val == brute, (P, r, A, m, val, brute)
        print(f"  ({P},{r}) A={A} m={m}: DP {val} == brute {brute}")
    # even-P control: DP == m_closed at all 15 cells, a = 2, m = 2
    for (P, r) in even_cells(12):
        cell = Cell(P, 2)
        caps = aligned_caps(P, 2, r, 2)
        g = gvec(cell, 2)
        val, _ = dp_max(g, caps)
        mc = m_closed(cell, r, 2)
        assert val == mc, (P, r, val, mc)
    c42 = Cell(4, 2)
    v42, _ = dp_max(gvec(c42, 2), aligned_caps(4, 2, 2, 2))
    print(f"  even-P: DP == m_closed at all 15 cells (a=2, m=2); "
          f"(4,2): {v42} vs N = {n_m(c42, 2)}")


def s1():
    print("== s1: N2 transport (u-row identity + Phi(comb) = 0 at "
          "odd P, even m)")
    checked = 0
    for (P, r) in odd_cells(11):
        for A in (2, 5, 8):
            cell = Cell(P, A)
            qt = qtilde(P, A, 7 * P + 2)
            for m in (2, 4, 6):
                n = m * P
                N = n_m(cell, m)
                b = bvec(cell, m, qt)
                ch = chat(cell, m)
                for j in range(n):
                    assert (cell.q[n - 1] * b[j] + cell.q[j] * N
                            + (cell.q[n] - 1) * ch[j]) == 0, \
                        (P, r, A, m, j)
                    checked += 1
                comb = comb_pattern(n)
                assert phi_of(comb, cell) == 0, (P, A, m)
    print(f"  u-row identity: {checked} instances, all exact; "
          f"Phi(comb) = 0 at every swept (P, A, m)")


def s1b():
    """Audit-round stage: the positive-multiple kill needs
    w* < N_m, and the even-P telescope bound w* <= q_{n-1} does NOT
    transport verbatim (even class slots carry cap A). Compute the
    max legal cyclic w* by the same DP on the mirrored weights
    h_j = (-1)^j q_{n-2-j} and print it against q_{n-1} and N_m."""
    print("== s1b: max legal w* vs q_{n-1} and N_m (the "
          "positive-multiple kill)")
    over_q = 0
    crossings = 0
    for (P, r) in odd_cells(11):
        for A in range(2, 9):
            cell = Cell(P, A)
            for m in (2, 4, 6):
                n = m * P
                caps = aligned_caps(P, A, r, m)
                h = [(cell.q[n - 2 - j] if n - 2 - j >= 0 else 0)
                     * (1 if j % 2 == 0 else -1) for j in range(n)]
                wmax, _ = dp_max(h, caps)
                if wmax > cell.q[n - 1]:
                    over_q += 1
                if wmax >= n_m(cell, m):
                    crossings += 1
                    print(f"  CROSSING ({P},{r}) A={A} m={m}: "
                          f"w*max {wmax} >= N {n_m(cell, m)}")
    print(f"  315 instances: w*max > q_(n-1) at {over_q}, "
          f"w*max >= N_m at {crossings}")


def s2():
    print("== s2: N3 the sweep — Dmax vs N_m at odd P, even r, even m")
    crossings = 0
    worst = (0.0, None)
    for (P, r) in odd_cells(11):
        cell_worst = (0.0, None)
        for A in range(2, 9):
            cell = Cell(P, A)
            for m in (2, 4, 6):
                caps = aligned_caps(P, A, r, m)
                g = gvec(cell, m)
                val, _ = dp_max(g, caps)
                N = n_m(cell, m)
                if val >= N:
                    crossings += 1
                    print(f"  CROSSING ({P},{r}) A={A} m={m}: "
                          f"Dmax {val} >= N {N}")
                ratio = val / N
                if ratio > cell_worst[0]:
                    cell_worst = (ratio, (A, m, val, N))
                if ratio > worst[0]:
                    worst = (ratio, (P, r, A, m, val, N))
        rr, (A, m, val, N) = cell_worst
        print(f"  ({P},{r}): worst ratio {rr:.4f} at A={A} m={m} "
              f"({val}/{N})")
    print(f"  crossings: {crossings}; global worst {worst[0]:.4f} "
          f"at {worst[1]}")


def s3():
    print("== s3: N4 argmax structure (even support vs class slots)")
    bad = 0
    shown = 0
    for (P, r) in odd_cells(11):
        for A in (2, 8):
            cell = Cell(P, A)
            for m in (2, 4):
                caps = aligned_caps(P, A, r, m)
                g = gvec(cell, m)
                _, arg = dp_max(g, caps)
                slots = set(class_slots(P, r, m))
                ev = [j for j in range(0, m * P, 2) if arg[j] != 0]
                off = [j for j in ev if j not in slots]
                if off:
                    bad += 1
                    print(f"  OFF-SLOT ({P},{r}) A={A} m={m}: "
                          f"even support {ev}, slots {sorted(slots)}, "
                          f"arg {arg}")
                elif shown < 4 and A == 8 and m == 2:
                    shown += 1
                    print(f"  ({P},{r}) A={A} m={m}: even support "
                          f"{ev} (slots {sorted(j for j in slots if j % 2 == 0)}), arg {arg}")
    print(f"  off-slot argmaxes: {bad}")


def s4():
    print("== s4: N5 the closed form — DP vs M_two")
    mismatch = 0
    total = 0
    for (P, r) in odd_cells(11):
        for A in range(2, 9):
            cell = Cell(P, A)
            for m in (2, 4, 6):
                caps = aligned_caps(P, A, r, m)
                g = gvec(cell, m)
                val, arg = dp_max(g, caps)
                m2 = m_two(cell, r, m)
                total += 1
                if val != m2:
                    mismatch += 1
                    if mismatch <= 8:
                        print(f"  MISMATCH ({P},{r}) A={A} m={m}: "
                              f"DP {val} vs M_two {m2} (diff "
                              f"{val - m2}), arg {arg}")
    print(f"  {total} instances, {mismatch} mismatches")


def s5():
    print("== s5: the tightness probe (r = P-1, m = 2, large A) and "
          "N6 comb verdicts")
    for P in (3, 5, 7, 9, 11):
        r = P - 1
        for A in (16, 64, 256):
            cell = Cell(P, A)
            caps = aligned_caps(P, A, r, 2)
            g = gvec(cell, 2)
            val, _ = dp_max(g, caps)
            N = n_m(cell, 2)
            print(f"  ({P},{r}) A={A}: N - Dmax = {N - val}, "
                  f"ratio {val / N:.6f}")
    print("  -- N6: census divisibility of the comb, q_{n-1} | w(comb)")
    for (P, r) in odd_cells(11):
        for A in (2, 8):
            cell = Cell(P, A)
            for m in (2, 4):
                n = m * P
                comb = comb_pattern(n)
                w = w_of(comb, cell)
                div = w % cell.q[n - 1] == 0
                if div:
                    print(f"  COMB DIVIDES ({P},{r}) A={A} m={m}: "
                          f"w {w}, q_(n-1) {cell.q[n - 1]}")
    print("  (comb verdicts: only divisible cases print)")


def s6():
    """Second-run stage: the m-trend. The first run's worst ratio sat
    at m = 6, not m = 2 — so the sweep's m <= 6 does not bound the
    trend. Sweep every odd cell at A in {2, 8}, even m = 2..16, and
    print the per-cell max ratio over m, where it sits, and whether
    the ratio is still rising at the top of the range."""
    print("== s6: the m-trend (even m = 2..16, A in {2, 8})")
    crossings = 0
    for (P, r) in odd_cells(11):
        for A in (2, 8):
            cell = Cell(P, A, top=200)
            ratios = []
            for m in range(2, 17, 2):
                caps = aligned_caps(P, A, r, m)
                g = gvec(cell, m)
                val, _ = dp_max(g, caps)
                N = n_m(cell, m)
                if val >= N:
                    crossings += 1
                    print(f"  CROSSING ({P},{r}) A={A} m={m}")
                ratios.append(val / N)
            best = max(ratios)
            at = 2 * (ratios.index(best) + 1)
            rising = ratios[-1] > ratios[-2]
            print(f"  ({P},{r}) A={A}: max ratio {best:.6f} at m={at}"
                  f"{' RISING at m=16' if rising else ''}")
    print(f"  crossings: {crossings}")


def s7():
    """Second-run stage: the survivor census. Full enumeration of
    legal cyclic patterns at the small odd cells, membership by the
    identity-derived criterion (valid at mP even, s1); prints every
    nonzero survivor. The comb's failed divisibility (s5) says the
    even-P {0, comb} census cannot stand here — what does?"""
    from explore_deep_pairs import criterion_member, d_of
    from explore_congruence_kill import full_member
    print("== s7: the survivor census (full enumeration, small cells; "
          "criterion cross-checked against full_member)")
    for (P, r, A, m) in [(3, 2, A, 2) for A in (2, 3, 4)] + \
                        [(3, 2, A, 4) for A in (2, 3)] + \
                        [(5, 2, A, 2) for A in (2, 3)] + \
                        [(5, 4, A, 2) for A in (2, 3)] + \
                        [(7, 2, 2, 2), (7, 4, 2, 2), (7, 6, 2, 2)]:
        cell = Cell(P, A)
        caps = aligned_caps(P, A, r, m)
        pats = enum_legal_cyclic(caps)
        members = []
        for e in pats:
            crit = criterion_member(list(e), cell, m)
            full = full_member(cell, r, d_of(list(e), r), m)
            assert crit == full, (P, r, A, m, e, crit, full)
            if crit:
                members.append(e)
        nz = [e for e in members if any(e)]
        print(f"  ({P},{r}) A={A} m={m}: {len(pats)} legal, "
              f"{len(members)} members (criterion == full_member "
              f"on all), nonzero {nz if nz else 'NONE'}")


if __name__ == "__main__":
    s0()
    s1()
    s1b()
    s2()
    s3()
    s4()
    s5()
    s6()
    s7()
