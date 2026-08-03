"""
The cover-exclusion twins, twin 2: the two-fat-slice exclusion.

The realizability law's one open direction (explore_realizability.py,
prediction 4): for d = q*q' a product of two odd
primes q < q', no nonzero (Phi_d)-codeword lives inside a triangle
exponent set E(A, B, D) at D <= q-2 -- proved by the slice forcing
whenever q' > 3(q-1)/2, censused empty at d = 143 and 221, OPEN in
the close-prime zone. Bar: a proof or a refuting
witness, never a re-walk census.

THE REDUCTION. Slices: write
Z/d = Z/q x Z/q' (CRT), c = sum_x delta_x (x) gamma_x. Membership
c in (Phi_d) is EXACTLY pairwise congruence of the slices mod
(Phi_q') [evaluation at (zeta, theta): for each primitive theta the
x-vector lies in (Phi_q) = span(all-ones)]. With q' prime,
(Phi_q') = span(all-ones) too, so slices differ by constants:

    c  =  1_q (x) gamma  +  lambda (x) 1_q'      (the evader form)

and conversely every such tensor-sum is a codeword. Support:
supp c = {(x, j) : lambda[x] + gamma[j] != 0} -- the complement of a
matched-level-set pattern. Line capacities (any mod-q or mod-q' line
meets the lattice triangle in <= D+1 <= q-1 points) force every
lambda-level-set to pair with a gamma-level-set and vice versa:
matched partitions {S_i} of Z/q, {L_i} of Z/q', r >= 2 blocks, with
E containing every off-diagonal block S_i x L_j (i != j).

PREDICTIONS (stated before the run):
 P1 (criterion, proved): THE ROOK REFORMULATION. A nonzero
    (Phi_d)-codeword supported in E(A, B, D) exists iff A, B are
    both units (else some grid row/column is empty of E and its
    full complement line connects everything) and the complement
    of E(1, A^-1 B, D) in the q x q' grid is rook-DISCONNECTED
    (two complement cells adjacent iff same row or same column):
    disconnection components group into the matched partitions, and
    any matched partition yields a codeword (distinct level values
    exist for p > r). Verified here PER SCALING CLASS against the
    kernel census: d = 143 and 221 (both must
    stay empty/connected) and d = 323 = 17*19, the smallest
    previously-uncensused instance (fresh cross-check AND a new
    exclusion result). Exclusion at D = q-2 closes all D below
    (E is monotone in D).
 P2 (rule, proved): THE COUNTING GATE. A 2-block pattern
    (a, beta) = (|S_1|, |L_1|) needs N = a*q' + beta*q - 2*a*beta
    cells, and identically N = [q*q' - (2a-q)(2beta-q')]/2, so
    |E| <= (D+1)(D+2)/2 = q(q-1)/2 forces
        (2a - q)(2beta - q') >= q(q' - q + 1).
    Max product over the box (a <= q-1, q'-q+1 <= beta <= q-1,
    both bounds = row capacity) is (q-2)(2q-2-q'): pure counting
    EXCLUDES every pair with q' > (3q-4)/2 -- reproving the
    slice-forcing boundary by counting alone (formally inside
    3(q-1)/2, but the only integer between is 3(q-1)/2 itself,
    divisible by 3: the excluded prime sets are IDENTICAL).
    THE OPEN ZONE = pairs with q' <= (3q-4)/2.
 P3 (rule, proved on the stated zone): THE WEAK STAIRCASE BOUND.
    Column lattice-counts f are the covering multiplicities of Z/q'
    by D+1 intervals A_u = [-Bu, -Bu+u], sizes 1..D+1, AP left ends
    (rows mirror, modulus q). Whenever 8s <= modulus:
        #{c : f(c) >= D+1-s}  <=  2s+1.
    Proof: two deep points at circular distance delta share >=
    D+1-2s good u's, and A_u (length u+1) cannot hold both when
    u < delta, so pairwise s_i + s_j >= dist(c_i, c_j); if k >=
    2s+2, all pairwise distances are <= 2s, the set sits in a
    +-2s window of any member (proper arc since 8s <= modulus),
    additive distances make its span <= 2s, so k <= 2s+1 --
    contradiction. (The clustering step needs the zone; outside it
    the bound is tallied here as data, never asserted.) At s = 0
    this is full-line uniqueness (at most ONE full column, and only
    B == 1 mod q' has one -- the u = 0, 1 conditions force it).
    Corollary with P2: every gate-feasible config is weak-killed
    inside the proved zone at (11,13) and (13,17) -- the two
    smallest open pairs are PROVED, before any sweep. (The
    bound became unconditional below half-range -- the counting
    proof, explore_staircase_reduction.py R1 -- lifting the kill
    count from 41 to 46 pairs; see the kill classification.)
 P4 (tested here as a sweep; a proved rule,
    explore_staircase_reduction.py R12-R14): THE STRONG STAIRCASE
    BOUND, half-range: #{c : f(c) >= D+1-s} <= s+1 for s < (D+1)/2,
    every B (the nested case B == 1 achieves equality; nesting
    extremal). False past half-range.
    Since it holds: every config dies -- the gate forces
    a > q/2, beta > q'/2 (or mirror); demand "q'-beta columns with
    >= a cells" needs q'-beta <= q-a, demand "q-a rows with >= beta
    cells" needs q-a <= q-beta, together q' <= q, contradiction --
    so twin 2 closes at EVERY odd prime pair. The twins' residual
    would compress to this one lattice statement.
 P5 (the sweep): rook-connectivity of the complement of
    E(1, B, q-2) for EVERY open-zone pair q <= Q_CAP and EVERY unit
    B up to inversion (B ~ B^-1 = the i<->j swap). Prediction: no
    disconnection anywhere (the exclusion). A disconnection is a
    REFUTING WITNESS -- the composite realizability row falls at
    that pair -- and is reconstructed as an explicit codeword and
    re-verified over F_p.
 P6 (scope probe): the strong
    bound decoupled from pairs -- every prime m <= 53, every
    D in [3, m-2], every B. If it holds, the lemma is native to
    the interval family (a proof hunt targets the general
    statement); a violation here at an off-pair (m, D) shape would
    narrow the lemma without touching the exclusion.

RESULTS (the run below prints the record; all confirmed):
  P1 kernel == rook at every unit scaling class, kernel empty at
     every non-unit class: 143 (62 + 24 classes), 221 (98 + 30),
     323 (146 + 36, ~17 s; NEW: d = 323 excluded at D = 15 ->
     D_min(323) = 16 = q_min - 1, extending the composite row's
     census beyond the earlier battery).
  P2 identity and boundary brute-checked (all odd-prime pairs
     q <= 31, q' < 3q); gate-closed sanity pair (11,17) rook-
     connected at every B.
  P3 weak bound: ZERO in-zone violations across all 534,592 swept
     line profiles -- and 348,488 outside-zone excesses, so the
     proved zone is real, not caution. Full-line count <= 1 per
     direction, equality iff B == 1 mod that prime.
  P4 strong half-range bound: ZERO violations across all 534,592
     profiles -- and now a proved rule at every (m, D, B)
     (explore_staircase_reduction.py R12-R14: lattice counting,
     analytic m >= 213 + exhaustive below). The half-range cut is
     exactly right: every outside-zone weak excess is a fortiori
     a strong excess (cnt > 2s+1 > s+1), and since in-range strong
     violations are zero, ALL 348,488 excesses sit at or beyond
     half-range -- the bound genuinely fails there (the two-stack
     construction is the suspected mechanism, not verified per-B).
  P5 sweep: ALL open-zone pairs q <= 97 (98 pairs, every unit B up
     to inversion, ~125 s): complement rook-CONNECTED everywhere --
     NO witness. Kill classification: weak+gate PROVE 46 of the 98
     outright (including (11,13) and (13,17); 41 by the zoned weak
     bound, +5 more by the unconditional weak scope: (37,47), (61,79),
     (79,103), (83,107), (97,127)); and the staircase closed region
     (explore_staircase_reduction.py R7-R11: equicoverage, the
     complementation duality, time reversal, the product bound)
     proves the needed strong-bound instances at (q', q-2) for
     EVERY unit B at ALL 98 pairs -- D = q-2 is odd, so only the
     coverage cap is needed, and the m = q side is equicoverage.
     The staircase lemma is a proved rule at EVERY
     (m, D, B), so the zone censuses are now benchmarks of the
     cheap arithmetic test (98/98 at q <= 97; 1103/1130 at
     q <= 400), not the closure's frontier.

  P6 decoupled probe: ZERO violations across all 11,416 (m, D, B)
     profiles (primes m <= 53, D in [3, m-2], all B) -- the lemma
     is native to the interval family, not the pair geometry.

Tier: P1, P2, P3 rule/criterion (proved; code-verified as stated).
P4: reduced to two caps, proved on the closed region,
and closed (explore_staircase_reduction.py R12-R14) -- a
rule with complete coverage at every (m, D, B): TWIN 2'S EXCLUSION
HOLDS AT EVERY ODD PRIME PAIR (kill algebra + gate + R7/R8 + the
lemma; no covering system with two fat slices evades at any
two-prime d, any D <= q-2). P5 observation at the swept range.
The realizability law's composite row now rests on: slice forcing
(q' > 3(q-1)/2), counting gate (q' > (3q-4)/2, subsumes), the
staircase lemma (every remaining pair, unconditional), and past two
prime factors the gon theorem + coset collapse
(explore_multiprime_exclusion.py); the weak staircase (46 close
pairs) and the zone censuses survive as benchmarks of the cheap
per-instance tests.

Classical contacts: Fine-Wilf (a complement gap of length
>= q+q'-1 forces r = 1 -- every evader gap is shorter); the
modular postage-stamp / h-basis literature (interval covering
multiplicities); the coset-cover bound -- both twins are
"a degenerate cover must not beat CRT" statements, and the
staircase bound is twin 2's version of one-class-per-modulus.

Runs in ~3.5 min, tiny memory. ALL CHECKS PASSED (16).
"""

import sys, time
from math import gcd

CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok' if cond else 'FAIL'}] {msg}")
    assert cond, msg

def section(t):
    print(); print("=" * 72); print(t); print("=" * 72)

# ---------------------------------------------------------------- helpers

def is_prime(n):
    if n < 2: return False
    q = 2
    while q * q <= n:
        if n % q == 0: return False
        q += 1
    return True

def factorize(n):
    fs, q = {}, 2
    while q * q <= n:
        while n % q == 0:
            fs[q] = fs.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1: fs[n] = fs.get(n, 0) + 1
    return fs

def mult_order(x, p):
    o, t = 1, x % p
    assert t != 0
    while t != 1:
        t = t * x % p
        o += 1
    return o

def primitive_root(p):
    n = p - 1
    qs = list(factorize(n))
    for g in range(2, p):
        if all(pow(g, n // q, p) != 1 for q in qs):
            return g

def units_mod(n):
    return [u for u in range(n) if gcd(u, n) == 1]

def exponent_set(A, B, D, d):
    E = set()
    for i in range(D + 1):
        for j in range(D + 1 - i):
            E.add((A * i + B * j) % d)
    return sorted(E)

def find_p(d):
    """Smallest prime p == 1 mod d."""
    p = d + 1
    while not is_prime(p):
        p += d
    return p

# ------------------------------------------------- the kernel machinery
# (the tester from explore_realizability.py, copied verbatim -- scripts
#  stay standalone)

class CodeTester:
    """Codewords of (Phi_d) over F_p, p = 1 mod d: c with c(zeta) = 0
    at every primitive d-th root zeta. kernel(E) returns a nonzero
    codeword supported on E (as a dict e -> coeff) or None."""

    def __init__(self, d, p):
        assert is_prime(p) and (p - 1) % d == 0, (d, p)
        self.d, self.p = d, p
        g = primitive_root(p)
        z = pow(g, (p - 1) // d, p)
        assert mult_order(z, p) == d
        self.zpow = [pow(z, t, p) for t in range(d)]
        self.units = units_mod(d)

    def kernel(self, E):
        d, p, zp = self.d, self.p, self.zpow
        cols = len(E)
        pivots = {}
        order = []
        for u in self.units:
            row = [zp[(u * e) % d] for e in E]
            for c in order:
                f = row[c]
                if f:
                    pr = pivots[c]
                    row = [(x - f * y) % p for x, y in zip(row, pr)]
            lead = next((c for c in range(cols) if row[c]), None)
            if lead is None:
                continue
            inv = pow(row[lead], p - 2, p)
            row = [x * inv % p for x in row]
            for c in order:
                f = pivots[c][lead]
                if f:
                    pivots[c] = [(x - f * y) % p
                                 for x, y in zip(pivots[c], row)]
            pivots[lead] = row
            order.append(lead)
            if len(order) == cols:
                return None
        free = next(c for c in range(cols) if c not in pivots)
        vec = {E[free]: 1}
        for c, prow in pivots.items():
            v = (-prow[free]) % p
            if v: vec[E[c]] = v
        for u in self.units:
            s = sum(co * zp[(u * e) % d] for e, co in vec.items()) % p
            assert s == 0, "kernel vector fails codeword condition"
        return vec

def scaling_classes(d):
    """(A,B) with gcd(A,B,d)=1, up to joint unit scaling and swap."""
    seen = set()
    reps = []
    us = units_mod(d)
    for A in range(d):
        for B in range(d):
            if (A, B) in seen: continue
            if gcd(gcd(A, B), d) != 1: continue
            orbit = set()
            for u in us:
                a, b = u * A % d, u * B % d
                orbit.add((a, b)); orbit.add((b, a))
            seen |= orbit
            reps.append((A, B))
    return reps

# ------------------------------------------------- the rook machinery

def grid_profiles(q, qp, B, D):
    """E(1, B, D) in the q x qp CRT grid. Returns (Rmask, f, g):
    per-column E-row bitmasks, per-column and per-row LATTICE
    counts."""
    d = q * qp
    R = [0] * qp
    f = [0] * qp
    g = [0] * q
    for j in range(D + 1):
        z = B * j % d
        x = z % q
        c = z % qp
        for _ in range(D + 1 - j):
            R[c] |= 1 << x
            f[c] += 1
            g[x] += 1
            x += 1
            if x == q: x = 0
            c += 1
            if c == qp: c = 0
    return R, f, g

def rook_connected(q, qp, Rmask):
    """Is the complement of E rook-connected? Flood-fill over the
    row set through column complement masks. Returns (connected,
    row_component) -- row_component = rows reached from column 0's
    complement (meaningful only when disconnected)."""
    FULL = (1 << q) - 1
    M = [FULL ^ r for r in Rmask]
    comp = M[0]
    assert comp, "column 0 has no complement cell (capacity violated)"
    pend = list(range(1, qp))
    changed = True
    while changed:
        changed = False
        rem = []
        for c in pend:
            m = M[c]
            assert m, "a column has no complement cell"
            if m & comp:
                comp |= m
                changed = True
            else:
                rem.append(c)
        pend = rem
    return comp == FULL, comp

def open_zone_pairs(qcap):
    """All odd prime pairs q < q' with q' <= (3q-4)/2, q <= qcap."""
    out = []
    for q in range(11, qcap + 1, 2):
        if not is_prime(q): continue
        for qp in range(q + 2, (3 * q - 4) // 2 + 1, 2):
            if is_prime(qp):
                out.append((q, qp))
    return out

def feasible_configs(q, qp):
    """2-block configs (a, beta) passing the counting gate."""
    out = []
    for a in range(1, q):
        for beta in range(qp - q + 1, q):
            if (2 * a - q) * (2 * beta - qp) >= q * (qp - q + 1):
                out.append((a, beta))
    return out

def config_kill(q, qp, a, beta, col_bound, row_bound):
    """Is config (a, beta) killed by the per-level count bounds
    (functions level -> max #lines with >= level cells)? The four
    demands: q'-beta cols >= a; beta cols >= q-a; a rows >= q'-beta;
    q-a rows >= beta. Row and column capacities are both D+1 = q-1;
    the bounds differ only in their proved zones (moduli)."""
    col_d = [(qp - beta, a), (beta, q - a)]
    row_d = [(a, qp - beta), (q - a, beta)]
    return (any(need > col_bound(lv) for need, lv in col_d) or
            any(need > row_bound(lv) for need, lv in row_d))

INF = 10**9

def weak_bound(q, modulus):
    # #{lines >= level} <= 2s+1, s = (q-1) - level. PROVED
    # unconditionally for s < (D+1)/2 = (q-1)/2 (the counting proof,
    # explore_staircase_reduction.py R1 -- any modulus, any interval
    # positions); the clustering proof adds 8s <= modulus beyond
    # half-range. Elsewhere: no claim.
    def b(level):
        s = (q - 1) - level
        return 2 * s + 1 if (2 * s < q - 1 or 8 * s <= modulus) else INF
    return b

def strong_bound(q):
    # <= s+1 for s < (D+1)/2 = (q-1)/2; no claim past half-range (P4)
    def b(level):
        s = (q - 1) - level
        return s + 1 if s < (q - 1) / 2 else INF
    return b

# =======================================================================
section("I. THE ROOK REFORMULATION -- verified per scaling class "
        "(P1)")

census = {}
for (q, qp, p) in [(11, 13, 859), (13, 17, 443), (17, 19, 647)]:
    d, D = q * qp, q - 2
    t0 = time.time()
    tester = CodeTester(d, p)
    reps = scaling_classes(d)
    n_unit = n_nonunit = 0
    agree = True
    any_kernel = False
    for (A, B) in reps:
        vec = tester.kernel(exponent_set(A, B, D, d))
        if vec is not None:
            any_kernel = True
        if gcd(A, d) == 1 and gcd(B, d) == 1:
            n_unit += 1
            Bp = pow(A, -1, d) * B % d
            R, _, _ = grid_profiles(q, qp, Bp, D)
            conn, _ = rook_connected(q, qp, R)
            if (vec is None) != conn:
                agree = False
        else:
            n_nonunit += 1
            if vec is not None:
                agree = False
    census[(q, qp)] = (agree, any_kernel, n_unit, n_nonunit)
    check(agree and not any_kernel,
          f"d={d}={q}*{qp}: kernel == rook at all {n_unit} unit classes,"
          f" kernel empty at all {n_nonunit} non-unit classes,"
          f" exclusion at D={D} ({len(reps)} classes,"
          f" {time.time()-t0:.0f}s)")

check(census[(17, 19)] == (True, False, 146, 36),
      "NEW census result: d = 323 = 17*19 exhaustively excluded at"
      " D = 15 (146 unit + 36 non-unit classes, no codeword) ->"
      " D_min(323) = 16 = q_min - 1 by the proved q-gon upper bound"
      " (the smallest previously-uncensused two-fat-slice instance)")

# =======================================================================
section("II. THE COUNTING GATE (P2)")

ok = True
for q in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
    for qp in range(q + 2, 3 * q, 2):
        if not is_prime(qp): continue
        for a in range(1, q):
            for beta in range(qp - q + 1, q):
                N = a * qp + beta * q - 2 * a * beta
                if 2 * N != q * qp - (2 * a - q) * (2 * beta - qp):
                    ok = False
check(ok, "identity 2N = qq' - (2a-q)(2beta-q') exact on all boxes"
          " (odd prime pairs q <= 31, q' < 3q)")

ok = True
for q in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
    for qp in range(q + 2, 3 * q, 2):
        if not is_prime(qp): continue
        feasible = bool(feasible_configs(q, qp))
        if feasible != (2 * qp <= 3 * q - 4):
            ok = False
check(ok, "gate boundary exact: configs exist iff q' <= (3q-4)/2"
          " (the slice-forcing bound, re-proved by counting)")

q, qp = 11, 17   # gate-closed pair: counting alone proves exclusion
allc = all(rook_connected(q, qp, grid_profiles(q, qp, B, q - 2)[0])[0]
           for B in units_mod(q * qp))
check(allc, "gate-closed sanity (11,17): rook-connected at every B")

# =======================================================================
section("III + V. THE STAIRCASE BOUNDS AND THE SWEEP (P3, P4, P5)")

Q_CAP = 97
pairs = open_zone_pairs(Q_CAP)
print(f"  open zone to q = {Q_CAP}: {len(pairs)} pairs: {pairs}")

weak_zone_viol = weak_outside_viol = strong_viol = 0
full_line_bad = 0
disconnections = []
profiles = 0

def staircase_check(counts, D1, modulus):
    """counts = per-line lattice-counts of one direction; D1 = q-1
    (the line capacity D+1); modulus = that direction's prime.
    Tallies violations of the weak bound (split by proved zone
    8s <= modulus) and the strong half-range bound (s < D1/2).
    Returns n_full = #lines at full capacity."""
    global profiles, weak_zone_viol, weak_outside_viol, strong_viol
    profiles += 1
    srt = sorted(counts, reverse=True)
    n_full = 0
    for v in srt:
        if v >= D1: n_full += 1
        else: break
    for s in range(D1):              # level = D1 - s
        lvl = D1 - s
        cnt = 0
        for v in srt:
            if v >= lvl: cnt += 1
            else: break
        if cnt > 2 * s + 1:
            if 8 * s <= modulus: weak_zone_viol += 1
            else: weak_outside_viol += 1
        if s < D1 / 2 and cnt > s + 1:
            strong_viol += 1
    return n_full

t_all = time.time()
for (q, qp) in pairs:
    d, D = q * qp, q - 2
    t0 = time.time()
    nB = 0
    hit = False
    for B in units_mod(d):
        if pow(B, -1, d) < B:        # B ~ B^-1 (the i<->j swap)
            continue
        nB += 1
        R, f, g = grid_profiles(q, qp, B, D)
        conn, comp = rook_connected(q, qp, R)
        if not conn:
            disconnections.append((q, qp, B, comp))
            hit = True
        nfull = staircase_check(f, q - 1, qp)
        if nfull > 1 or (nfull == 1) != (B % qp == 1):
            full_line_bad += 1
        nfull = staircase_check(g, q - 1, q)
        if nfull > 1 or (nfull == 1) != (B % q == 1):
            full_line_bad += 1
    print(f"    ({q},{qp}): {nB} B-classes, "
          f"{'WITNESS!' if hit else 'connected everywhere'}"
          f" ({time.time()-t0:.0f}s)")

check(weak_zone_viol == 0,
      f"P3 weak staircase bound holds in its proved zone at every"
      f" swept B ({profiles} line profiles, 0 violations;"
      f" outside-zone tally: {weak_outside_viol})")
check(full_line_bad == 0,
      "P3 full-line uniqueness: <= 1 full line per direction,"
      " equality iff B == 1 mod that prime")
print(f"  P4 strong half-range staircase: {strong_viol} violations"
      f" across {profiles} profiles")
check(strong_viol == 0,
      "P4 strong staircase bound: no violation anywhere swept"
      " (a proved rule -- explore_staircase_reduction.py; the sweep stays as its"
      " independent witness)")

if disconnections:
    print("  *** REFUTING WITNESS(ES) FOUND ***")
    for (q, qp, B, comp) in disconnections:
        d = q * qp
        p = find_p(d)
        tester = CodeTester(d, p)
        vec = tester.kernel(exponent_set(1, B, q - 2, d))
        print(f"    (q,q')=({q},{qp}) B={B}: rook-disconnected;"
              f" kernel codeword over F_{p}: {vec}")
check(not disconnections,
      f"P5 THE SWEEP: complement rook-connected at every unit B for"
      f" all {len(pairs)} open-zone pairs q <= {Q_CAP} -- twin 2's"
      f" exclusion holds everywhere swept, no witness"
      f" ({time.time()-t_all:.0f}s)")

# =======================================================================
section("IV. THE KILL CLASSIFICATION (P3 corollary + P4 algebra)")

proved_weak = []
strong_only = []
for (q, qp) in pairs:
    cfgs = feasible_configs(q, qp)
    wc, wr = weak_bound(q, qp), weak_bound(q, q)
    sb = strong_bound(q)
    all_weak = all(config_kill(q, qp, a, b, wc, wr) for (a, b) in cfgs)
    all_strong = all(config_kill(q, qp, a, b, sb, sb) for (a, b) in cfgs)
    assert all_strong, (q, qp)       # the P4 algebra: must be universal
    (proved_weak if all_weak else strong_only).append((q, qp))

check((11, 13) in proved_weak and (13, 17) in proved_weak
      and len(proved_weak) == 46,
      f"weak+gate PROVE the exclusion outright at {len(proved_weak)}"
      f" of {len(pairs)} pairs (every gate-feasible config"
      f" weak-killed; 41 by the zoned bound, +5 by the"
      f" unconditional scope): {proved_weak}")
check(len(strong_only) + len(proved_weak) == len(pairs),
      f"P4 algebra universal: every config at every open pair is"
      f" strong-killed -- {len(strong_only)} pairs need the strong"
      f" bound: {strong_only}")

# the staircase closed region: proves the strong-bound instances
# at (q', q-2) for every unit B (explore_staircase_reduction.py
# R7-R11; m = q side = equicoverage, D = q-2 odd so the coverage cap
# alone carries the lemma via the reduction)
def _orbit(B, m):
    Bi = pow(B, m - 2, m)
    return {B % m, (1 - B) % m, Bi, (1 - Bi) % m,
            pow((1 - B) % m, m - 2, m),
            (B * pow((B - 1) % m, m - 2, m)) % m}

def _caps_proved(B, m, D):
    for Dp in (D, m - 3 - D):
        if Dp <= 0: return True
        for x in _orbit(B, m):
            b = min(x, m + 1 - x)
            if b * Dp < m: return True
            if (b * Dp // m + 1) * (Dp // b + 1) <= Dp // 2 + 1:
                return True
    return False

stair_open = [(q, qp) for (q, qp) in strong_only
              if not all(_caps_proved(B, qp, q - 2)
                         for B in range(2, qp))]
check(not stair_open,
      f"STAIRCASE CLOSURE: the R11 closed region alone proves the"
      f" strong bound at (q', q-2) for every unit B at all"
      f" {len(strong_only)} pending pairs (the arithmetic-test"
      f" benchmark) -- and the lemma is now a proved rule at"
      f" EVERY (m, D, B), so twin 2's exclusion holds at every odd"
      f" prime pair, not just q <= 97")

# also: the strong-kill algebra at arbitrary pairs (no cap), pure arith
ok = True
for (q, qp) in open_zone_pairs(199):
    sb = strong_bound(q)
    for (a, b) in feasible_configs(q, qp):
        if not config_kill(q, qp, a, b, sb, sb):
            ok = False
check(ok, "strong-kill algebra verified through q = 199: with P4 now"
          " a proved rule (explore_staircase_reduction.py), twin 2 closes at EVERY odd prime"
          " pair unconditionally")

# =======================================================================
section("VI. THE LEMMA'S NATIVE SCOPE -- decoupled (m, D, B) probe "
        "(P6)")

viol6 = 0
tested6 = 0
t6 = time.time()
for m in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]:
    for D in range(3, m - 1):            # up to D = m-2, the row regime
        for B in range(1, m):            # m prime: every B is a unit
            f = [0] * m
            for u in range(D + 1):
                start = (-B * u) % m
                for _ in range(u + 1):
                    f[start] += 1
                    start += 1
                    if start == m: start = 0
            srt = sorted(f, reverse=True)
            tested6 += 1
            for s in range((D + 2) // 2):        # s < (D+1)/2
                lvl = D + 1 - s
                cnt = 0
                for v in srt:
                    if v >= lvl: cnt += 1
                    else: break
                if cnt > s + 1:
                    viol6 += 1
check(viol6 == 0,
      f"P6 the strong staircase bound holds DECOUPLED from pairs:"
      f" every prime m <= 53, every D in [3, m-2], every B"
      f" ({tested6} profiles, 0 violations, {time.time()-t6:.0f}s)"
      f" -- the lemma is native to AP-placed shrinking intervals,"
      f" not to the pair geometry")

print()
print(f"ALL CHECKS PASSED ({CHECKS})")
