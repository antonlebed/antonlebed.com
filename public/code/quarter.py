"""quarter.py -- over 2, the wild departure of a field holding i read off
the cofactor of i - 1: the lam <= e at which some field holds i are
exactly the even ones below e, and the cofactor readout of the odd
primes holds at 2 with lam in place of l.

QUESTION. Let K/Q_2 be totally ramified of degree e = 2^n >= 4, cut out
by an Eisenstein F with root pi, u = 2/pi^e (triangle.py), and lam the
wild departure of wild.py, the least level where a coefficient digit of
F leaves the anchor design A_e = x^e + 2x^(e/2) + 4x^(e/4) - 6. wild.py
proved min(lam, 3e/2) is the width of the head; weld.py that a field
without i has lam <= e, so lam > e forces i into K. Which lam <= e admit
i? staircase.py's designed fields with i all have an even lam < e. Is an odd lam < e ever a field with i, is lam
= e, and what fixes lam when i is in K?

THE DERIVATION (on paper, before the engine).
  (1) THE QUARTER RELATION. With h = e/2, i - 1 has level h in K
      ((i - 1)^2 = -2i), so write i - 1 = pi^h tau, tau a unit, and tau
      = 1 + y (the residue field is F_2), j = v(y) >= 1, the level of
      tau's principal part. i^2 = -1 reads 2 + 2 pi^h tau + pi^e tau^2
      = 0, and 2 = u pi^e turns it into
          u (1 + pi^h tau) = -tau^2.
  (2) THE READOUT. wild.py's S_0 = 1 + u + u pi^h + u^2 pi^(5e/4) has
      v(S_0) = lam below the cap 3e/2. Multiply by the unit 1 + pi^h
      tau and substitute (1): 1 - tau^2 + pi^h (tau - tau^2) = -(y^2 +
      2y + pi^h y + pi^h y^2), and u^2 (1 + pi^h tau) = tau^4/(1 + pi^h
      tau), whose correction to tau^4 sits h deeper, past 3e/2, so
          S_0 (1 + pi^h tau) = -(y^2 + 2y + pi^h y + pi^h y^2)
                               + pi^(5e/4) tau^4   mod pi^(3e/2).
      2y sits at e + j and pi^h y^2 at h + 2j; both lie above 2j when
      j < h and at or above 3e/2 when j >= h, and pi^(5e/4) tau^4 =
      pi^(5e/4) mod pi^(3e/2) at j >= e/16 and otherwise sits above
      2j. With
          xi = v(y (y + pi^h)),
      which is 2j at j < h, e + v(y/pi^h + 1) > e at j = h and h + j at
      j > h, this is v(S_0) = v(y(y + pi^h) + pi^(5e/4)) below 3e/2:
          lam = xi         when xi < 5e/4,
          lam = 5e/4       when xi > 5e/4,
          lam > 5e/4       when xi = 5e/4,
      the QUARTER READOUT. So j < h gives lam = 2j, even and below e,
      and j >= h gives lam > e: a field holding i has lam in {2, 4, ...,
      e - 2} or lam > e, never odd below e and never e. Since pi^e y (y
      + pi^h) = (i - 1 - pi^h)(i - 1 - pi^h + pi^e), xi reads off i with
      no division.
  (3) THE CLIMB. Let zeta be a primitive 2^N-th root of unity, N >= 2,
      zeta - 1 = pi^c tau_N, c = e/2^(N-1), i_tau the level of tau_N's
      principal part. For x of level y <= e/4, (1 + x)^2 - 1 = x^2 (1
      + 2/x), the correction at level e - y >= 3e/4, and squaring a
      principal unit of level k < e doubles k. So the cofactor of
      i - 1 = zeta^(2^(N-2)) - 1 has principal level 2^(N-2) i_tau
      when that is below h, and at least h otherwise. With (2):
          min(lam, e) = min(2^(N-1) i_tau, e),
      the odd primes' cofactor readout (cofactor.py) at p = 2, lam in
      the place of l and the bend s = e the same cap. So lam >= 2^(N-1)
      and below e lam is a multiple of 2^(N-1).
  (4) THE DESIGN. cofactor.py's x^k + a varpi x^i - varpi over
      Q_2(zeta_(2^N)), a = 1, has tau = 1/(1 - pi^i), i_tau = i, and
      its norm A^q + B^q (q = 2^(N-1)) is Eisenstein of degree e = k q.
      At k a power of 2 and 1 <= i < k, (3) predicts lam = 2^(N-1) i <
      e, every multiple of 2^(N-1) below e; N is kept at odd i, since a
      higher root would make lam a multiple of 2^N.

THE ENGINE. N, the root and the class data as cofactor.py reads them
(staircase.py's read_deep and root_search); i_tau at every primitive
root by cofactor.py's cofactor_level; i = zeta^(2^(N-2)) and its
inverse, and xi = v((i - 1 - pi^h)(i - 1 - pi^h + pi^e)) - e; lam by
wild.py's wild_departure off the coefficients. The admission census
reads i by root_search at N = 2 alone, a returned root certified by
Hensel (v(z^2 + 1) > 2e = 2 v(2z)); None is exhaustive, since a true
root's truncations survive every floor the search applies.

TRANSPLANTS. The climb (3) is cofactor.py's (2) rerun at p = 2, where
the correction bound is e - y and not (p - 1)^2 s/p, re-derived above.
The cap of (3) is s = e where wild.py's is 3e/2: below e, (2) is the
reading, and between e and 3e/2 only (2)'s piecewise law, not (3),
says what lam is.

POPULATIONS. Designs (N, k; i): (2, 2; 1), (2, 4; 1..3), (2, 8; 1..7),
(3, 2; 1), (3, 4; 1..3), (4, 2; 1), e = 4 to 16. staircase.py's
family Phi_(2^N)(1 + x^k + 2 r(x)) at (N, k) = (2, 2), (2, 4), (2, 8),
(3, 1), (3, 2), (4, 1), r = 0 and two random r. The census: wild.py's
designed polynomials at e = 4, 8, 16, lam = 1 .. 3e/2 + 1, four draws
each, digits random above lam.

PREDICTIONS, fixed before the run.
  C  CONTROL, run first. (a) The level reader returns 1..5 on pi^c (1 +
     pi^j) at Q_2(zeta_8) and Q_2(zeta_16). (b) At both, N = 3, 4, the
     readout (3) holds and min(lam, e) = e. (c) Every census polynomial
     reads its designed lam, and A_e at e = 4, 8, 16 holds i.
  R  THE 2-ADIC COFACTOR READOUT. At every field with N >= 2 and every
     primitive 2^N-th root, min(lam, e) = min(2^(N-1) i_tau, e).
  Q  THE QUARTER READOUT. At every field with N >= 2 and both of +-i,
     min(lam, 3e/2) is min(xi, 3e/2) when xi < 5e/4 and 5e/4 when xi >
     5e/4, and lam > 5e/4 when xi = 5e/4.
  D  THE DESIGN. lam = 2^(N-1) i at every design, N kept at odd i.
  A  THE ADMISSION. In the census, every field holding i has lam even
     below e or lam > e, and every field with lam > e holds i.
KILLS, as printed observables: a C line off (nothing below is read); one
(field, root) off R; one (field, +-i) off Q; one design off D; one census
field with i at odd lam < e or at lam = e, or one with lam > e without i.

FINDINGS. Every prediction landed: 9/9 checks PASS, no kill fired.
  C  The reader returns 1..5 at both fields. Q_2(zeta_8) reads N = 3,
     lam = 6, xi = 5 = 5e/4 at both of +-i; Q_2(zeta_16) N = 4, lam = 12,
     xi = 10 = 5e/4: the tie branch, lam past 5e/4. 180 designed
     polynomials read their designed lam (A's census draws 180 more
     from the same designer), and A_e holds i at e = 4, 8, 16.
  R  34 fields, N from 2 to 4, every primitive root: min(lam, e) =
     min(2^(N-1) i_tau, e).
  Q  The same 34 at both of +-i. All three branches met: lam = xi in (e,
     5e/4) (e = 8, lam = xi = 9; e = 16, lam = xi = 18, 19); xi > 5e/4
     giving lam = 5e/4 (e = 4, 8, 16 at r = 0, xi from 8 to past the
     precision, where it prints the cap, 99 at e = 16, the two roots
     reading different xi); the tie xi = 5e/4 at the cyclotomic fields,
     lam = 3e/2.
  D  16 designs: lam = 2^(N-1) i at each, every even lam from 2 to e - 2
     at N = 2 and e = 4, 8, 16, the multiples of 4 at N = 3 and lam = 8
     at N = 4, e = 16.
  A  180 census fields: i held at no odd lam below e and at no lam = e;
     at every lam > e, 4 of 4; at the even lam below e, rarely (e = 16:
     1 of 4 at lam = 8, 2 of 4 at 14, none at 2 to 6, 10, 12), so the
     even lam below e are the designs' to realize, not the census's.
  Tiers: the quarter readout (2) and the cofactor readout at 2 (3)
  theorems, their proof the derivation above; the design (4) a theorem
  given (3); the admission a corollary of (2) and weld.py's bound.

RUN RECORD. 9/9, 11.0 s wall, peak working set 14.5 MB under a memory guard,
green on the first run.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import random

from module_law import check, section, CHECKS
from tame import INF
from weld import Units
from staircase import root_search, cyclo
from wild import wild_departure, designed, anchor
from cofactor import design, val, cofactor_level, read_field

SEED = 1430


# ------------------------------------------------------------ the readers

def lam_of(e, b, d):
    return wild_departure(e, b, d)


def quarter_m(U, iota):
    """m = v((i - 1 - pi^h)(i - 1 - pi^h + pi^e)) - e."""
    e, mod = U.e, U.mod
    ph = U.loc.pi_pow(e // 2, mod)
    pe = U.loc.pi_pow(e, mod)
    a = [(x - (k == 0) - y) % mod for k, (x, y) in enumerate(zip(iota, ph))]
    b = [(x + y) % mod for x, y in zip(a, pe)]
    return val(U, U.mul(a, b)) - e


def quarter_ok(e, lam, m):
    cap, q = 3 * e // 2, 5 * e // 4
    if m == q:
        return lam > q
    want = m if m < q else q
    return min(lam, cap) == min(want, cap)


def fourth_roots(r):
    """i and its inverse, from the primitive 2^N-th root r['root']."""
    U, N = r["U"], r["N"]
    z = [x % U.mod for x in r["root"]]
    iota = U.pw(z, 2 ** (N - 2))
    return [iota, U.pw(iota, 3)]


def read(e, b, d):
    r = read_field(2, e, b, d)
    r["lam"] = lam_of(e, b, d)
    r["ms"] = [quarter_m(r["U"], t) for t in fourth_roots(r)] \
        if r["root"] is not None and r["N"] >= 2 else []
    return r


def readout_ok(r, e):
    N = r["N"]
    return (r["root"] is not None and r["higher"] is None and r["taus"]
            and all(min(r["lam"], e) == min(2 ** (N - 1) * t, e)
                    for t in r["taus"]))


def show(r, e, label):
    lam = "inf" if r["lam"] >= INF else r["lam"]
    print(f"  e={e:2d} N={r['N']} {label:30s} lam={lam:>3} "
          f"i_tau {sorted(set(r['taus']))} xi {r['ms']}")


def holds_i(e, b, d):
    Lp = 4 * e
    z = root_search(2, e, b, d, 2, Lp)
    if z is None:
        return False
    U = Units(2, e, b, d, Lp)
    z = [x % U.mod for x in z]
    w = U.mul(z, z)
    w = [(x + (k == 0)) % U.mod for k, x in enumerate(w)]
    assert val(U, w) > 2 * e, "Hensel certificate failed"
    return True


# ------------------------------------------------------------ sections

def section_control(rng):
    section("C  CONTROL: the reader, the cyclotomic fields, the census "
            "polynomials")
    for name, N, gen in [("Q_2(zeta_8)", 3, cyclo(2, 3, 1, [])),
                         ("Q_2(zeta_16)", 4, cyclo(2, 4, 1, []))]:
        e, b, d = gen
        r = read(e, b, d)
        U, c = r["U"], r["c"]
        got = []
        for j in range(1, 6):
            pc = U.loc.pi_pow(c, U.mod)
            pj = U.loc.pi_pow(c + j, U.mod)
            got.append(cofactor_level(U, [(x + y) % U.mod
                                          for x, y in zip(pc, pj)], c))
        check(f"Ca {name}: the reader returns 1..5", got == [1, 2, 3, 4, 5],
              f"read {got}")
        show(r, e, name)
        check(f"Cb {name}: N = {N}, the readout holds, min(lam, e) = e",
              r["N"] == N and readout_ok(r, e) and min(r["lam"], e) == e,
              f"N {r['N']}, lam {r['lam']}")
    bad = n = 0
    for e in (4, 8, 16):
        for lam in range(1, 3 * e // 2 + 2):
            for _ in range(4):
                b, d = designed(rng, e, lam, 2 * e + 4)
                n += 1
                bad += lam_of(e, b, d) != lam
    anc = [holds_i(e, *anchor(e)) for e in (4, 8, 16)]
    check("Cc the census reads its designed lam; A_e holds i at e = 4, 8, "
          "16", bad == 0 and all(anc), f"{n} polynomials, {bad} off; "
          f"anchors {anc}")


DESIGNS = [(2, 2, 1)] + [(2, 4, i) for i in (1, 2, 3)] \
    + [(2, 8, i) for i in range(1, 8)] + [(3, 2, 1)] \
    + [(3, 4, i) for i in (1, 2, 3)] + [(4, 2, 1)]
CYCLO = [(2, 2), (2, 4), (2, 8), (3, 1), (3, 2), (4, 1)]


def section_fields(rng):
    section("R, Q, D  THE COFACTOR READOUT AT 2, THE QUARTER READOUT, "
            "THE DESIGN")
    bad = dict(R=0, Q=0, D=0)
    n = dict(R=0, Q=0, D=0)
    rows = []
    for N, k, i in DESIGNS:
        e, b, d = design(2, N, k, i, 1)
        rows.append((e, b, d, f"design N={N} k={k} i={i}", (N, i)))
    for N, k in CYCLO:
        for t in range(3):
            rr = [] if t == 0 else [rng.randrange(4) for _ in range(k)]
            e, b, d = cyclo(2, N, k, rr)
            rows.append((e, b, d, f"Phi_2^{N}(1+x^{k}+2r) r={rr}", None))
    for e, b, d, label, des in rows:
        r = read(e, b, d)
        show(r, e, label)
        n["R"] += 1
        okR = readout_ok(r, e)
        bad["R"] += not okR
        okQ = r["N"] >= 2 and len(r["ms"]) == 2 and all(
            quarter_ok(e, r["lam"], m) for m in r["ms"])
        n["Q"] += 1
        bad["Q"] += not okQ
        okD = True
        if des is not None:
            N, i = des
            n["D"] += 1
            okD = r["lam"] == 2 ** (N - 1) * i and (i % 2 == 0
                                                     or r["N"] == N)
            bad["D"] += not okD
        if not (okR and okQ and okD):
            print(f"    OFF: R {okR} Q {okQ} D {okD}")
    check("R min(lam, e) = min(2^(N-1) i_tau, e) at every root",
          bad["R"] == 0, f"{n['R']} fields, {bad['R']} off")
    check("Q the quarter readout at both of +-i",
          bad["Q"] == 0, f"{n['Q']} fields, {bad['Q']} off")
    check("D the design: lam = 2^(N-1) i, N kept at odd i",
          bad["D"] == 0, f"{n['D']} designs, {bad['D']} off")


def section_admission(rng):
    section("A  THE ADMISSION: which lam hold i")
    bad = 0
    for e in (4, 8, 16):
        tally = {}
        for lam in range(1, 3 * e // 2 + 2):
            for _ in range(4):
                b, d = designed(rng, e, lam, 2 * e + 4)
                has = holds_i(e, b, d)
                tally.setdefault(lam, []).append(has)
                allowed = (lam < e and lam % 2 == 0) or lam > e
                if (has and not allowed) or (lam > e and not has):
                    bad += 1
        line = " ".join(f"{lam}:{sum(v)}/{len(v)}"
                        for lam, v in sorted(tally.items()))
        print(f"  e={e:2d} lam:with-i  {line}")
    check("A i only at even lam < e or lam > e, and always at lam > e",
          bad == 0, f"{bad} off")


def main():
    rng = random.Random(SEED)
    section_control(rng)
    if not all(CHECKS):
        print("\ncontrol failed: nothing below is read")
        raise SystemExit(1)
    section_fields(rng)
    section_admission(rng)
    print()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks PASS")
    if not all(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
