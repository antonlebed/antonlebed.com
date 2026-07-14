"""
The quantifier ladder: divisor-indexed partial collapses.

The idempotent-logic entry's named reopen question:
the partial collapses a^m, m | lambda, as a quantifier ladder between
the identity (m = 1) and the pair's collapse (m = lambda). THE BAR:
a ladder rung must decide something the pair alone cannot --
otherwise it is relabeled collapse and this chart says so.

Builds on the quantifier pair and envelope: DIA(a) =
a^lambda ("true to some degree"), BOX(a) = 1 - (1-a)^lambda ("fully
true"), the envelope bracketing every NNF formula's classical shadow
from the two leaf bits, with dependent shadows at repeated leaves
named open (a AND NOT a fully true wherever delta(x) = -1 is
solvable).

PREDICTIONS (stated before the run):
 P1 (rule, proved): THE TWO-LAYER LADDER. Raw rungs a^m filter, gates
    quantify. Raw layer: per channel the image of x -> x^m is the
    d-th-power subgroup plus 0, d = gcd(m, p-1); m | m' makes a^m'
    a function of a^m (a filtration of forgetting -- rungs are NOT
    projections in general, see P6). The De Morgan conjugacy
    DIA_m(NOT a) = NOT BOX_m(a), with DIA_m(a) = a^m and BOX_m(a) =
    1 - (1-a)^m, is DEFINITIONAL at every rung -- both sides are
    (1-a)^m. Gate layer: gate_m(a) = BOX(a^m) is bit-valued (lands
    on the idempotent lattice) and reads [ord(a) | m] per channel
    (0 reads no); gate_1 = BOX, gate_lambda = DIA -- THE PAIR IS THE
    TWO ENDS OF ONE d(lambda)-RUNG FAMILY, monotone along the
    divisor lattice, meet-exact (gate_gcd = gate_m AND gate_m'),
    gcd-complete (any integer exponent's gate = its gcd-with-lambda
    divisor's -- on the ring's channels, where p-1 | lambda by
    construction; a bare field outside the ring gcd's with its own
    p-1), all d(240) = 20 rungs distinct as functions on RAD.
 P2 (rule, proved): REPEATED LEAVES ARE THE LADDER. BOX of the m-fold
    AND of one leaf IS gate_m (definitional: the m-fold AND is a^m);
    DIA of the m-fold OR is the conjugate gate NOT gate_m(NOT a);
    the two cross-reads absorb into the pair (DIA of m-fold AND =
    DIA, BOX of m-fold OR = BOX). What repeated leaves compute
    beyond the pair is exactly order information -- the envelope's
    repeated-leaf gap and the ladder are the same object.
 P3 (the bar -- rule + witnesses): the dependent shadow
    BOX(a AND NOT a) = [a(1-a) = 1] = [Phi_6(a) = 0] identically
    (x - x^2 = 1 <=> x^2 - x + 1 = 0); for p != 3 its channel read
    is [ord(a) = 6] = the ladder's FIRST JOIN DEFECT
    gate_6 AND NOT(gate_2 OR gate_3) -- every gate join at lcm < 6
    is exact, the join first leaks at lcm(2,3) = 6 (the smallest
    non-prime-power order). Pair-decidability splits by the channel
    prime mod 3: p = 1 mod 3 (split in Q(zeta_6)) -- the pair is
    BLIND (graded residues share its bits, shadows differ);
    p = 2 mod 3 (inert) -- vacuously false, no Phi_6 roots;
    p = 3 (ramified) -- the rigidity pins the single graded point,
    the pair decides. The ladder decides EVERY channel with zero
    errors (exhaustive + ring-level stream); the pair-only envelope
    floor is identically 0 here (it can never certify this shadow
    true). On RAD the ladder earns exactly channels 7 and 13.
 P4 (rule): THE RIGIDITY IS THE RAMIFIED PRIME. Phi_6 = x^2 - x + 1
    has discriminant -3: root count mod p = 2 / 0 / 1 for p = 1,
    2 mod 3, p = 3, the split-root difference squaring to -3, and
    at p = 3 the single DOUBLE root is -1 = F_3's only graded point.
    At p = 3 the ladder folds: gate_6 = gate_2 (gcd(6, p-1) = 2) --
    the order-6 read drops to the order-2 rung exactly at the
    ramified channel, and p = 3 is the one odd channel whose graded
    region is a single point (pair bits pin the residue).
 P5 (the ladder's own wall -- rule for the swept range): the leaf
    ladder (both directions) measures exactly the joint order
    profile (ord(a), ord(1-a)). Shadows whose root condition is not
    cyclotomic escape: BOX(a AND a AND NOT a) = [a^2(1-a) = 1]
    first collides at p = 11 (x = 9 vs y = 3, both profile (5,5),
    shadows 1 vs 0); the Phi_6 shadow never collides (control).
    Multi-variable dependent shadows escape ALL single-leaf
    measurements: [ab = 1] (a AND b fully true) admits same-profile
    b's with different shadows (witness at p = 7) -- relative order
    is not a leaf quantity. The one-variable cyclotomic family is
    exactly the ladder's reach.
 P6 (rule, proved): THE PROJECTIONS. x -> x^e is an idempotent MAP
    on the ring iff e^2 = e mod lambda -- the idempotents of the
    EXPONENT RING Z/lambda, 2^omega(lambda) Hall projections (RAD:
    omega(240) = 3, count 8) splitting truth-degree by lambda's
    primes: the class-e projection keeps q^v_q(ord x) for the
    primes q with e = 1 mod q^v_q(lambda) and kills the rest. The
    identity (e = 1) and the collapse (e = 0, i.e. DIA) are the
    lattice's top and bottom: the logic's projection lattice is the
    idempotent lattice of Z/lambda, one level down (the second-log
    contact).

RESULTS (the run below prints the record; all six confirmed):
  P1 image law exhaustive (p <= 23, all 20 divisors); gate = order
     read exhaustive (9 channels x all residues x 20 rungs);
     endpoints, monotonicity (60 divisor pairs), meet-exactness
     (400 pairs, exhaustive residues), gcd-completeness (200
     sampled exponents to 10^4) all exact; 20/20 rungs distinct on
     RAD; ring-polynomial form 1 - (1 - a^m)^lambda matches the
     channel gates and lands on the lattice (300 RAD samples x 20
     rungs, 6000 idempotency checks).
  P2 all four repeated-leaf reads exhaustive (9 channels, divisors
     + non-divisor exponents): two absorb, two are the ladders.
  P3 shadow = Phi_6 = ord-6 exhaustive; join exact below 6 (the
     minimal defective lcm over all 400 rung pairs is exactly 6);
     join-defect formula = shadow at every (p, x) with p <= 23
     EXCEPT exactly (3, -1); pair blind exactly at p = 7, 13, 19
     (the split primes <= 23); ladder decision 0 errors exhaustive
     + 0/35,000 channel-verdicts on 5,000 RAD ring samples (pair
     envelope floor identically 0 on all of them; ladder certifies
     the 3,862 true-shadow channel slots the pair must leave open).
  P4 root law verified all p <= 199 (split difference^2 = -3 every
     split prime; double root -1 at p = 3); gate_6 = gate_2 at
     p = 3 exhaustive; graded region size p-2 => singleton iff
     p = 3.
  P5 control clean (Phi_6 never profile-collides, p <= 100);
     x^2(1-x) collides first at p = 11 (witness (9,3) found by
     search), 16 colliding profile classes over p <= 100;
     multi-variable [ab = 1] witness at p = 7 (a = 3; b = 5 and
     b' = 3 share profile (6,6), shadows 1 vs 0).
  P6 census: idempotent maps among the 240 exponent classes =
     exactly {0,1,16,81,96,145,160,225} = the solutions of
     e^2 = e mod 240 (8 = 2^3); Hall order-splitting law exhaustive
     over all RAD channels; top/bottom = identity/DIA.

Tier: P1, P2, P6 rule (proved by the identities named above;
verified exhaustively as stated). P3, P4 rule (proved per channel:
Phi_6 algebra + the splitting of primes in Q(zeta_6); censuses
exhaustive p <= 23 / p <= 199). P5 rule for the swept ranges
(p <= 100 one-variable, p = 7 multi-variable witness), observation
beyond.

Runs on RAD (k = 7) with exhaustive per-channel censuses. ~0.1 s,
tiny memory. ALL CHECKS PASSED (29).
"""

import sys, os, random
from math import gcd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import RAD_RING, encode, primes_up_to

random.seed(75)
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

DIVS = [d for d in range(1, LAM + 1) if LAM % d == 0]      # 20 divisors of 240

def ordp(x, p):
    o, y = 1, x % p
    while y != 1:
        y = y * x % p
        o += 1
    return o

ALL_P = [2, 3, 5, 7, 11, 13, 17, 19, 23]                   # census channels

def diap(y, p):  return 1 if y % p else 0                  # [y != 0]
def boxp(y, p):  return 1 if y % p == 1 else 0             # [y = 1]
def gatep(x, m, p):  return boxp(pow(x, m, p), p)          # [ord(x) | m], 0 -> 0
def cgatep(x, m, p): return 1 - gatep((1 - x) % p, m, p)   # conjugate gate

# ----------------------------------------------------------------------
section("I. THE TWO-LAYER LADDER (raw rungs filter, gates quantify)")
# ----------------------------------------------------------------------

ok = True
for p in ALL_P:
    for m in DIVS:
        img = {pow(x, m, p) for x in range(p)}
        if len(img) != (p - 1) // gcd(m, p - 1) + 1:
            ok = False
check(ok, "raw rung image per channel = the gcd(m,p-1)-th powers + 0 "
          "(exhaustive p <= 23, all 20 divisors)")

# Conjugacy is definitional at every rung: DIA_m(NOT a) and
# NOT BOX_m(a) are both (1-a)^m -- one spot confirmation suffices.
ok = all(pow((1 - x) % p, m, p) == (1 - (1 - pow((1 - x) % p, m, p))) % p
         for p in ALL_P for x in range(p) for m in DIVS[:6])
check(ok, "rung-uniform De Morgan conjugacy DIA_m NOT = NOT BOX_m "
          "(definitional: both sides are (1-a)^m)")

ok = True
for p in ALL_P:
    ords = {x: ordp(x, p) for x in range(1, p)}
    for x in range(p):
        for m in DIVS:
            expect = 1 if (x and m % ords[x] == 0) else 0
            if gatep(x, m, p) != expect:
                ok = False
check(ok, "gate_m = BOX(a^m) reads [ord(a) | m] per channel, 0 reads no "
          "(exhaustive, 9 channels x residues x 20 rungs)")

ok = all(gatep(x, 1, p) == boxp(x, p) and gatep(x, LAM, p) == diap(x, p)
         for p in PRIMES for x in range(p))
check(ok, "endpoints: gate_1 = BOX, gate_lambda = DIA -- the pair is the "
          "two ends of one family (exhaustive, RAD channels)")

ok = True
for p in ALL_P:
    for x in range(p):
        gs = {m: gatep(x, m, p) for m in DIVS}
        for m in DIVS:
            for m2 in DIVS:
                if m2 % m == 0 and gs[m] > gs[m2]:
                    ok = False
                if gs[gcd(m, m2)] != (gs[m] & gs[m2]):
                    ok = False
check(ok, "monotone along the divisor lattice + meet-exact "
          "(gate_gcd = gate_m AND gate_m'; exhaustive, 400 rung pairs)")

ok = True
for _ in range(200):
    m = random.randrange(1, 10001)
    # ring channels (p-1 | lambda by construction): gcd with lambda
    for p in PRIMES:
        x = random.randrange(p)
        if gatep(x, m, p) != gatep(x, gcd(m, LAM), p):
            ok = False
    # a bare census field outside the ring: gcd with its own p-1
    for p in (19, 23):
        x = random.randrange(p)
        if gatep(x, m, p) != gatep(x, gcd(m, p - 1), p):
            ok = False
check(ok, "gcd-complete: any integer exponent's gate = a divisor rung's "
          "(gcd with lambda on ring channels, with p-1 at a bare field; "
          "200 sampled exponents to 10^4)")

realized = set()
for p in PRIMES:
    for x in range(1, p):
        realized.add(ordp(x, p))
sigs = {}
for m in DIVS:
    sigs.setdefault(frozenset(d for d in realized if m % d == 0), []).append(m)
check(len(sigs) == len(DIVS),
      f"all {len(DIVS)} rungs distinct as functions on RAD "
      f"(realized orders {sorted(realized)})")

def ring_gate(a, m):
    return (1 - pow((1 - pow(a, m, N)) % N, LAM, N)) % N

ok_match = ok_idem = True
for _ in range(300):
    a = random.randrange(N)
    res = encode(a, R)
    for m in DIVS:
        g = ring_gate(a, m)
        if g * g % N != g:
            ok_idem = False
        gr = encode(g, R)
        if any(gr[i] != gatep(res[i], m, PRIMES[i]) for i in range(len(PRIMES))):
            ok_match = False
check(ok_match, "ring polynomial 1 - (1 - a^m)^lambda = the channel gates "
                "(300 RAD samples x 20 rungs)")
check(ok_idem, "every gate value is an idempotent -- the ladder outputs "
               "land on the lattice (6000 ring checks)")

# ----------------------------------------------------------------------
section("II. REPEATED LEAVES ARE THE LADDER")
# ----------------------------------------------------------------------
# m-fold AND of one leaf = a^m; m-fold OR = 1 - (1-a)^m.

EXPS = DIVS[:12] + [7, 9, 14, 100]
ok1 = ok2 = ok3 = ok4 = True
for p in ALL_P:
    for x in range(p):
        for m in EXPS:
            andm = pow(x, m, p)
            orm = (1 - pow((1 - x) % p, m, p)) % p
            if boxp(andm, p) != gatep(x, m, p): ok1 = False
            if diap(andm, p) != diap(x, p):     ok2 = False
            if boxp(orm, p) != boxp(x, p):      ok3 = False
            if diap(orm, p) != cgatep(x, m, p): ok4 = False
check(ok1, "BOX(m-fold AND) = gate_m -- the gate ladder IS the shadow "
           "of the repeated-AND family")
check(ok2 and ok3, "the two cross-reads absorb into the pair "
                   "(DIA of m-fold AND = DIA; BOX of m-fold OR = BOX)")
check(ok4, "DIA(m-fold OR) = the conjugate gate NOT gate_m(NOT a) -- "
           "the descending ladder")

# ----------------------------------------------------------------------
section("III. THE BAR: the dependent shadow is a ladder read")
# ----------------------------------------------------------------------

def shadow6(x, p):  return 1 if x * (1 - x) % p == 1 else 0
def defect6(x, p):  return gatep(x, 6, p) & (1 - (gatep(x, 2, p) | gatep(x, 3, p)))

ok = all((x * (1 - x) % p == 1) == ((x * x - x + 1) % p == 0)
         for p in ALL_P for x in range(p))
check(ok, "BOX(a AND NOT a) per channel = [Phi_6(a) = 0] "
          "(x - x^2 = 1 <=> x^2 - x + 1 = 0; exhaustive)")

ok = True
for p in ALL_P:
    if p == 3:
        continue
    for x in range(p):
        if shadow6(x, p) != (1 if (x and ordp(x, p) == 6) else 0):
            ok = False
check(ok, "for p != 3 the shadow's channel read is [ord(a) = 6] "
          "(the primitive 6th roots; exhaustive)")

# join exactness below 6, first defect at lcm(2,3) = 6
min_defective_lcm = None
for p in ALL_P:
    for x in range(p):
        gs = {m: gatep(x, m, p) for m in DIVS}
        for m in DIVS:
            for m2 in DIVS:
                l = m * m2 // gcd(m, m2)
                if gs[l] > (gs[m] | gs[m2]):
                    if min_defective_lcm is None or l < min_defective_lcm:
                        min_defective_lcm = l
check(min_defective_lcm == 6,
      f"gate joins are exact below 6; the FIRST join defect is at "
      f"lcm(2,3) = 6 (minimal defective lcm = {min_defective_lcm})")

exceptions = [(p, x) for p in ALL_P for x in range(p)
              if defect6(x, p) != shadow6(x, p)]
check(exceptions == [(3, 2)],
      "join-defect formula gate_6 AND NOT(gate_2 OR gate_3) = the shadow "
      "at every (p, x) EXCEPT exactly (3, -1) -- the ramified channel")

blind = []
for p in ALL_P:
    graded_shadows = {shadow6(x, p) for x in range(2, p)}
    if len(graded_shadows) > 1:
        blind.append(p)
check(blind == [7, 13, 19],
      "the pair is blind exactly at the split primes p = 1 mod 3 "
      "(graded residues share its bits, shadows differ); inert channels "
      "vacuously false, p = 3 pinned -- RAD's ladder-earned channels: 7, 13")

def decision(x, p):
    if p == 3:                       # ramified: rigidity pins the graded point
        return 1 if (diap(x, p) and not boxp(x, p)) else 0
    return defect6(x, p)

ok = all(decision(x, p) == shadow6(x, p) for p in ALL_P for x in range(p))
check(ok, "ladder decision (join defect + the p = 3 pin) = the shadow, "
          "zero errors (exhaustive all channels)")

err = tot = certified_true = 0
floor_zero = True
for _ in range(5000):
    a = random.randrange(N)
    res = encode(a, R)
    F = a * (1 - a) % N
    sh = encode((1 - pow((1 - F) % N, LAM, N)) % N, R)
    for i, p in enumerate(PRIMES):
        tot += 1
        s = 1 if sh[i] == 1 else 0
        if decision(res[i], p) != s:
            err += 1
        if s:
            certified_true += 1
        # pair-only envelope floor of a AND NOT a: BOX a AND NOT DIA a = 0
        if (boxp(res[i], p) & (1 - diap(res[i], p))) != 0:
            floor_zero = False
print(f"  ring stream: {tot} channel-verdicts on 5000 RAD samples, "
      f"{err} ladder errors; {certified_true} true-shadow slots")
check(err == 0, f"ring-level: 0 ladder errors / {tot} channel-verdicts")
check(floor_zero and certified_true > 0,
      f"the pair envelope's floor is identically 0 here -- it can never "
      f"certify this shadow true; the ladder certifies all "
      f"{certified_true} true slots")

# ----------------------------------------------------------------------
section("IV. THE RIGIDITY IS THE RAMIFIED PRIME (Phi_6, disc = -3)")
# ----------------------------------------------------------------------

ok = True
for p in primes_up_to(199):
    roots = [x for x in range(p) if (x * x - x + 1) % p == 0]
    if p == 3:
        if roots != [2] or (2 * 2 - 1) % 3 != 0:      # double root: Phi_6' = 2x-1
            ok = False
    elif p % 3 == 1:
        if len(roots) != 2 or (roots[0] - roots[1]) ** 2 % p != (-3) % p:
            ok = False
    else:
        if roots:
            ok = False
check(ok, "root law all p <= 199: 2 roots iff p = 1 mod 3 (difference^2 "
          "= -3), 0 iff p = 2 mod 3, double root -1 at the ramified p = 3")

ok = all(gatep(x, 6, 3) == gatep(x, 2, 3) for x in range(3))
check(ok, "at p = 3 the ladder folds: gate_6 = gate_2 (gcd(6, p-1) = 2) -- "
          "the order-6 read drops to the order-2 rung")

check(all(len(range(2, p)) == p - 2 for p in ALL_P) and
      [p for p in ALL_P if p > 2 and p - 2 == 1] == [3],
      "graded region has p-2 points: p = 3 is the only odd channel where "
      "the pair bits PIN the graded residue (the rigidity, pair-side)")

# ----------------------------------------------------------------------
section("V. THE LADDER'S WALL: the joint order profile is all it sees")
# ----------------------------------------------------------------------

def prof(x, p):  return (ordp(x, p), ordp((1 - x) % p, p))

first = None
total_collisions = 0
control_collisions = 0
for p in primes_up_to(100):
    if p < 5:
        continue
    t3, t6 = {}, {}
    for x in range(2, p):
        pr = prof(x, p)
        t3.setdefault(pr, set()).add(1 if (x * x % p) * (1 - x) % p == 1 else 0)
        t6.setdefault(pr, set()).add(shadow6(x, p))
    c = sum(1 for v in t3.values() if len(v) > 1)
    control_collisions += sum(1 for v in t6.values() if len(v) > 1)
    total_collisions += c
    if c and first is None:
        first = p
check(control_collisions == 0,
      "control: the Phi_6 shadow NEVER profile-collides (it is an order "
      "read; p <= 100)")
check(first == 11 and prof(9, 11) == prof(3, 11) == (5, 5),
      f"BOX(a AND a AND NOT a) = [a^2(1-a) = 1] escapes the ladder: first "
      f"collision at p = 11 (x = 9 shadow 1, y = 3 shadow 0, both profile "
      f"(5,5)); {total_collisions} colliding profiles over p <= 100")

p = 7
witness = None
for a in range(2, p):
    byprof = {}
    for b in range(2, p):
        byprof.setdefault(prof(b, p), []).append(b)
    for pr, bs in byprof.items():
        vals = {b: 1 if a * b % p == 1 else 0 for b in bs}
        if len(set(vals.values())) > 1:
            witness = (a, bs)
            break
    if witness:
        break
check(witness is not None,
      f"multi-variable: [ab = 1] (a AND b fully true) is NOT a leaf-profile "
      f"read -- witness at p = 7: a = {witness[0]}, b in {witness[1]} share "
      f"profiles, shadows differ (relative order is not a leaf quantity)")

# ----------------------------------------------------------------------
section("VI. THE PROJECTIONS: idempotents of the exponent ring Z/lambda")
# ----------------------------------------------------------------------

idem_maps = []
for e in range(LAM):
    E = e if e >= 1 else LAM
    if all(pow(pow(x, E, p), E, p) == pow(x, E, p)
           for p in PRIMES for x in range(p)):
        idem_maps.append(e)
expected = [e for e in range(LAM) if e * e % LAM == e]
check(idem_maps == expected and len(expected) == 8,
      f"x -> x^e is an idempotent map iff e^2 = e mod lambda: the 8 = 2^3 "
      f"idempotents of Z/240 exactly ({expected})")

def vq(n, q):
    v = 0
    while n % q == 0:
        n //= q; v += 1
    return v

LAMQ = sorted({q for q in range(2, LAM + 1) if LAM % q == 0 and
               all(q % r for r in range(2, q))})
ok = True
for e in idem_maps:
    E = e if e >= 1 else LAM
    kept = [q for q in LAMQ if e % q ** vq(LAM, q) == 1]
    for p in PRIMES:
        for x in range(1, p):
            o = ordp(x, p)
            target = 1
            for q in kept:
                target *= q ** vq(o, q)
            if ordp(pow(x, E, p), p) != target:
                ok = False
check(ok, f"Hall split: projection e keeps exactly the q-parts of the "
          f"order with e = 1 mod q^v_q(lambda), q in {LAMQ} "
          f"(exhaustive, all RAD units, all 8 projections)")

ok = 1 in idem_maps and 0 in idem_maps
for _ in range(200):
    a = random.randrange(N)
    c = pow(a, LAM, N)                    # the e = 0 projection
    if pow(a, 1, N) != a or c * c % N != c or \
       any((r != 0) != (cr == 1) for r, cr in zip(encode(a, R), encode(c, R))):
        ok = False
check(ok, "top and bottom: e = 1 is the identity, e = 0 (exponent lambda) "
          "is the collapse DIA = e_supp -- the pair brackets the "
          "projection lattice (200 RAD samples)")

print()
print("=" * 72)
print(f"ALL CHECKS PASSED ({CHECKS})")
print("=" * 72)
