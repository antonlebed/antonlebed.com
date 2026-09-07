"""explore_rank2_gap.py — THE RANK-2 GAP'S ASYMPTOTIC: is the ratio of
the two successive minima of a rank-2 flattening lattice
(sqrt(e)/2) sqrt(J + 1) with an explicit error bound, at every depth?

THE QUESTION. At rank 2 the flattening lattice {(a + b x)(x - 1)^J} has
first minimum lambda_1 = max_k |c_k - c_{k-1}|, the largest adjacent
difference of the binomial row c_k = C(J, k), and second minimum
lambda_2 = C(J, floor(J/2)), the row's central entry
(explore_flatten_theorem.py, a theorem at every J >= 2). The ratio was
measured, not proved: lambda_2/lambda_1 ~ (sqrt(e)/2) sqrt(J + 1), 2.41%
high at J = 10 and 0.01% at J = 2000, the residual oscillating because
the argmax of the difference is an integer where the saddle point is
not. This rig asks for the sentence as a rule: an inequality
    lambda_2 / lambda_1 = (sqrt(e)/2) sqrt(J + 1) (1 + eps_J),
    -1/(J + 1) < eps_J <= 5/(2 (J + 1))   for every J >= 2,
proved on paper past a depth and computed exactly below it, and for
the residual's own leading term, which the oscillation is.

THE OBJECTS. n = J + 1, m = n/2. For 0 <= k <= n/2 write u = m - k,
so u runs over m + Z in [0, m] (integers at even n, half-integers at
odd n). The adjacent difference is
    c_k - c_{k-1} = C(n, k) (n - 2k)/n = C(n, k) 2u/n,
so lambda_1 = (2/n) max_u C(n, m - u) u, and lambda_2 = C(n - 1,
floor((n - 1)/2)). B = Gamma(n + 1)/Gamma(m + 1)^2 is the real central
binomial: B = C(n, n/2) at even n. ROBBINS-FREE: every bound below is
on the digamma derivatives and one Gautschi-type ratio, never on
Stirling's series.

THE HAND DERIVATION (on paper, before the engine).

H1  THE ROW ABOUT THE CENTRE. phi(u) = ln Gamma(m + 1 - u)
    + ln Gamma(m + 1 + u) - 2 ln Gamma(m + 1) is even, phi(0) = 0,
    phi''(0) = 2 psi'(m + 1) =: 2A, phi'''' = psi'''(m + 1 - u)
    + psi'''(m + 1 + u) > 0 and decreasing in u, so by Taylor
        u^2 A <= phi(u) <= u^2 A + u^4 psi'''(m + 1 - u)/12,
    i.e. exp(-u^2 A - R(u)) <= C(n, m - u)/B <= exp(-u^2 A) with
    R(u) = u^4 psi'''(m + 1 - u)/12. The digamma bounds used:
    1/x + 1/(2x^2) < psi'(x) < 1/x + 1/(2x^2) + 1/(6x^3) and
    psi'''(x) <= 2/x^3 + 6/x^4 (the tail of sum 6/(x + j)^4 by an
    integral), all x > 0.
H2  THE FIRST MINIMUM. Upper: over real u, u e^{-u^2 A} peaks at
    u* = 1/sqrt(2A) with value 1/sqrt(2eA), so
    lambda_1 <= (2B/n)/sqrt(2eA). Lower: the admissible u_0 nearest u*
    is within 1/2 (u* < sqrt((m + 1)/2) <= m at n >= 2, so it exists),
    and with t = u_0 sqrt(2A) - 1, |t| <= sqrt(A/2) <= 1,
        u_0 e^{-u_0^2 A} = (1 + t) e^{-t - t^2/2}/sqrt(2A)
                         >= (1 - t^2)(1 - t^2/2)/sqrt(2A)
                         >= (1 - 3A/4)/sqrt(2A),
    using (1 + t) e^{-t} >= 1 - t^2 on [-1, 1] (its derivative
    t(2 - e^{-t}) has the sign that makes 0 the minimum on each side)
    and e^{-s} >= 1 - s. So
        (1 - 3A/4) e^{-R(u_0)} <= lambda_1 sqrt(2eA) n/(2B) <= 1.
H3  THE SECOND MINIMUM. At even n, lambda_2 = C(n - 1, n/2 - 1)
    = B/2 exactly. At odd n, lambda_2/B = (1/n)(Gamma(m + 1)/
    Gamma(m + 1/2))^2, and Kershaw's inequality at s = 1/2,
    sqrt(x + 1/4) < Gamma(x + 1)/Gamma(x + 1/2) < sqrt(x - 1/2 +
    sqrt(3/4)), gives lambda_2 = (B/2)(1 + theta/n) with
    1/2 < theta < 0.732; theta = 0 at even n.
H4  THE RATIO. lambda_2/lambda_1 = (sqrt(e)/2) sqrt(n) sqrt(nA/2)
    (1 + theta/n)/F with F the bracketed quantity of H2. From the
    psi' bounds with m + 1 = (n + 2)/2:
        nA/2 > n(n + 3)/(n + 2)^2 = 1 - (n + 4)/(n + 2)^2 >= 1 - 1/n,
        nA/2 < 1 - (n + 4)/(n + 2)^2 + 2n/(3(n + 2)^3) <= 1,
    so 1 - 1/n < sqrt(nA/2) <= 1. LOWER: eps >= sqrt(nA/2) - 1
    > -1/n, using F <= 1 and theta >= 0. UPPER: 3A/4 <= 3/(2n)
    + 1/n^3 and, at n >= 100, u_0 < (sqrt(n + 2) + 1)/2 and
    m + 1 - u_0 > (n + 1 - sqrt(n + 2))/2 >= 0.4495 n give
    R(u_0) <= 0.19/n; hence for n >= 100
        eps <= (1 + 0.732/n)/((1 - 1.5/n - 1/n^3)(1 - 0.19/n)) - 1
            <= (0.732 + 1.5 + 0.19)/(0.9832 n) <= 2.5/n,
    the numerator times n being at most a + b + d once
    c/n^2 < bd/n, and the denominator increasing in n. So for every
    J >= 99: -1/(J + 1) < eps_J <= 2.5/(J + 1), a THEOREM; the depths
    2..98 are the computation below, which makes the two-sided bound
    a RULE at every J >= 2.
H5  THE RESIDUAL'S LEADING TERM. Keeping the next order:
    sqrt(nA/2) ~ 1 - 1/(2n); theta ~ 1/2 at odd n (J even), 0 at even
    n; F ~ 1 - t^2 - R with t^2 ~ 4 delta^2/n for delta = u_0 - u*
    in [-1/2, 1/2] and R ~ 1/(12n). So
        n eps_J ~ theta_J - 5/12 + 4 delta_J^2,
    a bounded oscillation: in [-5/12, 7/12] at odd J and
    [1/12, 13/12] at even J, the parity of J and the rounding of
    sqrt(n)/2 to the lattice m + Z its two sources. The
    correction is O(n^{-1/2}) (the t^3 term).

PREDICTIONS, fixed before the engine ran.
  PR1 (the rule). At every J = 2..4000, eps_J computed exactly from
      the integer minima satisfies -1/(J + 1) < eps_J <= 2.5/(J + 1).
      KILL: one J off.
  PR2 (the chain). At every J = 2..4000 the explicit bracket of H2-H4
      holds term by term: lambda_1 lies in its H2 interval computed
      from A_lo, A_hi and R(u_0) with the psi bounds, lambda_2 in its
      H3 interval, and eps in [sqrt(n A_lo/2) - 1, U(n)] with U(n)
      the H4 upper formula evaluated at that n. KILL: one J off, which
      would be an error in the derivation, not in the rule.
  PR3 (the leading term). At every J = 10..4000,
      |n eps_J - (theta_J - 5/12 + 4 delta_J^2)| <= 1/sqrt(n), with
      theta_J = 1/2 at even J and 0 at odd J and delta_J = u_0 - u*
      for the exact u* = 1/sqrt(2 psi'(m + 1)). KILL: one J off.
  PR4 (the doc's two numbers, the positive control). eps_J prints
      0.0241 at J = 10 and 0.0001 at J = 2000, the doc's 2.41% and
      0.01%, and lambda_1, lambda_2 at J = 2..14 equal the theorem
      rig's enumeration (explore_flatten_theorem.py's closed forms
      recomputed here from the row). KILL: one off.
  PR5 (the window of n eps). Over J = 100..4000 the extremes of
      n eps_J at odd J lie in [-5/12 - 0.1, 7/12 + 0.1] and at even J
      in [1/12 - 0.1, 13/12 + 0.1]. KILL: an extreme outside.

THE DESIGN. Exact integers for lambda_1, lambda_2 (math.comb); eps by
Fraction against the float of (sqrt(e)/2) sqrt(n) at 60-digit
precision through decimal; psi' and psi''' by their asymptotic series
with a recurrence shift to x >= 40 (error below 1e-18, the bounds of
H1 are what the rule uses, the exact values only PR3's u*). Controls:
the psi' series against the two-sided bound at every x used.
Run: python prime/code/explore_rank2_gap.py   (~2 s)

FINDINGS (entered post-run, copied from printed output).

1. THE RULE (PR1, PR2 hit). At every J = 2..4000, -1/(J + 1) < eps_J
   <= 2.5/(J + 1), and the explicit H2-H4 bracket holds at every depth
   (0 off), the H4 closed formula valid and below 2.5/n at every
   n >= 100. The bracket is loose where the rule is not: at J = 2 it
   reads [-0.030, +145]/n against eps = +0.401 (n eps = 1.20, the
   largest over the range), at J = 100 [-0.004, +1.913]/n, at J = 4000
   [-0.000, +1.818]/n; R(u_0) is 8.2/n at J = 2 and 0.09/n at J = 4000
   against its limit 1/12.
2. THE RESIDUAL (PR3, PR5 hit). sqrt(n) |n eps_J - (theta_J - 5/12 +
   4 delta_J^2)| <= 0.1483 over J = 10..4000, the maximum at J = 19;
   over J >= 100 the window of n eps_J is [-0.4166, +0.5833] at odd J
   (predicted [-5/12, 7/12]) and [+0.0834, +1.0859] at even J
   (predicted [1/12, 13/12]), the even top 0.003 past its limit by the
   O(n^{-1/2}) term. n eps at J = 98, 99, 100: +1.087, -0.415, +0.902,
   the parity swing.
3. THE CONTROLS (PR4 hit). eps = +0.024105 at J = 10 (2.41%) and
   +0.000075 at J = 2000 (0.01%; 0.0075%), the doc's two figures;
   lambda_1, lambda_2 = (1, 2), (2, 3), (3, 6), (5, 10), (9, 20),
   (14, 35), (28, 70), (48, 126), (90, 252), (165, 462), (297, 924),
   (572, 1716), (1001, 3432) at J = 2..14 from the row; the psi'
   series inside its two-sided bound at every x checked.

TIER. THE RANK-2 GAP'S ASYMPTOTIC — lambda_2/lambda_1 = (sqrt(e)/2)
sqrt(J + 1) (1 + eps_J) with -1/(J + 1) < eps_J <= 5/(2(J + 1)) — is a
THEOREM at every J >= 99 (H1-H4, on the digamma bounds and Kershaw's
inequality, no computation) and a RULE at every J >= 2 (the depths
2..98 computed exactly). THE RESIDUAL'S LEADING TERM, n eps_J ->
theta_J - 5/12 + 4 delta_J^2 with an O(n^{-1/2}) correction, is a rule
in range (J = 10..4000), its derivation H5 a heuristic to the order
kept.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import sys
import time
from math import comb, sqrt, floor, exp
from decimal import Decimal, getcontext

getcontext().prec = 60


# ---------------------------------------------------------------- exact objects
def minima(J):
    """(lambda_1, lambda_2) of the rank-2 lattice at depth J, exact."""
    # c_k - c_{k-1} on the rising half, the row built by its ratio
    c, best = 1, 1
    for k in range(1, J // 2 + 1):
        nxt = c * (J - k + 1) // k
        best = max(best, nxt - c)
        c = nxt
    return best, comb(J, J // 2)


def eps_exact(J):
    """eps_J = lambda_2/lambda_1 / ((sqrt(e)/2) sqrt(J+1)) - 1, to 1e-40."""
    lam1, lam2 = minima(J)
    n = J + 1
    ratio = Decimal(lam2) / Decimal(lam1)
    pred = (Decimal(1).exp().sqrt() / 2) * Decimal(n).sqrt()
    return ratio / pred - 1


# ---------------------------------------------------------------- digamma derivatives
def psi1(x):
    """trigamma by recurrence to x >= 40 then the asymptotic series."""
    acc = 0.0
    while x < 40:
        acc += 1.0 / (x * x)
        x += 1
    s = 1 / x + 1 / (2 * x**2) + 1 / (6 * x**3) - 1 / (30 * x**5) \
        + 1 / (42 * x**7) - 1 / (30 * x**9)
    return acc + s


def psi3(x):
    """tetragamma psi''' by recurrence to x >= 40 then the series."""
    acc = 0.0
    while x < 40:
        acc += 6.0 / x**4
        x += 1
    s = 2 / x**3 + 3 / x**4 + 2 / x**5 - 1 / x**7 + 4 / (3 * x**9)
    return acc + s


def bounds_for(J):
    """the explicit H2-H4 bracket at depth J, every piece a float bound."""
    n = J + 1
    m = n / 2
    x = m + 1
    A_lo = 1 / x + 1 / (2 * x**2)
    A_hi = A_lo + 1 / (6 * x**3)
    A = psi1(x)
    assert A_lo < A < A_hi, (J, A_lo, A, A_hi)
    ustar = 1 / sqrt(2 * A)
    # nearest admissible u_0 in m + Z, within [0, m]
    frac = m - floor(m)                       # 0 at even n, 0.5 at odd n
    u0 = frac + round(ustar - frac)
    u0 = min(max(u0, frac), m)
    assert abs(u0 - ustar) <= 0.5 + 1e-12
    R = u0**4 * psi3(m + 1 - u0) / 12
    R_hi = u0**4 * (2 / (m + 1 - u0)**3 + 6 / (m + 1 - u0)**4) / 12
    # lambda_1 sqrt(2 e A) n / (2 B) in [(1 - 3A/4) e^{-R}, 1]
    F_lo = (1 - 3 * A_hi / 4) * exp(-R_hi)
    # lambda_2 / (B/2) in [1 + theta_lo/n, 1 + theta_hi/n]
    if n % 2 == 0:
        th_lo = th_hi = 0.0
    else:
        # Kershaw: lambda_2/B = (m + c)/n with 1/4 < c < sqrt(3/4) - 1/2,
        # so theta = 2c lies in (1/2, 0.732)
        th_lo, th_hi = 0.5, 2 * (sqrt(0.75) - 0.5)
    eps_lo = sqrt(n * A_lo / 2) * (1 + th_lo / n) / 1.0 - 1
    eps_hi = sqrt(n * A_hi / 2) * (1 + th_hi / n) / F_lo - 1
    return dict(n=n, A=A, A_lo=A_lo, A_hi=A_hi, ustar=ustar, u0=u0,
                delta=u0 - ustar, R=R, R_hi=R_hi, F_lo=F_lo,
                th_lo=th_lo, th_hi=th_hi, eps_lo=eps_lo, eps_hi=eps_hi)


def U_formula(n):
    """the H4 closed upper bound, valid at n >= 100."""
    return (1 + 0.732 / n) / ((1 - 1.5 / n - 1 / n**3) * (1 - 0.19 / n)) - 1


# ---------------------------------------------------------------- the arms
def main():
    t0 = time.time()
    fired = []
    JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4000

    print("== control: the psi' series against its two-sided bound")
    for x in (1.5, 2, 5, 10, 40, 100, 1000):
        lo = 1 / x + 1 / (2 * x**2)
        hi = lo + 1 / (6 * x**3)
        v = psi1(x)
        print(f"   x={x:>6}: {lo:.9f} < {v:.9f} < {hi:.9f}  {'ok' if lo < v < hi else 'OFF'}")
        if not lo < v < hi:
            fired.append(f"psi1 bound off at x={x}")

    print("== PR4: the doc's numbers and the small depths")
    for J in (10, 2000):
        e = eps_exact(J)
        print(f"   J={J}: eps = {float(e):+.6f} ({100*float(e):.2f}%)")
    e10, e2000 = float(eps_exact(10)), float(eps_exact(2000))
    if not (abs(e10 - 0.0241) < 5e-4 and abs(e2000 - 0.0001) < 5e-4):
        fired.append("PR4 doc numbers")
    print("   J : lambda_1 lambda_2  (rows 2..14)")
    for J in range(2, 15):
        l1, l2 = minima(J)
        row = [comb(J, k) for k in range(J + 1)]
        diffs = [row[0]] + [row[k] - row[k - 1] for k in range(1, J + 1)] + [-row[J]]
        l1_chk = max(abs(d) for d in diffs)
        print(f"   {J:>2}: {l1:>5} {l2:>5}   check {l1_chk == l1}")
        if l1_chk != l1:
            fired.append(f"PR4 minima at J={J}")

    print(f"== PR1/PR2/PR3/PR5 over J = 2..{JMAX}")
    worst_pr1 = (0.0, None)
    pr2_off = []
    pr3_max = (0.0, None)
    win_odd = [float("inf"), -float("inf")]
    win_even = [float("inf"), -float("inf")]
    formula_ok = True
    mx = (0.0, None)
    for J in range(2, JMAX + 1):
        n = J + 1
        e = float(eps_exact(J))
        if abs(e) * n > mx[0]:
            mx = (abs(e) * n, J)
        # PR1
        if not (-1 / n < e <= 2.5 / n):
            fired.append(f"PR1 off at J={J}: eps={e}")
        s = e * n
        # PR2 the chain
        b = bounds_for(J)
        if not (b["eps_lo"] <= e <= b["eps_hi"]):
            pr2_off.append((J, e, b["eps_lo"], b["eps_hi"]))
        if n >= 100:
            if b["eps_hi"] > U_formula(n) + 1e-15 or U_formula(n) > 2.5 / n + 1e-15:
                formula_ok = False
                pr2_off.append((J, "U_formula", b["eps_hi"], U_formula(n)))
        # PR3
        if J >= 10:
            theta = 0.5 if J % 2 == 0 else 0.0
            lead = theta - 5 / 12 + 4 * b["delta"] ** 2
            dev = abs(s - lead) * sqrt(n)
            if dev > pr3_max[0]:
                pr3_max = (dev, J)
            if dev > 1.0:
                fired.append(f"PR3 off at J={J}: n eps={s:.4f} lead={lead:.4f}")
        # PR5
        if J >= 100:
            w = win_even if J % 2 == 0 else win_odd
            w[0] = min(w[0], s)
            w[1] = max(w[1], s)
        if J in (2, 3, 4, 5, 6, 10, 20, 50, 98, 99, 100, 200, 500, 1000, 2000, 4000):
            print(f"   J={J:>5}: eps={e:+.6f}  n*eps={s:+.4f}  bracket [{b['eps_lo']*n:+.3f}, {b['eps_hi']*n:+.3f}]/n"
                  f"  delta={b['delta']:+.3f}  R={b['R']*n:.4f}/n")
    print(f"   PR2 chain off at {len(pr2_off)} depths" + (f": {pr2_off[:3]}" if pr2_off else ""))
    if pr2_off:
        fired.append("PR2 chain")
    print(f"   U formula valid and <= 2.5/n at every n >= 100: {formula_ok}")
    print(f"   PR3 max sqrt(n)*|n eps - lead| = {pr3_max[0]:.4f} at J={pr3_max[1]}")
    print(f"   PR5 window of n*eps, J>=100: odd J [{win_odd[0]:+.4f}, {win_odd[1]:+.4f}]"
          f" (predicted [-0.4167, +0.5833]); even J [{win_even[0]:+.4f}, {win_even[1]:+.4f}]"
          f" (predicted [+0.0833, +1.0833])")
    if not (-5 / 12 - 0.1 <= win_odd[0] and win_odd[1] <= 7 / 12 + 0.1):
        fired.append("PR5 odd window")
    if not (1 / 12 - 0.1 <= win_even[0] and win_even[1] <= 13 / 12 + 0.1):
        fired.append("PR5 even window")
    print(f"   largest |eps|*(J+1) over the range: {mx[0]:.4f} at J={mx[1]}")

    print(f"== verdict ({time.time()-t0:.1f}s): " + ("ALL PREDICTIONS HELD" if not fired else "FIRED: " + "; ".join(fired)))


if __name__ == "__main__":
    main()
