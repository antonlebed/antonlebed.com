"""What operator is the CRT eigenvalue an eigenvalue OF?

QUESTION
    crt.py defines eigenvalue(n) = sum_i w_i cos(2 pi r_i / q_i) and calls
    it "the eigenvalue of a CRT tuple" -- an eigenvalue of nothing, defined
    by its formula alone. The candidate object: the CHANNEL-STEP GRAPH on
    the ring -- vertices the ring elements, edges x ~ x +- e_i where the
    e_i are the atomic (weight-1) idempotents, one +-1 step in one channel
    -- which is the Cartesian product of cycles C_q1 [] ... [] C_qk on CRT
    coordinates. Its vertex degree is 2k (multigraph convention: the q=2
    channel's +e and -e coincide, so that edge carries adjacency entry 2).

PREDICTIONS (fixed before the run)
    P1  Diagonalizing the N x N adjacency matrix at Z/30 (k=3) and Z/210
        (k=4) reproduces {eigenvalue(n) : n in ring} at weight 2 as a
        multiset, max deviation < 1e-9.
    P2  For every residue tuple m, the CRT-coordinate character
        psi_m(r) = prod_i exp(2 pi i m_i r_i / q_i) satisfies
        A psi_m = eigenvalue(m) psi_m to 1e-9.
    P3  THE TWIST: the integer-label character chi_n(x) = exp(2 pi i nx/N)
        is also an eigenvector, but its eigenvalue is
        sum_i 2 cos(2 pi n_i u_i / q_i) with u_i = (N/q_i)^{-1} mod q_i --
        equal to eigenvalue(n) only when every u_i is +-1 mod q_i (cos is
        even). Prediction: some ring in {Z/30, Z/210} has a u_i not +-1,
        and there chi_n's eigenvalue differs from eigenvalue(n) for some n.
        The clean pairing n <-> eigenvector lives on CRT coordinates.
    P4  POSITIVE CONTROL (run before reading any verdict): the same
        diagonalization rig on the Hamming graph K_2 [] K_3 [] K_5
        (edges = any nonzero step in one channel) reproduces the
        subset-sum spectrum lambda_S = degree - sum_{i in S} p_i with
        multiplicity prod_{i in S}(p_i - 1).
    KILL (observable): the P1 multiset comparison prints max dev > 1e-9.

DESIGN
    Dense numpy diagonalization (eigvalsh); N <= 210 so the matrices are
    tiny. The adjacency matrix is built on integer labels via CRT: the
    atomic idempotent e_i is the integer that is 1 in channel i and 0
    elsewhere, and an edge adds +-e_i mod N. All comparisons print their
    max deviation; asserts carry the tolerance.

FINDINGS (entered post-run; tiers per naming discipline)
    The control ran first and passed (P4 subset-sum spectrum, max dev
    4.44e-15). All four predictions confirmed.

    1. THE OPERATOR EXISTS (property -- follows from Cayley character
       theory for all k; verified numerically at k=3 and k=4). The CRT
       eigenvalue at weight 2 is exactly the adjacency spectrum of the
       channel-step graph Cay(ring, {+-atomic idempotents}) =
       C_q1 [] ... [] C_qk: max dev 3.55e-15 at Z/30, 1.95e-14 at Z/210.
       Its vertex degree 2k is eigenvalue(0) -- the chord identity's
       "degree" was always this graph's degree.
    2. THE EIGENVECTORS ARE THE CRT-COORDINATE CHARACTERS (property,
       same proof): A psi_m = eigenvalue(m) psi_m, max dev 4.67e-14
       over every m at both rings.
    3. THE PAIRING LIVES ON CRT COORDINATES, NOT INTEGER LABELS (rule,
       verified k=3..4). The integer-label character chi_n is an
       eigenvector whose eigenvalue is the u-TWISTED sum
       sum_i 2 cos(2 pi n_i u_i / q_i), u_i = (N/q_i)^{-1} mod q_i
       (max dev 2.22e-12). At Z/210 the units are (1, 1, -2, -3): the
       twist is visible and chi_n's eigenvalue differs from
       eigenvalue(n) at 204/210 labels. The small rungs are the trap:
       at every k <= 3 the units are all +-1 (Z/30: 1,1,1; Z/6: 1,-1,
       with -1 invisible because cos is even), so the two pairings
       coincide there -- and the twist is visible at every k = 4..10
       (units_ladder(), added post-run), so the coincidence ends
       exactly where the small-ring check would stop.

RUN RECORD
    0.3 s wall, 27.5 MB peak (memwatch, limit 512 MB). All asserts
    passed.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from crt import primorial_ring, encode, eigenvalue

TOL = 1e-9


def atomic_idempotents(ring):
    """The k weight-1 idempotents as integers: 1 in one channel, 0 elsewhere."""
    out = []
    for i, q in enumerate(ring.moduli):
        residues = [0] * ring.k
        residues[i] = 1
        # CRT reconstruction
        n = 0
        for j, qj in enumerate(ring.moduli):
            Mj = ring.N // qj
            n = (n + residues[j] * Mj * pow(Mj, -1, qj)) % ring.N
        out.append(n)
    return out


def channel_step_adjacency(ring):
    """A[x][y] = number of generators s in {+-e_i} with y = x + s (multigraph)."""
    N = ring.N
    A = np.zeros((N, N))
    for e in atomic_idempotents(ring):
        for x in range(N):
            A[x][(x + e) % N] += 1
            A[x][(x - e) % N] += 1
    return A


def run_ring(k):
    ring = primorial_ring(k)
    N = ring.N
    print(f"\n=== Z/{N} (k={k}, moduli {ring.moduli}) ===")

    A = channel_step_adjacency(ring)
    spec = np.sort(np.linalg.eigvalsh(A))
    formula = np.sort([eigenvalue(encode(n, ring), ring) for n in range(N)])
    dev1 = float(np.max(np.abs(spec - formula)))
    print(f"P1 spectrum vs eigenvalue() multiset: max dev = {dev1:.2e}")
    assert dev1 < TOL, f"KILL: P1 mismatch {dev1}"

    # P2: CRT-coordinate characters are eigenvectors with eigenvalue(m)
    coords = np.array([encode(x, ring) for x in range(N)])  # N x k residues
    max_dev2 = 0.0
    for m in range(N):
        mres = encode(m, ring)
        phase = sum(
            mres[i] * coords[:, i] / ring.moduli[i] for i in range(ring.k)
        )
        psi = np.exp(2j * np.pi * phase)
        lam = eigenvalue(mres, ring)
        dev = float(np.max(np.abs(A @ psi - lam * psi)))
        max_dev2 = max(max_dev2, dev)
    print(f"P2 A psi_m = eigenvalue(m) psi_m: max dev over all m = {max_dev2:.2e}")
    assert max_dev2 < 1e-7, f"P2 fails: {max_dev2}"

    # P3: integer-label characters and the unit twist
    units = [pow(ring.N // q, -1, q) for q in ring.moduli]
    print(f"P3 CRT units u_i = (N/q_i)^-1 mod q_i: {units} "
          f"(mod q: {[u if u <= q // 2 else u - q for u, q in zip(units, ring.moduli)]})")
    twist_visible = any(u % q not in (1, q - 1) for u, q in zip(units, ring.moduli))
    max_chi_dev = 0.0
    n_differ = 0
    for n in range(N):
        chi = np.exp(2j * np.pi * n * np.arange(N) / N)
        nres = encode(n, ring)
        lam_twisted = sum(
            2 * np.cos(2 * np.pi * (r * u % q) / q)
            for r, u, q in zip(nres, units, ring.moduli)
        )
        dev = float(np.max(np.abs(A @ chi - lam_twisted * chi)))
        max_chi_dev = max(max_chi_dev, dev)
        if abs(lam_twisted - eigenvalue(nres, ring)) > TOL:
            n_differ += 1
    print(f"P3 chi_n eigenvector with TWISTED eigenvalue: max dev = {max_chi_dev:.2e}")
    print(f"P3 twist visible (some u_i != +-1): {twist_visible}; "
          f"chi_n eigenvalue != eigenvalue(n) at {n_differ}/{N} labels")
    assert max_chi_dev < 1e-7
    return twist_visible, n_differ


def positive_control():
    """P4: Hamming graph K_2 [] K_3 [] K_5 -- subset-sum spectrum."""
    ring = primorial_ring(3)
    N = ring.N
    A = np.zeros((N, N))
    for x in range(N):
        rx = encode(x, ring)
        for y in range(N):
            ry = encode(y, ring)
            if sum(a != b for a, b in zip(rx, ry)) == 1:
                A[x][y] = 1
    spec = np.sort(np.linalg.eigvalsh(A))
    degree = sum(q - 1 for q in ring.moduli)
    expected = []
    for S in range(8):
        subset = [i for i in range(3) if S >> i & 1]
        lam = degree - sum(ring.moduli[i] for i in subset)
        mult = 1
        for i in subset:
            mult *= ring.moduli[i] - 1
        expected += [lam] * mult
    dev = float(np.max(np.abs(spec - np.sort(expected))))
    print(f"P4 positive control (Hamming K2[]K3[]K5 subset-sum spectrum): "
          f"max dev = {dev:.2e}")
    assert dev < TOL, f"control fails: {dev}"


def units_ladder():
    """Where the twist turns visible: the CRT units rung by rung."""
    print("\n=== units ladder: u_i = (N/q_i)^-1 mod q_i, signed ===")
    for k in range(1, 11):
        ring = primorial_ring(k)
        signed = [
            (u if u <= q // 2 else u - q)
            for u, q in ((pow(ring.N // q, -1, q), q) for q in ring.moduli)
        ]
        visible = any(abs(s) != 1 for s in signed)
        print(f"k={k}: {signed} -> twist {'VISIBLE' if visible else 'invisible'}")
        assert visible == (k >= 4), f"visibility boundary moved at k={k}"


if __name__ == "__main__":
    positive_control()
    for k in (3, 4):
        run_ring(k)
    units_ladder()
    print("\nAll asserts passed.")
