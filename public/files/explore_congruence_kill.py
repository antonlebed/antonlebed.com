"""The even-P lemma's congruence layer: does the m = 1 congruence
become an exact integer equation at large A, and does that equation
kill everything but the comb?

THE QUESTION
------------
The even-P lattice-avoidance lemma (explore_lattice_avoidance.py
D1-D4, explore_bounded_half.py D8) needs: at every even-P cell with
even NONZERO residue r, no periodic legal pattern beyond the zero
pattern and the alternating comb C1 has its tail value
S_m/(1 - eta^m) in the lattice L (at r = 0 the classification is a
theorem already, with both classical telescopes among the
exceptions). The
roadmapped candidate mechanism is the m = 1 congruence — the period-P
column sums read in L/(1 - eta)L. This probe tests the hand-derivation
that sharpens the mechanism into a closed-form kill, and reads whether
it extends to every period.

THE HAND-ATTACK (pre-engine, on paper; conventions re-derived from
the rig: theta_k = q_k alpha - p_k as (u, w) = (-p_k, q_k), caps A at
phase P-1 else 1, q_k = F_{k+1} and p_k = F_k for k <= P-1 at the
one-class window, eta = -theta_{P-1}, N(eta) = +1 at even P)
----------------------------------------------------------------------
D1  ONE FUNCTIONAL CARRIES THE CONGRUENCE. eta acts on L in basis
    (1, alpha) by M with columns (p_{P-1}, -q_{P-1}) and
    (-p_P, q_P) (eta * alpha = theta_P); det M = +1 and
    det(I - M) = -N with N = p_{P-1} + q_P - 2 = |L/(1 - eta)L|
    (P = 4: N = 3A + 2). For a period-P legal pattern d with
    S = sum d_k theta_{k+r} = x + y alpha, membership S in
    (1 - eta)L is the integrality of adj(I - M)(x, y)/(-N): two
    congruences mod N, and the w-row folds A-free. Substituting the
    digit expansion, that row reads Phi = sum_k d_k c_k with
    c_k = (p_{P-1} q_{k+r} - q_{P-1} p_{k+r}) - q_{k+r}, and in
    ALIGNED position j = (k + r) mod P (folding
    theta_{j+P} = eta theta_j = theta_j mod (1 - eta)L; the class cap
    A lands at j = r - 1, cyclic adjacency preserved) d'Ocagne
    F_{j+1} F_{P-1} - F_j F_P = (-1)^j F_{P-1-j} gives the closed
    form c_j = (-1)^j F_{P-1-j} - F_{j+1}: A-INDEPENDENT.
D2  THE SIZE BOUND TURNS IT INTO AN EQUATION. |c_{r-1}| =
    F_{P-r} + F_r (r - 1 odd) and sum_j |c_j| <= F_{P+3} - 2, while
    N ~ A F_P; since F_{P-r} + F_r < F_P, for A past an explicit
    A_0(P, r) the whole range of Phi sits inside (-N, N), so
    Phi = 0 mod N forces Phi = 0 EXACTLY — an integer equation whose
    solution set is A-independent and finite (the class digit is
    bounded by the OTHER positions' |c_j| sum over |c_{r-1}|). At (4, 2): max |Phi| =
    2A + 5 < 3A + 2 iff A >= 4, and the equation e_0 - 2 e_1 - e_2 -
    3 e_3 = 0 over legal digits has EXACTLY the zero pattern and
    C1 = (1, 0, 1, 0): the m = 1 layer at (4, 2) is a theorem for
    A >= 4 by hand, with A <= 3 the certified scan.
D3  C1 SOLVES THE EQUATION AT EVERY EVEN P: sum over even j of c_j =
    (F_{P-1} + ... + F_1) - (F_1 + ... + F_{P-1}) over odd indices
    = F_P - F_P = 0.
D4  THE m >= 2 LAYER (the candidate uniformity for ALL periods). A
    period-mP pattern has S_m in (1 - eta^m)L with eta^m =
    -theta_{mP-1}: the same frame verbatim at N_m = p_{mP-1} +
    q_{mP} - 2 and c_k^(m) = (p_{mP-1} q_{k+r} - q_{mP-1} p_{k+r})
    - q_{k+r}, each folded to its centered representative mod N_m
    (the fold is what makes the top end small again — the window
    wraps). If the folded coefficients stay graded from both ends
    with the class positions carrying ~F_r/F_P of a scale, then
    sum caps |c| < N_m holds at large A UNIFORMLY in m and EVERY
    period's congruence is an exact equation — the even-P lemma
    would reduce to those equations plus the certified small-A scan.
    Whether the folded middle coefficients cooperate is honestly
    open: that ratio is this probe's central print. (Settled since:
    explore_equation_bound.py proves the bound by hand, uniform in
    m for A past an explicit per-cell threshold — the palindrome
    closed form for the aligned coefficients, a monotone dominator
    covering every larger A; this probe's ratio table survives as
    the empirical cross-check.)

PREDICTIONS, FIXED BEFORE THE RUN (observables)
  N1 (controls; red voids the run): the machine-folded m = 1
      coefficients equal the hand closed form at every probed cell
      and are identical at A = 7 and A = 25; Phi(C1) = 0 exactly;
      the full two-row integrality accepts C1 at m = 1 and C1C1 at
      m = 2 and rejects the zero-with-one-tooth patterns.
  N2 (the m = 1 kill): per even-P even-r cell (P <= 12), the
      A-independent equation Phi = 0 over legal aligned digits:
      prediction — the full-condition survivors are exactly the zero
      pattern and C1 at every cell; whether Phi = 0 ALONE admits
      extras (killed by the u-row or legality) is open — count them.
      Also printed: the explicit A_0(P, r) threshold.
  N3 (the m >= 2 ratio): the table max|Phi_m| / N_m = (sum_k cap_k
      |folded c_k^(m)|) / N_m for m = 1..5, P in {4, 6, 8}, even r,
      A in {5, 10, 20, 40}. Prediction, honestly open: the ratio
      stays bounded in m and falls below 1 at large A uniformly —
      supporting the all-periods route; a ratio growing in m kills
      route D4 and confines the equation to m = 1.
  N4 (the m = 2 solutions): at the five cells (4,2), (6,2), (6,4),
      (8,2), (8,4), A = 12, enumerate ALL legal period-2P patterns; prediction — the
      full-condition survivors are exactly the zero pattern and the
      doubled comb C1C1; the Phi_2 = 0 extras (if any) have their
      two period-P blocks read against the m = 1 equation — whether
      the equation SPLITS per block at large scale is the reading.

  N5 (the all-A closure; frozen after s0-s3 printed, before s1b/s1c
      ran — the first run showed Phi = 0 extras at 14 cells, all
      failing the full check at A = 40, which is one A and not a
      theorem): for each extra, F_P^2 times the u-row numerator
      reduces mod N(A) to a CONSTANT e (the polynomial remainder in
      A); prediction — e != 0 for every extra, killing it at every A
      with N(A) > |e|, and the direct exhaustive sweep over all A up
      to that threshold finds no survivor beyond the zero pattern
      and C1 at any of the 15 cells. If both land, the m = 1 layer
      is a theorem for ALL A >= 2 at all 15 cells.

FINDINGS (run record at the end; every stage green, exact arithmetic)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1): the machine-folded m = 1 coefficients equal
    the hand closed form (-1)^j F_{P-1-j} - F_{j+1} and are identical
    at A = 7 and A = 25 at all 15 cells (even P <= 12, even r);
    Phi(C1) = 0 exactly; the two-row integrality accepts C1 and C1C1
    and rejects every single-tooth pattern.
F2  THE EQUATION FORCES AT A0 = 4 EVERYWHERE, AND IS NOT ALONE
    (N2): at every cell the size bound gives A0 = 4 — the congruence
    IS an integer equation from A = 4 on. But Phi = 0 admits
    A-independent extras at 14 of the 15 cells (none at (4, 2); up
    to 23 at (12, 6)); every extra fails the full two-row condition
    at A = 40. The class-digit bound Ebound = sum|c_j|/|c_{r-1}|
    runs 2..35.
F3  THE u-ROW KILLS EVERY EXTRA FOR ALL A AT ONCE (N5, stronger
    than predicted): num_u is quadratic in A in general and N
    linear, but on every one of the 163 extras across the 15 cells
    the quadratic term VANISHES and num_u is an exact rational
    multiple of N with non-integral ratio (printed per extra; e.g.
    (0,0,0,0,1,1) at (6, 2): num_u = -10(A+1) = -(5/4) N) — never
    integral at any A. Zero remainder kills, zero progression
    passes, zero insoluble-congruence cases: the classification is
    one verdict 163 times. That num_u degenerates to a scalar
    multiple of N exactly on the Phi = 0 solutions is an
    OBSERVATION at this scope and smells derivable — a target for
    the general-P hand proof. (Derived since: explore_urow_kill.py
    D2-D3 — one exact identity makes the multiple -w/q_{mP-1} with
    w = sum d_j q_j, at every m.)
F4  THE m = 1 LAYER IS PROVED FOR ALL A >= 2 AT ALL 15 CELLS (N5
    lands; rule — proved in a, exhaustive over even P <= 12, every
    even r): A = 2..4 by exhaustive enumeration of legal period-P
    patterns against the full condition (only the zero pattern and
    C1 survive — this also covers P = 10, 12, where no prior scan
    ran), A >= 4 by the equation plus the u-row's rational-multiple
    kill. Complete case analysis, no scan citation left in the
    chain.
F5  THE RATIO IS FLAT IN m AND FALLS AS ~1/A (N3): max|Phi_m|/N_m
    stabilizes by m = 3 at every probed (P, r, A) (e.g. (4, 2)
    A = 5: 0.882, 1.050, 1.071, 1.080, 1.082 for m = 1..5; A = 40:
    0.697 -> 0.729) and drops with A; it exceeds 1 only at A = 5,
    m >= 2, (4, 2). At A >= 10 every probed cell and period has
    ratio < 1: past a small per-cell threshold EVERY period's
    congruence is an exact integer equation — route D4's hypothesis
    holds at probed scope.
F6  THE EQUATION DOES NOT SPLIT PER BLOCK (N4): at all five m = 2
    cells the full-condition survivors are exactly the zero pattern
    and C1C1 (the prediction lands — no interior lattice pattern of
    period 2P exists at A = 12), but Phi_2 = 0 alone admits extras
    at every cell — 4 at (4, 2) up to 64 at (8, 4) — and they MIX: some concatenate two m = 1
    solutions (zero + C1 in either order solves Phi_2 = 0 and still
    fails the full condition), others pair blocks that are not
    m = 1 solutions at all. The m >= 2 kill runs through the u-row,
    not through block decomposition.

RUN RECORD: python explore_congruence_kill.py — s0..s3 + s1b/s1c,
0.3 s wall, memory trivial, exit 0, run twice byte-identical (the
per-extra verdicts printed by s1b included); the first run (pre-s1b,
s0-s3 only) matches on s2/s3 byte-for-byte.

THE DESIGN
----------
Everything exact (integers and Fractions end to end). Cell imported
from explore_parity_derivation (convergents to depth 400). s0
controls; s1 the m = 1 enumeration per cell with legality the cyclic
cap-after-nonzero rule; s1b the exact-in-A u-row classification per
extra (Lagrange fit of the quadratic numerator, polynomial division
by N, the three verdicts: rational multiple / remainder threshold /
flagged progression); s1c the exhaustive sweep over every A below
the thresholds and A0; s2 the ratio table; s3 the m = 2 exhaustive
enumeration at A = 12 with both-row full checks. One command runs
all; wall-clock under a second; memory trivial.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell              # noqa: E402


def fibs(n):
    F = [0, 1]
    while len(F) <= n:
        F.append(F[-1] + F[-2])
    return F


def n_m(cell, m):
    P = cell.P
    return cell.p[m * P - 1] + cell.q[m * P] - 2


def raw_coeffs(cell, r, m):
    """c_k^(m) = (p_{mP-1} q_{k+r} - q_{mP-1} p_{k+r}) - q_{k+r},
    k = 0..mP-1 (digit positions, original caps)."""
    P = cell.P
    pm, qm = cell.p[m * P - 1], cell.q[m * P - 1]
    return [pm * cell.q[k + r] - qm * cell.p[k + r] - cell.q[k + r]
            for k in range(m * P)]


def fold(c, N):
    """Centered representative of c mod N, in (-N/2, N/2]."""
    v = c % N
    return v - N if v > N - v else v


def folded_coeffs(cell, r, m):
    N = n_m(cell, m)
    return [fold(c, N) for c in raw_coeffs(cell, r, m)]


def caps_vec(P, A, m):
    return [A if (k + 1) % P == 0 else 1 for k in range(m * P)]


def legal(d, caps):
    """Cyclic legality: a nonzero digit forces the next below cap."""
    n = len(d)
    for k in range(n):
        if d[k] < 0 or d[k] > caps[k]:
            return False
        if d[k - 1] != 0 and d[k] > caps[k] - 1:
            return False
    return True


def s_xy(cell, r, d):
    """S = sum d_k theta_{k+r} as (x, y), S = x + y alpha."""
    x = -sum(dk * cell.p[k + r] for k, dk in enumerate(d))
    y = sum(dk * cell.q[k + r] for k, dk in enumerate(d))
    return x, y


def full_member(cell, r, d, m):
    """S in (1 - eta^m) L: both Cramer rows integral."""
    P = cell.P
    x, y = s_xy(cell, r, d)
    N = n_m(cell, m)
    pm1, pm = cell.p[m * P - 1], cell.p[m * P]
    qm1, qm = cell.q[m * P - 1], cell.q[m * P]
    num_u = x * (1 - qm) - pm * y
    num_w = (1 - pm1) * y - qm1 * x
    return num_u % N == 0 and num_w % N == 0


def c1_pattern(P, m):
    """The alternating comb: 1 at even positions (r even keeps it)."""
    return [1 if k % 2 == 0 else 0 for k in range(m * P)]


def hand_c(P, j):
    F = fibs(P + 2)
    sgn = 1 if j % 2 == 0 else -1
    return sgn * F[P - 1 - j] - F[j + 1]


def even_cells(pmax):
    return [(P, r) for P in range(4, pmax + 1, 2) for r in range(2, P, 2)]


def enum_legal(caps, class_pos, class_top):
    """All legal digit vectors with the stated per-position tops
    (caps for legality, class_top the enumeration bound at the class
    position), depth-first with the cyclic wrap checked at the end."""
    n = len(caps)
    out = []
    vec = [0] * n

    def rec(k):
        if k == n:
            if not (vec[n - 1] != 0 and vec[0] > caps[0] - 1):
                out.append(tuple(vec))
            return
        top = class_top if k == class_pos else caps[k]
        if vec[k - 1] != 0 and k > 0:
            top = min(top, caps[k] - 1)
        for v in range(top + 1):
            vec[k] = v
            rec(k + 1)
        vec[k] = 0

    rec(0)
    return out


def main():
    print("s0: controls — folded coefficients vs hand closed form")
    for (P, r) in even_cells(12):
        rows = {}
        for A in (7, 25):
            cell = Cell(P, A)
            c = folded_coeffs(cell, r, 1)
            aligned = [c[(j - r) % P] for j in range(P)]
            rows[A] = aligned
            assert aligned == [hand_c(P, j) for j in range(P)], \
                (P, r, A, aligned)
        assert rows[7] == rows[25]
        cell = Cell(P, 7)
        c = folded_coeffs(cell, r, 1)
        c1 = c1_pattern(P, 1)
        assert sum(ck * dk for ck, dk in zip(c, c1)) == 0, (P, r)
        assert full_member(cell, r, c1, 1), (P, r)
        assert full_member(cell, r, c1_pattern(P, 2), 2), (P, r)
        for k in range(P):
            tooth = [0] * P
            tooth[k] = 1
            if tooth != c1:
                assert not full_member(cell, r, tooth, 1), (P, r, k)
    print("  hand formula, A-independence, C1/C1C1 acceptance,")
    print("  single-tooth rejection: PASS at %d cells"
          % len(even_cells(12)))

    print("s1: the m = 1 equation's A-independent solution set")
    cell_extras = {}
    for (P, r) in even_cells(12):
        cell = Cell(P, 40)
        c = folded_coeffs(cell, r, 1)
        N = n_m(cell, 1)
        class_pos = P - 1                     # digit-space class slot
        cc = abs(c[class_pos])
        rest = sum(abs(ck) for k, ck in enumerate(c) if k != class_pos)
        Ebound = rest // cc
        caps = caps_vec(P, Ebound + 2, 1)
        sols = [d for d in enum_legal(caps, class_pos, Ebound)
                if sum(ck * dk for ck, dk in zip(c, d)) == 0]
        c1 = tuple(c1_pattern(P, 1))
        zero = tuple([0] * P)
        extras = [d for d in sols if d not in (zero, c1)]
        surv = [d for d in extras if full_member(cell, r, list(d), 1)]
        A0 = 2
        while True:
            celA = Cell(P, A0)
            NA = n_m(celA, 1)
            if A0 * cc + rest < NA:
                break
            A0 += 1
        print("  (P,r)=(%2d,%2d): |c_class|=%2d Ebound=%d "
              "Phi=0 sols=%d extras=%d full-survivors=%d A0=%d"
              % (P, r, cc, Ebound, len(sols), len(extras),
                 len(surv), A0))
        for d in surv:
            print("    SURVIVOR:", d)
        assert (zero in sols) and (c1 in sols)
        cell_extras[(P, r)] = extras

    print("s1b: the u-row kill per extra, exact in A (all-A closure)")
    from fractions import Fraction

    def num_u_of(P, r, d, A):
        cell = Cell(P, A)
        x, y = s_xy(cell, r, list(d))
        return (x * (1 - cell.q[P]) - cell.p[P] * y,
                n_m(cell, 1))

    def fit_poly(samples, deg):
        """Exact Lagrange fit, list of (A, value) -> coeff list
        low-to-high, Fractions."""
        pts = samples[:deg + 1]
        coeffs = [Fraction(0)] * (deg + 1)
        for i, (xi, yi) in enumerate(pts):
            basis = [Fraction(1)]
            denom = Fraction(1)
            for j, (xj, _) in enumerate(pts):
                if j == i:
                    continue
                new = [Fraction(0)] * (len(basis) + 1)
                for kk, b in enumerate(basis):
                    new[kk] -= b * xj
                    new[kk + 1] += b
                basis = new
                denom *= (xi - xj)
            for kk in range(len(basis)):
                coeffs[kk] += yi * basis[kk] / denom
        return coeffs

    def poly_eval(coeffs, A):
        return sum(c * A ** k for k, c in enumerate(coeffs))

    maxA = {}
    for (P, r) in even_cells(12):
        thr = 3           # sweep at least below A0 = 4
        print("  (P,r)=(%2d,%2d), %d extras:"
              % (P, r, len(cell_extras[(P, r)])))
        for d in cell_extras[(P, r)]:
            As = (50, 101, 151, 200)
            nus = [num_u_of(P, r, d, A) for A in As]
            nu_poly = fit_poly([(A, Fraction(nu))
                                for A, (nu, _) in zip(As, nus)], 2)
            n_poly = fit_poly([(A, Fraction(N))
                               for A, (_, N) in zip(As, nus)], 1)
            assert poly_eval(nu_poly, 200) == nus[3][0]
            assert poly_eval(n_poly, 200) == nus[3][1]
            c2, c1, c0 = nu_poly[2], nu_poly[1], nu_poly[0]
            n1, n0 = n_poly[1], n_poly[0]
            # num_u = Q*N + R,  Q = qa*A + qb,  R constant
            qa = c2 / n1
            qb = (c1 - qa * n0) / n1
            R = c0 - qb * n0
            if R == 0:
                # num_u/N = qa*A + qb exactly; integrality of that
                den = (qa.denominator * qb.denominator
                       // __import__("math").gcd(qa.denominator,
                                                 qb.denominator))
                a1 = qa.numerator * (den // qa.denominator)
                a0 = qb.numerator * (den // qb.denominator)
                import math
                g = math.gcd(a1, den)
                if a1 == 0:
                    passes = (a0 % den == 0)
                    assert not passes, ("CONSTANT PASS", P, r, d)
                    verdict = ("rational multiple %s of N, never"
                               " integral" % (qa * 0 + qb))
                elif a0 % g != 0:
                    verdict = "congruence insoluble, never integral"
                else:
                    sol = [A for A in range(2, 2 * den + 2)
                           if (a1 * A + a0) % den == 0]
                    print("    PROGRESSION PASS at (%d,%d) %s: "
                          "A = %s mod %d" % (P, r, d, sol, den))
                    thr = max([thr] + sol)
                    verdict = "PROGRESSION - u-row can pass"
            else:
                # N | num_u => N | q2*R with q2 = lcm of Q denoms
                import math
                q2 = (qa.denominator * qb.denominator
                      // math.gcd(qa.denominator, qb.denominator))
                bound = abs(q2 * R)          # N(A) <= bound needed
                Athr = int((bound - n0) / n1) + 1
                thr = max(thr, Athr)
                verdict = "remainder kill, N(A) > %s from A = %d" \
                    % (bound, Athr + 1)
            print("    %s: %s" % (d, verdict))
        print("    sweep-threshold A<=%d" % thr)
        maxA[(P, r)] = thr

    print("s1c: direct sweep below the thresholds (the m = 1 close)")
    for (P, r) in even_cells(12):
        hi = max(maxA[(P, r)], 4)      # cover A < A0 = 4 too
        c1 = tuple(c1_pattern(P, 1))
        zero = tuple([0] * P)
        bad = []
        for A in range(2, hi + 1):
            cell = Cell(P, A)
            caps = caps_vec(P, A, 1)
            pats = enum_legal(caps, None, None)
            assert all(legal(list(d), caps) for d in pats)
            for d in pats:
                if full_member(cell, r, list(d), 1) \
                        and d not in (zero, c1):
                    bad.append((A, d))
        print("  (P,r)=(%2d,%2d): A = 2..%d exhaustive: %s"
              % (P, r, hi,
                 "only {0, C1}" if not bad else str(bad)))
        assert not bad, (P, r, bad)

    print("s2: the m >= 2 ratio  sum caps|c|/N_m  (route D4's gate)")
    for P in (4, 6, 8):
        for r in range(2, P, 2):
            for A in (5, 10, 20, 40):
                cell = Cell(P, A)
                row = []
                for m in range(1, 6):
                    c = folded_coeffs(cell, r, m)
                    caps = caps_vec(P, A, m)
                    tot = sum(cp * abs(ck) for cp, ck in zip(caps, c))
                    row.append(tot / n_m(cell, m))
                print("  (P,r)=(%d,%d) A=%2d: " % (P, r, A)
                      + "  ".join("m=%d:%.3f" % (m + 1, v)
                                  for m, v in enumerate(row)))

    print("s3: the m = 2 exhaustive enumeration, A = 12")
    A = 12
    for (P, r) in ((4, 2), (6, 2), (6, 4), (8, 2), (8, 4)):
        cell = Cell(P, A)
        c2 = folded_coeffs(cell, r, 2)
        c1m = folded_coeffs(cell, r, 1)
        caps = caps_vec(P, A, 2)
        pats = enum_legal(caps, None, None)
        zeros = [d for d in pats
                 if sum(ck * dk for ck, dk in zip(c2, d)) == 0]
        surv = [d for d in zeros if full_member(cell, r, list(d), 2)]
        zero = tuple([0] * 2 * P)
        c1c1 = tuple(c1_pattern(P, 2))
        extra_surv = [d for d in surv if d not in (zero, c1c1)]
        extras = [d for d in zeros if d not in surv]
        print("  (P,r)=(%d,%d): legal=%d Phi2=0:%d full=%d "
              "beyond {0, C1C1}: %d"
              % (P, r, len(pats), len(zeros), len(surv),
                 len(extra_surv)))
        assert zero in surv and c1c1 in surv
        for d in extras:
            b1, b2 = d[:P], d[P:]
            m1 = [sum(ck * dk for ck, dk in zip(c1m, b)) == 0
                  for b in (b1, b2)]
            print("    Phi2-only zero: %s blocks-m1-solutions=%s"
                  % (d, m1))
        for d in extra_surv:
            print("    FULL SURVIVOR BEYOND COMB:", d)

    print("ALL STAGES DONE")


if __name__ == "__main__":
    main()
