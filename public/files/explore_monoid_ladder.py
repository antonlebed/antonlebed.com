"""The generator ladder past cap 8: does a -theta_{r+4} family join
the member monoid on the r = 3 column at caps 9..12?

THE QUESTION
------------
The member-monoid chart (explore_member_monoid.py, P = 2..8, caps
A = 2..8, odd r) reads every indecomposable member as the comb, a
pure class-slot tooth, or a tooth-plus-unit word, and every value as
a landed cut t(-theta_j). The deeper-cut families arrive with the
cap: at A = 4 a family landing -theta_{r+2}, at A = 7 one landing
-theta_{r+3} (0160000 at (7, 7, 3), 01600100 at (8, 7, 3)), and at
(8, 8, 3) a fourth generator 00801001 landing 2(-theta_5) -- a
multiple of an earlier cut, not a new rung. This rig sweeps the
r = 3 column (P = 4..8) at caps 9..12 and asks whether the ladder
continues as ONE family per cap band (a -theta_{r+4} rung with
t = 1), stops (no generator beyond cap 8's), or continues only as
multiples (t >= 2) of the rungs already landed. The answer shapes
the theorem the census wants: a finite generator list per cap, or
one new family per band.

THE HAND-ATTACK (on paper, before the engine)
----------------------------------------------------------------------
H1  THE RINGS DIFFER PER CAP. Cell(P, A) designs the continued
    fraction from (P, A), so theta_j and the class lattice move with
    A: a cell at cap 9 is a different ring from the same (P, r) at
    cap 8, and nothing forces the generator set to be monotone in A.
    No monotonicity is predicted; every cap is read on its own.
H2  ENUMERATION COST. Aligned caps are 1 at every slot but the class
    slot (A there), so a cell enumerates at most 2^(P-1) (A + 1)
    vectors: under 2,000 at (8, 12, 3). Membership is a 2x2 integer
    solve. Wall-clock seconds; memory trivial.
H3  THE TOOTH HALF IS ALREADY A THEOREM. A pure class-slot tooth of
    height h is a member iff h0 | h (the tooth criterion), so a
    pure-tooth generator at a new cap is the height-h0 tooth exactly
    when h0 <= A, and never a new rung. A new rung must be a
    tooth-plus-unit word: the class slot at height h plus unit
    digits elsewhere. The indecomposability scan over sub-vectors
    (the monoid rig's pair scan) decides rungs against sums.
H4  TRANSPLANTS, flagged. "Cap 4 -> j = r+2, cap 7 -> j = r+3, so cap
    ~10 -> j = r+4" is a two-point extrapolation imported from the
    charted caps. The (8, 8, 3) row already broke the t = 1 half of
    the earlier reading, so the extrapolation is held at low
    confidence and stated only as an observable.

PREDICTIONS (frozen before the run; observables)
  N1 (control; red voids the run): at A = 8, r = 3, P = 4..8 the
      rig reproduces the monoid chart: closure control 0 cells off,
      generator counts (4,8,3) 1, (5,8,3) 1, (6,8,3) 2, (7,8,3) 3,
      (8,8,3) 4, and the (8,8,3) row carries 00801001 = 2(-th_5).
  N2 (the chart): per cell (P = 4..8, A = 9..12, r = 3) the member
      count, the generator count, and each generator's word, class
      (COMB / TOOTH(h) / OTHER) and value with its (t, j) print.
  N3 (the ladder): every generator value is a landed cut (a
      NOT-A-CUT row kills the landed-cut half of the values law).
      Among OTHER rows new at A >= 9 (a word not a generator at the
      same (P, r) at A = 8), the rig prints the multiset of (t, j).
      Three shapes, one of which the print decides: RUNG -- a row
      with t = 1 and j = r+4 = 7 at some cell; STOP -- no new
      generator at any cap; MULTIPLES -- new generators all with
      t >= 2. Frozen expectation (H4, low confidence): a RUNG row at
      P = 8 within caps 9..12, with MULTIPLES rows beside it.

FINDINGS (one run, 34 lines; the record at the end)
----------------------------------------------------------------------
F1  CONTROL PASSES (N1): closure 0 cells off over all 25 cells; at
    A = 8 the generator counts print 1, 1, 2, 3, 4 for P = 4..8 and
    (8, 8, 3) carries 00801001 = 2(-th_5) -- the chart reproduced.
F2  THE LADDER CONTINUES AS A RUNG (N3, the frozen expectation
    landed): at (8, 11, 3) and (8, 12, 3) a fifth generator
    0.1.10.0.0.0.0.1 -- the class slot at height 10 with a unit
    digit at its predecessor and one at the last slot -- lands
    v = 13-21a = -theta_7 = -theta_{r+4} with t = 1. Its predecessor
    unit caps the class slot at A-1, which is why height 10 first
    fits at A = 11. On the P = 8 column the rungs now read: height 4
    at cap 4 (-theta_5), height 6 at cap 7 (-theta_6), height 10 at
    cap 11 (-theta_7); no MULTIPLE row appeared beside the rung (the
    expectation's second half missed).
F3  THE LANDED-CUT HALF OF THE VALUES LAW DIES (N3's first clause):
    at (7, 9, 3) and every cap to 12 a fourth generator 0090010 --
    height 9 at the class slot, a unit at slot 5 -- lands
    v = 11-18a, which matches no t(-theta_j) for j < 20, t < 200.
    By hand it is 2(-theta_5) + (-theta_2) and equally
    -theta_5 - theta_6 + theta_3: a generator whose value is a
    Z-combination of cuts and not a cut. The reading "every
    indecomposable value is a landed cut" was a rule at caps <= 8
    and is an observation that fails at cap 9; what survives is the
    generator SHAPE (comb, tooth, tooth-plus-unit; no OTHER shape
    appeared) and the tooth criterion.
F4  THE SMALL COLUMNS STAY SMALL (N2): P = 4, 5 carry the comb alone
    at every cap (h0 equals the full index, 26..66); P = 6 keeps its
    two generators (comb, the height-4 tooth; h0 = 4 at every cap)
    and its member count grows 4, 5, 5, 5, 6 as the truncated
    monoid predicts. At (8, 10, 3) h0 = 78 is a proper divisor of
    the index 234 (elsewhere on the column h0 is the full index) --
    the pure tooth exists there at height 78 and sits far above the
    cap, so it changes nothing at this scale.

THE DESIGN
----------
Engines imported from explore_member_monoid.py (members_at,
indecomposables, closure, lam_of, cut_value, comb_aligned) and its
imports. One stage: for P in 4..8, A in 8..12, r = 3, print the
row in the monoid chart's format; A = 8 is the control (N1), A >= 9
the chart (N2), and the new-generator summary at the end is N3's
print. One command runs all; wall-clock seconds; memory trivial.

RUN RECORD: python explore_monoid_ladder.py -- 25 cells, about 3 s
wall, memory trivial, exit 0; run twice (the second after the word
print gained dot separators for two-figure digits), every verdict
identical: closure ok, non-cut=4, new generators 6, shapes
{RUNG: 2, MULTIPLE: 0, T1-OTHER: 0, NOT-A-CUT: 4}, LADDER VERDICT:
RUNG.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell                       # noqa: E402
from explore_deep_pairs import aligned_caps                      # noqa: E402
from explore_member_monoid import (                              # noqa: E402
    members_at, indecomposables, closure, lam_of, cut_value,
    comb_aligned, h0_of, el)


def word(g):
    """Digits joined; dot-separated once any digit has two figures."""
    return ".".join(map(str, g)) if max(g) > 9 else "".join(map(str, g))


R = 3
CAPS = range(8, 13)
PS = range(4, 9)


def row(P, A, r):
    cell = Cell(P, A)
    caps = aligned_caps(P, A, r, 1)
    ms = members_at(cell, r, 1)
    gens = indecomposables(ms)
    closed = closure(gens, caps) == set(ms)
    h0, idx = h0_of(cell, r)
    comb = comb_aligned(P, A, r)
    out = []
    for g in gens:
        v = lam_of(cell, r, g)
        cv = cut_value(cell, v, 2 * P + 6)
        supp = [j for j, x in enumerate(g) if x]
        if g == comb:
            cls = "COMB"
        elif supp == [(r - 1) % P]:
            cls = f"TOOTH(h={g[supp[0]]})"
        else:
            cls = "OTHER"
        out.append((g, cls, v, cv))
    return ms, out, closed, h0, idx


def main():
    print("=" * 74)
    print(f"THE LADDER PAST CAP 8: r={R}, P={PS.start}..{PS.stop - 1},"
          f" A={CAPS.start}..{CAPS.stop - 1}")
    closure_bad = noncut = 0
    at8 = {}
    new_rows = []
    for P in PS:
        for A in CAPS:
            ms, gens, closed, h0, idx = row(P, A, R)
            if not closed:
                closure_bad += 1
            tags = []
            for g, cls, v, cv in gens:
                if cv is None:
                    noncut += 1
                tags.append(f"{word(g)}={cls} v={el(*v)}"
                            + (f"=-th_{cv[1]}" if cv and cv[0] == 1
                               else (f"={cv[0]}(-th_{cv[1]})" if cv
                                     else " NOT-A-CUT")))
                if A == 8:
                    at8.setdefault(P, set()).add(g)
                elif g not in at8.get(P, set()) and cls != "COMB":
                    new_rows.append((P, A, g, cls, cv))
            print(f"  P={P} A={A} r={R}: members={len(ms)} "
                  f"gens={len(gens)} h0={h0} idx={idx}"
                  f"{'' if closed else ' CLOSURE != MEMBERS'} | "
                  + "; ".join(tags))
    print("-" * 74)
    print(f"  closure control: {closure_bad} cells off"
          f" {'ok' if closure_bad == 0 else '<-- CONTROL DEAD'}")
    print(f"  non-cut generator values: {noncut}")
    print(f"  generators new at A >= 9 (not a generator at A = 8,"
          f" comb excluded): {len(new_rows)}")
    shapes = {"RUNG": 0, "MULTIPLE": 0, "T1-OTHER": 0, "NOT-A-CUT": 0}
    for P, A, g, cls, cv in new_rows:
        if cv is None:
            shape = "NOT-A-CUT"
        elif cv[0] == 1 and cv[1] == R + 4:
            shape = "RUNG"
        elif cv[0] >= 2:
            shape = "MULTIPLE"
        else:
            shape = "T1-OTHER"
        shapes[shape] += 1
        print(f"    ({P},{A},{R}) {word(g)} {cls}"
              f" (t,j)={cv} {shape}")
    print(f"  shapes: {shapes}")
    verdict = ("RUNG" if shapes["RUNG"] else
               "STOP" if not new_rows else
               "MULTIPLES" if shapes["MULTIPLE"] == len(new_rows) else
               "MIXED")
    print(f"  LADDER VERDICT: {verdict}")


if __name__ == "__main__":
    main()
