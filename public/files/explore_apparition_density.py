"""The density of certificate-less windows: how often z(p) = 2 mod 4.

THE QUESTION
------------
The boundary-family criterion (explore_class_criterion.py) says: at a
constant-a window and odd prime m, the both-parity boundary class
exists iff the rank of apparition z(m) = 2 mod 4 — where it fails,
the reading gate needs comb machinery instead of a finite
certificate. So the DENSITY of {p odd prime : z(p) = 2 mod 4} per
window a measures how common the certificate-less windows are. Does
the density stabilize per a, and does a 2-adic argument derive it?

THE HAND-ATTACK (pre-engine, on paper, checkpointed before this
write)
------------------------------------------------------------------
Vocabulary: U_0 = 0, U_1 = 1, U_{n+1} = a U_n + U_{n-1};
D = a^2 + 4; alpha, beta = (a +- sqrt D)/2 the roots, alpha beta =
-1; z(p) = rank of apparition = order of gamma = alpha/beta =
-alpha^2 (p odd, p not | D). The criterion cell asks v2(z) = 1.

THE KEY REDUCTION. In a cyclic group -1 is the unique involution.
With t = v2(ord alpha) and s = v2(ord alpha^2) = max(t-1, 0):
s = 0 gives v2(z) = 1; s = 1 means alpha^2 = -(odd), so gamma has
odd order, v2(z) = 0; s >= 2 gives v2(z) = s. Hence
z = 2 mod 4 <=> v2(ord alpha) <= 1, and z odd <=> v2(ord alpha) = 2.

THE INERT LAW (exact — no density needed). For inert p not | 2D,
Frobenius gives alpha^p = beta, so alpha^{p+1} = alpha beta = -1,
forcing v2(ord alpha) = v2(p+1) + 1 exactly. Therefore:
p = 1 mod 4 -> z ODD; p = 3 mod 4 -> v2(z) = v2(p+1). [The
sentence that stood here — "inert z = 2 mod 4 iff p = 3 mod 8" —
was the slip THE EXTENSION names: p = 3 mod 8 gives v2(z) = 2,
i.e. z = 4 mod 8, and by the two laws just stated inert primes
NEVER have z = 2 mod 4.]

THE SPLIT FORCED HALF (exact). z | p - 1, so split p = 3 mod 4 has
every t <= 1: z = 2 mod 4 ALWAYS.

THE SPLIT FREE HALF (the only randomness). Split p = 1 mod 4 with
e = v2(p-1) >= 2: z = 2 mod 4 iff alpha lies in the index-2^{e-1}
subgroup {x : v2(ord x) <= 1}. Naive Kummer independence prices
this at 2^{-(e-1)}; degree collapses in Q(zeta_{2^k},
alpha^{1/2^j}) (alpha a unit of norm -1) could correct it —
observable, no prediction on the size.

THE NAIVE DENSITY. 1/4 (split forced) + 1/8 (inert p = 3 mod 8) +
(1/4) sum_{e>=2} 4^{-(e-1)} = 1/4 + 1/8 + 1/12 = 11/24. Cross-rail:
the same model prices P(z odd) = 1/3, matching the classical 2/3
density of primes dividing some Lucas number (z even) at a = 1.

FIELD ENTANGLEMENT ACROSS a. Split means (D/p) = 1, and the field
Q(sqrt D) decides whether splitting correlates with p mod 8:
a = 2 has D = 8, field Q(sqrt 2), split <=> p = +-1 mod 8 — fully
entangled; reworking the sum gives 13/24. a = 6 (D = 40, Q(sqrt 10))
mixes mod 8 with mod 5, leaving all four mod-8 classes equal among
split — generic. a = 4 shares Q(sqrt 5) with golden and its alpha
is phi^3, an odd power of phi. Every other a <= 8 has D prime or
4 x prime with the character independent of mod 8 — generic.

THE DESIGN (predictions frozen before the run)
------------------------------------------------------------------
D0  Positive controls: (i) brute z(p) (iterate U mod p) for p < 100,
    a in {1, 2, 3}, against the fast pipeline's v2(z); (ii) the
    golden criterion echoes explore_class_criterion.py:
    verdict(z = 2 mod 4) at
    m = 3, 5, 7 is NO; m = 11 YES; m = 13: z(13) = 7, odd -> NO.
    PREDICTION: green.
D1  The exact laws as running asserts on EVERY scanned prime:
    split p = 3 mod 4 -> v2(z) = 1; inert p = 1 mod 4 -> v2(z) = 0;
    inert p = 3 mod 4 -> v2(z) = v2(p+1). PREDICTION: no violation
    (they are theorems; a violation is a rig bug).
D2  The scan: a = 1..8, odd primes p <= 10^6, p not | D, bucket
    v2(z) in {0, 1, >=2} overall and by split/inert, with
    checkpoints at 10^4, 10^5, 10^6. PREDICTION: stabilization —
    |density(10^5) - density(10^6)| < 0.01 per a (KILL-SHAPE
    observable: the drift column).
D3  The model: per-a total density of z = 2 mod 4 against the
    prediction — a = 2: 13/24 = 0.5417; all other a: 11/24 =
    0.4583. PREDICTION: agreement within 0.01. OBSERVABLE, no
    prediction: the split-free-half residual (measured
    P(v2(ord alpha) <= 1 | split, e >= 2) against naive 1/3 —
    the Kummer correction column).

THE EXTENSION (design frozen before the second run). The first
run's D3 prediction FAILED — measured totals sit at 1/3 (a = 2:
0.2922), not 11/24 — and reading the prints against the hand-attack
found the slip in the frozen derivation itself, not the rig: the
inert column conflated v2(z) = 2 with z = 2 mod 4. Inert p = 3
mod 4 has v2(z) = v2(p+1) >= 2, never 1, so INERT PRIMES NEVER
CARRY THE CLASS and their 1/8 was phantom. Corrected totals:
generic 1/4 + (1/4)(1/3) = 1/3; a = 2: 1/4 + (1/4)(1/6) = 7/24.
The a = 2 deviation exists because Q(sqrt 2) ties splitting to
p mod 8, and that happens iff the squarefree kernel of a^2 + 4 is
exactly 2, i.e. a^2 + 4 = 8 m^2, i.e. a = 2k with k^2 + 1 = 2m^2 —
the Pell family a = 2, 14, 82, 478, ... For every other a the four
mod-8 classes are equidistributed among split primes and the
density is generic.
D4  The Pell-family check: windows a in {10, 12, 14, 82}, same
    scan. PREDICTION: a = 14 and a = 82 (kernels 2) -> 7/24 =
    0.2917 with split-free 1/6; a = 10 (kernel 26) and a = 12
    (kernel 37) -> 1/3 with split-free 1/3.

RESOURCE: pure Python, no numpy; sieve to 10^6 is a bytearray;
everything else O(log p) per prime. Estimate 2-5 min, < 50 MB.

FINDINGS (entered after the runs; both runs' full tables below)
------------------------------------------------------------------
THE DENSITY IS 1/3 — AND THE FIRST FROZEN TOTAL WAS WRONG. D0 and
the D1 asserts ran green (70 brute cells, the criterion echoes, the
exact laws at every prime x 12 windows), and D3 then MISSED at
every window: the naive 11/24 was an arithmetic slip in the frozen
derivation — the inert bookkeeping conflated v2(z) = 2 with z = 2 mod
4. Since inert p = 3 mod 4 has v2(z) = v2(p+1) >= 2 and inert
p = 1 mod 4 has z odd, INERT PRIMES NEVER CARRY THE CLASS: the
criterion's YES set is a subset of the split primes. Corrected
derivation, matching every scanned column to within 2e-3 (inside
sampling noise at 78497 primes):

  P(z = 2 mod 4) = P(split, p = 3 mod 4)   [forced YES, theorem]
                 + P(split, p = 1 mod 4) x P(v2(ord alpha) <= 1)
                 = 1/4 + (1/4)(1/3) = 1/3          generic a
                 = 1/4 + (1/4)(1/6) = 7/24         Pell family,

the Pell family being a^2 + 4 = 8 m^2 (a = 2, 14, 82, 478, ...),
where Q(sqrt 2) ties splitting to p mod 8 (split <=> p = +-1 mod
8, so the free half starts at e >= 3). Generic windows print the
uniform thirds (odd, 2 mod 4, 0 mod 4) = (1/3, 1/3, 1/3); the
Pell rows print (7/24, 7/24, 5/12). Drift 10^5 -> 10^6 is <= 0.002
everywhere: stabilized, the kill-shape did not fire.

TIERS. The 2-adic reduction, the inert law, and the split-forced
half: THEOREMS (proved above, asserted at every scanned prime).
The density VALUES: pattern (12 windows, odd primes to 10^6; the
one unproved ingredient is Kummer independence at the split free
half — measured 0.3331/0.1670 against naive 1/3 and 1/6, no
visible correction at this bound). [Settled since: the Kummer
independence is a proved theorem — Hasse's density method, run by
Lagarias (1985) and Moree (1996, Theorem 3), the degrees full
because N(alpha) = -1 is not a square in real Q(sqrt D) — so the
densities are theorems; the per-layer fingerprint is verified in
explore_kummer_layers.py.]

THE ODD-POWER SHARING LAW (theorem, explains the identical rows).
v2(ord x^j) = v2(ord x) for odd j, so windows whose alpha are odd
powers of one unit share v2(z) at EVERY prime: a = 2, 14, 82 have
alpha = (1+sqrt2)^{1,3,5} and print identical rows to 4 decimals
(0.2922 / 0.2911 / 0.4168 / 0.1670); a = 1 and a = 4 (alpha =
phi, phi^3) likewise (0.3337 / 0.3332 / 0.3330 / 0.3331).

THE ROADMAP'S ANSWER. Certificate-less windows are the MAJORITY:
at a generic constant-a window, 2/3 of odd primes m have no
both-parity boundary class and the gate needs comb machinery;
on the Pell family the certificate-less share rises to 17/24.
The golden obstructions at m = 3, 5, 7 were not bad luck.

RUN RECORD (python prime/code/explore_apparition_density.py,
~15 s; the two tables verbatim):

odd primes to 1000000: 78497
D0i  brute z vs pipeline v2, p < 100, a in {1,2,3}: 70 cells agree
D0ii golden criterion echo: m=3: z=4 NO; m=5: z=5 NO; m=7: z=8 NO;
     m=11: z=10 YES; m=13: z=7 NO (all as expected)

D1-D3 scan: odd primes to 10^6 per window
 a   D |   total    pred   drift |   z odd   2mod4   0mod4 | sp-free   naive
 1   5 |  0.3337  0.4583  0.0007 |  0.3332  0.3337  0.3330 |  0.3331  0.3333
 2   8 |  0.2922  0.5417  0.0013 |  0.2911  0.2922  0.4168 |  0.1670  0.3333
 3  13 |  0.3335  0.4583  0.0007 |  0.3328  0.3335  0.3337 |  0.3323  0.3333
 4  20 |  0.3337  0.4583  0.0007 |  0.3332  0.3337  0.3330 |  0.3331  0.3333
 5  29 |  0.3333  0.4583  0.0000 |  0.3332  0.3333  0.3335 |  0.3303  0.3333
 6  40 |  0.3331  0.4583  0.0014 |  0.3334  0.3331  0.3335 |  0.3317  0.3333
 7  53 |  0.3332  0.4583  0.0004 |  0.3334  0.3332  0.3333 |  0.3311  0.3333
 8  68 |  0.3334  0.4583  0.0017 |  0.3332  0.3334  0.3334 |  0.3343  0.3333

D4 Pell-family scan: odd primes to 10^6 per window
 a   D |   total    pred   drift |   z odd   2mod4   0mod4 | sp-free   naive
10 104 |  0.3326  0.3333  0.0006 |  0.3334  0.3326  0.3341 |  0.3314  0.3333
12 148 |  0.3342  0.3333  0.0008 |  0.3334  0.3342  0.3324 |  0.3335  0.3333
14 200 |  0.2922  0.2917  0.0012 |  0.2911  0.2922  0.4168 |  0.1670  0.3333
82 6728 |  0.2922  0.2917  0.0012 |  0.2911  0.2922  0.4168 |  0.1670  0.3333

(the D3 'pred' column in run 1 is the first frozen prediction, kept
as the record of the miss; the corrected values are 1/3 and 7/24.)
"""

import sys

BOUND = 10**6
CHECKPOINTS = (10**4, 10**5, 10**6)
WINDOWS = (1, 2, 3, 4, 5, 6, 7, 8)


def sieve_primes(n):
    mark = bytearray([1]) * (n + 1)
    mark[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if mark[i]:
            mark[i * i :: i] = bytearray(len(mark[i * i :: i]))
    return [i for i in range(3, n + 1) if mark[i]]  # odd primes only


def u_pair(a, n, p):
    """(U_n, U_{n+1}) mod p by fast doubling."""
    u, v = 0, 1  # U_0, U_1
    for bit in bin(n)[2:]:
        # double: k -> 2k
        uu = (u * ((2 * v - a * u) % p)) % p  # U_{2k} = U_k(2U_{k+1}-aU_k)
        vv = (u * u + v * v) % p              # U_{2k+1}
        u, v = uu, vv
        if bit == "1":
            u, v = v, (a * v + u) % p
    return u, v


def v2_of_z(a, p):
    """v2(z(p)) for odd prime p not dividing D = a*a+4."""
    D = a * a + 4
    chi = pow(D, (p - 1) // 2, p)
    chi = 1 if chi == 1 else -1  # p not | D so chi is +-1
    N = p - chi
    e = (N & -N).bit_length() - 1
    m = N >> e
    u, v = u_pair(a, m, p)
    if u == 0:
        return 0, chi
    # square up: track (U_n, L_n), n = m odd at start
    L = (2 * v - a * u) % p
    sign = -1  # (-1)^n for n odd
    for j in range(1, e + 1):
        u = (u * L) % p
        L = (L * L - 2 * sign) % p
        sign = 1
        if u == 0:
            return j, chi
    raise AssertionError(f"z does not divide N: a={a} p={p}")


def brute_z(a, p, cap=None):
    """Least n >= 1 with U_n = 0 mod p, by iteration."""
    u, v = 0, 1
    n = 0
    cap = cap or 4 * p
    while n < cap:
        u, v = v, (a * v + u) % p
        n += 1
        if u == 0:
            return n
    raise AssertionError(f"no apparition below {cap}: a={a} p={p}")


def d0_controls(primes_small):
    print("D0i  brute z vs pipeline v2, p < 100, a in {1,2,3}:")
    checked = 0
    for a in (1, 2, 3):
        D = a * a + 4
        for p in primes_small:
            if p >= 100 or D % p == 0:
                continue
            z = brute_z(a, p)
            v2b = (z & -z).bit_length() - 1
            v2f, _ = v2_of_z(a, p)
            assert v2b == v2f, (a, p, z, v2b, v2f)
            checked += 1
    print(f"     {checked} cells agree")
    print("D0ii golden criterion echo (explore_class_criterion.py cells):")
    for m, want in ((3, "NO"), (5, "NO"), (7, "NO"), (11, "YES"), (13, "NO")):
        z = brute_z(1, m)
        got = "YES" if z % 4 == 2 else "NO"
        print(f"     m={m}: z={z}, class {got} (expected {want})")
        assert got == want, (m, z)


def scan(primes, windows=WINDOWS, predfn=None, title="D1-D3"):
    if predfn is None:
        predfn = lambda a: 13 / 24 if a == 2 else 11 / 24
    header = (
        f"{'a':>2} {'D':>3} | {'total':>7} {'pred':>7} {'drift':>7} | "
        f"{'z odd':>7} {'2mod4':>7} {'0mod4':>7} | "
        f"{'sp-free':>7} {'naive':>7} | asserts"
    )
    print(f"\n{title} scan: odd primes to 10^6 per window")
    print(header)
    print("-" * len(header))
    for a in windows:
        D = a * a + 4
        n_tot = 0
        buckets = [0, 0, 0]  # v2 = 0, 1, >=2
        free_n = free_hit = 0  # the split free half: p = 1 mod 4, hits of v2(z) == 1
        checkpoint_dens = {}
        for p in primes:
            if D % p == 0:
                continue
            v2z, chi = v2_of_z(a, p)
            n_tot += 1
            buckets[min(v2z, 2)] += 1
            # exact-law asserts (D1)
            if chi == 1 and p % 4 == 3:
                assert v2z == 1, ("split-forced", a, p, v2z)
            if chi == -1:
                if p % 4 == 1:
                    assert v2z == 0, ("inert-odd", a, p, v2z)
                else:
                    v2p1 = ((p + 1) & -(p + 1)).bit_length() - 1
                    assert v2z == v2p1, ("inert-law", a, p, v2z, v2p1)
            if chi == 1 and p % 4 == 1:
                free_n += 1
                free_hit += v2z == 1
            for c in CHECKPOINTS:
                if p <= c:
                    checkpoint_dens.setdefault(c, [0, 0])
                    checkpoint_dens[c][0] += v2z == 1
                    checkpoint_dens[c][1] += 1
        dens = buckets[1] / n_tot
        pred = predfn(a)
        d5 = checkpoint_dens[10**5][0] / checkpoint_dens[10**5][1]
        drift = abs(d5 - dens)
        free = free_hit / free_n if free_n else float("nan")
        print(
            f"{a:>2} {D:>3} | {dens:7.4f} {pred:7.4f} {drift:7.4f} | "
            f"{buckets[0]/n_tot:7.4f} {dens:7.4f} {buckets[2]/n_tot:7.4f} | "
            f"{free:7.4f} {1/3:7.4f} | ok"
        )
        sys.stdout.flush()


def main():
    primes = sieve_primes(BOUND)
    print(f"odd primes to {BOUND}: {len(primes)}")
    d0_controls([p for p in primes if p < 100])
    scan(primes)
    scan(
        primes,
        windows=(10, 12, 14, 82),
        predfn=lambda a: 7 / 24 if a in (14, 82) else 1 / 3,
        title="D4 Pell-family",
    )


if __name__ == "__main__":
    main()
