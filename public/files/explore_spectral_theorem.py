"""The spectral fingerprint assembled: is the class-distinctness rule a theorem?

THE QUESTION. Eigenvalue classes of the squarefree rung are tuples
(c_1, ..., c_k) with 0 <= c_i <= floor(p_i/2), read as the real number
sum_i 2cos(2*pi*c_i/p_i). The distinctness of all such reals is filed as a
rule, exhaustive at k = 3..8, with a float ceiling near k = 10 (the minimum
separation falls ~2 orders per rung on average, unevenly). Two halves of a mechanism exist:
real-cyclotomic linear disjointness settles every channel with p >= 5, and
channels 2 and 3 — whose cosines are rational — leave differences in 4Z and
3Z that cannot cancel. This rig checks the assembled argument's one
computational load-bearing step in EXACT integer arithmetic, with no float
anywhere in the verdict path, so the check has no precision ceiling at all.

THE ARGUMENT BEING CHECKED (assembled on paper before this rig was written).
Suppose two class tuples give one sum. (1) ISOLATION: average the vanishing
difference over the Galois group of Q(zeta_N), N = prod p_i, fixing channel
i — the group is the product of the per-channel groups, so the average fixes
channel i's term and replaces every other channel's by a rational trace;
hence each per-channel difference delta_i = 2cos(2*pi*c_i/p_i) -
2cos(2*pi*c_i'/p_i) is RATIONAL. (2) RATIONAL FORCES ZERO at p >= 5: for
c, c' nonzero, Tr(2cos(2*pi*c/p)) = -2 independently of c, so a rational
delta equals Tr(delta)/(p-1) = 0, and 2cos is strictly decreasing on the
class range, forcing c = c'; for c' = 0 a rational delta would make
2cos(2*pi*c/p) itself rational, impossible at degree (p-1)/2 >= 2. (3) THE
SMALL CHANNELS: differences at p = 2 lie in {0, +-4}, at p = 3 in
{0, +-3}; a vanishing sum needs an element of 4Z meeting 3Z of magnitude
at most 4, so both are 0. Injectivity for ALL k, uniformly.

WHAT EXACT ARITHMETIC CAN CHECK. Step (2) is equivalent to a statement
about integer polynomials. Let psi_p be the monic integer polynomial of
degree m = (p-1)/2 whose roots are 2cos(2*pi*c/p), c = 1..m; it comes from
the cyclotomic identity z^(-m) * Phi_p(z) = 1 + sum_{j=1..m} (z^j + z^-j),
i.e. psi_p(x) = 1 + sum_{j=1..m} D_j(x) where D_0 = 2, D_1 = x,
D_{j+1} = x*D_j - D_{j-1} (so D_j(z + 1/z) = z^j + z^-j). In
Z[x]/psi_p(x), the class value 2cos(2*pi*c/p) IS the reduction of D_c.
BECAUSE psi_p is the MINIMAL polynomial of 2cos(2*pi/p) — certified
in-rig, S1b: monic and irreducible mod one small prime q by Rabin's test,
which suffices over Q — a rational difference of two distinct class
values, the recorded kill-shape, is exactly a pair c' < c whose reduced
difference D_c - D_{c'} mod psi_p is a CONSTANT polynomial (a reducible
psi_p could hide a rational value behind a nonconstant reduction, so the
certificate is load-bearing, not decoration). Scanning every pair at
every channel is pure integer arithmetic: no separation to measure, no
precision to run out of.

FROZEN PREDICTIONS (fixed before any code ran):
  PR1 (positive control, read FIRST): the constant-difference detector
      FIRES at the small channels — p = 2 gives the constant 4, p = 3
      gives the constant 3 (reduce 2 - x mod x + 1). A detector that
      cannot fire where rational differences provably exist reads nothing.
  PR2 (the kill-scan): at every tower prime 5 <= p <= 53 (k = 16), every
      one of the C(m+1, 2) pair differences reduces to a NONCONSTANT
      polynomial mod psi_p. KILL OBSERVABLE: a printed triple (p, c, c')
      with a constant reduced difference. If it prints, the theorem
      promotion is dead and k = 3..8 stays the honest claim.
  PR3 (identities the argument leans on, exact): psi_p(2) = p (from
      Phi_p(1) = p), and the x^(m-1) coefficient of psi_p is 1 (the trace
      sum_{c=1..m} 2cos(2*pi*c/p) = -1), at every odd tower prime.
  PR4 (instrument cross-check, float allowed HERE only): at p <= 13,
      psi_p evaluated at 2cos(2*pi*c/p) is below 1e-9 for every c = 1..m,
      tying the integer polynomial to the measured object.

Memory trivial (integer lists, degree <= 26); wall-clock well under a
minute. Run: python prime/code/explore_spectral_theorem.py

FINDINGS (entered by the post-run edit; the creating write ended at the
design, with a pre-authored findings block stripped BEFORE the first run).

  F1 (PR3, PR4 CONFIRMED). All 15 odd tower primes through 53: psi_p
      monic of degree (p-1)/2, psi_p(2) = p exactly, x^(m-1) coefficient
      1 exactly. Float cross-check at p <= 13: max |psi_p(2cos(2 pi c/p))|
      = 3.6e-15. The instrument is the object.

  F2 (PR1 CONFIRMED — the detector fires where it must). p = 2: class
      values 2, -2, difference the constant 4. p = 3: D_0 - D_1 reduces
      mod psi_3 to [3] — CONSTANT, through the same code path the
      kill-scan reads. A silent scan is a real silence, not a blind
      instrument.

  F1b (the certificates, added by the audit round that found the scan's
      soundness leaning on uncertified irreducibility). All 14 scanned
      channels certify: psi_p irreducible mod q = 2 (ten channels), q = 3
      (17, 31, 43), q = 7 (41) — Rabin exact, monic, so irreducible over
      Q and psi_p is the minimal polynomial the iff needs. p = 3 needs no
      certificate: its positive-control direction (constant reduction
      implies rational) is evaluation, irreducibility-free.

  F3 (PR2 CONFIRMED — the kill-shape is silent at every channel, exactly).
      All 14 channels p = 5..53, all 1656 pair differences: every
      reduction NONCONSTANT, KILLS: 0. The largest scan (p = 53, 351
      pairs) is integer-exact; no precision was consumed anywhere in the
      verdict path. With steps (1) and (3) holding on paper, this was the
      last computational load-bearing fact: the distinctness rule
      assembles into a THEOREM for all k. The per-channel scan replaces
      the exponential product enumeration, which is why the float ceiling
      near k = 10 was never mathematical.

  F4 (the small-channel clash, exhaustive). Over d2 in {0, +-4} and d3 in
      {0, +-3} the only pair summing to zero is (0, 0) — step (3) checked
      by enumeration on top of its one-line proof.

  F5 (assembly control, float, k = 5). 288 class sums enumerate to 288
      distinct reals (expected 2*2*3*4*6 = 288), min separation 2.2e-05 —
      the exact verdict and the measured object agree where both can see.

  RUN RECORD: python prime/code/explore_spectral_theorem.py — 0.031 s
      real, all sections green, VERDICT: kill-shape silent through p = 53.
      Re-run whole after the audit added S1b: 0.065 s, all sections green,
      the same verdict with the certificates now under it.
"""

from math import cos, pi

TOWER = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]


def section(title):
    print(f"\n{'=' * 72}\n  {title}\n{'=' * 72}")


# ── integer polynomial helpers (little-endian coefficient lists) ─────────

def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(n)]


def psub(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
            for i in range(n)]


def pnorm(a):
    while a and a[-1] == 0:
        a = a[:-1]
    return a


def pmod(a, m):
    """Reduce a mod monic m, exact integer division steps."""
    a = list(a)
    dm = len(m) - 1
    while len(pnorm(a)) - 1 >= dm and pnorm(a):
        a = pnorm(a)
        lead, da = a[-1], len(a) - 1
        # subtract lead * x^(da-dm) * m
        for i, c in enumerate(m):
            a[da - dm + i] -= lead * c
    return pnorm(a)


def peval_int(a, x):
    v = 0
    for c in reversed(a):
        v = v * x + c
    return v


def peval_float(a, x):
    v = 0.0
    for c in reversed(a):
        v = v * x + c
    return v


def dickson_polys(m):
    """D_0..D_m with D_j(z + 1/z) = z^j + z^-j."""
    D = [[2], [0, 1]]
    for _ in range(2, m + 1):
        D.append(pnorm(psub([0] + D[-1], D[-2])))
    return D[:m + 1]


def psi(p):
    """Monic integer polynomial with roots 2cos(2*pi*c/p), c = 1..(p-1)/2."""
    m = (p - 1) // 2
    D = dickson_polys(m)
    out = [1]
    for j in range(1, m + 1):
        out = padd(out, D[j])
    return pnorm(out), D


# ── S1: the instrument, exactly ──────────────────────────────────────────

section("S1. psi_p FOR THE ODD TOWER PRIMES — exact identities")
PSI = {}
for p in TOWER[1:]:
    ps, D = psi(p)
    PSI[p] = (ps, D)
    m = (p - 1) // 2
    assert len(ps) - 1 == m and ps[-1] == 1, (p, ps)
    at2 = peval_int(ps, 2)
    subl = ps[m - 1]
    print(f"  p={p:2d}  deg={m:2d}  psi(2)={at2:3d}  coeff[x^{m-1}]={subl}")
    assert at2 == p, (p, at2)          # PR3: psi_p(2) = Phi_p(1) = p
    assert subl == 1, (p, subl)        # PR3: trace of the roots is -1

print("\n  float cross-check (PR4), p <= 13:")
worst = 0.0
for p in [3, 5, 7, 11, 13]:
    ps, _ = PSI[p]
    for c in range(1, (p - 1) // 2 + 1):
        r = abs(peval_float(ps, 2 * cos(2 * pi * c / p)))
        worst = max(worst, r)
print(f"    max |psi_p(2cos(2 pi c/p))| = {worst:.1e}")
assert worst < 1e-9


# ── S1b: certify psi_p IRREDUCIBLE, exactly — the scan's soundness ──────
# The kill-scan's verdict direction (a rational pair difference forces a
# CONSTANT reduction) holds because psi_p is the MINIMAL polynomial of
# 2cos(2*pi/p); a reducible psi_p could hide a rational value behind a
# nonconstant reduction. Monic + irreducible mod one prime q suffices for
# irreducibility over Q, and Rabin's test mod q is exact integers.

section("S1b. IRREDUCIBILITY CERTIFICATES — psi_p mod q, Rabin, exact")


def pmulmod(a, b, mod, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca:
            for j, cb in enumerate(b):
                out[i + j] = (out[i + j] + ca * cb) % q
    return [c % q for c in pmod(out, mod)]


def ppowmod(base, e, mod, q):
    r = [1]
    while e:
        if e & 1:
            r = pmulmod(r, base, mod, q)
        base = pmulmod(base, base, mod, q)
        e >>= 1
    return r


def pgcd_fq(a, b, q):
    a = [c % q for c in pnorm(a)]
    b = [c % q for c in pnorm(b)]
    while pnorm(b):
        b = pnorm(b)
        inv = pow(b[-1], q - 2, q)
        b = [c * inv % q for c in b]
        a = [c % q for c in pmod(a, b)]
        a, b = b, a
    return pnorm(a)


def rabin_irreducible(ps, q):
    """psi monic; irreducible over F_q iff x^(q^m) = x and for each prime
    l | m, gcd(x^(q^(m/l)) - x, psi) = 1."""
    m = len(ps) - 1
    mq = [c % q for c in ps]
    if mq[-1] != 1:
        return False

    def frob_iter(k):                  # x^(q^k) mod (psi, q)
        t = [0, 1]
        for _ in range(k):
            t = ppowmod(t, q, mq, q)
        return t

    if pnorm(psub(frob_iter(m), [0, 1])):
        return False
    ls = {l for l in range(2, m + 1) if m % l == 0
          and all(l % d for d in range(2, l))}
    for l in ls:
        g = pgcd_fq(psub(frob_iter(m // l), [0, 1]), mq, q)
        if len(g) != 1:
            return False
    return True


SMALL_Q = [q for q in range(2, 400)
           if all(q % d for d in range(2, int(q ** 0.5) + 1))]
for p in TOWER[2:]:
    ps, _ = PSI[p]
    cert = next((q for q in SMALL_Q if q != p and rabin_irreducible(ps, q)),
                None)
    print(f"  p={p:2d}  psi_p irreducible mod q = {cert}")
    assert cert is not None, p


# ── S2: positive control — the detector must fire at p = 2 and 3 ────────

section("S2. POSITIVE CONTROL — rational differences exist at p = 2, 3")


def reduced_diff(p, c, cp):
    """D_c - D_cp reduced mod psi_p; classes c, cp in 0..(p-1)/2."""
    ps, D = PSI[p]
    return pmod(psub(D[c], D[cp]), ps)


# p = 2: values 2cos(0) = 2 and 2cos(pi) = -2 live in Q; difference 4.
d2 = 2 - (-2)
print(f"  p= 2: class values 2, -2   difference = {d2}  -> CONSTANT (fires)")
assert d2 == 4

# p = 3 through the SAME code path the kill-scan uses:
r = reduced_diff(3, 0, 1)
const = len(r) <= 1
print(f"  p= 3: (c,c')=(0,1)  D_0 - D_1 mod psi_3 = {r}  "
      f"-> {'CONSTANT (fires)' if const else 'nonconstant'}")
assert const and r == [3]


# ── S3: the kill-scan — every pair at every channel p >= 5, exact ───────

section("S3. THE KILL-SCAN — pair differences mod psi_p, p = 5..53")
kills = []
total = 0
for p in TOWER[2:]:
    m = (p - 1) // 2
    pairs = 0
    for c in range(m + 1):
        for cp in range(c):
            r = reduced_diff(p, c, cp)
            pairs += 1
            if len(r) <= 1:            # constant (or zero): the kill-shape
                kills.append((p, c, cp, r))
    total += pairs
    print(f"  p={p:2d}  pairs={pairs:3d}  constant reductions="
          f"{sum(1 for k in kills if k[0] == p)}")
print(f"\n  total pairs scanned: {total}   KILLS: {len(kills)}")
for k in kills:
    print(f"    KILL: p={k[0]} (c,c')=({k[1]},{k[2]}) reduction={k[3]}")
assert total == sum(((p - 1) // 2 + 1) * ((p - 1) // 2) // 2
                    for p in TOWER[2:])


# ── S4: the small-channel clash, exhaustive on top of the one-liner ─────

section("S4. CHANNELS 2 AND 3 — 4Z meets 3Z at nothing reachable")
sols = [(a, b) for a in (0, 4, -4) for b in (0, 3, -3) if a + b == 0]
print(f"  pairs (d2, d3) with d2 + d3 = 0: {sols}")
assert sols == [(0, 0)]


# ── S5: assembly cross-check at k = 5 (float, control only) ─────────────

section("S5. ASSEMBLY CONTROL — k = 5 enumeration agrees with the verdict")
from itertools import product as iproduct
ps5 = TOWER[:5]
sums = sorted(sum(2 * cos(2 * pi * c / p) for c, p in zip(t, ps5))
              for t in iproduct(*[range(p // 2 + 1) for p in ps5]))
expected = 1
for p in ps5:
    expected *= p // 2 + 1
minsep = min(b - a for a, b in zip(sums, sums[1:]))
print(f"  classes = {len(sums)} (expected {expected}); "
      f"min separation = {minsep:.1e}")
assert len(sums) == expected and minsep > 0


section("VERDICT")
if kills:
    print("  KILL-SHAPE FIRED — the rule stays a rule at k = 3..8.")
else:
    print("  Kill-shape silent at every channel through p = 53, exactly.")
    print("  Steps (1) and (3) hold on paper; step (2)'s computational")
    print("  content is exact. The fingerprint assembles for all k.")
