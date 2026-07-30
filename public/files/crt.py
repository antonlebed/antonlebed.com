"""CRT arithmetic library for the primorial tower — rings Z/p_k#.

Parametric: a Ring is any product of coprime prime-power moduli, but the
canonical objects are the squarefree tower rungs, where every channel is a
prime field. RAD = Z/510510 (k=7) is the reference rung; RUNG5 = Z/9699690
(k=8) is the next. Provides:
  - Ring constructors, indexed by the rung k: squarefree, and the
    prime-power variant that raises the first four channels
  - CRT encode/decode (decompose <-> reconstruct)
  - Per-channel arithmetic on CRT tuples
  - ECC: tower split (first k-3 data, last 3 parity), syndrome,
    detection, correction — MDS d=4, rate (k-3)/k for k >= 7
  - Idempotents, coupling, eigenvalues, seed-flower (-chi)

Usage:
    from crt import RAD_RING, encode, decode, ecc_syndrome, ecc_correct
    t = encode(42, RAD_RING)       # -> (0, 0, 2, 0, 9, 3, 8)
    n = decode(t, RAD_RING)        # -> 42
    s = ecc_syndrome(t, RAD_RING)  # -> (0, 0, 0) if valid codeword

Run: python prime/code/crt.py  (self-test)
"""

from math import gcd, prod, sin, cos, pi, isqrt
from functools import reduce


# ═══════════════════════════════════════════════════════════════════════
# NUMBER THEORY PRIMITIVES
# ═══════════════════════════════════════════════════════════════════════

def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_list(xs):
    return reduce(lcm, xs, 1)


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def euler_phi(n):
    result = n
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def carmichael_lambda(n):
    factors = factorize(n)
    lambdas = []
    for p, a in factors.items():
        if p == 2:
            if a <= 2:
                lambdas.append(2 ** (a - 1))
            else:
                lambdas.append(2 ** (a - 2))
        else:
            lambdas.append(p ** (a - 1) * (p - 1))
    return lcm_list(lambdas) if lambdas else 1


def multiplicative_order(a, n):
    if gcd(a, n) != 1:
        return None
    order = 1
    current = a % n
    while current != 1:
        current = (current * a) % n
        order += 1
        if order > n:
            return None
    return order


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1


def mod_inverse(a, m):
    g, x, _ = extended_gcd(a % m, m)
    if g != 1:
        raise ValueError(f"{a} has no inverse mod {m}")
    return x % m


def primes_up_to(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


# ═══════════════════════════════════════════════════════════════════════
# RING DEFINITION
# ═══════════════════════════════════════════════════════════════════════

PRIMES_7 = (2, 3, 5, 7, 11, 13, 17)


class Ring:
    """A CRT ring Z/NZ defined by prime-power moduli.

    data_channels/parity_channels default to the tower split: for k >= 7,
    the first k-3 channels are data and the last 3 are parity (MDS d=4,
    rate (k-3)/k). Rings below k=7 carry no parity by design. Pass n_data
    to override."""

    def __init__(self, name, primes, exponents, n_data=None):
        self.name = name
        self.primes = tuple(primes)
        self.exponents = tuple(exponents)
        self.moduli = tuple(p ** e for p, e in zip(primes, exponents))
        self.N = prod(self.moduli)
        self.k = len(primes)
        self.phi = euler_phi(self.N)
        self.lam = carmichael_lambda(self.N)
        self.num_idempotents = 2 ** self.k
        self.n_data = n_data

        self._crt_coeffs = None

    @property
    def crt_coefficients(self):
        """Precompute CRT reconstruction coefficients (lazy)."""
        if self._crt_coeffs is None:
            coeffs = []
            for i, qi in enumerate(self.moduli):
                Mi = self.N // qi
                yi = mod_inverse(Mi, qi)
                coeffs.append((Mi * yi) % self.N)
            self._crt_coeffs = tuple(coeffs)
        return self._crt_coeffs

    @property
    def data_channels(self):
        if self.n_data is not None:
            return tuple(range(self.n_data))
        if self.k >= 7:
            return tuple(range(self.k - 3))
        return tuple(range(self.k))

    @property
    def parity_channels(self):
        return tuple(i for i in range(self.k) if i not in self.data_channels)

    def __repr__(self):
        return f"Ring({self.name}, N={self.N}, k={self.k})"


# The first primes, in order — the tower's channels.
TOWER_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def primorial_ring(k):
    """Rung k of the squarefree tower: Z/(p_1 ... p_k), every channel a
    prime field. This is the canonical family — a Ring is named by its rung
    index and nothing else, so k is always the TOTAL channel count.

    Both constructors RAISE past the end of TOWER_PRIMES rather than
    truncating. A slice would return rung 12 for any larger k, quietly, and
    a caller asking for a rung it cannot have deserves the error: the fixed
    ring constants these replaced could not have this failure, so it arrived
    with the parameterization.
    """
    if not 1 <= k <= len(TOWER_PRIMES):
        raise ValueError(f"rung {k} outside 1..{len(TOWER_PRIMES)}")
    return Ring(f"k={k}", TOWER_PRIMES[:k], (1,) * k)


def powered_ring(k):
    """The prime-power variant of rung k: the same k primes, but the first
    four channels raised to (3, 2, 2, 2). Channels 2, 3, 5, 7 stop being
    fields, so the ring stops being a meadow — which is the only reason this
    family is kept.

    Requires k >= 4, and enforces it. Below 4 the exponent tuple is LONGER
    than the prime tuple, and Ring pairs them with zip, so the ring builds
    with a correct N and an exponents field disagreeing with its own primes
    and with its own k — a wrong object rather than a failure.
    """
    if not 4 <= k <= len(TOWER_PRIMES):
        raise ValueError(f"powered rung {k} outside 4..{len(TOWER_PRIMES)}")
    return Ring(f"k={k} powered", TOWER_PRIMES[:k], (3, 2, 2, 2) + (1,) * (k - 4))


# The two rungs the reference tables are written against. They carry their
# own names because the tables and the tower documentation cite them by
# name; every other rung is referred to by its index alone.
RAD_RING   = Ring("RAD",   TOWER_PRIMES[:7], (1,) * 7)   # Z/510510
RUNG5_RING = Ring("RUNG5", TOWER_PRIMES[:8], (1,) * 8)   # Z/9699690


# ═══════════════════════════════════════════════════════════════════════
# CRT ENCODE / DECODE
# ═══════════════════════════════════════════════════════════════════════

def encode(n, ring):
    """Decompose n into CRT residues: n -> (n mod q1, n mod q2, ...)."""
    return tuple(n % q for q in ring.moduli)


def decode(residues, ring):
    """Reconstruct n from CRT residues using precomputed coefficients."""
    if len(residues) != ring.k:
        raise ValueError(f"Expected {ring.k} residues, got {len(residues)}")
    return sum(r * c for r, c in zip(residues, ring.crt_coefficients)) % ring.N


def is_valid_tuple(residues, ring):
    """Check if residues are in-range for the ring's moduli."""
    return all(0 <= r < q for r, q in zip(residues, ring.moduli))


# ═══════════════════════════════════════════════════════════════════════
# CRT TUPLE ARITHMETIC
# ═══════════════════════════════════════════════════════════════════════

def crt_add(a, b, ring):
    """Per-channel addition of CRT tuples."""
    return tuple((ai + bi) % q for ai, bi, q in zip(a, b, ring.moduli))


def crt_sub(a, b, ring):
    """Per-channel subtraction of CRT tuples."""
    return tuple((ai - bi) % q for ai, bi, q in zip(a, b, ring.moduli))


def crt_mul(a, b, ring):
    """Per-channel multiplication of CRT tuples."""
    return tuple((ai * bi) % q for ai, bi, q in zip(a, b, ring.moduli))


def crt_pow(a, k, ring):
    """Per-channel exponentiation of CRT tuple."""
    return tuple(pow(ai, k, q) for ai, q in zip(a, ring.moduli))


def crt_neg(a, ring):
    """Per-channel negation (mirror): n -> N-n."""
    return tuple((q - ai) % q for ai, q in zip(a, ring.moduli))


def crt_scale(a, s, ring):
    """Multiply CRT tuple by scalar s."""
    return tuple((ai * s) % q for ai, q in zip(a, ring.moduli))


# ═══════════════════════════════════════════════════════════════════════
# COUPLING AND CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════

def coupling(n, ring):
    """Coupling of element n: N / gcd(n, N)."""
    return ring.N // gcd(n % ring.N, ring.N)


def null_channels(residues, ring):
    """Set of channel indices where residue is 0."""
    return frozenset(i for i, r in enumerate(residues) if r == 0)


def is_unit(n, ring):
    """n is a unit iff gcd(n, N) = 1."""
    return gcd(n % ring.N, ring.N) == 1


# ═══════════════════════════════════════════════════════════════════════
# IDEMPOTENTS
# ═══════════════════════════════════════════════════════════════════════

def idempotent(channels, ring):
    """Compute the idempotent that projects onto the given channel indices.
    CRT tuple: 1 in selected channels, 0 in others."""
    residues = tuple(1 if i in channels else 0 for i in range(ring.k))
    return decode(residues, ring)


def all_idempotents(ring):
    """Generate all 2^k idempotents as (channel_set, value) pairs."""
    results = []
    for mask in range(2 ** ring.k):
        channels = frozenset(i for i in range(ring.k) if mask & (1 << i))
        val = idempotent(channels, ring)
        results.append((channels, val))
    return results


def omega(ring):
    """OMEGA: kills the mod-2 channel, preserves everything else.
    CRT = (0, 1, 1, ..., 1)."""
    return idempotent(frozenset(range(1, ring.k)), ring)


def delta(ring):
    """delta: the mod-2-channel-only projector.
    CRT = (1, 0, 0, ..., 0). omega + delta = 1."""
    return idempotent(frozenset([0]), ring)


# ═══════════════════════════════════════════════════════════════════════
# ERROR CORRECTION (tower split: first k-3 data, last 3 parity)
# ═══════════════════════════════════════════════════════════════════════

# A codeword is the full CRT tuple of a data value n < prod(data moduli):
# data channels carry n's residues, parity channels carry n mod q. The
# code is MDS with d=4 for k >= 7 (RAD: rate 4/7; RUNG5: rate 5/8) — any
# k-3 channels reconstruct, and every single-channel error is correctable.
# Weight matrix (syndrome of +1 in data channel p is -e_p mod parity
# primes, e_p the data-ring idempotent): all entries nonzero for RAD —
# no blind spots. The fat ring fails this (the fat record is archived).

def _crt_reconstruct_subset(residues_subset, moduli_subset):
    """CRT reconstruction from an arbitrary subset of moduli.
    Returns n mod prod(moduli_subset)."""
    N_sub = prod(moduli_subset)
    n = 0
    for r, qi in zip(residues_subset, moduli_subset):
        Mi = N_sub // qi
        yi = mod_inverse(Mi, qi)
        n = (n + r * Mi * yi) % N_sub
    return n


def ecc_encode(data_residues, ring):
    """Given data-channel residues, compute the full CRT tuple with parity.
    Valid codewords are data values 0..prod(data_moduli)-1 encoded this way.
    ECC syndrome/detect/correct only apply to (possibly corrupted) codewords."""
    data_ch = ring.data_channels
    parity_ch = ring.parity_channels

    if len(data_residues) != len(data_ch):
        raise ValueError(f"Expected {len(data_ch)} data residues, got {len(data_residues)}")

    data_moduli = [ring.moduli[i] for i in data_ch]
    n_data = _crt_reconstruct_subset(data_residues, data_moduli)

    result = [0] * ring.k
    for i, di in enumerate(data_ch):
        result[di] = data_residues[i]
    for pi in parity_ch:
        result[pi] = n_data % ring.moduli[pi]
    return tuple(result)


def ecc_syndrome(residues, ring):
    """Compute the ECC syndrome: parity channel errors.
    For a valid codeword, syndrome = (0, 0, ...).
    Non-zero syndrome indicates corruption."""
    data_ch = ring.data_channels
    parity_ch = ring.parity_channels
    data_residues = [residues[i] for i in data_ch]
    data_moduli = [ring.moduli[i] for i in data_ch]
    n_data = _crt_reconstruct_subset(data_residues, data_moduli)
    return tuple(
        (residues[pi] - n_data % ring.moduli[pi]) % ring.moduli[pi]
        for pi in parity_ch
    )


def decode_partial(residues, ring, channel_indices):
    """Reconstruct from a subset of channels.
    Returns n mod prod(selected moduli)."""
    sub_residues = [residues[i] for i in channel_indices]
    sub_moduli = [ring.moduli[i] for i in channel_indices]
    return _crt_reconstruct_subset(sub_residues, sub_moduli)


def ecc_detect(residues, ring):
    """Detect if any channel has been corrupted.
    Returns True if corruption detected."""
    syn = ecc_syndrome(residues, ring)
    return any(s != 0 for s in syn)


def ecc_locate(residues, ring):
    """Locate the corrupted channel (single-channel error assumption).
    Returns channel index, or None if clean / multi-channel error."""
    _, ch = ecc_correct(residues, ring)
    return ch


def ecc_correct(residues, ring):
    """Correct a single-channel error.
    Returns (corrected_tuple, corrupted_channel) or (original, None) if clean.

    Strategy: parity errors show as a single non-zero syndrome component.
    Data errors show as all-non-zero syndrome; try each data channel with
    each possible delta until syndrome clears."""
    syn = ecc_syndrome(residues, ring)
    if all(s == 0 for s in syn):
        return residues, None

    parity_ch = ring.parity_channels
    data_ch = ring.data_channels
    nonzero = [i for i, s in enumerate(syn) if s != 0]

    if len(nonzero) == 1:
        pi = parity_ch[nonzero[0]]
        corrected = list(residues)
        corrected[pi] = (corrected[pi] - syn[nonzero[0]]) % ring.moduli[pi]
        return tuple(corrected), pi

    for di in data_ch:
        q = ring.moduli[di]
        for delta_err in range(1, q):
            test = list(residues)
            test[di] = (test[di] - delta_err) % q
            test_syn = ecc_syndrome(tuple(test), ring)
            if all(s == 0 for s in test_syn):
                return tuple(test), di

    return residues, None


# ═══════════════════════════════════════════════════════════════════════
# EIGENVALUE
# ═══════════════════════════════════════════════════════════════════════

def eigenvalue(residues, ring, weights=None):
    """Compute the eigenvalue of a CRT tuple.
    lambda_n = sum_i w_i * cos(2*pi*r_i / q_i).
    Default weight = 2 for all channels."""
    if weights is None:
        weights = [2] * ring.k
    return sum(
        w * _cos_2pi(r, q)
        for w, r, q in zip(weights, residues, ring.moduli)
    )


def _cos_2pi(r, q):
    """cos(2*pi*r/q) with exact value at r=0."""
    if r == 0:
        return 1.0
    return cos(2 * pi * r / q)


def eigenvalue_of(n, ring, weights=None):
    """Eigenvalue of integer n in the ring."""
    return eigenvalue(encode(n, ring), ring, weights)


def chord_distance_sq(residues, ring):
    """Squared chord distance from 0 on the CRT torus:
    ||d(n)||^2 = sum 4*sin^2(pi*r_i/q_i).
    eigenvalue(n) = degree - chord_distance_sq(n)."""
    return sum(
        4 * sin(pi * r / q) ** 2
        for r, q in zip(residues, ring.moduli)
    )


def spectral_gap(ring):
    """Minimum non-zero chord distance squared = 4*sin^2(pi/max_modulus)."""
    return 4 * sin(pi / max(ring.moduli)) ** 2


# ═══════════════════════════════════════════════════════════════════════
# HAMMING GRAPH
# ═══════════════════════════════════════════════════════════════════════

def hamming_distance(a, b, ring):
    """CRT Hamming distance: number of channels where residues differ."""
    return sum(1 for ai, bi in zip(a, b) if ai != bi)


def hamming_degree(ring):
    """Degree of the CRT Hamming graph = sum(q_i - 1)."""
    return sum(q - 1 for q in ring.moduli)


def hamming_neighbors(residues, ring):
    """All CRT Hamming neighbors (differ in exactly one channel)."""
    neighbors = []
    for ch in range(ring.k):
        q = ring.moduli[ch]
        for r in range(q):
            if r != residues[ch]:
                t = list(residues)
                t[ch] = r
                neighbors.append(tuple(t))
    return neighbors


# ═══════════════════════════════════════════════════════════════════════
# SEED-FLOWER (topology predicting unseen primes)
# ═══════════════════════════════════════════════════════════════════════

def euler_characteristic(ring):
    """CRT Euler characteristic: chi = N * (1 - k + sum(1/q_i)).
    Uses exact integer arithmetic via common denominator."""
    from fractions import Fraction
    s = Fraction(1 - ring.k)
    for q in ring.moduli:
        s += Fraction(1, q)
    return int(ring.N * s)


def seed_flower(primes, exponents=None):
    """Build a sub-ring from given primes and compute -chi.
    Default exponents are all 1 (thin — the canonical tower).
    Pass explicit exponents for fat sub-rings."""
    if exponents is None:
        exponents = [1] * len(primes)
    r = Ring("sub", primes, exponents)
    return -euler_characteristic(r), r


# ═══════════════════════════════════════════════════════════════════════
# SELF-TEST
# ═══════════════════════════════════════════════════════════════════════

def _self_test():
    import time
    start = time.time()
    passed = 0

    def check(name, condition):
        nonlocal passed
        assert condition, f"FAIL: {name}"
        passed += 1

    # ── Squarefree tower constants ──────────────────────────────────────
    check("RAD.N", RAD_RING.N == 510510)
    check("RAD.phi", RAD_RING.phi == 92160)
    check("RAD.lam", RAD_RING.lam == 240)
    check("RUNG5.N", RUNG5_RING.N == 9699690)
    check("RUNG5.phi", RUNG5_RING.phi == 1658880)
    check("RUNG5.lam", RUNG5_RING.lam == 720)
    check("k=6 N", primorial_ring(6).N == 30030)
    check("k=6 lam", primorial_ring(6).lam == 60)
    check("k=5 N", primorial_ring(5).N == 2310)
    check("k=5 lam", primorial_ring(5).lam == 60)
    check("k=4 N", primorial_ring(4).N == 210)
    check("k=4 lam", primorial_ring(4).lam == 12)
    # Every rung's exponent tuple must match its own prime tuple: Ring pairs
    # them with zip, which truncates, so a mismatch is silent in N and shows
    # only here. This is the check the fixed ring constants never needed.
    for kk in range(1, len(TOWER_PRIMES) + 1):
        r = primorial_ring(kk)
        assert len(r.exponents) == len(r.primes) == r.k == kk
        if kk >= 4:
            pw = powered_ring(kk)
            assert len(pw.exponents) == len(pw.primes) == pw.k == kk
    check("rung exponent/prime tuples agree, k=1..12", True)
    # Out-of-range and sub-4 powered raise instead of returning a wrong ring.
    for bad in (0, len(TOWER_PRIMES) + 1):
        try:
            primorial_ring(bad); assert False
        except ValueError:
            pass
    for bad in (3, len(TOWER_PRIMES) + 1):
        try:
            powered_ring(bad); assert False
        except ValueError:
            pass
    check("constructors reject out-of-range rungs", True)
    # The two constructors agree with the named rungs on the shared index.
    check("k=7 is RAD", primorial_ring(7).moduli == RAD_RING.moduli)
    check("k=7 powered N", powered_ring(7).N == 214414200)
    check("k=6 powered N", powered_ring(6).N == 12612600)
    check("k=5 powered N", powered_ring(5).N == 970200)

    # ── Tower split defaults ────────────────────────────────────────────
    check("RAD split", RAD_RING.data_channels == (0, 1, 2, 3)
          and RAD_RING.parity_channels == (4, 5, 6))
    check("RUNG5 split", RUNG5_RING.data_channels == (0, 1, 2, 3, 4)
          and RUNG5_RING.parity_channels == (5, 6, 7))
    check("k<7 all-data", all(primorial_ring(k).parity_channels == ()
                              for k in (4, 5, 6)))
    check("n_data override", Ring("t", (2, 3, 5), (1, 1, 1), n_data=2)
          .parity_channels == (2,))

    # ── Encode/decode round-trip ────────────────────────────────────────
    for n in [0, 1, 42, 137, 490, 510509]:
        check(f"RAD roundtrip({n})", decode(encode(n, RAD_RING), RAD_RING) == n)
    for n in [0, 1, 510510, 9699689]:
        check(f"RUNG5 roundtrip({n})", decode(encode(n, RUNG5_RING), RUNG5_RING) == n)

    # Exhaustive round-trip on rung 4, which is RAD's data space
    r4 = primorial_ring(4)
    for n in range(r4.N):
        assert decode(encode(n, r4), r4) == n
    check("k=4 exhaustive roundtrip", True)

    # ── CRT arithmetic on RAD ───────────────────────────────────────────
    a, b_val = 42, 137
    ta, tb = encode(a, RAD_RING), encode(b_val, RAD_RING)
    N = RAD_RING.N
    check("crt_add", decode(crt_add(ta, tb, RAD_RING), RAD_RING) == (a + b_val) % N)
    check("crt_sub", decode(crt_sub(ta, tb, RAD_RING), RAD_RING) == (a - b_val) % N)
    check("crt_mul", decode(crt_mul(ta, tb, RAD_RING), RAD_RING) == (a * b_val) % N)
    check("crt_pow", decode(crt_pow(ta, 3, RAD_RING), RAD_RING) == pow(a, 3, N))
    check("crt_neg", decode(crt_neg(ta, RAD_RING), RAD_RING) == (N - a) % N)
    check("crt_scale", decode(crt_scale(ta, 19, RAD_RING), RAD_RING) == (a * 19) % N)

    # ── Coupling, units ─────────────────────────────────────────────────
    for p in RAD_RING.primes:
        check(f"coupling({p}) = N/{p}", coupling(p, RAD_RING) == N // p)
    check("coupling(unit) = N", coupling(1, RAD_RING) == N
          and coupling(499, RAD_RING) == N)
    check("is_unit", is_unit(499, RAD_RING) and not is_unit(34, RAD_RING))
    check("null_channels", null_channels(encode(30, RAD_RING), RAD_RING)
          == frozenset({0, 1, 2}))

    # ── Idempotents on RAD ──────────────────────────────────────────────
    idem = all_idempotents(RAD_RING)
    check("RAD idempotents count", len(idem) == 128)
    check("RAD idempotents all idempotent",
          all(pow(val, 2, N) == val for _, val in idem))
    check("RAD idempotents distinct", len({val for _, val in idem}) == 128)

    om = omega(RAD_RING)
    check("OMEGA_RAD CRT", encode(om, RAD_RING) == (0, 1, 1, 1, 1, 1, 1))
    d = delta(RAD_RING)
    check("delta_RAD CRT", encode(d, RAD_RING) == (1, 0, 0, 0, 0, 0, 0))
    check("omega + delta = 1", (om + d) % N == 1)

    # ── ECC on RAD (rate 4/7, MDS d=4) ──────────────────────────────────
    # Codeword construction and clean syndrome, exhaustive over data space
    for n in range(210):
        cw = ecc_encode(tuple(n % p for p in (2, 3, 5, 7)), RAD_RING)
        assert cw == encode(n, RAD_RING)
        assert ecc_syndrome(cw, RAD_RING) == (0, 0, 0)
    check("ECC clean: all 210 codewords", True)

    # Weight matrix: syndrome of +1 in data channel p is -e_p mod parity,
    # where e_p is the Z/210 idempotent. Every entry is nonzero, which is
    # what makes each single-channel error visible in all three parities.
    expected_w = {11: [6, 4, 5, 10], 13: [1, 5, 9, 3], 17: [3, 2, 7, 1]}
    e210 = {p: idempotent(frozenset([i]), primorial_ring(4))
            for i, p in enumerate((2, 3, 5, 7))}
    for j, q in enumerate((11, 13, 17)):
        row = [e210[p] % q for p in (2, 3, 5, 7)]
        check(f"weight matrix row {q}", row == expected_w[q])
        check(f"no blind spots mod {q}", all(w != 0 for w in row))

    # Detect + locate + correct: every channel, every possible delta
    full = encode(42, RAD_RING)
    ok = True
    for ch in range(7):
        q = RAD_RING.moduli[ch]
        for delta_err in range(1, q):
            bad = list(full)
            bad[ch] = (bad[ch] + delta_err) % q
            bad = tuple(bad)
            corr, loc = ecc_correct(bad, RAD_RING)
            if not ecc_detect(bad, RAD_RING) or loc != ch or corr != full:
                ok = False
    check("ECC correct: all 7 channels x all 51 deltas", ok)

    # Random trials across the data space
    import random
    random.seed(7)
    ok = True
    for _ in range(50):
        n = random.randint(0, 209)
        orig = encode(n, RAD_RING)
        ch = random.randint(0, 6)
        err = random.randint(1, RAD_RING.moduli[ch] - 1)
        bad = list(orig)
        bad[ch] = (bad[ch] + err) % RAD_RING.moduli[ch]
        corr, loc = ecc_correct(tuple(bad), RAD_RING)
        if loc != ch or corr != orig:
            ok = False
    check("ECC random 50 trials (RAD)", ok)

    # MDS erasure: ANY 4 of 7 channels reconstruct the data value
    from itertools import combinations
    ok = True
    for n in (0, 1, 42, 137, 209):
        cw = encode(n, RAD_RING)
        for subset in combinations(range(7), 4):
            # n < 210 <= prod(subset moduli), so reconstruction is exact
            if decode_partial(cw, RAD_RING, subset) != n:
                ok = False
    check("MDS: all 35 4-of-7 subsets reconstruct", ok)

    # ── ECC on RUNG5 (rate 5/8) ─────────────────────────────────────────
    cw5 = ecc_encode(tuple(1234 % p for p in (2, 3, 5, 7, 11)), RUNG5_RING)
    check("RUNG5 codeword = encode(1234)", cw5 == encode(1234, RUNG5_RING))
    check("RUNG5 clean syndrome", ecc_syndrome(cw5, RUNG5_RING) == (0, 0, 0))
    ok = True
    for ch in range(8):
        bad = list(cw5)
        bad[ch] = (bad[ch] + 1) % RUNG5_RING.moduli[ch]
        corr, loc = ecc_correct(tuple(bad), RUNG5_RING)
        if loc != ch or corr != cw5:
            ok = False
    check("RUNG5 correct: all 8 channels, delta=1", ok)
    random.seed(8)
    ok = True
    for _ in range(30):
        n = random.randint(0, 2309)
        orig = encode(n, RUNG5_RING)
        ch = random.randint(0, 7)
        err = random.randint(1, RUNG5_RING.moduli[ch] - 1)
        bad = list(orig)
        bad[ch] = (bad[ch] + err) % RUNG5_RING.moduli[ch]
        corr, loc = ecc_correct(tuple(bad), RUNG5_RING)
        if loc != ch or corr != orig:
            ok = False
    check("ECC random 30 trials (RUNG5)", ok)

    # ── Eigenvalue / spectral ───────────────────────────────────────────
    ev0 = eigenvalue(encode(0, RAD_RING), RAD_RING)
    check("eigenvalue(0) = 2k", abs(ev0 - 2 * RAD_RING.k) < 1e-10)
    t42 = encode(42, RAD_RING)
    check("eigenvalue = degree - chord^2",
          abs(eigenvalue(t42, RAD_RING)
              - (2 * RAD_RING.k - chord_distance_sq(t42, RAD_RING))) < 1e-10)
    check("spectral gap from p=17",
          abs(spectral_gap(RAD_RING) - 4 * sin(pi / 17) ** 2) < 1e-15)

    # ── Hamming ─────────────────────────────────────────────────────────
    check("hamming_degree RAD = sum(p-1) = 51", hamming_degree(RAD_RING) == 51)
    check("hamming_distance", hamming_distance(
        encode(0, RAD_RING), encode(1, RAD_RING), RAD_RING) == 7)
    check("hamming_neighbors count",
          len(hamming_neighbors(encode(0, RAD_RING), RAD_RING)) == 51)

    # ── Seed-flower (thin default) ──────────────────────────────────────
    check("seed-flower {2,3,5} = 29", seed_flower([2, 3, 5])[0] == 29)
    check("seed-flower twin {2,5} = 3", seed_flower([2, 5])[0] == 3)
    check("seed-flower twin {2,7} = 5", seed_flower([2, 7])[0] == 5)
    check("seed-flower 3-root {3,5} = 7", seed_flower([3, 5])[0] == 7)
    check("seed-flower 3-root {3,7} = 11", seed_flower([3, 7])[0] == 11)
    check("seed-flower fat Z/72 = 55", seed_flower([2, 3], [3, 2])[0] == 55)

    # ── The prime-power variant at rung 7 ───────────────────────────────
    pw7 = powered_ring(7)
    check("k=7 powered phi", pw7.phi == 38707200)
    check("k=7 powered lam", pw7.lam == 1680)
    for n in [0, 42, 88200, 214414199]:
        check(f"k=7 powered roundtrip({n})", decode(encode(n, pw7), pw7) == n)
    check("k=7 powered omega", omega(pw7) == 26801776)
    full_pw = encode(42, pw7)
    ok = True
    for ch in range(7):
        bad = list(full_pw)
        bad[ch] = (bad[ch] + 1) % pw7.moduli[ch]
        corr, loc = ecc_correct(tuple(bad), pw7)
        if loc != ch or corr != full_pw:
            ok = False
    check("k=7 powered ECC channel sweep, delta=1", ok)
    check("490 split, powered", encode(pow(490, 1680, pw7.N), pw7)
          == (0, 1, 0, 0, 1, 1, 1))

    elapsed = time.time() - start
    print(f"crt.py self-test: {passed} checks passed in {elapsed:.2f}s")


if __name__ == "__main__":
    _self_test()
