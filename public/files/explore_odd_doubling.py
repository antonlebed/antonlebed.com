"""The doubling corollary: do the odd period multiples of odd P fall
out of the even-multiple theorem for free?

THE QUESTION
------------
The odd-P lattice-avoidance theorem (explore_odd_m2_bound.py F6)
covers even period multiples: at odd P, even nonzero residue r, every
A >= 2 and every EVEN m, no nonzero legal cyclic pattern of length mP
has a lattice tail value. The odd multiples (mP odd) were recorded
OPEN — "the congruence layer itself needs mP even" — with no chart of
what replaces the layer. The hand-attack below says nothing replaces
it: a period-mP pattern is also a period-2mP pattern with the SAME
tail value, so the even-multiple theorem at 2m already speaks for it.
This rig referees that identity with a membership test that assumes
nothing about the norm of eta^m, and enumerates the odd-multiple
census nobody had charted.

THE HAND-ATTACK (pre-engine, on paper; index conventions re-derived
from the engine: theta_k = q_k alpha - p_k with coordinate vector
(-p_k, q_k) in the basis (1, alpha); S = sum d_k theta_{k+r};
theta_{k+P} = eta theta_k at the purely periodic window; aligned caps
A at j = r-1 mod P; legality cap-1 after a nonzero, cyclic wrap;
full_member tests S in (1 - eta^m)L by Cramer rows with determinant
n_m = p_{mP-1} + q_{mP} - 2)
----------------------------------------------------------------------
THE DOUBLING IDENTITY. Let d be a legal cyclic pattern of length mP
and d2 = d concatenated with itself (length 2mP). Legality of d2 is
legality of d (the caps repeat with period P and the constraints are
local, wrap included). Then
  S(d2) = sum_{k < mP} d_k theta_{k+r} + sum_{k < mP} d_k
          theta_{k+mP+r} = S + eta^m S = (1 + eta^m) S,
and the periodic tail values coincide:
  v(d2) = S(d2)/(1 - eta^{2m}) = S(1+eta^m)/((1-eta^m)(1+eta^m))
        = S/(1 - eta^m) = v(d).
Membership IS "v in L", so member(d, m) <=> member(d2, 2m). The
even-multiple theorem at 2m says only the zero pattern is a member
of length 2mP; d2 = 0 forces d = 0. COROLLARY: at odd P, even
nonzero r, every A >= 2 and EVERY m >= 1 — odd multiples included —
no nonzero legal cyclic pattern of length mP has a lattice tail
value. And any legal periodic pattern whatever its period n is
periodic with period 2*lcm(n, P), an even multiple of P, so the
period quantifier goes entirely: the odd-P even-residue lattice
avoidance holds over ALL periodic patterns, matching even P's
"all period multiples at once" scope.
WHY full_member CANNOT REFEREE THIS ALONE: its determinant
n_m = p_{mP-1} + q_{mP} - 2 is Norm(1 - eta^m) only where
Norm(eta^m) = +1, i.e. mP even. At mP odd the norm is -1 and the
Cramer denominator is wrong, so the direct test below solves the
2x2 integer system with its OWN determinant: (1 - eta^m)L has the
integer basis b0 = theta_0 - theta_{mP}, b1 = theta_1 - theta_{mP+1}
in (1, alpha) coordinates ((theta_0, theta_1) is unimodular, and
eta^m theta_k = theta_{k+mP} at every m), and S in the sublattice
iff both Cramer solutions against det(b0, b1) are integral.

FINDINGS (all stages green; run twice byte-identical, 34 lines;
record at the end)
----------------------------------------------------------------------
F1  THE DIRECT TEST IS VALIDATED (s0, all pass): direct_member ==
    full_member on all 19,949 legal cyclic patterns at the control
    cells (odd P <= 7 at m = 2 and even P in {4, 6} at m in {1, 2},
    r even, A in {2, 3}), and the even-P comb positive control is a
    member under the direct test at 18/18 configurations — the test
    can say True.
F2  THE DOUBLING IDENTITY IS EXACT (s1, all pass): at all 766,232
    legal cyclic patterns over the odd cells (P <= 7, A in {2, 3},
    m in {1, 2, 3}), d2 is cyclically legal under the doubled caps
    (asserted), s_xy(d2) equals the (1 + eta^m) S coordinates
    and direct_member(d, m) == direct_member(d2, 2m) — zero
    mismatches either leg.
F3  THE ODD MULTIPLES ARE CLOSED (s2 + the hand-attack): the census
    at every odd multiple swept — odd cells P <= 7 with m in {1, 3},
    A in {2, 3}, plus P = 9 at m = 1 — prints NO nonzero member (28
    cell-instances, up to 166,540 legal patterns each), exactly the
    corollary's prediction. With F2 and the even-multiple theorem
    (explore_odd_m2_bound.py F6) the closure is a THEOREM: at odd P,
    even nonzero r, every A >= 2 and EVERY period multiple m >= 1 —
    and hence every periodic pattern of any period, via period
    2*lcm(n, P) — no nonzero legal periodic pattern has a lattice
    tail value. The odd-P even-residue half now matches even P's
    "all period multiples at once" scope, and the recorded
    odd-multiple frontier is EMPTY: nothing replaces the congruence
    layer because nothing is needed at the doubled period. What
    stays open at odd P: the odd residues only (non-comb interior
    cycles recorded — the gated half).

PREDICTIONS (frozen before the run; observables)
  N1 (controls; red voids the run): at even m the direct test equals
      full_member on EVERY legal cyclic pattern at the control cells,
      both parities of P; and the positive control — at even P, even
      nonzero r, the m-fold comb is a member under the direct test
      (the test must be able to say True).
  N2 (the doubling identity, mechanical): for every legal cyclic
      pattern d at the swept cells, s_xy(d2) equals the coordinates
      of (1 + eta^m) S, and direct_member(d, m) ==
      direct_member(d2, 2m). Exceptions printed with witnesses.
  N3 (the odd-multiple census, the uncharted leg): at every swept
      odd-P cell with m ODD, the count of nonzero members is printed.
      The corollary predicts 0 everywhere; a nonzero member is the
      kill-shape observable for the doubling reading and its meaning
      is weighed after the run.

THE DESIGN
----------
Everything exact (integers end to end). Cell, caps, enumeration,
s_xy, full_member imported from the shipped rigs, not
re-implemented. Stages:
  s0  N1 controls: direct test vs full_member at mP even — odd cells
      (P <= 7, r even, A in {2, 3}, m = 2) and even cells (P in
      {4, 6}, r even, A in {2, 3}, m in {1, 2}) — plus the even-P
      comb positive control at (4, 2), (6, 2), (6, 4), A in {2, 3},
      m in {1, 2, 3}.
  s1  N2: the doubling identity at every legal cyclic pattern,
      odd cells P <= 7, A in {2, 3}, m in {1, 2, 3}.
  s2  N3: the odd-multiple census — full enumeration at odd cells
      P <= 7, r even, A in {2, 3}, m in {1, 3}, nonzero members
      printed (plus P = 9, r in {2, 4, 6, 8}, A = 2, m = 1).
One command runs all; wall-clock estimate well under a minute;
memory trivial.

RUN RECORD
----------
python explore_odd_doubling.py — all stages, ~12 s wall, memory
trivial; run twice byte-identical (34 lines), zero mismatches, zero
nonzero members at every odd multiple.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell                    # noqa: E402
from explore_congruence_kill import full_member, s_xy         # noqa: E402
from explore_deep_pairs import (                              # noqa: E402
    aligned_caps, enum_legal_cyclic, d_of)


def theta(cell, k):
    """Coordinates of theta_k in the basis (1, alpha)."""
    return (-cell.p[k], cell.q[k])


def direct_member(cell, r, d, m):
    """S in (1 - eta^m)L by the 2x2 integer solve against the
    sublattice basis theta_0 - theta_mP, theta_1 - theta_{mP+1};
    no assumption on Norm(eta^m)."""
    P = cell.P
    x, y = s_xy(cell, r, d)
    t0, tmp = theta(cell, 0), theta(cell, m * P)
    t1, tmp1 = theta(cell, 1), theta(cell, m * P + 1)
    b0 = (t0[0] - tmp[0], t0[1] - tmp[1])
    b1 = (t1[0] - tmp1[0], t1[1] - tmp1[1])
    det = b0[0] * b1[1] - b0[1] * b1[0]
    assert det != 0
    nu = x * b1[1] - y * b1[0]
    nw = b0[0] * y - b0[1] * x
    return nu % det == 0 and nw % det == 0


def eta_pow_times(cell, m, xy):
    """(1 + eta^m) * (x + y alpha) in (1, alpha) coordinates, from
    the transport eta^m theta_k = theta_{k+mP} on the unimodular
    pair (theta_0, theta_1)."""
    P = cell.P
    x, y = xy
    t0, t1 = theta(cell, 0), theta(cell, 1)
    detm = t0[0] * t1[1] - t0[1] * t1[0]
    # (x, y) in the (theta_0, theta_1) basis, exactly
    u = (x * t1[1] - y * t1[0]) * detm
    w = (t0[0] * y - t0[1] * x) * detm
    assert u * t0[0] + w * t1[0] == x and u * t0[1] + w * t1[1] == y
    ta, tb = theta(cell, m * P), theta(cell, m * P + 1)
    return (x + u * ta[0] + w * tb[0], y + u * ta[1] + w * tb[1])


def odd_cells(pmax):
    return [(P, r) for P in range(3, pmax + 1, 2)
            for r in range(2, P, 2)]


def even_cells_list(ps):
    return [(P, r) for P in ps for r in range(2, P, 2)]


def comb_pattern(n):
    return [1 if j % 2 == 0 else 0 for j in range(n)]


def s0():
    print("== s0: controls — direct test vs full_member at mP even; "
          "even-P comb positive control")
    checked = mismatches = 0
    for (P, r), A, m in [((P, r), A, 2) for (P, r) in odd_cells(7)
                         for A in (2, 3)] + \
                        [((P, r), A, m) for (P, r) in
                         even_cells_list((4, 6))
                         for A in (2, 3) for m in (1, 2)]:
        cell = Cell(P, A)
        caps = aligned_caps(P, A, r, m)
        for e in enum_legal_cyclic(caps):
            d = d_of(list(e), r)
            a = direct_member(cell, r, d, m)
            b = full_member(cell, r, d, m)
            checked += 1
            if a != b:
                mismatches += 1
                print(f"  MISMATCH ({P},{r}) A={A} m={m} e={e}: "
                      f"direct {a} full {b}")
    print(f"  {checked} patterns checked, {mismatches} mismatches")
    pos = []
    for (P, r) in ((4, 2), (6, 2), (6, 4)):
        for A in (2, 3):
            cell = Cell(P, A)
            for m in (1, 2, 3):
                comb = comb_pattern(m * P)
                got = direct_member(cell, r, d_of(comb, r), m)
                pos.append(got)
                if not got:
                    print(f"  POSITIVE CONTROL FAIL ({P},{r}) A={A} "
                          f"m={m}: comb not a member")
    print(f"  even-P comb positive control: {sum(pos)}/{len(pos)} "
          f"member verdicts True")


def s1():
    print("== s1: the doubling identity — S(d2) = (1+eta^m)S, "
          "d2 legal, and member(d, m) == member(d2, 2m)")
    checked = bad_s = bad_m = 0
    from explore_deep_pairs import legal_cyclic
    for (P, r) in odd_cells(7):
        for A in (2, 3):
            cell = Cell(P, A)
            for m in (1, 2, 3):
                caps = aligned_caps(P, A, r, m)
                caps2 = aligned_caps(P, A, r, 2 * m)
                for e in enum_legal_cyclic(caps):
                    assert legal_cyclic(list(e) + list(e), caps2)
                    d = d_of(list(e), r)
                    d2 = d + d
                    checked += 1
                    s2c = s_xy(cell, r, d2)
                    pred = eta_pow_times(cell, m, s_xy(cell, r, d))
                    if s2c != pred:
                        bad_s += 1
                        print(f"  S MISMATCH ({P},{r}) A={A} m={m} "
                              f"e={e}: {s2c} vs {pred}")
                    if direct_member(cell, r, d, m) != \
                            direct_member(cell, r, d2, 2 * m):
                        bad_m += 1
                        print(f"  MEMBER MISMATCH ({P},{r}) A={A} "
                              f"m={m} e={e}")
    print(f"  {checked} patterns: S mismatches {bad_s}, member "
          f"mismatches {bad_m}")


def s2():
    print("== s2: the odd-multiple census (full enumeration, "
          "direct test)")
    for (P, r) in odd_cells(7) + [(9, r) for r in (2, 4, 6, 8)]:
        for A in ((2, 3) if P <= 7 else (2,)):
            cell = Cell(P, A)
            for m in ((1, 3) if P <= 7 else (1,)):
                caps = aligned_caps(P, A, r, m)
                pats = enum_legal_cyclic(caps)
                nz = [e for e in pats if any(e)
                      and direct_member(cell, r, d_of(list(e), r), m)]
                print(f"  ({P},{r}) A={A} m={m}: {len(pats)} legal, "
                      f"nonzero members {nz if nz else 'NONE'}")


if __name__ == "__main__":
    s0()
    s1()
    s2()
