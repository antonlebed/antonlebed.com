"""explore_pentanomial_free.py -- is any five-term 0/1 polynomial in one
variable reducible over Z with NO cyclotomic factor at all? An exact
census to degree 70, past the degree-16 one behind the menu-collision
corpus's size-5 front (explore_seed_torsion.py F4).

THE QUESTION. A 0/1 pentanomial is 1 + x^a + x^b + x^c + x^n with
0 < a < b < c < n. Call it FREE OUTRIGHT when it factors nontrivially over
Z and no irreducible factor is a cyclotomic polynomial. At four terms and
fewer, none exists at any degree: a reducible 0/1 trinomial's
non-cyclotomic part is irreducible (Ljunggren, Tverberg) and a reducible
0/1 quadrinomial carries a cyclotomic factor (Mills), so a free-outright
polynomial needs a nontrivial factorization with no cyclotomic factor,
which those theorems exclude. At six terms the least degree is 13
(x^13 + x^10 + x^6 + x^2 + x + 1 = (x^5 + x^2 + 1)(x^8 - x^3 + x + 1)) and
at seven it is 12. Five terms sit between a theorem and a witness with a
census reaching degree 16 and nothing past it. The question is whether the
five-term column is EMPTY (a theorem candidate, one term past Mills) or
holds a witness at some degree the old census never reached.

THE HAND-ATTACK, before any engine code.

  (1) A free-outright pentanomial f = g h with both g and h of degree >= 1,
      neither cyclotomic. f(1) = 5, so {g(1), h(1)} = {1, 5} or {-1, -5}
      up to the sign convention of monic factors; f(-1) is in {-3..5} and
      odd, so neither factor vanishes at -1, consistent with no
      cyclotomic factor.
  (2) The non-reciprocal part. Schinzel's reducibility theory for
      lacunary polynomials makes the non-reciprocal part of a 0/1
      polynomial with few terms irreducible for almost all exponent
      choices, and at three terms outright (Ljunggren, Tverberg). If the
      non-reciprocal part of every 0/1 pentanomial is irreducible, a
      witness must carry a RECIPROCAL non-cyclotomic factor, and both
      factors of a reciprocal 0/1 pentanomial (exponents {0, a, n/2,
      n - a, n}) would be reciprocal. That is the shape to look at in any
      witness the census prints: is a factor self-reciprocal.
  (3) Multiplicity. f = g^2 counts as reducible; a squarefree check is
      part of the read (the census prints the factorization whole).
  (4) Symmetry. f and its reciprocal x^n f(1/x) share every property
      asked here, so each pair is factored once and counted once; the
      exponent tuple (a, b, c, n) is canonical when (a, b, c) <=
      (n - c, n - b, n - a) lexicographically.
  (5) The cyclotomic test is exact: flint's is_cyclotomic on each
      irreducible factor (an irreducible monic integer polynomial is
      cyclotomic iff it equals some Phi_m, which is what the test
      decides).

THE RIG. For every canonical (a, b, c, n) with n <= 120: factor over Z
(python-flint 0.9.0, fmpz_poly.factor); if the factorization has two or
more irreducible factors counting multiplicity, test each for
cyclotomicity; record REDUCIBLE-WITH-CYCLOTOMIC or FREE-OUTRIGHT. Print,
per degree, the count of reducible pentanomials and the count free
outright; print every free-outright witness whole with its factors and
whether each factor is self-reciprocal; print the least free-outright
degree if any. Controls: the known seven-term and six-term least witnesses
must read FREE-OUTRIGHT under the same classifier, and Phi_5(x)(x^3 - x^2
+ 1) = 1 + x + x^3 + x^4 + x^7 must read REDUCIBLE-WITH-CYCLOTOMIC.

THE PREDICTIONS, FIXED BEFORE THE RUN -- each kill a printed count.

  F0  CONTROLS: the two free-outright controls print FREE and the
      cyclotomic control prints ROOTED; degrees <= 16 print 0 free
      outright (the old census re-derived).
  F1  THE COLUMN. Prediction, held loosely: 0 free-outright pentanomials
      to degree 120. The alternative is a witness at some degree in
      17..120, and the prediction is the one this file was written to
      test, not to confirm: a single witness closes the front as an
      exhibit and the count of them per degree is then the finding.
  F2  THE SHAPE, read only if F1 prints a witness: whether the witness
      carries a self-reciprocal non-cyclotomic factor (the route (2)
      predicts) or two non-reciprocal factors (which would contradict the
      non-reciprocal-part reading and is the more interesting print).

RESOURCE: the canonical tuples to degree N number about C(N, 4)/2 --
458,000 at N = 70, 4.1 million at N = 120 -- at 0.3 to 0.8 ms each in
flint; the default N = 70 is a 3-minute run, and the first attempt at 120
was killed as a runaway at 10 minutes (the docstring had summed one
degree's tuples for all of them). Progress prints per degree. Memory
negligible.

RUN RECORD (N = 70, 135.6 s, 2/2 checks pass; the first run's seven-term
control was mistyped as an eight-term polynomial and read ROOTED, fixed
before any verdict was read).

  F0  Controls: (x^5 - x^3 + 1)(x^7 + ... + 1) FREE, (x^5 + x^2 + 1)(x^8 -
      x^3 + x + 1) FREE, Phi_5(x)(x^3 - x^2 + 1) ROOTED; degrees <= 16
      print 0 free outright, the old census re-derived.
  F1  THE COLUMN IS EMPTY TO DEGREE 70 (rule, exhaustive): 458,745
      canonical pentanomials (reciprocal pairs once), 0 free outright.
      Reducible ones per degree run 1 at degree 6 to 3,412 at degree 68
      (the column: 12 at 12, 40 at 16, 47 at 20, 115 at 30, 482 at 40,
      704 at 50, 808 at 60, 2,159 at 70, the multiples of 5
      systematically lower), every one carrying a cyclotomic factor.
  F2  Not read: no witness.

  What the print supports: every reducible 0/1 pentanomial of degree at
  most 70 has a cyclotomic factor. Together with Ljunggren, Tverberg and
  Mills at fewer terms, five terms is the first count at which the
  statement is a finite-range rule and not a theorem; six terms fail it
  at degree 13. The theorem candidate is a Mills-type statement one term
  up, and the hand-attack's route (2) says what it needs: that the
  non-reciprocal part of a 0/1 pentanomial is irreducible or 1, which
  Filaseta, Ford and Konyagin's criterion turns into a finite
  exponent-matching problem (the non-reciprocal part of a 0/1 polynomial
  f is reducible iff a 0/1 polynomial w other than f and its reciprocal
  has w(1) = f(1) and w(x) w~(x) = f(x) f~(x); as quoted in Filaseta,
  Finch and Nicol, J. Theor. Nombres Bordeaux 2006, Lemma 2.1, read full
  text), plus a proof that a reciprocal non-cyclotomic factor cannot
  occur -- where a reciprocal 0/1 polynomial has only reciprocal
  irreducible factors (Filaseta and Meade, cited in Banerjee and Kundu,
  INTEGERS 24 (2024) A71, read full text) and the non-reciprocal case
  needs its own argument.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import sys
import time
from itertools import combinations

from flint import fmpz_poly

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 70


def poly_of(exps, n):
    co = [0] * (n + 1)
    for e in exps:
        co[e] = 1
    co[0] = 1
    co[n] = 1
    return fmpz_poly(co)


def is_reciprocal(g):
    co = [int(c) for c in g.coeffs()]
    return co == co[::-1]


def classify(f):
    """Return ('IRRED', None) / ('ROOTED', factors) / ('FREE', factors)."""
    _, fac = f.factor()
    total = sum(m for _, m in fac)
    if total < 2:
        return "IRRED", None
    if any(g.is_cyclotomic() for g, _ in fac):
        return "ROOTED", fac
    return "FREE", fac


def show(fac):
    return " * ".join(f"({g})^{m}" if m > 1 else f"({g})" for g, m in fac)


def main():
    checks = []

    def check(label, ok):
        checks.append(ok)
        print(("PASS " if ok else "FAIL ") + label)

    # F0 controls
    # (x^5 - x^3 + 1)(x^7 + x^5 + x^4 + x^3 + x^2 + x + 1) = 1 + x + x^2 + x^5 + x^7 + x^9 + x^12
    c7 = fmpz_poly([1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1])
    c6 = fmpz_poly([1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1])
    cr = fmpz_poly([1, 1, 0, 1, 1, 0, 0, 1])
    k7, f7 = classify(c7)
    k6, f6 = classify(c6)
    kr, fr = classify(cr)
    print(f"control seven-term degree 12: {k7} {show(f7) if f7 else ''}")
    print(f"control six-term degree 13:   {k6} {show(f6) if f6 else ''}")
    print(f"control Phi_5 pentanomial:    {kr} {show(fr) if fr else ''}")
    check("F0 controls: seven-term FREE, six-term FREE, Phi_5 one ROOTED",
          k7 == "FREE" and k6 == "FREE" and kr == "ROOTED")

    t0 = time.time()
    red = {}
    free = {}
    witnesses = []
    tuples = 0
    for n in range(4, NMAX + 1):
        r = 0
        fr_ = 0
        for a, b, c in combinations(range(1, n), 3):
            if (a, b, c) > (n - c, n - b, n - a):
                continue
            tuples += 1
            kind, fac = classify(poly_of((a, b, c), n))
            if kind == "IRRED":
                continue
            r += 1
            if kind == "FREE":
                fr_ += 1
                witnesses.append(((a, b, c, n), fac))
        red[n] = r
        free[n] = fr_
        print(f"  degree {n}: reducible {r}, free {fr_}, {time.time() - t0:.0f} s",
              file=sys.stderr, flush=True)
    wall = time.time() - t0
    print(f"\n{tuples} canonical pentanomials to degree {NMAX}, {wall:.1f} s")
    print("degree: reducible / free-outright (canonical, reciprocal pairs once)")
    line = []
    for n in range(4, NMAX + 1):
        line.append(f"{n}:{red[n]}/{free[n]}")
    for i in range(0, len(line), 10):
        print("  " + "  ".join(line[i:i + 10]))

    below17 = sum(free[n] for n in range(4, min(16, NMAX) + 1))
    check(f"F0 degrees <= 16: {below17} free outright (old census)", below17 == 0)
    total_free = sum(free.values())
    print(f"\nF1 free-outright pentanomials to degree {NMAX}: {total_free}")
    if witnesses:
        least = min(w[0][3] for w in witnesses)
        print(f"   least degree {least}")
        for (a, b, c, n), fac in witnesses:
            rec = ["R" if is_reciprocal(g) else "N" for g, _ in fac]
            print(f"   1+x^{a}+x^{b}+x^{c}+x^{n} = {show(fac)}   reciprocal flags {rec}")
        both_nonrec = sum(1 for _, fac in witnesses
                          if all(not is_reciprocal(g) for g, _ in fac))
        print(f"F2 witnesses with NO self-reciprocal factor: {both_nonrec} of {len(witnesses)}")
    print(f"\n{sum(checks)}/{len(checks)} checks pass")


if __name__ == "__main__":
    main()
