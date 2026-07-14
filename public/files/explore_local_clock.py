"""explore_local_clock.py — chamber twenty-two: the two-gear clock (the breathing descent).

THE QUESTION (ROAD P180; VERTIGO STOCK (a)'s descent remainder). The breathing
law sits at observation tier: the wall ticks on the 1-unit clock, tame places
breathe with period e, wild places tick irregularly (the measured P2 chain
1,2,4,4,4,4,8,8,16), equal characteristic doubles. Theorem A (the module law)
proved the two ENDS — mixed-char eventual linear pump, equal-char exact log —
but not the full chain with its wild transient. Is every local clock the orbit
of ONE two-branch map

    psi(i) = min(p*i, i + e)        (Frobenius gear / pump gear)

with cancellation possible ONLY at the Kummer seat i* = e/(p-1) — so that the
breathing law becomes a rule over ALL local fields, the chain reading
(p, e, f, torsion) and nothing else?

Objects: local field K_P, residue F_q (q = p^f), absolute ramification
e = v(p) (e = infinity iff equal char). U_i = 1 + P^i. E(a) = exp(U_1/U_a);
lambda(P^a) = lcm(q-1, E(a)). Orbit of a unit u: o_u(n) = v(u^{p^n} - 1);
order of u in U_1/U_a = p^{#{n : o_u(n) < a}}. E-chain = (E(a))_{a<=amax},
computed EXHAUSTIVELY (every representative of U_1/U_amax enumerated).

THE FROZEN SLATE (SCRATCH.md P180 passes 1-3, frozen and hand-attacked before
this file existed; the hand attack re-derived every naive chain independently,
fixed the fencepost convention m(a) = min{n : s_n >= a} against ground truth
Q_2, and downgraded two landings to pattern-freeze — N11 from 3 samples, N12
from a genericity step):

PR-A  upper gear bound o(n+1) >= psi(o(n)) at every step of every unit's
      orbit, every field in the zoo.
PR-A' exactness OFF the seat: o(n+1) = psi(o(n)) whenever o(n) != i*, for
      EVERY unit (cancellation is confined to the seat).
PR-B  naive fields (orbit misses the seat, or kernel avoidable) follow the
      plain psi-orbit chain exactly:
        N1  Q_2 unramified quadratic (e=1,f=2)      E = 2^(a-1), a<=8
        N2  Q_2(2^{1/3})   (e=3,f=1)   1,2,4,4,8,8,8,16,16,16,32,32,32
        N3  Q_2(2^{1/6})   (e=6,f=1)   1,2,4,4,8,8,8,8,16,16,16,16,16,16
        N4  Q_3(sqrt3)     (e=2,f=1)   1,3,3,9,9,27,27,81,81   (seat hit,
            kernel trivial: zeta_3 not in K — exact anyway)
        N6  Q_5(sqrt-5)    (e=2,f=1)   1,5,5,25,25,125,125
        Q_3 (e=1,f=1)                  E = 3^(a-1), a<=6
        PR-C Q_2 ramified with F_4 residue (e=2,f=2): the DODGE — seat hit,
            kernel proper in F_4: naive 1,2,4,4,8,8,16,16,32
PR-D  spliced fields (f=1, zeta_p in K, orbit lands on the seat): single
      splice to a landing l (THE SEAT DEFECT), then pump gear forever:
        N7  Q_2             l=3   E = 1,2,2,4,8,...,2^(a-2)
        N8  x^2-2x+6 (Q_2(sqrt-5) completion)  l=6
            E = 1,2,4,4,4,4,8,8,16,16,32,32   [a<=9 = the crossfield K0
            measured wild-P2 chain — the calibration instance]
        N9  Q_2(sqrt2)      l=5   E = 1,2,4,4,4,8,8,16,16,32,32,64
        N10 Q_2(sqrt-2)     l=5   same chain as N9
        N11 Q_2(i)          l=7   E = 1,2,4,4,4,4,4,8,8,16,16,32
            [pattern-freeze: 3 hand samples]
        N12 Q_3(zeta_3)     l=4   E = 1,3,3,3,9,9,27,27,81
            [derived-generic: the landing-4 step assumed one genericity]
        N13 Q_2(zeta_8) (e=4, seat 4 hit): l MEASURED here (no hand freeze;
            form frozen: single splice at the seat, then period 4)
PR-E  post-seat tick gaps are exactly e (mixed char, in range; N3 exempt —
      its one post-seat gap ends past amax, per the hand attack).
PR-F  equal char (F_2[[t]] a<=12, F_3[[t]] a<=9): E = p^ceil(log_p a),
      gaps doubling forever (seat at infinity, never hit).
PR-G  p=2, f=1 zoo: the defect exists iff e is a POWER OF 2 (the Frobenius
      segment 1,2,4,... lands on i* = e iff e = 2^j): e = 1,2,4 spliced,
      e = 3,6 naive.
PR-H  the defect chart {field: l} printed; candidate sub-law (torsion
      approximation orders l) eyeballed post-run, never asserted.

THE DESIGN. Fields as monogenic Eisenstein-over-unramified orders:
O = O_ur[x]/(f_eis), O_ur = Z[w]/(g) unramified of degree f, pi = x, e = deg
f_eis (e=1 realized as f_eis = x - p). Elements: e coefficients in
O_ur/p^M, M = amax//e + 3. Valuation exact below the cap: v(sum c_j x^j) =
min_j (e*v_p(c_j) + j) with v_p(c) = min over w-coordinates (monogenic
Eisenstein: distinct monomials have distinct valuations). U_1/U_amax
enumerated exactly once via the monomial basis {p^i x^j w^l : 1 <= ei+j <
amax}; each unit's full p-power orbit recorded to the cap. Equal char runs
the same census on F_p[t]/(t^amax). Everything asserts against the slate;
run `python prime/code/explore_local_clock.py`.

FINDINGS (entered post-run, copied from printed output; tiers per CLAUDE.md).

1. THE TWO-GEAR CLOCK LAW (rule, verified exhaustively across the zoo —
   1,132,648 checks): every unit orbit at every censused local field obeys
   o(n+1) >= psi(o(n)) with EQUALITY whenever o(n) != i*, for EVERY unit —
   cancellation is confined to the Kummer seat, at every one of the 14 mixed-
   char fields and both equal-char rings. The E-chain equals the law chain
   (max over start classes of the psi-orbit with that class's measured
   splice) at every field. All 13 frozen chains HIT, including the two
   risk-flagged landings (Q_2(i) l=7, pattern-frozen from 3 hand samples;
   Q_3(zeta_3) l=4, derived with one genericity step).

2. THE DODGE IS REAL (rule in range): residue degree f >= 2 erases the
   E-visible defect even when the orbit hits the seat — Q2-unram-F4 (seat 1
   hit): E = 2^(a-1) naive; Q2-ram-F4 x^2-2 (seat 2 hit, same Eisenstein
   poly as the spliced Q2(sqrt2)): naive 1,2,4,4,8,8,16,16,32. Same seat,
   bigger residue field, no defect: the seat needs F_p. And the odd-p
   kernel-trivial twin: Q_3(sqrt3) vs Q_3(zeta_3) — same (p,e,f) = (3,2,1),
   opposite chains (ticks [2,4,6,8] vs [2,5,7,9]): THE TWO RAMIFIED
   QUADRATICS OF Q_3 BREATHE ON OPPOSITE PARITIES, distinguished only by
   zeta_3 membership. The clock reads the field beyond (p, e, f).

3. E-VISIBILITY OF THE DEFECT = "THE SEAT IS A p-POWER" (rule in range,
   PR-G; sharpened by the run): the level-1 Frobenius segment 1, p, p^2, ...
   hits the seat iff i* = e/(p-1) is a p-power — for p = 2 that reads "e is
   a power of 2", for odd p it does NOT reduce to a condition on e alone
   (Q_3(zeta_3): e = 2 is no 3-power, yet i* = 1 = 3^0 and it splices).
   p=2 f=1 zoo: e = 1, 2, 4 spliced;
   e = 3, 6 NAIVE E-chains — yet the sextic's deeper classes DO splice
   (landings {6: 13, 3: 14}): the defect always lives at the seat classes;
   E-visibility requires the level-1 orbit to reach it.

4. THE STARTER FLOOR IS UNIVERSAL, THE ARRIVAL LANDING READS THE FIELD
   (observation, unfrozen — surfaced by the first run's operationalization
   catch: the slate's l was the LEVEL-1 landing; min-over-all-starts is
   graded). Every seat-STARTER class (units with v(u-1) = i*) lands at
   exactly p*i* + 1, at all nine fields whose seat level DIES (f = 1 and
   zeta_p in K; a dodging seat lands at psi(i*) instead — Q3(sqrt3)
   starters land at 3, the F_4 fields at psi): Q2: 3, sqrt2/sqrt-2/
   sqrt-5/i: 5, zeta_3: 4, x^3-2: 7, x^6-2: 13, zeta_8: 9. The level-1
   ARRIVAL landing sits deeper by an extra in {0, 0, 1, 2, 5}: sqrt2: 5+0,
   sqrt-2: 5+0, sqrt-5: 6 (+1), i: 7 (+2), zeta_8: 14 (+5); intermediate
   classes interpolate (zeta_8: {4: 9, 2: 10, 1: 14}). The extra is FINER
   than (e, f, different-exponent): sqrt2/sqrt-2 (d=3) get 0; sqrt3-field
   (d=2) gets 1, i-field (d=2, mu_4) gets 2 — candidate torsion tie
   (mu_4 in K raises it; zeta_8's mu_8 raises it more) EYEBALLED ONLY,
   never asserted. The arrival-defect chart is a new per-field invariant;
   its classical identity was an open remainder at this run (closed P184:
   the constellation law, explore_arrival_defect.py).

5. THE BREATHING LAW IS NOW A RULE IN RANGE (PR-E/PR-F): mixed char —
   post-splice tick gaps exactly e at every field (asserted; N3 exempt,
   its one post-seat gap ends past amax, and the zeta_8 assert is VACUOUS
   in range — its single post-splice tick sits at a = 15, so its period-4
   continuation is unverified, same range-truncation species as N3);
   equal char — pure Frobenius gear,
   E = p^ceil(log_p a), gaps doubling forever, seat at infinity. The
   transient is the Frobenius segment plus at most ONE splice. Subsumption:
   Q's tame odd columns (the Q_3 row; e=1 period-1 = "wall = state"), the
   crossfield wild-P2 chain 1,2,4,4,4,4,8,8,16 (N8 reproduces the K0
   measurement from the Eisenstein polynomial alone), P5's period-2 tame
   chain (N6), F_2[[t]]'s dyadic clock, and the module law's two ends
   (linear pump = pump gear; log clock = Frobenius gear) are ONE orbit.

RUN RECORD (python explore_local_clock.py, 6.9 s, exit 0):
1,132,648 checks passed. Chains as printed:
  Q2                1,2,2,4,8,...,2^(a-2)            landings {1:3}
  Q2(sqrt2)         1,2,4,4,4,8,8,16,16,32,32,64     landings {2:5, 1:5}
  Q2(sqrt-2)        same as sqrt2                    landings {2:5, 1:5}
  Q2(sqrt-5)        1,2,4,4,4,4,8,8,16,16,32,32      landings {2:5, 1:6}
  Q2(i)             1,2,4,4,4,4,4,8,8,16,16,32       landings {2:5, 1:7}
  Q2(zeta8)         1,2,4,4,8x10,16,16               landings {4:9, 2:10, 1:14}
  Q2(2^{1/3})       1,2,4,4,8,8,8,16,16,16,32,32,32  landings {3:7}
  Q2(2^{1/6})       1,2,4,4,8,8,8,8,16x6             landings {6:13, 3:14}
  Q2-unram-F4       2^(a-1)                          landings {1:2}
  Q2-ram-F4         1,2,4,4,8,8,16,16,32             landings {2:4, 1:4}
  Q3                3^(a-1)                          (no seat)
  Q3(sqrt3)         1,3,3,9,9,27,27,81,81            landings {1:3}
  Q3(zeta3)         1,3,3,3,9,9,27,27,81             landings {1:4}
  Q5(sqrt-5)        1,5,5,25,25,125,125              (no seat)
  F_2[[t]]          1,2,4,4,8,8,8,8,16,16,16,16      F_3[[t]] 1,3,3,9x6
First run caught the arrival grading (SCRATCH P180 pass 4) and an equal-char
truncation edge (a Frobenius step landing exactly at t^amax truncates to the
cap sentinel; assert re-scoped to p*i < amax). Two pre-green failures total;
every later rerun green.
"""

import itertools

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ---------------------------------------------------------------- local field


class LF:
    """Monogenic local field: O_ur[x]/(eis), O_ur = Z[w]/(g), pi = x."""

    def __init__(self, name, p, g, eis, amax):
        self.name, self.p, self.amax = name, p, amax
        self.g = g                      # monic, coeffs low->high, deg = f
        self.f = len(g) - 1
        self.eis = eis                  # monic Eisenstein, coeffs low->high (ints)
        self.e = len(eis) - 1
        self.M = amax // self.e + 3
        self.pM = p ** self.M
        self.CAP = amax + 1
        # Kummer seat e/(p-1), or None if not an integer
        self.seat = self.e // (p - 1) if self.e % (p - 1) == 0 else None
        self.zero_c = (0,) * self.f
        self.one = tuple((1 if j == 0 else 0,) + (0,) * (self.f - 1)
                         for j in range(self.e)) if self.e else None
        # precompute reduction of w^f, ..., w^(2f-2) mod g
        self.wred = []
        for k in range(self.f, 2 * self.f - 1):
            v = [0] * (2 * self.f - 1)
            v[k] = 1
            for kk in range(2 * self.f - 2, self.f - 1, -1):
                t = v[kk]
                if t:
                    v[kk] = 0
                    for j in range(self.f):
                        v[kk - self.f + j] = (v[kk - self.f + j]
                                              - t * self.g[j]) % self.pM
            self.wred.append(tuple(v[:self.f]))

    # -- coefficient (O_ur/p^M) arithmetic: tuples of f ints mod p^M
    def cmul(self, a, b):
        f, pM = self.f, self.pM
        if f == 1:
            return ((a[0] * b[0]) % pM,)
        conv = [0] * (2 * f - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    conv[i + j] += ai * bj
        out = list(conv[:f])
        for k in range(f, 2 * f - 1):
            t = conv[k]
            if t:
                red = self.wred[k - f]
                for j in range(f):
                    out[j] += t * red[j]
        return tuple(x % pM for x in out)

    def cint(self, a, n):               # coefficient times integer
        pM = self.pM
        return tuple((x * n) % pM for x in a)

    def cadd(self, a, b):
        pM = self.pM
        return tuple((x + y) % pM for x, y in zip(a, b))

    def vp_c(self, a):                  # p-valuation of a coefficient
        best = self.M
        for x in a:
            if x:
                v, p = 0, self.p
                while x % p == 0:
                    x //= p
                    v += 1
                if v < best:
                    best = v
        return best

    # -- element (O/p^M as x-poly of deg < e) arithmetic
    def emul(self, A, B):
        e = self.e
        conv = [self.zero_c] * (2 * e - 1)
        for i, ai in enumerate(A):
            if any(ai):
                for j, bj in enumerate(B):
                    if any(bj):
                        conv[i + j] = self.cadd(conv[i + j], self.cmul(ai, bj))
        for k in range(2 * e - 2, e - 1, -1):
            t = conv[k]
            if any(t):
                conv[k] = self.zero_c
                for j in range(e):
                    if self.eis[j]:
                        conv[k - e + j] = self.cadd(
                            conv[k - e + j], self.cint(t, -self.eis[j]))
        return tuple(conv[:e])

    def esub1(self, A):                 # A - 1
        out = list(A)
        c0 = list(out[0])
        c0[0] = (c0[0] - 1) % self.pM
        out[0] = tuple(c0)
        return tuple(out)

    def val(self, A):                   # P-adic valuation, capped at CAP
        best = self.e * self.M + self.e
        for j, cj in enumerate(A):
            if any(cj):
                v = self.e * self.vp_c(cj) + j
                if v < best:
                    best = v
        return best if best <= self.amax else self.CAP

    def powp(self, A):
        out = A
        for _ in range(self.p - 1):
            out = self.emul(out, A)
        return out

    def orbit(self, u):
        o, z = [], u
        while True:
            v = self.val(self.esub1(z))
            o.append(v)
            if v >= self.CAP or len(o) > 60:
                return o
            if v >= self.amax:
                return o
            z = self.powp(z)

    def units(self):                    # representatives of U_1/U_amax
        monos = []
        for i in range(self.M):
            for j in range(self.e):
                n = self.e * i + j
                if 1 <= n < self.amax:
                    for l in range(self.f):
                        el = [list(self.zero_c) for _ in range(self.e)]
                        el[j][l] = self.p ** i
                        monos.append(tuple(tuple(c) for c in el))
        for coeffs in itertools.product(range(self.p), repeat=len(monos)):
            u = [list(c) for c in self.one]
            for c, m in zip(coeffs, monos):
                if c:
                    for j in range(self.e):
                        for l in range(self.f):
                            u[j][l] = (u[j][l] + c * m[j][l]) % self.pM
            yield tuple(tuple(c) for c in u)


# ------------------------------------------------------------- equal char


def eq_orbit(p, amax, u):
    """Orbit of u (tuple, u[0]=1) in F_p[t]/(t^amax) under p-th powers."""
    CAP = amax + 1

    def mul(a, b):
        out = [0] * amax
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj and i + j < amax:
                        out[i + j] = (out[i + j] + ai * bj) % p
        return tuple(out)

    o, z = [], u
    while True:
        v = next((i for i in range(1, amax) if z[i]), CAP)
        o.append(v)
        if v >= amax or len(o) > 60:
            return o
        zp = z
        for _ in range(p - 1):
            zp = mul(zp, z)
        z = zp


# ------------------------------------------------------------------ the law


def psi_orbit(p, e, amax, start=1, splice=None):
    """psi-orbit from start; splice = (seat, landing) detour if given."""
    s, seq = start, [start]
    while s <= amax:
        if splice and s == splice[0]:
            s = splice[1]
        else:
            s = min(p * s, s + e)
        seq.append(s)
    return seq


def chain_from_orbits(p, orbits, amax):
    """E-chain from a census of unit orbits."""
    return [p ** max(sum(1 for v in o if v < a) for o in orbits)
            for a in range(1, amax + 1)]


def chain_from_law(p, e, amax, splice=None):
    """E-chain the two-gear law predicts: max over start levels."""
    best = [0] * amax
    for start in range(1, amax + 1):
        sp = splice if (splice and start <= splice[0]) else None
        seq = psi_orbit(p, e, amax, start, sp)
        for a in range(1, amax + 1):
            m = sum(1 for v in seq if v < a)
            if m > best[a - 1]:
                best[a - 1] = m
    return [p ** m for m in best]


def ticks(chain):
    return [a for a in range(2, len(chain) + 1)
            if chain[a - 1] != chain[a - 2]]


# ---------------------------------------------------------------------- zoo

ZOO = [
    # name                          p  g(w)        eis(x)                 amax
    ("Q2",                          2, [0, 1],     [-2, 1],               12),
    ("Q2(sqrt2)",                   2, [0, 1],     [-2, 0, 1],            12),
    ("Q2(sqrt-2)",                  2, [0, 1],     [2, 0, 1],             12),
    ("Q2(sqrt-5)  x^2-2x+6",        2, [0, 1],     [6, -2, 1],            12),
    ("Q2(i)  x^2-2x+2",             2, [0, 1],     [2, -2, 1],            12),
    ("Q2(zeta8)",                   2, [0, 1],     [2, 4, 6, 4, 1],       16),
    ("Q2(2^{1/3})",                 2, [0, 1],     [-2, 0, 0, 1],         13),
    ("Q2(2^{1/6})",                 2, [0, 1],     [-2, 0, 0, 0, 0, 0, 1], 14),
    ("Q2-unram-F4",                 2, [1, 1, 1],  [-2, 1],               8),
    ("Q2-ram-F4  x^2-2",            2, [1, 1, 1],  [-2, 0, 1],            9),
    ("Q3",                          3, [0, 1],     [-3, 1],               6),
    ("Q3(sqrt3)",                   3, [0, 1],     [-3, 0, 1],            9),
    ("Q3(zeta3)",                   3, [0, 1],     [3, 3, 1],             9),
    ("Q5(sqrt-5)",                  5, [0, 1],     [5, 0, 1],             7),
]

FROZEN = {
    # PR-B naive
    "Q2-unram-F4":           [1, 2, 4, 8, 16, 32, 64, 128],
    "Q2(2^{1/3})":           [1, 2, 4, 4, 8, 8, 8, 16, 16, 16, 32, 32, 32],
    "Q2(2^{1/6})":           [1, 2, 4, 4, 8, 8, 8, 8, 16, 16, 16, 16, 16, 16],
    "Q3(sqrt3)":             [1, 3, 3, 9, 9, 27, 27, 81, 81],
    "Q5(sqrt-5)":            [1, 5, 5, 25, 25, 125, 125],
    "Q3":                    [1, 3, 9, 27, 81, 243],
    "Q2-ram-F4  x^2-2":      [1, 2, 4, 4, 8, 8, 16, 16, 32],
    # PR-D spliced
    "Q2":                    [1, 2, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
    "Q2(sqrt-5)  x^2-2x+6":  [1, 2, 4, 4, 4, 4, 8, 8, 16, 16, 32, 32],
    "Q2(sqrt2)":             [1, 2, 4, 4, 4, 8, 8, 16, 16, 32, 32, 64],
    "Q2(sqrt-2)":            [1, 2, 4, 4, 4, 8, 8, 16, 16, 32, 32, 64],
    "Q2(i)  x^2-2x+2":       [1, 2, 4, 4, 4, 4, 4, 8, 8, 16, 16, 32],
    "Q3(zeta3)":             [1, 3, 3, 3, 9, 9, 27, 27, 81],
}

FROZEN_LANDING = {"Q2": 3, "Q2(sqrt2)": 5, "Q2(sqrt-2)": 5,
                  "Q2(sqrt-5)  x^2-2x+6": 6, "Q2(i)  x^2-2x+2": 7,
                  "Q3(zeta3)": 4}

SPLICED = set(FROZEN_LANDING) | {"Q2(zeta8)"}

# hand-attack exemptions: N3's one post-seat gap ends past amax
PR_E_EXEMPT = {"Q2(2^{1/6})"}


def run():
    print("THE TWO-GEAR CLOCK — exhaustive unit-orbit census")
    print("=" * 64)
    defect_chart = {}
    for name, p, g, eis, amax in ZOO:
        K = LF(name, p, g, eis, amax)
        orbits = [K.orbit(u) for u in K.units()]
        chain = chain_from_orbits(p, orbits, amax)
        tk = ticks(chain)
        # PR-A / PR-A': gear bound + exactness off the seat, every unit
        for o in orbits:
            for n in range(len(o) - 1):
                i, nxt = o[n], o[n + 1]
                if i >= K.CAP or i >= amax:
                    break
                ps = min(p * i, i + K.e)
                if ps <= amax:
                    ok(nxt >= ps, "%s: gear bound broken at %s" % (name, o))
                    if K.seat is None or i != K.seat:
                        ok(nxt == ps,
                           "%s: cancellation OFF the seat at %s" % (name, o))
        # landings BY START LEVEL: the defect is arrival-graded — the chart
        # maps start level sigma -> shallowest post-seat value among orbits
        # starting at sigma that pass through the seat. The E-chain is
        # governed by the level-1 class (the frozen l values are landing_1).
        landings = {}
        if K.seat is not None:
            for o in orbits:
                for n in range(len(o) - 1):
                    if o[n] == K.seat:
                        s = o[0]
                        if s not in landings or o[n + 1] < landings[s]:
                            landings[s] = o[n + 1]
        landing = landings.get(1)
        spliced = name in SPLICED

        def law_chain():
            best = [0] * amax
            for start in range(1, amax + 1):
                sp = ((K.seat, landings[start])
                      if K.seat is not None and start in landings else None)
                seq = psi_orbit(p, K.e, amax, start, sp)
                for a in range(1, amax + 1):
                    m = sum(1 for v in seq if v < a)
                    if m > best[a - 1]:
                        best[a - 1] = m
            return [p ** m for m in best]

        law = law_chain()
        naive = chain_from_law(p, K.e, amax)
        print("\n%-24s p=%d e=%d f=%d seat=%s" % (name, p, K.e, K.f, K.seat))
        print("  E-chain  %s" % chain)
        print("  ticks    %s   landings by start=%s" % (tk, landings))
        if name in FROZEN:
            ok(chain == FROZEN[name], "%s: frozen chain missed: %s" % (name, chain))
            print("  frozen chain: HIT")
        if name in FROZEN_LANDING:
            ok(landing == FROZEN_LANDING[name],
               "%s: frozen landing %s, measured %s"
               % (name, FROZEN_LANDING[name], landing))
        # form: measured chain = the law's chain (with measured landing)
        ok(chain == law, "%s: two-gear law chain missed: law %s" % (name, law))
        # PR-G bookkeeping
        if p == 2 and K.f == 1:
            defect_chart[name] = (K.e, landing, chain != naive)
        elif spliced:
            defect_chart[name] = (K.e, landing, chain != naive)
        # PR-E: post-seat tick gaps exactly e
        if K.seat is not None and name not in PR_E_EXEMPT:
            post = [t for t in tk if t > (landing or K.seat)]
            gaps = [b - a for a, b in zip(post, post[1:])]
            ok(all(gp == K.e for gp in gaps),
               "%s: post-seat gaps %s != e" % (name, gaps))
        elif K.seat is None:
            # seat never integer: every gap past the Frobenius segment is e
            post = [t for t in tk if t > K.e / (p - 1)]
            gaps = [b - a for a, b in zip(post, post[1:])]
            ok(all(gp == K.e for gp in gaps),
               "%s: gaps %s != e" % (name, gaps))

    # PR-G: p=2, f=1 defect iff e is a power of 2 (chart also carries the
    # odd-p spliced instance Q3(zeta3); the iff assert is p=2-scoped)
    print("\nPR-G  defect chart (p=2 f=1 zoo + spliced instances):")
    for name, (e, landing, has_defect) in sorted(defect_chart.items(),
                                                 key=lambda kv: kv[1][0]):
        pow2 = e & (e - 1) == 0
        print("  e=%-2d %-24s landing=%-4s defect=%s" %
              (e, name, landing, has_defect))
        if name.startswith("Q2") and "F4" not in name and "zeta3" not in name:
            ok(has_defect == pow2,
               "%s: defect %s but e=%d pow2=%s" % (name, has_defect, e, pow2))

    # PR-F equal char
    print("\nEqual characteristic:")
    for p, amax in ((2, 12), (3, 9)):
        orbits = []
        for coeffs in itertools.product(range(p), repeat=amax - 1):
            u = (1,) + coeffs
            orbits.append(eq_orbit(p, amax, u))
        chain = chain_from_orbits(p, orbits, amax)
        want = []                       # p^ceil(log_p a)
        for a in range(1, amax + 1):
            m = 0
            while p ** m < a:
                m += 1
            want.append(p ** m)
        ok(chain == want, "F_%d[[t]]: chain %s != %s" % (p, chain, want))
        for o in orbits:
            for n in range(len(o) - 1):
                if o[n] >= amax:
                    break
                if p * o[n] < amax:     # t^(p*i) with p*i >= amax truncates
                    ok(o[n + 1] == p * o[n],
                       "F_%d[[t]]: non-Frobenius step %s" % (p, o))
        print("  F_%d[[t]]  E-chain %s  (pure Frobenius gear: HIT)" % (p, chain))

    print("\n%d checks passed." % CHECKS)


if __name__ == "__main__":
    run()
