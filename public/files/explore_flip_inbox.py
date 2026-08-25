"""The replicates the level-set law sets aside: what decides their side
of one half, and is the audited sample in the answer at all?

THE QUESTION. explore_flip_level.py proved the flip is an exact level
set of A-hat -- but only where the replicate's OWN vertex G/(2B) lies
outside the box, which is where A(p) = G*p - B*p^2 is monotone. The
vertex-inside replicates are counted and set aside, and the count is not
small: 70 / 15 / 0 of 400 at the pi = 1/5 cell and 111 / 29 / 1 at the
pi = 4/5 one, so at the smallest audit size more than a quarter of the
second cell sits outside the derivation and the record says outright
that what happens there is unmeasured. This engine measures it.

  Q1  Is the set-aside one regime or several, and is the split
      derivable rather than empirical?
  Q2  Does the audited sample decide the side of 1/2 there at all?
  Q3  Does the set-aside flip at the same rate as the scored
      population -- is the reported flip rate biased by the exclusion?

WHAT THE DESIGNED CELL ALREADY ANSWERS, settled before designing
anything. explore_flip_floor.py carries cell W4, built with its
POPULATION vertex inside the box at 7/10, and it is a different object
from this one: W4 arrives at the condition deliberately and is used to
score the eight self-report ARMS, not the level-set law -- the entry it
contributes here is one number, that two in-box roots occur in 6-24% of
its replicates and the upper root takes the argmin 0.42-0.51 of the
time on floating-point residue and the candidate order. That is this
engine's sub-case (5) already priced at a designed cell, and it is
imported as a prediction rather than rediscovered. Everything else
below is the UNCONTROLLED entry at the two world cells, which W4 does
not reach: a cell designed to sit in the box says nothing about the
replicates that drift into it.

THE HAND-ATTACK (paper, before this engine). The set-aside is not one
regime; it is the estimator's own candidate list read under concavity,
and the split is exhaustive by construction rather than by measurement.
With B-hat > 0 and the vertex v = G/(2B) in [0, 1], A is concave on the
box with maximum A(v) = G^2/(4B), and the estimator returns the p in
[0, 1] whose A(p) is nearest A-hat, its candidates being {0, 1, v} plus
the real roots. So the returned TAG partitions the set-aside, and each
tag carries its own law:

  (1) tag = vert. A-hat is above A(v) (or the root interval misses the
      box entirely on one side), the nearest reachable value of A is its
      maximum, and p-hat = v EXACTLY. Then p-hat > 1/2 iff v > 1/2 iff
      G > B: the side of one half is read off the two CLASS samples
      alone. A-hat is in the answer only through which tag fires, never
      through the side.
  (2) tag = end0 and (3) tag = end1. The root interval covers the box,
      A stays above A-hat throughout, and the nearest value sits at the
      endpoint of smaller A. Then p-hat is 0 or 1 exactly, and the side
      of one half is that endpoint. A-hat-free again.
  (4) tag = root+ or root-, exactly one root in the box. The estimator
      lands on it, and the level-set law SURVIVES restricted to that
      root's branch: on the decreasing branch (r >= v) the root exceeds
      1/2 iff A-hat < A(1/2), on the increasing branch iff A-hat >
      A(1/2) -- and if 1/2 lies on the OTHER branch from the root, the
      vertex separates them and the side is decided by v alone, back to
      case (1)'s reading. A(1/2) = G/2 - B/4 is the same half-box cut
      the outside law uses.
  (5) two roots in the box. Both zero the objective EXACTLY, so the
      mathematics does not choose: the winner is decided by
      floating-point residue and the candidate order, root+ being
      offered first. This is the one sub-case where the tool's answer
      is not a fact about the sample.

So the honest reading of the set-aside is not "the law fails there". It
is that the law is REPLACED, on three of five tags, by a coarser law
that does not read the audited sample at all -- and on a fifth by
nothing.

THE TRANSPLANTS, marked. One. Sub-case (5)'s coin is imported from
explore_flip_floor.py's DESIGNED cell W4, where the population vertex
sits in the box by construction; here it is asserted at world cells
where the vertex arrives by sampling noise. PR5 states it as a range
and not as a number for exactly that reason.

THE CELLS AND THE SAMPLES. Unchanged and imported, not re-derived:
explore_flip_level.py's two world cells (12,3) at pi = 1/5 and (2,8) at
pi = 4/5, its sampler, its estimator, its audit sizes and its seed. The
draw order is replicated exactly -- cells in order, sizes in order,
replicates in order -- so the row counts must reproduce to the
replicate, which is PC1.

PREDICTIONS (fixed before the run).

  PC1  POSITIVE CONTROL, THE SAME REPLICATES. The set-aside counts
       reproduce the sibling's exactly: 70 / 15 / 0 at the pi = 1/5
       cell and 111 / 29 / 1 at the pi = 4/5 one, and the flip rates
       reproduce to three decimals (0.448 / 0.245 / 0.075 and 0.355 /
       0.168 / 0.003). A miss means the draw order moved and no count
       below is about the sibling's set-aside. Read before anything
       else.

  PC2  THE PARTITION IS EXHAUSTIVE. Every set-aside replicate carries
       one of the five tags and falls in exactly one sub-case, and
       B-hat > 0 on all of them (a vertex exists by definition of the
       set). A miss means the sub-case reading is not a partition and
       nothing below is a law.

  PR1  THE VERTEX TAG IS EXACT AND A-hat-FREE. Observable: on every
       tag = vert replicate, p-hat equals G/(2B) to float equality, and
       (p-hat > 1/2) equals (G > B). Zero exceptions, or sub-case (1)
       is wrong.

  PR2  THE ENDPOINT TAGS ARE EXACT. Observable: p-hat is exactly 0.0 on
       every end0 replicate and exactly 1.0 on every end1 replicate.

  PR3  THE BRANCH-RESTRICTED LEVEL SET HOLDS. Observable: on every
       single-in-box-root replicate the derived side of 1/2 from
       sub-case (4) equals the estimator's own. Zero exceptions, scored
       with no tolerance -- this is an algebraic statement about the
       estimator, like the outside law it extends.

  PR4  SO THE AUDITED SAMPLE IS MOSTLY OUT OF THE ANSWER. Observable:
       across the set-aside replicates of both cells, the share whose
       side of 1/2 is A-hat-free (tags vert, end0, end1, plus the
       root replicates the vertex separates from 1/2) EXCEEDS one half.
       This is the payload and it is gated: if the share is small, the
       set-aside is a level set after all and the exclusion was
       conservative bookkeeping.

  PR5  THE TWO-ROOT CASE IS A COIN, and its rate is a transplant.
       Observable, weighed not gated: two in-box roots occur on some
       set-aside replicates, both candidates' objective values sit
       within 1e-12 of zero, and the upper root's win share lies
       strictly between 0.2 and 0.8. A share of 0 or 1 makes the
       tie-break deterministic and the case a rule rather than a coin.

  PR6  THE EXCLUSION'S COST, printed and weighed. The set-aside's flip
       rate against the scored population's, per row. The counts are 70
       and 111 at the two largest set-asides and 15, 29, 0, 1 at the
       rest, so only the two n = 50 rows carry any resolution and
       nothing is gated on the others.

RUN. This file needs explore_flip_level.py beside it: the cells, the
sampler, the estimator and the seed are imported from there rather than
copied, so the two are one program in two files.

python explore_flip_inbox.py   (estimate ~5 s; 2400 replicates over two
cells and three audit sizes, the sibling's own loop with no bootstrap
and no re-splits; single process, largest array a 1000 x 15 shuffle,
memory far under the analysis ceiling.)

FINDINGS (from the printed run below; 2400 replicates, 226 of them set
aside).

F1  THE CONTROLS PASS AND THE REPLICATES ARE THE SIBLING'S. The
    set-aside counts reproduce to the replicate -- 70 / 15 / 0 and
    111 / 29 / 1 -- and the flip rates to the record's own three
    decimals at all six rows. The partition is exhaustive: all 226
    set-aside replicates carry exactly one sub-case, counts
    116 / 9 / 13 / 84 / 4 over cases (1) through (5). So what follows
    is about the set the sibling excluded and not a lookalike. PC1's
    bar was first written as an absolute 0.0005 against a
    three-decimal record and failed on three rows that in fact agreed;
    the record's precision is the bar (run record below).

F2  THE SET-ASIDE IS FIVE REGIMES AND EVERY DERIVED LAW HOLDS EXACTLY
    (rule, derived algebraically then verified on all 222 determined
    replicates). Zero exceptions on each of the three: p-hat equals
    G/(2B) to float equality on every one of the 116 vertex
    replicates and its side of 1/2 is (G > B); p-hat is exactly 0.0 on
    all 9 end0 and exactly 1.0 on all 13 end1 replicates; and the
    branch-restricted level set predicts the side on all 84
    single-in-box-root replicates -- and NOT VACUOUSLY: the branch
    split prints 19 decreasing against 65 increasing, so both of case
    (4)'s OPPOSITE inequalities fired and a hard-coded direction could
    not have survived either. That split is printed because the
    outside law shed two direction bugs, both invisible in a rate
    column and both in exactly this place. The outside law is not lost
    inside
    the box -- it is REPLACED by a case split the estimator's own
    candidate list dictates, and each case's law is as exact as the
    one it replaces.

F3  AND ON 61% OF THE SET-ASIDE THE AUDITED SAMPLE IS OUT OF THE ANSWER
    ONCE THE CASE IS KNOWN (PR4 pass, 138 of 226 = 0.611). Cases (1),
    (2) and (3) return a point -- the vertex or a box endpoint -- fixed
    by the two CLASS samples alone, so A-hat enters only through WHICH
    case fires and never through the side of 1/2 inside one. The
    conditional is the whole content and is not a weakening: A-hat still
    decides the case, but within a case it is absent, which is what the
    outside law never does. The split is clean: the A-hat-free set is
    exactly cases (1)+(2)+(3) = 116+9+13, and the separated reading
    fired ZERO times -- printed in the branch split, not inferred from a
    subtraction -- so every one of the 84 single-root replicates reads
    A-hat through its branch. That is the sharpest thing here. Where the
    vertex is outside the box the estimate is a monotone function of
    A-hat alone; where it is inside, the majority of replicates hand the
    decision to the two class samples instead. The instrument does not
    degrade gracefully across that boundary -- it changes which sample
    it listens to.

F4  THE TWO-ROOT COIN IS REAL AND RARE HERE (PR5, weighed). Two in-box
    roots occurred on 4 of 2400 replicates, all at the pi = 1/5 cell
    at n = 50; both candidates zeroed the objective to within 1e-12 in
    every case, and the upper root took the argmin on 2 of the 4. The
    share is inside the stated band but 4 replicates carry no
    resolution, and the number that means anything is the transplant:
    at the DESIGNED cell where the population vertex sits in the box,
    the same case runs 6-24% of replicates with the upper root at
    0.42-0.51 (explore_flip_floor.py). So the coin is a property of
    the estimator, priced where it is common and merely confirmed
    present where it is not.

F5  AND THE SET-ASIDE IS NOT A DIFFERENT POPULATION OF FLIPPERS (PR6,
    weighed). What the sibling excluded was the LAW'S SCORING and
    never the rate -- its flip column always ran over all 400
    replicates -- so the question here is not whether a number was
    biased but whether these replicates behave differently, and they
    do not measurably: at the only two rows with resolution the
    set-aside's flip rate sits within 0.03 of the scored population's
    and on the LOW side, 0.443 against 0.448 at pi = 1/5 and 0.333
    against 0.363 at pi = 4/5, on 70 and 111 replicates. The four
    remaining rows hold 15, 29, 0 and 1 replicates and are printed for
    completeness only. What the exclusion cost was the LAW, and F2
    pays that back.

READING. The unmeasured region was one word covering five regimes, and
the reason it read as unmeasured is that the sibling scored a single
directed inequality whose direction has no derived value inside the box
-- correctly refusing to report its own coding. Split by the
estimator's own candidate list the region is fully determined except on
a measure-4 coin, and the finding is not that the law survives but WHAT
replaces it: on 61% of these replicates, once the case is known, the
side of 1/2 is a function of the two class samples and the audited
sample is absent from it -- a different instrument answering a
different question under one name.
Tier: F2 is a rule, derived and verified with zero exceptions at this
scope (two cells, three audit sizes, 400 replicates each); F3 and F5
are observations at that scope; F4's rate is imported.

Run record: run 1 exit 0 with PC1 flagging three rows, the bar written
as an absolute 0.0005 against a record printed to three decimals -- a
bar bug and not a miss, the counts having matched to the replicate; run
2 exit 0, all controls green, 3.3 s; run 3 identical numbers with the
branch split added to PR3, which a review pass named as the way that
prediction could have passed vacuously.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np

import explore_flip_level as lvl

CELLS = ((12, 3), (2, 8))
# The sibling's recorded set-aside counts and flip rates, for PC1.
# Source: explore_flip_level.py PRINTED OUTPUT.
REC_ASIDE = {(12, 3): (70, 15, 0), (2, 8): (111, 29, 1)}
REC_FLIP = {(12, 3): (0.448, 0.245, 0.075), (2, 8): (0.355, 0.168, 0.003)}


def classify(p, tag, a_h, g_h, b_h):
    """The sub-case of a set-aside replicate, its derived side of 1/2,
    and whether that side reads A-hat at all.

    Returns (case, derived_above_half, a_free, branch). `branch` names
    which of case (4)'s two OPPOSITE inequalities was used, or the
    separated reading, so a vacuous pass -- one branch never firing --
    is visible rather than hidden inside a single exception count; the
    two direction bugs this law's outside sibling shed both lived
    exactly there. `derived_above_half` is None where the mathematics
    does not choose (sub-case 5)."""
    v = g_h / (2.0 * b_h)
    half_val = g_h / 2.0 - b_h / 4.0          # A(1/2)
    disc = g_h * g_h - 4.0 * b_h * a_h
    roots = []
    if disc >= 0.0:
        r = disc ** 0.5
        for q in ((g_h - r) / (2.0 * b_h), (g_h + r) / (2.0 * b_h)):
            if 0.0 <= q <= 1.0:
                roots.append(q)

    if len(roots) == 2:
        return 5, None, False, "two"
    if tag == "vert":
        return 1, v > 0.5, True, "vert"
    if tag == "end0":
        return 2, False, True, "end0"
    if tag == "end1":
        return 3, True, True, "end1"
    # Exactly one root in the box: the branch-restricted level set,
    # unless the vertex separates the root from 1/2.
    r = roots[0] if roots else p
    if r >= v and 0.5 < v:
        return 4, True, True, "sep"           # r >= v > 1/2
    if r <= v and 0.5 > v:
        return 4, False, True, "sep"          # r <= v < 1/2
    if r >= v:
        return 4, a_h < half_val, False, "dec"
    return 4, a_h > half_val, False, "inc"


def main():
    print("THE SET-ASIDE OF THE LEVEL-SET LAW -- what decides the side"
          " of 1/2 where the vertex is in the box")
    print("PC1 is the gate: the set-aside counts and flip rates must"
          " reproduce the sibling's exactly.\n")

    ok = True
    totals = {"aside": 0, "afree": 0, "case": {1: 0, 2: 0, 3: 0, 4: 0,
                                               5: 0}}
    exc = {"pr1": 0, "pr2": 0, "pr3": 0, "pr5": 0}
    two_root_upper = [0, 0]
    branches = {}

    for a, b in CELLS:
        pi_f = float(lvl.cell_population(a, b)[0])
        print(f"== cell ({a},{b})   pi = {pi_f:.4f}")
        print(f"{'n':>6} {'flip':>6} {'rec':>6} {'aside':>6} {'rec':>5}"
              f"   {'cases 1/2/3/4/5':>18} {'A-free':>7}"
              f"  {'flip|aside':>10} {'flip|scored':>11}")
        for idx, n in enumerate(lvl.AUDIT_SIZES):
            ests = np.empty(lvl.R_REPLICATES)
            aside = np.zeros(lvl.R_REPLICATES, dtype=bool)
            cases = np.zeros(lvl.R_REPLICATES, dtype=int)
            afree = np.zeros(lvl.R_REPLICATES, dtype=bool)
            agree = np.zeros(lvl.R_REPLICATES, dtype=bool)
            for r in range(lvl.R_REPLICATES):
                fm, fn, fu = lvl.world_features(a, b, n, lvl.RNG)
                p, tag, _has, a_h, g_h, b_h = lvl.smi_labelled(fm, fn, fu)
                ests[r] = p
                if b_h > 0.0:
                    v = g_h / (2.0 * b_h)
                    inside = 0.0 <= v <= 1.0
                elif g_h == 0.0:
                    inside = True             # the sibling's `degen`
                else:
                    inside = False
                if not inside or b_h <= 0.0:
                    aside[r] = inside
                    continue
                aside[r] = True
                case, derived, a_f, branch = classify(p, tag, a_h,
                                                      g_h, b_h)
                branches[branch] = branches.get(branch, 0) + 1
                cases[r] = case
                afree[r] = a_f
                if case == 5:
                    exc["pr5"] += 0
                    two_root_upper[1] += 1
                    if tag == "root+":
                        two_root_upper[0] += 1
                    # both candidates must zero the objective
                    disc = g_h * g_h - 4.0 * b_h * a_h
                    rr = disc ** 0.5
                    for q in ((g_h - rr) / (2.0 * b_h),
                              (g_h + rr) / (2.0 * b_h)):
                        f = (a_h - q * g_h + q * q * b_h) ** 2
                        if not abs(f) < 1e-12:
                            exc["pr5"] += 1
                    agree[r] = True
                    continue
                agree[r] = (p > 0.5) == derived
                if not agree[r]:
                    exc["pr1" if case == 1 else
                        "pr2" if case in (2, 3) else "pr3"] += 1
                if case == 1 and p != g_h / (2.0 * b_h):
                    exc["pr1"] += 1
                if case == 2 and p != 0.0:
                    exc["pr2"] += 1
                if case == 3 and p != 1.0:
                    exc["pr2"] += 1

            flip = np.abs(ests - (1.0 - pi_f)) < np.abs(ests - pi_f)
            n_as = int(aside.sum())
            cc = [int((cases == k).sum()) for k in (1, 2, 3, 4, 5)]
            totals["aside"] += n_as
            totals["afree"] += int(afree.sum())
            for k in (1, 2, 3, 4, 5):
                totals["case"][k] += int((cases == k).sum())
            f_as = float(np.mean(flip[aside])) if n_as else float("nan")
            f_sc = (float(np.mean(flip[~aside])) if (~aside).any()
                    else float("nan"))
            rec_a = REC_ASIDE[(a, b)][idx]
            # PC1's bar is the record's own precision: the sibling
            # printed three decimals, so agreement is agreement at
            # three decimals -- a tighter tolerance would compare this
            # run against a rounding and not against the record.
            hit = (n_as == rec_a
                   and "%.3f" % float(np.mean(flip))
                   == "%.3f" % REC_FLIP[(a, b)][idx])
            ok &= hit
            print(f"{n:>6} {float(np.mean(flip)):>6.3f}"
                  f" {REC_FLIP[(a, b)][idx]:>6.3f} {n_as:>6} {rec_a:>5}"
                  f"   {str(cc):>18} {int(afree.sum()):>7}"
                  f"  {f_as:>10.3f} {f_sc:>11.3f}"
                  f"{'' if hit else '   PC1 MISS'}")
        print()

    print("PC1 same replicates as the sibling:", "PASS" if ok else "FAIL")
    n_as = totals["aside"]
    covered = sum(totals["case"].values())
    print(f"PC2 partition exhaustive: {covered} of {n_as} set-aside"
          f" replicates carry a sub-case:"
          f" {'PASS' if covered == n_as else 'FAIL'}")
    print(f"    sub-case counts 1/2/3/4/5 ="
          f" {[totals['case'][k] for k in (1, 2, 3, 4, 5)]}")
    print(f"PR1 vertex tag exact and A-hat-free: {exc['pr1']} exception(s)")
    print(f"PR2 endpoint tags exact: {exc['pr2']} exception(s)")
    print(f"PR3 branch-restricted level set: {exc['pr3']} exception(s)"
          f" -- branch split {branches}, and the two OPPOSITE"
          f" inequalities must both fire or the pass is vacuous")
    share = totals["afree"] / n_as if n_as else float("nan")
    print(f"PR4 side of 1/2 is A-hat-free on {totals['afree']} of {n_as}"
          f" = {share:.3f} (bar: over half):"
          f" {'PASS' if share > 0.5 else 'FAIL'}")
    if two_root_upper[1]:
        s = two_root_upper[0] / two_root_upper[1]
        print(f"PR5 two in-box roots on {two_root_upper[1]} replicate(s),"
              f" upper root wins {s:.3f}"
              f" ({two_root_upper[0]}/{two_root_upper[1]});"
              f" objective-zero exceptions {exc['pr5']}")
    else:
        print("PR5 no two-in-box-root replicate occurred")


if __name__ == "__main__":
    main()
