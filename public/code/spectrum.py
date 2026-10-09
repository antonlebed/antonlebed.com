"""spectrum.py -- the critical point of the thermal dynamics column at
every finite place: over Z, over F_2[x] and over Z[sqrt(-5)].

QUESTION. Under the dynamics demand at inverse temperature beta, a
state M admits every m >= 2 with lambda(Mm) > lambda(M), and the
admissible mass is Psi_M(beta) = zeta(beta) - sigma_beta(xi(M)), xi(M) =
W(lambda(M))/M the headroom (thermal.py). Lock the state on one place
and deepen it: the column q^a. Given the depth the column's walk
reaches, it passes through each lower depth independently with
probability 1/(1 + Psi), Psi the admissible mass at that depth: a coin,
fair where Psi = 1 (memory.py, at q = 3). Does every
finite place carry its own critical point, what fixes it, which place
sits at the top, and what changes over F_2[x] and over a ring with a
class group?

THE ARGUMENT (written before the engine).
  (1) THE TRANSPARENCY CRITERION. Over Z, lambda(q^a) = (q - 1)
      q^(a-1) for odd q and 2^(a-2) at q = 2, a >= 3. W(L) =
      2^(v_2(L)+2) prod p^(v_p(L)+1) over odd p with p - 1 | L. At
      the column the factor q^(v_q(L)+1) = q^a is exactly the state,
      so the headroom carries no q: the EXCLUSION p != q is part of
      the criterion, since q - 1 divides L and q would otherwise
      read its own prime. So xi(q^a) is 2^(v_2(q-1)+2) times the
      odd p != q with p - 1 | (q - 1) q^(a-1), each at exponent
      v_p(q - 1) + 1; at q = 2 the 2-part cancels and the odd p are
      those with p - 1 a power of 2 below 2^(a-1), the Fermat
      primes. xi grows with a to the supernatural C_q, the same
      product over p - 1 | (q - 1) q^oo, that is p = d q^i + 1 with
      d | q - 1.
  (2) THE ROOT'S RANGE. Psi_q = zeta - sigma_beta(C_q) is a sum of m^(-beta)
      over a fixed set of m, so strictly decreasing in beta.
      sum 1/p over the transparent p converges (p > d q^i, geometric
      in i), so sigma_beta(C_q) stays bounded as beta -> 1+ while
      zeta blows up; and C_q >= 3 gives Psi_q < zeta - 1, below 1 at
      beta*, the root of zeta = 2. One root beta_q in (1, beta*).
  (3) THE ORDER AT THE TOP. beta_q < beta_r iff Psi_q(beta_r) < 1 iff
      sigma(C_q) > sigma(C_r) at beta_r; it suffices at every beta.
      (a) q odd, q != 3: C_q has 2-part >= 8 and holds 3, so
      sigma(C_q) >= sigma(8)(1 + 3^-b). C_2 = 3 times the Fermat
      primes F >= 5, all of the form 2^(2^n) + 1, and sum (2/F) over
      n >= 1 is below 0.5255, so for b >= 1 Y = sum F^-b <=
      0.5255 2^-b <= 0.263 and prod (1 + F^-b) - 1 <= Y e^Y <=
      0.684 2^-b < 2^-b < sigma(8) - 1. So beta_q < beta_2.
      (b) q = 3: sigma(C_3) >= 1 + 2^-b + 4^-b + 7^-b, and the same
      sum written against 5 (sum 5/F <= 1.3137) gives sigma(C_2) <=
      1 + 3^-b + 1.7085 (5^-b + 15^-b). Then (15/7)^b >= 1.7085,
      2^-b - 3^-b >= 2^-b / 3, and (5/2)^b / 3 + (5/4)^b >= 2.083 >
      1.7085 at every b >= 1, so beta_3 < beta_2.
      (c) q >= 5 against 3: sigma(C_3) = sigma(8) prod (1 + p^-b)
      over the primes p = 2 3^i + 1, i >= 1, and sum (2 3^i)^-b <=
      0.75 3^-b <= 0.25 gives prod - 1 <= 0.9631 3^-b < 3^-b, while
      sigma(C_q) >= sigma(8)(1 + 3^-b). So beta_q < beta_3.
      THE 2-ADIC PLACE TOPS THE SPECTRUM AND THE 3-ADIC IS SECOND, at
      every prime, unknown Fermat primes included.
  (4) F_2[x]. lambda(g^a) = (2^d - 1) 2^ceil(log2 a) at deg g = d, so
      f^j (f != g, deg f = e) is transparent at g^a iff e | d and
      2^ceil(log2 j) <= 2^ceil(log2 a). At the states a = 2^mu the
      column's own headroom is zero and every other place of degree
      dividing d rides at exponent 2^mu: the limit headroom is
      C_d(z) = prod_(e | d) (1 - z^e)^-(N_e - [e = d]), z = 2^-b,
      N_e the irreducibles of degree e. With zeta = 1/(1 - 2z) the
      clock equation zeta - C_d = 1 clears to a polynomial. d = 1:
      1/(1 - 2z) - 1/(1 - z) = 1 gives 2z^2 - 4z + 1 = 0, z = 1 -
      1/sqrt 2, gamma_1 = log2(2 + sqrt 2); beta* = 2 (z = 1/4). For
      d >= 2, C_d holds both degree-1 places at unbounded exponent,
      C_d >= (1 - z)^-2 > C_1 coefficientwise: DEGREE 1 TOPS. At
      a = 2^mu + 1 the column's own headroom is 2^mu - 1 and the
      cofactor tends to C_d / (1 - z^d): the headroom breathes, and
      the critical point is read at the zero-headroom states.
  (5) A NUMBER FIELD. At a prime P of norm N over p, lambda(P^a) =
      (N - 1) p^c(a) with c(a) -> oo on any chain (the 1-units of the
      completion contain a copy of Z_p, so the quotients' exponents
      grow without bound). A prime R != P enters the limit headroom to the
      largest j with lambda(R^j) | (N - 1) p^oo: a function of N, p
      and R's own chain, never of c. The limit headroom reads the splitting law
      and the entrants' depths, never the column's chain.
  (6) THE CLASS SPLIT. The element world admits principal moves only.
      Its normalizer is the total weight less the headroom's: the weight
      of every principal ideal, zeta_princ = (1/h) sum_chi L(b, chi)
      over the class-group characters, less that of the headroom's
      principal divisors, C_princ = (1/h) sum_chi C_chi, C_chi the
      headroom's divisor sum twisted by chi. At Z[sqrt(-5)], h = 2,
      zeta_K = zeta L(chi_-20) and the nontrivial L is L(chi_-4)
      L(chi_5). Near b = 1 only zeta_K has a pole, so Psi_id / Psi_el -> h:
      the class number is read off the two normalizers' ratio at the
      pole, never off their two roots.

DESIGN.
  Q  over Z. Q1 the criterion: for every prime q <= 47 and a <= 6 the
     set {m <= 20000 : lambda(q^a m) = lambda(q^a)} (lambda from the
     factorization, checked against brute element orders for M <= 400)
     equals the divisors <= 20000 of the finite cofactor of (1).
     POSITIVE CONTROL: the cofactor with the exclusion p != q dropped
     must disagree. Q2 the spectrum: beta_q for every prime q < 1000,
     the transparent primes to 10^24, zeta by mpmath; every root in
     (1, beta*), each bisected to 1e-12 with the sign of Psi - 1 read at
     both ends. Q3 the order: the three inequalities of (3) on a
     grid of b in [1, 12], each constant recomputed; beta_2 > beta_3
     > every other beta_q < 1000. POSITIVE CONTROL for the comparison:
     the pointwise test sigma(C_13) > sigma(C_11) on the grid, read
     against the roots, beta_13 < beta_11. Cross-check: beta_3 against
     memory.py's column normalizer.
  F  over F_2[x]. F1 lambda(g^a) of (4) against brute element orders
     in F_2[x]/(g^a) for deg g^a <= 8; the transparent set at g^a
     against a scan of every monic of degree <= 9, for the five
     irreducibles of degree <= 3 at a <= 4. F2 the clocks d = 1..6 as
     roots of zeta - C_d = 1 in z; d = 1 against log2(2 + sqrt 2);
     beta* = 2. F3 the breathing at d = 1: C_1 / (1 - z) =
     (1 - z)^-2 = C_2 as series, and the root finder's c_d at d = 1, 2
     against those series at z = 0.1, 0.25, 0.4.
  K  over Z[sqrt(-5)], O = Z[w], w^2 = -5. K1 the local chains:
     lambda(O/R^j) by brute element orders in the quotient (ideals in
     Hermite form) for every prime over a split r < 50, every inert
     prime of norm r^2 <= 400, P5, and N(R^j) <= 3000,
     against: split (r - 1) r^(j-1), inert (r^2 - 1) r^(j-1), P5
     4 5^ceil((j-1)/2); P2 by brute alone. K2 the headroom entrants at four
     columns P2, P3, Q7, (13) from (5), split primes r < 10^6;
     principality of each entrant by x^2 + 5y^2 = N(R). K3 the ideal
     and element clocks at P3 and the four ideal clocks. POSITIVE
     CONTROL: zeta_princ(2) from the L-functions against the direct
     lattice sum of (x^2 + 5y^2)^-2 / 2, and the Euler factor of L_cl
     at every split and ramified r < 1000 against the principality
     read by the norm form.
     K4 Psi_id / Psi_el at b = 1.2, 1.05, 1.01.

PREDICTIONS, fixed before the run. Numbers carried from the replaced
records are TRANSPLANTS, marked (T); the engine here is new.
  Q1 closed = brute at every (q, a); the control disagrees somewhere.
  Q2 beta* = 1.72865 (T); beta_2 = 1.60449 (T), beta_3 = 1.49595 (T,
     and memory.py's), beta_5 = 1.4206 (T); all 168 roots interior.
  Q3 every inequality holds at every grid point with the constants
     0.684, 1.7085, 2.083, 0.9631 reproduced; beta_2 > beta_3 > rest.
     The control: sigma(C_13) > sigma(C_11) at b = 1.45 (T), and the
     reverse fails.
  F1 formula = brute everywhere; the transparent set is the subfield
     lattice of (4). F2 1.77155, 1.50553, 1.47652, 1.39505, 1.48768,
     1.33584 (T); d = 5 above d = 3, so the spectrum is not monotone
     in d; degree 1 the maximum. F3 exact to the series order taken.
  K1 formula = brute on every split, inert and P5 power; P2's chain
     1, 2, 4, 4, 4, 4, 8, 8, 16 (T). K2 the P3 headroom entrants: P2 to exponent 2,
     P3' unbounded, both primes over 7, 163, 487, 39367 (T), 19 and
     1459 inert and absent (T); every entrant nonprincipal. K2b past
     10^6 the next split r = 2 3^i + 1 is 2 3^16 + 1 = 86093443 (T). K3 ideal
     1.54922, element 1.35270 (T); P2 1.70395 > P3 > Q7 1.45633 >
     (13) 1.31983 (T). K4 2.0317, 2.0056, 2.0010 (T), falling to 2.
  [Ruled after a later reading: the controls now run before the
  verdicts they guard and stop the run when one fails; F2's beta* = 2
  check, arithmetic on a literal, is cut; F3 builds both sides from
  the divisor-sum series; Q3 asserts the sums 0.5255 and 1.3137.]

FINDINGS. Every prediction held; every transplant was reproduced by
an engine that shares no code with the records it replaces.
  Q  THE CRITERION (property, from the closed forms; brute in range):
     the headroom of q^a is the divisors of (1)'s cofactor at all 88
     cells q <= 47, a <= 6 (a >= 3 at q = 2), m <= 20000; with the
     exclusion dropped, all 84 odd-q cells disagree. THE SPECTRUM
     (observation): beta* = 1.72865; beta_2 = 1.60449, beta_3 =
     1.49595 (memory.py's root, its bracket straddling 1), beta_5 =
     1.42057, beta_7 = 1.42344, beta_13 = 1.34090. Over the 168 primes
     below 1000 the largest past 3 is beta_47 = 1.44172 and the least
     beta_541 = 1.28150; every root interior. THE ORDER (theorem, by
     (3)): the constants come out 0.68335, 1.70837, 0.96302, and
     2.08333 against 1.7085; the three inequalities hold on the grid,
     and beta_2 > beta_3 > beta_47. The spectrum is not monotone in q
     (beta_5 < beta_7 < beta_11).
  F  lambda(g^a) = brute at 24 states; the transparency read as the
     places whose residue field embeds in F_(2^d), at 20440 cells. The
     clocks gamma_d, the roots in b of (4)'s zeta - C_d = 1 (printed as
     beta_d), are 1.77155, 1.50553, 1.47652, 1.39505, 1.48768, 1.33584
     at d = 1 to 6; z = 0.29289321881 at d = 1,
     gamma_1 = log2(2 + sqrt 2) = 1.77155330316. At a later reading F3
     also holds c_d at d = 1, 2 to the series, its residual printed.
  K  P2's chain to j = 11 is 1, 2, 4, 4, 4, 4, 8, 8, 16, 16, 32; the
     split, inert and P5 formulas = brute at 50 prime powers. The P3
     headroom entrants: P2 to exponent 2, P3' unbounded, both primes over 7, 163,
     487 and 39367, none principal; 19 and 1459 have r - 1 | 2 3^oo
     and are inert, so they never enter. Ideal clocks P2 1.70395, P3
     1.54922, Q7 1.45633, (13) 1.31983; element clock at P3 1.35270;
     Psi_id / Psi_el = 2.0317, 2.0056, 2.0010 at b = 1.2, 1.05, 1.01.

RUN RECORD. `python spectrum.py`: 25 of 25 checks pass, about 8 s,
peak commit 19.5 MB. The first run failed one check in the control
itself: the lattice sum counts the unit ideal at x = +-1, y = 0, and
a 1 had been added on top (2.2512107 against 1.2512111). With it
removed the two agree to 4e-7. At audit, the reason in (5) was
corrected: the exponents grow because the 1-units hold a copy of Z_p,
not because their rank is finite.
"""

import math
import os
import sys
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mpmath as mp  # noqa: E402

import growth  # noqa: E402
import memory  # noqa: E402
from growth import (IRR, factor, is_prime_mr, lam_f2, lam_int,  # noqa: E402
                    pdeg, pdivmod, pmul, unit_exponent)

mp.mp.dps = 30
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}"
                                                      if detail else ""))


def control(name, ok, detail=""):
    """A positive control: a failure stops the run before any verdict
    that leans on it."""
    check(name, ok, detail)
    if not ok:
        print("a control failed: no verdict after it is read")
        sys.exit(1)


def section(title):
    print()
    print(title)


def lcm(a, b):
    return a // gcd(a, b) * b


def vp(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def divisors_of(n):
    out = [1]
    for p, e in factor(n).items():
        out = [d * p ** k for d in out for k in range(e + 1)]
    return out


def zeta(b):
    return float(mp.zeta(b))


def bisect(f, lo, hi, tol=1e-12):
    """The root of a function decreasing through 0 on [lo, hi]."""
    flo, fhi = f(lo), f(hi)
    assert flo > 0 > fhi, (lo, hi, flo, fhi)
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# ------------------------------------------------------------------ Q

CAP = 10 ** 24          # Miller-Rabin in growth.py is exact below 3.3e24


def cofactor(q, a=None, excl=True):
    """The headroom of the column q^a as {p: exponent}; a = None is the
    limit C_q, truncated at CAP. excl=False drops the exclusion p != q
    (the positive control)."""
    out = {}
    if q == 2:
        top = a - 2 if a else 80
        for k in range(0, top + 1):
            p = 2 ** k + 1
            if p > CAP:
                break
            if p > 2 and is_prime_mr(p):
                out[p] = 1
        return out
    out[2] = vp(q - 1, 2) + 2
    for d in divisors_of(q - 1):
        i, val = 0, d
        while (a is None or i <= a - 1) and val + 1 < CAP:
            p = val + 1
            if p > 2 and (p != q or not excl) and is_prime_mr(p):
                out[p] = vp(q - 1, p) + 1
            val *= q
            i += 1
    return out


def sig(f, b):
    s = 1.0
    for p, e in f.items():
        s *= sum(p ** (-k * b) for k in range(e + 1))
    return s


def value_of(f):
    n = 1
    for p, e in f.items():
        n *= p ** e
    return n


def beta_q(q):
    C = cofactor(q)
    return bisect(lambda b: zeta(b) - sig(C, b) - 1, 1.0001, 1.75)


def section_q():
    section("Q  the place spectrum over Z")
    bad = sum(lam_int(M) != unit_exponent(M) for M in range(2, 401))
    check("Q0 lambda from the factorization = brute unit exponent, "
          "M <= 400", bad == 0)
    X = 20000
    lam_m = [0, 1] + [lam_int(m) for m in range(2, X + 1)]
    bad = ctrl = odd = odd_off = 0
    for q in [p for p in range(2, 48) if is_prime_mr(p)]:
        for a in range(3 if q == 2 else 1, 7):
            L0 = lam_int(q ** a)
            lq = [lam_int(q ** k) if k else 1 for k in range(a + 16)]
            brute = set()
            for m in range(2, X + 1):
                v = vp(m, q)
                if lcm(lq[a + v], lam_m[m // q ** v]) == L0:
                    brute.add(m)
            closed = {d for d in divisors_of(value_of(cofactor(q, a)))
                      if 1 < d <= X}
            cl2 = {d for d in divisors_of(value_of(cofactor(q, a, False)))
                   if 1 < d <= X}
            bad += brute != closed
            ctrl += brute != cl2
            if q > 2:
                odd += 1
                odd_off += brute != cl2
    control("Q1 CONTROL: the exclusion p != q dropped disagrees at every "
            "odd q", ctrl > 0 and odd_off == odd,
            f"{ctrl} cells off, {odd_off} of the {odd} odd-q cells")
    check("Q1 the transparent set = divisors of the closed cofactor, "
          "q <= 47, a <= 6, m <= 20000", bad == 0, f"{bad} off")

    bstar = bisect(lambda b: zeta(b) - 2, 1.0001, 3)
    qs = [p for p in range(2, 1000) if is_prime_mr(p)]
    B = {}
    for q in qs:
        B[q] = beta_q(q)
    inside = all(1 < B[q] < bstar for q in qs)
    print(f"  beta* = {bstar:.5f}; beta_q: " +
          ", ".join(f"{q}:{B[q]:.5f}" for q in qs[:10]))
    rest = max(B[q] for q in qs if q > 3)
    qmax = max((q for q in qs if q > 3), key=lambda q: B[q])
    qmin = min(qs, key=lambda q: B[q])
    print(f"  over the {len(qs)} primes below 1000: the largest past 3 is "
          f"beta_{qmax} = {rest:.5f}, the least beta_{qmin} = "
          f"{B[qmin]:.5f}")
    check("Q2 every root below beta*, each above 1.0001 by its "
          "bracket's signs", inside)
    check("Q2 beta* = 1.72865, beta_2 = 1.60449, beta_3 = 1.49595, "
          "beta_5 = 1.4206",
          abs(bstar - 1.72865) < 1e-5 and abs(B[2] - 1.60449) < 1e-5
          and abs(B[3] - 1.49595) < 1e-5 and abs(B[5] - 1.4206) < 1e-4)
    lo, hi = memory.z_col_bracket(B[3])
    check("Q2 beta_3 is memory.py's column root: its bracket straddles 1",
          lo <= 1.0 <= hi + 1e-12, f"[{lo:.10f}, {hi:.10f}]")

    # Q3 the order at the top, the constants of the argument recomputed
    F = [2 ** (2 ** n) + 1 for n in range(1, 7)]
    s2 = sum(2 / f for f in F) + 4 * 2.0 ** -64
    s5 = sum(5 / f for f in F) + 10 * 2.0 ** -64
    c_a = s2 * math.exp(s2 / 2)
    c_b = s5 * math.exp(s5 / 5)
    t3 = 2 ** -1 / (1 - 3 ** -1)          # sum of (2 3^i)^-b over i >= 1
    c_c = t3 * math.exp(t3 / 3)           # is at most t3 3^-b <= t3 / 3
    print(f"  constants: sum 2/F = {s2:.6f}, {c_a:.5f}; sum 5/F = "
          f"{s5:.6f}, {c_b:.5f}; {c_c:.5f}; (5/2)/3 + 5/4 = "
          f"{2.5 / 3 + 1.25:.5f}")
    C11, C13 = cofactor(11), cofactor(13)
    grid = [1 + 0.01 * i for i in range(1101)]
    fwd = all(sig(C13, b) > sig(C11, b) for b in grid)
    control("Q3 CONTROL: the pointwise test agrees with the roots, "
            "sigma(C_13) > sigma(C_11) on the grid and beta_13 < beta_11",
            fwd and B[13] < B[11])
    check("Q3 the constants: sum 2/F < 0.5255 and sum 5/F < 1.3137; "
          "0.684, 1.7085, 0.9631 bound them",
          s2 < 0.5255 and s5 < 1.3137
          and c_a <= 0.684 and c_b <= 1.7085 and c_c <= 0.9631
          and 2.5 / 3 + 1.25 > 1.7085 and 15 / 7 > 1.7085)
    C2, C3 = cofactor(2), cofactor(3)
    fer = {p: 1 for p in C2 if p != 3}
    odd3 = {p: e for p, e in C3.items() if p != 2}
    ok_a = ok_b = ok_c = True
    for b in grid:
        s8 = sum(2 ** (-k * b) for k in range(4))
        ok_a &= sig(fer, b) - 1 <= 0.684 * 2 ** -b < s8 - 1
        ok_b &= (sig(C2, b) <= 1 + 3 ** -b + 1.7085 * (5 ** -b + 15 ** -b)
                 < 1 + 2 ** -b + 4 ** -b + 7 ** -b <= sig(C3, b))
        ok_c &= sig(odd3, b) - 1 <= 0.9631 * 3 ** -b < 3 ** -b
    check("Q3 (a) (b) (c) hold at every b on [1, 12] by 0.01",
          ok_a and ok_b and ok_c, f"{ok_a} {ok_b} {ok_c}")
    check("Q3 beta_2 > beta_3 > every other beta_q, q < 1000",
          B[2] > B[3] > rest)
    return B


# ------------------------------------------------------------------ F

def pmod(a, m):
    return pdivmod(a, m)[1]


def f2_order(u, M):
    o, y = 1, u
    while y != 1:
        y = pmod(pmul(y, u), M)
        o += 1
    return o


def necklace(e):
    return len(IRR[e])


def c_d(d, x):
    out = 1.0
    for e in range(1, d + 1):
        if d % e == 0:
            out *= (1 - x ** e) ** -(necklace(e) - (e == d))
    return out


def c_d_series(d, n):
    """C_d's coefficients to z^n, exactly: the product over e | d of
    (1 - z^e)^-(N_e - [e = d])."""
    out = [1] + [0] * n
    for e in range(1, d + 1):
        if d % e == 0:
            k = necklace(e) - (e == d)
            f = [0] * (n + 1)
            for j in range(n // e + 1):
                f[e * j] = math.comb(k + j - 1, j) if k else int(j == 0)
            out = [sum(out[i] * f[t - i] for i in range(t + 1))
                   for t in range(n + 1)]
    return out


def beta_f2(d):
    # zeta - C_d - 1 decreases in b: it is a sum of 2^(-b deg m) over a
    # fixed set of monics
    return bisect(lambda b: 1 / (1 - 2 * 2 ** -b) - c_d(d, 2 ** -b) - 1,
                  1.0001, 2.5)


def section_f():
    section("F  the spectrum over F_2[x]")
    bad = n = 0
    for d in range(1, 4):
        for g in IRR[d]:
            a = 1
            while d * a <= 8:
                M = growth.ppow(g, a)
                L = 1
                for u in range(1, 1 << pdeg(M)):
                    if pmod(u, g) != 0:
                        L = lcm(L, f2_order(u, M))
                bad += L != (((1 << d) - 1) << (a - 1).bit_length())
                n += 1
                a += 1
    check("F1 lambda(g^a) = (2^d - 1) 2^ceil(log2 a), brute, "
          "deg g^a <= 8", bad == 0, f"{n} states")
    bad = n = 0
    mons = range(2, 1 << 10)
    for d in range(1, 4):
        for g in IRR[d]:
            for a in range(1, 5):
                M = growth.ppow(g, a)
                L0 = lam_f2(M)
                top = 1 << (a - 1).bit_length()
                for m in mons:
                    got = lam_f2(pmul(M, m)) == L0
                    want = True
                    for h, v in growth.pfactor(m).items():
                        if h == g:
                            want &= a + v <= top
                        else:
                            want &= d % pdeg(h) == 0 and v <= top
                    bad += got != want
                    n += 1
    check("F1 transparent at g^a iff every factor h^v has deg h | d, "
          "v <= 2^c (and a + v <= 2^c at h = g)", bad == 0,
          f"{n} cells")
    bs = {d: beta_f2(d) for d in range(1, 7)}
    x1 = 2 ** -bs[1]
    print("  beta_d: " + ", ".join(f"{d}:{bs[d]:.5f}" for d in bs))
    print(f"  z at d = 1: {x1:.11f}; log2(2 + sqrt 2) = "
          f"{math.log2(2 + math.sqrt(2)):.11f}")
    check("F2 d = 1 is z = 1 - 1/sqrt 2, beta = log2(2 + sqrt 2)",
          abs(x1 - (1 - 1 / math.sqrt(2))) < 1e-11
          and abs(2 * x1 * x1 - 4 * x1 + 1) < 1e-11)
    x2 = 2 ** -bs[2]
    check("F2 d = 2 solves 2z^3 - 4z^2 + 4z - 1 = 0",
          abs(2 * x2 ** 3 - 4 * x2 ** 2 + 4 * x2 - 1) < 1e-11)
    want = [1.77155, 1.50553, 1.47652, 1.39505, 1.48768, 1.33584]
    check("F2 the six clocks match; d = 5 above d = 3; degree 1 the max",
          all(abs(bs[d] - want[d - 1]) < 1e-5 for d in bs)
          and bs[5] > bs[3] and bs[1] == max(bs.values()))
    # the breathing: C_1 / (1 - z) against C_2, as series to z^20
    s1 = c_d_series(1, 20)
    s1b = [sum(s1[:k + 1]) for k in range(21)]     # C_1 / (1 - z)
    s2 = c_d_series(2, 20)
    # the root finder's c_d against the exact series, the tail past
    # z^20 below 22 x^21 / (1 - x)^2 < 1e-6 at x <= 0.4
    res = max(abs(c_d(d, x) - sum(c * x ** k for k, c in
                                  enumerate(c_d_series(d, 20))))
              for d in (1, 2) for x in (0.1, 0.25, 0.4))
    check("F3 C_1 / (1 - z) = (1 - z)^-2 = C_2 to z^20, and the root "
          "finder's c_d at d = 1, 2 equals the series at z = 0.1, 0.25, "
          "0.4", s1b == s2 == [k + 1 for k in range(21)] and res < 1e-6,
          f"largest residual {res:.1e}")


# ------------------------------------------------------------------ K

def emul(a, b):
    return (a[0] * b[0] - 5 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def egcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


class Ideal:
    """A Z-lattice in Z[w] closed under w, kept as the Hermite basis
    (A, 0), (B, C): the lattice {(A s + B t, C t)}."""

    def __init__(self, gens):
        vecs = []
        for g in gens:
            vecs += [g, emul(g, (0, 1))]
        C, v = 0, (0, 0)
        for u in vecs:
            g, s, t = egcd(C, u[1])
            if g != C:
                v = (s * v[0] + t * u[0], s * v[1] + t * u[1])
                C = g
        A = 0
        for u in vecs:
            A = gcd(A, u[0] - (u[1] // C) * v[0])
        self.A, self.B, self.C = A, v[0] % A, C

    def norm(self):
        return self.A * self.C

    def red(self, z):
        t = z[1] // self.C
        return ((z[0] - t * self.B) % self.A, z[1] - t * self.C)

    def gens(self):
        return [(self.A, 0), (self.B, self.C)]

    def __mul__(self, other):
        return Ideal([emul(g, h) for g in self.gens() for h in other.gens()])


def epow(z, n, I):
    r, z = I.red((1, 0)), I.red(z)
    while n:
        if n & 1:
            r = I.red(emul(r, z))
        z = I.red(emul(z, z))
        n >>= 1
    return r


def brute_lam(R, j):
    """The unit exponent of O/R^j by element orders, R prime."""
    I = R
    for _ in range(j - 1):
        I = I * R
    N, NR = I.norm(), R.norm()
    G = N - N // NR
    pf = factor(G)
    one = I.red((1, 0))
    L = 1
    for x in range(I.A):
        for y in range(I.C):
            if R.red((x, y)) == (0, 0):
                continue
            o = G
            for p in pf:
                while o % p == 0 and epow((x, y), o // p, I) == one:
                    o //= p
            L = lcm(L, o)
    return L


def chi4(n):
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


def chi5(n):
    r = n % 5
    return 0 if r == 0 else (1 if r in (1, 4) else -1)


def chi20(n):
    return chi4(n) * chi5(n)


def lfun(b, chi, m):
    return float(mp.power(m, -b) * mp.fsum(chi(a) * mp.zeta(b, mp.mpf(a) / m)
                                           for a in range(1, m + 1)))


def rep(n):
    """n = x^2 + 5 y^2 for some integers x, y."""
    y = 0
    while 5 * y * y <= n:
        x = math.isqrt(n - 5 * y * y)
        if x * x == n - 5 * y * y:
            return True
        y += 1
    return False


P2_CHAIN = []           # filled by brute force in K1


def lam_local(kind, r, j):
    if kind == "split":
        return (r - 1) * r ** (j - 1)
    if kind == "inert":
        return (r * r - 1) * r ** (j - 1)
    if kind == "P5":
        return 4 * 5 ** (j // 2)          # 4 5^ceil((j-1)/2)
    return P2_CHAIN[j - 1] if j <= len(P2_CHAIN) else None


def kind_of(r):
    if r == 2:
        return "P2"
    if r == 5:
        return "P5"
    return "split" if chi20(r) == 1 else "inert"


def places_over(r):
    """(kind, norm, count of primes over r, principal?)."""
    k = kind_of(r)
    if k == "split":
        return k, r, 2, rep(r)
    if k == "inert":
        return k, r * r, 1, True
    return k, r, 1, rep(r)


def fits(lam, N, p):
    while lam % p == 0:
        lam //= p
    return (N - 1) % lam == 0


RPRIMES = growth.primes_up_to(10 ** 6)


def menu(col):
    """The limit headroom entrants of the column at a prime over p of norm N: every
    prime R != P with its depth (None = unbounded), norm and class."""
    p, N = col
    out = []
    for r in RPRIMES:
        k, NR, cnt, pr = places_over(r)
        if r == p:
            cnt -= 1                       # the column's own prime
        for _ in range(cnt):
            j = 0
            while True:
                lam = lam_local(k, r, j + 1)
                assert lam is not None, "P2 chain too short"
                if not fits(lam, N, p):
                    break
                j += 1
                if j > 64:
                    j = None
                    break
            if j != 0:
                out.append((r, NR, j, pr))
    return out


def c_menu(men, b, twist=False):
    s = 1.0
    for r, NR, cap, pr in men:
        c = 1 if (pr or not twist) else -1
        if cap is None:
            s *= 1 / (1 - c * NR ** -b)
        else:
            s *= sum((c * NR ** -b) ** k for k in range(cap + 1))
    return s


def section_k():
    section("K  the spectrum over Z[sqrt(-5)]")
    P2 = Ideal([(2, 0), (1, 1)])
    P5 = Ideal([(5, 0), (0, 1)])
    for j in range(1, 12):
        P2_CHAIN.append(brute_lam(P2, j))
    print(f"  P2 chain j = 1..11: {P2_CHAIN}")
    check("K1 P2's chain begins 1, 2, 4, 4, 4, 4, 8, 8, 16",
          P2_CHAIN[:9] == [1, 2, 4, 4, 4, 4, 8, 8, 16])
    bad = n = 0
    for j in range(1, 5):
        bad += brute_lam(P5, j) != lam_local("P5", 5, j)
        n += 1
    for r in range(3, 50):
        if not is_prime_mr(r) or r == 5:
            continue
        k = kind_of(r)
        if k == "inert" and r * r > 400:
            continue
        roots = [s for s in range(r) if (s * s + 5) % r == 0]
        Rs = ([Ideal([(r, 0), (-s, 1)]) for s in roots] if k == "split"
              else [Ideal([(r, 0)])])
        for R in Rs:
            j = 1
            while R.norm() ** j <= 3000:
                bad += brute_lam(R, j) != lam_local(k, r, j)
                n += 1
                j += 1
    check("K1 the local chains: split, inert and P5 formulas = brute",
          bad == 0, f"{n} prime powers")

    bad = 0
    for r in range(2, 1000):
        if not is_prime_mr(r):
            continue
        k = kind_of(r)
        if k == "split":
            bad += (chi4(r) == 1) != rep(r)
        elif k == "P2":
            bad += rep(2) or chi5(2) != -1
        elif k == "P5":
            bad += (not rep(5)) or chi4(5) != 1
    control("K3 CONTROL: L(chi_-4) L(chi_5)'s Euler factors = the "
            "classes read off x^2 + 5y^2, split and ramified r < 1000",
            bad == 0)
    X = 1000
    tot = 0.0
    for y in range(-X, X + 1):
        c = 5 * y * y
        for x in range(-X, X + 1):
            if x or y:
                tot += (x * x + c) ** -2.0
    direct = tot / 2                     # (1) is x = +-1, y = 0
    zp2 = (zeta(2) * lfun(2, chi20, 20) + lfun(2, chi4, 4) *
           lfun(2, chi5, 5)) / 2
    control("K3 CONTROL: zeta_princ(2) from the L-functions = the "
            "lattice sum", abs(direct - zp2) < 1e-5,
            f"{zp2:.7f} vs {direct:.7f}")

    cols = {"P2": (2, 2), "P3": (3, 3), "Q7": (7, 7), "(13)": (13, 169)}
    men = {c: menu(v) for c, v in cols.items()}
    m3 = men["P3"]
    print("  P3 headroom entrants (norm, depth, principal): " +
          ", ".join(f"({NR},{cap},{int(pr)})" for r, NR, cap, pr in m3))
    gated = [r for r in range(4, 2000) if is_prime_mr(r)
             and kind_of(r) == "inert" and fits(r - 1, 3, 3)]
    print(f"  split-shaped r = d 3^i + 1 < 2000 that are inert: {gated}")
    norms = sorted({r for r, NR, cap, pr in m3})
    check("K2 the P3 headroom entrants: P2 to 2, P3' unbounded, both over 7, 163, "
          "487, 39367; none principal",
          norms == [2, 3, 7, 163, 487, 39367]
          and [c for r, _, c, _ in m3 if r == 2] == [2]
          and [c for r, _, c, _ in m3 if r == 3] == [None]
          and sum(r == 7 for r, *_ in m3) == 2
          and not any(pr for *_, pr in m3) and gated == [19, 1459])
    nxt = [i for i in range(10, 17) if is_prime_mr(2 * 3 ** i + 1)
           and kind_of(2 * 3 ** i + 1) == "split"]
    check("K2b past 10^6 the next split r = 2 3^i + 1 is 2 3^16 + 1",
          nxt == [16], f"split at i = {nxt}")

    def zK(b):
        return zeta(b) * lfun(b, chi20, 20)

    def lcl(b):
        return lfun(b, chi4, 4) * lfun(b, chi5, 5)

    ideal = {c: bisect(lambda b, m=men[c]: zK(b) - c_menu(m, b) - 1,
                       1.01, 3, 1e-9) for c in cols}
    el = bisect(lambda b: (zK(b) + lcl(b)) / 2
                - (c_menu(m3, b) + c_menu(m3, b, True)) / 2 - 1,
                1.01, 3, 1e-9)
    print("  ideal clocks: " + ", ".join(f"{c}:{ideal[c]:.5f}"
                                         for c in cols) +
          f"; element P3: {el:.5f}")
    check("K3 ideal P3 1.54922, element 1.35270",
          abs(ideal["P3"] - 1.54922) < 1e-5 and abs(el - 1.35270) < 1e-5)
    check("K3 P2 1.70395 > P3 > Q7 1.45633 > (13) 1.31983",
          abs(ideal["P2"] - 1.70395) < 1e-5
          and abs(ideal["Q7"] - 1.45633) < 1e-5
          and abs(ideal["(13)"] - 1.31983) < 1e-5
          and ideal["P2"] > ideal["P3"] > ideal["Q7"] > ideal["(13)"])
    rat = []
    for b in (1.2, 1.05, 1.01):
        zi = zK(b) - c_menu(m3, b)
        ze = ((zK(b) + lcl(b)) / 2
              - (c_menu(m3, b) + c_menu(m3, b, True)) / 2)
        rat.append(zi / ze)
    print("  Psi_id / Psi_el at 1.2, 1.05, 1.01: " +
          ", ".join(f"{x:.4f}" for x in rat))
    check("K4 the ratio 2.0317, 2.0056, 2.0010, falling to 2",
          all(abs(x - w) < 1e-4 for x, w in
              zip(rat, (2.0317, 2.0056, 2.0010)))
          and rat[0] > rat[1] > rat[2] > 2)


def main():
    section_q()
    section_f()
    section_k()
    print()
    print(f"{sum(CHECKS)} of {len(CHECKS)} checks pass")
    sys.exit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
