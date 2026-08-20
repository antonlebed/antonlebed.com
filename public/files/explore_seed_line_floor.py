"""explore_seed_line_floor.py -- the least size and least degree at which a
seed's negative factor is torsion-free ALONG A LINE, read with the criterion
the plane census used. (Vocabulary and the torsion notions of
explore_seed_torsion.py; this file is univariate and needs none of its
machinery.)

THE QUESTION. A MENU is a finite set of integers >= 2 read as a
0/1-coefficient polynomial in the primes; its CORE is that polynomial with
the monomial content divided out; a menu is a SEED when its core has two or
more non-monomial Z-irreducible factors and one of them carries a negative
coefficient. A factor is TORSION-ROOTED when it vanishes at a tuple of roots
of unity and TORSION-FREE otherwise; along a line (menus of powers of one
prime, cores univariate) torsion-rooted means "carries a cyclotomic factor",
and an IRREDUCIBLE univariate factor is torsion-free exactly when it is not
itself a cyclotomic polynomial. The plane census of explore_seed_torsion.py
asked, of every seed, whether ITS NEGATIVE FACTOR is torsion-free, with the
seed's other factors unconstrained -- and found the witnesses at size 6 of
the shape (1 + x)(A + yB), a cyclotomic cofactor beside a torsion-free
negative factor. Its univariate census asked a DIFFERENT question -- which
0/1 polynomials are reducible with NO cyclotomic factor at all -- and that
statistic's least degree, 12 at seven or nine terms, was then read as the
line's least degree for a torsion-free negative factor. The two questions
part exactly on the shape the plane witnesses have: a cyclotomic cofactor
times a torsion-free negative factor is reducible, carries a cyclotomic
factor, and is a seed whose negative factor is torsion-free. This file asks
the plane's question of the line.

THE HAND-ATTACK, on paper before any engine code.

  (1) SIZE 2 IS EXCLUDED. A size-2 core is 1 + m for a monomial m, which is
      1 + x^n in one variable after the lattice reduction of the parent
      file, and every factor of 1 + x^n is cyclotomic. So the least size
      with a torsion-free negative factor is at least 3.
  (2) SIZE 3 IS ATTAINED, BY HAND. (x^2 + x + 1)(x^3 - x + 1) = x^5 + x^4
      + x^3 - x^3 - x^2 - x + x^2 + x + 1 = 1 + x^4 + x^5. The cofactor
      x^3 - x + 1 is the plastic number's polynomial: irreducible (no
      rational root), of degree 3, hence not cyclotomic (the cyclotomic
      polynomials of odd degree are x - 1 and x + 1). As a menu: {2, 32,
      64} on the prime 2's line, core 1 + x^4 + x^5 -- a seed the
      three-member criterion finds in {2..64}, and outside every box the
      torsion cells swept, whose collinear menus reach exponent 5 only
      with the content x at exponent 1. So the least SIZE is 3, and this is a
      PROOF, not a census: (1) and (2) together. Ljunggren and Tverberg
      (a reducible 0/1 trinomial's non-cyclotomic part is irreducible or
      1) say that a trinomial seed's negative factor, when it is not
      cyclotomic, is always torsion-free: the theorem the parent file
      cited against four terms is the theorem that explains the witness.
  (3) FIVE TERMS, BY HAND. (x^4 + x^3 + x^2 + x + 1)(x^5 - x^4 + 1) =
      (x^9 + x^8 + x^7 + x^6 + x^5) - (x^8 + x^7 + x^6 + x^5 + x^4) +
      (x^4 + x^3 + x^2 + x + 1) = 1 + x + x^2 + x^3 + x^9. More generally
      x^{5k-1} = x^4 (mod Phi_5), so Phi_5 divides 1 + x + x^2 + x^3 +
      x^{5k-1} for every k >= 1, with cofactor 1 + x^4 (x - 1)(1 + x^5 +
      ... + x^{5(k-2)}) for k >= 2 -- negative at every k >= 2 (the
      coefficient of x^4 is -1). Whether that cofactor is irreducible and
      non-cyclotomic is a check per k, not a property: what the identity
      proves is that five terms hold a cyclotomic cofactor beside a
      NEGATIVE non-0/1 cofactor at every k >= 2.
  (4) THE DEGREE FLOOR. Along a line, what is the least degree of a 0/1
      polynomial with constant term 1 carrying a torsion-free negative
      factor? A reducible 0/1 polynomial of degree <= 4 has a factor of
      degree <= 2; a torsion-free negative irreducible factor of degree
      <= 2 would be x^2 + ax + b with a < 0 or b < 0, no positive real
      root (a factor of a 0/1 polynomial has none) and not cyclotomic:
      b = -1 gives a positive root, b = 1 needs a < 0 and a^2 < 4 for no
      real root, i.e. a = -1, which is Phi_6. So a degree-<= 4 witness
      would need the OTHER factor to be the torsion-free negative one, of
      degree 3 or 4 with a cofactor of degree 1 or 2 -- which the census
      settles, the candidate count being tiny. The prediction is that the
      floor is 5, attained by (2).
  (5) THE CONTROL. The parent file's census statistic -- reducible 0/1
      polynomials with NO cyclotomic factor, by degree -- is re-derived
      here from the same classification (every factor cyclotomic or not),
      and must reproduce its printed figures: none to degree 11, 24 at
      degree 12, 8 with seven terms and 16 with nine. That is the check
      that this file reads the same polynomials the parent did and that
      the two statistics differ by criterion and not by instrument.

THE RIG. C0 the two identities, checked exactly. C1 THE FULL LINE CENSUS:
every 0/1 polynomial with constant term 1 and degree <= 16 (2^15 per
degree) factored over Z, each irreducible factor tagged cyclotomic or not
and negative or not, and each polynomial classed IRREDUCIBLE / a PRODUCT
(two or more factors, none negative) / a ROOTED SEED (a negative factor,
every negative factor cyclotomic) / a FREE SEED (a torsion-free negative
factor). Per degree and per term count: the counts, and the least degree
per term count at which a free seed appears, with its first witness and
that witness's factorization. The parent's statistic (reducible with no
cyclotomic factor) is printed beside it as the control. C2 THE SPARSE
CENSUS by term count: every 0/1 polynomial with constant term 1 and 3, 4 or
5 terms to degree 30, classed the same way; for three terms the Ljunggren-
Tverberg statement is checked on every reducible one (the non-cyclotomic
part irreducible or 1). C3 THE PENTANOMIAL FAMILY: 1 + x + x^2 + x^3 +
x^{5k-1} for k = 2..12, the Phi_5 cofactor printed as irreducible /
reducible and cyclotomic-carrying / not. A rehearsal flag (--rehearse)
runs C1 to degree 10 and C2 to degree 14.

THE PREDICTIONS, FIXED BEFORE THE RUN -- every kill is a printed count.

  P1  The least degree of a free seed along the line is 5 (hand-attack
      (4)), attained at three terms by 1 + x^4 + x^5 and 1 + x + x^5; no
      free seed of degree <= 4.
  P2  Free seeds exist at EVERY term count from 3 to 9 within degree 16,
      and the least degree at five terms is <= 9 (hand-attack (3)); the
      least degree at seven terms is below 12.
  P3  THE CONTROL reproduces the parent's figures exactly: reducible with
      no cyclotomic factor, 0 to degree 11, 24 at degree 12 (8 at seven
      terms, 16 at nine).
  P4  Every reducible 0/1 trinomial to degree 30 has its non-cyclotomic
      part irreducible or 1 (Ljunggren, Tverberg), and the trinomial free
      seeds are exactly the trinomials whose non-cyclotomic part is
      negative.
  P5  The Phi_5 family's cofactor is irreducible and non-cyclotomic at
      k = 2, 3, 4 (seen in the preliminary probe); what happens at k >= 5
      is printed, not predicted.

  The KILLS are prints: a free seed of degree <= 4 kills P1; a term count
  in 3..9 with no free seed to degree 16 kills P2; a control figure off
  the parent's kills P3 and with it the comparability of the two census
  statistics; a reducible trinomial with a reducible non-cyclotomic part
  kills P4 -- which would contradict a theorem and so would first be read
  as an instrument error.

RESOURCE ENVELOPE. 65,535 factorizations of degree <= 16 (about 2 ms each,
~2.5 min), 31,900 sparse ones to degree 30 (~4 ms each, ~2 min), eleven
family members. Estimated five minutes, memory under 150 MB. Run: python
explore_seed_line_floor.py [--rehearse]

FINDINGS (the recorded run, 12 of 12 checks, 197.6 s; every figure below is
that run's print).

  F1  THE LEAST SIZE IS 3 AND THE LEAST DEGREE IS 5 (rule, exhaustive to
      degree 16 for the degree; the size by the proof in the hand-attack).
      No 0/1 polynomial of degree <= 4 is a free seed; degree 5 holds four
      -- 1 + x + x^5 = (x^2 + x + 1)(x^3 - x^2 + 1) and 1 + x^4 + x^5 at
      three terms, 1 + x + x^2 + x^5 = (x + 1)(x^4 - x^3 + x^2 + 1) and
      its reciprocal at four. The least degree per term count: 3 and 4
      terms at 5; 5 and 6 at 7 (1 + x + x^3 + x^4 + x^7 = (x^3 - x^2 + 1)
      Phi_5(x)); 7 and 8 at 9; 9 at 10; 10 at 11; 11 at 12; 12 at 13; 13
      and 14 at 15; 15 at 16 -- every term count from 3 to 15 reached
      within degree 16, and nothing about the degree-12 floor of the
      parent's statistic survives in the seed question: its seven-term
      witness at degree 12 is preceded by a seven-term free seed at
      degree 9, (x^3 - x^2 + 1)(1 + x + ... + x^6).
  F2  FREE IS THE GENERIC KIND (rule in range). By degree: free / rooted
      / product among the reducible 0/1 polynomials -- 4 / 3 / 1 at
      degree 5, 18 / 6 / 6 at 7, 117 / 35 / 29 at 10, 429 / 89 / 113 at
      12, 7,966 / 767 / 598 at 16; from degree 7 on the free seeds
      outnumber the rooted at every degree, and at 16 they are 85% of
      everything reducible. The picture the plane census left -- every
      negative factor met is an absorbed cyclotomic, the torsion-free
      kind a rarity first reached at size 6 -- was a statement about the
      parent's statistic and about boxes whose collinear menus stop at
      exponent 5 with the content at exponent 1; along the line, past
      degree 4, the rooted kind is the exception.
  F3  THE CONTROL REPRODUCES (check). Reducible with no cyclotomic factor:
      0 to degree 11; 24 at degree 12, 8 at seven terms and 16 at nine;
      36, 24, 106, 140 at degrees 13 to 16. The two census statistics
      differ by criterion and not by instrument.
  F4  THE SPARSE CENSUS TO DEGREE 30 (rule, exhaustive in range). Three
      terms: 98 free seeds over the 435 trinomials, first at degree 5,
      and every reducible trinomial's non-cyclotomic part is irreducible
      or 1 (Ljunggren, Tverberg, re-verified), so a trinomial is a free
      seed exactly when that part is negative -- 98 = 98. Four terms:
      first at degree 5, 1,580 over 4,060 quadrinomials by degree 30.
      Five terms: first at degree 7, 2,838 over 27,405 pentanomials.
  F5  THE PHI_5 FAMILY (property for the divisibility and the sign;
      observation to k = 12 for the rest). Phi_5 divides 1 + x + x^2 +
      x^3 + x^{5k-1} at every k, the cofactor negative at every k >= 2,
      and that cofactor is irreducible and non-cyclotomic at every
      k = 2..12 (degrees 9 to 59).

  TIERS. F1's size floor is proved (size 2 excluded, size 3 attained);
  its degree floor is exhaustive to 16, and the per-term-count table is a
  rule in that range. F2 rule in range. F3 a check. F4 rule, exhaustive
  to degree 30 at three, four and five terms. F5 as stated.

  RUN RECORD. Rehearsal (degree 10, sparse to 14): census stages 0.6 s
  and 1.2 s, every content check green, the total unprinted because the
  tally line crashed on a sympy boolean and was fixed before the full
  run; the full run 197.6 s, the full census 93.0 s and the sparse one 103.3 s of
  it; peak memory not measured, nothing allocated beyond sympy's
  factoring. The two identities of the hand-attack and the degree-9
  pentanomial were first seen in a preliminary probe over degree <= 20
  that read the plane criterion against the parent's census; the slate
  was frozen on them before this file ran, and every figure above is
  this file's own print. Python 3.12, sympy.
"""

import itertools
import os
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sympy
from sympy import Poly, ZZ, symbols, totient

x = symbols("x")
REHEARSE = "--rehearse" in sys.argv
D_FULL = 10 if REHEARSE else 16
D_SPARSE = 14 if REHEARSE else 30

CHECKS = []


def check(name, ok):
    ok = bool(ok)
    CHECKS.append((name, ok))
    print(("  PASS  " if ok else "  FAIL  ") + name)


# --- cyclotomic recognition -------------------------------------------------
# An irreducible factor of degree d is cyclotomic iff it equals Phi_m for some
# m with phi(m) = d. m <= 6 d^2 + 100 covers every d <= 30 comfortably.
_CYC = {}


def _cyc_of_degree(d):
    if d not in _CYC:
        _CYC[d] = [Poly(sympy.cyclotomic_poly(m, x), x, domain=ZZ)
                   for m in range(1, 6 * d * d + 100) if totient(m) == d]
    return _CYC[d]


def is_cyclotomic(f):
    return any(f == g for g in _cyc_of_degree(f.degree()))


def classify(exps):
    """exps: sorted exponents including 0. Returns (cls, factors) where cls is
    'irr', 'prod', 'rooted', 'free', and factors is a list of (poly, mult,
    is_cyc, is_neg)."""
    P = Poly(sum(x ** e for e in exps), x, domain=ZZ)
    fl = P.factor_list()[1]
    facts = []
    nfac = 0
    for f, m in fl:
        if f.degree() == 0:
            continue
        nfac += m
        facts.append((f, m, is_cyclotomic(f), min(f.all_coeffs()) < 0))
    if nfac < 2:
        return "irr", facts
    negs = [t for t in facts if t[3]]
    if not negs:
        return "prod", facts
    if any(not t[2] for t in negs):
        return "free", facts
    return "rooted", facts


def fmt(facts):
    return " * ".join(f"({sympy.sstr(f.as_expr())})" + (f"^{m}" if m > 1 else "")
                      for f, m, _, _ in facts)


def main():
    t0 = time.time()
    print(f"explore_seed_line_floor.py  rehearse={REHEARSE}  "
          f"full census to degree {D_FULL}, sparse to {D_SPARSE}")

    # C0 -- the identities, exactly
    print("\nC0  THE IDENTITIES")
    lhs = Poly((x ** 2 + x + 1) * (x ** 3 - x + 1), x, domain=ZZ)
    check("Phi_3 * (x^3 - x + 1) = 1 + x^4 + x^5",
          lhs == Poly(1 + x ** 4 + x ** 5, x, domain=ZZ))
    lhs = Poly((x ** 4 + x ** 3 + x ** 2 + x + 1) * (x ** 5 - x ** 4 + 1), x, domain=ZZ)
    check("Phi_5 * (x^5 - x^4 + 1) = 1 + x + x^2 + x^3 + x^9",
          lhs == Poly(1 + x + x ** 2 + x ** 3 + x ** 9, x, domain=ZZ))
    check("x^3 - x + 1 is irreducible and not cyclotomic",
          Poly(x ** 3 - x + 1, x, domain=ZZ).is_irreducible
          and not is_cyclotomic(Poly(x ** 3 - x + 1, x, domain=ZZ)))

    # C1 -- the full line census
    print(f"\nC1  THE FULL LINE CENSUS, degree <= {D_FULL}")
    least = {}          # term count -> (degree, exps, facts)
    per_deg = {}        # degree -> dict cls -> count
    ctrl = {}           # degree -> dict terms -> count of reducible w/o cyc
    free_by_terms = {}  # (degree, terms) -> count
    t1 = time.time()
    for d in range(1, D_FULL + 1):
        cnt = {"irr": 0, "prod": 0, "rooted": 0, "free": 0}
        for mask in range(2 ** (d - 1)):
            exps = [0] + [i + 1 for i in range(d - 1) if mask >> i & 1] + [d]
            cls, facts = classify(exps)
            cnt[cls] += 1
            k = len(exps)
            if cls != "irr" and not any(t[2] for t in facts):
                ctrl.setdefault(d, {}).setdefault(k, 0)
                ctrl[d][k] += 1
            if cls == "free":
                free_by_terms[(d, k)] = free_by_terms.get((d, k), 0) + 1
                if k not in least:
                    least[k] = (d, exps, facts)
        per_deg[d] = cnt
        c = ctrl.get(d, {})
        print(f"  degree {d:2d}: irr {cnt['irr']:5d}  prod {cnt['prod']:4d}  "
              f"rooted {cnt['rooted']:4d}  free {cnt['free']:4d}   | "
              f"reducible with no cyclotomic factor: "
              f"{sum(c.values())} {dict(sorted(c.items())) if c else ''}")
    print(f"  ({time.time() - t1:.1f} s)")
    print("  least degree of a FREE seed per term count:")
    for k in sorted(least):
        d, exps, facts = least[k]
        print(f"    {k:2d} terms: degree {d:2d}  exps {exps}  = {fmt(facts)}")
    print("  free seeds by (degree, terms):")
    for d in range(1, D_FULL + 1):
        row = {k: v for (dd, k), v in sorted(free_by_terms.items()) if dd == d}
        if row:
            print(f"    degree {d:2d}: {row}")

    min_free_deg = min(d for d, c in per_deg.items() if c["free"]) if any(
        c["free"] for c in per_deg.values()) else None
    check("P1  least degree of a free seed is 5", min_free_deg == 5)
    check("P1  both 1 + x^4 + x^5 and 1 + x + x^5 are free seeds at degree 5",
          classify([0, 4, 5])[0] == "free" and classify([0, 1, 5])[0] == "free")
    if not REHEARSE:
        check("P2  free seeds at every term count 3..9 within degree 16",
              all(k in least for k in range(3, 10)))
        check("P2  least degree at five terms <= 9 and at seven terms < 12",
              least.get(5, (99,))[0] <= 9 and least.get(7, (99,))[0] < 12)
        below = sum(sum(c.values()) for d, c in ctrl.items() if d <= 11)
        at12 = ctrl.get(12, {})
        check("P3  control: reducible with no cyclotomic factor, 0 to degree 11",
              below == 0)
        check("P3  control: 24 at degree 12, 8 at seven terms and 16 at nine",
              sum(at12.values()) == 24 and at12.get(7) == 8 and at12.get(9) == 16)

    # C2 -- the sparse census by term count
    print(f"\nC2  THE SPARSE CENSUS, 3..5 terms to degree {D_SPARSE}")
    t2 = time.time()
    lj_bad = []
    tri_free = tri_negpart = 0
    for k in (3, 4, 5):
        least_k = None
        by_deg = {}
        n = 0
        for inner in itertools.combinations(range(1, D_SPARSE), k - 2):
            for d in range(max(inner) + 1 if inner else 1, D_SPARSE + 1):
                exps = [0] + list(inner) + [d]
                n += 1
                cls, facts = classify(exps)
                if cls == "free":
                    by_deg[d] = by_deg.get(d, 0) + 1
                    if least_k is None or d < least_k[0]:
                        least_k = (d, exps, facts)
                if k == 3 and cls != "irr":
                    noncyc = [t for t in facts if not t[2]]
                    if sum(m for _, m, _, _ in noncyc) > 1:
                        lj_bad.append((exps, facts))
                    if noncyc and noncyc[0][3]:
                        tri_negpart += 1
                    if cls == "free":
                        tri_free += 1
        print(f"  {k} terms: {n} polynomials; free seeds by degree "
              f"{dict(sorted(by_deg.items()))}")
        if least_k:
            d, exps, facts = least_k
            print(f"    least: degree {d}  exps {exps}  = {fmt(facts)}")
        else:
            print("    least: none in range")
    print(f"  ({time.time() - t2:.1f} s)")
    check("P4  Ljunggren-Tverberg: every reducible trinomial's non-cyclotomic "
          "part irreducible or 1", not lj_bad)
    check("P4  trinomial free seeds = trinomials with a negative non-cyclotomic "
          f"part ({tri_free} = {tri_negpart})", tri_free == tri_negpart)
    for e, f in lj_bad[:5]:
        print("    Ljunggren violation?", e, fmt(f))

    # C3 -- the Phi_5 family
    print("\nC3  THE PHI_5 FAMILY  1 + x + x^2 + x^3 + x^(5k-1)")
    phi5 = Poly(x ** 4 + x ** 3 + x ** 2 + x + 1, x, domain=ZZ)
    fam_ok = True
    for k in range(2, 13):
        P = Poly(1 + x + x ** 2 + x ** 3 + x ** (5 * k - 1), x, domain=ZZ)
        q, r = P.div(phi5)
        neg = min(q.all_coeffs()) < 0
        qf = [(f, m, is_cyclotomic(f), min(f.all_coeffs()) < 0)
              for f, m in q.factor_list()[1] if f.degree() > 0]
        irr = len(qf) == 1 and qf[0][1] == 1
        cyc = any(t[2] for t in qf)
        tf_neg = any((not t[2]) and t[3] for t in qf)
        print(f"  k={k:2d} degree {5 * k - 1:2d}: remainder zero {r.is_zero}, "
              f"cofactor negative {neg}, irreducible {irr}, carries cyclotomic "
              f"{cyc}, torsion-free negative factor {tf_neg}"
              + ("" if irr else f"  = {fmt(qf)}"))
        fam_ok &= r.is_zero and neg
        if k <= 4:
            fam_ok &= irr and not cyc
    check("P5  Phi_5 divides every member with a negative cofactor, irreducible "
          "and non-cyclotomic at k = 2, 3, 4", fam_ok)

    print(f"\n{sum(ok for _, ok in CHECKS)} of {len(CHECKS)} checks pass; "
          f"{time.time() - t0:.1f} s")
    sys.exit(0 if all(ok for _, ok in CHECKS) else 1)


if __name__ == "__main__":
    main()
