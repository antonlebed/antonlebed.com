"""THE CHARGED RADIUS: what the cure graph's metric does not count.

THE QUESTION
------------
A stall's escape radius is the length of the shortest improving move
sequence out of it, measured through the CURE GRAPH -- a graph whose
nodes are behavioral classes and whose edge s -> t exists as soon as
SOME member of s carries a typed move landing in t
(explore_scale_clock.py build_quotient). None of the typed moves
changes which MEMBER of a class the next move departs from, so a
two-edge class walk s -> z -> t can spend THREE choices: a move out of
some p in s landing on q in z, a RE-SELECTION from q to some other
member r of z, and a move out of r landing in t. The quotient supplies
that re-selection free and the metric never counts it.

At the three squaring-map stalls the freeness is known to be harmless:
the radius-2 escape is two tree freshenings of the stall's OWN member,
with no re-selection spent anywhere on the route
(explore_pinned_composite.py F1, which refuted the opposite claim the
corpus had carried). Every OTHER radius the corpus states -- the ruler
disagreement and the six burst traps -- has never been read this way.

THE OBJECT, and it is a metric and not a cure. The floor theorem
(explore_minimal_cell.py) guarantees a strictly improving TARGET from
every off-bottom finite-loss class, so nothing here can decide whether
a cure exists; it decides how many MOVES a reader spends reaching one
when it may not change identity for free. A radius that grows under
the charge is a statement about the move set.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, cure moves, quotient, the stall
object and the landscape evaluators are the parents'
(explore_scale_clock.py, explore_stall_tie.py,
explore_stall_unresourced.py, explore_stall_assembly.py,
explore_shift_telescope.py). A policy is (st, ss, pt, pc, d): two
route preference bits, tree and chain patience on the axis
0,1,2,3,INF, and the drawdown coordinate. The cure move set is
neighbors_cure: eight single-coordinate steps plus the preference
diagonal. Classes are the counted-trace quotient, the counted window
opening at step 8.

WHOSE VOCABULARY THIS IS WRITTEN IN
-----------------------------------
The QUOTIENT's, not the telescopes'. "Nesting" and "freshening" are
statements about one run's cells against another's; nothing here reads
a cell. The objects are a graph, a walk and a length, and the only
question asked of a class is which policies it holds. TRANSPLANT,
flagged: the squaring-map settlement is an intuition about three
singleton stall classes under one map, and the specimens below include
non-singleton stall classes under the identity and doubling maps at
four resource settings. Nothing about the sq route is assumed here;
those three specimens are re-measured alongside the rest.

THE THREE METRICS
-----------------
Let s0 be a stall class and let BETTER(t) be that landscape's own
strict-improvement test on classes.
  r_class   BFS on the class graph from s0 -- the corpus's published
            metric. Re-selection free at every step.
  r_pure(p) BFS on the POLICY graph from a single member p, along
            typed moves only, to the first policy whose class is
            BETTER. Re-selection forbidden outright.
  r_chg(p)  BFS on the policy graph from p where an edge is either a
            typed move or a jump to another member of the current
            policy's class, both costing one. Re-selection charged.
Each per-member metric is reported at its MIN and its MAX over the
members of s0. The min is the reading where the reader picks its
starting identity free and pays for every later change; the max is
the reading where an adversary picks it.

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
THE ORDERING IS FORCED, and it is what makes the measurement cheap to
read. Project a charged walk onto classes: a typed-move edge projects
to a class edge or to a stay, a re-selection edge projects to a stay.
So every charged walk of length L yields a class walk of length at
most L, giving r_class <= min_p r_chg(p). And a pure walk is a charged
walk that happens to spend no re-selection, so min_p r_chg(p) <=
min_p r_pure(p). The measurement can therefore only move ONE way, and
a single number -- min_p r_chg(p) against r_class -- decides whether
the published metric under-counts.

WHEN THE CHARGE CAN BITE, exactly. Take a shortest class walk
s0 -> z -> t. The edge s0 -> z is witnessed by some p in s0 with a
move landing on q in z; the edge z -> t by some r in z with a move
landing in t. If q = r for some pair of witnesses the charge is free
there. So r_chg exceeds r_class only when at EVERY witnessing pair the
landing member and the departing member differ -- which is possible,
and is what the aim suspects. Two immediate corollaries: a stall class
whose intermediate class z is a SINGLETON cannot pay, since q and r
are then the same policy; and where r_chg does exceed r_class it does
so by at most the number of re-selections a shortest class walk needs,
which for a radius-2 stall is at most one, so the charged radius there
is 2 or 3 and nothing else.

WHAT THE CHARGE CANNOT DO. It cannot unstall a class. Stallhood asks
whether any class-neighbour is better, i.e. whether r_class = 1, and a
walk of length one departs from the START member, whose selection is
free in all three metrics as they are minimised here. So r_class = 1
iff min_p r_pure(p) = 1, and the stall census is metric-independent.
The charge is a statement about routes of length two and more.

THE START IS THE OTHER FREENESS, and it is not the aim's. Minimising
over p hides it; r_pure(p) at its MAX over p reads it. This is asked
of every off-bottom class and not only of the stalls, because for a
NON-stall r_class = 1 by definition while a reader sitting at an
unlucky member may spend more, and the population count of that is a
statement about the whole landscape rather than about ten specimens.

INDEX CONVENTIONS. Nothing here dereferences a trace by step index;
the counted window's start enters only through the parents' signature
construction, unmodified.

THE SPECIMENS, all ten the corpus states a finite radius for
--------------------------------------------------------------
RULER (1): the ruler disagreement, explore_scale_clock.py E6 -- the
  composite (clock-primary) order at (B, W) = (2, 0), a single-policy
  class of route preferences (1,1) at patiences (0,2), rank 3 of 60.
BURST (6): the six designed burst traps, explore_stall_tie.py E4 --
  the forge battery under the lexicographic deficit, spike and
  periodic streams under the identity and doubling maps at four
  resource settings.
SQ (3): the three horizon-cut stalls, explore_stall_assembly.py --
  unresourced, squaring map, explore_shift_telescope.py SQ_SPECIMENS.
  These are the corpus's "three squaring-map stalls" under the other
  name; the two lists are one list, and are re-measured here rather
  than assumed settled.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C0 [positive control, run first] Every specimen reproduces as a stall
   of its parent's landscape, the counts are 1, 6 and 3, and r_class
   is 2 at all ten -- the corpus's published figure. The ruler
   disagreement's class is a singleton and so are the three sq
   classes. A miss is K1 and no verdict below is read.
P1 [the charge, the aim's question] min_p r_chg(p) = r_class = 2 at
   all ten. GUESS: it holds -- the squaring settlement generalises.
P2 [the pure radius] min_p r_pure(p) = 2 at all ten, i.e. no shortest
   route spends a re-selection even when one is available. GUESS: it
   holds at the ruler disagreement and at a majority of the six burst
   traps, and this is a weaker guess than P1's, since P2 can fail
   where P1 holds only if... it cannot: P1 holding with P2 failing is
   exactly the case where re-selection is optional-but-cheaper, which
   the ordering forbids at equal length. Marked as one prediction with
   two readings and scored as two.
P3 [the start, not the route] max_p r_pure(p) > 2 at some specimen
   with a non-singleton stall class. GUESS: yes -- the freeness that
   is load-bearing is the START selection and not mid-route
   re-selection. Vacuous at the four singleton classes, so it is a
   statement about the burst traps alone.
P4 [the population] Over every off-bottom finite-loss class of all ten
   landscapes: r_class is 1 at every non-stall by definition, and the
   guess is that max_p r_pure(p) exceeds r_class at a substantial
   minority of them -- between a tenth and a half. Marked as a guess
   with a wide band because the corpus has never counted this.

KILL CRITERIA (observables; the meaning is weighed after the run)
----------------------------------------------------------------
K1 Any control miss: a specimen that does not reproduce as a stall,
   a count other than 1, 6, 3, or an r_class other than 2. The
   population is not the parents' and nothing below is a verdict.
K2 min_p r_chg(p) > r_class at any specimen. The published metric
   under-counts there; the rig prints the shortest class walk, the
   witnessing members at each end of each edge, and the charged walk.
K3 max_p r_pure(p) = min_p r_pure(p) at every specimen with a
   non-singleton stall class. Start selection is not load-bearing
   either and the class metric is exact at every reading.
K4 Any specimen where the three metrics disagree in a direction the
   hand-attack's ordering forbids. The rig has a bug and prints the
   walks rather than a verdict.

ENGINE
------
E0 the controls (C0): rebuild each parent landscape, reproduce the
   stall counts and the published radii.
E1 the three metrics at the ten specimens (P1, P2, P3).
E2 the anatomy of any specimen where the charge bites (K2), and of
   the widest max-min spread otherwise.
E3 the population sweep over every off-bottom finite-loss class of
   the ten landscapes (P4).
Exact integer and Fraction arithmetic for every verdict; floating
point only in printed logs. Sequential; estimated run a few minutes,
the burst forge the driver; memory trivial (no BLAS import); exit
nonzero on any check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, 12.5 s,
26.8 MB peak under the memory watch)
----------------------------------------------------------------
F1 THE PUBLISHED RADIUS IS NOT MEMBER-REALISABLE, AT ONE STALL OF
   TEN, AND THE KILL-SHAPE MISSES. K2 fires exactly once: the burst
   trap on the spike1@6 stream under the doubling map at horizon 120,
   (B, W) = (2, 0). Its class radius is 2, its charged radius 3 and
   its pure radius 3. The stall class is the singleton sigma = (1,1)
   at patiences (0,3); exactly one class supports a length-2 walk out
   of it, a class of ten policies, and that class's LANDING set --
   the 3 policies a typed move out of the stall reaches -- is
   DISJOINT from its DEPARTURE set -- the 2 policies carrying a typed
   move to a strictly better class. So the length-2 class walk exists
   and no reader realises it in two moves. The other nine specimens
   are unchanged at 2 under both charges. What survives is the
   distinction: "escape radius exactly 2" is true of the CURE GRAPH
   at all ten and false as a MOVE COUNT at one, and the corpus stated
   it in the second reading.
F2 THE FREENESS BUYS NOTHING AT THAT STALL EITHER. Charged and pure
   agree at 3 there, so the route the quotient's free re-selection
   would supply is not shorter than the route that spends none: one
   re-selection plus two moves is three, and three typed moves reach
   a better class directly. Re-selection is a way of paying, never a
   discount, at every one of the ten.
F3 START SELECTION IS NOT LOAD-BEARING AT ANY STALL. K3 fires. The
   three non-singleton stall classes all have size 2 and all have
   pure_hi = pure_lo, so an adversary choosing the starting member
   costs nothing anywhere in the stall corpus. P3 is wrong, and it
   was the prediction this rig was most confident of.
F4 THE FREENESS IS REAL AND IT LIVES OFF THE STALLS. Over all 545
   off-bottom finite-loss classes of the ten landscapes the
   per-member pure radius spreads at 7 of them, 1.3% -- P4's guessed
   band of a tenth to a half is wrong by an order of magnitude. None
   of the seven is a stall; every one has class radius 1 and a
   membership of ten to twenty policies, and they sit near the
   bottom. There the spread is wide: the census-2313 landscape's
   rank-1 class of 16 policies carries pure radii 1, 2, 3 and 4 while
   its class radius is 1. And at four of the seven the charge
   strictly HELPS: that class's charged radii are 1, 2, 2, 2, the
   rank-4 class of census-3212 goes 1,2,3 pure against 1,2,2 charged,
   and both spike1@10 classes go to a pure maximum of 3 against a
   charged maximum of 2. So the quotient's free re-selection is worth
   up to two moves, and it is worth them to the UNLUCKY member and
   never to the best one -- a mechanism for catching up, which is why
   minimising over the start member hides it completely.
F5 THE TWO-MOVE THEOREM IS NOT CONTACTED. The K2 stall holds no
   member with both patiences finite and positive -- 0 of 1, its tree
   patience being 0 -- so it sits outside the shift telescope's frame
   exactly as the three squaring-map stalls do. The one specimen
   where the published radius fails as a move count is one the proved
   cure never reached.
F6 THE THREE HORIZON-CUT STALLS AND THE THREE SQUARING-MAP STALLS ARE
   ONE LIST OF THREE. explore_shift_telescope.py SQ_SPECIMENS is the
   assembly rig's two census stalls at horizon 12 and its designed
   stall at horizon 16, all under the squaring map, which is what the
   corpus names the horizon-cut stalls. The population left unread
   before this rig was therefore seven stalls and not ten; the other
   three were settled already. Both names are kept because both
   are load-bearing -- one names the mechanism, the other the map --
   but they are not two populations.

THE VERDICT. The kill-shape -- every radius unchanged -- MISSES, by
one specimen of ten. The cure graph's metric under-counts a reader's
moves where a class walk's consecutive edges are witnessed by
disjoint member sets, that happens at one stall in the corpus, and
the re-selection the metric supplies free is not what closes the gap
there: nothing closes it, and the honest move count is 3. Off the
stalls the same freeness is a real discount of up to two moves to the
members that need it, at 1.3% of the off-bottom population.

Run record. The first run (E0-E3) exited 0 in 12.3 s with all checks
passing and K2 firing once. E4 was added after it, no prediction band
touched: E3's tally had come in at almost exactly one spreading class
per landscape, a number that wants its members named before it is
read as a rate, and it folded any member with nothing reachable
inside the BFS cap in with the genuine spreads -- E4 names every
spreading class and reports that count separately, and it is zero.
The same edit added the two-move theorem's hypothesis check to E2
(F5) and put the world column into E3 and E4, which had been printing
two distinct landscapes under one label. Final run 12.5 s, 26.8 MB
peak, ALL CHECKS PASS, exit 0.
"""

import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import explore_scale_clock as SC
import explore_stall_tie as ST
import explore_stall_assembly as SA
import explore_shift_telescope as TS

FAILURES = []


def check(name, ok, detail=""):
    print("  [%s] %s%s" % ("ok" if ok else "FAIL", name,
                           ("  " + detail) if detail else ""))
    if not ok:
        FAILURES.append(name)
    return ok


# ----------------------------------------------------------------- #
# the three metrics
# ----------------------------------------------------------------- #

CAP = 8


def r_class(s0, nbrs, better):
    """Fewest cure-graph edges from class s0 to a BETTER class."""
    seen, front = {s0}, [s0]
    for depth in range(1, CAP + 1):
        nxt = []
        for s in front:
            for t in nbrs[s]:
                if better(t):
                    return depth
                if t not in seen:
                    seen.add(t)
                    nxt.append(t)
        if not nxt:
            return None
        front = nxt
    return None


def r_member(p0, sig_of, nbr_fn, better, charged):
    """Fewest moves from the single policy p0 to a policy whose class
    is BETTER. Typed moves always; re-selection inside the current
    class as an extra unit-cost edge when charged."""
    seen, front = {p0}, [p0]
    for depth in range(1, CAP + 1):
        nxt = []
        for p in front:
            outs = list(nbr_fn(p))
            if charged:
                outs += [q for q in members_of[sig_of[p]] if q != p]
            for q in outs:
                if q not in sig_of:
                    continue
                if better(sig_of[q]):
                    return depth
                if q not in seen:
                    seen.add(q)
                    nxt.append(q)
        if not nxt:
            return None
        front = nxt
    return None


members_of = {}


def metrics(s0, mem, nbrs, nbr_fn, better):
    """(r_class, pure_min, pure_max, chg_min, chg_max, class size)."""
    global members_of
    members_of = mem
    sig_of = {p: s for s, ps in mem.items() for p in ps}
    rc = r_class(s0, nbrs, better)
    pure = [r_member(p, sig_of, nbr_fn, better, False) for p in mem[s0]]
    chg = [r_member(p, sig_of, nbr_fn, better, True) for p in mem[s0]]

    def lo(vals):
        fin = [v for v in vals if v is not None]
        return min(fin) if fin else None

    def hi(vals):
        return None if any(v is None for v in vals) else max(vals)

    return (rc, lo(pure), hi(pure), lo(chg), hi(chg), len(mem[s0]))


def fmt(v):
    return "-" if v is None else str(v)


# ----------------------------------------------------------------- #
# the specimens
# ----------------------------------------------------------------- #

def ruler_landscape():
    """The ruler disagreement's landscape: composite (clock-primary)
    order at (B, W) = (2, 0), rebuilt exactly as
    explore_scale_clock.py E6 builds it."""
    imgs = SC.build_images(SC.N_MAIN)
    jlens = {row: SC.j_length_pairs(imgs[row]) for row in SC.ROWS}
    B, W = 2, 0
    space, tab, sigd, lagd = SC.setting_tables(imgs, jlens, B, W)
    daxis = SC.d_axis(W)
    sig8 = {p: tuple(sigd[(p, r)] for r in SC.ROWS8) for p in space}
    loss8 = {}
    for p in space:
        s = sig8[p]
        if s not in loss8:
            loss8[s] = (sum(lagd[(p, r)] for r in SC.ROWS8),
                        SC.agg([tab[(p, r)] for r in SC.ROWS8]))
    nbr_fn = lambda p: SC.neighbors_cure(p, SC.AX_BASE, daxis)
    mem, nbrs, _key = SC.build_quotient(space, sig8, nbr_fn)
    qranks = SC.qrank_map(mem, loss8)
    stalls = SC.qstalls(mem, qranks, nbrs)
    return [("ruler-disagreement", "id+dbl rows", "(B,W)=(2,0)",
             mem, nbrs, nbr_fn, qranks, stalls)]


def burst_landscapes():
    """The six burst traps, from the forge battery of
    explore_stall_tie.py E4."""
    specimens, _ties = ST.e4_forge()
    out = []
    for (wname, mp, horizon, B, W, s, mem, nbrs,
         qloss, qranks, _cbs) in specimens:
        daxis = SC.d_axis(W) if B is not None else [SC.INF_D]
        nbr_fn = lambda p, d=daxis: SC.neighbors_cure(p, SC.AX_BASE, d)
        out.append(("burst/%s" % wname, "%s h=%d" % (mp, horizon),
                    "(B,W)=(%s,%s)" % (B, W), mem, nbrs, nbr_fn,
                    qranks, [s]))
    return out


def sq_landscapes():
    """The three horizon-cut stalls, unresourced under sq."""
    out = []
    for tag, digs, horizon in TS.SQ_SPECIMENS:
        ev = SA.evaluate(list(digs), "sq", horizon)
        nbr_fn = lambda p: SC.neighbors_cure(p, SC.AX_BASE, [SC.INF_D])
        out.append(("horizon-cut/%s" % tag, "sq h=%d" % horizon,
                    "unresourced", ev["mem"], ev["nbrs"], nbr_fn,
                    ev["qranks"], list(ev["stalls"])))
    return out


# ----------------------------------------------------------------- #
# E0-E3
# ----------------------------------------------------------------- #

def e0_controls(fams):
    print("\nE0  CONTROLS: the ten specimens and their published radii")
    counts = {}
    for family, rows in fams:
        n = sum(len(r[7]) for r in rows)
        counts[family] = n
    check("ruler disagreement: 1 stall class",
          counts.get("RULER") == 1, "got %s" % counts.get("RULER"))
    check("burst traps: 6 stall specimens",
          counts.get("BURST") == 6, "got %s" % counts.get("BURST"))
    check("horizon-cut stalls: 3 stall classes",
          counts.get("SQ") == 3, "got %s" % counts.get("SQ"))
    bad = []
    for _family, rows in fams:
        for (name, world, setting, mem, nbrs, nbr_fn,
             qranks, stalls) in rows:
            for s0 in stalls:
                better = lambda t, s=s0: qranks[t] < qranks[s]
                rc = r_class(s0, nbrs, better)
                if rc != 2:
                    bad.append((name, rc))
    check("published escape radius is 2 at all ten",
          not bad, "misses %s" % (bad,))


def e1_metrics(fams):
    print("\nE1  THE THREE METRICS at the ten specimens")
    print("    %-28s %-12s %-14s %5s %4s  %-9s %-9s"
          % ("specimen", "world", "setting", "|s0|", "cls",
             "pure lo/hi", "chg lo/hi"))
    rows_out = []
    for _family, rows in fams:
        for (name, world, setting, mem, nbrs, nbr_fn,
             qranks, stalls) in rows:
            for s0 in stalls:
                better = lambda t, s=s0: qranks[t] < qranks[s]
                rc, plo, phi, clo, chi, sz = metrics(
                    s0, mem, nbrs, nbr_fn, better)
                print("    %-28s %-12s %-14s %5d %4s  %-9s %-9s"
                      % (name, world, setting, sz, fmt(rc),
                         "%s/%s" % (fmt(plo), fmt(phi)),
                         "%s/%s" % (fmt(clo), fmt(chi))))
                rows_out.append((name, world, setting, s0, mem, nbrs,
                                 nbr_fn, qranks, rc, plo, phi, clo,
                                 chi, sz))
    k2 = [r for r in rows_out if r[11] is not None and r[8] is not None
          and r[11] > r[8]]
    k4 = [r for r in rows_out
          if not (r[8] is not None and r[11] is not None
                  and r[9] is not None
                  and r[8] <= r[11] <= r[9])]
    check("K4 clear: r_class <= chg_lo <= pure_lo everywhere",
          not k4, "violations %s" % [r[0] for r in k4])
    print("\n  K2 (the charge bites): %d of %d specimens"
          % (len(k2), len(rows_out)))
    nonsingle = [r for r in rows_out if r[13] > 1]
    spread = [r for r in nonsingle if r[10] is not None
              and r[9] is not None and r[10] > r[9]]
    print("  P3 (start selection is load-bearing): %d of %d "
          "non-singleton stall classes carry pure_hi > pure_lo"
          % (len(spread), len(nonsingle)))
    return rows_out, k2, spread


def e2_anatomy(rows_out, k2, spread):
    print("\nE2  ANATOMY")
    picks = k2 if k2 else spread
    if not picks:
        print("  no specimen where the charge bites and none where "
              "start selection costs; nothing to dissect.")
        return
    for r in picks[:3]:
        (name, world, setting, s0, mem, nbrs, nbr_fn, qranks,
         rc, plo, phi, clo, chi, sz) = r
        print("\n  %s (%s, %s): r_class %s | pure %s/%s | chg %s/%s"
              % (name, world, setting, fmt(rc), fmt(plo), fmt(phi),
                 fmt(clo), fmt(chi)))
        sig_of = {p: s for s, ps in mem.items() for p in ps}
        print("    stall members: %s"
              % "; ".join(SC.fmt_pol5(p)
                          for p in sorted(mem[s0], key=SC.pol_key)))
        telescoped = [p for p in mem[s0]
                      if p[2] not in (0, SC.INF_P)
                      and p[3] not in (0, SC.INF_P)]
        print("    members with both patiences finite and positive "
              "(the two-move theorem's hypothesis): %d of %d"
              % (len(telescoped), len(mem[s0])))
        for p in sorted(mem[s0], key=SC.pol_key):
            global members_of
            members_of = mem
            better = lambda t: qranks[t] < qranks[s0]
            rp = r_member(p, sig_of, nbr_fn, better, False)
            rg = r_member(p, sig_of, nbr_fn, better, True)
            print("      from %s: pure %s, charged %s"
                  % (SC.fmt_pol5(p), fmt(rp), fmt(rg)))
        # the intermediate classes on a shortest class walk
        for t in sorted(nbrs[s0], key=lambda t: qranks[t]):
            if qranks[t] < qranks[s0]:
                continue
            exits = [u for u in nbrs[t] if qranks[u] < qranks[s0]]
            if not exits:
                continue
            landing = set()
            for p in mem[s0]:
                for q in nbr_fn(p):
                    if q in sig_of and sig_of[q] == t:
                        landing.add(q)
            departing = set()
            for q in mem[t]:
                for u in nbr_fn(q):
                    if u in sig_of and qranks[sig_of[u]] < qranks[s0]:
                        departing.add(q)
            print("      via class %s (size %d): landings %d, "
                  "departures %d, shared %d"
                  % (SC.summarize_class(mem[t]), len(mem[t]),
                     len(landing), len(departing),
                     len(landing & departing)))


def e3_population(fams):
    print("\nE3  POPULATION: every off-bottom finite-loss class of the "
          "ten landscapes")
    print("    %-28s %-12s %6s %6s %6s %6s"
          % ("landscape", "world", "cls", "offbot", "hi>lo", "hi>=3"))
    tot = off = wider = deep = 0
    for _family, rows in fams:
        seen_world = set()
        for (name, world, setting, mem, nbrs, nbr_fn,
             qranks, stalls) in rows:
            key = (world, setting, len(mem))
            if key in seen_world:
                continue
            seen_world.add(key)
            sig_of = {p: s for s, ps in mem.items() for p in ps}
            global members_of
            members_of = mem
            n_off = n_wider = n_deep = 0
            for s in mem:
                if qranks[s] == 0:
                    continue
                better = lambda t, ss=s: qranks[t] < qranks[ss]
                vals = [r_member(p, sig_of, nbr_fn, better, False)
                        for p in mem[s]]
                fin = [v for v in vals if v is not None]
                if not fin:
                    continue
                n_off += 1
                lo = min(fin)
                hi = None if any(v is None for v in vals) else max(vals)
                if hi is None or hi > lo:
                    n_wider += 1
                if hi is None or hi >= 3:
                    n_deep += 1
            print("    %-28s %-12s %6d %6d %6d %6d"
                  % (name, world, len(mem), n_off, n_wider, n_deep))
            tot += len(mem)
            off += n_off
            wider += n_wider
            deep += n_deep
    print("    %-28s %-12s %6d %6d %6d %6d"
          % ("TOTAL", "", tot, off, wider, deep))
    if off:
        print("  P4: pure_hi > pure_lo at %d of %d off-bottom "
              "finite-loss classes (%.1f%%)"
              % (wider, off, 100.0 * wider / off))


def e4_widest(fams):
    """Added after the first run; no prediction band touched. E3
    counted the classes whose per-member pure radius spreads, and the
    count came in at one per landscape almost exactly -- a number that
    wants its members named before it is read as a rate. This prints
    every spreading class with its own numbers, and separately the
    count of members from which NOTHING better is reachable inside the
    BFS cap, which E3's tally folded in with the spreads."""
    print("\nE4  THE SPREADING CLASSES, named")
    unreachable = 0
    for _family, rows in fams:
        seen_world = set()
        for (name, world, setting, mem, nbrs, nbr_fn,
             qranks, stalls) in rows:
            key = (world, setting, len(mem))
            if key in seen_world:
                continue
            seen_world.add(key)
            sig_of = {p: s for s, ps in mem.items() for p in ps}
            global members_of
            members_of = mem
            for s in sorted(mem, key=lambda s: qranks[s]):
                if qranks[s] == 0:
                    continue
                better = lambda t, ss=s: qranks[t] < qranks[ss]
                vals = [r_member(p, sig_of, nbr_fn, better, False)
                        for p in mem[s]]
                cvals = [r_member(p, sig_of, nbr_fn, better, True)
                         for p in mem[s]]
                fin = [v for v in vals if v is not None]
                if not fin:
                    continue
                unreachable += sum(1 for v in vals if v is None)
                if all(v is not None for v in vals) and \
                        max(vals) == min(vals):
                    continue
                print("    %s / %s / %s: class %s (rank %d, "
                      "size %d)"
                      % (name, world, setting,
                         SC.summarize_class(mem[s]),
                         qranks[s], len(mem[s])))
                print("      r_class %s | pure %s | charged %s | "
                      "stall %s"
                      % (fmt(r_class(s, nbrs, better)),
                         ",".join(fmt(v) for v in vals),
                         ",".join(fmt(v) for v in cvals),
                         s in stalls))
    print("    members with nothing better inside the cap (%d): %d"
          % (CAP, unreachable))


def main():
    print("THE CHARGED RADIUS: what the cure graph's metric "
          "does not count")
    print("=" * 70)
    fams = [("RULER", ruler_landscape()),
            ("BURST", burst_landscapes()),
            ("SQ", sq_landscapes())]
    e0_controls(fams)
    if FAILURES:
        print("\nCONTROLS FAILED - no verdicts.")
        sys.exit(1)
    rows_out, k2, spread = e1_metrics(fams)
    e2_anatomy(rows_out, k2, spread)
    e3_population(fams)
    e4_widest(fams)
    print("\nVERDICT OBSERVABLES")
    print("  K2 specimens (charged radius above published): %d"
          % len(k2))
    print("  K3 fires (no non-singleton spread): %s"
          % (not spread))
    if FAILURES:
        print("\nFAILURES: %s" % FAILURES)
        sys.exit(1)
    print("\nALL CHECKS PASS")


if __name__ == "__main__":
    main()
