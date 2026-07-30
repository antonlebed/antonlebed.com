"""Torus knots and Brieskorn spheres for tower-prime pairs and triples.

PAIRS. The CRT torus T^k carries a torus knot T(p_i, p_j) for every pair
of tower primes (the diagonal winding restricted to two coordinates).
Signature formula (Brieskorn/Hirzebruch lattice-point count, via the
Milnor fiber of x^p + y^q + z^2):

    sigma(T(p,q)) = #{(i,j) in [1,p-1]x[1,q-1] : i/p + j/q in (0,1/2) u (3/2,2)}
                  - #{(i,j) in [1,p-1]x[1,q-1] : i/p + j/q in (1/2,3/2)}

Sanity anchors: sigma(T(2,3)) = -2 (trefoil), sigma(T(2,q)) = 1-q,
sigma(T(3,5)) = -8 (the E8 intersection form).
Crossing number (Murasugi): c(T(p,q)) = min(p(q-1), q(p-1)).

TRIPLES. Every triple of distinct tower primes is pairwise coprime, so
Sigma(p,q,r) = {x^p + y^q + z^r = 0} cap S^5 is a Brieskorn INTEGRAL
HOMOLOGY 3-SPHERE. The signature of its Milnor fiber F(p,q,r) has the
exact Hirzebruch lattice-point form (no boundary cases occur: the sum
i/p + j/q + k/r is never an integer when p,q,r are pairwise coprime):

    sigma(p,q,r) = #{(i,j,k) : i/p + j/q + k/r mod 2 in (0,1)}
                 - #{(i,j,k) : i/p + j/q + k/r mod 2 in (1,2)}
    over (i,j,k) in [1,p-1] x [1,q-1] x [1,r-1].

Anchors: (a) sigma(p,q,2) = sigma(T(p,q)) for ALL pairs in scope — the
z^2 suspension IS the definition of the knot signature, so the 3D count
must reproduce the 2D one; (b) sigma(2,3,5) = -8 (the E8 manifold).
The Casson invariant of Sigma(p,q,r) is sigma/8 (Neumann-Wahl theorem);
in our orientation lambda(Sigma(2,3,5)) = -1 (Poincare sphere).

FINDINGS (tiers per claim; scope = primes {2..23}, i.e. tower k <= 9):
1. (rule) All 36 pair signatures k <= 9 are negative (left-handed in
   our orientation). Per-level signature totals k = 2..9:
   -2, -14, -44, -134, -314, -658, -1196, -2066.
2. (rule, kill) The level-5 crossing-total coincidence (total 210 =
   level-4 modulus N(Z/210)) does NOT persist: crossing totals run
   3, 18, 67, 210, 509, 1104, 2073, 3660, and no later level's total
   equals any earlier modulus (asserted). One-off numerology.
3. (rule) All 84 triple signatures are divisible by 8 — the Milnor
   fiber of a Brieskorn homology sphere is spin with unimodular form
   (known background); verified exhaustively at k <= 9. All 84 are
   negative. Casson invariants lambda = sigma/8 run from -1
   (Poincare sphere) to -308 (Sigma(17,19,23)); level totals
   k = 3..9: -1, -8, -47, -187, -615, -1625, -3873.
4. (property) CHANNEL 2 IS THE SUSPENSION COORDINATE: sigma(2,q,r) =
   sigma(T(q,r)) exactly — definitional, since the z^2 suspension IS
   how the knot signature arises from a Milnor fiber (verified here
   for all 28 odd pairs). A triple containing 2 adds no new signature
   or Casson data beyond its pair; the genuinely new
   higher-dimensional objects are the 56 odd triples. (Echoes
   2-invisibility in the naming thread — channel 2 repeatedly acts
   as a degenerate direction.)

Run: python prime/code/explore_torus_knots.py
"""
from fractions import Fraction
from itertools import combinations
from math import prod

PRIMES9 = [2, 3, 5, 7, 11, 13, 17, 19, 23]   # tower primes through k=9


def signature(p, q):
    """sigma(T(p,q)) by exact lattice-point count (no floats)."""
    s = 0
    half, three_half = Fraction(1, 2), Fraction(3, 2)
    for i in range(1, p):
        for j in range(1, q):
            v = Fraction(i, p) + Fraction(j, q)
            s += -1 if half < v < three_half else 1
    return s


def crossings(p, q):
    return min(p * (q - 1), q * (p - 1))


def signature3(p, q, r):
    """sigma of the Milnor fiber of x^p + y^q + z^r (Hirzebruch count).

    Integer arithmetic: with s = i*qr + j*pr + k*pq and N = pqr, the
    class of i/p + j/q + k/r mod 2 is s mod 2N; sign +1 on (0, N),
    -1 on (N, 2N). s is never a multiple of N for pairwise-coprime
    p, q, r (s = 0 mod p forces p | i).
    """
    N = p * q * r
    qr, pr, pq = q * r, p * r, p * q
    sig = 0
    for i in range(1, p):
        a = i * qr
        for j in range(1, q):
            b = a + j * pr
            for k in range(1, r):
                s = (b + k * pq) % (2 * N)
                assert s % N != 0, (p, q, r, i, j, k)
                sig += 1 if s < N else -1
    return sig


def main():
    # --- sanity anchors from knot theory ---
    assert signature(2, 3) == -2          # trefoil
    assert signature(3, 5) == -8          # E8
    for q in (3, 5, 7, 11):
        assert signature(2, q) == 1 - q   # (2,q) torus knots
    print("pair anchors OK: T(2,3)=-2, T(3,5)=-8, T(2,q)=1-q")

    # --- suspension cross-check: 3D count with r=2 == 2D knot signature ---
    for p, q in combinations(PRIMES9[1:], 2):     # odd primes only
        assert signature3(p, q, 2) == signature(p, q), (p, q)
    assert signature3(2, 3, 5) == -8              # E8 manifold
    print("triple anchors OK: sigma3(p,q,2)=sigma(T(p,q)) all odd pairs;"
          " sigma3(2,3,5)=-8 (E8)")

    # --- pairs through k=9 ---
    print(f"\n{'pair':10s} {'sigma':>6s} {'crossings':>10s}")
    for p, q in combinations(PRIMES9, 2):
        print(f"T({p},{q}){'':4s} {signature(p, q):>6d} {crossings(p, q):>10d}")

    print(f"\n{'level':>6s} {'ring':>12s} {'sig total':>10s} {'cross total':>12s}")
    moduli = {}
    cross_totals = {}
    for k in range(2, 10):
        ps = PRIMES9[:k]
        st = sum(signature(a, b) for a, b in combinations(ps, 2))
        ct = sum(crossings(a, b) for a, b in combinations(ps, 2))
        moduli[k] = prod(ps)
        cross_totals[k] = ct
        print(f"{k:>6d} Z/{prod(ps):<11d} {st:>10d} {ct:>12d}")

    allneg = all(signature(a, b) < 0 for a, b in combinations(PRIMES9, 2))
    print(f"\nall 36 pair signatures negative (left-handed): {allneg}")
    assert allneg

    # the level-5 coincidence (cross total 210 = N(Z/210)): does it recur?
    hits = [(k, j) for k in range(3, 10) for j in range(2, k)
            if cross_totals[k] == moduli[j]]
    print(f"crossing-total == earlier-modulus hits: {hits} "
          f"(level-5 one-off {'persists' if len(hits) > 1 else 'does NOT persist'})")
    assert hits == [(5, 4)]

    # --- triples: Brieskorn homology spheres ---
    print(f"\n{'triple':16s} {'sigma':>6s} {'lambda':>7s}   (lambda = Casson = sigma/8)")
    trip_sigs = {}
    for t in combinations(PRIMES9, 3):
        s = signature3(*t)
        assert s % 8 == 0, t              # even unimodular form
        trip_sigs[t] = s
        print(f"Sigma{t!s:14s} {s:>6d} {s // 8:>7d}")

    assert trip_sigs[(2, 3, 5)] == -8     # Poincare sphere, lambda = -1
    allneg3 = all(s < 0 for s in trip_sigs.values())
    print(f"\nall {len(trip_sigs)} triple signatures negative: {allneg3}")
    assert allneg3

    print(f"\n{'level':>6s} {'#triples':>9s} {'sig total':>11s} {'lambda total':>13s}")
    for k in range(3, 10):
        ps = set(PRIMES9[:k])
        sigs = [s for t, s in trip_sigs.items() if set(t) <= ps]
        print(f"{k:>6d} {len(sigs):>9d} {sum(sigs):>11d} {sum(sigs) // 8:>13d}")


if __name__ == "__main__":
    main()
