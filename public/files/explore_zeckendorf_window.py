"""The Zeckendorf window: the two-gates law probed at a fourth window.

THE QUESTION
------------
The two-gates law holds at rule tier at three windows — trailing
b-adic, leading positional, continued fraction (the records live in
explore_reading_geometry.py and the explore_cf_*.py scripts) — and
is conjectured general: a window's multiplication-like maps are
readable at bounded delay iff the map is a unit of the window's
native structure. This script builds a FOURTH window, neither
positional nor continued-fraction, and measures the gate there.

THE WINDOW. The trailing Zeckendorf window on Z. Digits by greedy
Zeckendorf: n = sum d_k F_k (k >= 2, F_2 = 1, F_3 = 2, d_k in {0,1},
no two adjacent 1s). The depth-t cell of n is the set of integers
agreeing with n on the t low-order digits d_2..d_{t+1}. Cells
partition Z at each depth and nest across depths; the induced
first-disagreement metric is an ultrametric by construction. The
cover is NON-POSITIONAL: a depth-t cell is not a congruence class
mod W_t (base-b cells are cosets of b^t Z; Zeckendorf cells are
Sturmian-structured sets — the low digits of n are determined by
where n/phi falls mod 1 in a three-distance interval partition, the
Ostrowski correspondence). THE AXIS PROBED is the cover's
positionality: the arithmetic stays golden (weights F_k, ratios ->
phi) while the cells stop being cosets. The CONTROL that varies the
OTHER axis — the golden-mean POSITIONAL base, base-phi digit cells,
positional with the same arithmetic — is a named later leg (the
dual-pole mirror-rungs re-entry), deliberately not in this rig.

THE NATIVE STRUCTURE. The base ratio phi is a UNIT of Z[phi]
(Z[1/phi] = Z[phi]; units +-phi^k). The base's own mult/div are the
SHIFTS on digit strings: right shift R(n) = sum d_{k+1} F_k (drop
d_2; division-by-phi-like), left shift L(n) = sum d_k F_{k+1}
(multiplication-by-phi-like) — both carry-free on strings. Integer
m >= 2 is an ELEMENT of Z[phi] but NOT a unit (norm m^2). Base-b
trailing reads mult by any integer at delay 0 because carries
propagate only upward; Zeckendorf doubling has a DOWN carry
(2 F_k = F_{k+1} + F_{k-2}), so high digits can rewrite low digits.
Hand witness (pre-engine): 3 = "001" and 11 = "00101" (strings
low-to-high from d_2) agree on d_2..d_5; their doubles 6 = "1001"
and 22 = "1000001" disagree at d_5 — delay >= 1. The cascade shape
is the COMB n = F_K + F_{K-2} + F_{K-4} + ...: doubling each tooth
emits F_{k+1} + F_{k-2} and adjacent teeth interact, so carries walk
down the comb.

WHAT EITHER PRINT MEANS (weighed after the run, frozen before it):
c_min(x2, t) growing with t means the unit gate holds at this window
by a NEW mechanism — carry misalignment, not the CF window's rate
forcing (the Zeckendorf roof is near-constant, so scale rates always
match and rate forcing is unavailable). A plateau means the
two-gates law REFINES: trailing multiplication is gated by
INTEGRALITY, not unit-ness (matching base-b, where non-unit mult
reads at delay 0), and the Zeckendorf row files the division side.

PREDICTIONS, FIXED BEFORE THE RUN (as observables; the rig prints
c_min(f, t) = least c such that every sampled pair with input
agreement depth >= t + c has image agreement depth >= t, capped at
C_MAX):
  P1 (control)  f = id:   c_min = 0 at every t.
  P2 (control)  f = n+1:  c_min bounded and small (expected <= 2;
      +1 carries propagate up only — the odometer).
  P3 (unit half) f = L, R: c_min = 0 for L, 1 for R, at every t
      (structural, carry-free on strings; R consumes d_2 to emit
      nothing — one digit of lookahead. Corrected by hand-attack
      BEFORE the run from an initial "both 0").
  P4 (the gate) f = 2n, 3n: c_min(t) grows with t, no plateau over
      the tested range. KILL for the gate reading: a plateau holding
      across the top half of the t range.
  P5 (roof)     depth-t cylinder counts over interior digit
      patterns take at most TWO values (by last-digit class), count
      ratio -> phi.
  TRANSPLANT MARKS: P4's growth intuition is imported from the CF
  det gate (a different mechanism — rate forcing); the comb
  mechanism is this window's own. P2's bound is imported from
  adic-odometer continuity folklore, not from a corpus row.

THE DESIGN
----------
Exhaustive over n < F_LIM (no sampling): group integers by their
depth-(t+c) low-digit string, and call (t, c) READABLE iff every
group maps into one depth-t image cell. Digit extraction by greedy
Zeckendorf only — no closed form from the target laws enters the
rig.

E1  DIGIT SANITY + POSITIVE CONTROLS. Greedy digits reconstruct n
    and never carry adjacent 1s (exhaustive to F_LIM). c_min(id, t)
    must print 0 and c_min(L, t) = c_min(R, t) = 0 before any gate
    verdict is read (P1, P3 as controls).
E2  THE GATE TABLE. c_min(f, t) for f in {n+1, 2n, 3n, 4n,
    floor(n/2)} over t = 1..T_MAX, c capped at C_MAX; prints the
    full table and flags growth vs plateau.
E3  THE COMB WITNESS. For growing K, the comb pairs
    (comb(K, j), comb(K, j') truncated) — explicit pairs realizing
    the E2 delays for x2: prints input agreement depth vs image
    agreement depth along the comb family.
E4  THE ROOF. Depth-t cylinder counts among n < F_LIM for interior
    t: the set of distinct counts by last-digit class, and the
    ratio of the two class counts against phi.
E5  EXTREMAL WITNESSES. For f = 2n and the shallowest output depth
    t = 1: the deepest input agreement D realized by a pair whose
    images already differ at d_2, with the pair printed — separates
    a real delay ceiling from range exhaustion (depth-24 classes
    are singletons below F_LIM, so D is data-capped at 23).

RUN RECORD
----------
One run, exhaustive over n < F_26 = 121393; T_MAX = 14, C_MAX = 12;
seconds, trivial memory. E1 digit sanity: 0 failures. All controls
green before any verdict was read.

FINDINGS (each at its own tier)
-------------------------------
F1  THE UNIT FAMILY READS (rule at scanned scope). c_min(L, t) = 0,
    c_min(R, t) = 1, c_min(n+1, t) = 1, uniformly over t = 1..14 —
    the shifts (the base's own mult/div by phi) and the odometer
    read at bounded delay, exactly as the corrected predictions said
    (P1, P2, P3 all land; P2 sharper than expected: exactly 1).
F2  THE GATE BINDS EVERY TESTED NON-UNIT (rule at scanned scope).
    2n, 3n, 4n, n//2 are each unreadable at EVERY lookahead c <= 12
    for EVERY depth t <= 11, exhaustive below F_26. The E2 tail
    values (t = 12..14 -> c 12, 11, 10) all correspond to input
    depth 24, where depth-24 agreement classes are SINGLETONS below
    F_26 — a range-exhaustion artifact, vacuous readability, not a
    plateau. P4's kill (a genuine plateau) did not fire.
F3  THE FAILURE IS DATA-CAPPED, NOT DELAY-CAPPED (the unbounded
    shape; observation at exhaustive scope). E5: at output
    depth 1 a d_2-flipping pair for x2 exists at input agreement
    D = 23 — the deepest the range can express (24 is singleton) —
    pair (23183, 98208), difference F_25 = 75025. Adding F_25 moves
    2n by 2 F_25 = F_26 + F_22, and the down-carry from index 20
    cascades to the lowest digit. Delay grows past every bound the
    data can state.
F4  THE COMB IS NOT THE MECHANISM (negative worth keeping). The E3
    truncated-comb family realizes CONSTANT delay 2 at every K
    (out-depth = in-depth - 2) — a bounded-delay family, not the
    cascade. The real extremal pairs are E5's: one high digit
    F_K whose double's down-carry (2 F_k = F_{k+1} + F_{k-2}) walks
    a receptive low pattern all the way down.
F5  THE ROOF IS TWO-VALUED EXACTLY (rule at scanned scope). At each
    depth t in {6, 8, 10}, every last-digit-0 cylinder holds the
    same count and every last-digit-1 cylinder the same smaller
    count, the two consecutive Fibonacci numbers, ratio -> phi
    (6765/4181, 2584/1597, 987/610). Sharper than P5's "at most
    two values per class": exactly one per class. Near-constant
    roof confirmed: rate forcing is unavailable at this window, so
    F2's gate failure is a CARRY-MISALIGNMENT mechanism — a new
    mechanism slot beside the CF window's rate forcing.

THE READING. The two-gates law holds at the fourth window at rule
tier in range: readable multiplication-like maps = the units
+-phi^k of Z[phi] (shifts), and every tested non-unit fails. The
REFINEMENT the window forces: at base-b trailing, mult by ANY
integer reads at delay 0 (up-only carries), so unit-ness there
gates only division; at Zeckendorf the gate binds multiplication
itself. The uniform statement across both: lambda is readable iff
lambda acts CONTINUOUSLY on the window's completion — the b-adic
completion is a ring (all integer mult continuous); the Zeckendorf
completion is an odometer, and the evidence IN RANGE is that only
the unit action and the successor act continuously. That x2 does
not extend continuously (the odometer-not-a-ring statement) is the
CONJECTURED half — F3's witnesses are its finite shadow, the proof
open. (Settled since: explore_zeckendorf_discontinuity.py proves it
— the step-3 comb family generalizes F3's extremal pair; this rig's
in-range measurements survive as the discovery record.) Continuity
of the action, not ring membership, is the trailing gate's native
form.
"""

import sys
from fractions import Fraction

F_LIM_INDEX = 26          # exhaustive over n < F(F_LIM_INDEX)
T_MAX = 14                # depths probed
C_MAX = 12                # lookahead cap

# Fibonacci: F[2] = 1, F[3] = 2, ... (index = weight position)
F = [0, 1]
while len(F) < 40:
    F.append(F[-1] + F[-2])
# F[2] = 1, F[3] = 2, F[4] = 3, F[5] = 5 ... (F[0], F[1] unused pad)

F_LIM = F[F_LIM_INDEX]


def zeck_digits(n, width):
    """Greedy Zeckendorf digits d_2..d_{width+1}, low-to-high tuple."""
    ds = [0] * width
    k = len(F) - 1
    m = n
    while m > 0 and k >= 2:
        if F[k] <= m:
            m -= F[k]
            if k - 2 < width:
                ds[k - 2] = 1
            k -= 2          # no adjacent 1s: skip one index
        else:
            k -= 1
    return tuple(ds)


def zeck_full(n):
    """Full greedy Zeckendorf digit list d_2.. (low-to-high), minimal."""
    ds = []
    k = len(F) - 1
    m = n
    top = 0
    while m > 0 and k >= 2:
        if F[k] <= m:
            m -= F[k]
            top = max(top, k)
            ds.append(k)
            k -= 2
        else:
            k -= 1
    out = [0] * (top - 1 if top else 0)
    for k in ds:
        out[k - 2] = 1
    return out


def shift_left(n):
    """L(n) = sum d_k F_{k+1} — carry-free left shift on strings."""
    return sum(F[k + 3] for k, d in enumerate(zeck_full(n)) if d)


def shift_right(n):
    """R(n) = sum d_{k+1} F_k — drop d_2, carry-free right shift."""
    return sum(F[k + 1] for k, d in enumerate(zeck_full(n)) if d and k + 2 >= 3)


def c_min_table(f, nmax, t_max, c_max):
    """c_min(f, t): least c with (t+c)-agreement forcing t-agreement
    on images, exhaustive over 0 <= n < nmax. None = above cap."""
    # digs[n] cached at max width once
    width = t_max + c_max
    in_digs = [zeck_digits(n, width) for n in range(nmax)]
    out_digs = [zeck_digits(f(n), t_max) for n in range(nmax)]
    table = {}
    for t in range(1, t_max + 1):
        found = None
        for c in range(0, c_max + 1):
            groups = {}
            ok = True
            for n in range(nmax):
                key = in_digs[n][: t + c]
                img = out_digs[n][:t]
                prev = groups.get(key)
                if prev is None:
                    groups[key] = img
                elif prev != img:
                    ok = False
                    break
            if ok:
                found = c
                break
        table[t] = found
    return table


def comb(K, teeth):
    """F_K + F_{K-2} + ... (teeth terms)."""
    return sum(F[K - 2 * i] for i in range(teeth) if K - 2 * i >= 2)


def agree_depth(a, b, width):
    da, db = zeck_digits(a, width), zeck_digits(b, width)
    d = 0
    while d < width and da[d] == db[d]:
        d += 1
    return d


def main():
    print("Zeckendorf window rig: F_LIM = F[%d] = %d, T_MAX = %d, C_MAX = %d"
          % (F_LIM_INDEX, F_LIM, T_MAX, C_MAX))

    # E1 — digit sanity + positive controls
    bad = 0
    for n in range(F_LIM):
        ds = zeck_full(n)
        if sum(F[k + 2] for k, d in enumerate(ds) if d) != n:
            bad += 1
        if any(ds[i] and ds[i + 1] for i in range(len(ds) - 1)):
            bad += 1
    print("E1 digit sanity: reconstruction+no-11 failures = %d / %d" % (bad, F_LIM))

    for name, f in [("id", lambda n: n), ("L", shift_left), ("R", shift_right)]:
        tab = c_min_table(f, F_LIM, T_MAX, C_MAX)
        vals = sorted(set(tab.values()), key=lambda v: (v is None, v))
        print("E1 control c_min(%s): values over t=1..%d -> %s" % (name, T_MAX, vals))

    # E2 — the gate table
    print("\nE2 gate table: c_min(f, t), '.' = above cap %d" % C_MAX)
    fams = [("n+1", lambda n: n + 1),
            ("2n", lambda n: 2 * n),
            ("3n", lambda n: 3 * n),
            ("4n", lambda n: 4 * n),
            ("n//2", lambda n: n // 2)]
    header = "  t: " + " ".join("%3d" % t for t in range(1, T_MAX + 1))
    print(header)
    for name, f in fams:
        tab = c_min_table(f, F_LIM, T_MAX, C_MAX)
        row = " ".join("%3s" % ("." if tab[t] is None else tab[t])
                       for t in range(1, T_MAX + 1))
        print("%5s" % name + " " + row)

    # E3 — the comb witness for x2
    print("\nE3 comb witnesses (x2): input agree depth -> image agree depth")
    width = 30
    for K in range(8, 24, 2):
        teeth = (K - 2) // 2
        a = comb(K, teeth)
        b = comb(K - 2, teeth - 1)   # same comb, top tooth removed
        ia = agree_depth(a, b, width)
        oa = agree_depth(2 * a, 2 * b, width)
        print("  K=%2d teeth=%2d: pair (%d, %d) in-depth %2d -> out-depth %2d"
              % (K, teeth, a, b, ia, oa))

    # E4 — the roof
    print("\nE4 roof: depth-t cylinder counts by last-digit class")
    for t in (6, 8, 10):
        counts = {}
        for n in range(F_LIM):
            counts[zeck_digits(n, t)] = counts.get(zeck_digits(n, t), 0) + 1
        by_last = {0: set(), 1: set()}
        for key, ct in counts.items():
            by_last[key[-1]].add(ct)
        c0 = sorted(by_last[0])
        c1 = sorted(by_last[1])
        ratio = None
        if len(c0) <= 2 and len(c1) <= 2 and c1 and c0:
            ratio = Fraction(max(c0), max(c1))
        print("  t=%2d: last=0 counts %s | last=1 counts %s | max ratio %s (~%.4f vs phi %.4f)"
              % (t, c0, c1, ratio, float(ratio) if ratio else -1, (1 + 5 ** 0.5) / 2))

    # E5 — extremal witnesses for x2 at output depth 1
    print("\nE5 extremal x2 witnesses at output depth t=1:")
    width = 24
    digs = [zeck_digits(n, width) for n in range(F_LIM)]
    img0 = [zeck_digits(2 * n, 1)[0] for n in range(F_LIM)]
    for D in range(width - 1, 0, -1):
        seen = {}
        witness = None
        for n in range(F_LIM):
            key = digs[n][:D]
            if key in seen:
                m = seen[key]
                if img0[m] != img0[n]:
                    witness = (m, n)
                    break
            else:
                seen[key] = n
        if witness:
            m, n = witness
            print("  deepest D with a d_2-flipping pair: D=%d, pair (%d, %d), "
                  "diff %d" % (D, m, n, n - m))
            break
    else:
        print("  no witness at any D >= 1")


if __name__ == "__main__":
    sys.exit(main())
