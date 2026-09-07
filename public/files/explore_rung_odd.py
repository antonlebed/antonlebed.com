"""explore_rung_odd.py — THE RUNG BRACKET AT ODD p AND AT e WITH A
p-FREE PART: is every class's spectrum [min(R_c, e* + p^m), R_c], and
is the window defect the second frontier weight?

THE QUESTION. Over Q_2 at 2-power degree the landing spectrum of the
arrival class (c, m) is bracketed by Pagano's frontier: [min(w_2,
Phi_c), R_c] with both ends attained, Phi_c the class's floor (7e/2 at
c = 1, 2e + 2^m above), R_c the weight of the first frontier point of
order <= m (explore_rung_theorem.py, a theorem given Pagano's Theorems
1.4 and 1.6, read at 8192 octics). Separately, the tame readout theorem
prices every odd-p landing minimum as p i* + min(delta_w, p^m), delta_w
= v(-p/pi^e - 1) the window defect (explore_tame_readout.py). This rig
asks whether the same module derivation gives the bracket at odd p and
at a degree whose seat has a p-free part, and whether the two theorems
are one fact: the window defect the second frontier weight's excess over
p i*, truncated at p^m by the floor.

THE OBJECTS (explore_jump_set.py's conventions, parametric in p). K =
Q_p[x]/(F), F Eisenstein of degree e, f = 1, seat i* = e/(p - 1)
integral, i* = c_0 p^M with p not dividing c_0; rho(i) = min(p i, i + e),
e* = p i* = i* + e; T* = {a < e* : p not dividing a} u {e*}. Arrival
classes (c, m), c p^m = i*, c = c_0 p^(M-m); the top class is (c_0, M);
the landing of a class-(c, m) unit u is v(u^(p^(m+1)) - 1). The relation
is r = p dlog(zeta_p) when zeta_p lies in K (the open gate, w_0 = 1) and
there is none otherwise. The window object is w = -p/pi^e at odd p and
2/pi^e at p = 2, delta_w = v(w - 1).

THE HAND DERIVATION (on paper, before the engine).

H1  THE GATE. The p-th power of [d] pi^i* lands at level e* with
    coefficient d(1 - w) exactly (f = 1, Teichmueller d). Gate closed:
    the map on the graded piece is a bijection, U_1 is free on T* \
    {e*}, and every class lands rigidly at e* — the least weight of
    p^(m+1) x is rho^(m+1)(c) = e*, from a = c_0 alone. Gate open:
    e* is a basis level and U_1 is the free module modulo r.
H2  THE FIRST POINT is (c_0, M + 1) at weight e* at every open-gate
    field: zeta_p - 1 has weight i*, pullback (c_0, M), so r_(c_0)
    has order M + 1 and weight e*, and every other coordinate of
    dlog(zeta_p) has weight > i*, so its p-multiple has weight >=
    rho(i* + 1) = e* + 1. (x^12 - 2: (3, 3) at 24.)
H3  THE BRACKET. A class-(c, m) unit has ord x_(c_0) = M - m exactly
    and ord x_a >= n_a elsewhere, n_a the least n with rho^n(a) > c
    (no a != c_0 reaches c: the pullback is unique). Its landing is the
    largest weight of p^(m+1) x + t r over t. At a = c_0 both terms
    have order M + 1; t == t_0 (mod p), t_0 a unit, lifts the coordinate
    to weight >= rho^(M+2)(c_0) = e* + e, above every floor (Phi_c <=
    e* + p^M < e* + e); any other t leaves weight e*. So t is a unit in
    t_0 + p Z_p. A coordinate a != c_0 with b_a < m + 1 + n_a has order
    exactly b_a for every such t and every x of the class: FIXED at
    weight rho^(b_a)(a); R_c := the least of these. One with b_a >=
    m + 1 + n_a has order >= m + 1 + n_a, attained by an x_a of order
    n_a (or above it when the leading terms would cancel), the residual
    freedom in t perturbing at order >= b_a + 1; Phi_c := min_a
    rho^(m+1+n_a)(a). So the spectrum lies in [min(R_c, Phi_c), R_c]
    with both ends attained, the top by x_a := -t_0 r_a / p^(m+1) at every free
    coordinate; R_c is infinite exactly when no coordinate is fixed,
    which is when the class holds a primitive p^(m+1)-th root of unity.
H4  THE FLOOR IS e* + p^m AT EVERY CLASS OF EVERY ODD p, the top class
    included: c + 1 = a p^n with p not dividing a, a != c_0 (c_0 + 1 =
    c_0 p^n forces p = 2, c_0 = 1), n_a = n, and rho^(m+1)(c + 1) =
    p^m (c + 1) + e = e* + p^m; every other a has rho^(n_a)(a) >= c + 1
    and rho is monotone. The 7e/2 of the p = 2 top class is the c_0 = 1
    accident, 2 = rho(1) pulling back to the excluded a. At x^12 - 2
    the top class c_0 = 3 has c_0 + 1 = 4 = rho^2(1) with a = 1 != 3,
    so its floor is 24 + 4 = 28 and not 7e/2 = 42. The tame readout's
    p i* + p^m is this floor re-derived from the module.
H5  THE WELD. The tame readout theorem gives the class minimum as e* +
    min(delta_w, p^m); with H3 that is min(R_c - e*, p^m) = min(delta_w,
    p^m) at every class, so R_c = e* + delta_w whenever delta_w < p^m.
    For the top class the fixed set is {a > c_0 : b_a <= M} u {a < c_0
    : b_a <= M + n_a}; the first family's least weight is the second
    frontier weight w_2 (its least point is undominated, the only lower
    order being the first point's, at order M + 1 > M); the second
    family has weight >= e* and order > M, hence is dominated by the
    first point and never on the frontier. Whether it can undercut w_2
    is what R_full against R_front prints; where it cannot, w_2 = e* +
    delta_w whenever delta_w < p^M — the window defect is the second
    frontier weight's excess over e*, and the p^M truncation is the
    frontier's own invariance.
H6  THE ZETA_P CONSTRUCTOR. z = 1 + pi^i*: z^p - 1 has weight e* +
    min(delta_w, i*) > e* at the open gate; a correction 1 + s pi^j at
    j = L - e > i* moves z^p - 1 at level L by -w s = -s (the k >= 2
    binomials sit at e + k j > L, s^p at p j > L), so the digit s
    cancelling the leading coefficient raises v(z^p - 1) by at least
    one; the loop reaches CAP. At the closed gate it stops at e*.
H7  THE ENUMERATION. A class-(c, m) landing below X is decided by u
    modulo U_n once rho^(m+1)(n) > X: (p - 1) p^(n-c-1) representatives
    1 + d pi^c + sum c_i pi^i, i < n. The minimum is read at the least
    n with rho^(m+1)(n) > Phi_c; the top at the least n with
    rho^(m+1)(n) > R_c when that costs under 3000 representatives,
    else as ">= rho^(m+1)(n)" at the largest affordable n.

PREDICTIONS, fixed before the engine ran.
  PR1 (the gate). At every field the constructor reaches CAP exactly
      when w_0 = 1, and at every closed-gate field every class's exact
      spectrum is {e*}. KILL: one field off.
  PR2 (the first point). At every open-gate field the first frontier
      point is (c_0, M + 1) at weight e*, the only coordinate of weight
      e*. KILL: one field off.
  PR3 (the bracket). At every class of every open-gate field the exact
      minimum over the class's representatives is min(R_c, Phi_c),
      Phi_c by the formula equals e* + p^m by hand, the spectrum is
      rigid at R_c when R_c < Phi_c, and the exact top is R_c when
      finite and enumerable, else every representative lands at or
      above rho^(m+1)(n). KILL: one class off.
  PR4 (the weld). At every class min(R_c, Phi_c) = e* + min(delta_w,
      p^m), delta_w measured by the window element, the p = 2 top class
      at c_0 = 1 exempt (its floor is the wild 7e/2; the tame readout's
      wildness criterion). KILL: one class off.
      (The exemption and the hand floor's 7e/2 at that one class were
      written after the p = 2 control print showed the tame column at
      the quadratics' class 1 and before any odd-p field ran; the
      control's own row indexing was fixed at the same moment.)
  PR5 (the three readings of R_c). R_full (the full order vector),
      R_front (frontier points with b_a < m + 1 + n_a) and R_top (the
      first frontier point with beta <= m, a != c_0) agree at every
      class; R_full != R_front halts the read, R_top off is a finding
      about the odd-p frontier and not a kill.
  PR6 (torsion, Pagano's Proposition 3.42). R_c is infinite at class
      (c, m) exactly when beta(max I) >= m + 1, at every class; where
      infinite and enumerable some representative lands at CAP.
  PR7 (x^12 - 2). The gate is open (-1), the first point (3, 3) at 24,
      the floors 25, 26, 28 at classes (12, 0), (6, 1), (3, 2), the
      top class NOT at 42.
  PR8 (positive controls, run and read first). (a) The hand value at
      x^2 - 2 over Q_2 prints I = [1, 3], beta = [2, 1], class-1 minimum
      5, and the six ramified quadratics print class-1 minima 5, 6, 7 as
      explore_jump_haar.py reads them; at e = 4 the pure quartic x^4 - 2
      reads Phi_1 = 14, Phi_2 = 10 (explore_rung_theorem.py's floors).
      (b) The tame readout's sampled spectra at its twenty fields are
      reproduced by the exact enumeration: x^6+3x+3 class-1 {10} rigid
      and class-3 minimum 10, x^6+3x^2+3 {11}, x^6+3x^3+3 and C, D, K9
      floor 12 graded, the gate-closed sextics {9} at both classes,
      x^12+3x+3 class-2 {19} and class-6 minimum 19, x^12+3 class-2 floor
      21 graded, x^18+3 floors 28/30/36 at classes 9/3/1, x^18+3x+3 all
      28 with classes 1 and 3 rigid, x^18+3x^5+3 28/30/{32}, x^20+5x+5
      class-1 {26}, Q5(zeta25) floors 30/26, E5 {25}, Q3(sqrt3) {3},
      Q3(zeta3) starter minimum 4. (c) The frontier is unchanged under
      the uniformizer pi(1 + pi) at every open-gate field.

FINDINGS (entered post-run, copied from printed output).

1. THE BRACKET HOLDS AT EVERY CLASS OF EVERY FIELD READ (PR1-PR3, PR6,
   PR7 hit; rules at the 21 fields, the derivation the theorem). At the
   nine closed-gate classes (x^6+3x-3, B, B', Q3(sqrt3), E5) the exact
   spectrum is {e*}; at the 35 open-gate classes the exact minimum is
   min(R_c, Phi_c) with Phi_c = e* + p^m by formula and by hand, 0 off,
   rigidity 0 off, the top R_c at every finite enumerable class (2 to 486
   representatives) and at or above the enumeration's reach at every
   torsion class, 0 off; R_c infinite exactly when beta(max I) >= m + 1
   at all 44 classes. The first point is (c_0, M + 1) at e* at every
   open-gate field, and the frontier is unchanged under pi(1 + pi). At
   x^12 - 2 the jump set is I = [3, 9, 21], beta = [3, 2, 1] at weights
   24, 30, 33, the floors 25, 26, 28 and the class ends 25/unbounded,
   26/33, 28/30: the top class's floor is 28 = e* + 2^M and not 7e/2 = 42,
   as explore_mu16_face.py's TL9 read it.

2. THE WELD (PR4 hit, 0 off at 35 open classes; PR8(b) 0 off at the
   twenty tame fields): min(R_c, e* + p^m) = e* + min(delta_w, p^m) at
   every class — x^6+3x+3 (delta 1) w_2 = 10, x^6+3x^2+3 (2) 11,
   x^6+3x^3+3 (3 = p^M) 13 above the floor 12, x^6-6 (6) 13, x^18+3x^5+3
   (5) 32 = 27 + 5, x^18+3x+3 (1) 28, x^20+5x+5 (1) 26, and at w = 1
   exactly (x^6+3, x^12+3, x^18+3) the second weight 13, 26, 39 sits
   above the floor. So the tame readout's window defect is the second
   frontier weight's excess over e*, read up to the p^M truncation.

3. R_top = R_full AT EVERY CLASS (PR5, 0 off), AND THIS IS A LEMMA
   (derived after the print, before the doc entry): a coordinate at a
   level a < c with p not dividing a has p^(n_a - 1) a < c (the pullback
   of c is (c_0, M - m) alone), so p^(m + n_a) a < p^(m+1) c = e* with
   every intermediate step below i*, and rho^(b)(a) < e* for every
   b <= m + n_a; a relation coordinate has weight >= e*, so no level
   below c is ever fixed, the fixed set is {a > c : b_a <= m}, and its
   least weight is the weight of the first frontier point of order
   <= m, at every p. The intermediate classes read the frontier's tail:
   x^18+3's class (3, 1) tops at 43, the third point (25, 1); x^12-2's
   class (6, 1) at 33, its third point (21, 1).

TIER. The bracket [min(R_c, e* + p^m), R_c] on every arrival class's
landing spectrum, both ends attained, with R_c the first frontier
weight of order <= m and the floor e* + p^m at every class of every
odd p (7e/2 at the p = 2 top class with c_0 = 1 alone), is a THEOREM
for every totally ramified window with integral seat given Pagano's
Theorem 1.4 (H1-H4 and finding 3's lemma); the weld min(w_2 - e*, p^M)
= min(delta_w, p^M) at odd p is a COROLLARY of it and the tame readout
theorem; the instances are rules at the 21 fields read.

RUN RECORD. python prime/code/memwatch.py prime/code/explore_rung_odd.py:
26.8 s wall, peak working set 17.8 MB, 2474 checks. One pre-green
fault: explore_jump_set.py's dlog divides by the basis element once per
level, a 0/1 digit, and stalled at weight 7 of x^6+3x+3; the rig's own
dlog finds the digit in 1..p-1. The control's row indexing (the class-1
row is the last, not the first) and the p = 2 wild exemption were fixed
after the control print and before the fields ran.

THE DESIGN. engine: the field, the window element and delta_w, the
gate and zeta_p, the relation's order vector and frontier, n_a, Phi_c,
the three R_c, the exact class enumeration. controls: PR8. fields: the
tame readout's twenty at p = 3, 5 and x^12 - 2 at p = 2, each printed
as one block. verdict: PR1-PR7 as counts. Run: python
prime/code/memwatch.py prime/code/explore_rung_odd.py; estimate 3
minutes, under 100 MB.
"""
import os
import sys
import time
from math import comb

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, ".")
import explore_local_clock as lc          # noqa: E402
import explore_arrival_defect as ad       # noqa: E402
import explore_jump_set as js             # noqa: E402
import explore_tame_readout as tr         # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ---------------------------------------------------------------- engine

def field(name, p, eis, amax=None):
    e = len(eis) - 1
    F = lc.LF(name, p, [0, 1], eis, amax or 12 * e)
    ok(F.seat is not None, "%s: seat not integral" % name)
    return F


def seat_split(F):
    """i* = c_0 p^M."""
    c0, M = F.seat, 0
    while c0 % F.p == 0:
        c0 //= F.p
        M += 1
    return c0, M


def window(F):
    """(w, pi, delta_w): w = -p/pi^e at odd p, 2/pi^e at p = 2."""
    if F.p == 2:
        w = js.w_element(F)
        pi = js.pi_el(F)
    else:
        w, pi = tr.w_element(F)
    delta = F.val(ad.esub(F, w, F.one))
    w0 = w[0][0] % F.p
    return w, pi, delta, w0


def mono(F, d, j):
    """1 + d pi^j as an element (j < amax)."""
    el = [list(c) for c in F.one]
    i, r = divmod(j, F.e)
    el[r][0] = (el[r][0] + d * F.p ** i) % F.pM
    return tuple(tuple(c) for c in el)


def zeta_p(F):
    """zeta_p by H6, or None at the closed gate."""
    if F.p == 2:
        return js.const(F, -1)
    estar = F.p * F.seat
    z = mono(F, 1, F.seat)
    for _ in range(F.amax + 2):
        g = F.esub1(F.powp(z))
        L = F.val(g)
        if L >= F.CAP:
            return z
        if L <= estar:
            ok(L == estar, "%s: z^p - 1 below e*" % F.name)
            return None
        j = L - F.e
        for s in range(1, F.p):
            z2 = F.emul(z, mono(F, s, j))
            if F.val(F.esub1(F.powp(z2))) > L:
                z = z2
                break
        else:
            ok(False, "%s: no digit raises v(z^p - 1) at %d" % (F.name, L))
    ok(False, "%s: zeta_p loop did not reach CAP" % F.name)


def dlog(F, u, pi):
    """Coordinates of u in the basis 1 + pi^a, a in T*, at any p: at
    weight i with pullback (a, b) the digit d in 1..p-1 whose division
    by (1 + pi^a)^(d p^b) raises the weight is the one added."""
    T = js.tstar(F)
    c = {a: 0 for a in T}
    cache = {}
    while True:
        i = F.val(ad.esub(F, u, F.one))
        if i >= F.CAP:
            return c
        a, b = js.pullback(F, i)
        ok(a in T, "%s: pullback off T*" % F.name)
        if (a, b) not in cache:
            eta = js.epow(F, mono(F, 1, a), F.p ** b)
            inv = js.unit_inv(F, eta)
            pw = [F.one]
            for _ in range(F.p - 1):
                pw.append(F.emul(pw[-1], inv))
            cache[(a, b)] = pw
        for d in range(1, F.p):
            u2 = F.emul(u, cache[(a, b)][d])
            if F.val(ad.esub(F, u2, F.one)) > i:
                u = u2
                c[a] += d * F.p ** b
                break
        else:
            ok(False, "%s: no digit raises weight %d" % (F.name, i))


def orders(F, z, pi):
    """{a: b_a} of the relation p dlog(z), b_a = ord + 1."""
    c = dlog(F, z, pi)
    return {a: js.ordp(F, v) + 1 for a, v in c.items() if v}


def frontier(F, ords):
    pts = list(ords.items())
    front = []
    for (a, b) in pts:
        wt = js.rho_k(F, a, b)
        dom = any((b2 <= b and js.rho_k(F, a2, b2) <= wt)
                  for (a2, b2) in pts if (a2, b2) != (a, b))
        if not dom:
            front.append((a, b))
    front.sort()
    for (a1, b1), (a2, b2) in zip(front, front[1:]):
        ok(b1 > b2 and js.rho_k(F, a1, b1) < js.rho_k(F, a2, b2),
           "%s: frontier is not a jump set" % F.name)
    return tuple(front)


def n_of(F, a, c):
    n = 0
    while js.rho_k(F, a, n) <= c:
        n += 1
    return n


def classes(F):
    c0, M = seat_split(F)
    return [(c0 * F.p ** (M - m), m) for m in range(M + 1)]


def phi(F, c, m):
    c0, _ = seat_split(F)
    return min(js.rho_k(F, a, m + 1 + n_of(F, a, c))
               for a in js.tstar(F) if a != c0)


def r_full(F, c, m, ords):
    c0, _ = seat_split(F)
    ws = [js.rho_k(F, a, b) for a, b in ords.items()
          if a != c0 and b < m + 1 + n_of(F, a, c)]
    return min(ws) if ws else None


def r_front(F, c, m, front):
    c0, _ = seat_split(F)
    ws = [js.rho_k(F, a, b) for a, b in front
          if a != c0 and b < m + 1 + n_of(F, a, c)]
    return min(ws) if ws else None


def r_top(F, m, front):
    c0, _ = seat_split(F)
    ws = [js.rho_k(F, a, b) for a, b in front if a != c0 and b <= m]
    return min(ws) if ws else None


def reps(F, c, n):
    """Every 1 + d pi^c + sum c_i pi^i, c < i < n, d != 0."""
    import itertools
    pos = list(range(c + 1, n))
    for d in range(1, F.p):
        for cs in itertools.product(range(F.p), repeat=len(pos)):
            u = mono(F, d, c)
            for ci, i in zip(cs, pos):
                if ci:
                    u = F.emul(u, mono(F, ci, i))
            yield u


def landing(F, u, m):
    z = u
    for _ in range(m + 1):
        z = F.powp(z)
    return F.val(F.esub1(z))


def least_n(F, c, m, X):
    n = c + 1
    while js.rho_k(F, n, m + 1) <= X:
        n += 1
    return n


def spectrum(F, c, m, n):
    return sorted({landing(F, u, m) for u in reps(F, c, n)})


def fmt(F, v):
    return "inf" if v is None else ("CAP" if v >= F.CAP else str(v))


# ---------------------------------------------------------------- fields

def read_field(name, p, eis, budget=3000):
    """One block per field; returns the per-class rows."""
    F = field(name, p, eis)
    c0, M = seat_split(F)
    estar = F.p * F.seat
    w, pi, delta, w0 = window(F)
    z = zeta_p(F)
    gate = z is not None
    print("\n%s  p=%d e=%d i*=%d=%d*%d^%d e*=%d  w0=%d delta_w=%s gate=%s"
          % (name, p, F.e, F.seat, c0, p, M, estar, w0,
             fmt(F, delta), "open" if gate else "closed"))
    ok(gate == (w0 == 1), "%s: gate %s against w0 = %d" % (name, gate, w0))
    rows = []
    if not gate:
        for c, m in classes(F):
            n = least_n(F, c, m, estar)
            spec = spectrum(F, c, m, n)
            print("  class (%d,%d): spectrum %s over U_%d" % (c, m, spec, n))
            ok(spec == [estar], "%s: closed gate, class %d not {e*}"
               % (name, c))
            rows.append(dict(c=c, m=m, gate=False))
        return F, rows
    ords = orders(F, z, pi)
    front = frontier(F, ords)
    print("  jump set %s   orders %s" % (js.fmt_js(F, front),
                                        {a: ords[a] for a in sorted(ords)}))
    first = front[0]
    w_first = js.rho_k(F, first[0], first[1])
    n_estar = sum(1 for a, b in ords.items() if js.rho_k(F, a, b) == estar)
    ok(first == (c0, M + 1) and w_first == estar and n_estar == 1,
       "%s: first point %s at %d, %d coordinates at e*"
       % (name, first, w_first, n_estar))
    # uniformizer control
    pi2 = F.emul(pi, mono(F, 1, 1))
    front2 = frontier(F, orders(F, z, pi2))
    ok(front2 == front, "%s: frontier moved under pi(1+pi)" % name)
    beta_max = front[-1][1]
    for c, m in classes(F):
        Ph = phi(F, c, m)
        Rf, Rr, Rt = (r_full(F, c, m, ords), r_front(F, c, m, front),
                      r_top(F, m, front))
        ok(Rf == Rr, "%s: class %d R_full %s != R_front %s"
           % (name, c, Rf, Rr))
        pm = F.p ** m
        wild = (F.p == 2 and c0 == 1 and m == M)
        hand = 7 * F.e // 2 if wild else estar + pm
        pred_min = Ph if Rf is None else min(Rf, Ph)
        tame = None if wild else estar + min(delta, pm)
        n_min = least_n(F, c, m, Ph)
        spec = spectrum(F, c, m, n_min)
        got_min = spec[0]
        rigid = (Rf is not None and Rf < Ph)
        # the top
        top_note, top_ok = "", True
        if Rf is not None:
            n_top = least_n(F, c, m, Rf)
            cnt = (F.p - 1) * F.p ** (n_top - c - 1)
            if cnt <= budget:
                spec_t = spectrum(F, c, m, n_top)
                top_ok = spec_t[-1] == Rf and Rf < js.rho_k(F, n_top, m + 1)
                top_note = "top %d over U_%d (%d reps)" % (spec_t[-1], n_top,
                                                           cnt)
            else:
                n_big = n_min
                while (F.p - 1) * F.p ** (n_big - c) <= budget:
                    n_big += 1
                spec_t = spectrum(F, c, m, n_big)
                bound = js.rho_k(F, n_big, m + 1)
                top_ok = True
                top_note = "top >= %d unread (R_c %d past U_%d)" % (
                    min(spec_t[-1], bound), Rf, n_big)
        else:
            n_big = n_min
            while (F.p - 1) * F.p ** (n_big - c) <= budget:
                n_big += 1
            spec_t = spectrum(F, c, m, n_big)
            top_note = "top %s over U_%d (unbounded predicted)" % (
                fmt(F, spec_t[-1]), n_big)
            top_ok = spec_t[-1] >= js.rho_k(F, n_big, m + 1)
        print("  class (%d,%d): Phi=%d (hand %d) R=%s/%s/%s  min %d "
              "(pred %d, tame %s) spec %s over U_%d; %s%s"
              % (c, m, Ph, hand, fmt(F, Rf), fmt(F, Rr), fmt(F, Rt),
                 got_min, pred_min, "wild" if wild else tame,
                 [fmt(F, v) for v in spec], n_min, top_note,
                 "  RIGID" if rigid else ""))
        rows.append(dict(c=c, m=m, gate=True, phi=Ph, hand=hand,
                         R=Rf, Rt=Rt, min=got_min, pred=pred_min,
                         tame=tame, rigid=rigid, spec=spec,
                         top_ok=top_ok, beta_max=beta_max,
                         torsion=(Rf is None), cap=any(v >= F.CAP
                                                        for v in spec_t)))
    return F, rows


# --------------------------------------------------------------- controls

def controls():
    print("[controls] PR8(a): the p = 2 hand values")
    F, rows = read_field("x^2-2", 2, [-2, 0, 1])
    ok(rows[-1]["min"] == 5, "x^2-2 rung != 5")
    mins = []
    for name, eis in [("x^2+2", [2, 0, 1]), ("x^2-10", [-10, 0, 1]),
                      ("x^2+10", [10, 0, 1]), ("x^2+2x-2", [-2, 2, 1]),
                      ("x^2+2x+2", [2, 2, 1])]:
        F, rows = read_field(name, 2, eis)
        mins.append(rows[-1]["min"])
    ok(sorted(mins + [5]) == [5, 5, 5, 5, 6, 7],
       "quadratic rungs %s" % mins)
    F, rows = read_field("x^4-2", 2, [-2, 0, 0, 0, 1])
    ok([r["phi"] for r in rows] == [9, 10, 14], "x^4-2 floors %s"
       % [r["phi"] for r in rows])
    print("  controls (a) hit")


# ----------------------------------------------------------------- fields

def tame_fields():
    phi25 = [sum(comb(5 * j, k) for j in range(5)) for k in range(21)]
    return [
        ("x^6+3x-3", 3, [-3, 3, 0, 0, 0, 0, 1]),
        ("x^6+3x+3", 3, [3, 3, 0, 0, 0, 0, 1]),
        ("x^6+6x+3", 3, [3, 6, 0, 0, 0, 0, 1]),
        ("x^6+3x^2+3", 3, [3, 0, 3, 0, 0, 0, 1]),
        ("x^6+3x^3+3", 3, [3, 0, 0, 3, 0, 0, 1]),
        ("x^6+3 (C)", 3, [3, 0, 0, 0, 0, 0, 1]),
        ("x^6-6 (D)", 3, [-6, 0, 0, 0, 0, 0, 1]),
        ("zeta9 (K9)", 3, [3, 9, 18, 21, 15, 6, 1]),
        ("x^6-3 (B)", 3, [-3, 0, 0, 0, 0, 0, 1]),
        ("x^6-12 (B')", 3, [-12, 0, 0, 0, 0, 0, 1]),
        ("Q3(sqrt3)", 3, [-3, 0, 1]),
        ("Q3(zeta3)", 3, [3, 3, 1]),
        ("x^12+3x+3", 3, [3, 3] + [0] * 10 + [1]),
        ("x^12+3", 3, [3] + [0] * 11 + [1]),
        ("x^18+3", 3, [3] + [0] * 17 + [1]),
        ("x^18+3x+3", 3, [3, 3] + [0] * 16 + [1]),
        ("x^18+3x^5+3", 3, [3, 0, 0, 0, 0, 3] + [0] * 12 + [1]),
        ("x^20+5x+5", 5, [5, 5] + [0] * 18 + [1]),
        ("Q5(zeta25)", 5, phi25),
        ("x^20-5 (E5)", 5, [-5] + [0] * 19 + [1]),
    ]


# PR8(b): the tame readout's sampled reads, {name: {c: (min, rigid)}}
TAME_READS = {
    "x^6+3x-3": {1: (9, True), 3: (9, True)},
    "x^6+3x+3": {1: (10, True), 3: (10, None)},
    "x^6+6x+3": {1: (10, True)},
    "x^6+3x^2+3": {1: (11, True), 3: (10, None)},
    "x^6+3x^3+3": {1: (12, False)},
    "x^6+3 (C)": {1: (12, False)},
    "x^6-6 (D)": {1: (12, False)},
    "zeta9 (K9)": {1: (12, False)},
    "x^6-3 (B)": {1: (9, True), 3: (9, True)},
    "x^6-12 (B')": {1: (9, True), 3: (9, True)},
    "Q3(sqrt3)": {1: (3, True)},
    "Q3(zeta3)": {1: (4, None)},
    "x^12+3x+3": {2: (19, True), 6: (19, None)},
    "x^12+3": {2: (21, False), 6: (19, None)},
    "x^18+3": {9: (28, None), 3: (30, None), 1: (36, None)},
    "x^18+3x+3": {9: (28, None), 3: (28, True), 1: (28, True)},
    "x^18+3x^5+3": {9: (28, None), 3: (30, None), 1: (32, True)},
    "x^20+5x+5": {1: (26, True), 5: (26, None)},
    "Q5(zeta25)": {1: (30, None), 5: (26, None)},
    "x^20-5 (E5)": {1: (25, True), 5: (25, True)},
}


def run():
    t0 = time.time()
    controls()
    print("\n[fields] the tame readout's twenty and x^12 - 2")
    tallies = dict(fields=0, closed=0, classes=0, min_off=0, weld_off=0,
                   rigid_off=0, top_off=0, rtop_off=0, torsion_off=0,
                   tame_off=0)
    for name, p, eis in tame_fields() + [("x^12-2", 2, [-2] + [0] * 11 + [1])]:
        F, rows = read_field(name, p, eis)
        tallies["fields"] += 1
        estar = F.p * F.seat
        for r in rows:
            tallies["classes"] += 1
            if not r["gate"]:
                tallies["closed"] += 1
                exp = TAME_READS.get(name, {}).get(r["c"])
                if exp and exp[0] != estar:
                    tallies["tame_off"] += 1
                continue
            if r["min"] != r["pred"] or r["phi"] != r["hand"]:
                tallies["min_off"] += 1
            if r["tame"] is not None and r["min"] != r["tame"]:
                tallies["weld_off"] += 1
            if r["rigid"] != (len(r["spec"]) == 1):
                tallies["rigid_off"] += 1
            if not r["top_ok"]:
                tallies["top_off"] += 1
            if r["Rt"] != r["R"]:
                tallies["rtop_off"] += 1
            if r["torsion"] != (r["beta_max"] >= r["m"] + 1):
                tallies["torsion_off"] += 1
            exp = TAME_READS.get(name, {}).get(r["c"])
            if exp and (exp[0] != r["min"] or
                        (exp[1] is not None and exp[1] != r["rigid"])):
                tallies["tame_off"] += 1
        if name == "x^12-2":
            fl = [r["phi"] for r in rows]
            print("  PR7: floors %s, first point %s" % (fl, "read above"))
            ok(fl == [25, 26, 28], "x^12-2 floors %s" % fl)
    print("\n[verdict]")
    print("  fields %d (closed-gate classes %d, classes %d)"
          % (tallies["fields"], tallies["closed"], tallies["classes"]))
    print("  PR3 min off %d, floor-by-hand off (counted in min) ; "
          "rigidity off %d; top off %d" % (tallies["min_off"],
                                           tallies["rigid_off"],
                                           tallies["top_off"]))
    print("  PR4 weld off %d" % tallies["weld_off"])
    print("  PR5 R_top off %d" % tallies["rtop_off"])
    print("  PR6 torsion off %d" % tallies["torsion_off"])
    print("  PR8(b) tame reads off %d" % tallies["tame_off"])
    print("  checks %d, %.1f s" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    run()
