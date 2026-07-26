"""
Generator-step escape from non-units: the 2-boost, made exact.

Recovers the "2-boost gradient" finding (archive: explore_unit_density.c,
an earlier era). The archive measured "unit-neighbor density" -- for a non-unit
n in Z/p_k#, how many of its 2k generator neighbors n +/- p_j are units --
but the definition lived only in the archive and the published 3.6-4.5
table was unreproducible from the doc statement. Recovered and SUPERSEDED:
the whole table is an exact closed form.

THE ESCAPE RULE. Let n be a non-unit with null set S (the channels where
n = 0 mod p), and let +/-g be a signed generator step (g a tower prime).
Within n's coupling class (all elements with null set exactly S):

  g in S:      no element escapes (g | n  =>  g | n +/- g).
  g not in S:  EXACTLY (g-1) * prod_{p not in S, p != g} (p-2) class
               members land on a unit, out of prod_{p not in S} (p-1);
               escape probability  prod_{p not in S, p != g} (p-2)/(p-1).

Proof (all k): within the class, CRT makes the residue tuple (n mod p)
for p not in S range over ALL tuples of nonzero residues exactly once.
n+g is a unit iff every channel avoids 0: channels p in S, p != g pass
automatically (n+g = g != 0 mod p); channel p = g passes automatically
(n+g = n != 0 mod g since g not in S) -- the free factor (g-1); channels
p not in S, p != g need n != -g mod p: p-2 of the p-1 nonzero residues.
Same for -g by the unit-preserving bijection n -> -n.

THE PARITY DICHOTOMY (the p = 2 factor): if 2 not in S and g is odd, the
p = 2 term is (2-2) = 0 -- an odd step from an odd non-unit always lands
even. So an ODD non-unit escapes ONLY via +/-2 (the 2-boost), and an
EVEN non-unit escapes via any odd g not in S, never via +/-2. Every
nonzero CLASS has positive escape probability; the origin's class {0}
alone has none (0 +/- g is divisible by g). Class-level, NOT
per-element: individual stuck non-units exist (122 in Z/2310, e.g.
n = 119 = 7*17 with 117 = 3^2*13 and 121 = 11^2 -- both +/-2
neighbors non-unit, odd steps parity-trapped).

Sections:
  I.   Exhaustive verification k = 3..7      (every class x signed step)
  II.  k = 7 reference: class table, corollaries
  III. k = 5 archive table, reproduced exactly
  IV.  Asymptotics: the twin-prime constant

FINDINGS:
  1. (rule) The escape rule above: proved algebraically for all k,
     verified exhaustively k = 3..7 (every coupling class x every
     signed generator step, exact integer counts -- 127 classes x 14
     steps at k=7).
  2. (rule, corollary) Parity dichotomy + escape-proof origin class:
     odd non-units escape only via +/-2, even non-units never via
     +/-2; every nonzero class escapes with positive probability,
     class {0} never. Per-element is weaker: stuck non-units exist
     (122 in Z/2310). Verified same range.
  3. (property) The generic 2-boost probability is the twin-prime
     sieve product: from class S = {q}, P(escape via 2) =
     prod_{odd p <= p_k, p != q} (p-2)/(p-1); the full product
     A(k) = prod_{3 <= p <= p_k} (p-2)/(p-1) is EXACTLY the
     conditional twin-survivor density P(n+2 unit | n unit) on
     Z/p_k# (at k=7: 22275/92160 = 0.241699 = A(7)), and
     A(k) ~ 2*C2*e^-gamma /
     ln p_k (C2 = 0.66016... the twin prime constant). Measured ratio
     A(k)/model -> 1.00 by k = 10^5. Twin-unit density is the same
     kernel: #{n: n, n+2 both units} = prod_{odd p} (p-2) exactly
     (22,275 at k=7, verified by direct count).
  4. (observation) The archive's k=5 mean-unit-neighbor table is
     reproduced exactly by the rule; class means at k=5 range 0 (the
     origin) to 4.100 (S={2,3}: four odd escape steps), odd classes
     0.625-2.000 (2-boost only; the max is S = all four odd primes,
     escape probability 1). The cut's quoted "3.6-4.5" matches no
     breakdown we can recompute -- the exact rule replaces it.

Tier: rule (proved all k, verified exhaustively k <= 7).
Resource: pure stdlib, peak < 100 MB, wall ~1 s.
"""

from math import gcd, prod, log, exp
from itertools import combinations

PRIMES_ALL = [2, 3, 5, 7, 11, 13, 17]

C2 = 0.6601618158468696       # twin prime constant
EULER_GAMMA = 0.5772156649015329


def escape_counts_exhaustive(primes):
    """Measured escape counts: {(mask, signed step index)} over Z/prod."""
    N = prod(primes)
    k = len(primes)
    unit = bytearray(N)
    for n in range(N):
        unit[n] = 1 if gcd(n, N) == 1 else 0
    steps = [(g, s) for g in primes for s in (1, -1)]
    counts = {}     # mask -> [count per signed step]
    sizes = {}      # mask -> class size
    for n in range(N):
        if unit[n]:
            continue
        mask = 0
        for i, p in enumerate(primes):
            if n % p == 0:
                mask |= 1 << i
        if mask not in counts:
            counts[mask] = [0] * len(steps)
            sizes[mask] = 0
        sizes[mask] += 1
        row = counts[mask]
        for j, (g, s) in enumerate(steps):
            if unit[(n + s * g) % N]:
                row[j] += 1
    return counts, sizes, steps


def escape_count_rule(primes, mask, g):
    """Predicted escape count for class `mask` via one signed step g."""
    S = {p for i, p in enumerate(primes) if mask & (1 << i)}
    if g in S:
        return 0
    return (g - 1) * prod(p - 2 for p in primes if p not in S and p != g)


def verify_rung(primes):
    counts, sizes, steps = escape_counts_exhaustive(primes)
    checked = mismatches = 0
    for mask, row in counts.items():
        S = {p for i, p in enumerate(primes) if mask & (1 << i)}
        assert sizes[mask] == prod(p - 1 for p in primes if p not in S)
        for j, (g, s) in enumerate(steps):
            pred = escape_count_rule(primes, mask, g)
            checked += 1
            if row[j] != pred:
                mismatches += 1
                print(f"    MISMATCH S={sorted(S)} step={s*g}: "
                      f"measured {row[j]} predicted {pred}")
    return counts, sizes, steps, checked, mismatches


def main():
    # ----- I. exhaustive verification k = 3..7 -----
    print("=== I. ESCAPE RULE, EXHAUSTIVE k = 3..7 ===")
    k7 = None
    for k in range(3, 8):
        primes = PRIMES_ALL[:k]
        counts, sizes, steps, checked, bad = verify_rung(primes)
        n_classes = len(counts)
        assert n_classes == 2 ** k - 1, n_classes   # every nonempty S occurs
        print(f"  k={k} N={prod(primes)}: {n_classes} classes x "
              f"{len(steps)} signed steps = {checked} exact counts, "
              f"mismatches: {bad}")
        assert bad == 0
        if k == 7:
            k7 = (primes, counts, sizes, steps)

    # ----- II. k = 7 reference -----
    print("\n=== II. k = 7 (Z/510510) REFERENCE ===")
    primes, counts, sizes, steps = k7
    print("  class S (null channels) -> escape probability per signed step")
    print("  (single-prime and {2,...} classes; full table is rule-exact)")
    for mask in sorted(counts, key=lambda m: (bin(m).count('1'), m)):
        S = sorted(p for i, p in enumerate(primes) if mask & (1 << i))
        if len(S) > 2:
            continue
        probs = []
        for g in primes:
            c = escape_count_rule(primes, mask, g)
            probs.append(f"{g}:{c / sizes[mask]:.3f}")
        print(f"    S={S}: " + "  ".join(probs))

    # parity dichotomy + origin, asserted from the measured counts
    for mask, row in counts.items():
        S = {p for i, p in enumerate(primes) if mask & (1 << i)}
        for j, (g, s) in enumerate(steps):
            if 2 not in S and g != 2:
                assert row[j] == 0          # odd step from odd non-unit
            if g == 2 and 2 in S:
                assert row[j] == 0          # 2-step from even non-unit
    full = (1 << 7) - 1
    assert sizes[full] == 1                  # the origin's class is {0}
    assert all(c == 0 for c in counts[full])  # and it never escapes
    nonzero_escapers = sum(1 for m in counts
                           if m != full and sum(counts[m]) > 0)
    assert nonzero_escapers == 2 ** 7 - 2    # every other class escapes
    print("  parity dichotomy + escape-proof origin class: asserted "
          f"(126/126 nonzero classes escape, class {{0}} does not)")

    # ----- III. the k = 5 archive table -----
    print("\n=== III. k = 5 ARCHIVE TABLE (Z/2310), NOW EXACT ===")
    primes5 = PRIMES_ALL[:5]
    print("  mean unit neighbors (out of 10) per coupling class:")
    means = []
    for r in range(1, 6):
        for S in combinations(primes5, r):
            Sset = set(S)
            size = prod(p - 1 for p in primes5 if p not in Sset)
            total = sum(2 * escape_count_rule(primes5,
                        sum(1 << primes5.index(p) for p in S), g)
                        for g in primes5)
            mean = total / size
            means.append(mean)
            coupling = prod(S)
            print(f"    S={sorted(S)} (coupling {2310 // coupling}"
                  f" x{size}): {mean:.3f}")
    print(f"  range across classes: {min(means):.3f} .. {max(means):.3f}")

    # class-level vs per-element: stuck non-units (no signed step escapes)
    N5 = 2310
    stuck = [n for n in range(1, N5)
             if gcd(n, N5) > 1
             and all(gcd((n + s * g) % N5, N5) > 1
                     for g in primes5 for s in (1, -1))]
    print(f"  stuck nonzero non-units in Z/2310 (per-element): "
          f"{len(stuck)} (first: {stuck[:4]})")
    assert len(stuck) == 122 and stuck[:2] == [5, 7]

    # ----- IV. asymptotics: the twin-prime constant -----
    print("\n=== IV. THE 2-BOOST IS THE TWIN-PRIME PRODUCT ===")
    # twin-unit density at k=7, exact
    N7 = prod(PRIMES_ALL)
    twin_pred = prod(p - 2 for p in PRIMES_ALL if p > 2)
    twin_meas = sum(1 for n in range(N7)
                    if gcd(n, N7) == 1 and gcd(n + 2, N7) == 1)
    print(f"  twin units at k=7: measured {twin_meas}, "
          f"prod(p-2 odd p) = {twin_pred}")
    assert twin_meas == twin_pred

    # A(k) = prod (p-2)/(p-1) vs 2*C2*e^-gamma / ln p_k
    LIMIT = 1_300_000
    sieve = bytearray([1]) * (LIMIT + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(LIMIT ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    A = 1.0
    k = 1   # p = 2 counted, contributes no factor
    print("  A(k) = prod_(3<=p<=p_k) (p-2)/(p-1)  vs  2*C2*e^-gamma/ln p_k")
    targets = {7, 10, 100, 1_000, 10_000, 100_000}
    for p in range(3, LIMIT + 1):
        if not sieve[p]:
            continue
        k += 1
        A *= (p - 2) / (p - 1)
        if k in targets:
            model = 2 * C2 * exp(-EULER_GAMMA) / log(p)
            print(f"    k={k:>6} p_k={p:>8}: A={A:.6f} model={model:.6f} "
                  f"ratio={A / model:.4f}")
    print("\nALL ASSERTS PASSED")


if __name__ == "__main__":
    main()
