"""
NUMBERS WITHOUT THE INTEGER -- what replaces order.

Residue-tuple-first arithmetic: commit to never reconstructing the
integer value (never pay the reconstruction price). Over Z, the
order relation <= organizes everything -- induction, descent, Euclid,
comparison. An earlier result showed size is the deleted archimedean
place; the live
question: what REPLACES order as the organizing
relation, and what plays well-founded descent when size is gone?
The arena is the limit object Pi_p F_p (explore_limit_object.py).

Four candidate relations are tested here, each through a
relation-shaped form of an existing channel-conjunctive criterion: a relation R on (Z/N)^m is
CHANNEL-CONJUNCTIVE if R = AND_p R_p with each R_p reading only channel
p. The minimal candidate is canonical: R_p = the channel-p projection
of R, and R is conjunctive iff R equals the conjunction of its own
projections. A second, independent axis: the CONSUMPTION PARTITION --
per channel, the coarsest partition of F_p through which R factors
(swap test: r ~ r' iff swapping them never flips R) -- how many
per-channel bits a relation consumes.

Survey anchors (standard material, named so nothing here poses as new):
Green's relations / commutative Clifford monoids (Clifford 1941; the
ring's multiplicative monoid supplies the ground structure here), the full linear monoid M_n(F_q)
(Green's J-classes = rank, classical -- the classical rank-order floor), Steinitz 1910
supernatural numbers (orders/subfields of F_p-bar; divisibility lattice),
cyclically ordered groups (Rieger 1946-48, Swierczkowski 1959 embedding
theorem), well-quasi-orders vs well-founded orders (Higman, Kruskal --
P(N) under inclusion is neither: infinite descending chains AND infinite
antichains), bounded-loop computation (Meyer-Ritchie 1967 LOOP programs:
loop bounds known in advance), Dirichlet density for p = 1 mod q^e,
Borel-Cantelli (the measure leg of explore_limit_object.py), Mertens. Ours is the tower-side
composition: which relations survive channel-first reading, at what
per-channel price, and what termination becomes.

Findings preview (full statements at the bottom):
  1. THE CONJUNCTIVE SPLIT (rule): equality and divisibility ARE
     conjunctions of their channel projections; order, cyclic
     betweenness, and the order-grading are NOT. The failures differ
     in kind: order/betweenness fail MAXIMALLY (every channel
     projection saturates -- the conjunction of projections is the
     full relation, channels see nothing), the grading fails
     PROPERLY (projections are proper -- channels see something,
     the glue is cross-channel). Cyclifying buys nothing:
     btw(0,a,b) <=> a < b by definition, so the ternary cyclic
     relation carries the whole size wall.
  2. THE CONSUMPTION AXIS (rule): the swap partition is {0 | rest}
     for divisibility (1 bit: the valuation -- the tropical shadow),
     the order-classes for the grading (it conflates 0 with 1:
     support-blind, so the two surviving reads are independent), and
     DISCRETE for order and betweenness at every channel (no
     compression: every residue distinction matters). Equality is
     discrete too but conjunctive -- the two axes are orthogonal.
  3. THE CANDIDATES COLLAPSE (rule + classical): divisibility is
     support reverse-inclusion and Green's <=_J is support
     inclusion -- the SAME lattice (the idempotent lattice = the
     tropical shadow) read in opposite directions; two of the four
     candidates are ONE relation (Clifford). Noncommutative shadow: at M_2(F_2),
     J-order = rank order (full linear monoid; the rank-order floor).
     Per-channel cyclic structure is real but ADDITIVE-only: Z/n
     carries exactly phi(n) translation-invariant cyclic orders
     (exhaustive n = 5, 7; the ring's 1 picks one), and unit
     multiplication permutes them transitively -- no multiplication-
     stable cyclic order exists. The ring-level cycle is the diagonal
     flow on the torus; its time-order is what no channel sees.
  4. THE GRADING IS THE STEINITZ HALF (rule + classical): the
     powering period = lcm of per-channel orders (exhaustive Z/210)
     is profile-local -- a function of coarse per-channel invariants,
     though not conjunctive. In the limit the grade lattice completes
     to Steinitz's supernatural divisibility lattice exactly as the
     idempotents complete to P(Primes). But the grading does NOT
     separate Z: fixed integers climb to the TOP of the lattice too
     (verified n = 2, 3: the lcm of ord_p(n) accumulates prime
     powers); only support separates Z, and almost every element sits
     at the top grade (Dirichlet + Borel-Cantelli) while EVERY
     support stratum is null -- location, not magnitude, is the
     organizing data of the bulk.
  5. NOTHING PLAYS UNBOUNDED INDUCTION (rule): at a rung, descent is
     RUNG-BOUNDED -- support chains have length <= k+1 (attained),
     the lambda-chain has height 4 at RAD -- depth is a constant of
     the RING, not of the element (recursion compiles to fixed-depth
     loops; Meyer-Ritchie flavor). Euclid's loop has no meadow
     analogue (the remainder cannot shrink: explicit 2-cycle), but
     its PURPOSE trivializes: the gcd ideal is a one-step support
     read, (x, y) = (e_{supp x OR supp y}). In the limit both
     surviving lattices lose well-foundedness (infinite descending
     chains in P(Primes) and in the supernatural lattice): descent
     joins lambda and ECC in the DIES column of explore_limit_object.py.
     The trade against
     Z: well-founded-but-unbounded vs bounded-but-not-well-founded.

Runs exhaustively at Z/30 and Z/210 + closed-form channel sweeps.
~0.5 s, ~17 MB.
"""

import sys, os, math, random
from itertools import permutations, product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import (Ring, RAD_RING, encode, decode, carmichael_lambda,
                 factorize, primes_up_to)

random.seed(48)

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

def thin_ring(k):
    ps = primes_up_to(200)[:k]
    return Ring(f"T{k}", tuple(ps), (1,) * k)

R4 = thin_ring(4)            # Z/210, channels 2,3,5,7
N4 = R4.N
ENC4 = [encode(x, R4) for x in range(N4)]
R3 = thin_ring(3)            # Z/30, channels 2,3,5
N3 = R3.N
ENC3 = [encode(x, R3) for x in range(N3)]

def ordp(r, p):
    """Multiplicative order of r in F_p^*; 0 contributes 1 (idempotent:
    the powering cycle of 0 has length 1)."""
    if r == 0:
        return 1
    t, a = 1, r
    while a != 1:
        a = a * r % p
        t += 1
    return t

def period(x, ring, enc):
    """Powering period: least T >= 1 with x^(a+T) = x^a for a >= 1.
    On a squarefree ring = lcm of per-channel unit-part orders."""
    return math.lcm(*(ordp(r, p) for r, p in zip(enc[x], ring.primes)))

# the four binary candidate relations at Z/210, as verdict functions
def rel_eq(x, y):
    return x == y

def rel_div(x, y):
    """x divides y in the monoid: exists z with y = x*z."""
    return all(s == 0 or r != 0 for r, s in zip(ENC4[x], ENC4[y]))

def rel_le(x, y):
    return x <= y            # integer representatives 0..N-1

PERIOD4 = [period(x, R4, ENC4) for x in range(N4)]
def rel_orddiv(x, y):
    return PERIOD4[y] % PERIOD4[x] == 0

# ----------------------------------------------------------------------
section("I. THE CONJUNCTIVE TEST: WHICH RELATIONS ARE CHANNEL-READS")
# ----------------------------------------------------------------------
# R is channel-conjunctive iff R = AND_p proj_p(R). The projections are
# the unique minimal conjunctive candidate (R is always contained in
# their conjunction), so equality there is THE test.
# First certify rel_div = brute-force existential divisibility:
for x in range(N3):
    for y in range(N3):
        brute = any(x * z % N3 == y for z in range(N3))
        crit = all(s == 0 or r != 0 for r, s in zip(ENC3[x], ENC3[y]))
        assert brute == crit
for _ in range(2000):
    x, y = random.randrange(N4), random.randrange(N4)
    assert rel_div(x, y) == any(x * z % N4 == y for z in range(N4))
print("  divisibility (exists z: y = xz) = per-channel (y_p = 0 or")
print("  x_p != 0): exhaustive at Z/30, 2000 samples at Z/210")

def conjunctive_report(name, rel, ring, enc):
    k, ps = len(ring.primes), ring.primes
    proj = [set() for _ in range(k)]
    pairs_true = []
    for x in range(ring.N):
        for y in range(ring.N):
            if rel(x, y):
                pairs_true.append((x, y))
                for i in range(k):
                    proj[i].add((enc[x][i], enc[y][i]))
    n_conj = 0
    for x in range(ring.N):
        ex = enc[x]
        for y in range(ring.N):
            ey = enc[y]
            if all((ex[i], ey[i]) in proj[i] for i in range(k)):
                n_conj += 1
    saturated = all(len(proj[i]) == ps[i] * ps[i] for i in range(k))
    verdict = "CONJUNCTIVE" if n_conj == len(pairs_true) else \
              ("fails MAXIMALLY (projections saturate)" if saturated
               else "fails PROPERLY (projections proper)")
    print(f"  {name:12s} |R| = {len(pairs_true):6d}  |conj of projs| = "
          f"{n_conj:6d}  -> {verdict}")
    return len(pairs_true), n_conj, saturated, proj

nR, nC, sat, _ = conjunctive_report("equality", rel_eq, R4, ENC4)
assert nR == nC == N4 and not sat
nR, nC, sat, _ = conjunctive_report("divisibility", rel_div, R4, ENC4)
# closed form: per channel (p-1)p pairs with r != 0 plus (0,0), so
# |DIV| = prod (p^2-p+1) -- the same faithful-pair count as the limit
# object's (same relation)
assert nR == nC == math.prod(p * p - p + 1 for p in R4.primes)
nR, nC, sat, _ = conjunctive_report("order <=", rel_le, R4, ENC4)
assert nR == N4 * (N4 + 1) // 2 and nC == N4 * N4 and sat
nR, nC, sat, proj_od = conjunctive_report("ord-divides", rel_orddiv, R4, ENC4)
assert nR < nC < N4 * N4 and not sat
# the grading's cross-channel glue, exhibited: (x_7, y_7) = (3, 1) is in
# NO true pair -- ord_7(3) = 6 forces 6 | period(x), but y_7 = 1 leaves
# period(y) | lcm(1, 2, 4) = 4 and 6 does not divide 4. The channel
# verdict needs the OTHER channels' available orders.
assert ordp(3, 7) == 6 and (3, 1) not in proj_od[3]
print("  grading witness: residue pair (3,1) at channel 7 appears in NO")
print("  true pair -- whether ord_7(x_7) = 6 is coverable depends on the")
print("  other channels' orders (max lcm 4 here): cross-channel glue")

# the ternary candidate: cyclic betweenness btw(a,b,c) on distinct
# triples = "from a, going +1, b comes before c".
def btw(a, b, c, n):
    return (b - a) % n < (c - a) % n

# definition-check (not a discovery): anchoring at 0 recovers <, and
# the relation is translation-invariant -- so cyclic order and linear
# order are interdefinable on the ring; the wall transfers verbatim.
for a in range(1, N4):
    for b in range(1, N4):
        if a != b:
            assert btw(0, a, b, N4) == (a < b)
for _ in range(3000):
    a, b, c, t = (random.randrange(N4) for _ in range(4))
    if len({a, b, c}) == 3:
        assert btw(a, b, c, N4) == btw((a + t) % N4, (b + t) % N4,
                                       (c + t) % N4, N4)
print("  betweenness: btw(0,a,b) <=> a < b (exhaustive Z/210) and")
print("  translation-invariant (3000 samples) -- interdefinable with <=")
k3, ps3 = 3, R3.primes
projb = [set() for _ in range(k3)]
n_true = 0
for a in range(N3):
    for b in range(N3):
        for c in range(N3):
            if len({a, b, c}) == 3 and btw(a, b, c, N3):
                n_true += 1
                for i in range(k3):
                    projb[i].add((ENC3[a][i], ENC3[b][i], ENC3[c][i]))
assert all(len(projb[i]) == ps3[i] ** 3 for i in range(k3))
n_dist = N3 * (N3 - 1) * (N3 - 2)
assert n_true == n_dist // 2
print(f"  betweenness at Z/30: every channel projection saturates")
print(f"  (all p^3 residue triples appear among the {n_true} true triples")
print(f"  of {n_dist} distinct): conjunction of projections = EVERYTHING --")
print(f"  the maximal failure mode, the size wall in ternary clothes")

# ----------------------------------------------------------------------
section("II. THE CONSUMPTION PARTITION: BITS PER CHANNEL")
# ----------------------------------------------------------------------
# Per channel and argument slot, the coarsest partition of F_p through
# which R factors: r ~ r' iff swapping them (all contexts fixed) never
# flips the verdict. Computed exhaustively at Z/30.
def swap_partition(rel_n3, slot, chan, arity=2):
    p = ps3[chan]
    # contexts grouped by the residue at (slot, chan):
    by_res = {r: [] for r in range(p)}
    for t in product(range(N3), repeat=arity):
        by_res[ENC3[t[slot]][chan]].append(t)
    def shift(t, r_new):
        # replace slot's channel-chan residue by r_new via CRT
        old = list(ENC3[t[slot]])
        old[chan] = r_new
        s = list(t)
        s[slot] = decode(tuple(old), R3)
        return tuple(s)
    part = []
    for r in range(p):
        placed = False
        for cls in part:
            r0 = cls[0]
            ok = all(rel_n3(*t) == rel_n3(*shift(t, r0))
                     for t in by_res[r])
            if ok:
                cls.append(r)
                placed = True
                break
        if not placed:
            part.append([r])
    return [sorted(c) for c in part]

def rel3_div(x, y):
    return all(s == 0 or r != 0 for r, s in zip(ENC3[x], ENC3[y]))
def rel3_le(x, y):
    return x <= y
PERIOD3 = [period(x, R3, ENC3) for x in range(N3)]
def rel3_orddiv(x, y):
    return PERIOD3[y] % PERIOD3[x] == 0
def rel3_eq(x, y):
    return x == y

print("  coarsest factoring partition per channel (Z/30, slot 0 = x):")
for name, rel in [("equality", rel3_eq), ("divisibility", rel3_div),
                  ("order <=", rel3_le), ("ord-divides", rel3_orddiv)]:
    parts = [swap_partition(rel, 0, ch) for ch in range(k3)]
    desc = "; ".join(f"p={ps3[ch]}: {parts[ch]}" for ch in range(k3))
    print(f"    {name:12s} {desc}")
    if name == "divisibility":
        assert all(sorted(map(sorted, parts[ch])) ==
                   sorted(map(sorted, [[0], list(range(1, ps3[ch]))]))
                   for ch in range(k3))
    if name in ("equality", "order <="):
        assert all(len(parts[ch]) == ps3[ch] for ch in range(k3))
    if name == "ord-divides":
        # order classes, with 0 conflated into the order-1 class {0,1}
        for ch in range(k3):
            cls_of = {}
            for r in range(ps3[ch]):
                cls_of.setdefault(ordp(r, ps3[ch]), []).append(r)
            assert sorted(map(sorted, parts[ch])) == \
                   sorted(map(sorted, cls_of.values()))
print("  divisibility reads 1 bit per channel ({0 | rest} = the")
print("  valuation = the tropical shadow); the grading reads the")
print("  ORDER CLASS and conflates 0 with 1 (support-blind: the two")
print("  surviving reads are independent); order needs the DISCRETE")
print("  partition at every channel -- no per-channel compression at all")
# betweenness: the plain carrier relation (b-a) mod n < (c-a) mod n
# (no distinctness clause, so discreteness cannot come from an equality
# side-condition), every channel, every slot:
for slot in range(3):
    for ch in range(k3):
        partb = swap_partition(lambda a, b, c: btw(a, b, c, N3),
                               slot, ch, arity=3)
        assert len(partb) == ps3[ch]
print("  betweenness: discrete at EVERY channel, every slot (3 x 3,")
print("  plain carrier relation -- no distinctness side-condition)")
# ord-divides at Z/210 channel 7, slot 0: order classes again (the
# divisor lattice of p-1 = 6), confirming the Z/30 read at a 4-channel
# rung. x runs over multiples of 7 (= all 30 contexts for the other
# channels), the channel-7 residue is then added via d7 = (0,0,0,1):
d7 = decode((0, 0, 0, 1), R4)
for r_a in range(7):
    for r_b in range(7):
        same = all(
            rel_orddiv((x + r_a * d7) % N4, y)
            == rel_orddiv((x + r_b * d7) % N4, y)
            for x in range(0, N4, 7) for y in range(N4))
        assert same == (ordp(r_a, 7) == ordp(r_b, 7))
print("  Z/210 channel 7 confirms: x-slot residues are interchangeable")
print("  exactly within equal multiplicative order (all 30 x-contexts,")
print("  all 210 y; both directions of the biconditional)")

# ----------------------------------------------------------------------
section("III. THE CANDIDATES COLLAPSE: ONE LATTICE, ADDITIVE CYCLES")
# ----------------------------------------------------------------------
# (a) Green's <=_J on the multiplicative monoid = divisibility =
# support reverse-inclusion. Commutative monoid: x <=_J y iff x in yR.
for x in range(N3):
    for y in range(N3):
        green = any(y * z % N3 == x for z in range(N3))
        supp_x = {p for r, p in zip(ENC3[x], ps3) if r != 0}
        supp_y = {p for r, p in zip(ENC3[y], ps3) if r != 0}
        assert green == (supp_x <= supp_y)
print("  Green's x <=_J y <=> supp(x) inside supp(y) (exhaustive Z/30);")
print("  with finding 1: divisibility, Green's order, the idempotent")
print("  lattice, and the tropical shadow are ONE relation")
# constructive half at Z/210: supp x in supp y => z = y'.x works
for x in range(N4):
    for y in range(N4):
        if all(s != 0 or r == 0 for r, s in zip(ENC4[x], ENC4[y])):
            yi = decode(tuple(pow(s, p - 2, p) if s else 0
                              for s, p in zip(ENC4[y], R4.primes)), R4)
            assert y * (yi * x) % N4 == x
print("  meadow witness z = y'x verified for ALL comparable pairs at")
print("  Z/210 (the pseudo-inverse IS the division certificate)")
# (b) noncommutative shadow at M_2(F_2): J-order = rank order.
M = [(a, b, c, d) for a in range(2) for b in range(2)
     for c in range(2) for d in range(2)]
def mmul(X, Y):
    a, b, c, d = X
    e, f, g, h = Y
    return ((a * e + b * g) % 2, (a * f + b * h) % 2,
            (c * e + d * g) % 2, (c * f + d * h) % 2)
def rank2(X):
    a, b, c, d = X
    if (a, b, c, d) == (0, 0, 0, 0):
        return 0
    return 2 if (a * d - b * c) % 2 else 1
for X in M:
    for Y in M:
        below = any(mmul(mmul(A, Y), B) == X for A in M for B in M)
        assert below == (rank2(X) <= rank2(Y))
print("  M_2(F_2): X <=_J Y <=> rank X <= rank Y (exhaustive, 256 pairs;")
print("  classical full-linear-monoid fact) -- the rank-order floor refines the")
print("  support order into a rank order, channel by channel")
# (c) cyclic structure is additive-only. Translation-invariant cyclic
# arrangements of Z/n: exactly phi(n), the arithmetic cycles
# (0, t, 2t, ...) for units t. Exhaustive over all (n-1)! cyclic
# arrangements at n = 5, 7.
for n in (5, 7):
    invariant = []
    for tail in permutations(range(1, n)):
        arr = (0,) + tail                     # cycle as sequence
        pos = {v: i for i, v in enumerate(arr)}
        # +1 must act as a rotation of the cycle:
        d = (pos[1] - pos[0]) % n
        if all((pos[(v + 1) % n] - pos[v]) % n == d for v in range(n)):
            invariant.append(arr)
    units = [t for t in range(1, n) if math.gcd(t, n) == 1]
    assert len(invariant) == len(units)
    expected = {tuple(t * j % n for j in range(n)) for t in units}
    assert set(invariant) == expected
    print(f"  Z/{n}: exactly phi({n}) = {len(units)} translation-invariant "
          f"cyclic orders -- the arithmetic cycles (0, t, 2t, ...)")
# multiplication by a unit u maps the t-cycle to the ut-cycle:
n = 30
units30 = [t for t in range(1, n) if math.gcd(t, n) == 1]
cycles = {t: tuple(t * j % n for j in range(n)) for t in units30}
assert len(set(cycles.values())) == len(units30)
for u in units30:
    for t in units30:
        img = tuple(u * v % n for v in cycles[t])
        # img is the (ut)-cycle, up to rotation (it starts at 0 already)
        assert img == cycles[u * t % n]
print("  Z/30: unit multiplication permutes the 8 invariant cyclic")
print("  orders transitively (x u maps the t-cycle to the ut-cycle):")
print("  no multiplication-stable cyclic order exists; the ring's 1")
print("  picks one canonically, but it is ADDITIVE structure only")

# ----------------------------------------------------------------------
section("IV. THE GRADING: STEINITZ COMPLETION AND THE GENERIC TOP")
# ----------------------------------------------------------------------
# (a) period = lcm of per-channel orders; brute cycle length agrees.
for x in range(N4):
    T = 1
    a = x * x % N4
    while a != x:
        a = a * x % N4
        T += 1
    assert T == PERIOD4[x]
assert max(PERIOD4) == carmichael_lambda(N4) == 12
print("  powering period (brute cycle length) = lcm of per-channel")
print("  orders, exhaustive at Z/210; max = lambda = 12")
# (b) profile-locality: the verdict is a function of the per-channel
# order tuples alone (exhaustive consistency check at Z/210).
seen = {}
for x in range(N4):
    for y in range(N4):
        key = (tuple(ordp(r, p) for r, p in zip(ENC4[x], R4.primes)),
               tuple(ordp(s, p) for s, p in zip(ENC4[y], R4.primes)))
        v = rel_orddiv(x, y)
        assert seen.setdefault(key, v) == v
print("  ord-divides is PROFILE-LOCAL: a function of the per-channel")
print("  order tuples alone (exhaustive at Z/210) -- coarse per-channel")
print("  summaries, cross-channel glue: between the conjunctive class")
print("  and the wall")
# (c) in the limit the grade of an element is a SUPERNATURAL number
# (formal lcm of per-channel orders; Steinitz). Finite-rung shadow of
# the generic top: P[q^e | period] = 1 - prod_p (1 - c_p/p) climbs to 1.
# c_p = #{r in F_p : q^e | ord(r)} = (p-1)(1 - q^(e-1-v)) for
# v = v_q(p-1) >= e, else 0 (cyclic group count; cross-checked brute).
def count_ord_div(p, q, e):
    m, v = p - 1, 0
    t = p - 1
    while t % q == 0:
        t //= q
        v += 1
    return m - m // q ** (v - e + 1) if v >= e else 0
for p in primes_up_to(50):
    for q, e in ((2, 1), (2, 2), (3, 1), (3, 2), (5, 1)):
        brute = sum(1 for r in range(p) if ordp(r, p) % q ** e == 0)
        assert brute == count_ord_div(p, q, e)
print("  count formula = brute order census at every p < 50")
print("  P[q^e divides period of a Haar-random element], rungs k:")
qes = [(3, 1), (2, 2), (3, 2), (5, 1)]
ps_many = primes_up_to(2000)
print("       k " + "".join(f"  q^e={q ** e:2d} " for q, e in qes))
prev = None
for k in (5, 10, 20, 40, 100, 300):
    row = []
    for q, e in qes:
        miss = 1.0
        for p in ps_many[:k]:
            miss *= 1 - count_ord_div(p, q, e) / p
        row.append(1 - miss)
    print(f"    {k:4d} " + "".join(f"  {v:.4f} " for v in row))
    if prev is not None:
        assert all(b >= a - 1e-12 for a, b in zip(prev, row))
    prev = row
assert all(v > 0.99 for v in prev[:2])
print("  monotone to 1 (Dirichlet supplies channels with q^e | p-1,")
print("  Borel-Cantelli does the rest): almost every element has period")
print("  divisible by EVERY prime power -- the TOP supernatural number.")
# (d) the grading does not separate Z: fixed integers also climb to
# the top (n = 2, 3: the lcm of ord_p(n) accumulates prime powers).
LIMP = 10000
plist = primes_up_to(LIMP)
for base in (2, 3):
    L = 1
    for p in plist:
        if base % p == 0:
            continue
        t = p - 1
        for q in factorize(p - 1):
            while t % q == 0 and pow(base, t // q, p) == 1:
                t //= q
        L = math.lcm(L, t)
    for qe in (4, 8, 16, 32, 3, 9, 27, 5, 25, 7, 11, 13):
        assert L % qe == 0
    print(f"  n = {base}: lcm of ord_p({base}) over p <= {LIMP} is divisible by")
    print(f"    every prime power up to 32 -- integers sit at the top of")
    print(f"    the Steinitz lattice too; the grading cannot see Z")
# (e) every support stratum is null: the largest stratum (full support)
# has measure prod max(1-1/p, 1/p) -> 0 (Mertens), so the bulk fans
# into continuum-many null worlds, organized by LOCATION alone.
m = 1.0
for i, p in enumerate(primes_up_to(105000)[:10000], 1):
    m *= max(1 - 1 / p, 1 / p)
    if i in (100, 1000, 10000):
        print(f"  largest support-stratum measure at k = {i:5d}: {m:.6f}")
assert m < 0.05
print("  -> every stratum null; the support map organizes the bulk into")
print("  continuum-many measure-zero worlds (finite rungs: the 2^k")
print("  sub-ring worlds of the limit object (explore_limit_object.py), sizes prod(p-1) on supp)")

# ----------------------------------------------------------------------
section("V. DESCENT: WHAT TERMINATES RECURSION WITHOUT SIZE")
# ----------------------------------------------------------------------
# (a) support descent is RUNG-BOUNDED: strict chains have length k+1,
# attained; depth is a ring constant, not an element property.
chain = []
for j in range(8):
    t = tuple(1 if i < 7 - j else 0 for i in range(7))
    chain.append(decode(t, RAD_RING))
for a, b in zip(chain, chain[1:]):
    sa = {p for r, p in zip(encode(a, RAD_RING), RAD_RING.primes) if r}
    sb = {p for r, p in zip(encode(b, RAD_RING), RAD_RING.primes) if r}
    assert sb < sa
assert len(chain) == 8
print("  RAD: a strict support chain of length k+1 = 8 (attained bound;")
print("  any strict chain in the k-channel Boolean lattice has <= k+1")
print("  entries) -- support-descent recursion halts in <= k steps for")
print("  EVERY input: depth is a RUNG constant (loops with bounds known")
print("  in advance -- the Meyer-Ritchie shape, not while-loops)")
# (b) the lambda-chain bounds exponent-level descent: height 4.
lam_chain = [510510]
while lam_chain[-1] > 1:
    lam_chain.append(carmichael_lambda(lam_chain[-1]))
assert lam_chain == [510510, 240, 4, 2, 1]
print(f"  lambda-chain at RAD: {' -> '.join(map(str, lam_chain[1:]))}")
print("  (height 4): the other descent, also a ring constant")
# (c) Euclid: the gcd ideal is a ONE-STEP support read.
for x in range(N3):
    for y in range(N3):
        ideal = {(a * x + b * y) % N3 for a in range(N3) for b in range(N3)}
        outside = math.prod(p for r, s, p in zip(ENC3[x], ENC3[y], ps3)
                            if r == 0 and s == 0)
        e_union = decode(tuple(1 if (r or s) else 0
                               for r, s in zip(ENC3[x], ENC3[y])), R3)
        assert ideal == set(range(0, N3, outside))
        assert e_union in ideal and e_union * e_union % N3 == e_union
print("  (x, y) = (e_{supp x OR supp y}) -- exhaustive at Z/30, all 900")
print("  PAIRS (the 8 ideals of Z/30, each hit many times): gcd needs")
print("  ZERO descent steps, just the support union")
for x in range(N4):
    for y in range(N4):
        g = math.gcd(math.gcd(x, y), N4)
        assert g == math.prod(p for r, s, p
                              in zip(ENC4[x], ENC4[y], R4.primes)
                              if r == 0 and s == 0)
print("  gcd(x, y, N) = product of the jointly-dead channels (exhaustive")
print("  Z/210): the integer gcd ladder lands on the same one-step read")
# (d) but Euclid's LOOP does not transfer: the meadow remainder
# x mod y := x(1 - e_supp(y)) cannot shrink -- explicit 2-cycle.
def e_supp(v, ring, enc):
    return decode(tuple(1 if r else 0 for r in enc[v]), ring)
x = decode((1, 1, 0), R3)        # supp {2, 3}
y = decode((0, 1, 1), R3)        # supp {3, 5}
seq = [(x, y)]
for _ in range(6):
    x, y = seq[-1]
    r = x * (1 - e_supp(y, R3, ENC3)) % N3
    seq.append((y, r))
assert seq[2][0] != 0 and seq[4] == seq[2] and seq[5] == seq[3]
print("  Euclid's loop (x, y) -> (y, x off supp(y)) enters a 2-cycle and")
print("  never reaches y = 0 (witness at Z/30): with no size, the")
print("  remainder cannot SHRINK -- division-with-remainder died with")
print("  the deleted place; only its purpose (the gcd) survives")
# (e) in the limit, both surviving lattices lose well-foundedness:
# finite shadow -- the attained chain length k+1 is unbounded in k.
for k in range(3, 13):
    Rk = thin_ring(k)
    ch = [tuple(1 if i < k - j else 0 for i in range(k))
          for j in range(k + 1)]
    for ta, tb in zip(ch, ch[1:]):
        assert {i for i, v in enumerate(ta) if v} > \
               {i for i, v in enumerate(tb) if v}
print("  strict support chains of length k+1 verified k = 3..12:")
print("  unbounded in k -- in the limit P(Primes) has infinite")
print("  descending chains (drop one prime at a time), and the Steinitz")
print("  lattice likewise (divide one prime out at a time): neither")
print("  surviving order is well-founded. Well-founded descent joins")
print("  lambda and ECC in the DIES column of explore_limit_object.py.")

# ----------------------------------------------------------------------
section("FINDINGS (tier-labeled)")
# ----------------------------------------------------------------------
print("""
1. THE CONJUNCTIVE SPLIT (rule). A relation survives channel-first
   reading iff it equals the conjunction of its channel projections.
   Equality and divisibility do (exhaustive at Z/210; divisibility's
   conjunct is "y_p = 0 or x_p != 0"). Order, cyclic betweenness, and
   the order-grading do not -- and the failures differ in kind: order
   and betweenness fail MAXIMALLY (every projection saturates; the
   conjunction is the full relation -- channels retain nothing), the
   grading fails PROPERLY (projections proper: witness (3,1) at
   channel 7 -- whether an order is coverable depends on the OTHER
   channels). Cyclifying buys nothing: btw(0,a,b) <=> a < b and
   btw is translation-invariant, so the ternary cyclic relation is
   interdefinable with order and carries the whole size wall.

2. THE CONSUMPTION AXIS (rule). The coarsest per-channel partition
   through which a relation factors (swap test, exhaustive at Z/30;
   the grading's order-class read confirmed at Z/210): divisibility
   reads ONE BIT ({0 | rest} -- the
   valuation, i.e. the tropical shadow); the grading reads the order
   class and CONFLATES 0 with 1 (support-blind -- the two surviving
   reads are independent coordinates); order and betweenness need the
   discrete partition at every channel (no compression; the hiding
   lemma quantified relation-side). Equality is discrete too but
   conjunctive: consumption and conjunctivity are orthogonal axes.

3. THE CANDIDATES COLLAPSE (rule + classical). Two of the four
   candidates are one relation: divisibility is support reverse-inclusion
   (x | y <=> supp y inside supp x) and Green's <=_J is support
   inclusion -- the SAME lattice, the idempotent lattice = the
   tropical shadow, read in opposite directions: the
   commutative Clifford collapse (exhaustive
   Z/30; meadow witness z = y'x at Z/210). Noncommutative shadow:
   at M_2(F_2) the J-order is the RANK order (exhaustive; classical
   full-linear-monoid) -- the rank-order floor refines support to rank.
   Candidate 4 splits: Z/n carries exactly phi(n) translation-
   invariant cyclic orders, the arithmetic cycles (0, t, 2t, ...)
   (exhaustive n = 5, 7; classical contact: cyclically ordered
   groups, Rieger/Swierczkowski), the ring's 1 picks one -- but unit
   multiplication permutes them transitively (verified Z/30): cyclic
   structure is ADDITIVE-only, and the ring-level cycle's time-order
   (the diagonal flow on the torus) is exactly what no channel sees
   -- the braid of per-channel phases, the coupling-order probe's
   territory, not this chart's.

4. THE GRADING IS THE STEINITZ HALF (rule + classical). The powering
   period = lcm of per-channel orders (exhaustive Z/210) is
   PROFILE-LOCAL -- a function of coarse per-channel invariants,
   strictly between the conjunctive class and the wall. In the limit
   each element's grade is a supernatural number and the grade
   lattice completes to Steinitz's divisibility lattice, exactly as
   the idempotents complete to P(Primes) (classical contact, named).
   But the grading separates nothing that matters: almost every
   element sits at the TOP grade (P[q^e | period] -> 1, monotone,
   computed to 300 channels), and fixed integers sit at the top too
   (n = 2, 3: the lcm of ord_p(n) over p <= 10^4 already swallows
   all prime powers <= 32). Only SUPPORT separates Z from the bulk
   -- and every support stratum is Haar-null (largest stratum 0.05
   at 10^4 channels, Mertens): the bulk fans into continuum-many null
   worlds. What replaces order as the organizing relation is
   LOCATION (support: where you live) refined by TORSION (grade: how
   you turn) -- the question the limit object (explore_limit_object.py)
   leaves open (what
   structures the bulk that Z is a null anomaly in) answered: the
   support stratification, with the grading degenerate on it.

5. NOTHING PLAYS UNBOUNDED INDUCTION (rule). At a rung, descent is
   RUNG-BOUNDED: strict support chains have length exactly k+1
   (attained, k <= 12), the lambda-chain has height 4 at RAD --
   recursion depth is a constant of the RING, not a function of the
   element, so support-descent recursions are bounded loops
   (Meyer-Ritchie shape), circuits rather than while-loops. Euclid
   splits: the gcd IDEAL is a one-step support read ((x, y) =
   (e_{supp union}), exhaustive Z/30 + the gcd identity at Z/210),
   while Euclid's LOOP has no meadow analogue -- the sizeless
   remainder x(1 - e_supp(y)) enters a 2-cycle and never terminates
   (witness). In the limit, both surviving lattices have infinite
   descending chains: well-founded descent joins lambda and ECC in
   the DIES column of explore_limit_object.py. The trade against Z: Z is well-founded with
   unbounded recursion depth; the tower is bounded-depth at every
   rung with no well-foundedness in the limit. Induction is a
   finite-rung artifact; what survives is bounded descent.
""")
print("explore_organizing_relations.py: ALL CHECKS PASSED")
