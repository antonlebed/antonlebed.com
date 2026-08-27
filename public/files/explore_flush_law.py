"""Is c_int = max(c_saf, L*) a law? The flushed-state bound made exact by
a clairvoyant automaton, and the equality put to the 32 band cells no
rig has run.

THE QUESTION
------------
explore_flush_floor.py F4: the integer reader's lookahead c_int equals
the larger of c_saf -- the same game released from finishing,
explore_flush_price.py -- and L* -- the least level drop at which every
late legal tail's m-fold is a capped string, read over tails to length
P + 2 -- at all 130 cells the corpus has decided. Both are proved lower
bounds; the equality has no sufficiency proof under it and is filed as
an observation. This rig does two things to it. It replaces the
truncated L* by the untruncated object, so the equality is stated
against a quantity with no tail length in it; and it asks the equality
of the 32 band cells explore_lookahead_band.py found under s <= 12 and
never ran -- the cells that could break it, its whole evidential base
so far sitting at s <= 9.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
H1  THE INDEX CONVENTION, RE-DERIVED FROM THE ENGINE. Game.step at
    position pos emits y and then reads input index pos + look + 1; a
    state's branch set already holds the digits through pos + look. At
    look = 0 a state at pos holds d_0..d_pos and e_0..e_{pos-1}, and
    the reply to y is d_{pos+1}. Positions run 0, 1, 2..P+1 and then
    wrap to 2 (Game.npos), the wrap applying the period unit
    (apply_hinv); phase is pos mod P. cap_in(k) is a_1 - 1 at k = 0 and
    a_{k+1} otherwise, at the cap only over a zero; cap_out(k) is
    a_1 - 1 + s_0 at 0 and a_{k+1} + s otherwise. q_{-1} = 0, q_0 = 1,
    q_k = a_k q_{k-1} + q_{k-2}.
H2  THREE READERS OF ONE RESIDUAL. At lookahead c the reader's whole
    state is the integer residual R_t = m val(d_{<=t+c}) - val(e_{<t}),
    to be written from level t on. The game's reader must drive R to 0
    and hold it against every continuation. The reader released from
    FINISHING (c_saf) keeps R in the box forever. The reader released
    from IGNORANCE -- the CLAIRVOYANT reader, lookahead infinity --
    wins from a flushed state at level k - l against a late tail tau
    from k iff m val(tau) is a capped string from level k - l: L*'s
    condition verbatim. So L* is the clairvoyant reader's least
    lookahead from a flushed state, and the equality reads: the game
    costs nothing beyond its two relaxations.
H3  L* IS EXACT, WITHOUT A TAIL LENGTH. The set of residuals reachable
    by ANY choice of outputs so far, pruned to the box, is a
    deterministic automaton on the input digits -- Game.step with the
    UNION over y in place of the choice of y. The pruning is sound
    because every accepting string's partial residuals sit inside the
    derived box (explore_lookahead_band.py F6, no lookahead term in
    breal; bconj at look = 0 covers a residual holding digits through
    pos and nothing beyond). The automaton is finite because the box
    is. From the state ({(0, 0)}, pos, after a zero) the clairvoyant
    reader wins iff EVERY reachable state's zero-input path -- one
    path, the automaton being deterministic -- passes a state holding
    (0, 0): from there e = 0 under zero input holds it. Starting it at
    every phase with l zero levels below the tail reads L*_inf(l).
    The l - 1 replies below the tail are FORCED to zero: a nonzero one
    there is a tail starting closer to the start level, a STRONGER
    demand than the one asked (a first draft left them free and read
    the bound past its cap at every non-digitwise cell -- the sweep
    was asking level drop 1 of every cell; the per-tail control, which
    forces the zeros, was green throughout). Tails starting further
    up are weaker demands and cost nothing to leave in. Its
    comparison with the truncated bound is FORCED one way:
    c_int >= L*_inf >= L*_{P+2}, so at every cell with c_int =
    L*_{P+2} the two agree, and only at the 36 cells with
    c_int = c_saf > L*_{P+2} can the untruncated bound rise -- where
    the equality cannot move.
H4  WHAT WOULD BREAK THE EQUALITY: COMMITMENT. Mid-flush, R_t != 0 and
    e_t due, two legal continuations of the seen window can demand two
    incompatible pending strings for one R_t -- the union the
    clairvoyant automaton carries and the game cannot. The safety
    reader meets the fork only in the real coordinate, where the box
    is several units wide and integer strings of one value are
    indistinguishable, so the equality says: the fork never has two
    INTEGER prongs the box does not already separate. No proof here.
    The route to one is a strategy that never carries a pending
    residual into a late digit, flushing inside the zero window it
    sees; its obstruction is a digit at its cap arriving before the
    pending string has cleared the two levels below it, which is
    likelier the larger the cap a + s and the larger m -- the band's
    far end, and never its left endpoint, which the 42 - 10 = 32 unrun
    cells cover and the ten run ones do not.
H5  WHERE IT CAN BLOW UP. (a) The subset automaton's states are unions
    and the union tends to fill the box, so its state count is small
    but each state is wide; it is bounded by the box's lattice points.
    (b) The band cells' Game builds at caps 10..17 and m up to 5: the
    corpus's heaviest decided cell, [5] x3 s = 9 at cap 14, peaked at
    410 MB, so some of the 32 will not fit under 512 MB. Each cell is
    its own process under memwatch; a killed cell is reported UNRUN
    and never re-run wider: a wider run there buys a pattern and
    not a verdict. Cells are ordered by cap a_max + s and m, cheapest first.
    (c) c_int is searched to LOOKCAP = 3 as the band rig did (H3 of
    the parent bounds the completion reader and no integer one), and a
    cell reading "-" at 3 with c_saf and L*_inf both <= 3 is a KILL
    (c_int >= 4 > the max), while one whose c_saf is "-" as well is
    undecided and says so.
TRANSPLANT, marked: the game, its box, its step, the band and the
frozen c_int/c_saf/L* readings are explore_redundant_ostrowski.py's,
explore_lookahead_band.py's, explore_flush_price.py's and
explore_flush_floor.py's. Nothing here re-derives them; the automaton
is built from Game.step and the box is Game's own.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  C1 (controls, run FIRST; nothing below is read if any leg is red)
     (a) THE AUTOMATON AGAINST THE DECIDER. At every window, at
         several (s, s_0, m) and level drops l, for every legal tail
         to length P + 2 at every phase: the automaton fed the tail and
         then zeros reaches a (0, 0)-holder iff Caps.codable says
         m val(tau) is a capped string from level k - l. A mismatch in
         EITHER direction is red -- automaton-no/decider-yes is the box
         pruning an accepting string.
     (b) L*_inf >= L*_{P+2} AND L*_inf <= c_int at all 130 decided
         cells (H3; a violation is a fault of the automaton or of the
         box, never a finding).
  P1 THE UNTRUNCATED BOUND AT THE 130. Per cell L*_{P+2}, L*_inf,
     c_saf, c_int (the last three the parents' frozen readings, printed
     through explore_flush_floor.bounds and explore_flush_price.price
     for L*_{P+2} and the two lookaheads). Prediction: L*_inf =
     L*_{P+2} at the 94 cells with c_int = L*_{P+2} (forced). At the
     other 36 the count of cells where L*_inf rises is printed and not
     predicted; the tally of c_int - max(c_saf, L*_inf) is printed.
  P2 THE 32 BAND CELLS, cheapest first, each its own process under
     memwatch: L*_{P+2}, L*_inf, c_saf, c_int to LOOKCAP, state count,
     wall-clock. KILL, as an observable: any cell printing c_int
     finite and above max(c_saf, L*_inf); or c_int "-" with both
     c_saf and L*_inf <= LOOKCAP. Not predicted: how many cells fit
     under 512 MB; the unrun ones are listed by name.
  P3 THE TALLY over every decided cell of the 130 + the band cells
     that ran: c_int - max(c_saf, L*_inf), and the counts of
     c_int = c_saf, c_int = L*_inf, both.
  P4 wall-clock and peak per process in the run record.

THE DESIGN
----------
Stages: s0 the C1a control on the automaton; s1 the untruncated bound
at the 130 with C1b; s2 one band cell per process (LAW_CELL = index
into the sorted list, LAW_STAGES selects). The clairvoyant automaton
is `Clairvoyant`: a Game built at look = 0 supplies step, inbox and
the box; states are (pos, frozenset of branches, pzd), the transition
on a reply x is the union over every y of Game.step's branch set at
that reply. Verdict per start phase and level drop: BFS over the
reachable states; each state's zero-input path memoized to "passes a
holder". L*_inf(cell) is the least l at which every phase passes, or
None past LCAP. L*_{P+2} comes from explore_flush_floor.bounds and the
band's c_int/c_saf from explore_flush_price.price with top = LOOKCAP.
LAW_GAMES=0 prints the bounds and skips the games, for a cell the
ceiling refuses the game of.

FINDINGS (entered post-run; every number below sits in this file's
printed output. Runs under memwatch at the 512 MB default, peaks as
WORKING SET: s0 in 22 s at 104.0 MB; s1 in 193 s at 348.8 MB; the band
one cell per process, 23 decided between 6 s / 91.7 MB (bronze x4 s=7)
and 68 s / 474.3 MB ([4] x5 s=12), the highest peak 503.1 MB at [5] x4
s=9, the period-4 cells spending 69-201 s in the bounds alone; NINE
cells KILLED at 512-530 MB commit -- V2 x5 at s = 10, 11; [5] x5 at
s = 9, 10, 11, 12; [5] x4 at s = 10, 11, 12 -- and re-run with
LAW_GAMES=0: the bounds print at seven of them (28-74 s, under 181 MB)
and V2 x5 at s = 10 and 11 are killed in the BOUNDS stage itself, at
~516 MB after ~150 s, the automaton and the tail enumeration at a
period-4 window at cap 13 and 14. Nothing ran bare. One rig fault
fixed between the first and the second s1 run, recorded at H3: the
replies below the tail left free.)

F1  THE CONTROLS HOLD. C1a: 0 bad of 13,856 (tail, level-drop) pairs
    over the eight windows, four (m, s, s_0) cells each and l = 0..3 --
    the automaton and the decider agree in both directions, so the box
    prunes no accepting string. C1b: 0 bad at 130 -- L*_inf between
    L*_{P+2} and c_int at every cell.
F2  THE UNTRUNCATED BOUND (P1). L*_inf = L*_{P+2} at 128 of the 130
    cells and RISES at two, from 2 to 4 at golden x3 (0, 1) and
    sqrt3-1 x4 (0, 1) -- both cells with c_saf = c_int = 5, the only
    place H3 allows a rise. So the truncation at P + 2 was exact at
    every cell where L* was the binding bound and short by two at two
    cells where it was not. c_int = max(c_saf, L*_inf) at all 130,
    = c_saf at 91, = L*_inf at 94, both at 55: the counts of the
    parent's F4 unchanged, the two risen cells still sitting under
    their c_saf.
F3  THE BAND (P2). No kill. At all 23 decided cells c_int = 2 =
    max(c_saf, L*_inf) with L*_inf = L*_{P+2} = 2: c_saf = 1 at 20 of
    them and 0 at the three V2 (2,1,3,1) cells, x4 at s = 7 and 8 and
    x5 at s = 9, which price the flush at 2 beside V2 x3 (5, 5) and
    the grid's V1 x3 (3, 3) -- every price-2 cell of the corpus is a
    period-4 window whose released reader needs no lookahead at all.
    The 23 run from cap 10 to cap 16 and 1 + s = 13 against 2m = 10;
    the nine refused are the x4 and x5 cells of [5] at s >= 9 and of
    V2 at s >= 10, and L*_inf = 2 at seven of those too, the two V2
    x5 cells unread even there.
F4  THE TALLY (P3). Over the 153 decided cells c_int - max(c_saf,
    L*_inf) is 0 at every one; c_int = c_saf at 91, = L*_inf at 117,
    both at 55.

TIER. H2-H3 are a PROPERTY: L* is the clairvoyant reader's lookahead
from a flushed state, and the automaton decides it exactly, its
soundness resting on the box's derivation for accepting runs and its
completeness on the union keeping every choice -- C1a is the check
and not the argument. F2 and F3 are exhaustive computations at the
cells named. The equality c_int = max(c_saf, L*) is an OBSERVATION at
153 cells against an exact bound -- both sides proved lower bounds,
no sufficiency proof, H4's commitment the thing a proof must rule
out -- and this rig does not make it a rule. The band's floor at 2 is
the parent's rule and needs nothing here.
"""

import os
import sys
import time
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_redundant_ostrowski import (               # noqa: E402
    LOOKCAP, WINDOWS, Game)
from explore_flush_price import BAND, price, window_of  # noqa: E402
from explore_flush_floor import (                       # noqa: E402
    LCAP, Caps, all_cells, bounds)
from explore_lookahead_band import EXTRA, band_of       # noqa: E402

STAGES = os.environ.get("LAW_STAGES", "s0,s1,s2").split(",")


# ----------------------------------------------- the clairvoyant reader
class Clairvoyant:
    """The subset automaton of the residual game at look = 0: every
    output choice kept, the input digit the only branching."""

    def __init__(self, period, m, s, s0):
        self.g = Game(window_of(period), 1, m, (0,), 0, s, s0)
        self.P = self.g.P
        self.memo = {}

    def start(self, phase, seen=0):
        """The flushed state at a position of this phase inside the
        frame's cycle (pos >= 2), holding the seen digit `seen`."""
        pos = phase
        while pos < 2:
            pos += self.P
        u, w = self.g.thv[pos % self.P]
        m = self.g.mi
        return (pos, frozenset([(-m * seen * u, -m * seen * w)]),
                seen == 0, True)

    def step(self, state):
        """Every legal reply x -> the union state over all y."""
        g = self.g
        out = {}
        for y in g.outputs(state):
            for x, (npos, br, pzd, _pze) in g.step(state, y):
                key = x
                if key in out:
                    out[key][1].update(br)
                else:
                    out[key] = [npos, set(br), pzd]
        return [(x, (v[0], frozenset(v[1]), v[2], True))
                for x, v in out.items()]

    def zero_passes(self, state):
        """Does the zero-input path from `state` pass a (0,0)-holder?"""
        path = []
        st = state
        while True:
            if st in self.memo:
                verdict = self.memo[st]
                break
            if (0, 0) in st[1]:
                verdict = True
                break
            if not st[1] or st in path:
                verdict = False
                break
            path.append(st)
            st = dict(self.step(st))[0]
        for p in path:
            self.memo[p] = verdict
        return verdict

    def wins_from(self, phase_k, l):
        """The clairvoyant reader from a flushed state l levels below a
        tail from a level of phase phase_k: the l - 1 replies below
        the tail forced to zero (a tail starting closer is a STRONGER
        demand, not a weaker one), then every legal continuation, and
        every reachable state must pass. At l = 0 the tail's first
        digit is the start's own seen digit, every nonzero value."""
        if l == 0:
            starts = [self.start(phase_k, x)
                      for x in range(1, self.g.cap_in(phase_k + self.P) + 1)]
        else:
            starts = [self.feed(self.start((phase_k - l) % self.P),
                                [0] * (l - 1))]
        return all(self._bfs(st) for st in starts)

    def _bfs(self, st0):
        seen = {st0}
        dq = deque(seen)
        while dq:
            st = dq.popleft()
            if not self.zero_passes(st):
                return False
            for _x, nxt in self.step(st):
                if nxt not in seen:
                    seen.add(nxt)
                    dq.append(nxt)
        return True

    def feed(self, st, digits):
        """The state after the replies `digits` from `st`."""
        for x in digits:
            st = dict(self.step(st))[x]
        return st


def lstar_inf(period, m, s, s0, lcap=LCAP):
    """The least level drop l at which the clairvoyant reader wins from
    a flushed state at every phase, or None past lcap."""
    cl = Clairvoyant(period, m, s, s0)
    P = cl.P
    for l in range(lcap + 1):
        ok = True
        for phase_k in range(P):
            if not cl.wins_from(phase_k, l):
                ok = False
                break
        if ok:
            return l
    return None


def fmt(v):
    return "-" if v is None else str(v)


# ------------------------------------------------------------ stages
def s0_control():
    print("== s0  C1a: the automaton against the decider, every legal "
          "tail to P + 2")
    bad = checked = 0
    t0 = time.time()
    for name, period in WINDOWS + EXTRA:
        for m, s, s0 in ((2, 1, 1), (3, 3, 3), (3, 5, 5), (4, 2, 2)):
            caps = Caps(period, s, s0)
            cl = Clairvoyant(period, m, s, s0)
            P = cl.P
            for l in range(0, 4):
                for phase_k in range(P):
                    k = caps.deep(phase_k)
                    for tail in caps.legal_tails(k, P + 2):
                        V = m * sum(x * caps.q[k + i]
                                    for i, x in enumerate(tail))
                        want = caps.codable(V, k - l)
                        if l == 0:
                            # the tail's first digit is the start's own
                            # seen digit
                            st = cl.feed(cl.start(phase_k, tail[0]),
                                         tail[1:])
                        else:
                            st = cl.feed(cl.start((phase_k - l) % P),
                                         [0] * (l - 1) + list(tail))
                        got = cl.zero_passes(st)
                        checked += 1
                        if got != want:
                            bad += 1
                            if bad <= 5:
                                print("    BAD %s x%d (%d,%d) l=%d phase %d"
                                      " tail %s: automaton %s decider %s"
                                      % (name, m, s, s0, l, phase_k,
                                         tail, got, want))
    print("  C1a: %d bad of %d   (%.0f s)" % (bad, checked, time.time() - t0))
    return bad


def s1_untruncated():
    print("== s1  P1: L*_{P+2}, L*_inf, c_saf, c_int at the 130; C1b")
    t0 = time.time()
    bad = rise = 0
    rows = []
    for name, period, m, s, s0 in all_cells():
        win = window_of(period)
        top = None
        if any(b[0] == name and b[2] == m and b[3] == s and s0 == s
               for b in BAND):
            top = LOOKCAP
        c_int, c_saf, _n = price(win, m, s, s0, top=top)
        _L1, Lt, _st = bounds(period, m, s, s0)
        Li = lstar_inf(period, m, s, s0)
        flag = ""
        if Li is None or Lt is None or c_int is None:
            flag = "  (undecided)"
        else:
            if Li < Lt or Li > c_int:
                bad += 1
                flag = "  BAD C1b"
            elif Li > Lt:
                rise += 1
                flag = "  RISES"
        print("  %-14s x%d (%d,%d)  L*_{P+2} %s  L*_inf %s  c_saf %s  "
              "c_int %s%s" % (name, m, s, s0, fmt(Lt), fmt(Li),
                              fmt(c_saf), fmt(c_int), flag))
        rows.append((name, m, s, s0, Lt, Li, c_saf, c_int))
    tally(rows)
    print("  cells where L*_inf rises above L*_{P+2}: %d" % rise)
    print("  C1b: %d bad   (%.0f s)" % (bad, time.time() - t0))
    return bad


def tally(rows):
    t = {}
    eq_saf = eq_L = eq_both = n = 0
    for _name, _m, _s, _s0, _Lt, Li, c_saf, c_int in rows:
        if Li is None or c_saf is None or c_int is None:
            continue
        d = c_int - max(c_saf, Li)
        t[d] = t.get(d, 0) + 1
        n += 1
        eq_saf += (c_int == c_saf)
        eq_L += (c_int == Li)
        eq_both += (c_int == max(c_saf, Li))
    print("  c_int - max(c_saf, L*_inf) over %d decided cells:" % n)
    for d in sorted(t):
        print("    %d: %d cells" % (d, t[d]))
    print("  c_int = c_saf at %d, = L*_inf at %d, = max at %d" %
          (eq_saf, eq_L, eq_both))


def band_cells():
    """The band cells under s <= 12 not in the frozen answer key, sorted
    cheapest first by (a_max + s, m)."""
    ran = set((b[0], b[2], b[3]) for b in BAND)
    cells = []
    for name, period in WINDOWS + EXTRA:
        win = window_of(period)
        for m in (2, 3, 4, 5):
            _line, _first1, band = band_of(win, m)
            for s in band:
                if (name, m, s) not in ran:
                    cells.append((name, period, m, s))
    cells.sort(key=lambda c: (max(c[1]) + c[3], c[2]))
    return cells


def s2_band():
    cells = band_cells()
    idx = os.environ.get("LAW_CELL")
    if idx is None:
        print("== s2  the %d unrun band cells, cheapest first:" % len(cells))
        for i, (name, period, m, s) in enumerate(cells):
            print("  %2d  %-14s x%d s=%d  cap %d" % (i, name, m, s,
                                                     max(period) + s))
        return
    name, period, m, s = cells[int(idx)]
    t0 = time.time()
    _L1, Lt, _st = bounds(period, m, s, s)
    Li = lstar_inf(period, m, s, s)
    t1 = time.time()
    # the bounds are cheap and print first, so a game the ceiling
    # refuses still leaves them on record
    print("  bounds %2s %-14s x%d s=%d  L*_{P+2} %s  L*_inf %s  (%.0f s)"
          % (idx, name, m, s, fmt(Lt), fmt(Li), t1 - t0))
    if os.environ.get("LAW_GAMES", "1") == "0":
        return
    c_int, c_saf, n = price(window_of(period), m, s, s, top=LOOKCAP)
    verdict = ""
    if Li is not None and c_saf is not None:
        mx = max(c_saf, Li)
        if c_int is None:
            verdict = "  KILL (c_int > %d >= max)" % LOOKCAP if mx <= LOOKCAP \
                else "  undecided"
        elif c_int > mx:
            verdict = "  KILL (c_int above max)"
        else:
            verdict = "  equal" if c_int == mx else "  BAD (below a bound)"
    else:
        verdict = "  undecided"
    print("  BAND %2s %-14s x%d s=%d  L*_{P+2} %s  L*_inf %s  c_saf %s  "
          "c_int %s  states %d  (%.0f s bounds, %.0f s games)%s"
          % (idx, name, m, s, fmt(Lt), fmt(Li), fmt(c_saf), fmt(c_int), n,
             t1 - t0, time.time() - t1, verdict))


def main():
    t0 = time.time()
    if "s0" in STAGES:
        if s0_control():
            print("CONTROL RED -- nothing below is read")
            return
    if "s1" in STAGES:
        s1_untruncated()
    if "s2" in STAGES:
        s2_band()
    print("total %.0f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
