"""The generator ladder on the r = 1 and r = 5 columns at caps 9..12:
one new generator per cap band, of the tooth-plus-unit shape?

THE QUESTION
------------
On the r = 3 column (explore_monoid_ladder.py) the member monoid of
the odd-residue cycle chart gains its indecomposable generators one
family at a time as the class cap rises: on the P = 8 column a
class-slot tooth with unit digits beside it lands at cap 4, at cap 7
and at cap 11, each the first cap that fits its height, and no cap
in 9..12 brings two new generators at once. Every generator scanned
so far has one of three SHAPES: the comb, a pure class-slot tooth,
or a class-slot tooth plus unit digits. The reading "one new
generator per band, its shape fixed" is what a per-band presentation
of the cycle language would rest on. This rig reads the same
observables on the other two odd columns the chart holds to P = 8,
r = 1 (P = 4..8) and r = 5 (P = 6..8), at caps 8..12, and asks
whether either column breaks the reading: two new generators inside
one cap band, or a generator of a fourth shape.

THE HAND-ATTACK (on paper, before the engine)
----------------------------------------------------------------------
H1  THE CLASS SLOT MOVES WITH r. The aligned caps put the class cap
    A at slot (r - 1) mod P and cap 1 everywhere else, so the class
    slot is 0 at r = 1 and 4 at r = 5; a shape is read against that
    slot and never against slot 2, the r = 3 column's.
H2  THE RINGS DIFFER PER CAP (the ladder rig's H1): Cell(P, A)
    designs the continued fraction from (P, A), so no monotonicity
    in A is assumed. "New at cap A" means "a generator at A and not
    at A - 1", read cap by cap; a generator may appear and vanish.
H3  SHAPE IS DECIDED BY DIGITS. Comb: the cell's aligned comb word.
    Pure tooth: support exactly the class slot. Tooth-plus-unit: the
    class digit at least 1 and every other digit 0 or 1. A FOURTH
    shape is anything else: a non-class digit of 2 or more, or a
    class digit of 0 on a word that is not the comb. Under aligned
    caps a non-class digit above 1 is illegal, so the fourth shape
    can only arrive as a class-digit-0 word; the rig reads both.
H4  TRANSPLANTS, flagged. "A rung per band" and "P = 7 carries a
    non-cut value from cap 9" are the r = 3 column's facts; the r = 1
    column is the chart's exception column (its second families
    never fuse at m = 2), so nothing from r = 3 is expected of it
    with confidence. The r = 1 comb is the -theta_{r+1} cut at odd P
    and the -theta_r cut at even P (the gated derivation's cuts), so
    the "cut index" of a rung is read relative to r and printed, never
    predicted.
H5  COST. At most 2^(P-1) (A + 1) vectors per cell, under 2,000 at
    (8, 12, r); 40 cells; seconds; memory trivial.

PREDICTIONS (frozen before the run; observables)
  N1 (controls; red voids the run): (a) closure equals the member
      set at every cell (0 cells off). (b) The r = 3 rung reproduces
      through THIS rig's shape reader: at (8, 11, 3) the generator
      0.1.10.0.0.0.0.1 is read TOOTH+UNITS with value -theta_7, and
      (8, 8, 3)'s 00801001 is read TOOTH+UNITS at 2(-theta_5). (c)
      At A = 8 every generator on both columns is COMB, TOOTH or
      TOOTH+UNITS and every value a landed cut t(-theta_j) — the
      census's rule to cap 8 (explore_member_monoid.py F3, F4).
  N2 (the chart): per cell (P, A, r) the member count, generator
      count, h0, the index, and each generator's word, shape and
      value with its (t, j) or NOT-A-CUT.
  N3 (the kill observables): TWO-IN-A-BAND — a cell (P, A, r) with
      A >= 9 at which two or more generators are new (comb
      excluded); FOURTH-SHAPE — any generator read as neither COMB,
      TOOTH nor TOOTH+UNITS. The rig prints both counts and a
      VERDICT line: KILL if either count is positive, SURVIVES
      otherwise. Frozen expectation (H4, low confidence): SURVIVES;
      the P = 8 column at each r carrying at least one new t = 1
      generator within caps 9..12, and NOT-A-CUT values possible on
      the P = 7 column as at r = 3.

FINDINGS (one run, 58 lines; the record at the end)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1): closure 0 cells off over all 40 cells; every
    A = 8 generator on both columns is COMB or TOOTH+UNITS with a
    landed-cut value (0 rows off the census's rule); the r = 3 rung
    0.1.10.0.0.0.0.1 at (8, 11, 3) reads TOOTH+UNITS at (1, 7) and
    00801001 at (8, 8, 3) reads TOOTH+UNITS at (2, 5).
F2  THE COLUMNS ARE FLAT (N3; the frozen expectation's second half
    missed): no generator is new at any cap 9..12 on either column.
    Every cell's generator set is the cap-8 set unchanged — r = 1:
    {1010, 3001} at P = 4, {20010, 30101} at P = 5 (the exception
    column's second family, a height-3 class tooth plus units
    landing -theta_3), the comb alone at P = 6, 7, 8; r = 5: the
    comb alone at P = 6, 7, and {10004000, comb} at P = 8, the
    cap-4 family landing -theta_7 = -theta_{r+2}. TWO-IN-A-BAND 0,
    FOURTH-SHAPE 0, non-cut values 0; VERDICT SURVIVES. The rung
    ladder (-theta_{r+2}, -theta_{r+3}, -theta_{r+4} at caps 4, 7,
    11) is therefore the (8, ., 3) column's at P <= 8: the reading
    "one new generator per band" holds on r = 1 and r = 5 with zero
    per band, and "exactly one at every column" is false.
F3  h0 MOVES WITH THE CAP AND NEVER REACHES IT (N2): h0 equals the
    full index at 25 of the 40 cells and a proper divisor at 15
    (smallest (7, 9, 1) at 19 of 133); at every cell h0 > A, so no
    pure class tooth exists at these caps, as the tooth criterion
    says.
F4  WHAT IS LEFT OPEN: why the r = 3 column carries rungs and the
    r = 1, r = 5 columns none at P <= 8 — whether the ladder is a
    fact of the class slot's position (slot 2 against slots 0 and 4)
    or of P = 8 alone, which the P = 9, 10 columns decide.

THE DESIGN
----------
Engines imported from explore_monoid_ladder.py (row, word) and
explore_member_monoid.py (el, comb_aligned). One stage per column:
for each (P, A) print the row; then the r = 3 control at two cells;
then the kill counts and the verdict. One command; seconds.

RUN RECORD: python explore_monoid_columns.py -- 40 cells plus the two
r = 3 control cells, 0.3 s wall, peak working set 13.8 MB under
memwatch (limit 512), exit 0; run twice, 58 lines byte-identical.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_monoid_ladder import row, word                      # noqa: E402
from explore_member_monoid import el, comb_aligned                # noqa: E402

CAPS = range(8, 13)
COLUMNS = {1: range(4, 9), 5: range(6, 9)}


def shape(g, P, A, r, cls):
    if cls == "COMB":
        return "COMB"
    slot = (r - 1) % P
    others = [x for j, x in enumerate(g) if j != slot]
    if g[slot] >= 1 and all(x == 0 for x in others):
        return f"TOOTH(h={g[slot]})"
    if g[slot] >= 1 and all(x <= 1 for x in others):
        return "TOOTH+UNITS"
    return "FOURTH"


def cv_tag(cv):
    if cv is None:
        return " NOT-A-CUT"
    return f"=-th_{cv[1]}" if cv[0] == 1 else f"={cv[0]}(-th_{cv[1]})"


def cell_line(P, A, r):
    ms, gens, closed, h0, idx = row(P, A, r)
    out = []
    for g, cls, v, cv in gens:
        out.append((g, shape(g, P, A, r, cls), v, cv))
    tags = [f"{word(g)}={sh} v={el(*v)}{cv_tag(cv)}" for g, sh, v, cv in out]
    print(f"  P={P} A={A} r={r}: members={len(ms)} gens={len(gens)} "
          f"h0={h0} idx={idx}{'' if closed else ' CLOSURE != MEMBERS'} | "
          + "; ".join(tags))
    return out, closed


def main():
    print("=" * 74)
    print("THE LADDER ON THE r = 1 AND r = 5 COLUMNS, A = 8..12")
    closure_bad = two_in_band = fourth = noncut9 = 0
    at8_bad = 0
    for r, PS in COLUMNS.items():
        print("-" * 74)
        for P in PS:
            prev = None
            for A in CAPS:
                out, closed = cell_line(P, A, r)
                closure_bad += 0 if closed else 1
                gens = {g for g, sh, v, cv in out}
                for g, sh, v, cv in out:
                    if sh == "FOURTH":
                        fourth += 1
                        print(f"    FOURTH-SHAPE at ({P},{A},{r}): {word(g)}")
                    if cv is None and A >= 9:
                        noncut9 += 1
                    if A == 8 and (sh == "FOURTH" or cv is None):
                        at8_bad += 1
                if prev is not None:
                    new = [g for g, sh, v, cv in out
                           if g not in prev and sh != "COMB"]
                    if new:
                        print(f"    new at ({P},{A},{r}): "
                              + ", ".join(word(g) for g in new))
                    if len(new) >= 2:
                        two_in_band += 1
                        print(f"    TWO-IN-A-BAND at ({P},{A},{r})")
                prev = gens
    print("-" * 74)
    print("  r = 3 control through this rig's shape reader:")
    ctrl_ok = True
    for P, A, want_word, want_cv in ((8, 11, "0.1.10.0.0.0.0.1", (1, 7)),
                                     (8, 8, "00801001", (2, 5))):
        out, closed = cell_line(P, A, 3)
        hit = [(sh, cv) for g, sh, v, cv in out if word(g) == want_word]
        ok = hit == [("TOOTH+UNITS", want_cv)]
        ctrl_ok &= ok
        print(f"    ({P},{A},3) {want_word}: {hit} "
              f"{'ok' if ok else '<-- CONTROL DEAD'}")
    print("-" * 74)
    print(f"  closure control: {closure_bad} cells off"
          f" {'ok' if closure_bad == 0 else '<-- CONTROL DEAD'}")
    print(f"  A = 8 rows off the census's shapes-and-cuts rule: {at8_bad}"
          f" {'ok' if at8_bad == 0 else '<-- CONTROL DEAD'}")
    print(f"  r = 3 rung read as TOOTH+UNITS: "
          f"{'ok' if ctrl_ok else '<-- CONTROL DEAD'}")
    print(f"  non-cut generator values (A >= 9): {noncut9}")
    print(f"  TWO-IN-A-BAND cells: {two_in_band}")
    print(f"  FOURTH-SHAPE generators: {fourth}")
    controls = closure_bad == 0 and at8_bad == 0 and ctrl_ok
    verdict = ("VOID (control dead)" if not controls else
               "KILL" if (two_in_band or fourth) else "SURVIVES")
    print(f"  VERDICT: {verdict}")


if __name__ == "__main__":
    main()
