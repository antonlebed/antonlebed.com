"""explore_pentanomial_reciprocal.py -- does any five-term 0/1 polynomial in
one variable carry a NON-CYCLOTOMIC RECIPROCAL factor? The census behind the
one open case of the pentanomial question, beside two arithmetic checks of the
hand derivation that reduced the question to that case.

THE QUESTION. Filaseta and Solan (Math. Scand. 84, 1999, Theorem 1) proved
that a 0/1 pentanomial f = 1 + x^a + x^b + x^c + x^n with its irreducible
reciprocal factors removed is 1 or irreducible, and stated that they did not
know whether the same holds with "reciprocal" replaced by "cyclotomic",
proving that replacement only when n is exactly one of 2a, 2b, 2c, a+b, a+c,
b+c. Filaseta (Number Theory in Progress, 1999) restates the replacement as
unknown. So "every reducible 0/1 pentanomial has a cyclotomic factor", the
statement explore_pentanomial_free.py found empty of counterexamples to
degree 70, is the weaker half of that open question (the question also
forbids a cyclotomic factor beside two non-cyclotomic ones), and both
reduce to one case: a reciprocal irreducible factor g of f that is not
cyclotomic. This rig asks whether such a
g occurs in ANY 0/1 pentanomial to degree 70, reducible-with-cyclotomic-factor
ones included, which the earlier census never looked at.

THE HAND-ATTACK, before any engine code.

  (1) The non-reciprocal part (the Filaseta--Ford--Konyagin criterion, quoted
      as Lemma 2 of Filaseta--Kalogirou, arXiv 2508.12242, and Lemma 2.1 of
      Filaseta--Finch--Nicol 2006): it is reducible iff some w in Z[x] other
      than +-f, +-f~ has w w~ = f f~. The coefficient of x^n in f f~ is the sum
      of squared coefficients, 5, and w(1)^2 = 25, so |sum w_i| = 5 = sum
      w_i^2 forces w = +-(0/1 pentanomial) of degree n with w(0) = 1; the
      coefficient of x^(n+d) counts ordered exponent pairs at difference d, so
      w w~ = f f~ says the exponent sets of w and f have the same DIFFERENCE
      MULTISET. Two 5-subsets of [0, n] containing 0 and n with the same
      difference multiset are congruent (the five-point turnpike lemma: in gap
      coordinates the second-largest difference fixes the smaller end gap
      after reflection, the third-largest splits into two shapes, and each of
      the three shape pairs collapses by a sum or a minimum comparison), so w
      is f or f~ and the non-reciprocal part is 1 or irreducible. That is
      Filaseta--Solan's theorem re-derived by their own method; the lemma is
      checked here by brute force (F1).
  (2) The reciprocal case. A non-cyclotomic reciprocal irreducible g dividing
      f divides f~ and so D = f~ - f = x^(n-c) + x^(n-b) + x^(n-a) - x^a - x^b
      - x^c. The involution e -> n - e on {a, b, c} decides the cancellation:
      a two-cycle leaves D = x^e(x^(n-2e) - 1) up to sign; a single fixed point
      e = n/2 leaves four terms that factor as (x^v - 1)(x^i +- x^j) up to
      sign; in either case g is cyclotomic. Those are Filaseta--Solan's six
      special relations. The two cases left OPEN: no relation at all (six-term
      D, anti-reciprocal) and f itself reciprocal (D = 0, f = x^m G(x + 1/x)
      with G monic of degree m = n/2 and G(2) = 5).
  (3) Roots. f > 0 on x > 0. A non-cyclotomic monic reciprocal g has a root
      alpha with |alpha| > 1 whose inverse is also a root of f: from
      f(1/alpha) = 0, |alpha|^a <= 4; from f(alpha) = 0, |alpha|^(n-c) <= 4.
      No finiteness follows without a Lehmer-type bound.
  (4) Finiteness in principle: Bombieri--Zannier (as quoted by
      Filaseta--Kalogirou, Theorem 3) puts the exponent vectors of a
      pentanomial with a non-cyclotomic reciprocal factor on finitely many
      hyperplanes with coefficients bounded by a computable constant, so the
      open case is a finite list nobody has written down.

THE RIG. For every canonical (a, b, c, n) with n <= NMAX (reciprocal pairs
once, as in explore_pentanomial_free.py): factor f over Z (python-flint) and
classify each irreducible factor as cyclotomic, reciprocal non-cyclotomic, or
non-reciprocal; count factors with multiplicity. Print per degree the number of
pentanomials with two or more non-reciprocal factors and the number with a
non-cyclotomic reciprocal factor; print every polynomial of the second kind
whole with its factorization and which of the six relations n = 2a, 2b, 2c,
a+b, a+c, b+c hold (none = the generic open case; n = 2b with n = a+c = the
reciprocal open case). Separately, brute-force the turnpike lemma: for N <=
TMAX, group every 5-subset of [0, N] containing 0 and N by its difference
multiset and count classes holding two non-congruent sets. Controls: the
six-term degree-13 witness reads two non-reciprocal factors; (x^2 + 3x + 1)
(x^2 + 1) reads one non-cyclotomic reciprocal and one cyclotomic factor; the
six-subset census at N = 13 finds the homometric pair {0,1,2,6,10,13} and
{0,1,4,5,11,13} (the exponent sets of the degree-13 witness and of its
criterion partner).

THE PREDICTIONS, FIXED BEFORE THE RUN -- each kill a printed count.

  F0  CONTROLS as listed print as listed.
  F1  THE TURNPIKE LEMMA: 0 non-congruent homometric 5-subset classes for
      every N <= TMAX; the 6-subset control at N = 13 prints at least one.
  F2  FILASETA--SOLAN RE-VERIFIED: 0 pentanomials to NMAX with two or more
      non-reciprocal irreducible factors counted with multiplicity.
  F3  THE OPEN CASE. As first written: 0 pentanomials to NMAX with a
      non-cyclotomic reciprocal factor, held loosely. The degree-20 rehearsal
      showed that print mis-specified: an IRREDUCIBLE reciprocal pentanomial
      is its own non-cyclotomic reciprocal factor and 35 of them sit below
      degree 20. The question is a PROPER factor, so F3 was split before the
      full run, the rehearsal having also shown the split's first row:
      F3a  irreducible reciprocal pentanomials: counted, not read.
      F3b  REDUCIBLE pentanomials with a non-cyclotomic reciprocal factor:
           some exist (the rehearsal saw them from degree 10, every one
           reciprocal itself with a cyclotomic cofactor). Prediction for the
           full run: every F3b specimen is reciprocal (relations 2b and a+c)
           and carries a cyclotomic factor -- 0 in the generic case (no
           relation), 0 in any single-relation case, 0 with cyc = 0 (the
           earlier census's free-outright count). A generic-case specimen
           would be the shape of a witness for the open question and the
           more informative print.
  F4  FILASETA--SOLAN'S OWN QUESTION, added after the rehearsal beside the
      F3 split: 0 pentanomials to NMAX whose non-cyclotomic part has two or
      more irreducible factors with multiplicity -- the cyclotomic version
      of their theorem holding to degree NMAX. This is the statement the two
      censuses together decide, printed directly rather than inferred from
      F2 and F3b.
  F5  THE RECIPROCAL FAMILY, added after an ad hoc read of the F3b
      specimens and so a record of that read rather than a prediction: over
      the reciprocal pentanomials 1 + x^a + x^m + x^(2m-a) + x^(2m), m <=
      NMAX/2, print the count, the reducible count, the count with a
      non-cyclotomic factor, the largest number of non-cyclotomic factors
      in one polynomial, how many cyclotomic factors ride beside it, which
      Phi_m occur, and the value at x = 1 of the non-cyclotomic factor (the
      cofactor of value 5 or the factor of value 1: f(1) = 5 is prime).

RESOURCE: the same 458,745 factorizations as the earlier census, about 2.5
minutes at NMAX = 70; the turnpike census at TMAX = 30 is C(29, 3) = 3,654
subsets per N, negligible. Memory negligible.

RUN RECORD (NMAX = 70, TMAX = 30, 135.5 s, 6/6 checks pass; the degree-20
rehearsal that forced the F3 split is described under F3).

  F0  Controls: the six-term witness cyc 0 rnc 0 nr 2; (x^2+3x+1)(x^2+1)
      cyc 1 rnc 1 nr 0; the 6-subsets of [0, 13] hold one non-congruent
      homometric class and it is the witness pair.
  F1  THE TURNPIKE LEMMA HOLDS TO N = 30 (rule, exhaustive): 0 non-congruent
      homometric 5-subset classes at every N.
  F2  FILASETA--SOLAN RE-VERIFIED TO DEGREE 70: 0 of 458,745 canonical
      pentanomials have two or more non-reciprocal irreducible factors.
  F3a 290 irreducible reciprocal pentanomials, not read.
  F3b 269 REDUCIBLE PENTANOMIALS CARRY A NON-CYCLOTOMIC RECIPROCAL FACTOR,
      least degree 10 (1 + x^2 + x^5 + x^8 + x^10 = Phi_6 times a reciprocal
      octic), and EVERY ONE IS A RECIPROCAL PENTANOMIAL WITH A CYCLOTOMIC
      COFACTOR: relation pattern 2b with a+c in all 269; generic case 0,
      single-relation cases 0, with no cyclotomic factor 0. Per degree from
      1 at 10 to 23 at 66, even degrees only, as reciprocity forces.
  F4  THE NON-CYCLOTOMIC PART IS 1 OR IRREDUCIBLE THROUGHOUT (rule,
      exhaustive to degree 70): 0 pentanomials whose non-cyclotomic part has
      two or more irreducible factors with multiplicity. That is the
      cyclotomic version of Filaseta--Solan's theorem, their open question,
      holding on the whole census.
  F5  The reciprocal family to m = 35: 595 polynomials, 303 reducible, 269
      with a non-cyclotomic factor, never two; beside it 1 cyclotomic factor
      in 191, 2 in 65, 3 in 13; the Phi_m occurring are m = 5 (166), 6 (68),
      12 (49), 10 (34), 15 (11), 24 (10), 18 (7), 20 (4), 36 (4), 25 (3), 30
      (2), 42 (1), 48 (1), every m a multiple of 5 or of 6 (the two ways
      five roots of unity sum to zero, by Mann's bound: a five-term minimal
      sum, or a two-term beside a three-term), 42 among them, so the law
      is not 5-smoothness;
      the non-cyclotomic factor has value 1 at x = 1 in 169 cases and 5 in
      100, so the value-1 factor is not the cyclotomic one in general and
      the "value 1 forces cyclotomic" route is dead.

  What the print supports: to degree 70 the open question of Filaseta and
  Solan holds, and the only place a PROPER non-cyclotomic reciprocal factor
  of a 0/1 pentanomial has been seen is inside a reciprocal pentanomial
  (an irreducible reciprocal pentanomial is its own, F3a), always
  alone among the non-cyclotomic factors and always beside a Phi_m with m
  a multiple of 5 or of 6. A witness for the question would be either a non-reciprocal
  pentanomial sharing a non-cyclotomic factor with its reciprocal, which
  the census has never seen, or a reciprocal pentanomial whose
  x + 1/x form G splits into two non-cyclotomic-lift factors, which 595
  members of the family never did. Neither is forbidden by anything read.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import sys
import time
from collections import Counter, defaultdict
from itertools import combinations

from flint import fmpz_poly

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 70
TMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 30


def poly_of(exps, n):
    co = [0] * (n + 1)
    for e in exps:
        co[e] = 1
    co[0] = 1
    co[n] = 1
    return fmpz_poly(co)


def is_reciprocal(g):
    co = [int(c) for c in g.coeffs()]
    return co == co[::-1] or co == [-c for c in co[::-1]]


def classify(f):
    """Return (cyc, rnc, nr, fac): counts with multiplicity of cyclotomic,
    reciprocal non-cyclotomic and non-reciprocal irreducible factors."""
    _, fac = f.factor()
    cyc = rnc = nr = 0
    for g, m in fac:
        if g.degree() == 0:
            continue
        if g.is_cyclotomic():
            cyc += m
        elif is_reciprocal(g):
            rnc += m
        else:
            nr += m
    return cyc, rnc, nr, fac


def show(fac):
    return " * ".join(f"({g})^{m}" if m > 1 else f"({g})" for g, m in fac
                      if g.degree() > 0)


def relations(a, b, c, n):
    names = {"2a": n == 2 * a, "2b": n == 2 * b, "2c": n == 2 * c,
             "a+b": n == a + b, "a+c": n == a + c, "b+c": n == b + c}
    held = [k for k, v in names.items() if v]
    return held if held else ["none"]


def diff_multiset(s):
    return tuple(sorted(y - x for x, y in combinations(sorted(s), 2)))


def homometric_classes(N, k):
    """Classes of k-subsets of [0, N] containing 0 and N, grouped by
    difference multiset; return the classes holding two non-congruent sets."""
    groups = defaultdict(list)
    for mid in combinations(range(1, N), k - 2):
        s = (0,) + mid + (N,)
        groups[diff_multiset(s)].append(s)
    bad = []
    for d, sets in groups.items():
        # a class is bad when it holds a set that is neither its first
        # member nor that member's reflection
        base = sets[0]
        refl = tuple(sorted(N - x for x in base))
        others = [s for s in sets if s != base and s != refl]
        if others:
            bad.append((d, sets))
    return bad


def main():
    checks = []

    def check(label, ok):
        checks.append(ok)
        print(("PASS " if ok else "FAIL ") + label)

    # F0 controls
    c6 = fmpz_poly([1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1])
    cyc6, rnc6, nr6, fac6 = classify(c6)
    print(f"control six-term degree 13: cyc {cyc6} rnc {rnc6} nr {nr6}  {show(fac6)}")
    cr = fmpz_poly([1, 3, 2, 3, 1])
    cycr, rncr, nrr, facr = classify(cr)
    print(f"control (x^2+3x+1)(x^2+1):  cyc {cycr} rnc {rncr} nr {nrr}  {show(facr)}")
    bad6 = homometric_classes(13, 6)
    pair = {(0, 1, 2, 6, 10, 13), (0, 1, 4, 5, 11, 13)}
    found = any(pair <= set(sets) for _, sets in bad6)
    print(f"control 6-subsets of [0,13]: {len(bad6)} non-congruent homometric classes;"
          f" the witness pair present: {found}")
    check("F0 controls: nr 2 for the six-term witness, rnc 1 and cyc 1 for the"
          " quartic, the six-point homometric pair found",
          nr6 == 2 and rncr == 1 and cycr == 1 and found)

    # F1 turnpike lemma
    print(f"\nF1 five-point turnpike lemma, N <= {TMAX}")
    worst = 0
    for N in range(4, TMAX + 1):
        bad = homometric_classes(N, 5)
        worst = max(worst, len(bad))
        if bad:
            for d, sets in bad:
                print(f"   N={N}: non-congruent homometric 5-sets {sets}")
    print(f"   non-congruent homometric 5-subset classes, all N <= {TMAX}: {worst}")
    check("F1 no non-congruent homometric 5-subsets", worst == 0)

    # F2, F3 the census
    t0 = time.time()
    two_nr = {}
    with_rnc = {}
    irred_rec = {}
    noncyc2 = {}
    specimens = []
    tuples = 0
    for n in range(4, NMAX + 1):
        t2 = t3 = t3a = t4 = 0
        for a, b, c in combinations(range(1, n), 3):
            if (a, b, c) > (n - c, n - b, n - a):
                continue
            tuples += 1
            cyc, rnc, nr, fac = classify(poly_of((a, b, c), n))
            if nr >= 2:
                t2 += 1
            if rnc + nr >= 2:
                t4 += 1
            if rnc >= 1:
                if cyc + rnc + nr == 1:
                    t3a += 1
                    continue
                t3 += 1
                specimens.append(((a, b, c, n), cyc, rnc, nr, fac))
        two_nr[n] = t2
        with_rnc[n] = t3
        irred_rec[n] = t3a
        noncyc2[n] = t4
        print(f"  degree {n}: two-nonreciprocal {t2}, reducible with reciprocal-noncyclotomic"
              f" {t3}, irreducible reciprocal {t3a}, {time.time() - t0:.0f} s",
              file=sys.stderr, flush=True)
    wall = time.time() - t0
    print(f"\n{tuples} canonical pentanomials to degree {NMAX}, {wall:.1f} s")
    tot2 = sum(two_nr.values())
    tot3 = sum(with_rnc.values())
    print(f"F2 pentanomials with two or more non-reciprocal factors: {tot2}")
    check("F2 Filaseta--Solan re-verified: 0 with two non-reciprocal factors", tot2 == 0)
    print(f"F3a irreducible reciprocal pentanomials: {sum(irred_rec.values())}")
    print(f"F3b REDUCIBLE pentanomials with a non-cyclotomic reciprocal factor: {tot3}")
    if specimens:
        least = min(s[0][3] for s in specimens)
        print(f"   least degree {least}; per degree: "
              + " ".join(f"{n}:{with_rnc[n]}" for n in range(4, NMAX + 1) if with_rnc[n]))
        rel = Counter()
        for (a, b, c, n), cyc, rnc, nr, fac in specimens:
            r = relations(a, b, c, n)
            rel[",".join(r)] += 1
        print("   relation patterns: " + "; ".join(f"{k}: {v}" for k, v in rel.most_common()))
        for (a, b, c, n), cyc, rnc, nr, fac in specimens[:40]:
            print(f"   1+x^{a}+x^{b}+x^{c}+x^{n} [{','.join(relations(a, b, c, n))}]"
                  f" cyc {cyc} rnc {rnc} nr {nr} = {show(fac)}")
        if len(specimens) > 40:
            print(f"   ... {len(specimens) - 40} more")
        generic = sum(1 for s_ in specimens if relations(*s_[0]) == ["none"])
        single = sum(1 for s_ in specimens if len(relations(*s_[0])) == 1
                     and relations(*s_[0]) != ["none"])
        nocyc = sum(1 for s_ in specimens if s_[1] == 0)
        print(f"   generic (no relation): {generic}; exactly one relation: {single};"
              f" reciprocal f: {len(specimens) - generic - single};"
              f" with no cyclotomic factor: {nocyc}")
        check("F3b every specimen reciprocal (2b, a+c) with a cyclotomic factor",
              generic == 0 and single == 0 and nocyc == 0)
    else:
        check("F3b every specimen reciprocal (2b, a+c) with a cyclotomic factor", True)
    tot4 = sum(noncyc2.values())
    print(f"F4 pentanomials whose NON-CYCLOTOMIC part has two or more irreducible"
          f" factors (with multiplicity): {tot4}")
    check("F4 the non-cyclotomic part is 1 or irreducible throughout", tot4 == 0)

    # F5 the reciprocal family
    print(f"\nF5 reciprocal pentanomials 1+x^a+x^m+x^(2m-a)+x^(2m), m <= {NMAX // 2}")
    rec_total = rec_red = rec_nc = 0
    max_rnc = 0
    beside = Counter()
    phis = Counter()
    val1 = Counter()
    for m in range(2, NMAX // 2 + 1):
        for a in range(1, m):
            rec_total += 1
            cyc, rnc, nr, fac = classify(poly_of((a, m, 2 * m - a), 2 * m))
            if cyc + rnc + nr < 2:
                continue
            rec_red += 1
            if rnc + nr == 0:
                continue
            rec_nc += 1
            max_rnc = max(max_rnc, rnc + nr)
            beside[cyc] += 1
            for g, k in fac:
                if g.degree() > 0 and g.is_cyclotomic():
                    idx = next(i for i in range(1, 40 * g.degree() + 3)
                               if fmpz_poly.cyclotomic(i) == g)
                    phis[idx] += k
                elif g.degree() > 0:
                    val1[int(g(1))] += k
    print(f"   {rec_total} reciprocal pentanomials, {rec_red} reducible,"
          f" {rec_nc} with a non-cyclotomic factor, at most {max_rnc} such factor(s) each")
    print("   cyclotomic factors beside it: "
          + ", ".join(f"{c} cyclotomic in {k}" for c, k in sorted(beside.items())))
    print("   Phi_m occurring (m: count): "
          + ", ".join(f"{m_}: {k}" for m_, k in sorted(phis.items())))
    print("   value at 1 of the non-cyclotomic factor: "
          + ", ".join(f"{v}: {k}" for v, k in sorted(val1.items())))
    check("F5 no reciprocal pentanomial holds two non-cyclotomic factors", max_rnc <= 1)
    print(f"\n{sum(checks)}/{len(checks)} checks pass")


if __name__ == "__main__":
    main()
