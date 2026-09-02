"""Which states SEED the annihilation of the flush law's invariant --
the direct failures of R1 at every losing lookahead, split flushed /
mid-flush, and which kind the collapse runs through.

THE QUESTION
------------
c_int = max(c_saf, L*) is an observation with both sides proved lower
bounds and no sufficiency proof (explore_flush_law.py). The lemma a
proof owes has its invariant named (explore_flush_closure.py F4): let
R1 be the safe states from which a (0, 0)-holder is reachable under
zero input by moves whose EVERY reply is safe; then at c = c_int the
reader's winning set IS R1 at all 130 cells, while at every losing
lookahead from c_saf up one safety pass ANNIHILATES R1 to the empty set
rather than trimming it, at 41 pairs. An annihilation is seeded: some
state of R1 has no digit keeping every reply in R1, and its removal
takes the rest. This rig asks WHICH states those are. If they are the
FLUSHED ones -- the (0, 0)-holders -- the lemma reduces to a statement
about flushed states alone, which is exactly where L* is defined (the
lookahead of the clairvoyant reader from a flushed state), and the
proof owed becomes: at c >= L* no flushed state of R1 fails. That is
the question as it was asked; F3 declines the inference and says what
the prints support instead.

Conventions are the engine's (explore_redundant_ostrowski.py, Game): a
state is (pos, branch set, pzd, pze); a branch is the lattice point
sum (e - m d)_k theta_k - M in the frame of the current period; the
reader emits e_t having seen d_0..d_{t+c}. SAFE is the safety fixpoint
(explore_flush_price.safety_wins); a DIRECT failure of a set B is a
state of B with no digit keeping every reply in B, and everything else
the closure of B removes is propagation from one.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
H1  WHAT BEATS A FLUSHED STATE, ONE DIGIT. From a flushed state at
    level t -- residual 0 with the run's own lift alive -- the
    adversary's late digit a_{k+1} at its cap forces the reader to
    write m a_{k+1} q_k from level k - c with nothing below it
    (explore_flush_floor.py: the flushed state is the exposed one).
    Below L*'s one-digit case that
    integer has no capped string from that level, so after the cap
    reply no zero-input play reaches a (0, 0)-holder again: the reply
    leaves R1, and it leaves it for EVERY output digit the flushed
    state can emit, since the digit written now sits above the level
    the missing string would need. So at a cell whose L* is set by one
    late digit, a flushed direct failure is expected at every c < L*,
    and the reply at fault is the LARGEST LEGAL input digit -- the
    position's cap, or one below it where the preceding digit was
    nonzero, legality forbidding the cap there (Game.inputs).
H2  WHERE ONE DIGIT IS NOT ENOUGH. At V1 (1,1,1,2) x5, (s, s_0) =
    (1, 0) and (1, 1), the corpus reads L* = 4 with a late TAIL rather
    than a late digit needing the four levels, one digit codable at a
    smaller drop (explore_flush_law.py F2, explore_flush_closure.py
    H5). There the flushed state serves every single reply and the
    failure can only appear after the tail's first digits, at a state
    that is safe and not flushed. So the flushed / mid-flush split of
    R1's direct failures is predicted to track the one-digit / tail
    distinction, and those two cells are the specimens where a flushed
    failure alone cannot seed the annihilation.
H3  REMOVAL SAYS NOTHING AND EXEMPTION READS ONLY ITS EXCESS. Removing
    the failures of one kind from R1 and closing what is left is
    VACUOUS: closure is MONOTONE (a closed subset of the smaller set is
    a closed subset of the larger) and the parent already reads
    closure(R1) empty at every losing pair, so ANY subset of R1 closes
    to empty there whatever is removed. EXEMPTION -- closing R1 while
    one kind of state is never removed and stays a legal target -- is
    not vacuous, but its SIZE is not the reading either: the exempt set
    survives by construction, so a non-empty result says only that the
    exempt set is non-empty. What carries content is the EXCESS over
    the exempt set, the states of the OTHER kind that survive once this
    kind is forgiven. Two exempt closures, two independent questions:
    forgive the flushed states and the excess is the mid-flush states
    the flushed failures were killing; forgive the mid-flush states and
    the excess is the flushed states the mid-flush failures were. Both
    excesses are printed against their exempt sets, and the equality
    case -- no excess -- is the one that says the forgiven kind was
    carrying nothing.
H4  R1 IS NOT SAFE-AND-CODABLE and the difference is not this rig's
    subject: five cells hold a safe codable state every winning
    strategy avoids (explore_flush_closure.py F2). R1 is defined by
    reachability under zero input through safe moves and is computed
    here from the safety fixpoint alone -- no codability recursion
    enters, which is also why this rig is cheaper than its parent.
H5  A FLUSHED STATE IS ALWAYS IN R1 WHEN IT IS SAFE (distance 0), so
    R1 contains every safe (0, 0)-holder and the flushed direct
    failures are read over all of them. At c = c_int the parent's
    W = R1 forces both failure counts to 0 -- a control on this
    construction and never a finding.
H6  WHERE IT CAN BLOW UP. The band cells' games are the corpus's
    heaviest (348 MB at lookahead 2, explore_flush_price.py F6), so the
    band is its own stage under memwatch. Ascending c from 0 per cell
    is the parent's own walk (27 s for the grid with a codability
    recursion this rig drops).
TRANSPLANT, marked: the game, its box, the grid, the band cells, the
frozen c_int / c_saf readings and the safety fixpoint are the parents'
(explore_redundant_ostrowski.py, explore_flush_price.py,
explore_flush_closure.py); nothing here re-derives them.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  K0 (controls, run FIRST; nothing below is read if any leg is red)
     (a) R1 = W at c = c_int at every cell -- R1 minus W and W minus R1
         both empty (the parent's F4 through this rig's own build; a
         violation is a fault of the R1 construction, never a finding).
     (b) the direct failures of R1 at c = c_int: 0 flushed and 0
         mid-flush at every cell (H5).
     (c) c_int reproduces the parents' frozen rows -- silver x2
         "- 2 2 2 0 0", silver x3 "- 3 2 2 2 2", bronze x2
         "- 2 2 2 2 0", bronze x3 "- 2 2 2 2 2".
  K1 THE SPLIT, at every (cell, c) with c_saf <= c < c_int: the direct
     failures of R1, counted flushed and mid-flush. Prediction: at
     least one FLUSHED failure at every such pair except V1 (1,1,1,2)
     x5 at (1, 0) and (1, 1), where H2 predicts 0 flushed and at least
     one mid-flush. KILL, as an observable: a pair with 0 flushed
     failures anywhere else, or a nonzero flushed count at those two.
  K2 THE TWO EXCESSES (H3), per losing pair: R1 closed with the
     FLUSHED states exempt, against the count of flushed states in R1,
     and R1 closed with the non-flushed states exempt, against the count
     of those. No prediction is fixed on the excesses -- the first two
     designs of this observable were wrong (H3) and what the pair reads
     is settled only by the print. Each pair is classified: R1 ENTIRELY
     flushed (the excess questions are empty there), a nonzero excess
     when the flushed states are forgiven, or neither.
  K2b THE COMPOSITION, per losing pair: the size of R1 and how much of
     it is flushed. Prediction: at every pair holding a non-flushed
     state at least one non-flushed state fails directly. KILL, as an
     observable: a pair with a non-flushed state and no mid-flush
     direct failure, printed with its sizes.
  K3 THE CAP SIGNATURE (H1): per flushed direct failure, the count of
     output digits whose broken reply is the LARGEST LEGAL input digit,
     against the count broken only by a smaller one. Predicted: every
     digit broken by that reply. Printed, and no kill rides on it -- it
     says which mechanism the failure is, not whether it is there.
  K4 state counts, wall-clock and peak per stage.

THE DESIGN
----------
Stages: s1 the grid (the 120 cells that read; the zero-slack column,
which reads at no lookahead, is skipped), s2 the ten band cells. Per
cell c ascends 0..c_int with the parent's cap (h3_bound, else LOOKCAP);
per (cell, c): Game(win, 1, m, (0,), c, s, s_0); SAFE by the parent's
safety loop; R1 by the flush refinement of SAFE -- the (0, 0)-holders
of SAFE, then the reverse reachability under the zero reply over moves
whose every reply is safe, which is Game.solve's first refinement with
its argument the safety fixpoint; the direct failures of R1 by the
parent's closure helper; the two exempt closures of H3 read by their
EXCESS over their exempt sets. c_saf is the least c whose SAFE holds
every init, c_int the least whose W does. Stage selection by
SEED_STAGES, the band cells by SEED_CELLS, one process per stage under
memwatch.

FINDINGS (post-run; the prints are the record. Grid 24 s at 145 MB,
band 14 s at 347 MB, one process each under memwatch. K2's observable
went through TWO wrong designs before the one that ran, both caught
before any number was read as a finding: a REMOVAL that monotonicity
makes empty whatever is removed, and an EXEMPTION read by its SIZE
where only its EXCESS over the exempt set says anything -- H3 carries
both, and F3 below rests on the excess and on nothing else.)
----------------------------------------------
F1  THE CONTROLS HOLD (K0). R1 = W at c = c_int at all 120 grid cells
    and all 10 band cells, no direct failure of R1 of either kind
    there, and the four frozen parent rows reproduce through this rig's
    own builds.
F2  A FLUSHED FAILURE AT EVERY LOSING PAIR (K1; observation, 41 pairs).
    At every (cell, c) with c_saf <= c < c_int -- 30 on the grid, 11 in
    the band -- R1 has at least one FLUSHED direct failure, and none is
    without one. H2 is REFUTED where it had content: at V1 (1,1,1,2) x5
    (1, 0) and (1, 1) at c = 3, the cells whose L* is set by a late TAIL
    rather than a late digit, the split is 7 flushed / 20 mid-flush and
    7 / 22. A tail setting L* does not spare the flushed state, so the
    flushed / mid-flush split does not track the one-digit / tail
    distinction. And wherever R1 holds a non-flushed state at all, at
    least one non-flushed state fails directly too (K2b, no exception
    at either stage).
F3  THE ASYMMETRY (K2; observation, 41 pairs). Forgive the flushed
    states -- exempt them from having to serve, leaving them as legal
    targets -- and non-flushed states SURVIVE at 21 of the 41 pairs (19
    grid, 2 band), by as many as 342 at V2 (2,1,3,1) x3 (3, 3); forgive
    the non-flushed states instead and NOT ONE flushed state survives,
    at any pair of either stage. So the collapse runs one way: below
    c_int the flushed failures take the mid-flush states with them at
    half the pairs, and the mid-flush failures never take a flushed
    state anywhere. What that does NOT license is the reduction this
    rig went looking for. At 13 of the 41 pairs (7 grid, 6 band)
    forgiving the flushed states rescues nothing -- an obstruction sits
    on the mid-flush side of those on its own -- and at 7 more (4, 3)
    R1 is ENTIRELY flushed states, where the question does not arise.
F4  THE CAP SIGNATURE IS THE MAJORITY AND NOT THE WHOLE (K3, H1). Of
    the output digits at a flushed direct failure, 700 of 1,005 on the
    grid and 609 of 653 in the band are broken by the LARGEST LEGAL
    input reply, the rest by a smaller one only. The late digit at the
    top of its range is the mechanism at most of them, and a third of
    the grid's are beaten below it.

  TIER. F2 and F4 are OBSERVATIONS, exhaustive at the 130 cells and the
  41 losing pairs the corpus decides. F3's counts are exhaustive there
  too, but its reading -- the excess and not the size -- was settled
  AFTER the run against H3's argument, and no prediction stands under
  it. What this leaves for a proof of c_int = max(c_saf, L*): the owed
  lemma keeps its invariant R1 -- at c >= max(c_saf, L*) every state of
  R1 has a digit keeping every reply in R1 -- and gains the failing
  side's shape, an obstruction that is one-directional and yet not
  confined to the flushed states. Where to look next is the 13 pairs
  whose mid-flush side fails on its own: what those cells have that the
  21 do not is the one structural split this rig printed and did not
  read.

RUN RECORD. SEED_STAGES=s1 and SEED_STAGES=s2, each
python memwatch.py explore_flush_seed.py; peaks and walls in the
findings header; nothing ran bare.
"""

import os
import sys
import time
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_redundant_ostrowski import (               # noqa: E402
    GRID, WINDOWS, Game, LOOKCAP, h3_bound)
from explore_flush_price import BAND, window_of         # noqa: E402
from explore_flush_closure import safety_set, closure   # noqa: E402

PARENT = {("silver [2]", 2): "- 2 2 2 0 0", ("silver [2]", 3): "- 3 2 2 2 2",
          ("bronze [3]", 2): "- 2 2 2 2 0", ("bronze [3]", 3): "- 2 2 2 2 2"}


def flush_refine(g, S):
    """Game.solve's first flush refinement, over the set S: the states
    of S from which a (0, 0)-holder is reachable under the zero reply
    by moves whose every reply is in S."""
    Z = set(i for i in S if g.holds0[i])
    dist = {s: 0 for s in Z}
    dq = deque(Z)
    rev = {}
    for s in S:
        for _y, succ in g.trans[s].items():
            if all(s2 in S for _x, s2 in succ):
                for x, s2 in succ:
                    if x == 0:
                        rev.setdefault(s2, []).append(s)
    while dq:
        s = dq.popleft()
        for s0 in rev.get(s, ()):
            if s0 not in dist:
                dist[s0] = dist[s] + 1
                dq.append(s0)
    return set(dist), dist


def closure_exempt(g, base, exempt):
    """The greatest subset of `base` in which every state OUTSIDE
    `exempt` has a digit keeping every reply inside; the exempt states
    are never removed and stay legal targets."""
    I = set(base)
    changed = True
    while changed:
        changed = False
        for s in list(I):
            if s in exempt:
                continue
            ok = any(all(s2 in I for _x, s2 in succ)
                     for succ in g.trans[s].values())
            if not ok:
                I.discard(s)
                changed = True
    return I


def cap_signature(g, i, R1):
    """K3: over the output digits of a failing state, how many are
    broken by the LARGEST LEGAL input reply -- the position's cap, or
    one below where legality forbids it -- and how many only by a
    smaller one."""
    by_cap = other = 0
    for _y, succ in g.trans[i].items():
        bad = [x for x, s2 in succ if s2 not in R1]
        if not bad:
            continue
        xmax = max(x for x, _s2 in succ)
        if xmax in bad:
            by_cap += 1
        else:
            other += 1
    return by_cap, other


def read_cell(win, m, s, s0, top):
    """Ascend c = 0..c_int; per c the R1 counts and the seeding test."""
    rows = []
    c_int = c_saf = None
    for look in range(top + 1):
        t0 = time.time()
        g = Game(win, 1, m, (0,), look, s, s0)
        S = safety_set(g)
        R1, _dist = flush_refine(g, S)
        _I, direct = closure(g, R1)
        fl = set(i for i in direct if g.holds0[i])
        holds = set(i for i in R1 if g.holds0[i])
        keep_fl = closure_exempt(g, R1, holds)
        keep_mid = closure_exempt(g, R1, R1 - holds)
        vac = (len(keep_fl) == len(holds)
               and len(keep_mid) == len(R1) - len(holds))
        caps = [cap_signature(g, i, R1) for i in sorted(fl)]
        rows.append(dict(
            look=look, states=g.n_states, S=len(S), R1=len(R1), W=len(g.W),
            R1_W=len(R1 - g.W), W_R1=len(g.W - R1),
            d_fl=len(fl), d_mid=len(direct) - len(fl),
            keep_fl=len(keep_fl), keep_mid=len(keep_mid),
            n_holds=len(holds), vac=vac,
            by_cap=sum(a for a, _b in caps), by_other=sum(b for _a, b in caps),
            wall=time.time() - t0))
        if c_saf is None and all(i in S for i in g.init):
            c_saf = look
        if all(i in g.W for i in g.init):
            c_int = look
            break
    return c_int, c_saf, rows


def fmt(v):
    return "-" if v is None else str(v)


def new_tallies():
    return dict(ctrl_bad=0, cells=0, pairs=0, k1_flushed=0, k1_none=[],
                k2_empty=0, k2_exc=0, k2_none=0, k2_mexc=0,
                k2_left=[], k2_odd=[], by_cap=0, by_other=0)


def report(name, m, s, s0, c_int, c_saf, rows, tallies):
    parts = []
    for r in rows:
        look = r["look"]
        losing = (c_saf is not None and c_int is not None
                  and c_saf <= look < c_int)
        parts.append("c%d:%d/%d|R1 %d,%df%s"
                     % (look, r["d_fl"], r["d_mid"], r["R1"], r["n_holds"],
                        "!EXC" if losing and not r["vac"] else ""))
        if c_int is not None and look == c_int:
            tallies["cells"] += 1
            if r["R1_W"] or r["W_R1"] or r["d_fl"] or r["d_mid"]:
                tallies["ctrl_bad"] += 1
                parts.append("CTRL-BAD(R1\\W %d, W\\R1 %d, fl %d, mid %d)"
                             % (r["R1_W"], r["W_R1"], r["d_fl"], r["d_mid"]))
        if c_saf is not None and c_int is not None and c_saf <= look < c_int:
            tallies["pairs"] += 1
            tallies["by_cap"] += r["by_cap"]
            tallies["by_other"] += r["by_other"]
            if r["d_fl"]:
                tallies["k1_flushed"] += 1
            else:
                tallies["k1_none"].append((name, m, s, s0, look, r["d_mid"]))
            if not r["vac"]:
                tallies["k2_left"].append((name, m, s, s0, look,
                                           r["keep_fl"], r["n_holds"],
                                           r["keep_mid"],
                                           r["R1"] - r["n_holds"]))
            if r["R1"] == r["n_holds"]:
                tallies["k2_empty"] += 1
            elif r["keep_fl"] > r["n_holds"]:
                tallies["k2_exc"] += 1
            else:
                tallies["k2_none"] += 1
            if r["keep_mid"] > r["R1"] - r["n_holds"]:
                tallies["k2_mexc"] += 1
            if r["R1"] > r["n_holds"] and r["d_mid"] == 0:
                tallies["k2_odd"].append((name, m, s, s0, look, r["R1"],
                                          r["n_holds"]))
    print("  %-14s x%d (%d,%d)  c_int %s  c_saf %s  states %d  %s"
          % (name, m, s, s0, fmt(c_int), fmt(c_saf),
             max(r["states"] for r in rows), "  ".join(parts)))


def summarize(tallies, label):
    print("== %s summary" % label)
    print("  K0(a,b) control violations at c_int: %d of %d cells"
          % (tallies["ctrl_bad"], tallies["cells"]))
    print("  K1  losing pairs (c_saf <= c < c_int): %d; with a FLUSHED "
          "direct failure: %d; with none: %d"
          % (tallies["pairs"], tallies["k1_flushed"], len(tallies["k1_none"])))
    for k in tallies["k1_none"]:
        print("      no flushed failure: %s x%d (%d,%d) c=%d  mid-flush %d"
              % k)
    print("  K2  losing pairs by class: R1 entirely flushed %d; a nonzero "
          "excess with the flushed states forgiven %d; neither %d"
          % (tallies["k2_empty"], tallies["k2_exc"], tallies["k2_none"]))
    print("  K2  pairs where an exempt closure exceeds its exempt set: %d; "
          "of them, with the NON-flushed states forgiven (a flushed state "
          "surviving): %d" % (len(tallies["k2_left"]), tallies["k2_mexc"]))
    for k in tallies["k2_left"]:
        print("      %s x%d (%d,%d) c=%d  flushed-exempt %d vs %d  "
              "other-exempt %d vs %d" % k)
    print("  K2b pairs holding a non-flushed state with NO mid-flush direct "
          "failure (KILL): %d" % len(tallies["k2_odd"]))
    for k in tallies["k2_odd"]:
        print("      %s x%d (%d,%d) c=%d  |R1| %d  flushed %d" % k)
    print("  K3  output digits broken by the LARGEST LEGAL reply %d, by a "
          "smaller one only %d" % (tallies["by_cap"], tallies["by_other"]))


def s1_grid():
    print("== s1  the grid: per cell, per lookahead, the direct failures of "
          "R1 as flushed/mid-flush, R1's size and its flushed share; !EXC "
          "marks a LOSING pair whose exempt closure exceeds its exempt "
          "set, the class the summary counts")
    tallies = new_tallies()
    t0 = time.time()
    ctrl_bad = 0
    for name, period in WINDOWS:
        win = window_of(period)
        for m in (2, 3, 4, 5):
            cints = []
            for s, s0 in GRID:
                if (s, s0) == (0, 0):
                    cints.append(None)
                    continue
                hb = h3_bound(win, m, s, s0)
                top = LOOKCAP if hb is None else hb
                c_int, c_saf, rows = read_cell(win, m, s, s0, top)
                cints.append(c_int)
                report(name, m, s, s0, c_int, c_saf, rows, tallies)
            want = PARENT.get((name, m))
            if want is not None:
                got = " ".join(fmt(c) for c in cints)
                ok = got == want
                ctrl_bad += 0 if ok else 1
                print("  K0(c) %s x%d  got '%s'  want '%s'  %s"
                      % (name, m, got, want, "ok" if ok else "BAD"))
    print("  K0(c) parent-row mismatches: %d" % ctrl_bad)
    summarize(tallies, "s1")
    print("  s1 wall %.0f s" % (time.time() - t0))


def s2_band():
    print("== s2  the ten band cells (columns as s1; !EXC as there)")
    tallies = new_tallies()
    t0 = time.time()
    cells = os.environ.get("SEED_CELLS")
    pick = set(int(i) for i in cells.split(",")) if cells else None
    for i, (name, period, m, s, want) in enumerate(BAND):
        if pick is not None and i not in pick:
            continue
        win = window_of(period)
        c_int, c_saf, rows = read_cell(win, m, s, s, LOOKCAP)
        report(name, m, s, s, c_int, c_saf, rows, tallies)
        if c_int != want:
            print("      BAD c_int, the parent froze %d" % want)
    summarize(tallies, "s2")
    print("  s2 wall %.0f s" % (time.time() - t0))


STAGES = {"s1": s1_grid, "s2": s2_band}


def main():
    want = os.environ.get("SEED_STAGES", "s1,s2").split(",")
    for name in want:
        STAGES[name.strip()]()


if __name__ == "__main__":
    main()
