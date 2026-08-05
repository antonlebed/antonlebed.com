"""THE MAP-RATE QUESTION: does the horizon-cut stall need a fast
map, or only a bigger design space?

THE QUESTION
------------
Every horizon-cut stall found to date lives under the sq map: the
assembly forge (explore_stall_assembly.py) found the two census
stalls and its designed specimen under sq, while its id and dbl
climbs all ended at negative local maxima (best -0.7388 ln at
horizon 12, -1.0997 at 16). But that forge searched digits 1..6 at
horizons 12 and 16 only, so two explanations are live:
  (a) DESIGN-SPACE CAP - a slow map can buy per-step shrink through
      LARGE DIGITS, and the old digit cap simply priced the burst
      amplitude a slow-map stall needs out of the search space;
  (b) MAP-RATE THRESHOLD - the late collection needs the map's own
      shrink rate to grow along the window, which no digit choice
      supplies, and the refusal survives any widening.
This rig widens both axes - digits to 64, horizons to 10..20 - and
forges under id and dbl alone. A slow-map witness makes the species
map-free; a refusal at the widened scope strengthens the threshold
reading and names the shrink-rate derivation as the target.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, moves, quotient, the stall object,
the stall margin, the margin detector and the first-improvement
climb are the parents' (explore_scale_clock.py,
explore_stall_tie.py, explore_stall_unresourced.py,
explore_stall_assembly.py). UNRESOURCED throughout: delta inert,
100 policies, N0 = 8 counted start. The climb is the assembly
forge's first-improvement hill-climb with the digit set a
parameter instead of that rig's fixed 1..6.

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
L1 (AMPLITUDE IS MAP-FREE, COMPOUNDING IS NOT). One CF digit a
   shrinks the cylinder by a factor of order a^2 in a single step -
   an instrument every map applies verbatim, worth ~2 ln a of
   one-step collection, capped at ~3.6 ln by the old forge's digit
   ceiling of 6 and at ~8.3 ln by this rig's 64. What no digit
   buys is COMPOUNDING: under sq the ln-width of every image
   doubles each step regardless of the stream, so the gap a frozen
   neighbor concedes GROWS along the collection window for free,
   while under id it is the stream's own digits that must pay for
   every step of gap. So the two explanations separate exactly
   here: if the stall's collection only needs a large enough
   one-step gap held for a few steps, wide digits under id should
   assemble it; if it needs the gap to grow along the window, no
   digit widening helps.
L2 (dbl ADDS ALIGNMENT, NEVER RATE). dbl doubles endpoint
   numerators - a fixed scalar on id's images - so at the same
   stream its ln-widths equal id's plus ln 2, step for step: no
   acceleration anywhere. It differs from id only in where the
   images LAND on the fixed mediant-straddle cover, so it probes
   grid alignment at slow rate, not a second rate class.
L3 (WHAT DECIDES IS THE FREEZE DURATION). The trade's mechanism is
   the neighbor frozen on its own subdivision point while the
   reference dives (the trade rig's anatomy). If the freeze
   persists under a slow map once a burst digit has separated the
   cells - freeze bounded by patience mechanics, not by the map -
   then amplitude suffices and (a) wins; if the neighbor refines
   through unless the reference keeps OUTRUNNING it, only a
   growing rate holds the freeze and (b) wins. The forge measures
   which without needing the mechanism resolved on paper.
L4 (THE BURST BATTERY IS L1 MADE CONCRETE). Before any climb, the
   census leg carries designed burst worlds - an all-1 base with
   single and twin giant digits (8..64) placed inside the counted
   window near the cut - so the amplitude route is MEASURED
   directly per (horizon, map) cell even if every climb stalls in
   a local maximum elsewhere.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C1 [controls, gate]
   (i)  The evaluator reproduces the assembly rig's two census
        stalls (231313131313 and 321212121212, sq, horizon 12) as
        strict stalls with best margins in the printed bands
        (+0.17..+0.19 and +0.47..+0.49 ln).
   (ii) It reproduces the designed stall (3116131111111116, sq,
        horizon 16) strict with best margin in +0.27..+0.29 ln.
C2 [THE WIDENED CENSUS - the amplitude probe] Unresourced, maps id
   and dbl, horizons 10/12/14/16/20, over the parents' pools plus
   the burst battery and the all-1 head-3 seed: per-cell best
   margins and any census stalls. GUESS, marked as such: the burst
   battery moves the best id/dbl margin above the old plateau
   (best margin somewhere > -0.73 ln) - amplitude is at least the
   binding axis the old cap suggests.
C3 [THE WIDENED FORGE - the open observable] From the top seeds
   per cell, the parents' first-improvement climb over digits
   {1,2,3,4,6,8,12,16,24,32,48,64}, one global evaluation budget.
   GUESS, marked as such: a slow-map stall PRINTS - predicted
   locus a giant-digit burst world with the horizon cutting inside
   its window, single-policy class at pt + pc >= 2 - the amplitude
   route landing where the capped forge could not reach. The
   counterweight is named: the old forge's id/dbl climbs
   plateaued well below zero, and F5's observation that only sq's
   squared shrink amplified deep enough at that scope weighs
   toward refusal.
C4 [the cure] Any specimen found has escape radius exactly 2
   through the cure graph (the corpus's standing radius-2
   reading).

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 Any C1 check fails: the rig is dead, no verdicts.
K2 A stall prints under id or dbl (census or forge): the map-rate
   question settles MAP-FREE - the full anatomy prints (digits,
   map, horizon, class, per-neighbor margins, counted profiles),
   capped at three specimens, one hand-verified post-run.
K3 The forge exhausts at the widened scope with zero id/dbl
   stalls: the best margin per cell prints beside the digit and
   horizon that achieved it - the adversarial room measured, the
   threshold reading strengthened, the shrink-rate derivation the
   named target.

ENGINE
------
E1 controls: the three sq specimen reproductions (C1).
E2 the widened census (C2): per (horizon, map) cell over the
   parents' pools + the burst battery + head-3; margins, stalls,
   top seeds carried to E3.
E3 the widened forge (C3): first-improvement climbs, digit set
   WIDE_DIGITS, one global budget (40,000 evaluations, logged if
   hit); on a stall the cell's question is answered and the forge
   moves to the next cell.
E4 escape radius of every specimen (C4).
E5 the short-horizon frontier (added after the first run, no
   prediction band touched: the first run's E3 printed a local
   maximum at -0.0078 ln at horizon 10 under dbl - within one
   hundredth of stalling - with margins receding as the horizon
   grows, so the shortest horizons are where the question is
   decided and horizon 9 was never scanned): census plus climbs
   at horizons 9/10/11 under id and dbl, digit set widened to
   256, its own evaluation budget.
Exact big-integer arithmetic for every verdict (the parents'
comparators); ln only in printed logs. Sequential, one landscape
at a time; estimated run five to ten minutes (id/dbl integers
stay small; the budgets are the driver), memory trivial (no BLAS
import); positive controls gate all verdicts; exit nonzero on any
check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, ~9 min,
memory trivial)
----------------------------------------------------------------
F1 Controls exact. All three sq specimens reproduce strict with
   best margins +0.1815, +0.4775 and +0.2839 ln, each inside its
   band.

F2 THE WIDENED CENSUS REFUSES: zero stalls in 2,108 id/dbl
   landscapes at horizons 10-20 (the parents' pools plus the
   burst battery to digit 64), and zero more in the frontier
   census at horizons 9-11. The amplitude instrument works but
   never crosses: burst worlds top two census cells (burst7.D64
   at -0.4288 ln, h=10 id; burst9.D64 at -0.6989, h=12 dbl), so
   C2's guess paid - the best id/dbl margin rises above the old
   -0.73 plateau - yet every cell stays negative.

F3 THE FRONTIER: SUPREMUM ZERO, NOT ATTAINED, AT RATE 1/D. The
   forge's best margins at the shortest horizons sit within
   thousandths of stalling and scale inversely with the digit
   cap D: at h=10 dbl the same climb shape gives -0.007752 ln at
   D = 64 and -0.001949 at D = 256 - a factor 3.98 for a x4
   widening - and at h=9 the D = 256 climbs end at -0.0039 (id)
   and -0.0019 (dbl). Hand-check from the exact loss triples
   (the margins are ratios of exact rationals): the binding-edge
   ratios are 33538/33799 (h=10 dbl, D=64, ln = -0.007752),
   527362/528391 (h=10 dbl, D=256), 16973823/17040128 (h=9 id,
   D=256) - each within ~1 part in 10^4 of a one-cell ratio like
   128/129 or 256/257 but NOT equal to it, so the near-miss is
   structural, not a single clean identity. The adversarial
   optimum under a slow map approaches zero from below as the
   design space widens and never reaches it at any scanned
   scope.

F4 THE HORIZON SLOPE. Away from the frontier the deficit grows
   with the count: the id climbs land at -0.41, -1.11, -1.87,
   -2.64 ln at horizons 10/12/14/16 (each pair of added counted
   steps costs ~0.70-0.77 ln), and the dbl climbs sit shallower
   and can pin (-1.0986 at both h=14 and h=16, the same world
   prefix winning both cells). A slow map pays for every counted
   step of gap out of the stream's own digits; sq's compounding
   is what removes that bill.

F5 SCOPE CAPS, named: the E3 budget (40,000) exhausted before
   the h=20 id climbs ran (census only there: -4.2656), and the
   E5 budget (30,000) before the h=11 id climbs (census only:
   -0.4652). Both are the cells farthest from zero in their legs.
   E4 is vacuous - no specimen exists to measure a radius on -
   so C4 goes untested.

THE VERDICT. K3 - the widened design space still refuses:
observation (adversarial search at stated scope, exact
arithmetic). No unresourced id/dbl stall exists at digits to 256
and horizons 9-20 across 2,764 distinct census landscapes (3,086
runs; E5 re-censuses the h=10 cells) and 70,000 forge
evaluations, while the same detector reproduces all three sq
specimens. The map-rate threshold reading strengthens with a
measured shape: a slow map's best stall margin walks to zero
like 1/(digit cap) and never crosses, so the named target is
the derivation - a proof that a rate-preserving map bounds the
late collection strictly below the divergence bill, with the
1/D approach as the bound's own asymptotic.

Run record. The first run (E1-E4) exited 0 in ~4 min: K3 at
horizons 10-20 with the h=10 dbl climb printing -0.0078 ln,
within one hundredth of stalling. E5 (the short-horizon
frontier) added because that near-miss made horizons 9-11 the
deciding cells; no prediction band touched. Final run ~9 min,
both budgets fully spent, ALL CHECKS PASS, exit 0.
"""

import sys

import explore_scale_clock as SC
import explore_stall_tie as ST
import explore_stall_unresourced as SU
import explore_stall_assembly as SA

FAILURES = []

def check(name, ok):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s" % (tag, name))
    if not ok:
        FAILURES.append(name)

# ----------------------------------------------------------------- #
# E1: controls - the three sq specimens reproduced
# ----------------------------------------------------------------- #

CONTROLS = (
    ("census flagship-lite", "231313131313", "sq", 12, 0.17, 0.19),
    ("census flagship", "321212121212", "sq", 12, 0.47, 0.49),
    ("designed h16", "3116131111111116", "sq", 16, 0.27, 0.29),
)

def e1_controls():
    print("\nE1  CONTROLS (the assembly rig's sq specimens)")
    for tag, digstr, mp, h, lo, hi in CONTROLS:
        digs = [int(c) for c in digstr]
        ev = SA.evaluate(digs, mp, h)
        strict = all(ev["marg"][s][2] for s in ev["stalls"]
                     if s in ev["marg"])
        ok = (len(ev["stalls"]) >= 1 and strict
              and ev["best_m"] is not None
              and lo <= ev["best_m"] <= hi)
        if ev["best_m"] is not None:
            print("  %s: %d stall(s), best margin %+.4f ln"
                  % (tag, len(ev["stalls"]), ev["best_m"]))
        check("C1 %s strict in band %+.2f..%+.2f" % (tag, lo, hi), ok)

# ----------------------------------------------------------------- #
# E2: the widened census
# ----------------------------------------------------------------- #

FORGE_MAPS = ("id", "dbl")
FORGE_HORIZONS = (10, 12, 14, 16, 20)
WIDE_DIGITS = (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64)
SEED_K = 3

def burst_battery(horizon):
    """L4: all-1 base, single and twin giant digits inside the
    counted window near the cut."""
    worlds = []
    base = [1] * horizon
    for D in (8, 16, 32, 64):
        for j in range(SC.N0 - 1, horizon - 1):
            digs = list(base)
            digs[j] = D
            worlds.append(("burst%d.D%d" % (j, D), digs))
    for D in (16, 64):
        for g in (1, 2):
            for j in range(SC.N0 - 1, horizon - 1 - g):
                digs = list(base)
                digs[j] = D
                digs[j + g] = D
                worlds.append(("btwin%d+%d.D%d" % (j, g, D), digs))
    return worlds

def census_pool(horizon):
    pool = []
    seen = set()
    cand = (SU.density_pool(horizon) + SU.aimed_worlds(horizon)
            + ST.battery_worlds() + burst_battery(horizon)
            + [("head3", [3] + [1] * (horizon - 1))])
    for wname, digs in cand:
        key = tuple(digs[:horizon])
        if key in seen or len(digs) < horizon:
            continue
        seen.add(key)
        pool.append((wname, list(key)))
    return pool

def e2_census():
    print("\nE2  THE WIDENED CENSUS (unresourced, id/dbl)")
    seeds = {}
    n_land = 0
    stall_hits = []
    for horizon in FORGE_HORIZONS:
        pool = census_pool(horizon)
        for mp in FORGE_MAPS:
            cell = []
            for wname, digs in pool:
                ev = SA.evaluate(digs, mp, horizon)
                n_land += 1
                if ev["stalls"]:
                    stall_hits.append((wname, digs, mp, horizon, ev))
                if ev["best_m"] is not None:
                    cell.append((ev["best_m"], wname, digs))
            cell.sort(key=lambda z: (-z[0], z[1]))
            seeds[(horizon, mp)] = [(w, d) for _m, w, d
                                    in cell[:SEED_K]]
            print("  h=%-2d %-3s: %d worlds, best margin %+.4f ln "
                  "(%s)" % (horizon, mp, len(cell),
                            cell[0][0], cell[0][1]))
    print("  landscapes %d | census stalls %d"
          % (n_land, len(stall_hits)))
    return seeds, stall_hits

# ----------------------------------------------------------------- #
# E3: the widened forge
# ----------------------------------------------------------------- #

EVAL_CAP = 40000
MAX_ACCEPTS = 60

def climb(digs0, mp, horizon, budget, digits):
    """The assembly forge's first-improvement hill-climb on the
    best stall margin, digit set parameterized."""
    cur = list(digs0)
    ev = SA.evaluate(cur, mp, horizon)
    budget[0] -= 1
    if ev["stalls"]:
        return ev["best_m"], cur, ev, 0
    accepts = 0
    while accepts < MAX_ACCEPTS and budget[0] > 0:
        improved = False
        for pos in range(horizon):
            for d in digits:
                if d == cur[pos]:
                    continue
                cand = cur[:]
                cand[pos] = d
                ev2 = SA.evaluate(cand, mp, horizon)
                budget[0] -= 1
                if ev2["stalls"]:
                    return ev2["best_m"], cand, ev2, accepts
                if (ev2["best_m"] is not None
                        and (ev["best_m"] is None
                             or ev2["best_m"] > ev["best_m"])):
                    cur, ev = cand, ev2
                    improved = True
                    break
                if budget[0] <= 0:
                    break
            if improved or budget[0] <= 0:
                break
        if not improved:
            break
        accepts += 1
    return ev["best_m"], cur, None, accepts

def e3_forge(seeds):
    print("\nE3  THE WIDENED FORGE (digits %s)"
          % ",".join(str(d) for d in WIDE_DIGITS))
    budget = [EVAL_CAP]
    specimens = []
    cell_best = {}
    for (horizon, mp), cell in sorted(seeds.items()):
        for wname, digs in cell:
            if budget[0] <= 0:
                break
            m, d, spec, acc = climb(digs, mp, horizon, budget,
                                    WIDE_DIGITS)
            tag = "seed %s/%s h=%d" % (wname, mp, horizon)
            if spec is not None:
                specimens.append((d, mp, horizon, spec))
                print("  %s: STALL after %d accepts" % (tag, acc))
                break  # next cell: this cell's question is answered
            print("  %s: local max margin %+.4f ln after %d accepts"
                  % (tag, m, acc))
            key = (horizon, mp)
            if m is not None and (key not in cell_best
                                  or m > cell_best[key][0]):
                cell_best[key] = (m, d, wname)
        if budget[0] <= 0:
            break
    if budget[0] <= 0:
        print("  NOTE: evaluation budget (%d) exhausted - climbs "
              "beyond it were dropped" % EVAL_CAP)
    print("  evaluations spent %d of %d"
          % (EVAL_CAP - budget[0], EVAL_CAP))
    return specimens, cell_best

# ----------------------------------------------------------------- #
# E5: the short-horizon frontier (added after the first run, no
# prediction band touched: the first run's forge reached -0.0078 ln
# at horizon 10 under dbl, and margins recede as the horizon grows,
# so horizons 9..11 are where a slow-map stall would live if any
# does; horizon 9 - a single counted step - was never scanned)
# ----------------------------------------------------------------- #

FRONTIER_HORIZONS = (9, 10, 11)
FRONTIER_DIGITS = WIDE_DIGITS + (96, 128, 192, 256)
FRONTIER_CAP = 30000

def e5_frontier():
    print("\nE5  THE SHORT-HORIZON FRONTIER (h 9/10/11, digits to "
          "256)")
    budget = [FRONTIER_CAP]
    specimens = []
    cell_best = {}
    for horizon in FRONTIER_HORIZONS:
        pool = census_pool(horizon)
        for mp in ("dbl", "id"):
            cell = []
            for wname, digs in pool:
                ev = SA.evaluate(digs, mp, horizon)
                if ev["stalls"]:
                    specimens.append((wname, digs, mp, horizon, ev))
                if ev["best_m"] is not None:
                    cell.append((ev["best_m"], wname, digs))
            cell.sort(key=lambda z: (-z[0], z[1]))
            print("  census h=%-2d %-3s: %d worlds, best margin "
                  "%+.4f ln (%s)" % (horizon, mp, len(cell),
                                     cell[0][0], cell[0][1]))
            for wname, digs in [(w, d) for _m, w, d
                                in cell[:SEED_K]]:
                if budget[0] <= 0:
                    break
                m, d, spec, acc = climb(digs, mp, horizon, budget,
                                        FRONTIER_DIGITS)
                tag = "seed %s/%s h=%d" % (wname, mp, horizon)
                if spec is not None:
                    specimens.append(("forged", d, mp, horizon,
                                      spec))
                    print("  %s: STALL after %d accepts"
                          % (tag, acc))
                    break
                print("  %s: local max margin %+.4f ln after %d "
                      "accepts" % (tag, m, acc))
                key = (horizon, mp)
                if m is not None and (key not in cell_best
                                      or m > cell_best[key][0]):
                    cell_best[key] = (m, d, wname)
    if budget[0] <= 0:
        print("  NOTE: evaluation budget (%d) exhausted - climbs "
              "beyond it were dropped" % FRONTIER_CAP)
    print("  evaluations spent %d of %d"
          % (FRONTIER_CAP - budget[0], FRONTIER_CAP))
    for (horizon, mp), (m, d, wname) in sorted(cell_best.items()):
        print("  frontier best h=%-2d %-3s: %+.4f ln  digits %s  "
              "(seed %s)"
              % (horizon, mp, m,
                 "".join(str(x) + ("." if x > 9 else "")
                         for x in d), wname))
    return specimens

# ----------------------------------------------------------------- #

def main():
    print("THE MAP-RATE QUESTION: does the stall need a fast map?")
    print("=" * 70)
    e1_controls()
    if FAILURES:
        print("\nCONTROLS FAILED - no verdicts.")
        sys.exit(1)
    seeds, census_stalls = e2_census()
    for wname, digs, mp, horizon, ev in census_stalls[:3]:
        SA.anatomy("CENSUS SPECIMEN (%s)" % wname, digs, mp,
                   horizon, ev)
    specimens, cell_best = e3_forge(seeds)
    frontier = e5_frontier()
    print("\nE4  ESCAPE RADIUS of every specimen (cap 4)")
    pool = [(w, d, mp, h, ev) for w, d, mp, h, ev in census_stalls]
    pool += [("forged", d, mp, h, ev) for d, mp, h, ev in specimens]
    pool += frontier
    seen = set()
    for wname, digs, mp, horizon, ev in pool:
        key = (tuple(digs), mp, horizon)
        if key in seen:
            continue
        seen.add(key)
        for s in ev["stalls"]:
            r = SA.escape_radius(s, ev["nbrs"], ev["qloss"])
            print("  %s/%s h=%d class %s: radius %s"
                  % (wname, mp, horizon,
                     SC.summarize_class(ev["mem"][s]),
                     "NONE<=4" if r is None else str(r)))
    print("\nVERDICT OBSERVABLES")
    if census_stalls or specimens or frontier:
        print("  K2: a slow-map stall exists - specimens below.")
        shown = set()
        spool = ([(d, mp, h, ev) for d, mp, h, ev in specimens]
                 + [(d, mp, h, ev) for _w, d, mp, h, ev in frontier])
        for digs, mp, horizon, ev in spool:
            key = (tuple(digs), mp, horizon)
            if key in shown or len(shown) >= 3:
                continue
            shown.add(key)
            SA.anatomy("FORGE SPECIMEN", digs, mp, horizon, ev)
    else:
        print("  K3: zero id/dbl stalls at the widened scope.")
        for (horizon, mp), (m, d, wname) in sorted(cell_best.items()):
            print("  best h=%-2d %-3s: %+.4f ln  digits %s  (seed %s)"
                  % (horizon, mp, m,
                     "".join(str(x) + ("." if x > 9 else "")
                             for x in d), wname))
    print("\n%s" % ("ALL CHECKS PASS" if not FAILURES
                    else "FAILURES: %s" % FAILURES))
    sys.exit(1 if FAILURES else 0)

if __name__ == "__main__":
    main()
