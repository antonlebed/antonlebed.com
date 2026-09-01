"""The odd-P mass bound: does the m = 2 bound Dmax < N_2 fall on paper,
and how far does the charging bound reach?

THE QUESTION
------------
At odd P, even nonzero residue r, the mass step Dmax < N_m is what
blocks the odd-P lattice-avoidance theorem (explore_odd_transfer.py,
explore_weave.py). The aimed move was the m = 2 bound from the
weave's closed form; the hand-attack found two stronger routes and
this rig referees both:
  (a) THE CHARGING BOUND. The even-P odd-support theorem's charging
      argument (TRANSPLANT, flagged: explore_deep_pairs.py) transports
      to odd P with a remainder: for even j, g_j < g_{j+1} strictly,
      and legality right-charges every supported even position EXCEPT
      that an even CLASS SLOT (cap A) overflows its unit charge. So
      for EVERY m:  Dmax <= V0 + U_m,
      U_m = sum over even class slots s of [A g_s - g_{s+1}]_+ .
      At m = 2 there is ONE even slot s = P+r-1 and the hand
      derivation gives N_2 - V0 - [U]_+ > 0 in closed form — the
      m = 2 mass step would be a THEOREM with no weave form consumed.
  (b) THE POSITIVE-MULTIPLE THEOREM. w*(e) = sum e_j (-1)^j q_{n-2-j}
      maximizes at the all-even-support-at-cap pattern (odd h < 0,
      all-even is legal at full caps), giving a closed sum; the
      telescope identity q_{n-1} = 1 + sum_{i<=n-3} q_i +
      (A-1) sum_v q_{vP-1} plus the odd-sum bound
      sum_{odd i<=K} q_i <= q_{K+1} - 1 give
      w* <= q_{n-1} - (A-1)m/2 <= q_{n-1} - 1 < N_m at EVERY m —
      the measured-only bound of explore_odd_transfer s1b would be a
      theorem.

THE HAND-ATTACK (pre-engine, on paper; index
conventions re-derived from the engine: a_j = A iff j = 0 mod P,
cap_j = A iff j = r-1 mod P, g_j = q_j - (-1)^j q_{n-2-j}, legality
cap-1 after a nonzero; F_{-1} = 1, F_{-2} = -1)
----------------------------------------------------------------------
With Q = q_P = A F_P + F_{P-1}, R = p_P = A F_{P-1} + F_{P-2}, and
s = P+r-1 the one even slot at m = 2:
  V0  = 2[(F_P-1) + F_{P-1}Q + (F_{P-2}-1)F_P] + F_P Q + F_{P-1}F_P
        + (A-1)[F_r + F_{P-r}Q + F_{P-r-1}F_P]
  N_2 = F_P R + F_{P-1}^2 + A(F_P Q + F_{P-1}F_P) + F_{P-1}Q
        + F_{P-2}F_P - 2
  G   = N_2 - V0 = Q[(A-1)(F_P - F_{P-r}) - F_{P-1}]
        + F_P[(A-1)(F_{P-1} - F_{P-r-1}) + A F_{P-1}]
        + F_{P-1}^2 - (A-1)F_r
  U   = A g_s - g_{s+1} = (A F_r - F_{r+1})Q + (A F_{r-1} - F_r)F_P
        - A F_{P-r} - F_{P-r-1}
  gain (the weave F5 formula at m = 2, where jmin = P+3 with the
  exact tie delta_{P+1} = 0, so u = P+3 always)
      = [(A-2)F_r - 1]Q + (A-2)F_{r-1}F_P - (A-2)F_{P-r} - F_{P-1};
  at A = 2, gain = -Q - F_{P-1} < 0 (the 0-of-45 A = 2 observation as
  a consequence).
  gapU = G - U = B'_Q Q + B'_F F_P + T',
    B'_Q = (A-2)(F_P - F_{P-r} - F_r) + (F_{P-2} - F_{P-r} - F_{r-2})
    B'_F = (A-1)(F_{P-1} - F_{P-r-1}) + A(F_{P-1} - F_{r-1}) + F_r
    T'   = F_{P-1}^2 + A F_{P-r} + F_{P-r-1} - (A-1)F_r
  and the endpoint lemma F_K >= F_s + F_{K-s} makes B'_Q >= 0,
  B'_F > 0, with B'_F F_P covering T's negative part; G > 0 the same
  way. Worked check (3,2): G = 2A^2-2, U = (A-2)(Q+1),
  gain = (A-3)(Q+1), gapU = 2A+2, G - gain = 4A+4 = the recorded gap.
THE GENERAL-m TELESCOPING (the proof s4 referees): x_m = q_{mP},
y_m = q_{mP-1}, (u, v) the p-side twins; transport y_{m+1} =
F_P x_m + F_{P-1} y_m, x_{m+1} = Q x_m + B y_m, B = A F_{P-1} +
F_{P-2}. The mirror-free majorant Ubar_m = sum_{t odd <= m-1}
[(A-1) q_{tP+r-1} - q_{tP+r-2}] >= U_m termwise (A g_s - g_{s+1}
<= (A-1)q_s - q_{s-1}, always positive), and Lambda_m = N_m - V0_m
- Ubar_m telescopes exactly: Lambda_2 = B'_Q Q + B'_F F_P +
F_{P-1}^2 - (A-1)F_r > 0 (the same two brackets), and
  Lambda_{m+2} - Lambda_m = B'_Q x_{m+1} + (B - c) y_{m+1}
    - (2F_P - 1 + (A-1)F_r) x_m - (1 + 2F_{P-1} + (A-1)F_{r-1}) y_m
    + v_{m+2} - v_m,
  B - c = (A-1)E' - F_{P-2} + F_{r-2} + 2 >= 1,
  E' = F_{P-1} - F_{P-r-1} - F_{r-1} >= 0 (P = 3: E' = 0 direct).
Positivity: at P >= 5 use v_{m+2} >= q_{(m+2)P-3} = F_{P-2}x_{m+1}
+ F_{P-3}y_{m+1} and v_m <= y_m (p_k >= q_{k-2} and p_k < q_k, both
by the shared recurrence); substituting the transports, the x_m
coefficient is >= A F_{P-2}F_P - (A-1)F_r + F_{P-2}F_{P-1} +
(F_{P-3}-1)F_P + 1 > 0 and the y_m coefficient is >=
A F_{P-2}F_{P-1} - (A-1)F_{r-1} + F_{P-2}^2 - 2 + (F_{P-3}-1)F_{P-1}
> 0 (F_r <= F_{P-1} <= F_{P-2}F_P; F_{r-1} <= F_{P-2}). At P = 3
(r = 2) keep the p-side exact: the increment equals
(4A+4)u_m + (2A+1)v_m - A x_m - (A+1)y_m, positive by u_m >= A v_m,
(2A+1)v_m >= A y_m, x_m <= (A+1)y_m and 2A^3 + A^2 - 3A - 1 > 0 at
A >= 2. So Lambda_m > 0 at every even m: the charging bound clears
N_m everywhere.

FINDINGS (all stages green; run twice byte-identical, 25 lines;
record at the end)
----------------------------------------------------------------------
F1  THE CLOSED FORMS ARE EXACT (s0, all pass): V0, N_2, G, U, gain
    and the gapU decomposition each equal their engine numeric at
    every cell P <= 41, r even, A in {2, 3, 8, 64}; jmin = P + 3
    with the exact tie delta_{P+1} = 0 at every odd cell (the (7,6)
    m = 2 boundary tie is the j = P+1 tie, now derived: for even j
    the step is delta_j = q_{j-2} - q_{2P-j}, zero exactly at
    j = P+1, positive from P+3); and DP == V0 + [gain]_+ (the weave
    form) at odd_cells(13) x A in {2, 3, 8}.
F2  THE m = 2 MASS BOUND IS A THEOREM (s1, all pass; proof in the
    hand-attack above, machine-refereed leg by leg): G > 0,
    B'_Q >= 0, B'_F > 0, gapU > 0, U >= gain at every (P, r, A)
    with P <= 101, A <= 257 (minima: G = gapU = 6, B'_Q = 0,
    B'_F = 2, U - gain = 6, all at (3, 2, 2)), and DP Dmax <=
    V0 + [U]_+ < N_2 at every DP instance. At A = 2 the weave gain
    is -Q - F_{P-1} < 0: Dmax = V0 exactly, the recorded 0-of-45
    observation now derived. The recorded (3,2) gap 4a+4 is
    gapU + (U - gain) = (2A+2) + (Q+1).
F3  THE POSITIVE-MULTIPLE BOUND IS A THEOREM AT EVERY m (s2, all
    pass): DP max w* equals the all-even-at-cap closed sum at every
    (P, r, A, m) swept, and the slack q_{n-1} - w*max >= (A-1)m/2,
    minimum 1 at (3, 2, 2, 2) — exactly the telescope-minus-odd-sum
    prediction. w* <= q_{n-1} - 1 < N_m: positive multiples die,
    all m, all A, no legality consumed beyond digit bounds.
F4  THE CHARGING BOUND HOLDS AT EVERY m (s3): DP Dmax <= V0 + U_m
    <= V0 + Ubar_m at all 270 instances (m to 12), and BOTH margins
    stay positive everywhere — min Gamma_m = N_m - V0 - U_m and min
    Lambda_m = N_m - V0 - Ubar_m sit at (3, 2, 2) for every m and
    GROW (6/4 at m = 2, 168/164 at m = 4, ... 3.4e8 at m = 12): the
    crude mirror-free majorant is enough; no weave gain needed.
F5  THE GENERAL-m CLOSURE IS A THEOREM (s4, all pass): every
    algebraic step of the Lambda telescoping machine-checked exactly
    at P <= 31, A <= 64 — p_k >= q_{k-2} and p_k < q_k (the first
    cut ALSO asserted q_k - p_k >= q_{k-2} and the rig killed it:
    false from k = P+2 on, the A-step boosts q - p by only F_{P-2};
    the proof consumes only p < q), E, E', B'_Q >= 0, B - c_{y1} >= 1,
    Lambda_2 == B'_Q Q + B'_F F_P + F_{P-1}^2 - (A-1)F_r, the
    increment identity Lambda_{m+2} - Lambda_m == B'_Q x_{m+1} +
    (B - c_{y1}) y_{m+1} - (2F_P - 1 + (A-1)F_r) x_m -
    (1 + 2F_{P-1} + (A-1)F_{r-1}) y_m + v_{m+2} - v_m EXACT at every
    instance with every increment positive, and the P = 3 psi chain
    (u_m >= A v_m, (2A+1)v_m >= A y_m, x_m <= (A+1)y_m, psi_m > 0).
    CONCLUSION: Dmax <= V0 + U_m <= V0 + Ubar_m < N_m at every odd
    P, even nonzero r, A >= 2, every even m — the whole odd-P mass
    step is a THEOREM. With F3 and the congruence layer + u-row
    identity (already theorems), every legal cyclic pattern has
    Phi_m strictly between -N_m and N_m, so membership at odd P,
    even r, even m collapses to Phi_m = 0 and the census
    divisibility q_{mP-1} | sum d_j q_j.
F6  THE CENSUS PINCH — THE ODD-P EVEN-RESIDUE HALF CLOSES WHOLE
    (audit round; a pure composition of F3 with the chain, no new
    computation — the even-P census proof pinches w* = t q_{mP-1}
    against the mirrored-caps sum, which at even P EQUALS q_{mP-1},
    leaving the t = 1 comb; at odd P F3's bound is STRICT, so the
    pinch leaves nothing): a member has Phi_m = 0, hence w* = w,
    and the divisibility gives w = t q_{mP-1} with t >= 0; but
    w* <= q_{mP-1} - 1 (F3, cap-respecting suffices), so t = 0,
    w = 0, and every digit is 0. NO nonzero pattern is a member:
    the odd-P lattice-avoidance statement at even nonzero residues
    and even period multiples is a THEOREM at every odd P and every
    A >= 2 — the acyclicity reading proved, strictly deeper than
    even P's {0, comb}, and the enumerated 12-cell zero-only census
    (explore_odd_transfer.py F7) its corollary rather than its
    evidence. What stays open at odd P: the ODD period multiples
    (mP odd — the congruence layer itself does not exist there;
    SETTLED by explore_odd_doubling.py — a period-mP pattern is a
    period-2mP pattern with the same tail value, so this theorem at
    2m closes them, and only the odd residues survive as open) and
    the odd residues (non-comb cycles recorded).

PREDICTIONS (frozen before the run; observables)
  N1 (controls; red voids the run): every m = 2 closed form above
      equals its engine numeric (V0, N_2, G, U, gain, and the gapU
      decomposition) at every swept cell; jmin = P+3 and
      delta_{P+1} = 0 at every odd cell m = 2; DP Dmax ==
      V0 + [gain]_+ (the weave form, the known observation) at the
      DP sweep.
  N2 (the m = 2 theorem legs): at every swept (P, r, A): G > 0,
      B'_Q >= 0, B'_F > 0, gapU > 0, U >= gain, DP Dmax <=
      V0 + [U]_+, and DP Dmax < N_2. Exceptions printed with
      witnesses. Minima printed.
  N3 (the positive-multiple theorem): DP max of w* over legal cyclic
      patterns equals the all-even closed sum at every swept
      (P, r, A, m), and the slack q_{n-1} - w*max >= (A-1)m/2 >= 1.
      Exceptions printed.
  N4 (the general-m frontier; genuinely open): the sign of
      Gamma_m = N_m - V0_m - U_m printed per instance, plus DP
      Dmax <= V0_m + U_m checked. The kill-shape observable for
      extending the charging route to all even m is a printed
      negative Gamma_m; its meaning is weighed after the run.

THE DESIGN
----------
Everything exact (integers end to end). Cell/caps/g/DP imported from
the shipped rigs, not re-implemented. Stages:
  s0  N1 controls: closed forms vs numerics, wide (P <= 41, r even,
      A in {2, 3, 8, 64}); jmin/tie; DP == V0 + [gain]_+ at
      odd_cells(13) x A in {2, 3, 8}.
  s1  N2 legs: positivity + DP bounds at the DP sweep; closed-form
      positivity alone swept wide (P <= 101, A up to 257).
  s2  N3: w* DP vs closed sum and slack, odd_cells(11) x
      A in {2, 3, 8} x m in {2, 4, ..., 12}.
  s3  N4: Gamma_m sign trend over the same sweep, minima per m
      printed, and the s2/s3 sweep's DP charging check; plus the
      mirror-free majorant Ubar_m and its margin Lambda_m (added
      after the first run — see the run record).
  s4  the Lambda telescoping refereed step by step (added after
      s3's read made it the proof route): the p/q lemmas, the
      brackets, the Lambda_2 closed form, the exact increment
      identity, the P = 3 psi chain (P <= 31, A <= 64, m to 10).
One command runs all; wall-clock estimate under a minute; memory
trivial.

RUN RECORD
----------
python explore_odd_m2_bound.py — all stages, < 5 s wall, memory
trivial, exit 0, run twice byte-identical (25 lines). The first cut
of gain_num raised StopIteration at P = 3 (no even j in the window
has delta_j > 0 there; jmin = P+3 = n is the formula's value, made
the explicit default). s3's Lambda column and the whole of s4 were
added after the first full run: s3's read showed Gamma_m > 0
everywhere, which made the mirror-free majorant the proof route, and
s4 referees that derivation; s4's first cut carried the over-stated
lemma q_k - p_k >= q_{k-2} and the run killed it (F5) — the hand
derivation and the check were corrected to what the proof consumes. The
recorded runs are of the final rig.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell                    # noqa: E402
from explore_congruence_kill import n_m                       # noqa: E402
from explore_deep_pairs import aligned_caps, gvec, dp_max     # noqa: E402
from explore_odd_transfer import odd_cells, class_slots       # noqa: E402


# ---------------------------------------------------------------- fib

_FCACHE = {-2: -1, -1: 1, 0: 0, 1: 1}


def fib(k):
    if k in _FCACHE:
        return _FCACHE[k]
    a, b = 0, 1
    i = 1
    while i < k:
        a, b = b, a + b
        i += 1
    _FCACHE[k] = b
    return b


# ------------------------------------------------------- closed forms

def closed_m2(P, r, A):
    """All m = 2 closed forms; returns a dict of exact integers."""
    F = fib
    Q = A * F(P) + F(P - 1)
    R = A * F(P - 1) + F(P - 2)
    v0 = (2 * ((F(P) - 1) + F(P - 1) * Q + (F(P - 2) - 1) * F(P))
          + F(P) * Q + F(P - 1) * F(P)
          + (A - 1) * (F(r) + F(P - r) * Q + F(P - r - 1) * F(P)))
    n2 = (F(P) * R + F(P - 1) ** 2 + A * (F(P) * Q + F(P - 1) * F(P))
          + F(P - 1) * Q + F(P - 2) * F(P) - 2)
    g = (Q * ((A - 1) * (F(P) - F(P - r)) - F(P - 1))
         + F(P) * ((A - 1) * (F(P - 1) - F(P - r - 1)) + A * F(P - 1))
         + F(P - 1) ** 2 - (A - 1) * F(r))
    u = ((A * F(r) - F(r + 1)) * Q + (A * F(r - 1) - F(r)) * F(P)
         - A * F(P - r) - F(P - r - 1))
    gain = (((A - 2) * F(r) - 1) * Q + (A - 2) * F(r - 1) * F(P)
            - (A - 2) * F(P - r) - F(P - 1))
    bq = ((A - 2) * (F(P) - F(P - r) - F(r))
          + (F(P - 2) - F(P - r) - F(r - 2)))
    bf = ((A - 1) * (F(P - 1) - F(P - r - 1))
          + A * (F(P - 1) - F(r - 1)) + F(r))
    tp = F(P - 1) ** 2 + A * F(P - r) + F(P - r - 1) - (A - 1) * F(r)
    return dict(Q=Q, V0=v0, N2=n2, G=g, U=u, gain=gain,
                BQ=bq, BF=bf, TP=tp)


# ------------------------------------------------------ engine-side

def v0_num(cell, r, m):
    n = m * cell.P
    caps = aligned_caps(cell.P, cell.A, r, m)
    g = gvec(cell, m)
    return sum(caps[j] * g[j] for j in range(1, n, 2))


def u_m_num(cell, r, m):
    """The charging remainder: sum over even class slots of
    [A g_s - g_{s+1}]_+ (engine numerics)."""
    n = m * cell.P
    g = gvec(cell, m)
    tot = 0
    for s in class_slots(cell.P, r, m):
        if s % 2 == 0:
            tot += max(0, cell.A * g[s] - g[(s + 1) % n])
    return tot


def gain_num(cell, r, m):
    """The weave F5 formula, engine numerics (m = 2 use)."""
    P, A = cell.P, cell.A
    n = m * P
    g = gvec(cell, m)
    s = P + r - 1
    jmin = next((j for j in range(2, n - 1, 2) if g[j] > g[j - 1]),
                P + 3)   # P = 3: the window has no such j; P+3 = n
                         # is the formula's value, past every even j
    u = max(s - P + 3, jmin)
    tot = A * g[s] - g[s - 1] - g[s + 1]
    for j in range(u, s - 1, 2):
        tot += g[j] - g[j - 1]
    return tot, jmin


def wstar_dp(cell, r, m):
    """DP max of w*(e) over legal cyclic e."""
    n = m * cell.P
    q = cell.q
    h = [(q[n - 2 - j] if n - 2 - j >= 0 else 0) * (1 if j % 2 == 0
         else -1) for j in range(n)]
    caps = aligned_caps(cell.P, cell.A, r, m)
    val, _ = dp_max(h, caps)
    return val


def wstar_closed(cell, r, m):
    """The all-even-at-cap sum."""
    n = m * cell.P
    q = cell.q
    tot = sum(q[n - 2 - j] for j in range(0, n - 1, 2))
    tot += (cell.A - 1) * sum(
        q[n - 2 - s] for s in class_slots(cell.P, r, m) if s % 2 == 0)
    return tot


# ---------------------------------------------------------------- stages

def s0():
    print("== s0: N1 controls ==")
    bad = 0
    # closed forms vs numerics, wide
    for P in range(3, 42, 2):
        for r in range(2, P, 2):
            for A in (2, 3, 8, 64):
                cell = Cell(P, A, top=2 * P + 4)
                c = closed_m2(P, r, A)
                nv0 = v0_num(cell, r, 2)
                nn2 = n_m(cell, 2)
                gnum, jmin = gain_num(cell, r, 2)
                g2 = gvec(cell, 2)
                checks = [
                    ("V0", c["V0"], nv0),
                    ("N2", c["N2"], nn2),
                    ("G", c["G"], nn2 - nv0),
                    ("U", c["U"], A * g2[P + r - 1] - g2[P + r]),
                    ("gain", c["gain"], gnum),
                    ("gapU", c["G"] - c["U"],
                     c["BQ"] * c["Q"] + c["BF"] * fib(P) + c["TP"]),
                    ("jmin", P + 3, jmin),
                    ("tie", 0, g2[P + 1] - g2[P]),
                ]
                for name, a, b in checks:
                    if a != b:
                        bad += 1
                        print(f"  FAIL {name} ({P},{r}) A={A}: "
                              f"closed {a} != num {b}")
    print(f"  closed forms, jmin = P+3, tie at P+1: "
          f"{'all pass' if bad == 0 else f'{bad} FAIL'}")
    # DP == V0 + [gain]_+ (the weave form control)
    bad = 0
    for (P, r) in odd_cells(13):
        for A in (2, 3, 8):
            cell = Cell(P, A)
            dmax, _ = dp_max(gvec(cell, 2), aligned_caps(P, A, r, 2))
            gnum, _ = gain_num(cell, r, 2)
            if dmax != v0_num(cell, r, 2) + max(0, gnum):
                bad += 1
                print(f"  FAIL weave-form ({P},{r}) A={A}: "
                      f"DP {dmax} != V0+[gain]+")
    print(f"  DP == V0 + [gain]_+ (weave form): "
          f"{'all pass' if bad == 0 else f'{bad} FAIL'}")


def s1():
    print("== s1: N2 - the m = 2 theorem legs ==")
    bad = 0
    minima = {"G": None, "gapU": None, "BQ": None, "BF": None,
              "U-gain": None}

    def note(key, val, wit):
        if minima[key] is None or val < minima[key][0]:
            minima[key] = (val, wit)

    for P in range(3, 102, 2):
        for r in range(2, P, 2):
            for A in (2, 3, 8, 64, 257):
                c = closed_m2(P, r, A)
                wit = (P, r, A)
                note("G", c["G"], wit)
                note("gapU", c["G"] - c["U"], wit)
                note("BQ", c["BQ"], wit)
                note("BF", c["BF"], wit)
                note("U-gain", c["U"] - c["gain"], wit)
                if (c["G"] <= 0 or c["G"] - c["U"] <= 0 or c["BQ"] < 0
                        or c["BF"] <= 0 or c["U"] < c["gain"]):
                    bad += 1
                    print(f"  POSITIVITY FAIL {wit}: {c}")
                if A == 2 and c["gain"] >= 0:
                    bad += 1
                    print(f"  A=2 gain not negative {wit}")
    for k, v in minima.items():
        print(f"  min {k} = {v[0]} at {v[1]}")
    print(f"  wide positivity sweep (P <= 101, A <= 257): "
          f"{'all pass' if bad == 0 else f'{bad} FAIL'}")
    bad = 0
    for (P, r) in odd_cells(13):
        for A in (2, 3, 8, 64):
            cell = Cell(P, A)
            dmax, _ = dp_max(gvec(cell, 2), aligned_caps(P, A, r, 2))
            c = closed_m2(P, r, A)
            if dmax > c["V0"] + max(0, c["U"]):
                bad += 1
                print(f"  CHARGE FAIL ({P},{r}) A={A}")
            if dmax >= c["N2"]:
                bad += 1
                print(f"  BOUND FAIL ({P},{r}) A={A}")
    print(f"  DP <= V0 + [U]_+ and DP < N_2 at odd_cells(13) x "
          f"A in (2,3,8,64): {'all pass' if bad == 0 else 'FAIL'}")


def s2():
    print("== s2: N3 - the positive-multiple theorem ==")
    bad = 0
    minslack = None
    for (P, r) in odd_cells(11):
        for A in (2, 3, 8):
            cell = Cell(P, A)
            for m in range(2, 13, 2):
                wdp = wstar_dp(cell, r, m)
                wcl = wstar_closed(cell, r, m)
                slack = cell.q[m * P - 1] - wcl
                floor = (A - 1) * m // 2
                if wdp != wcl:
                    bad += 1
                    print(f"  FAIL w* dp {wdp} != closed {wcl} "
                          f"({P},{r}) A={A} m={m}")
                if slack < floor:
                    bad += 1
                    print(f"  FAIL slack {slack} < {floor} "
                          f"({P},{r}) A={A} m={m}")
                if minslack is None or slack < minslack[0]:
                    minslack = (slack, (P, r, A, m))
    print(f"  min slack q_(n-1) - w*max = {minslack[0]} at "
          f"{minslack[1]}")
    print(f"  w* closed sum + slack floor: "
          f"{'all pass' if bad == 0 else f'{bad} FAIL'}")


def s3():
    print("== s3: N4 - the general-m frontier Gamma_m ==")
    bad = neg = negl = 0
    permin = {}
    perminl = {}
    for (P, r) in odd_cells(11):
        for A in (2, 3, 8):
            cell = Cell(P, A)
            for m in range(2, 13, 2):
                caps = aligned_caps(P, A, r, m)
                g = gvec(cell, m)
                dmax, _ = dp_max(g, caps)
                v0 = v0_num(cell, r, m)
                um = u_m_num(cell, r, m)
                # the mirror-free majorant: A g_s - g_{s+1} <=
                # (A-1) q_s - q_{s-1}, summed over ALL odd t with
                # no positive part -- telescopes with no mirror
                ubar = sum((A - 1) * cell.q[t * P + r - 1]
                           - cell.q[t * P + r - 2]
                           for t in range(1, m, 2))
                gamma = n_m(cell, m) - v0 - um
                lam = n_m(cell, m) - v0 - ubar
                if ubar < um:
                    bad += 1
                    print(f"  MAJORANT FAIL ({P},{r}) A={A} m={m}")
                if dmax > v0 + um:
                    bad += 1
                    print(f"  CHARGE FAIL ({P},{r}) A={A} m={m}: "
                          f"DP {dmax} > V0+U {v0 + um}")
                if gamma <= 0:
                    neg += 1
                    print(f"  Gamma <= 0 at ({P},{r}) A={A} m={m}: "
                          f"{gamma}")
                if lam <= 0:
                    negl += 1
                key = m
                if key not in permin or gamma < permin[key][0]:
                    permin[key] = (gamma, (P, r, A))
                if key not in perminl or lam < perminl[key][0]:
                    perminl[key] = (lam, (P, r, A))
    for m in sorted(permin):
        print(f"  m={m:2d}: min Gamma = {permin[m][0]} at "
              f"{permin[m][1]}; min Lambda = {perminl[m][0]} at "
              f"{perminl[m][1]}")
    print(f"  DP <= V0 + U_m <= V0 + Ubar_m everywhere: "
          f"{'yes' if bad == 0 else 'NO'}; "
          f"nonpositive Gamma: {neg}; nonpositive Lambda: {negl}")


def s4():
    """The general-m closure: every algebraic step of the Lambda
    telescoping (the hand-attack above) machine-checked exactly.
    Stage designed after s3's read (the Lambda column made the
    mirror-free route the proof route)."""
    print("== s4: the Lambda telescoping, step by step ==")
    F = fib
    bad = 0
    for P in range(3, 32, 2):
        for r in range(2, P, 2):
            for A in (2, 3, 8, 64):
                cell = Cell(P, A)
                q, p = cell.q, cell.p
                Q = A * F(P) + F(P - 1)
                B = A * F(P - 1) + F(P - 2)
                # lemmas p_k >= q_{k-2} and p_k < q_k (k >= 2); the
                # first cut of this check also asserted
                # q_k - p_k >= q_{k-2} and the rig killed it (false
                # from k = P+2 on; the proof consumes only p < q)
                for k in range(2, 12 * P + 1):
                    if p[k] < q[k - 2] or p[k] >= q[k]:
                        bad += 1
                        print(f"  LEMMA FAIL k={k} ({P},{r}) A={A}")
                        break
                # closed forms of the brackets
                E = F(P) - F(P - r) - F(r)
                Ep = F(P - 1) - F(P - r - 1) - F(r - 1)
                bq = (A - 2) * E + (F(P - 2) - F(P - r) - F(r - 2))
                bcy = (A - 1) * Ep - F(P - 2) + F(r - 2) + 2
                if E < 0 or Ep < 0 or bq < 0 or bcy < 1:
                    bad += 1
                    print(f"  BRACKET FAIL ({P},{r}) A={A}: "
                          f"E={E} E'={Ep} BQ={bq} B-c={bcy}")

                def lam(m):
                    v0 = v0_num(cell, r, m)
                    ubar = sum((A - 1) * q[t * P + r - 1]
                               - q[t * P + r - 2]
                               for t in range(1, m, 2))
                    return n_m(cell, m) - v0 - ubar

                # Lambda_2 closed form (= B'_Q Q + B'_F F_P + T'')
                bf = ((A - 1) * (F(P - 1) - F(P - r - 1))
                      + A * (F(P - 1) - F(r - 1)) + F(r))
                l2c = bq * Q + bf * F(P) + F(P - 1) ** 2 - (A - 1) * F(r)
                if lam(2) != l2c:
                    bad += 1
                    print(f"  LAMBDA_2 FAIL ({P},{r}) A={A}: "
                          f"{lam(2)} != {l2c}")
                # the increment identity, m = 2..8
                for m in (2, 4, 6, 8):
                    x1 = q[(m + 1) * P]
                    y1 = q[(m + 1) * P - 1]
                    xm, ym = q[m * P], q[m * P - 1]
                    v2, vm = p[(m + 2) * P - 1], p[m * P - 1]
                    dlam = (bq * x1 + bcy * y1
                            - (2 * F(P) - 1 + (A - 1) * F(r)) * xm
                            - (1 + 2 * F(P - 1)
                               + (A - 1) * F(r - 1)) * ym
                            + v2 - vm)
                    if lam(m + 2) - lam(m) != dlam:
                        bad += 1
                        print(f"  DELTA FAIL ({P},{r}) A={A} m={m}: "
                              f"{lam(m + 2) - lam(m)} != {dlam}")
                    if dlam <= 0:
                        bad += 1
                        print(f"  DELTA NONPOS ({P},{r}) A={A} m={m}")
                # P = 3: the psi chain
                if P == 3:
                    for m in (2, 4, 6, 8):
                        um, vm = p[3 * m], p[3 * m - 1]
                        xm, ym = q[3 * m], q[3 * m - 1]
                        psi = ((4 * A + 4) * um + (2 * A + 1) * vm
                               - A * xm - (A + 1) * ym)
                        ok = (um >= A * vm
                              and (2 * A + 1) * vm >= A * ym
                              and xm <= (A + 1) * ym and psi > 0)
                        if not ok:
                            bad += 1
                            print(f"  PSI FAIL A={A} m={m}")
    print(f"  lemmas, brackets, Lambda_2 closed form, increment "
          f"identity, psi chain: "
          f"{'all pass' if bad == 0 else f'{bad} FAIL'}")


if __name__ == "__main__":
    s0()
    s1()
    s2()
    s3()
    s4()
    print("done.")
