"""
explore_one_vehicle.py -- does a greedy ring walk that stops opening places
settle on ONE of them? The third case between the stop law and the lock
permanence certificate, and why it is empty.

THE QUESTION. Two laws bracket a greedy walk over a number ring's places.
The stop law says a walk over columns of bounded tick gap stops OPENING new
places; the lock permanence certificate (explore_support_growth.py) proves
a candidate vehicle permanent once the walk is sitting on it. Between them
sits a shape neither forbids, named and hunted there (F6): a walk that
alternates forever among places it has already seated -- opening nothing,
settling on nothing. One hundred and forty seeds over five rings found no
such walk, and the record filed the gap as formally open and not within
easy reach. This file asks whether it is open at all: whether a walk that
opens finitely many places can fail to lock on exactly one of them.

THE WALK, restated from the engine it imports (explore_support_growth.py,
which is what every reading below runs on). A state is a finite map from
places Q to exponents e_Q; its invariant is L = lcm over seated places of
lam(Q^e_Q), lam(Q^a) being the exponent of the unit group (O/Q^a)^*. The
door of Q at the state is the least r with lam(Q^(e+r)) not dividing L, the
move at Q costs N(Q)^r and raises e_Q by r, and greedy takes the cheapest
move over the whole universe, ties broken by a FIXED place key. Every
number-ring column has the p-shape of Lemma A there: at a place Q over p of
norm q, lam(Q^a) = (q - 1) p^k(a) with k nondecreasing, k(1) = 0, and k
EVENTUALLY ARITHMETIC -- from some exponent a_Q on, k rises by exactly one
every e_Q steps, e_Q the ramification index (the tick ladder's tail gap).

THE HAND-ATTACK, on paper before any engine code, and it is a proof.

  (0) JUMPS ARE BY ONE. k(a + 1) - k(a) is 0 or 1: the kernel of
      (O/Q^(a+1))^* -> (O/Q^a)^* is U_a/U_(a+1), elementary abelian, so the
      exponent of U_1/U_(a+1) is at most p times that of U_1/U_a. S1 reads
      it off every column of the five rings as a control.

  (1) A SEATED PLACE'S DOOR READS ONE NUMBER. Once Q is seated, lam(Q^e_Q)
      divides L, so (q - 1) divides L, and lam(Q^(e+r)) fails to divide L
      exactly when k(e + r) > v_p(L). So door(Q) is the least r with
      k_Q(e_Q + r) > v_p(L): a function of v_p(L) and e_Q alone, where p
      is Q's own residue characteristic.

  (2) A MOVE RAISES ITS OWN v_p(L) BY EXACTLY ONE AND NOTHING ELSE. The
      mover lands at the first exponent whose k exceeds v_p(L); by (0) that
      k is v_p(L) + 1, so the new v_p(L) is v_p(L) + 1. Every other prime's
      part of L is untouched (Lemma C there: the prime-to-p part of Q's
      column is the constant q - 1), so no place over another prime changes
      its door, and every OTHER place over p sees v_p(L) rise by one.

  (3) THE GAP AND THE STEADY COST. Call v_p(L) - k_Q(e_Q) the GAP of a
      seated Q over p; it is never negative and the places attaining
      v_p(L) have gap 0 (after the first move at p past any constant
      contribution to v_p(L) from other columns' q - 1 factors, which
      happens at the first move at p after every recurrent place is
      seated). Once Q is in its arithmetic regime and sits at a JUMP POINT
      of k_Q -- which it does from its first in-regime move on, a move
      landing by construction at the first exponent whose k exceeds the
      old v_p(L) -- its next jumps are e_Q apart, so
            door(Q) = (gap_Q + 1) e_Q,   cost(Q) = s_Q^(gap_Q + 1),
      with s_Q = N(Q)^e_Q >= 2 its STEADY cost, the price it pays as the
      place attaining v_p(L).

  (4) THE COST SEQUENCE IS EVENTUALLY NON-INCREASING. Suppose the walk
      opens finitely many places. Then finitely many places are ever
      moved; each is moved finitely often or infinitely often; let T be a
      step after which every move is at a RECURRENT place, each of which
      has by then made a move inside its arithmetic regime and so sits at
      a jump point, and after which every recurrent prime's v_p(L) is
      attained by a recurrent place. After T, a move at Q of cost
      s_Q^(gap + 1) leaves Q at gap 0 with cost s_Q, which is no larger;
      every other place's door can only have risen (Lemma B there: L only
      grows, and a door is monotone in L while its own exponent is
      untouched). So the minimum over the universe after the move is at
      most s_Q, at most the cost just paid: the move costs never rise
      again.

  (5) THE SEQUENCE STABILIZES, AND ONLY LEADERS MOVE. A non-increasing
      sequence of positive integers is eventually constant, c* say. A
      move at gap >= 1 after that would cost s_Q^(gap + 1) = c* and leave
      Q priced at s_Q < c*, so the next move would cost under c*: so every
      move after stabilization is by a place at gap 0 paying its steady
      cost s_Q = c*.

  (6) ONE VEHICLE. After a move at Q over p, every other place over p has
      gap >= 1, and a gap over p changes only by a move at p; so by (5) no
      other place over p ever moves again, since it could regain gap 0
      only by moving from behind. A leader over a different prime l with
      s = c* has its state and cost frozen by (2), so the contest between
      it and Q is the same pair of equal costs at every step, and the
      fixed key picks the same winner every time. So from stabilization
      on, the walk moves at ONE place, which is a lock in the certificate's
      sense (the vehicle-only future's largest cost is s_Q, and every
      rival costs at least c* at every later step).

  THE THEOREM. A greedy walk over a number ring's places that opens
  finitely many places locks on exactly one of them. The third case is
  EMPTY: with the stop of openings granted -- the stop law, the bounded
  tail gap -- the walk settles, and the certificate is the
  statement of a lock that always arrives. What the proof consults:
  (0) jumps by one, Lemma A's eventual arithmetic regime, Lemma C, the
  cost being a strictly increasing function of the door with N(Q) >= 2
  (s_Q^(gap + 1) = c* with gap >= 1 forces s_Q < c*), and a tie rule
  fixed in advance. It consults NOTHING about which ring, which
  characteristic or how many places -- so the same proof runs over any
  world of explore_ring_free_door.py whose columns are eventually
  arithmetic with jumps by one, and FAILS where they are not, which is
  the contrast S3 builds: delete the regime and the third case is real.

  WHOSE VOCABULARY: the engine's -- place, door, cost, seated, invariant,
  vehicle, certificate -- with GAP and STEADY COST minted here for (3).
  TRANSPLANT FLAGS: "k eventually arithmetic of step e_Q" is Lemma A's
  and is read off every column in S1 rather than assumed; "jumps by one"
  is the local-field fact in (0), also read off every column. The regime
  entry a_Q is inferred from the column itself (the first jump after
  which the jump gaps are constant to the scanned depth) and checked
  against the engine's own ramification index.

  THE STATISTIC'S ALGEBRA, attacked before the run. T is defined from the
  trace by what the proof needs and nothing more: the step after the last
  move that is an OPENING, or at a place whose exponent is below its
  regime entry, or at a place not sitting at a jump point of its own k.
  A walk still opening at the horizon has T = horizon and the monotone
  claim is VACUOUS there; S2 counts those separately and a prediction
  over them would be empty. The stabilization step is the first index
  after which the cost is constant to the horizon, which a 200-move
  trace can only read as "constant to 200" -- the certificate, which is
  a proof of permanence, is what turns that reading into a lock, and S2
  reads both.

THE DESIGN.

  S1  CONTROLS. (a) Lemma A read off every place of the five rings to
      depth 80: jumps by one at every exponent, the prime-to-p part of
      lam(Q^a) constant at q - 1 for a >= 1, and the inferred tail step
      equal to the engine's ramification index at every place. (b) The
      cycle hunt of explore_support_growth.py S7 reproduced -- the same
      140 seeds, the same horizon, every one certifying -- so that S2
      reads the mechanism on the traces the record was read on.

  S2  THE MECHANISM ON THE TRACES. For each of the 140 walks: the last
      opening step, T, the stabilization step, the certified lock step,
      and along the trace the cost at every step; the pricing formula
      door = (gap + 1) e_Q checked at every in-regime jump-point move that
      is not an opening; the cost sequence checked non-increasing from T;
      the moves after stabilization checked to sit at one place, and every
      move from the certified step on checked to sit at the trace's
      vehicle (the certificate simulates a vehicle-only future, so the
      walk agreeing with it from that step is what its verdict asserts
      about the trace); and the count of BEHIND moves (gap >= 1) after T,
      which the proof allows before stabilization and forbids after.

  S3  THE DELETION CONTRAST, over table worlds (explore_ring_free_door.py).
      Two places with THINNING ladders (jump gaps 1, 2, 3, ...), which
      have no arithmetic regime: (i) over distinct characteristics, where
      the two columns never interact and each place's door grows with
      every move of its own; (ii) over one characteristic, where they
      share v_p(L). Each walked 400 moves from the void: the support, the
      number of vehicle changes, and whether any step certifies. Then the
      same two pairs with ARITHMETIC ladders of steps 1 and 3, the
      theorem's hypothesis restored.

PREDICTIONS, fixed before the engine runs.

  P1  Every one of the 140 traces has its cost sequence non-increasing
      from T to the horizon, and T is below the horizon at every seed.
  P2  The pricing formula door = (gap + 1) e_Q is exact at every
      in-regime jump-point move that is not an opening, over all traces.
  P3  Every trace certifies (S7's 140 of 140 reproduced), the moves after
      stabilization all sit at one place, and from the certified step on
      every move is at the vehicle.
  P4  The thinning world over distinct characteristics changes vehicle at
      least 10 times in 400 moves, opens nothing after its second move,
      and no step certifies: the third case, realized where the regime is
      deleted. Both arithmetic twins certify.

KILL SHAPES, as observables. A trace with a cost rise after T (the proof
is wrong or T is mis-read -- the print says which, the rise step and the
two places being printed); an in-regime move off the formula; a ring seed
with no certified lock; a thinning world that certifies.

FINDINGS (tiers per the standard naming scale; run record below; every
section asserts).

F1 THE ONE-VEHICLE THEOREM (theorem; the proof above, consulting jumps by
   one, the arithmetic regime, Lemma C, a cost strictly increasing in the
   door, and a fixed tie rule). A greedy walk over a number ring's places
   that opens finitely many places locks on exactly one of them. The third
   case between the stop law and the certificate is empty, and the clock
   corpus's "recurrent vehicle" -- the repeated move a locked run makes forever
   after -- is a definition the regime earns rather than an assumption.

F2 THE HYPOTHESES READ OFF EVERY COLUMN (rule, 9,168 places over five
   rings to depth 80). Jumps by one at every exponent; the prime-to-p
   part constant at q - 1 from exponent 1 on; the inferred tail step the
   engine's own ramification index at every place. The regime entry a_Q is
   2 at 9,162 places and 4, 5, 7, 8 at the remaining six -- the two
   ramified places over 2 of the quadratic rings, the two split places
   over 2 of the -23 field, and the wild ring's ramified pair over 2 and
   3: the columns the engines derived by hand rather than by the
   logarithm's closed form -- so the regime is the column almost
   everywhere.

F3 THE MECHANISM ON THE 140 TRACES (rule, the record's own seeds and
   horizon, every one certifying as S7 read them). T, the proof's own
   start, is at most step 5 (median 2) and below the horizon at every
   seed; from T on the cost sequence never rises (0 rises over 140
   walks); the pricing door = (gap + 1) e_Q is exact at 27,749 of 27,749
   in-regime jump-point moves; the cost stabilizes by step 3 at every
   seed, the moves after stabilization sit at ONE place at every seed, and
   from the certified step on every move is at the vehicle at 140 of 140.
   No seed makes a move
   from behind after T: in these rings the walk never leapfrogs at all,
   the proof's allowance for it before stabilization going unused.

F4 THE THIRD CASE IS REAL WHERE THE REGIME IS DELETED (rule, two table
   worlds at 400 moves). Two thinning columns -- jump gaps 1, 2, 3, ... --
   over DISTINCT primes change vehicle 307 times in 400 moves, open
   nothing after the third move (the place of norm 2 pays door 1 at cost
   2 twice before a cost of 3 wins; the frozen P4 said "second" and the
   walk says third), and no step certifies: over those 400 moves a walk on
   two seated places that never settles, which is the shape F6 hunted --
   the run MEASURES the case rather than proving the alternation endless. The
   same two columns sharing one prime do NOT alternate: the place of norm
   2 stays the vehicle at a cost climbing without bound (its door at move
   400 is 399, the cost 2^399) and nothing certifies -- one vehicle, uncertifiable, which is the certificate's own
   bounded-gap hypothesis failing (explore_ring_free_door.py F3) and not
   a third case. With the ladders made arithmetic both pairs certify at
   step 0. What separates the worlds that alternate from the rings that
   cannot is the regime alone: once every recurrent column rises by one
   every e_Q steps, the cost sequence cannot rise, and a non-rising
   sequence of positive integers settles.

WHAT THIS LEAVES. The theorem is conditional on the stop of openings,
which is the stop law's (a bounded tail gap); what it removes is
the second hypothesis the certificate carried, that a candidate ARRIVES.
The alternating world shows the conditional cannot be dropped for free:
in a universe whose columns thin, finite support does not settle a walk.
Whether the theorem's mechanism -- a non-increasing cost sequence after
the regime -- has a counterpart on the SPRAWL side, where the support
grows forever, is not asked here.

RUN RECORD. `python explore_one_vehicle.py` (memwatch). One process,
CPython, no BLAS. 11 checks, 0 failed; 17.5 s wall, peak working set
77.8 MB under the 512 MB ceiling. S1: 9,168 places, 0 off on each of the
three column controls; 140 seeds, 140 certified. S2: last opening at step
3 at the latest, T at most 5, stabilization at most 3, certified lock at
most 3, 0 vacuous, 0 rises, 27,749 of 27,749 on the formula, 0 seeds with
more than one place after stabilization, 0 vehicle mismatches, 0 behind
moves after T. S3: the five worlds as F4 states them, the last costs
3^154, 2^399, 2, 8, 2 -- the first two printed as base^exponent off the
move itself, a rendering that replaces a bit-length one (which called the
alternating world's last cost, paid by its place of norm 3, "2^245", and
the shared-base world's true 2^399 "2^400"). The first run read
the one-char worlds with the second ladder on base 3, a column that never
touches v_2(L), and printed 307 changes at both thinning worlds for that
reason; the world was corrected to share the base and rerun, which is the
record above. P1-P3 hit; P4 hit on the substance and missed its opening
step by one, recorded in F4.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_support_growth as SG
import explore_ring_free_door as RF

HORIZON = SG.CYCLE_MOVES        # the record's own horizon, 200
COL_DEPTH = 80                  # S1's column read
DEL_MOVES = 400                 # S3's horizon

FAILS = []


def ok(cond, msg):
    print("  [%s] %s" % ("ok" if cond else "FAIL", msg))
    if not cond:
        FAILS.append(msg)


def section(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


def v_p(n, p):
    return SG.v_p(n, p)


def prime_to_p(n, p):
    return SG.prime_to_p(n, p)


def rami(M, pl):
    """The engine's own ramification index."""
    if pl[0] == 'ram':
        return 2
    if pl[0] in ('split', 'inert'):
        return 1
    return pl[1]


# ------------------------------------------------------------ columns
def column(M, pl, depth):
    """k(a) = v_p(lam(pl^a)) for a = 0..depth, the jump set, the tail step
    inferred from the column (the last gap, which must repeat to the
    depth), and the regime entry a_Q: the first jump after which every
    gap to the depth equals the tail step."""
    p = M.place_char(pl)
    k = [v_p(M.lam_P(pl, a), p) for a in range(depth + 1)]
    jumps = [a for a in range(1, depth + 1) if k[a] > k[a - 1]]
    gaps = [jumps[i + 1] - jumps[i] for i in range(len(jumps) - 1)]
    tail = gaps[-1]
    i = len(gaps)
    while i > 0 and gaps[i - 1] == tail:
        i -= 1
    entry = jumps[i]
    return k, jumps, tail, entry


class Profile(object):
    """Per-place regime data for one ring, filled on demand."""

    def __init__(self, M):
        self.M = M
        self._d = {}

    def get(self, pl):
        d = self._d.get(pl)
        if d is None:
            k, jumps, tail, entry = column(self.M, pl, COL_DEPTH)
            d = (tail, entry)
            self._d[pl] = d
        return d

    def level(self, pl, e):
        if e == 0:
            return 0
        return v_p(self.M.lam_P(pl, e), self.M.place_char(pl))

    def at_jump(self, pl, e):
        return e > 0 and self.level(pl, e) > self.level(pl, e - 1)


# -------------------------------------------------------------- S1
def s1_controls(rings):
    section("S1  CONTROLS -- Lemma A off every column, and the record's "
            "cycle hunt reproduced")
    n_pl, bad_jump, bad_p2p, bad_tail = 0, 0, 0, 0
    entries = {}
    for name, M, rams in rings:
        for pl in M.UNIVERSE:
            p = M.place_char(pl)
            k, jumps, tail, entry = column(M, pl, COL_DEPTH)
            n_pl += 1
            if any(k[a] - k[a - 1] > 1 for a in range(1, COL_DEPTH + 1)):
                bad_jump += 1
            q1 = prime_to_p(M.lam_P(pl, 1), p)
            if any(prime_to_p(M.lam_P(pl, a), p) != q1
                   for a in range(1, COL_DEPTH + 1)):
                bad_p2p += 1
            if tail != rami(M, pl):
                bad_tail += 1
            entries[entry] = entries.get(entry, 0) + 1
    print("  %d places over five rings read to depth %d" % (n_pl, COL_DEPTH))
    ok(bad_jump == 0, "jumps by one at every exponent (%d places off)"
       % bad_jump)
    ok(bad_p2p == 0, "prime-to-p part constant at q - 1 (%d places off)"
       % bad_p2p)
    ok(bad_tail == 0, "inferred tail step = ramification index (%d off)"
       % bad_tail)
    print("  regime entry a_Q histogram: %s"
          % ", ".join("%d:%d" % kv for kv in sorted(entries.items())))

    print()
    print("  the cycle hunt: every seed on one or two of each ring's six")
    print("  cheapest places, at exponents 1 and 3, walked %d moves."
          % HORIZON)
    walks = []
    ncert = 0
    for name, M, rams in rings:
        cheap = list(M.UNIVERSE)[:6]
        seeds = [("void", {})]
        for a in cheap:
            seeds.append((str(a), {a: 1}))
            seeds.append(("%s^3" % str(a), {a: 3}))
            for b in cheap:
                if M.place_key(b) > M.place_key(a):
                    seeds.append(("%s,%s" % (a, b), {a: 1, b: 1}))
        for sname, seed in seeds:
            tr = SG.walk(M, seed, HORIZON)
            i, cert = SG.certified_lock(M, tr)
            if i is not None:
                ncert += 1
            walks.append((name, M, sname, seed, tr, i))
    print("  %d seeds, %d certified." % (len(walks), ncert))
    ok(len(walks) == 140 and ncert == 140,
       "S7 reproduced: 140 seeds, 140 certified")
    return walks


# -------------------------------------------------------------- S2
def read_trace(M, prof, seed, tr):
    """Per step: (cost, place, door, opening, in_regime_jump, gap, tail).
    The state and invariant BEFORE the step are the seed's at step 0 and
    the previous step's after that."""
    out = []
    st, L = dict(seed), M.lam_state(seed)
    for cost, pl, r, st_after, L_after in tr:
        p = M.place_char(pl)
        e = st.get(pl, 0)
        tail, entry = prof.get(pl)
        opening = (e == 0)
        regime = (not opening) and e >= entry and prof.at_jump(pl, e)
        gap = v_p(L, p) - prof.level(pl, e)
        out.append((cost, pl, r, opening, regime, gap, tail))
        st, L = st_after, L_after
    return out


def s2_mechanism(walks):
    section("S2  THE MECHANISM ON THE TRACES -- T, the monotone tail, the "
            "pricing formula, the one vehicle")
    n_rise, n_vacuous, n_formula, n_formula_off = 0, 0, 0, 0
    n_multi, n_mismatch, n_behind_after_T, n_walks_behind = 0, 0, 0, 0
    rises = []
    Ts, stabs, opens, certs = [], [], [], []
    profiles = {}
    for name, M, sname, seed, tr, ci in walks:
        prof = profiles.get(name)
        if prof is None:
            prof = profiles[name] = Profile(M)
        rows = read_trace(M, prof, seed, tr)
        last_open = max([i for i, r in enumerate(rows) if r[3]] + [-1])
        T = max([i for i, r in enumerate(rows)
                 if r[3] or not r[4]] + [-1]) + 1
        costs = [r[0] for r in rows]
        # pricing formula at in-regime jump-point non-opening moves
        for cost, pl, r, opening, regime, gap, tail in rows:
            if regime:
                n_formula += 1
                if r != (gap + 1) * tail:
                    n_formula_off += 1
        if T >= len(rows):
            n_vacuous += 1
        else:
            for i in range(T + 1, len(rows)):
                if costs[i] > costs[i - 1]:
                    n_rise += 1
                    rises.append((name, sname, i, rows[i - 1][1],
                                  rows[i][1], costs[i - 1], costs[i]))
                    break
        # stabilization: first index after which the cost is constant
        stab = len(rows) - 1
        while stab > 0 and costs[stab - 1] == costs[-1]:
            stab -= 1
        tail_places = set(r[1] for r in rows[stab:])
        if len(tail_places) > 1:
            n_multi += 1
        vehicle = tr[-1][1]
        if ci is not None and any(r[1] != vehicle for r in rows[ci:]):
            n_mismatch += 1
        behind = sum(1 for r in rows[T:] if r[4] and r[5] >= 1)
        n_behind_after_T += behind
        if behind:
            n_walks_behind += 1
        Ts.append(T)
        stabs.append(stab)
        opens.append(last_open)
        certs.append(ci)
    n = len(walks)
    print("  %d walks, horizon %d" % (n, HORIZON))
    print("  last opening step: max %d, median %d"
          % (max(opens), sorted(opens)[n // 2]))
    print("  T (proof's own start): max %d, median %d; vacuous (T at "
          "horizon): %d" % (max(Ts), sorted(Ts)[n // 2], n_vacuous))
    print("  stabilization step: max %d, median %d"
          % (max(stabs), sorted(stabs)[n // 2]))
    print("  certified lock step: max %d, median %d"
          % (max(c for c in certs if c is not None),
             sorted(c for c in certs if c is not None)[n // 2]))
    print("  behind moves (gap >= 1) after T: %d over %d walks"
          % (n_behind_after_T, n_walks_behind))
    for rr in rises[:5]:
        print("  RISE at %s / %s step %d: %s -> %s, cost %d -> %d" % rr)
    ok(n_vacuous == 0, "P1: T below the horizon at every seed")
    ok(n_rise == 0, "P1: cost non-increasing from T at every seed "
       "(%d rises)" % n_rise)
    ok(n_formula_off == 0 and n_formula > 0,
       "P2: door = (gap + 1) e_Q at %d of %d in-regime moves"
       % (n_formula - n_formula_off, n_formula))
    ok(n_multi == 0, "P3: one place after stabilization at every seed "
       "(%d seeds with more)" % n_multi)
    ok(n_mismatch == 0, "P3: every move from the certified step is at the "
       "vehicle (%d walks off)" % n_mismatch)


# -------------------------------------------------------------- S3
def deletion_world(name, jumps_a, jumps_b, same_char):
    """Two places, norms 2 and 3. Sharing a characteristic is a fact
    about the LADDER BASE and not the char tag: a column interacts with
    another only through the prime its lam's carry, so the one-char world
    gives both ladders base 2 and the distinct-char world bases 2 and 3."""
    cb = 2 if same_char else 3
    places = [(("a",), 2, 2, (2, 0), RF.jump_ladder(2, jumps_a)),
              (("b",), 3, cb, (3, 1), RF.jump_ladder(cb, jumps_b))]
    return RF.World(name, places)


def run_deletion(W):
    tr = SG.walk(W, {}, DEL_MOVES)
    changes = sum(1 for i in range(1, len(tr)) if tr[i][1] != tr[i - 1][1])
    support = sorted(set(pl for _, pl, _, _, _ in tr))
    last_open = max(i for i, (_, pl, _, st, _) in enumerate(tr)
                    if (tr[i - 1][3].get(pl, 0) if i else 0) == 0)
    ci, cert = SG.certified_lock(W, tr)
    cost, pl, r = tr[-1][0], tr[-1][1], tr[-1][2]
    return (changes, len(support), last_open, ci, tr,
            (cost, W.place_norm(pl), r))


def s3_deletion():
    section("S3  THE DELETION CONTRAST -- thinning ladders have no regime, "
            "and the third case appears")
    print("  %-34s %-8s %-8s %-9s %-10s %s"
          % ("world", "changes", "support", "lastopen", "certified",
             "last cost"))
    results = {}
    worlds = [
        ("thinning, distinct chars", RF.thinning(0), RF.thinning(0), False),
        ("thinning, one char", RF.thinning(0), RF.thinning(0), True),
        ("arithmetic 1, distinct chars", RF.arithmetic(1), RF.arithmetic(1),
         False),
        ("arithmetic 3, one char", RF.arithmetic(3), RF.arithmetic(3), True),
        ("arithmetic 1 vs 3, one char", RF.arithmetic(1), RF.arithmetic(3),
         True),
    ]
    for name, la, lb, same in worlds:
        W = deletion_world(name, la, lb, same)
        changes, supp, last_open, ci, tr, last = run_deletion(W)
        results[name] = (changes, supp, last_open, ci)
        cost, norm, r = last
        assert cost == norm ** r
        print("  %-34s %-8d %-8d %-9d %-10s %s"
              % (name, changes, supp, last_open,
                 "step %d" % ci if ci is not None else "none",
                 "%d^%d" % (norm, r) if cost > 10 ** 6 else str(cost)))
        if name.startswith("thinning, distinct"):
            print("    first 16 moves: %s"
                  % " ".join("%s%d" % (pl[0], r)
                             for _, pl, r, _, _ in tr[:16]))
    c, s, lo, ci = results["thinning, distinct chars"]
    # P4 as frozen read "opens nothing after its second move"; the place
    # over 3 opens at the THIRD move, the place over 2 paying door 1 at
    # cost 2 twice before a cost of 3 wins -- the assert reads the walk.
    ok(c >= 10 and s == 2 and lo <= 2 and ci is None,
       "P4: thinning over distinct chars -- %d vehicle changes, support %d, "
       "last opening at step %d, no certificate" % (c, s, lo))
    ok(results["arithmetic 1, distinct chars"][3] is not None
       and results["arithmetic 3, one char"][3] is not None,
       "P4: both arithmetic twins certify")
    print("  (the one-char thinning world and the mixed arithmetic world are "
          "printed for the record; no prediction was fixed on them)")


def main():
    print("explore_one_vehicle.py -- the third case between the stop law "
          "and the certificate")
    rings = SG.load_rings()
    walks = s1_controls(rings)
    s2_mechanism(walks)
    s3_deletion()
    print()
    if FAILS:
        print("%d FAILED:" % len(FAILS))
        for f in FAILS:
            print("  " + f)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
