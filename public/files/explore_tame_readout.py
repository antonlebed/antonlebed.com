"""explore_tame_readout.py — THE TAME READOUT: the odd-p face of the
readout theorem.

THE QUESTION. The readout theorem (proved at p = 2 in an earlier
script) prices every binomial monomial's entry level by its exact
multinomial 2-content. The sigma-machinery is p-generic — multinomial
p-content, tau alphabet. Does a tame-thinned ladder drop out of the
SAME enumeration at odd p, matching the tame face's censused floors
(explore_tame_face.py: 12/10 at the p = 3 sextics, 30/26 at Q5(zeta25),
the {13} mid-field ceiling, K9's {12,16,17,18} fork)?

THE HAND DERIVATION (worked out by hand, before this file existed).

Setup: K/Q_p tot ram degree e, f = 1, odd p, seat i* = e/(p-1).
Arrival classes: start levels c with c*p^m = i* (m = 0: starters).
Below the seat the Frobenius gear is exact, so landing
L = v(u^{p^{m+1}} - 1). THE DIGIT OBJECT: w = -p/pi^e (a unit;
-p, not p: -p = lambda^{p-1} * principal-unit by Wilson, tame face
L2, so w_0 = 1 iff zeta_p in K). Canonical Teichmueller digits
(f = 1: digit^p = digit; odd-p negation is DIGIT-WISE). Carry rule
exact: p*pi^r = -w*pi^{r+e}.

TR1 (level formula): u = 1 + sum tau_i, tau_i = [rho_i]pi^{c+i};
    monomial a of (1+t)^{p^{m+1}} enters at Lambda(a) =
    i*(sigma(a) - 1) + cA + W, sigma = s_p(p^{m+1} - A) +
    sum s_p(a_i); v_p(multinomial) = (sigma - 1)/(p - 1) (Legendre =
    Kummer carries). Carry bound: lowest nonzero digit at position l
    among summands forces v_p >= m + 1 - l.
TR2 (THE GATE): rel := Lambda - p*i* = 0 holds for EXACTLY two
    monomials — tau_0^{p^{m+1}} (coeff 1) and tau_0^{p^m} (coeff
    p*gamma, gamma = C(p^{m+1}, p^m)/p == 1 mod p). Both exact, so
    the gate branch is [rho_0](1 - gamma*w)pi^{p*i*} EXACTLY: stop
    digit rho_0(1 - w_0) — the splice gate IS the leading digit.
TR3 (THE LADDER): in-window (0 < rel < p^m) NOTHING else enters
    (k >= 2 squaring constants: rel >= i*(p - 2 + 1/p) > p^m for
    every odd p — THE WILDNESS CRITERION c(p-1)^2 < p separates
    p = 2; low-content parts excluded by the carry bound; the d*p^m
    family has rel = (sum(c+i_k)d_k - c)p^m). So D_rel-j =
    -rho_0 * w_j for 1 <= j <= p^m - 1: pure w-readout, spectra
    rigid below freedom. No in-window constants, no blind rungs at
    odd p.
TR4 (FREEDOM): rel = p^m carriers: tau_1^{p^m} (digit -gamma w_0
    rho_1, sweeps F_p) plus, at c = 1 only, the pair a_0 = 2p^m
    (fixed offset). Floor attained and graded at the truncation.
TR5 (THE TAME READOUT LAW): L = p*i* + min(delta, p^m), delta =
    v(w - 1) = v(pi^e + p) - e = THE WINDOW DEFECT (delta = 0 iff
    the gate is closed: the out-fields' rigid p*i* is the law's
    zeroth rung). delta alone is pi-COVARIANT; the truncation
    min(delta, p^m) is pi-invariant (pi -> eta*pi perturbs w - 1 at
    depth v(eta^{-e} - 1) >= min(me + 1, i*) >= p^m: the window is
    exactly the invariant content of w - 1). Starters: min(delta, 1)
    — the universal starter floor p*i* + 1 derived (gate-open).
TR6 (THE COINCIDENCE — the p-fold pair-cancellation): rho_i's two
    routes tau_i^{p^m} (one carry, -gamma_1 w) and, at m = 1, tau_i
    (two carries, +w^2) share a level iff i = c(p-1) — rel e, digit
    coefficient w(w - gamma_1): cancels iff w == 1, deferring that
    freedom by delta (K9's {16,17,18} fork lives here — charted in
    explore_deep_spectrum.py: 16/17 are free-sailing singles
    at rel_c + i, i > c(p-1); only 18 is the deferral firing at
    rel e + delta). At p = 2,
    i-dagger = c(p-1) = c IS the top-class rho_1 pair whose F_2
    total cancellation defers freedom to 3e/2: the top bonus, the
    always-open gate, and the skeleton constants are all the same
    F_2 pigeonhole. Above freedom; not part of the floor law.
TR7 (corollaries): out-fields land p*i* RIGID at every class; the
    mid-field ceiling 13 = 2e + c is the p^2 tau_0 term (digit
    rho_0 w_0^2, forced when w == 1 deeply); K9's hole at 13 is
    D = rho_0(1 - w_4) with the hand expansion giving w_3 = 2,
    w_4 = 1; the p = 2 first-digit lock is delta = 1 of TR5, and
    the p = 2 INTERMEDIATE rung functions are literally
    p*i* + min(first-nonzero-digit, 2^mu).

THE PREDICTIONS (worked out by hand before this
file existed; every row load-bearing — a miss falsifies its lemma):

SL-A (p-content): the sigma/Legendre formula == integer-factored
     multinomial v_p, exhaustive small scopes, p = 3, 5, 7.
SL-B (enumeration brute) per (p, c, m) in {(3,1,1),(3,2,1),(3,3,1),
     (3,1,2),(5,1,1),(5,2,1),(7,1,1)}: in-window list == the TR2
     gate pair exactly; freedom carriers == tau_1^{p^m} (+ a_0 =
     2p^m iff c = 1); the 5-part exclusion bound; the TR6
     coincidence pair at rel e with gamma == 1 mod p and
     C(p^2, 1) = p^2 exact.
SL-C (gate, new field): x^6+3x-3 (w_0 = 2): class-1 AND class-3
     spectra {9} rigid — same tail as x^6+3x+3, flipped gate.
SL-D (the ladder, new fields, p = 3, e = 6): x^6+3x+3 (delta = 1,
     w_1 = 2): class-1 {10} RIGID, starters min 10, zeta_3 in K
     (constructed, Phi_3 = 0 at CAP); x^6+6x+3 (delta = 1, w_1 = 1):
     class-1 {10} rigid; x^6+3x^2+3 (delta = 2): class-1 {11} rigid,
     starters min 10; x^6+3x^3+3 (delta = 3 = p^m): class-1 floor 12
     graded.
SL-E (regressions re-read): C/D/K9 floors 12 with measured deltas
     (w = 1 exactly / 6 / 3), K9 digits w_3 = 2, w_4 = 1; B/B' {9}
     rigid; zeta3-quad starter 4; sqrt3-quad {3}; Z25 floor 30 with
     delta >= 5, starters 26; E5 (x^20-5) gate closed {25}.
SL-F (e = 12, i* = 6 — first censused odd-p c > 1 arrival):
     x^12+3x+3 (delta = 1): class-2 {19} rigid, class-6 min 19;
     x^12+3 (w = 1): class-2 floor 21 = 18 + p^m graded, class-6
     min 19.
SL-G (e = 18, i* = 9 — first m = 2): x^18+3 (w = 1): floors
     28 / 30 / 36 at classes (9,0)/(3,1)/(1,2) — 36 = 27 + p^2
     BEATS the tame face's censused-scope law p(i*+1) = 30;
     x^18+3x+3 (delta = 1): all three classes min 28, classes 1
     and 3 rigid {28}; x^18+3x^5+3 (delta = 5): 28 / 30 / {32}
     (class 1 rigid at 32 = 27 + 5).
SL-H (p = 5): x^20+5x+5 (delta = 1, w_1 = 4): class-1 {26} rigid,
     class-5 min 26.
SL-I (p = 2 containment): the intermediate p = 2 rung functions
     (m16.rung2/rung4, m32.rung2_16/rung4_16/rung8_16) ==
     p*i* + min(first-nonzero, 2^mu) over all digit vectors, brute.
SL-J (digits): measured canonical digit vectors match design at
     every new field (w = 1/(1+b*pi^k): digits vanish BELOW the
     defect, w_k = [-b], alternating-sign tail above — 1/(1+pi)
     prints [2,1,2,1,...]).

THE DESIGN. [A] exact factorial integers vs the sigma formula over
part multisets. [B] pruned recursive enumeration of monomials (one
(value, index) per distinct index), exact Legendre v_p via sigma;
the 5-part exclusion bound asserted per scope row (5 distinct
indices force sigma >= smin and W >= 10). [C] LF censuses
(machinery of explore_local_clock; sampled census + gear checks of
explore_tame_face) at the new and regression fields, each paired
with a digit twin (amax = 9e) where w = unit_inv(eis-tail/p),
verified pi^e * w = -p exactly; delta = v(w - 1); canonical
Teichmueller digits reconstruction-checked; THE LAW ROW asserts
min(spec[c]) = p*i* + min(delta, p^m) and rigidity below freedom at
every censused class of every field. zeta_3 constructed at the SL-D
field via Newton sqrt (sqrt(-3) = pi^3/sqrt(1+pi)). [D] SL-I brute
over F_2 vectors. Labels never read orbits; the engine only ever
reads MEASURED digits.
Run: python prime/code/explore_tame_readout.py

FINDINGS (entered post-run, copied from printed output).

1. THE TAME READOUT LAW (theorem — the enumeration proof is general
   in (p, c, m, e); field verification rule-in-range at p = 3, 5):
   for every odd p, every totally ramified f = 1 window K/Q_p with
   integral seat i* = e/(p-1), and every seat class c*p^m = i*, the
   landing is L = p*i* + min(delta, p^m) with delta = v(w - 1) =
   v(pi^e + p) - e THE WINDOW DEFECT of w = -p/pi^e: the gate digit
   w_0 != 1 stops at delta = 0 (out-fields rigid p*i* — the tame
   thinness IS the zeroth digit), the ladder digits D_rel-j =
   -rho_0 w_j (1 <= j < p^m) stop rigidly, freedom arrives at rel
   p^m (tau_1^{p^m}, plus the a_0 = 2p^m pair at c = 1). delta is
   pi-covariant; its p^m-truncation is the pi-invariant content of
   w - 1. In-window the enumeration is EXACTLY the two gate
   monomials (brute at seven (p, c, m) scopes incl. p | c and
   m = 2): odd p has NO in-window constants and NO blind rungs —
   THE WILDNESS CRITERION c(p-1)^2 < p (the first deeper-squaring
   constant undercuts freedom iff it holds) fails at every odd p
   AND every p = 2 intermediate class, holding exactly at the
   p = 2 top class — where the always-open gate (F_2 pigeonhole),
   the top-class 3e/2 bonus (the rho_1 pair's total cancellation =
   the i-dagger = c(p-1) coincidence collapsing), and the skeleton
   constants all live.

2. THE LADDER STRIKES SIGHT-UNSEEN (rule in range; the falsification
   core): x^6+3x+3 and x^6+6x+3 (delta = 1) land class 1 at {10}
   RIGID, x^6+3x^2+3 (delta = 2) at {11} RIGID — BELOW the tame
   face's censused floor 12 = p(i*+1), refining its m = 1 law to
   its delta >= p^m branch (its fields C/D/K9 measure delta =
   CAP/6/3); x^6+3x^3+3 (delta = 3 = p^m) rejoins floor 12 graded
   {12, 13}. The flipped-gate twin x^6+3x-3 (w_0 = 2) lands {9}
   rigid at both classes. The p = 2 first-digit lock (9 =
   p*i* + 1) is delta = 1 of the same formula, and the p = 2
   INTERMEDIATE rung functions are p*i* + min(first-nonzero, 2^mu)
   verbatim (all 4096 digit vectors, five rung functions).

3. THE m = 2 AND c > 1 FACES (rule in range; never censused before):
   x^18+3 (w = 1 exactly) lands classes (9,0)/(3,1)/(1,2) at floors
   28 / 30 / 36 = 27 + p^m — the m = 2 floor BEATS the old
   censused-scope law p(i*+1) = 30; x^18+3x+3 (delta = 1) pins all
   three classes to min 28 with classes 1 and 3 rigid {28};
   x^18+3x^5+3 (delta = 5) grades them 28 / 30 / {32} — the
   truncation ladder visible at one field. x^12+3x+3 (delta = 1)
   lands the first censused odd-p c > 1 arrival rigid {19};
   x^12+3 (w = 1) at floor 21 = 18 + p^m (spectrum {21, 24, 26}).
   p = 5: x^20+5x+5 (delta = 1, w_1 = 4) lands {26} rigid; Q5(zeta25)
   measures delta = 5 exactly (= p^m: floor 30, starters 26).

4. THE K9 MECHANISM (observation with the hand expansion, measured):
   zeta9's window defect is 3 with digits w_3 = 2, w_4 = 1 — exactly
   the hand lambda-expansion (w - 1 = -lambda + 2u + ..., u =
   -w pi^4(1+pi)) — so its truncation-level landing is 12 and the
   post-freedom hole at 13 is D = rho_0(1 - w_4) = 0, where the
   mid-fields (w_4 = 0: C, D measure all-zero windows) are FORCED to
   stop by the p^2 tau_0 term (the {13} ceiling = 2e + c, TR7): the
   fork/ceiling contrast of the tame face is two values of one
   digit.

5. ONE LAW, EVERY CENSUSED ROW (synthesis; the tame face + arrival-
   defect + mu-face corpora re-read): out-fields' rigid {9}/{25},
   the universal starter floor p*i* + 1 (delta >= 1 = p^0 whenever
   the gate is open), the m = 1 floors 12/30, the zeta3-quad starter
   4, and the p = 2 lock/intermediate staircases are all
   L = p*i* + min(delta, p^m). The readout theorem's odd-p face is
   THINNED to exactly this: window = gate digit + p^m - 1 ladder
   digits per class — the long p = 2 windows (2^m - 1 with the top
   3e/2 - 1 bonus and its skeleton constants) are a wildness
   privilege with an exact criterion.

PRE-GREEN FAILURES: one, engine-side — the enumeration recorder
appended the current monomial at every skip-recursion node
(duplicates), caught by the first [B] gate assert before any field
arithmetic ran; the hand lists stood unchanged.

RUN RECORD (python explore_tame_readout.py, 12.4 s, exit 0): 27,707
checks this module + 40,680 through the imported gear/torsion
machinery (explore_tame_face counter) = 68,387 (a later re-run added
20 heavy-class presence asserts, one per censused field,
closing law_row's vacuous-pass hole; spectra and deltas unchanged). Landings as printed
(spectra truncated at six values):
  x^6+3x-3    1->{9}  3->{9}         x^6+3x+3    1->{10} 3->{10,...}
  x^6+6x+3    1->{10}                x^6+3x^2+3  1->{11} 3->{10,...}
  x^6+3x^3+3  1->{12,13}             C 1->{12,13}   D 1->{12,13}
  K9          1->{12,16,17,18,CAP}   B/B' 1->{9} 3->{9}
  x^12+3x+3   2->{19} 6->{19,...}    x^12+3      2->{21,24,26}
  x^18+3      1->{36,39} 3->{30,33,...} 9->{28,...}
  x^18+3x+3   1->{28} 3->{28}        x^18+3x^5+3 1->{32} 3->{30,32}
  x^20+5x+5   1->{26} 5->{26,...}    Z25 1->{30,CAP}   E5 1->{25} 5->{25}
Deltas as printed: 0 at the four gate-closed fields; 1/1/2/3 at the
designed SL-D fields; CAP/6/3 at C/D/K9 (K9 digits [0,0,2,1,1]);
1/CAP at e = 12; CAP/1/5 at e = 18; 1/5/0 at p = 5.
"""

import itertools
import random
from math import comb, factorial

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_tame_face as tf
import explore_mu16_face as m16
import explore_mu32_face as m32

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ------------------------------------------------- p-adic integer helpers


def sp(n, p):
    s = 0
    while n:
        s += n % p
        n //= p
    return s


def vp_int(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def vp_multinomial(n, parts, p):
    """v_p(n! / (prod a! * (n - A)!)) by exact integer factorials."""
    A = sum(parts)
    num, den = factorial(n), factorial(n - A)
    for a in parts:
        den *= factorial(a)
    assert num % den == 0
    return vp_int(num // den, p)


def sigma_vp(n, parts, p):
    """(sigma - 1)/(p - 1), sigma = s_p(n - A) + sum s_p(a_i) (TR1)."""
    A = sum(parts)
    s = sp(n - A, p) + sum(sp(a, p) for a in parts)
    assert (s - 1) % (p - 1) == 0
    return (s - 1) // (p - 1)


# ------------------------------------------------------- field helpers


def unit_inv(F, T):
    """Newton inverse of a unit element (any p)."""
    x = ad.const_el(F, pow(T[0][0] % F.p, -1, F.pM))
    two = ad.const_el(F, 2)
    for _ in range(14):
        x = F.emul(x, ad.esub(F, two, F.emul(T, x)))
    ok(F.val(ad.esub(F, F.emul(T, x), ad.const_el(F, 1))) >= F.amax,
       "%s: unit_inv failed" % F.name)
    return x


def pi_el(F):
    pi = [list(F.zero_c) for _ in range(F.e)]
    pi[1][0] = 1
    return tuple(tuple(c) for c in pi)


def w_element(F):
    """w = -p/pi^e via pi^e = -p*T, T = eis-tail/p; verified exactly."""
    p = F.p
    T = [list(F.zero_c) for _ in range(F.e)]
    for j in range(F.e):
        assert F.eis[j] % p == 0
        T[j][0] = (F.eis[j] // p) % F.pM
    w = unit_inv(F, tuple(tuple(c) for c in T))
    pe, pi = F.one, pi_el(F)
    for _ in range(F.e):
        pe = F.emul(pe, pi)
    ok(F.val(ad.esub(F, F.emul(pe, w), ad.const_el(F, -p))) >= F.amax,
       "%s: pi^e * w != -p" % F.name)
    return w, pi


def teich(F, d):
    """Teichmueller lift of the residue d, as an int mod p^M."""
    x = d % F.p
    for _ in range(F.M + 2):
        x = pow(x, F.p, F.pM)
    return x


def w_digits(F, w, pi, n):
    """Canonical Teichmueller digits of the unit w, reconstruction-
    checked to level n. Division by pi via *pi^(e-1)*w*(-1/p)."""
    pik = F.one
    for _ in range(F.e - 1):
        pik = F.emul(pik, pi)
    A, out = w, []
    for _ in range(n):
        d = A[0][0] % F.p
        out.append(d)
        B = [list(c) for c in A]
        B[0][0] = (B[0][0] - teich(F, d)) % F.pM
        C = F.emul(F.emul(tuple(tuple(c) for c in B), pik), w)
        ok(all(c[0] % F.p == 0 for c in C),
           "%s: inexact digit division" % F.name)
        A = tuple(((-(c[0] // F.p)) % F.pM,) for c in C)
    R, pw = ad.const_el(F, 0), F.one
    for d in out:
        if d:
            R = tuple(F.cadd(a, F.cint(b, teich(F, d)))
                      for a, b in zip(R, pw))
        pw = F.emul(pw, pi)
    ok(F.val(ad.esub(F, w, R)) >= n, "%s: digit reconstruction" % F.name)
    return out


def newton_sqrt_el(F, c_el):
    """Element square root of a 1-unit (odd p), Newton from x = 1."""
    x = ad.const_el(F, 1)
    inv2 = pow(2, -1, F.pM)
    for _ in range(8):
        y = F.emul(c_el, unit_inv(F, x))
        x = tuple(F.cint(F.cadd(a, b), inv2) for a, b in zip(x, y))
    ok(F.val(ad.esub(F, F.emul(x, x), c_el)) >= F.amax,
       "%s: newton sqrt failed" % F.name)
    return x


# ---------------------------------------------------------------- [A]


def section_a():
    print("\n[A] the p-content lemma (TR1): sigma formula == integer v_p")
    for p, ns, rmax in [(3, [3, 9, 27], 4), (5, [5, 25], 3), (7, [7, 49], 3)]:
        rows = 0
        for n in ns:
            seen = set()
            stack = [[]]
            while stack:
                m = stack.pop()
                if m:
                    key = tuple(sorted(m))
                    if key not in seen:
                        seen.add(key)
                        ok(sigma_vp(n, m, p) == vp_multinomial(n, m, p),
                           "p-content mismatch p=%d n=%d %s" % (p, n, m))
                        rows += 1
                if len(m) < rmax:
                    lo = m[-1] if m else 1
                    for x in range(lo, n - sum(m) + 1):
                        stack.append(m + [x])
        print("  p=%d: %d part-multisets verified" % (p, rows))


# ---------------------------------------------------------------- [B]


def enumerate_window(p, c, m, relmax):
    """All monomials (one (value, index) part per distinct index, up
    to 4 indices) with rel = Lambda - p*i* in [0, relmax], exact v_p
    via sigma. Returns {rel: [monomials]}."""
    n = p ** (m + 1)
    istar = c * p ** m
    e = c * (p - 1) * p ** m
    lammax = p * istar + relmax
    imax = lammax - c
    found = {}

    def rec(i, parts, A, W, spsum):
        if len(parts) == 4 or i > imax:
            return
        rec(i + 1, parts, A, W, spsum)          # skip index i
        for x in range(1, n - A + 1):
            if c * (A + x) + W + i * x > lammax:
                break
            lb = spsum + sp(x, p)               # sigma lower bound
            if A + x < n:
                lb += 1
            if e * ((lb - 1) // (p - 1)) + c * (A + x) + W + i * x > lammax:
                continue
            parts.append((x, i))
            lam = (e * sigma_vp(n, [xx for xx, _ in parts], p)
                   + c * (A + x) + W + i * x)
            rel = lam - p * istar
            if 0 <= rel <= relmax:
                found.setdefault(rel, []).append(tuple(sorted(parts)))
            rec(i + 1, parts, A + x, W + i * x, spsum + sp(x, p))
            parts.pop()

    rec(0, [], 0, 0, 0)
    return found


def section_b():
    print("\n[B] the enumeration lemma (TR2-TR4, TR6): gate / empty / freedom")
    scopes = [(3, 1, 1), (3, 2, 1), (3, 3, 1), (3, 1, 2),
              (5, 1, 1), (5, 2, 1), (7, 1, 1)]
    for p, c, m in scopes:
        n, pm = p ** (m + 1), p ** m
        istar, e = c * p ** m, c * (p - 1) * p ** m
        # 5-part exclusion: sigma >= smin (next 1 mod p-1 above 5),
        # A >= 5, W >= 0+1+2+3+4 = 10 (distinct indices)
        smin = 5 + ((1 - 5) % (p - 1))
        ok(istar * (smin - 1) + c * 5 + 10 > p * istar + pm,
           "(%d,%d,%d): 5-part bound fails" % (p, c, m))
        w = enumerate_window(p, c, m, pm)
        gate = sorted(w.get(0, []))
        ok(gate == sorted([((n, 0),), ((pm, 0),)]),
           "(%d,%d,%d): gate list %s" % (p, c, m, gate))
        for rel in range(1, pm):
            ok(rel not in w, "(%d,%d,%d): rel-%d not empty: %s"
               % (p, c, m, rel, w.get(rel)))
        free = sorted(w.get(pm, []))
        want = sorted([((pm, 1),)] + ([((2 * pm, 0),)] if c == 1 else []))
        ok(free == want,
           "(%d,%d,%d): freedom carriers %s" % (p, c, m, free))
        gam = comb(n, pm) // p
        ok(comb(n, pm) % p == 0 and gam % p == 1,
           "(%d,%d,%d): gamma != 1 mod p" % (p, c, m))
        if m == 1:
            idag = c * (p - 1)
            l1 = e * 1 + (c + idag) * p          # tau_idag^p, one carry
            l2 = e * 2 + (c + idag) * 1          # tau_idag, two carries
            ok(l1 == l2 == e + p * istar,
               "(%d,%d,%d): coincidence level" % (p, c, m))
            ok(comb(n, 1) == p * p, "(%d,%d,%d): p^2 route" % (p, c, m))
        print("  (p,c,m)=(%d,%d,%d): gate pair, rel 1..%d empty, freedom"
              " %s" % (p, c, m, pm - 1, "rho1+pair" if c == 1 else "rho1"))


# ---------------------------------------------------------------- [C]


def field_readout(name, p, eis, amax, heavy, rng, n_heavy=400, n_light=40,
                  extra=()):
    """Census + digit twin: (F, spec, delta, digs, orbits)."""
    F = lc.LF(name, p, [0, 1], eis, amax)
    Fd = lc.LF(name + "-dig", p, [0, 1], eis, 9 * F.e)
    w, pi = w_element(Fd)
    delta = Fd.val(ad.esub(Fd, w, ad.const_el(Fd, 1)))
    digs = w_digits(Fd, w, pi, min(12, 9 * F.e // 2))
    units = []
    for c in heavy:
        units += list(ad.sample_class(F, c, n_heavy, rng))
    for c in range(1, min(F.amax, 2 * F.seat + 2)):
        units += list(ad.sample_class(F, c, n_light, rng))
    units += list(extra)
    spec, orbits = ad.landing_spectra(F, units, keep_orbits=True)
    tf.gear_check(F, orbits)
    ok(set(heavy) <= set(spec),
       "%s: heavy classes %s not all censused at the seat: %s"
       % (F.name, heavy, sorted(spec)))
    return F, spec, delta, digs, orbits


def law_row(F, spec, delta, p):
    """THE LAW ROW (TR5): every censused arrival class obeys
    L_min = p*i* + min(delta, p^m); rigid below freedom."""
    istar = F.seat
    for c in sorted(spec):
        t, m = c, 0
        while t < istar:
            t, m = t * p, m + 1
        ok(t == istar, "%s: class %d not on the seat" % (F.name, c))
        pm = p ** m
        want = p * istar + min(delta, pm)
        got = min(spec[c])
        ok(got == want, "%s: class %d min %d != %d = p*i* + min(%d, %d)"
           % (F.name, c, got, want, delta, pm))
        if delta < pm:
            ok(spec[c] == {want},
               "%s: class %d spectrum %s not rigid below freedom"
               % (F.name, c, sorted(spec[c])))
        else:
            ok(all(v >= want for v in spec[c]),
               "%s: class %d value in the hole range: %s"
               % (F.name, c, sorted(spec[c])))


def fmt_delta(F, delta):
    return "CAP" if delta > 9 * F.e else str(delta)


def section_c(rng):
    print("\n[C] the field censuses: the gate, the ladder, the law")
    results = {}

    # --- e = 6, p = 3 (arrival class 1, starters class 3)
    e6 = [
        ("x^6+3x-3", [-3, 3, 0, 0, 0, 0, 1], "SL-C gate closed"),
        ("x^6+3x+3", [3, 3, 0, 0, 0, 0, 1], "SL-D delta 1"),
        ("x^6+6x+3", [3, 6, 0, 0, 0, 0, 1], "SL-D delta 1"),
        ("x^6+3x^2+3", [3, 0, 3, 0, 0, 0, 1], "SL-D delta 2"),
        ("x^6+3x^3+3", [3, 0, 0, 3, 0, 0, 1], "SL-D delta 3"),
        ("x^6+3 (C)", [3, 0, 0, 0, 0, 0, 1], "SL-E"),
        ("x^6-6 (D)", [-6, 0, 0, 0, 0, 0, 1], "SL-E"),
        ("zeta9 (K9)", [3, 9, 18, 21, 15, 6, 1], "SL-E"),
        ("x^6-3 (B)", [-3, 0, 0, 0, 0, 0, 1], "SL-E gate closed"),
        ("x^6-12 (B')", [-12, 0, 0, 0, 0, 0, 1], "SL-E gate closed"),
    ]
    for name, eis, tag in e6:
        F, spec, delta, digs, orbits = field_readout(
            name, 3, eis, 18, [1, 3], rng)
        law_row(F, spec, delta, 3)
        results[name] = (F, spec, delta, digs)
        print("  %-13s w0=%d delta=%-3s digs=%s %s  [%s]"
              % (name, digs[0], fmt_delta(F, delta), digs[1:6],
                 ad.fmt_spec(F, spec), tag))

    # gate-closed rows (SL-C + SL-E): whole spectra {9}
    for name in ["x^6+3x-3", "x^6-3 (B)", "x^6-12 (B')"]:
        F, spec, delta, digs = results[name]
        ok(digs[0] != 1 and delta == 0, "%s: gate not closed" % name)
        ok(spec[1] == {9} and spec[3] == {9},
           "%s: out spectra not {9} rigid" % name)
    ok(results["x^6+3x-3"][3][0] == 2, "x^6+3x-3: w0 != 2")

    # designed digit vectors + deltas (SL-D, SL-J)
    for name, dlt, wd in [("x^6+3x+3", 1, 2), ("x^6+6x+3", 1, 1),
                          ("x^6+3x^2+3", 2, 2), ("x^6+3x^3+3", 3, 2)]:
        F, spec, delta, digs = results[name]
        ok(digs[0] == 1 and delta == dlt and digs[dlt] == wd,
           "%s: digits %s delta %d != design" % (name, digs[:5], delta))
    ok(results["x^6+3x+3"][1][1] == {10}, "x^6+3x+3: class-1 not {10}")
    ok(results["x^6+3x^2+3"][1][1] == {11}, "x^6+3x^2+3: class-1 not {11}")

    # SL-E regression deltas + K9 digits
    ok(results["x^6+3 (C)"][2] > 54, "C: w != 1")
    ok(results["x^6-6 (D)"][2] == 6, "D: delta != 6")
    Fk, speck, dk, digk = results["zeta9 (K9)"]
    ok(dk == 3 and digk[3] == 2 and digk[4] == 1,
       "K9: delta/digits %d %s != (3; w3=2, w4=1)" % (dk, digk[:6]))
    # graded at the truncation
    for name in ["x^6+3x^3+3", "x^6+3 (C)", "x^6-6 (D)", "zeta9 (K9)"]:
        spec = results[name][1]
        ok(min(spec[1]) == 12 and len(spec[1]) > 1,
           "%s: class-1 floor 12 not graded: %s" % (name, sorted(spec[1])))

    # zeta_3 constructed at the SL-D field: sqrt(-3) = pi^3/sqrt(1+pi)
    F = lc.LF("x^6+3x+3-tor", 3, [0, 1], [3, 3, 0, 0, 0, 0, 1], 18)
    pi = pi_el(F)
    one_pi = tuple(F.cadd(a, b) for a, b in zip(ad.const_el(F, 1), pi))
    s = newton_sqrt_el(F, one_pi)
    pi3 = F.emul(F.emul(pi, pi), pi)
    rt = F.emul(pi3, unit_inv(F, s))
    ok(F.val(ad.esub(F, F.emul(rt, rt), ad.const_el(F, -3))) >= F.amax,
       "sqrt(-3) failed at x^6+3x+3")
    inv2 = pow(2, -1, F.pM)
    neg1 = ad.const_el(F, -1)
    z3 = tuple(F.cint(F.cadd(a, b), inv2) for a, b in zip(rt, neg1))
    ok(tf.phi_torsion(F, z3, 3) >= F.CAP, "zeta_3 not in x^6+3x+3")
    print("  zeta_3 constructed in x^6+3x+3: Phi_3 = 0 at CAP (gate label)")

    # --- the quadratics (starters only)
    for name, eis, closed in [("Q3(sqrt3)", [-3, 0, 1], True),
                              ("Q3(zeta3)", [3, 3, 1], False)]:
        F, spec, delta, digs, orbits = field_readout(
            name, 3, eis, 10, [1], rng)
        law_row(F, spec, delta, 3)
        ok((digs[0] != 1) == closed, "%s: gate parity" % name)
        print("  %-13s w0=%d delta=%-3s %s"
              % (name, digs[0], fmt_delta(F, delta), ad.fmt_spec(F, spec)))

    # --- e = 12: the first censused odd-p c > 1 arrival (SL-F)
    for name, eis in [("x^12+3x+3", [3, 3] + [0] * 10 + [1]),
                      ("x^12+3", [3] + [0] * 11 + [1])]:
        F, spec, delta, digs, orbits = field_readout(
            name, 3, eis, 28, [2, 6], rng, n_heavy=300, n_light=20)
        law_row(F, spec, delta, 3)
        ok({2, 6} <= set(spec), "%s: classes %s" % (name, sorted(spec)))
        print("  %-13s w0=%d delta=%-3s %s"
              % (name, digs[0], fmt_delta(F, delta), ad.fmt_spec(F, spec)))
    # the c > 1 rigid row + the graded truncation row
    # (law_row already asserted min/rigidity from measured delta)

    # --- e = 18: the first m = 2 (SL-G)
    for name, eis in [("x^18+3", [3] + [0] * 17 + [1]),
                      ("x^18+3x+3", [3, 3] + [0] * 16 + [1]),
                      ("x^18+3x^5+3", [3, 0, 0, 0, 0, 3] + [0] * 12 + [1])]:
        F, spec, delta, digs, orbits = field_readout(
            name, 3, eis, 42, [1, 3, 9], rng, n_heavy=300, n_light=15)
        law_row(F, spec, delta, 3)
        ok({1, 3, 9} <= set(spec), "%s: classes %s" % (name, sorted(spec)))
        print("  %-13s w0=%d delta=%-3s %s"
              % (name, digs[0], fmt_delta(F, delta), ad.fmt_spec(F, spec)))

    # --- p = 5 (SL-H) + regressions Z25, E5
    phi25 = [sum(comb(5 * j, k) for j in range(5)) for k in range(21)]
    for name, eis in [("x^20+5x+5", [5, 5] + [0] * 18 + [1]),
                      ("Q5(zeta25)", phi25),
                      ("x^20-5 (E5)", [-5] + [0] * 19 + [1])]:
        F, spec, delta, digs, orbits = field_readout(
            name, 5, eis, 34, [1, 5], rng, n_heavy=200, n_light=10)
        law_row(F, spec, delta, 5)
        print("  %-13s w0=%d delta=%-3s %s"
              % (name, digs[0], fmt_delta(F, delta), ad.fmt_spec(F, spec)))
        if name == "x^20+5x+5":
            ok(delta == 1 and digs[1] == 4 and spec[1] == {26},
               "x^20+5x+5: %s" % ad.fmt_spec(F, spec))
        if name == "Q5(zeta25)":
            ok(delta >= 5 and min(spec[1]) == 30 and min(spec[5]) == 26,
               "Z25: floors %s" % ad.fmt_spec(F, spec))
        if name == "x^20-5 (E5)":
            ok(digs[0] != 1 and spec[1] == {25} and spec[5] == {25},
               "E5: gate/spectra")


# ---------------------------------------------------------------- [D]


def section_d():
    print("\n[D] SL-I: the p = 2 intermediate rungs ARE the tame law")

    def generic(pistar, mu, digs):
        pm = 2 ** mu
        fnz = next((j for j in range(1, pm) if digs[j]), pm)
        return 2 * pistar + fnz

    rows = 0
    for digs in itertools.product((0, 1), repeat=12):
        digs = (1,) + digs
        ok(m16.rung2(digs) == generic(8, 2, digs), "m16.rung2 %s" % (digs,))
        ok(m16.rung4(digs) == generic(8, 1, digs), "m16.rung4 %s" % (digs,))
        ok(m32.rung2_16(digs) == generic(16, 3, digs),
           "m32.rung2_16 %s" % (digs,))
        ok(m32.rung4_16(digs) == generic(16, 2, digs),
           "m32.rung4_16 %s" % (digs,))
        ok(m32.rung8_16(digs) == generic(16, 1, digs),
           "m32.rung8_16 %s" % (digs,))
        rows += 1
    print("  all %d digit vectors: rung == p*i* + min(first-nonzero, 2^mu)"
          % rows)


# ------------------------------------------------------------------- run


def run():
    rng = random.Random(196)
    print("THE TAME READOUT — the odd-p face of the readout theorem")
    print("=" * 64)
    section_a()
    section_b()
    section_c(rng)
    section_d()
    print("\nALL GREEN — %d checks this module (+%d imported machinery)"
          % (CHECKS, tf.CHECKS))


if __name__ == "__main__":
    run()
