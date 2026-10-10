"""
erring_widths.py -- does a width profile growing with position err
locally below rounding's quarter?

QUESTION. Fill [0, c) with m intervals below the overflow label
(N = 2c - 1), the error as in erring_label.py. Rounding (equal widths,
one wide top [uc, c)) errs on a quarter of its fine pairs and tends to
1/10. Does a profile w(t) = g c (t/c)^p, widths at least 1, err less at
the same m, and how does the least error per c^2 fall with m?

THE ARGUMENT (written before this script). A cell of widths a, b sums
over an interval of width a + b at x + y, where the label has width
W(x + y); it errs nowhere unless a cut lies inside. At a phase spread
over the cells it straddles with chance about (a + b)/W, then errs on
between 1/6 (a = b) and 1/4 (a << b) of its pairs. Rounding has
a = b = W, a block twice its label, aligned at the best phase: 1/4.
Under t^p, (a + b)/W averages 2/(p + 1) over the triangle, so the local
error falls like 1/p; the uniform phase is a transplant the run decides.

PREDICTIONS AND KILLS (written before the run).
  W1 at c = 4000, m near 34, 66, 162: some profile with p >= 2 prints
     e/c^2 below rounding's best (u over 0.70..0.90) at the same m.
  W2 p = 2 at m near 160 prints below 0.095; p = 3 below p = 2 at large
     enough m.
  W3 at fixed m the best profile's e/c^2 moves under 2% from c = 2000
     to c = 4000.
  K-floor: the lean "1/10 is the limit" dies if a profile prints
     e/c^2 < 0.095 at c = 4000 and within 2% at c = 2000.
  K-power: the heuristic dies if no profile at p = 2, 3, 4 prints below
     rounding's best at the same m for any m in 34..400 at c = 4000.

  W4 (written after W1..W3's prints) at m = 1000, c = 10000, the best
     profile over p = 1, 2, 3 and top None, 0.8, 0.9 prints below 0.0785
     (m = 400's best), holding within 2% scaled x2, and its p is >= 2.
     Dies (the fall stalls) if the best is above 0.0785.

FINDINGS (from the printed run; both controls passed first).
  K-floor fired: m = 400, p = 1, top 0.8 prints 0.0852 at c = 4000, and
     the same cut set scaled x2 to x16 prints 0.0854 to 0.0857 against
     rounding's 0.1012 to 0.1009. 1/10 is rounding's limit, not a floor:
     at m = 162 the p = 1, top 0.8 cut set prints 0.0905 at every scale
     x1 to x16 (rounding 0.1027 to 0.1029). On the reading it froze, the
     re-tuned c = 2000 prints 0.0837, within 2% of 0.0852.
  K-power survived: at m = 400, p = 2 (top 0.8) prints 0.0785 and p = 3
     (top 0.8) 0.1005 against rounding's 0.1022. At p = 1 a profile beats
     rounding's best from m = 66 (top 0.8: 0.1034 against 0.1068), not at
     m = 34 (best 0.1362 against 0.1120, the widest label 800 of 4000).
  W1 failed: no p >= 2 profile beats rounding at m <= 162; p = 1
     (geometric widths) does from m = 66.
  W2 failed: p = 2 at m = 162 prints 0.1183 at best; p = 3 is above
     p = 2 at every m run (m = 400: 0.1005 against 0.0785). The profile
     spends its labels on singletons near 0 (p = 3, m = 400: 299), so
     larger p needs larger m.
  W3 failed on the re-tuned reading it froze: re-tuned at c/2 the
     profiles print 1.8 to 9.6% lower (m = 400, p = 2: 0.0710 against
     0.0785). The reading kappa_m needs is
     the same cut set scaled.
  W4 held on the row run: m = 1000, c = 10000, p = 2, top 0.9 prints
     0.0723, scaled x2 0.0731 (1.1%), x4 0.0734; rounding 0.1017, 0.1007,
     0.1004. (Its comparison over p = 1, 2, 3 and three tops, and so its
     clause that the best p is >= 2, is not run here.)
  The scaled readings rise with the scale, the increments shrinking:
  0.0785, 0.0793, 0.0796, 0.0798, 0.0799 at m = 400, p = 2, x1 to x16.
  Each cut set's limit as it is scaled is its continuum error, an upper
  bound on kappa_m; the run prints the approach, not the limit. The hand
  estimate for p = 1, top 0.8: the local error at uniform phase, v =
  x/(x + y) uniform, prints phi_1 = 0.1989 (section_phi; 1/4 at a flat
  block, 1/6 at a triangle), so 0.64 x 0.1989/2 + 0.02 = 0.0836, against
  0.0857 at m = 400, x16. The uniform phase is a transplant here; the
  widths are a companding quantizer's (steps 1/G'(t), p = 1 the
  logarithmic compressor of mu-law), and only the constants are the
  run's.

CONTROLS. The fast error equals erring_label.error on every cut set at
N = 12, s = 2..5, and on rounding at c = 2000, w = 100; rounding at
c = 2000 reprints 0.1301 at w = 100.
"""

from bisect import bisect_right

from erring_label import below, error, cutsets, rounding

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tail = f"  ({detail})" if detail else ""
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{tail}")


def fast_error(cuts, N):
    """error(cuts, N), reading only the labels each cell's sums meet."""
    s = len(cuts) - 1
    E = 0
    for a in range(s):
        u1, n1 = cuts[a], cuts[a + 1] - cuts[a]
        for b in range(s):
            u2, n2 = cuts[b], cuts[b + 1] - cuts[b]
            base = u1 + u2
            if base >= N:
                continue
            tot = below(n1, n2, N - base)
            top = min(base + n1 + n2 - 2, N - 1)
            lo = bisect_right(cuts, base) - 1
            hi = bisect_right(cuts, top) - 1
            if lo == hi:
                continue
            best = 0
            for L in range(lo, hi + 1):
                k = (below(n1, n2, min(cuts[L + 1], N) - base)
                     - below(n1, n2, cuts[L] - base))
                best = max(best, k)
            E += tot - best
    return E


def profile(c, p, g, u=None):
    """Cuts of the profile t -> t + max(1, round(g c (t/c)^p)) on [0, U),
    U = c or the top cut u c, then [U, c) as one top label."""
    U = c if u is None else round(u * c)
    cuts = [0]
    t = 0
    while True:
        t = t + max(1, round(g * c * (t / c) ** p))
        if t >= U:
            break
        cuts.append(t)
    cuts.append(U)
    if U < c:
        cuts.append(c)
    return tuple(cuts)


def profile_at(c, p, m, u=None):
    """A profile with m intervals, g found by bisection (None if missed)."""
    lo, hi = 1e-9, 1e3
    for _ in range(200):
        g = (lo * hi) ** 0.5
        k = len(profile(c, p, g, u)) - 1
        if k == m:
            return profile(c, p, g, u)
        if k > m:
            lo = g
        else:
            hi = g
    return None


def round_at(c, m, u):
    """Rounding with m intervals: m - 2 cuts below the top u c."""
    w = u * c / (m - 2)
    cuts = rounding(c, w, u)
    return cuts if len(cuts) - 1 == m else None


def ratio(cuts, c):
    return fast_error(cuts + (2 * c - 1,), 2 * c - 1) / c / c


def section_controls():
    print("controls")
    bad = n = 0
    for s in range(2, 6):
        for cu in cutsets(12, s):
            n += 1
            bad += fast_error(cu, 12) != error(cu, 12)
    check("control: fast error equals error() at N = 12", bad == 0,
          f"{n} cut sets, {bad} faults")
    cu = rounding(2000, 100, 0.8) + (3999,)
    e1, e2 = fast_error(cu, 3999), error(cu, 3999)
    check("control: fast error equals error() on rounding, c = 2000, w = 100",
          e1 == e2 and f"{e1 / 4e6:.4f}" == "0.1301", f"{e1}, {e2}")


US = (0.70, 0.74, 0.78, 0.80, 0.82, 0.86, 0.90)


def best_round(c, m):
    out = []
    for u in US:
        cu = round_at(c, m, u)
        if cu:
            out.append((ratio(cu, c), u))
    return min(out) if out else (None, None)


def section_profiles(c, ms, ps, tops):
    print(f"profiles against rounding, c = {c}")
    rows = {}
    for m in ms:
        r, ru = best_round(c, m)
        print(f"    m = {m:3d}  rounding best {r:.4f} (u = {ru})")
        for p in ps:
            for u in tops:
                cu = profile_at(c, p, m, u)
                if cu is None:
                    print(f"      p = {p}  top {u}: no g gives m = {m}")
                    continue
                e = ratio(cu, c)
                rows[(m, p, u)] = e
                ones = sum(1 for i in range(len(cu) - 1)
                           if cu[i + 1] - cu[i] == 1)
                print(f"      p = {p:3}  top {str(u):4}  e/c^2 = {e:.4f}"
                      f"{'  < rounding' if e < r else ''}"
                      f"  singletons {ones}, widest {max(cu[i + 1] - cu[i] for i in range(len(cu) - 1))}")
        rows[(m, "round")] = r
    return rows


def section_scale(cases, c=4000, ks=(1, 2, 4)):
    """W3: the same shape at fixed m, scaled; and as frozen, re-tuned at
    c/2."""
    print(f"fixed m: the c = {c} cut set scaled, and re-tuned at {c // 2}")
    for m, p, u in cases:
        cu = profile_at(c, p, m, u)
        row = [ratio(tuple(k * x for x in cu), c * k) for k in ks]
        re = profile_at(c // 2, p, m, u)
        r2 = ratio(re, c // 2) if re else float("nan")
        rr = [best_round(c * k, m)[0] for k in ks]
        print(f"    m = {m} p = {p} top {u}: scaled "
              + ", ".join(f"x{k}" for k in ks) + " "
              + ", ".join(f"{x:.4f}" for x in row)
              + f"; re-tuned c = {c // 2} {r2:.4f}; rounding "
              + ", ".join(f"{x:.4f}" for x in rr))


def section_phi(n=600):
    """The p = 1 local error at uniform phase: U[0, a] + U[0, 1 - a]
    against a cut at a uniform offset of [0, 1), a = min(v, 1 - v), the
    mean of min(F, 1 - F) over the offset and v, both by midpoints."""
    def cdf(t, a, b):
        if a == 0:
            return t / b
        if t <= a:
            return t * t / (2 * a * b)
        if t <= b:
            return (t - a / 2) / b
        s = a + b - t
        return 1 - s * s / (2 * a * b)
    tot = 0.0
    for i in range(n):
        v = (i + 0.5) / n
        a, b = min(v, 1 - v), max(v, 1 - v)
        tot += sum(min(x, 1 - x) for x in
                   (cdf((j + 0.5) / n, a, b) for j in range(n))) / n
    phi = tot / n
    print(f"phi_1 = {phi:.4f} (flat block 1/4, triangle 1/6); at u = 0.8 "
          f"the estimate 0.64 phi/2 + 0.02 = {0.64 * phi / 2 + 0.02:.4f}")


def main():
    section_controls()
    if not all(CHECKS):
        print("\nCONTROL FAILED: nothing below is read.")
        raise SystemExit(1)
    section_profiles(4000, (34, 66, 162, 400), (1, 2, 3), (None, 0.8, 0.9))
    section_scale([(162, 1, 0.8), (400, 1, 0.8), (400, 2, 0.8)],
                  ks=(1, 2, 4, 8, 16))
    section_scale([(1000, 2, 0.9)], c=10000, ks=(1, 2, 4))
    section_phi()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
