"""THE RESIDUAL THE SWEEP CANNOT REACH -- how late a number field can
first admit a rank-1 place, and what that costs it in discriminant.

THE QUESTION. explore_cascade_chars.py closed the cascade boundary at
every odd characteristic below 1000, which by the reduction's
conjunction (a carrier is demanded at EVERY characteristic carrying a
rank-1 place, so breaking ONE suffices) closes every char-0 ring
possessing a rank-1 characteristic below 1000. The residual it handed
on is the rings whose rank-1 characteristics ALL exceed 1000, and the
question is whether that residual is inhabited -- and if it is, whether
extending the sweep is a route to emptying it.

Write L(K) for the LEAST rank-1 characteristic of a number field K: the
least rational prime unramified in K with a place of residue degree 1.
The residual at bound P is exactly {K : L(K) > P}. So the question is
how large L(K) can be, and at what price.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) WHAT A RANK-1 CHARACTERISTIC IS, MECHANICALLY. p is rank-1 for K
      iff p is unramified in K and some place above it has residue
      degree 1 -- iff the Frobenius class of p in G = Gal(L/Q), acting
      on the n = [K:Q] embeddings, has a FIXED POINT. Fixed-point-free
      elements exist in any transitive G of degree n > 1 (Jordan), so
      the set of bad primes is not empty; but a point stabilizer has
      index n and every one of its elements fixes that point, so the
      good elements are at least |G|/n and the good primes have density
      at least 1/n by Chebotarev. L(K) is therefore FINITE for every K.
      (Burnside is the wrong instrument here and the error is easy to
      make: it gives an AVERAGE of one fixed point per element, which
      bounds no COUNT from below, one element being free to carry many.)

  (2) THE DENSITY ARGUMENT SAYS NOTHING ABOUT THE LEAST ONE, AND THE
      GAP IS RAMIFICATION. Density 1/n is a statement about the tail;
      it survives the deletion of any FINITE set of primes untouched.
      The ramified primes are exactly such a finite set, and they are
      excluded from rank-1 by definition. So the whole of L(K) can be
      pushed up by RAMIFYING, and the cost is paid in discriminant and
      nowhere else.

  (3) THE RESIDUAL IS INHABITED AT EVERY BOUND, CONSTRUCTIVELY. Take
      the primorial d = 2*3*5*...*P and K = Q(sqrt d). Every prime <= P
      divides the discriminant of K (d = 2 mod 4, so disc = 4d), hence
      ramifies, hence is not rank-1. So L(K) > P. This is elementary,
      unconditional, and available at every P -- so NO finite sweep over
      characteristics empties the residual, and extending P_MAX raises
      the bar without ever clearing it. The witness is the project's own
      object, which is a coincidence of vocabulary and not of content.

  (4) SO THE REAL QUESTION IS THE PRICE, AND THERE ARE TWO WAYS TO PAY
      IT. A prime p < P fails to be rank-1 in a quadratic K in exactly
      two ways: RAMIFIED (p | disc) or INERT (chi(p) = -1). Ramifying
      every prime below P costs a discriminant of size exp(theta(P)) ~
      exp(P) -- the primorial, and it is a terrible deal. Inertness
      costs no discriminant factor at all; it costs a CONGRUENCE, one
      of the (p-1)/2 non-residue classes mod p, i.e. a factor of about
      2 in the count of surviving discriminants per prime. Demanding it
      at every prime below P leaves a density of about 2^-pi(P), so the
      least witness should sit near exp(pi(P) * ln 2), which is
      exp(P ln 2 / ln P) -- SMALLER than the primorial by an entire
      logarithm in the exponent. The prediction is therefore that the
      cheapest witnesses are mostly INERT and hardly ramified at all,
      and the primorial construction of (3) is the honest existence
      proof and the worst possible witness.

  (5) WHY THIS IS COMPUTABLE AT ALL. For a fundamental discriminant D
      the whole of the above is the Kronecker symbol: p is rank-1 for
      Q(sqrt D) iff chi_D(p) = +1, ramified iff 0, inert iff -1, at
      p = 2 as well as at odd p. So L(D) is a walk up the primes
      evaluating one symbol each, and the champion sequence -- the
      smallest |D| attaining each record value of L -- is one sweep over
      an initial segment of the fundamental discriminants.

  (6) WHAT THE ANSWER IS WORTH EVEN SO. If the champions grow like
      (4) says, then L(K) <= about log|disc| * loglog|disc| at the
      extreme, so the sweep a GIVEN ring needs, to have its own cascade
      boundary closed by explore_cascade_chars.py's machinery, is
      logarithmic in that ring's discriminant. The residual is then
      uncloseable wholesale and cheap retail: no uniform close without
      a theorem, but a per-ring close within reach for any ring anyone
      writes down. That is the shape of the answer this rig is after.

PREDICTIONS (fixed before any engine code; hand-derived above).

  H1 (POSITIVE CONTROL, the splitting test). For every fundamental
     discriminant |D| <= 400 and every prime p <= 200, the Kronecker
     symbol chi_D(p) agrees with the root count of the ring's own
     minimal polynomial mod p -- x^2 - x + (1-D)/4 for D = 1 mod 4 and
     x^2 - D/4 for D = 0 mod 4, whose root count is 2 / 1 / 0 exactly
     as chi is +1 / 0 / -1 (Dedekind, applicable at every p because
     that polynomial generates the maximal order). KILL: any
     disagreement.
  H2 (POSITIVE CONTROL, hand specimens). L(-4) = 5, L(-3) = 7,
     L(8) = 7, L(5) = 11 -- each derived by hand from the splitting
     congruence (p = 1 mod 4; p = 1 mod 3; p = +-1 mod 8; p = +-1 mod
     5). KILL: any mismatch.
  H3 (THE CONSTRUCTION, (3) above). For every odd prime P <= 97, the
     field attached to the primorial through P has L > P. OBSERVABLE:
     the printed pair (P, L) for each. KILL: any L <= P -- the
     ramification argument would then be wrong, and with it the claim
     that the residual is inhabited at all.
  H4 (THE HEADLINE, rule if it holds). The champions are exponentially
     cheaper than the primorial: over the swept range the ratio
     log|D_champ| / theta(L) DECREASES across the champion sequence.
     OBSERVABLE: that ratio printed at every champion, and the count of
     increases over the last half of the sequence. KILL: the ratio
     rises on more than half of the steps in that half -- the primorial
     would then not be being beaten, and (4)'s congruence accounting
     would be the thing that is wrong.
  H5 (THE MARGIN, distrusted by construction). log|D_champ| /
     (pi(L) * ln 2) lies in [0.5, 2.0] for every champion with L >= 10.
     OBSERVABLE: the ratio at each champion and the count outside the
     band. This scores the heuristic of (4) and carries no verdict
     either way: the kill is H4's, which is a comparison between two
     measured sequences, and this one is a comparison against a model.
  H6 (THE MECHANISM). At every champion with L >= 20, the primes below
     L are mostly INERT rather than ramified: the ramified count is at
     most a third of pi(L). OBSERVABLE: the two counts printed per
     champion. KILL: a champion with L >= 20 whose ramified count
     exceeds a third -- (4) would then have the two prices backwards.

WHAT A CLEAN RUN BUYS, and what it does not. It does not touch the
reduction, which is cited from explore_module_law.py and read rather
than checked, and it does not close any characteristic: the ladder is
explore_cascade_chars.py's and is not re-run here. It settles whether
the residual that rig handed on is inhabited, and it prices the entry.
The sweep is over QUADRATIC fields only, so every quantitative claim
below is a claim about degree 2; the degree-n direction (a cyclic field
of degree n makes a proportion 1 - 1/n of Frobenius classes bad, so the
congruence price per prime FALLS with n while the conductor rises) is
named here and not measured.

FINDINGS.

  1. THE RESIDUAL IS INHABITED AT EVERY BOUND, SO NO SWEEP EMPTIES IT
     (theorem: the argument is hand-derivation (3), complete for every P
     with no computation in it, and the engine only controls it). For every P the primorial field
     Q(sqrt(2*3*...*P)) has every prime <= P dividing its discriminant,
     hence ramified, hence not rank-1: L > P, checked at every odd
     P <= 97 and printed with its witness (H3). So extending
     explore_cascade_chars.py's P_MAX raises the bar and never clears
     it, and the residual is not a shrinking remainder but a moving
     target with members at every bound. The machinery this question
     first appears to need -- effective Chebotarev, GRH, the density 1/n
     from a point stabilizer -- is the wrong instrument for BOUNDING L,
     and precisely the right one for the neighbouring question (1) uses
     it on, which is whether L is finite at all. The distinction is the
     whole content: a density is a statement about the TAIL and survives
     the deletion of any finite set, so it settles that rank-1
     characteristics exist and says nothing about where the first one
     is, while the ramified primes ARE such a finite set and are exactly
     what the least one is at the mercy of. The construction is
     elementary and no density argument can see it.

  2. THE ENTRY PRICE IS EXPONENTIALLY BELOW THE PRIMORIAL, AND THAT IS
     THE USEFUL HALF (rule, verified |D| <= 10^8, degree 2). Sweeping
     every fundamental discriminant to 10^8 gives 15 champions -- the
     least |D| attaining each record L -- reaching L = 127 at
     D = 46,305,413. The champion law is log|D| ~ ln2 * pi(L), and the
     comparison it licenses is DIRECT and needs no trend in it: at
     L = 127 the champion's log|D| is 17.65, sitting beside
     pi(<127) ln 2 = 20.79 at a ratio of 0.85, against a primorial
     witness's theta(<127) = 107.07 for the SAME guarantee. So finding
     1's existence proof pays 6.07 times the exponent and is the worst
     possible witness -- exp(pi(P) ln 2) = exp(P ln 2 / ln P) against
     exp(theta(P)) ~ exp(P), an entire logarithm in the exponent.

     Two things the law is NOT. It is not a TREND result: the ratio to
     theta satisfies H4 (2 of 7 steps rising in the last half), but that
     half runs 0.175 to 0.165, which is nearly flat, and the visible
     fall from 0.41 at L = 17 is a small-L artifact rather than the
     asymptotics arriving. The ratio should decay like ln2/ln L, which
     over L = 41 to 127 predicts a factor 0.77 where the data deliver
     0.96: the direction is right, the rate is not yet visible, and the
     sweep is too short to measure it. And it is not a BOUND. Inverting
     gives L ~ 1.44 log|D| ln L, which is implicit, and the explicit
     expansion in |D| alone carries a second-order term nearly as large
     as its leading one at this reach -- the naive
     L ~ 1.4 log|D| loglog|D| reads 71 where the top champion has
     L = 127, so it is quoted only to be refused. What the law describes
     is the measured extremal family to 10^8 in degree 2; for an
     arbitrary field what is available is conditional -- effective
     Chebotarev under GRH giving L << (log|disc|)^2 -- and nothing
     measured here replaces it. Claiming the retail case cheap BECAUSE
     of a bound would
     claim for every ring what was measured of one family's extremes --
     which is what hand-derivation (6) reached for before the run, and
     it is left standing there as the expectation it was, corrected here
     rather than edited there.

     It is cheap for a different reason: L(K) is
     COMPUTABLE -- a walk up the primes evaluating one Frobenius each,
     which is exactly what this rig does over 10^8 discriminants -- so a
     ring anyone actually writes down does not need its L estimated. It
     needs it computed, and the ladder is then run at that single
     characteristic. The residual is uncloseable wholesale and cheap
     retail, and the cheapness is a computation rather than an
     asymptotic.

  3. THE MECHANISM IS NOT TWO RIVALS BUT A TERM AND A BONUS (H6, 0
     violations). Every champion with L >= 20 is mostly inert: at
     L = 127, 26 inert against 4 ramified. But the ramified count is
     never zero past L = 41 either, and that is what the two failures
     NOT competing would lead one to expect -- expect, and not explain:
     the observation is 15 minimizers deep and finding 5 refuses the
     stronger reading of it. A prime fails to be rank-1 with
     probability (p-1)/2p + 1/p = (p+1)/(2p), the inert half PLUS the
     ramified 1/p -- so ramification is a bonus term on top of
     inertness rather than an alternative to it, worth prod (1 + 1/p) ~
     (6 e^gamma / pi^2) ln L over the whole range.

  4. THE MARGIN'S FAILURE WAS THE INSTRUMENT, AND THE GUARD POINTS THE
     WRONG WAY FOR THAT. As first run, H5 FAILED on one champion and
     POST-HOC A was written to diagnose it. The diagnosis was of nothing:
     theta and pi were summing over the primes p <= L, where L is the
     one prime a champion is NOT required to kill -- it is by definition
     that champion's rank-1 characteristic -- so both baselines charged
     it for a prime it never had to buy, by log L at theta and by one
     count at pi. Corrected to p < L, H5 PASSES with nothing outside the
     band (0.5805 to 1.0299) and the crude mean moves 0.7988 to 0.8615.
     The failure was the instrument and not the model, which is the
     ordinary lesson of any negative result and has a sharper edge here.
     A prediction of this rig's H5 kind -- a band around a heuristic,
     written down before the run and expected to be the soft part of the
     slate -- is easy to distrust while it PASSES, because a pass is
     what a loose band does anyway. When it FAILS it stops being
     distrusted: a failure looks like the rig catching itself, it is
     expensive to have written, and it invites a diagnosis rather than
     an audit. That is what happened here for one round, and the
     baseline underneath went unexamined the whole time.

     POST-HOC A survives its own audit and still fails its own test, and
     both facts are kept: it is scored on the SPAN, the span widens
     (0.74 to 1.41 against 0.58 to 1.03), and a refined density model
     moves the BIAS (mean 0.8615 to 1.0317) while it cannot touch the
     SCATTER, a champion being a MINIMUM over a pseudorandom set whose
     logarithm fluctuates by O(1) at every L. A margin test on a minimum
     must be scored on the mean; the range is the fluctuation and does
     not shrink. The kills that carried verdicts (H3, H4) were derived
     and both held.

     One more thing the correction owes the record, since it moved the
     basis of predictions that were FROZEN. H4 and H6 are scored on the
     same two baselines and were re-run on the corrected ones. H4 reads
     2 of 7 rising steps under BOTH, so its verdict is untouched and
     does not rest on the change; H6 passes with room under both. Only
     H5 moved, and it is the only one of the three whose statistic is a
     ratio the missing prime shifts hardest at the small-L end.

  5. THE RAMIFICATION-FREE CHAMPIONS ARE EULER'S PRIME-GENERATING
     POLYNOMIALS, WHICH IS AN EXTERNAL CONTROL (POST-HOC B). Exactly
     two champions have no ramified prime below L: D = -67 at L = 17
     and D = -163 at L = 41. Writing D = 1 - 4q, "every prime below q
     is inert" is precisely Rabinowitsch's condition, equivalent to
     class number one, and x^2 + x + q is verified prime for
     x = 0..q-2 at both (q = 17, 41). The rig contains no class-field
     theory and no Heegner list; that its ramification-free champions
     land on the two largest classical discriminants is a check on the
     whole sweep from mathematics the sweep does not know. It is NOT
     evidence that the unramified route closes at 41: the later
     champions have L far below |D|/4, where Rabinowitsch says nothing,
     so their buying a little ramification is a fact about minimizers
     and not a theorem about availability.

RUN RECORD. 10/11 checks pass; the one failure is POST-HOC A, a margin
and no-verdict by construction (finding 4). Peak
working set 131.5 MB against the 512 MB ceiling, wall 38.8 s under
memwatch.py (the squarefree sieve at 10^8 is the peak, and the length
of each strided assignment is computed rather than sliced because the
slice would copy 25 MB before being overwritten). X = 10^8,
PRIME_CAP = 100,000, CTRL_D = 400, CTRL_P = 200.

ONE THING ABOUT HOW THIS RIG GOT HERE. X was set at 4*10^6 from a
wall-clock estimate of minutes and raised to 10^8 after a timing probe
showed 121,588 discriminants swept in 0.08 s -- the estimate was wrong
by two orders of magnitude because the walk up the primes exits at
p = 2 for a quarter of all discriminants and at p = 3 or 5 for most of
the rest, so the average L evaluated is a handful of small-modulus
powmods and not a walk. The raise can only lengthen the champion
sequence, and it cannot have selected for a verdict for a reason that is
checkable rather than argued: it was made on the timing probe alone,
which printed a discriminant count and a record L and no ratio at all,
so not one statistic H4 or H5 is scored on had been seen when X was
chosen.
"""

import os
import sys
from math import log

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

PASS = []


def ok(cond, label):
    PASS.append(bool(cond))
    print(f"    [{'PASS' if cond else 'FAIL'}] {label}")


# ---------------------------------------------------------------- parameters

X = 100_000_000        # sweep |D| <= X over fundamental discriminants
PRIME_CAP = 100_000    # primes available to the L walk; overflow is a hard error
CTRL_D = 400           # H1 control range in |D|
CTRL_P = 200           # H1 control range in p


# ---------------------------------------------------------------- primitives

def primes_upto(n):
    """Sieve of Eratosthenes -> list of primes <= n."""
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        i += 1
    return [i for i in range(n + 1) if sieve[i]]


PRIMES = primes_upto(PRIME_CAP)


def squarefree_flags(n):
    """bytearray f with f[a] = 1 iff a is squarefree, for a <= n."""
    f = bytearray([1]) * (n + 1)
    f[0] = 0
    q = 2
    while q * q <= n:
        sq = q * q
        # length computed rather than sliced: at X = 10^8 the slice f[sq::sq]
        # would copy 25 MB before being overwritten, and the copy is the peak.
        f[sq::sq] = bytearray((n - sq) // sq + 1)
        q += 1
    return f


def chi(D, p):
    """The Kronecker symbol (D/p) for a fundamental discriminant D and a
    prime p: +1 rank-1 (split), 0 ramified, -1 inert. At p = 2 this is
    the residue of D mod 8, which is what makes the walk uniform in p."""
    if p == 2:
        r = D % 8
        return 0 if r % 2 == 0 else (1 if r == 1 else -1)
    a = D % p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def least_rank1(D):
    """L(D): the least prime p with chi_D(p) = +1."""
    for p in PRIMES:
        if chi(D, p) == 1:
            return p
    raise RuntimeError(f"no rank-1 characteristic below {PRIME_CAP} for D={D}")


def is_fundamental(D, sf):
    """D is a fundamental discriminant: D = 1 mod 4 squarefree (D != 1),
    or D = 4m with m = 2 or 3 mod 4 and m squarefree."""
    if D in (0, 1):
        return False
    a = abs(D)
    if D % 4 == 1:
        return bool(sf[a])
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and bool(sf[abs(m)])
    return False


def poly_root_count(D, p):
    """Roots mod p of the minimal polynomial of the maximal order's
    generator -- the H1 control, independent of the symbol."""
    if D % 4 == 1:
        c = (1 - D) // 4
        return sum(1 for x in range(p) if (x * x - x + c) % p == 0)
    c = D // 4
    return sum(1 for x in range(p) if (x * x - c) % p == 0)


def fundamental_of(d):
    """The fundamental discriminant of Q(sqrt d) for squarefree d."""
    return d if d % 4 == 1 else 4 * d


def theta(L):
    """The primorial witness's cost at the same guarantee as a champion
    with least rank-1 characteristic L: sum of log p over the primes
    STRICTLY BELOW L. L itself is the rank-1 prime and is the one prime
    the witness is not required to kill, so a baseline summing to <= L
    overstates by log L -- which at L = 127 is 4.8 of 111.9."""
    return sum(log(p) for p in PRIMES if p < L)


def pi(L):
    """Likewise: the count of primes the champion has to make fail."""
    return sum(1 for p in PRIMES if p < L)


# ---------------------------------------------------- H1: the splitting test

print("\nH1  the splitting test against the maximal order's own polynomial")
sf_ctrl = squarefree_flags(CTRL_D)
bad = []
ctrl_pairs = 0
for D in range(-CTRL_D, CTRL_D + 1):
    if not is_fundamental(D, sf_ctrl):
        continue
    for p in PRIMES:
        if p > CTRL_P:
            break
        want = {2: 1, 1: 0, 0: -1}[poly_root_count(D, p)]
        if chi(D, p) != want:
            bad.append((D, p, chi(D, p), want))
        ctrl_pairs += 1
print(f"    {ctrl_pairs} (D, p) pairs compared; {len(bad)} disagreements")
ok(not bad, "H1  Kronecker symbol == Dedekind root count, every pair")


# ------------------------------------------------------- H2: hand specimens

print("\nH2  hand-derived least rank-1 characteristics")
SPEC = {-4: 5, -3: 7, 8: 7, 5: 11}
for D, want in sorted(SPEC.items()):
    got = least_rank1(D)
    print(f"    L({D:+d}) = {got}   hand-derived {want}")
    ok(got == want, f"H2  L({D:+d}) = {want}")


# -------------------------------------------------- H3: the primorial witness

print("\nH3  the primorial construction: every prime <= P ramifies")
prim = 2
h3_bad = 0
for P in [p for p in PRIMES if 3 <= p <= 97]:
    prim *= P
    D = fundamental_of(prim)
    L = least_rank1(D)
    if L <= P:
        h3_bad += 1
    if P in (3, 5, 11, 31, 97):
        print(f"    P = {P:3d}  disc = 4 * primorial ({len(str(D))} digits)"
              f"   L = {L:4d}   L > P: {L > P}")
print(f"    {h3_bad} of the swept P have L <= P")
ok(h3_bad == 0, "H3  L > P for every primorial witness, P <= 97")


# ------------------------------------------- the sweep: the champion sequence

print(f"\nsweeping fundamental discriminants |D| <= {X:,}")
sf = squarefree_flags(X)
champions = []          # (L, D)
best = 0
for a in range(1, X + 1):
    for D in (a, -a):
        if not is_fundamental(D, sf):
            continue
        L = least_rank1(D)
        if L > best:
            best = L
            champions.append((L, D))
print(f"    {len(champions)} champions; the record reaches L = {best}")
print(f"\n    {'L':>5} {'D':>12} {'log|D|':>8} {'/theta(L)':>10} "
      f"{'/pi(L)ln2':>10} {'ram':>4} {'inert':>6}")
rows = []
for L, D in champions:
    lg = log(abs(D))
    th = theta(L)
    pl = pi(L) * log(2)
    ram = sum(1 for p in PRIMES if p < L and chi(D, p) == 0)
    inert = sum(1 for p in PRIMES if p < L and chi(D, p) == -1)
    rows.append((L, D, lg, lg / th if th else float("nan"),
                 lg / pl if pl else float("nan"), ram, inert))
    print(f"    {L:>5} {D:>12} {lg:>8.3f} {rows[-1][3]:>10.4f} "
          f"{rows[-1][4]:>10.4f} {ram:>4} {inert:>6}")


# ------------------------------------------------------------ H4, H5, H6

print("\nH4  the champions beat the primorial: log|D|/theta(L) decreasing")
half = rows[len(rows) // 2:]
rises = sum(1 for i in range(1, len(half)) if half[i][3] > half[i - 1][3])
steps = max(1, len(half) - 1)
print(f"    last half = {len(half)} champions, {rises} of {steps} steps rise")
ok(rises * 2 <= steps, "H4  ratio to theta(L) rises on at most half the steps")

print("\nH5  the margin (distrusted): log|D| / (pi(L) ln 2) in [0.5, 2.0]")
band = [r for r in rows if r[0] >= 10]
out = [r for r in band if not (0.5 <= r[4] <= 2.0)]
if band:
    print(f"    {len(band)} champions with L >= 10; {len(out)} outside the band"
          f"; range {min(r[4] for r in band):.4f} to "
          f"{max(r[4] for r in band):.4f}")
ok(not out, "H5  every champion with L >= 10 inside the band")

print("\nH6  the mechanism: the cheap witnesses are inert, not ramified")
h6 = [r for r in rows if r[0] >= 20]
h6_bad = [r for r in h6 if r[5] > pi(r[0]) / 3]
print(f"    {len(h6)} champions with L >= 20; {len(h6_bad)} with ramified "
      f"count above pi(L)/3")
ok(not h6_bad, "H6  ramified count <= pi(L)/3 at every champion with L >= 20")



# --------------------------------------------------------------- POST-HOC
# Both blocks below were written AFTER the run above printed, to diagnose
# H5's failure and to anchor the champion sequence against mathematics the
# rig does not contain. Neither carries a verdict on the question; they are
# marked so that a later reader cannot mistake a fitted model for a frozen
# prediction.

print("\nPOST-HOC A  the refined density, diagnosing H5")
# (4) priced a prime's failure to be rank-1 at 1/2 -- the inert half. But
# RAMIFIED is also a failure, so the true per-prime survival is
# (p-1)/2/p + 1/p = (p+1)/(2p), and the product over p < L carries an extra
# factor prod (1 + 1/p) ~ (6 e^gamma / pi^2) ln L. That factor is what makes the
# observed ratio DRIFT DOWNWARD instead of sitting on a constant, which is
# the shape H5's fixed band could not express.
print(f"    {'L':>5} {'log|D|':>8} {'crude':>8} {'refined':>8} {'ratio':>8}")
for L, D, lg, _rt, _rp, _r, _i in rows:
    if L < 10:
        continue
    surv = 1.0
    for p in PRIMES:
        if p >= L:
            break
        surv *= (p + 1) / (2 * p)
    refined = -log(surv)
    print(f"    {L:>5} {lg:>8.3f} {pi(L) * log(2):>8.3f} {refined:>8.3f} "
          f"{lg / refined:>8.4f}")
ref_ratios = []
for L, D, lg, _rt, _rp, _r, _i in rows:
    if L < 10:
        continue
    surv = 1.0
    for p in PRIMES:
        if p >= L:
            break
        surv *= (p + 1) / (2 * p)
    ref_ratios.append(lg / -log(surv))
crude_ratios = [r[4] for r in band]
print(f"    refined ratio spans {min(ref_ratios):.4f} to "
      f"{max(ref_ratios):.4f}")
print(f"    MEAN ratio: crude {sum(crude_ratios) / len(crude_ratios):.4f}, "
      f"refined {sum(ref_ratios) / len(ref_ratios):.4f}  <- the bias, which "
      f"is what the (1+1/p) factor moves")
ok(max(ref_ratios) - min(ref_ratios)
   < max(r[4] for r in band) - min(r[4] for r in band),
   "POST-HOC A  the refined model spans a NARROWER band than the crude one")

print("\nPOST-HOC B  the unramified champions against classical mathematics")
# Every champion whose primes below L are ALL inert is, by definition, a
# discriminant with no small split prime and no small ramified one. For
# D = 1 - 4q that is exactly Rabinowitsch's condition, equivalent to class
# number one, and the imaginary quadratic fields with class number one stop
# at D = -163 (Baker-Heegner-Stark). The rig knows none of this; that its
# ramification-free champions ARE the classical discriminants is an external
# control on the whole sweep.
unram = [(L, D) for L, D, _lg, _rt, _rp, r, _i in rows if r == 0]
print(f"    ramification-free champions: {unram}")
euler_ok = True
for L, D in unram:
    if D >= 0 or (1 - D) % 4 != 0:
        euler_ok = False
        continue
    q = (1 - D) // 4
    prime_run = all(
        all((x * x + x + q) % t for t in range(2, int((x * x + x + q) ** 0.5) + 1))
        for x in range(q - 1))
    print(f"    D = {D}: q = {q}, x^2 + x + {q} prime for x = 0..{q - 2}: "
          f"{prime_run}   L = {L} = q: {L == q}")
    euler_ok = euler_ok and prime_run and L == q
ok(euler_ok and len(unram) == 2,
   "POST-HOC B  both unramified champions are Rabinowitsch discriminants")


print(f"\n{sum(PASS)}/{len(PASS)} checks pass")
