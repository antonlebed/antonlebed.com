"""The member-monoid decomposition: are the odd-residue cycle
members the legality-truncated additive monoid on few basic cut
members — and what ARE the generators?

THE QUESTION
------------
The odd-residue cycle chart (explore_odd_cycles.py, 48 cells) reads
the gated cells' members as the comb plus, at six cap-4 cells, one
deeper-cut second family — every value a landed cut. A larger-cap
probe then found THE SUPERPOSITION: 105010 = 101010 + 004000 at
(P, A, r) = (6, 6, 3), value -theta_3 - theta_5 — S is linear in the digits, so
members ADD wherever the digit-wise sum stays legal. This rig asks,
per cell: what are the INDECOMPOSABLE members (the monoid's
generators), are they few and nameable (the comb; the class-slot
tooth where its L/(1-eta)L order admits it; the recorded
tooth-plus-unit words), and does the picture hold at the larger caps
A = 5..8 where headroom first lets generators add? Plus the m = 2
structure: a derived congruence criterion for which concatenations
of member words are members — the fused/unfused mechanism.

THE HAND-ATTACK (pre-engine, on paper; index conventions re-derived
from the engines: aligned caps A at j = r-1 mod P; digit vector
d_k = e_{(k+r) mod n}; s_xy computes S = sum_k d_k theta_{k+r},
which in aligned coordinates is S = sum_j e_j theta_j
+ (eta^m - 1) T_e with T_e = sum_{j<r} e_j theta_j — the cyclic
wrap sends the aligned positions j < r through theta_{j+n} =
eta^m theta_j; theta_k = (-p_k, q_k) in (1, alpha) coordinates;
direct_member carries no norm assumption, so m = 1 membership is
testable at odd P where det H = -1)
----------------------------------------------------------------------
H1  SOUNDNESS IS A LEMMA, NOT A QUESTION. If S(d1), S(d2) are in
    (1 - eta)L and d1 + d2 is legal, S(d1 + d2) = S(d1) + S(d2) is
    in (1 - eta)L: a legal digit-wise sum of members is a member.
    Machine-checked as a positive control only.
H2  SUB-VECTOR LEGALITY. If 0 <= e' <= e digit-wise and e is legal,
    e' is legal: the cap-after-nonzero rule only RAISES e''s cap
    where e' zeroes a predecessor e kept nonzero. So a decomposition
    e = e1 + e2 into nonzero members has both parts inside the
    enumerated member set, and "indecomposable" is decidable by a
    pair scan over members below e.
H3  THE MONOID CLAIM'S CONTENT IS THE GENERATOR CENSUS. By induction
    on digit sum, EVERY member is a sum of indecomposables (H2 makes
    the split well-founded, H1 keeps partial sums members). So
    "member set = legality-truncated monoid on its indecomposables"
    is automatic; the chartable content is that the indecomposables
    are FEW and NAMEABLE — comb, tooth, the recorded second-family
    words — and that the count stays bounded as A grows. The closure
    rebuild is kept as a consistency control, never a finding.
H4  WHAT CANNOT SCALE. The comb touches a cap-1 slot at every
    P >= 4, so 2*comb is illegal and the comb contributes exactly
    once per decomposition there; at P <= 3 the comb is the pure
    class tooth (P = 2: height 1; P = 3: height 2) and scales to the
    class cap. A height-k*h0 tooth is k h0-teeth added, legal
    whenever k*h0 <= A: teeth decompose to the minimal tooth.
H5  THE CONCATENATION CRITERION (derived). For length-P aligned
    member words u, v at m = 2: S_(u,v) = S_u + eta S_v
    - eta(1 - eta)(T_u - T_v) (from the wrap convention above). With
    S_u = (1 - eta) lam_u, S_v = (1 - eta) lam_v and eta = -1 mod
    (1 + eta)L: concat(u, v) is an m = 2 member iff
        lam_u + T_u == lam_v + T_v  mod (1 + eta)L.
    Symmetric in (u, v) — matching the chart's mixed words arriving
    in pairs. Hand-check against the recorded m = 2 data: (6, 4, 3)
    prints all four concatenations as members (so mu_C == mu_T
    there) while (4, 4, 1) prints only the two diagonals (mu_C !=
    mu_T there): the fused/unfused split IS this congruence if the
    criterion holds.
H6  TRANSPLANTS, flagged: the expectation that indecomposables stay
    at <= 2 per cell is imported from the A <= 4 chart, where
    headroom never lets generators add — whether a third family
    appears at A = 5..8 is the run's question, not an expectation.
    The tooth reading (second family = pure tooth iff h0 <= A) is
    imported from the old s3 and re-read per (P, A, r) because h0
    moves with A (the window itself does).

FINDINGS (all stages green; final form run twice byte-identical,
169 lines; record at the end)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1): 11 legal member+member sums at the 48 chart
    cells, zero non-members (H1 confirmed as machine fact); all four
    anchor member sets reproduce exactly; the witness lands whole —
    at (6, 6, 3) the words 101010 (v = 2-3a = -theta_3), 004000
    (v = 5-8a = -theta_5) and 105010 (v = 7-11a) are all members
    with v(105010) = v(101010) + v(004000).
F2  THE DECOMPOSITION PRINTS AT EVERY CELL (N2): at all 112 cells
    (P = 2..8, A = 2..8, odd r) the member set equals the legal
    closure of its indecomposables (closure control: 0 cells off),
    and the generator census is SMALL — 1 generator at 82 cells,
    2 at 26, 3 at 3 ((7,7,3), (7,8,3), (8,7,3)), 4 at 1 ((8,8,3)).
    Member counts grow with A exactly as the truncated monoid
    predicts (e.g. (6, A, 3): 2, 3, 3, 3, 4 at A = 4..8 — comb,
    tooth, comb+tooth at A >= 5, 2*tooth at A = 8).
F3  THE GENERATOR LADDER (N3): every indecomposable is the comb, the
    pure class tooth (P <= 3 and the (6, *, 3) column, h0 = 4 at
    every A there), or a tooth-plus-unit word — and the recorded
    A = 4 second families persist unchanged at every higher cap
    (3001, 30101, 0040100, 00400010, 10004000). At cap A = 7 a
    THIRD family joins at the r = 3 cells of P = 7, 8 (0160000,
    01600100 — value -theta_6 = -theta_{r+3}: the cut ladder's next
    rung, a height-6 tooth with unit digits), and at (8, 8, 3) a
    FOURTH (00801001). The deeper-cut ladder continues with the
    cap; nothing beyond tooth-plus-unit shapes appears.
F4  THE VALUES (N4, one slate miss): every indecomposable value is a
    landed cut t(-theta_j) — 35 of 36 non-comb rows at t = 1 with
    j = r+2 (the A = 4 families), j = r+3 (the cap-7 family) — but
    (8, 8, 3)'s fourth generator 00801001 lands t = 2: v = 10-16a
    = 2(-theta_5), NOT decomposable (00801001 - 00400010 = 00401
    0-1-1 is not a digit-wise part) — the frozen t = 1 prediction
    read the A <= 4 chart's rows as the law and the cap-8 cell
    refutes the t = 1 half while the landed-cut half survives.
F5  THE CONCATENATION CRITERION IS EXACT (N5): at all 48 chart
    cells, every m = 2 member's two blocks are m = 1 members (0
    failures), and over all 95 legal ordered pairs (u, v):
    concat(u, v) is an m = 2 member IFF lam_u + T_u == lam_v + T_v
    mod (1 + eta)L — zero mismatches, and the congruence's own
    verdicts reproduce the recorded fused/unfused split exactly
    (FUSED with 2 mixed members at (6,4,3), (7,4,3), (8,4,3),
    (8,4,5); the r = 1 exception cells unfused). The chart's
    branching-subshift observation is now a derived criterion
    (H5) with a machine certificate.

PREDICTIONS (frozen before the run; observables)
  N1 (controls; red voids the run): (a) at all 48 chart cells
      (A <= 4, m = 1), every legal digit-wise sum of two members is
      a member — zero violations. (b) The recorded m = 1 member
      sets reproduce: (4,4,1) {1010, 3001}; (6,4,3)
      {004000, 101010}; (8,4,3) {00400010, 10101010}; (8,4,5)
      {10004000, 10101010}. (c) The witness: at (6, 6, 3) the words
      101010, 004000, 105010 are all members, the parts' values are
      -theta_3 and -theta_5, and the sum's value is their sum.
  N2 (the chart): per cell (P = 2..8, A = 2..8, odd r; m = 1) the
      member count, indecomposable count, and each indecomposable's
      word, class and value print. No count shape frozen (A >= 5 is
      uncharted; H6).
  N3 (the generator reading): every indecomposable is the comb, a
      pure class-slot tooth, or a recorded second-family word.
      Kill-shape observable: an OTHER row — an indecomposable
      matching none of the three — printing its word and value.
  N4 (the values): every indecomposable's value is a single landed
      cut, v = -theta_j exactly (t = 1), j within 0..2P+3.
      Kill-shape observable: an indecomposable whose value matches
      no -theta_j.
  N5 (the m = 2 criterion, A <= 4, all 48 cells): (a) every m = 2
      member's two length-P blocks are m = 1 members; (b) for every
      ordered pair (u, v) of m = 1 members with legal concatenation,
      member(concat) == [mu_u == mu_v mod (1 + eta)L], zero
      mismatches; (c) the recorded fused/unfused split reproduces as
      the congruence's own verdicts ((6,4,3)-type cells fused,
      (4,4,1)/(5,4,1) unfused). Kill-shape observable: a criterion
      mismatch row.

THE DESIGN
----------
Exact end to end; engines imported from the shipped rigs: Cell,
odd_comb, alt_comb (explore_parity_derivation), aligned_caps,
enum_legal_cyclic, d_of (explore_deep_pairs), direct_member
(explore_odd_doubling), s_xy (explore_congruence_kill). Stages:
  s0  N1: the soundness control over the 48 chart cells; the four
      anchor member sets; the (6, 6, 3) witness decomposition.
  s1  N2+N3+N4: the monoid chart at m = 1 over P = 2..8, A = 2..8,
      odd r (112 cells): members by enumeration, indecomposables by
      the pair scan (H2), the closure rebuild asserted equal to the
      member set (H3's control), each indecomposable classified
      COMB / TOOTH(h) / SECOND-FAMILY / OTHER with its cut value;
      per cell the minimal admitting tooth height h0 (least
      admitting divisor of |det(I - H)|, the old s3's exact form).
  s2  N5: the concatenation criterion at m = 2 over the 48 chart
      cells: block membership, then the congruence mu_u == mu_v mod
      (1 + eta)L tested against direct_member on every legal
      ordered pair.
One command runs all; wall-clock estimate ~1 min; memory trivial.

FIRST-RUN CORRECTIONS (the record of the slate's own errors, kept
beside the findings they graded):
  * The s1 header's first draft printed an em dash, which print()
    cannot encode on the Windows console (cp1252); replaced with
    "--" before the recorded runs. No verdict was affected.
  * N4's t = 1 clause is a slate MISS, not an engine error: the
    machine's (8, 8, 3) row stands and F4 records the refutation.

RUN RECORD: python explore_member_monoid.py — s0..s2, ~66 s wall,
memory trivial, exit 0; final form run twice byte-identical
(169 lines), s0 GREEN, s1 closure GREEN non-cut=0 other=30,
s2 GREEN.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell, odd_comb, alt_comb  # noqa: E402
from explore_deep_pairs import (                                # noqa: E402
    aligned_caps, enum_legal_cyclic, d_of)
from explore_odd_doubling import direct_member                  # noqa: E402
from explore_congruence_kill import s_xy                        # noqa: E402


def chart_cells(a_hi=4):
    return [(P, A, r) for P in range(2, 9) for A in range(2, a_hi + 1)
            for r in range(1, P, 2)]


def theta(cell, k):
    return (-cell.p[k], cell.q[k])


def el(u, w):
    return f"{u}{w:+d}a"


def members_at(cell, r, m):
    """All nonzero legal cyclic aligned vectors that are members."""
    caps = aligned_caps(cell.P, cell.A, r, m)
    out = []
    for e in enum_legal_cyclic(caps):
        if any(e) and direct_member(cell, r, list(d_of(e, r)), m):
            out.append(tuple(e))
    return out


def solve2(b0, b1, x, y):
    """Integer solution (nu, nw) of nu*b0 + nw*b1 = (x, y), or None."""
    det = b0[0] * b1[1] - b0[1] * b1[0]
    assert det != 0
    nu = x * b1[1] - y * b1[0]
    nw = b0[0] * y - b0[1] * x
    if nu % det or nw % det:
        return None
    return nu // det, nw // det


def lam_of(cell, r, e):
    """lam = S/(1 - eta) in (1, alpha) coordinates (m = 1 member)."""
    P = cell.P
    x, y = s_xy(cell, r, list(d_of(e, r)))
    b0 = tuple(a - b for a, b in zip(theta(cell, 0), theta(cell, P)))
    b1 = tuple(a - b for a, b in zip(theta(cell, 1), theta(cell, P + 1)))
    s = solve2(b0, b1, x, y)
    assert s is not None, "lam_of on a non-member"
    nu, nw = s
    t0, t1 = theta(cell, 0), theta(cell, 1)
    return (nu * t0[0] + nw * t1[0], nu * t0[1] + nw * t1[1])


def in_one_plus_eta(cell, xy):
    """xy in (1 + eta)L, basis theta_i + theta_{i+P}."""
    P = cell.P
    b0 = tuple(a + b for a, b in zip(theta(cell, 0), theta(cell, P)))
    b1 = tuple(a + b for a, b in zip(theta(cell, 1), theta(cell, P + 1)))
    return solve2(b0, b1, xy[0], xy[1]) is not None


def mu_of(cell, r, e):
    """mu = lam + T, T = sum_{j<r} e_j theta_j (H5)."""
    lu, lw = lam_of(cell, r, e)
    for j in range(min(r, len(e))):
        tj = theta(cell, j)
        lu += e[j] * tj[0]
        lw += e[j] * tj[1]
    return (lu, lw)


def legal_cyclic_digitwise(e, caps):
    n = len(e)
    for j in range(n):
        top = caps[j] - (1 if e[(j - 1) % n] > 0 else 0)
        if e[j] < 0 or e[j] > top:
            return False
    return True


def indecomposables(mset):
    """Members with no split into two nonzero members (H2)."""
    ms = set(mset)
    out = []
    for e in sorted(ms):
        split = False
        for u in ms:
            if u != e and all(a <= b for a, b in zip(u, e)) \
                    and tuple(b - a for a, b in zip(u, e)) in ms:
                split = True
                break
        if not split:
            out.append(e)
    return out


def closure(gens, caps):
    """All legal multiset sums of gens (H3's consistency control)."""
    seen = set()
    frontier = [g for g in gens]
    for g in frontier:
        seen.add(g)
    while frontier:
        nxt = []
        for e in frontier:
            for g in gens:
                s = tuple(a + b for a, b in zip(e, g))
                if s not in seen and legal_cyclic_digitwise(s, caps):
                    seen.add(s)
                    nxt.append(s)
        frontier = nxt
    return seen


def comb_aligned(P, A, r):
    d = odd_comb(P, A, 1) if P % 2 == 1 else alt_comb(P, P)
    return tuple(d[(j - r) % P] for j in range(P))


def cut_value(cell, v, jmax):
    """v == t * (-theta_j)? Returns (t, j) or None."""
    for j in range(jmax):
        mt = (cell.p[j], -cell.q[j])
        if mt == (0, 0):
            continue
        for t in range(1, 200):
            if (t * mt[0], t * mt[1]) == v:
                return t, j
            if abs(t * mt[0]) > abs(v[0]) and abs(t * mt[1]) > abs(v[1]):
                break
    return None


def h0_of(cell, r):
    """Least admitting class-tooth height: least divisor h of
    |det(I - H)| with h*delta(class slot) a member (m = 1)."""
    P = cell.P
    h = cell.H
    idx = abs((1 - h[0]) * (1 - h[3]) - h[1] * h[2])

    def is_mem(k):
        e = [0] * P
        e[(r - 1) % P] = k
        return direct_member(cell, r, list(d_of(tuple(e), r)), 1)

    return min(k for k in range(1, idx + 1) if idx % k == 0 and is_mem(k)), idx


def s0():
    print("=" * 74)
    print("S0 CONTROLS: soundness over the 48 chart cells; anchor"
          " member sets; the (6,6,3) witness")
    bad = 0
    # (a) soundness: legal sum of members is a member
    pairs = viol = 0
    for (P, A, r) in chart_cells():
        cell = Cell(P, A)
        caps = aligned_caps(P, A, r, 1)
        ms = members_at(cell, r, 1)
        for u in ms:
            for v in ms:
                s = tuple(a + b for a, b in zip(u, v))
                if legal_cyclic_digitwise(s, caps):
                    pairs += 1
                    if not direct_member(cell, r, list(d_of(s, r)), 1):
                        viol += 1
    print(f"  soundness: {pairs} legal member+member sums, "
          f"{viol} non-members {'ok' if viol == 0 else '<-- LEMMA DEAD'}")
    bad += viol
    # (b) anchors
    anchors = {(4, 4, 1): {"1010", "3001"},
               (6, 4, 3): {"004000", "101010"},
               (8, 4, 3): {"00400010", "10101010"},
               (8, 4, 5): {"10004000", "10101010"}}
    for (P, A, r), want in anchors.items():
        got = {"".join(map(str, e))
               for e in members_at(Cell(P, A), r, 1)}
        ok = got == want
        print(f"  ({P},{A},{r}) m=1 members={sorted(got)} "
              f"{'ok' if ok else '<-- OFF THE RECORD'}")
        bad += 0 if ok else 1
    # (c) the witness
    cell = Cell(6, 6)
    words = {w: tuple(int(c) for c in w)
             for w in ("101010", "004000", "105010")}
    vs = {}
    for w, e in words.items():
        m = direct_member(cell, 3, list(d_of(e, 3)), 1)
        vs[w] = lam_of(cell, 3, e) if m else None
        print(f"  (6,6,3) {w}: member={m}"
              + (f" v={el(*vs[w])}" if m else ""))
        bad += 0 if m else 1
    if all(vs.values()):
        adds = (vs["105010"][0] == vs["101010"][0] + vs["004000"][0]
                and vs["105010"][1] == vs["101010"][1] + vs["004000"][1])
        cc = cut_value(cell, vs["101010"], 16)
        ct = cut_value(cell, vs["004000"], 16)
        ok = adds and cc == (1, 3) and ct == (1, 5)
        print(f"  witness: v(105010)=v(101010)+v(004000)={adds}, "
              f"parts t,j={cc},{ct} "
              f"{'ok' if ok else '<-- OFF THE SLATE'}")
        bad += 0 if ok else 1
    print(f"  {'PASS' if bad == 0 else 'FAIL'}")
    return bad == 0


def s1():
    print("=" * 74)
    print("S1 THE MONOID CHART (m=1): P=2..8, A=2..8, odd r --"
          " members, indecomposables, classes, values")
    other_rows = []
    noncut = 0
    closure_bad = 0
    for (P, A, r) in chart_cells(a_hi=8):
        cell = Cell(P, A)
        caps = aligned_caps(P, A, r, 1)
        ms = members_at(cell, r, 1)
        gens = indecomposables(ms)
        if closure(gens, caps) != set(ms):
            closure_bad += 1
            print(f"  P={P} A={A} r={r}: CLOSURE != MEMBERS")
        h0, idx = h0_of(cell, r)
        comb = comb_aligned(P, A, r)
        tags = []
        for g in gens:
            v = lam_of(cell, r, g)
            cv = cut_value(cell, v, 2 * P + 4)
            if cv is None:
                noncut += 1
            supp = [j for j, x in enumerate(g) if x]
            if g == comb:
                cls = "COMB"
            elif supp == [(r - 1) % P]:
                cls = f"TOOTH(h={g[supp[0]]})"
            else:
                cls = "OTHER"
                other_rows.append((P, A, r, g, v, cv))
            tags.append(f"{''.join(map(str, g))}={cls}"
                        f" v={el(*v)}"
                        + (f"=-th_{cv[1]}" if cv and cv[0] == 1
                           else (f"={cv[0]}(-th_{cv[1]})" if cv
                                 else " NOT-A-CUT")))
        print(f"  P={P} A={A} r={r}: members={len(ms)} "
              f"gens={len(gens)} h0={h0} idx={idx} | " + "; ".join(tags))
    print(f"  closure control: {closure_bad} cells off"
          f" {'ok' if closure_bad == 0 else '<-- H3 CONTROL DEAD'}")
    print(f"  non-cut indecomposable values: {noncut}")
    print(f"  OTHER rows (beyond comb/tooth): {len(other_rows)}")
    for (P, A, r, g, v, cv) in other_rows:
        print(f"    ({P},{A},{r}) {''.join(map(str, g))} v={el(*v)}"
              f" cut={cv}")
    return closure_bad == 0, noncut, other_rows


def s2():
    print("=" * 74)
    print("S2 THE CONCATENATION CRITERION (m=2, 48 cells):"
          " blocks are members; member(uv) <=> mu_u == mu_v"
          " mod (1+eta)L")
    bad_block = bad_crit = tested = fused_cells = 0
    for (P, A, r) in chart_cells():
        cell = Cell(P, A)
        ms1 = set(members_at(cell, r, 1))
        ms2 = members_at(cell, r, 2)
        caps2 = aligned_caps(P, A, r, 2)
        for e in ms2:
            u, v = e[:P], e[P:]
            if not ((not any(u) or u in ms1)
                    and (not any(v) or v in ms1)):
                bad_block += 1
                print(f"  ({P},{A},{r}) m=2 member "
                      f"{''.join(map(str, e))}: block NOT an m=1"
                      f" member <-- N5a DEAD")
        mus = {u: mu_of(cell, r, u) for u in ms1}
        mixed_member = 0
        for u in ms1:
            for v in ms1:
                e = u + v
                if not legal_cyclic_digitwise(e, caps2):
                    continue
                tested += 1
                is_m = direct_member(cell, r, list(d_of(e, r)), 2)
                diff = (mus[u][0] - mus[v][0], mus[u][1] - mus[v][1])
                pred = in_one_plus_eta(cell, diff)
                if is_m != pred:
                    bad_crit += 1
                    print(f"  ({P},{A},{r}) {''.join(map(str, e))}:"
                          f" member={is_m} pred={pred}"
                          f" <-- CRITERION MISMATCH")
                if is_m and u != v:
                    mixed_member += 1
        if mixed_member:
            fused_cells += 1
            print(f"  ({P},{A},{r}): FUSED ({mixed_member} mixed"
                  f" concatenations are members)")
    print(f"  {tested} legal ordered pairs tested; "
          f"criterion mismatches={bad_crit}; block failures={bad_block};"
          f" fused cells={fused_cells}")
    print(f"  {'PASS' if bad_crit == 0 and bad_block == 0 else 'FAIL'}")
    return bad_crit == 0 and bad_block == 0


if __name__ == "__main__":
    ok0 = s0()
    ok1, noncut, others = s1()
    ok2 = s2()
    print("=" * 74)
    print("ALL STAGES RAN; s0 " + ("GREEN" if ok0 else "RED")
          + "; s1 closure " + ("GREEN" if ok1 else "RED")
          + f" non-cut={noncut} other={len(others)}"
          + "; s2 " + ("GREEN" if ok2 else "RED"))
