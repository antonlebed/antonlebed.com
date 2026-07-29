r"""explore_cubic_undercut.py -- is the separation lemma's local-degree
hypothesis load-bearing, and what does a residue degree above 2 buy?

THE QUESTION. The undercut lemma ported to a number ring
(explore_undercut_nf.py F1) carries two hypotheses the function-field
statement does not: (H0) the frozen place and its witness share a residue
characteristic, and (H1) the comparison is by degree times LADDER GAP --
in the tail e*f, the LOCAL DEGREE -- rather than by the residue degree
alone. (H0) was exercised. (H1) was DERIVED AND NEVER EXERCISED, and that
file says why in its own words: both its rings are QUADRATIC, where two
places over one rational prime can only be a conjugate SPLIT pair with
equal norm, equal ramification and equal ladder, so (H1) holds with
EQUALITY at every pair either ring can present and nothing measured tells
e*f from f. Separating them needs a rational prime under two places of
different ramification, which is degree three at the least.

explore_cubic_ring.py supplies one. In K = Q[x]/(x^3 - x - 1) the prime 23
factors as P*Q^2 with e_P = f_P = f_Q = 1 and e_Q = 2, so the two places
share the norm 23 and carry local degrees 1 and 2. At a pair like that the
two readings of (H1) DISAGREE: read by f the hypothesis holds with equality
and the certificate would freeze P; read by e*f it fails and the
certificate refuses. So the ring decides which reading is right, which is
the whole of question 1.

Question 2 is the same ring at a different prime. A seated place's door is
set by one p-adic valuation of the state invariant, and a place R over
another rational prime supplies v_p(N(R) - 1) -- its residue CARDINALITY
alone (explore_populated_door.py F3). Residue cardinality is NOT what a
quadratic ring cannot reach: planting a split place of norm 257 in Z[i]
drives a door from 5 to 17 there. What a quadratic ring cannot have is
residue DEGREE above 2, and explore_undercut_nf.py F8 (iii) names the
consequence exactly -- at f = 3, q - 1 can carry a large p-part at a SMALL
rational prime, "exactly where the residue route should bite hardest". This
file measures that as a CARRIER COST rather than as a reachable valuation,
because the valuation is reachable either way and only the price differs.

Question 3, whether the menu's (matrix, ladder) reproduces this ring, is
answered in explore_cubic_ring.py F4 and is not repeated here.

THE WORLD IS THE IDEAL ONE THROUGHOUT. K has class number 1 (Minkowski's
bound is 1.36), so there is no class layer, no rider and no covering norm;
the element world's slack has nothing to be measured against and is not
entered. Every certificate below is run with world = "ideal".

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The suspicion is
written in the CERTIFICATE's terms -- (H0)..(H3), the cost gap, the ladder
gap, the local degree -- and not in the walker's. That is deliberate and it
is what keeps the rig from asking the wrong question: the lemma's claim is
about an INVARIANT preserved under a move model, and a rig written in the
walker's words would ask instead what one greedy trajectory happens to do.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From the quadratic rings to this one: the CERTIFICATE and nothing else.
    certificate(), next_rung(), ladder_gap() and m_level() are imported from
    explore_undercut_nf.py rather than restated, so the object under test is
    the filed one. Its place_f had to be repaired to reach here at all -- it
    read residue degree off the tag alphabet ('inert' meaning f = 2), which
    is the quadratic case and not a definition; it now reads N(X) = p^f as
    one valuation, which is ring-independent and agrees with the old reading
    at every quadratic place.
 T2 From explore_populated_door.py's excess census to this ring: NOTHING.
    Its 717 readings are over three quadratic rings and its walked maximum
    of 2 is a fact about those walks. This ring's own walk is DEGENERATE
    (explore_cubic_ring.py F5), so no excess census here is comparable to
    one there and none is attempted.
 T3 From "the certificate refuses" to "the walk unfreezes P": NOT MADE, and
    this is the flag that changed the rig. See the hand-attack.

THE HAND-ATTACK, on paper before any engine code, and it killed the
observable this file was going to be built on.

  A. THE DOOR ARITHMETIC AT 23. Write kappa = v_23(L) and s_X for X's
     exponent in the state. With m_X(a) = v_23(lam(X^a)):
         m_P(a) = a - 1                  m_Q(a) = ceil((a-1)/2)
         next_P(kappa) = kappa + 2       next_Q(kappa) = 2*kappa + 2
         sigma_P = kappa + 2 - s_P       sigma_Q = 2*kappa + 2 - s_Q
     and the ladder gaps are g_P = 1, g_Q = 2. Costs are 23^sigma at both,
     the norms being equal, so the whole comparison is between the two
     sigmas and the log-gap is sigma_P - sigma_Q = s_Q - s_P - kappa.

  B. THE CONFIGURATION. (H2) needs cost(Q) < cost(P), i.e. kappa <
     s_Q - s_P. Take s_P = 1 and s_Q = 3: then m_P(1) = 0 and m_Q(3) = 1
     force kappa >= 1, and (H2) forces kappa < 2, so kappa = 1 exactly and
     the state {P:1, Q:3} realises it with nothing else seated. There
     L = lcm(22, 22*23) = 506, sigma_P = 2 and sigma_Q = 1, so cost(P) = 529
     against cost(Q) = 23 -- a strict gap, and 22 | L makes both members
     fresh-INELIGIBLE, which (H2)'s other half demands. Every hypothesis
     but (H1) holds by construction; (H1) fails because f_P*g_P = 1 <
     f_Q*g_Q = 2 at every level, and in the tail because e_P*f_P = 1 <
     e_Q*f_Q = 2. Read by f alone both sides are 1 and (H1) HOLDS.

  C. WHAT BREAKS THE INVARIANT, case by case against the lemma's own list.
     - a clock move above a rational prime other than 23: kappa untouched,
       both sigmas stand, I preserved. Harmless, as the lemma says.
     - a clock move at a THIRD place above 23: THERE IS NO THIRD PLACE.
       1*f_P + 2*f_Q = 3 exhausts the degree, so this ring cannot present
       the case at 23 at all -- worth saying plainly, since
       explore_undercut_nf.py's own hand-attack names this case as where
       (H1) enters, so the ring that DECIDES the hypothesis is one that
       cannot present the case introducing it.
     - a clock move at Q: Q lands on next_Q(kappa) and kappa rises by one,
       so sigma_Q resets to g_Q = 2 while sigma_P rises by g_P = 1. The gap
       is preserved and then WIDENS. Clocking Q never helps.
     - a clock move at P: not available while I holds, Q's door being
       strictly cheaper.
     - A FRESH MOVE ANYWHERE, which is the case (H1) exists to carry. A
       fresh R over l != 23 multiplies L by N(R) - 1 and lifts kappa to
       v_23(N(R) - 1) when that is larger. A jump of j levels raises
       sigma_P by j*g_P = j and sigma_Q by j*g_Q = 2j, so the log-gap FALLS
       BY j. From a gap of 1: j = 1 ties the two costs, and a tie already
       makes P a minimal move again, the menu returning every tie member;
       j = 2 reverses them outright and P becomes strictly the cheaper.
     So the supplier wanted is a place with 23^2 | N(R) - 1 for the tie and
     23^3 | N(R) - 1 for the reversal. Since 23 never divides l^2 + l + 1
     (its discriminant -3 is a non-residue mod 23), an f = 3 place needs
     23^k | l - 1; an f = 2 place needs l = +-1 mod 23^k. Let the engine
     SEARCH for both rather than hardcoding either.

  D. AND THE OBSERVABLE THE HANDOVER NAMED CANNOT FIRE HERE, which is the
     hand-attack's real catch. "P never moves again along the walk" reads a
     GREEDY TRAJECTORY. This ring's greedy walk is degenerate: it has no
     head at any place (explore_cubic_ring.py F3), so its least-norm place
     -- the rational place over 5 -- has door 1 at every depth and is priced
     at 5 forever, and nothing in the universe can undercut it. The walk
     clocks that one place and touches 23 never. So P would fail to move for
     a reason with nothing to do with e*f, and the walk-level reading would
     be VACUOUS in exactly the way (H2) would have been vacuous had the
     configuration been chosen by norm.
     THE OBSERVABLE IS THEREFORE THE LEMMA'S OWN INVARIANT I: cost(Q) <
     cost(P), which the induction claims every move case preserves. That is
     what the lemma proves and what (H1) is used to prove; running the cases
     and reading I tests the LEMMA rather than the walker. What it can
     establish is that (H1) is load-bearing IN THE INDUCTION at a real
     Dedekind domain; what it cannot establish is what a walk does, and this
     ring is the wrong instrument for that question.

  E. QUESTION 2's OBSERVABLE, chosen for the same reason. A quadratic ring
     reaches any VALUATION by planting a large enough place, so the reach is
     not the difference -- explore_populated_door.py's own planted drive
     shows it. What residue degree 3 changes is the CARRIER: N = p^3 puts
     the factor l^k into the
     invariant from a place of norm p^3 where degree <= 2 needs the least
     p^d with l | p^d - 1, and p^3 - 1 = (p-1)(p^2+p+1) supplies primes
     l = 1 mod 3 dividing p^2 + p + 1 at a p far below anything p - 1 or
     p^2 - 1 reaches. Carrier cost is what a MENU prices, so this is the
     half of the residue route that a price can see.

PREDICTIONS, fixed before any engine code, each naming what the rig PRINTS.
  PR1 The door identity ports. Over every place of this ring at depths 0..8
      and every kappa the depth admits, the engine's door_r equals
      next_rung(kappa) - e computed through explore_undercut_nf.py's own
      ladder reading, and the tail gap is the ramification index.
      KILL: one mismatch; the certificate would then be running on a ladder
      the engine does not have.
  PR2 The certificate's controls fire at this ring: an ACCEPT at a planted
      pair over 5 (the f = 2 place as P, the f = 1 place as Q), and REFUSALS
      with the dearer member as witness, with a cross-characteristic
      witness, and with a place against itself.
      KILL: no ACCEPT. Without one, every refusal below says nothing.
  PR3 At {P:1, Q:3} over 23 the certificate REFUSES, and the first failing
      hypothesis it names is an (H1) clause -- not (H0), not (H2).
  PR4 The same certificate with (H1) read by residue degree ALONE ACCEPTS
      the same configuration. This is the separation and it is the point:
      the two readings disagree at a pair a quadratic ring cannot build.
  PR5 The invariant I survives every clock case and BREAKS at a fresh
      seating: a tie at a supplier with 23^2 | N(R) - 1, and a strict
      reversal at one with 23^3 | N(R) - 1. Both suppliers are found by
      search and each is verified to be a genuine place of the ring through
      the engine's own factor_shape.
  PR6 Residue degree 3 lowers the least CARRIER NORM of a supply. Printed:
      for each small prime l, the least norm p^d with d <= 2 and l | p^d - 1
      against the least p^3, with the ring's own realization of each.
  PR7 The two places over 23 share a norm and their prices PART with depth
      -- the lone-place cost of P is flat while Q's alternates -- which a
      conjugate pair in a quadratic ring never does.

KILL-SHAPES, as observables.
  K1 the certificate refuses the planted ACCEPT control (PR2), or the door
     identity misses (PR1): the instrument is wrong.
  K2 the certificate refuses at {P:1, Q:3} for a reason other than (H1):
     the configuration does not isolate the hypothesis and has to be rebuilt.
  K3 no move case breaks I: e*f is SUFFICIENT but not NECESSARY, the true
     hypothesis is weaker than the derivation found, and the reading by f
     survives. Worth as much as the other outcome.

DISTRUST THE MARGIN. The DERIVED half is the sigma arithmetic in A, and the
falling log-gap in C, both of which follow from the closed form. The VIBES
half is "both suppliers exist": neither is asserted, both are searched for,
and the reversal's supplier lies beyond the engine's enumerated universe and
so is checked to be a real place through factor_shape before it is planted.

POSITIVE CONTROL, run before any verdict is read (S1). The door identity at
this ring through the certificate's own ladder functions, and the
certificate's ACCEPT and three REFUSALS on planted configurations. The
ACCEPT is over 5, where the f = 2 and f = 1 places give (H1) a STRICT
inequality -- itself something no quadratic ring presents, since there (H1)
is an equality at every pair.

THE SECTIONS.
  S1  the control: the door identity, and the certificate's ACCEPT/REFUSALS.
  S2  question 1: the two readings of (H1), and the invariant under every
      move case.
  S3  question 2: what residue degree 3 buys, priced as a carrier.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE LOCAL-DEGREE HYPOTHESIS IS LOAD-BEARING, AND THE READING BY RESIDUE
   DEGREE IS REFUTED (observation -- one ring, one prime, one configuration;
   the arithmetic behind it is a derivation but the witness is a single
   pair). At P*Q^2 over 23 the two readings of (H1) DISAGREE: read by f the
   certificate ACCEPTS and freezes P; read by e*f it REFUSES, naming an H1
   clause and no other, with (H0) and both halves of (H2) holding by
   construction. The engine then decides between them. Seating one fresh
   place whose N(R) - 1 carries 23^3 lifts kappa_23 from 1 to 3, and the
   invariant the induction claims to preserve does not merely fail -- it
   REVERSES: cost(P) falls to 23^4 = 279841 against cost(Q) at
   23^5 = 6436343, so the place the f-reading had frozen is strictly the
   cheaper of the two. A supplier carrying only 23^2 gives the weaker
   version, a TIE at 12167 apiece, which already ends the freeze since the
   menu returns every tie member. THE MECHANISM IS ONE LINE OF ARITHMETIC
   AND IT IS THE HYPOTHESIS ITSELF: a jump of j levels raises sigma_P by
   j*g_P and sigma_Q by j*g_Q, so the LOG-COST gap -- f_X*sigma_X in units
   of log p -- moves by j*(f_P*g_P - f_Q*g_Q), which is nonnegative exactly
   when (H1) holds and IS (H1). At 23 both residue degrees are 1 and the f's
   drop out, which is why this pair reads as a bare gap comparison and is
   not one. Read by f that
   comparison is 1 against 1 and predicts a gap that stands; read by e*f it
   is 1 against 2 and predicts the fall that happens. So explore_undercut_nf
   F1's derived clause was not decoration, and the source lemma's degree
   reading was the equal-characteristic coincidence that file called it.

F2 WHAT THE RING DECIDES IS THE LEMMA, NOT THE WALK, AND THE TWO ARE NOT
   INTERCHANGEABLE HERE (rule in range; six moves applied at one state and
   two further cases named unavailable, two of the six breaking the
   invariant, both fresh seatings). The handover's own
   observable was "P never moves again along the WALK", and it cannot fire
   in this ring for a reason that has nothing to do with e*f: the ring has
   no head at any place, so its least-norm place is priced at its norm
   forever and the greedy walk clocks that one place and touches 23 never
   (explore_cubic_ring.py F5). A walk-level reading here would have been
   VACUOUS. What IS testable is the induction's own invariant I, cost(Q) <
   cost(P), and the case sweep is the test: a fresh seating with no 23-part
   preserves it, clocking it preserves it, clocking Q preserves and then
   WIDENS it, clocking P is excluded while it holds -- and the case where
   (H1) ENTERS, a clock move at a THIRD place above the shared prime, is
   UNAVAILABLE at 23, since 1*f_P + 2*f_Q = 3 exhausts the degree. So the
   configuration that first DECIDES the hypothesis is one that cannot
   present the case explore_undercut_nf.py's hand-attack introduces it at --
   worth recording as a property of partial ramification in a cubic field
   rather than as a limitation of this rig, and it is why the fresh-seating
   case had to carry the whole test.

F3 (H1) HOLDS STRICTLY SOMEWHERE IN THIS RING, WHICH IS WHAT MAKES THE
   REFUSAL READABLE (rule in range; the planted pair over 5 accepted, three
   planted violations refused, 1858 door readings over 43 places with 0
   off). At 5 the ring carries an f = 2 place and an f = 1 place, and the
   certificate ACCEPTS the pair with (H1) a strict inequality, 2 against 1.
   No quadratic ring can present that either: there two places over one
   rational prime are conjugate, so (H1) is an EQUALITY at every pair
   available and the hypothesis is never seen doing anything. So this ring
   exercises the clause in both directions -- strictly satisfied at 5,
   strictly violated at 23 -- and the second reading means something only
   because the first one fired.
   WHAT THE ACCEPT IS NOT, said so it is not over-read: an instrument
   control, never a verified freeze. explore_undercut_nf.py's S5 follows
   each certified place forward to see whether it ever moves, and that
   check cannot be run here for the same reason the walk-level kill-shape
   cannot -- a degenerate walk moves nothing, so it would pass vacuously.
   This ring can decide the HYPOTHESIS and cannot witness the CONCLUSION,
   and those are two different jobs.

F4 WHAT RESIDUE DEGREE 3 BUYS IS A CHEAPER CARRIER, NOT A LONGER REACH
   (rule in range; the least residue cardinality carrying each of the nine
   primes below 24, at degree <= 2 against degree 3). The reach is not the
   difference -- planting a norm-257 place in Z[i] drives a door from 5 to
   17, so any valuation is reachable at degree 1. What changes is the PRICE
   OF THE CARRIER, which is the half a
   menu can see: N - 1 = p^3 - 1 factors as (p-1)(p^2+p+1), and the second
   factor supplies primes l = 1 mod 3 from a rational prime far below
   anything p - 1 or p^2 - 1 reaches. Two of the nine are carried more
   cheaply at degree 3 and this ring realizes both -- a supply of 7 from
   norm 8 against 29 at degree <= 2, and of 13 from norm 27 against 53 --
   and the first is the INERT place over 2, whose residue field F_8 puts the
   whole of 7 into the invariant where the only cardinalities over 2 at
   degree <= 2 are 2 and 4, carrying 1 and 3. Seated beside a rational place
   over 7 it widens that place's door from 1 to 2, price 49 against 7. THE
   CONSEQUENCE IS NOT MEASURED HERE and is named rather than claimed: a
   carrier's norm is what decides whether a walk can SEAT it rather than
   only have it planted, so a cheaper carrier is what would let the residue
   route fire in a walk -- but this ring's walk is degenerate, so the
   implication is untested and belongs to a ring with heads.

F5 A SHARED NORM DOES NOT TIE TWO PLACES, WHICH IS ONLY VISIBLE ABOVE
   DEGREE 2 (rule in range; the pair over 23 read at eight depths, differing
   at four). P and Q carry one norm and two ladders, so their lone-place
   prices part with depth: P is flat at 23 while Q alternates 23 and 529 on
   its step-2 staircase. In a quadratic ring the only two places over one
   rational prime are conjugates, which share a ladder and therefore stay
   priced alike at every depth forever. So "two places share a norm" is a
   tie there and a transient here, and any argument that reads a shared norm
   as a permanent tie is reading the quadratic case.

RUN RECORD. `python explore_cubic_undercut.py`. One process, CPython, no
BLAS. 1920 checks, 0.5 s wall, peak working set 20.2 MB under memwatch.py's
512 MB ceiling. The certificate, the ladder functions and every door are
explore_undercut_nf.py's and explore_cubic_ring.py's, imported rather than
restated. S1: 1858 door readings over the 43 places of norm <= 200, 0 off,
the tail gap the ramification index at 43 of 43; one ACCEPT and three
REFUSALS on planted configurations. S2: six moves applied at one state, I
holding at four and broken at two, with two further cases of the lemma's
list named unavailable rather than applied -- tied at a supplier with
23^2 | N(R)-1
(the f = 2 place over 4231) and reversed at one with 23^3 (a rational place
over 535349, found by search beyond the enumerated universe and checked to
be a real place through the engine's own factor_shape). S3: 0 off on the
depth-freeness of a foreign-prime supply over 400 places, six primes and six
depths; the carrier table over nine primes with two won at degree 3; the
planted drive at 7. Slate PR1-PR7 all hit; K3 -- no case breaking I, which
would have made e*f sufficient but not necessary -- did not fire.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_ring as CR
import explore_undercut_nf as UN

CHECKS = 0

DEPTH_CAP = 8        # depths a place is read at in the control
LEVEL_CAP = 8        # ladder levels the hypothesis is checked over
CARRIER_L = 24       # small primes the carrier table is read at
SEARCH_K = 60        # multiples of 23^3 scanned for the reversal's supplier


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def v_p(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


class Ring(object):
    """The record explore_undercut_nf.certificate reads. In the ideal world
    it touches only .M; the element world's .minnorm and .rider have no
    counterpart at h = 1 and are deliberately absent, so an accidental
    element-world call raises rather than reading a default."""

    def __init__(self, M, name):
        self.M = M
        self.name = name


R = Ring(CR, "K(-23)")
P_UNRAM = (23, 1, 1, 0)
Q_RAM = (23, 2, 1, 0)


def cert_by_f(st, L, P, Q):
    """The certificate with (H1) read by RESIDUE DEGREE alone -- the reading
    the function-field lemma's own statement licenses, and the one every
    quadratic pair is consistent with. Hypotheses in explore_undercut_nf's
    own order, so the only difference from it is the (H1) comparison."""
    M = R.M
    if M.place_char(P) != M.place_char(Q):
        return False, "H0 different characteristic"
    if P == Q:
        return False, "H0 same place"
    if UN.eligible_fresh(M, P, L) or UN.eligible_fresh(M, Q, L):
        return False, "H2 a member is still fresh-eligible"
    cP = UN.cost_of(M, P, st.get(P, 0), L)
    cQ = UN.cost_of(M, Q, st.get(Q, 0), L)
    if not cQ < cP:
        return False, "H2 no cost gap"
    fP, fQ = UN.place_f(M, P), UN.place_f(M, Q)
    # No per-level loop, and its ABSENCE is the difference under test: a
    # residue degree carries no dependence on the ladder level, so this
    # reading has one comparison where the local-degree reading has one per
    # level the walk can cross. Writing the loop anyway would dress a
    # constant as a per-level check.
    if fP < fQ:
        return False, "H1 residue degree"
    return True, ""


def sigmas(st, L):
    """(kappa, sigma_P, sigma_Q, cost_P, cost_Q) at a state, all through the
    engine's own door_r rather than through the hand formula."""
    M = R.M
    kap = v_p(L, 23)
    sP = M.door_r(P_UNRAM, st.get(P_UNRAM, 0), L)
    sQ = M.door_r(Q_RAM, st.get(Q_RAM, 0), L)
    return kap, sP, sQ, 23 ** sP, 23 ** sQ


# ------------------------------------------------------------------ S1
def s1_control():
    section("S1  THE CONTROL -- the door identity at this ring, and the "
            "certificate's own ACCEPT and REFUSALS")
    M = R.M
    print("  PR1. A seated place's door is one p-adic valuation, so it must")
    print("  equal next_rung(kappa) - e read off the place's own ladder. Be")
    print("  precise about what this does and does not check: both sides")
    print("  consume the ENGINE's lam_P, so it checks that the door LOOP and")
    print("  the ladder READING agree on that table, not the table itself.")
    print("  The table is checked against brute-forced unit groups in")
    print("  explore_cubic_ring.py S1, and that is where it earns trust.")
    n_read, gap_ok, n_pl = 0, 0, 0
    for pl in M.UNIVERSE:
        if M.place_norm(pl) > 200:
            continue
        n_pl += 1
        p = M.place_char(pl)
        for e in range(0, DEPTH_CAP):
            for kap in range(UN.m_level(M, pl, e) if e else 0, LEVEL_CAP):
                # an invariant with v_p exactly kappa and lambda(X^e) | L,
                # built from the place's own residue factor rather than from
                # any state, so the reading is the ladder's and not a walk's
                L = (M.place_norm(pl) - 1) * p ** kap
                if L % M.lam_P(pl, e):
                    continue
                want = UN.next_rung(M, pl, kap) - e
                ok(M.door_r(pl, e, L) == want,
                   "door at %s depth %d kappa %d reads %d, the ladder says %d"
                   % (CR.show(pl), e, kap, M.door_r(pl, e, L), want))
                n_read += 1
        tail = set(UN.ladder_gap(M, pl, k) for k in range(5, 20))
        ok(len(tail) == 1, "%s has no constant tail gap: %s"
                           % (CR.show(pl), sorted(tail)))
        gap_ok += (tail.pop() == UN.place_e(M, pl))
    ok(gap_ok == n_pl,
       "%d places whose tail gap is not the ramification index"
       % (n_pl - gap_ok))
    print("    %d door readings over %d places of norm <= 200, 0 off; the"
          % (n_read, n_pl))
    print("    tail gap is the ramification index at %d of %d."
          % (gap_ok, n_pl))

    print()
    print("  PR2, THE CERTIFICATE'S OWN CONTROLS. The ACCEPT is planted over")
    print("  5, whose two places have residue degrees 2 and 1 -- so (H1)")
    print("  holds STRICTLY there, which no quadratic ring can present: two")
    print("  places over one rational prime are conjugate there and (H1) is")
    print("  an equality at every pair. Without an ACCEPT every refusal in")
    print("  S2 would say nothing about the ring.")
    print()
    print("  %-38s %-9s %s" % ("planted", "verdict", "reason"))
    A = next(pl for pl in M.UNIVERSE if pl[0] == 5 and pl[2] == 2)   # norm 25
    B = next(pl for pl in M.UNIVERSE if pl[0] == 5 and pl[2] == 1)   # norm 5
    st = {A: 1, B: 1}
    L = M.lam_state(st)
    good, why = UN.certificate(R, "ideal", st, L, A, B)
    print("  %-38s %-9s %s" % ("f=2 place over 5 against the f=1 one",
                               "ACCEPT" if good else "REFUSE", why))
    ok(good, "the certificate refuses the planted pair over 5 -- %s" % why)
    print("       (cost %d against %d, e*f %d against %d, kappa_5 = %d)"
          % (UN.cost_of(M, A, 1, L), UN.cost_of(M, B, 1, L),
             M.place_ef(A), M.place_ef(B), v_p(L, 5)))
    good, why = UN.certificate(R, "ideal", st, L, B, A)
    print("  %-38s %-9s %s" % ("the same pair, dearer as witness",
                               "ACCEPT" if good else "REFUSE", why))
    ok(not good, "the certificate accepts the dear member as witness")
    other = next(pl for pl in M.UNIVERSE if pl[0] == 7 and pl[2] == 1)
    st2 = dict(st)
    st2[other] = 4
    L2 = M.lam_state(st2)
    good, why = UN.certificate(R, "ideal", st2, L2, A, other)
    print("  %-38s %-9s %s" % ("a witness of another characteristic",
                               "ACCEPT" if good else "REFUSE", why))
    ok(not good and why.startswith("H0"),
       "a cross-characteristic witness was not refused at H0: %s" % why)
    good, why = UN.certificate(R, "ideal", st, L, A, A)
    print("  %-38s %-9s %s" % ("a place against itself",
                               "ACCEPT" if good else "REFUSE", why))
    ok(not good, "a place certifies against itself")
    return n_read, n_pl


# ------------------------------------------------------------------ S2
def s2_local_degree():
    section("S2  QUESTION 1 -- the two readings of (H1) at a pair no "
            "quadratic ring builds, and the invariant under every move case")
    M = R.M
    st = {P_UNRAM: 1, Q_RAM: 3}
    L = M.lam_state(st)
    kap, sP, sQ, cP, cQ = sigmas(st, L)
    print("  the configuration, read off the engine:")
    print("    state %s, invariant %d, kappa_23 = %d"
          % (CR.show_st(st), L, kap))
    print("    %-14s e*f = %d, ladder gap = %d, door %d, cost %d"
          % (CR.show(P_UNRAM), M.place_ef(P_UNRAM),
             UN.ladder_gap(M, P_UNRAM, kap + 1),
             sP, cP))
    print("    %-14s e*f = %d, ladder gap = %d, door %d, cost %d"
          % (CR.show(Q_RAM), M.place_ef(Q_RAM),
             UN.ladder_gap(M, Q_RAM, kap + 1),
             sQ, cQ))
    ok(M.place_norm(P_UNRAM) == M.place_norm(Q_RAM),
       "the two places over 23 no longer share a norm")
    ok(cQ < cP, "(H2) does not hold at the planted state: %d vs %d"
                % (cQ, cP))
    ok(not UN.eligible_fresh(M, P_UNRAM, L)
       and not UN.eligible_fresh(M, Q_RAM, L),
       "a member of the pair is still fresh-eligible, so (H2) is not met")
    print("  equal norms, so the whole comparison is between the two doors;")
    print("  (H2) holds strictly and neither member is fresh-eligible, which")
    print("  is what leaves (H1) as the only hypothesis in question.")

    print()
    print("  PR3/PR4, THE TWO READINGS:")
    good_ef, why_ef = UN.certificate(R, "ideal", st, L, P_UNRAM, Q_RAM)
    good_f, why_f = cert_by_f(st, L, P_UNRAM, Q_RAM)
    print("    (H1) by LOCAL DEGREE e*f : %-7s %s"
          % ("ACCEPT" if good_ef else "REFUSE", why_ef))
    print("    (H1) by RESIDUE DEGREE f : %-7s %s"
          % ("ACCEPT" if good_f else "REFUSE", why_f))
    ok(not good_ef and why_ef.startswith("H1"),
       "the local-degree certificate did not refuse at an H1 clause: %s"
       % why_ef)
    ok(good_f, "the residue-degree reading did not accept, so the two "
               "readings do not separate here after all: %s" % why_f)
    print("  They disagree. Read by f the certificate FREEZES P; read by e*f")
    print("  it refuses. Everything below decides which is right.")

    print()
    print("  PR5, THE MOVE CASES. The lemma's induction claims the invariant")
    print("  I -- cost(Q) < cost(P) -- survives every move. Each case is")
    print("  applied to the state above and I is read after it.")
    print()
    print("  %-42s %-6s %-8s %-10s %s"
          % ("case", "kappa", "doors", "costs", "I: cost(Q) < cost(P)"))
    rows, broke = [], []

    def report(label, st2):
        L2 = M.lam_state(st2)
        k2, a2, b2, ca, cb = sigmas(st2, L2)
        held = cb < ca
        print("  %-42s %-6d %-8s %-10s %s"
              % (label, k2, "%d/%d" % (a2, b2), "%d/%d" % (ca, cb),
                 "holds" if held else
                 ("TIED -- P is a minimal move again" if cb == ca
                  else "REVERSED -- P is strictly cheaper")))
        rows.append((label, k2, ca, cb, held))
        if not held:
            broke.append((label, k2, ca, cb))
        return L2

    report("(start) the planted state", st)

    # (a) a fresh move at a place carrying no 23-part: kappa untouched
    free = next(pl for pl in M.UNIVERSE
                if pl[0] not in (23,) and v_p(M.place_norm(pl) - 1, 23) == 0)
    st_a = dict(st)
    st_a[free] = 1
    report("(a) fresh %s, no 23-part in N-1" % CR.show(free), st_a)

    # (a') clocking that same place: still no 23-part
    st_a2 = dict(st_a)
    st_a2[free] = 1 + M.door_r(free, 1, M.lam_state(st_a))
    report("(a') clock the same place", st_a2)

    # (b) a clock move at a THIRD place above 23 -- none exists
    over23 = [pl for pl in M.UNIVERSE if pl[0] == 23]
    ok(len(over23) == 2,
       "23 lies under %d places, so the case that introduces (H1) is "
       "available "
       "after all" % len(over23))
    print("  %-42s %s"
          % ("(b) clock a third place above 23",
             "UNAVAILABLE: 1*f_P + 2*f_Q = 3 exhausts the degree"))

    # (c) a clock move at Q itself
    st_c = dict(st)
    st_c[Q_RAM] = st[Q_RAM] + sQ
    report("(c) clock Q to exponent %d" % st_c[Q_RAM], st_c)
    st_c2 = dict(st_c)
    L_c = M.lam_state(st_c)
    st_c2[Q_RAM] = st_c[Q_RAM] + M.door_r(Q_RAM, st_c[Q_RAM], L_c)
    report("(c') clock Q again, to exponent %d" % st_c2[Q_RAM], st_c2)

    # (d) a clock move at P -- not a minimal move while I holds
    print("  %-42s %s"
          % ("(d) clock P",
             "EXCLUDED while I holds: %d against Q's %d" % (cP, cQ)))

    # (e) a fresh move lifting kappa_23. The suppliers are SEARCHED.
    print()
    print("  and the case (H1) exists to carry -- a fresh seating whose")
    print("  N(R) - 1 carries a 23-part above the state's own kappa. A jump")
    print("  of j raises sigma_P by j*g_P = j and sigma_Q by j*g_Q = 2j, so")
    print("  the log-gap falls by j. The suppliers are searched for, not")
    print("  assumed:")
    tie = min((pl for pl in M.UNIVERSE
               if pl[0] != 23 and v_p(M.place_norm(pl) - 1, 23) == 2),
              key=M.place_norm, default=None)
    ok(tie is not None,
       "no place of the enumerated universe supplies v_23 = 2, so the tie "
       "case cannot be exhibited")
    print("    tie supplier      %-16s norm %d, v_23(N-1) = %d"
          % (CR.show(tie), M.place_norm(tie),
             v_p(M.place_norm(tie) - 1, 23)))
    st_e = dict(st)
    st_e[tie] = 1
    report("(e) fresh %s, v_23(N-1) = 2" % CR.show(tie), st_e)

    rev = find_reversal_supplier()
    print("    reversal supplier %-16s norm %d, v_23(N-1) = %d"
          % (CR.show(rev), M.place_norm(rev),
             v_p(M.place_norm(rev) - 1, 23)))
    print("      beyond the engine's enumerated universe, so its splitting")
    print("      type is checked through the engine's own factor_shape:")
    print("      %d factors as %s" % (rev[0], CR.factor_shape(rev[0])))
    st_f = dict(st)
    st_f[rev] = 1
    report("(e') fresh %s, v_23(N-1) = 3" % CR.show(rev), st_f)

    ok(broke, "no move case broke the invariant, so the local-degree clause "
              "is sufficient but not necessary and K3 has fired")
    ok(any(ca < cb for _, _, ca, cb in broke),
       "no case made P strictly the cheaper member -- the gap only tied")
    print()
    print("  %d of the %d MOVES applied broke I, and both are fresh"
          % (len(broke), len(rows) - 1))
    print("  seatings. The row count is one higher: the start state is read")
    print("  as a baseline and is not a move.")
    return rows, broke


def find_reversal_supplier():
    """The cheapest place whose N(R) - 1 carries 23^3, searched beyond the
    engine's enumerated universe. 23 never divides l^2 + l + 1 -- the
    discriminant -3 is a non-residue mod 23 -- so an f = 3 place needs
    23^3 | l - 1 and an f = 2 place needs l = +-1 mod 23^3; either way the
    rational prime is congruent to +-1 modulo 23^3 and the scan is over
    those alone."""
    M = R.M
    inuniv = [pl for pl in M.UNIVERSE
              if pl[0] != 23 and v_p(M.place_norm(pl) - 1, 23) >= 3]
    if inuniv:
        return min(inuniv, key=M.place_norm)
    best = None
    for k in range(1, SEARCH_K):
        for s in (1, -1):
            l = 23 ** 3 * k + s
            if not is_prime(l):
                continue
            for (e, f) in CR.factor_shape(l):
                if e != 1 or v_p(l ** f - 1, 23) < 3:
                    continue
                cand = (l, e, f, 0)
                if best is None or M.place_norm(cand) < M.place_norm(best):
                    best = cand
    ok(best is not None,
       "no supplier with 23^3 | N(R) - 1 below %d, so the reversal cannot "
       "be exhibited" % (23 ** 3 * SEARCH_K))
    return best


def is_prime(n):
    if n < 2:
        return False
    for d in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % d == 0:
            return n == d
    d = 41
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


# ------------------------------------------------------------------ S3
def s3_residue_degree():
    section("S3  QUESTION 2 -- what a residue degree above 2 buys, priced "
            "as a CARRIER rather than as a reach")
    M = R.M
    print("  A place R over a rational prime other than p supplies")
    print("  v_p(N(R) - 1) to the invariant, its residue cardinality alone.")
    print("  The reach is NOT what a quadratic ring lacks -- planting a")
    print("  norm-257 place in Z[i] drives a door from 5 to 17. What degree")
    print("  3 changes is the PRICE OF THE CARRIER, and a carrier's norm is")
    print("  what a menu charges.")
    print()
    print("  the supply identity, re-read at this ring: a place's")
    print("  contribution at a foreign prime is depth-free.")
    off = []
    for pl in M.UNIVERSE[:400]:
        for l in (2, 3, 5, 7, 11, 13):
            if l == pl[0]:
                continue
            for a in range(1, 7):
                if v_p(M.lam_P(pl, a), l) != v_p(M.place_norm(pl) - 1, l):
                    off.append((pl, l, a))
    ok(not off, "a foreign-prime contribution moves with depth at %s"
                % off[:2])
    print("    0 off over 400 places, six foreign primes and six depths.")

    print()
    print("  PR6, THE CARRIER TABLE. For each prime l: the least residue")
    print("  cardinality p^d with l | p^d - 1, at d <= 2 -- every shape a")
    print("  quadratic ring has -- against d = 3, with what this ring")
    print("  actually realizes.")
    print()
    print("  %-5s %-16s %-16s %-9s %s"
          % ("l", "least d<=2", "least d=3", "cheaper?", "realized here"))
    wins = 0
    for l in [q for q in range(2, CARRIER_L) if is_prime(q)]:
        lo2 = least_carrier(l, (1, 2))
        lo3 = least_carrier(l, (3,))
        here = [pl for pl in M.UNIVERSE if M.place_norm(pl) == lo3[0]]
        win = lo3 < lo2
        wins += win
        print("  %-5d %-16s %-16s %-9s %s"
              % (l, "%d = %d^%d" % (lo2[0], lo2[1], lo2[2]),
                 "%d = %d^3" % (lo3[0], lo3[1]),
                 "yes" if win else "no",
                 CR.show(here[0]) if here else "-- (not a place of K)"))
    ok(wins > 0, "residue degree 3 never lowers the carrier, so the ceiling "
                 "it lifts buys nothing a price can see")
    print("  %d of the primes read are carried more cheaply at degree 3."
          % wins)

    print()
    print("  and the drive it licenses, run through the engine's own doors --")
    print("  a place over 7 seated beside the INERT place over 2, whose")
    print("  residue field F_8 puts the whole of 8 - 1 = 7 into the")
    print("  invariant, which no residue cardinality of the shape p or p^2")
    print("  over 2 can do (they are 1 and 3):")
    p7 = next(pl for pl in M.UNIVERSE if pl[0] == 7 and pl[2] == 1)
    p2 = next(pl for pl in M.UNIVERSE if pl[0] == 2)
    lone = M.door_r(p7, 1, M.lam_P(p7, 1))
    st = {p7: 1, p2: 1}
    L = M.lam_state(st)
    pop = M.door_r(p7, 1, L)
    print("    state %s, invariant %d, kappa_7 = %d"
          % (CR.show_st(st), L, v_p(L, 7)))
    print("    %-14s lone door %d (price %d), populated door %d (price %d)"
          % (CR.show(p7), lone, 7 ** lone, pop, 7 ** pop))
    ok(pop > lone, "the inert place over 2 does not widen the door over 7, "
                   "so the carrier reading buys nothing here")
    print("    carrier norm %d; the cheapest degree-<=2 carrier of a 7 is %d."
          % (M.place_norm(p2), least_carrier(7, (1, 2))[0]))

    print()
    print("  PR7, THE SHARED NORM. The two places over 23 carry one norm and")
    print("  two ladders, so their LONE-place prices part with depth -- a")
    print("  conjugate pair in a quadratic ring shares a ladder and stays")
    print("  tied forever.")
    print("  %-6s %-22s %-22s"
          % ("depth", "P: door / price", "Q: door / price"))
    parted = 0
    for a in range(1, 9):
        rp = M.door_r(P_UNRAM, a, M.lam_P(P_UNRAM, a))
        rq = M.door_r(Q_RAM, a, M.lam_P(Q_RAM, a))
        parted += (rp != rq)
        print("  %-6d %-22s %-22s"
              % (a, "%d / %d" % (rp, 23 ** rp), "%d / %d" % (rq, 23 ** rq)))
    ok(parted > 0, "the two places over 23 are priced alike at every depth, "
                   "so a shared norm ties them the way a conjugate pair is "
                   "tied")
    print("  they differ at %d of the 8 depths read." % parted)

    print()
    print("  AND THE WALKED EXCESS HERE IS NOT A DATUM, stated so it is not")
    print("  read as one. This ring's walk is degenerate -- one place, no")
    print("  head anywhere (explore_cubic_ring.py F5) -- so it seats nothing")
    print("  a second place could widen. What a WALK reaches in a ring with")
    print("  heads is explore_populated_door.py's measurement and this ring")
    print("  says nothing about it in either direction.")
    return wins


def least_carrier(l, degrees):
    """(N, p, d): the least residue cardinality p^d with d in degrees and
    l | p^d - 1. A pure statement about cardinalities, over all primes p --
    which ring realizes it is read separately."""
    best = None
    p = 2
    while True:
        if is_prime(p):
            for d in degrees:
                if (p ** d - 1) % l == 0:
                    if best is None or p ** d < best[0]:
                        best = (p ** d, p, d)
        if best is not None and p ** min(degrees) > best[0]:
            return best
        p += 1


def main():
    s1_control()
    s2_local_degree()
    s3_residue_degree()
    print("\n  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
