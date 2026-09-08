"""explore_storey_descent.py -- THE STOREY DESCENT: does the p^m-power
Kummer defect of zeta_p in a local field descend to a subfield, and
by what law (the open question left by explore_cutoff_ladder.py's
finding 4).

THE QUESTION. For a local field K with zeta_p in K, the p^m-power
Kummer defect is D_m(K) = max_y v_K(y^(p^m) - zeta_p), the ceiling of
the (i*/p^m, m)-game and the per-root cutoff D_m/p^m of the wild
layer (explore_cutoff_ladder.py CL1). x^18+3 has D_1 = 25 and D_2 =
21 = 3 * 7 = e(K/C) * D_1(C) for the cube subfield C = x^6+3. The
transport argument tried there had a gap (the C-witness is a K-cube
only mod U_4). Is the arithmetic a law, and for which storeys?

THE HAND DERIVATION (before this file existed).

SD1 (the collapse). Let K/C be totally ramified of degree p with
    zeta_p in C, so K = C(theta), theta^p = b in C (Kummer), and let
    pi_K be a uniformizer with O_K = O_C[pi_K]. Every y in O_K is
    sum_{j<p} c_j pi_K^j with c_j in O_C, and
      y^p == sum_j c_j^p pi_K^(pj)   (mod p O_K)
    (the multinomial's mixed terms carry p). If pi_K^p is a C-element
    to level L in v_K units, then y^p is a C-element mod pi_K^L:
      radical storey, b = pi_C, pi_K = theta:  pi_K^p = pi_C exactly,
        L = e_K;
      unit-root storey, b = 1 + beta pi_C^l with i*_C < l < e_C and
        p not dividing l: v_K(theta - 1) = l, pi_K = (theta-1)^a /
        pi_C^b' with al - b'p = 1, (theta-1)^p = (b-1) + p r with
        v_K(r) >= l (the binomial middle vanishes at theta = 1), so
        pi_K^p = (b-1)^a pi_C^(-b'p) + O(pi_K^(e_K + p - (p-1)l)) and
        L = min(e_K, e_K + p - (p-1) l); l = 4 over x^6+3 reads 13,
        l = 8 over x^12+3 reads 23. SD2 below needs (p-1)L >= e_K,
        which bounds l <= 3 e_C/4 + 1 at p = 3 (13 >= 9, 23 >= 18 at
        the two built); a storey above that bound is outside SD3's
        scope, its congruence level (m-2)e_K + pL being the smaller.
    Conversely every c in O_C is such a sum to level L: position
    n = pi + j of c is controlled by digit i of c_j and the map is
    triangular in the leading digits, so it is ONTO O_C / pi_K^L.
    So {y^p mod pi_K^L : y in O_K} = (O_C + pi_K^L O_K) / pi_K^L.

SD2 (the lift). y^p = c + r, v_K(r) >= L, gives
      y^(p^m) == c^(p^(m-1))   (mod pi_K^(L + (m-1) e_K))
    (the k-th binomial term has valuation >= (m-1-v_p(k)) e_K + k L
    >= (m-1) e_K + L for k >= 1, using (p-1)L >= e_K, the scope
    condition of SD1).

SD3 (the theorem). Hence for m >= 2, with A = p D_(m-1)(C):
      D_m(K) = p * D_(m-1)(C)        if A < (m-1) e_K + L,
      D_m(K) >= (m-1) e_K + L         otherwise.
    Upper: any y has its c with v_K(c^(p^(m-1)) - zeta) <= A < the
    congruence level, so v_K(y^(p^m) - zeta) equals it. Lower: take
    c the C-witness, y any preimage under SD1. At m = 1 the same
    argument gives only D_1(K) >= L (c = zeta_p itself): the first
    defect of a storey is FRESH and at least L; every higher rung is
    the storey below's, times p. For odd p and m >= 2 the clause
    holds automatically at a radical storey unless the ladder is at
    torsion and off the boundary D_(m-1)(C) = p i*_C (A <= p^2 i*_C
    = p e_K/(p-1) <= (m-1) e_K + L, strict off the boundary).

SD4 (the unramified storey). K/C unramified: the digits of y^(p^m)
    are F_C-polynomials in the digits of y; matching zeta_p's digits
    level by level, the newest digit enters by Frobenius (unique,
    F_C-rational) or linearly, except at the Artin-Schreier level,
    whose first output level is p i*_C. So D_m(K) = D_m(C) whenever
    D_m(C) != p i*_C, and only the boundary value can move (it may
    split: the designed sextic's lift, explore_cutoff_ladder.py
    finding 3).

SD5 (the radical tower). C_0 = Q_p(zeta_p) has i* = 1, D_m = 1 for
    every m; C_n = C_(n-1)(pi^(1/p)). Iterating SD3:
      D_m(C_n) = p^(m-1) D_1(C_(n-m+1))  for 2 <= m <= n + 1,
      D_m(C_n) = p^n = i*(C_n)           for m >= n + 2,
    so a radical tower's whole cutoff ladder is its floors' FIRST
    defects, one storey down per rung; x^18+3 reads 25, 21 = 3*7,
    9 = 9*1, 9, ... A nontrivial rung needs p^m | i*, else D_m = i*
    is forced by the class ladder (the arrival window of
    explore_cutoff_ladder.py CL2).

THE TRANSPLANT, marked: the first design of SD1 for the unit-root
storey read a digit-support set S (digits at positions == r mod p
free only from level i_r * l) transplanted from the radical case; the
triangular argument replaces it, S is everything mod pi_K^L, and the
unit-root storey descends by the same factor p. The prediction below
carries the corrected law; a print matching the transplant's smaller
value instead would falsify SD1 as corrected.

THE PREDICTIONS (frozen before the run; a printed defect ABOVE a
frozen value falsifies the law, one BELOW indicts the climb unless
the constructive witness of SD1 also sits below).

P1 (the positive control, x^18+3 over x^6+3 over Q3(zeta3)):
    D_1(E) = 1; D_1(C) = 7, D_2(C) = 3 (forced, 9 does not divide 3;
    = 3 * 1); D_1(K) = 25, D_2(K) = 21 = 3 * 7, D_3(K) = 9 (forced).
P2 (x^36+3 over x^12+3, 9 | i* = 18): D_1(x^12+3) = 14 (known);
    D_2(x^36+3) = 42 (fresh, nontrivial; clause 42 < 36 + 36);
    D_1(x^36+3) >= 36 and in the menu (18, 54) with 3 not dividing,
    or 54.
P3 (x^54+3 over x^18+3, 27 | i* = 27): D_2 = 3 * 25 = 75 (75 < 108),
    D_3 = 3 * 21 = 63 (63 < 162), both fresh and nontrivial;
    D_1 >= 54, in (27, 81) prime to 3, or 81.
P4 (p = 2, target -1, the tower x^2-2, x^4-2, x^8-2, x^16-2):
    D_m(Q2) = 1; D_1(x^2-2) = 3 (known), D_2 = 2 (forced);
    D_1(x^4-2) = 7 (known), D_2(x^4-2) = 6 (fresh, 6 < 8);
    x^8-2: D_1 >= 8 in {9, 11, 13, 15, 16}, D_2 = 14, D_3 = 12;
    x^16-2: D_1 >= 16, D_2 = 2 * D_1(x^8-2) if that is < 32 else
    >= 32, D_3 = 28, D_4 = 24. Also x^4+2 over x^2+2: D_2 = 6.
P5 (the unramified storey at m = 2): the f = 2 lift of x^18+3 has
    D_2 = 21 (21 != 27); the f = 2 lift of x^12+3 has D_1 = 14
    (14 != 18). Boundary control: the designed sextic [12, 0, 0, 3,
    6, 6, 1] has D_1 = 9 = p i* and its f = 3 lift climbs past 13.
P6 (unit-root storeys): K_4 = C((1 + pi_C^4)^(1/3)) over C = x^6+3,
    degree 18, L = 13, pi_K = (theta - 1)/pi_C; K_8 = C'((1 +
    pi_C^8)^(1/3)) over C' = x^12+3, degree 36, L = 23, pi_K =
    (theta - 1)^2/pi_C^5. D_2(K_4) = 21 (21 < 18 + 13), D_2(K_8) = 42
    (42 < 36 + 23); the constructive witness y = sum_j (a_j mod 3)
    pi_K^j from the C-witness c = sum_j a_j pi_C^j satisfies
    v_K(y^3 - c) >= L; D_1(K_l) in the menu, an observation, >= L.
P7 (the floor): D_1(K) >= L at every ramified storey censused.

FROZEN AFTER THE FIRST RUN PRINTED SECTIONS 1-4 AND DIED IN SECTION 5
(a climb with no good start), BEFORE SECTIONS 5-8 RAN. The prints
read 7, 25, 79 up the x^6+3 tower, 14, 50 up x^12+3, 3, 7, 15, 31 up
x^2-2: the first defect climbs by exactly e_K per radical storey, so
the break t = p i* - D_1 of K(zeta_(p^2))/K is invariant. HERBRAND
PROVES IT: for a storey K/C with break t_(K/C) and the cyclotomic
break t_C = p i*_C - D_1(C), and K not C(zeta_(p^2)) itself, the
compositum L = K(zeta_(p^2)) over C
is bicyclic with upper breaks {t_C, t_(K/C)}; Gal(L/K) meets
Gal(L/C(zeta_(p^2))) trivially, so its upper break is psi_(K/C)(t_C)
(G_K^psi(u) = G_K meet G_C^u, Herbrand's transitivity), which is t_C
itself when t_C < t_(K/C) and p t_C - (p-1) t_(K/C) when above. With
D_1 = p i* - t:
  D_1(K) = D_1(C) + e_K                     if l < D_1(C) (radical:
                                            t_(K/C) = p i*_C, always),
  D_1(K) = p D_1(C) + e_K - (p-1) l         if l > D_1(C),
the two agreeing at l = D_1(C). SD3 now has a first rung: the storey
adds e_K to D_1 and multiplies every higher D_m by p.
P8 (the first rung, fresh): x^18-6 over x^6-6 and x^18+3x^12+3 over
    x^6+3x^4+3 read D_1 = 7 + 18 = 25; x^8+2 over x^4+2 reads
    7 + 8 = 15; x^4-10 over x^2-10 reads 3 + 4 = 7; K_4 (l = 4 < 7)
    reads 25; K_8 (l = 8 < 14) reads 50.
P9 (the second branch): the e = 12 family x^12 + 3c, c == 1 mod 3
    (zeta_3 in C since -3c is -3 times a square), scanned for its D_1
    alphabet; over a member with D_1(C) = 7 the storey l = 8 (a = 2,
    b' = 5, L = 23) reads D_1(K) = 21 + 36 - 16 = 41, against 43 on
    the first branch, and D_2(K) = 21 = 3 * 7 by SD3. If no member
    reads 7, the rig says so and tests l = 8 at a member with D_1 = 8
    (both branches 44) or the first branch at one with D_1 > 8.

THE DESIGN. LF machinery of explore_local_clock; tclimb, sample_cls,
zeta3_el, menu_ok from explore_cutoff_ladder; embed(C -> K) is the
position map j -> pj at a radical storey and Horner in pi_C at a
unit-root storey, where pi_C = pi_K^3 rho with rho the e_C-th root of
w_K = -3/pi_K^e_K nearest 1 (every root of x^e_C + 3 in K_l lies in
C, K_l being totally ramified), extracted as square roots by Newton
and cube roots by Newton with exact coefficient division by 3 in a
high-precision copy of the field; the f-lift pads coefficients. Every D_m is
climbed twice: from random starts of class i*/p^m (the climb's own
reach) and from the constructive witness (SD1's preimage), the
witness's own v_K(y^(p^m) - zeta) printed as the lower bound that
needs no climb. The unit-root storeys' Eisenstein polynomials are
resultants (sympy) of the storey relation against x^e_C + 3, checked
Eisenstein. One process, well under 512MB; the first run's
sections 1-4 took 5 s, the e = 12 scan is the added cost (estimate
under 2 min). Run:
python prime/code/explore_storey_descent.py

FINDINGS (entered post-run, copied from printed output).

1. THE STOREY DESCENT HOLDS AT EVERY RUNG BUILT (theorem SD3, checked
   at thirteen rungs over p = 2, 3; the constructive witness of SD1
   reaches the law's value at every one, the seeded climb never
   exceeds it, and the random climb reaches it at every rung):
     x^18+3  over x^6+3      D_2 = 21 = 3 * 7    (y^p - c at 18 >= 18)
     x^36+3  over x^12+3     D_2 = 42 = 3 * 14   (38 >= 36)   fresh
     x^54+3  over x^18+3     D_2 = 75 = 3 * 25   (57 >= 54)   fresh
                             D_3 = 63 = 3 * 21   (55 >= 54)   fresh
     x^4-2   over x^2-2      D_2 =  6 = 2 * 3    ( 5 >=  4)   fresh
     x^8-2   over x^4-2      D_2 = 14 = 2 * 7,  D_3 = 12 = 2 * 6
     x^16-2  over x^8-2      D_2 = 30 = 2 * 15, D_3 = 28 = 2 * 14,
                             D_4 = 24 = 2 * 12
     x^4+2   over x^2+2      D_2 =  6 = 2 * 3
     K_4     over x^6+3      D_2 = 21 = 3 * 7    (13 >= L 13) unit-root
     K_8     over x^12+3     D_2 = 42 = 3 * 14   (26 >= L 23) unit-root
   The forced rungs read as forced (D_2(x^6+3) = 3 = i*, D_m(E) = 1,
   D_m(Q2) = 1). The collapse levels print at or above L everywhere,
   and at the unit-root storeys pi_C = pi_K^3 holds to exactly the
   derived level (13 at l = 4, 23 at l = 8).

2. THE FIRST RUNG (P8, frozen after the first run; theorem by
   Herbrand, first branch checked at thirteen storeys): D_1(K) = D_1(C) +
   e_K at every radical storey and both unit-root storeys:
     x^6+3 tower 7, 25, 79;  x^12+3 tower 14, 50;
     x^2-2 tower 3, 7, 15, 31;  x^2+2, x^4+2, x^8+2: 3, 7, 15;
     x^6-6 -> x^18-6: 7 -> 25;  x^6+3x^4+3 -> x^18+3x^12+3: 7 -> 25;
     x^2-10 -> x^4-10: 3 -> 7;  K_4: 25 = 7 + 18;  K_8: 50 = 14 + 36.
   So the break of K(zeta_(p^2))/K is invariant up every tower built
   (2 over x^6+3, 4 over x^12+3, 1 over Q2). THE SECOND BRANCH IS
   UNRUN: no member of x^12 + 3c, c == 1 mod 3, c < 3^5, reads below
   14 (the alphabet is the single value 14, an observation: this
   family's window defect sits at or beyond e_C), so no storey the
   rig can build (l < 3 e_C / 4, the Hensel margin of its root
   construction) has its break below the cyclotomic break; section 8
   rebuilt K_8 and read the first branch again (50, with the second
   branch's 62 excluded). Herbrand's prediction for the second branch
   stands as the open front.

3. THE UNRAMIFIED STOREY IS DEFECT-INVARIANT OFF THE BOUNDARY (SD4;
   rule at three lifts): the f = 2 lift of x^18+3 reads D_2 = 21
   (seeded 21, the random climb 21), the f = 2 lift of x^12+3 reads
   D_1 = 14 (seeded 14; the random climb stalled at 6 = i*, a start
   whose leading F_9-digit is off F_3 cannot be repaired by the
   climb's steps — the climb's reach, not the field's), and the
   boundary control moves: the designed sextic reads 9 = p i* and
   its f = 3 lift 16 >= 13.

4. THE CLIMB'S REACH (a rig fact): at every ramified rung the random
   climb (24-40 starts of class i*/p^m) reached the law's value
   unaided; the one stall was the unramified f = 2 lift at m = 1.
   The constructive witness makes the lower bound climb-free.

RUN RECORD (python explore_storey_descent.py under memwatch, 8.5 s,
exit 0): 343 checks passed; peak working set 63 MB. The first run
died in section 5 at the unseeded lift climb (D_1 read 6, finding 3);
sections 5-8 were then seeded with the C-witness and P8-P9 frozen
before rerunning. A pre-green failure: the resultant carries a
content (the norm of the relation's u-leading coefficient, 9 at K_4),
divided out before the Eisenstein check.
"""

import random
import time

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_cutoff_ladder as cl
import explore_tame_readout as tr

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def ct(F, n):
    return ad.const_el(F, n)


def epow(F, u, n):
    return cl.epow(F, u, n)


def phi_p_zero(F, z, p):
    """1 + z + ... + z^(p-1) vanishes: z a primitive p-th root."""
    s, pw = ct(F, 1), ct(F, 1)
    for _ in range(p - 1):
        pw = F.emul(pw, z)
        s = tuple(F.cadd(a, b) for a, b in zip(s, pw))
    return F.val(s) >= F.amax


# --------------------------------------------------------- embeddings


def embed_radical(C, K, A):
    """C -> K = C(pi_C^(1/p)): coefficient j of A at position p*j."""
    p = K.p
    ok(C.M >= K.M, "%s -> %s: C precision %d below K's %d"
       % (C.name, K.name, C.M, K.M))
    out = [list(K.zero_c) for _ in range(K.e)]
    for j, cj in enumerate(A):
        for l in range(K.f):
            out[p * j][l] = cj[l] % K.pM
    return tuple(tuple(c) for c in out)


def embed_lift(C, K, A):
    """C -> its unramified lift K (same eis, bigger g): pad."""
    ok(C.M >= K.M, "%s -> %s: C precision %d below K's %d"
       % (C.name, K.name, C.M, K.M))
    return tuple(tuple([cj[0] % K.pM] + [0] * (K.f - 1)) for cj in A)


def horner(K, coeffs, x):
    """sum_j coeffs[j] * x^j in K, coeffs ints."""
    acc = ct(K, 0)
    for a in reversed(coeffs):
        acc = tuple(K.cadd(c, d) for c, d in
                    zip(K.emul(acc, x), ct(K, a)))
    return acc


def embed_unit_root(C, K, piC, A):
    """C -> K_l with pi_C given as a K-element: Horner over the
    coefficients of A (f = 1)."""
    ok(C.f == 1 and K.f == 1, "unit-root embed: f = 1 only")
    return horner(K, [cj[0] for cj in A], piC)


def witness(C, K, c_el):
    """SD1's preimage: y = sum_j (a_j mod p) pi_K^j, f = 1."""
    ok(C.f == 1 and K.f == 1, "witness: f = 1 only")
    piK = tuple(tuple([1] if j == 1 else [0]) for j in range(K.e))
    return horner(K, [cj[0] % K.p for cj in c_el], piK)


# --------------------------------------------------------------- climbs


def climb_Dm(F, m, T_inv, cap, rng, seeds=(), n=40):
    """D_m = max_y v(y^(p^m) - zeta): tclimb at class i*/p^m, P = p^m.
    Returns (random-start stick, seeded stick) -- the seeded run
    starts from the given witnesses alone."""
    P = F.p ** m
    ok(F.seat % P == 0, "%s: p^%d does not divide i* = %d"
       % (F.name, m, F.seat))
    c = F.seat // P
    starts = list(cl.sample_cls(F, c, n, rng))
    _, s_rand = cl.tclimb(F, starts, c, P, T_inv, cap)
    s_seed = None
    if seeds:
        _, s_seed = cl.tclimb(F, list(seeds), c, P, T_inv, cap)
    return s_rand, s_seed


def defect_of(F, y, P, T_inv):
    """v(y^P * T_inv - 1) = v(y^P - zeta)."""
    return F.val(ad.esub(F, F.emul(epow(F, y, P), T_inv), ct(F, 1)))


def storey(C, K, embed, zC, m, D_prev, L, cap, rng, label):
    """One rung: predict D_m(K) = p * D_(m-1)(C) from the printed
    D_(m-1)(C), build the witness, climb both ways, print."""
    p = K.p
    P = p ** m
    zK = embed(zC)
    ok(phi_p_zero(K, zK, p), "%s: embedded zeta not primitive" % K.name)
    T_inv = epow(K, zK, p - 1)
    A = p * D_prev
    level = (m - 1) * K.e + L
    pred = A if A < level else None
    s_rand, s_seed = climb_Dm(K, m, T_inv, cap, rng)
    line = "  %-26s D_%d: climb %2d" % (label, m, s_rand)
    if pred is not None:
        ok(s_rand <= pred, "%s: D_%d climb %d ABOVE p*D_%d(C) = %d"
           % (K.name, m, s_rand, m - 1, pred))
        line += "  law %2d = %d * %2d  (clause %d < %d)" % (
            pred, p, D_prev, A, level)
    else:
        line += "  law >= %d (clause fails: %d >= %d)" % (level, A, level)
        ok(s_rand >= level, "%s: D_%d %d below the floor %d"
           % (K.name, m, s_rand, level))
    print(line)
    return s_rand, pred


def storey_with_witness(C, K, embed, zC, cC, m, D_prev, L, cap, rng,
                        label):
    """The radical / unit-root rung with SD1's constructive witness:
    v(y^p - c) >= L printed, v(y^(p^m) - zeta) >= min(level, p*D)."""
    p = K.p
    P = p ** m
    zK = embed(zC)
    ok(phi_p_zero(K, zK, p), "%s: embedded zeta not primitive" % K.name)
    T_inv = epow(K, zK, p - 1)
    cK = embed(cC)
    y = witness(C, K, cC)
    coll = K.val(ad.esub(K, epow(K, y, p), cK))
    ok(coll >= L, "%s: witness y^p - c at %d < L = %d" % (K.name, coll, L))
    wv = defect_of(K, y, P, T_inv)
    A = p * D_prev
    level = (m - 1) * K.e + L
    pred = A if A < level else None
    ok(wv >= min(A, level), "%s: witness defect %d < min(%d, %d)"
       % (K.name, wv, A, level))
    s_rand, s_seed = climb_Dm(K, m, T_inv, cap, rng, seeds=[y])
    line = ("  %-26s D_%d: climb %2d  seeded %2d  witness %2d"
            " (y^p-c at %2d >= L %2d)" % (label, m, s_rand, s_seed, wv,
                                          coll, L))
    if pred is not None:
        ok(s_seed <= pred, "%s: D_%d seeded climb %d ABOVE law %d"
           % (K.name, m, s_seed, pred))
        ok(s_rand <= pred, "%s: D_%d climb %d ABOVE law %d"
           % (K.name, m, s_rand, pred))
        ok(wv == pred, "%s: D_%d witness %d != law %d (the lower bound"
           " is exact by SD3; a miss is the witness's)"
           % (K.name, m, wv, pred))
        line += "  law %2d = %d * %2d" % (pred, p, D_prev)
    else:
        line += "  law >= %d" % level
    print(line)
    return max(s_rand, s_seed, wv), pred


def first_defect(F, T_inv, cap, rng, L, label, n=40):
    """D_1 by the class-i*/p climb, menu-checked, floor L checked."""
    d, _ = climb_Dm(F, 1, T_inv, cap, rng, n=n)
    cl.menu_ok(F, d, F.name)
    ok(d >= L, "%s: D_1 %d below the floor L = %d" % (F.name, d, L))
    print("  %-26s D_1: %2d  (menu (%d, %d) or %d; floor L = %d)"
          % (label, d, F.seat, F.p * F.seat, F.p * F.seat, L))
    return d


# ------------------------------------------------------------------ run


def run():
    rng = random.Random(1200)
    t0 = time.time()
    print("THE STOREY DESCENT -- D_m(K) = p * D_(m-1)(C) down a storey")
    print("=" * 68)

    # ---------------- [1] p = 3: the positive control tower, P1
    print("\n[1] x^18+3 over x^6+3 over Q3(zeta3): the control tower")
    E = lc.LF("Q3(zeta3)", 3, [0, 1], [3, 3, 1], 12)
    zE = tuple(((1,), (1,)))                               # x + 1
    dE = max(E.val(ad.esub(E, epow(E, y, 3), zE)) for y in E.units())
    ok(dE == 1, "E: D_1 %d != 1" % dE)
    print("  %-26s D_1: %2d  (i* = 1, 3 does not divide: forced)"
          % ("Q3(zeta3)", dE))
    C6 = lc.LF("x^6+3", 3, [0, 1], [3, 0, 0, 0, 0, 0, 1], 20)
    z6 = cl.zeta3_el(C6)
    T6 = epow(C6, z6, 2)
    d6 = first_defect(C6, T6, 11, rng, L=6, label="x^6+3 (C)")
    ok(d6 == 7, "C: D_1 %d != 7" % d6)
    # D_2(C) is forced at i* = 3 (9 does not divide 3): check the
    # forced value directly on the class-1 units' 9th powers
    d6_2 = max(defect_of(C6, y, 9, T6)
               for y in cl.sample_cls(C6, 1, 60, rng))
    ok(d6_2 == 3, "C: D_2 %d != 3 = i* (forced)" % d6_2)
    print("  %-26s D_2: %2d  (forced = i*; = 3 * D_1(E) = 3)"
          % ("x^6+3 (C)", d6_2))
    K18 = lc.LF("x^18+3", 3, [0, 1], [3] + [0] * 17 + [1], 48)
    emb = lambda A: embed_radical(C6, K18, A)
    z18 = emb(z6)
    T18 = epow(K18, z18, 2)
    d18 = first_defect(K18, T18, 29, rng, L=18, label="x^18+3 (K)")
    ok(d18 == 25, "K: D_1 %d != 25" % d18)
    # the C-witness for D_1(C): a class-1 unit with v(y^3 - zeta) = 7
    cC = None
    for y in cl.sample_cls(C6, 1, 400, rng):
        if defect_of(C6, y, 3, T6) == 7:
            cC = y
            break
    if cC is None:
        # climb to it: tclimb returns sticks, not elements; rebuild by
        # a small greedy on the element
        cC = greedy_element(C6, 1, 3, T6, 7, rng)
    ok(cC is not None and defect_of(C6, cC, 3, T6) == 7,
       "C: no D_1 witness found")
    D2, pred = storey_with_witness(C6, K18, emb, z6, cC, 2, d6, 18, 23,
                                   rng, "x^18+3 over x^6+3")
    ok(D2 == 21 and pred == 21, "K: D_2 %d, law %s != 21" % (D2, pred))
    print("  [%.0f s]" % (time.time() - t0))

    # ---------------- [2] x^36+3 over x^12+3, P2
    print("\n[2] x^36+3 over x^12+3: the first fresh nontrivial rung")
    C12 = lc.LF("x^12+3", 3, [0, 1], [3] + [0] * 11 + [1], 40)
    z12 = cl.zeta3_el(C12)
    T12 = epow(C12, z12, 2)
    d12 = first_defect(C12, T12, 20, rng, L=12, label="x^12+3 (C)")
    ok(d12 == 14, "x^12+3: D_1 %d != 14" % d12)
    c12 = greedy_element(C12, 2, 3, T12, d12, rng)
    K36 = lc.LF("x^36+3", 3, [0, 1], [3] + [0] * 35 + [1], 58)
    emb = lambda A: embed_radical(C12, K36, A)
    z36 = emb(z12)
    T36 = epow(K36, z36, 2)
    d36 = first_defect(K36, T36, 56, rng, L=36, label="x^36+3 (K)")
    D2_36, pred = storey_with_witness(C12, K36, emb, z12, c12, 2, d12, 36,
                                      46, rng, "x^36+3 over x^12+3")
    print("  [%.0f s]" % (time.time() - t0))

    # ---------------- [3] x^54+3 over x^18+3, P3
    print("\n[3] x^54+3 over x^18+3: two fresh rungs, D_2 and D_3")
    c18 = greedy_element(K18, 3, 3, T18, d18, rng)         # D_1 witness
    c18_2 = greedy_element(K18, 1, 9, T18, 21, rng)        # D_2 witness
    K54 = lc.LF("x^54+3", 3, [0, 1], [3] + [0] * 53 + [1], 84)
    emb = lambda A: embed_radical(K18, K54, A)
    z54 = emb(z18)
    T54 = epow(K54, z54, 2)
    d54 = first_defect(K54, T54, 83, rng, L=54, label="x^54+3 (K)", n=24)
    D2_54, p2 = storey_with_witness(K18, K54, emb, z18, c18, 2, d18, 54,
                                    79, rng, "x^54+3 over x^18+3")
    D3_54, p3 = storey_with_witness(K18, K54, emb, z18, c18_2, 3, 21, 54,
                                    67, rng, "x^54+3 over x^18+3")
    print("  [%.0f s]" % (time.time() - t0))

    # ---------------- [4] p = 2: the radical tower over Q2, P4
    print("\n[4] p = 2: x^2-2, x^4-2, x^8-2, x^16-2 (target -1)")
    Q2 = lc.LF("Q2", 2, [0, 1], [2, 1], 8)
    dQ = max(Q2.val(ad.esub(Q2, epow(Q2, y, 4), ct(Q2, -1)))
             for y in Q2.units())
    ok(dQ == 1, "Q2: D_2 %d != 1" % dQ)
    print("  %-26s D_m: %2d  (i* = 1: forced)" % ("Q2", dQ))
    tower = [("x^2-2", [-2, 0, 1], 2), ("x^4-2", [-2, 0, 0, 0, 1], 4),
             ("x^8-2", [-2] + [0] * 7 + [1], 8),
             ("x^16-2", [-2] + [0] * 15 + [1], 16)]
    prev = None                     # (F, {m: (D_m, witness element)})
    for name, eis, e in tower:
        F = lc.LF(name, 2, [0, 1], eis, 2 * e + 6)
        Tm1 = ct(F, -1)
        ladder = {}
        d1 = first_defect(F, Tm1, 2 * e + 2, rng, L=e, label=name)
        ladder[1] = (d1, greedy_element(F, e // 2, 2, Tm1, d1, rng)
                     if d1 < F.CAP else None)
        if prev is not None:
            Cf, Cl = prev
            emb = lambda A, Cf=Cf, F=F: embed_radical(Cf, F, A)
            m = 2
            while m <= len(Cl) + 1 and F.seat % (2 ** m) == 0:
                Dp, cw = Cl[m - 1]
                if cw is None:
                    break
                Dm, pred = storey_with_witness(
                    Cf, F, emb, ct(Cf, -1), cw, m, Dp, e, 2 * e + 2, rng,
                    "%s over %s" % (name, Cf.name))
                ladder[m] = (Dm, greedy_element(F, F.seat // 2 ** m,
                                                2 ** m, Tm1, Dm, rng))
                m += 1
        prev = (F, ladder)
    # the minus tower: x^4+2 over x^2+2
    Cm = lc.LF("x^2+2", 2, [0, 1], [2, 0, 1], 10)
    dm1 = first_defect(Cm, ct(Cm, -1), 6, rng, L=2, label="x^2+2")
    cw = greedy_element(Cm, 1, 2, ct(Cm, -1), dm1, rng)
    Km = lc.LF("x^4+2", 2, [0, 1], [2, 0, 0, 0, 1], 14)
    first_defect(Km, ct(Km, -1), 10, rng, L=4, label="x^4+2")
    storey_with_witness(Cm, Km, lambda A: embed_radical(Cm, Km, A),
                        ct(Cm, -1), cw, 2, dm1, 4, 10, rng,
                        "x^4+2 over x^2+2")
    print("  [%.0f s]" % (time.time() - t0))

    # ---------------- [5] the unramified storey, P5
    print("\n[5] unramified lifts: f = 2 of x^18+3 (m = 2), of x^12+3"
          " (m = 1); the boundary control")
    g2 = [1, 0, 1]                                          # x^2 + 1
    K18f2 = lc.LF("x^18+3 f2", 3, g2, [3] + [0] * 17 + [1], 30)
    z = embed_lift(K18, K18f2, z18)
    ok(phi_p_zero(K18f2, z, 3), "x^18+3 f2: zeta not primitive")
    Tl = epow(K18f2, z, 2)
    s_rand, s_seed = climb_Dm(K18f2, 2, Tl, 24, rng, n=24,
                              seeds=[embed_lift(K18, K18f2, c18_2)])
    ok(s_seed == 21 and s_rand <= 21, "x^18+3 f2: D_2 climb %d seeded"
       " %d != 21 = D_2(C) (unramified storey moved a non-boundary"
       " value)" % (s_rand, s_seed))
    print("  %-26s D_2: climb %2d  seeded %2d  law %2d = D_2(x^18+3)"
          " (21 != 27)" % ("x^18+3, f = 2 lift", s_rand, s_seed, 21))
    K12f2 = lc.LF("x^12+3 f2", 3, g2, [3] + [0] * 11 + [1], 22)
    z = embed_lift(C12, K12f2, z12)
    ok(phi_p_zero(K12f2, z, 3), "x^12+3 f2: zeta not primitive")
    Tl = epow(K12f2, z, 2)
    s_rand, s_seed = climb_Dm(K12f2, 1, Tl, 20, rng, n=24,
                              seeds=[embed_lift(C12, K12f2, c12)])
    ok(s_seed == 14 and s_rand <= 14, "x^12+3 f2: D_1 climb %d seeded"
       " %d != 14" % (s_rand, s_seed))
    print("  %-26s D_1: climb %2d  seeded %2d  law %2d = D_1(x^12+3)"
          " (14 != 18)" % ("x^12+3, f = 2 lift", s_rand, s_seed, 14))
    # boundary control: the designed sextic, D_1 = 9 = p i*, lift splits
    eis_u = [12, 0, 0, 3, 6, 6, 1]
    U = lc.LF("designed", 3, [0, 1], eis_u, 18)
    zU = cl.zeta3_el(U)
    dU = climb_Dm(U, 1, epow(U, zU, 2), 12, rng)[0]
    ok(dU == 9, "designed: D_1 %d != 9 = p i*" % dU)
    cU = greedy_element(U, 1, 3, epow(U, zU, 2), 9, rng)
    U3 = lc.LF("designed f3", 3, [1, 2, 0, 1], eis_u, 18)
    zU3 = embed_lift(U, U3, zU)
    dU3 = max(climb_Dm(U3, 1, epow(U3, zU3, 2), 16, rng, n=24,
                       seeds=[embed_lift(U, U3, cU)]))
    ok(dU3 >= 13, "designed f3: D_1 %d < 13 (boundary did not move)"
       % dU3)
    print("  %-26s D_1: %2d = p i*;  f = 3 lift: %2d >= 13 (the boundary"
          " value moves, and only it)" % ("designed sextic", dU, dU3))
    print("  [%.0f s]" % (time.time() - t0))

    # ---------------- [6] unit-root storeys, P6
    print("\n[6] unit-root storeys: K_4 over x^6+3 (L = 13), K_8 over"
          " x^12+3 (L = 23)")
    import sympy as sp
    t, u = sp.symbols("t u")
    cases = [(4, C6, z6, cC, d6, 6, 3 * u + 3 * t * u ** 2 + t ** 2 * u ** 3
              - t ** 3, 13, 31, 23),
             (8, C12, z12, c12, d12, 12, t ** 5 * (t ** 3 - 3 * u) ** 2
              - u * (t ** 5 * u + 3) ** 2, 23, 60, 46)]
    for l, Cf, zC, cw, dC, eC, rel, L, amax_lo, cap in cases:
        res = sp.Poly(sp.resultant(t ** eC + 3, rel, t), u)
        coeffs = [int(c) for c in reversed(res.all_coeffs())]   # low->high
        lead = coeffs[-1]                     # the norm of the u-leading
        ok(all(c % lead == 0 for c in coeffs), "K_%d: content" % l)
        coeffs = [c // lead for c in coeffs]  # coefficient: a power of 3
        eK = 3 * eC
        ok(coeffs[-1] == 1 and len(coeffs) == eK + 1,
           "K_%d: degree %d / lead %d" % (l, len(coeffs) - 1, coeffs[-1]))
        ok(all(c % 3 == 0 for c in coeffs[:-1]) and coeffs[0] % 9 != 0,
           "K_%d: not Eisenstein" % l)
        Khi = lc.LF("K_%d hi" % l, 3, [0, 1], coeffs, eK * 8)
        w, piK = tr.w_element(Khi)
        rho = root_1unit(Khi, w, eC)
        piC = Khi.emul(epow(Khi, piK, 3), rho)
        chk = Khi.val(ad.esub(Khi, epow(Khi, piC, eC), ct(Khi, -3)))
        ok(chk >= 4 * eK, "K_%d: pi_C^%d + 3 at level %d only" % (l, eC, chk))
        Kl = lc.LF("K_%d" % l, 3, [0, 1], coeffs, amax_lo)
        piC = tuple(tuple(x % Kl.pM for x in c) for c in piC)
        piK = tuple(tuple(x % Kl.pM for x in c) for c in piK)
        near = Kl.val(ad.esub(Kl, piC, epow(Kl, piK, 3)))
        print("  K_%d: Eisenstein degree %d; pi_C = pi_K^3 to level %d"
              % (l, eK, near))
        emb = lambda A, Kl=Kl, piC=piC, Cf=Cf: embed_unit_root(Cf, Kl, piC, A)
        zl = emb(zC)
        Tl = epow(Kl, zl, 2)
        d1 = first_defect(Kl, Tl, 3 * Kl.seat + 2, rng, L=L,
                          label="K_%d" % l, n=24)
        ok(l < dC and d1 == dC + eK, "K_%d: D_1 %d != D_1(C) + e_K = %d"
           " (first branch, l = %d < %d)" % (l, d1, dC + eK, l, dC))
        print("  %-26s      first rung: %d = %d + %d (l = %d < D_1(C))"
              % ("", d1, dC, eK, l))
        storey_with_witness(Cf, Kl, emb, zC, cw, 2, dC, L, cap, rng,
                            "K_%d over %s" % (l, Cf.name))
    print("  [%.0f s]" % (time.time() - t0))

    # ---------------- [7] the first rung at fresh radical storeys, P8
    print("\n[7] the first rung D_1(K) = D_1(C) + e_K: the towers above,"
          " and fresh siblings")
    ok(d18 == d6 + 18 and d54 == d18 + 54, "x^6+3 tower: 7, 25, 79 break")
    ok(d36 == d12 + 36, "x^12+3 tower: 14, 50 break")
    print("  x^6+3 tower %d, %d, %d; x^12+3 tower %d, %d; x^2-2 tower"
          " (asserted below)" % (d6, d18, d54, d12, d36))
    sibs = [(3, "x^6-6", [-6, 0, 0, 0, 0, 0, 1], "x^18-6",
             [-6] + [0] * 17 + [1]),
            (3, "x^6+3x^4+3", [3, 0, 0, 0, 3, 0, 1], "x^18+3x^12+3",
             [3] + [0] * 11 + [3] + [0] * 5 + [1]),
            (2, "x^4+2", [2, 0, 0, 0, 1], "x^8+2", [2] + [0] * 7 + [1]),
            (2, "x^2-10", [-10, 0, 1], "x^4-10", [-10, 0, 0, 0, 1])]
    for pp, cn, ceis, kn, keis in sibs:
        eC, eK = len(ceis) - 1, len(keis) - 1
        Cs = lc.LF(cn, pp, [0, 1], ceis, 2 * pp * (eC // (pp - 1)) + 6)
        Ks = lc.LF(kn, pp, [0, 1], keis, pp * (eK // (pp - 1)) + 4)
        if pp == 3:
            zc = cl.zeta3_el(Cs)
            Tc, Tk = epow(Cs, zc, 2), epow(Ks, embed_radical(Cs, Ks, zc), 2)
        else:
            Tc, Tk = ct(Cs, -1), ct(Ks, -1)
        dc = first_defect(Cs, Tc, pp * Cs.seat + 2, rng, L=eC, label=cn)
        dk = first_defect(Ks, Tk, pp * Ks.seat + 2, rng, L=eK, label=kn)
        ok(dk == dc + eK, "%s over %s: D_1 %d != %d + %d" % (kn, cn, dk, dc,
                                                            eK))
        print("  %-26s first rung: %d = %d + %d" % (kn + " over " + cn, dk,
                                                    dc, eK))
    print("  [%.0f s]" % (time.time() - t0))

    # ---------------- [8] the e = 12 alphabet and the second branch, P9
    print("\n[8] x^12 + 3c, c == 1 mod 3: the D_1 alphabet; the l = 8"
          " storey over a D_1 = 7 member")
    alphabet = {}
    for c in range(1, 3 ** 5, 3):
        Cc = lc.LF("x^12+%d" % (3 * c), 3, [0, 1],
                   [3 * c] + [0] * 11 + [1], 22)
        zc = cl.zeta3_el(Cc)
        dc = climb_Dm(Cc, 1, epow(Cc, zc, 2), 20, rng, n=24)[0]
        cl.menu_ok(Cc, dc, Cc.name)
        alphabet.setdefault(dc, []).append(c)
    print("  alphabet: " + ", ".join("D_1 = %d at c in %s%s" % (
        d, alphabet[d][:6], "..." if len(alphabet[d]) > 6 else "")
        for d in sorted(alphabet)))
    pick = None
    for want in (7, 8, 10, 11, 13, 14, 16, 17):
        if want in alphabet:
            pick = (want, alphabet[want][0])
            break
    ok(pick is not None, "e = 12: no finite D_1 in the family")
    dC, c = pick
    branch = "second (l = 8 > D_1 = 7)" if dC == 7 else (
        "boundary (l = 8 = D_1)" if dC == 8 else "first (l = 8 < D_1)")
    print("  member x^12+%d, D_1(C) = %d: testing the %s branch"
          % (3 * c, dC, branch))
    Cc = lc.LF("x^12+%d" % (3 * c), 3, [0, 1], [3 * c] + [0] * 11 + [1], 40)
    zc = cl.zeta3_el(Cc)
    Tc = epow(Cc, zc, 2)
    dc = first_defect(Cc, Tc, 20, rng, L=12, label=Cc.name)
    ok(dc == dC, "member: D_1 %d != %d at the wider window" % (dc, dC))
    cw = greedy_element(Cc, 2, 3, Tc, dc, rng)
    l, a, bp = 8, 2, 5
    rel = t ** bp * (t ** (l - bp) - 3 * u) ** 2 - u * (u * t ** bp + 3) ** 2
    res = sp.Poly(sp.resultant(t ** 12 + 3 * c, rel, t), u)
    coeffs = [int(x) for x in reversed(res.all_coeffs())]
    lead = coeffs[-1]
    ok(all(x % lead == 0 for x in coeffs), "K over x^12+%d: content" % (3 * c))
    coeffs = [x // lead for x in coeffs]
    ok(coeffs[-1] == 1 and len(coeffs) == 37 and coeffs[0] % 9 != 0
       and all(x % 3 == 0 for x in coeffs[:-1]), "K over x^12+%d: not"
       " Eisenstein of degree 36" % (3 * c))
    Khi = lc.LF("K hi", 3, [0, 1], coeffs, 36 * 8)
    w, piK = tr.w_element(Khi)
    rho = root_1unit(Khi, Khi.emul(w, ct(Khi, c)), 12)
    piC = Khi.emul(epow(Khi, piK, 3), rho)
    chk = Khi.val(ad.esub(Khi, epow(Khi, piC, 12), ct(Khi, -3 * c)))
    ok(chk >= 4 * 36, "K: pi_C^12 + 3c at level %d only" % chk)
    Kc = lc.LF("K(l=8) over x^12+%d" % (3 * c), 3, [0, 1], coeffs, 60)
    piC = tuple(tuple(x % Kc.pM for x in cc) for cc in piC)
    emb = lambda A, Kc=Kc, piC=piC, Cc=Cc: embed_unit_root(Cc, Kc, piC, A)
    Tk = epow(Kc, emb(zc), 2)
    L = min(36, 36 + 3 - 2 * l)
    dk = first_defect(Kc, Tk, 3 * Kc.seat + 2, rng, L=L, label=Kc.name,
                      n=24)
    first = dc + 36
    second = 3 * dc + 36 - 2 * l
    law = first if l < dc else second
    ok(dk == law, "K: D_1 %d != %d (%s branch; other branch %d)"
       % (dk, law, branch, second if l < dc else first))
    print("  %-26s first rung: %d = law %d (%s; the other branch would"
          " read %d)" % (Kc.name, dk, law, branch, second if l < dc else first))
    storey_with_witness(Cc, Kc, emb, zc, cw, 2, dc, L, 3 * dc + 2, rng,
                        "K(l=8) over x^12+%d" % (3 * c))
    print("  [%.0f s]" % (time.time() - t0))

    print("\n%d checks passed  [%.0f s]" % (CHECKS, time.time() - t0))


# ------------------------------------------------ element-level helpers


def greedy_element(F, c, P, T_inv, target, rng, n=60):
    """A class-c unit y with v(y^P - zeta) == target, by the same greedy
    ascent as tclimb but returning the element. None if unreached."""
    steps = []
    for k in range(c + 1, F.amax):
        i, j = divmod(k, F.e)
        for r in cl.residues(F):
            s = [list(cc) for cc in F.one]
            for l in range(F.f):
                s[j][l] = (s[j][l] + r[l] * (F.p ** i)) % F.pM
            steps.append(tuple(tuple(cc) for cc in s))

    def obj(y):
        return defect_of(F, y, P, T_inv)

    best_y, best_v = None, -1
    for y in cl.sample_cls(F, c, n, rng):
        v = obj(y)
        if v > best_v:
            best_y, best_v = y, v
    y, v = best_y, best_v
    while v < target:
        nxt = None
        for s in steps:
            y2 = F.emul(y, s)
            w = obj(y2)
            if w > v and (nxt is None or w < nxt[0]):
                nxt = (w, y2)
        if nxt is None:
            break
        v, y = nxt
    ok(v == target, "%s: greedy element reached %d, wanted %d"
       % (F.name, v, target))
    return y


def div3(K, A):
    """A / 3 for an element with every coefficient divisible by 3
    (v(A) >= e); costs one coefficient digit of precision."""
    out = []
    for c in A:
        assert all(x % 3 == 0 for x in c), "div3: inexact"
        out.append(tuple((x // 3) % K.pM for x in c))
    return tuple(out)


def root_1unit(K, A, n):
    """The n-th root of the 1-unit A nearest 1, n = 2^a 3^b: square
    roots by Newton (explore_tame_readout.newton_sqrt_el), cube roots
    by Newton on (1+s)^3 = A from s_0 = (A-1)/3, valid when
    v(A - 1) > p i*_K (the cube map is a bijection U_j -> U_(j+e) for
    j > i*_K). Trusted to K's precision less the divisions taken."""
    B = A
    while n % 2 == 0:
        B = tr.newton_sqrt_el(K, B)
        n //= 2
    while n % 3 == 0:
        a = ad.esub(K, B, ct(K, 1))
        ok(K.val(a) > K.p * K.seat, "%s: cube root below the Hensel"
           " margin (level %d)" % (K.name, K.val(a)))
        s = div3(K, a)
        for _ in range(4):
            one_s = tuple(K.cadd(c, d) for c, d in zip(ct(K, 1), s))
            f = ad.esub(K, epow(K, one_s, 3), B)
            if K.val(f) >= K.amax:
                break
            inv = tr.unit_inv(K, K.emul(one_s, one_s))
            s = ad.esub(K, s, K.emul(div3(K, f), inv))
        B = tuple(K.cadd(c, d) for c, d in zip(ct(K, 1), s))
        n //= 3
    ok(n == 1, "root_1unit: order not 2^a 3^b")
    return B


if __name__ == "__main__":
    run()
