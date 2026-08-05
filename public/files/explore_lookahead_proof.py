"""The exact lookahead law for redundant addition, proved for every
radix and every contiguous digit set — and the proof checked against
the measured census.

THE QUESTION. The addition law for redundant windows — X + Y is
window-local at lookahead c = 1 iff the slack rho >= 2 and the radix
b >= 3 and the digit set is not a rho = 2 set with an endpoint at
magnitude 1, and at c = 2 otherwise — was a rule by exhaustion: 58
symmetric systems (explore_redundant_lookback.py) and 214 contiguous
asymmetric systems (explore_margin_locus.py), game-tight at every
cell but derived at none. This run supplies the derivation: a proof
over ALL radices b >= 2 and ALL contiguous digit sets D = {-am..ap}
with slack rho = am + ap + 1 - b >= 1, and a rig that checks every
object the proof constructs against the residual safety game's
actual fixed points on the census grid and beyond it.

THE PROOF, hand-derived before this engine was written. Conventions
as in explore_margin_locus.py: spread W = am + ap, injected set for
addition S = D + D = {-2am..2ap}, game state R with successor
b*R + s - e*b^c for a chosen emission e in D, safety interval
[-am*r_c, ap*r_c] with r_c the c-digit repunit, the winning set the
game's greatest fixed point, and locality at lookahead c equivalent
to 0 lying in that set. Write

    sigma = ceil(am/(b-1)) + ceil(ap/(b-1)).

(1) ENDPOINT BOUNDS (any c). If the winning set is nonempty with
maximum H, the opponent injects s = 2ap there: every available
successor is at least b*H + 2ap - ap*b^c, and one must stay <= H,
forcing H*(b-1) <= ap*(b^c - 2). Mirrored at the minimum L with
s = -2am: -L*(b-1) <= am*(b^c - 2). At c = 1 the identity
floor(x*(b-2)/(b-1)) = x - ceil(x/(b-1)) turns these into

    H <= ap - ceil(ap/(b-1)) =: H1,   L >= -(am - ceil(am/(b-1))) =: L1.

(2) RESIDUE COUNT (c = 1). A successor b*(R - e) + s is congruent to
s mod b: the injected value stamps the successor's residue class.
S is contiguous of length 2W + 1 >= 2b + 1, so the opponent commands
every class; from the maximum H every injection must find a
surviving successor, so a nonempty winning set meets all b residue
classes, hence spans at least b integers: H - L + 1 >= b. With (1),

    b <= H - L + 1 <= W - sigma + 1,   i.e.   rho >= sigma.

(3) INVARIANT INTERVAL (any c). For [L, H] to trap the game, each
(R, s) needs an emission e in
[ceil((b*R+s-H)/b^c), floor((b*R+s-L)/b^c)] intersected with
[-am, ap]. The first interval is nonempty whenever H - L + 1 >= b^c;
its lower end stays <= ap for all (R, s) iff H*(b-1) <= ap*(b^c - 2),
and its upper end stays >= -am iff -L*(b-1) <= am*(b^c - 2) — and two
intervals with x1 <= x2, x1 <= ap, x2 >= -am intersect. Taking
H = floor(ap*(b^c-2)/(b-1)) and L = -floor(am*(b^c-2)/(b-1)) meets
both endpoint conditions by construction and contains 0, leaving only
the length condition.

(4) THE LAW AT c = 1. The interval [L1, H1] of (1) is precisely (3)'s
choice at c = 1, of length W - sigma + 1, which reaches b iff
rho >= sigma. So: rho >= sigma makes [L1, H1] invariant and the
greatest fixed point contains it, while (1) bounds the fixed point
inside it — THE WINNING SET IS EXACTLY [L1, H1]. And rho < sigma
forces the winning set empty by (2). Locality at c = 1 holds iff

    rho >= ceil(am/(b-1)) + ceil(ap/(b-1)),

necessary and sufficient, every radix, every contiguous set.

(5) c = 2 ALWAYS SUFFICES, c = 0 NEVER (rho >= 1). At c = 2 the
identity (b^2-2)/(b-1) = b + 1 - 1/(b-1) makes (3)'s length
W*(b+1) - sigma + 1; with W >= b and sigma <= (W + 2b - 4)/(b-1) the
worst case W = b needs b^2 - 3b + 3 >= 0, true at every radix (b = 2
directly: length 2W + 1 >= 5 > 4). At c = 0 the safety interval is
{0} alone and S strictly exceeds D on at least one side, so some
injection has no emission. Hence c_min is always 1 or 2, decided by
the inequality of (4).

(6) THE CLAUSE FORM IS THE INEQUALITY'S UNPACKING. For rho >= 1,
rho >= sigma is equivalent to: rho >= 2 AND b >= 3 AND not
(rho = 2 with min(am, ap) = 1). Forward: b = 2 gives sigma = W =
rho + 1; rho = 1 gives sigma >= 2 in every shape; rho = 2 with
min = 1 gives sigma = 1 + ceil(b/(b-1)) = 3. Backward, b >= 3: at
rho = 2, min = 0 has sigma = ceil((b+1)/(b-1)) = 2 and min >= 2
pins both parts to 1; at rho = 3 every shape lands sigma <= 3; at
rho >= 4, min = 0 gives sigma = 1 + ceil(rho/(b-1)) <= rho and
min >= 1 gives sigma <= 3 + (rho-2)/(b-1) <= rho. The endpoint
clause is the term ceil(1/(b-1)) = 1: an endpoint at magnitude 1
spends a full unit of slack — the one-digit residual can absorb all
but 1/(b-1) of a full digit per side, so a side of reach x costs
ceil(x/(b-1)) slack units, and a 0-endpoint side costs none.

THE DESIGN, frozen before the engine.

P-A The controls come back: (2,1) at c_min = 2 and (10,6) at
    c_min = 1 through this code path, the census grid (2 <= b <= 10,
    1 <= rho <= 5, am <= ap, spread <= 14) counts 214 cells, and the
    measured c_min equals the clause law at every one.
P-B The winning set identity holds cell-for-cell: the computed
    fixed point at c = 1 equals [L1, H1] where rho >= sigma and is
    EMPTY where rho < sigma, at every census cell and every cell of
    an extension ring (b <= 12, rho <= 6, spread <= 16) the census
    never ran.
P-C The unpacking of (6) holds at every (b, am, ap) with b <= 40,
    am, ap <= 30, rho >= 1 — pure arithmetic, no game.
P-D The c = 2 interval of (5) is invariant at every census cell,
    checked directly against the trap condition, never via the
    fixed-point engine.
P-E c = 0 is infeasible at every census cell.

KILLS, frozen as what this rig PRINTS.

K1 A cell prints a fixed point differing from the predicted interval
   (or nonempty where the inequality fails) -> the derivation is
   wrong; the law stays a rule by exhaustion and the tier does not
   move.
K2 The arithmetic sweep prints a cell where the inequality and the
   clause form disagree -> the proved statement is not the shipped
   statement; whichever the game sides with is the law and the other
   is retired.
K3 A predicted interval fails its own direct invariance check while
   the fixed-point comparison passes -> harness bug in the formula
   translation, not a finding.
K4 The census recount differs from 214 or an anchor misses -> wrong
   grid, nothing downstream is read.

POSITIVE CONTROL, run and read before any verdict line: P-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. Both anchors return their recorded values
   through this code path — (2,1) at c_min = 2, (10,6) at
   c_min = 1 — the census recounts 214 cells, and the measured
   c_min matches the clause law at 214/214. P-A held.

F2 THE WINNING-SET IDENTITY HOLDS EVERYWHERE RUN [the check behind
   the criterion]. The game's greatest fixed point at c = 1 equals
   the proof's interval [L1, H1] where rho >= sigma and is empty
   where rho < sigma, at 214/214 census cells AND at all 140
   extension-ring cells (b <= 12, rho <= 6, spread <= 16) the
   census never ran. The predicted interval also passes the direct
   trap check independently of the fixed-point engine, so the match
   is not a shared bug. K1 and K3 never fired.

F3 THE UNPACKING IS EXACT. The inequality rho >= sigma and the
   shipped three-clause form agree at 26330/26330 parameter cells
   with b <= 40, am, ap <= 30, rho >= 1. K2 never fired.

F4 c = 2 STAYS SUFFICIENT AND c = 0 STAYS INFEASIBLE at 214/214
   cells each, both checked directly. P-D, P-E held.

VERDICT. With the derivation in the docstring and no kill fired,
the addition law is a CRITERION — necessary and sufficient, proved
for every radix b >= 2 and every contiguous digit set with
rho >= 1, no computation at specific values load-bearing — in its
sharpest form: locality at c = 1 holds iff
rho >= ceil(am/(b-1)) + ceil(ap/(b-1)), the winning set then being
exactly [-(am - ceil(am/(b-1))), ap - ceil(ap/(b-1))], and c = 2
suffices otherwise. The 354 game cells are now the check on the
proof rather than the evidence for the law.

RUN RECORD: pure Python, integers only, standard library; largest
win set a few hundred residues, far under the analysis memory
ceiling; ~0.6s wall clock. Prints reproduced by:
python prime/code/explore_lookahead_proof.py
"""

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def ceil_div(x, y):
    return -(-x // y)


def digits(am, ap):
    return list(range(-am, ap + 1))


def repunit(b, c):
    return sum(b ** i for i in range(c))


def add_sums(am, ap):
    return list(range(-2 * am, 2 * ap + 1))


def win_set(b, am, ap, c, S):
    """Greatest fixed point of the residual safety game (the same
    engine explore_margin_locus.py measured the census with)."""
    lo, hi = -am * repunit(b, c), ap * repunit(b, c)
    win = set(range(lo, hi + 1))
    changed = True
    while changed:
        changed = False
        for R in list(win):
            for s in S:
                pre = b * R + s
                if not any(pre - e * b ** c in win
                           for e in digits(am, ap)):
                    win.discard(R)
                    changed = True
                    break
    return win


def measured_cmin(b, am, ap, cap=2):
    S = add_sums(am, ap)
    for c in range(cap + 1):
        if 0 in win_set(b, am, ap, c, S):
            return c
    return None


def sigma(b, am, ap):
    return ceil_div(am, b - 1) + ceil_div(ap, b - 1)


def predicted_win1(b, am, ap):
    """The proof's winning set at c = 1: [L1, H1] iff rho >= sigma,
    else empty."""
    rho = am + ap + 1 - b
    if rho < sigma(b, am, ap):
        return set()
    L1 = -(am - ceil_div(am, b - 1))
    H1 = ap - ceil_div(ap, b - 1)
    return set(range(L1, H1 + 1))


def clause_cmin(b, am, ap):
    """The shipped clause form of the law."""
    rho = am + ap + 1 - b
    one = rho >= 2 and b >= 3 and not (rho == 2 and min(am, ap) == 1)
    return 1 if one else 2


def interval_invariant(b, am, ap, c, L, H):
    """Direct trap check: every (R, s) finds an emission keeping the
    state in [L, H]. Independent of the fixed-point engine."""
    if L > H:
        return False
    for R in range(L, H + 1):
        for s in add_sums(am, ap):
            pre = b * R + s
            if not any(L <= pre - e * b ** c <= H
                       for e in digits(am, ap)):
                return False
    return True


def grid(bmax, rhomax, wmax):
    cells = []
    for b in range(2, bmax + 1):
        for am in range(0, wmax + 1):
            for ap in range(am, wmax + 1):
                rho = am + ap + 1 - b
                if 1 <= rho <= rhomax and am + ap <= wmax:
                    cells.append((b, am, ap))
    return cells


def main():
    print("== POSITIVE CONTROL (P-A) ==")
    a21 = measured_cmin(2, 1, 1)
    a106 = measured_cmin(10, 6, 6)
    print(f"anchor (2,1): c_min = {a21}   anchor (10,6): c_min = {a106}")
    ok(a21 == 2 and a106 == 1, "K4: an anchor missed")

    census = grid(10, 5, 14)
    print(f"census cells: {len(census)}")
    ok(len(census) == 214, "K4: census recount is not 214")

    law_miss = [c for c in census
                if measured_cmin(*c) != clause_cmin(*c)]
    print(f"census law check: {len(census) - len(law_miss)}/"
          f"{len(census)} cells match the clause law")
    ok(not law_miss, f"K4: law census mismatch at {law_miss[:5]}")

    print("\n== WINNING-SET IDENTITY (P-B) ==")
    ext = [c for c in grid(12, 6, 16) if c not in set(census)]
    for name, cells in (("census", census), ("extension", ext)):
        miss = []
        for (b, am, ap) in cells:
            got = win_set(b, am, ap, 1, add_sums(am, ap))
            if got != predicted_win1(b, am, ap):
                miss.append((b, am, ap))
        print(f"{name}: {len(cells) - len(miss)}/{len(cells)} fixed "
              f"points equal the predicted interval")
        ok(not miss, f"K1: winning-set mismatch ({name}) at {miss[:5]}")

    print("\n== THE UNPACKING (P-C, arithmetic only) ==")
    bad = []
    n = 0
    for b in range(2, 41):
        for am in range(0, 31):
            for ap in range(0, 31):
                rho = am + ap + 1 - b
                if rho < 1:
                    continue
                n += 1
                ineq = rho >= sigma(b, am, ap)
                clause = clause_cmin(b, am, ap) == 1
                if ineq != clause:
                    bad.append((b, am, ap))
    print(f"inequality vs clause form: {n - len(bad)}/{n} agree")
    ok(not bad, f"K2: unpacking fails at {bad[:5]}")

    print("\n== c = 2 INTERVAL, c = 0 (P-D, P-E) ==")
    bad2, bad0, bad1 = [], [], []
    for (b, am, ap) in census:
        H2 = (ap * (b * b - 2)) // (b - 1)
        L2 = -((am * (b * b - 2)) // (b - 1))
        if not interval_invariant(b, am, ap, 2, L2, H2):
            bad2.append((b, am, ap))
        if 0 in win_set(b, am, ap, 0, add_sums(am, ap)):
            bad0.append((b, am, ap))
        pw = predicted_win1(b, am, ap)
        if pw and not interval_invariant(b, am, ap, 1, min(pw), max(pw)):
            bad1.append((b, am, ap))
    print(f"c = 2 predicted interval invariant: "
          f"{len(census) - len(bad2)}/{len(census)}")
    print(f"c = 1 predicted interval invariant where nonempty "
          f"(direct): {len(bad1) == 0}")
    print(f"c = 0 infeasible: {len(census) - len(bad0)}/{len(census)}")
    ok(not bad2, f"K1: c = 2 interval not invariant at {bad2[:5]}")
    ok(not bad1, f"K3: c = 1 interval fails direct invariance {bad1[:5]}")
    ok(not bad0, f"K1: c = 0 feasible at {bad0[:5]}")

    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILURES")
    else:
        print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
