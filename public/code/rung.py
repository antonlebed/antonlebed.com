"""rung.py -- the weight of every point of a field's jump set but the
first is the highest landing of one class of units: the jump set is the
staircase of the class maxima.

QUESTION. Let K/Q_p be totally ramified of degree e, cut out by an
Eisenstein F with root pi and u = p/pi^e (triangle.py), holding zeta_p
but not zeta_(p^2), so the bend s = e/(p - 1) = c_0 p^M, p not dividing
c_0, and e* = p s. For 0 <= m <= M the CLASS Gamma_m = (s/p^m, m) is the
units of level exactly s/p^m, whose p^m-th powers reach level s; a unit
z LANDS at v(z^(p^(m+1)) - 1) (tame.py). weld.py showed the weight of
the second point of Pagano's jump set is the highest landing of the
seat class Gamma_M. What do the other classes' landings read, and does
the whole jump set come out of them?

THE DERIVATION (on paper, before the engine).
  (1) THE CLASS MAXIMUM IS g(m) + e. Let g(n) be the largest
      v(zeta_p h - 1) over h in H_n = U_1^(p^n) (weld.py; g(0) is
      infinite, h = zeta_p^(-1)). The units of level s in H_m are
      exactly the p^m-th powers of the units of Gamma_m: rho(i) = min(p i,
      i + e) is strictly increasing, a level passing s never returns to
      it, and a level below s/p^m stays below s. For y of level s,
      v(y^p - 1) > e* (zeta_p in K forces ubar = -1), and if it is e* +
      j then y^p = y'^p with y' in U_(s+j) (above the bend the p-th
      power carries each level onto the level e higher), so
      y = zeta_p^a y' with a prime to p and
          v(y^p - 1) = e* + v(zeta_p^(-a) y - 1) - s.
      For b with a b = -1 mod p, (zeta_p^(-a) y)^b = zeta_p y^b with y^b
      in H_m, and a power prime to p keeps a 1-unit's level, so every
      landing of Gamma_m is at most e* + g(m) - s = g(m) + e. Conversely
      let h in H_m attain g(m) > s and put x = zeta_p h. Then y := h^(-1)
      = zeta_p x^(-1) lies in H_m at level s, a = 1, and zeta_p^(-1) y
      = x^(-1) has level g(m). So the class attains e* + g(m) - s, and
          max landing of Gamma_m = g(m) + e = rho(g(m)),
      using g(m) > s for m <= M. No outside theorem is used in (1).
  (2) THE STAIRCASE (Pagano, Proposition 3.39, N = 1, as weld.py (1)).
      g(n) is the least rho^(beta(i) - 1)(i) over the points with
      beta(i) <= n, so with rho increasing the class maximum is
          H(m) = min{ rho^beta(i)(i) : beta(i) <= m },
      the weight of the point with the largest beta at most m: every
      point's weight but the first's, (c_0, M + 1)'s, is a class
      maximum, the maxima are non-increasing in m, and they drop
      exactly at the points' beta. The jump set is H's
      staircase: the first point (c_0, M + 1) at e*, and at each beta in
      1..M with H(beta) < H(beta - 1) (H(0) infinite) the point (i,
      beta), i the pullback of H(beta) through rho^beta into T*.
  (3) THE FLOOR. The readouts give the least landing of Gamma_m as e* +
      min(dep_m, X_m), the whole class landing there when dep_m < X_m
      (tame.py at odd p and at c >= 2 over 2, dep = l, X = p^m; wild.py
      at the top class over 2, dep = lam, X = 3e/2). A rigid class has
      H(m) = e* + dep_m < e* + X_m; otherwise H(m) >= e* + X_m. So the
      least landing is min(H(m), e* + X_m): every class's spectrum lies
      in [min(H(m), e* + X_m), H(m)], both ends attained, read by the
      jump set and the class's own floor with no departure named.
  (4) THE SECOND POINT IN CLOSED FORM. At a rigid seat (dep < X, M >=
      1) the second point has weight e* + dep with dep < e (X <= s < e
      except at the top class over 2, where N = 1 gives lam <= e,
      weld.py). Its pullback: e* + dep > e*, so one step back is s + dep,
      in (s, e*); while the value is divisible by p it pulls back by p
      (below the bend), and v_p(s + dep) = v_p(dep) < M. So
          (i_2, beta_2) = ((s + dep)/p^(v_p(dep)), v_p(dep) + 1),
      except dep = e (the top class over 2 at lam = e), where s + dep =
      e* lies in T* and (i_2, beta_2) = (e*, 1).

THE ENGINE. g(n) from weld.py's filtered echelon of H_n. The class
maxima by brute force, g setting only how many digits K the enumeration
carries: every unit of Gamma_m written to K
digits past its level, z = 1 + pi^c (a_0 + ... + a_(K-1) pi^(K-1)),
a_0 != 0 (tame.py's landings). A factor from U_(c+K) moves the landing
only at or above rho^(m+1)(c + K), and every truncation is itself a
unit of Gamma_m, so with rho^(m+1)(c + K) > g(m) + e the largest landing
over the truncations is the class maximum and every smaller landing is
exact; K is the least such, at least 4, and a class with more than
CAP truncations is skipped and counted. m = 0 is not enumerated:
zeta_p lies in Gamma_0 and its landing is at precision (weld.py C).

TRANSPLANTS. The bracket [min(R, Phi), R] is the record this script
replaces; nothing of it is used. Pagano's Proposition 3.39 enters only
at (2); (1) and the brute maxima never use it.

PREDICTIONS, fixed before the run.
  C  CONTROL, run first. The brute staircase (g setting only K) reproduces the
     module-basis points of two fields: x^6 + 3x^3 + 3 at p = 3 reads
     (1, 2), (7, 1); x^12 - 2 at p = 2 reads (3, 3), (9, 2), (21, 1),
     that is H(2) = 30, H(1) = 33.
  R  THE CLASS MAXIMUM. At every field and every 1 <= m <= M enumerated:
     the largest brute landing of Gamma_m equals g(m) + e.
  S  THE STAIRCASE. At every field with all classes enumerated, the set
     rebuilt from the brute maxima by (2) equals weld.py's jump_set(g).
  F  THE FLOOR. At every enumerated class the least brute landing is
     min(H(m), e* + X_m), and the class is one value iff dep_m < X_m.
  P  THE SECOND POINT. At every rigid seat with M >= 1 the second point
     of jump_set(g) is (4)'s closed form.
  Populations: odd p at (3, 6), (3, 12), (3, 18), (5, 20), (3, 36);
  over 2 the heads e = 4, 8, 16 and c_0 > 1 at e = 12, 20, 24; every
  departure 1..X + 2 and infinity (lam to e at the heads, lam > e
  holding i), deeper digits random. A field with zeta_(p^2) is set
  aside and counted.
KILLS, as printed observables: a C line off (nothing below is read);
one enumerated class whose brute maximum differs from g(m) + e; one
field whose brute staircase differs from jump_set(g); one class whose
least landing differs from min(H(m), e* + X_m) or whose rigidity
differs from dep_m < X_m; one rigid seat off the closed form.

FINDINGS. Every prediction landed: 6/6 checks PASS, no kill fired.
  C  The brute maxima alone rebuild x^6 + 3x^3 + 3's (1, 2), (7, 1)
     (H(1) = 13) and x^12 - 2's (3, 3), (9, 2), (21, 1) (H = 33, 30).
  R  238 classes over 101 fields: every brute maximum is g(m) + e.
  S  At the 100 fields with every class enumerated, the staircase of
     the brute maxima is jump_set(g), 0 off; it holds up to four points
     (p = 2, e = 24, l infinite: (3, 4), (9, 3), (21, 2), (45, 1)).
  F  At all 238 classes the least landing is min(H(m), e* + X_m), and
     a class is one value exactly when dep_m < X_m.
  P  At the 69 rigid seats the second point is the closed form, among
     them (4, 2) at p = 3, e = 18, l = 3, and (e*, 1) = (32, 1) at
     e = 16, lam = 16.
  Two fields at e = 4 held i and were set aside; one class (p = 3,
  e = 36, l infinite, m = 1) exceeded CAP and was skipped.
  Tiers: (1) and (3) a theorem, needing no outside result; (2) and (4)
  a theorem given Pagano's Proposition 3.39.

RUN RECORD. 6/6, 14.3 s wall, peak working set 12.1 MB under a memory guard,
green on the first run.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import random

from module_law import check, section, CHECKS, vp
from tame import departure, designed, local, landings, INF
import wild
from weld import read_field, jump_set, pullback, rho

SEED = 1427
CAP = 6000


def class_dep(p, e, b, d, c):
    """(dep_m, X_m) of the class of level c."""
    if p == 2 and c == 1:
        return wild.wild_departure(e, b, d), 3 * e // 2
    s = e // (p - 1)
    return departure(p, e, b, d), s // c


def digits_needed(p, e, c, m, H):
    K = 4
    while True:
        x = c + K
        for _ in range(m + 1):
            x = rho(p, e, x)
        if x > H:
            return K
        K += 1


def brute(p, e, b, d, rec):
    """{m: (max, min, set)} over the enumerated classes 1 <= m <= M."""
    loc = local(p, e, b, d)
    s, g, out, skipped = rec["s"], rec["g"], {}, 0
    for m in range(1, rec["M"] + 1):
        c = s // p ** m
        K = digits_needed(p, e, c, m, g[m] + e)
        if (p - 1) * p ** (K - 1) > CAP:
            skipped += 1
            continue
        land, ok, top = landings(loc, c, m, K)
        assert ok
        out[m] = (max(land), min(land), set(land), top)
    return out, skipped


def staircase(p, e, s, M, H):
    """The jump set rebuilt from the class maxima H[1..M] alone."""
    c0 = s // p ** M
    pts, prev = [(c0, M + 1)], None
    for bt in range(1, M + 1):
        if prev is None or H[bt] < prev:
            pts.append((pullback(p, e, H[bt], bt), bt))
        prev = H[bt]
    return sorted(pts)


def second_closed(p, e, dep):
    s = e // (p - 1)
    if dep == e:
        return (p * s, 1)
    k = vp(dep, p)
    return ((s + dep) // p ** k, k + 1)


# ------------------------------------------------------------ populations

ODD = [(3, 6), (3, 12), (3, 18), (5, 20), (3, 36)]
HEADS = [4, 8, 16]
EVEN = [12, 20, 24]


def population(rng):
    out = []
    for (p, e) in ODD:
        s = e // (p - 1)
        X = p ** vp(s, p)
        for l in list(range(1, X + 3)) + [INF]:
            b, d = designed(rng, p, e, l, 2 * e + s)
            out.append((f"l={'inf' if l >= INF else l}", p, e, b, d))
    for e in HEADS:
        for lam in range(1, e + 1):
            b, d = wild.designed(rng, e, lam, 2 * e + 4)
            out.append((f"lam={lam}", 2, e, b, d))
        for _ in range(2):
            b, d = wild.random_poly(rng, e)
            out.append(("random", 2, e, b, d))
    for e in EVEN:
        X = 2 ** vp(e, 2)
        for l in list(range(1, X + 3)) + [INF]:
            b, d = wild.designed_l(rng, e, l, 2 * e + 4)
            out.append((f"l={'inf' if l >= INF else l}", 2, e, b, d))
    return out


# ------------------------------------------------------------ sections

CONTROLS = [("x^6 + 3x^3 + 3", 3, 6, [0, 0, 0, 1, 0, 0], -1,
             [(1, 2), (7, 1)]),
            ("x^12 - 2", 2, 12, [0] * 12, 1, [(3, 3), (9, 2), (21, 1)])]


def section_control(rng):
    section("C  CONTROL: the brute staircase reproduces printed points")
    for name, p, e, b, d, want in CONTROLS:
        rec = read_field(p, e, b, d)
        br, skipped = brute(p, e, b, d, rec)
        H = {m: br[m][0] for m in br}
        pts = (staircase(p, e, rec["s"], rec["M"], H)
               if skipped == 0 else None)
        check(f"C {name}: {want}", pts == want,
              f"H = {H}, rebuilt {pts}")


def section_classes(rng):
    section("R, S, F, P  THE CLASS MAXIMA, THE STAIRCASE, THE FLOOR, "
            "THE SECOND POINT")
    bad = dict(R=0, S=0, F=0, P=0)
    n = dict(R=0, S=0, F=0, P=0, aside=0, skipped=0, fields=0)
    for label, p, e, b, d in population(rng):
        rec = read_field(p, e, b, d)
        g, s, M, L = rec["g"], rec["s"], rec["M"], rec["L"]
        if g[1] >= L:
            n["aside"] += 1
            continue
        es = rec["es"]
        n["fields"] += 1
        br, skipped = brute(p, e, b, d, rec)
        n["skipped"] += skipped
        H, row = {}, []
        for m, (hi, lo, vals, _) in sorted(br.items()):
            H[m] = hi
            n["R"] += 1
            okR = hi == g[m] + e
            bad["R"] += not okR
            dep, X = class_dep(p, e, b, d, s // p ** m)
            n["F"] += 1
            okF = lo == min(hi, es + X) and ((len(vals) == 1) ==
                                             (dep < X))
            bad["F"] += not okF
            row.append(f"m={m}:[{lo - es},{hi - es}]")
            if not (okR and okF):
                print(f"    OFF p={p} e={e} {label} m={m}: brute "
                      f"[{lo},{hi}] g+e={g[m] + e} dep={dep} X={X} "
                      f"values {sorted(vals)}")
        pts = jump_set(p, e, g, M + 2)
        if skipped == 0:
            n["S"] += 1
            st = staircase(p, e, s, M, H)
            bad["S"] += st != pts
            if st != pts:
                print(f"    OFF p={p} e={e} {label}: staircase {st}, "
                      f"g's {pts}")
        dep, X = class_dep(p, e, b, d, s // p ** M)
        if M >= 1 and dep < X:
            n["P"] += 1
            want = second_closed(p, e, dep)
            bad["P"] += pts[1] != want
            if pts[1] != want:
                print(f"    OFF p={p} e={e} {label}: second point "
                      f"{pts[1]}, closed form {want}")
        print(f"  p={p} e={e:2d} {label:8s} points {pts}  "
              f"excess brackets {' '.join(row)}")
    print(f"  {n['fields']} fields read, {n['aside']} set aside "
          f"(zeta_p^2 in K), "
          f"{n['skipped']} classes over CAP skipped")
    check("R every class maximum is g(m) + e", bad["R"] == 0,
          f"{n['R']} classes, {bad['R']} off")
    check("S the brute staircase is jump_set(g)", bad["S"] == 0,
          f"{n['S']} fields, {bad['S']} off")
    check("F least landing min(H, e* + X), one value iff dep < X",
          bad["F"] == 0, f"{n['F']} classes, {bad['F']} off")
    check("P the rigid seat's second point in closed form", bad["P"] == 0,
          f"{n['P']} fields, {bad['P']} off")


def main():
    rng = random.Random(SEED)
    section_control(rng)
    if not all(CHECKS):
        print("\ncontrol failed: nothing below is read")
        raise SystemExit(1)
    section_classes(rng)
    print()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks PASS")
    if not all(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
