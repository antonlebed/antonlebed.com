"""explore_slot_algebra.py — THE SLOT-FORM ALGEBRA: the landing form,
the general forced-slot digit laws, the odd-p triangle, and the true
orbit action.

THE QUESTION. explore_deep_spectrum.py charted the
post-freedom game but left three algebra gaps: the second slot's
digit -rho_0(w_3+w_5) is OBSERVATION-tier (three words); the
eta-orbit invariance constraints are measured, not derived; and the
odd-p grid -> word bijection is brute at e = 6 only. Derive all
three as exact algebra.

THE HAND DERIVATION (derived by hand before this script existed).

P1 (THE LANDING FORM). The one-step map is exact: (1+x)^p - 1 =
   x^p - w pi^e x g(x), g(x) = sum_{j=1}^{p-1} (C(p,j)/p) x^{j-1},
   using the element identity p = -w pi^e. Iterating m+1 times from
   a class-(c,m) walker (v(x) = c, seat i* = c p^m) and normalizing
   X_k = x_k / pi^{c p^k}:

       L  =  p i*  +  v( 1 - w g(x_m) X_m^{1-p} )        [EXACT]

   with X_m = X_0^{p^m} PROD_{k<m} (1 - w pi^{D_k} G_k)^{p^{m-1-k}},
   D_k = c(p-1)(p^m - p^k). In-window (rel <= e), mod p, with
   u := pi^{p^m}, z := pi^{p^{m-1}}, F(z) := sum s_i z^i (the
   walker's canonical digits of X_0), phi(y) := sum_{j=0}^{p-2}
   [(-1)^j/(j+1)] y^j (the truncated log; C(1-p,n) == 0 mod p for
   2 <= n <= p-1), everything collapses to

       V = 1 - w (1+xi) phi(rho u^c (1+xi)),
       xi = F(u) - w pi^{rel_c} Gamma(z),
       Gamma = (1+F(z)) (1+F(u))^{-1} phi(rho z^c (1+F(z))),

   only the k = m-1 unroll factor surviving in-window (depth
   D_{m-1} = rel_c; k <= m-2 land past e). Landing digit =
   rho_0 * V_rel. Gate/ladder/freedom/forks/slot-lattice (TR2-TR6,
   DR1-DR2) all fall out; hand-rederived from V: x^18+3x^5+3 class
   (3,1) ceiling rel 5 (between-lattice -w_5), x^18+3 class (1,2)
   holes rels 10,11 + slot-0 ceiling rel 12, K9's rel-6 digit.

P2 (THE SLOT LAWS). Slot-game regime (gate open, delta >= p^m, so
   w_j = 0 for 0 < j < p^m). Forced slot t (t != -c mod p): D_t =
   -w_{rel_c + p^{m-1} t} + (w^2 Gamma)_{p^{m-1} t}. Hand values:
   D_0 = w_0^2 - w_{rel_c} (all scopes; DR3 rederived);
   fork-1 elimination (s_1 = -w_{p^m} - c2bar rho at c = 1) makes
   the phi-offset cancel between fork and slot:
       D_1 = -( w_{p^m} + w_{rel_c + p^{m-1}} )
   — the deep-spectrum observation DERIVED, conjecturally at every
   c (the offset is absent on both sides for c >= 2). At the
   deferral rel e the s_{i-dagger} coefficient cancels exactly in
   F_p (pivot w(w-1) + h.o.t. = TR6); the RESIDUAL forced digit at
   (3,1,1) is V_6 = w_3^2 - w_6 (K9: 4 - 1 == 0: the 15-hole).
   Between-lattice rels carry forced digits -w_r - (word cross
   terms): the whole post-freedom window is a word readout.

P3 (THE TRIANGLE, odd p, general e). F(x) = x^e + sum p b_i x^i
   - p d Eisenstein: w = (-1/d)(1-T)^{-1}, T = sum (b_i/d) pi^i.
   Grid (b_i mod p; d mod p^2) -> word (w_0..w_e) is UNITRIANGULAR:
   w_0 = -1/d mod p; w_r = -beta_r w_0^2 + poly(beta_{<r}, d mod p)
   for 1 <= r <= e-1 (T^1 is the diagonal; T^k parts are < r;
   p-parts and Teichmueller carries deposit at r + e > e); w_e =
   (second digit of d) * unit + poly (the level-0 carry, the ONE
   carry landing in the word). Corollaries: grid -> word bijection
   at EVERY e (seat-free — no arrival game needed), greedy
   digit-by-digit design of any word.

P4 (THE ORBIT ACTION). pi' = eta pi twists the element, w' =
   w eta^{-e}, with v(eta^{-e} - 1) = min_j ((m-j)e + p^j k) =
   p^m k for eta in U_k, k < cp (binomial p-content; leading coeff
   c*a*unit != 0; at k = cp the j = m, m-1 terms TIE and can cancel
   deeper — the run: v in {19, 21} > p^m cp at e = 12); the CHART
   re-expansion adds digit mixing
   [w_r] r a pi^{r+k} (killed at p | r). Full-word twist-invariance
   boundary is k > i-dagger = c(p-1), NOT k >= i* (they coincide
   only at c = 1, m = 1 — the censused case). THE EXTRACTOR PAIR:
   w_digits(F, W, pi, n) divides by multiplying pi^{e-1} W (-1/p),
   correct only for the chart's OWN pair (pi', -p/pi'^e).
   explore_deep_spectrum section_d(i) passed (w eta^{-e}, OLD pi):
   the unroll shows it extracts digits of w' along the uniformizer
   pi eta^e — a THIRD chart, matched to neither element;
   reconstruction passes at n = 7 only by depth luck (d_1 = d_2 = 0
   plus p-power boosts).
   The true chart word is w_digits(F, w eta^{-e}, eta pi, n).

PREDICTIONS (fixed before the run; a miss falsifies its lemma):

SA-A (the landing form, end-to-end): per gate-open censused field
   (the four gate-open e=6 fields + K9 + x^12+3 + x^18+3) and class
   (m >= 1), ~25 sampled walkers each: the first r <= e with
   V_r(measured word, measured walker digits) != 0 equals the
   measured landing rel; if none, measured rel > e.
SA-B (symbolic elimination; scopes (3,1,1),(5,1,1),(3,1,2),(3,2,1),
   (5,2,1)): fork s_i-coefficients constant units; forced-slot
   count = c(p-2)+1; s_{i-dagger} cancels exactly at rel e;
   D_0-form = 1 - w_{rel_c} at every scope; D_1-form =
   -(w_{p^m} + w_{rel_c+p^{m-1}}) at the four slot-1-forced scopes;
   deferral residual at (3,1,1) = w_3^2 - w_6.
SA-C (designed splits, via the triangle solve):
 (1) LAND-15 pair at p=3 e=6: word [1,0,0,0,1,0,1] -> class-1
     visits {12, 15}, stick 15 (a landing never censused at any
     (3,1,1) field); word [1,0,0,0,1,0,0] -> passes 15, visits
     {12,16,17,18}, climbs to CAP (m=1: every rel above e has a
     fresh digit) => zeta_9 in it => the field IS Q_3(zeta_9) and
     its word lies in K9's genuine chart-word set.
 (2) p=5 e=20 pair, class 1 (rel_c = 16): word A (w_5=1, w_16=1,
     w_17=2): visits {30,35,40,42}, stick 42 (slot-1: -(1+2) != 0);
     word B (w_5=1, w_16=1, w_17=4): stick > 42 (slot-1: 1+4 == 0),
     stick == the engine's own next nonzero forced digit.
 (3) x^18+3 class (1,2): engine forms at the all-zero word predict
     holes rels 10,11 and slot-0 ceiling rel 12 (= censused 37, 38,
     39).
SA-D (the triangle): full census p=3 e=4 (162) and p=5 e=3 (500):
   words pairwise distinct, w_0 = -1/d; flip tests: flipping beta_r
   moves digit r by EXACTLY -Delta w_0^2 with prefix unchanged;
   flipping d's second digit moves w_e only, bijectively; p=3 e=6
   (1458) distinct + sampled flips. e = 3, 4 are NON-SEAT windows:
   the theorem is seat-free.
SA-E (the orbit action):
 (1) at x^12+3x+3 (e=12, class (2,1)): sampled eta in exact U_k,
     v(eta^{-12} - 1) = 3k for k = 1..5 (k = 6 = cp is the tie
     case: record only). Kills "full invariance iff k >= i*" as
     the general boundary.
 (2) the genuine chart-word set of K9 = {w_digits over eta reps
     [t](1+a1 pi)(1+a2 pi^2)(1+a3 pi^3)} (54 reps exhaust: twist
     depth 3k, mixing depth r+k, word support r >= 3): every
     member satisfies w_4 = 1 AND w_3 + w_5 == 0 AND w_6 = w_3^2;
     the section_d(i) vector [1,0,0,1,1,1,0] violates w_3+w_5 == 0
     hence is NOT a genuine chart word (of any uniformizer); the
     a3 digit never changes the word (the p | r kill at r = 3).

THE DESIGN. [P] F_p multivariate polynomials + pi-power series;
build V symbolically per P1; elimination walk rel 1..e (forks solve
s_i, coefficients asserted constant units; forced rels recorded as
pure word polynomials; deferral cancellation asserted); SA-B forms
asserted, the slot-form table printed. [N] SA-A: measured word
(ds.word_of) + measured walker digits (exact pi-division then
w_digits) -> first nonzero V digit vs measured landing. [T] SA-D
censuses + flips + solve_word (unitriangular greedy, one field per
level). [S] SA-C splits, climbs via ds.climb_row. [O] SA-E: true
chart words (matched extractor pairs). Labels never read orbits;
the engine only ever reads measured digits.
Run: python prime/code/explore_slot_algebra.py

FINDINGS (entered post-run, copied from printed output; tiers use
the standard scale: property / observation / pattern / rule /
criterion / theorem).

1. THE LANDING FORM (theorem — the P1 identity is exact algebra;
   verified end-to-end rule-in-range): L = p i* + v(1 - w g(x_m)
   X_m^{1-p}), and its in-window mod-p collapse V predicts the
   landing of EVERY sampled walker: 200/200 across eight
   field-classes (five e = 6 fields, x^12+3 (2,1), x^18+3 (3,1) and
   (1,2)) — the first nonzero V-digit equals the measured landing
   rel, walker by walker, not just spectra. The whole monomial
   enumeration of the readout theorem sits inside one identity.

2. THE SLOT LAWS — THE RECIPROCAL LAW (rule at the five scopes
   (3,1,1),(5,1,1),(3,1,2),(3,2,1),(5,2,1), symbolically exhaustive
   per scope): fork-eliminating and passage-conditioning V yields
   the complete forced-digit table. Every forced rel r has diagonal
   -w_r; the slot lattice reads ONLY fork-rel digits: with K(z) =
   sum_{i<i-dagger} w_{i p^m} z^i the conditioned slot series is

       D_t = [1/(1 + K)]_t - w_{rel_c + p^{m-1} t}

   EXACT at c = 1 for ALL t (deferral included: the (3,1,1) residual
   w_3^2 - w_6 and (3,1,2)'s w_9^2 - w_18 are its z^2 row, (5,1,1)'s
   rel-20 its z^4 row) and at every t < p for the c = 2 scopes; the
   residual intrusion (the phi/F(u) window products of the hand
   derivation) observed from t = 5 = p at (5,2,1) but ONLY at the
   deferral t = 4 = i-dagger at (3,2,1) — slots proper are
   reciprocal-exact there; the onset law closed: the two-layer
   law T = Omega^3(1+FB)/(1+K), explore_reciprocal_layer.py.
   D_1 = -(w_{p^m} + w_{rel_c+p^{m-1}}): the
   deep-spectrum observation -rho_0(w_3+w_5) is now derived, and K9's
   15-hole is the z^2 row vanishing (4 - 1 == 0 mod 3). Passage
   conditioning is load-bearing: unconditioned forms carry
   cross-terms in the passed digits (the (*) rows).

3. THE TRIANGLE (theorem — the P3 argument is general in (p, e),
   seat-free; census rule-in-range): the grid (b_i mod p; d mod p^2)
   -> word map is unitriangular with diagonal -w_0^2: full censuses
   at (3,4) 162/162, (5,3) 500/500, (3,6) 1458/1458 distinct, EVERY
   flip moving digit r by exactly -Delta w_0^2 with prefix frozen,
   d's carry digit moving w_e alone bijectively. The greedy solve
   designs any word: LAND-15 (x^6+6x^4-15, word [1,0,0,0,1,0,1])
   lands class-1 {12, 15} stick 15 — a landing absent from every
   censused (3,1,1) field, designed into existence from D_e =
   w_3^2 - w_6 != 0; the p = 5 pair splits the slot-1 law on cue
   (w_17 = 2: stick 42; w_17 = 4: hole, stick 43 = the engine's own
   rel-18 form); x^6+6x^4-24 ([1,0,0,0,1,0,0]) climbs to CAP —
   zeta_9 in it, the field IS Q_3(zeta_9).

4. THE TRUE ORBIT ACTION (rule in range; corrects deep-spectrum
   finding 4's boundary and vectors): the twist obeys
   v(eta^{-e} - 1) = p^m k exactly (k = 1..5 at x^12+3x+3, e = 12;
   k = 6 = cp is the tie case, v in {19, 21}), so the word caps at
   k > i-dagger = c(p-1), NOT k >= i* (equal only at c = 1, m = 1 —
   the censused coincidence); chart re-expansion mixes digit r into
   r + k with coefficient r*a (dead at p | r). K9's genuine
   chart-word set (matched extractor pairs (eta pi, w eta^{-e}),
   all 54 uniformizer reps) is EXACTLY the 3-word solution variety
   of its forced-digit constraints {w_4 = 1, w_5 = -w_3, w_6 =
   w_3^2}: the orbit IS the constraint variety, the spectrum's
   field-invariance made word-level exact. The section_d(i) vectors
   ([1,0,0,1,1,1,0]) are mixed-pair artifacts — w_digits conflates
   element and division helper, and (old pi, new w) extracts digits
   along neither chart; the artifact vector violates w_3 + w_5 == 0
   and is NOT a chart word of any uniformizer. The LAND-15-B word
   IS in the variety: the design is the anchor, third specimen.

PRE-GREEN FAILURES (adjudicated during development):
(1) Run 1: the frozen "D_0 = w_0^2 - w_{rel_c} at ALL scopes"
    printed passage cross-terms at (5,1,1) (w_10 w_6 + w_11 w_5 +
    ...): the hand lemma was imprecise — the slot forms are
    PASSAGE-CONDITIONED (reduced mod the earlier forced digits,
    each linear in its own -w_r). The (3,1,1) forms were exact as
    frozen; conditioning recovers the predicted forms at every scope.
(2) Runs 2-4: engine scaffolding — regime rels below p^m are
    identically zero (no diagonal to solve); the walker extractor
    first reused w_digits, whose conflated element/helper pair is
    the SAME species as the section_d(i) bug this file exposes
    (fixed: digits_of with an explicit helper).
(3) Run 5: the reciprocal assert double-counted w_e (K must stop at
    i-dagger - 1: the deferral's -w_e is its slot DIAGONAL, which is
    the uniformity, not a fork coefficient).

RUN RECORD (python explore_slot_algebra.py, ~2.7 s, exit 0): 16,891
checks this module + 21,194 through the imported census/gear
machinery. Printed rows as copied: [P] five scope tables, c = 2
residuals {4: w3^2} / {5: 4w5, 6: w5^2, 7: ..., 8: ...}; [N] 25/25
walkers at each of 8 field-classes; [T] 162 + 500 + 1458 words
distinct, flips unitriangular, diagonal -w_0^2 exact; [S] L15A
{12,15} stick 15, L15B passes 15 -> CAP (stick >= 43), p5A
{30,35,40,42} stick 42, p5B stick 43 = rel-18 form, x^18+3 (1,2)
holes 10,11 + ceiling 12; [O] v = 3k at k = 1..5, tie k = 6 in
{19,21}; chart-word set [1,0,0,0,1,0,0] / [1,0,0,1,1,2,1] /
[1,0,0,2,1,1,1] over 54 reps, artifact vector excluded, L15B word
included.
"""

import itertools
import random
from math import comb

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_tame_readout as tr
import explore_deep_spectrum as ds

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ------------------------------------------------- [P] F_p polynomials

# poly = {monomial: coeff mod p}, monomial = sorted tuple of (var, exp)


def padd(p, a, b):
    out = dict(a)
    for mo, co in b.items():
        out[mo] = (out.get(mo, 0) + co) % p
    return {mo: co for mo, co in out.items() if co}


def pmul(p, a, b):
    out = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            dd = dict(m1)
            for v, x in m2:
                dd[v] = dd.get(v, 0) + x
            mo = tuple(sorted(dd.items()))
            out[mo] = (out.get(mo, 0) + c1 * c2) % p
    return {mo: co for mo, co in out.items() if co}


def pconst(p, c):
    c %= p
    return {(): c} if c else {}


def pvar(v):
    return {((v, 1),): 1}


def psub(p, poly, var, val):
    out = {}
    for mo, co in poly.items():
        dd = dict(mo)
        k = dd.pop(var, 0)
        base = {tuple(sorted(dd.items())): co}
        for _ in range(k):
            base = pmul(p, base, val)
        for mm, cc in base.items():
            out[mm] = (out.get(mm, 0) + cc) % p
    return {mo: co for mo, co in out.items() if co}


def peval(p, poly, env):
    tot = 0
    for mo, co in poly.items():
        t = co
        for v, x in mo:
            t = (t * pow(env[v], x, p)) % p
        tot = (tot + t) % p
    return tot


def smul(p, A, B, top):
    out = [{} for _ in range(top + 1)]
    for i, a in enumerate(A):
        if a and i <= top:
            for j, b in enumerate(B):
                if b and i + j <= top:
                    out[i + j] = padd(p, out[i + j], pmul(p, a, b))
    return out


def sinv(p, A, top):
    """Inverse of a series with A[0] = 1."""
    assert A[0] == {(): 1}
    out = [{} for _ in range(top + 1)]
    out[0] = {(): 1}
    for k in range(1, top + 1):
        acc = {}
        for j in range(1, k + 1):
            if j < len(A) and A[j]:
                acc = padd(p, acc, pmul(p, A[j], out[k - j]))
        out[k] = {mo: (-co) % p for mo, co in acc.items()}
    return out


def sphi(p, Y, top):
    """phi(Y) = sum_{j=0}^{p-2} [(-1)^j / (j+1)] Y^j, v(Y) >= 1."""
    assert not Y[0]
    out = [pconst(p, 1)] + [{} for _ in range(top)]
    pw = [pconst(p, 1)] + [{} for _ in range(top)]
    for j in range(1, p - 1):
        pw = smul(p, pw, Y, top)
        cf = (pow(-1, j, p) * pow(j + 1, -1, p)) % p
        for r in range(top + 1):
            if pw[r]:
                out[r] = padd(p, out[r], {mo: (co * cf) % p
                                          for mo, co in pw[r].items()})
    return out


def build_V(p, c, m, regime):
    """The in-window landing form V_0..V_e, symbolic (gate open,
    w_0 = 1). regime: impose w_j = 0 for 0 < j < p^m."""
    pm, pm1 = p ** m, p ** (m - 1)
    e = c * (p - 1) * pm
    relc = c * pm1 * (p - 1) ** 2
    idag = c * (p - 1)
    W = [pconst(p, 1)]
    for j in range(1, e + 1):
        W.append({} if (regime and j < pm) else pvar("w%d" % j))
    Fu = [{} for _ in range(e + 1)]
    for i in range(1, idag + 1):
        if i * pm <= e:
            Fu[i * pm] = pvar("s%d" % i)
    # Gamma to depth gtop = e - relc
    gtop = e - relc
    Fz = [{} for _ in range(gtop + 1)]
    for i in range(1, idag + 1):
        if i * pm1 <= gtop:
            Fz[i * pm1] = pvar("s%d" % i)
    oneFz = [padd(p, pconst(p, 1), Fz[0])] + Fz[1:]
    oneFz[0] = pconst(p, 1)
    invFu = sinv(p, [pconst(p, 1)] + Fu[1:gtop + 1], gtop)
    y = [{} for _ in range(gtop + 1)]
    for r in range(gtop + 1 - c * pm1):
        if oneFz[r]:
            y[r + c * pm1] = pmul(p, pvar("r"), oneFz[r])
    gam = smul(p, smul(p, oneFz, invFu, gtop), sphi(p, y, gtop), gtop)
    # xi = F(u) - w pi^relc Gamma
    WG = smul(p, W[:gtop + 1], gam, gtop)
    xi = [dict(x) for x in Fu]
    for t in range(gtop + 1):
        if WG[t]:
            xi[relc + t] = padd(p, xi[relc + t],
                                {mo: (-co) % p for mo, co in WG[t].items()})
    onexi = [pconst(p, 1)] + xi[1:]
    y2 = [{} for _ in range(e + 1)]
    for r in range(e + 1 - c * pm):
        if onexi[r]:
            y2[r + c * pm] = pmul(p, pvar("r"), onexi[r])
    E = smul(p, onexi, sphi(p, y2, e), e)
    WE = smul(p, W, E, e)
    V = [padd(p, pconst(p, 1), {mo: (-co) % p for mo, co in WE[0].items()})]
    for r in range(1, e + 1):
        V.append({mo: (-co) % p for mo, co in WE[r].items()})
    meta = dict(p=p, c=c, m=m, e=e, pm=pm, pm1=pm1, relc=relc, idag=idag)
    return V, meta


def split_linear(p, c, m, r, poly, var):
    """Split poly = coeff*var + rest, var strictly linear."""
    lin, rest = {}, {}
    for mo, co in poly.items():
        dd = dict(mo)
        k = dd.get(var, 0)
        ok(k <= 1, "(%d,%d,%d) rel %d: %s power %d" % (p, c, m, r, var, k))
        if k == 1:
            dd.pop(var)
            lin[tuple(sorted(dd.items()))] = co
        else:
            rest[mo] = co
    return lin, rest


def eliminate(p, c, m):
    """Fork-eliminate the regime V; return (forced digit polys D,
    passage-conditioned forms Dc, meta). Dc[r] = D[r] reduced mod
    the ideal of the earlier forced digits (the walker REACHED r):
    each forced digit is -w_r + rest, so passage substitutes
    w_r := rest downstream."""
    V, mt = build_V(p, c, m, regime=True)
    e, pm, idag = mt["e"], mt["pm"], mt["idag"]
    forks = {i * pm: i for i in range(1, idag)}
    solved = {}
    passage = {}
    D, Dc = {}, {}
    ok(not V[0], "(%d,%d,%d): gate digit nonzero: %s" % (p, c, m, V[0]))
    for r in range(1, e + 1):
        poly = V[r]
        for var, val in solved.items():
            poly = psub(p, poly, var, val)
        if r in forks:
            var = "s%d" % forks[r]
            lin, rest = split_linear(p, c, m, r, poly, var)
            ok(lin == {(): p - 1},
               "(%d,%d,%d) rel %d: fork coeff not -1: %s" %
               (p, c, m, r, lin))
            solved[var] = rest  # -1 * s + rest = 0  =>  s = rest
        else:
            svars = {v for mo in poly for v, _ in mo if v[0] == "s"}
            if r == e:
                ok("s%d" % idag not in svars,
                   "(%d,%d,%d): deferral s_%d survives at rel e: %s" %
                   (p, c, m, idag, poly))
            ok(not svars, "(%d,%d,%d) rel %d: walker vars %s in forced "
               "digit" % (p, c, m, r, svars))
            if r < pm:
                ok(not poly, "(%d,%d,%d) rel %d: regime ladder digit "
                   "nonzero: %s" % (p, c, m, r, poly))
                continue
            D[r] = poly
            cond = poly
            for var, val in passage.items():
                cond = psub(p, cond, var, val)
            Dc[r] = cond
            wl, wrest = split_linear(p, c, m, r, cond, "w%d" % r)
            ok(wl == {(): p - 1},
               "(%d,%d,%d) rel %d: forced diagonal not -w_r: %s" %
               (p, c, m, r, wl))
            passage["w%d" % r] = wrest
    return D, Dc, mt


def fmt_poly(poly):
    if not poly:
        return "0"
    parts = []
    for mo, co in sorted(poly.items()):
        s = "" if (co == 1 and mo) else str(co)
        s += "*".join("%s^%d" % (v, x) if x > 1 else v for v, x in mo)
        parts.append(s if s else str(co))
    return " + ".join(parts)


def section_p():
    print("\n[P] SA-B: the symbolic slot-form table (fork-eliminated)")
    tables = {}
    for p, c, m in [(3, 1, 1), (5, 1, 1), (3, 1, 2), (3, 2, 1), (5, 2, 1)]:
        D, Dc, mt = eliminate(p, c, m)
        tables[(p, c, m)] = (D, mt)
        e, pm, pm1 = mt["e"], mt["pm"], mt["pm1"]
        relc, idag = mt["relc"], mt["idag"]
        forced_slots = [t for t in range(idag + 1) if t % p != (-c) % p]
        ok(len(forced_slots) == c * (p - 2) + 1,
           "(%d,%d,%d): forced slot count %d != %d" %
           (p, c, m, len(forced_slots), c * (p - 2) + 1))
        # D_0 conditioned form at every scope
        ok(Dc[relc] == {(): 1, (("w%d" % relc, 1),): p - 1},
           "(%d,%d,%d): D_0 %s" % (p, c, m, fmt_poly(Dc[relc])))
        # D_1 conditioned form where slot 1 is forced
        if 1 % p != (-c) % p:
            r1 = relc + pm1
            want = {(("w%d" % pm, 1),): p - 1, (("w%d" % r1, 1),): p - 1}
            ok(Dc[r1] == want, "(%d,%d,%d): D_1 %s" %
               (p, c, m, fmt_poly(Dc[r1])))
        # deferral residual at (3,1,1)
        if (p, c, m) == (3, 1, 1):
            ok(Dc[e] == {(("w3", 2),): 1, (("w6", 1),): 2},
               "(3,1,1): deferral residual %s" % fmt_poly(Dc[e]))
        # THE RECIPROCAL LAW: conditioned slot series vs 1/(1 + K),
        # K = the fork-digit series (exact at c = 1; c >= 2 residuals)
        K = [pconst(p, 1)] + [pvar("w%d" % (i * pm))
                              for i in range(1, idag)]
        K += [{}] * (idag + 1 - len(K))
        R = sinv(p, K, idag)
        resid = {}
        for t in range(idag + 1):
            r = relc + pm1 * t
            if r not in Dc:
                continue
            want = padd(p, R[t], {(("w%d" % r, 1),): p - 1})
            diff = padd(p, Dc[r], {mo: (-co) % p for mo, co in
                                   want.items()})
            if diff:
                resid[t] = diff
        if c == 1:
            ok(not resid, "(%d,%d,%d): reciprocal law fails: %s" %
               (p, c, m, {t: fmt_poly(q) for t, q in resid.items()}))
        else:
            print("    c = %d reciprocal residuals (the phi/F(u) window"
                  " intrusion): %s" % (c, {t: fmt_poly(q)
                                           for t, q in resid.items()}))
        shown = [r for r in sorted(Dc) if r >= pm]
        print("  (%d,%d,%d) e=%-2d relc=%-2d conditioned forced digits"
              " (rel >= p^m):" % (p, c, m, e, relc))
        for r in shown:
            tag = ("slot t=%d" % ((r - relc) // pm1)
                   if r >= relc and (r - relc) % pm1 == 0 and r != e else
                   "deferral" if r == e else "ladder")
            star = "" if D[r] == Dc[r] else " (*)"
            print("    rel %-3d %-9s D = %s%s"
                  % (r, tag, fmt_poly(Dc[r]), star))
    print("  slot-form table asserted (passage-conditioned): D_0 = "
          "1 - w_relc (5 scopes),\n    D_1 = -(w_p^m + w_relc+p^m-1) "
          "(4 scopes), deferral s-cancellation exact\n    everywhere; "
          "(*) = passage cross-terms present pre-conditioning")
    return tables


# --------------------------------------------------- [N] the landing form


def div_pi(F, x, w, k):
    """Exact division of x by pi^k (mirrors w_digits' inner step)."""
    pik = F.one
    for _ in range(F.e - 1):
        pik = F.emul(pik, tr.pi_el(F))
    for _ in range(k):
        Cx = F.emul(F.emul(x, pik), w)
        ok(all(cc[0] % F.p == 0 for cc in Cx),
           "%s: inexact pi division" % F.name)
        x = tuple(((-(cc[0] // F.p)) % F.pM,) for cc in Cx)
    return x


def digits_of(F, A, pi, w, n):
    """Canonical digits of ANY element A, with the chart's own helper
    pair (pi, w = -p/pi^e) doing the division — w_digits conflates
    element and helper (correct only when A IS the chart's w)."""
    out = []
    for _ in range(n):
        d = A[0][0] % F.p
        out.append(d)
        B = [list(cc) for cc in A]
        B[0][0] = (B[0][0] - tr.teich(F, d)) % F.pM
        A = div_pi(F, tuple(tuple(cc) for cc in B), w, 1)
    R, pw = ad.const_el(F, 0), F.one
    for d in out:
        if d:
            R = tuple(F.cadd(a, F.cint(b, tr.teich(F, d)))
                      for a, b in zip(R, pw))
        pw = F.emul(pw, pi)
    return out, R


def walker_digits(F, u, w, pi, c, n):
    """(rho_0, s_1..s_n) of the class-c walker u."""
    x = ad.esub(F, u, ad.const_el(F, 1))
    X0 = div_pi(F, x, w, c)
    rho = X0[0][0] % F.p
    ok(rho != 0, "%s: walker not class %d" % (F.name, c))
    inv = tr.teich(F, pow(rho, -1, F.p))
    X0 = tuple((cc[0] * inv % F.pM,) for cc in X0)
    digs, R = digits_of(F, X0, pi, w, n + 1)
    ok(F.val(ad.esub(F, X0, R)) >= n + 1,
       "%s: walker digit reconstruction" % F.name)
    ok(digs[0] == 1, "%s: normalized walker digit0 %d" % (F.name, digs[0]))
    return rho, digs[1:]


def section_n(rng):
    print("\n[N] SA-A: the landing form vs measured landings")
    fields = [
        ("x^6+3x^4+3", 3, [3, 0, 0, 0, 3, 0, 1], 22, [(1, 1)]),
        ("x^6-3x^4+3", 3, [3, 0, 0, 0, -3, 0, 1], 22, [(1, 1)]),
        ("x^6+3 (C)", 3, [3, 0, 0, 0, 0, 0, 1], 22, [(1, 1)]),
        ("x^6+3x+3", 3, [3, 3, 0, 0, 0, 0, 1], 22, [(1, 1)]),
        ("zeta9 (K9)", 3, [3, 9, 18, 21, 15, 6, 1], 22, [(1, 1)]),
        ("x^12+3", 3, [3] + [0] * 11 + [1], 32, [(2, 1)]),
        ("x^18+3", 3, [3] + [0] * 17 + [1], 48, [(3, 1), (1, 2)]),
    ]
    Vcache = {}
    for name, p, eis, amax, classes in fields:
        F = lc.LF(name, p, [0, 1], eis, amax)
        w, pi = tr.w_element(F)
        e = F.e
        word = ds.word_of(name, p, eis, e)
        ok(word[0] == 1, "%s: gate closed" % name)
        for c, m in classes:
            if (p, c, m) not in Vcache:
                Vcache[(p, c, m)] = build_V(p, c, m, regime=False)
            V, mt = Vcache[(p, c, m)]
            pistar, idag = p * c * p ** m, mt["idag"]
            P = p ** (m + 1)
            nsamp, agree = 25, 0
            for u in ad.sample_class(F, c, nsamp, rng):
                rho, s = walker_digits(F, u, w, pi, c, idag + 1)
                env = {"r": rho}
                for i, sv in enumerate(s):
                    env["s%d" % (i + 1)] = sv
                for j in range(1, e + 1):
                    env["w%d" % j] = word[j]
                pred = None
                for r in range(1, e + 1):
                    if peval(p, V[r], env):
                        pred = r
                        break
                got = ds.land(F, u, P)
                if pred is None:
                    ok(got > pistar + e,
                       "%s class (%d,%d): predicted past-window, "
                       "measured %d" % (name, c, m, got))
                else:
                    ok(got == pistar + pred,
                       "%s class (%d,%d): predicted rel %d, measured %d"
                       % (name, c, m, pred, got - pistar))
                agree += 1
            print("  %-12s class (%d,%d): %d/%d walkers, V-digit == "
                  "landing" % (name, c, m, agree, nsamp))


# ------------------------------------------------------ [T] the triangle


def grid_eis(p, e, betas, d):
    return [(-p * d)] + [p * b for b in betas] + [1]


def census(p, e):
    words = {}
    for bs in itertools.product(range(p), repeat=e - 1):
        for d in range(1, p * p):
            if d % p:
                words[(bs, d)] = tuple(
                    ds.word_of("g", p, grid_eis(p, e, bs, d), e))
    return words


def section_t():
    print("\n[T] SA-D: the odd-p triangle — census, flips, diagonal law")
    for p, e in [(3, 4), (5, 3)]:
        words = census(p, e)
        n = len(words)
        ok(len(set(words.values())) == n,
           "p=%d e=%d: %d grid words not distinct" % (p, e, n))
        for (bs, d), wv in words.items():
            ok(wv[0] == (-pow(d, -1, p)) % p,
               "p=%d e=%d: w_0 %d != -1/d" % (p, e, wv[0]))
        # beta_r flips: digit r moves by -Delta*w_0^2, prefix fixed
        for (bs, d), wv in words.items():
            w0sq = (wv[0] * wv[0]) % p
            for r in range(1, e):
                for delta in range(1, p):
                    bs2 = bs[:r - 1] + (((bs[r - 1] + delta) % p),) \
                        + bs[r:]
                    wv2 = words[(bs2, d)]
                    ok(wv2[:r] == wv[:r],
                       "p=%d e=%d: beta_%d flip moved the prefix" %
                       (p, e, r))
                    ok((wv2[r] - wv[r]) % p == (-delta * w0sq) % p,
                       "p=%d e=%d: beta_%d diagonal %d != -%d*w0^2" %
                       (p, e, r, (wv2[r] - wv[r]) % p, delta))
            # d second-digit flips: w_e alone, bijectively
            seen = set()
            for t in range(p):
                wv2 = words[(bs, d % p + t * p)]
                ok(wv2[:e] == wv[:e],
                   "p=%d e=%d: d-carry flip moved the prefix" % (p, e))
                seen.add(wv2[e])
            ok(len(seen) == p,
               "p=%d e=%d: w_e not bijective in d's carry digit" % (p, e))
        print("  p=%d e=%d: %d words distinct, every flip unitriangular,"
              " diagonal -w_0^2 exact" % (p, e, n))
    # e = 6 distinctness + sampled flips
    words6 = census(3, 6)
    ok(len(set(words6.values())) == 1458,
       "p=3 e=6: words not distinct")
    rng = random.Random(210)
    keys = rng.sample(sorted(words6), 40)
    for bs, d in keys:
        wv = words6[(bs, d)]
        w0sq = (wv[0] * wv[0]) % 3
        r = rng.randrange(1, 6)
        delta = rng.randrange(1, 3)
        bs2 = bs[:r - 1] + (((bs[r - 1] + delta) % 3),) + bs[r:]
        wv2 = words6[(bs2, d)]
        ok(wv2[:r] == wv[:r] and (wv2[r] - wv[r]) % 3 == (-delta * w0sq) % 3,
           "p=3 e=6: sampled flip fails at beta_%d" % r)
    print("  p=3 e=6: 1458 words distinct, 40 sampled flips unitriangular")


def solve_word(p, e, target, name):
    """Greedy unitriangular solve: grid hitting the target word."""
    d = (-pow(target[0], -1, p)) % p
    if d == 0:
        d = p  # unreachable: target[0] != 0 always
    betas = [0] * (e - 1)
    w0sq_inv = pow(target[0] * target[0], -1, p)
    for r in range(1, e):
        wv = ds.word_of(name, p, grid_eis(p, e, tuple(betas), d), e)
        ok(wv[:r] == list(target[:r]),
           "%s: prefix disturbed at level %d" % (name, r))
        diff = (wv[r] - target[r]) % p
        if diff:
            betas[r - 1] = (betas[r - 1] + diff * w0sq_inv) % p
    # level e: probe the carry digit
    for t in range(p):
        d2 = d + t * p
        wv = ds.word_of(name, p, grid_eis(p, e, tuple(betas), d2), e)
        ok(wv[:e] == list(target[:e]),
           "%s: prefix disturbed at the carry probe" % name)
        if wv[e] == target[e]:
            eis = grid_eis(p, e, tuple(betas), d2)
            ok(ds.word_of(name, p, eis, e) == list(target),
               "%s: final word mismatch" % name)
            return eis
    raise AssertionError("%s: carry digit never hit the target" % name)


# ------------------------------------------------- [S] designed splits


def section_s(rng, tables):
    print("\n[S] SA-C: the designed splits (triangle -> slot laws live)")
    # (1) LAND-15 pair at p=3 e=6
    eisA = solve_word(3, 6, (1, 0, 0, 0, 1, 0, 1), "L15A")
    FA = lc.LF("L15A", 3, [0, 1], eisA, 30)
    ds.climb_row(FA, 1, rng, [12, 15], 15)
    print("  [1,0,0,0,1,0,1] (%s): class-1 visits {12,15}, stick 15 —"
          "\n    landing 15 designed into existence (V_6 = w_3^2 - w_6"
          " != 0)" % poly_name(eisA))
    eisB = solve_word(3, 6, (1, 0, 0, 0, 1, 0, 0), "L15B")
    FB = lc.LF("L15B", 3, [0, 1], eisB, 42)
    ds.climb_row(FB, 1, rng, [12, 16, 17, 18], None)
    print("  [1,0,0,0,1,0,0] (%s): passes 15, climbs to CAP (stick >= %d):"
          "\n    Hensel margin => zeta_9 in it — the field IS Q_3(zeta_9)"
          % (poly_name(eisB), FB.CAP))
    # (2) p=5 e=20 pair
    tgtA = [0] * 21
    tgtA[0], tgtA[5], tgtA[16], tgtA[17] = 1, 1, 1, 2
    eis5A = solve_word(5, 20, tuple(tgtA), "P5A")
    F5A = lc.LF("P5A", 5, [0, 1], eis5A, 52)
    ds.climb_row(F5A, 1, rng, [30, 35, 40, 42], 42)
    print("  p=5 word A (w_5=1, w_16=1, w_17=2): visits {30,35,40,42},"
          " stick 42\n    — the slot-1 law -(w_5 + w_17) at p = 5")
    tgtB = list(tgtA)
    tgtB[17] = 4
    eis5B = solve_word(5, 20, tuple(tgtB), "P5B")
    F5B = lc.LF("P5B", 5, [0, 1], eis5B, 52)
    D5, mt5 = tables[(5, 1, 1)]
    env = {"r": 1}
    for j in range(1, 21):
        env["w%d" % j] = tgtB[j]
    nxt = None
    for r in sorted(D5):
        if r > 17 and peval(5, D5[r], env):
            nxt = r
            break
    ok(nxt is not None, "p=5 B: engine predicts full sail (unexpected)")
    uB, PB = ds.floor_walker(F5B, 1, rng)
    achB, stickB = ds.climb(F5B, uB, 1, PB, F5B.CAP)
    ok(stickB > 42, "p=5 B: stuck at %d, slot-1 hole missed" % stickB)
    ok(stickB == 25 + nxt,
       "p=5 B: stick %d != engine's next forced digit rel %d"
       % (stickB, nxt))
    print("  p=5 word B (w_17=4): slot-1 hole (1+4 == 0), sticks at %d ="
          "\n    the engine's next nonzero forced digit (rel %d: D = %s)"
          % (stickB, nxt, fmt_poly(D5[nxt])))
    # (3) x^18+3 class (1,2): engine forms at the all-zero word
    D18, mt18 = tables[(3, 1, 2)]
    env0 = {"r": 1}
    for j in range(1, 19):
        env0["w%d" % j] = 0
    vals = {r: peval(3, D18[r], env0) for r in sorted(D18) if r >= 9}
    ok(vals.get(10) == 0 and vals.get(11) == 0,
       "x^18+3 (1,2): rels 10,11 not holes: %s" % vals)
    ok(vals.get(12) == 1,
       "x^18+3 (1,2): slot-0 rel 12 not a ceiling: %s" % vals)
    first = min(r for r, v in vals.items() if v)
    ok(first == 12, "x^18+3 (1,2): first forced stop %d != 12" % first)
    print("  x^18+3 class (1,2), all-zero word: holes 10,11 + slot-0"
          " ceiling 12\n    (= censused 37, 38, 39) read off the engine"
          " forms")
    return FB


def poly_name(eis):
    e = len(eis) - 1
    terms = ["x^%d" % e]
    for i in range(e - 1, 0, -1):
        if eis[i]:
            terms.append("%+dx^%d" % (eis[i], i))
    terms.append("%+d" % eis[0])
    return "".join(terms)


# ---------------------------------------------------- [O] the orbit action


def section_o(rng, FB):
    print("\n[O] SA-E: the true orbit action")
    # (1) the twist-depth law at e = 12, class (2,1)
    F = lc.LF("x^12+3x+3", 3, [0, 1], [3, 3] + [0] * 10 + [1], 40)
    for k in range(1, 6):
        for eta in ad.sample_class(F, k, 4, rng):
            inv = tr.unit_inv(F, ds.epow(F, eta, 12))
            v = F.val(ad.esub(F, inv, ad.const_el(F, 1)))
            ok(v == 3 * k, "e=12: v(eta^-12 - 1) = %d != 3k at k=%d"
               % (v, k))
    v6 = set()
    for eta in ad.sample_class(F, 6, 6, rng):
        inv = tr.unit_inv(F, ds.epow(F, eta, 12))
        v6.add(F.val(ad.esub(F, inv, ad.const_el(F, 1))))
    print("  x^12+3x+3: v(eta^-12 - 1) = 3k exactly, k = 1..5 (i* = 6,"
          " i-dagger = 4:\n    the word caps at k > 4, NOT k >= i*);"
          " k = 6 tie case: v in %s" % sorted(v6))
    # (2) the genuine chart-word set of K9
    F9 = lc.LF("K9", 3, [0, 1], [3, 9, 18, 21, 15, 6, 1], 30)
    w, pi = tr.w_element(F9)
    base = tuple(tr.w_digits(F9, w, pi, 7))
    charts = {}
    for t in (1, 2):
        for a1 in range(3):
            for a2 in range(3):
                for a3 in range(3):
                    eta = [list(cc) for cc in F9.one]
                    eta[0][0] = tr.teich(F9, t)
                    if a1:
                        eta[1][0] = (tr.teich(F9, a1) * eta[0][0]) % F9.pM
                    eta_el = tuple(tuple(cc) for cc in eta)
                    for dep, av in ((2, a2), (3, a3)):
                        if av:
                            b = [list(cc) for cc in F9.one]
                            b[dep][0] = tr.teich(F9, av)
                            eta_el = F9.emul(
                                eta_el, tuple(tuple(cc) for cc in b))
                    winv = tr.unit_inv(F9, ds.epow(F9, eta_el, 6))
                    wp = F9.emul(w, winv)
                    pip = F9.emul(eta_el, pi)
                    wd = tuple(tr.w_digits(F9, wp, pip, 7))
                    charts.setdefault(wd, []).append((t, a1, a2, a3))
    ok(base in charts, "K9: base word missing from its own chart set")
    for wd in charts:
        ok(wd[4] == 1 and (wd[3] + wd[5]) % 3 == 0
           and wd[6] == (wd[3] * wd[3]) % 3,
           "K9 chart word %s violates the slot constraints" % (wd,))
    # the orbit IS the constraint variety: 3 solutions of {w_0 = 1,
    # w_1 = w_2 = 0, w_4 = 1, w_5 = -w_3, w_6 = w_3^2}, all realized
    ok(len(charts) == 3,
       "K9 chart set %d != the constraint variety's 3 words"
       % len(charts))
    rec = (1, 0, 0, 1, 1, 1, 0)
    ok(rec not in charts,
       "the section_d(i) vector IS a genuine chart word after all")
    # a3 never matters (the p | r kill at r = 3)
    for wd, etas in charts.items():
        keys = {(t, a1, a2) for t, a1, a2, _ in etas}
        ok(len(etas) == 3 * len(keys),
           "K9: a3 changed a chart word (%s)" % (wd,))
    # the LAND-15-B word lies in the set (B is Q_3(zeta_9))
    wB, piB = tr.w_element(FB)
    wordB = tuple(tr.w_digits(FB, wB, piB, 7))
    ok(wordB in charts,
       "LAND-15-B word %s not a K9 chart word" % (wordB,))
    print("  K9's genuine chart-word set %s\n    (%d words over 54"
          " uniformizer reps), ALL satisfy w_4 = 1, w_3 + w_5 == 0,\n"
          "    w_6 = w_3^2; a3 never moves the word (p | r kill);"
          " the section_d(i)\n    half-pair vector %s is NOT among"
          " them;\n    the LAND-15-B word %s IS (the design is the"
          " anchor, third specimen)"
          % (sorted(list(wd) for wd in charts), len(charts),
             list(rec), list(wordB)))


# ------------------------------------------------------------------- run


def run():
    rng = random.Random(210)
    print("THE SLOT-FORM ALGEBRA — the landing form, slots, triangle,"
          " orbit")
    print("=" * 66)
    tables = section_p()
    section_n(rng)
    section_t()
    FB = section_s(rng, tables)
    section_o(rng, FB)
    print("\nALL GREEN — %d checks this module (+%d imported machinery)"
          % (CHECKS, tr.CHECKS + ds.CHECKS))


if __name__ == "__main__":
    run()
