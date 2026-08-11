"""explore_opening_law.py -- THE OPENING LAW'S UNPROVED HALF: can the
greedy menu's minimum rise past an unseated ramified place's price?

THE QUESTION. The clock corpus files: A RAMIFIED PLACE IS SEATED FROM THE
VOID ONLY AS THE CHEAPEST OPENING (rule in range, three rings walked).
Half of that is argued -- an unseated place's price never falls while it
stays unseated (explore_support_growth.py Lemma B: the invariant's
divisors only accumulate), so a place that loses the opening never gets
cheaper. The other half is not: nothing proved says the MENU'S OWN
MINIMUM cannot rise past a stalled door, which would seat the place
mid-walk after all. This file asks exactly that, in three scopes: the
void walks the claim is filed at; a sweep of ram-free planted seeds (the
generalization the claim does not make); and a designed seed built to
put an unplanted ramified place at the bottom of a menu.

WHOSE VOCABULARY, asked at the freeze. "The min cannot rise past it" is
the DOOR corpus's phrase, and its objects -- menu, door, invariant -- are
the ring engines' own. No schedule vocabulary enters: the abstract
family has no ramified places and no menu, so there is nothing to
transplant from it. What IS carried in is flagged below.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 The mechanism sketch in hand-attack E (every seated place feeds
    v_2 of the invariant, so char-2 ram doors climb in lockstep with the
    menu) is written in Z[sqrt(-5)]'s lambda shapes and carried to the
    other two rings. The engines' own lambda tables are the object; the
    sketch is a suspicion the prints must confirm per ring or retire.
 T2 "Any strict late seating lives in the finite transient" imports the
    lock/tail split from explore_lock_budget.py's ideal-world results.
    A walk that witnesses no lock inside WALK_CAP is reported as
    UNLOCKED, never assumed locked.

THE HAND-ATTACK, on paper before any engine code; the one dereference of
an engine convention (the door table at the designed seed) was re-derived
from the engine's own door_r before this freeze, per the index-convention
rule.

 A. THE EVENT IS A MENU FACT. Greedy pays the menu minimum every step,
    first tie member taken. So an unseated ramified place R is seated at
    step t exactly when its current price is the menu minimum at t (and
    it wins the tie-break). "Seated late" = such an event at t >= 2.
 B. MONOTONE HALF (the argued one, verified in-walk rather than
    assumed). While R stays unseated its exponent is untouched, so by
    Lemma B its door never falls as L grows: price_R is nondecreasing.
 C. THE POST-LOCK REDUCTION. Once a walk locks, its paid price is flat
    at the lock cost forever (explore_lock_budget.py PR1), and at every
    tail step the lock cost is <= price_R since greedy took the min. A
    flat floor against a nondecreasing price meets only at a TIE. So any
    STRICT late seating must happen in the transient -- a finite window
    -- and the unproved half is a transient question plus a tie clause.
    This is a derivation; S5 checks its two premises in the walk data.
 D. THE DESIGNED SEED. At Z[sqrt(-5)], seed a split place over 163
    beside one over 3 (both depth 1): L = lcm(162, 2) = 2 * 3^4. On the
    engine's door convention the menu reads: deepening the 3-place costs
    3^5 = 243 (its char's invariant part outruns its depth), the
    163-place 163, the fresh conjugate over 3 costs 3^6, fresh ram
    R2 2^3 = 8, fresh ram R5 5^1 = 5 (lambda(R5^1) = 4 does not
    divide L). The minimum is the UNPLANTED RAMIFIED place at 5. So a
    seeded state can put an unplanted ram at the bottom of a menu; what
    the sweep decides is whether a walk can ARRIVE at such a state --
    the min rising past the stalled door -- rather than being planted in
    it.
 E. THE VOID'S SUSPECTED PROTECTION (mechanism sketch, T1). From the
    void the walk seats small norms first, and every seated place of
    odd norm contributes lambda(P^1) = N(P) - 1, even there -- so
    v_2(L) climbs with the walk and the char-2 rams' doors climb with
    it. The odd-char
    rams' (R5, R23) doors widen only when their next ladder rung
    divides L, and the divisors a rung waits for (the factors of q - 1
    first, powers of q above) enter L only through seatings whose
    lambda carries them, so their doors CAN stall -- but their floor
    price (norm >= 5^1, 23^1) sits at or
    above the small-norm menu the void keeps affordable. Whether that
    accounting closes is what S3's margins print.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 CONTROL. The three void walks reproduce the filed record: K5 and
    K23 lock on a split place of norm 3 at cost 3 with no ramified
    place ever seated; ZI's first move seats its ram at cost 4 and the
    walk locks on the inert place of norm 9 at cost 9. PRINTS: per
    ring, the first move, the lock vehicle and cost, the seated rams.
    KILL: any mismatch.
PR2 MONOTONE. Across every walk in every section, no unseated place's
    price ever decreases step-to-step. PRINTS: the total count of
    decrease events (expected 0). KILL: one event -- which would break
    Lemma B's instance here and reopen the argued half itself.
PR3 VOID MARGINS. In each void walk, at every step from the second on,
    every unseated ram's price strictly exceeds the paid price.
    PRINTS: per ring, the minimum margin (ram price - paid) over the
    walk and the step attaining it. KILL: one step with margin <= 0.
PR4 SEEDED SWEEP. Over every ram-free seed (single places at depth 1
    and 2, and unordered pairs at depth 1, norms <= SEED_NORM_CAP, all
    three rings), the rig detects every seating of an UNPLANTED ram and
    classifies it by step: step 1 is the seed's own cheapest opening --
    the void claim's shape at a shifted origin -- and step >= 2 is a
    genuine LATE seating, the menu minimum having risen past the door.
    PRINTS: per ring, walks run, seating events, the step histogram,
    every step->=2 event's full trajectory, and every tie a ram loses.
    The suspicion fixed now: step-1 events exist at K5 (D witnesses the
    state; whether the depth caps reach it is the sweep's to say);
    step->=2 events are the open question and no count is predicted.
    KILL for the GENERALIZED law: any step->=2 event -- the void claim
    would then stand on the void's own arithmetic, not on a general
    impossibility.
PR5 DESIGNED CONTROL. The 163-and-3 seed at K5 walks its first move to
    R5 at cost 5. PRINTS: the step-1 vehicle and cost. KILL: anything
    else.
PR6 POST-LOCK REDUCTION. In every walk that witnesses a lock, both
    premises of C hold in the data: the paid price is constant along
    the tail, and every unseated ram's margin over it is nondecreasing.
    PRINTS: the count of violations (expected 0), and the count of
    UNLOCKED walks reported separately (T2). KILL: one violation.

RESOURCE ENVELOPE, named before the run: one process, no BLAS; the sweep
is ~1000 walks per ring x <= 60 steps x a ~300-place menu scan, estimate
under 5 minutes wall and well under 512 MB.

THE FINDINGS, entered after the run by copying printed output.

F1 CONTROL (PR1 met). K5: first move P3.1^1 at 3, lock P3.1 cost 3 at
   step 10, no rams seated. K23: P3.0^1 at 3, lock P3.0 cost 3 at step
   10, no rams. ZI: first move R2^2 at 4, lock Q3 cost 9 at step 12,
   rams seated [R2]. The filed record reproduced exactly.
F2 THE UNPROVED HALF IS FALSE IN GENERAL (PR4's kill fired: the
   generalized reading dies, the void claim stands as scoped). The menu
   minimum CAN rise past a stalled ramified door. 34 late seatings:
   K5 945 walks, histogram {1: 339, 2: 10, 3: 4}; K23 1080 walks,
   histogram {1: 380, 2: 20}. Specimen at K5, a seed of split places
   over 29 and 47: paid 7 (a fresh place over 7), then 23, then 25 --
   seating R5
   at EXPONENT 2 in one move, its price stalled at 25 through the whole
   climb. At K23 the paid climbs 13 -> 23 and seats R23 at door 1. So
   the minimum rising past the stall is real, and a late-seated ram can
   even enter above exponent 1.
F3 THE VOID'S PROTECTION IS ITS POVERTY (PR3 met). Void margins strict:
   K5 minimum margin 2 (R5 priced 5 against paid 3, step 2), K23
   margin 20 (23 against 3), ZI no unseated ram past step 1. Both
   odd-char rings lock on norm 3 by step 10 and the paid sequence never
   leaves 3: from the void the walk cannot afford the states the sweep
   plants, because reaching them costs more than the lock it would have
   to refuse. The claim's mechanism is the void's reachable set, not
   any general impossibility.
F4 THE RESIDUE-CHARACTERISTIC DICHOTOMY (pattern at three rings; the
   even-lambda half argued, the stall half exhibited). Every one of the
   753 seeded seatings is an ODD-characteristic ram -- R5 353, R23
   400 -- and no char-2 ram ever seats: K5's R2 never priced below 8
   (range 8..512), ZI's R2 never below 256 (range 256..65536) over its
   1080 walks. Mechanism: lambda(P^1) = N(P) - 1 is even at every
   place of ODD norm -- only places over 2 have even norm -- so every
   seating off the char-2 fibre feeds v_2 of the invariant and a char-2
   ram's door climbs in lockstep with the menu (at Z[i] every split
   prime is 1 mod 4, feeding v_2 twice over); an odd-char ram's door
   widens only when its next ladder rung divides L, and the divisors a
   rung waits for (the factors of q - 1 first, powers of q above) a
   seed's L need never carry -- the stall. T1's sketch held per ring;
   retired.
F5 THE TRANSIENT REDUCTION HOLDS (PR2, PR6 met). 3109 walks, 0
   monotone violations, 0 post-lock violations, 0 unlocked. The
   hand-attack C derivation stands on checked premises: a strict late
   seating lives in the transient, and past the lock only a tie could
   seat a ram -- and 0 lost ties were observed anywhere, either.
F6 DESIGNED CONTROL (PR5 met). The 163-and-3 seed at K5: step 1 pays 5
   at R5^1 (ram prices at the seed: R2 8, R5 5). The walk then locks on
   a split place over 23:
   R5's paired lambda ladder (4, 20, 20, 100, 100, ...) prices
   every second rung at 25, so the seated ram rides its cheap rungs and
   still loses the lock to an unramified place -- the seeding and the
   lock are separate questions.

WHAT IS LEFT OPEN. Nothing of the void question: the sibling rig
explore_late_seating.py settles it both ways -- the winner-kind
dichotomy (an unramified void winner of odd norm locks the menu at its
own norm, proved) and the void late seating its quadratic-ring factory
exhibits
at Z[sqrt(-30)], the two-ram shape this file's dichotomy points at.
This file is that record's SCALE companion: the ~3000-walk sweep, the
per-ram census behind the residue-characteristic dichotomy, the zero
tie count, and the checked premises of the transient reduction.

RUN RECORD. One process, CPython, no BLAS. Wall 15.5 s, peak working
set 79.0 MB against the 512 MB ceiling. 15 checks green. 3109 walks:
three void, 945 + 1080 + 1080 seeded (SEED_NORM_CAP 200), one designed.
One classification bug caught by its own print before any finding was
read: the first build recorded a ram's post-seating deepenings as fresh
seatings ("late at step 2" directly after a step-1 seating of the same
place); the event condition now reads the pre-move exponent.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_number_field_lock as K5     # Z[sqrt(-5)], h = 2
import explore_module_law as K23           # Z[w], w^2 = w - 6, h = 3
import explore_gaussian_runaway as ZI      # Z[i], the inverted ordering

CHECKS = 0

WALK_CAP = 60        # moves before a walk is reported UNLOCKED
LOCK_R = 10          # consecutive identical vehicles that witness a lock
SEED_NORM_CAP = 200  # seed places drawn at or below this norm
DESIGNED_SEED = [(('split', 163, 22), 1), (('split', 3, 1), 1)]

RINGS = [("K5", K5, "Z[sqrt(-5)]"),
         ("K23", K23, "Z[w], w^2 = w - 6"),
         ("ZI", ZI, "Z[i]")]


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def show_place(pl):
    if pl[0] == 'split':
        return "P%d.%d" % (pl[1], pl[2])
    if pl[0] == 'inert':
        return "Q%d" % pl[1]
    return "R%d" % pl[1]


def show_state(M, st):
    parts = ["%s^%d" % (show_place(pl), e)
             for pl, e in sorted(st.items(), key=lambda kv: M.place_key(kv[0]))
             if e]
    return "*".join(parts) if parts else "(1)"


def rams(M):
    return [pl for pl in M.UNIVERSE if pl[0] == 'ram']


def walk(M, seed):
    """Greedy walk from a seed state, instrumented. Returns a dict:
    steps: list of (paid, chosen place, r, {ram: price for unseated rams
    at this step, read BEFORE the move}), lock: (place, cost, step) or
    None, monotone_viol: count of unseated-price decreases (over the
    WHOLE universe, not only rams), ram_events: [(step, place, paid)]
    seatings of rams not in the seed, ram_ties: [(step, place, price)]
    steps where an unseated ram tied the min and lost the tie-break."""
    st = dict(seed)
    L = M.lam_state(st)
    prev_price = {}          # last seen price per still-unseated place
    steps, ram_events, ram_ties = [], [], []
    monotone_viol = 0
    run_pl, run, lock = None, 0, None
    for i in range(WALK_CAP):
        cost, ties = M.ideal_menu(st, L)
        # unseated prices, monotone check over the whole universe
        ram_prices = {}
        for pl in M.UNIVERSE:
            if st.get(pl, 0):
                prev_price.pop(pl, None)
                continue
            r = M.door_r(pl, 0, L)
            price = M.place_norm(pl) ** r
            if pl in prev_price and price < prev_price[pl]:
                monotone_viol += 1
            prev_price[pl] = price
            if pl[0] == 'ram':
                ram_prices[pl] = price
        pl, r = ties[0]
        t = i + 1
        for rp, price in ram_prices.items():
            if price == cost and rp != pl:
                ram_ties.append((t, rp, price))
        if pl[0] == 'ram' and st.get(pl, 0) == 0:
            ram_events.append((t, pl, cost))
        steps.append((cost, pl, r, ram_prices))
        st[pl] = st.get(pl, 0) + r
        L = M.lam_state(st)
        if pl == run_pl:
            run += 1
        else:
            run_pl, run = pl, 1
        if run >= LOCK_R and lock is None:
            lock = (pl, cost, t)
    return {"steps": steps, "lock": lock, "monotone_viol": monotone_viol,
            "ram_events": ram_events, "ram_ties": ram_ties, "seed": seed}


def seeds_for(M):
    """Ram-free seeds: singles at depth 1 and 2, unordered pairs at depth
    1, over places of norm <= SEED_NORM_CAP."""
    pool = sorted((pl for pl in M.UNIVERSE
                   if pl[0] != 'ram' and M.place_norm(pl) <= SEED_NORM_CAP),
                  key=M.place_key)
    out = []
    for pl in pool:
        out.append([(pl, 1)])
        out.append([(pl, 2)])
    for a in range(len(pool)):
        for b in range(a + 1, len(pool)):
            out.append([(pool[a], 1), (pool[b], 1)])
    return out


# ---------------------------------------------------------------- sections
def s1_control(store):
    section("S1 CONTROL (PR1): the three void walks against the filed record")
    filed = {"K5": ('split', 3, 3), "K23": ('split', 3, 3),
             "ZI": ('inert', 9, 9)}
    for name, M, desc in RINGS:
        w = walk(M, [])
        store[(name, "void")] = w
        first_cost, first_pl, first_r, _ = w["steps"][0]
        lock = w["lock"]
        seated_rams = sorted(set(pl for _, pl, _ in w["ram_events"]),
                             key=M.place_key)
        print("%-4s first move %s^%d at %d; lock %s cost %s at step %s; "
              "rams seated: %s"
              % (name, show_place(first_pl), first_r, first_cost,
                 show_place(lock[0]) if lock else "NONE",
                 lock[1] if lock else "-", lock[2] if lock else "-",
                 [show_place(p) for p in seated_rams] or "none"))
        kind, nrm, cost = filed[name]
        ok(lock is not None, "%s: void walk did not lock" % name)
        ok(lock[0][0] == kind and M.place_norm(lock[0]) == nrm
           and lock[1] == cost,
           "%s: lock differs from filed record" % name)
        if name == "ZI":
            ok(first_pl[0] == 'ram' and first_cost == 4,
               "ZI: first move is not the ram at 4")
            ok(seated_rams == [('ram', 2)], "ZI: seated rams differ")
        else:
            ok(not seated_rams, "%s: a ram was seated from the void" % name)


def s2_void_margins(store):
    section("S2 VOID MARGINS (PR3): unseated ram price minus paid, per step")
    for name, M, desc in RINGS:
        w = store[(name, "void")]
        worst = None
        for t, (paid, pl, r, ram_prices) in enumerate(w["steps"], 1):
            if t == 1:
                continue
            for rp, price in ram_prices.items():
                m = price - paid
                if worst is None or m < worst[0]:
                    worst = (m, t, rp, price, paid)
        if worst is None:
            print("%-4s no unseated ram past step 1" % name)
            continue
        m, t, rp, price, paid = worst
        print("%-4s min margin %d at step %d (%s priced %d, paid %d)"
              % (name, m, t, show_place(rp), price, paid))
        ok(m > 0, "%s: margin <= 0 -- late seating or tie at the void" % name)


def s3_seeded_sweep(store):
    section("S3 SEEDED SWEEP (PR4): every ram-free seed, all three rings")
    for name, M, desc in RINGS:
        seeds = seeds_for(M)
        events, ties, late = [], [], []
        unlocked = 0
        for seed in seeds:
            w = walk(M, seed)
            if w["lock"] is None:
                unlocked += 1
            store.setdefault((name, "sweep"), []).append(w)
            for (t, pl, paid) in w["ram_events"]:
                events.append((t, pl, paid, seed))
                if t >= 2:
                    late.append((t, pl, paid, seed, w))
            for tie in w["ram_ties"]:
                ties.append(tie + (seed,))
        hist = {}
        per_ram = {}
        for (t, pl, _, _) in events:
            hist[t] = hist.get(t, 0) + 1
            per_ram[pl] = per_ram.get(pl, 0) + 1
        # each ram's price range over every sweep step it stayed unseated
        floors = {}
        for w in store[(name, "sweep")]:
            for (_, _, _, rp) in w["steps"]:
                for pl, price in rp.items():
                    lo, hi = floors.get(pl, (price, price))
                    floors[pl] = (min(lo, price), max(hi, price))
        print("%-4s %d walks (%d unlocked): %d unplanted-ram seatings, "
              "step histogram %s, %d lost ties"
              % (name, len(seeds), unlocked, len(events),
                 sorted(hist.items()) or "{}", len(ties)))
        print("  per ram: seatings %s; unseated price range %s"
              % ({show_place(p): n for p, n in sorted(per_ram.items())} or
                 "none",
                 {show_place(p): floors[p] for p in sorted(floors)}))
        for (t, pl, paid, seed, w) in late:
            print("  LATE at step %d: %s seated at %d from seed %s"
                  % (t, show_place(pl), paid, show_state(M, dict(seed))))
            for u, (c, p, r, rp) in enumerate(w["steps"][:t], 1):
                print("    step %d: paid %d at %s^%d, ram prices %s"
                      % (u, c, show_place(p), r,
                         {show_place(k): v for k, v in rp.items()}))
        for (t, rp, price, seed) in ties[:10]:
            print("  tie lost at step %d: %s priced %d, seed %s"
                  % (t, show_place(rp), price, show_state(M, dict(seed))))
        store[(name, "late")] = late
        store[(name, "events")] = events


def s4_designed(store):
    section("S4 DESIGNED CONTROL (PR5): the seed over 163 and 3 at K5")
    w = walk(K5, DESIGNED_SEED)
    store[("K5", "designed")] = w
    cost, pl, r, ram_prices = w["steps"][0]
    print("step 1: paid %d at %s^%d; ram prices at the seed: %s"
          % (cost, show_place(pl), r,
             {show_place(k): v for k, v in ram_prices.items()}))
    lock = w["lock"]
    print("lock: %s cost %s at step %s; ram events: %s"
          % (show_place(lock[0]) if lock else "NONE",
             lock[1] if lock else "-", lock[2] if lock else "-",
             [(t, show_place(p), c) for t, p, c in w["ram_events"]]))
    ok(pl == ('ram', 5) and cost == 5,
       "designed seed's first move is not R5 at 5")


def s5_monotone_and_reduction(store):
    section("S5 MONOTONE + POST-LOCK REDUCTION (PR2, PR6): every walk")
    total_mono = 0
    tail_viol = 0
    unlocked = 0
    walks = 0
    for key, val in store.items():
        wlist = val if isinstance(val, list) else [val]
        for w in wlist:
            if not isinstance(w, dict) or "steps" not in w:
                continue
            walks += 1
            total_mono += w["monotone_viol"]
            lock = w["lock"]
            if lock is None:
                unlocked += 1
                continue
            _, lock_cost, lock_step = lock
            prev_margin = {}
            for t, (paid, pl, r, ram_prices) in enumerate(w["steps"], 1):
                if t < lock_step:
                    continue
                if paid != lock_cost:
                    tail_viol += 1
                for rp, price in ram_prices.items():
                    m = price - paid
                    if rp in prev_margin and m < prev_margin[rp]:
                        tail_viol += 1
                    prev_margin[rp] = m
    print("%d walks: %d monotone violations, %d post-lock violations, "
          "%d unlocked (reported, per T2)" % (walks, total_mono, tail_viol,
                                              unlocked))
    ok(total_mono == 0, "an unseated price decreased (PR2 kill)")
    ok(tail_viol == 0, "a post-lock premise failed (PR6 kill)")


def main():
    store = {}
    s1_control(store)
    s2_void_margins(store)
    s3_seeded_sweep(store)
    s4_designed(store)
    s5_monotone_and_reduction(store)
    print("\nALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
