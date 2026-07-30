"""explore_undercut_nf.py -- does the separation lemma run over a number
ring?

THE QUESTION. One fact is proved twice by two unrelated arguments. An
exponent being FROZEN -- a coordinate settled forever, which is what lets a
limit be NAMED rather than censused -- is delivered over the function fields
by the UNDERCUT LEMMA, which compares two places' door prices and shows the
gap between them can never close. Over the two number rings the same
conclusion rests instead on the LOCK: once the recurrent vehicle touches only
a fixed set of places, every exponent outside that set stops moving.
explore_undercut.py F2 states the gap exactly -- the freeze is the undercut
in SHAPE, its cases live over the number rings where that rig carries
nothing, and whether they are literally instances "is a question about door
prices over a number ring, and it is banked rather than answered". This file
answers it.

THE DOOR ARITHMETIC OVER A NUMBER RING, re-derived from the engines rather
than remembered. lam_P(X, a) is the exponent of (O/X^a)^*, which is
lcm(N(X) - 1, p^m_X(a)) with p the residue characteristic: the residue field
contributes the cyclic factor N(X) - 1 at EVERY depth, and the principal
units contribute a p-group whose level m_X(a) climbs X's own ladder. L is
the lcm over seated places. A SEATED place already has N(X) - 1 | L, so its
door loses the prime-to-p clause entirely and reads ONE p-adic valuation.
Write kappa_p = v_p(L) and

    next_X(kappa) = least a with m_X(a) > kappa      (the (kappa+1)-th rung)
    sigma_X       = next_X(kappa_{p(X)}) - e_X       (the door radius)
    cost(X)       = N(X)^sigma_X

and the ladder gap g_X(kappa) = next_X(kappa) - next_X(kappa-1), which is
X's RAMIFICATION INDEX in the tail and can be wider over a head.

WHERE THIS DIFFERS FROM F_2[x], which is the whole of the port. There every
place has residue characteristic 2 and m_X(a) = ceil(log2 a) at every place
alike: ONE kappa, ONE ladder, so next(kappa) = T + 1 with T = 2^kappa and
sigma_X = T + 1 - e_X, and every place's sigma rises by T' - T together. A
number ring breaks that in two independent ways. kappa is a VECTOR over the
rational primes, so two places share a clock only if they share a residue
characteristic; and inside one characteristic the ladder is per-place, so
the sigmas rise by DIFFERENT amounts.

THE HAND-ATTACK, on paper before any engine code. Invariant I: cost(Q) <
cost(P), with N(Q) <= N(P). Log-costs inside one characteristic are
f_X * sigma_X in units of log p, f_X the residue degree.

 A. THE CASES, against the function-field lemma's own list.
    - a clock move at R above q != p(P) = p(Q): kappa_p is untouched, since
      raising e_R raises only v_q(L) -- N(R) - 1 is depth-free. Both sigmas
      stand and the gap is PRESERVED. A case the function field does not
      have, and a harmless one.
    - a clock move at R above p, R outside {P, Q}: the mover lands on
      next_R(kappa), whose level is kappa + 1, so kappa_p rises by exactly
      one. sigma_P rises by g_P and sigma_Q by g_Q, and the gap changes by
      f_P*g_P - f_Q*g_Q. THIS IS THE PORT'S FIRST HYPOTHESIS and it is not
      implied by N(Q) <= N(P): over F_2[x] the two gaps are the same number
      and factor out, leaving the degree comparison; over a number ring the
      tail gap is the ramification index, so the comparison is by e*f -- the
      LOCAL DEGREE -- and a wide cheap place can outrun a narrow dear one.
    - a clock move at Q: sigma_Q resets to g_Q and sigma_P rises by g_P, so
      the same hypothesis carries it with sigma_P >= 1, exactly as over a
      function field.
    - a clock move at P: impossible while I holds, Q's door being an
      admissible move that is strictly cheaper.
    - a fresh move at P or Q: excluded by ineligibility, which is permanent
      because L only grows.
    - a rider landing on Q drops sigma_Q and widens the gap; a rider landing
      on P is excluded by hypothesis.
    - A FRESH MOVE ANYWHERE, which is the second break and has no
      function-field shadow at all. Over F_2[x] a fresh move multiplies
      lambda by the ODD 2^d - 1 and cannot touch T. Over a number ring
      N(R) - 1 carries a p-part for many p at once, so seating a fresh place
      ANYWHERE can jump kappa_p by an arbitrary amount j >= 0 -- the measured
      excess is unbounded (explore_populated_door.py). Inside one
      characteristic that is j levels of the same case above and the same
      hypothesis carries it. ACROSS characteristics it is fatal: kappa_{p(Q)}
      can jump with kappa_{p(P)} standing, so cost(Q) climbs while cost(P)
      does not and the gap closes.
 B. SO THE PORTED LEMMA, with the two hypotheses that are invisible in equal
    characteristic. If at some state P and Q satisfy
      (H0) p(P) = p(Q) -- one residue characteristic, hence one clock;
      (H1) f_P * g_P(k) >= f_Q * g_Q(k) at every level k the walk can cross,
           which in the tail is e_P*f_P >= e_Q*f_Q, the local degree;
      (H2) cost(Q) < cost(P), and neither can be seated FRESH;
      (H3) no rider can carry P (element world only),
    then P is never a minimal move again and its exponent is FROZEN. Both
    (H0) and (H1) are vacuous over F_2[x], which is why the source lemma
    states neither: one characteristic, one shared ladder. The unified
    reading is that the undercut compares LOCAL DEGREES, and reading it as
    the norm was the equal-characteristic coincidence.
 C. WHAT REPLACES THE GENUS. The element world's vehicle is a core times the
    minimal representative of the class that power must cancel, so
    N(P)^sigma_P <= cost(P) <= N(P)^sigma_P * C with C the largest norm of a
    minimal integral representative of a class -- and the certificate needs
    the cost gap to clear a factor C. Over a function field that constant is
    bounded by the GENUS, every class of degree at least g carrying an
    effective representative; over a number ring by MINKOWSKI's bound. So
    the slack is ONE object in both worlds -- the class group's covering
    norm -- and the genus is its function-field name. The
    same-degree-different-classes certificate reaches the same constant
    (explore_class_species_nf.py), and by the same route rather than by the
    same argument: both vehicles carry a minimal representative.
 D. WHAT THE HAND-ATTACK PREDICTS ABOUT THE ANSWER. (H0) is a strong
    condition over a QUADRATIC ring: two places above one rational prime
    means a split pair, which is Galois-conjugate and therefore of equal
    norm, equal residue degree and equal ladder -- so (H1) holds with
    equality and the certificate reduces to "the shallower conjugate is
    frozen". It also cannot be met by an unseated witness: an unseated
    conjugate sits at exponent 0, where its door is the WIDEST any place of
    that ladder has, so it is dearer than its seated partner and never the
    cheap side. The witness must therefore be a SEATED place above the same
    rational prime -- and explore_populated_door.py reports that of 717 swept
    readings not one state carries two seated places of equal
    characteristic.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the function fields to the number rings: the SHAPE of the induction
    and nothing else. Every quantity in it -- the tick, the ladder, the
    degree comparison, the genus -- is re-derived here from the number
    ring's own arithmetic, and the two hypotheses above are what the
    re-derivation adds. No figure crosses.
 2. From the ideal world to the element world: the sigma recurrence and the
    monotone gap, stated for bare place powers. C above names the two holes
    the rider opens and the rig carries the slack explicitly.
 3. From explore_populated_door.py's 717 swept readings to the states walked
    here: nothing. Its census is over its own sweep and is re-measured here
    on the states this file's seeds actually reach.
 4. The lemma is asserted against the searches' own rejoin behaviour, which
    is what would catch it being wrong.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE DOOR IS ONE VALUATION AND THE LADDER IS THE PLACE'S OWN. What the
    rig PRINTS: over every place of both rings at depths 0..12, the engine's
    door_r against next_X(kappa) - e computed from m_X read off lam_P, at
    every kappa the depth admits; and each place's tail ladder gap against
    its ramification index.
    KILL: one mismatch. The whole argument is arithmetic on these two
    identities.
PR2 A CLOCK MOVE ADVANCES ONE CHARACTERISTIC'S COUNTER BY ONE. What the rig
    PRINTS: at every move of every walked state, the kappa vector before and
    after, split by whether the move seats a place freshly or clocks a
    seated one.
    KILL: one clock move at a place above p that changes kappa_q for some
    q != p, or that changes kappa_p by other than one. The FRESH half is
    printed and not predicted -- that a fresh seating can move any component
    is the mechanism, not a claim under test.
PR3 THE PORTED CERTIFICATE FREEZES WHAT IT CERTIFIES. What the rig PRINTS:
    every certified (place, witness) pair on a walked state, followed along
    the canonical continuation with the certified place's exponent at each
    step.
    KILL: one certified place whose exponent moves.
PR4 THE SAME-CHARACTERISTIC HYPOTHESIS IS THE BINDING ONE. What the rig
    PRINTS: per ring per world, over every state the searches walk, the
    number carrying two places above one rational prime with the cheaper one
    strictly cheaper -- counted separately for seated/seated and for
    seated/unseated-but-ineligible witnesses.
    KILL: a nonzero seated/seated count, which would mean the port has cases
    to speak about after all.
PR5 THE FREEZE'S CASES ARE NOT UNDERCUT INSTANCES. What the rig PRINTS: for
    every seed whose limits separate at a FROZEN finite place, that place
    and the ported certificate run over every candidate witness in the
    universe below the state's own cost, with the refusal reason per witness.
    KILL: one frozen place the ported certificate certifies -- which would
    settle the question the other way and unify the two arguments.
PR6 WHAT THE LOCK USES INSTEAD, printed and not predicted: for each frozen
    place, whether kappa at its own residue characteristic stops rising once
    the walk locks, and whether the recurrent vehicle's cost is flat and
    strictly below the frozen place's own door cost.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE UNDERCUT PORTS, AND WHAT IT COMPARES IS THE LOCAL DEGREE (proved for
   the ideal world -- lemma B above, an induction over the move model
   calling on no computation; a rule in range in the element world, where
   the slack is measured). THE TWO IDENTITIES IT RESTS ON ARE NOT THIS
   FILE'S and are re-read here as controls rather than found: that a seated
   place's door is one p-adic valuation is filed as a PROPERTY
   (explore_populated_door.py), and that a place's tail ladder gap is its
   ramification index is filed as a rule in range over the same 90 places
   (explore_tick_pump.py). What S1 adds is that the LADDER READING this
   file computes agrees with the engine's own door loop -- 5945 (place,
   depth, level) readings over the 90 places of norm at most 200 in the two
   rings, 0 off, and a constant tail gap equal to the ramification index at
   90 of 90.
   The lemma needs two hypotheses the function-field statement does not
   carry, and both are VACUOUS in equal characteristic rather than absent:
   the frozen place and its witness must share a RESIDUE CHARACTERISTIC,
   since kappa is a vector and two places above different rational primes
   share no clock at all; and the comparison is by degree times LADDER GAP,
   which in the tail is e*f, the LOCAL DEGREE, and not by the norm. Over
   F_2[x] there is one characteristic and one shared ladder, so the gap
   factors out of the comparison and leaves the degree -- which is why the
   source lemma reads as a statement about degrees. It is a statement about
   local degrees, and the degree reading was the coincidence.
   THE LOCAL-DEGREE HALF IS DERIVED AND NOT EXERCISED, which is this
   result's own boundary. Both rings here are QUADRATIC, where two places
   above one rational prime can only be a conjugate SPLIT pair: equal norm,
   equal ramification, equal ladder. So (H1) holds with EQUALITY at every
   pair either ring can present, and nothing here distinguishes comparing by
   e*f from comparing by f. Separating them needs a ring with a rational
   prime under two places of different ramification -- degree three at the
   least -- or a universe whose ladders are dialled rather than derived.
   EXERCISED BY explore_cubic_undercut.py, on the engine
   explore_cubic_ring.py, at 23 = P*Q^2 in Q[x]/(x^3 - x - 1): the two
   readings disagree there and the e*f one is right, a fresh seating
   carrying 23^3 reversing the cost gap this induction claims to preserve.
   What that does NOT settle is anything about a WALK -- the ring has no
   head at any place, so its greedy walk clocks one place forever.

F2 AND THE FREEZE'S CASES ARE INSTANCES -- the banked question answers YES
   (rule in range; 36 of 36 frozen (seed, place) records certified over both
   rings and both worlds, 0 refused; 35 distinct certified pairs followed
   with 0 exponents moving over 12 menu moves and 12 applications of the
   lock's own recurrent vehicle). AND IT FIRES BEFORE THE LOCK AT 34 OF THE
   36, by 1 to 5 moves, which is the number that keeps the finding from
   being circular: at the locked state the walk is already recurrent, so a
   certificate read only there asserts little the lock does not, and the
   first draft of this section read only there. EACH RECORD IS CERTIFIED IN
   EXACTLY ONE OF THE TWO BRANCHES, and the split is even at every cell --
   4/4, 10/10, 4/4 -- which is asserted and not merely observed: a conjugate
   pair freezes one member per branch, so a place certified in both would be
   frozen in the branch that moves it, and one certified in neither would be
   a case the port misses. Every place the
   lock freezes is a SPLIT place, at 36 of 36 -- which is exactly the
   configuration (H0) demands, a second place above the same rational
   prime. So (H0) is not the limitation it looks like; it is a PREDICTION
   about which coordinates a number ring can freeze, and the freeze's own
   cases meet it everywhere. The branch structure is that same
   reading: where two limits differ at a conjugate pair, each branch
   freezes the DEARER member and the cheaper one there is that branch's
   witness, so no single branch can certify both and reading only the
   canonical one covers exactly half.

F3 THE HYPOTHESIS IS MET AWAY FROM THE LOCK TOO, so the port is not a
   restatement of the freeze (rule in range; 263 walked states over the four
   cells, 50 of them carrying two seated places above one rational prime,
   and 22 such PAIRS -- counted per pair, where the 50 is per state --
   carrying a cost gap, of which 10 are certified). The 12 refusals are 10
   with no cost gap once the covering norm is charged as slack, and 2 with
   the frozen place
   inside the rider set -- hypotheses, not absences. This also fixes the
   scope of a neighbouring census: explore_populated_door.py reports no
   swept state carrying two SEATED places of equal characteristic, and that
   is a fact about ITS sweep -- on these seed belts 50 walked states carry
   one.

F4 A CLOCK MOVE ADVANCES ONE CHARACTERISTIC BY ONE, EXCEPT WHERE THE RIDER
   RIDES THE SAME CLOCK (rule in range; 51 of 51 ideal-world clock moves at
   exactly one component and exactly one level, 0 off; the element world
   reaching a jump of 2). PR2's kill fired, and in the element world only.
   A vehicle there is a core times the minimal representative of the class
   it must cancel, and when that representative lands on a second place of
   the CORE'S OWN characteristic the two raise that component together. The
   prediction was written unscoped over a world whose move is not a bare
   place power; what survives unscoped is the weaker law the induction
   actually uses, that every component which moves is the characteristic of
   a place the vehicle carries, and that holds at every move of every walked
   state. The lemma is untouched, but not for the reason that first
   suggests itself: the repair is NOT case (f), which covers only a rider
   landing on P or on Q. A two-level jump is case (b) applied twice, and
   (H1) is quantified over EVERY level the walk crosses rather than over one
   -- which is what makes the hypothesis robust to a jump of any size, and
   is why case (g) needed no separate clause either. What the miss does cost
   is the tick recurrence: in the element world it is not the bare-power
   one, and any argument reading a single level off a single move is wrong
   there.

F5 SO THE TWO ARGUMENTS ARE TWO SUFFICIENT CONDITIONS FOR ONE INVARIANT,
   NOT ONE LEMMA TWICE (rule in range; 58 frozen (place, state) records,
   kappa at the frozen place's own characteristic unmoved after 12
   applications of the recurrent vehicle at 58 of 58, and that vehicle's
   cost flat across those 12 and strictly below the frozen place's own
   price at 58 of 58, each read in its world's own currency). The undercut
   holds an invariant while BOTH prices move, by a monotone gap; the lock
   holds it because NEITHER price moves, the
   recurrent vehicle not reaching that characteristic at all -- read over
   twelve applications of it, which is a measurement and not a forever. The
   undercut
   is the stronger of the two where it applies, needing no recurrence and
   speaking at states the walk is still opening from -- F3's 10 pairs are
   all such states. What the lock adds is the cases the undercut cannot
   reach, which over a quadratic ring are the places with no conjugate:
   inert and ramified places, sole above their rational prime, where (H0)
   is unmeetable by construction and stasis is the only argument left.

F6 AND THE GENUS'S COUNTERPART IS THE CLASS GROUP'S COVERING NORM (a
   derivation, used as the element world's slack throughout above). The
   element vehicle is a core times a minimal class representative, so a
   place's price sits between its bare door and that door times the largest
   minimal-representative norm, and the certificate needs the cost gap to
   clear that factor. Over a function field it is bounded by the GENUS,
   every class of degree at least g carrying an effective representative;
   over a number ring by MINKOWSKI's bound. One object, two names. The
   same-degree-different-classes certificate reaches the same constant by
   the same route rather than by the same argument -- both vehicles carry a
   minimal representative -- so the coincidence is in the vehicle and not in
   the two lemmas.

Run: `python explore_undercut_nf.py`. RUN RECORD (6840 assertions here plus
the imported engines' own, 0.48 s). S1: 2912 and 3033 door readings over 44
and 46 places, the engine's door_r equal to next(kappa) - e at every one; a
constant tail gap at every place and that gap the ramification index at 44 of
44 and 46 of 46; the certificate ACCEPTING a planted conjugate pair at depths
1 and 3 at both rings and REFUSING the same pair with the dear member as
witness, a cross-characteristic witness (at H0), and a place against itself.
S2: 53, 124, 29 and 57 moves over the four cells; every clock move moving
only components its vehicle lies above, the ideal world at exactly one
component and one level and K23's element world reaching two. S3: 4, 9, 11
and 26 STATES with a seated same-characteristic pair, 0, 4, 3 and 15 such
PAIRS with a cost gap, 0, 4, 3 and 3 of those certified; no unseated witness
cheaper than a seated place at any of the 263 states. S4: 8, 20, 0 and 8
frozen records, ALL certified with 0 refused, the frozen place a SPLIT place
at 36 of 36, the two branches splitting them 4/4, 10/10 and 4/4, and the
certificate firing
before the lock at 8, 18 and 8 of them -- 34 of 36 -- with leads of 1..1,
1..5 and 1..3 moves. S5: 35 distinct certified
pairs, 0 exponents moving. S6: 22, 18, 11 and 7 frozen records with kappa
stopped and the recurrent vehicle cheaper at all of them. Slate PR1-PR6:
PR1, PR3 and PR6 hit; PR2 MISSED in the element world (F4) and hit in the
ideal; PR4 and PR5 both MISSED, and both are the interesting direction --
PR4 predicted the same-characteristic hypothesis unmeetable on walked states
and it is met at 50, PR5 predicted the freeze's cases uncovered and 36 of 36
are covered. The hand-attack's own D was the source of both misses: it read
a neighbouring rig's census as a fact about walked states in general
(transplant flag 3 named that risk and the flag was right). Unfrozen finds:
the branch split -- each conjugate frozen in exactly one branch, which is
what turned a canonical-only 18 of 36 into 36 of 36 (F2) -- the currency
mismatch S6 was
first written with -- a bare door against a full vehicle, which read 8 of 18
where the matched comparison reads 18 of 18 -- and F6's identification of
the slack.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_number_field_lock as K5      # the h = 2 ring
import explore_module_law as K23            # the h = 3 ring
import explore_greedy_image_nf as NF        # the two searches and the belts
import explore_class_species_nf as CS       # the class layer and the walks

CHECKS = 0
DEPTH_CAP = 12          # depths a place is read at in the control
LEVEL_CAP = 10          # ladder levels the hypothesis is checked over


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg


def section(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


def show(pl):
    return CS.show(pl)


def show_st(st):
    return CS.show_st(st)


# ---------------------------------------------------------- the ladder layer
def v_p(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def m_level(M, pl, a):
    """The principal-unit level of X^a: v_p of lam_P with p the residue
    characteristic. The prime-to-p factor N(X) - 1 is depth-free, so this is
    the whole of what a seated place's door reads."""
    return v_p(M.lam_P(pl, a), M.place_char(pl))


def next_rung(M, pl, kappa, cap=400):
    """The least depth whose level exceeds kappa -- the (kappa+1)-th rung of
    this place's own ladder."""
    for a in range(1, cap):
        if m_level(M, pl, a) > kappa:
            return a
    ok(False, "ladder runaway at %s beyond depth %d" % (show(pl), cap))


def ladder_gap(M, pl, kappa):
    """next(kappa) - next(kappa - 1); the ramification index in the tail."""
    lo = next_rung(M, pl, kappa - 1) if kappa >= 1 else 0
    return next_rung(M, pl, kappa) - lo


def place_f(M, pl):
    """The residue degree, read off the RING rather than off the tag. N(X)
    is p^f by definition, so f is one valuation and no tag alphabet is
    needed -- reading 'inert' as f = 2 is the QUADRATIC case, where a place
    is rational or the square of one and nothing else. This was the only
    helper here taking no ring argument, and it is the line that assumed
    two."""
    n, p, f = M.place_norm(pl), M.place_char(pl), 0
    while n % p == 0:
        n //= p
        f += 1
    return f


def place_e(M, pl):
    return M.place_ef(pl) // place_f(M, pl)


def kappa_vec(L):
    """v_p(L) at every rational prime dividing L."""
    out, n, d = {}, L, 2
    while d * d <= n:
        if n % d == 0:
            v = 0
            while n % d == 0:
                n //= d
                v += 1
            out[d] = v
        d += 1
    if n > 1:
        out[n] = 1
    return out


def kappa_at(L, p):
    return v_p(L, p)


def cost_of(M, pl, e, L):
    return M.place_norm(pl) ** M.door_r(pl, e, L)


def eligible_fresh(M, pl, L):
    """A place that can still be seated FRESH -- its residue factor is not
    yet in the invariant, so its door is 1 and its price is its norm."""
    return L % (M.place_norm(pl) - 1) != 0


# ------------------------------------------------------------ THE CERTIFICATE
def certificate(R, world, st, L, P, Q):
    """The ported undercut. Returns (True, "") or (False, reason) naming the
    FIRST hypothesis that fails, in the order (H0), (H2)-eligibility, (H2)-
    cost, (H1), (H3)."""
    M = R.M
    if M.place_char(P) != M.place_char(Q):
        return False, "H0 different characteristic"
    if P == Q:
        return False, "H0 same place"
    eP, eQ = st.get(P, 0), st.get(Q, 0)
    if eligible_fresh(M, P, L) or eligible_fresh(M, Q, L):
        return False, "H2 a member is still fresh-eligible"
    cP, cQ = cost_of(M, P, eP, L), cost_of(M, Q, eQ, L)
    if world == "element":
        cQ *= max(R.minnorm.values())          # the covering norm, as slack
    if not cQ < cP:
        return False, "H2 no cost gap"
    fP, fQ = place_f(M, P), place_f(M, Q)
    kap = kappa_at(L, M.place_char(P))
    for k in range(kap + 1, kap + 1 + LEVEL_CAP):
        if fP * ladder_gap(M, P, k) < fQ * ladder_gap(M, Q, k):
            return False, "H1 local degree at level %d" % k
    if M.place_ef(P) < M.place_ef(Q):
        return False, "H1 local degree in the tail"
    if world == "element" and P in R.rider:
        return False, "H3 P lies in the rider set"
    return True, ""


def witnesses(R, world, st, L, P):
    """Every candidate witness for P: the places above P's own rational prime
    within the universe. Seated ones and ineligible unseated ones both
    qualify -- the source lemma admits either."""
    M = R.M
    p = M.place_char(P)
    return [X for X in M.UNIVERSE if M.place_char(X) == p and X != P]


def best_certificate(R, world, st, L, P):
    """(True, witness, "") at the first witness that certifies, else
    (False, None, the reason histogram)."""
    reasons = {}
    for X in witnesses(R, world, st, L, P):
        good, why = certificate(R, world, st, L, P, X)
        if good:
            return True, X, ""
        reasons[why] = reasons.get(why, 0) + 1
    return False, None, reasons


# ------------------------------------------------------------------ S1
def s1_control(rings):
    section("S1  THE CONTROL -- the door identity, the ladder, the clock")
    print("  The door of a seated place is ONE p-adic valuation: the least r")
    print("  with m(e + r) > v_p(L). Read every place of both rings at every")
    print("  depth to %d, against the engine's own door_r." % DEPTH_CAP)
    print("  Then the ladder's tail gap against the ramification index, and")
    print("  the certificate on planted configurations it must ACCEPT and")
    print("  planted ones it must REFUSE.\n")
    print("  %-5s %-8s %-9s %-9s %s"
          % ("ring", "places", "readings", "tail gap", "gap = e at"))
    for R in rings:
        M = R.M
        n_read, gap_ok = 0, 0
        pls = [pl for pl in M.UNIVERSE if M.place_norm(pl) <= 200]
        for pl in pls:
            p = M.place_char(pl)
            for e in range(0, DEPTH_CAP):
                for kap in range(m_level(M, pl, e) if e else 0, LEVEL_CAP):
                    L = M.lam_P(pl, next_rung(M, pl, kap - 1) if kap else 1)
                    L *= p ** max(0, kap - m_level(M, pl,
                                                   next_rung(M, pl, kap - 1)
                                                   if kap else 1))
                    if v_p(L, p) != kap or L % M.lam_P(pl, e) != 0:
                        continue
                    want = next_rung(M, pl, kap) - e
                    ok(M.door_r(pl, e, L) == want,
                       "%s: door at %s depth %d kappa %d reads %d, ladder "
                       "says %d" % (R.name, show(pl), e, kap,
                                    M.door_r(pl, e, L), want))
                    n_read += 1
            tail = set(ladder_gap(M, pl, k) for k in range(5, 24))
            ok(len(tail) == 1, "%s: %s has no constant tail gap, %s"
               % (R.name, show(pl), sorted(tail)))
            gap_ok += (tail.pop() == place_e(M, pl))
        print("  %-5s %-8d %-9d %-9s %d of %d"
              % (R.name, len(pls), n_read, "constant", gap_ok, len(pls)))
        ok(gap_ok == len(pls),
           "%s: %d places whose tail gap is not the ramification index"
           % (R.name, len(pls) - gap_ok))
    print("\n  THE CERTIFICATE'S OWN CONTROLS. A planted conjugate split pair")
    print("  at two depths must be ACCEPTED -- without one acceptance a")
    print("  refusal below says nothing about the ring -- and three planted")
    print("  violations must be REFUSED.\n")
    print("  %-5s %-34s %-9s %s" % ("ring", "planted", "verdict", "reason"))
    for R in rings:
        M = R.M
        pair = None
        for pl in M.UNIVERSE:
            if pl[0] == 'split' and M.place_char(pl) > 2:
                conj = M.conj_place(pl)
                if conj in M.UNIVERSE and conj != pl:
                    pair = (pl, conj)
                    break
        ok(pair is not None, "%s: no split pair in the universe" % R.name)
        P, Q = pair
        st = {P: 1, Q: 3}
        L = M.lam_state(st)
        good, why = certificate(R, "ideal", st, L, P, Q)
        print("  %-5s %-34s %-9s %s"
              % (R.name, "conjugates at depths 1 and 3",
                 "ACCEPT" if good else "REFUSE", why))
        ok(good, "%s: the certificate refuses a planted conjugate pair at %s"
                 " -- %s" % (R.name, show_st(st), why))
        good, why = certificate(R, "ideal", st, L, Q, P)
        print("  %-5s %-34s %-9s %s"
              % (R.name, "the same pair, dearer as witness",
                 "ACCEPT" if good else "REFUSE", why))
        ok(not good, "%s: the certificate accepts the dear member as witness"
           % R.name)
        other = [X for X in M.UNIVERSE
                 if M.place_char(X) != M.place_char(P)
                 and M.place_norm(X) < M.place_norm(P)]
        if other:
            st2 = dict(st)
            st2[other[0]] = 4
            L2 = M.lam_state(st2)
            good, why = certificate(R, "ideal", st2, L2, P, other[0])
            print("  %-5s %-34s %-9s %s"
                  % (R.name, "a witness of another characteristic",
                     "ACCEPT" if good else "REFUSE", why))
            ok(not good and why.startswith("H0"),
               "%s: a cross-characteristic witness was not refused at H0"
               % R.name)
        good, why = certificate(R, "ideal", st, L, P, P)
        print("  %-5s %-34s %-9s %s"
              % (R.name, "a place against itself",
                 "ACCEPT" if good else "REFUSE", why))
        ok(not good, "%s: a place certifies against itself" % R.name)


# ------------------------------------------------------------------ S2
def s2_clock(rings, data):
    section("S2  THE CLOCK -- what a move does to the kappa VECTOR")
    print("  A clock move lands its mover on the next rung of that place's")
    print("  own ladder, so it must raise kappa at ONE rational prime by")
    print("  exactly one and leave every other component alone. A FRESH")
    print("  seating is under no such law: it multiplies L by N(R) - 1,")
    print("  whose p-part is arbitrary. Both are read at every move of every")
    print("  walked state.\n")
    print("  PR2's kill is an OBSERVABLE and it FIRED, in the element world")
    print("  only: a vehicle there is a core times a minimal representative,")
    print("  and when the rider lands on a second place of the core's own")
    print("  characteristic the two raise that component TOGETHER. The")
    print("  prediction was written unscoped over a world whose move is not")
    print("  a bare place power. What survives unscoped is the weaker law")
    print("  the induction actually uses -- every component that moves is")
    print("  the characteristic of a place the VEHICLE carries -- and that")
    print("  is what is asserted in the element world.\n")
    print("  %-5s %-8s %-7s %-24s %-20s %s"
          % ("ring", "world", "moves", "clock: components moved",
             "widest clock jump", "fresh: moved / widest jump"))
    for R in rings:
        M = R.M
        for world in ("ideal", "element"):
            n_clock, n_fresh, clock_comp, fresh_comp, widest = 0, 0, 0, 0, 0
            wclock = 0
            for rec in data[R.name][1][world]:
                st, L = dict(rec["seed"]), M.lam_state(rec["seed"])
                for _ in range(NF.T_CAP):
                    if NF.lock_probe(M, world, st, L, NF.T_CAP) is not None:
                        break
                    cost, vehs = NF.MENUS[world](M, st, L)
                    nxt = NF.apply_vehicle(st, vehs[0])
                    L2 = M.lam_state(nxt)
                    before, after = kappa_vec(L), kappa_vec(L2)
                    moved = [p for p in set(before) | set(after)
                             if before.get(p, 0) != after.get(p, 0)]
                    core = [pl for pl in vehs[0] if L % M.lam_P(
                        pl, st.get(pl, 0) + vehs[0][pl])]
                    is_fresh = any(st.get(pl, 0) == 0 for pl in core)
                    if is_fresh:
                        n_fresh += 1
                        fresh_comp += len(moved)
                        for p in moved:
                            widest = max(widest,
                                         after.get(p, 0) - before.get(p, 0))
                    else:
                        n_clock += 1
                        clock_comp += len(moved)
                        vchars = [M.place_char(pl) for pl in vehs[0]]
                        for p in moved:
                            wclock = max(wclock,
                                         after.get(p, 0) - before.get(p, 0))
                            ok(p in vchars,
                               "%s/%s: a clock move at %s moved kappa at %d,"
                               " which no place of the vehicle lies above"
                               % (R.name, world, show_st(st), p))
                        if world == "ideal":
                            ok(len(moved) == 1,
                               "%s/%s: a clock move at %s changed %d kappa "
                               "components" % (R.name, world, show_st(st),
                                               len(moved)))
                            p = moved[0]
                            ok(after[p] - before.get(p, 0) == 1,
                               "%s/%s: a clock move raised kappa_%d by %d"
                               % (R.name, world, p,
                                  after[p] - before.get(p, 0)))
                    st, L = nxt, L2
            print("  %-5s %-8s %-7d %-24s %-20d %s"
                  % (R.name, world, n_clock + n_fresh,
                     "%d moves, %d total" % (n_clock, clock_comp), wclock,
                     "%d moves, %d total / %d" % (n_fresh, fresh_comp,
                                                  widest)))


# ------------------------------------------------------------------ S3
def s3_same_char(rings, data):
    section("S3  THE SAME-CHARACTERISTIC CENSUS -- can (H0) be met at all?")
    print("  (H0) needs two places above ONE rational prime, one of them")
    print("  strictly cheaper. Over a quadratic ring that means a split pair,")
    print("  which is Galois-conjugate: equal norm, equal ladder. Count the")
    print("  walked states that carry such a pair -- seated/seated, and")
    print("  seated against an unseated but ineligible witness.\n")
    print("  And where a pair with a gap IS found, run the certificate on it")
    print("  -- the ported lemma's live cases, which S5 then follows.\n")
    print("  %-5s %-8s %-7s %-8s %-8s %-8s %-8s %s"
          % ("ring", "world", "states", "st/pair", "gap prs", "certified",
             "unseated", "refusals"))
    out, certified = {}, []
    for R in rings:
        M = R.M
        for world in ("ideal", "element"):
            n_st, seated, gapped, unseat = 0, 0, 0, 0
            ncert, why_all = 0, {}
            for rec in data[R.name][1][world]:
                st, L = dict(rec["seed"]), M.lam_state(rec["seed"])
                for _ in range(NF.T_CAP):
                    if NF.lock_probe(M, world, st, L, NF.T_CAP) is not None:
                        break
                    n_st += 1
                    live = [pl for pl, e in st.items() if e]
                    bychar = {}
                    for pl in live:
                        bychar.setdefault(M.place_char(pl), []).append(pl)
                    pairs = [v for v in bychar.values() if len(v) > 1]
                    seated += bool(pairs)
                    for v in pairs:
                        cs = [(cost_of(M, pl, st[pl], L), pl) for pl in v]
                        cs.sort()
                        if cs[0][0] >= cs[-1][0]:
                            continue
                        gapped += 1
                        P, X = cs[-1][1], cs[0][1]
                        good, why = certificate(R, world, st, L, P, X)
                        if good:
                            ncert += 1
                            certified.append((R, world, dict(st), L, P, X))
                        else:
                            why_all[why] = why_all.get(why, 0) + 1
                    for pl in live:
                        for X in witnesses(R, world, st, L, pl):
                            if st.get(X, 0):
                                continue
                            if eligible_fresh(M, X, L):
                                continue
                            if cost_of(M, X, 0, L) < cost_of(M, pl,
                                                             st[pl], L):
                                unseat += 1
                                break
                    cost, vehs = NF.MENUS[world](M, st, L)
                    st = NF.apply_vehicle(st, vehs[0])
                    L = M.lam_state(st)
            out[(R.name, world)] = (n_st, seated, gapped, unseat, ncert)
            print("  %-5s %-8s %-7d %-8d %-8d %-8d %-8d %s"
                  % (R.name, world, n_st, seated, gapped, ncert, unseat,
                     "; ".join("%s x%d" % (k, v)
                               for k, v in sorted(why_all.items(),
                                                  key=lambda t: -t[1])[:2])))
    return out, certified


# ------------------------------------------------------------------ S4
def s4_freeze_cases(rings, data):
    section("S4  THE FREEZE'S OWN CASES -- run the ported certificate on them")
    print("  Every seed whose limits separate at a FROZEN finite place: the")
    print("  place the lock froze, and the ported certificate run over every")
    print("  candidate witness above that place's own rational prime, at the")
    print("  state where the walk locks -- and, separately, at the EARLIEST")
    print("  state along the walk where it fires at all. That lead is the")
    print("  column that matters: at the lock the walk is already recurrent,")
    print("  so certifying there asks the weakest question available.\n")
    print("  %-5s %-8s %-6s %-6s %-6s %-16s %-16s %-10s %s"
          % ("ring", "world", "frozen", "certif", "refuse", "kind",
             "fires BEFORE lock", "branch 0/1", "why fails"))
    rows = []
    for R in rings:
        M = R.M
        for world in ("ideal", "element"):
            frozen, cert, refused, allwhy, kinds = [], 0, 0, {}, {}
            seenc, refs, early, leads = set(), [], 0, []
            branches = {}
            # A limit is keyed by repr(place); map back to the place itself.
            bykey = dict((repr(pl), pl) for pl in M.UNIVERSE)
            for rec in data[R.name][1][world]:
                lims = sorted(rec["bfs_limits"])
                if len(lims) < 2:
                    continue
                for i in range(len(lims)):
                    for j in range(i + 1, len(lims)):
                        a, b = dict(lims[i]), dict(lims[j])
                        ooa = set(pl for pl, e in a.items() if e == 'oo')
                        oob = set(pl for pl, e in b.items() if e == 'oo')
                        if ooa != oob:
                            continue
                        diff = [pl for pl in set(a) | set(b)
                                if a.get(pl, '0') != b.get(pl, '0')]
                        for key in diff:
                            if key in ooa:
                                continue
                            ok(key in bykey,
                               "%s/%s: a limit names %s, which is no place "
                               "of the universe" % (R.name, world, key))
                            frozen.append((rec["seed"], bykey[key]))
            for seed, P in frozen:
                # Walk to the lock recording the EARLIEST state at which the
                # certificate fires. Reading it only AT the lock asks the
                # weakest question there is -- the walk is recurrent there,
                # so a frozen coordinate is most of what the lock itself
                # asserts. What makes the undercut a separate argument is
                # firing BEFORE the lock, so that lead is the observable.
                # BOTH BRANCHES, not just the canonical one. A place frozen
                # in one branch is the MOVER in the other, so reading only
                # the canonical walk certifies half the records by
                # construction and leaves the other half to a symmetry
                # argument. `pick` chooses the tie member at the FIRST
                # opening; the record is certified if ANY branch certifies
                # it, and the branch that does is the one that froze it.
                first, lockat, st, L, br = None, None, None, None, 0
                for pick in range(2):
                    s, l, k, f, la, used = (dict(seed), M.lam_state(seed),
                                            0, None, None, False)
                    while k < NF.T_CAP:
                        if f is None and best_certificate(
                                R, world, s, l, P)[0]:
                            f = k
                        if NF.lock_probe(M, world, s, l, NF.T_CAP) is not None:
                            la = k
                            break
                        _, vehs = NF.MENUS[world](M, s, l)
                        j = pick if (not used and pick < len(vehs)) else 0
                        used = used or len(vehs) > 1
                        s = NF.apply_vehicle(s, vehs[j])
                        l = M.lam_state(s)
                        k += 1
                    if st is None or (first is None and f is not None):
                        first, lockat, st, L, br = f, la, s, l, pick
                    if first is not None:
                        break
                if first is not None:
                    # Count the branch only where one CERTIFIED. Counting a
                    # record no branch covers would land it in branch 0 and
                    # tilt the split the assertion below reads.
                    branches[br] = branches.get(br, 0) + 1
                if first is not None and lockat is not None and first < lockat:
                    early += 1
                    leads.append(lockat - first)
                kinds[P[0]] = kinds.get(P[0], 0) + 1
                good, X, why = best_certificate(R, world, st, L, P)
                if good:
                    cert += 1
                    seenc.add((NF.frz(seed), repr(P)))
                    rows.append((R, world, dict(st), L, P, X))
                else:
                    refused += 1
                    refs.append((NF.frz(seed), P))
                    if not why:
                        why = {"H0 no other place above that prime": 1}
                    for k, v in why.items():
                        allwhy[k] = allwhy.get(k, 0) + v
            conj = sum(1 for (sk, P) in refs
                       if (sk, repr(M.conj_place(P))) in seenc)
            top = sorted(allwhy.items(), key=lambda t: -t[1])[:2]
            print("  %-5s %-8s %-6d %-6d %-6d %-16s %-16s %-10s %s"
                  % (R.name, world, len(frozen), cert, refused,
                     " ".join("%s %d" % (k, v) for k, v in sorted(
                         kinds.items())),
                     "%d, lead %s" % (early, "-" if not leads else
                                      "%d..%d" % (min(leads), max(leads))),
                     "%d/%d" % (branches.get(0, 0), branches.get(1, 0)),
                     "; ".join("%s x%d" % (k, v) for k, v in top)))
            ok(conj == refused,
               "%s/%s: %d of %d refusals are not the conjugate of a "
               "certified place" % (R.name, world, refused - conj, refused))
            # Each conjugate is frozen in exactly ONE branch, so reading
            # both must split the records evenly. An uneven split would mean
            # a place certified in both branches -- it cannot be frozen in
            # the branch that moves it -- or one certified in neither.
            ok(branches.get(0, 0) == branches.get(1, 0),
               "%s/%s: the two branches certify %d and %d records, so some "
               "place is frozen in both or in neither"
               % (R.name, world, branches.get(0, 0), branches.get(1, 0)))
    return rows


# ------------------------------------------------------------------ S5
def s5_forward(rows):
    section("S5  THE FORWARD CHECK -- does a certified place ever move?")
    if not rows:
        print("  No certified pair to follow. The certificate's ACCEPT")
        print("  control in S1 is what keeps that from being vacuous.")
        return
    print("  Every certified pair, followed. A state that is already LOCKED")
    print("  has no menu continuation: there the recurrent vehicle is the")
    print("  continuation and is applied 12 times instead -- the 'lock'")
    print("  column -- so no certified place goes unfollowed.\n")
    print("  %-5s %-8s %-12s %-12s %-5s %-3s %s"
          % ("ring", "world", "place", "witness", "e", "lock",
             "exponent along the menu"))
    seen = set()
    for R, world, st, L, P, X in rows:
        M = R.M
        key = (R.name, world, NF.frz(st), repr(P))
        if key in seen:
            continue
        seen.add(key)
        e0, trace, tail = st.get(P, 0), [], 0
        s, l = dict(st), L
        for _ in range(12):
            veh = NF.lock_probe(M, world, s, l, NF.T_CAP)
            if veh is not None:
                # At the lock the continuation IS the recurrent vehicle;
                # applying it is the only forward step there is.
                for _ in range(12):
                    s = NF.apply_vehicle(s, veh)
                    l = M.lam_state(s)
                    tail += 1
                    ok(s.get(P, 0) == e0,
                       "%s/%s: a certified place %s moved under the lock's "
                       "own vehicle" % (R.name, world, show(P)))
                break
            _, vehs = NF.MENUS[world](M, s, l)
            s = NF.apply_vehicle(s, vehs[0])
            l = M.lam_state(s)
            trace.append(s.get(P, 0))
            ok(s.get(P, 0) == e0,
               "%s/%s: a certified place %s moved from %d to %d"
               % (R.name, world, show(P), e0, s.get(P, 0)))
        print("  %-5s %-8s %-12s %-12s %-5d %-3d %s"
              % (R.name, world, show(P), show(X), e0, tail, trace))


# ------------------------------------------------------------------ S6
def s6_lock_mechanism(rings, data):
    section("S6  WHAT THE LOCK USES INSTEAD -- printed, not predicted")
    print("  If the undercut cannot speak, what does? Read the lock's own")
    print("  invariant at each frozen place: does kappa at the place's own")
    print("  residue characteristic STOP rising once the walk locks, and is")
    print("  the recurrent vehicle's cost flat and strictly below the frozen")
    print("  place's door cost? That is stasis rather than a monotone gap --")
    print("  a different argument for the same conclusion.\n")
    print("  %-5s %-8s %-8s %-14s %-14s %s"
          % ("ring", "world", "frozen", "kappa frozen", "recurrent cheaper",
             "example"))
    for R in rings:
        M = R.M
        for world in ("ideal", "element"):
            n, kfroze, cheaper, ex = 0, 0, 0, ""
            for rec in data[R.name][1][world]:
                lims = sorted(rec["bfs_limits"])
                if len(lims) < 2:
                    continue
                st, L = dict(rec["seed"]), M.lam_state(rec["seed"])
                veh = None
                for _ in range(NF.T_CAP):
                    veh = NF.lock_probe(M, world, st, L, NF.T_CAP)
                    if veh is not None:
                        break
                    _, vehs = NF.MENUS[world](M, st, L)
                    st = NF.apply_vehicle(st, vehs[0])
                    L = M.lam_state(st)
                if veh is None:
                    continue
                rec_chars = set(M.place_char(pl) for pl in veh)
                rec_cost = 1
                for pl, e in veh.items():
                    rec_cost *= M.place_norm(pl) ** e
                # Apply the recurrent vehicle and read what MOVES. kappa
                # stasis is a measurement, not a restatement of the loop
                # bound: run the lock forward and compare v_p(L) before
                # against after, at the frozen place's own characteristic.
                s2, l2, flat = dict(st), L, True
                for _ in range(12):
                    s2 = NF.apply_vehicle(s2, veh)
                    l2 = M.lam_state(s2)
                    cc = 1
                    for pl2, e2 in veh.items():
                        cc *= M.place_norm(pl2) ** e2
                    flat = flat and (cc == rec_cost)
                for pl, e in st.items():
                    if not e or M.place_char(pl) in rec_chars:
                        continue
                    n += 1
                    p = M.place_char(pl)
                    kfroze += (kappa_at(l2, p) == kappa_at(L, p))
                    # The frozen place's own price at this state, as the
                    # WORLD prices it: a bare door in the ideal world, and
                    # the door times its class representative in the
                    # element world -- comparing a bare door against a full
                    # vehicle would compare two different currencies.
                    c = CS.bare_door(R, world, st, L, pl)[2]
                    cheaper += (rec_cost < c and flat)
                    if not ex:
                        ex = "%s at %s: recurrent %d against %d" % (
                            show(pl), show_st(rec["seed"]), rec_cost, c)
            print("  %-5s %-8s %-8d %-14d %-14d %s"
                  % (R.name, world, n, kfroze, cheaper, ex))


def main():
    print("=" * 70)
    print("THE UNDERCUT LEMMA OVER A NUMBER RING")
    print("=" * 70)
    print("Does the certificate that freezes a coordinate over the function")
    print("fields run over a number ring -- and are the LOCK's own freeze")
    print("cases instances of it?")
    rings = [CS.Ring(*r) for r in CS.RINGS]
    data = CS.census(rings)
    s1_control(rings)
    s2_clock(rings, data)
    _, live = s3_same_char(rings, data)
    rows = s4_freeze_cases(rings, data)
    s5_forward(live + rows)
    s6_lock_mechanism(rings, data)
    print("\n" + "=" * 70)
    print("ALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
