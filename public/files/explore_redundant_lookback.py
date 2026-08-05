"""Grading a hardware-arithmetic look-back claim against the exact
redundant-window addition law.

THE QUESTION. Redundant digit sets buy constant-time addition: the sum
digit at a position is a function of that position and finitely many
positions of right context. Computer arithmetic states the depth of
that context in terms of the REDUNDANCY INDEX alone. For radix r and
symmetric digit set {-a..a}, the redundancy index is

    rho = (2a + 1) - r,

and the field's stated thresholds (Jaberipur and Parhami, "Constant-
Time Addition with Hybrid-Redundant Numbers: Theory and
Implementations", full text; the thresholds attributed there to the
generalized-signed-digit framework) are:

    "For digit sets with rho >= 3 and most cases of rho = 2 (a few
     cases of rho = 2 and all cases of rho = 1), it has been shown
     that the required look-back is 1 (2)."

Their Definition 4 fixes the units: look-back is the number of
consecutive operand positions in the RIGHT CONTEXT of position i that
contribute to the sum digit at i, and their gloss makes look-back 1
mean positions i and i-1, look-back 2 positions i, i-1, i-2. That is
exactly the lookahead c of the exact-locality game in
explore_dual_redundant.py, whose addition law is

    c_min = smallest c with r^c * rho >= 4a,

measured game-tight at (r,a) = (2,1) and (10,6).

The two laws are parameterized DIFFERENTLY, and that is the whole
question. The field's is a function of rho alone. The corpus's --
throughout, "the corpus" is this library of experiments, the law
above being explore_dual_redundant.py's -- is a
function of 4a/rho against the radix r. They agree exactly where
4a/rho <= r and must part where it does not -- which is small radix
with rich redundancy, where hardware actually lives.

TRANSPLANT, marked. The corpus law was measured at rho = 1 and rho = 3
only. Every value it asserts at rho = 2, and every value it asserts at
small radix, is carried over from the closed form and has never been
run. The closed form is the thing on trial here as much as the
field's threshold is.

THE DESIGN, frozen before the engine.

P-A The conventions reconcile with no fudge: at (2,1) both laws say 2,
    at (10,6) both say 1. If the rig reproduces those two rows the
    units are shared and the rest of the table is a real comparison.

P-B At rho = 2 the two laws disagree everywhere. rho = 2 forces
    r = 2a - 1, so 4a/rho = 2a > r for every a >= 2 and the corpus
    form gives c_min = 2 at every rho = 2 system, while the field
    calls look-back 1 the common case there.

P-C At rho >= 3 they disagree only at small radix. The corpus form
    gives 1 wherever 4a/rho <= r and 2 below that; the field says 1
    throughout. The predicted parting cells are radix 2 with a = 2
    (rho = 3) and a = 3 (rho = 5).

P-D The disagreement is not noise but a difference of FACULTY: a
    single scalar rho is being asked to price an object paying two
    independent costs -- how much slack the digit set carries (rho)
    and how much value one emitted position absorbs (r). Where those
    two are pinned together the scalar suffices; where they are free
    it cannot. So the corpus form should win at exactly the cells
    where r and a are not tied, and the field's threshold should be
    recoverable as its restriction.

KILLS, frozen as what this rig PRINTS.

K1 The game is FEASIBLE at c = 1 at any rho = 2 system -> the corpus
   closed form is not tight off its two measured rows, its generality
   was a transplant, and the field's threshold stands.
K2 The game is INFEASIBLE at c = 1 and feasible at c = 2 across the
   rho = 2 family -> the corpus form holds at a parameter value it
   had never run, and the field's rho-only threshold is loose at
   cells its own framework covers.
K3 Either verdict must hold ACROSS the family, not at one cell: a
   split verdict inside rho = 2 kills the closed form just as K1
   does, since the form is constant there.
K4 A c reported by the game whose greedy adder then computes a wrong
   sum is a harness bug, not a finding.

POSITIVE CONTROL, run and read BEFORE any verdict cell. The two rows
the corpus already measured -- (2,1) at c = 2 tight, (10,6) at c = 1
tight -- must come back through this code path, and the adder must be
exact on exhaustive short pairs at every c the game reports.

FINDINGS (post-run; the rig printed every number below).

F1 THE CONTROL HOLDS: (2,1) returns c_min = 2 and (10,6) returns
   c_min = 1 through this code path, matching the two rows
   explore_dual_redundant.py measured, with the greedy adder exact on
   all 6561 length-4 and all 28561 length-2 pairs. The units are
   shared and the rest of the table is a real comparison. P-A holds.

F2 THE CORPUS CLOSED FORM IS SUFFICIENT, NOT TIGHT, AND K1 FIRED
   [rule, exhaustive at the stated range]. The inequality
   r^c * rho >= 4a overpredicts by exactly one digit at every
   rho = 2 system: measured c_min = 1 at (3,2), (5,3), (7,4), (9,5)
   and (11,6) where the form gives 2. Those five are the ONLY cells
   it misses across the 58 symmetric systems with 2 <= r <= 12,
   2a + 1 > r, a <= 8. P-B named that disagreement exactly and named
   no winner; K1 is the kill that fired, and the form is what lost
   it. The generality was carried from two measured rows to a
   parameter value never run, and it did not survive being run.

F3 THE FIELD'S THRESHOLD IS RADIX-BLIND, AND IT BREAKS AT RADIX 2
   [observation, two witnesses, scoped to symmetric digit sets].
   The printed sentence makes look-back a function of rho alone and
   calls rho >= 3 always sufficient for look-back 1. Measured
   c_min = 2 at (2,2) with rho = 3 and at (2,3) with rho = 5. P-C
   named both cells before the run. WHAT IS GRADED IS THE SENTENCE AS
   PRINTED, and nothing beyond it: the framework it attributes the
   thresholds to was not read, so whether that framework carries a
   radix side condition the summary drops is UNCONTACTED and no claim
   is made about it. The sweep is also symmetric-digit-set only, while
   the paper's setting admits asymmetric sets -- so the hedge over
   "a few cases of rho = 2" has no witness here and is not
   contradicted either, every symmetric rho = 2 system being forced to
   odd radix r = 2a - 1 and reading at look-back 1 throughout.

F4 THE EXACT LAW [rule, exhaustive over the 58 systems above; since
   PROVED as a criterion for every radix and every contiguous digit
   set, symmetric sets included, in explore_lookahead_proof.py —
   this sweep survives as the check on that proof]:

       c_min = 1  iff  rho >= 2 and r >= 3,   else  c_min = 2.

   45 of the 58 read at 1, 13 at 2. Both stated laws agree with it on
   the large common set and fail on DISJOINT classes -- the field's
   only at r = 2, the corpus form's only at rho = 2, and rho = 2
   forces the odd radix r = 2a - 1, so the two failure sets cannot
   meet. Neither is a special case of the other: each supplies
   exactly the half the other is missing, the field's rho >= 2
   threshold being the correct condition wherever r >= 3, and the
   corpus form's sensitivity to the radix being what the field's
   sentence lacks at r = 2. BOTH HALVES OF IT ARE THE FIELD'S OWN,
   as far as contact reaches: the redundancy threshold is the
   paper's own printed sentence, and the radix condition is
   documented in the founding signed-digit framework, which is
   defined for radix 3 and above and whose standard carry-free
   algorithm is reported failing at radix 2. That founding paper was
   NOT read -- the point rests on secondary sources -- and whether
   the field anywhere states the two together as an IFF is
   uncontacted. What this rig establishes is the iff, not its
   priority.

F5 THE PARAMETERIZATION IS THE DEFECT, in both directions [reading
   of F2-F4]. A single scalar rho prices an object paying two
   independent costs: how much slack the digit set carries, and how
   much value one emitted position absorbs. The field's family gives
   one knob and is radix-blind by construction. The corpus form
   holds both parameters but bundles them into one ratio, 4a/rho
   against r, which is a MARGIN where the truth is a threshold plus
   a side condition -- so it survives wherever the margin happens to
   round the same way and fails on the class where it does not.
   P-D SPLIT ON EXACTLY THAT, and the half that failed is the
   instructive one: the diagnosis above is its surviving half, while
   its PREDICTED OUTCOME did not survive -- it expected the corpus
   form to win and the field's threshold to come back as that form's
   restriction, where F4 has them failing on disjoint classes with
   neither a special case of the other. Holding the
   better diagnosis did not make ours the better law, which is the
   whole reason the cell was worth running rather than reasoning.

F6 THE SIBLING BOUND CARRIES THE SAME DEFECT AT THE SAME CLASS
   [rule, scanned scope: m in {2,3,5,7} over six systems]. The
   scaling law for x -> m*x was verified against its closed form at
   the same two systems as addition, so rho = 2 was never run there
   either. Priced in the law's OWN two branches -- b-power part read
   at its exponent, b-coprime part at ceil(log_r(2a*m0/rho)) -- it
   misses at (3,2) for m = 2 and m = 5, at (5,3) for m = 2, and at
   (7,4) for m = 2. Every miss is by exactly one digit and every
   miss sits at rho = 2; nothing at rho = 1 or rho >= 3 moved. So
   this is not two findings but one, and its object is the Lebesgue
   MARGIN rather than either operation -- the two operations were two
   ways of asking one question.
   NO THINNESS MECHANISM IS CLAIMED, and the tempting one is false:
   rho = 1 is the THINNEST overlap and the form is exactly right
   there, at every system tested and in both operations. Whatever
   selects rho = 2 is not monotone in the overlap, and this rig does
   not identify it. What it can say is where the arithmetic puts that
   class: rho = 2 forces r = 2a - 1, so the addition form's demand
   4a/rho is exactly r + 1 -- one past the radix, so the ceiling buys
   a digit the cover turns out to already cover. That is a
   description of the class, not a mechanism, and the radix-2 rows
   are why it cannot be promoted to one: there the same excess ratio
   occurs and the extra digit is genuinely needed.
   (Settled downstream: over asymmetric contiguous digit sets the
   loss locus is a wedge in radix and slack, not a slack value, and
   the exact law gains an endpoint clause at rho = 2 --
   explore_margin_locus.py; the margin story is since PROVED at the
   criterion's scope for addition -- never underpredicting, one
   digit exactly on the wedge, explore_margin_wedge.py -- while the
   scaling bound's walk of the same wedge stays a scanned rule.)

RUN RECORD: pure Python, integers only, no imports beyond the
standard library; the largest state set is a few hundred residues.
Well under the analysis memory ceiling; seconds of wall clock. The
paper's text was read in full.
"""

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def digits(a):
    return list(range(-a, a + 1))


def repunit(b, c):
    return sum(b ** i for i in range(c))


def game_feasible(b, a, c, S):
    """0 in the greatest fixed point of the residual safety game with
    injected values S, emission granularity b^c, flushable residuals
    |R| <= a * repunit(b, c). Same game as explore_dual_redundant.py."""
    F = a * repunit(b, c)
    win = set(range(-F, F + 1))
    changed = True
    while changed:
        changed = False
        for R in list(win):
            for s in S:
                pre = b * R + s
                if not any(pre - e * b ** c in win for e in digits(a)):
                    win.discard(R)
                    changed = True
                    break
    return 0 in win


def transducer_run(b, a, c, injected):
    """Greedy residual transducer at granularity b^c, then c flush
    digits; None if stuck. Exactness re-checked by the caller."""
    R = 0
    out = []
    for s in injected:
        pre = b * R + s
        best = None
        for e in digits(a):
            R2 = pre - e * b ** c
            if abs(R2) <= a * repunit(b, c) and \
                    (best is None or abs(R2) < abs(best[1])):
                best = (e, R2)
        if best is None:
            return None
        out.append(best[0])
        R = best[1]
    for rem in range(c - 1, -1, -1):
        scale = b ** rem
        cands = [d for d in digits(a)
                 if abs(R - d * scale) <= a * repunit(b, rem)]
        if not cands:
            return None
        e = min(cands, key=lambda d: abs(R - d * scale))
        out.append(e)
        R -= e * scale
    return out if R == 0 else None


def value(b, ds):
    v = 0
    for d in ds:
        v = v * b + d
    return v


def strings(a, t):
    if t == 0:
        yield ()
        return
    for head in digits(a):
        for tail in strings(a, t - 1):
            yield (head,) + tail


def corpus_cmin(b, a):
    """Smallest c with b^c * rho >= 4a, rho = 2a + 1 - b."""
    rho = 2 * a + 1 - b
    c = 0
    while b ** c * rho < 4 * a:
        c += 1
    return c


def field_lookback(b, a):
    """The field's threshold, a function of rho alone. Returns the
    stated value, or the pair it hedges over at rho = 2."""
    rho = 2 * a + 1 - b
    if rho == 1:
        return "2"
    if rho == 2:
        return "1 (mostly)"
    return "1"


def measured_cmin(b, a, cap=4):
    """Smallest c at which the addition game is feasible, by running
    it upward from 0. None if none through the cap."""
    S = sorted(set(x + y for x in digits(a) for y in digits(a)))
    for c in range(cap + 1):
        if game_feasible(b, a, c, S):
            return c
    return None


def adder_exact(b, a, c, t):
    """Greedy adder reproduces every sum of two length-t strings."""
    n = 0
    for xs in strings(a, t):
        for ys in strings(a, t):
            out = transducer_run(b, a, c, [x + y for x, y in zip(xs, ys)])
            if out is None or value(b, out) != value(b, xs) + value(b, ys):
                return None
            n += 1
    return n


def pair_len(b, a):
    """Exhaustive pair length that keeps the sweep small."""
    return 4 if (2 * a + 1) ** 2 <= 25 else 2


CONTROL = [(2, 1, 2), (10, 6, 1)]

FAMILY = [
    # rho = 1
    (2, 1), (4, 2), (6, 3), (8, 4),
    # rho = 2
    (3, 2), (5, 3), (7, 4), (9, 5),
    # rho = 3
    (2, 2), (4, 3), (6, 4), (10, 6),
    # rho >= 4
    (2, 3), (3, 3), (5, 4),
]


def s1_control():
    print("== S1 POSITIVE CONTROL: the two measured rows ==")
    for (b, a, c_known) in CONTROL:
        c = measured_cmin(b, a)
        ok(c == c_known,
           f"control row ({b},{a}): game says c={c}, corpus record "
           f"says {c_known}")
        t = pair_len(b, a)
        n = adder_exact(b, a, c_known, t)
        ok(n is not None,
           f"control row ({b},{a}): adder wrong at c={c_known}")
        print(f"  (r,a)=({b},{a}): game c_min = {c}, record {c_known}, "
              f"adder exact on {n} length-{t} pairs")


def s2_family():
    print("== S2 THE FAMILY: measured against both laws ==")
    print("   r   a  rho | corpus | field      | measured | adder")
    rows = []
    for (b, a) in FAMILY:
        rho = 2 * a + 1 - b
        pred = corpus_cmin(b, a)
        c = measured_cmin(b, a)
        t = pair_len(b, a)
        n = adder_exact(b, a, c, t) if c is not None else None
        ok(c is not None, f"({b},{a}): no feasible c through the cap")
        ok(n is not None, f"({b},{a}): adder wrong at measured c={c}")
        rows.append((b, a, rho, pred, c))
        print(f"  {b:2d}  {a:2d}   {rho:2d} | {pred:6d} | "
              f"{field_lookback(b, a):10s} | {str(c):8s} | "
              f"{'exact' if n else 'WRONG'} ({n} pairs)")
    agree_corpus = sum(1 for r in rows if r[3] == r[4])
    print(f"  corpus form matches the measurement at "
          f"{agree_corpus}/{len(rows)} cells")
    return rows


def s3_verdict(rows):
    print("== S3 THE TWO DISAGREEMENT CLASSES ==")
    rho2 = [r for r in rows if r[2] == 2]
    print(f"  rho = 2 (field: look-back 1 in most cases): measured "
          f"{[r[4] for r in rho2]} at r = {[r[0] for r in rho2]}")
    small = [r for r in rows if r[2] >= 3 and 4 * r[1] > r[0] * r[2]]
    print(f"  rho >= 3 with 4a > r*rho (field: look-back 1): measured "
          f"{[r[4] for r in small]} at (r,a) = "
          f"{[(r[0], r[1]) for r in small]}")
    tied = [r for r in rows if 4 * r[1] <= r[0] * r[2]]
    print(f"  cells where 4a <= r*rho (the laws coincide by "
          f"construction): measured {[r[4] for r in tied]}")


def s4_sweep():
    """Every symmetric redundant system with 2 <= r <= 12 and
    2a + 1 > r, a <= 8: the measured c_min against the candidate
    'c_min = 1 iff rho >= 2 and r >= 3, else 2'."""
    print("== S4 THE SWEEP: is the threshold an iff? ==")
    cells = [(r, a) for r in range(2, 13) for a in range(1, 9)
             if 2 * a + 1 > r]
    bad = []
    counts = {}
    for (r, a) in cells:
        rho = 2 * a + 1 - r
        c = measured_cmin(r, a, cap=3)
        cand = 1 if (rho >= 2 and r >= 3) else 2
        counts[c] = counts.get(c, 0) + 1
        if c != cand:
            bad.append((r, a, rho, c, cand))
    print(f"  {len(cells)} systems swept; measured c_min counts "
          f"{dict(sorted(counts.items()))}")
    ok(not bad, f"candidate threshold fails at {bad[:6]}")
    if bad:
        print(f"  counterexamples (r,a,rho,measured,candidate): {bad}")
    else:
        print("  c_min = 1 iff rho >= 2 and r >= 3, else 2 -- holds at "
              f"all {len(cells)} systems")
    corpus_bad = [(r, a) for (r, a) in cells
                  if corpus_cmin(r, a) != measured_cmin(r, a, cap=3)]
    print(f"  the corpus closed form misses {len(corpus_bad)}/"
          f"{len(cells)} of them: {corpus_bad}")


def scaling_pred(b, a, m):
    """The corpus scaling law in its OWN two branches: split off the
    b-power part, and price the b-coprime part by the closed form
    ceil(log_b(2a*m0/rho)). Pure b-powers b^s read at s exactly."""
    rho = 2 * a + 1 - b
    s = 0
    while m % b == 0:
        m //= b
        s += 1
    if m == 1:
        return s
    c = 0
    while b ** c * rho < 2 * a * m:
        c += 1
    return s + c


def s5_scaling():
    """The sibling bound. x -> m*x was verified against the same closed
    form at the same two systems as addition, and rho = 2 was never run
    there either."""
    print("== S5 THE SIBLING BOUND: scaling at rho = 2 ==")
    miss = []
    for (b, a) in [(2, 1), (10, 6), (4, 3), (3, 2), (5, 3), (7, 4)]:
        for m in (2, 3, 5, 7):
            p = scaling_pred(b, a, m)
            S = sorted(set(m * d for d in digits(a)))
            q = next((c for c in range(6) if game_feasible(b, a, c, S)),
                     None)
            ok(q is not None, f"scaling ({b},{a}) m={m}: no feasible c")
            if q is not None and p != q:
                miss.append((b, a, 2 * a + 1 - b, m, p, q))
    print(f"  (r,a,rho,m,predicted,measured) misses: {miss}")
    off_by = {abs(x[4] - x[5]) for x in miss}
    rhos = sorted({x[2] for x in miss})
    print(f"  every miss is by {off_by} digit(s), and lands at "
          f"rho in {rhos}")


def main():
    s1_control()
    rows = s2_family()
    s3_verdict(rows)
    s4_sweep()
    s5_scaling()
    print()
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}")
        for f in FAILURES:
            print(f"  - {f}")
    else:
        print("all checks passed")


if __name__ == "__main__":
    main()
