"""The subset-sum weld — three corpus faces of one combinatorial object.

Three places state a question about subset sums of a weight list, each over a
DIFFERENT ambient group, and none of them references the others:

  FACE A (the Hamming spectrum).  The CRT neighbour graph K_2 [] K_3 [] ...
    has one eigenvalue per subset S of channels, lambda_S = deg - sum_{i in S} p_i.
    Distinct eigenvalues = distinct subset sums of the first k primes, taken in
    Z.  At k=7 the 128 subsets give 53 distinct values in the range 0..58; the
    unreachable values are 1, 4, 6 and their reflections 52, 54, 57.
    WEIGHTS: the primes themselves.  AMBIENT: an interval of Z.

  FACE B (naming coverage).  A prime s absent from a sub-ring S is named iff
    sum_{i in S} p_i^{-1} = |S| - 1  (mod s).  Naming success is subset-sum
    coverage of Z/s, governed by the Erdos-Renyi threshold: k random elements
    of an order-n abelian group have subset sums covering it once
    k >= (log n + log log n)/log 2, measured here as k_full ~ 1.36 log2(s).
    WEIGHTS: the inverses p_i^{-1} mod s.  AMBIENT: Z/s.

  FACE C (the matching gap).  A working amnesiac needs a partition that is
    spread and flat.  Necessity is a mass-majority test; sufficiency is EXACT
    SUBSET-MASS MATCHING and is not claimed weighted.  The gap between them is
    the census's price surface, and the measured breadth world is a TIE DESERT
    (0 tied route pairs across 363 fibers).
    WEIGHTS: positive masses.  AMBIENT: an ordered torsion-free group.

THE QUESTION.  Write the identification exactly, then ask what TRANSFERS.  A
transfer between faces over different groups has to state the map between the
groups and say what it preserves; a weld that does not is the failure mode, and
a rhyme with the mismatch named is a complete outcome.

THE SLATE (frozen before any engine code; TRANSPLANT flags below).

P1 -- THE SHIFT.  Face B's criterion carries a target that DEPENDS on |S|,
  which is why the corpus reads it as "miss every target" (plural) rather than
  as one subset-sum instance.  Substituting b_i = p_i^{-1} - 1 (mod s) turns it
  into sum_{i in S} b_i = -1 (mod s): a SINGLE fixed target, which is what makes
  it the same instance shape as the other two faces.
  PREDICTION: the shifted single-target form agrees with the |S|-dependent form
  on every (k, s) tested, and both agree with brute-force divisibility of -chi.
  KILL (observable): any (k, s, S) where the three disagree.

P2 -- WHERE THE DEFICIT SITS.  Faces A and B both fall short of covering their
  ambient.  If they were one phenomenon the shortfalls would have one shape.
  PREDICTION 2a (Face A, over Z): the unreachable set is a BOUNDARY effect and
  is k-independent past the first few rungs -- for every k >= 4 the subset-sum
  image of the first k primes is the full interval [0, sum p_i] minus exactly
  {1, 4, 6} and their reflections, six values, so the distinct-eigenvalue count
  is sum(p_i) - 5.  (At k=7 that is 59 - 6 = 53, the corpus number.)
  PREDICTION 2b (Face B, over Z/s): Z/s has no boundary, so the missed targets
  carry no positional structure -- their positions in 0..s-1 are uniform, which
  is the coupon-collector reading the corpus already files.
  KILL (observable): 2a fails if any k >= 4 has an unreachable value outside
  {1,4,6} and reflections.  2b fails if missed residues concentrate positionally
  (measured as a chi-square over deciles of Z/s, and as a mean-position test).

P3 -- WHAT THE AMBIENT DECIDES.  TRANSPLANT: this imports the Erdos-Renyi
  threshold, established over FINITE abelian groups (Face B), into an ordered
  torsion-free setting (Face C) where it has no statement.  Flagged as such.
  The proposed discriminator is one ratio: 2^k against the size of the ambient
  the sums can land in.  Finite group -> wrap-around piles 2^k sums into s
  slots, coverage cheap above the log threshold.  Interval of Z -> no wrap, the
  ends are thin, deficit is boundary-only.  Ordered torsion-free with generic
  weights -> the ambient is unbounded, 2^k sums are all distinct, and hitting an
  exact target is a coincidence rather than a shortfall.
  PREDICTION: quantizing Face C's weights to W levels makes the matching gap a
  THRESHOLD phenomenon rather than a peculiarity of the breadth world -- exact
  subset-mass matching succeeds at a rate that rises from 0 to 1 as 2^N grows
  past the ambient size ~ N*W, and the transition sits near the same log2 line
  Face B measures.  The tie desert is then the W -> infinity limit of one law,
  not a separate fact about normalizer products.
  KILL (observable): no transition -- success rate flat in W at fixed N, or the
  transition not tracking log2(N*W).
  NOTE ON SCOPE: this rig abstracts Face C to its FEASIBILITY PRIMITIVE (does a
  subset hit an exact target mass), not to the full spread-and-flat partition
  search.  A transfer claimed here is a claim about that primitive.

POSITIVE CONTROL (run first, before any verdict is read).  The rig must
reproduce two numbers it did not derive, both established elsewhere: the 53
distinct Hamming eigenvalues at k=7 with unreachable {1,4,6,52,54,57}
(verify_algebra.py::test_hamming_spectrum), and the k=7 read of s=41 -- the
seven inverses {21,14,33,6,15,19,29} reaching 37 of 41 residues and missing
every naming target (explore_missed_primes.py).  A failure on either means
the harness is wrong and no kill/survive reading below is admissible.

Run: python prime/code/explore_subset_sum_weld.py  (9s, peak 98.2MB)

FINDINGS (run recorded below; control PASSED before any verdict was read —
Face A gave 53 distinct with unreachable [1,4,6,52,54,57], Face B gave 37 of 41
residues and no target hit).

THE IDENTIFICATION.  All three faces are one primitive: given k weights, which
elements of the ambient are subset sums, and does a named target land in that
image.  What differs is only the ambient, and the ambient is what decides the
answer's SHAPE.  The name for that: THE AMBIENT TRICHOTOMY.

P1 SURVIVES — the shift is exact.  286,107 (k, s, S) triples over k=2..12 and
primes s<200: ZERO disagreements between the |S|-dependent form, the fixed-target
form with b_i = p_i^{-1} - 1 (mod s) and target -1, and brute-force divisibility
of -chi.  The equivalence is a one-line identity (subtract 1 from each of the |S|
terms), so the plural "targets" in the corpus reading was a presentation, not a
feature: naming IS one subset-sum instance, and the three faces are comparable
only after this shift.

P2a SURVIVES, and stronger than stated.  Over Z the image of the first k primes
is, for every k = 4..30 checked, the FULL interval [0, sum p_i] minus exactly
{1, 4, 6} and their reflections {sum-6, sum-4, sum-1}.  So the distinct-subset-sum
count is sum(p_i) - 5 at every rung, and the k=7 value 53 = 58 - 5 is one instance
of a k-independent law rather than a fact about k=7.  The deficit never grows: it
is six values at every rung, and every one of them sits at an END of the range.
AND THE MECHANISM IS COPY-AND-SHIFT, NOT PIGEONHOLE.  2^k outrunning the range
gives collisions, never coverage -- the first statement of this finding got that
backwards.  What actually happens: adding p_{k+1} sends the reached set to its
union with a translate of itself, and the two overlap and cover [7, T_{k+1}-7] as
soon as p_{k+1} <= T_k - 13.  That holds at k=5 directly (13 <= 15) and for every
k >= 6 because T_k - 2p_k starts at 15 and increases -- each rung adds p_{k+1} to
T against 2(p_{k+1} - p_k) to 2p_k, and p_{k+1} > 2(p_{k+1} - p_k) is exactly
Bertrand's p_{k+1} < 2p_k.  The three small misses survive every step because
1, 4, 6 < p_{k+1} once k+1 >= 5, and the top three are their reflections under the
complement involution.  So the law is PROVED for all k >= 5 on a base verified at
k=5, with k=4 the one rung outside the induction and checked directly.  (The
classical "every integer past 6 is a sum of distinct primes" is NOT what does this
-- it allows primes outside the first k, so it settles only v <= p_k.)

P2b SURVIVES.  Over Z/s the missed residues carry no positional structure at all:
decile chi-square against uniform is 1.5 (k=6), 1.8 (k=7), 2.6 (k=8), 3.3 (k=9)
against a 5% critical value of 16.9, and the mean relative position is 0.500,
0.500, 0.499, 0.496.  Measured over primes s in [50, 400], 1,920 to 10,018 missed
residues per rung.  A cyclic group has no ends, so nothing can sit at one.

SO FACES A AND B DO NOT TRANSFER TO EACH OTHER, and the near-identical coverage
FRACTION at k=7 (53/59 = 90% over Z, 37/41 = 90% in Z/41) is a coincidence of two
different mechanisms.  Face A's deficit is boundary and permanent; Face B's is
positional noise and vanishes as k passes the log threshold.  Reading either as
evidence for the other is the error this weld rules out.

P3 SURVIVES — and this is the transfer that is REAL.  Face C's matching gap is
Face B's coverage threshold with the ambient size read as N*W:

  N_half (smallest N with >=50% exact-match rate) against log2(N*W):
    W=2 -> 2 vs 2.00    W=4 -> 2 vs 3.00     W=16 -> 5 vs 6.32
    W=64 -> 8 vs 9.00   W=256 -> 11 vs 11.46 W=4096 -> 15 vs 15.91

N_half tracks log2(N*W) to within 1.4 across the whole sampled range of W (worst
deviation 1.32 at W=16, best 0.46 at W=256) — the same log2 line Face B measures
as k_full ~ 1.36 log2(s).  And the real-weight
limit is the W -> infinity end of that one law: at N=10, 16, 20 the subset sums of
random real weights are INJECTIVE (2^N distinct sums out of 2^N), so no target is
hit at all.  SO THE TIE DESERT HAS A GENERIC EXPLANATION AVAILABLE, WHICH IS NOT
THE SAME AS BEING EXPLAINED.  A fine enough weight supply produces the desert on
its own -- but this rig's weights are random reals and the fibers' are
interior-normalizer products, and nothing here shows the latter are fine in that
sense.  The standing verdict is untouched: a scope fact and not a theorem, since
no argument says those products cannot tie.  What the transfer buys is a REASON to
expect the measurement rather than a second measurement of it, plus a direction --
a tie must come from COARSE masses, so hunting a tying world means hunting a
coarse one, and the search that found none was searching a fine one.
SCOPE: this rig abstracts Face C to its feasibility primitive (does a subset hit
an exact target mass), not to the full spread-and-flat partition search, so the
transfer is a claim about that primitive.

WHAT THE THREE REGIMES ARE, stated once.  Finite group: wrap-around piles 2^k sums
into s slots, coverage is cheap above the log threshold, and the shortfall is
positional noise.  Bounded interval of Z: no wrap, so the interior fills by
copy-and-shift overlap and only the ENDS stay thin -- the deficit is a
boundary constant.
Ordered with real weights: the range is still bounded, but it is cut into a
CONTINUUM of slots, so the sums never pile and an exact hit is a coincidence
rather than a shortfall.  ONE discriminator across all three, the ratio of 2^k to
the number of SLOTS the sums can land in -- and what varies the slot count is the
ORDER, which cuts a bounded range into T+1 slots with thin ENDS in the second
regime and into a continuum in the third.  The cyclic ambient has s slots and no
ends, which is the whole of why it is the cheap one.

RUN RECORD.  Python 3, Windows.  Control PASS/PASS.  P1 286,107 triples, 0
disagreements.  P2a k=2..30 exhaustive.  P2b k=6..9 over primes s in [50,400].
P3 400 trials per cell, seed 20250609; the target is drawn uniformly over
[0, sum w], which includes the two endpoints the empty and full sets always
reach, so each rate is inflated by ~2/(sum w + 1) -- negligible at the sums
here and it does not move the transition.  Measured under memwatch.py: wall 9.0s,
peak working set 98.2 MB against the 512 MB ceiling.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
from math import log2, prod
from itertools import combinations
from crt import is_prime


def section(title):
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}")


def first_n_primes(n):
    out, c = [], 2
    while len(out) < n:
        if is_prime(c):
            out.append(c)
        c += 1
    return out


# --------------------------------------------------------------------------
# The shared primitive: reachable subset sums of a weight list in a group.
# --------------------------------------------------------------------------

def subset_sums_Z(weights):
    """All subset sums (including the empty sum 0) over Z."""
    reach = {0}
    for w in weights:
        reach |= {r + w for r in reach}
    return reach


def subset_sums_mod(weights, m):
    """All subset sums (including the empty sum 0) over Z/m."""
    reach = {0}
    for w in weights:
        reach |= {(r + w) % m for r in reach}
    return reach


# --------------------------------------------------------------------------
# CONTROL
# --------------------------------------------------------------------------

def control():
    section("POSITIVE CONTROL — reproduce two numbers the rig did not derive")

    primes7 = first_n_primes(7)
    total = sum(primes7)
    reach = subset_sums_Z(primes7)
    missing = sorted(set(range(total + 1)) - reach)
    print(f"Face A, k=7: primes {primes7}, total {total}")
    print(f"  distinct subset sums = {len(reach)}   (corpus: 53)")
    print(f"  unreachable = {missing}   (corpus: [1, 4, 6, 52, 54, 57])")
    ok_a = (len(reach) == 53 and missing == [1, 4, 6, 52, 54, 57])

    s = 41
    inv = [pow(p, -1, s) for p in primes7]
    reach41 = subset_sums_mod(inv, s)
    named = any(
        sum(pow(p, -1, s) for p in S) % s == (len(S) - 1) % s
        for r in range(1, 8) for S in combinations(primes7, r)
    )
    print(f"Face B, k=7, s=41: inverses {inv}   (corpus: [21,14,33,6,15,19,29])")
    print(f"  residues reached = {len(reach41)} of {s}   (corpus: 37)")
    print(f"  any naming target hit = {named}   (corpus: False)")
    ok_b = (inv == [21, 14, 33, 6, 15, 19, 29] and len(reach41) == 37
            and named is False)

    print(f"\nCONTROL: Face A {'PASS' if ok_a else 'FAIL'}, "
          f"Face B {'PASS' if ok_b else 'FAIL'}")
    return ok_a and ok_b


# --------------------------------------------------------------------------
# P1 — the shift to a single target
# --------------------------------------------------------------------------

def p1_shift(kmax=12, smax=200):
    section("P1 — THE SHIFT: |S|-dependent target vs one fixed target")

    disagreements = []
    checked = 0
    for k in range(2, kmax + 1):
        P = first_n_primes(k)
        for s in range(3, smax):
            if not is_prime(s) or s in P:
                continue
            b = [(pow(p, -1, s) - 1) % s for p in P]
            for r in range(1, k + 1):
                for idx in combinations(range(k), r):
                    lhs_orig = sum(pow(P[i], -1, s) for i in idx) % s
                    orig = (lhs_orig == (r - 1) % s)
                    shifted = (sum(b[i] for i in idx) % s == (s - 1) % s)
                    # -chi = N*(|S|-1) - sum(N/p_i), in exact integers
                    N = prod(P[i] for i in idx)
                    neg_chi = N * (r - 1) - sum(N // P[i] for i in idx)
                    brute = (neg_chi % s == 0)
                    checked += 1
                    if not (orig == shifted == brute):
                        disagreements.append((k, s, idx, orig, shifted, brute))
    print(f"(k, s, S) triples checked: {checked}")
    print(f"disagreements among |S|-target / fixed-target / brute -chi: "
          f"{len(disagreements)}")
    if disagreements:
        for d in disagreements[:5]:
            print(f"  {d}")
    return len(disagreements) == 0


# --------------------------------------------------------------------------
# P2a — Face A's deficit is a boundary effect, k-independent
# --------------------------------------------------------------------------

def p2a_face_a(kmax=30):
    section("P2a — FACE A over Z: where the unreachable values sit")

    print(f"{'k':>3} {'p_k':>5} {'total':>8} {'distinct':>9} "
          f"{'total-5':>9} {'unreachable':>28}")
    ok = True
    for k in range(2, kmax + 1):
        P = first_n_primes(k)
        total = sum(P)
        reach = subset_sums_Z(P)
        missing = sorted(set(range(total + 1)) - reach)
        pred = total - 5
        tag = ""
        if k >= 4:
            expect = sorted({1, 4, 6, total - 1, total - 4, total - 6})
            if missing != expect or len(reach) != pred:
                ok = False
                tag = "  <-- KILL"
        shown = str(missing) if len(missing) <= 6 else f"{missing[:3]}...({len(missing)})"
        print(f"{k:>3} {P[-1]:>5} {total:>8} {len(reach):>9} {pred:>9} {shown:>28}{tag}")
    print(f"\nP2a (k>=4: image = [0,total] minus {{1,4,6}} and reflections): "
          f"{'HOLDS' if ok else 'KILLED'}")
    return ok


# --------------------------------------------------------------------------
# P2b — Face B's misses carry no positional structure
# --------------------------------------------------------------------------

def p2b_face_b(kmax=9, slo=50, shi=400):
    section("P2b — FACE B over Z/s: do missed residues sit anywhere special?")

    for k in range(6, kmax + 1):
        P = first_n_primes(k)
        deciles = [0] * 10
        tot_missed = 0
        mean_rel = 0.0
        n_s = 0
        for s in range(slo, shi):
            if not is_prime(s) or s in P:
                continue
            inv = [pow(p, -1, s) for p in P]
            reach = subset_sums_mod(inv, s)
            missed = sorted(set(range(s)) - reach)
            if not missed:
                continue
            n_s += 1
            tot_missed += len(missed)
            for m in missed:
                deciles[min(9, (m * 10) // s)] += 1
                mean_rel += m / s
        if tot_missed == 0:
            print(f"k={k}: no misses in s range")
            continue
        mean_rel /= tot_missed
        exp = tot_missed / 10
        chi2 = sum((d - exp) ** 2 / exp for d in deciles)
        print(f"k={k}: {n_s} moduli with misses, {tot_missed} missed residues")
        print(f"  decile counts {deciles}")
        print(f"  chi-square vs uniform (9 df, 5% crit 16.9) = {chi2:.1f}")
        print(f"  mean relative position = {mean_rel:.3f}  (uniform: 0.500)")


# --------------------------------------------------------------------------
# P3 — the ambient decides: quantize Face C's weights
# --------------------------------------------------------------------------

def p3_ambient(trials=400, seed=20250609):
    section("P3 — FACE C: exact subset-mass matching vs weight granularity")

    rng = random.Random(seed)
    print("Exact matching of a random target mass, weights drawn from W levels.")
    print("Ambient size ~ N*W; the Erdos-Renyi line predicts the transition")
    print("near 2^N ~ N*W, i.e. N ~ log2(N*W).\n")
    print(f"{'N':>3} " + " ".join(f"{'W='+str(w):>9}" for w in
                                  (2, 4, 16, 64, 256, 4096)))
    for N in range(4, 21, 2):
        row = []
        for W in (2, 4, 16, 64, 256, 4096):
            hits = 0
            for _ in range(trials):
                w = [rng.randrange(1, W + 1) for _ in range(N)]
                target = rng.randrange(0, sum(w) + 1)
                reach = subset_sums_Z(w)
                hits += (target in reach)
            row.append(hits / trials)
        print(f"{N:>3} " + " ".join(f"{v:>9.3f}" for v in row))

    print("\nThe real-weight limit (W -> infinity): distinct subset sums out of 2^N")
    for N in (10, 16, 20):
        w = [rng.random() for _ in range(N)]
        sums = {0.0}
        for x in w:
            sums |= {t + x for t in sums}
        print(f"  N={N}: {len(sums)} distinct sums of 2^N = {2**N}  "
              f"(injective: {len(sums) == 2**N})")

    print("\nTransition line: smallest N reaching rate >= 0.5, against log2(N*W)")
    print(f"{'W':>6} {'N_half':>7} {'log2(N*W)':>10}")
    for W in (2, 4, 16, 64, 256, 4096):
        for N in range(2, 25):
            hits = 0
            for _ in range(trials):
                w = [rng.randrange(1, W + 1) for _ in range(N)]
                target = rng.randrange(0, sum(w) + 1)
                if target in subset_sums_Z(w):
                    hits += 1
            if hits / trials >= 0.5:
                print(f"{W:>6} {N:>7} {log2(N * W):>10.2f}")
                break
        else:
            print(f"{W:>6} {'>24':>7} {log2(24 * W):>10.2f}")


def main():
    if not control():
        print("\nCONTROL FAILED — no verdict below is admissible.")
        return
    p1_shift()
    p2a_face_a()
    p2b_face_b()
    p3_ambient()


if __name__ == "__main__":
    main()
