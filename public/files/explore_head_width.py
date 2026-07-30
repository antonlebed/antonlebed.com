r"""explore_head_width.py — the tick ladder's head is the breathing clock's
splice, and the two corners of the corpus disagree about where it is.

THE QUESTION. A place's tick ladder is a HEAD and then a periodic GAP.
explore_tick_pump.py F1 files WHERE a head sits — at the places with
p - 1 <= e, at 90 of 90 — and explore_gaussian_runaway.py F3 files that
the WIDTH is open, with the obvious closed form (excess = e*a, for p^a
the order of the local p-power torsion) already dead: it fits both mu_2
places and runs HIGH at Z[i], predicting 4 against a measured 3. This
asks for the width itself, from the local unit filtration alone.

THE OBJECT, and the index convention re-derived from the engine before
anything was frozen. lambda(P^n) is the exponent of (O/P^n)^*,
which is lcm(q - 1, p^m) for q = p^f the residue cardinality. Define the
LEVEL SEQUENCE

    M(m) := max{ n : U_1^(p^m) subset U_n },     U_i = 1 + P^i.

Then m(n) = min{ m : M(m) >= n }, so the RUNS of constant lambda are
exactly the successive differences M(m) - M(m-1), the tail runs are the
filed gap e, and the filed observable — EXCESS = longest run minus e —
is a statement about one difference of M. Read off the brute-forced
tables already in the corpus:

    Z[w] P2.0 (p2 e1 f1)  lambda 1,2,2,4,8,...      M = 1,3,4,5,...
    K5   R2   (p2 e2 f1)  lambda 1,2,4,4,4,4,8,8    M = 1,2,6,8,...
    Z[i]  R2  (p2 e2 f1)  lambda 1,2,4,4,4,4,4,8,8  M = 1,2,7,9,...

THE DERIVATION, on paper before this file existed. IT IS WRONG AT (ii)
AND IS KEPT ONLY AS THE QUESTION THIS FILE SET OUT WITH — the corrected
law is F1-F2 below, and F4 says which half broke and why. Write e0 = e/(p-1),
and let p^a be the order of mu_(p^inf)(K_P). M has TWO regimes and the
head is the SEAM between them.

  (i) BELOW e0 the p-th power map MULTIPLIES the level: for x of level
      i, p*(x-1) has level i + e and (x-1)^p has level p*i, and p*i is
      the smaller exactly when i < e0. So M(m) = p^m while p^m <= e0.
      Torsion never beats this: mu_(p^a) subset K_P forces
      p^(a-1)*(p-1) | e, hence p^(a-1) <= e0, so the deepest torsion a
      p^m-th power can leave sits at level e0/p^(a-m-1) >= p^m.

  (ii) ONCE the level passes e0 the map is the isomorphism
      U_i -> U_(i+e), so U_1^(p^m) is squeezed between two congruence
      subgroups and its level follows from an INDEX COUNT alone.
      U_1 = mu_(p^a) x Z_p^d with d = ef, so [U_1 : U_1^(p^m)] =
      p^(a + m*e*f) for m >= a, while [U_1 : U_j] = q^(j-1) =
      p^(f*(j-1)). The squeeze f*(M-1) <= a + m*e*f < f*M gives

          M(m) = m*e + floor(a/f) + 1.

      (This regime also DERIVES the filed tail gap: consecutive M differ
      by e, which the corpus has only ever measured.)

Let t := floor(log_p(e0)). Regime (i) runs to m = t and regime (ii) from
m = t+1 — consistently, since p^(a-1) <= e0 gives a <= t+1, which is
what puts the seam at or after the last torsion-limited step. The seam
run is M(t+1) - M(t), so

    EXCESS = 1 + floor(a/f) + t*e - p^t,   t = floor(log_p(e/(p-1))),

clamped at 0. The dead candidate is subsumed: e*a agrees only where t=1,
f=1 and a happens to track the seam, which is why it fitted the two mu_2
places and ran high at the one place with a > 1.

WHAT MAKES THIS WORTH A RIG RATHER THAN A PARAGRAPH: the closed form's
own POSITIVITY CONDITION is a criterion for where a head is, and it is
NOT the filed one. They agree on every place the corpus has measured
because every ring in it is quadratic — e <= 2 — and none of them has 2
inert: the 90 places are 82 split, 5 inert and 3 ramified, and the 5
inert places are over odd primes. Two divergences were frozen as PR3 and
PR5; the run found eight.

TWO TRANSPLANTS, flagged before the run. (T1) The whole derivation is
written in the LOCAL field's vocabulary while the observable is the
GLOBAL engine's lambda column; the bridge is O/P^n = O_P/P^n, which is
assumed and not re-proved. (T2) Regime (i) is exercised beyond m=0 by
exactly two filed places, both at t=1 and both at p=2, so the t*e - p^t
term is fitted at one value of t; S5's quartic is the only row that
tests t = 2.

PREDICTIONS, fixed before the run and stated as observables.
  PR1  The closed form reproduces the measured excess at every place of
       every ring already in the corpus, ramified, split and inert.
  PR2  The level sequence itself matches, depth by depth: M(m) = p^m for
       m <= t and M(m) = m*e + floor(a/f) + 1 for m >= t+1.
  PR3  DIVERGENCE ONE. At an INERT place over 2 (p2, e1, f2, a1) the
       filed criterion p-1 <= e holds, and the measured excess is 0 —
       lambda's runs are all of length 1. Read in a quadratic field with
       2 inert: disc = 5 mod 8, t^2 = t + 1.
  PR4  Outside the quadratic range, at Z[2^(1/3)] (p2 e3 f1 a1, t=1):
       excess 3, with M = 1, 2, 8, 11, 14.
  PR5  DIVERGENCE TWO. At Z[3^(1/3)] (p3 e3 f1 a0) the filed criterion
       holds (2 <= 3) and the closed form gives t=0, a=0, excess 0 —
       every lambda run is exactly e = 3.
  PR6  At Z[2^(1/4)] (p2 e4 f1 a1) the seam sits at t = 2, the only row
       that tests regime (i) past its first step: excess 6, with
       M = 1, 2, 4, 14, 18.

  The values of a above are DERIVED, never fitted: mu_(p^j) subset K_P
  forces p^(j-1)*(p-1) | e, which caps a at 1 for Z[2^(1/3)] and at 0
  for Z[3^(1/3)]; and Z[2^(1/4)] has exactly one quadratic subfield,
  Q_2(sqrt 2), because its Galois closure is D_4 over Q_2 — so i is not
  in it and a = 1 there too.

KILL-SHAPES, as observables.
  K1  a measured excess differs from the closed form at any place.
  K2  the inert-over-2 place prints a lambda run longer than 1 — PR3
      misses and the filed criterion survives its first inert test.
  K3  Z[3^(1/3)] prints a lambda run longer than 3.
  K4  a measured M sequence differs from the two-regime prediction at
      any depth, even where the excess happens to agree.

DISTRUST THE MARGIN. The DERIVED half is regime (ii): it is
an index count with no vibes in it, and it is what the two divergences
rest on. The VIBES half is the claim that regime (i) is exactly M(m) =
p^m with no cancellation before the seam — argued from the two terms
having distinct valuations below e0, but exercised at one value of t in
the filed data, which is what PR6 exists to test.

THE POSITIVE CONTROL (S1, run before any verdict is read). Two
instruments, each checked against a table it did not write.
  - The quadratic brute-forcer is IMPORTED from
    explore_gaussian_runaway.py, where it already reproduces two rings'
    independently written tables; it is re-run here against Z[i]'s
    filed R2 column before any new ring is read.
  - The PURE-RADICAL brute-forcer is new. It is checked twice: its
    generating-set exponent against a full enumeration of the unit
    group at small depth, and its n=2 instance (alpha^2 = -5, P =
    (alpha)) against K5's filed R5 column 4,20,20,100,100,500,500 —
    a table this code was not fitted to and did not write.

THE INSTRUMENT. For alpha^n = m with |m| = p prime, x^n -+ p is
Eisenstein at p, so P = (alpha) is the unique place over p, with e = n,
f = 1, and O/(alpha^k) = O/P^k of order p^k. Writing k = n*s + r, the
ideal (alpha^k) = (p^s * alpha^r) has Z-basis p^(s+1)*alpha^j for j < r
and p^s*alpha^j for j >= r, so a residue is a coefficient vector reduced
coordinatewise. The exponent is the lcm of the orders of a GENERATING
SET — legitimate because the group is abelian — and
{g} u {1 + c*alpha^i} generates, the second family filling every layer
U_i/U_(i+1) of the filtration.

FINDINGS (tiers below; run record at bottom; all sections assert).

0. READ THIS FIRST — WHAT IS NEW HERE IS A WELD, NOT A DERIVATION. The
   question above was minted from the LIMIT corpus, where the head's
   width is filed as open and its location as "p - 1 <= e". Everything
   this file derives on paper — the recursion psi(i) = min(p*i, i+e),
   the seat i* = e/(p-1), the level-1 segment reaching the seat iff the
   seat is a p-power, the seat dying iff f = 1 and mu_p is in K — was
   ALREADY IN THE CORPUS, in explore_local_clock.py, under the
   OBSERVATORY corpus's names: the two-gear clock, the Kummer seat, the
   splice. The width was already closed too, by
   explore_local_clock.py F4's landing chart and
   explore_arrival_defect.py's identity for it: the width is that
   landing less the seat and less e, and at e = 2 the landing's own
   EXTRA over the starter floor runs 0/1/2 as K(i)/K is ramified,
   unramified or split, which is the width running 1/2/3. So the
   derivation below re-walked a road the corpus had paved and did not
   know it owned. THE FINDING IS THAT THESE ARE ONE OBJECT,
   and that the two corners disagree — with the observatory's version
   right and the limit's wrong. The imports are where this should have
   been caught earlier and were not: this rig reaches the ring engines
   through explore_module_law.py and explore_number_field_lock.py, and
   the first of those carries the tail-gap theorem in its own docstring.
   An import is one mechanical line and its findings never come into
   view, which is exactly how a filed law gets re-derived twice over
   in one sitting. The rig is what welds them: it computes
   the LIMIT-side observable (the excess of lambda's longest run over e)
   from the OBSERVATORY-side conditions, at 24 places, and finds 9 where
   the limit corpus's own criterion is wrong.

1. THE HEAD IS THE BREATHING CLOCK'S TRANSIENT (derivation + rule in
   range, 24 places over 21 local fields, to depth 26). lambda's runs
   ARE the successive differences of the level sequence M(m) =
   max{n : U_1^(p^m) subset U_n}, so a place's tick ladder is the orbit
   of psi from M(0) = 1, with AT MOST ONE step where psi is not the
   whole story. psi is EXACT at 15 of the 24
   places, and at the other 9 it is exact up to ONE step and steps by e
   forever after. That one step is the head, and it is the splice ON THE
   LEVEL-1 ORBIT specifically — not every splice, which is a distinction
   the corpus's other corner already carries and this one must not lose.
   lambda is the exponent of U_1/U_a, so M is a MINIMUM over units and
   the ladder sees only the shallowest orbit; a deeper class can splice
   with the ladder none the wiser. Z[2^(1/6)] is that case here, running
   psi-exact at excess 0 while explore_local_clock.py records its deeper
   classes splicing at 13 and 14. So a head is an E-VISIBLE splice, and
   the criterion below is a criterion for visibility and not for
   existence. One corollary falls out, and it is NOT this file's: "the
   tail gap is the ramification index", which the limit corpus files as a
   rule measured at 90 of 90, is psi's second branch — and it is already
   a THEOREM at explore_module_law.py A, which this rig IMPORTS, for
   every complete DVR with finite residue field. So a head is a visible
   splice under another name, and that is why the width question could
   sit open on one side of the corpus while the other side charted it.
   THREE FACTS, ONE PATTERN — and the pattern is DUPLICATION, not a
   proof-against-measurement gap, which is a tier claim and has to be
   read off the tiers. The tail gap is the only leg where the other
   corner PROVED it (explore_module_law.py A, theorem). The criterion
   and the width are both RULES over exhaustive censuses on the
   observatory side (explore_local_clock.py, 14 mixed-char fields;
   explore_arrival_defect.py, 551 checks) — established, cross-verified,
   and every bit as binding on a later corner, but not proofs. What
   repeats at all three is that the limit corner re-derived a filed
   result under a name that shares no tokens with the filing, which is
   why no grep was ever going to find it. Three is a pattern about the
   corpus, not three coincidences.

2. THE LIMIT CORPUS'S CRITERION IS WRONG, AT 9 OF 24 MEASURED PLACES
   (rule in range; a criterion for a head, which is an E-VISIBLE splice
   per F1, and never for a splice existing at all). Filed at
   explore_tick_pump.py F1 and re-instanced
   at explore_gaussian_runaway.py F3, explore_lock_budget.py F6 and
   explore_element_schedule_nf.py: a head sits at exactly the places
   with p - 1 <= e. The right condition is the observatory's, restated
   in the head's own vocabulary:

       f = 1  AND  mu_p subset K_P  AND  e = (p-1)*p^t for some t >= 0.

   The necessity is derived, not fitted. psi's multiplying runs are
   p^j*(p-1) with p^j <= i*, so each is at most e and the TAIL run is
   the longest — no head — unless the segment LANDS on the seat, which
   needs i* = p^t, i.e. e = (p-1)p^t. Landing is not enough: at the seat
   the two gears have equal valuation and cancel only if the whole
   residue layer dies, which needs f = 1 (so the layer is F_p) and mu_p
   in K (so u -> u^p + cu is zero rather than injective). When it dies
   the step overshoots by at least 1, so a head is guaranteed rather
   than merely possible. The surviving e are the ramification indices of
   Q_p(zeta_(p^(t+1)))/Q_p: a head sits exactly where the place's
   ramification is cyclotomic.
   THE NINE COUNTEREXAMPLES, all measured at excess 0 where p - 1 <= e
   predicts a head, by which clause of the criterion each one fails:
     f = 1  — both INERT places over 2, where the residue layer is F_4
        and the seat dodges rather than dies. No ring the limit corpus
        walks has 2 inert, which is why its 90 never saw this.
     e = (p-1)p^t — Z[2^(1/3)] and Z[2^(1/6)], e not a power of 2;
        Z[3^(1/3)] and Z[3^(1/4)], e neither 2 nor 6 nor 18.
     mu_p in K_P — Z[sqrt 3], Z[3^(1/6)] and Z[5^(1/4)], all three of
        which LAND on the seat and still carry no head. Z[sqrt 3] is the
        sharp one at p = 3: zeta_3 needs sqrt -3, which would seat the
        unramified quadratic inside a ramified one, and Z[sqrt -3] is the
        same p and e WITH the torsion and carries a head of width 1. That
        pair is explore_local_clock.py's own opposite-parity twin
        arriving here through the other observable. Z[5^(1/4)] isolates
        the same clause at a THIRD prime, its e = 4 = (p-1)p^0 landing on
        the seat while Q_5(5^(1/4)) misses zeta_5 by not being Galois.
   Each clause is therefore load-bearing on its own evidence, and none of
   the three is carried by the other two.
   WHY 90 OF 90 HELD: every ring the limit corpus walks is quadratic, so
   e <= 2, and no ring in it has 2 inert — its 90 places are 82 split, 5
   inert and 3 ramified, the 5 inert over odd primes. At e <= 2 with
   f = 1 the two criteria separate only at p = 3 with e = 2 and no
   zeta_3, which is a ring the limit corpus does not have and the
   observatory corpus does.

3. THE WIDTH IS NOT THE TORSION'S, AND IT WAS NEVER OPEN (rule in range,
   9 headed places; the identity is explore_arrival_defect.py's).
   explore_gaussian_runaway.py F3 reads the local p-power torsion as
   SETTING the width, on the three headed places then available.
   Q_2(sqrt 2) and Q_2(sqrt -5) agree in p, e, f AND in the torsion
   order and carry widths 1 and 2, so no closed form in those four can
   exist; Q_2(sqrt -2) repeats Q_2(sqrt 2) at 1, which is the control
   that the clash is not one ring's accident.
   WHAT THE WIDTH IS: the level-1 ARRIVAL LANDING L of
   explore_local_clock.py F4, less the seat and less the gap --

       excess = L - i* - e,      i* = e/(p-1) the Kummer seat.

   BE PRECISE ABOUT WHICH HALF OF THAT IS CONTENT. Given that the step
   before the seam sits at p^t = i*, "excess = L - i* - e" is
   bookkeeping; what it asserts beyond bookkeeping is that the seam step
   lands where the OTHER corner's chart says, and that the seam run is
   the longest run in the ladder. Both are checked. The first is checked
   at the SEVEN places the two corners share, which is where the weld is
   load-bearing; at Q_2(2^(1/4)) and Q_2(2^(1/8)) the chart has no entry
   and L is this rig's own reading, so those two extend the relation and
   do not test it.
   S4 asserts the seam value of M against that file's filed landings
   (Q_2: 3, Q_2(sqrt +-2): 5, Q_2(sqrt -5): 6, Q_2(i): 7,
   Q_3(zeta_3): 4) -- a chart written elsewhere, for another observable,
   which this rig did not fit to, and it agrees at every place the two
   have in common. At p = 2 with e = 2 the relation collapses to
   excess = extra + 1, which is where explore_arrival_defect.py F1's
   trichotomy enters: the extra is 0, 1, 2 as K(i)/K is ramified,
   unramified or split, giving the three width VALUES 1, 2, 3 across the
   four places Q_2(sqrt +-2), Q_2(sqrt -5) and Q_2(i). "Plus one" is
   that corner and not the law. The wider
   identity is that file's F5 — the landing is the avoidance value of
   the p-power torsion constellation over K, so the head's width reads
   the ramification of the p-power cyclotomic tower. The measured widths
   here, as one more independent instance of that chart: 1 at Q_2 and
   Q_2(sqrt +-2) and Q_3(sqrt -3), 2 at Q_2(sqrt -5) and Q_2(2^(1/4)),
   3 at Q_2(i), 4 at Q_2(2^(1/8)).

4. THE FROZEN CLOSED FORM DIED, AND THE MARGIN-DISTRUST POINTED AT THE
   WRONG HALF. PR1, PR2, PR3 and PR5 held; PR4 and PR6 both MISSED, at
   the first two rows outside the range that produced the form. The half
   flagged VIBES — that the level segment is exactly p^m with no
   cancellation before the seat — held at all 24 places. The half
   flagged DERIVED, the index count, is what broke: [U_1 : U_1^(p^m)]
   pins the INDEX and nothing else, and a subgroup carrying a congruence
   subgroup's index need not be one. At e <= 2 it happens to be one, so
   the count fitted nine places; at e = 3, U_1^4 has index 2^7 and level
   4 where the congruence subgroup of that index has level 8. An index
   count is not a derivation when what it constrains is only the index —
   and the DERIVED/VIBES split is a claim about which step was CHECKED,
   never about which step sounds like arithmetic.

RUN RECORD. One command, 148 checks over 24 places in 21 local fields,
3.8 s wall clock, peak working set 21.9 MB under memwatch.py's 512 MB
ceiling. The pure-radical instrument agreed with a full enumeration of
the unit group at every depth small enough to enumerate, and reproduced
K5's filed R5 column, which it did not write.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import gcd

import explore_gaussian_runaway as GR
import explore_module_law as K23
import explore_number_field_lock as K5

CHECKS = 0

DEPTH_Q = 12         # depths brute-forced in a quadratic order
DEPTH_INERT = 8      # an inert place has norm q^2: fewer depths, same cost
FULL_CAP = 4096      # residues allowed in a full-enumeration cross-check

# explore_local_clock.py F4's level-1 ARRIVAL landings, filed there for the
# breathing clock and imported here as an outside reference for the head.
FILED_LANDINGS = {"K23 split2a": 3, "K23 split2b": 3, "Z[sqrt2]": 5,
                  "Z[sqrt-2]": 5, "K5 ram2": 6, "Zi ram2": 7,
                  "Z[sqrt-3]": 4}


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def lcm(a, b):
    return a * b // gcd(a, b)


# ---------------------------------------------- the pure-radical brute-forcer
# O = Z[alpha], alpha^n = m with |m| = p prime; P = (alpha).
def rad_moduli(n, p, k):
    """Coefficient moduli of O/(alpha^k), one per basis power of alpha."""
    s, r = divmod(k, n)
    return [p ** (s + 1) if j < r else p ** s for j in range(n)]


def rad_reduce(u, mods):
    return tuple(c % d for c, d in zip(u, mods))


def rad_mul(u, v, n, m, mods):
    out = [0] * n
    for i, a in enumerate(u):
        if not a:
            continue
        for j, b in enumerate(v):
            if not b:
                continue
            d, q = i + j, a * b
            if d >= n:
                d -= n
                q *= m
            out[d] += q
    return rad_reduce(tuple(out), mods)


def rad_pow(u, k, n, m, mods):
    res = rad_reduce(tuple([1] + [0] * (n - 1)), mods)
    base = u
    while k:
        if k & 1:
            res = rad_mul(res, base, n, m, mods)
        base = rad_mul(base, base, n, m, mods)
        k >>= 1
    return res


def _prime_factors(x):
    fac, q = set(), 2
    while q * q <= x:
        while x % q == 0:
            fac.add(q)
            x //= q
        q += 1
    if x > 1:
        fac.add(x)
    return sorted(fac)


def rad_order(u, n, m, mods, group_order, fac):
    one = rad_reduce(tuple([1] + [0] * (n - 1)), mods)
    o = group_order
    for q in fac:
        while o % q == 0 and rad_pow(u, o // q, n, m, mods) == one:
            o //= q
    return o


def rad_lambda(n, m, p, k, full=False):
    """Exponent of (O/P^k)^* for O = Z[alpha], alpha^n = m, P = (alpha)."""
    mods = rad_moduli(n, p, k)
    group_order = p ** (k - 1) * (p - 1)
    fac = _prime_factors(group_order)
    if full:
        exp, total = 1, 1
        for d in mods:
            total *= d
        idx = [0] * n
        for _ in range(total):
            u = tuple(idx)
            if u[0] % p:
                exp = lcm(exp, rad_order(u, n, m, mods, group_order, fac))
            for j in range(n):
                idx[j] += 1
                if idx[j] < mods[j]:
                    break
                idx[j] = 0
        return exp
    gens = []
    g = next(c for c in range(2, p + 2) if pow(c, p - 1, p) == 1
             and all(pow(c, (p - 1) // q, p) != 1 for q in _prime_factors(p - 1))
             ) if p > 2 else 1
    gens.append(rad_reduce(tuple([g] + [0] * (n - 1)), mods))
    for i in range(1, k):
        vec = [1] + [0] * (n - 1)
        vec[i % n] += p ** (i // n)
        gens.append(rad_reduce(tuple(vec), mods))
    exp = 1
    for u in gens:
        exp = lcm(exp, rad_order(u, n, m, mods, group_order, fac))
    return exp


# ------------------------------------------------------- the shared observable
def levels_from_lambda(col, p):
    """M(m) read off a lambda column: the last depth at which the p-part is
    p^m. Returns M as a list indexed by m, truncated to what the column
    determines (the final run may be incomplete and is dropped)."""
    part = []
    for lam in col:
        v = 0
        while lam % p == 0:
            lam //= p
            v += 1
        part.append(v)
    M, seen = [], -1
    for depth, v in enumerate(part, start=1):
        while seen < v:
            seen += 1
        if depth < len(part) and part[depth] > v:
            M.append(depth)
    return M


def runs_of(col):
    out, cur = [], 1
    for i in range(1, len(col)):
        if col[i] == col[i - 1]:
            cur += 1
        else:
            out.append(cur)
            cur = 1
    return out           # the trailing run is dropped: it may be incomplete


def seam_t(p, e):
    """t with e = (p-1)*p^t, or None -- the ladder lands ON e0 only there."""
    t, x = 0, p - 1
    while x < e:
        x *= p
        t += 1
    return t if x == e else None


def head_expected(p, e, f, a):
    """f = 1 and mu_p in K_P and e = (p-1)*p^t -- the cyclotomic criterion."""
    return f == 1 and a >= 1 and seam_t(p, e) is not None


def psi_levels(p, e, upto):
    """The tie-free recursion: M(m+1) = min(p*M(m), M(m)+e), M(0) = 1."""
    out, i = [1], 1
    for _ in range(upto - 1):
        i = min(p * i, i + e)
        out.append(i)
    return out


# ------------------------------------------------------- S1 positive control
def s1_control():
    section("S1  POSITIVE CONTROL -- two instruments, each against a table it "
            "did not write")
    print("  (a) the IMPORTED quadratic brute-forcer against Z[i]'s filed")
    print("      ramified column, before any new ring is read.")
    zi = [GR.lam_P(('ram', 2), n) for n in range(1, 13)]
    filed = [1, 2, 4, 4, 4, 4, 4, 8, 8, 16, 16, 32]
    print("      brute %s" % (",".join(str(x) for x in zi)))
    print("      filed %s" % (",".join(str(x) for x in filed)))
    ok(zi == filed, "imported brute-forcer lost Z[i]'s filed column")

    print()
    print("  (b) the NEW pure-radical brute-forcer, checked twice.")
    print("      generating-set exponent against FULL enumeration:")
    print("      %-22s %-6s %-8s %-8s" % ("ring", "depth", "gen-set", "full"))
    for n, m, p, kmax in ((2, -5, 5, 5), (3, 2, 2, 9), (3, 3, 3, 6),
                          (4, 2, 2, 10), (4, 5, 5, 5)):
        for k in range(1, kmax + 1):
            mods = rad_moduli(n, p, k)
            total = 1
            for d in mods:
                total *= d
            if total > FULL_CAP:
                continue
            gs = rad_lambda(n, m, p, k)
            fu = rad_lambda(n, m, p, k, full=True)
            print("      %-22s %-6d %-8d %-8d"
                  % ("alpha^%d = %d" % (n, m), k, gs, fu))
            ok(gs == fu, "generating set missed the exponent at depth %d" % k)

    print()
    print("      alpha^2 = -5 at P = (alpha) against K5's filed R5 column:")
    rad = [rad_lambda(2, -5, 5, k) for k in range(1, 8)]
    fk5 = [K5.lam_P(('ram', 5), k) for k in range(1, 8)]
    print("      radical %s" % (",".join(str(x) for x in rad)))
    print("      filed   %s" % (",".join(str(x) for x in fk5)))
    ok(rad == fk5, "the radical brute-forcer disagrees with K5's filed R5")
    print("      the instrument reproduced a filed column it did not write.")


# ------------------------------------------ S2 the criterion on filed places
# Every place read in this file, as (label, lambda-column, p, e, f, a).
# a is the local p-power torsion exponent, DERIVED in every row:
#   p = 2  -> mu_2 = {+-1} lies in every 2-adic field, so a >= 1 always;
#            a = 2 only at Q_2(i), the one ramified quadratic holding i.
#   p odd  -> mu_p needs (p-1) | e AND the right quadratic subfield:
#            Q_3(sqrt -3) = Q_3(zeta_3) holds it; Q_3(sqrt 3) cannot, being
#            ramified where Q_3(i) is unramified; and Q_3(3^(1/6)) cannot
#            hold both sqrt 3 and sqrt -3 without holding i, which would put
#            the unramified quadratic inside a totally ramified degree-6
#            extension.
def filed_places():
    rows = []
    for tag, mod, places in (
            ("K5", K5, [(('ram', 2), "ram2", 2, 2, 1, 1),
                        (('ram', 5), "ram5", 5, 2, 1, 0),
                        (('split', 3, 1), "split3", 3, 1, 1, 0)]),
            ("K23", K23, [(('split', 2, 0), "split2a", 2, 1, 1, 1),
                          (('split', 2, 1), "split2b", 2, 1, 1, 1),
                          (('ram', 23), "ram23", 23, 2, 1, 0)]),
            ("Zi", GR, [(('ram', 2), "ram2", 2, 2, 1, 2),
                        (('inert', 3), "inert3", 3, 1, 2, 0),
                        (('split', 5, 2), "split5", 5, 1, 1, 0)])):
        for pl, nm, p, e, f, a in places:
            col = [mod.lam_P(pl, n) for n in range(1, DEPTH_Q + 1)]
            rows.append(("%s %s" % (tag, nm), col, p, e, f, a))
    for nm, T, N0 in (("inert2 t^2=t+1", 1, 1), ("inert2 t^2=t-1", 1, -1)):
        col = [GR.unit_exponent(('inert', 2), k, T, N0)
               for k in range(1, DEPTH_INERT + 1)]
        rows.append((nm, col, 2, 1, 2, 1))
    return rows


RADICAL = (("Z[sqrt2]", 2, 2, 2, 1, 12), ("Z[sqrt-2]", 2, -2, 2, 1, 12),
           ("Z[2^(1/3)]", 3, 2, 2, 1, 16), ("Z[2^(1/4)]", 4, 2, 2, 1, 20),
           ("Z[2^(1/6)]", 6, 2, 2, 1, 20), ("Z[2^(1/8)]", 8, 2, 2, 1, 26),
           ("Z[sqrt3]", 2, 3, 3, 0, 10), ("Z[sqrt-3]", 2, -3, 3, 1, 10),
           ("Z[3^(1/3)]", 3, 3, 3, 0, 12), ("Z[3^(1/4)]", 4, 3, 3, 0, 13),
           ("Z[3^(1/6)]", 6, 3, 3, 0, 16),
           ("Z[5^(1/4)]", 4, 5, 5, 0, 10),
           ("Z[sqrt-5] R5", 2, -5, 5, 0, 8))


def radical_places():
    out = []
    for nm, n, m, p, a, depth in RADICAL:
        col = [rad_lambda(n, m, p, k) for k in range(1, depth + 1)]
        out.append((nm, col, p, n, 1, a))
    return out


def s2_criterion(rows):
    section("S2  THE CRITERION, AT EVERY PLACE THIS FILE CAN REACH")
    print("  filed criterion:  a head exists iff p - 1 <= e.")
    print("  this file's:      iff f = 1 AND mu_p in K_P AND e = (p-1)p^t,")
    print("                    which is the ramification index of")
    print("                    Q_p(zeta_(p^(t+1))) -- the only e at which the")
    print("                    multiplying sequence LANDS on e0 = e/(p-1).")
    print("  %-16s %-3s %-3s %-3s %-3s %-5s %-6s %-7s %-8s %s"
          % ("place", "p", "e", "f", "a", "t", "filed", "here", "excess",
             "verdict"))
    split = 0
    for nm, col, p, e, f, a in rows:
        exc = max(runs_of(col)) - e
        t = seam_t(p, e)
        here = head_expected(p, e, f, a)
        filed = (p - 1 <= e)
        if filed != here:
            split += 1
        print("  %-16s %-3d %-3d %-3d %-3d %-5s %-6s %-7s %-8d %s"
              % (nm, p, e, f, a, "-" if t is None else t,
                 "head" if filed else "none", "head" if here else "none",
                 exc, "agree" if filed == here else "SPLIT"))
        ok((exc > 0) == here,
           "%s: criterion says %s, measured excess %d" % (nm, here, exc))
    print("  the measurement follows this file's criterion at all %d places;"
          % len(rows))
    print("  the filed criterion is wrong at %d of them." % split)
    return split


# ------------------------------------------------ S3 the level sequence itself
def s3_levels(rows):
    section("S3  THE LEVEL SEQUENCE -- the two regimes, and where the tie bites")
    print("  Below e0 the p-th power map MULTIPLIES the level; above it the")
    print("  map is U_i -> U_(i+e) and the level STEPS by e. Where the two")
    print("  agree -- level exactly e0 -- the leading terms cancel iff the")
    print("  whole residue layer dies, which needs f = 1 and mu_p in K_P.")
    print("  So psi(i) = min(p*i, i+e) is EXACT wherever no head is expected,")
    print("  and a head is precisely the one step where it is not.")
    print("  %-16s %-26s %-26s %s"
          % ("place", "M measured", "psi (tie-free)", "note"))
    for nm, col, p, e, f, a in rows:
        M = levels_from_lambda(col, p)
        P = psi_levels(p, e, len(M))
        expect = head_expected(p, e, f, a)
        print("  %-16s %-26s %-26s %s"
              % (nm, ",".join(str(x) for x in M),
                 ",".join(str(x) for x in P), "seam" if expect else "psi exact"))
        if not expect:
            ok(M == P, "%s: psi is not exact: %s vs %s" % (nm, M, P))
            continue
        k = next(i for i in range(len(M)) if M[i] != P[i])
        ok(M[:k] == P[:k], "%s: psi broke before the seam" % nm)
        ok(P[k - 1] * (p - 1) == e, "%s: the break is not at level e0" % nm)
        ok(M[k] > P[k], "%s: the seam step went the wrong way" % nm)
        for i in range(k, len(M) - 1):
            ok(M[i + 1] == M[i] + e,
               "%s: the tail does not step by e at m=%d" % (nm, i))
    print("  psi is exact at every headless place, and at every headed one it")
    print("  is exact up to the seam and steps by e forever after it.")


# ------------------------------------ S4 what the width is NOT a function of
def s4_width_open(rows):
    section("S4  THE WIDTH IS NOT A FUNCTION OF (p, e, f, a)")
    print("  The corpus reads the local torsion as SETTING the width, on")
    print("  three headed places. Sorting every headed place this file")
    print("  measures by (p, e, f, a) refutes it: one signature carries two")
    print("  widths.")
    print("  %-16s %-14s %-8s" % ("place", "(p,e,f,a)", "excess"))
    seen = {}
    for nm, col, p, e, f, a in rows:
        if not head_expected(p, e, f, a):
            continue
        exc = max(runs_of(col)) - e
        print("  %-16s %-14s %-8d" % (nm, "(%d,%d,%d,%d)" % (p, e, f, a), exc))
        seen.setdefault((p, e, f, a), set()).add(exc)
    print()
    print("  And the seam value of M against explore_local_clock.py F4's")
    print("  filed level-1 arrival landings -- a chart written for another")
    print("  observable, which this rig did not fit to:")
    print("  %-16s %-8s %-8s %s" % ("place", "M at seam", "filed", "excess"))
    for nm, col, p_, e, f, a in rows:
        if nm not in FILED_LANDINGS:
            continue
        M = levels_from_lambda(col, p_)
        P = psi_levels(p_, e, len(M))
        k = next(i for i in range(len(M)) if M[i] != P[i])
        seat = e // (p_ - 1)
        print("  %-16s %-8d %-8d %d"
              % (nm, M[k], FILED_LANDINGS[nm], M[k] - seat - e))
        ok(M[k] == FILED_LANDINGS[nm],
           "%s: seam lands at %d, the clock chart says %d"
           % (nm, M[k], FILED_LANDINGS[nm]))
        ok(M[k] - seat - e == max(runs_of(col)) - e,
           "%s: excess is not L - i* - e" % nm)
    print("  every shared place agrees, so the head's width IS the arrival")
    print("  landing less the seat and the gap -- one object, two corners.")
    clash = [k for k, v in seen.items() if len(v) > 1]
    for k in clash:
        print("  SIGNATURE %s carries widths %s" % (str(k), sorted(seen[k])))
    ok(clash, "no signature carries two widths -- the torsion reading stands")
    print("  so no closed form in (p, e, f, a) can give the width, and the")
    print("  torsion reading is dead. What separates the clashing pair is")
    print("  measured elsewhere: Q_2(sqrt 2) has different exponent 3 where")
    print("  Q_2(sqrt -5) has 2 -- and the seam step above is that same")
    print("  reading arriving through the clock, so nothing here is open.")


def main():
    s1_control()
    rows = filed_places() + radical_places()
    split = s2_criterion(rows)
    s3_levels(rows)
    s4_width_open(rows)
    section("CHECKS")
    print("  %d checks passed over %d places, %d of which split the two "
          "criteria" % (CHECKS, len(rows), split))


if __name__ == "__main__":
    main()
