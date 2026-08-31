"""explore_flatten_gen.py -- DOES THE WALK PAST RANK 26 MINT A SIXTH
MEMBER?

The one question the flattening corpus's ambient class leaves open, in
its own words: whether the class the LATTICE EXHIBITS is finitely
generated -- whether some finite set of members makes every residual it
can exhibit. Five members are minted -- A, B, C off the chart's own
census, D at rank 22 depth 30 (explore_flatten_swap.py's find, re-minted
by the walk), E at rank 22 depth 32 and rank 26 depth 36
(explore_flatten_class.py) -- and nothing in reach bounds the number.
The question is the lattice's and never the ambient class's, which is
infinitely generated at its lowest degree by the W_c family
(explore_flatten_deep.py).

THE PROBE, chosen over a derivation because the record's own facts
choose it: members show at a column's first few failing cells across
ranks (the class walk's F1/F3, the deep rig's F1), the cheap filter
hs < ph is blind exactly at minting cells so route_h is the only
scanner, and a bounding derivation has no handle -- the ambient class
being infinitely generated at degree 2, any bound must consult the
lattice, and nothing in reach prices that. So: WALK THE RANKS PAST THE
SCANNED ONES -- 27, 28, 29 -- take each column's first failing cell and
its next three failing cells, and ask whether each residual is a product
of the members in hand, the class SEEDED at the full five and GROWING as
the walk goes.

(The senses are the thread's, restated because this rig is read alone.
A vector c on M atoms is the polynomial P(x) = sum_i c_i x^i; its
FLATTENING is the multiplicity of the root 1; its HEIGHT is the sup
norm max_i |c_i|. h(M, J) is the least height of a nonzero P with
flattening at least J and degree < M. A PURE PRODUCT is prod_i
(x^{d_i} - 1) over a multiset of positive PARTS; ph(M, J) is the least
height of a pure product admissible at the cell. RANK is always
r = M - J; the index convention is re-derived from the engine, not
assumed: decide_cell(r, J) computes M = J + r and scans J = 2 upward.
A cell FAILS when h < ph. The COFACTOR of a lattice vector is
q = P/(x-1)^J, and split_witness factors it as a monomial times a sign
times a product of cyclotomics times a RESIDUAL R carrying no
cyclotomic factor. A MEMBER is a residual, or a factor of one, that no
product of the members already in hand can make. The SWAP FAMILY at a
cell is every admissible pure cofactor with a sub-multiset of its own
cyclotomic blocks traded for an equal-degree product of class members,
and hs is its least height. h <= hs <= ph always.)

THE HAND ATTACK, worked before any engine code. Most of it is
inherited derivation, re-read rather than re-proved, and the two
transplants are marked.

FIRST, WHAT MINTS, unchanged from the class walk: at a failing cell
the minimiser's residual is divided greedily by the members in hand; a
leftover of degree >= 1 is a candidate, and a member only after an
admissible parent is printed to exist AND admitting the leftover drops
hs to h at that cell. The greedy division is well defined for
{A, B, C, D}, which are proved irreducible (the deep rig's hand attack,
step five); E's irreducibility is measured, not proved, so the
permutation control stays load-bearing and runs at every examined cell.

SECOND, THE TWO TRANSPLANTS. (i) "Members live at a column's first few
failing cells" is TWO columns' fact -- D and E sit in rank 22's and
rank 26's first four failing cells, and the twelve deeper depths of
each carry nothing new. Carrying it to ranks 27..29 is a SCAN DESIGN
and never a claim: a member living deeper here would be missed, and the
scan's scope is stated with the verdict. (ii) The value 1 at -1 is a
RULE only over the chart's cells at h >= 4 (explore_flatten_endvalue.py)
and an observation at the five members and the 24 deep-column cells;
these cells sit outside the chart, so predicting it here TRANSPLANTS
the pattern past its proved scope, deliberately -- that is what makes
P2 falsifiable.

THIRD, THE COST MODEL IS KNOWN TO NOT EXIST, so the budget is a node
cap and not a wall-clock model: route_h's cost is not a function of M
and the rank and is not monotone in either, while its node rate holds
between about 19000 and 25000 a second (the class walk's F6). The cap
here is NODE_CAP = 2,000,000 -- five times the class walk's, because
the one price measured in this range, rank 27 depth 36 at 99.57 s
uncapped, sits right at 2M nodes and a cap of 400,000 would shed
exactly the cells this walk is for. A capped cell is UNDECIDED and
printed as such; a first failing depth is claimed only when every cell
below it was decided, and an undecided cell below turns the claim into
an upper bound, stated as such. Worst case per cell is the cap over
the measured rate -- 80 to 105 s -- and the rehearsal multiplies its
own wall out to the full range before the full range is run.

FOURTH, THE STATISTIC HAS NO ALGEBRA TO ATTACK -- every quantity here
is an exact integer computed by exhaustion (h, hs, ph) or an exact
polynomial division; there is no estimator, no denominator, no null.
The one count read as evidence is minted-vs-quiet over the examined
cells, and it is reported as a count over a stated population, never a
rate.

THE PREDICTIONS, fixed here before the engine ran.

P1. THE WALK MINTS A SIXTH. At least one examined failing cell of
    ranks 27..29 prints a leftover of degree >= 1 against the class in
    hand. (Prior rate: three minting cells among the 32 examined at
    ranks 19..26.)
P2. ANY MINTED MEMBER HAS VALUE 1 AT -1. The transplant marked above.
P3. ANY MINTED MEMBER HAS AN ODD VALUE AT 1. Implied by P2, printed
    separately so a failure separates the implication from the pattern.
P4. IT KEEPS THE MEMBERS' SHAPE OTHERWISE: reciprocal, no cyclotomic
    factor, every coefficient strictly positive. The circle test is
    REPORTED AND NOT PREDICTED -- E already left the circle.
P5. THE FIRST CELLS STAY QUIET AND A-VALUED: at least two of the three
    first failing cells print residual exactly A (six of eight did at
    ranks 19..26).

THE KILLS, frozen as OBSERVABLES the rig prints, never as inferences.

K1 No examined failing cell of ranks 27..29 prints a leftover of
   degree >= 1. P1 dies, and the five close every cell this walk
   reached.
K2 A minted member printing a value at -1 other than 1. P2 dies.
K3 A minted member printing an even value at 1. P3 dies.
K4 A minted member printing reciprocal FALSE, a non-empty cyclotomic
   part, or a coefficient that is not strictly positive. P4 dies. Wired
   at EVERY minted member -- the class walk's own record names its K3
   guarding only first-cell admits as a gap in its kill wiring, and
   this rig closes it.
K5 Fewer than two of the three first failing cells print residual
   exactly A, over the first cells DECIDED. P5 dies.
K6 Instrument: h > ph at any decided cell (clean cells included), or
   hs < h, or hs > ph, or hs0 != ph, or a leftover that is a constant
   other than 1, or a split that does not multiply back to its own
   cofactor, or admitting a leftover that does not drop hs to h.
K7 Answer key: rank 22 depth 30 against {A, B, C} does not print
   h = 42222, hs = ph = 44108, leftover [3, 9, 15, 17, 15, 9, 3]; or
   rank 22 depth 32 against {A, B, C, D} does not print h = 108376,
   hs = 110932, ph = 125135, leftover [3, 11, 24, 37, 43, 37, 24, 11,
   3].
K8 Instrument: the leftover differs across the permutations of the
   members in hand at any examined cell.

THE POSITIVE CONTROLS, run before any survive/kill result is read.

C1 The class printed before anything is measured: each member's
   degree, height, value at 1, value at -1, reciprocity, the exact
   Sturm circle test, and the cyclotomic part, which must be empty for
   a residual.
C2 The answer key (K7), each cell RE-MINTING its own member from a
   class that does not contain it, by the same code path every new
   cell uses -- D from {A, B, C}, E from {A, B, C, D}.
C3 The reconstruction at every examined cell: split_witness's own
   output multiplied back equals the cofactor exactly (tallied).
C4 The leftover recomputed over every permutation of the members in
   hand at every examined cell (K8, tallied).
C5 The tallies printed, so a control that RAN cannot be told apart
   from one that never did by reading the output.

COST. Single process, exact integer arithmetic, no array library, run
under memwatch against the 512 MB ceiling. The scan is bounded by
NODE_CAP per cell at the measured rate; the swap family is run only at
examined failing cells, at the per-rank prices the class walk measured
rising with the rank alone. A REHEARSAL -- the two answer-key cells
plus rank 27's column to its first failing cell only -- runs first,
and its wall is multiplied out before the full range is run.

THE FINDINGS.

F1. TWO MORE MEMBERS, AND THE COUNT IS SEVEN. Rank 27 first fails at
J = 34 (M = 61), where h = 140702 against ph = 143411 and the
minimiser's residual divided by A leaves

    F = 3 + 10x + 20x^2 + 29x^3 + 33x^4 + 29x^5 + 20x^6 + 10x^7 + 3x^8,

degree 8, height 33, F(1) = 157 prime, F(-1) = 1, reciprocal, all
roots ON the unit circle by the exact Sturm test, no cyclotomic part,
every coefficient positive; admitting it drops hs from 141410 to h.
Rank 28's third examined failing cell, J = 33 (M = 61), has residual

    G = 3 + 6x + 8x^2 + 6x^3 + 3x^4

whole -- divided by nothing, the leftover is G itself -- degree 4,
height 8, reciprocal, on the circle, cyclotomic-free, positive;
admitting it drops hs from 67578 to h = 67323. P1 holds and K1 does
not fire: the walk mints at two of its three ranks, and the class
{A, B, C, D, E, F, G} now counts seven members with nothing slowing.

F2. G BREAKS BOTH END-VALUE PATTERNS AT ONCE. G(-1) = 2 and G(1) = 26
= 2*13: K2 and K3 fired, P2 and P3 die. The value 1 at -1 was five for
five at the members and held at every deep-column residual; G is the
first member off it, so the pattern was the first six members' and
never the class's law -- the endvalue rule keeps exactly its proved
scope, the chart's cells at h >= 4, and the transplant past that scope
is what died here. With it dies the forced oddness at 1, and the
primality reading with that: the deep rig killed primality as a law
about the AMBIENT class (W_4 composite); G kills it as a fact about
the MEMBERS -- a minted member with an even, composite value at 1.

F3. F RECURS AT THREE CONSECUTIVE RANKS AND TAKES OVER THE FIRST
CELLS. Rank 27's first cell carries A*F, rank 28's first cell F alone,
rank 29's first AND second cells F alone -- four cells across all
three ranks, where E needed two sightings at two ranks to stop being
an accident. And residual exactly A stands at ZERO of the three first
cells: K5 fired, P5 dies. The A-dominance of first failing cells (six
of eight at ranks 19..26) was those ranks' fact; at 27..29 the
dominant first-cell residual is the new member itself.

F4. THE FILTER'S FIRST-CELL BLINDNESS WAS RANK 22'S FACT TOO. At both
minting cells hs sits strictly BETWEEN h and ph -- 141410 and 67578 --
so the filter FIRES at cells that mint, where the class walk's F5 had
hs = ph exactly at its one minting first cell. The blindness is
class-relative: a seven-member class in hand can improve on pure
without reaching h, so hs < ph no longer separates reached from
minting cells and the coincidence is not a law.

F5. THE FIRST FAILING DEPTH IS NOT MONOTONE IN THE RANK: 34, 31, 25
at ranks 27, 28, 29 against 26, 23, 25, 30, 22, 29, 31, 27 at 19..26,
and rank 29's first failure sits at h = 939 where rank 27's is at
140702. The one undecided cell, rank 28 J = 37, capped at 2M nodes in
106.8 s with decided cells on both sides -- the same one-cell
Fincke-Pohst story the deep rig's F4 names, not a frontier.

F6. THE SHAPE SURVIVES WHERE THE VALUES DO NOT. P4 holds at both
mints: reciprocal, cyclotomic-free, strictly positive coefficients.
And both new members are ON the circle, so E remains the only member
off it -- the circle description regained two specimens the same run
that killed the end-value pattern.

F7. F AND G ARE IRREDUCIBLE OVER Q, by the thread's descent, worked on
paper AFTER the run from the printed circle tests and cross-checked by
an independent factorisation. Both have all roots on the circle and a
nonzero value at -1, so every irreducible factor is self-reciprocal of
even degree and descends to S in y = x + 1/x. S_G = 3y^2 + 6y + 2 has
non-square discriminant 12. S_F = 3y^4 + 10y^3 + 8y^2 - y - 1 has no
rational root (1, -1, 1/3, -1/3 give 19, 1, -1/27, -1/9) and no
integer split (3y^2+ay+b)(y^2+cy+d): bd = -1 forces (b, d) = (1, -1)
or (-1, 1), whose systems force 4a = 13 or 4c = 11. So the greedy
division stays well defined with both admitted, E alone still measured
rather than proved.

THE RUN RECORD. ONE REHEARSAL and ONE FULL RUN. The rehearsal ran the
two answer-key cells and rank 27's column to its first failing cell:
184.4 s, peak working set 119.7 MB, and it already showed F's cell.
The full run: 1426.2 s wall, peak working set 272.0 MB against the 512
MB ceiling, kills fired K2 x1, K3 x1, K5 x1. The answer key reproduced
in both: h = 42222 with hs = ph = 44108 and leftover D at rank 22
depth 30 against {A, B, C}; h = 108376, hs = 110932, ph = 125135 and
leftover E at depth 32 against {A, B, C, D}; each admitted falls to h.
Controls: the bracket holds at 12 of the 12 walk cells it is checked
at, the split reconstructs at 14 of 14 examined cells, the leftover is
permutation-stable at 14 of 14.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_family import on_unit_circle
from explore_flatten_band import xm1_pow
from explore_flatten_class import (SEED, decide_cell, examine,
                                   describe_member, swap_at, TALLY)

D_POLY = [3, 9, 15, 17, 15, 9, 3]
E_POLY = [3, 11, 24, 37, 43, 37, 24, 11, 3]
FULL = list(SEED) + [("D", D_POLY), ("E", E_POLY)]

RANK_LO = 27
RANK_HI = 29
J_CAP = 44          # a column giving fewer than four failing cells by
                    # here is reported as such, never extended silently
NODE_CAP = 2000000
EXTRA_CELLS = 3

KEY30 = (42222, 44108, D_POLY)
KEY32 = (108376, 110932, 125135, E_POLY)


def factorise(n):
    """Trial division, for values at 1 of the sizes this thread sees."""
    out, m, d = [], abs(n), 2
    while d * d <= m:
        while m % d == 0:
            out.append(d)
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        out.append(m)
    return out


def at_minus_1(p):
    return sum(c * (-1) ** i for i, c in enumerate(p))


def show(nm, p):
    """One line through describe_member plus the value at -1 and the
    factorisation of the value at 1."""
    d = describe_member(p)
    f = factorise(d["at1"])
    print("   %-6s %-34s deg %d  height %-3d  P(1) %6d = %-14s  "
          "P(-1) %3d  recip %-5s  circle %-5s  cyc %s"
          % (nm, str(p), d["deg"], d["height"], d["at1"],
             "prime" if len(f) == 1 else "*".join(map(str, f)),
             at_minus_1(p), d["recip"], d["circle"],
             list(d["cyc"]) or "(none)"))
    return d


def mint_checks(nm, p, fired):
    """K2, K3, K4 at a minted member -- every minted member, first cell
    or not."""
    d = show(nm, p)
    if at_minus_1(p) != 1:
        fired["K2"] += 1
        print("      K2 the value at -1 is %d" % at_minus_1(p))
    if d["at1"] % 2 == 0:
        fired["K3"] += 1
        print("      K3 the value at 1 is even")
    if not (d["recip"] and not d["cyc"] and d["positive"]):
        fired["K4"] += 1
        print("      K4 the minted member does not keep the shape")


def key_cell(J, seed, key, fired):
    """One answer-key cell: decide, examine against the given seed, and
    compare every committed number (C2/K7). Returns ok."""
    h, v, ph, verdict = decide_cell(22, J, NODE_CAP)
    if verdict != "F":
        print("   r=22 J=%d did not decide as failing (verdict %s)"
              % (J, verdict))
        return False
    e = examine(22, J, h, v, seed, fired)
    if len(key) == 3:
        ok = (h, e["hs"], e["rest"]) == key and e["hs"] == ph
        print("   r=22 J=%d: h=%d (key %d) hs=%d (key %d) ph=%d "
              "leftover %s (key %s) %s"
              % (J, h, key[0], e["hs"], key[1], ph, e["rest"], key[2],
                 "ok" if ok else "MISMATCH"))
    else:
        ok = (h, e["hs"], ph, e["rest"]) == key
        print("   r=22 J=%d: h=%d (key %d) hs=%d (key %d) ph=%d (key %d) "
              "leftover %s (key %s) %s"
              % (J, h, key[0], e["hs"], key[1], ph, key[2], e["rest"],
                 key[3], "ok" if ok else "MISMATCH"))
    if ok:
        # the admit test, same path a new mint takes
        _, hsx = swap_at(22, J, list(seed) + [("Z", list(e["rest"]))],
                         xm1_pow(J))
        if hsx != h:
            fired["K6"] += 1
            print("      K6 admitting the key leftover does not reach h")
            ok = False
        else:
            print("      admitted, hs falls to h = %d -- re-minted from "
                  "a class that does not contain it" % h)
    return ok


def walk_rank(r, members, fired, minted_log, firstcell_log):
    """One rank: scan J = 2 upward, examine the first failing cell and
    the next EXTRA_CELLS failing cells against the class in hand,
    minting into it where a leftover of degree >= 1 admits."""
    t_r = time.time()
    und, taken, first_seen = [], 0, None
    for J in range(2, J_CAP + 1):
        if taken > EXTRA_CELLS:
            break
        t0 = time.time()
        h, v, ph, verdict = decide_cell(r, J, NODE_CAP)
        if verdict == "?":
            und.append(J)
            print("   r=%d J=%d M=%d UNDECIDED at the %d-node cap "
                  "(%.1f s)" % (r, J, J + r, NODE_CAP, time.time() - t0))
            sys.stdout.flush()
            continue
        if verdict != "F":
            if h > ph:
                fired["K6"] += 1
                print("   K6 h = %d > ph = %d at r=%d J=%d" % (h, ph, r, J))
            if first_seen is None and J >= 20:
                print("   r=%d J=%d M=%d clean (%.1f s)"
                      % (r, J, J + r, time.time() - t0))
                sys.stdout.flush()
            continue
        taken += 1
        if first_seen is None:
            first_seen = J
            below = [j for j in und if j < J]
            print("\n   rank %2d: first failure at J = %d (M = %d)%s"
                  % (r, J, J + r,
                     " -- UNDECIDED BELOW IT AT %s, so this depth is an "
                     "UPPER BOUND" % below if below else ""))
        e = examine(r, J, h, v, members, fired)
        print("   r=%d J=%d M=%d: h=%d hs=%d ph=%d, residual %s, divided "
              "by %s leaves %s (%.1f s)"
              % (r, J, J + r, h, e["hs"], ph, e["R"],
                 e["used"] or "(none)", e["rest"], time.time() - t0))
        if e["hs"] < h or e["hs"] > ph or e["hs0"] != ph:
            fired["K6"] += 1
            print("      K6 bracket at r=%d J=%d" % (r, J))
        else:
            TALLY["C2"] += 1
        if first_seen == J:
            firstcell_log.append((r, J, list(e["R"]), list(e["rest"])))
        if e["rest"] != [1]:
            if not e["parent"]:
                print("      NO admissible parent holds %s with %d to "
                      "spare -- a PARENT obstruction, and no member is "
                      "minted here" % (list(e["S"]), len(e["R"]) - 1))
            else:
                nm = chr(ord("F") + sum(1 for _ in minted_log))
                print("      A MEMBER THE CLASS CANNOT MAKE -- minted "
                      "as %s:" % nm)
                mint_checks(nm, e["rest"], fired)
                _, hsx = swap_at(r, J, members + [(nm, list(e["rest"]))],
                                 xm1_pow(J))
                print("      with %s admitted, hs = %d against h = %d "
                      "-- %s" % (nm, hsx, h,
                                 "reached" if hsx == h
                                 else "STILL NOT REACHED"))
                if hsx != h:
                    fired["K6"] += 1
                    print("      K6 admitting the leftover does not "
                          "reach h")
                minted_log.append((r, J, nm, list(e["rest"])))
                members.append((nm, list(e["rest"])))
        sys.stdout.flush()
    print("   (rank %d: %d failing cells examined, %d undecided, "
          "%.1f s)" % (r, taken, len(und), time.time() - t_r))
    sys.stdout.flush()
    return first_seen, und, taken


def main():
    rehearse = "--rehearse" in sys.argv
    t_all = time.time()
    fired = dict((k, 0) for k in
                 ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "C3"))

    print("=" * 70)
    print("explore_flatten_gen.py -- does the walk past rank 26 mint "
          "a sixth member?")
    print("=" * 70)

    print("\n[C1] the class as seeded, the FULL five, before anything "
          "is measured")
    for (nm, p) in FULL:
        show(nm, p)

    print("\n[C2] the answer key, each cell re-minting its own member "
          "from a class that does not contain it")
    ok30 = key_cell(30, list(SEED), KEY30, fired)
    ok32 = key_cell(32, list(SEED) + [("D", D_POLY)], KEY32, fired)
    if not (ok30 and ok32):
        fired["K7"] += 1
        print("   K7 the answer key is not reproduced")

    if rehearse:
        print("\nREHEARSAL -- rank 27's column to its first failing "
              "cell only")
        members = [(nm, list(p)) for (nm, p) in FULL]
        minted_log, firstcell_log = [], []
        t0 = time.time()
        # first failing cell only: EXTRA_CELLS behaviour via early exit
        for J in range(2, J_CAP + 1):
            h, v, ph, verdict = decide_cell(27, J, NODE_CAP)
            if verdict == "?":
                print("   r=27 J=%d UNDECIDED" % J)
                continue
            if verdict == "F":
                e = examine(27, J, h, v, members, fired)
                print("   r=27 first failure at J=%d M=%d: h=%d hs=%d "
                      "ph=%d residual %s leftover %s"
                      % (J, J + 27, h, e["hs"], ph, e["R"], e["rest"]))
                break
        print("   rehearsal wall %.1f s -- multiply out before the "
              "full range" % (time.time() - t0))
        print("wall %.1f s" % (time.time() - t_all))
        return

    print("\nTHE WALK -- ranks %d..%d, the first failing cell and the "
          "next %d failing cells of each column, the class growing as "
          "it goes. Node cap %d."
          % (RANK_LO, RANK_HI, EXTRA_CELLS, NODE_CAP))
    members = [(nm, list(p)) for (nm, p) in FULL]
    minted_log, firstcell_log = [], []
    firsts = {}
    for r in range(RANK_LO, RANK_HI + 1):
        firsts[r] = walk_rank(r, members, fired, minted_log,
                              firstcell_log)

    print("\nTHE VERDICT")
    for r in sorted(firsts):
        f, und, taken = firsts[r]
        print("   rank %d: first failure at J = %s, %d failing cells "
              "examined%s"
              % (r, f, taken,
                 ", undecided at %s" % und if und else ""))
    print("   minted: %s"
          % (", ".join("%s at r=%d J=%d" % (nm, r, J)
                       for (r, J, nm, _) in minted_log) or "NOTHING"))
    if not minted_log:
        fired["K1"] += 1
        print("   K1 no examined cell of ranks %d..%d mints -- the five "
              "close every cell this walk reached" % (RANK_LO, RANK_HI))
    a_first = sum(1 for (_, _, R, _) in firstcell_log
                  if R == [2, 4, 5, 4, 2])
    print("   first cells with residual exactly A: %d of %d decided"
          % (a_first, len(firstcell_log)))
    if a_first < 2:
        fired["K5"] += 1
        print("   K5 fewer than two first cells carry residual A")

    print("\n[C3, C4, C5] the controls that pass silently, counted: "
          "%d cells examined; bracket holds at %d of those checked; "
          "split reconstructs at %d; leftover permutation-stable at %d"
          % (TALLY["cells"], TALLY["C2"], TALLY["C3"], TALLY["C4perm"]))

    print("\n" + "=" * 70)
    hit = ", ".join("%s x%d" % (k, n) for k, n in sorted(fired.items())
                    if n and k != "C3")
    print("KILLS FIRED: %s" % (hit or "none"))
    print("wall %.1f s" % (time.time() - t_all))
    print("=" * 70)


if __name__ == "__main__":
    main()
