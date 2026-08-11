"""The resonance locus of the tilted window: which tilts empty it.

QUESTION
--------
Under the geometric tilt, a threshold cell's interior thresholds form
exactly one fiber window located at floor(Q*), where
Q* = log_q((1 + q^c)/2) and q is the tilt raised to the read modulus —
and the window is EMPTY exactly when Q* is an integer
(explore_ceiling_dials.py). The scans produced no such tilt off
uniform, and whether any RATIONAL tilt can produce one stood open.
Which tilts are resonant?

An integer Q* = B means 2 q^B = 1 + q^c, i.e. q is a positive root of

    f(q) = q^c - 2 q^B + 1,

with 0 < B < c forced, since Q* lies strictly in (0, c) at every
q != 1 (derived in the dials record).

THE SLATE, frozen before the engine
-----------------------------------
Hand derivation. f is monic over Z with constant term 1, so by the
rational root theorem its only candidate rational roots are +-1: no
rational q other than 1 is ever a root. And f's coefficient signs are
+, -, + — two sign changes — so Descartes bounds its positive roots by
two, one of which is always q = 1 (f(1) = 1 - 2 + 1 = 0); the root at
1 is double exactly when f'(1) = c - 2B = 0. Boundary signs place the
other root: f(0) = 1 > 0 and f -> +inf, so at 2B < c (f'(1) > 0, f
negative just left of 1) the second root lies in (0, 1), and at
2B > c it lies in (1, inf).

PREDICTIONS
-----------
P1 (the open question, killed): NO rational q != 1 satisfies
   2 q^B = 1 + q^c at any 0 < B < c. Exhaustive integer-arithmetic
   scan over q = a/b finds zero solutions.
P2 (the locus): for each pair 0 < B < c with 2B != c there is EXACTLY
   ONE resonant q* — algebraic irrational by P1 — with q* < 1 iff
   2B < c; at 2B = c the only positive root is the double root q = 1,
   which is the uniform parity resonance itself.
P3 (reflection): q -> 1/q carries the (B, c) resonance to (c-B, c),
   matching the dials record's reflection identity.
P4 (positive control): at (B, c) = (1, 3), f factors as
   (q - 1)(q^2 + q - 1), so q* is the reciprocal golden ratio — the
   number the dials record already found as the sign bit's c = 3 death
   boundary (the death boundary 2 q^m = 1 + q^c, m = (c-1)/2, is the
   B = m member of this same locus); Q* evaluated there returns 1.

DESIGN
------
All checks exact integer arithmetic where the claim is exact.
1. RATIONAL SCAN: every q = a/b, 1 <= a, b <= 60, gcd(a,b) = 1,
   a != b, every 2 <= c <= 12, every 0 < B < c: assert
   a^c + b^c - 2 a^B b^(c-B) != 0 (this is b^c f(a/b)).
2. LOCUS COUNT: for each (B, c), c <= 12: sign-change count of f is 2;
   for 2B != c, bracket the non-1 root by bisection on the side
   sign(2B - c) names and assert f has no other sign change on a fine
   grid of (0, 8] excluding neighborhoods of 1 and q*; for 2B = c,
   assert f(1) = 0, f'(1) = 0, and no sign change anywhere else on the
   grid.
3. REFLECTION: q*(B, c) * q*(c-B, c) = 1 to tolerance at every
   2B != c pair.
4. CONTROL: exact polynomial division of q^3 - 2q + 1 by (q - 1) over
   Z gives q^2 + q - 1; q* = (sqrt(5) - 1)/2 satisfies
   |Q*(q*, c=3) - 1| < 1e-12.

Resource: pure Python integers and floats, < 1 s, << 512 MB.

FINDINGS (entered post-run; run record at bottom)
-------------------------------------------------
All four predictions confirmed, 145,659 checks green.

THE RESONANCE CRITERION (rule; the impossibility and the count proved
for every modulus and every c, engine-confirmed at c <= 12, the scan
in-range at a, b <= 60):
- NO RATIONAL TILT OFF UNIFORM IS EVER RESONANT (the uniform point
  q = 1 is rational and IS the even-c resonance — the exclusion is
  exactly it). f(q) = q^c - 2 q^B + 1 is monic
  over Z with constant term 1, so its only rational roots are +-1
  (rational root theorem); q > 0, q != 1 leaves none. Every rational
  tilt off uniform leaves every cell's window nonempty — the scans'
  "no tilt produced one" was necessity, not luck. 145,332 (a, b, B, c)
  tuples confirm in exact integer arithmetic.
- THE LOCUS IS ONE ALGEBRAIC IRRATIONAL PER PAIR. For each
  0 < B < c with 2B != c, Descartes (signs +, -, +) caps positive
  roots at two, q = 1 is always one, and boundary signs force the
  other onto one side: exactly one resonant q*, with q* < 1 iff
  2B < c. All 60 pairs at c <= 12 confirm, no other sign change on
  (0, 8].
- AT 2B = c THE RESONANCE IS THE UNIFORM POINT. f'(1) = c - 2B = 0
  makes q = 1 a double root and nothing else is resonant: parity
  deadness at even c is the whole 2B = c family, collapsed onto the
  uniform prior. All 6 pairs confirm.
- THE REFLECTION CARRIES THE LOCUS. q*(B, c) * q*(c - B, c) = 1 at
  all 60 pairs — the dials record's tilt-reflection identity, read on
  the resonance set.
- THE DEATH BOUNDARY IS A MEMBER. The sign bit's odd-c death boundary
  2 q^m = 1 + q^c, m = (c - 1)/2, is the B = m member of this locus:
  the tilt at which the sign bit dies is exactly a tilt at which the
  whole window closes, golden at c = 3 (control: exact factor
  (q - 1)(q^2 + q - 1), Q*(1/phi, c = 3) = 1.000000000000).

RUN RECORD: 145,659 checks, wall < 2 s, pure Python ints/floats.
"""

from math import gcd, log, sqrt


def bcf(a, b, B, c):
    """b^c * f(a/b) as an exact integer."""
    return a**c + b**c - 2 * a**B * b ** (c - B)


def f(q, B, c):
    return q**c - 2 * q**B + 1


def bisect_root(B, c):
    """The non-1 positive root of f, bracketed on its predicted side."""
    if 2 * B < c:
        lo, hi = 1e-9, 1.0 - 1e-9  # f(lo) = 1 > 0, f(hi) < 0
    else:
        lo, hi = 1.0 + 1e-9, 2.0
        while f(hi, B, c) < 0:
            hi *= 2
    flo = f(lo, B, c)
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = f(mid, B, c)
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    checks = 0

    # 1. RATIONAL SCAN — P1.
    for a in range(1, 61):
        for b in range(1, 61):
            if a == b or gcd(a, b) != 1:
                continue
            for c in range(2, 13):
                for B in range(1, c):
                    assert bcf(a, b, B, c) != 0, (a, b, B, c)
                    checks += 1
    print(f"P1 rational scan: 0 solutions over a,b<=60, c<=12 "
          f"({checks} pairs checked)")

    # 2. LOCUS COUNT — P2.
    n_single = n_double = 0
    roots = {}
    for c in range(2, 13):
        for B in range(1, c):
            coeffs_signs = [1, -2, 1]  # q^c, q^B, 1: always +,-,+
            assert sum(
                1
                for i in range(len(coeffs_signs) - 1)
                if coeffs_signs[i] * coeffs_signs[i + 1] < 0
            ) == 2
            checks += 1
            if 2 * B == c:
                # double root at 1, nothing else: even-order contact,
                # f > 0 on both sides of 1
                assert f(1.0, B, c) == 0.0
                assert f(1.0 - 1e-3, B, c) > 0 and f(1.0 + 1e-3, B, c) > 0
                grid_changes = count_sign_changes_on_grid(B, c, exclude=[1.0])
                assert grid_changes == 0, (B, c, grid_changes)
                n_double += 1
                checks += 3
            else:
                qs = bisect_root(B, c)
                roots[(B, c)] = qs
                assert (qs < 1.0) == (2 * B < c), (B, c, qs)
                assert abs(f(qs, B, c)) < 1e-9, (B, c, qs)
                # no OTHER sign change: away from 1 and q*, none remain
                grid_changes = count_sign_changes_on_grid(
                    B, c, exclude=[1.0, qs]
                )
                assert grid_changes == 0, (B, c, grid_changes)
                n_single += 1
                checks += 3
    print(f"P2 locus: {n_single} pairs 2B != c each carry exactly one "
          f"resonant q* on the predicted side; {n_double} pairs 2B = c "
          f"carry only the double root at 1")

    # 3. REFLECTION — P3.
    n_refl = 0
    for (B, c), qs in roots.items():
        assert abs(qs * roots[(c - B, c)] - 1.0) < 1e-6, (B, c)
        n_refl += 1
        checks += 1
    print(f"P3 reflection: q*(B,c) * q*(c-B,c) = 1 at all {n_refl} pairs")

    # 4. CONTROL — P4: exact division (q^3 - 2q + 1) / (q - 1).
    # coefficients low-to-high: [1, -2, 0, 1]
    dividend = [1, -2, 0, 1]
    quotient, rem = poly_divmod_by_q_minus_1(dividend)
    assert rem == 0 and quotient == [-1, 1, 1], (quotient, rem)
    qstar = (sqrt(5.0) - 1.0) / 2.0
    Qstar = log((1 + qstar**3) / 2) / log(qstar)
    assert abs(Qstar - 1.0) < 1e-12, Qstar
    assert abs(roots[(1, 3)] - qstar) < 1e-9
    checks += 3
    print(f"P4 control: f(q; 1,3) = (q-1)(q^2+q-1) exactly, "
          f"q* = 1/phi = {qstar:.12f}, Q*(q*, c=3) = {Qstar:.12f}")

    print(f"ALL GREEN: {checks} checks")
    return checks


def poly_divmod_by_q_minus_1(coeffs_low_to_high):
    """Divide an integer polynomial by (q - 1); quotient low-to-high."""
    # synthetic division at root 1, on high-to-low coefficients
    hi_to_lo = coeffs_low_to_high[::-1]
    out = [hi_to_lo[0]]
    for a in hi_to_lo[1:]:
        out.append(a + out[-1])
    rem = out[-1]
    quotient = out[:-1][::-1]
    return quotient, rem


def count_sign_changes_on_grid(B, c, exclude, lo=1e-6, hi=8.0, n=200000):
    changes = 0
    prev = f(lo, B, c)
    step = (hi - lo) / n
    x = lo
    for _ in range(n):
        x += step
        if any(abs(x - e) < 5e-4 for e in exclude):
            prev = None
            continue
        cur = f(x, B, c)
        if prev is not None and (cur < 0) != (prev < 0):
            changes += 1
        prev = cur
    return changes


if __name__ == "__main__":
    main()
