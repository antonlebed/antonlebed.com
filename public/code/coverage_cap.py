"""
coverage_cap.py -- how many points of a degree triangle one residue
class can hold.

QUESTION. Fix a prime l, a multiplier B not 0 or 1 mod l, and a degree
0 <= D <= l - 2. The TRIANGLE COUNT of a class w mod l is

    f(w) = #{(i, j) : i, j >= 0, i + j <= D, i + B*j = w mod l}.

Is f(w) <= floor(D/2) + 1 at every w (THE COVERAGE CAP)? The cap is
what the two-prime row of the realizability law needs (torsion.py):
with it, a class mod the larger prime of m = q*q' holds at most
(q - 1)/2 exponents of a degree q - 2 triangle, and a codeword of
Phi_m cannot live there.

THE ARGUMENT (written before this script). Work with the STAIRCASE
COUNT g(c) = #{u in [0, D] : (c + B*u) mod l <= u}. Row j of the
triangle covers the exponents [B*j, B*j + D - j]; putting u = D - j
gives f(w) = g(w - B*D), so the two counts have one maximum, gmax.
B = 1 is excluded for a reason: there g(0) = D + 1.
  (1) THE LATTICE FRAME. g(c) counts the points (u, v) of the triangle
      T_D = {0 <= v <= u <= D} with v = c + B*u mod l: a translate of
      the lattice L_B = {(u, v) : v = B*u mod l}, of determinant l.
      Equivalently u is good iff some integer P has
      P*l in [c + (B - 1)*u, c + B*u].
  (2) THE SYMMETRIES. (a) g_B(c) = g_(1-B)(-c): for good u,
      z = (c + B*u) mod l and u - z = ((1 - B)*u - c) mod l.
      (b) time reversal, (u, v) -> (D - v, D - u):
      g^B_D(c) = g^(1/B)_D(D - D/B + c/B). So gmax is constant on the
      orbit {B, 1 - B, 1/B, 1 - 1/B, 1/(1 - B), B/(B - 1)}.
      (c) EQUICOVERAGE: at D = l - 2, g = (l - 1)/2 at every c. The
      difference g(c + 1) - g(c) is #{u <= l - 2 : -B*u = c + 1} less
      #{u <= l - 2 : (1 - B)*u = c}; each congruence has one solution
      in Z/l, lost only when it is u = l - 1, and both are lost at the
      same c = B - 1. So g is constant, and its mean is (l - 1)/2.
      (d) DUALITY: for D < l - 2 and D~ = l - 3 - D,
      g^B_D(c) = g^(1-B)_(D~)(c - 2B + 1) + D + (3 - l)/2: equicoverage
      less the tail u in [D + 1, l - 2], whose complements, reindexed
      by l - 2 - u, are the (1 - B)-staircase of degree D~. The cap
      transfers EXACTLY, (D + 1)/2 or D/2 + 1 on both sides by parity
      (D~ has D's parity, l being odd), so only
      min(D, D~) <= (l - 3)/2 needs proving.
  (3) ONE LINE AND THE PRODUCT BOUND. Let b = min(B, l + 1 - B), the
      smaller of the pair {B, 1 - B}, 2 <= b <= (l + 1)/2. By (2a) take
      the multiplier b. The good times at one P lie in
      [X/b, min(D, X/(b - 1))], X = P*l - c, at most
      min(X/(b(b - 1)), D - X/b) + 1 <= D/b + 1 of them. For a good u,
      P*l lies in [c + (b - 1)*u, c + b*u], of length u < l, and in
      [c, c + b*D]: at most floor(b*D/l) + 1 values of P. So
          gmax <= (floor(b*D/l) + 1) * (floor(D/b) + 1).
      At b*D < l (ONE LINE) this is floor(D/b) + 1 <= cap. At
      D + 1 <= b <= (l - 1)/2 (SPARSE) it is floor(b*D/l) + 1 <= cap.
      THE SMALL-D COROLLARY: if min(D, D~)^2 < l the cap holds at every
      B -- b <= D' is one line, D' < b <= (l - 1)/2 is sparse, and
      b = (l + 1)/2 is B = 1/2, whose orbit holds 2, one line.
  (4) THE LATTICE LEMMAS. (A) For phi >= 0 unimodal and sample points
      h apart, sum phi(y_i) <= (1/h) * integral(phi) + max(phi).
      (B) Let g0 be a shortest vector of L_B, of length lam. The points
      of L_B lie on lines parallel to g0, h = l/lam apart, lam apart on
      each line; a chord of the convex T_D is a concave function of
      the line's offset (Brunn), so (A) with area D^2/2, diameter and
      width at most sqrt2*D gives
          gmax <= D^2/(2l) + sqrt2*D/lam + sqrt2*lam*D/l + 1.
      (C) n consecutive points x0 + k*g0 inside T_D, g0 = (t, s) with
      t >= 1, satisfy (n - 1)*r <= D, where r = s if s > t, t if
      0 <= s <= t, t - s if s < 0: add the binding constraints among
      v >= 0, v <= u, u <= D. (D) So if lam < 7, a line holds at most
      min(chord/lam + 1, floor(D/r) + 1) points, and
          gmax <= D^2/(2l) + sqrt2*lam*D/l + floor(D/r) + 1.
  (5) THE FAMILIES. A primitive (t, s) with t^2 + s^2 < 49 and r <= 4
      puts B = s/t in the orbit of 2 ({2, -1, 1/2}), of 3 ({3, -2,
      1/3, 2/3, 3/2, -1/2}) or of 4 ({4, -3, 1/4, 3/4, 4/3, -1/3}), a
      finite list of rationals. The orbit of 2 is one line at b = 2
      (2D < l). THE TENTS, B = -a for a = 2, 3: the intervals are
      [a*u, (a + 1)*u], and with D <= (l - 3)/2 only X = c and
      X = c + l carry good times (X <= (a + 1)*D < 2l). A line holds
      N(X) <= min(X/(a(a + 1)), D - X/(a + 1)) + 1 <= D/(a + 1) + 1,
      and the second is nonempty only when c <= (a + 1)*D - l
      <= (a - 1)*D - 3. At a = 2: N(c) <= c/6 + 1 and
      N(c + l) < D/3 - c/3 + 1. At a = 3, with Y = c + l in [l, 4D]:
      N(c) <= (Y - 2D)/12 + 1, and N(Y) <= Y/12 + 1 below Y = 3D and
      D - Y/4 + 1 above it. Either way gmax <= D/3 + 2.
  (6) THE CLOSURE, l >= 213, D <= (l - 3)/2. Target: gmax < D/2 + 1/2
      (so gmax <= cap), or the one-line bound. Case 0: D^2 < l, the
      corollary. Case 1: lam >= 7, lemma (B); the condition
      sqrt2/lam + sqrt2*lam/l < 1/2 - D/(2l) - 1/(2D) is convex in lam
      and its right side concave in D, so four corners decide it, lam
      in {7, 2*sqrt(l/pi)} (Minkowski) and D in {sqrt l, (l - 3)/2}.
      Case 2: lam < 7 and r >= 5, lemma (D) with floor(D/r) <= D/5;
      the condition D/(2l) + 9.9/l + 1/5 + 1/(2D) < 1/2 is convex in D,
      so its two ends decide it. Case 3: lam < 7 and r <= 4, the
      families: the orbit of 2 by one line, the others by the tents,
      D/3 + 2 < D/2 + 1/2 at D >= 10, and D <= 9 is case 0. Every
      corner holds at l = 213, and each margin increases with l: the
      terms in lam/l, 9.9/l and, at lam = 2 sqrt(l/pi), 1/lam fall; at
      D = sqrt l the D-terms are 1/sqrt l, falling; at D = (l - 3)/2
      they add -3/(4 l^2) + 1/(l - 3)^2 > 0 to each margin's
      derivative. X2 checks a grid of l to 10^7.
  (7) THE FINITE LEG: every prime l <= 211, every D, every B, by the
      tests of (2)-(3) and brute force where they are silent.

DESIGN. Sections of checks printing PASS or FAIL, the control first.
  C  controls: B = 1 breaks the cap at every D >= 2 (g(0) = D + 1);
     B = 2 at even D meets it exactly (g(-D) = D/2 + 1); the frame
     f(w) = g(w - B*D) and the lattice frame (1), every w, at five
     systems.
  Y  the symmetries (2a)-(2d), exact at every c: (2a), (2b) for every
     prime 5 <= l <= 47, every D and B; (2c) for every modulus 5..79
     with B and B - 1 units; (2d) for every prime 5 <= l <= 47.
  O  the bounds (3): the product bound against brute force for every
     prime 5 <= l <= 103, every D >= 1, every b and both of its pair;
     the small-D corollary against the test at every prime
     5 <= l <= 211.
  L  the lemmas (4)-(5): (B) and (D) at l = 211, 401 and three D each,
     every B; (C) on random runs; the family list as exact rationals;
     the tents at every prime 53 <= l <= 401 and every
     D <= (l - 3)/2.
  X  the closure (6): the four corners of case 1 and the two ends of
     case 2 at l = 213 and on a grid of l to 10^7; then the assembled
     split at every B and every D <= (l - 3)/2 for the primes
     213 <= l <= 449 and l = 1009, D^2 < l and the orbit of 2 left to
     the corollary and one line: every other triple in a case, every
     bound under target, brute samples under their bounds.
  The controls stop the run when one fails.
  F  the finite leg (7): every prime l <= 211, every D in [0, l - 2],
     every B in [2, l - 1].

PREDICTIONS (fixed before the run). Every check passes. The cap is met
with equality somewhere in the finite leg (the orbit of 2 meets it at
every even D), so the finite leg's brute-forced triples are counted
and their equality cases printed, not predicted.

RESULTS (the run below; 18 of 18 checks pass, 3.3 s, peak commit
9 MB). Equicoverage over 1048 systems; the tents to l = 401; the
closure's least corner margin 0.0003 at l = 213; the assembled split
over 2,795,067 triples at 41 primes, 5066 brute samples under their
bounds; the finite leg over 596,366 triples, 48,172 of them brute
forced, the cap met with equality where the tests are silent only at
(l, D, B) = (13, 5, 4) and (13, 5, 10).
"""

import random
from fractions import Fraction
from math import gcd, pi, sqrt

CHECKS = []
SQ2 = sqrt(2)


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" +
          (f"  [{detail}]" if detail else ""))


def is_prime(n):
    return n >= 2 and all(n % k for k in range(2, int(n ** 0.5) + 1))


def primes(lo, hi):
    return [n for n in range(lo, hi + 1) if is_prime(n)]


def stair(l, D, B):
    """g(c) for every c: interval [-B*u, -B*u + u] laid down for each u."""
    diff = [0] * (l + 1)
    for u in range(D + 1):
        lo = (-B * u) % l
        hi = lo + u
        if hi < l:
            diff[lo] += 1
            diff[hi + 1] -= 1
        else:
            diff[lo] += 1
            diff[l] -= 1
            diff[0] += 1
            diff[hi - l + 1] -= 1
    g, acc = [], 0
    for c in range(l):
        acc += diff[c]
        g.append(acc)
    return g


def triangle(l, D, B):
    f = [0] * l
    for i in range(D + 1):
        for j in range(D + 1 - i):
            f[(i + B * j) % l] += 1
    return f


def cap(D):
    return D // 2 + 1


def orbit(B, l):
    inv = lambda x: pow(x % l, l - 2, l)
    Bi = inv(B)
    return {B % l, (1 - B) % l, Bi, (1 - Bi) % l, inv(1 - B),
            B * inv(B - 1) % l}


def cap_by_test(l, D, B):
    """The cap at (l, D, B) by the tests alone, or False: D = 0, or by
    duality (2d) D = l - 3, or by equicoverage (2c) D = l - 2; else the
    bounds (3) at D or its dual, over B's orbit under (2a), (2b)."""
    for Dp in (D, l - 3 - D):
        if Dp <= 0:
            return True
        for x in orbit(B, l):
            b = min(x, l + 1 - x)
            if b * Dp < l or Dp + 1 <= b <= (l - 1) // 2:
                return True
            if (b * Dp // l + 1) * (Dp // b + 1) <= cap(Dp):
                return True
    return False


def section_c():
    print("C  controls")
    ok1 = all(stair(l, D, 1)[0] == D + 1 > cap(D)
              for l in (11, 31) for D in range(2, l - 1))
    check("C1 B = 1 breaks the cap: g(0) = D + 1 at every D >= 2", ok1)
    ok2 = all(stair(l, D, 2)[(-D) % l] == cap(D)
              for l in (11, 31) for D in range(0, l - 1, 2))
    check("C2 B = 2 meets the cap at every even D, at c = -D", ok2)
    bad = 0
    for l, D, B in [(13, 5, 4), (23, 9, 5), (31, 14, 7), (47, 21, 12),
                    (61, 29, 44)]:
        g, f = stair(l, D, B), triangle(l, D, B)
        bad += sum(f[w] != g[(w - B * D) % l] for w in range(l))
        bad += sum(g[c] != sum((c + B * u) % l <= u for u in range(D + 1))
                   for c in range(l))
    check("C3 f(w) = g(w - B*D), and g is the lattice-translate count",
          bad == 0, "five systems, every class")


def section_y():
    print("Y  the symmetries")
    ba = bb = bd = 0
    for l in primes(5, 47):
        inv = lambda x: pow(x % l, l - 2, l)
        for D in range(0, l - 1):
            for B in range(2, l):
                g = stair(l, D, B)
                g1 = stair(l, D, (1 - B) % l)
                gi = stair(l, D, inv(B))
                ba += any(g[c] != g1[(-c) % l] for c in range(l))
                bb += any(g[c] != gi[(D - inv(B) * D + inv(B) * c) % l]
                          for c in range(l))
                if D < l - 2:
                    Dt = l - 3 - D
                    gt = stair(l, Dt, (1 - B) % l)
                    off = D + (3 - l) // 2
                    bd += any(g[c] != gt[(c - 2 * B + 1) % l] + off
                              for c in range(l))
    check("Y1 involution g_B(c) = g_(1-B)(-c)", ba == 0, "primes 5..47")
    check("Y2 time reversal", bb == 0, "primes 5..47")
    n = be = 0
    for l in range(5, 80):
        for B in range(2, l):
            if gcd(B, l) == 1 and gcd(B - 1, l) == 1:
                n += 1
                be += any(v != (l - 1) // 2 for v in stair(l, l - 2, B))
    check("Y3 equicoverage at D = l - 2", be == 0 and n > 1000,
          f"{n} systems, moduli 5..79, composite included")
    check("Y4 duality with D~ = l - 3 - D", bd == 0, "primes 5..47")


def section_o():
    print("O  one line and the product bound")
    top = 103
    bad = 0
    for l in primes(5, top):
        for D in range(1, l - 1):
            for b in range(2, (l + 1) // 2 + 1):
                bound = (b * D // l + 1) * (D // b + 1)
                for B in (b, (1 - b) % l):
                    bad += max(stair(l, D, B)) > bound
    check(f"O1 product bound against brute force, primes 5..{top}",
          bad == 0)
    hole = 0
    for l in primes(5, 211):
        for D in range(0, l - 1):
            if min(D, l - 3 - D) ** 2 < l:
                hole += sum(not cap_by_test(l, D, B) for B in range(2, l))
    check("O2 small-D corollary: min(D, D~)^2 < l closes every B",
          hole == 0, "primes 5..211")


def short_vec(B, l):
    """Shortest (t, s), t >= 1, s = B*t mod l taken signed; norm^2."""
    best = (0, l, l * l)
    t = 1
    while t * t < best[2]:
        s = B * t % l
        if s > l - s:
            s -= l
        if t * t + s * s < best[2]:
            best = (t, s, t * t + s * s)
        t += 1
    return best


def run_r(t, s):
    return s if s > t else (t if s >= 0 else t - s)


FAM2 = {Fraction(2), Fraction(-1), Fraction(1, 2)}
FAM34 = {Fraction(x) for x in (3, -2, Fraction(1, 3), Fraction(2, 3),
                               Fraction(3, 2), Fraction(-1, 2), 4, -3,
                               Fraction(1, 4), Fraction(3, 4),
                               Fraction(4, 3), Fraction(-1, 3))}


def section_l():
    print("L  the lattice lemmas and the families")
    bB = bD = 0
    for l in (211, 401):
        for B in range(2, l):
            t, s, n2 = short_vec(B, l)
            lam = sqrt(n2)
            for D in (l // 4 + 1, l // 3, (l - 3) // 2):
                gm = max(stair(l, D, B))
                bB += gm > D * D / (2 * l) + SQ2 * D / lam \
                    + SQ2 * lam * D / l + 1 + 1e-9
                if n2 < 49:
                    bD += gm > D * D / (2 * l) + SQ2 * lam * D / l \
                        + D // run_r(t, s) + 1 + 1e-9
    check("L1 lemma (B), every B", bB == 0, "l = 211, 401, three D")
    check("L2 lemma (D), every B with lam < 7", bD == 0)
    rng = random.Random(92)
    bC = nr = 0
    for _ in range(3000):
        D, t, s = rng.randint(10, 400), rng.randint(1, 6), rng.randint(-6, 6)
        if gcd(t, abs(s)) != 1:
            continue
        for _ in range(30):
            u0 = rng.randint(0, D)
            v0 = rng.randint(0, u0)
            n = 0
            while 0 <= v0 + n * s <= u0 + n * t <= D:
                n += 1
            bC += n > D // run_r(t, s) + 1
            nr += 1
    check("L3 lemma (C): runs never exceed floor(D/r) + 1", bC == 0,
          f"{nr} random runs")
    dirs = [(t, s) for t in range(1, 7) for s in range(-6, 7)
            if gcd(t, abs(s)) == 1 and s not in (0, t)
            and t * t + s * s < 49 and run_r(t, s) <= 4]
    fams = [Fraction(s, t) in FAM2 | FAM34 for t, s in dirs]
    check("L4 every short direction with r <= 4 is a family member",
          all(fams) and len(dirs) == 15, f"{len(dirs)} directions")
    top = 401
    bad = 0
    for l in primes(53, top):
        for a in (2, 3):
            for D in range(1, (l - 3) // 2 + 1):
                bad += max(stair(l, D, l - a)) > D / 3 + 2
    check(f"L5 the tents: gmax <= D/3 + 2 at B = -2, -3, primes "
          f"53..{top}", bad == 0)


def corners(l):
    """The closure's analytic conditions at l, as four + two margins."""
    lmax = 2 * sqrt(l / pi)
    out = []
    for lam in (7.0, lmax):
        for D in (sqrt(l), (l - 3) / 2):
            rhs = 0.5 - D / (2 * l) - 1 / (2 * D)
            out.append(rhs - (SQ2 / lam + SQ2 * lam / l))
    for D in (sqrt(l), (l - 3) / 2):
        out.append(0.5 - (D / (2 * l) + 9.9 / l + 0.2 + 1 / (2 * D)))
    return out


def section_x():
    print("X  the closure at l >= 213")
    m213 = corners(213)
    grid = [213 + k * k * 997 for k in range(0, 101)]
    check("X1 case 1 corners and case 2 ends hold at l = 213",
          min(m213) > 0, f"least margin {min(m213):.4f}")
    check("X2 and on a grid of l to 10^7", all(min(corners(l)) > 0
                                               for l in grid))
    ls = primes(213, 449) + [1009]
    rng = random.Random(214)
    total = unc = over = brute = sampled = 0
    for l in ls:
        inv = lambda x: pow(x % l, l - 2, l)
        f2 = {r.numerator * inv(r.denominator) % l for r in FAM2}
        f34 = {r.numerator * inv(r.denominator) % l for r in FAM34}
        for B in range(2, l):
            t, s, n2 = short_vec(B, l)
            lam = sqrt(n2)
            for D in range(0, (l - 3) // 2 + 1):
                total += 1
                if D * D < l:
                    continue
                if n2 >= 49:
                    bnd = D * D / (2 * l) + SQ2 * D / lam \
                        + SQ2 * lam * D / l + 1
                elif run_r(t, s) >= 5:
                    bnd = D * D / (2 * l) + SQ2 * lam * D / l \
                        + D // run_r(t, s) + 1
                elif B in f2:
                    continue
                elif B in f34:
                    bnd = D / 3 + 2
                else:
                    unc += 1
                    continue
                if bnd >= D / 2 + 0.5:
                    over += 1
                elif rng.random() < 0.002:
                    sampled += 1
                    brute += max(stair(l, D, B)) > bnd
    check(f"X3 the split: {total} triples at {len(ls)} primes, none "
          f"outside a case, every bound under target, {sampled} brute "
          f"samples under their bounds",
          unc == 0 and over == 0 and brute == 0)


def section_f():
    print("F  the finite leg")
    top = 211
    total = forced = bad = 0
    met = []
    for l in primes(2, top):
        for D in range(0, l - 1):
            for B in range(2, l):
                total += 1
                if cap_by_test(l, D, B):
                    continue
                forced += 1
                gm = max(stair(l, D, B))
                bad += gm > cap(D)
                if gm == cap(D):
                    met.append((l, D, B))
    check(f"F1 the cap at every prime l <= {top}, every D, every B",
          bad == 0, f"{total} triples, {forced} by brute force")
    print(f"       met with equality where the tests are silent: {met}")


def main():
    section_c()
    if not all(CHECKS):
        raise SystemExit("a control failed: no verdict is read")
    section_y()
    section_o()
    section_l()
    section_x()
    section_f()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
