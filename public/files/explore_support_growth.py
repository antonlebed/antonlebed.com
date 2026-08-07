r"""explore_support_growth.py -- can a greedy walk's SUPPORT grow fast
enough to build a surplus, and what freezes it if it cannot.

THE QUESTION. The stop law -- a bounded tick gap stops a walk -- is scoped
rather than safe because the walked surplus is a MEASUREMENT: five rings,
twelve walks, sixty moves each, v_p(L) above a seated place's own ladder
reading 0 at four rings and 1 at Z[i] (explore_wild_ring.py F5). What a
bound needs is not a sixth ring. The surplus a walk can build is supplied
by the places it SEATS, so the object to bound is the SUPPORT: how far out
in norm a greedy walk can reach, and for how long it keeps reaching. This
file derives that bound and runs the walks far past the horizon the
measurement used.

THE DERIVATION, on paper before any engine code. Four steps, the first
three one line each.

  LEMMA A (the p-shape of a column). At every place P over p with norm
  q = N(P), (O/P^a)^* = mu_{q-1} x U_1/U_a with U_1/U_a a p-group, so
  lam(P^a) = (q - 1) * p^k(a) with k nondecreasing and k(1) = 0. This is
  local structure and holds at every place of every number ring -- the
  corpus's non-standard columns (Z[i]'s plateau, the level shift and the
  phase shift of explore_wild_ring.py F1) all have this shape, differing
  only in k. S1 reads it off every filed column as a control.

  LEMMA B (doors are monotone in the invariant). door(Q, e, L) is the
  least r with lam(Q^(e+r)) not dividing L. If L divides L', the set
  {r : lam(Q^(e+r)) | L} grows, so the least r outside it can only grow:
  door(Q, e, L) <= door(Q, e, L'). A place's cost therefore NEVER falls
  while its own exponent is untouched. A surplus can only price a place
  OUT, never in.

  LEMMA C (a run at one place moves one prime). If the walk moves only at
  P over p between two steps, then for every prime l != p, v_l(L) is
  constant across them: L is the lcm of the seated lam's, only lam(P^e)
  changes, and by Lemma A its prime-to-p part is the constant q - 1.

  THE COST LIMIT. Combine: under a P-only run, every OTHER place Q has a
  cost that is nondecreasing (B) and eventually CONSTANT, with a value
  computable at the moment the run starts.
  [CORRECTED POST-RUN -- "eventually constant" is the finite case only,
  and the same paragraph names the other two lines down: where every r
  divides, the door climbs with v_p(L) forever and the cost diverges. The
  statement that survives is that the LIMIT is computable at the start,
  finite or infinite; S3 reads five infinite ones and none of them is a
  constant.] Divisibility of lam(Q^(e+r))
  into L splits into its p-part and its prime-to-p part; the prime-to-p
  part of L is frozen (C) while v_p(L) grows without bound, so the p-part
  condition is eventually satisfied for every r. Hence
      door_inf(Q, e) = least r with lam(Q^(e+r))_{p'} not dividing L_{p'}
  (infinite if there is none, which is a place priced out forever), where
  the subscript is the prime-to-p part. For Q over l != p this reads
  (N(Q) - 1)_{p'} * l^k against L; for Q over p itself it reads
  (N(Q) - 1)_{p'} alone, so a co-characteristic place is priced out
  exactly when its prime-to-p part already divides L.

  THE LOCK PERMANENCE CERTIFICATE. Let the walk move at P at step s, let
  C* be the supremum of P's own cost over the P-only future (finite: P's
  door sequence is eventually periodic, since k_P is eventually an
  arithmetic progression of step e_P), and let m be the minimum cost over
  all Q != P at step s -- a minimum over the finitely many places of norm
  at most C*, since cost >= N(Q). If C* < m the walk moves at P forever:
  by B no rival ever gets cheaper, so P wins every subsequent menu.
  Support frozen, greedy support growth zero from step s on.

  THE SUPPORT BOUND. A place is seated only by being the argmin, so a
  place Q seated at step t paid cost_t(Q) = c_t, the walk's own move cost
  at t; and cost_t(Q) >= N(Q) because a door is at least 1. Hence
      every seated place has N(Q) <= max cost the walk ever pays,
  with no hypothesis at all. Under a certified lock that maximum is
  finite, so the support is finite and lies inside an explicit norm ball.

  THE RACE, DECIDED. The route's carrier floor says pushing the surplus to
  k needs a seated place of norm at least p^k + 1: supply costs
  exponentially in what it supplies. The support bound caps every seated
  norm by the largest cost paid, C. So the cross-supply a walk can seat is
  at most log_p(C) -- the race is settled against the walk, and by a
  BUDGET argument rather than by a rate comparison. Under a lock at price
  N^gap the ceiling is gap * log_p(N), which is small for the same reason
  locks are cheap.

  THE SURPLUS DICHOTOMY, the sting in the tail. After a permanent lock on
  P over p, v_p(L) grows without bound along P's own column. At a seated
  Q over l != p the surplus is frozen (C). At a seated Q != P over p
  itself the surplus DIVERGES, linearly in the move count. So "a ring
  walk's surplus stays small" is not a law: it is true exactly when the
  lock's characteristic hosts no second seated place, and false without
  bound otherwise. Sixty moves cannot tell the two apart. What is bounded
  is the SUPPORT, and the divergence is harmless for the reason B gives --
  it prices a strand further out and can never bring one in.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The engine's --
lam_P, door_r, ideal_menu, seated, v_p(L) -- because the claim under test
is explore_wild_ring.py F5's and explore_populated_door.py F6/F7's, and
the SUPPORT is a term already in those files (F4's "support 3^2 * 5^10").
The schedule family's vocabulary (head, gap, price) enters only where the
recurrent price is named, which is a quantity the walker returns.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 The recurrent cost cycle's PERIOD is not carried from the wild ring's
    reading (doors cycling with period e at its ramified places). S4
    MEASURES the period of each vehicle's door sequence under its own
    P-only future and asserts the repeat, rather than assuming e_P.
 T2 "Every walk locks" is carried from three engines that each witnessed a
    lock from their own seeds, and it is an EXPECTATION here, never a
    hypothesis of the derivation: the certificate is conditional on a lock
    and prints FAIL where none is witnessed.
 T3 The horizon 500 is chosen against the 60 of the sweep it extends, with
    no claim that 500 is enough for anything; every statement read at 500
    is a statement about 500 moves unless the certificate carries it to
    infinity. Divergence is read as a SLOPE over the last half of the
    walk, not as a large value.
 T4 The surplus and door-excess observables are explore_wild_ring.py's own
    -- v_p(L) - v_p(lam_P(Q^e)) per seated place -- reused verbatim, so
    the long horizon extends that sweep rather than resembling it.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 Lemma A reads clean at every place of all five rings to the brute
     cap: lam(P^a) / (N(P) - 1) is a power of the residue characteristic
     at every (place, depth), 0 off -- Z[i]'s plateau and both of the
     wild ring's deviating columns included. And the two filed locks
     reproduce through the imported walker: the wild ring's void walk
     locks on the rational place over 5 at cost 5 with support
     3^2 * 5^10 after 12 steps (explore_wild_ring.py F4).
  P2 Zero violations of Lemma B over every nested pair (L, L') the twelve
     walks actually produce, read at every place of norm <= 60 and every
     seated exponent.
  P3 Under each certified lock: v_l(L) constant for every prime l != p
     across the whole locked stretch; every rival's cost sequence
     nondecreasing; and each rival's eventual cost equals the closed-form
     door_inf prediction at every place of norm <= 60, 0 off.
  P4 All twelve walks lock inside 500 moves and the permanence
     certificate PASSES at all twelve, so the support at move 500 is the
     support at the lock, place for place.
  P5 The support bound holds at all twelve walks: max seated norm <= max
     cost paid. This is a theorem, so a violation is an engine bug and
     stops the run.
  P6 The race bound holds: max seated cross-supply v_p(N(Q) - 1) over all
     twelve walks is at most floor(log_p C) at every walk, and the
     corpus's filed maximum of 3 (Z[i], explore_wild_ring.py F5) sits
     under its own ceiling.
  P7 THE DICHOTOMY. At 500 moves the walks split exactly by the
     co-characteristic criterion: a walk whose lock characteristic hosts
     a second seated place has a surplus growing with positive slope over
     the last half of the walk, and every other walk's surplus at 500
     equals its surplus at 60. WHICH walks fall which side is not
     predicted -- the partition itself is the prediction, and a single
     walk on the wrong side of it kills the dichotomy.

KILL-SHAPES, as observables.
  K1 the imported walker disagrees with a filed lock: instrument wrong,
     stop before any verdict.
  K2 a door-monotonicity violation prints: Lemma B is false and the cost
     limit, the certificate and the support bound all fall with it.
  K3 a walk seats a place whose norm exceeds every cost it paid: the
     support bound is false, which would mean the argmin reading of a
     move is wrong.
  K4 the certificate passes at a walk whose support then grows: lock
     permanence is false as derived.
  K5 a walk sits on the wrong side of the co-characteristic partition:
     the dichotomy is false and the surplus has a third behaviour.

THE SECOND SLATE (S6), frozen after S1-S5 printed and before S6 was
written, because the first sweep left one side of the dichotomy
unexercised: not one of the twelve walks ever seats a second place in its
vehicle's own characteristic, so every walk sits on the frozen side and
the criterion is confirmed vacuously. A prediction only one side of which
can fire is not a prediction, so the other side is CONSTRUCTED.
  THE CONSTRUCTION. For each ring take the certified vehicle P over p of
  its void walk and plant, one at a time, every OTHER place of the ring
  over that same p -- a split prime supplies one, an inert or ramified
  prime supplies none. Then walk the same horizon.
  Q1 Where such a place Q exists, the designed walk still certifies a
     lock; and where the certified vehicle's characteristic is still p
     with Q still seated, the surplus grows without bound -- strictly
     positive slope over the second half of the walk.
  Q2 The support bound and the race bound hold at every designed walk
     unchanged. The support half has no lock hypothesis in it at all, so
     a failure there is an engine bug and not a scope.
  Q3 The divergence is the vehicle's own column and nothing else: the
     surplus gained between move 60 and move 500 equals v_p(L) gained
     over the same stretch, exactly.
  K6 no designed seed diverges: the dichotomy's divergent side is not
     realizable in these rings and the law is the simpler "the walked
     surplus is frozen after a certified lock", which would be a
     STRONGER result than the one derived.

S6 ROUND 2, frozen after round 1 printed. K6 fired, and the specimens name
the mechanism: a place ALREADY SEATED is cheaper than its unseated sibling
over the same prime, its first rung being covered already, so greedy takes
the planted place as its vehicle rather than seating a second one beside
it. One seed defeats that -- plant EVERY place over p at once, so that
whichever becomes the vehicle, another is seated and co-characteristic by
construction.
  Q4 That seed diverges: the non-vehicle place over p stays seated, its
     surplus climbs with the vehicle's own column, and the gain from move
     60 to move 500 equals v_p(L)'s gain over the same stretch. If it does
     not, no configuration in these rings realizes the divergent side and
     the frozen reading stands as a measurement rather than as the law
     the derivation predicts.

DISTRUST THE MARGIN. The derived halves are Lemmas A, B, C and the two
bounds that follow from them -- each a one-line argument over a
divisibility set, and each with an engine reading beside it. The vibes
half is P4: that every walk locks at all, and that a certificate computed
over a SIMULATED P-only future is the same future the walk takes. S4
therefore simulates the P-only run and then WALKS it, asserting the two
agree step for step, so a certificate that lies prints as a disagreement
rather than as a silent pass.

POSITIVE CONTROL (S1, run before any verdict is read): the imported
walker against a filed lock, and Lemma A against every filed column of
all five rings. Nothing downstream is read until both print clean.

THE SECTIONS.
  S1  positive control: Lemma A over five rings, a filed lock reproduced.
  S2  Lemma B: door monotonicity over every nested invariant pair the
      walks produce.
  S3  the cost limit: the frozen primes, the nondecreasing rivals, and
      door_inf against the observed eventual cost.
  S4  the certificate: lock, C*, m, PASS/FAIL, then 500 moves walked
      against the simulated future and the support compared.
  S5  the support bound, the race bound, and the surplus dichotomy at the
      long horizon.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE SUPPORT BOUND: A GREEDY WALK NEVER SEATS A PLACE COSTLIER THAN THE
   MOST IT EVER PAYS (theorem, holding at every walk in every number ring
   with no hypothesis in it at all; read at 20 walks over five rings, 12
   swept and 8 designed). A place is seated only by winning the menu, so
   the cost it pays IS the walk's move cost at that step; and a door is at
   least 1, so that cost is at least N(Q). Hence every seated norm is at
   most the largest cost the walk ever pays. The bound is TIGHT at 10 of
   the 12 swept walks -- the walk buys, at its dearest, exactly the place
   whose norm equals that price -- and slack at the two whose planted seed
   raised the ceiling above anything the walk went on to buy (Z[w]'s
   planted place over 23: norm 3 against a ceiling of 9; the wild ring's
   planted X: 2 against 8). So "greedy seating starves diversity"
   (explore_wild_ring.py F5) is not a reading off five rings: it is what
   the argmin does. The support of a greedy walk lies in an explicit norm
   ball, and under a certified lock (F3) that ball stops growing.

F2 THE RACE IS SETTLED BY A BUDGET AND NEVER RUNS AS A RATE COMPARISON
   (theorem, given the carrier floor it consumes; the ceiling read at all
   12 swept walks). The route's floor prices a surplus of k at a seated
   norm of at least p^k + 1 -- supply costs exponentially in what it
   supplies -- while F1 caps every seated norm by the largest cost paid C.
   So the cross-supply a walk can seat is at most log_p C, and the rig
   reads the p-free form log_2 C, which bounds every characteristic at
   once and is the one comparable across a table. The two
   exponential rates never meet: the walk cannot afford the carrier at
   any surplus its own budget does not already permit. The ceiling reads
   1 to 3 across the sweep against supplies that are 0 at nine walks and 1
   at Z[sqrt-5]'s planted place over 2; the exception is Z[i], where BOTH
   walks seat the corpus's filed maximum of 3 -- v_2(N - 1) at the inert
   place over 3 -- and it sits EXACTLY at its own ceiling, floor(log_2 9)
   being 3. The largest supply anybody has measured is
   the largest one the budget allows, which is why five rings kept
   returning the same small number.

F3 THE LOCK PERMANENCE CERTIFICATE, AND THE WITNESS THAT PROVES NOTHING
   (theorem for the certificate; rule in range for its 12 of 12, five
   rings, 500 moves). Simulate the vehicle-only future, take C* as its
   largest cost, take m as the cheapest rival at that step; C* < m carries
   the lock to infinity, because by Lemma B no rival ever gets cheaper
   while its own exponent is untouched. All 12 walks certify. Beside it,
   the walker's own lock test -- 10 consecutive moves at one place -- is a
   heuristic, and the two disagree at the wild ring's planted-X walk,
   where the witness fires at step 1 and the certificate only at step 2:
   at step 1 a rival stood at cost 5 against C* = 8 and only Lemma B's
   climb, not the witness, put it out of reach. The certificate is
   SUFFICIENT and one-sided, so its step is an upper bound on the true
   lock step. And a witnessed door period is part of the
   certificate, not a decoration -- without one, C* is a max over a sample
   rather than a supremum over the future. It reads 1 at all 12: every
   vehicle's recurrent price is a single constant and not a cycle, so C*
   IS that price.

F4 THE COST LIMIT IS A CLOSED FORM, AND FIVE RIVALS ARE PRICED OUT FOREVER
   (theorem for the form; rule in range, 196 rival readings across 12
   certified locks, 0 off). Under a lock at P over p, every prime but p
   holds its valuation in L at all 12 walks (Lemma C), so a rival's door
   is decided by a divisibility that no longer moves:
   door_inf(Q, e) = the least r whose lambda's prime-to-p part fails to
   divide L. Every rival of norm at most 60 reaches that value and stops,
   at every walk. Five of the 196 are infinite -- a door climbing forever,
   which at this horizon reads as a finite number between 499 and 502 and
   would be scored a miss by anyone comparing a limit to a sample. All
   five are the co-characteristic SIBLING of a split vehicle, the other
   place over the vehicle's own prime, and the reason is exact:
   a SEATED place over p has (N - 1) | L already, which is the whole of
   its prime-to-p condition, so its door climbs with v_p(L) and never
   stops. Being seated is what prices a co-characteristic place out.

F5 THE SURPLUS DICHOTOMY IS EXACT, AND GREEDY REFUSES ITS DIVERGENT SIDE
   (theorem for the two implications; PATTERN for the refusal, 16 walks
   over five rings; the divergent side realized by construction at 4).
   After a certified lock at P over p: a seated place over l != p has a
   FROZEN surplus, and a seated place over p other than P has one that
   DIVERGES, gaining exactly what v_p(L) gains. The sweep exercises only
   the frozen side -- 0 of 12 walks diverge, every surplus at move 500
   equal to its value at move 60 -- because no walk ever seats a second
   place under its own vehicle's characteristic. Planting one does not
   force it either (0 of 4): the planted place BECOMES the vehicle at both
   quadratic rings, and at both cubic rings the lock leaves the
   characteristic entirely, moving from the place over 5 to the place over
   11. The mechanism is one line and is the same one as F4's: a seated
   place has its first rung covered, so it is CHEAPER than its unseated
   sibling over the same prime, and greedy takes it rather than seating a
   second beside it. Only a seed holding EVERY place over p forces the
   configuration, and then the divergence is immediate and exact: at all
   four rings that admit the seed the surplus runs 60 at move 60 to 500 at
   move 500, gaining 440 -- precisely v_p(L)'s own gain of 440 over the
   same window. So "a ring walk's surplus stays small" is a fact about
   GREEDY and not about the dynamics, and the object that is bounded
   outright is the SUPPORT.

WHAT THIS LEAVES. The stop law's populated-door readings are safe for a
reason the corpus was not using: not that the surplus is small, but that
doors are monotone in the invariant (Lemma B), so a surplus can only ever
price a place OUT. A diverging surplus at a co-characteristic strand
strands it harder and can never bring a place in. And the measurement
becomes a bound where a certificate stands: at these five rings the walked
surplus is frozen from the certified lock step on, so 500 moves and
infinity read the same number. What is NOT settled is whether every
greedy walk locks at all -- the certificate is conditional on a lock and
proves permanence, never existence -- and the refusal in F5 is a pattern
over five rings with a mechanism, not a theorem.

RUN RECORD. `python explore_support_growth.py` (memwatch). One process,
CPython, no BLAS. 2660 checks, 1.0 s wall, peak working set 26.5 MB under
the 512 MB ceiling. S1: 576 Lemma A readings over five rings, the filed
wild-ring lock reproduced (place over 5 at cost 5, support 3^2 * 5^10 at
step 12), 480 menu readings against the imported engine, 0 off. S2: 49920
door readings over the invariant chains, 0 violations. S3: 196 rival
readings, 0 off the closed form, 5 infinite doors. S4: 12 of 12 certified,
door period 1 at every one. S5: 12 walks at 500 moves, 0 divergent. S6: 4
designed walks 0 divergent, 4 round-2 walks all 4 divergent. P1-P6 hit;
P7 hit vacuously, which is what fired the second slate; Q1-Q3's K6 fired
(the designed seed does not diverge) and Q4 hit, the two together being
F5.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import gcd

CHECKS = 0

HORIZON = 500       # moves per walk at the long horizon
SIM_MOVES = 200     # moves of P-only future simulated for the certificate
RIVAL_NORM = 60     # places whose doors are read against door_inf
BRUTE_DEPTH = 12    # depths a column is read for Lemma A
LOCK_R = 10         # consecutive identical vehicles that witness a lock


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def v_p(n, p):
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def prime_to_p(n, p):
    while n % p == 0:
        n //= p
    return n


# ------------------------------------------------------------- the rings
def load_rings():
    """The five engines of the filed sweep, each exposing the same handful
    of names: UNIVERSE, place_norm, place_char, place_key, lam_P,
    lam_state, door_r, ideal_menu. Returns (name, module, ramified places)
    per ring, and the seeds are the sweep's own: void plus one planted
    seed per ramified place, which is what makes twelve walks."""
    import explore_cubic_ring as C3
    import explore_wild_ring as W3
    quads = C3._load_quadratics()
    rings = []
    for name, M in quads:
        rings.append((name, M, [pl for pl in M.UNIVERSE
                                if _is_ramified(M, pl)]))
    rings.append(("-23 cubic", C3, [pl for pl in C3.UNIVERSE if pl[1] > 1]))
    rings.append(("Z[2^(1/3)]", W3, [pl for pl in W3.UNIVERSE if pl[1] > 1]))
    return rings


def _is_ramified(M, pl):
    """A quadratic engine tags its places by kind rather than by (e, f)."""
    return pl[0] == 'ram'


def show_pl(M, pl):
    return "%s/N%d" % (str(pl), M.place_norm(pl))


def seeds_of(M, rams):
    out = [("void", {})]
    for pl in rams:
        out.append(("planted %s" % str(pl), {pl: 1}))
    return out


# ----------------------------------------------------------- the walk
# The imported engines' door_r asserts at r = 500, which is sound at the
# 60-move horizon they were written for and NOT at this one: the cost
# limit's own co-characteristic case is a place every one of whose
# lambdas divides L, whose door is genuinely infinite. So the door and
# the menu are re-implemented here with infinity as a value. Both are
# exact -- the menu's early abort fires only where the place's cost has
# already passed the incumbent minimum, which cannot change an argmin --
# and S1 asserts they reproduce the imported engine's own answers.
DOOR_CAP = 4000


def door(M, pl, e, L, ceiling=None):
    """The least r with lam(pl^(e+r)) not dividing L, or INF. `ceiling`
    aborts the search once the cost has passed a known-better cost."""
    nrm = M.place_norm(pl)
    r = 1
    while L % M.lam_P(pl, e + r) == 0:
        r += 1
        if ceiling is not None and nrm ** r > ceiling:
            return INF
        if r > DOOR_CAP:
            return INF
    return r


INF = float('inf')


def cost_of(M, pl, e, L, ceiling=None):
    r = door(M, pl, e, L, ceiling)
    return INF if r is INF else M.place_norm(pl) ** r


def menu(M, st, L):
    """(cost, place, door) at the cheapest place, ties broken by place_key
    -- the imported engine's rule with infinite doors admitted."""
    best, arg = None, None
    for pl in M.UNIVERSE:
        nrm = M.place_norm(pl)
        if best is not None and nrm > best:
            break
        r = door(M, pl, st.get(pl, 0), L, best)
        if r is INF:
            continue
        c = nrm ** r
        if best is None or c < best or (c == best
                                        and M.place_key(pl)
                                        < M.place_key(arg)):
            best, arg = c, (pl, r)
    assert best is not None, "every place in the universe is priced out"
    return best, arg[0], arg[1]


def step(M, st, L):
    """One greedy move: (cost, place, door)."""
    return menu(M, st, L)


def walk(M, seed, moves, record=None):
    """Greedy walk from a seed. Returns the trace: per step the cost, the
    place, the door, the state and the invariant. `record` is a callback
    fired after each move for the columns that need every step."""
    st = dict(seed)
    L = M.lam_state(st)
    trace = []
    for i in range(moves):
        cost, pl, r = step(M, st, L)
        st = dict(st)
        st[pl] = st.get(pl, 0) + r
        L = M.lam_state(st)
        trace.append((cost, pl, r, dict(st), L))
        if record is not None:
            record(i, cost, pl, r, st, L)
    return trace


def witness_step(trace):
    """The first index at which LOCK_R consecutive moves share a place --
    the walker's own lock witness, which is a HEURISTIC and not a proof."""
    run_pl, run = None, 0
    for i, (cost, pl, r, st, L) in enumerate(trace):
        if pl == run_pl:
            run += 1
        else:
            run_pl, run = pl, 1
        if run >= LOCK_R:
            return i - LOCK_R + 1, run_pl
    return None, None


def door_inf(M, pl, e, L, p):
    """The eventual door at pl under a P-only run in characteristic p: the
    least r whose lambda's prime-to-p part fails to divide L, or None
    where every r divides -- a place priced out forever."""
    for r in range(1, 200):
        lam = prime_to_p(M.lam_P(pl, e + r), p)
        if L % lam != 0:
            return r
    return None


def _period(seq):
    for q in range(1, len(seq) // 3 + 1):
        if all(seq[i] == seq[i + q] for i in range(len(seq) - q)):
            return q
    return None


def certificate(M, trace, i):
    """The permanence certificate at step i of a trace: simulate the
    vehicle-only future, take C* and the door period, take m over every
    rival of norm at most C*, and PASS where C* < m. Returns
    (vehicle, C*, period, m, pass)."""
    vpl = trace[i][1]
    st0, L0 = dict(trace[i][3]), trace[i][4]
    st, L = dict(st0), L0
    costs, doors = [], []
    for _ in range(SIM_MOVES):
        r = door(M, vpl, st.get(vpl, 0), L)
        assert r is not INF, "the vehicle itself is priced out"
        costs.append(M.place_norm(vpl) ** r)
        doors.append(r)
        st[vpl] = st.get(vpl, 0) + r
        L = M.lam_state(st)
    Cstar = max(costs)
    period = _period(doors[SIM_MOVES // 2:])
    m = None
    for pl in M.UNIVERSE:
        if M.place_norm(pl) > Cstar:
            break
        if pl == vpl:
            continue
        c = cost_of(M, pl, st0.get(pl, 0), L0)
        if m is None or c < m:
            m = c
    # Without a witnessed period, C* is a max over a sample rather than a
    # supremum over the future, and the certificate would be unsound: a
    # cost cycle longer than the simulation could exceed it unseen. No
    # period, no certificate.
    return vpl, Cstar, period, m, (period is not None
                                   and (m is None or Cstar < m))


def certified_lock(M, trace):
    """The FIRST step whose certificate passes, scanning only the steps
    that move at the trace's own last place -- every other step is one the
    walk demonstrably leaves. Returns (index, cert) or (None, None)."""
    last = trace[-1][1]
    for i, t in enumerate(trace):
        if t[1] != last:
            continue
        cert = certificate(M, trace, i)
        if cert[4]:
            return i, cert
    return None, None


def moved_places(trace):
    return set(t[1] for t in trace)


# ------------------------------------------------ S1 the positive control
def s1_control(rings):
    section("S1  POSITIVE CONTROL -- Lemma A over five rings, a filed lock "
            "reproduced, and the re-implemented menu against the imported "
            "one, before any verdict is read")
    print("  Lemma A: lam(P^a) / (N(P) - 1) is a power of the residue")
    print("  characteristic at every place and depth. The corpus's three")
    print("  non-standard columns are the hard cases -- Z[i]'s plateau and")
    print("  the wild ring's level shift and phase shift.")
    print()
    print("  %-12s %-8s %-40s" % ("ring", "places", "verdict"))
    n = 0
    for name, M, rams in rings:
        for pl in M.UNIVERSE:
            if M.place_norm(pl) > 30:
                break
            p = M.place_char(pl)
            base = M.place_norm(pl) - 1
            for a in range(1, BRUTE_DEPTH + 1):
                lam = M.lam_P(pl, a)
                ok(lam % base == 0 if base else True,
                   "%s: lam(%s^%d) = %d is not a multiple of N - 1 = %d"
                   % (name, pl, a, lam, base))
                q = lam // base if base else lam
                ok(q == p ** v_p(q, p),
                   "%s: lam(%s^%d)/(N-1) = %d is not a power of %d"
                   % (name, pl, a, q, p))
                n += 1
        print("  %-12s %-8d %-40s"
              % (name, sum(1 for pl in M.UNIVERSE
                           if M.place_norm(pl) <= 30), "clean"))
    print("  %d (place, depth) readings, 0 off. Lemma A stands in range."
          % n)

    print()
    print("  The filed lock: the wild ring's void walk, through this file's")
    print("  own walker, against explore_wild_ring.py F4.")
    W3 = [m for nm, m, r in rings if nm == "Z[2^(1/3)]"][0]
    tr = walk(W3, {}, 20)
    i, vpl = witness_step(tr)
    ok(i is not None, "the wild ring's void walk does not lock")
    cost = tr[i][0]
    print("    lock place %s at cost %d, witnessed from step %d"
          % (show_pl(W3, vpl), cost, i + 1))
    print("    state at step 12: %s"
          % ", ".join("%s^%d" % (str(q), e)
                      for q, e in sorted(tr[11][3].items(),
                                         key=lambda kv: W3.place_key(kv[0]))
                      if e))
    ok(W3.place_norm(vpl) == 5 and cost == 5,
       "the filed lock is the place over 5 at cost 5; got %s at %d"
       % (str(vpl), cost))
    st12 = tr[11][3]
    ok(sorted((W3.place_char(q), e) for q, e in st12.items() if e)
       == [(3, 2), (5, 10)],
       "the filed support 3^2 * 5^10 at step 12; got %s" % str(st12))
    print("    filed lock reproduced.")

    print()
    print("  The re-implemented menu against the imported one, at every")
    print("  step of every walk inside the horizon the imported door_r can")
    print("  answer at all.")
    nmenu = 0
    for rname, M, rams in rings:
        for sname, seed in seeds_of(M, rams):
            st, L = dict(seed), M.lam_state(seed)
            for _ in range(40):
                c1, p1, r1 = menu(M, st, L)
                c2, ties = M.ideal_menu(st, L)
                p2, r2 = ties[0]
                ok((c1, p1, r1) == (c2, p2, r2),
                   "%s/%s: the local menu says (%s, %s, %s), the imported "
                   "one (%s, %s, %s)"
                   % (rname, sname, c1, p1, r1, c2, p2, r2))
                nmenu += 1
                st = dict(st)
                st[p1] = st.get(p1, 0) + r1
                L = M.lam_state(st)
    print("    %d menu readings, 0 off. The instrument stands." % nmenu)
    return n, nmenu


# ------------------------------------------------- S2 door monotonicity
def s2_monotone(walks):
    section("S2  LEMMA B -- a door never falls as the invariant grows, over "
            "every nested pair the walks produce")
    print("  Every walk's invariant sequence is a divisibility chain by")
    print("  construction (L is an lcm that only gains factors). For each")
    print("  consecutive pair the door is read at every place of norm at")
    print("  most %d at four exponents." % RIVAL_NORM)
    print()
    print("  %-12s %-20s %-8s %-8s" % ("ring", "seed", "pairs", "reads"))
    total, viol = 0, 0
    for name, M, sname, seed, tr in walks:
        Ls = [M.lam_state(seed)] + [t[4] for t in tr[:60]]
        npair, nread = 0, 0
        for a, b in zip(Ls, Ls[1:]):
            ok(b % a == 0, "%s/%s: the invariant chain breaks, %d then %d"
               % (name, sname, a, b))
            npair += 1
            for pl in M.UNIVERSE:
                if M.place_norm(pl) > RIVAL_NORM:
                    break
                for e in (0, 1, 2, 3):
                    if door(M, pl, e, b) < door(M, pl, e, a):
                        viol += 1
                    nread += 1
        total += nread
        print("  %-12s %-20s %-8d %-8d" % (name, sname, npair, nread))
    print("  %d door readings over the chains, %d violations." % (total, viol))
    ok(viol == 0, "Lemma B fails: %d doors fell as the invariant grew" % viol)
    return total


# ------------------------------------------------------ S3 the cost limit
def _primes_of(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def s3_cost_limit(walks, locks):
    section("S3  THE COST LIMIT -- what a vehicle-only run freezes, and "
            "door_inf against the eventual cost")
    print("  Over the certified stretch of each walk: every prime other")
    print("  than the vehicle's own holds its valuation in L (Lemma C),")
    print("  every rival's door is nondecreasing (Lemma B), and each")
    print("  rival's EVENTUAL door equals the closed form door_inf.")
    print()
    print("  %-12s %-19s %-9s %-7s %-7s %s"
          % ("ring", "seed", "vehicle", "frozen", "rivals",
             "priced out / off"))
    nrival_tot, noff_tot = 0, 0
    for name, M, sname, seed, tr in walks:
        i, cert = locks[(name, sname)]
        if i is None:
            print("  %-12s %-19s %s" % (name, sname, "NO CERTIFIED LOCK"))
            continue
        vpl = cert[0]
        p = M.place_char(vpl)
        L0, Lz = tr[i][4], tr[-1][4]
        frozen = all(v_p(L0, l) == v_p(Lz, l)
                     for l in _primes_of(L0) + _primes_of(Lz) if l != p)
        nrivals, noff, ndiverge = 0, 0, 0
        for pl in M.UNIVERSE:
            if M.place_norm(pl) > RIVAL_NORM:
                break
            if pl == vpl:
                continue
            e = tr[i][3].get(pl, 0)
            seq = [door(M, pl, e, t[4]) for t in tr[i:]]
            ok(all(x <= y for x, y in zip(seq, seq[1:])),
               "%s/%s: the door at %s falls under the lock"
               % (name, sname, str(pl)))
            # door_inf predicts a LIMIT, and the walk is finite: a finite
            # prediction must be STABILIZED by the half-horizon, and an
            # infinite one must still be climbing at the horizon. Reading
            # seq[-1] against door_inf directly would call every
            # priced-out place a miss, its door being finite at every
            # finite step.
            di = door_inf(M, pl, e, L0, p)
            half, end = seq[len(seq) // 2], seq[-1]
            if di is None:
                ndiverge += 1
                if not (end > half):
                    noff += 1
            elif not (end == di and half == di):
                noff += 1
            nrivals += 1
        print("  %-12s %-19s %-9s %-7s %-7d %d / %d"
              % (name, sname, show_pl(M, vpl),
                 "yes" if frozen else "NO", nrivals, ndiverge, noff))
        ok(frozen, "%s/%s: a prime other than %d moved under the lock"
           % (name, sname, p))
        ok(noff == 0, "%s/%s: %d rivals miss the door_inf closed form"
           % (name, sname, noff))
        nrival_tot += nrivals
        noff_tot += noff
    print("  %d rival readings, %d off the closed form."
          % (nrival_tot, noff_tot))
    return nrival_tot


# ------------------------------------------------------ S4 the certificate
def s4_certificate(walks, locks):
    section("S4  THE LOCK PERMANENCE CERTIFICATE -- C* against m, and the "
            "witness it disagrees with")
    print("  At a candidate step: simulate the vehicle-only future for %d"
          % SIM_MOVES)
    print("  moves, take C* = its largest cost and the period of its door")
    print("  cycle, take m = the cheapest rival at that step, and PASS")
    print("  where C* < m. Beside it the walker's own witness -- %d"
          % LOCK_R)
    print("  consecutive moves at one place -- which proves nothing.")
    print()
    print("  %-12s %-19s %-9s %-5s %-5s %-6s %-6s %-5s %s"
          % ("ring", "seed", "vehicle", "cert", "wit", "C*", "m", "per",
             "witness place"))
    ncert = 0
    for name, M, sname, seed, tr in walks:
        i, cert = locks[(name, sname)]
        w, wpl = witness_step(tr)
        if i is None:
            print("  %-12s %-19s %s" % (name, sname, "NO CERTIFIED LOCK"))
            continue
        vpl, Cstar, period, m, passed = cert
        ok(period is not None,
           "%s/%s: a certificate passed with no witnessed door period"
           % (name, sname))
        ncert += 1
        ok(all(t[1] == vpl for t in tr[i:]),
           "%s/%s: the certificate passed at step %d and the walk left %s"
           % (name, sname, i + 1, str(vpl)))
        print("  %-12s %-19s %-9s %-5d %-5s %-6d %-6s %-5s %s"
              % (name, sname, show_pl(M, vpl), i + 1,
                 str(w + 1) if w is not None else "-", Cstar,
                 str(m) if m is not None else "none", str(period),
                 show_pl(M, wpl) if wpl is not None else "-"))
    print("  %d of %d walks carry a permanence certificate."
          % (ncert, len(walks)))
    return ncert


# ------------------------------- S5 the support bound and the dichotomy
def cross_supply(M, moved, st):
    """The residue-route term the carrier floor prices: for a place Q a
    MOVE seated and any prime p that is the characteristic of some OTHER
    seated place, v_p(N(Q) - 1). The pairing is explore_wild_ring.py F5's,
    so the readings are comparable with its filed maximum."""
    chars = set(M.place_char(x) for x, e in st.items() if e)
    out = 0
    for q in moved:
        for p in chars:
            if p == M.place_char(q):
                continue
            out = max(out, v_p(M.place_norm(q) - 1, p))
    return out


def _max_surplus(M, st, L):
    out = 0
    for q, e in st.items():
        if not e:
            continue
        p = M.place_char(q)
        out = max(out, v_p(L, p) - v_p(M.lam_P(q, e), p))
    return out


def s5_support_and_surplus(walks, locks):
    section("S5  THE SUPPORT BOUND, THE RACE BOUND, AND THE SURPLUS "
            "DICHOTOMY AT %d MOVES" % HORIZON)
    print("  support bound: every norm a MOVE seats is at most the largest")
    print("  cost the walk pays (a planted seed is exempt by construction,")
    print("  being given rather than bought).")
    print("  race bound: the cross-supply v_p(N(Q)-1) at most log_p C.")
    print("  dichotomy: the surplus diverges exactly where the vehicle's")
    print("  own characteristic hosts a second seated place.")
    print()
    print("  %-12s %-19s %-5s %-5s %-4s %-4s %-6s %-6s %-6s %s"
          % ("ring", "seed", "maxN", "maxC", "sup", "cap", "sur60",
             "sur500", "slope", "cochar"))
    rows = []
    for name, M, sname, seed, tr in walks:
        maxC = max(t[0] for t in tr)
        moved = moved_places(tr)
        maxN = max(M.place_norm(q) for q in moved)
        ok(maxN <= maxC,
           "%s/%s: a move seated norm %d against every cost paid %d"
           % (name, sname, maxN, maxC))
        st_end, L_end = tr[-1][3], tr[-1][4]
        s60 = _max_surplus(M, tr[59][3], tr[59][4])
        shalf = _max_surplus(M, tr[HORIZON // 2][3], tr[HORIZON // 2][4])
        s500 = _max_surplus(M, st_end, L_end)
        i, cert = locks[(name, sname)]
        cochar, sup, cap = False, 0, 0
        if i is not None:
            vpl = cert[0]
            p = M.place_char(vpl)
            cochar = any(q != vpl and e and M.place_char(q) == p
                         for q, e in st_end.items())
            sup = cross_supply(M, moved, st_end)
            while 2 ** (cap + 1) <= maxC:
                cap += 1
            ok(sup <= cap, "%s/%s: cross-supply %d beats the race bound %d"
               % (name, sname, sup, cap))
        slope = s500 - shalf
        print("  %-12s %-19s %-5d %-5d %-4d %-4d %-6d %-6d %-6d %s"
              % (name, sname, maxN, maxC, sup, cap, s60, s500, slope,
                 "yes" if cochar else "no"))
        ok((slope > 0) == cochar,
           "%s/%s: the dichotomy fails -- slope %d, co-characteristic %s"
           % (name, sname, slope, cochar))
        rows.append((name, sname, maxN, maxC, sup, cap, s60, s500, slope,
                     cochar))
    ndiv = sum(1 for r in rows if r[9])
    print("  %d of %d walks diverge, and the co-characteristic criterion "
          "calls every one." % (ndiv, len(rows)))
    return rows


# ------------------------------- S6 the designed co-characteristic seed
def s6_designed(rings, walks, locks):
    section("S6  THE DESIGNED CO-CHARACTERISTIC SEED -- the dichotomy's "
            "other side, constructed because no walk supplied it")
    print("  Plant, one at a time, every place sharing the void walk's")
    print("  certified vehicle's characteristic, and walk the same %d"
          % HORIZON)
    print("  moves. The surplus at such a place is v_p(L) minus a frozen")
    print("  number, so it must climb with the vehicle's own column.")
    print()
    print("  %-12s %-15s %-9s %-5s %-6s %-6s %-6s %-6s %s"
          % ("ring", "planted", "vehicle", "cert", "sur60", "sur500",
             "dv_p", "maxN<=C", "cochar"))
    rows = []
    for name, M, rams in rings:
        i, cert = locks[(name, "void")]
        if i is None:
            continue
        vpl = cert[0]
        p = M.place_char(vpl)
        mates = [pl for pl in M.UNIVERSE
                 if M.place_char(pl) == p and pl != vpl]
        if not mates:
            print("  %-12s %-15s (no other place over %d)" % (name, "-", p))
            continue
        for q in mates:
            tr = walk(M, {q: 1}, HORIZON)
            j, c2 = certified_lock(M, tr)
            st_end, L_end = tr[-1][3], tr[-1][4]
            s60 = _max_surplus(M, tr[59][3], tr[59][4])
            s500 = _max_surplus(M, st_end, L_end)
            shalf = _max_surplus(M, tr[HORIZON // 2][3], tr[HORIZON // 2][4])
            maxC = max(t[0] for t in tr)
            moved = moved_places(tr)
            maxN = max(M.place_norm(x) for x in moved)
            ok(maxN <= maxC,
               "%s/designed %s: a move seated norm %d against every cost "
               "paid %d" % (name, str(q), maxN, maxC))
            cochar = False
            v2 = c2[0] if j is not None else None
            if j is not None:
                p2 = M.place_char(v2)
                cochar = any(x != v2 and e and M.place_char(x) == p2
                             for x, e in st_end.items())
                sup = cross_supply(M, moved, st_end)
                cap = 0
                while 2 ** (cap + 1) <= maxC:
                    cap += 1
                ok(sup <= cap,
                   "%s/designed %s: cross-supply %d beats the race bound %d"
                   % (name, str(q), sup, cap))
            dv = v_p(L_end, M.place_char(v2)) - v_p(tr[59][4],
                                                    M.place_char(v2)) \
                if j is not None else 0
            print("  %-12s %-15s %-9s %-5s %-6d %-6d %-6d %-6s %s"
                  % (name, str(q), show_pl(M, v2) if v2 else "-",
                     str(j + 1) if j is not None else "none", s60, s500, dv,
                     "%d<=%d" % (maxN, maxC), "yes" if cochar else "no"))
            ok((s500 - shalf > 0) == cochar,
               "%s/designed %s: the dichotomy fails -- slope %d, "
               "co-characteristic %s"
               % (name, str(q), s500 - shalf, cochar))
            if cochar:
                ok(s500 - s60 == dv,
                   "%s/designed %s: the surplus gained %d and v_p(L) gained "
                   "%d" % (name, str(q), s500 - s60, dv))
            rows.append((name, q, v2, j, s60, s500, dv, cochar))
    ndiv = sum(1 for r in rows if r[7])
    print("  %d designed walks, %d of them divergent." % (len(rows), ndiv))

    print()
    print("  ROUND 2 -- every place over p planted at once, so that")
    print("  whichever becomes the vehicle another is seated beside it.")
    print()
    print("  %-12s %-6s %-9s %-5s %-6s %-6s %-6s %s"
          % ("ring", "over", "vehicle", "cert", "sur60", "sur500", "dv_p",
             "cochar"))
    rows2 = []
    for name, M, rams in rings:
        i, cert = locks[(name, "void")]
        if i is None:
            continue
        p = M.place_char(cert[0])
        over = [pl for pl in M.UNIVERSE if M.place_char(pl) == p]
        if len(over) < 2:
            print("  %-12s %-6d (only one place over it)" % (name, p))
            continue
        tr = walk(M, {pl: 1 for pl in over}, HORIZON)
        j, c2 = certified_lock(M, tr)
        st_end, L_end = tr[-1][3], tr[-1][4]
        s60 = _max_surplus(M, tr[59][3], tr[59][4])
        s500 = _max_surplus(M, st_end, L_end)
        shalf = _max_surplus(M, tr[HORIZON // 2][3], tr[HORIZON // 2][4])
        maxC = max(t[0] for t in tr)
        maxN = max(M.place_norm(x) for x in moved_places(tr))
        ok(maxN <= maxC, "%s/round 2: a move seated norm %d against every "
           "cost paid %d" % (name, maxN, maxC))
        cochar, dv, v2 = False, 0, None
        if j is not None:
            v2 = c2[0]
            p2 = M.place_char(v2)
            cochar = any(x != v2 and e and M.place_char(x) == p2
                         for x, e in st_end.items())
            dv = v_p(L_end, p2) - v_p(tr[59][4], p2)
        print("  %-12s %-6d %-9s %-5s %-6d %-6d %-6d %s"
              % (name, p, show_pl(M, v2) if v2 else "-",
                 str(j + 1) if j is not None else "none", s60, s500, dv,
                 "yes" if cochar else "no"))
        ok((s500 - shalf > 0) == cochar,
           "%s/round 2: the dichotomy fails -- slope %d, co-characteristic "
           "%s" % (name, s500 - shalf, cochar))
        if cochar:
            ok(s500 - s60 == dv,
               "%s/round 2: the surplus gained %d and v_p(L) gained %d"
               % (name, s500 - s60, dv))
        rows2.append((name, p, v2, j, s60, s500, dv, cochar))
    ndiv2 = sum(1 for r in rows2 if r[7])
    print("  %d round-2 walks, %d of them divergent." % (len(rows2), ndiv2))
    return rows, rows2


def main():
    rings = load_rings()
    n_lemA, n_menu = s1_control(rings)
    walks = []
    for name, M, rams in rings:
        for sname, seed in seeds_of(M, rams):
            walks.append((name, M, sname, seed, walk(M, seed, HORIZON)))
    locks = {}
    for name, M, sname, seed, tr in walks:
        locks[(name, sname)] = certified_lock(M, tr)
    n_mono = s2_monotone(walks)
    n_riv = s3_cost_limit(walks, locks)
    ncert = s4_certificate(walks, locks)
    rows = s5_support_and_surplus(walks, locks)
    des, des2 = s6_designed(rings, walks, locks)

    section("VERDICT -- the predictions read against what printed")
    print("  P1 %d Lemma A readings, %d menu readings, the filed lock:"
          " see S1" % (n_lemA, n_menu))
    print("  P2 %d door readings, monotone: see S2" % n_mono)
    print("  P3 %d rival readings against door_inf: see S3" % n_riv)
    print("  P4 %d of %d walks certified: see S4" % (ncert, len(walks)))
    print("  P5 the support bound: see S5")
    print("  P6 the race bound: see S5")
    print("  P7 %d of %d walks diverge: see S5"
          % (sum(1 for r in rows if r[9]), len(rows)))
    print("  Q1-Q3 %d designed walks, %d divergent: see S6"
          % (len(des), sum(1 for r in des if r[7])))
    print("  Q4 %d round-2 walks, %d divergent: see S6"
          % (len(des2), sum(1 for r in des2 if r[7])))
    print("\n  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
