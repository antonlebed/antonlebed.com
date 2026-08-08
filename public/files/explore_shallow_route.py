"""explore_shallow_route.py — THE SHALLOW-ROUTE GENERAL LAW: which
above-window rels are target-shifted at general (p, c, m), the
shallow term's closed form, and the unit-landable levels at m >= 2
(the slot algebra's last edge).

THE QUESTION. explore_above_window.py charted the above-window
game at (3,1,2) only: pure between rels read -w_r, and TWO rels (28, 29)
are target-shifted by the v_p = 3 shallow family; the climb needed
an enriched pool because pure steps leave 27 + 2e = 63 uncovered.
Generalize all three: the shifted-rel set at (p, c, m), the shallow
term as a closed form, and the pure-step landing spectrum.

THE HAND DERIVATION (fixed before this file existed; every prediction
below is frozen against it).

M1 (THE MASTER REL FORMULA). For a monomial of (1+x)^P - 1 (parts
   (x_l, i_l), A = sum x, W = sum i*x, P = p^{m+1}), with
   j = v_p(A) and kappa = the base-p carry count of adding the
   parts (Kummer):

       rel = e*(m - j + kappa) + c*(A - p^m) + W        [A < P]
       rel = e*kappa + W                                 [A = P]

   [Digit lemma: s_p(P - A) = (m - j)(p-1) + p - s_p(A) for A < P.]
   Forks (j = m), slots (j = m-1), the shallow family (j = 0) are
   the same formula at three j's.
M2 (THE STOREY LADDER + THE DECORATION LAW). kappa = 0 forces every
   part to be a multiple of p^j, so family j lives on the
   p^j-lattice from its onset rel_j = e*(m - j) - c*(p^m - p^j),
   j = m (gate), m-1 (slot floor rel_c), ..., 0. Onsets INCREASE as
   j drops (rel_j - rel_{j+1} = e - c(p-1)p^j > 0). A between rel r
   (t = v_p(r) <= m-2) is reachable only by families j <= t, so:

       r is TARGET-SHIFTED iff r >= rel_t = e(m-t) - c(p^m - p^t),
       PURE (-w_r bare) below.

   At m = 2: pure iff r < rel_0 = 2e - c(p^2 - 1) — (3,1,2)'s
   {28, 29} verbatim, and every between rel >= rel_0 is shifted
   (explore_above_window.py's 'uncharted past 29' answered: none
   pure). At m = 3 there are TWO between classes (t = 0, 1) with
   separate onsets.
M3 (THE SHALLOW PINS, first band, m = 2, regime + gate open). In
   the first band the w-expansion of (-w)^{m+1} contributes [w_0]
   only (Teichmueller digit powers exact; cross terms pay p -> e
   deeper or land 3a >= 3p^m deeper; gamma-digit corrections pay
   e). Passage-conditioned:
     delta-r = 0: monomial ((1,0),), gamma = unit(C(P,1)) = 1:
       D_{rel_0} = -w_{rel_0} + (-1)^{m+1}
       PIN w_{rel_0} = (-1)^{m+1} = p - 1 at m = 2 — a UNIVERSAL
       constant; the j = m-1 instance of the same formula is the
       slot pin w_relc = +1 = w_0^2 (DR3): the storey pins
       ALTERNATE SIGN (-1)^{m+1-j}.
     delta-r = 1 (between iff c < p-1): ((1,1),) [gamma 1] and, at
       c = 1 only, ((2,0),) [gamma = -1/2]; with the fork-1 value
       s_1 = -k_1 - ((p-1)/2)*rho (c = 1; s_1 = -k_1 at c >= 2) the
       rho^2 parts CANCEL exactly at every p, leaving
       D_{rel_0+1} = -w_{rel_0+1} + k_1,   k_1 = w_{p^m}
       PIN w_{rel_0+1} = k_1 — the fork digit returns one storey
       up. K27's measured w_28 = w_29 = 2 are two DIFFERENT
       objects: the constant p - 1 and its own k_1 = w_9 = 2.
M4 (THE LANDING/GAP LAW). One p-power step: psi(k) = min(pk, k+e),
   seat s = e/(p-1). Off-seat the leading unit survives: v(u^P - 1)
   = psi^{m+1}(k) EXACTLY, rigid for the whole class. AT the seat,
   pure Teichmueller y = [a]pi^s: the pi^{ps} coefficient is
   [a]^p - w[a] = [a](1 - w) exactly (Teichmueller Fermat), so
   GATE-OPEN => full cancellation at every p and every a, and the
   step lands past ps reading the word/element digits (the defect
   game — the gate itself is the t = 0 instance: the in-window slot
   game is the deepest storey of the same object). The orbit of k
   hits the seat iff k = c*p^t; hence THE GAP LAW:

       gate-open: NO pure step lands G_t = c*p^{m+1} + t*e,
       t = 1..m (unique psi-preimage chain through the seat, which
       always cancels past); gate-closed: the seat step does NOT
       cancel and the seat orbits land the G_t exactly.

   The G_t stay WALKER-landable through lower-class defect games
   (45 = G_1 at (3,1,2) is the deferral landing; 63 = G_2 is rel
   2e, a fresh rel) — the gap is a property of the pure-step pool,
   which is WHY the m >= 2 climb needs the enriched pool (the gap
   noted in explore_above_window.py). Hybrids
   1 + [a]pi^{c p^m} + [b]pi^{c p^m + j} land G_m + j.

THE PREDICTIONS (fixed before this file existed; a miss falsifies
its lemma):

SR-A (master/decoration): every enumerated monomial at (3,1,2)@33,
   (3,2,2)@58, (3,1,3)@140, (5,1,2)@177 satisfies MASTER; between
   rels split pure/shifted exactly at rel_t; at (3,1,3) the t = 1
   class shifts from 84 and the t = 0 class from 136; onset
   monomials are the predicted singles with the predicted gammas.
SR-B (the onset pin): w-pin at rel_0 = (-1)^{m+1}: K27 w_28 = 2
   (regression); K125 w_176 = 4 (sight-unseen); the (3,2,2)
   designed pass-field (word [1,0^23,1,0^12], sparse grid) sticks
   AT 27 + 56 = 83 with every pure between rel 37..55 a hole.
SR-C (the k_1 pin): pin at rel_0 + 1 = k_1: K27 w_29 = w_9 = 2
   (regression); K125 w_177 = its own w_25 (sight-unseen); the
   (3,1,2) 3x3 grid (k_1 in {0,1,2} via the word, w_29 in {0,1,2}
   via b_11's second digit, w_28 opened to 2 via b_10): stick = 56
   iff w_29 != k_1 (6 cells), stick > 56 on the diagonal (3 cells).
SR-D (landing/gap): off-seat pure steps land psi^{m+1}(k) exactly
   at (3,1,2), (3,2,2), (5,1,2); NO pure step lands any G_t at the
   gate-open fields; seat-orbit pure steps land STRICTLY past
   their G_t; hybrids 1+[a]pi^{cp^m}+[b]pi^{cp^m+j} land G_m + j on
   cue; at gate-CLOSED x^18-3 the seat orbits land G_1 = 45
   (k = 3) and G_2 = 63 (k = 9) EXACTLY; the frozen
   explore_above_window.py line '30 (k = 3, seat tie)' at gate-open
   (3,1,2) is falsified —
   k = 3 lands >= 54 (v(u^9-1) >= 36 after the tie, + e rigid).
SR-E (null controls): the minimal-representative designs (sparse
   grids) leave every pure between digit zero on cue.

THE DESIGN. Machinery imported whole: enumeration (tr.sp/sigma_vp
pattern, generalized part cap), fields (lc.LF), words (ds.word_of),
designs (sa.solve_word), climbs (aw.step_pool/lean_climb + a local
class-c census + mate powers so one mate per level suffices at
every coefficient). Enumeration completeness is RIGOROUS per scope
via the n-part lower bound rel_lb(n) = min_A [e*v_min(A,n) + cA] +
n(n-1)/2 - p*i* (W >= n(n-1)/2 always; Sigma s >= max(n, s_p(A))
congruent to s_p(A) mod p-1): the part cap is the largest n with
rel_lb(n) <= relmax, and every larger n is asserted cleared. The
deep onsets the brute budget cannot reach ((3,1,3)@140,
(5,1,2)@177) are covered DERIVED: the clearance loop asserts every
family class (j, kappa) except (t, 0) opens strictly above rel_t,
using the mini-lemma anchored by the brute scopes. Labels never
read orbits; the engine only ever reads measured digits.
Run: python prime/code/explore_shallow_route.py

FINDINGS (entered post-run, copied from printed output).

1. THE MASTER REL FORMULA + THE STOREY LADDER (the digit lemma is
   exact algebra; monomial-exhaustive at (3,1,2)@rel 33,
   (3,2,2)@58, (3,1,3)@85 — 94 + 113 + 37 monomials, every one
   satisfying rel = e(m - j + kappa) + c(A - p^m) + W on both the
   digit-lemma and sigma routes): the window game's monomials
   organize by j = v_p(A) into STOREYS with onsets rel_j =
   e(m - j) - c(p^m - p^j) — the gate (j = m), the slot floor
   rel_c (j = m-1), and below them m - 1 shallow families, onsets
   RISING as j drops. The kappa-carry mini-lemma (kappa carries
   bridge kappa digit positions, so parts == 0 mod p^{j - kappa})
   holds at every censused monomial.

2. THE DECORATION LAW (rule — brute at the three p = 3 scopes,
   derived via clearance + mini-lemma at (3,1,3)@140 and
   (5,1,2)@177): a between rel r (t = v_p(r) <= m - 2) is
   target-shifted iff r >= rel_t, pure (-w_r bare) below. At m = 2:
   pure iff r < rel_0 = 2e - c(p^2 - 1) — (3,1,2)'s {28, 29}
   verbatim, then {31, 32, ...}: NOTHING past the onset is pure
   (explore_above_window.py's 'uncharted past 29' closed). Shifted
   between rels in range: (3,1,2) {28, 29, 31, 32}; (3,2,2) {56, 58} (57 is
   on-lattice); (3,1,3) t = 1 opens at 84, t = 0 at 136 — TWO
   between classes, two onsets (the m = 3 storey structure live).

3. THE SHALLOW PINS (rule in range; the hand derivation general in
   (p, c, m) at delta-r = 0 and in (p, c) at m = 2 for
   delta-r = 1): passage-conditioned, D_{rel_0} = -w_{rel_0} +
   (-1)^{m+1} and D_{rel_0+1} = -w_{rel_0+1} + k_1 (the rho^2
   parts cancel through the fork-1 value at every p, c = 1 and
   c >= 2 alike). PINS: w_{rel_0} = (-1)^{m+1} — a universal
   constant, the storey-alternating twin of the slot pin w_0^2 —
   and w_{rel_0+1} = k_1: THE FORK DIGIT RETURNS ONE STOREY UP.
   GENERALIZED (explore_telescope.py): at general m the
   delta-r = 1 pin is (-1)^m * k_1 (+k_1 at m = 2 verbatim), the
   return repeating at every storey with alternating sign.
   Verified: K27 w_28 = 2 = p - 1, w_29 = 2 = its w_9 (regression
   — explore_above_window.py's 'w_28 = w_29 = 2' split into two
   different objects);
   K125 SIGHT-UNSEEN w_176 = 4 = p - 1, w_177 = 3 = its own
   w_25 = 3; the (3,1,2) 3x3 grid: stick = 56 iff w_29 != k_1 at
   all nine (k_1, w_29) cells (diagonal sticks 59/58/58); the
   (3,2,2) designed pass-field x^36+6x^24-24 sticks at 110 =
   p*i* + 56 with every pure between rel 37..55 a hole (c = 2,
   class-2 census landings [63, 72, 81, 93, 96, 99, 108]).

4. THE LANDING/GAP LAW (rule at K27, x^36+3, K125 + the closed
   control): off-seat pure steps land psi^{m+1}(k) EXACTLY
   (psi(k) = min(pk, k + e)); at the seat the pi^{ps} coefficient
   is [a]^p - w[a] = [a](1 - w) exactly (Teichmueller Fermat), so
   the gate digit keys the spectrum: GATE-OPEN, no pure step lands
   any gap G_t = c*p^{m+1} + t*e (t = 1..m) — seat orbits land
   past them ((3,1,2) k=3 -> {54, 73}, k=9 -> {72, 75}; (3,2,2)
   k=6 -> 108, k=18 -> >126; (5,1,2) k=5 -> {250, >=346}) — while
   GATE-CLOSED x^18-3 lands them exactly (k=3 -> 45 = G_1, k=9 ->
   63 = G_2). Hybrids 1+[a]pi^9+[b]pi^{9+j} land 63 + j (j = 1..8):
   the gap is exactly the pure point; the G_t stay walker-reachable
   through lower-storey defect games (45 = the deferral landing,
   MEASURED at explore_above_window.py's broken-deferral field; 63 =
   rel 2e on the fresh lattice, reachable by inference, not
   measured) — and walker levels != pure-step levels is WHY the
   m >= 2 climb needs the enriched pool (noted in
   explore_above_window.py), now explained. The class-c game itself
   is the t = 0 seat game: gate cancellation = the seat tie of the
   walker orbit — window game, pins, and gaps are one psi-orbit
   object read at successive storeys. COROLLARY: the frozen
   explore_above_window.py line '30 (k = 3, seat tie)' is FALSIFIED
   — k = 3 at gate-open (3,1,2) lands {54, 73}, never 30 (the pool
   built on measured v was never affected; the hand line was a
   derivation note error).

PRE-GREEN FAILURES (adjudicated during development):
(1) Runs 1-3: engine scaffolding — rel_lb crashed on n > P (no
    n-part monomial exists; now returns +inf) and vp(0) looped
    forever on the gate monomials (rel 0) in the between-filter;
    plus the (5,1,2)@177 FULL brute enumeration was unaffordable
    (W-budget ~600 with weak sigma pruning): [M] restructured to
    brute-at-p=3 + derived clearance. No assert was wrong.
(2) Run 4 (SLATE MISS, SR-B): the frozen '(3,2,2) stick 83 =
    27 + rel_0' transplanted the c = 1 coincidence p*i* = P — the
    class-(c,m) landing offset is p*i* = c*p^{m+1} = 54. The pin
    rel_0 = 56 itself was right; corrected stick 110 = 54 + 56,
    measured on cue. Same run exposed two harness slips: the first
    observed stick '102' was this file's own cap=100 truncating the
    climb, and aw.census hardcodes class 1 (the (3,2,2) census read
    {27: 400} = the class-1 rigid psi^3(1) = 27, not the walkers)
    — replaced by the local class-c census.

RUN RECORD (python prime/code/explore_shallow_route.py, ~20 s,
exit 0): 1059 checks this module (1058 at this file's first run; +1
= a later run's onset_content fix, the added A-step master-check) +
4951 through the imported machinery. Printed rows as copied: [M]
(3,1,2) cap 4, 94 monomials,
shifted between {28, 29, 31, 32}; (3,2,2) cap 3, 113, {56, 58};
(3,1,3) cap 3, 37, t=1 onset 84; derived (3,1,3) 136/137 +
(5,1,2) 176/177 content {((1,0),)} / {((1,1),), ((2,0),)}.
[P] K27 w_28 = 2, w_29 = 2 = w_9; K125 w_176 = 4, w_177 = 3 =
w_25; 3x3 sticks 59/56/56/56/58/56/56/56/58; P322 stick 110,
landings [63, 72, 81, 93, 96, 99, 108]. [U] K27 gaps {45, 63}
unhit, k=3 {54, 73}, k=9 {72, 75}, hybrids 63+j; x^36+3 gaps
{90, 126} unhit, k=6 108, k=18 141(cap); K125 gaps {225, 325}
unhit, k=5 {250, 346(cap)}; x^18-3 closed: 45/63 exact.
"""

import random
import time
from math import comb

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_tame_readout as tr
import explore_deep_spectrum as ds
import explore_slot_algebra as sa
import explore_above_window as aw

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def sp(x, p):
    s = 0
    while x:
        s += x % p
        x //= p
    return s


def vp(x, p):
    if x == 0:
        return 10 ** 9
    v = 0
    while x % p == 0:
        v += 1
        x //= p
    return v


# ------------------------------------------------ the master formula


def master_rel(p, c, m, mono):
    """rel via the digit lemma (M1) — independent of the sigma route."""
    P, pm = p ** (m + 1), p ** m
    e = c * (p - 1) * pm
    A = sum(x for x, i in mono)
    W = sum(x * i for x, i in mono)
    kap = (sum(sp(x, p) for x, i in mono) - sp(A, p)) // (p - 1)
    if A == P:
        return e * kap + W
    j = vp(A, p)
    return e * (m - j + kap) + c * (A - pm) + W


def sigma_rel(p, c, m, mono):
    """rel via the sigma route (the enumerate_window bookkeeping)."""
    P, istar = p ** (m + 1), c * p ** m
    e = c * (p - 1) * p ** m
    A = sum(x for x, i in mono)
    W = sum(x * i for x, i in mono)
    sig = sp(P - A, p) + sum(sp(x, p) for x, i in mono)
    return e * ((sig - 1) // (p - 1)) + c * A + W - p * istar


def gamma_unit(p, m, mono):
    """Unit part mod p of the monomial's multinomial coefficient."""
    P = p ** (m + 1)
    A = sum(x for x, i in mono)
    M = 1
    rem = P
    for x, i in mono:
        M *= comb(rem, x)
        rem -= x
    return (M // p ** vp(M, p)) % p


# ------------------------------- the capped enumeration + completeness


def enum_cap(p, c, m, relmax, rmax):
    """enumerate_window generalized to rmax parts."""
    n = p ** (m + 1)
    istar = c * p ** m
    e = c * (p - 1) * p ** m
    lammax = p * istar + relmax
    imax = lammax - c
    found = {}

    def rec(i, parts, A, W, spsum):
        if len(parts) == rmax or i > imax:
            return
        rec(i + 1, parts, A, W, spsum)
        for x in range(1, n - A + 1):
            if c * (A + x) + W + i * x > lammax:
                break
            lb = spsum + sp(x, p)
            if A + x < n:
                lb += 1
            if e * ((lb - 1) // (p - 1)) + c * (A + x) + W + i * x > lammax:
                continue
            parts.append((x, i))
            lam = (e * tr.sigma_vp(n, [xx for xx, _ in parts], p)
                   + c * (A + x) + W + i * x)
            rel = lam - p * istar
            if 0 <= rel <= relmax:
                found.setdefault(rel, []).append(tuple(sorted(parts)))
            rec(i + 1, parts, A + x, W + i * x, spsum + sp(x, p))
            parts.pop()

    rec(0, [], 0, 0, 0)
    return found


def rel_lb(p, c, m, n):
    """Rigorous lower bound on rel over ALL n-part monomials:
    W >= n(n-1)/2 (n distinct indices); Sigma s_p(parts) >=
    max(n, s_p(A)), congruent to s_p(A) mod p-1."""
    P, pm = p ** (m + 1), p ** m
    e, istar = c * (p - 1) * pm, c * pm
    if n > P:
        return 10 ** 9          # no n-part monomial exists at all
    best = None
    for A in range(n, P + 1):
        sA = sp(A, p) if A < P else 1
        ssum = max(n, sA)
        ssum += (sA - ssum) % (p - 1)
        spa = sp(P - A, p) if A < P else 0
        v = (spa + ssum - 1) // (p - 1)
        val = e * v + c * A
        if best is None or val < best:
            best = val
    return best + n * (n - 1) // 2 - p * istar


def scope_census(p, c, m, relmax):
    """Complete census to relmax: cap chosen by rel_lb, larger part
    counts asserted cleared (monotone tail)."""
    cap = 1
    while rel_lb(p, c, m, cap + 1) <= relmax:
        cap += 1
    for n in range(cap + 2, p ** (m + 1) + 1):   # all n <= P; n > P
        cur = rel_lb(p, c, m, n)                 # has no monomial
        ok(cur > relmax, "(%d,%d,%d): lb(%d) = %d <= relmax" %
           (p, c, m, n, cur))
    return enum_cap(p, c, m, relmax, cap), cap


def clearance(p, c, m, rmax):
    """Derived decoration completeness (master + the parts-lattice
    mini-lemma, brute-anchored below): a family class (j, kappa)
    has parts == 0 mod p^{j-kappa} (kappa carries bridge kappa digit
    positions), so it can decorate a between rel of depth t =
    v_p(rel) only if j - kappa <= t; its minimal rel is
    e(m - j + kappa) - c(p^m - p^j). Assert every eligible class
    except (t, 0) opens strictly above rel_t, for every t and every
    kappa in range — the onset at rel_t is exactly the kappa = 0,
    j = t family."""
    pm = p ** m
    e = c * (p - 1) * pm
    kmax = rmax // e + 2
    for t in range(m - 1):
        relt = e * (m - t) - c * (pm - p ** t)
        for j in range(m + 1):
            for kap in range(kmax + 1):
                if (j, kap) == (t, 0) or max(0, j - kap) > t:
                    continue
                minrel = e * (m - j + kap) - c * (pm - p ** j)
                ok(minrel > relt,
                   "(%d,%d,%d): class (j=%d,k=%d) opens at %d <= "
                   "rel_%d = %d" % (p, c, m, j, kap, minrel, t, relt))
        for kap in range(kmax + 2):        # A = P: v(rel) >= m+1-kap
            if m + 1 - kap > t:
                continue
            ok(e * kap > relt,
               "(%d,%d,%d): A=P class k=%d opens at %d <= rel_%d"
               % (p, c, m, kap, e * kap, t))


def onset_content(p, c, m, t):
    """The onset + next-lattice-rel (relt + p^t) monomials of family
    t, constructed (A + W walk, kappa = 0), master-checked."""
    pm = p ** m
    e = c * (p - 1) * pm
    relt = e * (m - t) - c * (pm - p ** t)
    out = {relt: [((p ** t, 0),)]}
    nxt = [((p ** t, 1),)]         # the W-step, every c
    if c == 1:                     # the A-step lands on the same rel
        nxt.append(((2 * p ** t, 0),))
    out[relt + p ** t] = nxt
    for r, monos in out.items():
        for mo in monos:
            ok(master_rel(p, c, m, mo) == r,
               "(%d,%d,%d): onset content %s not at rel %d"
               % (p, c, m, mo, r))
    return relt, out


def section_m():
    print("\n[M] the master formula, the storey ladder, the decoration"
          " law")
    scopes = [(3, 1, 2, 33), (3, 2, 2, 58), (3, 1, 3, 85)]
    for p, c, m, relmax in scopes:
        t0 = time.time()
        pm, pm1 = p ** m, p ** (m - 1)
        e = c * (p - 1) * pm
        w, cap = scope_census(p, c, m, relmax)
        nmono = sum(len(v) for v in w.values())
        # M1: master == sigma route, per monomial; and the
        # parts-lattice mini-lemma (kappa carries bridge kappa digit
        # positions: parts == 0 mod p^{j - kappa}) — the anchor of
        # the derived clearance below
        for r, monos in w.items():
            for mo in monos:
                ok(master_rel(p, c, m, mo) == r
                   and sigma_rel(p, c, m, mo) == r,
                   "(%d,%d,%d): MASTER fails at %s (rel %d)" %
                   (p, c, m, mo, r))
                A = sum(x for x, i in mo)
                kap = (sum(sp(x, p) for x, i in mo) - sp(A, p)) \
                    // (p - 1)
                j = (m + 1) if A == p ** (m + 1) else vp(A, p)
                lat = p ** max(0, j - kap)
                ok(all(x % lat == 0 for x, i in mo),
                   "(%d,%d,%d): mini-lemma fails at %s (j=%d k=%d)"
                   % (p, c, m, mo, j, kap))
        # M2: the decoration law at every between rel in range
        onsets = {t: e * (m - t) - c * (pm - p ** t) for t in range(m - 1)}
        for r in range(1, relmax + 1):
            t = vp(r, p)
            if t >= m - 1:
                continue          # fork/slot/fresh lattice
            if r >= onsets[t]:
                ok(r in w, "(%d,%d,%d): shifted rel %d (t=%d) has no"
                   " monomial" % (p, c, m, r, t))
            else:
                ok(r not in w, "(%d,%d,%d): pure rel %d (t=%d) carries"
                   " %s" % (p, c, m, r, t, w.get(r)))
        # onset monomials + gammas
        for t, r0 in onsets.items():
            if r0 <= relmax:
                ok(sorted(w[r0]) == [((p ** t, 0),)],
                   "(%d,%d,%d): onset %d list %s" % (p, c, m, r0, w[r0]))
                ok(gamma_unit(p, m, ((p ** t, 0),)) == 1,
                   "(%d,%d,%d): onset gamma != 1" % (p, c, m))
        # the delta-r = 1 monomials one past the t = 0 onset
        r0 = onsets.get(0)
        if r0 is not None and c == 1 and r0 + 1 <= relmax:
            want = sorted([((1, 1),), ((2, 0),)])
            ok(sorted(w[r0 + 1]) == want,
               "(%d,%d,%d): rel_0+1 list %s" % (p, c, m, w[r0 + 1]))
            g2 = gamma_unit(p, m, ((2, 0),))
            ok(g2 == ((p ** (m + 1) - 1) * pow(2, -1, p)) % p,
               "(%d,%d,%d): gamma((2,0)) = %d" % (p, c, m, g2))
        between = sorted(r for r in w
                         if vp(r, p) < m - 1 and r > e)
        print("  (%d,%d,%d) e=%-3d cap=%d: %d monomials <= rel %d;"
              " onsets %s;\n    shifted between rels above e: %s"
              "  [%.1fs]"
              % (p, c, m, e, cap, nmono, relmax,
                 {t: r for t, r in sorted(onsets.items(), reverse=True)},
                 between, time.time() - t0))
    # derived scopes: the deep onsets the brute budget cannot reach
    for p, c, m, rmax, t in [(3, 1, 3, 140, 0), (5, 1, 2, 177, 0)]:
        clearance(p, c, m, rmax)
        relt, content = onset_content(p, c, m, t)
        print("  (%d,%d,%d) DERIVED (clearance + mini-lemma): t=%d"
              " onset rel %d,\n    content %s"
              % (p, c, m, t, relt,
                 {r: v for r, v in sorted(content.items())}))
    # (3,1,3) t = 1: the middle storey, constructive singles
    relt1, content1 = onset_content(3, 1, 3, 1)
    ok(relt1 == 84, "(3,1,3): t=1 onset %d != 84" % relt1)
    print("  (3,1,3) t=1 onset rel 84 (storey ladder: 84 then 136 —"
          " two between\n    classes, two onsets)")


# ------------------------------------------------------- [P] the pins


def deep_word(name, p, eis, depth):
    return ds.word_of(name, p, eis, depth)


def knob(p, eis, pos, rel, target, depth, name):
    """Walk b_pos's second digit until word[rel] == target, prefix
    frozen."""
    base = deep_word(name, p, eis, depth)
    for t in range(p):
        trial = list(eis)
        trial[pos] += p * p * t
        wv = deep_word(name + "k", p, trial, depth)
        ok(wv[:rel] == base[:rel],
           "%s: knob at b_%d moved the prefix" % (name, pos))
        if wv[rel] == target:
            return trial, wv
    raise AssertionError("%s: knob b_%d never hit %d at rel %d"
                         % (name, pos, target, rel))


def census_c(F, c, P, rng, n):
    """Class-c landing multiset + walkers (aw.census hardcodes
    class 1)."""
    lands, mates = {}, []
    for u in ad.sample_class(F, c, n, rng):
        v = ds.land(F, u, P)
        lands[v] = lands.get(v, 0) + 1
        mates.append(u)
    return lands, mates


def climb_c(F, c, P, rng, mates, cap=None):
    """Class-c lean climb with mate POWERS in the pool (one mate per
    level then suffices at every leading coefficient)."""
    if cap is None:
        cap = F.CAP
    u, Pf = ds.floor_walker(F, c, rng)
    ok(Pf == P, "%s: class-%d exponent %d != %d" % (F.name, c, Pf, P))
    mpow = []
    for s0 in mates:
        s = s0
        for _ in range(F.p - 1):
            mpow.append(s)
            s = F.emul(s, s0)
    pool = aw.step_pool(F, c, P, mates=mpow)
    return aw.lean_climb(F, u, c, P, cap, pool)


def section_p(rng):
    print("\n[P] the shallow pins: the (-1)^{m+1} constant and the"
          " returning fork digit")
    # K27 regression (the anchor's pinned digits, measured in
    # explore_above_window.py)
    eis27 = aw.phi27_shift()
    w27 = deep_word("K27", 3, eis27, 29)
    ok(w27[28] == 2, "K27: w_28 = %d != 2 = (-1)^3" % w27[28])
    ok(w27[29] == w27[9], "K27: w_29 = %d != k_1 = %d"
       % (w27[29], w27[9]))
    print("  K27: w_28 = %d = p - 1, w_29 = %d = its own k_1 = w_9"
          " (regression)" % (w27[28], w27[29]))
    # K125 sight-unseen: Phi_125(x+1), pins at rel_0 = 176, 177
    eis125 = [sum(comb(25 * t, j) for t in range(5)) for j in range(101)]
    ok(eis125[100] == 1 and eis125[0] == 5, "Phi125 shift malformed")
    for j in range(100):
        ok(eis125[j] % 5 == 0, "Phi125(x+1) not Eisenstein at %d" % j)
    wK = deep_word("K125", 5, eis125, 177)
    ok(wK[0] == 1 and all(wK[j] == 0 for j in range(1, 25)),
       "K125 gate/regime: %s" % wK[:26])
    ok(wK[176] == 4, "K125: w_176 = %d != 4 = (-1)^3 mod 5" % wK[176])
    ok(wK[177] == wK[25], "K125: w_177 = %d != k_1 = %d"
       % (wK[177], wK[25]))
    print("  K125 (e = 100, rel_0 = 176, SIGHT-UNSEEN): w_176 = %d ="
          " p - 1,\n    w_177 = %d = its own k_1 = w_25 = %d"
          % (wK[176], wK[177], wK[25]))
    # the (3,1,2) 3x3 grid: k_1 x w_29
    print("  the (3,1,2) 3x3 grid (stick = 56 iff w_29 != k_1):")
    for k1 in range(3):
        word = [1] + [0] * 8 + [k1, 0, 0, 1, 0, 0, (-k1) % 3, 0, 0,
                                (k1 * k1) % 3]
        eisB = sa.solve_word(3, 18, tuple(word), "G%d" % k1)
        eisB, wv = knob(3, eisB, 10, 28, 2, 29, "G%d" % k1)
        for w29 in range(3):
            eisC, wv = knob(3, eisB, 11, 29, w29, 29, "G%dw%d"
                            % (k1, w29))
            ok(wv[:28] == deep_word("G%d" % k1, 3, eisB, 29)[:28],
               "grid cell (%d,%d): prefix moved" % (k1, w29))
            FC = lc.LF("G%dw%d" % (k1, w29), 3, [0, 1], eisC, 66)
            lands, mates = aw.census(FC, rng, n=80)
            uC, stick = climb_c(FC, 1, 27, rng, mates, cap=60)
            if w29 != k1:
                ok(stick == 56, "cell k1=%d w29=%d: stick %d != 56"
                   % (k1, w29, stick))
            else:
                ok(stick > 56, "cell k1=%d w29=%d: stick %d <= 56"
                   % (k1, w29, stick))
            print("    k_1=%d w_29=%d: stick %d%s" %
                  (k1, w29, stick, "  (hole: w_29 = k_1)"
                   if w29 == k1 else ""))
    # the (3,2,2) designed pass-field: the c = 2 onset stick.
    # [SLATE MISS, run 4: SR-B froze 'stick 83 = 27 + rel_0' — but the
    #  class-(2,2) landing offset is p*i* = 54, not P = 27 (their
    #  equality at c = 1 was a coincidence the slate transplanted):
    #  the pin itself stands, the stick is 54 + 56 = 110.]
    tgt = [1] + [0] * 23 + [1] + [0] * 12
    eisP = sa.solve_word(3, 36, tuple(tgt), "P322")
    wv = deep_word("P322", 3, eisP, 56)
    ok(wv[:37] == tgt, "P322: word %s != target" % wv[:37])
    ok(all(wv[r] == 0 for r in range(37, 56) if r % 3 != 0),
       "P322: pure between digits nonzero: %s" % wv[37:56])
    FP = lc.LF("P322", 3, [0, 1], eisP, 130)
    lands, mates = census_c(FP, 2, 27, rng, n=400)
    uP, stick = climb_c(FP, 2, 27, rng, mates, cap=118)
    ok(stick == 110, "P322: stick %d != 110 = 54 + rel_0(3,2,2)"
       % stick)
    ok(all(v <= stick for v in lands),
       "P322: landing beyond the stick: %s" % sorted(lands))
    print("  (3,2,2) designed pass-field %s:\n    pure betweens 37..55"
          " all holes (sparse grid), class-2 census landings\n    %s,"
          " stick %d = 54 + 56 = p*i* + the c = 2 shallow ONSET\n"
          "    (w_56 = 0 != 2; the slate's 83 was the c = 1"
          " offset transplanted)"
          % (sa.poly_name(eisP), sorted(lands), stick))


# ----------------------------------------------- [U] the landing law


def psi_orbit(k, p, m, e):
    v = k
    for _ in range(m + 1):
        v = min(p * v, v + e)
    return v


def pure_step(F, k, a):
    s = [list(cc) for cc in F.one]
    i, j = divmod(k, F.e)
    s[j][0] = (s[j][0] + tr.teich(F, a) * (F.p ** i)) % F.pM
    return tuple(tuple(cc) for cc in s)


def pure_map(F, P, ks):
    out = {}
    one = ad.const_el(F, 1)
    for k in ks:
        for a in range(1, F.p):
            s = pure_step(F, k, a)
            v = F.val(ad.esub(F, ds.epow(F, s, P), one))
            out.setdefault(k, {})[a] = v
    return out


def section_u(rng):
    print("\n[U] the landing/gap law: psi off-seat, the gate-keyed"
          " seat gaps")
    runs = [
        ("K27 (open)", lc.LF("K27u", 3, [0, 1], aw.phi27_shift(), 108),
         3, 1, 2, 27, range(3, 13)),
        ("x^36+3 (open)", lc.LF("x36", 3, [0, 1],
                                [3] + [0] * 35 + [1], 140),
         3, 2, 2, 27, [3, 4, 5, 6, 7, 8, 9, 10, 18]),
        ("K125 (open)", None, 5, 1, 2, 125, [2, 3, 4, 5, 6, 7, 25, 26]),
    ]
    for name, F, p, c, m, P, ks in runs:
        if F is None:
            eis125 = [sum(comb(25 * t, j) for t in range(5))
                      for j in range(101)]
            F = lc.LF("K125u", 5, [0, 1], eis125, 345)
        e, seat = c * (p - 1) * p ** m, c * p ** m
        gaps = {t: c * p ** (m + 1) + t * e for t in range(1, m + 1)}
        seatks = {c * p ** t for t in range(1, m + 1)}
        mp = pure_map(F, P, ks)
        hit = set()
        for k, row in mp.items():
            for a, v in row.items():
                hit.add(v)
                if k in seatks:
                    t = vp(k // c, p)
                    ok(v > gaps[t], "%s: seat k=%d lands %d, not past"
                       " G_%d = %d" % (name, k, v, t, gaps[t]))
                else:
                    ok(v == psi_orbit(k, p, m, e),
                       "%s: k=%d a=%d lands %d != psi = %d"
                       % (name, k, a, v, psi_orbit(k, p, m, e)))
        ok(not (hit & set(gaps.values())),
           "%s: a pure step landed a gap: %s" %
           (name, hit & set(gaps.values())))
        seatrow = {k: sorted(set(mp[k].values()))
                   for k in sorted(seatks & set(ks))}
        print("  %-14s seat %d, gaps %s unhit; off-seat = psi^%d"
              " exact;\n    seat orbits land %s" %
              (name, seat, sorted(gaps.values()), m + 1, seatrow))
        if name.startswith("K27"):
            # the explore_above_window.py '30 (k = 3)' line adjudicated
            ok(all(v >= 54 for v in mp[3].values()),
               "K27: k=3 lands %s, below 54" % mp[3])
            print("    k = 3 lands %s (>= 54: the frozen"
                  " explore_above_window.py '30' was a hand error)"
                  % sorted(set(mp[3].values())))
            # hybrids fill G_2 + j
            one = ad.const_el(F, 1)
            for j in range(1, 9):
                s = [list(cc) for cc in F.one]
                i1, j1 = divmod(9, F.e)
                s[j1][0] = (s[j1][0] + tr.teich(F, 1) * (F.p ** i1)) \
                    % F.pM
                i2, j2 = divmod(9 + j, F.e)
                s[j2][0] = (s[j2][0] + tr.teich(F, 1) * (F.p ** i2)) \
                    % F.pM
                v = F.val(ad.esub(F, ds.epow(
                    F, tuple(tuple(cc) for cc in s), 27), one))
                ok(v == 63 + j, "K27 hybrid j=%d lands %d != %d"
                   % (j, v, 63 + j))
            print("    hybrids 1+[1]pi^9+[1]pi^{9+j} land 63 + j,"
                  " j = 1..8 — the gap is\n    exactly the pure point")
    # the gate-closed control: x^18 - 3 (w_0 = 2)
    Fc = lc.LF("x18-3", 3, [0, 1], [-3] + [0] * 17 + [1], 80)
    wd = deep_word("x18-3", 3, [-3] + [0] * 17 + [1], 1)
    ok(wd[0] == 2, "x^18-3: gate %d != closed" % wd[0])
    mp = pure_map(Fc, 27, [3, 9])
    ok(set(mp[3].values()) == {45}, "closed: k=3 lands %s != {45}"
       % mp[3])
    ok(set(mp[9].values()) == {63}, "closed: k=9 lands %s != {63}"
       % mp[9])
    print("  x^18-3 (gate CLOSED, w_0 = 2): k = 3 -> 45 = G_1, k = 9"
          " -> 63 = G_2\n    EXACTLY — the seat cancellation, and the"
          " gaps, are keyed to the gate")


# ---------------------------------------------------------------- main


def main():
    rng = random.Random(215)
    print("THE SHALLOW-ROUTE GENERAL LAW — the storey ladder, the"
          " pins, the gaps")
    print("=" * 68)
    section_m()
    section_p(rng)
    section_u(rng)
    imported = (lc.CHECKS + ad.CHECKS + tr.CHECKS + ds.CHECKS
                + sa.CHECKS + aw.CHECKS)
    print("\n%d checks this module + %d through the imported machinery"
          % (CHECKS, imported))


if __name__ == "__main__":
    main()
