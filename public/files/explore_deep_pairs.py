"""The deep pairs: does LEGALITY close the sixteen strip pairs the
mass inequality leaves open — is the legal cyclic maximum of the
deficit functional below N_m at a = 2?

THE QUESTION
------------
The even-P lattice-avoidance lemma is a theorem for all a >= a_0(P, r)
(explore_urow_kill.py F7), and below threshold the negative-multiple
exclusion T_full + T*_odd < N_m closes every strip pair at P <= 12
except SIXTEEN: a = 2 at all 15 cells plus a = 3 at (4, 2), verified
m <= 30 (F8). On a member below a_0, Phi_m is 0 or a negative
multiple of N_m; Phi_m = 0 members die into {0, comb} by the census
theorem. What is open is Phi_m = -k N_m, k >= 1. Nothing in the
proved chain uses legality; at a = 2 legality is the tightest coding
in the family (a nonzero digit forces the next to 0 except
class-to-1). This probe asks whether legality ALONE excludes the
negative multiples at the deep pairs.

THE HAND-ATTACK (pre-engine, on paper; conventions re-derived from
the engine: digit caps cap(k) = A iff (k+1) % P == 0 else 1, cyclic
legality d_{j-1} != 0 => d_j <= cap_j - 1, aligned position
j = (k+r) mod mP so aligned caps are A at j = r-1 mod P — odd slots
since r and P are even — and Phi_m = w* - w EXACTLY with
w = sum_j e_j q_j, w* = sum_j e_j (-1)^j q_{mP-2-j} over aligned
digits e)
----------------------------------------------------------------------
D1  THE DEFICIT FUNCTIONAL. Phi_m = -k N_m is exactly
        D(e) := w - w* = sum_j e_j g_j = k N_m,
    g_j := q_j - (-1)^j q_{mP-2-j} (q at negative index = 0). So the
    negative multiples live iff some legal cyclic pattern has
    D(e) >= N_m — the sharp object is Dmax := max over legal cyclic
    e of D(e), against N_m. The mass bound T_full + T*_odd is the
    cap-only relaxation of this max (drop legality, drop the even
    positions' negative terms), and it is exactly what fails at the
    sixteen pairs.
D2  REFLECTION STRUCTURE OF THE WEIGHTS. Under j <-> mP-2-j (mP
    even, so the reflection preserves parity): at even j,
    g_{mP-2-j} = q_{mP-2-j} - q_j = -g_j (antisymmetric); at odd j,
    g_{mP-2-j} = g_j (symmetric); and g_{mP-1} = q_{mP-1} alone.
    So D = sum_{odd j} e_j (q_j + q_{mP-2-j}) + (an antisymmetric
    even part whose paired weights cancel), and any bound must let
    the even top half contribute while the bottom half only hurts.
D3  THE k-LEVEL DIVISIBILITY (the census criterion at depth k). On
    Phi_m = -k N_m the u-row identity (explore_urow_kill.py F2)
    gives q_{mP-1} Psi_m = N_m (k (q_{mP} - 1) - w), so membership
    — N_m | Psi_m — is EXACTLY q_{mP-1} | k (q_{mP} - 1) - w; at
    k = 0 this is the census theorem's divisibility q_{mP-1} | w.
    So even where Dmax crosses N_m, a survivor must ALSO satisfy
    w = k (q_{mP} - 1) mod q_{mP-1} — the second kill layer.
D4  WORKED CASE (4, 2), a = 2, m = 2 (N_2 = 96, the cell where the
    mass bound fails at 114): g = (-18, 12, -6, 6, 6, 12, 18, 30),
    caps (1, 2, 1, 1, 1, 2, 1, 1). The best legal pattern found by
    hand is e = (0, 2, 0, 1, 0, 2, 0, 1): D = 24 + 6 + 24 + 30 =
    84 < 96 — every route to more needs adjacent nonzeros legality
    forbids (d_6 = 1 and d_7 = 1 clash; d_4 = 1 costs d_5 its cap,
    18 < 24). Legality cuts 114 to 84 here: the deficit CAN be
    closed by legality where mass alone fails.
D5  THE ALL-ODD PATTERN (control): e_j = 1 at every odd j is legal
    (evens all zero, so no nonzero-successor constraint binds, the
    cyclic wrap included), and
        D(all-odd) = q_{mP-1} + 2 sum_{odd i <= mP-3} q_i
    by the reflection in D2 — a closed-form lower witness for Dmax.
D6  WHAT A CLOSE WOULD MEAN. Dmax < N_m at all sixteen pairs and
    all m >= 2, plus the census theorem at k = 0, closes the even-P
    lattice-avoidance lemma at P <= 12 for ALL a >= 2 — the m = 1
    layer is already a theorem at all a (explore_congruence_kill).
    The hand proof owed would be a bound on the legality DP's value
    function; the argmax patterns' structure (s2) is its target.

D7  THE ODD-SUPPORT THEOREM (proved on paper AFTER the first run
    printed the argmax patterns — all of them the all-odd pattern
    with class slots at cap; s0c is the proof's machine control).
    Claim: for every legal cyclic e (even P, even nonzero r, any
    A >= 2, any m >= 1),
        D(e) <= sum_{odd j} cap_j g_j = T_odd + T*_odd,
    with equality attained by the all-odd-at-cap pattern (legal:
    odd positions are never cyclically adjacent, and every class
    slot is odd since r and P are even). Proof: even caps are all 1
    (class slots odd), so let E = {even j : e_j = 1}. For j in E,
    legality forces e_{j+1} <= cap_{j+1} - 1 (indices mod mP). At
    even j, g_j = q_j - q_{mP-2-j} <= q_j <= q_{j+1} <=
    q_{j+1} + q_{mP-3-j} = g_{j+1}. Charging each j in E to its
    right neighbour j+1 (odd, charged by at most one member of E,
    deficit cap_{j+1} - e_{j+1} >= 1):
        sum_{j in E} g_j <= sum_{j in E} (cap_{j+1} - e_{j+1})
        g_{j+1} <= sum_{odd i} (cap_i - e_i) g_i,
    so D(e) = sum_{odd} e_j g_j + sum_{E} g_j <=
    sum_{odd} cap_j g_j. QED. Hence
        Dmax = T_odd + T*_odd =: M(P, r, A, m)
    exactly — the DP is redundant, and legality's whole
    contribution against the mass bound is DELETING THE EVEN
    COLUMNS from T_full.
D8  THE EXACT-VALUE COROLLARY. On any member, Phi_m = 0 mod N_m
    with -Phi_m = D(e) <= M and Phi_m <= w* <= q_{mP-1} < N_m (the
    mirrored comb telescope, census theorem's step). So wherever
        M(P, r, A, m) < N_m,
    every member has Phi_m = 0 EXACTLY — at EVERY a >= 2, no
    threshold — and the census theorem closes membership to
    {0, comb}. The equation bound's a_0 machinery is subsumed
    wherever this one inequality holds: the whole even-P lemma
    reduces to M < N_m plus two proved telescopes.
D9  THE FOR-ALL-m CERTIFICATE. Every ingredient of G_m := N_m - M_m
    is a constant plus fixed linear combinations of block-residue
    sequences z_t = q_{c+tP}, p_{c+tP} and their running sums, and
    each z satisfies z_t = tau z_{t-1} - z_{t-2} (Cayley-Hamilton
    on the P-step block matrix, det 1 at even P, tau = q_P +
    p_{P-1} >= 10). Constants cancel in differences, so DeltaG_m :=
    G_{m+1} - G_m is homogeneous: DeltaG_{m+1} = tau DeltaG_m -
    DeltaG_{m-1} for every m >= 2 — every offset in DeltaG is
    >= -1, so each component instance is Cayley-Hamilton at a
    nonnegative index. Since tau >= 3, once
    DeltaG_{m*+1} >= DeltaG_{m*} > 0 the increments grow forever
    (Delta_{m+1} >= (tau-1) Delta_m), so G_m > 0 for ALL m follows
    from finitely many exact base values per (P, r, a): the
    recursion verified at the base, G positive up to m*, and the
    two-increment handle. This is the strip's for-all-m dominator.

FINDINGS (F1-F4 the first run, F5-F8 the second; every stage green,
exact arithmetic; run record at the end)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1, N2): g-reflection, D(comb) = 0, the all-odd
    closed form, DP = brute force at the three s0 cells (98, 970,
    674 legal patterns), the D4 hand witness 84 reproduced; and
    full_member agrees with the identity criterion [Phi_m = -k N_m,
    q_{mP-1} | k(q_{mP}-1) - w] on every legal pattern at all three
    cells — the k-level divisibility is the membership, at every
    depth k.
F2  LEGALITY CLOSES ALL SIXTEEN DEEP PAIRS (N3 lands): Dmax < N_m
    at every deep pair and every m = 2..30, worst ratio always at
    m = 2, max 0.8750 at (4,2) a=2 (84/96), min 0.7241 at (12,6);
    the k-level census s3 never fires. The mass bound's 114 at
    (4,2) a=2 m=2 is legality-cut to 84.
F3  THE ARGMAX IS THE ALL-ODD-AT-CAP PATTERN (N4): at every probed
    (pair, m <= 4) the DP argmax is 1 at every odd position with
    the class slots raised to cap (e.g. 020101 repeating at (6,2)) —
    the pattern whose value is T_odd + T*_odd, which D7 then proved
    maximal by hand.
F4  SURVIVORS = {0, COMB} EVERYWHERE (N5): full enumeration at all
    16 deep pairs at m = 2 and the P <= 6 cells at m = 3 (98 to
    217154 legal patterns per cell) — exactly 2 members every time,
    the zero pattern and the m-fold comb.
F5  THE CLOSED FORM IS THE MAX (N7, D7's control): DP max ==
    T_odd + T*_odd at all 395 probed (cell, a, m) instances — the
    16 deep pairs at m = 2..6 and all 15 cells at a = 2..8,
    m = 2..4.
F6  THE STRIP CERTIFICATE LANDS AT EVERY PAIR (N8): at all 106
    strip pairs (P <= 12, every even nonzero r, 2 <= a < a_0):
    G_m = N_m - M > 0 at m = 1..40, the DeltaG recursion
    DeltaG_{m+1} = tau DeltaG_m - DeltaG_{m-1} holds from m = 2 on
    (tau = q_P + p_{P-1}), and the handle sits at m* = 2 everywhere
    (G_1, G_2 > 0, DeltaG_2 > 0, DeltaG_3 >= DeltaG_2). With D9's
    paper recursion this closes EVERY strip pair for ALL m — the
    sixteen deep pairs included, and the strip inequality's
    for-all-m dominator with them.
F7  G_1 IS EXACTLY LINEAR IN A - 1 (read off the s1b table, then
    proved by hand): minG is always G_1 and equals
    (A-1)(F_P - F_r - F_{P-r}) — the constant part vanishes
    identically, since below the first A-quotient q_j = F_{j+1},
    p_j = F_j, so 2 sum_{odd j <= P-3} q_j = 2(F_{P-1} - 1) =
    p_{P-1} + q_{P-2} - 2 (the classical even-index Fibonacci sum),
    and the class terms give q_{P-1} - q_{r-1} - q_{P-r-1} times
    A - 1. F_r + F_{P-r} < F_P at every even P >= 4 and even
    0 < r < P (endpoint maximum 1 + F_{P-2} < F_P), so THE BASE
    CASE G_1 > 0 IS A THEOREM at every even P, not only P <= 12.
F8  THE EVEN P >= 14 TERRAIN IS UNIFORM (N9): M < N_m at every
    P = 14..20 cell, every even nonzero r, a = 2..12 and a = a_0,
    m = 1..12 — worst ratio 0.8095 at (14, 2) a = 2 m = 1. The
    transplanted margin pattern holds: worst at small m, extreme r.
    What a fully uniform even-P theorem still owes: three base
    inequalities in closed form over all even P and A — G_2 > 0,
    DeltaG_2 > 0, DeltaG_3 >= DeltaG_2 (G_1 > 0 is F7's theorem,
    and the recursion is D9's for every m >= 2, its component
    Cayley-Hamilton instances sitting at nonnegative indices from
    the first).

PREDICTIONS (N1-N6 frozen before the first run, N7-N9 before the
second; observables)
  N1 (controls; red voids the run): g-reflection (even antisym, odd
      sym, g_{mP-1} = q_{mP-1}) at all 16 deep pairs, m = 2..4;
      D(comb) = 0 and D(all-odd) matches D5's closed form
      everywhere; the DP maximum equals the brute-force maximum of
      D over the full legal cyclic enumeration at (4,2) a=2 m=2,3
      and (6,2) a=2 m=2; the D4 hand witness 84 is reproduced at
      (4,2) a=2 m=2.
  N2 (membership = criterion; the identity's control): on the full
      legal enumeration at the s0 cells, full_member agrees with
      [Phi_m = -k N_m for some integer k >= 0 AND q_{mP-1} |
      k (q_{mP} - 1) - w] on every pattern.
  N3 (the DP table; honestly open): Dmax vs N_m at the 16 deep
      pairs, m = 2..30. Prediction (from D4, open): Dmax < N_m at
      every pair and every m — legality closes the deep strip — and
      Dmax/N_m stabilizes in m (both sides share the P-periodic
      block recursion).
  N4 (the argmax structure, for the owed hand proof): the DP argmax
      at m = 2..4 per pair prints; prediction (open): supported on
      the odd positions and the top-half evens, class slots at cap
      where reachable.
  N5 (cross-check): full enumeration of legal cyclic period-mP
      patterns with full_member at every deep pair at m = 2, plus
      m = 3 at the P = 4 and P = 6 cells: nonzero survivors exactly
      the m-fold comb.
  N6 (conditional, only if N3 sees a crossing): at every (pair, m)
      with Dmax >= N_m, the patterns at D = k N_m are enumerated
      and the k-level divisibility (D3) kills all of them.
  N7 (the odd-support theorem's control; red = derivation bug in
      D7): DP max == T_odd + T*_odd at all 16 deep pairs m = 2..6,
      and at all 15 cells for a = 2..8, m = 2..4.
  N8 (the strip closes for all m; honestly open): at every strip
      pair (P, r, a) with P <= 12, 2 <= a < a_0(P, r): M < N_m at
      m = 1..40; DeltaG_m := G_{m+1} - G_m obeys DeltaG_{m+1} =
      tau DeltaG_m - DeltaG_{m-1} (tau = q_P + p_{P-1}) from some
      base m <= 5 on; and a handle m* <= 38 exists with G_m > 0 up
      to m*, DeltaG_{m*} > 0 and DeltaG_{m*+1} >= DeltaG_{m*} — the
      D9 certificate, closing every strip pair for ALL m.
  N9 (the even-P >= 14 terrain; open, TRANSPLANT — the margin
      pattern is imported from P <= 12): at P = 14..20, every even
      nonzero r, a = 2..12 and a = a_0(P, r), m = 1..12: M < N_m
      everywhere, worst margins at small m and extreme r.

THE DESIGN
----------
Everything exact (integers end to end; the one float is the display
ratio). Cell imported from explore_parity_derivation (convergents to
depth 400); n_m, full_member, c1_pattern, even_cells imported from
explore_congruence_kill. Work in ALIGNED coordinates throughout:
aligned caps A at j = r-1 mod P else 1, cyclic legality verbatim
(rotation-invariant), digit-coordinate vector recovered by d_k =
e_{(k+r) mod mP} only where full_member needs it. s0 the controls
(reflection, comb, all-odd, DP vs brute force, hand witness,
membership = criterion); s1 the DP table (Dmax, N_m, ratio, verdict
per pair, m = 2..30) — the DP runs the line twice per boundary
state (d_{mP-1} zero / nonzero), state = previous-digit-nonzero,
max-weight with per-position tops; s2 the argmax dump at m = 2..4;
s3 the conditional k-level census (only fires on a crossing); s4
the full-enumeration cross-check (one emit per object asserted at
the emitter). The sixteen deep pairs are recomputed from
explore_urow_kill's own strip criterion, not hardcoded. The second
run adds s0c (DP == T_odd + T*_odd, the D7 control), s1b (the strip
certificate: every (P <= 12, r, 2 <= a < a_0) pair swept m = 1..40
on M < N_m, the DeltaG recursion checked against tau = q_P +
p_{P-1}, and the D9 handle located), and s1c (the P = 14..20
closed-form terrain). One command runs all; wall-clock estimate
under two minutes (the P = 12 m = 2 enumerations dominate); memory
trivial.

RUN RECORD: python explore_deep_pairs.py — all stages, 4.4 s wall,
memory trivial, exit 0, run twice byte-identical (222 lines); the
first run was s0..s4 without s0c/s1b/s1c, and every shared stage's
prints are unchanged in the second.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell              # noqa: E402
from explore_congruence_kill import (                   # noqa: E402
    n_m, full_member, c1_pattern, even_cells)


def aligned_caps(P, A, r, m):
    """Aligned cap vector: A at j = r-1 mod P, else 1."""
    return [A if j % P == (r - 1) % P else 1 for j in range(m * P)]


def gvec(cell, m):
    """g_j = q_j - (-1)^j q_{mP-2-j}, q at negative index = 0."""
    n = m * cell.P
    q = cell.q
    out = []
    for j in range(n):
        mirror = q[n - 2 - j] if n - 2 - j >= 0 else 0
        out.append(q[j] - (mirror if j % 2 == 0 else -mirror))
    return out


def w_of(e, cell):
    return sum(ej * cell.q[j] for j, ej in enumerate(e))


def phi_of(e, cell):
    """Phi_m = w* - w, exact folded form."""
    n = len(e)
    q = cell.q
    wstar = sum(ej * (q[n - 2 - j] if n - 2 - j >= 0 else 0)
                * (1 if j % 2 == 0 else -1) for j, ej in enumerate(e))
    return wstar - w_of(e, cell)


def d_of(e, r):
    """Aligned vector -> digit-coordinate vector: d_k = e_{(k+r) mod n}."""
    n = len(e)
    return [e[(k + r) % n] for k in range(n)]


def legal_cyclic(e, caps):
    n = len(e)
    for j in range(n):
        if e[j] < 0 or e[j] > caps[j]:
            return False
        if e[j - 1] != 0 and e[j] > caps[j] - 1:
            return False
    return True


def dp_max(g, caps):
    """Max of sum e_j g_j over legal cyclic e; returns (value, argmax).

    Two passes over the boundary state s = [e_{n-1} != 0]; DP state =
    previous digit nonzero; per-position top = caps[j] minus 1 if the
    previous digit is nonzero.
    """
    n = len(g)
    best_val, best_arg = None, None
    for s in (0, 1):
        # states: 0 = prev zero, 1 = prev nonzero; value + backpointer
        cur = {s: (0, [])}
        for j in range(n):
            nxt = {}
            for prev, (val, arg) in cur.items():
                top = caps[j] - (1 if prev else 0)
                for v in range(top + 1):
                    if j == n - 1 and (v != 0) != bool(s):
                        continue
                    st = 1 if v else 0
                    cand = val + v * g[j]
                    if st not in nxt or cand > nxt[st][0]:
                        nxt[st] = (cand, arg + [v])
            cur = nxt
        for st, (val, arg) in cur.items():
            if best_val is None or val > best_val:
                best_val, best_arg = val, arg
    return best_val, best_arg


def enum_legal_cyclic(caps):
    """All legal cyclic digit vectors under caps (nonzero forces the
    next below cap, wrap included)."""
    n = len(caps)
    out = []
    vec = [0] * n

    def rec(j):
        if j == n:
            if not (vec[n - 1] != 0 and vec[0] > caps[0] - 1):
                out.append(tuple(vec))
            return
        top = caps[j]
        if j > 0 and vec[j - 1] != 0:
            top = min(top, caps[j] - 1)
        for v in range(top + 1):
            vec[j] = v
            rec(j + 1)
        vec[j] = 0

    rec(0)
    assert len(out) == len(set(out))
    return out


def deep_pairs():
    """Recompute the sixteen strip pairs the mass inequality leaves
    open (explore_urow_kill s6's criterion, not hardcoded), using
    the equation bound's thresholds."""
    from explore_equation_bound import big_u
    pairs = []
    for (P, r) in even_cells(12):
        # a_0 = least A >= 2 with U < 1 (monotone dominator)
        A = 2
        while big_u(P, r, A) >= 1:
            A += 1
        a0 = A
        for a in range(2, a0):
            cell = Cell(P, a)
            ok_all_m = True
            for m in range(2, 31):
                n = m * P
                caps = aligned_caps(P, a, r, m)
                t_full = sum(caps[j] * cell.q[j] for j in range(n))
                t_odd = sum(caps[j] * cell.q[n - 2 - j]
                            for j in range(1, n - 2, 2))
                if t_full + t_odd >= n_m(cell, m):
                    ok_all_m = False
                    break
            if not ok_all_m:
                pairs.append((P, r, a))
    return pairs


def m_closed(cell, r, m):
    """M = T_odd + T*_odd, the odd-support theorem's closed form."""
    P = cell.P
    n = m * P
    caps = aligned_caps(P, cell.A, r, m)
    t_odd = sum(caps[j] * cell.q[j] for j in range(1, n, 2))
    ts_odd = sum(caps[j] * cell.q[n - 2 - j] for j in range(1, n - 2, 2))
    return t_odd + ts_odd


def a0_of(P, r):
    from explore_equation_bound import big_u
    A = 2
    while big_u(P, r, A) >= 1:
        A += 1
    return A


def criterion_member(e, cell, m):
    """The identity-derived membership: Phi = -k N (k >= 0 integer)
    and q_{mP-1} | k (q_{mP} - 1) - w."""
    n = m * cell.P
    N = n_m(cell, m)
    phi = phi_of(e, cell)
    if phi > 0 or phi % N != 0:
        return False
    k = -phi // N
    return (k * (cell.q[n] - 1) - w_of(e, cell)) % cell.q[n - 1] == 0


def main():
    pairs = deep_pairs()
    print("deep pairs recomputed: %d" % len(pairs))
    print("  " + " ".join("(%d,%d)a=%d" % t for t in pairs))

    print("\ns0: controls")
    for (P, r, a) in pairs:
        cell = Cell(P, a)
        for m in range(2, 5):
            n = m * P
            g = gvec(cell, m)
            assert g[n - 1] == cell.q[n - 1]
            for j in range(0, n - 1):
                if j % 2 == 0:
                    assert g[n - 2 - j] == -g[j]
                else:
                    assert g[n - 2 - j] == g[j]
            comb = c1_pattern(P, m)  # aligned: 1 at even j
            assert sum(cj * g[j] for j, cj in enumerate(comb)) == 0
            allodd = [1 if j % 2 else 0 for j in range(n)]
            caps = aligned_caps(P, a, r, m)
            assert legal_cyclic(allodd, caps)
            d5 = cell.q[n - 1] + 2 * sum(cell.q[i]
                                         for i in range(1, n - 2, 2))
            assert sum(g[j] for j in range(1, n, 2)) == d5
    print("  g-reflection, D(comb) = 0, all-odd legal + closed form: OK")

    s0_cells = [(4, 2, 2, 2), (4, 2, 2, 3), (6, 2, 2, 2)]
    for (P, r, a, m) in s0_cells:
        cell = Cell(P, a)
        caps = aligned_caps(P, a, r, m)
        g = gvec(cell, m)
        pats = enum_legal_cyclic(caps)
        brute = max(sum(ej * g[j] for j, ej in enumerate(e))
                    for e in pats)
        val, arg = dp_max(g, caps)
        print("  (%d,%d) a=%d m=%d: %d legal patterns, brute max %d,"
              " DP max %d %s" % (P, r, a, m, len(pats), brute, val,
                                 "OK" if brute == val else "MISMATCH"))
        assert brute == val
        # N2: membership = criterion on every pattern
        agree = all(full_member(cell, r, d_of(e, r), m)
                    == criterion_member(e, cell, m) for e in pats)
        print("    full_member == identity criterion on all: %s"
              % ("OK" if agree else "MISMATCH"))
        assert agree
    val, arg = dp_max(gvec(Cell(4, 2), 2), aligned_caps(4, 2, 2, 2))
    print("  D4 hand witness: DP max at (4,2) a=2 m=2 = %d (hand 84)"
          % val)

    print("\ns1: the DP table — Dmax vs N_m, m = 2..30")
    verdicts = []
    for (P, r, a) in pairs:
        cell = Cell(P, a)
        worst = None
        for m in range(2, 31):
            g = gvec(cell, m)
            caps = aligned_caps(P, a, r, m)
            val, arg = dp_max(g, caps)
            N = n_m(cell, m)
            rat = val / N
            if worst is None or rat > worst[1]:
                worst = (m, rat, val, N)
        m_, rat, val, N = worst
        verdict = "CLOSED" if rat < 1 else "CROSSES"
        verdicts.append((P, r, a, verdict))
        print("  (%2d,%2d) a=%d: worst m=%2d Dmax=%d N_m=%d "
              "ratio=%.4f %s" % (P, r, a, m_, val, N, rat, verdict))
    n_closed = sum(1 for v in verdicts if v[3] == "CLOSED")
    print("  closed by legality alone: %d / %d" % (n_closed, len(pairs)))

    print("\ns0c: DP max == T_odd + T*_odd (the odd-support theorem)")
    checked = 0
    for (P, r, a) in pairs:
        cell = Cell(P, a)
        for m in range(2, 7):
            val, _ = dp_max(gvec(cell, m), aligned_caps(P, a, r, m))
            assert val == m_closed(cell, r, m), (P, r, a, m)
            checked += 1
    for (P, r) in even_cells(12):
        for a in range(2, 9):
            cell = Cell(P, a)
            for m in range(2, 5):
                val, _ = dp_max(gvec(cell, m),
                                aligned_caps(P, a, r, m))
                assert val == m_closed(cell, r, m), (P, r, a, m)
                checked += 1
    print("  closed form == DP at %d (cell, a, m) instances: OK"
          % checked)

    print("\ns1b: the strip certificate — every (P<=12, r, a<a_0), "
          "m = 1..40")
    all_ok = True
    for (P, r) in even_cells(12):
        a0 = a0_of(P, r)
        for a in range(2, a0):
            cell = Cell(P, a, top=41 * P + 2)
            tau = cell.q[P] + cell.p[P - 1]
            G = [n_m(cell, m) - m_closed(cell, r, m)
                 for m in range(1, 41)]        # G[i] = G_{i+1}
            dG = [G[i + 1] - G[i] for i in range(len(G) - 1)]
            # recursion base: least m with DeltaG_{m+1} = tau
            # DeltaG_m - DeltaG_{m-1} holding from there on
            rec_from = None
            for base in range(1, len(dG) - 1):
                if all(dG[i + 1] == tau * dG[i] - dG[i - 1]
                       for i in range(base, len(dG) - 1)):
                    rec_from = base + 1   # in m-units (dG[i] = DeltaG_{i+1})
                    break
            # handle: least m* with G>0 up to m*, dG_{m*}>0,
            # dG_{m*+1} >= dG_{m*}
            handle = None
            for i in range(1, len(dG) - 1):
                if (all(g > 0 for g in G[:i + 1]) and dG[i] > 0
                        and dG[i + 1] >= dG[i]):
                    handle = i + 1
                    break
            ok = (all(g > 0 for g in G) and rec_from is not None
                  and rec_from <= 5 and handle is not None
                  and handle >= rec_from)
            all_ok = all_ok and ok
            print("  (%2d,%2d) a=%2d: minG=%-12d rec from m=%s "
                  "handle m*=%s %s"
                  % (P, r, a, min(G),
                     rec_from, handle, "OK" if ok else "FAIL"))
    print("  strip certificate everywhere: %s"
          % ("YES" if all_ok else "NO"))

    print("\ns1c: the even P = 14..20 closed-form terrain")
    worst = None
    for P in range(14, 21, 2):
        for r in range(2, P, 2):
            a0 = a0_of(P, r)
            for a in list(range(2, 13)) + [a0]:
                cell = Cell(P, a)
                for m in range(1, 13):
                    rat = m_closed(cell, r, m) / n_m(cell, m)
                    if worst is None or rat > worst[0]:
                        worst = (rat, P, r, a, m)
    rat, P, r, a, m = worst
    print("  all M < N_m: worst ratio %.4f at (%d,%d) a=%d m=%d"
          % (rat, P, r, a, m) if rat < 1 else
          "  CROSSING at (%d,%d) a=%d m=%d ratio %.4f" % (P, r, a, m, rat))

    print("\ns2: argmax structure at m = 2..4")
    for (P, r, a) in pairs:
        cell = Cell(P, a)
        for m in range(2, 5):
            g = gvec(cell, m)
            caps = aligned_caps(P, a, r, m)
            val, arg = dp_max(g, caps)
            print("  (%2d,%2d) a=%d m=%d: Dmax=%-8d argmax %s"
                  % (P, r, a, m, val, "".join(str(x) for x in arg)))

    print("\ns3: k-level census (fires only on a crossing)")
    fired = False
    for (P, r, a, verdict) in verdicts:
        if verdict != "CROSSES":
            continue
        fired = True
        cell = Cell(P, a)
        for m in range(2, 31):
            g = gvec(cell, m)
            caps = aligned_caps(P, a, r, m)
            val, _ = dp_max(g, caps)
            N = n_m(cell, m)
            if val < N:
                continue
            if m * P > 26:
                print("  (%d,%d) a=%d m=%d: crossing beyond "
                      "enumeration reach (mP = %d) — NOT swept"
                      % (P, r, a, m, m * P))
                continue
            pats = enum_legal_cyclic(caps)
            hits = [e for e in pats
                    if phi_of(e, cell) < 0
                    and phi_of(e, cell) % N == 0]
            surv = [e for e in hits if criterion_member(e, cell, m)]
            print("  (%d,%d) a=%d m=%d: %d at negative multiples, "
                  "%d survive the k-level divisibility"
                  % (P, r, a, m, len(hits), len(surv)))
    if not fired:
        print("  no crossing — s3 idle")

    print("\ns4: full-enumeration cross-check (survivors = {0, comb})")
    for (P, r, a) in pairs:
        for m in (2, 3):
            if m == 3 and P > 6:
                continue
            if m * P > 26:
                print("  (%d,%d) a=%d m=%d: skipped (mP = %d too wide)"
                      % (P, r, a, m, m * P))
                continue
            cell = Cell(P, a)
            caps = aligned_caps(P, a, r, m)
            pats = enum_legal_cyclic(caps)
            members = [e for e in pats
                       if full_member(cell, r, d_of(e, r), m)]
            comb = tuple(c1_pattern(P, m))
            nonzero = [e for e in members if any(e)]
            ok = nonzero == [comb] or (not nonzero)
            print("  (%2d,%2d) a=%d m=%d: %6d legal, %d members, "
                  "nonzero survivors %s %s"
                  % (P, r, a, m, len(pats), len(members),
                     [e for e in nonzero if e != comb] or "= {comb}",
                     "OK" if ok and comb in members else "UNEXPECTED"))


if __name__ == "__main__":
    main()
