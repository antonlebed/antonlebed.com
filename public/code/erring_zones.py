"""
erring_zones.py -- the continuum error of a cut set, the scaling limits
of the growing-width profiles, and the zone construction at reachable m.

QUESTION. Fill [0, c) with m intervals below one overflow label
[c, 2c - 1), the error as in erring_label.py, kappa_m the limsup over c
of the least error over c^2. A cut set P scaled by k has error / (kc)^2
tending to the continuum error E(P / c): each cell's area less its
largest label area, overflow [1, 2). What are the growing-width
profiles' limits, each an upper bound on kappa_m at its m, and what does
the zone construction (independent uniform phases per zone, the route
by which kappa_m -> 0) print at the m a run reaches?

DESIGN. cont_error computes E exactly: the area of a cell [A, A + a) x
[B, B + b) below t is G(t) - G(t - a) - G(t - b) + G(t - a - b),
G(t) = max(t, 0)^2 / 2, so a label's share is a difference of two such
areas. zones builds the construction: [0, t0) one interval, [t0, 1) cut
into zones of width D, zone k a grid of width eps z_k^p (z_k its start)
at a phase uniform on [0, w_k), zone ends cuts. bound prints the mean
bound B = main + 2 t0 + 4 (nz + 1) wmax + 2 (nz + 2) wmax, main the
integral over x, y >= t0, x + y < 1 of (w(x) + w(y)) / (4 w(x + y)) on a
midpoint grid; the edge terms are areas, far above what the edges cost.

PREDICTIONS AND KILLS (written before the run).
  C1 the continuum error of rounding's cut set (u = 0.8, m = 162) equals
     erring_label's error of its x16 scaling over c^2 within 0.002.
  L1..L4 the limits of the profiles p = 1 at m = 162 and 400, p = 2 at
     m = 400 (top 0.8, c = 4000) and p = 2 at m = 1000 (top 0.9,
     c = 10000): 0.0905..0.0908, 0.0857..0.0860, 0.0799..0.0802,
     0.0734..0.0740, each at or a little above its largest scaled
     reading. Kill: a limit less its largest scaled reading below
     -0.0005 or above +0.002 (cont_error and the scaling disagree).
  Z (written before the zone run, as a check of the bound) the mean of
     E over 8 seeds at most B; at the scales a run reaches B's edge
     areas dwarf main, so Z prints beside its bound and checks nothing.

FINDINGS (from the printed run; both controls passed first: C1 0.1030
against 0.1030 at m = 162, the s = 3 form exact).
  L1..L4 held, the kill silent: the limits print 0.09054, 0.08572,
     0.08000 and 0.07380, against the largest scaled readings 0.0905,
     0.0857, 0.0799 (x16) and 0.0734 (x4). So kappa_162 < 0.0906,
     kappa_400 < 0.0801 and kappa_1000 < 0.0739.
  Z: mean E 0.2285 (p = 1, eps 0.005, D = t0 = 0.1, m near 575)
     against B 0.5536; 0.1684 (p = 1, eps 0.0025, D = t0 = 0.05, m near
     1438) against 0.4870; 0.2074 and 0.2094 (p = 2, D = t0 = 0.1, eps
     0.01 and 0.005, m near 1550 and 3090) against 0.7448 and 0.4937.
     Eight seeds spread under 0.0014 in every case. At t0 = 0.1 the
     means sit near the 2 t0 = 0.2 the one bottom interval costs, and
     halving eps at p = 2 moved E up by 0.0020: at reachable m the
     bottom interval carries the error, and the construction errs above
     rounding's 1/10. kappa_m -> 0 rests on its proof, not on this run.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np  # noqa: E402

from erring_label import error, rounding  # noqa: E402
from erring_widths import profile_at, ratio  # noqa: E402

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tail = f"  ({detail})" if detail else ""
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{tail}")


def G(t):
    t = np.maximum(t, 0.0)
    return t * t / 2


def below(a, b, t):
    """Area of {(u, v) in [0, a) x [0, b) : u + v < t}."""
    return G(t) - G(t - a) - G(t - b) + G(t - a - b)


def cont_error(cuts):
    """Continuum error of cuts 0 = c_0 < ... < c_m = 1, overflow [1, 2)."""
    C = np.asarray(cuts, dtype=float)
    lab = np.append(C, 2.0)
    A, W = C[:-1], np.diff(C)
    return sum(_rows(lab, A, W, i, i + 128) for i in range(0, len(W), 128))


def _rows(lab, A, W, i, j):
    """The error of the cells whose first summand is interval i..j - 1."""
    base = (A[i:j, None] + A[None, :]).ravel()
    a = np.broadcast_to(W[i:j, None], (len(W[i:j]), len(W))).ravel()
    b = np.broadcast_to(W[None, :], (len(W[i:j]), len(W))).ravel()
    lo = np.searchsorted(lab, base, side="right") - 1
    hi = np.searchsorted(lab, base + a + b, side="left") - 1
    best = np.zeros_like(base)
    K = 8
    for k in range(K + 1):
        L = np.minimum(lo + k, len(lab) - 2)
        land = (below(a, b, lab[L + 1] - base) - below(a, b, lab[L] - base))
        best = np.maximum(best, np.where(lo + k <= hi, land, 0.0))
    for i in np.flatnonzero(hi - lo > K):
        L = np.arange(lo[i], hi[i] + 1)
        land = (below(a[i], b[i], lab[L + 1] - base[i])
                - below(a[i], b[i], lab[L] - base[i]))
        best[i] = land.max()
    return float((a * b - best).sum())


def zones(p, eps, D, t0, rng):
    """[0, t0) one interval; zones of width D on [t0, 1), each a grid of
    width eps z^p (z the zone start) at an independent uniform phase."""
    cuts = [0.0, t0]
    z, ws = t0, []
    while z < 1 - 1e-12:
        z2 = min(z + D, 1.0)
        w = eps * z ** p
        ws.append(w)
        t = z + rng.uniform(0, w)
        while t < z2 - 1e-12:
            if t > cuts[-1] + 1e-12:
                cuts.append(t)
            t += w
        cuts.append(z2)
        z = z2
    return cuts, ws


def bound(p, eps, D, t0, n=1500):
    """B: main by a midpoint grid of n x n over [t0, 1)^2, plus areas."""
    starts = np.arange(t0, 1 - 1e-12, D)
    wz = eps * starts ** p

    def w(x):
        return wz[np.minimum(((x - t0) / D).astype(int), len(wz) - 1)]
    h = (1 - t0) / n
    x = t0 + (np.arange(n) + 0.5) * h
    X, Y = np.meshgrid(x, x)
    S = X + Y
    ok = S < 1
    main = float(((w(X) + w(Y)) / (4 * w(np.where(ok, S, X))))[ok].sum()
                 * h * h)
    nz, wmax = len(wz), float(wz.max())
    return main, main + 2 * t0 + 4 * (nz + 1) * wmax + 2 * (nz + 2) * wmax


def section_controls():
    print("controls")
    cu = rounding(4000, 0.8 * 4000 / 160, 0.8)
    m = len(cu) - 1
    c = 4000 * 16
    disc = error(tuple(16 * x for x in cu) + (2 * c - 1,), 2 * c - 1) / c / c
    cont = cont_error([x / 4000 for x in cu])
    check("C1: continuum error of rounding equals its x16 scaling",
          abs(disc - cont) < 0.002, f"m = {m}, {cont:.4f} against {disc:.4f}")
    two = cont_error([0, 0.3, 1])
    want = 3 * 0.3 ** 2 / 2 + 0.4 ** 2 / 2
    check("control: one cut at 0.3 is the s = 3 continuum form "
          "3a^2/2 + (1 - 2a)^2/2", abs(two - want) < 1e-12,
          f"{two:.6f} against {want:.6f}")


def section_limits(cases):
    """L1..L4: each profile cut set's continuum error, its limit under
    scaling, against its largest scaled reading."""
    print("profile limits: the continuum error of each cut set")
    for c, p, m, u, k in cases:
        cu = profile_at(c, p, m, u)
        lim = cont_error([x / c for x in cu])
        last = ratio(tuple(k * x for x in cu), k * c)
        print(f"    m = {m}  p = {p}  top {u}  c = {c}: limit {lim:.5f}, "
              f"x{k} {last:.4f}, limit - x{k} {lim - last:+.4f}")
        check(f"limit against x{k} at m = {m}, p = {p}",
              -0.0005 <= lim - last <= 0.002)


def section_zones(cases, seeds=8):
    """Z: the construction's mean error over seeds beside its bound B."""
    print("zone construction: mean E over seeds beside the bound B")
    for p, eps, D, t0 in cases:
        Es, ms = [], []
        for s in range(seeds):
            cuts, _ = zones(p, eps, D, t0, np.random.default_rng(s))
            ms.append(len(cuts) - 1)
            Es.append(cont_error(cuts))
        main, B = bound(p, eps, D, t0)
        print(f"    p = {p}  eps = {eps}  D = {D}  t0 = {t0}  m {min(ms)}.."
              f"{max(ms)}: E mean {np.mean(Es):.4f}, seeds {min(Es):.4f}.."
              f"{max(Es):.4f}; main {main:.4f}, B {B:.4f}")


def main():
    section_controls()
    if not all(CHECKS):
        print("\nCONTROL FAILED: nothing below is read.")
        raise SystemExit(1)
    section_limits([(4000, 1, 162, 0.8, 16), (4000, 1, 400, 0.8, 16),
                    (4000, 2, 400, 0.8, 16), (10000, 2, 1000, 0.9, 4)])
    section_zones([(1, 0.005, 0.1, 0.1), (1, 0.0025, 0.05, 0.05),
                   (2, 0.01, 0.1, 0.1), (2, 0.005, 0.1, 0.1)])
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
