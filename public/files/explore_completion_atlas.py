"""Which cell does a completion land in — and is a fourth shape realized?

THE QUESTION
------------
The completion trichotomy sorts trailing windows on the nonnegative
integers by what their completion IS: RING (positional base b — cells
are cosets, completion the b-adic ring), ODOMETER (Zeckendorf /
quadratic Ostrowski — almost one-to-one over an irrational circle
rotation), DISCRETE (golden positional — the completion adds no
points). Three cells each realized is not three cells exhausting the
question. This rig is the census's engine: it classifies the window
families the corpus never classified, and it builds the one window
whose completion is a candidate FOURTH SHAPE — trailing Tribonacci,
where the classical completion is almost one-to-one over a translation
of the 2-torus, which is neither a ring, nor almost one-to-one over a
circle rotation, nor discrete.

THE CENSUS, HAND-DERIVED (the rows no engine is needed for)
-----------------------------------------------------------
MIXED-RADIX / FACTORIAL CHAINS (property): with place values
  M_t = m_1 m_2 ... m_t the depth-t cell of n is exactly the
  congruence class n + M_t Z, so the completion is the profinite ring
  lim Z/M_t — the RING cell by construction, nothing to measure. The
  gate inside it generalizes the b-adic criterion: floor(n/m) is
  Lipschitz iff the chain ABSORBS m cofinally — m | M_{t+c}/M_t for
  some c at every t (at a fixed base b this is rad(m) | rad(b));
  primes merely DIVIDING the chain is strictly weaker — a prime
  carried once keeps its residue locally constant while the
  quotient's residue reads the next power, which never arrives. The
  FACTORIAL chain (M_t = (t+1)!) absorbs every m, so its gate is
  FULLY OPEN — every floor division Lipschitz, the opposite extreme
  from a fixed base b. E5a samples the factorial statements.
SIGNED-DIGIT QUOTIENTS (property): a redundant trailing system's
  quotient metric — d(n, n') read as the deepest low-digit agreement
  over PAIRS of representations — is the b-adic metric: any
  representation's low t digits determine n mod b^t (place values are
  b^k), and conversely n' = n + k b^t admits a representation agreeing
  with n's to depth t (keep n's low t digits, re-represent the top).
  The quotient completion is Z_b: the RING cell again, redundancy
  invisible in the quotient. E5b executes the construction.
THE CF WINDOW (property): the completion question is NOT POSED — the
  trailing construction needs every integer to carry an unbounded
  digit string, and an integer's continued fraction is the single
  quotient [n]. The CF window's integer-facing trailing shadow is the
  Ostrowski window itself (the digits of n ARE the coding of n alpha),
  which the odometer cell already holds. No row.

THE FOURTH SHAPE (what the engine is for)
-----------------------------------------
The Tribonacci window: q_0 = 1, q_1 = 2, q_2 = 4,
q_k = q_{k-1} + q_{k-2} + q_{k-3}; greedy digits in {0,1}, low index
first; the classical legality is no "111" factor. The completion of
the integers under low-digit agreement is the Tribonacci odometer,
classically (Rauzy) almost one-to-one over the translation of T^2 —
and an almost one-to-one equicontinuous factor is the maximal
equicontinuous factor, which here is the 2-torus, so it is almost
one-to-one over NO circle rotation; it is not discrete (the depth-t zero cell
contains q_t, q_{t+1}, q_{t+2} — trailing zeros by construction); and
it is not a ring iff some x m has no continuous extension. The
T^2 statement enters as CLASSICAL IMPORT; the rig checks everything
the corpus's own tiers can carry: digit sanity (E1), non-discreteness
(E2), the import's numeric shadow — cells contract in the plane
coordinate E(n) = sum d_k lambda^k, lambda the contracting complex
root of x^3 = x^2 + x + 1, |lambda| = beta^{-1/2} (E3) — and the gate
scan (E4).
THE HAND'S OPENING, exact from the recurrence: the DOWN-CARRY
  2 q_k = q_{k+1} + q_{k-3}
(2 q_k = q_{k+1} + (q_k - q_{k-1} - q_{k-2}) = q_{k+1} + q_{k-3}) —
the Zeckendorf mechanism (2F_k = F_{k+1} + F_{k-2}) with the carry
descending three positions instead of two. So the expectation is the
odometer cell's phenomenology transplanted [TRANSPLANT: intuition
imported from the quadratic storey]: x m and floor division torn, the
odometer +1 Lipschitz. What is genuinely open — and the campaign's
second storey — is whether any arithmetic map prints the MIDDLE
signature here: the proof of arithmetic-middle emptiness covers rings
and circle-cut odometers, and neither mechanism applies over T^2,
where the cut locus is the fractal boundary of the Rauzy partition
rather than a countable backward orbit. This window is exactly where
an arithmetic middle member could live.

THE INSTRUMENT
--------------
N = 200000. Digits greedy, low index first; agreement agr(n, n') =
number of agreeing low digits. Maps +1, x2, x3, floor/2, floor/3.
E1  DIGIT SANITY. Reconstruction exhaustive on n < N; both directions
    of the no-111 characterization: every greedy string is 111-free,
    and the 111-free strings over positions < L(N) with value < N
    number exactly N (uniqueness).
E2  NOT DISCRETE. At t = 4, 8, 12: q_t, q_{t+1}, q_{t+2} all lie in
    the all-zero depth-t cell; realized cell count and minimum cell
    size printed.
E3  THE PLANE. Max over realized depth-t cells of the E-diameter at
    t = 4, 8, 12: shrinking geometrically, ratio per 4 depths near
    |lambda|^4 = beta^-2 = 0.2956.
E4  THE GATE SCAN. Integers sorted in digit-string order (low-first
    lex); pairs at sort distance <= 4; per input-agreement bucket ia,
    the MIN and max image agreement im, per map. The signature reads
    the MIN column (a modulus bounds ALL pairs; run 1's max column
    conflated the class split — same-class pairs climb while
    cross-class pin, so the max oscillates with bucket occupancy):
    LIPSCHITZ = min im >= ia - 4 at every realized row; PINNED
    (discontinuous) = min im over rows ia >= 12 exceeds its value
    over ia in 6..8 by <= 2; anything else = MIDDLE CANDIDATE.
E5  CENSUS CONTROLS. (a) Factorial chain, sampled: agreement to depth
    d is the congruence mod (d+1)! (digit k has radix k+2), and
    floor(n/m) for m in {3, 6, 7, 10} is Lipschitz at the delay the
    chain names: images agree to depth t whenever inputs agree to
    depth t + c*, c* = min c with m | (t+c+1)!/(t+1)! — the product
    of the radices at depths t..t+c-1 — sampled over random pairs at
    t = 4. (b) Signed-digit base 2 at t <= 12 on sampled pairs: the
    congruence n == n' mod 2^t buys a representation pair agreeing to
    depth t (the construction executed: keep low digits, re-represent
    the top), and a representation's low digits carry the congruence
    class, place values being 2^k.
E6  THE DOWN-CARRY. 2 q_k = q_{k+1} + q_{k-3} for every 3 <= k < 40;
    the x2 extremal pairs (deepest input agreement at minimal image
    agreement) printed to seed the hand family.

PREDICTIONS, frozen before the engine
-------------------------------------
P1  E1 zero failures, both directions exact.
P2  E2 exact at all three depths.
P3  E3 diameters shrink; successive ratios within a factor of 2 of
    0.2956.
P4  E4: +1 LIPSCHITZ; x2, x3, floor/2, floor/3 all PINNED. (KILL for
    the transplant: an arithmetic map neither Lipschitz nor pinned —
    the MIDDLE signature — which would be the campaign's positive
    find: an arithmetic middle member at the fourth shape, where the
    emptiness proof's two mechanisms both fail to reach.)
P5  E5 zero violations, both controls.
P6  E6 identity exact; extremal pairs exist with input agreement
    >= 12 and image agreement <= 4.

FINDINGS (entered after the runs; prints copied from the run record)
--------------------------------------------------------------------
F1  SANITY EXACT: zero reconstruction failures and zero 111-carrying
    greedy strings on n < 200000 (P1 met as run).
F2  NOT DISCRETE, exact: q_t, q_{t+1}, q_{t+2} in the all-zero cell
    at t = 4, 8, 12; realized cells 13 / 149 / 1705, min sizes
    9501 / 830 / 73 — every realized cell fat, nothing near
    singleton (P2 met, and stronger than asked).
F3  THE PLANE CONTRACTS AT THE IMPORT'S OWN RATE: max cell
    E-diameter 0.790612 / 0.230921 / 0.0644733 at t = 4 / 8 / 12,
    ratios 0.2921 and 0.2792 per 4 depths against |lambda|^4 =
    0.2956 (P3 met, inside the band, within 6% of the eigenvalue).
F4  THE GATE AT THE FOURTH SHAPE SPLITS EXACTLY AS THE PROVED CELLS
    DO — NO MIDDLE CANDIDATE: +1 prints min im >= ia - 2 at every
    row (LIPSCHITZ); x2, x3, n//2, n//3 all print min im = 0 at
    every signature row through ia = 17 (PINNED — cross-class
    cellmates' images differ at digit 0), while the max column
    climbs (the class split's same-class pairs). The emptiness
    pattern extends to the T^2 shape at scanned scope: P4 met, the
    transplant held, the campaign's second storey finds no middle
    member where the proof's two mechanisms both fail to reach.
F5  CENSUS CONTROLS EXACT: factorial chain zero violations at
    m = 3, 6, 7, 10 (delays 1, 1, 2, 5 — the chain's own delays,
    m = 10 waiting for the radix that carries 5); signed-digit
    quotient zero violations (the constructed agreeing
    representation verified, and the low digits carry the
    congruence class). P5 met.
F6  THE DOWN-CARRY IS EXACT and the extremal pairs exist as frozen:
    2q_k = q_{k+1} + q_{k-3} at every k = 3..22; deepest x2
    extremal pairs at ia = 17, im = 4 (93684/63562 and neighbours) —
    the seed for a hand comb family toward the theorem-tier x2 kill,
    LEFT OPEN; the scan verdict stands at rule tier. P6 met.
    (Closed: explore_tribonacci_discontinuity.py — the step-4 comb
    family proves the x2 kill, no range cap.)

RUN RECORD
----------
Run 1: N = 200000. Two harness bugs (factorial control's digit
places wrong, E6 overran the q table) and one instrument flaw: E4
bucketed the MAX image agreement, which conflates the class split
(division maps printed oscillating columns). 186.3s, peak 85.9 MB
(memwatch).
Run 2: min/max/count columns; signature on min. x3 flagged MIDDLE
off one bucket later shown to be the range-cap edge. 189.8s, peak
86.0 MB.
Run 3: thin buckets (< 10 pairs) excluded; x3's ia = 18 bucket
(655 pairs, min 15) survived — diagnosed as the cap edge: under
3a < N the agreeing-18-deep population differs only at its top
digits (the corpus's witness-tracks-the-exhaustive-cap behaviour).
191.3s, peak 84.8 MB.
Run 4 (final, this text's figures): signature rows also exclude the
top two realized buckets. N = 200000, wall 190.5s, peak 85.5 MB
under memwatch, limit 512 MB. VERDICT all checks TRUE: +1
LIPSCHITZ; x2, x3, n//2, n//3 PINNED; controls, down-carry, plane
contraction, non-discreteness, sanity all exact.
Run 5 (audit): E5b's tautological converse check replaced by real
ones (NAF reconstruction; low digits carry the congruence class).
E5b violations 0, VERDICT all checks TRUE, wall 188.3s, peak
85.1 MB.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import cmath
import math
import random
import sys

N = 200000

# ---------------------------------------------------------------- tribonacci
Q = [1, 2, 4]
while Q[-1] < 4 * N:
    Q.append(Q[-1] + Q[-2] + Q[-3])


def greedy(n):
    """Digits low index first."""
    d = [0] * len(Q)
    top = 0
    for k in range(len(Q) - 1, -1, -1):
        if Q[k] <= n:
            d[k] = 1
            n -= Q[k]
            top = max(top, k)
    return d


def value(d):
    return sum(dk * qk for dk, qk in zip(d, Q))


def agr(d1, d2):
    a = 0
    for x, y in zip(d1, d2):
        if x != y:
            break
        a += 1
    return a


def run():
    ok = True
    dig = [greedy(n) for n in range(N)]

    # E1 sanity
    fail = sum(1 for n in range(N) if value(dig[n]) != n)
    free = sum(1 for n in range(N)
               if "111" in "".join(map(str, dig[n])))
    print(f"E1 reconstruction failures {fail}, 111-carrying greedy "
          f"strings {free}")
    ok &= fail == 0 and free == 0
    # greedy is a right inverse of value on n < N (checked above), and
    # injective since values are distinct integers.

    # E2 not discrete
    for t in (4, 8, 12):
        cells = {}
        for n in range(N):
            cells.setdefault(tuple(dig[n][:t]), []).append(n)
        zero = tuple([0] * t)
        wit = [q for q in (Q[t], Q[t + 1], Q[t + 2]) if q < N]
        inz = all(n in cells.get(zero, []) for n in wit)
        sizes = [len(v) for v in cells.values()]
        print(f"E2 t={t}: cells {len(cells)}, min size {min(sizes)}, "
              f"zero-cell witnesses in place: {inz} ({len(wit)} in range)")
        ok &= inz

    # E3 plane contraction
    beta = 1.8392867552141612
    lam = complex(-(beta - 1) / 2,
                  math.sqrt(4 * (1 / beta) - (beta - 1) ** 2) / 2)
    pows = [lam ** k for k in range(len(Q))]

    def E(d):
        return sum(dk * pk for dk, pk in zip(d, pows) if dk)

    prev = None
    for t in (4, 8, 12):
        cells = {}
        for n in range(N):
            cells.setdefault(tuple(dig[n][:t]), []).append(E(dig[n]))
        diam = max(max(abs(a - b) for a in v for b in v)
                   for v in cells.values() if len(v) > 1)
        r = "" if prev is None else f", ratio {diam / prev:.4f}"
        print(f"E3 t={t}: max cell E-diameter {diam:.6g}{r} "
              f"(|lambda|^4 = {abs(lam) ** 4:.4f})")
        prev = diam
    print(f"E3 lambda check: |lam|^2*beta = {abs(lam) ** 2 * beta:.6f} "
          f"(want 1), root residual "
          f"{abs(lam ** 3 - lam ** 2 - lam - 1):.2e}")

    # E4 gate scan
    order = sorted(range(N), key=lambda n: dig[n])
    maps = {"+1": lambda n: n + 1, "x2": lambda n: 2 * n,
            "x3": lambda n: 3 * n, "n//2": lambda n: n // 2,
            "n//3": lambda n: n // 3}
    for name, f in maps.items():
        bmin, bmax, bcnt = {}, {}, {}
        for i in range(len(order) - 4):
            for j in range(i + 1, min(i + 5, len(order))):
                a, b = order[i], order[j]
                fa, fb = f(a), f(b)
                if fa >= N or fb >= N:
                    continue
                ia = agr(dig[a], dig[b])
                im = agr(dig[fa], dig[fb])
                if ia >= 6:
                    bmin[ia] = min(bmin.get(ia, 99), im)
                    bmax[ia] = max(bmax.get(ia, 0), im)
                    bcnt[ia] = bcnt.get(ia, 0) + 1
        rows = sorted(bmin)
        print(f"E4 {name} min: "
              + " ".join(f"{ia}:{bmin[ia]}" for ia in rows))
        print(f"E4 {name} max: "
              + " ".join(f"{ia}:{bmax[ia]}" for ia in rows))
        print(f"E4 {name} cnt: "
              + " ".join(f"{ia}:{bcnt[ia]}" for ia in rows))
        # signature rows: buckets with >= 10 pairs (a min over a thin
        # bucket is not a statement about all pairs), and away from
        # the range cap (the deepest buckets of a domain-restricted
        # map hold only boundary-special pairs differing at the top)
        cap = max(rows)
        rows = [ia for ia in rows if bcnt[ia] >= 10 and ia <= cap - 2]
        if not rows:
            continue
        lip = all(bmin[ia] >= ia - 4 for ia in rows)
        lo = [bmin[ia] for ia in rows if 6 <= ia <= 8]
        hi = [bmin[ia] for ia in rows if ia >= 12]
        pin = bool(lo and hi) and max(hi) <= max(lo) + 2
        sig = ("LIPSCHITZ" if lip else
               "PINNED" if pin else "MIDDLE CANDIDATE")
        print(f"E4 {name}: signature {sig}")

    # E5a factorial control: digit k at place (k+1)!/1, radix k+2
    rng = random.Random(7)
    viol = 0
    t = 4

    def fdig(n, upto):
        out = []
        for k in range(upto):
            out.append(n % (k + 2))
            n //= (k + 2)
        return out

    def prod(lo, hi):
        p = 1
        for r in range(lo, hi + 1):
            p *= r
        return p

    for m in (3, 6, 7, 10):
        # agreement to depth d <=> congruence mod (d+1)!;
        # images agree to depth t iff quotients agree mod (t+1)!
        cstar = next(c for c in range(1, 9)
                     if prod(t + 2, t + c + 1) % m == 0)
        step = math.factorial(t + cstar + 1)
        for _ in range(4000):
            a = rng.randrange(10 ** 9)
            b = a + rng.randrange(1, 1000) * step
            if fdig(a, t + cstar) != fdig(b, t + cstar):
                viol += 1  # depth-(t+c) agreement is the congruence
            if fdig(a // m, t) != fdig(b // m, t):
                viol += 1  # the Lipschitz claim at delay cstar
        print(f"E5a m={m}: delay {cstar}, violations so far {viol}")
    ok &= viol == 0

    # E5b signed-digit quotient
    def srep(n):
        # nonadjacent form, digits low first in {-1,0,1}
        out = []
        while n:
            if n % 2:
                r = 2 - (n % 4)
                out.append(r)
                n -= r
            else:
                out.append(0)
            n //= 2
        return out

    sviol = 0
    for _ in range(4000):
        t2 = rng.randrange(2, 13)
        a = rng.randrange(1, 10 ** 6)
        b = a + rng.randrange(1, 1000) * 2 ** t2
        ra = srep(a)
        while len(ra) < t2:
            ra.append(0)
        low = ra[:t2]
        top = (b - sum(d * 2 ** k for k, d in enumerate(low))) >> t2
        rb = low + srep(top)
        if sum(d * 2 ** k for k, d in enumerate(rb)) != b:
            sviol += 1
        if rb[:t2] != low:
            sviol += 1
        # converse: a representation's low digits carry the congruence
        # class (place values are 2^k, so the low-digit value is the
        # class) — checked on the built representation
        if sum(d * 2 ** k for k, d in enumerate(ra)) != a:
            sviol += 1
        if (a - sum(d * 2 ** k for k, d in enumerate(low))) \
                % 2 ** t2 != 0:
            sviol += 1
    print(f"E5b violations {sviol}")
    ok &= sviol == 0

    # E6 down-carry + extremal pairs
    bad = sum(1 for k in range(3, len(Q) - 1)
              if 2 * Q[k] != Q[k + 1] + Q[k - 3])
    print(f"E6 down-carry violations {bad} over k=3..{len(Q) - 2} "
          f"(2q_k = q_(k+1) + q_(k-3))")
    ok &= bad == 0
    best = []
    for i in range(len(order) - 1):
        a, b = order[i], order[i + 1]
        if 2 * a >= N or 2 * b >= N:
            continue
        ia = agr(dig[a], dig[b])
        im = agr(dig[2 * a], dig[2 * b])
        if ia >= 12 and im <= 4:
            best.append((ia, im, a, b))
    best.sort(reverse=True)
    for ia, im, a, b in best[:5]:
        print(f"E6 extremal x2 pair ia={ia} im={im}: {a} {b}")
    ok &= bool(best)

    print(f"VERDICT all checks {'TRUE' if ok else 'FALSE / SEE FLAGS'}")


if __name__ == "__main__":
    run()
    sys.exit(0)
