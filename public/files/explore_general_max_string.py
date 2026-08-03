"""The next storey: the boundary family at arbitrary-period quadratic
windows -- and the max-string theorem that turns out to hold at EVERY
window at once.

THE QUESTION
------------
The trailing-gate conjecture (readable at bounded delay iff the map
acts continuously on the completion; unit-ness what continuity of the
inverse pair costs) carries proved discontinuity cells at Zeckendorf,
every constant-a window, every [0; 1, a] period-2 window, and the
period-3 window [0; 1, 1, 2]; at [0; 1, 1, a], a = 2..7, the
BOUNDARY FAMILY witnesses the gate by measurement
(explore_max_string_witness.py). This rig takes the storey up: does
the same machinery -- one proved image family plus a residue-class
scan -- carry the gate at ARBITRARY period, alphabets mixed, a_1 > 1
included? Four fresh windows at periods 4 and 5, maps xm for
m = 2..7.

THE WINDOWS (vocabulary identical to explore_ostrowski_window.py's
engine, re-derived from its code before this freeze). Weights
q_0 = 1, q_1 = a_1, q_k = a_k q_{k-1} + q_{k-2} with
a_k = tail[(k-1) mod P]; convergent numerators p_0 = 0, p_1 = 1,
p_k = a_k p_{k-1} + p_{k-2}. Digits by greedy descent; classical
legality: b_0 <= a_1 - 1, b_k <= a_{k+1} = tail[k mod P] for k >= 1,
and b_k at its cap forces b_{k-1} = 0.

  V1  tail (1, 1, 1, 2)     period 4, a_1 = 1
  V2  tail (2, 1, 3, 1)     period 4, a_1 = 2
  V3  tail (1, 2, 1, 1, 3)  period 5, a_1 = 1
  V4  tail (3, 1, 2, 2, 1)  period 5, a_1 = 3

THE HAND-ATTACK (pre-engine, on paper)
------------------------------------------------------------------
THE MAX-STRING THEOREM (arbitrary tail -- periodicity never used).
Greedy on q_K - 1: since q_K - 1 = a_K q_{K-1} + (q_{K-2} - 1) and
q_{K-2} - 1 < q_{K-2} <= q_{K-1}, the top greedy digit is
d_{K-1} = a_K and the remainder is q_{K-2} - 1: the string recurses
in steps of TWO. Base cases: q_1 - 1 = a_1 - 1 (the single digit
d_0 = a_1 - 1, legal at its cap); q_0 - 1 = 0 (empty). Hence

  even K:  d_{K-1-2i} = a_{K-2i} for i = 0..(K-2)/2
           (support K-1, K-3, ..., 1; bottom d_0 = 0, d_1 = a_2),
  odd K:   d_{K-1-2i} = a_{K-2i} for i = 0..(K-3)/2, d_0 = a_1 - 1
           (support K-1, K-3, ..., 2, and 0; bottom d_1 = 0,
            d_2 = a_3 from K >= 3 -- K = 1 is the single digit
            a_1 - 1).

Legality: every written digit sits AT its cap (cap(k) = a_{k+1}) over
a zero, and the forced-zero rule is satisfied position by position;
uniqueness of the legal string closes it -- the pattern IS the greedy
string. Telescope check: summing a_{K-2i} q_{K-1-2i} = q_{K-2i} -
q_{K-2i-2} telescopes to q_K - q_0 = q_K - 1 (even K) or
q_K - q_1 + (a_1 - 1) q_0 = q_K - 1 (odd K). The two parities put
their support on DISJOINT position parities, so the bottoms differ at
the lowest position whose cap admits a nonzero digit -- d_0 when
a_1 >= 2 (a_1 - 1 against 0), d_1 when a_1 = 1 (a_2 against 0): the
flip-address conjecture is DERIVED for this family, every window at
once. Hand instances, both fresh period-4 windows: V1 has q =
1, 1, 2, 3, 8, 11, ...; q_4 - 1 = 7 = (0, 1, 0, 2) and q_5 - 1 =
10 = (0, 0, 1, 0, 1) -- flip at d_1. V2 has q = 1, 2, 3, 11, 14,
39, ...; q_4 - 1 = 13 = (0, 1, 0, 1) and q_5 - 1 = 38 =
(1, 0, 3, 0, 2) -- flip at d_0.

THE BOUNDARY FAMILY (the input side; the argument of
explore_max_string_witness.py, unchanged). delta_K = q_K theta - p_K
alternates in sign with K and shrinks. For knobs (r, u, t) and a
residue class (q_K + u q_{K-r}, p_K + u p_{K-r}) = (t, c) mod m held
at BOTH K-parities, the inputs x_K = (q_K + u q_{K-r} - t)/m
converge to the point (c - t theta)/m, which sits OFF the coding
boundary orbit iff NOT (m | t and c = 0) -- exclude exactly that
class -- while the images m x_K = q_K + u q_{K-r} - t converge to
the boundary point -t theta, sided by K's parity: the image strings
alternate between the two codings of one point forever. TRANSPLANT
FLAGS: (i) the flip-address expectation for general t is IMPORTED
from the period <= 3 storeys (derived above only for t = 1, u = 0);
left as an observable print. (ii) the odometer delay <= period + 1
is imported from periods 1..3; D4 tests it out of sample.

THE DESIGN (checks; greedy extraction only -- no closed form from
the proof enters the digit path; predictions frozen before the run)
------------------------------------------------------------------
D0  Positive control, every window: greedy digits reconstruct n
    exactly and are legal, all n < 100000. PREDICTION: green.
D1  (the theorem check) Every window, K = 1..40: the greedy string
    of q_K - 1 equals the alternating cap-filling above, and the
    bottom (d_0, d_1, d_2) is (0, a_2, 0) at even K against
    (a_1 - 1, 0, a_3) at odd K. PREDICTION: all green (derived;
    theorem-shaped).
D2  (the class scan) Every window, every m in {2..7}: the smallest
    (r in {1,2}, u in 0..m-1, t in 1..m) whose class
    (q_K + u q_{K-r}, p_K + u p_{K-r}) = (t, c) mod m holds both
    K-parities at K <= 400, the boundary class (m | t, c = 0)
    excluded. PREDICTION: a class exists at every one of the 24
    cells. KILL AS OBSERVABLE: any cell with none.
D3  (the witness) Every cell with a class: the family
    x_K = (q_K + u q_{K-r} - t)/m over the class members (z > 0
    guarded) -- consecutive input agreement depths (the kill is a
    bounded run), and the image low-4 (d_0, d_1, d_2, d_3) per
    member. PREDICTION: depths grow throughout every family; within
    each K-parity the low-4 is eventually constant and the two
    parity values differ inside the low-4 window. A cell whose two
    parity values coincide on the low-4 prints as the finding (a
    deeper flip), not a failure.
D4  (the unit control) Every window: the odometer n + 1 is readable
    at output depth t = 6 with some lookahead c <= period + 1
    (readability = every input low-(t+c) class maps into one output
    low-t class, n < 100000). PREDICTION: readable at every window
    at c <= period + 1 (the transplant flag (ii) on trial).
D5  (the gate scan) Every window, map x2, N in {30000, 100000,
    300000}: CAP(N) = deepest consecutive-pair input agreement
    (sorted digit strings) and A(N) = deepest such agreement among
    pairs whose image low-3 prefixes differ. PREDICTION: A(N)
    tracks CAP(N) within a few everywhere -- the gate binds; A
    frozen while CAP rises >= 3 reads as a readable plateau, the
    conjecture refuted at that window.

RESOURCE: estimate ~2 min (the D5 sorts at N = 300000 x 4 windows
dominate), well under 512MB (digit strings as tuples of small ints,
~30 positions at the largest N).

THE EXTENSION (design frozen before the second run; D2's one kill
applied). The first run's D2 found no class at V1, m = 5 with
r <= 2 -- the same shape as explore_max_string_witness.py's D6/D8
kills, answered there by widening the knob set. D6 widens r alone:
r in {1..6}, same u and t ranges, same exclusion, the killed cell
only. PREDICTION: a class exists at some r <= 6 and its family
passes the D3 checks (depths grow, parity-split low-4). KILL AS
OBSERVABLE: none at r <= 6.

RUN RECORD
----------
Two runs: D0-D5, then D6 added after D2's one kill (design frozen
above before the second run). 7.5 s, 124 MB peak each.

FINDINGS (post-run)
-------------------
D0: zero reconstruction failures, zero legality failures, every
window, n < 100000 (the positive control, printed before any
verdict was read).
D1: THE THEOREM VERIFIED -- zero pattern mismatches at every
window, K = 1..40, and the bottoms land exactly as derived:
even K (0, a_2, 0) against odd K (a_1 - 1, 0, a_3) -- V1
(0,1,0)/(0,0,1), V2 (0,1,0)/(1,0,3), V3 (0,2,0)/(0,0,1), V4
(0,1,0)/(2,0,2).
D2: a class at 23 of 24 cells with r <= 2 -- 15 of them the
plain max-string class (u = 0, t = 1). THE KILL FIRED once: V1,
m = 5, none at r <= 2, K <= 400.
D3: WITNESS CONFIRMED AT EVERY CELL WITH A CLASS -- input
agreement depths grow throughout every family (e.g. V1 m=2:
4, 7, 9, ..., 25; V4 m=5: 25, 60, ..., 225), and the image low-4
splits by K-parity everywhere. At the t = 1 cells the two values
are exactly the max-string bottoms (the two codings of -theta:
V1 (0,0,1,0)/(0,1,0,2), V2 (1,0,3,0)/(0,1,0,1), V3
(0,0,1,0)/(0,2,0,1), V4 (2,0,2,0)/(0,1,0,2)); the other-t cells
split at d_0 or d_1 (V2 m=6 t=2: (1,0,0,1)/(0,0,3,0), first odd
member (1,0,1,0) before settling -- eventually constant as
predicted; V3 m=7 t=3: (0,1,0,0)/(0,0,0,1); V4 m=4 t=2:
(1,0,2,0)/(2,0,0,2)). The flip sits at d_0 or d_1 at every cell
-- never deeper in the low-4 window.
D6: the widened scan fills the killed cell -- class
(r,u,t,c) = (3,1,2,2), K = 13, 18, 29, ..., depths 13, 18, 29,
..., 77 growing, images (0,0,0,2) odd against (0,1,0,0) even:
24 of 24.
D4: the odometer reads at c_min = 1 at every window -- far
inside the imported period + 1 bound (5, 5, 6, 6).
D5: A(N) tracks CAP(N) within 1 at every window and every N
(V1: CAP 19/20/23, A 18/20/22; V2: 14/16/17, A 13/15/17; V3:
16/17/19, A 15/17/18; V4: 13/15/16, A 12/14/15) -- no readable
plateau anywhere; the kill missed.

THE READING: the storey generalizes -- and the proof burden
collapses onto one lemma. The max-string theorem (the alternating
cap-filling of q_K - 1, flipping whole by the parity of K at the
lowest position whose cap admits a nonzero digit) is proved at
ARBITRARY tail, periodicity never used: a two-line greedy
recursion in steps of 2. It hands every window its image family
at once -- where the period <= 3 storeys each built a bespoke
comb telescope, the general storey needs no comb at all. The
boundary family then witnesses xm gated at all 24 (window, m)
cells (rule at scanned scope: K <= 400, depths to 225), the unit
side reads (the odometer at lookahead 1 everywhere), and the
range scan finds no readable plateau. What stays measured per
cell is only CLASS EXISTENCE -- a both-parity nontrivial residue
class of (q_K + u q_{K-r}, p_K + u p_{K-r}) mod m -- whose knob
budget is arithmetic per window (V1 m=5 needed r = 3), and whose
general proof is the storey's remaining open beside the odd-a
comb freeze.
"""

import sys

WINDOWS = [
    ("V1 (1,1,1,2)", (1, 1, 1, 2)),
    ("V2 (2,1,3,1)", (2, 1, 3, 1)),
    ("V3 (1,2,1,1,3)", (1, 2, 1, 1, 3)),
    ("V4 (3,1,2,2,1)", (3, 1, 2, 2, 1)),
]

M_RANGE = range(2, 8)
K_SCAN = 400


def build_qp(tail, count):
    """Weights and convergent numerators to index count-1 inclusive.
    q_0=1, q_1=a_1, q_k = a_k q_{k-1} + q_{k-2}; p_0=0, p_1=1, same
    recurrence; a_k = tail[(k-1) % P]."""
    q = [1, tail[0]]
    p = [0, 1]
    for k in range(2, count):
        a_k = tail[(k - 1) % len(tail)]
        q.append(a_k * q[-1] + q[-2])
        p.append(a_k * p[-1] + p[-2])
    return q, p


def build_q_top(tail, top_value):
    """Weights until q exceeds top_value (engine-identical)."""
    q = [1, tail[0]]
    k = 2
    while q[-1] <= top_value:
        a_k = tail[(k - 1) % len(tail)]
        q.append(a_k * q[-1] + q[-2])
        k += 1
    return q


def greedy_digits(v, q):
    """Greedy Ostrowski digits of v >= 0, low-to-high, len(q)."""
    d = [0] * len(q)
    for k in range(len(q) - 1, -1, -1):
        if q[k] <= v:
            b = v // q[k]
            d[k] = b
            v -= b * q[k]
    return d


def legality_failures(d, tail):
    """Violations of the classical Ostrowski conditions."""
    fails = 0
    if d[0] > tail[0] - 1:
        fails += 1
    for k in range(1, len(d)):
        a_next = tail[k % len(tail)]
        if d[k] > a_next:
            fails += 1
        if d[k] == a_next and d[k - 1] != 0:
            fails += 1
    return fails


def agreement_depth(d1, d2):
    """First position where two digit lists differ (list lengths may
    differ; missing high digits read as 0)."""
    n = max(len(d1), len(d2))
    for i in range(n):
        a = d1[i] if i < len(d1) else 0
        b = d2[i] if i < len(d2) else 0
        if a != b:
            return i
    return n


def cap_at(k, tail):
    return tail[0] - 1 if k == 0 else tail[k % len(tail)]


def max_string_pattern(K, tail, length):
    """The hand-derived alternating cap-filling for q_K - 1."""
    d = [0] * length
    k = K - 1
    while k >= 1:
        a_top = tail[(k + 1 - 1) % len(tail)]  # a_{k+1}
        d[k] = a_top
        k -= 2
    if K % 2 == 1:
        d[0] = tail[0] - 1
    return d


def d0_control():
    print("== D0: positive control (reconstruct + legality) ==")
    total_fail = 0
    for name, tail in WINDOWS:
        q = build_q_top(tail, 100000)
        bad = 0
        for n in range(100000):
            d = greedy_digits(n, q)
            if sum(b * q[k] for k, b in enumerate(d)) != n:
                bad += 1
            elif legality_failures(d, tail):
                bad += 1
        print(f"  {name}: failures {bad} / 100000")
        total_fail += bad
    assert total_fail == 0, "D0 control failed"


def d1_theorem():
    print("== D1: the max-string theorem, K = 1..40 ==")
    for name, tail in WINDOWS:
        q, _ = build_qp(tail, 42)
        mism = 0
        for K in range(1, 41):
            d = greedy_digits(q[K] - 1, q)
            pat = max_string_pattern(K, tail, len(q))
            if d != pat:
                mism += 1
        # bottoms
        even_ok = odd_ok = True
        for K in range(2, 41):
            d = greedy_digits(q[K] - 1, q)
            bot = (d[0], d[1], d[2])
            if K % 2 == 0:
                if bot != (0, tail[1 % len(tail)], 0):
                    even_ok = False
            else:
                if bot != (tail[0] - 1, 0, tail[2 % len(tail)]):
                    odd_ok = False
        print(f"  {name}: pattern mismatches {mism}, "
              f"even bottom (0,{tail[1 % len(tail)]},0) {'OK' if even_ok else 'FAIL'}, "
              f"odd bottom ({tail[0]-1},0,{tail[2 % len(tail)]}) {'OK' if odd_ok else 'FAIL'}")
        assert mism == 0 and even_ok and odd_ok, f"D1 failed at {name}"


def find_class(tail, m, r_range=(1, 2)):
    """Smallest (r, u, t) with a both-parity class (t, c) mod m at
    K <= K_SCAN, boundary class (m | t and c == 0) excluded.
    Returns (r, u, t, c, members) or None."""
    q, p = build_qp(tail, K_SCAN + 1)
    for r in r_range:
        for u in range(m):
            for t in range(1, m + 1):
                by_c = {}
                for K in range(r + 2, K_SCAN + 1):
                    z = q[K] + u * q[K - r]
                    if z % m != t % m:
                        continue
                    c = (p[K] + u * p[K - r]) % m
                    if t % m == 0 and c == 0:
                        continue  # the boundary class
                    by_c.setdefault(c, []).append(K)
                for c, ks in sorted(by_c.items()):
                    if any(K % 2 == 0 for K in ks) and any(K % 2 == 1 for K in ks):
                        return r, u, t, c, ks
    return None


def witness_report(name, tail, m, found):
    """Print the D3 witness rows for one (window, m) class."""
    r, u, t, c, ks = found
    q, _ = build_qp(tail, K_SCAN + 1)
    members = [K for K in ks if q[K] + u * q[K - r] - t > 0][:10]
    pad = 2
    while True:
        qlong, _ = build_qp(tail, max(members) + pad)
        if qlong[-1] > qlong[max(members)] + u * qlong[max(members) - r]:
            break
        pad += 1
    xs = [(K, (qlong[K] + u * qlong[K - r] - t) // m) for K in members]
    depths = []
    prev = None
    rows = []
    for K, x in xs:
        dx = greedy_digits(x, qlong)
        img = greedy_digits(m * x, qlong)
        if prev is not None:
            depths.append(agreement_depth(prev, dx))
        prev = dx
        rows.append((K, K % 2, tuple(img[:4])))
    odd_l4 = [row[2] for row in rows if row[1] == 1]
    even_l4 = [row[2] for row in rows if row[1] == 0]
    print(f"  {name} m={m}: class (r,u,t,c)=({r},{u},{t},{c}) "
          f"K={members}")
    print(f"    depths {depths}")
    print(f"    image low-4 odd K {odd_l4}")
    print(f"    image low-4 even K {even_l4}")


def d2_d3_boundary():
    print("== D2/D3: class scan + boundary-family witness ==")
    kills = 0
    for name, tail in WINDOWS:
        for m in M_RANGE:
            found = find_class(tail, m)
            if found is None:
                print(f"  {name} m={m}: NO CLASS at K <= {K_SCAN}  <-- KILL")
                kills += 1
                continue
            witness_report(name, tail, m, found)
    print(f"  D2 kills: {kills} / {4 * len(list(M_RANGE))}")


def d6_widened():
    print("== D6: the killed cell V1 m=5, r widened to 1..6 ==")
    name, tail = WINDOWS[0]
    found = find_class(tail, 5, r_range=(1, 2, 3, 4, 5, 6))
    if found is None:
        print("  V1 m=5: NO CLASS at r <= 6, K <= 400  <-- KILL")
    else:
        witness_report(name, tail, 5, found)


def readable_at(tail, fmap, N, t, c):
    """Is the map readable at output depth t with lookahead c?
    Every input low-(t+c) class must map into one output low-t
    class."""
    q = build_q_top(tail, 4 * N + 16)
    seen = {}
    for n in range(N):
        key = tuple(greedy_digits(n, q)[: t + c])
        out = tuple(greedy_digits(fmap(n), q)[:t])
        if key in seen:
            if seen[key] != out:
                return False
        else:
            seen[key] = out
    return True


def d4_odometer():
    print("== D4: the odometer n+1, output depth 6 ==")
    for name, tail in WINDOWS:
        P = len(tail)
        cmin = None
        for c in range(0, P + 4):
            if readable_at(tail, lambda n: n + 1, 100000, 6, c):
                cmin = c
                break
        verdict = "OK" if (cmin is not None and cmin <= P + 1) else "FAIL"
        print(f"  {name}: c_min = {cmin} (period+1 = {P+1}) {verdict}")
        assert cmin is not None and cmin <= P + 1, f"D4 failed at {name}"


def d5_gate_scan():
    print("== D5: gate scan, map x2 ==")
    for name, tail in WINDOWS:
        line = []
        for N in (30000, 100000, 300000):
            q = build_q_top(tail, 2 * N + 8)
            recs = []
            for n in range(N):
                d = tuple(greedy_digits(n, q))
                img3 = tuple(greedy_digits(2 * n, q)[:3])
                recs.append((d, img3))
            recs.sort()
            cap = 0
            aval = 0
            for i in range(1, len(recs)):
                dep = agreement_depth(list(recs[i - 1][0]), list(recs[i][0]))
                if dep > cap:
                    cap = dep
                if recs[i - 1][1] != recs[i][1] and dep > aval:
                    aval = dep
            line.append((N, cap, aval))
        print(f"  {name}: " + "  ".join(
            f"N={N}: CAP={cap} A={a}" for N, cap, a in line))


def main():
    d0_control()
    d1_theorem()
    d2_d3_boundary()
    d6_widened()
    d4_odometer()
    d5_gate_scan()
    print("ALL CHECKS COMPLETE")


if __name__ == "__main__":
    sys.exit(main())
