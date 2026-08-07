"""explore_undercut.py -- separating two branches with neither a starved
place nor a lock.

THE QUESTION. Proving that two branches of a minimal-move policy reach
DIFFERENT limits takes a certificate, and two are known. STARVATION shows a
declined core is never seated again, so its limit exponent is 0 in one branch
and positive in the other; it needs the core UNSEATED, and says nothing where
both cores are already seated. THE FREEZE uses a LOCK: once the recurrent
vehicle touches only a fixed set of places, every exponent outside that set
stops moving and any difference there is permanent; it needs the run to lock.
The species that stay open are exactly the ones with neither -- two seated
cores in a SPRAWLING world, where deepening either only makes the other
dearer and the openings never stop (explore_reordering.py F6: EVEN-EVEN, and
DEPTH and ODD-ODD beside it). So the question is whether a THIRD certificate
exists, and one level down: in a sprawling world, does any coordinate of the
limit ever become DETERMINED?

THE DOOR ARITHMETIC, re-derived from the engine rather than remembered
(lam_pp(d, a) = lcm(2^d - 1, 2^ceil_log2(a)), lam_state the lcm over seated
places). Write kappa = v2(lambda) and T = 2^kappa, the TICK. Then
lambda_odd = lcm(2^d - 1) over seated degrees, kappa = max ceil_log2(e), and
the engine's door_r at a place of degree d and exponent e is

  1                  if 2^d - 1 does not divide lambda   (a FRESH-ELIGIBLE
                                                          place; price d)
  sigma := T + 1 - e otherwise                           (price d*sigma)

since raising the 2-part needs e + r > T. A degree whose 2^d - 1 already
divides lambda_odd can never become fresh-eligible again, lambda_odd being
non-decreasing.

THE TICK RECURRENCE, which is the whole mechanism. A clock move takes its
core to e = T + 1, so kappa rises and T at least doubles. Since
sigma = T + 1 - e, EVERY place's sigma rises by T' - T at once, and the
core's own sigma lands at T' - T. A fresh move leaves T alone and drops one
place's sigma by 1. So the state, as the prices see it, is a vector of
sigmas that all shift up together while the mover is reset to the bottom.

THE HAND-ATTACK, on paper before any engine code.

 A. THE UNDERCUT LEMMA (ideal world). If at some state a place Q satisfies
    deg Q <= deg P and price(Q) < price(P), and NEITHER of them can be
    freshly seated, then P is never a minimal move again -- its exponent is
    FROZEN forever, and the limit reads it as a finite coordinate. The
    witness's own ineligibility is load-bearing and not decoration: an
    eligible place's door is 1, so the move that seats it leaves it at
    exponent 1 under an unmoved tick and its price jumps from d to d*T in one
    step, which is the one way the gap below can close behind the
    certificate. Induction on the invariant price(Q) < price(P):
      - a clock move at R outside {P, Q}: both sigmas rise by T' - T, so the
        gap changes by (deg P - deg Q)(T' - T) >= 0;
      - a clock move at Q: price(Q) becomes deg Q * (T' - T) while price(P)
        becomes deg P * (sigma_P + T' - T) >= deg Q * (sigma_P + T' - T),
        which is strictly larger since sigma_P >= 1;
      - a clock move at P: impossible while the invariant holds, Q's door
        being an admissible move that is strictly cheaper;
      - a fresh move at Q or at P: excluded by hypothesis, both being
        ineligible. A RIDER landing on Q drops sigma_Q and so widens the gap;
        a rider landing on P is excluded by lemma C.
    The hypothesis holds for every SEATED place and for every unseated place
    whose degree is already covered by lambda_odd, and lambda_odd never
    falls, so ineligibility once had is permanent. It also needs the TICK
    never to fall, which holds because each state's lambda is a multiple of
    its predecessor's (asserted at every move in S1).
 B. IT NEEDS NEITHER OF THE TWO. P is seated at a positive exponent, so
    nothing is starved, and no recurrence is used -- only two door prices and
    the tick. AND IT SUBSUMES BOTH: starvation is the lemma with Q the seated
    sibling of P's own degree, pinning P at exponent 0, and the freeze is the
    lemma pinning P at whatever exponent it holds. What the two certificates
    share is not a family resemblance but one argument. (The run splits this
    in half -- F2. Starvation's subsumption is measurable here and measured;
    the freeze's cases live over the number rings, which flag 2 carries
    nothing to, so for those the shared SHAPE is all this slate is entitled
    to and the instance claim is banked.)
 C. THE ELEMENT WORLD PAYS TWO PRICES. A vehicle there is a core plus the
    minimal representative of the class it must cancel, so
    deg P * sigma_P <= price(P) <= deg P * sigma_P + g and the certificate
    needs SLACK g on the core gap. And a RIDER raises a place's exponent
    without a clock move, so the induction also needs P outside the rider
    set -- which is the passenger route lemma A already had to shut, and
    needs deg P > g.
 D. WHAT IT DOES TO THE THREE OPEN SPECIES.
    EVEN-EVEN, two clock moves at degrees d1 < d2 tied at d1*s1 = d2*s2:
    take the LOWER degree, and the higher member's price becomes
    d2(s2 + T) = d1*s1 + d2*T against the mover's d1*T, so the gap is
    d1*s1 + (d2 - d1)T, at least (d2 - d1)T > 0, and lemma A freezes P2 at
    its current exponent. The other
    branch seats P2 at T + 1 > e2 and exponents never fall, so THE TWO
    LIMITS DIFFER AT P2 -- at every occurrence, with no horizon.
    DEPTH, one degree at two exponents (element world only, the rider being
    what lets equal degrees tie): the gap after taking the deeper member is
    d*sigma2 > 0 with equal degrees, so the lemma applies where the slack
    clears g.
    ODD-ODD, two fresh moves at degrees d1 != d2: taking P1 leaves P2
    fresh-eligible unless d2 divides d1, in which case P2's door jumps to
    T + 1 and the lemma starves it. Predicts the split the source rig saw as
    "mixed": REJOIN exactly when neither degree divides the other.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the ideal world to the element world: the sigma recurrence and the
    monotone gap. Both are stated for bare place powers, and lemma C names
    the two holes the rider opens. The rig runs the worlds separately and
    the element certificate carries the slack explicitly.
 2. From the function fields to the number rings: NOTHING is carried. There
    the tick has no analogue yet written down and the freeze already runs
    off the lock; the transfer is named and left to the ring that owns it.
 3. From the exhaustive region to the trajectory region: nothing. A zero in
    the shallow region says "cannot occur to the cap", a zero along walks
    says only "did not occur", and the two are printed apart.
 4. "Branches never rejoin in any measured run" is NOT assumed in either
    direction: every certificate here is asserted against the source rig's
    own rejoin detector, which is what would catch the lemma being wrong.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE DOOR ARITHMETIC IS THE ENGINE'S. What the rig PRINTS: over the
    exhaustive region, the engine's door_r against 1 for fresh-eligible
    places and T + 1 - e for the rest, and the tick recurrence at every
    minimal move -- T' >= 2T for a clock move, T' = T for a fresh one, the
    core landing at exponent T + 1.
    KILL: one mismatch. The whole argument is arithmetic on these two
    identities, so a miss here ends it.
PR2 THE CERTIFICATE FREEZES. What the rig PRINTS: at every certified
    (place, witness) pair on a walked state, a forward check following the
    canonical continuation and the certified place's exponent at each step.
    KILL: one certified place whose exponent moves.
PR3 EVERY IDEAL-WORLD EVEN-EVEN PAIR IS A CHOICE. What the rig PRINTS: per
    ring per region, the pairs, the certificate on the higher-degree member
    in the lower-degree member's branch, and the two branches' exponents at
    that place.
    KILL: one even-even pair where the higher-degree member is a minimal
    move again in the lower's branch, or where the two exponents agree.
PR4 THE CERTIFICATE AND THE REJOIN DETECTOR NEVER BOTH FIRE. What the rig
    PRINTS: pairs the source rig calls REJOIN, with the certificate run on
    both members.
    KILL: one rejoining pair carrying a certificate -- which would refute
    the lemma rather than the species reading.
PR5 THE UNDERCUT SUBSUMES STARVATION. What the rig PRINTS: every within-type
    decline and every CLASS-species decline the older certificates cover,
    with the undercut run on the same core.
    KILL: one core the old certificate covers and the undercut does not.
PR6 THE OPEN SPECIES, printed and not predicted: EVEN-EVEN, DEPTH and
    ODD-ODD pairs by CERTIFIED / REJOIN / UNCOVERED, and for ODD-ODD the
    split by whether one degree divides the other.
PR7 THE FREEZE CENSUS, printed and not predicted: at every tie state, how
    many places the certificate freezes and how many stay LIVE -- the
    quantitative answer to whether a sprawling world determines
    coordinates.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE UNDERCUT IS A THIRD CERTIFICATE, and it needs neither of the other
   two (proved for the ideal world -- lemma A above, which is an induction
   over the move model and calls on no computation; 2489 certified places
   followed 18198 moves along canonical continuations with 0 exponents
   moving; every aggregate here printed by the rig). A place is frozen by
   TWO DOOR PRICES and the doubling tick: some place of degree at most its
   own is cheaper by more than the genus, and neither that place nor this one
   can still be seated FRESH, and no rider can carry this one. Nothing is
   starved --
   the frozen place is seated at a positive exponent -- and nothing locks:
   the trajectory goes on opening fresh degrees forever while the frozen
   coordinate stands. So the answer to the question one level down is YES: a
   sprawling world does determine coordinates of its limit.

F2 AND IT SUBSUMES STARVATION OUTRIGHT (rule in range; 60972 of 60972
   cores the starvation certificate covers, over six rings and both worlds).
   Starvation is the undercut with the witness taken to be the seated sibling
   of the declined core's own degree, pinning the exponent at 0, and the
   correspondence is exact rather than a family resemblance: that
   certificate's hypotheses -- d*e > g against a seated neighbour's door, and
   the core off the rider set -- are the undercut's own two hypotheses in the
   special case where the witness IS the neighbour.
   THE FREEZE IS THE SAME SHAPE AND IS NOT MEASURED HERE, which is the
   honest half. It lives over the number rings, where this rig carries
   nothing (transplant flag 2): the undercut pinning an exponent wherever it
   stands is what a freeze does, and the lock it was written with is
   unnecessary in a SPRAWLING world -- which is proved above. Whether the
   lock's own cases are literally instances of this lemma is a question about
   door prices over a number ring, and it is banked rather than answered.
   (Answered since, in explore_undercut_nf.py: they are, once the lemma is
   ported with two hypotheses equal characteristic hides -- a shared residue
   characteristic, and a comparison by LOCAL degree rather than by degree.
   What survives here unchanged is everything above; what this paragraph
   should no longer be read as saying is that the number-ring side is open.)

F3 THE EVEN-EVEN SPECIES IS A CHOICE, AT EVERY OCCURRENCE, and the corpus
   filed it open (proved in the ideal world, 952 of 952 pairs certified over
   six rings and both regions with 0 uncovered; rule in range in the element
   world, 396 of 558). Take the LOWER degree and the higher-degree member's
   price exceeds the mover's by d1*s1 + (d2 - d1)*T, hence by AT LEAST
   (d2 - d1)*T, a margin the tick doubles, so it
   never competes again and its exponent stands at e2 forever; the other
   branch seats it at T + 1 > e2 and exponents never fall. The two limits
   differ at that place with no horizon, no lock and nothing starved. The
   element world's 162 residual pairs are all at ONE ring and all for one
   reason -- a core of degree at most the genus, which a rider can carry
   back.

F4 WHAT A SPRAWLING WORLD ACTUALLY LOOKS LIKE, which the certificate makes
   countable (rule in range, S2; six rings, both worlds, both regions --
   the figures below are the IDEAL world's, the element world freezing
   strictly more at every ring and reaching 0.00 live at two of them). At a
   walked state the certificate can speak about 8.3 to 16.8 places, and all
   but 1.05 to 1.10 of them are FROZEN. The survivors are not a scatter:
   701 of the 712 live places over the six ideal-world walks have DEGREE 1.
   WHAT THIS DOES NOT SAY is the limit. It counts frozen coordinates at the
   states the walks reach, and reading it as "the limit is determined almost
   everywhere as soon as it is passed, with only rational places still
   moving" is an EXTRAPOLATION: the census is a measurement over a horizon
   and the reading is a claim about infinity. The mechanism that would close
   the gap is a race between the tick and the fresh price, and it is written
   down rather than proved. That reading is the open claim, not a finding
   here.

F5 THE RESIDUAL IS ALMOST ALL RIDER'S REACH, NOT ABSENCE OF A CERTIFICATE
   (rule in range; 1866 uncovered pairs, each filed under BOTH branches'
   refusals, S4). A residual means neither branch certifies, so both reasons
   are read, and the roll-up is the rig's. 1822 of the 1866 have a branch
   refused because a core lies inside the RIDER'S REACH: the DEPTH species --
   one degree at two exponents, which is where the handover pointed -- at 295
   of 295, every one of its cores a rational place at g = 1, plus 1303 CLASS
   pairs, 162 EVEN-EVEN ones and 62 ODD-EVEN ones whose other branch is a
   fresh core instead. Another 32, the whole exhaustive-region ODD-ODD
   residual, are refused on BOTH sides for a core that can still be seated
   FRESH -- the state the discount of F6 out-competes.
   The last 12, all ODD-EVEN with a fresh member on the other side, carry a
   branch whose cheapest witness does not clear the SLACK -- which is what
   this rig's tag records and all it records. (Read off the pairs since, in
   explore_the_twelve.py: none of the twelve lacks a cheaper witness. Eight
   are tied with one exactly and four are cheaper than one by less than the
   genus, all twelve in the element world where the slack is the genus; and
   the refusing state's unique minimal move certifies the target one step
   later, so all twelve separate. What this paragraph should no longer be
   read as saying is that any pair here carries a genuine absence.) So the
   open species no longer divide into "has a certificate" and "has none";
   they divide at the line the GENUS draws, which is the line the older
   certificate drew too. One lemma and one blind spot, and the blind spot is
   a ring-design question rather than a missing argument.

F6 THE RIDER'S DISCOUNT -- an UNFROZEN find, and it replaces a prediction of
   this rig's own that the run refuted (rule in range, S7; every fall in the
   menu minimum attributed over the trajectory region at six rings, 0 falls
   outside the move's own support). A rider is not priced at its degree: it
   raises a place's exponent by a, so that place's own DOOR COUNT falls by a
   and its PRICE by d*a, with no clock move at all. So an element FRESH move can lower the menu
   minimum below the tie cost, and the other member of a tie is then
   OUT-COMPETED rather than dominated -- neither rejoining nor separating.
   This is the hole lemma C looked for in the wrong place: the rider does not
   move the clock (0 of 1065 in the source rig, and 0 again here), it
   discounts a door. It accounts for the two residuals the source rig left
   unexplained -- the element ODD-EVEN residual at 74 of 74 pairs and the
   exhaustive-region ODD-ODD residual at 32 of 32 both sit at a fallen
   minimum, read in both orders. THE REFUTED PREDICTION was lemma D's
   ODD-ODD half: that a pair rejoins exactly when neither degree divides the
   other. Every ODD-ODD pair measured has non-dividing degrees and 32 of
   them do not rejoin, so divisibility explains nothing there.

F7 WHAT IS STILL OPEN, sharpened rather than closed. The 74-pair and 32-pair
   residuals are shown to sit at a fallen minimum but are not attributed
   pair by pair to the core drop or the rider drop, which S7 separates only
   in aggregate. And a place inside the rider's reach has no certificate in
   any world -- the DEPTH species entire, and the CLASS species below the
   genus -- which is the readmission regime the capacity bound already
   files, and is now the ONLY thing between the undercut and every species
   here: the 12 pairs of F5 read as the smaller half when this was written,
   and explore_the_twelve.py closes them where they stand.

THE DESIGN, in seven sections after the control.

 S1 THE POSITIVE CONTROL, run before any census is read.
    (a) The door arithmetic and the tick recurrence (PR1).
    (b) THE CERTIFICATE DETECTOR on planted states: a place undercut by an
        equal degree (must fire), a place undercut only by a LARGER degree
        (must refuse -- the case the induction cannot cover), a
        fresh-eligible place (must refuse), a place whose ONLY cheaper
        neighbour is fresh-eligible (must refuse -- and the same state must
        FIRE with the eligibility filter lifted, or the control says nothing
        about the filter), and in the element world a ridable place (must
        refuse, the passenger route being open), a core gap inside the genus
        SLACK (must refuse) and one clear of it (must fire) -- the element
        path carries a third of the verdicts and needs a positive of its
        own.
    (c) The exponent shape along ideal walks: every seated exponent is 1 or
        a tick plus one, which is what makes sigma >= T/2.
    (d) THE CENSUS PATH AGAINST THE CERTIFICATE PATH, place by place. The
        freeze census reads per-degree minima and the certificate reads a
        witness list, so F4's headline rests on a second code path; two
        paths for one predicate are compared rather than trusted.
 S2 THE FREEZE CENSUS over the exhaustive region, both worlds, six rings
    (PR7), with the LIVE set printed by degree.
 S3 THE FORWARD CHECK: certified places followed along the canonical
    continuation (PR2).
 S4 THE SPECIES VERDICTS in both regions: every cross-type pair classified
    by the source rig's own species function, then run through the
    certificate and the rejoin detector, which are asserted never to agree
    (PR3, PR4, PR6).
 S5 THE SUBSUMPTION: the two older certificates against the undercut on the
    same cores (PR5).
 S6 THE SEPARATION SPECIMENS: for even-even pairs, the frozen place's
    exponent in each branch, printed as the separation itself.
 S7 WHERE THE MENU MINIMUM FALLS, and what lowered it -- the section the run
    added: every fall attributed to the move's own core or to its rider, a
    fall anywhere else being a third mechanism.

Run: `python explore_undercut.py`. RUN RECORD (128206 checks, ~15 s). S1
control: the closed-form door against the engine's own door_r at 44828 place
readings over 12 ring-world slices, with the tick recurrence read at 2351
moves -- a clock move at least doubling the tick and landing its core at
T + 1 exactly in the ideal world, a fresh move leaving it alone, and 0
element fresh vehicles moving the tick through a rider; the detector firing
on a planted starved sibling at all six rings and REFUSING all four cases the
induction cannot cover -- including a place whose only cheaper neighbour is
fresh-eligible, where the same state is checked to FIRE with the eligibility
filter lifted, so the control tests the filter and not the state -- plus the
ELEMENT path's own planted positive and a core gap inside the genus slack
refused at all five rings that have a genus, each control asserted to have
actually run; and
every seated exponent along the ideal walks either 1 or a tick plus one, to
a maximum of 17. S2 census, states to degree 8: per walked state 8.3/9.8/
13.1/12.2/16.8/13.1 speakable places in the ideal world against 1.05 to 1.10
live, the live set 701 of 712 at degree 1 (F4); the element world's live
count falls to 0.00 at two rings. S1(d): the census path against the
certificate path place by place, 480224 comparisons over 642 states and 12
ring-world slices with 0 disagreements. S3: 2489 certified places followed 18198 moves, 0
exponents moved, 2091 walks cut short by the trimmed universe and
reported. S4, both regions, every total printed by the rig rather than added
by hand: ideal EVEN-EVEN 952 certified and 0 otherwise; element EVEN-EVEN 396
certified against 162 uncovered, every one at g2 with a ridable core; DEPTH
295 uncovered, all ridable; CLASS 478 certified and 1303 uncovered, every
one ridable; ideal ODD-EVEN 3401 rejoins plus 868 delayed and 0 uncovered;
element ODD-EVEN 74 uncovered and ODD-ODD 32, all 106 at a fallen minimum.
1866 uncovered pairs in all, filed under BOTH branches' refusals: 1822 with a
branch inside the rider's reach, 32 with a core still seatable fresh on both
sides, and 12 with a branch whose cheapest witness does not clear the slack.
The certificate and the rejoin detector
never both fired, and every certified pair was also read against the
ENGINE's menu at the successor. S5: 60972 of 60972 older certificates
covered. S7, at the first three minimal vehicles of each walked
state: 37 ideal falls over 1632 moves, every one at the move's own core,
against 18 element falls over 1370 of which 4 at a rider; and not one
cheapened place outside the moving vehicle's own support at either world.
Slate PR1-PR7: PR1, PR2, PR3, PR4, PR5, PR6 and PR7 hit. Unfrozen finds: the
rider's discount and the two residuals it accounts for (F6), and the freeze
census reading almost the whole speakable universe (F4). REFUTED at the run:
lemma D's ODD-ODD divisibility half (F6).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_greedy_image_ec as EC        # the genus 0 and 1 rings
import explore_coarse_type as CT            # the ladder, the types, the states
import explore_reordering as RO             # the species, the two detectors

CHECKS = 0

SCAN_DEG = {"F_2[x]": 8, "h2": 8, "h3": 8, "h4": 8, "h5": 8, "g2": 8}
WALK_T = 10          # moves per canonical walk in the trajectory region
SEED_DEG = 2         # walk seeds are the void + every effective divisor here
FORWARD_T = 10       # moves the forward check follows a frozen place for
PAIR_CAP = 2000      # pairs examined per tie state; excess is REPORTED
ARITH_STATES = 400   # states per ring the door-arithmetic control reads
TRUNC = {"pair-cap": 0, "forward-short": 0}


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# --------------------------------------------------------- the arithmetic
def tick(lam):
    """T = 2^v2(lambda)."""
    return 1 << EC.v2(lam)


def eligible(R, pl, lam):
    """Can this place be seated by a FRESH move -- one that raises
    lambda_odd? Its degree's factor must be missing from lambda, and since
    lambda_odd never falls, a No here is permanent."""
    return lam % ((1 << R.deg[pl]) - 1) != 0


def sigma(R, st, pl, lam):
    """The door count in closed form: T + 1 - e for a place whose degree
    lambda_odd already covers, 1 for a fresh-eligible one."""
    if eligible(R, pl, lam):
        return 1
    return tick(lam) + 1 - st.get(pl, 0)


def price(L, st, pl, lam):
    """THE CORE PRICE, deg * door, which is what the lemma's invariant is
    written in -- and it takes no WORLD, because it has none to take: the
    core costs deg * door in both, and the element world's difference is the
    rider, which veh_price below carries. The door is the CLOSED FORM, which S1 certifies against the
    engine's own door_r -- the engine searches for it one exponent at a time
    and this rig prices every place of every state.

    The element world's VEHICLE costs this plus a rider of degree at most g,
    so the two prices differ by at most g and the certificate carries that
    slack (below). Certifying on the vehicle price instead would be a
    DIFFERENT and insufficient condition: the induction's monotone quantity is
    the CORE gap, and a vehicle gap of g leaves the core gap only positive
    where the invariant needs it above g."""
    return L.R.deg[pl] * sigma(L.R, st, pl, lam)


def veh_price(L, world, st, pl, lam):
    """What the ENGINE's menu would charge for a vehicle cored here: the core
    plus the rider its class summons, minimised over the offsets the engine
    offers, which is one per unit of genus (0..1 at the elliptic ladder,
    0..2 at genus 2 -- the ranges those two menus actually enumerate)."""
    r = sigma(L.R, st, pl, lam)
    if world == "ideal":
        return L.R.deg[pl] * r
    return min(L.R.veh_deg(L.complete(pl, r + j)) for j in range(L.g + 1))


def witnesses(L, world, st, lam, pl, allow_eligible=False):
    """The candidate undercutters for `pl`: every place of degree at most
    deg pl whose price the dynamics cannot RAISE relative to pl's.

    A FRESH-ELIGIBLE place is disqualified as a witness, and this is not
    fastidiousness -- it is where the induction breaks. Its door is 1, so its
    price is its bare degree; the move that seats it leaves it at exponent 1
    under an unmoved tick, so its price jumps from d to d*T in one step and
    the gap the certificate opened can close behind it. Every other place's
    price moves only with the tick, or DOWN when a rider lands on it, and
    both widen the gap. Unseated places share a price inside a degree, so one
    per (degree, class) group is priced."""
    R, d = L.R, L.R.deg[pl]
    out, seen = [], set()
    for q, e in st.items():
        if e and R.deg[q] <= d and q != pl:
            out.append(q)
    for dd in range(1, d + 1):
        for q in R.by_deg.get(dd, []):
            if st.get(q, 0) or q == pl:
                continue
            if eligible(R, q, lam) and not allow_eligible:
                continue
            key = (dd, R.cls[q] if world == "element" else -1)
            if key in seen:
                continue
            seen.add(key)
            out.append(q)
    return out


def undercut(L, world, st, lam, pl):
    """The certificate at (state, place). Returns (verdict, detail).

    Three conditions, each one of the lemma's hypotheses: the place cannot be
    freshly seated, it lies outside the rider set in the element world (the
    passenger route), and some place of degree at most its own has a cheaper
    CORE -- by more than the slack g where a rider can move a vehicle's
    price. The witness list carries the fourth hypothesis, its own
    ineligibility."""
    R = L.R
    if eligible(R, pl, lam):
        return False, "eligible", \
            "fresh-eligible, so a fresh move can still seat it"
    if world == "element" and pl in RO.ridable(L):
        return False, "ridable", \
            "degree %d <= g = %d, so a rider can carry it" % (R.deg[pl], L.g)
    slack = 0 if world == "ideal" else L.g
    own = price(L, st, pl, lam)
    best, bq = None, None
    for q in witnesses(L, world, st, lam, pl):
        p = price(L, st, q, lam)
        if best is None or p < best:
            best, bq = p, q
    if best is None or best + slack >= own:
        return False, "no-undercut", \
            "no cheaper vehicle at a degree <= %d (own %d, best %s)" \
            % (R.deg[pl], own, best)
    return True, "undercut", "core gap: a degree-%d place at %d + %d < %d" % (
        R.deg[bq], best, slack, own)


def live_places(L, world, st, lam):
    """(speakable, frozen, live degrees) over the whole place universe.
    SPEAKABLE is the set the certificate can say anything about at all: a
    fresh-eligible place is still seatable by a fresh move and a ridable one
    can arrive as a passenger, so both are exempt by hypothesis and are
    counted apart rather than scored LIVE. Of the rest, a place is LIVE when
    the certificate does not fire on it, and the certificate fires exactly when
    the place's price is above the running minimum over the degrees at or
    below its own -- so the census reads the per-degree minima and never
    prices a place twice. Unseated places share a price inside a (degree,
    class) group, which is the same grouping the element menu prices by."""
    R = L.R
    frozen = speakable = 0
    livedeg = {}
    run = None                                  # min price at a LOWER degree
    slack = 0 if world == "ideal" else L.g
    rid = RO.ridable(L) if world == "element" else set()
    for d in sorted(R.by_deg):
        rows, groups = [], {}
        for pl in R.by_deg[d]:
            if st.get(pl, 0):
                rows.append((price(L, st, pl, lam), 1,
                             eligible(R, pl, lam) or pl in rid,
                             eligible(R, pl, lam)))
            else:
                groups.setdefault(R.cls[pl] if world == "element" else -1,
                                  []).append(pl)
        for pls in groups.values():
            rows.append((price(L, st, pls[0], lam), len(pls),
                         eligible(R, pls[0], lam) or pls[0] in rid,
                         eligible(R, pls[0], lam)))
        if not rows:
            continue
        # an eligible place cannot WITNESS (its price jumps when it is
        # seated), so it sets no minimum -- the same restriction the
        # certificate's witness list carries
        wit = [p for p, _, _, el in rows if not el]
        md = min(wit) if wit else None
        if md is None:
            base = run
        else:
            base = md if run is None else min(md, run)
        for p, n, exempt, _ in rows:
            if exempt:
                continue
            speakable += n
            # a place at the degree's own minimum can only be cut from BELOW
            cut = run if p == md else base
            if cut is not None and cut + slack < p:
                frozen += n
            else:
                livedeg[d] = livedeg.get(d, 0) + n
        run = base
    return speakable, frozen, livedeg


# ------------------------------------------------------------- S1 control
def s1a_arithmetic(ladder):
    """PR1: the closed-form door and the tick recurrence, against the
    engine, over a bounded slice of the exhaustive region."""
    print("  ring     world    states  places read  moves read  "
          "rider moved the tick")
    tot = [0, 0, 0, 0]
    for L in ladder:
        for world in ("ideal", "element"):
            divs = CT.eff_divisors(L, 5)[:ARITH_STATES]
            nplace = nmove = riderclock = 0
            for v, _ in divs:
                st = dict(v)
                lam = L.R.lam_state(st)
                T = tick(lam)
                for d in sorted(L.R.by_deg):
                    for pl in L.R.by_deg[d][:3]:
                        r = L.R.door_r(pl, st.get(pl, 0), lam)
                        ok(r == sigma(L.R, st, pl, lam),
                           "%s: door_r %d against the closed form %d at "
                           "degree %d exponent %d, T = %d"
                           % (L.name, r, sigma(L.R, st, pl, lam), d,
                              st.get(pl, 0), T))
                        nplace += 1
                try:
                    _, _, ties = RO.menu_of(L, world, st)
                except AssertionError:
                    continue
                for veh in ties[:4]:
                    core, e, r, kind = RO.core_of(L, world, st, veh, lam)
                    st2 = EC.apply_veh(st, veh)
                    T2 = tick(L.R.lam_state(st2))
                    if kind == "fresh":
                        # a fresh CORE leaves the tick alone, but an element
                        # rider lands on a place of its own and can carry it
                        # over a 2-power frontier: an observable, not a law
                        if world == "ideal":
                            ok(T2 == T, "%s: a fresh move moved the tick "
                                        "%d -> %d" % (L.name, T, T2))
                        elif T2 != T:
                            riderclock += 1
                    else:
                        ok(T2 >= 2 * T,
                           "%s/%s: a clock move left the tick at %d -> %d"
                           % (L.name, world, T, T2))
                        # the core reaches T + 1 exactly in the ideal world;
                        # in the element world its own rider can push further
                        ok(st2[core] == T + 1 if world == "ideal"
                           else st2[core] >= T + 1,
                           "%s/%s: a clock move landed at exponent %d against "
                           "T + 1 = %d" % (L.name, world, st2[core], T + 1))
                    # the monotone gap rests on this: lambda is a multiple
                    # of its predecessor, so the tick can never fall
                    ok(T2 >= T, "%s/%s: the tick FELL, %d -> %d"
                       % (L.name, world, T, T2))
                    for pl in list(st2)[:6]:
                        ok(sigma(L.R, st2, pl, L.R.lam_state(st2))
                           == L.R.door_r(pl, st2.get(pl, 0),
                                         L.R.lam_state(st2)),
                           "%s/%s: the closed form missed the successor"
                           % (L.name, world))
                    nmove += 1
            print("  %-8s %-8s %-7d %-12d %-11d %d"
                  % (L.name, world, len(divs), nplace, nmove, riderclock))
            for i, v in enumerate((len(divs), nplace, nmove, riderclock)):
                tot[i] += v
    print("  %-8s %-8s %-7d %-12d %-11d %d"
          % ("TOTAL", "", tot[0], tot[1], tot[2], tot[3]))


def s1b_detector(ladder):
    """PR1's other half: the certificate must fire on a planted undercut and
    REFUSE the three cases the induction does not cover."""
    print("  ring     fires  refuses-larger-degree  refuses-fresh  "
          "refuses-ridable  refuses-eligible-witness  element fires  "
          "refuses-inside-slack")
    for L in ladder:
        R = L.R
        fires = larger = fresh = rid = elig_wit = 0
        el_fire = el_slack = 0
        # a state where one place of a degree is seated and its siblings are
        # not: the seated one undercuts them, which is starvation
        for d in sorted(R.by_deg):
            pls = R.by_deg[d]
            if len(pls) < 2:
                continue
            st = {pls[0]: 3}
            lam = R.lam_state(st)
            if eligible(R, pls[1], lam):
                continue
            v = undercut(L, "ideal", st, lam, pls[1])[0]
            ok(v, "%s: the certificate missed a starved sibling at degree %d"
               % (L.name, d))
            fires += 1
            break
        # a place of SMALLER degree that is pricier than a larger-degree one:
        # the invariant can break when the cheap witness is clocked, so the
        # detector must refuse it
        for d in sorted(R.by_deg):
            if larger or d < 2 or not R.by_deg.get(d) or not R.by_deg.get(1):
                continue
            lo, hi = R.by_deg[1][0], R.by_deg[d][0]
            # a deeply seated place of degree d has door T + 1 - e, so at
            # e = T it costs d against an unseated rational place's T + 1
            for e in (2, 4, 8):
                st = {hi: e}
                lam = R.lam_state(st)
                if eligible(R, lo, lam) or price(L, st, lo, lam) \
                        <= price(L, st, hi, lam):
                    continue
                v = undercut(L, "ideal", st, lam, lo)[0]
                ok(not v, "%s: the certificate fired on a place undercut only "
                          "from ABOVE its degree" % L.name)
                larger += 1
                break
        # a fresh-eligible place is never frozen: a fresh move can seat it
        for d in sorted(R.by_deg):
            st = {R.by_deg[max(R.by_deg)][0]: 1}
            lam = R.lam_state(st)
            cand = [pl for pl in R.by_deg[d] if eligible(R, pl, lam)]
            if not cand:
                continue
            v = undercut(L, "ideal", st, lam, cand[0])[0]
            ok(not v, "%s: the certificate froze a fresh-eligible place"
               % L.name)
            fresh += 1
            break
        # and in the element world a place a rider can carry is refused
        for pl in sorted(RO.ridable(L)):
            st = {R.by_deg[max(R.by_deg)][0]: 1, pl: 2}
            lam = R.lam_state(st)
            v = undercut(L, "element", st, lam, pl)[0]
            ok(not v, "%s: the element certificate fired on a ridable place"
               % L.name)
            rid += 1
            break
        # THE ELIGIBLE WITNESS. A place whose only cheaper neighbour at or
        # below its degree can still be seated FRESH must be REFUSED, since
        # that neighbour's price jumps from d to d*T the moment it is taken.
        # Two-sided: the same state must FIRE once the eligibility filter is
        # lifted, or the control says nothing about the filter.
        for d in sorted(R.by_deg):
            if elig_wit or not R.by_deg.get(d):
                continue
            for e in (2, 4, 8):
                target = R.by_deg[d][0]
                st = {target: e}
                lam = R.lam_state(st)
                if eligible(R, target, lam):
                    continue
                own = price(L, st, target, lam)
                with_el = [price(L, st, q, lam) for q
                           in witnesses(L, "ideal", st, lam, target, True)]
                without = [price(L, st, q, lam) for q
                           in witnesses(L, "ideal", st, lam, target)]
                if not with_el or min(with_el) >= own:
                    continue
                if without and min(without) < own:
                    continue
                v, tag, _ = undercut(L, "ideal", st, lam, target)
                ok(not v, "%s: the certificate fired on a place whose only "
                          "cheaper neighbour is fresh-eligible" % L.name)
                ok(tag == "no-undercut",
                   "%s: the eligible-witness refusal came back as %s"
                   % (L.name, tag))
                elig_wit += 1
                break

        # THE ELEMENT PATH'S OWN POSITIVE, and THE SLACK. Every control above
        # runs the IDEAL path while a third of the verdicts are the element
        # path's, so that path needs a planted positive of its own; and the
        # genus SLACK is a hypothesis with the same standing as the two above,
        # so it needs a state where the core gap is positive but no larger
        # than g -- refused with the slack, firing without it.
        for a in range(1, 10):
            for b in range(0, 10):
                if el_fire and el_slack:
                    continue
                for dp in sorted(R.by_deg):
                    if dp <= L.g or not R.by_deg.get(dp):
                        continue
                    for dq in sorted(R.by_deg):
                        if dq > dp or not R.by_deg.get(dq):
                            continue
                        tgt = R.by_deg[dp][0]
                        wit = next((x for x in R.by_deg[dq] if x != tgt), None)
                        if wit is None:
                            continue
                        st = {tgt: a}
                        if b:
                            st[wit] = b
                        lam = R.lam_state(st)
                        if eligible(R, tgt, lam) or eligible(R, wit, lam):
                            continue
                        # the gap the CERTIFICATE sees, which is against the
                        # cheapest witness and not against the planted one:
                        # measuring it against `wit` alone would call a state
                        # slack-bound that some third place undercuts outright
                        wits = [price(L, st, q, lam) for q in
                                witnesses(L, "element", st, lam, tgt)]
                        if not wits:
                            continue
                        gap = price(L, st, tgt, lam) - min(wits)
                        v, tag, _ = undercut(L, "element", st, lam, tgt)
                        if 0 < gap <= L.g and not el_slack:
                            ok(not v, "%s: the element certificate fired on a "
                                      "core gap of %d, inside the slack g = %d"
                               % (L.name, gap, L.g))
                            ok(tag == "no-undercut",
                               "%s: the slack refusal came back as %s"
                               % (L.name, tag))
                            el_slack += 1
                        elif gap > L.g and not el_fire:
                            ok(v, "%s: the element certificate missed a core "
                                  "gap of %d against g = %d"
                               % (L.name, gap, L.g))
                            el_fire += 1

        # a control that never ran is not a control: each planted case must
        # have been exercised, the ridable one only where a rider exists
        ok(fires == 1, "%s: the fire control never ran" % L.name)
        ok(larger == 1, "%s: the larger-degree refusal never ran" % L.name)
        ok(fresh == 1, "%s: the fresh-eligible refusal never ran" % L.name)
        ok(rid == 1 or not RO.ridable(L),
           "%s: the ridable refusal never ran" % L.name)
        ok(elig_wit == 1, "%s: the eligible-witness refusal never ran"
           % L.name)
        ok(el_fire == 1 or not L.g, "%s: the element path got no positive"
           % L.name)
        ok(el_slack == 1 or not L.g, "%s: the slack refusal never ran"
           % L.name)
        print("  %-8s %-6d %-22d %-14d %-16d %-25d %-13d %d"
              % (L.name, fires, larger, fresh, rid, elig_wit, el_fire,
                 el_slack))


def s1c_shape(ladder):
    """The exponent shape the tick story implies: along an ideal walk every
    seated exponent is 1 or a tick plus one, so sigma >= T/2 and the cheapest
    door is never free."""
    print("  ring     walk states  seated exponents read  max exponent")
    for L in ladder:
        n = m = 0
        best = 0
        for seed in [{}] + [dict(v) for v, _ in CT.eff_divisors(L, 1) if v]:
            for st, lam, cost, ties in RO.walk(L, "ideal", seed, WALK_T):
                n += 1
                T = tick(lam)
                for pl, e in st.items():
                    if not e:
                        continue
                    ok(e == 1 or (e - 1) & (e - 2) == 0,
                       "%s: a seated exponent %d is neither 1 nor a tick "
                       "plus one" % (L.name, e))
                    ok(e <= max(1, T // 2 + 1),
                       "%s: exponent %d against tick %d" % (L.name, e, T))
                    best = max(best, e)
                    m += 1
        print("  %-8s %-12d %-22d %d" % (L.name, n, m, best))


def s1d_census_path(ladder):
    """The freeze census (S2) reads per-degree minima and the certificate
    reads a witness list: TWO code paths for one predicate, and the census
    carries a headline. So the counts are compared place by place -- a census
    that agrees with nothing is a number, not a measurement."""
    print("  ring     world    states  places compared  disagreements")
    tot = [0, 0, 0]
    for L in ladder:
        for world in ("ideal", "element"):
            n = m = bad = 0
            for v, _ in CT.eff_divisors(L, 4)[:80]:
                st = dict(v)
                lam = L.R.lam_state(st)
                frozen = live_places(L, world, st, lam)[1]
                byhand = 0
                for d in sorted(L.R.by_deg):
                    for pl in L.R.by_deg[d]:
                        if undercut(L, world, st, lam, pl)[0]:
                            byhand += 1
                        m += 1
                if byhand != frozen:
                    bad += 1
                ok(byhand == frozen,
                   "%s/%s: the census froze %d places and the certificate %d "
                   "at %s" % (L.name, world, frozen, byhand,
                              L.mod.fmt_state(L.R, st)))
                n += 1
            print("  %-8s %-8s %-7d %-16d %d" % (L.name, world, n, m, bad))
            for i, v in enumerate((n, m, bad)):
                tot[i] += v
    print("  %-8s %-8s %-7d %-16d %d"
          % ("TOTAL", "", tot[0], tot[1], tot[2]))


# ---------------------------------------------------------- S2 the census
def s2_census(ladder, region):
    """PR7: how much of the place universe the certificate freezes."""
    print("  ring     world    states  speakable/state  frozen  live  "
          "live degrees")
    out = {}
    tot = {}
    for L in ladder:
        for world in ("ideal", "element"):
            n = sp = fz = 0
            degs = {}
            for st, lam in region(L, world):
                s, f, ld = live_places(L, world, st, lam)
                n += 1
                sp += s
                fz += f
                for d, c in ld.items():
                    degs[d] = degs.get(d, 0) + c
            out[(L.name, world)] = (n, sp, fz)
            print("  %-8s %-8s %-7d %-16.1f %-7.1f %-5.2f %s"
                  % (L.name, world, n, sp / max(n, 1), fz / max(n, 1),
                     (sp - fz) / max(n, 1), dict(sorted(degs.items()))))
            a = tot.setdefault(world, [0, 0, 0, 0, 0])
            a[0] += n
            a[1] += sp
            a[2] += fz
            a[3] += sum(degs.values())
            a[4] += degs.get(1, 0)
    for world, a in sorted(tot.items()):
        print("  %-8s %-8s %-7d speakable %d  frozen %d  live %d, of which "
              "%d at degree 1" % ("TOTAL", world, a[0], a[1], a[2], a[3], a[4]))
    return out


# ---------------------------------------------- S3 the forward check
def forward(L, world, st, lam, pl):
    """Follow the canonical continuation and report the certified place's
    exponents. The lemma says the first is the last."""
    seen = [st.get(pl, 0)]
    cur = dict(st)
    for _ in range(FORWARD_T):
        try:
            l2, _, ties = RO.menu_of(L, world, cur)
        except AssertionError:
            TRUNC["forward-short"] += 1
            break
        cur = EC.apply_veh(cur, ties[0])
        seen.append(cur.get(pl, 0))
    return seen


def s3_forward(ladder):
    """PR2, on walked states: every certified place, followed."""
    print("  ring     world    certified  steps walked  short walks  "
          "exponent moved")
    tot = [0, 0, 0, 0]
    for L in ladder:
        for world in ("ideal", "element"):
            cert = moved = steps = short = 0
            for seed in [{}] + [dict(v) for v, _ in
                                CT.eff_divisors(L, SEED_DEG) if v]:
                for st, lam, cost, ties in RO.walk(L, world, seed, WALK_T):
                    for pl in list(st):
                        if not st[pl]:
                            continue
                        v = undercut(L, world, st, lam, pl)[0]
                        if not v:
                            continue
                        cert += 1
                        seen = forward(L, world, st, lam, pl)
                        steps += len(seen) - 1
                        if len(seen) - 1 < FORWARD_T:
                            short += 1
                        if len(set(seen)) > 1:
                            moved += 1
                        ok(len(set(seen)) == 1,
                           "%s/%s: a certified exponent moved: %s"
                           % (L.name, world, seen))
            print("  %-8s %-8s %-10d %-13d %-12d %d"
                  % (L.name, world, cert, steps, short, moved))
            for i, v in enumerate((cert, steps, short, moved)):
                tot[i] += v
    print("  %-8s %-8s %-10d %-13d %-12d %d"
          % ("TOTAL", "", tot[0], tot[1], tot[2], tot[3]))


# ------------------------------------------------------- S4 the species
class Tally(object):
    def __init__(self):
        self.pairs = 0
        self.verdict = {}
        self.divisible = {}
        self.spec = {}
        self.why = {}          # (species, why the certificate refused) -> n
        self.dropped = {}      # (species, did the menu minimum fall?) -> n

    def add(self, sp, verdict):
        self.pairs += 1
        k = (sp, verdict)
        self.verdict[k] = self.verdict.get(k, 0) + 1


def cross_pairs(L, world, st, lam, ties):
    """Every cross-type pair of a tie set, with its species and its two core
    readings, using the source rig's own type function and classifier."""
    reads = []
    for veh in ties:
        reads.append((veh, RO.core_of(L, world, st, veh, lam),
                      CT.coarse_type(L, world, veh)))
    out = []
    for i in range(len(reads)):
        for j in range(i + 1, len(reads)):
            if reads[i][2] == reads[j][2]:
                continue
            if len(out) >= PAIR_CAP:
                TRUNC["pair-cap"] += 1
                return out
            out.append((reads[i], reads[j],
                        RO.species(L, world, reads[i][1], reads[j][1])))
    return out


def judge(L, world, st, lam, cost, a, b, sp, tally):
    """One cross-type pair: take a member, run the certificate on the OTHER
    core, and cross-check against the rejoin detector. The two must never
    agree.

    BOTH orders are tried. A separation needs only one branch to freeze the
    other's core, so testing only the branch the lemma points at would score
    UNCOVERED on pairs the lemma does cover from the other side -- and
    "uncovered" is read as "no certificate reaches this", which is a
    statement about both. The lemma's own pick is tried FIRST so that the
    reported witness is the derived one where it works: the member of the
    LOWER degree, and at equal degrees the DEEPER one, in both cases the one
    whose price its own move resets to the bottom."""
    R = L.R
    (v1, (p1, e1, r1, k1), _), (v2, (p2, e2, r2, k2), _) = a, b
    if R.deg[p1] != R.deg[p2]:
        order = [(a, b)] if R.deg[p1] < R.deg[p2] else [(b, a)]
    else:
        order = [(a, b)] if e1 > e2 else [(b, a)]
    order.append((order[0][1], order[0][0]))
    tags = []
    for first, other in order:
        vf = first[0]
        po = other[1][0]
        st2 = EC.apply_veh(st, vf)
        lam2 = R.lam_state(st2)
        v, tag, detail = undercut(L, world, st2, lam2, po)
        tags.append(tag)
        if v:
            break
    # a two-sided refusal has TWO reasons and they are usually different --
    # one branch's core is ridable where the other's is still fresh-eligible,
    # say -- so the pair is what the residual is filed under, never whichever
    # side the loop happened to end on
    why = "+".join(sorted(set(tags)))
    rj = RO.rejoins(L, world, st, v1, v2)
    # why a REJOIN can fail even where no core is starved: the taken move can
    # lower the menu MINIMUM below the tie cost, and then the other member is
    # out-competed rather than dominated (S7 attributes the drop). Read in
    # BOTH orders -- a one-sided reading would miss the drop whenever the
    # lemma happens to point at the branch that does not fall
    drop = False
    for veh in (v1, v2):
        try:
            if RO.menu_of(L, world, EC.apply_veh(st, veh))[1] < cost:
                drop = True
        except AssertionError:
            pass
    if v:
        ok(rj != "rejoin",
           "%s/%s: the certificate fired on a REJOINING %s pair -- %s"
           % (L.name, world, sp, detail))
        # the certificate is priced in the closed form, so it is also read
        # against the ENGINE's own menu at the successor: a certified place
        # must not be a minimal move there
        try:
            cost2 = RO.menu_of(L, world, st2)[1]
        except AssertionError:
            cost2 = None                  # the trimmed universe, not a verdict
        if cost2 is not None:
            ok(veh_price(L, world, st2, po, lam2) > cost2,
               "%s/%s: a certified place is a minimal move at the successor "
               "(%d against the menu's %d)"
               % (L.name, world, veh_price(L, world, st2, po, lam2), cost2))
        # the separation itself: the frozen exponent against the other
        # branch's, which seats the same place at its door
        other_e = EC.apply_veh(st, other[0]).get(po, 0)
        ok(other_e > st2.get(po, 0),
           "%s/%s: the two branches agree at the frozen place (%d vs %d)"
           % (L.name, world, other_e, st2.get(po, 0)))
        tally.add(sp, "certified")
        tally.spec.setdefault((sp, "certified"), (L.name, world, detail))
    elif rj == "rejoin":
        tally.add(sp, "rejoin")
    elif rj == "unreadable":
        tally.add(sp, "unreadable")
    else:
        # the source rig's own second question: the branches may still meet
        # after the moves a dropped door invites, and a residual is only
        # UNCOVERED once that search has missed too
        verdict = ("rejoin-delayed"
                   if RO.meets(L, world, st, v1, v2, RO.BFS_BUDGET,
                               RO.BFS_CAP) else "uncovered")
        tally.add(sp, verdict)
        if verdict == "uncovered":
            tally.spec.setdefault((sp, "uncovered"), (L.name, world, detail))
            tally.dropped[(sp, drop)] = tally.dropped.get((sp, drop), 0) + 1
            # a residual with a NAMED reason is a different object from a
            # residual with none: the first says where the certificate's
            # hypothesis fails, the second says the lemma is not enough
            tally.why[(sp, why)] = tally.why.get((sp, why), 0) + 1
    if sp == "odd-odd":
        div = R.deg[p1] % R.deg[p2] == 0 or R.deg[p2] % R.deg[p1] == 0
        key = (div, "rejoin" if rj == "rejoin" else
               ("certified" if v else "uncovered"))
        tally.divisible[key] = tally.divisible.get(key, 0) + 1
    return v


def s4_species(ladder, region, tag):
    """PR3, PR4, PR6: every cross-type pair, judged."""
    print("  ring     world    tie states  pairs  verdicts by species")
    out = {}
    for L in ladder:
        for world in ("ideal", "element"):
            tally = Tally()
            n = 0
            for st, lam in region(L, world):
                try:
                    _, cost, ties = RO.menu_of(L, world, st)
                except AssertionError:
                    continue
                if len(ties) < 2:
                    continue
                n += 1
                for a, b, sp in cross_pairs(L, world, st, lam, ties):
                    judge(L, world, st, lam, cost, a, b, sp, tally)
            out[(L.name, world)] = tally
            rows = ", ".join("%s/%s %d" % (k[0], k[1], v) for k, v
                             in sorted(tally.verdict.items()))
            print("  %-8s %-8s %-11d %-6d %s"
                  % (L.name, world, n, tally.pairs, rows or "-"))
    return out


# --------------------------------------------------- S5 the subsumption
def s5_subsume(ladder):
    """PR5: wherever an older certificate covers a declined core, the
    undercut must cover it too."""
    print("  ring     world    old certificates  undercut also fires")
    tot = [0, 0]
    for L in ladder:
        for world in ("ideal", "element"):
            old = both = 0
            for seed in [{}] + [dict(v) for v, _ in
                                CT.eff_divisors(L, SEED_DEG) if v]:
                for st, lam, cost, ties in RO.walk(L, world, seed, WALK_T):
                    if len(ties) < 2:
                        continue
                    reads = [(veh, RO.core_of(L, world, st, veh, lam))
                             for veh in ties]
                    for i, (v1, (p1, _, _, _)) in enumerate(reads):
                        for v2, (p2, _, _, _) in reads[i + 1:]:
                            verdict, _ = RO.dominated(L, world, st, v1, p2)
                            if not verdict:
                                continue
                            old += 1
                            st2 = EC.apply_veh(st, v1)
                            u, _, detail = undercut(
                                L, world, st2, L.R.lam_state(st2), p2)
                            if u:
                                both += 1
                            ok(u, "%s/%s: lemma A covers a core the undercut "
                                  "does not -- %s" % (L.name, world, detail))
            print("  %-8s %-8s %-17d %d" % (L.name, world, old, both))
            tot[0] += old
            tot[1] += both
    print("  %-8s %-8s %-17d %d" % ("TOTAL", "", tot[0], tot[1]))


# ------------------------------------------------- S7 the falling minimum
def s7_discount(ladder):
    """Where the menu MINIMUM falls, and what lowered it.

    A tie's other member is out-competed rather than dominated when the taken
    move leaves the menu CHEAPER than the tie cost, and two vehicles can do
    that. The CLOCKED-DOOR DROP: a move seating a place from exponent 0 pays
    d(T + 1) and leaves that place a next door of d*T, which is cheaper than
    what it just paid (explore_reordering.py F4). THE RIDER'S DISCOUNT,
    element world only: the rider raises a place's exponent by a, so that
    place's own door COUNT falls by a and its PRICE by d*a, with no clock move
    at all -- so a rider is not priced at its degree, it is priced at its
    degree minus the discount it hands the place it lands on. Every drop is attributed to one of the two,
    and a drop at a place OUTSIDE the vehicle's support would be a third
    mechanism -- which is the observable. Read at the first three minimal
    vehicles of each walked state, a cap that can only leave falls unseen."""
    print("  ring     world    moves  minimum fell  at the core  at a rider  "
          "elsewhere")
    tot = {}
    for L in ladder:
        for world in ("ideal", "element"):
            n = fell = core_drop = rider_drop = other = 0
            for st, lam in trajectory(L, world):
                try:
                    cost, ties = RO.menu_of(L, world, st)[1:]
                except AssertionError:
                    continue
                for veh in ties[:3]:
                    st2 = EC.apply_veh(st, veh)
                    lam2 = L.R.lam_state(st2)
                    try:
                        cost2 = RO.menu_of(L, world, st2)[1]
                    except AssertionError:
                        continue
                    n += 1
                    if cost2 >= cost:
                        continue
                    fell += 1
                    core, _, _, _ = RO.core_of(L, world, st, veh, lam)
                    # which places now offer a vehicle under the old cost
                    cheap = [pl for pl in st2
                             if veh_price(L, world, st2, pl, lam2) < cost]
                    ok(cheap, "%s/%s: the menu fell to %d and no place is "
                              "under %d" % (L.name, world, cost2, cost))
                    if any(pl == core for pl in cheap):
                        core_drop += 1
                    elif any(pl in veh for pl in cheap):
                        rider_drop += 1
                    else:
                        other += 1
                    # EVERY cheapened place, not merely one of them: an
                    # off-support place's door count cannot fall, the tick
                    # never falling and nothing having touched its exponent,
                    # so one appearing here would be a third mechanism
                    off = [pl for pl in cheap if pl not in veh]
                    ok(not off,
                       "%s/%s: the menu minimum fell at %d place(s) OUTSIDE "
                       "the move's support -- a third mechanism"
                       % (L.name, world, len(off)))
            print("  %-8s %-8s %-6d %-13d %-12d %-11d %d"
                  % (L.name, world, n, fell, core_drop, rider_drop, other))
            a = tot.setdefault(world, [0, 0, 0, 0, 0])
            for i, v in enumerate((n, fell, core_drop, rider_drop, other)):
                a[i] += v
    for world, a in sorted(tot.items()):
        print("  %-8s %-8s %-6d %-13d %-12d %-11d %d"
              % ("TOTAL", world, a[0], a[1], a[2], a[3], a[4]))


# ---------------------------------------------------------- the regions
def exhaustive(L, world):
    for v, _ in CT.eff_divisors(L, SCAN_DEG[L.name]):
        st = dict(v)
        yield st, L.R.lam_state(st)


def trajectory(L, world):
    for seed in [{}] + [dict(v) for v, _ in CT.eff_divisors(L, SEED_DEG) if v]:
        for st, lam, cost, ties in RO.walk(L, world, seed, WALK_T):
            yield st, lam


def main():
    ladder = CT.build_ladder()

    section("S1  THE POSITIVE CONTROL")
    print("(a) THE DOOR ARITHMETIC AND THE TICK RECURRENCE")
    s1a_arithmetic(ladder)
    print("\n(b) THE CERTIFICATE DETECTOR: what it must refuse")
    s1b_detector(ladder)
    print("\n(c) THE EXPONENT SHAPE ALONG IDEAL WALKS")
    s1c_shape(ladder)
    print("\n(d) THE CENSUS PATH AGAINST THE CERTIFICATE PATH")
    s1d_census_path(ladder)

    section("S2  THE FREEZE CENSUS")
    print("  How much of the place universe the certificate freezes, and")
    print("  what stays LIVE -- the places still able to move an exponent.")
    print("\n  the exhaustive region")
    s2_census(ladder, exhaustive)
    print("\n  the trajectory region")
    s2_census(ladder, trajectory)

    section("S3  THE FORWARD CHECK")
    print("  Every certified place followed along the canonical")
    print("  continuation: the lemma says the exponent never moves again.")
    s3_forward(ladder)

    section("S4  THE SPECIES VERDICTS")
    print("  the exhaustive region")
    ex = s4_species(ladder, exhaustive, "exhaustive")
    print("\n  the trajectory region")
    tr = s4_species(ladder, trajectory, "trajectory")

    print("\n  SPECIES TOTALS over both regions, by world -- the aggregates")
    print("  every claim about a species quotes, summed here and not by hand")
    tot = {}
    for table in (ex, tr):
        for (name, world), tally in table.items():
            for (sp, verdict), n in tally.verdict.items():
                key = (sp, world, verdict)
                tot[key] = tot.get(key, 0) + n
    for sp in sorted(set(k[0] for k in tot)):
        for world in ("ideal", "element"):
            row = [(k[2], v) for k, v in sorted(tot.items())
                   if k[0] == sp and k[1] == world]
            if row:
                print("  %-10s %-8s %-5d %s"
                      % (sp, world, sum(v for _, v in row),
                         ", ".join("%s %d" % r for r in row)))

    print("\n  WHY the uncovered residual is uncovered -- BOTH branches'")
    print("  refusals, since a residual means neither of them certifies")
    why = {}
    for tag, table in (("exhaustive", ex), ("trajectory", tr)):
        for (name, world), tally in sorted(table.items()):
            if tally.why:
                print("  %-8s %-8s %-12s %s"
                      % (name, world, tag, dict(sorted(tally.why.items()))))
            for k, v in tally.why.items():
                why[k] = why.get(k, 0) + v
    print("  TOTAL by species and reason, %d residual pairs:"
          % sum(why.values()))
    for k, v in sorted(why.items()):
        print("    %-10s %-24s %d" % (k[0], k[1], v))
    # the three-way roll-up every claim about the residual quotes, summed
    # here rather than by hand
    hard = sum(v for k, v in why.items() if "no-undercut" in k[1])
    ride = sum(v for k, v in why.items()
               if "ridable" in k[1] and "no-undercut" not in k[1])
    el = sum(v for k, v in why.items()
             if "ridable" not in k[1] and "no-undercut" not in k[1])
    print("  by REASON: %d refused for the rider's reach, %d for a core that"
          % (ride, el))
    print("  can still be seated fresh, and %d for a cheapest witness that "
          "does not" % hard)
    print("  clear the SLACK -- which is not the same as having none, and "
          "the last")
    print("  group is read off the pairs in explore_the_twelve.py")

    print("\n  ODD-ODD by divisibility of the two degrees")
    for tag, table in (("exhaustive", ex), ("trajectory", tr)):
        for (name, world), tally in sorted(table.items()):
            if tally.divisible:
                print("  %-8s %-8s %-12s %s"
                      % (name, world, tag, dict(sorted(tally.divisible.items()))))

    section("S5  THE SUBSUMPTION")
    print("  Every core the older certificate covers, run through the")
    print("  undercut: the two are one argument or they are not.")
    s5_subsume(ladder)

    section("S7  WHERE THE MENU MINIMUM FALLS")
    s7_discount(ladder)

    print("\n  the UNCOVERED residual against a fallen minimum")
    for tag, table in (("exhaustive", ex), ("trajectory", tr)):
        for (name, world), tally in sorted(table.items()):
            if tally.dropped:
                print("  %-8s %-8s %-12s %s"
                      % (name, world, tag, dict(sorted(
                          tally.dropped.items(), key=lambda kv: str(kv[0])))))

    section("S6  THE SEPARATION SPECIMENS")
    for tag, table in (("exhaustive", ex), ("trajectory", tr)):
        for (name, world), tally in sorted(table.items()):
            for key in sorted(tally.spec):
                print("  %-8s %-8s %-12s %-22s %s"
                      % (name, world, tag, "%s/%s" % key, tally.spec[key][2]))

    print()
    print("  where the search stopped short: %s" % TRUNC)
    print("  (a pair cap only hides pairs and a short forward check only")
    print("  shortens a walk; neither can manufacture a verdict)")
    print("\n%d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
