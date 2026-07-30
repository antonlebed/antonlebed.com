"""
explore_ruler_ladder.py -- THE RULER LADDER (the open descent from the
archimedean dial, a remainder left open by an earlier probe and
corrected in a later pass).

THE QUESTION. explore_archimedean_dial.py found undecidability has TWO
doors, both tower deletions: the archimedean borrow (machine layer) and
depth ladders at two places (predicate layer -- Buchi decidable at ONE
V_p, Villemaire undecidable at TWO). This record charts the predicate
dial fully and hunts the NECESSITY direction: is every route to
undecidability over <N,+> the re-import of a magnitude-reading ruler
that couples windows?

CONTACT (full-text): Bes "A survey of arithmetical definability";
BHMV "Logic and p-recognizable sets of integers" (Bull. Belg. Math. Soc.
1, 1994); Hieronymi-Schulz "A strong version of Cobham's theorem"
(STOC'22, arXiv:2110.11858); Schulz "Undefinability of multiplication in
Presburger arithmetic with sets of powers" (arXiv:2209.11858);
Bell-Block Gorman-Schulz "A dichotomy for k-automatic expansions of
Presburger arithmetic" (arXiv:2508.04851v2). Villemaire 1992 (TCS 106)
itself is paywalled; its theorem + both proof routes are carried in full
by the Bes and BHMV surveys.

THE LADDER (the predicate dial over <N,+>; all DEC/UND entries cited
theorems by others -- undecidability cannot be run; our contribution is
the chart, the ruler reading, and the run-verified door mechanisms):

  rung  added predicate(s)         theory   x definable?  citation
  ----------------------------------------------------------------------
  R0    eventually periodic        DEC      no   Presburger 1929; Cobham
        (the floor: what every scale agrees on -- Cobham 1969)
  R1a   one scale, tick marks      DEC      no   Semenov 1979/1983
        (k^N; sparse sets; f compatible with +: factorials, Fibonacci)
  R1b   one scale, full ladder     DEC      no   Buchi 1960 / Bruyere
        (V_k -- all k-automatic sets)
        [NOTHING sits between R1a and R1b in one base: for k-automatic
         non-periodic X, <N,+,X> defines ALL k-automatic sets or X is
         already <N,+,k^N>-definable -- Bell-Block Gorman-Schulz 2025]
  R2a   two indep scales, ticks    UND      NO   Hieronymi-Schulz 2022;
        (2^N, 3^N)                               Schulz 2022
  R2b   two indep scales, ladder   UND      YES  Villemaire 1992; Bes
        (V_k,V_l; V_k + any l-recognizable non-Presburger L)  1997
  --    one ladder + conversion    UND      YES  Cherlin-Point 1986
        (V_k, x->k^x: same base!)
  --    mid-scale archimedean read UND      YES  Putnam 1957; Buchi
        (squares; any poly range deg>=2)
  --    breadth-infinity           UND      YES  Woods 1981/J.Robinson
        (coprimality with +; divisibility with S: Robinson 1949)
        (coprimality with S only: UND (Woods), x open -- tied to the
        Erdos-Woods conjecture)
  --    Pascal triangle mod n      n = p^j: DEC (Korec 95, Bes 97a);
        (<N,=,B_n> alone, no +!)   n with 2 prime windows (first: 6 =
                                   2*3, the k = 2 rung; the first
                                   primorial that is not a prime
                                   power): + AND x definable from
                                   B_n ALONE (Korec 93)

THE RULER READING (synthesis; the necessity direction's state):
 - EVERY door mints a ruler: any non-Presburger M c= N definably yields
   an EXPANDING set -- unbounded gaps, a scale (Michaux-Villemaire 1996,
   Thm 29 in Bes's survey).
 - ONE ruler never opens the door: Semenov's compatibility criterion is
   literally "every derived linear probe is bounded or outruns the set"
   -- no readable MID-SCALE ruler (x^2 fails exactly because the
   successor-gap 2x+1 is one; verified S2). One full ladder (Buchi) is
   still decidable: a scale with nothing independent to compare against.
 - The door opens when TWO INDEPENDENT rulers get COMPARED: V_k+V_l /
   k^N+l^N (multiplicative independence = the joint ladder is dense,
   verified S1), B_6 (Lucas digit reads at two primes; Kummer: the
   binomial's p-content COUNTS CARRIES -- the inter-window coupling the
   tower deletes -- verified S5), coprimality-with-+ (breadth-infinity:
   co-support bounds size, the tower's own archimedean certificate,
   verified S3), divisibility (the full valuation profile).
 - Hansel's lemma is the impossibility half: a set recognizable in two
   independent scales is NOT expanding (no shared ruler) -- the
   Cobham floor from below.
 - THE KNIFE EDGE SPLITS (new precision vs the dial's earlier picture):
   undecidability =/= multiplication. <N,+,2^N,3^N> is undecidable
   (Hieronymi-Schulz) yet does NOT define x (Schulz, S-unit machinery):
   the archimedean re-import has TWO GRADES -- OVERHEARING (coupling
   enough to interpret undecidable questions) vs REBUILDING (definitional
   x). R2a is a no-man's-land strictly between Presburger and Peano.
 - NECESSITY stands OPEN in general, settled inside the charted classes:
   Semenov's criterion IS the no-mid-scale-ruler characterization for
   sparse sets/functions; Hieronymi-Schulz + the dichotomy close the
   automatic class (any two independent non-trivial scales suffice; one
   scale never does). The counterexample shape: an undecidable <N,+,X>
   defining no two independent expanding scales. No known specimen.

THE TOWER'S CORNER (why the finite-window family is the decidable
corner; each closure verified S4 or cited):
 - DEPTH <= 1 (residue fields): the ladder V_p truncates to the presence
   bit -- same residue tuple, unboundedly different depth (S4/PR11).
 - BREADTH <= k (finitely many windows): coprimality-to-fixed-support is
   p_k#-periodic = rung R0 (S4/PR12); the breadth door needs support
   beyond every bound, and its size leak min{n>1: n coprime to p_k#} =
   p_{k+1} (S3/PR9) is exactly the tower's own archimedean certificate.
 - ARCHIMEDEAN DELETED: the machine-layer borrow (the dial) and the
   mid-scale reads (squares) both live at the deleted place; carry-free
   addition is the deletion of what Kummer's theorem exposes (S5).

FINDINGS (tiers per the standard naming scale; every section asserts;
range = stated).

1. THE JOINT-LADDER DENSITY SPLIT (rule at the stated range + classical;
   S1). Multiplicative independence read as measurement, with the right
   object identified the hard way: the UNION of tick marks {2^a} u
   {3^b} NEVER densifies (full ratio-2 gaps -- a 2-gap no 3-power
   splits -- recur forever; 10 above sqrt(1e18) in range), but the
   PRODUCT ladder {2^a 3^b} that the two columns jointly generate DOES:
   per-decade max consecutive ratio 1.5000 (decade 0) -> 1.03932
   (decade 17), 0/17 up-steps. The DEPENDENT pair (2,8): its product
   ladder is {2^n}, every ratio locked at exactly 2 forever. And the
   comparison records min_a |a - b*log2(3)| over b <= 2000 improve
   EXACTLY at b = 1, 2, 5, 12, 41, 53, 306, 665 = the continued-
   fraction convergent denominators of log2(3), both sides computed
   from a 60-digit CF (Lagrange best-approximation). Two independent
   scales jointly generate a magnitude ruler of unbounded precision; a
   dependent pair never sharpens. This is the MECHANISM of the R2
   doors.

2. THE PUTNAM DOOR RUNS (rule, brute-verified 0 <= x <= 60, all
   y <= 3721; S2). The mid-scale archimedean read: y = x^2 iff
   [C(y) & C(y+2x+1) & no square strictly between] -- all pair-checks
   agree; z = xy recovered from squaring by the polarization identity
   (x+y)^2 = x^2 + 2z + y^2. The Semenov failure witness asserted: the
   square-gap probe A(x) = 2x+1 is unbounded AND below x^2 from x = 3
   -- a readable mid-scale ruler, exactly what compatibility-with-+
   forbids.

3. THE WOODS DOOR RUNS (rule, brute-verified at stated ranges; S3). The
   breadth-infinity read, pure coprimality: for distinct primes p,q <=
   60, min{z > 0: ~(z _|_ p) & ~(z _|_ q)} = pq exactly (naive scan);
   for primes p <= 100, min{z > p: same coprimality profile as p} = p^2
   exactly (SPF-sieve radicals). THE SIZE LEAK: min{n > 1: n _|_ p_k#}
   = p_{k+1} for k <= 12 -- unbounded breadth reads magnitude (a number
   invisible to k windows is at least p_{k+1}); the tower's naming
   criterion is the DECIDABLE truncation of Woods' door. The
   fingerprint census (observation, N <= 1e5): radical-window collision
   groups (rad(a+i) = rad(b+i), i = 0..w) collapse 8 (w = 1) -> 0
   (w = 2) below 1e5 -- identity pinning sharpens with every added
   window read; the (2,8) specimen dies at w = 2 (rad 4 =/= rad 10).
   Whether some finite w pins ALL integers is the Erdos-Woods
   CONJECTURE, open (strongly connected to x-definability in
   <N,S,_|_> -- Bes survey 4.2, "strongly connected", not proved
   equivalent); the related covering specimen -- every n inside
   (2184, 2200) shares a factor with an endpoint -- is verified
   directly (that 16 is the SMALLEST such width, the Erdos-Woods
   number, is cited, not run).

4. THE TOWER'S TRUNCATIONS CLOSE THE DOORS (rule, verified k = 4; S4).
   DEPTH: among n = 1..210, exactly the even n (frozen prediction 105,
   adjudicated by the assert) have V_2(n) =/= V_2(n+210): same residue
   tuple mod 210, different rung of the 2-ladder -- the window sees
   presence, never depth. BREADTH: gcd(n, 210) = gcd(n+210, 210) for
   n = 1..630 -- fixed-support coprimality is N-periodic, rung R0 of
   the ladder; the Woods ruler needs support beyond every bound
   (finding 3's leak at every k). ARCHIMEDEAN: the machine layer is the
   dial's (explore_archimedean_dial.py); the predicate layer's
   mid-scale reads (finding 2) live at the same deleted place.

5. THE KOREC DOOR IS A CARRY DETECTOR (rule, brute-verified x,y <= 243
   at p = 2,3; S5). Kummer's theorem run: v_p of C(x+y, x) EQUALS the
   number of carries when adding x and y in base p (verified on the
   exact integers, no Legendre shortcut). Lucas run: C(m,n) mod p =
   prod of digit binomials (both primes, all pairs). So the Pascal
   triangle mod n is a CARRY DETECTOR for base-p addition at every
   p | n: one prime window (n = p^j) = one detector = decidable
   (Korec 95/Bes 97a); two windows (n = 6 = the FIRST PRIMORIAL
   modulus) = two independent carry channels = + and x definable from
   B_6 alone (Korec 93) -- the two-ruler door in CRT dress, printed on
   Z/6. B_6 = CRT(B_2, B_3) verified, both Lucas reads live (witnesses
   where mod-2 distinguishes what mod-3 cannot and vice versa). The
   tower's carry-free componentwise addition (the dial's carry-freedom
   identity) is precisely the DELETION of what B_6 reads: the deleted
   place, seen from the Pascal triangle.

WHAT IT WOULD MEAN: undecidability over the additive integers
is, at every known door, the capacity to MEASURE -- to hold two
independent unbounded scales against each other. One scale is always
tame; two tick-marked scales already overhear enough to be unsolvable
yet cannot rebuild multiplication (a strict no-man's-land between
Presburger and Peano; its two halves -- undecidability, asked from the
mid-80s, and x-freeness, asked from 1996 -- were both settled only in
2022); and the
machine-layer borrow and the predicate-layer ruler are the SAME deleted
place read twice. If necessity holds in general, the Godel boundary of
additive arithmetic IS Ostrowski's boundary: unsolvability = the return
of the measuring stick.

RUN RECORD: python prime/code/explore_ruler_ladder.py -> ALL
SECTIONS PASS, 419,071 checks, ~0.5 s. Predictions PR1-PR14 fixed
before the run. Two discipline catches, recorded: (a) S1's first design
measured the UNION of tick marks and its trend-assert passed on a
fluctuation (the union's max ratio has limsup 2, it never densifies) --
the band-absorbed-bias species, caught by reading the printed values
against the hand law; redesigned to the product ladder, the true joint
object. (b) A remembered "Erdos-Woods radical witness (2184, 5197600)"
was a conflation of the EW-number interval with the EW-conjecture
profile; the assert killed it at i = 0 (fabricated-from-memory
constant), replaced by the true covering specimen.
"""

import math
from decimal import Decimal, getcontext
from fractions import Fraction

CHECKS = 0


def check(cond, msg=""):
    global CHECKS
    assert cond, msg
    CHECKS += 1


# ----------------------------------------------------------------------
# shared small number theory
# ----------------------------------------------------------------------

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
    return [i for i in range(n + 1) if sieve[i]]


def spf_sieve(n):
    """smallest prime factor for 0..n"""
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def rad(n, spf):
    r = 1
    while n > 1:
        p = spf[n]
        r *= p
        while n % p == 0:
            n //= p
    return r


def v_p(n, p):
    """exponent of p in n (n >= 1)"""
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def V_p(n, p):
    """largest POWER of p dividing n (Buchi's V), V_p >= 1"""
    return p ** v_p(n, p)


# ----------------------------------------------------------------------
# S1 -- the joint-ladder density split (the two-scales mechanism)
# ----------------------------------------------------------------------

def s1_joint_ladder():
    print("S1  the joint-ladder density split")
    LIMIT = 10 ** 18

    # the UNION of tick marks {2^a} u {3^b} never densifies: 2-gaps with
    # no 3-power inside recur forever (density of 3-powers per 2-gap in
    # log2 scale is 1/log2(3) ~ 0.63 < 1). Verify: full-ratio-2 gaps
    # keep appearing in the top half of the range.
    lad = sorted(set(
        [2 ** a for a in range(1, 70) if 2 ** a <= LIMIT] +
        [3 ** b for b in range(1, 45) if 3 ** b <= LIMIT]))
    late_locked = [x for x, y in zip(lad, lad[1:])
                   if y == 2 * x and x > LIMIT ** 0.5]
    check(len(late_locked) > 0, "union keeps ratio-2 gaps late")
    print(f"     union of tick marks: {len(late_locked)} full ratio-2 "
          f"gaps above sqrt(LIMIT) -- the union NEVER densifies")

    # the PRODUCT ladder {2^a 3^b} (the joint ruler the two columns
    # generate) DOES densify: per-decade max consecutive ratio -> 1
    prods = sorted(x for x in
                   (2 ** a * 3 ** b for a in range(70) for b in range(45))
                   if 2 <= x <= LIMIT)
    decades = {}
    for x, y in zip(prods, prods[1:]):
        d = len(str(x)) - 1
        decades[d] = max(decades.get(d, 0.0), y / x)
    ds = sorted(decades)
    first, last = decades[ds[0]], decades[ds[-1]]
    check(first > 1.4, "early decades coarse")
    check(last < 1.1, "late decades fine")
    ups = sum(1 for a, b in zip(ds, ds[1:]) if decades[b] > decades[a])
    check(ups <= 3, "near-monotone descent of the max gap")
    print(f"     product ladder {{2^a 3^b}}: decade max-ratio "
          f"{first:.4f} (decade {ds[0]}) -> {last:.5f} (decade {ds[-1]}), "
          f"{ups}/{len(ds)-1} up-steps -- the joint ruler densifies")

    # dependent pair (2,8): the product ladder {2^a 8^b} = {2^n} stays
    # locked at ratio exactly 2 forever -- no densification, ever
    prods8 = sorted(set(
        x for x in (2 ** a * 8 ** b for a in range(60) for b in range(20))
        if 2 <= x <= LIMIT))
    for x, y in zip(prods8, prods8[1:]):
        check(y == 2 * x, "dependent product ladder locked at ratio 2")
    print(f"     (2,8) product ladder: all {len(prods8)-1} ratios exactly "
          f"2 (multiplicative dependence = no ruler)")

    # comparison records at CF convergents of log2(3)
    getcontext().prec = 60
    alpha = Decimal(3).ln() / Decimal(2).ln()  # log2(3)
    # CF of alpha
    cf, x = [], alpha
    for _ in range(16):
        a = int(x)
        cf.append(a)
        x = 1 / (x - a)
    # convergent denominators
    ps, qs = [cf[0], cf[0] * cf[1] + 1], [1, cf[1]]
    for a in cf[2:]:
        ps.append(a * ps[-1] + ps[-2])
        qs.append(a * qs[-1] + qs[-2])
    conv_dens = set(q for q in qs if q <= 2000)
    # records of min_a |a - b*alpha| over b = 1..2000
    best = None
    records = []
    for b in range(1, 2001):
        t = b * alpha
        err = min(abs(t - int(t)), abs(t - int(t) - 1))
        if best is None or err < best:
            best = err
            records.append(b)
    check(set(records) == conv_dens,
          f"records {records} vs convergents {sorted(conv_dens)}")
    print(f"     records of min_a|a - b*log2(3)| at b = {records}")
    print(f"     = CF convergent denominators (Lagrange)   [PASS]")


# ----------------------------------------------------------------------
# S2 -- the Putnam door (mid-scale archimedean read: squares)
# ----------------------------------------------------------------------

def s2_putnam():
    print("S2  the Putnam door (squares)")
    B = 60
    top = B * B + 2 * B + 1
    squares = set(i * i for i in range(int(top ** 0.5) + 2))

    n_pairs = 0
    for x in range(B + 1):
        for y in range(top + 1):
            formula = (y in squares and (y + 2 * x + 1) in squares and
                       not any(z in squares
                               for z in range(y + 1, y + 2 * x + 1)))
            check(formula == (y == x * x), f"Putnam x={x} y={y}")
            n_pairs += 1
    print(f"     y = x^2 <=> [C(y) & C(y+2x+1) & no square between]: "
          f"{n_pairs} pair-checks")

    # polarization: z = xy from squaring
    n_pol = 0
    for x in range(B + 1):
        for y in range(B + 1 - x):
            z = ((x + y) ** 2 - x ** 2 - y ** 2)
            check(z == 2 * x * y, "polarization")
            n_pol += 1
    print(f"     z = xy by polarization identity: {n_pol} checks")

    # the Semenov failure witness: A(x) = 2x+1 is a mid-scale ruler
    for x in range(3, 200):
        check(2 * x + 1 < x * x, "A below the set from x = 3")
    check(2 * 199 + 1 > 200, "A unbounded")
    print("     square-gap probe A(x) = 2x+1: unbounded, below x^2 from "
          "x = 3 (the forbidden mid-scale ruler)   [PASS]")


# ----------------------------------------------------------------------
# S3 -- the Woods door (breadth-infinity: coprimality)
# ----------------------------------------------------------------------

def s3_woods():
    print("S3  the Woods door (coprimality)")
    ps60 = primes_upto(60)
    n_mp = 0
    for i, p in enumerate(ps60):
        for q in ps60[i + 1:]:
            z = 1
            while not (math.gcd(z, p) > 1 and math.gcd(z, q) > 1):
                z += 1
            check(z == p * q, f"MULTP {p},{q}")
            n_mp += 1
    print(f"     min z non-coprime to both = pq: {n_mp}/{n_mp} prime pairs")

    ps100 = primes_upto(100)
    spf = spf_sieve(101 * 101)
    for p in ps100:
        z = p + 1
        while rad(z, spf) != p:
            z += 1
        check(z == p * p, f"profile {p}")
    print(f"     min z > p with p's coprimality profile = p^2: "
          f"{len(ps100)}/{len(ps100)} primes")

    # the size leak: min n > 1 coprime to p_k# is p_{k+1}
    ps = primes_upto(50)
    for k in range(1, 13):
        firstk = ps[:k]
        n = 2
        while any(n % p == 0 for p in firstk):
            n += 1
        check(n == ps[k], f"size leak k={k}")
    print("     min{n>1: n _|_ p_k#} = p_(k+1) for k = 1..12 "
          "(co-support bounds size: the archimedean certificate)")

    # fingerprint census: radical-window collisions up to 1e5
    N = 10 ** 5
    spf = spf_sieve(N + 8)
    rads = [0] * (N + 8)
    for i in range(1, N + 8):
        rads[i] = rad(i, spf)
    counts = {}
    prev = None
    for w in range(1, 9):
        groups = {}
        for a in range(1, N):
            key = tuple(rads[a + i] for i in range(w + 1))
            groups.setdefault(key, []).append(a)
        col = {k: v for k, v in groups.items() if len(v) > 1}
        counts[w] = len(col)
        if prev is not None:
            check(counts[w] <= prev, "collisions non-increasing in w")
        prev = counts[w]
        if counts[w] == 0:
            break
    check(counts[1] > 0, "w=1 collisions exist")
    # (2,8) is a w=1 specimen
    check(rads[2] == rads[8] and rads[3] == rads[9], "(2,8) at w=1")
    check(rads[4] != rads[10], "(2,8) dies at w=2")
    seq = " -> ".join(f"{counts[w]} (w={w})" for w in sorted(counts))
    print(f"     radical-window collision groups, N <= 1e5: {seq}")

    # the covering specimen that keeps the S-only door delicate: 16 is
    # an Erdos-Woods NUMBER -- every n strictly inside [2184, 2200]
    # shares a prime factor with an endpoint (the interval the endpoints
    # cover; the smallest such k = 16). Verified directly.
    a, b = 2184, 2200
    for n in range(a + 1, b):
        check(math.gcd(n, a) > 1 or math.gcd(n, b) > 1, f"EW cover {n}")
    print(f"     the covering specimen: every n in ({a},{b}) shares a "
          f"factor with an endpoint (width 16 = the smallest "
          f"Erdos-Woods number, cited)")
    print("     identity pinning sharpens with breadth; whether some "
          "finite w pins ALL integers = the Erdos-Woods conjecture "
          "(open; tied to x-definability in <N,S,_|_>)   [PASS]")


# ----------------------------------------------------------------------
# S4 -- the tower's truncations close the doors
# ----------------------------------------------------------------------

def s4_tower_closures():
    print("S4  the tower's truncations")
    N = 210  # k = 4
    diff = sum(1 for n in range(1, N + 1) if V_p(n, 2) != V_p(n + N, 2))
    check(diff == 105, f"depth invisibility count {diff}")
    print(f"     depth: {diff}/210 residues (all even n) carry a 2-ladder "
          f"rung the tuple cannot see")

    for n in range(1, 3 * N + 1):
        check(math.gcd(n, N) == math.gcd(n + N, N), "breadth periodicity")
    print("     breadth: gcd(n,210) is 210-periodic -- fixed-support "
          "coprimality sits at rung R0 (the floor)")


# ----------------------------------------------------------------------
# S5 -- the Korec door is a carry detector (Kummer + Lucas at 2,3)
# ----------------------------------------------------------------------

def carries(x, y, p):
    c, n = 0, 0
    carry = 0
    while x > 0 or y > 0 or carry:
        s = x % p + y % p + carry
        carry = 1 if s >= p else 0
        c += carry
        x //= p
        y //= p
        n += 1
        if n > 200:
            break
    return c


def lucas_rhs(m, n, p):
    r = 1
    while m > 0 or n > 0:
        r = (r * math.comb(m % p, n % p)) % p if n % p <= m % p else 0
        if r == 0:
            return 0
        m //= p
        n //= p
    return r


def s5_korec():
    print("S5  the Korec door (Pascal mod n = carry detector)")
    B = 243
    n_kum = 0
    for p in (2, 3):
        for x in range(B + 1):
            for y in range(B + 1):
                c = math.comb(x + y, x)
                check(v_p(c, p) == carries(x, y, p), f"Kummer p={p}")
                n_kum += 1
    print(f"     Kummer: v_p(C(x+y,x)) = #carries base p, p = 2,3: "
          f"{n_kum} pairs on exact integers")

    n_luc = 0
    for p in (2, 3):
        for m in range(B + 1):
            for n in range(m + 1):
                check(math.comb(m, n) % p == lucas_rhs(m, n, p),
                      f"Lucas p={p}")
                n_luc += 1
    print(f"     Lucas: C(m,n) mod p = prod of digit binomials: "
          f"{n_luc} pairs")

    # B_6 = CRT(B_2, B_3); both reads live
    wit2 = wit3 = None
    seen = {}
    for x in range(101):
        for y in range(101):
            b = math.comb(x + y, x)
            b2, b3, b6 = b % 2, b % 3, b % 6
            check(b6 % 2 == b2 and b6 % 3 == b3, "CRT")
            seen[(x, y)] = (b2, b3)
    items = list(seen.items())
    for i in range(len(items)):
        (xy, (a2, a3)) = items[i]
        if wit2 and wit3:
            break
        for (xy2, (c2, c3)) in items[i + 1:]:
            if a2 != c2 and a3 == c3 and not wit2:
                wit2 = (xy, xy2)
            if a2 == c2 and a3 != c3 and not wit3:
                wit3 = (xy, xy2)
            if wit2 and wit3:
                break
    check(wit2 is not None and wit3 is not None, "both Lucas reads live")
    print(f"     B_6 = CRT(B_2,B_3); mod-2 separates {wit2[0]},{wit2[1]}; "
          f"mod-3 separates {wit3[0]},{wit3[1]}")
    print("     one prime window = one carry channel = decidable "
          "(Korec 95); two windows (n = 6 = 2*3, the k = 2 rung) "
          "= + and x from B_6 alone (Korec 93)   [PASS]")


if __name__ == "__main__":
    import time
    t0 = time.time()
    s1_joint_ladder()
    s2_putnam()
    s3_woods()
    s4_tower_closures()
    s5_korec()
    print(f"ALL SECTIONS PASS -- {CHECKS} checks, "
          f"{time.time() - t0:.1f} s")
