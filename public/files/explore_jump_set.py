"""explore_jump_set.py — THE JUMP SET BESIDE THE WINDOW WORD: is the
readout's word, or its rung, a function of Pagano's jump set of the
field?

THE QUESTION. The window word of an Eisenstein field K/Q_2 of degree
e (the canonical digits w_1..w_{3e/2-1} of 2/pi^e) is a complete
invariant of the defining equation's sub-leading bits, and the
class-1 rung (the deepest arrival class's landing) is a function of
it (explore_readout_triangle.py, explore_reduction_law.py,
explore_mu8_grading.py). The literature owns a different invariant
of the same object: the JUMP SET of the local field (Pagano, "Jump
sets in local fields", arXiv:1810.09975), the invariant of the
1-unit group U_1(K) as a FILTERED Z_p-module. U_1 is quasi-free: it
is the free filtered module on one generator at each level of
T* = {i < p*i* : p does not divide i} u {p*i*}, i* = e/(p-1) the
Kummer seat, modulo ONE relation, and the orbit of that relation
vector under the filtered automorphisms is classified by an
extended jump set (I, beta) (his Theorem 1.4, Theorem 3.38): I a
subset of T*, beta : I -> Z_{>=1} strictly decreasing, with
i -> rho^{beta(i)}(i) strictly increasing, rho(i) = min(p*i, i + e)
the two-gear map. The relation is the torsion: with mu_p in K the
relation vector is p times the coordinate vector of zeta_p, and its
jump set is read off that vector as the set of Pareto-minimal points
of {(a, ord_p(c_a))} under (order, weight-after-powering) — a point
(a', b') is absorbed by (a, b) whenever b <= b' and
rho^b(a) <= rho^{b'}(a') (his effective computation of filt-ord,
right after Theorem 1.4; Proposition 3.42 then reads the torsion
back: mu_{p^inf}(K) = Z/p^{beta(max I)}).

  The jump set is the invariant a stranger would name as owning the
arrival spectrum: the spectrum is a function of the unit orbits
under p-powering, and p-powering commutes with the filtered
automorphisms. Nothing here has ever printed the two side by side.
The question is: on the six ramified quadratics of Q_2 and the 48
Eisenstein quartics plus zeta_8 of the mu_8 census, what does
(I, beta) read, and how does its partition of the fields sit against
the word's and the rung's?

THE OBJECTS. K = Q_2[x]/(F), F Eisenstein of degree e in {2, 4},
pi = x, f = 1. T* at e = 2: {1, 3, 4}; at e = 4: {1, 3, 5, 7, 8}.
The basis eta_a = 1 + pi^a, a in T*; the coordinate vector of a
1-unit u is its DISCRETE LOG in that basis, computed by successive
approximation: at weight i = v(u - 1) pull i back along rho to the
unique (a, b) in T* x Z_{>=0} with rho^b(a) = i (i = p*i* is the
basis level e* itself, never (i*, 1) — the seat squares cancel at
f = 1, which is exactly why e* is a basis level), divide u by
eta_a^{p^b}, add p^b to c_a, repeat until u = 1 to the working
precision. Off the seat the square of a weight-j unit has weight
exactly rho(j) with residue 1 at f = 1, and no pull-back chain ever
asks for a power that crosses the seat (the chain through the seat
ends at e*, a basis level), so each division raises the weight by
at least one — asserted at every step. The vector of the relation is
2 * dlog(-1); its Pareto frontier is (I_K, beta_K).

THE WORD AND THE RUNG. w = 2/pi^e from the Eisenstein relation
(pi^e * w = 2 asserted exactly), its canonical F_2 digits by the
division routine of explore_mu8_grading.py generalized to any e; the
rung at e = 4 is the mu_8 ladder on w_1..w_5 (a rule over exactly
this census, explore_mu8_grading.py finding 1), at e = 2 the
exhaustive class-1 landing minimum (explore_arrival_defect.py's
census, amax = 10).

PREDICTIONS, fixed before the engine ran.
  PR1 (transplant from the contact's reading — "his jump sets being
      few"): the 49 fields at e = 4 realize at most 8 distinct
      (I, beta), against 17 realized words.
  PR2: the word is NOT a function of the jump set — at least one
      jump-set class carries two words.
  PR3 (the contact's inference, stated as the observable it
      predicts): the RUNG is a function of the jump set — every
      jump-set class carries exactly one rung. KILL: a jump-set class
      printed with two rungs.
  PR4: whether the jump set is a function of the word is not called;
      the partition is printed both ways.
  PR5 (positive controls, run before any of PR1-PR4 is read):
      (a) beta(max I) = 1 at every field without i, 2 at the fields
          with i (-1 a square by the label census, sq_approach past
          2e), 3 at zeta_8 — Proposition 3.42 against the census's
          own torsion labels;
      (b) the jump set is UNIFORMIZER-FREE: recomputed in the bases
          1 + pi'^a for pi' = pi(1 + pi) and pi(1 + pi + pi^2) it is
          unchanged at every field (Theorem 1.4: a change of filtered
          basis is a filtered automorphism);
      (c) HAND VALUE at Q_2(sqrt 2), x^2 - 2: -1 = 1 - pi^2 divides
          once by eta_1^2 at weight 2 and once by eta_3 at weight 3,
          so 2*dlog(-1) has ord 2 at a = 1 and ord 1 at a = 3, and
          the a = 4 coordinate (order >= 1, weight >= 6) is absorbed
          by (3, 1) at weight 5: I = {1, 3}, beta = (2, 1), weights
          (4, 5). The rig must print exactly this.

  PR6 (fixed after the e = 2, 4 prints were read and BEFORE the e = 8
      run; the e = 2, 4 print showed the first frontier point to be
      (1, log_2 e + 1) at weight 2e and the rung to be the second
      point's weight): at e = 8 on a seeded sample of the octic scan
      plus its six pure members and zeta_16, every field's first point
      is (1, 4) at weight 16, the class-1 rung (the mu_16 ladder on
      w_1..w_11, explore_mu16_face.py) equals the second frontier
      point's weight at every field, and zeta_16 prints I = {1},
      beta = 4. KILL: one field whose rung is not its second weight.

THE DESIGN. [A] the six quadratics, then the 48 quartics of the mu_8
sweep and Phi_8(x + 1): per field the word, the rung, and (I, beta)
with the weights rho^beta(a), the frontier read from the printed
coordinate orders. [B] the controls PR5(a)-(c). [C] the partitions:
per jump set the words and rungs it carries; per word the jump sets;
the counts that decide PR1-PR3 printed as bare numbers.
[D] e = 8: the six pure octics, 58 seeded members of the 768-octic
scan of explore_mu16_face.py and Phi_16(x + 1), the rung by that
rig's ladder; the torsion control is not run there (its census is
2^17 units a field) and the uniformizer control runs on the pures.
Precision: amax = 12e (U_1/U_{12e}); every frontier point has
beta <= 3 + |T*| - 1 and the least-order frontier point has weight
<= rho^3(e*) < 12e, so any coordinate bit beyond the precision is
absorbed — the frontier is exact.

FINDINGS (entered post-run, copied from printed output).

1. THE RUNG IS THE JUMP SET'S SECOND WEIGHT (rule in range; 120
   fields at three windows: the six ramified quadratics, the 48
   quartics and zeta_8, 65 octics and zeta_16 — PR3 and PR6 hit, and
   more than PR3 asked): at every field the first frontier point is
   (1, log_2 e + 1) at weight 2e = p*i* (the seat's image: -1 has
   weight e = rho^{log_2 e}(1)), and the class-1 rung — the deepest
   arrival class's landing — is the weight rho^{beta(a)}(a) of the
   SECOND point, the first level above the seat's image at which
   the torsion relation is essential: e = 2 weights (4, 5) / (4, 6) /
   (4) print rungs 5 / 6 / 7; e = 4 second weights 9, 10, 11, 12,
   13 print rungs 9..13; e = 8 second weights print rungs 17..24 at
   all 64 non-anchor octics. The cyclotomic anchors zeta_{2e} have
   I = {1} alone (beta = log_2 e + 1, the torsion): no second point,
   and their rung is the window's no-stop landing (7, 14, 28). The
   mechanism, SKETCHED and not derived: eta_1^{2e} is (-1)^{odd}
   squared times the relation's remaining factors squared, whose
   distinct weights make its weight the least of theirs, and on the
   census that least weight is the second point's; what a class-1
   unit's higher factor adds, and whether a term dominated by the
   first point can sit below the second weight, is not priced here.
   Read that way, the seat cancellation of the two-gear clock is the
   relation vector's Pareto frontier past its first point.

2. THE WORD REFINES THE JUMP SET, THE JUMP SET REFINES THE RUNG
   (rule in range at e = 4, the 49-field census; PR1, PR2, PR4): 17
   words, 8 distinct jump sets (PR1's bound met exactly), 6 rungs.
   The jump set is a function of the word (every one of the 17 word
   classes carries one jump set), the word is not a function of the
   jump set (3 of the 8 jump-set classes carry several words; the
   lock class I = {1, 5}, beta = (3, 1), weight 9, holds 24 fields
   and 8 words), and the rung is a function of the jump set (0
   classes with two rungs). At e = 8 the sample prints 16 jump sets
   against 9 rungs: the points past the second carry information
   the rung does not. So Pagano's invariant sits strictly between
   the readout's two objects: word -> (I, beta) -> rung, each arrow
   many-to-one on the census.

3. THE CONTROLS (PR5, all hit): beta(max I) = log_2 |mu_{2^inf}(K)|
   at all 55 fields of e = 2, 4 by the label census (Proposition
   3.42 live on the rig's own frontier); the frontier unchanged in
   the bases 1 + pi'^a for two other uniformizers at every e = 2, 4
   field and at the pure octics (Theorem 1.4's basis-freedom); the
   hand value at x^2 - 2 printed verbatim.

PRE-GREEN FAILURES: two, both the rig's. (1) The first draft's
torsion control labelled i in K by rung 13 alone; the run failed at
x^4 + 2x^3 + 2 (rung 10, beta(max I) = 2) and the label census says
-1 IS a square there (the blind bucket's single non-ram letter can be
-1 split) — the control was rewritten to the census's own test and
the docstring's PR5(a) with it. (2) That test enumerated U_1/U_{12e}
(2^47 units); it now runs on its own amax = 2e + 2 field.

RUN RECORD (python explore_jump_set.py, 3.7 s, exit 0): 21,928
checks passed. Printed: e = 2 jump sets (I, beta, wt) x2-2 / x2+2 /
x2-10 / x2+10 ([1,3],[2,1],[4,5]) rung 5, x2+2x-2 ([1,4],[2,1],[4,6])
rung 6, x2+2x+2 ([1],[2],[4]) rung 7. e = 4 partition: [1] b=[3]
wt=[8] 1 field (zeta8) rung 14; [1,3] b=[3,2] wt=[8,10] 3 fields
rung 10; [1,3,7] b=[3,2,1] wt=[8,10,11] 6 fields 2 words rung 10;
[1,3,8] b=[3,2,1] wt=[8,10,12] 3 fields rung 10; [1,5] b=[3,1]
wt=[8,9] 24 fields 8 words rung 9; [1,5] b=[3,2] wt=[8,13] 3 fields
rung 13; [1,7] b=[3,1] wt=[8,11] 6 fields 2 words rung 11; [1,8]
b=[3,1] wt=[8,12] 3 fields rung 12. Counts: 8 jump sets, 17 words,
49 fields; classes with >1 rung 0, with >1 word 3; jump sets per
word class all 1. e = 8: 65 fields, 16 jump sets, rungs {17..24,
28}; the pures [1,3,7,15] b=[4,3,2,1] wt=[16,20,22,23] rung 20;
zeta16 [1] b=[4] wt=[16] rung 28; rung = second weight True.
"""
import sys

sys.path.insert(0, ".")
import explore_local_clock as lc          # noqa: E402
import explore_arrival_defect as ad       # noqa: E402
import explore_mu16_face as m16           # noqa: E402
import random                             # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ------------------------------------------------------------ elements

def const(F, n):
    return ad.const_el(F, n)


def pi_el(F):
    el = [list(F.zero_c) for _ in range(F.e)]
    el[1][0] = 1
    return tuple(tuple(c) for c in el)


def scale(F, A, n):
    return tuple(F.cint(c, n) for c in A)


def unit_inv(F, D):
    """Inverse of a 1-unit by Newton, x <- x(2 - Dx)."""
    x = F.one
    two = const(F, 2)
    for _ in range(8):
        x = F.emul(x, ad.esub(F, two, F.emul(D, x)))
    ok(F.val(ad.esub(F, F.emul(D, x), F.one)) >= F.CAP,
       "%s: inverse failed" % F.name)
    return x


def epow(F, A, n):
    out, base = F.one, A
    while n:
        if n & 1:
            out = F.emul(out, base)
        base = F.emul(base, base)
        n >>= 1
    return out


def w_element(F):
    """w = 2/pi^e from F(pi) = 0: pi^e = -c0 (1 + sum (c_i/c0) pi^i)."""
    c0 = F.eis[0]
    mu0 = c0 // 2
    inv = pow(mu0 % F.pM, -1, F.pM)
    D = [list(F.zero_c) for _ in range(F.e)]
    D[0][0] = 1
    for i in range(1, F.e):
        D[i][0] = ((F.eis[i] // 2) * inv) % F.pM
    w = scale(F, unit_inv(F, tuple(tuple(c) for c in D)), (-inv) % F.pM)
    ok(F.val(ad.esub(F, F.emul(epow(F, pi_el(F), F.e), w), const(F, 2)))
       >= F.CAP, "%s: pi^e w != 2" % F.name)
    return w


def digits(F, w, n):
    """Canonical F_2 digits of w = 2/pi^e; division by pi is
    (A - d) pi^(e-1) w / 2, the coefficients exactly even."""
    pi = pi_el(F)
    pim = epow(F, pi, F.e - 1)
    A, out = w, []
    for _ in range(n):
        d = 1 if F.val(A) == 0 else 0
        out.append(d)
        B = [list(c) for c in A]
        B[0][0] = (B[0][0] - d) % F.pM
        C = F.emul(F.emul(tuple(tuple(c) for c in B), pim), w)
        ok(all(c[0] % 2 == 0 for c in C), "%s: odd digit division" % F.name)
        A = tuple(((c[0] // 2),) for c in C)
    ok(out[0] == 1, "%s: w_0 != 1" % F.name)
    return out


def rung4(d):
    w1, w2, w3, w4, w5 = d[1], d[2], d[3], d[4], d[5]
    if w1:
        return 9
    if w2 == 0:
        return 10
    if w3:
        return 11
    if w4:
        return 12
    if w5 == 0:
        return 13
    return 14


# ------------------------------------------------------------ the jump set

def rho(F, i):
    return min(F.p * i, i + F.e)


def rho_k(F, i, k):
    for _ in range(k):
        i = rho(F, i)
    return i


def tstar(F):
    estar = F.p * F.seat
    return [i for i in range(1, estar) if i % F.p] + [estar]


def pullback(F, i):
    """The unique (a, b), a in T*, with rho^b(a) = i."""
    estar, b = F.p * F.seat, 0
    while True:
        if i == estar or (i < estar and i % F.p):
            return i, b
        i = i // F.p if i < estar else i - F.e
        b += 1


def dlog(F, u, pi):
    """Coordinates of the 1-unit u in the basis 1 + pi^a, a in T*."""
    T = tstar(F)
    c = {a: 0 for a in T}
    inv_cache = {}
    while True:
        i = F.val(ad.esub(F, u, F.one))
        if i >= F.CAP:
            return c
        a, b = pullback(F, i)
        ok(a in T, "%s: pullback off T*" % F.name)
        key = (a, b)
        if key not in inv_cache:
            eta = ad.esub(F, F.one, scale(F, epow(F, pi, a), -1 % F.pM))
            inv_cache[key] = unit_inv(F, epow(F, eta, F.p ** b))
        u = F.emul(u, inv_cache[key])
        j = F.val(ad.esub(F, u, F.one))
        ok(j > i, "%s: division at weight %d did not raise it" % (F.name, i))
        c[a] += F.p ** b


def ordp(F, n):
    if n == 0:
        return None
    v = 0
    while n % F.p == 0:
        n //= F.p
        v += 1
    return v


def jump_set(F, pi):
    """(I, beta) of K: the Pareto frontier of p * dlog(-1)."""
    c = dlog(F, const(F, -1), pi)
    pts = [(a, ordp(F, v) + 1) for a, v in c.items() if v]
    front = []
    for (a, b) in pts:
        wt = rho_k(F, a, b)
        dominated = any((b2 <= b and rho_k(F, a2, b2) <= wt)
                        for (a2, b2) in pts if (a2, b2) != (a, b))
        if not dominated:
            front.append((a, b))
    front.sort()
    # the jump-set axioms
    for (a1, b1), (a2, b2) in zip(front, front[1:]):
        ok(b1 > b2 and rho_k(F, a1, b1) < rho_k(F, a2, b2),
           "%s: frontier is not a jump set" % F.name)
    return tuple(front), c


def fmt_js(F, js):
    return "I=%s beta=%s wt=%s" % (
        [a for a, _ in js], [b for _, b in js],
        [rho_k(F, a, b) for a, b in js])


# ------------------------------------------------------------ fields

QUADS = [("x2-2", [-2, 0, 1]), ("x2+2", [2, 0, 1]),
         ("x2-10", [-10, 0, 1]), ("x2+10", [10, 0, 1]),
         ("x2+2x-2", [-2, 2, 1]), ("x2+2x+2", [2, 2, 1])]

SWEEP = []
for d in (-2, 2, -6, 6, -10, 10):
    for c3 in (0, 1):
        for c2 in (0, 1):
            for c1 in (0, 1):
                SWEEP.append((d, 2 * c1, 2 * c2, 2 * c3))
QUARTS = [("[%d,%d,%d,%d]" % k, list(k) + [1]) for k in SWEEP]
QUARTS.append(("zeta8", [2, 4, 6, 4, 1]))

_rng = random.Random(1118)
OCTS = [(m16.poly_name(k), list(k) + [1]) for k in m16.PURE]
OCTS += [(m16.poly_name(k), list(k) + [1])
         for k in _rng.sample([k for k in m16.SCAN if k not in m16.PURE],
                              58)]
OCTS.append(("zeta16", [2, 8, 28, 56, 70, 56, 28, 8, 1]))


def field(name, eis):
    e = len(eis) - 1
    return lc.LF(name, 2, [0, 1], eis, 12 * e)


def torsion_log(F):
    """log_2 |mu_{2^inf}(K)| by the label census: -1 a square in K
    iff some unit approaches sqrt(-1) past 2e (the Hensel margin,
    explore_arrival_defect.py sq_approach); zeta8 only at its anchor
    (rung 14 is all-split and unique to it in this census)."""
    G = lc.LF(F.name, 2, [0, 1], F.eis, 2 * F.e + 2)
    t = 1 + (1 if ad.sq_approach(G, -1) > 2 * F.e else 0)
    return t + (1 if F.name == "zeta8" else 0)


def run():
    print("THE JUMP SET BESIDE THE WINDOW WORD")
    print("=" * 64)
    rows = []
    for e, fields in ((2, QUADS), (4, QUARTS)):
        print("\n[A] e = %d: word, rung, (I, beta)" % e)
        for name, eis in fields:
            F = field(name, eis)
            w = w_element(F)
            n = 3 * e // 2 - 1
            d = digits(F, w, n + 1)
            word = tuple(d[1:n + 1])
            if e == 4:
                rg = rung4(d)
            else:
                F10 = lc.LF(name, 2, [0, 1], eis, 10)
                spec, _ = ad.landing_spectra(F10, F10.units())
                rg = min(spec[1])
            pi = pi_el(F)
            js, c = jump_set(F, pi)
            rows.append((e, name, word, rg, js, F))
            print("  %-16s w=%s rung %2d  %s  ord=%s" % (
                name, "".join(map(str, word)), rg, fmt_js(F, js),
                {a: ordp(F, v) for a, v in c.items()}))

    print("\n[B] controls")
    # (c) the hand value
    F = [r for r in rows if r[1] == "x2-2"][0][5]
    js = [r for r in rows if r[1] == "x2-2"][0][4]
    ok(js == ((1, 2), (3, 1)), "hand value at x2-2: got %s" % (js,))
    print("  x2-2: (I, beta) = %s - the hand value" % fmt_js(F, js))
    # (a) torsion by Proposition 3.42
    for e, name, word, rg, js, F in rows:
        t = torsion_log(F)
        ok(js[-1][1] == t, "%s: beta(max I) = %d, torsion log %d"
           % (name, js[-1][1], t))
    print("  beta(max I) = log_2 |mu_{2^inf}(K)| at all %d fields" % len(rows))
    # (b) uniformizer freedom
    for e, name, word, rg, js, F in rows:
        pi = pi_el(F)
        for eta_pow in (1, 2):
            eta = F.one
            for k in range(1, eta_pow + 1):
                eta = tuple(F.cadd(a, b) for a, b in zip(eta, epow(F, pi, k)))
            pi2 = F.emul(pi, eta)
            js2, _ = jump_set(F, pi2)
            ok(js2 == js, "%s: jump set moved under pi -> pi eta" % name)
    print("  (I, beta) unchanged in the bases 1 + pi'^a, two pi' per field")

    print("\n[C] partitions at e = 4")
    r4 = [r for r in rows if r[0] == 4]
    by_js, by_word = {}, {}
    for e, name, word, rg, js, F in r4:
        by_js.setdefault(js, []).append((word, rg, name))
        by_word.setdefault(word, set()).add(js)
    F = r4[0][5]
    for js in sorted(by_js):
        words = sorted({w for w, _, _ in by_js[js]})
        rungs = sorted({g for _, g, _ in by_js[js]})
        print("  %-38s fields %2d words %2d %s rungs %s" % (
            fmt_js(F, js), len(by_js[js]), len(words),
            ["".join(map(str, w)) for w in words], rungs))
    multi_rung = sum(1 for v in by_js.values()
                     if len({g for _, g, _ in v}) > 1)
    multi_word = sum(1 for v in by_js.values()
                     if len({w for w, _, _ in v}) > 1)
    js_per_word = sorted(len(v) for v in by_word.values())
    print("  distinct jump sets %d, distinct words %d, fields %d"
          % (len(by_js), len(by_word), len(r4)))
    print("  jump-set classes carrying >1 rung: %d" % multi_rung)
    print("  jump-set classes carrying >1 word: %d" % multi_word)
    print("  jump sets per word class: %s" % js_per_word)
    rung_of_js = {}
    for e, name, word, rg, js, F in r4:
        rung_of_js.setdefault(js, set()).add(rg)
    print("  rung is a function of the jump set: %s"
          % all(len(v) == 1 for v in rung_of_js.values()))
    print("  jump set is a function of the word: %s"
          % all(len(v) == 1 for v in by_word.values()))
    print("\n[D] e = 8: sampled octics, the rung against the second weight")
    r8 = []
    for name, eis in OCTS:
        F = field(name, eis)
        w = w_element(F)
        d = digits(F, w, 12)
        rg = m16.rung1(d)
        js, c = jump_set(F, pi_el(F))
        r8.append((name, tuple(d[1:12]), rg, js, F))
    for name, word, rg, js, F in r8[:6] + r8[-1:]:
        print("  %-18s w=%s rung %2d  %s" % (
            name, "".join(map(str, word)), rg, fmt_js(F, js)))
    for name, word, rg, js, F in r8:
        ok(js[0] == (1, 4), "%s: first point %s" % (name, js[0]))
        second = rho_k(F, js[1][0], js[1][1]) if len(js) > 1 else None
        if name == "zeta16":
            ok(js == ((1, 4),), "zeta16: %s" % (js,))
        else:
            ok(second == rg,
               "%s: rung %d, second weight %s" % (name, rg, second))
    for name, word, rg, js, F in r8[:6]:
        pi = pi_el(F)
        eta = tuple(F.cadd(a, b) for a, b in zip(F.one, pi))
        js2, _ = jump_set(F, F.emul(pi, eta))
        ok(js2 == js, "%s: jump set moved under pi -> pi eta" % name)
    sets8 = sorted({js for _, _, _, js, _ in r8})
    print("  %d fields, %d distinct jump sets, rungs %s"
          % (len(r8), len(sets8), sorted({rg for _, _, rg, _, _ in r8})))
    print("  rung = second frontier weight at every non-anchor field: %s"
          % all(len(js) > 1 and rho_k(F, js[1][0], js[1][1]) == rg
                for name, _, rg, js, F in r8
                if name != "zeta16"))
    print("  zeta16: %s" % fmt_js(r8[-1][4], r8[-1][3]))
    print("\n%d checks passed." % CHECKS)


if __name__ == "__main__":
    run()
