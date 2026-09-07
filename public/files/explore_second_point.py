"""explore_second_point.py — THE SECOND FRONTIER POINT FROM THE DIGITS:
is the jump set's second weight the tail of zeta_p past its leading
basis monomial, and is that tail the window defect, at every p?

THE QUESTION. The rung theorem brackets every arrival class's landing
spectrum by Pagano's frontier, [min(R_c, Phi_c), R_c], with R_c the
first frontier weight of order <= m (explore_rung_odd.py). The tame
readout theorem prices the same minimum as e* + min(delta_w, p^m),
delta_w = v(w - 1) the window defect of w = -p/pi^e (2/pi^e at p = 2;
explore_tame_readout.py). The two agree at every class read, so the
second frontier weight w_2 obeys min(w_2 - e*, p^M) = min(delta_w,
p^M) — a weld of two theorems. This rig asks whether the weld is a
DERIVATION: whether the module alone reads the second point off the
digits of w, which would make the tame readout theorem, and the p = 2
readout theorem's top-class law with its skeleton constants, a
corollary of the structure theorem.

THE OBJECTS (explore_jump_set.py and explore_rung_odd.py conventions).
K = Q_p[x]/(F), F Eisenstein of degree e, f = 1, seat i* = c_0 p^M
with p not dividing c_0, e* = p i* = i* + e, rho(i) = min(p i, i + e),
T* = {a < e* : p not dividing a} u {e*}; the pullback of a level L is
the unique (a, b) with a in T* and rho^b(a) = L. The relation is
r = p dlog(zeta_p); its frontier (I, beta) is the jump set; w_2 is
the weight of the second frontier point. B := (1 + pi^(c_0))^(d p^M)
is the seat's basis monomial, d the leading digit of zeta_p - 1 at
level i*; u' := zeta_p / B; tau := v(u' - 1) - i* is THE TAIL of
zeta_p past its leading basis monomial.

THE HAND DERIVATION (on paper, before the engine).

H1  THE PULLBACK LEMMA. A level L in (i*, e*) has v_p(L) >= M iff
    L = i* + j p^M for some j >= 1, since then L = (c_0 + j) p^M; a
    level L = a p^b with b <= M - 1 has a > c_0 p^(M-b) >= c_0. So the
    coordinate of dlog(u') at weight i* + tau, whose r-order is b + 1
    and r-weight rho(i* + tau) = e* + tau, is undominated by the first
    point (c_0, M + 1) iff p^M does not divide tau: w_2 - e* = tau
    when p^M does not divide tau, and w_2 - e* > tau when it does
    (tau < e throughout).
H2  THE EQUATION AT THE SEAT. zeta_p = 1 + y, y = d pi^i* (1 + t).
    Dividing (1 + y)^p = 1 by y, with p = -w pi^e and C(p, k) = p c_k:
    (1 + t)^(p-1) = w (1 + c_2 y + c_3 y^2 + ...), c_2 = (p - 1)/2.
H3  THE DIGITS AT ODD p. B = 1 + d pi^i* + C(d, 2) pi^(2 i*) + (the
    p^M-power tail at i* + (p-1)^2 c_0 p^(M-1) >= i* + 4 i*/3). So
    delta_w < i* gives tau = delta_w; delta_w > i* gives tau = i*
    (the level-2i* digit of zeta_p - B is d t_(i*) - C(d, 2) with
    t_(i*) = d/2, total d/2 != 0); delta_w = i* gives t_(i*) =
    d/2 - w_(i*), so tau > i* iff the digit w_(i*) is (p + 1)/2.
H4  THE DIGITS AT p = 2. 2 = w pi^e, so zeta_2 - 1 = -w pi^e, which is
    w pi^e to precision e* (they differ by 2 w pi^e at level 2e);
    B = (1 + pi^(c_0))^(2^M) = 1 + pi^e + C(2^M, 2^(M-1)) pi^(e/2) +
    C(2^M, 2^(M-2)) pi^(e/4) + ..., the two terms at levels e + e/2
    and e + 5e/4 and nothing else below e + 3e/2. Within the window
    the effective digit of zeta_2 - B at rel r is w_r + [r = e/2] +
    [r = 5e/4] mod 2: tau = delta_w below e/2, tau = e/2 when
    delta_w > e/2, tau > e/2 when delta_w = e/2. The readout theorem's
    skeleton is the binomial tail of the basis monomial.
H5  THE WELD, DERIVED. X := p^M, except X := e/2 at the p = 2 class
    c_0 = 1. min(w_2 - e*, X) = min(delta_w, X) at every open gate.
H6  THE TAME READOUT AS A COROLLARY. For (c, m) with p^m <= X:
    delta_w < p^m puts a frontier point of order v_p(delta_w) + 1 <= m
    at e* + delta_w, so R_c = e* + delta_w < Phi_c; delta_w >= p^m
    puts every r-coordinate past the first at weight >= e* + p^m, so
    R_c >= Phi_c. Hence min(R_c, Phi_c) = e* + min(delta_w, p^m) at
    every class of every odd p and every p = 2 class but the wild one,
    where the rung is e* + (the first r with effective digit nonzero)
    capped at the floor 7e/2.

PREDICTIONS, fixed before the engine ran.
  PR1 (pullback lemma). At every field, every level L in (i*, i* + p^M)
      pulls back to (a, b) with a > c_0 and b <= M - 1, and every level
      i* + j p^M < e* pulls back to order b >= M. KILL: one level off.
  PR2 (the module reads the tail). At every open-gate field with
      tau < e: w_2 = e* + tau and the second point is (a, b + 1) with
      (a, b) the pullback of i* + tau, whenever p^M does not divide
      tau; w_2 > e* + tau (or no second point) when it does.
      KILL: one field off.
  PR3 (the digits read the tail). Odd p: tau = delta_w when delta_w <
      i*; tau = i* when delta_w > i*; at delta_w = i*, tau > i* iff
      w_(i*) = (p + 1)/2. p = 2: tau = delta_w when delta_w < e/2;
      tau = e/2 when delta_w > e/2; tau > e/2 when delta_w = e/2.
      KILL: one field off.
  PR4 (the skeleton law at the wild class). At every p = 2 field with
      c_0 = 1, min(w_2, 7e/2) = 2e + min(r_1, 3e/2), r_1 the first
      r >= 1 with w_r + [r = e/2] + [r = 5e/4] odd. KILL: one field.
  PR5 (controls, read first). x^2 - 2: tau = 1, w_2 = 5, second point
      (3, 1). x^6 + 3x + 3: tau = 1, w_2 = 10, second point (4, 1).
      x^4 - 2: tau = 2, w_2 = 10. x^6 + 3x^3 + 3 (delta_w = i* = 3,
      w_3 = 2): tau = 4; x^6 + 6x^3 + 3 (w_3 = 1): tau = 3 with the
      level 6 dominated, w_2 = 13 at both.
  PR6 (the corollary). At every class of every field but the wild
      class, min(R_c, Phi_c) = e* + min(delta_w, p^m); at the wild
      class min(w_2, 7e/2) = e* + min(tau, 3e/2). KILL: one class.
  PR7 (x^12 - 2). delta_w is 4 or at least 7 (w_2 - e* = 6 with
      c_0 = 3, M = 2: delta_w = 5 would read 29, delta_w = 6 would
      defer past 30).

THE DESIGN. engine: explore_rung_odd.py's field, window, zeta_p,
orders and frontier; the tail tau by stripping the leading basis
monomial with the digit that raises the weight; the digits of w by
explore_tame_readout.py at odd p and explore_jump_set.py at p = 2.
fields: the controls; the tame readout's twenty fields at p = 3, 5
with x^6 + 6x^3 + 3 and x^12 - 2; the six ramified quadratics; 512
Haar-random quartics and 512 Haar-random octics (seed 1178,
explore_rung_theorem.py's sampler), where the wild-class law and the
rung's distribution by delta_w are read. verdict: PR1-PR7 as counts.
Run: python prime/code/explore_second_point.py

FINDINGS (entered post-run, copied from printed output).

1. THE MODULE READS THE TAIL (PR1, PR2 hit, 0 off at 1046 open-gate
   fields; PR1 at the 5 closed-gate fields too). At every field the
   second frontier weight is e* + tau exactly when p^M does not divide
   tau, the second point the pullback of i* + tau at one order more,
   and sits above e* + tau when p^M divides tau: x^6+3x+3 tau 1, w_2
   10, point (4, 1); x^6+3x^3+3 tau 4, w_2 13, point (7, 1);
   x^6+6x^3+3 tau 3 = p^M, w_2 13 above 12; x^6+3 and x^6-6 tau 3,
   w_2 13; x^12+3 (c_0 = 2) tau 6 = 2 p^M, w_2 26 above 24; x^18+3
   tau 9 = p^M, w_2 39 above 36; x^18+3x^5+3 tau 5, w_2 32 = 27 + 5;
   x^12-2 tau 6, w_2 30, point (9, 2); zeta_9, Q_3(zeta_3),
   Q_5(zeta_25) and x^2+2x+2 have tau at CAP and I = [1] alone.

2. THE DIGITS READ THE TAIL (PR3 hit, 0 off). Odd p: tau = delta_w
   below i* (delta_w = 1 at x^6+3x+3, x^6+6x+3, x^12+3x+3, x^18+3x+3,
   x^20+5x+5; 2 at x^6+3x^2+3; 5 at x^18+3x^5+3), tau = i* above it
   (x^6-6 delta_w 6; x^6+3, x^12+3, x^18+3 with w = 1), and at delta_w
   = i* the digit w_i* decides: x^6+3x^3+3 (w_3 = 2) tau 4,
   x^6+6x^3+3 (w_3 = 1) tau 3, zeta_9 (w_3 = 2) tau at CAP. p = 2: the
   quadratics read tau = min(delta_w, e/2) off delta_w = e/2 = 1
   (x^2+2x-2 delta_w 1 tau 2; x^2+2x+2 delta_w 1 tau CAP), and x^4-2,
   x^12-2 with w = 1 read tau = e/2 = 2 and 6.

3. THE WILD CLASS'S RUNG IS THE SKELETON LAW (PR4, PR6 hit, 0 off at
   the 1024 Haar fields, the quadratics and every class of every field
   read). At e = 4 delta_w = 1 lands 256 of 256 at rung 9, delta_w >= 3
   lands 129 of 129 at 10 = 2e + e/2, and delta_w = e/2 defers 127
   fields over rungs 11, 12, 13, 14 (56, 37, 14, 20); at e = 8 delta_w
   = 1, 2, 3 land 248, 136, 63 at 17, 18, 19, delta_w >= 5 lands 38 at
   20, and delta_w = e/2 defers 27 over 21 to 27 (13, 6, 4, 2, 1, 0,
   1). The readout theorem's skeleton positions e/2 and 5e/4 are the
   binomial tail of (1 + pi)^e.

4. x^12 - 2 has w = 1 exactly (PR7 hit: delta_w at CAP, tau = 6 = e/2).

TIER. THE SECOND POINT FROM THE DIGITS — min(w_2 - e*, X) = min(delta_w,
X) with X = p^M, and X = e/2 at the wild class, the second point the
pullback of i* + delta_w at one order more whenever delta_w < X — is a
THEOREM for every totally ramified window with integral seat at every
p, given Pagano's Theorem 1.4 (H1-H5); the tame readout law at every
class, the p = 2 intermediate staircases and the readout theorem's
top-class law with its skeleton are COROLLARIES of it and the rung
theorem (H6), each also proved directly by its own enumeration; the
instances are rules at the 1051 fields read.

RUN RECORD. python prime/code/memwatch.py prime/code/explore_second_point.py:
25.8 s wall, peak working set 17.4 MB, 11,936 checks. One pre-green
fault: the digit vector was read to max(i*, e) + 2 and the octics'
skeleton read at 3e/2 ran past it; lengthened to 3e/2 + 2 before the
octics ran, no prediction touched.
"""
import os
import random
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, ".")
sys.path.insert(0, "prime/code")
import explore_arrival_defect as ad       # noqa: E402
import explore_jump_set as js             # noqa: E402
import explore_tame_readout as tr         # noqa: E402
import explore_rung_odd as ro             # noqa: E402
import explore_rung_theorem as rt         # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ---------------------------------------------------------------- engine

def tail(F, z, c0, M):
    """(d, tau): strip the leading basis monomial (1 + pi^c0)^(d p^M)
    from zeta_p with the digit d that raises the weight past i*."""
    base = js.epow(F, ro.mono(F, 1, c0), F.p ** M)
    inv = js.unit_inv(F, base)
    u = z
    for d in range(1, F.p):
        u = F.emul(u, inv)
        v = F.val(ad.esub(F, u, F.one))
        if v > F.seat:
            return d, v - F.seat
    ok(False, "%s: no digit strips the seat" % F.name)


def w_digits(F, w, pi, n):
    if F.p == 2:
        return js.digits(F, w, n)
    return tr.w_digits(F, w, pi, n)


def read(name, p, eis, verbose=True):
    """One field: returns a row dict or None at the closed gate."""
    F = ro.field(name, p, eis)
    c0, M = ro.seat_split(F)
    istar, estar, pM = F.seat, F.p * F.seat, F.p ** M
    w, pi, delta, w0 = ro.window(F)
    z = ro.zeta_p(F)
    # PR1 at every field, gate open or closed
    for L in range(istar + 1, istar + pM):
        a, b = js.pullback(F, L)
        ok(a > c0 and b <= M - 1,
           "%s: level %d pulls back to (%d, %d)" % (name, L, a, b))
    for L in range(istar + pM, estar, pM):
        ok(js.pullback(F, L)[1] >= M,
           "%s: level %d pulls back below order M" % (name, L))
    if z is None:
        if verbose:
            print("%-14s p=%d e=%d i*=%d gate closed (w0=%d)"
                  % (name, p, F.e, istar, w0))
        return None
    d, tau = tail(F, z, c0, M)
    ords = ro.orders(F, z, pi)
    front = ro.frontier(F, ords)
    w2 = js.rho_k(F, *front[1]) if len(front) > 1 else None
    wild = (p == 2 and c0 == 1)
    X = F.e // 2 if wild else pM
    n = max(istar, 3 * F.e // 2) + 2
    dig = w_digits(F, w, pi, n)
    row = dict(name=name, p=p, e=F.e, c0=c0, M=M, istar=istar,
               estar=estar, delta=delta, tau=tau, w2=w2, front=front,
               d=d, dig=dig, wild=wild, X=X, F=F)
    if verbose:
        print("%-14s p=%d e=%d i*=%d=%d*%d^%d  delta_w=%s tau=%d  "
              "w2=%s  jump set %s"
              % (name, p, F.e, istar, c0, p, M, ro.fmt(F, delta), tau,
                 ro.fmt(F, w2), js.fmt_js(F, front)))
    # PR2
    if tau < F.e:
        if tau % pM:
            a, b = js.pullback(F, istar + tau)
            ok(w2 == estar + tau and front[1] == (a, b + 1),
               "%s: tau=%d w2=%s second point %s, expected (%d,%d) at %d"
               % (name, tau, w2, front[1:2], a, b + 1, estar + tau))
        else:
            ok(w2 is None or w2 > estar + tau,
               "%s: tau=%d divisible by p^M but w2=%s" % (name, tau, w2))
    # PR3
    if p == 2:
        h = F.e // 2
        if delta < h:
            ok(tau == delta, "%s: p=2 delta=%d tau=%d" % (name, delta, tau))
        elif delta > h:
            ok(tau == h, "%s: p=2 delta=%s tau=%d != e/2" % (name, delta, tau))
        else:
            ok(tau > h, "%s: p=2 delta=e/2 but tau=%d" % (name, tau))
    else:
        if delta < istar:
            ok(tau == delta, "%s: delta=%d tau=%d" % (name, delta, tau))
        elif delta > istar:
            ok(tau == istar, "%s: delta=%s tau=%d != i*" % (name, delta, tau))
        else:
            half = (p + 1) // 2
            ok((tau > istar) == (dig[istar] == half),
               "%s: delta=i*, w_i*=%d, tau=%d" % (name, dig[istar], tau))
    # PR4 and PR6
    for c, m in ro.classes(F):
        Ph = ro.phi(F, c, m)
        Rt = ro.r_top(F, m, front)
        lhs = min(Rt, Ph) if Rt is not None else Ph
        if wild and m == M:
            law = estar + min(tau, 3 * F.e // 2)
            ok(lhs == law, "%s: wild class min %d, tail law %d"
               % (name, lhs, law))
            r1 = next(r for r in range(1, 3 * F.e // 2 + 1)
                      if r == 3 * F.e // 2
                      or (dig[r] + (r == F.e // 2)
                          + (4 * r == 5 * F.e)) % 2)
            ok(lhs == 2 * F.e + r1, "%s: wild class min %d, skeleton %d"
               % (name, lhs, 2 * F.e + r1))
            row["rung"] = lhs
        else:
            law = estar + min(delta, p ** m)
            ok(lhs == law, "%s: class (%d,%d) min %d, readout %d"
               % (name, c, m, lhs, law))
    return row


# ---------------------------------------------------------------- run

def run():
    t0 = time.time()
    print("[controls] PR5")
    r = read("x^2-2", 2, [-2, 0, 1])
    ok(r["tau"] == 1 and r["w2"] == 5 and r["front"][1] == (3, 1),
       "x^2-2 control")
    r = read("x^6+3x+3", 3, [3, 3, 0, 0, 0, 0, 1])
    ok(r["tau"] == 1 and r["w2"] == 10 and r["front"][1] == (4, 1),
       "x^6+3x+3 control")
    r = read("x^4-2", 2, [-2, 0, 0, 0, 1])
    ok(r["tau"] == 2 and r["w2"] == 10, "x^4-2 control")
    r = read("x^6+3x^3+3", 3, [3, 0, 0, 3, 0, 0, 1])
    ok(r["tau"] == 4 and r["w2"] == 13 and r["dig"][3] == 2,
       "x^6+3x^3+3 control: tau %d w2 %s w3 %d"
       % (r["tau"], r["w2"], r["dig"][3]))
    r = read("x^6+6x^3+3", 3, [3, 0, 0, 6, 0, 0, 1])
    ok(r["tau"] == 3 and r["w2"] == 13 and r["dig"][3] == 1,
       "x^6+6x^3+3 control: tau %d w2 %s w3 %d"
       % (r["tau"], r["w2"], r["dig"][3]))
    print("  controls hit\n")

    print("[fields] the tame readout's twenty and x^12 - 2")
    n_open = n_closed = 0
    for name, p, eis in ro.tame_fields():
        r = read(name, p, eis)
        n_open += r is not None
        n_closed += r is None
    r = read("x^12-2", 2, [-2] + [0] * 11 + [1])
    n_open += 1
    ok(r["delta"] == 4 or r["delta"] >= 7,
       "x^12-2: delta_w = %s" % r["delta"])
    print("  x^12-2: delta_w = %s, tau = %d (PR7)" % (r["delta"], r["tau"]))

    print("\n[p = 2] the six ramified quadratics")
    quads = [("x^2-2", [-2, 0, 1]), ("x^2+2", [2, 0, 1]),
             ("x^2-10", [-10, 0, 1]), ("x^2+10", [10, 0, 1]),
             ("x^2+2x-2", [-2, 2, 1]), ("x^2+2x+2", [2, 2, 1])]
    for name, eis in quads:
        read(name, 2, eis)
        n_open += 1

    print("\n[p = 2] 512 Haar quartics and 512 Haar octics, seed 1178")
    rng = random.Random(1178)
    for e, prec in ((4, 5), (8, 6)):
        by = {}
        for _ in range(512):
            eis = rt.haar_octic(rng, e, prec)
            r = read("e=%d" % e, 2, eis, verbose=False)
            n_open += 1
            key = (min(r["delta"], e // 2 + 1) if r["delta"] != e // 2
                   else "e/2")
            by.setdefault(key, {})
            by[key][r["rung"]] = by[key].get(r["rung"], 0) + 1
        print("  e=%d: rung counts by delta_w (e/2 deferred, >e/2 pooled):"
              % e)
        for k in sorted(by, key=str):
            print("    delta_w=%-4s %s" % (k, dict(sorted(by[k].items()))))
    print("\nVERDICT: PR1-PR7 hit at %d open-gate and %d closed-gate "
          "fields; %d checks, %.1f s" % (n_open, n_closed, CHECKS,
                                         time.time() - t0))


if __name__ == "__main__":
    run()
