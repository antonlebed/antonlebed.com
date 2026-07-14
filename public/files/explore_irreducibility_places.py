"""IRREDUCIBILITY CLOCKS READ THE PLACE — the finite-place spectrum of beta_col.

VERTIGO STOCK (a) generalization, P166. P165 found ONE interior irreducibility
critical clock: the depth 3-column's beta_col ~ 1.4959
(explore_irreducibility_order.py). The structural law said an interior critical
point exists iff the fate's normalizer keeps a nonzero infinite-depth limit --
which happens exactly when the tower RE-IMPORTS a place (depth = one returned
ultrametric ruler; breadth deletes all -> clocks pile at the zeta pole). This
script asks the sharper question: does the critical clock READ the place? Every
finite place (every lock prime q) carries its own depth column q^a and its own
interior beta_col^q. Is {beta_col^q} a thermodynamic shadow of the finite places
of Q -- Ostrowski read as temperature?

THE OBJECT. Depth column locks prime q, state q^a, lambda(q^a)=(q-1)q^(a-1). The
thermal D-DYN normalizer is the WALL DISCOUNT (explore_depth_observer.py finding
1): Z_{q^a}(beta) = zeta - 1 - [cofactor_sum - 1], cofactor = W(lambda(q^a))/q^a.
In the a->infinity limit the cofactor converges to a place-specific constant:
  odd q: cofactor = 2^(v2(q-1)+2) * prod_{odd p != q, p-1 | (q-1)q^inf} p^(vp(q-1)+1)
  q=2  : cofactor =                prod_{odd p, p-1 | 2^inf} p          (Fermat primes;
                                   the 2-column CANCELS its own 2-part base)
where p-1 | (q-1)q^inf  <=>  p = d*q^i + 1, d | (q-1), i >= 0. So the transparent
primes visible to the q-column read q's multiplicative arithmetic (v2(q-1),
q mod 3 via 7, q mod 4 via 5, ...). beta_col^q = interior root of Z_col^q = 1,
i.e. cofactor_sum(beta) = zeta(beta) - 1.

FINDINGS (tiers per section; run record at bottom).

S1 THE FINITE-PLACE FAMILY LIVES, IN A BOUNDED WINDOW (observation; closed form
cross-checked vs the general brute cofactor machinery). Every lock prime q gives
an interior beta_col^q in (1, beta*), beta* the root of zeta=2 (~1.729): the
cofactor sum falls [~2-3]->1 while zeta-1 falls inf->0, one crossing, always
above 1 and below beta*. beta_col^q is NOT universal -- it varies with q (PR1):
the clock reads the PLACE, not just the fate.

S2 THE CLOCK DECREASES WITH TRANSPARENT RICHNESS, AND THE RICHNESS IS RESIDUE
DATA (observation). More small transparent primes -> larger cofactor sum ->
crossing at SMALLER beta. The transparent set reads q's residues: 2 always;
3 for every odd q != 3 (q=3 uniquely blind, its own column prime); 5 iff
q = 1 mod 4; 7 iff q = 1 mod 3 OR q = 3 (the column's own powers supply the
3-part of 7-1=6: 6 | 2*3^inf -- the i >= 1 route p = d*q^i + 1 that the
residue shorthand elides). So beta_col^q is FIXED BY the transparent set
{p : p-1 | (q-1)q^inf} (the root of cofactor_sum = zeta-1), and coarse residue
classes order the clock:
median(beta_col | q=1 mod4) < median(q=3 mod4).

S3 THE 2-ADIC SEAT. The endpoints name themselves. beta_col^2 is the MAXIMUM of
the spectrum (over the tested family; the mechanism argues global): the 2-column
cancels its own 2-part base and sees only the
Fermat primes, so it is the LEAST rich column -- the 2-adic place (the tower's
default lock, the universal rudder's target, the returned ultrametric ruler)
sits at the top of the irreducibility temperature. Among odd q, q=3 is the max
(uniquely blind to the small prime 3). The critical temperature of computational
irreducibility is a valuation-theoretic invariant: it reads which place returned.

Run: `python explore_irreducibility_places.py`. Predictions frozen in SCRATCH.md
(P166) BEFORE the run (PR3/PR4 direction corrected by a pre-run hand attack --
richness LOWERS beta_col; q=2 tops the spectrum); asserts adjudicate; printed
values read against the hand law. RUN RECORD (76 checks pass, ~1 s):
beta* (zeta=2) = 1.72865; spread = 0.2869 (not universal, PR1). The spectrum
beta_col^q: 2:1.6045, 3:1.4959, 5:1.4206, 7:1.4234, 11:1.4367, 13:1.3409,
17:1.3881, 19:1.3935, 23:1.4399, 29:1.3902 -- beta_col^3 = 1.49595 reproduces
explore_irreducibility_order.py's beta_col EXACTLY by the general q-column
machinery (independent cross-validation). Closed-form cofactor cross-checked vs
brute cofactor_divisors on N=q^6 (q=2,3,5,7,11). S2: transparent rules verified
(2 all; 3 all odd q!=3; 5 iff q=1 mod4; 7 iff q=1 mod3 or q=3); median beta_col q=1
mod4 = 1.3881 < q=3 mod4 = 1.4234 (beta_col DECREASES with richness, PR4
corrected). S3: q=2 Fermat set = {3,5,17,257,65537}; beta_col^2 = 1.60449 is the
spectrum MAX (Fermat-only, no 2-base -- least rich; the mechanism argues global
but only the tested family is checked), beta_col^3 = 1.49595 the odd max
(self-blind to 3), 2>3>rest
(rest <= 1.4417, PR3 corrected). Self-blindness refinement caught by the S2
assert (q blind to its own prime -- residue rules hold for p != q; q=5 blind to
5 tripped the first run, expected physics).
"""

import sys, os, math
from math import log

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_depth_observer import (  # lineage: the general wall machinery
    is_prime, factorize, W_of_L, cofactor_divisors, lam_of, dict_to_int, lam_int,
)

CHECKS = 0

def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1

# ---------------------------------------------------------------- zeta (hp)
# Euler-Maclaurin tail (as in explore_irreducibility_order.py): error
# O(M^{-beta-3}). beta_col^q lives near ~1.5; the roots are well separated so no
# cross-cancellation wall (unlike the order.py clock GAP) -- direct bisection.
_ZHP = {}

def zeta_hp(beta, M=20000):
    if beta not in _ZHP:
        s = sum(n ** -beta for n in range(1, M + 1))
        tail = (M ** (1 - beta) / (beta - 1)
                - 0.5 * M ** -beta
                + beta / 12.0 * M ** (-beta - 1))
        _ZHP[beta] = s + tail
    return _ZHP[beta]

# ---------------------------------------------- the q-column cofactor (limit)

def v_p(n, p):
    """p-adic valuation of n."""
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e

def transparent_primes(q, i_max, CAP=10 ** 15):
    """Odd primes p != q with p-1 | (q-1)q^inf, capped: p = d*q^i + 1 for
    d | (q-1), 0 <= i <= i_max, p < CAP. Returns {p: exponent = vp(q-1)+1}.
    Matches W(lambda(q^a))/q^a's odd part with a = i_max+1 (p-1 | (q-1)q^(a-1))."""
    qm1 = q - 1
    # divisors of q-1
    fd = factorize(qm1)
    divs = [1]
    for r, e in fd.items():
        divs = [d * r ** j for d in divs for j in range(e + 1)]
    out = {}
    for d in divs:
        val = d
        i = 0
        while i <= i_max and val < CAP:
            p = val + 1
            if p > 2 and p != q and is_prime(p):
                out[p] = v_p(qm1, p) + 1
            val *= q
            i += 1
    return out

def cofactor_sum(q, beta, i_max=200, CAP=10 ** 15):
    """Product-form divisor sum of the q-column cofactor W(lambda(q^inf))/q^inf.
    odd q: 2-part 2^(v2(q-1)+2) times odd transparent primes.
    q=2: the 2-part cancels (the column IS the 2-column) -- Fermat primes only."""
    if q == 2:
        s = 1.0
    else:
        e2 = v_p(q - 1, 2) + 2
        s = sum(2.0 ** (-i * beta) for i in range(e2 + 1))  # 1 + 2^-b + ... + 2^-e2 b
    for p, e in transparent_primes(q, i_max, CAP).items():
        s *= sum(p ** (-i * beta) for i in range(e + 1))
    return s

def Z_col_q(q, beta):
    """Z_col^q(beta) = zeta - cofactor_sum (= zeta - 1 - T_col^q)."""
    return zeta_hp(beta) - cofactor_sum(q, beta)

def bisect_root(f, lo, hi, tol=1e-13):
    flo, fhi = f(lo), f(hi)
    assert flo > 0 > fhi, f"bracket not straddling: f({lo})={flo}, f({hi})={fhi}"
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)

def beta_col(q):
    """Interior root of Z_col^q = 1, i.e. cofactor_sum(q,beta) = zeta(beta)-1."""
    return bisect_root(lambda b: Z_col_q(q, b) - 1.0, 1.0001, 1.75)

BETA_STAR = bisect_root(lambda b: zeta_hp(b) - 2.0, 1.0001, 3.0)  # zeta(beta*)=2

# ------------------------------------------------------------------ S1 family

def s1():
    print("S1 the finite-place family lives, in a bounded window")
    # CROSS-CHECK the closed-form cofactor against the general brute machinery
    # (cofactor_divisors on N = q^a) at a finite level -- verify, don't assume.
    for q in (2, 3, 5, 7, 11):
        a = 6
        N_dict = {q: a}
        L = lam_int(q ** a)
        brute = sum(d ** -1.4 for d in cofactor_divisors(N_dict, L))  # full sum
        # p-1 | lambda(q^a): odd q -> (q-1)q^(a-1), i<=a-1; the 2-column ->
        # lambda(2^a)=2^(a-2), i<=a-2 (the 2-column's shorter clock)
        closed = cofactor_sum(q, 1.4, i_max=(a - 2 if q == 2 else a - 1),
                              CAP=10 ** 30)
        ok(abs(brute - closed) < 1e-9 * brute,
           f"S1 closed cofactor != brute at q={q}: {closed} vs {brute}")
    # every q gives an interior beta_col in (1, beta*)
    fam = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    bc = {q: beta_col(q) for q in fam}
    for q in fam:
        ok(1.0 < bc[q] < BETA_STAR + 1e-9,
           f"S1 beta_col^{q} = {bc[q]} not in (1, beta*={BETA_STAR:.4f})")
        ok(abs(Z_col_q(q, bc[q]) - 1.0) < 1e-9, f"S1 beta_col^{q} not a root")
    # NOT universal: the clock varies with q (PR1)
    spread = max(bc.values()) - min(bc.values())
    ok(spread > 0.05, f"S1 beta_col nearly constant (spread {spread:.4f}) -- PR1")
    print(f"  beta* (zeta=2) = {BETA_STAR:.5f}; spread = {spread:.4f} (not universal);")
    print("  beta_col^q: " + ", ".join(f"{q}:{bc[q]:.4f}" for q in fam[:10]))
    return bc

# --------------------------------------------------------------- S2 residues

def s2(bc):
    print("S2 the clock decreases with transparent richness (residue data)")
    # the transparent-prime membership rules ARE q's residues (PR2)
    def transp(q):
        return set(transparent_primes(q, 40))
    # a prime is never transparent to its OWN column (self-blindness): the
    # residue rules hold for p != q. q=3 blind to 3, q=5 blind to 5, etc.
    for q in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        T = transp(q)
        ok(3 in T, f"S2 3 not transparent for odd q={q} (should be, q!=3)")
        if q != 5:
            ok((5 in T) == (q % 4 == 1), f"S2 5-transparency != (q=1 mod4) at q={q}")
        if q != 7:
            ok((7 in T) == (q % 3 == 1), f"S2 7-transparency != (q=1 mod3) at q={q}")
    ok(3 not in transp(3), "S2 3 wrongly transparent for its own column q=3")
    # the q=3 clause of the 7-rule: the column's OWN powers supply the 3-part
    # of 7-1=6 (6 | 2*3^inf, the i>=1 route p = d*q^i + 1) -- the plain
    # residue iff fails at q=3, and the q>=5 loop above never sees it
    ok(7 in transp(3), "S2 7 not transparent for q=3 (6 | 2*3^inf)")
    ok(2 not in transp(11), "S2 2 leaked into odd transparent set (belongs to 2-part)")
    # richer column (more/smaller transparent primes) -> larger cofactor sum ->
    # SMALLER beta_col. Check the mechanism directly at a fixed beta.
    b0 = 1.45
    ok(cofactor_sum(13, b0) > cofactor_sum(11, b0),
       "S2 q=13 (5&7 transp, base16) not richer than q=11 at fixed beta")
    ok(bc[13] < bc[11], "S2 richer q=13 does not have smaller beta_col than q=11")
    # coarse residue classes order the clock: mod-4 split (odd q, exclude 3)
    odd = [q for q in bc if q not in (2, 3)]
    c1 = [bc[q] for q in odd if q % 4 == 1]  # 5 transparent, bigger 2-part
    c3 = [bc[q] for q in odd if q % 4 == 3]
    med = lambda xs: sorted(xs)[len(xs) // 2]
    ok(med(c1) < med(c3),
       f"S2 median(q=1 mod4)={med(c1):.4f} !< median(q=3 mod4)={med(c3):.4f}")
    print(f"  transparent rules verified (2 all; 3 all odd q!=3; 5 iff q=1(4); "
          f"7 iff q=1(3) or q=3);")
    print(f"  median beta_col: q=1 mod4 {med(c1):.4f} < q=3 mod4 {med(c3):.4f} "
          f"(beta_col decreases with richness)")

# ---------------------------------------------------------------- S3 2-adic

def s3(bc):
    print("S3 the 2-adic seat")
    # q=2 the spectrum MAX (over the family): no 2-part base, only Fermat = least rich
    fermat = set(transparent_primes(2, 40))
    ok(fermat == {3, 5, 17, 257, 65537},
       f"S2 q=2 transparent set not the Fermat primes: {sorted(fermat)}")
    ok(bc[2] == max(bc.values()), f"S3 beta_col^2 not the max: {bc[2]}")
    # among ODD q, q=3 is the max (uniquely blind to the small prime 3)
    odd_bc = {q: bc[q] for q in bc if q != 2}
    ok(max(odd_bc, key=odd_bc.get) == 3, "S3 q=3 not the odd max")
    # the ordering: 2 > 3 > the rest (PR3)
    rest = [bc[q] for q in bc if q not in (2, 3)]
    ok(bc[2] > bc[3] > max(rest), "S3 spectrum not 2 > 3 > rest")
    print(f"  beta_col^2 = {bc[2]:.5f} (MAX, Fermat-only, no 2-base) "
          f"> beta_col^3 = {bc[3]:.5f} (odd max) > rest (<= {max(rest):.4f});")
    print(f"  the 2-adic place tops the irreducibility temperature spectrum.")

def main():
    bc = s1()
    s2(bc)
    s3(bc)
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")

if __name__ == "__main__":
    main()
