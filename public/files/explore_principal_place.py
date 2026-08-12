"""HOW FAR DOWN IS A FIELD'S FIRST PRINCIPAL RANK-1 PLACE? -- the
coverage statistic the per-place reading of the door actually needs.

THE QUESTION. explore_element_cascade.py finding 4 established that the
door's padding constant is PER-PLACE and not per-field: the door at a
rank-1 characteristic pads P^(v+2) by an ideal of class [P]^-(v+2), so
the constant applying there is tau_P = max over k of the least norm in
[P]^-k, which is at most tau_K and is exactly 1 when P is PRINCIPAL.
At a principal rank-1 place the door costs p^(v+2) on the nose and the
ideal world's cap m <= p-1 holds verbatim, so the UNLOOSENED walk --
the tau = 1 ladder, already certified dead at every odd characteristic
below 1000 (explore_cascade_chars.py) -- closes the ELEMENT dynamics of
that ring outright. Since the reduction demands a carrier at EVERY
characteristic carrying a rank-1 place, breaking ONE closes the ring.

So a char-0 ring is closed in the element world the moment it holds a
principal rank-1 characteristic below 1000, and the coverage statistic
is not tau_K at all. It is

    L_1(K) = the least PRINCIPAL rank-1 characteristic of K,

against which explore_element_cascade.py finding 3's census -- mean
tau_K = 9.58, only 11.8% of fields at tau_K <= 4 -- measured the wrong
quantity. That finding's numbers stand as a measurement of tau_K; what
they do not measure is coverage. THIS rig measures coverage.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) WHAT A PRINCIPAL RANK-1 PLACE IS, MECHANICALLY, IN THE QUADRATIC
      CASE. For a fundamental discriminant D < 0, p is rank-1 iff it is
      unramified with a residue-degree-1 place, i.e. iff chi_D(p) = +1
      (the Kronecker symbol), which for odd p not dividing D is
      quadratic residuacity of D mod p. Such a p has two places P and
      P-bar with [P-bar] = [P]^-1 in the class group. Under the
      classical correspondence between ideal classes and classes of
      primitive positive-definite binary forms of discriminant D, the
      class of P is represented by a form, and p is a value of that
      form and of its opposite. So P is PRINCIPAL exactly when p is
      REPRESENTED BY THE PRINCIPAL FORM. No class-field computation is
      needed: the whole test is arithmetic.

  (2) THE TEST, EXACTLY, AND IT IS A ONE-LINE COMPLETION OF THE SQUARE.
      The principal form is (1, b0, c0) with b0 = D mod 2 in {0,1} and
      c0 = (b0^2 - D)/4. Then

          x^2 + b0*x*y + c0*y^2 = p   <=>   (2x + b0*y)^2 + |D|*y^2 = 4p.

      So p is represented iff 4p = u^2 + |D|*y^2 for integers u, y with
      u = b0*y mod 2. The parity side-condition is in fact automatic
      when D is odd (|D| = 3 mod 4 forces u and y to share parity for
      the sum to be 0 mod 4) and vacuous when D is even (b0 = 0 and u
      must be even, which u^2 = 4p - |D|y^2 = 0 mod 4 gives), but it is
      checked rather than argued: an asserted automatic condition that
      is wrong is a silent acceptance, which is the failure mode that
      would inflate coverage. The loop is over y with |D|*y^2 <= 4p, so
      the test costs O(sqrt(4p/|D|)) and is essentially free.

  (3) A RAMIFIED PRIME CAN PASS THE REPRESENTATION TEST AND MUST NOT
      COUNT. D = -4 and p = 2 gives 2 = 1^2 + 1^2, and (2) ramifies.
      Representation by the principal form says the place is principal,
      not that it is rank-1; rank-1 is the SYMBOL's business. So L_1
      takes the conjunction, and the control on the test is that it
      never accepts an INERT prime (chi = -1) -- accepting a RAMIFIED
      one is correct behaviour and not a bug.

  (4) WHAT TO EXPECT, AND IT IS CHEBOTAREV. Principal degree-1 places
      are exactly the primes splitting completely in the Hilbert class
      field H, and [H:Q] = 2h for imaginary quadratic K (H/K of degree
      h, K/Q of degree 2, and H/Q is Galois here because K/Q is). So
      the principal rank-1 primes have density 1/(2h), and the naive
      first-hit heuristic puts L_1 near the p with pi(p) = 2h, i.e.

          L_1 ~ 2h * ln(2h).

      Over |D| <= 1000 the class number reaches 28, so the heuristic
      tops out near 225 -- comfortably below 1000. [CORRECTION, made at
      the audit and left in place because the slate is a frozen record:
      28 is misread off the tau_K census's LARGEST-tau field, which is
      not its largest-h one. The class number over this range reaches
      36, so the heuristic's ceiling is 308. Neither number changes what
      the prediction says or how the run answers it -- finding 4 has the
      heuristic wrong in KIND -- and the misreading is recorded rather
      than repaired because it is the one place a neighbouring census's
      number was carried without being recomputed.] Since h grows like
      sqrt|D| (Siegel), the heuristic grows like sqrt|D|*log|D|, and the
      bound 1000 should start to bite somewhere around |D| ~ 10^4. That
      is a prediction the extended sweep can hit or miss.

  (5) THE THEOREM SHAPE BEHIND IT, AND WHY THE PARALLEL WITH THE
      LADDER'S OWN DEATH IS A COINCIDENCE OF INSTRUMENT AND NOT OF
      OBSTRUCTION. "How far down is the least prime splitting completely
      in H" is a least-prime-in-a-Chebotarev-class question, the same
      analytic object as the least prime in an arithmetic progression;
      unconditionally it is a Linnik-type bound and under GRH it is
      O((log disc H)^2), which with log disc H of order h*log|D| gives
      L_1 = O((h log|D|)^2) -- polynomial, and conditional. The ladder's
      death is ALSO blocked by a least-prime-shaped statement, and the
      resemblance invites reading one obstruction twice. It is not one.
      Here the analytic bound is the one we WANT and points at the
      answer: an upper bound on the least prime in the class is exactly
      an upper bound on L_1. At the ladder the same instrument points
      the wrong way: what is needed there is that NO prime power sits in
      a short window of candidates, and a theorem producing a prime in a
      progression produces a SURVIVOR, not a death. The two questions
      share an object and stand on opposite sides of it. That is worth
      recording precisely because the shared vocabulary invites filing
      the one as evidence about the other.

  (6) THE RESIDUAL CARRIES OVER FOR FREE, AND IT IS NOT GOOD NEWS.
      L_1(K) >= L(K) always, so the primorial witness of
      explore_cascade_residual.py -- K = Q(sqrt(2*3*...*P)), every prime
      <= P ramified, hence L(K) > P -- has L_1(K) > P too. The residual
      of the PRINCIPAL reading is inhabited at every bound by the same
      construction, with no new work. So a wide L_1 census would widen
      COVERAGE and would not touch the uniform front; those are separate
      questions and this rig answers only the first.

PREDICTIONS (fixed before any engine code; no timing probe was run).

  C1 (POSITIVE CONTROL, the representation test). The completed-square
     test agrees with a brute-force search over the (x,y) box on every
     prime p < CTRL_P and every fundamental D with |D| <= CTRL_D. KILL:
     any disagreement. A test that under-accepts inflates L_1 and would
     manufacture the kill-shape; one that over-accepts deflates it and
     would manufacture the headline. Both directions are fatal here,
     which is why the control is exhaustive rather than sampled.
  C2 (POSITIVE CONTROL, the symbol). The test never accepts a prime with
     chi_D(p) = -1. KILL: any inert acceptance. (Ramified acceptances
     are expected -- hand-derivation (3) -- and are printed, not killed.)
  C3 (POSITIVE CONTROL, class number one). At h = 1 every split prime is
     principal, so L_1(D) = L(D) at every one-class fundamental
     discriminant in range. KILL: any disagreement. Both quantities are
     taken over ODD primes throughout, the certified walk being a walk
     over odd characteristics; p = 2 is closed separately by the budget
     inequality and is not this rig's business.
  C4 (POSITIVE CONTROL, the density). For a handful of named fields the
     count of principal rank-1 primes below DENS_CAP agrees with
     pi(DENS_CAP)/(2h) to within 25%. KILL: a miss. This is the
     Chebotarev density stated in (4), and it is the assumption the
     whole heuristic in (4) rests on.

  Q1 (THE QUESTION; observation). Over the 305 fundamental discriminants
     down to -1000, the distribution of L_1: mean, median, max, and the
     COUNT OF FIELDS WITH L_1 > 1000. OBSERVABLE: that count.
     KILL-SHAPE: it exceeds 10% of the fields -- then the principal-place
     reading covers little, the honest coverage number goes back to being
     small, and /growth/fields must say so where it now says the
     per-place reading is the one that scales.
  Q2 (THE CROSSOVER; observation, no kill). Over |D| <= D_BIG, the
     fraction of fields with L_1 > 1000 by |D| band. Hand-derivation (4)
     puts the crossover near |D| ~ 10^4. OBSERVABLE: the per-band
     fractions.
  Q3 (THE MARGIN; scored, no kill and no evidential weight). Mean L_1
     binned by h against the heuristic 2h*ln(2h). OBSERVABLE: the ratio
     per bin. A heuristic is not a claim and a miss here is a fact about
     the heuristic.
  Q4 (THE CHAMPIONS; observation, no kill). The record-setting L_1 in
     each sweep with its D and h -- the analogue of the champion
     sequence explore_cascade_residual.py measured for L, whose
     mechanism (ramification bought with discriminant) is a DIFFERENT
     one from this sweep's (class number bought with discriminant).

WHAT A CLEAN RUN BUYS. A coverage number for the element-world close
that is measured rather than assumed: the fraction of imaginary
quadratic fields whose element dynamics the ALREADY-CERTIFIED tau = 1
ladder closes. It buys nothing about the uniform front (6), nothing
outside degree 2, and nothing about tau_K, whose census stands as a
measurement of tau_K and is simply not the coverage statistic.

FINDINGS (all sections assert; copied from run output only).

  1. THE FLOOR: L_1 >= |D|/4, EXACTLY, AND IT IS ATTAINED (theorem over
     every imaginary quadratic field, both directions proved; derived
     post-hoc, and controlled at 0 violations over 6079 fields). The
     tier is the corpus's own for an elementary unconditional statement
     holding at its whole scope with no computation in it -- the same
     one the inhabited residual carries -- and "property" would
     under-claim a proof that needs no range. The slate did not
     see it and the run made it unmissable -- no band above |D| = 5000
     had a single field under the bound, and a first-hit process with a
     lower tail cannot print a clean 100.0%. It is the same completion
     of the square the test runs: 4p = u^2 + |D|y^2, y = 0 would make p
     a square, so y != 0 and 4p >= |D|; for odd D the parity forces u
     odd and 4p >= |D| + 1. The bound is TIGHT -- D = -19995 has
     L_1 = 4999 = (|D|+1)/4 on the nose -- and attained at 499 of the
     6079 fields (8.2%), every one of them at ODD D, exactly when
     (|D|+1)/4 is an odd prime. Both halves of that are mechanism: the
     principal form takes the value c_0 = (|D|+1)/4 at (x, y) = (0, 1),
     and D = 1 - 4c_0 makes gcd(c_0, D) = 1, so a prime c_0 is
     unramified and principal by that very representation; while at
     D = 0 mod 4 the floor value |D|/4 DIVIDES D, hence ramifies, hence
     is never rank-1 -- and no even discriminant attains the floor. The
     converse needs no more than the definition: L_1 is an odd prime, so
     if it equals the floor then the floor IS an odd prime, and the even
     case is excluded by the ramification just given. The floor knows
     nothing about the class group and holds at every h.

  2. SO THE COVERAGE IS A FINITE SET, AND THE FLOOR NAMES IT (rule,
     proved + verified to |D| = 20000). At sweep bound P, no field with
     |D| > 4P holds a principal rank-1 characteristic below P AT ALL.
     At P = 1000 that leaves 1217 fundamental discriminants, of which
     856 (70.3%) are closed and the other 4862 fields in the sweep are
     closed by nothing. At most 36 of the same 1217 (3.0%) are reached
     by the tau route -- that is the count with tau_K <= 4, which is
     necessary and not sufficient, so the rival is being over-counted in
     its own favour. So the per-place reading is the wider of the two by
     at least 24x over the range where either lives -- and BOTH are finite-set
     readings. Neither scales, and the uniform front is untouched:
     hand-derivation (6) hands the primorial witness L_1 >= L > P for
     free, so the residual of the principal reading is inhabited at
     every bound by the construction already in the corpus.

  3. THE CENSUS THE AIM ASKED FOR, AND THE KILL-SHAPE MISSED
     (observation; the 305 fundamental discriminants to -1000). L_1
     <= 1000 at 296 of 305 (97.0%), mean 291.2, median 181, max 2111 at
     D = -815 (h = 30); the nine survivors are D = -479, -671, -815,
     -831, -863, -887, -959, -983, -991. Against finding 3 of
     explore_element_cascade.py -- 11.8% of these same fields at
     tau_K <= 4 -- the per-place reading covers at LEAST eight times as
     much, that 11.8% being an upper bound on the tau route for finding
     2's reason, and covers it with the UNLOOSENED walk. But the 97% is the range's
     number and not the world's, and finding 2 is why: |D| <= 1000 sits
     entirely under the floor's cap of 4000, so this census samples
     exactly the region where the reading is alive. Quote 97% only with
     its range attached; the reading that survives the range being
     changed is finding 2's.

  4. THE CROSSOVER IS THE FLOOR'S, NOT CHEBOTAREV'S (observation; 6079
     fields to -20000). Fields with L_1 > 1000, by band: 3.0% at
     |D| <= 1000, then 35.8%, 65.0%, 100.0%, 100.0%. Hand-derivation
     (4) predicted a crossover near |D| ~ 10^4 from the class number
     alone; it sits at 4000 and is forced by the floor. The heuristic
     2h*ln(2h) undershoots the measured mean L_1 at every one of the 34
     class numbers in range, by 2.88x (at h = 20) to 8.56x (at h = 3),
     and it is wrong in KIND rather than in constant: it models
     L_1 as a first hit in a density-1/(2h) set starting from the
     bottom, and below |D|/4 that set is EMPTY. The density itself is
     not what failed -- C4 measures it at 0.887 to 0.980 of 1/(2h) over
     100,000 primes -- so the failure is entirely in where the walk
     starts.

  5. THE MULTIPLE OVER THE FLOOR IS A FUNCTION OF NEITHER VARIABLE
     ALONE (observation). Binning L_1/(|D|/4) by class number and by
     |D| kills both readings on one table: along h in [13, 30] the
     multiple falls 4.31 -> 2.44 -> 1.55 -> 1.17 -> 1.02 as |D| grows
     (widest row spread 3.29), so it is no function of h; down the
     |D| <= 5000 column it rises 1.01 -> 1.55 -> 3.44 -> 5.00, so it is
     no function of |D| either. What IS stable is that it stays modest
     -- row means 1.29 to 3.74 across the whole sweep -- which is what
     makes finding 2's cap the right ORDER and not merely a bound. The
     falling rows have finding 1's mechanism behind them: a fixed h band
     at growing |D| selects fields with an unusually small class number
     for their size, and those are the fields whose c_0 is prime or
     nearly so, sitting at or just above the floor.

RUN RECORD. 11/11 checks pass. Peak working set 15.7 MB and peak commit
10.4 MB against the 512 MB ceiling, wall 2.8 s under memwatch.py.
D_MAX = 1000, D_BIG = 20,000, BOUND = 1000, PRIME_CAP = 200,000,
CTRL_D = 400, CTRL_P = 200, DENS_CAP = 100,000.
"""

import os
import sys
import time
from math import gcd, isqrt, log

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

PASS = []


def ok(cond, label):
    PASS.append(bool(cond))
    print(f"    [{'PASS' if cond else 'FAIL'}] {label}")


# ---------------------------------------------------------------- parameters

D_MAX = 1000           # the primary census, matching finding 3's 305 fields
D_BIG = 20_000         # the extended sweep, to find the crossover of Q2
BOUND = 1000           # the certified sweep bound: the walk kills odd p < 1000
PRIME_CAP = 200_000    # primes available to the L_1 walk; overflow is an error
CTRL_D = 400           # C1 control range in |D|
CTRL_P = 200           # C1 control range in p
DENS_CAP = 100_000     # C4 density-count range


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
ODD_PRIMES = [p for p in PRIMES if p != 2]


def squarefree_flags(n):
    """bytearray f with f[a] = 1 iff a is squarefree, for a <= n."""
    f = bytearray([1]) * (n + 1)
    f[0] = 0
    q = 2
    while q * q <= n:
        sq = q * q
        f[sq::sq] = bytearray((n - sq) // sq + 1)
        q += 1
    return f


def chi(D, p):
    """Kronecker symbol (D/p): +1 rank-1 (split), 0 ramified, -1 inert."""
    if p == 2:
        r = D % 8
        return 0 if r % 2 == 0 else (1 if r == 1 else -1)
    a = D % p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def is_fundamental(D, sf):
    """D < 0 is fundamental: D = 1 mod 4 squarefree, or D = 4m with
    m = 2,3 mod 4 and m squarefree."""
    if D >= 0:
        return False
    a = -D
    if D % 4 == 1:
        return bool(sf[a])
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and bool(sf[-m])
    return False


def principal_form(D):
    """(1, b0, c0), the principal reduced form of discriminant D < 0."""
    b0 = D % 2
    return 1, b0, (b0 * b0 - D) // 4


def represents_principal(D, p):
    """Hand-derivation (2): (x, y) with x^2 + b0*x*y + c0*y^2 = p, or
    None. Solved as 4p = u^2 + |D|*y^2 with u = b0*y mod 2."""
    b0 = D % 2
    fourp, absD = 4 * p, -D
    y = 0
    while absD * y * y <= fourp:
        r = fourp - absD * y * y
        u = isqrt(r)
        if u * u == r and (u - b0 * y) % 2 == 0:
            return (u - b0 * y) // 2, y
        y += 1
    return None


def brute_represents(D, p):
    """C1's independent search: the (x, y) box directly, no completion of
    the square. x^2 + b0*x*y + c0*y^2 = p with (x + b0*y/2)^2 <= p and
    (|D|/4)*y^2 <= p."""
    _, b0, c0 = principal_form(D)
    ylim = isqrt(4 * p // -D) + 1
    xlim = isqrt(p) + ylim + 1
    for y in range(-ylim, ylim + 1):
        for x in range(-xlim, xlim + 1):
            if x * x + b0 * x * y + c0 * y * y == p:
                return True
    return False


def reduced_forms(D):
    """Every reduced primitive positive-definite form of discriminant
    D < 0 -- one per ideal class, so len() is h(D)."""
    out = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if gcd(gcd(a, abs(b)), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            out.append((a, b, c))
        a += 1
    return out


def least_rank1(D):
    """L(D): the least ODD prime with chi_D(p) = +1."""
    for p in ODD_PRIMES:
        if chi(D, p) == 1:
            return p
    raise RuntimeError(f"no rank-1 characteristic below {PRIME_CAP}, D={D}")


def least_principal_rank1(D, primes=None):
    """L_1(D): the least ODD prime that is rank-1 AND principal."""
    for p in (primes or ODD_PRIMES):
        if chi(D, p) == 1 and represents_principal(D, p) is not None:
            return p
    raise RuntimeError(f"no principal rank-1 char below {PRIME_CAP}, D={D}")


SF = squarefree_flags(D_BIG + 1)

print("=" * 72)
print("C1 THE TEST: completed square against a brute (x, y) box search")
print("=" * 72)

t0 = time.time()
disagree = []
for D in range(-3, -CTRL_D - 1, -1):
    if not is_fundamental(D, SF):
        continue
    for p in PRIMES:
        if p >= CTRL_P:
            break
        if (represents_principal(D, p) is not None) != brute_represents(D, p):
            disagree.append((D, p))
ok(not disagree,
   f"C1: agrees with the box search on every fundamental |D| <= {CTRL_D} "
   f"and every p < {CTRL_P} ({len(disagree)} disagreements, {time.time()-t0:.1f}s)")

hits, exact = 0, True
for D in range(-3, -CTRL_D - 1, -1):
    if not is_fundamental(D, SF):
        continue
    _, b0, c0 = principal_form(D)
    for p in PRIMES:
        if p >= CTRL_P:
            break
        rep = represents_principal(D, p)
        if rep is None:
            continue
        hits += 1
        x, y = rep
        exact = exact and x * x + b0 * x * y + c0 * y * y == p
ok(hits > 0 and exact,
   f"C1: every acceptance returns an exact representation "
   f"({hits} acceptances checked)")

print()
print("=" * 72)
print("C2 THE SYMBOL: the test never accepts an inert prime")
print("=" * 72)

inert_accept, ram_accept = [], []
for D in range(-3, -CTRL_D - 1, -1):
    if not is_fundamental(D, SF):
        continue
    for p in PRIMES:
        if p >= CTRL_P:
            break
        if represents_principal(D, p) is None:
            continue
        s = chi(D, p)
        if s == -1:
            inert_accept.append((D, p))
        elif s == 0:
            ram_accept.append((D, p))
ok(not inert_accept,
   f"C2: no inert acceptance ({len(inert_accept)}); ramified acceptances "
   f"{len(ram_accept)}, e.g. {ram_accept[:6]}")

print()
print("=" * 72)
print("C3 CLASS NUMBER ONE: L_1 = L at every h = 1 field")
print("=" * 72)

one_class = []
for D in range(-3, -D_MAX - 1, -1):
    if not is_fundamental(D, SF):
        continue
    if len(reduced_forms(D)) == 1:
        one_class.append(D)
mismatch = [D for D in one_class if least_principal_rank1(D) != least_rank1(D)]
print(f"    h = 1 discriminants in range: {one_class}")
ok(not mismatch and len(one_class) == 9,
   f"C3: L_1 = L at all {len(one_class)} one-class fields "
   f"({len(mismatch)} mismatches)")

print()
print("=" * 72)
print(f"C4 THE DENSITY: principal rank-1 primes below {DENS_CAP} vs pi/(2h)")
print("=" * 72)

dens_primes = [p for p in ODD_PRIMES if p <= DENS_CAP]
dens_bad = []
for D in (-23, -47, -71, -239, -935):
    h = len(reduced_forms(D))
    n = sum(1 for p in dens_primes
            if chi(D, p) == 1 and represents_principal(D, p) is not None)
    want = len(dens_primes) / (2.0 * h)
    ratio = n / want
    print(f"    D = {D:>5}  h = {h:>2}  counted {n:>5}  expected {want:8.1f}  "
          f"ratio {ratio:.3f}")
    if not 0.75 <= ratio <= 1.25:
        dens_bad.append(D)
ok(not dens_bad, f"C4: every field within 25% of density 1/(2h) "
                 f"({len(dens_bad)} misses)")

print()
print("=" * 72)
print(f"Q1 THE CENSUS: L_1 over fundamental discriminants to -{D_MAX}")
print("=" * 72)

t0 = time.time()
rows = []
for D in range(-3, -D_MAX - 1, -1):
    if not is_fundamental(D, SF):
        continue
    h = len(reduced_forms(D))
    rows.append((D, h, least_rank1(D), least_principal_rank1(D)))

L1s = sorted(r[3] for r in rows)
over = [r for r in rows if r[3] > BOUND]
mean = sum(L1s) / len(L1s)
med = L1s[len(L1s) // 2]
worst = max(rows, key=lambda r: r[3])
print(f"    fields: {len(rows)}   mean L_1 = {mean:.1f}   median {med}   "
       f"max {worst[3]} at D = {worst[0]} (h = {worst[1]})")
for t in (10, 50, 100, 250, 500, BOUND):
    n_le = sum(1 for v in L1s if v <= t)
    print(f"    L_1 <= {t:>5}: {n_le:>4} of {len(rows)} "
          f"({100.0 * n_le / len(rows):5.1f}%)")
print(f"    fields with L_1 > {BOUND}: {len(over)}  {[r[0] for r in over][:12]}")
print(f"    (mean L over the same fields, for scale: "
      f"{sum(r[2] for r in rows) / len(rows):.1f}; {time.time()-t0:.1f}s)")
ok(len(over) <= 0.10 * len(rows),
   f"Q1: fields with L_1 > {BOUND} are at most 10% of the census "
   f"({len(over)}/{len(rows)} = {100.0*len(over)/len(rows):.1f}%)")

print()
print("=" * 72)
print(f"Q3 THE MARGIN: mean L_1 by class number against 2h*ln(2h)")
print("=" * 72)

by_h = {}
for D, h, _L, L1 in rows:
    by_h.setdefault(h, []).append(L1)
for h in sorted(by_h):
    vals = by_h[h]
    heur = 2 * h * log(2 * h) if h > 1 else 2.0
    print(f"    h = {h:>2}  n = {len(vals):>3}  mean L_1 = "
          f"{sum(vals)/len(vals):8.1f}  heuristic {heur:7.1f}  "
          f"ratio {(sum(vals)/len(vals))/heur:5.2f}")

print()
print("=" * 72)
print(f"Q2/Q4 THE CROSSOVER: L_1 over fundamental discriminants to -{D_BIG}")
print("=" * 72)

t0 = time.time()
big = []
for D in range(-3, -D_BIG - 1, -1):
    if not is_fundamental(D, SF):
        continue
    forms = reduced_forms(D)
    big.append((D, len(forms), least_principal_rank1(D),
                max(a for a, _, _ in forms)))
print(f"    fields: {len(big)}  ({time.time()-t0:.1f}s)")

edges = [1000, 2500, 5000, 10000, D_BIG]
lo = 0
for hi in edges:
    band = [r for r in big if lo < -r[0] <= hi]
    if not band:
        lo = hi
        continue
    n_over = sum(1 for r in band if r[2] > BOUND)
    print(f"    |D| in ({lo:>5}, {hi:>5}]: {len(band):>4} fields, "
          f"mean h {sum(r[1] for r in band)/len(band):5.1f}, "
          f"mean L_1 {sum(r[2] for r in band)/len(band):7.1f}, "
          f"L_1 > {BOUND} at {n_over:>4} ({100.0*n_over/len(band):5.1f}%)")
    lo = hi

champs, best = [], 0
for D, h, L1, _t in sorted(big, key=lambda r: -r[0]):
    if L1 > best:
        best = L1
        champs.append((D, h, L1))
print(f"    champions (record L_1 by |D|): "
      f"{champs[-8:] if len(champs) > 8 else champs}")
ok(all(r[2] >= 1 for r in big) and len(big) > len(rows),
   f"Q2: the extended sweep resolved every one of {len(big)} fields")

# ------------------------------------------------------------- POST-HOC
# Derived AFTER the slate froze, from Q2's printed bands: no band above
# |D| = 5000 has a single field under the bound, and a first-hit process
# with a lower tail cannot produce a clean 100.0%. The cause is a floor
# the slate did not see, and it is three lines of the same completion of
# the square the test itself runs. These sections predicted nothing.

print()
print("=" * 72)
print("POST-HOC A  THE FLOOR: L_1 >= |D|/4, and it is exact arithmetic")
print("=" * 72)
# 4p = u^2 + |D|*y^2. y = 0 forces p = (u/2)^2, and no prime is a square,
# so y != 0 and 4p >= |D| + u^2 >= |D|. For D odd the parity of (2) makes
# u odd, so u >= 1 and 4p >= |D| + 1. The floor is a statement about the
# FORM and knows nothing about the class group -- it applies to every
# field, whatever h is.
allrows = [(D, h, L1) for D, h, L1, _t in big]
floor_of = {D: (-D + 1) // 4 if D % 2 else -D // 4 for D, _, _ in allrows}
viol = [(D, L1, floor_of[D]) for D, _, L1 in allrows if L1 < floor_of[D]]
tight = min(allrows, key=lambda r: r[2] / (-r[0] / 4.0))
ok(not viol,
   f"POST-HOC A  L_1 >= |D|/4 at every one of {len(allrows)} fields "
   f"({len(viol)} violations); tightest is D = {tight[0]}, "
   f"L_1 = {tight[2]} against floor {floor_of[tight[0]]}")

# And the floor is ATTAINED on the nose by an identifiable set. For
# D = 1 mod 4 the principal form takes the value c0 = (|D|+1)/4 at
# (x, y) = (0, 1), and gcd(c0, D) = 1 since D = 1 - 4*c0, so if c0 is
# PRIME it is unramified, principal by that very representation, hence
# rank-1, hence L_1 = c0 = the floor. For D = 0 mod 4 the floor value
# |D|/4 = m DIVIDES D and is therefore ramified, so the floor is never
# attained there. Both halves are predictions of the mechanism, not
# observations of it, and the rig checks both directions. The floor
# value must also be ODD to be attained: L_1 walks odd characteristics,
# and D = -7 puts a prime 2 at the floor which the walk does not take.
PSET = set(PRIMES)


def floor_attained_predicted(D):
    f = floor_of[D]
    return D % 2 == 1 and f % 2 == 1 and f in PSET


mis = [D for D, _, L1 in allrows
       if (L1 == floor_of[D]) != floor_attained_predicted(D)]
att = [D for D, _, L1 in allrows if L1 == floor_of[D]]
even_att = [D for D in att if D % 2 == 0]
print(f"    floor attained at {len(att)} of {len(allrows)} fields "
      f"({100.0*len(att)/len(allrows):.1f}%), of which even D: {len(even_att)}")
ok(not mis,
   f"POST-HOC A  L_1 hits the floor exactly when D is odd and (|D|+1)/4 "
   f"is prime ({len(mis)} mismatches)")

print()
print("=" * 72)
print("POST-HOC B  THE MULTIPLE OVER THE FLOOR: what it is NOT a function of")
print("=" * 72)
# The band table above reads as if L_1/|D| were a constant near 0.52,
# which would say the class number contributes nothing. It is an
# artefact: h and |D| grow together across bands, so a band average
# holds neither fixed. Dividing out the floor and binning by h separates
# them. Two hypotheses die on this table and it is worth naming both
# BEFORE reading it: "the multiple is a function of h" needs the rows
# flat, and "the multiple is a function of |D|" needs the columns flat.
# Whatever it does, the ROW SPREAD is the number that decides the first.
HB = [(1, 4), (5, 12), (13, 30), (31, 70), (71, 10 ** 6)]
lo = 0
dbands = []
for hi in edges:
    dbands.append((lo, hi))
    lo = hi
head = "".join(f"{f'<={hi}':>10}" for _, hi in dbands)
print(f"    mean L_1 / (|D|/4){'':>4}{head}      all")
rowspread = []
for h0, h1 in HB:
    cells, alln = [], []
    for lo, hi in dbands:
        part = [r for r in allrows if lo < -r[0] <= hi and h0 <= r[1] <= h1]
        cells.append(sum(r[2] / (-r[0] / 4.0) for r in part) / len(part)
                     if len(part) >= 10 else None)
        alln.extend(part)
    if not alln:
        continue
    seen = [c for c in cells if c is not None]
    rowspread.append(max(seen) - min(seen))
    lab = f"h in [{h0}, {h1 if h1 < 10**6 else ''}]"
    print(f"    {lab:<22}" +
          "".join(f"{c:>10.2f}" if c is not None else f"{'-':>10}"
                  for c in cells) +
          f"{sum(r[2] / (-r[0] / 4.0) for r in alln) / len(alln):>9.2f}"
          f"  (n = {len(alln)})")
print(f"    widest spread along any single h row: {max(rowspread):.2f}")

print()
print("=" * 72)
print(f"POST-HOC C  WHAT THE FLOOR DOES TO COVERAGE AT BOUND {BOUND}")
print("=" * 72)
# The floor caps the principal-place route at a FINITE set of fields: no
# field with |D| >= 4*BOUND can hold a principal rank-1 place below
# BOUND at all. The comparison against the tau_K route is made over that
# same capped range, which is the only range where either is alive.
# tau_K <= 4 is counted as an UPPER BOUND on that route and not as its
# reach: it is necessary but not sufficient, the tau = 3 and tau = 4
# walks being swept only to 700 and 500, so a field with tau_K in {3, 4}
# whose least rank-1 characteristic lies above its own tau's bound is
# counted here and is not in fact closed. The over-count runs in favour
# of the rival, which is the safe direction for the comparison below.
cap = 4 * BOUND
inrange = [(D, h, L1, tk) for D, h, L1, tk in big if -D <= cap]
closed = [r for r in inrange if r[2] <= BOUND]
tau4 = [r for r in inrange if r[3] <= 4]
print(f"    fundamental discriminants with |D| <= {cap}: {len(inrange)}")
print(f"    of them closed by a principal rank-1 char below {BOUND}: "
      f"{len(closed)} ({100.0*len(closed)/len(inrange):.1f}%)")
print(f"    of them with tau_K <= 4, an UPPER BOUND on the tau route's "
      f"reach: {len(tau4)} ({100.0*len(tau4)/len(inrange):.1f}%)")
print(f"    fields with |D| > {cap} closed by this route: 0, by POST-HOC A")
ok(all(r[2] > BOUND for r in big if -r[0] > cap),
   f"POST-HOC C  no field with |D| > {cap} has L_1 <= {BOUND} "
   f"({sum(1 for r in big if -r[0] > cap)} fields checked)")
ok(len(closed) > len(tau4),
   f"POST-HOC C  the principal route reaches more of the capped range "
   f"than the tau route's upper bound ({len(closed)} against {len(tau4)})")

print()
print(f"{sum(PASS)}/{len(PASS)} checks pass")
if not all(PASS):
    sys.exit(1)
