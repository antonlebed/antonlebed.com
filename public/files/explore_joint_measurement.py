"""
The joint measurement: two-leaf word gates.

An open question from the idempotent-logic work: the quantifier
ladder proved relative order -- [ab = 1] -- escapes every SINGLE-LEAF
measurement, yet BOX(ab) reads it in one gate once the product is
admitted as a leaf. Chart the TWO-LEAF measurement family: gates on
words a^i b^j (i, j in Z via the meadow inverse). THE BAR: a
two-variable analogue of the single-leaf classification -- which
two-variable shadows the word family decides, blind channels named
by a LAW -- or a proved wall that no finite word family suffices.

Setting: per channel F_p the unit group is cyclic of order n = p-1;
write a = g^alpha, b = g^beta. Then ord(a^i b^j) =
n / gcd(i*alpha + j*beta, n): the word-order profile is gcd data on
the Z-linear forms of the dlog pair. Gates read it bit by bit:
gate_m(w) = [ord(w) | m].

PREDICTIONS (stated before the run):
 P1 (rule, proved): THE WORD-PROFILE THEOREM. The full word-order
    profile {ord(a^i b^j) : i, j in Z} determines and is determined
    by the dlog pair (alpha, beta) up to ONE unit of Z/n -- i.e. the
    pair (a, b) up to simultaneous conjugacy (a, b) -> (a^u, b^u),
    gcd(u, n) = 1 (one automorphism of the cyclic unit group acting
    on both leaves; single leaves are the L = 1 case, alpha up to a
    unit = ord(a)). Proof: unit-invariance of gcd gives orbit <=
    profile-class; conversely per prime power q^e || n the profile's
    capped q-valuations on the pencil i*alpha + beta pin the
    normalized pair exactly (normalize the min-valuation coordinate
    to q^v; the slice data v_q(i*alpha + beta) over i recovers the
    other coordinate mod q^e; residual normalizing freedom w = 1 mod
    q^(e-v) acts trivially), and the per-q units CRT-glue to one u.
    The proof is generic to marked pairs in ANY cyclic group
    (provenance: cyclic-group fact; the field only dresses it).
    Sharpening: the TWO PENCILS {ord(a^i b)}, {ord(a b^j)} plus the
    two single-leaf orders already generate the profile; the three
    words (ord a, ord b, ord ab) do NOT (witness in C_8).
 P2 (rule): THE NEW CONTENT IS THE RELATIVE POSITION. When a is
    primitive the profile pins b EXACTLY (classes with a primitive
    = n, one per value of dlog_a b): the word family measures the
    relative discrete log -- precisely what the single-leaf
    classification proved no single-leaf family sees. [ab = 1], the
    escape witness for that classification, is ONE gate: gate_1(ab).
 P3 (rule, proved): DECIDABILITY = CONJUGACY INVARIANCE + THE
    CRYSTALLOGRAPHIC SKELETON. By P1 a two-variable shadow is
    word-decidable on a channel iff it is constant on conjugacy
    orbits. All multiplicative-coset shadows [a^i b^j = 1] are
    decided (each IS a gate). The affine line a + b = c splits:
    c = 0 is wholly decided ([ab^-1 = -1], a multiplicative shadow
    in disguise); for c != 0 the orbit-stable unit pairs are EXACTLY
    {(a, a^-1) : a + a^-1 = c, ord(a) in {1, 2, 3, 6}} -- u = -1
    forces ab = 1, all-u stability forces all order-d elements to
    share one trace, phi(d) <= 2, and d = 4 (trace 0) lands on the
    c = 0 line: the CRYSTALLOGRAPHIC RESTRICTION, arriving uninvited.
    So the word-visible part of the additive world is the torsion of
    orders 1, 2, 3, 4, 6: c = 2 keeps (1,1), c = -2 keeps (-1,-1),
    c = 1 keeps the Phi_6 pair (present iff p = 1 mod 6 -- the
    splitting law of Q(zeta_6), a dependent shadow reappearing here
    as the line's multiplicative skeleton), c = -1 the
    Phi_3 pair (iff p = 1 mod 3), EVERY OTHER c is word-invisible.
    Blind channels for [a+b = 1]: all p >= 5 (straddling orbits
    exist); deciding channels: exactly p <= 3, where the Galois
    group (Z/(p-1))* is trivial -- the p = 3 rigidity, one level up.
 P4 (rule, proved): THE PAIRING VERDICT. gate_m(ab^-1) =
    [dlog a = dlog b mod n/gcd(m, n)]: a divisor-indexed EQUALITY
    GRADING on the units -- reflexive, symmetric, AND-transitive
    (ord(xy) | lcm(ord x, ord y)), unit-translation-invariant
    ((ax)(bx)^-1 = ab^-1 for unit x) -- the congruence filtration
    of the diagonal, i.e. the profinite metric on the index ring
    Z/n one level down (the two-orders chart's convergence-order
    distance). The bilinear candidate gcd(alpha*beta, n) IS
    well-defined (unit^2-invariant) and profile-readable, but
    FACTORS through the single-leaf orders: gcd(alpha*beta, n) =
    gcd(gcd(alpha,n)*gcd(beta,n), n) (capped valuations add).
    Verdict: every word's dlog is a LINEAR form in the leaf dlogs,
    so no word reads a bilinear form, and the candidate's gcd-type
    adds nothing beyond single leaves -- the pairing structure is
    the ultrametric, not an inner product.
 P5 (rule + witnesses): THE ALPHABET LADDER. Measurement reach is
    alphabet-graded, the word-profile theorem covering every level
    (L letters -> dlog L-tuple up to one unit):
    (a) one leaf, MIXED words in {a, 1-a} already beat the
        single-leaf polynomial family: the profile-collision x = 9
        vs 3 at p = 11 (both (ord, ord) = (5,5)) is separated by the
        word a^2(1-a) -- that wall witness was itself a word;
    (b) two leaves, four letters {a, b, 1-a, 1-b}: profile = the
        dlog 4-tuple up to one unit; newly decided: the six
        +-1-ratio affine lines (a+b in {0,1,2}, a-b in {0,1,-1}),
        each one or two gates; still blind: lines needing other
        constants -- [a + b = 3] witnessed by the Phi_6 pairs (3,3)
        vs (5,5) at p = 7, which share the FULL 4-letter profile
        (the letter coincidence (1-a)^u = 1-a^u at the order-6
        points) yet split the shadow;
    (c) the FULL MEADOW CLOSURE (NOT and inverse nesting freely) is
        COMPLETE: NOT(a^-1) * (NOT a)^-1 * a = -1 identically on
        units a != 1, so 2 = NOT(-1), and induction c = NOT(-(c-1))
        generates EVERY constant as a word in one graded leaf; then
        [x = c] = gate_1(x c^-1) pins every unit residue exactly
        (0 and 1 are the pair bits'). The meadow inverse is the
        WALL-BREAKER: every measurement wall in the hierarchy --
        including the single-leaf wall -- is a fact about
        inverse-free alphabets; total division buys omniscience.
 P6 (rule): RING LEVEL. All reads are ring polynomials assembling
    per channel (gates of CRT words); on RAD the d(240) = 20
    equality-grading rungs are distinct as relations; the deciding
    channels of the affine shadow [x + y = 1] are exactly {2, 3}.

RESULTS (the run below prints the record; all six confirmed):
  P1 profile partition = conjugacy-orbit partition: exhaustive over
     ALL pairs of C_n for n in {6,8,10,12,16,18,22,24} and over all
     unit pairs of F_p for p in {5,7,11,13,17,19,23}; two-pencil
     signature gives the same partition everywhere; the three-word
     profile fails in C_8 ((1,2) vs (1,6): same (ord a, ord b,
     ord ab), different orbits); the field dressing ord(a^i b^j) =
     (p-1)/gcd(i alpha + j beta, p-1) spot-verified 400x.
  P2 classes with a primitive = n exactly (every p in the census);
     the earlier witness (p = 7: b = 5 vs b' = 3 over a = 3, same
     single-leaf profiles) split by the one gate gate_1(ab).
  P3 stable census = the crystallographic law at every (p, c),
     p <= 100, ALL c (line c = 0 wholly stable; c != 0 matches the
     trace formula; nonempty c = 1 iff p = 1 mod 6, c = -1 iff
     p = 1 mod 3); blind witness orbits found at every 5 <= p <= 100
     on c = 1; at p = 3 every orbit is a singleton (trivial Galois)
     -- the channel decides everything.
  P4 equality grading exhaustive (7 census primes, all unit pairs,
     all divisors m | p-1); AND-transitivity exhaustive at p = 7,
     11; translation invariance is the identity (ax)(bx)^-1 = ab^-1;
     bilinear factorization gcd(ab, n) = gcd(gcd(a,n)gcd(b,n), n)
     exhaustive over all pairs, all n in the C_n list.
  P5 (a) 9 vs 3 at p = 11 separated by ord(a^2(1-a)) = 1 vs 5; the
     one-leaf two-letter word partition strictly refines the
     single-leaf (ord a, ord(1-a)) partition (first at p = 11) and
     equals the 2-tuple-up-to-unit partition (exhaustive p <= 23);
     (b) 4-letter profile partition = 4-tuple-up-to-unit partition
     (exhaustive p = 7, 11); all six +-1-ratio lines read by gates
     (exhaustive p <= 19); [a+b = 3] blind witness (3,3) vs (5,5)
     at p = 7 verified profile-equal, shadow-split;
     (c) the -1 identity exhaustive (p <= 31, all units a != 1);
     meadow closure from EVERY graded start = all of F_p
     (exhaustive p <= 31); completeness follows.
  P6 ring gates of CRT words match channel reads (300 RAD pairs x
     20 rungs); the 20 rungs distinct as RAD relations; RAD deciding
     channels for the affine shadow = {2, 3} by the P3 law.

Tier: P1, P4, P5(c) rule (proved by the arguments above; verified
exhaustively as stated). P2, P3 rule (proved per channel: the u = -1
argument + the trace/crystallographic classification; censuses
exhaustive p <= 100). P5(a), (b) rule for the swept ranges,
observation beyond. P6 rule (assembly by construction; verified).

Runs on RAD (k = 7) with exhaustive censuses. ~0.2 s, tiny memory.
ALL CHECKS PASSED (24).
"""

import sys, os, random
from math import gcd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import RAD_RING, encode, decode, multiplicative_order

random.seed(77)
R = RAD_RING
N, LAM, PRIMES = R.N, R.lam, R.primes

CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok' if cond else 'FAIL'}] {msg}")
    assert cond, msg

def section(t):
    print(); print("=" * 72); print(t); print("=" * 72)

def primitive_root(p):
    n = p - 1
    qs = [q for q in range(2, n + 1) if n % q == 0 and
          all(q % r for r in range(2, int(q ** 0.5) + 1))]
    for g in range(2, p):
        if all(pow(g, n // q, p) != 1 for q in qs):
            return g

def units_mod(n):
    return [u for u in range(1, n + 1) if gcd(u, n) == 1]

def partition_of(keys):
    """keys: dict item -> hashable class key; returns the partition
    as a frozenset of frozensets."""
    cls = {}
    for item, k in keys.items():
        cls.setdefault(k, set()).add(item)
    return frozenset(frozenset(s) for s in cls.values())

# ----------------------------------------------------------------------
section("I. THE WORD-PROFILE THEOREM (cyclic core + field dressing)")
# ----------------------------------------------------------------------

# Cyclic core: marked pairs (alpha, beta) in C_n; profile = gcd data
# on all Z-linear forms; claim: profile class = unit orbit.
N_LIST = [6, 8, 10, 12, 16, 18, 22, 24]
ok_full = ok_pencil = True
for n in N_LIST:
    G = [gcd(x, n) for x in range(n)]
    U = units_mod(n)
    sig_f, sig_p, orb = {}, {}, {}
    for al in range(n):
        for be in range(n):
            sig_f[(al, be)] = bytes(G[(i * al + j * be) % n]
                                    for i in range(n) for j in range(n))
            sig_p[(al, be)] = (G[al], G[be],
                               bytes(G[(i * al + be) % n] for i in range(n)),
                               bytes(G[(al + j * be) % n] for j in range(n)))
            orb[(al, be)] = min((u * al % n, u * be % n) for u in U)
    if partition_of(sig_f) != partition_of(orb):
        ok_full = False
    if partition_of(sig_p) != partition_of(orb):
        ok_pencil = False
check(ok_full, "profile partition = unit-orbit partition, ALL pairs of C_n, "
               f"n in {N_LIST} (the word-profile theorem, cyclic core)")
check(ok_pencil, "the two pencils + the two single orders generate the "
                 "profile (same partition, same range)")

# Three words do not suffice: C_8 witness.
n = 8
tri = lambda al, be: (gcd(al, n), gcd(be, n), gcd(al + be, n))
o8 = lambda al, be: min((u * al % n, u * be % n) for u in units_mod(n))
check(tri(1, 2) == tri(1, 6) and o8(1, 2) != o8(1, 6),
      "(ord a, ord b, ord ab) alone does NOT suffice: C_8 witness "
      "(1,2) vs (1,6) -- same three orders, different orbits")

# Field dressing: ord(a^i b^j) = (p-1)/gcd(i alpha + j beta, p-1).
P_CENSUS = [5, 7, 11, 13, 17, 19, 23]
DLOG = {}
for p in P_CENSUS:
    g = primitive_root(p)
    DLOG[p] = {pow(g, e, p): e for e in range(p - 1)}
ok = True
for _ in range(400):
    p = random.choice(P_CENSUS)
    n = p - 1
    a, b = random.randrange(1, p), random.randrange(1, p)
    i, j = random.randrange(-6, 7), random.randrange(-6, 7)
    w = pow(a, i % n, p) * pow(b, j % n, p) % p
    if multiplicative_order(w, p) != n // gcd(i * DLOG[p][a] + j * DLOG[p][b], n):
        ok = False
check(ok, "field dressing: ord(a^i b^j) = (p-1)/gcd(i alpha + j beta, p-1) "
          "(400 sampled words across the census primes)")

# Field-level partition: profile class = simultaneous-conjugacy orbit.
ok = True
CLASS_COUNTS = {}
for p in P_CENSUS:
    n = p - 1
    G = [gcd(x, n) for x in range(n)]
    dl = DLOG[p]
    U = units_mod(n)
    sig, orb = {}, {}
    for a in range(1, p):
        for b in range(1, p):
            al, be = dl[a], dl[b]
            sig[(a, b)] = bytes(G[(i * al + j * be) % n]
                                for i in range(n) for j in range(n))
            orb[(a, b)] = min((pow(a, u, p), pow(b, u, p)) for u in U)
    if partition_of(sig) != partition_of(orb):
        ok = False
    CLASS_COUNTS[p] = len(set(sig.values()))
check(ok, "unit pairs of F_p: profile class = conjugacy orbit "
          "(a,b) ~ (a^u, b^u), exhaustive p in " + str(P_CENSUS))
print("    profile classes on unit pairs:",
      {p: CLASS_COUNTS[p] for p in P_CENSUS})

# ----------------------------------------------------------------------
section("II. THE NEW CONTENT: the relative discrete log")
# ----------------------------------------------------------------------

ok = True
for p in P_CENSUS:
    n = p - 1
    dl, U = DLOG[p], units_mod(n)
    # classes among pairs with a primitive: one per exact value of
    # dlog_a b -- the relative dlog is pinned, count = n.
    reps = set()
    for a in range(1, p):
        if gcd(dl[a], n) != 1:
            continue
        for b in range(1, p):
            reps.add(min((pow(a, u, p), pow(b, u, p)) for u in U))
    if len(reps) != n:
        ok = False
check(ok, "classes with a primitive = p-1 exactly: the profile pins "
          "dlog_a b -- the relative position single leaves never see "
          "(exhaustive, census primes)")

# The single-leaf escape witness, decided by ONE gate.
p, a, b, b2 = 7, 3, 5, 3
prof = lambda x: (multiplicative_order(x, p), multiplicative_order((1 - x) % p, p))
check(prof(b) == prof(b2) and (a * b % p == 1) != (a * b2 % p == 1)
      and (a * b % p == 1) == (pow(a * b % p, 1, p) == 1),
      "the multi-variable escape ([ab = 1] blind to single leaves at "
      "p = 7) is ONE word gate: gate_1(ab)")

# ----------------------------------------------------------------------
section("III. DECIDABILITY + THE CRYSTALLOGRAPHIC SKELETON")
# ----------------------------------------------------------------------

def is_prime(m):
    return m > 1 and all(m % r for r in range(2, int(m ** 0.5) + 1))

P_BIG = [p for p in range(5, 101) if is_prime(p)]

ok_law = ok_split = True
blind_found = 0
for p in P_BIG:
    n = p - 1
    U = units_mod(n)
    inv = {a: pow(a, p - 2, p) for a in range(1, p)}
    # predicted stable unit pairs on a + b = c, c != 0:
    pred = {}
    for a in range(1, p):
        d = multiplicative_order(a, p)
        if d in (1, 2, 3, 6):
            c = (a + inv[a]) % p
            if c:
                pred.setdefault(c, set()).add((a, inv[a]))
    for c in range(1, p):
        line = [(a, (c - a) % p) for a in range(1, p) if (c - a) % p]
        stable = {(a, b) for a, b in line
                  if all((pow(a, u, p) + pow(b, u, p)) % p == c for u in U)}
        if stable != pred.get(c, set()):
            ok_law = False
    # c = 0: wholly stable (u odd: a^u + (-a)^u = 0 identically)
    if not all(all((pow(a, u, p) + pow(p - a, u, p)) % p == 0 for u in U)
               for a in range(1, p)):
        ok_law = False
    # splitting laws
    if (1 in pred) != (p % 6 == 1) or ((p - 1) in pred) != (p % 3 == 1):
        ok_split = False
    # blindness witness on c = 1: a straddling orbit
    for a in range(2, p - 1):
        b = (1 - a) % p
        if b == 0:
            continue
        for u in U:
            if (pow(a, u, p) + pow(b, u, p)) % p != 1:
                blind_found += 1
                break
        else:
            continue
        break
check(ok_law, "stable census = the crystallographic law at every (p, c), "
              "p <= 100: c = 0 wholly stable, c != 0 keeps exactly the "
              "trace-c torsion pairs of order 1, 2, 3, 6")
check(ok_split, "the splitting laws: the c = 1 (Phi_6) skeleton exists iff "
                "p = 1 mod 6, the c = -1 (Phi_3) skeleton iff p = 1 mod 3")
check(blind_found == len(P_BIG),
      f"[a + b = 1] blind at every p in 5..100 ({blind_found}/{len(P_BIG)} "
      "straddling orbits found; orbit = profile class by P1)")

# p = 3: trivial Galois group, every orbit a singleton -- decides all.
p = 3
check(all(len({(pow(a, u, p), pow(b, u, p)) for u in units_mod(p - 1)}) == 1
          for a in (1, 2) for b in (1, 2)),
      "p = 3: the Galois group (Z/2)* is trivial, every orbit a singleton "
      "-- the rigidity channel decides every shadow")

# ----------------------------------------------------------------------
section("IV. THE EQUALITY GRADING (the pairing verdict)")
# ----------------------------------------------------------------------

ok = True
for p in P_CENSUS:
    n = p - 1
    dl = DLOG[p]
    divs = [m for m in range(1, n + 1) if n % m == 0]
    inv = {a: pow(a, p - 2, p) for a in range(1, p)}
    for a in range(1, p):
        for b in range(1, p):
            w = a * inv[b] % p
            ow = multiplicative_order(w, p)
            for m in divs:
                if (m % ow == 0) != ((dl[a] - dl[b]) % (n // gcd(m, n)) == 0):
                    ok = False
check(ok, "gate_m(ab^-1) = [dlog a = dlog b mod (p-1)/gcd(m, p-1)]: the "
          "equality grading (exhaustive, census primes, all divisors)")

ok = True
for p in (7, 11):
    n = p - 1
    inv = {a: pow(a, p - 2, p) for a in range(1, p)}
    divs = [m for m in range(1, n + 1) if n % m == 0]
    for a in range(1, p):
        for b in range(1, p):
            for c in range(1, p):
                for m in divs:
                    gab = m % multiplicative_order(a * inv[b] % p, p) == 0
                    gbc = m % multiplicative_order(b * inv[c] % p, p) == 0
                    gac = m % multiplicative_order(a * inv[c] % p, p) == 0
                    if gab and gbc and not gac:
                        ok = False
check(ok, "AND-transitive at every rung (ord(xy) | lcm: exhaustive unit "
          "triples x divisors, p = 7, 11) -- with reflexivity and symmetry, "
          "a divisor-indexed ultrametric on the units; unit-translation "
          "invariance is the identity (ax)(bx)^-1 = ab^-1, x a unit")

ok = True
for n in N_LIST + [22]:
    for al in range(n):
        for be in range(n):
            if gcd(al * be % n, n) != gcd(gcd(al, n) * gcd(be, n), n):
                ok = False
check(ok, "the bilinear candidate factors: gcd(alpha*beta, n) = "
          "gcd(gcd(alpha,n)*gcd(beta,n), n) -- single-leaf data only "
          "(exhaustive, all n in the C_n list); every word's dlog is a "
          "linear form, so the pairing is the ultrametric, not an inner "
          "product")

# ----------------------------------------------------------------------
section("V. THE ALPHABET LADDER")
# ----------------------------------------------------------------------

# (a) one leaf, mixed words in {a, 1-a} beat the single-leaf family.
p = 11
x, y = 9, 3
sep = lambda t: multiplicative_order(t * t * (1 - t) % p, p)
prof11 = lambda t: (multiplicative_order(t, p),
                    multiplicative_order((1 - t) % p, p))
check(prof11(x) == prof11(y) == (5, 5) and sep(x) != sep(y),
      f"the known collision 9 vs 3 at p = 11 (both order profile (5,5)) is "
      f"separated by the WORD a^2(1-a): ord {sep(x)} vs {sep(y)} -- the "
      "earlier wall witness was itself a word")

ok_thm = True
strictly_finer_at = []
for p in P_CENSUS:
    n = p - 1
    G = [gcd(t, n) for t in range(n)]
    dl, U = DLOG[p], units_mod(n)
    sig, orb, p75 = {}, {}, {}
    for a in range(2, p):          # a != 0, 1: both letters units
        al, ga = dl[a], dl[(1 - a) % p]
        sig[a] = bytes(G[(i * al + k * ga) % n]
                       for i in range(n) for k in range(n))
        orb[a] = min((u * al % n, u * ga % n) for u in U)
        p75[a] = (G[al], G[ga])
    if partition_of(sig) != partition_of(orb):
        ok_thm = False
    if len(set(sig.values())) > len(set(p75.values())):
        strictly_finer_at.append(p)
check(ok_thm and strictly_finer_at and min(strictly_finer_at) == 11,
      "one-leaf two-letter words measure (dlog a, dlog(1-a)) up to one "
      "unit -- strictly finer than the joint order profile, first at "
      f"p = {min(strictly_finer_at) if strictly_finer_at else '?'} "
      f"(strict at p in {strictly_finer_at})")

# (b) two leaves, four letters: the L = 4 theorem.
ok = True
for p in (7, 11):
    n = p - 1
    G = [gcd(t, n) for t in range(n)]
    dl, U = DLOG[p], units_mod(n)
    grid = [(e1, e2, e3, e4) for e1 in range(n) for e2 in range(n)
            for e3 in range(n) for e4 in range(n)]
    sig, orb = {}, {}
    for a in range(2, p):
        for b in range(2, p):
            t = (dl[a], dl[(1 - a) % p], dl[b], dl[(1 - b) % p])
            sig[(a, b)] = bytes(G[(e1 * t[0] + e2 * t[1] + e3 * t[2]
                                   + e4 * t[3]) % n] for e1, e2, e3, e4 in grid)
            orb[(a, b)] = min(tuple(u * c % n for c in t) for u in U)
    if partition_of(sig) != partition_of(orb):
        ok = False
check(ok, "four-letter profile = dlog 4-tuple up to one unit "
          "(the L = 4 word-profile theorem; exhaustive p = 7, 11)")

# The six +-1-ratio lines are gate-readable on letter-unit pairs.
ok = True
for p in [q for q in range(5, 20) if is_prime(q)]:
    inv = {a: pow(a, p - 2, p) for a in range(1, p)}
    is_m1 = lambda w: w == p - 1                       # [w = -1] = gate_2 & ~gate_1
    for a in range(2, p):
        for b in range(2, p):
            na, nb = (1 - a) % p, (1 - b) % p
            reads = [((a + b) % p == 1, a * inv[nb] % p == 1),
                     ((a + b) % p == 0, is_m1(a * inv[b] % p)),
                     ((a + b) % p == 2, is_m1(na * inv[nb] % p)),
                     (a == b,           a * inv[b] % p == 1),
                     ((a - b) % p == 1, is_m1(na * inv[b] % p)),
                     ((b - a) % p == 1, is_m1(nb * inv[a] % p))]
            if any(s != r for s, r in reads):
                ok = False
check(ok, "the six +-1-ratio affine lines (a+b in {0,1,2}, a-b in "
          "{0,1,-1}) are each one or two gates on the four letters "
          "(exhaustive p <= 19)")

# [a + b = 3]: blind for the 4-letter family -- the Phi_6 witness.
p = 7
n, dl, U = 6, DLOG[7], units_mod(6)
G = [gcd(t, 6) for t in range(6)]
def sig4(a, b):
    t = (dl[a], dl[(1 - a) % p], dl[b], dl[(1 - b) % p])
    return bytes(G[(e1 * t[0] + e2 * t[1] + e3 * t[2] + e4 * t[3]) % n]
                 for e1 in range(n) for e2 in range(n)
                 for e3 in range(n) for e4 in range(n))
check(sig4(3, 3) == sig4(5, 5) and (3 + 3) % 7 != 3 and (5 + 5) % 7 == 3,
      "[a + b = 3] is blind to ALL four-letter words: (3,3) vs (5,5) at "
      "p = 7 (the Phi_6 points; (1-a)^u = 1-a^u there) share the full "
      "4-letter profile yet split the shadow")

# (c) the meadow wall-breaker.
P31 = [q for q in range(3, 32) if is_prime(q)]
ok = True
for p in P31:
    for a in range(2, p):
        na_inv = pow((1 - a) % p, p - 2, p)
        ai = pow(a, p - 2, p)
        if (1 - ai) % p * na_inv % p * a % p != p - 1:
            ok = False
check(ok, "the wall-breaker identity NOT(a^-1) * (NOT a)^-1 * a = -1 at "
          "every unit a != 1 (exhaustive p <= 31)")

ok = True
for p in P31:
    for a0 in range(2, p):
        S = {a0}
        frontier = True
        while frontier:
            new = ({(1 - x) % p for x in S}
                   | {pow(x, p - 2, p) if x else 0 for x in S}
                   | {x * y % p for x in S for y in S})
            frontier = not new <= S
            S |= new
        if S != set(range(p)):
            ok = False
check(ok, "meadow-term closure from EVERY graded start = all of F_p "
          "(exhaustive p <= 31): every constant is a word, [x = c] = "
          "gate_1(x c^-1) -- the full meadow family identifies every "
          "residue; all measurement walls are inverse-free facts")

# ----------------------------------------------------------------------
section("VI. RING LEVEL (RAD)")
# ----------------------------------------------------------------------

DIVS = [d for d in range(1, LAM + 1) if LAM % d == 0]
def ring_gate(w, m):
    return (1 - pow((1 - pow(w, m, N)) % N, LAM, N)) % N

ok_match = True
vectors = {m: [] for m in DIVS}
for _ in range(300):
    x, y = random.randrange(N), random.randrange(N)
    rx, ry = encode(x, R), encode(y, R)
    w_res = tuple(rx[i] * pow(ry[i], p - 2, p) % p if ry[i] else 0
                  for i, p in enumerate(PRIMES))
    w = decode(w_res, R)
    for m in DIVS:
        gv = encode(ring_gate(w, m), R)
        for i, p in enumerate(PRIMES):
            r = w_res[i]
            expect = 1 if (r and m % multiplicative_order(r, p) == 0) else 0
            if gv[i] != expect:
                ok_match = False
        vectors[m].append(gv)
check(ok_match, "ring gates of the CRT word x y^-1 match the per-channel "
                "equality reads (300 RAD pairs x 20 rungs)")
check(len({tuple(map(tuple, vectors[m])) for m in DIVS}) == len(DIVS),
      f"the {len(DIVS)} equality-grading rungs are distinct as relations "
      "on RAD (verdict vectors over the sample all differ)")

ok = True
for p in PRIMES:
    U = units_mod(p - 1)
    pts = [(a, (1 - a) % p) for a in range(1, p) if (1 - a) % p]
    if p <= 3:   # trivial Galois group: every orbit a singleton
        if any(len({(pow(a, u, p), pow(b, u, p)) for u in U}) != 1
               for a, b in pts):
            ok = False
    else:        # a straddling orbit exists
        if not any(any((pow(a, u, p) + pow(b, u, p)) % p != 1 for u in U)
                   for a, b in pts):
            ok = False
check(ok, "RAD channel verdicts for [x + y = 1]: 2 and 3 decide "
          "(singleton orbits), 5..17 blind (straddling orbits found) -- "
          "deciding channels exactly p <= 3")

print()
print(f"ALL CHECKS PASSED ({CHECKS})")
