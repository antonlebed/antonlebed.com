"""Does the ONE-CLASS STRUCTURE play the period, or does e-2? The
closure instrument read at three designed aperiodic one-class windows.

THE QUESTION
------------
The prefix closures call e-2 whole and refuse the cubic
(explore_cascade_closure.py C2-C6), and the named difference is
one-class largeness structure: e-2's large caps sit on one residue
class mod 3, the cubic's on no class. But one aperiodic window of each
kind has been read, so "the structure plays the period" rests on a
single member per side. This rig designs aperiodic one-class windows
whose large-cap VALUES are arbitrary -- sharing nothing with e-2 but
the class -- and reads them on the same closure ladder with the same
composite candidate:

    verdict(r) = DELAY-0  if the true window has no drop site at
                 stride r (census from the quotients);
    verdict(r) = the stabilized closure verdict  otherwise.

If the class does the work, the new windows read like e-2. If e-2's
specific quotient arithmetic (1, 1, 2n -- an arithmetic progression,
the Hurwitz tail of e) does the work, something breaks.

THE WINDOWS (defined by their quotient lists; each is its own
certification -- a designed window's quotients are its definition).
  W1 "primes"      caps 1, 1, c_k with c_k the k-th prime:
                   1, 1, 2, 1, 1, 3, 1, 1, 5, 1, 1, 7, ...
                   One-class mod 3 (large at j = 2 mod 3, 0-based),
                   UNBOUNDED so aperiodic (a periodic window has
                   bounded caps), MONOTONE along the class like e-2,
                   values sharing no progression with e-2's 2n.
                   THE PRIMARY WINDOW: its verdict is the test.
  W2 "swapped"     c'_k = adjacent primes transposed: 3, 2, 7, 5,
                   13, 11, 19, 17, ... One-class, unbounded,
                   NON-monotone along the class: the class stride
                   r = 3 has TRUE drops (3 > 2 at j = 2 onto j = 5),
                   r = 6 is dropless (lag-2 along the class is
                   increasing). Separates "one-class" from
                   "one-class + monotone".
  W3 "thue-morse"  c''_k = 2 + tm(k-1), tm the Thue-Morse bit:
                   caps 2, 3, 3, 2, 3, 2, 2, 3, ... on the class.
                   One-class, BOUNDED, aperiodic by Thue's theorem
                   (the sequence is cube-free, in particular not
                   eventually periodic). No stride is expected
                   dropless (the rig counts rather than argues).
                   Separates "one-class" from "one-class + unbounded".

MARKED TRANSPLANTS. (1) The automaton and the word "period" are the
periodic storey's machinery, imported as an instrument exactly as the
parent rig imports them. (2) The parity expectation -- gated at
r = 1 mod 3, not gated at r = 2 mod 3 -- is imported from the
stride-parity reading recorded with explore_shift_repair.py, which
that record files as a READING and not a derivation; whether it
transfers to windows sharing only the class is the question, so at
W2/W3 it is an expectation under test, never a control.

THE HAND-ATTACK (pre-engine, on paper; index convention re-derived
from the engine: prefix is 0-based, a drop site of the true window at
stride r is j with prefix[j] > prefix[j+r], the closure census reads
the period cyclically).
  W1 drop census. r = 0 mod 3: large maps to large with c_k
    increasing, small to small -- NO drop at any j; r = 1, 2 mod 3:
    every large j (j = 2, 5, 8, ...) drops onto a cap-1 position and
    no other j drops. So the dropless clause fires exactly at
    r = 3, 6 -- where the proved non-decreasing mechanism already
    makes the shift the bare coordinate map (delay 0) as a PROPERTY.
    The LIVE test at W1 is therefore the gated/not-gated split on
    r not = 0 mod 3.
  W1 seam. A closure at m = 0 mod 3 wraps c_M onto c_1 (both large,
    c_M > c_1): at r = 3 the wrap manufactures ONE seam drop per
    period, the parent rig's paper death in the same place -- so
    small-m closures should corrupt r = 3 and the corruption should
    wash out with m if W1 behaves as e-2 did (there: r = 3 gated
    m = 4..8, bounded from m = 9 on).
  W2 drop census. r = 3: true drops at half the class (c'_odd >
    c'_even neighbours); r = 6: dropless (increasing at lag 2);
    r not = 0 mod 3: large onto small as at W1.
  W3 drop census. Expected drops at every stride including 3 and 6
    (3-onto-2 happens at both lags in TM); the rig prints the count.

PREDICTIONS, FIXED BEFORE THE RUN (as observables; the verdict names
what the rig PRINTS)
  Q1 (positive control -- wiring). The golden window and the designed
      periodic (P, A) = (3, 2), (4, 2), (5, 3) cells print the
      recorded residue law (r = 0 mod P delay-0, even nonzero residue
      finite, odd gated); e-2's closures m = 12, 15 print the
      recorded vector G b b G b b G b at r = 1..8. KILL: any cell
      off -- the rig is miswired and nothing below is a measurement.
  Q2 (the primary window). At W1, closures m = 3..21, 24, r = 1..8:
      (a) the verdict vector is STABLE AT THE SCANNED SCOPE (identical
      at the top five computed closures); (b) the stabilized composite
      table reads G b d0 G b d0 G b -- gated 1, 4, 7, not gated
      2, 5, 8, delay-0 at the dropless 3, 6; (c) the r = 3 seam
      corruption washes out by some m as at e-2. All three landing =
      the one-class structure does the work at a second aperiodic
      window, values arbitrary. Any stabilized cell OFF the parity
      table, or no stabilization, is the other verdict: e-2's call
      rested on more than the class. Both exits are findings; only Q1
      voids the run.
  Q3 (the contrasts -- forks, no direction frozen where the record
      has none). W2: r = 6 prints delay-0 (dropless, mechanism);
      r = 1, 4, 7 / 2, 5, 8 read against the parity expectation;
      r = 3 -- true drops ON the class stride -- is an open fork: the
      composite candidate says the stabilized closure verdict, and
      whatever it stabilizes to (or fails to) is the finding. W3: the
      parity expectation at r not = 0 mod 3; r = 3, 6 open forks with
      true drops; stabilization itself is the headline observable at
      a bounded-cap aperiodic window.
  Q4 (peaks). Per window, over the deep half of the ladder: strides
      whose stabilized verdict is GATED print unbounded-trending
      peaks (gated cells counted as new highs); strides not gated
      hold a band with no new high. KILL of the peak reading at that
      window, either direction, as in the parent's Q6.
  Q5 (cross-instrument control). At W1 closures m = 6, 9 and W3
      closures m = 6, 9, the finite engine's column at its own range
      sits at or below the limit column at every depth. KILL: any
      violation -- the box or the automaton is wrong, run void.
  Q6 (witness transfer). At each window, cells picked off the printed
      ladder where a deep closure GATES: the walker run with the TRUE
      window's numeration (build_q_positions on the defining
      quotients). A pair counts only at POSITIVE MARGIN (agreement
      minus recomputed parting position). Frozen observables: at W1's
      predicted-gated strides, positive-margin pairs with the parting
      position fixed while agreement climbs = certified integer
      ladders, the e-2 signature; at W1's predicted-bounded strides a
      positive-margin pair is not a kill but a REFUTATION of the
      parity table at that stride (an exact instance outranks the
      transplanted reading). Zero positive-margin hits anywhere at a
      window whose closures stabilize gated = the transfer carries no
      content there and the closure evidence stays closure-side.

THE DESIGN
----------
Everything is imported: PrecWindow, tile, verdict_of, seam_census,
true_census, read_closure from explore_cascade_closure (the recorded
instrument, unchanged -- which is what makes Q1 a control of this
rig's wiring); Shift, limit_column, witness, finite_column from
explore_limit_column; designed, build_q_positions from
explore_shift_repair. Nothing about the automaton or the walker is
rewritten.

S0  CONTROLS. Q1's cells.
S1  W1 LADDER. m = 3..21, 24, r = 1..8: verdict, seam census, peaks;
    finite check at m = 6, 9.
S2  W2 LADDER. m = 3..21, r = 1..8.
S3  W3 LADDER. m = 3..21, r = 1..8; finite check at m = 6, 9.
S4  ASSEMBLY. Per window: the true-window drop census per stride
    (j <= 60), the composite verdict table beside the parity
    expectation, stability at the scanned scope, peak matrices.
S5  WITNESS TRANSFER. Per window, per stride: the two deepest
    closures whose cell GATES, walker at four cycle counts, margin
    in every print.

RESOURCE: ~500 cells, the parent's deepest cell ran 0.2 s at period
30 caps 14; W1's caps reach 19 at m = 24. Estimate 3-8 min wall,
bounded, expected far under 512MB but run through memwatch at the
default ceiling; stages print as they complete.

RUN RECORD
----------
Recorded run: wall 29.7 s, peak working set 41.5 MB under memwatch's
512 MB ceiling. Every cell decided, none refused, none near the state
ceiling. Controls: all 30 S0 cells exact (golden + three designed
windows on the recorded law; e-2's closures m = 12, 15 reproduce the
recorded vector G b b G b b G b); 32 of 32 finite-engine-vs-limit
checks OK; zero reconstruction or legality failures.

FINDINGS (each at its own tier)
-------------------------------
F1  THE COMPOSITE CANDIDATE CALLS THE PRIMARY WINDOW WHOLE (rule at
    scanned scope; Q2 lands on all three observables). At W1 the
    verdict vector is G b b G b b G b -- gated 1, 4, 7 -- at EVERY
    closure from m = 12 through 24, eleven consecutive, stabilizing
    at the same m = 12 as e-2; the dropless clause reads r = 3, 6
    (0 sites at j <= 60) as delay-0; the composite table matches the
    parity expectation at all eight strides. The seam drops the wrap
    manufactures at r = 3 gate only at m = 4..6 and wash out from
    m = 7, every stride settling by m = 12. Peaks read the same
    split: gated strides gate outright at every deep closure, the
    bounded strides' peaks hold a band of 7 over the deep half. So
    the one-class structure does the work at a second aperiodic
    window whose cap values (the primes) share nothing with e-2's
    2n beyond the class.
F2  W1'S GATED HALF CARRIES CERTIFIED INTEGER LADDERS AND ITS BOUNDED
    HALF REFUSES EVERY PAIR (verified instances; Q6's W1 half). At
    r = 1, 4, 7 the walker hands out pairs verifying by integer
    arithmetic on the defining quotients with the parting position
    fixed AT THE STRIDE (part = r) while agreement climbs: 26, 50,
    74 at m = 24 (integers to 43 digits), 44, 86 at m = 21 (to 52
    digits). At r = 2, 5, 8 every extracted pair MISSes greedy-ness
    or verifies at negative margin (-3 to -6, parting climbing with
    agreement) -- no instance, e-2's Q7 signature.
F3  MONOTONICITY ALONG THE CLASS IS NOT LOAD-BEARING, AND THE CLASS
    STRIDE FOLLOWS ITS OWN DROP CENSUS (rule at scanned scope; Q3's
    W2 fork resolves). W2 stabilizes from m = 12 to
    G b G G b b G b: the parity split at every r not = 0 mod 3 with
    r = 1, 4, 7 certified (margins to +166, integers to 124 digits),
    the dropless class stride r = 6 delay-0, and the TRUE-dropped
    class stride r = 3 GATED at every stable closure -- but
    closure-side only: every r = 3 pair verifies at constant margin
    -3 with the parting position climbing alongside agreement, the
    cubic's non-transfer signature, so the r = 3 gate stands as
    instrument output with no certified instance.
F4  BOUNDED CLASS CAPS BREAK THE VERDICT LEG AND NOT THE OTHER TWO
    (observation, one bounded window scanned; Q3's W3 fork). W3's
    verdict sequence never stabilizes -- the deep vectors cycle with
    the wrapped Thue-Morse word (m = 18 and 21 print identical
    vectors) -- yet the peak reading separates the parity split
    cleanly at r not = 0 mod 3 (r = 2, 5, 8 band at peaks <= 4 over
    the whole deep half while 1, 4, 7 gate or print new highs), and
    positive-margin certificates transfer at EXACTLY r = 1, 4, 7
    (margins to +169, agreement to 170, integers to 49 digits),
    zero positive instances anywhere else. The class strides r = 3,
    6 (sparse true drops, 7 and 6 sites at j <= 60) read mostly
    bounded and stay open.
F5  WHAT PLAYS THE PERIOD, SHARPENED (synthesis of F1-F4 with the
    parent's C6; pattern over four one-class aperiodic windows
    counting e-2, one cubic). The SPLIT -- gated at r = 1 mod 3, not
    gated at r = 2 mod 3 -- and the CERTIFICATES ride the class
    alone: they land identically at unbounded monotone (e-2, W1),
    unbounded non-monotone (W2), and bounded (W3) class caps.
    STABILIZATION of the closure verdict additionally needs the
    class caps unbounded: the one bounded window scanned cycles like
    the cubic. The class strides r = 0 mod 3 are decided by their
    own drop census where it is empty (delay-0, the proved
    mechanism) and gated closure-side at W2's dropped r = 3. The
    cubic's refusal is thereby sharpened: it fails BOTH legs -- no
    class, nothing stabilizes, nothing transfers -- where a
    one-class window with the wrong cap growth fails only the
    verdict leg.
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_cascade_closure import (       # noqa: E402
    PrecWindow,
    read_closure,
    seam_census,
    tile,
    true_census,
    verdict_of,
)
from explore_limit_column import (          # noqa: E402
    Shift,
    limit_column,
    witness,
)
from explore_shift_repair import (          # noqa: E402
    build_q_positions,
    designed,
    quotients_e_minus_2,
)

CENSUS_J = 60
QWANT = 200


# ------------------------------------------------------------- windows

def sieve_primes(n):
    ps, k = [], 2
    while len(ps) < n:
        if all(k % p for p in ps):
            ps.append(k)
        k += 1
    return ps


def quotients_w1(want):
    """1, 1, c_k with c_k the k-th prime."""
    ps = sieve_primes(want // 3 + 2)
    return [ps[k // 3] if k % 3 == 2 else 1 for k in range(want)]


def quotients_w2(want):
    """Adjacent primes transposed on the class: 3, 2, 7, 5, 13, 11..."""
    ps = sieve_primes(want // 3 + 3)
    sw = []
    for i in range(0, len(ps) - 1, 2):
        sw += [ps[i + 1], ps[i]]
    return [sw[k // 3] if k % 3 == 2 else 1 for k in range(want)]


def tm_bit(n):
    return bin(n).count("1") & 1


def quotients_w3(want):
    """2 + Thue-Morse bit on the class."""
    return [2 + tm_bit(k // 3) if k % 3 == 2 else 1 for k in range(want)]


WINDOWS = [
    ("W1-primes", quotients_w1),
    ("W2-swapped", quotients_w2),
    ("W3-thue-morse", quotients_w3),
]

# The parity expectation (marked transplant; under test, never a
# control): per stride 1..8, G = gated, b = not gated, d = delay-0
# where the dropless clause fires, ? = open fork.
EXPECT = {
    "W1-primes":     {1: "G", 2: "b", 3: "d", 4: "G", 5: "b",
                      6: "d", 7: "G", 8: "b"},
    "W2-swapped":    {1: "G", 2: "b", 3: "?", 4: "G", 5: "b",
                      6: "d", 7: "G", 8: "b"},
    "W3-thue-morse": {1: "G", 2: "b", 3: "?", 4: "G", 5: "b",
                      6: "?", 7: "G", 8: "b"},
}


# ------------------------------------------------------------------ s0

def s0_controls():
    print("=" * 78)
    print("S0 CONTROLS: wiring against the recorded law (Q1)")
    ok = True
    cells = [("golden", [1] * 70, 1, (1, 2, 3))]
    for P, A in ((3, 2), (4, 2), (5, 3)):
        cells.append((f"designed({P},{A})", designed(P, A, 70), P,
                      tuple(range(1, 2 * P + 1))))
    for name, caps, P, rs in cells:
        for r in rs:
            lc = limit_column(Shift(PrecWindow(caps, P), r))
            v = verdict_of(lc)
            if P == 1 or r % P == 0:
                good = (v == "delay-0")
                want = "delay-0"
            elif (r % P) % 2 == 0:
                good = (v != "GATED")
                want = "finite"
            else:
                good = (v == "GATED")
                want = "GATED"
            ok &= good
            print(f"  {name} r {r}: {v:7s} want {want:7s} "
                  f"{'ok' if good else 'MISS'}")
    e2 = quotients_e_minus_2(QWANT)
    recorded = "GbbGbbGb"
    for m in (12, 15):
        got = ""
        for r in range(1, 9):
            lc = limit_column(Shift(PrecWindow(tile(e2, m), m), r))
            v = verdict_of(lc)
            got += "G" if v == "GATED" else "b"
        good = (got == recorded)
        ok &= good
        print(f"  e-2 closure m {m}: {got} want {recorded} "
              f"{'ok' if good else 'MISS'}")
    return ok


# --------------------------------------------------------- the ladders

def ladder(name, prefix, ms, finite_ms=()):
    print("=" * 78)
    print(f"{name} LADDER: closures over m, r = 1..8")
    table = {}
    for m in ms:
        for r in range(1, 9):
            cell = read_closure(name, prefix, m, r,
                                check_finite=(m in finite_ms))
            table[(m, r)] = cell
    return table


# ----------------------------------------------------------- assembly

def assemble(name, prefix, table, ms):
    print("=" * 78)
    print(f"{name} ASSEMBLY: composite verdict against the expectation")
    exp = EXPECT[name]
    print("  true-window drop census (j <= %d):" % CENSUS_J)
    dropless = set()
    for r in range(1, 9):
        sites = true_census(prefix, r)
        if not sites:
            dropless.add(r)
        head = ", ".join(str(j) for j in sites[:8])
        more = " ..." if len(sites) > 8 else ""
        print(f"    r {r}: {len(sites):2d} sites"
              f"{('  [' + head + more + ']') if sites else '  DROPLESS'}")
    # stability: top five computed closures
    top5 = ms[-5:]
    vecs = {}
    for m in ms:
        vecs[m] = "".join(
            {"GATED": "G", "delay-0": "0", "bounded": "b",
             "REFUSED": "?"}[table[(m, r)]["v"]] for r in range(1, 9))
        print(f"    m {m:2d}: {vecs[m]}")
    stable = len({vecs[m] for m in top5}) == 1
    print(f"  stable at the scanned scope (top five {top5}): "
          f"{'YES' if stable else 'NO'}")
    # the composite table
    verdicts = {}
    line = []
    for r in range(1, 9):
        if r in dropless:
            comp = "d"
        elif stable:
            comp = {"G": "G", "b": "b", "0": "b"}[vecs[top5[-1]][r - 1]]
        else:
            comp = "?"
        verdicts[r] = comp
        want = exp[r]
        mark = ("ok" if want == comp else
                ("fork" if want == "?" else "OFF"))
        line.append(f"r{r} {comp}/{want} {mark}")
    print("  composite vs expectation:  " + "  ".join(line))
    # peaks over the deep half
    print("  peak ladder per stride (deep half; * = gated cell):")
    half = ms[len(ms) // 2:]
    for r in range(1, 9):
        seq = []
        for m in half:
            c = table[(m, r)]
            seq.append("*" if c["v"] == "GATED"
                       else str(c["peak"]))
        print(f"    r {r}: " + " ".join(seq))
    return verdicts, stable


# ----------------------------------------------------------- witnesses

def transfer(name, prefix, table, ms):
    print("=" * 78)
    print(f"{name} WITNESS TRANSFER: gated closure cells against the"
          f" true numeration (Q6)")
    qtrue = build_q_positions(list(prefix), QWANT - 10)
    for r in range(1, 9):
        gated_ms = [m for m in ms if table[(m, r)]["v"] == "GATED"]
        for m in gated_ms[-2:]:
            sh = Shift(PrecWindow(tile(prefix, m), m), r)
            lc = limit_column(sh)
            if lc["inf_from"] is None:
                continue
            t = lc["inf_from"]
            for turns in (1, 2, 3, 4):
                got = None
                for tt in range(t, t + 7):
                    try:
                        got = witness(sh, tt, turns, qtrue)
                    except AssertionError:
                        got = "MISS"
                    if got is not None:
                        break
                if got is None:
                    print(f"  {name} m {m:2d} r {r} turns {turns}: no"
                          f" parted infinite pair near t = {t}")
                elif got == "MISS":
                    print(f"  {name} m {m:2d} r {r} turns {turns}:"
                          f" MISS -- pair not greedy on the true"
                          f" window")
                else:
                    n1, n2, agree, diff, cyc = got
                    inst = agree - diff
                    big = max(n1, n2)
                    show = (f"n1 {n1} n2 {n2}" if big < 10 ** 60
                            else f"n1,n2 with {len(str(n1))},"
                                 f"{len(str(n2))} digits")
                    kind = ("POSITIVE INSTANCE" if inst > 0 else
                            "no instance (agreement below parting)")
                    print(f"  {name} m {m:2d} r {r} turns {turns}:"
                          f" greedy-verified, agree {agree} part"
                          f" {diff} margin {inst:+d} --> {kind}"
                          f" (cycle {cyc}; {show})")


if __name__ == "__main__":
    t0 = time.time()
    if not s0_controls():
        print("S0 RED: stopping -- nothing below is a measurement.")
        sys.exit(1)
    ms = list(range(3, 22))
    plans = {}
    for name, qfun in WINDOWS:
        prefix = qfun(QWANT)
        use = ms + [24] if name == "W1-primes" else ms
        fin = (6, 9) if name in ("W1-primes", "W3-thue-morse") else ()
        plans[name] = (prefix, use,
                       ladder(name, prefix, use, finite_ms=fin))
    for name, _ in WINDOWS:
        prefix, use, table = plans[name]
        assemble(name, prefix, table, use)
    for name, _ in WINDOWS:
        prefix, use, table = plans[name]
        transfer(name, prefix, table, use)
    print(f"total wall {time.time() - t0:.1f}s")
