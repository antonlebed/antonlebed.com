"""
The realizability law at bounded degree (MOONSHOT probe, P86).

The curve skeleton's sharp residual (LOGIC.md SI), taken with the
P82/P83 bar: which torsion orders d does a degree-D curve reach
through the codeword species? The torsion-menu law counts MONOMIALS
(q_min(d) <= M); degree caps starve exponent reachability separately
-- before this chart the only censused case was conics missing
25-torsion (P82-P7). Bar: a LAW for all (d, D), proved mechanisms,
exhaustive censuses, never a bare table.

Setting (P82 inherited): a unit pair of torsion order d is
codeword-species stable for some [f = 0], deg f <= D, iff its
collected fiber is a nonzero codeword of (Phi_d) in F_p[T]/(T^d - 1).
Writing the pair as (theta^A, theta^B), theta of order d, the
monomial x^i y^j contributes exponent Ai + Bj mod d, so the reachable
supports are subsets of the TRIANGLE EXPONENT SET
E(A, B, D) = {Ai + Bj mod d : i, j >= 0, i + j <= D}.

PREDICTIONS (stated before the run; P2-P4 derived on paper first,
the censuses adjudicate):
 P1 (criterion, proved): THE EXPONENT REDUCTION. A degree-D curve
    holds a codeword-species stable orbit of order d iff some
    A, B with gcd(A, B, d) = 1 (= the pair's lcm-order condition:
    gcd(gcd(A,d), gcd(B,d)) = gcd(A,B,d)) has a nonzero codeword of
    (Phi_d) supported inside E(A, B, D). Collection is surjective --
    coefficients are free per monomial, one monomial per exponent
    class suffices -- and joint unit scaling (A, B) -> (uA, uB)
    plus the x<->y swap preserve everything (T -> T^u permutes the
    primitive roots), so the census runs over scaling classes.
    Verified end-to-end: every realization below is rebuilt as an
    actual curve over F_p vanishing on an actual orbit of an actual
    pair of lcm-order d; plus an exhaustive line-level brute force
    (all curves x all pairs) at (d=3, p=7) and (d=9, p=19).
 P2 (rule; reduction proved, c-values censused): THE PRIME ROW.
    For d = q an odd prime, (Phi_q) has dimension 1 -- every nonzero
    codeword is a scalar multiple of the full q-gon 1 + T + ... +
    T^{q-1}, support ALL of Z/q -- so degree D reaches q iff the
    triangle COVERS: E(A, B, D) = Z/q, WLOG A = 1 by scaling (A = 0
    degenerates to the B = 0 interval). D_min(q) = c(q), THE
    TRIANGLE COVER NUMBER -- a modular two-denomination postage
    stamp problem. Hand values: c(3) = 1, c(5) = 2 (the pentagon:
    six monomials cover Z/5), c(7) = 3, c(11) = 4, c(13) = 5.
    THE PRIME-ROW BRACKET (rule, proved both sides): the count
    floor (D+1)(D+2)/2 >= q lower-bounds, and the construction
    B = ceil(sqrt q), D = 2B - 1 -- whose intervals [jB, jB + D-j]
    stay contiguous through j = D - B + 1 and cover the prefix
    [0, B(B+1) - 1] >= [0, q-1] before wraparound is even used --
    upper-bounds: c(q) = Theta(sqrt q), between ~sqrt(2q) - 3/2
    and 2*ceil(sqrt q) - 1. A first hand-guess "c = floor or
    floor + 1" was REFUTED by the run (the excess grows: +3 at
    q = 53, +4 at q = 149): the covering obstruction beyond
    counting strengthens with q, and c is not even monotone in q
    (c(107) = 16 < 17 = c(103)). Also c(q) <= q - 2 every odd q
    (B = 2 chains the intervals [2j, j + q - 2] into [0, q-1]),
    so the tax below is strict at every prime.
 P3 (rule, proved field-free): THE PRIME-POWER LAW. For d = q^k,
    q odd, k >= 2: D_min(q^k) = q - 1. Mechanisms: (a) the basis
    {T^j Phi_{q^k}, j < q^{k-1}} has disjoint supports = full cosets
    of the order-q subgroup H, so EVERY nonzero codeword's support
    is a union of full H-cosets; (b) THE LINE PIGEONHOLE -- an
    H-coset's exponents all agree mod q^{k-1}, hence mod q, so its
    >= q triangle points sit on one mod-q line {ai + bj = c mod q},
    (a, b) != (0, 0) since gcd(A, B, d) = 1, and such a line meets
    the triangle in at most D + 1 points when D <= q - 2 (both
    coefficients nonzero: j is determined by i with at most one
    representative in [0, D - i]; one zero: a single row or column).
    So D >= q - 1; (c) A = q^{k-1}, B = 1 realizes it.
 P4 (rule -- mechanisms proved on the stated scope, the gap species
    censused at its smallest instance): THE COMPOSITE LAW. For d odd
    composite, not a prime power, q = q_min(d): D_min(d) = q - 1.
    Upper: the q-gon (T^d-1)/(T^{d/q}-1), A = d/q, B = 1. Lower, at
    D <= q - 2, via THE SLICE FORCING: split d = Q*m, Q the q-part;
    evaluating at zeta*theta (zeta prim Q-th, theta prim m-th) makes
    each x-vector (over x in Z/Q, theta fixed) a (Phi_Q)-codeword.
    If all vanish, every x-slice of c lies in (Phi_m); a slice's
    support is a mod-q line fiber, <= D + 1 <= q - 1 < q_min(m)
    points, below the menu law's minimum weight: all slices zero.
    If some survive: for Q = q^k, k >= 2, the x-support contains a
    full H-coset of Z/Q, exponents agree mod q^{k-1}: the line
    pigeonhole kills directly. For Q = q (squarefree at q),
    dim (Phi_q) = 1 forces the slices PAIRWISE CONGRUENT mod
    (Phi_m); when (D+1) + smallest-slice < q_min(m) -- guaranteed
    whenever 3(q-1)/2 < q_min(m), so always for q in {3, 5, 7} --
    all slices are EQUAL, c = 1_q (x) gamma, the support a union of
    full q-gons of spacing d/q, and the line pigeonhole (any prime
    r | d/q, r > D) kills again. GAP: pairs of close primes evade
    the forcing inequality -- TWO FAT SLICES carrying a full
    weight-q_min(m) difference, first conceivable at d = 11*13 =
    143; its two smallest instances, 143 and 13*17 = 221, censused
    exhaustively here. Non-prime realizability below q - 1
    anywhere = the law refuted.
 P5 (rule, from P2-P4): THE COMPOSITE TAX. At equal least prime,
    prime orders are strictly cheaper in degree: c(q) <= q - 2 <
    q - 1 for every odd q, with the gap widening (c tracks the
    sqrt-scale count floor, composites pay their full least prime
    linearly). The degree-D menu of odd reachable orders:
    {primes q : c(q) <= D} + {composites : q_min <= D + 1}; even
    orders all enter at D = 1 (the antipodal word 1 + T^{d/2},
    A = d/2, B = 1 -- x = -1 in curve clothing). The conics row
    must reproduce P82: 5, 9, 15 in; 25 out. Degree reads
    arithmetic the monomial count cannot: the menu law's gate is
    q_min(d) <= M for every d, the degree gate splits prime from
    composite at the same least prime.
 P6 (housekeeping): field-freeness. Every mechanism above is
    field-free given mu_d in F_p (p = 1 mod d); re-running three
    battery entries at a second prime must reproduce every verdict.

RESULTS (the run below prints the record; all confirmed):
  P1 brute force exhaustive at (d=3, p=7, D=1): codeword-species
     stable (line, pair) events = exactly {scalar multiples of
     1 + x + y} x {(2,4), (4,2)} = 12, matching the kernel census
     (one scaling class realizable, two classes not); at (d=9,
     p=19, D=1): 6,858 lines x 72 pairs, ZERO codeword-species
     events (group species occur, as they must), matching the
     exclusion. Every realization in P3/P4 batteries verified
     end-to-end on F_p (curve built from the kernel vector,
     vanishes on the full unit orbit of a pair of lcm-order d).
  P2 c(q) censused for the 34 odd primes q <= 149 (exhaustive in
     B at each D; A = 1 WLOG proved): c = 1, 2, 3, 4, 5, 6, 6, 7,
     8, 8, 9, 10, 10, 10, 12, 12, 12, 14, 13, 14, 14, 14, 16, 16,
     16, 17, 16, 17, 17, 18, 18, 20, 19, 20; hand values
     confirmed; c(13) = 5 > 4 = count floor; the bracket holds at
     every q (floor <= c <= 2*ceil(sqrt q) - 1, the explicit
     (B, D) construction verified per q); the floor+1 hand-guess
     refuted as stated; c(q) <= q - 2 with equality only at
     q = 3; kernel census == covering census at q = 5, 7, 11,
     13 (both directions, both sides of the threshold).
  P3 prime powers 9, 25, 27, 49, 81, 121: exclusion at D = q - 2
     exhaustive over all scaling classes (e.g. 121: 67 classes at
     D = 9, p = 727), realization at D = q - 1 with end-to-end
     witness: D_min = 2, 4, 2, 6, 2, 10. P82-P7's conic bound
     sharpened: 25-torsion enters at quartics exactly.
  P4 composites 15, 21, 33, 35, 45, 55, 63, 75, 77, 99, 105, 143,
     221: exclusion at D = q_min - 2 exhaustive over all scaling
     classes (the two-fat-slice species' two smallest instances
     both empty: 143 at 86 classes, D = 9, p = 859; 221 at 128
     classes, D = 11, p = 443), realization at q_min - 1: D_min =
     q_min - 1 everywhere; no sub-law realization anywhere swept.
  P5 conics row (odd d <= 121): primes {3, 5} + odd multiples of 3
     -- reproduces P82 (5, 9, 15 in; 25, 35 out); tax witnesses
     (5 vs 25/35: 2 vs 4; 7 vs 49/77: 3 vs 6; 13 vs 143: 5 vs 10).
  P6 verdicts reproduced at second primes: (15, 61), (25, 151),
     (35, 211).

Tier: P1 criterion (proved; brute-verified as stated). P2 rule
(reduction proved field-free; c-values censused exhaustively,
q <= 149). P3 rule (proved field-free both directions; censuses as
stated). P4 rule (mechanisms proved for q_min <= 7, for q_min^2 | d,
and whenever the second prime exceeds 3(q_min - 1)/2; the two-fat-
slice gap censused at its two smallest instances d = 143, 221;
taken further P89-P92 -- explore_cover_exclusion.py: rook
reduction, then the staircase closed region, then the lattice-count
closure (explore_staircase_reduction.py R12-R14): the strong
staircase lemma is a proved rule at every instance, so the law
holds at EVERY two-prime d; residual = the >=3-factor close zone
only). P5 rule (follows from
P2-P4 on their scopes). Realizability is monotone in D (E grows),
so each exclusion at D closes everything below.

Classical contacts: the modular postage stamp problem / h-bases for
Z_n (the triangle cover number is its two-denomination triangle
variant); Lang's torsion-coset theorem (the group species stays
degree-blind); BCH-flavored support constraints on cyclotomic codes;
the line pigeonhole is a one-class-per-line CRT count, cousin to the
orbit-cost law's coset-cover bound (P85).

Runs in ~4 s, tiny memory. ALL CHECKS PASSED (55).
"""

import sys, os
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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

def spf(n):
    q = 2
    while q * q <= n:
        if n % q == 0: return q
        q += 1
    return n

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

# ------------------------------------------------- the kernel machinery

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
        self.zpow = [pow(z, t, p) for t in range(d)]  # z^t table
        self.units = units_mod(d)

    def kernel(self, E):
        d, p, zp = self.d, self.p, self.zpow
        cols = len(E)
        pivots = {}            # col -> reduced row (RREF maintained)
        order = []             # pivot cols in insertion order
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
            for c in order:    # keep full RREF
                f = pivots[c][lead]
                if f:
                    pivots[c] = [(x - f * y) % p
                                 for x, y in zip(pivots[c], row)]
            pivots[lead] = row
            order.append(lead)
            if len(order) == cols:
                return None    # full column rank: no codeword on E
        free = next(c for c in range(cols) if c not in pivots)
        vec = {E[free]: 1}
        for c, prow in pivots.items():
            v = (-prow[free]) % p
            if v: vec[E[c]] = v
        # assert: really a codeword
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

def realizable(tester, D, reps=None):
    """Is (d, D) codeword-realizable? Returns a witness
    (A, B, kernel-vec) or None. Exhaustive over scaling classes."""
    d = tester.d
    if reps is None: reps = scaling_classes(d)
    for (A, B) in reps:
        vec = tester.kernel(exponent_set(A, B, D, d))
        if vec is not None:
            return (A, B, vec)
    return None

def end_to_end(tester, D, A, B, vec):
    """Rebuild a real curve from the kernel vector and verify it
    vanishes on the full unit orbit of an actual pair of lcm-order
    d over F_p."""
    d, p = tester.d, tester.p
    # one monomial per exponent class, coefficient from vec
    monos = []
    used = set()
    for i in range(D + 1):
        for j in range(D + 1 - i):
            e = (A * i + B * j) % d
            if e in vec and e not in used:
                monos.append((i, j, vec[e])); used.add(e)
    assert used == set(vec), "collection missed an exponent"
    th = tester.zpow[1]
    a, b = pow(th, A, p), pow(th, B, p)
    la = d // gcd(A, d); lb = d // gcd(B, d)
    if la * lb // gcd(la, lb) != d: return False
    for u in tester.units:
        au, bu = pow(a, u, p), pow(b, u, p)
        s = sum(c * pow(au, i, p) * pow(bu, j, p)
                for i, j, c in monos) % p
        if s != 0: return False
    return True

# =======================================================================
section("I. THE EXPONENT REDUCTION -- exhaustive line-level brute force")

def brute_line_events(d, p):
    """All lines c0 + c1 x + c2 y over F_p x all unit pairs of
    lcm-order d: count codeword-species stable events and collect
    the stable (line, pair) set."""
    els = [x for x in range(1, p)]
    byord = {}
    for x in els: byord.setdefault(mult_order(x, p), []).append(x)
    pairs = []
    for oa in byord:
        if d % oa: continue
        for ob in byord:
            if d % ob or oa * ob // gcd(oa, ob) != d: continue
            for a in byord[oa]:
                for b in byord[ob]:
                    pairs.append((a, b))
    us = units_mod(d)
    orbits = [[(pow(a, u, p), pow(b, u, p)) for u in us] for a, b in pairs]
    full = [[(pow(a, t, p), pow(b, t, p)) for t in range(d)]
            for a, b in pairs]
    events = []
    for c0 in range(p):
        for c1 in range(p):
            for c2 in range(p):
                if c0 == c1 == c2 == 0: continue
                for k, orb in enumerate(orbits):
                    if all((c0 + c1 * x + c2 * y) % p == 0
                           for x, y in orb):
                        grp = all((c0 + c1 * x + c2 * y) % p == 0
                                  for x, y in full[k])
                        if not grp:
                            events.append((c0, c1, c2, pairs[k]))
    return pairs, events

pairs3, ev3 = brute_line_events(3, 7)
expected3 = set()
for c in range(1, 7):
    for ab in [(2, 4), (4, 2)]:
        expected3.add((c, c, c, ab))
check(set(ev3) == expected3 and len(ev3) == 12,
      f"(d=3,p=7,D=1) brute: codeword-species events = "
      f"{{c(1+x+y)}} x {{(2,4),(4,2)}}, {len(ev3)} events")

t3 = CodeTester(3, 7)
got = {(A, B): t3.kernel(exponent_set(A, B, 1, 3)) is not None
       for (A, B) in scaling_classes(3)}
check(sum(got.values()) == 1 and got.get((1, 2), False),
      "(d=3) kernel census: exactly one scaling class realizable "
      "at D=1 (the 3-gon class (1,2)), matching brute")

pairs9, ev9 = brute_line_events(9, 19)
check(len(pairs9) == 72 and len(ev9) == 0,
      f"(d=9,p=19,D=1) brute: {len(pairs9)} pairs x 6,858 lines, "
      f"ZERO codeword-species events (exclusion confirmed by brute)")

# =======================================================================
section("II. THE PRIME ROW -- the triangle cover number c(q)")

def covers(q, B, D):
    cov = bytearray(q)
    n = 0
    for j in range(D + 1):
        s = (j * B) % q
        for t in range(D + 1 - j):
            e = s + t
            if e >= q: e -= q
            if not cov[e]:
                cov[e] = 1; n += 1
        if n == q: return True
    return n == q

def cover_number(q):
    D = 1
    while True:
        for B in range(q):
            if covers(q, B, D): return D
        D += 1

PRIMES = [q for q in range(3, 150) if is_prime(q) and q % 2]
ctab = {q: cover_number(q) for q in PRIMES}
print("  q : " + " ".join(f"{q}" for q in PRIMES))
print("  c : " + " ".join(f"{ctab[q]}" for q in PRIMES))

def count_floor(q):
    D = 1
    while (D + 1) * (D + 2) // 2 < q: D += 1
    return D

check(ctab[3] == 1 and ctab[5] == 2 and ctab[7] == 3
      and ctab[11] == 4 and ctab[13] == 5,
      "hand values confirmed: c(3,5,7,11,13) = 1,2,3,4,5")
check(ctab[13] == 5 > 4 == count_floor(13),
      "c(13) = 5 beats the count floor 4: covering carries an "
      "obstruction beyond counting")
excess = {q: ctab[q] - count_floor(q) for q in PRIMES}
print(f"  excess over count floor: max +{max(excess.values())} "
      f"(at q={max(excess, key=excess.get)}); the floor+1 "
      f"hand-guess is refuted -- the excess grows")

def isqrt_up(n):
    r = int(n ** 0.5)
    while r * r < n: r += 1
    return r

ok_bracket = True
for q in PRIMES:
    B = isqrt_up(q); D = 2 * B - 1
    if not (count_floor(q) <= ctab[q] <= D and covers(q, B, D)):
        ok_bracket = False
check(ok_bracket,
      "THE PRIME-ROW BRACKET at every swept q: count floor <= c(q) "
      "<= 2*ceil(sqrt q) - 1, the explicit (B = ceil sqrt q, "
      "D = 2B-1) cover verified: c(q) = Theta(sqrt q)")
check(all(ctab[q] <= q - 2 for q in PRIMES)
      and [q for q in PRIMES if ctab[q] == q - 2] == [3],
      "c(q) <= q - 2 every odd prime; equality only at q = 3")

# kernel census == covering census on both sides of the threshold
for q, p in [(5, 11), (7, 29), (11, 23), (13, 53)]:
    t = CodeTester(q, p)
    reps = scaling_classes(q)
    at = realizable(t, ctab[q], reps) is not None
    below = realizable(t, ctab[q] - 1, reps) is not None
    check(at and not below,
          f"(q={q},p={p}) kernel census == covering: realizable at "
          f"D={ctab[q]}, not at D={ctab[q]-1}")

# =======================================================================
section("III. THE PRIME-POWER LAW -- D_min(q^k) = q - 1, k >= 2")

PP = [(9, 19), (25, 101), (27, 109), (49, 197), (81, 163), (121, 727)]
for d, p in PP:
    q = spf(d)
    t = CodeTester(d, p)
    reps = scaling_classes(d)
    w = realizable(t, q - 2, reps)
    check(w is None,
          f"(d={d},p={p}) exclusion at D={q-2}: no codeword on any "
          f"of {len(reps)} scaling classes (monotone: closes D<{q-1})")
    w = realizable(t, q - 1, reps)
    check(w is not None and end_to_end(t, q - 1, *w),
          f"(d={d}) realization at D={q-1} = q-1, end-to-end witness "
          f"on F_{p}: D_min({d}) = {q-1}")

# =======================================================================
section("IV. THE COMPOSITE LAW -- D_min(d) = q_min(d) - 1")

COMP = [(15, 31), (21, 43), (33, 67), (35, 71), (45, 181), (55, 331),
        (63, 127), (75, 151), (77, 463), (99, 199), (105, 211),
        (143, 859)]
for d, p in COMP:
    q = spf(d)
    t = CodeTester(d, p)
    reps = scaling_classes(d)
    w = realizable(t, q - 2, reps)
    check(w is None,
          f"(d={d},p={p}) exclusion at D={q-2}: no codeword on any "
          f"of {len(reps)} scaling classes")
    w = realizable(t, q - 1, reps)
    check(w is not None and end_to_end(t, q - 1, *w),
          f"(d={d}) realization at D={q-1} = q_min-1, end-to-end "
          f"witness on F_{p}: D_min({d}) = {q-1}")

# the gap species' second instance, d = 13*17 = 221 (q_min = 13,
# second prime 17 <= 18 = 3(q_min-1)/2): exclusion sweep + canonical
# realization (A = d/q = 17, B = 1)
t221 = CodeTester(221, 443)
reps221 = scaling_classes(221)
check(realizable(t221, 11, reps221) is None,
      f"(d=221,p=443) exclusion at D=11: no codeword on any of "
      f"{len(reps221)} scaling classes -- the two-fat-slice species' "
      f"second instance, empty")
vec221 = t221.kernel(exponent_set(17, 1, 12, 221))
check(vec221 is not None and end_to_end(t221, 12, 17, 1, vec221),
      "(d=221) realization at D=12 = q_min-1 (13-gon, A=17, B=1), "
      "end-to-end witness on F_443: D_min(221) = 12")

# =======================================================================
section("V. THE COMPOSITE TAX + the degree menu")

def law(d):
    if d % 2 == 0: return 1
    if d == 1: return 1
    if is_prime(d): return ctab[d]
    return spf(d) - 1

conics = sorted(d for d in range(3, 122, 2) if law(d) <= 2)
check(set(conics) == {3, 5} | {d for d in range(9, 122, 2) if d % 3 == 0},
      f"conics row (odd d <= 121): {{3, 5}} + odd multiples of 3 "
      f"-- 5, 9, 15 in; 25, 35 out (P82 reproduced)")
check(law(5) == 2 < 4 == law(25) == law(35)
      and law(7) == 3 < 6 == law(49) == law(77)
      and law(13) == 5 < 10 == law(143),
      "the composite tax: 5 vs 25/35 = 2 vs 4; 7 vs 49/77 = 3 vs 6; "
      "13 vs 143 = 5 vs 10")
print("  D_min, odd d <= 121:")
print("   " + "  ".join(f"{d}:{law(d)}" for d in range(3, 122, 2)))

# even row: antipodal realization at D = 1, exclusion at D = 0
t20 = CodeTester(20, 41)
vec = t20.kernel(exponent_set(10, 1, 1, 20))
check(vec is not None and end_to_end(t20, 1, 10, 1, vec)
      and all(t20.kernel(exponent_set(A, B, 0, 20)) is None
              for (A, B) in scaling_classes(20)),
      "(d=20,p=41) even row: antipodal realization at D=1 (A=d/2), "
      "exclusion at D=0: D_min(even) = 1")

# =======================================================================
section("VI. FIELD-FREENESS -- second-prime verdicts")

for d, p in [(15, 61), (25, 151), (35, 211)]:
    q = spf(d)
    t = CodeTester(d, p)
    reps = scaling_classes(d)
    same = (realizable(t, q - 2, reps) is None
            and realizable(t, q - 1, reps) is not None)
    check(same, f"(d={d}) verdicts reproduced at second prime p={p}")

print()
print(f"ALL CHECKS PASSED ({CHECKS})")
