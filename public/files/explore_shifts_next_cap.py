"""THE NEXT CAP: every scoped rule of the digit-shift storey's parity
law and its cycle census, re-read one step past the scope it was
verified at -- P = 9 where the period was the cap, cap 13 where the
class cap was, m = 8 and P = 21 where the period multiple was.

THE QUESTION
------------
Four rules of the trailing Ostrowski shift at the designed one-class
window [0; (1^{P-1}, a)^inf] are stated at a scanned scope, and the
cheapest audit a scoped rule can have is its next cap. Each is
re-read here, exactly, with the engine that verified it:

  R1  the parity law's verdicts -- r = 0 mod P delay 0, r mod P even
      and nonzero bounded, r mod P odd gated -- certified by the
      deficit-walk criterion at P <= 8, a <= 4
      (explore_bounded_half.py s1, s4);
  R2  the corner ratio's m-freeness -- at the (r, a, m) = (2, 2, m)
      corner the mass ratio is ONE fraction per P across every period
      multiple, F_{P+2} / (2 F_{P+1}) at odd P, at m <= 6 and P <= 20
      (explore_corner_limit.py s3);
  R3  the odd-residue cycle chart -- the cycle set contains the scaled
      comb orbits at every cell and equals them at most, the class
      tooth's admitting heights the multiples of one h0 dividing
      |det(I - H)|, at P <= 8, a <= 4 (explore_odd_cycles.py s0, s1,
      s3);
  R4  the member monoid -- every member a legal digit-wise sum of its
      cell's indecomposables, each of three shapes (comb, class tooth,
      tooth-plus-units), at most five per cell, at P <= 8 to cap 8
      (explore_member_monoid.py s1), with the rung ladder of deeper
      cuts on the r = 3 column to cap 12 and the r = 1, 5 columns flat
      to cap 12 (explore_monoid_ladder.py, explore_monoid_columns.py).

The one-cap steps: R1 and R3 at P = 9 (a = 2, 3, 4, every stride);
R2 at m <= 8 and P <= 21; R4 at P = 9 for every odd stride from cap 2
to cap 13, and at P <= 8 for the r = 1, 3, 5 columns at cap 13.

PREDICTIONS (frozen before the engine ran)
------------------------------------------
P1  R1 holds at P = 9: 27 cells, 0 off the law. This is not a guess:
    the even nonzero residues are acyclic by the odd-P mass theorems
    and the odd residues gate by the derived comb family, so P1 is a
    control of the criterion rig one period past its record.
P2  R2 holds: one fraction per P at P = 3..21 across m <= 8, the odd-P
    value the half-convergent. A TRANSPLANT from m <= 6 -- the
    derivation is open, so a second fraction at any P is the print
    that kills the rule.
P3  R3 holds: comb-orbit containment at all 12 cells of P = 9; the
    tooth law (admitting heights = multiples of h0, h0 | index) at
    all 12. Equality of the cycle set with the scaled comb orbits is
    printed per cell and not predicted (it fails at 6 of 48 cells on
    record).
P4  R4's shapes hold at P = 9 to cap 13: no fourth shape, at most five
    indecomposables per cell, closure equal to the member set at
    every cell (the closure equality is a control: soundness plus
    finite descent make it a tautology).
P5  THE LADDER'S LOCUS, two readings frozen as observables and not as
    a prediction, because the backlog's big-if-true reading turns on
    them: at P = 9 the print names WHICH odd-stride columns gain a
    non-comb generator past cap 8, HOW MANY join per band (two in one
    band is the kill-shape), and whether any is a fourth shape. If
    the ladder is the (8, ., 3) column's alone, every P = 9 column is
    flat past cap 8; if it is a fact of the class slot's position, the
    P = 9 column at r = 3 carries the same rungs -- -theta_{r+2},
    -theta_{r+3}, -theta_{r+4} -- at heights 4, 6, 10 (a TRANSPLANT
    from P = 8), and the printed heights say which.
P6  At P <= 8 and cap 13 the r = 3 column gains no rung (the recorded
    rungs sit at class-slot heights 4, 6, 10 with the last two needing
    cap height + 1; a fourth at height 16 would need cap 17) and the
    r = 1 and r = 5 columns stay flat. A TRANSPLANT from the recorded
    heights.

KILLS, as prints: R1 dies on any cell printed OFF THE LAW; R2 on any
P printed M-DEP; R3 on a containment miss or a tooth-law FAIL; R4's
shape claim on any FOURTH-SHAPE line or a cell with six or more
generators. The positive control is s0: the recorded verdicts at the
recorded scope reproduced through these imports -- the P = 8, a = 4
row of the parity law, the (8, 11, 3) rung and the (7, 9, 3) non-cut
generator, the flat (8, 12, 1) cell, the P = 5 corner fraction 13/16.

RESOURCES. One process; the engines are exact integer arithmetic; the
largest enumeration is 2^8 * 14 legal cyclic vectors at (9, 13, r).
Wall-clock estimate: 2-4 minutes, most of it the deficit-walk graphs
at P = 9. Memory trivial, run under memwatch at the 512 MB default.

FINDINGS (entered post-run; every number below sits in this file's
printed output)
--------------------------------------------------------------------
F0 THE CONTROLS HOLD: the P = 8, a = 4 row of the parity law at 0 off,
   the (8, 11, 3) rung read as TOOTH+UNITS at cut (1, 7), the single
   non-cut generator 0090010 at (7, 9, 3), the (8, 12, 1) generator
   set equal to (8, 8, 1)'s, the P = 5 corner fraction 13/16 at
   m = 2, 4, 6.
F1 R1 HOLDS AT P = 9 (P1): 27 cells, 0 off the law; every even residue
   on the classification -- r = 0 the 18-state cap comb, r = 2, 4, 6,
   8 acyclic. Box sizes 847 to 2939.
F2 R2 HOLDS AT m <= 8, P <= 21 (P2): one fraction per P at every
   P = 3..21, equal to the m = 2 closed form, the odd-P value the
   half-convergent (P = 21: 28657/35422 = F_23 / (2 F_22)).
F3 R3 HOLDS AT P = 9 (P3): comb-orbit containment at 12 of 12, the
   tooth law at 12 of 12 -- h0 divides the index, and the admitting
   heights scanned to 2 h0 are exactly h0 and 2 h0 (the first run
   scanned to 40 against h0 up to 178, a check green by vacuity at
   8 cells; the audit widened it); no h0 at or below a = 4, so no
   tooth cycle at any cell. The cycle set equals the scaled comb orbits at 10 of 12; the
   two excess cells are (9, 4, 3) and (9, 4, 5), each 15 cycle states
   against the comb's 9, one SCC, branching -- the cap-4 tooth-plus-
   unit word's orbit, as at P <= 8.
F4 R4's SHAPES HOLD AT P = 9 TO CAP 13 (P4): closure equal to the
   member set at 48 of 48 cells, no fourth shape, at most five
   indecomposables in a cell, no non-cut value at a >= 9, no band with
   two new generators.
F5 THE LADDER'S LOCUS (P5, the observable read): the r = 3 column at
   P = 9 carries the P = 8 column's CUTS AT ITS HEIGHTS -- -theta_{r+2}
   at class-slot height 4 (cap 4), -theta_{r+3} at height 6 with a
   unit at the slot's predecessor (cap 7), 2(-theta_{r+2}) at height 8
   (cap 8), -theta_{r+4} at height 10 (cap 11) -- the same cut offsets
   and the same heights, the unit digits beside the tooth differing
   (two at P = 8 against three at P = 9 on the height-8 and height-10
   words), so the ladder is the stride's and not P = 8's. And it is NOT one column's: the r = 5
   column at P = 9 carries -theta_{r+2} at height 4 (cap 4),
   -theta_{r+3} at height 6 (cap 7) and 2(-theta_{r+3}) at height 13
   (cap 13), where at P = 8 the same column stopped at its cap-4 word.
   The r = 1 and r = 7 columns are the comb alone at every cap to 13.
   Columns gaining a non-comb generator past cap 8: r = 3 (cap 11) and
   r = 5 (cap 13) -- two of the four, which is the backlog reading's
   named kill-shape (a second rung-carrying column).
F6 CAP 13 AT P <= 8 (P6, the transplant half wrong): the r = 3 column
   gains nothing at P = 4, 5, 6, 8 and ONE generator at P = 7 --
   0.0.13.0.0.0.1, tooth height 13 plus a unit, value 2(-theta_6) --
   a multiple-shaped rung the recorded heights did not predict; the
   r = 1 and r = 5 columns stay flat at cap 13.

VERDICT. R1, R2, R3 and R4's shapes each hold one cap past their
record and keep their tier (rule at the widened scope; R1's even
residues and the corner ratio's m = 2 form already theorems). The
ladder is a fact of the stride: the r = 3 column's rungs are P-stable
at P = 8, 9, with cut offsets r + 2, r + 3, 2(r + 2), r + 4 at heights
4, 6, 8, 10 (rule at that scope). The big-if-true reading -- one
automaton at every precision, the generator set cap-independent off a
thin set of columns -- is KILLED at P = 9 by its own kill-shape: two
of four odd columns gain a generator past cap 8.

RUN RECORD: python memwatch.py explore_shifts_next_cap.py -- ALL
STAGES GREEN, wall 96.9 s, peak working set 17.5 MB under the 512 MB
ceiling, exit 0; s3 re-run alone after the audit widened its height
scan, PASS at 12 of 12 with the heights printed.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell                       # noqa: E402
from explore_deep_pairs import aligned_caps, gvec                # noqa: E402
from explore_congruence_kill import n_m                          # noqa: E402
from explore_bounded_half import Rig, law, comb_orbit            # noqa: E402
from explore_corner_limit import fib, corner_closed              # noqa: E402
from explore_odd_cycles import (                                 # noqa: E402
    cell_data, derived_comb, legal_digit_cyclic)
from explore_odd_doubling import direct_member                   # noqa: E402
from explore_member_monoid import el, h0_of                      # noqa: E402
from explore_monoid_ladder import row, word                      # noqa: E402
from explore_monoid_columns import shape, cv_tag                 # noqa: E402


def gens_of(P, A, r):
    """The cell's indecomposables as (word, shape, value, cut)."""
    ms, gens, closed, h0, idx = row(P, A, r)
    out = [(g, shape(g, P, A, r, cls), v, cv) for g, cls, v, cv in gens]
    return ms, out, closed, h0, idx


def print_cell(P, A, r, ms, out, closed, h0, idx):
    tags = [f"{word(g)}={sh} v={el(*v)}{cv_tag(cv)}" for g, sh, v, cv in out]
    print(f"  P={P} A={A} r={r}: members={len(ms)} gens={len(out)} "
          f"h0={h0} idx={idx}{'' if closed else ' CLOSURE != MEMBERS'} | "
          + "; ".join(tags))


def s0():
    print("=" * 74)
    print("S0 CONTROLS: the recorded scope through this rig's imports")
    bad = 0
    off = 0
    for r in range(8):
        n, cyc, endp, inter = Rig(8, 4, r).verdict()
        v = "G" if inter else "B"
        if v != law(8, r):
            off += 1
    print(f"  parity law at (8, 4, r = 0..7): {off} off the law "
          f"{'ok' if off == 0 else '<-- CONTROL DEAD'}")
    bad += off
    ms, out, closed, h0, idx = gens_of(8, 11, 3)
    rung = [(sh, cv) for g, sh, v, cv in out
            if word(g) == "0.1.10.0.0.0.0.1"]
    ok = rung == [("TOOTH+UNITS", (1, 7))]
    print(f"  (8,11,3) rung 0.1.10.0.0.0.0.1: {rung} "
          f"{'ok' if ok else '<-- CONTROL DEAD'}")
    bad += 0 if ok else 1
    ms, out, closed, h0, idx = gens_of(7, 9, 3)
    noncut = [word(g) for g, sh, v, cv in out if cv is None]
    ok = len(noncut) == 1
    print(f"  (7,9,3) non-cut generators: {noncut} "
          f"{'ok' if ok else '<-- CONTROL DEAD'}")
    bad += 0 if ok else 1
    g8 = {g for g, sh, v, cv in gens_of(8, 8, 1)[1]}
    g12 = {g for g, sh, v, cv in gens_of(8, 12, 1)[1]}
    ok = g8 == g12
    print(f"  (8,12,1) generator set == (8,8,1)'s: {ok} "
          f"{'ok' if ok else '<-- CONTROL DEAD'}")
    bad += 0 if ok else 1
    cell = Cell(5, 2, top=8 * 5 + 4)
    ratios = set()
    for m in (2, 4, 6):
        caps = aligned_caps(5, 2, 2, m)
        g = gvec(cell, m)
        mm = sum(caps[j] * g[j] for j in range(1, m * 5, 2))
        ratios.add(Fraction(mm, n_m(cell, m)))
    ok = ratios == {Fraction(13, 16)}
    print(f"  corner ratio P = 5, m = 2, 4, 6: {sorted(ratios)} "
          f"{'ok' if ok else '<-- CONTROL DEAD'}")
    bad += 0 if ok else 1
    print(f"  {'PASS' if bad == 0 else 'FAIL'}")
    return bad == 0


def s1():
    print("=" * 74)
    print("S1 R1 AT P = 9: the criterion's verdict against the parity"
          " law, A = 2, 3, 4, r = 0..8; even residues classified")
    off = 0
    cls_bad = 0
    for A in (2, 3, 4):
        for r in range(9):
            rig = Rig(9, A, r)
            n, cyc, endp, inter = rig.verdict()
            v = "G" if inter else "B"
            want = law(9, r)
            mark = "" if v == want else "   <-- OFF THE LAW"
            off += 0 if v == want else 1
            note = ""
            if r % 2 == 0:
                if r == 0:
                    expect = comb_orbit(
                        rig, [rig.caps[k % 9] if k % 2 == 0 else 0
                              for k in range(18)])
                else:
                    expect = set()
                ok = set(cyc) == expect and not inter
                cls_bad += 0 if ok else 1
                note = (f" | cyc={len(cyc)} expect={len(expect)}"
                        f"{'' if ok else ' <-- OFF THE CLASSIFICATION'}")
            print(f"  P=9 A={A} r={r}: box={n} cyc={len(cyc)} "
                  f"interior={len(inter)} -> {v} (law {want}){mark}{note}")
    print(f"  27 cells: {off} off the law; even residues: {cls_bad} off"
          f" the classification")
    print(f"  {'PASS' if off == 0 and cls_bad == 0 else 'FAIL'}")
    return off == 0 and cls_bad == 0


def s2():
    print("=" * 74)
    print("S2 R2 AT m <= 8, P <= 21: one corner fraction per P")
    bad = 0
    for P in range(3, 22):
        cell = Cell(P, 2, top=10 * P + 4)
        ratios = set()
        ms = (2, 4, 6, 8) if P % 2 else (1, 2, 3, 4, 5, 6, 7, 8)
        for m in ms:
            caps = aligned_caps(P, 2, 2, m)
            g = gvec(cell, m)
            mm = sum(caps[j] * g[j] for j in range(1, m * P, 2))
            ratios.add(Fraction(mm, n_m(cell, m)))
        mcl, ncl = corner_closed(P)
        closed = Fraction(mcl, ncl)
        half = Fraction(fib(P + 2), 2 * fib(P + 1)) if P % 2 else None
        ok = ratios == {closed} and (half is None or half == closed)
        bad += 0 if ok else 1
        if P in (3, 4, 20, 21) or not ok:
            print(f"  P={P}: ratios={sorted(ratios)} closed={closed}"
                  f"{'' if ok else '   <-- M-DEP'}")
    print(f"  P = 3..21, m to 8: {'all pass' if bad == 0 else f'{bad} FAIL'}")
    return bad == 0


def s3():
    print("=" * 74)
    print("S3 R3 AT P = 9: comb-orbit containment, the chart, the tooth"
          " law at A = 2, 3, 4, r = 1, 3, 5, 7")
    bad = 0
    eqs = 0
    cells = [(9, A, r) for A in (2, 3, 4) for r in (1, 3, 5, 7)]
    for (P, A, r) in cells:
        rig, n, cyc, endp, inter, sccs, branch = cell_data(P, A, r)
        comb = derived_comb(P, A)
        orb = comb_orbit(rig, comb)
        contained = orb <= cyc
        bad += 0 if contained else 1
        union = set()
        k = 1
        while True:
            kd = [k * x for x in comb]
            if not legal_digit_cyclic(kd, rig.caps):
                break
            if direct_member(rig.cell, r, kd, 1):
                union |= comb_orbit(rig, kd)
            k += 1
        eq = union == cyc
        eqs += 1 if eq else 0
        cell = rig.cell
        h0, idx = h0_of(cell, r)

        def is_mem(h):
            d = [0] * P
            d[P - 1] = h
            return direct_member(cell, r, d, 1)

        top = 2 * h0 + 1
        hits = [h for h in range(1, top) if is_mem(h)]
        tooth_ok = hits == [h0, 2 * h0]
        bad += 0 if tooth_ok else 1
        print(f"  P={P} A={A} r={r}: box={n} cyc={len(cyc)} "
              f"int={len(inter)} sccs={[len(s) for s in sccs]} "
              f"branch={branch} comb-orbit "
              f"{'contained' if contained else 'NOT CONTAINED'}; "
              f"combs(k<={k - 1}): {'EQ' if eq else f'excess={len(cyc - union)}'}"
              f"; h0={h0} idx={idx} heights<={2 * h0}: {hits} tooth-cycle="
              f"{'YES' if h0 <= A else 'no'}"
              f"{'' if tooth_ok else ' <-- TOOTH LAW FAIL'}")
    print(f"  12 cells: containment misses + tooth failures = {bad};"
          f" cycle set == scaled comb orbits at {eqs} of 12")
    print(f"  {'PASS' if bad == 0 else 'FAIL'}")
    return bad == 0


def s4():
    print("=" * 74)
    print("S4 R4 AT P = 9: the monoid from cap 2 to cap 13 on every odd"
          " stride -- shapes, counts, the ladder's locus")
    closure_bad = fourth = 0
    max_gens = 0
    rung_columns = {}
    two_in_band = 0
    noncut9 = 0
    for r in (1, 3, 5, 7):
        print("-" * 74)
        prev = None
        for A in range(2, 14):
            ms, out, closed, h0, idx = gens_of(9, A, r)
            print_cell(9, A, r, ms, out, closed, h0, idx)
            closure_bad += 0 if closed else 1
            max_gens = max(max_gens, len(out))
            gens = {g for g, sh, v, cv in out}
            for g, sh, v, cv in out:
                if sh == "FOURTH":
                    fourth += 1
                    print(f"    FOURTH-SHAPE at (9,{A},{r}): {word(g)}")
                if cv is None and A >= 9:
                    noncut9 += 1
            if prev is not None:
                new = [(g, sh, cv) for g, sh, v, cv in out
                       if g not in prev and sh != "COMB"]
                if new:
                    print(f"    new at (9,{A},{r}): "
                          + ", ".join(f"{word(g)} {sh}{cv_tag(cv)}"
                                      for g, sh, cv in new))
                    if A >= 9:
                        rung_columns.setdefault(r, []).append(
                            (A, [word(g) for g, sh, cv in new]))
                if len(new) >= 2:
                    two_in_band += 1
                    print(f"    TWO-IN-A-BAND at (9,{A},{r})")
            prev = gens
    print("-" * 74)
    print(f"  closure control: {closure_bad} cells off"
          f" {'ok' if closure_bad == 0 else '<-- CONTROL DEAD'}")
    print(f"  most indecomposables in one cell: {max_gens}")
    print(f"  FOURTH-SHAPE generators: {fourth}")
    print(f"  non-cut generator values at A >= 9: {noncut9}")
    print(f"  TWO-IN-A-BAND cells: {two_in_band}")
    print(f"  columns gaining a non-comb generator past cap 8: "
          f"{sorted(rung_columns)} -> {rung_columns}")
    ok = closure_bad == 0 and fourth == 0 and max_gens <= 5
    print(f"  {'PASS' if ok else 'FAIL'}: shapes and counts at P = 9")
    return ok


def s5():
    print("=" * 74)
    print("S5 R4 AT CAP 13, P <= 8: the r = 3 column and the r = 1, 5"
          " columns, new generators against cap 12")
    new_total = 0
    for r, PS in ((3, range(4, 9)), (1, range(4, 9)), (5, range(6, 9))):
        for P in PS:
            g12 = {g for g, sh, v, cv in gens_of(P, 12, r)[1]}
            ms, out, closed, h0, idx = gens_of(P, 13, r)
            new = [(g, sh, cv) for g, sh, v, cv in out
                   if g not in g12 and sh != "COMB"]
            new_total += len(new)
            print(f"  ({P},13,{r}): gens={len(out)} "
                  f"{'' if closed else 'CLOSURE != MEMBERS '}new vs cap 12: "
                  + (", ".join(f"{word(g)} {sh}{cv_tag(cv)}"
                               for g, sh, cv in new) or "none"))
    print(f"  new generators at cap 13 over the three columns: {new_total}")
    return True


def main():
    ok = s0()
    ok = s1() and ok
    ok = s2() and ok
    ok = s3() and ok
    ok = s4() and ok
    s5()
    print("=" * 74)
    print("ALL STAGES GREEN" if ok else "RED - read the failures above")


if __name__ == "__main__":
    main()
