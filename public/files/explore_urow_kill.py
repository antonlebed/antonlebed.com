"""The u-row identity: does one exact linear identity tie the second
Cramer row to the first at EVERY period multiple, reducing the m >= 2
kill to a divisibility in the Ostrowski numeration?

THE QUESTION
------------
The even-P lattice-avoidance campaign stands at: every period-mP
congruence is an exact integer equation for A >= a_0(P, r)
(explore_equation_bound.py), the m = 1 solution set is killed by the
u-row read exactly in A (explore_congruence_kill.py F3-F4, an
OBSERVATION at 163 extras: num_u degenerates to a non-integral
rational multiple of N on every Phi = 0 solution), and the m >= 2
solution sets are open — the equation does not split per block. A
prior hand pass derived the u-row's aligned closed form; this probe
machine-checks it, machine-checks the exact identity the hand-attack
below sharpens it into, and reads whether that identity closes the
m >= 2 kill at probed cells.

THE HAND-ATTACK (pre-engine, on paper; conventions re-derived from
the engine: quotients 1-based with a_i = A iff i = 0 mod P else 1,
q_0 = 1, p_0 = 0, q_k = F_{k+1} and p_k = F_k for k <= P-1, caps
cap(k) = a_{k+1} with the class at k = P-1 mod P, aligned position
j = (k+r) mod mP, N_m = p_{mP-1} + q_{mP} - 2)
----------------------------------------------------------------------
D1  THE u-ROW'S CLOSED FORM (the scratch's Pass 4, restated). The
    u-row coefficient at aligned j is
        b_j = -p_j - (-1)^j K(a_{j+2}..a_{mP})   (mod N_m at wraps),
    by the q-side d'Ocagne q_{mP} p_j - p_{mP} q_j =
    -(-1)^j K(a_{j+2}..a_{mP}); and reversal sends a_{j+2}..a_{mP}
    to the A-FIRST rotated word (atilde_i = A iff i = 1 mod P), so
    K(a_{j+2}..a_{mP}) = qtilde_{mP-1-j} with qtilde the rotated
    window's denominators, qtilde_t = A F_t + F_{t-1} at t <= P.
D2  THE IDENTITY, PROVED FOR ALL m. Claim:
        q_{mP-1} b_j + q_j N_m + (q_{mP} - 1) chat_j = 0
    for every j = 0..mP-1 and every m >= 1 (chat_j =
    (-1)^j q_{mP-2-j} - q_j, the w-row's palindrome closed form).
    Proof: substitute D1 and chat; the sign-free part collapses by
    d'Ocagne (p_{mP-1} q_j - q_{mP-1} p_j = (-1)^j K_j with
    K_n := K(a_{j+2}..a_n)), leaving
        (-1)^j [q_{mP} K_{mP-1} - q_{mP-1} K_{mP}] = q_j;
    and G_n := q_n K_{n-1} - q_{n-1} K_n satisfies G_n = -G_{n-1}
    (both factors share the recursion), with base G_{j+1} =
    q_{j+1}*0 - q_j*1 = -q_j, so G_{mP} = (-1)^{mP-j-1} (-q_j) =
    (-1)^j q_j at even mP. QED. At m = 1 this is equivalent to the
    scratch's constancy statement F_P Psi = v N + (F_{P-1}-1) Phi
    (checked numerically at P = 4 and 6 pre-engine).
D3  THE KILL BECOMES A DIVISIBILITY. Summing D2 against digits:
        q_{mP-1} Psi_m = -w(d) N_m - (q_{mP} - 1) Phi_m,
    w(d) := sum_j d_j q_j (all-positive weights). On Phi_m = 0
    exactly (A >= a_0), Psi_m / N_m = -w/q_{mP-1}, so membership —
    N_m | Psi_m — is EXACTLY q_{mP-1} | w(d). The zero pattern has
    w = 0; the m-fold comb has w = sum_{even j} q_j = q_{mP-1}
    EXACTLY (class positions are odd at even P, so every even-j
    step is a Fibonacci step and the sum telescopes:
    q_{j+1} - q_{j-1} = q_j at even j). Both pass, as they must.
    This derives explore_congruence_kill.py F3 by hand: on ker Phi,
    num_u is the rational multiple -w/q_{mP-1} of N, non-integral
    iff q_{mP-1} does not divide w.
D4  THE LOWER MASS IS UNDER TWO TOP DENOMINATORS (scaffolding —
    superseded by the direct proof D6, which needs no mass bound;
    kept because s3/s3b verify it AT ITS SCOPE: the least A where it
    holds, m <= 6, NOT all A — the r = P-2 cells sit at ratio 1.99
    already at A = 2 and nothing here checks larger A). If
        T := sum_{j <= mP-2} cap_j q_j < 2 q_{mP-1},
    then for any legal d, w(d) = d_{mP-1} q_{mP-1} + (lower part)
    with lower part in [0, 2 q_{mP-1}), so q_{mP-1} | w forces the
    lower part to 0 or exactly q_{mP-1}: the kill reduces to a
    census of legal lower-digit representations of q_{mP-1}.
D5  THE CENSUS AS A MACHINE OBJECT. The census of legal lower
    representations of q_{mP-1} is this probe's test bed: the comb's
    lower part is one; the counts and the kernel members print per
    cell.
D6  THE CENSUS IS A THEOREM — proved after the first run printed
    (the machine showed the comb alone on ker Phi at all 13
    instances; the proof was then found on paper and s4 stands as
    its control). Claim: at every even P, even nonzero r, every
    a >= 2 and every m >= 1, a cap-respecting pattern d (0 <= d_j <=
    cap_j; legality NOT needed) with Phi_m(d) = 0 and
    q_{mP-1} | w(d) is the zero pattern or the m-fold comb.
    Proof: w = t q_{mP-1}, t >= 0. Phi_m = w* - w with
    w* := sum_j d_j (-1)^j q_{mP-2-j}, so w* = t q_{mP-1}. Every
    EVEN aligned position has cap 1: the class slots sit at
    j = r-1 mod P, odd since r is even and P is even. Hence
        t q_{mP-1} = w* <= sum_{even j <= mP-2} d_j q_{mP-2-j}
                       <= sum_{even j <= mP-2} q_{mP-2-j}
                        = q_{mP-1}
    — the last step the mirrored comb telescope (i = mP-2-j runs
    over the evens; q_{i+1} = q_i + q_{i-1} at even i since class
    quotient steps sit at odd i). So t <= 1. t = 0 forces d = 0
    (positive weights). t = 1 forces equality throughout: d_j = 0
    at every odd j <= mP-3 (their -q_{mP-2-j} terms must vanish),
    d_j = 1 at every even j <= mP-2, and then w = (1 + d_{mP-1})
    q_{mP-1} = q_{mP-1} pins the top digit to 0. The comb. QED.
    COROLLARY (with D3 and the equation bound): for a >= a_0(P, r),
    the even-P lattice-avoidance lemma holds at EVERY period
    multiple m >= 1 — and the m = 1 general-even-P classification
    is the same statement (the census argument reads verbatim at
    m = 1), so the extras' per-cell kills are one theorem.
D7  THE STRIP'S SHAPE UNDER THE IDENTITY. Below a_0 the congruence
    is not an equation, but on a member Phi_m = k N_m with
    k >= 1 impossible unconditionally (w* <= q_{mP-1} < N_m), so
    Phi_m is 0 or a NEGATIVE multiple of N_m; k <= -1 requires
    w >= |k| N_m - T*_odd with w <= T_full :=
    sum_{j <= mP-1} cap_j q_j and T*_odd :=
    sum_{odd j <= mP-3} cap_j q_{mP-2-j}. So wherever
        T_full + T*_odd < N_m,
    every member has Phi_m = 0 exactly and dies into {0, comb} by
    D6 — no equation bound needed at all. Worked check at (4, 2),
    a = 2, m = 2: T_full + T*_odd = 87 + 27 = 114 > N_2 = 96, so
    the DEEP strip is not closed by this inequality; where it
    crosses is s6's print.

PREDICTIONS, FIXED BEFORE THE RUN (observables)
  N1 (controls; red voids the run): the closed form b_j matches the
      engine's raw u-row coefficient exactly at non-wrap positions
      and mod N_m at wraps, at all 15 cells (even P <= 12, even
      nonzero r), m = 1..3, A in {7, 12}; qtilde_t = A F_t + F_{t-1}
      at t <= P; w(comb) = q_{mP-1} exactly at m = 1..4.
  N2 (the identity; proved on paper, red = derivation bug):
      q_{mP-1} b_j + q_j N_m + (q_{mP} - 1) chat_j = 0 at every j,
      all 15 cells, m = 1..4, A in {7, 12}.
  N3 (F3 re-derived): at m = 1, every one of the extras of
      explore_congruence_kill.py s1 (163 across the 15 cells,
      recomputed here) FAILS q_{P-1} | w(d); the zero pattern and C1
      pass; per-cell extra counts match the frozen 163 total.
  N4 (the lower-mass bound): T < 2 q_{mP-1} holds at m = 2..6 from
      an explicit a_1(P, r) on, a_1 read off the same monotone
      dominator machinery as a_0 — prediction: a_1 <= a_0 at every
      cell (the margin here is F_{P+1}/F_P < 2, far slacker than
      the equation bound's mass < 1).
  N5 (the census; honestly open): at the five m = 2 cells (4,2),
      (6,2), (6,4), (8,2), (8,4), the legal lower-digit
      representations of q_{2P-1}: count them, and count how many
      satisfy Phi_2 = 0. Prediction (open): the comb's lower part is
      the ONLY representation with Phi_2 = 0, killing every m = 2
      solution beyond zero and C1C1 for all A >= max(a_0, a_1); a
      second Phi_2 = 0 representation would name the exact obstacle.
  N6 (the cross-check): full enumeration of legal period-2P patterns
      against the exact criterion (Phi_2 = 0 and q_{2P-1} | w) vs
      the two-row full membership at A >= a_0: identical verdicts —
      (4,2) at A = 18, (6,2) and (6,4) at A = 12, (8,4) at A = 10.
  N7 (frozen AFTER the first full run s0-s5 printed, before s3b/s4b
      ran; the first run landed a_1 = 2 at every cell and the comb
      alone on Phi_m = 0 at every census): the MIRRORED mass bound
      T* = sum_{j <= mP-2} cap_j q_{mP-2-j} < 2 q_{mP-1} — which
      pins the top digit to 0 in any surviving pattern, since
      w*_low = (1+e) q_{mP-1} <= T* forces e = 0 — holds with
      a_1* = 2 at every cell, m = 2..6; and the census re-run at a
      SECOND A per cell (A+5) keeps the comb as the only Phi_m = 0
      representation.
  N8 (the census theorem's control; frozen after D6 was proved,
      before any further run): s4's counts and kernel members are
      unchanged (the theorem predicts them), and a direct check of
      the equality mechanism — the even-position mirrored caps sum,
      sum_{even j <= mP-2} q_{mP-2-j} = q_{mP-1} — passes at all 15
      cells, m = 1..4, A in {7, 12}.
  N9 (the strip table; honestly open, frozen before s6 ran): per
      cell and per a in 2..a_0-1, the least m-uniform verdict of
      T_full + T*_odd < N_m over m = 2..12: prediction — the
      inequality holds from a per-cell crossing a_2 < a_0 upward
      (shrinking the strip), fails in the deep strip (the (4,2)
      a = 2 hand check above), and the ratio
      (T_full + T*_odd)/N_m is monotone or stabilizing in m so the
      m-sweep verdict is trustworthy at scanned scope. (The sweep
      was widened from m <= 12 to m <= 30 after the first s6 print;
      verdicts unchanged.)

FINDINGS (run record at the end; every stage green, exact arithmetic)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1): b_j = -p_j - (-1)^j qtilde_{mP-1-j} matches
    the engine's raw u-row coefficient exactly at every non-wrap
    position and mod N_m at every wrap, at all 15 cells (even
    P <= 12, even nonzero r), m = 1..3, A in {7, 12};
    qtilde_t = A F_t + F_{t-1} at t <= P; w(comb) = q_{mP-1} exactly
    at m = 1..4 everywhere.
F2  THE IDENTITY IS EXACT EVERYWHERE (N2; theorem — proved by hand
    in D2 for every even-P window, every j, every m, and every A,
    by d'Ocagne plus the two-term recursion on
    G_n = q_n K_{n-1} - q_{n-1} K_n):
    q_{mP-1} b_j + q_j N_m + (q_{mP} - 1) chat_j = 0 at all 2800
    machine instances (15 cells x 2 A x m = 1..4 x all j). Its
    digit-summed form q_{mP-1} Psi_m = -w N_m - (q_{mP} - 1) Phi_m
    turns the second Cramer row into ONE divisibility: on
    Phi_m = 0, membership is exactly q_{mP-1} | w(d),
    w(d) = sum d_j q_j.
F3  THE 163 EXTRAS RE-DIE BY DIVISIBILITY (N3):
    explore_congruence_kill.py F3's per-extra rational-multiple kill
    is now the one statement q_{P-1} = F_P does not divide w(d) —
    verified at all 163 extras across the 15 cells (counts match
    cell for cell), with the comb landing w = F_P exactly. The
    observation "num_u degenerates to a rational multiple of N on
    ker Phi" is DERIVED: the multiple is -w/q_{mP-1}, at every m.
F4  THE MASS BOUNDS HOLD AT THEIR SCANNED SCOPE — AND ARE
    SCAFFOLDING (N4/N7 as frozen, rescoped): T = sum_{j<=mP-2}
    cap_j q_j < 2 q_{mP-1} and the mirrored T* hold AT a = 2 (the
    least a; a_1 = a_1* = 2), m = 2..6, every cell — T/q at a = 2,
    m = 2 runs 1.62..1.999 with the near-2 cells at r = P-2.
    Larger a was NOT swept, and the r = P-2 margins say the bound
    may cross 2 there; the question is MOOT for the chain, because
    the census theorem D6 needs no mass bound at all — D4's
    reduction survives only as the frame that pointed at the
    census.
F5  THE COMB IS THE ONLY KERNEL REPRESENTATION (N5 lands, N7's
    second-A re-run identical): at all 13 probed (cell, m, A) — the
    five m = 2 cells at A in {a_0-ish, +5}, m = 3 at (4,2) and
    (6,2) — the legal lower-digit representations of q_{mP-1}
    number 3..12, and EXACTLY ONE lies on Phi_m = 0: the m-fold
    comb, at every probed cell, both A values (census counts
    A-independent at the probed pairs except (8,2), 10 -> 12).
    (The audit's repair: the first census DFS re-appended a
    completed vector once per remaining level, so the counts first
    printed as 9..41 with only representations whose bottom digit
    is nonzero counted once; the kernel verdicts were untouched —
    duplication multiplies a solution, never hides one — and every
    kernel member, being the comb, was bottom-nonzero and printed
    once even then.)
F6  CRITERION = MEMBERSHIP, SURVIVORS = {0, C1C1} (N6): full
    enumeration at (4,2) A = 18, (6,2)/(6,4) A = 12, (8,4) A = 10
    (3362..55694 legal period-2P patterns) — the exact criterion
    (Phi_2 = 0 and q_{2P-1} | w) agrees with two-row membership on
    every pattern, and the nonzero survivors are exactly the doubled
    comb.
F7  THE CENSUS IS A THEOREM AND THE LEMMA CLOSES ABOVE THE
    THRESHOLD (D6, proved on paper after the first run; s4/s4b its
    controls, N8 green at 120 instances): at every even P, even
    nonzero r, every a >= 2 and every m >= 1, a cap-respecting
    pattern with Phi_m = 0 and q_{mP-1} | w is zero or the m-fold
    comb — one telescope inequality, no legality, no mass bound.
    With the identity (F2) and the equation bound
    (explore_equation_bound.py), the even-P lattice-avoidance lemma
    is a THEOREM at every even P and even nonzero residue for all
    a >= a_0(P, r), ALL period multiples at once; and the m = 1
    general-even-P classification is the same statement read at
    m = 1.
F8  THE STRIP COLLAPSES TO a = 2 (N9 lands; sweep m = 2..30,
    verdicts identical to the frozen m <= 12 first print): on a
    member below a_0, Phi_m is 0 or a negative multiple of N_m
    (positive multiples die on w* <= q_{mP-1} < N_m
    unconditionally), and T_full + T*_odd < N_m excludes the
    negative multiples at EVERY strip pair (P, r, a) except a = 2
    (all 15 cells) and a = 3 at (4, 2) — 16 open pairs, everything
    else in 2 <= a < a_0 closed at scanned m <= 30 (the
    inequality's two sides share the P-periodic recursion, so the
    per-m verdict stabilizes; a for-all-m dominator is the
    formalization owed). The worked failure at (4, 2), a = 2,
    m = 2 (114 > 96) says the deep pairs need legality or the box,
    not more of this inequality. (Settled: explore_deep_pairs.py —
    legality does it, the odd-support theorem cutting T_full to
    T_odd, and its DeltaG block-recursion certificate is the
    for-all-m dominator; every strip pair at P <= 12 is closed for
    all m.)

RUN RECORD: python explore_urow_kill.py — s0..s6, 0.5 s wall,
memory trivial, exit 0, run twice byte-identical after each
extension (the first run was s0..s5 without s3b/s4's second-A rows,
s4b and s6; each later widening matches the earlier prints on every
shared stage).

THE DESIGN
----------
Everything exact (integers end to end; the one float is s3's display
ratio). Cell
imported from explore_parity_derivation (convergents to depth 400);
raw/folded coefficients, caps, legality, membership and the m = 1
enumeration imported from explore_congruence_kill. s0 the controls
(closed form, qtilde, comb telescope); s1 the identity sweep; s2 the
m = 1 divisibility re-derivation over the recomputed extras; s3 the
lower-mass threshold table a_1(P, r) and s3b its mirrored twin
a_1*(P, r); s4 the lower-representation census at the five m = 2
cells (bounded DFS on the remaining sum, digits capped by legality
and by the remaining value), an m = 3 spot census at (4,2) and
(6,2), and the N7 re-run at a second A per cell; s4b the census
theorem's telescope control; s5 the full cross-check enumerations;
s6 the strip table (T_full + T*_odd vs N_m per strip pair,
m = 2..30). One command runs all; wall-clock estimate under two
minutes (the (8,4) enumeration at A = 10 dominates); memory
trivial.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell              # noqa: E402
from explore_congruence_kill import (                   # noqa: E402
    fibs, n_m, raw_coeffs, fold, caps_vec, legal, s_xy, full_member,
    c1_pattern, hand_c, even_cells, enum_legal)


def chat(cell, m):
    """chat_j = (-1)^j q_{mP-2-j} - q_j (the w-row closed form)."""
    n = m * cell.P
    q = cell.q
    return [((q[n - 2 - j] if n - 2 - j >= 0 else 0)
             * (1 if j % 2 == 0 else -1)) - q[j] for j in range(n)]


def qtilde(P, A, top):
    """Rotated (A-first) window denominators: atilde_i = A iff
    i = 1 mod P."""
    qt = [1]
    prev = 0
    for t in range(1, top + 1):
        at = A if (t - 1) % P == 0 else 1
        qt.append(at * qt[-1] + (qt[-2] if t >= 2 else prev))
    return qt


def bvec(cell, m, qt):
    """b_j = -p_j - (-1)^j qtilde_{mP-1-j}, j = 0..mP-1."""
    n = m * cell.P
    return [-cell.p[j] - (qt[n - 1 - j] if j % 2 == 0
                          else -qt[n - 1 - j]) for j in range(n)]


def raw_u(cell, r, m):
    """Engine u-row coefficient at digit k: contribution of theta_{k+r}
    to num_u = x(1 - q_{mP}) - p_{mP} y."""
    P = cell.P
    qm, pm = cell.q[m * P], cell.p[m * P]
    return [-cell.p[k + r] * (1 - qm) - pm * cell.q[k + r]
            for k in range(m * P)]


def w_of(d, cell):
    """w(d) = sum_j d_j q_j over ALIGNED positions j."""
    return sum(dj * cell.q[j] for j, dj in enumerate(d))


def aligned_digits(d, r, n):
    """Digit vector (positions k) -> aligned vector (positions
    j = (k+r) mod n)."""
    out = [0] * n
    for k, dk in enumerate(d):
        out[(k + r) % n] = out[(k + r) % n] + dk
    return out


def aligned_caps(P, A, r, m):
    """Caps carried to aligned positions: cap at j comes from digit
    k = (j-r) mod mP."""
    n = m * P
    caps = caps_vec(P, A, m)
    return [caps[(j - r) % n] for j in range(n)]


def rep_census(cell, r, m, target_lower_only=True):
    """All legal ALIGNED digit vectors d (lower positions j <= mP-2
    free, top position forced 0) with w(d) = q_{mP-1}. Legality is
    the cyclic cap-after-nonzero rule read on the DIGIT vector, i.e.
    unaligned; enumerate aligned, check legality after rotating
    back. DFS from the top weight down, pruned by remaining value
    and by the max remaining mass."""
    n = m * cell.P
    q = cell.q
    caps = aligned_caps(cell.P, cell.A, r, m)
    target = q[n - 1]
    suffix_max = [0] * (n + 1)          # max mass from positions < j
    for j in range(n - 1):
        suffix_max[j + 1] = suffix_max[j] + caps[j] * q[j]
    out = []
    vec = [0] * n

    def rec(j, rem):
        if rem == 0:
            # every position <= j is forced to 0: the vector is
            # complete as it stands, and recursing would re-append it
            d = [vec[(k + r) % n] for k in range(n)]
            if legal(d, caps_vec(cell.P, cell.A, m)):
                out.append(tuple(vec))
            return
        if j < 0 or rem < 0 or rem > suffix_max[j + 1]:
            return
        top = min(caps[j], rem // q[j])
        for v in range(top, -1, -1):
            vec[j] = v
            rec(j - 1, rem - v * q[j])
        vec[j] = 0

    rec(n - 2, target)
    assert len(out) == len(set(out))    # one emit per object
    return out


def phi_of(d_aligned, ch):
    return sum(dj * cj for dj, cj in zip(d_aligned, ch))


def main():
    print("s0: controls - closed form, qtilde, the comb telescope")
    F = fibs(60)
    for (P, r) in even_cells(12):
        for A in (7, 12):
            cell = Cell(P, A)
            qt = qtilde(P, A, 4 * P)
            for t in range(P + 1):
                assert qt[t] == A * F[t] + F[t - 1] if t >= 1 \
                    else qt[t] == 1, (P, A, t)
            for m in (1, 2, 3):
                n = m * P
                N = n_m(cell, m)
                b = bvec(cell, m, qt)
                ru = raw_u(cell, r, m)
                for k in range(n):
                    j = (k + r) % n
                    if k + r < n:
                        assert ru[k] == b[j], (P, r, A, m, k)
                    else:
                        assert (ru[k] - b[j]) % N == 0, (P, r, A, m, k)
            for m in (1, 2, 3, 4):
                comb = c1_pattern(P, m)
                assert w_of(comb, cell) == cell.q[m * P - 1], (P, A, m)
    print("  b_j closed form (exact off-wrap, mod N_m at wraps),")
    print("  qtilde_t = A F_t + F_{t-1}, w(comb) = q_{mP-1}:")
    print("  PASS at %d cells, m <= 4, A in {7, 12}"
          % len(even_cells(12)))

    print("s1: the identity  q_{mP-1} b_j + q_j N_m + (q_{mP}-1)"
          " chat_j = 0")
    checked = 0
    for (P, r) in even_cells(12):
        for A in (7, 12):
            cell = Cell(P, A)
            qt = qtilde(P, A, 5 * P)
            for m in (1, 2, 3, 4):
                n = m * P
                N = n_m(cell, m)
                b = bvec(cell, m, qt)
                ch = chat(cell, m)
                for j in range(n):
                    assert (cell.q[n - 1] * b[j] + cell.q[j] * N
                            + (cell.q[n] - 1) * ch[j]) == 0, \
                        (P, r, A, m, j)
                    checked += 1
    print("  PASS: %d (cell, A, m, j) instances, all exactly zero"
          % checked)

    print("s2: m = 1 divisibility - the 163 extras re-killed by"
          " q_{P-1} | w")
    total_extras = 0
    for (P, r) in even_cells(12):
        cell = Cell(P, 40)
        c = [fold(x, n_m(cell, 1)) for x in raw_coeffs(cell, r, 1)]
        class_pos = P - 1
        cc = abs(c[class_pos])
        rest = sum(abs(ck) for k, ck in enumerate(c) if k != class_pos)
        Ebound = rest // cc
        caps = caps_vec(P, Ebound + 2, 1)
        sols = [d for d in enum_legal(caps, class_pos, Ebound)
                if sum(ck * dk for ck, dk in zip(c, d)) == 0]
        c1 = tuple(c1_pattern(P, 1))
        zero = tuple([0] * P)
        extras = [d for d in sols if d not in (zero, c1)]
        killed = 0
        for d in extras:
            da = aligned_digits(list(d), r, P)
            w = w_of(da, cell)
            assert w % cell.q[P - 1] != 0, (P, r, d, w)
            killed += 1
        da_c1 = aligned_digits(list(c1), r, P)
        assert w_of(da_c1, cell) % cell.q[P - 1] == 0
        total_extras += killed
        print("  (P,r)=(%2d,%2d): %2d extras, all fail F_P | w;"
              " comb w = %d = F_P" % (P, r, killed,
                                      w_of(da_c1, cell)))
    print("  total extras re-killed: %d" % total_extras)

    print("s3: the lower-mass threshold a_1(P, r)  [T < 2 q_{mP-1}]")
    for (P, r) in even_cells(12):
        a1 = None
        for A in range(2, 200):
            cell = Cell(P, A)
            ok = True
            for m in range(2, 7):
                n = m * P
                caps = aligned_caps(P, A, r, m)
                T = sum(caps[j] * cell.q[j] for j in range(n - 1))
                if T >= 2 * cell.q[n - 1]:
                    ok = False
                    break
            if ok:
                a1 = A
                break
        cell = Cell(P, max(a1, 2))
        print("  (P,r)=(%2d,%2d): a_1 = %d  (T/q ratio at m=2, A=a_1:"
              " %.3f)" % (P, r, a1,
                          sum(aligned_caps(P, a1, r, 2)[j]
                              * cell.q[j] for j in range(2 * P - 1))
                          / cell.q[2 * P - 1]))

    print("s3b: the mirrored-mass threshold a_1*(P, r)"
          "  [T* < 2 q_{mP-1}]")
    for (P, r) in even_cells(12):
        a1s = None
        for A in range(2, 200):
            cell = Cell(P, A)
            ok = True
            for m in range(2, 7):
                n = m * P
                caps = aligned_caps(P, A, r, m)
                Ts = sum(caps[j] * cell.q[n - 2 - j]
                         for j in range(n - 1))
                if Ts >= 2 * cell.q[n - 1]:
                    ok = False
                    break
            if ok:
                a1s = A
                break
        print("  (P,r)=(%2d,%2d): a_1* = %d" % (P, r, a1s))

    print("s4: the lower-representation census (w = q_{mP-1}, top"
          " digit 0)")
    for (P, r, m, A) in ((4, 2, 2, 18), (6, 2, 2, 12), (6, 4, 2, 12),
                         (8, 2, 2, 10), (8, 4, 2, 10),
                         (4, 2, 3, 18), (6, 2, 3, 12),
                         (4, 2, 2, 23), (6, 2, 2, 17), (6, 4, 2, 17),
                         (8, 2, 2, 15), (8, 4, 2, 15),
                         (4, 2, 3, 23)):
        cell = Cell(P, A)
        reps = rep_census(cell, r, m)
        ch = chat(cell, m)
        on_kernel = [d for d in reps if phi_of(d, ch) == 0]
        comb_aligned = tuple(aligned_digits(c1_pattern(P, m), r,
                                            m * P))
        print("  (P,r)=(%d,%d) m=%d A=%2d: %3d representations, "
              "%d on Phi_m = 0" % (P, r, m, A, len(reps),
                                   len(on_kernel)))
        for d in on_kernel:
            tag = "  <- the comb" if d == comb_aligned else \
                  "  <- NOT the comb"
            print("      %s%s" % (d, tag))

    print("s5: cross-check - exact criterion vs full membership")
    for (P, r, A) in ((4, 2, 18), (6, 2, 12), (6, 4, 12),
                      (8, 4, 10)):
        cell = Cell(P, A)
        m = 2
        n = m * P
        caps = caps_vec(P, A, m)
        ch = chat(cell, m)
        agree = 0
        crit_surv = []

        def rec_enum(k, vec):
            nonlocal agree
            if k == n:
                d = list(vec)
                if not legal(d, caps):
                    return
                da = aligned_digits(d, r, n)
                crit = (phi_of(da, ch) == 0
                        and w_of(da, cell) % cell.q[n - 1] == 0)
                full = full_member(cell, r, d, m)
                assert crit == full, (P, r, A, d)
                agree += 1
                if crit and any(d):
                    crit_surv.append(tuple(d))
                return
            top = caps[k]
            if k > 0 and vec[k - 1] != 0:
                top = min(top, caps[k] - 1)
            for v in range(top + 1):
                vec[k] = v
                rec_enum(k + 1, vec)
            vec[k] = 0
        rec_enum(0, [0] * n)
        comb = tuple(c1_pattern(P, m))
        print("  (P,r)=(%d,%d) A=%2d: %7d legal patterns, verdicts"
              " identical; nonzero survivors: %s"
              % (P, r, A, agree,
                 ["C1C1" if s == comb else s for s in crit_surv]))

    print("s4b: the census theorem's equality mechanism (N8)")
    checked = 0
    for (P, r) in even_cells(12):
        for A in (7, 12):
            cell = Cell(P, A)
            for m in (1, 2, 3, 4):
                n = m * P
                assert sum(cell.q[n - 2 - j] for j in range(0, n - 1, 2)
                           ) == cell.q[n - 1], (P, r, A, m)
                checked += 1
    print("  mirrored even-caps sum = q_{mP-1}: PASS at %d instances"
          % checked)

    print("s6: the strip table - where T_full + T*_odd < N_m closes"
          " the cell (m = 2..30)")
    from explore_equation_bound import big_u
    a0 = {}
    for (P, r) in even_cells(12):
        A = 2
        while big_u(P, r, A) >= 1:
            A += 1
        a0[(P, r)] = A                  # recomputed, never copied
    for (P, r) in even_cells(12):
        verdicts = []
        for A in range(2, a0[(P, r)]):
            cell = Cell(P, A)
            worst = 0.0
            ok = True
            for m in range(2, 31):
                n = m * P
                caps = aligned_caps(P, A, r, m)
                Tf = sum(caps[j] * cell.q[j] for j in range(n))
                Tso = sum(caps[j] * cell.q[n - 2 - j]
                          for j in range(1, n - 2, 2))
                N = n_m(cell, m)
                ratio = (Tf + Tso) / N
                worst = max(worst, ratio)
                if Tf + Tso >= N:
                    ok = False
            verdicts.append((A, ok, worst))
        closed = [A for (A, ok, _) in verdicts if ok]
        open_ = [A for (A, ok, _) in verdicts if not ok]
        print("  (P,r)=(%2d,%2d) a_0=%2d: closed a: %s | still open"
              " a: %s" % (P, r, a0[(P, r)],
                          closed if closed else "none",
                          open_ if open_ else "none"))

    print("ALL STAGES GREEN")


if __name__ == "__main__":
    main()
