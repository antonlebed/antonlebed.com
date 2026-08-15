"""Does sign's SYNTACTIC MONOID answer to the normalized reach too, or is
the reach only the automaton's answer?

THE QUESTION. Sign in a signed-digit system (b, D) with D = {-am..ap} is
finite-state, and the minimal automaton's state count is now a closed form
in the normalized reaches: ceil(am/(b-1)) + ceil(ap/(b-1)) + 1, the two
ceilings attached to the OPPOSITE sides from the naive reading
(explore_sign_minimal.py F1, G1, G2). The companion object is not settled.
The order-wall rig recorded the TRANSITION MONOID's size at nine systems --
at reach-ceiling 1, sizes 10, 8, 8 and 3 at the four redundant cells and 3
at both balanced controls; above it, 31, 65 and 14
(explore_order_wall_shape.py F4/F5) -- and read it as not following the
reach: at ceiling 1 the state count is 3 at all six of those cells while
the monoid takes three different sizes. But those are the CLAMPED machine's
transition maps, and the clamped machine is two states too wide at exactly
the cells where (b-1) divides a. The canonical object is the SYNTACTIC
monoid: the transition monoid of the MINIMAL automaton. Nobody has computed
it, and a surplus state pair can change a monoid's size without changing
the language, so the recorded spread is not evidence about the canonical
object either way.

It matters because the monoid is what the wall is MADE of. The automaton is
the state cost; the monoid is the algebra the log-depth balanced-tree
bracketing actually evaluates. If the monoid too is a function of the
reach, the whole order-wall block collapses onto one parameter. If it is
not, the corpus has a measured quantity that genuinely escapes the reach --
a companion cost sitting beside one that does answer to it.

THE OBJECT. For the minimal Moore machine computing sgn, the transition
monoid IS the syntactic monoid of the function, so "syntactic" here is a
statement about which machine is used and not a second construction. Its
elements are the distinct maps S -> S induced by input words, under
composition, with the empty word giving the identity.

HAND-ATTACK, on paper before this file was written.

Write c- = am/(b-1) and c+ = ap/(b-1). The minimal machine's live states are
the integers in the open interval I = (-c+, c-) -- the CROSSED interval --
plus two absorbing sinks NEG and POS. Put L = I n Z and n = |L|, so the
state count is n + 2 and n = ceil(am/(b-1)) + ceil(ap/(b-1)) - 1.

STEP 1: every word acts by an affine map, then a clamp. Reading a word w of
length m and value t from a live state v lands on b^m*v + t, clamped to a
sink when that leaves I. Progressive clamping and final clamping agree:
once a prefix leaves I no tail returns it, which is exactly what makes the
sinks absorbing. So the monoid is the SET of maps

    phi_{m,t}(v) = clamp(b^m * v + t),   m >= 0, -T_m^- <= t <= T_m^+,

with T_m^± = a^±(b^m - 1)/(b-1) the exact value range of a length-m word,
and every such t realized because the digit set covers (am + ap + 1 >= b).

STEP 2: every phi_{m,t} is monotone for the chain NEG < L < POS, since
b^m*v + t increases in v and the clamp preserves order. So the live
preimages form a contiguous run: phi is NEG on a prefix of L, affine with
step b^m on a middle run, POS on a suffix.

STEP 3: the maps with AT MOST ONE live point are exactly the monotone maps
with at most one live value, and there are n^2 of those with exactly one
(choose the live argument and its image freely) and n + 1 with none (a
split point in a chain of n). All n^2 + n + 1 are realized: taking m large
makes b^m exceed the width of I, so at most one point stays live, and the
t-range T_m^± grows like c^±*b^m while the required |t| grows like
b^m*(n/2), with the slack (c - (top state)) > 0 buying the difference once
b^m is large enough.

STEP 4: a map with TWO OR MORE live points needs two integers differing by
b^m to both lie in I, hence b^m < |I| = (am + ap)/(b-1). For such m the map
determines b^m (the step between consecutive live values) and then t, so
distinct (m, t) with >= 2 live points give distinct maps, and no map of
this kind is shared between two levels. Write E_m for the number of t in
[-T_m^-, T_m^+] whose map has >= 2 live points; E_0 = 1 when n >= 2 (the
identity) and 0 when n = 1.

So the count is

    |M| = n^2 + n + 1 + SUM_{m >= 0} E_m,

and the correction SUM E_m is [n >= 2] alone -- no m >= 1 contributes --
exactly when b(b-1) >= am + ap. That is the shape the predictions below
fix: a leading term that is a function of the state count and nothing else,
plus a correction that is not.

PREDICTIONS, fixed here and weighed only after the run.
  N1 |M| = n^2 + n + 1 + SUM_{m>=0} E_m at every swept cell, symmetric and
     asymmetric, with n the minimal machine's live-state count and E_m
     computed from the integer model above. This is the whole claim: that
     the monoid is exactly the set of clamped affine maps, with no
     collisions across levels and no unrealized monotone map.
  N2 SUM_{m>=0} E_m = [n >= 2] exactly when b(b-1) >= am + ap, so on that
     part of the grid |M| = n^2 + n + 2 for n >= 2 and |M| = 3 for n = 1 --
     a function of the state count alone.
  N3 At reach-ceiling 1 on the symmetric grid (a <= b-1, minimal count 3)
     the monoid is 3 at EVERY cell. The clamped monoid's 3/8/10 spread over
     those same six recorded systems is entirely surplus-state artifact.
  N4 |M| is NOT a function of the minimal state count, nor of (b, state
     count). Named witnesses, computed by hand from the model above and
     therefore falsifiable as stated: symmetric (3,3) and asymmetric
     (b, am, ap) = (3, 3, 4) both have n = 3, and |M| = 14 for the first
     and strictly more for the second.
  N5 The clamped and minimal monoids DIFFER wherever the machines do. Hand
     figures on the recorded systems, which is where the corpus's numbers
     came from: (2,1) 10 -> 3, (3,2) 8 -> 3, (4,3) 8 -> 3, (2,2) 31 -> 16,
     (2,3) 65 -> 43, while (3,3) 14, (5,3) 3, (3,1) 3 and (5,2) 3 are
     unchanged because those machines were already minimal.
  N6 On the unsigned edge am = 0 the monoid has 2 elements at every cell:
     the machine is {0, POS} and a word either keeps 0 or leaves it.

KILLS, named as things this file PRINTS, not as what they would mean.
  K1 Any cell whose printed |M| differs from the N1 formula kills N1 and
     the "monoid = clamped affine maps" reading with it.
  K2 A cell with b(b-1) >= am + ap whose printed correction is not [n >= 2]
     kills N2.
  K3 Any symmetric cell with a <= b-1 printing |M| != 3 kills N3.
  K4 Equal printed |M| at every pair of cells sharing (b, n) kills N4 --
     which would mean the monoid does answer to the reach after all, and is
     the outcome that collapses the order-wall block.
  K5 Any recorded system whose printed clamped monoid differs from the size
     explore_order_wall_shape.py printed kills the run, not a prediction:
     the two files would be computing different objects.

CONTROLS, run and read BEFORE any size is weighed.
  C1 WITNESSED CLOSURE. Every element the closure produces carries the word
     that generated it, and the word is REPLAYED state by state on the
     machine; the replayed map must equal the stored one. A closure that
     composes in the wrong order, or that stores a map it cannot realize,
     fails here. Run at every cell.
  C2 CLAMP INVARIANCE. The monoid is recomputed from the machine built with
     the clamp pushed OUT by 3 states on each side and then minimized. The
     two minimal machines are isomorphic so the sizes must agree. This is
     the control that makes the answer a fact about sign rather than about
     a builder's constant, and it is the one the predecessor file needed.
  C3 THE CLAMPED CONTRAST IS ITSELF A CONTROL. At cells where (b-1) divides
     neither reach the clamped machine IS minimal, so the monoid computed
     from the clamped build must EQUAL the one from the minimized build.
     Cells where they differ must be exactly the cells where the state
     counts differ. This ties the new computation to the old rig's object
     at the cells where the two objects coincide -- K5 is the same tie read
     at the recorded systems.
  C4 GENERATOR SANITY. The monoid must contain the identity and be closed
     under composition, rechecked by brute force over all pairs at a sample
     of cells rather than trusted from the BFS that built it.

SCOPE. The symmetric grid is b = 2..12, a = 1..12 restricted to covering
sets (2a+1 >= b) -- the 107 cells the minimal-count sweep ran. The
asymmetric grid is b = 2..9, reaches 0..8 with at least one nonzero and
am + ap + 1 >= b -- the 528 cells of that file's Part II, split into 456
signed and 72 unsigned-edge. Monoid sizes are bounded by the number of
monotone maps on a chain of at most 25 states; the largest cells are a few
thousand elements. Memory is well under the analysis ceiling; runtime is
expected in the low minutes, dominated by the closure at b = 2.

RUN RECORD: one run over 107 symmetric cells and 528 asymmetric ones (456
signed, 72 unsigned-edge), every one of them under C1 and C2 and the nine
recorded systems additionally under C3 and C4. 0.4 s, far under the
analysis ceiling; the largest monoid on the grid is 975 elements at
(b, a) = (2, 12). All four controls clean at every cell. K1, K2, K3 and K5
all 0; N6 clean; N4 missed as stated and survives on measured witnesses
(M6); and N2, whose kill counter is among the zeros, is HALF confirmed and
half false, K2 having been written to test one direction of a biconditional
(M5). A post-run measurement and a post-run control were both added after
the findings below were read and are marked as such where they appear.

FINDINGS.

M1 THE SYNTACTIC MONOID IS EXACTLY THE SET OF CLAMPED AFFINE MAPS
   (rule, exhaustive over 107 symmetric and 456 signed asymmetric cells,
   K1 = 0). |M| = n^2 + n + 1 + SUM_{m>=0} E_m at every one, with n the
   minimal machine's live-state count. So the hand-attack's three steps all
   hold on the grid: every monotone map with at most one live point is
   realized, distinct (m, t) with two or more live points give distinct
   maps, and no such map is shared between levels. The controls are what
   make this a statement about the SYNTACTIC monoid rather than about a
   build: C2 recomputes it from a machine clamped 3 states wider on each
   side and minimized, and the size moves at zero cells.
   AND ONE CONTROL WAS ADDED AFTER THE FACT, because the frozen four could
   not see one direction. C1 replays each stored element's witness word and
   C4 checks closure under composition, so both catch a SPURIOUS element;
   nothing frozen catches a MISSING one, the BFS being trusted to be
   complete. Enumerating every word up to a bounded length and collecting
   the distinct maps directly reproduces the closure exactly at (2,2),
   (2,3), (3,3) and (3,7) -- 16, 43, 14 and 73, the last being the witness
   the whole finding turns on.

M2 AND THE ANSWER TO THE QUESTION IS NO -- THE MONOID DOES NOT ANSWER TO
   THE REACH (rule, from the sweep). The witness is symmetric and it is
   the sharpest available: at b = 3 the systems a = 7 and a = 8 have the
   SAME normalized reach ceiling 4, the same minimal machine size of 9
   states, and monoids of 73 and 75. Reach, state count and base are all
   equal across that pair and the monoid is not. Four (b, n) pairs on the
   symmetric grid carry two sizes each, and the asymmetric grid -- which
   contains the symmetric diagonal, so its pairs are not a separate tally
   -- carries two pairs at three sizes: (3, 7) widened from the symmetric
   two by cells off the diagonal, and (3, 6), which has no symmetric
   member at all because a symmetric n is 2R - 1 and therefore odd. So the
   failure is generic rather than a single cell. The
   automaton's collapse onto one parameter therefore does NOT extend to the
   algebra the log-depth bracketing evaluates, and the order-wall block
   keeps two parameters.

M3 THE RECORDED SPREAD WAS SURPLUS-STATE ARTIFACT, AND THE OLD NUMBERS ARE
   CONFIRMED AS THE CLAMPED MACHINE'S. At reach-ceiling 1 the syntactic
   monoid is 3 at EVERY symmetric cell (K3 = 0), so the 3 / 8 / 10 spread
   explore_order_wall_shape.py recorded over six such systems collapses to
   a single value once the two surplus states are merged away. That rig's
   sizes are reproduced here exactly from its own object -- 10, 8, 8, 3 at
   reach 1 and 31, 65, 14 above it (K5 = 0) -- which is what makes this a
   correction to the ATTRIBUTION rather than a disagreement: both files
   compute the same thing, and only one of them was computing the canonical
   object. The syntactic sizes at those nine are 3, 3, 3, 3, 16, 43, 14, 3,
   3, and the five that move are exactly the five whose machines were not
   minimal. N5 named all nine of those numbers on paper before the engine
   existed, both columns, and hit every one -- which is the strongest
   evidence here that the integer model is the object and not a fit, since
   16 and 43 were computed from the model by hand and could not have been
   read off anything.

M4 SO WHAT ESCAPES THE REACH IS ISOLATED TO ONE TERM. The leading part
   n^2 + n + 1 is a function of the state count alone and hence of the
   reach pair; every departure in M2 lives in the correction. The seam is
   therefore not "the monoid is a different object from the automaton" but
   "the monoid is the automaton's count plus a residue that reads the digit
   set below the resolution the reach has". At (3,7) against (3,8) the
   corrections are 16 and 18 against an identical leading 57.

M5 THE CORRECTION'S SUPPORT IS EXACTLY A LATTICE CONDITION (post-run
   measurement, added after M1-M4 were read and not a frozen prediction;
   269 levels tested, 0 mismatches). The hand-attack's b^m < |I| is
   NECESSARY for a level to contribute and it is NOT SUFFICIENT: 33 of the
   269 levels it admits contribute nothing. A level contributes iff the
   crossed interval I holds two INTEGERS exactly b^m apart, which an
   interval longer than b^m can fail -- at (b, a) = (3, 4), I = (-2, 2)
   has length 4 > 3 and no pair of integers 3 apart inside it, so E_1 = 0
   and the monoid is 14, the same as (3,3) where the level does not exist
   at all. That closes the SUPPORT of the sum in floors and ceilings and
   nothing more: which levels contribute is now a criterion, how much each
   contributes is still a count, so |M| remains a formula plus a computed
   sum rather than an expression. The SCOPE paragraph below is that same
   fact stated as the front it leaves.
   AND THIS IS ALSO N2's VERDICT, WHICH IS NOT "IT HELD". N2 was frozen as
   "SUM E_m = [n >= 2] EXACTLY WHEN b(b-1) >= am + ap" -- a biconditional --
   while K2 was written to fire only on a cell satisfying b(b-1) >= am + ap
   whose correction differs. So the kill tests the forward direction alone,
   and K2 = 0 says that direction held at every cell and says nothing about
   the other. The other is FALSE, and (3, 3, 4) is the witness: 6 < 7, so
   N2's condition fails, and the correction is 1 = [n >= 2] all the same.
   A zero kill counter is not a confirmed prediction when the prediction is
   an iff and the kill is an implication -- which is why the criterion here
   had to be measured rather than inferred from K2.

M6 N4 MISSED ON ITS NAMED WITNESS AND THE MISS IS THE SAME LATTICE FACT.
   N4 predicted (b, am, ap) = (3, 3, 4) would exceed symmetric (3,3) at
   equal state count; both print 14. The witness was chosen by the
   necessary condition b(b-1) < am + ap -- 6 < 7 -- without checking
   sufficiency, and I = (-2, 1.5) holds no two integers 3 apart. The
   prediction's SUBSTANCE survives on witnesses the sweep found instead
   (M2), and the miss is recorded rather than folded in because it is the
   same error M5 corrects, caught by the grid rather than by the slate.

M7 THE UNSIGNED EDGE IS 2 EVERYWHERE (rule, all 72 edge cells, N6 clean).
   N6 named only am = 0 and the sweep ran the whole edge, ap = 0 included:
   with one reach at zero every value carries the other side's sign or is
   zero, so the machine is the all-zeros class and one sink, and a word
   either keeps 0 or leaves it forever. The monoid has two elements
   whatever the other reach and the base are. The edge degenerates in the
   monoid exactly as it does in the state count.

SCOPE, and the front this leaves. What SUM E_m is as a formula rather than
a count is untouched: M5 says exactly which levels contribute, not how much
each contributes. The per-level E_m is a count of integer translates of a
fixed step landing twice in an interval, which is a lattice-point count and
looks closed-form, and settling it would turn |M| into an expression rather
than a sum. That is the cheap next probe, and it is where the digit set
enters at a resolution the reach does not have.
AND THE SPLIT IS ALGEBRAIC, NOT JUST ARITHMETIC, which is the handle to
take it by. The n^2 + n + 1 maps with at most one live point form an IDEAL:
every phi is injective on its own live run, since consecutive live values
differ by b^m >= 1, so composing a rank-<= 1 map with anything on either
side stays rank <= 1. So the monoid is that ideal plus SUM E_m elements of
higher rank, the ideal is the part fixed by the state count, and everything
that escapes the reach lives in the higher-rank quotient. A formula for E_m
is therefore a count of the monoid ABOVE its ideal rather than a lattice
identity that happens to fit.
THAT FRONT IS CLOSED: explore_monoid_correction.py derives E_m, and the
constraint that binds it turns out to be the word range and not the machine.
"""

import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from explore_sign_minimal import (
    RECORDED, build, build_margin, ceil_div, minimize, sgn, sweep, asym_cells,
)

CONTROLS = [(3, 1), (5, 2)]  # the balanced non-redundant systems


# ---------------------------------------------------------------- machines

def quotient(b, am, ap, margin=0):
    """Minimize the clamped build and return the minimal machine explicitly.

    Returns (nstates, blocks, delta, out) with blocks a sorted list of block
    ids and delta[block][digit] the induced transition. The minimal machine
    is what the syntactic monoid is the transition monoid OF, so it is built
    here rather than reasoned about.
    """
    st, dl, ou, s0 = build_margin(b, am, ap, margin)
    _, cls = minimize(st, dl, ou, s0)
    delta, out = {}, {}
    for s, blk in cls.items():
        row = {d: cls[t] for d, t in dl[s].items()}
        if blk in delta and delta[blk] != row:
            raise AssertionError(f"quotient not well defined at {(b, am, ap)}")
        delta[blk] = row
        out[blk] = ou[s]
    blocks = sorted(delta)
    return len(blocks), blocks, delta, out


def clamped(b, am, ap):
    """The unminimized clamped machine, as the old rig's object."""
    st, dl, ou, s0 = build_margin(b, am, ap, 0)
    # restrict to the reachable part -- the old rig's count is over states
    # the start can actually get to
    seen, stack = {s0}, [s0]
    while stack:
        s = stack.pop()
        for t in dl[s].values():
            if t not in seen:
                seen.add(t)
                stack.append(t)
    blocks = sorted(seen, key=str)
    delta = {s: dict(dl[s]) for s in blocks}
    return len(blocks), blocks, delta, {s: ou[s] for s in blocks}


# ------------------------------------------------------------------ monoid

def transition_monoid(blocks, delta, witnesses=False):
    """The monoid of maps induced by input words, as tuples over `blocks`.

    Closure by BFS: start from the identity, right-multiply by each digit's
    map. Composition order is "apply the stored map, then the digit", which
    is the order words are read in.
    """
    index = {s: i for i, s in enumerate(blocks)}
    digits = sorted(delta[blocks[0]])
    gens = {d: tuple(index[delta[s][d]] for s in blocks) for d in digits}
    ident = tuple(range(len(blocks)))
    seen = {ident: ()}
    frontier = [ident]
    while frontier:
        nxt = []
        for f in frontier:
            for d in digits:
                g = gens[d]
                comp = tuple(g[f[i]] for i in range(len(blocks)))
                if comp not in seen:
                    seen[comp] = seen[f] + (d,)
                    nxt.append(comp)
        frontier = nxt
    return seen if witnesses else set(seen)


def replay_map(blocks, delta, word):
    """C1: the map of `word`, computed by walking the machine from each
    state independently rather than by composing stored tuples."""
    index = {s: i for i, s in enumerate(blocks)}
    out = []
    for s in blocks:
        cur = s
        for d in word:
            cur = delta[cur][d]
        out.append(index[cur])
    return tuple(out)


# ------------------------------------------------------- the integer model

def live_states(b, am, ap):
    """The integers in the crossed open interval (-ap/(b-1), am/(b-1))."""
    lo = -ap / (b - 1)
    hi = am / (b - 1)
    v, out = 0, []
    top = ceil_div(am, b - 1)
    bot = -ceil_div(ap, b - 1)
    for v in range(bot, top + 1):
        if lo < v < hi:
            out.append(v)
    return out


def correction(b, am, ap):
    """SUM_{m>=0} E_m from the hand-attack: the number of (m, t) whose
    clamped affine map keeps two or more live points."""
    L = live_states(b, am, ap)
    if len(L) < 2:
        return 0
    lo = -ap / (b - 1)
    hi = am / (b - 1)
    total, m, q = 0, 0, 1
    while True:
        if m > 0 and q >= (am + ap) / (b - 1):
            break
        Tm = am * (q - 1) // (b - 1)
        Tp = ap * (q - 1) // (b - 1)
        count = 0
        for t in range(-Tm, Tp + 1):
            hits = 0
            for v in L:
                u = q * v + t
                if lo < u < hi:
                    hits += 1
                    if hits == 2:
                        break
            if hits >= 2:
                count += 1
        total += count
        m += 1
        q *= b
    return total


def two_apart(b, am, ap, m):
    """POST-RUN, not a frozen prediction: does the crossed interval hold two
    integers exactly b^m apart? The hand-attack's b^m < |I| is NECESSARY for
    a level to contribute and the run showed it is not SUFFICIENT -- at
    (b, am, ap) = (3, 3, 4) the interval (-2, 1.5) has length 3.5 > 3 and
    still holds no pair 3 apart. This is the exact condition, tested against
    the measured E_m below."""
    q = b ** m
    # an integer u with -ap/(b-1) < u and u + q < am/(b-1)
    lo = -ceil_div(ap, b - 1)
    for u in range(lo, lo + q + 2):
        if -ap / (b - 1) < u and u + q < am / (b - 1):
            return True
    return False


def levels(b, am, ap):
    """Per-level E_m, as a list indexed by m, for the criterion check."""
    L = live_states(b, am, ap)
    if len(L) < 2:
        return []
    lo, hi = -ap / (b - 1), am / (b - 1)
    out, m, q = [], 1, b
    while q < (am + ap) / (b - 1):
        Tm, Tp = am * (q - 1) // (b - 1), ap * (q - 1) // (b - 1)
        count = 0
        for t in range(-Tm, Tp + 1):
            hits = 0
            for v in L:
                if lo < q * v + t < hi:
                    hits += 1
                    if hits == 2:
                        break
            if hits >= 2:
                count += 1
        out.append(count)
        m += 1
        q *= b
    return out


def predicted(b, am, ap):
    """The integer model, SIGNED SETS ONLY. At a reach of 0 the crossed
    interval degenerates -- it excludes the state 0 that is the whole live
    set there -- so the model would silently return 3 where the machine has
    two states and a two-element monoid (M7). Refused rather than guarded,
    since a wrong number is worse than a stopped run."""
    if not (am and ap):
        raise ValueError(f"model is for signed sets; {(b, am, ap)} is edge")
    n = len(live_states(b, am, ap))
    return n * n + n + 1 + correction(b, am, ap), n


# ------------------------------------------------------------------- sweep

def cell_report(b, am, ap, do_controls):
    """One cell: the syntactic monoid, the model, and the controls."""
    n_min, blocks, delta, out = quotient(b, am, ap, 0)
    mon = transition_monoid(blocks, delta, witnesses=True)
    size = len(mon)
    fails = []

    if do_controls:
        for mp, word in mon.items():
            if replay_map(blocks, delta, word) != mp:
                fails.append("C1")
                break
        _, wb, wd, _ = quotient(b, am, ap, 3)
        if len(transition_monoid(wb, wd)) != size:
            fails.append("C2")

    return size, n_min, fails, mon


def main():
    print("SIGN'S SYNTACTIC MONOID -- does it answer to the reach?")
    print()

    # ---------------- controls on the recorded systems, read first --------
    print("C1/C2/C3/K5 on the nine recorded systems")
    print(f"{'(b,a)':>8} {'states':>7} {'clamped':>8} {'monoid':>7} "
          f"{'clampM':>7} {'model':>7} {'ctl':>5}")
    ctl_fail = 0
    for (b, a) in RECORDED + CONTROLS:
        size, n_min, fails, mon = cell_report(b, a, a, True)
        n_cl, cb, cd, _ = clamped(b, a, a)
        csize = len(transition_monoid(cb, cd))
        # C4: closure under composition, brute force over all pairs
        S = set(mon)
        for x in S:
            for y in S:
                if tuple(y[x[i]] for i in range(len(x))) not in S:
                    fails.append("C4")
                    break
            else:
                continue
            break
        pred, _ = predicted(b, a, a)
        ctl_fail += len(fails)
        print(f"{str((b, a)):>8} {n_min:>7} {n_cl:>8} {size:>7} "
              f"{csize:>7} {pred:>7} {','.join(fails) or 'ok':>5}")
    print(f"control failures on the recorded systems: {ctl_fail}")
    print()

    # ---------------- the symmetric grid ----------------------------------
    print("=" * 64)
    print("PART I -- THE SYMMETRIC GRID")
    print()
    cells = sweep()
    k1 = k2 = k3 = 0
    c_fail = 0
    by_shape = {}
    reach1 = set()
    for (b, a) in cells:
        size, n_min, fails, _ = cell_report(b, a, a, True)
        c_fail += len(fails)
        pred, n = predicted(b, a, a)
        if size != pred:
            k1 += 1
            print(f"  K1 at (b,a)={(b, a)}: monoid {size}, model {pred}")
        corr = correction(b, a, a)
        want = 1 if n >= 2 else 0
        if b * (b - 1) >= 2 * a and corr != want:
            k2 += 1
            print(f"  K2 at (b,a)={(b, a)}: correction {corr}, want {want}")
        if a <= b - 1:
            reach1.add(size)
            if size != 3:
                k3 += 1
                print(f"  K3 at (b,a)={(b, a)}: reach-ceiling 1 gives {size}")
        by_shape.setdefault((b, n), set()).add(size)
    print(f"cells: {len(cells)}   control failures: {c_fail}")
    print(f"K1 {k1}   K2 {k2}   K3 {k3}")
    print(f"sizes at reach-ceiling 1 (a <= b-1): {sorted(reach1)}")
    split = {k: v for k, v in by_shape.items() if len(v) > 1}
    print(f"(b, n) pairs carrying more than one monoid size: {len(split)}")
    for k in sorted(split)[:6]:
        print(f"   b={k[0]} n={k[1]}: {sorted(split[k])}")
    print()

    # a small table of the symmetric cells, for the record
    print(f"{'(b,a)':>8} {'n':>3} {'states':>7} {'monoid':>7} {'corr':>6}")
    for (b, a) in cells:
        if b <= 4 and a <= 6:
            size, n_min, _, _ = cell_report(b, a, a, False)
            n = len(live_states(b, a, a))
            print(f"{str((b, a)):>8} {n:>3} {n_min:>7} {size:>7} "
                  f"{correction(b, a, a):>6}")
    print()

    # ---------------- the asymmetric grid ---------------------------------
    print("=" * 64)
    print("PART II -- THE ASYMMETRIC GRID")
    print()
    acells = asym_cells()
    signed = [c for c in acells if c[1] and c[2]]
    edge = [c for c in acells if not (c[1] and c[2])]
    l1 = l2 = l6 = 0
    ac_fail = 0
    shapes = {}
    for (b, am, ap) in signed:
        size, n_min, fails, _ = cell_report(b, am, ap, True)
        ac_fail += len(fails)
        pred, n = predicted(b, am, ap)
        if size != pred:
            l1 += 1
            if l1 <= 8:
                print(f"  K1 at {(b, am, ap)}: monoid {size}, model {pred}")
        corr = correction(b, am, ap)
        want = 1 if n >= 2 else 0
        if b * (b - 1) >= am + ap and corr != want:
            l2 += 1
            if l2 <= 8:
                print(f"  K2 at {(b, am, ap)}: correction {corr}, "
                      f"want {want}")
        shapes.setdefault((b, n), set()).add(size)
    print(f"signed cells: {len(signed)}   control failures: {ac_fail}")
    print(f"K1 {l1}   K2 {l2}")
    asplit = {k: v for k, v in shapes.items() if len(v) > 1}
    print(f"(b, n) pairs carrying more than one monoid size: {len(asplit)}")
    for k in sorted(asplit)[:6]:
        print(f"   b={k[0]} n={k[1]}: {sorted(asplit[k])}")
    print()

    edge_sizes = set()
    for (b, am, ap) in edge:
        size, n_min, _, _ = cell_report(b, am, ap, False)
        edge_sizes.add(size)
        if size != 2:
            l6 += 1
            if l6 <= 8:
                print(f"  N6 miss at {(b, am, ap)}: monoid {size}")
    print(f"unsigned-edge cells: {len(edge)}   sizes: {sorted(edge_sizes)}"
          f"   N6 misses: {l6}")
    print()

    # ---------------- N4: the two named witnesses -------------------------
    print("=" * 64)
    print("N4 -- the named witnesses")
    s33, n33, _, _ = cell_report(3, 3, 3, False)
    s34, n34, _, _ = cell_report(3, 3, 4, False)
    print(f"  symmetric (3,3):      states {n33}, monoid {s33}")
    print(f"  asymmetric (3, 3, 4): states {n34}, monoid {s34}")
    print(f"  same state count: {n33 == n34}   same monoid: {s33 == s34}")
    print()

    # ---------------- post-run: the exact criterion for a contributing level
    print("=" * 64)
    print("POST-RUN MEASUREMENT -- when does a level contribute?")
    bad = necessary_only = 0
    tested = 0
    for (b, am, ap) in [(b, a, a) for (b, a) in cells] + signed:
        for i, e in enumerate(levels(b, am, ap)):
            tested += 1
            crit = two_apart(b, am, ap, i + 1)
            if (e > 0) != crit:
                bad += 1
                if bad <= 8:
                    print(f"  mismatch at {(b, am, ap)} m={i+1}: "
                          f"E={e}, criterion {crit}")
            if e == 0:
                necessary_only += 1
    print(f"levels tested (b^m < |I|): {tested}   "
          f"of which E_m = 0: {necessary_only}   mismatches: {bad}")
    print()

    # ---------------- post-run: closure completeness by brute enumeration --
    print("POST-RUN CONTROL -- the closure against word enumeration")
    print(f"{'(b,a)':>8} {'words<=L':>9} {'brute':>7} {'closure':>8}")
    for (b, a), L in [((2, 2), 8), ((2, 3), 7), ((3, 3), 6), ((3, 7), 5)]:
        _, blocks, delta, _ = quotient(b, a, a, 0)
        index = {s: i for i, s in enumerate(blocks)}
        digits = sorted(delta[blocks[0]])
        seen = set()
        frontier = {tuple(blocks)}
        for _ in range(L):
            nxt = set()
            for row in frontier:
                for d in digits:
                    nxt.add(tuple(delta[s][d] for s in row))
            seen |= frontier
            frontier = nxt
        seen |= frontier
        brute = {tuple(index[s] for s in row) for row in seen}
        print(f"{str((b, a)):>8} {L:>9} {len(brute):>7} "
              f"{len(transition_monoid(blocks, delta)):>8}")


if __name__ == "__main__":
    sys.exit(main())
