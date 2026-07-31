"""Does the eigenvalue fingerprint survive the powered rungs?

THE QUESTION. The squarefree distinctness theorem (see
explore_spectral_theorem.py) kills a rational per-channel difference of
class cosines at p >= 5 because every nonzero class value is irrational
with one shared trace. At a powered channel that premise is FALSE by
inspection: 2cos(2*pi*c/8) is rational at three classes (c = 0, 2, 4:
values 2, 0, -2) and 2cos(2*pi*c/9) at two (c = 0, 3: values 2, -1), so
channel 8 alone carries nonzero rational pair differences and the
"rational forces equal" step fails inside one channel. Distinctness for
the powered rung 8 * 9 * 25 * 49 * 11 * 13 * 17 (the k = 7 powered ring;
crt.py powered_ring) then rests entirely on whether the per-channel
rational differences can SUM to zero across channels.

THE ARGUMENT, and why the scan below DECIDES the question rather than
probing it. (1) ISOLATION survives the powers: the moduli are still
coprime, so the Galois group of Q(zeta_N) is the product of the
per-channel groups and averaging a vanishing class-sum difference while
fixing one channel makes that channel's own difference rational — any
collision forces EVERY per-channel difference into that channel's set of
rational pair differences. (2) Those sets are finite and computable
EXACTLY: with psi_m the minimal polynomial of alpha = 2cos(2*pi/m)
(obtained by folding Phi_{p^e}(z) = Phi_p(z^(p^(e-1))) into the
z + 1/z variable, certified irreducible by Rabin's test mod a small
prime), the class value 2cos(2*pi*c/m) is the reduction of the Dickson
polynomial D_c mod psi_m, and a pair difference is rational exactly when
D_c - D_c' reduces to a CONSTANT — whose value is then the difference
itself, exactly. (3) The converse is free: per-channel differences are
realized independently (one pair of classes per channel, CRT), so a
choice of realized rational differences, not all zero, summing to zero
IS an explicit eigenvalue collision, no further check needed. So the
scan's silence is a proof of distinctness for the rung and its firing
prints a genuine collision — either outcome is a closed verdict.

THE TRANSPLANT, marked: the psi/Dickson instrument is imported verbatim
from the squarefree rig. It transfers because minimal-polynomial
representation is generic — nothing in "constant reduction iff rational"
uses primality of the modulus — but the FOLD is new (Phi_{p^e} is sparse,
not all-ones) and the class range c = 0..m/2 now includes classes NOT
coprime to m, whose values live in proper subfields. Both are exercised
by the positive control before any verdict is read.

FROZEN PREDICTIONS (fixed before any code ran):
  PR1 (positive control, read FIRST): the constant-difference detector
      fires at channel 8 at exactly the pairs among classes {0, 2, 4},
      constants -2, -4, -2 (for (2,0), (4,0), (4,2)), and at channel 9
      at exactly (3, 0), constant -3. A detector that cannot fire where
      rational differences provably exist reads nothing.
  PR2 (the scan): channels 25, 49, 11, 13, 17 are SILENT — every pair
      difference reduces nonconstant. (11, 13, 17 re-run through this
      rig's own code path, cross-checking the squarefree rig.)
  PR3 (instrument identities, exact): psi_m monic of degree phi(p^e)/2;
      psi_m(2) = p (from Phi_{p^e}(1) = p, NOT p^e); psi_m irreducible
      mod a small prime q (Rabin); float cross-check
      |psi_m(2cos(2*pi/m))| < 1e-9 at every channel.
  PR4 (the verdict): over the per-channel difference sets the scan
      records, no choice with at least one nonzero entry sums to zero.
      KILL OBSERVABLE: a printed tuple (delta_8, delta_9, ..., delta_17),
      not all zero, summing to 0 — which by (3) is an explicit collision
      at the powered rung, and finding one is the MORE interesting
      outcome, not the failure.

Memory trivial (integer lists, degree <= 21); wall-clock well under a
minute. Run: python prime/code/explore_powered_fingerprint.py

FINDINGS (entered by the post-run edit; the creating write ended at the
design).

  F1 (PR3 CONFIRMED). All 7 channels: psi_m monic of degree phi(p^e)/2
      (2, 3, 10, 21, 5, 6, 8), psi_m(2) = p exactly, irreducibility
      certificates mod q = 3 (m = 8, 17) and q = 2 (the rest), float tie
      worst 9.0e-10 at m = 49 (degree 21; the rest at or under 5.4e-15).

  F2 (PR1 CONFIRMED — the detector fires where it must). Channel 8:
      constant at exactly (2,0), (4,0), (4,2) with reductions [-2], [-4],
      [-2]; channel 9: exactly (3,0), reduction [-3]. The predicted pairs,
      the predicted constants, and nothing else.

  F3 (PR2 CONFIRMED). Channels 25, 49, 11, 13, 17: constant at none,
      every pair difference nonconstant — 470 pairs scanned in all. The
      prime channels re-read silent through this rig's own fold path,
      agreeing with the squarefree scan.

  F4 (PR4 CONFIRMED — the verdict). Per-channel rational-difference
      sets [-4,-2,0,2,4], [-3,0,3], [0], [0], [0], [0], [0]; zero-sum
      choices with a nonzero entry: 0. VERDICT: DISTINCT. By the
      argument's two directions this is a closed proof for the rung:
      all 5*5*13*25*6*7*9 = 3,071,250 eigenvalue classes of the k = 7
      powered ring are distinct reals, and so are every powered
      subring's (k = 4..6, channel subsets). The whole burden sits on
      the lattice clash: channel 8's differences have magnitude 2 or 4,
      channel 9's magnitude 3, and no other channel contributes — a
      strictly thinner margin than the squarefree rung's, where every
      channel p >= 5 was killed outright.

  RUN RECORD: python prime/code/explore_powered_fingerprint.py — 0.054 s
      real, all sections green, verdict DISTINCT (the S3 print gained
      the constant-pair list before findings were read, so PR1's
      "exactly" is a printed observable rather than an inference).
      Re-run whole after the audit added S3's nonzero guard (an empty
      reduction — a within-channel collision — must abort rather than
      enter the verdict scan as a zero) and S4's class-count print
      (3,071,250 had been authored into the record before anything
      printed it): 0.049 s, same verdict, the count now an observable.
"""

from itertools import product as iproduct
from math import cos, pi

# The k = 7 powered rung's channels: prime powers, pairwise coprime.
CHANNELS = [(2, 3), (3, 2), (5, 2), (7, 2), (11, 1), (13, 1), (17, 1)]


def section(title):
    print(f"\n{'=' * 72}\n  {title}\n{'=' * 72}")


# -- integer polynomial helpers (little-endian coefficient lists) --------

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


def cyclotomic_pe(p, e):
    """Phi_{p^e}(z) = Phi_p(z^(p^(e-1))), little-endian, exact."""
    step = p ** (e - 1)
    out = [0] * ((p - 1) * step + 1)
    for j in range(p):
        out[j * step] = 1
    return out


def fold(P):
    """z^-d * P(z) for palindromic monic P of even degree 2d, written in
    x = z + 1/z: returns b_d + sum_{j=1..d} b_{d+j} D_j(x)."""
    d = (len(P) - 1) // 2
    assert P == P[::-1], "fold needs a palindromic polynomial"
    D = dickson_polys(d)
    out = [P[d]]
    for j in range(1, d + 1):
        if P[d + j]:
            out = padd(out, [P[d + j] * c for c in D[j]])
    return pnorm(out)


# -- Rabin irreducibility over F_q, exact (as in the squarefree rig) -----

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
    m = len(ps) - 1
    mq = [c % q for c in ps]
    if mq[-1] != 1:
        return False

    def frob_iter(k):
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


# -- S1: the instrument at every powered channel, exact ------------------

section("S1. psi_m FOR THE POWERED CHANNELS — fold, identities, certificates")
SMALL_Q = [q for q in range(2, 400)
           if all(q % d for d in range(2, int(q ** 0.5) + 1))]
PSI = {}
for p, e in CHANNELS:
    m = p ** e
    ps = fold(cyclotomic_pe(p, e))
    deg = (p - 1) * p ** (e - 1) // 2
    assert len(ps) - 1 == deg and ps[-1] == 1, (m, ps)
    at2 = peval_int(ps, 2)
    assert at2 == p, (m, at2)                       # PR3: psi_m(2) = p
    cert = next((q for q in SMALL_Q if q != p and rabin_irreducible(ps, q)),
                None)
    assert cert is not None, m
    flt = abs(peval_float(ps, 2 * cos(2 * pi / m)))
    assert flt < 1e-9, (m, flt)                     # PR3: float tie
    PSI[m] = (ps, dickson_polys(m // 2))
    print(f"  m={m:2d}  deg={deg:2d}  psi(2)={at2}  irreducible mod q={cert:2d}"
          f"  |psi(2cos(2pi/m))|={flt:.1e}")


# -- S2: positive control — the detector must fire at 8 and 9 ------------

section("S2. POSITIVE CONTROL — channels 8 and 9 carry rational differences")


def reduced_diff(m, c, cp):
    """D_c - D_cp reduced mod psi_m; classes c, cp in 0..m//2."""
    ps, D = PSI[m]
    return pmod(psub(D[c], D[cp]), ps)


expected = {(8, 2, 0): -2, (8, 4, 0): -4, (8, 4, 2): -2, (9, 3, 0): -3}
for (m, c, cp), want in sorted(expected.items()):
    r = reduced_diff(m, c, cp)
    got = r[0] if r else 0
    const = len(r) <= 1
    print(f"  m={m}  (c,c')=({c},{cp})  reduction={r}  "
          f"-> {'CONSTANT (fires)' if const else 'NONCONSTANT'}")
    assert const and got == want, (m, c, cp, r)


# -- S3: the full scan — every pair at every channel, exact --------------

section("S3. THE SCAN — pair differences mod psi_m, every powered channel")
DIFFS = {}
total = 0
for p, e in CHANNELS:
    m = p ** e
    consts = set()
    const_pairs = []
    pairs = 0
    for c in range(m // 2 + 1):
        for cp in range(c):
            r = reduced_diff(m, c, cp)
            pairs += 1
            if len(r) <= 1:
                v = r[0] if r else 0
                # v = 0 would be two DISTINCT classes with equal values —
                # a within-channel collision S4's nonzero test would then
                # misread as "no difference". 2cos is strictly decreasing
                # on the class range, so this cannot happen; assert it,
                # so the verdict path cannot swallow one silently.
                assert v != 0, (m, c, cp)
                consts.add(v)
                consts.add(-v)
                const_pairs.append((c, cp))
    total += pairs
    DIFFS[m] = sorted(consts)
    print(f"  m={m:2d}  pairs={pairs:3d}  constant at {const_pairs if const_pairs else 'none'}"
          f"  rational differences: {DIFFS[m] if DIFFS[m] else 'NONE'}")
print(f"\n  total pairs scanned: {total}")


# -- S4: the verdict — can the per-channel lattices sum to zero? ---------

section("S4. THE VERDICT — zero-sum choices over the recorded sets")
sets = [DIFFS[p ** e] + [0] for p, e in CHANNELS]
sets = [sorted(set(s)) for s in sets]
hits = []
for choice in iproduct(*sets):
    if any(choice) and sum(choice) == 0:
        hits.append(choice)
classes = 1
for p, e in CHANNELS:
    classes *= p ** e // 2 + 1
print(f"  channels: {[p ** e for p, e in CHANNELS]}")
print(f"  eigenvalue classes (product of m//2 + 1): {classes:,}")
print(f"  per-channel sets: {sets}")
print(f"  zero-sum choices with a nonzero entry: {len(hits)}")
for h in hits:
    print(f"    KILL: {h}")
print(f"\n  VERDICT: {'COLLISION AT THE POWERED RUNG' if hits else 'DISTINCT'}")
