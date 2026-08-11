r"""explore_late_seating.py -- CAN THE MENU'S MINIMUM RISE PAST AN UNSEATED
RAMIFIED DOOR? The unproved half of the cheapest-opening law, attacked from
both sides.

THE QUESTION. The clock corpus files, as a rule in range over three rings:
a ramified place is seated from the void ONLY as the cheapest opening. Half
is argued -- an unseated place's cost is nondecreasing as the invariant
grows (explore_support_growth.py Lemma B), so a place that loses the
opening never gets cheaper. The other half is open: that the menu's own
minimum cannot RISE past a stalled unseated door. If it can, greedy seats
the ramified place mid-walk and the law's three specimens were a scope
accident. This file attacks both directions: prove the missing half where
it is provable, and hunt a ring where it is false.

WHOSE VOCABULARY. "The menu min rises" is the SCHEDULE's phrase; a ring's
min is a concrete number the engine prints per step. Everything below is
stated as engine observables: door_r(pl, e, L) = the least r >= 1 with
lam_P(pl, e+r) not dividing L; a move at pl costs norm(pl)^r; greedy takes
the menu minimum, first tie member. These conventions are re-derived from
the three ring engines (explore_number_field_lock.py,
explore_module_law.py, explore_gaussian_runaway.py), not from memory.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 The instant-lock induction below assumes the void winner's lambda
    column climbs strictly at every depth -- split/inert vocabulary. A
    ramified column PLATEAUS (Z[i]'s wild place: 1, 2, 4, 4, ...), so the
    induction's hypothesis is exactly where the two halves part; the
    winner's KIND is the boundary, not a leak.
 T2 The odd-ramified lambda columns at the two minted rings (d = -6, -30)
    are hand-modelled on the 2-adic plateau shape (Z[i], Z[sqrt(-5)]).
    Q_3(sqrt(-30)) = Q_3(sqrt(-3)) contains mu_3, so a 3-torsion plateau is
    likely and the hand walk's step count may be off by the plateau's
    width. The brute-forcer (explore_gaussian_runaway.unit_exponent, run
    on the actual residue rings) is the authority; PR4's kill names this
    transplant dying.
 T3 "Late seating" is the VOID claim's phrase. A seeded walk has no
    cheapest opening, so seeded events answer a DIFFERENT sentence -- can a
    fuller invariant hand a ramified place the menu? -- and are reported
    apart, never as kills of the void law.

THE HAND-ATTACK, on paper before any engine code.

 A. THE REDUCTION. Greedy pays the menu minimum every step, so an unseated
    place is seated exactly at a step where its cost IS the minimum. Its
    cost is nondecreasing (Lemma B); past the lock the paid price is flat.
    So a post-lock seating needs a stalled cost meeting a flat minimum --
    a tie, decided by tie-break -- and the strict danger window is the
    TRANSIENT, which is finite. The open half is a transient question.

 B. THE INSTANT-LOCK INDUCTION (the provable half). Suppose the void's
    step-1 winner P0 is split or inert, norm n0. At the void L = 1 and
    lam_P(P0, 1) >= 2 does not divide 1, so the door is 1 and the opening
    costs n0. Thereafter, while the walk only deepens P0, L = lam_P(P0, e)
    and lam_P(P0, e+1) = p * lam_P(P0, e) never divides L: the door stays
    1 and the menu min stays n0 FOREVER. Every rival lost the void menu at
    cost >= n0 and is nondecreasing (Lemma B), so no rival is ever
    strictly below the min: the walk seats exactly one place, and the menu
    minimum never rises at all. The only escape is a TIE at exactly n0 at
    the void -- the cheapest-opening tie. This proves the missing half
    whenever the void winner is unramified.

 C. THE ESCAPE (where the void winner is ramified). A ramified column
    plateaus, so the winner's own door widens mid-walk and the paid price
    CLIMBS (Z[i] from the void pays 4, 2, 2, then 8). A climbing min can
    cross a second unseated ramified place's stalled cost -- Z[i] has no
    second cheap ramified place, but a ring can be MINTED with several:
    d = -30 ramifies 2, 3 and 5 at norms 2, 3, 5, with the least
    unramified norm 11 (split primes need (-30|p) = 1). Hand walk, on the
    hand-modelled columns (T2): the void seats R3 at 3 (lam(R3,1) = 2
    fails to divide 1); deepening R3 stays cheap until its pump widens the
    door to cost 9; meanwhile R5's cost is PINNED at 5 -- lam(R5, a)
    carries v_2 = 2 at every a while v_2(L) = 1, since the only cheap
    v_2-feeders are R2 (priced 8: door 3 at v_2(L) = 1) and split places
    (norms >= 11) -- so the first time R3's recurrent price exceeds 5,
    R5 is FORCED onto the menu minimum: a second ramified place, seated
    from the void, NOT the cheapest opening. The unproved half would be
    FALSE in general, and the filed law's true content the winner-kind
    dichotomy of B.

 D. THE SEEDED LEVER (the walked rings, T3). A seed's lambda factors
    (p - 1) feed the ODD parts of L, widening split doors while an odd
    ramified place's cost reads only v_2(L). At Z[sqrt(-5)], seed
    P3 * P7 (both split): L = lcm(2, 6) = 6; deepening P3 has door 2
    (lam(P3, 2) = 6 divides L), cost 9; deepening P7 costs 7; the fresh
    conjugates are walled (door >= 2); and R5 -- lam(R5, 1) = 4, which
    does not divide 6 -- has door 1, cost 5: an UNPLANTED ramified place
    takes the very first move of a ram-free seeded walk. If the engines
    agree, the void law does not survive planting even a two-place seed,
    and the mechanism is named: the invariant's odd growth outruns its
    2-adic growth.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 IMPORTED-WALKER CONTROL. The void walks of the three filed rings
    through explore_lock_budget's walker reproduce the filed facts:
    Z[sqrt(-5)] and Z[w] lock on a split place of norm 3 at cost 3 having
    seated exactly one place; Z[i]'s first move seats its ramified place
    at cost 4 and the walk locks on the inert place of norm 9. PRINTS:
    per ring, the walk table. KILL: any mismatch.

PR2 MODULE-MAKER CONTROL. The quadratic-ring factory below, instantiated
    at (T, N0) = (0, -5) and (0, -1), reproduces the host engines' own
    lambda tables at every ramified cell inside brute range and the
    split/inert closed forms, and agrees with door_r at sampled states.
    PRINTS: the compared cells. KILL: one disagreeing cell.

PR3 MONOTONE. Across every trajectory recorded in this file, an unseated
    place's cost never falls while it stays unseated (Lemma B's shape, in
    situ). PRINTS: pairs checked, violations. KILL: one violation, which
    would break the reduction A and not just a prediction.

PR4 THE VOID LATE SEATING. The d = -30 void walk seats a SECOND ramified
    place -- the hand walk names R5 at cost 5 within the first handful of
    moves (step count soft under T2) -- while the void walks of
    Z[sqrt(-5)], Z[w], Z[i] and d = -6 seat no ramified place past step 1.
    PRINTS: per ring, every fresh seating with its step and cost, and per
    step the margin (least unseated-ramified cost minus paid). KILL: no
    second-ramified seating at d = -30 inside 40 moves.

PR5 THE INDUCTION, CHECKED. At the rings here whose void winner is split
    or inert (Z[sqrt(-5)], Z[w]), the void walk seats exactly one place in
    40 moves, pays a constant n0 = 3 from step 1 on, and the winner's
    column climbs strictly to depth 20 (so its door is 1 at every reached
    depth). PRINTS: the paid sequence and the column. KILL: a second
    seating, a paid change, or a non-climbing cell.

PR6 THE SEEDED LEVER. At Z[sqrt(-5)], the ram-free seed P3 * P7 seats the
    ramified place over 5 at cost 5 on its very first move. Across the
    ram-free seed sweep (seed norm <= 40) at all five rings, the rig
    prints every unplanted-ramified seating. KILL: the P3 * P7 walk's
    first move is not that seating.

FINDINGS, entered after the run from printed output. All six predictions
landed; both controls clean.

F1 THE WINNER-KIND DICHOTOMY (rule, proved; premises machine-checked).
   When the void's step-1 winner is split or inert, the walk seats exactly
   one place EVER: the winner's column climbs strictly (checked to depth
   21 at both rings), so its door is 1 and the menu minimum is a constant
   n0 from step 1 on, while every rival lost the void menu at >= n0 and is
   nondecreasing (Lemma B, re-verified in situ: 1,338,247 consecutive
   unseated-cost pairs across every trajectory here, 0 violations). The
   missing half of the cheapest-opening law is PROVED on this side, up to
   a void tie at exactly n0. K5 and K23 print flat paid 3, one seating.

F2 THE UNPROVED HALF IS FALSE IN GENERAL (rule in range; the witness is
   one ring, the mechanism proved at its cells). Z[sqrt(-30)] -- ramified
   at 2, 3, 5, least split norm 11 -- seats a SECOND ramified place from
   the void: paid runs 3 3 5 5 17 ..., R3 is the cheapest opening at 3,
   and R5 is seated at step 3 at cost 5, exactly the hand walk. The
   mechanism is the pinning the hand-attack named: v_2(lam(R5, a)) = 2 at
   every depth while v_2(L) = 1 until something of norm >= 8 is bought,
   so R5's cost is stuck at 5 while the ramified winner's plateau pushes
   the minimum past it. A ramified void winner generically hands the walk
   a CLIMBING transient -- Z[sqrt(-6)] climbs 3 3 5 and seats a split
   place late the same way -- and one cheap ramified place can catch
   another. The filed law's true content is F1's dichotomy, not a general
   impossibility; its three rings were safe by winner kind (K5, K23) or
   by having no second cheap ramified place (Z[i]).

F3 THE SEEDED LEVER IS GENERIC (observation sweep; a different sentence
   from the void law, flag T3). Ram-free generator-product seeds hand
   unplanted ramified places the menu at 8 of 19 K5 seeds (R5 at cost 5,
   the P3*P7 lever exact), 1 of 77 K23 seeds (inert Q5 makes L = 24 and
   R23 walks in at 23), and 10 of 14 QM30 seeds; 0 at Z[i] and
   Z[sqrt(-6)]. The mechanism prints as the hand-attack's: a seed's
   lambda factors feed the odd part of L faster than its 2-part, widening
   split doors while an odd ramified door reads only v_2(L).

F4 INCIDENTAL: QM30's void walk locks at the split place of norm 17 at
   cost 17 -- not its least split norms 11 and 13, both walled at the
   lock era: 10 and 12 divide the invariant 60 while 16 at norm 17
   escapes, the same 2-adic pinning as F2. The corpus's locks at 3 and 9
   were never a smallest-norm law, and this ring prints the separation.

RUN RECORD. One process, CPython, no BLAS; the walker imported from
explore_lock_budget.py, the exact-exponent brute-forcer from
explore_gaussian_runaway.py run on the minted rings' actual residue
rings (cells to 200,000 residues). 458 checks green. Under memwatch:
peak working set 24.2 MB, peak commit 18.3 MB against the 512 MB
ceiling, wall 2.0 s; a second bare run printed identically. (Universe
truncation checked harmless in review: the minted universes enumerate
rational primes to 61 only, and the max menu minimum over every recorded
walk -- void and seeded, all five rings -- is 25, below the norm of any
absent place, so no truncated place could ever have undercut a menu.)
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_gaussian_runaway as ZI      # Z[i] module + the brute-forcer
import explore_lock_budget as LB           # the imported walker
import explore_module_law as K23           # Z[w], w^2 = w - 6, h = 3
import explore_number_field_lock as K5     # Z[sqrt(-5)], h = 2

CHECKS = 0

NMOVES = 40          # moves per recorded walk
SEED_NORM_CAP = 40   # generator-product seeds by norm, as the image census
BRUTE_CAP = 200_000  # residue-ring size ceiling for the exact exponent
PMAX = 61            # rational primes enumerated into a minted universe
NORM_CAP = 500       # menu guard: no minimum may reach this
DEPTH_CHECK = 20     # depths of the winner column checked for PR5


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def lcm(a, b):
    from math import gcd
    return a // gcd(a, b) * b


def _sieve(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i, f in enumerate(s) if f]


PRIMES = _sieve(PMAX)


# ------------------------------------------------- the quadratic-ring factory
class QRing:
    """A quadratic order Z[t], t^2 = T*t + N0, as a walkable ring module:
    the seven names the imported walker touches (UNIVERSE, place_norm,
    place_key, lam_P, lam_state, door_r, ideal_menu), with the ramified
    lambda columns brute-forced from the actual residue rings
    (explore_gaussian_runaway.unit_exponent) inside BRUTE_CAP and extended
    past it by the pump lam(a) = p * lam(a - 2), the extension asserted
    against the top of the brute window before first use."""

    def __init__(self, name, T, N0):
        self.name, self.T, self.N0 = name, T, N0
        self.disc = T * T + 4 * N0
        self._lam_memo = {}
        self._tail_ok = set()
        self.UNIVERSE = self._build_universe()

    def _build_universe(self):
        places = []
        for p in PRIMES:
            if self.disc % p == 0:
                places.append(('ram', p))
            else:
                rr = [r for r in range(p)
                      if (r * r - self.T * r - self.N0) % p == 0]
                if rr:
                    places.append(('split', p, rr[0]))
                    places.append(('split', p, rr[1]))
                elif p * p <= NORM_CAP:
                    places.append(('inert', p))
        places.sort(key=self.place_key)
        return places

    def place_norm(self, pl):
        return pl[1] * pl[1] if pl[0] == 'inert' else pl[1]

    def place_key(self, pl):
        return (self.place_norm(pl), pl[0], pl[1], pl[2] if len(pl) > 2 else 0)

    def _lam_ram(self, pl, a):
        p = pl[1]
        key = (pl, a)
        if key in self._lam_memo:
            return self._lam_memo[key]
        if p ** a <= BRUTE_CAP:
            v = ZI.unit_exponent(pl, a, self.T, self.N0)
        else:
            if pl not in self._tail_ok:
                top = a - 1
                while p ** top > BRUTE_CAP:
                    top -= 1
                for b in (top, top - 1):
                    assert (self._lam_ram(pl, b)
                            == p * self._lam_ram(pl, b - 2)), \
                        "%s: pump fails at brute depth %d" % (self.name, b)
                self._tail_ok.add(pl)
            v = p * self._lam_ram(pl, a - 2)
        self._lam_memo[key] = v
        return v

    def lam_P(self, pl, a):
        if a == 0:
            return 1
        k, p = pl[0], pl[1]
        if k == 'split':
            return (p - 1) * p ** (a - 1)
        if k == 'inert':
            return (p * p - 1) * p ** (a - 1)
        return self._lam_ram(pl, a)

    def lam_state(self, st):
        L = 1
        for pl, e in st.items():
            L = lcm(L, self.lam_P(pl, e))
        return L

    def door_r(self, pl, e, L):
        r = 1
        while L % self.lam_P(pl, e + r) == 0:
            r += 1
            assert r < 500, "door search runaway"
        return r

    def ideal_menu(self, st, L):
        best, ties = None, []
        for pl in self.UNIVERSE:
            nrm = self.place_norm(pl)
            if best is not None and nrm > best:
                break
            r = self.door_r(pl, st.get(pl, 0), L)
            cost = nrm ** r
            if best is None or cost < best:
                best, ties = cost, [(pl, r)]
            elif cost == best:
                ties.append((pl, r))
        assert best < NORM_CAP, "universe guard: menu minimum at the cap"
        ties.sort(key=lambda t: self.place_key(t[0]))
        return best, ties


QM6 = QRing("Q(sqrt-6)", 0, -6)
QM30 = QRing("Q(sqrt-30)", 0, -30)

RINGS = [("K5", K5, "Z[sqrt(-5)]"),
         ("K23", K23, "Z[w], w^2 = w - 6"),
         ("Zi", ZI, "Z[i]"),
         ("QM6", QM6, "Z[sqrt(-6)]"),
         ("QM30", QM30, "Z[sqrt(-30)]")]


# ------------------------------------------------------ the recorded ring walk
def walk_record(M, seed, nmoves):
    """nmoves greedy steps from the seed. Returns the trajectory as a list
    of (state-before, L-before, cost, place, r)."""
    st = dict(seed)
    L = M.lam_state(st)
    rec = []
    for _ in range(nmoves):
        cost, ties = M.ideal_menu(st, L)
        pl, r = ties[0]
        rec.append((dict(st), L, cost, pl, r))
        st = LB.apply_move(st, pl, r)
        L = M.lam_state(st)
    return rec


def fresh_seatings(rec):
    """[(step, place, cost)] for moves that seat a place (1-based steps)."""
    return [(i + 1, pl, cost)
            for i, (st, L, cost, pl, r) in enumerate(rec)
            if st.get(pl, 0) == 0]


def ram_margins(M, rec):
    """Per step: (paid, least unseated-ramified cost, that place); the cost
    entry is None at steps where every ramified place is already seated."""
    out = []
    for st, L, cost, pl, r in rec:
        best = None
        for q in M.UNIVERSE:
            if q[0] == 'ram' and st.get(q, 0) == 0:
                c = M.place_norm(q) ** M.door_r(q, 0, L)
                if best is None or c < best[0]:
                    best = (c, q)
        out.append((cost, best[0] if best else None,
                    best[1] if best else None))
    return out


# ------------------------------------------------- S1 the module-maker control
def s1_factory_control():
    section("S1  MODULE-MAKER CONTROL -- the factory against two engines "
            "whose tables it did not write (PR2)")
    pairs = [(QRing("ctl-K5", 0, -5), K5), (QRing("ctl-Zi", 0, -1), ZI)]
    for F, M in pairs:
        host = {}
        for pl in M.UNIVERSE:
            host[(pl[0], pl[1]) if pl[0] != 'split' else pl] = pl
        shared = 0
        for pl in F.UNIVERSE:
            key = (pl[0], pl[1]) if pl[0] != 'split' else pl
            if key not in host:
                continue
            hpl = host[key]
            ok(F.place_norm(pl) == M.place_norm(hpl),
               "norm mismatch at %s" % (pl,))
            amax = 1
            while F.place_norm(pl) ** (amax + 1) <= BRUTE_CAP and amax < 12:
                amax += 1
            for a in range(1, amax + 1):
                got, want = F.lam_P(pl, a), M.lam_P(hpl, a)
                ok(got == want, "%s lam(%s,%d): factory %d vs host %d"
                   % (F.name, pl, a, got, want))
            shared += 1
        print("  %s vs host: %d shared places, lambda tables agree on the"
              " brute window" % (F.name, shared))
        for L in (1, 2, 6, 12, 60):
            for pl in F.UNIVERSE[:6]:
                key = (pl[0], pl[1]) if pl[0] != 'split' else pl
                if key not in host:
                    continue
                for e in (0, 1, 2):
                    ok(F.door_r(pl, e, L) == M.door_r(host[key], e, L),
                       "door mismatch %s e=%d L=%d" % (pl, e, L))
        print("  doors sampled at L in {1, 2, 6, 12, 60}, e in {0, 1, 2}:"
              " agree")


# --------------------------------------------- S2 the imported-walker control
def s2_walker_control():
    section("S2  IMPORTED-WALKER CONTROL -- the three filed void walks (PR1)")
    res = {}
    for name, M, desc in RINGS[:3]:
        got = LB.walk_to_lock(M, {})
        ok(got is not None, "%s: no lock witnessed from the void" % name)
        st, L, pl, cost, steps = got
        print("  %-4s %-20s lock at %-8s cost %-4d after %2d moves, state %s"
              % (name, desc, LB.show_place(M, pl), cost, steps,
                 LB.show_state(M, st)))
        res[name] = (st, pl, cost)
    st, pl, cost = res["K5"]
    ok(pl[0] == 'split' and pl[1] == 3 and cost == 3 and len(st) == 1,
       "K5 void: filed lock is one split place of norm 3 at cost 3")
    st, pl, cost = res["K23"]
    ok(pl[0] == 'split' and pl[1] == 3 and cost == 3 and len(st) == 1,
       "K23 void: filed lock is one split place of norm 3 at cost 3")
    st, pl, cost = res["Zi"]
    ok(pl[0] == 'inert' and pl[1] == 3 and cost == 9,
       "Zi void: filed lock is the inert place of norm 9")
    rec = walk_record(ZI, {}, 3)
    ok(rec[0][3][0] == 'ram' and rec[0][2] == 4,
       "Zi void: first move seats the ramified place at cost 4")
    print("  Zi first three paid: %s" % [c for _, _, c, _, _ in rec])


# ------------------------------------------------------- S3 the five void walks
VOID_RECS = {}


def s3_void_walks():
    section("S3  THE FIVE VOID WALKS -- fresh seatings and ramified margins "
            "(PR4, PR5)")
    for name, M, desc in RINGS:
        rec = walk_record(M, {}, NMOVES)
        VOID_RECS[name] = rec
        seat = fresh_seatings(rec)
        marg = ram_margins(M, rec)
        print("\n  %s (%s)" % (name, desc))
        print("    paid:     %s" % " ".join(
            "%d" % c for _, _, c, _, _ in rec[:14]))
        print("    seatings: %s" % "; ".join(
            "step %d: %s cost %d" % (s, LB.show_place(M, pl), c)
            for s, pl, c in seat))
        tight = min((m[1] - m[0], i + 1) for i, m in enumerate(marg)
                    if m[1] is not None) \
            if any(m[1] is not None for m in marg) else None
        if tight is not None:
            print("    tightest unseated-ram margin: %+d at step %d"
                  % tight)
        ram_late = [(s, pl, c) for s, pl, c in seat
                    if pl[0] == 'ram' and s >= 2]
        if name == "QM30":
            ok(len(ram_late) >= 1,
               "PR4: QM30 void seats a second ramified place")
            s, pl, c = ram_late[0]
            print("    LATE RAMIFIED SEATING: step %d, %s, cost %d"
                  % (s, LB.show_place(M, pl), c))
        else:
            ok(len(ram_late) == 0,
               "PR4: %s void seats no ramified place past step 1" % name)
    for name in ("K5", "K23"):
        M = dict((n, m) for n, m, _ in RINGS)[name]
        rec = VOID_RECS[name]
        seat = fresh_seatings(rec)
        ok(len(seat) == 1, "PR5: %s void seats exactly one place" % name)
        paid = [c for _, _, c, _, _ in rec]
        ok(all(c == 3 for c in paid),
           "PR5: %s void pays a constant 3 from step 1" % name)
        P0 = seat[0][1]
        for a in range(1, DEPTH_CHECK + 1):
            ok(M.lam_P(P0, a + 1) % M.lam_P(P0, a) == 0
               and M.lam_P(P0, a + 1) > M.lam_P(P0, a),
               "PR5: %s winner column climbs at depth %d" % (name, a))
        print("  PR5 %s: one seating, flat paid 3, winner column climbs to"
              " depth %d" % (name, DEPTH_CHECK + 1))


# ------------------------------------------------------- S4 the monotone check
def s4_monotone(all_recs):
    section("S4  UNSEATED COSTS ARE NONDECREASING, IN SITU (PR3)")
    pairs = viol = 0
    for M, rec in all_recs:
        last = {}
        for st, L, cost, pl, r in rec:
            for q in M.UNIVERSE:
                if st.get(q, 0):
                    last.pop(q, None)
                    continue
                c = M.place_norm(q) ** M.door_r(q, 0, L)
                if q in last:
                    pairs += 1
                    if c < last[q]:
                        viol += 1
                        print("    VIOLATION: %s falls %d -> %d"
                              % (q, last[q], c))
                last[q] = c
    print("  %d consecutive unseated-cost pairs checked, %d violations"
          % (pairs, viol))
    ok(viol == 0, "PR3: no unseated cost ever falls")


# --------------------------------------------------------- S5 the seeded sweep
def ram_free_seeds(M):
    """Generator-product seeds from split/inert places, seed norm <= cap,
    void excluded."""
    places = [pl for pl in M.UNIVERSE
              if pl[0] != 'ram' and M.place_norm(pl) <= SEED_NORM_CAP]
    seeds = []

    def go(i, st, nrm):
        if st:
            seeds.append(dict(st))
        for j in range(i, len(places)):
            n2 = nrm * M.place_norm(places[j])
            if n2 <= SEED_NORM_CAP:
                st[places[j]] = st.get(places[j], 0) + 1
                go(j, st, n2)
                st[places[j]] -= 1
                if not st[places[j]]:
                    del st[places[j]]

    go(0, {}, 1)
    return seeds


def s5_seeded(all_recs):
    section("S5  THE SEEDED LEVER -- ram-free seeds, every unplanted "
            "ramified seating (PR6)")
    lever_hit = None
    for name, M, desc in RINGS:
        seeds = ram_free_seeds(M)
        events = []
        for seed in seeds:
            rec = walk_record(M, seed, NMOVES)
            all_recs.append((M, rec))
            for s, pl, c in fresh_seatings(rec):
                if pl[0] == 'ram':
                    events.append((seed, s, pl, c))
        print("\n  %-4s %d ram-free seeds (norm <= %d): %d walks seat an"
              " unplanted ramified place"
              % (name, len(seeds), SEED_NORM_CAP,
                 len(set(tuple(sorted((str(k), v) for k, v in e[0].items()))
                         for e in events))))
        for seed, s, pl, c in events[:8]:
            print("      seed %-22s step %2d  %-6s cost %d"
                  % (LB.show_state(M, seed), s, LB.show_place(M, pl), c))
        if len(events) > 8:
            print("      ... %d more" % (len(events) - 8))
        if name == "K5":
            p3 = next(pl for pl in M.UNIVERSE
                      if pl[0] == 'split' and pl[1] == 3)
            p7 = next(pl for pl in M.UNIVERSE
                      if pl[0] == 'split' and pl[1] == 7)
            rec = walk_record(M, {p3: 1, p7: 1}, 1)
            st, L, cost, pl, r = rec[0]
            print("    the lever seed %s: first move %s at cost %d"
                  % (LB.show_state(M, {p3: 1, p7: 1}),
                     LB.show_place(M, pl), cost))
            lever_hit = (pl, cost)
    pl, cost = lever_hit
    ok(pl[0] == 'ram' and pl[1] == 5 and cost == 5,
       "PR6: K5's P3*P7 seed seats the ramified place over 5 at cost 5")


def main():
    all_recs = []
    s1_factory_control()
    s2_walker_control()
    s3_void_walks()
    for name, M, desc in RINGS:
        all_recs.append((M, VOID_RECS[name]))
    s5_seeded(all_recs)
    s4_monotone(all_recs)
    print("\n%d checks green." % CHECKS)


if __name__ == "__main__":
    main()
